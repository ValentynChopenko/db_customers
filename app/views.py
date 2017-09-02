from flask import render_template
from flask import request
from app.utils import id_generator
from app.utils import ask_all_customers_info
from app.utils import ask_customer_by_id
from app.utils import ask_customers_by_phone
from app.utils import ask_customers_by_country
from app.utils import get_filter_db

def index():
    return render_template('index.html')

def gen_pass(pass_len, pass_count):
    context = {
        "passwords": [id_generator(pass_len) for i in range(pass_count)],
        "pass_len": pass_len,
        "pass_count": pass_count,
    }
    return render_template('passwords.html', context = context)

def all_customers():
    context = ask_all_customers_info()
    return render_template('customers.html', context = context)

def customer_by_id(customer_id):
    context = ask_customer_by_id(customer_id)
    return render_template('customers.html', context = context)

def customers_by_phone(phone):
    context = ask_customers_by_phone(phone)
    return render_template('customers.html', context = context)

def customers_by_country(country):
    context = ask_customers_by_country(country)
    return render_template('customers.html', context = context)

def filter_db():
    country = request.args.get('country')
    state = request.args.get('state')
    city = request.args.get('city')
    context = get_filter_db(country, state, city)
    return render_template('customers.html', context = context)
