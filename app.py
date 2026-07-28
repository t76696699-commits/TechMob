import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Column
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/img'

db = SQLAlchemy(app)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    img_url = Column(String(255))
    color = Column(String(50))
    price = Column(Integer)
    phone = Column(String(20), default="+998949061323")
    storage = Column(String(100), default="128 GB, 256 GB, 512 GB, 1 TB")


with app.app_context():
    db.create_all()
    if not User.query.first():
        sample_phones = [
            User(name="Samsung Galaxy S10+ (Plus)",
                 img_url="https://cdn.3dnews.ru/assets/external/illustrations/2019/03/11/984021/sm.03.800.JPG",
                 color="Prism White",
                 price=150, storage="128 GB, 512 GB"),
            User(name="Samsung Galaxy note 10+ (Plus)",
                 img_url="https://superg.ru/wp-content/uploads/2019/09/P1430165.jpg",
                 color="Prism White",
                 price=150, storage="128 GB, 512 GB"),
            User(name="Samsung Galaxy S20 Ultra",
                 img_url="https://content.onliner.by/news/1400x5616/1b1ea59deef1c2dda6beed614258c22a.jpeg",
                 color="Cosmic Gray",
                 price=220, storage="128 GB, 256 GB, 512gb"),
            User(name="Samsung Galaxy note 20 Ultra",
                 img_url="https://frankfurt.apollo.olxcdn.com/v1/files/abntgyx9lnc82-UZ/image",
                 color="Cosmic Gray",
                 price=220, storage="128 GB, 256 GB, 512gb"),
            User(name="Samsung Galaxy S21 Ultra",
                 img_url="https://i.pcmag.com/imagery/reviews/060dYYYtGVk2fNOFYMRGldi-3.fit_lim.size_1050x.jpg",
                 color="Phantom Black",
                 price=310, storage="128 GB, 256 GB, 512 GB"),
            User(name="Samsung Galaxy S22 Ultra",
                 img_url="https://cdn.3dnews.ru/assets/external/illustrations/2022/03/18/1062297/sm.02.800.JPG",
                 color="Burgundy",
                 price=390, storage="128 GB, 256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy S23 Ultra",
                 img_url="https://cdn.mos.cms.futurecdn.net/a6WGxh7TLoRUw2wGntMTdM-1200-80.jpeg", color="Green",
                 price=480,
                 storage="256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy S24 Ultra",
                 img_url="https://www.lbtechreviews.com/wp-content/uploads/sites/3/2024/02/SamsungGalaxyS24Ultra_TOP-1080x608.jpeg",
                 color="Titanium Gray",
                 price=590, storage="256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy S25 Ultra",
                 img_url="https://static0.anpoimages.com/wordpress/wp-content/uploads/wm/2026/01/galaxy-s25-ultra-vs-iphone-16-pro-max-is-closer-than-ever-2-19-screenshot.png?w=1600&h=900&fit=crop",
                 color="Titanium Silver",
                 price=750, storage="256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy S26 Ultra",
                 img_url="https://digirpt.com/wp-content/uploads/2026/04/samsung-galaxy-s26-camera-features.webp",
                 color="Phantom Titanium",
                 price=1100, storage="256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy a80 5g",
                 img_url="https://assets.prophotos.ru/data/articles/0002/1304/175465/original.jpg",
                 color="Prism White",
                 price=150, storage="128 GB, 512 GB"),
            User(name="Apple iPhone Xs max",
                 img_url="https://mobilecity-live.s3.ap-southeast-2.amazonaws.com/wp-content/uploads/2021/03/01014422/G18-600x600.jpg",
                 color="Space Gray",
                 price=190, storage="64 GB, 256 GB"),
            User(name="Apple iPhone 11 Pro Max",
                 img_url="https://cdn.iphones.ru/wp-content/uploads/2019/11/iphone11promax-review-iphonesru-18.jpg",
                 color="Midnight Green",
                 price=300, storage="64 GB, 256 GB, 512 GB"),
            User(name="Apple iPhone 12 Pro Max",
                 img_url="https://cdn.mos.cms.futurecdn.net/kSUXaLsWD6dMQuXrSRYMKg-1200-80.jpg", color="Pacific Blue",
                 price=380, storage="128 GB, 256 GB, 512 GB"),
            User(name="Apple iPhone 13 Pro Max",
                 img_url="https://www.notebookcheck-ru.com/fileadmin/_processed_/3/1/csm_vorschau2_b3a4324106.jpg",
                 color="Sierra Blue",
                 price=530, storage="128 GB, 256 GB, 512 GB, 1 TB"),
            User(name="Apple iPhone 14 Pro Max",
                 img_url="https://i.pcmag.com/imagery/reviews/03POP0TjDjuXonJXI16Omn2-3.fit_lim.size_1050x.jpg",
                 color="Deep Purple",
                 price=610, storage="128 GB, 256 GB, 512 GB, 1 TB"),
            User(name="Apple iPhone 15 Pro Max",
                 img_url="https://www.notebookcheck-ru.com/fileadmin/Notebooks/Apple/iPhone_15_Pro_Max/Bild_Apple_iPhone_15_Pro_Max-Intro.jpg",
                 color="Natural Titanium",
                 price=750, storage="256 GB, 512 GB, 1 TB"),
            User(name="Apple iPhone 16 Pro Max",
                 img_url="https://itshaman.ru/images/23475.webp", color="Desert Titanium",
                 price=950, storage="256 GB, 512 GB, 1 TB"),
            User(name="Apple iPhone 17 Pro Max",
                 img_url="https://static0.anpoimages.com/wordpress/wp-content/uploads/wm/2025/10/iphone-17-pro-max-hand-hero.JPG?w=1600&h=900&fit=crop",
                 color="Cosmic Orange",
                 price=1300, storage="256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy A17",
                 img_url="https://media.wired.com/photos/698a7a42c46327732f7f76fd/master/w_2560%2Cc_limit/Samsung%2520Galaxy%2520A17%25205G%2520SOURCE%2520Julian%2520Chokkattu.jpg",
                 color="Light Green",
                 price=130, storage="128 GB, 256 GB"),
            User(name="Samsung Galaxy A27",
                 img_url="https://i.ytimg.com/vi/3CIb2l0phVQ/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAekoRO_1XuNHd9gXeihuUecBTYRg",
                 color="Blue Black",
                 price=170, storage="128 GB, 256 GB"),
            User(name="Samsung Galaxy A37",
                 img_url="https://www.notebookcheck.net/fileadmin//Notebooks/Samsung/Galaxy_A37_5G/sPic_Samsung_Galaxy_A37_5G-2258.jpg",
                 color="Awesome Lilac",
                 price=220, storage="128 GB, 256 GB"),
            User(name="Samsung Galaxy A57",
                 img_url="https://technoperry.com/upload/medialibrary/6ab/hrhxa9s3ml8hzvjv5kfojvw230fgv6zc/fed9ef4bc53f4f8abdd71536e8d97ee3.jpeg",
                 color="Awesome Iceblue",
                 price=280, storage="128 GB, 256 GB"),
            User(name="Samsung Galaxy Z Fold 6",
                 img_url="https://i.ytimg.com/vi/QYNTHbRWaSw/maxresdefault.jpg", color="Silver Shadow",
                 price=1100, storage="256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy Z Fold 7",
                 img_url="https://www.notebookcheck-ru.com/fileadmin/_processed_/4/8/csm_aPic_Samsung_Galaxy_Z_Fold7-0814_658fe05ccc.jpg",
                 color="Crafted Black",
                 price=1250, storage="256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy Z Fold 8",
                 img_url="https://digirpt.com/wp-content/uploads/2026/07/samsung-galaxy-z-fold8-4.webp",
                 color="Phantom Black",
                 price=1400, storage="256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy Z Fold 8 ultra",
                 img_url="https://cdn.3dnews.ru/assets/external/illustrations/2026/07/21/1145479/01.jpg",
                 color="Phantom Black",
                 price=1400, storage="256 GB, 512 GB, 1 TB"),
            User(name="Samsung Galaxy Z Flip 6",
                 img_url="https://static0.anpoimages.com/wordpress/wp-content/uploads/wm/2024/07/samsung-galaxy-z-flip-6-review-photos-21-1.jpg?w=1600&h=900&fit=crop",
                 color="Yellow",
                 price=650, storage="256 GB, 512 GB"),
            User(name="Samsung Galaxy Z Flip 7",
                 img_url="https://sm.pcmag.com/pcmag_me/review/s/samsung-ga/samsung-galaxy-z-flip-7_kkdv.jpg",
                 color="Mint", price=750,
                 storage="256 GB, 512 GB"),
            User(name="Samsung Galaxy Z Flip 8",
                 img_url="https://www.cnet.com/wp-content/uploads/sites/2/Samsung-Galaxy-Z-Flip-8-Joseph-Maldonado-CNET.jpg",
                 color="Blue", price=850,
                 storage="256 GB, 512 GB")
        ]
        db.session.add_all(sample_phones)
        db.session.commit()


@app.route('/')
def home():
    q = request.args.get('q')
    if q:
        users = User.query.filter(User.name.ilike(f"%{q}%")).all()
    else:
        users = User.query.all()
    return render_template('index.html', users=users, q=q)


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = User.query.get_or_404(product_id)
    storages = [s.strip() for s in product.storage.split(',')] if product.storage else ["128 GB"]
    return render_template('detail.html', product=product, storages=storages)


@app.route('/search')
def search():
    q = request.args.get('q', '')
    if q:
        users = User.query.filter(
            (User.name.ilike(f"%{q}%")) |
            (User.price.ilike(f"%{q}%"))
        ).all()
    else:
        users = User.query.all()

    data = []
    for u in users:
        safe_price = int(u.price) if u.price and str(u.price).isdigit() else 0
        data.append({
            "id": u.id,
            "name": u.name,
            "color": u.color,
            "price": safe_price,
            "img_url": u.img_url,
            "phone": u.phone or "+998949061323"
        })
    return jsonify(data)


@app.route('/ai-predict', methods=['POST'])
def ai_predict():
    data = request.json
    brand = data.get('brand', 'apple')
    model_name = data.get('model', 'iphone_15')
    version = data.get('version', 'standard')
    storage = int(data.get('storage', 128))
    box = data.get('box', 'yes')
    screen = data.get('screen', 'ideal')
    body = data.get('body', 'ideal')
    flaws = data.get('flaws', 'none')

    base_market_prices = {
        'iphone_x': 130, 'iphone_xs': 150, 'iphone_11': 180, 'iphone_12': 220,
        'iphone_13': 390, 'iphone_14': 450, 'iphone_15': 520, 'iphone_16': 750, 'iphone_17': 1000,
        's10': 95, 's20': 130, 's21': 160, 's22': 200, 's23': 260,
        's24': 340, 's25': 430, 's26': 530,
        'a17': 70, 'a27': 190, 'a37': 250, 'a57': 410,
        'fold6': 600, 'fold7': 720, 'fold8': 880, 'fold8 ultra': 1200,
        'flip6': 300, 'flip7': 380, 'flip8': 450
    }

    price = base_market_prices.get(model_name, 150)

    if version == 'plus':
        price += 30
    elif version == 'pro':
        price += 60
    elif version in ['pro_max', 'ultra']:
        price += 100

    brand_title = "Apple" if brand == 'apple' else "Samsung Galaxy"
    auto_name = f"{brand_title} {model_name.upper().replace('_', ' ')} {version.upper() if version != 'standard' else ''}".strip()

    if storage == 256:
        price += 40
    elif storage == 512:
        price += 90
    elif storage >= 1024:
        price += 150

    if box == 'no':
        price -= 20
    if screen == 'scratched':
        price -= 25
    elif screen == 'broken':
        price -= 70
    if body == 'minor_dents':
        price -= 15
    elif body == 'heavy_damage':
        price -= 50
    if flaws != 'none':
        price -= 40

    if price < 40:
        price = 40

    final_price = round(price)
    return jsonify({"predicted_price": final_price, "auto_name": auto_name})


@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    color = request.form.get('color')
    price = request.form.get('price')
    storage = request.form.get('storage', '128 GB, 256 GB, 512 GB')
    file = request.files.get('img')

    photo_url = 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600'
    if file and file.filename:
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        photo_url = f"/static/img/{filename}"

    new_user = User(
        name=name,
        img_url=photo_url,
        color=color,
        price=price,
        phone="+998949061323",
        storage=storage
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.json
    cart_items = data.get('cart', [])
    phone_number = data.get('phone', '')
    name = data.get('name', '')
    location = data.get('location', '')  

    print(f"Yangi buyurtma! Mijoz: {name}, Tel: {phone_number}, Manzil: {location}")
    for item in cart_items:
        print(f"- {item['name']} ({item['price']}$ x {item['quantity']})")

    return jsonify({"status": "success", "message": "Buyurtma qabul qilindi!"})


if __name__ == '__main__':
    app.run(debug=True)
