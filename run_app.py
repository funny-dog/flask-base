#!/usr/bin/env python3
import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('FLASK_ENV') == 'development'

    print(f"Starting Flask app on {host}:{port}")
    print(f"Debug mode: {debug}")

    app.run(host=host, port=port, debug=debug)