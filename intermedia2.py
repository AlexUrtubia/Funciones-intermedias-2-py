# Cambia el valor 10 en x a 15. Una vez que haya terminado, 
    # x ahora debería ser [[5,2,3], [15,8,9]].
#Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
#En el directorio sports_directory, cambia 'Messi' a 'Andres'
#Camba el valor 20 en z a 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
x[1][0]=15
students[0]['last_name']="Bryant"
sports_directory['soccer'][0]='Andres'
z[0]['y']=30
#               2  ........................................................
# Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, 
# la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:
students1 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# ---------------------------------------------------------------------------
for elem in students1:
    print(f"first_name - {elem['first_name']}, last_name - {elem['last_name']}")
#       3 :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Obtén valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios 
# y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
def iterateDictionary2(some_value, some_list):
    for i in range (len(some_list)):
        print(some_list[i][some_value])
iterateDictionary2('first_name', students1)
iterateDictionary2('last_name',students1)
# Itera a través de un diccionario con valores de listas
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, 
# imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores 
# asociados dentro de la lista de cada clave. Por ejemplo:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_list):
    for i in some_list:
        print(len(some_list[i]),i.upper())
        for j in range (len(dojo[i])):
            print(some_list[i][j])
        print()
printInfo(dojo)
