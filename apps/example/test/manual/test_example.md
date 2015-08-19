# Example Suite
## fxos.func.sanity.launch_contacts
`draft`

WHEN Launch contacts app. 
THEN It works!

## fxos.func.sanity.add_contacts
`active`

WHEN Launch contacts app. 
THEN It opens
WHEN Add a contact. 
THEN The contact is successfully added

## fxos.func.sanity.click_buttons
`disabled`

WHEN I click the :color button
THEN The button :behavior

| color |  behavior |
|-------|-----------|
| green |  glows    |
| red   |  disappers|



