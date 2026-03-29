"""
# Module 7:
# Course Number Lookup
# Jeremy Matthews
# Colorado State University Global
# CSC500– Principles of Programming
# Dr. Douglas Mujeye
# Due Date: 03/29/26
# 
# Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where the courses meet. 
# The dictionary should have the following key-value pairs:
# 
# Key-Value Pairs: Room Number
# _________________________
# | Course # | Room Number |
# |------------------------|
# | (Key)    | (value)     |
# |------------------------|
# | CSC101   |    3004     |
# |------------------------|
# | CSC102   |    4501     |
# |------------------------|
# | CSC103   |    6755     |
# |------------------------|
# | NET110   |    1244     |
# |------------------------|
# | COM241   |    1411     |
# |------------------------|
# 
# The program should also create a dictionary containing course numbers and the names of the instructors that teach each course. 
# The dictionary should have the following key-value pairs:
# 
# Key-Value Pairs: Instructors
# ________________________
# | Course # | Instructor |
# |-----------------------|
# | (key)    |  (value)   |
# |-----------------------|
# | CSC101   |   Haynes   |
# |-----------------------|
# | CSC102   |  Alvarado  |
# |-----------------------|
# | CSC103   |    Rich    |
# |-----------------------|
# | NET110   |   Burke    |
# |-----------------------|
# | COM241   |    Lee     |
# |-----------------------|
# 
# The program should also create a dictionary containing course numbers and the meeting times of each course. 
# The dictionary should have the following key-value pairs:
# 
# Key-Value Pairs: Meeting Time
# Course Number (key)
# __________________________
# | Course # | Meeting Time |
# |-------------------------|
# | (key)    | (value)      |
# |-------------------------|
# | CSC101     | 8:00 a.m.  |
# |-------------------------|
# | CSC102     | 9:00 a.m.  |
# |-------------------------|
# | CSC103     | 10:00 a.m. |
# |-------------------------|
# | NET110     | 11:00 a.m. |
# |-------------------------|
# | COM241     | 1:00 p.m.  |
# |-------------------------|
# The program should let the user enter a course number and then it should display the course's room number, instructor, and meeting time.
"""

# Course information dictionaries
room_numbers = {
    'CSC101': 3004,
    'CSC102': 4501,
    'CSC103': 6755,
    'NET110': 1244,
    'COM241': 1411
}

instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

meeting_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

def main():
    """Prompt the user for a course number and display its details."""
    while True:
        try:
            # Get course number from user
            course = input('Enter a course number: ').strip().upper()
        except (EOFError, KeyboardInterrupt):
            print('\nNo input received. Exiting.')
            return

        # Validate that input is not empty before lookup
        if not course:
            print('No input entered. Please try again.')
            continue

        # Validate that input follows a course number format (letters + digits)
        if not course[:3].isalpha() or not course[3:].isdigit():
            print(f'"{course}" is not a valid course number format. '
                  'Expected format: letters followed by digits (e.g., CSC101).')
            continue

        # Look up and display course info using .get() for safe dictionary access
        room = room_numbers.get(course)
        instructor = instructors.get(course)
        meeting_time = meeting_times.get(course)

        if room and instructor and meeting_time:
            print(f'Room Number:   {room}')
            print(f'Instructor:    {instructor}')
            print(f'Meeting Time:  {meeting_time}')
            break
        elif room is not None:
            print(f'Incomplete data found for "{course}".')
            break
        else:
            valid_courses = ', '.join(room_numbers.keys())
            print(f'"{course}" was not found. '
                  f'Valid courses: {valid_courses}')


if __name__ == '__main__':
    main()


"""
---Sample output — valid entry:---
Enter a course number: csc101
Room Number:   3004
Instructor:    Haynes
Meeting Time:  8:00 a.m.

---Sample output — invalid entry:---
Enter a course number: 101
"101" is not a valid course number format. Expected format: letters followed by digits (e.g., CSC101).
Enter a course number: csc1001
"CSC1001" was not found. Valid courses: CSC101, CSC102, CSC103, NET110, COM241
"""