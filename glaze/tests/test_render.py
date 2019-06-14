import numpy as np
import pytest
from glaze import render

contour1 = np.random.randn(5, 3, 2)
contour2 = np.random.randn(2, 3, 2)
contour3 = np.random.randn(1, 3, 2)


def test_render_args():
    assert render(contour1)
    assert render(contour1, contour2)
    assert render(contour1, contour2, contour3)

    assert render([contour1])
    assert render([contour1, contour2])
    assert render([contour1, contour2, contour3])


def test_render_raises_valueerror():
    invalid_inputs = [
        [],
        [contour1, 1],
        [contour1, contour2, contour3, contour3],
        [[]],
        [[contour1, 1]],
        [[contour1, contour2, contour3, contour3]],
    ]

    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError):
            render(*invalid_input)
