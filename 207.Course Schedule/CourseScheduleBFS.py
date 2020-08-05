import queue

class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        # 字典，存储图结构，key为图的课程名，value为其先修课程
        mapCoursePre = {}
        # list， 存储入度列表
        indegrees = [0] * numCourses
        # 存储已经学完几门课程
        result = 0

        # 构建图及其入度列表
        for pre in prerequisites:
            if pre[1] not in mapCoursePre:
                mapCoursePre[pre[1]] = [pre[0]]
            else:
                mapCoursePre[pre[1]].append(pre[0])
            # if pre[0] not in mapCoursePre:
            #     mapCoursePre[pre[0]] = []
            indegrees[pre[0]] += 1

        # 定义队列并将入度为0的定点加入到队列中
        q = queue.Queue()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.put_nowait(i)

        # BTS
        while not q.empty():
            course = q.get_nowait()
            # q.task_done()

            result += 1
            if course in mapCoursePre:
                for preCourse in mapCoursePre[course]:
                    indegrees[preCourse] -= 1
                    if indegrees[preCourse] == 0:
                        q.put(preCourse)

        
        return result == numCourses
            
solution = Solution()
print(solution.canFinish(2, [[1,0], [0,1]]))

