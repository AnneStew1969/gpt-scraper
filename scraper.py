from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing URL'}), 400

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return jsonify({'content': text[:5000]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/healthz')
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(debug=True)
# redeploy trigger
