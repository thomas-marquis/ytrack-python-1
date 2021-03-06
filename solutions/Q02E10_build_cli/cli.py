import argparse

import read_recipes
import menu
import filter_recipes
import sort_list
import datetime_utils

recipes_file = 'recipes_data.json'


def main(args):
    max_persons = args.max_persons
    start_date = datetime_utils.parse_time(args.start)

    recipes = read_recipes.get_recipes(recipes_file)
    recipes = sort_list.sort_recipes(recipes, by='title')
    recipes = filter_recipes.filter_recipes(recipes, max_persons=max_persons)
    
    menu_list = menu.build_menu(recipes, start_date.date())  # Notion: get date from datetime
    menu.save_menu(menu_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build your weekly menu')
    parser.add_argument('-s', '--start', help='menu start date with format dd/mm/YYYY', required=True)
    parser.add_argument('-p', '--max-persons', help='maximum persons for each meal', default=4, type=int)
    
    args = parser.parse_args()
    
    main(args)
