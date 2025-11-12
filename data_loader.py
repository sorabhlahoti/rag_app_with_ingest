#use ollama and enmbedding geems to embed the document
#take the file path and parse teh document
#split in chunks
#use embedding to generate embedding
#push to qdrant storage


import ollama
from llama_index.core.node_parser import SentenceSplitter
from llama_index.readers.file import PDFReader
from dotenv import load_dotenv


EMBED_MODEL="embeddinggemma"
EMBED_DIM=768

splitter=SentenceSplitter(chunk_size=1000,chunk_overlap=200)

def load_and_chunk_pdf(path:str):
  docs=PDFReader().load_data(file=path)
  print(docs)
  texts=[d.text for d in docs if getattr(d,"text",None)]
  
  chunks=[]
  
  for t in texts:
    chunks.extend(splitter.split_text(t))
  return chunks

def embed_texts(texts:list[str])->list[list[float]]:
  response=ollama.embed(
  model='embeddinggemma',
  input=texts)
  
  return [item for item in response['embeddings']]



