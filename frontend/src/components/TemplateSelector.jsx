import React from 'react';

const TEMPLATES = [
    { id: 'modern', name: 'Modern', img: '/templates/modern.png' },
    { id: 'classic', name: 'Classic', img: '/templates/classic.png' },
    { id: 'creative', name: 'Creative', img: '/templates/creative.png' },
    { id: 'professional', name: 'Professional', img: '/templates/professional.png' },
    { id: 'elegant', name: 'Elegant', img: '/templates/elegant.png' },
];

function TemplateSelector({ selectedTemplate, onTemplateChange }) {
    return (
        <div className="form-group">
            <label>Select Template</label>
            <div className="template-grid">
                {TEMPLATES.map((template) => (
                    <div
                        key={template.id}
                        className={`template-card ${selectedTemplate === template.id ? 'selected' : ''}`}
                        onClick={() => onTemplateChange(template.id)}
                    >
                        <img src={template.img} alt={template.name} className="template-preview" />
                        <div className="template-name">{template.name}</div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default TemplateSelector;
