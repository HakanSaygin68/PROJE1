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
    def __init__(self, borrower_name, book, date):
        self.book = book
        self.borrower_name = borrower_name
        self.date = date

class Kitaplik():
    "Burada satin alma kitap ekleme funksiyonlari vardir."
    kitapliklar = []

    def __init__(self, kitap_adi, kitap_fiyati, kontenjan):
        self.kitap_adi = kitap_adi
        self.kitap_fiyati = kitap_fiyati
        self.kontenjan = kontenjan
        self.ogrenciler = []

    @classmethod
    def kitap_ekle(cls, kitap_adi, kitap_fiyati, kontenjan):
        yeni_kitap = cls(kitap_adi, kitap_fiyati, kontenjan)
        cls.kitapliklar.append(yeni_kitap)
        print(f"{kitap_adi} kitabi eklendi.")

    def satin_alma(self, ogr_adi,):
        if self.kontenjan > 0:
            self.ogrenciler.append(ogr_adi) 
            print(f"{ogr_adi} isimli öğrenci, {self.kitap_adi} kitap satin aldi.")
            self.kontenjan -= 1
        else:
            print(f"{self.kitap_adi} kitap kalmadi.")

"Örnekler:"
Kitaplik.kitap_ekle("Investment", 10, 3)
Kitaplik.kitap_ekle("Cristiano Ronaldo", 10, 4)
Kitaplik.kitap_ekle("Hayat", 20, 2)

kitap1 = Kitaplik.kitapliklar[0] 
kitap2 = Kitaplik.kitapliklar[1]
kitap3 = Kitaplik.kitapliklar[2]

kitap3.satin_alma("recep",)
kitap3.satin_alma("mehmet",)
kitap3.satin_alma("Kemal",)



student1 = Student("Akif", "Yildiz", 17, numara=200)
student2 = Student("Recep", "Öztürk", 29, numara=201)
student3 = Student("Deniz", "Tas", 45, numara=203)

borrow1 = BorrowBook("Akif", "Harry Potter", "09.2023")
borrow2 = BorrowBook("Recep", "Berserk", "08.2023")
borrow3 = BorrowBook("Deniz", "Yüzüklerin Efendisi", "09.2023")

print("Ögrenci 1 =", student1.name, student1.surname, student1.age)
print("Ögrenci 2 =", student2.name, student2.surname, student2.age)
print("Ögrenci 3 =", student3.name, student3.surname, student3.age)
print("Harry Potter kitabini ödünc alan ögrenci:", borrow1.borrower_name, borrow1.book, borrow1.date)
print("Berserk kitabini ödünc alan kisi:", borrow2.borrower_name, borrow2.book, borrow2.date)
print("Yüzüklerin Efendisi kitabini ödünc alan kisi:", borrow3.borrower_name, borrow3.book, borrow3.date)
