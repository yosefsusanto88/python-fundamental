# List
list_kota = ['bandung', 'cimahi', 'sumedang', 'sukabumi', 'ciamis']

for i, kota in enumerate(list_kota):
    print(i, kota)

## 0 sampai 4
print('-------------------------------------')
for i in range(5):
    print('perulangan ke -', i)

## 10 sampai 16
print('-------------------------------------')
for i in range(10, 16):
    print(i)

## Bilangan genap kelipatan 2
print('-------------------------------------')
for i in range(2, 30, 2):
    print(i)

## Bilangan ganjuil kelipatan 2
print('-------------------------------------')
for i in range(3, 21, 2):
    print(i)

## For dengan tuple
print('-------------------------------------')
tuplebuah = ['mangga', 'jeruk', 'semangka', 'apel', 'pisang', 'delima']

for buah in tuplebuah:
    print(buah)

## For dengan string
print('-------------------------------------')
for karakter in ('indonesiaid'):
    print(karakter)