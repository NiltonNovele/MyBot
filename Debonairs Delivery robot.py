from turtle import bgcolor 


print("Welcome to Debonairs, you are now currently chatting with the Delivery Robot.")
name = input("What is your name?\n")
print("Alright " + name + ", Check out our today's specials.")
menu = input("These are our specials for today: \n Club, Debonairs chicken, Blurb, something meaty and tripple decker.\n So what would you like to order today, " + name +"?\n")
print("Nice choice, a " + menu + " it is for you!") 
ordertype = input("Well " + name + ", which option are you taking?\n Delivery or Collect.\n")   
if ordertype == "Delivery":
    address = input("Enter your address.\n")
if ordertype == "Collect":
    number = input("Please enter your phone number.\n")
print("Thank you for ordering with Debonairs! Your order is being processed by our store.")
input("Feel free to leave a feedback or concerns below.\n")
print("Thank your helping Debonairs improve!")


    


input("Press enter to exit")
