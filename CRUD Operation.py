
# CREATE 2 OBEJECT MODELS INCLUDE 5 TEST CASES USING PYTHON

class Object1:
    def __init__(self,author_name,movie,mobile,channel,car):
        self.author_name = author_name
        self.movie = movie
        self.mobile = mobile
        self.channel = channel
        self.car = car
        self.book_names = []
        self.genres = []
        self.brands = []
        self.shows = []
        self.models = []

    def display_info(self):
        print(self.author_name)
        print(self.movie)
        print(self.mobile)
        print(self.channel)
        print(self.car)
    
    def add_book_name(self,book_name):
        self.book_names.append(book_name)

    def add_genre(self,genre):
        self.genres.append(genre)

    def add_brand(self,brand):
        self.brands.append(brand)

    def add_show(self,show):
        self.shows.append(show)

    def add_model(self,model):
        self.models.append(model)


    def get_book_names(self):
        return self.book_names
    
    def get_genres(self):  
        return self.genres
    
    def get_brands(self):   
        return self.brands
    
    def get_shows(self):    
        return self.shows
    
    def get_models(self):    
        return self.models

    def Update_author_name(self,new_author_name):
        self.author_name = new_author_name
    def Update_movie(self,new_movie_name):
        self.movie = new_movie_name
    def Update_mobile(self,new_mobile_name):
        self.mobile = new_mobile_name
    def update_channel(self,new_channel_name):
        self.channel = new_channel_name
    def Update_car(self,new_car_name):
        self.car = new_car_name

    def delete_book_name(self,book_name):
        if book_name in self.books:
            self.books.remove(book_name)
    def delete_genre(self,genre):
        if genre in self.genres:
            self.genres.remove(genre)
    def delete_brand(self,brand):
        if brand in self.brands:
            self.brands.remove(brand)
    def delete_show (self,show):
        if show in self.shows:
            self.shows.remove(show)
    def delete_model(self,model):
        if model in self.models:
            self.models.remove(model)


class Object2:
    def __init__(self,book_name,genre,brand,show,model):
        self.book_name = book_name
        self.genre = genre
        self.brand = brand
        self.show = show
        self.model = model
        self.author = None
        self.movie = None
        self.mobile = None
        self.channel = None
        self.car = None

    def display_info(self):
        print(self.book_name)
        print(self.genre)
        print(self.brand)
        print(self.show)
        print(self.model)
    
    def set_author_name(self,author_name):
        self.author = author_name
        author_name.add_book_name(self)

    def set_movie_name(self,movie):
        self.movie = movie
        movie.add_genre(self)

    def set_mobile(self,mobile):
        self.mobile = mobile
        mobile.add_brand(self) 

    def set_channel(self,channel):
        self.channel= channel
        channel.add_show(self)

    def set_car(self,car):
        self.car= car
        car.add_model(self)
    

    def get_author_name(self):
        return self.author_name
    def get_movie_name(self):    
        return self.movie_name
    def get_mobile(self):
        return self.mobile
    def get_channel(self):
        return self.channel
    def get_car(self):
        return self.car
    
    def update_book_name(self,new_book_name):
        self.book_name = new_book_name
    def update_genre(self,new_genre):
        self.genre = new_genre
    def update_brand(self,new_brand):
        self.brand = new_brand
    def update_channel(self,new_channel):
        self.channel = new_channel
    def update_model(self,new_model):
        self.model = new_model


# Creating instances of Object1 and Object2
        
Test_case1_object1 = Object1("Maharishi Veda Vyasa","Devera","Oneplus Nord CE 2","Discovery","TATA")
Test_case1_object2= Object2("Bhagavad Gita","Action","ONEPLUS","National Geographic","Altroz")


Test_case2_object1 = Object1("Jawaharlal Nehru","Salaar","IQOO Z7 Pro","Star Sports","BMW")
Test_case2_object2= Object2("Discovery of India","Action","VIVO","Cricket","BMW X7")

Test_case3_object1 = Object1("R.K Narayan","Karthikeya 2 ","Iphone 15 Pro","MAA TV","Audi")
Test_case3_object2= Object2("The Guide","Adventure","I PHONE ","Singer","RS Q8")

Test_case4_object1 = Object1("J.K Rowling","Kanchana","Relame 6 Pro","Gemini","Maruti")
Test_case4_object2= Object2("Harry Potter and the Philsopher's Stone","Horror","Realme","Serials","Maruti Brezza")

Test_case5_object1 = Object1("George Orwell","Cold Case","MI","V6","Mahindra")
Test_case5_object2= Object2("1984","Suspense","Xiomi","NEWS","Mahindra Thar")

# Create 

Test_case1_object1.display_info()

Test_case5_object2.display_info()


#Accessing and Manipulating the data using CRUD Operations

print(Test_case1_object1.author_name)
print(Test_case1_object2.book_name)
print(Test_case5_object1.movie)
print(Test_case5_object2.genre)

# Update Movie and Genre name

Test_case1_object1.Update_movie("Toxic")
Test_case1_object2.update_genre("Action Thriller")

print(Test_case1_object1.movie)
print(Test_case1_object2.genre)

# Delete a Test_Case

Test_case1_object1.delete_show(Test_case1_object2)

# check if Test_Case is deleted 

print(Test_case1_object1.get_shows())

