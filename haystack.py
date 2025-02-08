def strStr(haystack, needle):
    if not needle:
        return 0
    haystack_length = len(haystack)
    needle_length = len(needle)
    for i in range(haystack_length - needle_length + 1):
        if haystack[i:i + needle_length] == needle:
            return i
    return -1
haystack = "sadbutsad"
needle = "sad"
result = strStr(haystack, needle)
print(result)  
