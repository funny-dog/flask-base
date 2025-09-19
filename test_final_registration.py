from app import create_app, db
from app.models import User

app = create_app('development')

with app.app_context():
    # 清空测试用户
    User.query.filter_by(email='finaltest@example.com').delete()
    db.session.commit()

    print("Testing complete registration flow...")

    # 使用测试客户端模拟完整注册流程
    with app.test_client() as client:
        # 1. 访问注册页面
        response = client.get('/account/register')
        print(f"1. GET /account/register status: {response.status_code}")

        # 2. 提交注册表单（不跟随重定向）
        response = client.post('/account/register', data={
            'first_name': 'Final',
            'last_name': 'Test',
            'email': 'finaltest@example.com',
            'password': 'FinalTest123',
            'password2': 'FinalTest123'
        }, follow_redirects=False)

        print(f"2. POST /account/register status: {response.status_code}")
        print(f"   Location header: {response.headers.get('Location')}")

        # 3. 检查用户是否创建成功
        user = User.query.filter_by(email='finaltest@example.com').first()
        if user:
            print(f"3. ✅ User created: {user.full_name()} ({user.email})")
            print(f"   User confirmed: {user.confirmed}")
            print("🎉 REGISTRATION SUCCESSFUL!")
        else:
            print("3. ❌ User not found in database")

        # 4. 跟随重定向（如果有）
        if response.status_code == 302 and response.headers.get('Location'):
            redirect_url = response.headers.get('Location')
            response = client.get(redirect_url)
            print(f"4. GET {redirect_url} status: {response.status_code}")

        # 5. 验证可以登录
        response = client.post('/account/login', data={
            'email': 'finaltest@example.com',
            'password': 'FinalTest123'
        }, follow_redirects=False)

        print(f"5. POST /account/login status: {response.status_code}")
        if response.status_code == 302:
            print("   ✅ Login redirect successful (user can log in)")
        else:
            print("   ❌ Login failed")