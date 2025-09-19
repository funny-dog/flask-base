#!/usr/bin/env python
import requests
import time

def test_auth():
    base_url = "http://127.0.0.1:5000"

    # 1. 获取登录页面获取CSRF token
    print("1. 获取登录页面...")
    response = requests.get(f"{base_url}/account/login")
    print(f"状态码: {response.status_code}")

    # 2. 尝试管理员登录
    print("\n2. 尝试管理员登录...")
    login_data = {
        'email': 'admin@example.com',
        'password': 'admin123'
    }

    # 尝试直接登录（不处理CSRF，只是测试）
    response = requests.post(
        f"{base_url}/account/login",
        data=login_data,
        allow_redirects=False
    )

    print(f"登录响应状态码: {response.status_code}")
    print(f"响应头: {dict(response.headers)}")

    # 3. 测试注册页面
    print("\n3. 测试注册页面...")
    response = requests.get(f"{base_url}/account/register")
    print(f"注册页面状态码: {response.status_code}")

    # 4. 测试主页
    print("\n4. 测试主页...")
    response = requests.get(f"{base_url}/")
    print(f"主页状态码: {response.status_code}")

    print("\n✅ 认证功能测试完成！")

if __name__ == "__main__":
    time.sleep(2)  # 等待服务器完全启动
    test_auth()