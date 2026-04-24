from flask import Flask, render_template, request, redirect
from redis import Redis
import os

app = Flask(__name__)

# Fetch environment variables
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
DEBUG_MODE = os.getenv('DEBUG', 'False') == 'True'

cache = Redis(host=REDIS_HOST, port=REDIS_PORT)

@app.route('/')
def index():
    # Fetch all tasks from a Redis list named 'task_list'
    tasks = cache.lrange('task_list', 0, -1)
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        cache.rpush('task_list', task_content)
    return redirect('/')

if __name__ == "__main__":
    port = int(os.getenv('APP_PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=DEBUG_MODE)
