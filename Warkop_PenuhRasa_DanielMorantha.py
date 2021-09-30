#Daniel Morantha
#2019230088

import random                                # saran secara acak

import sys

from random import sample

import os           # untuk menghapus perintah sebelumnya

from time import sleep      # bila tidak ada respon langsung keluar peringatan default = 3mnt



font_list = ['big']
random_font = random.sample(font_list, 1)

try:    
    from pyfiglet import Figlet
    f = Figlet(font='{}'.format(*random_font))
    print(f.renderText('Penuh Rasa by Daniel Morantha'))
except ImportError or ModuleNotFoundError:
    pass



random_choice = ["Roti Bakar", "Bubur Ayam", "Internet (Indomie telor kornet)", 'Roti Bakar', 'Teh Manis']     # If something is unavailable orfor suggesting random things

cart = []


new_list = []


def lqimit():             # Jika pesananan melebihi 10 pesanan
    cls()
    print('Maaf Anda tidak dapat memesan lebih dari 10 pesanan')
    sleep(3)


def cls():

    if sys.platform.startswith('win32' or 'win64' or 'win86'):
        os.system('cls')
    else:
        os.system('clear')




    
def limit_reached():        # melebihi batas
    cls()
    print('Maaf sepertinya Anda telah mencapai batas maksimum memesan item ini. Mungkin Anda dapat mencoba sesuatu yang lain. \n')
    order()


    
def get_name(shop_name = 'Warkop Penuh Rasa by Daniel Morantha'):
    name = input("Silahkan masukan nama Anda?\n\n> ")
    name1 = name.title()
    cls()
    
    if len(name1) > 0 and not name1.isdigit():
        print("Hallo {}, Selamat datang di {}." .format(name1, shop_name))
        print('')
        order()

        
    elif len(name1) == 0:
        print('Error, Silahkan Masukan Nama Anda')
        get_name()

        
    elif name1.isdigit():
        print('Mohon untuk memasukan abjad')
        print('')
        get_name()

        
    else:
        print('')
        print('Maaf saya tidak mengerti apa yang anda pesan')
        print('')
        get_name()

        
def empty_response():  # respon jawaban kosong
    cls()
    print("Tidak ada jawaban, silahkan jawab")
    sleep(3)

# "Roti Bakar", "Bubur Kacang ijo", "Internet (Indomie telor kornet)", 'kopi', 'Teh Manis']
    
def unavailable():    # digunakan jika stok tidak tersedia
    cls()
    random1 = random.sample(random_choice, 1)
    abc = input('Maaf, hal yang Anda cari saat ini tidak tersedia.\n \nApakah Anda ingin mencoba menu lezat lainnya dari kami {}? (Enter  \'Iya\' atau \'Tidak\')\n\n> ' .format(*random1))
    print('')
    
    if abc == 'Iya' or abc == 'IYA' or abc == 'iya' or abc == 'y' or abc == 'Y' and abc.isalpha() and len(abc) > 0:
        new_list.append(*random1)
        
        if new_list.count('Roti Bakar') > 0:
            roti_bakar()
            
        elif new_list.count('Bubur Ayam') > 0:
            bubur_ayam()
            
        elif new_list.count('Internet (Indomie telor kornet)') > 0:
            internet()
            
        elif new_list.count('Kopi') > 0:
            kopi()
            
        elif new_list.count('Pisang Bakar') > 0:
            pisang_bakar()
            
    elif abc == 'tidak' or abc == 'TIDAK' or abc == 'Tidak' or abc == 't' or abc == 'T' and abc.isalpha() and len(abc) > 0:
        cls()
        print('oke lah kalau begitu')
        print('')
        order()
        
    elif abc != 'iya' or abc != 'Iya' or abc != 'IYA' or abc != 'y' or abc != 'Y' or abc != 'tidak' or abc != 'Tidak' or abc != 'TIDAK' or abc != 'T' or abc != 't':
        print('Hanya enter \'Iya\' atau \'Tidak\'')
        unavailable()
        
    elif len(abc) == 0:
        print('Error, Tidak ada jawaban.')
        unavailable()
        
    elif abc != abc.isalpha():
        print('Mohon, Hanya Enter \'Iya\' atau \'Tidak\'')
        unavailable()
        
    else:
        print('Maaf saya tidak mengerti.')
        unavailable()



def order2(nama_toko = 'Warkop Penuh Rasa'):  # untuk memilih menu pada tampilan awal.
    print('')
    choice = input('Apakah Anda ingin memesan sesuatu yang lain? (Masukan Enter \'Iya\' atau \'Tidak\' )\n\n> ')
    
    if choice == 'iya' or choice == 'IYA' or choice == 'Iya' or choice == 'Y' or choice == 'y' and choice.isalpha() and len(choice) > 0:
        cls()
        order()
        return cart
    
    elif choice == 'Tidak' or choice == 'tidak' or choice == 'TIDAK' or choice == 'T' or choice == 't' and choice.isalpha() and len(choice) > 0:
        cls()
        print("Berikut adalah pesanan Anda: ") #\n{} .format(*cart))
        print('')
        for items in cart:
            print('{}\n' .format(items))
        print('')
        abc = input('Terima Kasih sudah memesan makanan di {}.\n\nTekan Enter untuk keluar \n \n' .format(nama_toko))
        
        if len(abc) > 0:
            exit()
            
        else:
            exit()
            
    elif choice != 'iya' or choice != 'tidak':
        empty_response()
        order2()
        
    elif len(choice) == 0:
        empty_response()
        order2()
        
    elif choice != choice.isalpha():
        empty_response()
        order2()
        
    else:
        print('Maaf, saya tidak mengerti.')
        order2()

        
# function acak menu       
def random_suggestion(): # Saran secara acak
    cls()
    suggestion_sample = random.sample(random_choice, 1)
    will = input('Kami pikir Anda meyukai {}.\n \nApakah Anda ingin melanjutkan? Masukan Enter \'Iya\' atau \'Tidak\'.\n\n> '.format(*suggestion_sample))
    
    if will == 'iya' or will == 'IYA' or will == 'Iya' or will == 'Y' or will == 'y' and will.isalpha() and len(will) > 0:
        new_list.append(*suggestion_sample)

       # Roti Bakar", "Bubur Kacang ijo", "Internet (Indomie telor kornet)", 'Telor 1/2 matang', 'Teh Manis'

        if new_list.count('Roti Bakar') > 0:
            roti_bakar()
            
        elif new_list.count('Bubur Ayam') > 0:
            bubur_ayam()
            
        elif new_list.count('Internet (Indomie telor kornet)') > 0:
            internet()
            
        elif new_list.count('Kopi') > 0:
            kopi()
            
        elif new_list.count('Pisang Bakar') > 0:
            pisang_bakar()
            
    elif will == 'tidak' or will == 'TIDAK' or will == 'Tidak' or will == 'T' or will == 't' and will.isalpha() and len(will) > 0:
        cls()
        print('Okelah kalau begitu.')
        print('')
        order()
    elif will != 'tidak' or will != 'TIDAK' or will != 'Tidak' or will != 'T' or will != 't' or will != 'Iya' or will != 'IYA' or will != 'iya' or will != 'Y' or will != 'y':
         empty_response()
         random_suggestion()


# function roti_bakar  
def roti_bakar():
    cls()
    p_rasa = input("Rasa apa yang Anda mau? \n \na) Coklat \nb) Stawberry \n\nMasukan Pilihan, lalu enter \'a\', \'b\', atau enter \'1\' untuk kembali ke menu. \n> ")
    
    if p_rasa  == 'a' or p_rasa == 'A' or p_rasa == 'a)' or p_rasa == 'A)' and p_rasa.isalpha() and len(p_rasa) > 0:
        cls()
        
        while cart.count('10 buah dari Roti Bakar.') == 0:
            
            try:
                pieces = int(input("Dan berapa banyak potongan-potongan roti bakar yang Anda ingin?\n\n> "))
                
                if pieces == 1:
                    cls()
                    print("Berikut Pesanan Anda:\n\n{} Roti Bakar coklat dengan 1 potongan." .format(pieces))
                    cart.append("{} Roti Bakar coklat.".format(pieces))
                    order2()
                    return counter
                
                elif pieces == 0:
                    empty_response()
                    roti_bakar()
                    
                elif pieces > 10:
                    limit()
                    roti_bakar()
                    
                elif pieces != 1:
                    cls()
                    print("Berikut adalah pesanan Anda:\n\n{} buah Roti Bakar Coklat dengan banyak potongan." .format(pieces))
                    cart.append("{} pieces of Double sided Bread cheesecake.".format(pieces))
                    order2()
                    
                else:
                    empty_response()
                    roti_bakar()
                    
            except ValueError:
                empty_response()
                roti_bakar()
                
        if cart.count('10 buah pemesanan, pemesanan terbatas.') > 0:
            limit_reached()
            roti_bakar()
            
        else:
            limit_reached()
            roti_bakar()
            
    elif p_rasa  == 'b' or p_rasa == 'B' or p_rasa == 'b)' or p_rasa == 'B)' and p_rasa.isalpha() and len(p_rasa) > 0:
        cls()
        try:
            pieces = int(input("Dan berapa banyak potongan-potongan roti bakar apakah Anda ingin satu sisi?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Berikut Pesanan Anda:\n\n{} roti bakar Stawberry dengan banyak potongan.".format(pieces))
                cart.append("{} roti bakar Stawberry dengan banyak potongan.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                roti_bakar()
                
            elif pieces > 10:
                limit()
                roti_bakar()
                
            elif pieces != 1:
                cls()
                print('Berikut Pesanan Anda:\n\n{} roti bakar Stawberry dengan banyak potongan.' .format(pieces))
                cart.append("{} roti bakar Stawberry dengan banyak potongan." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                roti_bakar()
                
        except ValueError:
            empty_response()
            roti_bakar()
            
    elif p_rasa != 'a' or p_rasa != 'b':
        try:
            try:
                if int(p_rasa) == 1:
                    order()
                    
                elif int(p_rasa) > 1 or int(p_rasa) < 1 or int(p_rasa) == 0:
                    empty_response()
                    roti_bakar()
                    
            except p_rasa !=1:
                empty_response()
                roti_bakar()
                
        except TypeError:
            empty_response()
            roti_bakar()
            
    elif p_rasa != p_rasa.isalpha():
        empty_response()
        roti_bakar()
        
    elif len(p_rasa) == 0:
        empty_response()
        roti_bakar()
        
    else:
        print('Maaf saya tidak mengerti.')
        roti_bakar()


# function bubur ayam        
def bubur_ayam():
    cls()
    p_selera = input("Apakah Anda ingin memakai?\n\na) daun sledri \nb) jeroan \nc) kacang \nd) daun bawang \n \nEnter dengan pilihan huruf \'a\', \'b\', \'c\', \'d\', atau Enter \'1\' Untuk kembali ke menu.\n\n> ")
    
    if p_selera  == 'a' or p_selera == 'A' or p_selera == 'a)' or p_selera == 'A)' and p_selera.isalpha() and len(p_selera) > 0:
        cls()
        b_selera = input('Dan seberapa banyak yang Anda inginkan?\n\na) Sedikit \nb) Banyak\n\n> ')
        
        if b_selera == 'a' or b_selera == 'A' or b_selera == 'a)' or b_selera == 'A)':
            cls()
            
            while cart.count('10 buah bubur ayam pakai daun sledri.') == 0:
                try:
                    pieces = int(input("Dan berapa banyak bubur ayam pakai daun sledri sedkit yang Anda inginkan?\n\n> "))
                    
                    if pieces == 1:
                        print('')
                        print("Berikut Pesanan Anda:\n\n{} bubur ayam pakai daun sledri." .format(pieces))
                        cart.append("{} bubur ayam pakai daun sledri.".format(pieces))
                        order2()
                        return cart
                    
                    elif pieces == 0:
                        empty_response()
                        bubur_ayam()
                        
                    elif pieces > 10:
                        limit()
                        bubur_ayam()
                        
                    elif pieces != 1:
                        cls()
                        print("Berikut Pesanan Anda:\n\n{} bubur ayam pakai daun sledri." .format(pieces))
                        cart.append("{} bubur ayam pakai daun sledri.".format(pieces))
                        order2()
                        return cart
                    
                    else:
                        empty_response()
                        bubur_ayam()
                        
                except ValueError:
                    empty_response()
                    bubur_ayam()
                    
            if cart.count('10 buah bubur ayam pakai daun sledri..') > 0:
                limit_reached()
                bubur_ayam()
                
            else:
                limit_reached()
                bubur_ayam()
                
        elif b_selera == 'b' or b_selera == 'B' or b_selera == 'B)' or b_selera =='b)':
                unavailable()
                
        elif b_selera != b_selera.isalpha():
                empty_response()
                bubur_ayam()
                
        elif len(b_selera) == 0:
                empty_response()
                bubur_ayam()
                
        elif b_selera != 'a' or b_selera != 'b':
                empty_response()
                bubur_ayam()
        else:
                print("Maaf Saya Tidak Mengerti")
                bubur_ayam()
                
    elif p_selera  == 'b' or p_selera == 'B' or p_selera == 'b)' or p_selera == 'B)' and p_selera.isalpha() and len(p_selera) > 0:
        cls()
        
        try:
            pieces = int(input("Dan berapa banyak bubur ayam pakai daun sledri banyak yang Anda inginkan?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Berikut Pesanan Anda:\n\n{} bubur ayam pakai daun sledri banyak.".format(pieces))
                cart.append("{} bubur ayam pakai daun sledri banyak.".format(pieces))
                order2()
                return cart
            
            elif pieces > 10:
                limit()
                bubur_ayam()
                
            elif pieces == 0:
                empty_response()
                bubur_ayam()
                
            elif pieces != 1:
                cls()
                print('Berikut Pesanan Anda:\n\n{} bubur ayam pakai daun sledri banyak.' .format(pieces))
                cart.append("{} bubur ayam pakai daun sledri banyak." .format(pieces))
                order2()
                
            elif len(pieces) >= 0:
                empty_response()
                bubur_ayam()
                
        except ValueError:
            empty_response()
            bubur_ayam()
            
    elif p_selera == 'c' or p_selera == 'C' or p_selera == 'c)' or p_selera == 'C)' and p_selera.isalpha() and len(p_selera) >0:
        cls()
        
        try:
            pieces = int(input("Dan berapa banyak bubur ayam pakai kacang yang Anda inginkan??\n\n> "))
            if pieces == 1:
                cls()
                print("Berikut Pesanan Anda:\n\n{} bubur ayam pakai kacang.".format(pieces))
                cart.append("{} bubur ayam pakai kacang.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                bubur_ayam()
                
            elif pieces > 10:
                limit()
                bubur_ayam()
                
            elif pieces != 1:
                cls()
                print('Berikut Pesanan Anda:\n\n{} bubur ayam pakai kacang.' .format(pieces))
                cart.append("{} bubur ayam pakai kacang." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                bubur_ayam()
                
        except ValueError:
            empty_response()
            bubur_ayam()
            
    elif p_selera == 'd' or p_selera == 'D' or p_selera == "D)" or p_selera =='d)' and p_selera.isalpha() and len(p_selera) > 0:
        unavailable()
        
    elif p_selera != 'a' or p_selera != 'b' or p_selera != 'c' or p_selera != 'd':
        try:
            try:
                if int(p_selera) == 1:
                    order()
                    
                elif int(p_selera) > 1 or int(p_selera) < 1 or int(p_selera) == 0:
                    empty_response()
                    bubur_ayam()
                    
            except choice !=1:
                empty_response()
                bubur_ayam()
                
        except TypeError:
            empty_response()
            bubur_ayam()
            
    elif p_selera != p_selera.isalpha():
        empty_response()
        bubur_ayam()
        
    elif len(p_selera) == 0:
        empty_response()
        bubur_ayam()
        
    else:
        print('Maaf, saya tidak mengerti.')



# Function internet
def internet():
    cls()
    p_selera = input("cita rasa apa yang mau di pakai ?\n\na) pedes \nb) tanpa pedes \n \nMasukan Pilihan Huruf, lalu Enter \'a\', \'b\' atau enter \'1\' untuk kembali ke menu.\n\n> ")
    
    if p_selera == 'a' or p_selera == 'A' or p_selera == 'A)' or p_selera == 'a)' and p_selera.isalpha() and len(p_selera) > 0:
        cls()
        
        p_kepedasan  = input('Berapa tingkat kepedasan Anda?\n\na) 25% \nb) 50% \nc) 75% \n \nMasukan Pilihan Huruf, lalu Enter \'a\', \'b\', \'c\', atau enter \'1\' untuk kembali ke menu.\n\n> ')
        
        if p_kepedasan == 'a' or p_kepedasan == 'A' or p_kepedasan == 'a)' or p_kepedasan == 'A)' and p_kepedasan.isalpha() and len(p_kepedasan) > 0:
            cls()
            
            try:
                j_pesanan = int(input('Dan berapa banyak internet yang Anda inginkan?\n\n> '))
                if j_pesanan == 1:
                    cls()
                    print('Berikut Pesanan Anda:\n\n{} internet dengan tingkat kepedasan 25%.' .format(j_pesanan))
                    cart.append('{} internet dengan tingkat kepedasan 25%.' .format(j_pesanan))
                    order2()
                    return cart
                
                if j_pesanan == 0:
                    empty_response()
                    internet()
                    
                elif j_pesanan > 10:
                    limit()
                    internet()
                    
                elif j_pesanan != 1:
                    cls()
                    print('Berikut Pesanan Anda:\n\n{} internet dengan tingkat kepedasan 25%.' .format(j_pesanan))
                    cart.append('{} internet dengan tingkat kepedasan 25%.' .format(j_pesanan))
                    order2()
                    return cart
                
                else:
                    empty_response()
                    internet()
                    
            except ValueError:
                empty_response()
                internet()
                
        elif p_kepedasan == 'b' or p_kepedasan == 'B' or p_kepedasan == 'b)' or p_kepedasan == 'B)' and p_kepedasan.isalpha() and len(p_kepedasan) > 0:
            cls()
            
            try:
                amount = int(input('Dan berapa banyak internet yang Anda inginkan??\n\n> '))
                if amount == 1:
                    cls()
                    print('Berikut Pesanan Anda:\n\n{} internet dengan tanpa pedas.' .format(amount))
                    cart.append('{} internet dengan tanpa pedas.' .format(amount))
                    order2()
                    return cart
                
                elif amount > 10:
                    limit()
                    internet()
                    
                elif amount > 1:
                    cls()
                    print('Berikut Pesanan Anda:\n\n{} internet dengan tanpa pedas.' .format(amount))
                    cart.append('{} internet dengan tanpa pedas.' .format(amount))
                    order2()
                    return cart
                
                elif amount == 0:
                    empty_response()
                    internet()
                    
                else:
                    empty_response()
                    internet()
                    
            except ValueError:
                empty_response()
                internet()
                
        elif p_kepedasan == 'c' or p_kepedasan == 'C' or p_kepedasan == 'c)' or p_kepedasan == 'C)' and p_kepedasan.isalpha() and len(p_kepedasan) > 0:
            unavailable()
            
        elif p_kepedasan != 'a' or p_kepedasan != 'b' or p_kepedasan != 'c':
            try:
                try:
                    if int(p_kepedasan) == 1:
                        order()
                        
                    elif int(p_kepedasan) > 1 or int(p_kepedasan) < 1 or int(p_kepedasan) == 0:
                        empty_response()
                        internet()
                        
                except p_kepedasan !=1:
                    empty_response()
                    internet()
                    
            except TypeError:
                empty_response()
                internet()
                
        elif p_kepedasan != p_kepedasan.isalpha():
            print('mohon hanya memasukan Abjad.')
            print('')
            internet()
            
        elif len(p_kepedasan) == 0:
            empty_response()
            internet()
            
        else:
            print('Maaf, Saya tidak mengerti.')
            print('')
            internet()
            
    

# function kopi
        
def kopi():
    cls()
    p_kopi = input("Kopi Apa yang Anda pesan?\n\na) Hitam \nb) Cappucino \nc) Hitam Susu \nd) Hitam atjen\n\n> ")
    
    if p_kopi  == 'a' or p_kopi == 'A' or p_kopi == 'a)' or p_kopi == 'A)' and p_kopi.isalpha() and len(p_kopi) > 0:
        cls()
        choco = input('Dan disajikan secara apa kopi hitam yang di inginkan?\n\na) panas \n\n> ')
        
        if choco == 'a' or choco == 'A' or choco == 'a)' or choco == 'A)':
            cls()
            
            try:
                pieces = int(input("Dan berapa banyak kopi hitam panas yang Anda inginkan?\n\n> "))
                
                if pieces == 1:
                    cls()
                    print("Berikut pesanan Anda:\n\n{} kopi hitam panas." .format(pieces))
                    cart.append("{} kopi hitam panas.".format(pieces))
                    order2()
                    return cart
                
                elif pieces == 0:
                    empty_response()
                    kopi()
                    
                elif pieces > 10:
                    limit()
                    kopi()
                    
                elif pieces != 1:
                    cls()
                    print("Berikut pesanan Anda:\n\n{} kopi hitam panas." .format(pieces))
                    cart.append("{} kopi hitam panas.".format(pieces))
                    order2()
                    return cart
                
                else:
                    empty_response()
                    kopi()
                    
            except ValueError:
                empty_response()
                kopi()
                
       
            
    elif p_kopi  == 'b' or p_kopi == 'B' or p_kopi == 'b)' or p_kopi == 'B)' and p_kopi.isalpha() and len(p_kopi) > 0:
        cls()

        choco = input('Dan disajikan secara apa kopi Cappucino yang di inginkan?\n\na)Dingin \n\n> ')

        if choco == 'a' or choco == 'A' or choco == 'a)' or choco == 'A)':
            cls()


        try:
            pieces = int(input("Dan berapa banyak kopi Cappucino dingin yang Anda inginkan?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Berikut Pesanan Anda:\n\n{} buah kopi Cappucino dingin.".format(pieces))
                cart.append("{} kopi Cappucino dingin.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                kopi()
                
            elif pieces > 10:
                limit()
                kopi()
                
            elif pieces != 1:
                cls()
                print('Berikut Pesanan Anda:\n\n{} kopi Cappucino panas.' .format(pieces))
                cart.append("{}kopi Cappucino panas." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                kopi()
                
        except ValueError:
            empty_response()
            kopi()
            
            
    elif p_kopi == 'c' or p_kopi == 'C' or p_kopi == 'c)' or p_kopi == 'C)' and p_kopi.isalpha() and len(p_kopi) >0:
        cls()
        choco = input('Dan disajikan secara apa kopi Hitam Susu yang di inginkan?\n\na)Panas \n\n> ')

        if choco == 'a' or choco == 'A' or choco == 'a)' or choco == 'A)':
            cls()

        try:
            pieces = int(input("Dan berapa banyak kopi Hitam Susu Panas yang Anda inginkan?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Berikut Pesanan Anda:\n\n{} kopi Hitam Susu Panas.".format(pieces))
                cart.append("{} kopi Hitam Susu Panas.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                kopi()
                
            elif pieces > 10:
                limit()
                kopi()
                
            elif pieces != 1:
                cls()
                print('Berikut Pesanan Anda:\n\n{} kopi Hitam Susu Panas.' .format(pieces))
                cart.append("{} kopi Hitam Susu Panas." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                kopi()
                
        except ValueError:
            empty_response()
            kopi()
            
    elif p_kopi == 'd' or p_kopi == 'D' or p_kopi == "D)" or p_kopi =='d)' and p_kopi.isalpha() and len(p_kopi) > 0:
        cls()
        choco = input('Dan disajikan secara apa kopi Hitam atjen yang di inginkan?\n\na)Panas \n\n> ')

        if choco == 'a' or choco == 'A' or choco == 'a)' or choco == 'A)':
            cls()
        try:
            pieces = int(input("Dan berapa banyak kopi Hitam atjen Panas yang Anda inginkan??\n\n> "))
            
            if pieces == 1:
                cls()
                print("Berikut Pesanan Anda:\n\n{} kopi Hitam atjen Panas.".format(pieces))
                cart.append("{} kopi Hitam atjen Panas.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                kopi()
                
            elif pieces > 10:
                limit()
                kopi()
                
            elif pieces != 1:
                cls()
                print('Berikut Pesanan Anda:\n\n{} kopi Hitam atjen Panas.' .format(pieces))
                cart.append("{} kopi Hitam atjen Panas." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                kopi()
                
        except ValueError:
            empty_response()
            kopi()
            
    elif p_kopi != 'a' or p_kopi != 'b' or p_kopi != 'c' or p_kopi != 'd':
        empty_response()
        kopi()
        
    elif choice != choice.isalpha():
        empty_response()
        kopi()
        
    elif len(p_kopi) == 0:
        empty_response()
        kopi()
        
    else:
        print('Maaf, saya tidak mengerti apa yang Anda pesan.')
        kopi()


#function pisang_bakar
        
def pisang_bakar():
    cls()
    pb_rasa = input('Rasa apa yang ingin Anda Pesan?\n \na) Keju \nb) Coklat \nc) Coklat Keju \n\nMohon masukan huruf, lalu Enter \'a\', \'b\' atau \'c\'.\n\n> ')
    
    if pb_rasa  == 'a' or pb_rasa == 'A' or pb_rasa == 'a)' or pb_rasa == 'A)' and pb_rasa.isalpha() and len(pb_rasa) > 0:
        unavailable()
        
    elif pb_rasa == 'b' or pb_rasa == 'B' or pb_rasa == 'b)' or pb_rasa == 'B)' and pb_rasa.isalpha() and len(pb_rasa) > 0:
        cls()
        
        try:
            pieces = int(input("Dan berapa banyak Pisang Bakar Coklat yang Anda inginkan?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Berikut Pesanan Anda:\n\n{} Pisang Bakar Coklat.".format(pieces))
                cart.append("{} Pisang Bakar Coklat.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                pisang_bakar()
                
            elif pieces > 10:
                limit()
                pisang_bakar()
                
            elif pieces != 1:
                cls()
                print('Berikut Pesanan Anda:\n\n{} Pisang Bakar Coklat.' .format(pieces))
                cart.append("{} Pisang Bakar Coklat." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                pisang_bakar()
                
        except ValueError:
            empty_response()
            pisang_bakar()
            
    elif pb_rasa == 'c' or pb_rasa == 'C' or pb_rasa == 'c)' or pb_rasa == 'C)' and pb_rasa.isalpha() and len(pb_rasa) > 0:
        cls()
        
        try:
            pieces = int(input("Dan berapa banyak Pisang Bakar Coklat Keju yang Anda inginkan?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Berikut Pesanan Anda:\n\n{} Pisang Bakar Coklat Keju.".format(pieces))
                cart.append("{} Pisang Bakar Coklat Keju.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                pisang_bakar()
                
            elif pieces > 10:
                limit()
                pisang_bakar()
                
            elif pieces != 1:
                cls()
                print('Berikut Pesanan Anda:\n\n{} Pisang Bakar Coklat Keju.' .format(pieces))
                cart.append("{} Pisang Bakar Coklat Keju." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                pisang_bakar()
                
        except ValueError:
            empty_response()
            pisang_bakar()
            
    elif pb_rasa != 'c' or pb_rasa != 'C':
        empty_response()
        pisang_bakar()
        
    elif pb_rasa != pb_rasa.isalpha():
        print('Mohon, masukan abjad.')
        print('')
        pisang_bakar()
        
    elif len(pb_rasa) == 0:
        empty_response()
        pisang_bakar()
        
    else:
        print('Maaf saya tidak mengerti.')
        print('')
        pisang_bakar()


#function order

def order():
    print("Berikut adalah menu kami: \n\na) Roti Bakar \nb) Bubur Ayam \nc) Internet (Indomie telor kornet) \nd) kopi \ne) Pisang Bakar \nf) Saran pesanan dari kami")
    print('')
    p_order = input("Masukan Pilihan, lalu enter \'a\', \'b\', \'c\', \'d\', \'e\', \'f\' atau enter \'1\' untuk keluar program.\n\n> ")
    
    if p_order == 'a' or p_order == 'A' or p_order == 'a)' or p_order == 'A)' and p_order.isalpha() and len(p_order) > 0:
       roti_bakar()
        
    elif p_order == 'b' or p_order == 'B' or p_order == 'b)' or p_order == 'B)' and p_order.isalpha() and len(p_order) > 0:
        bubur_ayam()
        
    elif p_order == 'c' or p_order == 'C' or p_order == 'C)' or p_order == 'c)' and p_order.isalpha() and len(p_order) > 0:
        internet()
        
    elif p_order == 'd' or p_order == 'D' or p_order == 'D)' or p_order == 'd)' and p_order.isalpha() and len(p_order) > 0:
        kopi()
        
    elif p_order == 'e' or p_order == 'E' or p_order == 'E)' or p_order == 'e)' and p_order.isalpha() and len(p_order) > 0:
        pisang_bakar()
        
    elif p_order == 'f' or p_order == 'F' or p_order == 'f)' or p_order == 'F)' and p_order.isalpha() and len(p_order) > 0:
        random_suggestion()
        
    elif p_order != 'a' or p_order != 'b' or p_order != 'c' or p_order != 'd' or p_order != 'e' or p_order != 'f':
        try:
            try:
                if p_order == 1:
                    exit()
                    
                elif int(p_order) > 1 or int(p_order) < 1 or int(p_order) == 0:
                    empty_response()
                    order()
                    
            except p_order !=1:                                                                      # WHY ARE YOU HERE RN???
                empty_response()
                order()
                
        except TypeError:
            empty_response()
            order()
            
    elif p_order != p_order.isalpha():
        empty_response()
        print('')
        order()
        
    elif len(p_order) == 0:
        empty_response()
        print('')
        order()

        
get_name()
