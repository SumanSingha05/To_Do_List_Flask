from app import create_app, db

app = create_app()

# Import Task model after app creation to ensure table creation
from app.models import Task

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)