import streamlit as st
import pandas as pd
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="极速出海 | 2026世校赛参赛项目",
    page_icon="🚢",
    layout="wide"
)

# 自定义CSS（保持原有风格，增加新元素）
st.markdown("""
<style>
    .main-header {
        font-size: 3.2rem;
        font-weight: 700;
        color: #1e5f7a;
        text-align: center;
        margin-bottom: 0.3rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.05);
    }
    .sub-header {
        font-size: 1.6rem;
        color: #f3b33d;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    .slogan {
        font-size: 2rem;
        font-weight: 600;
        text-align: center;
        color: #0a3142;
        background: linear-gradient(90deg, #e6f0f5, #ffffff);
        padding: 1rem 2rem;
        border-radius: 60px;
        margin: 1.5rem auto;
        width: fit-content;
        border: 1px solid #cde0e7;
        box-shadow: 0 4px 8px rgba(0,0,0,0.03);
    }
    .stat-card {
        background-color: #f8fbfd;
        border-left: 5px solid #1e5f7a;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    .stat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.05);
    }
    .badge {
        background-color: #1e5f7a;
        color: white;
        padding: 0.2rem 1rem;
        border-radius: 30px;
        font-size: 0.8rem;
        display: inline-block;
        margin-right: 0.5rem;
    }
    .quote-block {
        background-color: #f9f2e5;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #f3b33d;
        font-style: italic;
        margin: 1.5rem 0;
    }
    .score-pill {
        display: inline-block;
        background-color: #e6f0f5;
        color: #1e5f7a;
        padding: 0.3rem 1rem;
        border-radius: 30px;
        font-size: 0.9rem;
        font-weight: 600;
        margin: 0.2rem;
        border: 1px solid #c0d5df;
    }
    .footer-note {
        text-align: center;
        color: #7a8e99;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #e0eef5;
    }
</style>
""", unsafe_allow_html=True)

# ===== 头部 =====
st.markdown('<div class="main-header">🚢 极速出海</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">-AI赋能的报价履约协同助手</div>', unsafe_allow_html=True)

# 口号
st.markdown('<div class="slogan">2026世校赛备赛情况汇报</div>', unsafe_allow_html=True)

# 汇报人信息
col_logo, col_title, col_logo2 = st.columns([1, 2, 1])
with col_title:
    st.markdown("""
    <div style="text-align: center; background: linear-gradient(145deg, #f0f7fa, #ffffff); padding: 0.8rem; border-radius: 50px; margin: 0.5rem 0 2rem 0; border: 1px solid #cde0e7;">
        <span style="font-weight: 600; color: #1e5f7a;">汇报人：郑秀英</span> 
        <span style="color: #666;"> | 指导老师</span>
        <span style="color: #999; font-size: 0.9rem; margin-left: 15px;"> | 基础科学系</span>
    </div>
    """, unsafe_allow_html=True)

# ===== 方案对标展示区（新增）=====
st.markdown("## 📋 与2026世校赛方案深度对标")

# 创建指标卡片
col_s1, col_s2, col_s3, col_s4, col_s5 = st.columns(5)

with col_s1:
    st.markdown("""
    <div style="background-color: #e6f0f5; padding: 0.8rem; border-radius: 10px; text-align: center; height: 100%;">
        <span style="font-size: 1.8rem;">🔧</span>
        <h4 style="color: #1e5f7a; margin: 0.3rem 0;">技能水平</h4>
        <p style="font-size: 0.8rem;">数字人+Coze+报价+RPA<br>四项硬技能全覆盖</p>
    </div>
    """, unsafe_allow_html=True)

with col_s2:
    st.markdown("""
    <div style="background-color: #e6f0f5; padding: 0.8rem; border-radius: 10px; text-align: center; height: 100%;">
        <span style="font-size: 1.8rem;">👥</span>
        <h4 style="color: #1e5f7a; margin: 0.3rem 0;">团队合作</h4>
        <p style="font-size: 0.8rem;">四人分工无缝衔接<br>营销+运营+技术+单证</p>
    </div>
    """, unsafe_allow_html=True)

with col_s3:
    st.markdown("""
    <div style="background-color: #e6f0f5; padding: 0.8rem; border-radius: 10px; text-align: center; height: 100%;">
        <span style="font-size: 1.8rem;">💡</span>
        <h4 style="color: #1e5f7a; margin: 0.3rem 0;">应用价值</h4>
        <p style="font-size: 0.8rem;">40%报价快进到2分钟<br>26%错误率降至2%</p>
    </div>
    """, unsafe_allow_html=True)

with col_s4:
    st.markdown("""
    <div style="background-color: #e6f0f5; padding: 0.8rem; border-radius: 10px; text-align: center; height: 100%;">
        <span style="font-size: 1.8rem;">✨</span>
        <h4 style="color: #1e5f7a; margin: 0.3rem 0;">创新创意</h4>
        <p style="font-size: 0.8rem;">AI+数字化融合<br>大模型辅助开发</p>
    </div>
    """, unsafe_allow_html=True)

with col_s5:
    st.markdown("""
    <div style="background-color: #e6f0f5; padding: 0.8rem; border-radius: 10px; text-align: center; height: 100%;">
        <span style="font-size: 1.8rem;">📋</span>
        <h4 style="color: #1e5f7a; margin: 0.3rem 0;">职业素养</h4>
        <p style="font-size: 0.8rem;">规范操作+安全意识<br>6S管理贯穿全程</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== 导航提示 =====
st.markdown("---")
st.markdown("### 👈 请从左侧边栏选择页面，深入了解我们的备赛实力")

nav_info = pd.DataFrame({
    "页面": ["01_痛点与数据", "02_技术架构", "03_技能展示", "04_团队与备赛", "05_产教融合"],
    "核心内容": ["调研数据+三组数字", "AI+数字化融合+四大模块详解", "四项技能实操演示+代码", "团队分工+指导教师实力+备赛方案", "企业合作+学生实习+产业价值"],
    "对应评分点": ["真问题", "创新创意", "技能水平", "团队合作", "应用价值"]
})
st.dataframe(nav_info, use_container_width=True, hide_index=True)

# ===== 页脚 =====
st.markdown("""
<div class="footer-note">
    ⚡ | 完全符合2026世校赛方案要求 | 五项评分要素全覆盖<br>
    汇报人：郑秀英 | 基础科学系 | 2026年3月
</div>
""", unsafe_allow_html=True)
