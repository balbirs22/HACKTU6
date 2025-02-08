function obtenerRoadmap(selectedRole) {
    var roadmaps = {
        'data-analyst': [
            {"id": 1, "skill": "Statistics", "completed": false},
            {"id": 2, "skill": "Python Programming", "completed": false},
            {"id": 3, "skill": "Data Analysis", "completed": false},
            {"id": 4, "skill": "Visualization Tools (Matplotlib, Seaborn)", "completed": false},
            {"id": 5, "skill": "SQL and Relational Databases", "completed": false},
            {"id": 6, "skill": "Data Manipulation with Pandas", "completed": false},
            {"id": 7, "skill": "Basic Machine Learning", "completed": false},
            {"id": 8, "skill": "Advanced Excel", "completed": false},
            {"id": 9, "skill": "Business Intelligence", "completed": false},
            {"id": 10, "skill": "Results Communication", "completed": false}
        ],
        'web-developer': [
            {"id": 1, "skill": "HTML5, CSS3, JavaScript", "completed": false},
            {"id": 2, "skill": "Web Frameworks (React, Angular, Vue.js)", "completed": false},
            {"id": 3, "skill": "AJAX and RESTful APIs", "completed": false},
            {"id": 4, "skill": "Responsive Design and UX/UI", "completed": false},
            {"id": 5, "skill": "SEO", "completed": false},
            {"id": 6, "skill": "Build and Packaging Tools (Webpack, npm)", "completed": false},
            {"id": 7, "skill": "Mobile Application Development", "completed": false},
            {"id": 8, "skill": "Web Security", "completed": false},
            {"id": 9, "skill": "Performance Testing and Optimization", "completed": false},
            {"id": 10, "skill": "Content Management Systems (WordPress)", "completed": false}
        ],
        'cybersecurity': [
            {"id": 1, "skill": "Network Security", "completed": false},
            {"id": 2, "skill": "Ethical Hacking", "completed": false},
            {"id": 3, "skill": "Incident Response and Forensics", "completed": false},
            {"id": 4, "skill": "Security Information and Event Management (SIEM)", "completed": false},
            {"id": 5, "skill": "Cryptography", "completed": false},
            {"id": 6, "skill": "Security Policies and Procedures", "completed": false},
            {"id": 7, "skill": "Web Application Security", "completed": false},
            {"id": 8, "skill": "Cloud Security", "completed": false},
            {"id": 9, "skill": "Wireless Security", "completed": false},
            {"id": 10, "skill": "Malware Analysis", "completed": false}
        ],
        'game-developer': [
            {"id": 1, "skill": "Game Design Principles", "completed": false},
            {"id": 2, "skill": "Game Development Engines (Unity, Unreal)", "completed": false},
            {"id": 3, "skill": "3D Modeling and Animation", "completed": false},
            {"id": 4, "skill": "Physics in Games", "completed": false},
            {"id": 5, "skill": "Artificial Intelligence in Games", "completed": false},
            {"id": 6, "skill": "Multiplayer Game Development", "completed": false},
            {"id": 7, "skill": "Virtual Reality (VR) Development", "completed": false},
            {"id": 8, "skill": "Game Testing and Quality Assurance", "completed": false},
            {"id": 9, "skill": "Monetization Strategies for Games", "completed": false},
            {"id": 10, "skill": "Game Marketing and Community Building", "completed": false}
        ],
        'data-scientist': [
            {"id": 1, "skill": "Mathematics and Statistics", "completed": false},
            {"id": 2, "skill": "Machine Learning Algorithms", "completed": false},
            {"id": 3, "skill": "Big Data Technologies (Hadoop, Spark)", "completed": false},
            {"id": 4, "skill": "Data Cleaning and Preprocessing", "completed": false},
            {"id": 5, "skill": "Feature Engineering", "completed": false},
            {"id": 6, "skill": "Natural Language Processing (NLP)", "completed": false},
            {"id": 7, "skill": "Time Series Analysis", "completed": false},
            {"id": 8, "skill": "Data Visualization (Tableau, Power BI)", "completed": false},
            {"id": 9, "skill": "Experimentation and A/B Testing", "completed": false},
            {"id": 10, "skill": "Deep Learning", "completed": false}
        ],
        'database-developer': [
            {"id": 1, "skill": "Relational Database Management Systems (RDBMS)", "completed": false},
            {"id": 2, "skill": "SQL Programming", "completed": false},
            {"id": 3, "skill": "Database Design and Normalization", "completed": false},
            {"id": 4, "skill": "Data Modeling", "completed": false},
            {"id": 5, "skill": "Stored Procedures and Triggers", "completed": false},
            {"id": 6, "skill": "Database Security", "completed": false},
            {"id": 7, "skill": "NoSQL Databases (MongoDB, Cassandra)", "completed": false},
            {"id": 8, "skill": "Database Optimization", "completed": false},
            {"id": 9, "skill": "Backup and Recovery", "completed": false},
            {"id": 10, "skill": "ETL Processes", "completed": false}
        ],
        'software-developer': [
            {"id": 1, "skill": "Programming Languages (Java, C++, Python)", "completed": false},
            {"id": 2, "skill": "Object-Oriented Programming (OOP)", "completed": false},
            {"id": 3, "skill": "Version Control (Git)", "completed": false},
            {"id": 4, "skill": "Software Development Life Cycle (SDLC)", "completed": false},
            {"id": 5, "skill": "Debugging and Troubleshooting", "completed": false},
            {"id": 6, "skill": "Web Services (REST, SOAP)", "completed": false},
            {"id": 7, "skill": "Agile Methodologies", "completed": false},
            {"id": 8, "skill": "Continuous Integration/Continuous Deployment (CI/CD)", "completed": false},
            {"id": 9, "skill": "Unit Testing", "completed": false},
            {"id": 10, "skill": "Code Review", "completed": false}
        ],
        'aws-developer': [
            {"id": 1, "skill": "AWS Services Overview", "completed": false},
            {"id": 2, "skill": "Compute Services (EC2, Lambda)", "completed": false},
            {"id": 3, "skill": "Storage Services (S3, EBS)", "completed": false},
            {"id": 4, "skill": "Database Services (RDS, DynamoDB)", "completed": false},
            {"id": 5, "skill": "Networking in AWS", "completed": false},
            {"id": 6, "skill": "Identity and Access Management (IAM)", "completed": false},
            {"id": 7, "skill": "Security Best Practices in AWS", "completed": false},
            {"id": 8, "skill": "Serverless Architecture", "completed": false},
            {"id": 9, "skill": "AWS CloudFormation", "completed": false},
            {"id": 10, "skill": "Monitoring and Logging in AWS", "completed": false}
        ],
        'devops': [
            {"id": 1, "skill": "Infrastructure as Code (IaC)", "completed": false},
            {"id": 2, "skill": "Configuration Management (Ansible, Puppet, Chef)", "completed": false},
            {"id": 3, "skill": "Containerization (Docker, Kubernetes)", "completed": false},
            {"id": 4, "skill": "Continuous Integration/Continuous Deployment (CI/CD) Pipelines", "completed": false},
            {"id": 5, "skill": "Monitoring and Logging Tools", "completed": false},
            {"id": 6, "skill": "Collaboration and Communication Tools", "completed": false},
            {"id": 7, "skill": "Version Control Systems", "completed": false},
            {"id": 8, "skill": "Security Practices in DevOps", "completed": false},
            {"id": 9, "skill": "Cloud Technologies (AWS, Azure, GCP)", "completed": false},
            {"id": 10, "skill": "Agile and Scrum Methodologies", "completed": false}
        ]
        
    };

    return roadmaps[selectedRole] || [];
}


var checksTotales = 10;  
var checksCompletados = 0;


function mostrarGrafico(container, checksTotales, checksCompletados) {
    container.find('#myChart').html('');

    var porcentajeCompletado = (checksCompletados / checksTotales) * 100;

    var progressHTML = `
        <div class="progress">
            <div class="progress-bar bg-success" role="progressbar" style="width: ${porcentajeCompletado}%" aria-valuenow="${porcentajeCompletado}" aria-valuemin="0" aria-valuemax="100">
                ${Math.floor(porcentajeCompletado)}%
            </div>
        </div>
    `;

    container.find('#myChart').html(progressHTML);
}


function reiniciarYMostrar() {
    checksCompletados = 0;

 
    mostrarGrafico($('#stats'), checksTotales, checksCompletados);
}


function mostrarRoadmap() {
    reiniciarYMostrar(); 
    var selectedRole = $('#roles').val();
    var roadmapData = obtenerRoadmap(selectedRole);
    mostrarSkills(roadmapData);
}

function mostrarSkills(roadmapData) {
    var roadmapContainer = $('#roadmap');
    roadmapContainer.empty();

    for (var i = 0; i < roadmapData.length; i++) {
        var skill = roadmapData[i];
        var skillHTML = `
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="check${skill.id}" onchange="marcarCheck(${skill.id})">
                <label class="form-check-label" for="check${skill.id}">${skill.skill}</label>
            </div>
        `;
        roadmapContainer.append(skillHTML);
    }

    mostrarGrafico($('#stats'), checksTotales, checksCompletados);
}

function marcarCheck(checkId) {
    var isChecked = $('#check' + checkId).prop('checked');

    checksCompletados += isChecked ? 1 : -1;

    mostrarGrafico($('#stats'), checksTotales, checksCompletados);
}

$(document).ready(function () {
    mostrarRoadmap();
});