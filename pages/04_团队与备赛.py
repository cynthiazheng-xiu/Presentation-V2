import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="团队与备赛 | 极速出海", page_icon="👥")

st.title("👥 04 团队与备赛：打造金牌参赛团队")

st.markdown("""
<div class="quote-block" style="background-color: #f0f7fa; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #1e5f7a; margin-bottom: 2rem;">
    <strong>评分要素：团队合作</strong> — 按团队成员分工，同步进行技能操作和现场讲解。
    <div style="text-align: right; margin-top: 0.5rem;">—— 《2026年世界职业院校技能大赛实施方案》第4页</div>
</div>
""", unsafe_allow_html=True)

# ===== 团队分工 =====
st.markdown("### 👥 团队分工：四人各司其职")

col_t1, col_t2, col_t3, col_t4 = st.columns(4)

with col_t1:
    st.markdown("""
    <div style="background-color: #1e5f7a; color: white; padding: 1rem; border-radius: 10px; text-align: center; height: 180px;">
        <h3 style="color: #f3b33d; margin-top: 0;">👨‍💼 队长</h3>
        <h4 style="margin: 0.5rem 0;">XXX</h4>
        <p>整体把控<br>开场结尾<br>时间管理</p>
    </div>
    """, unsafe_allow_html=True)

with col_t2:
    st.markdown("""
    <div style="background-color: #1e5f7a; color: white; padding: 1rem; border-radius: 10px; text-align: center; height: 180px;">
        <h3 style="color: #f3b33d; margin-top: 0;">🎤 营销专员</h3>
        <h4 style="margin: 0.5rem 0;">XXX</h4>
        <p>数字人直播<br>话术设计<br>直播演示</p>
    </div>
    """, unsafe_allow_html=True)

with col_t3:
    st.markdown("""
    <div style="background-color: #1e5f7a; color: white; padding: 1rem; border-radius: 10px; text-align: center; height: 180px;">
        <h3 style="color: #f3b33d; margin-top: 0;">🧠 运营专员</h3>
        <h4 style="margin: 0.5rem 0;">XXX</h4>
        <p>Coze工作流<br>流程搭建<br>业务逻辑</p>
    </div>
    """, unsafe_allow_html=True)

with col_t4:
    st.markdown("""
    <div style="background-color: #1e5f7a; color: white; padding: 1rem; border-radius: 10px; text-align: center; height: 180px;">
        <h3 style="color: #f3b33d; margin-top: 0;">🔧 技术专员</h3>
        <h4 style="margin: 0.5rem 0;">XXX</h4>
        <p>报价系统+PRA<br>代码调试<br>自动化演示</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin: 1.5rem 0;">
    <span class="score-pill">✅ 四人分工明确，可无缝衔接演示</span>
    <span class="score-pill">✅ 每人主讲自己模块，边操作边讲解</span>
    <span class="score-pill">✅ 角色互换训练，确保团队无短板</span>
</div>
""", unsafe_allow_html=True)

# ===== 指导教师实力 =====
st.markdown("---")
st.markdown("### 👩‍🏫 指导教师：郑秀英")

col_teacher1, col_teacher2 = st.columns([1, 2])

with col_teacher1:
    st.markdown("""
    <div style="background-color: #1e5f7a; width: 150px; height: 150px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
        <span style="color: white; font-size: 60px; font-weight: bold;">郑</span>
    </div>
    """, unsafe_allow_html=True)

with col_teacher2:
    st.markdown("""
    **郑秀英** 讲师 | 贵州航天职业技术学院基础科学系  
    
    **专业背景**：四川大学国际贸易专业经济学学士  
    
    **行业经验**：10+年知名企业实战经验（深圳鸿富锦、上海惠普、安永全球商务服务等），曾任采购主管、项目主管
    """)

st.markdown("#### 🏆 省教育厅获奖（近三年）")

honors_data = pd.DataFrame({
    "年份": ["2023", "2021", "2025", "2024", "2023", "2025"],
    "赛项": [
        "贵州省职业院校技能大赛高职组‘跨境电子商务’",
        "贵州省职业院校技能大赛高职组‘英语口语’",
        "中国国际大学生创新大赛贵州省省赛",
        "贵州省职业院校技能大赛‘互联网+国际经济与贸易’",
        "贵州省职业院校技能大赛‘互联网+国际贸易综合技能’",
        "贵州省职业院校技能大赛‘互联网+国际经济与贸易’"
    ],
    "等级": ["一等奖", "一等奖", "银奖", "二等奖", "二等奖", "二等奖"]
})
st.dataframe(honors_data, use_container_width=True, hide_index=True)

st.info("🏆 **指导教师战绩**：近三年累计获得贵州省教育厅颁发的省级技能大赛奖项6项，其中一等奖2项，二等奖4项。累计指导学生获省级以上奖项20余项，多次荣获学院“优秀教师”称号（2021、2022、2024）。")

# ===== 备赛方案 =====
st.markdown("---")
st.markdown("### 📅 三阶段备赛冲刺计划")

col_phase1, col_phase2, col_phase3 = st.columns(3)

with col_phase1:
    st.markdown("""
    <div style="background-color: #e6f0f5; padding: 1rem; border-radius: 10px; height: 200px;">
        <h4 style="color: #1e5f7a;">📌 第一阶段</h4>
        <p><strong>寒假-3月底</strong></p>
        <p>技能专项训练<br>每人主攻1-2个模块<br><strong>产出：</strong>各模块独立可演示</p>
    </div>
    """, unsafe_allow_html=True)

with col_phase2:
    st.markdown("""
    <div style="background-color: #e6f0f5; padding: 1rem; border-radius: 10px; height: 200px;">
        <h4 style="color: #1e5f7a;">📌 第二阶段</h4>
        <p><strong>4月</strong></p>
        <p>模块串联演练<br>话术打磨<br><strong>产出：</strong>联调流程顺畅</p>
    </div>
    """, unsafe_allow_html=True)

with col_phase3:
    st.markdown("""
    <div style="background-color: #e6f0f5; padding: 1rem; border-radius: 10px; height: 200px;">
        <h4 style="color: #1e5f7a;">📌 第三阶段</h4>
        <p><strong>最后2周</strong></p>
        <p>模拟校内选拔<br>应急演练<br><strong>产出：</strong>最终版演示成型</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("#### 🎯 培训方法创新")

col_method1, col_method2, col_method3 = st.columns(3)

with col_method1:
    st.markdown("""
    <div style="background-color: #f0f7fa; padding: 1rem; border-radius: 10px; text-align: center;">
        <h3 style="color: #1e5f7a;">🤖</h3>
        <h4>大模型辅助学习</h4>
        <p>用AI辅助编程和问题排查，培养“会用AI解决问题”的能力</p>
    </div>
    """, unsafe_allow_html=True)

with col_method2:
    st.markdown("""
    <div style="background-color: #f0f7fa; padding: 1rem; border-radius: 10px; text-align: center;">
        <h3 style="color: #1e5f7a;">🔄</h3>
        <h4>角色互换</h4>
        <p>每人轮流主讲不同模块，确保团队无短板、能补位</p>
    </div>
    """, unsafe_allow_html=True)

with col_method3:
    st.markdown("""
    <div style="background-color: #f0f7fa; padding: 1rem; border-radius: 10px; text-align: center;">
        <h3 style="color: #1e5f7a;">🎥</h3>
        <h4>录像复盘</h4>
        <p>演练录像，集体回看，抠细节、优化话术</p>
    </div>
    """, unsafe_allow_html=True)

# ===== 风险预案 =====
st.markdown("---")
st.markdown("### ⚠️ 风险预案")

risk_data = pd.DataFrame({
    "风险": ["网络中断", "软件报错", "学生超时"],
    "预案": [
        "所有演示文件本地化，Coze提前录屏备用",
        "两套方案（Excel版+Python版+Web版+本地部署）",
        "严格控时训练，队长手卡计时"
    ]
})
st.dataframe(risk_data, use_container_width=True, hide_index=True)
