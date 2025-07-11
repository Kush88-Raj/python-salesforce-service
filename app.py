from flask import Flask, jsonify
import importlib.util

app = Flask(__name__)

@app.route('/run-script')
def run_script():
    spec = importlib.util.spec_from_file_location("script", "./script.py")
    script = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script)

    if hasattr(script, 'main'):
        result = script.main()
        return jsonify(result)
    return jsonify([]), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
