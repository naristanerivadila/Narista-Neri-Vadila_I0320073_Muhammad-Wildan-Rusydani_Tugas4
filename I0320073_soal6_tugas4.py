print("SOAL 6")

#!/usr/bin/python

a = 4   #4 = 0000 0100
b = 11  #11 = 0000 1011
c = 0

print('a berisi angka', a, 'desimal atau', bin(a), 'biner')
print('b berisi angka', b, 'desimal atau', bin(b), 'biner')

c = a | b;
print("a). Hasil dari c = a | b     : ", c)

c = a >> b;
print("b). Hasil dari c = a >> b    : ", c)

c = a ^ b;
print("c). Hasil dari c = a ^ b     : ", c)

c = ~a;
print("d). Hasil dari c = ~a        : ", c)

c = b & a;
print("e). Hasil dari c = b & a     : ", c)
