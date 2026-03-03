import streamlit as st
import plotly.graph_objects as go

# 页面配置
st.set_page_config(page_title="技术架构 | 极速出海", page_icon="🧠")

# 页面标题
st.title("🧠 02 技术架构：AI+数字化深度融合")

# 引用方案原文
st.markdown("""
<div class="quote-block" style="background-color: #f0f7fa; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #1e5f7a; margin-bottom: 2rem;">
    <strong>评分要素：创新创意</strong> — 突出对技能水平、职业素养、团队合作、实践应用、创新创意等方面的综合考查。
    <div style="text-align: right; margin-top: 0.5rem;">—— 《2026年世界职业院校技能大赛实施方案》第4页</div>
</div>
""", unsafe_allow_html=True)

# ===== AI+数字化融合理念（自适应高度）=====
st.markdown("### 🧠 AI是大脑 + 💪 数字化是手脚")

col_ai, col_plus, col_digital = st.columns([2, 1, 2])

with col_ai:
    st.markdown("""
    <div style="background: linear-gradient(145deg, #e1f0f7, #ffffff); padding: 1.5rem; border-radius: 15px; border: 2px solid #1e5f7a; height: auto; min-height: 450px; display: flex; flex-direction: column;">
        <h3 style="color: #1e5f7a; text-align: center; margin-top: 0;">🧠 AI模块</h3>
        <div style="flex: 1;">
            <p><strong>🤖 数字人直播</strong></p>
            <ul style="margin-top: -5px; margin-bottom: 10px;">
                <li><strong>技术</strong>：AI数字人、语音合成、自然语言处理</li>
                <li><strong>功能</strong>：24小时智能获客、多语言互动</li>
                <li><strong>创新点</strong>：替代初级人力，成本200元/月</li>
            </ul>
            <p style="margin-top: 15px;"><strong>🧠 Coze工作流</strong></p>
            <ul style="margin-top: -5px; margin-bottom: 10px;">
                <li><strong>技术</strong>：智能体+知识库+意图识别</li>
                <li><strong>功能</strong>：询盘自动分类、智能回复生成</li>
                <li><strong>创新点</strong>：0代码搭建，业务人员可配置</li>
            </ul>
        </div>
        <p style="text-align: center; margin-top: 15px; margin-bottom: 0;"><a href="https://www.coze.cn/work_flow?space_id=7491136436608106536&workflow_id=7613027449315885065&force_stay=1" target="_blank">🔗 点击查看Coze工作流（需登录）</a></p>
    </div>
    """, unsafe_allow_html=True)

with col_plus:
    st.markdown("<h1 style='text-align: center; color: #f3b33d; font-size: 3rem; margin-top: 200px;'>+</h1>", unsafe_allow_html=True)

with col_digital:
    st.markdown("""
    <div style="background: linear-gradient(145deg, #fef9e9, #ffffff); padding: 1.5rem; border-radius: 15px; border: 2px solid #f3b33d; height: auto; min-height: 450px; display: flex; flex-direction: column;">
        <h3 style="color: #f3b33d; text-align: center; margin-top: 0;">💪 数字化模块</h3>
        <div style="flex: 1;">
            <p><strong>💰 报价系统</strong></p>
            <ul style="margin-top: -5px; margin-bottom: 10px;">
                <li><strong>技术</strong>：Excel VBA / Python+Streamlit</li>
                <li><strong>功能</strong>：2分钟极速报价、汇率实时同步</li>
                <li><strong>创新点</strong>：双方案并行，适应不同企业需求</li>
            </ul>
            <p style="margin-top: 15px;"><strong>📄 RPA单证</strong></p>
            <ul style="margin-top: -5px; margin-bottom: 10px;">
                <li><strong>技术</strong>：Power Automate Desktop</li>
                <li><strong>功能</strong>：3秒自动填单，错误率26%→2%</li>
                <li><strong>创新点</strong>：0成本，单证员可自己录制</li>
            </ul>
        </div>
        <p style="text-align: center; margin-top: 15px; margin-bottom: 0; visibility: hidden;">占位符</p>
    </div>
    """, unsafe_allow_html=True)

# ===== 技术架构图 =====
st.markdown("---")
st.markdown("### 📐 技术架构图")

# 创建架构图
fig = go.Figure()

# 定义节点
nodes = [
    {"x": 0, "y": 5, "text": "客户", "color": "#f3b33d", "size": 40},
    {"x": 2, "y": 5, "text": "数字人(AI)", "color": "#1e5f7a", "size": 40},
    {"x": 4, "y": 5, "text": "Coze(AI)", "color": "#1e5f7a", "size": 40},
    {"x": 6, "y": 5, "text": "报价(数字化)", "color": "#f3b33d", "size": 40},
    {"x": 8, "y": 5, "text": "RPA(数字化)", "color": "#f3b33d", "size": 40}
]

# 添加节点
fig.add_trace(go.Scatter(
    x=[n["x"] for n in nodes],
    y=[n["y"] for n in nodes],
    mode="markers+text",
    marker=dict(
        size=[n["size"] for n in nodes],
        color=[n["color"] for n in nodes],
        line=dict(color="#FFFFFF", width=2)
    ),
    text=[n["text"] for n in nodes],
    textposition="bottom center",
    textfont=dict(size=12, color="#0a3142"),
    showlegend=False
))

# 添加连接线
for i in range(4):
    fig.add_shape(
        type="line",
        x0=i*2, y0=5,
        x1=(i+1)*2, y1=5,
        line=dict(color="#aaa", width=2, dash="dot")
    )

# 添加箭头指示
for i in range(4):
    fig.add_annotation(
        x=i*2+1, y=5.1,
        text="→",
        showarrow=False,
        font=dict(size=20, color="#666")
    )

fig.update_layout(
    title="数据流向图：从获客到履约全流程",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-0.5, 8.5]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[4, 6]),
    height=350,
    plot_bgcolor="white",
    margin=dict(l=20, r=20, t=40, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# 流程图说明
st.markdown("""
<div style="display: flex; justify-content: space-around; margin: 1rem 0; padding: 1rem; background-color: #f8fbfd; border-radius: 10px;">
    <div><span style="color: #1e5f7a; font-weight: bold;">🧠 AI模块</span>：思考、互动、决策</div>
    <div><span style="color: #f3b33d; font-weight: bold;">💪 数字化模块</span>：执行、提效、落地</div>
</div>
""", unsafe_allow_html=True)

# ===== 技术融合价值总结 =====
st.markdown("---")
st.markdown("""
<div style="background-color: #e6f0f5; padding: 1.8rem; border-radius: 15px; margin-top: 1rem;">
    <h4 style="color: #1e5f7a; margin-top: 0;">✨ 技术融合价值</h4>
    <p style="font-size: 1.1rem;">AI负责<strong>思考、互动、决策</strong>，数字化负责<strong>执行、提效、落地</strong>。两者结合，形成完整的“极速出海”解决方案，完全符合世校赛对“创新创意”的评分要求。</p>
    <div style="display: flex; gap: 2rem; margin-top: 1rem; justify-content: center; flex-wrap: wrap;">
        <div><span style="background-color: #1e5f7a; color: white; padding: 0.3rem 1rem; border-radius: 20px;">🧠 数字人直播</span></div>
        <div><span style="background-color: #1e5f7a; color: white; padding: 0.3rem 1rem; border-radius: 20px;">🧠 Coze工作流</span></div>
        <div><span style="background-color: #f3b33d; color: #1e3f4e; padding: 0.3rem 1rem; border-radius: 20px;">💰 报价系统</span></div>
        <div><span style="background-color: #f3b33d; color: #1e3f4e; padding: 0.3rem 1rem; border-radius: 20px;">📄 RPA单证</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# 底部导航提示
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7a8e99; font-size: 0.9rem; padding: 1rem;">
    ⚡ 本页面展示了“极速出海”的核心技术架构 | 自适应高度，防止内容溢出
</div>
""", unsafe_allow_html=True)
