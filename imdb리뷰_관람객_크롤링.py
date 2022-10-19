from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def get_rev_list(driver):
    soup= BeautifulSoup(driver.page_source, 'html.parser')
    ratings = []
    titles = []
    reviews = []
    box_list = soup.select("div.lister > div.lister-list > div")
    for box in box_list:
        try:
            rating= box.select_one('span.rating-other-user-rating > span').text
        except:
            rating= None
        ratings.append(rating)
        title= box.select_one('div.lister-item-content > a').text
        titles.append(title)
        review= box.select_one('div.lister-item-content > div.content > div').text
        reviews.append(review)
    return {'ratings':ratings, 'titles':titles, 'reviews':reviews}

def selenium_service(url, TIMEOUT):
    try: 
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(3)
        
        #load more 클릭
        for k in range(99999):
            try:
                driver.find_element(by=By.ID, value="load-more-trigger").click()
                time.sleep(TIMEOUT)
            except Exception:
                print('더이상 "Load More" 없음')
                break
    
        driver.find_element(by=By.CSS_SELECTOR, value="div.ipl-expander").click()
        time.sleep(TIMEOUT)
        
        rev_df = pd.DataFrame(get_rev_list(driver))
        return rev_df

    except Exception:
        raise
    
    finally:
        if driver is not None:
            driver.quit()


### 실행코드 ###
# 영화코드 입력 : 기생충  'tt6751668', 범죄도시 'tt15838850'
movie_code = ''
url = f'https://www.imdb.com/title/{movie_code}/reviews?ref_=tturv_ql_3'
TIMEOUT=3
rev_df = selenium_service(url, TIMEOUT)
print(rev_df.info())

# csv로 저장 > 파일 이름 입력
title = '.csv'
rev_df.to_csv(title)
