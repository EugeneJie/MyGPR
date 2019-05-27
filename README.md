# MyGPR
## 用机器学习方法对GPR模拟数据进行异常定位和分类
*由于GitHub的限制，本项目只上传了大部分的实现代码（不包含gprMax3和YOLO模型的源码、数据集、训练模型以及MyGPR软件集成部分），完整的项目下载地址：https://pan.baidu.com/s/1GonJ49mzBCsCaM2c0gmEeQ 提取码：ebmw*
### 配置说明
在计算机配置较低时建议使用Google Colab来进行本文所涉及的数据模拟以及模型训练等工作，该网站（https://colab.research.google.com ）需要使用Google的Gmail邮箱账号进行登录，并与谷歌云盘进行绑定以存储训练数据以及训练模型等资源。它实际上是一个免费的云端Jupyter Notebook运行环境，支持Python编程语言，并且已经对Python中常用的模块特别是机器学习相关模块进行了配置，因此我们可以在该环境下快速建立自己的机器学习项目。详细的配置项如下：<br>
* 正演程序：gprMax3（从https://github.com/gprmax/gprMax 下载程序源码，修改tools.plot_Bscan源码(或直接使用本项目提供的已修改过的源码)，并上传到谷歌云盘）
* 运行环境：Google Colab（需通过pip额外安装gprMax3所依赖的colorama,terminaltables,pycuda模块）
* 浏览器插件：谷歌访问助手（用于访问Google相关的网站）
* 编程语言：Python3
---
在计算机配置较高时可以使用本地运行环境来进行训练，详细的配置项如下：
* 正演程序：gprMax3（从https://github.com/gprmax/gprMax 下载程序源码，修改tools.plot_Bscan源码(或直接使用本项目提供的已修改过的源码)）
* 运行环境：Jupyter Notebook（下载地址：https://jupyter.org ）
* 编程语言：Python3（下载地址：https://www.python.org ）
* 主要的Python模块：keras, tensorflow, matplotlib等以及gprMax3所依赖的一些模块（在程序运行过程中可以通过错误提示来安装缺少的模块，安装方式：在命令行窗口输入“pip install 模块名”）
---
本文所涉及代码均根据云端运行环境编写，项目中已包含修改过的gprMax3和YOLO模型源码，以及用于训练的探地雷达B-scan图像和标签文件，并将训练好的模型集成在MyGPR软件中。若在本地环境中运行程序，需要将涉及到谷歌云端硬盘的相关代码删除（主要是第一个单元格中绑定云端硬盘的相关代码），并根据本地目录对代码中的涉及的文件路径进行相应的修改。<br>
此外，本文所使用的标注工具为labelImg（下载地址：https://github.com/tzutalin/labelImg ），在云端运行环境中，需要将云端生成的定位模型训练图片下载到本地，用labelImg进行标注，然后运行标签格式转换程序，得到符合YOLO模型要求的标签文件“train.txt”，将其上传到谷歌云盘。
最后，对模型训练过程中主要涉及的文件目录结构进行说明：
> gpr_data（用以训练分类模型的数据）<br>
>> train（训练集，将同种异常体图像放在相同文件夹，并以异常体名称命名）<br>
>>> pec<br>
>>> free_space<br>
>>> soil<br>
>>> coal<br>

>> val（验证集，将同种异常体图像放在相同文件夹，并以异常体名称命名）<br>
>>> pec<br>
>>> free_space<br>
>>> soil<br>
>>> coal<br>

>> predict（测试集，将所有测试图像放在该文件夹下以测试模型的表现）<br>

> gpr_locate（用以训练定位模型的数据）<br>
>> train（训练集，将同种异常体图像放在相同文件夹，并以异常体名称命名）<br>
>>> pec<br>
>>> free_space<br>
>>> soil<br>
>>> coal<br>

>> val（验证集，将同种异常体图像放在相同文件夹，并以异常体名称命名）<br>
>>> pec<br>
>>> free_space<br>
>>> soil<br>
>>> coal<br>

>> predict（测试集，将所有测试图像放在该文件夹下以测试模型的表现）<br>

### 相关图片展示
* gprMax某模型结构示意图<br>
![1](https://github.com/EugeneJie/MyGPR/blob/master/images/1.png)
* gprMax模型中各种介质的性质参数<br>
![2](https://github.com/EugeneJie/MyGPR/blob/master/images/2.png)
* 探地雷达B-scan图像<br>
![3](https://github.com/EugeneJie/MyGPR/blob/master/images/3.png)
* 异常双曲线定位模型的测试结果<br>
![4](https://github.com/EugeneJie/MyGPR/blob/master/images/4.png)
* 异常体分类模型的网络结构图<br>
![5](https://github.com/EugeneJie/MyGPR/blob/master/images/5.png)
* loss值随学习率增大的变化曲线（用以确定分类模型的最佳学习率）<br>
![6](https://github.com/EugeneJie/MyGPR/blob/master/images/6.png)
* 分类模型训练过程中loss值随迭代次数增加的变化曲线<br>
![7](https://github.com/EugeneJie/MyGPR/blob/master/images/7.png)
* MyGPR软件界面<br>
![8](https://github.com/EugeneJie/MyGPR/blob/master/images/8.png)
