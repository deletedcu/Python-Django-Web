# Part 1

students = [
	{'first_name': 'Michael', 'last_name' : 'Jordan'},
	{'first_name': 'John', 'last_name': 'Rosales'},
	{'first_name': 'Mark', 'last_name': 'Guillen'},
	{'first_name' : 'KB', 'last_name' : 'Tonel'}
]

count = 0
while count < len(students):
	fullname = ''
	for val in students[count].itervalues():
		fullname += val + ' '
	count += 1
	print fullname

