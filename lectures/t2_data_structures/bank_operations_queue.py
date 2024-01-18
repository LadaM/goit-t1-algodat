import random
from queue import Queue


class Client:
    def __init__(self, name):
        self.name = name
        self.operations = random.randint(1, 5)  # Випадкова кількість операцій


class Bank:
    def __init__(self):
        self.clients = Queue()

    def new_client(self, client):
        self.clients.put(client)

    def serve_clients(self):
        while not self.clients.empty():
            current_client = self.clients.get()
            print(
                f"Обслуговуємо клієнта {current_client.name} з {current_client.operations} операцій"
            )
            # Тут можна додати час обслуговування та іншу логіку


# Створюємо банк
bank = Bank()

# Додаємо клієнтів
for i in range(5):
    bank.new_client(Client(f"Client-{i}"))

# Обслуговуємо клієнтів
bank.serve_clients()
