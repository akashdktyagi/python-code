
def sir_ka_code(s):
    word = [s.lower() for i in speech for s in i.split()]
    word_count = {}
    for w in word:
        word_count[w] = word_count.get(w, 0) + 1
    print(' '.join([w for w, c in word_count.items() if c >= 3]))

def count_word_appearing_for_more_than_3_words(speech_array):
    joined_array = ' '.join(speech_array)
    splitted_array = joined_array.split(" ")
    result_dict={}

    for i in range(len(splitted_array)):
        if (splitted_array[i] in result_dict):
            value = result_dict[splitted_array[i]]
            result_dict[splitted_array[i]] = value+1
        else:
            result_dict[splitted_array[i]]=1
    for key,value in result_dict.items():
        if value>2:
            print(key)




    # result_dict={}
    # for i in range(len(long_list)):
    #     counter=1
    #     if not(long_list[i] in result_dict): # check if the value exist in the dict
    #         for j in range(i+1, len(long_list)):
    #             if long_list[j]==long_list[i]: # if the same value is found, then increment the count by 1
    #                 counter = counter + 1
    #         result_dict[long_list[i]]=counter # add the final counter value in the dict
    #         if counter>2:
    #             return long_list[i]

def temp1():
    s = 'akash is smart'
    list = s.split(" ")
    print(list)

def temp2():
    surname = [i.split()[-1] for i in physicists]
    surname.sort()
    v = (8 * 60 + 5) + 25 * surname.index('Einstein')
    print('{:02d}{:02d}hrs'.format(v // 60, v % 60))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    speech = ['the United States has conducted an operation that killed Osama bin Laden',
              'Abu Bakr al-Baghdadi is dead',
              'the United States launched a targeted operation against that compound',
              'they did a lot of shooting and they did a lot of blasting even not going through the front door You know you would think you go through the door If you are a normal person you say Knock knock  May I come in',
              'After a firefight they killed Osama bin Laden and took custody of his body',
              'He died like a dog',
              'Yet his death does not mark the end of our effort',
              'a beautiful dog a talented dog',
              'We give thanks for the men who carried out this operation',
              'And I dont get any credit for this but thats okay I never do But here we are',
              'May God bless you And may God bless the United States of America',
              'And Im writing a book I think I wrote 12 books All did very well']
    count_word_appearing_for_more_than_3_words(speech)
    sir_ka_code(speech)






