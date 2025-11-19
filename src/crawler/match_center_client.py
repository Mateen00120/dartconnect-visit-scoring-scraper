import requests
import logging

class MatchCenterClient:
 def __init__(self, base_url: str, timeout: int = 10):
 self.base_url = base_url.rstrip("/")
 self.timeout = timeout
 self.session = requests.Session()

 def fetch_match(self, match_id: str) -> dict:
 url = f"{self.base_url}/match/{match_id}.json"
 try:
 r = self.session.get(url, timeout=self.timeout)
 r.raise_for_status()
 return r.json()
 except Exception as e:
 logging.error(f"Failed to fetch match {match_id}: {e}")
 return {}

 def fetch_event_matches(self, event_id: str) -> list:
 url = f"{self.base_url}/event/{event_id}/matches.json"
 try:
 r = self.session.get(url, timeout=self.timeout)
 r.raise_for_status()
 return r.json().get("matches", [])
 except Exception as e:
 logging.error(f"Failed to fetch matches for event {event_id}: {e}")
 return []