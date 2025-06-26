from helpers.validation import is_valid_year, is_valid_rating
from helpers.color import Color

def get_valid_year(prompt):
    while True:
        try:
            year = int(input(prompt))
            if is_valid_year(year):
                return year
            else:
                print(Color.red("Year must be between 1888 and 2100."))
        except ValueError:
            print(Color.red("Invalid year! Please enter a number."))


def get_valid_rating(prompt):
    while True:
        try:
            rating = float(input(prompt))
            if is_valid_rating(rating):
                return rating
            else:
                print(Color.red("Rating must be between 0 and 10."))
        except ValueError:
            print(Color.red("Invalid rating! Please enter a number."))


def get_movie_name(prompt):
    """ This function prompts the user to enter the movie title and return movie title """
    return input(Color.green(prompt)).title()

def get_valid_menu_choice(number_of_allowed_choice):
    """ Get and validate user choice from the menu. """
    while True:
        try:
            user_choice = int(input(Color.green(
                f'Enter choice (0-{number_of_allowed_choice - 1}):'
            )))
            if  -1 < user_choice < number_of_allowed_choice:
                return user_choice
            raise ValueError(f'Number out of range')

        except ValueError as e:
            if str(e) == 'Number out of range':
                print(Color.red(
                    f'Please enter a number between 1 and '
                    f'{number_of_allowed_choice - 1}'
                ))
            else:
                print(Color.red('Invalid choice! Please write a number.'))

