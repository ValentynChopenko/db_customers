from flask import Flask
from app import views

app = Flask(__name__)

app.add_url_rule('/', 'index', views.index)
app.add_url_rule('/customers/', 'customers', views.all_customers)
app.add_url_rule('/get_customer/<int:customer_id>/', 'customer_by_id', views.customer_by_id)
app.add_url_rule('/search_phone/<phone>/', 'customers_by_phone', views.customers_by_phone)
app.add_url_rule('/country_search/<country>/', 'customers_by_country', views.customers_by_country)
app.add_url_rule('/filter_db/', 'filter_db', views.filter_db)
