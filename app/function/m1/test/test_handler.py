import unittest

from src.main import index


class TestHandler(unittest.TestCase):
    def test_ping_request(self):
        event = {
            "@type": "PingRequest",
            "identity": {},
            "queryId": "query-1",
            "catalogName": "catalog-1",
        }
        res = index.handler(event, None)
        self.assertEqual(res["@type"], "PingResponse")
        self.assertEqual(res["catalogName"], "catalog-1")
        self.assertEqual(res["queryId"], "query-1")

    def test_missing_type(self):
        with self.assertRaises(ValueError):
            index.handler({}, None)

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            index.handler({"@type": "UnknownRequest"}, None)


if __name__ == "__main__":
    unittest.main()
