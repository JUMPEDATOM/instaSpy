
# instaSpy

Welcome to instaSpy! Here, you will find an exciting Python script that utilizes the power of Selenium to scrape usernames of your Instagram followers and following. But that's not all – this script goes a step further by identifying the users who have unfollowed you on Instagram.

Tracking followers and unfollowers can be a time-consuming task, especially when dealing with a large number of users. That's where this script comes in handy, automating the process and providing you with valuable insights about your Instagram audience.

By leveraging Selenium, a powerful web automation tool, this script navigates through Instagram's interface, interacts with the elements, and extracts the usernames of your followers and following. It then cleverly compares the lists to determine who has recently unfollowed you.

I have designed this script with a focus on simplicity, efficiency, and readability. Each step is thoroughly documented, making it easy for you to understand and customize the code to suit your specific needs. Additionally, I have included comprehensive instructions on how to set up and run the script successfully.

Whether you're an Instagram influencer, a social media enthusiast, or simply curious about tracking your followers, this Python script will be a valuable addition to your toolkit. So, go ahead and explore this repository to take control of your Instagram audience and stay informed about those who choose to unfollow you.





## Features

- **Scraping Usernames:** The script utilizes Selenium to scrape the usernames of your Instagram followers and following. It automates the process of navigating through the Instagram interface, accessing user profiles, and extracting relevant information.

- **Tracking Unfollowers:** By comparing the lists of followers and following, the script identifies users who have unfollowed you on Instagram. It provides you with a clear view of the changes in your follower count and helps you stay informed about your audience.

- **Automated Execution:** The script automates the process of scraping and unfollower detection, saving you time and effort. Once configured and executed, it performs the necessary steps without requiring manual intervention.

- **Customizable and Extendable:** The script is designed to be easily customizable and extendable. You can modify it to adapt to changes in Instagram's interface or add additional functionalities based on your specific requirements.




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`INSATGRAM_USERNAME`

`INSTAGRAM_PASSWORD`

`BROWSER_PATH` `{your browser PATH}`

`BROWSER_DRIVER` `{your downloaded browser driver PATH}`


## Run Locally

Clone the project

```bash
  git clone https://github.com/JUMPEDATOM/instaSpy.git
```

Go to the project directory

```bash
  cd instaSpy-master
```

Install dependencies

```bash
   pip install -r requirements.txt
```

Run script

```bash
  python instaSpy.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

