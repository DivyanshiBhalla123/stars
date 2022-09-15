from bs4 import BeautifulSoup
import time
import csv
START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=["name","distance","mass","radius"]
    stars_data=[]
    for i in range(0,509):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            tem_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:
                    tem_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        tem_list.append(li_tag.contents[0])
                    except:
                        tem_list.append("")
            stars_data.append(tem_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper2.csv","w")as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)
scrape()        

