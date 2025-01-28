from .app import app, db
from . import models
from . import views


if __name__ == '__main__':
    app.run(debug=True, port=8000)
