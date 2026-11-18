# Judgment Framework

| Part of the tool | Cost of being wrong | Can it be verified without AI? | Who is accountable? |
|---|---|---|---|
| Lab extraction | Request sent to the wrong room or follow-up delayed | Yes: compare lab name/code with the original message and labs.csv | Request reviewer; lab in-charge makes final decision |
| Date extraction | Wrong-day scheduling or missed request | Yes: compare original wording and use Python datetime | Python validates; lab in-charge verifies |
| Session extraction | Session clash or wrong timetable | Yes: compare morning/afternoon wording with FN/AN | Lab in-charge |
| Student count | Room may be unsuitable or unsafe | Yes: compare explicit count with original request | Request reviewer and lab in-charge |
| Capacity check | Overcrowding and safety risk | Yes: compare count with labs.csv capacity | Python applies rule; lab in-charge accountable |
| Sunday check | Closed facility could be requested | Yes: Python date.weekday() | Application operator and lab in-charge |
| Conflict check | Double-booking and disruption | Yes: compare bookings.csv and earlier accepted requests | Lab in-charge owns booking register |
| Final availability label | Incorrect expectation that a room is reserved | Yes: inspect every rule and source record | **Lab in-charge confirms every booking** |

## Human checkpoint
`available` means only that no automated rule found a problem. It is not an approval or reservation. The lab in-charge checks the original request, reports and booking register, then confirms or rejects the request. The program never edits `bookings.csv`.
