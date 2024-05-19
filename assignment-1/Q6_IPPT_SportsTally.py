class IPPT:
    def __init__(self):
        self.log = {}

    def add_record(self, list_of_tuples):
        for item in list_of_tuples:
             if item[0] in self.log:
                 self.log[item[0]] = self.log[item[0]] + item[1]
             else:
                 self.log[item[0]] = item[1]

        print(self.log)


    def check(self, category):
        if category in self.log:
            #return self.log[category]
            print(self.log[category])
        else:
            #return 0
            print('0')

if __name__=='__main__':
   # ippt2024=IPPT()

    ## Open Test-case 6.1

    # ippt2024 = IPPT()
   # ippt2024.add_record([('pushup', 10)])
    #ippt2024.add_record([('pushup', 10), ('situp', 20), ('2.4run', 9.3)])
    # ippt2024.add_record([('2.4run', 10.1)])
    # ippt2024.check('2.4run')

    # if list_of_tuples[0] in self.log:
    #     self.log[list_of_tuples[0]]= self.log[list_of_tuples[0]] + list_of_tuples[1]
    #
    # else:
    #      self.log[list_of_tuples[0]] = list_of_tuples[1]
    # print(self.log)

    ## Open Test-case 6.2

    ippt2024 = IPPT()
    ippt2024.add_record([('pushup', 10)])
    ippt2024.add_record([('pushup', 10), ('2.4run', 9.3)])
    ippt2024.add_record([('pushup', 10)])
    ippt2024.check('situp')

