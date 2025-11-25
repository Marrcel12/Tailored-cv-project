import React from 'react';

function AdvancedOptions({
    showAdvanced,
    onToggle,
    basePrompt,
    onBasePromptChange,
    temperature,
    onTemperatureChange,
}) {
    return (
        <div className="advanced-section">
            <button type="button" className="advanced-toggle" onClick={onToggle}>
                {showAdvanced ? 'Hide Advanced Options' : 'Show Advanced Options'}
            </button>

            {showAdvanced && (
                <div className="advanced-options">
                    <div className="form-group">
                        <label htmlFor="basePrompt">
                            Base System Prompt
                            <span
                                className="tooltip-icon"
                                title="Edit the core instructions for the AI. This replaces the default behavior."
                            >
                                ?
                            </span>
                        </label>
                        <textarea
                            id="basePrompt"
                            value={basePrompt}
                            onChange={(e) => onBasePromptChange(e.target.value)}
                            placeholder="Loading default prompt..."
                            rows="10"
                            style={{ fontFamily: 'monospace', fontSize: '0.9rem' }}
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="temperature">
                            Creativity Level (Temperature): {temperature}
                            <span
                                className="tooltip-icon"
                                title="Controls how creative the AI is. Lower values (0.0) make it more focused and deterministic. Higher values (1.0) make it more creative and varied."
                            >
                                ?
                            </span>
                        </label>
                        <input
                            type="range"
                            id="temperature"
                            min="0"
                            max="1"
                            step="0.1"
                            value={temperature}
                            onChange={(e) => onTemperatureChange(parseFloat(e.target.value))}
                            className="range-slider"
                        />
                        <div className="range-labels">
                            <span>Precise</span>
                            <span>Balanced</span>
                            <span>Creative</span>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

export default AdvancedOptions;
