import logging

from celery.result import AsyncResult
from flask import Blueprint
from flask import request

from . import tasks

bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/list_dir", methods=['GET', 'POST'])
def request_list_dir():
    if request.method == 'GET':
        task_id = request.args.get('task_id')
        result = AsyncResult(task_id)
        execution_successful = False
        if result.ready() and result.successful():
            execution_successful = result.result["success"]
            if not execution_successful:
                logger = logging.getLogger('task')
                logger.info("Execution failed".format(result.result['message']))
        return {
            "ready": result.ready(),
            "successful": result.successful() and execution_successful,
            "value": result.result if result.ready() else None,
        }
    else:
        json_body = request.get_json()
        directory = json_body["directory"]
        params = json_body["params"]
        return {'task_id': tasks.list_dir.delay(directory, params).id}