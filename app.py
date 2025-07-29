import streamlit as st
from agents.conductor_agent import ConductorAgent
import json
import os
from datetime import datetime

from core.emotion_logger import analyze_emotion
from core.chat_vault import save_to_vault
from utils.web_search import search_web  # Use Gemini instead of DuckDuckGo

import matplotlib.pyplot as plt
from collections import Counter

st.set_page_config(page_title="NeuroNexus", layout="centered")
st.title("🧠 NeuroNexus: Your Cognitive Companion")

st.markdown("Enter a thought, feeling, or question below. Let the agents work their magic!")

# Setup session state to persist data
if "responses" not in st.session_state:
    st.session_state.responses = None
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

input_text = st.text_area("💬 What’s on your mind?", height=150, value=st.session_state.input_text)

# Emojis for tabs
emojis = {
    "Memory": "🧠",
    "Emotion": "❤️",
    "Imagination": "🌌",
    "Planner": "🗓️",
    "Therapy": "🧘",
    "Base": "🪙",
    "Conductor": "🎼",
    "WebSearch": "🌐",
    "Analytics": "📊"
}

# Ask button logic
if st.button("Ask NeuroNexus"):
    if input_text.strip():
        st.session_state.input_text = input_text
        agent = ConductorAgent()
        emotion_info = analyze_emotion(input_text)
        emotion = emotion_info["emotion"]
        st.success(f"🧠 Detected Emotion: **{emotion}**")
        with st.spinner("Agents thinking..."):
            responses = agent.receive(input_text)
        save_to_vault(input_text, responses)

        # Save memory
        memory_log_file = "memory_log.json"
        memory_log = []
        if os.path.exists(memory_log_file):
            with open(memory_log_file, "r") as f:
                memory_log = json.load(f)

        raw_memory = responses.get("Memory", "")
        if raw_memory.startswith("Stored memory:"):
            raw_memory = raw_memory.replace("Stored memory:", "").strip().strip("'\"")

        memory_log.append(raw_memory)
        with open(memory_log_file, "w") as f:
            json.dump(memory_log, f, indent=2)

        st.session_state.responses = responses
    else:
        st.warning("Please enter something first!")

# Render Tabs if Responses Exist
if st.session_state.responses:
    responses = st.session_state.responses
    tab_labels = [f"{emojis.get(name, '🤖')} {name}" for name in list(responses.keys()) + ["WebSearch", "Analytics"]]
    tabs = st.tabs(tab_labels)

    for (agent_name, response), tab in zip(responses.items(), tabs[:len(responses)]):
        with tab:
            st.subheader(f"{emojis.get(agent_name, '🤖')} {agent_name} Agent Response")
            if isinstance(response, (dict, list)):
                st.json(response)
            else:
                st.write(response)

    # 🌐 Web Search Tab
    with tabs[-2]:
        st.subheader("🌐 Web Search")
        web_query = st.text_input("🔎 Enter a search query", key="web_query")
        if st.button("🌍 Search Web"):
            if web_query:
                with st.spinner("Searching the web with Gemini..."):
                    results = search_web(web_query)
                if results:
                    for item in results:
                        st.markdown(f"**{item['title']}**")
                        st.markdown(f"[{item['link']}]({item['link']})")
                        st.caption(item['snippet'])
                        st.markdown("---")
                else:
                    st.info("No results found or API issue.")

    # 📊 Analytics Tab
    with tabs[-1]:
        st.subheader("📊 Analytics & Stats")
        memory_log_file = "memory_log.json"
        if os.path.exists(memory_log_file):
            with open(memory_log_file, "r") as f:
                logs = json.load(f)

            emotion_counts = Counter()
            if "input_text" in st.session_state and st.session_state.input_text:
                emotion_info = analyze_emotion(st.session_state.input_text)
                emotion = emotion_info["emotion"]
                emotion_counts[emotion] += 1

            agent_counts = Counter(responses.keys())

            st.subheader("📈 Agent Usage")
            fig1, ax1 = plt.subplots()
            ax1.bar(agent_counts.keys(), agent_counts.values(), color="#4F8EF7")
            ax1.set_ylabel("Interactions")
            ax1.set_title("Agent Call Frequency")
            ax1.tick_params(axis='x', rotation=30)
            st.pyplot(fig1)

            st.subheader("💖 Emotion Trends")
            fig2, ax2 = plt.subplots()
            ax2.pie(emotion_counts.values(), labels=emotion_counts.keys(), autopct='%1.1f%%', startangle=140)
            ax2.axis('equal')
            st.pyplot(fig2)
        else:
            st.info("No interaction logs yet to analyze.")
