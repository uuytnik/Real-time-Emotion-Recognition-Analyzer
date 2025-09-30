# Flask app.py - 完整的情绪识别后端
from flask import Flask, Response, render_template, jsonify, request
import cv2
from deepface import DeepFace
from flask_cors import CORS
import numpy as np
import base64
from PIL import Image
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # 允许跨域访问

# 全局变量：摄像头实例
cap = cv2.VideoCapture(0)

# 配置参数
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}


def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def decode_base64_image(base64_string):
    """
    解码Base64图片为numpy array
    
    Args:
        base64_string: Base64编码的图片字符串
        
    Returns:
        numpy.ndarray: OpenCV格式的图片数组
    """
    try:
        # 移除Base64前缀 (data:image/jpeg;base64,)
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        
        # 解码Base64
        img_data = base64.b64decode(base64_string)
        
        # 转换为PIL Image
        img = Image.open(io.BytesIO(img_data))
        
        # 转换为RGB (如果是RGBA或其他格式)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # 转换为numpy array (OpenCV格式: BGR)
        img_array = np.array(img)
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        return img_array
    except Exception as e:
        raise ValueError(f"Base64解码失败: {str(e)}")


def analyze_emotion(img_array):
    """
    使用DeepFace分析图片中的情绪
    
    Args:
        img_array: OpenCV格式的图片数组
        
    Returns:
        dict: 情绪分析结果
    """
    try:
        # 调用DeepFace进行情绪分析
        result = DeepFace.analyze(
            img_array, 
            actions=['emotion'], 
            enforce_detection=False,  # 即使检测不到人脸也返回结果
            silent=True  # 禁止打印日志
        )
        
        # DeepFace可能返回列表或字典
        if isinstance(result, list):
            face = result[0]
        else:
            face = result
        
        # 提取情绪数据
        emotions = face['emotion']
        
        # 将百分比转换为整数
        emotions_rounded = {k: round(v, 2) for k, v in emotions.items()}
        
        return {
            'success': True,
            'emotions': emotions_rounded,
            'dominant_emotion': face.get('dominant_emotion', 'unknown')
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': f'情绪分析失败: {str(e)}'
        }


@app.route('/')
def index():
    """首页路由"""
    return render_template('index.html')


def gen_frames():
    """生成视频流的生成器函数"""
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        
        # 编码为JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        # 生成multipart格式的视频流
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """视频流端点"""
    return Response(
        gen_frames(), 
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


@app.route('/emotion')
def emotion_api():
    """
    从摄像头获取当前帧并分析情绪
    用于实时视频模式
    """
    ret, frame = cap.read()
    
    if not ret:
        return jsonify({
            'success': False,
            'error': '无法从摄像头读取帧'
        }), 500
    
    # 分析情绪
    result = analyze_emotion(frame)
    
    if result['success']:
        return jsonify(result['emotions'])
    else:
        return jsonify({'error': result['error']}), 500


@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    """
    分析上传的图片文件
    支持两种方式：
    1. FormData文件上传 (推荐)
    2. JSON Base64字符串
    """
    img_array = None
    
    try:
        # 方式1: FormData文件上传
        if 'file' in request.files:
            file = request.files['file']
            
            # 验证文件
            if file.filename == '':
                return jsonify({
                    'success': False,
                    'error': '未选择文件'
                }), 400
            
            if not allowed_file(file.filename):
                return jsonify({
                    'success': False,
                    'error': f'不支持的文件格式，允许的格式: {", ".join(ALLOWED_EXTENSIONS)}'
                }), 400
            
            # 检查文件大小
            file.seek(0, 2)  # 移动到文件末尾
            file_size = file.tell()
            file.seek(0)  # 重置到开头
            
            if file_size > MAX_FILE_SIZE:
                return jsonify({
                    'success': False,
                    'error': f'文件过大，最大允许 {MAX_FILE_SIZE // (1024*1024)}MB'
                }), 400
            
            # 读取文件并转换为numpy array
            file_bytes = file.read()
            nparr = np.frombuffer(file_bytes, np.uint8)
            img_array = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if img_array is None:
                return jsonify({
                    'success': False,
                    'error': '无法解析图片文件'
                }), 400
        
        # 方式2: JSON Base64字符串
        elif request.is_json and 'image' in request.json:
            base64_string = request.json['image']
            
            # 检查Base64字符串长度 (粗略估算文件大小)
            estimated_size = len(base64_string) * 3 / 4
            if estimated_size > MAX_FILE_SIZE:
                return jsonify({
                    'success': False,
                    'error': f'图片过大，最大允许 {MAX_FILE_SIZE // (1024*1024)}MB'
                }), 400
            
            img_array = decode_base64_image(base64_string)
        
        else:
            return jsonify({
                'success': False,
                'error': '请提供图片文件或Base64字符串'
            }), 400
        
        # 分析情绪
        result = analyze_emotion(img_array)
        
        if result['success']:
            return jsonify(result['emotions'])
        else:
            return jsonify({'error': result['error']}), 500
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'服务器内部错误: {str(e)}'
        }), 500


@app.route('/health')
def health_check():
    """健康检查端点"""
    return jsonify({
        'status': 'healthy',
        'camera_available': cap.isOpened(),
        'version': '1.0.0'
    })


@app.errorhandler(413)
def request_entity_too_large(error):
    """处理文件过大错误"""
    return jsonify({
        'success': False,
        'error': '上传的文件过大'
    }), 413


@app.errorhandler(500)
def internal_error(error):
    """处理服务器内部错误"""
    return jsonify({
        'success': False,
        'error': '服务器内部错误'
    }), 500


# 应用启动时的配置
@app.before_first_request
def startup():
    """应用启动时的初始化"""
    print("=" * 50)
    print("情绪识别服务已启动")
    print(f"访问地址: http://127.0.0.1:5000")
    print(f"摄像头状态: {'已连接' if cap.isOpened() else '未连接'}")
    print("=" * 50)


# 应用关闭时释放资源
@app.teardown_appcontext
def cleanup(error=None):
    """应用关闭时释放摄像头资源"""
    if cap.isOpened():
        cap.release()


if __name__ == '__main__':
    # 配置上传文件大小限制
    app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE
    
    # 启动Flask应用
    app.run(
        host='0.0.0.0', 
        port=5000,
        debug=True,  # 开发模式，生产环境请设置为False
        threaded=True  # 启用多线程支持
    )