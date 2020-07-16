Best_Friends = ["Bul", "Bambang"]
friends = ["Nathan", "Bimo", "Kevin", "Bobi", "Andi"]
friends.extend(Best_Friends) #untuk menggabungkan 2 string yang ada
print(friends)
friends.append("Boy") #untuk menambahkan item kedalam list
print(friends)
friends.insert(3, "Kevin") #untuk menambahkan item setelah index yang dimasukkan
print(friends)
friends.remove("Andi") #untuk mendelete item tersebut dari list
print(friends)
friends.pop() #mendelete item terakhir yang ada di dalam list
print(friends)
print(friends.index("Nathan")) #untuk mencari index item yang ada di list
print(friends.count("Kevin")) #untuk menghitung berapa kali item yanng ada di list muncul
friends.sort()
print(friends) #mengurutkan dari huruf/angka paling kecil ke paling besar
friends2 = friends.copy() #mengopy list yang ada ke list lain
print(friends2)
