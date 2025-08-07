import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def read_csv(file_path):
    """
    Reads a CSV file and returns a DataFrame.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    df = pd.read_csv(path,skipfooter=1)
    age = df['Age'].fillna(df['Age'].mean())
    salary = df['Salary'].fillna(df['Salary'].mean())
    length = age.shape[0]
    return length,age, salary

def plot_nba_data(age,salary,length):

    """
    Plots NBA data using matplotlib.

    Parameters:
    data (pd.DataFrame): DataFrame containing NBA statistics with columns 'Player', 'Points', 'Assists', 'Rebounds'.

    Returns:
    None
    """
    #创建画布
    fig = plt.figure(figsize=(10, 6),dpi=300)
    #添加子图
    axes =fig.subplots()
    line1, = axes.plot(range(1,length+1),age,label='Age',color='blue',linestyle='--',marker='o')
    line2, = axes.plot(range(1,length+1),salary,label='Salary',color='red',linestyle='--',marker='o')
    #坐标轴标签
    axes.set_xlabel(xlabel='Player Number')
    axes.set_ylabel(ylabel='Age/Salary')
    axes.set_title(label='NBA Player Age and Salary')
    #坐标轴倾斜
    axes.tick_params(axis='x',rotation=45)
    #图例
    axes.legend(handles=[line1,line2,],loc='best')
    #网格
    axes.grid(linestyle='--',alpha=0.5)
    #展示
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    file_path = 'data\\nba.csv'
    length,age,salary = read_csv(file_path)
    print(f"Number of players: {length}")
    plot_nba_data(age,salary,length)
    