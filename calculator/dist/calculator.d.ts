/**
 * Calculator class providing basic arithmetic operations.
 */
export declare class Calculator {
    private result;
    constructor(initialValue?: number);
    /** Returns the current result. */
    getResult(): number;
    /** Resets the calculator to zero or a specified value. */
    reset(value?: number): this;
    /** Adds a number to the current result. */
    add(value: number): this;
    /** Subtracts a number from the current result. */
    subtract(value: number): this;
    /** Multiplies the current result by a number. */
    multiply(value: number): this;
    /**
     * Divides the current result by a number.
     * @throws Error if dividing by zero.
     */
    divide(value: number): this;
    /** Raises the current result to a power. */
    power(exponent: number): this;
    /** Returns the square root of the current result. */
    sqrt(): this;
    /** Returns the remainder of division by a number. */
    modulo(value: number): this;
    /** Negates the current result. */
    negate(): this;
}
/** Evaluates a simple arithmetic expression string. */
export declare function evaluate(expression: string): number;
//# sourceMappingURL=calculator.d.ts.map