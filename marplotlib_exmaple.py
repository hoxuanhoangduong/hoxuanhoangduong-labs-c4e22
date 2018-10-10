from matplotlib import pyplot

# 1. Prepare data
machine_counts = [18, 4, 2]

# 2. prepare labels 
machine_names = ["PC", "Mac", "Linux"]

# 3 . draw pipe
pyplot.pie(machine_counts, labels = machine_names, autopct="%.1f", shadow=True, explode=[0, 0.2, 0])
pyplot.title("PC vs MAC and Linux usage")
pyplot.axis("equal")
# 4 . show
pyplot.show()