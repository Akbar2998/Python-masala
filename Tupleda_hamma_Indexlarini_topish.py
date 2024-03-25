sequence = (5,17,16,19,4,25,5,22,4,5,90,5,12,23,33,445,5)
indexes = []
search_index = -1
number = int(input("Qaysi sonni izlaymiz: "))
for i in range(sequence.count(number)):
    current_index = sequence.index(number,search_index + 1)
    indexes.append(current_index)
    search_index = current_index
print(indexes)    

