from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# ----------------------------------------------------------------------------
# 根路径 / 的功能（保持不变）
# 访问 http://127.0.0.1:5000/ 时，返回一个页面:
#   - 调用 /api/time 获取 JSON
#   - 只显示并复制日期部分
# ----------------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# 返回 JSON（包含 time, author, site），供前端 AJAX 获取
@app.route('/api/time', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        "time": current_time,
        "author": "AI悦创",
        "site": "bornforthis.cn"
    }
    return jsonify(data)

# ----------------------------------------------------------------------------
# 新增路径 /date-text
# 访问 http://127.0.0.1:5000/date-text 时，会在页面上显示特定的"纯文本"，并自动复制
# ----------------------------------------------------------------------------
@app.route('/date-text')
def date_text():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('date_text.html', current_time=current_time)

# ----------------------------------------------------------------------------
# 启动服务
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    # 访问 http://127.0.0.1:5000/      -- 原有 JSON 功能，返回日期并复制日期
    # 访问 http://127.0.0.1:5000/date-text -- 新增的纯文本格式页面，并自动复制
    app.run(host='0.0.0.0', port=5000, debug=True)
