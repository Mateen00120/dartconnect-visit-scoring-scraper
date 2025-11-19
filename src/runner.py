import json
from pathlib import Path
from pipelines.historical_loader import HistoricalLoader
from pipelines.weekly_update import WeeklyUpdate
from config.settings import load_settings

def main():
 settings = load_settings()
 mode = settings.get("mode", "historical")

 if mode == "historical":
 loader = HistoricalLoader(settings)
 data = loader.run()
 elif mode == "weekly":
 loader = WeeklyUpdate(settings)
 data = loader.run()
 else:
 raise ValueError(f"Unknown mode: {mode}")

 output_path = Path(settings.get("output_path", "output.json"))
 with output_path.open("w") as f:
 json.dump(data, f, indent=2)

 print(f"[OK] Scraping completed. Saved to {output_path}")

if __name__ == "__main__":
 main()