'''
Date: 22-07-2020

Tools ini hanya untuk orang yang tidak mau susah:v
Semoga Bermanfaat:)
'''

import os

def instal():
    # Install Package
    os.system('pkg install vim')
    os.system('pkg install git')
    os.system('git clone https://github.com/VundleVim/Vundle.vim')

    # Move Folder
    os.system('mkdir ~/.vim')
    os.system('mkdir ~/.vim/bundle')
    os.system('cp -r Vundle.vim ~/.vim/bundle')
    os.system('rm /data/data/com.termux/files/usr/share/vim/vimrc')
    os.system('cp vimrc /data/data/com.termux/files/usr/share/vim/vimrc')

    # Langkah selanjutnya
    print('\n')
    print('     '+'+'*33)
    print("     * Masuklah ke vim Anda lalu masukan perintah ':PluginInstall'")
    print('\n')
    print('     * Jika kurang mengerti silakan hubungi Author')
    print('     * 082250223147 (hanya wa)')

def main():
    os.system('clear')
    print()
    print('     [ Instant Configuration For VIM ]')
    print('     '+'-'*33)
    print('     1. Start The Installation Process')
    sel = input('\n     -> ')
    if sel == '1':
        instal()
    else:
        main()

if __name__ == '__main__':
    main()
