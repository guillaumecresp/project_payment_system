class Payment:
    def __init__(self, name):
        self.name = name
    def pay(self):
        print("payment accepted")
class Cash(Payment):
    def __init__(self, name):
        super().__init__(name)
class Paypal(Payment):
    def __init__(self, name):
        super().__init__(name)
class Card(Payment):
    def __init__(self, name):
        super().__init__(name)

services = [
    ["réparer maison", "10€"], ["réparer voiture", "20€"], ["réparer ordinateur", "30€"]
]
mode_de_paiement = ["espèces", "chèque", "carte bancaire"]
def main():
    while True:
        print("Bonjour veuillez insérer votre nom")
        name = input()
        print("Bonjour", name)

        print("Veuillez choisir un service")
        for i, service in enumerate(services):
            print(i, service[0], service[1])
        service = int(input())
        print("Vous avez choisi", services[service][0], services[service][1])
        print("Veuillez choisir un mode de paiement")
        for i, mode in enumerate(mode_de_paiement):
            print(i, mode)
        mode = int(input())
        print("Vous avez choisi", mode_de_paiement[mode])
        print("Voulez-vous confirmer votre paiement ?")
        print("1 oui")
        print("2 non")
        confirmation = int(input())
        if confirmation == 1:
            print("Paiement effectué")
            break
        else:
            print("Paiement annulé")
            break
if __name__ == '__main__':
    main()