from flask import Flask
from app import views

app = Flask(__name__)

app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/gen-pass/<int:pass_len>/<int:pass_count>', 'gen_pass', views.gen_pass)
app.add_url_rule('/all_customers/', 'all_customers', views.all_customers)
app.add_url_rule('/get_customer/<int:customer_id>/', 'customer_by_id', views.customer_by_id)
app.add_url_rule('/search_phone/<phone>/', 'customers_by_phone', views.customers_by_phone)
app.add_url_rule('/country_search/<country>/', 'customers_by_country', views.customers_by_country)
app.add_url_rule('/filter_db/', 'filter_db', views.filter_db)

"""
"""
