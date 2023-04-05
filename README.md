# 数据分析流程

## 数据筛选

1. 输入：路径点数据/线数据、路径属性数据、北京市面数据
2. 处理
   1. 连接：线数据-属性数据连接（完成）
   2. 筛选：筛选位于北京的数据（完成）
   3. 合并：合并北京线数据（完成）
   4. 拆分：将多线数据拆分为单线数据
   5. 分类：根据`triptype`划分
   6. 优化：去除杂线、去除距离较远的误差点
3. 输出：位于北京的分类轨迹线数据
    ![pic](../outputs/分类清洗后图片.png)

## 数据处理

1. 处理方法：线密度中心线提取+打断+小节要素赋值
2. `属性`内容：线密度、经停者属性
3. `要素`内容：坡度、气候、景观

## 当前问题

1. 数据分类重新编码
2. 数据筛选
