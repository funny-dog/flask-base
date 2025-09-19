from app import create_app, db
from app.models import User

app = create_app('development')

with app.app_context():
    # 清空测试用户
    User.query.filter_by(email='testuser@example.com').delete()
    db.session.commit()

    # 使用测试客户端模拟注册流程
    with app.test_client() as client:
        # 模拟注册表单提交
        response = client.post('/account/register', data={
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password': 'TestPassword123',
            'password2': '极速赛车开奖直播平台TestPassword123'
        })

        print(f"POST /account/register status: {response.status_code}")
        print(f"Location header: {response.headers.get('Location')}")

        # 验证用户是否创建成功
        user = User.query.filter_by(email='testuser@example.com').first()
        if user:
            print(f"✅ User created: {user.full_name()} ({user.email})")
            print(f"User confirmed: {user.confirmed}")
            print("✅ Registration successful!")
        else:
            print("❌ User not found in database after registration")