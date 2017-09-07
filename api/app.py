import os
from flask import Flask
from flask import url_for
from worker import celery
import celery.states as states

app = Flask(__name__)


@app.route('/add/<int:param1>/<int:param2>')
def add(param1, param2):
    task = celery.send_task('tasks.add', args=[param1, param2], kwargs={})
    response = "<a href='{url}'>check status of {id} </a>".format(id=task.id,
                                                                  url=url_for('check_task', task_id=task.id, external=True))
    return response


@app.route('/check/<string:task_id>')
def check_task(task_id):
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)

if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', True),
            port=int(os.environ.get('PORT', 5000)),
            host=os.environ.get('HOST', '0.0.0.0'))
