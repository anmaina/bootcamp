import pandas as pd

class MovieLibrary():
    def __init__(self, db_path:str):
        self._db_path = db_path
        try:
            self._db = pd.read_csv("ukrainian_films.csv")
        except FileNotFoundError:
            self._db = open("ukrainian_films.csv", "x")

    # Add note to .csv file
    def add_row(self, _db, new_row:dict)->dict:
        return _db.append(new_row, ignore_index=True)

    # Remove note from .csv file
    def delete_row(self, _db, column:str, row:str)->dict:
        return _db.loc[_db[column] == row]


    # Print notes to console
    def print_data(self, _db):
        print(_db)

    #Get films with the highest rating
    def get_max_rate(self, _db):
        return _db[_db['rating'] == 5]

    #Get films with the lowest rating
    def get_min_rate(self, _db):
        return _db[_db['rating'] <= 2]

    def get_avrg_rate(self, _db):
    # Get average rating among all films
        return _db["rating"].mean()

add_row("film_name":"Коломия", "note":"1995", "rating":"2")