from datetime import datetime
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate('./remake-portaldeinvestidores-firebase-adminsdk-qicex-c999fc9f2f.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
collection_name = 'users'

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    try:
        doc_refs = db.collection(collection_name)
        docs = doc_refs.stream()
        json = [doc.to_dict() for doc in docs]
        return jsonify(json)
    except Exception as e:
        print(f"Error in GET /users: {str(e)}")
        return jsonify({"Error": "Internal Server Error"}), 500


@app.route('/users', methods=['POST'])
def post_users():
    if not request.json or 'display_name' not in request.json:
        return jsonify({"Error": "Invalid input"}), 400

    email = request.json.get('email')
    password = request.json.get('password')
    display_name = request.json.get('display_name')

    try:
        user = auth.create_user(email=email, password=password)
    except Exception as e:
        print(f"Error creating user: {str(e)}")
        return jsonify({"Error": f"Failed to create user: {str(e)}"}), 400

    user_id = user.uid
    current_time = datetime.utcnow().isoformat()
    request_json = {
        "display_name": display_name,
        "email": email,
        "password": password,
        "user_id": user_id,
        "created_time": current_time
    }

    try:
        doc_ref = db.collection(collection_name).document(user_id)
        doc_ref.set(request_json)
    except Exception as e:
        print(f"Error saving user data: {str(e)}")
        return jsonify({"Error": f"Failed to save user data: {str(e)}"}), 500

    return jsonify(request_json), 201


@app.route('/users/<string:id>', methods=['PATCH'])
def patch_user(user_id):
    user_ref = db.collection('users').document(user_id)
    user = user_ref.get()
    
    if not user.exists:
        return jsonify({"error": "Usuário não encontrado"}), 404

    data = request.get_json()
    
    if 'email' in data:
        email = data['email']
        try:
            auth.update_user(user_id, email=email)
        except firebase_admin._auth_utils.EmailAlreadyExistsError:
            return jsonify({"error": "Este email já está em uso."}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    
    user_ref.update(data)
    updated_user = user_ref.get().to_dict()
    
    return jsonify(updated_user), 200

@app.route('users/<string:id>', method=['DELETE'])
def delete_user(user_id):
    user_ref = db.collection('users').document(user_id)
    user = user_ref.get()

    if not user.exists:
        return jsonify({"error": "Usuário não encontrado"}), 404

    try:
        auth.delete_user(user_id)
        user_ref.delete()

    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"message": "Usuário deletado com sucesso"}), 200
        
        
if __name__ == '__main__':
    app.run(debug=True)
