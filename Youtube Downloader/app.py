from flask import Flask, jsonify, render_template, request, redirect, session, url_for
from pytube import YouTube
import sys

app = Flask(__name__)
app.secret_key = 'ytdownload'
app.config['SESSION_TYPE'] = 'filesystem'


link = ''
videoName = ''
videoTumbnail = ''
availableResolution = []
selectedResolution = []
yt = YouTube('https://youtu.be/lxKufwwtz4E')
resolutions = []


@app.route('/', methods=['POST', 'GET'])
def getlink():
    global data
    method = request.method
    print(method)
    if method == 'POST':
        isPostback = True
        link = str(request.form['tag'])
        print(link)
        session['link'] = link
        st = extractInformation(link)
        print('Completed again')
        return redirect(url_for('downloadPage', name=videoName, resol=availableResolution))
    return render_template('index.html')


@app.route('/<name>/<resol>', methods=['POST', 'GET'])
def downloadPage(name, resol):
    if request.method == 'POST':
        index = request.form.get('index')
        if index is None:
            index = 0
        if int(index) > len(availableResolution):
            index = 0
        index = int(index)
        download(index)
    print('redirecting')
    print(videoTumbnail)
    return render_template('index.html', name=name, resol=resol, img=videoTumbnail)


def extractInformation(link):
    global videoName
    global videoTumbnail
    global availableResolution
    global selectedResolution
    global yt
    global resolutions
    fileSize = []
    try:
        print('link: ', link)
        yt = YouTube(link)
    except:
        print('Connection Error')
        sys.exit()
    print('Extracting Information...')
    availableResolution = [
        stream.resolution for stream in yt.streams.filter(progressive=True)]
    videoName = yt.title[0:20]+"..."
    videoTumbnail = yt.thumbnail_url
    sizeIn = 'MB'
    for r in availableResolution:
        resolutions.append((r))
        size = yt.streams.filter(
            resolution=r).first().filesize/(1024*1024)
        if size >= 1000:
            size /= 1024
            sizeIn = 'GB'
        size = round(size, 2)
        fileSize.append(str(size)+sizeIn)
    print(videoName)
    size = len(availableResolution)
    count = 1
    for r in availableResolution:
        availableResolution[count-1] = availableResolution[count -
                                                           1] + ' - ' + fileSize[count-1]
        print(f'{count}: {r} Size: {fileSize[count-1]}')
        count += 1
    print('completed')
    return yt


@app.route('/download', methods=['GET', 'POST'])
def download(index):
    global yt
    global resolutions
    downloadLocation = 'Downloads'
    print('Download Started')
    yt.streams.filter(
        resolution=resolutions[index]).first().download(downloadLocation)
    print('Download Finished\nDownload Path: ')
    return render_template('index.html')


if __name__ == "__main__":

    app.run(debug=True)
