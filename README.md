# 优可打标校验工具 / Youkengi Label Verification Tool

TXT 文件管理工具，用于示词的人工检验与调整。

A TXT file management tool for manual inspection and adjustment of prompts.

## 功能特性 / Features

- 📤 **批量加载 TXT 文件 / Batch Load TXT Files** - 支持多选文件批量导入 / Support batch import of multiple files
- 📝 **文本预览与编辑 / Text Preview & Edit** - 内置文本编辑器，支持修改和保存 / Built-in text editor with save support
- 📷 **图片预览 / Image Preview** - 自动加载同名图片（支持 .jpg 和 .png 格式）/ Auto-load images with same name (supports .jpg and .png)
- 📂 **文件列表管理 / File List Management** - 支持多种排序方式（创建时间、文件名）/ Multiple sorting options (creation time, file name)
- 💾 **保存修改 / Save Changes** - 一键保存文本修改 / One-click save
- 🗑️ **删除文件 / Delete File** - 从列表中移除文件 / Remove files from list
- 🧹 **清空功能 / Clear Function** - 支持清空预览区和文件列表 / Clear preview and file list
- 🌐 **中英双语 / Bilingual** - 支持中文和英文界面切换 / Support Chinese and English interface switching

## 安装依赖 / Installation

```bash
pip install -r requirements.txt
```

## 运行方式 / Usage

```bash
python txt_manager_app.py
```

程序启动后会自动在浏览器中打开界面（默认端口 8080，如被占用会自动切换）。

The application will automatically open in your browser (default port 8080, will auto-switch if occupied).

## 使用说明 / Instructions

### 中文

1. 点击"批量加载 TXT 文件"按钮选择需要管理的 TXT 文件
2. 在右侧文件列表中点击文件名进行预览和编辑
3. 左侧预览区会显示：
   - 同名图片（如果存在）
   - 文本内容（可编辑）
4. 编辑完成后点击"保存修改"按钮保存更改
5. 可使用排序功能按创建时间或文件名排序文件列表
6. 点击右上角语言切换按钮可在中文和英文之间切换

### English

1. Click "Batch Load TXT Files" to select TXT files to manage
2. Click on a file name in the right panel to preview and edit
3. The left preview area displays:
   - Image with same name (if exists)
   - Text content (editable)
4. Click "Save Changes" to save modifications
5. Use sorting options to sort files by creation time or name
6. Click the language switch button in the top right to switch between Chinese and English

## 界面布局 / Layout

- **左侧 / Left**: 预览区（图片预览 + 文本编辑）/ Preview Area (Image + Text Editor)
- **右侧 / Right**: 加载区 + 文件列表 / Load Area + File List
- **右上角 / Top Right**: 语言切换下拉框 / Language Switch Dropdown

## 技术栈 / Tech Stack

- Python 3.x
- NiceGUI - 现代化的 Python UI 框架 / Modern Python UI framework
- Tailwind CSS - 用于界面样式 / For UI styling

## 语言切换 / Language Switching

点击页面右上角的下拉框（🌐 Language）即可在中文和英文之间切换界面语言。

Click the dropdown (🌐 Language) in the top right corner to switch between Chinese and English.
