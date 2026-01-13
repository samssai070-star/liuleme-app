import streamlit as st
import streamlit.components.v1 as components

# --- 1. 后端精算逻辑 ---
def get_expert_analysis(data):
    try:
        score_val = data.get('score', 0)
        score = int(score_val) if score_val else 0
    except:
        score = 0
    province = data.get('province', '全国')
    
    base_rate = 65 + (score / 10)
    return {
        "success_rate": f"{min(base_rate, 98.5):.1f}%",
        "prov_report": f"检测到您来自 {province}。2026 年该地区竞争极其激烈，继续投入的 ROI 正在下滑。",
        "expert_advice": f"基于均分 {score} 的画像，建议利用日本赛道的降维打击优势。",
        "roi_report": "预测毕业起薪可覆盖 85% 以上的留学总成本。"
    }

# --- 2. 页面配置 ---
st.set_page_config(page_title="溜了么 | 留学就业规划", layout="wide")

# 显示二维码（确保仓库里有 wechat_qr.png）
try:
    st.sidebar.image("wechat_qr.png", caption="扫码添加溜老师")
except:
    st.sidebar.warning("请上传 wechat_qr.png 以显示二维码")

# --- 3. HTML 界面 ---
# 所有的 CSS { } 都已经转义为 {{ }}
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ background-color: #f5f5f7; font-family: sans-serif; text-align: center; padding: 50px; }}
        .card {{ background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); display: inline-block; }}
        .ai-btn {{ background: #ff3b30; color: white; border: none; padding: 12px 25px; border-radius: 20px; cursor: pointer; font-weight: bold; }}
        input, select {{ padding: 10px; margin: 10px; border-radius: 10px; border: 1px solid #ddd; }}
    </style>
</head>
<body>
    <div class="card">
        <h1 style="color:#ff3b30;">溜了么 | 跃迁评估</h1>
        <p>既然这么卷，不如“溜了么”</p>
        <input type="number" id="userScore" placeholder="输入均分">
        <select id="province">
            <option value="北京">北京</option><option value="上海">上海</option><option value="山东">山东</option><option value="广东">广东</option>
        </select>
        <br>
        <button class="ai-btn" onclick="sendData()">开启早规划</button>
    </div>

    <script>
        function sendData() {{
            const data = {{
                score: document.getElementById('userScore').value,
                province: document.getElementById('province').value
            }};
            window.parent.postMessage({{
                type: 'streamlit:setComponentValue',
                value: data
            }}, '*');
        }}
    </script>
</body>
</html>
"""

# --- 4. 运行 ---
user_input = components.html(html_content, height=450)

if user_input:
    res = get_expert_analysis(user_input)
    st.balloons()
    st.divider()
    st.metric("跃迁成功率", res["success_rate"])
    st.error(res["prov_report"])
    st.success(res["expert_advice"])
    st.info(res["roi_report"])
