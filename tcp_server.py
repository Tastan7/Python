import socket
import random

# Definerer host og port
HOST = '127.0.0.1'  # Standard loopback interface adresse (localhost)
PORT = 12345        # Port at lytte til (vælg hvilken som helst tilgængelig port)

# Funktion til at håndtere klientens forespørgsel
def handle_request(command, numbers):
    if command == "Random":
        # Generer et tilfældigt tal mellem de angivende tal (fx 1 og 10)
        num1, num2 = map(int, numbers.split())
        random_number = random.randint(num1, num2)
        return str(random_number)
    elif command == "Add":
        # summet af angivne tal (fx 5+5 = 10)
        num1, num2 = map(int, numbers.split())
        result = num1 + num2
        return str(result)
    elif command == "Subtract":
        # Trække tal 2 fra tal 1 (fx 5-5 = 0)
        num1, num2 = map(int, numbers.split())
        result = num1 - num2
        return str(result)
    else:
        return "Invalid command"

# Opretter en TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Binder socket til adressen og porten
    server_socket.bind((HOST, PORT))
    
    # Lytter efter indkommende forbindelser
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        # Accepterer indkommende forbindelser
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Behandler forbindelsen
        with client_socket:
            # Modtager data fra clienten
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Parser den modtagene data
            lines = data.decode().split('\n')
            command = lines[0]
            numbers = lines[1]

            # Processer den modtagende data og sender en respons
            response = handle_request(command, numbers)
            client_socket.sendall(response.encode())
