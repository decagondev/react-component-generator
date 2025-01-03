from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

# Define the system prompt for creating React components
system_prompt = """
You are an expert React developer specializing in TypeScript and TailwindCSS.
Your goal is to generate a high-quality, reusable, and well-documented React component
based on the user's input. The component must adhere to the following:

1. Use TypeScript for type safety and include detailed prop types.
2. Use TailwindCSS for styling, following a utility-first approach.
3. Include well-written JSDoc comments for props and any functions.
4. Output the code in a complete and functional format.

Include usage examples as comments in the output. The output should be a complete .tsx file.
"""

# Define the user prompt template
user_prompt_template = PromptTemplate(
    input_variables=["component_name", "purpose", "props", "behavior", "styling", "examples"],
    template="""
Create a React component using TypeScript and styled with TailwindCSS.

- **Component Name**: {component_name}
- **Purpose**: {purpose}
- **Props**: {props}
- **Behavior**: {behavior}
- **Styling**: {styling}
- **Examples**: {examples}
"""
)

llm = ChatOpenAI(temperature=0.5)

def create_component_chain(user_input: dict, output_file: str):
    chain = LLMChain(
        llm=llm,
        prompt=user_prompt_template,
        verbose=True  # For debugging/logging
    )

    generated_code = chain.run(user_input)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(generated_code)
    print(f"Component saved to {output_file}")

def react_component_repl():
    print("Welcome to the React Component Generator!")
    print("Enter the details of the component you'd like to build:")
    
    component_name = input("Component Name: ")
    purpose = input("Purpose: ")
    props = input("Props (describe as a list): ")
    behavior = input("Behavior: ")
    styling = input("Styling (optional): ")
    examples = input("Examples (optional): ")

    user_input = {
        "component_name": component_name,
        "purpose": purpose,
        "props": props,
        "behavior": behavior,
        "styling": styling,
        "examples": examples,
    }

    output_file = f"{component_name}.tsx"
    
    create_component_chain(user_input, output_file)

if __name__ == "__main__":
    react_component_repl()
