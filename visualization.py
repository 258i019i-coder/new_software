import matplotlib.pyplot as plt


# 人口系変数
population_vars = [
    "comm_pop",
    "malepop",
    "male15_19pop",
    "male15_24pop",
    "male15_29pop",
    "allwhitepop",
    "allblackpop"
]


# 犯罪系変数
crime_vars = [
    "other1",
    "property1",
    "public_order1",
    "violent1"
]


def plot_chicago(
    chicago
):

    # 利用可能変数
    available_vars = [
        col for col in chicago.columns
        if col not in [
            "year",
            "community_area",
            "community",
            "commarea_km2"
        ]
    ]


    # Community Area入力

    while True:

        try:

            area = int(
                input(
                    "Community Areaを入力してください（1〜77）: "
                )
            )

            if 1 <= area <= 77:
                break

            print(
                "1〜77の範囲で入力してください"
            )

        except ValueError:

            print(
                "整数で入力してください"
            )



    # 変数一覧

    variable_text = "\n".join(
        [
            f"{i}: {var}"
            for i, var in enumerate(
                available_vars,
                start=1
            )
        ]
    )


    while True:

        selected = input(
            "\n利用可能な変数:\n"
            "----------------\n"
            f"{variable_text}\n"
            "----------------\n"
            "表示する変数番号を入力してください"
            "（カンマ区切り、最大5個）: "
        )


        numbers = [
            x.strip()
            for x in selected.split(",")
        ]


        try:

            numbers = [
                int(x)
                for x in numbers
            ]

        except ValueError:

            print(
                "番号で入力してください"
            )

            continue


        if len(numbers) > 5:

            print(
                "最大5個までです"
            )

            continue


        if not all(
            1 <= x <= len(available_vars)
            for x in numbers
        ):

            print(
                "存在する番号を入力してください"
            )

            continue


        break



    variables = [
        available_vars[i-1]
        for i in numbers
    ]


    print(
        "選択された変数:",
        variables
    )



    data = (
        chicago[
            chicago["community_area"] == area
        ]
        .sort_values("year")
    )



    if data.empty:

        print(
            "データがありません"
        )

        return



    fig, ax1 = plt.subplots(
        figsize=(10,6)
    )


    pop_selected = [
        v for v in variables
        if v in population_vars
    ]


    crime_selected = [
        v for v in variables
        if v in crime_vars
    ]



    # 人口

    for var in pop_selected:

        ax1.plot(
            data["year"],
            data[var],
            marker="o",
            label=var
        )


    if pop_selected:

        ax1.set_ylabel(
            "Population"
        )



    # 犯罪

    ax2 = None


    if crime_selected:

        ax2 = ax1.twinx()


        for var in crime_selected:

            ax2.plot(
                data["year"],
                data[var],
                marker="x",
                linestyle="--",
                label=var
            )


        ax2.set_ylabel(
            "Crime Count"
        )



    # 凡例

    lines1, labels1 = (
        ax1.get_legend_handles_labels()
    )


    if ax2:

        lines2, labels2 = (
            ax2.get_legend_handles_labels()
        )


        ax1.legend(
            lines1 + lines2,
            labels1 + labels2
        )

    else:

        ax1.legend()



    ax1.set_xticks(
        data["year"]
    )


    ax1.set_xlabel(
        "Year"
    )


    plt.title(
        f"Trend in Community Area {area}"
    )


    plt.grid(
        True
    )


    plt.show()