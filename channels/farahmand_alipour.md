<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/EV2MqBw1UVHiVE985kcfIKpVREe4wNLiDznHDuk7drhdh2seC384itudXtYEokGSo4bL9VnDJI9MMZd8o7LpFfh0_Z0nOwUDuuME4b0yaioALblflBX7BsLnXiX6BFhs5HnWjvCX_KRAxsk6KxYzcX05PM8bIORt2RHJkmJsoTyUndNhDZCY3GM9cC97l75lSambeShB9wYfT7jeyH3vhdsYzPMLQC9dQqjkXcH8cQ_e-MCyJNGBWAHy8YqbnsfMiY4IfX8kNCuMuREbRN6dpZuGe8fTutx4YFWxcut_1TyvTEZWVcFJLb_mmKFQGDCWRxS3BjEsqVtVNlrFCCAAtw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-6411">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
وزیر جنگ آمریکا امروز با نتانیاهو (در واشنگتن) دیدار می‌کند.
نزدیکان نتانیاهو دیدار دیروز او با ترامپ را «عالی» توصیف کردند.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farahmand_alipour/6411" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6410">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :  ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farahmand_alipour/6410" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6409">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Utev5yPOd-ooKzNstrUIc-ybcjSVSKLbqLtxIVNTXGsCaTykpa6pjGrUJnzmI0HmrtPRVPFmtT-RH-9OKU2XXh5WhM8vF76AZj6IcPL1pswXHJVigtuDV-oGucR-3x5ua5V0HeYf9UOnmDYEOGtkyqLXHMTQqv5A5mmPE5g3aGaZ9na90F8Il3WXM_3o9rdyzQoWwyy4EAgxK1E8WYtpBZha_Qn9mt85M7bK9_9GUYjfYqj4g9YvYNQb0koTegOVZKap0IhVSVnzFVk3dhc5f8G8MiNEZ1prBkF5gGE1tfazxQ9VVYXmWVPbTmnAony5TXG8FtmcMRGtqgI8xA99iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436236e24c.mp4?token=Utev5yPOd-ooKzNstrUIc-ybcjSVSKLbqLtxIVNTXGsCaTykpa6pjGrUJnzmI0HmrtPRVPFmtT-RH-9OKU2XXh5WhM8vF76AZj6IcPL1pswXHJVigtuDV-oGucR-3x5ua5V0HeYf9UOnmDYEOGtkyqLXHMTQqv5A5mmPE5g3aGaZ9na90F8Il3WXM_3o9rdyzQoWwyy4EAgxK1E8WYtpBZha_Qn9mt85M7bK9_9GUYjfYqj4g9YvYNQb0koTegOVZKap0IhVSVnzFVk3dhc5f8G8MiNEZ1prBkF5gGE1tfazxQ9VVYXmWVPbTmnAony5TXG8FtmcMRGtqgI8xA99iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به حمله موشکی شب گذشته ج‌ا به پایگاه آمریکایی در اردن :
ما ایران را به‌شدت هدف قرار خواهیم داد. به‌شدت به آن‌ها حمله می‌کنیم .</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farahmand_alipour/6409" target="_blank">📅 15:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6408">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
گروه تروریستی حزب‌الله لبنان با یک پهپاد به یک خودروی نظامی اسرائیلی حمله کرد،
ارتش اسرائیل : بزودی به نقض آتش‌بس حزب‌الله پاسخ می‌دهیم.</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farahmand_alipour/6408" target="_blank">📅 15:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6407">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaa361a599.mp4?token=CKVQ6kQK5M5BnWcRlbrfk6R1Az8ACbnlCQxuOAY0Z8cvZdxOansSVJzeo-mlj5eMPiraqQ7tmWhzNQMq6hOx2wmxu98h5TnMWuaHv0axpGuy8cqGEFpGCfB5YtH__A_IRopMWltBNxvM_DHESigZxM70MaoRnS1Z_GfTupQfTcxef0_lOApDvWRGrYP5qWBuJeSjj8Qqq-RcCYBrxRZXAVbSZLCrFw6_wxQuSRq2qC40JG-mFY692MHu-SwxCb2_V2--1Kow782XLEBq2jKMPU6uJq_pzjDDRH979V_xvOM-4eiKhXFTodBavZzYYVeugK2agoSJRltbG6RJDwds8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاکسپاری اعضای حشدالشعبی در استان دیالی عراق که دیشب توسط آمریکا و عربستان مورد حمله قرار گرفتن</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6407" target="_blank">📅 15:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6406">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZDC12oBufPddG70KmZA7zjfZUPnhmKYUvV4aUS6WINeP9XbTstDi2fAL5aWRr-YoJuu9Z6TCAFJYbGBmaTQMdbB3Bp4wF5luQoxVGSLa372BO7ODr3I2QJRGPYWPbqfA7g_suaQw72TZdKtaaoDP3StWQVm3FlGBiaeO0lv8odXQUDac4f2alQ4XuSiYpteXYxwt1zPkU0c0REjBpftlfyte3n1Ow9HrXbNBDsdP7laTJoPhxF2FRnUPd36KAUBT7b29j2JfhKCGD42ar7uVaxCN35IrS0_42MMisGd9AP76SJozRS4qwJRuTHLKZaqolpmkP1rIOZHmnzGh44-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز وزیر دفاع اسرائیل برای اینکه جمهوری اسلامی رو تحقیر کنه گفت که حملات این دو سه هفته اخیر، از خاک اسرائیل انجام شده و جمهوری اسلامی
به همه کشورهای عربی حمله کرد
اما به اسرائیل حمله نکرد!
(یعنی از اسرائیل ترسید و بهش حمله نکرد در عوض بقیه رو زد)</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6406" target="_blank">📅 15:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6405">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJrw3ChXN3NCI9-ptnOcieOxVzrDApaY8cG7XHGcX80bifNNc1oCbcpsNtBAYT8WSZJguD_If1bchEoAANRUiNdgTxjjtR2nu0WusDDWjaMRRyLdKW67MQZWoaZLYlBlpB6nAxGRNCK_7buokA5LxL3ZN4aGItZS6f4CMC8Gocno_cBnr04eyi8fU--e-49hMdCXGQPfPXkiO1cShOcoO7SKLRsNKo0EIqUxdhpUkb7M5l4uVjxB6h6nVlNEJEsPnxH7WhiQnXryCGshjY4sVqJ-CNadxLGowYOQB-Q6o9slsVHWI8PeDX0ALzltigpjvOuytS72-_aAvocI0vuKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی صدر با صدور بیانیه‌ای به شدت از «سپاه»  و «شبه نظامیان افسارگریخته» انتقاد کرد که از خاک عراق به همسایه‌ها [عربستان] حمله میکنن و موجب میشن بقیه کشورها
- عربستان و آمریکا - به خاک عراق حمله کنن!
این داستان دقیقا همون وضعیتی است که سر لبنان آوردن! از خاک لبنان حمله می‌کنن به اسرائیل، این بار هم برای خونخواهی خامنه‌ای از خاک لبنان به اسرائیل حمله کردن.
ولی اونجا مسئولیت دست آقای «املاکی»  - ترامپ - نبود، اونجا اسرائیل بود و چنان درسی بهشون داد
که خونخواهی و انتقام رو فراموش کردن و «آتش بس» در لبنان شد مهم‌ترین و اولین خواسته جمهوری اسلامی!
سفیرشون رو هم از لبنان اخراج کردن!
در هر جا و هر مدلی، تحقیر بشید
خوشحال میشیم
✌🏼</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6405" target="_blank">📅 14:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
صدا و سیما: دقایقی پیش نقطه ای در نوار مرزی پیرانشهر مورد حمله هوایی آمریکا قرار گرفت.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6404" target="_blank">📅 14:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IwKb054uRCtUHTVCZZ09_lXiAeZyjTX9p8F71v8Qep6O9sqcP5xj1wSvzhkn0Lc3lkoUExRODxehDdqx01HfvnCuJcH3YJtqqQueDpv38K1wntMbCt5x3YDIlrOWgodcHuI8W8Hum2vdOjf7aJ_v6J0j4Ij2WMuQ58luQfPCZSRucYw0tf4viT9NP1lpnU_2z-eGXYS1F9zuId2oLstoCUUMU6x0a7rPW1XgaC5YzIODXVkZjc2VWrQBYwt99k6jXiuyOCeeseLT3XXw8IwdvTswjOBcj2fU6wA3iHVEH5ovUMakRoR1qTw8KVJo0-cIRwXVCsjI45xnTwshMx0f3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd7033f96.mp4?token=IwKb054uRCtUHTVCZZ09_lXiAeZyjTX9p8F71v8Qep6O9sqcP5xj1wSvzhkn0Lc3lkoUExRODxehDdqx01HfvnCuJcH3YJtqqQueDpv38K1wntMbCt5x3YDIlrOWgodcHuI8W8Hum2vdOjf7aJ_v6J0j4Ij2WMuQ58luQfPCZSRucYw0tf4viT9NP1lpnU_2z-eGXYS1F9zuId2oLstoCUUMU6x0a7rPW1XgaC5YzIODXVkZjc2VWrQBYwt99k6jXiuyOCeeseLT3XXw8IwdvTswjOBcj2fU6wA3iHVEH5ovUMakRoR1qTw8KVJo0-cIRwXVCsjI45xnTwshMx0f3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا و عربستان شب گذشته
به چندین مقر گروه تروریستی حشد الشعبی
در عراق حمله کردند و تاکنون اعلام شده که ۳۲ تن از این نیروهای وابسته به ج‌ا کشته شده‌اند!
حملات به مقرهای حشدالشعبی در ۷ استان عراق صورت گرفت بصره، کربلا، نینوا، کرکوک ،
دیالی و واسط.
در ۷۲ ساعت اخیر حشد الشعبی بیش از ۳۰ حمله پهپادی به عربستان انجام داده بود.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6403" target="_blank">📅 11:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83ac14cf04.mp4?token=edI5JjcBNI8rcSCXsj3snl3tO-j3GuiCFujTxfhw1-C5Tw4H-X9p22CMfNjyZp0dRocizdpJCgZX9KQhVm3egB6ApG9PNERLFqFO_VSke77YTUNebJvHE0vVAdEICnPhEWr7ilHpapIzLfbh51Sqs1ARoyCfErPSezQiBgBBqWwgNb6XZ2PXoBrPZCvvtiUQxz-eITRSlIsUM3qpRk_0P6z11q64oXeA3rRL3Fv0c7FR91nsRuoB8Ivx__WpZsnvhzvxkvX22neS3T6gS6VH1GSRAAkrhA8MltVyn4vJYUx8pRNpeCoalF3xBaHeJXvSozefcc_KFyD2oLOTVXfOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟  این تجمعات شبانه دست کیه که هم دولت و وزیرخارجه ازش  ناراحته و گلایه داره و هم سپاه!!   کی بهشون یاد میداد که بگن «بزن» «بزن»؟  کی موشک میزد به ۳ تا کشتی در روز و توی خبرگزاری خودش (فارس و تسنیم)  می‌نوشت…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6402" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5tsr5IzXk3jiI-qoQqo3P4SPx_vRWaDQm_DX-IZfkX5TpIJcq8vuS_cQGuQL-bVkDvfZLrzgjd8M-R5s4enJLlTPsEv0qV5grl8GN6RwVLmZ9S2FN4ykDfltQNVHHEiCFPffBUBCfoMw-qKWnFBbn1E7ED6Q1udNAsIEuZBPYULgL3uJFPIsGIRFvg1zriXsbe7H20I2Wa8In9LQ3v9XooNPQ-ABtY3cWuJF08k_RuwpiwqJd2m228GkOk2Bb8e72uKLbtiqXl4mUWWiYq88vbcUvWO0Cq--lSw4LOtN-Eey9vMbGu8Hu13jlQg_oi4BHCpvmUx9mIz6nKoXKk_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب چرا همون موقع نیومدید از تفاهم نامه دفاع کنید؟
این تجمعات شبانه دست کیه
که هم دولت و وزیرخارجه ازش
ناراحته و گلایه داره و هم سپاه!!
کی بهشون یاد میداد که بگن «بزن» «بزن»؟
کی موشک میزد به ۳ تا کشتی در روز
و توی خبرگزاری خودش (فارس و تسنیم)
می‌نوشت : «به تیر غیب» گرفتار شدن؟؟
مگه معاون سیاسی سپاه در یکی از همین تجمعات سخنرانی نکرد و نگفت
: حملات آمریکا به ما «واکنشی» است! یعنی ما اول میزنیم و آمریکا پاسخ میده.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6401" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
سپاه ساعاتی پیش از هدف قرار دادن سه کشتی که قصد عبور از تنگه هرمز را داشتند خبر داد.
همزمان با سفر نتانیاهو به آمریکا
هر روز دارند به کشتی‌ها حمله می‌کنن ولی به اوکراین میگن حمله به کشتی‌ها خلاف موازین بین‌الملل و  حقوق دریاها و آزادی کشتیرانی و … است!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6400" target="_blank">📅 09:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2jvxndXuOlDQ90AS4zSGOMX9a898jsjr8sv3dRWPhb-jHNTbppzu0wHR2u3nPPCIa2kQ13MAftcNDA5C15hlyvmWitzWY-eu5RHfFcUgM_-OrcUBVGu6QTlicHiP_ZXgZJMYGhUO4IdyB-X7PjZf2faOOJ1FEd4fJObt5xlo9hhALXC2yyvhJfUD0ik4VSFoGM8J2UDoggZ4X4qVj_UlnIDP40Y94GFlWbt62bme7hvhZEq2JH_LbPiEt2y3krTRG5u7epc2cfL3tmq3QG-7bxrQhJo7ubGcsZJqj7U2_MeDTL9sHbZXsumbwdRCtc53QSWFFSSzrXOpRVrO3-ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9aPxx-ivjmeebdwMhUPzMmBWJpkYla_Xuv6QeLWSjWSFrJE7Fwmjw9I5b1cjQ6sjBTkwoFBS5FtEj6_pHYjXXpBxX95jsrcHb1EWMdeTRcEQTkv7X9t7n0eYDRxyV1ngsecIv1Dnf9RSFCG8wU9lG4BXqRLFAJ2PEoBxp5b_sU53LzjLuR6JdV_5673tscO_RQJgqGMd-VktOu8ZCvziRkGq9tDjcsXMr6u7CdIcoenWluSpdFHKQaG--jG4mCcaRrg86CuTCz2N0XfXniMAL96cKLLPt71EgktRMnFBo3zt2VrDMhap-XfekVCdHTPvNEppxJyg0hI-rMmGSjTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtxaaGa2NHgdANT6h6NVASJI_uCrr1X6OkpWbWA_CK2TIviPIeIQi9MYYFHKuUsTXjpvk_aw3gIi3rLa0ff6Y0NNlI3wHEBrzWoHd3UsB56U2f2lp3fCxKlG4YqQCDPar43PzAd97dUIEZo68MhH8gdcYmSbef6POekZynlaY_8dhhEP_sIAPFMahunBSlhAKjFzFg4SDajTLxbimArdzwLWd5mmG3oJCoGoUd8MAgnMXjch9bVJiJH7xW_i80VfxW_1C9qg-i3j1JMo4aGqclXhmzcwLz8dGYsAnUuY8-UD_JGqKcdIBMIbgkLT2IvK2K8l3JfYr7Vmm9ped5j-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDyfFjTye7nEyMKk_CTVYaigurmUBdJjjq25DtfPE9NSbgCmj3Mctf2Cx-ExX1liX1ZKNZvEDaRerfTiaLg3o9htunliWUtKSM0-FLKk4q2BsaQfPA_ZrYz4Gr5T2fZDqXf61zJumnnWWv_dIPxdQCpD4GSD-kok-n2Ad1vnBexqc7mB5DLlM45MdpTDeCLqWF5aYx_7E-mSpY6SG12qy4oc7xj1fkZyHB8IKWm7xpu1nBBbKBObX2zWcYHU9B1S3zLqwPXzbIvvAfd2FtuPmNyHLFsSmfDnqv9GJfcrYmOU89E6arkeWWbkowcCrMIwlAaZnBe32z1SJEgK8PIJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq4FFCiSrLHABNGk-4kB30QMBZ-uszNP8idHLG2880AavKf_iydTe9v5LrH-7aMXbtUsTinNvvT-IHgIhyHOpyxsbgVcwhI9RyF6VU0DBDMqzjBzTc7OXXJYNWme_-mXideRLGGdBusb9wjnbOaLJ0NEtUjDNBLQux55aps9rr7ca4UbGUMyyzKRasT_nBpRh1plOy7Q6ZbomlpzlPy8r1GKVc-JXS6zL985Q1mOQgUgK_loHpcP86zA_VFn2DrWpgFbtqR2Q-Csc1kElIFi9z7NKWsARexoOOpqe0RpUlRNkBwUZ4qYwN7QsSQ5KCgfXP2ap70spGmpr8g5PLqO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTQhEZCUZ4qWZcT0th3x3TDgLdupWpnF63h9KEvI-llq1J0B2FLubTq7cHBD65DjpuWHZsTE3WadJg86WRU_R6Eny64I8tuMPJnpKewW5MEXp7Rm4241HiSjci8_k19RMY4vJqD_GIqYr3630gEn2dQtV0TKv75nULaPuHHSOrf5eU5-tVP-7QwQ7jaAsA0NjUplR6gULfuqLkT-YdfS50N0kPq6E3F9Zxy1i1mWeuEDspN_uJAwijN7xM5BF5-RokNzKzntgK7PwLDN2mjTC4dEDJ4zr8T0eDbYgoGgitoT5Lc0ELGJ9IE7OngdfSPKBVAUfn7oZ_kgWnUrge5sVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwipT02uG6P8hl5vwe9yOk0IBbKqvGpT7zRYYGaHm6V2pYh1SJ7DoFG4X_sn2b_zFinp3KCWjWtQI3OfbDEd3zrJWj7JwpxQMvrIUGa5xQemRKYKJgq4VuBEyMM7WEkWpLDXnhXGAgP0pgHV4cpXqZvkX0DWFWkhiW0aHcB9MIAH1528tsvWh6MQUtvXhpQTYDiNK401IyeCr4grpQEL-25FB82ay-N6djXNfuS4Ny6bZirRRGpyPF3jJ7ri-Jw4gv0zH-V8Z96T_v9IkSuHOagbOeGjBRvtUmuTnl5qB4e0tCeyauqoUEtyKSK6O7BTtxenoj18bWrPe8zJyzd-gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDKTHn3aDJKNchfCGtHpMUv5ChMrvKReB-IarW95mzLp-HE62tcTVWn-4cNo1ee7l2oBk36sRaKqlbCWYASTRmrrwiRRwVtjPy7lsU0XnF8ZUDc7ob029m2mPSKsmB2CEihMPkGIVD4gwdANUcD-QSgTWM4kGZg5Yj2un4Q-_2qsYAEdSkfvUyr-fCP0B2kWVP-Fph1wOJnKP_Gm2WK-i8XOnaIrxHRWwdte61OghVpmPDdp_72L1uk1nO5AaVLB9fFdTRx1fhRfp9NCMbnqCFQERr-uU94TQ9Pir8JvjpxwOMddKfCJsFNzKQ2LeJS-F6XRz3kH_UDh_MM7Rh1wTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cds_WYl-doejUxxQrF4Nmq6KX46UOwTujb_Kuc90dARFS9KQe-7eKqxA3Fj501MxWM7QUCxTQYqDfdUAf4hR541-ai1hBznEHksDI5FRKfDUlE4Eqwi9PGzFiCWihftdT_lpQPJZI3-1Hp5TKuqTS679DQ496mAHAtHqBp-M9rA9StFw8_pq8EF4B106DXg-ESb0rVr3Mgs88U77YhQbP1sjswwlWkG6guqIjYc8gNXWw2MbZSINl2MFGfzUqSiB8jpovZuN9C1ksYnAiHdJUVPxgWp_0e55hijlWVlZfSLje4C3Myghf7G08u_c2w6Cnk7_iKUQm8vDQ8yII8WT6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=sJlReZHoGbPYDHalIcyssPwwsNoHZn9WnQ6z1S8rzgDNkmzpa7108QZTgANwno2Uj7rKIOYT335gfqdJjWQwfWgsJV_bZyk_gG9tdO9xaQ9OAdM5Iht04d4BLl7YiA-tv8phj77Ccg_RP4qASIodi1P0RaDmTzfY5Lx3WfCl_5qYTABr-LJ0qtG4lSOLTEVz_utykvZVzMm-UmZgc3OZkr-jjfbKz1gMLoje04HDDqlk3nAflNsEuU5UKfwY5kSasRD22yypYvfuUB-5JDwoPOrdoXXok6e95R4WB9MIx8BJJA9Y_3yaJAkg6SPnXnkTrfiQLy3nsriM0Gfnh52E2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=sJlReZHoGbPYDHalIcyssPwwsNoHZn9WnQ6z1S8rzgDNkmzpa7108QZTgANwno2Uj7rKIOYT335gfqdJjWQwfWgsJV_bZyk_gG9tdO9xaQ9OAdM5Iht04d4BLl7YiA-tv8phj77Ccg_RP4qASIodi1P0RaDmTzfY5Lx3WfCl_5qYTABr-LJ0qtG4lSOLTEVz_utykvZVzMm-UmZgc3OZkr-jjfbKz1gMLoje04HDDqlk3nAflNsEuU5UKfwY5kSasRD22yypYvfuUB-5JDwoPOrdoXXok6e95R4WB9MIx8BJJA9Y_3yaJAkg6SPnXnkTrfiQLy3nsriM0Gfnh52E2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=uT_fzI_OL8mU31h-Z8kmc_L5sQaxpnTc96XvZRzc5T0d5gGi9zpXdN2iMSsuCZlBkh0RLIUl5cRgbJneFXy4rbX0fs91jE6Kd4OTbKpwSVMG_9A3clOVlWhRbtXpnljz_3ER7NzIgqe_iaBXyAZax0tHd9fh1vj1CueIY6CWTig0w69hlPCGHSo3A35NGpGa5J0COVLGiHhctgUcoh0bEcioM71yj0H0tbp8PuVArFtszCUBsbQyj80cdj0uoAqRGvUXCAB7UyuqyJmDEWqFRgLuWqWHH-Oo9mEJLcOzMh2YBuUbruhHOEAqO9YwHB7RD-R4tSJCcbKOTy9yL0DLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=uT_fzI_OL8mU31h-Z8kmc_L5sQaxpnTc96XvZRzc5T0d5gGi9zpXdN2iMSsuCZlBkh0RLIUl5cRgbJneFXy4rbX0fs91jE6Kd4OTbKpwSVMG_9A3clOVlWhRbtXpnljz_3ER7NzIgqe_iaBXyAZax0tHd9fh1vj1CueIY6CWTig0w69hlPCGHSo3A35NGpGa5J0COVLGiHhctgUcoh0bEcioM71yj0H0tbp8PuVArFtszCUBsbQyj80cdj0uoAqRGvUXCAB7UyuqyJmDEWqFRgLuWqWHH-Oo9mEJLcOzMh2YBuUbruhHOEAqO9YwHB7RD-R4tSJCcbKOTy9yL0DLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=NG3omz-9IHIm51gFggZFGH8SGtsQizKH8Aej6LWUh5ucCuDh0VUOztod41WkgJr1OK0ciiWBp9itUmRDx2hGtWseLdVGs9JSlHvSNGFhNcYA2kqGed0gLsFo0_UezIIUuyP9uC68f-YJBL5ets0TsBI_B6k3MNh2o-XnhD08Lz74ynBsm_I1RrdVGFLPXgS1p3Mr_3EPqlPLa8d5jiaVG-GPSVGTW_LoWQfKtH5bQP4U26vuPubXAjK_R0G9Y3XB4dQmFqsMv6ZpnvIVAt_CYCN-HUBCHU2byzyuwZ4vMEqYQ00h91ytiIwgG7x-eksL1YyMhIcdK826wo1mTmkNEi7hoj8uldNaA7J3LQWTkasBOXvaMQD0meFjLXoRKqYMzyKvCsSLyNKUhFDHaxzxso_8qrt3s7s3q18uzaI2q3A3xPAAgJAFpZ5hYkAgpDEDo49rcY8aeABXPlEvHT6XmzjKeXwVWy5SQCRdcJmS-FzCqenxFcbY6KGAg3L7JtL5TyvdO1wSHVEymFoqa8zZBjC1T5_7J_s11TrwLSUx51IpjW9QWzO8x_VRNFJYi4AX-FfgNTQP3GiXakvwzBhWykFkoZtYJkvIIfj8-CA1tFzWSa5lLvCuhEnSJZ-AtTZT0NCUnUhvEb4bJrzdg6mGRCD4B-Hi8AndeS87fjZnDvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=NG3omz-9IHIm51gFggZFGH8SGtsQizKH8Aej6LWUh5ucCuDh0VUOztod41WkgJr1OK0ciiWBp9itUmRDx2hGtWseLdVGs9JSlHvSNGFhNcYA2kqGed0gLsFo0_UezIIUuyP9uC68f-YJBL5ets0TsBI_B6k3MNh2o-XnhD08Lz74ynBsm_I1RrdVGFLPXgS1p3Mr_3EPqlPLa8d5jiaVG-GPSVGTW_LoWQfKtH5bQP4U26vuPubXAjK_R0G9Y3XB4dQmFqsMv6ZpnvIVAt_CYCN-HUBCHU2byzyuwZ4vMEqYQ00h91ytiIwgG7x-eksL1YyMhIcdK826wo1mTmkNEi7hoj8uldNaA7J3LQWTkasBOXvaMQD0meFjLXoRKqYMzyKvCsSLyNKUhFDHaxzxso_8qrt3s7s3q18uzaI2q3A3xPAAgJAFpZ5hYkAgpDEDo49rcY8aeABXPlEvHT6XmzjKeXwVWy5SQCRdcJmS-FzCqenxFcbY6KGAg3L7JtL5TyvdO1wSHVEymFoqa8zZBjC1T5_7J_s11TrwLSUx51IpjW9QWzO8x_VRNFJYi4AX-FfgNTQP3GiXakvwzBhWykFkoZtYJkvIIfj8-CA1tFzWSa5lLvCuhEnSJZ-AtTZT0NCUnUhvEb4bJrzdg6mGRCD4B-Hi8AndeS87fjZnDvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEKdsbRGHs8EoxCjjzDFet8-iMKHPBDLDyW6EygzZxamj9IaYXbVcG_tfWURCGbw3pOdlc4PPIG0DAyTQGmWatkrBr0mtl4wJlS7UmPw5Wrr18D7HmvlicQLS67s_KGcia52COyhr17JPvKunwQOknBqT53VCFevRgFUv4ERc3yJG-4EvM6TsDbhQKh-ewh6qAH8zLvD-dCRp8bFji82Im8ruiZdzcjm7NTdD0-2N_JHkQWmFqjsAiZi-Rwp0HgLZ9pExwxgMyhOTeVh2BHw2k6-lfo8Y6vXZPa3dE-Bz1PDZ3JSP7yxCal3HhazU-nJDJuUf_BXNcVZPeIEKD6Mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=q1uKmjN3kI8ClAOTxJ3JAMogWXn40pX7RKWTSrU38VCMSfIQQIdBqi6m6KIfFK5KLEBsZY5GRy8HgtvJ-YK4cntgEXDHlDsexvcY1VsqJ1osV5cgkbM6yxm_srJP_IniRnTBTHazLU3HFvo1idIzWk0JB6J58PDhr-gR8CWmsft9BB7w9zZuv4vZrUxxLahBjOeNqiXXuwgcqEK3OOHjIn_ahwOmqIXjSM52hzsBcJWnKO1Zd5Bt0h4hAm2J9YT2DHaPdYCtMRCVtvNE0oKpfhOOOJfnx3yLXO3AD-1KT4IFPsHQjaF7jcKO4A2UaGU2vAxhjCEhgKBbNHYlAYPOnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=q1uKmjN3kI8ClAOTxJ3JAMogWXn40pX7RKWTSrU38VCMSfIQQIdBqi6m6KIfFK5KLEBsZY5GRy8HgtvJ-YK4cntgEXDHlDsexvcY1VsqJ1osV5cgkbM6yxm_srJP_IniRnTBTHazLU3HFvo1idIzWk0JB6J58PDhr-gR8CWmsft9BB7w9zZuv4vZrUxxLahBjOeNqiXXuwgcqEK3OOHjIn_ahwOmqIXjSM52hzsBcJWnKO1Zd5Bt0h4hAm2J9YT2DHaPdYCtMRCVtvNE0oKpfhOOOJfnx3yLXO3AD-1KT4IFPsHQjaF7jcKO4A2UaGU2vAxhjCEhgKBbNHYlAYPOnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr1gZe4dd8TcS6aziHA6Zfo7cThX8AyvC6mTMfwPjvHzxdkHUnwpxiCF9VGbQ_FR1_YzHj2cE2mlKs3ddlmy_AH3IKfZ84F76fBHPmMc8eRVHkwjBF0-HHoku86za8L_q3NmljQi8yGjjSKwFXZ9doycZ7byI0XAqW5tUafhOozYN7KzjI8_y1pwneas7Gq6b3BzSoDjr3AUiVTD_h3WwEwlit06SuQ0b8znedeFYOiWdccWhckNh55GN4cSPA15SQhpY0u6935I_4sDvs2zPe_8AM6Y_92dT9oeMnIrIFYtuhgNxIVp8Ivfplmlgd1vwac8wnN-ZVxhEpcPZz0ang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJH9pKFSSqB0w2tpUvFXpkcHGrvNRIDLxdNdPRnZmWcKKfnSMJejNEUspWZzdqGbmMvovQlaWOxf4Mfki84aEyKuHE5V4r3gAit-ls_29HfVmKOaJE-4dFEfIugXAZ27S5A80q78jqnLnju060dHRW7sJpuHmmp7_zevHByXgItI-GIfjK70Ll9Odt21OR8Hpp9gQ35Xz5PVyPiSF2aeuqTYSmQQ2MY16F9GIAdxDtsT-S405x-EMtyftGMb42NhrFPhitaRM4UGztNEC6nWJ8EQZyDe3F-wR-5LzW3v4AmyyEeaSEAeDqjVCNxLz9WfQJq4HZe8gAsH7TYbfmhfmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmmuCGIc1cqdKZUS3JoVeXDecbWG5aiQEUMzDv-LqJLwh9i4YjlyWgXr9UoUhldBfNQPb40p-9cUwucQMpfjZB1Go5KdxpdZf0L6orgypwHDfB0ORzph52tIO3Po1I4PMDx4SMFbJ26tVqQGqLvbDY3PcXxx-Vr1XblMiWJysbdwXtlwsLBUBIlNHyQ6erVNYytFi9qL1r-fT4z98uu3hLqUKqyy5gBasQIjqlANU44fnkjrI3-jbURswA4Wr1_ho_VlhigKsRUcq67MrrnbTzYUlypq2zpEgTVuouP9Wvxx7nlEef16-97-BVd2sCf8k2eFh_SZFBLnQ9dbNaGUsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txULuUX64mcexZ358YU7KFMRBQelHWDHDMqZfzOXoIiOb6PXPuGq1-XK8-eeWG8f2IbqBzHwWtaUDXUZS--7KOIxsRo90zeY4dWOO9Z-I6BgIfBg5R1hgfRkOQ98guUyFOW0pq2YGX-8tK5RlVVrS094yMhetgrieMdQoDRPT2Qm3_39D-r057FCXE_oiSjkGebwF4YUngnAnxDat-4DKJzeyAb0LYV0jmFkpMnQYnZcgGMd2ygIQ_9Z91PJRF9s0mMIz07q6_2-gifJg83IJrBldoO91d6uo8STDblSyQ8mUJ-gbkBBSdfOosWBPMFtU2ftmwUw49sjieoK2GLb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnS6HRgyzL7Em2dfw9bONqwH6tuFFTcB8OfvpQthHVX3l9cyQTwgsmYUx-zVU7QCZSO3_i7Q6ykLN9WnnKao-f9oDRox_bzflqvRIGDWgj0XeI28HDk_IXlVttS1xW2QFubUS_yO4mmkHHboIq40eTaZ7622b5AfwHUp5nRBb2-LJzRqqvjDIMK_eFsl8twcBwzKQ8I4k2oZTOekAiqG4nDSddSlfnr4OxwUKCjY79PMFXx0XwZgQj6Ube9ff-WOnbtlP6aWRRE-ViaCDwOWGO10yP_Y22BS4sO4-lNlJRgyF7M-nUXAD6_FNupSu_e4E9Yxaax5wlaiGyCphjD4ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAsHd2Tx9uQWiVSn6BSsWWb09CuptmtHwqQ0NbX150FGqTYBuz06LarU7-1qI0Psdmlo7HE4VWPmb9oyH6ibFA38DNJOBVHdfPQ1kYNC1rxGt1ZioYJJEcBji2C9b_Q2lXKln7Mam0Ddr0RKIs2d5oPHvFj63KqzXyQVwjq1SJHvCeWODiCh5T9CgAwkMyCsL-p0N3b6_m10QAbk5lVnznvbY0MuIcUyXhVniIxlE8No54QvS5WnKd8DkBHHKWAZfaIMRy0YVTfgqGegd62K4j0iEXQw-AHEwTICGZ3MdI8P7xuFZo9dDgM8CRoAUwGl0nQObYEx05acAMVu-YqdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zrd5-2IsUtfLBdFvyB_C5nyRq8u0umFHLd__AUpSQYGcM_F6EdtF4Q5Gp27uaCfCCH7XGoxyEQ3SwPmhHsBXpqB3Z5ptWLkgPvE35HsmWZbDeRxonRsdOcOWJOv9MFv-9qEA1ghn5wcjL0kyhPygkqDvl2HW8DxpoQ8BY7ru5JAhJ2tzVn3tGsnc-cZMWg67AyzcDT83VYBF8zvwpxaZHtxYYndJMTqOtyyvUTdaoOKhd7GOIJMHUjN_gdmzYXKgg5UZRq2i5yhsTZifKwHRE_q3HljGX4khoOjq5n7VrtbTfQ977YdJqlVWgV6xzV9_pE2Oon3ZEtBkKCeZBkUo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdnX22hdboAds3ON2KnW9EYa4jwKsaiCv1Gql3tgD-UMHwC8AfheMG5JPoFDRmFoQwV8LIWKhlryNWGGR7D3Ia4YuW0MZ8st5H00b6Fwol7vu_mo-8uS025UVSzTrP9LIO5PlDipyf_gdL-lbuOX7oPf_bmOptsN82QoiXol5oV69OrTjPhcOO1K-nXRaeNxa9vnLMuaUpLUf1icbQFInHDDZ4RBy2mj8vZTNyUx3LO-_YMJTPJ1_v4aer_XrGa3U_JduyGYGfmGtnugCI8frPSCjZyCOlhrt11llq6NkQiQAUmxz06OM_XwZZFC6HEQlbWW-5Awrugp55q8GJ2iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BV9ktNJLccCOZk9ZnLRxtUMCjwq6__yPWoTmBInFQQjv_2eVpjl1Pe3oTLuT4IpSRFTi-1VbpiK71m3BuCsTfMhXh2UrMNv7fcQYAImeiWUWRVG74_GFkjucI6Y23HH-7MjtwPhXAndkAmIY7qPYiNWDaxw40e7VMpCvCySurPkmFmm_90lFNSo23e8NodoHgGIKtynEpoqn3FmEtBNbakzbHtolqdrOaeN8LEyB9Iox26F8aArWkj0Sc8WQTzClxNTHE8lKbAwamKrR-NF_KcRGMnKXbxKtHINJ7vKB0MqIDCdipbs0Dg46D6nZcSc0Qew82DkZNofLc452S1XQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFO4RSaBoiUeiytZT5pvloybJlgppAMgVNpibNLjpVnyA8ucTmMtPC7aDgEvh12eOhhihK_txVeJkv3xZ2cffSw73dJRZOroLasQCQD-qSXdlQvuzXNOMe_wTaAMudT2SrGRpmScgguW9kaQwi4MZc6f8r7401DqwPf-6F5QvU3qAlwMAl9dwucLP1izonf8YQWTNMW-mIiGFKiZgaw2cR3nKpvtthFFEtDxl41CM21_pMoRUMeWd78u1EqV6_m3Nj4G4y2ST0YvY_YHGnuBiCNZPQrtiR-jNdhlg52ZWHcFib9RMmgNCDi06IdrJh4_MTUdkuCow4plNSugh3ZtUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZB8ltILUOVqPyxWOr8GDqsSlvMgIOI13uXI10z-8xEwZ5pp-vhYMwgpX_jaVYbaZFMrjsiqAb5R7T1_V2eF9D_nu-2VCYskyMgelok2mCH0WsJWB6tkIqggpv0AvO6zzcqjAx0R5DFisys91m9wEWQKppMglmeL-c_K_FE3usIRFAKHFjuPs7EnyzOens8crWfzbRvUo1TdQIBFcm5DphAQ5rhpPgGjI2_KfjlkG399XXFx50NfutvaVDHscSMMqK7fwHvlNfYVt55iEBaBn5BzXu22FBK7offqc3Sry1lY4SENss8Ig5QJk54wqLW1rHjYF4YvAIHRDEqScMMrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxUITsRyfZn0bM0GX5rsaqp8zvJMozebrCMkuYnlDA70dXvtRtEcsqJFKWlYKsTQlFNoRiVFaDdBusoNIvAhySW2lDn3WR7N3srKEiM4X6iZDj_WAiXIMO0X8BdYAOkUXVHuf6DBQcNELRjKDRRqo0qTHnhD5CmN9Qcl7yOOUx93OBfYCFDiCYbUkLi-bmizmDPS9qlvH5EiSs8rv4mUa_YafD-x5XjqcYj8P9pxbSDfVd2mc463u6v3gFcEGBhsRyStd1nJwrL26k3kR087kcel--av9NSReYE_KyR4s27sE7y6wBqnmHNRrbqJKI3GBOobtPI6vtZ-JTLI3vstPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tlZx-2sNZyUsf6JJa3kdelKQIVrhJrVQkfZnCpYWNdEydf6nUTTgKx-e5stZWozO58KDnSBAl80_aeLGAzoqakR-9-EQqcPjQ6XPaNDAOUmD6q_58P68LX3DQDPL3hL0ljwN2CtWMlPsNvONIv-C7wnOjk9eFG7AbXPoVMpeV_mdxigJy9W6JPUZ87ktDSwCCoKOREXSll6qzoIRY--72B1pFPKGLCEuIa3IBZt274-6BI_SygO_I1H90I1XM1uQMAIp0yqAq-qeHsdbNGC8r5o0FNzHLjvmalYm8XwQk8grW-9MMp0nTIedhiF6xE5DOmNwvyeB9fIX2vzeFM5CVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/isEpNO3H5zYsjVGWU69j3wK92rvQR3FOzO7r4I4gQqTAXP6XiYW_eiNUjdgAAq9r3VqpOUAsJgPyQBZS8UCXIPcMyAsgWjZubnq3dXXAZXSJeBdYZhlgB30czUPQL_gwkMjswDD4UoGfN0PMAJvMYdu-uk_I4q0w6Ieegg6_cdSVY6aVrU3PFD-m8J48_bvWKXdW_7OVBvgLXkTWbHxGPax6TH8ZtQ9N4GfX0DmQoUj6XSV24HZ0uTa5EmOhYh46w_3j27WPqgRLRfthE72IbChwHh3i8KNSqKrIOwjs-T-FRqULEcN-4kwkJRG3Jn0p3fj3L2PQmdWIWJvc8wAu-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KPdjq-c26zAjfWThjBZm5bRirWMyzlJeAFsE-fHzR3aOUYf8xIGwSeYpfjYBT9qSftV6rohRJ_GDS0xtvZ2q6JCMaEUhw3E1zNYEq7GoWjHraADka4_4nLLYy6-oGKSHOUP3iaa5lIch5hzDYKZ-PXAga6sHVlJT4Mm4huFphuVB26OoR6uR4EFGOsScEj4rbTiR2QJY6yGevbXnHvxB8XIVQWeEjjbASnxrIc5AiwtR-LJE4ar_phdot6LnJHpIvFLIdYLfx16a4wHT3aTnld81FekrPUoeaG6aVS5-b4DISajIe-hMAqe1l21LWkcqsas40_MZgcsnYKCz3HhGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EA19F1Erbw795n4_AOuMRlNFoXwpo-4SHrWj9UkSJM9S02Rj-sUc5T8GeJCok2Oo8H5d7aPg0g2N8IPtMzHDN4L493713DZ0ETCDcKwy2Oqrb0FsMFlNe2tTerLgin2iXxnGJ7Q0X_6YCD6ORRpDaBzpSA-V2--j5SOTHqFW4160i9BZziPSW0AyLnPTJRQiYM7aGO6Q6V9GzKU3-F-M9t4hGMaOuKqd0fJPifql3cFX7BmgjXn9n9EUDSD3rg_Bo4fJYBGGtAVlrnpll0Ns4RFff2y_AKRZdfNPgUAAj88HqqlY_EGmOGGokvci0D49C3cZdw5MUXxssVNNrbiZNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsVBeKLrMnnMf4DVdjEg8TTYNgSuCv6ThKzpTrwuUEJS-epWKUT8shpmyZJGkes06bHAOpBRkgXpuEsE5bi9f2QVF2RwEBv2eGXIJR5p-bD4dyxoW3fKQaeNAqHPS8BxGA9vk47gXukuOtw_5fJ3L_ogR0tRu21C4YugETYd7kg2LUQAhPR6uP2MurAUYJe9XNyGL5NllAIzuaqm5xSQJ36bVWceia6K2B8R9SPKbU3LvYyDJbeDK4ScSMmGkuEQg95mh3guNhlK8JSWpPtYkxjNRomEQG8hCP0YFqcbF6S7UDdQkHMis4SLdrKyx02EslBFLqhvMn4nVD9vcnu0Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=iNGMvZML3ocNrvxJLc576L1qn9W0Igls_JqFaEY5uPfprQvGmEj4ma01hBpB3r22zeo7JpFvhbuDhcuHUPhRK98qoUZ2bNvw-ku6cexW82tkijaPpo49ppw4_u0xzICv87B_oP1JVDvoKhE1nylFWcyzy6fgmVYbweMs7hdl5MD_SrOmrvJoalHsTJ-AO1MGuhXcU_kNTo6zCx8DxxfLjep_jsRSE-pX7Uwq1YyydCdJRHrnKY6ivBiH-8_QqldJFhKdH5bEQOszyvy5jEnMLQ4-K6xcHNU_YGl-RQbhognira9XdDRS-tJdYp9ZSxzZw7o7KaiPm_Tj8magbzuJzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=iNGMvZML3ocNrvxJLc576L1qn9W0Igls_JqFaEY5uPfprQvGmEj4ma01hBpB3r22zeo7JpFvhbuDhcuHUPhRK98qoUZ2bNvw-ku6cexW82tkijaPpo49ppw4_u0xzICv87B_oP1JVDvoKhE1nylFWcyzy6fgmVYbweMs7hdl5MD_SrOmrvJoalHsTJ-AO1MGuhXcU_kNTo6zCx8DxxfLjep_jsRSE-pX7Uwq1YyydCdJRHrnKY6ivBiH-8_QqldJFhKdH5bEQOszyvy5jEnMLQ4-K6xcHNU_YGl-RQbhognira9XdDRS-tJdYp9ZSxzZw7o7KaiPm_Tj8magbzuJzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jykTh3O089JKkIEElIwOlKXCPavp12ry7Q_oUMoFcNg5XFpewf5gj2gkemsifBakwc6l2JkESGIx5HbXhIc92FasDuyNdjyKTRjpCmaKCEcvwKk2g37z59JLg5EHVLjcBzlGVbJjxg4nMLklF7vd8ONh8Fz9aODg-wJPknBMg14phYRU1NLDsDjpcQqV5bge4kUYXMgGlL5t-8I-enXfNclv6ObbWDMPWU-bCubdYZjePktVPdOiAGACCwxPf_IzKbu01BgaQ-R5UisZj4f-n6zBzTUjiNKSfCuwa2D83taCghF2p5ukFnETEhRuMRsaWxKvKvS8QcpE-UoT6_cC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRXSBaysA9FY1kssFxdLwN3kZz1IQ3YlYtgD-PN1cB19Q-QKssTjF8816Nux0t_TgRu-33CLpccw7KyT0g_3WeAsorhwy2WA7GxJWI8c_Bb0sb29-XU5l6tBBnTuu0y_BPE8FDnRIOHJC72Enrm6W3-fhNby-HHRABuw3Y7jjJWH4GvaqiFBiN9VhdMvWDedmnp5mDA7_NpKFmT2Apw4gP7he2cPczCnMcQjJqBsCcDXkKxGy-r5zaIPWB04F8kmwkvJJ13fUJeaM68wCepyE-iWR-qLUhrUpiDspenRCuldHnfuiWFOkg9SCfJG6T0VZAGdSYz5rt38hDBDsC5cAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTw7HlNq01oF0JO115H_yDfJDfazelGMq2PEoaIpFJoB48h3ZNxmMkaMmSYvrvvUPFGFEQQJ6ROXVvSgOTbLdPGhpmTiHLXKmoWWkkFqOuRXuoqUR3yK6WpOCP2iD9etHljoh-c4C8Ys3oyCotpymMD8wA1gSHqTPlDV-epTJsaSWS8oRgRnZUJYBx346dWNDQTDVsdN3XDDWDmDGZRlVSzcJjZ8_KmPhYvJokrSsvqxMDq_eOnZlTdWkorHzHSJ4eX5cg2a00FQJJHEZMq2zk5TmQ9tXkLl2ZSPQRptSf3x8umrlwSx5_6hNetIiwabEI8VwBvmS9FXkmvmv1UCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=gTbQJShegaTrTSTPtAwKNVLCobYsKnGfFC4EticNM0NSQw-3wsnInph5qouKeBaBASJqAgJxvcdGXDAgA80odne6VTEnNmyUXV2MN12fMdWkbuxjsK85W8mbCS7t8BxK7vDb8mAO8mDyH3gLx126wPV_sG5j-n1B43bhzy_B-6QHWNlv1tI8t4Dd1t9G7vllmGyBcryRzKUDobQXpSF9i4jsXuqQbyslyhvepo19DClOe4boPa0o0dKKg4HT_8NXMnmwDRoc9UOhqv0bcZyk1j3dnCR3268NYHmaZTAbX-vfTFci2sD9Oah4pZMBRNgGZzoFIv-IfDVpqrJ8KB5caA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=gTbQJShegaTrTSTPtAwKNVLCobYsKnGfFC4EticNM0NSQw-3wsnInph5qouKeBaBASJqAgJxvcdGXDAgA80odne6VTEnNmyUXV2MN12fMdWkbuxjsK85W8mbCS7t8BxK7vDb8mAO8mDyH3gLx126wPV_sG5j-n1B43bhzy_B-6QHWNlv1tI8t4Dd1t9G7vllmGyBcryRzKUDobQXpSF9i4jsXuqQbyslyhvepo19DClOe4boPa0o0dKKg4HT_8NXMnmwDRoc9UOhqv0bcZyk1j3dnCR3268NYHmaZTAbX-vfTFci2sD9Oah4pZMBRNgGZzoFIv-IfDVpqrJ8KB5caA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4KAZ0CETdEXsq4DKp6pbyvhRcQg-MArSE9rklF934SfGSl07EMpBxdt9XKhFLNzEEynzxIcJZcbwuSGkXVPFwvQR0UDTkxyMXD_zL3UR78wrZsJ25-NsxF5vSo-wWkbFywasPoWwmsmWR4-Q8f95NKoITawUSQ8l3tDmw5pS2Yz2gklMtw2-L-cRzRjTWNvz-8sCC6-V0FFOOnqU3CwWTKKf41ItB7Mfy7kqAnWVeYUPr_HEB5ekCBPwCEIjpzAXaa0A6nQeJt5y6T0MBLKMBQE9UxtUwKDtn7WTETNlEj5gnBoTQ8SE5xPp8pVAoy15x2w0hjAac1_vMlOdxyLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=H01Texd8LYuVZAQKWUB-Gx0RqgxTAQnXZ4CPXWRPsLKY7XHgcs1Q6RGlIyx6PHyMnF37er3XphghlXgyLa9ekt_ksWVq9l1mD0YrNArh09V_MYIr5BWp2_IwJK5PZhSNtaIYT77h0Z2mZjwCD6QxHfPn9eV2f2Hv0_TneaA9aLoQMYuSWJXD4FqoAdbYfZFnAUfP2cArrr_AsoFnNd1Lh3Ivf7qQRJH4_84WLPn7fW1Q4V9Y--3SWk54QwEk2cd4vLp13qQnsMj6dYmA-r--9YM0e_NDlyirK9rhMUA1bZAai4Ou6CR1kVk3vdMsQwiNlhEFKMcXxe_QTPXz4u2BHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=H01Texd8LYuVZAQKWUB-Gx0RqgxTAQnXZ4CPXWRPsLKY7XHgcs1Q6RGlIyx6PHyMnF37er3XphghlXgyLa9ekt_ksWVq9l1mD0YrNArh09V_MYIr5BWp2_IwJK5PZhSNtaIYT77h0Z2mZjwCD6QxHfPn9eV2f2Hv0_TneaA9aLoQMYuSWJXD4FqoAdbYfZFnAUfP2cArrr_AsoFnNd1Lh3Ivf7qQRJH4_84WLPn7fW1Q4V9Y--3SWk54QwEk2cd4vLp13qQnsMj6dYmA-r--9YM0e_NDlyirK9rhMUA1bZAai4Ou6CR1kVk3vdMsQwiNlhEFKMcXxe_QTPXz4u2BHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUCdZp5ER7480EsqvQ7dkCUg-3vGlJn8P5rZIL0IEs2LqbB47Eb5tceixfuIuJjd6gba-RWgp98936MQTgu-D06B0DEFMfvwJSxTQiQ5yHHyQvNZuncMfWkygGP3y8qQKWVlcA5gF01ukNe0kbvkXmEyEUlrPM0wAigysVPfLwBtuGZ8e6VdIU_C4wAo5hK2apH22xLm78dx-bjSotm3j8apjSPL1hhS2cBeht4SthjKalWCykpGGGASlGhCxmFShNmghku5clr_6TG3ZCT04VroCmnPKZc-Z4H-_qdqS6_jsMZ-3RCqLklOmfExb9VmfODaqM_Mu3qicb10xPQM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPmt54NU8heMWyUt9xJ_uf38BXskDDpgoCp6wMvqev7k6yFwafZuk9OOnxwW9u1BcsG-GuoAF7lUmXSLzDnrkagFr0mi-21yYA5458WnfjBs2qnym9E-xKx7HuA2y0PwgKYp6-1ooQG8pmfHj-94w0V1N9HEHkZMz6YG6-OKwBSF4MVTQQOjus-AxihGa1Vdg9o_mHvg-eP11JjZqZ_BzSRgdAzSHt9d1xpJLfosE3slSN6c6DSrCDaQyGqBh9lbESkOVkv8TaCV8BgOP1ArTYWi77_W41AtBM7Szmx1zDssCl804vVtVdPlqa8YOELooWIsLKXuo1bp8ojbm4gdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=AyC7q2h0ZhHRzmEos0b9NryunEk5zH20Ik9uQEpwwft3PrbRF3uKtiNpfL3tIrxX1Xtx02Ime9ovCC0XpIWzFfxLykIY7uNsYBs0ERaqmUl5f862LPuUcCV-OWpGwDdk2mZuweP8TlO8lUVd8Wub0WzTNhlIhvzgDQqXDhjY7i-cW1-wNCmeR9FMAagJ_JVqKfZ_m3RpVWqH7hRcYXuU3Fcc5Y1wOUd65cgL0AzBdT5bF94rtd0aJ5hNfjHyMzQWPmjMjxZ3zcAorGLzTEcj5lJ4mNv0UXe7wtE_gGS5DXca9CxDeKAD5MSvY97A0afIfwxOblvG2S3NG0j1DLke4JyR2U2YBIG9qnY0z_tk7dAxTHAN3cyOXotnBPZHX0rZvBUehU6EZS5X5mrdWPzHwD11ht0IKDp7wC2vzcbrV7RIb8ObLlF3EGb6AdFyDP0rWLVG8s8WcW9M-1ey9ui6ptSYhRum2_nd3_SO0G5clP3o-QyugizFYbz8_MQh3SatT3XncMq0zVDalyO8Z8QW933FnPgJssuhQeJrPqanjRgHv6bLiLto_sy907BCx-jq4mnqH5IATqpjuG5BRckfzkRb6jGDWygSxvKz5X7CUsNAmI3f6E6IAdKNK5wlKVkF-2MXK5crtllRYHJVKv1ndokq-VveiQZu0XLR1cYhvJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=AyC7q2h0ZhHRzmEos0b9NryunEk5zH20Ik9uQEpwwft3PrbRF3uKtiNpfL3tIrxX1Xtx02Ime9ovCC0XpIWzFfxLykIY7uNsYBs0ERaqmUl5f862LPuUcCV-OWpGwDdk2mZuweP8TlO8lUVd8Wub0WzTNhlIhvzgDQqXDhjY7i-cW1-wNCmeR9FMAagJ_JVqKfZ_m3RpVWqH7hRcYXuU3Fcc5Y1wOUd65cgL0AzBdT5bF94rtd0aJ5hNfjHyMzQWPmjMjxZ3zcAorGLzTEcj5lJ4mNv0UXe7wtE_gGS5DXca9CxDeKAD5MSvY97A0afIfwxOblvG2S3NG0j1DLke4JyR2U2YBIG9qnY0z_tk7dAxTHAN3cyOXotnBPZHX0rZvBUehU6EZS5X5mrdWPzHwD11ht0IKDp7wC2vzcbrV7RIb8ObLlF3EGb6AdFyDP0rWLVG8s8WcW9M-1ey9ui6ptSYhRum2_nd3_SO0G5clP3o-QyugizFYbz8_MQh3SatT3XncMq0zVDalyO8Z8QW933FnPgJssuhQeJrPqanjRgHv6bLiLto_sy907BCx-jq4mnqH5IATqpjuG5BRckfzkRb6jGDWygSxvKz5X7CUsNAmI3f6E6IAdKNK5wlKVkF-2MXK5crtllRYHJVKv1ndokq-VveiQZu0XLR1cYhvJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=rWkLgzolp1eYsumy9KQYl-U6zmfJHlqlRO6UJEu93lDms9ZJ9snjIOHPDxxe_x8IoN1HfWBgSZnIwSgSQK4ES9le62lyfhAY5PgCbD6egK9lj-0qbHm7HakU6pOfYxU8vAXeFQbQBt2RBPH5kgZA9f9M83JSm1jhTIHJYAWcmqT1JQjScCe4xWVPC0jV6YScme8fgzui0NX6OpTFjUuG5-9Vd7xTOjLqmYzuMEPWMErQAPWISW4Y6eyUP3DAThHPWtfU5SXQqrOBIDhL7TQGRUHJ3BoMPPcfkixJXGkEOfIEBnj9Us1fZ-ZudvTuJgUKmdCPUHcNJyX5QC6o6apQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=rWkLgzolp1eYsumy9KQYl-U6zmfJHlqlRO6UJEu93lDms9ZJ9snjIOHPDxxe_x8IoN1HfWBgSZnIwSgSQK4ES9le62lyfhAY5PgCbD6egK9lj-0qbHm7HakU6pOfYxU8vAXeFQbQBt2RBPH5kgZA9f9M83JSm1jhTIHJYAWcmqT1JQjScCe4xWVPC0jV6YScme8fgzui0NX6OpTFjUuG5-9Vd7xTOjLqmYzuMEPWMErQAPWISW4Y6eyUP3DAThHPWtfU5SXQqrOBIDhL7TQGRUHJ3BoMPPcfkixJXGkEOfIEBnj9Us1fZ-ZudvTuJgUKmdCPUHcNJyX5QC6o6apQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImgC_VHHZlhzipJEpoU1towxSTxve89LTO0PDE81lZ0WfTtTqWZn-CnPeof8IlVXm14mYRM9O8RECFTy-MnlOp-0vyacUzs3G5jUpBWazNANWTQy2xfeYH29eFBa1rt5e7mt1gK08skRKbGLV_uWDaKdPlfndIOOXnVevO2mX9va2uVhh3bdoO2ttSxMC1o4DfCtrNhi9Ln9lbMvdtkUiAI32kYFjqORFvsCO2eW9X_fdOxzCnbK-y7lju3s6uGLYoM9F45T7kb1Lok_0oNoyB3I_OysXuVKQmKJ52sW5EQ5HCqabHdvwkHjfnRaIWIDXEYzuKvkU_0YfTjlVZqqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=elB5y4l3mVcAZ98668JE8twT4PWXu-Bl1HkbVxomS_1BZGCSEWcrSwf0j3gFJRONKBn1AefQEf0MYn4h_QK3hPiM0zY32_003Ks-atwao0E-9aZQaczvF0hZed6FRjFKCUoo3hQbE5VYs8sU63eTd-oMgNqENuzTShqE1vJ2FK8N-GY8TX7LD6yw7aLITJ3f4TKEGCskx8KchGYdiczu9p909OXcOHgB80mCwDr2Z0Kr2N1jjVT4Y8j-2mKrN3B4yvZIYcWetssz2Jp2H6qrEv1KCVaAAh6wI0M_G6MwkawxHgI8bpf42veyUKXcIcRIJwFad_jfoXZynU3sokFxxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=elB5y4l3mVcAZ98668JE8twT4PWXu-Bl1HkbVxomS_1BZGCSEWcrSwf0j3gFJRONKBn1AefQEf0MYn4h_QK3hPiM0zY32_003Ks-atwao0E-9aZQaczvF0hZed6FRjFKCUoo3hQbE5VYs8sU63eTd-oMgNqENuzTShqE1vJ2FK8N-GY8TX7LD6yw7aLITJ3f4TKEGCskx8KchGYdiczu9p909OXcOHgB80mCwDr2Z0Kr2N1jjVT4Y8j-2mKrN3B4yvZIYcWetssz2Jp2H6qrEv1KCVaAAh6wI0M_G6MwkawxHgI8bpf42veyUKXcIcRIJwFad_jfoXZynU3sokFxxTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzPLHrb17u4BIfDZr-bRqYKvm6EMtzYyWpkn9vzDToFifMnIgZpuxLHiC7WmVGKthPS2jx_J9mMraHXnKO1qiESzruqC_a3gD4mxrotYShdsFmHAvwtauoBxkGnDjZkDhpcnSy5-mAY4B7geTefZDVd8g3ogO5QjH-v4HZSO_NuHCREvXIftK9ezyxrvBJEy1u6vb8UX32lyTLCsndJSMBKcSunQO5ChpU76O6DhU41Juj8yzN4tkqvl1RE2RGrqcrSVM2X-RXMMFlJ8S64_mdAhKbiCKKQxFGgpnBnbDZPEfKQkk4mO62yvDJfBoc-hpOgB5e_ZzdsqvLVIni6Tyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEeSGrnRQ3b2sZkDAWHxuW6966mmnhFk6ar6x7sCFuD-284eDA7hiHO9Zn-wSA_zvOxVL4NjWXXkxubhiqviZN1H4Ths7DtNiwqIPLuVwZ4eyawmU-l7Io44sqdNgqz_QJuFA2VBixAk3NH8V4Xw2Kgn5jR_wzZvjnU9b_W1cfUrMf85ukeByop7MPLYgqzBipWo7kvFpahkTeSBfR_zAnnhc7G9tK_nuMYQ_s6xbFwX4GsYb-EueiLyFPggTf7dK0q9DXF4N_QFx8nD8btZEj_8f2rDci9ckqY-lYehviJnKGGjBYIfKEZjU63ywm26KYRobPxOwXfDopbwtlJZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFQlfSHMCeoe-HjXcmneqhNx-XjulTTmXjoXppJ7v6ryWz1VVeFSCeklB_Kf-5B70lmaWNhAlxyKJRf8wffVKZMmUYfK_psp6geVxfmv9EnEDHIYVXJXMaa-3sG4-rBzPN-9Vii6kRa77RMyKfaDHpLVKTOjsSDXEvtpQLxPrrDCMd3oAHyEfWsjN6dYULvKEyG7n0enGD9HZ9pozSxv2Duem1Ts5p3P6FpDTPH2nkLaS3XzHQfyZ3lgLdM9Pjziw0RzEePqlYlZIZRnfDTtHyJeYM8Vy3FEegkVZWwwsk-eqpLaxdZd6_ENXe7a9he0kRHRp2YhL1NBRKSnR0BsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyV8QU3elyrsuo8gRih_NUEvKBZixq1_EXaPqcs0If-1Cz4YLbz1GaXmJroRl85gEulTELpt0R6JNQ1HA9f91OWFH1nhdoKzUQahc_sTh0CDEwiIBrT3TuJE3epuIrKphg4f1kB_kZFbU1QRyyhYOZhym8_Gc2hMzGzFVcZRBMuNcA5qQHvlXcC_0DBdTHwDfd9_rH4ePjeXZa1noaYY-5jcKeCoRk2zcXKCtmn8NZlafxeLAxkYp-qs8_9Np0mV80q_Gk0YU-8hQNarVhzW4Ks-qAKMl9rV-jft6yYQsiVqQhPkJRfzR8G10mLAFDE4rFC4-71mVDI3DSpJnfPceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ5aoIKoNbDTiRcUv6Nbu2PI5u7e_FjQJumYS_-jCFHf8MZ5dkyNJPNV6a41xHqtDZTI7pJiBktHRrOYTt_iDXmvEpAzb7cxapZEufCVTT4WmA45zGOu7Ee_0Om_xabECw0I7MPnccFvMphDEDqVyjcxexMAH2dwwfmsh-lUcMbZWYrJraWBe0dY5YwhX5GClgolwayoQj9QGQhLyi7knXev5-l3Fk6WH307Egwi7IIJD-qVrLYv9YINpmo2F_aK3qW49EuKqj1lizb5hO4ifaRaD7xLAukrDKVyPomchGlbLgDBdXnVpNaTyrJaVDWGS0AfnOo5rIKanxLV-wUdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=rOkvr-NF-7f3uKCV8muvhm7lYu_OWDB94P0tVU-fYFv7-q45yV0p_93ZPw-uhoGOdmdnYNapGblaDqSm00fsijAEG1FiD7tiiMrtNVpyjyP4rNPH3RptjjySiH0ThVPDwbIfLWttAZ66pBGRJ84PT1NHl-W-ln5ZSihhOswuTUOQDk8GajZ9OcM3A4G3PWSs9Um8M-W1UaZgDFbp_kUHbWN_8yY4LmFI0qIoD6FTVtXy9SLsRk-wuyRZ3xBPl_Ct6cqfmRKQyq_HZMKw6PY96344Z1i6EzLnJNgDhmKB7heao026M1mT56GREb9krs49hsVwrj8tBDipffHZ2kgmig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=rOkvr-NF-7f3uKCV8muvhm7lYu_OWDB94P0tVU-fYFv7-q45yV0p_93ZPw-uhoGOdmdnYNapGblaDqSm00fsijAEG1FiD7tiiMrtNVpyjyP4rNPH3RptjjySiH0ThVPDwbIfLWttAZ66pBGRJ84PT1NHl-W-ln5ZSihhOswuTUOQDk8GajZ9OcM3A4G3PWSs9Um8M-W1UaZgDFbp_kUHbWN_8yY4LmFI0qIoD6FTVtXy9SLsRk-wuyRZ3xBPl_Ct6cqfmRKQyq_HZMKw6PY96344Z1i6EzLnJNgDhmKB7heao026M1mT56GREb9krs49hsVwrj8tBDipffHZ2kgmig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gzgyqcr87lRd-JOWVwMAxHDV6QK4mpVJ5ukJhnGEF207vkyh3JkLCLcr3DSYy50QSzkR4nOpebbeGmB_fMruAaLW2ecMys57oW7rQjMe__ApDYTohSfpUG-ufuD3E1nHVgA6Kvty37t4nyLDmAZwTbDBZrXVp7erKk7IegNEm_6TVZ-847QeIIViCB5MuC0lC5_6tITIurncZS19Levw95QCbULbnkvPQF1H5R1wgi8CxYvyxhyusXutGHQOaP4Igaa5F90SvjH4XUnjCRSVFkKt40A0UhKUGYYVtzrS-6AJXXmaozR5NKV7wFR2gyn9JVt69iVyj0UGG6pPyofQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixkSUm8VD72VShpWluSA9eu_USclahH7UZ3rfDbxDB023l_lcVpasmrh9YdhBa7mYoKa3EE8asVXzfPbE8jadL_IjKFLRGTItZwhSai9SJpPbAWkL-UYbHU2QCcmrhQTT8KG1l4ka4UEf65SEy-1K7OAPcOCY510JeWPfL0kiVTinzkd0LTwf2SNX1xKLiWtrwxuv9Tr8qmbn8f6WmSTD1ikB3J_k4nTbH6hHG2Kq2KfVcxJZf2JvFKHizyDbP5VWGf1QWXcTEYUWQ-bJDUDx9wyvO2mF9DowChjwe6YlZiREr4dikwMm8jYTFx_S3mVLVWGU7_rgQe7ustkN_fGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=q6WCkWRqE-Bj0xNW-AAhn5UBYWLJjEi9J9yvNCQLzZcEiGZ26JnBUeQOkaz_6iPRCA6dAfBlDSun0zC2ays08ceEAgNA-NNl_omn1AXpP87yGCIm2pSZ-BpjM02TmMiRggluraGYmxPsqu64cnCqoktMoJELD30t3ViI4BZLulR4d7IJjufAylEt47kXUW-q9lvgCRqHKBMDsW5D3X6MAZXSNRhjMBAGV5S8G9FYZk-fflcwIsSAaLVpa-QRB8YICwQbMM4AJaK-vlULzhWg0kmp5mbJXQZkNVk10vzEoiXqvdOjaqueTdK0hVpdVZeJcrBpuedUTyOHC9hv6JIrbS55qUWi5Yz05h2f8Hy5u_e0BbEadaGMUVtMsXM7qy0IoORHv0-e5zx4VRZkFfYER8VFaKJyJdl6rAjfNLeBRcZwiC11Vk04dbVyE3pYe9MtE6VlOL5PqOR1rB_T3Tp6mmoDZuaxNcstf7z5lmjZOfSu-SxU7F6z4EjTQEudyrx2yGZvpzt98EmPp_jiaLy641Gj6qzGGjO2d2gsUEBGknKbKR12NF2FSaC7hu3QRRGSgT6qbEooQC1RVYKFn7yTLImu9JdaYvSzqeASP5eHJbOSA2bpKVdOAikrvaCxvuOT5knLPJJgIa7FMWwTLf83QyT9VEWtXeGoRpmEnLlBNC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=q6WCkWRqE-Bj0xNW-AAhn5UBYWLJjEi9J9yvNCQLzZcEiGZ26JnBUeQOkaz_6iPRCA6dAfBlDSun0zC2ays08ceEAgNA-NNl_omn1AXpP87yGCIm2pSZ-BpjM02TmMiRggluraGYmxPsqu64cnCqoktMoJELD30t3ViI4BZLulR4d7IJjufAylEt47kXUW-q9lvgCRqHKBMDsW5D3X6MAZXSNRhjMBAGV5S8G9FYZk-fflcwIsSAaLVpa-QRB8YICwQbMM4AJaK-vlULzhWg0kmp5mbJXQZkNVk10vzEoiXqvdOjaqueTdK0hVpdVZeJcrBpuedUTyOHC9hv6JIrbS55qUWi5Yz05h2f8Hy5u_e0BbEadaGMUVtMsXM7qy0IoORHv0-e5zx4VRZkFfYER8VFaKJyJdl6rAjfNLeBRcZwiC11Vk04dbVyE3pYe9MtE6VlOL5PqOR1rB_T3Tp6mmoDZuaxNcstf7z5lmjZOfSu-SxU7F6z4EjTQEudyrx2yGZvpzt98EmPp_jiaLy641Gj6qzGGjO2d2gsUEBGknKbKR12NF2FSaC7hu3QRRGSgT6qbEooQC1RVYKFn7yTLImu9JdaYvSzqeASP5eHJbOSA2bpKVdOAikrvaCxvuOT5knLPJJgIa7FMWwTLf83QyT9VEWtXeGoRpmEnLlBNC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=sQD5XDqtRfFpcqqR6QsUI2ocNhZDWeyWGhElwIvclAl7kKAYsN4rAiXKowK8nyumr8wskjhDFtfZRrrXcstD7MBFjskA3TUze_8jntkEcwPUnU0mD2KA4N_kkWw5FMcJz-xwd5WwhP-3XS7XLB9_K3r12N7kHUxqql_k9AXkgIArEb70b_c0ntPAo0gDmecR_iraixRylebI9gzsSaMiUgG8nA-QSrgBbfdQrJFwbZ9qHCICS1RQ7QmAuaikP-nb7-GC7VYp1y5DRwv69l4hrwzhyGjR2AwlSMe79_rbd88DbtUHeXZMM_5xLnIKlXLLSnXbi0onBFYDpk-LWYvZgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=sQD5XDqtRfFpcqqR6QsUI2ocNhZDWeyWGhElwIvclAl7kKAYsN4rAiXKowK8nyumr8wskjhDFtfZRrrXcstD7MBFjskA3TUze_8jntkEcwPUnU0mD2KA4N_kkWw5FMcJz-xwd5WwhP-3XS7XLB9_K3r12N7kHUxqql_k9AXkgIArEb70b_c0ntPAo0gDmecR_iraixRylebI9gzsSaMiUgG8nA-QSrgBbfdQrJFwbZ9qHCICS1RQ7QmAuaikP-nb7-GC7VYp1y5DRwv69l4hrwzhyGjR2AwlSMe79_rbd88DbtUHeXZMM_5xLnIKlXLLSnXbi0onBFYDpk-LWYvZgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCkkhSVBx_UnCyEnsGw21wHZ0FtUgK7KHwjSZDMbehVUKq9LI18wldXEhi741boj2KU60s-fArsZ70y9MIS6J-PhRU-G2UUg3EZF3hSti7VOxhlGhfkFdpBWFAUBnfiK2LZlA0_GIRxeNlGfuZucb7FnWecaHMbzXG_kqGHKs3YUD1f5KAHzj5NvZWReHDE2rXLAWNJaUOj84_9n6W_TpRDRN1Lx2-TArkwkAqlu_bb_IS4T4mXRU2p4rzmdu7CXitg1jXkqfXwoxjsY_8K3tIp7HDBKvVHEldgWXS3BaddP9m47zO_8pNltHiFG23Lo0Px5Yoducxk0O1Y8aZ9vJ-NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCkkhSVBx_UnCyEnsGw21wHZ0FtUgK7KHwjSZDMbehVUKq9LI18wldXEhi741boj2KU60s-fArsZ70y9MIS6J-PhRU-G2UUg3EZF3hSti7VOxhlGhfkFdpBWFAUBnfiK2LZlA0_GIRxeNlGfuZucb7FnWecaHMbzXG_kqGHKs3YUD1f5KAHzj5NvZWReHDE2rXLAWNJaUOj84_9n6W_TpRDRN1Lx2-TArkwkAqlu_bb_IS4T4mXRU2p4rzmdu7CXitg1jXkqfXwoxjsY_8K3tIp7HDBKvVHEldgWXS3BaddP9m47zO_8pNltHiFG23Lo0Px5Yoducxk0O1Y8aZ9vJ-NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4HMN-J2m7yGLffm9n3XdK2xM1bU8xNpPapEJ3Lb-fEi5t6N6vfG6IuE0urV8q5OapT-Xn8yFHpCphLUonjLevQ3A8pXqyi4u9YJ9ULsgAESse85_I2TIpFge2XoL7x9PgjI1KkWNIitlvlO3SexgCZBggEPUDbGeJ8OdlgaAPW6iW9ij_gAGyga5Oi4P2xV5Z7BCeP4y3mPAhJCPAyPeaV4U3LbeGclejwDHQsuPizSXcMlfJFOTWo3OgtXvjTZVOHhJvbANYA-7MHaN8xKqQ0W_FCEUwczq5kAHa3kAiRq7p_9pkFzOt-3xPZkjjRDHXU_bjz6ztjEviOWUMm_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaYrGI4_E5vcKTejHdOfqa5Vrh4B9mgbn8A3VbHXk9HBtHXOEeFweCgGsDhIm-tYa8qIUn0kDQSfX-Vnr492ozRi-rgwEbQuRqRVDLIgzNqWgaLrGNT3AOFdaGG3UFgiAuJjvTDmrSu60G5RGAkEqDabX5knn0u2tndgxlCO4EVPEm6GKXlRgr8edVeit9RQ_lWbn-xRKyLzZ_sEuMYfT1FQS4lgb3gkKBcAwIrBerErFx3G6FhJVGEkhS62T7-nZoL39p__ypGcCbtgmgYcDwbALtoRJEKsePJHyVsw3EQQf7s6wCCKl88ucJ6bUUItxGCHhRE8k-UDjoew2c-VLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UduoQzQm5VFMIxYG1UrWbDfJ-Qr8bGvZ9icqDkreaFrWS4SLG_Bsb6aljDbMmOxt1SEhukpUjRLU4rn6dsvGs5GnddWD9ZPH3zN_c6oxaLCUFMG0vZWnzGr1W_a-1IZSBWyLLjlcFiE5vktXD4Bl4YzcxXgr9ZuuGSwanmp4ixuNLoaN2FJUYrD_uNtRipTeXpzulK6EbrHOHX22iUX3DMFtOAFJRZy52utVtsSsR1Htpd6uwCKrl0gYTPl-gnBVGvAwbyQGNRNHSK0RbRCFCOlYRiWGND8PsexEXn9CoFCEIUQsL4pf2r10oVyfm85DmpMXmasMVmj_lWP6edgXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=Bhs9hJsnPYcbtjscDOJoz2IE0r32CHBWFnDilj3S0PyDSSgZYBLiQmpiBIZhaVza1hiU7J-lbeTmY1cZh5kIrjGzXcKqZROStbwlDIBViMf1MrMRCCcxk41tgxKzGiIHdtgqwkbYmK1oM9qwoKjZ_Nl3SkHVx9BX7WiKWjFXuI1VHTR7BllKU8cURE_lpADsNILXhh_3RKfXliMK8vFSxlZx_PzRlkBtHYY1tMH2iLIqnY7ekiFOcvPiQ04tD5V8Vwma3Twe1Ax2iyDk6jYeIfUOSGEIMVuhBU9dPLvw4fUP7pI00T3mzjSDfa9phLwCfmVcQ2__26Yu5z8TbArQeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=Bhs9hJsnPYcbtjscDOJoz2IE0r32CHBWFnDilj3S0PyDSSgZYBLiQmpiBIZhaVza1hiU7J-lbeTmY1cZh5kIrjGzXcKqZROStbwlDIBViMf1MrMRCCcxk41tgxKzGiIHdtgqwkbYmK1oM9qwoKjZ_Nl3SkHVx9BX7WiKWjFXuI1VHTR7BllKU8cURE_lpADsNILXhh_3RKfXliMK8vFSxlZx_PzRlkBtHYY1tMH2iLIqnY7ekiFOcvPiQ04tD5V8Vwma3Twe1Ax2iyDk6jYeIfUOSGEIMVuhBU9dPLvw4fUP7pI00T3mzjSDfa9phLwCfmVcQ2__26Yu5z8TbArQeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wANO0YpNrZQKCbgMY5-C0BU9dLS-jes69o4DfVzdMUKcpOJP5wyZPfmsfXskuRueOixoXlaq6lZlAHJvLVeReWn-WuJ2xz0Q27fSsMtZ0s1-79EugYzLPkcZENQ3asofXHOYOCQgFU63soqYzEPN_dNOTrvpmSp-T70nCl20nqO3Q8vS9oEg8A5sgTejTsXLnS9lTSGsv2e2EFDr1UocH0PaMFldl952h2a0Qjk8liyKS_iatfn0p3-PTT9G07Xvv_Zr8YyR3IEH2QuIPl2uY8C77CNWhjZwNbEC0QN1hwoV5EJOuzgHyc0L2tFHsDghBj5C68TG5MLYAswwcrvz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tK3JEOKmP4yE9il8ygwB7XKPtVnwOF0hteOOhRx6pVrDJECREbObLfilJQCTxlth6IWPJ9uRYprpWt5JiFxBiFvVuBE6P8-dERxQznbwAkJ60RYtOhRAEjrSoUbjsFJrl1h_YRDr_-Dq2FkmOO8KaWTLR2W3s-Fvo_lVEo1jUkAEbJRG7rtvpdAmfMg-g6pv2b3iYsT-D7tqXe1AnU18u7S5r3VYnZIunmrsrgb9yVDb7JtTxASzrvDqFA8PnN-UqZ8MyWleH0QIavOSZ7OPqPV1-sGu_JUa21YZVPCFiFrP23kvDteGhEmxHaxXJc_Ceen_XXLFy76gvUY2p0Bsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EToZ5rtB1SaEuMLao9RZytN67J_e2ght6SrOxdb3vbbkzxK7hDzkAhJD-WA05qd1ucGVoVXhSIomTBSA0LymFcGj9htmm3SYzLZl_TkvxfQEDVNyZbFlSFWy93uUSLeWux8dHG0M3DtEi_kMM6Sdi2yv_aAjOvxbAWZTfd2nry-yl_HOu-XE0U_JHXYzwWcArOkt38B5Z8sg3jiJCHwG343GvrhaQWVt0xms43ZpKqTM5taXwbO2K5oNvAQFwY-_Jy1eFGoGeNLxjE5JUdxzZ3BaxJXmYJrjRHKi7AALzTNJNTbZBGZx9iMe8edjANvdE-Kd9bQrT7EBjAUBZHbblw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FChKwr_G4c_J4Lii12CaP9ybhIBTxosecHXlWDFlCCCpnhcZlJadE3cRNkKc1bpe_jboY2OGTz_DAe3euErLLcG7EwIZJXyx2_8b1nHP1QuxQNIgKBqw3iWIu8Mym_f-Zey1ao6foATPu3WHRHzOKRldF3_c_Zo32cROdyyf8om7qoY2ZBrmngKnMsz6IcE0AQJsvvp1mH5ybT6eq3Df1YrB2iMgoqJEl-1QvHbm-AkeMentNuqwAzqT2AfcmPC64I6Y4GzyAypgQan2PzXSdffDzBSo_NFKhr3lXKjzn5oa2KRYh5tm1Cc0gKHAErW3ohFWZ3sT8zlUAoDkLPt5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=IPTDKadzi0WMwbPhhT95XPxsHNBJIBgXdFX6-WItqWnBkvF_byCKYn55F4bEjdZOo__J7NnhUycMW9an9BHq_1hfbthJUxwf0Q-twGPigskwMrpXx8aw05wLjyakbnGtMLFvRvTD_1UPnLFMpD1AjsJxiciiusbiIrBAEkVSap2VN0vt5nOfzRcqgTc2Cbg6gLZFHpr-UaMORfQY1Yu2RtPZFLWcnuPC4f2pr2dWYFYQFMHFuKMbpU8MKNfslAMxCSN52B8vFqojSe1_D_GpuF3UQjnoQKXnKfDWpHRBoC6Mb-cZ2__5DxMJx2onDdP_S-2_il18vFec0EclYasBdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=IPTDKadzi0WMwbPhhT95XPxsHNBJIBgXdFX6-WItqWnBkvF_byCKYn55F4bEjdZOo__J7NnhUycMW9an9BHq_1hfbthJUxwf0Q-twGPigskwMrpXx8aw05wLjyakbnGtMLFvRvTD_1UPnLFMpD1AjsJxiciiusbiIrBAEkVSap2VN0vt5nOfzRcqgTc2Cbg6gLZFHpr-UaMORfQY1Yu2RtPZFLWcnuPC4f2pr2dWYFYQFMHFuKMbpU8MKNfslAMxCSN52B8vFqojSe1_D_GpuF3UQjnoQKXnKfDWpHRBoC6Mb-cZ2__5DxMJx2onDdP_S-2_il18vFec0EclYasBdzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Ly3JI4PQ_2RhoW5xyGLbgzq35xvokHP19Q8MEFMh2WUICmm_qmWvRadqhPfOggHma1VkTSLkIQ-xaciNJb8Ud6GT-5fVe0RYBL_FvbFdYaFkgkOYtEP7VTLKxVaJjXjLnclt7KcddZHh3_SVoUxtcFX9htxRake5f0ZQoZmF2TN1gPGVfTBFd2_pG5s5YgcdUm4_NBEAm5xQl9sNGZFMzCB2vPPKG7MHpFhcsoJWrrtKIWvdcP5gEBTeKuA8YXOD2jw9d90OFQBVdpLffP2LUhmNsV41myLyLnnr5wr5b-NOJmVnUOwFAzTOE6cxCNOccjlhjWe0SU0emdsKPiZuKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=Ly3JI4PQ_2RhoW5xyGLbgzq35xvokHP19Q8MEFMh2WUICmm_qmWvRadqhPfOggHma1VkTSLkIQ-xaciNJb8Ud6GT-5fVe0RYBL_FvbFdYaFkgkOYtEP7VTLKxVaJjXjLnclt7KcddZHh3_SVoUxtcFX9htxRake5f0ZQoZmF2TN1gPGVfTBFd2_pG5s5YgcdUm4_NBEAm5xQl9sNGZFMzCB2vPPKG7MHpFhcsoJWrrtKIWvdcP5gEBTeKuA8YXOD2jw9d90OFQBVdpLffP2LUhmNsV41myLyLnnr5wr5b-NOJmVnUOwFAzTOE6cxCNOccjlhjWe0SU0emdsKPiZuKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=WtKIPBN8tt4RJhcir_NEa62jAOWE_oDbMfKgwiZbArrgw0b5oMz43gkrAzcJYiITZrH8XKzPXHHuzU6ikTutskiPitSYpJWLJwiHb6K2x5AY2WMODzPSLBTS01vAo1PAYB7EV0aB6jfUqS_9w2jpcXiPDtjut5bIRP3wVTWEVWfzYQTv_mu2Dp5D_Yu01xUwBKlkDJYuuibeSKbUat3ShIXAbkBT3SUexaCivzPWy5LseEfvybvWcyStiKItG6bwTQYC0gfJcuILGU6Zuxo41D6HP8yJuC6A7arQYqsEkItOkWF554VV4a175ZXQYdGmSEMF2kLBurChHC_t_8nhdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=WtKIPBN8tt4RJhcir_NEa62jAOWE_oDbMfKgwiZbArrgw0b5oMz43gkrAzcJYiITZrH8XKzPXHHuzU6ikTutskiPitSYpJWLJwiHb6K2x5AY2WMODzPSLBTS01vAo1PAYB7EV0aB6jfUqS_9w2jpcXiPDtjut5bIRP3wVTWEVWfzYQTv_mu2Dp5D_Yu01xUwBKlkDJYuuibeSKbUat3ShIXAbkBT3SUexaCivzPWy5LseEfvybvWcyStiKItG6bwTQYC0gfJcuILGU6Zuxo41D6HP8yJuC6A7arQYqsEkItOkWF554VV4a175ZXQYdGmSEMF2kLBurChHC_t_8nhdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANp5pb7Ju5nRjZ63CAZw3EkWs-KoQ7XzqgHX8-uFA-o_ZXkPczJcVis1p1_UPvISGKrJFvzZkRlSE_tDSf5Km2C30jmdAvEvSrF3rpFS6Xj8aUNk5WMYxI27X3G866VvtyzXAQGk9GJEeBXLegVM3kt-tHKmNYNUu2LaSPjg-1Fe6_7_oCAItvd8OxZUkpZtNJ1E5uuRmB-Pl92Bzhzw0E7BmRhbwxm83rEjX7jNp_lDGqydXbZpLakgKCdD9L_46UpBX9zMM-FfbdIreGlfJKmoNnIkZrorpNbvy8MsuaCt5dzZJwVhDzN985ZhW2hG__gly-2cZ-lDSMT6k29Sog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=SHEzNybSaV54zgNl_JN5KcMh5u9vHPQb1rffDDLCvjOK1J3BNObZNiO5lABvMgZ_GV4iby5YqRVW0goTUdK79MaJHuDzRdTWzFzaOUrwpzG2c0McLjWK0a7dQOaZxy5tTbUFzobw2CcMEsZ9V_qFzlVjVa1A0pPX_ILlklPoedVhT8EMUFbEpZwgUKx7B1qlggFaEuEhx_ud9ajQ2VlQT7Z3jbQhbf3ACEKZfVpCXloIlAVuGJfgSFI7f3ZZxEiPcntoerfbXnIk3T-0oxCpJYLal7i3CZWYZJladSKEnJsNI2GrKFZDYx3KZSMrqLA1tR2xH9vA9fxRm33qmhduqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=SHEzNybSaV54zgNl_JN5KcMh5u9vHPQb1rffDDLCvjOK1J3BNObZNiO5lABvMgZ_GV4iby5YqRVW0goTUdK79MaJHuDzRdTWzFzaOUrwpzG2c0McLjWK0a7dQOaZxy5tTbUFzobw2CcMEsZ9V_qFzlVjVa1A0pPX_ILlklPoedVhT8EMUFbEpZwgUKx7B1qlggFaEuEhx_ud9ajQ2VlQT7Z3jbQhbf3ACEKZfVpCXloIlAVuGJfgSFI7f3ZZxEiPcntoerfbXnIk3T-0oxCpJYLal7i3CZWYZJladSKEnJsNI2GrKFZDYx3KZSMrqLA1tR2xH9vA9fxRm33qmhduqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=k35wd6zW5Z9BRDSVieg-Z9Tf0K7cLqjSpWoDSMDckwKhKW0-TqsXZC-X2OtnzZa2p4OCYNNeOKoe0ypPSTeeqoUmMVNt16uuQrDnAOXqJODeeamt5igI4NF3gQKGognjhQaiGek73vR7R_sLf7y4bD90yvwRDnpMGTI5Q3HfjMp1P68XCyI9lyUu0SFMvK6sCbFdfa4uIukDSXc2smAnAJl_VsVOhg-7wc9vzJ_NPIvqxJ_oUB1RlEzDHyAls11LDORZ-MlphHGXxbrm-YnQxlK4zjmZlZsrNYh7OvMi2ePlUv_72dDu-hyiw1HNtKAW8uswqvsXsFTjTkPPREpTYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=k35wd6zW5Z9BRDSVieg-Z9Tf0K7cLqjSpWoDSMDckwKhKW0-TqsXZC-X2OtnzZa2p4OCYNNeOKoe0ypPSTeeqoUmMVNt16uuQrDnAOXqJODeeamt5igI4NF3gQKGognjhQaiGek73vR7R_sLf7y4bD90yvwRDnpMGTI5Q3HfjMp1P68XCyI9lyUu0SFMvK6sCbFdfa4uIukDSXc2smAnAJl_VsVOhg-7wc9vzJ_NPIvqxJ_oUB1RlEzDHyAls11LDORZ-MlphHGXxbrm-YnQxlK4zjmZlZsrNYh7OvMi2ePlUv_72dDu-hyiw1HNtKAW8uswqvsXsFTjTkPPREpTYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
