from flask import Flask

app = Flask(__name__)

@app.route('/health')
def photon():
  return {'success': 'true'}

   