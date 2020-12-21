import Html as Html

html = Html.HtmlClass()

html.Html([html.Head('testPage'), html.Body([html.Div([html.H1('text'), html.H2('text2'), html.H3('text3'), html.H4('text4'), html.H5('text5')]), html.Div([html.Img('href to image'), html.Span('this is the image'), html.P('text under the image')]), html.Div([html.Span('textHere'), html.Span()])])])
