import os
from flask import Flask, render_template, url_for
import random
import string


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        return render_template('index.html', password = gen_password())

    def gen_password(): 
 	    #input the length of password
        length = 8

        #define data
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        #string.ascii_letters

        #combine the data
        all = lower + upper + num + symbols

        #use random 
        temp = random.sample(all,length)

        #create the password 
        password = "".join(temp)

        #print the password
        return password
    
    return app

app = create_app()

app.run(debug=True)