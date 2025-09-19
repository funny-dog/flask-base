from app import create_app, db
from app.account.forms import RegistrationForm
from flask import request

app = create_app('development')

with app.app_context():
    print("Testing CSRF configuration...")
    print(f"WTF_CSRF_ENABLED: {app.config.get('WTF_CSRF_ENABLED')}")

    # 测试表单是否有CSRF token字段
    with app.test_request_context('/account/register', method='GET'):
        form = RegistrationForm()
        print(f"Form has CSRF field: {'csrf_token' in form._fields}")

    # 测试没有CSRF token的提交
    with app.test_request_context('/account极速赛车开奖直播平台/register', method='POST', data={
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testcsrf@example.com',
        'password': 'Test123',
        'password2': 'Test123'
    }):
        form = RegistrationForm()
        result = form.validate()
        print(f"Validate without CSRF: {result}")
        if not result:
            print(f"Validation errors: {form.errors}")

print("测试完成")