import random

# 1.KISIM
print("\n\n\t\t\t\t\tHoşgeldiniz")
print("\tBurada wifi atak saldırıları için hedefe yönelik wordlist oluşturabilirsiniz.\n\n")
print("Başlamak için 'start' ")
print("Çıkmak için 'exit yazabilirsiniz.")
firstinput = input("Seçiminiz : ")
while True:
    if firstinput == 'start':
        print("\nSistemi durdurmak için 'yeterli' yazınız\n ")
        inputs = []
        sayac = 0

        for i in range(1,10000):
            user_input = input("Lütfen %d. girdinizi girin: "%i)
            if user_input == 'yeterli':
                break
            else:
                inputs.append(user_input)
                sayac = sayac + 1
        print(inputs)

        # 2. KISIM
        dosyaadi = input("Dosya nasıl kaydedilsin : ")
        with open(dosyaadi, "w") as f:
            kombin = 1
            for a in range(sayac):
                kombin = kombin * sayac
            for i in range(0, kombin):
                random_list = []
                random_list = random.sample(inputs, k=len(inputs))
                output = []
                for b in range(0, sayac-1):
                    random_index = random.randint(0, sayac - 1)
                    output.append(inputs[random_index])
                    output2 = ''.join(output)
                    # Yaygın şifreler 8 ile 12 karakter arasında olduğundan default olarak bu şekilde belirlerdim. Bunu değiştirebilirsiniz.
                    if 12 >= len(output2) >= 8 :
                        
                        f.write("%s" %output2)
                        f.write("\n")
                    else:
                         continue

        f.close()
        break
    elif firstinput == 'exit':
       break
    else:
        print("Seçiminizi tekrar yapınız: ")
        firstinput = input("Seçiminiz : ")



