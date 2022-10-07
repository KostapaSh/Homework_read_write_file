import os

def get_cook_book():
    dishes = []
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf8') as meal_list:
        for list in meal_list:
            getlist = list.strip()
            dishes.append(getlist)
            all_ingredients_meal = []
            meal_list_range = meal_list.readline()
            for meal_range in range(int(meal_list_range)):
                emp = meal_list.readline()
                ingredient_name, quantity, measure = emp.split(' | ')
                ingredients = {'ingredient_name' : ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                all_ingredients_meal.append(ingredients)
            cook_book[getlist] = all_ingredients_meal
            meal_list.readline()

        print(cook_book)
        print()
        return cook_book

        # get_shop_list_by_dishes(dishes, 2)
        # get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    ingredients_dict = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        for l2 in ingredients:
            if l2['ingredient_name'] in ingredients_dict.keys():
                ingredients_dict[l2['ingredient_name']]['quantity'] += l2['quantity'] * person_count
            else:
                ingredients_dict[l2['ingredient_name']] = {'measure': l2['measure'], 'quantity': l2['quantity']*person_count}

    print(ingredients_dict)


#get_cook_book()
#get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

def merge_files():
    fil_dict = {}
    str_to_file = ''
    files = ['1.txt', '2.txt', '3.txt']
    for file in files:
        with open(file, 'r', encoding='utf8') as r_file:
            file_read = r_file.read()
            row_count = file_read.count('\n') + 1
        fil_dict[r_file.name]= row_count, file_read

    sort_fil_dict = sorted(fil_dict.items(), key=lambda item: item[1])
    # print(result)

    for fil_dict_0, fil_dict_1 in sort_fil_dict:
        str_to_file += fil_dict_0 + '\n'
        for fil_dict_3 in fil_dict_1:
            str_to_file += str(fil_dict_3) + '\n'
        str_to_file += '\n'

    with open('result.txt', 'w', encoding='utf8') as w_file:
        w_file.writelines(str_to_file)



#get_cook_book()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
merge_files()