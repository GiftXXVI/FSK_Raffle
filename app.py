from flask import Flask
from flask import request, jsonify, abort
from random import shuffle, sample, choices
import numpy as np
from flask_cors import CORS
import os


def create_app(test_mode=False):
    app = Flask(__name__)
    CORS(app)
    return app


test_mode = os.getenv('TEST_MODE')
APP = create_app(test_mode)


@APP.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization, true')
    response.headers.add(
        'Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
    return response


@APP.route('/winners/get', methods=['POST'])
def get_winner():
    body = request.get_json()
    rng = np.random.default_rng()
    n = 1
    p = 0.5
    flip = rng.binomial(n, p)
    if body is None:
        abort(400)
    else:
        participants = body.get('participants', None)
        num_winners = body.get('num_winners', 1)
        if participants is None or num_winners > len(participants):
            abort(422)
        else:
            if flip < p:
                shuffle(participants)
                winners = choices(participants, k=num_winners)
            else:
                rng.shuffle(participants)
                np_winners = rng.choice(participants, num_winners)
                winners = np_winners.tolist()
            return jsonify({
                'success': True,
                'winners': winners
            })


@APP.errorhandler(422)
def error_422(error):
    message = 'unprocessable'
    return jsonify({
        'success': False,
        'error': 422,
        'message': message.lower()
    }), 422


@APP.errorhandler(400)
def error_400(error):
    message = 'bad request'
    return jsonify({
        'success': False,
        'error': 400,
        'message': message.lower()
    }), 400


@APP.errorhandler(500)
def error_500(error):
    message = 'server error'
    return jsonify({
        'success': False,
        'error': 500,
        'message': message.lower()
    }), 500


@APP.errorhandler(403)
def error_403(error):
    message = 'forbidden'
    return jsonify({
        'success': False,
        'error': 403,
        'message': message.lower()
    }), 401


@APP.errorhandler(405)
def error_405(error):
    message = 'not allowed'
    return jsonify({
        'success': False,
        'error': 405,
        'message': message.lower()
    }), 405


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
