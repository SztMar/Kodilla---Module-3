#example1
shopping = {"piekarnia":["chleb","bułki","pączek"],"warzywniak":["marchew","seler","rukola"]}
counter = 0
for shop, product in shopping.items():
    print("Idę do %s i kupuję tam %s." % (shop.upper(),", ".join(product).upper()))
    counter+= len(product)

print("W sumię kupuję %d produktów." % counter)

#example2
div_by_5 = []
div_by_5_squared = []

for num in range(101):
    if num % 5 == 0:
        div_by_5.append(num)
        div_by_5_squared.append(num**3)

print(div_by_5)
print(div_by_5_squared)
print("excellent")
