# -*- coding: utf-8 -*-
"""mad libs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10RkLYTWYpL2m8PhuXhrvMgsDBIZbXlHH
"""



# Hard, but interesting solution using random method.
# it chooses input fields randomly, first offers user to fill word based on its type, then in the end shows the taxt. 


#text processing
text="It was about () () ago when I arrived at the hospital in a (). The hospital is a/an () place, there are a lot of () () here. There are nurses here who have () (). If someone wants to come into my room I told them that they have to () first. I\’ve decorated my room with () (). Today I talked to a doctor and they were wearing a () on their (). I heard that all doctors () () every day for breakfast. The most () thing about being in the hospital is the () () !"
text=text.replace("()","{}")

list1=['Number','Measure_of_time', 'Mode_of_Transportation', 'Adjective', 'Adjective2', 'Noun', 'Color', 'Part_of_the_Body', 'Verb1', 'Number2', 'Noun2', 'Noun3' ,'Part_of_the_Body_2', 'Verb2','Noun4', 'Adjective3', 'Silly_Word', 'Noun5']



#this function takes 3 inputs: a , b, t . a is the list of all individual parts of texts seperated withn {}, as described in previews code. b is the list of input variables. t is the text with missing input fields.
# The steps in code are the following: 
#1) creates list of all individual parts of texts seperated withn {} (list a)
#2) take the random var from list b and get it's index. then take element of list a with the same index and using .format, fill {} with input word.
#3)repeat it until all items are replaced in list a 
#4) join all items in filled list, after all indexes are replaced 
def mad_libs(s, b,t):
  s=[]
  for i in range(len(b)):
    idx=t.find('{}')
    idx=idx+2
    a=t[0:idx+1]
    s.append(a)
    t=t[idx+1::]

  import random
  check=[]
  while len(check)<len(s):
    random_word = random.choice(b)
    idx_new=b.index(random_word)
    if idx_new in check:
      continue
    else:
      print('Please enter a '+random_word)
      item=input()
      a=s[idx_new].format(item)
      s[idx_new]=a
      check.append(idx_new)
  return ''.join(s)

mad_libs(list, list1,text)

