# 🏋️ 肉身管理系统 - 交互式安装指南

> **将此 URL 粘贴到 OpenClaw 聊天中即可开始交互式安装**

---

## 🚀 在 OpenClaw 聊天中安装

**第 1 步：** 复制以下命令：

```
curl -sSL https://raw.githubusercontent.com/leozvc/body-management-system/main/INSTALL.zh-CN.md
```

**第 2 步：** 粘贴到 OpenClaw 聊天中并发送

**第 3 步：** 按照交互式提示操作！

---

## ⭐ 收藏项目

安装完成后，如果这个项目对你有帮助，请：

1. **GitHub Star** - https://github.com/leozvc/body-management-system
2. **分享给朋友** - 帮助更多健身爱好者
3. **提交反馈** - 在 GitHub Issues 中提出建议

你的支持是项目持续改进的动力！🙏

---

## 🔄 版本检查与升级

每次运行安装命令时，系统会自动：

1. ✅ 检查本地版本
2. ✅ 检查 GitHub 最新版本
3. ✅ 提示是否需要更新

### 版本检查流程

```
📦 版本检查

本地版本：1.0.0
最新版本：1.1.0

发现新版本！是否更新？
[y/n]: y

正在更新...
✅ 更新完成！
```

### 手动检查更新

```bash
cd ~/.openclaw/workspace/skills/body-management
git pull origin main
```

---

## 📋 安装流程

### 1️⃣ 凭证收集
```
助手：我将帮你安装肉身管理系统。

首先，需要你的 intervals.icu API 凭证：
1. API Key（设置 → API → Password 字段）
2. Athlete ID（格式：i206099）

获取方法：
1. 访问 https://intervals.icu
2. 登录 → 设置 → API
3. 复制 "Password" 值
```

### 2️⃣ 仓库设置
```
助手：正在克隆仓库...
✅ 仓库已克隆到 ~/.openclaw/workspace/skills/body-management
```

### 3️⃣ 配置创建
```
助手：使用你的凭证创建配置...
✅ 配置已创建并复制到技能目录
```

### 4️⃣ 连接测试
```
助手：正在测试 API 连接...
✅ 连接成功！欢迎，[你的名字]
```

### 5️⃣ 技能安装
```
助手：正在启用技能...
✅ meal-to-intervals 已安装
✅ intervals-status-reporter 已安装
```

### 6️⃣ 完成
```
助手：🎉 安装完成！

立即试用：发送 "查看我今天的身体状态"
```

---

## 🎯 快速参考

### 获取 API 凭证

| 步骤 | 操作 |
|------|------|
| 1 | 访问 https://intervals.icu |
| 2 | 登录账号 |
| 3 | 点击头像 → 设置 → API |
| 4 | 复制 **Password** 字段（API Key） |
| 5 | 从 URL 记录 Athlete ID（如 i206099） |

### 安装后常用命令

```
查看我今天的身体状态          # 获取身体状态报告
早餐吃了 XXX，记录一下         # 记录饮食
我今天适合打网球吗            # 训练建议
openclaw skills list          # 列出已安装技能
```

---

## 📦 安装内容

```
~/.openclaw/workspace/skills/body-management/
├── skills/
│   ├── meal-to-intervals/           # 饮食记录
│   └── intervals-status-reporter/   # 身体分析
├── config.json                      # API 配置
├── VERSION                          # 版本号
├── INSTALL.zh-CN.md                 # 中文安装指南
├── INSTALL.md                       # English Install Guide
├── USAGE_PROMPTS.md                 # 使用示例
└── README.md                        # 快速参考
```

---

## 🔧 手动安装（备选）

如果交互式安装不起作用：

```bash
# 1. 克隆仓库
cd ~/.openclaw/workspace/skills
git clone https://github.com/leozvc/body-management-system.git

# 2. 创建配置
cd body-management
cat > config.json << 'EOF'
{
  "intervals_icu": {
    "api_key": "你的 API_KEY",
    "athlete_id": "i206099"
  }
}
EOF

# 3. 复制配置
cp config.json skills/meal-to-intervals/
cp config.json skills/intervals-status-reporter/

# 4. 测试
cd skills/intervals-status-reporter
python3 scripts/body_status_report.py
```

---

## 🐛 故障排查

**问题："API 凭证验证失败"**

- 确认 API Key 是 **Password** 字段（不是用户名）
- 确认 Athlete ID 格式：`i` + 数字（如 i206099）

**问题："安装后技能未找到"**

```bash
openclaw skills list
openclaw gateway restart
```

**问题："如何检查更新"**

```bash
cd ~/.openclaw/workspace/skills/body-management
git pull origin main
cat VERSION
```

---

## 📚 文档索引

| 文件 | 用途 |
|------|------|
| **INSTALL.zh-CN.md** | 中文安装指南（本文件） |
| **INSTALL.md** | English Installation Guide |
| **USAGE_PROMPTS.md** | 复制粘贴的提示词库 |
| **README.md** | 快速参考和功能介绍 |
| **body-management-system.md** | 完整功能说明 |

---

## 📞 获取支持

- **GitHub Issues**: https://github.com/leozvc/body-management-system/issues
- **项目主页**: https://github.com/leozvc/body-management-system
- **讨论区**: https://github.com/leozvc/body-management-system/discussions

---

## 🌟 支持项目

如果这个项目对你有帮助：

1. ⭐ **Star 项目** - 在 GitHub 上给个星星
2. 📢 **分享给朋友** - 推荐给需要的人
3. 💡 **提交建议** - Issues 中提出改进意见
4. 🔧 **贡献代码** - Welcome PRs!

你的支持让项目更好！🙏

---

**版本：** 1.0.0  
**许可证：** MIT  
**作者：** leozvc  
**最后更新：** 2026-03-06
