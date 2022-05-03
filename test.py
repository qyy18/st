import streamlit as st
import requests
from urllib3 import encode_multipart_formdata

st.set_page_config(page_title="Streamlit APP", layout="wide")
bugs = ['请选择：', '文件上传']
st.sidebar.subheader("Test")
server_url = st.sidebar.text_input(label='服务器地址', value="http://192.168.0.106:8080/")
case = st.sidebar.selectbox("选择工具", bugs)


if case == bugs[0]:
    st.subheader("Welcome")


if case == '文件上传':
    st.info('文件上传')
    pic_ex = ['png', 'jpg', 'jpeg', 'bmp']
    with st.expander('Form', True):
        api = st.text_input(label='接口名称', value="file/upload/")
        key = st.text_input(label='参数名称', value="file")
        file = st.file_uploader('选择一个文件')
        upload = st.button('上传')
        if upload and file:
            st.markdown("<p style='color:green'>uploaded</p>", True)

        else:
            st.markdown("<p style='color:red'>not upload</p>", True)
    if upload and file:
        filename = file.name
        filesize = file.size
        with st.expander('Content', True):
            for pe in pic_ex:
                if filename.endswith(pe):
                    st.image(file)
            if filename.endswith('txt') or filename.endswith('jsp'):
                st.markdown("<h6>文件内容:</h6>", True)
                line = str(file.read(), 'UTF-8')
                st.markdown(line, True)
        data = {key: (filename, file.read())}
        encode_data = encode_multipart_formdata(data)
        header = {"content-type": encode_data[1]}
        data = encode_data[0]
        r = requests.post(url=server_url + api, headers=header, data=data)
        with st.expander('Response', True):
            st.markdown(r.text)

if case == '文件下载':
    st.info('文件下载测试')
    with st.expander('Form', True):
        api = st.text_input(label='接口名称', placeholder="如：file/download/")
        key = st.text_input(label='参数名称', value="file")
        file = st.text_input(label='文件路径', value="/Users/common/test.txt")
        download = st.button('下载')
        if download and file:
            st.markdown("<p style='color:green'>downloaded</p>", True)
    if download and file:
        download_info = "download file from server: " + file
        with st.expander('Content', True):
            st.code(download_info, language="python")
        api_url = 'file/download/'
        if len(api) > 0:
            api_url = api
        param = {key: file}
        r = requests.get(url=base_url + api_url, params=param)
        with st.expander('Response', True):
            st.markdown(r.text)

if case == '文件重命名':
    st.info('文件重命名测试')
    with st.expander('Form', True):
        api = st.text_input(label='接口名称', value="file/rename/")
        file_base = st.text_input(label='原文件所在根目录', value="/Users/common/")
        key1 = st.text_input(label='原文件参数名', value="src")
        src = st.text_input(label='原文件名', value="test.txt")
        key2 = st.text_input(label='目的文件参数名', value="dst")
        dst = st.text_input(label='重命名文件为', value="test.sh")
        send = st.button('Send')
        if send:
            st.markdown("<p style='color:green'>sended</p>", True)
    if send:
        rename_info = "rename file from  " + file_base + src + " to " + file_base + dst
        with st.expander('Content', True):
            st.code(rename_info, language="python")
        data = {key1: file_base+src, key2: file_base+dst}
        r = requests.post(url=base_url + api, data=data)
        with st.expander('Response', True):
            st.markdown(r.text)

if case == '命令执行':
    st.info('命令执行测试')
    with st.expander('Form', True):
        api = st.text_input(label='接口名称', placeholder="如：cmd/")
        key = st.text_input(label='参数名称', value="cmd")
        cmd_input = st.text_input(label='输入命令', placeholder="如：whoami")
        send = st.button('Send')
        if send:
            st.markdown("<p style='color:green'>sended</p>", True)
    cmd = 'whoami'
    if len(cmd_input) > 0:
        cmd = cmd_input
    if send:
        cmd_info = "remote run cmd: " + cmd
        with st.expander('Content', True):
            st.code(cmd_info, language="python")
        api_url = 'cmd/'
        if len(api) > 0:
            api_url = api
        param = {key: cmd}
        r = requests.get(url=base_url + api_url, params=param)
        with st.expander('Response', True):
            st.markdown(r.text)
