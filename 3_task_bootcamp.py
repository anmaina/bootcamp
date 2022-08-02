import pandas as pd
import os

class MovieLibrary():
    def __init__(self, db_path:str):
        self._db_path = db_path
        try:
            self._db = pd.read_csv("ukrainian_films.csv")
        except FileNotFoundError:
            self._db = pd.DataFrame(columns=["film_name","note","rating"])

    def save_to_csv(self, _db):
        _db = _db.to_csv("ukrainian_films.csv", index=False)

    # Add note to .csv file
    def add_row(self, _db, new_row:dict)->dict:
        _db = _db.append(new_row, ignore_index=True)
        return self.save_to_csv(_db)

    # Remove note from .csv file
    def delete_row(self, _db, column:str, row:str)->dict:
        return _db.loc[_db[column] == row]


    # Print notes to console
    def print_data(self, _db):
        print(_db)

    #Get films with the highest rating
    def get_max_rate(self, _db):
        max_rate = _db['rating'].max()
        return _db[_db['rating'] == max_rate]

    #Get films with the lowest rating
    def get_min_rate(self, _db):
        min_rate = _db['rating'].min()
        return _db[_db['rating'] == min_rate]

    def get_avrg_rate(self, _db):
    # Get average rating among all films
        return _db["rating"].mean()

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    full_path = os.path.join(path, 'ukrainian_films')
    movielibrary = MovieLibrary(db_path=full_path)

    movielibrary.add_row(MovieLibrary, 
    _db="ukrainian_films.csv", 
    new_row={"film_name":"Коломия","note":"1995","rating":"2"})
    for film_name, note, rating in movielibrary:
        print(film_name, note, rating)