from app import create_app, db
from app.account.forms import RegistrationForm
from app.models import User
from flask import request

app = create_app('development')

with app.app_context():
    # 清空测试用户
    User.query.filter_by(email='testuser@example.com').delete()
    db.session.commit()

    print("Testing registration form validation...")

    # 测试表单验证
    with app.test_request_context('/account/register', method='POST', data={
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testuser@example.com',
        'password': 'TestPassword123',
        'password2': 'TestPassword123'
    }):
        form = RegistrationForm()
        print(f"Form validate_on_submit(): {form.validate_on_submit()}")

        if form.validate_on_submit():
            print("Form validation passed")

            # 尝试手动创建用户
            user = User(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=form.password.data
            )

            try:
                db.session.add(user)
                db.session.commit()
                print("✅ User committed to database")
            except Exception as e:
                print(f"❌ Database error: {e}")
                db.session.rollback()
        else:
            print(f"Form errors: {form.errors}")

    # 检查用户是否存在
    user = User.query.filter_by(email='testuser@example.com').first()
    if user:
        print(f"✅ User found: {user.full_name()}")
    else:
        print("❌ User not found")