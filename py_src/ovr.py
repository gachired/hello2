import win32gui
import win32api
import win32con
import win32ui

class OverlayWindow:
    def __init__(self):
        # Создание окна
        self.window_class = win32gui.WNDCLASS()
        self.hinstance = self.window_class.hInstance = win32api.GetModuleHandle(None)
        self.window_class.lpszClassName = "OverlayWindowClass"
        self.window_class.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        self.window_class.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        self.window_class.hbrBackground = win32gui.GetStockObject(win32con.WHITE_BRUSH)
        self.window_class.lpfnWndProc = self.window_proc
        win32gui.RegisterClass(self.window_class)
        self.hwnd = win32gui.CreateWindow(self.window_class.lpszClassName,
                                          "Overlay Window",
                                          win32con.WS_POPUP | win32con.WS_VISIBLE,
                                          0, 0, 800, 600,
                                          None, None, self.hinstance, None)
        # Устанавливаем прозрачность окна
        # win32gui.SetLayeredWindowAttributes(self.hwnd, 0, 255, win32con.LWA_ALPHA)



        # Установка окна поверх всех остальных окон
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    def window_proc(self, hwnd, msg, wparam, lparam):
        # Обработчик событий окна
        if msg == win32con.WM_PAINT:
            # hdc, paint_struct = win32gui.BeginPaint(hwnd)
            # win32gui.FillRect(hdc, paint_struct.rcPaint, win32gui.GetStockObject(win32con.BLACK_BRUSH))
            # win32gui.EndPaint(hwnd, paint_struct)
            # Рисуем текст на окне оверлея
            hdc = win32gui.GetWindowDC(self.hwnd)
            dc = win32ui.CreateDCFromHandle(hdc)
            dc.SetBkMode(win32con.TRANSPARENT)
            dc.SetTextColor(win32api.RGB(255, 255, 255))
            font = win32ui.CreateFont({
                'name': 'Arial',
                'height': 24,
                'weight': 400
            })
            dc.SelectObject(font)
            dc.DrawText("Hello, Overlay!", (50, 50, 20, 20), win32con.DT_LEFT)
            dc.DeleteDC()
            win32gui.ReleaseDC(self.hwnd, hdc)
            win32gui.ShowWindow(self.hwnd, win32con.SW_SHOWNOACTIVATE)
            win32gui.UpdateWindow(self.hwnd)
            return 0
        else:
            return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

    def run(self):
        # Запуск обработки событий окна
        win32gui.PumpMessages()

if __name__ == "__main__":
    overlay = OverlayWindow()
    overlay.run()