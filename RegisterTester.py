"""
Rasmus Hén
Uppgift 2, WEBPROG VT18
Python 3.6.2, Windows 10
"""

import Register

#Main menu that calls the different methods depending on the user's input
def mainMenu():
    #Creates four different variables, each conatining an instance of the class "CashRegister"
    FinReg = Register.CashRegister(18)
    SweReg = Register.CashRegister(18)
    NorReg = Register.CashRegister(20)
    DenReg = Register.CashRegister(22)
    
    while True:
        action = input("\n\nMAIN MENU\nChoose one of the following:\n1 to add an item\n2 to see sold products\n3 to see number of products sold\n4 to see total amount of money made this session\n5 to see how much of this is tax\n6 to reset registers\nexit to quit\n\nType choice here: ").lower()
        #If "1": input for products, price and in what country the product in question was sold
        if action == "1":
            product = input("product: ")
            while True:
                try:
                    price = float(input("price (in Euro): "))
                    break
                except ValueError:
                    print("Wrong input type")
            while True:
                country = input("country: sweden, finland, denmark or norway?\nInput:").lower()
                #Creates different instances of the class "CashRegister" depending on the selected country
                if country == "sweden":
                    SweReg.addItem(product, price)
                    break
                elif country == "finland":
                    FinReg.addItem(product, price)
                    break
                elif country == "denmark":
                    DenReg.addItem(product, price)
                    break
                elif country == "norway":
                    NorReg.addItem(product, price)
                    break
                else:
                    print("That is not an option, try again")
                
        #If "2": Creates an instance of the class "CashRegister" that gets sold items
        elif action == "2":
            print(Register.CashRegister(0).get_soldProducts())

        #If "3": Creates an instance of the class "CashRegister" that gets number of sold products
        elif action == "3":
            print(Register.CashRegister(0).get_productsCount())

        #If "4": Creates an instance of the class "CashRegister" that gets total money
        elif action == "4":
            print(Register.CashRegister(0).get_moneyCount())

        #If "5": Creates an instance of the class "CashRegister" that gets total tax
        elif action == "5":
            print(Register.CashRegister(0).get_taxCount())

        #If "6": Asks for user input about which register to reset and then creates an instance of "CashRegister" that resets the right one
        elif action == "6":
            whatRegister = input("What register would you like to reset?\n1. Sold Products\n2. Total Money\n3. Total Tax\n4. All of the Above\n\nType choice here: ")
            if whatRegister == "1":
                print(Register.CashRegister(0).reset_soldProducts())
            if whatRegister == "2":
                print(Register.CashRegister(0).reset_moneyCount())
            if whatRegister == "3":
                print(Register.CashRegister(0).reset_taxCount())
            if whatRegister == "4":
                print(Register.CashRegister(0).reset_all_registers())

        #If "exit": Kill program      
        elif action == "exit":
            print("See you later!")
            break
        #If none of the above: print error message      
        else:
            print("That is not an option, try again")

mainMenu()
