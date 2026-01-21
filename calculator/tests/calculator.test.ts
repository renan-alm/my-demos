import { describe, it, expect, beforeEach } from 'vitest';
import { Calculator, evaluate } from '../src/calculator';

describe('Calculator', () => {
    let calculator: Calculator;

    beforeEach(() => {
        calculator = new Calculator();
    });

    it('should initialize with 0 by default', () => {
        expect(calculator.getResult()).toBe(0);
    });

    it('should initialize with a specific value', () => {
        const calc = new Calculator(10);
        expect(calc.getResult()).toBe(10);
    });

    it('should add numbers correctly', () => {
        calculator.add(5);
        expect(calculator.getResult()).toBe(5);
        calculator.add(3.5);
        expect(calculator.getResult()).toBe(8.5);
    });

    it('should subtract numbers correctly', () => {
        calculator.reset(10);
        calculator.subtract(4);
        expect(calculator.getResult()).toBe(6);
        calculator.subtract(7);
        expect(calculator.getResult()).toBe(-1);
    });

    it('should multiply numbers correctly', () => {
        calculator.reset(2);
        calculator.multiply(3);
        expect(calculator.getResult()).toBe(6);
        calculator.multiply(-2);
        expect(calculator.getResult()).toBe(-12);
    });

    it('should divide numbers correctly', () => {
        calculator.reset(10);
        calculator.divide(2);
        expect(calculator.getResult()).toBe(5);
    });

    it('should throw error when dividing by zero', () => {
        calculator.reset(10);
        expect(() => calculator.divide(0)).toThrow('Cannot divide by zero');
    });

    it('should calculate power correctly', () => {
        calculator.reset(2);
        calculator.power(3);
        expect(calculator.getResult()).toBe(8);
    });

    it('should calculate square root correctly', () => {
        calculator.reset(9);
        calculator.sqrt();
        expect(calculator.getResult()).toBe(3);
    });

    it('should throw error when calculating square root of negative number', () => {
        calculator.reset(-4);
        expect(() => calculator.sqrt()).toThrow('Cannot calculate square root of negative number');
    });

    it('should calculate modulo correctly', () => {
        calculator.reset(10);
        calculator.modulo(3);
        expect(calculator.getResult()).toBe(1);
    });

    it('should throw error when calculating modulo by zero', () => {
        calculator.reset(10);
        expect(() => calculator.modulo(0)).toThrow('Cannot perform modulo by zero');
    });

    it('should negate the result', () => {
        calculator.reset(5);
        calculator.negate();
        expect(calculator.getResult()).toBe(-5);
        calculator.negate();
        expect(calculator.getResult()).toBe(5);
    });

    it('should reset the calculator', () => {
        calculator.add(10);
        calculator.reset();
        expect(calculator.getResult()).toBe(0);
        calculator.reset(5);
        expect(calculator.getResult()).toBe(5);
    });

    it('should support method chaining', () => {
        calculator.reset(0)
            .add(5)
            .multiply(2)
            .subtract(2)
            .divide(4); // (0 + 5) * 2 - 2 / 4 = 2 (Wait: ((5)*2)-2)/4 = 8/4=2 
        expect(calculator.getResult()).toBe(2);
    });
});

describe('evaluate', () => {
    it('should evaluate simple addition', () => {
        expect(evaluate('2 + 3')).toBe(5);
    });

    it('should evaluate simple subtraction', () => {
        expect(evaluate('10 - 4')).toBe(6);
    });

    it('should evaluate simple multiplication', () => {
        expect(evaluate('3 * 4')).toBe(12);
    });

    it('should evaluate simple division', () => {
        expect(evaluate('10 / 2')).toBe(5);
    });

    it('should respect operator precedence (multiplication/division over addition/subtraction)', () => {
        expect(evaluate('2 + 3 * 4')).toBe(14); // 2 + 12
        expect(evaluate('10 - 6 / 2')).toBe(7); // 10 - 3
    });

    it('should handle parentheses', () => {
        expect(evaluate('(2 + 3) * 4')).toBe(20);
        expect(evaluate('2 * (3 + 4)')).toBe(14);
    });

    it('should evaluate power operator', () => {
        expect(evaluate('2 ^ 3')).toBe(8);
        expect(evaluate('2 + 2 ^ 3')).toBe(10);
    });

    it('should evaluate modulo operator', () => {
        expect(evaluate('10 % 3')).toBe(1);
    });

    it('should handle complex expressions', () => {
        expect(evaluate('((2 + 3) * 4) / 2')).toBe(10); 
    });

    it('should handle decimals', () => {
        expect(evaluate('2.5 + 3.5')).toBe(6);
    });

    it('should throw error for invalid expressions', () => {
        expect(() => evaluate('2 + ')).toThrow(); // The regex might or might not catch this depending on implementation detail, but logic should fail or throw. 
        // Based on `calculator.ts`, `tokenize` matches valid parts. if nothing matches it throws. 
        // `parseExpression` calls implementation details I haven't seen fully. 
        // Let's stick safe tests or verify implementation.
    });
    
    // I'll read the rest of `calculator.ts` to see how `parseExpression` works to write better tests for errors and precedence if needed.
    // For now, let's keep basic error checks.
});
