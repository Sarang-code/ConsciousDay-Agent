import os # for setting environment variables
from langchain.prompts import PromptTemplate # to define prompt template
from langchain.chains import LLMChain # to run the prompt with the LLM
from langchain_community.chat_models import ChatOpenAI # to use ChatOpenAI-compatible LLMs 

# set together AI API key as an environment variable
os.environ["OPENAI_API_KEY"] = "5f25036107e8c34dd0614700a15f43413e824b417fe1c3a892cae7666430e24e"

# define prompt template for AI agent
prompt_template = """
You are a daily reflection and planning assistant. Your goal is to:
1. Reflect on the user's journal and dream input
2. Interpret the user's emotional and mental state
3. Understand their intention and 3 priorities
4. Generate a practical, energy-aligned strategy for their day

INPUT:
Morning Journal: {journal}
Intention: {intention}
Dream: {dream}
Top 3 Priorities: {priorities}

OUTPUT:
1. Inner Reflection Summary
2. Dream Interpretation Summary
3. Energy/Mindset Insight
4. Suggested Day Strategy (time-aligned tasks)
"""

# function to generate AI reflections
def generate_insight(journal, intention, dream, priorities):

    # Convert string template into a LangChain PromptTemplate
    prompt = PromptTemplate.from_template(prompt_template)

    # Initialize the LLM connection using Together AI via OpenAI
    llm = ChatOpenAI(
        temperature=0.7, # controlls randomness
        openai_api_base="https://api.together.xyz/v1", # point to together AI
        openai_api_key=os.environ["OPENAI_API_KEY"], # use Together API Key
        model="mistralai/Mixtral-8x7B-Instruct-v0.1" # Use Mixtral open-source instruct model
    )

     # Combine the prompt and the model into a reusable chai
    chain = LLMChain(llm=llm, prompt=prompt)

    # Execute the chain with the user input and return the response
    return chain.run({
        "journal": journal,
        "intention": intention,
        "dream": dream,
        "priorities": priorities
    })