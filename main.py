#from phone import Phone
from keyboard import Keyboard

item1 = Keyboard("MyItem", 750, 6)

item1.apply_discount()

print(item1.price)
item1.send_email()