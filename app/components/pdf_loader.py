import os 
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException 
from app.config.config import DATA_PATH,CHUNK_SIZE,CHUNK_OVERLAP

logger =get_logger(__name__)

def load_pdf_files(): ## it is useful to load the entire pdfs present in the data folder 
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Data Path Doesn't exists ")
        
        logger.info("Loading the files from {DATA_PATH}")

        loader= DirectoryLoader(DATA_PATH,glob="*.pdf",loader_cls=PyPDFLoader)
        documents=loader.load()

        if not documents:
            logger.warning("No PDFS were found ")
        else:
            logger.info(f"Successfully fetched {len(documents)} documents ")

        return documents 
    except Exception as e:
        error_message=CustomException("Failed to load the pdf ",e)
        logger.error(str(error_message))


## Fetching the contents of the document and chunk it 
def create_text_chunks(documents):
    try:
        if not documents:
            raise CustomException("NO documents are found ")

        logger.info(f"Splitting the {len(documents )} into chunks ")

        text_splitter=RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)

        text_chunks=text_splitter.split_documents(documents)

        logger.info(f"Generated the {len(text_chunks)} text chunks ")

        return text_chunks

    except Exception as e:
        error_message=CustomException("Failed to generate Chunks ",e)
        logger.error(str(error_message))

