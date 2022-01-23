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

    cursor.execute(query)
    executed = cursor.fetchall()[0]
          
    return {
        "title": executed[0],
        "country": executed[1],
        "release_year": executed[2],
        "genre": executed[3],
        "description": executed[4]
    }


def get_films_in_interval(start, finish):
    """
    Возврат списка фильмов, вышедших между двумя годами
    :param start: Год выхода ОТ
    :param finish: Год выхода ДО
    :return: Список словарей с информацией о фильмах
    """
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()

    query = f"""
            SELECT title, release_year FROM netflix
            WHERE release_year BETWEEN '{start}' AND '{finish}' 
            ORDER BY release_year DESC
            LIMIT 100
        """

    cursor.execute(query)
    executed = cursor.fetchall()
    result = []
    for film in executed:
        result.append(
            {"title": film[0],
             "release_year": film[1]}
        )
    return result


def get_films_by_rating(ratings):
    """
    Возврат фильмов по списку рейтингов
    :param ratings: Список рейтингов
    :return: Список словарей с информацией о фильмах
    """
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()

    query = f"""
                SELECT title, rating, description FROM netflix
                WHERE rating IN ('{"', '".join(ratings)}')   
            """

    cursor.execute(query)
    executed = cursor.fetchall()

    result = []
    for film in executed:
            
        result.append(
            {
                "title": film[0],
                "rating": film[1],
                "description": film[2]
            }
        )
    return result


def get_films_by_genre(genre):
    """
    Возврат фильмов с определенным жанром
    :param genre: Жанр картины
    :return: Список словарей с информацией о фильмах
    """
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()

    query = f"""
                    SELECT title, description, listed_in FROM netflix
                    WHERE listed_in LIKE '%{genre}%'
                    ORDER BY release_year DESC
                    LIMIT 10
                """

    cursor.execute(query)
    executed = cursor.fetchall()

    result = []
    for film in executed:
            
        result.append(
            {
                "title": film[0],
                "description": film[1]
            }
        )
    return result


# Тестирование функций выше
# get_info_by_title('7:19')
# get_films_in_interval(2000, 2010)
# get_films_by_rating(['PG-13', 'TV-MA', 'G'])
# get_films_by_genre("Documentaries") # Documentaries

def get_list_of_common_actors(actor1, actor2):
    """
    Поиск актеров, снимавшихся в фильмах с двумя другими более 2 раз
    :param actor1: Актер 1
    :param actor2: Актер 2
    :return: Список актеров
    """
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()

    query = f"""
                    SELECT title, `cast` FROM netflix
                    WHERE `cast` LIKE '%{actor1}%' AND `cast` LIKE '%{actor2}%'
                    """

    cursor.execute(query)
    executed = cursor.fetchall()  # Получаем фильмы, в которых были оба актера

    # Проходимся по всем актерам, если они не совпадают с данными, записываем их в словарь и увеличиваем счетчик
    result = {}
    for film in executed:
            
        for actor in film[1].strip().split(', '):
                 
            if actor != actor1 and actor != actor2:
                result[actor] = result.get(actor, 0) + 1
    # Выводим актеров, которые были в фильмах с парой больше двух раз
    for actor, counter in result.items():
        if counter > 2:
            print(actor)


# get_list_of_common_actors('Jack Black','Dustin Hoffman')  # Вызов функции для поиска актеров


def search_by_type_year_genre(type, year, genre):
    """
    Возврат картин, подходящих под параметры
    :param type: Тип картины
    :param year: Год выпуска
    :param genre: Жанр картины
    :return: Список подходящих картин в JSON формате
    """
    connection = sqlite3.connect("netflix.db")
    cursor = connection.cursor()

    query = f"""
                SELECT title, description FROM netflix
                WHERE type = '{type}' AND release_year = {year} AND listed_in LIKE '%{genre}%'
    """

    cursor.execute(query)
    executed = cursor.fetchall()  # Получаем фильмы, в которых были оба актера

    result = []
    # Проходимся по всем актерам, если они не совпадают с данными, записываем их в словарь и увеличиваем счетчик
    for film in executed:
        result.append(
            {
                "title": film[0],
                "description": film[1]
            }
        )
    return result

# print(search_by_type_year_genre('TV Show', 2020, 'TV Comedies'))
