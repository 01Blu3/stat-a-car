from bs4 import BeautifulSoup
import requests


def generate_make_list():
    car_model_text = requests.get('https://www.autotrader.com/').text

    # Makes a workable beautiful soup object
    make_model_soup = BeautifulSoup(car_model_text, 'lxml')

    # Variable that will hold the list of all available model names
    model_list = []

    # Gets the list of Popular Makes
    popular_make_optgroup = make_model_soup.find('optgroup')
    pop_options = popular_make_optgroup.findAll('option')
    for pop_make in pop_options:
        # print(pop_make.text)
        model_list.append(pop_make.text)

    # Gets the list of Models for each make
    all_make_optgroup = make_model_soup.find('optgroup', label='All Makes')
    all_options = all_make_optgroup.findAll('option')
    for all_make in all_options:
        model_list.append(all_make.text)

    return model_list


updated_make_list = generate_make_list()
print(updated_make_list)
