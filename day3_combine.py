prices = {"Rice": 500, "Beans": 600, "Garri": 300}

for name in prices:
    if prices[name] > 450:
        print(name, "is expensive")
    else:
        print(name, "is affordable")