<div id="test"></div>
<script type="text/javascript" src="renderjson.js"></script>
<script>
var example = {
    "glossary": {
        "title": "example glossary",
        "comprehensive": true,
        "link": undefined,
        "count": 1,
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
};
document.getElementById("test").appendChild(renderjson(example));
</script>
