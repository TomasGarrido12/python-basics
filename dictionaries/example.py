oscar_director_winners = [
    {
        "name": "Daniel Kwan, Daniel Scheinert",
        "year": 2023,
        "movie": "Everything everywhere all at once",
    },
    {"name": "Jane Campion", "year": 2022, "movie": "The Power of the Dog"},
    {"name": "Chloé Zhao", "year": 2021, "movie": "Nomadland"},
    {"name": "Bong Joon-ho", "year": 2020, "movie": "Parasite"},
    {"name": "Alfonso Cuarón", "year": 2019, "movie": "Roma"},
    {"name": "Guillermo del Toro", "year": 2018, "movie": "The Shape of Water"},
    {"name": "Damien Chazelle", "year": 2017, "movie": "La La Land"},
    {"name": "Alejandro González Iñárritu", "year": 2016, "movie": "The Revenant"},
    {"name": "Alejandro González Iñárritu", "year": 2015, "movie": "Birdman"},
]


# quisiera saber que director(a) ganó mas veces y con cuales peliculas
# output: { "name": "Alejandro González Iñárritu", "movies": ["The Revenant", "Birdman"] }
def most_winner_director(director_movies):
    grouped = {}
    max_count = 0
    dir_name_max = ""

    for director in director_movies:
        if director["name"] in grouped:
            grouped[director["name"]]["count"] += 1
            grouped[director["name"]]["movies"].append(director["movie"])
        else:
            grouped[director["name"]] = {"count": 1, "movies": [director["movie"]]}

    for [name, group] in grouped.items():
        if group["count"] > max_count:
            max_count = group["count"]
            dir_name_max = name

    return {"name": dir_name_max, "movies": grouped[dir_name_max]["movies"]}


print(most_winner_director(oscar_director_winners))
