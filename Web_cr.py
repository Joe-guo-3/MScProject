# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 00:00:44 2023

@author: not exactly Hang Zhou
"""

import requests
import json
import datetime

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d")

url = 'https://app.goflightlabs.com/advanced-flights-schedules?access_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMzMxNTFhYjU0MzM3NzcxMGMzMTdjY2ZlMTRiZGRkMGZmYmEyODNmNDFhOTFjMDQxYzMxMDdhNjZkNTlmYzVlMWQ5OTE5MGVkMzY4YmRlMDIiLCJpYXQiOjE2NzkyNjU1MjAsIm5iZiI6MTY3OTI2NTUyMCwiZXhwIjoxNzEwODg3OTIwLCJzdWIiOiIyMDUxNiIsInNjb3BlcyI6W119.Qe9ScfbkSVvRY0g03egqq_pt_x8b3BAWfGCtgOK3JOV0yGoJ9x11XicUcKfmOtmI1CmeH6LvAh_tYHusxjDPLw&iataCode=GLA&type=departure'
headers = {'User-Agent': 'Mozilla/5.0'}  # optional header to avoid bot detection

response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)
    filename = f"GLA_departure_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(data, f)
    print(f"JSON data saved to {filename}")
else:
    print(f"Request failed with status code {response.status_code}")

url = 'https://app.goflightlabs.com/advanced-flights-schedules?access_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMzMxNTFhYjU0MzM3NzcxMGMzMTdjY2ZlMTRiZGRkMGZmYmEyODNmNDFhOTFjMDQxYzMxMDdhNjZkNTlmYzVlMWQ5OTE5MGVkMzY4YmRlMDIiLCJpYXQiOjE2NzkyNjU1MjAsIm5iZiI6MTY3OTI2NTUyMCwiZXhwIjoxNzEwODg3OTIwLCJzdWIiOiIyMDUxNiIsInNjb3BlcyI6W119.Qe9ScfbkSVvRY0g03egqq_pt_x8b3BAWfGCtgOK3JOV0yGoJ9x11XicUcKfmOtmI1CmeH6LvAh_tYHusxjDPLw&iataCode=GLA&type=arrival'
headers = {'User-Agent': 'Mozilla/5.0'}  # optional header to avoid bot detection

response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)
    filename = f"HAJ_arrival_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(data, f)
    print(f"JSON data saved to {filename}")
else:
    print(f"Request failed with status code {response.status_code}")

url = 'https://app.goflightlabs.com/advanced-flights-schedules?access_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMzMxNTFhYjU0MzM3NzcxMGMzMTdjY2ZlMTRiZGRkMGZmYmEyODNmNDFhOTFjMDQxYzMxMDdhNjZkNTlmYzVlMWQ5OTE5MGVkMzY4YmRlMDIiLCJpYXQiOjE2NzkyNjU1MjAsIm5iZiI6MTY3OTI2NTUyMCwiZXhwIjoxNzEwODg3OTIwLCJzdWIiOiIyMDUxNiIsInNjb3BlcyI6W119.Qe9ScfbkSVvRY0g03egqq_pt_x8b3BAWfGCtgOK3JOV0yGoJ9x11XicUcKfmOtmI1CmeH6LvAh_tYHusxjDPLw&iataCode=HAJ&type=departure'
headers = {'User-Agent': 'Mozilla/5.0'}  # optional header to avoid bot detection

response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)
    filename = f"HAJ_departure_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(data, f)
    print(f"JSON data saved to {filename}")
else:
    print(f"Request failed with status code {response.status_code}")

url = 'https://app.goflightlabs.com/advanced-flights-schedules?access_key=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMzMxNTFhYjU0MzM3NzcxMGMzMTdjY2ZlMTRiZGRkMGZmYmEyODNmNDFhOTFjMDQxYzMxMDdhNjZkNTlmYzVlMWQ5OTE5MGVkMzY4YmRlMDIiLCJpYXQiOjE2NzkyNjU1MjAsIm5iZiI6MTY3OTI2NTUyMCwiZXhwIjoxNzEwODg3OTIwLCJzdWIiOiIyMDUxNiIsInNjb3BlcyI6W119.Qe9ScfbkSVvRY0g03egqq_pt_x8b3BAWfGCtgOK3JOV0yGoJ9x11XicUcKfmOtmI1CmeH6LvAh_tYHusxjDPLw&iataCode=HAJ&type=arrival'
headers = {'User-Agent': 'Mozilla/5.0'}  # optional header to avoid bot detection

response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)
    filename = f"GLA_arrival_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(data, f)
    print(f"JSON data saved to {filename}")
else:
    print(f"Request failed with status code {response.status_code}")