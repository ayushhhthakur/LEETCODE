import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    merged = views.merge(views, left_on=['author_id', 'article_id'], right_on=['viewer_id', 'article_id'])
    
    result = merged[merged['author_id_x'] == merged['viewer_id_y']]
    
    result = result[['author_id_x']].rename(columns={'author_id_x': 'id'})
    
    result = result.drop_duplicates().sort_values(by='id', ascending=True)
    
    return result
