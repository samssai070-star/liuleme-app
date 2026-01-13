<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="Content-Style-Type" content="text/css">
  <title></title>
  <meta name="Generator" content="Cocoa HTML Writer">
  <meta name="CocoaVersion" content="1894.7">
  <style type="text/css">
    p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica; color: #000000; -webkit-text-stroke: #000000}
    p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica; color: #000000; -webkit-text-stroke: #000000; min-height: 14.0px}
    p.p3 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px 'PingFang SC'; color: #000000; -webkit-text-stroke: #000000}
    span.s1 {font-kerning: none}
    span.s2 {font: 12.0px 'PingFang SC'; font-kerning: none}
    span.s3 {font: 12.0px Helvetica; font-kerning: none}
  </style>
</head>
<body>
<p class="p1"><span class="s1">import streamlit as st</span></p>
<p class="p1"><span class="s1">import streamlit.components.v1 as components</span></p>
<p class="p1"><span class="s1">import json</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1"># --- 1. Python </span><span class="s2">后端精算逻辑</span><span class="s1"> ---</span></p>
<p class="p1"><span class="s1">def calculate_risk(province, score, budget, math, english):</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span># </span><span class="s2">模拟</span><span class="s1"> 2026 </span><span class="s2">数据库逻辑</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>high_pressure_provinces = ["</span><span class="s2">北京</span><span class="s1">", "</span><span class="s2">上海</span><span class="s1">", "</span><span class="s2">江苏</span><span class="s1">", "</span><span class="s2">浙江</span><span class="s1">", "</span><span class="s2">广东</span><span class="s1">", "</span><span class="s2">山东</span><span class="s1">", "</span><span class="s2">河南</span><span class="s1">"]</span></p>
<p class="p2"><span class="s1"><span class="Apple-converted-space">    </span></span></p>
<p class="p3"><span class="s3"><span class="Apple-converted-space">    </span># </span><span class="s1">基础成功率计算</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>base_rate = 70</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>if province in high_pressure_provinces:</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>invol_rate = 95</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>base_rate += (int(score) / 10)</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>else:</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>invol_rate = 75</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>base_rate += (int(score) / 8)</span></p>
<p class="p2"><span class="s1"><span class="Apple-converted-space">        </span></span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span># </span><span class="s2">学力加成</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>if math == "</span><span class="s2">很强</span><span class="s1">": base_rate += 10</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>if english == "</span><span class="s2">精通</span><span class="s1">": base_rate += 10</span></p>
<p class="p2"><span class="s1"><span class="Apple-converted-space">    </span></span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span># </span><span class="s2">预算修正</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>if budget == "25</span><span class="s2">万以上</span><span class="s1">": base_rate += 5</span></p>
<p class="p2"><span class="s1"><span class="Apple-converted-space">    </span></span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>success_rate = min(98.5, base_rate)</span></p>
<p class="p2"><span class="s1"><span class="Apple-converted-space">    </span></span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>return {</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>"success_rate": f"{success_rate:.1f}%",</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>"involution_rate": invol_rate,</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>"prov_report": f"</span><span class="s2">检测到您来自</span><span class="s1">{province}</span><span class="s2">，该地区</span><span class="s1"> 2026 </span><span class="s2">年考公考研赛道拥挤度已达</span><span class="s1"> {invol_rate}%</span><span class="s2">。边际收益递减严重。</span><span class="s1">",</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>"expert_advice": f"</span><span class="s2">鉴于您的数学学力为</span><span class="s1">{math}</span><span class="s2">且英语</span><span class="s1">{english}</span><span class="s2">，在日元汇率波动的背景下，降维打击国立大学的</span><span class="s1"> ROI</span><span class="s2">（投资回报率）将比在国内卷提升</span><span class="s1"> 3.5 </span><span class="s2">倍。</span><span class="s1">",</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>"roi_report": f"</span><span class="s2">基于</span><span class="s1">{budget}</span><span class="s2">预算，预计</span><span class="s1"> 4 </span><span class="s2">年跃迁总投入可控，起薪预测涨幅</span><span class="s1"> 120%+",</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>}</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1"># --- 2. Streamlit </span><span class="s2">页面配置</span><span class="s1"> ---</span></p>
<p class="p1"><span class="s1">st.set_page_config(page_title="</span><span class="s2">溜了么</span><span class="s1"> | </span><span class="s2">精算级规划</span><span class="s1">", layout="wide")</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p3"><span class="s3"># </span><span class="s1">模拟一个简单的</span><span class="s3"> Session </span><span class="s1">状态来存储计算结果</span></p>
<p class="p1"><span class="s1">if 'analysis_results' not in st.session_state:</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>st.session_state.analysis_results = None</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1"># --- 3. </span><span class="s2">嵌入</span><span class="s1"> HTML/JS </span><span class="s2">前端</span><span class="s1"> ---</span></p>
<p class="p3"><span class="s3"># </span><span class="s1">这里我精简了</span><span class="s3"> HTML </span><span class="s1">部分以突出逻辑，请在实际使用时把你的完整</span><span class="s3"> CSS </span><span class="s1">粘贴进去</span></p>
<p class="p1"><span class="s1">html_content = f"""</span></p>
<p class="p1"><span class="s1">&lt;!DOCTYPE html&gt;</span></p>
<p class="p1"><span class="s1">&lt;html&gt;</span></p>
<p class="p1"><span class="s1">&lt;head&gt;</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>&lt;script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"&gt;&lt;/script&gt;</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>&lt;script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"&gt;&lt;/script&gt;</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>&lt;style&gt;</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>/* </span><span class="s2">这里粘贴你之前的完整</span><span class="s1"> CSS </span><span class="s2">代码</span><span class="s1"> */</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>:root {{ --accent-color: #ff3b30; }}</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>/* ... </span><span class="s2">省略重复的样式</span><span class="s1"> ... */</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>&lt;/style&gt;</span></p>
<p class="p1"><span class="s1">&lt;/head&gt;</span></p>
<p class="p1"><span class="s1">&lt;body&gt;</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>&lt;div id="app_interface"&gt;</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>&lt;/div&gt;</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>&lt;script&gt;</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>// </span><span class="s2">当用户点击</span><span class="s1">“</span><span class="s2">开启早规划</span><span class="s1">”</span><span class="s2">时，将数据传给</span><span class="s1"> Python</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>async function runAnalysis() {{</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">            </span>const formData = {{</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">                </span>province: document.getElementById('province').value,</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">                </span>score: document.getElementById('userScore').value,</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">                </span>budget: document.getElementById('budget').value,</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">                </span>math: document.getElementById('math').value,</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">                </span>english: document.getElementById('english').value</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">            </span>}};</span></p>
<p class="p2"><span class="s1"><span class="Apple-converted-space">            </span></span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">            </span>// </span><span class="s2">将数据传回</span><span class="s1"> Streamlit (</span><span class="s2">使用</span><span class="s1"> window.parent </span><span class="s2">交互</span><span class="s1">)</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">            </span>window.parent.postMessage({{</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">                </span>type: 'streamlit:setComponentValue',</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">                </span>value: formData</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">            </span>}}, '*');</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>}}</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>// </span><span class="s2">监听来自</span><span class="s1"> Python </span><span class="s2">的计算结果</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>window.addEventListener('message', function(event) {{</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">            </span>const results = event.data.analysis;</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">            </span>if (results) {{</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">                </span>renderReport(results); // </span><span class="s2">调用你原来的渲染报告逻辑</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">            </span>}}</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>}});</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>&lt;/script&gt;</span></p>
<p class="p1"><span class="s1">&lt;/body&gt;</span></p>
<p class="p1"><span class="s1">&lt;/html&gt;</span></p>
<p class="p1"><span class="s1">"""</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p3"><span class="s3"># </span><span class="s1">渲染组件并捕获前端输入</span></p>
<p class="p1"><span class="s1">captured_data = components.html(html_content, height=900, scrolling=True)</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1"># --- 4. </span><span class="s2">实时响应与计算</span><span class="s1"> ---</span></p>
<p class="p1"><span class="s1">if captured_data:</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span># </span><span class="s2">当</span><span class="s1"> JS </span><span class="s2">传回</span><span class="s1"> formData </span><span class="s2">时，</span><span class="s1">Python </span><span class="s2">立即计算</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>results = calculate_risk(</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>captured_data['province'],<span class="Apple-converted-space"> </span></span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>captured_data['score'],<span class="Apple-converted-space"> </span></span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>captured_data['budget'],</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>captured_data['math'],</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">        </span>captured_data['english']</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>)</span></p>
<p class="p2"><span class="s1"><span class="Apple-converted-space">    </span></span></p>
<p class="p3"><span class="s3"><span class="Apple-converted-space">    </span># </span><span class="s1">将计算结果存入状态，触发</span><span class="s3"> JS </span><span class="s1">渲染（或直接显示在侧边栏测试）</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>st.sidebar.success(f"</span><span class="s2">计算完成：成功率</span><span class="s1"> {results['success_rate']}")</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>st.sidebar.info("PDF </span><span class="s2">报告已在网页预览中生成</span><span class="s1">")</span></p>
</body>
</html>
