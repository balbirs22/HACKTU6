const jobs = [
   { title: "Director", 
    steps: [
        "Start with Entry-Level Position in Your Field",
        "Gain Relevant Experience in Your Industry",
        "Develop Leadership and Management Skills",
        "Build Strong Communication Skills",
        "Network with Industry Professionals",
        "Understand Financial and Budgeting Processes",
        "Take on More Responsibility at Work",
        "Seek Out Mentorship from Established Directors",
        "Pursue Continuing Education and Training",
        "Gain Experience in Project Management",
        "Stay Informed about Industry Trends and Innovations",
        "Develop a Strategic Vision for Your Career",
        "Build a Personal Brand and Reputation",
        "Participate in Industry Conferences and Workshops",
        "Create a Portfolio of Achievements and Projects",
        "Contribute to Team Success and Company Goals",
        "Learn Conflict Resolution and Problem-Solving Techniques",
        "Understand Corporate Governance and Ethics",
        "Foster a Positive Workplace Culture",
        "Prepare for Interviews for Director Positions",
        "Showcase Your Leadership Experience in Your Resume",
        "Seek Feedback on Your Management Style",
        "Join Professional Organizations in Your Field",
        "Explore Opportunities for Advancement within Your Company",
        "Consider Further Education (e.g., MBA) for Advancement",
        "Be Open to Relocation for Better Opportunities"
    ]
},
    { title: "Frontend Developer", steps: ["Learn HTML", "Learn CSS", "Learn JavaScript", "Learn React", "Build Projects", "Apply for Internships", "Create a Portfolio", "Network with Professionals", "Prepare for Interviews", "Keep Learning"] },
    { title: "Backend Developer", steps: ["Learn Python", "Learn Node.js", "Understand APIs", "Learn SQL", "Work with Databases", "Build Projects", "Deploy Applications", "Join Coding Communities", "Prepare for Interviews", "Stay Updated with Tech"] },
    { title: "Data Scientist", steps: ["Learn Python/R", "Master Statistics", "Learn Data Visualization", "Work with Databases", "Learn Machine Learning", "Build Projects", "Create a Portfolio", "Network with Professionals", "Prepare for Interviews", "Stay Updated with Trends"] },
    { title: "UI/UX Designer", steps: ["Learn Design Principles", "Learn Figma/Sketch", "Understand User Research", "Create Wireframes", "Build Prototypes", "Conduct User Testing", "Iterate Designs", "Build a Portfolio", "Network with Designers", "Prepare for Interviews"] },
    { title: "Digital Marketing Specialist", steps: ["Understand SEO", "Learn Content Marketing", "Learn Social Media Marketing", "Master Google Analytics", "Build Marketing Campaigns", "Analyze Campaign Performance", "Create a Portfolio", "Network with Professionals", "Prepare for Interviews", "Stay Updated with Trends"] },
    { title: "Cybersecurity Analyst", steps: ["Learn Networking Basics", "Understand Security Fundamentals", "Learn Penetration Testing", "Study Compliance Standards", "Build a Lab for Testing", "Work on Security Projects", "Create a Portfolio", "Network with Professionals", "Prepare for Interviews", "Stay Updated with Threats"] },
    { title: "Mobile App Developer", steps: ["Learn Swift/Kotlin", "Understand Mobile UI/UX", "Build Projects", "Learn About APIs", "Deploy Apps to App Stores", "Create a Portfolio", "Network with Developers", "Prepare for Interviews", "Stay Updated with Trends", "Contribute to Open Source"] },
    { title: "DevOps Engineer", steps: ["Learn Linux Basics", "Understand CI/CD", "Learn Cloud Platforms", "Work with Docker", "Automate Processes", "Build Projects", "Create a Portfolio", "Network with Professionals", "Prepare for Interviews", "Stay Updated with Tools"] },
    { title: "Game Developer", steps: ["Learn C#/C++", "Understand Game Engines", "Build Game Projects", "Participate in Game Jams", "Create a Portfolio", "Network with Game Developers", "Prepare for Interviews", "Stay Updated with Trends", "Contribute to Open Source", "Join Gaming Communities"] },
    { title: "Cloud Engineer", steps: ["Learn Cloud Fundamentals", "Understand AWS/Azure", "Work with Containers", "Build Cloud Solutions", "Create a Portfolio", "Network with Cloud Professionals", "Prepare for Interviews", "Stay Updated with Trends", "Join Cloud Communities", "Get Certified"] },
    { title: "AI Engineer", steps: ["Learn Python", "Understand Machine Learning", "Study Neural Networks", "Work with TensorFlow/PyTorch", "Build AI Projects", "Create a Portfolio", "Network with AI Professionals", "Prepare for Interviews", "Stay Updated with AI Trends", "Contribute to Open Source"] },
    { title: "Full Stack Developer", steps: ["Learn HTML/CSS", "Learn JavaScript", "Learn Node.js", "Understand Databases", "Work with REST APIs", "Build Full Stack Applications", "Create a Portfolio", "Network with Developers", "Prepare for Interviews", "Stay Updated with Technologies"] },
    { title: "Web Designer", steps: ["Learn HTML/CSS", "Understand Graphic Design", "Learn Design Tools", "Create Mockups", "Build Responsive Websites", "Create a Portfolio", "Network with Designers", "Prepare for Interviews", "Stay Updated with Trends", "Contribute to Design Communities"] },
    { title: "Software Tester", steps: ["Learn Testing Principles", "Understand Automation Testing", "Learn Selenium", "Build Testing Frameworks", "Create Test Cases", "Work with Development Teams", "Create a Portfolio", "Network with Testers", "Prepare for Interviews", "Stay Updated with Testing Tools"] },
    { title: "Blockchain Developer", steps: ["Learn Blockchain Fundamentals", "Understand Smart Contracts", "Learn Solidity", "Build Decentralized Apps", "Participate in Blockchain Projects", "Create a Portfolio", "Network with Developers", "Prepare for Interviews", "Stay Updated with Trends", "Contribute to Open Source"] },
    { title: "Technical Writer", steps: ["Learn Technical Writing Skills", "Understand Documentation Tools", "Create User Guides", "Work with Developers", "Build a Portfolio", "Network with Professionals", "Prepare for Interviews", "Stay Updated with Trends", "Join Writing Workshops", "Get Published"] },
    { title: "Business Analyst", steps: ["Learn Business Analysis Principles", "Understand Data Analysis", "Work with Stakeholders", "Build Business Cases", "Create Reports", "Network with Analysts", "Prepare for Interviews", "Stay Updated with Business Trends", "Join Business Communities", "Get Certified"] },
    { title: "System Administrator", steps: ["Learn Operating Systems", "Understand Networking", "Learn Server Management", "Work with Security", "Build System Documentation", "Network with IT Professionals", "Prepare for Interviews", "Stay Updated with Technologies", "Join IT Communities", "Get Certified"] },
    { title: "Network Engineer", steps: ["Learn Networking Fundamentals", "Understand Routing/Switching", "Work with Firewalls", "Build Network Infrastructure", "Create Network Documentation", "Network with Engineers", "Prepare for Interviews", "Stay Updated with Networking Trends", "Join Networking Communities", "Get Certified"] },
    { title: "Salesforce Developer", steps: ["Learn Salesforce Basics", "Understand Apex Programming", "Work with Visualforce", "Build Applications on Salesforce", "Create a Portfolio", "Network with Developers", "Prepare for Interviews", "Stay Updated with Salesforce Trends", "Join Salesforce Communities", "Get Certified"] },
    { title: "Data Analyst", steps: ["Learn SQL", "Understand Data Visualization", "Work with Excel/Tableau", "Build Data Reports", "Create a Portfolio", "Network with Analysts", "Prepare for Interviews", "Stay Updated with Data Trends", "Join Data Communities", "Get Certified"] },
    { title: "Product Manager", steps: ["Learn Product Management Principles", "Understand Market Research", "Work with Development Teams", "Build Product Roadmaps", "Create a Portfolio", "Network with Managers", "Prepare for Interviews", "Stay Updated with Trends", "Join Product Communities", "Get Certified"] },
    { title: "HR Manager", steps: ["Learn HR Principles", "Understand Recruitment Processes", "Work with Teams", "Build HR Policies", "Create a Portfolio", "Network with HR Professionals", "Prepare for Interviews", "Stay Updated with HR Trends", "Join HR Communities", "Get Certified"] },
    { title: "Financial Analyst", steps: ["Learn Financial Principles", "Understand Financial Modeling", "Work with Data Analysis", "Build Financial Reports", "Create a Portfolio", "Network with Analysts", "Prepare for Interviews", "Stay Updated with Financial Trends", "Join Financial Communities", "Get Certified"] },
    { title: "Video Game Designer", steps: ["Learn Game Design Principles", "Understand Game Mechanics", "Build Game Prototypes", "Create Game Design Documents", "Network with Game Designers", "Prepare for Interviews", "Stay Updated with Game Trends", "Join Game Design Communities", "Contribute to Game Projects", "Attend Game Jams"] },
    { title: "Research Scientist", steps: ["Learn Research Methodologies", "Understand Data Analysis", "Work in Labs", "Publish Research Papers", "Network with Scientists", "Prepare for Interviews", "Stay Updated with Scientific Trends", "Join Research Communities", "Attend Conferences", "Get Published"] },
    { title: "Operations Manager", steps: ["Learn Operations Management Principles", "Understand Supply Chain", "Work with Teams", "Build Operational Plans", "Create a Portfolio", "Network with Managers", "Prepare for Interviews", "Stay Updated with Operations Trends", "Join Operations Communities", "Get Certified"] },
    { title: "Agricultural Scientist", steps: ["Learn Agricultural Principles", "Understand Crop Management", "Work in Labs", "Conduct Experiments", "Publish Research Papers", "Network with Scientists", "Prepare for Interviews", "Stay Updated with Agricultural Trends", "Join Agricultural Communities", "Get Published"] },
    { title: "Quality Assurance Engineer", steps: ["Learn Quality Assurance Principles", "Understand Testing Methodologies", "Work with Development Teams", "Build Test Plans", "Create a Portfolio", "Network with Engineers", "Prepare for Interviews", "Stay Updated with QA Trends", "Join QA Communities", "Get Certified"] },
    { title: "Interior Designer", steps: ["Learn Design Principles", "Understand Color Theory", "Work with Clients", "Create Design Proposals", "Build a Portfolio", "Network with Designers", "Prepare for Interviews", "Stay Updated with Design Trends", "Join Design Communities", "Contribute to Design Projects"] },
    { title: "Content Writer", steps: ["Learn Writing Principles", "Understand SEO", "Build a Portfolio", "Create Content Strategies", "Network with Writers", "Prepare for Interviews", "Stay Updated with Writing Trends", "Join Writing Communities", "Contribute to Writing Projects", "Attend Writing Workshops"] },
    { title: "Graphic Designer", steps: ["Learn Graphic Design Basics", "Understand Color Theory", "Work with Design Tools", "Build a Portfolio", "Network with Designers", "Prepare for Interviews", "Stay Updated with Design Trends", "Join Design Communities", "Create Projects", "Get Certified"] },
    { title: "Network Security Specialist", steps: ["Learn Cybersecurity Principles", "Understand Firewalls", "Monitor Network Traffic", "Implement Security Protocols", "Conduct Security Audits", "Network with Professionals", "Prepare for Interviews", "Stay Updated with Cybersecurity Trends", "Join Security Communities", "Get Certified"] },
    { title: "Voice Actor", steps: ["Learn Voice Techniques", "Practice Different Accents", "Build a Voice Portfolio", "Network with Other Voice Actors", "Audition for Roles", "Join Voice Acting Communities", "Stay Updated with Industry Trends", "Attend Workshops", "Get Feedback on Performances", "Create a Demo Reel"] },
    { title: "Legal Assistant", steps: ["Learn Legal Terminology", "Understand Legal Procedures", "Work with Lawyers", "Draft Legal Documents", "Network with Legal Professionals", "Prepare for Interviews", "Stay Updated with Legal Trends", "Join Legal Communities", "Attend Legal Workshops", "Get Certified"] },
];

function displayJobs() {
    const jobList = document.getElementById('job-list');
    jobs.forEach(job => {
        const jobElement = document.createElement('div');
        jobElement.className = 'job';
        jobElement.innerHTML = `<h3>${job.title}</h3>`;
        jobElement.onclick = () => {
            localStorage.setItem('selectedJob', JSON.stringify(job));
            window.location.href = 'roadmap.html'; // Redirect to the roadmap page
        };
        jobList.appendChild(jobElement);
    });
}

function filterJobs() {
    const searchInput = document.getElementById('search').value.toLowerCase();
    const jobElements = document.querySelectorAll('.job');
    jobElements.forEach(job => {
        const title = job.querySelector('h3').innerText.toLowerCase();
        job.style.display = title.includes(searchInput) ? 'block' : 'none';
    });
}

// Initialize job display
displayJobs();
