no = []

while True:
    p = input("Enter a numerical value or hit Enter to finish ")
    if p == "":
        break
    no.append(int(p))

no.sort(reverse=True)

print("The top five numbers in descending sequence are the largest.")
for number in no [:5]:
 print(number)
