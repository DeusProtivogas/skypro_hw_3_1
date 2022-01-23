import sqlite3
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание

# connection = sqlite3.connect("netflix.db")
# cursor = connection.cursor()
#
# query = """
#     SELECT title, release_year, date_added FROM netflix
#     ORDER BY date_added DESC
# """
#
# cursor.execute(query)
# executed = cursor.fetchall()
# for s in executed:
#     print(s)
# print(executed)

def get_info_by_title(title):
    """
    Поиск фильма по названию
    (В задании сказано "по названию", так что функция, которая принимает id, выглядела неуместно)
    :param title: Название фильма
    :return: Информация о фильме: название, страна производства, когда выпущен в прокат, жанры, описание
    """
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()

    query = f"""
        SELECT title, country, release_year, listed_in, description FROM netflix
        WHERE title LIKE '{title}' 
        ORDER BY release_year DESC
    """
    # print(query)
    cursor.execute(query)
    executed = cursor.fetchall()[0]
    # print(executed)
    return {
        "title": executed[0],
        "country": executed[1],
        "release_year": executed[2],
        "genre": executed[3],
        "description": executed[4]
    }

def get_films_in_interval(start, finish):
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()

    query = f"""
            SELECT title, release_year FROM netflix
            WHERE release_year BETWEEN '{start}' AND '{finish}' 
            ORDER BY release_year DESC
            LIMIT 100
        """
    # print(query)
    cursor.execute(query)
    executed = cursor.fetchall()
    result = []
    for film in executed:
    #     print(film)
        result.append(
            {"title": film[0],
             "release_year": film[1]}
        )
    # print(result)
    return result

# get_info_by_title('7:19')
# get_films_in_interval(2000, 2010)