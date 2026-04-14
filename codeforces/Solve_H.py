# H : Two numbers
from math import floor, ceil

a, b = map(int, input().split())
print(
    f"floor {a} / {b} = {floor(a / b)}",
    f"ceil {a} / {b} = {ceil(a / b)}",
    f"round {a} / {b} = {floor((a / b) + .5)}",
    sep = "\n"
)

# Note : بايثون بيستخدم حاجة اسمها
# 👉 Banker's Rounding
# يعني لما الرقم يبقى .5 بيقرب لأقرب عدد زوجي مش الأكبر.
# بايثون: round(2.5) → 2 ❌
# المطلوب في المسألة: → 3 ✅ (تقريب عادي)
#لازم تعمل التقريب بنفسك، مش تستخدم round() مباشرة

# 💡 الفكرة:
# بنضيف 0.5 وبعدين نعمل floor
# كده:
# 2.5 + 0.5 = 3 → floor = 3 ✅
# 2.3 + 0.5 = 2.8 → floor = 2 ✅
