from app import create_app, db

app = create_app('development')
with app.app_context():
    print('Database URI:', app.config.get('DATABASE_URL'))
    print('Debug mode:', app.config.get('DEBUG'))
    try:
        db.engine.connect()
        print('Database connection successful')
    except Exception as e:
        print('Database connection error:', e)