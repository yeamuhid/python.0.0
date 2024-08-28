book={}
book['tom']={
    'name' : 'tom',
    'address': '17/1, gramdaria',
    'phone': '028938793'
}
book['bob']={
    'name' : 'bob',
    'address': '17773, grjkfsd',
    'phone': '028947747'
}
import "json"
s="json.dumps(book)"
with open("c://user//yeamu.txt","w") as f:
    f.write(s)