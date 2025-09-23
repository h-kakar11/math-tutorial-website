from flask import Flask, render_template

app = Flask(__name__)

# ============================================
# MAIN PAGES (Root level templates)
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
# ============================================
# SERIES (components/ folder)
# ============================================

@app.route("/SeriesBasics")
def series_basics():
    return render_template("SeriesCP1/SeriesBasics.html")

@app.route("/SeriesFrontPage")
def series_front_page():
    return render_template("SeriesCP1/SeriesFrontPage.html")


# ============================================
# TOPIC OVERVIEW PAGES (components/ folder)
# ============================================

@app.route("/ComplexNumbers")
def complex_numbers():
    return render_template("components/ComplexNumbers.html")

@app.route("/FurtherVectors")
def lesson1():
    return render_template("components/FurtherVectors.html")

# ============================================
# LESSON PAGES FOR THE COMPLEX NUMBERS YEAR 1 (lessons/ folder)
# ============================================

# Complex Numbers Lessons
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
    return render_template("ComplexNumbersCP1/ModArgComplex.html")

@app.route("/MultiplyComplex")
def multiply_complex():
    return render_template("ComplexNumbersCP1/MultiplyComplex.html")

@app.route("/DivisionComplex")
def division_complex():
    return render_template("ComplexNumbersCP1/DivisionComplex.html")

@app.route("/ComplexCubicEquations")
def complex_cubic_equations():
    return render_template("ComplexNumbersCP1/ComplexCubicEquations.html")

#========================================================================================

# ========================================================================================
# A LEVEL MATHS PAGES (AlgebraicExpressionsMath/ folder)
# ========================================================================================

@app.route("/ExpandingBrackets")
def expanding_brackets():
    return render_template("AlgebraicExpressionsMath/ExpandingBrackets.html")

@app.route("/NegAndFracIndices")
def neg_and_frac_indices():
    return render_template("AlgebraicExpressionsMath/NegAndFracIndices.html")

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

@app.route("/FurtherMathsMatrices")
def further_maths_matrices():
    return render_template("components/FurtherMatrices.html")

@app.route("/FurtherMathsDifferentiation")
def further_maths_differentiation():
    return render_template("components/FurtherDifferentiation.html")

@app.route("/FurtherMathsIntegration")
def further_maths_integration():
    return render_template("components/FurtherIntegration.html")

@app.route("/FurtherMathsNumericalMethods")
def further_maths_numerical_methods():
    return render_template("components/FurtherNumericalMethods.html")

@app.route("/templateForALevelPage")
def template_for_a_level_page():
    return render_template("components/templateForALevelPage.html")

if __name__ == "__main__":
    app.run(debug=True)
