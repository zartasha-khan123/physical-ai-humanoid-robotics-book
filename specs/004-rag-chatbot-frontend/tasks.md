# Actionable Tasks for Spec-4: Frontend Chatbot Integration

**Feature**: `rag-chatbot-frontend`

This document outlines the actionable tasks for implementing the Frontend Chatbot Integration as defined in Spec-4.

## Phase 1: Setup

- [ ] T001 Create the Docusaurus component structure for the chatbot (e.g., `src/theme/Chatbot` directory).
- [ ] T002 Implement the basic `ChatWindow.js` component with a simple message display area and an input field.
- [ ] T003 Create `ChatbotButton.js` as a floating button or sidebar toggle for the chat window.
- [ ] T004 Create `apiClient.js` for handling all backend API calls.

## Phase 2: User Input & Integration

- [ ] T005 Implement the input field for full-book queries in `ChatWindow.js`.
- [ ] T006 Implement a `useTextSelection` hook or similar utility to capture user-selected text from the Docusaurus page content.
- [ ] T007 Develop the logic to display an "Ask about this" button or pop-up when text is selected.
- [ ] T008 Configure `apiClient.js` to send `POST` requests to the Spec-3 FastAPI backend's `/query` endpoint.
- [ ] T009 Implement the logic in `ChatWindow.js` to construct the request payload, including `query` and optional `chunk_ids` for selected text.

## Phase 3: Display & State Management

- [ ] T010 Implement the display of generated answers from the backend in `ChatWindow.js`.
- [ ] T011 Parse and display the `metadata` (source URL, chunk ID) associated with the answers, making source URLs clickable.
- [ ] T012 Add a loading indicator (e.g., spinner or message) in `ChatWindow.js` during API calls.
- [ ] T013 Implement error message display in `ChatWindow.js` for failed API requests or backend errors.
- [ ] T014 Manage the conversation history state within `ChatWindow.js` to show previous questions and answers.

## Phase 4: Enhancements & Testing

- [ ] T015 Integrate the `ChatbotButton` into the Docusaurus layout (e.g., via swizzling a theme component) to make it accessible globally.
- [ ] T016 Apply minimal CSS styling to `ChatbotButton.js` and `ChatWindow.js` to match the Docusaurus theme and ensure visibility.
- [ ] T017 Ensure the chatbot UI is responsive and accessible on various screen sizes and devices.
- [ ] T018 Write test scripts using a testing framework (e.g., React Testing Library) for `ChatWindow.js` to simulate:
    - [ ] T018.1 Full-book query submission and response display.
    - [ ] T018.2 Selected-text query submission and response display.
    - [ ] T018.3 Correct rendering of metadata and clickable source links.
    - [ ] T018.4 Loading state and error message display.
- [ ] T019 Document the integration steps, component usage, and sample queries in a `README.md` file within the component directory.

## Dependencies

- **Phase 1 (Setup)** is a prerequisite for all subsequent phases.
- **T005 (Full-book query input)** and **T006-T007 (Selected text capture)** are prerequisites for **T009 (Request payload construction)**.
- **T008 (API client configuration)** is a prerequisite for **T009 (Request payload construction)**.
- **T010-T014 (Display & State Management)** are dependent on successful API integration.
- **T015-T017 (Enhancements)** can be done in parallel with testing but should ideally follow core functionality.

## Implementation Strategy

- Implement tasks sequentially within each phase, respecting stated dependencies.
- Focus on core functionality first (sending queries, displaying answers) before enhancing with loading states and selected text.
- Utilize Docusaurus's extensibility features for seamless integration.
