from flask import Flask 

def routes(app):
    @app.route('/')
    def index():
        return 'hello world'