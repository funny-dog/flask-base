#!/usr/bin/env python
from flask import Flask, render_template_string, session
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf
import requests

app = Flask(__name__)
app.secret_key = 'test-secret-key'
csrf = CSRFProtect(app)

@app.route('/test-csrf')
def test_csrf():
    csrf_token = generate_csrf()
    return f'''
    <html>
    <body>
        <h1>CSRF Test</h1>
        <form method="POST" action="/test-submit">
            <input type="hidden" name="csrf_token" value="{csrf_token}">
            <input type="text" name="test" value="test">
            <button type="submit">Submit</button>
        </form>
        <p>CSRF Token: {csrf_token}</p>
    </body>
    </html>
    '''

@app.route('/test-submit', methods=['POST'])
def test_submit():
    return 'CSRF test successful!'

if __name__ == '__main__':
    app.run(port=5001, debug=True)