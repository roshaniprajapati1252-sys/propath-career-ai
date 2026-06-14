from flask import Flask, render_template, request

app = Flask(__name__)


# ---------------- GPA CALCULATOR ---------------- #

def calculate_gpa(marks):
    """
    marks: list of numbers (0-100)
    returns: cgpa, percentage, grade
    """
    if not marks:
        return 0.0, 0.0, "N/A"

    avg = sum(marks) / len(marks)
    percentage = avg
    cgpa = round(percentage / 9.5, 2)  # simple conversion

    if percentage >= 90:
        grade = "O"
    elif percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B+"
    elif percentage >= 50:
        grade = "B"
    else:
        grade = "F"

    return cgpa, round(percentage, 2), grade


# ---------------- SKILL GAP ANALYZER ---------------- #

def compute_skill_gap(user_levels, required_levels):
    """
    user_levels, required_levels: dicts with same keys, values 0-10
    returns: match_percent, gap_percent, prep_months, top_priority
    """
    gaps = {}
    total_skills = len(user_levels)
    if total_skills == 0:
        return 0, 100, 0, "N/A"

    for skill, user_val in user_levels.items():
        req_val = required_levels.get(skill, user_val)
        gaps[skill] = max(req_val - user_val, 0)

    total_gap_points = sum(gaps.values())
    max_gap_points = total_skills * 10
    gap_percent = round((total_gap_points / max_gap_points) * 100, 1)
    match_percent = round(100 - gap_percent, 1)

    # very rough prep time estimate: each point ~ 0.3 months
    prep_months = round(total_gap_points * 0.3, 1)

    # top priority = skill with highest gap
    top_priority = max(gaps, key=gaps.get) if gaps else "N/A"

    return match_percent, gap_percent, prep_months, top_priority


# ---------------- SALARY ESTIMATOR ---------------- #

def estimate_salary(experience_years, skill_level):
    """
    experience_years: float
    skill_level: 'beginner', 'intermediate', 'advanced'
    returns: low, avg, high (LPA)
    """
    base_low = 3.0
    base_high = 8.0

    if skill_level == "beginner":
        factor = 1.0
    elif skill_level == "intermediate":
        factor = 1.3
    else:
        factor = 1.6

    exp_factor = 1 + (experience_years * 0.1)

    low = round(base_low * factor * exp_factor, 1)
    high = round(base_high * factor * exp_factor, 1)
    avg = round((low + high) / 2, 1)

    return low, avg, high


# ---------------- STATIC DATA ---------------- #

INTERVIEW_QA = [
    {
        "category": "DSA",
        "question": "Stack vs Queue – what is the difference?",
        "answer": "Stack is LIFO (last in, first out); Queue is FIFO (first in, first out). "
                  "Stack uses push/pop; queue uses enqueue/dequeue."
    },
    {
        "category": "OOP",
        "question": "Explain the 4 pillars of OOP.",
        "answer": "Encapsulation, Inheritance, Polymorphism, and Abstraction."
    },
    {
        "category": "DBMS",
        "question": "What is normalization in DBMS?",
        "answer": "Normalization reduces redundancy and improves data integrity using normal forms like 1NF, 2NF, 3NF."
    },
]

PROJECT_IDEAS = [
    {
        "level": "Beginner",
        "title": "Student Result Management System",
        "tags": ["Python", "MySQL", "Tkinter"],
        "desc": "Manage marks, generate grades and ranks for students."
    },
    {
        "level": "Intermediate",
        "title": "Weather App with API",
        "tags": ["JavaScript", "REST API"],
        "desc": "Show live weather and 5-day forecast using a public API."
    },
    {
        "level": "Advanced",
        "title": "AI Chatbot for College FAQs",
        "tags": ["Python", "Flask", "LLM API"],
        "desc": "Answer student questions about courses, exams and placements."
    },
]


# ---------------- ROUTES ---------------- #

@app.route("/", methods=["GET", "POST"])
def index():
    gpa_result = None
    skill_result = None
    salary_result = None

    if request.method == "POST":
        form_type = request.form.get("form_type")

        # GPA form
        if form_type == "gpa":
            marks = []
            for i in range(1, 7):
                val = request.form.get(f"sub{i}")
                if val:
                    try:
                        marks.append(float(val))
                    except ValueError:
                        pass
            gpa_result = calculate_gpa(marks)

        # Skill gap form
        elif form_type == "skills":
            # user levels
            t_user = int(request.form.get("tech_user", 5))
            s_user = int(request.form.get("sys_user", 3))
            l_user = int(request.form.get("lead_user", 4))
            c_user = int(request.form.get("comm_user", 6))

            # required levels
            t_req = int(request.form.get("tech_req", 8))
            s_req = int(request.form.get("sys_req", 9))
            l_req = int(request.form.get("lead_req", 8))
            c_req = int(request.form.get("comm_req", 8))

            user_levels = {
                "Technical": t_user,
                "System Design": s_user,
                "Leadership": l_user,
                "Communication": c_user,
            }
            required_levels = {
                "Technical": t_req,
                "System Design": s_req,
                "Leadership": l_req,
                "Communication": c_req,
            }

            skill_result = compute_skill_gap(user_levels, required_levels)

        # Salary form
        elif form_type == "salary":
            exp = float(request.form.get("experience", 0))
            skill = request.form.get("skill_level", "beginner")
            salary_result = estimate_salary(exp, skill)

    return render_template(
        "index.html",
        gpa_result=gpa_result,
        skill_result=skill_result,
        salary_result=salary_result,
        interview_qa=INTERVIEW_QA,
        project_ideas=PROJECT_IDEAS,
    )


if __name__ == "__main__":
    app.run(debug=True)
