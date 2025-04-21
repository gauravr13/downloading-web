from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def handle_download():
    data = request.get_json()
    url = data.get('url')
    
    # Mock response - Replace with actual API integration
    return jsonify({
        "formats": [
            {
                "url": url,
                "type": "video",
                "quality": "1080p",
                "mimeType": "video/mp4",
                "size": "125MB"
            },
            {
                "url": url,
                "type": "audio",
                "quality": "320kbps",
                "mimeType": "audio/mpeg",
                "size": "8.5MB"
            }
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)