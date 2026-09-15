import copy
import unittest

from priority import counts, normalize, ordered


class PriorityTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize([{"title": "  A ", "priority": " HIGH "}, {"title": "B"}]),
                         [{"title": "A", "priority": "high"}, {"title": "B", "priority": "medium"}])

    def test_validation(self):
        with self.assertRaises(ValueError):
            normalize([{"title": "A", "priority": "urgent"}])
        with self.assertRaises(ValueError):
            normalize([{"title": "  "}])

    def test_order_and_counts(self):
        items = normalize([{"title": "low", "priority": "low"}, {"title": "A", "priority": "high"},
                           {"title": "B", "priority": "high"}, {"title": "medium"}])
        self.assertEqual([x["title"] for x in ordered(items)], ["A", "B", "medium", "low"])
        self.assertEqual(counts(items), {"high": 2, "medium": 1, "low": 1})

    def test_immutable_and_empty(self):
        source = [{"title": " A ", "priority": "LOW"}]
        before = copy.deepcopy(source)
        result = normalize(source)
        self.assertEqual(source, before)
        self.assertEqual(result, [{"title": "A", "priority": "low"}])
        self.assertEqual(counts([]), {"high": 0, "medium": 0, "low": 0})


if __name__ == "__main__":
    unittest.main()
