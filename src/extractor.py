import re
from datetime import datetime, timedelta

def extract_information(query):
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=365)

    company_pattern = re.compile(r"(?P<company>[A-Z][a-z]+(?: [A-Z][a-z]+)*)")
    metric_pattern = re.compile(r"(GMV|revenue|profit)", re.IGNORECASE)
    date_pattern = re.compile(r"(\d{4}-\d{2}-\d{2})")

    company_match = company_pattern.findall(query)
    metric_match = metric_pattern.search(query)
    date_matches = date_pattern.findall(query)
    if len(date_matches) == 2:
        start_date = datetime.fromisoformat(date_matches[0]).date()
        end_date = datetime.fromisoformat(date_matches[1]).date()
    elif len(date_matches) == 1:
        start_date = datetime.fromisoformat(date_matches[0]).date()

    return {
        "companies": company_match,
        "metric": metric_match.group(0) if metric_match else None,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat()
    }

def convert_to_json(extracted_info):
    json_output = []
    for company in extracted_info['companies']:
        json_output.append({
            "entity": company,
            "parameter": extracted_info["metric"],
            "startDate": extracted_info["start_date"],
            "endDate": extracted_info["end_date"]
        })
    return json_output
