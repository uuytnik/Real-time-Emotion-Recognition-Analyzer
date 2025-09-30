# 🎭 实时表情识别分析器

> 基于深度学习的人工智能表情识别 Web 应用

![表情识别演示](https://img.shields.io/badge/表情识别-实时分析-blue)
![Vue3](https://img.shields.io/badge/Vue3-前端框架-green)
![Flask](https://img.shields.io/badge/Flask-后端框架-red)
![DeepFace](https://img.shields.io/badge/DeepFace-AI模型-orange)

## ✨ 项目特色

- 🎯 **实时表情分析** - 通过摄像头实时捕捉并分析面部表情
- 🖼️ **图片上传分析** - 支持上传图片进行表情识别
- 🎨 **现代化 UI 设计** - 玻璃态设计 + 流畅动画效果
- 📱 **响应式布局** - 完美适配各种设备屏幕
- ⚡ **高性能优化** - 使用 requestAnimationFrame 实现高效分析循环

## 🚀 快速开始

### 环境要求
- Python 3.8+
- 现代浏览器（支持 WebRTC）

### 安装与运行

1. **克隆项目**
   ```bash
   git clone https://github.com/your-username/emotion-recognition.git
   cd emotion-recognition
安装 Python 依赖
bash
复制
pip install -r requirements.txt
启动后端服务
bash
复制
python app.py
打开前端页面
bash
复制
# 直接打开 frontend.html
# 或访问 http://localhost:5000
🛠️ 技术栈
前端技术
Vue 3 - 渐进式 JavaScript 框架
现代 CSS - 玻璃态设计、渐变动画
WebRTC API - 摄像头访问
Canvas API - 图像处理
后端技术
Flask - Python Web 框架
DeepFace - 深度学习表情识别
OpenCV - 计算机视觉处理
CORS 支持 - 跨域请求处理
📁 项目结构
复制
emotion-recognition/
├── frontend.html          # 主前端页面
├── app.py                 # Flask 后端服务
├── requirements.txt       # Python 依赖
├── README.md              # 项目说明
├── 前端设计方案.md         # 详细设计文档
├── 前后端对接方案.md       # 接口文档
└── 团队协作规范.md         # 开发规范
🎮 使用方式
实时视频分析
点击「实时视频分析」标签
允许摄像头访问权限
点击「开始分析」按钮
查看实时表情识别结果
图片上传分析
点击「上传图片分析」标签
拖拽或点击选择图片
系统自动分析并显示结果
📊 识别情绪类型
表格
复制
情绪	中文	Emoji
happy	高兴	😄
sad	悲伤	😢
angry	愤怒	😡
surprise	惊讶	😮
neutral	中性	😐
fear	害怕	😨
disgust	厌恶	🤢
👥 团队协作
团队成员
成员 A - 后端开发 & AI 集成
成员 B - 前端开发 & UI 设计
成员 C - 项目管理 & 文档撰写
成员 D - 测试验证 & 质量保证
开发流程
我们采用 Git Flow 工作流，详细规范请参考「团队协作规范.md」
🔧 API 接口
实时情绪分析
http
复制
GET /emotion
响应示例：
JSON
复制
{ "happy": 75.2, "sad": 12.1, ... }
图片情绪分析
http
复制
POST /analyze_image
请求体：
JSON
复制
{ "image": "base64_string" }
响应示例：
JSON
复制
{ "emotions": { ... }, "dominant_emotion": "happy" }
🎯 性能优化
✅ 图像压缩处理（480×480 分辨率）
✅ 分析频率控制（1 秒/次）
✅ 内存泄漏防护
✅ 错误边界处理
📝 许可证
本项目采用 MIT 许可证 —— 查看 LICENSE 文件了解详情。
🤝 贡献指南
欢迎提交 Issue 和 Pull Request！
Fork 本仓库
创建特性分支 (git checkout -b feature/AmazingFeature)
提交更改 (git commit -m 'Add some AmazingFeature')
推送到分支 (git push origin feature/AmazingFeature)
开启 Pull Request
