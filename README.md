# Lab Booking Request Sorter

A Python console application for extracting details from informal lab-booking requests, checking rules and producing a tentative schedule. **It does not reserve rooms or approve requests. The lab in-charge confirms every booking.**

## Project files
- `lab_booking_sorter.py` — application and required functions
- `requests.csv`, `labs.csv`, `bookings.csv` — input data
- `system_prompt.txt` — five-role extraction prompt
- `test_sorter.py` — offline unit tests
- `evaluation_harness.py` — five-status evaluation
- `red_team_tests.csv` — three adversarial/edge cases
- `Judgment_Framework.md`, `Cost_and_Latency.md`, `AI_Decision_Journal.md` — assessment notes

## Setup (Windows PowerShell)
1. Open this folder in VS Code and open Terminal > New Terminal.
2. Install the dependency: `python -m pip install -r requirements.txt`
3. Set your existing Groq key in the terminal (do not put it in the source code):
   `$env:LLM_API_KEY="YOUR_GROQ_KEY"`
4. Optional overrides:
   `$env:LLM_API_URL="https://api.groq.com/openai/v1/chat/completions"`
   `$env:LLM_MODEL="openai/gpt-oss-20b"`
5. Run: `python lab_booking_sorter.py`

The key is read from the environment variable. If it is missing or the API fails twice, the program uses a safe fallback and does not mark the request available.

## Run offline checks
- `python -m unittest -v`
- `python evaluation_harness.py`

These tests do not need an API key or internet access. The evaluation harness uses fixed, pre-validated extraction examples to test Python's decision rules; it is not a measurement of LLM extraction accuracy.

## Rules
Semester window: 1 October 2026 through 30 November 2026 (confirm this with faculty). FN = morning; AN = afternoon. Rule order: validate explicit date and student count; require lab/date/slot/students; Sunday closure; capacity; existing/earlier conflict; otherwise tentative available. Requests are processed in CSV order.

## Outputs
The application creates `results.csv`, date-sorted `schedule.csv`, `issues.csv` (including original request) and `summary.txt` (counts by status and lab). It never modifies `bookings.csv`.

## GitHub safety
`.gitignore` excludes `.env`, virtual environments and Python cache files. Never commit an API key. Suggested meaningful commits: (1) add specification, inputs and prompt; (2) implement extraction, validation and reports; (3) add evaluation, red-team tests and documentation.
