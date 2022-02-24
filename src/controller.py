from mysql.connector import connect
from auth_data import *

def get_all_cities():
    # 1: create connection
    with connect(host=HOSTNAME, user=USER_NAME, password=PASSWORD) as mysql_connection:
        #2: connect cursor object
        with mysql_connection.cursor() as cursor:
            #3: execute query
            query = "SELECT * FROM sakila.city;"
            cursor.execute(query)
            #4: fetch all data returned
            all_cities = cursor.fetchall()
            #print(all_cities)
            city_list = []
            for city in all_cities:
                city_list.append(city[1])
            return city_list
cities = get_all_cities()

#print(cities)

"""
SQL Query:
SELECT 
    f.film_id, f.title, fa.actor_id, a.first_name, a.last_name
FROM
    film f
        INNER JOIN
    film_actor fa ON f.film_id = fa.film_id
        INNER JOIN
    actor a ON fa.actor_id = a.actor_id
where f.title = "FARGO GANDHI"
ORDER BY f.title;
"""

def get_actors_for_movie_by_title(title:str):
    pass

def get_movie_names_by_category():
    pass
