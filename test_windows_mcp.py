#!/usr/bin/env python3
"""
Windows-MCP 功能测试脚本
用于验证Windows-MCP的安装和基本功能
"""

import sys
print("=== Windows-MCP 功能测试 ===\n")

# 测试基础导入
print("1. 测试基础模块导入...")
try:
    import windows_mcp
    print("   ✅ windows_mcp 导入成功")
    
    # 尝试导入主要组件
    try:
        from windows_mcp.__main__ import main
        print("   ✅ MCP主函数导入成功")
    except Exception as e:
        print(f"   ⚠️ MCP主函数导入警告: {e}")
        
except Exception as e:
    print(f"   ❌ windows_mcp 导入失败: {e}")
    sys.exit(1)

# 测试关键依赖
print("\n2. 测试关键依赖...")
dependencies = [
    ('pyautogui', 'UI自动化'),
    ('pywinauto', 'Windows应用控制'),
    ('psutil', '系统信息'),
    ('pillow', '图像处理'),
    ('click', '命令行界面'),
    ('fastmcp', 'MCP协议框架'),
    ('python-dotenv', '环境变量'),
    ('requests', 'HTTP请求')
]

all_deps_ok = True
for dep, desc in dependencies:
    try:
        __import__(dep)
        print(f"   ✅ {dep} ({desc}): 导入成功")
    except Exception as e:
        print(f"   ❌ {dep} ({desc}): 导入失败 - {e}")
        all_deps_ok = False

# 测试系统功能
print("\n3. 测试系统功能...")
try:
    import pyautogui
    screen_size = pyautogui.size()
    print(f"   ✅ 屏幕分辨率: {screen_size}")
except Exception as e:
    print(f"   ❌ 屏幕分辨率获取失败: {e}")

try:
    import psutil
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    print(f"   ✅ 系统资源: CPU {cpu_percent}%, 内存 {memory.percent}%")
except Exception as e:
    print(f"   ❌ 系统资源获取失败: {e}")

# 检查缺失的依赖
print("\n4. 检查缺失依赖...")
missing_deps = [
    'fuzzywuzzy', 'humancursor', 'ipykernel', 'live-inspect', 
    'markdownify', 'pdfplumber', 'posthog', 'python-levenshtein', 
    'tabulate', 'uiautomation', 'uuid7'
]

for dep in missing_deps:
    try:
        __import__(dep)
    except ImportError:
        print(f"   ⚠️ {dep}: 缺失（可能影响部分功能）")

print("\n=== 测试结果汇总 ===")
if all_deps_ok:
    print("✅ 核心功能测试通过！")
    print("📝 缺失的依赖包可能会影响部分高级功能")
    print("💡 建议：")
    print("   - 核心UI自动化功能可用")
    print("   - 可配置到Claude Desktop等MCP客户端")
    print("   - 如需完整功能，可尝试安装缺失依赖")
else:
    print("⚠️ 部分核心依赖存在问题")
    print("💡 建议检查Python环境和依赖安装")

print("\n=== 配置信息 ===")
print("Claude Desktop配置已创建: claude_desktop_config.json")
print("配置路径: %USERPROFILE%\\AppData\\Roaming\\Claude\\claude_desktop_config.json")
print("\n使用方法:")
print("1. 将配置文件复制到Claude Desktop配置目录")
print("2. 重启Claude Desktop")
print("3. Windows-MCP将自动集成到Claude中")