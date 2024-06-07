from zhipuai import ZhipuAI
import os

import ApiKeyConfig

client = ZhipuAI(api_key=ApiKeyConfig.zhipu_api_key_prod)  # 请填写您自己的APIKey


# 1.上传Batch文件
batchFile = client.files.create(
    file=open("../exampleFile/glm3turboBatchAPITest.jsonl", "rb"), ## 填自己准本的batch请求文件
    purpose="batch"  # batch请求需要写死batch
)
print("batch文件id: " + batchFile.id)


# 2.创建Batch
createBatch = client.batches.create(
    input_file_id=batchFile.id,
    endpoint="/v4/chat/completions",
    completion_window="24h",  # 完成时间只支持 24 小时
    metadata={
        "description": "测试hy"
    }
)
print("创建Batch成功：" + createBatch.__str__())

#3.实时查询Batch处理结果
retrieve = client.batches.retrieve(createBatch.id)
print("Batch处理结果: " + retrieve.__str__())

#==============================得等待一段时间=====================
# 4.下载batch
# content = client.files.content(retrieve.output_file_id)
# # 使用write_to_file方法把返回结果写入文件
# content.write_to_file("write_to_file_batchoutput.jsonl")






