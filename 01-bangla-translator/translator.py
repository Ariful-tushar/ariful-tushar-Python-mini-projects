from translate import Translator
translator= Translator(to_lang="bn")

try:
    with open ("./english.txt") as my_file:
        text = my_file.read();
        translation = translator.translate(text)
        print (translation)
        with open ("./bangla.txt", mode = "w", encoding="utf-8") as my_file2:
            my_file2.write(translation)
except:
    print ("Something is wrong!")