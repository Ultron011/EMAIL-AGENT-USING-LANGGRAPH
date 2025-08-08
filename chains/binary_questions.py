from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')

binary_question_model = ChatGroq(model="llama-3.3-70b-versatile")

class BinaryAnswer(BaseModel):
    if_true: bool = Field(
        description="Whether the answer to the question is yes or no. True if yes otherwise False."
    )

binary_question_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
        """ Answer this question as True for "yes" and False for "no".
            No Other answers are allowed:
            
            {question}
        """
        )
    ]
)

BINARY_QUESTION_CHAIN = (
    binary_question_prompt
    | binary_question_model.with_structured_output(BinaryAnswer)
)
