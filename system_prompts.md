# React Component Generation Guide

This guide provides examples of prompts for generating React components with TypeScript and TailwindCSS.

## Basic Prompt
```
Generate a reusable React component in TypeScript using TailwindCSS for styling.
```

## Robust Prompt
```
You are a React developer specializing in TypeScript and TailwindCSS. Write a high-quality, reusable, and well-documented React component based on user input. Use TypeScript for type safety, TailwindCSS for styling, and include usage examples and JSDoc comments in the output.
```

## Component Examples

### Button Component

**Prompt:**
```
Create a button component that supports primary and secondary variants and handles a click event.
```

**Implementation:**
```tsx
import React from 'react';

type ButtonProps = {
  /** The label to display on the button */
  label: string;
  /** The variant of the button: "primary" or "secondary" */
  variant: 'primary' | 'secondary';
  /** Function to handle click events */
  onClick: () => void;
};

/**
 * Button Component
 * @param {ButtonProps} props - Props for the button component
 * @returns A styled button component
 */
const Button: React.FC<ButtonProps> = ({ label, variant, onClick }) => {
  const baseStyles = 'px-4 py-2 rounded font-semibold focus:outline-none';
  const variantStyles =
    variant === 'primary'
      ? 'bg-blue-500 text-white hover:bg-blue-600'
      : 'bg-gray-200 text-gray-700 hover:bg-gray-300';

  return (
    <button className={`${baseStyles} ${variantStyles}`} onClick={onClick}>
      {label}
    </button>
  );
};

export default Button;

/**
 * Example Usage:
 *
 * <Button
 *   label="Click Me"
 *   variant="primary"
 *   onClick={() => console.log('Button clicked!')}
 * />
 */
```

### Email Input Component

**Prompt:**
```
Create an input component for email addresses with validation.
```

**Implementation:**
```tsx
import React, { useState } from 'react';

type EmailInputProps = {
  /** Placeholder text for the input field */
  placeholder?: string;
  /** Callback function to handle changes to the email */
  onEmailChange: (email: string) => void;
};

/**
 * Email Input Component
 * @param {EmailInputProps} props - Props for the email input component
 * @returns A styled input component for email addresses
 */
const EmailInput: React.FC<EmailInputProps> = ({ placeholder, onEmailChange }) => {
  const [email, setEmail] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setEmail(value);
    onEmailChange(value);
  };

  return (
    <input
      type="email"
      placeholder={placeholder}
      value={email}
      onChange={handleChange}
      className="px-3 py-2 border rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
    />
  );
};

export default EmailInput;

/**
 * Example Usage:
 *
 * <EmailInput
 *   placeholder="Enter your email"
 *   onEmailChange={(email) => console.log('Email:', email)}
 * />
 */
```

### Card Component

**Prompt:**
```
Create a card component that accepts a title, description, and an image.
```

**Implementation:**
```tsx
import React from 'react';

type CardProps = {
  /** Title of the card */
  title: string;
  /** Description text for the card */
  description: string;
  /** URL of the image for the card */
  imageUrl: string;
};

/**
 * Card Component
 * @param {CardProps} props - Props for the card component
 * @returns A styled card component
 */
const Card: React.FC<CardProps> = ({ title, description, imageUrl }) => {
  return (
    <div className="max-w-sm rounded overflow-hidden shadow-lg">
      <img className="w-full" src={imageUrl} alt={title} />
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">{title}</div>
        <p className="text-gray-700 text-base">{description}</p>
      </div>
    </div>
  );
};

export default Card;

/**
 * Example Usage:
 *
 * <Card
 *   title="Beautiful Sunset"
 *   description="A breathtaking view of the sunset over the mountains."
 *   imageUrl="https://example.com/sunset.jpg"
 * />
 */
```
