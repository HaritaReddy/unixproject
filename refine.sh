#!/bin/bash/
echo "Enter the name with which you want to save the book"
read book
sed -e 's:<p.*>: :g; s:</p>: :g; s:<br />: :g; s:<br/>: :g; s:<em.*>: :g; s:</em>: :g; s:<strong.*>: :g; s:</strong>: :g' inter | cat>"$book"
rm inter

