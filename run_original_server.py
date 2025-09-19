#!/usr/bin/env python
"""
启动原始Flask应用服务器
解决了数据库兼容性问题后的完整版本
"""
from app import create_app, db
import os
import time

app = create_app('development')

def setup_database():
    """设置数据库"""
    with app.app_context():
        print("正在初始化数据库...")
        db.create_all()
        print("数据库初始化完成！")

def run_server():
    """启动服务器"""
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '127.0.0.1')

    print(f"Flask Base 应用服务器启动中...")
    print(f"服务器地址: http://{host}:{port}")
    print(f"调试模式: {app.debug}")
    print(f"数据库: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print("-" * 50)

    # 确保数据库已设置
    setup_database()

    # 启动服务器
    app.run(host=host, port=port, debug=False, threaded=True)

if __name__ == '__main__':
    run_server()