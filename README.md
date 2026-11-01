# Ai-Blog-Generator
# 🚀 AI-Powered Blog Generator

An intelligent, multi-agent blog generation platform built using **Streamlit**, **LangGraph**, **Tavily AI Search**, and **Google Gemini (or OpenAI)**. This application automates the end-to-end content creation lifecycle—from real-time web research and fact-checking to structured drafting and markdown refinement.

---

## 🌟 Key Features

* **Multi-Agent Orchestration:** Powered by LangGraph, coordinating specialized nodes for research, outline generation, writing, and review.
* **Real-Time Web Grounding:** Leverages the Tavily Search API to fetch up-to-date information, news, and technical references beyond model training cutoffs.
* **Dynamic LLM Backend:** Compatible with high-efficiency models like Google Gemini Flash and OpenAI GPT-4o-mini.
* **Interactive Streamlit UI:** Clean, responsive, and user-friendly frontend allowing real-time streaming of generation steps and final blog previews.
* **Production-Ready Architecture:** Easily configurable for cloud deployment using environment variables and Streamlit Cloud secrets management.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Orchestration & Logic:** [LangChain](https://www.langchain.com/) & [LangGraph](https://www.langchain.com/langgraph)
* **Search & Retrieval:** [Tavily AI](https://tavily.com/)
* **Large Language Models:** Google Gemini (`gemini-2.5-flash`) / OpenAI
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```text
ai-blog-generator/
│
├── bwa_backend.py      # LangGraph workflow, nodes, and state management
├── bwa_frontend.py     # Streamlit user interface and execution stream
├── tavily_test.py      # Integration test script for Tavily Search API
├── requirements.txt    # Python dependencies
├── .env                # Local environment variables (not tracked in Git)
├── .gitignore          # Git ignore file
└── README.md           # Project documentation
