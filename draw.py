# Check if ticket is lucky
def isLucky(ticket: []):
    middle = int(len(ticket)/2)
    right = [x for x in ticket[(middle):]]
    left = [x for x in ticket[:middle]]
    if (sum(right) == sum(left)):
        return True
    return False


# fill tickets[] with arrays with values from [0,0,0,0,0,0] to [9,9,9,9,9,9]
def fillTickets(length: int = 3):
    length = length*2
    tickets = []
    for i in range(10**length):
        ticket = []
        num = i
        for j in range(length):
            ticket.append(num % 10)
            num //= 10
        tickets.append(ticket[::-1])
    return tickets


# fill tickets in reverse order
def fillTicketsFaster(length: int = 3):
    length = length*2
    tickets = []
    for i in range(10 ** length):
        ticket = [0] * length
        num = i
        for j in range(length - 1, -1, -1):
            ticket[j] = num % 10
            num //= 10
        tickets.append(ticket)
    return tickets


# Main function
def getAllLuckyTickets(tickets: []):
    luckyTickets = []
    for ticket in tickets:
        if isLucky(ticket):
            luckyTickets.append(ticket)
    return luckyTickets


tickets = fillTicketsFaster()
print(len(getAllLuckyTickets(tickets)))
