schedules = {
    'The Dark Knight': '18:00',
    'Harry Potter': '16:00',
    'The Lord of the Rings': '20:00',
    'The Matrix': '22:00'
}

print('We are currently showing the following movies:')
for key in schedules:
    print(key)

movie =  input("What movie do you want to watch?\n")

showtime = schedules.get(movie)
if showtime:
    print(f'{movie} is playing at {showtime}')
else:
    print('The movie is not in the schedule')