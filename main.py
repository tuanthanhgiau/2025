# main.py

from core.prompt_brain import handle_prompt
from rich import print
import sys

def main():
    print("[bold blue]🤖 Chào mừng đến với AI Mẹ - Hệ sinh AI/App tự động[/bold blue]")
    
    # Nhận prompt từ dòng lệnh
    if len(sys.argv) < 2:
        print("[red]❗ Hãy nhập prompt mô tả app hoặc AI cần tạo.[/red]")
        print("Ví dụ: python main.py 'Tạo app quản lý công việc bằng Flutter, có đăng nhập Google'")
        return
    
    prompt = sys.argv[1]
    print(f"[green]📥 Prompt nhận được:[/green] {prompt}")

    # Xử lý prompt bằng AI Mẹ
    result = handle_prompt(prompt)

    print("\n[bold green]✅ Kết quả xử lý:[/bold green]")
    print(result)

if __name__ == "__main__":
    main()
