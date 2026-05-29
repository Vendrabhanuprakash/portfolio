from django.shortcuts import render


def home(request):
    context = {
        'projects': [
            {
                'title': 'Personal Portfolio',
                'description': 'A responsive Django portfolio showcasing projects, skills, and resume — built with Bootstrap and custom CSS.',
                'icon': 'fas fa-laptop-code',
                'tags': ['Django', 'Python', 'Bootstrap', 'CSS'],
                'link': '#',
            },
            {
                'title': 'ML Learning Projects',
                'description': 'Hands-on experiments with Python data libraries, model training basics, and visualization of results.',
                'icon': 'fas fa-brain',
                'tags': ['Python', 'NumPy', 'Pandas', 'Scikit-learn'],
                'link': '#',
            },
            {
                'title': 'Web App Backend',
                'description': 'REST-style Django backend with user-facing pages, forms, and structured templates for scalable features.',
                'icon': 'fas fa-server',
                'tags': ['Django', 'SQLite', 'HTML', 'Git'],
                'link': '#',
            },
        ],
        'skill_categories': [
            {
                'name': 'Languages',
                'icon': 'fas fa-code',
                'skills': [
                    {'name': 'Python', 'level': 90},
                    {'name': 'HTML / CSS', 'level': 85},
                    {'name': 'SQL', 'level': 75},
                ],
                'badges': ['JavaScript basics'],
            },
            {
                'name': 'Frameworks & Tools',
                'icon': 'fas fa-layer-group',
                'skills': [
                    {'name': 'Django', 'level': 85},
                    {'name': 'Bootstrap', 'level': 80},
                    {'name': 'Git & GitHub', 'level': 78},
                ],
                'badges': ['VS Code', 'Postman'],
            },
            {
                'name': 'AI & Data',
                'icon': 'fas fa-chart-line',
                'skills': [
                    {'name': 'Machine Learning', 'level': 70},
                    {'name': 'NumPy / Pandas', 'level': 75},
                    {'name': 'Data Visualization', 'level': 72},
                ],
                'badges': ['Jupyter', 'Matplotlib'],
            },
        ],
    }
    return render(request, 'index.html', context)
