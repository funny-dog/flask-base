import requests

# 测试当前运行的服务器
print("Testing registration on running server...")

# 测试注册页面可访问性
try:
    response = requests.get('http://localhost:8000/account/register')
    print(f"GET /account/register status: {response.status_code}")

    # 测试注册提交（注意：需要处理CSRF token，但我们在开发环境禁用了）
    response = requests.post('http://localhost:8000/account/register', data={
        'first_name': 'Live',
        'last_name': 'Test',
        'email': 'livetest@example.com',
        'password': 'LiveTest123',
        'password2': '极速赛车开奖直播平台LiveTest123'
    }, allow_redirects=False)

    print(f"POST /account/register status: {response.status_code}")
    print(f"Redirect location: {response.headers.get('Location')}")

    if response.status_code == 302:
        print("✅ Registration submission successful (redirected)")
    else:
        print(f"❌ Registration failed with status: {response.status_code}")
        print(f"Response content: {response.text[:500]}...")

    # 测试是否可以使用相同的邮箱再次注册（应该失败）
    response2 = requests.post('http://localhost:8000/account/register', data={
        'first_name': 'Duplicate',
        'last_name': 'User',
        'email': 'livetest@example.com',
        'password': 'Password123',
        'password2': 'Password123'
    }, allow_redirects=False)

    print(f"Duplicate registration attempt status: {response2.status_code}")
    if response2.status_code == 200 and "already registered" in response2.text.lower():
        print("✅ Duplicate email validation working correctly")
    else:
        print("⚠️  Duplicate email validation may not be working")

except Exception as e:
    print(f"❌ Error during registration test: {e}")

print("\n请描述您遇到的具体问题:")
print("- 无法访问注册页面？")
print("- 表单提交失败？")
print("- 出现错误消息？")
print("- 页面重定向不正确？")
print("- 其他问题？")