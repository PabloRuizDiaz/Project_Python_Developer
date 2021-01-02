'''
Diseño de graficos
----------------------------------------------------------
En este script se realizan los diversos graficos de barra o lineales
que son implementados para el website.
Funciones:
 1. bar_graph_continent()
 2. bar_graph_continent_death()
 3. ranking_table_graph()
 4. ranking_table_graph_death()
 5. line_graph()
 6. line_graph_death()
 7. line_graph_per_country(country)
'''

import requests
import json
import sqlite3
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors
from itertools import accumulate


def bar_graph_continent():
    '''
    Grafico de barra que muestra el avance de casos de contagio total en el mundo por contiente.
    '''
    conn = sqlite3.connect('db_covid_world.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()
    
    c.execute("""
            SELECT 
            SUM(cases_weekly), continent_exp
            FROM table_covid_world
            GROUP BY continent_exp;
            """)
    
    row = c.fetchall()

    conn.commit()
    conn.close()

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.bar(row[0][1], row[0][0], label=f'{row[0][1]}')
    ax.bar(row[1][1], row[1][0], label=f'{row[1][1]}')
    ax.bar(row[2][1], row[2][0], label=f'{row[2][1]}')
    ax.bar(row[3][1], row[3][0], label=f'{row[3][1]}')
    ax.bar(row[4][1], row[4][0], label=f'{row[4][1]}')
    
    ax.set_facecolor('whitesmoke')
    ax.legend()

    plt.show()

    return


def bar_graph_continent_death():
    '''
    Grafico de barra que muestra el avance de casos de muertes total en el mundo por contiente.
    '''
    conn = sqlite3.connect('db_covid_world.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()
    
    c.execute("""
            SELECT 
            SUM(deaths_weekly), continent_exp
            FROM table_covid_world
            GROUP BY continent_exp;
            """)
    
    row = c.fetchall()

    conn.commit()
    conn.close()

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.bar(row[0][1], row[0][0], label=f'{row[0][1]}')
    ax.bar(row[1][1], row[1][0], label=f'{row[1][1]}')
    ax.bar(row[2][1], row[2][0], label=f'{row[2][1]}')
    ax.bar(row[3][1], row[3][0], label=f'{row[3][1]}')
    ax.bar(row[4][1], row[4][0], label=f'{row[4][1]}')
    
    ax.set_facecolor('whitesmoke')
    ax.legend()

    plt.show()

    return


def ranking_table_graph():
    '''
    Tabla donde muestra el top 10 de los paises en el mundo que la peor situacion de contagios por pais.
    '''
    conn = sqlite3.connect('db_covid_world.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()
    
    c.execute("""
            SELECT 
            SUM(cases_weekly), countries_and_territories, 
            (SUM(cases_weekly)* 100 / (Select SUM(cases_weekly) From table_covid_world))
            FROM table_covid_world
            GROUP BY countries_and_territories
            ORDER BY SUM(cases_weekly) DESC
            LIMIT 10;
            """)
    
    row = c.fetchall()

    conn.commit()
    conn.close()

    return row


def ranking_table_graph_death():
    '''
    Tabla donde muestra el top 10 de los paises en el mundo con la peor situacion de muertes por pais.
    '''
    conn = sqlite3.connect('db_covid_world.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()
    
    c.execute("""
            SELECT 
            SUM(deaths_weekly), countries_and_territories, 
            (SUM(deaths_weekly)* 100 / (Select SUM(deaths_weekly) From table_covid_world))
            FROM table_covid_world
            GROUP BY countries_and_territories
            ORDER BY SUM(deaths_weekly) DESC
            LIMIT 10;
            """)
    
    row = c.fetchall()

    conn.commit()
    conn.close()

    return row


def line_graph():
    '''
    Grafico de linea temporal (semanal) que muestra el avance de casos de contagio total en el mundo por contienente.
    '''
    conn = sqlite3.connect('db_covid_world.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()
    
    c.execute("""
            SELECT 
            year_week,
            SUM(cases_weekly),
            continent_exp
            FROM table_covid_world
            GROUP BY year_week, continent_exp
            ORDER BY year_week;
            """)

    row = c.fetchall()

    conn.commit()
    conn.close()

    africa_acc = list(accumulate([i[1] for i in row if i[2] == 'Africa']))
    america_acc = list(accumulate([i[1] for i in row if i[2] == 'America']))
    asia_acc = list(accumulate([i[1] for i in row if i[2] == 'Asia']))
    europe_acc = list(accumulate([i[1] for i in row if i[2] == 'Europe']))
    oceania_acc = list(accumulate([i[1] for i in row if i[2] == 'Oceania']))

    week_year = [i[0] for i in row if i[2] == 'Africa']

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(week_year, africa_acc, color='b', label='Africa')
    ax.plot(week_year, america_acc, color='c', label='America')
    ax.plot(week_year, asia_acc, color='g', label='Asia')
    ax.plot(week_year, europe_acc, color='k', label='Europe')
    ax.plot(week_year, oceania_acc, color='r', label='Oceania')
    ax.set_facecolor('whitesmoke')
    ax.set_ylabel("Cases of Covid-19")
    ax.set_xlabel("Number of week")
    plt.xticks(week_year, rotation ='vertical')

    ax.legend()
    plt.show()

    return


def line_graph_death():
    '''
    Grafico de linea temporal (semanal) que muestra el avance de casos de muertes total en el mundo.
    '''
    conn = sqlite3.connect('db_covid_world.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()
    
    c.execute("""
            SELECT 
            year_week,
            SUM(deaths_weekly),
            continent_exp
            FROM table_covid_world
            GROUP BY year_week, continent_exp
            ORDER BY year_week;
            """)

    row = c.fetchall()

    conn.commit()
    conn.close()

    africa_acc = list(accumulate([i[1] for i in row if i[2] == 'Africa']))
    america_acc = list(accumulate([i[1] for i in row if i[2] == 'America']))
    asia_acc = list(accumulate([i[1] for i in row if i[2] == 'Asia']))
    europe_acc = list(accumulate([i[1] for i in row if i[2] == 'Europe']))
    oceania_acc = list(accumulate([i[1] for i in row if i[2] == 'Oceania']))

    week_year = [i[0] for i in row if i[2] == 'Africa']

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(week_year, africa_acc, color='b', label='Africa')
    ax.plot(week_year, america_acc, color='c', label='America')
    ax.plot(week_year, asia_acc, color='g', label='Asia')
    ax.plot(week_year, europe_acc, color='k', label='Europe')
    ax.plot(week_year, oceania_acc, color='r', label='Oceania')
    ax.set_facecolor('whitesmoke')
    ax.set_ylabel("Cases of Covid-19")
    ax.set_xlabel("Number of the week")
    plt.xticks(week_year, rotation ='vertical')

    ax.legend()
    plt.show()

    return


def line_graph_per_country(country):
    '''
    Grafico de linea temporal que muestra el avance de casos de contagio\muertes total por pais.
    '''
    conn = sqlite3.connect('db_covid_world.db')
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()
    
    c.execute("""
            SELECT 
            year_week,
            SUM(cases_weekly),
            SUM(deaths_weekly),
            countries_and_territories
            FROM table_covid_world
            WHERE countries_and_territories LIKE ?
            GROUP BY year_week, countries_and_territories
            ORDER BY year_week;
            """, (country,))
    
    row = c.fetchall()

    conn.commit()
    conn.close()

    country_acc_cases = list(accumulate([i[1] for i in row]))
    country_acc_death = list(accumulate([i[2] for i in row]))

    week_year = [i[0] for i in row]

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot(week_year, country_acc_cases, color='b', label='cases')
    ax.plot(week_year, country_acc_death, color='r', label='death')
    ax.set_facecolor('whitesmoke')
    ax.set_title(f'{country}')
    ax.set_ylabel("Cases/Deaths of Covid-19")
    ax.set_xlabel("Number of the week")
    plt.xticks(week_year, rotation ='vertical')

    ax.legend()
    plt.show()

    return
