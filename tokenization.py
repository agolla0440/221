my_sentence = 'Today is sunday, Im going to do some python programming'

the_split_up_words = my_sentence.split()
print(type(the_split_up_words))

print(the_split_up_words)

for word in the_split_up_words:
    print(word)

my_advanced_sentence = "Today is sunday. Today Im going to $ do some python $ programming"

dollar = my_advanced_sentence.split("Today")
print(dollar)