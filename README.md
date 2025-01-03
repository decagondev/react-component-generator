# React Component Generator 🎨

A CLI tool powered by LangChain and OpenAI to generate TypeScript React components with TailwindCSS styling.

## Features ✨

- TypeScript React components with proper type definitions
- TailwindCSS styling integration
- JSDoc documentation
- Interactive REPL interface
- Component generation with customizable:
  - Props
  - Behavior
  - Styling
  - Usage examples

## Prerequisites 🛠️

- Python 3.7+
- OpenAI API key
- LangChain
- TypeScript/React development environment

## Installation 📦

```bash
pip install langchain openai
export OPENAI_API_KEY='your-api-key'
```

## Usage 💻

Run the REPL interface:

```bash
python component_generator.py
```

Follow the prompts to specify your component details:
- Component Name
- Purpose
- Props
- Behavior
- Styling preferences
- Usage examples

The generator will create a `.tsx` file with your component.

## Example Output 📝

```typescript
// Button.tsx
import React from 'react';

interface ButtonProps {
  label: string;
  onClick: () => void;
  variant?: 'primary' | 'secondary';
}

export const Button: React.FC<ButtonProps> = ...
```

## Technical Details 🔧

- Uses OpenAI's Chat model (temperature: 0.5)
- Components include TypeScript types
- TailwindCSS utility-first styling
- Full JSDoc documentation
- Includes usage examples as comments

## License 📄

MIT
