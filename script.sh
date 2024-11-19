#!/bin/bash

website_url=$1
email=""  # Replace with your actual email

check_website() {
    # Get the HTTP status code for the website
    status_code=$(curl --head -s $website_url | awk '/^HTTP/{print $2}')
    
    # Check if status code is 200 or 301
    if [[ $status_code == "200" || $status_code == "301" ]]; then
        echo "Website is running"
    else
        echo "Website is down"
        send_email  # Call send_email if the website is down
    fi
}

send_email() {
    subject="Website is not working"
    body="The application is terminated. Website $website_url is down."
    
    # Send the email using the 'mail' command
    echo "$body" | mail -s "$subject" $email
    
    # Check if the email was sent successfully
    if [[ $? -eq 0 ]]; then
        echo "Email sent successfully."
    else
        echo "Failed to send email."
    fi
}

# Run the check_website function
check_website

