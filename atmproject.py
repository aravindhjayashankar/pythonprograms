print("welcome to bank!!!")
balance = 15000
val = 1234
i = 0
while i < 3:
    pin = int(input("enter your pin:"))
    if val == pin:
        print("sucess")
        j = 2
        while j > 0:
            print("1.withdrawl\n2.deposit\n3.balance enquir\n4.exit")
            opt = int(input("choose your option:"))
            if opt == 1:
                print("enter the amount")
                amunt = int(input(""))
                print("collect ur cash", amunt)
            elif opt == 2:
                print("enter the amunt to be deposit")
                dep = int(input(""))
                print("deposit ur cash in tray")
                print("amount deposited:", dep)
            elif opt == 3:
                bal = 10000
                print("balance enquiry:", bal)
            elif opt == 4:
                print("thank you visit again!!!")
                break
            else:
                print("enter valid option")
            j += 1
    else:
        i += 1
        print("try again")
print("card blocked")
