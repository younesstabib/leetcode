class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occ_arr = []
        arr_without_occ = []
        for ar in arr: 
            if ar not in arr_without_occ:
                arr_without_occ.append(ar)

        for a in arr_without_occ:
            if arr.count(a) in occ_arr:
                return False
            occ_arr.append(arr.count(a))
        
        return True