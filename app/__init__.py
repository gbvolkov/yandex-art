from flask import Flask, redirect, url_for
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    from app.art import art as art_blueprint

    app.register_blueprint(art_blueprint)
    
    #with app.app_context():
    #    db.create_all()
    @app.route('/')
    def root():
        return redirect(url_for('art.post_generator'))

    return app
