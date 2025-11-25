from pypdf import PdfReader
import io

def parse_cv(file_storage):
    try:
        # Check file extension
        filename = file_storage.filename.lower()
        if filename.endswith('.pdf'):
            # Read PDF
            reader = PdfReader(file_storage)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        elif filename.endswith('.txt'):
            # Read Text
            return file_storage.read().decode('utf-8')
        else:
            # Fallback or error for unsupported types
            print(f"Unsupported file type: {filename}")
            return None
    except Exception as e:
        print(f"Error parsing CV: {e}")
        return None
