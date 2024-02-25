import win32api
import win32con
import win32gui
import win32ui

def overlay_window():
    # Создаем окно оверлея
    overlay = win32gui.CreateWindowEx(
        win32con.WS_EX_TOPMOST | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT,
        win32gui.WNDCLASS(),
        "Overlay Window",
        win32con.WS_POPUP,
        0, 0, win32api.GetSystemMetrics(win32con.SM_CXSCREEN),
        win32api.GetSystemMetrics(win32con.SM_CYSCREEN),
        None, None, None, None
    )

    # Устанавливаем прозрачность окна
    win32gui.SetLayeredWindowAttributes(overlay, 0, 255, win32con.LWA_ALPHA)

    # Рисуем текст на окне оверлея
    hdc = win32gui.GetWindowDC(overlay)
    dc = win32ui.CreateDCFromHandle(hdc)
    dc.SetBkMode(win32con.TRANSPARENT)
    dc.SetTextColor(win32api.RGB(255, 255, 255))
    font = win32ui.CreateFont({
        'name': 'Arial',
        'height': 24,
        'weight': 400
    })
    dc.SelectObject(font)
    dc.DrawText("Hello, Overlay!", (50, 50), win32con.DT_LEFT)
    dc.DeleteDC()
    win32gui.ReleaseDC(overlay, hdc)

    # Отображаем окно оверлея
    win32gui.ShowWindow(overlay, win32con.SW_SHOWNOACTIVATE)
    win32gui.UpdateWindow(overlay)

    # Запускаем цикл обработки сообщений окна
    while True:
        msg = win32gui.GetMessage(None, 0, 0)
        win32gui.TranslateMessage(msg)
        win32gui.DispatchMessage(msg)

if __name__ == "__main__":
    overlay_window()