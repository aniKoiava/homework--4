

def faces():
    sentence = input("How are you feeling? ")
    sentence = convert(sentence)
    print(sentence)
    
def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

faces()



