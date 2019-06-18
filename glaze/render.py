import bezier
import matplotlib.pyplot as plt
import numpy as np


def _validate_glyph(args):
    """ Whatever the input is, return a list of correctly-shaped contours. """
    if len(args) == 1 and isinstance(args[0], list):
        glyph = args[0]
    else:
        glyph = list(args)

    if (not glyph) or (len(glyph) > 3):
        msg = "Expected glyph with 1, 2 or 3 contours, got {} contours.".format(
            len(glyph)
        )
        raise ValueError(msg)
    for i, contour in enumerate(glyph):
        if not isinstance(contour, np.ndarray):
            msg = "Expected contour of type np.ndarray, got contour #{} of type {}.".format(
                i + 1, type(contour).__name__
            )
            raise ValueError(msg)
        if len(contour.shape) != 3 or contour.shape[-2:] != (3, 2):
            msg = "Expected contour with shape (*, 3, 2), got contour #{} of shape {}.".format(
                i + 1, contour.shape
            )
            raise ValueError(msg)

    return glyph


def render(*args, num_points=32, lim=[-0.3, 1.2], grid=False):
    """
    Renders one glyph.

    Parameters
    ----------
    *args
        Up to three np.ndarrays, where each array has shape [*, 3, 2], or a list
        of such np.ndarrays.
    num_points : int
        Number of points per Bezier curve. Defaults to 32.
    lim : list
        x and y limits of rendered glyph. Defaults to [-0.3, 1.2].
    grid : boolean
        If True, overlays axes and gridlines. Defaults to False.

    Returns
    -------
    fig : matplotlib.pyplot.Figure
        Rendered glyph.

    Examples
    --------
    ```python
    import numpy as np
    from glaze import render

    contour1 = np.random.randn(10, 3, 2)
    contour2 = np.random.randn(7, 3, 2)
    contour3 = np.random.randn(5, 3, 2)

    # The following are equivalent.
    fig = render(contour1, contour2, contour3)
    fig = render([contour1, contour2, contour3])
    ```
    """
    glyph = _validate_glyph(args)

    fig = plt.figure()
    ax = plt.gca()

    for contour in glyph:
        contour = np.transpose(contour, axes=(0, 2, 1)).astype(np.float64)
        for curve in contour:
            curve = bezier.Curve(curve, degree=2)
            curve.plot(num_pts=num_points, ax=ax)

    ax.set_aspect("equal")
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)

    if grid:
        ax.spines["right"].set_visible(False)
        ax.spines["top"].set_visible(False)
        ax.grid()
    else:
        ax.axis("off")

    return fig
