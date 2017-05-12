from selenium import webdriver

import codecs
import time

# Run this script twice, for page=1 and page=2
# TODO: automate the process
URL = "https://hackerone.com/directory?query=type%3Ahackerone&sort=published_at%3Adescending&page=1"
# URL = "https://hackerone.com/directory?query=type%3Ahackerone&sort=published_at%3Adescending&page=2"

OUTPUT = "../output/hackerone_programs.txt"
output_file = codecs.open(OUTPUT, "a", "utf-8", buffering=0)

driver = webdriver.Firefox()
driver.get(URL)
assert "Directory" in driver.title

# HackerOne apparently uses a lot of javascript, so we need to wait for the loading to complete.
# TODO: We should find a more reliable solution.
time.sleep(2)

programs = driver.find_elements_by_xpath('//a[@class="leaderboard-user__name spec-profile-name-with-popover"]')

print(len(programs))

for program in programs:
    output_file.write(program.get_attribute("href") + "\n")

driver.close()
output_file.close()


