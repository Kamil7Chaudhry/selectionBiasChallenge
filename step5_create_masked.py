import numpy as np


def create_masked_stipple(stipple_img: np.ndarray, mask_img: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    """
    Applies a block letter mask to a stippled image.
    Parameters:
        stipple_img: 2D numpy array of the stippled image (values in [0, 1])
        mask_img: 2D numpy array of the block letter (values in [0, 1])
        threshold: cutoff to decide what counts as the mask (default 0.5)
    Returns:
        2D numpy array same shape as inputs
        Where mask is dark (below threshold) stipples are removed (set to white 1.0)
        Where mask is light (above threshold) stipples are kept as they are
    """
    result = stipple_img.copy()
    result[mask_img < threshold] = 1.0
    return result


if __name__ == "__main__":
    stipple = np.random.choice([0.0, 1.0], size=(375, 250), p=[0.08, 0.92])
    mask = np.ones((375, 250))
    mask[100:300, 50:200] = 0.0
    result = create_masked_stipple(stipple, mask)
    print(f"Shape: {result.shape}")
    print(f"Stipple dots kept: {np.sum(result == 0.0)}")