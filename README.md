# Running the Task 3 API Locally
To run the UK Postcode API locally, you will need to follow these steps:
- Clone this repository to your local machine.
- Navigate to the project directory.
- Install the requirements.txt dependencies.
- Start the API server: uvicorn task_3_main:app --reload

This will start the API server on http://localhost:8000.

## API Documentation
The UK Postcode API comes with built-in documentation. To access the documentation, navigate to http://localhost:8000/docs in your web browser.

The documentation details the endpoint request and response formats.

You can try out the API directly in the documentation by clicking on the endpoint and then clicking on the "Try it out" button. This will open a form where you can enter the postcode you want to validate or format.

Similarly, you can use curl to interact with the API endpoint from the terminal: curl http://127.0.0.1:8000/?input_postcode=wc2n%204js