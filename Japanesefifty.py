from random import choice
from os import system
import sys  

def loadData():
    fiftyTones = {"あ" : "a","か" : "ka","さ" : "sa","た" : "ta","な" : "na","は" : "ha","ま" : "ma","や" : "ya","ら" : "ra","わ" : "wa",
                  "い" : "i","き" : "ki","し" : "shi","ち" : "chi","に" : "ni","ひ" : "hi","み" : "mi","い" : "i","り" : "ri","い" : "i",
                  "う" : "u","く" : "ku","す" : "su","つ" : "tsu","ぬ" : "nu","ふ" : "hu","む" : "mu","ゆ" : "yu","る" : "ru","う" : "u",
                  "え" : "e","け" : "ke","せ" : "se","て" : "te","ね" : "ne","へ" : "he","め" : "me","え" : "e","れ" : "re","え" : "e",
                  "お" : "o","こ" : "ko","そ" : "so","と" : "to","の" : "no","ほ" : "ho","も" : "mo","よ" : "yo","ろ" : "ro","を" : "(w)o"}
    return fiftyTones

def loadVoicedSoundData():
    voicedSound = {"が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", 
                   "ざ": "za", "じ": "zi", "ず": "zu", "ぜ": "ze", "ぞ": "zo", 
                   "だ": "da", "ぢ": "di", "づ": "du", "で": "de", "ど": "do", 
                   "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",  
                   "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"}
    return voicedSound

def loadLongVoweldata():
    longVowel = {"あ 行": "あ", "い 行": "い", "う 行": "う", "え 行": ("え","い"), "お 行": ("お","う")}
    return longVowel

def randomLoad(data):
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
def showData(selected, data):
    count=0
    print("the whole  tones : ") 
    for key in list(data.keys()):
        print(key,":",data[key],end=", ")
        count=count+1
        if count==10:
            count=0
            print("\n")
    if selected=="1":
        print("\n\nNotes:\n\
          \tthese words pronunciation is special:\n\n\
          'し'读:'xi', 'ち'读:'qi', 'つ'读:'ci', 'ふ'读:'fu', 'r'读:'l'\n\
          \tn 作为辅音")
    if selected=="2":
        print("\n\nNotes:\n\
          \tthese words pronunciation is special:\n\n\
          'じ'读:'ji', 'ぢ'读:'ji', 'ず'读:'zi', 'づ'读:'zi'\n")
    if selected=="3":
        print("\n\nNotes:\n\
          \t例如: あ 行指 か さ た な は ま や ら わ \n\
          \tあ行 + あ 发长音")
    if sys.stdin.isatty():
        input("\npress <enter> to clear these tones")
    system("cls")

def runTrain(selected):
    if selected == '1':
        data = loadData()
    elif selected == "2":
        data = loadVoicedSoundData()
    elif selected == "3":
        data = loadLongVoweldata()
        _data = loadData()
        showData(selected, _data)
        showData(selected, data)
        return True
    else:
        print("no selected")
        return False
    showData(selected, data)
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
                randomdatakey, randomdatavalue = randomLoad(data)
                if trainAndcheck(randomdatakey, randomdatavalue):
                    i=i+1
            print("accuracy: ",i/int(times))
            print("\n\n\n")
        else:
            break


def menu():
    print("====================     MENU    ====================")
    print("\n========== 1. 日语五十音看字识音训练\t==========")
    print("\n========== 2. 日语浊音看字识音训练\t==========")
    print("\n========== 3. 日语延长音组合\t\t==========")
    print("\n========== 0. 退出\t\t\t==========")



if __name__ == "__main__":
    while True:
        menu()
        selected = input("Select your choice... [default is 0]: ")
        if selected == "0" or not selected:
            exit(0)
        if int(selected) <=3 and int(selected) >=1:
            runTrain(selected)
            
        else:
            print("**********Error,input your choice again**************\n\n")
            input("\npress <enter> to continue...")
            system("cls")

