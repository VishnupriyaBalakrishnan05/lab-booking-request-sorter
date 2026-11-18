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
