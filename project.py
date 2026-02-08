import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

def plot_region_participants(csv_path, mini_count):
    
    df = pd.read_csv(csv_path)
    filtered_df = df[df["count"] >= mini_count]
    result = filtered_df.groupby("region")["count"].sum()

    ax = result.plot(
        kind = "bar",
        color = "skyblue",
        figsize = (6,4)
    )

    for bar in ax.patches:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{int(height)}",
            ha = "center",
            va = "bottom"
        )
    
    plt.title("지역별 참가자 수")
    plt.xlabel("지역")
    plt.ylabel("참여자 수")
    plt.tight_layout()
    plt.savefig("region_participants.png")
    plt.show()

plot_region_participants("test.csv", 30)    