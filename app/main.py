from scraper import fetch_job_data, parse_job_data, save_to_json

# URL of the job board (replace with a real job board URL)
JOB_BOARD_URL = "https://ca.indeed.com/jobs?q=rf+engineer&l=Ottawa%2C+ON&from=searchOnHP%2Cwhatautocomplete&vjk=5c170111941cb8a2"

def main():
    print("Fetching job postings...")
    html_content = fetch_job_data(JOB_BOARD_URL)

    if html_content:
        print("Parsing job postings...")
        job_data = parse_job_data(html_content)
        save_to_json(job_data, "jobs_raw.json")
    else:
        print("Failed to fetch job postings.")

if __name__ == "__main__":
    main()
