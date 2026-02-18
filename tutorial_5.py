from mcp.server.fastmcp import FastMCP, Context

mcp=FastMCP("tutorial_5")

@mcp.tool()
async def greeting(name: str, ctx: Context) -> str: #greeting이라는 비동기 함수를 정의합니다
    """Get a greeting using the greeting resource"""
    try:
        result = await ctx.read_resource(f"greeting://{name}") #ctx.read_resource()를 사용해서 리소스를 읽어옵니다. greeting://{name} 형식의 URI로 리소스에 접근합니다 
        #await를 사용해서 비동기적으로 결과를 기다림
        content =result[0] if isinstance(result, tuple) else result
        #result가 튜플인지 확인합니다
        #튜플이면 첫 번째 요소(result[0])를 가져오고, 아니면 result 자체를 사용합니다
        #리소스 읽기 결과가 여러 형태로 올 수 있어서 안전하게 처리합니다
        return f"Tool response:{content}" #"Tool response:"라는 접두사와 함께 content를 문자열로 반환합니다
    except Exception as e:
        return f"Error retrieving greeting: {str(e)}"
    
@mcp.resource("greeting://{name}") #URI 패턴: greeting://{name} - name 부분이 동적으로 바뀝니다
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!! Welcome to FastMCP"

if __name__ == "__main__":
    mcp.run()

#Tool(도구): AI가 호출할 수 있는 함수
#Resource(리소스): URI 기반으로 데이터를 제공하는 함수

#greeting 도구가 호출되면
#ctx.read_resource()로 greeting://{name} 리소스를 요청
#해당 URI 패턴에 매칭되는 get_greeting 함수가 실행됨