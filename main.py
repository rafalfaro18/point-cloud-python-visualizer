import open3d as o3d

pcd = o3d.io.read_point_cloud('sfm.ply')
o3d.visualization.draw_geometries([pcd])

voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,voxel_size=0.004)
o3d.visualization.draw_geometries([voxel_grid])