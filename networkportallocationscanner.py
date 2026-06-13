""""
14. Network Port Allocation Scanner

Scenario: An interactive CLI configuration initialization tool requests a port assignment. The script must validate inputs continuously until a safe choice is committed.
Requirements:
Run an infinite input polling loop that prompts the user for a listening port number.
Convert the string input into an integer. Use error handling blocks to catch parsing issues if strings are typed.
Add validation conditions to confirm the integer sits between 1 and 65535.
Acceptance Criteria:
Typing "abc" or 70000 must trigger an error message and immediately prompt the user again.
Typing 8080 must break the loop and print: Port 8080 allocated successfully.
"""



while True:
    try:
        port_number= int(input("Enter a listening port number: "))
    except ValueError:
            print("Error:  please enter a valid number .")
    else:
            if port_number <1 or port_number > 65535:
                 print("Error: port must be between 1 and 65535.")
            else:
                 print(f"port {port_number} allocated successfuly.")
                 break
            
       
        

