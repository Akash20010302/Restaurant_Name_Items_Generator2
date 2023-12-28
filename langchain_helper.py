from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os
os.environ["OPENAI_API_KEY"] = "PLACE YOUR API KEY"

llm = OpenAI(temperature=0.7)

def generate_restraunt_name_and_items(cuisine):
    # Chain 1
    prompt_template_name = PromptTemplate(
        input_variables = ["cuisine"],
        template = "I want to open a restraunt for {cuisine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restraunt_name")

    # Chain 2: Menu-Items
    prompt_template_name = PromptTemplate(
        input_variables=["restraunt_name"],
        template="Suggest some menu items non-veg and veg separated for {restraunt_name} and dont show duplicate."
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ["cuisine"],
        output_variables = ["restraunt_name", "menu_items"]
    )

    response = chain({"cuisine": cuisine})

    return response

if __name__ == "__main__":
    print(generate_restraunt_name_and_items("Italian"))
