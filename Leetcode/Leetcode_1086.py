"""
Given a list of scores of different students,
return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.
The average score is calculated using integer division.

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
"""

from typing import List
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        new_dict = {}
        for id, score in items:
            if not id in new_dict:
                new_dict[id] = [score]
            else:
                new_dict[id].append(score)

        required_list = []
        for key in new_dict:
            required_average = int(sum(sorted(new_dict[key])[-5:]) / 5)
            required_list.append([key, required_average])

        return required_list


if __name__ == "__main__":
    my_solution =  Solution()
    print(my_solution.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))