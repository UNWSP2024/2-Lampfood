#Elliott Morris, 1/13/2026, Average Age Calculator
#This program grabs the age of 5 friends and averages them together.

def average_age():
    # Get User Input
    first_friend_age = float(input('How old is your first friend?: '))
    second_friend_age = float(input('How old is your second friend?: '))
    third_friend_age = float(input('How old is your third friend?: '))
    fourth_friend_age = float(input('How old is your fourth friend?: '))
    fifth_friend_age = float(input('How old is your fifth friend?: '))

    # Sum ages
    total_age = first_friend_age + second_friend_age + third_friend_age + fourth_friend_age + fifth_friend_age

    # Average the ages
    average_age = total_age / 5

    # Print the results
    print('The average age is:', average_age)

# Line which calls the above function.
average_age()
