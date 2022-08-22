import open3d as o3d
import numpy as np

# print(o3d.__version__)

# check properties
def check_property(mesh):
    edge_manifold = mesh.is_edge_manifold(allow_boundary_edges=True)
    edge_manifold_boundary = mesh.is_edge_manifold(allow_boundary_edges=False)
    vertex_manifold = mesh.is_vertex_manifold()
    self_intersecting = mesh.is_self_intersecting()
    watertight = mesh.is_watertight()
    orientable = mesh.is_orientable()

    print(f"  edge_manifold:          {edge_manifold}")
    print(f"  edge_manifold_boundary: {edge_manifold_boundary}")
    print(f"  vertex_manifold:        {vertex_manifold}")
    print(f"  self_intersecting:      {self_intersecting}")
    print(f"  watertight:             {watertight}")
    print(f"  orientable:             {orientable}")


# Vertices and triangles of a mesh
def vert_tri(mesh):
    print("Vertices")
    print(np.asarray(mesh.vertices))
    print("triangles")
    print(np.asarray(mesh.triangles))

# Average filter
def aver_filter(mesh, n_iter):
    print(f"filter with average with {n_iter} iteration(s)")
    mesh_out = mesh.filter_smooth_simple(number_of_iterations=n_iter)
    # # computing normal
    mesh_out.compute_vertex_normals()

    # # Rendering a mesh
    o3d.visualization.draw_geometries([mesh])


if __name__ == '__main__':
    """ Opening and viewing an .obj file """
    obj_data = "shoe.obj"
    mesh = o3d.io.read_triangle_mesh(obj_data)
    # print(mesh)

    # check_property(mesh)

    aver_filter(mesh, 1)
