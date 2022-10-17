import seaborn as sb
import json
import matplotlib.pyplot as pl
import pandas as pd
import os
import numpy as np
sb.set_theme(style="ticks")


def main(pickle_path):

    df = pd.read_pickle(pickle_path)

    BASE_DIR = os.path.dirname(pickle_path)
    json_path = os.path.join(BASE_DIR, "project_meta.json")

    with open(json_path, 'r') as openfile:
        meta = json.load(openfile)

    subgroups = ['project','subject','session','acquisition']

    for group in subgroups:
        f, ax = pl.subplots(1, 1, figsize=(17, 8.5))
        pos = [0.7, 0.08, 0.3, 0.8]
        ax.set_position(pos)
        working_df = df[df['query'].str.startswith(group)]

        sb.boxplot(x="time", y="query", data=working_df,
                    whis=[0, 100], width=.6, palette="vlag", ax=ax)

        # Add in points to show each observation
        sb.stripplot(x="time", y="query", data=working_df,
                      size=4, color=".3", linewidth=0, ax=ax)

        # Tweak the visual presentation
        ax.xaxis.grid(True)
        ax.set(ylabel="Time (s)")
        ax.set(title="API call time (s)")
        sb.despine(trim=True, left=True)


        title = f"{df['site'][0]}\nSITE: #projects: {meta['nproj']}, PROJECT: #sub: {meta['nsub']}, #ses: {meta['nses']}, #acq: {meta['nacq']}"

        f.suptitle(title)
        xn,xm = ax.get_xlim()

        newmin = min(5.0, xm)
        newticks = np.linspace(0, newmin, 4)
        new_tick_labels = [str(a) for a in newticks]

        ax.set_xlim(0, newmin)
        ax.set_xticks(newticks)
        ax.set_xticklabels(new_tick_labels)

        file_out=os.path.join(BASE_DIR,f"{group}_report.png")
        pl.savefig(file_out, dpi='figure', format="png")
        pl.close()