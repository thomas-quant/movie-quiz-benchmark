# Movie Types Quiz - Specification

## Project Overview
- **Project name**: Movie Types Quiz
- **Type**: Multi-page Flask web application
- **Core functionality**: A 30-question trivia quiz about different movie genres, types, and cinema knowledge. Each question on its own page with session-based progress tracking.
- **Target users**: Movie enthusiasts testing their cinema knowledge

## Technical Stack
- Flask (Python web framework)
- Session-based state management
- HTML/CSS templates

## UI/UX Specification

### Layout Structure
- Single column centered layout
- Max width: 600px
- Pages: Welcome → 30 Question pages → Results

### Visual Design
- **Color palette**:
  - Background: #0a0a0f (deep noir black)
  - Card background: #16161d (dark charcoal)
  - Primary accent: #e50914 (cinema red)
  - Secondary: #f5c518 (golden yellow - movie gold)
  - Text primary: #f0f0f0
  - Text muted: #8a8a9a
  - Success: #22c55e
  - Error: #ef4444
- **Typography**:
  - Headings: "Bebas Neue", sans-serif (bold, cinematic)
  - Body: "Source Sans 3", sans-serif
- **Spacing**: 16px base unit

### Components
- Question card with question number badge
- 4 answer buttons (A, B, C, D style)
- Progress bar showing current question / total
- Navigation: Next button (after answer selection)
- Results screen with score breakdown

### Animations
- Fade-in on page load
- Answer button hover scale
- Correct/incorrect feedback flash

## Functionality Specification

### Core Features
1. **Welcome page**: Title, start button
2. **Question pages** (30 total):
   - Display question number (e.g., "Question 5 of 30")
   - Progress bar
   - Question text
   - 4 multiple choice answers
   - Visual feedback on selection (green/red flash)
   - "Next" button appears after selection
3. **Results page**:
   - Final score (X/30)
   - Percentage score
   - Performance message
   - List of questions with user's answers
   - "Play Again" button

### Session Management
- Track: current question index
- Track: all user answers
- Track: correct answers count

### Questions (30 total)
Covering: film genres, directors, famous movies, awards, cinematography terms, classic films, modern cinema, international cinema, animation, franchises

## Acceptance Criteria
- [ ] All 30 questions render correctly
- [ ] Session persists between pages
- [ ] Score calculated correctly at end
- [ ] Results show all answers
- [ ] Play again resets session
- [ ] Responsive on mobile