from todoapi import app, db
from waitress import serve

if __name__ == "__main__":
    db.create_all()
    serve(app, host='0.0.0.0', port=5000)