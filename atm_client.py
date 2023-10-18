#!/usr/bin/env python3
#
# Automated Teller Machine (ATM) client application.

import socket

HOST = "127.0.0.1"      # The bank server's IP address
PORT = 65432            # The port used by the bank server

##########################################################
#                                                        #
# ATM Client Network Operations                          #
#                                                        #
# NEEDS REVIEW. Changes may be needed in this section.   #
#                                                        #
##########################################################

def send_to_server(sock, msg):
    """ Given an open socket connection (sock) and a string msg, send the string to the server. """
    # TODO make sure this works as needed
    return sock.sendall(msg.encode('utf-8'))

def get_from_server(sock):
    """ Attempt to receive a message from the active connection. Block until message is received. """
    # TODO make sure this works as needed
    msg = sock.recv(1024)
    return msg.decode('utf-8')

def login_to_server(sock, acct_num, pin):
    """ Attempt to login to the bank server. Pass acct_num and pin, get response, parse and check whether login was successful. """
     # TODO: Write this code!
    #validated = 0

    send_to_server(sock, acct_num + "," + pin)
    validation_status = get_from_server(sock)

    if validation_status == "True":
        return True
    elif validation_status == "False":
        print("Pin does not match account number")
        return False
    else:
        print("Validation process error")
        return False

# moved from bank server, makes more sense to check format validity before sending to server
def acctNumberIsValid(ac_num):
    """Return True if ac_num represents a valid account number. This does NOT test whether the account actually exists, only
    whether the value of ac_num is properly formatted to be used as an account number.  A valid account number must be a string,
    lenth = 8, and match the format AA-NNNNN where AA are two alphabetic characters and NNNNN are five numeric characters."""
    return isinstance(ac_num, str) and \
        len(ac_num) == 8 and \
        ac_num[2] == '-' and \
        ac_num[:2].isalpha() and \
        ac_num[3:8].isdigit()

# moved from bank server, makes more sense to check format validity before sending to server
def acctPinIsValid(pin):
    """Return True if pin represents a valid PIN number. A valid PIN number is a four-character string of only numeric characters."""
    return (isinstance(pin, str) and \
        len(pin) == 4 and \
        pin.isdigit())

def amountIsValid(amount):
    """Return True if amount represents a valid amount for banking transactins. For an amount to be valid it must be a positive float()
    value with at most two decimal places."""
    return isinstance(amount, float) and (round(amount, 2) == amount) and (amount >= 0)

def get_login_info():
    """ Get info from customer. DONE TODO: Validate inputs, ask again if given invalid input. """
    acct_num = input("Please enter your account number: ")
    while not acctNumberIsValid(acct_num):
        acct_num = input("Invalid input. Please enter your account number of the form AA-NNNNN where AA are two alphabetic characters and NNNNN are five numeric characters: ")
        acctNumberIsValid(acct_num)

    pin = input("Please enter your four digit PIN: ")
    while not acctPinIsValid(pin):
        pin = str(input("Invalid input. Please enter your four digit PIN: "))
        acctPinIsValid(pin)

    return acct_num, pin

def process_deposit(sock, acct_num):
    """ TODO: Write this code. """
    bal = get_acct_balance(sock)
    amt = float(input(f"How much would you like to deposit? (You have ${bal} available)"))
    # TODO communicate with the server to request the deposit, check response for success or failure.

    while not amountIsValid(amt):
        amt = float(input("Invalid deposit amount. Please input correct amount: "))
        amountIsValid(amt)

    # sends deposit amount to the server
    send_to_server(sock, str(amt))

    # server makes the deposit and returns the new balance
    new_bal = get_from_server(sock)
    
    print(f"Deposit transaction completed. You now have ${new_bal} in your account.")
    return

def get_acct_balance(sock):
    """ DONE TODO: Ask the server for current account balance. """
    bal = 0.0
    bal = get_from_server(sock)
    return bal

def process_withdrawal(sock, acct_num):
    """ TODO: Write this code. """
    bal = get_acct_balance(sock, acct_num)
    amt = float(input(f"How much would you like to withdraw? (You have ${bal} available)"))
    # TODO communicate with the server to request the withdrawal, check response for success or failure.
    print("Withdrawal transaction completed.")
    return

def process_customer_transactions(sock, acct_num):
    """ Ask customer for a transaction, communicate with server. TODO: Revise as needed. """
    while True:
        print("Select a transaction. Enter 'd' to deposit, 'w' to withdraw, or 'x' to exit.")
        req = input("Your choice? ").lower()
        if req not in ('d', 'w', 'x'):
            print("Unrecognized choice, please try again.")
            continue
        if req == 'x':
            # if customer wants to exit, break out of the loop
            break
        elif req == 'd':
            process_deposit(sock, acct_num)
        else:
            process_withdrawal(sock, acct_num)

def run_atm_core_loop(sock):
    """ Given an active network connection to the bank server, run the core business loop. """
    acct_num, pin = get_login_info()
    validated = login_to_server(sock, acct_num, pin)
    if validated:
        print("Thank you, your credentials have been validated.")
    else:
        print("Account number and PIN do not match. Terminating ATM session.")
        return False
    process_customer_transactions(sock, acct_num)
    print("ATM session terminating.")
    return True

##########################################################
#                                                        #
# ATM Client Startup Operations                          #
#                                                        #
# No changes needed in this section.                     #
#                                                        #
##########################################################

def run_network_client():
    """ This function connects the client to the server and runs the main loop. """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            run_atm_core_loop(s)
    except Exception as e:
        print(f"Unable to connect to the banking server - exiting...")

if __name__ == "__main__":
    print("Welcome to the ACME ATM Client, where customer satisfaction is our goal!")
    run_network_client()
    print("Thanks for banking with us! Come again soon!!")