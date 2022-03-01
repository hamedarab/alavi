import time

print("________________________Begin of List________________________")
time.sleep(0.5)
colors1 = ["red", "orange", "purple", "pink", "red"]
colors2 = ["green", "yellow", "black"]

print(colors1)
print(colors2)
time.sleep(0.5)
colors1.append("white")
print(colors1)
time.sleep(0.5)
print(colors1.count("red"))
time.sleep(0.5)
colors3 = colors1.copy()
print(colors3)
time.sleep(0.5)
colors1.extend(colors2)
print(colors1)
time.sleep(0.5)
print(colors1.index("purple"))
time.sleep(0.5)
colors1.insert(0, "blue")
print(colors1)
time.sleep(0.5)
colors1.pop(1)
print(colors1)
time.sleep(0.5)
colors1.remove("pink")
print(colors1)
time.sleep(0.5)
colors1.sort()
print(colors1)
time.sleep(0.5)
colors1.reverse()
print(colors1)
time.sleep(0.5)
colors2.clear()
time.sleep(0.5)
print(colors2)
time.sleep(0.5)
print("________________________End of List________________________")

time.sleep(0.5)

print("________________________Begin of Tuple________________________")
time.sleep(0.5)
colors4 = ("white", "orange", "purple", "white", "red")
print(colors4)
time.sleep(0.5)


print(colors4.count("white"))
time.sleep(0.5)
print(colors4.index("red"))
time.sleep(0.5)
print("________________________End of Tuple________________________")

time.sleep(0.5)

print("________________________Begin of Set________________________")
time.sleep(0.5)
colors5 = {"green", "yellow", "black", "red", "blue"}
print(colors5)
time.sleep(0.5)
colors6 = colors5.copy()
print(colors6)
time.sleep(0.5)
colors5.add("white")
print(colors5)
time.sleep(0.5)
print(colors5.difference(colors6))
time.sleep(0.5)
colors5.difference_update(colors6)
print(colors5)
time.sleep(0.5)
colors6.discard(0)
print(colors6)
time.sleep(0.5)
colors6.pop()
print(colors6)
time.sleep(0.5)
colors6.remove("red")
print(colors6)
time.sleep(0.5)
colors6.union(colors5)
time.sleep(0.5)
colors6.clear()
print(colors6)
time.sleep(0.5)

print("________________________End of Set________________________")

time.sleep(0.5)

print("________________________Begin of Dictionary________________________")
time.sleep(0.5)
me1 = {

    "name" : "Mohammad Hossein",
    "family_name" : "Arab",
    "phone_nmber" : "09001234567",
    "year" : 1385,
    "month" : "Esfand",
    "day" : 14,

}

print(me1)
time.sleep(0.5)
me2 = me1.copy()
print(me2)
time.sleep(0.5)
print(me1.get("name"))
time.sleep(0.5)
me1.pop("year")
print(me1)
time.sleep(0.5)
me1.update({"color" : "green"})
print(me1)
time.sleep(0.5)
me3 = me1.values()
print(me3)
