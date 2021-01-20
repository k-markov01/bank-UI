import sys
accounts = list()


def DRAW(account_balance):
    draw_num = int(input("\nEnter in amount to DRAW\n>>>"))    
    if draw_num > account_balance:
        print("The amount you wish to DRAW is larger than your total funds\n")
        return
    account_balance -= draw_num
    print(f"Your balance is {account_balance}")
    return account_balance

def PUT(account_balance):
    input_num = int(input("\nEnter in amount to Input in your account\n >>>"))
    account_balance += input_num
    print(f"New Balance is:  {account_balance}")
    return account_balance

def TRANSFER(account_balance):
    global accounts
    """GET THE ID OF THE ACCOUT TO TRANSFER TO"""
    target_id = input("\nEnter the ID of the account you wish to transfer to\n>>>")
    for account in accounts:
        if target_id == account[0]:
            tranfer_num = int(input("Enter in the amount to transfer\n>>>"))
            if tranfer_num < 0:
                print("The transfer amount cannot be less than 0\n")
                return account_balance
            if tranfer_num > account_balance:
                print("The tranfer amount is greater than your balance\n")
                return account_balance
            account_balance -= tranfer_num
            account[2] += tranfer_num
            print(f"Tranfered money is: {tranfer_num}")
            print(f"Money left is: {account_balance}")
            return account_balance
    else:
        print("Account ID not found, Returning to main menu\n")
        return    

        
def main(account):
    print(f"Your account balance is {account[2]}")
    while True:
        print(f"\n"+"*"*70)
        u_in = input("INPUT\tDRAW\tTRANSFER\tINFO\tLOGOUT\tEXIT\n>>>")
        if u_in == "INPUT":
            account[2] = PUT(account[2])
        elif u_in =="DRAW":
            account[2] = DRAW(account[2])
        elif u_in == "TRANSFER":
            account[2] = TRANSFER(account[2])
        elif u_in == "INFO":
            print(f"Current balance is: {account[2]}")
        elif u_in == "LOGOUT":
            return account
        elif u_in == "EXIT":
            sys.exit(0)
    
"""ADD ACCOUNTS"""
def DATA():
    print("Input DATA:\n")
    while True:
        u_in = input(">>>")
        u_in = u_in.strip()
        content = u_in.split(" ")
        if all(num == "0" for num in content):
            break
        print(content)
        content[-1] = int(content[-1])
        accounts.append(content) 
    return

"""LOG into an account"""
def LOGIN():
    ID = input("ID:\n>>>")
    PASS = input("Passowrd:\n>>>")
    for account in accounts:
        if ID == account[0] and PASS == account[1]:
            account = main(account)
    else:
        print("ID OR PASSWORD DOES NOT EXIST, TRY AGAIN")
    LOGIN()


DATA()
"""MAIN LOOP"""
while True:
    u_in = input("\nType \"LOGIN\" or \"EXIT\"\n>>>")
    if u_in == "LOGIN":
        LOGIN()
    elif u_in == "EXIT":
        sys.exit(0)
    else:
        print("Input was incorrect\n")