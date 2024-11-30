## My steps/algorithms, how I see the solution.

1. Install and import needed libs (+add logger config and const's).
2. Download testing files from github to local machine using requests lib.

CSV links:
- csv_file1: 'https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_csv/random-michaels.csv'
- csv_file2: 'https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_csv/random.csv'

JSON links:
- json_file1: 'https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_json/localizations_en.json'
- json_file2: 'https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_json/localizations_ru.json'
- json_file3: 'https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_json/login.json'
- json_file4: 'https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_json/swagger.json'

XML links:
- xml_file1: 'https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_xml/groups.xml'
- xml_file2: 'https://raw.githubusercontent.com/dntpanix/automation_qa/refs/heads/main/ideas_for_test/work_with_xml/login.xml'

3. CSV task:
- read data from both files;
- combine the data;
- find and remove duplicates;
- write the result to a file;

4. JSON task:
- check files in the folder;
- try to load each file as JSON;
- handle errors;
- write results to a log file;

5. XML task:
- load the XML file;
- create a search function;
- implement the search logic;
- log the result to the console;
