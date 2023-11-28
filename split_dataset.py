from sklearn.model_selection import train_test_split

import numpy as np
import os
import shutil

# Obter uma lista com os nomes dos arquivos
PATH = 'dataset/Orelha_elefante'
filenames = os.listdir(PATH)
print(f'Número de arquivos: {len(filenames)}')

# Remover a extensão .jpg e .txt
filenames = list(map(lambda name: name.split('.')[0], filenames))
# Remover as duplicações
filenames = list(set(filenames))
print(f'Número de arquivos: {len(filenames)}')

# Separação entre treino, validação e teste
train, rest = train_test_split(filenames, test_size= 0.3, random_state=42)
test, val = train_test_split(rest, test_size= 0.5, random_state=42)
print(f'Número de arquivos de treino: {len(train)}')
print(f'Número de arquivos de validação: {len(val)}')
print(f'Número de arquivos de teste: {len(test)}')

# Criar diretório de treino
train_dir = 'final_dataset/train'
if not os.path.exists(train_dir):
    os.makedirs(train_dir)
    print('Diretório dos arquivos de treino foi criado!')
    
# Criar diretório de validação
val_dir = 'final_dataset/val'
if not os.path.exists(val_dir):
    os.makedirs(val_dir)
    print('Diretório dos arquivos de validação foi criado!')

# Criar diretório de teste
test_dir = 'final_dataset/test'
if not os.path.exists(test_dir):
    os.makedirs(test_dir)
    print('Diretório dos arquivos de teste foi criado!')

# Mover arquivos de treino para o diretório de treino
for train_file in train:
    img = f'{PATH}/{train_file}.jpg'
    annotation = f'{PATH}/{train_file}.txt'
    shutil.move(img, train_dir)
    shutil.move(annotation, train_dir)
    
# Mover arquivos de validação para o diretório de validação
for val_file in val:
    img = f'{PATH}/{val_file}.jpg'
    annotation = f'{PATH}/{val_file}.txt'
    shutil.move(img, val_dir)
    shutil.move(annotation, val_dir)

# Mover arquivos de teste para o diretório de teste
for teste_file in test:
    img = f'{PATH}/{teste_file}.jpg'
    annotation = f'{PATH}/{teste_file}.txt'
    shutil.move(img, test_dir)
    shutil.move(annotation, test_dir)

print('OK!')

