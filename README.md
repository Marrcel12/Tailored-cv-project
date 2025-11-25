# AI CV Tailoring Generator - be careful it was hardly vibecoded but it works and I check it :)

A powerful web application that uses AI to tailor your CV to specific job offers. It generates professionally styled, ATS-friendly PDFs with support for profile pictures and multiple templates.

## Features

- **AI-Powered Tailoring**: Analyzes your CV and the job description to highlight relevant skills and experience.
- **Job Offer Scraping**: Automatically extracts details from job offer URLs.
- **Multiple Templates**: Choose from 5 professional styles:
  - **Modern**: Clean, two-column layout.
  - **Classic**: Traditional, serif-based design.
  - **Creative**: Bold headers and colorful accents.
  - **Professional**: Minimalist and corporate.
  - **Elegant**: Sophisticated with gold accents.
- **Profile Picture Support**: Upload your photo to personalize your CV.
- **Advanced Control**:
  - **Custom Prompts**: Guide the AI with specific instructions.
  - **Creativity Tuning**: Adjust the "temperature" to control how creative the AI should be.
- **Instant Preview**: See visual examples of templates before generating.
- **Downloadable PDF**: Get a high-quality PDF ready for application.

## Tech Stack

- **Frontend**: React, Vite
- **Backend**: Flask (Python)
- **AI**: OpenAI API (GPT-4o)
- **PDF Generation**: WeasyPrint
- **Containerization**: Docker, Docker Compose

## Prerequisites

- Docker and Docker Compose installed.
- An OpenAI API Key.

## Setup & Running

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd cv-project
    ```

2.  **Configure Environment**:
    Copy the example environment file and add your OpenAI API key.
    ```bash
    cp .env.example .env
    # Open .env and set OPENAI_API_KEY=your_key_here
    ```

3.  **Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```

4.  **Access the App**:
    - Frontend: [http://localhost:5173](http://localhost:5173)
    - Backend API: [http://localhost:5000](http://localhost:5000)

## Usage

1.  Paste the link to the job offer you are applying for.
2.  Upload your current CV (PDF or TXT).
3.  (Optional) Upload a profile picture.
4.  Select a template style.
5.  (Optional) Use "Advanced Options" to customize the AI prompt or creativity level.
6.  Click "Generate Tailored CV".
7.  Review the AI's explanation and download your new CV.

## Development

- **Frontend**: Located in `frontend/`. Runs on port 5173.
- **Backend**: Located in `backend/`. Runs on port 5000.
- **Hot Reload**: Enabled for both services. Changes to source files will automatically update the running application.
