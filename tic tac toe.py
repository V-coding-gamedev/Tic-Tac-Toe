Nordic_countries = {
    "number of countries" : 5,
    "populatioin (2019)" : "27.36 million",
    "capital_city" : "Oslo",
}

for city in Nordic_countries.values():
    if city != "Oslo":
        break
    else:
        print(f"Viet has gone to {city} three times")