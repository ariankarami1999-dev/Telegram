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
<img src="https://cdn4.telesco.pe/file/J6KcmeRY7xxAcRrqbvEsL8tGxE1IYZPA_x7ZyZDhgqsa-FxI5TxDmqt_cieWiMNeVXu4m4io4lpVGk2b7EmYF596Pj5VGC-_b7OkBthCMkohVBlc9PdJs5vmNOLqMoSWbd3-J30R6bmXWE9EzBEROrIz2a6-B8scRSd2EazueSSLvNU9h8PG2KVcH46PdScI1rg66BWqmLJ5gBq6X3uh7Epw7XWhtowDn4-PZk0COt7SbcO-Ir_Y3Nuw03pXqwWP4ianlB65AhpRnPYiisetuI9jMffvtXTZq1_BXTAM3gERFWOgcxCq4hOuD5U4z9wBI0_GBiy7wYK1v4i0-0xxRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 23:27:51</div>
<hr>

<div class="tg-post" id="msg-19924">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/19924" target="_blank">📅 23:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19921">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ViO1MUlgx9R1wOkVntgpwEKJhx7ruFoiXRU0K6TEXXE6j8kFasey0HkQx8xFMxHCC20Ru51NMFNI8SyvrjTsE4Z3HYKslZkkp8VsPPvdKw1YneMeUqi8uRe6JTCkshWzDJUF35VkBZ1aC90St34tXIIyWAzp9JF9z0nhsXbvx4d1Lyf-HO_cCkl-BDaW0WvOLKjnZMTd7B-vSRjAytYiZuPmgUx2Yj39kfIpUEiRWeYB3xOlp30y9ZVEuAbEdXdRvCM3u02y3CQkr_crMUABlXZ9QfyzDrmTPSZ8cpG-Cnk0BdvLhljf839lXe_Ud5V0eU0wWfB8XvKrDlaaBKCKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6fuokvZc8C1ju_CwAjeSJEPer7RavoueVqIQY5-J9M8f5yDtkIL8-dZus3Xf9Uc0_0lsSqQmVk0cqd8-RXFV_E6zLWHjOcsYDmXinoc2Es--MTWKCnqPJ3YeA27xgcmPqwBll1LtVr2tZh1eUnkFdy6Sm41zE6-0VhfJmpfCeteDp8EmGKLnR7XA-kBoGQRAcYA5yTUVSus7K6VyIzB5Tbl-vwP2QcTadWmvIg8glMuUcajuGgbGJ4r3m9sDrDgvTMa0P3KaSJL2pSdBWFBEJG1Du-FARYHj-Fac2td4bPMy1g27Nj0mbrmoGX58D4Uil3KKehD9Y3DQkXijG63kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SV5t0MjFYsaxrxmt0Sen2eQtw-dk4-uLO6KeGNGNo0mn-naRL-DOD0EZUqLarTEUbbp8qyVwk4bKZv3e45oj88CDkU75sxF76c5R5lCfMakARm5JTdDKGQIms16oRx-2cA31PigQYYC2zqeeJXJbzVCYYXcmNvM6hGp0dcsLBSboTrgUxzwT23NLpbGXQSch_acupxUprpcb8Aa-2FdfFuAknEX0y08WW_kfqIGNQWeTf_NO7A0Xow0ixvD8iQg0rgfu0zMEfxx-53Oy_MS9JzgH78qK6HXLzMqEdONURT_Rpw792-ioOAYlw3bSm9WJ82myYC_Wj-xf2t3sn-fDCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین تصویر شاهزاده در مراسم درگذشت سناتور فقید لینزی گراهام که با اندکی فاصله سناتور تیم شیهی که صحبتهای جنجالیی درباره ایران در سنا کرده بود و ویدئویش را برای شما گذاشته بودم دیده میشوند.
@WarRoom</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/withyashar/19921" target="_blank">📅 23:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19919">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jME5n3JGiHtT5-q_QzmegB0oq5dCO-ISCtQRWiRBnCwmuk54KZPQyYV4vq1iiGB6SdFdROjNIeoWzoxAi8omsy7Y54DDEQkUUIsEofsT5f6zBeHQbAwDN-xVzf2rGIQ3XiThz9CtPvzxTTrlzBe4SQb_ViDTV2bZCGNH1l4hV0WC7SR85OTF-Famv8PveC0haLQNrJh7T-l331_1RDXfFfTFY_CYU4pDuWz1FamoLhz2gpI-j9T-GqbGP9pCTKSKr-IuOe3NtV9jwGck0e3kXvR4-VgM6UZbD6MfYx3y0sUy96gITJZd9PCfd3De4Fy_0_JRSTBoDbLQQQfVeXXe0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ff6vf20tfrL_Fl7kgY9wcvKIy97rye9p1f9MWnHvDiH6pYgwo-hoSEa8qjsL0MAXyFqLySQMYMYeoNCadoM1wB_D94HW5gQ7wBNrkbBqyhctwgBKrxcVaDK2ZLr6sDsYCYj4j07fsWSbSLdoJGsmx2sYU9AeSrsCAIEZtIGCCTmAwK7W6NCWkI8oiP-3RaxJybzmJWI12ExwzCzZQBou_rM5rclV-2IVbmFZZr_XEHogByjdZFpL97_ohkLwhhruQDZua6NIZ4grkwIYc5YIty1y7_Z0h5SDnn_aaAax5QFL6Sd3VPI6qZgua8nVZrBLMWERijLjugA59sTZPt6WIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهزاده در کنار کامران خوانساری‌نیا در مراسم
@WarRoom</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/withyashar/19919" target="_blank">📅 23:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19918">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19918" target="_blank">📅 23:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19911">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اکسیوس:ترامپ و نتانیاهو جلسه‌ای به مدت ۹۰ دقیقه برگزار کردند که به عنوان یک جلسه سازنده توصیف شد و تمرکز آن بر روی ایران بود، بدون اینکه هیچ نشانه‌ای از اختلاف نظر بین آن‌ها دیده شود.
دفتر نتانیاهو تأکید کرد که اسرائیل، واشنگتن را در مورد ایران تحت فشار قرار نمی‌دهد و هر دو طرف در یک هدف مشترک برای جلوگیری از دستیابی تهران به سلاح هسته‌ای، سهیم هستند.
همچنین، دو طرف در مورد امکان عادی‌سازی روابط بین عربستان سعودی و اسرائیل گفتگو کردند. موضوع فروش جنگنده‌های F-35 به ترکیه مطرح نشد و ترامپ از اسرائیل درخواست انصراف از مناطق تحت کنترل خود را نکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19911" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19910">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c9ed022ed.mp4?token=sZ7fRUb2X8srIaW_fJa9uKRrFaDrbdenekT70QH5Arf9BsB7PVCvHGJuUbneMKuwwcMH8n-hvlR9ciIIDF3-85YCfHsk8i3pkJDp77y9GeFWfdmmvb9yLj0yl0zI8XlCrypwJbqnJICpxCZS2EGF5M7zBf0Rbq-2bpAdV9-W51EXxGKuKtLz_iZds34Ad67r8Iy6QBjv6OOPxU9onvLSwkgSM8NbK-kxzkHHnDF1QzVzqRxuz_apPGw4-4p92W2yF4IxGf36yW8MlU1ZwPMGRRvwGk-esa0DrGPT1jJdQOy80YwPYrSndEmMMcsSnTettsSLGBnbGeGRke7O_5XLrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c9ed022ed.mp4?token=sZ7fRUb2X8srIaW_fJa9uKRrFaDrbdenekT70QH5Arf9BsB7PVCvHGJuUbneMKuwwcMH8n-hvlR9ciIIDF3-85YCfHsk8i3pkJDp77y9GeFWfdmmvb9yLj0yl0zI8XlCrypwJbqnJICpxCZS2EGF5M7zBf0Rbq-2bpAdV9-W51EXxGKuKtLz_iZds34Ad67r8Iy6QBjv6OOPxU9onvLSwkgSM8NbK-kxzkHHnDF1QzVzqRxuz_apPGw4-4p92W2yF4IxGf36yW8MlU1ZwPMGRRvwGk-esa0DrGPT1jJdQOy80YwPYrSndEmMMcsSnTettsSLGBnbGeGRke7O_5XLrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره لیندزی گراهام گفت:
او به‌شدت جنگ‌طلب بود.
راستش را بگویم، هیچ جنگی نبود که از آن خوشش نیاید.
فقط دوستان نزدیکش منظورم را می‌فهمند؛
اما او همه این‌ها را برای کشورمان میکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/19910" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19909">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یک منبع آگاه گفت مهنام نواب صفوی، ۲۲ ساله، خواننده رپ فارسی و از بازداشت‌شدگان انقلاب ملی دی‌ماه، از سوی شعبه پنجم دادگاه انقلاب اصفهان به ریاست قاضی همتی‌نژاد به اعدام محکوم شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/19909" target="_blank">📅 22:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19908">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ixptzz8H3bLK1ILyi3eSrMEHqINo42MDZ0_V0OxCyrECbxp9GmG93um7BMzV9lasBkb4wpBi5Hb-SojQfGphlMfRSCI__DvgVIlJz4QAyHJabBkBFqayDMVe2r-4zArYLMVh1p7LkmsjkbH0pDE10dUQmt7h871UGPT0sl-fb6y0fPBOH1Cp_m0EO_WoZlIO0Lh0k82wf5c-g-JtzhtQoY3sP9IYwOGkclZAj6yK_JjAVvy4iZr9HSNGLp6K98YVfsd34mCrFPqX2any1O1LNDZNrTTy4xBjPCKdeH2T0bpOFI2_V1XLzuI5N2sEMN0BCyRN6L0kYo5JFRrKjuoz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز : علی واعظ، مدیر پروژه ایران در گروه بین‌المللی بحران، یک سازمان پیشگیری از درگیری، گفت که پس از ملاقات با رضا پهلوی در ۱۵ سال پیش، به این نتیجه رسیده است که او اشتیاقی برای کشمکش‌های سیاسی لازم برای رهبری تغییر در ایران ندارد و از آن زمان تاکنون هیچ چیز دیدگاه او را تغییر نداده است. اما پهلوی به رویترز گفت: «من از حمایت زیادی در سراسر کشور، در داخل و خارج از ایران، برخوردار هستم.»
@WarRoom</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/19908" target="_blank">📅 22:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19907">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کانال ۱۲ اسرائیل: نتانیاهو به ترامپ تأکید کرده که حملات بیشتر علیه تأسیسات هسته‌ای بازسازی‌شده ایران حتمی است
@WarRoom</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/19907" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19906">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو:من همین الان یک جلسه عالی با رئیس‌جمهور ترامپ داشتم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/19906" target="_blank">📅 21:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19905">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">instagram.com/yashar
LIVE NOW !</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/19905" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19904">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/19904" target="_blank">📅 21:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19903">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/19903" target="_blank">📅 21:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19902">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06b2086bda.mp4?token=oa6RCCyglq0Ar0HMU4C-AD7S6v6VWeV7okLsULf_0tTkLkaAG3_zE3t6rmLYxWOeAtXRkUzNK2ol-W7Q0sabWRrSXVqYnXeMn9d0DKTaIUy3FnBd0tLmGeqnRx8y-BON2NWcFaAL1bh-FS6LXvN0yuWWKVYrI77WM2stg6IiIIyfyit9NHicHCpU93rLHpq3nm-orP7qJRHDaQ3xrYjOMHgWO2YpYjT3dRvBhhQDefCj3UnN7D4H_mxn_2CThVdZr3VdVSyOqHAP8-XK-EVWqKUK056ALxMcbPYKiPEEo5K0PElf6tYmfwVNYwXaeNvD24Hd1eUCwe_pvJxvyiJZcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06b2086bda.mp4?token=oa6RCCyglq0Ar0HMU4C-AD7S6v6VWeV7okLsULf_0tTkLkaAG3_zE3t6rmLYxWOeAtXRkUzNK2ol-W7Q0sabWRrSXVqYnXeMn9d0DKTaIUy3FnBd0tLmGeqnRx8y-BON2NWcFaAL1bh-FS6LXvN0yuWWKVYrI77WM2stg6IiIIyfyit9NHicHCpU93rLHpq3nm-orP7qJRHDaQ3xrYjOMHgWO2YpYjT3dRvBhhQDefCj3UnN7D4H_mxn_2CThVdZr3VdVSyOqHAP8-XK-EVWqKUK056ALxMcbPYKiPEEo5K0PElf6tYmfwVNYwXaeNvD24Hd1eUCwe_pvJxvyiJZcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/19902" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19901">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کاخ سفید : پایگاه مشترک چارلستون در کارولینای جنوبی به افتخار سناتور فقید لیندزی گراهام تغییر نام خواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/19901" target="_blank">📅 21:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19900">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مقام اسرائیلی نزدیک به نتانیاهو:
ما در یک مقطع حساس هستیم. رئیس جمهور ترامپ به زودی تصمیم میگیره که کدوم سمتی باشه.
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/19900" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19899">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/19899" target="_blank">📅 20:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19898">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کانال 14 اسرائیل به نقل یک مقام بلند پایه : ترامپ و نتانیاهو بر این موضوع تاکید کردند که هدف مشترک آنها، جلوگیری از دستیابی ایران به سلاح هسته‌ای است
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/19898" target="_blank">📅 20:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19897">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer"><a href="https://t.me/withyashar/19897" target="_blank">📅 20:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19896">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کاخ سفید:
جلسات ترامپ با زلنسکی و نتانیاهو، سازنده و مثبت بودند
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19896" target="_blank">📅 19:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19895">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پایان جلسه دیدار بین نتانیاهو و ترامپ.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19895" target="_blank">📅 19:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19894">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO2Q7wABTfDdz97YouELqbM-lQVIGtwXmfTlguxhZm11-kBZZAzINk6KefzTSNy3eWq8wYZAC8YlcGUZ2oJMPc2XmPQcdP0rp0fgqxDlRAP15CfWBijUGINXSg7f-KRnlZh4X0Less7N2lM1DgoEbz0xrIWh4WyYaKg2k__zAKmCnSQKQAzgBv-QwRMNod4_5sMB-tIgcqHL9B6uWyeoBGFBS6YYxg-ROfn9Pmew4WWzONLfsFAjGjZ4bNb6_xm4jwPjIIMqS82B10tnsbHd3-QK_nGjIJcb9JkSZbmMiFJEPNWW95gLauvT4GxsBJVeuncd9oKIdTCOkvhlAo5hSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون نتانیاهو و ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19894" target="_blank">📅 19:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19893">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شاهزاده رضا پهلوی نیز ساعتی دیگر در مراسم سناتور فقید لیندسی گراهم در کلیسای واشنگتن شرکت خواهد کرد.
@WarRoom
🇮🇷</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19893" target="_blank">📅 19:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19892">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در دیدار نتانیاهو و ترامپ، یک تیم گسترده از مقامات ریاست جمهوری حضور دارند: معاون رئیس جمهور ونس، وزیر امور خارجه روبیو، وزیر جنگ گست، رئیس سازمان سیا راتکلیف و نماینده ویژه رئیس جمهور، ویتکوف.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/19892" target="_blank">📅 19:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3UImib_GdOTAWLT49htQVHSuZB4jnUfYR-KxN2-80ENoqRuHgnuHUaqG-VYkJtwGOfVYieFiKDKdJsOfO2mpjFyGeKSqALF5TVTxIU458GXGkFicTjN8so3N-RQFBb6tGnyEcwbCcNkDkKde5tiR-i5B_XGG79UNdrscBX-zDSPNswipUazUzbBR5637SQEHd-G6yKykMV5GwvxqvHtJzoVHikJ-I4v5jeQSBuK75fChPnLOAfQ9Z93BCbCPL5SfjbtYG2EyATw1Edobv2ZrMBzo9dUxyEe0-yscZNJcL07dpHjkqQXBBYxEc9BDz7tmIbKBAoKEVbTpicdotKOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملاقات ترامپ و زلنسکی در کاخ سفید: رئیس‌جمهور اوکراین گفت که آن‌ها در مورد مجوزهای تولید موشک‌های پدافندی پاتریوت در خاک اوکراین گفتگو کردند.
@WarRoom
پیشتر رسانه های فیک نیوز گفته بودند زلنسکی بدون ملاقات کاخ سفید را ترک کرده.</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19891" target="_blank">📅 19:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19890">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM07vdFrX25Hwm6uagP_gh9-LDYOXdf7Mi6OaH8i6RHsMHp4tiYVj3no-nezuQgfOIlgHxxQiNteITt5GiuJnayZSjsQ1Uo7KefySY4xlDek9ILueTpl3FQAF7gwsVqklQyh-axS2CBEZ4O_hRYsJh4_uOIGET7nK4WFBeZBJCjpu2IRZ0Ds3LAUdf8X1ouxDnzDqyz7eJYMyctRGvc3ttVG2fxZBeeyTejfdMxnuu-fY3n_6gyd6Q0Bt9s_l3Oh9P_Zh-n7slJ0GLzOaFYuWNt9pN58srCigc4veYE9kMdaILmIV_tvyPzgJYFoYRkycAalPHChyLMd3LaA2b1G4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/19890" target="_blank">📅 19:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19889">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرنگار اکسیوس: یک مقام ارشد کاخ سفید گفت «ترامپ در مصاحبه با شبکه فاکس‌نیوز قصد داشت پیش از دیدار با بنیامین نتانیاهو، پیامی قاطع و سخت‌گیرانه به او منتقل کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/19889" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19888">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سلاح دیوانه وار «میله های خدایان» گزینه دیگر غیر اتمی برای «کوه کلنگ گزلا» در ایران !
این ایده نخستین بار در دهه ۱۹۵۰ و سپس در دهه ۱۹۹۰ در مطالعات نظامی آمریکا مطرح شد و بعدها به دلیل جذابیتش در رسانه‌ها، مستندها و بازی‌های ویدئویی بسیار مشهور شد، عملیاتی بودن این سلاح مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19888" target="_blank">📅 18:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b359db05.mp4?token=ca2KUv9ZFbuPRbzJn6LfBGApgjPJeuxJnU82okDHTGtfkNZFp8z-_lMjh0phrzha9NOdqXEvkBZBVVDSrDlnr3nARAqEWLGBiQFa7CAO6NQ3PuzZ5UTsnP-Y6ULFks7XoDL87Oq1v_6en8Vtmkd_PS37H4T0FasRb2597aDU3iq0RIlRtF3yAaciyBkFA3xzIwlcr4ojoO4aoXDjNjW9oxQSiKTUQMvQN5st34qQJW1RkrafrPtaA76gE36NZLwcm67URrvKlRJi07VJzdxl1cfMGaOxFIjiW-mmKHC1SsmQYOGdvclBd76Ei5nCY3D02jP16ae3KsLJUUnWEKHL1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b359db05.mp4?token=ca2KUv9ZFbuPRbzJn6LfBGApgjPJeuxJnU82okDHTGtfkNZFp8z-_lMjh0phrzha9NOdqXEvkBZBVVDSrDlnr3nARAqEWLGBiQFa7CAO6NQ3PuzZ5UTsnP-Y6ULFks7XoDL87Oq1v_6en8Vtmkd_PS37H4T0FasRb2597aDU3iq0RIlRtF3yAaciyBkFA3xzIwlcr4ojoO4aoXDjNjW9oxQSiKTUQMvQN5st34qQJW1RkrafrPtaA76gE36NZLwcm67URrvKlRJi07VJzdxl1cfMGaOxFIjiW-mmKHC1SsmQYOGdvclBd76Ei5nCY3D02jP16ae3KsLJUUnWEKHL1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو برای دیدار با ترامپ وارد کاخ سفید شد
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/19887" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19886">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتاق جنگ با یاشار : طبق تجربه و تحلیل من این شرایط دوهفته دیگه پر پرش دوام بیاره و باز دعوا شروع میشه
😁
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/19886" target="_blank">📅 18:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19885">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIkSuN7e0Ets6w28OoIMRKfSBcn5Q7UPaPNEU8ahkfGnDDmH4xIi3bT8MjVsxuPFtArwXsarqk3zlIC0qsK2aTiNp5tWQdD2Thd4y5-DLqK0x5CeadgpX3JExttflBLlcoPaPxF0v8WJgqlYuTo5ieQfnTLVXkIOL4d3BhN_Wf4TMDkFrUvFRHAPIP2zI3ZZ6nvS3_jqCG6745LKXBrrYkRDo2B6F1a50uiPoZd7aFxuwXCqWas0WYnzm3iwCYIY5_9fb9xJnOKWr7joIYS894B1PqpKzQRUOXLW5uYKqqHqJzZOgGqXpG9SQ2p-o2P6ujO7gFjD1AeQ5yuD0p4xGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تابوت لیندسی گراهام با استقبال خواهرش و اعضای کنگره ایالات متحده وارد ساختمان کنگره شد  جی‌دی ونس، معاون ترامپ پیش از مراسم تشییع جنازه امروز، برای ادای احترام به لیندسی گراهام وارد ساختمان کنگره شد طبق گزارش CBS News، مراسم امروز با آیین ورود به ساختمان کنگره…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19885" target="_blank">📅 18:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19884">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c954e618d1.mp4?token=BOua-pT-DSGN5IVUSyxWHtGuKO-8OF0aVcCzJCe-OhrLMZV7huxEKjxWj9jmwsbZQgAqfRt2UYtAqzXS8QN1ttDW8fU6vuxdv1iU4d-72c2hJit3Oi7dwJlketPmsKdfQW_2BEFm45yxso_ZFpVuSQOPsVnm-BHexAVBCzCXxziJ_yi5A_0v1o_DTxuZbAYoKSw2O_xYH9uZuDzyPvSUj6xA5uRMH03PXUGjtVl-ceyeWmwisj4pGaQyoZSj65XM-Ymo247xe0USM7t1COJtQb8Tnu1pBFNjTqjmjzBxqLN9UcO7M429-CoV-_ee7AK4_exYsoNdYq0J2EOWY2kmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c954e618d1.mp4?token=BOua-pT-DSGN5IVUSyxWHtGuKO-8OF0aVcCzJCe-OhrLMZV7huxEKjxWj9jmwsbZQgAqfRt2UYtAqzXS8QN1ttDW8fU6vuxdv1iU4d-72c2hJit3Oi7dwJlketPmsKdfQW_2BEFm45yxso_ZFpVuSQOPsVnm-BHexAVBCzCXxziJ_yi5A_0v1o_DTxuZbAYoKSw2O_xYH9uZuDzyPvSUj6xA5uRMH03PXUGjtVl-ceyeWmwisj4pGaQyoZSj65XM-Ymo247xe0USM7t1COJtQb8Tnu1pBFNjTqjmjzBxqLN9UcO7M429-CoV-_ee7AK4_exYsoNdYq0J2EOWY2kmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعتی پیش
لحظه ورود زلنسکی به کاخ سفید
@WarRoom</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/19884" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c7fe4f226.mp4?token=BmUtQN3u89UFJv6tCM1ylyEeJQPGXdLx8gLq2J4ENIegqBX2zGQvCJrD2I9EThjjvPk-x6f03Dv1g30Tn_k0kdlQBmtfr_qQh75bN5CEllHL1M7LDGi8xFxpfs9rWRAd17z7nlITviv9oYCP-denpbg6EJzt7kJFP4yrQs7ba7_RcJODkWlFZjSmrqkMzchvkT8Lelp7ezvuNMfH1mrjGCQD7PjwyMM6uYMY4lSyuI1y04vOq3MrGLZ41grr0-6L-Of_kuUjUqySH91uTUwHMVXFwNNHvWBem1Y5CJNoS9JW59lvNdJ4ouvccl7jJHjBVluWaX7tNGdKsm1FrK9EKRd_wTDcxFLtJZsvJtFOtNsthnkKG5oT5lfkhcCn1HTK5v1l3RNe-co-DhGdenpCilzL16_ays8D3NK9q9hjSrQdRFAJ-QyL1GIUQ9rVw24tGddt48fl2j-NAZnyjoaxuxOnaJm2b-fLtoS2-pQqhWCFyBLKeXoPC2Hw1rRVlR-aBgLrR_KqWZMcYhFOw9uS5BHRHXibMAt_8GVfQhbvytOhgqoV6LJd-5WDEhBEHEtb3bMzVRmzjKqgmsSxnnJ6XlsCeEj2RkLTqLiYNxjHBr83Ua6bqB64G7nYUR0e2KPsrDKdp7b0Xn7Dj2UWB62tOe_tghJZr9eSxO3mRGNXQVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c7fe4f226.mp4?token=BmUtQN3u89UFJv6tCM1ylyEeJQPGXdLx8gLq2J4ENIegqBX2zGQvCJrD2I9EThjjvPk-x6f03Dv1g30Tn_k0kdlQBmtfr_qQh75bN5CEllHL1M7LDGi8xFxpfs9rWRAd17z7nlITviv9oYCP-denpbg6EJzt7kJFP4yrQs7ba7_RcJODkWlFZjSmrqkMzchvkT8Lelp7ezvuNMfH1mrjGCQD7PjwyMM6uYMY4lSyuI1y04vOq3MrGLZ41grr0-6L-Of_kuUjUqySH91uTUwHMVXFwNNHvWBem1Y5CJNoS9JW59lvNdJ4ouvccl7jJHjBVluWaX7tNGdKsm1FrK9EKRd_wTDcxFLtJZsvJtFOtNsthnkKG5oT5lfkhcCn1HTK5v1l3RNe-co-DhGdenpCilzL16_ays8D3NK9q9hjSrQdRFAJ-QyL1GIUQ9rVw24tGddt48fl2j-NAZnyjoaxuxOnaJm2b-fLtoS2-pQqhWCFyBLKeXoPC2Hw1rRVlR-aBgLrR_KqWZMcYhFOw9uS5BHRHXibMAt_8GVfQhbvytOhgqoV6LJd-5WDEhBEHEtb3bMzVRmzjKqgmsSxnnJ6XlsCeEj2RkLTqLiYNxjHBr83Ua6bqB64G7nYUR0e2KPsrDKdp7b0Xn7Dj2UWB62tOe_tghJZr9eSxO3mRGNXQVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت لیندسی گراهام با استقبال خواهرش و اعضای کنگره ایالات متحده وارد ساختمان کنگره شد
جی‌دی ونس، معاون ترامپ پیش از مراسم تشییع جنازه امروز، برای ادای احترام به لیندسی گراهام وارد ساختمان کنگره شد
طبق گزارش CBS News، مراسم امروز با آیین ورود به ساختمان کنگره آغاز می‌شود. تابوت سناتور گراهام توسط تیم حمل‌کنندگان نیروهای مسلح حمل خواهد شد تا خدمات او در نیروی هوایی ارتش آمریکا گرامی داشته شود و سپس تحت نگهبانی پلیس کنگره قرار می‌گیرد. این مراسم در کنگره برگزار می‌شود و حضور برای عموم آزاد نیست.
مراسم اصلی تشییع جنازه ساعت ۲ بعدازظهر به وقت محلی در کلیسای جامع ملی واشنگتن (Washington National Cathedral) برگزار خواهد شد.
دونالد ترامپ سخنرانی خواهد کرد و نخست‌وزیر اسرائیل بنیامین نتانیاهو و رئیس‌جمهور اوکراین ولودیمیر زلنسکی نیز در آن حضور خواهند داشت.
@WarRoom
*ویدیو رو خودم از لایو مراسم رکورد و خلاصه کردم</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19883" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19881">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6rrXrIUY800FVEVxqAQ7J6GiLlN8HPl-8C08yG-aj_NSXypjl5aD9TWdkZXd2gX19yPJZ0MJ6GosNkCEXxqbLfkNrUOtZpetwKKMwPUyGVI3dnkVadKeZqB8MAtkOPngCM-nwWdbLvQDzrlvbvSyzwF5zHVo8iIEg8Rv6WryW8ITZ1IFb0CVDwx-IJpuiU2ILeew0r7o7zD7YqAQr6RO0XFQNC51GSoDaRRaSvw1KhCXXrgvSouQfn0FnSpm1r2n4O8ATb_R9-X6GfIz-iiC2fvs-lqBufI0757SKegwpaVOFYtiRcj94TpYLf7L4Qys79D4utV2ou1OEODqyNYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltT5tlvdkCmw187WCaA0SY225Mz-tQ9uRycOtPEBHCyuN9PgehJemeWrJ4Fi48Hw7a42f9XqoviibuAssvo5OSsnTO6seR29qY0uyzlIHqX9iWjqt9Zc8gGpNBvXgbLiZZqOK6GHNM2mHpQtdEmLJCZoTHQrMF32Mwn9sMBhoULUaLEr9dGZtbAWYVu2e2uFKUfuYmlf2-sSvAh9b1VUAxYu1gtCTgkcHoovR4MqMCgTaE3Tu9NK2DlWqiErj4rheHwPvMoSkJvUxk3FnrhE1AUIEXMfRAvNYmQW5tdnXG9iPjfuGUH7Mm-vbxbcvDVVNec2E9LXDLkwdsLCzOhdMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واکنش مارک لوین به اعدام و سرکوب مردم در اصفهان:
با این نازی‌ها مذاکره نکنید.
مردم رو مسلح کنید
@WarRoom
عکس دوم چهره کریه قاضی اصفهان که حکم داد</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19881" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19880">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اگر توافق نکنیم به راحتی کوه کلنگ را از بین می‌بریم ترامپ به فاکس :" من دقیقاً می‌دانم در کوه کلنگ چه می‌گذرد، مشکل بزرگی نیست. ما سایت‌های هسته‌ای آنها را از بین بردیم و اگر توافق نکنیم، باید کلنگ را از بین ببریم. اگر توافق نکنیم، خیلی راحت آن را از بین خواهیم…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19880" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19879">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049afcae48.mp4?token=r-IAnu3dDH62mdWfShSn8IswKRPmntFZ2lK47kuFXXKJ98jO9pFMqp-iaMH2UrCxGXROVGotXNFvwOl5abNQcKAc0RluHXpsgagUngS5lkjavgFTmF4AAGchWlH8eZpo10SGy6-bypBR1ndkkEj0jklp_gxYwPWIPmX75DPveEYEBSA7I8S1WZe9DslMof5phR8lppEqnXuBMw7ooQj61I7SpWP0hggxNqUmOMPdJPosTj8jnBCYcaLdDDuBhvvunUpDEAIgYLEqLkgkRUe9THkYA5TBPTJ7QOm3SDBNaPWaaMu0jfxil1yf-Tonpu5p3PZvwomNy3HGSt094xUcqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049afcae48.mp4?token=r-IAnu3dDH62mdWfShSn8IswKRPmntFZ2lK47kuFXXKJ98jO9pFMqp-iaMH2UrCxGXROVGotXNFvwOl5abNQcKAc0RluHXpsgagUngS5lkjavgFTmF4AAGchWlH8eZpo10SGy6-bypBR1ndkkEj0jklp_gxYwPWIPmX75DPveEYEBSA7I8S1WZe9DslMof5phR8lppEqnXuBMw7ooQj61I7SpWP0hggxNqUmOMPdJPosTj8jnBCYcaLdDDuBhvvunUpDEAIgYLEqLkgkRUe9THkYA5TBPTJ7QOm3SDBNaPWaaMu0jfxil1yf-Tonpu5p3PZvwomNy3HGSt094xUcqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران گفت: ما محاصره را برداشتیم، اما بعد آن‌ها توافق را نقض کردند، بنابراین دوباره محاصره را برقرار کردیم.آن‌ها توافق را می‌شکنند.دیگر نمی‌توانیم اجازه دهیم که توافق‌ها را نقض کنند
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19879" target="_blank">📅 16:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19878">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f30f4312.mp4?token=QO-lUGO5pLyUKl6ujh50UEgSJrkxrPj-iDnkVVm5oVmiUHyUAql8uHZnfn1s9bKnpa1f4lklK9DsKgqFKBFFokUaFBzigTpFmQdFM2n4ZL8RYqsIzYZuni6yrsMoENVsp2VgaIaM90a-4X7Uw8XxhEFJv-6MYaomW35loTeybboOyM_y540t_OQFtaI2Q35qAIaM5vv6G4xLyRxz9v-cI3pvMzDDIwc6LZpb0c4kri3cnHcnljlZvxQL2PjkAWQ0zic227cEsHE1DTxLfI8_qbkivYEF_yJPuFa3LTgROTedaRQb0ERFeZNDdMMAiFS3uz-a3_ybg0hSTElgsDnuKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f30f4312.mp4?token=QO-lUGO5pLyUKl6ujh50UEgSJrkxrPj-iDnkVVm5oVmiUHyUAql8uHZnfn1s9bKnpa1f4lklK9DsKgqFKBFFokUaFBzigTpFmQdFM2n4ZL8RYqsIzYZuni6yrsMoENVsp2VgaIaM90a-4X7Uw8XxhEFJv-6MYaomW35loTeybboOyM_y540t_OQFtaI2Q35qAIaM5vv6G4xLyRxz9v-cI3pvMzDDIwc6LZpb0c4kri3cnHcnljlZvxQL2PjkAWQ0zic227cEsHE1DTxLfI8_qbkivYEF_yJPuFa3LTgROTedaRQb0ERFeZNDdMMAiFS3uz-a3_ybg0hSTElgsDnuKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرارگاه تروریستی خاتم الانبیا
هشدار داد هر شرکت یا کشوری که بر اساس طرح غرامت ایالات متحده برای کشتی‌های آسیب‌دیده در طول جنگ، از دارایی‌های مسدود شده ایران وجهی برداشت کند، از عبور از تنگه هرمز منع خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19878" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19877">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ در مورد ایران:
لیندسی گراهام یک جغد جنگی در مورد ایران بود، اما در چند هفته گذشته، شروع به این فکر کرد که یک توافق بهتر از نابودی بقیه ایران خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19877" target="_blank">📅 16:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19876">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa71f5aa10.mp4?token=G5kn4vIQ_xxHRUdNqan0b29UllLRWDVNha7iU0sDqV2ra2hC5jsNbu2Z1vJuU5Bfaf2k8TS9sFZccGUvTEW7A_FogqAkDJIWJ4L_zTlkeMml4i4IhYc4tFhJfPfJ-seid2USq69jpGyWzi_EfAwURJjPeoHAv0vhUMmC08tjIJIjjqEV3IbHCLl-p0h3g-llBzWun9APdp__mg86WtKrOKPgR10xfQDxY8EJVCVCDQs87O8p1nnYFSK3FM51Wbmi6-dirdnPGhN3ek-rDFJf2aRKVWDb9pzMD7sN_cAvm54IgNDgPmtmlvRTolFyPokr2hsYrts7VNU_e-uqNF1aQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa71f5aa10.mp4?token=G5kn4vIQ_xxHRUdNqan0b29UllLRWDVNha7iU0sDqV2ra2hC5jsNbu2Z1vJuU5Bfaf2k8TS9sFZccGUvTEW7A_FogqAkDJIWJ4L_zTlkeMml4i4IhYc4tFhJfPfJ-seid2USq69jpGyWzi_EfAwURJjPeoHAv0vhUMmC08tjIJIjjqEV3IbHCLl-p0h3g-llBzWun9APdp__mg86WtKrOKPgR10xfQDxY8EJVCVCDQs87O8p1nnYFSK3FM51Wbmi6-dirdnPGhN3ek-rDFJf2aRKVWDb9pzMD7sN_cAvm54IgNDgPmtmlvRTolFyPokr2hsYrts7VNU_e-uqNF1aQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها موافقت کردند که سلاح هسته‌ای نداشته باشند. اساساً، ما باید این را رسمی کنیم، اما آنها موافقت کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19876" target="_blank">📅 16:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19875">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1021ee49.mp4?token=OXekXUSMlrjlfzrIUCoQAa_ubNodK6EvU4ah4qbNaR6Khx_pIHu_fJ7zsfsHMuIhn3o-rWkcnWTGJ1qzceBKH1k2L3O1RjBoZJwsMTb-fEmGbfUseEY4_Q1CNJAIAc0CEmiiHHxC93RyZKFJtMizIb7p5Ppu9SQbA0-8EJz8GnKr_cx-voxpob3wVLHLIqU90oZ3q6z_qm6Ewl6J1lkuvx5CH6Jox5HaCEjD_Bm5Z9sn5n_dapZLXZR94-WgDPDwMCYT3kLSL__VoxwTNXUTK-tMfymEsrv_DK8gYNV_1_bt-hRo3nfQV8g_nSdMnH_28Tt22-At7w7gZTFZtNQWYWd34DnC80ebZzP2eYocJJQpFRWD3f5-TfLfR3OYJIBypiB8ugmxZDODJZpK3N9cWSMphG4u7H1ZvBStWAvFfiswTpslLAnZYje5Q_r3WGWmlfUlXEiKKKtVG1cnORZq1ZgMW_shrl1_KU99T0WLA5q1HCxmY5W38CelAsWte8stdQL2KdzPNglUWj3GJjUTmSOTFGP81efhFjyAjhi1WWl6NhCvzmPAViL_n7zm3psm81DtTNCpf0pfnROvOt2Fj3vnb4OM2UWEzkmUzPCieh9OoH2ZsHh7JLnMEArp4db3qDthApdBjxuqBMdoVWtcQ2E_BkJPrl_QK0vrcOTamSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1021ee49.mp4?token=OXekXUSMlrjlfzrIUCoQAa_ubNodK6EvU4ah4qbNaR6Khx_pIHu_fJ7zsfsHMuIhn3o-rWkcnWTGJ1qzceBKH1k2L3O1RjBoZJwsMTb-fEmGbfUseEY4_Q1CNJAIAc0CEmiiHHxC93RyZKFJtMizIb7p5Ppu9SQbA0-8EJz8GnKr_cx-voxpob3wVLHLIqU90oZ3q6z_qm6Ewl6J1lkuvx5CH6Jox5HaCEjD_Bm5Z9sn5n_dapZLXZR94-WgDPDwMCYT3kLSL__VoxwTNXUTK-tMfymEsrv_DK8gYNV_1_bt-hRo3nfQV8g_nSdMnH_28Tt22-At7w7gZTFZtNQWYWd34DnC80ebZzP2eYocJJQpFRWD3f5-TfLfR3OYJIBypiB8ugmxZDODJZpK3N9cWSMphG4u7H1ZvBStWAvFfiswTpslLAnZYje5Q_r3WGWmlfUlXEiKKKtVG1cnORZq1ZgMW_shrl1_KU99T0WLA5q1HCxmY5W38CelAsWte8stdQL2KdzPNglUWj3GJjUTmSOTFGP81efhFjyAjhi1WWl6NhCvzmPAViL_n7zm3psm81DtTNCpf0pfnROvOt2Fj3vnb4OM2UWEzkmUzPCieh9OoH2ZsHh7JLnMEArp4db3qDthApdBjxuqBMdoVWtcQ2E_BkJPrl_QK0vrcOTamSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
اگر به عقب برگردم و کار را تمام کنم، همانطور که بعضی‌ها دوست دارند، با پل‌ها - خیلی راحت می‌توانم بیشتر پل‌هایشان را در کمتر از یک ساعت خراب کنم.اما می‌دانید، ساخت یک پل برای آنها 10 سال طول می‌کشد. پل‌ها طولانی‌ترین زمان را می‌برند و نیروگاه‌ها در رتبه دوم قرار دارند.من می‌توانم نیروگاه‌ها را در عرض یک روز از کار بیندازم. تمام نیروگاه‌هایشان از بین خواهند رفت.
فکر می‌کنم حدود 91 میلیون نفر بدون برق، بدون پل، باید زندگی کنند. و این یک تعادل بسیار بسیار ظریف است.آنها می‌دانند که اگر آنها توافق نکنند، من این کار را خواهم کرد.پل‌ها به معنای واقعی کلمه از بین خواهند رفت. در کمتر از... به نظرم در دو ساعت، بیشتر پل‌ها، پل‌های اصلی، همه از بین خواهند رفت.و نیروگاه‌ها در یک روز.اگر بتوانم از انجام این کار اجتناب کنم، می‌خواهم از آن اجتناب کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19875" target="_blank">📅 16:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19874">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8482ff12f2.mp4?token=KwL2kh5Uq0Bf9g--L1E61YqEbDkplfNw24FwkTVvz4lL9XI_rAMP-Ju6ehbCL71eFCzALokphKcO4lCayVwWG65Bvx4ODMgyZDErzopScckvUFKCm9o7Am8R-mGQEap2DvFESxNXYmtMKWy0PAtQ97EB4FD_1G9MZpgNWnEBg6W8i2mw9eF1jt_YYlTod8VD4XKveUvdYiXyBjAAF7a1ibVKWtFAShWpEZ9kbh0FUPiT4ifGGksXFN8PRKipEK_PaTAhV3By8anKjaFkvH4xxf8BobTW5LYhhm_js9yx64PrtTWMPoyVnhj3mfgX-KuCAr_SV84l4Geo4QIMVWjOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8482ff12f2.mp4?token=KwL2kh5Uq0Bf9g--L1E61YqEbDkplfNw24FwkTVvz4lL9XI_rAMP-Ju6ehbCL71eFCzALokphKcO4lCayVwWG65Bvx4ODMgyZDErzopScckvUFKCm9o7Am8R-mGQEap2DvFESxNXYmtMKWy0PAtQ97EB4FD_1G9MZpgNWnEBg6W8i2mw9eF1jt_YYlTod8VD4XKveUvdYiXyBjAAF7a1ibVKWtFAShWpEZ9kbh0FUPiT4ifGGksXFN8PRKipEK_PaTAhV3By8anKjaFkvH4xxf8BobTW5LYhhm_js9yx64PrtTWMPoyVnhj3mfgX-KuCAr_SV84l4Geo4QIMVWjOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر توافق نکنیم به راحتی کوه کلنگ را از بین می‌بریم
ترامپ
به فاکس
:
" من دقیقاً می‌دانم در کوه کلنگ چه می‌گذرد، مشکل بزرگی نیست. ما سایت‌های هسته‌ای آنها را از بین بردیم و اگر توافق نکنیم، باید کلنگ را از بین ببریم. اگر توافق نکنیم، خیلی راحت آن را از بین خواهیم برد."
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/19874" target="_blank">📅 16:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19873">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رویترز به نقل از یک منبع خلیج فارس:
عمان حمایت کشورهای خلیج فارس را برای طرحی که به تهران اجازه می‌دهد داوطلبانه برای استفاده از تنگه هرمز هزینه دریافت کند، جلب کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19873" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19872">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسانه‌های عبری: دفاتر نتانیاهو و زلنسکی در حال هماهنگی برای دیداری سه جانبه در واشنگتن هستند؛ با وجود سردی روابط، دو طرف ، ولی در موضوع ایران منافع مشترکی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/19872" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19871">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec75b87ae.mp4?token=PoDUnXSqT7Zp2UgSeWymDGh2dikQ69TTL8i-xQt7Ks22o6DXTwFdIFIxCRDsDNmWmJMonPFXLD8JiO6ikyXjKtwrp8VA7LFxl3WX4xpAk3AOJ-TK9tm_koAA8H7uZQI-xZbbBTTXezqt0fd6PWroX5OsGYm-1psedjNgqndTHjErvbyalQmtH0GuGB3i9_h_u0d3b0PdMkYlWPVF2ImUP4jh_MKVBX8MTPnW46hX9eJDt556KySNX9m3tqVpVeDgjVi1GKbvJZp1uH5qt0_M7PgA99P72pYhAouH_Cz4L2fKXSQkPZ5UzI3qV14KF3Lim80-RxZtDHDKYJGMyISvVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec75b87ae.mp4?token=PoDUnXSqT7Zp2UgSeWymDGh2dikQ69TTL8i-xQt7Ks22o6DXTwFdIFIxCRDsDNmWmJMonPFXLD8JiO6ikyXjKtwrp8VA7LFxl3WX4xpAk3AOJ-TK9tm_koAA8H7uZQI-xZbbBTTXezqt0fd6PWroX5OsGYm-1psedjNgqndTHjErvbyalQmtH0GuGB3i9_h_u0d3b0PdMkYlWPVF2ImUP4jh_MKVBX8MTPnW46hX9eJDt556KySNX9m3tqVpVeDgjVi1GKbvJZp1uH5qt0_M7PgA99P72pYhAouH_Cz4L2fKXSQkPZ5UzI3qV14KF3Lim80-RxZtDHDKYJGMyISvVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فروریختن یک مرکز خرید در ژاپن در پی وقوع زلزله ۷/۱ ریشتری
به گزارش "ان اچ کی"، شمار زیادی زیر آوار گرفتار شده و شماری مصدوم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/19871" target="_blank">📅 15:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19870">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آمیت سگال:در اقدامی که از دونالد ترامپ کمتر دیده می‌شود، دیدار او با بنیامین نتانیاهو دور از حضور دوربین‌ها برگزار خواهد شد؛ موضوعی که پیام‌های زیادی در خود دارد
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19870" target="_blank">📅 15:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19869">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏شالوم بن حنان، از مقامات ارشد پیشین سازمان امنیت داخلی اسرائیل (شاباک)، گفت در طول سال‌ها صدها هزار حساب کاربری رباتی که بیشتر آن‌ها وابسته به رژیم جمهوری اسلامی بودند، شناسایی و مسدود شده‌اند. به گفته او، این شبکه‌ها با هدف مداخله در انتخابات اسرائیل، تأثیرگذاری بر افکار عمومی و ایجاد هرج‌ومرج فعالیت می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19869" target="_blank">📅 15:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19867">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وزیر جنگ اسرائیل:ما قویاً خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
۷۰ درصد غزه را نابود کردیم و الگوی آن را به جنوب لبنان منتقل کردیم.
ایالات متحده در موضوع ایران ملاحظات و منافعی دارد که با منافع اسرائیل متفاوت و فراتر از آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19867" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19866">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانال ۱۲ اسرائیل , وزیر دفاع کاتز فاش کرد: جنگنده‌های آمریکایی از اسرائیل برای انجام حملات به ایران به پرواز درمی‌آیند‌ و ایرانی‌ها از این موضوع آگاه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19866" target="_blank">📅 13:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19865">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مهاجرانی: هواپیمای تازه‌خریداری‌شده در فرودگاه بوشهر بر اثر اصابت موشک منهدم شد؛ تنها بخشی از دم هواپیما باقی مانده است
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19865" target="_blank">📅 12:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19864">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام کاخ سفید: ترامپ در کاخ سفید با زلنسکی و نتانیاهو به طور جداگانه و پشت سر هم دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19864" target="_blank">📅 11:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19863">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19863" target="_blank">📅 11:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19862">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مدیرکل مدیریت بحران استانداری اصفهان:صداهای شبیه به انفجار در برخی مناطق جنوب و غرب اصفهان، بهارستان و حومه ارتفاعات صفه و شهر ابریشم شنیده خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19862" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19861">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سخنگوی دولت: سهمیه بنزین ۳ هزار تومنی از ۱۰۰ لیتر به ۵۰ لیتر کاهش پیدا کرده
اما هنوز هیچ تصمیمی به صورت جمع‌بندی شده برای قیمت بنزین در جایگاه نگرفتیم
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19861" target="_blank">📅 11:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19860">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏زلنسکی و نتانیاهو همزمان به کاخ سفید رسیدند
‏ولودیمیر زلنسکی، رئیس‌جمهوری اوکراین، و نتانیاهو، نخست‌وزیر اسرائیل، همزمان وارد کاخ سفید شدند تا در دیدارهایی جداگانه با پرزیدنت ترامپ گفت‌وگو کنند.
‏همزمانی حضور این دو رهبر در کاخ سفید، گمانه‌زنی‌ها درباره احتمال دیداری محرمانه میان آن‌ها برای جنگ همه‌جانبه با رژیم جمهوری اسلامی را افزایش داده است.
‏این دیدارها در شرایطی انجام می‌شود که پرونده‌های امنیتی مهمی از جمله جنگ اوکراین و تهدیدهای مرتبط با رژیم جمهوری اسلامی در دستور کار واشنگتن قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19860" target="_blank">📅 10:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19859">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :گزارش رسانه های غیررسمی در اینستاگرام و تلگرام نادرست است مبنی بر اجرای حکم ۳ نفر . دیشب مردم اصفهان درگیر شدند تیر اندازی شد و جلادان فقط توانستند دو نفر از عزیزان را اعدام کنند و یک نفر اعدام نشد. @WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19859" target="_blank">📅 10:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19858">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند  @WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19858" target="_blank">📅 09:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19857">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جلسۀ شورای هماهنگی مجلس با حضور قالیباف
سخنگوی هیئت‌رئیسۀ مجلس: صبح امروز جلسۀ شورای هماهنگی مجلس با حضور قالیباف، اعضای هیئت‌رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19857" target="_blank">📅 09:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19856">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxHqv1fLLMlSDzTBtnVUicd9BclYBsxfhu0fD1oLN944Wj4qp4GpH2MyAJlMLSNlu6jIunKDPYsgJvMz0Gp4UxPx4ca1_WdCm31wQ3EOuRjC30ccxxscELhZHl3wASgx6FefudS4PYKCqz_1mgyOc4x8ZKSasdFpIHI9cyGq4JN5Zn3i-o_du5U7S5ekYy1ShvVEwb8j3YhpCceD6mazs2ZuUEtF5q6ddOVjnRj1CCCsBT9CD-T-KhVo_z-GmHuOm-32a7kNVcQ7XeAnSjAuTue5KjsBH4iA3RPuYfKnr34Hu4HUkonNqxHlbof_7xwaMqwRbqLuIKGmk1qHpQ_x9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویرک پست : ملانیا و بارون ترامپ در ویدئویی نگران‌کننده که ترور آنها را تشویق می‌کند
یک ویدئوی جدید از ایران، حامیان رژیم اسلامی را به ترور همسر رئیس جمهور ترامپ تشویق می‌کند.
این ویدئو با عنوان «چگونه ملانیا ترامپ را بکشیم» تصاویری از بانوی اول را در کاروان موتوری و در برخی مکان‌های اطراف شهر نیویورک نشان می‌دهد و حتی نام برخی از فروشگاه‌های طراحان مد که او از آنها خرید می‌کند را نیز ذکر می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19856" target="_blank">📅 09:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19855">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">روزنامه لبنانی "النذاع الوتان"، که با مخالفان حزب‌الله همسو است، امروز به نقل از منابع خود گزارش داد که ایالات متحده پیامی قاطع و جدی به لبنان ارسال کرده است. این پیام حاکی از آن است که هزینه دخالت حزب‌الله به نفع ایران و انجام حملات علیه اسرائیل ( در صورتی که ایالات متحده یک عملیات گسترده علیه تهران آغاز کند ) بسیار سنگین خواهد بود. منابعی که در این روزنامه ذکر شده‌اند، گفتند که این پیام به این معناست که هر راکت یا پهپادی که به سمت اسرائیل شلیک شود، در واقع دروازه‌های جهنم را برای حزب‌الله و لبنان باز خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19855" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19854">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش انفجار در اردن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19854" target="_blank">📅 08:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19853">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzs6r7NKh4Px_FT2c5lVUyQLzuc0HWI4ccJfpyEPRqcmJrvjgkV0iJV0mpxcwerlTgFkVlJ0u41xBcgqzCQVzbxR02RLfOFL1JIBOsqC24a-zn-rcDKg0v8VBC4qP0IwskndoYfS11QBAPZUQGAt3bZo-ysBENQxdhTTrRLVd9Gt8spt-CUmmjgXOCbmIDvNJyKG-dzb0R5_zep-S6xZ6inUnyDHgGK23GQcsr9SqW5OL17Rn2geCXBOeTet9N_LEaYBlm5SsvwTR7c5j0KAVfhlovn1Uh1EmDdatC0NoglVK2oCar9kHBMgaXoMCUBfjMFNjQP38Uis8YnUC_T0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار نفت سعودی شده و همکنون 89 دلار است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19853" target="_blank">📅 08:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19852">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM7R5ByuM4jrMXalHltmP_GimRu4VumPSt2Ro2oQjBs3sTh-wYgom_KQhpXiMlJPDS8KHziVjecCg8g7AyK8wfnLkDd85H5-ESOYf8G1fdjC8WofO8WlLhagqCpk09hrnKDXjPGUy_3fABiyFk06jvfBi4I2vwAxcfFRVebVoGzO0VEzBCQGcoYwHgyxSeXDjLd2BEGLi3B7oiT517ttLDF2dCL07nmeYi3cUHU3h2PWAiE5AZd3ahHAz2ECtQSm2LGWur2f75FDFVdo8eWE0Ke8rovQDZohuKHk9TN2-IlXkKfQ-2YTYvcswM-aiezh1ylx9lxw8erkHq51z7A3vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و همسرش با «اطلاعات محرمانه‌ای» درباره ایران و تأسیسات هسته‌ای کوه کلنگ وارد واشنگتن دی‌سی شدند
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19852" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19851">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به گزارش وال استریت ژورنال، رئیس جمهور ترامپ پس از آنکه بیش از یک سال به مشاورانش گفته بود که کیف در حال شکست در جنگ است، به طور فزاینده‌ای نسبت به چشم‌انداز اوکراین در جنگ علیه روسیه خوش‌بین شده است.
ترامپ «برندگان را دوست دارد» و اکنون به طور فزاینده‌ای زلنسکی را یکی از آنها می‌داند. انتظار می‌رود این دو رهبر روز سه‌شنبه در جریان سفر زلنسکی به واشنگتن برای مراسم تشییع جنازه سناتور لیندسی گراهام در کاخ سفید دیدار کنند.
او تحت تأثیر صنعت پهپاد اوکراین، به ویژه توانایی آن در مقابله با پهپادهایی مشابه پهپادهایی که ایالات متحده در جریان درگیری با ایران با آنها مواجه شده است، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19851" target="_blank">📅 08:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19850">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حکم ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی در اصفهان انجام شد و جاویدنام شدند
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19850" target="_blank">📅 08:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19849">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شنیده شدن صدای انفجار در اربیل در شمال عراق
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/19849" target="_blank">📅 00:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19847">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=mO2tulCGy2P6w6tw5MocuU7XX6JAIJ6b69ebOZlB1Cw9c9I52p_H-VoCWUsPLPR5Ea31Byd-hBzWVyknMs-k-hXpR4bNY3ggjOU0m-RFeXuxnnuJ-dZxWYKEhTVJLExTRLuk8WOl3MctLGWB-btvgrv_ZbZlYuCbs8CLpJGLTpc2Ztb_PC8jbx3MVBciAqopuZb2gEXeuykF-nnSBvRF5FDvMj34C2poQIBLlHlKnLsFyLBTxCXCrwN6bajdyuB8FyqF6Z81DbaIFwpKqA0uSZcaAxXTtmCJrJ38S8u_p6nEGwZn9pHRJwSerjEUULGA6zYXDw2XOZbz2BXc8Z9kAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da687f9ab.mp4?token=mO2tulCGy2P6w6tw5MocuU7XX6JAIJ6b69ebOZlB1Cw9c9I52p_H-VoCWUsPLPR5Ea31Byd-hBzWVyknMs-k-hXpR4bNY3ggjOU0m-RFeXuxnnuJ-dZxWYKEhTVJLExTRLuk8WOl3MctLGWB-btvgrv_ZbZlYuCbs8CLpJGLTpc2Ztb_PC8jbx3MVBciAqopuZb2gEXeuykF-nnSBvRF5FDvMj34C2poQIBLlHlKnLsFyLBTxCXCrwN6bajdyuB8FyqF6Z81DbaIFwpKqA0uSZcaAxXTtmCJrJ38S8u_p6nEGwZn9pHRJwSerjEUULGA6zYXDw2XOZbz2BXc8Z9kAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست وزیر قطر: پول‌هایی که به حماس پرداخت می‌شد، شفاف بود و با مجوز دولت بنت انجام می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19847" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19846">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3e86fee4.mp4?token=n5ZX0rHRK-ScNujxz-sYUevKH4Cj4hqVE23_PDmkxytQNb07J8cDLm0jNy7bRI2WJxKsXdJskwazqiV39XBJtaoxa7VaSzvTzD9FnSDsiEo01blcMna_VfWF5ngk4NYc2BXdZGFKeIWBgKS5ac9esba4U97dC7JdSO5VvcJwKGGRKLqszL0BcWeOwBmZezhxALd_NDpXKYdx-BD6C93xMGd5GPgMrHx9RYn7XJCgEdvG2XF7WwnNNgCiaVaPdcUXBeFX2BXImg2-cAE69rBtk_QnYIcCdwpJnjzJU-OGTnIl7AYN-CB0efqiwvtiIumxg372TM-euPzABtmnebrrm4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3e86fee4.mp4?token=n5ZX0rHRK-ScNujxz-sYUevKH4Cj4hqVE23_PDmkxytQNb07J8cDLm0jNy7bRI2WJxKsXdJskwazqiV39XBJtaoxa7VaSzvTzD9FnSDsiEo01blcMna_VfWF5ngk4NYc2BXdZGFKeIWBgKS5ac9esba4U97dC7JdSO5VvcJwKGGRKLqszL0BcWeOwBmZezhxALd_NDpXKYdx-BD6C93xMGd5GPgMrHx9RYn7XJCgEdvG2XF7WwnNNgCiaVaPdcUXBeFX2BXImg2-cAE69rBtk_QnYIcCdwpJnjzJU-OGTnIl7AYN-CB0efqiwvtiIumxg372TM-euPzABtmnebrrm4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زامبی لند
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19846" target="_blank">📅 23:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19845">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c6fd33f33.mp4?token=iX83PNXq9jBMAx2uLjUPW7dPcutsdASeMymDnxZCizt5H-6MuQzhdsDKYPpMifJxSu96Rg6poYiNFPkymAzWrXOrrv09z35GLhucipl5q2JxW0gxy_s6k4jjreEqbCXDDYviHoMHP_24pxmSiw9XWuV92C7-uaZbfe-agMDqSnaIxGuuTJaOqgaktZ68l43XYgRSgn_nFgYfHU_JUNJDTPyestAvB8LPk5xpg6A2nUcvUWiMLY32-KslsYJ-KJfpB1B7uUHS4rr4wWkB-fu8zeLFbZ-CzkPsaY4Mhtlsxa1Sl5A3vdwH-rKr-y3hfI4b0m24FNI8OVA_ZeovNDp2Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c6fd33f33.mp4?token=iX83PNXq9jBMAx2uLjUPW7dPcutsdASeMymDnxZCizt5H-6MuQzhdsDKYPpMifJxSu96Rg6poYiNFPkymAzWrXOrrv09z35GLhucipl5q2JxW0gxy_s6k4jjreEqbCXDDYviHoMHP_24pxmSiw9XWuV92C7-uaZbfe-agMDqSnaIxGuuTJaOqgaktZ68l43XYgRSgn_nFgYfHU_JUNJDTPyestAvB8LPk5xpg6A2nUcvUWiMLY32-KslsYJ-KJfpB1B7uUHS4rr4wWkB-fu8zeLFbZ-CzkPsaY4Mhtlsxa1Sl5A3vdwH-rKr-y3hfI4b0m24FNI8OVA_ZeovNDp2Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برای مدتی قیمت سوخت پایین آمد. سپس آنها رفتار مناسبی نداشتند و من مجبور شدم برگردم.
حالا آنها دوباره رفتار مناسبی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19845" target="_blank">📅 23:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19844">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c208632.mp4?token=m00nUZgnJgdtK9M_N28nRckFiL5XjaBCJcjHnMdp8XEfvkzHs13fUopOy4veFkC6K9lG99AXUdJ-w3cCI5doIbTp9W98KDK2vnxpgUTvVQ0T2-aG3H_HULMrrI2dukU5Trz9axHL0cQeH1QyMx8sueIgfaC_G3xGQbJewIWXPllIXyR7eAsKdAaKEv_e72TKWX-6g1kcRDPt_Ejez6Yego-_x3DrVm4-NCtU5usq3jGxuRgSP7x5umA9dHSlNaVUac82_8TYjQBH4vXq9eBmwjpp8fhIJlWwcGJeQfZ3tUVPLBmQyr2vBf3H4uZpN2aocHIzUtGeWAmZcpAJyyjCTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c208632.mp4?token=m00nUZgnJgdtK9M_N28nRckFiL5XjaBCJcjHnMdp8XEfvkzHs13fUopOy4veFkC6K9lG99AXUdJ-w3cCI5doIbTp9W98KDK2vnxpgUTvVQ0T2-aG3H_HULMrrI2dukU5Trz9axHL0cQeH1QyMx8sueIgfaC_G3xGQbJewIWXPllIXyR7eAsKdAaKEv_e72TKWX-6g1kcRDPt_Ejez6Yego-_x3DrVm4-NCtU5usq3jGxuRgSP7x5umA9dHSlNaVUac82_8TYjQBH4vXq9eBmwjpp8fhIJlWwcGJeQfZ3tUVPLBmQyr2vBf3H4uZpN2aocHIzUtGeWAmZcpAJyyjCTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
مذاکرات دوستانه‌ای در جریان است.
ایران می‌گوید: «لطفا، لطفا، محاصره نکنید.»
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19844" target="_blank">📅 23:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19843">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4de1bcc9.mp4?token=fObb-DOvZKDSEKsAe1aSCCejXrTXnsQ7Kpz16L3WUGDQV7qXsOHl_tOchTnNQ5E9BF-EVmuy0WckXsxmkFOe63KRCIUFkscPDba77rflWU29LDcObxgAcU1G33PvH7hU1WkOfJa6bPtX0zKSbmtRaxbvzX4pcN8iunpsKFhf88zoCDhq8g8NAvpPZs1EOC7jgY4NDZ0d5xgzcda9qnTb1urqHBsNW0WrJq-VcOQVOEbcKreRXiCAlnxs7Oc_cyaAv30-s-1BsmIlVrlip1UEPnDHBhDoQX2LWFkMfUkarbshNEPL9jaZC7sV7lCBFw4EIMhidjCvs7UcFiftZSkizQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4de1bcc9.mp4?token=fObb-DOvZKDSEKsAe1aSCCejXrTXnsQ7Kpz16L3WUGDQV7qXsOHl_tOchTnNQ5E9BF-EVmuy0WckXsxmkFOe63KRCIUFkscPDba77rflWU29LDcObxgAcU1G33PvH7hU1WkOfJa6bPtX0zKSbmtRaxbvzX4pcN8iunpsKFhf88zoCDhq8g8NAvpPZs1EOC7jgY4NDZ0d5xgzcda9qnTb1urqHBsNW0WrJq-VcOQVOEbcKreRXiCAlnxs7Oc_cyaAv30-s-1BsmIlVrlip1UEPnDHBhDoQX2LWFkMfUkarbshNEPL9jaZC7sV7lCBFw4EIMhidjCvs7UcFiftZSkizQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
شما نمی‌توانید به آنها رشوه بدهید. شما باید آنها را شکست دهید.
و ما داریم آنها را به شدت شکست می‌دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19843" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19842">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a198bcb3de.mp4?token=MSmZdJEZDK5sdoMu_hZmL2yMKyx20sxxxY9g04-YoJh8bkI9S8Tkv2YudAGrTNVMABGLQc4pIY4GqadSMr1StvFMMjD9k-cLWkWOc3hL9ziF_seWUSgm9Vf_dJWeQy3Snx-lqRIGAYsnJPv-L75G1f40xWF5rHruOzpSrDnL57iq4aDcQZmJcYwM3tuH8Tick4Nec1GXTDQG0L67Oe-uGGAqg92-i8gHl0Wil6nmoi65-AdOpAq3_9LD7KnxOT5grS6QJzr0nZDBju2CZo08GK-Zlmzf2XcgtvOQarQdA4jaK76o5heqVL_1oZpU9uYJUWa05Lrhp6-chpEARQuu4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a198bcb3de.mp4?token=MSmZdJEZDK5sdoMu_hZmL2yMKyx20sxxxY9g04-YoJh8bkI9S8Tkv2YudAGrTNVMABGLQc4pIY4GqadSMr1StvFMMjD9k-cLWkWOc3hL9ziF_seWUSgm9Vf_dJWeQy3Snx-lqRIGAYsnJPv-L75G1f40xWF5rHruOzpSrDnL57iq4aDcQZmJcYwM3tuH8Tick4Nec1GXTDQG0L67Oe-uGGAqg92-i8gHl0Wil6nmoi65-AdOpAq3_9LD7KnxOT5grS6QJzr0nZDBju2CZo08GK-Zlmzf2XcgtvOQarQdA4jaK76o5heqVL_1oZpU9uYJUWa05Lrhp6-chpEARQuu4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : همون اتفاقی که توی ونزوئلا افتاد، داره توی ایران هم می‌افته
فقط مردم متوجهش نمی‌شن
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19842" target="_blank">📅 23:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/506238d711.mp4?token=q_VBgzk1soQ4b2SBGlCD6xMdXnzUL8qaTCJZhzcyFkAF_E7K0wYc6kw0d1jlWbtGPBCGls_E8FAcxxJUeTrDSXur1nPTmSpjGNODSE0bqBLLaY_ysdkAMwfiOvAeuB1LhsHnjwKwRd8eOC8m4arNpsdJwYgpPH25MlMX8zOCuw0N_T8UxojNjF6zK0qDczoGyFniWoIs_71Xohsq5kJtJaSW7TDd4wXcm5dkVXjvg6DL_BqaiTw0dbD7WepgKr-NeQtevQ7QutEI89qdz-m1tQiCRQ7dxl7BGuyTLFltDZaZCHkk2C0qJNe9m47QnGphJjJPl2Gr03_Xs_ei-accqYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/506238d711.mp4?token=q_VBgzk1soQ4b2SBGlCD6xMdXnzUL8qaTCJZhzcyFkAF_E7K0wYc6kw0d1jlWbtGPBCGls_E8FAcxxJUeTrDSXur1nPTmSpjGNODSE0bqBLLaY_ysdkAMwfiOvAeuB1LhsHnjwKwRd8eOC8m4arNpsdJwYgpPH25MlMX8zOCuw0N_T8UxojNjF6zK0qDczoGyFniWoIs_71Xohsq5kJtJaSW7TDd4wXcm5dkVXjvg6DL_BqaiTw0dbD7WepgKr-NeQtevQ7QutEI89qdz-m1tQiCRQ7dxl7BGuyTLFltDZaZCHkk2C0qJNe9m47QnGphJjJPl2Gr03_Xs_ei-accqYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به كشاورز زمين داد، چريك شد
به زن هويت داد، آنارشيست شد
به كارگر سهام داد، كمونيست شد
به هنرمند اعتبار داد، توده اى شد
به مسلمان حرمت داد، تروريست شد
به دانشجو بورسيه داد، ماركسيست شد
به اقليت حقوق برابر داد، جدايى طلب شد
@WarRoom
نسل ۵۷</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19841" target="_blank">📅 22:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19840">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2-QJ9OVILL6rkdPfKdD7x-273ReoB4uVYXaVc4bGlYdxdCuZNp0oBGK_jiyhfgvDLgORJww7TI6Ub3buKxmo976OsbZipREjXjLYvrxcXLckMPVz5f0883qxOBgSBHVxvRcO8chiMXi5vbH5Y2E-OJnwFgFw7H0IaPjxoFaY1DVJTIl6VhQLS5QL2X4O_ITyR0J-pbWACf4PdbZ_cjvQjGcn0y_pvE015P-naTWDtVxpswuxGvFIeip4wRZzoBHDqJMh8n4mkPqWZGniVYkfa8CRLvjBY4Z_L-93ZSfzrmW2s8GG_UxwuiLcUHiFQ4xbhmcf3FWGxjGzJMVuopBSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عمو لیندزی بخاطر ما تا مونیخ اومد، حالا وقتشه ما بخاطرش تا واشنگتن بریم.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19840" target="_blank">📅 22:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=EDpa7MEbyYZukk7IP8Licp8spBMieTUXPGJYufcj2QC7WxYeHyc3AgusbQoB7hgEA-2xklMCY5cNO1-IeJo3uc2vWqE7AuYdN3xm91PW2rI6HBK3oKOdVIMPy9briRshS7r3JdEhp6BfqlSvadEAcrdjEs3ltQA89kG-9ip463B16onsCioWhW3wC1JI9xf8qE-5zQkVoG23kO6hIkQymRNuMpknUBvrUaKpEsbJ9vqIhWnn3eHvAJKxTmXolZBIKaEYow_ZuF4glgdubZxcX1Et8bAFZD-c_RLBplwTIWdyCd5WAbCjEk45gYd3IS_N9l1ui8S0VK5BwOQfQzlnYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3a98b01b.mp4?token=EDpa7MEbyYZukk7IP8Licp8spBMieTUXPGJYufcj2QC7WxYeHyc3AgusbQoB7hgEA-2xklMCY5cNO1-IeJo3uc2vWqE7AuYdN3xm91PW2rI6HBK3oKOdVIMPy9briRshS7r3JdEhp6BfqlSvadEAcrdjEs3ltQA89kG-9ip463B16onsCioWhW3wC1JI9xf8qE-5zQkVoG23kO6hIkQymRNuMpknUBvrUaKpEsbJ9vqIhWnn3eHvAJKxTmXolZBIKaEYow_ZuF4glgdubZxcX1Et8bAFZD-c_RLBplwTIWdyCd5WAbCjEk45gYd3IS_N9l1ui8S0VK5BwOQfQzlnYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏در برنامه دیشب مارک لوین پیشنهاد داده شد که یک دولت قانونی در تبعید با رهبری شاهزاده رضا پهلوی تشکیل داده بشه. مارک لوین این رو یک ایده فوق‌العاده خواند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19839" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19838">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانال ۱۵ عبری: نتانیاهو در دیدار خود با ترامپ، تحت فشار زیادی قرار خواهد گرفت در مورد مسائل مختلف، از جمله سوریه، غزه و لبنان. این دیدار بسیار مهم است و امیدواریم که مقدمه‌ای برای یک عملیات مشترک بین اسرائیل و آمریکا علیه ایران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19838" target="_blank">📅 21:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19837">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبرنگار: آیا نتانیاهو از شما می‌خواهد که با ایران به توافق برسید، یا از شما می‌خواهد که به حملات خود ادامه دهید؟
ترامپ: عملکرد بیبی عالی بود. ما در کنار هم عالی هستیم ، نمیخوام بگم ولی ایران اکنون ۸ درصد او چیزی هست که چهار ماه پیش بوده
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19837" target="_blank">📅 20:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19836">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: از پوتین درباره ارائه کردن تصاویر ماهواره‌ای روسیه به ایران، سؤال خواهم کرد. با اسرائیل در مورد ایران مواضع بسیار نزدیکی داریم. ذخایر مهمات زیادی داریم و مایلم که مهمات بیشتری فراهم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19836" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19835">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یاشار : نگران نباشید یک سری مدارک رو و آلبوم رو حتما موساد دیر حاضر کرده  تکمیل کنه میپره
😁
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19835" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19834">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرنگار: آیا شما و نتانیاهو در مورد ایران با هم موافق هستید؟
ترامپ: یک اختلاف جزئی وجود دارد، اما ما بسیار به هم نزدیک هستیم، بله.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19834" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19833">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ: من زمان زیادی را با ایران سپری می‌کنم و فرصتی وجود دارد که اتفاقات خوبی رخ دهد.
ایران در طول چهارده روز گذشته، ضربه بزرگی دریافت کرده است.
آنها به ما با لحنی بسیار مؤدبانه درخواست کردند: "لطفاً دست از این کارها بردارید. بیایید ملاقات کنیم."
احتمال رسیدن به توافق وجود دارد.
اگر اقداماتی که ما انجام دادیم، صورت نگرفته بود، آن‌ها اکنون آمادگی مذاکره با ما را نداشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19833" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19832">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار: آیا از وزیر دفاع، پیتر هیگز، به خاطر توصیه‌هایی که در ابتدای جنگ با ایران به شما ارائه کرد و نتایجی که در پی آن حاصل شد، احساس خشم یا ناامیدی کردید؟
ترامپ: نه، ایشان وظیفه‌اش را به بهترین نحو انجام داد. ما ارتش ایران را نابود کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19832" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19831">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZumQ9RB83xR4HYMeVweU5UgAXl9Oqtjit3TkMS_yfjM4fRmu8HLTHObs_3u_bfOLAoEJEiG49I64Zrt9B-eAdKsct6B3l3lE6_9CLB_ry5B8Y6Ja59vqcdygbDweX06cmBD76VAV_XMKxXdwPOPkG8BiHuR1npPRBfEzGvjs7WLrwGJogHvJQnMMQPpxW2AWsV3jP6P5zZjL7DieZ9Izy7z0sYmbHT-AX0RSPvF_UQXp3_1cP5bhD_DUIC3KfhUad5UUZQLz9bb_tEwfDuHDZdMTnLaqSHgs8W8Q0tv31_haD5nXvAiOcvuLTZssnfwc351JYNcvHZL_aVqL2-Nog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19831" target="_blank">📅 20:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19830">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیویورک تایمز : ترامپ در حال بررسی سه گزینه اصلی در مورد ایران است: تشدید اقدامات نظامی، تشدید تحریم‌های اقتصادی، یا اعلام پیروزی و عقب‌نشینی نیروها.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/19830" target="_blank">📅 19:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19829">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند. جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند. @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/19829" target="_blank">📅 19:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19828">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrKir5Qx5bbIp48Rw0pUr0x8W17dCFq0qjCunpKIEeRnoXbk2mGllma7DuM_qe-ygmxcvmjmjeDPmEXAu5svi3BZ-nyXjQKrHlbDVURgqLLxtk_a3bRKRZlCrtcidkAKEFdFMzen8RAMa2Dh13IBTBB-2kxSt3rVEPzPZSWL8mSt-TrQAA3F3LCIduvKyKLI5izg-rN9ZbXs0V0yAXGO2y_4E22B-AnWKwU4GATAU07qD-96MFalXQvNciNwAN6ZX4lpth1yuit_H7Zf1JGJs1adMEMivgucScbSt3UcSmCfOT4Sr2Yk6whf4JyahsA1xDPTFdsAvADRkosPXhchwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک ملوان آمریکایی در حال گشت‌زنی در دریای عرب توسط ناو هواپیمابر یو اس اس فرانک ای. پترسن جونیور (DDG 121) است که از محاصره دریایی ایران توسط آمریکا حمایت می‌کند. سنتکام ۱۷ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی دیگر را توقیف کرده است تا از رعایت این تحریم‌ها اطمینان حاصل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19828" target="_blank">📅 19:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19827">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">هم اکنون
تیراندازی نزدیک کنسولگری آمریکا در تورنتوی کانادا
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19827" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19826">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تامیز اسرائیل : بنیامین نتانیاهو در دیدار پیش‌رو با دونالد ترامپ در کاخ سفید قصد دارد اطلاعاتی جدید و حساسی درباره روند بازسازی برنامه‌های نظامی و هسته‌ای ایران ارائه کند. به گفته منابع اسرائیلی، این اطلاعات شامل ارزیابی‌هایی است که نشان می‌دهد ایران تلاش‌های خود را برای بازیابی توان نظامی و پیشبرد برنامه هسته‌ای افزایش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/19826" target="_blank">📅 19:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19825">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرنگار:علت پذیرش درخواست میانجی‌ها برای توقف آتش توسط شما چی بود؟
ترامپ:چیزی برای از دست دادن یا به دست آوردن نبود ‏
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19825" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19824">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcde86Zlw7D8lGkADg57nBGHVqz60eyhjMVU-sAePHrkW7UGs8ZrJ5n1IsK2PuJjnCbjZHbiCVjJkibE9x6uOVTAF64qzU2uOgejqQZs_DypBrRgXJwhZ9cWMjI_xkIIUAdcYQKnCJsVRXumFOKWCFyuWGcF2ZkXNFOXsWGsQABm3fdkon_hD1rJoOyK4uKBasHa9x0sap4f9wxtseewdZQQRUUgS7JYu_O8v5FISDJxaVFYkiB8q-ORtbRbOJ4BYRjWdgj4U7qmLJpjQtbL6qJk-deaTm66UIp5fY2RJb-bq8FWiK42HKMaxLsGeurskaVOX-zjbZ4DmFrWQ8BIPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها از حمله هوایی اسرائیل به شهرک طیر ابلعروب در جنوب لبنان خبر دادند.
جنگنده‌ها ۶ نوبت این منطقه را بمباران کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19824" target="_blank">📅 18:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19823">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: به درخواست واسطه‌ها پاسخ دادم تا فرصتی برای مذاکره با ايران فراهم شود.
"من زمان زیادی را برای مذاکرات اختصاص نخواهم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19823" target="_blank">📅 18:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19822">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل گفت: ما در حال انجام مذاکرات عمیقی با ايران هستیم و اگر این مذاکرات موفقیت‌آمیز نباشند، به یک عملیات نظامی گسترده باز خواهیم گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19822" target="_blank">📅 18:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19821">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کاظم دست کج : در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و اصرار داشت که مسیر جنوبی تنگۀ هرمز فعال باشد و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19821" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19819">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9nXWyOwWpDcuQ9rtvA_dL4Oir0SJlpW6hdEkfNLEvcG2NFdKWXMcyVVMrPtiPlXTwVI3JelnY-70v4IsDrBH6KYpqPFdKOwjayXckB3ABAzBTzxRUKnN3LDJYxjh00cijJKv6AQWA7YLM8RDqG7Zwc5mlWOiuixDChB2eM60SV1Ccdrdha6W8qSg5rkWR13UuFR_pu84ZRaBG3vqAcNMse2Nv7uwocngwLrLbP0tPrFGxXue0oRA1jKlDQXJFKszqXJgsipWLdgbZNT4a_MexpWlfKrHw4vQ0HGqgCcjpmvLFC3evOovx-QNJzRejnCV_esWqFTSEUv4Bd-O_gkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند پهپاد MQ-4C آمریکا پس از فعالیت در خلیج فارس، نزدیکی ایران، در آسمان عربستان سیگنال اضطراری ۷۶۰۰ ( از کار افتادن ارتباط رادیویی ) صادر کرد و به مقر خود برمیگردد ، همچنین ادامه پل هوایی ترابری سنگین نظامی آمریکا را شاهد هستیم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19819" target="_blank">📅 17:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19818">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وزارت امور خارجه عربستان : ما پهپادهایی که قصد هدف قرار دادن تاسیسات نفتی در مناطق شرقی و ریاض را داشتند از بین بردیم همچنین این حملات را که توسط شبه‌نظامیان تحت کنترل ایران در عراق انجام شده است محکوم می‌کنیم و تأکید می‌کنیم که پادشاهی عربستان سعودی مصمم است جلوی متجاوزان را بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19818" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19817">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">همشهری: سران قوا با بنزین ۱۰ هزار تومانی برای سهمیه سوم موافقت کرده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19817" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19816">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جی دی ونس در انتقاد از اسرائیل برای جلوگیری از مذاکرات:
من قطعاً فکر میکنم شاهد یک کارزار بسیار پنهان و با بودجه بسیار بالا بودیم که تلاش میکنه مذاکرات رو منحرف کنه و مانع رسیدن به توافق بشه.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19816" target="_blank">📅 15:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19815">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=nVsBFwsI56pNqzM5ATyzyV8ci77PVRnsu6HaLFM4vj1hgpRGo67NPnzPAF8EHH3p3VVOHc-yZd2Lla-mZJf6aHHnwurPiF0ZhS-Ii0X_SZALtt63vfj5lK-CJsW54mDSMjdNnoBIveiyBYmP14z05wUQtgYBoorsYhrzpk9gPUydrCE8vWkc9od5yiV9o_cIV7a-cd9AZnSIc2zEdE18NfLgjHOasnW0h-mT9sutW1CwqCXcyjXzx7oObWahXQ7FerF1Wy4qUwj1VMNt-21rjg_AaWHUgNo2IiT6355Xy9PwpvRyhkYgmbXgqOFo_hnRK-iOQFOO0mlhDj1UtKu_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbef676e41.mp4?token=nVsBFwsI56pNqzM5ATyzyV8ci77PVRnsu6HaLFM4vj1hgpRGo67NPnzPAF8EHH3p3VVOHc-yZd2Lla-mZJf6aHHnwurPiF0ZhS-Ii0X_SZALtt63vfj5lK-CJsW54mDSMjdNnoBIveiyBYmP14z05wUQtgYBoorsYhrzpk9gPUydrCE8vWkc9od5yiV9o_cIV7a-cd9AZnSIc2zEdE18NfLgjHOasnW0h-mT9sutW1CwqCXcyjXzx7oObWahXQ7FerF1Wy4qUwj1VMNt-21rjg_AaWHUgNo2IiT6355Xy9PwpvRyhkYgmbXgqOFo_hnRK-iOQFOO0mlhDj1UtKu_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: من با رئیس جمهور ترامپ در مورد مسائل مختلف گفتگو خواهم کرد، و در صدر این مسائل، ايران قرار دارد.هدف از سفر من به واشنگتن، تضمین امنیت، قدرت و آینده اسرائیل و همچنین گسترش دامنه صلح در منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19815" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19814">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwjnYNcfikcjS7TQzBRUXSLMST5BHTNg4Z9hrgB0BxSvOfp-zDI6mQAdAwJKxkESswf-b5w5_rFHW8ypJREDbBUlvpDnW5RHbQYDfD2kGq4mLMjbq5ji7m4ID-k8zglNQPvjjqxEgemOB6NUvf22LdjjZ6HMnyiijgGFXXtU5zDrlvX_6nAcmlGIB0m93R_qtLlxckJT0cn1QTnmiV0VS9KmxDbzMGLjGO7ggSFCqqmJHKMOqvLHljlFa9xXQGN9K4251Ulq41qeLqZnfKnXew3sPS9uLUnYtwp56-4_ZurHkW2QRJt95gX_JUBbZp2hnXukUmWY2K4d3JwzsJmH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون کرج سمت فرودگاه پیام
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19814" target="_blank">📅 14:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19813">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">صداوسیما: تلاش آتش نشانی برای نجات ۳ نفر که در طبقه سوم ساختمان مجاور هتل استقلال محبوس شده اند @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19813" target="_blank">📅 14:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19812">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI_i2iwEYtk53T0tg8tKD2Tu4k9vgCwPKxzZV6bNDdvTMXrrfv8satHPpwM4mt5mmW-W4PpJEvr5lnX7pM8A4f3xWm-qqlzPSB_EurYPE_ZHIfjX3zVpdb4TGRa7W0s8lkdSUql-GNECYqJwKyUS01VrfbcYPgx452h4qs4ayfTFpzZLmNbTa5xNJryJpGlKMZorQZuIi0SGasIOObZQHTuYlVBvU1H3IlQS-Qhwwnxl1CphYaTZRjpvMK5vm7OOSr63KnZRTL1V10bDFiRLQFD0HnfdEIpDw5GjS2HLUYK3bBHYDqO5HYFk0qboOTIsrsM_gS2xpLeNHNEf2lo4sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دهه هفتاد میلادی، در زمانی که در منطقه کسی نمیدانست سوخترستان حتی چیست. عکس بسیار زیبا از سوختگیری دو فروند بویینگ 747 شاهنشاهی بر فراز دماوند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19812" target="_blank">📅 14:15 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
