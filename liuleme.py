Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
import streamlit as st
import streamlit.components.v1 as components
import json

# --- 1. Python 精算逻辑 (核心算法) ---
def get_expert_analysis(data):
    try:
        # 确保数据存在且能转为整数
        score_val = data.get('score', 0)
        score = int(score_val) if score_val else 0
    except (ValueError, TypeError):
        score = 0
        
    province = data.get('province', '全国')
    budget = data.get('budget', '10-15万')
    
    # 成功率模型
    base_rate = 65 + (score / 10)
    if budget == "25万以上": base_rate += 10
    
    return {
        "success_rate": f"{min(base_rate, 98.5):.1f}%",
        "involution_rate": 88 if province in ["北京", "上海", "山东", "河南"] else 75,
        "prov_report": f"检测到您来自 {province}。2026 年该地区竞争极其激烈，继续投入的 ROI 正在下滑。",
        "expert_advice": f"基于均分 {score} 的画像，日本国立大学（如：筑波大学）的降维打击优势明显。",
        "roi_report": f"年度预算 {budget} 适配当前汇率环境，预测起薪涨幅 120%+"
    }

# --- 2. 页面基础配置 ---
st.set_page_config(page_title="溜了么 | 留学就业规划", layout="wide", initial_sidebar_state="collapsed")

# 侧边栏：放置你的微信二维码
try:
    st.sidebar.image("wechat_qr.png", caption="扫码添加溜老师，获取 1对1 深度解析")
except:
    st.sidebar.warning("请上传 wechat_qr.png 到 GitHub 仓库以显示二维码")

# --- 3. HTML 界面逻辑 ---
# 注意：CSS 中的所有 { } 必须替换为 {{ }} 否则 Python f-string 会报错
html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <style>
        :root {{ --accent-color: #ff3b30; --apple-grey: #86868b; }}
        p.p1 {{
            margin: 0.0px 0.0px 0.0px 0.0px; 
            font: 12.0px Helvetica; 
            color: #000000; 
            -webkit-text-stroke: #000000;
        }}
        body {{ background-color: #f5f5f7; font-family: sans-serif; }}
        .hero {{ text-align: center; padding: 100px 20px; }}
        .ai-btn {{ background: var(--accent-color); color: white; border: none; padding: 15px 30px; border-radius: 30px; font-weight: 600; cursor: pointer; }}
        .search-box {{ margin-top: 30px; }}
        input {{ padding: 12px; border-radius: 10px; border: 1px solid #ddd; width: 250px; }}
    </style>
</head>
<body>
    <section class="hero">
        <div class="hero-text">
            <h1>从焦虑中，<br><span style="color:var(--accent-color);">优雅地溜出去。</span></h1>
            <div class="search-box">
                <input type="number" id="userScore" placeholder="输入均分（如 85）">
                <select id="province" style="padding:12px; border-radius:10px;">
                    <option value="北京">北京</option>
                    <option value="上海">上海</option>
                    <option value="山东">山东</option>
                    <option value="广东">广东</option>
                </select>
                <button class="ai-btn" onclick="sendToPython()">开启早规划</button>
            </div>
        </div>
    </section>

    <script>
        async function sendToPython() {{
            const formData = {{
                province: document.getElementById('province').value,
                score: document.getElementById('userScore').value,
                budget: "15-25万",
                math: "一般",
                english: "良好"
            }};
... 
...             // 将数据发送给 Python 后端
...             window.parent.postMessage({{
...                 type: 'streamlit:setComponentValue',
...                 value: formData
...             }}, '*');
...         }}
... 
...         // 监听 Python 返回的结果（如果需要预览）
...         window.addEventListener('message', function(e) {{
...             if (e.data.type === 'streamlit:render') {{
...                 const result = e.data.args.analysis_result;
...                 if (result) {{
...                     console.log("分析结果已到达前端", result);
...                 }}
...             }}
...         }});
...     </script>
... </body>
... </html>
... """
... 
... # --- 4. 运行 Streamlit 应用 ---
... user_input = components.html(html_content, height=600, scrolling=False)
... 
... # 如果前端传回了数据
... if user_input:
...     analysis_result = get_expert_analysis(user_input)
...     
...     # 在 Streamlit 原生界面显示结果（这样最稳妥，不会报错）
...     st.divider()
...     col1, col2 = st.columns(2)
...     with col1:
...         st.metric("跃迁成功率预测", analysis_result["success_rate"])
...         st.error(f"🚩 赛道诊断: {analysis_result['prov_report']}")
...     with col2:
...         st.success(f"🎓 专家建议: {analysis_result['expert_advice']}")
...         st.info(f"💰 ROI 财务回报: {analysis_result['roi_report']}")
...     
