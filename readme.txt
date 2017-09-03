If you want to use db_filter there are following urls:
    - /all_customers/ - output all customers;
    - /get_customer/<int:customer_id>/ - ouput customer with id = customer_id;
    - /search_phone/<phone>/ - output customer with a phone number that contents
      requested data <phone>. For example: requested phone is '345' (integer), appropriately 
      all customers with a part of phone number '345' will be output;
    - /country_search/<country>/ - output all customers with country = <country>;
    - /filter_db/ - output all customers with country = country(string),
      state = state(string), city = city(string), for example:
      /filter_db/?country=usa&state=ca&city=cupertino.
