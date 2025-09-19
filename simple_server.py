#!/usr/bin/env python
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Base App</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            .header { background: #f8f9fa; padding: 20px; border-radius: 8px; }
            .content { margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Flask Base Application</h1>
                <p>Server is running successfully!</p>
            </div>
            <div class="content">
                <h2>Status: ✅ Running</h2>
                <p>The Flask server is working and accessible.</p>
                <p><strong>Note:</strong> Some database features may be disabled due to compatibility issues.</p>
                <hr>
                <h3>Available Features:</h3>
                <ul>
                    <li>✅ Flask web server</li>
                    <li>✅ Basic routing</li>
                    <li>⚠️  Database features (limited due to SQLAlchemy version compatibility)</li>
                    <li>⚠️  Task queue (RQ functionality disabled)</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)