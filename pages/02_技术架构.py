import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="技术架构 | 极速出海", page_icon="🧠")

st.title("🧠 02 技术架构：AI+数字化深度融合")

st.markdown("""
<div class="quote-block" style="background-color: #f0f7fa; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #1e5f7a; margin-bottom: 2rem;">
    <strong>评分要素：创新创意</strong> — 突出对技能水平、职业素养、团队合作、实践应用、创新创意等方面的综合考查。
    <div style="text-align: right; margin-top: 0.5rem;">—— 《2026年世界职业院校技能大赛实施方案》第4页</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🧠 AI是大脑 + 💪 数字化是手脚")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
    <div style="background: linear-gradient(145deg, #e1f0f7, #ffffff); padding: 2rem; border-radius: 20px; border: 3px solid #1e5f7a; height: 100%;">
        <h2 style="color: #1e5f7a; text-align: center;">🧠 AI模块</h2>
        <h4>🤖 数字人直播</h4>
        <ul>
            <li><strong>技术</strong>：AI数字人、语音合成、自然语言处理</li>
            <li><strong>功能</strong>：24小时智能获客、多语言互动</li>
            <li><strong>创新点</strong>：替代初级人力，成本200元/月</li>
        </ul>
        <h4 style="margin-top: 1.5rem;">🧠 Coze工作流</h4>
        <ul>
            <li><strong>技术</strong>：智能体+知识库+意图识别</li>
            <li><strong>功能</strong>：询盘自动分类、智能回复生成</li>
            <li><strong>创新点</strong>：0代码搭建，业务人员可配置</li>
        </ul>
        <p style="margin-top: 1rem; text-align: center;"><a href="https://www.coze.cn/work_flow?space_id=7491136436608106536&workflow_id=7610438014247305225&force_stay=1" target="_blank">🔗 点击查看Coze工作流（需登录）</a></p>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div style="background: linear-gradient(145deg, #fef9e9, #ffffff); padding: 2rem; border-radius: 20px; border: 3px solid #f3b33d; height: 100%;">
        <h2 style="color: #f3b33d; text-align: center;">💪 数字化模块</h2>
        <h4>💰 报价系统</h4>
        <ul>
            <li><strong>技术</strong>：Excel VBA / Python+Streamlit</li>
            <li><strong>功能</strong>：2分钟极速报价、汇率实时同步</li>
            <li><strong>创新点</strong>：双方案并行，适应不同企业需求</li>
        </ul>
        <h4 style="margin-top: 1.5rem;">📄 PRA单证</h4>
        <ul>
            <li><strong>技术</strong>：Power Automate Desktop</li>
            <li><strong>功能</strong>：3秒自动填单，错误率26%→2%</li>
            <li><strong>创新点</strong>：0成本，单证员可自己录制</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📐 技术架构图")

# 架构图
fig = go.Figure()

# 添加节点
nodes = [
    {"x": 0, "y": 5, "text": "客户", "color": "#f3b33d"},
    {"x": 2, "y": 5, "text": "数字人(AI)", "color": "#1e5f7a"},
    {"x": 4, "y": 5, "text": "Coze(AI)", "color": "#1e5f7a"},
    {"x": 6, "y": 5, "text": "报价(数字化)", "color": "#f3b33d"},
    {"x": 8, "y": 5, "text": "PRA(数字化)", "color": "#f3b33d"}
]

fig.add_trace(go.Scatter(
    x=[n["x"] for n in nodes],
    y=[n["y"] for n in nodes],
    mode="markers+text",
    marker=dict(size=[40]*5, color=[n["color"] for n in nodes]),
    text=[n["text"] for n in nodes],
    textposition="bottom center",
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

fig.update_layout(
    title="数据流向图：从获客到履约全流程",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    height=300,
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div style="background-color: #e6f0f5; padding: 1.5rem; border-radius: 10px; margin-top: 2rem;">
    <h4 style="color: #1e5f7a;">✨ 技术融合价值</h4>
    <p>AI负责<strong>思考、互动、决策</strong>，数字化负责<strong>执行、提效、落地</strong>。两者结合，形成完整的“极速出海”解决方案，完全符合世校赛对“创新创意”的评分要求。</p>
</div>
""", unsafe_allow_html=True)
