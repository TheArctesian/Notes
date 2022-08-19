import pinyin
#from googletrans import Translator
#translator = Translator()
running = True
while running:
    chars = input("Write you char\n")
    if chars == "exit":
        running = False
    print(pinyin.get(chars))
#    print(translator.translate('你好', src='chinese (traditional)', dest="en"))
