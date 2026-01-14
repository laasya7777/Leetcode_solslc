class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted = path.split('/')
        dir_names = [name for name in splitted if name != '']
        stack = []
        for dir_name in dir_names:
            if dir_name == '.':
                continue
            elif dir_name == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir_name)
        
        if not stack:
            return '/'
        else:
            result = ''
            for name in stack:
                result+='/'+name
            return result