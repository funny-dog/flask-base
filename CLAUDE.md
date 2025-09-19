# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 在此代码库中工作时提供指导。

## 项目概述

这是一个 Flask 应用程序模板，提供了完整的代码基础结构，包括用户管理、权限系统、数据库操作、邮件发送等功能。

## 核心架构

### 应用结构
- **Blueprint 模式**: 使用 Flask Blueprint 进行模块化开发
  - `app/main/`: 主要功能模块（主页、错误处理等）
  - `app/account/`: 用户账户管理（注册、登录、个人资料等）
  - `app/admin/`: 管理员功能（用户管理、页面编辑等）
- **模型-视图-控制器**: 遵循 MVC 架构模式
- **数据库**: 使用 Flask-SQLAlchemy ORM，支持 PostgreSQL 和 SQLite

### 扩展组件
- **Flask-SQLAlchemy**: 数据库 ORM
- **Flask-Login**: 用户会话管理
- **Flask-Mail**: 邮件发送
- **Flask-WTF**: 表单处理和 CSRF 保护
- **Flask-Assets**: 资源管理和 SCSS 编译
- **Flask-Compress**: Gzip 压缩
- **Flask-RQ**: 异步任务队列（基于 Redis）
- **Flask-Migrate**: 数据库迁移

## 常用命令

### 开发环境设置
```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Unix/MacOS
venv\Scripts\activate.bat  # Windows

# 安装依赖
pip install -r requirements.txt

# 创建配置文件
echo "SECRET_KEY=your_secret_key_here" > config.env

# 初始化数据库
python manage.py recreate_db

# 设置开发环境
python manage.py setup_dev

# 可选：添加测试数据
python manage.py add_fake_data
```

### 运行应用
```bash
# 开发服务器
python manage.py runserver

# 使用 Honcho（支持环境变量）
honcho start -e config.env -f Local
```

### 测试和代码质量
```bash
# 运行测试
python manage.py test

# 代码格式化
python manage.py format
```

### 数据库操作
```bash
# 创建数据库迁移
python manage.py db migrate

# 应用迁移
python manage.py db upgrade

# 重建数据库
python manage.py recreate_db
```

### 异步任务
```bash
# 启动任务队列工作进程
python manage.py run_worker
```

## 配置管理

### 环境变量
应用使用环境变量进行配置，主要配置项：
- `SECRET_KEY`: 应用密钥（必需）
- `FLASK_CONFIG`: 运行环境（development/production/testing/heroku/unix）
- `DATABASE_URL`: 数据库连接字符串
- `REDIS_URL`: Redis 连接字符串
- `MAIL_USERNAME`/`MAIL_PASSWORD`: 邮件服务器凭据
- `ADMIN_EMAIL`/`ADMIN_PASSWORD`: 管理员账户

### 配置文件结构
- `config.py`: 主配置文件，包含不同环境的配置类
- `config.env`: 本地环境变量文件（不应提交到版本控制）

## Docker 支持

### 开发环境
```bash
# 构建并启动所有服务
docker-compose up

# 初始化数据库
docker-compose exec server ./init_database.sh
```

### 服务端口
- **Flask 应用**: http://localhost:5000
- **数据库管理**: http://localhost:8080
- **Redis**: http://localhost:6379

## 开发注意事项

### 代码组织
- 遵循现有的目录结构和命名约定
- 使用 Blueprint 进行模块化开发
- 表单放在 `forms.py`，视图放在 `views.py`
- 数据库模型放在 `models/` 目录

### 资源管理
- SCSS 文件放在 `assets/styles/`
- JavaScript 文件放在 `assets/scripts/`
- 使用 Flask-Assets 进行资源编译和管理

### 邮件系统
- 使用 Flask-Mail 发送邮件
- 支持 SendGrid 或其他 SMTP 服务器
- 邮件模板位于相应的模块中

### 安全性
- 使用 Flask-WTF 提供 CSRF 保护
- 密码使用 ZXCVBN 进行强度检查
- 生产环境应使用 HTTPS（通过 Flask-SSLify）

## 部署

### 本地部署
1. 设置环境变量
2. 初始化数据库
3. 启动 Redis
4. 运行应用服务器
5. 启动任务队列工作进程

### 生产部署
- 使用 Gunicorn 作为 WSGI 服务器
- 配置 Nginx 作为反向代理
- 使用 PostgreSQL 作为生产数据库
- 配置环境变量和日志记录