import pandas
from pathlib import Path

def search(csv_path):
    path = Path(csv_path)

    if not path.exists():
        print(csv_path, "does not exist")
        return 
    if not path.is_file():
        print("path is not a file")
    
    if path.suffix.lower() != '.csv':
        print(csv_path, "is not a .csv file")

    try:
        dataframe = pandas.read_csv(csv_path, low_memory=False)
    except Exception as e:
        print(csv_path, "could not be loaded")
    
    print("CSV Search - Salford 100 Hackathon")

    while True:
        try:
            q = input("Search: ").strip()
        except KeyboardInterrupt:
            print("exit")
            break
        if q.lower() in ['quit', 'exit', 'q']:
            print("exit")
            break

        if not q:
            continue

        mask = pandas.Series(False, index = dataframe.index)

        try:
            for column in dataframe.columns:
                try:
                    column_mask = dataframe[column].astype(str).str.contains(q)
                    mask |= column_mask
                except:
                    pass

            matches = dataframe[mask]

            if len(matches) == 0:
                print("no matches for '",q,"'\n")
            else:
                print("found",len(matches),"for", q, "\n")
                with pandas.option_context(
                    'display.max_rows', 300000000000000,
                    'display.max_columns', 3000000000,
                    'display.width', 20000000000000000,
                    'display.max_colwidth', 18000000000000000
                ):
                
                    print(matches.to_string(index=False))
        except Exception as e:
            print("search failed")


search('businesses.csv')