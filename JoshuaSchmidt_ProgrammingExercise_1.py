# JoshuaSchmidt_ProgrammingExercise_1 - Pre-sell Cinema Tickets

# Number of tickets purchased
def buy_tickets():
    tickets = int(input("How many tickets would you like to purchase (1-4)?: "))
    return tickets

# Number of tickets sold.
def sold_tickets():
    total_tickets = 10
    total_buyers = 0

# Loop to process ticket sales
    while total_tickets > 0:

        print("\nTickets remaining:", total_tickets)
        request = buy_tickets()

        if request < 1 or request > 4:
            print("Error: You can only buy 1-4 tickets.")

        elif request > total_tickets:
            print("Error: Not enough tickets remaining.")

        else:
            total_tickets -= request
            total_buyers += 1

            print("Ticket purchase completed.")
            print("Remaining tickets:", total_tickets)

    print("\nAll tickets have been purchased.")
    print("Total number of buyers:", total_buyers)

# Program to
sold_tickets()
