
outlets = 1;

function readfile(s)
{
	var f = new File(s);
	var i,a,c;

	if (f.isopen) {
		c = f.eof;
		for (i=0;i<c;i++) {
			a = f.readchars(1); //returns an array of single character strings
			//post("char at fileposition[" + f.position + "]: " + a + "\n");
		}
		f.close();
		outlet(0, 1);
	} else {
		//post("could not open file: " + s + "\n");
		outlet(0, 0);
	}
}

/*
function writefile(s)
{
	var f = new File(s,"write","TEXT"); 
	var s2 = "I am a file named " + f.filename + ", located in " + f.foldername;

	if (f.isopen) {
		post("writing string to file: " + s2 + "\n");
		f.writestring(s2); //writes a string
		f.close();
	} else {
		post("could not create file: " + s + "\n");
	}
}

function copyfile(src,dst)
{
	var i,a,c;
	var srcfile = new File(src,"read"); 
	if (srcfile.isopen) {
		var dstfile = new File(dst,"write",srcfile.filetype); 
		c = srcfile.eof;
		if (dstfile.isopen) {
			post("copying: " + src + " to " + dst + "\n");
			for (i=0;i<c;) {
				a = srcfile.readbytes(32); //returns array of bytes, in this case upto 32 at a time
				if (a.length) {
					dstfile.writebytes(a);
					i += a.length;
				} else {
					break; //shouldn't get here, but just incase
				}
			}
			dstfile.eof = c;
			dstfile.close();
		} else {
			post("could not create file: " + dst + "\n");
		}
		srcfile.close();
	} else {
		post("could not create file: " + src + "\n");
	}
}

function readlines(s)
{
	var f = new File(s);
	var i,a,c;

	if (f.isopen) {
		i=0;
		while ((a = f.readline()) != null) { // returns a string
			post("line[" + i + "]: " + a + "\n");
			i++;
		}
		f.close();
	} else {
		post("could not open file: " + s + "\n");
	}
}
*/