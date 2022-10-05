import sys
import nltk

#prende in input i due file di parole piene
# crea la lista delle parole che appaiono in entrambi i testi
# di fianco stampa la frequenza dei quella parola in entrambi i testi

def Analisi (frasi):
   tokensTOT=[]
   for frase in frasi:
      tokens=nltk.word_tokenize(frase)
      tokensTOT+=tokens
   return tokensTOT


def VocabolarioComune (tokensTOT1, tokensTOT2):
   ListaComuneToken =[]

   for tok in tokensTOT1:
      ListaComuneToken.append(tok)
   for tok in tokensTOT2:
      ListaComuneToken.append(tok)

   VocabComune=sorted(list(set(ListaComuneToken)))

   return VocabComune
   

def main(listapiene1, listapiene2):
   parole1=open(listapiene1, mode="r", encoding="utf-8")
   parole2=open(listapiene2, mode="r", encoding="utf-8")
   raw1=parole1.read()
   raw2=parole2.read()
   sent_tokenizer=nltk.data.load("tokenizers/punkt/english.pickle")
   frasi1=sent_tokenizer.tokenize(raw1)
   frasi2=sent_tokenizer.tokenize(raw2)

   tokensTotJE=Analisi(frasi1)
   tokensTotTG=Analisi(frasi2)

   vocabolarioComune = VocabolarioComune (tokensTotJE, tokensTotTG)
# per ottenere l'output parola-frequenza primo testo-frequenza secondo testo:
# stampare una colonna alla volta e incollarla in excel

#tok
#tokensTotJE.count(tok)
#tokensTotTG.count(tok)
   for tok in vocabolarioComune:
      print (tok)


main(sys.argv[1], sys.argv[2]) 
