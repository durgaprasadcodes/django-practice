from django.shortcuts import render


def home(request):
    data = {
        "personal": {
            "name": "Durga Prasad Kota",
            "title": "Python Full Stack Developer",
            "subtitle": "FastAPI • Django • React.js • Machine Learning",
            "description": "I build scalable web applications, REST APIs, and AI-powered solutions using Python, React, FastAPI, Django, and Machine Learning.",
            "email": "durgaprasadkota.dev@gmail.com",
        },

        "socials": { 
            "github": "https://github.com/durgaprasadcodes",
            "linkedin": "https://linkedin.com/in/your-linkedin",
            "leetcode": "https://leetcode.com/Durga_Prasad_Kota",
            "portfolio": "https://durgaprasadcodes.vercel.app"
        },

        "stats": {
            "projects": 10,
            "leetcodeProblems": 200,
            "hackathons": 2,
        }
    }

    return render(request, "home.html", data)

def about(request):
    return render(request,'about.html')

def footer(request):
    return render(request,'footer.html')

def skills(request):
    data = {
            "skills": [
                "Python",
                "FastAPI",
                "Django",
                "React.js",
                "JavaScript",
                "HTML",
                "CSS",
                "PostgreSQL",
                "MySQL",
                "MongoDB",
                "Machine Learning",
                "Git",
                "GitHub",
                "Docker"
            ]
    }
    return render(request,'skills.html',data)

def contact(request):
    return render(request,'contact.html')
