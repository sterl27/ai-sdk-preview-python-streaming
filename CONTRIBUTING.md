# Contributing to AI SDK Python Streaming

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## 🚀 Getting Started

### Prerequisites

- Node.js 16+ and pnpm
- Python 3.11+
- Git

### Setup

1. **Fork and clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-sdk-preview-python-streaming.git
   cd ai-sdk-preview-python-streaming
   ```

2. **Install dependencies**

   ```bash
   # Node dependencies
   pnpm install

   # Python virtual environment
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Python dependencies
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. **Set up environment variables**

   ```bash
   cp .env.example .env.local
   # Edit .env.local and add your API keys
   ```

4. **Run the development server**
   ```bash
   pnpm dev
   ```

## 🧪 Testing

### Python Tests

Run Python tests with pytest:

```bash
# Run all tests
pnpm test:python

# Run with verbose output
./venv/bin/pytest tests -v

# Run specific test file
./venv/bin/pytest tests/test_prompt.py -v
```

### Linting and Formatting

**Python:**

```bash
# Format code with black
./venv/bin/black api/ tests/

# Lint with ruff
./venv/bin/ruff check api/ tests/

# Type check with mypy
./venv/bin/mypy api/
```

**JavaScript/TypeScript:**

```bash
# Lint
pnpm lint

# Fix linting issues
pnpm lint:fix

# Format with Prettier
pnpm format

# Check formatting
pnpm format:check
```

## 📝 Code Style

### Python

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Maximum line length: 100 characters
- Use Black for formatting
- Use Ruff for linting

### TypeScript/JavaScript

- Use TypeScript for type safety
- Follow the existing code style
- Use Prettier for formatting
- Maximum line length: 80 characters

## 🔀 Pull Request Process

1. **Create a feature branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write clear, concise commit messages
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**

   ```bash
   pnpm lint
   pnpm format:check
   pnpm test:python
   ```

4. **Commit your changes**

   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

5. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Provide a clear description of the changes
   - Reference any related issues
   - Ensure all tests pass

## 📋 Commit Message Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:

```
feat: add support for image attachments
fix: resolve streaming timeout issue
docs: update README with deployment instructions
```

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Description**: Clear description of the issue
2. **Steps to Reproduce**: Detailed steps to reproduce the behavior
3. **Expected Behavior**: What you expected to happen
4. **Actual Behavior**: What actually happened
5. **Environment**: OS, Node version, Python version, etc.
6. **Screenshots**: If applicable

## 💡 Suggesting Features

Feature suggestions are welcome! Please:

1. Check if the feature has already been suggested
2. Provide a clear use case
3. Explain why this feature would be useful
4. Consider implementation details

## 📚 Documentation

- Update README.md for user-facing changes
- Add inline comments for complex logic
- Update API documentation for endpoint changes
- Include examples where helpful

## ✅ Checklist

Before submitting a PR, ensure:

- [ ] Code follows the style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] No console.log or debugging code left in

## 🤝 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## 📞 Getting Help

- Open an issue for bugs or feature requests
- Check existing issues and discussions
- Ask questions in pull request comments

Thank you for contributing! 🎉
