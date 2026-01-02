import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="한화 AI 자산 나침반", layout="wide")

# 사이드바 메뉴
st.sidebar.title("메뉴 탐색")
page = st.sidebar.radio("이동할 화면", ["홈: 자산 날씨", "AI 분석: 변수 분석", "포트폴리오: 리밸런싱", "미래 시뮬레이션"])

# --- Screen 1: [홈] 나의 자산 날씨와 시장 국면 ---
if page == "홈: 자산 날씨":
    st.title("☀️ 나의 자산 날씨와 시장 국면")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 현재 날씨")
        st.header("🌫️ 안개 낀 폭풍우")
        st.caption("고금리-고물가 지속 상태")
        
    with col2:
        st.subheader("김한화님, 오늘 당신의 자산 나침반은")
        st.info("### **'방어적 성장'** 국면을 가리키고 있습니다.")
        st.write("현재 시장은 **[고금리 지속]** 국면입니다. AI가 자산을 보호할 준비를 마쳤습니다.")

# --- Screen 2: [AI 분석] 왜 나침반이 움직였나요? ---
elif page == "AI 분석: 변수 분석":
    st.title("🔍 AI는 왜 그렇게 생각했을까요?")
    st.subheader("AI가 분석한 비중 변경의 결정적 이유 3가지")
    
    # SHAP 시각화용 데이터
    df_shap = pd.DataFrame({
        '변수': ['미국 국채 금리', '환율 변동성', '지정학적 리스크'],
        '영향도(%)': [45, 30, 25],
        '상태': ['상승', '확대', '감지']
    })
    
    fig = px.bar(df_shap, x='영향도(%)', y='변수', orientation='h', 
                 title="변수별 영향도 (SHAP 지수)", text='영향도(%)',
                 color='영향도(%)', color_continuous_scale='Reds')
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("1. **미국 국채 금리 상승 (45%↑):** 금리가 오르면서 안전자산의 매력도가 높아졌습니다.")
    st.write("2. **환율 변동성 확대 (30%↑):** 달러 자산의 비중 조절이 필요한 시점입니다.")
    st.write("3. **지정학적 리스크 (25%↑):** 에너지 관련 자산의 변동성을 감지했습니다.")

# --- Screen 3: [포트폴리오] 한화 맞춤형 리밸런싱 ---
elif page == "포트폴리오: 리밸런싱":
    st.title("⚖️ 맞춤형 리밸런싱")
    
    col1, col2 = st.columns(2)
    
    # 차트 데이터
    labels = ['주식', '채권', '현금']
    before = [60, 30, 10]
    after = [40, 50, 10]
    
    with col1:
        st.write("#### 변경 전 (Before)")
        fig_before = px.pie(values=before, names=labels, hole=0.4)
        st.plotly_chart(fig_before, use_container_width=True)
        
    with col2:
        st.write("#### 변경 후 (After)")
        fig_after = px.pie(values=after, names=labels, hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig_after, use_container_width=True)
        
    st.success("추천 변경안: 주식 60% → 40%, 채권 30% → 50%, 현금 10%")
    
    st.markdown("---")
    st.write("🔗 **연계 상품**")
    st.button("한화 LifePlus TDF 2050")
    st.button("한화 ARIRANG 미국단기채권 ETF")
    
    st.divider()
    btn1, btn2 = st.columns(2)
    with btn1:
        st.button("✅ 설명 이해함 - 포트폴리오 적용하기", use_container_width=True, type="primary")
    with btn2:
        st.button("📞 상담사 연결하기", use_container_width=True)

# --- Screen 4: [미래 시뮬레이션] 내 꿈의 실현 가능성 ---
elif page == "미래 시뮬레이션":
    st.title("📈 내 꿈의 실현 가능성")
    
    # 가상의 성장 곡선 데이터
    years = list(range(2024, 2045))
    growth = [100 * (1.05**i) for i in range(len(years))]
    growth_optimized = [100 * (1.06**i) for i in range(len(years))] # 리밸런싱 시 더 높은 성장률 가정
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=growth, name='현재 유지 시'))
    fig.add_trace(go.Scatter(x=years, y=growth_optimized, name='AI 리밸런싱 적용 시', line=dict(width=4, color='orange')))
    
    fig.update_layout(title='20년 뒤 자산 성장 예측 곡선', xaxis_title='연도', yaxis_title='자산 가치')
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 이 국면 대응을 유지할 경우, **60세 은퇴 자산 목표 달성률이 8% 상승**합니다.")