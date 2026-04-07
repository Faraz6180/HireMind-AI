import streamlit as st

# ✅ MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="HireMind AI", layout="wide")

# Imports AFTER config
from ai_engine import *
from storage import *
from utils import *

# ---------------- UI STYLING ----------------
st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("HireMind AI 🧠")
page = st.sidebar.radio("Navigation", [
    "Dashboard",
    "Resume Analysis",
    "Resume Optimizer",
    "Cover Letter",
    "Interview Prep",
    "Tracker",
    "AI Chat"
])

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>🚀 HireMind AI Platform</h1>", unsafe_allow_html=True)

# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.header("📊 Smart Job Dashboard")

    job_title = st.text_input("Job Title")
    job_desc = st.text_area("Paste Job Description")

    if st.button("Add Job"):
        if job_title and job_desc:
            add_job(job_title, job_desc)
            st.success("✅ Job added!")
        else:
            st.warning("⚠️ Please fill both fields")

    jobs = load_jobs()

    if jobs:
        st.subheader("📌 Saved Jobs")
        for job in jobs:
            st.write(f"- {job['title']}")

        resume = st.text_area("Paste Your Resume")

        if st.button("Run Full Analysis"):
            if not resume:
                st.warning("⚠️ Please paste your resume")
            else:
                for job in jobs:
                    st.subheader(f"🔹 {job['title']}")

                    # Keyword Score
                    k_score, matched = keyword_match_score(resume, job["description"])

                    # ATS Analysis (LLM)
                    ats = ats_analysis(resume, job["description"])

                    # Decision
                    decision = decision_engine(k_score)

                    st.write(f"**📊 Keyword Match Score:** {k_score}%")
                    st.write(f"**🎯 Decision:** {decision}")

                    st.write("**✅ Matched Keywords:**")
                    st.write(matched if matched else "No strong matches")

                    st.write("**🧠 ATS Analysis:**")
                    st.write(ats)

                    st.divider()

# ---------------- RESUME ANALYSIS ----------------
elif page == "Resume Analysis":
    st.header("🧠 Skill Gap Analysis")

    resume = st.text_area("Paste Resume")
    jobs = load_jobs()

    if st.button("Analyze Skill Gaps"):
        if not jobs:
            st.warning("⚠️ Add jobs first")
        elif not resume:
            st.warning("⚠️ Paste resume")
        else:
            all_desc = " ".join([j["description"] for j in jobs])
            gaps = get_skill_gaps(resume, all_desc)
            st.write(gaps)

# ---------------- OPTIMIZER ----------------
elif page == "Resume Optimizer":
    st.header("✨ Resume Optimization")

    resume = st.text_area("Paste Resume")

    if st.button("Optimize Resume"):
        if not resume:
            st.warning("⚠️ Paste resume")
        else:
            improved = optimize_resume(resume)
            st.write(improved)

# ---------------- COVER LETTER ----------------
elif page == "Cover Letter":
    st.header("📄 Cover Letter Generator")

    resume = st.text_area("Resume")
    job_desc = st.text_area("Job Description")

    if st.button("Generate Cover Letter"):
        if not resume or not job_desc:
            st.warning("⚠️ Fill both fields")
        else:
            letter = generate_cover_letter(resume, job_desc)
            st.write(letter)

# ---------------- INTERVIEW ----------------
elif page == "Interview Prep":
    st.header("🎯 Interview Preparation")

    job_desc = st.text_area("Job Description")

    if st.button("Generate Questions"):
        if not job_desc:
            st.warning("⚠️ Paste job description")
        else:
            qna = generate_interview_questions(job_desc)
            st.write(qna)

# ---------------- TRACKER ----------------
elif page == "Tracker":
    st.header("📌 Application Tracker")

    jobs = load_jobs()

    if not jobs:
        st.info("No jobs added yet.")
    else:
        for i, job in enumerate(jobs):
            status = st.selectbox(
                f"{job['title']}",
                ["Not Applied", "Applied", "Interview"],
                index=["Not Applied", "Applied", "Interview"].index(job["status"]),
                key=i
            )
            update_status(i, status)

# ---------------- AI CHAT ----------------
elif page == "AI Chat":
    st.header("💬 Career AI Chat")

    query = st.text_input("Ask anything about jobs, resumes, or interviews")

    if st.button("Ask AI"):
        if not query:
            st.warning("⚠️ Enter a question")
        else:
            response = chat_with_ai(query)
            st.write(response)
