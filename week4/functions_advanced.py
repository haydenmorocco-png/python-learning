def get_stats(test_scores):
    lowest = min(test_scores)
    highest = max(test_scores)
    total = 0
    for s in test_scores:
        total += s
    avg = total / len(test_scores)
    stats = lowest, highest, avg
    return stats
    
def compund_interest(princple, rate, years):
    """
    Calculate compound interest.

    Args:
        principal: starting amount in dollars
        rate: annual interest rate as decimal (e.g. 0.05 for 5%)
        years: number of years

    Returns:
        Final amount after compound interest and args
    """
    future_value = princple * ((1 + rate) ** years)
    interest = future_value, princple, rate, years
    return interest

def make_coffee(size="Medium", milk=True, shots=1):
    if milk == False:
        milk = 'black'
    else:
        milk = "with milk"
    coffee = size, milk, shots
    return coffee

stats = get_stats([5, 6, 7, 10])
print(f"Lowest: {stats[0]}")
print(f"Highest: {stats[1]}")
print(f"Average: {stats[2]}")
interest = compund_interest(1000, 0.07, 10)
print(f"${interest[1]} at {(100 * interest[2]):.2f}% for {interest[3]} years: ${interest[0]:.2f}")
coffee = make_coffee()
print(f"{coffee[0]} coffee, {coffee[2]} shot(s), {coffee[1]}")
coffee = make_coffee("Large")
print(f"{coffee[0]} coffee, {coffee[2]} shot(s), {coffee[1]}")
coffee = make_coffee("Small", False, 2)
print(f"{coffee[0]} coffee, {coffee[2]} shot(s), {coffee[1]}")
coffee = make_coffee(milk=False, shots=3)
print(f"{coffee[0]} coffee, {coffee[2]} shot(s), {coffee[1]}")