def carregaDades(fitxerAObrir="dades.txt"):
    """
    Carrega els ordinadors des del fitxer rebut.

    :param fitxerAObrir: és el nom del fitxer a obrir.
        Tipus str
        OPCIONAL, valor per defecte "dades.txt"

    :return: retorna una llista de diccionaris amb els ordinadors.
        Tipus list
    """
    # Definició de variables
    inventari = list()
    fitxer = object()
    liniesFitxer = list()
    liniaFitxer = str()
    dadesOrdinador = list()
    ordinador = dict()
    # Inicialització de variables
    inventari = []
    # Obrir fitxer
    fitxer = open(fitxerAObrir, "r")
    # Llegir línies
    liniesFitxer = fitxer.readlines()
    # Tancar fitxer
    fitxer.close()
    # Recórrer línies del fitxer
    for liniaFitxer in liniesFitxer:
        # Eliminar \n
        liniaFitxer = liniaFitxer.strip()
        # Separar dades
        dadesOrdinador = liniaFitxer.split(";")
        # Crear diccionari
        ordinador = {
      "nom": dadesOrdinador[0],
      "cpu": dadesOrdinador[1],
      "ram": int(dadesOrdinador[2])
     }
        # Afegir ordinador a l'inventari
        inventari.append(ordinador)
    # Retornar inventari
    return inventari

def guardaDades(inventari, fitxerAGuardar="dades.txt"):
    fitxer = open(fitxerAGuardar, "w")

    for ordinador in inventari:
        fitxer.write(
            f"{ordinador['nom']};"
            f"{ordinador['cpu']};"
            f"{ordinador['ram']}\n"
        )

    fitxer.close()