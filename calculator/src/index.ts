import * as readline from 'readline';
import { Calculator, evaluate } from './calculator.js';

const calculator = new Calculator();

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

/** Prints the welcome message and available commands. */
function printHelp(): void {
  console.log(`
╔════════════════════════════════════════════════════════════╗
║                    TypeScript Calculator                   ║
╠════════════════════════════════════════════════════════════╣
║  Modes:                                                    ║
║    • Expression: Type math expressions (e.g., 2 + 3 * 4)   ║
║    • Chained: Use result with operations                   ║
║                                                            ║
║  Operations: + - * / ^ (power) % (modulo)                  ║
║  Commands:                                                 ║
║    clear   - Reset to 0                                    ║
║    result  - Show current result                           ║
║    sqrt    - Square root of result                         ║
║    neg     - Negate result                                 ║
║    help    - Show this message                             ║
║    exit    - Quit calculator                               ║
╚════════════════════════════════════════════════════════════╝
`);
}

/** Processes a single user command or expression. */
function processInput(input: string): void {
  const trimmed = input.trim().toLowerCase();

  if (!trimmed) return;

  switch (trimmed) {
    case 'exit':
    case 'quit':
    case 'q':
      console.log('Goodbye!');
      rl.close();
      process.exit(0);
      break;
    case 'help':
    case 'h':
    case '?':
      printHelp();
      break;
    case 'clear':
    case 'c':
      calculator.reset();
      console.log('= 0');
      break;
    case 'result':
    case 'r':
      console.log(`= ${calculator.getResult()}`);
      break;
    case 'sqrt':
      try {
        calculator.sqrt();
        console.log(`= ${calculator.getResult()}`);
      } catch (err) {
        console.log(`Error: ${(err as Error).message}`);
      }
      break;
    case 'neg':
      calculator.negate();
      console.log(`= ${calculator.getResult()}`);
      break;
    default:
      evaluateInput(input.trim());
  }
}

/** Evaluates mathematical expressions or chained operations. */
function evaluateInput(input: string): void {
  try {
    // Check for chained operations starting with an operator
    const chainMatch = input.match(/^([+\-*/^%])\s*(.+)$/);
    if (chainMatch) {
      const [, op, valueStr] = chainMatch;
      const value = evaluate(valueStr);
      applyOperation(op, value);
      return;
    }

    // Evaluate as a full expression
    const result = evaluate(input);
    calculator.reset(result);
    console.log(`= ${result}`);
  } catch (err) {
    console.log(`Error: ${(err as Error).message}`);
  }
}

/** Applies a chained operation to the current result. */
function applyOperation(op: string, value: number): void {
  switch (op) {
    case '+':
      calculator.add(value);
      break;
    case '-':
      calculator.subtract(value);
      break;
    case '*':
      calculator.multiply(value);
      break;
    case '/':
      calculator.divide(value);
      break;
    case '^':
      calculator.power(value);
      break;
    case '%':
      calculator.modulo(value);
      break;
  }
  console.log(`= ${calculator.getResult()}`);
}

/** Main entry point. */
function main(): void {
  printHelp();
  console.log('Current result: 0\n');

  rl.setPrompt('> ');
  rl.prompt();

  rl.on('line', (line) => {
    processInput(line);
    rl.prompt();
  });

  rl.on('close', () => {
    console.log('\nGoodbye!');
    process.exit(0);
  });
}

main();
