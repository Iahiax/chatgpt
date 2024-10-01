from flask import Flask, request, jsonify
from ai_module import generate_code  # افترض أن لديك وحدة ذكاء اصطناعي لتوليد الأكواد

app = Flask(__name__)

@app.route('/generate_code', methods=['POST'])
def generate_code_endpoint():
    data = request.json
    language = data.get('language')
    requirements = data.get('requirements')
    code = generate_code(language, requirements)
    return jsonify({'code': code})

if __name__ == '__main__':
    app.run(debug=True)
