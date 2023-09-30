#!/usr/bin/env python3
#
# Bank Server application

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

ALL_ACCOUNTS = dict()   # initialize an empty dictionary

# Helper functions for Bank Server
def acctNumberIsValid(ac_num):
    # a valid account number must be a string, lenth = 8, and match the format AA-NNNNN where AA are two alphabetic characters
    # and NNNNN are five numeric characters
    return isinstance(ac_num, str) and \
        len(ac_num) == 8 and \
        ac_num[2] == '-' and \
        ac_num[:2].isalpha() and \
        ac_num[3:8].isdigit()

def acctPinIsValid(pin):
    return (isinstance(pin, str) and \
        len(pin) == 4 and \
        pin.isdigit())

def amountIsValid(amount):
    # For an amount to be valid it must be a positive float() value with at most two decimal places
    return isinstance(amount, float) and (round(amount, 2) == amount) and (amount >= 0)

# Individual bank accounts are stored as BankAccount instances
class BankAccount:
    acct_balance = 0    # initial account balance is zero

    def __init__(self, ac_num = "zz-00000", ac_pin = "0000"):
        # initialize the state variables of a new BankAccount instance
        if acctNumberIsValid(ac_num):
            self.acct_number = ac_num
        if acctPinIsValid(ac_pin):
            self.acct_pin = ac_pin

    def deposit(self, amount):
        # if the amount is valid, then update the acct_balance
        # return three values: self, success_code, current balance
        # Success codes:
        #  0: valid result
        #  1: invalid amount
        success_code = 0
        if not amountIsValid(amount):
            success_code = 1
        else:
            # valid amount, so add it to balance and set succes_code 1
            self.acct_balance += amount
        return self, success_code, self.acct_balance

    def withdraw(self, amount):
        # if the amount is valid, then update the acct_balance
        # return three values: self, success_code, current balance
        # Success codes:
        #  0: valid result
        #  1: invalid amount
        #  2: attempt to overdraw account
        success_code = 0
        if not amountIsValid(amount):
            # invalid amount, return error 
             success_code = 1
        elif amount > self.acct_balance:
            # attempted overdraft
            success_code = 2
        else:
            # all checks out, subtract amount from the balance
            self.acct_balance -= amount
        return self, success_code, self.acct_balance

# Bank Server operations
def process_client_msg(msg_bytes):
    return

def send_response_to_client(code, result):
    return

def run_bank_server():
    # Needs to be written!
    return False

if __name__ == "__main__":
    run_bank_server()
    print("bank server exiting...")