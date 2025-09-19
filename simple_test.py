import time
import requests

print("等待服务器启动...")
time.sleep(3)

# 测试服务器是否响应
try:
    response = requests.get('http://127.0.0.1:8000/', timeout=5)
    print(f"首页状态: {response.status_code}")

    # 测试注册页面
    response = requests.get('http://127.0.0.1:8000/account/register', timeout=5)
    print(f"注册页面状态: {response.status_code}")

    # 简单的表单测试
    if response.status_code == 200:
        print("✅ 注册页面可访问")

        # 检查页面内容
        if '注册' in response.text or 'Register' in response.text:
            print("✅ 注册表单找到")
        else:
            print("❌ 注册表单未找到")
            print("页面内容预览:", response.text[:200])
    else:
        print("❌ 注册页面不可访问")

except requests.exceptions.RequestException as e:
    print(f"❌ 服务器连接错误: {e}")
    print("请检查服务器是否正在运行")

print("\n如果您仍然无法注册，请描述:")
print("1. 具体的错误消息")
print("2. 您进行的操作步骤")
print("3. 浏览器中看到的页面内容")