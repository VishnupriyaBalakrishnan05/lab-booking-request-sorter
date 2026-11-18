"""Offline unit tests: no Groq key or network connection required."""
import unittest
from lab_booking_sorter import decide, is_valid, check_date

LABS = {"LAB1": {"name": "Python Lab 1", "capacity": 60},
        "LAB3": {"name": "AI Lab", "capacity": 40},
        "LAB5": {"name": "Seminar Hall", "capacity": 120}}


def row(req_id, text):
    return {"id": req_id, "sent": "2026-11-01", "request": text}


class SorterTests(unittest.TestCase):
    def test_valid_schema(self):
        self.assertTrue(is_valid({"lab":"LAB1", "date":"2026-11-09", "slot":"AN", "students":55, "summary":"CS101 practice"}, LABS))

    def test_invalid_extra_field(self):
        data = {"lab":"LAB1", "date":"2026-11-09", "slot":"AN", "students":55, "summary":"Practice", "status":"available"}
        self.assertFalse(is_valid(data, LABS))

    def test_available(self):
        result = decide(row("T1", "Python Lab 1 on 9 November afternoon for 55 students"),
                        {"lab":"LAB1", "date":"2026-11-09", "slot":"AN", "students":55, "summary":"CS101 practice"}, LABS, set())
        self.assertEqual(result["status"], "available")

    def test_conflict(self):
        taken = {("2026-11-10", "AN", "LAB3")}
        result = decide(row("T2", "AI Lab on 10 November afternoon for 25 students"),
                        {"lab":"LAB3", "date":"2026-11-10", "slot":"AN", "students":25, "summary":"AI demo"}, LABS, taken)
        self.assertEqual(result["status"], "conflict")

    def test_over_capacity(self):
        result = decide(row("T3", "Seminar Hall on 12 November afternoon for 130 students"),
                        {"lab":"LAB5", "date":"2026-11-12", "slot":"AN", "students":130, "summary":"Seminar"}, LABS, set())
        self.assertEqual(result["status"], "over_capacity")

    def test_sunday_closed(self):
        result = decide(row("T4", "Python Lab 1 on 15 November morning for 20 students"),
                        {"lab":"LAB1", "date":"2026-11-15", "slot":"FN", "students":20, "summary":"Practice"}, LABS, set())
        self.assertEqual(result["status"], "lab_closed")

    def test_relative_date_needs_info(self):
        result = decide(row("T5", "Need a lab tomorrow for project review"),
                        {"lab":None, "date":None, "slot":None, "students":None, "summary":"Project review"}, LABS, set())
        self.assertEqual(result["status"], "needs_more_info")

    def test_impossible_date_rejected(self):
        ok, reason = check_date("2026-11-31", "Book LAB1 on 31 November for 20 students")
        self.assertFalse(ok)
        self.assertEqual(reason, "Invalid calendar date")


if __name__ == "__main__":
    unittest.main(verbosity=2)
