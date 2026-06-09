import os
from menu import pintaMenu, carregarMenu, mostrarLlista
from inventari import carregaDades, guardaDades

# Programa principal
if __name__ == "__main__":
    # Definició de variables
    volSeguir = bool()
    opcionsMenu = list()
    opcioEscollida = int()
    nomOrdinador = str()
    cpuOrdinador = str()
    ramOrdinador = int()
    inventari = list()

    # Inicialització de variables
    inventari = []
    inventari = carregaDades()
    guardaDades(inventari)

    volSeguir = True
    opcionsMenu = carregarMenu()
    qtatOpcions = len(opcionsMenu)

    # Bucle per sortir quan l'usuari entri l'opció 0
    # volSeguir = False
    while(volSeguir):
        pintaMenu(opcionsMenu, "Inventari")

        try:
            opcioEscollida = int(input())
        except ValueError:
            print("\tERROR! Cal introduir un número.")
            continue
        
        # La funció input() sempre retorna un str (cadena)
        # i cal passar el str a int (enter)
        if not(opcioEscollida >= 0 and opcioEscollida < qtatOpcions):
            print(f"L'opció {opcioEscollida} no és correcte")
        else:
            match(opcioEscollida):
                case 0:     # Vol sortir
                    print(F"\n\tFins la propera!")
                    volSeguir = False

                case 1:     # Vol Afegir ordinador
                    print(f"Entra el nom de l'ordinador: ", end="")
                    nomOrdinador = input()
                    print(f"Entra la CPU de l'ordinador: ", end="")
                    cpuOrdinador = input()
                    try:
                        print(f"Entra la RAM de l'ordinador: ", end="")
                        ramOrdinador = int(input())
                    except ValueError:
                        print("\tERROR! Cal introduir un número.")
                
                    ordinador={
                        "nom": nomOrdinador,
                        "cpu": cpuOrdinador,
                        "ram": ramOrdinador
                    }
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    fitxer = open(os.path.join(script_dir, "dades.txt"), "a")
                    fitxer.write(f"{nomOrdinador};{cpuOrdinador};{ramOrdinador}\n")
                    fitxer.close()

                    inventari.append(ordinador)
                case 2: # Vol Mostra inventari
                    mostrarLlista(inventari)
                case _:
                    print("\t\tOpció encara no definida!")


    # noms = list()
    # nom = str()

    # # Omplo la llista amb 3 valors
    # noms = ["Joan", "Anna", "Marc"]

    # print(f"Mostro la llista primera")
    # mostrarLlista(noms)

    # # Afegeixo un nou valor a la llista
    # noms.append("Laura")

    # print(f"Mostro la llista amb Laura afegida:")
    # mostrarLlista(noms)

    # inventari = [] # Llista inventari (Col·lecció d'elements)

    # Diccionari => K:V (Key:value o clau:valor)

    # ordinador = {
    #     "nom": "PC01",
    #     "cpu": "i5",
    #     "ram": 16
    # }

    # print(f"Nom = {ordinador["nom"]}")
    # print(f"CPU = {ordinador["cpu"]}")
    # print(f"RAM = {ordinador["ram"]}")

    # ordinador["ram"] = 32
    # print("RAM modificada")
    # print(f"Nom = {ordinador["nom"]}")
    # print(f"CPU = {ordinador["cpu"]}")
    # print(f"RAM = {ordinador["ram"]}")

    # ordinador2 = {
    #     "nom": "PC02",
    #     "cpu": "i7",
    #     "ram": 64
    # }

    # inventari.append(ordinador)
    # inventari.append(ordinador2)

    # mostrarLlista(inventari)


    # fitxer = open("dades.txt", "r")
    # contingut = fitxer.readlines()
    # print(f"{contingut}")

    # fitxer = open("dades.txt", "a")
    # fitxer.write("\n\tHola, i tu com estas?")
    # fitxer.close()