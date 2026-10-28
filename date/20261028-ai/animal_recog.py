import ai_method.utils as ai

def main():
    img_path = ai.pick_file("选择要识别的动物图片")
    if not img_path:
        print("已取消。")
        return

    client = ai.get_baidu_client()
    image = ai.get_file_content(img_path)
    result = client.animalDetect(image)

    ai.print_json(result)
    
if __name__ == "__main__":
    main()