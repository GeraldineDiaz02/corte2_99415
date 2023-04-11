
import csv  # Importamos el módulo csv para poder leer el archivo .csv csv: es una biblioteca de Python que permite leer y escribir archivos en formato CSV (Comma-Separated Values), que es un formato de archivo de texto utilizado para representar datos en forma de tabla

with open('organization_data.csv', 'r', encoding='utf-8') as f:  # Abrimos el archivo en modo lectura, encoding='utf-8' al abrir un archivo en Python, nos aseguramos de que cualquier caracter que se encuentre en el archivo, independientemente del idioma, pueda ser leído correctamente por Python.
    reader = csv.reader(f)  # Creamos un objeto reader con el archivo csv, csv.reader lee los datos de un archivo CSV y los convierte en una secuencia de listas, donde cada lista representa una fila del archivo. Por defecto, csv.reader utiliza la coma como separador de campo, pero se puede especificar cualquier otro carácter.
    next(reader)  # Saltamos la primera línea que contiene las cabeceras
    companies_by_country = {}  # Creamos un diccionario vacío para almacenar las empresas por país
    for row in reader:  # Iteramos sobre cada fila del archivo csv,  row se utiliza en el bucle for para iterar sobre todas las filas del archivo y realizar diferentes operaciones en cada fila, como obtener la información de la empresa y el país de la fila actual.
        country = row[4]  # Obtenemos el país de la fila actual, 
        company_info = row[1:]  # Obtenemos la información de la empresa de la fila actual

        if country not in companies_by_country:  # Si el país no está en el diccionario, lo agregamos
            companies_by_country[country] = []
        companies_by_country[country].append(company_info)  # Agregamos la información de la empresa al país correspondiente, pero esto es opcion, .append() es un método de las listas de Python que se utiliza para agregar un elemento al final de la lista.

countries = sorted(companies_by_country.keys())  # Obtenemos una lista de los países ordenada alfabéticamente, sorted: es una función de Python que se utiliza para ordenar listas. Toma una lista y devuelve una nueva lista ordenada.
countries_dict = {i+1: country for i, country in enumerate(countries)}  # Creamos un diccionario con el número de cada país

print("Lista de países:")
for num, country in countries_dict.items():  # Imprimimos la lista de países numerada
    print(f"{num}. {country}")

selected_country_num = int(input("\nSeleccione un país (ingrese el número correspondiente): "))  # Pedimos al usuario que seleccione un país
selected_country = countries_dict[selected_country_num]  # Obtenemos el país seleccionado

companies_in_country = companies_by_country[selected_country]  # Obtenemos la lista de empresas del país seleccionado
num_companies = len(companies_in_country)  # Obtenemos el número de empresas en el país seleccionado, len() es una función integrada de Python que devuelve la longitud (número de elementos) de un objeto iterable como una lista, cadena, tupla, etc.


companies_in_country = companies_by_country[selected_country]  # Obtenemos la lista de empresas del país seleccionado

max_employees = -1  # Inicializamos la cantidad máxima de empleados en -1 para poder encontrar la máxima cantidad
min_employees = float('inf')  # Inicializamos la cantidad mínima de empleados en infinito para poder encontrar la mínima cantidad
max_company = None  # Inicializamos la empresa con más empleados en None para poder encontrar la que tenga más empleados
min_company = None  # Inicializamos la empresa con menos empleados en None para poder encontrar la que tenga menos empleados
total_employees = 0  # Inicializamos el total de empleados en 0 para poder calcular el promedio
for company in companies_in_country:  # Iteramos sobre cada empresa del país seleccionado
    num_employees = int(company[7])  # Obtenemos el número de empleados de la empresa actual
    total_employees += num_employees  # Sumamos el número de empleados al total
    if num_employees > max_employees:  # Si el número de empleados es mayor al máximo encontrado hasta el momento
        max_employees = num_employees  # Lo reemplazamos como el máximo
        max_company = company  # Guardamos la información de la empresa
    if num_employees < min_employees:  # Si el número de empleados es menor al mínimo encontrado hasta el momento
        min_employees = num_employees  # Lo reemplazamos como el mínimo
        min_company = company  # Guardamos la información de la empresa
        
print(f"___________________________________________________________________________")
print(f"\nIndice del pais de busqueda :  {selected_country_num}") #"\n" es un carácter especial que se utiliza en programación para representar un salto de línea. Se llama "carácter de nueva línea" o "carácter de retorno de carro" y se utiliza para indicar al programa que debe avanzar al inicio de la siguiente línea de texto.
print(f"\nPais de busqueda: {selected_country}")
print(f"___________________________________________________________________________")
print(f"\nEmpresa con mayor número de empleados:")
print(f"\tNombre de la empresa: {max_company[1]}") #\t es un caracter de escape que representa un tabulador horizontal en una cadena de texto. Cuando se usa en una cadena de texto, indica que se debe insertar un espacio horizontal para separar el texto. El uso común de \t es en la indentación de código y en la alineación de columnas en tablas.
print(f"\tWeb site: {max_company[2]}")
print(f"\tDescripción: {max_company[4]}")
print(f"\tFundación: {max_company[5]}")
print(f"\tIndustria: {max_company[6]}")
print(f"\tNúmero de empleados: {max_company[7]}")
print(f"___________________________________________________________________________")
print(f"\nEmpresa con menor número de empleados:")
print(f"\tNombre de la empresa:: {min_company[1]}")
print(f"\tWeb site: {min_company[2]}")
print(f"\tDescripción: {min_company[4]}")
print(f"\tFundadación: {min_company[5]}")
print(f"\tIndustria: {min_company[6]}")
print(f"\tNúmero de empleados: {min_company[7]}")
print(f"___________________________________________________________________________")
avg_employees = total_employees / len(companies_in_country)
print(f"\nPromedio de empleos: {avg_employees}")
print(f"Cantidad de empresas {selected_country}: {num_companies}")
print(f"___________________________________________________________________________")






