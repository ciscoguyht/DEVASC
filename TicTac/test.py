import random

tictac = {"Top-L":" ","Top-M":" ","Top-R":" ","Mid-L":" ","Mid-M":" ","Mid-R":" ","Low-L":" ", "Low-M": " ","Low-R":" "}
choosenValue = random.choice(tictac.keys())

for key , value  in tictac.items():
    if key == choosenValue:
        tictac[key] = "X"


