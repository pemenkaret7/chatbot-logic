# Fungsi untuk merespon pertanyaan pengguna
def respon_Bot(inputan):
    
    # Mengubah input menjadi huruf kecil untuk mempermudah bot mengenali pertanyaan
    inputan = inputan.lower()
    
    #pertanyaan yang dikenali chatbot
    if "halo" in inputan or "hai" in inputan:
        return "Halo bang! Ada yang bisa saya bantu?"
    elif "kamu siapa?" in inputan:
        return "Saya adalah Chatbot. saya jomblo."
    elif "apa kabar?" in inputan:
        return "Saya hanyalah sebuah program komputer, tidak memiliki perasaan, maka dari itu saya jomblo!"
    elif "terima kasih" in inputan:
        return "Sama-sama! Jika Anda memiliki pertanyaan lain, jangan ragu untuk bertanya."
    elif "exit" in inputan or "quit" in inputan:
        return "Terima kasih. See u broo!"
    else:
        return "Pertanyaanmu rumit seperti hidupmu,silahkan ulangi lagi!."

# Fungsi utama untuk menjalankan chatbot
def main():
    print("halo bang!.silahkan bertanya dan ketik 'exit' untuk keluar.")

    while True:
        inputan_pengguna = input(" Anda: ")
        response = respon_Bot(inputan_pengguna) 
        print("Chatbot:", response)  

        if "exit" in inputan_pengguna or "quit" in inputan_pengguna: 
            break


    main()
