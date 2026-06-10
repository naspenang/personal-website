try:
    from PIL import Image
    import sys

    img_path = r"d:\_ASSISTANTS\COURSES\SEM_4\IML254\projects\personal_website\images\iclam_logo_new.png"
    img = Image.open(img_path).convert("RGBA")
    
    # We want to change the white/light colors to a nice dark blue matching the theme #2980b9 -> (41, 128, 185) or darker #2c3e50 -> (44, 62, 80)
    target_r, target_g, target_b = 41, 128, 185
    
    data = img.getdata()
    new_data = []
    
    for item in data:
        r, g, b, a = item
        if a > 0:
            # Recolor everything that has opacity to the target blue, maintaining alpha
            # Or just recolor white pixels. Since it's a white logo, we can just recolor all non-transparent pixels.
            new_data.append((target_r, target_g, target_b, a))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(img_path)
    print("Successfully recolored the iClam logo.")
except ImportError:
    print("PIL not installed. Installing Pillow...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    
    # Try again
    from PIL import Image
    img = Image.open(img_path).convert("RGBA")
    target_r, target_g, target_b = 41, 128, 185
    data = img.getdata()
    new_data = [(target_r, target_g, target_b, a) if a > 0 else item for item in data]
    img.putdata(new_data)
    img.save(img_path)
    print("Successfully recolored the iClam logo after installing Pillow.")
except Exception as e:
    print(f"Error: {e}")
