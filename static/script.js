// Calculator and Dark Mode JavaScript
class Calculator {
    constructor() {
        this.display = document.getElementById('display');
        this.currentInput = '';
        this.shouldResetDisplay = false;
        this.memory = 0;
        this.angleMode = 'deg';
        
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        // Calculator dropdown toggle
        const calcToggle = document.getElementById('calculator-toggle');
        const calcDropdown = document.getElementById('calculator-dropdown');
        
        if (calcToggle && calcDropdown) {
            calcToggle.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                calcDropdown.classList.toggle('show');
            });

            // Close dropdown when clicking outside
            document.addEventListener('click', (e) => {
                if (!calcDropdown.contains(e.target) && !calcToggle.contains(e.target)) {
                    calcDropdown.classList.remove('show');
                }
            });
        }

        // Calculator button listeners
        document.querySelectorAll('.calculator-dropdown button').forEach(button => {
            button.addEventListener('click', (e) => {
                e.stopPropagation();
                this.handleButtonClick(button);
            });
        });

        // Angle mode radio buttons
        document.querySelectorAll('input[name="angle"]').forEach(radio => {
            radio.addEventListener('change', () => {
                this.angleMode = radio.value;
            });
        });
    }

    handleButtonClick(button) {
        const func = button.getAttribute('data-func');
        
        if (button.classList.contains('number')) {
            this.inputNumber(func);
        } else if (button.classList.contains('operator')) {
            this.inputOperator(func);
        } else if (button.classList.contains('function')) {
            this.inputFunction(func);
        } else if (button.classList.contains('equal')) {
            this.calculate();
        }
    }

    inputNumber(num) {
        if (this.shouldResetDisplay) {
            this.currentInput = '';
            this.shouldResetDisplay = false;
        }
        
        if (num === '.' && this.currentInput.includes('.')) return;
        
        this.currentInput += num;
        this.updateDisplay();
    }

    inputOperator(op) {
        if (this.shouldResetDisplay) {
            this.shouldResetDisplay = false;
        }
        
        // Handle special operators
        switch(op) {
            case '+/-':
                if (this.currentInput) {
                    this.currentInput = this.currentInput.startsWith('-') ? 
                        this.currentInput.slice(1) : '-' + this.currentInput;
                }
                break;
            case 'x²':
                this.inputFunction('x²');
                return;
            case 'x³':
                this.inputFunction('x³');
                return;
            case '1/x':
                this.inputFunction('1/x');
                return;
            default:
                this.currentInput += op;
        }
        
        this.updateDisplay();
    }

    inputFunction(func) {
        try {
            let result;
            const current = parseFloat(this.currentInput) || 0;
            
            switch(func) {
                case 'sin':
                    result = Math.sin(this.toRadians(current));
                    break;
                case 'cos':
                    result = Math.cos(this.toRadians(current));
                    break;
                case 'tan':
                    result = Math.tan(this.toRadians(current));
                    break;
                case 'asin':
                    result = this.fromRadians(Math.asin(current));
                    break;
                case 'acos':
                    result = this.fromRadians(Math.acos(current));
                    break;
                case 'atan':
                    result = this.fromRadians(Math.atan(current));
                    break;
                case 'ln':
                    result = Math.log(current);
                    break;
                case 'log':
                    result = Math.log10(current);
                    break;
                case 'sqrt':
                    result = Math.sqrt(current);
                    break;
                case 'exp':
                    result = Math.exp(current);
                    break;
                case 'x²':
                    result = current * current;
                    break;
                case 'x³':
                    result = current * current * current;
                    break;
                case '1/x':
                    result = 1 / current;
                    break;
                case 'M+':
                    this.memory += current;
                    return;
                case 'MR':
                    this.currentInput = this.memory.toString();
                    this.updateDisplay();
                    return;
                case 'C':
                    this.clear();
                    return;
                default:
                    return;
            }
            
            this.currentInput = this.formatResult(result);
            this.shouldResetDisplay = true;
            this.updateDisplay();
        } catch (error) {
            this.currentInput = 'Error';
            this.shouldResetDisplay = true;
            this.updateDisplay();
        }
    }

    calculate() {
        try {
            // Handle power operations
            let expression = this.currentInput.replace(/\^/g, '**');
            expression = expression.replace(/×/g, '*');
            expression = expression.replace(/÷/g, '/');
            
            // Evaluate the expression
            let result = Function('"use strict"; return (' + expression + ')')();
            
            this.currentInput = this.formatResult(result);
            this.shouldResetDisplay = true;
            this.updateDisplay();
        } catch (error) {
            this.currentInput = 'Error';
            this.shouldResetDisplay = true;
            this.updateDisplay();
        }
    }

    clear() {
        this.currentInput = '';
        this.shouldResetDisplay = false;
        this.updateDisplay();
    }

    formatResult(result) {
        if (typeof result !== 'number' || !isFinite(result)) {
            return 'Error';
        }
        
        // Round to avoid floating point precision issues
        if (Math.abs(result) < 1e-10) {
            return '0';
        }
        
        // Format very large or very small numbers
        if (Math.abs(result) > 1e10 || (Math.abs(result) < 1e-6 && result !== 0)) {
            return result.toExponential(6);
        }
        
        return parseFloat(result.toPrecision(12)).toString();
    }

    updateDisplay() {
        if (this.display) {
            this.display.textContent = this.currentInput || '0';
        }
    }

    toRadians(degrees) {
        return this.angleMode === 'deg' ? degrees * (Math.PI / 180) : degrees;
    }

    fromRadians(radians) {
        return this.angleMode === 'deg' ? radians * (180 / Math.PI) : radians;
    }
}

// Dark Mode is now permanent - no toggle needed
class DarkMode {
    constructor() {
        this.init();
    }

    init() {
        // Always apply dark mode
        document.body.classList.add('dark-mode');
        
        // Remove any toggle elements if they exist
        const toggle = document.getElementById('dark-mode-toggle');
        if (toggle) {
            toggle.style.display = 'none';
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize calculator
    new Calculator();
    
    // Initialize dark mode
    new DarkMode();
    
    // Initialize topic filter
    initializeTopicFilter();
});

// Topic Filter Functionality
function initializeTopicFilter() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const topicItems = document.querySelectorAll('#maths-topics-list li[data-category]');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.getAttribute('data-filter');
            
            // Update active button
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            // Filter topics with animation
            filterTopics(filter, topicItems);
        });
    });
}

function filterTopics(filter, items) {
    // Clear any existing timeouts to prevent memory leaks
    window.filterTimeouts?.forEach(timeout => clearTimeout(timeout));
    window.filterTimeouts = [];
    
    items.forEach((item, index) => {
        const category = item.getAttribute('data-category');
        const shouldShow = filter === 'all' || category === filter;
        
        if (shouldShow) {
            // Show item immediately instead of staggered animation to reduce memory usage
            item.classList.remove('hidden', 'fadeOut');
            item.style.display = '';
        } else {
            // Hide item immediately
            item.classList.add('hidden');
            item.style.display = 'none';
        }
    });
}


//
//------------------------------------------------------------------------------------
//

// Removed jQuery rolldown animations that were causing memory leaks