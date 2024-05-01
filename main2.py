
def print_pattern():
    star_a1 = 1
    star_d = 4
    star_n=1

    dash_a1 = 3
    dash_d = 4
    dash_n = 1

    clm_length=19
    for i in range(0,10):
        print()
        if i == 0:
            print('*******************', end='')
            # print()
        elif i % 2 == 0: # 3,7,11,15
            total_dash = dash_a1 + dash_d * (dash_n-1)

            val = int(clm_length/2)
            for j in range(0,int((clm_length-total_dash)/2)):
                print('*', end='')

            for j in range(0,total_dash):
                print('-', end='')

            for j in range(0, int((clm_length - total_dash) / 2)):
                print('*', end='')
            dash_n = dash_n + 1
        else: # 1,5,9,13  = a1 + (n-1)d  d=4, a1=1  n= j
            total_stars = star_a1 + star_d * (star_n-1) # Find the total stars for each row
            val = int(clm_length/2) # where to place them, find the mid point
            for j in range(0,int((clm_length-total_stars)/2)):
                print('-', end='')

            for j in range(0,total_stars):
                print('*', end='')

            for j in range(0, int((clm_length - total_stars) / 2)):
                print('-', end='')
            star_n = star_n + 1




# 3,7,11 ,15  a1 + d(n-1)   0+
    # *******************
    # ---------*---------
    # ********---********
    # -------*****-------
    # ******-------******
    # -----*********-----
    # ****-----------****
    # ---*************---
    # **---------------**
    # -*****************-

def sir_ka_code_1():
    for i in range(10):
        if i == 0:
            print('*' * 19)
        elif i % 2 == 1:
            print('-' * (10 - i) + '*' * (2 * i - 1) + '-' * (10 - i))
        else:
            print('*' * (10 - i) + '-' * (2 * i - 1) + '*' * (10 - i))

def sir_ka_code(physicists):
    surname = [i.split()[-1] for i in physicists]
    surname.sort()
    v = (8 * 60 + 25) + 25 * surname.index('Einstein')
    print('{:02d}{:02d}hrs'.format(v // 60, v % 60))

def find_albert_speech(physicists):
    surname_list=[]
    for item in physicists:
        surname_list.append(item.split(" ")[-1])

    sorted_surnames = sorted(surname_list)
    index = sorted_surnames.index('Einstein')
    elapsed_minute = 25*index
    hour_component = 25*index / 60
    remainder_component = elapsed_minute % 60
    final_hour = str(int(8 + hour_component))
    final_min = str(int(25 + remainder_component))
    print(final_hour+":"+final_min)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sir_ka_code_1()
    # print_pattern()
    # physicists = ['Erwin Schroedinger', 'Wolfgang Pauli', 'Max Born', 'Niels Bohr', 'Max Planck', 'Madame Curie',
    #               'Hendrik Antoon Lorentz', 'Albert Einstein', 'Paul Langevin', 'Louis Victor de Broglie', 'Paul Dirac',
    #               'Werner Heisenberg']
    # find_albert_speech(physicists)
    # sir_ka_code(physicists)






