contacts = {
    'number': 4,
    'students': [
        {
            'name': 'Sarah',
            'email': 'sarah@email.com'
        },
        {
            'name': 'Mike',
            'email': 'mike@email.com'
        },
        {
            'name': 'John',
            'email': 'john@email.com'
        },
        {
            'name': 'Jessica',
            'email': 'jess@email.com'
        }
    ]
}

print('students email:')
for student in contacts['students']:
    print(f"{student['name']}: {student['email']}")