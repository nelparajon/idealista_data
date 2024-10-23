import pandas as pd
import searching
import process_data

def extract_data(province):
    url, params = searching.define_search_url(province)
    result = searching.search_api(url, params)
    return result

def data_convertion(result):
    df = process_data.convert_result_to_df(result)
    return df

def concatenate_dfs(df, t_df):
    total_df = process_data.concat_dfs(df, t_df)
    return total_df

def save_data(df, province):
    df_csv = process_data.save_df_to_csv(df, province)
    return df_csv

def load_data():
    df = process_data.load_data()
    return df
    
def main_process(province):
    first_result = extract_data(province)
    first_df = data_convertion(first_result)
    total_pages = first_result['totalPages']
    print(f'TOTAL PAGES: {total_pages}')
    t_df = pd.DataFrame()
    total_df = concatenate_dfs(first_df, t_df)
    for i in range(2, total_pages):
        result = extract_data(province)
        df = data_convertion(result)
        total_df = concatenate_dfs(df, total_df)

    save_data(total_df, province)
    df = load_data()
    print(df.head())

def menu():
    province = input("Enter the name of the province you want to extract the dataset in csv format: ")
    main_process(province)

    

if __name__ == '__main__':
    menu()
    
    
    


