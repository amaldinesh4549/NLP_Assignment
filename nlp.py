from collections import Counter 
import string

f = open("text.txt" , "r")
data = f.read()  

trans = str.maketrans('', '', string.punctuation)
data_set=data.translate(trans)

res = len(data_set.split())
print ("\nTHE NO OF WORDS IN THE STRING ARE : " + str(res)) 
 
split_it = data_set.split() 
Counter = Counter(split_it) 

# most_common() produces k frequently encountered 
most_occur = Counter.most_common(10) 
print("")
print ("------------------------------------MOST OCCURING 10 WORDS, THEIR COUNT AND PERCENTAGE---------------------------------")
print("")

for x in most_occur:
  per=(x[1]/res)*100
  print(str(x[0]) + " --> " + str(x[1]) + " --> " + "%.2f" % per + "%")
  print("")
 
s = open("stop.txt" , "r") 
stopword = s.read()
stop_words = stopword.split() 
words = data_set.split() 

final_data=""
for r in words: 
	if not r in stop_words: 
		final_data+=r+" " 
print ("------------------------------------------------TEXT WITHOUT STOPWORDS------------------------------------------------")
print("")
print(final_data)
					 
f.close()
s.close()

