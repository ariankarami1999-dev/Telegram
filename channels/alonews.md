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
<img src="https://cdn4.telesco.pe/file/jBi5S9davFQ3OZbsy6ezOQHvkkB_7_q58CsS9y4LcnZYjfJr66v6ioNHBi1fXKPEyIaN0TVoKTxgtYqzaNpzGCjuaSnrEQhGFHMDOkK9p-WD9GR6eWXvIfHXVymADfFQRKiz80Va4QscDO7D5jdtezieTOm-VqE3_QSpe4yiL_w4-Zsys2n3Tt5h5H3qGTCbT6Al_cMAKVa36xk64h4XuoZluQ16ptBktPJy5ZRFaefDsRoNH5h25g8Pt_tpqKSE7X6Elr9UfurzN133uv6zbGeeMwiCJJnr2j1m-msDpW_EPCe1YDYLv8A-Pn0tj36hYwQZMJmMI3aWOhoo9x6WZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 03:12:51</div>
<hr>

<div class="tg-post" id="msg-149453">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcY86Ugj6lg5zColOjxYhj3hH1RR3pqBL0X7GG8rYoETQBK9yFTJpzk_an4OsgRua6BXMLusecXCVlMIyQi2OEHBZDZe0HSPUCTORBzdjbPtQ6mAcPk2kVuO2hgOLH0aJSimFnP-VN9claivPHLjkvsZLkj4IxVcTwD-8Y2gyaM4lolH_4UShLs-Tp2c9k6eKwNHJmcqb_hSR79WPyLtAAR4iWTY9mAW7VXUju5gFjgUKzwZFUViv6CwCRG5COOTuv88EaZttXpoe8RvuvnNpeiLNA2erWm5yJhl9Fa2zWI1e4_KDzO2NGYlUM02xxzc41-x1Xio5bIBuWmJnNw-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">LIT VPN
نسل جدید فیلترشکن
🔥
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
🔥
فیلیمو
و
فیلم‌نت
و
نماوا
رایگان
‼️
سرویس نامحدود فقط ۱۷۹ تومن
‼️
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کدتخفیف ۲۰٪:
IRAN
🔥
خرید
از ربات:
@
litvpn_bot
❤️
پشتیبانی
۲۴ ساعته:
@mahan_lit
.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/149453" target="_blank">📅 01:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149452">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmAVJMwl1bk7vNm_T3Oypgcskan1Ej00JYwhSxpuu6GE7OkJSfBzkxPskbv8uRARuvi-EdIx9cVa-c5B39gEhUB63eRT7u0OiwH-f5GDzao20k25hMezbNhSCqRqjcKt2I-4FbQDBeTNoavmB4o8Pf1jrnW2iigaN2zUI9upRcHlMWo0DP8K4Z1erYsom38dksyqchqpPzeBtTtHejqe6fPGq_h8oPwgHysyfrGBLw8K-4GNU16HAzuP2GzKoWzhx3eB-pIjktF-XC7w9s96tt7_-wV5Vam_WBxvQVrjiIBMMj2RVdQ6ImenjoCdhnJ3LXsbOOzRh6XNWnfjvLKd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل: عربستان سعودی تمام‌وقت مشغول التماس به اسرائیل برای کمک در برابر حوثی‌هاست.
🔴
اما در نهایت هیئت نمایندگی‌اش هنگام سخنرانی نتانیاهو تو سازمان ملل، جلسه رو ترک میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/149452" target="_blank">📅 01:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149451">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
هشدار حمله موشکی در جیزان عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/149451" target="_blank">📅 01:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149450">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b4430e11.mp4?token=ueKcViG5IaDwWQr-6sKqizY3z-peZKuqcWcBJihXveULl1TAv_iM7x_O7mQArB9tWbW82GMllyZh9qGE7cuHHvzifXK9xUUR-Xzs2tB0sGLdiAA6iz6kZuRZwkvqzCLn6qxnQ7nrglAP8mGaaqoWWqQBmAsHRSv5fOACitHGT_LOxPtS6FeKbCwt-Sft6rRanw667pC7fxqvdHhkaM9_iLMJCtTl9K4BsUFsnZDT8o4JGJGse2OgZLgXfVdNJ-EyjMdYF6e3-xkJUEF27GLYx1WjE_O7bzlpfJDPe1C0v0blPnjZfUzycV9PWLMwAq_WnjdEFnTrDF678v_TTVhP4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b4430e11.mp4?token=ueKcViG5IaDwWQr-6sKqizY3z-peZKuqcWcBJihXveULl1TAv_iM7x_O7mQArB9tWbW82GMllyZh9qGE7cuHHvzifXK9xUUR-Xzs2tB0sGLdiAA6iz6kZuRZwkvqzCLn6qxnQ7nrglAP8mGaaqoWWqQBmAsHRSv5fOACitHGT_LOxPtS6FeKbCwt-Sft6rRanw667pC7fxqvdHhkaM9_iLMJCtTl9K4BsUFsnZDT8o4JGJGse2OgZLgXfVdNJ-EyjMdYF6e3-xkJUEF27GLYx1WjE_O7bzlpfJDPe1C0v0blPnjZfUzycV9PWLMwAq_WnjdEFnTrDF678v_TTVhP4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی دوست دخترم میگه منو میگیری؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/149450" target="_blank">📅 01:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149449">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دقایقی قبل اسرائیل به جنوب لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/alonews/149449" target="_blank">📅 01:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149448">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">💢
توضیحات عراقچی درباره طرح هفت‌روزه بازگشایی تنگه هرمز درصورت پذیرش شروط ایران
💢
مهلت هفت‌روزه از زمانی آغاز می‌شود که ایالات متحده این برنامه را بپذیرد. اگر این اتفاق فردا رخ دهد، اجرای برنامه از همان زمان آغاز خواهد شد.
💢
در صورت انجام اقدامات لازم، معتقدیم…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/149448" target="_blank">📅 01:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149447">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhVmR6ZA_oAmbES_rXGPNy27Z5nubt393Lw0MyfTHvoWzXULJse5DKvqNKkAT0HG8Vhvmn17b5xOCD_xMljMDWvTJXNrgDc2J5X1A9eNL5gMvHvtdWRXQdoH0DLTiM-FtobDBmW7bYeKbM6VnWM980wNFRfiXL8OEgG2DikH_7lUBoe_nGnadFH-ejR4hsHMbPevB__yIrt8a5kEHHXm4Az1fO4TK1krGhhQcC-ZV8HI-cmbf3n6aK-HxmO0Hmzo-PVyr4WlW3O489sQma3At4eHKSQbG2hz3EQIBaTSP3J4EAEn5-rA9jmPA-R1yfJTsT7wrH64TETbUGyINow_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی‌زاده
:
دستاورد سفر نیویورک رئیس‌جمهور و وزیر‌امورخارجه، افزایش احتمال اقدام نظامی علیه ایران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/149447" target="_blank">📅 01:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149446">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع امنیتی ایران: خبرسازی رسانه‌های غربی در رابطه با مذاکرات کذب است
🔴
ایران شروط ۷گانه خود را به طرف امریکایی ابلاغ کرد و توپ در زمین آمریکا است.
🔴
دلیل بسته ماندن تنگه هرمز عدم اجرای تعهدات از سوی آمریکایی ها است و همانطور که پیش از این مشخص شده است تنگه هرمز با توییت، خبرسازی رسانه‌های نزدیک به کاخ سفید و فشار هرگز باز نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/149446" target="_blank">📅 00:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149445">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=X55XzRkCUnwAEevg7IPb2btjAcWPZ6fcFHjpVCaSm01JfAQyfYjOHjbDxY7XkOFYJSDuUvfhVKSqLja8cW1KWMhNr-UXRY33z7RrygPoLat_1to_0FI5N4bCx0QQb8ZmiWB7izLbaRCE8_tRQgmMi4IXF4etOQ2haQgnwUG88xlrT0Y4abMaR5mJcf3GShoNhYsKeSAIAjP0dF8dxFoGycXIRRJSkR_ZiqJzNUIpjhTgPW55YfIZWYkcrh6eINNOnwWfFGVs798Op3y8C4ppXAuMf0lw0UVpHX7BkE3nbK4FNOHt70xomXjSfNzc9ev07vxyCXZ3p37K4hJ4F82Tmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=X55XzRkCUnwAEevg7IPb2btjAcWPZ6fcFHjpVCaSm01JfAQyfYjOHjbDxY7XkOFYJSDuUvfhVKSqLja8cW1KWMhNr-UXRY33z7RrygPoLat_1to_0FI5N4bCx0QQb8ZmiWB7izLbaRCE8_tRQgmMi4IXF4etOQ2haQgnwUG88xlrT0Y4abMaR5mJcf3GShoNhYsKeSAIAjP0dF8dxFoGycXIRRJSkR_ZiqJzNUIpjhTgPW55YfIZWYkcrh6eINNOnwWfFGVs798Op3y8C4ppXAuMf0lw0UVpHX7BkE3nbK4FNOHt70xomXjSfNzc9ev07vxyCXZ3p37K4hJ4F82Tmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توضیحات عراقچی درباره طرح هفت‌روزه بازگشایی تنگه هرمز درصورت پذیرش شروط ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/149445" target="_blank">📅 00:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE06p_nNLiFrCPJr3Cpcvr6nRsuP4Au8CYvrHHLwRKlrkVnK8R-2V8GUB2dyXmldWi8Rhav_JqfZsPGaDuyNJiO90uGR6kHQWqNNA6M3tXfdBFo_vjvhu1IpH56zBoNUbC16hCvd5OL7UZk74w5uBvxCKFrJ-DlMr0HQCHrXoxma0fF3wxuXRZupEuXXK4jSLsPRhZ1coUUS17tWxRcDoNZuRumqlRIwtkVgbmkUVHlDExVd3nCUSQ5DciiGOoKmwqbJWj9z9FcMKH8rkp1MPNFe0x5bjAYK4nv9ORPfm8Dx5aA9-HtDA_E8r9HRxJq9G6NA3yTWkYqKLeZLqAb74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توافق شد
⁉️
🔴
خوش چشم: جنگ قطعی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/149443" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پزشکیان: ایران بر بازگشت به تفاهم‌نامه اسلام‌آباد شدیدا تأکید دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/149442" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراقچی : ایران یک طرح مشخص و 7 روزه را به ایالات متحده ارائه کرده است. در صورت فراهم شدن شرایط به دور از فشار و تهدید، تنگه هرمز ظرف ۷ روز می‌تواند بازگشایی شود. مهلت ۷ روزه به محض پذیرش طرح پیشنهادی ما از سوی ایالات متحده آغاز می‌شود که این پیام را از طریق قطر منتقل کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/149441" target="_blank">📅 00:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149440">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43bb16d0b.mp4?token=kMoCHqECj9DqW9s-ZyEKDdME2OcCOWNEhlmNw7g5kJwceBP0L61KG4bumbabGzHKJxF1bhnNmVaFPvRThYYjwhMDb4c8DpkGU9GaGW8kOnT0BGGhEiLrLVXAj-zorRjnqF6Qo_MTtj3VkNXBedl0ZqdZRQ-4us7_kn_-2YGuJoR-fC_5KoERMNMIuKno1TMrT1O_g9XE2QypTaOa1eCQqW5VnQ6ay1IMR1e7s7Rn1jDB1x5KFAq6xuFRKuCHQAvwOQkOgBgjmiuCE1O4E-wAS6T9DaQMNg2L9IFITffzZAs7vqk8B3gyxJNg_GszJomv-RhAJaoB2A9DghdTjfkQAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43bb16d0b.mp4?token=kMoCHqECj9DqW9s-ZyEKDdME2OcCOWNEhlmNw7g5kJwceBP0L61KG4bumbabGzHKJxF1bhnNmVaFPvRThYYjwhMDb4c8DpkGU9GaGW8kOnT0BGGhEiLrLVXAj-zorRjnqF6Qo_MTtj3VkNXBedl0ZqdZRQ-4us7_kn_-2YGuJoR-fC_5KoERMNMIuKno1TMrT1O_g9XE2QypTaOa1eCQqW5VnQ6ay1IMR1e7s7Rn1jDB1x5KFAq6xuFRKuCHQAvwOQkOgBgjmiuCE1O4E-wAS6T9DaQMNg2L9IFITffzZAs7vqk8B3gyxJNg_GszJomv-RhAJaoB2A9DghdTjfkQAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری تلویزیون: این جنگ تمام می‌شود آمریکا هم می‌رود ما می‌مانیم و این همسایگان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/149440" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149439">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9373fc68d3.mp4?token=LfCy1vDL4Y_rBihyGG8vUVsP1HITKR_QC9k4D9h8EH7Sl-38fNLllBn9i0pjWTdGjELPu7YDXev65I9rszF61xeEXjT8PdPDG3V64Dmqf2HTb9ZXiwl9rVHfwk_Y1bKlGHVLOvaJuLtBe8b_W-XDGwUSbUTdADILOo9IYt48aob0SxH_zqnWcPAQ-OIdsMoLOploduWI7r1VtXDF-hBhyelA6MFEUCZ87aifRe9fi_440QoXO0IW_XCDXzgeNNwHRJbBGPVS8Qqse3MHi2s14HxKyr3K33FaSi4xuSJDiOv5CGc3hry0fpj7SFPk44kyMVDyuotYuPXIPuvcn_WbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9373fc68d3.mp4?token=LfCy1vDL4Y_rBihyGG8vUVsP1HITKR_QC9k4D9h8EH7Sl-38fNLllBn9i0pjWTdGjELPu7YDXev65I9rszF61xeEXjT8PdPDG3V64Dmqf2HTb9ZXiwl9rVHfwk_Y1bKlGHVLOvaJuLtBe8b_W-XDGwUSbUTdADILOo9IYt48aob0SxH_zqnWcPAQ-OIdsMoLOploduWI7r1VtXDF-hBhyelA6MFEUCZ87aifRe9fi_440QoXO0IW_XCDXzgeNNwHRJbBGPVS8Qqse3MHi2s14HxKyr3K33FaSi4xuSJDiOv5CGc3hry0fpj7SFPk44kyMVDyuotYuPXIPuvcn_WbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجاب استایل‌ها از حموم رفتنشون هم فیلم میزارن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/149439" target="_blank">📅 00:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149438">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/149438" target="_blank">📅 23:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149437">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
دبیرکل سازمان ملل: ایران به دنبال سلاح هسته‌ای نیست
🔴
آنتونیو گوترش در دیدار با پزشکیان: صدای شما و ایران، صدای صلح و میانه‌روی بوده است.
🔴
بر اساس ارزیابی ها، معتقدم ایران به دنبال دستیابی به سلاح هسته‌ای نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149437" target="_blank">📅 23:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149435">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی سپاه: تا تحقق هفت شرط ایران، دست از تنبیه آمریکا برنمی‌داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/149435" target="_blank">📅 23:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149434">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0beae5d2de.mp4?token=ESam5yOt9YxCmZnBtXN7hD7M5a-1tC6i7OyD1UIYhq3InS2WBFjiDQpmBEJhu-lhb5GE2lx0CSkYz03qUsXOhVqmIPrB883rFltyv0qbSIQNQECCc9cpbkyY16qSvOVTSlbeqS4NlY74IDPVWKC5X1uFpEi_fnGenCCfI8IFpW5RPBly9XPjl-bnAfz5KYDXgxt2AdrCAk8C7r-xnfgHNkUymDS3s8gG0g2nTM5lgrs_BSbJ1VC4FtVDxaoxaAeIMR8Lguz9TESnD9VBp2qzPAdg6PHSTER9YO6MZMPwugxWoB57PERqN32A--qLjYpKhbl071BylHr5ozT0RKAQow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0beae5d2de.mp4?token=ESam5yOt9YxCmZnBtXN7hD7M5a-1tC6i7OyD1UIYhq3InS2WBFjiDQpmBEJhu-lhb5GE2lx0CSkYz03qUsXOhVqmIPrB883rFltyv0qbSIQNQECCc9cpbkyY16qSvOVTSlbeqS4NlY74IDPVWKC5X1uFpEi_fnGenCCfI8IFpW5RPBly9XPjl-bnAfz5KYDXgxt2AdrCAk8C7r-xnfgHNkUymDS3s8gG0g2nTM5lgrs_BSbJ1VC4FtVDxaoxaAeIMR8Lguz9TESnD9VBp2qzPAdg6PHSTER9YO6MZMPwugxWoB57PERqN32A--qLjYpKhbl071BylHr5ozT0RKAQow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عراقچی و وزیر خارجۀ ترکیه در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/149434" target="_blank">📅 23:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149433">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWPFqdJ0PYufeArxJQm1SFy3yaHpHbyVyddf5YYaVfey2GGKalUAxtQMcQBraVucl89u72eiVE4hzCfkiJ5ZFBW-QfJ4aZhYD7Dayi0a39ZztTlY1u9EKOwIGjBKgQU_VqNUApfC0s4lf9z5Ak16Bo4kGTC9WKfGmhW6wnmibtiecdkqli1z7YaqGAJXcouqfT3R4T4eQsHW9_qH7e1sWxRQ843i8fzCPLM_BFTYwmN1rVd2c_JDVOnWeGNsyhxUhMzCebVz03D1EUVnhxrRWMskU2i76wDS7A-mEdlCMNy_DwtjzRLZz7YNm4L9jZ15sDYyn0bMifsTcXXP499q-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تجمع کنندگان شبانه از دولت درخواست کردند که حقوق نمایندگان رو قطع کنید و به حساب رزمندگان واریز کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/149433" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149432">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
کریستیانو امانپور، مجری ارشد سی‌ان‌ان:
وزیر خارجه قطر، محمد بن عبدالرحمن آل‌ثانی، به من گفت:
🔴
«ما در چند هفته گذشته تلاش کرده‌ایم تا دیپلماسی میان ایران و آمریکا را دوباره به مسیر اصلی بازگردانیم.»
🔴
او افزود که مذاکرات غیرمستقیم این هفته «پیشرفت‌های مثبتی» داشته است
🔴
«ما واقعاً امیدواریم که دیپلماسی پیروز شود و بتوانیم راه‌حلی پیدا کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149432" target="_blank">📅 23:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149431">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e658b1bc.mp4?token=DK9rVOY8sNd7PZshZsFzA8d7I74WxPPP4D124RHTX8z86rpYpQgenxqPQgeW8YSU6lxcd1ZrwkSVbRfTmm5woPd-aSJRsP6lkGmCMZGD8kWRx8RmyizgqO8P1dUmM1ksbkJniU-lcVpn52A0V3mkptmkT6rZCtE25vRBHyjy8n8-Roe9JSAIN-7aa4nq5UAAQH3naAUwvpAnIZ2dGkxQe5xhqlzqEdvDTTAOeXcT2IE2w6cH0-gj4erzSXm1f6tr2-cwsAqYLinR3lq-yFra9hoVGKGPXiZ6F5FX_7TOLU-ziEe8GtiX5DoryvytSkR-cW3zGbZEusos8n75GIbWfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e658b1bc.mp4?token=DK9rVOY8sNd7PZshZsFzA8d7I74WxPPP4D124RHTX8z86rpYpQgenxqPQgeW8YSU6lxcd1ZrwkSVbRfTmm5woPd-aSJRsP6lkGmCMZGD8kWRx8RmyizgqO8P1dUmM1ksbkJniU-lcVpn52A0V3mkptmkT6rZCtE25vRBHyjy8n8-Roe9JSAIN-7aa4nq5UAAQH3naAUwvpAnIZ2dGkxQe5xhqlzqEdvDTTAOeXcT2IE2w6cH0-gj4erzSXm1f6tr2-cwsAqYLinR3lq-yFra9hoVGKGPXiZ6F5FX_7TOLU-ziEe8GtiX5DoryvytSkR-cW3zGbZEusos8n75GIbWfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعارهای امروز پیر پاتال‌ها مقابل منزل حسن روحانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149431" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149430">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ایرنا ، خبر خبرنگار الجزیره درباره اعزام کارشناسان فنی به نیویورک صحت ندارد
‏
🔴
ترکیب هیئت ایرانی تغییری نکرده ‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/149430" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149429">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizz Vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opGAuvB39RBwKG6C3Koh9Xyv5j2bzzm9yS04ghILaawVmUeTMyfAIH6xhzjm-D00TzedhCwEzrPtnKdAvohDWGEdTM80Z-LB-uUVXNeh8aOPWmkH2toJ_EN_Dz7kQT5bpSvXYOQAIZahJNDqCdHm406stGTyDOR_hBIK0uqLI1ze44XczACsgyjGjLF46IEdv8POv69-AqCIlvURjoQ3TqOVCd6O7OBuBn37ADEPyIB1uMuAAukUVFPeWvHqtO8taMAoCPVQtP23cBUh0SqRCmVpJu3NZyxdg4-ImxZ7sZCKU92wAWU00JPbQhT9OLu0KARQNx0OUcGqm2De69f2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
دارای IP ثابت
💥
سرعت بالا و اتصال پایدار
💥
اتصال پایدار حتی در جنگ
💬
تعرفه ها
🔸
سرویس نیمه عزیز
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود نیمه عزیز
▫️
تک کاربر — 180,000 تومان
▫️
دو کاربر — 230,000 تومان
🔸
سرویس عزیز
▫️
10 گیگ — 30,000 تومان
▫️
20 گیگ — 60,000 تومان
▫️
30 گیگ — 90,000 تومان
▫️
50 گیگ — 125,000 تومان
▫️
100 گیگ — 250,000 تومان
🔹
نامحدود عزیز
هفتگی:
▫️
تک کاربر — 129,000 تومان
▫️
دو کاربر — 149,000 تومان
▫️
سه کاربر — 169,000 تومان
ماهانه:
▫️
تک کاربر — 240,000 تومان
▫️
دو کاربر — 360,000 تومان
▫️
سه کاربر — 450,000 تومان
🔸
سرویس اختصاصی
▫️
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 275,000 تومان
▫️
100 گیگ — 500,000 تومان
▫️
200 گیگ — 800,000 تومان</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149429" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149428">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=Fr7TJqj7EnTrsb0mLhU-PVFEe6MHdV4VdJMz2wi3kZuhgKLfB4TpeE1BdiMvabp9oOUd1_CYBj1DF7wM985h3WMF53f6gQx90KyKgh8Qzv0t8TjegEIR_7aRr2XIvsLIGsSl-KDg1ftoOQDlmCK3RKE5nJQM15xALENf1ueSAqORPtmO2R4fUPkyCAWWZRSbKb9AyodrUEFByqTb5M8dnJ55EW7tcStPubWnaefiEilWiJlBGXMWIhcXUqYFXlMSH4r3QbIYXaPGjisIRPoM7js36KoiNsArAC6hbwnquALve8J3jVyyuezPMiWx0u90XxQ2CvILYZXunXEr6Ugruw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=Fr7TJqj7EnTrsb0mLhU-PVFEe6MHdV4VdJMz2wi3kZuhgKLfB4TpeE1BdiMvabp9oOUd1_CYBj1DF7wM985h3WMF53f6gQx90KyKgh8Qzv0t8TjegEIR_7aRr2XIvsLIGsSl-KDg1ftoOQDlmCK3RKE5nJQM15xALENf1ueSAqORPtmO2R4fUPkyCAWWZRSbKb9AyodrUEFByqTb5M8dnJ55EW7tcStPubWnaefiEilWiJlBGXMWIhcXUqYFXlMSH4r3QbIYXaPGjisIRPoM7js36KoiNsArAC6hbwnquALve8J3jVyyuezPMiWx0u90XxQ2CvILYZXunXEr6Ugruw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مسابقات کبدی بانوان، کاپیتان ایران حریف رو گرفت عین گوسفند پرت کرد اونور :))
بعدش خودشم زد تو سرش
😂
😭
@AloSport</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/149428" target="_blank">📅 22:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149427">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فارس: ادعای آکسیوس و الجزیره دربارهٔ مذاکرات ایران و آمریکا دروغه و هیچ مذاکره ای نکردیم
✅
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/149427" target="_blank">📅 22:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149426">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
نخست‌وزیر لبنان: با کشورهای خلیج فارس و اردن در برابر حملات جمهوری اسلامی اعلام همبستگی میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/149426" target="_blank">📅 22:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149425">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oghq_40uVJY6fabwUp_phOFWwlvWghaymw992lHzTdqqTYT7vB1WlGmOkTXRInPrfkxyeFUS8YtpaxrQRVsMqw_aTBJzRJhveqiqN85qWqoPSlDQhyT3gR1Ff5H8xbd92NQcF72VP4MspwZZ_RFiqCk6HwaqOKmF9qWjpItzMpmIh1xGkx9BVlZ7UoI2Er9PjsjAxW3ZV0Mh7YqInNxXuQ1vH1YibKqt_afXCyS6Tk6w3zS_F_k4r1urWraB-Gze4gM9VjMzPoCrNe_zFWG1UcI_Rub5IDQGKfPSv5XXF-KTfWrgIHKQDyPqqomsKtEo8fJk055T7pyg5WnDPScpOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ایران بر ضرورت بازگشت به تفاهمنامه اسلام‌آباد تأکید دارد
🔴
از موضع مسئولانه جناب آقای شی جین‌پینگ، رئیس‌جمهور محترم جمهوری خلق چین، در حمایت از بازگشت به تفاهم‌نامه اسلام‌آباد و حل‌وفصل اختلافات از مسیر گفت‌وگو و مذاکره قدردانی می‌کنم.
🔴
ایران نیز بر ضرورت بازگشت به این تفاهم، اجرای تعهدات مورد توافق و فراهم‌کردن زمینه برای تداوم مذاکراتی جدی و نتیجه‌محور تأکید دارد.
🔴
اشتراک نظر تهران و پکن در ضرورت احترام به حاکمیت کشورها، کاهش تنش و صیانت از صلح و ثبات منطقه‌ای، مبنایی مهم برای همکاری‌های سازنده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/149425" target="_blank">📅 22:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149424">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
گزارش‌های تازه از وقوع انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/149424" target="_blank">📅 22:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149423">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyxLvMXEP_k-vwBJvlWbljHqh8ktQgw5aws32aKuqs_DywMmmEyGmaxnGlJHheHgw6pXfY-NEVVDo2cDC_XbTwx4BK758sg9tI-6W0gjRwCUMiTJG_JkVmvIKVCfnjBKssciUA_USukpsa9RNggpLRGwt6HkthKWPqSSjJJs_87ZT6Cbs4xdEEue_IxsoT2QLqEYfG9INyw4Dh0SlQYYWSL8LmwW9kFogCxL9G9VkOFX-KbgLzER3un48KRqL-hB7WfVvOXfa1Ir3DLxrUHMvJPy0NEZPd7esEczMxlFhyziurpZZVjcVPpHSHzVW560hgxPn31VHuxRNWejpsRVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: هیچ پیشرفتی در مذاکرات غیرمستقیم با ترامپ حاصل نشده است؛ منطقه به سمت تشدید تنش‌ها پیش می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/149423" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149422">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر خارجه عراق: با آمریکا درباره مسئله تحریم‌ها گفت‌وگو خواهیم کرد تا امکان ارائه خدمات به پروازهای ایران فراهم شود
🔴
طرف ایرانی را در جریان ممنوعیت پروازها قرار داده‌ایم
✅
@AloNewd</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/149422" target="_blank">📅 22:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149421">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSMyuhq_XItdqP0GjuAtGeCa_YaNhdK2FcbgJcNDN2C9T05NbxGswMhjPswdhHWfyTspVmjAZDF_R4FuB5Lx0eviaxw3Jw9x0bQu-__ol_kAL0ScKy4RNh6nHUlzng5vGb3QThBiTkxPOMoMDNy3eXd7nK4SgaWW5vz9C11n4N1Rhr74lEioyobnstq9gK0W9GURcflcO5Cf4WJeC1tSvs_63FjVZMPXyfuR9vJiBL1c3cthGkfCPOJRQSh8UYpRgRSmCGHRVzSv4NBTQw9_ej7x4iAtBotwxPvAF2wTNpSX17B_2tVj6MmkW9k-U9Xhv6vfXx6zXt298FjHMB1IvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت کلمبیا  را یک گروه تروریستی اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/149421" target="_blank">📅 22:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149420">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
فارس: ادعای آکسیوس و الجزیره دربارهٔ مذاکرات ایران و آمریکا دروغه و هیچ مذاکره ای نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/149420" target="_blank">📅 22:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149419">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف:
به رهبری قاطع و بینش‌مند رئیس‌جمهور دونالد ترامپ، صدها میلیون نفر از جان‌ها در جنوب آسیا نجات یافتند.
🔴
مداخله به‌موقع او در یک نقطه عطف تعیین‌کننده رخ داد، زمانی که دو همسایه دارای سلاح هسته‌ای بر لبه یک جنگ تمام‌عیار ایستاده بودند.
🔴
و چه کسی می‌داند که اگر رئیس‌جمهور ترامپ در این لحظه حیاتی با شفافیت در اندیشه و عمل مداخله نمی‌کرد، چه میزان ویرانگری رخ می‌داد.
🔴
بنابراین باید اطمینان حاصل کنیم که جنوب آسیا هرگز دوباره به آن لبه پرتگاه نرسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/149419" target="_blank">📅 22:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149418">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان:
تعهد پایدار ما به صلح همچنین در توافق‌نامه دفاعی مشترک تاریخی مکه میان کشورهای برادر — عربستان سعودی، ترکیه و پاکستان — منعکس شده است.
🔴
این ائتلاف علیه هیچ کشوری نیست
🔴
این یک تعهد جمعی برای دفاع، ثبات و صلح در منطقه است و چیزی بیش از این نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/149418" target="_blank">📅 21:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149417">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان:
ما یک‌بار دیگر حمله‌های اخیر و ناپسند حوثی‌ها علیه پادشاهی عربستان سعودی را با قاطع‌ترین لحن محکوم می‌کنیم.
🔴
تلاش برای حمله با پهپاد به شهر مقدس مکه مکرمه، مسلمانان سراسر جهان را خشمگین کرده است.
🔴
هرگونه تهدید علیه امنیت و حرمت حرمین شریفین، خط قرمز ماست که هرگز نباید از آن عبور شود. هیچ مسلمان نمی‌تواند حتی فکر ارتکاب چنین جرمی را در سر بپروراند.
🔴
پاکستان با مردم برادر عربستان سعودی، همان‌طور که در طول تاریخ همیشه بوده‌ایم، در همبستگی کامل ایستاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149417" target="_blank">📅 21:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149416">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف:
پاکستان انتخاب کرد که با سرعت عمل کند. از طریق تلاش‌های هماهنگ، پاکستان با موفقیت واشنگتن و تهران را تحت یک سقف در اسلام‌آباد گرد آورد
🔴
از مذاکرات اسلام‌آباد تا تفاهم‌نامه اسلام‌آباد، گام‌های تاریخی بسیاری برای پایان دادن به این تعارض جدی برداشته شد.
🔴
در اینجا، من از فیلدمارشال عاصم منیر، رئیس نیروهای دفاعی پاکستان و رئیس ستاد ارتش، که تلاش‌های بی‌وقفه او به ایجاد فضای دیپلماسی در شرایط استثنایی دشوار و چالش‌برانگیز کمک کرد، عمیقاً قدردانی می‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/149416" target="_blank">📅 21:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149415">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه نیوز‌نیشن گفت که در طول ۴۸ ساعت گذشته، تقریباً ۴۰ میلیون بشکه نفت از تنگه هرمز عبور کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/149415" target="_blank">📅 21:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad11830c5f.mp4?token=Z0ApOViXWTCM_3S198f8L8bsuIKZgVEpxH5JrG3RtBlVKudrrOfC5osrhbHZ4ZVZPH3AizmCEtDwnJEEoXD3RKdZFAro3xq9qDqBt3jIIE2kL-1N8bwfBJK7e8VNIM4thkPaiirXgv8lvgRopzvYgSQ7NS0_UwtkvlxoIPLSrfbiTd_kZkyQZLNYS5FljTDjBLqBdqSWn6nptVNmoSBQbmWMfjkHGPDNKXulE6HIHGNV76D9uKxHGBbH4vAaXKysvhO-2F0mY7lkEggHSs05_IrC5XNog1TTtbVCLRC0IImg3e6WUfrnn8bnopjS_nBjcNF3E4jBzFWPeOpYRBQvhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad11830c5f.mp4?token=Z0ApOViXWTCM_3S198f8L8bsuIKZgVEpxH5JrG3RtBlVKudrrOfC5osrhbHZ4ZVZPH3AizmCEtDwnJEEoXD3RKdZFAro3xq9qDqBt3jIIE2kL-1N8bwfBJK7e8VNIM4thkPaiirXgv8lvgRopzvYgSQ7NS0_UwtkvlxoIPLSrfbiTd_kZkyQZLNYS5FljTDjBLqBdqSWn6nptVNmoSBQbmWMfjkHGPDNKXulE6HIHGNV76D9uKxHGBbH4vAaXKysvhO-2F0mY7lkEggHSs05_IrC5XNog1TTtbVCLRC0IImg3e6WUfrnn8bnopjS_nBjcNF3E4jBzFWPeOpYRBQvhoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: تنگه هرمز و تنگه باب‌المندب، شریان‌های اقتصاد جهانی هستند و باید باز بمانند، حامل رونق و پیشرفت باشند، نه خطرات جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/149414" target="_blank">📅 21:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع بلندپایه: بازگشت به تفاهم‌نامه میان آمریکا و ایران امکان‌پذیر است
🔴
پیام‌هایی میان دو طرف درباره بازگشایی تنگه هرمز در مقابل کاهش محاصره و تحریم‌ها منتقل کرده‌ایم.
🔴
تماس‌ها برای تأمین ضمانت‌ها و هماهنگی و تنظیم گام‌های میان آمریکا و ایران در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/149413" target="_blank">📅 21:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149412">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نخست‌وزیر و وزیر امور خارجه قطر در گفت‌وگو با CNN: ما دیروز مذاکرات غیرمستقیمی بین تهران و واشنگتن داشتیم و پیشرفت‌هایی حاصل شد.
🔴
ما تمایلی را در هر دو طرف آمریکایی و ایرانی برای پیشرفت در مذاکرات احساس کردیم.
🔴
ما تمام تلاش خود را برای بازگرداندن روند دیپلماتیک به مسیر اصلی انجام داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/149412" target="_blank">📅 21:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149411">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBx9FrA75TZKrk3UshYHALK8JINLhp0ZOnB8FW81lgjThqqznK_bXPtUhNXYJB0A9606u2tXm0aPGvfG54qr8wo4ctPEK0xSK7KJ8i70VT3Tft4IiPfBGgzTIChaRoqvFQjNXiFWhRhFMwWxm6pexxwFbTeAVVsO6-bf_QucWZ6bpe9HL3UrWFPcKQ0RUwfphnSXLQnlCxS-e9ajgpfBHzK5RkafttDPaP0R_Q7ZEiZf87tYlbb7UW6gBQcnBilLnqKpE-P_Sur0JgotnJLjyKd0V6AlM6W2b91rajFoAjEO6EOEmGAcOuQkvYvOLsfZ6o02Ria1iMV-SShXWwpcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار پزشکیان و دبیرکل سازمان ملل در نیویورک
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/149411" target="_blank">📅 21:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149410">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBpSQqWqmx0nW4CcQr9NQSeANmCaBqLe4lo52Zm9gzTAyhUZ9n2C3n5Rcg6jgA_ggYQ2EggKBIntqdpb1WVPKqXGa4RGAkmp9vYZ4cXyCyCY3W_O-vZS2iPFhxIvnlAkLzNMO8uaPAddwAx0kp5__FaPUKI53Km1ZlyAxyZpXON6AhokFUEen6VKrpBiJwetE4cvkFd8T0DqHw-lcerpI3YBRHKl6TdQlG55zD0TkF7GDe5jZczJD5cZQ5Zpyo7pE-UTu54m0VHSQHjA2hhzr9Ud6diBCLiLUFaPZN7byUgtlCXKKRj0bRdFe3P6pHP2-Tgw2YQ9uDPLDBSETD3gcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان بریتانیا وارد جنگ علیه یمن شده‌اند؛ به‌طوری‌که برای نخستین بار از زمان آغاز جنگ عربستان و یمن، یکی از این هواپیماها بر فراز خاک عربستان سعودی و در نزدیکی مرز یمن دیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/149410" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149409">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T16hM5k_o6_QyaQtYv-CdLQjqnX3-wOKF7XgnWjW8zwQb1lYYNER9lA_c9TcS5iRvABEww832CpyJ1JIhGP-H6B3jYgXP5Sk4kWBUEgsTbk_zCPYT4DMGMtquEBE_S7MTwmp7qJ2XNsOmSi07G_1lKTqxskK27Y-JWpjV8eTiY5u9Og8LyXm5c9iRPjdoQxyiomFM5oGVF3CG6ztXXCg6r06JT3UNyoXvo8ylmXjN3mOAUFNtWYXsr-JVJcaKVmbHJ2nMnia4ulTMCp8BZINEHM8C7QCdkD6tRe6gSrlJ3XzdR51emLkCfUL_VMKj46Ez-LO4mBTydMk_mhIsbF2_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از رزمایش موتوری امروز که طبق معمول سردار بلاگر بازهم تو تصویره
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/149409" target="_blank">📅 21:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149408">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucBhmUYg-AVspPFrtSLeP6uw2f0Gv9NTt7ZY2EQdkfA9x4Wxq1XYf3BfaIDIr0wXGbZjtVSOg-8wKmKysDLmef8iSksiLyASR4MECR-MtyyHvxPEHuZMMGesY5eEgYkC0Q6AJwli-wWIV4B5MpGNgmTl3hr86rfcJPJxwZThVKrlZBvhOzm7emhKZ5tey5da7VrcCirTcrGcirOyTclza4NS4n3sXKs41JGhMRQRNMd-8H3c4IDBFICWZturM3nHuZRms-F-5waQNPyP3ejuZOdqUBikz2tL0AJPN6jsarSbPzq_7m-Q1s3wgIfwoVgvUVMUlX3Q7YFf6mSrybzPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: رئیس‌جمهور شی و خانم پنگ همین حالا از واشینگتن دی‌سی خارج شده و در حال حرکت به سمت چین هستند. این نشست نشانی از دوستی، قدرت و موفقیت برای هر دو کشور چین و ایالات متحده آمریکا بود.
🔴
ما در ماه نوامبر در چین و سپس در ماه دسامبر در میامی، فلوریدا، در نشست G20 دوباره با یکدیگر دیدار خواهیم کرد. کارهای زیادی انجام شده و در آینده نیز انجام خواهد شد. من با اشتیاق منتظر نشست بعدی خود با آن‌ها هستم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/149408" target="_blank">📅 21:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
واشنگتن پست به نقل از مقامات آمریکایی: اسناد محرمانه‌ای که به کنگره ارائه شده، نشان می‌دهد که عربستان سعودی احتمال توسعه یک برنامه تسلیحات هسته‌ای را منتفی نمی‌داند
🔴
این موضوع نگرانی برخی از نمایندگان آمریکایی را در مورد موافقت ترامپ با کمک به آن‌ها در ایجاد یک برنامه هسته‌ای غیرنظامی افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/149407" target="_blank">📅 21:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149406">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر خارجه عراق: ما با هماهنگی آمریکا از طریق تنگه هرمز نفت خود را صادر می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/149406" target="_blank">📅 21:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149405">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
اکسیوس به نقل از یک منبع مطلع:
قطر و ایران منتظر دریافت پاسخ ترامپ به پیشنهاد ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/149405" target="_blank">📅 21:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149404">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bccf790968.mp4?token=jkmfT8ykfKOiG7sIEubt6BicUt7XOT008H1VPTZdpL1HDFojOMcxnVFaUu-I67GN7DXSF9b6k7cWeoInz3SFPAr-RuDeZwUGzrYArspGY2uLDj7Ctk0Gw2-WgZKUKpr_l0mEFow4RCORtPS5Sndss9wA1FaSqe_XmBGDJtP6_kat5E3vHv7Le-cP3yXef5TuiNIsqrwvfgbaTbDJa-4kRKM29S2DjejClIswprzdoswpDtfrnX5gn0-J-0csl-MKSN_vOSG98S0zypEYQtaKeKkd8_qZbW5QGgLoCptnwamreK9gBV4arP1jFOeGOnEf-iSqsBQmga5WH65a6UYtFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bccf790968.mp4?token=jkmfT8ykfKOiG7sIEubt6BicUt7XOT008H1VPTZdpL1HDFojOMcxnVFaUu-I67GN7DXSF9b6k7cWeoInz3SFPAr-RuDeZwUGzrYArspGY2uLDj7Ctk0Gw2-WgZKUKpr_l0mEFow4RCORtPS5Sndss9wA1FaSqe_XmBGDJtP6_kat5E3vHv7Le-cP3yXef5TuiNIsqrwvfgbaTbDJa-4kRKM29S2DjejClIswprzdoswpDtfrnX5gn0-J-0csl-MKSN_vOSG98S0zypEYQtaKeKkd8_qZbW5QGgLoCptnwamreK9gBV4arP1jFOeGOnEf-iSqsBQmga5WH65a6UYtFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پایان سفر شی به آمریکا
🔴
ترامپ و شی با یکدیگر خداحافظی کردند، چرا که شی بازدید سه روزه خود از ایالات متحده را به پایان رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/149404" target="_blank">📅 20:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149402">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نیویورک تایمز: نتانیاهو از عملیات هفت اکتبر خبر داشت
‏
🔴
نیویورک تایمز گزارش داد که محمد بن زاید (MBZ)، رئیس‌امارات، پیش از ۷ اکتبر به نتانیاهو هشدار داده بود که حماس در حال آماده‌سازی یک حمله بزرگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/149402" target="_blank">📅 20:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149401">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wqnnb6SBxpby5et0Qc5nIYlotkZrpMCrtZ3Z3PPlJo5U_6DUMiL5uRzBML23BhWptXWMlNzUjZytkzKs6H22rz1VPROCi0rJu99_2qoAl-YCAgq7LFxMyCkFeFH7ZhyylIzGR4jKjSl5Rff_i8ruZusOwjKntx2vQQ3rCqF0t1uRs-T8-C3Cvxg9Q2z-vJ4QEri65v5JdMVjO1RcprrRbv4wEYIWWbpFZZBK_sASfMDcsiIkGgvtwxq7PnxRx2V2cUGF90cpfVvjjGaQCp0vOE8rMXvAKHQoLnPpT3nwplJ02RKIdI_dt-BFIcklSVb_a-6SnZt5_aWUrAT2NADz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه، گفت که از رابطه شی جین‌پینگ، رئیس‌جمهور چین، با ترامپ حسادت نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149401" target="_blank">📅 20:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149400">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سنتکام: تا کنون مسیر ۱۲۲ کشتی تجاری به سمت ایران را تغییر دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/149400" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149399">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مقام ارشد ایرانی به رویترز: حتی در صورت پذیرش پیشنهاد تهران درباره هرمز، امتیاز هسته‌ای نمی‌دهیم
🔴
یک مقام ارشد ایرانی به رویترز گفت: «حتی اگر آمریکا پیشنهاد تهران برای بازگشایی تنگه هرمز را بپذیرد، ایران هیچ امتیازی در موضوع هسته‌ای نخواهد داد.»
🔴
این مقام افزود: «تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته خواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149399" target="_blank">📅 20:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149398">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره:
پس از نخستین دیدار میان استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، کارشناسان فنی نیز به مذاکرات در نیویورک پیوسته‌اند.
🔴
اگرچه دولت آمریکا در ابتدا برای هیئت ایرانی روادید صادر نکرده بود، اما این روادیدها به‌سرعت صادر شد و به هیئت ایرانی اجازه داد به مذاکرات ملحق شود
🔴
طرح پیشنهادی ایران برای بازگشایی تنگه هرمز طی هفت روز، در صورت کنار گذاشتن محاصره از سوی آمریکا، در حال بررسی است.
🔴
این طرح نسخه‌ای تسریع‌شده از روند ۶۰ روزه‌ای خواهد بود که پیش‌تر درباره آن گفت‌وگو شده بود و شامل اقدامات فوری برای بازگرداندن دو کشور به مذاکرات مستقیم درباره برنامه هسته‌ای ایران خواهد شد.
🔴
مهم‌ترین مطالبات ایران که در حال حاضر در مذاکرات مطرح است، شامل رفع تحریم‌ها، لغو محدودیت‌های صادرات نفت و دسترسی به منابع مالی بلوکه‌شده ایران است.
🔴
دو طرف همچنین همچنان درباره ترتیبات مربوط به تنگه هرمز گفت‌وگو می‌کنند؛ از جمله این موضوع که آیا ایران و عمان می‌توانند تحت چارچوبی مورد توافق که کشورهای منطقه و آمریکا نیز در آن مشارکت داشته باشند، به نوعی از مدیریت مشترک تنگه بازگردند یا خیر. همچنین ترتیبات مربوط به عبور و مرور کشتی‌های آمریکایی از تنگه نیز در دست بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/149398" target="_blank">📅 20:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149397">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3acdf0c4.mp4?token=vXHg-VA6OWSvAkzv81-6BG9R4TLLkEJpyOOynmarrG18lPmudPsdYq8L3OTMQF_uX8Jo0lzSpUrzD8yjil-hcgNOOws1n0-inPlZvDranAjG0ubI5Z7mNsxWLHrLYltcCTdzguzVp_DdiaeR_TySxvEklPZYzb0tJhEoKXFySXnz87hH8dRk_6kwV6oanLiCIK1NBUtyqvQ52kc3TJyZkcpvvkAY0NFz36aKnJQ-D7xkpb1-GBJTGI8ApKbVwoqUriqfJbwiYm0Zf9UP0EffTjdgIzdkpUywY5zOK6y92ME89fE4ytL8_7p7KVWCy7ZS1HDtZoHMvcxT8Fl0s7pkCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3acdf0c4.mp4?token=vXHg-VA6OWSvAkzv81-6BG9R4TLLkEJpyOOynmarrG18lPmudPsdYq8L3OTMQF_uX8Jo0lzSpUrzD8yjil-hcgNOOws1n0-inPlZvDranAjG0ubI5Z7mNsxWLHrLYltcCTdzguzVp_DdiaeR_TySxvEklPZYzb0tJhEoKXFySXnz87hH8dRk_6kwV6oanLiCIK1NBUtyqvQ52kc3TJyZkcpvvkAY0NFz36aKnJQ-D7xkpb1-GBJTGI8ApKbVwoqUriqfJbwiYm0Zf9UP0EffTjdgIzdkpUywY5zOK6y92ME89fE4ytL8_7p7KVWCy7ZS1HDtZoHMvcxT8Fl0s7pkCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی عجیب قائم پناه معاون پزشکیان از برش دادن کیک ۹۶امین سالگرد تاسیس سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/149397" target="_blank">📅 20:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZ37ABgVsisp1BniNGZebDaon9ABNqGdE5vqitWx3i3Om2JSC_D7gzDAZPQXmQ3g38wmrYZ8FfWWvLBneszEN0-GPo4LdmxpdodV0fX46Y23aHVAb6311rsZ5RKzRU3zDtuTNnScoUoX1v0Jv119xZHMQGyDdgT2y4FJQK-GFTUVToNmv2qrHd6HdbTD4atmOiDeAZCEaeIRBVGPtR4iNRvSF772axkE2L6J7u_H14oWpF35_BLiOGDimrWo9z5BQdlrCG50HFCyetGNjOiEmshAhi24tsnf8VMDj9L0LdrKNoYZW0K7fekkkUuhVBoEg5FsJMATRolKEIvtzKB2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOfD56UIpbo2-wpz80WEPHKrF4nJEFx9mr77NmY2HSKZwaUhzFGpcLHRU2rX5wPzkn-AtAtZlLYhLrLIaHBiC1MdCkkAFHW7O1LEJrIeAKG91jvcBJ3Hz331KlLRf_1IgIGk2-42FyZdUaTp9KggXlXSrHgTxEUv49xJmzWSs1yhMm0BkzWyxTB10nSKsGCltQU7WldV-arQDLv3nKvDrAb01QFllnwvUpzsdIqWuA3CkcooQ8ucxIj0xUaF3Vrkzqdv8T3AlAqf4ldo8xy45L3aZD_fq5C05iZOwjMpR7WHFJ_JxF2d8vniSGxelRgqP_l0xfy3tiuzt1g12CxPMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار فرماندهان ستاد‌های ارتش عربستان، پاکستان و ترکیه در ریاض جهت مقابله با حوثی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/149395" target="_blank">📅 20:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43bbf6157d.mp4?token=gCAN634ZQFci-88X9AroRqIz-fqws0hr2gC2YDRnRYoApBMur-Xo7c6JPL0_L_NB8jxT6b0sL_fmyN2repANGYyt31yyRlXGMlv_Dt3Bji50JdQN5324GFj3JDHAV2DM86khGVim3m01K-ipp2w6y0k7-6CcdG-gqQORmiLxAmAIO3aKD0kQr8X7hWvi7wre-iDmGNNqG824VAuaSPG73AjHR87DKBfsADQjZbMFU0vqhfUxANpz1wd0rZdKzlDjPC4lZ7LeFZDIP2TgbM8k4U5rMTDLLg1le9Y125G_GEbss8myMhZbCvHJ4Y7JWYTgdUqKlLayeu9FyZWgoLj0iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43bbf6157d.mp4?token=gCAN634ZQFci-88X9AroRqIz-fqws0hr2gC2YDRnRYoApBMur-Xo7c6JPL0_L_NB8jxT6b0sL_fmyN2repANGYyt31yyRlXGMlv_Dt3Bji50JdQN5324GFj3JDHAV2DM86khGVim3m01K-ipp2w6y0k7-6CcdG-gqQORmiLxAmAIO3aKD0kQr8X7hWvi7wre-iDmGNNqG824VAuaSPG73AjHR87DKBfsADQjZbMFU0vqhfUxANpz1wd0rZdKzlDjPC4lZ7LeFZDIP2TgbM8k4U5rMTDLLg1le9Y125G_GEbss8myMhZbCvHJ4Y7JWYTgdUqKlLayeu9FyZWgoLj0iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار خطاب به ترامپ: آیا درباره جنگ با ایران با رئیس‌جمهور شی گفت‌وگو کردید؟
🔴
ترامپ: بله، صحبت کردیم. فکر می‌کنم قرار است اوضاع خیلی خوب پیش برود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/149394" target="_blank">📅 19:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149393">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f22063209.mp4?token=MADq7QiR-bevNMO-GGSCREFcLn7Wga-mzyy1uuQjmo0I1NygUHX2Iy1G_8B8fxE3p3j_xWJNoo6rj4dJx7v0B2UFP-GQ7pCv1ircXwI2Nypq-Fl0VIZdzK4yFbbe28rpMGvQSBFGZ-0TTY9AGnP45nwUZIRsBC0DeLTyHe-vxzY1T7dcgVi2j2x0PK-Jb5vlRNTYztQcbL_OMsstY2HheH2SUAoe4hoA4a3ufBix4Fql4zof5ZFvz7Veoevr98D755zUU7m6FcHiKo-xeeYfpe3oWl0waz3G5E1WHFx1asROlyN8faOEAZUAjJSB_P2zwG5KtxmrRQl_gRlnyVogLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f22063209.mp4?token=MADq7QiR-bevNMO-GGSCREFcLn7Wga-mzyy1uuQjmo0I1NygUHX2Iy1G_8B8fxE3p3j_xWJNoo6rj4dJx7v0B2UFP-GQ7pCv1ircXwI2Nypq-Fl0VIZdzK4yFbbe28rpMGvQSBFGZ-0TTY9AGnP45nwUZIRsBC0DeLTyHe-vxzY1T7dcgVi2j2x0PK-Jb5vlRNTYztQcbL_OMsstY2HheH2SUAoe4hoA4a3ufBix4Fql4zof5ZFvz7Veoevr98D755zUU7m6FcHiKo-xeeYfpe3oWl0waz3G5E1WHFx1asROlyN8faOEAZUAjJSB_P2zwG5KtxmrRQl_gRlnyVogLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بازم عجیب اما واقعی
‼️
🔴
عده‌ای بیکار و علاف هم جلوی منزل حسن روحانی تجمع کردن و خواستار محاکمه وی شدن
🔴
این جماعت معلوم نیست از کجا کسب درآمد دارن که هر روز ول میچرخن به یکی گیر میدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/149393" target="_blank">📅 19:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149392">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f93e70ab2e.mp4?token=QHLYIsu4As3Rh_TZ5r_NvcPgJqn698RB_IdVH4vSoricJ91_MY4atRcESpsFESV6qJQEwxWeienoAI9-X7YV5iYe2q202zinUPwAG1c4RXCZYYnY_PhB6cgR2gyOuyJuoWPw0uKs7HyfNBrmf1W7z0LNJMAeSMQwAGhz3ka_e3QROkpPKc56YxC7jD2xymDYWIXU8WlOw9XCIAgfDJl7ig-MsMzJqjBGQHAtFVVyg2DNJsOp5Ta1hIKEcHFSv_nLgxuHSQQdW7uY5Z2DSxYHzQ9UNeRfX2oKxgGPWDhs2uMJ2WEbn77ISCNC1zChytUb0BERihtB4gKUST4ij0KHwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f93e70ab2e.mp4?token=QHLYIsu4As3Rh_TZ5r_NvcPgJqn698RB_IdVH4vSoricJ91_MY4atRcESpsFESV6qJQEwxWeienoAI9-X7YV5iYe2q202zinUPwAG1c4RXCZYYnY_PhB6cgR2gyOuyJuoWPw0uKs7HyfNBrmf1W7z0LNJMAeSMQwAGhz3ka_e3QROkpPKc56YxC7jD2xymDYWIXU8WlOw9XCIAgfDJl7ig-MsMzJqjBGQHAtFVVyg2DNJsOp5Ta1hIKEcHFSv_nLgxuHSQQdW7uY5Z2DSxYHzQ9UNeRfX2oKxgGPWDhs2uMJ2WEbn77ISCNC1zChytUb0BERihtB4gKUST4ij0KHwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
امروز بسیجی‌ها به یک جوان که پرچم آمریکا رو پیراهنش بود وحشیانه حمله کردن
#بی_شناسنامه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149392" target="_blank">📅 19:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149391">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2c9f2c38.mp4?token=e8_T6Mhyl4cO_JfYuEwL3s5KBcgrQt1DpVQR0huf7trpoqowlOCvXhEjaW3ulOPLsDjTSvHRFjfd98mmwUKLdFyquWmQk1v6SFAQjrm4p6G9WuNZFwDpxGhrZMuokDLwvicsI4nB6oXKVafj1ksyaTPu_15AZMBwrO2ISVvDdDG5B-TsKSYCecVlr_ZVhmbCxPfSzvcPz7csK1C6fCiQ8CASdIisUTiJWE8AK8u5Ygi-OAepONVnJbwuC8Ps28sSIiMk3L_f6xhceCJVbH7mABomdTZVbZ5VA9HD0FDA57lPpj-3UUuyCy0DK5tpyfHmRadrPSwgNXPnG0kxIf_c-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2c9f2c38.mp4?token=e8_T6Mhyl4cO_JfYuEwL3s5KBcgrQt1DpVQR0huf7trpoqowlOCvXhEjaW3ulOPLsDjTSvHRFjfd98mmwUKLdFyquWmQk1v6SFAQjrm4p6G9WuNZFwDpxGhrZMuokDLwvicsI4nB6oXKVafj1ksyaTPu_15AZMBwrO2ISVvDdDG5B-TsKSYCecVlr_ZVhmbCxPfSzvcPz7csK1C6fCiQ8CASdIisUTiJWE8AK8u5Ygi-OAepONVnJbwuC8Ps28sSIiMk3L_f6xhceCJVbH7mABomdTZVbZ5VA9HD0FDA57lPpj-3UUuyCy0DK5tpyfHmRadrPSwgNXPnG0kxIf_c-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
گسیل ترابری های نظامی ایالات متحده به خاورمیانه جهت امضای توافق
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/149391" target="_blank">📅 19:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جررررررررر
🤣
سفیر اسرائیل رفته استارلینک رو تحویل نماینده ج.ا بده نماینده ج.ا هم عین دخترا قهر کرده و اونور رو نگاه میکنه
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/149390" target="_blank">📅 19:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏
👈
رهبر مذهبی عربستان سعودی در بیانیه ای بی سابقه از تمام مردم عربستان خواست برای جنگ با حوثی های یمن آماده شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/149389" target="_blank">📅 19:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHYZvoRQxMmBMu4OzgjP9lpCtwyUAAqTKNSm5FTS7bwQWy6d2flK6IbmfmUruvAkhcROxNNKTIF8BBNabuhnXAtYhLfTfrs-B44tfjKpU6i3gSuZWPL5zpcRJRZbrwCgLwukNTFr07xcoTxtZ1_WuY6XBhx4_ZxlFci_gn1XdHsF88HfdJY4UtbM3gue95s6IuP66sax4ylvinbOOx_-5_Ij0d0WbkD2c_X5J53NJIFDh2nGKcn8M_zPlHM-rgGH1DLrejvBbA9Ma5_5p2MpI3AgGnSNgo-9aNudUi6h8fZ2HuCzlfHmLmqHi_kqeizCwba_E6cmoHOB6SePSEu97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
دیروز تو تهران 96امین سالگرد تاسیس پادساهی سعودی جشن گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/149388" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فایننشال تایمز: حوثی‌ها به اروپا تعهد دادند کشتی‌های اروپایی را هدف قرار ندهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149387" target="_blank">📅 19:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149386">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0d77058e.mp4?token=DOwXIg4wLo3ZPBmUVVXBwYZL27_6P42iFyveXhJobJtwH71hfsN3ZDJnQhWnwqnVhO0q9b9-cfHTTbOBIJ2xKvRKLeeHdmp0UCFNogoOJj8v2716ru1ESXroE7fYPgFfOhqoFEugcz-tly-wYCmpx_COhrra3L_vyCELmsg94z2KgkwW-pnK5PaULlv6GaFkcOBmxzgXTwpNJxW0ewEv9Gwx17SKHbPyFy0aZrpCv0dYUWuMgPR879PnJLMOqYpvOJpZ6Cms-WEcqHI1LcHn7Ul_1-f3aLKDLgQg4yGWSwGnbnMnGOh_Z6ezXFTfYlDno1WcHzRaDUXkOZCewePlOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0d77058e.mp4?token=DOwXIg4wLo3ZPBmUVVXBwYZL27_6P42iFyveXhJobJtwH71hfsN3ZDJnQhWnwqnVhO0q9b9-cfHTTbOBIJ2xKvRKLeeHdmp0UCFNogoOJj8v2716ru1ESXroE7fYPgFfOhqoFEugcz-tly-wYCmpx_COhrra3L_vyCELmsg94z2KgkwW-pnK5PaULlv6GaFkcOBmxzgXTwpNJxW0ewEv9Gwx17SKHbPyFy0aZrpCv0dYUWuMgPR879PnJLMOqYpvOJpZ6Cms-WEcqHI1LcHn7Ul_1-f3aLKDLgQg4yGWSwGnbnMnGOh_Z6ezXFTfYlDno1WcHzRaDUXkOZCewePlOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در دیدار با شی جین‌پینگ: این سفر برای آمریکا و چین بسیار ثمربخش بوده است
🔴
دونالد ترامپ در جریان استقبال از شی جین‌پینگ، رئیس‌جمهور چین، در کاخ سفید گفت: «آمریکا از این سفر بسیار خرسند است و مطمئنم چین نیز بسیار خوشحال است.»
🔴
او افزود: «اتفاقات بزرگی برای هر دو کشور در پیش است؛ این دیدار بسیار ثمربخش بوده است.»
🔴
ترامپ هنگام استقبال از شی جین‌پینگ به پرسش‌های خبرنگاران پاسخ نداد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/149386" target="_blank">📅 19:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149385">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/149385" target="_blank">📅 18:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149384">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نفت خام برنت ۱۰۶ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/149384" target="_blank">📅 18:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149383">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee60910e82.mp4?token=l7e_2uWPACQQOv57W_p9aNz9oiC_dzMJNZeJs0Vv-LWgvme99O6-uzAg6ST7nOHb-EWPQrPnGY1ujAcVdolRGrXwkjmX0J9pWFvmTIuxlc7RT-slNo8uBONrjEddojKAE3SZKeySsLCHW2nDxPtEYb2W59A9WwCZ1FTuw4OrSxD34a-FUPhle8tFXTd_EW_PtkHP6XY9LjKjNptsBKCy8v5RKOT5602_9vGBkBBKWMmrqa4JOPiCHYZXqf9gtZcHdrs5cNy91QxBIOjgJnsrM3Exxy2Gmz1P0ediHKDK9JUrIYZtTO4pYCvxSXC5v5Cm5IF9Grl_G3ki5JUJrzsS5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee60910e82.mp4?token=l7e_2uWPACQQOv57W_p9aNz9oiC_dzMJNZeJs0Vv-LWgvme99O6-uzAg6ST7nOHb-EWPQrPnGY1ujAcVdolRGrXwkjmX0J9pWFvmTIuxlc7RT-slNo8uBONrjEddojKAE3SZKeySsLCHW2nDxPtEYb2W59A9WwCZ1FTuw4OrSxD34a-FUPhle8tFXTd_EW_PtkHP6XY9LjKjNptsBKCy8v5RKOT5602_9vGBkBBKWMmrqa4JOPiCHYZXqf9gtZcHdrs5cNy91QxBIOjgJnsrM3Exxy2Gmz1P0ediHKDK9JUrIYZtTO4pYCvxSXC5v5Cm5IF9Grl_G3ki5JUJrzsS5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ و شی در حال چای خوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/149383" target="_blank">📅 18:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149382">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
کارشناس نظامی صداوسیما: در روز های اخیر پرواز هواپیماهای جاسوسی و شناسایی آمریکایی اطراف ایران بسیار افزایش پیدا کرده است که نشان دهنده یک حمله قریب‌الوقوع احتمالی به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/149382" target="_blank">📅 18:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149381">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc1yUKHrfPcH3-DzCC_t3Oe73FXLROmMdWt4w8e_WB8KAT0wBGhsGj_AKOsCW6w9_pXS-tAiVZcsb-qkWEna_-2ASV1slsunEczkTUvuyL6BILQIkSsTm4j70DAtKDWoJ6PW4EQvGCVnVaq43_tx0qo6btd6kpvu0BHe0kwgbxCIv7H8zHTsRltxMvTwt0k0d3tulAFQfn_U4QzdxLN38hhitDK_a04NsyzK4f7_gsS9r4kPFjlqSNQBhNX1INkOhpH9_zE77J5NdaabGRxLingndl_2lsdj2y63PXFhhm2nT76EfXOROOeWRsmstEDTa_-_8G8uXEE7oWlLmz7uEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
عراقچی و پزشکیان باید استیضاح بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/149381" target="_blank">📅 18:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149380">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZQVUK_DtOh6fKTnnyNBPlgziQPekTxZDH-uFpGTKXwKVxfo0mvyjUbZo9loAlBYAa0rzjjGp84DJHVumLF1hrCYUKKh2CqJhrKUpmMxezSjq3gtLZ_1XBvb55lTZNgTpTsdYshe_GOvm2UI48ObRuRdVn0mVDLI-_NhDdWx8pjYp0ZC7tlDgU1b9vAM_aBFZYSalwwxG7TxaDg5cTnB5JYdvnrpvB9pWF7ANgNg_sXZiPcUNGI3fvyLsyINF3Gry7fN8bXhPek7BOD_Lzl0lsh5dc4HvGanqQHO8Dv4eVYRhc7-hskalbtehGkFBct1JrhHCBFkiHkGcJ9-tj7Xdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:
«محاصره هوایی ایران» (لغو شدن پروازهای ایران به کشورهای همسایه، منطقه و دیگر نقاط دنیا)، پیوستِ «محاصره دریایی» است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/149380" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149379">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ و همسرش، ملانیا، از رئیس جمهور چین، شی جینپینگ، و همسرش، پنگ لی‌یوان، در کاخ سفید استقبال کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/149379" target="_blank">📅 18:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149378">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان: ترامپ آمار اشتباه می‌دهد؛ تعداد افرادی که جانشان را از دست دادند ۳۰۱۵ نفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/149378" target="_blank">📅 18:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149377">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
روزنامه اسرائیل هیوم: نمایندگان آمریکا در مذاکرات با ایران در سازمان ملل به ترامپ اطلاع دادند که تهران حاضر به مذاکره درباره برنامه هسته‌ای خود نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/149377" target="_blank">📅 18:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149376">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مجری فاکس: شما میخواهید بمب بسازید؟
🔴
مسعود: نخیر نخیر
🔴
مجری فاکس: پس چرا اورانیوم بردید تو دل کوه؟
🔴
مسعود: اون داستان داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/149376" target="_blank">📅 18:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149375">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
پیش بینی پشم ریزون قیمت دلار توسط نوستراداموس ایرانی</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/149375" target="_blank">📅 18:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر خارجه اوکراین: دیدار با عراقچی مفید بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/149374" target="_blank">📅 17:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149373">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وال‌استریت ژورنال : پس از تلاش قطر برای برقراری دور جدیدی از مذاکره بین ایران و آمریکا ، دولت آمریکا به قطر اعلام کرده است که ترامپ قصدی برای لغو تحریم یا محاصره دریایی ایران ندارد.
🔴
یک مقام کاخ سفید نیز گفته است تحریم‌ها و محاصره دریایی، آمریکا را در موقعیت قدرتمندی در برابر ایران قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/149373" target="_blank">📅 17:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149372">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سی‌بی‌اس: ارتش آمریکا در حال زمینه‌سازی برای اقدام احتمالی در کوباست
🔴
ارتش آمریکا در حال بررسی این است که کدام واحدها می‌توانند از عملیات بالقوه علیه کوبا در چند ماه آینده پشتیبانی کنند
🔴
واحدهای درخواستی شامل یک گردان پشتیبانی رزمی، تیپ پزشکی، دسته جراحی پیشرو و یک تیپ پلیس نظامی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149372" target="_blank">📅 17:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149371">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
توقف فروش بلیت پروازهای عراق تا اطلاع ثانوی
🔴
سازمان هواپیمایی کشوری: در پی توقف پروازهای اشرف از صبح امروز، این سازمان به شرکت‌های هواپیمایی ابلاغ کرده است نمایش و فروش بلیت این مسیر برای امروز و روزهای آینده تا اطلاع ثانوی متوقف شود.
🔴
شرکت‌های هواپیمایی موظف‌اند وجوه بلیت پروازهای تعلیق‌شده را در اسرع وقت و به‌طور کامل، بدون کسر جریمه، به مسافران بازگردانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149371" target="_blank">📅 17:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149370">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ulubd6Pn-UdIfRGt11oRheh5bbM7EFCbtFIb35N9BCnMyR3v24X_z0h_05IyO99k99tzLiuE_HqYh5sMxjVXl23N2YXDIYw1-VKZ1Dfq1rqHWX2wbKltVsroCDA649XtIKFaflpNXggESefbRPVz3wDk73O06engpiBhTQea3ixL5aQ_AQz_dmlAGJCtkKyYuoFQPG9vvuiwQ600hktH8uNXYaEPw1vvBBwit7UtMwS_w0h2NsKkCSFUzSYyHqTUsMZQB-BxeYOA-IRA6waW7PcQVJp4g4KNrTgfS_9LRRg_jjjaBhApYWWJVsYQz1mNjcaZ3UCD5KvrEQTiJsYJ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلبری جانفدایان خانم با موتور و کلاشنیکف
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/149370" target="_blank">📅 17:16 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149369">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqUAltKxaVIWq05S4lw6QulSLHqjJqxT_BQWhgnXRVcNtNRC4XDsX06N9ql9fQMh6-9sVEPJq6zFnj-T1hN8mnD-WuQYYy71jEeRi8-tsm2TLItAPEz7Cj2xHsjJ1zKiRwVMs3RLdrekiOaJ-CuzIO5OemLcuUzPA3tHfzJw4MC1yOvw53jM877ZUWhJpacYlCI14yHIQ6BWuQHX5mzj6N22-rlWFrwGHTftpAxjV8dG5dp0Nx8UeW1F_tBeZsBeULdooteunA05vlT-_4qHgpiIbVnxg8ruDjsjzXS9IW_6_gwIhvUgl5IQuBRNYOiQrlJF93lDMySp0Ola9szL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا پزشکیان به دلیل تحریم هوایی تو آمریکا گیر افتاده و حالا حالاها نمیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149369" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149368">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پزشکیات در گفتگو با فاکس‌نیوز:
ما اصلاً کاری به انتخابات آمریکا نداریم.
🔴
اگر آمریکا برای گفت‌وگو بیاید و حق و حقوق ما را در چارچوب قوانین بین‌المللی به رسمیت بشناسد، آماده گفت‌وگو هستیم.
🔴
اگر نخواهد این حقوق را ببیند، چه قبل از انتخابات باشد و چه بعد از آن، برای ما چه فرقی می‌کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/149368" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سفیر آمریکا در چین: طرف چینی در مذاکرات روز پنجشنبه تأیید کرد که از ایران حمایت نمی‌کند/پکن با ما موافق است که ایران نمی‌تواند سلاح هسته‌ای داشته باشد و تنگه هرمز باید باز بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/149367" target="_blank">📅 17:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
در گفتگو با فاکس‌نیوز؛ پزشکیان درباره جزییات جلسه هیئت ایرانی با کوشنر و ویتکاف:
🔴
آنچه درباره‌اش بحث می‌کنیم، چارچوب قوانین بین‌المللی و حق و حقوقی است که باید داشته باشیم.
🔴
ما چیزی غیر از حق و حقوق خود در چارچوب قوانین بین‌المللی نخواسته‌ایم و نخواهیم خواست.
🔴
در نتیجه، بر همین اساس در حال تفاهم هستیم، اگر طرف مقابل بپذیرد.
🔴
پزشکیان درمورد منشأ اصلی نقض تفاهم‌نامه: مشکل این است که وقتی کسانی که یک عمر مسئول آن تنگه [هرمز] بوده‌اند، نتوانند کشتی خودشان را از آن منطقه عبور بدهند، طبیعتاً برای کشتی‌های دیگر هم حق عبوری نخواهد بود.
🔴
الان آمریکا نمی‌گذارد کشتی خودمان را از آنجا عبور بدهیم. به چه دلیل آمریکا آمده آنجا و اجازه نمی‌دهد؟ مگر کشتیرانی آزاد نیست؟ چرا راه ما را بسته است؟
🔴
پزشکیان در گفت‌وگو با فاکس‌نیوز:
مشکلی که در منطقه وجود دارد، نوعی عدم هماهنگی میان آمریکا و کسانی است که در منطقه و در ایران باید در چارچوب آن تفاهم‌نامه با هم کار کنند.
🔴
در اجرای آنچه در تفاهم‌نامه نوشته شده، سوءتفاهم‌هایی به وجود آمد. این سوءتفاهم‌ها، به جای اینکه پای میز مذاکره حل شود، به درگیری کشیده شد و همین، کل تفاهم‌نامه را زیر سؤال برد. اگر بخواهیم بر اساس تفاهم‌نامه عمل کنیم، طبعاً ممکن است در طول مسیر مشکلاتی هم وجود داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/149366" target="_blank">📅 17:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=ZMCeq6xxgMZJ9umCMenZrae_jplUmeSBlUmCbgl-AASaHgKWurHID6maqDoc3VaOSPOZoJ-yDCiazQAS8SJvd4ULUcsy2mVZWtwW8gvgdXnEGg84hNcpAXaM67jKs_wBbEkUL0_qnzvs7izXvqE1h8QF_Z7g26fgbaUPYqIdqMd-odaDTCpiZcegAdLegO2Hond_dusTUkTUMa0XaReU7LQShPE3_D5_Se8n2W-TUw-VvYux2p6YshAgJAeGfRO9KmYr3446x_0WVwiSq68bq_0iwWj8bfcombnDImoAXAQx9bDi1gbQshpkw_UErlHSt8Plp8d0m9jR8gxW-e9z0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=ZMCeq6xxgMZJ9umCMenZrae_jplUmeSBlUmCbgl-AASaHgKWurHID6maqDoc3VaOSPOZoJ-yDCiazQAS8SJvd4ULUcsy2mVZWtwW8gvgdXnEGg84hNcpAXaM67jKs_wBbEkUL0_qnzvs7izXvqE1h8QF_Z7g26fgbaUPYqIdqMd-odaDTCpiZcegAdLegO2Hond_dusTUkTUMa0XaReU7LQShPE3_D5_Se8n2W-TUw-VvYux2p6YshAgJAeGfRO9KmYr3446x_0WVwiSq68bq_0iwWj8bfcombnDImoAXAQx9bDi1gbQshpkw_UErlHSt8Plp8d0m9jR8gxW-e9z0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کشتی باری-مسافری Blue Car Carrier II با پرچم یونان در شمال جزیره میکونوس دچار آتش‌سوزی شد
🔴
این کشتی ۲۹ سرنشین و نزدیک به ۲۰۰ کامیون و خودرو داشت
🔴
بر اساس گزارش‌ها، مصدومی گزارش نشده و مسافران در حال انتقال به جزیره تینوس هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149365" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
فایننشال تایمز: حوثی‌های یمن به اتحادیه اروپا اعلام کرده‌اند که کشتی‌های اروپایی در دریای سرخ را هدف قرار نخواهند داد و گفته‌اند عملیات آنها علیه عربستان سعودی است، نه برای مختل کردن کشتیرانی بین‌المللی
🔴
حوثی‌ها همچنین پس از مذاکرات با واشنگتن با میانجی‌گری عمان، به آمریکا اطمینان داده‌اند که کشتی‌های آمریکایی را نیز هدف قرار نخواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/149364" target="_blank">📅 16:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e6ed712f.mp4?token=hcDuvOp9l1qDaHJGmxRjMxvt_NhPmXtsChtwSK_XJ2r1PDCz6Ga8nCjhrrXFqT_T6_msESSVWOK_j3k5f2fF3hmQ0lSp3503zqr7rqxP7Z3BxtxmROdJM25TeMqvvrN6wx5LC7KjkgtkGh8mjUQ8_Fra5Niywk5N0GVY_6Vb-xSRyLmlgA9SNizmOuK53ADQM7Jiz403QlrKi1vL_7aJzd-rrKmn3mI9i9N1A9XkeBUO0ky1iOjC9WzobV0AjjTfL4pVVFCsa0bR9TYxsXDVIUW2nSBt1kgk0FmHjIUA2_xuO7gYN8GZ9A5RVYNJicmnAY7xieD5z9GiRa0Ct_QbqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e6ed712f.mp4?token=hcDuvOp9l1qDaHJGmxRjMxvt_NhPmXtsChtwSK_XJ2r1PDCz6Ga8nCjhrrXFqT_T6_msESSVWOK_j3k5f2fF3hmQ0lSp3503zqr7rqxP7Z3BxtxmROdJM25TeMqvvrN6wx5LC7KjkgtkGh8mjUQ8_Fra5Niywk5N0GVY_6Vb-xSRyLmlgA9SNizmOuK53ADQM7Jiz403QlrKi1vL_7aJzd-rrKmn3mI9i9N1A9XkeBUO0ky1iOjC9WzobV0AjjTfL4pVVFCsa0bR9TYxsXDVIUW2nSBt1kgk0FmHjIUA2_xuO7gYN8GZ9A5RVYNJicmnAY7xieD5z9GiRa0Ct_QbqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی طائب: «حضرت موسی ساخت بی‌سیم را به یهودیان یاد داد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/149363" target="_blank">📅 16:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149362">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6hupJY7LSTeTE26ZwqNBA5tPivAovQ73IsJe8cGiq7VBFHntI3ClhxGO_Z96ydyDu3W63namVHV2RNIwF4bMNBuCok0DPQtLOm0CJy4RbQKuYo3pBUqx5WQAPogjL4VDaPhryDN0eTaz-d2t2gHhI2wg150ZhibRb_vqrc6Eiv83D8sIm7LdIkHVTqpAuNPzwB2WuWANlqTRwCqKpUDAaIsjE9ceuqvtam9fDQAOlrmkIYA7ggcFY0gELatq61aVoWxfQo07Ew_7wRMjC4frBKS3qOYQCBU-C19gSa_OHjiS6uoVR4mjgcaY1Osb8rayKCiRs0HSjhEsj42fjUgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به فارسی:
یه خبر خوب.حکومت شرور جمهوری اسلامی سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/149362" target="_blank">📅 16:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149361">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
رئیس جمهور ترکیه، اردوغان:درست نیست که به پیمان دفاع مشترک که در مکه منعقد شد، به عنوان یک ائتلاف تأسیس‌شده علیه ایران، اسرائیل یا هر کشور ثالث دیگری نگاه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/149361" target="_blank">📅 16:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149360">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⛔️
پیش بینی دقیق طلا و دلار توسط نابغه دانشگاه شریف
😳
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/149360" target="_blank">📅 16:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149359">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
الجزیره: عاصم منیر به‌زودی برای نشست با همتایان سعودی و ترکیه‌ای خود وارد عربستان می‌شود
🔴
انتظار می‌رود فیلد مارشال عاصم منیر، رئیس ستاد نیروهای دفاعی پاکستان، به‌زودی وارد ریاض شود تا در نشست پیش‌تر اعلام‌شده با همتایان سعودی و ترکیه‌ای خود شرکت کند.
🔴
این نشست در چارچوب توافق دفاعی مشترک مکه برگزار می‌شود
🔴
الجزیره از روابط عمومی نیروهای مسلح پاکستان، نهاد رسانه‌ای ارتش این کشور، درباره اینکه آیا منیر سفر خود به ریاض را آغاز کرده است یا خیر، سؤال کرد اما پاسخی دریافت نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149359" target="_blank">📅 16:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149358">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
الجزیره: ایران اعلام کرده طرحی به آمریکا پیشنهاد داده که بر اساس اون، تنگه هرمز ظرف ۷ روز دوباره باز بشه. این پیام‌ها در حاشیه مجمع عمومی سازمان ملل در نیویورک و با میانجیگری قطر بین تهران و واشنگتن ردوبدل شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/149358" target="_blank">📅 16:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149357">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUYd-mZTxdk5RorMoMeikxdfCa3gUdOjwPL3rtgweTdYPAJfcIsF3Dkk9zI_B_FEotJTejuYRQjwbBZVZWq-fslKA4jmW1ra91bSluzl3LU7u5W0W-mNDy-jXIJsGfFgo672RCr4DwuJOilhDQ5moPt_6zl_mLgEXh1ppk5gIlU9_CsJZTPZUxKf3B736V5KSz2iQbpUZWpf1ATMxrheQC724wudY4zJzKLckwZmF2rMPZS5-pQvm48wPxbj1CzFU2WtslR6q_QC8KMSDVNfziF_OoHxEJt6DufvdYxYRZiRBvut61WFStTR8-_siYNcCoN9HyecisASrh0AX8CLIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : جلسه بسیار سازنده‌ای با رئیس‌جمهور شی جین‌پینگ، هم برای ایالات متحده و هم برای چین داشتیم. اتفاقات فوق‌العاده‌ای در راه است.
🔴
او، مانند تقریباً همه، به نظر می‌رسید که نام "هوش مصنوعی" را که نامی نامناسب و نادرست است، به نامی دقیق‌تر و مهم‌تر، یعنی "هوش فوق‌العاده" تغییر می‌دهد. همه دیشب نیز با این موضوع موافق بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/149357" target="_blank">📅 16:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149356">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری / ترامپ خطاب به رئیس‌جمهور چین: هرگونه حمایت از تهران کاملا غیرقابل قبول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/149356" target="_blank">📅 16:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149355">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1707c895.mp4?token=Zn4--kPmkrN9Dubqe2ZKe4XtAPJxMc4Y_ePcruWQ8clAX0vTT9-ecWR7z2j5zXNipZrhHTG1wAiE4CUVV2nb_Anb4pBDfLFp4zzLE8aqdjlUOai3hcZ_ga8mMv_N7CUqdrW4szTYdaa5BqYosKicpgkAJ5St4TlbTEfWJt9b7tz8DrQpgyx0VT8yZfDkLggMw3POyd9VUj0b4ZTxDrcyVDlav9YG273CLFC59ROSFOKOfZiGsqXRd2J0NDBsk6Gx78H4jomyF73Cx0QvAaCwpoIjXcP-v2K3AZxfj0HJGbWL7D2K8HskIA9VPEPdQPMwqKHyd9qetr5cywRnMz1EJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1707c895.mp4?token=Zn4--kPmkrN9Dubqe2ZKe4XtAPJxMc4Y_ePcruWQ8clAX0vTT9-ecWR7z2j5zXNipZrhHTG1wAiE4CUVV2nb_Anb4pBDfLFp4zzLE8aqdjlUOai3hcZ_ga8mMv_N7CUqdrW4szTYdaa5BqYosKicpgkAJ5St4TlbTEfWJt9b7tz8DrQpgyx0VT8yZfDkLggMw3POyd9VUj0b4ZTxDrcyVDlav9YG273CLFC59ROSFOKOfZiGsqXRd2J0NDBsk6Gx78H4jomyF73Cx0QvAaCwpoIjXcP-v2K3AZxfj0HJGbWL7D2K8HskIA9VPEPdQPMwqKHyd9qetr5cywRnMz1EJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاظم جلالی، سفیر ایران در روسیه:
به نظر می‌رسد که دولت ترامپ، با وجود مواضع و اظهارات رسانه‌ای که مدعی پیروزی و موفقیت است، به طور کامل درک می‌کند که ملت ایران استوار ایستاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/149355" target="_blank">📅 16:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149354">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhOkeCazkRJYKEvybvQj8wbfFnRsYSOgH99TjhpYx-PDMunRWYLweTtIXEAIj20hbb4yDmYPr4gBPfFSXhXcZ9VL6dOxxlCJ5eDWifhL8hhLHRUE155sTi6HVByF4TiWzy7okHzoGu-2L_4Zqb-VE2K4PdYl49-BgPKQU5A_Chp4noHQ0tnd3UGVhbPaqc5JLdb5PJ8CXksi-EljsprNdaUY1u5GA00Otr-NLzkFU4R3IiJ4gdyDweSEJaL8n2lAJvXahlSc9iYSy9kpSXt0E3vUA02tle34wK5JZEri_PJh9KC8TTEAo77kZwGyxujTlKcTqBSWXEZlM3-F61OkOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست عجیب خبرگزاری فارس که میگه شکاف در داخل باعث میشه ما شکست خورده به نظر برسیم و دلیل این شکاف، اصلاح‌طلبا بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149354" target="_blank">📅 16:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149353">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
اکونومیست: چین در حال بهره‌گیری از تجربه جنگی روسیه است
🔴
اکونومیست در گزارشی نوشته است که چین برای جبران کمبود تجربه رزمی خود، به‌دنبال استفاده از درس‌ها، داده‌ها و فناوری‌هایی است که روسیه در جنگ اوکراین به دست آورده است.
🔴
به نوشته این نشریه، چنین همکاری‌هایی می‌تواند در سناریوی درگیری احتمالی بر سر تایوان برای ارتش چین اهمیت پیدا کند؛ از آموزش نبرد پهپادی و شهری گرفته تا همکاری در حوزه پدافند، موشکی و فناوری‌های زیردریایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149353" target="_blank">📅 16:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149352">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رویترز: آمریکا و ایران در حال بررسی توافق مرحله‌ای برای پایان وضعیت جنگی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/149352" target="_blank">📅 16:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149351">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fn6U6ipA3cKbZQ7leTdxMw7kxiOb0iQjX_aBJAlt3OM-e2YQAEUBWO2JCUtMuYTkDkpmlWYfvcmL1oxrxTG-_dyF2i9GmUGtOI7C4GLID95uStV_n0X3ywlbU7BuA8mSRrlq_PjXC6ww1h0z-wDMpSY4nbE3kE4KWwsa5azArcfn4BXvsHJ46giSnXgQmRkMi2-n1a_eiRxZzTn_g-iuKEZdDpZylUmYhqGBs0JWe6LwgfYUA-4N-FwOrYXAf1Cs6eULTVeHpVPFgLuE9tqEYUqBuE6bcqPWEN5lstV5a5gNp5zbCzPFjXXZxKnIAXIsN_7-3yQy3K6ZV3anUAVizw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند لحظه پیش، دو حمله هوایی اسرائیل به حومه شهر زوتار الشرقیه در جنوب لبنان انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/149351" target="_blank">📅 15:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149348">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLX_anU_axbwIGgVl8zysoTr7MCj6U8g9KpCOgd0-zDiYShMWN7-CZevcI9jvLrVcyxA_IJYjMwoRA5yOfoGfNDDv4iyQGoIilpslb6KlCTpkASBgX7UApsTcukRiDPBb-DPvZTZdyImZRbcs2Chj_4vLAZMTrPw1fenxJROGP3Ec7Fz9DnoZiCX5JYf0siTaxq7Dwj3_0AWoM5UuRYb7zQ5bvKhVxd2FiDFlpvrD7qo6stm2NfuvMdXTKvqfYwNNBfeCLjNNLMVJReZBRmaMct1DuQ6ljhQjbaU62dVRC3-j2p6sg8OyZHhi9T7a-Au_cQRixAqwlK7koaQAG72kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lk496WUhRxB_xeHIx9I-xMY_8-6vRJTgxx4FbvlsJElzBnr_c_tgNy2p6ZOkbCREL8VMtqcFr2K8J3y7ZQA_0IS7Em52aRw2-OJNH49KGf00U76UoVLHj7qo5500vEprmlR98hPjZb7n5yLyd5KdvkfhM0WT-UDw3BFG11kvJDj_8gDf8Lncctnrof_YNrLA38R9SPIPJ_XjFdFHf2zw7IAqtuM8Sfkl5I4sK7wLuBxNnxrb5ltZhx5YiiiJJEAG6sfjXVNOkFbZDPjEdFvy09Pul9KVlObvgzlLW-ytosnj0nUtmyfBLOVVqpHNyPFqLTARHU5vGHa2AzDKY1TCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haSTHEWLVebbk3EuAJfcErjj8_9Ecyr-TmZAIlBRrXJcbTa9uGpBHE4vxvzrncNmK0GaBqPS5R7si27U9euFLmic6a5G3lfzSS_Uhmy4hUAFbVzgBDpuozhwfSqmA1SRllcK5Ap64cfNPvz3N0eWBujVXjzLLLSascfiwx3NB-DnT0yGtfwe9vVlLp6MXAvrPtZtiV7L10RTqQ99vkqCj_wPEFmFQDghRR5gFkMZFmyweAraMT3gP3c0_7ZI66IBNZ9vjvGAjIDz95DPnCnCDovTZDTuhYPqVyz18lOtCqUlczMmHgz3vH2gEA7YkiiFbYKGCdxAEUEvl5dRDCDwow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هنوز پروازهای متعددی از تهران به ترکیه، چین، پاکستان، تایلند و روسیه انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/149348" target="_blank">📅 15:45 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
