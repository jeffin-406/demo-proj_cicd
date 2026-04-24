from flask import Flask
from redis import Redis
import os

app = Flask(__name__)

# Fetch variables from .env (via Docker)
DEBUG_MODE = os.getenv('DEBUG', 'False') == 'True'
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)

cache = Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f"<h1>Task Monitor</h1><p>Environment: {'Debug' if DEBUG_MODE else 'Production'}</p><p>Hits: {count}</p>"

if __name__ == "__main__":
    # Use the port defined in .env
    port = int(os.getenv('APP_PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=DEBUG_MODE)
