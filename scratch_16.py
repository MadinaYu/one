import random
import time
def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)
start_time = time.time()
nums = [random.randint(1, 1000) for _ in range(1000)]
sorted_nums = quicksort(nums)
end_time = time.time()
v_time = end_time - start_time
print("Время:", v_time, "сек.")
