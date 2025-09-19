from app import create_app, db
from app.models import User

app = create_app('development')

with app.app_context():
    # 清空测试用户
    User.query.filter_by(email='testuser@example.com').delete()
    db.session.commit()

    # 使用测试客户端模拟注册流程
    with app.test_client() as client:
        # 先访问注册页面获取表单
        response = client.get('/account/register')
        print(f"GET /account/register status: {response.status_code}")

        # 模拟注册表单提交
        response = client.post('/account/register', data={
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password': 'TestPassword123',
            'password2': 'TestPassword123'
        }, follow_redirects=True)

        print(f"POST /register status: {response.status_code}")
        print(f"Redirected to: {response.request.path}")

        # 检查是否重定向到首页
        if response.status_code == 200 and response.request.path == '/':
            print("✓ Registration successful - redirected to homepage")
        else:
            print("✗ Registration failed or unexpected redirect")
            print(f"Response data: {response.get_data(as_text=True)[:500]}...")

        # 验证用户是否创建成功
        user = User.query.filter_by(email='testuser@example.com').first()
        if user:
            print(f"✓ User created: {user.full_name()} ({user.email})")
            print(f"User confirmed: {user.confirmed}")
        else:
            print("✗ User not found in database after registration")