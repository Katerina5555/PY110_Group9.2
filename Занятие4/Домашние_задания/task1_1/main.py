# ����� ����f��� ������ IP4

import re

ip4 = re.compile(r"""
    (?:(?:25[0-5]| # 250-255
          2[0-4][0-9]|  # 200-249
          [01]?[0-9]?[0-9])\.){3}
          (?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])
""", re.VERBOSE)


if __name__ == "__main__":
    # Write your solution here
    pass
