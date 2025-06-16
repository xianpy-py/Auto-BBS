import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
import keyboard
import time
import logging
import gc
import concurrent.futures

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

last_screenshot = None
running = True
confidence = 0.9
pyautogui.PAUSE = 0.5


def capture_window(window_title):
    global last_screenshot, running
    while running :
        screenshot = pyautogui.screenshot()
        last_screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
        time.sleep(0.2)




def load_templates(image_values):
    templates = []
    for item in image_values:
        name = item['name']
        path = item['path']
        template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            logging.error(f"无法加载图像：{path}，请检查路径和文件是否正确")
            raise FileNotFoundError(f"无法加载图像：{path}")
        templates.append({"name": name, "value": template})
        logging.info(f"成功加载了{name}图像")

    # 清理变量
    del image_values
    gc.collect()
    return templates



def find_image(template_value):
    global last_screenshot
    if last_screenshot is None:
        logging.warning("截图为空，无法进行图像匹配")
        return None
    result = cv2.matchTemplate(last_screenshot, template_value, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    if max_val >= confidence:
        template_height, template_width = template_value.shape[:2]
        image_info = {
            "location": max_loc,
            "width": template_width,
            "height": template_height
        }
        return image_info
    else:
        return None



def click_image(image_info):
    location = image_info["location"]
    width = image_info["width"]
    height = image_info["height"]
    center_x = location[0] + width // 2
    center_y = location[1] + height // 2
    pyautogui.click(center_x, center_y)


def stop():
    global running
    while running:
        if keyboard.is_pressed('f6'):
            print(f"检测到 F6 键按下，停止")
            running = False
            break


def single_quest(max_orbs, templates):
    global running, last_screenshot
    orbs_used = 0
    value_dict = {item["name"]: item["value"] for item in templates}
    image_info_cache = {name: None for name in value_dict.keys()}  # 缓存找到的图像信息

    def find_image_cached(template_name):
        """从缓存中获取图像信息，如果没有则重新查找"""
        if image_info_cache[template_name] is None:
            image_info_cache[template_name] = find_image(value_dict[template_name])
        return image_info_cache[template_name]

    while running and orbs_used < max_orbs:
        if orbs_used >= max_orbs:
            running = False
            break

        for name in image_info_cache.keys():
            image_info_cache[name] = None

        purchase_quest = find_image_cached("purchase")
        if purchase_quest is not None:
            click_image(purchase_quest)
            while running :
                buy_50 = find_image_cached("buy_50")
                if buy_50 is not None:
                    click_image(buy_50)
                    time.sleep(2)
                    break
            pyautogui.moveRel(900, 0)
            pyautogui.click()
            orbs_used += 10
            continue

        tap_quest = find_image_cached("tap_screen")
        if tap_quest is not None:
            click_image(tap_quest)
            continue

        done_quest = find_image_cached("done")
        if done_quest is not None:
            click_image(done_quest)
            continue

        close_quest = find_image_cached("close")
        if close_quest is not None:
            click_image(close_quest)
            continue

        continue_quest = find_image_cached("continue")
        if continue_quest is not None:
            click_image(continue_quest)
            continue

        award_quest = find_image_cached("award")
        if award_quest is not None:
            click_image(award_quest)
            continue
            
        retry_quest = find_image_cached("retry")
        if retry_quest is not None:
            click_image(retry_quest)
            continue


        quest_clear_quest = find_image_cached("quest_clear")
        if quest_clear_quest is not None:
            click_image(quest_clear_quest)
            continue

        ok_quest = find_image_cached("ok")
        if ok_quest is not None:
            click_image(ok_quest)
            continue

        start_quest = find_image_cached("go")
        if start_quest is not None:
            click_image(start_quest)
            continue


    logging.info(f"已经使用{orbs_used}玉，结束")
    del value_dict
    del image_info_cache
    gc.collect()


def add_idle(max_orbs, templates):
    global running, last_screenshot
    orbs_used = 0
    value_dict = {item["name"]: item["value"] for item in templates}
    image_info_cache = {name: None for name in value_dict.keys()}  # 缓存找到的图像信息

    def find_image_cached(template_name):
        """从缓存中获取图像信息，如果没有则重新查找"""
        if image_info_cache[template_name] is None:
            image_info_cache[template_name] = find_image(value_dict[template_name])
        return image_info_cache[template_name]

    while running and orbs_used < max_orbs:
        for name in image_info_cache.keys():
            image_info_cache[name] = None

    del value_dict
    del image_info_cache
    gc.collect()

def main():
    """
    主函数
    """
    window_title = "BLEACH: Brave Souls"

    click_list = [
        {"name": "go_10", "path": r'.\png\go_10.png'},
        {"name": "go", "path": r".\png\go.png"},
        {"name": "creat_room", "path": r".\png\create_room_2.png"},
        {"name": "close", "path": r".\png\close.png"},
        {"name": "tap_screen", "path": r'.\png\TAP SCREEN.png'},
        {"name": "award", "path": r".\png\award.png"},
        {"name": "buy_50", "path": r".\png\buy_50.png"},
        {"name": "purchase", "path": r".\png\purchase.png"},
        {"name": "continue", "path": r'.\png\continue.png'},
        {"name": "labour_award", "path": r".\png\labour_award.png"},
        {"name": "buy", "path": r".\png\buy.png"},
        {"name": "retry", "path": r".\png\retry.png"},
        {"name": "quest_clear", "path": r".\png\quest clear.png"},
        {"name": "ok", "path": r".\png\OK.png"},
        {"name": "star", "path": r".\png\star.png"},
        {"name": "add", "path": r".\png\add.png"},
        {"name": "claim", "path": r".\png\claim.png"},
        {"name": "plus", "path": r".\png\claim.png"},
        {"name": "done", "path": r".\png\done.png"}
    ]

    logging.info("加载模板...")
    templates = load_templates(click_list)
    logging.info("一共要用多少玉?")
    orbs = int(input())
    logging.info("按下 F5 开始运行，按下 F6 结束运行")
    keyboard.wait('f5')
    logging.info("开始运行")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(capture_window, window_title)
        executor.submit(single_quest, orbs, templates)
        # executor.submit(add_idle, orbs, templates)
        # executor.submit(claim_award,templates)
        # executor.submit(co_op, templates)
        executor.submit(stop)

    logging.info("主线程退出")
    del templates
    del click_list
    gc.collect()
    logging.info("清理完成")


if __name__ == "__main__":
    main()
    logging.info("脚本结束")

