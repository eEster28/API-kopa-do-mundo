from exceptions import *
from datetime import datetime


def data_processing(data: dict):

    title_data = data.get("titles")
    first_cup = data.get("first_cup")

    converting_first_str = datetime.strptime(first_cup, "%Y-%m-%d")
    first_year = converting_first_str.year

    current_data = datetime.now()
    current_year = current_data.year
    cup_numbers = current_year - first_year

    if title_data < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if first_year < 1930:
        raise InvalidYearCupError("there was no world cup this year")
    elif (first_year - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")

    if (cup_numbers // 4) < title_data:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
