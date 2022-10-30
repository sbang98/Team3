import requests
from bs4 import BeautifulSoup
import math

#리뷰추출
def get_review_viewer(box):
    rating = box.select_one('div em').text
    try:
        review = box.select_one('div p span a')['data-src']
    except:
        review = box.select_one('div p').text
    return { "ratings": rating, "reviews": review.replace('\n관람객','').replace('\t', '').replace('\n', '').replace('\r', '')}

def get_page_reviews(url) :
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    elements = soup.select('div.score_result ul li')
    return  [get_review_viewer(element)   for element in elements ]


#전체 리뷰 수 추출
def get_all_review_count(url) : 
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    all_review_count = soup.select_one('div.score_total strong em').text # 정상 경로로 수정 필요
    return all_review_count



#####실행코드

#전체 리뷰 추출 > 영화코드 & 전체 리뷰 수 입력
#범죄도시 코드 192608, 기생충 코드 161967
movie_code = 
url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='
all_review_count = int(get_all_review_count(url+str(1)).replace(',',''))

last_num = math.ceil(all_review_count/10)+1
review_list=[]
for i in range(1, last_num) :
    review_list.extend(get_page_reviews(url+str(i)))


#데이터 프레임 저장 > 파일명 입력
from save_csv import save_csv
data = review_list
title = '.csv'
save_csv(data=data, index=None, title=title)
