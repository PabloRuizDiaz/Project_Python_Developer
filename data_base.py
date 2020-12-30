'''
BASE DE DATOS DE COVID-19
------------------------------------------------------------------------------------------
En este script se definen los comandos basicos para crear y cargar la informacion
extraida del json de la URL https://opendata.ecdc.europa.eu/covid19/casedistribution/json
donde sera guardada en una base de datos SQL. La misma estara utilizando las bases de 
SQLite.

Contiene dos funciones principales:
    create_table() -> se crea la base de datos con su correspondiente tabla "table_covid_world";
    actualise_table() -> se carga los datos extraidos del json a la tabla "table_covid_world".

Sus Campos SQL son:
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [date_rep] TEXT,
    [year_week] TEXT,
    [cases_weekly] INTEGER,
    [deaths_weekly] INTEGER,
    [countries_and_territories] TEXT,
    [geo_id] TEXT,
    [country_territory_Code] TEXT,
    [pop_data_2019] INTEGER,
    [continent_exp] TEXT,
    [Cumulative_number_for_14_days_of_COVID_19_cases_per_100000] TEXT.
'''

import requests
import json
import sqlite3

API_REQUEST = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json'


def create_table_SQL():
    '''
    Crea la base de datos con su correspondiente tabla "table_covid_world";
    '''

    conn = sqlite3.connect('db_covid_world.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()

    c.execute("""
            DROP TABLE IF EXISTS table_covid_world;
            """)
    
    c.execute("""
            CREATE TABLE IF NOT EXISTS table_covid_world(
            [id] INTEGER PRIMARY KEY AUTOINCREMENT,
            [date_rep] TEXT,
            [year_week] TEXT,
            [cases_weekly] INTEGER,
            [deaths_weekly] INTEGER,
            [countries_and_territories] TEXT,
            [geo_id] TEXT,
            [country_territory_Code] TEXT,
            [pop_data_2019] INTEGER,
            [continent_exp] TEXT,
            [Cumulative_number_for_14_days_of_COVID_19_cases_per_100000] TEXT
            );
            """)
    
    conn.commit()
    conn.close()


def actualise_table_SQL():
    '''
    Se carga los datos extraidos del json a la tabla "table_covid_world"
    '''
    group = list()

    conn = sqlite3.connect('db_covid_world.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()

    response = requests.get(API_REQUEST, timeout=60)
    json_data = response.json()

    data = json_data.get('records')

    for i in data:
        for j in i:
            group.append(i[j])    
        
        c.execute("""
                INSERT INTO table_covid_world 
                (date_rep, year_week, cases_weekly, deaths_weekly, countries_and_territories,
                geo_id, country_territory_Code, pop_data_2019, continent_exp, 
                Cumulative_number_for_14_days_of_COVID_19_cases_per_100000)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                """, group)
        
        group = []
    
    conn.commit()
    conn.close()
