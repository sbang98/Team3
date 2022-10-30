import requests
from bs4 import BeautifulSoup

#리뷰추출
def get_review_pro(box, route):
    point = box.select_one('div em').text
    if route == 'div.score_result ul li':
        review = box.select_one('div p').text
    else:
        review = box.select_one('p.tx_report').text
    return { "point": point, "review": review}

def get_page_reviews_pro(url, route) :
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    elements = soup.select(route)
    return  [get_review_pro(element, route)   for element in elements ] 



#####실행코드

#전문가 리뷰 추출 > 영화코드 입력
movie_code = 
review_pro_list=[]
review_pro_list.extend(get_page_reviews_pro(f'https://movie.naver.com/movie/bi/mi/point.naver?code={movie_code}', 'div.reporter ul li'))
review_pro_list.extend(get_page_reviews_pro(f'https://movie.naver.com/movie/bi/mi/point.naver?code={movie_code}', 'div.score_result ul li'))


#데이터 프레임 저장 > 파일명 입력
from save_csv import save_csv
data = review_pro_list
title = '.csv'
save_csv(data=data, index=None, title=title)
