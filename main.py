import requests
from flask import Flask, jsonify, request
from dateutil import parser

app = Flask(__name__)

def is_vax_ready(birthdate):
  r = requests.post("https://covid19.min-saude.pt/pedido-de-agendamento/", data = { "f_dia" : birthdate.day, "f_mes": birthdate.month , "f_ano" : birthdate.year })
  return b"Aguarde" not in r.content

@app.route("/", methods=['GET']) 
def homepage():
  birthdate = parser.parse(request.args.get('birthdate'))
  return jsonify({'is_vax_ready' : is_vax_ready(birthdate)})
