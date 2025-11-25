import React from 'react';
import ReactMarkdown from 'react-markdown';

function ResultDisplay({ generatedCv, explanation, pdfBase64, onDownload }) {
    if (!generatedCv) {
        return null;
    }

    return (
        <section className="result-section">
            <div className="result-header">
                <h2>Your Tailored CV</h2>
                {pdfBase64 && (
                    <button onClick={onDownload} className="download-btn">
                        Download PDF
                    </button>
                )}
            </div>

            {explanation && (
                <div className="explanation-box">
                    <h3>AI Explanation</h3>
                    <p>{explanation}</p>
                </div>
            )}

            <div className="cv-preview">
                <ReactMarkdown>{generatedCv}</ReactMarkdown>
            </div>
        </section>
    );
}

export default ResultDisplay;
