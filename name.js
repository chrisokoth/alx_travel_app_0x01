``html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Image Upload</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 20px;
      }
      .image-group {
        margin-bottom: 20px;
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 5px;
      }
      .image-group input {
        margin: 5px 0;
      }
      .remove-btn {
        margin-top: 10px;
        color: white;
        background-color: red;
        border: none;
        padding: 5px 10px;
        cursor: pointer;
      }
    </style>
  </head>
  <body>
    <h1>Upload Images</h1>
    <form id="uploadForm" enctype="multipart/form-data">
      <div id="imageInputs">
        <!-- Dynamic image input groups will be added here -->
      </div>
      <button type="button" onclick="addImageInput()">Add Image</button>
      <br /><br />
      <button type="submit">Upload</button>
    </form>

    <script>
      const imageInputsContainer = document.getElementById('imageInputs');

      // Function to add a new image input group
      function addImageInput() {
        const index = imageInputsContainer.children.length;
        const div = document.createElement('div');
        div.className = 'image-group';
        div.innerHTML = `
        <label for="images">Select Image:</label>
        <input type="file" name="images" accept="image/*" required>
        <br>
        <label for="altText">Alt Text:</label>
        <input type="text" name="altText" placeholder="Enter alt text">
        <br>
        <label for="videoUrl">Video URL:</label>
        <input type="url" name="videoUrl" placeholder="Enter video URL">
        <br>
        <button type="button" class="remove-btn" onclick="removeImageInput(this)">Remove</button>
      `;
        imageInputsContainer.appendChild(div);
      }

      // Function to remove an image input group
      function removeImageInput(button) {
        const group = button.parentElement;
        imageInputsContainer.removeChild(group);
      }

      // Handle form submission
      const form = document.getElementById('uploadForm');
      form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData();
        const images = document.querySelectorAll('input[name="images"]');
        const altTexts = document.querySelectorAll('input[name="altText"]');
        const videoUrls = document.querySelectorAll('input[name="videoUrl"]');

        // Attach images and their metadata to FormData
        images.forEach((image, index) => {
          formData.append('images', image.files[0]); // Attach the file
          formData.append(
            'metadata',
            JSON.stringify({
              altText: altTexts[index].value,
              videoUrl: videoUrls[index].value,
            }),
          );
        });

        // Add the global setupId
        formData.append('setupId', '1');

        try {
          const response = await fetch('/api/images/upload', {
            method: 'POST',
            body: formData,
          });

          if (response.ok) {
            alert('Images uploaded successfully!');
          } else {
            const result = await response.json();
            alert('Error: ' + result.message);
          }
        } catch (error) {
          console.error('Error:', error);
          alert('An error occurred during the upload.');
        }
      });
    </script>
  </body>
</html>
```