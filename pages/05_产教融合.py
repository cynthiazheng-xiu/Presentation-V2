import streamlit as st

st.set_page_config(page_title="产教融合 | 极速出海", page_icon="🤝")

st.title("🤝 05 产教融合：真实落地服务产业")

st.markdown("""
<div class="quote-block" style="background-color: #f0f7fa; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #1e5f7a; margin-bottom: 2rem;">
    <strong>评分要素：应用价值</strong> — 着力推进产教融合机制创新，坚持产业行业需求引领，提升人才培养与产业需求的适配度。
    <div style="text-align: right; margin-top: 0.5rem;">—— 《2026年世界职业院校技能大赛实施方案》第2页</div>
</div>
""", unsafe_allow_html=True)

# ===== 企业合作 =====
st.markdown("### 🏢 企业合作进展")

col_enter1, col_enter2 = st.columns(2)

with col_enter1:
    st.markdown("""
    <div style="background-color: #f0f7fa; padding: 1.5rem; border-radius: 15px; border-left: 5px solid #1e5f7a; height: 250px;">
        <h3 style="color: #1e5f7a;">🏢 贵州遵礼外贸有限公司</h3>
        <p style="font-size: 1.2rem; margin: 1rem 0;"><strong>合作进展</strong></p>
        <ul>
            <li>✅ 4名学生正在实习</li>
            <li>✅ 合作开发报价模板</li>
            <li>✅ 企业反馈积极</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_enter2:
    st.markdown("""
    <div style="background-color: #f0f7fa; padding: 1.5rem; border-radius: 15px; border-left: 5px solid #f3b33d; height: 250px;">
        <h3 style="color: #f3b33d;">🏢 贵州一码进出口有限责任公司</h3>
        <p style="font-size: 1.2rem; margin: 1rem 0;"><strong>合作进展</strong></p>
        <ul>
            <li>✅ 已见面3次</li>
            <li>✅ 正在洽谈实训基地</li>
            <li>✅ 意向明确</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ===== 学生技能 =====
st.markdown("---")
st.markdown("### ✅ 学生已掌握技能")

skill_col1, skill_col2, skill_col3, skill_col4 = st.columns(4)

with skill_col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h1 style="color: #1e5f7a;">🎤</h1>
        <h4>数字人运营</h4>
    </div>
    """, unsafe_allow_html=True)

with skill_col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h1 style="color: #1e5f7a;">🧠</h1>
        <h4>AI工作流配置</h4>
    </div>
    """, unsafe_allow_html=True)

with skill_col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h1 style="color: #1e5f7a;">📊</h1>
        <h4>Excel自动化</h4>
    </div>
    """, unsafe_allow_html=True)

with skill_col4:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h1 style="color: #1e5f7a;">🤖</h1>
        <h4>PRA流程优化</h4>
    </div>
    """, unsafe_allow_html=True)

# ===== 产业价值 =====
st.markdown("---")
st.markdown("### 📊 产业价值")

st.markdown("""
<div style="background: linear-gradient(145deg, #1e5f7a, #2c7a9c); color: white; padding: 2.5rem; border-radius: 20px; text-align: center; margin: 2rem 0;">
    <h1 style="font-size: 4rem; margin: 0;">63.64%</h1>
    <p style="font-size: 1.5rem;">企业想要的本地产业带实战案例</p>
    <h2 style="color: #f3b33d; font-size: 2.5rem;">我们做出来了！</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background-color: #e6f0f5; padding: 2rem; border-radius: 15px;">
    <h4 style="color: #1e5f7a;">📈 项目对产业的价值</h4>
    <ul style="font-size: 1.1rem;">
        <li><strong>降低门槛</strong>：让无IT人员、低预算的小微企业用上数字化工具</li>
        <li><strong>提升效率</strong>：报价效率提升95%，单证错误率降低92%</li>
        <li><strong>培养人才</strong>：培养“懂业务+会用AI”的复合型人才</li>
        <li><strong>服务本地</strong>：聚焦遵义白酒、茶叶等特色产业带</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ===== 产教融合成果 =====
st.markdown("---")
st.markdown("### 🎓 产教融合成果")

results_data = {
    "成果": [
        "已转化为高职院校实战教学案例",
        "学生可独立完成企业数字化配置",
        "企业可零成本试用、低成本采购",
        "形成可复制的“产业+教育”模式"
    ]
}
for result in results_data["成果"]:
    st.markdown(f"- ✅ {result}")
