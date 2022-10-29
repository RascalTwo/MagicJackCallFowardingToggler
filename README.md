# MagicJack Call Fowarding Toggle

Toggle the call-forwarding status of a MagicJack number with a single script.

https://user-images.githubusercontent.com/9403665/131439320-d292e3f7-ff15-4ba1-8132-ea2565406e5c.mp4

## How It's Made

**Tech Used:** Python 2, Selenium

After inspecting the user flow to login to the MagicJack website, navigate to the call forwarding page, and toggle the call forwarding status, I was able to automate the process with Selenium.

## Optimizations

Currently the username and password are read via standard input, making this use environment variables or another easily-accessible method of storing credentials. The next optimization would be looking into using something lighter, from explicit HTTP requests, to another headless browser such as Playwright, etc.
