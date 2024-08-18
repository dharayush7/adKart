
# ADKart
## Description
Welcome to the ADKart project! This README file provides an overview of the project, including its features, tech stack, setup instructions, and additional requirements.

## Project Overview

ADKart is a dynamic e-commerce website built to provide users with a seamless shopping experience. The website allows users to browse and list products, place orders with secure payment processing, and receive live updates on their order status. Additionally, a contact form is available for user inquiries.

## Features

- **Product Listing:** Browse a variety of products listed on the platform.
- **Order Placement:** Users can place orders with integrated payment processing.
- **Live Order Updates:** Real-time updates on order status.
- **Contact Us Form:** Reach out with questions or feedback.
## Tech Stack

- **Framework:** Django
- **Payment Gateway:** PayU
- **Cloudflare Tunnel:** For secure payment processing and development
## Setup Instructions
### Prerequisites

- Python 3.x
- Django
- PayU account and credentials
- Cloudflare Tunnel account (for localhost development)

### Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/dharayush7/adKart.git
cd ADKart
```

#### 2. **Create a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### 3. **Install Dependencies:**
 ```bash
   pip install -r requirements.txt
```

#### 4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

#### 5. Create Admin user

```bash
python manage.py createsuperuser
```
Provide some information like username, email and password

#### 6. Create a cloudflare tunnnel

Open a new terminal and run following command to create a temporary tunnerl.
- Note - cloudflare must be installed in the system. To verify run 
```bash
cloudflared --version
```
- For more information visit - https://developers.cloudflare.com/pages/how-to/preview-with-cloudflare-tunnel/

```bash
cloudflared tunnel --url http://localhost:8000
```
- Output look like this:
```bash
2021-07-15T20:11:29Z INF Cannot determine default configuration path. No file [config.yml config.yaml] in [~/.cloudflared ~/.cloudflare-warp ~/cloudflare-warp /etc/cloudflared /usr/local/etc/cloudflared]
2021-07-15T20:11:29Z INF Version 2021.5.9
2021-07-15T20:11:29Z INF GOOS: linux, GOVersion: devel +11087322f8 Fri Nov 13 03:04:52 2020 +0100, GoArch: amd64
2021-07-15T20:11:29Z INF Settings: map[url:http://localhost:3000]
2021-07-15T20:11:29Z INF cloudflared will not automatically update when run from the shell. To enable auto-updates, run cloudflared as a service: https://developers.cloudflare.com/argo-tunnel/reference/service/
2021-07-15T20:11:29Z INF Initial protocol h2mux
2021-07-15T20:11:29Z INF Starting metrics server on 127.0.0.1:42527/metrics
2021-07-15T20:11:29Z WRN Your version 2021.5.9 is outdated. We recommend upgrading it to 2021.7.0
2021-07-15T20:11:29Z INF Connection established connIndex=0 location=ATL
2021-07-15T20:11:32Z INF Each HA connection's tunnel IDs: map[0:cx0nsiqs81fhrfb82pcq075kgs6cybr86v9vdv8vbcgu91y2nthg]
2021-07-15T20:11:32Z INF +-------------------------------------------------------------+
2021-07-15T20:11:32Z INF |  Your free tunnel has started! Visit it:                    |
2021-07-15T20:11:32Z INF |    https://seasonal-deck-organisms-sf.trycloudflare.com     |
2021-07-15T20:11:32Z INF +-------------------------------------------------------------+
```

- Now copy url provided by cloulflare `https://seasonal-deck-organisms-sf.trycloudflare.com`.

- For paramanent tunnel visit - https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/get-started/

#### 7. Handle Tunnel Request:
- Navigate into `/adKart/settings.py` and add few configuration.
- Find ALLOWED_HOSTS arrey and a host which provided by cloudflare like this
```bash
  ALLOWED_HOSTS = [
    "seasonal-deck-organisms-sf.trycloudflare.com", #cloudflare host name
    "localhost"
]
```
- Make sure `https://` not pasted in to this and add a comma ",".
- Find CSRF_TRUSTED_ORIGINS arrey and a url which provided by cloudflare like this

```bash
CSRF_TRUSTED_ORIGINS = [
    "https://seasonal-deck-organisms-sf.trycloudflare.com", # cloudflare url
    "http://localhost:8000"
]
```
- Make sure affter the url add a comma ","

- Now navigate into `/shop/views.py`
- Find `HOME_PAGE_URL = " # Add a home page url "`

- In side the string paste the cloudflare url and append a slash

```bash
HOME_PAGE_URL = "https://seasonal-deck-organisms-sf.trycloudflare.com/" # cloudflare url and ended with a slash 
```

#### 8. **Run the Development Server:**

   Start the server locally:

```bash
python manage.py runserver
```










## Usage

1. **Access the Website:**

   Visit `http://localhost:8000` or cloudflare url in your web browser to view and interact with ADKart.

2. **Add products** 
There no product is display in `/shop` page. To add product go `/admin` page and log in with the admin credentials. In products section add some products.

2. **Testing Payment Integration:**

   Use PayU's test credentials and sandbox environment to test payment functionality.

- some test credentials of PayU:
  - Card No. : 5123456789012346, Expiry : 05/25, CVV : 123, OTP : 123456 
  - Card No. : 4012001037141112, Expiry : 05/25, CVV : 123, OTP : 123456 
  - Card No. : 5118-7000-0000-0003, Expiry : 05/25, CVV : 123, OTP : 123456 

For more credentials Visit -  https://docs.payu.in/docs/test-cards-upi-id-and-wallets

3. **Order Update push**:

In the django admin go to `Order Updates` and add new. 
provide the order no and desc and save. Now track the order and hare new order updates are available.

4. **Important Note**: 
When a order placed few oreder updates are autometically pushed. When payment is initiate a order updates of this pushed the database. After successfull payment there are two order updates are pushed which are that payment success and order placed. If transaction are failed, in order updates also be changed to payment failed and order cancelled. 

## Convert PayU Test Environment to live

### 1. Setup Credetials like Api key and Salt:
- Navigate to `/shop/payments/payU.py`
- In `merchant_key` function replace MID and SALT to live Credetials

  ```bash
  def merchant_key():
    MID = "JPM7Fg" # merchant_key
    SALT = "TuxqAugd" # salt
    credes = {
        "key":MID,
        "salt": SALT
    }
    return credes
  ``` 
### 2. Set Production Environment
- Navigate to `/shop/templates/payu.html`
- Replace the action to `https://secure.payu.in/_payment` 

 ```bash
 <form id="frm" action="https://secure.payu.in/_payment" method="post">
      <input type="hidden" name="key" value="{{ key }}" />
      <input type="hidden" name="txnid" value="{{ txnid }}" />
      <input type="hidden" name="productinfo" value="{{ productinfo }}" />
      <input type="hidden" name="amount" value="{{ amount }}" />
      <input type="hidden" name="email" value="{{ email }}" />
      <input type="hidden" name="firstname" value="{{ firstname }}" />
      <input
        type="hidden"
        name="surl"
        value="{{ surl }}"
      />
      <input
        type="hidden"
        name="furl"
        value="{{ furl }}"
      />
      <input type="hidden" name="phone" value="{{ phone }}" />
      <input
        type="hidden"
        name="hash"
        value="{{ hash }}"
      />
    </form>
 ```

 - Now its ready to go


## Troubleshooting


- **Database Issues:** Ensure migrations have been applied and default data is loaded.
- **Payment Processing Errors:** Verify PayU credentials and Cloudflare Tunnel configuration.
## 🔗 Links
[portfolio](https://www.ayushdhar.com/)



## License

[MIT]

