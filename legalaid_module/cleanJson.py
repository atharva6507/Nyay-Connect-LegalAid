from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import json

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="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",
    temperature=0,
)

import json
import re
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="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",
    temperature=0,
)

def cleanjson(input):
    jsonstr = json.dumps(input)
    prompt = PromptTemplate.from_template(
        """
        You are a JSON formatter. Given a JSON string, return only the properly formatted JSON.
        Do not include any explanations, comments, or additional text.
        Return **only** valid JSON.
        ### Input:
        {jsonstr}
        
        ### Output:
        """
    )

    chain = prompt | llm
    response = chain.invoke(jsonstr)

    # Extract the response text
    cleaned_json_str = response.content if hasattr(response, "content") else str(response)

    # Debugging: Print raw AI response
    print("AI Response:", cleaned_json_str)

    # Extract only the JSON part using regex
    match = re.search(r"\{.*\}", cleaned_json_str, re.DOTALL)
    if match:
        cleaned_json_str = match.group(0)
    else:
        raise ValueError("AI did not return valid JSON.")

    return json.loads(cleaned_json_str)