import streamlit as st
import random
import time
# from streamlit_autorefresh import st_autorefresh

# Refresh the page every second
# st_autorefresh(interval=1000, key="refresh")

st.title("🎮 Python Quiz Challenge")





if st.button("Start Game"):
    st.session_state.started = True
    st.rerun()

if st.button("Restart"):

    for key in list(st.session_state.keys()):
        del st.session_state[key]

    st.rerun()



# -------------------------
# Number Guessing Game
# -------------------------
if "game_stage" not in st.session_state:
    st.session_state.game_stage = "guess"

if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)

if "attempts" not in st.session_state:
    st.session_state.attempts = 3


# -------------------------
# Stage 1 - Number Guessing Game
# -------------------------
if st.session_state.game_stage == "guess":

    st.header(" Number Guessing Challenge")
    st.write("Guess a number between **1 and 10**.")
    st.write(f"You have **{st.session_state.attempts}** attempts remaining.")

    guess = st.number_input(
        "Enter your guess",
        min_value=1,
        max_value=100,
        step=1,
        key="guess"
    )

    if st.button("Guess Number"):

        if guess == st.session_state.secret_number:
            st.success("🎉 Congratulations! You guessed correctly.")
            st.success("You have unlocked the Quiz Game!")

            st.session_state.game_stage = "quiz"
            st.rerun()

        else:
            st.session_state.attempts -= 1

            if st.session_state.attempts == 0:
                st.error("❌ Game Over!")
                st.write(f"The correct number was **{st.session_state.secret_number}**.")
                st.stop()

            elif guess < st.session_state.secret_number:
                st.warning("⬆️ Too low! Try a higher number.")

            else:
                st.warning("⬇️ Too high! Try a lower number.")

    st.stop()









# Quiz questions
quiz = (
    ("What is the capital of France?", "paris"),
    ("What is 5 + 7?", "12"),
    ("What is the largest planet in our solar system?", "jupiter"),
    ("What programming language are you using?", "python"),
    ("How many days are there in a leap year?", "366")
)

st.title("Python Quiz Game")

# -------------------------
# Initialize session state
# -------------------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "question" not in st.session_state:
    st.session_state.question = random.choice(quiz)

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# Used to create a fresh text box for each question
if "question_id" not in st.session_state:
    st.session_state.question_id = 0

# -------------------------
# Timer
# -------------------------
elapsed = int(time.time() - st.session_state.start_time)
time_left = max(0, 10 - elapsed)

# Automatically load next question after 10 seconds
if elapsed >= 10:
    st.session_state.question = random.choice(quiz)
    st.session_state.start_time = time.time()
    st.session_state.question_id += 1
    st.rerun()

# -------------------------
# Display score and timer
# -------------------------
st.write(f"🏆 Score: {st.session_state.score}")
st.write(f"⏱️ Time Remaining: {time_left} seconds")

# -------------------------
# Display question
# -------------------------
question, answer = st.session_state.question

st.subheader(question)

# Unique key so the input is cleared every new question
input_key = f"answer_{st.session_state.question_id}"

user_answer = st.text_input(
    "Your answer:",
    key=input_key
)

# -------------------------
# Submit Answer
# -------------------------
if st.button("Submit"):

    if user_answer.strip().lower() == answer:
        st.success("✅ Correct!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Incorrect! Correct answer: {answer}")

    # Load another question
    st.session_state.question = random.choice(quiz)
    st.session_state.start_time = time.time()
    st.session_state.question_id += 1

    st.rerun()

# -------------------------
# Exit Game
# -------------------------
if st.button("Exit Game"):
    st.success("🎮 Game Over!")
    st.write(f"## Final Score: {st.session_state.score}")
    st.stop()
