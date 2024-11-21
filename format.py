import json
import os
from pathlib import Path

def ensure_crlf_line_endings(directory):
    # 确保目录存在
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist!")
        return

    # 获取所有json文件
    json_files = list(Path(directory).glob('*.json'))
    
    print(f"Found {len(json_files)} JSON files")
    
    for json_file in json_files:
        try:
            # 读取JSON文件
            with open(json_file, 'r', encoding='utf-8', newline=None) as f:
                content = f.read()
            
            # 解析JSON以确保它是有效的
            json_content = json.loads(content)
            
            # 重新格式化JSON，确保使用CRLF
            formatted_content = json.dumps(json_content, indent=4, ensure_ascii=False)
            
            # 显式转换所有换行符为CRLF
            formatted_content = formatted_content.replace('\n', '\r\n')
            
            # 写入文件时强制使用CRLF
            with open(json_file, 'w', encoding='utf-8', newline='\r\n') as f:
                f.write(formatted_content)
                # 确保文件以CRLF结尾
                if not formatted_content.endswith('\r\n'):
                    f.write('\r\n')
            
            print(f"Successfully processed {json_file}")
            
            # 验证文件
            verify_line_endings(json_file)
            
        except Exception as e:
            print(f"Error processing {json_file}: {str(e)}")

def verify_line_endings(file_path):
    """验证文件是否使用CRLF换行符"""
    with open(file_path, 'rb') as f:
        content = f.read()
        if b'\r\n' not in content:
            print(f"WARNING: {file_path} does not have CRLF line endings!")
            return False
        
        # 确保所有换行都是CRLF
        lf_count = content.count(b'\n')
        crlf_count = content.count(b'\r\n')
        if lf_count != crlf_count:
            print(f"WARNING: {file_path} has mixed line endings!")
            return False
            
    return True

if __name__ == "__main__":
    # 指定bucket目录的路径
    bucket_dir = "./bucket"  # 根据实际情况修改路径
    
    print("Starting JSON file processing...")
    ensure_crlf_line_endings(bucket_dir)
    print("\nVerification complete!")
