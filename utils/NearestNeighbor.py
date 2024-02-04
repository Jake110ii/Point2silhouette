import numpy as np

class NearestNeighbor:
    def __init__(self, points):
        self.points = points
        self.n = len(points)
        self.visited = [False] * self.n
        self.tour = [None] * self.n

    def calculate_distance(self, point1, point2):
        return np.linalg.norm(np.array(point1) - np.array(point2))

    def nearest_neighbor_algorithm(self):
        self.tour[0] = self.points[0]
        self.visited[0] = True

        for i in range(1, self.n):
            min_distance = float('inf')
            nearest_point = None

            for j in range(self.n):
                if not self.visited[j]:
                    distance = self.calculate_distance(self.tour[i-1], self.points[j])
                    if distance < min_distance:
                        min_distance = distance
                        nearest_point = j

            self.tour[i] = self.points[nearest_point]
            self.visited[nearest_point] = True

        return self.tour

def align_lists_to_numpy_array(x_list, y_list):
    # x_listとy_listの長さが一致していることを確認
    if len(x_list) != len(y_list):
        raise ValueError("x_list and y_list must have the same length.")

    # (x[0], y[0])から始まるnumpyの2次元配列を作成
    array_result = np.array([x_list, y_list]).T

    return array_result


def nearest_sort(x_list, y_list):
    # 10点の座標の例
    #x_list = [1, 5, 3, 8, 5]
    #y_list = [10, 50, 30, 80, 50]
    points = align_lists_to_numpy_array(x_list, y_list)

    # NearestNeighborクラスのインスタンスを作成
    nn_solver = NearestNeighbor(points)

    # 最寄り隣接法を実行
    result_tour = nn_solver.nearest_neighbor_algorithm()
    result_distance = sum(nn_solver.calculate_distance(result_tour[i], result_tour[i+1]) for i in range(len(result_tour)-1))
    
    out_x_list = np.array(result_tour)[:, 0].tolist()
    out_y_list = np.array(result_tour)[:, 1].tolist()
    return out_x_list, out_y_list

    
def main():
    # 10点の座標の例
    points = [(0, 0), (1, 1), (6, 6), (7, 7), (2, 2), (3, 3), (8, 8), (9, 9), (4, 4), (5, 5)]

    # NearestNeighborクラスのインスタンスを作成
    nn_solver = NearestNeighbor(points)

    # 最寄り隣接法を実行
    result_tour = nn_solver.nearest_neighbor_algorithm()
    result_distance = sum(nn_solver.calculate_distance(result_tour[i], result_tour[i+1]) for i in range(len(result_tour)-1))

    print("最短経路:", result_tour)
    print("最短距離:", result_distance)
    print(points)

if __name__ == "__main__":
    main()
