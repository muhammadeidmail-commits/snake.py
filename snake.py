import streamlit as st
import random

st.title("🐍 لعبة الدودة - Snake Game")

# إعداد الحالة البدائية للعبة
if 'snake' not in st.session_state:
    st.session_state.snake = [(10, 10), (10, 11), (10, 12)]
    st.session_state.direction = (0, -1)
    st.session_state.food = (5, 5)
    st.session_state.score = 0

# زر تحريك الدودة
col1, col2, col3 = st.columns(3)
if col1.button("⬅️ يسار"): st.session_state.direction = (0, -1)
if col2.button("⬆️ فوق"): st.session_state.direction = (-1, 0)
if col3.button("⬇️ تحت"): st.session_state.direction = (1, 0)
if col1.button("➡️ يمين"): st.session_state.direction = (0, 1)

# منطق اللعبة البسيط
def update_game():
    head = st.session_state.snake[0]
    new_head = (head[0] + st.session_state.direction[0], head[1] + st.session_state.direction[1])
    st.session_state.snake.insert(0, new_head)
    
    if new_head == st.session_state.food:
        st.session_state.score += 1
        st.session_state.food = (random.randint(0, 19), random.randint(0, 19))
    else:
        st.session_state.snake.pop()

update_game()

# رسم اللعبة
grid = [["⬛" for _ in range(20)] for _ in range(20)]
for segment in st.session_state.snake:
    grid[segment[0]][segment[1]] = "🟩"
grid[st.session_state.food[0]][st.session_state.food[1]] = "🍎"

for row in grid:
    st.text(" ".join(row))

st.write(f"### النقاط: {st.session_state.score}")
