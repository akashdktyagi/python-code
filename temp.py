class PrimeNo:
    result = []

    def __init__(self, num_list):

        self.num_list = num_list

    def findPrimeNumber(self):

        for i in range(len(self.num_list)):
            isPrime = True

            for j in range(2, (self.num_list[i])):
                if self.num_list[i] % j == 0:
                    isPrime = False
                    break;

            if isPrime == True:
                self.result.append(self.num_list[i])

        return self.result

num_list = [649, 778, 652, 653, 912, 402, 917, 536,
            664, 922, 284, 158, 415, 672,
            673, 33, 419, 414, 421, 811, 683,
            48, 818, 566, 567, 310, 580, 838, 199,
            586, 458, 460, 337, 728, 604, 94, 607,
            865, 354, 230, 367, 752, 625, 371, 505,
            635, 893, 382, 767]



if __name__ == '__main__':
    objPrime = PrimeNo(num_list)
    print(objPrime.findPrimeNumber())
    # answer = objPrime.findPrimeNumber()
    # print(answer)