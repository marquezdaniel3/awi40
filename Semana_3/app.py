import web

urls = (
    '/(.*)', 'mvc.controllers.hello.visita'
)
app = web.application(urls, globals())



if __name__ == "__main__":
    app.run()