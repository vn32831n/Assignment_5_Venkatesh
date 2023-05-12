import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)

from flask import Flask, jsonify

app = Flask(__name__)

# Route to display a collection of records
@app.route('/customers', methods=['GET'])
def get_customers():
    # Read data from the database
    # Here, you would typically parse the 'database.json' file
    # and retrieve the collection of customer records
    
    # Example response
    customers = [
        {'id': 1, 'name': 'John Doe'},
        {'id': 2, 'name': 'Jane Smith'}
    ]
    
    return jsonify(customers)


# Route to display a single record by ID
@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    # Read data from the database and find the customer with the given ID
    
    # Example response
    customer = {'id': customer_id, 'name': 'John Doe'}
    
    return jsonify(customer)


# Route to display a collection of records for a given entity
@app.route('/customers/<int:customer_id>/orders', methods=['GET'])
def get_customer_orders(customer_id):
    # Read data from the database and find the orders for the given customer ID
    
    # Example response
    orders = [
        {'id': 1, 'product': 'Product A'},
        {'id': 2, 'product': 'Product B'}
    ]
    
    return jsonify(orders)


# Route to display a single record from a collection of a given entity
@app.route('/customers/<int:customer_id>/orders/<int:order_id>', methods=['GET'])
def get_customer_order(customer_id, order_id):
    # Read data from the database and find the order with the given IDs
    
    # Example response
    order = {'id': order_id, 'product': 'Product A'}
    
    return jsonify(order)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
