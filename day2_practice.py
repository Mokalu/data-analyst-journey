products = ["Rice", "Beans", "Garri"]
print(products)
print(products[0])
print(products[1])
print(products[2])
print(products[-1])
products.append("Yam")
print(products)
print(products[-1])
print(len(products))
#There was an error because the list index number doesn't correspond with the above.
#print(products[10])
prices = {"Rice": 500, "Beans": 400, "Garri": 300}
print(prices["Beans"])
print(prices["Rice"])
print(prices["Garri"])
prices["Yam"] =700
prices["Rice"] =600
print(prices)
total = 3 * prices["Rice"] + 2 * prices["Beans"]
print(total)