from matplotlib import pyplot as plt


def draw(x, y):
    # set up range of the plot
    limit = max(x, y) + 1

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')

    # lines corresponding to x- and y-coordinates
    plt.plot([x, x], [0, y], '-', c='blue', linewidth=3)
    plt.plot([0, x], [y, y], '-', c='blue', linewidth=3)

    plt.scatter(x, y, s=100, marker='o', c='red')  # actual point

    ax.set_xlim((-limit, limit))
    ax.set_ylim((-limit, limit))

    # axis arrows
    left, right = ax.get_xlim()
    bottom, top = ax.get_ylim()
    draw_arrow(left, right, bottom, top)

    plt.grid()
    plt.show()


def draw_arrow(left, right, bottom, top):
    plt.arrow(left, 0, right - left, 0, length_includes_head=True,
              head_width=0.15)
    plt.arrow(0, bottom, 0, top - bottom, length_includes_head=True,
              head_width=0.15)
