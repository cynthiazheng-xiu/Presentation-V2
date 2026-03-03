import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="痛点与数据 | 极速出海", page_icon="📊")

st.title("📊 01 痛点与数据：从11家企业真实问卷出发")

st.markdown("""
<div class="quote-block" style="background-color: #f9f2e5; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #f3b33d; margin-bottom: 2rem;">
    “参赛队伍围绕生产、管理、服务一线<strong>真问题、真场景</strong>，自主确定参赛项目名称，自主设计参赛项目内容，自主选择参赛设备，<strong>展示真技能</strong>。”
    <div style="text-align: right; margin-top: 0.5rem;">—— 《2026年世界职业院校技能大赛实施方案》第3页</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📋 调研概况")

col_info1, col_info2, col_info3 = st.columns(3)
with col_info1:
    st.metric("调研企业", "11家", "遵义小微外贸")
with col_info2:
    st.metric("问卷回收", "11份", "有效率100%")
with col_info3:
    st.metric("信度系数", "0.683", "可接受水平")

st.markdown("### 🔍 三组核心数据（项目灵魂）")

# 数据可视化
col1, col2, col3 = st.columns(3)

with col1:
    fig1 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=40,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "报价半天以上 (%)"},
        delta={'reference': 100, 'valueformat': ".0f"},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "#1e5f7a"},
            'steps': [
                {'range': [0, 40], 'color': "#e6f0f5"},
                {'range': [40, 100], 'color': "#f8d7da"}],
            'threshold': {
                'line': {'color': "#f3b33d", 'width': 4},
                'thickness': 0.75,
                'value': 40}}))
    fig1.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("**💡 我们解决：2分钟报价**")
    st.caption("专业软件使用率：0%")

with col2:
    fig2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=26,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "单证错误率 (%)"},
        gauge={
            'axis': {'range': [None, 30]},
            'bar': {'color': "#dc3545"},
            'steps': [
                {'range': [0, 2], 'color': "#d4edda"},
                {'range': [2, 26], 'color': "#fff3cd"}],
            'threshold': {
                'line': {'color': "#f3b33d", 'width': 4},
                'thickness': 0.75,
                'value': 2}}))
    fig2.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("**💡 我们解决：3秒填单，错误率2%**")
    st.caption("60%企业无IT人员")

with col3:
    fig3 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=70,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "缺运营人才 (%)"},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "#1e5f7a"},
            'steps': [
                {'range': [0, 70], 'color': "#e6f0f5"},
                {'range': [70, 100], 'color': "#f8d7da"}]}))
    fig3.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("**💡 我们解决：24小时数字人直播，成本200元/月**")
    st.caption("预算1000-3000元占71%")

st.markdown("---")
st.markdown("### 📋 详细调研数据")

detail_data = pd.DataFrame({
    "指标": ["报价时间>半天", "专业软件使用率", "单证错误率", "无IT人员", "缺运营人才", "预算1000-3000元", "已开展外贸业务", "计划1年内开展"],
    "比例": ["40%", "0%", "26%", "60%", "70%", "71%", "36.36%", "54.55%"],
    "解决方案": ["2分钟报价", "Excel+VBA+Python", "PRA自动填充", "轻量化工具", "AI数字人", "服务费模式", "已对接", "正在对接"]
})
st.dataframe(detail_data, use_container_width=True, hide_index=True)

st.markdown("""
<div style="background-color: #e6f0f5; padding: 1.5rem; border-radius: 10px; margin-top: 2rem;">
    <h4 style="color: #1e5f7a;">📌 调研结论</h4>
    <p>遵义小微外贸企业数字化基础薄弱，但发展意愿强烈：<strong>90.91%</strong> 企业已开展或计划1年内开展外贸/跨境电商业务。我们的项目正是针对这一需求，提供轻量化、零IT、低预算的数字化解决方案。</p>
</div>
""", unsafe_allow_html=True)
