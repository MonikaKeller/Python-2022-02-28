# DRY
input_value = input("Ird be a szuletesi eved!")
year = int(input_value)
if year > 2022:
    print("Hazudsz!")
elif year >= 2020:
    print("Ezen évtized")
else:
    print("Nem ezen évtizedben")