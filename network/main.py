# データのロード
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# データの整形
from tensorflow.keras.utils import to_categorical

x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# ここから
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255
# ここまでがないと予測精度ひどい

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# モデル構築
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

model = Sequential()

model.add(Dense(units=256, input_shape=(784,)))
model.add(Activation('relu'))
model.add(Dense(units=100))
model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 学習
model.fit(x_train, y_train, batch_size=1000, epochs=100, verbose=1, validation_data=(x_test, y_test))

# 性能評価
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

import numpy as np
X = []
X.append(x_test[100])
X = np.asarray(X)

print(model.predict(X))

# モデルの保存
from tensorflow.keras.models import load_model
model.save('model.h5', include_optimizer=True)
