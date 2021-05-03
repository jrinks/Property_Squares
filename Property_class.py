#Intro:  This program takes in property info and determines if the property will be a good investment.  The program starts by instantiating a class Property which contains a dictionary which will bes used to store all user input and calculated values.  Next, there are several class methods, some take user input, some do calculations, some do both. Finally, there is a driver function which starts by giving the user a welcome message, instantiating the class, then calling each function in order. 

#---------class----------------------

#Define class object Property
class Property():
    
    #init class, take in basic property info
    def __init__(self):
        self.prop_dict = {}
  
    # input property name
    def propName(self):
        self.prop_name = input("First, give this property a name. You can use this name to refer back to this property's information later. ")
        self.prop_dict["prop_name"] = self.prop_name
    
    def propType(self):
        #property type
        self.prop_type = input("Enter property type: SF for single family, D for duplex, MU for multi-unit: ")
        if self.prop_type.upper() == "SF" or self.prop_type.upper() == "D" or self.prop_type.upper() == "MU":
            self.prop_dict["prop_type"] = self.prop_type
        else: 
            print("Please enter a valid property type")
            self.propType()

    #purchase price
    def purchPrice(self):
        while True:
            try:
                self.purch_price = int(input("Enter purchase price: "))
                self.prop_dict["purch_price"] = self.purch_price
                break
            except ValueError:
                print("Please enter a valid numerical value")
                selfpurchPrice()
    
    #num of units
    def numUnits(self):
        while True:
            try:
                self.num_units = int(input("How many units does this property have? "))
                self.prop_dict["num_units"] = self.num_units
                break
            except ValueError:
                print("Please enter a valid numerical value")
                self.numUnits()

    def unitBeds(self, unit_num):
        while True:
            try:
                self.unit_beds = int(input(f"For {unit_num}, enter number of bedrooms: "))
                self.prop_dict[(f"{unit_num}_beds")] = self.unit_beds
                break
            except ValueError:
                print("Please enter a valid numerical value")
                selfunitBeds()
    
    def unitBaths(self, unit_num):
        while True:
            try:
                self.unit_baths = int(input(f"For {unit_num}, enter number of whole baths: "))
                self.prop_dict[(f"{unit_num}_baths")] = self.unit_baths
                break
            except ValueError:
                print("Please enter a valid whole number")
                selfunitBaths()

    def unitSQFT(self, unit_num):
        while True:
            try:
                self.unit_sqft = int(input(f"For {unit_num}, enter square feet: "))
                self.prop_dict[(f"{unit_num}_sqft")] = self.unit_sqft
                break
            except ValueError:
                print("Please enter a valid whole number")
                selfunitSQFT()
    
    def perUnitRent(self, unit_num):
        self.[(f"{unit_num}_price")] = (self.prop_dict[(f"{unit_num}_beds")]) *100 + (self.prop_dict[(f"{unit_num}_baths")]) *100 + (self.prop_dict[(f"{unit_num}_sqft")])
        #print(self.[(f"{unit_num}_price")])

    # calc total monthly rent for all units combined
    def allUnitRentMo():
        #get unit rent for all units, add them up in variable self.allUnitRent
        for u in range(1, ((int(property.num_units))+1)):
            self.allUnitRent = self.allUnitRent + self.prop_dict.get[(f"{unit_num}_price")] 
        # divide by 12 to get monthly
        self.allUnitRentMo = self.allUnitRent /12      

    # calculate monthly mortgage expenses
    # add up purchase price and loan interest and divide by 12
    def calcMonthlyMort():
        # get mortgage interest
        while True:
        try:
            self.mort_intr = int(input("Enter mortgage interest ratee: "))
            self.prop_dict["mort_intr"] = self.mort_intr
            break
        except ValueError:
            print("Please enter a valid numerical value")
            selfcalcMort()
        # calculate monthly mortgage cost
        self.prop_dict["calcmonthlymort"] = (self.mort_intr + self.purch_price) / 12


    def otherMonthlyEx(self):
        self.vacancy = self.allUnitRentMo * 0.05
        self.repair = self.prop_dict.get("num_units")  * 100
        self.capex = self.prop_dict.get("num_units") * 100
        self.management = self.prop_dict("calcmonthlymort")* 0.1
        total_mo_expenses = sum(self.vacancy, self.repair, self.capex , self.management)
        self.prop_dict["other_monthly_ex"] = total_mo_expenses

    # get total monthly expenses by adding up total mortgage with total other expenses
    def TotalMonthlyEx(self):
        self.prop_dict["total_monthly_ex"] = sum( self.prop_dict.get("calcmonthlymort"),  self.prop_dict.get("otherMonthlyEx")


    #calcualte monthly cash flow by subtracting all monthly expenses from all monthly income
    def cashFlowMo(self):
        self.prop_dict["cashFlowMo"] = self.prop_dict.get("allUnitRentMo") - self.prop_dict.get("total_monthly_ex") 

    #total investment equals total mortgage plus down payment
    def totalInvestement():
        #total mortgage, interest and down payment
        pass

    #calculate cash on cash  
    def cashOnCash(self):
        #cash_on_cash = cash_flow * 12 / total_investment  
        pass

    #Finally, recommend if this is a good investment by comparing cash on cash earnings with average stock appreciation 
    def goodInvestmen():
    # if cash on cash > average stock market return:
        #good investment
    #else:
        #bad investment


#----------driver---------------
def driver():
    #welcome and give property name
    print("Welcome to the magic property calculator! Let us help determine if a potential investment property is a money maker or a money taker.  First please enter some basic information about the property. ")
    # init
    property = Property()
    # input property name
    property.propName()
    # input property type
    property.propType()
    # input purchase price
    property.purchPrice()
    # input number of units
    property.numUnits()
    print("Now lets get information about each unit in the property")
    # for each unit input beds baths and sqft
    # enter per unit info
    for u in range(1, ((int(property.num_units))+1)):
        unit_num = (f"unit_{u}")
        print(unit_num)
        property.unitBeds(unit_num)
        property.unitBaths(unit_num)
        property.unitSQFT(unit_num)
    # calculate per unit rent
    for u in range(1, ((int(property.num_units))+1)):
        unit_num = (f"unit_{u}")
        property.perUnitRent(unit_num)
    # calculate monthly mortgage
    property.calcMonthlyMort()
    # calculate monthly rent for all units
    property.allUnitRentMo()
    # calculate all other monthly expenses
    property.otherMonthlyEx()
    # calculate cash flow
    property.cashFlowMo()
    # calculate total investment
    self.totalInvestement()
    #calculate cash on cash  
    self.cashOnCash()
    #Finally, is this a good investment?
    self.goodInvestment()


driver()
