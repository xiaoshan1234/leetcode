# 浅拷贝问题（P9）
```python
flg1 = [[False]*5]*5 # 浅拷贝
flg1[1][1] = True
flg2 = [[False for i in range(5)] for i in range(5)] # 深拷贝
flg2[1][1] = True

print(flg1)
print(flg2)
```
