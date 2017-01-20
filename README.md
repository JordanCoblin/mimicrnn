# rnnApp #
A web app that uses a LSTM Recurrent Neural Net to generate text based on user inputted training data.

## Running Instructions ##

You will need to open three separate terminal windows.

1. Start celery worker by running in the first terminal window: `celery -A mimicrnn.app.celery worker`
2. Start redis server (assuming that you've added redis to PATH) in the second terminal window: `redis-server`
3. Set the flask app, in cmd: `set FLASK_APP=mimicrnn` OR in powershell: `setx FLASK_APP mimicrnn`
4. Run the flask app in the third terminal window: `flask run`
