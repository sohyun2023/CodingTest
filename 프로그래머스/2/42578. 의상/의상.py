import pandas as pd

def solution(clothes):
    
    df = pd.DataFrame(clothes, columns=['name', 'type'])
    
    
    new_df = df['type'].value_counts().reset_index()
    new_df.columns = ['type', 'count']
    
    totalsum = 1
    
    
    for count in new_df['count']:
        totalsum *= (count + 1)
    
    
    totalsum -= 1
    
    return totalsum