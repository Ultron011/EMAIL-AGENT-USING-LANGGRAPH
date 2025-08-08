from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')

escalation_check_model = ChatGroq(model="llama-3.3-70b-versatile")


class EscalationCheck(BaseModel):
    needs_escalation: bool = Field(
        description="""Whether the notice requires escalation
        according to specified criteria"""
    )

escalation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Determine whether the following notice received
            from a regulatory body requires immediate escalation.
            Immediate escalation is required when {escalation_criteria}.

            Here's the notice message:

            {message}
            """,
        )
    ]
)


ESCALATION_CHECK_CHAIN = (
    escalation_prompt
    | escalation_check_model.with_structured_output(EscalationCheck)
)