# Answer-Assistant
手机移动端答题辅助工具。(理想之光app卡尔马克思杯，网课课后题等......)

## 平台
- Mac OS X + IOS

## 安装依赖
1. 参考下面的配置安装 **WebDriverAgent**

- 使用真机调试 WDA，参考 iOS 真机如何安装 [WebDriverAgent · TesterHome](https://testerhome.com/topics/7220)
- 安装 [openatx/facebook-wda](https://github.com/openatx/facebook-wda)

2. 安装所需 python 包

   命令行：

   `pip install -r requirements.txt`


## 使用步骤 (百度 OCR)

1. 在[百度平台](https://cloud.baidu.com/product/ocr)上创建应用申请 API Key 和 Secret Key

2. 在 `config.conf` 中加入相应 key, 并设置截取区域

      ```
      [region]
      # 题目和选项一起的区域
      combine_region = 50, 350, 1000, 1200
      [baidu_api]
      APP_ID = 
      API_KEY = 
      SECRET_KEY = 
      ```

3. 运行脚本 

   `python answer.py`

## 参考自
 
- [wechat_jump_game](https://github.com/wangshub/wechat_jump_game)
- [TopSup](https://github.com/Skyexu/TopSup)