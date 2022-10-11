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
- [x] Style page

## Step 3: Make Add Pet Form

- [x] Make a form for adding pets using Flask-WTF
- Should include the following:
  - [x] Pet name
  - [x] Species
  - [x] Img URL
  - [x] Age
  - [x] Notes
- [x] Should be at URL path `/add`
- [x] Add a link to this on homepage

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

- [x] Make a page displaying info about the pet
  - [x] Name
  - [x] Species
  - [x] Photo (if present)
  - [x] Age (if present)
- [x] Should also have a form that lets us edit the pet
  - [x] Photo URL
  - [x] Notes
  - [x] Availability
- [x] Should be at /[pet_id_number]
  - [x] Homepage should link to this

## Step 7: Handle Edit Form

- [x] Validate form
  - [x] Re-render if it doesn't validate
  - [x] Edit pet if it does
- [x] Should be a POST request to /[pet_id_number]

## Step 8: Clean up Code

- [x] Make sure function names start with a verb
- [x] Good variable names
- [x] Every class or function should have a docstring
- [x] Add comments to areas that'd benefit
- [x] Add a file showing all of the Python requirements

## Further Study

- [x] Add message flashing to give feedback after a pet is added/edited
- [x] Divide homepage into listings for pets that are available and ones that aren't
- [x] Add Bootstrap and a simple theme
- [ ] Instantiate a pet directly from the dictionary of values from the form
- [ ] Add a field for a photo upload in addition to URL field
  - [ ] Save file to /static/images
  - [ ] Make it so only one of these can be used
  - [ ] If user tries to use both, return a validation error

## Takeaways

- Just keep the venv folder in the project folder, that's what .gitignore is for
- Learn Bootstrap.  Or Tailwind.  Seriously.
- Keeping the project folder neater with subfolders makes things a lot easier
- Choices need to be set before the `if form.validate_on_submit()` block
- Writing tests for post requests for this is a pain
- Never work directly on the main branch in Git.  Create new branches and merge the changes when they're up and running
- 
