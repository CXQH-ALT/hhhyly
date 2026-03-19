from docx import Document

# 打开文档
doc = Document('产品服务.docx')

# 提取文本内容
content = []
for para in doc.paragraphs:
    if para.text.strip():
        content.append(para.text)

# 提取标题和正文结构
title = content[0] if content else "无标题"
sections = []
current_section = {"title": "", "content": []}

for line in content[1:]:
    # 简单判断标题（假设标题是加粗或有特定格式，这里简化处理）
    if line.isupper() or line.endswith('：') or line.endswith(':'):
        if current_section["title"]:
            sections.append(current_section)
        current_section = {"title": line, "content": []}
    else:
        current_section["content"].append(line)

if current_section["title"] or current_section["content"]:
    sections.append(current_section)

# 输出结果
print("标题:", title)
print("\n sections:")
for i, section in enumerate(sections):
    print(f"\nSection {i+1}: {section['title']}")
    print("Content:", "\n".join(section['content']))
