import { evaluate } from './calculator.js';
/** Calculator display element. */
let display;
/** Current expression being built. */
let expression = '';
/** Whether the last action was evaluation (for reset behavior). */
let justEvaluated = false;
/** Initializes the calculator UI. */
function init() {
    display = document.getElementById('display');
    setupEventListeners();
    updateDisplay();
}
/** Sets up click handlers for all calculator buttons. */
function setupEventListeners() {
    document.querySelectorAll('[data-value]').forEach((btn) => {
        btn.addEventListener('click', () => handleInput(btn.dataset.value));
    });
    document.getElementById('clear')?.addEventListener('click', clear);
    document.getElementById('backspace')?.addEventListener('click', backspace);
    document.getElementById('equals')?.addEventListener('click', calculate);
    // Keyboard support
    document.addEventListener('keydown', handleKeyboard);
}
/** Handles keyboard input. */
function handleKeyboard(e) {
    const key = e.key;
    if (/^[0-9.]$/.test(key)) {
        handleInput(key);
    }
    else if (['+', '-', '*', '/', '%', '^'].includes(key)) {
        handleInput(key);
    }
    else if (key === '(' || key === ')') {
        handleInput(key);
    }
    else if (key === 'Enter' || key === '=') {
        e.preventDefault();
        calculate();
    }
    else if (key === 'Backspace') {
        backspace();
    }
    else if (key === 'Escape' || key === 'c' || key === 'C') {
        clear();
    }
}
/** Handles number and operator input. */
function handleInput(value) {
    if (justEvaluated && /^[0-9.]$/.test(value)) {
        expression = '';
    }
    justEvaluated = false;
    expression += value;
    updateDisplay();
}
/** Clears the display and expression. */
function clear() {
    expression = '';
    justEvaluated = false;
    updateDisplay();
}
/** Removes the last character from the expression. */
function backspace() {
    expression = expression.slice(0, -1);
    justEvaluated = false;
    updateDisplay();
}
/** Evaluates the current expression. */
function calculate() {
    if (!expression)
        return;
    try {
        const result = evaluate(expression);
        expression = formatResult(result);
        justEvaluated = true;
        updateDisplay();
        animateResult();
    }
    catch (err) {
        showError(err.message);
    }
}
/** Formats a number result, removing unnecessary decimals. */
function formatResult(num) {
    if (Number.isInteger(num)) {
        return num.toString();
    }
    // Round to 10 decimal places to avoid floating point issues
    return parseFloat(num.toFixed(10)).toString();
}
/** Updates the display with the current expression. */
function updateDisplay() {
    display.value = expression || '0';
}
/** Shows an error message briefly on the display. */
function showError(message) {
    const originalValue = display.value;
    display.value = `Error: ${message}`;
    display.classList.add('error');
    setTimeout(() => {
        display.value = originalValue;
        display.classList.remove('error');
    }, 1500);
}
/** Adds a brief animation when showing result. */
function animateResult() {
    display.classList.add('result');
    setTimeout(() => display.classList.remove('result'), 150);
}
// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', init);
//# sourceMappingURL=app.js.map