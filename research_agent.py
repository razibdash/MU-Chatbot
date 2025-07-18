from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from crewai import Agent
from crewai_tools import SerperDevTool
from crewai import Task
from crewai import Crew

load_dotenv()

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
os.environ["SERPER_API_KEY"] = SERPER_API_KEY 
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
search_tool = SerperDevTool()
#model 
llm=ChatGroq(
        temperature = 0.7,
        model="llama3-70b-8192",
        api_key= os.getenv("GROQ_API_KEY"),
)


def create_research_agent():
    return Agent(
        role="Research Specialist",
        goal="Conduct thorough research on given topics",
        backstory="You are an experienced researcher with expertise in finding and synthesizing information from various sources",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool],
        llm=llm,
    )

def create_research_task(agent,topic):
    return Task(
        description=f"Research the following topic and provide a comprehensive summary: {topic}",
        agent=agent,
        expected_output = "A detailed summary of the research findings, including key points and insights related to the topic"
    )

def excucute_research_agent(topic):
    agent = create_research_agent()
    task = create_research_task(agent, topic)
    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    return result
