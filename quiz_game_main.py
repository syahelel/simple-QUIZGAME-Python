print("Selamat Datang di QUIZ GAME!!")

playing = input("apakah anda ingin bermain? Y/N ")
if playing.upper() != "Y":
    quit()

print("OkAY! Let's Play...")
nilai = 0

answer =input("1. CPU Kepanjangan dari?\nA. Central Processing Unit\nB. Center Processor User\nC. Cache Proxy Utility\nJAWAB: ")
if answer.upper() == "A":
     print("Anda Benar!\n")
     nilai +=1
else:
     print("Maaf Anda Salah\n")
     
answer =input("2. Perangkat Hardware yang Menghasilkan Output Suara?\nA. Monitor\nB. Keyboard\nC. Speaker\nJAWAB: ")
if answer.upper() == "C":
     print("Anda Benar!\n")
     nilai +=1
else:
     print("Maaf Anda Salah\n")

answer =input("3. RAM kepanjangan dar?\nA. Random Access Memory\nB. Rally Access Memory\nC. Random Axel Motor\nJAWAB: ")
if answer.upper() == "A":
     print("Anda Benar!\n")
     nilai +=1
else:
     print("Maaf Anda Salah\n") 

answer =input("4. Transmitter Berfungsi Untuk?\nA. Menerima Sinyal\nB. Memancarkan Sinyal\nC. Menolak Sinyal\nJAWAB: ")
if answer.upper() == "B":
     print("Anda Benar!\n")
     nilai +=1
else:
     print("Maaf Anda Salah\n")  

answer =input("5. GPU Kepanjangan dari?\nA. Grade Post Unit\nB. Graphic Processing Unit\nC. Graphic Processor Unit\nJAWAB: ")
if answer.upper() == "B":
     print("Anda Benar!\n")
     nilai +=1
else:
     print("Maaf Anda Salah\n")  
     
print("--------------------------")
print(f"anda benar {nilai} Soal")
print(f"Nilai anda {((nilai/5) * 100)}%")