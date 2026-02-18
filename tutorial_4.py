from mcp.server.fastmcp import FastMCP, Image
from PIL import Image as PILImage
import os

mcp = FastMCP("tutorial_4")

@mcp.tool()
def create_thumbnail() -> Image:
    """Create a thumbnail from an image"""
    try:
        import io #메모리상에서 바이트 데이터를 다루기 위해 io 모듈을 가져옵니다
        img_path = os.path.join("C:\\test", "image.png") #C:\test 폴더와 image.png 파일명을 합쳐서 전체 경로를 만듭니다
        img = PILImage.open(img_path)
        img.thumbnail((100, 100))
        
        buffer = io.BytesIO() #메모리상에 바이트 버퍼를 생성합니다 (파일처럼 사용할 수 있는 메모리 공간)
        img.save(buffer, format="PNG") #썸네일 이미지를 PNG 형식으로 버퍼에 저장합니다
        return Image(data=buffer.getvalue(), format="png") #버퍼의 바이트 데이터를 가져와서 Image 객체로 만들어 반환합니다
    except Exception as e:
        return f"Error creating thumbnail: {str(e)}"

if __name__ == "__main__":
    mcp.run()
    