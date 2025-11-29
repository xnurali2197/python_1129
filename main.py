IF ELSE: 🧩 Foydalanuvchi ishga kirish uchun quyidagi 3 bosqichdan o‘tishi kerak:
1. Hujjat topshirish
2. Suhbatdan o‘tish (intervyu)
3. Test sinovidan o‘tish
Dastur foydalanuvchidan har bir bosqich bo‘yicha holatni so‘rashi kerak (masalan, `"ha"` yoki `"yo'q"` deb javob
beriladi).
* Agar foydalanuvchi barcha 3 bosqichni **muvaffaqiyatli** bajargan bo‘lsa → `"Siz ishga qabul qilindingiz!"`
degan xabar chiqsin.
* Agar foydalanuvchi **hujjat topshirmagan** bo‘lsa → `"Avvalo hujjatlaringizni topshiring."` degan ogohlantirish
chiqsin.
* Agar hujjatlar topshirilgan, lekin foydalanuvchi **suhbatdan o‘tmagan** bo‘lsa → `"Suhbatdan o‘tmagansiz."`
* Agar foydalanuvchi hujjat va suhbatdan o‘tgan, lekin **testdan yiqilgan** bo‘lsa → `"Test natijalari yetarli
emas."`
* Boshqa har qanday holatda → `"Jarayon davom etmoqda."` degan xabar chiqsin.
Kirish:
* `docs` — hujjat topshirilganmi? (`"ha"` yoki `"yo'q"`)
* `interview` — suhbatdan o‘tdimi? (`"ha"` yoki `"yo'q"`)
* `test` — testdan o‘tdimi? (`"ha"` yoki `"yo'q"`)
Chiqish:
* Holatga mos xabar chiqariladi.

FOR: 🧩 Foydalanuvchi tomonidan kiritilgan jumladagi har bir so‘zning faqat birinchi harfini olib, ketma-ket
birlashtiring va natijada yangi maxfiy kod (string) hosil qiling.

Kirish: "Salom bu mening yangi loyiham"
Chiqish: "Sbmyl"

Kirish: Bugun havo juda chiroyli
Chiqish: Bhjc

LIST – 1: Berilgan ro‘yxatdagi har bir elementni uning indeksiga ko‘paytirib, yangi ro‘yxat hosil qiling.
ma’lumot: royxat = [4, 7, 2, 5, 1, 10]
Chiquvchi ma’lumot: [0, 7, 4, 15, 4, 50]

LIST – 2 🔍Sizga bir nechta so‘zlardan iborat ro‘yxat beriladi.
Vazifangiz — ushbu ro‘yxatdan **eng uzun so‘zni** va undan keyingi **ikkinchi uzun so‘zni** aniqlash.
Agar uzunliklari bir xil bo‘lgan bir nechta so‘zlar bo‘lsa, ular ro‘yxatda birinchi uchragan tartibda hisobga olinadi.
Masalan:
words = ["dasturlash", "kitob", "shunday", "kompyuter", "ilm", "maktab"]
Chiquvchi ma’lumot:
1-chi eng uzun so‘z: dasturlash
2-chi eng uzun so‘z: kompyuter

STRING: 🧩 Foydalanuvchi tomonidan kiritilgan biror **so‘z yoki matn** har bir harfiga **tartib raqamini**
biriktiring va quyidagi shaklda chiqaring:
* Har bir harf yangi qatordan chiqariladi.
* Harf oldidan uning **tartib raqami** va `-` belgisi bo‘ladi.

Kirish: Python
Chiqish:
1 - P
2 - y
3 - t
4 - h
5 - o
6 - n
STRING SLICE: 🎭Foydalanuvchidan biror ism (string) kiritiladi. Sizning vazifangiz — ushbu ismni quyidagi tarzda
maskalash:
* Faqat **birinchi** va **oxirgi** harflar o‘z holicha qoladi.
* O‘rtadagi barcha harflar o‘rniga `X` belgisi qo‘yiladi.
* Agar ism uzunligi 2 yoki undan kam bo‘lsa, uni o‘zgartirmasdan chiqariladi.

📥Kirish: Muhammad
📤Chiqish: MXXXXXXd

📥Kirish: Sarvarbek
📤Chiqish: SXXXXXXXk

TUPLE – 1: 📌Berilgan `tuple` ichida bir nechta elementlar mavjud. Sizning vazifangiz — ushbu `tuple`dagi har bir
elementni uning indeks raqami bilan birga yangi `tuple` ko‘rinishida ifodalash. Har bir yangi element ikkita
qiymatdan iborat bo‘lsin:
* birinchi qiymat — elementning indeksi (ya’ni tartib raqami),
* ikkinchi qiymat — o‘sha indeksi ostidagi asl element.

my_tuple = ("a", "b", "c", "d")
Natija: ((0, "a"), (1, "b"), (2, "c"), (3, "d"))

TUPLE – 2:
🧩Tuple ichidagi har bir stringni teskari tartibda yozing. Natijani yangi tuple ko‘rinishida qaytaring.
Masalan: ("apple", "banana", "ok") → ("elppa", "ananab", "ko")

DICT – 1: 🔀Kalit va qiymatlarni almashtirish. Berilgan lug‘atda har bir kalit va qiymatni joyini almashtiring.
Misol: {"a": "1", "b": "2"} → {"1": "a", "2": "b"}

DICT – 2: 🐾Quyidagi lug‘atda bir nechta hayvonlar va ularning chiqaradigan tovushlari berilgan:
{"it": "vov", "mushuk": "miyov", "sigir": "muu"}

Namuna:
🧩 Kiritish: it
💻Natija: vov

🧩 Kiritish: ot
💻Natija: Bunday hayvon bazada yo‘q
