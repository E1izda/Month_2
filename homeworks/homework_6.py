from blessed import Terminal

term = Terminal()

fruits_colors = {
    "Kiwi": "darkgreen",
    "Peach": "peachpuff2",
    "Cherry": "webmaroon",
    "Pear": "khaki3",
    "Lemon": "yellow2",
    "Blueberry": "steelblue4"
}

for fruit, color in fruits_colors.items():
    print(getattr(term, color) + fruit + term.normal)
