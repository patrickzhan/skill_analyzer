import requests
from bs4 import BeautifulSoup

import json
import os

def fetch_job_data(url, headers=None):
    """
    Fetches job postings from the provided URL.
    Args:
        url (str): The job portal URL.
        headers (dict): Headers for the HTTP request (optional).
    Returns:
        list: A list of job postings in raw HTML format.
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_job_data(html_content):
    """
    Parses raw HTML to extract job details like title, skills, and description.
    Args:
        html_content (str): HTML content of the job page.
    Returns:
        list: List of dictionaries containing job details.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    job_list = []

    # Customize parsing logic based on the structure of the job portal
    for job_card in soup.find_all('div', class_='job-card'):
        title = job_card.find('h2', class_='job-title').text.strip()
        company = job_card.find('div', class_='company').text.strip()
        description = job_card.find('div', class_='description').text.strip()
        
        job_list.append({
            'title': title,
            'company': company,
            'description': description
        })

    return job_list

def save_to_json(data, filename):
    """
    Saves job data to a JSON file.
    Args:
        data (list): List of job postings.
        filename (str): Path to save the JSON file.
    """
    os.makedirs('app/data', exist_ok=True)  # Ensure directory exists
    filepath = os.path.join('app/data', filename)

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filepath}")
