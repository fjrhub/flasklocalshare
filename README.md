# Simple Flask File Uploader

A lightweight web application built with **Flask** that allows users to
upload and download files through a clean web interface. This project is
ideal for learning basic routing, file handling, and template rendering
in Flask.

------------------------------------------------------------------------

## Features

-   Upload files directly from the browser
-   Display a list of uploaded files
-   Download available files
-   Automatically creates the upload directory
-   Clean and simple code, easy to modify

------------------------------------------------------------------------

## Requirements

Make sure you have Python installed along with Flask:

``` bash
pip install Flask
```

------------------------------------------------------------------------

## Project Structure

    project/
    ├── app.py
    ├── uploads/
    ├── templates/
    │   ├── index.html
    │   └── upload_success.html
    └── README.md

The **uploads/** folder will be created automatically when the app runs.

------------------------------------------------------------------------

## How to Run

Run the following command:

``` bash
python app.py
```

Then open:

    http://0.0.0.0:8080

------------------------------------------------------------------------

## Code Overview

-   **/** → Shows the list of uploaded files\
-   **/upload/** → Handles file uploads via POST\
-   **/download/`<filename>`{=html}** → Downloads a file from the
    uploads directory

------------------------------------------------------------------------

## Example Usage

1.  Open the homepage in the browser
2.  Select a file and upload it
3.  Click the filename to download it

------------------------------------------------------------------------

## Notes

-   There is no file extension validation. Add filters if needed.
-   For production, disable debug mode and use a server like Gunicorn or
    uWSGI.