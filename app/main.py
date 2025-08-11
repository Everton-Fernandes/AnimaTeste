import os
import json
import requests
from tabulate import tabulate

SAMPLE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", "sample_events.json"
)


def load_sample():
    with open(SAMPLE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["value"]


def fetch_from_graph(token: str):
    url = "https://graph.microsoft.com/v1.0/me/events?$top=10&$orderby=start/dateTime"
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json().get("value", [])


def display_events(events):
    table = []
    for ev in events:
        table.append(
            [
                ev.get("subject", "Sem título"),
                ev.get("start", {}).get("dateTime", ""),
                ev.get("end", {}).get("dateTime", ""),
                ev.get("location", {}).get("displayName", ""),
            ]
        )
    print(
        tabulate(
            table, headers=["Assunto", "Início", "Fim", "Localização"], tablefmt="grid"
        )
    )


def main():
    token = os.getenv("GRAPH_TOKEN")
    try:
        if token:
            events = fetch_from_graph(token)
        else:
            print("[INFO] GRAPH_TOKEN não definido. Usando dados de exemplo.")
            events = load_sample()
    except Exception as e:
        print(f"[WARN] Falha ao chamar Graph: {e}. Usando dados de exemplo.")
        events = load_sample()

    table = []
    for ev in events:
        table.append(
            [
                ev.get("subject", "Sem título"),
                ev.get("start", {}).get("dateTime", ""),
                ev.get("end", {}).get("dateTime", ""),
                ev.get("location", {}).get("displayName", ""),
            ]
        )
    print(
        tabulate(
            table, headers=["Assunto", "Início", "Fim", "Localização"], tablefmt="grid"
        )
    )


if __name__ == "__main__":
    # events = load_sample()
    # display_events(events)
    main()
