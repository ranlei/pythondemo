
class Palindrome(object):
    """docstring for Palindrome"""
    def __init__(self, arg):
        pass
    @classmethod
    def is_palindrome1(cls,s):
        if not isinstance(s,str):
            raise ValueError("please input string!")
        front,back = 0,len(s)-1
        while front<back:
            if s[front] != s[back]:
                return False
            front += 1
            back -= 1
        return True
    @classmethod
    def is_palindrome2(cli,s):
        if not isinstance(s,str):
            raise ValueError("please input string.")
        if len(s)%2 == 0:
            front,back = int(len(s)/2-1),int(len(s)/2)
        else:
            front,back = int(len(s)/2),int(len(s)/2)
        while back<len(s)-1:
            if s[front] != s[back]:
                return False
            front -= 1
            back += 1
        return True

if __name__ == "__main__":
    s = raw_input("please input string:")
    print "this is palindrome1:%s\n" % Palindrome.is_palindrome1(s)
    print "this is palindrome2:%s\n" % Palindrome.is_palindrome2(s)


        
