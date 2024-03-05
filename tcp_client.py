import socket

def main():
    # Definerer server adresse og port
    server_address = ('localhost', 12345)  # Localhost og IP

    # Opretter en TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Forbinder til serveren
        client_socket.connect(server_address)

        # Beder brugeren om kommando, tal, osv.
        command = input("Enter command (Random/Add/Subtract): ")
        numbers = input("Enter two numbers separated by space: ")

        # konstruerer beskeden der skal sendes til serveren
        message = f"{command}\n{numbers}\n"

        # Sender beskeden til serveren
        client_socket.sendall(message.encode())

        # Modtager serverens svar
        response = client_socket.recv(1024)

        # Udskriver svaret
        print("Server response:", response.decode())

    except Exception as e:
        print("Error:", e)

    finally:
        # Lukker socket
        client_socket.close()

if __name__ == "__main__":
    main()
