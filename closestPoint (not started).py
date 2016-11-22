#finds the closest point

def closestPoint(point, pointMap):
    from scipy.spatial.distance import cdist

    def closest_node(node, nodes):
        return nodes[cdist([node], nodes).argmin()]

    return closest_node(point, pointMap)
