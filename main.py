import os
import time
import module.loading as ld
import module.scene_manager as sm
import data_manager as dm
from module.text_type import textType as tt

cur_path = os.path.dirname(__file__)

def SplashLoad():
    os.system('clear')
    print('   __                  _     _         __ _                   ')
    print('   \ \  ___  _ __ ___ | |__ | | ___   / _\ |_ ___  _ __ _   _ ')
    print('    \ \/ _ \|  _ ` _ \|  _ \| |/ _ \  \ \| __/ _ \|  __| | | |')
    print(' /\_/ / (_) | | | | | | |_) | | (_) | _\ \ || (_) | |  | |_| |')
    print(' \___/ \___/|_| |_| |_|_.__/|_|\___/  \__/\__\___/|_|   \__, |')
    print('                                                        |___/ ')
    print('\n                           Main Menu\n')
    print('                      1. Mulai Story Baru')
    print('                      2. Lanjutkan Story')
    print('                      3. Keluar\n')
    menu = input('                               ')
    if menu == '1' or menu == 'baru':
        sm.firstScene()
    elif menu == '2' or menu == 'lanjut':
        dm.loadSavedProgress();
    elif menu == '3' or menu == 'keluar':
        exit(0)
    else:
        print('                          Menu salah...')
        input('                  Tekan enter untuk melanjutkan...')
        SplashLoad()


if __name__ == '__main__':
    SplashLoad()
