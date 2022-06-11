import libchecker

libchecker.check_if_libraries_exist([("httpx", "httpx"), ("colorlib", "tui-colorlib")], True)

print("installed everything")
