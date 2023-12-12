contacts = {
    'number' : 4,
    'students' : 
        [
            {'name': 'Kipp Jennings', 'email': 'kipp@example.com'},
            {'name': 'Louis Armstrong', 'email': 'louis@example.com'},
            {'name': 'Viola Davis', 'email': 'viola@example.com'},
            {'name': 'Anne Hathaway', 'email': 'anne@example.com'},
        ]
}


print('Student emails:')
for student in contacts['students']:
    print(student['email'])