from background.background import Background

def main():
    # Create background object
    bk = Background()

    # Example 1 - Change background to specific image
    bk.change('testing\\test_image.jpg')

    # Example 2
    # Choose background at random from files in a folder
    bk.random_from_folder('testing')

    # Example 3
    # Choose background at random from files in a list
    files = ['testing\\test_image.jpg', 'testing\\test_image2.jpg',
             'testing\\test_image3.jpg', 'testing\\test_image4.jpg']
        
    bk.random_from_list(files)

    # Example 4
    # Set verbose = False to prevent detailed command line printing
    bk.verbose = False
    bk.change('testing\\test_image4.jpg')
    
    return

if __name__ == '__main__':
    main()
