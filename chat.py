import nltk
from nltk.chat.util import Chat, reflections

#respon chatbot
pola = [
    ['(hai|halo|hey)', ['Halo!', 'Hai, ada yang bisa saya bantu?']],
    ['(saya|aku) ingin (.*)', ['Kenapa Anda ingin %2?', 'Anda ingin %2 karena apa?']],
    ['(saya|aku) (.*)', ['Mengapa Anda %2?', 'Apakah ada alasan mengapa Anda %2?']],
    ['siapa kamu?', ['Saya adalah bot sederhana.', 'Anda bisa memanggil saya bot.', 'Ini bapak budi', 'Ini ibu budi']],
    ['apa kabar?', ['Saya hanyalah sebuah program, jadi saya tidak punya perasaan.']],
    ['(.*) berapa (.*)(harga|biaya)(.*)', ['Maaf, saya tidak bisa memberikan informasi tentang harga.']],
    ['burung apa itu, man?', ['Burung puyuh']],
    ['aku merasa (.*)', ['Kenapa Anda merasa %1?', 'Mengapa Anda merasa %1?', 'Bagaimana perasaan Anda ketika %1?']],
    ['aku sedih', ['Saya turut merasa sedih mendengarnya. Ceritakan lebih banyak tentang perasaan Anda.']],
    ['aku senang', ['Saya senang mendengarnya! Ada hal spesifik yang ingin Anda bagikan tentang kebahagiaan Anda?']],
    ['aku kesepian', ['Saya bisa mendengar bahwa Anda merasa kesepian. Apakah ada yang bisa saya lakukan untuk membantu?']],
    ['(.*) curhat (.*)', ['Tentu, saya siap mendengarkan curhatan Anda. Silakan ceritakan apa yang Anda rasakan.']],
    ['(.*) putus cinta (.*)', ['Saya turut merasa sedih mendengarnya. Ceritakan lebih banyak tentang hubungan Anda.']],
    ['(.*) stres (.*)', ['Stres bisa menjadi hal yang sulit. Apakah Anda ingin berbicara lebih banyak tentang penyebabnya?']],
    ['(.*) depresi (.*)', ['Depresi adalah masalah serius. Saya sarankan Anda mencari bantuan dari profesional medis.']],
    ['(.*) bosan (.*)', ['Ada banyak hal yang bisa dilakukan untuk mengatasi kebosanan. Apa hobi atau kegiatan yang Anda sukai?']],
    ['(.*) tidak percaya diri (.*)', ['Rendahnya rasa percaya diri bisa menjadi tantangan. Apakah ada yang bisa saya bantu untuk meningkatkan kepercayaan diri Anda?']],
    ['(.*) cemas (.*)', ['Cemas bisa menjadi hal yang mengganggu. Apakah ada teknik tertentu yang biasa Anda gunakan untuk mengatasi kecemasan?']],
    ['(.*) marah (.*)', ['Marah adalah emosi yang alami. Apakah Anda ingin berbicara lebih banyak tentang apa yang membuat Anda marah?']],
    ['(.*) bersalah (.*)', ['Bersalah adalah perasaan yang umum. Apakah Anda ingin berbicara tentang apa yang membuat Anda merasa bersalah?']],
    ['(.*) putus asa (.*)', ['Putus asa adalah perasaan yang sulit. Apakah ada hal-hal yang biasanya membuat Anda merasa lebih baik?']],
    ['keluar', ['Sampai jumpa!', 'Terima kasih telah berbicara dengan saya.']],
    ['(.*)', ['Maaf, saya tidak mengerti.', 'Maaf, saya tidak bisa membantu dengan itu.']]
]

chatbot = Chat(pola, reflections)

def mulai_chat():
    print("Selamat datang! Silakan mulai berbicara dengan bot. Ketik 'keluar' untuk mengakhiri percakapan.")
    while True:
        user_input = input("Anda: ")
        if user_input.lower() == 'keluar':
            break
        else:
            response = chatbot.respond(user_input)
            print("Bot:", response)


mulai_chat()
