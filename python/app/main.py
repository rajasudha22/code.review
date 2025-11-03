from flask import Flask
from app.routes.task_routes import task_routes

def create_app():
    app = Flask(__name__)
    
    # Register routes
    app.register_blueprint(task_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)