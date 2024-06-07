import crewai
from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer

## tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in Health'})
print(result)