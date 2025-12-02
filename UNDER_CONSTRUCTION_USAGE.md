# Under Construction Templates - Usage Guide

## 1. Full Page Under Construction (Inheritance Method)
**File:** `templates/under_construction.html`

This is the best way to create new pages that are under construction. It works just like `base.html` but pre-fills the content with the under construction design.

**How to use in a new template file:**
Create your new file (e.g., `templates/MyNewTopic.html`) and add this code:

```html
{% extends "under_construction.html" %}

{% block title %}My New Topic - K4Maths{% endblock %}

{% block construction_title %}My New Topic Coming Soon{% endblock %}

{% block construction_message %}
We are currently building this specific topic. It will include interactive graphs and practice questions.
{% endblock %}
```

Then in your `app.py`:
```python
@app.route("/MyNewTopic")
def my_new_topic():
    return render_template("MyNewTopic.html")
```

## 2. Quick Redirect (No new file needed)
**File:** `templates/pages/UnderConstruction.html`
**Route:** `/UnderConstruction`

Use this if you don't want to create a specific HTML file yet.

**Example usage in Flask route:**
```python
@app.route("/SomeNewTopic")
def some_new_topic():
    return render_template("pages/UnderConstruction.html")
```

## 3. Reusable Under Construction Component
**File:** `templates/components/under-construction.html`

Use this component inside any existing page where you want to show an "under construction" section mixed with other content.

### Basic Usage (default message):
```html
{% include 'components/under-construction.html' %}
```

### With Custom Message:
```html
{% set custom_message = "Your custom message about what's coming for this specific topic..." %}
{% include 'components/under-construction.html' %}
```

### With Custom Message and Buttons:
```html
{% set custom_message = "Custom message here..." %}
{% set show_buttons = true %}
{% include 'components/under-construction.html' %}
```

## Features

### Full Page Version:
- Complete page layout with back-to-home button
- Progress bar animation
- Feature list with what's coming
- Multiple action buttons (Home, Browse Topics, Contact)
- Responsive design
- SEO-friendly meta tags

### Component Version:
- Smaller, embeddable design
- Can be placed anywhere in a template
- Customizable message
- Optional action buttons
- Animated icons
- Consistent styling with the main site

## Styling

Both versions use:
- Your site's CSS variables (--accent-blue, --primary-purple, etc.)
- Consistent K4Maths color scheme
- Smooth animations and transitions
- Mobile-responsive design
- Dark theme compatibility

## Quick Examples

### Create a specific under construction page:
Create `templates/AdvancedCalculus.html`:
```html
{% extends "under_construction.html" %}
{% block title %}Advanced Calculus{% endblock %}
{% block construction_title %}Calculus Module In Progress{% endblock %}
```

### Add under construction section to existing page:
```html
{% extends "base.html" %}
{% block content %}
<h1>My Topic</h1>
<p>Some existing content...</p>

<!-- Under construction section -->
{% set custom_message = "Advanced exercises and video tutorials coming soon!" %}
{% include 'components/under-construction.html' %}

<p>More existing content...</p>
{% endblock %}
```

This makes it easy to maintain a consistent look across your site while clearly communicating to users what's in development!