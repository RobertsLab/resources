# Website Subscription Setup

This document provides guidance on configuring the email subscription feature added to the Roberts Lab Handbook homepage.

## Overview

A subscription form has been added to the main page (`docs/index.md`) allowing visitors to subscribe to lab updates with their choice of weekly or monthly frequency.

## Integration with Email Services

The subscription form is designed to integrate with popular email service providers. To connect it with your chosen service:

### Option 1: Mailchimp
1. Create a Mailchimp account and mailing list
2. Generate an embedded form code from Mailchimp
3. Update the `action` attribute in the form to point to your Mailchimp endpoint
4. Example: `action="https://your-domain.us1.list-manage.com/subscribe/post?u=YOUR_USER_ID&id=YOUR_LIST_ID"`

### Option 2: ConvertKit
1. Set up a ConvertKit account and create a form
2. Get the form action URL from ConvertKit
3. Update the form action accordingly
4. Example: `action="https://app.convertkit.com/forms/YOUR_FORM_ID/subscriptions"`

### Option 3: Other Services
The form can work with any service that accepts standard HTML form submissions with:
- `email` field (email address)
- `frequency` field (weekly/monthly preference)

## Form Fields

- **Email Address**: Required email input field
- **Update Frequency**: Radio buttons for "Weekly Updates" or "Monthly Summary"
- **Subscribe Button**: Submits the form

## Styling

The form uses CSS custom properties to match the Material theme:
- `--md-primary-fg-color` for accent colors
- `--md-default-bg-color` for backgrounds
- `--md-default-fg-color--light` for secondary text

## Location

The subscription form is located at the bottom of the homepage (`docs/index.md`) in the "Stay Updated with Roberts Lab" section.