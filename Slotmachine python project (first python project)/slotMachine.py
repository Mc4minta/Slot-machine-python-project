import random

#define constant
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
ROWS = 3
COLS = 3

#define dictionary
symbol_count = {
    "A" : 3,
    "B" : 5,
    "C" : 7,
    "D" : 9,
}            
symbol_value = {
    "A" : 10,
    "B" : 8,
    "C" : 6,
    "D" : 4,
}                                                                                           

#define the function to deposit money
def deposit():
    while True:
        #get the amount of money
        amount = input("How much would you like to deposit?: $")
        #check if the amount is a number and is greater than zero or not
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("\n> The amount can't be zero.\n")
        else: 
            print("\n> Please enter a number.\n")
    return amount

#define the function to withdraw the money out
def withdraw(balance):
    #enter the amount of money you want to withdraw
    while True:
        amount = input("How much do you want to withdraw?: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > balance :
                print("--------------------------------------------")
                print("You can't withdraw more that you have!")
            else:
                balance = balance - amount
                print("--------------------------------------------\n")
                print(f"You have withdrawed ${amount}")
        else:
            print("Please enter a number")
        return balance
       
#define function for checking the money won
def check_winning(columns,lines,bet,values):
    winnings = 0
    #check if the first symbols on that columns in 'lines' rows is the same or not
    lines_won = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            lines_won.append(line + 1)
            winnings += values[symbol] * bet
    return winnings, lines_won

#define the funciton to get the machine slot spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    slots = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):            
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        slots.append(column)
    return slots

#define the function to print the slot machine out
def print_slot_machine(slots):
    print("--------------------------------------------")
    print("\nYour slots below!")
    for row in range(len(slots[0])):
        for i,column in enumerate(slots):
            if i != len(slots) - 1:
                print(column[row], end=" | ")
            else: 
                print(column[row], end="")
        print()  

#define the function to get the number of lines you want to bet on
def get_number_of_lines():
    while True:
        #get the amount of lines
        lines = input("How many lines you want to bet on? (1-" + str(MAX_LINES) + "): ")
        #check if the amount is number and greater that zero or not
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("\n> Please enter a valid number of lines <\n")
        else: 
            print("\n> Please enter a number <\n")
    return lines

#define the function to get the amount of money you want to bet on
def get_bet():
    while True:
        amount = input("How much bet on each lines?: $")
        #check if the amount is a number and is in the required range or not
        if amount.isdigit() :
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                #print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") 
                # the code above perform the same as below but just wrote diffrent
                print("Amount must be between $%d and $%d." % (MIN_BET,MAX_BET))
        else:
            print("\n> Please enter a number <\n")
    return amount
    
#define a funtion to spin slot machine
def spin(balance):
    #get the number of lines to bet on
    lines = get_number_of_lines()

    #check if you have enough money to bet on that amount or not
    while True:
        bet = get_bet()
        total_bet = lines * bet;
        if total_bet > balance:
            print("--------------------------------------------")
            print(
                f"\n> You don't have enough to bet ${total_bet}")
            print(
                f"> your current balance is ${balance}")   
            print(
                f"> You will have to deposit ${total_bet - balance} more to bet this amount.\n")
            print("--------------------------------------------")
            
        else: 
            break

    # print the number of money and lines bet.
    print("--------------------------------------------")
    print(f"> You are betting ${bet} on {lines} lines <")
    print(f"> Total bet is equal to: ${total_bet} <")
    print("--------------------------------------------")
    #Ask to confirm the bet
    print("Confirm your bet")
    ans = input(
        "Press N to re enter\nPress any key to confirm: ")
    if ans.lower() == "n":
        print("--------------------------------------------")
        print("> Re enter <")   
        spin(balance)
    else:
        #get and print the slot machine and check the lines won and money won
        slots = get_slot_machine_spin(ROWS,COLS, symbol_count)
        print_slot_machine(slots)
        winnings, lines_won = check_winning(slots, lines, bet, symbol_value)
        print(f"\nYou won ${winnings}.")
        if winnings == 0:
            print("You didn't win any lines :(")
        else :
            print(f"You won on the following lines:", *lines_won)
        #give you the balance after the bet
        return balance,total_bet,winnings
        
#define the main function
def main(balance,total_bet,winnings):
    #make you deposit the balance
    #also if it's n time playing the balance will be the sum of your old balance and the money you deposit
    balance += deposit()
    
    while True:
        #print out the current balance and ask what the action you want to do?
        # q to quit , d to deposit, w to withdraw or any other keys to play
        balance -= total_bet
        total_bet = 0
        balance += winnings
        winnings = 0
        print("\n--------------------------------------------\n↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓\n")
        print(f"Current balance is ${balance}")
        print("\n↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑")
        print("--------------------------------------------")
        print("Q to quit.\nD to deposit.\nW to withdraw.\n> Press any other keys to play <")
        print("--------------------------------------------")
        answer = input("Your answer?: ")
        answer = answer.lower()
        if answer == "q":
            break
        elif answer == "d":
            main(balance,total_bet,winnings)
        elif answer == "w":
            balance = withdraw(balance)
        else : 
            balance,total_bet,winnings = spin(balance)
    print("--------------------------------------------")
    print(f"> You left with ${balance} <")  
    print("--------------------------------------------\n")  
    
    

#set the intitial balance before playing for the first time
balance = 0
total_bet = 0
winnings = 0
#run the program main fuction
main(balance,total_bet,winnings) 
