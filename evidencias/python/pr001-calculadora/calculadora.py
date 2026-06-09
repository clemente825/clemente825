# ------------------------------------------------
def demanarUnNombre(missatge="Entra el nombre: "):
    while(True):    # Bucle infinit!! SEMPRE HA D'EXISTIR UN EXIT!!!
        print(f"{missatge}", end="")
        try:
            nombreDemanat = float(input())
        except ValueError:
            print("\tERROR! Cal introduir nombres vàlids!")
            continue
        return nombreDemanat
# ------------------------------------------------
def demanarNombres():
        priNomDemanat=demanarUnNombre("Entra el primer nombre:")
        segNomDemanat=demanarUnNombre("Entra el segon nombre:")
        return priNomDemanat, segNomDemanat
# ------------------------------------------------
def suma(priNumSuma, segNumSuma):
    """
    Calcula la suma de dos nombres.

    :param priNumSuma: primer nombre (float)
    :param segNumSuma: segon nombre (float)
    :return: el resultat de la suma (float)
    """
    return priNumSuma + segNumSuma
# ------------------------------------------------
def resta(priNumResta, segNumResta):
    """
    Calcula la resta de dos nombres.

    :param priNumResta: primer nombre (float)
    :param segNumResta: segon nombre (float)
    :return: el resultat de la resta (float)
    """
    return priNumResta - segNumResta
# ------------------------------------------------
def producte(priNumProd, segNumProd):
    """
    Calcula el producte de dos nombres.

    :param priNumProd: primer nombre (float)
    :param segNumProd: segon nombre (float)
    :return: el resultat del producte (float)
    """
    return priNumProd * segNumProd
# ------------------------------------------------
def divisio(priNumDiv, segNumDiv):
    """
    Calcula la divisió de dos nombres. Retornará None si s'intenta dividir per zero.

    :param priNumDiv: conté el primer nombre de la divisió (float)
    :param segNumDiv: conté el segon nombre de la divisió (float)
    :return: el resultat de la divisió (float)
    """
    if(segNumDiv==0):
        print("No es pot dividir per zero")
        return None # No hi ha resultat de la divisió
    return priNumDiv / segNumDiv
# ------------------------------------------------
def esParell(nomRebut):
    """
    Comprova si un nombre és parell.

    :param nomRebut: nombre a comprovar (float)
    :return: "parell" si és parell, "senar" si no és parell (str)
    """
    return (nomRebut % 2==0)
# ------------------------------------------------
def esPositiu(numeroRebut):
    """
    Comprova si un nombre és positiu.

    :param numeroRebut: nombre a comprovar (float)
    :return: "positiu" si és positiu, "negatiu" si no és positiu (str)
    """
    return "positiu" if numeroRebut >= 0 else "negatiu"
# ------------------------------------------------

qtatOpcions = 6

primerNombre = float()
segonNombre = float()
resultatOperacio = float()
opcioEscollida = int()
opcioEscollidaText = str()

llistaTextos = list()

llistaTextos = [
    "El resultat",          # Posició 0
    "de la suma",           # Posició 1
    "de la resta",          # Posició 2
    "del producte",         # Posició 3
    "de la divisió",        # Posició 4
    "El número entrat és "  # Posició 5
    ]

while(True):    # Bucle infinit!! SEMPRE HA D'EXISTIR UN EXIT!!!
    print("\n------ CALCULADORA ------")
    print("1. Suma")
    print("2. Resta")
    print("3. Producte")
    print("4. Divisió")
    print("5. Parell/Senar")
    print("6. Positiu/Negatiu")
    print("0. Sortir")
    print("-"*25)
    print("Escull una opció: ", end="")
    
    try:
        opcioEscollida = int(input())
    except ValueError:
        print("\tERROR! Cal introduir un número.")
        continue

    # if (opcioEscollida < 0 or opcioEscollida > qtatOpcions ):      # Si opció és <0 o >4
    if not (opcioEscollida >= 0 and opcioEscollida <= qtatOpcions ):  # Si opció és <0 o >4
        print(f"\tERROR! Cal que estigui entre 0 i {qtatOpcions} (ambdos inclosos)!")
        continue

    match(opcioEscollida):
        case 1:     # Vol fer una suma
            print("\n--------- SUMA ----------")
            primerNombre,segonNombre = demanarNombres()
            resultatOperacio = suma(primerNombre,segonNombre)

        case 2:      # Vol fer una resta
            print("\n--------- RESTA ---------")
            primerNombre,segonNombre = demanarNombres()
            resultatOperacio = resta(primerNombre,segonNombre)

        case 3:   # Vol fer un producte
            print("\n------- PRODUCTE --------")
            primerNombre,segonNombre = demanarNombres()
            resultatOperacio = producte(primerNombre,segonNombre)

        case 4:   # Vol fer una divisió
            print("\n-------- DIVISIÓ --------")
            primerNombre,segonNombre = demanarNombres()
            resultatOperacio = divisio(primerNombre,segonNombre)

        case 5:   # Vol coneixer si és parell o senar
            print("\n----- PARELL/SENAR ------")
            primerNombre = demanarUnNombre()
            resultatOperacio = esParell(primerNombre)
            
        case 6:   # Vol coneixer si és positiu i negatiu
            print("\n------- POSITIU -------")
            resultatOperacio = esPositiu(primerNombre)
            
        case 0: # Vol sortir
            print("\n\tAdéu fins la propera!")
            print(  "\t"-"*21")
            exit(0)

        case _: # Cap de les anteriors
            print("Entra una opció vàlida!")

    if opcioEscollida in [1,2,3,4]:
     if  resultatOperacio != None:
        print(f"{llistaTextos[0]} {llistaTextos[opcioEscollida]} és {resultatOperacio}.")
        print("-"*25)
        # opcioEscollida = 2 primerNombre=7 segonNombre = 27
        # resultatOperacio = 20 // resta(primerNombre,segonNombre)
        # El resultat de la resta és 20.
    elif opcioEscollida in [5,6]:
        print(f"El número és {resultatOperacio}.")
        print("--------------------")

