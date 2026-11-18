"""Five-status evaluation harness. Runs locally without calling the LLM."""
import csv
from lab_booking_sorter import decide

LABS = {"LAB1": {"name": "Python Lab 1", "capacity": 60},
        "LAB3": {"name": "AI Lab", "capacity": 40},
        "LAB5": {"name": "Seminar Hall", "capacity": 120}}
CASES = [
    ("E1", "Python Lab 1 on 9 November afternoon for 55 students", {"lab":"LAB1","date":"2026-11-09","slot":"AN","students":55,"summary":"CS101 practice"}, set(), "available"),
    ("E2", "AI Lab on 10 November afternoon for 25 students", {"lab":"LAB3","date":"2026-11-10","slot":"AN","students":25,"summary":"AI demo"}, {("2026-11-10","AN","LAB3")}, "conflict"),
    ("E3", "Seminar Hall on 12 November afternoon for 130 students", {"lab":"LAB5","date":"2026-11-12","slot":"AN","students":130,"summary":"Seminar"}, set(), "over_capacity"),
    ("E4", "Python Lab 1 on 15 November morning for 20 students", {"lab":"LAB1","date":"2026-11-15","slot":"FN","students":20,"summary":"Practice"}, set(), "lab_closed"),
    ("E5", "Need a lab tomorrow for project review", {"lab":None,"date":None,"slot":None,"students":None,"summary":"Project review"}, set(), "needs_more_info"),
]
results = []
for case_id, request, extracted, taken, expected in CASES:
    row = {"id":case_id,"sent":"2026-11-01","request":request}
    actual = decide(row, extracted, LABS, set(taken))["status"]
    results.append({"test_id":case_id,"expected":expected,"actual":actual,"passed":actual == expected})
with open("evaluation_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["test_id","expected","actual","passed"])
    writer.writeheader(); writer.writerows(results)
passed = sum(r["passed"] for r in results)
print(f"Evaluation: {passed}/{len(results)} passed")
for r in results: print(f"{r['test_id']}: expected={r['expected']}, actual={r['actual']}, {'PASS' if r['passed'] else 'FAIL'}")
