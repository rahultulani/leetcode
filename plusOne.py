class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def list_to_int(arr):
            out = 0
            i = len(arr)
            for i in range(len(arr)):
                out = out + arr[i] * (10 ** (len(arr)-i-1))
            return out
        val = ""
        for i in list(map(str, digits)):
            val += i
        print(int(val))
        output_arr = list((str(int(val) + 1)))
        return list(map(int, output_arr))
