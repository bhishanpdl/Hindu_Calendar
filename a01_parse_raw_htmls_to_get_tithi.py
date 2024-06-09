import bs4
import pandas as pd
import glob

def get_tithi_start_end_from_astroica(fname):
    dfs = pd.read_html(fname)
    df = dfs[0]

    tts = df[0].values
    del df[2] # we dont want last column, which is same as second column somehow

    df['start_time'] = df[1].str[0:39].str.replace('Start Time : ', '', regex=False)
    df['end_time'] = df[1].str[39:].str.replace('End Time : ', '', regex=False)

    # Convert the columns to datetime
    df['start_time'] = pd.to_datetime(df['start_time'], format='%a, %d %b %Y, %I:%M %p')
    df['end_time'] = pd.to_datetime(df['end_time'], format='%a, %d %b %Y, %I:%M %p')

    del df[1]
    df.columns = ['tithi', 'start_time','end_time']

    month = fname.split('/')[1]
    ofile = f'data/astroica_tithi_start_end_{month}.csv'

    print(f'Writing: {ofile}')
    df.to_csv(ofile,index=False)


if __name__ == '__main__':
    fnames = glob.glob("data/*/*.html")
    for fname in fnames:
        get_tithi_start_end_from_astroica(fname)
    # combine these files
    fnames = glob.glob("data/*.csv")
    dfs = [pd.read_csv(fname) for fname in fnames]
    df = pd.concat(dfs,axis=0,ignore_index=True)
    df = df.drop_duplicates()
    df.to_csv('astroica_tithi_start_end.csv',index=False)
