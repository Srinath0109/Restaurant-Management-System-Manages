from flask import Flask
from routes import restaurant_routes
from database import init_db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
init_db(app)

# Register API routes
app.register_blueprint(restaurant_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
