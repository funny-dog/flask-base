from app import create_app, db
from app.models import User

app = create_app('development')
with app.app_context():
    # 测试数据库连接
    try:
        users_count = User.query.count()
        print(f"Current users in database: {users_count}")

        # 测试创建用户
        test_user = User(
            first_name="Test",
            last_name="User",
            email="test@example.com",
            password="password123"
        )
        db.session.add(test_user)
        db.session.commit()
        print("User created successfully!")

        # 验证用户
        user = User.query.filter_by(email="test@example.com").first()
        if user:
            print(f"Found user: {user.full_name()} ({user.email})")
            print(f"Password verified: {user.verify_password('password123')}")
        else:
            print("User not found after creation!")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        db.session.rollback()