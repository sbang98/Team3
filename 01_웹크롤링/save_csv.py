#데이터프레임형식으로 변환 및 저장
def save_csv(data, index, title):
    import pandas as pd
    news_table = pd.DataFrame(data, index=index)
    news_table.to_csv(title)
