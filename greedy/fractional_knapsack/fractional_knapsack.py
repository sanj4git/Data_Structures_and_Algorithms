# fractional_knapsack

def fractional_knapsack(limit, items):
    """
    limit: Maximum weight of the knapsack you can carry
    items: List of tuples of the form (weight, profit)
    """

    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_profit = 0
    chosen_items = []
    for weight, profit in items:
        if limit >= weight:
            limit -= weight
            total_profit += profit
            chosen_items.append((weight, profit))
        else:
            total_profit += (limit / weight) * profit
            chosen_items.append((limit, (limit / weight) * profit))
            break

    return total_profit, chosen_items


items = [(10, 60), (40, 40), (20, 100), (30, 120)]
limit = 50

print(fractional_knapsack(limit, items))