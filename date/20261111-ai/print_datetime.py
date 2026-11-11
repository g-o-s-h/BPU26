import datetime as dt
now = dt.datetime.now()
print("当前时间：", now)
print()
print("日期：", now.date())
print("时间：", now.time())
print()
print("日期：", now.strftime("%Y-%m-%d"))
print("时间：", now.strftime("%H:%M:%S"))
print()
print("日期：", now.strftime("%x"))
print("时间：", now.strftime("%X"))

# ------------------------------------------------------------
# 当前时间： 2026-11-11 08:53:20.185187

# 日期： 2026-11-11
# 时间： 08:53:20.185187

# 日期： 2026-11-11
# 时间： 08:53:20

# 日期： 11/11/26
# 时间： 08:53:20

# ------------------------------------------------------------