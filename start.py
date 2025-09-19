#!/usr/bin/env python3
import os
from flask import Flask
from app import create_app, db
from app.models import Role, User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

with app.app_context():
    db.create_all()
    Role.insert_roles()
    # 创建管理员用户
    admin_query = Role.query.filter_by(name='Administrator')
    if admin_query.first() is not None:
        if User.query.filter_by(email='admin@example.com').first() is None:
            user = User(
                first_name='Admin',
                last_name='Account',
                password='admin123',
                confirmed=True,
                email='admin@example.com'
            )
            db.session.add(user)
            db.session.commit()
            print('Added administrator {}'.format(user.full_name()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)