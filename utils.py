import random

def generate_random_color():
    """見やすい薄い色を生成する"""
    # HSV色空間を使用して、鮮やかすぎない色を生成
    # H: 0-360 (色相), S: 0.3-0.6 (彩度), V: 0.8-1.0 (明度)
    h = random.randint(0, 360)
    s = random.uniform(0.3, 0.6)
    v = random.uniform(0.8, 1.0)
    
    # HSVをRGBに変換
    r, g, b = hsv_to_rgb(h, s, v)
    
    # RGBを16進数に変換
    return f"#{r:02x}{g:02x}{b:02x}"

def hsv_to_rgb(h, s, v):
    """HSV色空間をRGBに変換する"""
    h = h % 360
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    
    if 0 <= h < 60:
        rp, gp, bp = c, x, 0
    elif 60 <= h < 120:
        rp, gp, bp = x, c, 0
    elif 120 <= h < 180:
        rp, gp, bp = 0, c, x
    elif 180 <= h < 240:
        rp, gp, bp = 0, x, c
    elif 240 <= h < 300:
        rp, gp, bp = x, 0, c
    else:  # 300 <= h < 360
        rp, gp, bp = c, 0, x
    
    r = int((rp + m) * 255)
    g = int((gp + m) * 255)
    b = int((bp + m) * 255)
    
    return r, g, b