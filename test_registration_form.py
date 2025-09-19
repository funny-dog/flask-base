from app import create_app, db
from app.account.forms import RegistrationForm
from app.models import User
from flask import request
from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request

app = create_app('development')
with app.app_context():
    try:
        # 模拟表单提交
        with app.test_request_context('/register', method='POST', data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'Password123',
            'password2': 'Password123'
        }):
            form = RegistrationForm()
            print(f"Form validate_on_submit(): {form.validate_on_submit()}")

            if form.validate_on_submit():
                print("Form validation passed!")
                print(f"First name: {form.first_name.data}")
                print(f"Email: {form.email.data}")

                # 尝试创建用户
                user = User(
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    password=form.password.data
                )

                db.session.add(user)
                try:
                    db.session.commit()
                    print("User created successfully!")
                except Exception as e:
                    print(f"Database commit error: {e}")
                    db.session.rollback()
            else:
                print("Form validation failed:")
                for field, errors in form.errors.items():
                    print(f"  {field}: {errors}")

    except Exception as e:
        print(f"Error in test: {e}")
        import traceback
        traceback.print_exc()