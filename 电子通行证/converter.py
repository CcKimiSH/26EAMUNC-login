import json
import hashlib

def convert_data(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        crypto_list = []

        for entry in data:
            # 获取原始 QQ 号并转换为字符串进行哈希处理
            raw_qq = str(entry.get('qq_id', ''))
            # 使用 SHA-256 进行哈希运算，生成不可逆的摘要
            qq_hash = hashlib.sha256(raw_qq.encode('utf-8')).hexdigest()

            # 构建脱敏后的数据对象
            new_entry = {
                "name": entry.get('name'),
                "qq_hash": qq_hash,  # 存储哈希值，不再存真实 ID
                "venue": entry.get('venue'),
                "school": entry.get('school'),
                "seat": entry.get('seat'),
            }
            crypto_list.append(new_entry)

        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(crypto_list, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 转换成功！已生成脱敏文件: {output_filename}")
        print("⚠️ 请注意：请务必只将 crypto_data.json 上传到 GitHub，严禁上传 fact_data.json")

    except FileNotFoundError:
        print("❌ 错误：未找到 fact_data.json，请检查文件是否存在。")
    except Exception as e:
        print(f"❌ 发生错误: {e}")

# 执行转换
if __name__ == "__main__":
    convert_data('fact_data.json', 'crypto_data.json')
