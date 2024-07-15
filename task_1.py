import os
import shutil
import sys

def recursive_copy(src_dir, dst_dir):
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        if os.path.isdir(item_path):
            recursive_copy(item_path, dst_dir)
        else:
            file_ext = os.path.splitext(item)[1][1:]  # get file extension
            dst_subdir = os.path.join(dst_dir, file_ext)
            if not os.path.exists(dst_subdir):
                os.makedirs(dst_subdir)
            dst_file_path = os.path.join(dst_subdir, item)
            try:
                shutil.copy2(item_path, dst_file_path)
                print(f"Copied {item} to {dst_file_path}")
            except Exception as e:
                print(f"Error copying {item}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <src_dir> [<dst_dir>]")
        sys.exit(1)

    src_dir = sys.argv[1]
    dst_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.exists(src_dir):
        print(f"Error: {src_dir} does not exist")
        sys.exit(1)

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    recursive_copy(src_dir, dst_dir)

    # Run the copy and sort operation
    print(f"Copying files from {args.src_dir} to {args.dst_dir}")
    copy_and_sort_files(args.src_dir, args.dst_dir)



