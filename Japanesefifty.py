from random import choice
from os import system
import sys  

def loaddata():
    fiftytones = {"あ" : "a","か" : "ka","さ" : "sa","た" : "ta","な" : "na","は" : "ha","ま" : "ma","や" : "ya","ら" : "ra","わ" : "wa",
                  "い" : "i","き" : "ki","し" : "shi","ち" : "chi","に" : "ni","ひ" : "hi","み" : "mi","い" : "i","り" : "ri","い" : "i",
                  "う" : "u","く" : "ku","す" : "su","つ" : "tsu","ぬ" : "nu","ふ" : "hu","む" : "mu","ゆ" : "yu","る" : "ru","う" : "u",
                  "え" : "e","け" : "ke","せ" : "se","て" : "te","ね" : "ne","へ" : "he","め" : "me","え" : "e","れ" : "re","え" : "e",
                  "お" : "o","こ" : "ko","そ" : "so","と" : "to","の" : "no","ほ" : "ho","も" : "mo","よ" : "yo","ろ" : "ro","を" : "(w)o"}
    return fiftytones

def randomload(data):
    randomdatakey = choice(list(data.keys()))
    randomdatavalue = data[randomdatakey]
    return randomdatakey, randomdatavalue

def trainAndcheck(randomdatakey, randomdatavalue):
    print("\n\n")
    print("this time the word is : ", randomdatakey)
    # print("the word pronunciation is : ", randomdatavalue)
    if sys.stdin.isatty():
        pronunc = input("please input the Roman pronunciation : ")
    else:    
        print("无法在非终端环境中读取输入")
    pronunc = pronunc.lower()
    if pronunc==str(randomdatavalue):
        print("your answer is true")
        return True
    else:
        print("your answer is error")
        print("the word correct pronunciation is : ", randomdatavalue)
        return False
def showdata(data):
    count=0
    print("the whole fifty tones : ") 
    for key in list(data.keys()):
        print(key,":",data[key],end=", ")
        count=count+1
        if count==10:
            count=0
            print("\n")
    print("\n\nNotes:\n\
          \tthese words pronunciation is special:\n\
          'し'读:'xi', 'ち'读:'qi', 'つ'读:'ci', 'ふ'读:'fu', 'r'读:'l'\n\
          \tn 作为辅音")
    if sys.stdin.isatty():
        input("\npress <enter> to clear these tones")
    system("cls")


if __name__ == "__main__":
    data = loaddata()
    showdata(data)
    while True:
        if sys.stdin.isatty():
            next = input("do you want to start the train ?(y/n)[default is y,press <enter>]: ")
        else:    
            print("无法在非终端环境中读取输入")
        
        if next.lower() == "y" or not next:
            if sys.stdin.isatty():
                times = input("input the times that you want to train: ")
            else:    
                print("无法在非终端环境中读取输入")
            i=0
            for _ in range(int(times)):
                randomdatakey, randomdatavalue = randomload(data)
                if trainAndcheck(randomdatakey, randomdatavalue):
                    i=i+1
            print("accuracy: ",i/int(times))
            print("\n\n\n")
        else:
            break
