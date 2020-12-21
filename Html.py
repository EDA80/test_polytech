class HtmlClass:

    def __init__(self):
        self.content = ''
        self.ending = ''
        self.toRender = ''

    def Html(self, array=[]):

        if len(array) != 0:
            
            for val in array:
                if isinstance(val, list):
                    for vall in array:
                        self.content += val
                else:
                    self.content += val

        self.toRender = '<html>\n' + self.content + '</html>\n'
        html_frame = open('template.html', 'w')
        html_frame.write(self.toRender)
        html_frame.close()

        return self.toRender

    def Head(self, title_name='none'):
        content = '<head>\n'

        if title_name == 'none':
            content += '<title>no title</title>\n'
        else:
            content += '<title>'+title_name+'</title>\n'

        content += '</head>\n'

        return content

    def Body(self, array=[]):
        content = '<body>\n'

        for val in array:
            if isinstance(val, list):
                for vall in array:
                    content += val
            else:
                content += val


        content += '</body>\n'

        return content

    def Div(self, array=[]):
        content = '<div>\n'

        for val in array:
            if isinstance(val, list):
                for vall in array:
                    content += val
            else:
                content += val

        content += '</div>\n'

        return content

    def H1(self, text='none'):
        if text == 'none':
            return '<h1>No content was set</h1>\n'
        else:
            return '<h1>'+text+'</h1>\n'

    def H2(self, text='none'):
        if text == 'none':
            return '<h2>No content was set</h2>\n'
        else:
            return '<h2>'+text+'</h2>\n'

    def H3(self, text='none'):
        if text == 'none':
            return '<h3>No content was set</h3>\n'
        else:
            return '<h3>'+text+'</h3>\n'

    def H4(self, text='none'):
        if text == 'none':
            return '<h4>No content was set</h4>\n'
        else:
            return '<h4>'+text+'</h4>\n'

    def H5(self, text='none'):
        if text == 'none':
            return '<h5>No content was set</h5>\n'
        else:
            return '<h5>'+text+'</h5>\n'

    def Img(self, text='none'):
        if text == 'none':
            return '<img src=""></h1>\n'
        else:
            return '<img src="science-of-earworms-explain-why-never-gonna-give-you-up-is-stuck-in-our-heads-30-years-later.png"></h1>\n'

    def Span(self, text='none'):
        if text == 'none':
            return '<span>No content was set</span>\n'
        else:
            return '<span>'+text+'</span>\n'

    def P(self, text='none'):
        if text == 'none':
            return '<p>No content was set</p>\n'
        else:
            return '<p>'+text+'</p>\n'
