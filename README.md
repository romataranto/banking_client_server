# STATUS REPORT

### (a) Design Requirements
I met the following design requirements:
- MUST run in its own computing process (i.e., in a dedicated terminal window).
- MUST communicate with ATM clients exclusively by sending and receiving messages over the network using an application-layer message protocol of your own design.
- MUST validate an account's PIN code before allowing any other transactions to be performed on that account.
- MUST transmit error results to the client using numeric codes rather than literal message strings.
- After a customer "logs in" to their account from an ATM client, the server MUST allow any number of transactions to be performed during that client banking session. 
- The bank server MAY generate console output for tracing and debugging purposes.
- The bank server MUST NOT assume that any customer has access to the server's console.

I did not meet the following design requirements:
- MUST allow multiple simultaneous ATM client connections.
- MUST allow multiple ATM clients to send messages to the server and receive timely responses from the server. One client should never be blocked until other client(s) have completed all their transactions.
- MUST prevent more than one ATM client at a time from accessing a bank account and performing transactions on it.
- During the session, access to the account from other ATM clients MUST be rejected.
- MUST prevent malicious client applications (i.e., other than the implemented ATM client application) from being able to send messages to the server which cause the server to crash, behave incorrectly, and/or provide unauthorized access to customer bank accounts.

### (b) Knowledge Gaps
1. I’m not sure how to have multiple clients connecting to the server. I didn’t have time to attempt this, so I’m not sure how difficult it is to get this to work, but I also have no idea where to start with this. I know that there is information on the tutorial about this, and I plan on working through that, but I feel like a little more guidance could be helpful. I do really enjoy struggling and figuring things out for myself (the engineering major in me), but I feel like this is a little too far.
2. Getting used to using classes has taken a lot of time for me. For example, referencing the instance variables outside the class was something that wasn’t intuitive for me, since Python is a little rusty. However, I feel more comfortable with this now.
3. I’m not sure what the best way to be coding this is. I feel like I’m possibly brute-forcing a lot of this in a really un-delicate way and I don’t like doing that, but am unsure how to do this otherwise. This isn’t really code that I’m proud of.

### (c) Overcoming Knowledge Gaps
I need to go to office hours because I need help coming up with a game plan of what to code next. I jumped in by starting with the log-on validation, and then got deposits and withdrawals to work (as many times as the client wants). But, I haven’t done anything with multiple connections and I’m not sure where to start with adding that in. I would also like to say that what I have worked on thus far has taken so many hours, partially because I needed time to understand the code that was already written. Jumping into somebody else’s half written (and decently long) code is not easy. This also meant that debugging was extremely time consuming. Thus, to overcome my knowledge gaps, office hours and TA hours would be helpful. Mostly though, I just need more time.


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
* MUST prevent more than one ATM client at a time from accessing a bank account and performing transactions on it.
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
* MUST obtain all needed user inputs through keyboard interaction.
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

1. Source code for your bank_server and atm_client. Ideally, this will be a link to your public Git code repository. (Use of Git is encouraged but not required; you may instead upload your individual files directly to Gradescope without involving Git.)
2. A message specification document. For required contents, see Message Specification Document Requirements below.

## Message Specification Document Requirements

* This document MUST include a written summary of the application-layer message protocol you developed for all communications between the client and the server.
* Message formats MUST be documented using Augmented Backus–Naur form (ABNF). See [https://en.wikipedia.org/wiki/Augmented_Backus%E2%80%93Naur_form] for details on ABNF.
* In addition to the ABNF specification, you MUST include some examples of each type of message you have defined.
* You MUST describe the component fields of each message, what constitutes allowed values for each field, and expected receiver actions in response to each message.
* You MUST include a brief description of how you solved the design problem of preventing bank account access from more than one atm_client at a time.

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
