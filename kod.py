from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# 1.Úprava
# Nacitanie súboru CSV
df = pd.read_csv(r"c:\Users\randy\OneDrive\Počítač\Heart dataset\heart.csv")

# Distribution graphs (histogram/bar graph) of column data
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]]
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = int((nCol + nGraphPerRow - 1) / nGraphPerRow)  # oprava: int()
    plt.figure(num=None, figsize=(6 * nGraphPerRow, 8 * nGraphRow), dpi=80, facecolor='w', edgecolor='k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation=90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
    plt.show()

# Correlation matrix
def plotCorrelationMatrix(df, graphWidth):
    filename = df.dataframeName
    df = df.dropna(axis='columns')  # oprava: axis
    df = df[[col for col in df if df[col].nunique() > 1]]
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum=1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {filename}', fontsize=15)
    plt.show()

# Scatter and density plots
def plotScatterMatrix(df, plotSize, textSize):
    df = df.select_dtypes(include=[np.number])
    df = df.dropna(axis='columns')
    df = df[[col for col in df if df[col].nunique() > 1]]
    columnNames = list(df)
    if len(columnNames) > 10:
        columnNames = columnNames[:10]
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df.corr().values
    for i in range(len(corrs)):
        for j in range(i+1, len(corrs)):
            ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j],
                              (0.8, 0.2),
                              xycoords='axes fraction',
                              ha='center', va='center',
                              size=textSize)
    plt.suptitle('Scatter and Density Plot')
    plt.show()

# ======== načítanie CSV ========
#nRowsRead = None  # specify 'None' if want to read whole file
#df1 = pd.read_csv(r"c:\Users\randy\OneDrive\Počítač\Heart dataset\heart.csv", delimiter=",", nrows=nRowsRead)
#df1.dataframeName = 'heart.csv'
#nRow, nCol = df1.shape
#print(f'There are {nRow} rows and {nCol} columns')

# Krok 1 
print('Prvých 5 riadkov: ')
print(df.head())

# Krok 2
print("\nPočet 0. hodnôt v stĺpcoch:")
print(df.isnull().sum())

# Odstránenie chýbajúcich hodnôt
# V datasete by nemali byť žiadne riadky bez pridelenej hodnoty(hodnoty 0 sú v tomto datasete platné)
# Takže tento príkaz by teoreticky nemal v podstate kde vymazať riadky kedže riadky bez hodnoty by tu nemali byť
df = df.dropna()


# Krok 3 – Základná analýza 
print("\nZákladné štatistiky o dátach:")
print(df.describe())

print("\nPočet riadkov a stĺpcov v datasete:")
print(df.shape)

# Krok 4 – Vizualizácia dát 
# Histogram jedného stĺpca (napr. vek – 'age')
df['age'].hist()
plt.title("Rozdelenie veku pacientov")
plt.xlabel("Vek")
plt.ylabel("Počet")
plt.show()

# Histogram ďalšieho stĺpca (napr. cholesterol – 'chol')
df['chol'].hist()
plt.title("Rozdelenie cholesterolu pacientov")
plt.xlabel("Cholesterol")
plt.ylabel("Počet")
plt.show()