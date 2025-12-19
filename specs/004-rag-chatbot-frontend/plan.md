# Technical Execution Plan: Frontend Chatbot Integration (Spec-4)

**Feature Branch**: `feature/rag-chatbot-frontend`
**Created**: 2025-12-08
**Status**: Draft

## 1. Scope and Dependencies

### In Scope
-   **React Chatbot Component**: Development of a self-contained chatbot UI component.
-   **Docusaurus Integration**: Embedding the component into the Docusaurus site layout.
-   **State Management**: Handling of loading, error, and conversation history states on the frontend.
-   **Backend Connection**: Integrating with the `POST /query` endpoint from the Spec-3 FastAPI backend.
-   **UI/UX**: Basic styling, responsiveness, and accessibility for the chatbot.

### Out of Scope
-   Backend implementation (handled in Spec-3).
-   Advanced conversational memory.
-   Major changes to the Docusaurus theme or layout.

### Dependencies
-   **Docusaurus v2+**: A running Docusaurus project.
-   **Spec-3 FastAPI Backend**: A running instance of the backend server, accessible from the frontend's environment.
-   **React 17+**: The version of React used by Docusaurus.

## 2. Key Libraries and Tools

-   **Frontend Framework**: `React` (via Docusaurus)
-   **Styling**: CSS Modules or a lightweight CSS-in-JS library (e.g., `styled-components`) to avoid conflicts with Docusaurus styles.
-   **API Client**: Browser's built-in `fetch` API or `axios` for making requests to the backend.
-   **State Management**: React Hooks (`useState`, `useEffect`, `useReducer`).

## 3. Execution Plan (Step-by-Step)

### Step 1: Component Scaffolding
-   **Task**: Create the basic file structure for the chatbot component.
-   **Details**:
    -   Use Docusaurus's "swizzling" feature to override a theme component (e.g., the root layout) or create a new custom component.
    -   Create a directory `src/theme/Chatbot` with the following files:
        -   `ChatbotButton.js`: The floating button to toggle the chat window.
        -   `ChatWindow.js`: The main chat interface.
        -   `style.css`: Styles for the components.
        -   `apiClient.js`: A helper for backend communication.
-   **Output**: A basic, non-functional React component rendered on Docusaurus pages.

### Step 2: UI Implementation
-   **Task**: Build the UI for the chat window, including the display and input areas.
-   **Details**:
    -   In `ChatWindow.js`, implement a scrollable area for messages and a text input form.
    -   Use React state (`useState`) to manage the user's input.
    -   Style the components using CSS modules to ensure they are scoped and don't leak.
    -   Ensure the UI is responsive and accessible from the start.

### Step 3: Backend Integration
-   **Task**: Connect the UI to the FastAPI backend.
-   **Details**:
    -   In `apiClient.js`, create a function `postQuery(query, chunk_ids = null)` that sends a POST request to the backend's `/query` endpoint.
    -   In `ChatWindow.js`, on form submission, call `postQuery` with the user's input.
    -   Use `useState` to manage the conversation history, appending both the user's query and the bot's response to an array of messages.
    -   Render the conversation history in the display area.

### Step 4: State Management (Loading and Errors)
-   **Task**: Implement loading indicators and error handling.
-   **Details**:
    -   Introduce a `loading` state (`useState(false)`). Set it to `true` before the API call and `false` after.
    -   Display a loading indicator in the chat window when `loading` is `true`.
    -   Introduce an `error` state. If the API call fails, set the error state and display an error message to the user.

### Step 5: Selected-Text Query
-   **Task**: Implement the logic for querying selected text.
-   **Details**:
    -   Create a React hook (e.g., `useTextSelection`) that adds a `mouseup` event listener to the document.
    -   Inside the listener, use `window.getSelection()` to get the selected text.
    -   If text is selected, display a small, floating "Ask about this" button near the selection.
    -   When this button is clicked, open the chat window and pre-fill the context with the selected text's chunk IDs (this will require the Docusaurus content to have accessible chunk IDs on its HTML elements).
    -   The subsequent query will be sent to the backend with the `chunk_ids` parameter.

### Step 6: Testing and Documentation
-   **Task**: Validate the functionality and document the component.
-   **Details**:
    -   Manually test all interactions on different pages and screen sizes.
    -   Write a `README.md` for the component, explaining how it's integrated and how to use it.
    -   Include sample queries and expected interactions in the documentation.

## 4. Frontend-Backend Interaction

-   **Endpoint**: `POST /query`
-   **Request Body**:
    ```json
    {
      "query": "string",
      "chunk_ids": "list[string] | null"
    }
    ```
-   **Success Response (200 OK)**:
    ```json
    {
      "answer": "string",
      "metadata": [
        {
          "source_url": "string",
          "chunk_id": "string",
          "section": "string"
        }
      ]
    }
    ```
-   **Error Response (e.g., 500)**:
    ```json
    {
      "detail": "Error message here"
    }
    ```

## 5. Validation Examples

-   **Full-Book Query**:
    1.  Open the chatbot.
    2.  Type "What is ROS 2?" and submit.
    3.  **Expected**: The chatbot displays a loading indicator, then an answer explaining ROS 2, with clickable links to the relevant chapters.
-   **Selected-Text Query**:
    1.  Select a paragraph about "Nodes" in the ROS 2 chapter.
    2.  Click the "Ask about this" button.
    3.  Type "Explain this in simpler terms" and submit.
    4.  **Expected**: The chatbot provides a simplified explanation based only on the selected paragraph.
-   **Error Handling**:
    1.  Stop the backend server.
    2.  Try to ask a question.
    3.  **Expected**: The chatbot displays an error message like "Sorry, I can't connect to the server right now."
