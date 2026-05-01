import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def create_statistics_meme(
    original_img: np.ndarray,
    stipple_img: np.ndarray,
    block_letter_img: np.ndarray,
    masked_stipple_img: np.ndarray,
    output_path: str,
    dpi: int = 150,
    background_color: str = "white"
) -> None:
    """
    Assembles four panels into a statistics meme and saves it as a PNG.
    Parameters:
        original_img: 2D numpy array of the original grayscale image
        stipple_img: 2D numpy array of the stippled image
        block_letter_img: 2D numpy array of the block letter S
        masked_stipple_img: 2D numpy array of the masked stipple image
        output_path: file path to save the PNG
        dpi: image resolution (default 150)
        background_color: background color of the figure (default white)
    """
    fig = plt.figure(figsize=(16, 5), facecolor=background_color)
    gs = GridSpec(2, 4, figure=fig, height_ratios=[0.12, 1], hspace=0.05, wspace=0.05)

    panels = [
        (original_img,       "Reality",                "The true population"),
        (stipple_img,         "Your Model",             "Your data collection"),
        (block_letter_img,    "Selection Bias",         "Systematic missing data"),
        (masked_stipple_img,  "Estimate\n('seems legit')", "The biased result"),
    ]

    label_colors = ["#2c2c2c", "#2c2c2c", "#c0392b", "#2c2c2c"]

    for i, (img, title, subtitle) in enumerate(panels):
        ax_title = fig.add_subplot(gs[0, i])
        ax_title.set_facecolor("#f0f0f0" if i != 2 else "#fdecea")
        ax_title.text(
            0.5, 0.5, title,
            ha="center", va="center",
            fontsize=13, fontweight="bold",
            color=label_colors[i],
            transform=ax_title.transAxes
        )
        ax_title.set_xticks([])
        ax_title.set_yticks([])
        for spine in ax_title.spines.values():
            spine.set_edgecolor("#cccccc")
            spine.set_linewidth(0.8)

        ax_img = fig.add_subplot(gs[1, i])
        ax_img.imshow(img, cmap="gray", vmin=0, vmax=1, aspect="auto")
        ax_img.set_xticks([])
        ax_img.set_yticks([])
        for spine in ax_img.spines.values():
            spine.set_edgecolor("#cccccc")
            spine.set_linewidth(0.8)

    plt.savefig(output_path, dpi=dpi, bbox_inches="tight",
                facecolor=background_color, edgecolor="none")
    plt.close()
    print(f"Meme saved to {output_path}")


if __name__ == "__main__":
    dummy = np.ones((375, 250)) * 0.8
    create_statistics_meme(dummy, dummy, dummy, dummy, "test_meme.png")
    print("Test meme created.")