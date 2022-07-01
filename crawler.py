from requests import get  

def download(url, file_name = None):
	if not file_name:
		file_name = url.split('/')[-1]

	with open(file_name, "wb") as file:   
        	response = get(url)               
        	file.write(response.content)      

if __name__ == '__main__':
        ext = ['bmp','cr2','cur','dds','dng','erf','exr','fts','gif','hdr','heic','heif','ico','jfif','jp2','jpe','jpeg','jpg','jps','mng','nef','nrw','orf','pam','pbm','pcd','pcx','pef','pes','pfm','pgm','picon','pict','png','pnm','ppm','psd','raf','ras','rw2','sfw','sgi','svg','tga','tiff','wbmp','webp','wpg','x3f','xbm','xcf','xpm','xwd']
        for i in ext:
            url = "https://filesamples.com/samples/image/" + i + "/sample_1280x853." + i
            download(url)
