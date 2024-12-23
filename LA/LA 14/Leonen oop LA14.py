class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    def describeSpiderman(self):
        print(f" {self.name} {self.age}")
       
class Tobey(Spiderman):
    def __init__(self, name, age, movie_title):
        super().__init__(name, age)
        self.movie_title = movie_title
l1 = Tobey("Tobey", "20", "spider1")
print(l1.name.upper(), l1.movie_title)
       
class Andrew(Spiderman):
    def __init__(self, name, age, movie_title):
        super().__init__(name, age)
        self.movie_title = movie_title
m1 = Andrew("Andrew", "21", "spider2")
print(m1.name.upper(), m1.movie_title)

class Tom(Spiderman):
    def __init__(self, name, age, movie_title):
        super().__init__(name, age)
        self.movie_title = movie_title
n1 = Tom("Tom", "22", "spider3")
print(n1.name.upper(), n1.movie_title)