import re
# Asterisk, Question Mark and Plus########################################################################
# ex1

if __name__=="__main__":
    # p = re.compile(r'a[ab]+c')  # one or more
    # m = p.findall('a ab ac abc aac aabc aaac abababc')  #
    # print(m)
    #
    # p = re.compile(r'a[ab]*c')  # zero wala bhi print karo or more
    # m = p.findall('a ab ac abc aac aabc aaac abababc ')  # [ab]*
    # print(m)
    #
    # p = re.compile(r'a[ab]?c')  # Zero or one,
    # m = p.findall(
    #     'a ab ac abc aac aabc aaac abababc')  # aabc mei a ko gayab kiya / abababc mei se ab ab ko kyun gayab kiya
    # print(m)  # [ab]?: Matches zero or one occurrence of either 'a' or 'b'.

    p = re.compile(r'(ha)+')
    m = p.findall('ha hh aa hahahaha')  # print only last occurance//one or more
    print(m)

    p = re.compile(r'(ha)*')
    m = p.findall('ha hh aa hahahaha')  # zero or more
    print(m)

    p = re.compile(r'(ha)?')
    m = p.findall('ha hh aa hahahaha')  # zero or one
    print(m)

