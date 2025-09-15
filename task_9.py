class UnionFind:
    def __init__(self: "UnionFind", n: int)-> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self: "UnionFind", x:str)->list[str]:
        # this function finds the root of x / parent of x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self: "UnionFind", x: str, y: str)-> None:
        # this functions finds the root of x and of y and unions them according to whose rank is higher
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                # if x's rank is higher than y's , then y is now added to x
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                # in case y's rank is higher than x's
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                # in case of equality then the rank of x will be incremented
                self.rank[rootX] += 1

    def common_words(sentences_list: list[list[str]],threshold: int)-> dict[str,dict[str,list]]:
        ''' this function unions two sentences if they have common words more than threshold.
        then sorts the sentences by their lengths then alphabetically
        and lastly adds them to a dictionary as a result .
        '''
        result_dict = {"Question 9": {"group Matches": []}}
        n = len(sentences_list)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                # Split the sentences into words and find common words

                words_set_i = set(sentences_list[i])
                words_set_j = set(sentences_list[j])

                # Check if the common words meet the threshold
                common_words = words_set_i.intersection(words_set_j)
                if len(common_words) >= threshold:
                    uf.union(i, j)  # Union the sentences if they have enough common words

        # Group sentences by their connected components
        grouped_sentences = {}
        for i in range(n):
            root = uf.find(i)
            if root not in grouped_sentences:
                grouped_sentences[root] = []
            grouped_sentences[root].append(sentences_list[i])

        # sorting the inner sentences by their lengths
        sorted_groups = sorted(
        grouped_sentences.values(),
        key=lambda group: (len(group), [s for s in sorted(group)])  # Sort by length, then alphabetically
    )
        # sorting the sentences alphabetically
        for group in sorted_groups:
            group.sort()

        # assembling the sentences inside the dictionary
        for idx, group in enumerate(sorted_groups, 1):
            group_label = f"Group {idx}"
            result_dict["Question 9"]["group Matches"].append([group_label, group])

        return result_dict

