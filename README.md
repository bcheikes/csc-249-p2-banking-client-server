# CSC 249 – Project 2 – ATM client with multi-client back-end banking server

In this project you will build a distributed ATM banking application. This application consists of two separate software programs: (1) a bank server, which holds all bank account records and handles all financial transactions; and (2) an Automated Teller Machine client, which obtains needed inputs from the customer but otherwise relies on the server to perform transaction processing.

The main focus of your work will be on enabling the banking server to handle simultaneous connections from different ATM client instances, and then process transaction requests correctly. Relevant technical resources include the Jennings tutorial we encountered in Project 1 (https://realpython.com/python-sockets/). For this project, it is recommended that you focus on the tutorial material pertaining to Handling Multiple Connections [(https://realpython.com/python-sockets/#handling-multiple-connections)].

To help you get started on this project and enable you to focus on the most important parts (that is, the networking components and the client-server message protocol), you are given initial code for both programs. The Python file "bank_server.py" implements all the back-end server functionality EXCEPT none of the network communication components have been implemented. The Python file "atm_client.py" contains a basic ATM client application EXCEPT none of the client-server messaging and message handling functions have been implemented. You should study this code and make sure you understand how it works and where you need to make changes and/or insert new code. Both programs are sprinkled with "TODO" in comments to help you find and focus on the parts of the programs where you will need to be working.

**If you have any questions about the provided code or the instructions below, please seek help from the instructor and/or the teaching assistant as soon as possible!**

## Bank Server Design Requirements

Conceptually at least, the bank_server application runs in a secure data center on a server that is owned and operated by the bank. Although the server is welcome to generate log messages to the console for debugging and development purposes, it should not be assumed that any customer would be able to access the bank_server console. All communications from the server to the customer must be mediated by the ATM client. That is, server communications must take the form of messages that are sent to the ATM client and interpreted there.

The bank_server:

* MUST run in its own computing process (i.e., in a dedicated terminal window).
* MUST allow multiple simultaneous ATM client connections.
* MUST communicate with ATM clients exclusively by sending and receiving messages over the network using an application-layer message protocol of your own design.
* MUST allow multiple ATM clients to send messages to the server and receive timely responses from the server. One client should never be blocked until other client(s) have completed all their transactions.
* MUST validate an account's PIN code before allowing any other transactions to be performed on that account.
* MUST prevent two or more ATM clients from accessing the same bank account and performing transactions on it.
* MUST transmit error results to the client using numeric codes rather than literal message strings.
* After a customer "logs in" to their account from an ATM client, the server MUST allow any number of transactions to be performed during that client banking session. During the session, access to the account from other ATM clients MUST be rejected.
* MUST prevent malicious client applications (i.e., other than the implemented atm_client application) from being able to send messages the the server which cause the server to crash, behave incorrectly, and/or provide unauthorized access to customer bank accounts.
* The bank_server MAY generate console output for tracing and debugging purposes.
* The bank_server MUST NOT assume that any customer has access to the server's console.

## ATM Client Design Requirements

Conceptually, each ATM client is a "thin" software application that connects to the remote bank_server, then interacts with a single customer at a time. The ATM client relies on the bank_server for all transaction processing. The ATM client communicates with the bank_server using an application-layer message protocol which you will design as part of this assignment.

Notionally, every ATM banking session begins with a customer "logging in" by providing an account number and a PIN code. (In real life, a customer inserts a physical card into the machine, which then reads the account number off the card.) Only after a customer has provided a valid account-PIN pair will the machine permit any transactions. The ATM machine allows customers to make deposits, withdrawals, and check their account balance. The ATM machine allows customers to make an unlimited number of deposits and/or withdrawals during a session, but does not allow customers to overdraw their accounts. When the customer chooses to exit the banking session, the ATM client "logs out" from the bank_server and exits.

The atm_client:

* MUST run in its own computing process (i.e., in a dedicated terminal window).
* MUST connect to only one bank_server at a time.
* MUST communicate with the bank_server exclusively by sending and receiving messages over the network using an application-layer message protocol of your own design.
* MUST require each banking session to being with a customer "log in" step, where the customer provides an account number and PIN which are then validated by the bank_server.
* MUST NOT allow a customer to perform any banking transactions unless their account number and PIN are first validated by the bank_server.
* MUST allow a customer to perform any sequence of deposits, withdrawals, and balance checks after they have validated their account number and PIN.
* MUST NOT allow a customer to overdraw their bank account.

## General Client-Server Application Design Requirements

* You MUST use the provided bank_server and atm_client programs as your starting point. You MUST NOT implement your own bank server and client from scratch.
* You MAY extend the core banking functionality in the bank_server and atm_client, but only to the degree needed to enable the two components to be able to interoperate.
* Your code MUST be readable, well organized, and demonstrate care and attention to computer programming best practices. The provided bank_server and atm_client provide good examples of such practices: classes and functions with easy-to-understand names are used extensively; functions are kept short (under 20 lines is ideal); functions are commented, and comments are inserted at key points within the function body.

## Deliverables

Your work on this project must be submitted for grading by **WEDNESDAY 10/18 at 11:59PM**. Extensions may be obtained by following the late submission policy [https://docs.google.com/document/d/1Fx0iviSFzelwKQWx-QmeSulg4MwX9xXS].

All work must be submitted via Gradescope.

You must submit these work products:

1. Source code for your bank_server and atm_client. Ideally, this will be a link to your public Git code repository. (Use of Git is encouraged but not required; you may instead upload your individual Python files directly to Gradescope without involving Git.)
2. A message specification document. This document must include a written description of the application-layer message protocol you developed for communications that are sent between the client and the server. You **must** document your message formats using Augmented Backus–Naur form (ABNF). (For more details on ABNF, see [https://en.wikipedia.org/wiki/Augmented_Backus%E2%80%93Naur_form].)

## Teamwork Policy

**For this project, submissions from two-person teams are welcome**.

Teams should consider code revisions that enable the atm_client and bank_server to use real IP addresses instead of the loopback address. In this way, one team member could focus on client development and the other on server development, then the team members could test their components from different locations. This could be very cool!

## Getting Help

There is plenty of self-help material out there to help you understand socket programming in Python. 

* Socket Programming in Python (Guide) by Nathan Jennings [https://realpython.com/python-sockets/]
* Python sockets library documentation [https://docs.python.org/3/library/socket.html]
* LinkedIn Learning (Smith College offers free access) – search “python sockets”
* Slack messages in the #questions channel. Students are encouraged to help each other out – this is part of what “participation and engagement” means in the overall course grading rubric.
* Instructor and TA office hours!

## Grading Rubric

Your work on this project will be graded on a ten-point scale. Fractional points may be awarded.

_0 pts:_ No deliverables were received by the due date or requested extension date.

_1-5 pts:_ Incomplete deliverables were received by the due date or extension date.

_6-7 pts:_ All deliverables received. Most design requirements are not satisfied.

_7-8 pts:_ All deliverables received. Many design requirements are not satisfied.

_8-9 pts:_ All deliverables received. A few design requirements are not satisfied.

_9-10 pts:_ Complete deliverables, all or nearly all design requirements are satisfied.
