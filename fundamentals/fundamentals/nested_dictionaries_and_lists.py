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

x[1][0]=15

students[0]['last_name']='Bryant'

sports_directory['soccer'][0]='Andres'

z[0]['y']=30

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for one_student in students:
        for key in one_student:
            print(f"{key} - {one_student[key]}")

iterateDictionary(students)

def iterateDictionary(some_list):
    for i in range(0, len(some_list), 1):
        print("first_name - " + some_list[i]['first_name'], ", last_name - "+ some_list[i]['last_name'])

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for one_item in some_list:
        print(one_item[key_name])
    return one_item[key_name]

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for item in some_dict:
        print(len(item), item)
        for i in some_dict[item]:
            print(i)

printInfo(dojo)