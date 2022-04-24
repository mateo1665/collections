import random
spellijst = ["monopoly","poker","mens erger je niet","kat en muis","30 secondes","jachtseizoen","dammen","schaken"]
def spelprogamma(spellijst,minimum = 3,maximum = 10):
    nummer = random.choice(range(minimum,maximum))
    return random.choices(spellijst, k=nummer)
print(spelprogamma(spellijst))
print(spelprogamma(spellijst,1))
print(spelprogamma(spellijst,1,3))