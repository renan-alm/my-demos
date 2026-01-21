/**
 * Calculator class providing basic arithmetic operations.
 */
export class Calculator {
  private result: number;

  constructor(initialValue: number = 0) {
    this.result = initialValue;
  }

  /** Returns the current result. */
  getResult(): number {
    return this.result;
  }

  /** Resets the calculator to zero or a specified value. */
  reset(value: number = 0): this {
    this.result = value;
    return this;
  }

  /** Adds a number to the current result. */
  add(value: number): this {
    this.result += value;
    return this;
  }

  /** Subtracts a number from the current result. */
  subtract(value: number): this {
    this.result -= value;
    return this;
  }

  /** Multiplies the current result by a number. */
  multiply(value: number): this {
    this.result *= value;
    return this;
  }

  /**
   * Divides the current result by a number.
   * @throws Error if dividing by zero.
   */
  divide(value: number): this {
    if (value === 0) {
      throw new Error('Cannot divide by zero');
    }
    this.result /= value;
    return this;
  }

  /** Raises the current result to a power. */
  power(exponent: number): this {
    this.result = Math.pow(this.result, exponent);
    return this;
  }

  /** Returns the square root of the current result. */
  sqrt(): this {
    if (this.result < 0) {
      throw new Error('Cannot calculate square root of negative number');
    }
    this.result = Math.sqrt(this.result);
    return this;
  }

  /** Returns the remainder of division by a number. */
  modulo(value: number): this {
    if (value === 0) {
      throw new Error('Cannot perform modulo by zero');
    }
    this.result %= value;
    return this;
  }

  /** Negates the current result. */
  negate(): this {
    this.result = -this.result;
    return this;
  }
}

/** Evaluates a simple arithmetic expression string. */
export function evaluate(expression: string): number {
  const tokens = tokenize(expression);
  return parseExpression(tokens);
}

/** Tokenizes an expression into numbers and operators. */
function tokenize(expression: string): string[] {
  const regex = /(\d+\.?\d*|[+\-*/()^%])/g;
  const matches = expression.match(regex);
  if (!matches) {
    throw new Error('Invalid expression');
  }
  return matches;
}

/** Parses and evaluates tokens handling operator precedence. */
function parseExpression(tokens: string[]): number {
  let pos = 0;

  function parseNumber(): number {
    const token = tokens[pos];
    if (token === '(') {
      pos++;
      const result = parseAddSub();
      if (tokens[pos] !== ')') {
        throw new Error('Missing closing parenthesis');
      }
      pos++;
      return result;
    }
    if (token === '-' && (pos === 0 || '(+-*/^%'.includes(tokens[pos - 1]))) {
      pos++;
      return -parseNumber();
    }
    const num = parseFloat(token);
    if (isNaN(num)) {
      throw new Error(`Invalid number: ${token}`);
    }
    pos++;
    return num;
  }

  function parsePower(): number {
    let left = parseNumber();
    while (pos < tokens.length && tokens[pos] === '^') {
      pos++;
      left = Math.pow(left, parseNumber());
    }
    return left;
  }

  function parseMulDiv(): number {
    let left = parsePower();
    while (pos < tokens.length && '*/%'.includes(tokens[pos])) {
      const op = tokens[pos++];
      const right = parsePower();
      if (op === '*') left *= right;
      else if (op === '/') {
        if (right === 0) throw new Error('Cannot divide by zero');
        left /= right;
      } else if (op === '%') {
        if (right === 0) throw new Error('Cannot perform modulo by zero');
        left %= right;
      }
    }
    return left;
  }

  function parseAddSub(): number {
    let left = parseMulDiv();
    while (pos < tokens.length && '+-'.includes(tokens[pos])) {
      const op = tokens[pos++];
      const right = parseMulDiv();
      if (op === '+') left += right;
      else left -= right;
    }
    return left;
  }

  const result = parseAddSub();
  if (pos < tokens.length) {
    throw new Error(`Unexpected token: ${tokens[pos]}`);
  }
  return result;
}
