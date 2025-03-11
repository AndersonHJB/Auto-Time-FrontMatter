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
# 功能2: /date-text
# 返回 date_text.html, 显示指定文本, 其中 date 只替换当前日期, 并自动复制
# ----------------------------------------------------------------------------
@app.route('/date-text')
@app.route('/vuepress-front-matter')
@app.route('/docs')
def date_text():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('date_text.html', current_time=current_time)

# ----------------------------------------------------------------------------
# 功能3: /vlog
# 返回 vlog_content.html, 内含多行 YAML 风格文本 + 一段文案
# 同样自动替换 date: 为当前日期, 并自动复制
# ----------------------------------------------------------------------------
@app.route('/hexo-front-matter')
@app.route('/hexo')
@app.route('/blog')
def vlog():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('vlog_content.html', current_time=current_time)

# ----------------------------------------------------------------------------
# 启动
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    # 1) http://127.0.0.1:5000/        -> index.html + 只复制日期
    # 2) http://127.0.0.1:5000/date-text -> date_text.html + 文本 + 自动复制
    # 3) http://127.0.0.1:5000/vlog    -> vlog_content.html + 文本 + 自动复制
    app.run(host='0.0.0.0', port=5000, debug=True)
