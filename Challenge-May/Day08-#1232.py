"""
Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:

    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        #vector1: (x1-x0, y1-y0)  vector2: (x2-x0, y2-y0)
        #cross product of vector1 and vector2
        if len(coordinates) == 2:
            return True
        else:
            v1 = [coordinates[1][0]-coordinates[0][0], coordinates[1][1]-coordinates[0][1]]
            for i in range(2, len(coordinates)):
                v2 = [coordinates[i][0]-coordinates[0][0], coordinates[i][1]-coordinates[0][1]]
                if v1[0]*v2[1] != v1[1]*v2[0]:
                    return False
            return True


if __name__=="__main__":
    S = Solution()
    print(S.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
