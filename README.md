# Web Scraping Using Docker

This project demonstrates how to perform web scraping using a Docker container. It includes a Docker image with the Firefox web browser and Python libraries (such as Selenium) for scraping data from websites.

## Purpose

The main purpose of this project is to showcase how to set up a Docker environment for web scraping tasks. By containerizing the browser and necessary libraries, you can easily deploy and manage your scraping scripts.

## Components

- **Docker Image**: Contains Firefox browser and Python libraries.
- **Scraping Logic**: Update the `home.py` file with your specific scraping logic.
- **Deployment**: Hosted on Amazon Web Services (AWS).

## Instructions

1. **Scraping Logic**: Modify the `home.py` file in the `code` folder. Add your custom scraping code here.
2. **Archive Content**: Create a ZIP archive of the contents in the `code` folder. Name it `code.zip`.
3. **Upload to S3**: Upload the `code.zip` archive to your specified S3 bucket (refer to the CloudFormation script for the bucket name).

## Note

- **Firefox Updates**: Keep your Firefox browser up to date for security reasons.
- **Alternative Browsers**: If needed, consider using alternative browsers for web scraping.
- **Puppeteer**: Explore Puppeteer (headless Chrome/Chromium) as an alternative to Selenium.

Happy scraping! 🚀
