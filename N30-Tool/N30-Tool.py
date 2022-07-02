from re import S, X
import sys
import os
import time
from turtle import Pen
from colorama import init
from termcolor import colored

os.system("mode con cols=77 lines=45")

def tulisan():
    import sys
    import os
    import time
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    

    cprint(figlet_format('N-30 TOOLS', font='starwars'),
           'blue', attrs=['bold'])
def bar():
    import sys
    import os
    import time
    print("Loading: ")
    toolbar_width = 37

    # setup toolbar
    
    sys.stdout.write("|%s|" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.1) # do real work here
        # update the bar
        sys.stdout.write("█")
        sys.stdout.flush()

    sys.stdout.write("|\n") # this ends the progress bar
#DONE   
    os.system('cls')
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format

    cprint(figlet_format('     DONE!', font='starwars'),
           'white', attrs=['bold'])

#=== WELCOME PAGE ===
def selamat():
    import sys
    import os
    import time
    os.system('cls')
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format

    cprint(figlet_format('WELCOME', font='starwars'),
           'white', attrs=['bold'])

def batas():
    print("=============================================================================")

def home():
    selamat()
    batas()

#=== HELP ===
def Help(): 
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    os.system('cls')

    cprint(figlet_format('       HELP', font='starwars'),
        'white', attrs=['bold'])
    batas()
    hlp = ["Perhatikan Angka Yang dimasukan", "Perhatikan Ketikan anda", "Tekan ENTER jika sudah"]
    for lis_hlp in hlp:
        print('%30s' % "● " + lis_hlp)
    batas()
    print(colored('%45s' % "BY @AUTOFAT ", attrs=['bold']))
    batas()
    backh = input('%52s' % "Tekan ENTER Untuk Kembali")
    if backh == "a":
        selamat()
    else:
        selamat()
        homep()

#=== TOOLS LANDING PAGE ===
def tools():
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    os.system('cls')

    cprint(figlet_format('   TOOLS', font='starwars'),
        'magenta', attrs=['bold'])
    batas()
    hlp = ["HITUNG CEPAT      [1]", "LUAS BANGUN DATAR [2]", "HOME              [H]", "EXIT              [X]"]
    for lis_hlp in hlp:
        print('%30s' % "● " + lis_hlp)
    batas()
    hap = input('%48s' %"Masukan Perintah: ")
    if hap == "h":
        selamat()
        homep()
    elif hap == "H":
        selamat()
        homep()
    elif hap == "x":
        exit
    elif hap == "X":
        exit
    elif hap == "1":
        hc()
    
    else:
        selamat()
        homep()
    
def kredit(): 
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    os.system('cls')

    cprint(figlet_format(' CREDITS', font='starwars'),
    'white', attrs=['bold'])
    batas()
    txt = "Applikasi ini dibuat sebagai projek belajar bahasa Python", "semoga aplikasi ini dapat digunakan sebaik dan sebijak mungkin."
    for lis_txt in txt:
        print('%5s' % "" + lis_txt)
    batas()
    print('%20' %"By: @Autofat")
    

    input("Tekan ENTER, untuk kembali") 


    
#=== LANDING PAGE ===
def homep():
    mob = ["Help    [1]","Tools   [2]","Credits [3]", "Exit    [4]"]
    print('%50s' % "Perintah Yang Tersedia: ")
    batas()
    for lis_mob in mob:
        print('%35s' % "● " + lis_mob)

    print(colored('%68s' %  'Pilih Perintah Dengan Menuliskan Angka Didalam [] ', 'red'))
    batas()
    cmd = input('%50s' % "Masukan Perintah: ")
    batas()
    if cmd == "1":
        Help()

    elif cmd == "2":
        tools()
    elif cmd == "3":
        kredit()

    elif cmd == "4":
        exit
       
    else:
        os.system('cls')
        selamat()
        homep()

#=== HOME PAGE ===
def hc():
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    os.system('cls')

    cprint(figlet_format('   TOOLS', font='starwars'),
    'magenta', attrs=['bold'])
    batas()


    info = ["PENJUMLAHAN  [1]", "PENGURANGAN  [2]", "PERKALIAN    [3]", "PEMBAGIAN    [4]", "KEMBALI      [H]", "EXIT         [X]"]
    print('%48s' % "Perintah Yang Tersedia: ")
    batas()
    for lis_info in info:
        print('%30s' % "● " + lis_info)
    batas()
    print(colored('%68s' %  'Pilih Perintah Dengan Menuliskan Angka Didalam [] ', 'red'))
    batas()
    cmd = input('%50s' % "Masukan Perintah: ")
    batas()

    if cmd == "1":
        Penjumlahan()
    elif cmd == "2":
        Pengurangan()
    elif cmd == "3":
        Perkalian()
    elif cmd == "4":
        Pembagian()
    elif cmd == "H":
        tools()
    elif cmd == "h":
        tools()
    elif cmd == "X":
        exit
    elif cmd == "x":    
        exit

#=== PENJUMLAHAN ===
def Penjumlahan():
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    os.system('cls')

    cprint(figlet_format('   TOOLS', font='starwars'),
    'magenta', attrs=['bold'])
    batas()

    angka1 = input("Masukan Angka Pertama: ")
    angka2 = input ("Masukan Angka Kedua: ")
    os.system('cls')
    cprint(figlet_format('   TOOLS', font='starwars'),
    'magenta', attrs=['bold'])
    batas()  
    print ('Hasil: ', int(angka1) + int(angka2))
    batas()
    abc = input('%55s' % "KEMBALI [1], ULANGI [2], HOMEPAGE [3]")
    if abc == "1":
        hc()
    elif abc == "2":
        Penjumlahan()
    elif abc == "3":
        homep()

#=== PENGURANGAN ===
def Pengurangan():
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    os.system('cls')

    cprint(figlet_format('   TOOLS', font='starwars'),
    'magenta', attrs=['bold'])
    batas()

    angka1 = input("Masukan Angka Pertama: ")
    angka2 = input ("Masukan Angka Kedua: ")
    os.system('cls')
    cprint(figlet_format('   TOOLS', font='starwars'),
    'magenta', attrs=['bold'])
    batas()  
    print ('Hasil: ', int(angka1) - int(angka2))
    batas()
    abc = input('%55s' % "KEMBALI [1], ULANGI [2], HOMEPAGE [3]")
    if abc == "1":
        hc()
    elif abc == "2":
        Pengurangan()
    elif abc == "3":
        homep()
    
#=== PERKALIAN ===
def Perkalian():
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    os.system('cls')

    cprint(figlet_format('   TOOLS', font='starwars'),
    'magenta', attrs=['bold'])
    batas()

    angka1 = input("Masukan Angka Pertama: ")
    angka2 = input ("Masukan Angka Kedua: ")
    os.system('cls')
    cprint(figlet_format('   TOOLS', font='starwars'),
    'magenta', attrs=['bold'])
    batas()  
    print ('Hasil: ', int(angka1) * int(angka2))
    batas()
    abc = input('%55s' % "KEMBALI [1], ULANGI [2], HOMEPAGE [3]")
    if abc == "1":
        hc()
    elif abc == "2":
        Perkalian()
    elif abc == "3":
        homep()
    
#=== PEMBAIAN ===
def Pembagian():
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    os.system('cls')

    cprint(figlet_format('   TOOLS', font='starwars'),
    'magenta', attrs=['bold'])
    batas()

    angka1 = input("Masukan Angka Pertama: ")
    angka2 = input ("Masukan Angka Kedua: ")
    os.system('cls')
    cprint(figlet_format('   TOOLS', font='starwars'),
    'magenta', attrs=['bold'])
    batas()  
    print ('Hasil: ', int(angka1) / int(angka2))
    batas()
    abc = input('%55s' % "KEMBALI [1], ULANGI [2], HOMEPAGE [3]")
    if abc == "1":
        hc()
    elif abc == "2":
        Pembagian()
    elif abc == "3":
        homep()    
    

#===============================================================================================

tulisan()#n30
bar()#loading
batas()
welcome = input('%45s' % "PRESS ANY KEY", )

#============================================ HOMEPAGE =========================================

welcome = str(welcome)
if welcome == "A":
    selamat()
    homep()
else :
    selamat()
    homep()


