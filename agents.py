from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode
news_researcher=Agent(
    role="Senior Researcher",
    goal='Uncover cutting-edge technologies in the field of artificial intelligence and machine learning',
    verbose=True,
    memory=True,
    backstory=(
        "With an insatiable thirst for knowledge, you are driven by a relentless curiosity to explore the frontiers of"
        "artificial intelligence and machine learning. You are passionate about uncovering groundbreaking innovations"
        "that have the potential to revolutionize these domains and shape the future of technology."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

## creating a write agent with custom tools responsible in writing news blog
news_writer = Agent(
  role='Writer',
  goal='Craft captivating narratives that bring the latest advancements in artificial intelligence and machine learning to life',
  verbose=True,
  memory=True,
  backstory=(
    "With a gift for storytelling and a knack for breaking down complex concepts into accessible narratives,"
    "you have a talent for captivating audiences and igniting their curiosity. Your mission is to illuminate the"
    "cutting-edge developments in artificial intelligence and machine learning, weaving compelling tales that"
    "inspire wonder and foster a deeper understanding of these transformative technologies."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)