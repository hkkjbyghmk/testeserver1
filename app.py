from flask import Flask, request, jsonify

app = Flask(__name__)

ADMIN_CODE = '7851'  # Código do administrador

@app.route('/check_code', methods=['POST'])
def check_code():
    if request.method == 'POST':
        data = request.get_json()  # Recebe os dados JSON
        code = data.get('code')  # Obtém o código enviado

        if code == ADMIN_CODE:
            return jsonify({"status": "success", "message": "Código correto!"})
        else:
            return jsonify({"status": "failure", "message": "Código incorreto!"})
    return jsonify({"status": "error", "message": "Método não permitido!"}), 405

if __name__ == '__main__':
    app.run(debug=True)
