# Auto-Bleach: 《BLEACH Brave Souls》自动化脚本

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-✓-yellow)

## 项目简介
这是一个用于自动化操作《BLEACH: Brave Souls》游戏的脚本。它通过图像识别和模拟鼠标点击，帮助玩家自动完成一些重复性任务，例如购买、战斗、领取奖励等。

## 功能特点
- **自动识别并点击游戏中的按钮和图像**
- **支持多线程运行，提高操作效率**
- **可配置的玉（Orbs）使用数量，避免过度消耗资源**
- **可通过按键（F5 开始，F6 停止）控制脚本运行**
- 自动购买任务次数
- 自动开始任务
- 自动领取奖励
- 自动处理任务完成后的弹窗

## 系统要求
- **Python**：3.6 或更高版本
- **依赖库**：`opencv-python`、`numpy`、`pyautogui`、`pygetwindow`、`keyboard`
- **操作系统**：Windows（其他系统可能需要额外配置）

## 安装方法
1. **安装 Python**：确保你已安装 Python 3.6 或更高版本，并将其添加到系统环境变量中。
2. **克隆项目**：
   ```bash
   git clone https://github.com/xianpy-py/Auto-BBS.git
   cd Auto-BBS
   ```
3. **安装依赖库**：
   ```bash
   pip install opencv-python numpy pyautogui pygetwindow keyboard
   ```

## 使用说明
1. 将游戏窗口标题设置为 "BLEACH: Brave Souls"
2. 确保游戏窗口位于前台
3. 准备模板图片（路径参考 `main()` 中的 `click_list`）
4. 运行脚本：
   ```bash
   python auto_bleach.py
   ```
5. 输入要消耗的玉数量（整数）
6. 按 F5 开始执行
7. 按 F6 随时停止

## 模板图片配置
脚本使用以下模板图片进行图像识别：

| 图片名称         | 功能描述               | 文件路径               |
|------------------|----------------------|-----------------------|
| `go_10.png`      | 开始10次任务按钮      | `.\png\go_10.png`     |
| `go.png`         | 开始任务按钮          | `.\png\go.png`        |
| `create_room_2.png` | 创建房间按钮         | `.\png\create_room_2.png`|
| `close.png`      | 关闭按钮              | `.\png\close.png`     |
| `TAP SCREEN.png` | 点击屏幕提示          | `.\png\TAP SCREEN.png`|
| `award.png`      | 奖励图标              | `.\png\award.png`     |
| `buy_50.png`     | 购买50次按钮          | `.\png\buy_50.png`    |
| `purchase.png`   | 购买确认按钮          | `.\png\purchase.png`  |
| `continue.png`   | 继续按钮              | `.\png\continue.png`  |
| `labour_award.png`| 劳动奖励图标          | `.\png\labour_award.png`|
| `buy.png`        | 购买按钮              | `.\png\buy.png`       |
| `retry.png`      | 重试按钮              | `.\png\retry.png`     |
| `quest clear.png`| 任务完成提示          | `.\png\quest clear.png`|
| `OK.png`         | 确认按钮              | `.\png\OK.png`        |
| `star.png`       | 星级评价图标          | `.\png\star.png`      |
| `add.png`        | 添加按钮              | `.\png\add.png`       |
| `claim.png`      | 领取按钮              | `.\png\claim.png`     |
| `plus.png`       | 增加按钮              | `.\png\plus.png`      |
| `done.png`       | 完成按钮              | `.\png\done.png`      |

## 自定义配置
在代码中可调整以下参数：
```python
confidence = 0.9  # 图像匹配置信度阈值（0-1）
pyautogui.PAUSE = 0.5  # 操作间隔时间（秒）
```

