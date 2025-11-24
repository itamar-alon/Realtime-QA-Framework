# Real-Time WebSocket QA Framework (Latency & Multi-Client Simulation)

## Project Overview
This project demonstrates advanced **Quality Assurance (QA) automation** techniques for modern, event-driven applications using the **WebSocket** protocol. 

It validates the core functionality of real-time messaging and measures critical performance metrics like **Round Trip Time (RTT) Latency**.

## Technologies & Dependencies
* **Language:** Python 3.10+
* **Automation Framework:** Pytest
* **Async/Real-Time:** `websockets`, `asyncio`
* **Reporting:** Allure Reports (Professional, graphical test reporting)
* **Code Quality:** Black (Used for automatic code formatting)

## Setup and Execution

### 1. Prerequisites
Ensure you have Python 3.10+ installed and access to your terminal (CMD or PowerShell).

### 2. Clone Repository (Assuming this is your first step)
```bash
git clone [YOUR_REPO_URL]
cd WebSocket
3. Create and Activate Virtual EnvironmentThis step isolates project dependencies.Bash# Create venv
python3 -m venv venv 
# Activate venv (Use 'source venv/bin/activate' on Mac/Linux)
.\venv\Scripts\activate
4. Install DependenciesInstall all required libraries from the precise requirements.txt file:Bashpip install -r requirements.txt
5. Run All Tests and Generate Allure ReportsThe following command runs all tests (-s) and outputs the raw data for the Allure report:Bash.\venv\Scripts\python.exe -m pytest --alluredir=./allure-results
Test CoverageTestObjectiveMetricStatusTest 1Latency Check & Functional ValidationMeasures RTT (Round Trip Time) in milliseconds and asserts it's below a set threshold (2000ms for public servers).PassedTest 2Multi-Client Concurrent FlowSimulates two clients exchanging data simultaneously using asyncio.gather. (Note: This test validates the logic but may fail on public Echo servers due to connection closing limitations).Passed📊 Viewing Professional Reports (Allure)To view the interactive HTML reports, you need to serve the data generated in the previous step:Install Allure Commandline: (Required only once. Install via npm, brew, or similar package manager).Serve the Report:Bashallure serve allure-results
This will automatically open the report in your web browser, showing execution details, timing, and clear pass/fail status.

# Run all tests and see output in console
bash
.\venv\Scripts\python.exe -m pytest -s

#Run all tests and generate raw data for Allure reports
bash
.\venv\Scripts\python.exe -m pytest --alluredir=./allure-results