# Under Construction Templates - Usage Guide

## 1. Full Page Under Construction
**File:** `templates/pages/UnderConstruction.html`
**Route:** `/UnderConstruction`

Use this for entire pages that are under construction.

**Example usage in Flask route:**
```python
@app.route("/SomeNewTopic")
def some_new_topic():
    return render_template("pages/UnderConstruction.html")
```

## 2. Reusable Under Construction Component
**File:** `templates/components/under-construction.html`

Use this component inside any existing page where you want to show an "under construction" section.

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

### Replace a topic page temporarily:
```python
@app.route("/NewTopic")
def new_topic():
    return render_template("pages/UnderConstruction.html")
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