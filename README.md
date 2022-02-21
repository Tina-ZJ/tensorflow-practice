# tensorflow-practice
basic scripts with tensorflow 

### tensorboard
[tensorboard.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/tensorboard.py)
### tensorflow常量定义
[constant.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/constant.py)
### eager执行测试
[eager.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/eager.py)
### eager中求解梯度
[gradient.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/gradient.py)
### tf.gradients求解梯度
[gradients_chain.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/gradients_chain.py)
### 测试tf.nn.embedding_lookup和tf.gather速度
[test_lookup.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/test_lookup.py)
### tf.argsort 返回降序或升序后的索引位置值
[argsort.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/argsort.py)
### tf.argmax 求最大的值索引位置
[argmax.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/argmax.py)
### tf.assign 对一个variable node进行赋值
[assign.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/assign.py)
### tf.case 条件判断选择
[case.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/case.py)
### tf.cast tensor数据类型转换
[cast.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/cast.py)
### tf.clip_by_norm 将tensor值修剪到最大为L2-norm
[clip_by_norm.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/clip_by_norm.py)
### tf.clip_by_value 将tensor值归一化到min和max之间
[clip_by_value.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/clip_by_value.py)
### tf.concat 将tensor拼接
[concat.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/concat.py)
### tf.cond 条件语句,if else作用
[cond.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/cond.py)
### tf.dynamic_partition 对data进行分片处理
[dynamic_partition.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/dynamic_partition.py)
### tf.constant 常量constant定义
[constant_v2.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/constant_v2.py)
### tf.convert_to_tensor 将numpy arrays, python list, scalar转tensor
[convert_to_tensor.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/convert_to_tensor.py)
### tf.ensure_shape 检查tensor的shape，若不符合，则会抛出异常
[ensure_shpe.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/ensure_shape.py)
### tf.expand_dims 将tensor的扩展维度
[expand_dims.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/expand_dims.py)
### tf.eye 生成单位矩阵，对角元素为1，其它为0
[eye.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/eye.py)
### tf.fill 用给定的值生成tensor
[fill.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/fill.py)
### tf.gather 根据索引取tensor值
[gather.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/gather.py)
### tf.get_current_name_scope 获取当前的scope name
[get_current_name_scope.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/get_current_name_scope.py)
### tf.get_static_value 获取tensor的值，得到numpy ndarray值
[get_static_value.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/get_static_value.py)
### tf.identity 返回和输入形状和内容一样的tensor
[identity.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/identity.py)
### tf.is_tensor 检查python object是否是tensor type
[is_tensor.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/is_tensor.py)
### tf.linspace 相当于python range函数
[linspace.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/linspace.py)
### tf.make_ndarray 将tensorProto的值返回为一个numpy array
[make_ndarray.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/make_ndarray.py)
### tf.map_fn 将输入的tensor的每个元素用给定的函数fn进行变化
[map_fn.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/map_fn.py)
### tf.norm 计算tensor的norms，支持(l1, l2, inf-norm, euclidean)
[norm.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/norm.py)
### tf.one_hot 根据索引值，返回one-hot tensor
[one_hot.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/one_hot.py)
### tf.ones 生成一个tensor，所有元素值为1
[ones.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/ones.py)
### tf.ones_like 生成一个和输入tensor一样的shap，并且所有元素值为1
[ones_like.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/ones_like.py)
### tf.parallel_stack 对输入的List tensor进行stack
[parallel_stack.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/parallel_stack.py)
### tf.print 打印tensor
[print.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/print.py)
### normal and uniform initializer初始化
[initializer.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/initializer.py)
### tf中的range函数
[range.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/range.py)
### 求一个tensor的秩
[rank.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/rank.py)
### 两个数相除
[realdiv.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/realdiv.py)
### 对输入tensor做repeat操作
[repeat.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/repeat.py)
### 对输入tensor做reshape操作
[reshape.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/reshape.py)
### 对输入tensor做reverse操作
[reverse.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/reverse.py)
### 对输入tensor进行scan转换操作
[scan.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/scan.py)
### 得到一个mask tensor
[sequence_mask.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/sequence_mask.py)
### 求一个tensor的shape
[shape.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/shape.py)
### 求一个tensor的元素数量
[size.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/size.py)
### 从一个tensor抽取对应的区域范围
[slice.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/slice.py)
### 对tensor排序
[sort.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/sort.py)
### 对tensor分割
[split.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/split.py)
### 对tensor的size为1的dimension去掉
[squeeze.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/squezze.py)
### 对tensor进行stack
[stack.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/stack.py)
### stop_gradient操作, 对一个tensor梯度屏蔽
[stop_gradient.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/stop_gradient.py)
### switch_case操作, 进行分支函数选择
[switch_case.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/switch_case.py)
### tensor_scatter_nd_add按照索引对一个tensor进行加值操作
[tensor_scatter_nd_add.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/tensor_scatter_nd_add.py)
### tensor_scatter_nd_update按照索引对一个tensor的值进行update操作
[tensor_scatter_nd_update.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/tensor_scatter_nd_update.py)
### tensordot对tensor a 和b按照axes进行dot乘积
[tensordot.py](https://github.com/Tina-ZJ/tensorflow-practice/blob/main/tensordot.py)
