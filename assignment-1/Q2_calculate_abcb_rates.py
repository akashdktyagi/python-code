
# NOT WORKING

def calculate(abcb_rates, amount):
    effective_rate = 0
    remaining_amount = amount
    for k, v in abcb_rates.items():
        lower_limit = int(k.split("-")[0].split("$")[1])
        upper_limit = int(k.split("-")[1].split("$")[1])
        temp_amount = min(remaining_amount, upper_limit - lower_limit)
        effective_rate += (temp_amount / amount) * v
        remaining_amount -= temp_amount
        if remaining_amount <= 0:
            break
    if remaining_amount > 0:
        effective_rate += (remaining_amount / amount) * 0.05
    return effective_rate

# def calculate(abcb_rates,amount):
#     effective_rate=0
#     remaining_amount=amount
#     for k,v in abcb_rates.items():
#         lower_limit = int(k.split("-")[0].split("$")[1])
#         upper_limit = int(k.split("-")[1].split("$")[1])
#         temp_amount = upper_limit-lower_limit
#         if (remaining_amount<upper_limit):
#             effective_rate = effective_rate + remaining_amount/amount * v
#             break
#         else:
#             effective_rate = effective_rate + (temp_amount / amount) * v
#             remaining_amount = remaining_amount - temp_amount
#
#     if remaining_amount>0:
#         effective_rate = effective_rate + (remaining_amount / amount) * 0.05
#
#
#
#     return effective_rate

if __name__ == '__main__':
    # abcb_rates = {
    #     '$0 - $10000': 3.00,
    #     '$10000 - $30000': 4.00,
    # }
    # print(calculate(abcb_rates, 40000))
    #
    #
    # abcb_rates = {
    #     '$0 - $10000': 2.00,
    #     '$10000 - $30000': 2.50,
    #     '$30000 - $90000': 3.00,
    #     '$90000 - $100000': 7.00
    # }
    # print(calculate(abcb_rates, 50000))

    abcb_rates = {
        '$0 - $50000': 2.88,
        '$50000 - $51000': 9.18,
    }
    print(calculate(abcb_rates, 100000))
