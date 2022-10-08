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

- [ ] Homepage (route `/`) lists pets
- Should include...
  - Name
  - Photo, if present (add default pic!)
  - Display 'Available' if pet is available for adoption

## Step 3: Make Add Pet Form

- [ ] Make a form for adding pets using Flask-WTF
- Should include the following:
  - [ ] Pet name
  - [ ] Species
  - [ ] Img URL
  - [ ] Age
  - [ ] Notes
- [ ] Should be at URL path `/add`
- Should be a link to this on homepage

## Step 4: Create Handler for Add Pet Form

- [ ] Validate form
  - If it doesn't validate, re-render the form
  - If it does, create a new pet and redirect to homepage
- This should be a post request to `/add`

## Step 5: Add Validation

- [ ] Species should be either cat, dog, or porcupine
- [ ] Photo URL must be a URL (but still be optional)
- [ ] Age should be between 0 and 30, if provided

## Step 6: Add Display/Edit Form

- asdf

## Takeaways

- asdf
