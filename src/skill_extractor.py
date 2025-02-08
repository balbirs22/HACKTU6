# skill_extraction.py

import spacy
from spacy.matcher import PhraseMatcher
import text_preprocessing  # Import the module as a whole to avoid circular imports

def extract_skills(text, skills_list=None):
    """
    Extracts skills from the input text using spaCy's PhraseMatcher.

    Parameters:
        text (str): Raw text (e.g., extracted from PDF/DOCX) to analyze.
        skills_list (list, optional): List of known skills to search for.
            If None, a default list is used.

    Returns:
        list: A list of unique extracted skills.
    """
    # Default skills list (you can expand this as needed)
    if skills_list is None:
        skills_list = [
    "python", "java", "c", "c++", "c#", "javascript", "typescript", "ruby", "perl", "php",
    "swift", "kotlin", "scala", "go", "rust", "haskell", "lua", "r", "objective-c", "dart",
    "visual basic", "matlab", "groovy", "shell scripting", "powershell", "assembly", "fortran",
    "cobol", "delphi", "f#", "clojure", "erlang", "lisp", "prolog", "sql", "pl/sql", "nosql",
    "mongodb", "mysql", "postgresql", "mariadb", "oracle", "sqlite", "redis", "cassandra",
    "dynamodb", "neo4j", "hbase", "hive", "bigquery", "impala", "presto", "cockroachdb",
    "firestore", "elasticsearch", "influxdb", "timescale", "aws", "azure", "gcp", "oracle cloud",
    "digitalocean", "heroku", "ibm cloud", "alibaba cloud", "vmware", "openstack", "kubernetes",
    "docker", "jenkins", "ansible", "chef", "puppet", "terraform", "vagrant", "travis ci",
    "circleci", "gitlab ci", "azure devops", "bamboo", "maven", "gradle", "ant", "sbt", "npm",
    "yarn", "bower", "webpack", "gulp", "grunt", "rollup", "parcel", "babel", "eslint",
    "prettier", "stylelint", "jshint", "jest", "mocha", "chai", "jasmine", "cypress", "selenium",
    "puppeteer", "protractor", "karma", "enzyme", "integration testing", "unit testing",
    "system testing", "acceptance testing", "performance testing", "security testing",
    "usability testing", "test automation", "bdd", "tdd", "agile testing", "continuous integration",
    "continuous deployment", "continuous delivery", "data analysis", "data visualization",
    "machine learning", "deep learning", "neural networks", "computer vision",
    "natural language processing", "nlp", "reinforcement learning", "scikit-learn",
    "tensorflow", "keras", "pytorch", "theano", "caffe", "mxnet", "pandas", "numpy", "scipy",
    "matplotlib", "seaborn", "plotly", "power bi", "tableau", "d3.js", "ggplot", "bokeh",
    "business intelligence", "predictive analytics", "data mining", "statistical modeling",
    "regression analysis", "time series analysis", "forecasting", "optimization", "simulation",
    "big data", "hadoop", "spark", "mapreduce", "flink", "kafka", "storm", "pig", "flume",
    "sqoop", "zookeeper", "ambari", "oozie", "rdbms", "nosql databases", "etl", "data warehousing",
    "data lakes", "information architecture", "data governance", "data modeling",
    "data engineering", "business analytics", "statistics", "mathematics", "probability",
    "linear algebra", "calculus", "discrete math", "graph theory", "cryptography", "blockchain",
    "bitcoin", "ethereum", "smart contracts", "decentralized applications", "dapps", "iot",
    "internet of things", "embedded systems", "arduino", "raspberry pi", "sensor networks",
    "wearable technology", "augmented reality", "virtual reality", "mixed reality", "unity",
    "unreal engine", "3d modeling", "game development", "game design", "animation", "vr", "ar",
    "openGL", "directx", "vulkan", "3d rendering", "computer graphics", "mobile development",
    "android", "ios", "react native", "flutter", "xamarin", "cordova", "mobile app development",
    "responsive design", "ui/ux", "user interface design", "user experience design",
    "interaction design", "wireframing", "prototyping", "adobe xd", "sketch", "figma", "invision",
    "photoshop", "illustrator", "indesign", "after effects", "premiere pro", "digital marketing",
    "seo", "sem", "google analytics", "content marketing", "social media marketing",
    "email marketing", "ppc", "affiliate marketing", "ecommerce", "wordpress", "joomla",
    "drupal", "shopify", "magento", "prestashop", "salesforce", "crm", "sap", "oracle erp",
    "microsoft dynamics", "business process management", "enterprise resource planning",
    "customer relationship management", "it service management", "itil", "cybersecurity",
    "information security", "network security", "cloud security", "application security",
    "penetration testing", "ethical hacking", "vulnerability assessment", "risk management",
    "compliance", "gdpr", "firewalls", "ids", "ips", "siem", "data privacy", "security operations",
    "zero trust", "malware analysis", "forensics", "incident response", "disaster recovery",
    "business continuity", "networking", "tcp/ip", "dns", "dhcp", "routing", "switching",
    "wireless networking", "lan", "wan", "vpn", "firewall configuration", "load balancing",
    "sdn", "software defined networking", "virtualization", "hypervisors", "hyper-v", "kvm",
    "virtualbox", "containerization", "lxc", "openvz", "ci/cd", "devops", "infrastructure as code",
    "monitoring", "logging", "alerting", "prometheus", "grafana", "datadog", "new relic",
    "splunk", "system administration", "linux", "windows", "macos", "unix", "network administration",
    "system architecture", "cloud architecture", "microservices", "restful apis", "graphql",
    "soap", "api development", "api integration", "web services", "serverless", "lambda",
    "event-driven architecture", "message queues", "rabbitmq", "activemq", "middleware",
    "enterprise integration", "soa", "design patterns", "mvc", "mvvm", "mvp", "clean architecture",
    "domain driven design", "object oriented design", "data structures", "algorithms",
    "complexity analysis", "git", "github", "gitlab", "bitbucket", "version control", "svn",
    "mercurial", "software development lifecycle", "agile methodologies", "scrum", "kanban",
    "lean", "waterfall", "collaboration", "jira", "confluence", "slack", "trello", "asana",
    "basecamp", "time management", "leadership", "communication", "problem solving",
    "critical thinking", "creative thinking", "ux research", "user testing", "market research",
    "business analysis", "financial analysis", "risk assessment", "a/b testing", "multivariate testing",
    "predictive modeling", "customer segmentation", "data storytelling", "business strategy",
    "strategic planning", "digital transformation", "innovation", "change management",
    "operational excellence", "lean manufacturing", "six sigma", "quality assurance",
    "software quality assurance", "performance tuning", "scalability", "load testing",
    "stress testing", "benchmarking", "container orchestration", "service mesh",
    "distributed systems", "parallel computing", "quantum computing", "edge computing",
    "fog computing", "data center management", "hardware", "network hardware", "iot security",
    "supply chain management", "logistics", "procurement", "inventory management", "3d printing",
    "robotics", "automation", "process automation", "machine vision", "speech recognition",
    "voice assistants", "chatbots", "virtual assistants", "augmented analytics",
    "predictive maintenance", "digital twins", "simulation", "modeling", "information systems",
    "enterprise architecture", "systems integration", "customer experience", "product management",
    "content management", "multimedia", "video production", "audio engineering", "network monitoring",
    "virtual reality", "augmented reality", "mixed reality", "cross-platform development",
    "remote work", "telecommuting", "collaborative tools", "information retrieval", "data curation",
    "knowledge management", "enterprise search", "semantic search", "recommendation systems",
    "personalization", "adaptive learning", "smart devices", "wearable tech", "healthtech",
    "fintech", "insurtech", "regtech", "legaltech", "edtech", "proptech", "agritech", "martech",
    "cleantech", "biotech", "medtech", "robot process automation"
    ]

    
    # Step 1: Clean the text using the clean_text function from text_preprocessing
    cleaned_text = text_preprocessing.clean_text(text)
    
    # Step 2: Process the cleaned text with spaCy (using the nlp object from text_preprocessing)
    doc = text_preprocessing.nlp(cleaned_text)
    
    # Step 3: Initialize the PhraseMatcher with case-insensitive matching.
    matcher = PhraseMatcher(text_preprocessing.nlp.vocab, attr="LOWER")
    patterns = [text_preprocessing.nlp.make_doc(skill) for skill in skills_list]
    matcher.add("SKILL", patterns)
    
    # Step 4: Apply the matcher to the doc to find skills.
    matches = matcher(doc)
    
    # Step 5: Extract matched skills and deduplicate them.
    extracted_skills = set()
    for match_id, start, end in matches:
        span = doc[start:end]
        extracted_skills.add(span.text)
    
    return list(extracted_skills)

# Example usage (for testing):
if __name__ == "__main__":
    sample_text = """
    Jane Smith is an experienced Data Scientist with a strong background in Python,
    machine learning, and data analysis. She has applied SQL and deep learning techniques using
    TensorFlow and PyTorch. In previous roles, she has also worked with Java and C++ for developing software.
    """
    skills_found = extract_skills(sample_text)
    print("Extracted Skills:", skills_found)
