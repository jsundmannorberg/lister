# Directory list API

## How to use
    
    > docker run -d -p 6379:6379 redis
    > python3 -m venv venv
    > . venv/bin/activate
    > pip install flask redis celery pytest
    > python -m flask --app app run

And then in a separate terminal:

    > . venv/bin/activate
    > python -m celery -A make_celery worker

Now the API is up and running. It accepts POST and GET requests to /api/list_dir
The body of the POST request should be a json body with two different parameters
`directory` and `params`, where `directory` should be a string containing a path to a
directory on the server, and `params` is a string containing the parameters to be
sent to the `ls` command.

`curl -X POST localhost:5000/api/list_dir -H "Content-Type: application/json" -d '{"directory": "/home/my_computer/code", "params": "-la"}'`

The API will return a task id which can then be used to get the result of the execution.

`curl -X GET localhost:5000/api/list_dir?task_id=c7bbbee8-8d63-4d71-8a11-4273e6d5f0c2`