picture = open('cat.bmp', 'rb') # открывает картинку '1cat.bmp'  как бинарный файл для чтения
from_file = picture.readlines()
picture.close() 
new_picture = open('cat.bmp', 'wb') # создает новый файл '11cat.bmp' и открывает его для записи
all_from_picture = picture.readlines() # считываем ВСЁ из файла с картинкой
new_picture.writelines(all_from_picture) # записываем ВСЁ в новый файл
message = "Malware is a form of malicious software in which any file or program can be used to harm a computer user. Different types of malware include worms, viruses, Trojans and spyware."
new_picture.write(message.encode()) # функция encode() переводит строку в бинарный список, чтобы его можно было записать в файл
picture.close()
new_picture.close()