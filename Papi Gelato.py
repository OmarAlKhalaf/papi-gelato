A = "Cone"
B = "Bowl"

def containers ():
    print("-------------------------------------------------")
    print("Sorry, we don't have such large containers...")
    print("_________________________________________________")

def sorry ():
    print("-------------------------------------")
    print("Sorry, I don't understand that...")
    print("_____________________________________")

step3 = "y"
print("Welcome to Papi Gelato, you can choose any flavor as long as it's vanilla ice cream. ^_^ ")
while step3 == "y":   
    while True : 
        number = int(input("How many balls do you want ? : "))
        if number  <= 3 :
            break
        elif number <= 8 :
            print ("Then I will give you a tray with",number,"balls")
            break
        else:
            containers()  
    while True :
        if number <=3 :
            for x in range(number):
                extra = input("Wat flavors do you want we have : A) Strawberry, C) Chocolate, M) Mint or V) Vanilla ? :")
                if extra == "a":
                    extra = "Strawberry"
                elif extra == "c":
                    extra = "Chocolate"
                elif extra == "m":
                    extra = "Mint"
                elif extra == "v":
                    extra = "Vanilla" 
        elif number <=8 :
            for t in range(number):
                extra = input("Wat flavors do you want we have : A) Strawberry, C) Chocolate, M) Mint or V) Vanilla ? :")
                if extra == "a":
                    extra = "Strawberry"
                elif extra == "c":
                    extra = "Chocolate"
                elif extra == "m":
                    extra = "Mint"
                elif extra == "v":
                    extra ="Vanilla"
        step2 = input("Would you like this ball(s) " + str( number ) +""" in 
A: cone
B: bowl 
A or B ? : """)
        if step2 == "a" :
            step2 = A
            print("Here is your",step2, "with", number,"ball(s).")
            step3 = input("Would you like to order even more? (Y/N) ? :")
            if step3 == "n":
                print("Thank you for coming and goodbye!")
                break 
            elif step3 == "y":
                break

        elif step2 == "b":
            step2 = B
            print("Here is your",step2, "with", number, extra ,"ball(s). Would you like to order even more? (Y/N)”")
            step3 = input("Would you like to order even more? (Y/N) ? :")
            if step3 == "n":
                print("Thank you for coming and goodbye!")
                break
            elif step3 == "y":
                break
        else:
            sorry()