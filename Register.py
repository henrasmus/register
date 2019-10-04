"""
Rasmus Hén
Uppgift 2, WEBPROG VT18
Python 3.6.2, Windows 10
"""


class CashRegister():
    #List to keep track of sold products
    __soldProducts = []
    #Attribute that keeps track of how much the total tax count is
    __taxCount = 0
    #Attribute that keeps track of how much the total money count is
    __moneyCount = 0
    #These attribute are class global because I don't want them to reset every time a new instance of the class is created

    def __init__(self, taxRate):
        #Attribute that keeps the taxrate divided by 100 because I want to multiply it later
        self.__taxRate = taxRate / 100

    #Method that puts the product name in the list "__soldProducts", price in "__moneyCount" and tax in "__taxCount"
    def addItem(self, product, price):
        CashRegister.__soldProducts.append(product)
        CashRegister.__moneyCount += price
        CashRegister.__taxCount += (price * self.__taxRate)

    #Method that returns the list "__soldProducts"
    def get_soldProducts(self):
        return CashRegister.__soldProducts


    #Method that returns the length of the list "__soldProducts" i.e. number of sold products       
    def get_productsCount(self):
        return len(self.__soldProducts)

    #Method that returns the attribute "__moneyCount"
    def get_moneyCount(self):
        return CashRegister.__moneyCount

    #Method that returns the attribute "__taxCount"          
    def get_taxCount(self):
        return CashRegister.__taxCount

    #Method to reset all registers and three more to reset each one
    def reset_all_registers(self):
        CashRegister.__soldProducts = []
        CashRegister.__moneyCount = 0
        CashRegister.__taxCount = 0
        return "Done!"

    def reset_soldProducts(self):
        CashRegister.__soldProducts = []
        return "Done!"

    def reset_moneyCount(self):
        CashRegister.__moneyCount = 0
        return "Done!"

    def reset_taxCount(self):
        CashRegister.__taxCount = 0
        return "Done!"
    
