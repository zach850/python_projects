def dis(price, discount):
    disc = 100 - (discount)
    percent = disc / 100
    total_discount = price * percent
    return total_discount


print(dis(89, 20))
