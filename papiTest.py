#===========================varibales hereunder =========================#
balls = 1.10
amountb = 0
cone = 1.25
amountCone = 0
trays = 0.75
amountTrays =0   
# ==========================functions here under==========================#
def containers ():
    print("-------------------------------------------------")
    print("Sorry, we don't have such large containers...")
    print("_________________________________________________")

def sorry ():
    print("-------------------------------------")
    print("Sorry, I don't understand that...")
    print("_____________________________________")
#============================== smaak function=============================#
def smaak(x):
     for x in range(x):
        extra = input("Wat flavors do you want we have : \nA) Strawberry, \nC) Chocolate, \nM) Mint, \nV) Vanilla ? :")
        if extra == "a":
            extra = "Strawberry"
        elif extra == "c":
            extra = "Chocolate"
        elif extra == "m":
            extra = "Mint"
        elif extra == "v":
            extra = "Vanilla" 
#=============================== repeat function ========================#
def herhalen():
    vraag = input('would u like to order again?(Y/N) ').lower()
    if vraag == 'y':
        start()
    else:
        factuur()

#=================================step 2 funtion =========================#
def step2():
    global aantalBalls,amountCone,amountTrays
    stap2 = input("Would you like this ball(s) " + str( aantalBalls ) +"in \nA: cone \nC: trays \nC or A o ? :").lower()
    if stap2 == 'a':
        amountCone += 1
    elif stap2 == 'c':
        amountTrays += 1
#================================= Factuur funtion ========================#
def factuur():
    global trays,amountTrays,balls,amountb,cone,amountCone
    print(f'balls{amountb} x {balls} Euro = {amountb*balls:.2f}')
    print(f'your total is : {amountCone*cone+trays*amountTrays+balls*amountb:.2f}')
#=================================== start funtion =========================#
def start():
    global amountb,balls,aantalBalls
    check = True
    aantalBalls = int(input('how many balls  do u want ? '))
    amountb = amountb + aantalBalls
    while check == True:

        if aantalBalls <= 3: 
            smaak(aantalBalls)
            check = False

        elif aantalBalls <=8:
            smaak(aantalBalls)
            check = False

        elif aantalBalls > 8 :
            pass

        else:
            sorry()
    step2()
    herhalen()


start()
