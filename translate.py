
import json
 
SINHALA = "si"
ENGLISH = "en"
TAMIL = "ta"
# Opening JSON file
fEn = open('locale/en.json')
fSi = open('locale/si.json')
fTa = open('locale/ta.json')

 
# returns JSON object as
# a dictionary
english = json.load(fEn)
sinhala = json.load(fSi)
tamil = json.load(fTa)
 

 
# Closing file
fEn.close()
fSi.close()
fTa.close()

def translate(locale, title):
    for i in english:
        print(i)
