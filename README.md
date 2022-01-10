# Mission-to-Mars
The purpose of the assignment was to scrape Mars information off of multiple sites, capture that 'messy' data within a Mongo Database, and then present it within an HTML page. For this assignment, I used the following libraries with Python:
  - splinter, for loading an automated browser
  - BeautifulSoup, to parse the HTML
  - pandas, to read HTML and create dataframes
  - flask, to host the web app

Unfortunately, my browser would not properly load a specific page by leaving out the element that holds news articles that I needed to scrape. This was an on and off issue that I had been able to remedy multiple times, but the problem continued to resurface. Many steps and actions were taken to reconcile the matter to no avail; this included updating my laptop's drivers, updating Chrome, reinstalling Chrome, and "upgrading" splinter. For anybody reading this, if you have a solution you feel is worth an attempt, please do let me know!

Despite all of this, the app does function properly. I give tremendous credit to my instructor, who spent over two hours with me on a virtual call testing it on his own computer.
