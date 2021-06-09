tekst=""
import requests
import bs4
URL = 'https://www.edmprod.com/5-stages-electronic-music-producer/'
strona = requests.get(URL)
zawartosc = bs4.BeautifulSoup(strona.content, 'html.parser')
txt = zawartosc.find_all('p')
for t in txt:
   tekst+=str(t.contents[:1])
   tekst+=' '
import nltk
tokeny=nltk.word_tokenize(tekst)
tagi=nltk.pos_tag(tokeny)
print(tagi)
rzeczowniki=[]
for para in tagi:
    if para[1]=='NN':
        rzeczowniki.append(para[0])
for r in rzeczowniki:
    if len(r)<2:#usuwam pojedyncze litery które program wcześniej potraktował jako rzeczowniki
        rzeczowniki.remove(r)
from nltk.corpus import stopwords
stop_lista=set(stopwords.words("english"))
rzeczowniki_bez_stopwords=[]
lista=['href=','https','//app.monstercampaigns.com/c/joxgwrgz1uzfqjhrnkfe/','rel=','font-weight','<','>',']','[','noopener',
'noreferrer','target=','_blank','font-size:1.3rem','align']


for r in rzeczowniki:
    if r not in stop_lista and r not in lista:
        rzeczowniki_bez_stopwords.append(r)

rzeczowniki=rzeczowniki_bez_stopwords

bez_interpunkcji = [word for word in rzeczowniki if word.isalnum()]
rzeczowniki=bez_interpunkcji

rz=""

for rzeczownik in rzeczowniki:
    rz+=rzeczownik+' '
    print(rzeczownik)

import numpy as np
from PIL import Image
mask = np.array(Image.open('D:/NOTATKI UE 5 SEMESTR/PRZETWARZANIE DANYCH W PYTHON/projekt pliki/3/note.jpg'))

from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc = WordCloud(width = 3000, height = 2000, mask=mask, background_color='white', colormap='inferno')
chmura=wc.generate(rz)
plt.figure()
plt.imshow(chmura)
plt.axis("off")
plt.show()
chmura.to_file('D:/NOTATKI UE 5 SEMESTR/PRZETWARZANIE DANYCH W PYTHON/projekt pliki/3/result.jpg')