from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Fetch environment variables
DEBUG_MODE = os.getenv('DEBUG', 'False') == 'True'
APP_PORT = int(os.getenv('APP_PORT', 5000))

# Local in-memory storage (Resets on restart)
task_list = []

@app.route('/')
def index():
    return render_template('index.html', tasks=task_list)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('task')
    if task_content:
        task_list.append(task_content)
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT, debug=DEBUG_MODE)
