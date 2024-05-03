class BaseNetflix:
    def __init__(self, title, cast, year):
        self.title = title
        self.cast = cast
        self.year = year

    def display(self):
        print("Title: " + self.title)
        print("Cast: " + str(self.cast))
        print("Year: " + str(self.year))



class Movie(BaseNetflix):
    def __init__(self, title, cast, year, length):
        super.__init__(title,cast,year)
        self.length=length

    def display(self):
        print("Title: " + self.title)
        print("Cast: " + str(self.cast))
        print("Year: " + str(self.year))
        print("Length: " + str(self.length))



class TVseries(BaseNetflix):
    def __init__(self, title, cast, year, season):
        super.__init__(title,cast,year)
        self.season=season

    def display(self):
        print("Title: " + self.title)
        print("Cast: " + str(self.cast))
        print("Year: " + str(self.year))
        print("Season: " + str(self.season))

    def update_season(self):
        self.season=self.season+1


class StructuredNetflix:
    def __init__(self, title, cast, length, year):
        self.title = title
        self.cast = cast
        self.length = length
        self.year = year

    def display(self):
        print("Title: " + self.title)
        print("Cast: " + str(self.cast))
        print("Length: " + str(self.length))
        print("Year: " + str(self.year))

#Write your class here
class Netflix:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def display(self):
        print("Title: " + self.title)
        print("Year: " + str(self.year))


if __name__=='__main__':
    # Test your code here
    netflix = Netflix('The call', 2020)
    netflix.display()

    # Normal
    netflix_structured = StructuredNetflix('The call', ['Park Shine-hye', 'Jun Jong-seo', 'Kim Sung-ryoung'], '1h 52m', 2020)
    netflix_structured.display()

    netList_struct_list = [StructuredNetflix('The call', ['Park Shine-hye', 'Jun Jong-seo', 'Kim Sung-ryoung'], '1h 52m', 2020),
          StructuredNetflix('Alive', ['Yoo Ah-in', 'Park Shine-hye'], '1h 38m', 2020),
          StructuredNetflix('Miss Americana', ['Taloy Swift'], '1h 25m', 2020)]

    # Check
    # we want to find all of the ones that Park Shine-hye acted and shows in 2020 except the movie we just watched ('The call')
    condition_Actor='Park Shine-hye'
    condition_Year=2020
    condition_except_title='The call'

    for element in netList_struct_list:
        if element.title!=condition_except_title and element.year==condition_Year and condition_Actor in element.cast:
            print("****Filtered Result****")
            element.display()

