## Core Requirements

- Avoid unnecessary verbosity. Keep it concise.
- If a yes/no question is asked, answer with a simple "yes" or "no" before providing additional context.
- Use @terminal when answering questions about Git.

## Custumisation Instructions
- If I write "rc", it means "remove comments of the current file".

## Code Quality Requirements

- Use clear, descriptive variable and function names
- Write unit tests for core functionality
- Keep functions focused and manageable (generally under 50 lines)
- Use error handling patterns consistently
- Keep all lines, including comments, under 120 characters
- For any code use the following configuration files (if they are present): `<root>/.editorconfig`
- For all JavaScript/TypeScript/Node.js code, ensure the formatting adheres to the rules specified in the following files (if they are present):
  - `<root>/eslint.config.js`
  - `<root>/prettier.config.js` and `<root>/.prettierignore`

## Documentation Requirements

- Follow standard JavaScript/TypeScript/Node.js (JSDoc/HereDoc) conventions and best practices
- Add JSDoc/HereDoc if missing, but keep it short. Do not align it.
- Add comments to explain complex logic or non-obvious implementations
- Place inline comments above the code, not on the same line
- Use full sentences for comments
- Never comment in Markdown, except code blocks

