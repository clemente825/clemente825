# ------------------------------------------------
def demanarUnNombre():
    while(True):    # Bucle infinit!! SEMPRE HA D'EXISTIR UN EXIT!!!
        print(f"Entra el número: ", end="")
        try:
            númeroDemanat = float(input())
        except ValueError:
            print("\tERROR! Cal introduir números vàlids!")
            continue
        return númeroDemanat
# ------------------------------------------------
def demanarNombres():
    while(True):    # Bucle infinit!! SEMPRE HA D'EXISTIR UN EXIT!!!
        print(f"Entra el primer dels números: ", end="")
        try:
            priNomDemanat = float(input())
        except ValueError:
            print("\tERROR! Cal introduir números vàlids!")
            continue
        print(f"Entra el segon dels números: ", end="")
        try:
            segNomDemanat = float(input())
        except ValueError:
            print("\tERROR! Cal introduir números vàlids!")
            continue
        return priNomDemanat, segNomDemanat
# ------------------------------------------------
def suma(priNumSuma, segNumSuma):
    """
    Calcula la suma de dos números.

    :param priNumSuma: primer número (float)
    :param segonNumeroSuma: segon número (float)
    :return: resultat de la suma (float)
    """
    resultatSuma = float()
    resultatSuma = priNumSuma + segNumSuma
    return resultatSuma
# ------------------------------------------------
def resta(priNumResta, segNumResta):
    resultatResta = float()
    ## Cal escriure les comandes per calcular la resta
    resultatResta = priNumResta - segNumResta
    return resultatResta
# ------------------------------------------------
def producte(priNumProd, segNumProd):
    resultatProducte = float()
    ## Cal escriure les comandes per calcular el producte
    resultatProducte = priNumProd * segNumProd
    return resultatProducte
# ------------------------------------------------
def divisio(priNumDiv, segNumDiv):
    resultatDivisio = float()
    ## Cal escriure les comandes per calcular la divisió
    if(segNumDiv==0):
        print("No es pot dividir per zero")
        return 0
    resultatDivisio = priNumDiv / segNumDiv
    return resultatDivisio
# ------------------------------------------------
def esParell(nomRebut):
    esParellONoEsParell = bool()
    if(nomRebut%2==0):
        esParellONoEsParell = True
    else:
        esParellONoEsParell = False
    return esParellONoEsParell
# ------------------------------------------------
def esPositiu(numeroRebut):
    esPositiu = bool()
    if(numeroRebut >= 0):
        esPositiu = True
    else:
        esPositiu = False
    return esPositiu
# ------------------------------------------------

qtatOpcions = 7

primerNombre = float()
segonNombre = float()
resultatOperacio = float()
opcioEscollida = int()
opcioEscollidaText = str()
operacioText = str()
llistaTextos = list()

# historial = []          # llista
llista_historial_dicc = []  # llista d'operacions



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
    print("7. Mostar historic")
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
            operacioText="suma"
            primerNombre,segonNombre = demanarNombres()
            resultatOperacio = suma(primerNombre,segonNombre)

        case 2:      # Vol fer una resta
            print("\n--------- RESTA ---------")
            operacioText="resta"
            primerNombre,segonNombre = demanarNombres()
            resultatOperacio = resta(primerNombre,segonNombre)

        case 3:   # Vol fer un producte
            print("\n------- PRODUCTE --------")
            operacioText="producte"
            primerNombre,segonNombre = demanarNombres()
            resultatOperacio = producte(primerNombre,segonNombre)

        case 4:   # Vol fer una divisió
            print("\n-------- DIVISIÓ --------")
            operacioText="divisio"
            primerNombre,segonNombre = demanarNombres()
            resultatOperacio = divisio(primerNombre,segonNombre)

        case 5:   # Vol coneixer si és parell o senar
            print("\n----- PARELL/SENAR ------")
            primerNombre = demanarUnNombre()
            resultatOperacio = esParell(primerNombre)
            
        case 6:   # Vol coneixer si és positiu i negatiu
            print("\n------- POSITIU -------")
            primerNombre = demanarUnNombre()
            resultatOperacio = esPositiu(primerNombre)

        case 7:     # mostar historic
            print("\n------ Historial -------")
            # print(llista_historial_dicc)
            for element in llista_historial_dicc:
                print(f"Operació => {element['operacio']}\n1r núm.  => {element['primerNombre']}\n2n núm.  => {element['segonNombre']}\nResultat => {element['resultatOperacio']}")
                print("========================")

        case 0: # Vol sortir
            print("\n\tAdéu fins la propera!")

            exit(0)

        case _: # Cap de les anteriors
            print("Entra una opció vàlida!")


    if opcioEscollida in [1,2,3,4]:
        print(f"{llistaTextos[0]} {llistaTextos[opcioEscollida]} és {resultatOperacio}.")
        print("-"*25)
        # opcioEscollida = 2 primerNombre=7 segonNombre = 27
        # resultatOperacio = 20 // resta(primerNombre,segonNombre)
        # El resultat de la resta és 20.

        # historial.append(f"{operacioText} {primerNombre} {segonNombre} {resultatOperacio}")
        # Exemple: 1 opcioEscollida=1 primerNombre=3 segonNombre=5 resultatOperacio=8
        # historial.append(f"{primerNombre} {segonNombre} {opcioEscollida} {resultatOperacio}")
        # historial["suma 3 5 8"]
        operacio = { 
                "operacio": f"{operacioText}", 
                "primerNombre" : f"{primerNombre}",
                "segonNombre" : f"{segonNombre}",
                "resultatOperacio" : f"{resultatOperacio}"
                }
        llista_historial_dicc.append(operacio)

        # Exemple: 1 opcioEscollida=1 primerNombre=3 segonNombre=5 resultatOperacio=8
        # historial.append(f"{primerNombre} {segonNombre} {opcioEscollida} {resultatOperacio}")
        # historial["suma 3 5 8"]
        
 
    elif opcioEscollida in [5,6]:
        if opcioEscollida == 5:
            if (resultatOperacio):
                print("El número és parell.")
                print("--------------------")
            else:
                print("El número és senar.")
                print("-------------------")
        elif opcioEscollida == 6:
            if (resultatOperacio):
                print("El número és positiu.")
                print("--------------------")
            else:
                print("El número és negatiu.")
                print("-------------------")