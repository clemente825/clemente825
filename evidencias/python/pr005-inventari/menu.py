# Definició constants
CARACTER_PER_DEFECTE = "-"
AMPLE_MENU = 50

def mostrarInventari(inventari):
    """
    Mostra tots els ordinadors de l'inventari.

    :param inventari: és la llista de diccionaris amb els ordinadors.
        Tipus list

    :return: no retorna res.
    """
    # Definició de variables
    i = int()
    ordinador = dict()
    # Inicialització de variables
    i = 1
    # Comprovar si l'inventari està buit
    if len(inventari) == 0:
        print("No hi ha ordinadors a l'inventari.")
    else:
        # Recórrer inventari
        for ordinador in inventari:
            print(f"Ordinador #{i}")
            print("------------------------------")
            print(f"Nom: {ordinador['nom']}")
            print(f"CPU: {ordinador['cpu']}")
            print(f"RAM: {ordinador['ram']} GB")
            print("------------------------------")
            # Incrementar comptador
            i = i + 1

def mostrarLlista(llistaAMostrar):
    # Bucle per mostrar la llista
    for elementDeLaLlista in llistaAMostrar:
        print(elementDeLaLlista)

def carregarMenu(fitxerAObrir="menu.txt"):
  """
  Carrega les opcions del menú des del fitxer rebut.

  :param fitxerAObrir: és el nom del fitxer a obrir.
      Tipus str
      OPCIONAL, valor per defecte "menu.txt"

  :return: retorna una llista amb totes les opcions del menú.
      Tipus list
  """
  # Definició de variables
  opcionsMenu = list()
  liniesFitxer = list()
  liniaFitxer = str()
  fitxer = object()
  # Inicialització de variables
  opcionsMenu = []
  # Obrir fitxer
  fitxer = open(fitxerAObrir, "r")
  # Llegir línies
  liniesFitxer = fitxer.readlines()
  # Tancar fitxer
  fitxer.close()
  # Recórrer línies
  for liniaFitxer in liniesFitxer:
      # Eliminar \n
      liniaFitxer = liniaFitxer.strip()
      # Afegir opció a la llista
      opcionsMenu.append(liniaFitxer)
  # Retornar llista
  return opcionsMenu

def pintaTitolEsquerra(cadenaRebuda,
                       mida=AMPLE_MENU):
    """
    Pinta la cadena rebuda (de tipus cadena) alineada a l'esquerra.
    :param cadenaRebuda: És obligatori - Tipus str
        És la cadena a mostrar.
    :param mida: És la mida a on cal alinear a l'esquerra la cadena rebuda. (int)
        Tipus int
        OPCIONAL, valor per defecte AMPLE
    :return: no retorna res.
    """
    # Definició de variables
    midaCadena = int()
    qtatEspais = int()
    # Inicialització de variables
    midaCadena = len(cadenaRebuda)
    qtatEspais = mida - midaCadena
    print(f"{cadenaRebuda}{" "*qtatEspais}")

def pintaTitolDreta(cadenaRebuda,
                    mida = AMPLE_MENU,
                    caracter = "-"):
    """
    Pinta la cadena rebuda (de tipus cadena) alineada a la dreta.
    :param cadenaRebuda: És obligatori - Tipus str
        És la cadena a mostrar.
    :param mida: És la mida a on cal alinear a la dreta la cadena rebuda. (int)
        OPCIONAL, valor per defecte AMPLE
    :param caracter: És el caràcter a pintar per alinear la cadena rebuda. (str)
        OPCIONAL, valor per defecte "-"
    :return: no retorna res.
    """
    # Definició de variables
    qtatEspais = int()
    # Inicialització de variables
    qtatEspais = mida - len(cadenaRebuda)
    print(f"{caracter * qtatEspais}{cadenaRebuda}")

def pintaTitolCentrat(cadenaRebuda,mida=AMPLE_MENU, caracter="-"):
    """
    Pinta la cadena rebuda (de tipus cadena) centrada a la mida rebuda.
    :param cadenaRebuda: És obligatori - Tipus str
        És la cadena a mostrar. En aquest cas centrada a la mida rebuda.
    :param mida: És la mida a on cal centrar la cadena rebuda. (int)
        OPCIONAL, valor per defecte AMPLE
    :param caracter: És el caràcter a pintar per centrar la cadena rebuda.
        Tipus str
        OPCIONAL, valor per defecte "-"
    :return: no retorna res.
    """
    # Definició de variables
    midaTitol = int()
    qtatEspais = int()
    qtatEspaisAbans = int()
    qtatEspaisDespres = int()

    # Inicialització de variables
    cadenaRebuda = f"  {cadenaRebuda}  "
    midaTitol = len(cadenaRebuda)
    qtatEspais = mida - midaTitol
    qtatEspaisAbans = qtatEspais // 2
    qtatEspaisDespres = qtatEspais - qtatEspaisAbans
    print(f"{caracter*qtatEspaisAbans}{cadenaRebuda}{caracter*qtatEspaisDespres}")

def pintaLinia(caracter=CARACTER_PER_DEFECTE, mida=AMPLE_MENU):
    """
    Pinta una línia de caracters (str) rebuts i de mida rebuda (int)
    :param caracter: És obligatori (str)
        És el caràcter per pintar la línia.
        OPCIONAL, valor per defecte CARACTER
    :param mida: És la mida de la línia a pinta. (int)
        OPCIONAL, valor per defecte AMPLE
    :return: no retorna res.
    """
    print(caracter*mida)

def pintaMenu(llistatOpcions,
              titol,
              missEntraOpcio="Escull una opció: "):
    """
    Pinta un menú, enumerant totes les opcions rebudes com a cadenes, a la llista 
        rebuda amb el nom llistatOpcions (list)
    :param llistatOpcions: És obligatori - Tipus list()
        És la llista d'opcions del menú.
    :param titol: És el títol del menú.
        Tipus str
    :param missEntraOpcio: És la cadena per demanar a l'usuari entrar una opció
        OPCIONAL, valor per defecte "Escull una opció: "
    :return: no retorna res.
    """
    # Definició de variables
    qtatOpcions = int()
    i = int()
    # Inicialització de variables
    pintaLinia("=")
    pintaTitolCentrat(titol)
    pintaLinia("=")
    qtatOpcions = len(llistatOpcions) # lenght
    for i in range(1,qtatOpcions):
        print(f"{i}. {llistatOpcions[i]}")
    print(f"0. {llistatOpcions[0]}")
    pintaLinia()
    print(missEntraOpcio, end="")