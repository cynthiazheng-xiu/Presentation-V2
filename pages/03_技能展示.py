import streamlit as st

st.set_page_config(page_title="技能展示 | 极速出海", page_icon="🔧")

st.title("🔧 03 技能展示：四项核心技能实操演示")

st.markdown("""
<div class="quote-block" style="background-color: #f0f7fa; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #1e5f7a; margin-bottom: 2rem;">
    <strong>评分要素：技能水平</strong> — 技能操作重点展示专业技能熟练程度、规范程度以及解决技术难题的创新能力。
    <div style="text-align: right; margin-top: 0.5rem;">—— 《2026年世界职业院校技能大赛实施方案》第4页</div>
</div>
""", unsafe_allow_html=True)

# 选项卡展示四项技能
tabs = st.tabs(["🤖 数字人直播", "🧠 Coze工作流", "💰 报价系统", "📄 RPA单证"])

with tabs[0]:
    st.header("🤖 数字人直播——24小时智能获客")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **操作步骤**：
        1. 平台选择：HeyGen/硅基智能
        2. 形象配置：选择西方商务女性
        3. 语言设置：英语/多语言切换
        4. 话术导入：产品卖点+常见QA
        5. 生成发布：30秒生成直播切片
        
        **技能要点**：
        - ✅ 5分钟内完成配置
        - ✅ 能讲解选品逻辑
        - ✅ 懂直播数据分析
        """)
    with col2:
        st.markdown("""
        **效果对比**：
        
        | 维度 | 人工直播 | 数字人直播 |
        |------|----------|------------|
        | 时长 | 8小时/天 | 24小时/天 |
        | 成本 | 1万/月 | 200元/月 |
        | 转化率 | 2.5% | 10% |
        """)
    
    st.code("""
    # 话术模板示例
    欢迎来到直播间！今天给大家带来的是遵义特色——15年窖藏酱香白酒。
    这款酒曾获巴拿马金奖，口感醇厚，回味悠长。
    现在下单可享受新客优惠，点击下方链接咨询详情！
    """, language="text")

with tabs[1]:
    st.header("🧠 Coze工作流——智能询盘分类")
    
    coze_url = "https://www.coze.cn/work_flow?space_id=7491136436608106536&workflow_id=7613027449315885065&force_stay=1"
    
    st.markdown(f"""
    **工作流节点设计**：
    1. 输入节点：接收客户邮件/询盘
    2. 意图识别：关键词匹配（FOB/CIF/DDP/认证等）
    3. 知识库查询：匹配产品目录、报价规则
    4. 话术生成：根据客户类型生成回复
    5. 输出节点：分类标签+建议话术+回复草稿
    
    **技能要点**：
    - ✅ 15分钟内搭建一个询盘分类智能体
    - ✅ 知识库配置与优化
    - ✅ 工作流调试与测试
    """)
    
    st.markdown(f"""
    <div style="background-color: #f0f7fa; padding: 1rem; border-radius: 10px; text-align: center;">
        <a href="{coze_url}" target="_blank">
            <button style="background-color: #1e5f7a; color: white; padding: 10px 30px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">
                🔗 查看Coze工作流（需登录）
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **测试示例**：
    > 输入："Hi, I'm interested in your baijiu. Please quote CIF Los Angeles price for 200 cases."
    
    **AI输出**：
    - 分类标签：CIF报价询盘
    - 建议话术：建议报含运费保险的价格
    - 效果：人工25分钟 → AI辅助2分钟
    """)

with tabs[2]:
    st.header("💰 报价系统——双方案并行")
    
    option = st.radio("选择版本查看", ["📊 Excel+VBA版", "🐍 Python+Streamlit版"], horizontal=True)
    
    if option == "📊 Excel+VBA版":
        st.markdown("""
        **Excel+VBA改造方案**：
        - 产品下拉菜单（告别手打编号）
        - 汇率自动抓取（不用百度查）
        - 一键生成PDF（自动命名存档）
        
        **技能要点**：
        - ✅ 10分钟内完成Excel改造
        - ✅ VBA代码调试与优化
        - ✅ 理解业务人员使用习惯
        """)
        
        st.code("""
        ' VBA代码示例：汇率自动抓取
        Sub UpdateExchangeRate()
            Dim http As Object
            Set http = CreateObject("MSXML2.XMLHTTP")
            http.Open "GET", "https://api.exchangerate-api.com/v4/latest/USD", False
            http.send
            Dim response As String
            response = http.responseText
            ' 解析JSON获取汇率
            Range("B2").Value = 6.8923 ' 示例值
        End Sub
        """, language="vbnet")
        
    else:
        st.markdown("""
        **Python+Streamlit方案**：
        - 实时计算总价
        - 汇率自动联动
        - 一键导出报价单
        
        **技能要点**：
        - ✅ 10分钟内完成Python演示
        - ✅ 大模型辅助编程
        - ✅ 理解业务需求转化为代码
        """)
        
        # 添加外部链接按钮
        python_demo_url = "https://export-quotation-system-7gwfeahqyaafdp8mnofrjg.streamlit.app/"
        st.markdown(f"""
        <div style="background-color: #e6f0f5; padding: 1.2rem; border-radius: 10px; margin: 1rem 0; text-align: center; border: 1px solid #1e5f7a;">
            <h4 style="color: #1e5f7a; margin-top: 0;">🚀 在线演示</h4>
            <p>点击下方按钮体验完整的Python报价系统：</p>
            <a href="{python_demo_url}" target="_blank">
                <button style="background-color: #1e5f7a; color: white; padding: 12px 35px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; font-weight: bold;">
                    🔗 打开Python报价系统演示
                </button>
            </a>
            <p style="margin-top: 10px; font-size: 0.9rem; color: #666;">在新标签页中打开独立部署的报价系统</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.code("""
        # Streamlit报价系统核心代码
        import streamlit as st
        
        procurement = st.number_input("采购成本", value=1000.0)
        freight = st.number_input("运输成本", value=500.0)
        domestic = st.number_input("国内费用", value=300.0)
        bank = st.number_input("银行费用", value=200.0)
        
        exchange_rate = st.number_input("汇率(USD/CNY)", value=6.8923)
        
        total_cny = procurement + freight + domestic + bank
        total_usd = total_cny / exchange_rate
        
        st.metric("总报价(USD)", f"${total_usd:,.2f}")
        """, language="python")

with tabs[3]:
    st.header("📄 RPA单证——3秒自动填单")
    
    st.markdown("""
    **Power Automate Desktop流程**：
    1. 录制：复制Excel订单号→粘贴到报关系统
    2. 优化：添加等待元素、修改选择器
    3. 变量：使用变量实现动态数据读取
    4. 运行：一键执行，3秒填完20个字段
    
    **技能要点**：
    - ✅ 15分钟内完成录制+运行
    - ✅ 选择器优化与调试
    - ✅ 错误处理机制设计
    - ✅ 错误率控制在2%以内
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("**人工操作**")
        st.markdown("""
        - ⏱️ 耗时：15-20分钟
        - ❌ 错误率：26%
        - 🔄 操作：60次复制粘贴
        """)
    with col2:
        st.success("**RPA机器人**")
        st.markdown("""
        - ⏱️ 耗时：**3秒**
        - ✅ 错误率：**2%**
        - 👆 操作：**1次点击**
        """)

# 技能总结
st.markdown("---")
st.markdown("""
<div style="background-color: #e6f0f5; padding: 1.5rem; border-radius: 10px;">
    <h4 style="color: #1e5f7a;">📊 技能水平总结</h4>
    <table style="width: 100%; border-collapse: collapse;">
        <tr style="background-color: #1e5f7a; color: white;">
            <th style="padding: 10px;">模块</th>
            <th style="padding: 10px;">核心技能</th>
            <th style="padding: 10px;">掌握时间</th>
            <th style="padding: 10px;">熟练度</th>
        </tr>
        <tr style="background-color: #f0f7fa;">
            <td>数字人直播</td>
            <td>平台配置+话术设计</td>
            <td>5分钟</td>
            <td>⭐⭐⭐⭐⭐</td>
        </tr>
        <tr>
            <td>Coze工作流</td>
            <td>智能体搭建+知识库配置</td>
            <td>15分钟</td>
            <td>⭐⭐⭐⭐⭐</td>
        </tr>
        <tr style="background-color: #f0f7fa;">
            <td>报价系统</td>
            <td>VBA编程+Python开发</td>
            <td>10分钟</td>
            <td>⭐⭐⭐⭐</td>
        </tr>
        <tr>
            <td>RPA单证</td>
            <td>流程录制+选择器优化</td>
            <td>15分钟</td>
            <td>⭐⭐⭐⭐⭐</td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)
