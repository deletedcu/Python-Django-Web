print ("\n")
students = [
	{'first_name': 'Michael', 'last_name': 'Jordan'},
	{'first_name': 'John', 'last_name': 'Rosales'},
	{'first_name': 'Mark', 'last_name': 'Guillen'},
	{'first_name': 'KB', 'last_name': 'Tonel'}
]
for dict in students:
	print (dict['first_name'] + " " + dict['last_name'])

print("\n")
users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }



for key,data in users.items():
	index = 1
	print key
	for value in data:		
		count_chars = len(value['first_name']) + len(value['last_name'])
		print str(index) + ' - ', value['first_name'], value['last_name'], count_chars
		index = index + 1
	