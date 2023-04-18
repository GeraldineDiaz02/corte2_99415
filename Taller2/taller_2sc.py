with open('organization_data.csv', 'r', encoding='utf-8') as f:
    next(f)  # Saltamos la primera línea que contiene las cabeceras
    companiesByCountry = {}  # Creamos un diccionario vacío para almacenar las empresas por país
    for line in f:  # Iteramos sobre cada línea del archivo csv
        row = line.strip().split(',')  # Convertimos la línea en una lista de valores separados por comas
        country = row[4]  # Obtenemos el país de la fila actual
        companyInfo = row[1:]  # Obtenemos la información de la empresa de la fila actual

        if country not in companiesByCountry:  # Si el país no está en el diccionario, lo agregamos
            companiesByCountry[country] = []
        companiesByCountry[country].append(companyInfo)  # Agregamos la información de la empresa al país correspondiente

countries = sorted(companiesByCountry.keys())  # Obtenemos una lista de los países ordenada alfabéticamente
countriesDict = {i+1: country for i, country in enumerate(countries)}  # Creamos un diccionario con el número de cada país

print("Lista de países:")
for num, country in countriesDict.items():  # Imprimimos la lista de países numerada
    print(f"{num}. {country}")

selectedCountryNum = int(input("\nSeleccione un país (ingrese el número correspondiente): "))  # Pedimos al usuario que seleccione un país
selectedCountry = countriesDict[selectedCountryNum]  # Obtenemos el país seleccionado

companiesInCountry = companiesByCountry[selectedCountry]  # Obtenemos la lista de empresas del país seleccionado
numCompanies = len(companiesInCountry)  # Obtenemos el número de empresas en el país seleccionado

maxEmployees = -1  # Inicializamos la cantidad máxima de empleados en -1 para poder encontrar la máxima cantidad
minEmployees = float('inf')  # Inicializamos la cantidad mínima de empleados en infinito para poder encontrar la mínima cantidad
maxCompany = None  # Inicializamos la empresa con más empleados en None para poder encontrar la que tenga más empleados
minCompany = None  # Inicializamos la empresa con menos empleados en None para poder encontrar la que tenga menos empleados
totalEmployees = 0  # Inicializamos el total de empleados en 0 para poder calcular el promedio
for company in companiesInCountry:  # Iteramos sobre cada empresa del país seleccionado
    numEmployees = int(company[7])  # Obtenemos el número de empleados de la empresa actual
    totalEmployees += numEmployees  # Sumamos el número de empleados al total
    if numEmployees > maxEmployees:  # Si el número de empleados es mayor al máximo encontrado hasta el momento
        maxEmployees = numEmployees  # Lo reemplazamos como el máximo
        maxCompany = company  # Guardamos la información de la empresa
    if numEmployees < minEmployees:  # Si el número de empleados es menor al mínimo encontrado hasta el momento
        minEmployees = numEmployees  # Lo reemplazamos como el mínimo
        minCompany = company  # Guardamos la información de la empresa

print(f"___________________________________________________________________________")
print(f"\nIndice del pais de busqueda :  {selectedCountryNum}") #"\n" es un carácter especial que se utiliza en programación para representar un salto de línea. Se llama "carácter de nueva línea" o "carácter de retorno de carro" y se utiliza para indicar al programa que debe avanzar al inicio de la siguiente línea de texto.
print(f"\nPais de busqueda: {selectedCountry}")
print(f"___________________________________________________________________________")
print(f"\nEmpresa con mayor número de empleados:")
print(f"\tNombre de la empresa: {maxCompany[1]}") #\t es un caracter de escape que representa un tabulador horizontal en una cadena de texto. Cuando se usa en una cadena de texto, indica que se debe insertar un espacio horizontal para separar el texto. El uso común de \t es en la indentación de código y en la alineación de columnas en tablas.
print(f"\tWeb site: {maxCompany[2]}")
print(f"\tDescripción: {maxCompany[4]}")
print(f"\tFundación: {maxCompany[5]}")
print(f"\tIndustria: {maxCompany[6]}")
print(f"\tNúmero de empleados: {maxCompany[7]}")
print(f"___________________________________________________________________________")
print(f"\nEmpresa con menor número de empleados:")
print(f"\tNombre de la empresa:: {minCompany[1]}")
print(f"\tWeb site: {minCompany[2]}")
print(f"\tDescripción: {minCompany[4]}")
print(f"\tFundadación: {minCompany[5]}")
print(f"\tIndustria: {minCompany[6]}")
print(f"\tNúmero de empleados: {minCompany[7]}")
print(f"___________________________________________________________________________")
avgEmployees = totalEmployees / len(companiesInCountry)
print(f"\nPromedio de empleos: {avgEmployees}")
print(f"Cantidad de empresas {selectedCountry}: {numCompanies}")
print(f"___________________________________________________________________________")






