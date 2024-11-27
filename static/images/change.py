from PIL import Image

# 加载图片
image_path = "chatgpt.png"  # 替换为你的图片路径
image = Image.open(image_path).convert("RGBA")

# 指定要替换的颜色和新颜色
target_color = (0, 168, 132)  # 替换为图片中绿色的 RGB 值
new_color = (159, 137, 194, 255)  # 替换为紫色 RGB 值并设置不透明度

# 创建空白图片用于存储替换后的结果
pixels = image.load()
for y in range(image.size[1]):
    for x in range(image.size[0]):
        # 获取当前像素的颜色
        current_color = pixels[x, y]
        # 如果颜色接近绿色，则替换为紫色
        if abs(current_color[0] - target_color[0]) < 30 and \
           abs(current_color[1] - target_color[1]) < 30 and \
           abs(current_color[2] - target_color[2]) < 30:
            pixels[x, y] = new_color

# 保存更改后的图片
image.save("chatgpt_with_purple_bg.png", format="PNG")