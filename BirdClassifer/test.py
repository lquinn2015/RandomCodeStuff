ke sure you are in the directory where you downloaded infer.py to

for f in test_images/*.jpg; do echo "File: ${f}"; python2 infer.py ${f} 2>/dev/null; echo  ""; done
