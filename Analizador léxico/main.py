# from scanner import Scanner

# def main():
#     s = Scanner('const true = 2 || false !')
#     tokens = s.scanAll()
#     print(tokens)

# if __name__ == '__main__':
#     main()

from scanner import Scanner

def analyze_file(file_path):
    try:
        print('sfd')
        with open(file_path, 'r') as file:
            content = file.read()
            
        scanner = Scanner(content)
        tokens = scanner.scanAll()
        
        print("Tokens encontrados:")
        for token in tokens:
            print(token)
            
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado")
    except Exception as e:
        print(f"Error durante el análisis: {str(e)}")

if __name__ == "__main__":
    analyze_file('factorize.gox')
