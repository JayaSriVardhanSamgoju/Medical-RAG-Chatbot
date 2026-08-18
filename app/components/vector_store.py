from langchain_community.vectorstores import FAISS
import os 
from app.components.embeddings import get_embeddings_models

from app.common.logger import get_logger 
from app.common.custom_exception import CustomException 
from app.config.config import DB_FAISS_PATH

logger=get_logger(__name__)

# we need to write this to load the existing vector store 

def load_vector_store():
    try:
        embedding_model=get_embeddings_models()

        if os.path.exists(DB_FAISS_PATH):
            logger.info("loading existing Vector Store from {} ".format(DB_FAISS_PATH))
            return FAISS.load_local(
                DB_FAISS_PATH,
                embedding_model,
                allow_dangerous_deserialization=True
            )
        else:
            logger.warning("No vector store found ")
    except Exception as e:
        error_message=CustomException("Error loading vector store ",e)
        logger.error(str(error_message))
        raise error_message



# now i need to write  a method to create a new vector store
def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No chunks were found ")
        
        logger.info("Generating a new vector store ")
        embedding_model=get_embeddings_models()
        db=FAISS.from_documents(text_chunks,embedding_model)
        logger.info("Saving Vector store ")
        db.save_local(DB_FAISS_PATH)

        logger.info("Vectorstore saved successfully ")
        return db

    except Exception as e:
        error_message=CustomException("Failed to save the vectorstore",e)
        logger.error(str(error_message))
        raise error_message     