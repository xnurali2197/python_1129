docs = input("Hujjat topshirilganmi? (ha/yo'q): ")
interview = input("Suhbatdan o'tdingizmi? (ha/yo'q): ")
test = input("Testdan o'tdingizmi? (ha/yo'q): ")

if docs == "ha" and interview == "ha" and test == "ha":
    print("Siz ishga qabul qilindingiz!")
elif docs == "yo'q":
    print("Avvalo hujjatlaringizni topshiring.")
elif interview == "yo'q":
    print("Suhbatdan o'tmagansiz.")
elif test == "yo'q":
    print("Test natijalari yetarli emas.")
else:
    print("Jarayon davom etmoqda.")

