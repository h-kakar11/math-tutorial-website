from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Secret key for flash messages
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Optimize Flask
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # 1 year cache for production
    app.config['TEMPLATES_AUTO_RELOAD'] = False
else:
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching in development
    app.config['TEMPLATES_AUTO_RELOAD'] = True

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USERNAME')  # Your email
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')  # Your app password
app.config['MAIL_DEFAULT_SENDER'] = ('K4Maths Contact Form', os.environ.get('EMAIL_USERNAME'))

# Initialize Flask-Mail
mail = Mail(app)

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
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Create email message
        msg = Message(
            subject=f'SQWCKDS K4Maths Contact Form - Message from {name} at {email}',
            recipients=[os.environ.get('EMAIL_USERNAME')],  # Send to yourself
            body=f'''
K4Maths Contact Form Submission
================================

Name: {name}
Email: {email}

Message:
{message}

---
This email was sent from the K4Maths website contact form.
Visit: https://k4maths.com

Best regards,
K4Maths Enhanced Automated Systems
            '''.strip()
        )
        
        # Send email
        mail.send(msg)
        
        flash('Thank you! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact_me'))
        
    except Exception as e:
        flash('Sorry, there was an error sending your message. Please try again.', 'error')
        print(f"Email error: {e}")  # For debugging
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

@app.route("/ArgandDiagrams")
def argand_diagrams():
    return render_template("components/ArgandDiagrams.html")

@app.route("/RootsOfPolynomials")
def roots_of_polynomials():
    return render_template("components/RootsOfPolynomials.html")

@app.route("/VolumesOfRevolution")
def volumes_of_revolution():
    return render_template("components/VolumesOfRevolution.html")

@app.route("/LinearTransformations")
def linear_transformations():
    return render_template("components/LinearTransformations.html")

@app.route("/ProofByInduction")
def proof_by_induction():
    return render_template("components/ProofByInduction.html")

@app.route("/BinomialExpansion")
def binomial_expansion():
    return render_template("components/BinomialExpansionMath.html")

@app.route("/Circles")
def circles():
    return render_template("components/CircleMath.html")

@app.route("/Differentiation")
def differentiation():
    return render_template("components/DifferentiationMath.html")

@app.route("/EquationsAndInequalities")
def equations_and_inequalities():
    return render_template("components/EquationsAndInequalitiesMath.html")

@app.route("/ExponentialsAndLogarithms")
def exponentials_and_logarithms():
    return render_template("components/LogsAndExponentMath.html")

@app.route("/GraphsAndTransformations")
def graphs_and_transformations():
    return render_template("components/GraphsAndTransformationsMath.html")

@app.route("/Integration")
def integration():
    return render_template("components/IntegrationMath.html")

@app.route("/Matrices")
def matrices():
    return render_template("components/Matrices.html")

@app.route("/Quadratics")
def quadratics():
    return render_template("components/QuadraticsMath.html")

@app.route("/Radians")
def radians():
    return render_template("components/RadiansMath.html")

@app.route("/RationalisingDenominators")
def rationalising_denominators():
    return render_template("components/RationalisingDenominatorsMath.html")

@app.route("/StraightLineGraphs")
def straight_line_graphs():
    return render_template("components/StraightLineGraphsMath.html")

@app.route("/TrigonometricIdentitiesAndEquations")
def trigonometric_identities_and_equations():
    return render_template("components/TrigonometricIdentitiesAndEquationsMath.html")

@app.route("/TrigonometricRatios")
def trigonometric_ratios():
    return render_template("components/TrigonometricRatiosMath.html")

@app.route("/Vectors")
def vectors():
    return render_template("components/VectorsMath.html")

# ============================================
# Complex Numbers PAGES (lessons / folder)
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

# ============================================
# SERIES (components/ folder)
# ============================================

@app.route("/SeriesBasics")
def series_basics():
    return render_template("SeriesCP1/SeriesBasics.html")

@app.route("/Series")
def series():
    return render_template("components/Series.html")

@app.route("/SquareSeries")
def square_series():
    return render_template("SeriesCP1/SquareSeries.html")

@app.route("/CubicSeries")
def cubic_series():
    return render_template("SeriesCP1/CubicSeries.html")

# ========================================================================================
# MATRICES (components/ folder)
# ============================================

@app.route("/IntroductionToMatrices")
def introduction_to_matrices():
    return render_template("MatrixCP1/IntroductionToMatrices.html")

@app.route("/MatrixMultiplication")
def matrix_multiplication():
    return render_template("MatrixCP1/MatrixMultiplication.html")

@app.route("/Determinants")
def determinants():
    return render_template("MatrixCP1/Determinants.html")

@app.route("/Inverting2x2Matrix")
def inverting_2x2_matrix():
    return render_template("MatrixCP1/Inverting2x2Matrix.html")

@app.route("/Inverting3x3Matrix")
def inverting_3x3_matrix():
    return render_template("MatrixCP1/Inverting3x3Matrix.html")

@app.route("/SolvingSystemsWithMatrices")
def solving_systems_with_matrices():
    return render_template("MatrixCP1/SolvingSystemsWithMatrices.html")
#========================================================================================
# ROOTS OF POLYNOMIALS (components/ folder)
# ========================================================================================.
@app.route("/RootsOfQuarticEquation")
def roots_of_quartic_equation():
    return render_template("RootsOfPolynomialsCP1/RootsOfQuarticEquation.html") 

@app.route("/ExpressionsRelatingToRoots")
def expressions_relating_to_roots():    
    return render_template("RootsOfPolynomialsCP1/ExpressionsRelatingToRoots.html")

@app.route("/LinearTransformationsOfRoots")
def linear_transformations_of_roots():
    return render_template("RootsOfPolynomialsCP1/LinearTransformationsOfRoots.html")

@app.route("/RootsOfCubicEquation")
def roots_of_cubic_equation():
    return render_template("RootsOfPolynomialsCP1/RootsOfCubicEquation.html")

@app.route("/RootsOfQuadraticEquation")
def roots_of_quadratic_equation():
    return render_template("RootsOfPolynomialsCP1/RootsOfQuadraticEquation.html")
#========================================================================================
# VOLUMES OF REVOLUTION (components/ folder)
# ========================================================================================.

@app.route("/VolumesAroundXAndYAxis")
def volumes_around_x_and_y_axis():
    return render_template("VolumesOfRevolutionCP1/VolumesAroundXAndYAxis.html")

@app.route("/AddingAndSubtractingVolumes")
def adding_and_subtracting_volumes():
    return render_template("VolumesOfRevolutionCP1/AddingAndSubtractingVolumes.html")

@app.route("/ModellingWithVolumes")
def modelling_with_volumes():
    return render_template("VolumesOfRevolutionCP1/ModellingWithVolumes.html")


#========================================================================================
# vectors cp1 (components/ folder)
# ========================================================================================.

@app.route("/EquationOfLine3D")
def equation_of_line_3d():
    return render_template("VectorsCP1/EquationOfLine3D.html")

@app.route("/ScalarProduct")
def scalar_product():
    return render_template("VectorsCP1/ScalarProduct.html")

@app.route("/VectorsCP1")
def vectors_cp1():
    return render_template("VectorsCP1/VectorsCP1.html")

#========================================================================================
# LEGACY ROUTES (for backwards compatibility)
# ============================================

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

