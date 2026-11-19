# AI Decision Journal

| Decision | Why it was made | Human check / safeguard |
|---|---|---|
| Use an LLM only for extracting five fields | Free-text requests vary in wording; status rules should remain deterministic | Python validates schema and original request |
| Require JSON with exactly five keys | Makes the LLM response predictable for Python | `is_valid()` checks keys, types, allowed lab and slot, and summary length |
| Return null for relative dates and unclear details | Prevents the model from inventing missing information | `check_date()` rejects missing or unsupported dates |
| Retry one failed/invalid response once | Allows recovery from a temporary error without unlimited API calls | Safe fallback after second failure |
| Keep booking decisions in Python | Capacity, Sunday and conflict rules are explicit and testable | Unit tests cover each status |
| Keep `bookings.csv` unchanged | Only the authorised lab in-charge can confirm a booking | Schedule is labelled tentative; no write path targets bookings.csv |
| Keep API key in an environment variable | Prevents secrets from being embedded in source or Git | `.gitignore` excludes `.env`; README warns against publishing secrets |

AI assistance was used to draft and review code and test documentation. The developer must understand the code, run the tests, inspect generated reports and explain the design during assessment.

## Final Testing and Execution Results

The final application execution processed 20 booking requests successfully.

### Classification Results

| Status | Count |
|---|---:|
| Available | 13 |
| Conflict | 2 |
| Needs More Information | 1 |
| Over Capacity | 2 |
| Lab Closed | 2 |
| **Total** | **20** |

### Unit Testing

The application was tested using the Python unittest framework. All 8 unit tests passed.

### API Rate Limiting

During execution, some Groq API requests returned HTTP 429 rate-limit errors. The application handled these errors using its retry mechanism and continued processing the requests.

### Generated Reports

The final execution generated the following output files:

- `results.csv`
- `schedule.csv`
- `issues.csv`
- `summary.txt`

The system provides preliminary booking classifications. Final booking approval remains the responsibility of the lab in-charge.
