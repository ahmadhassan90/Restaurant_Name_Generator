from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key # place your api key here in secret_key.py file
import os
os.environ["OPENAI_API_KEY"] = openapi_key
llm = OpenAI(temperature=0.7)
def generate_restaurantname_and_items(cuisine):
    # for name
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="Suggest me a one name for {cuisine} Food Restaurant",

    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
    # for menu items
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest me a menu items for {restaurant_name}.Return as a Comma Separated String."
    )

    items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menuitems")
    chain = SequentialChain(chains=[name_chain, items_chain],
                            input_variables=["cuisine"],
                            output_variables=["restaurant_name", "menuitems"])

    response =chain({"cuisine": cuisine})

    return response

if __name__=="__main__":
    print(generate_restaurantname_and_items("Italian"))
