#Uzycie funckji Console
from rich.console import Console
from os import system

console = Console()


################################################################################
#
# Program: Create A Menu For The Console/Terminal/Shell
# 
# Description: Example of how to create a simple menu for the console/terminal/
# shell using Python.  We model a simple ATM machine in this example that allows
# a user to make deposits, withdraw money, print a balance, and quit.
#
# YouTube Lesson: https://www.youtube.com/watch?v=nqx2kMgKRVo 
#
# Author: Kevin Browne @ https://portfoliocourses.com
#
################################################################################

# Create variables to store the balance, amount to deposit/withdraw, and menu 
# choice selected

user_choice = ""

# Because we know we want to display the menu repeatedly until the user decides 
# to quit, and because we know we want to display it once, use a while loop 
# with condition True to present the menu.  This will present the menu again 
# and again to the user, and we'll use the 'break' keyword to terminate the 
# loop when the user chooses to quit

#while True:
  
  # Present the menu options to the user
  #print("1) Wpłata")
  #print("2) Wypłata")
  #print("3) Wyświetl stan konta")
  #print("4) Zrób bilans wydatków")
  #print('5) Quit')
  
def print_menu():
    console.print('========= MENU =========', style='#BD6711 bold')
    console.print('[1] Wpłata', style='#BD6711')
    console.print('[2] Wypłata', style='#BD6711')
    console.print('[3] Bilans wydatków', style='#BD6711')
    console.print('[4] Wyjście', style='#BD6711')
    console.print('========= MENU =========', style='#BD6711 bold')


def definition_of_variable_amount():
    expenses = {}  # Tworzymy słownik do przechowywania stałych wydatków
    amount_of_cost = int(console.input('Wpisz liczbę typów stałych wydatków w tym miesiącu: '))
    for i in range(amount_of_cost):
        variable = console.input(f"Podaj nazwę wydatku (prąd, gaz itp.) {i + 1}: ")
        expenses[variable] = float(console.input(f"Podaj kwotę dla tego rodzaju wydatku {variable}: "))
    
    console.print("""
                  Twoje stałe wydatki w danym miesiącu: """)
    total_expenses = sum(expenses.values())  # Obliczamy sumę stałych wydatków
    for variable, value in expenses.items():
        console.print(f"{variable}: {value}")
    console.print(f"Suma stałych wydatków: {total_expenses}")

    return expenses  # Zwracamy słownik ze stałymi wydatkami

def main():
    balance = float(0)
    amount = float(0)
    expenses = {}  # Słownik do przechowywania stałych wydatków

    while True:
        print_menu()
        user_choice = int(input('Wybierz opcje [1-5]: '))
        console.clear()
        #user_choice = user_choice.strip()

        if user_choice == 1:
            console.print('===================== Konto =====================', style='blue bold')
            amount = float(input ('Wpisz kwotę: '))
            balance += amount
            console.print ('Aktualny stan konta: ', balance)
            console.print('===================== Konto =====================\n', style='blue bold')

        elif user_choice == 2:
            console.print('===================== Konto =====================', style='blue bold')
            amount = float (input ('Wpisz kwotę: '))
            balance -= amount
            console.print ('Aktualny stan konta: ', balance)
            console.print('===================== Konto =====================\n', style='blue bold')

        elif user_choice == 3:
            amount_of_cost = int (0)
            name_of_cost = str ('')
            console.print('================= Bilans wydatków ================', style='blue bold')
            definition_of_variable_amount ()
            console.print('================= Bilans wydatków ================', style='blue bold')

            

        elif user_choice == 4:
            break

        else:
            print ('Błędnie wpisana kwota, spróbuj ponownie')

if __name__ == "__main__":
    main()
        
  # Prompt the user to enter a choice, store the string entered into choice
  #choice = input("Wybierz opcję   : ")
  
  # Trims any leading and trailing whitespace characters from the string, so 
  # that if the user enters something like "  3  " with leading and/or 
  # trailing whitespace when trying to enter in the option "3", the string 
  # will be trimmed down to "3" before making the comparisons below (allowing
  # the user to successfully make their selection).
        
   
  # Handle the choice entered with an if-elif-else control structure, first 
  # checking to see if a valid choice from 1-4 was entered using the if and 
  # elif conditions, and then using the else case to handle invalid input.
  #if (choice == "1"):
    # In the case of a deposit we prompt the user to enter an amount, convert it
    # to a float value and add it to the balance.
    #amount = float(input("Wpisz kwotę: "))
    #balance += amount 
  #elif (choice == "2"):
    # In the case of a withdraw we again prompt the user to enter an amount, 
    # and convert it to a float, but this time we subtract it from the balance.
   # amount = float(input("Enter Amount: "))
    #balance -= amount 
  #elif (choice == "3"):
    # Output the balance
   # print("Balance:", balance)
    #Enter new function for prepare bilans
  #elif (choice == "4"):
   # input ('Wpisz ile rodzajów stałych kosztów ponosisz miesięcznie: ')



  #elif (choice == "5"):
    # Using break will end the loop right here, control flow will jump to the 
    # next statement after the loop
   # break
  # If we have invalid input, inform the user of this and ask them to try again.
  #else:
   # print("Błędnie wpisana opcja, spróbuj ponownie")