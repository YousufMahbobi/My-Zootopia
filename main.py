from helpers.color import Color
from helpers.input import (get_valid_year,
                           get_valid_rating,
                           get_movie_name,
                           get_valid_menu_choice
                           )
from service import get_unique_movie_name, get_existing_movie_name
from movie_storage import (insert_movie,
                           delete_movie,
                           update_movie,
                           get_movies_list,
                           get_random_movie,
                           search_movie
                           )
from movies_analytics import (calculate_movies_status,
                              calculate_movies_by_rating
                             )




def display_menu():
    """ This function displays the menu, get the user choice and call the menu action """
    print('Menu:')
    menu_list = (
        '0. Exit',
        '1. List movies',
        '2. Add movie',
        '3. Delete movie',
        '4. Update movie',
        '5. Stats',
        '6. Random movie',
        '7. Search movie',
        '8. Movies sorted by rating'
    )

    for item in menu_list:
        print(Color.cyan(item))

    print('') # Blank line after menu
    menu_length = len(menu_list)
    user_menu_choice = get_valid_menu_choice(menu_length)
    call_menu_action(user_menu_choice)
    print('') # Blank line before showing result


def show_movie_list():
    """ get the movies list and total movies and print it on the screen """
    total_movies, movies = get_movies_list()
    print(f'Total movies {total_movies}')

    for movie_name, movie_details in movies:
        print(f'{movie_name} ({movie_details['year']}): {movie_details["rate"]} ')


def add_movie():
    """
        prompt the user to enter the movie title, year, and rating and call the insert_movie
        function to add a new movie to the dictionary of dictionaries. finally it prints
        success message to the user
    """
    movie_name =  get_unique_movie_name()
    movie_year = get_valid_year(Color.green('Enter new movie year:'))
    movie_rating = get_valid_rating(Color.green('Enter new movie rating (0-10):'))
    message = insert_movie(movie_name, movie_rating, movie_year)
    print(message)


def delete_movie_interface():
    """ prompts the user to enter existing movie from the catalog and delete that movie. """
    movie_name = get_existing_movie_name()
    if movie_name:
        response = delete_movie(movie_name)
        print(response)


def edit_movie():
    """ prompts the user to enter existing movie from the catalog and prompt the user to enter
    rate and year. call update_movie to update the movie and print success message """
    movie_name = get_existing_movie_name()
    if movie_name:
        movie_rate = get_valid_rating(Color.green('Enter movie rating (0-10):'))
        response = update_movie(movie_name, movie_rate)
        print(response)


def get_movie_status():
    """ get the movie status from by calling the show_movie function and print the movie status """
    response = calculate_movies_status()
    print(response)


def show_random_movie():
    """ get the random movie from show_random_movie function and print it """
    response = get_random_movie()
    print(response)


def prompt_user_search():
    """ prompt the user search a movie then the function call search movies to get the movie if exists and
        return the movie and it's rating to the user
    """
    user_searched_query = get_movie_name(Color.green('Enter part of movie name:'))
    response = search_movie(user_searched_query)
    print(response)


def get_movie_by_rating():
    """ get the movie from the calculate_movies_by_rating function and print them to the user
    """
    response = calculate_movies_by_rating()
    if type(response) is str:
        print(response)
    else:
        for movie_name, movie_info in response.items():
            print(f'{movie_name} ({movie_info['year']}), {movie_info['rate']}')


def call_menu_action(user_choice):
    """ This function calls the menu action.
     :param user_choice: user choice from the menu."""
    if user_choice == 0:
        print('Bye!')
        exit()
    if user_choice == 1:
        show_movie_list()
    elif user_choice == 2:
        add_movie()
    elif user_choice == 3:
        delete_movie_interface()
    elif user_choice == 4:
        edit_movie()
    elif user_choice == 5:
        get_movie_status()
    elif user_choice == 6:
        show_random_movie()
    elif user_choice == 7:
        prompt_user_search()
    elif user_choice == 8:
        get_movie_by_rating()
    else:
        print(Color.red('Invalid choice!'))


def main():
    print('*' * 10, 'My Movies Database', '*' * 10)
    print('') # Blank line after the title
    while True:
        display_menu()

        print('') # Blank line before continue
        input(Color.blue('Press enter to continue'))
        print('') # Blank line before continue

if __name__ == "__main__":
    main()