from flask import Blueprint, request, jsonify


def api_blueprint(redis_client):
    api_bp = Blueprint('api', __name__)

    @api_bp.route('/', methods=['GET'])
    def get_index():
        key = request.args.get('key')
        if not key:
            return jsonify({'error': 'Bad request'}), 400
            
        value = redis_client.get(key)
        if value is None:
            return jsonify({'error': 'This "key" doesnt exists'}), 400
        
        value = value.decode('utf-8')
        return jsonify({'value': value}), 200

    @api_bp.route('/', methods=['POST'])
    def post_index():
        data = request.json
        key = data.get('key')
        if not key or not data.get('value'):
            return jsonify({'error': 'Bad request'}), 400
    
        if redis_client.exists(key):
            return jsonify({'error': 'This key alredy exists'}), 400
                
        redis_client.set(data['key'], data['value'])
        return jsonify({'messge': 'Data saved'}), 200

    @api_bp.route('/', methods=['PUT'])
    def put_index():
        data = request.json
        key = data.get('key')
        value = data.get('value')
        if not key or not value:
            return jsonify({'error': 'Bad request'}), 400
        
        if not redis_client.exists(key):
            return jsonify({'error': 'This "key" doesnt exists'}), 400

        redis_client.set(key, value)
        return jsonify({'messge': 'New value saved'}), 200

    return api_bp