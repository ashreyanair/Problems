accounts={101:1000, 102:1000}

def mains(accounts,ch):
 while(True):
     print("-----------bank management system-------------")
     print("1. CHECK BALANCE ")
     print("2. DEPOSIT ")
     print("3. WITHDRAW")
     print("4. TRANSFER")
     print("5.LOGOUT")
     d = int(input("enter your choice"))
     if d == 1:
         if(ch in accounts):
           print("balance is {}".format(accounts[ch]))
         else:
           print("account doesnt exist")
     elif d == 2:
         deposit(accounts, ch)
     elif d == 3:
         withdraw(accounts, ch)
     elif d == 4:
         to_acc = int(input(("enter account no to transfer")))
         transfer(accounts, ch, to_acc)
     else:
         print("logging out")
         break

def withdraw(accounts, ch):
    amt=int(input("enter amt to be withdrawn"))
    if amt>accounts[ch]:
        print("insufficient balance")
    else:
        accounts[ch]-=amt
        print("amt withdrawn successfully")

def deposit(accounts, ch):
    amt=int(input("enter the amt to be deposited"))
    accounts[ch]+=amt
    print("Amount deposited successfully")

def transfer(accounts, ch, to_acc):
    amt=int(input(("Input amount to be sent ")))
    if amt>accounts[ch]:
        print("not enough balance")
    else:
        accounts[to_acc]+=amt
        accounts[ch]-=amt
        print("Amount transferred successfully!")

while True:
    ch=int(input("enter the account number "))
    mains(accounts,ch)
