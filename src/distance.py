import pandas as pd
import numpy as np

# 创建DataFrame
data = {
"City": ["Tokyo", "Los Angeles", "London"],
"Latitude": [35.6895, 34.0522, 51.5074],
"Longitude": [139.6917, -118.2437, -0.1278],
}
df = pd.DataFrame(data)

def haversine(lat1,lon1,lat2,lon2):
    """
    计算两个地理坐标点之间的Haversine距离。

    参数:
    lat1, lon1: 初始坐标向量（以度为单位）
    lat2, lon2: 坐标矩阵（以度为单位）

    返回:
    两个点之间的距离（以公里为单位）
    """
    R = 6371.0  # 地球半径，单位为公里

    # 将角度转换为弧度
    lat1_rad = np.deg2rad(lat1)
    lon1_rad = np.deg2rad(lon1)
    lat2_rad = np.deg2rad(lat2)
    lon2_rad = np.deg2rad(lon2)
    print(lat1_rad,lon1_rad,lat2_rad,lon2_rad)

    # 计算差值
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    print(dlat,dlon)
    # Haversine公式
    a = (np.sin(dlat / 2) ** 2
    + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2)** 2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c

    return distance

def location(datafeame):
    """
    基于datafame，返回城市经纬度矩阵
    """
    lat_ori = df['Latitude'].values
    lon_ori = df['Longitude'].values
    #将一维向量转换为列向量
    lat = lat_ori.reshape(-1, 1)
    lon = lon_ori.reshape(-1, 1)
    #计算经纬度矩阵
    lat_matrix = np.tile(lat_ori,(len(lat_ori),1))
    lon_matrix = np.tile(lon_ori,(len(lon_ori),1))

    return lat,lon,lat_matrix,lon_matrix

def calculate_distance():
    """ 计算城市之间的Haversine距离矩阵。"""
    lat,lon,lat_matrix,lon_matrix = location(df)
    print(lat,lon,lat_matrix,lon_matrix)
    haversine_matrix = haversine(lat,lon,lat_matrix,lon_matrix)
    #转换为dataframe
    return pd.DataFrame(haversine_matrix,index=df['City'].values,columns=df['City'].values)

distance_df = calculate_distance()
print("Haversine Distance Matrix (in km):")
print(distance_df)