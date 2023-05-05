"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaai4bhp8u791guddcg-a.oregon-postgres.render.com",
        database="todo_hp0v",
        user="todo_hp0v_user",
        password="wqcXk0AXQ1RaYnLOq0uQ7Fseobzs8RFq")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
