import logging
from crawler.match_center_client import MatchCenterClient
from crawler.darts_parser import DartsParser

class WeeklyUpdate:
 def __init__(self, settings: dict):
 self.client = MatchCenterClient(settings["base_url"])
 self.latest_matches = settings.get("latest_matches", [])

 def run(self) -> list:
 output = []

 for item in self.latest_matches:
 match_id = item["match_id"]
 event_id = item["event_id"]

 logging.info(f"Weekly update fetching {match_id} ...")
 payload = self.client.fetch_match(match_id)
 parsed = DartsParser.parse_match_payload(match_id, event_id, payload)
 output.extend(parsed)

 return output