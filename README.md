# 並列分散処理課題(Parallel_QuickSort)
pythonのconcurrent.futuresを利用した並列分散処理を行ったクイックソートと逐次処理のクイックソートを比べるためのリポジトリ

#実験内容  
クイックソートを並列化し速度の向上を図る。  
使用モジュールはpythonのConcurrent.fututes.ThreadPoolExecutorとConcurrent.futures.ProcessPoolExecutorを使用した。  

#コード内容  
Parallel_QuickSort.pyにプロセスで並列化、スレッドで並列化、逐次処理の順番で処理させるようになっている。  
ソートされるデータは変数(arr)の中に0から1万までのランダムの数字が1万個配列に入っていて、それをソートする。  

#実行方法  
pythonの実行環境を整えてもらった状態で、そのまま実行してもらって良い。  
concurrent.futuresやrandom、timeなどはpythonの標準ライブラリであるためインストールなどはしなくて良い。  
ソートされた中身が見たい場合は39,49,56行目のコメントアウトを外すと見れるようになる。  
