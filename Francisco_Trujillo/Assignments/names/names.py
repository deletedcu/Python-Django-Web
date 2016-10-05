# '''
#     Part I
#
#     Given the following list:
#
#     students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
#     Create a program that outputs:
#
#     Michael Jordan
#     John Rosales
#     Mark Guillen
#     KB Tonel
#     Part II
#
#     Now, given the following dictionary:
#
#     users = {
#      'Students': [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#       ],
#      'Instructors': [
#          {'first_name' : 'Michael', 'last_name' : 'Choi'},
#          {'first_name' : 'Martin', 'last_name' : 'Puryear'}
#       ]
#      }
#     Create a program that prints  the following format (including number of characters in each combined name):
#
#     Students
#     1 - MICHAEL JORDAN - 13
#     2 - JOHN ROSALES - 11
#     3 - MARK GUILLEN - 11
#     4 - KB TONEL - 7
#     Instructors
#     1 - MICHAEL CHOI - 11
#     2 - MARTIN PURYEAR - 13


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}]

for dict in students:
    print(" {} {}"). format(dict['first_name'], dict['last_name'])
print ('\n')


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

for user_item, user_list in users.iteritems():
    print user_item
    counter= 0
    for user in user_list:
        counter+=1
        print("{} - {} {} - {}").format(
            str(counter),
            user['first_name'].upper(),
            user['last_name'].upper(),
            (len(user['first_name'])+ len(user['last_name'])))
