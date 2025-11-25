import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';

function App() {
    const [jobLink, setJobLink] = useState('');
    const [cvFile, setCvFile] = useState(null);
    const [profilePic, setProfilePic] = useState(null);
    const [templateId, setTemplateId] = useState('modern');
    const [generatedCv, setGeneratedCv] = useState('');
    const [explanation, setExplanation] = useState('');
    const [pdfBase64, setPdfBase64] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleFileChange = (e) => {
        if (e.target.files) {
            setCvFile(e.target.files[0]);
        }
    };

    const handleProfilePicChange = (e) => {
        if (e.target.files) {
            setProfilePic(e.target.files[0]);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        setGeneratedCv('');
        setExplanation('');
        setPdfBase64('');

        if (!jobLink || !cvFile) {
            setError('Please provide both a job link and a CV file.');
            setLoading(false);
            return;
        }

        const formData = new FormData();
        formData.append('jobLink', jobLink);
        formData.append('cvFile', cvFile);
        formData.append('templateId', templateId);
        if (profilePic) {
            formData.append('profilePic', profilePic);
        }

        try {
            const response = await axios.post('http://localhost:5000/api/generate-cv', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            // The backend now returns structured data, but we might still want to show a simple preview
            // For now, let's assume the backend returns a 'preview' string or we just show the explanation
            setGeneratedCv(response.data.generatedCv || "CV Generated Successfully! Download the PDF to view.");
            setExplanation(response.data.explanation);
            setPdfBase64(response.data.pdfBase64);
        } catch (err) {
            console.error(err);
            setError(err.response?.data?.error || 'An error occurred while generating the CV.');
        } finally {
            setLoading(false);
        }
    };

    const handleDownloadPdf = () => {
        if (!pdfBase64) return;

        const link = document.createElement('a');
        link.href = `data:application/pdf;base64,${pdfBase64}`;
        link.download = 'tailored_cv.pdf';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        <div className="app-container">
            <header className="app-header">
                <h1>AI CV Generator</h1>
                <p>Tailor your CV to any job offer in seconds.</p>
            </header>

            <main className="main-content">
                <section className="input-section">
                    <form onSubmit={handleSubmit} className="cv-form">
                        <div className="form-group">
                            <label htmlFor="jobLink">Job Offer Link</label>
                            <input
                                type="url"
                                id="jobLink"
                                placeholder="https://example.com/job-offer"
                                value={jobLink}
                                onChange={(e) => setJobLink(e.target.value)}
                                required
                            />
                        </div>

                        <div className="form-group">
                            <label htmlFor="cvFile">Your Current CV (PDF or TXT)</label>
                            <div className="file-input-wrapper">
                                <input
                                    type="file"
                                    id="cvFile"
                                    accept=".pdf,.txt"
                                    onChange={handleFileChange}
                                    required
                                />
                                <span className="file-name">{cvFile ? cvFile.name : 'Choose file...'}</span>
                            </div>
                        </div>

                        <div className="form-group">
                            <label htmlFor="profilePic">Profile Picture (Optional)</label>
                            <div className="file-input-wrapper">
                                <input
                                    type="file"
                                    id="profilePic"
                                    accept="image/*"
                                    onChange={handleProfilePicChange}
                                />
                                <span className="file-name">{profilePic ? profilePic.name : 'Choose image...'}</span>
                            </div>
                        </div>

                        <div className="form-group">
                            <label>Select Template</label>
                            <div className="template-grid">
                                {[
                                    { id: 'modern', name: 'Modern', img: '/templates/modern.png' },
                                    { id: 'classic', name: 'Classic', img: '/templates/classic.png' },
                                    { id: 'creative', name: 'Creative', img: '/templates/creative.png' },
                                    { id: 'professional', name: 'Professional', img: '/templates/professional.png' },
                                    { id: 'elegant', name: 'Elegant', img: '/templates/elegant.png' },
                                ].map((t) => (
                                    <div
                                        key={t.id}
                                        className={`template-card ${templateId === t.id ? 'selected' : ''}`}
                                        onClick={() => setTemplateId(t.id)}
                                    >
                                        <img src={t.img} alt={t.name} className="template-preview" />
                                        <div className="template-name">{t.name}</div>
                                    </div>
                                ))}
                            </div>
                        </div>

                        <button type="submit" className="generate-btn" disabled={loading}>
                            {loading ? 'Generating...' : 'Generate Tailored CV'}
                        </button>

                        {error && <div className="error-message">{error}</div>}
                    </form>
                </section>

                {generatedCv && (
                    <section className="result-section">
                        <div className="result-header">
                            <h2>Your Tailored CV</h2>
                            {pdfBase64 && (
                                <button onClick={handleDownloadPdf} className="download-btn">
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
                )}
            </main>
        </div>
    );
}

export default App;
