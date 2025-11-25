import os
from openai import OpenAI

def generate_tailored_cv(cv_text, job_description):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")

    client = OpenAI(api_key=api_key)

    prompt = f"""
    You are an expert CV writer. I will provide you with my current CV and a job description.
    Your task is to rewrite my CV to better match the job description, highlighting relevant skills and experiences.
    Do not invent false information, but emphasize the truth in a way that appeals to this specific employer.
    
    Also, provide a brief explanation of the changes you made and why.
    
    JOB DESCRIPTION:
    {job_description}
    
    CURRENT CV:
    {cv_text}
    
    OUTPUT:
    Return a JSON object with the following structure:
    {{
        "personal_info": {{
            "name": "Full Name",
            "email": "Email",
            "phone": "Phone",
            "linkedin": "LinkedIn URL",
            "location": "City, Country"
        }},
        "summary": "Professional summary tailored to the job.",
        "skills": ["Skill 1", "Skill 2", "Skill 3"],
        "experience": [
            {{
                "title": "Job Title",
                "company": "Company Name",
                "dates": "Date Range",
                "description": ["Bullet point 1", "Bullet point 2"]
            }}
        ],
        "education": [
            {{
                "degree": "Degree Name",
                "school": "School Name",
                "dates": "Date Range"
            }}
        ],
        "explanation": "A brief explanation of the changes made and why they improve the CV for this specific job."
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes professional CVs. You always return valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            response_format={ "type": "json_object" }
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating CV: {e}")
        # Return a fallback JSON structure in case of error, or re-raise
        return f'{{"error": "{str(e)}"}}'
