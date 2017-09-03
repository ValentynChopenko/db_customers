import os
import string
import sqlite3
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = BASE_DIR + '/database.db'

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def exec_query(query):
    conn = sqlite3.connect(DATABASE_DIR)
    c = conn.cursor()
    data = tuple(c.execute(query))
    res = tuple(data)
    conn.commit()
    conn.close()
    return res

def ask_all_customers_info():
    query = "SELECT * FROM customers"
    answer = exec_query(query)
    return answer

def ask_customer_by_id(customer_id):
    query = "SELECT * FROM customers WHERE CustomerId={}".format(customer_id)
    answer = exec_query(query)
    return answer

def ask_customers_by_phone(phone):
    query = "SELECT * FROM customers WHERE Phone LIKE \'%{}%\'".format(phone)
    answer = exec_query(query)
    return answer

def ask_customers_by_country(country):
    query = "SELECT * FROM customers WHERE LOWER(Country) = \'{}\'".format(country)
    answer = exec_query(query)
    return answer

def get_filter_db(country='%', state='%', city='%'):
    query = "SELECT * FROM customers WHERE LOWER(Country) LIKE \'{}\' AND LOWER(State) LIKE \'{}\' AND LOWER(City) LIKE \'{}\'".format(country, state, city)
    answer = exec_query(query)
    return answer


# clipit
