import celery.states as states
from flask import Flask
from flask import url_for, jsonify
from worker import celery

dev_mode = True
app = Flask(__name__)
app.config.update(
    TESTING=dev_mode,
    DEBUG=dev_mode,
    USE_RELOADER=dev_mode,
    THREADED=False
)


@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    task = celery.send_task('tasks.add', args=[param1, param2], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response


@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)


@app.route('/health_check')
def health_check() -> str:
        return jsonify("OK")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')
