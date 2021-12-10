import os
from flask import Flask, request, abort, jsonify, send_file, send_from_directory
from flask_cors import CORS
import random
from datetime import datetime, timedelta
from werkzeug import secure_filename


import io




def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    
    '''
    @DONE: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    '''
    CORS(app, resources={r"/*": {'origins': '*'}})
    

    '''
    @DONE: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response


    @app.route("/")
    def hello():
        return "Hello World! this is vicintori api"

    @app.route('/rates', methods=['POST'])
    def shipping_rates():
        body = request.get_json()
        # text = body.get('text', 'No text')
        result = "Hello our shipping rates are 7.99 EUR!"
        return jsonify(
            {
                "result": result
            }
        )


    





    '''
    @DONE: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found",
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable",
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request",
        }), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed",
        }), 405
    
    return app

        
