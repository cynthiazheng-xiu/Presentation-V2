st.markdown("---")
st.markdown("### 🧠 AI + 💪 数字化 = 完整方案")

# 使用columns并设置高度自适应
col_ai, col_plus, col_digital = st.columns([2, 1, 2])

with col_ai:
    st.markdown("""
    <div style="background: linear-gradient(145deg, #e1f0f7, #ffffff); padding: 1.5rem; border-radius: 15px; border: 2px solid #1e5f7a; height: 380px; display: flex; flex-direction: column;">
        <h3 style="color: #1e5f7a; text-align: center; margin-top: 0;">🧠 AI模块</h3>
        <div style="flex: 1;">
            <p><strong>🤖 数字人直播</strong></p>
            <ul style="margin-top: -5px;">
                <li><strong>技术</strong>：AI数字人、语音合成、自然语言处理</li>
                <li><strong>功能</strong>：24小时智能获客、多语言互动</li>
                <li><strong>创新点</strong>：替代初级人力，成本200元/月</li>
            </ul>
            <p style="margin-top: 15px;"><strong>🧠 Coze工作流</strong></p>
            <ul style="margin-top: -5px;">
                <li><strong>技术</strong>：智能体+知识库+意图识别</li>
                <li><strong>功能</strong>：询盘自动分类、智能回复生成</li>
                <li><strong>创新点</strong>：0代码搭建，业务人员可配置</li>
            </ul>
        </div>
        <p style="text-align: center; margin-top: auto;"><a href="https://www.coze.cn/work_flow?space_id=7491136436608106536&workflow_id=7610438014247305225&force_stay=1" target="_blank">🔗 点击查看Coze工作流（需登录）</a></p>
    </div>
    """, unsafe_allow_html=True)

with col_plus:
    st.markdown("<h1 style='text-align: center; color: #f3b33d; font-size: 3rem; margin-top: 150px;'>+</h1>", unsafe_allow_html=True)

with col_digital:
    st.markdown("""
    <div style="background: linear-gradient(145deg, #fef9e9, #ffffff); padding: 1.5rem; border-radius: 15px; border: 2px solid #f3b33d; height: 380px; display: flex; flex-direction: column;">
        <h3 style="color: #f3b33d; text-align: center; margin-top: 0;">💪 数字化模块</h3>
        <div style="flex: 1;">
            <p><strong>💰 报价系统</strong></p>
            <ul style="margin-top: -5px;">
                <li><strong>技术</strong>：Excel VBA / Python+Streamlit</li>
                <li><strong>功能</strong>：2分钟极速报价、汇率实时同步</li>
                <li><strong>创新点</strong>：双方案并行，适应不同企业需求</li>
            </ul>
            <p style="margin-top: 15px;"><strong>📄 RPA单证</strong></p>
            <ul style="margin-top: -5px;">
                <li><strong>技术</strong>：Power Automate Desktop</li>
                <li><strong>功能</strong>：3秒自动填单，错误率26%→2%</li>
                <li><strong>创新点</strong>：0成本，单证员可自己录制</li>
            </ul>
        </div>
        <p style="text-align: center; margin-top: auto; visibility: hidden;">占位符</p>
    </div>
    """, unsafe_allow_html=True)
