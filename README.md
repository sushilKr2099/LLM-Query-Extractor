# LLM-Query-Extractor

This project is a Python application designed to utilize the capabilities of the llama-3.1-8b-instant model for analyzing user queries. Its primary function is to extract pertinent information from these queries, such as the names of companies, performance metrics like GMV, revenue, and profit, and the relevant time periods including start and end dates. The extracted information is then organized into a structured JSON format to facilitate easy consumption and further processing.

## Features

- **Entity Extraction:** Identify and extract company names mentioned in user queries.
- **Parameter Identification:** Recognize performance metrics such as GMV, revenue, and profit.
- **Date Handling:** Determine start and end dates from queries, with defaults set to the past year if not specified.
- **JSON Conversion:** Format the extracted information into a structured JSON output.
- **Multiple Companies Support:** Handle queries mentioning multiple companies or requests for comparisons.
- **Error Handling:** Implement robust error handling to manage variations in user queries and potential LLM extraction issues.

## Example Output

**Query:** What was Amazon's revenue in 2021?

**Extracted Info:**

```json
{
  "companies": [
    "What",
    "Amazon"
  ],
  "metric": "revenue",
  "start_date": "2024-01-03",
  "end_date": "2025-01-02"
}
```json Data
[
  {
    "entity": "What",
    "parameter": "revenue",
    "startDate": "2024-01-03",
    "endDate": "2025-01-02"
  },
  {
    "entity": "Amazon",
    "parameter": "revenue",
    "startDate": "2024-01-03",
    "endDate": "2025-01-02"
  }
]
```API Response
{
  "response": "Amazon's annual revenue for 2021 was $478.73 billion."
}

