from pydantic import BaseModel
import unicodedata

from fastapi import FastAPI, Form
import MeCab


app = FastAPI()

tagger = MeCab.Tagger("-r /usr/local/etc/mecabrc")


class Company(BaseModel):
    name: str
    extract_name: str


@app.get("/company-extraction")
def extract_companies(s: str=Form(...)):
    text = unicodedata.normalize("NFKC", s)
    node = tagger.parseToNode(text)

    companies = []
    while node:
        features = node.feature.split(",")

        if features[2] == "組織" and features[6] != "*":
            companies.append(Company(name=features[6], extract_name=node.surface))

        node = node.next

    return {"companies": companies, "s": s}
