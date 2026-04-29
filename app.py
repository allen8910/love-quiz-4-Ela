import streamlit as st

# --- CONFIGURATION ---
st.set_page_config(page_title="Love Trivia for Ela", page_icon="💖")

# --- 10 ROMANTIC QUESTIONS ---
# Customize the 'answer' field to match the correct letter for your relationship!
quiz_data = [
    {"q": "Where was our very first date?", "options": ["A) Coffee Shop", "B) The Park", "C) Cinema", "D) A Restaurant"], "correct": "A"},
    {"q": "What is my favorite physical feature of yours?", "options": ["A) Your Smile", "B) Your Eyes", "C) Your Hair", "D) Your Hands"], "correct": "B"},
    {"q": "Where we have kissed for the time first?", "options": ["A) Karkardooma", "B) Nirman Vihar", "C) Laxmi Nagar", "D) Random Metro station"], "correct": "A"},
    {"q": "Where did I touch you first?", "options": ["A) Neck", "B) Waist", "C) Face", "D) Shoulder"], "correct": "B"},
    {"q": "What I have did first at our first time, You know What I mean Ela?", "options": ["A) Kiss", "B) Undress", "C) Grab you on bed", "D) Hug"], "correct": "C"},
    {"q": "What was the first movie we watched together?", "options": ["A) Laila Majnu", "B) Rockstar", "C) Satyaprem ki Katha", "D) Animal"], "correct": "C"},
    {"q": "What is my favorite nickname for you?", "options": ["A) Babu", "B) Elu", "C) Chotu", "D) Shanty"], "correct": "D"},
    {"q": "My favourite habit of yours?", "options": ["A) None", "B) Politeness", "C) Shyness", "D) Kindness"], "correct": "B"},
    {"q": "What is the one thing that always makes me laugh?", "options": ["A) Your childness", "B) Your bigggg smileeee", "C) Your facial expressions", "D) All of the above"], "correct": "D"},
    {"q": "If I could describe our love in one word, what would it be?", "options": ["A) Magical", "...B) Eternal", "C) Chaotic (in a good way)", "D) Perfect"], "correct": "B"}
]

# --- SESSION STATE ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'finished' not in st.session_state:
    st.session_state.finished = False

# --- UI INTERFACE ---
st.title("🏹 The Ultimate Love Quiz for Ela")
st.markdown(f"### 💋 Kisses Earned: **{st.session_state.score}**")
st.progress(st.session_state.current_step / len(quiz_data))

if not st.session_state.finished:
    item = quiz_data[st.session_state.current_step]
    
    st.write(f"#### Question {st.session_state.current_step + 1}:")
    st.info(item["q"])

    # Create 4 buttons for A, B, C, D
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(item["options"][0]): # Option A
            check_ans = "A"
        if st.button(item["options"][1]): # Option B
            check_ans = "B"
    with col2:
        if st.button(item["options"][2]): # Option C
            check_ans = "C"
        if st.button(item["options"][3]): # Option D
            check_ans = "D"
            
    # Logic when a button is clicked
    if 'check_ans' in locals():
        if check_ans == item["correct"]:
            st.session_state.score += 1
            st.balloons()
            st.toast("Correct! Sending a kiss... 😘")
        else:
            st.error(f"Wrong! The correct answer was {item['correct']}")

        # Move to next question or finish
        if st.session_state.current_step < len(quiz_data) - 1:
            st.session_state.current_step += 1
            st.rerun()
        else:
            st.session_state.finished = True
            st.rerun()

else:
    st.header("🎉 You Finished the Quiz!")
    st.success(f"You earned a total of **{st.session_state.score} Kisses**! 💋")
    st.write("I'm waiting to deliver them in person. ❤️")
    
    if st.button("Play Again?"):
        st.session_state.score = 0
        st.session_state.current_step = 0
        st.session_state.finished = False
        st.rerun()
