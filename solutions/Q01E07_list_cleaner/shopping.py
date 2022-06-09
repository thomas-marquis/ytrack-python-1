def remember_the_milk(shopping_list: list[str]) -> list[str]:
    if not shopping_list:
        return []
    if 'milk' not in shopping_list:
        shopping_list += ['milk']
    return shopping_list


def clean_list(shopping_list: list[str]) -> list[str]:
    shopping_list = remember_the_milk(shopping_list)

    if not shopping_list:
        return shopping_list

    formatted_list = []
    for idx, item in enumerate(shopping_list):
        formatted_list.append(f'{idx+1}/ {item.title()}')
    
    return formatted_list
