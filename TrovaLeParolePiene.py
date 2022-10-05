import sys
import nltk

# prende in input un file dal prompt di comandi
# lo tokenizza e inserisce in una lista le parole POS taggate con le diciture "Sostantivo", "Verbo", "Aggettivo"

def PosTagger (frasi):
   
   tokensPOStot=[]
   for frase in frasi:
      tokens=nltk.word_tokenize(frase)
      tokensPOS=nltk.pos_tag(tokens)
      tokensPOStot+=tokensPOS
   return tokensPOStot

def EstraiParolePiene(TestoAnalizzatoPOS):
   ListaParolePiene=[]
   for bigramma in TestoAnalizzatoPOS:
      if bigramma[1] in ("NN", "NNS", "NNP", "NNPS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "JJ","JJR", "JJS", "MD"):
         ListaParolePiene.append(bigramma[0])
   return ListaParolePiene


def main(file):
   file1=open(file, mode="r", encoding="utf-8")
   raw=file1.read()
   sent_tokenizer=nltk.data.load("tokenizers/punkt/english.pickle")
   frasi = sent_tokenizer.tokenize(raw)
   TestoAnalizzatoPOS=PosTagger(frasi)
   ListaParolePiene = EstraiParolePiene(TestoAnalizzatoPOS)

   for tok in ListaParolePiene:
      
      print(tok)




main (sys.argv[1])
