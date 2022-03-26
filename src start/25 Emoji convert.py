massage=input(">")
#whaer you have space it will use it as boundary  to spreated it
words= massage.split(' ')
print(words)

emojis={
    "(:":"😊",
    ":(":"☹"
}
output=""
for word in words:
  output+=  emojis.get(word,word) +" "
print(output)




