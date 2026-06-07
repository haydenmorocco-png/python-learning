import random
winning_numbers = [4, 12, 23, 31, 38, 47]

def generate_ticket():
    ticket = []
    while len(ticket) < 6:
        num = random.randint(1, 49)
        if num not in ticket:
            ticket.append(num)
    return sorted(ticket)

def check_ticket(ticket, winning_numbers):
    matches = 0
    correct_numbers = []
    for number in ticket:
        if number in winning_numbers:
            matches +=1
            correct_numbers.append(number)
    return matches , correct_numbers
        
def prize(matches):
    prize_money = 0
    if matches == 6:
       prize_money =  1000000
    elif matches == 5:
        prize_money = 1000
    elif matches == 4:
        prize_money = 100
    elif matches == 3:
        prize_money = 10
    return prize_money

def number_of_tickets():
    while True:
        number_of_tickets = input("How many tickets would you like ($2 per ticket): ")
        try:
            num_of_ticks = int(number_of_tickets)
            return num_of_ticks
        except ValueError:
            print("Enter a valid number of tickets: ")


def main():
    prize_money = 0
    num_of_ticks = number_of_tickets()
    i = 1
    print(winning_numbers)
    while i <= num_of_ticks:
        ticket = generate_ticket()
        matches = check_ticket(ticket, winning_numbers)
        temp_prize = prize(matches[0])
        prize_money += temp_prize
        print(f"Ticket {i}. {ticket} → {matches[0]} match(es) {matches[1]} ${temp_prize}")
        i += 1
    print(f"Total spent: ${num_of_ticks * 2}")
    print(f"Total won: ${prize_money}")
    print(f"Net result: ${prize_money - (num_of_ticks * 2)}")

main()