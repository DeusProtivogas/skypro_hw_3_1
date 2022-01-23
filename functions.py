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

def get_films_by_rating(ratings):

    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()

    query = f"""
                SELECT title, rating, description FROM netflix
                WHERE rating IN ('{ "', '".join(ratings) }')   
            """
    # print(query)
    cursor.execute(query)
    executed = cursor.fetchall()

    result = []
    for film in executed:
        # print(film)
        result.append(
            {
                "title": film[0],
                "rating": film[1],
                "description": film[2]
            }
        )
    return result

def get_films_by_genre(genre):
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()

    query = f"""
                    SELECT title, description, listed_in FROM netflix
                    WHERE listed_in LIKE '%{genre}%'
                    ORDER BY release_year DESC
                    LIMIT 10
                """
    # print(query)
    cursor.execute(query)
    executed = cursor.fetchall()

    result = []
    for film in executed:
        # print(film)
        result.append(
            {
                "title": film[0],
                "description": film[1]
            }
        )
    return result

# get_info_by_title('7:19')
# get_films_in_interval(2000, 2010)
# get_films_by_rating(['PG-13', 'TV-MA', 'G'])
# get_films_by_genre("Documentaries") # Documentaries

def get_list_of_common_actors(actor1, actor2):
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()
    # print([description[0] for description in cursor.description])

    query = f"""
                    SELECT title, `cast` FROM netflix
                    WHERE `cast` LIKE '%{actor1}%' AND `cast` LIKE '%{actor2}%'
                    """
    # print(query)
    cursor.execute(query)
    executed = cursor.fetchall()  # Получаем фильмы, в которых были оба актера

    # Проходимся по всем актерам, если они не совпадают с данными, записываем их в словарь и увеличиваем счетчик
    result = {}
    for film in executed:
        # print(film)
        for actor in film[1].strip().split(', '):
            # print(actor)
            if actor != actor1 and actor != actor2:
                result[actor] = result.get(actor, 0) + 1
    # Выводим актеров, которые были в фильмах с парой больше двух раз
    for actor, counter in result.items():
        if counter > 2:
            print(actor)


# get_list_of_common_actors('Jack Black','Dustin Hoffman')  # Вызов функции для поиска актеров
