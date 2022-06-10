def remember_the_milk(shopping_list: list[str]) -> list[str]:
    if not shopping_list:
        return []
    if 'milk' not in shopping_list:
        shopping_list += ['milk']
    return shopping_list
