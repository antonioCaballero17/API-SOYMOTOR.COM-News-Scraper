from flask import Flask, jsonify


from blueprints.blueprint_soy_motor import blueprint_soy_motor

app = Flask(__name__)

app.register_blueprint(blueprint=blueprint_soy_motor, url_prefix="/api/v1/soy_motor")

app.run()
