# Tasks: Retrieval and Pipeline Validation

**Input**: Design documents from `specs/002-rag-retrieval-validation/`
**Prerequisites**: `plan.md`, `spec.md`

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and dependency configuration.

- [ ] **T001**: [P] Update `backend/pyproject.toml` to include development dependencies: `pytest`, `qdrant-client`, and `sentence-transformers`.
- [ ] **T002**: [P] Create the directory structure `backend/tests/validation/`.
- [ ] **T003**: [P] Create the directory `validation_notebooks/` at the project root.

---

## Phase 2: User Story 1 - AI Engineer Validates Retrieval Pipeline (Priority: P1) 🎯 MVP

**Goal**: Enable an engineer to run a script that validates the RAG pipeline's retrieval accuracy and performance against a benchmark.

**Independent Test**: Run `pytest backend/tests/validation/` and verify that the tests pass or fail correctly based on the benchmark data, and that a log file with metadata is produced.

### Tests for User Story 1 (Write these tests FIRST)

- [ ] **T004**: [US1] Create the initial test file `backend/tests/validation/test_retrieval_pipeline.py` with a simple placeholder test that fails, confirming `pytest` is set up correctly.
- [ ] **T005**: [US1] Create the benchmark data file `backend/tests/validation/benchmark_data.json` with at least two sample queries and their corresponding "golden" retrieved document IDs.

### Implementation for User Story 1

- [ ] **T006**: [US1] In `backend/tests/validation/test_retrieval_pipeline.py`, implement a `pytest` fixture to initialize the `qdrant-client` in read-only mode.
- [ ] **T007**: [US1] In `backend/tests/validation/test_retrieval_pipeline.py`, implement a `pytest` fixture to initialize the `sentence-transformers` model.
- [ ] **T008**: [US1] Implement the main, parameterized test function in `test_retrieval_pipeline.py` that:
    a. Loads the data from `benchmark_data.json`.
    b. Uses the fixtures to run each query against the Qdrant collection.
    c. Asserts that the retrieved document IDs match the expected results.
- [ ] **T009**: [US1] Integrate structured logging into `test_retrieval_pipeline.py` to capture and log the query text, retrieved IDs, similarity scores, and execution latency for each test case.

**Checkpoint**: User Story 1 is fully functional. `pytest` can be run to automatically validate the pipeline against the benchmark.

---

## Phase 3: User Story 2 - Project Evaluator Assesses Pipeline Quality (Priority: P2)

**Goal**: Provide a simple, reproducible example that demonstrates how the validation pipeline works, allowing a stakeholder to easily assess its function.

**Independent Test**: Execute the Jupyter notebook `validation_notebooks/01_retrieval_validation_example.ipynb` from top to bottom and verify it runs without error, displaying the results of a sample query.

### Implementation for User Story 2

- [ ] **T010**: [US2] Create the Jupyter Notebook `validation_notebooks/01_retrieval_validation_example.ipynb`.
- [ ] **T011**: [US2] In the notebook, add cells with clear markdown explanations for each step.
- [ ] **T012**: [US2] Add code cells to the notebook to:
    a. Initialize the Qdrant client and sentence transformer model.
    b. Define a single sample query.
    c. Execute the search against Qdrant.
    d. Print the retrieved results in a human-readable format.

**Checkpoint**: User Story 2 is functional. A non-developer can open and run the notebook to understand and verify the retrieval process.

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Final documentation and cleanup.

- [ ] **T013**: [P] Create a `README.md` file inside `backend/tests/validation/` explaining how to install dependencies and run the validation suite using `pytest`.
- [ ] **T014**: [P] Review and refactor code in `test_retrieval_pipeline.py` and the notebook for clarity and style.