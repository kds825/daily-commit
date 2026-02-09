from mcp.server.fastmcp import FastMCP

mcp = FastMCP("tutorial_2")


@mcp.tool()
def add(a: int, b: int) -> int:
    """두 숫자를 더하는 함수"""
    return a + b

@mcp.resource("greeting://hello")
def get_greeting() -> str:
    """인사말을 제공하는 함수"""
    return f"Hello, World!"

if __name__ == "__main__":
    mcp.run()
    