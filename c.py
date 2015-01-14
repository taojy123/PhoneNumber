import os

TEMPLATE = """
<html>
<head>
    <script type="text/javascript" src="../jquery.js"></script>
    <script type="text/javascript">
    $(function(){
        $("button").click(function(){
           $(this).next().toggle()
        })
        $("a").click(function(){
            var num = $(this).html()
            top.location.href = "../phone.html?" + num
        })
    })
    </script>
    <style type="text/css">
        body{
            text-align: center;
        }
        div{
            display:none;
            text-align: center;
            width: 95%;
        }
        a{
            cursor: pointer;
            color: blue;
            margin-left: 30px;
        }
    </style>
</head>

<body>
    <!--$$-->
</body>

</html>

"""


names = os.listdir("./citys/")

for name in names:
    fn = "./citys/" + name
    print fn
    s = TEMPLATE
    lines = open(fn).readlines()
    h = lines[0][:3]
    r = []
    for line in lines:
        line = line.strip()
        h2 = line[:3]
        if h == h2:
            r.append(line)
        else:
            content = """
            <button>%s</button>
            <div>
                <a>%s</a>
            </div>
            <br/>
            """ % ( h, "</a>\n<a>".join(r) )
            s = s.replace("<!--$$-->", content+"<!--$$-->")
            h = h2
            r = [line]
    content = """
    <button>%s</button>
    <div>
        <a>%s</a>
    </div>
    <br/>
    """ % ( h, "</a>\n<a>".join(r) )
    s.replace("<!--$$-->", content+"<!--$$-->")

    open(fn, "w").write(s)


print "ok"


