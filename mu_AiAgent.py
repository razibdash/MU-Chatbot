import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import Tool
from langchain.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END

load_dotenv()

# === SETUP LLM ===
llm = ChatGroq(
    temperature=0.3,
    model="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

# === TAVILY TOOL ===
tavily = TavilySearchAPIWrapper()

@tool
def web_search_tool(query: str) -> str:
    """Searches the web using Tavily"""
    results = tavily.results(query)
    return results

# === AGENT MEMORY STATE ===
from typing import TypedDict, Annotated

class AgentState(TypedDict):
    question: str
    search_results: str
    final_answer: str

# === SEARCH NODE ===
def search_node(state: AgentState):
    print("\n[Search Node]")
    query = state['question']
    result = web_search_tool.invoke(query)
    return {"search_results": result}

# === REASONING NODE ===
def reasoning_node(state: AgentState):
    print("\n[Reasoning Node]")
    prompt = f"""You are MU Chatbot, the official virtual assistant of Metropolitan University Bangladesh.

Your role is to assist students, faculty, and prospective applicants by providing accurate, helpful, and friendly responses about the university. You are informative, respectful, and clear in your answers.

You have access to university information such as:
- Admission process, eligibility, and fees
- Department and course details (like CSE, BBA, English, etc.)
- Faculty members and contact directories
- Class schedules, academic calendar, and exam routines
- Campus facilities (library, labs, cafeteria, etc.)
- Rules, regulations, and grading system
- Student services (IT helpdesk, clubs, events, etc.)

You should respond in a helpful, conversational tone and explain things clearly, even when the user is unfamiliar with the topic.

If you do not know the answer, politely let the user know and recommend contacting the university admin or visiting the official website.

Only respond in English (or Bengali if asked). Keep your responses concise, informative, and tailored to the context of a university environment.


.

    Question: {state['question']}
    Search Results: {state['search_results']}

    Always represent Metropolitan University Bangladesh professionally:"""
    response = llm.invoke(prompt)
    return {"final_answer": response.content}

# ✅ Your search_node and reasoning_node should remain as-is

def execute_mu_agent(question: str):
    # Create the graph with the schema
    graph = StateGraph(AgentState)
    graph.add_node("search", search_node)
    graph.add_node("reason", reasoning_node)

    graph.set_entry_point("search")
    graph.add_edge("search", "reason")
    graph.add_edge("reason", END)

    # Compile and run the graph
    chain = graph.compile()
    res = chain.invoke({"question": question})  # 👈 Pass as dict, not just string
    return res['final_answer']

