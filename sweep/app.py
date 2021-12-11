from flask import Flask, render_template, redirect
from scripts import login, sweep_run
from logging import error
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import scripts as s


app = Flask(__name__)

# Main Page where functions live in app

@app.route('/')
def index():
    return render_template('index.html')

# login page to sign in and verify through microsoft

@app.route('/login')
def login():
    login = s.login()
    return redirect('/')

# Warehouse shipment URL 

@app.route('/ship_lines')
def ship_lines():
    shiplines = s.ship_lines()
    return redirect('/')

# Route to run the sweep

@app.route('/sweep_run')
def sweep_run():
    sweep_run = s.sweep_run()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)