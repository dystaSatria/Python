names = ['Reza','John','Kevin','Mike']
years = [1998,2002,1998,2000]


# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")

# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0, "Sena")

# 3- "Deniz" ismini listeden siliniz.
names.remove("Deniz")

# 4- "Deniz" isminin indeksi nedir ? (Deniz'i sildikten sonra bu işlem hatalı olacaktır, öncesinde yapılmalıydı.)
# Deniz'in indeksini bulmak için silinmeden önce bu işlem yapılmalıydı. Ancak, yine de örneğin nasıl yapılacağını gösteriyorum:
# deniz_index = names.index("Deniz")

# 5- "Ali" listenin bir elemanı mıdır ?
is_ali_in_list = "Ali" in names

# 6- Liste elemanlarını ters çevirin.
names.reverse()

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()

# 9- str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
car_brands = "Chevrolet, Dacia".split(", ")

# 10- years dizisinin en büyük ve en küçük elemanı nedir?
min_year = min(years)
max_year = max(years)

# 11- years dizisinde kaç tane 1998 değeri vardır ?
count_1998 = years.count(1998)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
brands = []
for i in range(3):
    brand = input(f"Marka {i+1} giriniz: ")
    brands.append(brand)

# Not: Kodların çalışabilmesi için names ve years listelerinin tanımlı olması gerekmektedir.
# Ayrıca, "Deniz" isminin indeksi ve "Deniz" isminin silinmesi ile ilgili adımların yerleri değiştirilmelidir.
