import argparse

import read_recipes
import menu
import filter_recipes
import sort_list
import datetime_utils


def main(args):
    max_persons = args.max_persons
    start_date = datetime_utils.parse_time(args.start)
    
    recipes = read_recipes.get_recipes()
    recipes = sort_list.sort_recipes(recipes, by='title')
    recipes = filter_recipes.filter_recipes(recipes, max_persons=max_persons)
    
    menu_list = menu.build_menu(recipes, start_date.date)  # Notion: get date from datetime
    menu.save_menu(menu_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build your weekly menu')  # Notion: use argparse
    parser.add_argument('start')
    
    args = parser.parse_args()
