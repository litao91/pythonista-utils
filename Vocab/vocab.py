import appex
import youdao
import codecs

def format_text():
    text = appex.get_text()
    if len(text.split(" ")) <= 1:
        definition = youdao.query_words(text)
        if definition:
            print(definition)
            text = text + '\n' + definition
    text = text + '\n ===========\n' 
    return text

def main():
    icloud_path='/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/'
    with codecs.open(icloud_path + 'Vocab/vocab.txt', 'a', 'utf-8') as f:
        f.write(format_text())
        
if __name__ == '__main__':
    main()
