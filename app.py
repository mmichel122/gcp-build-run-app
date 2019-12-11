import os
from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello():
    target = os.environ.get('TARGET', 'GOOGLE CLOUD PLATFORM')
    return 'Greetings from {}!!!'.format(target)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
