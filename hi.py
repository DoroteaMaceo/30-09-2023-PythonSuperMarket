"""A menu driven supermarket system using python where users can add items to their list delete
items from their list and display the current items on the list"""

def ch():
    global opt
    opt = int(input("Choose an option"))


print("WELCOME TO SUPERMARKET!"
      "\nPlease note the following:"
      "\n1.Add item"
      "\n2.Remove item"
      "\n3.Display list"
      "\n4.End")
cart=[]
ch()
while True:
    if opt==1:
        cart.append(input("Enter item"))
        ch()

    elif opt==2:
        rem=(input("Remove item "))
        cart.remove(rem)
        ch()

    elif opt==3:
        print("Shopping list",cart)
        ch()
    elif opt==4:
        print("Your shopping list includes\n",cart,"\nPlease proceed to the counter")
        break

    else:
        print("Enter a valid choice")
        ch()