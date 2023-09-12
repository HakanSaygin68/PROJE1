class Student():
    "Bu sinif ögrenci kaydi icin olusturulan siniftir."    
    def __init__(self, name, surname, age, **kwargs):
        self.name = name 
        self.surname = surname 
        self.age = int(age)

        for key, value in kwargs.items():
            setattr(self, key, value)

class BorrowBook():
    "Burada kayıt olan kişi kitap ödünç alıyor"
    def __init__(self, name, book, date):
        self.book = book
        self.name = name
        self.date = date
student1 = Student("Akif", "Yildiz", 17, numara=200)
student2 = Student("Recep", "Öztürk", 29, numara=201)
student3 = Student("Deniz", "Tas", 45, numara=203)

borrow1 = BorrowBook("Akif", "Harry Potter", "09.2023")
borrow2 = BorrowBook("Recep", "Berserk", "08.2023")
borrow3 = BorrowBook("Deniz", "Yüzüklerin Efendisi", "09.2023")

print("Ögrenci 1 =", student1.name, student1.surname, student1.age)
print("Ögrenci 2 =", student2.name, student2.surname, student2.age)
print("Ögrenci 3 =", student3.name, student3.surname, student3.age)
print("Harry Potter kitabini ödünc alan ögrenci:", borrow1.name, borrow1.book, borrow1.date)
print("Berserk kitabini ödünc alan kisi:", borrow2.name, borrow2.book, borrow2.date)
print("Yüzüklerin Efendisi kitabini ödünc alan kisi:", borrow3.name, borrow3.book, borrow3.date)
