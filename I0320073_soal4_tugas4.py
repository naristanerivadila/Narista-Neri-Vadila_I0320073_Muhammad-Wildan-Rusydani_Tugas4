print('SOAL 4')

usia = '21 tahun'
status = 'Telah lulus ujian kualifikasi'

#menampilkan persyaratan kursus
print('Persyaratan kursus online: ')
print("1. Usia minimal  : ", usia)
print("2. Status        : ", status)

print("Para pendaftar diharuskan memenuhi persyaratan khusus tersebut untuk dapat mengikuti kursus online.")
print("Jawablah pertanyaan di bawah ini : ")

#input usia
usia = (input("Berapa usia kamu: "))

if (usia > str(21)) :
      print("Keterangan : Anda dapat mendaftarkan di kursus")

else :
      print("Keterangan : Anda tidak dapat mendaftar di kursus")

#input status
status = (input("Apakah Anda sudah lulus ujian kualifikasi (Y/T) : "))

if (status == 'Y') :
      print("Keterangan : Anda dapat mendaftar di kursus")

else :
      print("Keterangan : Anda tidak dapat mendaftar di kursus")

x = 'kedua syarat terpenuhi'
y = 'salah satu syarat tidak terpenuhi'

print("Berdasarkan keterangan di atas, Anda dinyatakan dapat mengikuti kursus jika ", x)
print("Dan Anda dinyatakan tidak dapat mengikuti kursus jika ", y)
