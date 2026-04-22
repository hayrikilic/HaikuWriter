from crewai import Agent, Task, Crew, LLM

#LLM
ollama_llm = LLM(
    model="ollama/llama3.1:8b",
    api_base="http://localhost:11434"
)

#Agents
haiku_topic_finder_agent = Agent (
    role = "Haiku Topic Finder",
    goal = "State the topic of haiku that will be written by haiku writer",
    backstory=(
        "You are an expert on poem, Japanese and English literature." 
        "Your goal is to state topics such as love, nature, life for Haiku Writer who will write their haiku on this topic."
    ),
    llm=ollama_llm,
    allow_delegation = False,
    verbose = True
)

haiku_writer_agent = Agent (
    role = "Haiku Writer",
    goal = "Write beautiful haiku on the topic that is stated by Haiku Topic Finder",
    backstory=(
        "You are an expert on haiku and poem and have a deep knowledge on Japanese literature." 
        "Your goal is to write haiku on the topic which is stated by Haiku Topic Finder"
    ),
    llm=ollama_llm,
    allow_delegation = False,
    verbose = True
)

#Tasks
finding_topic_task = Task(
    description=(
        "Generate randomly one word such as love, nature, life etc. for haiku."
    ),
    expected_output="Randomly generated one word such as love, nature,life etc. ",
    agent=haiku_topic_finder_agent
)

writing_haiku_task = Task(
    description=(
        "Write a short haiku on the topic whichc is stated by Haiku Topic Finder "
    ),
    expected_output="Generate a well written, short Japanese Haiku",
    agent=haiku_writer_agent
)

#Crew
crew = Crew(
    agents=[haiku_topic_finder_agent,haiku_writer_agent],
    tasks=[finding_topic_task, writing_haiku_task],
    verbose = True,
    model="ollama/llama3.1:8b"
)

#Run Crew Kickoff
result = crew.kickoff()

raw_result = result.raw
print(result)