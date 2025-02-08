// Navigation Toggle
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelector('.nav-links');

navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollTop({
            behavior: 'smooth'
        });
    });
});

// Intersection Observer for Animation
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        }
    });
}, observerOptions);

document.querySelectorAll('.roadmap-card, .feature').forEach((element) => {
    observer.observe(element);
});

// Form Validation (for Contact Page)
const validateForm = (form) => {
    const email = form.querySelector('input[type="email"]');
    const message = form.querySelector('textarea');
    
    let isValid = true;
    
    if (!email.value.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
        email.classList.add('error');
        isValid = false;
    } else {
        email.classList.remove('error');
    }
    
    if (message.value.length < 10) {
        message.classList.add('error');
        isValid = false;
    } else {
        message.classList.remove('error');
    }
    
    return isValid;
};

// Resume ATS Checker
const resumeChecker = {
    keywords: ['javascript', 'python', 'react', 'node.js', 'html', 'css'],
    
    checkResume(text) {
        const foundKeywords = new Set();
        const lowercaseText = text.toLowerCase();
        
        this.keywords.forEach(keyword => {
            if (lowercaseText.includes(keyword.toLowerCase())) {
                foundKeywords.add(keyword);
            }
        });
        
        return {
            matchedKeywords: Array.from(foundKeywords),
            score: (foundKeywords.size / this.keywords.length) * 100
        };
    }
};

// Initialize Resume Checker if on Resume Page
if (document.querySelector('#resume-upload')) {
    const fileInput = document.querySelector('#resume-upload');
    const results = document.querySelector('#resume-results');
    
    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();
        
        reader.onload = (event) => {
            const text = event.target.result;
            const analysis = resumeChecker.checkResume(text);
            
            results.innerHTML = `
                <h3>ATS Analysis Results</h3>
                <p>Match Score: ${analysis.score.toFixed(1)}%</p>
                <p>Matched Keywords: ${analysis.matchedKeywords.join(', ')}</p>
            `;
        };
        
        reader.readAsText(file);
    });
}

// Add animation classes
document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    elements.forEach(element => {
        element.classList.add('animate');
    });
});
// Roadmap Filtering
const filterButtons = document.querySelectorAll('.filter-btn');
const roadmapItems = document.querySelectorAll('.roadmap-item');

filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons
        filterButtons.forEach(btn => btn.classList.remove('active'));
        // Add active class to clicked button
        button.classList.add('active');
        
        const filter = button.dataset.filter;
        
        roadmapItems.forEach(item => {
            if (filter === 'all' || item.dataset.category === filter) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
});

// Resume Upload Handling
const uploadBox = document.getElementById('upload-box');
const fileInput = document.getElementById('resume-upload');
const loader = document.getElementById('analysis-loader');
const resultsContainer = document.getElementById('resume-results');

if (uploadBox && fileInput) {
    uploadBox.addEventListener('click', () => {
        fileInput.click();
    });

    uploadBox.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadBox.classList.add('drag-over');
    });

    uploadBox.addEventListener('dragleave', () => {
        uploadBox.classList.remove('drag-over');
    });

    uploadBox.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadBox.classList.remove('drag-over');
        
        if (e.dataTransfer.files.length) {
            fileInput.files = e.dataTransfer.files;
            handleFileUpload(e.dataTransfer.files[0]);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) {
            handleFileUpload(e.target.files[0]);
        }
    });
}

function handleFileUpload(file) {
    // Show loader
    loader.style.display = 'block';
    resultsContainer.innerHTML = '';

    // Simulated analysis delay
    setTimeout(() => {
        analyzeResume(file);
    }, 2000);
}

function analyzeResume(file) {
    const reader = new FileReader();
    
    reader.onload = (e) => {
        const text = e.target.result;
        const keywords = ['javascript', 'react', 'node.js', 'python', 'java', 'sql', 'aws', 'docker'];
        const foundKeywords = keywords.filter(keyword => 
            text.toLowerCase().includes(keyword.toLowerCase())
        );
        
        const score = (foundKeywords.length / keywords.length) * 100;
        
        // Hide loader and show results
        loader.style.display = 'none';
        resultsContainer.innerHTML = `
            <div class="analysis-results">
                <h3>ATS Analysis Results</h3>
                <div class="score-container">
                    <div class="score">${score.toFixed(1)}%</div>
                    <p>ATS Compatibility Score</p>
                </div>
                <div class="keywords-found">
                    <h4>Keywords Found:</h4>
                    <div class="keyword-tags">
                        ${foundKeywords.map(keyword => 
                            `<span class="keyword-tag">${keyword}</span>`
                        ).join('')}
                    </div>
                </div>
                <div class="recommendations">
                    <h4>Recommendations:</h4>
                    <ul>
                        <li>Include more industry-specific keywords</li>
                        <li>Use standard section headings</li>
                        <li>Ensure proper formatting</li>
                    </ul>
                </div>
            </div>
        `;
    };
    
    reader.readAsText(file);
}

// Contact Form Validation
const contactForm = document.querySelector('.contact-form');

if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const name = contactForm.querySelector('input[name="name"]').value;
        const email = contactForm.querySelector('input[name="email"]').value;
        const message = contactForm.querySelector('textarea[name="message"]').value;
        
        if (validateForm(name, email, message)) {
            // Simulate form submission
            alert('Message sent successfully!');
            contactForm.reset();
        }
    });
}

function validateForm(name, email, message) {
    let isValid = true;
    
    if (!name.trim()) {
        isValid = false;
        showError('name');
    }
    
    if (!email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
        isValid = false;
        showError('email');
    }
    
    if (!message.trim()) {
        isValid = false;
        showError('message');
    }
    
    return isValid;
}

function showError(fieldName) {
    const field = document.querySelector(`[name="${fieldName}"]`);
    field.classList.add('error');
    
    field.addEventListener('input', () => {
        field.classList.remove('error');
    });
}

// Animations
const animateOnScroll = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        }
    });
}, {
    threshold: 0.1
});

document.querySelectorAll('.service-card, .team-member, .pricing-card, .contact-card').forEach(element => {
    animateOnScroll.observe(element);
});
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
