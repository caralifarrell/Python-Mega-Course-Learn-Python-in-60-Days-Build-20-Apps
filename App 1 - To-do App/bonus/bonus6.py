contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly slides.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

# To create multiple files

for content, filenames in zip(contents, filenames):
    file = open(f"../files/{filenames}", 'w')  # .. to go one directory up one level, goes to app1 > files
    file.write(content)

a = "I am a string " \
     "on my "\
     "own"
