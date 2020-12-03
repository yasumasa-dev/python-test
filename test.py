# -*- coding: utf-8 -*- Pythonを日本語に対応

# print("Hello World")

# print("Hello")
# print("World")

# print(1+1)
# print(1-1)
# print(2*2)
# print(10/2)
# print(5%2)

# unko = 'こんにちは'

# print(unko)

###with
# open()
# with open('./unko.txt','r') as file:
#   print(file.read())

###class
# class Card:
#   def __init__(self, date, user_name):
#     self.date = date
#     self.user_name = user_name
#   def message(self):
#     return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'

# date_a = '2020-01-01'
# user_name_a = 'Taro'
# card_a = Card(date_a, user_name_a)

# date_b = '2020-01-03'
# user_name_b = 'Kayoko'
# card_b = Card(date_b, user_name_b)

# print(card_b.message()) 

###import
import math
print(math.pi)

#外部モジュール
#Numpy

import numpy

numpy_list = [3,1,5,10,2093,304,123]
print(numpy.sum(numpy_list))



