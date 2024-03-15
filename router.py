import socket
import threading
import json
import time
import datetime

class EBGPRouter:
    def __init__(self, ip, as_number, port):
        self.ip = ip
        self.as_number = as_number
        self.port = port
        self.neighbors = {}  # neighbor IP is key and AS number is value
        self.routes = []  # list of routes advertised by this router
        self.routing_table = {}  # routing table mapping prefixes to paths

    def add_neighbor(self, neighbor_ip, neighbor_as, neighbor_port):
        self.neighbors[neighbor_as] = (neighbor_ip, neighbor_port)

    def advertise_route(self, route):
        self.routes.append(route)
        # update routing table with this new route, assuming self path is the best
        as_path = [self.as_number]
        self.routing_table[route] = []
        for neighbor in self.neighbors:
            self.send_route(route, neighbor, self.ip, as_path)
            time.sleep(1)

    def send_route(self, route, neighbor_as, source_ip,as_path):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                neighbor_ip, neighbor_port = self.neighbors[neighbor_as]
                # print(f"AS {self.as_number} sending route {route} to {neighbor_as}")
                route_info = json.dumps(
                    {"route": route, "as_number": self.as_number, "source_ip": source_ip, "as_path": as_path})
                s.connect((neighbor_ip, neighbor_port))
                s.sendall(route_info.encode('utf-8'))
            except ConnectionRefusedError as e:
                print(f"Socket Error {e}. Connection to {neighbor_ip} refused")

    def routing_decision(self, route_info, route):
        as_path = route_info.get('as_path', [])
        # prevent routing loops: checking if this router's ASN is already in AS_PATH (redundant in default ebgp)
        if self.as_number in as_path:
            return  # loop -> ignore route

        # update routing table if the route is new or if the received AS_PATH is shorter than the current one
        if route not in self.routing_table or len(self.routing_table[route]) > len(as_path):
            self.routing_table[route] = as_path

    def log_advertisement(self, route, as_path):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp}, AS: {self.as_number}, prefix: {route}, AS_PATH: {as_path} \n"

        with open("chain.log", "a") as f:
            f.write(entry)

    def reconstruct(self, prefix):
        hist = []
        with open("chain.log", "r") as log:
            for line in log:
                if prefix in line:
                    hist.append(line.strip())
        for entry in hist:
            print(entry)
            
    def handle_client(self, connection, address):
        try:
            with connection:
                received_data = connection.recv(1024).decode('utf-8')
                if received_data:
                    route_info = json.loads(received_data)
                    route = route_info['route']
                    as_number = route_info['as_number']
                    source_ip = route_info.get('source_ip', address[0])
                    received_as_path = route_info.get('as_path', [])

                    # print(
                    #     f"AS {self.as_number} received route {route} from AS {as_number} with AS_PATH: {received_as_path}")

                    # prevent routing loop
                    if self.as_number in received_as_path:
                        # print(f"routing loop detected for route {route}, dropping advertisement")
                        return  # loop->ignore

                    new_as_path = received_as_path + [self.as_number]

                    # make a routing decision (could replace or update existing route)
                    self.routing_decision(route_info, route)

                    self.log_advertisement(route, received_as_path)

                    # forward to all neighbors except source
                    for neighbor in self.neighbors:
                        if neighbor != as_number:  # avoid sending back to the source
                            self.send_route(route, neighbor, self.ip, new_as_path)

        except Exception as e:
            print(f"An error occurred in handle_client thread: {e}")

    def listen_for_routes(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((self.ip, self.port))
                s.listen()
                while True:
                    conn, addr = s.accept()
                    client_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                    client_thread.start()
            except Exception as e:
                print(f"Error occurred in listen_for_routes: {e}")

    def start(self):
        self.listener_thread = threading.Thread(target=self.listen_for_routes)
        self.listener_thread.start()

"""

    TEST METHODS
"""
# def setup_routers():
#     router1 = EBGPRouter('127.0.0.1', 65001, 5001)
#     router2 = EBGPRouter('127.0.0.1', 65002, 5002)
#     router3 = EBGPRouter('127.0.0.1', 65003, 5003)

#     router1.add_neighbor('127.0.0.1', 65002, 5002)  # r1 -> r2
#     router2.add_neighbor('127.0.0.1', 65001, 5001)  # r2 -> r1
#     router2.add_neighbor('127.0.0.1', 65003, 5003)  # r2 -> r3
#     router3.add_neighbor('127.0.0.1', 65002, 5002)  # r3 -> r2

#     return router1, router2, router3
# def start_routers(routers):
#     for router in routers:
#         router.start()
# def verify_routes(routers, advertised_route):
#     time.sleep(2)
#     for router in routers:
#         if advertised_route in router.routing_table:
#             print(f"Router AS{router.as_number} knows about route {advertised_route}: {router.routing_table}")
#         else:
#             print(f"Router AS{router.as_number} does NOT know about route {advertised_route}")

# # test
# router1, router2, router3 = setup_routers()
# start_routers([router1, router2, router3])
# router1.advertise_route("192.168.1.0/24")
# router2.advertise_route("192.168.2.0/24")
# #verify_routes([router1, router2, router3], "192.168.1.0/24")
# #verify_routes([router1, router2, router3], "192.168.2.0/24")
# router1.reconstruct("192.168.1.0/24")

"""