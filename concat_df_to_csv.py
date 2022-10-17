import pandas as pd
import os
import json

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
site_dir = os.path.join(BASE_DIR, 'Sites')
data_dir = os.path.join(BASE_DIR, "plotter", "dashboard", "data")

def main():

    dirs = [d for d in os.listdir(site_dir) if os.path.isdir(d) and not d.startswith('_') and not d.startswith('.')]

    df_list = []

    for dir in dirs:
        print(dir)
        df_pickle = os.path.join(dir, 'call_time_df.pkl')

        if not os.path.exists(df_pickle):
            continue

        df = pd.read_pickle(df_pickle)

        json_path = os.path.join(dir, "project_meta.json")

        with open(json_path, 'r') as openfile:
            meta = json.load(openfile)

        df['NProjects']=meta['nproj']
        df['NSubjects']=meta['nsub']
        df['NSessions']=meta['nses']

        df_list.append(df)

    new_df = pd.concat(df_list, ignore_index=True, sort=False)

    csv_out = os.path.join(BASE_DIR, 'concat_times.csv')
    new_df.to_csv(csv_out)
    DF_PATH = os.path.join(data_dir, "df.pkl")
    new_df.to_pickle(DF_PATH)


if __name__ == "__main__":
    main()
