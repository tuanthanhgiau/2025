from core.prompt_brain import handle_prompt
from rich import print
import sys

def main():
    print("[bold blue]🤖 Chào mừng đến với AI Mẹ![/bold blue]")

    if len(sys.argv) < 2:
        print("[red]❌ Nhập prompt đi bạn ơi![/red]")
        return

    prompt = sys.argv[1]
    print(f"[green]📥 Prompt nhận được:[/green] {prompt}")
    result = handle_prompt(prompt)
    print(f"[bold green]✅ Kết quả xử lý:[/bold green]\n{result}")

if __name__ == "__main__":
    main()
