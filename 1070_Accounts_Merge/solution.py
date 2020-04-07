class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """

    """
    Solution 1: DFS in undirected graph
    """
    def accountsMerge(self, accounts):
        results = []
        if not accounts:
            return results
        
        email_to_name = {}
        graph = collections.defaultdict(set)
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                # connect the graph
                graph[email].add(account[1])
                graph[account[1]].add(email)
        
        visited = set([])
        for e in graph:
            if e not in visited:
                visited.add(e)
                email_list = []
                self.dfs(e, graph, visited, email_list)
                results.append([email_to_name[e]] + sorted(email_list))
                
        return results
    
    def dfs(self, e, graph, visited, email_list):
        email_list.append(e)
        for neighbor in graph[e]:
            if neighbor not in visited:
                visited.add(neighbor)
                self.dfs(neighbor, graph, visited, email_list)

    """
    Solution 2: Union Find
    """
    def __init__(self):
        self.father = {}
        
    def accountsMerge(self, accounts):
        # initialize each account is its own father
        for id in range(len(accounts)):
            self.father[id] = id
        
        # each email is map to the account id
        email_to_ids = {}
        for id, account in enumerate(accounts):
            for email in account[1:]:
                email_to_ids[email] = email_to_ids.get(email, []) + [id]
                # connect each id to the main id
                self.union(id, email_to_ids[email][0])
        
        # find each id's father id then add the email address
        id_to_email_set = collections.defaultdict(set)
        for user_id, account in enumerate(accounts):
            root_user_id = self.find(user_id)
            for email in account[1:]:
                id_to_email_set[root_user_id].add(email)
        
        # format the output
        merged_accounts = []
        for user_id, email_set in id_to_email_set.items():
            new_lst = [accounts[user_id][0]] + sorted(email_set)
            merged_accounts.append(new_lst)
        return merged_accounts
            
    def union(self, id_1, id_2):
        father_1 = self.find(id_1)
        father_2 = self.find(id_2)
        if father_1 != father_2:
            self.father[father_1] = father_2
    
    def find(self, id):
        if self.father[id] == id:
            return id
        self.father[id] = self.find(self.father[id])
        return self.father[id]