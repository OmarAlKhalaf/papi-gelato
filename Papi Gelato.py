#===========================varibales hereunder =========================#
balls = 0.95
amountb = 0
cone = 1.25
amountCone = 0
trays = 0.75
amountTrays =0   
whippedcream = 0.50
amountcream = 0
sprinkles = 0.30
amountsprinkles = 0
caramelSauces_creen = 0.60
amountcaramelsauces_creen = 0
caramelsauces_trays = 0.90
amountcaramelsauces_trays = 0
anser = None
liter_cost = 9.80
amountliter = 0
total = (liter_cost*int(amountliter))
btw = (total / 100) *6

# ==========================functions here under==========================#
def sorry ():
    print("-------------------------------------")
    print("Sorry dat is geen optie die we aanbieden...")
    print("_____________________________________")
#============================== flaever function=============================#
def flaever(x):
     for x in range(x):
        flaever = input("Wat flavors do you want we have : \nA) Strawberry, \nC) Chocolate, \nM) Mint, \nV) Vanilla ? :") .lower()
        if flaever == "a":
            flaever = "Strawberry"
        elif flaever == "c":
            flaever = "Chocolate"
        elif flaever == "m":
            flaever = "Mint"
        elif flaever == "v":
            flaever = "Vanilla" 
#================================ extra flaever's =======================#
def extra_flaever(i):
    global question,amountcream,amountsprinkles,amountcaramelsauces_creen,amountcaramelsauces_trays
    for i in range(i):
        question = input("What kind of topping do you want: \nA) None, \nB) Whipped cream, \nC) Sprinkles, \nD) Caramel Sauce in cone or \nE) Caramel Sauce in trays ?").lower()
        if question == "a":
            question = anser
        elif question == "b":
            amountcream +=1
        elif question == "c":
            amountsprinkles += 1
        elif question == "d":
            amountcaramelsauces_creen += 1 
        elif question == "e":
            amountcaramelsauces_trays += 1

#=============================== repeat function ========================#
def again():
    vraag = input('Would u like to order again?(Y/N) ').lower()
    if vraag == 'y':
        start()
    else:
        invoice()

#=================================step 2 funtion =========================#
def step2():
    global aantalBalls,amountCone,amountTrays
    stap2 = input("Would you like this ball(s) " + str( aantalBalls ) +" in \nA: cone \nC: trays \nC or A o ? :").lower()
    if stap2 == 'a':
        amountCone += 1
    elif stap2 == 'c':
        amountTrays += 1
#================================= invoice funtion ========================#
def invoice():
    global trays,amountTrays,balls,amountb,cone,amountCone
    print('----------["Papi Gelato"]----------')
    print(f'Balls {amountb} x {1.10} Euro = {amountb*1.10:.2f}')
    print(f"Cone {amountCone} x {1.25} Euro = {amountCone*1.25:.2f}")
    print(f"Trays  {amountTrays} x {0.75} Euro = {amountTrays*0.75:.2f}")
    print(f"Your total topping is {whippedcream*amountcream+sprinkles*amountsprinkles+caramelSauces_creen*amountcaramelsauces_creen+caramelsauces_trays*amountcaramelsauces_trays:.2f} ")
    print(f'your total is : {amountCone*cone+trays*amountTrays+balls*amountb+whippedcream*amountcream+sprinkles*amountsprinkles+caramelSauces_creen*amountcaramelsauces_creen+caramelsauces_trays*amountcaramelsauces_trays:.2f}')
    print("Thanks for coming, Have a nice day.")
#=================================== business ==============================#
def business_question():
    global ask,liter,amountliter,flaever
    ask = int(input("Are you 1) private or 2) business?  \n1/2 :  "))
    if ask == 1:
        start()
    elif ask == 2:
        liter = int(input("how many liters do u like to order ? "))
        amountliter = amountliter + liter
        flaever(1)
        invoice_business()
#=================================== invoice_business ========================#
def invoice_business():
    global ask,liter,amountliter,btw,total,liter_cost
    print('----------["Papi Gelato"]----------')
    print(f"Liter                  {liter} x {9.50} = {liter*liter_cost} ")
    print('                         ------')
    print(f'Totaal(inclusief BTW) = {liter_cost*int(amountliter):.2f}')
    print(f'BTW 6%                = {(liter_cost*int(amountliter) / 100) *6:.2f}')
#=================================== start funtion =========================#
def start():
    global amountb,balls,aantalBalls,ask,liter,amountliter
    check = True
    print('----------["Welcome to Papi Gelato"]----------')
    aantalBalls = int(input('How many balls do u want ? '))
    amountb = amountb + aantalBalls
    while check == True:
        if aantalBalls <= 3: 
            flaever(aantalBalls)
            extra_flaever(aantalBalls)
            check = False

        elif aantalBalls <=8:
            flaever(aantalBalls)
            extra_flaever(aantalBalls)
            check = False

        else:
            sorry()
    step2()
    again()
business_question()
start()






