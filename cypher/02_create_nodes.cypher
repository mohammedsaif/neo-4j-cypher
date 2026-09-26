CREATE
(:Student {
    id: "S001",
    name: "RahulG",
    email: "rahul@example.com",
    experience: 2
}),
(:Student {
    id: "S002",
    name: "PriyaJ",
    email: "priya@example.com",
    experience: 1
}),
(:Student {
    id: "S003",
    name: "ArjunR",
    email: "arjun@example.com",
    experience: 3
}),
(:Student {
    id: "S004",
    name: "Sneha",
    email: "sneha@example.com",
    experience: 2
}),
(:Student {
    id: "S005",
    name: "Vikram",
    email: "vikram@example.com",
    experience: 4
});

CREATE
(:Course {
    id: "C001",
    name: "Python Programming",
    level: "Beginner"
}),
(:Course {
    id: "C002",
    name: "FastAPI Development",
    level: "Intermediate"
}),
(:Course {
    id: "C003",
    name: "Data Analytics",
    level: "Intermediate"
}),
(:Course {
    id: "C004",
    name: "Generative AI",
    level: "Advanced"
});

CREATE
(:Mentor {
    id: "M001",
    name: "Amit Sharma",
    expertise: "Python"
}),
(:Mentor {
    id: "M002",
    name: "Neha Kapoor",
    expertise: "Data Analytics"
}),
(:Mentor {
    id: "M003",
    name: "Ravi Kumar",
    expertise: "Generative AI"
});

CREATE
(:Skill {
    id: "SK001",
    name: "Python"
}),
(:Skill {
    id: "SK002",
    name: "FastAPI"
}),
(:Skill {
    id: "SK003",
    name: "SQL"
}),
(:Skill {
    id: "SK004",
    name: "Machine Learning"
}),
(:Skill {
    id: "SK005",
    name: "Generative AI"
});

CREATE
(:Project {
    id: "P001",
    name: "AI Data Analyst",
    status: "Completed"
}),
(:Project {
    id: "P002",
    name: "Task Management API",
    status: "Completed"
}),
(:Project {
    id: "P003",
    name: "Customer Support Bot",
    status: "In Progress"
}),
(:Project {
    id: "P004",
    name: "Sales Dashboard",
    status: "Completed"
});

CREATE
(:Company {
    id: "CO001",
    name: "Microsoft",
    industry: "Technology"
}),
(:Company {
    id: "CO002",
    name: "Google",
    industry: "Technology"
}),
(:Company {
    id: "CO003",
    name: "Amazon",
    industry: "Technology"
}),
(:Company {
    id: "CO004",
    name: "Deloitte",
    industry: "Consulting"
});