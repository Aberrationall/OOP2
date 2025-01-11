def read_cook_book(f_path = "recepts.txt"):
    cook_book = {}
    with open(f_path, "r", encoding="utf-8") as f:
        while True:
            dish = f.readline().strip()
            if not dish:
                break
            i_count = int(f.readline().strip())
            ingredients = []
            for x in range(i_count):
                ingredient_line = f.readline().strip().split(" | ")
                ingredients.append({
                    "ingredient_name": ingredient_line[0],
                    "quantity": int(ingredient_line[1]),
                    "measure": ingredient_line[2]
                })
            cook_book[dish] = ingredients
            f.readline()
    return cook_book

f_path = "recepts.txt"
cook_book = read_cook_book(f_path)
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] *person_count
                
                if name in ingredient_list:
                    ingredient_list [name]['quantity'] += quantity
                else:
                   ingredient_list[name] = {'measure': measure,'quantity': quantity}
                    
    return ingredient_list
    
print(get_shop_list_by_dishes(['Омлет'],8))

ingredient_list = get_shop_list_by_dishes(['Утка по-пекински'], 5)
print(ingredient_list)



