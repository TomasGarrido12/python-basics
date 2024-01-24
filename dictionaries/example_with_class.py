from typing import List
from typeguard import typechecked
from collections import defaultdict


class DirectorMovie:
    def __init__(self, name: str, year: int, movie: str):
        self.name = name
        self.year = year
        self.movie = movie


# quisiera saber que director(a) ganó mas veces y con cuales peliculas
@typechecked
def most_winner_director(director_movies: List[DirectorMovie]) -> (str, List[str]):
    win_count = defaultdict(int)
    movies_by_director = defaultdict(list)

    # Contar victorias y almacenar películas
    for director_movie in director_movies:
        win_count[director_movie.name] += 1
        movies_by_director[director_movie.name].append(director_movie.movie)

    # Encontrar el director con más victorias
    max_wins = max(win_count.values())
    winner = [director for director, wins in win_count.items() if wins == max_wins]

    # Asegurarse de que solo hay un ganador o manejar múltiples ganadores
    if len(winner) == 1:
        return winner[0], movies_by_director[winner[0]]

    # En caso de empate, devuelve todos los ganadores y sus películas
    return [(w, movies_by_director[w]) for w in winner]


oscar_director_winners = [
    DirectorMovie(
        "Daniel Kwan, Daniel Scheinert", 2023, "Everything everywhere all at once"
    ),
    DirectorMovie("Jane Campion", 2022, "The Power of the Dog"),
    DirectorMovie("Chloé Zhao", 2021, "Nomadland"),
    DirectorMovie("Bong Joon-ho", 2020, "Parasite"),
    DirectorMovie("Alfonso Cuarón", 2019, "Roma"),
    DirectorMovie("Guillermo del Toro", 2018, "The Shape of Water"),
    DirectorMovie("Damien Chazelle", 2017, "La La Land"),
    DirectorMovie("Alejandro González Iñárritu", 2016, "The Revenant"),
    DirectorMovie("Alejandro González Iñárritu", 2015, "Birdman"),
]

print(most_winner_director(oscar_director_winners))
