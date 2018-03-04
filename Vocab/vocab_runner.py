import sys
icloud_path='/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/'
# vocab_path = icloud_path + 'Vocab'
# from os import listdir
# from os.path import isfile, join
# onlyfiles = [f for f in listdir(vocab_path)]
# print(onlyfiles)
sys.path.append(icloud_path + 'Vocab')
# print(sys.path)
import vocab

if __name__ == '__main__':
    vocab.main()
