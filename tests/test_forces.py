import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.transforms import Affine2D

def draw_arced_arrow(ax, start, end, radius=0.2, arrowstyle='-|>', color='b', linewidth=1):
    # Calculate the angle between the start and end points
    angle = 180  # This is the default angle for a semicircular arrow
    center = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
    
    # Create a FancyArrowPatch
    arrow = FancyArrowPatch(
        start, end,
        arrowstyle=arrowstyle,
        mutation_scale=10,
        color=color,
        linewidth=linewidth,
        shrinkA=0,  # No shrinking at the start point
        shrinkB=0,  # No shrinking at the end point
    )

    # Create an Affine2D transformation to rotate the arrow and set its center
    transform = Affine2D().rotate(angle, center=center)
    arrow.set_transform(transform + ax.transData)
    
    ax.add_patch(arrow)

# Example usage:
fig, ax = plt.subplots()
ax.set_aspect('equal', adjustable='box')

start_point = (1, 1)
end_point = (4, 1)
draw_arced_arrow(ax, start_point, end_point, radius=0.2, arrowstyle='-|>', color='b', linewidth=2)

plt.xlim(0, 5)
plt.ylim(0, 2)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.show()
