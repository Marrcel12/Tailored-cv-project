def render_template(data, template_id, profile_pic_base64):
    personal_info = data.get("personal_info", {})
    summary = data.get("summary", "")
    skills = data.get("skills", [])
    experience = data.get("experience", [])
    education = data.get("education", [])

    # Helper to generate list items
    def get_list_items(items):
        return "".join([f"<li>{item}</li>" for item in items])

    skills_html = get_list_items(skills)

    experience_html = ""
    for exp in experience:
        desc_html = get_list_items(exp.get("description", []))
        experience_html += f"""
        <div class="job">
            <h3>{exp.get('title', '')}</h3>
            <div class="company-date">
                <span class="company">{exp.get('company', '')}</span>
                <span class="date">{exp.get('dates', '')}</span>
            </div>
            <ul>{desc_html}</ul>
        </div>
        """

    education_html = ""
    for edu in education:
        education_html += f"""
        <div class="edu">
            <h3>{edu.get('degree', '')}</h3>
            <div class="school-date">
                <span class="school">{edu.get('school', '')}</span>
                <span class="date">{edu.get('dates', '')}</span>
            </div>
        </div>
        """

    profile_img_tag = (
        f'<img src="data:image/jpeg;base64,{profile_pic_base64}" class="profile-pic">'
        if profile_pic_base64
        else ""
    )
    linkedin_div = (
        f'<div><strong>LinkedIn:</strong><br>{personal_info.get("linkedin", "")}</div>'
        if personal_info.get("linkedin")
        else ""
    )

    # --- TEMPLATE STYLES ---

    if template_id == "classic":
        # Classic: Single column, serif font, traditional
        style = """
            @page { margin: 2.5cm; size: A4; }
            body { font-family: 'Times New Roman', serif; color: #000; line-height: 1.4; }
            .header { text-align: center; border-bottom: 1px solid #000; padding-bottom: 20px; margin-bottom: 20px; }
            .name { font-size: 24pt; font-weight: bold; text-transform: uppercase; margin-bottom: 10px; }
            .contact-info { font-size: 10pt; }
            .profile-pic { width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin-bottom: 10px; }

            .section-title { font-size: 14pt; font-weight: bold; border-bottom: 1px solid #000; margin-top: 20px; margin-bottom: 10px; text-transform: uppercase; }
            .job h3, .edu h3 { font-size: 12pt; font-weight: bold; margin: 0; }
            .company-date, .school-date { font-style: italic; margin-bottom: 5px; }
            ul { margin-top: 5px; padding-left: 20px; }
        """
        body_content = f"""
            <div class="header">
                {profile_img_tag}
                <div class="name">{personal_info.get('name', 'Your Name')}</div>
                <div class="contact-info">
                    {personal_info.get('location', '')} | {personal_info.get('phone', '')} | {personal_info.get('email', '')}
                </div>
            </div>

            <div class="section">
                <div class="section-title">Summary</div>
                <p>{summary}</p>
            </div>

            <div class="section">
                <div class="section-title">Experience</div>
                {experience_html}
            </div>

            <div class="section">
                <div class="section-title">Education</div>
                {education_html}
            </div>

            <div class="section">
                <div class="section-title">Skills</div>
                <ul>{skills_html}</ul>
            </div>
        """

    elif template_id == "creative":
        # Creative: Bold header, colorful accents
        style = """
            @page { margin: 0; size: A4; }
            body { font-family: 'Helvetica', sans-serif; margin: 0; color: #333; }
            .header-bg { background-color: #ff6b6b; color: white; padding: 40px; text-align: center; }
            .name { font-size: 32pt; font-weight: bold; margin: 0; }
            .contact-info { margin-top: 10px; font-size: 11pt; }
            .profile-pic { width: 120px; height: 120px; border-radius: 50%; border: 4px solid white; margin-bottom: 15px; }

            .content { padding: 40px; }
            .section-title { color: #ff6b6b; font-size: 16pt; font-weight: bold; text-transform: uppercase; letter-spacing: 2px; margin-top: 30px; margin-bottom: 15px; }
            .job h3, .edu h3 { font-size: 14pt; font-weight: bold; }
            .company-date, .school-date { color: #666; font-weight: bold; margin-bottom: 10px; }
            ul { padding-left: 20px; }
            li { margin-bottom: 5px; }
        """
        body_content = f"""
            <div class="header-bg">
                {profile_img_tag}
                <div class="name">{personal_info.get('name', 'Your Name')}</div>
                <div class="contact-info">
                    {personal_info.get('email', '')} &bull; {personal_info.get('phone', '')} &bull; {personal_info.get('location', '')}
                </div>
            </div>

            <div class="content">
                <div class="section-title">Profile</div>
                <p>{summary}</p>

                <div class="section-title">Experience</div>
                {experience_html}

                <div class="section-title">Education</div>
                {education_html}

                <div class="section-title">Skills</div>
                <ul>{skills_html}</ul>
            </div>
        """

    elif template_id == "professional":
        # Professional: Minimalist, corporate, clean lines, blue/grey accents
        style = """
            @page { margin: 0; size: A4; }
            body { font-family: 'Roboto', 'Arial', sans-serif; margin: 0; color: #333; line-height: 1.5; }
            .header { background-color: #f1f5f9; padding: 40px; border-bottom: 4px solid #0f172a; display: flex; align-items: center; justify-content: space-between; }
            .header-info { flex: 1; }
            .name { font-size: 28pt; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 1px; margin: 0; }
            .contact-info { margin-top: 10px; font-size: 10pt; color: #475569; }
            .profile-pic { width: 100px; height: 100px; border-radius: 5px; object-fit: cover; border: 2px solid #cbd5e1; margin-left: 20px; }

            .content { padding: 40px; display: flex; gap: 40px; }
            .left-col { width: 65%; }
            .right-col { width: 35%; }

            .section-title { font-size: 12pt; font-weight: 700; color: #0f172a; text-transform: uppercase; letter-spacing: 1px; border-bottom: 2px solid #e2e8f0; padding-bottom: 5px; margin-bottom: 15px; margin-top: 20px; }
            .section-title:first-child { margin-top: 0; }

            .job { margin-bottom: 20px; }
            .job h3 { font-size: 11pt; font-weight: 700; color: #334155; margin: 0; }
            .company-date { font-size: 9pt; color: #64748b; margin-bottom: 5px; font-weight: 500; }
            ul { margin: 5px 0 0 0; padding-left: 15px; color: #475569; font-size: 10pt; }
            li { margin-bottom: 3px; }

            .skills-list { list-style: none; padding: 0; }
            .skills-list li { background: #f1f5f9; color: #334155; padding: 5px 10px; margin-bottom: 5px; border-radius: 4px; font-size: 9pt; font-weight: 500; }
        """
        body_content = f"""
            <div class="header">
                <div class="header-info">
                    <div class="name">{personal_info.get('name', 'Your Name')}</div>
                    <div class="contact-info">
                        {personal_info.get('email', '')} | {personal_info.get('phone', '')} | {personal_info.get('location', '')}
                    </div>
                </div>
                {profile_img_tag}
            </div>

            <div class="content">
                <div class="left-col">
                    <div class="section-title">Professional Summary</div>
                    <p style="font-size: 10pt; color: #475569;">{summary}</p>

                    <div class="section-title">Experience</div>
                    {experience_html}

                    <div class="section-title">Education</div>
                    {education_html}
                </div>

                <div class="right-col">
                    <div class="section-title">Skills</div>
                    <ul class="skills-list">
                        {skills_html}
                    </ul>

                    {f'<div class="section-title">LinkedIn</div><div style="font-size: 10pt; color: #475569;">{personal_info.get("linkedin", "")}</div>' if personal_info.get('linkedin') else ''}
                </div>
            </div>
        """

    elif template_id == "elegant":
        # Elegant: Sophisticated, centered headers, serif fonts, gold/beige accents
        style = """
            @page { margin: 0; size: A4; }
            body { font-family: 'Georgia', serif; margin: 0; color: #2c2c2c; line-height: 1.6; background-color: #fdfbf7; }
            .container { padding: 50px; max-width: 800px; margin: 0 auto; }

            .header { text-align: center; margin-bottom: 40px; border-bottom: 1px solid #d4af37; padding-bottom: 30px; }
            .profile-pic { width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin-bottom: 20px; border: 1px solid #d4af37; padding: 3px; }
            .name { font-size: 30pt; font-weight: normal; color: #1a1a1a; margin: 0 0 10px 0; letter-spacing: 2px; }
            .contact-info { font-size: 10pt; color: #666; font-style: italic; }

            .section { margin-bottom: 30px; }
            .section-title { text-align: center; font-size: 14pt; color: #d4af37; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 20px; font-weight: normal; }

            .job, .edu { margin-bottom: 25px; }
            .job h3, .edu h3 { font-size: 12pt; font-weight: bold; margin: 0; color: #333; }
            .company-date, .school-date { font-size: 10pt; color: #888; font-style: italic; margin-bottom: 8px; }
            ul { padding-left: 20px; color: #444; font-size: 11pt; }

            .skills-grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
            .skill-item { border: 1px solid #d4af37; color: #d4af37; padding: 5px 15px; font-size: 10pt; border-radius: 20px; }
        """

        skills_grid_html = "".join([f'<span class="skill-item">{skill}</span>' for skill in skills])

        body_content = f"""
            <div class="container">
                <div class="header">
                    {profile_img_tag}
                    <div class="name">{personal_info.get('name', 'Your Name')}</div>
                    <div class="contact-info">
                        {personal_info.get('location', '')} &bull; {personal_info.get('email', '')} &bull; {personal_info.get('phone', '')}
                    </div>
                </div>

                <div class="section">
                    <div class="section-title">Profile</div>
                    <p style="text-align: center; max-width: 600px; margin: 0 auto;">{summary}</p>
                </div>

                <div class="section">
                    <div class="section-title">Experience</div>
                    {experience_html}
                </div>

                <div class="section">
                    <div class="section-title">Education</div>
                    {education_html}
                </div>

                <div class="section">
                    <div class="section-title">Expertise</div>
                    <div class="skills-grid">
                        {skills_grid_html}
                    </div>
                </div>
            </div>
        """

    else:  # Default to 'modern'
        # Modern: Two-column layout (Sidebar + Main)
        style = """
            @page { margin: 0; size: A4; }
            body { font-family: 'Helvetica', 'Arial', sans-serif; margin: 0; padding: 0; color: #333; line-height: 1.5; }
            .container { display: flex; height: 100%; }

            /* Sidebar (Left Column) */
            .sidebar { width: 30%; background-color: #2c3e50; color: white; padding: 30px 20px; height: 100%; box-sizing: border-box; }
            .profile-pic { width: 150px; height: 150px; border-radius: 50%; object-fit: cover; margin: 0 auto 20px; display: block; border: 3px solid white; }
            .contact-info { margin-bottom: 30px; font-size: 0.9em; }
            .contact-info div { margin-bottom: 10px; word-wrap: break-word; }
            .skills-section h2 { border-bottom: 1px solid #7f8c8d; padding-bottom: 5px; margin-bottom: 15px; font-size: 1.2em; text-transform: uppercase; letter-spacing: 1px; }
            .skills-list { list-style: none; padding: 0; }
            .skills-list li { background: #34495e; padding: 5px 10px; margin-bottom: 5px; border-radius: 3px; font-size: 0.9em; }

            /* Main Content (Right Column) */
            .main { width: 70%; padding: 40px; box-sizing: border-box; background-color: white; }
            .header { margin-bottom: 30px; border-bottom: 2px solid #2c3e50; padding-bottom: 20px; }
            .name { font-size: 2.5em; font-weight: bold; color: #2c3e50; margin: 0; text-transform: uppercase; }
            .summary { font-style: italic; color: #555; margin-top: 10px; }

            .section { margin-bottom: 25px; }
            .section-title { font-size: 1.3em; font-weight: bold; color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px; margin-bottom: 15px; text-transform: uppercase; }

            .job { margin-bottom: 20px; }
            .job h3 { margin: 0 0 5px; font-size: 1.1em; color: #2980b9; }
            .company-date { font-size: 0.9em; color: #7f8c8d; margin-bottom: 10px; display: flex; justify-content: space-between; }
            .job ul { margin: 0; padding-left: 20px; color: #444; }
            .job li { margin-bottom: 5px; }

            .edu { margin-bottom: 15px; }
            .edu h3 { margin: 0 0 5px; font-size: 1.1em; color: #2980b9; }
            .school-date { font-size: 0.9em; color: #7f8c8d; }
        """
        body_content = f"""
            <div class="container">
                <div class="sidebar">
                    {profile_img_tag}

                    <div class="contact-info">
                        <div><strong>Email:</strong><br>{personal_info.get('email', '')}</div>
                        <div><strong>Phone:</strong><br>{personal_info.get('phone', '')}</div>
                        <div><strong>Location:</strong><br>{personal_info.get('location', '')}</div>
                        {linkedin_div}
                    </div>

                    <div class="skills-section">
                        <h2>Skills</h2>
                        <ul class="skills-list">
                            {skills_html}
                        </ul>
                    </div>
                </div>

                <div class="main">
                    <div class="header">
                        <h1 class="name">{personal_info.get('name', 'Your Name')}</h1>
                        <div class="summary">{summary}</div>
                    </div>

                    <div class="section">
                        <div class="section-title">Experience</div>
                        {experience_html}
                    </div>

                    <div class="section">
                        <div class="section-title">Education</div>
                        {education_html}
                    </div>
                </div>
            </div>
        """

    return f"""
    <html>
    <head>
        <style>{style}</style>
    </head>
    <body>
        {body_content}
    </body>
    </html>
    """
