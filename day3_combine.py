prices = {"Rice": 500, "Beans": 400, "Garri": 300}

for name in prices:
    if prices[name] > 350:
        print(name, "is expensive")
    else:
        print(name, "is affordable")