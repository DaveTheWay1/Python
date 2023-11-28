students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for i in range(0,len(students)):
    first_name = students[i]["first_name"] 
    last_name = students[i]["last_name"]
    print(f"first_name - {first_name}, last_name - {last_name}")