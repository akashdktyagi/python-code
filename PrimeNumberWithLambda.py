
# class PrimeNo:
#     def isPrime(self,number):
#         for i in range(2, number):
#             if number % i == 0:
#                 return False
#         return True


if __name__ == '__main__':
    num_list = [649, 778, 652, 653, 912, 402, 917, 536,
                    664, 922, 284, 158, 415, 672,
                    673, 33, 419, 414, 421, 811, 683,
                    48, 818, 566, 567, 310, 580, 838, 199,
                    586, 458, 460, 337, 728, 604, 94, 607,
                    865, 354, 230, 367, 752, 625, 371, 505,
                    635, 893, 382, 767]

    # obj = PrimeNo()
    # print(obj.isPrime(7))

    is_prime = lambda number: all(number % i != 0 for i in range(2, number))
    prime_numbers = [num for num in num_list if is_prime(num)]
    print(prime_numbers)





