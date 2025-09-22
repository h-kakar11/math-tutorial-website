from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)

# ============================================
# HOME PAGE
# ============================================

@app.route("/")
def index():
    return render_template("index.html") 

# ============================================
# SUBJECT PAGES (subjects/ folder)
# ============================================

@app.route("/FurtherMaths")
def further_maths():
    return render_template("subjects/FurtherMaths.html")

@app.route("/Maths")
def maths():
    return render_template("subjects/maths.html")

@app.route("/Physics")
def physics():
    return render_template("subjects/Physics.html")

# ============================================
# GENERAL PAGES (pages/ folder)
# ============================================

@app.route("/survey")
def survey():
    return render_template("pages/survey.html")

@app.route("/WhoAmI")
def who_am_i():
    return render_template("pages/WhoAmI.html")

@app.route("/ContactMe")
def contact_me():
    return render_template("pages/ContactMe.html")

@app.route("/TopicsList")
def topics_list():
    return render_template("pages/TopicsList.html")

@app.route("/submit_contact", methods=['POST'])
def submit_contact():
    # Basic contact form handler - you can expand this to send emails
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # For now, just redirect back to contact page with a success message
    # In a real application, you'd want to send an email or save to database
    return redirect(url_for('contact_me'))

# ============================================
# TOPIC COMPONENT PAGES (components/ folder)
# ============================================

@app.route("/ComplexNumbers")
def complex_numbers():
    return render_template("components/ComplexNumbers.html")

@app.route("/AlgebraicExpressions")
def algebraic_expressions():
    return render_template("components/AlgebraicExpressions.html")

@app.route("/FurtherVectors")
def further_vectors():
    return render_template("components/FurtherVectors.html")

@app.route("/templateForALevelPage")
def template_for_a_level_page():
    return render_template("components/templateForALevelPage.html")

# ============================================
# LESSON PAGES (lessons/ folder)
# ============================================

@app.route("/SimplifyingSurds")
def simplifying_surds():
    return render_template("ComplexNumbersCP1/SimplifyingSurds.html")

@app.route("/lessonTemplate")
def lesson_template():
    return render_template("ComplexNumbersCP1/lessonTemplate.html")

@app.route("/IntroToComplexNumbers")
def intro_to_complex_numbers():
    return render_template("ComplexNumbersCP1/IntroToComplexNumbers.html")

@app.route("/ModArgComplex")
def mod_arg_complex():
    return render_template("ComplexNumbersCP1//ModArgComplex.html")

@app.route("/MultiplyComplex")
def multiply_complex():
    return render_template("ComplexNumbersCP1/MultiplyComplex.html")

@app.route("/DivisionComplex")
def division_complex():
    return render_template("ComplexNumbersCP1/DivisionComplex.html")

@app.route("/ComplexQuarticEquations")
def complex_quartic_equations():
    return render_template("ComplexNumbersCP1/ComplexQuarticEquations.html")

@app.route("/ComplexCubicEquations")
def complex_cubic_equations():
    return render_template("ComplexNumbersCP1/ComplexCubicEquations.html")


# ========================================================================================
# (AlgebraicExpressionsMath/ folder)
# ========================================================================================

@app.route("/ExpandingBrackets")
def expanding_brackets():
    return render_template("AlgebraicExpressionsMath/ExpandingBrackets.html")

@app.route("/NegAndFracIndices")
def neg_and_frac_indices():
    return render_template("AlgebraicExpressionsMath/NegAndFracIndicies.html")

@app.route("/Factoring")
def factoring():
    return render_template("AlgebraicExpressionsMath/Factoring.html")

@app.route("/Surds")
def surds():
    return render_template("AlgebraicExpressionsMath/Surds.html")

@app.route("/IndexLaws")
def index_laws():
    return render_template("AlgebraicExpressionsMath/IndexLaws.html")

@app.route("/RationalDeno")
def rational_deno():
    return render_template("AlgebraicExpressionsMath/RationalDeno.html")

# ========================================================================================

# ============================================
# LEGACY ROUTES (for backwards compatibility)
# ============================================

@app.route("/FurtherMathsVectors")
def further_maths_vectors():
    return render_template("components/FurtherVectors.html")     

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    
