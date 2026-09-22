# Knapsack App

Protótipo didático de seleção de itens sob restrição de capacidade, com Python, PuLP/CBC e Streamlit.

## Arquivos principais

- `scripts/app.py`: interface e modelo de mochila binária.
- `data/knapsack.csv`: exemplo de entrada.
- `models/ks.py`: implementação auxiliar.
- `Dockerfile`: configuração histórica de execução.

## Estado

Protótipo anterior ao ORKit atual. O endereço antigo de hospedagem foi removido da apresentação porque não há implantação atual verificada. As dependências e a interface precisam de atualização e execução em ambiente atual antes de considerar o projeto pronto para demonstração.

Ponto conhecido a revisar: `st.set_option('deprecation.showfileUploaderEncoding', False)` usa uma opção antiga do Streamlit. Também faltam verificações explícitas do status do solver e da estrutura do CSV. Essas observações vieram da inspeção de código; a aplicação não foi executada nesta revisão.

## Relação com o ORKit

O problema da mochila é útil para fundamentos de otimização discreta. A versão revisada deve convergir para a biblioteca [orkit-free](https://github.com/helano-pessoa/orkit-free); este protótipo foi preservado, sem duplicar sua interface no produto.
