words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

result = {'apple': 3, 'orange': 2, 'banana': 1}

# Refined solution
def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# # My method
# def count_word_frequency(words):
#     output = {}
#     for fruit in words:
#         if fruit not in output.keys():
#             output[fruit] = 1
#         else:
#             output[fruit] += 1
#     return output

output = count_word_frequency(words)

if output == result:
    print("Perfect Algorithm")
else:
    print("Something went wrong")