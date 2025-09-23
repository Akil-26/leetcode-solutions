class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    p1, p2 = 0, 0
    n1, n2 = len(version1), len(version2)
    while p1 < n1 or p2 < n2:
      rev1 = 0
      while p1 < n1 and version1[p1] != '.':
        rev1 = rev1 * 10 + int(version1[p1])
        p1 += 1
      p1 += 1
      rev2 = 0
      while p2 < n2 and version2[p2] != '.':
        rev2 = rev2 * 10 + int(version2[p2])
        p2 += 1
      p2 += 1  
      if rev1 > rev2:
        return 1
      if rev1 < rev2:
        return -1
    return 0
