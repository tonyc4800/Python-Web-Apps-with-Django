from googletrans import Translator

def translate(text):
    t = Translator()
    return t.translate(text, dest = 'de').text