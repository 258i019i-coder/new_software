from crime import create_crime_summary
from acs import create_acs_summary
from merge import create_chicago
from visualization import plot_chicago

def main():

    # 1. Crimeデータのクリーニング
    crime_summary = create_crime_summary()

    # 2. ACSデータのクリーニング
    acs_summary = create_acs_summary()

    # 3. データ結合
    chicago = create_chicago(
        crime_summary,
        acs_summary
    )

    # 4. 保存
    chicago.to_csv(
        "chicago.csv",
        index=False
    )

    print("Chicago dataset created.")


    # 5. グラフ描画
    plot_chicago(
        chicago
        )

    return chicago

if __name__ == "__main__":
    main()