import socket
import threading
import json
import time


class EBGPRouter:
    def __init__(self, ip, as_number, port):
        self.ip = ip
        self.as_number = as_number
        self.port = port
        self.neighbors = {}  # neighbor IP is key and AS number is value
        self.routes = []  # list of routes advertised by this router
        self.routing_table = {}  # routing table mapping prefixes to paths

    def add_neighbor(self, neighbor_ip, neighbor_as, neighbor_port):
        self.neighbors[neighbor_ip] = (neighbor_as, neighbor_port)

    def advertise_route(self, route):
        self.routes.append(route)
        # update routing table with this new route, assuming self path is the best
        self.routing_table[route] = [self.as_number]
        for neighbor in self.neighbors:
            self.send_route(route, neighbor, self.ip)

    def send_route(self, route, neighbor_ip, source_ip):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                neighbor_as, neighbor_port = self.neighbors[neighbor_ip]
                s.connect((neighbor_ip, neighbor_port))  # use the neighbor's port
                route_info = json.dumps({"route": route, "as_number": self.as_number, "source_ip": source_ip})
                s.sendall(route_info.encode('utf-8'))
                print(f"as {self.as_number} sending route to {neighbor_ip}")
            except ConnectionRefusedError:
                print(f"Connection to {neighbor_ip} refused")

    def routing_decision(self, route_info, route):
        # update routing table if new or shorter path (w/o blockchain validation)
        if route not in self.routing_table or len(self.routing_table[route]) > len(route_info['path']) + 1:
            self.routing_table[route] = [self.as_number] + route_info.get('path', [])

    def handle_client(self, connection, address):
        try:
            with connection:
                received_data = connection.recv(1024).decode('utf-8')
                if received_data:
                    route_info = json.loads(received_data)
                    route = route_info['route']
                    as_number = route_info['as_number']
                    source_ip = route_info.get('source_ip', address[0])
                    print(f"AS {self.as_number} received route {route} from AS {as_number}")

                    # would be overwritten in securebgp router
                    self.routing_decision(route_info, route)

                    # forward to all neighbors except the source
                    for neighbor_ip in self.neighbors:
                        neighbor_as, neighbor_port = self.neighbors[neighbor_ip]
                        if neighbor_as != as_number:  # check to avoid sending back to the source
                            self.send_route(route, neighbor_ip,self.ip)

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
        listener_thread = threading.Thread(target=self.listen_for_routes)
        listener_thread.start()

"""
    TEST METHODS
"""
def setup_routers():
    router1 = EBGPRouter('127.0.0.1', 65001, 5001)
    router2 = EBGPRouter('127.0.0.1', 65002, 5002)
    router3 = EBGPRouter('127.0.0.1', 65003, 5003)

    router1.add_neighbor('127.0.0.1', 65002, 5002)  # r1 -> r2
    router2.add_neighbor('127.0.0.1', 65001, 5001)  # r2 -> r1
    router2.add_neighbor('127.0.0.1', 65003, 5003)  # r2 -> r3
    router3.add_neighbor('127.0.0.1', 65002, 5002)  # r3 -> r2

    return router1, router2, router3
def start_routers(routers):
    for router in routers:
        router.start()
def verify_routes(routers, advertised_route):
    time.sleep(2)
    for router in routers:
        if advertised_route in router.routing_table:
            print(f"Router AS{router.as_number} knows about route {advertised_route}")
        else:
            print(f"Router AS{router.as_number} does NOT know about route {advertised_route}")

# test
router1, router2, router3 = setup_routers()
start_routers([router1, router2, router3])
router1.advertise_route("192.168.1.0/24")
verify_routes([router1, router2, router3], "192.168.1.0/24")
