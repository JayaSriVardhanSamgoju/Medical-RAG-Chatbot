from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

from app.components.llm import load_llm
from app.components.vector_store import load_vector_store

from app.config.config import HUGGINGFACE_REPO_ID,HF_TOKEN
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os 

logger=get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE="""Answer the following medical questions in 2 - 3 lines maximum using only the information provided in the context.
Context :{context}
Question:{question}
Answer:
"""

def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE, input_variables=["context", "question"])

def create_qa_chain():
    try:
        logger.info("Loading vectorstore for context")
        db=load_vector_store()

        if db is None:
            raise CustomException("vector store not present or empty ")

        llm=load_llm(huggingface_repo_id=HUGGINGFACE_REPO_ID,hf_token=HF_TOKEN)

        qa_chain=RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=False,
            chain_type_kwargs={'prompt': set_custom_prompt()}
        )

        logger.info("Successfully created the QA chain")
        return qa_chain
        

    except Exception as e:
        error_message=CustomException("Failed to create the QA chain ",e)
        logger.error(str(error_message))
        raise error_message
            