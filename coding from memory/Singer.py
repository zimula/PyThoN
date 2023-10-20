from Human import Human
class singer(Human):
    def __init__(self, name, gender, age, genre):
        super().__init__("Singer",name, gender, age)
        self.genre = genre
        self.songs = []
    def greeting(self):
        return f'Hej, jeg hedder {self.name}. Og arbejder som {self.type}'

sin = singer("d", "t", 50, "opera")
print(sin.genre)
print(sin.greeting())