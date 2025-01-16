import random

def select_random_element(elements):
    return random.choice(elements)

items = [1, 2, 3, 4, 5, "apple", "banana"]
selected_item = select_random_element(items)

print(f"Randomly Selected Element: {selected_item}")
