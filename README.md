# CSC 249 – Project 2 – Multi-connection bank backend server and ATM client

In this project you will build a distributed banking service application. This application will consist of two separate software programs: (1) a bank server, which holds all bank account records and handles all financial transactions; and (2) an Automated Teller Machine client, which obtains needed inputs from the customer but otherwise relies on the server to perform transaction processing.

In this project, you will first study some more elaborate socket programming code demonstrating how to implement a multi-connection client and server. Again, the tutorial and code are taken from the Jennings tutorial on RealPython.com (https://realpython.com/python-sockets/). This time, I want you to focus on the material about Handling Multiple Connections [(https://realpython.com/python-sockets/#handling-multiple-connections)]. Study the material and code.




To help you get started and enable you to focus on the important parts (the networking components and the client-server message protocol), you are given initial code for both programs. The Python file "bank_server.py" implements all the back-end server functionality EXCEPT none of the network communication components have been implemented. The Python file "atm_client.py" contains a basic ATM client application EXCEPT none of the client-server messaging and message handling functions have been implemented.

Both programs are sprinkled with "TODO" in comments to help you find and focus on the parts of the programs where you will need to be working.

## Bank Server Design Requirements

Conceptually at least, the bank_server application runs in a secure data center on a server that is owned and operated by the bank. Although the server is welcome to generate log messages to the console for debugging and development purposes, it should not be assumed that any customer would be able to access the bank_server console. All communications from the server to the customer must be mediated by the ATM client. That is, server communications must take the form of messages that are sent to the ATM client and interpreted there.

The bank_server:

* MUST run in its own process (i.e., in a dedicated terminal window).
* MUST allow multiple simultaneous ATM_client connections.
* MUST allow multiple ATM clients to send messages to the server and receive timely responses from the server. One client should never be blocked until other client(s) have completed all their transactions.
* MUST validate an account's PIN code before allowing any other transactions to be performed on that account.
* MUST prevent two or more ATM clients from accessing the same bank account and performing transactions on it.
* After a customer "logs in" to their account from an ATM client, the server MUST allow any number of transactions to be performed during that client banking session. During the session, access to the account from other ATM clients MUST be rejected.
* After a customer "logs out" of their account from an ATM client by exiting the client, the server MUST again allow a new ATM client to connect and access that account.
* MUST prevent unfriendly clients from sending messages which cause the server to crash, behave incorrectly, or provide unauthorized access to customer bank accounts.
* The bank_server MAY generate console output for tracing and debugging purposes.
* The bank_server MUST NOT assume that any customer has access to the server's console.
* Server source code must be well documented following program documentation standards posted at this link:
* Source code comments should be sufficient to allow a third party to understand your code, run it, and confirm that it works.

## ATM Client Design Requirements

Conceptually, ... thin client, multiple running instances that are able to communicate simultaneously with the running server.

In this project, you will first study some more elaborate socket programming code demonstrating how to implement a multi-connection client and server. Again, the tutorial and code are taken from the Jennings tutorial on RealPython.com (https://realpython.com/python-sockets/). This time, I want you to focus on the material about Handling Multiple Connections [(https://realpython.com/python-sockets/#handling-multiple-connections)]. Study the material and code. The code has been downloaded for you to this Git repo, which you are welcome to clone (https://github.com/bcheikes/csc-249-p2-multiconn-rpc-app).

## Deliverables

Your work on this project must be submitted for grading by **WEDNESDAY 10/18 at 11:59PM**. Extensions may be obtained by following the late submission policy [https://docs.google.com/document/d/1Fx0iviSFzelwKQWx-QmeSulg4MwX9xXS].

All work must be submitted via Gradescope.

You must submit these work products:

1. Source code for your bank_server and atm_client. Ideally, this will be a link to your public Git code repo.
2. Document that...
3. One or more command-line traces that collectively show at least two clients connecting to the server and the server processing all client requests. 

## Teamwork Policy

**For this project, submissions from two-person teams are welcome**.

## Getting Help

There is plenty of self-help material out there to help you understand socket programming in Python. 

* Socket Programming in Python (Guide) by Nathan Jennings [https://realpython.com/python-sockets/]
* Python sockets library documentation [https://docs.python.org/3/library/socket.html]
* LinkedIn Learning (Smith College offers free access) – search “python sockets”
* Python sockets tutorials on YouTube [for example, try https://www.youtube.com/watch?v=3QiPPX-KeSc]. There are many!
* Slack messages in the #questions channel. Students are encouraged to help each other out – this is part of what “participation and engagement” means in the overall course grading rubric.
* Instructor and TA office hours!

## Grading Rubric

Your work on this project will be graded on a ten-point scale. Fractional points may be awarded.

_0 pts:_ No deliverables were received by the due date or requested extension date.

_1-2 pts:_ Incomplete deliverables were received by the due date or extension date.

_3-4 pts:_ Required deliverables were received but are deficient in various ways.

_5-6 pts:_ Complete and adequate deliverables. Code runs but is deficient in various ways.

_7-8 pts:_ Code runs and does most but not all of what is required.

_9-10 pts:_ Nailed it. Complete deliverables, code runs and does what is required.

