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
<img src="https://cdn1.telesco.pe/file/tvgg9PMB6BsXOejtfe5ONZI2UMBDF80KP-xNM-EbE8hkWfzMuroHZU6MJuM7i8QYJ6LRV3qzmOOjxGWsur1ZjYtl-S5iIOzT1T_f7VgRSMlg0UlNgN66SUXzZR4jiSjMyzalH3khiOOi7IT32nr_TyoX4hBVeZYoNexIbvOE0q0LedOpVKaFvRwAKOrMeU_bArLzgl1MLJ-k1r3LC5zl9qDFV8BuqlzbRMkpP9Gs1o9FynHALF5NtlwfuYKB1As95s-ICrTEsCwJz1qzyvfu-0YtHSR9oTHLcMAdTmRlz7obfX1GkJ__NShfNpd7-tQTb90gRftvVG94_xfzE2ma5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 12:13:41</div>
<hr>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BsnpJ71TRLHcS-vY4FPw1YAOA_tBcx0nQB6LYmXdQ2bJjGdYJ6oAa7fKSQ19T6c0julH1tt91XMXVpb7teJ3qj1LdMtYpo77AnqUIbrHl74Q4-bZ_xCN2_HJQg776SQw_xAjdTpBWWp7QmaNSrXi4r3x61iMPP8rK6WFEZvYp-wATkH-u7vKZ4oyir4kAcvw3lyY4tq7FQ6qeaMuoXJGDrhcxdFcne2nkkizC-lbusx4Hc-Rrz3nog4pwJCvFgPgIZzd7Oc_YygYq7aNJ2JwLcjcZRRruRX7DgeOXlgXTHDaDrd3YUujsEGwexs_S0mBn8r23O9UNAFReTkjgQc1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJBA_YhjY4jjo7e9CJWkfAdy4Y9WzYl3-4IVBnBEMV5_Kn2-bYv7JH9s6W99mMnh4xpFwRjcH2juv3njRuXpTZXKC5WIzfRAEFZdZllhAOiTOJKk0xYyLgknZ33iwHM1tGt8WOlHB-IZWSQWJZgZ0VdYHKDiNLjpxCXwZYBLZVcFN2ynV2WnUbS-f-pA8MtJUdqNVeEbWLRfq9qV9SVQb1DmEuQz0BECZ22W1v_hhTagC4GL883R5ixisQ-c4wSHjka8vXUbc30D7I6IeZeHnvf0gjfU2J8_aITKBfGS-Ch4Drrh84p6Q9IF_dy9S8e-LnHW3qjYAaKtj_zvx5nu1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZWt4pXkgU97DhKRkpfv8U6y3JtBgei4yhi3jZ6Z8V7_yNjZ7DOyX9zuvuIFnVS2xYoxP0h3rsf2X4MTCX6UKP-Uevgx4xBuQUJblN69HEeOJkSxedzFZ54EdoroYfEJk_r28OLPhlwAgedfdjo-sTvo3hVbzVZg-_MWve1Iawq2y3VvjmZMhvf71DNyAl5kXvH0O971YooL55gTWca_0mzaNYNi29q48ih5WKDh4B-KxazAYCfyRbRzRHn0L0z8_xAkxOPu9uSB4Og3vhBz0zqosrHc9j5P5UGe_vusNC9yPhqrIalSYCC9Oj_6OrPykz1dD6vtAd2JozU007BW9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UxTzR3pyjlRiQmkOduYnAJH31j2JCmCbgY9WLCMAmZFwwWkq2crw7fdqDvja4HnC9BWuOvQedWjzpAyqL0XIgtHdE85gH97Rkdx20B5EugH12e23-9kGz9D0Ff491WtFmgVm3d2dT8C3pf12EgppAKcLDsPb6R28OPTG7O1LkHzw2WrAD1O36F70M5A4h8rc4vJIZQQsljhW1nGgHJZxB-jl3D-hYJTmPmioEJwFK-JN7RL1dTQ4PKFtJ2_CPqKA3ZNOKbfLaIG-rKjeWrVUZQNl-0ecRJeCqJFtm88a6ot5o9EYxR-oTq3rIoTkhYeglVOxhGNk1S1yQGpzWov4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=pSZwGvd4Xf1kx9g1EDDLCCQCXO0XK0iHdKGfaeq7_ctFPQ8471T8DNoDifXYVm7PVXlHLTKWa1wmDbubmPwt7fheEhsFmPwg3AeokNawpHBnucoyQehao6CHGaHxYIxcixpeRZKGxNXI3NNuvxGgqL8KxQrZDDL9tX7Vt6E6lRSd6rgk3-HuWXI4pEgcZt9VGLI61c5S902eFuRIPaVVUXBKoH3J41BcrrVbcqPQYV_F1BoImDn5Zc_dWGDZ_UsbKFuO-DlkUVwGrNtM-Xd7wQTNobj6MBCq_UR2hAVtDJSU77kr6QkB9tLxc1rg2_RLcCsTFy4CFoUq_1-mnrBHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=pSZwGvd4Xf1kx9g1EDDLCCQCXO0XK0iHdKGfaeq7_ctFPQ8471T8DNoDifXYVm7PVXlHLTKWa1wmDbubmPwt7fheEhsFmPwg3AeokNawpHBnucoyQehao6CHGaHxYIxcixpeRZKGxNXI3NNuvxGgqL8KxQrZDDL9tX7Vt6E6lRSd6rgk3-HuWXI4pEgcZt9VGLI61c5S902eFuRIPaVVUXBKoH3J41BcrrVbcqPQYV_F1BoImDn5Zc_dWGDZ_UsbKFuO-DlkUVwGrNtM-Xd7wQTNobj6MBCq_UR2hAVtDJSU77kr6QkB9tLxc1rg2_RLcCsTFy4CFoUq_1-mnrBHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/tInMDglxBSnkbmJsDkjFHBeDN8fybrpzD1PuHgDQGacL4xzsPKjcXadsdsObST9deogUtb2eP8WeuLylYb5ysJRO5qZhDkIYNNKH_ijY14jDE0iChrR2udxHYOEC9G8oYTsQN8qpqoI2dN76U-LxZdWjup8TxcsUawXHCCvP6HzMUvyrOgcazQiWI01NE_W6eaWYUJfryHd45dRnLHnNHrZG75yiaAARV8V_t4IUufORHR4C_kzJxYQ_m6Pwjc9mDTvrj3ogQR_dO9xZBp8bap61a_NLKeVYOG3aHb1f_Zq-30A0gww63hkytX4BWv1jlejWx9DZhJf76lWrNK_aVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/fM3_V7JKaq2E6LsrBS1QSiqozQDKTP2P5U4ld3EpDZ4oE8SibQ1n1ySaJ6MxNzCjOX2LseXrkMzyIUYuD2KLL68yEpCUqAVZo2FDqPVDvXvdbj5sJwt1_AVfAJTgQ5yYlcy6D6u75HBPkYoROBazc4VK9NFvyfFZffQQyRcOSeUcYiF5AE8mt5xQBEvguAsq7p97MUZ7PkETf4hLb6-KWlnaEgI5WTWZh8ROgzCwFGbcxTZwA067deiA4QPmIXeAzuK7_W33ZPlJzweQkcm1MaJKCPM-BCP_SI0BiVtuYI2E2j-xM0XMj2t6KXMuIiStQ8DTSg-A-OJM56DID_FIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/LoQ_8-R1wA7o8yBdvl8yUUk9KXLw6tC2Yj9-iQGA9A1ortSlp3u8y6Q09NkMtdTLWXuD82aQxZyhr0K_uDU6sAFXJ2GZNnSXlw9sj4MrpzzVjNBxqUizm_aTa0we8Ky_-FJvW-m_CB4_x-iq0JQcsoLj9wHXtXYCJQWOljB-U3AloBcwQeoGJ-NnGtG1ycabhCVvk731NsUAjxlNXTSLFYiwxL-J9XW7GU3oVv-FK1wZGrZ3UE9FbLHuWi7Fuy8GiPuhlALPJN5fttWAmI6DKY_d3XctUCUPOUa6D2qXaiiDMKBdnd4JzsCvWzfF__KOzemLtUStVQ6QvO-8vxkIKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T2dSlvO-zCAtACjrHpuwnOwW4xYN7I0PVp3AflhEtlK5vPM8-IKZiAY08ZBIJpvGo9jhvTGZdOjgyWDGxxJWWiuCL7XXrEdDWIyiza9ohNW0WnGZnxhnP5GJxErxb8Z47agA6neKEQfiYJbj9dwbqOKhFnQ2p21blEwCocITQ6mgvhWRfseeLbWj3ogmlovr-xtIYiur1roHFVlUzHWJvlRIst1Ouec7aNorMgXk-U0eSkDh60E8E-VXRz1BinjSwNxor4bTHbnU-KanMsqF6YFLKkrbALSQQaXETtkHY6s4BsmogGsWOrKmpA-qlMBjBvRDwurz2azVe1PmSRQD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2XMp9-fnZbKLUDYSExaSIWTdGSD0K0YYsFMF72Fyi4zQH2Q5yUCufONRcOIaqXHjTY6ycXkMD99rblq3jdhGIjBAymX7XTUgDci15KH6g_UvaZ_XFNlaon-fA14MeMVvSSeYf3cKeNCgJ-gszuktCgH9Xm32TUSPviQ3_6pBccupP0ePh53MInl7NCD3QA5AcYD40jpU-TiOkgOKkICMRnF19TCnl4nNHjPoADc2gLdSsRy4ieM8CPlqaxbLsdHCO7da1RnzKjj0MczHV82Q_RWLgGwGkIMeGp07i-ZQa9wuVoii3CD6C_8MgQG27wIckX-aE2fJ6mD58qp_gU9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_Go-JHD0u8DI1siziFHzTcbr7DFOAdhCEpGFOgO4HKyh9RPo9VPP1DlOPr7TK9sDhRPM3xTc-rY5O0kYYiIJCjtU_eWxFlKh56nBBMAf4qiw11aC8GnDCDZufzUhI9Lwce5kjN-jPIbWHR-B99BnZHQUS0Xfcz54CXOdCzgouNpDcRH5WfUUBIf6VPAhrnczijf9rYA8p3KlehChdMk3DAN23VQlQDZk6mN_fBxrqkly6BMMb1S-4kPkJ0urLRzmPpnuKqneLzJu0yYZfeuHyyN6vqb2g-Di4PqRi0koqhJXkj-ANsaVBh0t__IQgW5yv3IBmF4a4z2oDxyA6tbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sGKFbh2eAFVYfUer5nCjL_UOvy582DH3SnHz2O8jlbGQyhbjw8-YeFo4F9hUT6VRaFBRCMx6m7BBz2PWkqjrd-_RG9IbBl0l39r7u0gg9Ra6vh__DLUk6csW-mnLtgIkkt7kMAa-Y7JZqxBvgpdbSTCzKqdjJliNAJiy3MD1nXF7yGDEqBlaPWPVs9-cBbX2NcfV2NY0B5J3mnKmOrgZCYQoGdMvWunLoyB5GReSPVonUoI7nZzNuzTZ3A8OA_xyPn14O4Di1gfEEYR2KcivzQFH68H_BQJDwRSyONLoBFMaRlnhw1MOmFvsU7Ve2UUXQ7XOuYpILhOvSEwlsIRMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l7up1oXpxs-cBwZ20i9nrfY2hOjsm7qTqQL1kgzdIVanCU-1-sIc5OyyEYN38Mxb10AthTBmatydyzGdgeZGTjQrn5fUquQ-CE2DGgTCBcDn9Uj2CLEZkhcSKW3sZAT62ViuhgPFowiGSG7xNPz2lorR1JnIkttu2qsl9a20Hfg-nOGu6MVy2GeMyy93w9sYhr7wr1bfBpWaWwSne4LKhRKpub6p_VFRIOoZNcWjvGodPuDxxUbq2sJ-yy9R7x4ptvgYShAaehwOQtLKCQqZ-tsxyyVF-2sIf91-D-fUvubCMKjuy5gz910hUFhHS4oDZ7q7tR34juTyn1r5WtYBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lZvRq9XxGsq8zAkkyvZyF_Egla-dS0I0A-hCdNw0TeIYDkGZkGrL1BTBGgWXeyASzSa69e2DbNimch-hWFz1YxmiHE_46lBk-zk8SNURABG9VpIcLCCJh1080iC8cajahjK5COv5T22-H39WDZCo2ikVCSHjpVzxLjaWmrqoB3nv8ZgH-aJ669eEYp-0M0BiH03NTWrQ6fqEkjTk3j3G-yWISrnfFDbr7d7czT50lTwT1PLkxjCdZIuKS94hXPWQKxW5ag8Voly-2nFVr_Ps-PJUQgE7Yq1GvQZIAIt0-EjOJesK9vM9Y_m0TG7hImYhpLzxfLLuNSJlrNOb-OjXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=k5WWw9vplCOHiWc6L5E6pKpDWarqQE3A3ce9LE6iodewmIhv7NXxG_7ZNvqSjn5-hbOeKd600_MrpjxdcJG2ktEJV9RDe-T6YQQZzdUe3n6OVUZUBzozOjwFjDs3oa4DJE1uJnv86O85fmTu9JdHr9Flj8k6HMTwfg1oZMgGniD1P_oBYxKOOhndIyykyaB6AH1_yZVENKkFnew4FMeNSYYVGvVZc1OexI7NF29NHDNHbrc16bjEcisuvHeB2Qo2UY6JXRRpn0UikwTv0uIwyIEoJOTw_R1jb9WS24jp3SzlDy6vCeB13RprUlChelut3iSmF548BHfI6aBbCpdK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=k5WWw9vplCOHiWc6L5E6pKpDWarqQE3A3ce9LE6iodewmIhv7NXxG_7ZNvqSjn5-hbOeKd600_MrpjxdcJG2ktEJV9RDe-T6YQQZzdUe3n6OVUZUBzozOjwFjDs3oa4DJE1uJnv86O85fmTu9JdHr9Flj8k6HMTwfg1oZMgGniD1P_oBYxKOOhndIyykyaB6AH1_yZVENKkFnew4FMeNSYYVGvVZc1OexI7NF29NHDNHbrc16bjEcisuvHeB2Qo2UY6JXRRpn0UikwTv0uIwyIEoJOTw_R1jb9WS24jp3SzlDy6vCeB13RprUlChelut3iSmF548BHfI6aBbCpdK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NtTYPmSECCKy8ZFH0Mw3NyKvTr0r2iyWJtTIuAsswL3mPs3-V-yrpG5NuM1BQiWJYlw1LURBgHy15TdY7WIu5GDWCcMJeKkZ6Xu-yvJuABEmaHiMjkJBvmS2DjZoD0TfYRqmf9VI7MvvRID6sgOgAIm5Sph2E7bIPRgfXea60v_yl1J8OL5_YpE5K2P31N_A9pbtiZVFV4404L1FH5SB4aKIyTT6ctISvMJai_mMSFaq1zZsES416y6Sih3-v8kzCbULK4Ru2n-umzifutEQHw-g5ol63JuHd_H9nMv6WU5wNsef2LbjxpYXTZtINmSkZaIrU-Z3KSOcbgyRhaI6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YuEGgTaC7HC1gDwT9PdDnXJrLUoAHwKfNxtrOL_WT8gMtbm7Q2yopVla3mVuI4ft9bkJAVw-vQOSPjngY4snV-TTqAmC0OB-_AWWgd-fFr9R_zpztf_9uogiYElE1If8Qoy02faPDBDKTBGCmdXqkhsSYpGtdvbJUKq4y9SwdTrAhWjbxB26z-yIGMNe8UmGQr5rU-TyYDVOhrPpEHb_u3dN1u5qAk-DMI6umBN5bLHcs7VkUH18_Z1eLuutuBEYqjpO8Kc2LubYyhFTZpdltNZMWONoPrEVWDt9qJ7Sj_ITbTtPBDLBxUj6B4ryPLVrl19SAFZ2vLret83ZDSnrzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GeODLWtiGx5V4PhWsxptQzmcpUEm5cOS8qyS7P9xVweljcnBSZhRm6SKRpQ7HtdYuKPLqa5Dqt1VqZpnEQ8IpSJYJfiOy7VbuGZqutXmLLKzQdrIOj0wyI0QfeJwfyyrBQbU9HFp_4auyBEefO4qRW4Nc9NJKYpYza5VNG8GibQ9Cb6NUaQQZdENad91GrYFqo_Wgtlu4gGtpdHL1cpphhqGQF3e8uj1Xs3qihtGTjNLVHjstXa31k20mcYOQ0a2eyOHep2PFNhP6BO1Q179uYeeyRrqgQgbiwA5t-mWcYiN83ZwW0hbe091_SwS1Mn4UApAe4gYPXJpfOEWacErKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjhPb1GPrrClcOAktCz4jD6nfzRc4E2zL6IcBJQwDqDUkESodAyknb4FDJbUiqP_w0BPwIyZNjvx1kLPwCMvKTirC5U76shB6SGdhmm_JwWK7nu6wOz4AsHIyoll_f3G9ZKYXv0U6hMX8XH-V75LLx_LMO3WI1ByQ3cbI_YCD6nRO2RduDNBAaJqMIVx-qOC-t1ocfvJLhvUGghgJDxoK4b_AZHkY7dBjE5FU1lsaPy2PmCZddEy4FTaF_-aXlDFZ_SAV-sbwCU7DD0Ds1jfSb1x3y-ll9zj3AH98S6XthWOOGt_btgkuiDfmG3DeRmJLl7yOZvXKY2C6nDwQgsITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HRFgD0HO9R19-ldfY9oPfHJei-yg9IObDn2rHiJ47GBGa4Now8QxNKXLVd9Ej6FlCUzYzH0yjU7S4lIVqKdKGddUqgZKoP72AlZcW-wharTCwg3T6u23sdcX4MgC_xYXwyweMFslibo1z7kH62WYlwDeUVFvqVYIvY9fHig7bsj0cRfNSVTChH1sf5nFIpR2XLb13Otm9pG2_SV27WX9drwHpgycpUDlGbHXeS0R5RXx_smHnboqVB4VTDoOt-i7RJxdWT0Bb_0r8v9qOUIX1-eri3iIjlfrHCcrx31nrBE6889UuVQVX5TT9SEVKQAbiu19zDOWjqEpRGIwR7o9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UG24x9-KoDEIjXYQkbHskRJSjiqoAQ76RaX5Ql2uJ0s2sccmzl97XFbR1SNbU6yY8W0Fm5yTD72ZJalKzTsOSWf_Q4BEGveAWaX84MjWNmAtWcffkrHjOnYvHmhoUC4otE1sWw_qdd-pq1zW16H84Erf9UHurVDc9pgwLG_zxX0gQi6ZhNECuZ7ZslbJlhTADTjnIKHFcVp1q52i0-2MAdisRJoHQs8umlefSQs9SoRoqE4nvn4Dyzy6e0XEq1It5ABV9q4YN7_Rk7spGTLfDQK81amEmEYvQmgyNn_Y6RLR6gOxnT4gUVTZYRc5r1Vikeuqx2IZhi79OvekDcTuqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bPiOVx6Ih3kl7Qmz6l7O4396tPJiuOx3X2f_UMirLth8XQRvLazL_qXlCoRY2s5oKjy8tjpQ91Zgw7pp_An8NLc2e71hIKWEYoJED7wQ0p-l1gX4aW3rIrvcxr91nP-1vuwCljh-qjQWLhZv2AjFdFOl4w5ZW-qeJQ3n-E_aYf6zFHfRHYA6aKwftxHuNE2HpDpTnRNfXHNz1tlh09BtJaPRxYgUEyRbslQ1GhQt9UsDuMCj6SFzpsrLutHqj4HPMRyh2hnp-5bV1ocRU9mVBIoT-BM7fUnyZqT_b62P4OJB3Ev0GgGiP19CwAGSSmDvV-qWJQV-qR_qYUh3T363yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QOBgEquO5EAsLLUdCE1O4uA7uE2hLHHMcZLMf2qOt-WVvkRhPv5NdgD7RevQ8_QWT0VE3EsR-rn7AapjItFGY69XHuDAilOrD_eLMjD61SqDA-sLIZsw2cYl_5ilxA1vFPGJBVIggGbdGeryOpR79uVaAfDg7LinJC9K-Ewbh2ZY1QHEqpo6ey7EjxyEM_1UjjucosDPTi51_I4HfBIejyhtjpQIXf6kZuBd_JX0nsi3ZI44ZU2CC-Dd9EQ-OKqMEELVWOmpijFHTwYLqhF7ypPHgIKEA1MRrfueFiexjfspErY14GQJHSnSIaYMjJqxRQB8_Im7HkIVbutGmQxfQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PXnse9rk9wCtdIObzUftysjGrR7QWqXTja-2hEAGIW9iO-Yn39AJ3Y6UqwULcU6Srki1yOm0AvKmi0zHOWSQARFh0fcPd-8l-sqRWWyfSu-6X3G3eq-RDTEa1dM8Wf9GxBMoW0d_TX8W8jJFrnzDi-Mh8lRRFz5QgJ8CePfolYYP5oHtCwG3952FnRTABQNV8_koHFMbGznwdFs0rcQIUSN7fDSkcf2A67fr2RcMjdpwWw1-0XWQAOdYDG6x7MmNU2lgUmvRbkqPuAbH44VB5t69Jvb2olNKPWf6okoLc_8btvtAlWPF9RCkHu7iknQooiAp2dkLIouWVNFNvOygCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b6BzoasnF1-XRYGqIThCXdbgoLlZt6GFlDcAQjsrg5n1nn2y-lTcRWXAJ84gRVyEPj_q1MajgIrORcuPmRL1OQnlvrUQUUWKif3MfRLVAvqUYHDSxzO8Jwk_c9GagLnhMzITwIMmBOxqvE90CdrmTErtfuWOUXoi5FuH6SpRGrpyfUUSIwjTEeNokdtFEcFvoUn-CC3ZIwApwlH0eYUxAp_pLXPWLo2_j3B4pq_HS3rnk0x8mAeSu5BXWeNI3frNZH4jPdRr08m1Z1iHd99zoHRlReC_v_QcSTvp78Nrpi_1XHtGEkmFyAUwCk-hm624rEBACnBngMjE0s99OApFjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی GLM-5.3-Flash و ماجرای Ox Alpha
شرکت چینی
Z.ai
بالاخره مدل GLM-5.3-Flash را رسماً معرفی کرد؛ مدلی با ۳۲۰ میلیارد پارامتر (معماری ۳۲۰B-A18B)، لایسنس کاملا متن‌باز MIT، کانتکست یک میلیون توکنی و قابلیت چندوجهی (multimodal)، که به‌طور کامل روی تراشه‌های هوش مصنوعی داخلی چین اجرا می‌شود.
نکته جالب ماجرا، پیشینه‌ی این مدل است. حدود یک هفته قبل از رونمایی رسمی، یک مدل ناشناس با نام Ox Alpha به‌صورت رایگان روی پلتفرم‌هایی مثل OpenRouter ظاهر شد و به‌سرعت بین توسعه‌دهندگان وایرال شد؛ در عرض چند روز، حجم مصرف توکن آن به رقم نجومی ۴۲ تریلیون توکن در شش روز رسید و صدر جدول‌های استفاده را قبضه کرد. جامعه‌ی فنی با تحلیل نشانه‌های تکنیکال (مثل نوع توکنایزر و کدهای خطای مشخص API) به این نتیجه رسیدند که Ox Alpha احتمالاً نسخه‌ی آزمایشی همین مدل GLM است، تا اینکه بلومبرگ گزارش داد
Z.ai
این حدس را تأیید کرده و وعده‌ی انتشار رسمی وزن‌های مدل را داد. جالب است که Ox Alpha پنجمین مدل ناشناسی بود که طی شش ماه اخیر همین الگو را تکرار کرد (قبلاً Pony Alpha از GLM-5 و Hunter Alpha از Xiaomi هم به همین شکل رونمایی شده بودند).
از نظر قیمت، GLM-5.3-Flash بسیار رقابتی است: ۰.۱۵ دلار برای هر یک‌میلیون توکن ورودی، ۰.۵۰ دلار برای خروجی و ۰.۰۳ دلار برای ورودی کش‌شده. روی بنچمارک کدنویسی واقعی (Code Bench) در همه‌ی سطوح تلاش از نسخه‌ی قبلی (GLM-5.2) بهتر عمل کرده و با Claude Opus 4.8 برابری می‌کند!
از نظر معماری هم ترکیبی از MoE، Sparse Attention، Linear Attention و لایه MTP به‌کار رفته که باعث شده حافظه KV-Cache به ازای هر لایه حدود ۴.۴۴ برابر و محاسبات attention به ازای هر توکن حدود ۳ برابر کاهش پیدا کند؛
خلاصه: هوش وحشتناک بیشتر با محاسبات بسیار کمتر.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lu-noBC2OkIx5Je8QtN7IxYB8mqnQqRzNVrDJBU9Oh_c5IaePRIEk0HBnTROzZ4j1QHNo4CkDt0J559mx30lxIk8z29cwqN8Be-bg229k7_roZI2JUQlwdU0gQZWj54kIVCy6Eab0eMerGSpDgc91272Lq73LBdw7q3hfyQOcwYuZMXAscHjJLE2erYSO-S8IUIPSKWWrym3Z1ltO-ki67lEh0xjErwY0LwvnleysA5zLy-4NTRpisl2XZlPPAwSuqn4iGNF02mZ9e_YsFPhsP-35uZVmFdoZoSb9_spJr33JI1Q-Q-wI8m9lATdPCID7AO2p0i3BYUrG7OFu9KoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SAjTslB9Bz81qWwW_U3VEzU0NF_T3fB0nh0B02ilbbj-kGrQSfqkaJeQH1BMArWIZn1jNgWFSuCbtwK0nlLZDEuA0Bfuj_RSl1OQdIoeoBJgKDPcJOJbtBdQV0325zRJDrp4TuCvoUAIH046k0P5WwTBvzguqylNIQDRgzhywTQDxijqtk2ePkX-X2wTzkG5zxAyMNlKyiosO16uHrRJn_ET8AKrBTxpDhX-ko5MpNP5GXvQZMv0zc2N_GAD5q6-QWG6G74nWhEYH9t01sFlyaCDhE4LKh2VwTpvNDyHBk1D2v9TORd-w3gESVEeUleieJB8GiqMW1uIOt-Ayo_3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n9P31Pbg_BX2iVEsmWrYJDREg5w9YOAHDS2F76367FoHqIShq_zyfVS7hWHHBXZNHyTU0AjEsNwbHxKqjVzLgwCAWToN54HkgDOEAo1uJsO3pfME89sc8wWlAl47lPERYd14ga9SwXKrt78MH6s9asEdTTkjEsA_zwLkrlOF2KO0vd1UYtglxgkWl2cKaQZQOlWy5hiXAITvubQnWc39xaY0jMDv6OF6x7CiG2jahdrt3G6e-OuoXBsq3huhpuA3SOcm_v8g55IEz7dDJyzh6jJ-w87KbgqY23unbACKL6d9JrGVCK7pEbZK5oAOcqk9iMh85xgZwIpgq6WWkQ1CFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUToHdkXr7BK-0G8EWAi_ECvGSrAvKfUEMSVWfpHGqYIHceeR2Rx6_J8DsibnRQ3pVFRR999YabmEdG2ARt7MDwuGZiCu1AY6xC5AdI4G8GKIpM-_c3WytQbEF73SM1LMmCRnhdt3RDdpahLQ9ybsocPHF_CwcQStWt4Mrv9fV3vUhhdApRX6mgj_kimDA2A8mTVg2_ziK5lck5SZZ4-xnwdtxdp0Lw3WLCTt9AgY4z0i2CSCkMejcmTeyhVLTZRjQLLzgfTO52y4B57bB2NnouwAvg0f0j6-1ep1dc6QbjXY2dt3z57bjfEO_MkRo74Ul1LRtfLS0t-pRCSdXOXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AofExsdEVQxrSMMq_voIstvvQzu-4M1UibDo8PCQVKjGveP2W9Qm0vmWDV87ct6Kq7Q2A9HqQtOBEd7J27wSj_cbzXujdwF2Z1lAmboAMwy9da-irM0QrTiBkIiKmp1wRdXIb8vAN-5wuAuSzxvu1V2vt6IXaliV9sPsL4ZJEzTN5xoVz1UoRYggWVRS7L2ya7ShyeOA1PvUF8sATIKhc_etzMUcNPXNvJGNbGFn2cOT13yhn-3zxQSIVLo5ZeSL8NeQb5AETC0tyS91GxrmQWsDlA-iGWqQ22fPCZlVKZO-BCRZaBky1l5mCZezoDKdNWEfXzSw4io4uE3r4stMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha
با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.
هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha:
https://youtu.be/FIhoccZtpZQ
برای شرکت در چالش:
1- ابزار یا پروژه‌ای که ساختید رو همراه با یه توضیح کوتاه و ترجیحاً عکس/ویدئو ازش توییت کنید.
2- من رو توی توییت تگ کنید:
@MatinSenPai
3- عضو کانال اسپانسر چالش، Lira Candles باشید:
https://t.me/liracandles
من پروژه‌هایی که برام جالب باشن رو ری‌توییت می‌کنم و در نهایت از بین شرکت‌کننده‌ها ۵ پروژه برتر رو انتخاب می‌کنم.
🔥
🎁
جایزه هرکدوم از ۵ برنده: یک
شمع صدف
و
توت‌فرنگی
از Lira
🕯️
🍓
معیار انتخابم بیشتر روی خلاقیت ایده، کاربردی بودن و کیفیت چیزی که با Ox Alpha ساختید خواهد بود.
تا فردا همین ساعت می‌تونید توی چالش شرکت کنید! چون احتمالا آخرین مهلت استفاده‌ی رایگان از مدل Ox Alpha خواهد بود طبق گفته‌ی OpenCode</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QlTb_lGqsv6ZBAPrFUBVn2_1oibRXjqcbI-glZXt4bau5XXk2i-1N4rJW6vsQLgBcG6Vhk_nu3kUP6aHq4wWxDHX7L13qZIGaL3HnWvv-9MejXZ6srcrdOSIEfslIDKrwo4_lH5uZyiX0lwhEDCHmBGUYhH269ELtJ4qp2cqmYYuVT7gporD30e4iElZFGOyuyUL9iPGPQcKgsKM6eKwzgQHAJwdVE6TV5MONJO916JKT17cYxhKlN-IC0dodLapch54_o2mCB7Z95yb6gi42xaoQDjEP6rXyNKMbTimV9_LKYF1T2SlMr4S3rdCEs9WEhueQSkDlNxIeHpFnrbfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=VUBucrGGqGXl4On5hJ8hC12rlcXy1FmNo_yuvJxkYydgQ3EsffIGIHtKSJlshPmpQAKITj1tKEGYqwZe0zA8MOZSg6l7bsjkNla8Kt4lDYqmnHe-QjYve9s4rUwqA6zQVInZigF78ljfETL39fBm5vl3LkaKH8vrWkYDFVv6RCjxIF60By0cI76L4LAz0eP_9q9_jHgbKYuHld2-awFbQsVzfvqbVgxfbZtb7tKBlcQdIiiFUzjKQuA5iRmzB6qec-zAE1Tf_7gZ7Kj70-3IAkMuMqubM1QsGYXbILuI9H7Dj85mfAklWsBHotGSW7xhIYIT9yMdCmLZqM0OghKy9A0JhH1GxqTZPiDbvnu9CxcnmXMBqR9tu9UwqL2dENQb_CBZ8ju1Jl4RNw71EqvwHSSiJRCvwf473Wp0Qq0DxtOA1SvmopdsJoFQvo_8tmi2C1Aop2JzB_hWX615YnH6Ir_tGc7oK522t2JWHsa6rd67znis-pGLVy3K0sVVueaMFdMRJ-Fj-UrSTrhfYoAtzaQ-GVz8yAuYDdkVUclHqa6VYss4TwaLIMcy4udGqVxyLpVNLBcWl5KlvRFtPoBxRzVshJdEwyVJ1ZGTpRuBr4pmZnslUO6axxwHpez61xaOYbPNBix0_TTUF-wcEJAkp1aWuOCpKUwmfSal3j2SWH8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=VUBucrGGqGXl4On5hJ8hC12rlcXy1FmNo_yuvJxkYydgQ3EsffIGIHtKSJlshPmpQAKITj1tKEGYqwZe0zA8MOZSg6l7bsjkNla8Kt4lDYqmnHe-QjYve9s4rUwqA6zQVInZigF78ljfETL39fBm5vl3LkaKH8vrWkYDFVv6RCjxIF60By0cI76L4LAz0eP_9q9_jHgbKYuHld2-awFbQsVzfvqbVgxfbZtb7tKBlcQdIiiFUzjKQuA5iRmzB6qec-zAE1Tf_7gZ7Kj70-3IAkMuMqubM1QsGYXbILuI9H7Dj85mfAklWsBHotGSW7xhIYIT9yMdCmLZqM0OghKy9A0JhH1GxqTZPiDbvnu9CxcnmXMBqR9tu9UwqL2dENQb_CBZ8ju1Jl4RNw71EqvwHSSiJRCvwf473Wp0Qq0DxtOA1SvmopdsJoFQvo_8tmi2C1Aop2JzB_hWX615YnH6Ir_tGc7oK522t2JWHsa6rd67znis-pGLVy3K0sVVueaMFdMRJ-Fj-UrSTrhfYoAtzaQ-GVz8yAuYDdkVUclHqa6VYss4TwaLIMcy4udGqVxyLpVNLBcWl5KlvRFtPoBxRzVshJdEwyVJ1ZGTpRuBr4pmZnslUO6axxwHpez61xaOYbPNBix0_TTUF-wcEJAkp1aWuOCpKUwmfSal3j2SWH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نکته عجیب در تست‌های اخیر کاربران از مدل Ox Alpha دیده شده که واقعاً سؤال‌برانگیز است.
همان پرامپت روز اول، بدون حتی یک کلمه تغییر، حالا خروجی بسیار دقیق‌تر و جزئی‌تری تولید می‌کند؛ مخصوصاً در مدل‌سازی سه‌بعدی موتور Raptor که اختلاف کیفیت با خروجی قبلی کاملاً محسوس است.
اما سؤال اصلی اینجاست:
اگر پرامپت همان است و آپدیت رسمی هم اعلام نشده، این جهش کیفیت دقیقاً از کجا آمده؟
آیا مدل در سکوت روی داده‌های جدید Fine-tune شده؟
آیا وزن‌های مدل یا پایپ‌لاین رندرینگ پشت صحنه تغییر کرده؟
یا Ox Alpha واقعاً نوعی یادگیری مداوم دارد؟
اگر این تغییرات بدون اطلاع‌رسانی رسمی در حال رخ دادن باشد، ما فقط با یک مدل بهتر طرف نیستیم؛ بلکه با مدلی مواجهیم که رفتار و توانایی‌هایش می‌تواند بدون انتشار نسخه جدید تغییر کند.
و این، از خودِ افزایش کیفیت جالب‌تر و البته نگران‌کننده‌تر است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8dR0PgiL4_OmBVnu7qGC3YvVJeElBBRWvF85QxwZPA1du_0Bl2na49kGaeuCGHtMDFjYbXWvcKjqohLsP4P_hN8xDV7_d06Kn2J9IhFgLU-jW5wlp1UtYLJCe2hRP00IWCAJ-BtMcPiIstz6BX_mKgvxBEgifj7EDpjmLJx4dcMwj1HKL5HMuKyuWNAJiEaK6jjRNQi68LW2Zjih0DD2_2qt7yyuFwq4bJOcnnPjVs0hWPk981ALxnFLfn0i3Xxb6NfgxN-4lDb8MNVj4I5_QmgLr-5vZ1Vpzq0f6zYyG5ctA9c0HEskKiPwJJOLvoNDRaHbMfVMLr2XZdYX-jJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E1ja55tUwhWK8wg5epb-0LQb3GWewxeecTKd8DkiM3qe5nsoMYbumTfejdoTa6bmuCQFEoYYVyKvqIDd2NJM4P3lrp1V0sjfmdtqLHd0VCPJ2KBcDlVTEtDhEEBd2ddBpgInxRfmbXk677iXdQa0lXeHYRzDeO2v9RGsTFnkaLNVZDYQZpibNsJM4_oHYmWNya2gTb4b7GFoX6P0tFmbAr39mWlVfj-Z0xTJsPPnIR5J6lt9-ZlJzwNuA_Xsio5GLBzC1MRd5VIp-oSkWW6laBKU6DATy3YzIM72J2jLhR-1EuRcJjsWr3hPPWoAfxEvmwI5ijb2i63zC_hSW9vhaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو:
1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه)
2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید
3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی بعدی که پشت این میاد فردا، قراره حسابی ارتقاش بدیم)
4- آخر ویدئو هم توی ثانیه‌های آخر یه چیز جادویی هست. اولین نفر برید ببینیدش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به هیچ دانش شبکه یا کامپیوتری نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آموزش مدل‌های AI روی کتاب‌های کپی‌رایت‌دار؛ قانونی یا نه؟
خبر:
اکثر نویسنده‌ها بدون اطلاع و رضایت خودشون عملاً توی ساخت همین ابزارهایی که شغلشون رو تهدید می‌کنه سهیم شدن. TechCrunch یه تحلیل مفصل نوشته که چرا قضیه از نظر حقوقی خیلی پیچیده‌تر از یه «دزدی!» ساده‌ست و Fair Use وسط این ماجراجویی نقش تعیین‌کننده‌ای داره
🔗
https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/
نظر من اینه که حتی کاری هم از دستشون بر بیاد که انجام بدن، دیگه به چه درد میخوره
😂
مثلا فکر کردن OpenAI یا علی‌بابا با Qwen که خودش دزدی و دیستیلیشن از کلاد هست(
🤣
) و... تره خورد می‌کنن واسشون؟ =)) یا مثلا میان بگن آقا بیا این قسمت از کتاب شما رو قیچی کردیم از LLM چند تریلیون پارامتریمون؟</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBG6e0ibParOt570R_7pLeHyG05LyF2O6GK5kOgG4wJmr_aLPZ4ruSaYhGyhbsBElkq7ckwzbF5fdZAO_sh_RuEjfTBxBsDpGhGVgVT5l92-MycU88KEJBOMLC93kA285McUNB64C4xZHy16lmiaAP1Z-22c-eY2mFXhVhSSyRYN7rR-Lih5Pzz-l06EkJVoGCE-PdtDA2CmQucMivO59hsqfFVs2WZoSjFI4mskhgJC9aJkvSPeF58stR7WRrKVAT4BNmp9YhaRgMOlPm8jOGWxIzOMr0s4mBNWA83h2sP2jY_E6fOV1-Qa6jLLo0IF3hTF_6nwQbdS0cMiP6C5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hMuV5W8Da5yLLdAun28PAcEANBIuCfIjIey98tkR-QQLsBd5f_TbQLoBDEp69HmGgv5MmfxHqN8oQz_cceUB-YMTIALnbY6R_cEjshnuTTuLAGB9SZVirgTiDN_nlqOb6fbqSSwue5Fb4ev9pdTN47rQybbNYSyBV6RxRsAELdVBIiECsrXhX8E2BNGAugD5zB4t2aNiCgBGck6c-Gu3MI35fV0gwn41IUAA69HcjXlLo2Ogn0QWOsxFW7W_zpYR-2kf6Xad1VbO7feEDDrsRPwTXRX3zCHbit4qyzJq-NKzL2yz_Tq0n5ygxB50ivi69j-lXrdG92Lwcsuenxe0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eIQwBc0b8B6hXRisZf5P8ITPffxfNeGj8C9ldXUzJfCZWGOfAXY_RQ7YM1q3D6kyOChtoncY7q4UaPtKxLf0kChTCQwQvfoJe8IcyO5DPtoBlodQIYK5z45S9JoTLa1ntb8BvOLaXFsd7kjjKN1U9-cmrKUmbI3XQcCEX_3eUJupU8cwO-lCk4-FFmxCQTx0pxxhPwqoQ4SjpuNw13PKGUtpuwJas04n-wUOUzupXQjVDaivHcDhm0C3Jj6LpQwHgocwn9GF-ckwbQEwUKtmEa1cetNKbgdlwlem14HuSvXC_zSsyS4eW2byoCh2wNLN4NliZzHyUrkg-k2PnA48QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه چیزی دیدم تازگی ترند شده توی توییتر، یاد همستر افتادم
😂
😭
گویا اسمش ووچ(VOUCH) هست و طبق گفته‌ی دوستان کریپتویی، یه کمپین پولساز هستش و فقط هم یه روز ازش مونده.
اگر که تونستم جزو 1000 نفر اول بشم و جایزه‌اش رو بگیرم، یه اشتراک Claude Max میگیریم و روی استریم میریم میفتیم به جون ایده‌هایی که می‌دید. بازی سه بعدی چرت و پرت هم می‌سازیم
😂
فکر می‌کنم نهایتا 5-6 دقیقه زمان ببره انجام دادن این کارها واسه‌تون اما اگر که انجام دادید، هم به من ووچ میده هم به شما:
الف- برید توی سایت
commonsmade.com/vouch
و روی Claim With X بزنید
ب- جوین که شدید بعدش روی پروفایلتون رو بزنید. اینجا باید دوتا کار بکنید:
1- گیتهابتون رو وصل کنید
( گیتهاب ندارید هم راحت بزنید Continue with google )
2- مجددا توی همون بخش پروفایل، یه جای کد تخفیف داره به اسم gift code. کلیک میکنید روش و کد "love" رو میزنید، باعث میشه ضریب 2 بده بهتون.
بعدش بالا، سمت راست صفحه براتون 7 تا قلب ووچ میاد و میتونید به دیگران به شکل زیر ووچ بدید توی توییتر:
Hey @commonsmade, vouch @MatinSenPai
زیر این توییت من می‌تونید همین جمله بالا رو بنویسید:
https://x.com/MatinSenPai/status/2091522197537919325</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qtZiHmgpy2_g3jzhbAi4v7tpWfL3pul67_6QEGOv7TYVNBl-hIn_CoxXhpPsRrf6fwXVcqHhsrd7PlRkWyCjPhg0f8egZlOEzPuAh74Lmn5dwk0nvW5XxyYtrcpjt6wgHjxK5nUCIzx8PYRwwBfaZhpxTKq3x3QDEUvUfYoyHIUdkM-dxX8jhaQYh3PZMrCM4nUW2GHd8IYW93YxNKP0MnqOn5aAMHaQ83JxVcZ-W3A_XL1KCZmCVWoMLsWGZFhn3O_hnqekJ3n2RUdcUOtqF3o-YObBpLwbXbWxATnTEn-_aO6RPf-V7ZN-mZevunxbk5ksFMp0UfwEknbqxA42lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=L9q2XQTBQesywD7KV45kNQDDvsB632jrEU8x_UBy6W7CjlJY7mPjLX-SLBLU8HA90LSXY_ZvS_8Uo0fokJJKeSY0jMpZM72UKLmehDpQI2nd0lHF2t7ZNA3FCA-vZnA4HTpSk6N3BS5D7tT7EOPaNlAsGPNrdKTcj7gpymn_kBHmObJNLbEXfRBw2Zp-VsJuH8j0x8PnN72bHE_rXq-JeSWbZEaWmrOIRgN6rIyI9AIJCSIQHL88ivziCkWui6Icrvhu60w5xUVUmG6pjtMsG9fVooeoQBtgxzhK_WAnHIki0y1Lrhwal94JZnReAFnsyJd2mE5f-wumUNJJ0GIr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=L9q2XQTBQesywD7KV45kNQDDvsB632jrEU8x_UBy6W7CjlJY7mPjLX-SLBLU8HA90LSXY_ZvS_8Uo0fokJJKeSY0jMpZM72UKLmehDpQI2nd0lHF2t7ZNA3FCA-vZnA4HTpSk6N3BS5D7tT7EOPaNlAsGPNrdKTcj7gpymn_kBHmObJNLbEXfRBw2Zp-VsJuH8j0x8PnN72bHE_rXq-JeSWbZEaWmrOIRgN6rIyI9AIJCSIQHL88ivziCkWui6Icrvhu60w5xUVUmG6pjtMsG9fVooeoQBtgxzhK_WAnHIki0y1Lrhwal94JZnReAFnsyJd2mE5f-wumUNJJ0GIr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حدودا 20 روز هست که دارم با ابزارهای مختلف و AIهای مختلف کار می‌کنم و خودم رو آپدیت می‌کنم و چیزهای جدید یاد می‌گیرم، و ویدئوی جدیدی ندادم در مورد AIها تا هم دانشم بیشتر بشه هم محتوا باکیفیت‌تر. اما طی روزهای آینده، کلی ویدئوی جدید راجب تجربیات این بیست روزم می‌سازم و می‌ذارم توی کانال.
(آرک سولو لولینگ مخفی به پایان رسید
✨
)</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5022" target="_blank">📅 06:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UL8TTHn2HPatIkSRoFvUclPozEHm3_n2ilUjKMxrERipbOKsp-k5rmbcfr-VFd1wal0cpfROyBFulNSUl9x4Ah0uaUVws6rG5xAoIQagO1Cp3col5m2u1inQVSZhX7kCkBJ7_7wC3WLtTLzU6ROCrp7K6lwqI7VA4aTsuMIUiKK5FnqUHl5aI2zIgiVx9-3UeHhtvx0-ZVjUOr-WbxgIdBvHze6pzEH1_rK8hVSiPdQhYGv6N6cDaFsT3vUMuRgGFQXz96Ge7Qd6Wgv6Lr9pkaJSZhvEnZOK3prUldhsaxAx9kTujXXRXXZcDk88hPyGMWdTkmMsZgKlsZE9ZLioqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TIDyC8EsPraIdh-mpybf5u8itkWrnv7AhTYwYemNQ8sHLF2-JO3cduMAjXM1_RpW_8Oe6E8V8YwhIEsVvB_Z9fH7erRVWuMuCq-bxMcXZ-dHVjeRZ_r2Shcf4qbgkXjgL4V4C-AIE9h7qj9rAkagtdREe8NjGSDhwr1NB32jwcYRfsO01CK37qxLTBwWGMawlxlO04zzHLvkXtdrmpLUjxdAZdg8lPJt-oWDw8VbPSAgsWWyZX3WJ3DgoWyWR5mfnJVWVrctIcTB3UnAYNCbBhhYoxKuoYWGOClfGCuNmsBkdi6ZX34F1JYk4t7fKaay9dJnxpvrioXxo0JTHbtOkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیلی خوشحال شدم امشب از پیام‌های محبت‌آمیزتون و از اینکه آموزش‌ها چقدر کاربردی بوده واستون
❤️</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5020" target="_blank">📅 05:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LM9q-16XCJlTGEKw52auWE0oXD2HlVcjUxnSimONhBzfN-izbigNRPDc6zWWNHSjAcNQ4AKqcUrJ7arVBIernV5RFS2R7_Yd32CiPjvXMIjqwQ1zrFVFpuGTnfe5unVWoxTJO0_626hfwcECUFQrEnOhBcZnit6l3HHrnX49O-sidw6x-EZkaLbvuzMiTGX2TSLAC1oLCBy77sHOK7sGQEYux0oZHi5p1-wxyYvA0UKhFCjkNQfaiNzwpBM9jV5Zlb_F1FXA8qEse1nD4kH6-Oj5c4eorT-zRj2F0RbeRt-0t1e1PB5440CoSSZaTodpIKueBaKwehMf3vEoQJvUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XCla-T4hX2dzMayIFytNWHeKmmszru1My_46xiYcE8QVCXPFxwdjvR5XX5Maut4rUXUee-rAxMoOmDEkbbm3TH5_v214FuPkosIj7Bt7dhcnFowFEk77wMmZ_kymjKEc7bFCiFNTPgKhsvms6iSsI8-9pOzYZM2UKEsOm7X4gQ4Y6JPgIf9Js3k4jVW6k-1FyZIi60G3C5OkJ555ceqUb3rbysBu2aKZhll97XGW0aiom_6OhCiB0dklCgsbFfAaALhRnkQT4F3xRDJqAqUpvEz6n0nv2fZHiiO4M0uIiNfa-3HFDuFyNUjW3ueomijSLli-wOcI9JkEF8xf3vKyeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eNo9GxQzL_iWZJKKTZAFDsYn6h7oD27llO9ZydjWZlUOaKBqqjlHHuyIvDOMbFk9pNU2qDqh1nlvsutJLDm12ULMDh2HlnQmhz84tq_Hk2x2ATYEAhxUs-TuyqhqBRjDN-F_b-gRHMeCrW_LsmNOsQjYtPfm0x7Sz194MReot2M5i9QoGFf4VGs1sG0H1YcHpZLP_DTYt-hnVfleDJrC73FJSPqC22gXb3WjEx0OtfqkWi2UNJVTcGwwCNWIBW3DUYGrVeDP_3tCENA1VFyrW8HwtLp3tAyGs16mNAvUGr8NgXygpXGdmM5YZDXJPbhNSOJFpwKjzxRZXpjMW2__NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم
با همین روشی که اینجا یاد دادم
مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون
تا الان اینها رو تونستم بگیرم باهاش:
1- اشتراک ChatGPT(بیست دلاری)
2- توی کلش رویال کلی آفر گرفتم(رایگان)
3- توییتر پریمیوم(فکر کنم ۹ دلار ماهانه بودش)
4- پلن رایگان Hermes Nous Research
5- همه‌ی پرداخت‌های گوگل پلی(با آیپی آمریکا زدم. و یه سری آفرها رایگان)
6- اشتراک OpenCode Go(5 دلار)
7- آفر سه ماهه رایگان اسپاتیفای پریمیوم(با گوگل پلی. هزینه یه ماه بعدش رو هم کم کرد یعنی ماهی ۳ دلار. حواستون باشه)
و در کل اکثر جاها میشد خرید کرد، تنها چیزی که نشد بگیرم آفر رایگان GPT بود که انگار واسه‌ی خیلیا خارج از کشور هم قبول نمیکنه کلا.
و مجددا همینجا آموزشش و مابقی مزایا و معایبش رو گفتم:
https://t.me/MatinSenPaii/4917</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dlertrstOi_fX3s0TMQV1IczLEjiHllzX8f5JL9M8LBu-wR6-JnYs3Zs8wlkl91DPdFaIcGf-IIgdORBfh7Y9KRIAMTvQO7uP5g2xCMBr0CPWloBRHthHSzbxpGlKLyYzwfMjz3RKGMablJZn89PffDz8MjclmwVPgXUQMOFwsSANes95CyHz2MwuWB27uIojOe3cZ--6xfylZ9pCAPcXL3NMOF8UZYhgksZM4CKmrqsGrM9fCNlKYx25duuiIpWzA-PopX-0B4aC9yfHjfFG056zABg2I60bSjGbF94CNkVLi2gb8JiCHrupUFcWstyZoBZwOLaOezwnMX799cKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bg-ahBFE0E9en8j5as1i_jRmf7EjQ-p4QmU6TzjNuZzNnlCvTxx1KzAVotOwIf6bLog2mH-EO_rCj4JmbAFN8X5tdPt1X0nbXdOuA0xH17sysWbGaljlqlHYr04T3-3z1ewpyDtx8lUaNFjZWOsYjpNVQ3IWTjOTTI2F9pA2g-jGoudH2SYHbPcDsyaE5d1_KtH431YOv4kK5H9OG_VvsTjXBL_n68-ZWkTS4cplLvm7qCpLqp2LVOk5LAEHtnnSH5d6fuFG1ZzkoA2VJzqeTkGVID613AQBt-53ohRUkHY5wMr712keu0B7c3FFtsjoi2K0RfJBpIDoMBOjCHh1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/n-Q62xnmq_7udwt-UoalNltU_STAM6udlj8ojA68QuB8--7kDvhWRqII061ORHKTZAkVhQQpkDPLfsSQpjUjDd8nYRxiQipnpwRMsn3hh6-WlmoaoWliUF2HhnJeLhefL8R8WW1DP9QKzuXVwgRmkDLXI2nnq901Fc3nNYd8YzEGQVcRH-kqGvkkSEOwKVLswkMRLzL0u8D7hGJu9iCGKodT8QzcO_9k0j-BRgHpr1ysjizkB3Ze7UXF8AUedKSQ9ksrxcX_pzYGsy8rwc70lN_Ri5u5hWGTtxIEBNnGoArUZWLV5zF3LvSobCIQ-QxWam-x0w5ho1RCs6LOW1VYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c74WfnBGBLAOCXyqyvygO8yI_q1eEg-H-5CCOlT9ubASMQrdP62Qn2tc-rQt-qxWsgyLrMO8RSLaIif7XKnRTdaHB30_dyYQirCscq8knYCgyWdS9DdQ449gfMd0Wo9WvLXTRmeGqiRMnLoSCVprgoKLBY7VN0WaTLHv0e9vvcn52z-iuYZV7rU4eoEXB7qBehUhdsEl3LFeVp9d44n9l2rhA1atTrpIm0-WCXWDKNh4YMF7l-BRCBlLEtUS5BFcCMzJRXFIgr2k2A9LwUVNYljTBmBuyYBn4fiEXu0mIM-fulx8oH0Yo5-LYAN1cI6559DcIgVkx0zlYVnVXm2kXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m_Dz0DmaZYnlJXkBEZLh4nA437W82ammo07LKlywMdoLTOP8rhAhWVvFHG_ZZ-mrZ6epPZumNhbH-hrM3_RDb8mF608VnvFaevisUpSyEn_CAcjY0pmJnGypww00w2ZeA0DXGBOocz-4HUqZQm7J3gtwJL5qVgsBz2kkqT2ICVvdnA78ntDrqDEgU_-Y_7jVrmW0oy84qgG-H93mxhap3oPOxDIAZxAMPbovTlKKdhHfyh2oSA7xowpPlw7MDVPSqIokUnTO5q320vM0ZZ1ruag6ILc7MWV-MSM3OBd5aogqgavpNEa6XQMqn38lGuC1m2uuIHFDaxePIVTw-cIieg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Di-mW9alZcphe00GzZNSG_DYMYrQ79eSYD1-h2Tb0Q-F5mBOEhdAzixaXvG4FnqX1TX5ocY6pL1iKb83Egv5NhSZ-Bz4kj59ItKMzXEGpkV6ZTGJUgfTPwdntsM4hBmowdfR_g7uomznc_k0GKEvvgZyeZcD8IBl7uw4d_1nEkNmkDaLsHnp1-btnOi8U8pn8qot7ZVX9TwC5g8j385Q_jWAqFbuq2fnUs2dqOCnddrxIJ3wXUKP913rVQ9kz-awZ0HGlzYGSh1pUCWzV0Ys_XK5-N6e751MuQQsbhZKUdTiui5tilljDS4XY12mx2hW6vkH0QQFswbgzrRglwLGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcCGEm-OfsYj_A-ZXckeWOf3O4dUd_-p48S-NloVwh4U8EM8IgygKi_BgWd35Vb_hspFR5TzPEjo0Oa3fmXQPAXZn_uSGdcSNdmveNJCT6UkJru-_Ua1Pv7585DAU8onzuhzciEHZbLvg-2-LgFHyUfePlwudB0Pk7Dc2tqXcDRtCcaP_GnF8q3nBthwGFHLFAslv7YcptCgBCa1UgQMM9leJWuKZX83Ne2JHWgdNrDTJVQmJ8No38ADmuDilmFcGMA-VBCk9os501acUsWczmnHFbUJt4vUYTf0NCs6udUpSFsB__5vNO0Xg3gRqkLSXiNx_3OBmGOZHI-aJk1qbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب هرمس وب یوآی با یک کلیک
متین سنپای
بهم گفت که Hermes WebUi نصبش سخته و بهتره با یک کلیک بشه نصبش کرد برای همین روی پروژه اصلی PR زدم که اگر تایید بشه از این به بعد میتونید راحت این پنل رو نصب کنید و ازش استفاده کنید.
لینک PR:
https://github.com/nesquena/hermes-webui/pull/7152
میتونید روش ری اکت بدید شاید تاثیری داشته باشه.
اگر هم تایید نکردن مهم نیست
یک پروژه جدید روی گیت هاب خودم اوردم بالا
لینک پروژه:
https://github.com/nesquena/hermes-webui
میتونید به هرمس بدید و بگید براتون نصبش کنه
خیلی ساده همون پروژه اصلی رو میاد براتون نصب میکنه
حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g4S90Faf0dMkSs-rmy22v4_65ts2lEAnmVOLarU8L29R_EsKHRumyH1-1rCMUfKErDBUJwqziFf5N1eyrAsSLBn1-na6ep4aMxT8uGSiGTnYAt3Z32LmuJXyO9frWnnLSntb_3MJFk0u51pgbt6M2yrozL5hnuZdUj2yHAEZ80V-zmhYK6LhvjwbCMFYddcweNw09htbJZ3z5sEg5ODFBDiSLy33X4wpBTD3J80gkeJGwHtIc7zNOAt-q6pymeSJHW5uSuvCCcWjY52cLKq_UP1VrOTBjyQJgC2EfM4SsOklHQ_U7XDC73Knp7ntSV4wRFuNr2YvbCtkAj8JZcm-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DLEGvMa5rPFxepLdleNFaDAcXqr-u-OoDuXHq_6vUbQTU8m5FamfkDq0GLUj3EHTd9Hfv_VReZ0xInfdWtBqKhV53UmUKBY6J6Cubba-PtR9Tav_mpKMk6rVI7s_KMjhC8AAr2P8urlJ4NAOoA5eH4SdrduZNT3HF6NXQdtgX7mAm4HrqO5qHG3CXS0MeebzmEbKSoHWViH0EsRXRy2sJn6vl1lfi6VbYXhzmCnnQQTCx2qZD7kQnhAohnl6bwSyY0SnacTmEDd0Jhus9QQMG1t1__ONCge8klG9oUegcJkRxqCaTeNt-jW1dOKRSVwLOKuCWTuBM9jo1oU1T4-H1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G6KBlNLfyoJOjIXBPBEGEMe-4lQAM1VvKyfYetf3wEqrziM2I5RV-mE1mp6FtEYKlAq9uec8A9mw2cmLNCQ8sm3MaL8oSYvGaAAYXcr_32MPkRiHXHZUIBZr-wlroehvPPg9y4RsjcPVwW3pzsATN9IOIVCrDnYwf1FoHaU3m2jP7VdWaYUR-BX0VCN45ODP9VqPrVD-PcOZHtKIo_JmG1BXbP_xke7BJ_ydvmWOPesPaBb-amIqkoKcQuZ3C2UWAM_BuErMjfs1K7L0_yT-39cjuj8gGPA3z-23qiLwBa4PRh8ViqWYpX58vYE_K7wVVojPUTMdalFnu-_-4PeH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس استریم شخصی هم نوشتم واسه خودم که با نت داخلی بیام روی Kick
(تانل rathole
😂
)
هاهاها
به من خندیدین؟
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qiew1J0xiJd2xt-QmWGc_IX-HfLlNx2hcLquZ9UrOCx6BCVUMHSOwuFOMsDLpPMnEtmGJb6fEfPnxul04n2Nh2n5jzRO3ZdBBFTozYQ94CY434dw5kaEyHuXutOe06IuGiBkRSnDIivVRGiiv2w3FzFgXi-m7uOazpsAyTJWFYVEzGveol5Z-5jN-XcLpf_1G0ueM5ghrUTaba1UsbuCHzaCzwOQ0V0DSZoAfP-tW8obKZ_kPiRGjvfLkdPZr8sdWmAQSgRzlvPxcq7OER3gc9SN1JvA7L7CJMRVgsSmps6cVTpDk5QHlEsNxnfICVFBeGeWnON0ZTqg7nFkL7XB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nVml7tvfyS3ASNFJ5TolkAECGLl-L5u2pW-uHydV1hJXTwit9JS2ZwHsBn5WWer3Av6hyvFltvkujaXyHCDcpodbyEurgJu9ncWaQAhiH8VNppwyEUfuvMdGs5eHooOVgeZdzodGBfT0cOmPHsQtRdB6l-MO3C-nN8j-ifzSN-p_tjhplhIUaewt1OQOaHq53PwXV8TNGFQ7IZL6x9_fWmvW304d9iT3Q42vQnnqM5ZaVIKeQYZgDO6i4NllzyRvU2l5WSokSGBaOPXhdp16Qj-xcw8ijbucfnDODk8oQSs534UbWRVb0v8huGXpbiToSoiEWk6wHUD8pRsTB5e6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gptdRpkud8o1GuiID2brIJ8E1VnLZeOyKrhHJ0CEsXd26f0oCrX1Z2DkTLDYS8D64C5qpg0GATtSMPf5Vh1li8j3kYHnDV970cJv8b5PigaqEgFWd5TXILA6cVFa50LRlbOotxwgGSQOmJSzdAt3LZjQNTsqgD7puE7WqNoYd2ye99cfbr-3fcGlxJQiAgoYnuz4UkVPprxmhDi1bmK2hkx0Unlr-hf0HG321eWbkmMuRrOoDskpCzInpQq3xtr4K98KZY6xWGspVc1RnF_C0IAkecxhZElm3y527tc-TJIZdJFVCsg4xKf90GnT0gsJ1054C5Eb8NJ3PQkYvuhJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pqmc3A3wsvUVzKUiuh5MoY8_3PCcqUfjeFmDyD9Dp56Hx2RuBDLWB83W8uIk6V38xEinFIFi0ejMUc8cbcmRTvOP_FreXvxarZLcGdTEyHOHUap_uiL4LNoo_sCbI3aROtzFd0w_0REB504bF8iycB3tGfOERO-E2WOUmWVF66IVDGJt85ZLtW6jx6zr0qtw795e8H6Rx3jFWQg71mPqFBT69frg-EZKGQZX5YmYGmYEUH9Y4R0MKou5TIpSJYzRvCugFn1I5W-oVD909SgWv5YG84zMT1m4RIWpS_B8EONuwFylxLeNwgay51QzYLNBEc-1JwCDQAMw1nygzeemEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxjcuX12Q5uBLwx_DnM0Fp-nPiIupIuv90jNtGA1Wet0JKZhPnY9qSkBlM0G32pva3TEtgEio2SmB6jP6qIKMCkhoXZMykXBo5lxoLTqOI1AU1JiolweW9n9pJLG7l-jcvxv8KR6p39vMda7LR2ySdFOCCUwH4NLOEvBtqvwIuP6eZvvlSu9-OJr0Se72ldMJaAOdK_LdIyAYdY41tK__rkzIsksQufc4UGE9PDKGcaP4uJ41G9jR7h0unTyohnYjjBidGch1fQfgfdNWTlNqcsEJBZSMgH7XuBweYGMI7GlZrADaVfK384EQemZvcQ3F8ACUtwU7pH1e4m38oH2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
