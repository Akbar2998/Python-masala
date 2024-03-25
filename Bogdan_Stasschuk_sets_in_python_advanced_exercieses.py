random_things = {12,15,16,17,19,21,99,'heart','a','Akbar', 'Gullola', 'A', 'G'}
second_nabor = {12,12312,13,15,17,16,'b','slice','Gullola', 'love', 'forever'}
random_things.add(1000)
new_nabor = random_things.intersection(second_nabor)
exec = list(new_nabor)
print(*exec)
