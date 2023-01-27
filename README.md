# Japanese company extraction

This API extracts Japanese company names from text.

## Requirements

- Docker Compose

## Usage

### 1. Setup

```sh
git clone https://github.com/Doarakko/japanese-company-extraction
cd japanese-company-extraction
```

### 2. Run

```sh
docker-compose up --build
```

### 3. Go

```sh
curl -X "GET" "http://0.0.0.0:8000/company-extraction" --data-urlencode "s=<text>"
```

## Example

```sh
curl -X "GET" "http://0.0.0.0:8000/company-extraction" --data-urlencode "s=TIS株式会社は自然言語処理で企業名認識を行うための辞書JCLdic（日本会社名辞書）を無償公開。"
```

```json
{
   "companies":[
      {
         "name":"TIS株式会社",
         "extract_name":"TIS株式会社"
      },
      {
         "name":"株式会社JCL",
         "extract_name":"JCL"
      }
   ],
   "s":"TIS株式会社は自然言語処理で企業名認識を行うための辞書JCLdic（日本会社名辞書）を無償公開。"
}
```

## Credit

- [Japanese Company Lexicon (JCLdic)](https://github.com/chakki-works/Japanese-Company-Lexicon)
