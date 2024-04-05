# app.py

from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Route to display inventory
@app.route('/')
def index():
    inventory = read_inventory()
    return render_template('index.html', inventory=inventory)

# Route to add new item to inventory
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']

        add_to_inventory(name, quantity, price)
        return redirect(url_for('index'))
    return render_template('add_item.html')

# Function to read inventory from CSV
def read_inventory():
    with open('data/inventory.csv', 'r') as file:
        reader = csv.DictReader(file)
        inventory = [row for row in reader]
    return inventory

# Function to add item to inventory CSV
def add_to_inventory(name, quantity, price):
    with open('data/inventory.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, quantity, price])

if __name__ == '__main__':
    app.run(debug=True)
