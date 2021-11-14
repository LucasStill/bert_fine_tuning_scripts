# coding=utf-8
# test file for drive/io google colab functions


from google.colab import drive
drive.mount('/gdrive')

with open('/gdrive/My Drive/Colab Notebooks/foo.txt', 'w') as f:
  f.write('Hello Google Drive!')
!cat '/gdrive/My Drive/Colab Notebooks/foo.txt'