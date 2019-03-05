digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']


#lang = zip(digits, en)
#dicta = dict(lang)
#print(dicta)

#lang2 = zip(digits, fr)
#dicta2 = dict(lang2)

#dicta = {zip(digits,en), (digits, fr)}

#print(dicta)




words = {}
for word in range(0,len(digits)):
    num = digits[word]
    words[num] = { 'french': fr[word], 'english': en[word]}


print(words)