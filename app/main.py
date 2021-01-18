from todoapi import app, db
from waitress import serve
from paste.translogger import TransLogger

import logging

if __name__ == "__main__":
    db.create_all()

    app = TransLogger(app)
    serve(app, host='0.0.0.0', port=5000)