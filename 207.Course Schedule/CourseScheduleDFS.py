class Solution:
    def __init__(self):
        super().__init__()
        # 字典，存储图结构，key为图的课程名，value为其先修课程
        self.mapCoursePre = {}
        # 判断是否存在环
        self.flagCirle = False
        # 存储已经学完几门课程
        self.result = 0
        # self.states = []

    def canFinish(self, numCourses, prerequisites) -> bool:
        # 状态表 0表示未搜索，1表示搜索中，2表示已搜索
        # for i in range(numCourses):
        #     self.states.append(0)
        self.states = [0] * numCourses
        # 构建图及其入度列表
        for pre in prerequisites:
            if pre[1] not in self.mapCoursePre:
                self.mapCoursePre[pre[1]] = [pre[0]]
            else:
                self.mapCoursePre[pre[1]].append(pre[0])

            if pre[0] not in self.mapCoursePre:
                self.mapCoursePre[pre[0]] = []

        for i in range(numCourses):
            if not self.flagCirle and not self.states[i]:
                self.dfs(i)

        return self.result == numCourses
        

            
    def dfs(self, i):
        # 执行深度优先搜索
        self.states[i] = 1
        if i in self.mapCoursePre:
            for pre in self.mapCoursePre[i]:
                if self.states[pre] == 0:
                    self.dfs(pre)
                    if self.flagCirle:
                        return
                elif self.states[pre] == 1:
                    # 表示有环
                    self.flagCirle = True
                    return
        self.states[i] = 2
        self.result += 1

solution = Solution()
print(solution.canFinish(3, [[1,2]]))