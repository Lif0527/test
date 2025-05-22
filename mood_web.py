# mood_web.py
import streamlit as st

st.title("🎮 游戏决策助手")
st.write("---")

# 输入框 + 自动校验数字
mood = st.number_input(
    "输入今日心情指数（0-100）:", 
    min_value=0, 
    max_value=100,
    value=60,
    help="请输入0-100之间的整数"
)

# 动态结果展示
if st.button("点击分析"):
    if mood >= 60:
        st.success(f"### 恭喜！心情指数 {mood} 🎉")
        st.write("**今晚可以打游戏，去吧皮卡丘！**")
        st.write("(๑╹◡╹)ﾉ”")
    else:
        st.error(f"### 警告！心情指数 {mood} ⚠️")
        st.write("**为了小命，建议休息哦~**")
        st.write("(；´д｀)ゞ")