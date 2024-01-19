def max_profit(price):
    if len(price) < 2:
        return "Not enough data to calculate profit"

    # Find the first non-zero price as the initial minimum price
    current_min_price = next((p for p in price if p != 0), None)

    if current_min_price is None:
        return "All prices are zero, cannot calculate profit"

    # Initialize variables to keep track of the best buy and sell days
    best_buy_day = price.index(current_min_price)
    best_sell_day = best_buy_day + 1
    max_profit = price[best_sell_day] - current_min_price

    # Iterate through the prices to find the best buy and sell days
    for i in range(best_sell_day + 1, len(price)):
        current_profit = price[i] - current_min_price

        if current_profit > max_profit:
            best_sell_day = i
            max_profit = current_profit

            # Update the best_buy_day only if it's before best_sell_day
            if best_buy_day > best_sell_day:
                best_buy_day = price.index(current_min_price)

        # Update the current minimum price if a lower price is encountered
        if price[i] < current_min_price:
            current_min_price = price[i]
            best_buy_day = i

    return best_buy_day, best_sell_day