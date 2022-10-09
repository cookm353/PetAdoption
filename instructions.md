# Adoption Agency

## Step 1: Create a Database and Model

- [x] Make a model called Pet
  - **id**: auto-incrementing int
  - **name**: text, required
  - **species**: text, required
  - **photo_url**: text, optional
  - **age**: int, optional
  - **notes**: text, optional
  - **available**: Boolean, required, defaulted to available

## Step 2: Make a Homepage Listing Pets

- [x] Homepage (route `/`) lists pets
- Should include...
  - [x] Name
  - [x] Photo, if present (add default pic!)
  - [x] Display 'Available' if pet is available for adoption in bold
- [ ] Finish styling

## Step 3: Make Add Pet Form

- [x] Make a form for adding pets using Flask-WTF
- Should include the following:
  - [x] Pet name
  - [x] Species
  - [x] Img URL
  - [x] Age
  - [x] Notes
- [x] Should be at URL path `/add`
- [ ] Add a link to this on homepage

## Step 4: Create Handler for Add Pet Form

- [x] Validate form
  - [x] If it doesn't validate, re-render the form
  - [x] If it does, create a new pet and redirect to homepage
- [x] This should be a post request to `/add`

## Step 5: Add Validation

- [x] Species should be either cat, dog, or porcupine
- [x] Photo URL must be a URL (but still be optional!)
- [x] Age should be between 0 and 30, if provided

## Step 6: Add Display/Edit Form

- [ ] Make a page displaying info about the pet
  - [ ] Name
  - [ ] Species
  - [ ] Photo (if present)
  - [ ] Age (if present)
- [ ] Should also have a form that lets us edit the pet
  - [ ] Photo URL
  - [ ] Notes
  - [ ] Availability
- [ ] Should be at /[pet_id_number]
  - [ ] Homepage should link to this

## Step 7: Handle Edit Form

- [ ] Validate form
  - [ ] Re-render if it doesn't validate
  - [ ] Edit pet if it does
- [ ] Should be a POST request to /[pet_id_number]

## Step 8: Clean up Code

- [x] Make sure function names start with a verb
- [x] Good variable names
- [ ] Every class or function should have a docstring
- [ ] Add comments to areas that'd benefit
- [x] Add a file showing all of the Python requirements

## Further Study

- [ ] Add message flashing to give feedback after a pet is added/edited
- [ ] Divide homepage into listings for pets that are available and ones that aren't
- [ ] Add Bootstrap and a simple theme
- [ ] Instantiate a pet directly from the dictionary of values from the form
- [ ] Add a field for a photo upload in addition to URL field
  - [ ] Save file to /static/images
  - [ ] Make it so only one of these can be used
  - [ ] If user tries to use both, return a validation error

## Takeaways

- Just keep the venv folder in the project folder, that's what .gitignore is for
- Learn Bootstrap.  Seriously.
- Keeping the project folder neater with subfolders makes things a lot easier
