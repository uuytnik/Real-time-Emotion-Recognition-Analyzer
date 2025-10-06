
---

# 🎭 实时表情识别分析器

> 基于深度学习的人工智能表情识别 Web 应用

![表情识别](https://img.shields.io/badge/表情识别-实时分析-blue)
![Vue3](https://img.shields.io/badge/Vue3-前端框架-green)
![Flask](https://img.shields.io/badge/Flask-后端框架-red)
![DeepFace](https://img.shields.io/badge/DeepFace-AI模型-orange)

---

## ✨ 项目特色

* 🎯 **实时表情分析** - 通过摄像头实时捕捉并分析面部表情
* 🖼️ **图片上传分析** - 支持上传图片进行表情识别
* 🎨 **现代化 UI 设计** - 玻璃态设计 + 流畅动画效果
* 📱 **响应式布局** - 完美适配各种设备屏幕
* ⚡ **高性能优化** - 使用 `requestAnimationFrame` 实现高效分析循环

---

## 🚀 快速开始

### 环境要求

* Python 3.8+
* 现代浏览器（支持 WebRTC）

### 安装与运行

1. **克隆项目**

   ```bash
   git clone https://github.com/your-username/emotion-recognition.git
   cd emotion-recognition
   ```

2. **安装 Python 依赖**

   ```bash
   pip install -r requirements.txt
   ```

3. **启动后端服务**

   ```bash
   python app.py
   ```

4. **打开前端页面**
   直接在浏览器中打开 `frontend.html` 或访问 `http://localhost:5000`

---

## 🛠️ 技术栈

* **前端技术：** Vue 3、现代 CSS、WebRTC API、Canvas API
* **后端技术：** Flask、DeepFace、OpenCV、CORS 支持

---

## 📁 项目结构

```
emotion-recognition/
├── frontend.html        # 主前端页面
├── app.py               # Flask 后端服务
├── requirements.txt     # Python 依赖
├── README.md            # 项目说明文档
├── test.py              # 测试脚本
├── camera_check.py      # 摄像头检查工具
└── .gitignore           # Git 忽略配置
```

---

## 🎮 使用方式

### 实时视频分析

1. 点击 "实时视频分析" 标签
2. 允许摄像头访问权限
3. 点击 "开始分析" 按钮
4. 查看实时表情识别结果

### 图片上传分析

1. 点击 "上传图片分析" 标签
2. 拖拽或点击选择图片
3. 系统自动分析并显示结果

---

## 📊 识别情绪类型

| 情绪       | 中文 | Emoji |
| -------- | -- | ----- |
| happy    | 高兴 | 😄    |
| sad      | 悲伤 | 😢    |
| angry    | 愤怒 | 😡    |
| surprise | 惊讶 | 😮    |
| fear     | 害怕 | 😨    |
| disgust  | 厌恶 | 🤢    |
| neutral  | 中性 | 😐    |

---

## 🔧 核心接口

### 实时情绪分析

```http
GET /emotion
Response: { "happy": 75.2, "sad": 12.1, ... }
```

### 图片情绪分析

```http
POST /analyze_image
Body: { "image": "base64_string" }
Response: { "emotions": { ... }, "dominant_emotion": "happy" }
```

---

## 👥 团队成员

* **宋亦晨** - 后端开发 & AI 集成
* **龙俊海** - 前端开发 & UI 设计
* **陈殿泽** - 项目管理 & 文档撰写
* **左得霖** - 测试验证 & 质量保证

---

## 📝 许可证

本项目采用 **MIT 许可证**

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

---
