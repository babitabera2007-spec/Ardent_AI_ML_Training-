# 🎓 Babita Bera — AI & Python Student Portfolio

> **B.Sc (Computer Science) · 2nd Year · 4th Semester · Haldia Institute of Management**

A fully responsive, single-page personal portfolio website built with pure **HTML, CSS, and JavaScript** — no frameworks required. Showcases AI/ML projects, technical skills, and workshop experience.

---

## 🔗 Live Preview

> _Deploy to GitHub Pages, Netlify, or Vercel and add your link here._

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Projects](#projects)
- [Skills & Tools](#skills--tools)
- [Workshops](#workshops)
- [Customization Guide](#customization-guide)
- [File Structure](#file-structure)
- [Deployment](#deployment)
- [Contact](#contact)
- [Credits](#credits)

---

## About

This portfolio was created as part of an **AI/ML workshop** (Ardent) to present real, working projects to recruiters and collaborators. The site is designed to be clean, modern, and recruiter-friendly — with a dark glassmorphism aesthetic and smooth animations.

**Portfolio owner:** Babita Bera  
**Location:** Haldia, India  
**Focus areas:** Python · Data Analysis · Machine Learning · AI Automation  
**Open to:** Internships and beginner-level ML collaborations  

---

## ✨ Features

- **Particle canvas background** — animated floating dots and gradient connector lines
- **Typing animation** — cycles through project types in the hero section
- **Scroll-reveal animations** — cards and sections animate in as you scroll
- **Scroll progress bar** — fixed top bar showing reading progress
- **Glassmorphism UI** — frosted-glass cards with gradient blobs and backdrop blur
- **Responsive design** — collapses gracefully on mobile with a hamburger drawer menu
- **Sticky navigation** — blurred header stays at top while scrolling
- **Smooth anchor scrolling** — all nav links scroll smoothly to sections
- **URL query personalization** — pass `?name=YourName` or `?github=URL` to override defaults
- **Zero dependencies** — only Font Awesome (CDN) for icons; everything else is vanilla JS/CSS

---

## 🚀 Projects

### Project 1 · EDA Dashboard (Titanic Dataset)
**Type:** Exploratory Data Analysis · Visual Insights

A beginner-friendly EDA project using a real-world dataset.

| Step | Details |
|------|---------|
| Data loading | Loaded and explored columns using **Pandas** |
| Cleaning | Handled missing values using mean and mode imputation |
| Visualization | Survival count, gender vs survival, age distribution charts |
| Insights | Summarized key findings — presentation-ready |

**Tech:** `Pandas` · `Matplotlib` · `Google Colab`  
**Links:** [Notebook](https://github.com/Programmer-Babita/Ardent_AI_ML_Training-/blob/main/PROJECT-1/Project_1_(EDA).ipynb) · [GitHub Repo](https://github.com/Programmer-Babita/Ardent_AI_ML_Training-/tree/main/PROJECT-1)

---

### Project 2 · House Price Prediction
**Type:** Supervised Machine Learning · Linear Regression

A first end-to-end ML model that learns from training data and predicts house prices on unseen test data.

| Step | Details |
|------|---------|
| Split | Train-test split for unbiased evaluation |
| Model | Trained with **scikit-learn** `LinearRegression` |
| Evaluation | RMSE and R² score computed |
| Visualization | Actual vs Predicted plot · Residual error analysis |

**Tech:** `scikit-learn` · `Pandas` · `Matplotlib` · `Google Colab`  
**Links:** [Notebook](https://github.com/Programmer-Babita/Ardent_AI_ML_Training-/blob/main/PROJECT-2/Project_2_(HPR).ipynb) · [GitHub Repo](https://github.com/Programmer-Babita/Ardent_AI_ML_Training-/tree/main/PROJECT-2)

---

## 🛠 Skills & Tools

| Category | Technologies |
|----------|-------------|
| **Language** | Python (functions, loops, data structures) |
| **Data Handling** | Pandas · Data cleaning · EDA |
| **Visualization** | Matplotlib (bar charts, histograms, scatter plots) |
| **ML** | scikit-learn · Linear Regression · Train-test split |
| **Evaluation** | RMSE · R² Score · Residual analysis |
| **Environment** | Google Colab · GitHub |
| **Web** | HTML5 · CSS3 · Vanilla JavaScript |

---

## 🏫 Workshops

### Ardent – AI & Machine Learning Workshop _(3 Days)_
Practical workshop with theory + live coding in Google Colab. Built portfolio projects covering EDA and Linear Regression model development.

### Code_ScholarEU – AI Development Learning _(Ongoing)_
Learning modern AI development: automation workflows, LLM use-cases, and building real projects step-by-step.  
Mentored by **SK Sahil** (AI Developer & Tutor) — [@code_scholar_eu](https://www.instagram.com/code_scholar_eu/)

---

## ⚙️ Customization Guide

All personal links are managed in a single `LINKS` object at the bottom of `index.html`:

```javascript
const LINKS = {
  githubProfile:    "https://github.com/your-username",
  linkedin:         "https://www.linkedin.com/in/your-profile/",
  project1Repo:     "https://github.com/your-username/project-1",
  project2Repo:     "https://github.com/your-username/project-2",
  project1Notebook: "https://colab.research.google.com/...",
  project2Notebook: "https://colab.research.google.com/...",
  email:            "your.email@example.com"
};
```

### Other things to update

- **Name** — Replace `Babita Bera` in the `<h1>` tag
- **College/Year** — Update the brand subtitle in the `<header>`
- **About cards** — Edit the three "About Me" card descriptions
- **Workshop section** — Add or remove timeline items to match your experience
- **Contact section** — Update the open-to-work message and social links

---

## 📁 File Structure

```
portfolio/
│
├── index.html          # Complete portfolio (HTML + CSS + JS in one file)
└── README.md           # This file
```

All styles and scripts are embedded in `index.html` for zero-setup deployment.

---

## 🌐 Deployment

### GitHub Pages (recommended — free)
1. Push `index.html` and `README.md` to a GitHub repository
2. Go to **Settings → Pages**
3. Set source branch to `main` and folder to `/ (root)`
4. Your site will be live at `https://your-username.github.io/repo-name/`

### Netlify
1. Drag and drop the folder at [netlify.com/drop](https://app.netlify.com/drop)
2. Get an instant live URL — no signup required

### Vercel
1. Import your GitHub repository at [vercel.com](https://vercel.com)
2. Deploy with one click

---

## 📬 Contact

| Platform | Link |
|----------|------|
| **Email** | babitabera2007@gmail.com |
| **GitHub** | [github.com/programmer-babita](https://github.com/programmer-babita) |
| **LinkedIn** | [linkedin.com/in/babita-bera](https://www.linkedin.com/in/babita%20bera/) |
| **Mentor's Instagram** | [@code_scholar_eu](https://www.instagram.com/code_scholar_eu/) |

---

## 🙏 Credits

| Role | Name |
|------|------|
| **Portfolio Owner** | Babita Bera |
| **Mentor & Guide** | SK Sahil (AI Developer & Tutor) |
| **Workshop Organizer** | Ardent AI/ML Training Program |
| **Icons** | [Font Awesome 6](https://fontawesome.com/) (CDN) |
| **Built with** | HTML5 · CSS3 · Vanilla JavaScript |

---

<p align="center">
  © 2025 Babita Bera • Student Portfolio • Built with HTML, CSS & JS •
  <a href="https://github.com/programmer-babita">GitHub</a>
</p>
