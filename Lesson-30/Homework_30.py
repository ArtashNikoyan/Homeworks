# 1․ Գրել MyShows class, որը․
#    - __init__ ում կստանա
#      -- սերիալի անունը (պետք է լինի տեքստ),
#      -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ),
#      -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
#      -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 1,
#      -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
#      -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
#    - բոլոր ատրիբուտները կլինեն private,
#    - կունենա getter բոլոր ատրիբուտների համար,
#    - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
#    - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից սահմանելու հնարավորություն լինի,
#    - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
#    - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան:


class MyShows:
    shows = []
    stars = []
    
    # validators
    @staticmethod
    def __is_str(a):
        if isinstance(a, str):
            return True
        raise ValueError('Invalid input')
    
    @staticmethod
    def __is_int(a):
        if isinstance(a, int):
            return True
        raise ValueError('Invalid input')
    
    @staticmethod
    def __validate_stars_list(lst):
        if isinstance(lst, list) and len(lst) >= 2:
            return True
        raise ValueError('Invalid input')
    
    # get, set, del
    @property
    def serial_name(self):
        return self.__serial_name
    
    @property
    def platform(self):
        return self.__platform
    
    @property
    def year(self):
        return self.__year
    
    @property
    def watched_last_epizode(self):
        return self.__watched_last_epizode
    
    @watched_last_epizode.setter
    def watched_last_epizode(self, value):
        self.__watched_last_epizode = value
    
    @property
    def user_rating(self):
        return self.__user_rating
    
    @user_rating.setter
    def user_rating(self, value):
        self.__user_rating = value
    
    @user_rating.deleter
    def user_rating(self):
        self.__user_rating = None
    
    @property
    def stars_list(self):
        return self.__stars_list
    
    # magic methods
    def __init__(self, serial_name, platform, year, stars_list, watched_last_epizode=1, user_rating=None):
        if self.__is_str(serial_name) and self.__is_str(platform):
            self.__serial_name = serial_name
            self.__platform = platform
        
        if self.__is_int(year):
            self.__year = int(year)
        
        if self.__is_int(watched_last_epizode):
            self.__watched_last_epizode = watched_last_epizode
        
        if (self.__is_int(user_rating) or user_rating is None) and (1 <= user_rating <= 10):
            self.__user_rating = user_rating
        
        if self.__validate_stars_list(stars_list):
            self.__stars_list = stars_list
            
    def __repr__(self):
        return f"{self.__serial_name} - {self.__platform} - {self.__year} - {self.__watched_last_epizode} - {self.__user_rating} - {self.__stars_list}"
    
    # instance methods
    
    def add_show(self):
        name = input("input the serial name: ")
        platform = input("input the platform name: ")
        year = int(input("input the year: "))
        stars_list = input("input the star list (sep by space): ").split()
        watched_last_epizode = int(input("input the watched last epizode: "))
        user_rating = int(input("input the user rating: "))
        
        m = MyShows(name, platform, year, stars_list, watched_last_epizode, user_rating)
        
        MyShows.shows.append(m)
        print('Film successfully entered: \n\t', m)
    
    def del_show(self):
        film_name = input("input the film name: ")
        
        for show in MyShows.shows:
            if show.serial_name.lower() == film_name.lower():
                MyShows.shows.remove(show)
                print('Film successfully deleted: \n\t', film_name)
                return
        print("Film not found")
        
    def add_star(self, star):
        self.__stars_list.append(star)
    
    def remove_star(self, star):
        if star in self.__stars_list:
            self.__stars_list.remove(star)


    
m1 = MyShows('Harry', 'Python', 2020, ['Daniel Redglife', 'Hermiona Granger'], 5, 10)
print(m1)
print(m1.serial_name)
print(m1)

m1.add_show()
m1.add_show()
print(MyShows.shows)