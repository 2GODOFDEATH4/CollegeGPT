from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def read_doc(directory):
    file_loader = PyPDFDirectoryLoader(directory)
    documents = file_loader.load()
    return documents

pdf_file = './assets/'
document = read_doc(pdf_file)

def chunk_data(docs, chunk_size=1000, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(docs)
    chunks = [i.page_content for i in chunks]
    return chunks

def chunk_json(student_data):
    """
    Function to chunk the student data from the JSON file.
    Each chunk will consist of a student's roll number, name, main section, and sub section.
    """
    chunks = []
    for year_data in student_data:
        year = year_data['year']
        for section in year_data['sections']:
            class_name = section['className']
            branch = section['branch']
            
            for student in section['students']:
                student_chunk = {
                    'chunk_text': f"Roll Number: {student['roll_number']}, Name: {student['name']}, "
                                  f"Main Section: {student['main_section']}, Sub Section: {student['sub_section']}, "
                                  f"Class: {class_name}, Branch: {branch}, Year: {year}",
                    'metadata': {
                        'roll_number': student['roll_number'],
                        'name': student['name'],
                        'main_section': student['main_section'],
                        'sub_section': student['sub_section'],
                        'class_name': class_name,
                        'branch': branch,
                        'year': year
                    }
                }
                chunks.append(student_chunk)
    
    return chunks


