# MyProject
Before you can use these apps, make sure you have the requirements installed:
Windows: py -m pip install -r requirements.txt
Linux: python3 -m pip install -r requirements.txt

Also, you have to run "employeesdb.py" once before running any of the apps. This will create the database and populate it with some example data.

Assuming you've already unzipped this file, proceed as follows:
1. Go to this directory (project) with: cd <path-to-directory>
2. Install a Python Environment:
    Windows: py -m venv .venv
    Linux: python3 -m venv .venv
3. Activate the VEnv:
    Windows: .\.venv\Scripts\activate
    Linux: sudo ./venv/Scripts/activate
4. Install requirements in the VEnv:
    Windows: py -m pip install -r requirements.txt
    Linux: python3 -m pip install -r requirements.txt
5. Run the employeesdb script:
    Windows: py .\employeesdb.py
    Linux: python3 ./employeesdb.py

6. Note that you'll have to do this only the first time when starting the proccess.

After completing all these steps, in the same terminal you should start the project server as follows:
    Windows: py .\employees_api.py
    Linux: python3 ./employees_api.py

Now, with this terminal opened, open another one, repeat steps 1 and 3 from above and start the frontend website with:
    Windows: py .\employees_frontend.py
    Linux: python3 ./employees_frontend.py
