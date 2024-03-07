import socket
import threading
import json
from simple_blockchain import Blockchain, Block


class EBGPRouter:
    def __init__(self, ip, as_number, port):
        self.ip = ip
        self.as_number = as_number
        self.port = port
        self.neighbors = {}  # neighbor IP is key and AS number is value
        self.routes = []  # list of routes advertised by this router

    def add_neighbor(self, neighbor_ip, neighbor_as):
        self.neighbors[neighbor_ip] = neighbor_as

    def advertise_route(self, route):
        self.routes.append(route)
        for neighbor in self.neighbors:
            self.send_route(route, neighbor)

    def send_route(self, route, neighbor_ip):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((neighbor_ip, self.neighbors[neighbor_ip]))  # use the neighbor's port
                route_info = json.dumps({"route": route, "as_number": self.as_number})
                s.sendall(route_info.encode('utf-8'))
            except ConnectionRefusedError:
                print(f"connection to {neighbor_ip} refused")

    def handle_client(self, connection, address):
        try:
            with connection:
                received_data = connection.recv(1024).decode('utf-8')
                if received_data:
                    route_info = json.loads(received_data)
                    print(f"received route {route_info['route']} from AS {route_info['as_number']}")


        except Exception as e:
            print(f"an error occurred in handle_client thread: {e}")

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
                print(f"error occurred in listen_for_routes: {e}")

    def start(self):
        listener_thread = threading.Thread(target=self.listen_for_routes)
        listener_thread.start()