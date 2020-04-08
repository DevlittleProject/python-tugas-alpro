#Contoh pengulangan for sederhana

angka = [1,2,3,4,5]
for x in angka:
	print(x)

#Contoh pengulangan for

buah = ["nanas", "apel", "jeruk"]

for makanan in buah:
	print "Saya suka makan", makanan


#Contoh penggunaan Nested Loop

i = 2
while(i < 10):
	j = 2
	while(j <= (i/j)):
		if not(i%j): break
		j = j + 1
		if (j > i/j) : print i, " is prime"
		i = i + 1
	print "Good bye!"