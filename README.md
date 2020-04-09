# GetRobots

## Description
If you want to scrape a site with a bot/search-engine, you first have to be allowed to scrape the website. Site's lay out the restrictions for which pages these bots/search-engines can reach in their robots.txt file. 
Before creating this script, I would have to access a website's robots.txt file through a browser, and find my agent in the (sometimes) very large, unorganized file.
This script automates the process of searching the robots.txt file for rules applying to my bot/search-engine.

## Usage
Executing From Command Line
  Format:
  > python getRobots.py <MANDATORY: website host> <OPTIONAL: bot name, DEFAULT: *> 

  Example:
  > python getRobots.py facebook Applebot

## Further Reading
To read a websites robots.txt file, try reaching the endpoint:

  https://www.\<host>.\<domain>/robots.txt
  
Example:
  
  https://wwww.facebook.com/robots.txt
  
To learn more about robots.txt:
https://support.google.com/webmasters/answer/6062608?hl=en
