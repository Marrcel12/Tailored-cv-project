import os
import json
import base64
import markdown
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from weasyprint import HTML
from services.scraper import scrape_job_offer
from services.cv_parser import parse_cv
from services.ai_generator import generate_tailored_cv
from services.template_renderer import render_template

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/generate-cv', methods=['POST'])
def generate_cv():
    try:
        # 1. Get Job Offer Link
        job_link = request.form.get('jobLink')
        if not job_link:
            return jsonify({'error': 'Job link is required'}), 400

        # 2. Get CV File
        if 'cvFile' not in request.files:
            return jsonify({'error': 'CV file is required'}), 400
        
        cv_file = request.files['cvFile']
        if cv_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Get Template ID (default to 'modern')
        template_id = request.form.get('templateId', 'modern')

        # 3. Scrape Job Offer
        job_description = scrape_job_offer(job_link)
        if not job_description:
             return jsonify({'error': 'Failed to scrape job offer'}), 400

        # 4. Parse CV
        cv_text = parse_cv(cv_file)
        if not cv_text:
             return jsonify({'error': 'Failed to parse CV'}), 400

        # 5. Generate Tailored CV
        ai_response_str = generate_tailored_cv(cv_text, job_description)
        
        try:
            ai_response = json.loads(ai_response_str)
        except json.JSONDecodeError:
            return jsonify({'error': 'Failed to parse AI response'}), 500

        if 'error' in ai_response:
             return jsonify({'error': ai_response['error']}), 500

        # Extract structured data
        summary = ai_response.get('summary', '')
        explanation = ai_response.get('explanation', '')

        # Handle Profile Picture
        profile_pic_base64 = ""
        if 'profilePic' in request.files:
            pic_file = request.files['profilePic']
            if pic_file.filename != '':
                pic_bytes = pic_file.read()
                profile_pic_base64 = base64.b64encode(pic_bytes).decode('utf-8')

        # 6. Generate PDF with Selected Template
        html_template = render_template(ai_response, template_id, profile_pic_base64)
        
        pdf_bytes = HTML(string=html_template).write_pdf()
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')

        return jsonify({
            'generatedCv': summary, # Just return summary for preview
            'explanation': explanation,
            'pdfBase64': pdf_base64
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
