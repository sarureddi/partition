def checkEven(v):
if v%2==0:
  return "YES";
else:
  return "NO";
if __name__ == "__main__":
  v,a,s=map(int, raw_input().split())
if checkEven(v) == "NO":
       print("NO")
 else:
      par=v/2
       left=par%a
 if (left==0 or left%s==0):
      print("YES")
  else:
     print("NO")
