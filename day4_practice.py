def say_hello():
    print("Hello, I am learning functions")
say_hello()
say_hello()
say_hello()

def greet(name):
    print(f"Hello, {name}")

greet("Ada")
greet("Chidi")

def add_vat(price):
    return price * 1.075

new_price = add_vat(1000)
print(new_price)

print(5000 * 10 / 100)
print(5000 - 5000 * 10 /100)

def apply_discount(price,discount_percent):
    return price - price * discount_percent / 100

result = apply_discount(5000,10)
print(result)

print(apply_discount(2000, 20))
print(apply_discount(800, 50))

prices = {"Rice": 500, "Beans": 400, "Garri": 300}

for name in prices:
    print(name,apply_discount(prices[name],10))