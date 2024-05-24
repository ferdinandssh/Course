from item import Item
from phone import Phone
from keyboard import Keyboard

## Initiate instance from csv
# Item.instantiate_from_csv()

item1 = Keyboard("jscKeyboard",1000,3)
item1.apply_discount()

print(item1.price)


