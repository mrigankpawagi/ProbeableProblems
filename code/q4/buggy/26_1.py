def max_profit(price):
    positive_prices = [p for p in price if p > 0]
    if not positive_prices or len(set(positive_prices)) == 1:
        min_price = min(positive_prices)
        min_index = price.index(min_price)
        max_index = price.index(min_price, min_index + 1) if price.count(min_price) > 1 else min_index
        if min_index == max_index:
            return 0,0
        return min_index, max_index
    min_price = min(positive_prices)
    min_index = price.index(min_price)
    max_price = max(price[min_index:])
    max_index = price.index(max_price, min_index)
    if min_index == max_index:
        return 0,0# start looking for max_price from min_index
    return min_index, max_index