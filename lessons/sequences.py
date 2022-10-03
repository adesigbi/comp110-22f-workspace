"""Notes and examples of tuple and range sequence types."""

#Declairing a type aliast that "invents" the Point2D type 
Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)

print(start_position)


#examples of ranges

a_range: range = range(0, 10, 3)

#aceess items 

print(a_range[2])

print(len(a_range))

for i in a_range: 
    print(i)

#note that the default step is one 
another_range: range = range(0, 10 )

#start marker is defaulted 10 so 
sero_start: range = range(10)

names: list[str] = ["Kris", "Alyssa", "Ben", "arnold"]
print("for in loop every thing")
for name in names:
    print(name)


#ranges are often used when iteration patter is not consecuative and you don't feel like writting the whole while situation
print("for in loop every other")
for i in range(0, len(names), 2):
    print(names[i])

print(range(10))

counts_evens_to_20: range = range(0, 21, 2)

for number in counts_evens_to_20:
    print(number)