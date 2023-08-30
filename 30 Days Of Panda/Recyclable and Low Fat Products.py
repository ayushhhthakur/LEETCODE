import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    find_products_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]

    result = find_products_df[['product_id']]
    
    return result
