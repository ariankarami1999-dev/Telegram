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
<img src="https://cdn4.telesco.pe/file/vg7qumNc66eMXZ2cO3boI9fJs26fA5yoaQ9E4uW0p-HU-0vaYw0jIGAhQOMCAYYMtwfhWOtl7Hs1_kbnorsaUsBMRQXoJxJnX3_sV3xnqF0Y3x3D5nHpnxjnqfy72Q49yoMy8EXbNGkY0uKlYuZSQ9x-Lum57PCzLtJXc_4vK06KDuuQ4qNoImlVTwStVOKIWm1o-Y6hqxW_BnHCQsPZUdQgkWitkiS937NgSMgEK-aQ5yIlGboHIyBBaNO6mq6JpFgJ_A2gLVqXAYW4SfQtbHTKs-wo_v0avBrTDCQFMydKOWGYQvMfz8K6pj-q9Qjzlx5etFAUE3XI0yGlbw2HjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-71250">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVVqDhP_ozVdC7RuN_qkpNJEkhgtzu6AYGnfs738l9UG4vxUbuZhQ51Q3n-5tuLW2ID_Voq8DhXDsbd6fKP0BF-WCqARWDpKrZ4z8uulAJkdi948ajNrZ7krcAoQx9xwHXZ6u2tbLwzFShZZPp9vyj2wkTUwzkn-Hcn-Io7RhjFDe2SsuQQkFj9j3Nbl4-zBx3K99hEGAhtISVZO1nlo8ccxfFPynZ97yIfQ5R7AVFLmWMSYjWB6rwwTnkqwUZ9WsP3yAde92gyUyu2uNC5U1ob3luwhvA45cUxLov72Jeyxha6HkNhsKTXXIYxd9IwZClQ_y7pJFLiWwXNfHHElCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
🇺🇸
ترامپ بازنشر کرد:
سیاستمداران ارشد ایران خواستار پایان دادن به جنگ هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/news_hut/71250" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71249">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=Eo8H6C9C7b71TDDnIVLsRsFzHTVJc-tKEF8Y4Cn4EXyVvYHZtRo47qGBSyv1eEZ-PgfWiFEmiHS0EhiJOvmAjmQSH51n6X5rQu9gt9s7u4P5y8miZ-zkC2XxJXvZLb1nWiof1LseR5H7gOIJGJ1NSR3jkZk05WuAox14WWoe1RQTYuokGTmxLBJWMhzhIfLShkK8TWzp5jrl5ZcCW0jdU3gXWhw04IAeHOWp8L1tqykgwbrusSbDcxBR8QJOt5TObp2rnzqdIkl7Aty4fJkRXBKkKGj0x3s4gHhLc7PXoIXMgk0b0u446-0l9FDfBg6DDPcwmxUMuCXhbSFrIEGDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=Eo8H6C9C7b71TDDnIVLsRsFzHTVJc-tKEF8Y4Cn4EXyVvYHZtRo47qGBSyv1eEZ-PgfWiFEmiHS0EhiJOvmAjmQSH51n6X5rQu9gt9s7u4P5y8miZ-zkC2XxJXvZLb1nWiof1LseR5H7gOIJGJ1NSR3jkZk05WuAox14WWoe1RQTYuokGTmxLBJWMhzhIfLShkK8TWzp5jrl5ZcCW0jdU3gXWhw04IAeHOWp8L1tqykgwbrusSbDcxBR8QJOt5TObp2rnzqdIkl7Aty4fJkRXBKkKGj0x3s4gHhLc7PXoIXMgk0b0u446-0l9FDfBg6DDPcwmxUMuCXhbSFrIEGDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
به تازگی یه چیزی مُد شده به اسم «جوجه پارتی» ، تو این پارتی، پسرا رفیقای دوس دخترشون رو به همراه رفیق سینگلشون به این پارتی میارن، تا برای همدیگه جوجه بکشن و از سینگلی در بیان.
@News_Hut</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/news_hut/71249" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71248">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7Fsbt5DhlEU0CQnt0liXa0TExIFRd3H4cSre3bpHnzfol1hTnGnMMbc7xgICEOUoqnSBX8O2hDt_h4HhFveJGWVCYnA2dpQbQOj8HSawF331MVUG4NyOf4LIRsuTnqFdpQeFVQC9ZKQZ2Eko9ECCnJ21xJIddOg2dOnALg2sBDIpxc-57_EMwglJQQ5YNuanBZ-2j_5QPWUzqBykLWucjolJQEcz_cF5q2jQuDNlzNR1XlBc6rIKj01Mzr959fqQGYOrJU0W6pqixFlifvRmP3ySvOgBcxUnQGe3IkSlM5dZ2Sd2hWQJLkK9vrtC0GtiGp957ge2T5PlbodFuOswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/news_hut/71248" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71247">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71247" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/news_hut/71247" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71246">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9O_z4L2kLBpxHvcnS4uXdONI7YaDYJYeu6cjjJCRl8pRCFPsSYfRqk-V8plpgMHnLFHUjmOWtPOpsdHGxPU1ZSFPxuckLnxNfbGQ_mJDPOVAHDyy6Pk3yr-E2q-uRaM6SCQVJ272k5F-fAdQzPek-O39uspOMuJkQylEkM4vrCaMWH8D7coGbUhrtD3As7D3TiD0g8nlVVkHi270bmdnL6eZDD0KlcjRjPcw2QkdcfpBPtWy77j3esCdynMcqTcpzfwCxZNcbiwReqOe0FgnR9MMoJ_w3yVo2S3Bne_MATQh3XhBxsWDZEl5tcA9_Ff3En5xVzqQXYUtcv0MdQI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/news_hut/71246" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71245">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">▶️
🇱🇧
🇱🇧
این ویدیو رونمایی شهر موشکی عماد است که مو به مو طبق شهرهای موشکی و پهپادی سپاه پاسداران ساخته شده؛
دو سال پیش حزب‌الله لبنان از این شهر موشکی زیر کوه‌های علی الطاهر رونمایی کرد.
جمهوری اسلامی بیشتر از خود حزب‌الله لبنان خرکیف شده بود؛
از برنامه ثریا تا اخبار سراسری صداوسیما تماماً افتتاح شهر موشکی عماد با ۴۸ کیلومتر تونل بود که مدعی بودند ساختش چندین سال طول کشیده و اکنون تسخیرناپذیر و نفوذناپذیرترین دژ عالم است.
این شهر پس از سه ماه محاصره توسط ارتش اسرائیل سه شب پیش در سکوت خبری تمام رسانه‌های جمهوری اسلامی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/news_hut/71245" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71244">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=BkVvp0DMCbonYMbCXQEdB3JFc7lFvjEMi54HCXya7b4hFFufmiUf0HX6VEnvn8h6FH5Ox0UYbh93PEcPBhkBEYPJNrYo0VZkCHT3w7FYKTFR0yI1p9I0K-L_pNy3EGCn8w80k61R7R8QpnxzySuGO1jph6Mb1fZYay_9xY_i8pq9Jz6BQHQ6gK0bhJTLtq3kpCqXEF0l-S5BSmTpIFornnnwhHBbHGFsdIYlUCuHMz8cX5Y6whYXCrd-IjCgTQEYzjpFPLpXhx7UVSiOiigqhqy8bcqNigt4dUOJa2vPvCyOrx6UkbjzlPerthtwD3QvsA-kgd_1wS4bfpGMwUP72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=BkVvp0DMCbonYMbCXQEdB3JFc7lFvjEMi54HCXya7b4hFFufmiUf0HX6VEnvn8h6FH5Ox0UYbh93PEcPBhkBEYPJNrYo0VZkCHT3w7FYKTFR0yI1p9I0K-L_pNy3EGCn8w80k61R7R8QpnxzySuGO1jph6Mb1fZYay_9xY_i8pq9Jz6BQHQ6gK0bhJTLtq3kpCqXEF0l-S5BSmTpIFornnnwhHBbHGFsdIYlUCuHMz8cX5Y6whYXCrd-IjCgTQEYzjpFPLpXhx7UVSiOiigqhqy8bcqNigt4dUOJa2vPvCyOrx6UkbjzlPerthtwD3QvsA-kgd_1wS4bfpGMwUP72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از لحظه فاجعه انفجار تانکر حمل سوخت در سنندج که باعث مرگ 11 نفر شد
@News_Hut</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/news_hut/71244" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71243">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=JYb0JcABkRLu-zFhAciCJM4qAR__wdD4ovCFkNGvfqfsDjZSk83bipKXFrv2X9qDF0bSGDyrVLPvUaGQxkZL0og1zBolfdRcBiYTag_wjNUhvGUWZKbU4gkeVT-QmgW2PGqKMdffwfxYOx81AixaFdLy9rHWotj5pD9dqmhSDX4G2XYfwSkT-NMBeLNPAPCn_IdF-QUhlRM0yUTpEWfDoJtuPAQJGqIi5lZW_lMORjs4mLU1aRnikRCe6v7c7zyC5tNJkLUoXQcEfi7sA4VaPS__9-0DtoOKB5jsh7xpQujKVDrmt9WTwkg5oLEEiw6lQ59jlBJPDMvjNWDZ2Z-VtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=JYb0JcABkRLu-zFhAciCJM4qAR__wdD4ovCFkNGvfqfsDjZSk83bipKXFrv2X9qDF0bSGDyrVLPvUaGQxkZL0og1zBolfdRcBiYTag_wjNUhvGUWZKbU4gkeVT-QmgW2PGqKMdffwfxYOx81AixaFdLy9rHWotj5pD9dqmhSDX4G2XYfwSkT-NMBeLNPAPCn_IdF-QUhlRM0yUTpEWfDoJtuPAQJGqIi5lZW_lMORjs4mLU1aRnikRCe6v7c7zyC5tNJkLUoXQcEfi7sA4VaPS__9-0DtoOKB5jsh7xpQujKVDrmt9WTwkg5oLEEiw6lQ59jlBJPDMvjNWDZ2Z-VtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
طبق قانون، استیکر و گیف خنده داری که از رفیقت میسازی جرمه...
و میتونه ازتون شکایت کنه و تا 1 سال حبس و 5 تا 33 میلیون جریمه نقدی داره.
اینکه شوخی بوده هم هیچ تاثیری تو مجازاتش نداره
@News_Hut</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/news_hut/71243" target="_blank">📅 17:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71242">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06303045.mp4?token=kN4d7eCpzXuKwUBqmhbmcv5gb4vjcr3IVgn75zrR8E0Bt4sEc1hDzd00ISyAnLSI7AoG-vtTENzujRrwHZFCp2ARYjg5aM7h94Zm9uXx-4ELAuTK1Lv5vmHf5IozxwEEggn9cEShJObUuWhU9-doSbaSb1eJupGno-A6_wmWd9hCf_44w0v0PX5uws8oK89yRd58xQixTonK6nqiHiqEfEC1_U3i2r4lr3lcx_cNHtxtggAmBhVJHKynRAyrpVZc7vhcBN2IqLuHI0UZSx5c2G3RMRM7SFP5hNV8qvJi1ZcQ90Q-l3WI0T79X6dnLBcQz3bM80lHaTePhEV4GngAGQ_g0-fO4BSDnQAh3ENkAJJWpy692b-CIGM46Oxdyc1aM9M71aID0ELElmaw6HPhaE4m78l-oPYZAxgLSsyEOrbe51M8_WJtFjV1YruPqdelPFfk6F_y89v3E2CrHrwdKojEdlvnziXxV4NOnvM7LA4nd8hVF8Bu1UW1YAs9_BMOzT4BsZr6GfF0ch9u2RXCtSLJ5E4StJ5dBffGeVCe3XZkMpwBBU7lYaJ0ko4mbuu02L1zuE_W7Wkt_kYOZdy6iFgc78DhWvwBtyEIvwKy4ybNCxOsZnTFaOxdPzIeUhhe0yiPNpliEwQG8LIeJSz34XeHqf5ke26xDoWalXMeQio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06303045.mp4?token=kN4d7eCpzXuKwUBqmhbmcv5gb4vjcr3IVgn75zrR8E0Bt4sEc1hDzd00ISyAnLSI7AoG-vtTENzujRrwHZFCp2ARYjg5aM7h94Zm9uXx-4ELAuTK1Lv5vmHf5IozxwEEggn9cEShJObUuWhU9-doSbaSb1eJupGno-A6_wmWd9hCf_44w0v0PX5uws8oK89yRd58xQixTonK6nqiHiqEfEC1_U3i2r4lr3lcx_cNHtxtggAmBhVJHKynRAyrpVZc7vhcBN2IqLuHI0UZSx5c2G3RMRM7SFP5hNV8qvJi1ZcQ90Q-l3WI0T79X6dnLBcQz3bM80lHaTePhEV4GngAGQ_g0-fO4BSDnQAh3ENkAJJWpy692b-CIGM46Oxdyc1aM9M71aID0ELElmaw6HPhaE4m78l-oPYZAxgLSsyEOrbe51M8_WJtFjV1YruPqdelPFfk6F_y89v3E2CrHrwdKojEdlvnziXxV4NOnvM7LA4nd8hVF8Bu1UW1YAs9_BMOzT4BsZr6GfF0ch9u2RXCtSLJ5E4StJ5dBffGeVCe3XZkMpwBBU7lYaJ0ko4mbuu02L1zuE_W7Wkt_kYOZdy6iFgc78DhWvwBtyEIvwKy4ybNCxOsZnTFaOxdPzIeUhhe0yiPNpliEwQG8LIeJSz34XeHqf5ke26xDoWalXMeQio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
🇰🇵
روسیه و کره شمالی یک پل جدید را در امتداد رودخانه تومن افتتاح کردند. این پل دو کشور را به هم متصل می‌کند و با گسترش همکاری‌های نظامی و اقتصادی این دو کشور، اهمیت این اتصال نیز افزایش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/71242" target="_blank">📅 17:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71241">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=mKxyLRE9V4th-pN-3TZciGbjvVBwBXZYU93gYXmTDRKl6wDwuTh7XMP3js2H874bQp64fHSilxBhZFmwT8_pr8VQDjRpPiDvlvA6y8mtWJUEpJbG0dckkPBn8PzKtPzim7GAW8D0-1GQ4xfvJJFC2lNkwXKmh4F-GlP6Y_VFidsPlwKyMb1uOikrYO5vCpXeZjIJaUCY9aoMnXZNFO5_7I3iQl5xbfqR-W4EpPzHVGe3AdZy3hYM1FTKqTWm-Wl_ponN2NDCeO_DMawBOkO2dPahotMS0msNfQCMQfc7-IoBZ_HjnrzgJRCkr1R8bOLGekj6JojZ1_yvTXwmBMgJHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=mKxyLRE9V4th-pN-3TZciGbjvVBwBXZYU93gYXmTDRKl6wDwuTh7XMP3js2H874bQp64fHSilxBhZFmwT8_pr8VQDjRpPiDvlvA6y8mtWJUEpJbG0dckkPBn8PzKtPzim7GAW8D0-1GQ4xfvJJFC2lNkwXKmh4F-GlP6Y_VFidsPlwKyMb1uOikrYO5vCpXeZjIJaUCY9aoMnXZNFO5_7I3iQl5xbfqR-W4EpPzHVGe3AdZy3hYM1FTKqTWm-Wl_ponN2NDCeO_DMawBOkO2dPahotMS0msNfQCMQfc7-IoBZ_HjnrzgJRCkr1R8bOLGekj6JojZ1_yvTXwmBMgJHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
معاون وزارت ارتباطات :
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی باید ادامه داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/71241" target="_blank">📅 16:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71240">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=f0_VPEkIvuKgWfX-UzLOP_x1rhsOUSg8KOqJ1z1eYP8OAheNfNEMf-7HKoul764q_F2D8WDHmykubhnPEypc4Wb5-adOdjhArBVeuNk0N3ynJEuAOJTY2l96ogo_5ZPRdsakTVg7irPwjxt86mqIrcgdFYm82raLVWWK-EzSJmPdWEDblgt-ZTG9o9oaNGN9dOI_nDFmaQ6KBpF3EaOSd3uV0RPHH8jPa2mWb_iHeTpE12jr-VTk4dLxMitnHstC88q73syEoRzu3pLi97dAYtsqsL5cgfbJivJKpbWS-USC48GOW9QcrpiHZP1g27CSDUsqj-NdQ-usZyG4EZhbOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=f0_VPEkIvuKgWfX-UzLOP_x1rhsOUSg8KOqJ1z1eYP8OAheNfNEMf-7HKoul764q_F2D8WDHmykubhnPEypc4Wb5-adOdjhArBVeuNk0N3ynJEuAOJTY2l96ogo_5ZPRdsakTVg7irPwjxt86mqIrcgdFYm82raLVWWK-EzSJmPdWEDblgt-ZTG9o9oaNGN9dOI_nDFmaQ6KBpF3EaOSd3uV0RPHH8jPa2mWb_iHeTpE12jr-VTk4dLxMitnHstC88q73syEoRzu3pLi97dAYtsqsL5cgfbJivJKpbWS-USC48GOW9QcrpiHZP1g27CSDUsqj-NdQ-usZyG4EZhbOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آخوند قاسمیان:
برادران یوسف 11/11 وحدت کردن یوسف رو انداختن تو چاه، این که وحدت نیست، وحدت باید حول محور رهبری باشه..
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/71240" target="_blank">📅 16:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71239">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/98f065761f.mp4?token=jHCDmYZkfs-LxY5IonANWtGG1T0fnj9kXgOL9OD1brZIbjUbpwRioTYExs03EbJHVaaI6y-csNTnrqC24jwwhr6dxpsfgu2ID6003oNgId0hk5szXOvUawMHygQN8W5c892FNTB3frvMyxd3qQ7ixrKoCxTotYn2P5jiJu1YpERuDc1PI0TV05INIzuNLZAERjhS_DqrDZVSQ7noLrkGotac6qWVXbaaBKcC7O-IM0DIq2W8PZC4JZfW7xyhkT9NdIANZjTj4d6NSvInIy5FsPEKLbFg6nOhWlstZ4lweFChCD-dqnSeSS4JJPZ_ro_IhFRnDbbmDn04Mb7q_pXwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/98f065761f.mp4?token=jHCDmYZkfs-LxY5IonANWtGG1T0fnj9kXgOL9OD1brZIbjUbpwRioTYExs03EbJHVaaI6y-csNTnrqC24jwwhr6dxpsfgu2ID6003oNgId0hk5szXOvUawMHygQN8W5c892FNTB3frvMyxd3qQ7ixrKoCxTotYn2P5jiJu1YpERuDc1PI0TV05INIzuNLZAERjhS_DqrDZVSQ7noLrkGotac6qWVXbaaBKcC7O-IM0DIq2W8PZC4JZfW7xyhkT9NdIANZjTj4d6NSvInIy5FsPEKLbFg6nOhWlstZ4lweFChCD-dqnSeSS4JJPZ_ro_IhFRnDbbmDn04Mb7q_pXwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رو آورده بودن موقع زایمان پیش زنش باشه و بهش روحیه بده، آخرش دکترا مجبور شدن خودشو درمان کنن
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71239" target="_blank">📅 15:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71238">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f53489458.mp4?token=pJYVHrmZtduj0mc7eMHCS67-r37Yfzcx9efSO-R6Ir3apt-rhOyVBrJjlJqlhjZeaK-uj-dQGZ-hd6gwqWkBOz2Jykp5shOf9_aGnU_xGziy-Pz0skFG_-0AoQV24o6eMPbNLedgYsv5BNCB67082H8Uf88s7m6HgYjgmpciyEurUr9x3A59z2l9WrEBecMRfRylqhQf21tVd-Sy4qlO1W9wYT0ahVgQiW0d2snu4RRFL5Dqp12kM46K1vt4ratgM9tT3TMGCG0SLeqmlNteJopvUiwFh8kGBc79vLAi4t1frGsPH6_yaNmXrHek3gGyBbbnXnX4dioS01QFl_mJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f53489458.mp4?token=pJYVHrmZtduj0mc7eMHCS67-r37Yfzcx9efSO-R6Ir3apt-rhOyVBrJjlJqlhjZeaK-uj-dQGZ-hd6gwqWkBOz2Jykp5shOf9_aGnU_xGziy-Pz0skFG_-0AoQV24o6eMPbNLedgYsv5BNCB67082H8Uf88s7m6HgYjgmpciyEurUr9x3A59z2l9WrEBecMRfRylqhQf21tVd-Sy4qlO1W9wYT0ahVgQiW0d2snu4RRFL5Dqp12kM46K1vt4ratgM9tT3TMGCG0SLeqmlNteJopvUiwFh8kGBc79vLAi4t1frGsPH6_yaNmXrHek3gGyBbbnXnX4dioS01QFl_mJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویدیو وایرال شده از یکی از معلم‌های مملکت :
اگه مدارس امسال مجازی بشه، از گوشیِ شخصی‌ام نمی‌تونم استفاده کنم.
چون پارسال 4 تومن گذاشتم رو حقوقِ 14 تومنیم و این گوشیِ 18 میلیونی رو خریدم.
امسال همین گوشی 70 میلیون تومن شده!
حقوق من چقدر شده بعد ده سال تدریس؟ 20 میلیون تومن...
اگه این گوشی من خراب بشه، دیگه نمی‌تونم گوشی بخرم.
آموزش و پرورش باید به فکر تهیه وسایل آموزشی (گوشی و لپ‌تاب) واسه معلم‌ها باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/71238" target="_blank">📅 15:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71237">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
این خانم ادعا می‌کنه که در جزیره اپستین بوده؛
صداوسیما هم صحبتاش رو پخش کرده.
ادعا کرده که به کل جزیره تجاوز کردن و شرایط بدی بوده.
بعد میگه خداروشکر فقط خودم مصون موندم و بهم تجاوز نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71237" target="_blank">📅 14:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71236">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c603211e44.mp4?token=XEX2PU3dDdyqenO9jn2AClVltmD8OjLGc9EA1vPduK__Nl1PBC7512WbVLPPWOWUflJ5GxeboOyluHbteLYPDG_4yD6dCe891-M-f_jMoNxIv2hphEs53508yYoyTRvoUIXCeu1Ag5djCWsYE8VQzMwS2WQj0J8llSy459CpENmI4xa6dIWhorB2_Z-7hz3bzaP-_-uhHeb2xBKoRxSoTFame-sHP_UTjG_nG3MMxjD_qkiPB4QOWnjVX0vaz9r6TaA1AxalCTUgECGfO6xocwkQ3q6yTZ327-x-iFEX5usBRpgshB7DyKwzqLCvq8Cua7f4PqxzLfjrLvVIo-OFvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c603211e44.mp4?token=XEX2PU3dDdyqenO9jn2AClVltmD8OjLGc9EA1vPduK__Nl1PBC7512WbVLPPWOWUflJ5GxeboOyluHbteLYPDG_4yD6dCe891-M-f_jMoNxIv2hphEs53508yYoyTRvoUIXCeu1Ag5djCWsYE8VQzMwS2WQj0J8llSy459CpENmI4xa6dIWhorB2_Z-7hz3bzaP-_-uhHeb2xBKoRxSoTFame-sHP_UTjG_nG3MMxjD_qkiPB4QOWnjVX0vaz9r6TaA1AxalCTUgECGfO6xocwkQ3q6yTZ327-x-iFEX5usBRpgshB7DyKwzqLCvq8Cua7f4PqxzLfjrLvVIo-OFvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی
:
چهل‌هشت ساعت پیش اولین موشک ناوشکن خودمون رو بالای سر یه ناو آمریکا تست کردیم
واقعاً یک جهنمی به وجود اومد.
🎙
مجری:
موشک بالستیک؟
🇮🇷
محسن رضایی:
موشک خاص حالاااا. موشک خاص
😟
ناوها فرار کردن.
حادثه آنقدر بزرگی هست که سنتکام هم نتونسته نفی بکنه. اعتراف کرده به این
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71236" target="_blank">📅 13:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71235">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJyodev9TSJbtqRTnbqYvVmfkNaneD70bSld43KH2OdEdt8d3YO0UgbqZ-p4gjw-NjgTg_yceNiQwtKpXOgB5olDjuTJnaIizjxnl7IHH5UYeMES0XDDxjGp7xCLZT7xW2oaLd0EmmO6CFW5ZQRLLgoc5FHe7qGTWAxnxFETHy4gSqz_ykDgLlBSz63SlIqBMHkIRacRPP1LKX0ToQVgreatfEp8HnsmpZiCjlpoCjALoVNPM2BP9H_ntdkfujWirjMdTWUnu_ikk8wXyy3W69ryEGYNB05fpc6axwC49cDbmGaLyWFs2PRTE_5Z_i9u81PjAuIIKvFFxC2WqAdipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
⭕️
🇺🇸
👀
افزایش شمار هواپیماهای سوخت‌رسان آمریکا در شبکه مرتبط با عملیات ایران
بر اساس نقشه OSINT منتشرشده توسط DefenceGeek در ۷ سپتامبر ۲۰۲۶، مجموعاً ۱۹۵ فروند هواپیمای سوخت‌رسان KC-135 و KC-46 در شبکه مورد بررسی این نقشه ثبت شده‌اند.
⭕️
جزئیات این آمار:
۱۶۶ فروند KC-135
۲۹ فروند KC-46
مجموع: ۱۹۵ فروند
این نقشه پایگاه‌ها و نقاط مورد استفاده برای مأموریت‌های تانکر در مناطق تحت پوشش CENTCOM و EUCOM را نشان می‌دهد و علاوه بر پایگاه‌های فعلی، برخی پایگاه‌های مورد استفاده قبلی و مسیرهای ترانزیتی را نیز دربر می‌گیرد.
در نسخه فعلی، تعداد KC-135 نسبت به آپدیت قبلی(3 اوت۲۰۲۶ منتشر شده) ۷ فروند و تعداد KC-46 ۲ فروند افزایش نشان داده شده است؛ بنابراین مجموع ثبت‌شده ۹ فروند افزایش داشته است.
منابع مستقل نیز در سال ۲۰۲۶ از به‌کارگیری گسترده تانکرهای KC-135 و KC-46 برای عملیات مرتبط با ایران گزارش داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71235" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71234">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjnQmBBEp_55Q2TdX4Q5aeRiaVgBMQMDakOA8C-_MaxFMFA5o76i329RT4d6eLdR0ZxshXY1gMhkWr1hdVf6D_btpgbC6EsvtnNkTytL_N-ogIte6wWe_OqBV_R-LIoS9sJPr2XljfLLaXLaAYvLpahbYtivWeJnCGpgmGv0U9_qsRHnlvXhJV0cWmmd7yjy2klMRbW3BpGRDDzn0xcNyRNcDlnIH5WvXIKBnBKmgodDHfMApJX-W0iLpYQ_Sk3FBkuvT71oxzCL8lng91BxRSQP4ROiDkV2-jGPrmRVjGMYEA8H-JShtGVd9u1ivoqE_LTMLfFcqDfX9zNwAw6QtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
موضوع ساده است: زنجیره تولید نفت و گاز در اینجا گسترده، در دسترس و آسیب‌پذیر است.
شرکت‌های نفت و گاز آمریکایی که در این آب‌ها و تأسیسات حضور دارند نیز در معرض همین آسیب‌پذیری قرار دارند.
به دارایی‌های ما حمله کنید، ضربه خواهید خورد. ما پیش‌تر این را ثابت کرده‌ایم؛ از پایگاه‌هایی بپرسید که دیگر کارایی ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71234" target="_blank">📅 12:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71233">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=C5-M5xZfIvisoXI4NAiE3-lrFjUDoiSYBk0IOzEfkv_8_e3sziRIsObaGBkSqFDFCtI9GRt26qdaDGT3GYZqlRQAhlO2U9UFBd7LLs5_7DXm_0yt2yvvaWKWDjf5IAV2m-UH1HhR6gpQRSNWmUXrvq-Zl0KqrUEfyC4yiieEVJ1NF_iCyhzVII3dmwjGEYxlje7GSMUCGCIikcLi4n-VAFo0pOliVva0j5mnhHyv4feXEJiXqlUu7wqHEGG529HDw0isXxWfDUpYWhJrTPsLVAfGCwp1Qe7SQo2GLnj8RgG-YNkLEsg2Uo2kuTXaQv1_j5QkdCOQw5ru3_5Lv72ghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=C5-M5xZfIvisoXI4NAiE3-lrFjUDoiSYBk0IOzEfkv_8_e3sziRIsObaGBkSqFDFCtI9GRt26qdaDGT3GYZqlRQAhlO2U9UFBd7LLs5_7DXm_0yt2yvvaWKWDjf5IAV2m-UH1HhR6gpQRSNWmUXrvq-Zl0KqrUEfyC4yiieEVJ1NF_iCyhzVII3dmwjGEYxlje7GSMUCGCIikcLi4n-VAFo0pOliVva0j5mnhHyv4feXEJiXqlUu7wqHEGG529HDw0isXxWfDUpYWhJrTPsLVAfGCwp1Qe7SQo2GLnj8RgG-YNkLEsg2Uo2kuTXaQv1_j5QkdCOQw5ru3_5Lv72ghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بمباران آخرالزمانی پادگان فتح خوش‌نام کرج توسط جنگنده های اسرائیلی در جنگ ۴۰روزه
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71233" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71232">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71232" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71231">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p94bvqQKm_pOqXURIopkPXLDV85Jx2hv7UAwEYWzr_Vzm-4iHMs4Rm8ZD8CnN_4KtRbsflVCDLnwGAsfw1rEC7z7gwRF3lGu8nIlJby3I_7e3EAoZnRNL8rX-DEVfxwXAI0ccu9mxFGoZeAtjkn3XeK3WXnp7m7C05F5MVEB2_vQyxcoiMxFrXvDg0YR4zuwPDBIEIGUSb776ZytYVvDa9Drv2ckrmC0qFWz3WF2gCOjfLWyAPcvEiPOpyXHzyutJLuoYBaOTAC_5zO8Ijq2TjzFuc3o4rLUNXGvg9VixCHKWDX7CXO--ogbzFXLk3pfPlgWhnqh8gs0Goc0eOWLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71231" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71228">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=kUb-8VXwaBRDoD5SYvNrRyxHtR8r8vymk0Qdk-fLaMr9V8V7OGiLVEfMYYkFm0fEc8QUnHdzJ4C4-3Otxf_sPozTmz1SjqbjFYLdVepVsfSAkhuP1dwEwrsnl-sWbgaiHDh61idtfjqUqucqWQeRkepqoM2Xalyxo9-U_cm1wOr0abkgtdSksgVYrE1b9-GP8KlkefhmRTCgeY6qbm3c-YPhOGpXG8Ofs_zKKn4YGsWjCX1qFWRFD0k5fwOULoZyET03Rk3own8P11ufl272ih1Rmall6uqR0LhpHk7xRNtAZU9zHQHgVK6nDdeyf4zHXcD2LHqkKmytlAFaA8PPog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=kUb-8VXwaBRDoD5SYvNrRyxHtR8r8vymk0Qdk-fLaMr9V8V7OGiLVEfMYYkFm0fEc8QUnHdzJ4C4-3Otxf_sPozTmz1SjqbjFYLdVepVsfSAkhuP1dwEwrsnl-sWbgaiHDh61idtfjqUqucqWQeRkepqoM2Xalyxo9-U_cm1wOr0abkgtdSksgVYrE1b9-GP8KlkefhmRTCgeY6qbm3c-YPhOGpXG8Ofs_zKKn4YGsWjCX1qFWRFD0k5fwOULoZyET03Rk3own8P11ufl272ih1Rmall6uqR0LhpHk7xRNtAZU9zHQHgVK6nDdeyf4zHXcD2LHqkKmytlAFaA8PPog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇶
#فوری
؛ بیش از ۱۵۰ ایرانی به دانشجویان عراقی در سمنان حمله کردند.
🎙
به نوشته خبرنگار بغداد الیوم در سمنان:
گروهی که این رسانه تعدادشان را بیش از ۱۵۰ نفر اعلام کرده، به محل اسکان دانشجویان عراقی در دانشگاه سمنان حمله کرده‌اند.
گزارش ادعا می‌کند پلیس پس از اطلاع از حادثه به دانشگاه رسیده، اما هیچ‌یک از مهاجمان را بازداشت نکرده و صرفاً تلاش کرده درگیری را متوقف کند.
طبق این گزارش، مهاجمان وارد محوطه محل اقامت دانشجویان شده و تعدادی از دانشجویان را به‌شدت مورد ضرب‌وشتم قرار داده‌اند و در نتیجه، شماری از آنها زخمی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71228" target="_blank">📅 11:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71227">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=lx-CWXgzRkNJKGXaeHqI-6s78EAbOjZQlvD0anoD54Oic4K2JMYlBbUUVv_DHh-oACJ8K9_wNQ_L9yc6XPHJocPsyeg9CrRWsBk_zzKMmVhxZx4ZlMhOV9VUj_85JCBLrDk0N3tHZugb_GWoJNW1CbrBLXafllkdjP4FxKD6gimdoUMSTsAb0zojHDL1zhstiSKChMVw72BSbVwZQELrR87_hb05d2ZAOmEajHSN8qcVsMoejUwbJFvAMu9DpQ1aGhI6vEA0Oo_trJFDE4t4dYbIp5Ujt3r_vQP2_URKuvEqzyBimykY-ql3DqbeKtxHXonElAaGPlfc2Nm93T08Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=lx-CWXgzRkNJKGXaeHqI-6s78EAbOjZQlvD0anoD54Oic4K2JMYlBbUUVv_DHh-oACJ8K9_wNQ_L9yc6XPHJocPsyeg9CrRWsBk_zzKMmVhxZx4ZlMhOV9VUj_85JCBLrDk0N3tHZugb_GWoJNW1CbrBLXafllkdjP4FxKD6gimdoUMSTsAb0zojHDL1zhstiSKChMVw72BSbVwZQELrR87_hb05d2ZAOmEajHSN8qcVsMoejUwbJFvAMu9DpQ1aGhI6vEA0Oo_trJFDE4t4dYbIp5Ujt3r_vQP2_URKuvEqzyBimykY-ql3DqbeKtxHXonElAaGPlfc2Nm93T08Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از روز انتخابات دانش‌آموزان پایه هفتم آمریکا که این پسره ادای ترامپ درمیاره و مثل ترامپ وعده میده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71227" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71226">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc7xOlfY3YqTvPdydwii0dsipJOdwcfE0nO5xdQnm53Zl0oekTCgQioAGbK4Toup70ccF3ygrIf8tuFCnEeJaMqAGic6D0nqlbBQLlzHJ08J3-bWm_sCKWcmXkokc-vNuix0Ky-35opzmIGMvD6uV7BqgReM8sbXPetcZlNQGGU9kdAbixmbInnHk-QyF1BJ97f5IAQKdGYE1UchuXBojwsDVYI_86E7z9JfWZqMuCZ70NaRqCVJlUbExBBFReqSclRIhuNFvPa7RUfrG0XZ4SgxM3kyDS4KOm81iCLuwJhqRHsXqw8p1k5qTfFGTl9gZqgQbRx9lkzDlFIdCDrVLX99E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc7xOlfY3YqTvPdydwii0dsipJOdwcfE0nO5xdQnm53Zl0oekTCgQioAGbK4Toup70ccF3ygrIf8tuFCnEeJaMqAGic6D0nqlbBQLlzHJ08J3-bWm_sCKWcmXkokc-vNuix0Ky-35opzmIGMvD6uV7BqgReM8sbXPetcZlNQGGU9kdAbixmbInnHk-QyF1BJ97f5IAQKdGYE1UchuXBojwsDVYI_86E7z9JfWZqMuCZ70NaRqCVJlUbExBBFReqSclRIhuNFvPa7RUfrG0XZ4SgxM3kyDS4KOm81iCLuwJhqRHsXqw8p1k5qTfFGTl9gZqgQbRx9lkzDlFIdCDrVLX99E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرفداران حکومت یه بازی ساختن که برگرفته از بازی مافیاست و فقط نام نقش ها فرق میکنه.
در این دور از بازیا ترامپ برنده میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71226" target="_blank">📅 11:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71225">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=IiATQjNxL22OdKVjCDqxcoxy7bG66vheSXU7J6X5AI1CYTm6m9SmZ9jYXhTPlc_yPsNCOchMDh1flO3-hJyy_bvipUs3bAWrPZAYk0ZjLo8FpWCwXoWSNDe_PmTKbd2aoj9Zk2h5PK-BgPr1wkgBWAELBVj20hud3jg7CccQVM18BzWf3fHobbSuY2B0g5K8fjPXlwjnO1av76tBlOoNLSbnZXrI56mt03UPR-YAyeLZvXRuku8ETWI89hfHqvMs9qQYKsYOVHUQabf79G5T4GJCAWD99Vl6xz2D_plSKFbdB-FD5tRvHoyPA_DcG3txj0UVEfK7Qx2djgkDa-XYXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=IiATQjNxL22OdKVjCDqxcoxy7bG66vheSXU7J6X5AI1CYTm6m9SmZ9jYXhTPlc_yPsNCOchMDh1flO3-hJyy_bvipUs3bAWrPZAYk0ZjLo8FpWCwXoWSNDe_PmTKbd2aoj9Zk2h5PK-BgPr1wkgBWAELBVj20hud3jg7CccQVM18BzWf3fHobbSuY2B0g5K8fjPXlwjnO1av76tBlOoNLSbnZXrI56mt03UPR-YAyeLZvXRuku8ETWI89hfHqvMs9qQYKsYOVHUQabf79G5T4GJCAWD99Vl6xz2D_plSKFbdB-FD5tRvHoyPA_DcG3txj0UVEfK7Qx2djgkDa-XYXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای عجیب یه آفریقاییِ سیاه‌پوستِ ساکن ایران:
خیلی از کاکولدها به پیجم دایرکت میدن و اصرار میکنن که بیا وارد رابطه‌مون بشو و با زنم بخواب!
حتی یکی‌شون می‌گفت هرچقدر پول بخوای بهت میدیم تو فقط بیا..
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71225" target="_blank">📅 10:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71224">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-D3vaiopHeDL6i71Us6X9JGOLM3xXvFFML91idN0RPTP7wj1DQdbLYAJZwTpw9YDggwx4nvaKpSD2Gisgjntrk0uQoy0J8HyAkiTzu2rNrkti6HORrRxcGqNYhHcaO_yH5yChxj4GXYHZ2wIdjfDsROPmyYPNQYre5T7VFq6c03CrryVA5FFbbDhKmrqjuytAXkfUHQQHppJQJv5r6UU1aZQusOLBwqA8zcn2uVOYW0qwBJDaGYcQwaaTPDfBxlDZx0zU7oHjPiAxJJRGzw-rDGfOIKroW9zoNfE9AivDM9XJV-dSRXxY1D2wOdC7HATRKh_jkqCLossiF59us0_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
شاهزاده رضا پهلوی:
هم‌میهنان،
جمهوری اسلامی بار دیگر با افزایش قیمت بنزین، هزینه بی‌کفایتی، فساد و جنگ‌افروزی خود را بر دوش مردم ایران گذاشت.
همان‌گونه که در پیام ۳۱ مرداد گفتم، گران کردن سوخت در شرایطی که مردم زیر فشار سنگین اقتصادی قرار دارند، اقدامی ظالمانه و خیانت به ملت ایران است.
به رژیم ضحاکی و رهبر مفقودش می‌گویم: فقر و فشار اقتصادی که بر مردم ایران تحمیل کرده‌اید، نتیجه مستقیم سیاست‌های ویرانگر شماست. منابع کشور متعلق به مردم ایران است؛ نه برای پر کردن جیب مافیاها و نه برای تأمین مالی تروریسم و جنگ‌افروزی. اموال غارت‌شده ملت را بازگردانید و حمایت از تروریست‌ها را قطع کنید.
گمان نکنید با کشتار ده‌ها هزار میهن‌پرست توانسته‌اید اراده ملت را درهم بشکنید. آتش خشم و اعتراض مردم خاموش نشده است. ملتی که برای آزادی، رفاه و آینده‌ای بهتر ایستاده است، در برابر سرکوب، فساد، بی‌کفایتی و تحمیل فقر سکوت نخواهد کرد.
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71224" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71223">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSmqNrObdN7aS56l-NSEl--SurarUuVJJTYayUghUfZOEne5s_4EoiRZ8_UPnIHxLnhY1hUlCHTkwXOVePDiZiojVXuAGQRhqpi-kW56GEASWQBy4YSaLxaiRyJYS8xg2q-OZT6Vwa1OnAB22s2k6R5jYTqYOwgLqjB1i9LtVjA2Jp2E6nwjkWVpI9SxM5GLTdlmbT12LxYznsjmp5OKWJ2-cb_qUM7z4U9Tp0G_JjK6cWi4x4NI_m_CAHN2gvfhJkhURHxXf7iaH1z46clwUWkUNBfv40j67UuhBiof4amnh2zwUAJusYVJOveJtkMkZstf51PbE0jxJk2fDCffZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/71223" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71222">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=K0Koly-oS4LP4CcErPiod32F0Q79ONxegOv2rTLAgDpPA1df3-4oRElvtcSksF2ZoTj1m7fijaqlq2JM3mAcYMP-wbVBGqh7tWCwOWxa5aJuEjOs8KgFqU7Bsla4XDjZE-On2UrmznPEhtZHsp7Vhp16gGhrJDanWvQNMExZprMa6ChYw5Tjh_MHQp-_W42xQjm0NJLHYwrpsjiB97CvJx87rg-HCWPRHlFsfkM6VayTzPx3UQ6Q31gib0hrafnTzgBORoo2A05q7dJrRyVoaajj1z2bH7z3F4pn8J_7YcVZtTjNviUQKgXqaectp13gyCoLKhCMSAeCm2oKN_zf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=K0Koly-oS4LP4CcErPiod32F0Q79ONxegOv2rTLAgDpPA1df3-4oRElvtcSksF2ZoTj1m7fijaqlq2JM3mAcYMP-wbVBGqh7tWCwOWxa5aJuEjOs8KgFqU7Bsla4XDjZE-On2UrmznPEhtZHsp7Vhp16gGhrJDanWvQNMExZprMa6ChYw5Tjh_MHQp-_W42xQjm0NJLHYwrpsjiB97CvJx87rg-HCWPRHlFsfkM6VayTzPx3UQ6Q31gib0hrafnTzgBORoo2A05q7dJrRyVoaajj1z2bH7z3F4pn8J_7YcVZtTjNviUQKgXqaectp13gyCoLKhCMSAeCm2oKN_zf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک سرهنگ ارتش :
از فرمانده‌ی کل ارتش ایران تقاضا دارم، یه قایق پر از بمب با جلیقه انتحاری در اختیار من قرار دهد تا خودم را به ناو آمریکایی بزنم و منفجرشان کنم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71222" target="_blank">📅 09:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71221">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=TZ_grNtz53sKbLuuoPT-XTHI-0Yh-9d2UvguoSzBFFbUd-0o70WHtxSuketPBLq6TNbbccCeFMtFWR_ul34XBF1L6EzmFahUin4416RA2b8cL2gKN4EtxiR0y5oUKkuh6hRvRtE1dqS5SRKW1FMisJx23RSgNpLv9D1vvdVQeB3Mk2Ozh8HWBHVkaF3C5CkB1_OLf_-Ubypc_fKa49K4E1UnrF8q28JSMVwNW4QghBV0hkZyUiTxVZL1GR69SsP8JCBwW7oImAD7QWD2E-W9retSesHUr8oPW9lAGUrbIWPljDOCL1SRoDkRKqNSsCKnrnlfHX0PM1_UDL1T3qdQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=TZ_grNtz53sKbLuuoPT-XTHI-0Yh-9d2UvguoSzBFFbUd-0o70WHtxSuketPBLq6TNbbccCeFMtFWR_ul34XBF1L6EzmFahUin4416RA2b8cL2gKN4EtxiR0y5oUKkuh6hRvRtE1dqS5SRKW1FMisJx23RSgNpLv9D1vvdVQeB3Mk2Ozh8HWBHVkaF3C5CkB1_OLf_-Ubypc_fKa49K4E1UnrF8q28JSMVwNW4QghBV0hkZyUiTxVZL1GR69SsP8JCBwW7oImAD7QWD2E-W9retSesHUr8oPW9lAGUrbIWPljDOCL1SRoDkRKqNSsCKnrnlfHX0PM1_UDL1T3qdQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان زمان انتخابات:
خیلی‌ها میگن من اگه رئیس‌جمهور بشم میخوام بنزین رو گرون کنم، ولی من بارها گفتم بنزین رو گرون نخواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71221" target="_blank">📅 09:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71220">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71220" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71220" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71219">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_dX66uuWYUSmLfbvOrsPm-bsW1QvFAfKGCqu7_nBdLDK9aMJrYauLiiioCCD80mvD4WNG5uJ0NYSyw2WdWwgd8cTP4TWmh2q7rca66QXoptbLRgWcybuhAQi1gh6OvQzzWZrg67tGFfqZmjE6Cg2bGgSEKKoMYg28YB8xGddViDO-wM9H8jBKP8qvH5bKrwPxnJmrDemh1oeQD-Nm_GShvdSd8BuhgxvDNsgrjqEEbFi0cNLv6fuDEo1dhRd62U0q7Lt-ll97_lYk5SJuJlmMm3SdvtuyduK0kwDl2tAr_9ixw_abOJmu1WBR_vWJO4HqSxBAz-a_OU5D2eD2fw6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71219" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0E4xZPkAc6aZT3ZofH1g_ie-1A0jh5qbj4O08C9KZV0OZ6jFQgjiD6d5SmJqfEB92JrYXIez55N6xI4oeHdeFCUGTZuFQr-XKqX4mPvE1lVOIOZrXfYPzHSq4Upsoa2DnapzDHdsJhj3_oQU3j-dQNiftgxll9G4lGEaTGPfiogPX7y_BwllJIdE_N6u1Z22z6_DqUfFxIsqffF7S3M8ceIz741cwZzP4mATohotkIqiJswXn1MxcrPWiHjTO41UqRG1uKdqHIDzptFLFYxR3OYuum9wN9i6XuP6oQqOSUNU0pY5Maa7ZkPkehp01FA6SRkHpAM_wy8ikP5cf2pgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ee_2EpSZrHFA9mv67s_iON9S9GVUM89s7gGhpoCTELOa7_H7Ty9nAAmEb83nVEB-KBrVZ5TsETCBxeB1R8Y7ZVDq-vY-OdWYC9hE2EaK3Zrrkqs4lh5aOSQz0rkZ5nUAlrY_wA53xHBFteBdBLIGwdDuLx_9Dlb_nPEFUarsYSsH-PONhEdEUgUrTLr1XjU93w-vrDotB6aoUdMO4p84xw7skPwKc2RPNTbrl8ut6cetxtmXfRNJBUUCENqlbzZ5jJCtu28i-NR9Omzdaw30zqnRiqS2jIXbANcEzPPf8GGIuiFisBGtRkkEm23qkSdeJBFZD0d9TsOv-WUSGRs2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9zTAgICxK6ne7zMlyWPhAEwUHmUAD_uGm1fSc81e7pRVZSqwSXx4WTDCh_WHWdnVed62vn_-_keD4lHlqvQ3VCOnBnsvXDMquFS2_IhMysCKX3keR4OsAjDEIPLRMB8ram_x5GtlnipSOqU7A2tUwINlQEnbEipSK37TSlhrcW_jEznubCeJTY2r1f29S07s-EFAxWnnxcfZeMslAb5JAc49fdZ8pykdI-YrS5bfL3klG85xATT5IOCptUo0vbXNezhuWkCjRJJH0kIo9semjpvlLBpPd8jRgFLiQP56P0PN_amB8l2yXVHp7DbAcyY3e9xUWRofjrCWrhGlC7j7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HhY0N0_-hSTOIG5IeSPqwwlaTHKv4oxqzUz8o_-_VqRs4RxhytnXNQF2Wxvx2VzXf1WL9TIMMXt6nuxhxr3WuIySnpk6SCzShT8Jg7Zkkaf-9ldSuy1gDBT7Z-TSVS3bZy2WmOaNCV3ciC5bAQZSm5x1awnMAZz56Imh3mCBVJojQkxY-7xdsZn5qP10ndCOPm2GHsNGKvT0TuanHORfJkrZImwpeOMQknlsMQ3plLwayLZdqayW6BIA408rRvp9pOE_xK0SLNXaY7PjRObQMkJrnzBhf5wwpnESs_MAsI8lU93Pn5pyR5gi9PyZhrVnictqDpfJmv-SabDdz-MJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoYHUb-4FFm8B-cx34VISggXutLcwvZU3y0Wptq3bCU7rgJVQaHYLpKemkTqot_Uh_V9ore6mLwedWir1aoOocInRVaGxzVhO-Pgo_Lc8uESkt9O0q7D_Gyo1mU6lbC-Pzmad-47U7aggfiytTde19xa0LbDIxoLL9YjpmiOBspgEEXj4YxDJ1ozKND_KFzg4e6icSY6v9ZuvQgJ-nFAbzwC0bUmHDVeLBDaLr9jzomfK0O2hZvhB87EtOL0QDwnfDyIT1SEe9gUMJdR22Vf4UXufTL0eEUwZRj7_cdeo5N0-yMqD9NY6QfWarMuWQdBE-4Ftu4S_YT6zEb4tmKV4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ:
۱_ایران کشوری در حال فروپاشی‌ست.
۲_خداحافظ جزیره خارک.
۳_ارزش پول ایران از بین رفته است.
۴_صادرات نفت ایران به شدت در حال سقوط است.
۵_ حجم‌های نفت هرمز به سطح قبلی بازگشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71214" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71210">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUzHzQVto53Di7K_nZNNiX4Y_ageeh1jmnoElFKaWwMa5jAuVk0IeT_5jTjsnS9aGEX1PbeFXxNcvFtZeQRf52ykxt6qPETT3K_02ehDKSs--r9IGOyF5tvxWPzKo1GKuzrPBYv2OHLPGyUW2YRf8rnoJES_WxvmJfpdRFGqP2x2EkPbj1i7Yb3QF2R7nDCuASKQF_B6cAgs6L-Uj9bpLDV8h8xh3TpocMtVrsLExFMWEQZojCbzxNxRcxlV89cCiYG5FIkyghwxgeZpytWIIfh4oGEOKAckzvW4Sa_GLiyHwFpZhZu2NbejyNoAE3dsPOBag2EPqg0S-Ju4QLhQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukwPW8gFaTgxgG12ti1a3AkYI4umfmY9jT4MW0dP9sTJrYHJDfiv7SQYRbQWlVE_UArsd9scgFPX3a4e8Go_scdZo2Au9TiOBN_i8oSFnwvTlmDYn2AvHjGaY7cuKnxUrln7Rhk8woKjWbWHDJiCwr2NB6CgRl0nsaMdjwX-gq9msOONRQsKf2sJW4qLJMtiuA_wdpFbEyZwkCWxPpZNRgoKP61ae1YwEJxdeDQ2ZsY6FQa9aiqmjBLSABXbPDPbibwjW0UN83kqQVhaMpeT0pnUp5Qm1C-iRx5eobdVtNVcUV6HCn5I2hMEnMxSCJi1ZaxQg83TRm_KMpIJV6q1pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ در تروث سوشال منتشر کرده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71210" target="_blank">📅 00:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71209">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=LO37DWnjnWQdhGRjcxnBimJoidHRtsKAmiP8c75Ajcu0-HbdpkHDmbeJzgCPYOqdvpRmM6poDKR9aPLCulKvve4v7mfATdayx2ARMqHqLF3Qm38SmsvRIBhA7JFiD75Al38_8hjy-GknM3MTnpQvD3USmpMxhBhybC7B7c-8JFq9hEYrwqLwShw7RGwOixEHGwZlB0Jqtqd4PCpu_yl6vS4UzcmgzlVlrZMQ1o0KFhc20FAcjeDNc5uGQDsppdxVtT3--pLsJG7NN6LlL68d2uBQMv-ZsVEUkxbL4nxalJdWzyhYU_7qLq7r6Ep8q1sKom-sE6Th8KUXrT69pHb4fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=LO37DWnjnWQdhGRjcxnBimJoidHRtsKAmiP8c75Ajcu0-HbdpkHDmbeJzgCPYOqdvpRmM6poDKR9aPLCulKvve4v7mfATdayx2ARMqHqLF3Qm38SmsvRIBhA7JFiD75Al38_8hjy-GknM3MTnpQvD3USmpMxhBhybC7B7c-8JFq9hEYrwqLwShw7RGwOixEHGwZlB0Jqtqd4PCpu_yl6vS4UzcmgzlVlrZMQ1o0KFhc20FAcjeDNc5uGQDsppdxVtT3--pLsJG7NN6LlL68d2uBQMv-ZsVEUkxbL4nxalJdWzyhYU_7qLq7r6Ep8q1sKom-sE6Th8KUXrT69pHb4fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دو عدد سیب زمینی 100 هزار تومان؛ اینکه قیمت یه دونه سیب زمینی بزرگ‌ به ۵۰ هزار تومن رسیده‌؛ یعنی فاجعه اقتصادی.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71209" target="_blank">📅 23:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71208">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=OUqhq8-TxFUyxcpsJ7OUatjZzOcc46amBAci24v0DESb5zqLa-Tw5oBJ1DiCUEgIIy5dh-xeqy-KzDmD8J09ybniCCDS4iABhDuyPIXOlyNOII68tiK7N2oCKgd9eijOVAFjCrrfnLGyedJv6z3a5u6o0URYMen6CUWNideEaBwY6wE5spilEsdSOCfBqBl3bmdB9bn2zWGvmeEXO-AtOhLg1AA5FabNvBqOpmGimP9yIIytfN-Y08EJUyc23D3kTW3ooQnG-b2lxejBnq1kq70QqZqWbSDDpoKhsCwBe0r5cvfJK5s2Fz3tJYxeH1GzZtgc0rajyaGtyaXiQP4cBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=OUqhq8-TxFUyxcpsJ7OUatjZzOcc46amBAci24v0DESb5zqLa-Tw5oBJ1DiCUEgIIy5dh-xeqy-KzDmD8J09ybniCCDS4iABhDuyPIXOlyNOII68tiK7N2oCKgd9eijOVAFjCrrfnLGyedJv6z3a5u6o0URYMen6CUWNideEaBwY6wE5spilEsdSOCfBqBl3bmdB9bn2zWGvmeEXO-AtOhLg1AA5FabNvBqOpmGimP9yIIytfN-Y08EJUyc23D3kTW3ooQnG-b2lxejBnq1kq70QqZqWbSDDpoKhsCwBe0r5cvfJK5s2Fz3tJYxeH1GzZtgc0rajyaGtyaXiQP4cBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سعید لیلاز، اقتصاددان و کارشناس اقتصادی:
«کشور با تذبذب و دودلی، مس‌مس کردن و فس‌فس کردن  اداره نمی‌شود و حکومت باید تصمیم‌های قاطع بگیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71208" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71207">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7BqdoufWeadF56iZ4tuSmS3u0baDYhFhFmah1q_IkkuFNf-ffkYh2hRa4hybFSbKBmCoWMGLpuxf0PIqrkuTjWt5DBFAMEna7Ry8TWwCFCtMCOw7FAMQ-xgr1m4oj5py9xXrp0MH7MzMg__YA2er81BxQ4cv-aU5bfMBRhsIobt8kJt3fed0Qh7MOOzvZ8cgclumhZvFYqgGR_UID8B1ZklPkcOv329n9NZGi6VRbty3xF1tu-S6yToaERONXbJOR7wSA73kLwKSskPQb4LMOD5G-cEFxavqKSkbTRMydL5Mv1dVm79DH-dxhITEHF7tJkRrc-pA1JmLzgw3EHx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث که اومده کلشو جای نقشه ایران گذاشته
😟
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71207" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71206">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=Sk7WfeBqNv7VdNpZQNCUKhQwlI1sohj4swVInAd5X5JfAL1vJlA5h-NCgVNGYz0mmFo3Hvs5l_gUZ3YPkRJJWPWmFzZGG_8gnF8EOuMVks_7WAJ7ivPAbui6Sa9fZ5I3hB838gpt2dmVQZxKx3NVHpiFt9xuJRYplRZeW4oLZjcwbufuG808EQhN7vD2X44LDsoLXSvwDDu6MxsCG4EXzK2q-O_vrhH5ddgLAKLOJJpuX9DrOf4dBhhkNTsVdATIHdeLYaBG6fbHD2M-9LASGebss5HWDe53yYPRaXuD4SoRE6VSwx2z-tdmGd4u_HPP2s3Uf4RvJ6bImi8S5aqmwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=Sk7WfeBqNv7VdNpZQNCUKhQwlI1sohj4swVInAd5X5JfAL1vJlA5h-NCgVNGYz0mmFo3Hvs5l_gUZ3YPkRJJWPWmFzZGG_8gnF8EOuMVks_7WAJ7ivPAbui6Sa9fZ5I3hB838gpt2dmVQZxKx3NVHpiFt9xuJRYplRZeW4oLZjcwbufuG808EQhN7vD2X44LDsoLXSvwDDu6MxsCG4EXzK2q-O_vrhH5ddgLAKLOJJpuX9DrOf4dBhhkNTsVdATIHdeLYaBG6fbHD2M-9LASGebss5HWDe53yYPRaXuD4SoRE6VSwx2z-tdmGd4u_HPP2s3Uf4RvJ6bImi8S5aqmwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مجری لبنانی:
مجتبی خامنه‌ای، رهبر عالی و ولی‌فقیه، اگر به بیروت بیاید باید بداند که هویت ما عربی است، نه فارسی.
بگذارید این را به روشنی دریابد: اینجا بیروت است، نه تهران؛
اینجا پایتختی عربی و آزاد است و هرگز به پایتختی فارسی بدل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71206" target="_blank">📅 21:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71205">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⭕️
#فوری
؛ نرخ سوم بنزین تغییر کرد
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71205" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsEW18nRlbz5LICQ_5147bZEvGbCjAYAK-rPYIrL0Ju81jYXoB6aTzH_MDmfB3YICeqk2AVv9en3T3Lq2wwWaOuO0a2WWSlERhcYMEaSSuwVFqye6laGo_3iuONKqFlsFGtgcMopDLCT_jJJHc2gWzp3h1Aef8Gk0OXagZEoEdJBlcLBjJsIsnhElwFbk4aHDlzuDtin_GjnvDBauSf4140ixrs3kJDD5qLpVkcBQvr9iJoK_8JUuqeg3omqODBamLZW9b1AV31RMRQZraKPJ9PBjH1Agg4ntLI7AcfAMEnvU2zLEjisb7NBowHw_iPSPCCPVVSZNfPa4HSkgIkitw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fw15b8Yc2_mf9BIDl-7Jdm7T0RsX55jDtHhR430GJp_EulfjyCuwlv6Yh8zyrccuv0GiL0T3F_mHy05Ftj5Ssv4xeO4Lk0fpBnXI52QnHggy_PqKW8NGJ4qIAMBD1me2X8Cz6gt3JI-gTY40-U0CjBlkq5OlzYQJ4WgQ0M0xANBY37vwac9YPVcAbb8asG54RyARG49qnOaUoIDCjmZnPhMq0vI5KB6KO39Q_4X8yo175jx46BqJ6fU-KGkRr7tVuU03Uwcay4s1eae3o5P-EW5gUjl0QCfYS_0oRDD3wESfUX-UibLLqgaWOlf_5Yuyr4iPUFu950e0O67RQl_IDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=eDu1ziQWZ7AGYS5JPJ6XanqNK7f8rqhtQnwLtYhfhTtqgaey308jRC76Ye3V3Hia1FOabEfSOG1-UpooJ95fT2AkhTfqMYrdJ3-HG5meEA1GBzesSv5kPhQ8oSaOg7C_J2H3Mjz7iXc5IebtVI4udIS9EOMZ1n_h9F--fL5wK2UE-rhD_voS7YS6IHfliudP08osHcwNOBAPXR2W-fs3OGo1srEW7knFOhGuIeWYSqahgmcbjz_Kx9lUXxbjJ_1voOlJJDh6zUO4_jWoKmBxIU2qVoZ21dnpgJ6zlvuyMZaEITP-pzW3PKVxOKgzM16icucKIf38L9dh5m1ItEodXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=eDu1ziQWZ7AGYS5JPJ6XanqNK7f8rqhtQnwLtYhfhTtqgaey308jRC76Ye3V3Hia1FOabEfSOG1-UpooJ95fT2AkhTfqMYrdJ3-HG5meEA1GBzesSv5kPhQ8oSaOg7C_J2H3Mjz7iXc5IebtVI4udIS9EOMZ1n_h9F--fL5wK2UE-rhD_voS7YS6IHfliudP08osHcwNOBAPXR2W-fs3OGo1srEW7knFOhGuIeWYSqahgmcbjz_Kx9lUXxbjJ_1voOlJJDh6zUO4_jWoKmBxIU2qVoZ21dnpgJ6zlvuyMZaEITP-pzW3PKVxOKgzM16icucKIf38L9dh5m1ItEodXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
حملات شبانه جنگنده های اسرائیلی به ارتفاعات علی الطاهر و نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a237cee509.mp4?token=IpqMbvJyf4bTm44WIK4ajsv3eSUWTy0kheMC-nSgHGlhlPWgSR-Y1h3CBPspl-tH4oSoMRkt9X5oyuYY-ROwtnNRC4YGDYrIyeuWMhAhEfDa8PaQlaEdpoIBdsu---N6PdX8-T480y3HJftWMiT5Kk7v3HpKU3hiJZIamVamsgowjp10eeT1Za6-TTYpkIs2H28ba2e3e_YjxmwJ5cxV9QTaP6myR0-cUuTNXS2ya1f203ESfZCG4dPMKTUaxAuYOkp479xH7npqLjH5eYApfMC2pU31b8vPPtOBjCt4E_ENntb_d-_SPTFVp3m-Szzfpuqea5jStnfUTMgGWC6Swg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a237cee509.mp4?token=IpqMbvJyf4bTm44WIK4ajsv3eSUWTy0kheMC-nSgHGlhlPWgSR-Y1h3CBPspl-tH4oSoMRkt9X5oyuYY-ROwtnNRC4YGDYrIyeuWMhAhEfDa8PaQlaEdpoIBdsu---N6PdX8-T480y3HJftWMiT5Kk7v3HpKU3hiJZIamVamsgowjp10eeT1Za6-TTYpkIs2H28ba2e3e_YjxmwJ5cxV9QTaP6myR0-cUuTNXS2ya1f203ESfZCG4dPMKTUaxAuYOkp479xH7npqLjH5eYApfMC2pU31b8vPPtOBjCt4E_ENntb_d-_SPTFVp3m-Szzfpuqea5jStnfUTMgGWC6Swg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زاکانی:از وصیت‌نامه علی خامنه‌ای خبری نیست، احتمالا در بمباران از بین رفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71200" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90305378ee.mp4?token=EgGqNedj0WFq_U_ZV5Z0XtdfyErU1yKtSW7_Gt1DPb6xsCWW8BDKt8EGQHmV_2RFhsp5hdZGdJg6HKftPXvUQ3tbBzufaq-TjpWsHncIL3hDP6s1bsD0xve_4nKyadbx-sG0bmH2jnHxU-QjI_542vkBxNKEGGt2MFP___Q_BQgIbqH6irSxMhb5SaZ3a5nPAyCgPMrleaKtk0xx56Al3HDIKcyTDKVBzCqsnVpaWQqTD5ol6EC_RcxtzMjHNSeKdKnrUIQ9Cj7QeEnk_WKlJ377CDO0j5xSrefl85heIvZeD0lNQzaV7XkDo60uVdkncEvIdcESWPprlAvaxyg_1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90305378ee.mp4?token=EgGqNedj0WFq_U_ZV5Z0XtdfyErU1yKtSW7_Gt1DPb6xsCWW8BDKt8EGQHmV_2RFhsp5hdZGdJg6HKftPXvUQ3tbBzufaq-TjpWsHncIL3hDP6s1bsD0xve_4nKyadbx-sG0bmH2jnHxU-QjI_542vkBxNKEGGt2MFP___Q_BQgIbqH6irSxMhb5SaZ3a5nPAyCgPMrleaKtk0xx56Al3HDIKcyTDKVBzCqsnVpaWQqTD5ol6EC_RcxtzMjHNSeKdKnrUIQ9Cj7QeEnk_WKlJ377CDO0j5xSrefl85heIvZeD0lNQzaV7XkDo60uVdkncEvIdcESWPprlAvaxyg_1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇵🇰
بلاتکلیفی بیش از یک‌هفته‌ای صدها راننده ترانزیت ایرانی در نقطه صفر مرزی پاکستان
این سنگین‌سواران ١۴ شهریور در ویدیویی گفتند که بی آب، غذا و امکانات بهداشتی به حال خود رها شده‌اند. با اتمام سوخت یخچال‌ها، بارهای فاسدشدنی در آستانه نابودی است و گمرک هیچ‌یک از دو کشور پاسخگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71199" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71198">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بیناموسا مگه نگفتین از امروز برق نمی‌ره؟ رفت که
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71198" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=DuZG3iAfUZs6DGVeu0FUits6pNItlDSgYp6uprxYKy_4t81_J_IBgHxJqySJsAtPIarAutOAolbS_vHKRR1Dz9EE8yPkX5SzrKyECw_Z1sYed5pHjwQUB-T45N5g_b1rCmWwoqaPiT0skvh12OuUv-GYUcLcPOJOPNWotsjaijnWg0_S9LKhwRKgnTEM0YGgtYhqgmW095kh14V7HSYnzgoUWWmUJwvbcfLMLJqQ6O4sOfiEIi57LY9K_bxQaEbR986VOL-gNvOc4_6hdmKUYgDBIe3KEibex0UPfVDwpiay-znvKhIRokKSfIPEGFyZ3TfyO_QIQH4r_EqIzR0HaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=DuZG3iAfUZs6DGVeu0FUits6pNItlDSgYp6uprxYKy_4t81_J_IBgHxJqySJsAtPIarAutOAolbS_vHKRR1Dz9EE8yPkX5SzrKyECw_Z1sYed5pHjwQUB-T45N5g_b1rCmWwoqaPiT0skvh12OuUv-GYUcLcPOJOPNWotsjaijnWg0_S9LKhwRKgnTEM0YGgtYhqgmW095kh14V7HSYnzgoUWWmUJwvbcfLMLJqQ6O4sOfiEIi57LY9K_bxQaEbR986VOL-gNvOc4_6hdmKUYgDBIe3KEibex0UPfVDwpiay-znvKhIRokKSfIPEGFyZ3TfyO_QIQH4r_EqIzR0HaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
پایان این رژیم در ایران نزدیک است.
این رژیم ضعیف است، برای بقای خود می‌جنگد، متزلزل شده است و هنوز مأموریتی ناتمام باقی مانده که ما مصمم به انجام آن هستیم.
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71197" target="_blank">📅 19:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jby_4ld3E8ns5z3uExUcIM-zpLq-RoBl48hc8--LS1mPpv9IOtZAzACoQZ-yopPSvhGSdMPBdYcQLh1OnfXcPLfZlGEDe1V0fzznWVSM_cQF-shV7OLzmBI1LFNeTO31JEV3K0Ot8Y7Hi6-mv4SG4lMC2oR0O2tjA1PMyYzK1Q6qbuYs9biBCHiXAyZdAdKgtWkXOdWjdjT4J8puytYL2kSTu4ztJcD2gjmqIULt_poQFeLMa0uWEGxHWgQIh_JcXWaxUJSV5Qj1lWry5mS93_yivPWTDj9yMB1Z6VdvtNJbgkb-UnriX9fxLrBvOpZYKWypLSdgehQSYAjNI3ecHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیس قالیباف به بسنت:
چرخ‌ها آماده. گرم کردن قبل از پرتاب:
دیزل ATH: فروش فوری
بزرگترین طلبکار شما: موفق باشید با Yentervention++
80میلیارد دلار کاهش می‌دهد: نام نروژ را به Americaway تغییر دهید
استخدام کم: بدهی به خدمات با DO[Israel's]W، طبق گفته عروسک‌گردان‌های شما
اوه. طرح نقطه‌ای فدرال رزرو قرمز چشمک می‌زند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71196" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71195">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gT1QEQxarsc2xvt_INt18BXsCPCYE7tPjOgXcMxQsZgBZ4OMC9WuYSYc3fddrQuEG23_9_TDnEq_wMwjr_3eZm4yI-KCNjBkipYbaTX82BeRuALT1PQ0AnREtnVMzyH3BTjFbI1yaoObo-g8HIgXFR8LFTP2Ug82BznFHQfESnbfikKwoKy9OXPdJ58q4f4ZprmDkJZUvAwFj-gylnRHT08T0YeQXTjmTd5BUBRc3wl4RUr5BW0n5u84HF4KhqTG-CECnsMn8kjrfuIlESnsefCLXFouOC2seBW7HvpJOPUn5aQgntFSQ1WSe1MUdm8zJNlxzxtBpvR-mmdgXEDsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
گویا املاکی موهاشو رنگ کرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71195" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv9AXLVlzZvCC1VvV8y8ioOSyp-gG_jwt9pYHPhrEDSnxg7lfEPdGUZn4Jx05sc260WqtdNy9tAhYSbcnQszo77AbQ7x0zdI2_HlvjIsmTKjtWSt730b_buAY5EOVjBpMT61lwdv6QasvaTd3S6OTPQsF5Vb8hfTeqzILygMacK8diVOdi_2fpPvD4Hyo1ZH5aLwld-AztLiq7gxfmT22VoFCh3QdhbP0DdJEfNPOFy6SwGFSwy1TBPg5sKYnKTV3bGpYAXdbC7pVmdFIuqlqSIUCzMGASa1qOb7xhyFV8Sil0favfO9XSLrdFJd54RdmjENFQqKcnuuEFmk9e31vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=iTtxGQsHmmiDngQXnnYjLB8OI1jtccfqSEzRkba56x0qFSzilg36gEwHGz8TUEw72CK9BtZXkyE7_zhjO-gtimMqfSrpWHgvZsjbfm6W9e1KOZqpz1-bz5UcQ3WdFv1yTojjgEYocE7gBJEo6E_tzF0c1X0pTweopoWP7X1NJQjqkz53rlRHBDgdmRq_imqCsn9cSMctuZ2BoCKp88SBuS4Qzq_h9D_CH9ifytXIUhrGkp7zoK0Kh3eSnH4JX2s1_E6ymK7moIamz5axz1b_CvK8lI1uYVYlZ0r7grLf8A-lDJZ9wDesylWjtaAnwIRGoSPaEKHjHOMSJPQJeT-mKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=iTtxGQsHmmiDngQXnnYjLB8OI1jtccfqSEzRkba56x0qFSzilg36gEwHGz8TUEw72CK9BtZXkyE7_zhjO-gtimMqfSrpWHgvZsjbfm6W9e1KOZqpz1-bz5UcQ3WdFv1yTojjgEYocE7gBJEo6E_tzF0c1X0pTweopoWP7X1NJQjqkz53rlRHBDgdmRq_imqCsn9cSMctuZ2BoCKp88SBuS4Qzq_h9D_CH9ifytXIUhrGkp7zoK0Kh3eSnH4JX2s1_E6ymK7moIamz5axz1b_CvK8lI1uYVYlZ0r7grLf8A-lDJZ9wDesylWjtaAnwIRGoSPaEKHjHOMSJPQJeT-mKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
تو همه جای جهان هوش مصنوعی داره جای آدما رو میگیره ولی تو ایران برعکسه
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71193" target="_blank">📅 18:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=I8p9h-7EgSfVt7DAVpl_YVg6V4DPoW5fr-u6QCw6uX7AtjE3pn8f9QCjxFbNDLS8_vEVh8TYPYV-CIdp6gksgHMKQ2brN5lewSkaWD2C2Rn7e1TkgiIHVA_yIt7A9qWxfTtwWqqqFAXLRrIw_kUMJFzdehy7lC7z6_WKD3hBeMCGxMA3qQdcPuy3A3UM7qgEmAZCOTcFbDv4W0Ub2PyogwQejY7H0Bz4aoEdVlj6MbsBeztYFNnD-tkm-W1OScxu8HKs6Q2i4saIzXSdAeNQeubYovWKAjxzfvPwLY-prZ5xNnT2sqTzxQ-k6P5b53XAnfDBhKZAb4ArMydg-MHauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=I8p9h-7EgSfVt7DAVpl_YVg6V4DPoW5fr-u6QCw6uX7AtjE3pn8f9QCjxFbNDLS8_vEVh8TYPYV-CIdp6gksgHMKQ2brN5lewSkaWD2C2Rn7e1TkgiIHVA_yIt7A9qWxfTtwWqqqFAXLRrIw_kUMJFzdehy7lC7z6_WKD3hBeMCGxMA3qQdcPuy3A3UM7qgEmAZCOTcFbDv4W0Ub2PyogwQejY7H0Bz4aoEdVlj6MbsBeztYFNnD-tkm-W1OScxu8HKs6Q2i4saIzXSdAeNQeubYovWKAjxzfvPwLY-prZ5xNnT2sqTzxQ-k6P5b53XAnfDBhKZAb4ArMydg-MHauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای دو تا ترنس تو پارک لاله تهران!
فقط آخرش
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71192" target="_blank">📅 17:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=Oh-6VZK8uFvwk6LR9Qci2OBQZXXA-szlSjCD09E_kgSTKN8NUybaG43ec_vRQ2wDTcl6ISlkgKskGVzLlW6gzJ5iQM8mOyxxt9-6ufsZsV76gBUQ6hFnVg3KKXrcaFs5SFhn1RJ8HTDa5_VAi4mujByVZsJg-W1jBTmiJUO54FvgxtmnYw3JJeGDC6-cqgyITbDMC8pqOST1GQSV8LRPmgwwwyJ68KyYAys--EwdM8w8r04aX2ZgXsqnBL1xEAEAuNDlSr8L2IDgFS4FERJe_3_TzI_5rnhYmZQLh5IP7QWJ9OWewxEbV3Igv-1TlHS0PywPW-ulKQg0JmrPrWF4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=Oh-6VZK8uFvwk6LR9Qci2OBQZXXA-szlSjCD09E_kgSTKN8NUybaG43ec_vRQ2wDTcl6ISlkgKskGVzLlW6gzJ5iQM8mOyxxt9-6ufsZsV76gBUQ6hFnVg3KKXrcaFs5SFhn1RJ8HTDa5_VAi4mujByVZsJg-W1jBTmiJUO54FvgxtmnYw3JJeGDC6-cqgyITbDMC8pqOST1GQSV8LRPmgwwwyJ68KyYAys--EwdM8w8r04aX2ZgXsqnBL1xEAEAuNDlSr8L2IDgFS4FERJe_3_TzI_5rnhYmZQLh5IP7QWJ9OWewxEbV3Igv-1TlHS0PywPW-ulKQg0JmrPrWF4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71191" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=TEOw3YQ6MOqxwky-7g62i_dq0EOzKFhKMCV01msad7WWlHQEYSuDXDTQwI60noODYMmD2wy4IJ6XhHy3TqCaHNEQ7A3V06-8tCfjg82fbZS9wnc3mE-nVxqQB0ZSTOyT4tYGMSfXmn2ZYbvzlqshUl1PIguVVW6NgunqwHsdTDwsfuPa7_TEv6lGb6gzPOmIoadodcblzGBQh3wBT0Km3BqYXWP8cdZkGCQ3B51675xISji2fTV1EJgH3beWiCjt-StjWyaZbbqykmkSB5G4F7SKDqe9HfAqXIgIZBtfpTJWvSTnzDRdN873maucMF-WHnSO4YG_XvWzsuKuKRyrlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=TEOw3YQ6MOqxwky-7g62i_dq0EOzKFhKMCV01msad7WWlHQEYSuDXDTQwI60noODYMmD2wy4IJ6XhHy3TqCaHNEQ7A3V06-8tCfjg82fbZS9wnc3mE-nVxqQB0ZSTOyT4tYGMSfXmn2ZYbvzlqshUl1PIguVVW6NgunqwHsdTDwsfuPa7_TEv6lGb6gzPOmIoadodcblzGBQh3wBT0Km3BqYXWP8cdZkGCQ3B51675xISji2fTV1EJgH3beWiCjt-StjWyaZbbqykmkSB5G4F7SKDqe9HfAqXIgIZBtfpTJWvSTnzDRdN873maucMF-WHnSO4YG_XvWzsuKuKRyrlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
راننده ای که چند شب پیش در مشهد طرفداران حکومت رو زیر گرفت:
عمدی نبود تعادل نداشتم به یکی برخورد کردم تشنج کردم جای ترمز گاز دادم و یهویی زیر گرفتم
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71190" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71189" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9UZPepKwXRpqu8HAMRbRLEAMZIV7N-pSW611pKzSnRP5b-LkLl_m42ZpXAwpl0upHjJRRm8CiFZ4Qsg8KMf5gqn1cgN7f71v6jFy0s0TyGDqvSh2N63zkiec84d92s6OxI7zMbd2yhPk92X2yJsVev2uMQwtbqxBYcQyyTg-K5Ywsp__saxAvbbelgnhduXn3FPExNNHILQS7_kxQSfoZjL19TFoifdYhqrgsSt9edSq87BUWVlAnVrtlGVkaHKvQHzs-X2oiDA4yXaMhEze3oFzM7uXnlZufoJSvNyRiuRMoXRClPAd0yWh8vb3pheJ8ehS6NLV17sB7wQbXmnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71188" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHT1f4ID6jvC3eIPmEh6PbckvSxYBC-4AjyOfsJ8y9oJEPxEBH2fbVsCTK7CmzDir5TcI3o-Ncchb9X3Dq2EAPluYHBOVVgP01-2HjYnzr3YTXU-sIPilAh-yAazEC6ORw3BbPtc0QgqC6Y-xk3HfzHeMqEJhdBKAitlmpE1oH5Cz9K7-4RVKF8dabhHpx7vV4wglowSLDVzJM8UnCirAPBsTsjoE9rryKwxLbV0BoFCbPCj-zjeawHIi2oGfMydpHoD1gx8tK5oxzeJWjilPmHY5R4ZiWlclhrFGDjb-Qp7Dq_ASzDIibAb4t17xQ9Hxtzc32dcJXGn2lcVed32gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇵🇰
پارلمان پاکستان برای نخستین بار در تاریخ این کشور، فرماندهی قانونی هر سه شاخه نیروهای مسلح — شامل نیروی زمینی، نیروی دریایی و نیروی هوایی — را به «عاصم منیر»، فرمانده ارتش، واگذار کرده است.
او می‌تواند بدون نیاز به تصویب کابینه، کارکنان این نیروها را بازنشسته یا اخراج کند و یا در خدمت نگه دارد.
دوره پنج‌ساله مسئولیت او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت.
او با دریافت درجه «فیلد مارشال»، این درجه و مصونیت قانونی را مادام‌العمر حفظ خواهد کرد و برکناری‌اش مستلزم کسب رأی دو‌سوم نمایندگان پارلمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71187" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=ZEy9yDgBSNgLmwAeBOCcg_kjoKox9GQcyITEDeyfbfBULB4MxYnr2p8qSQuYHjqlFZttZZEBrPCaHVuHb8MKnAxaRhp6jhGu1p5pEqgzpm1EjdtHwV8hdIeyzs95H8YkefjUNGmXUAyW-rAF9MC3iulOmouvx7t1tcyIWoxT_rQQKTzvLhWQMSbbbCtZN1SE5hgIW7N5Asy9T-6FfkCD_54XtAauotpWDX39cOEaV1SKwLo-WvRgIcG0VE9SJQak-3pejtg7rAcUEqDaSU_apYfWlly0W0ItaOEUHLC1jrg56fJQmjXUKNbBuwZObGO8U8ExKcXsmCZjaZFo-nc5Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=ZEy9yDgBSNgLmwAeBOCcg_kjoKox9GQcyITEDeyfbfBULB4MxYnr2p8qSQuYHjqlFZttZZEBrPCaHVuHb8MKnAxaRhp6jhGu1p5pEqgzpm1EjdtHwV8hdIeyzs95H8YkefjUNGmXUAyW-rAF9MC3iulOmouvx7t1tcyIWoxT_rQQKTzvLhWQMSbbbCtZN1SE5hgIW7N5Asy9T-6FfkCD_54XtAauotpWDX39cOEaV1SKwLo-WvRgIcG0VE9SJQak-3pejtg7rAcUEqDaSU_apYfWlly0W0ItaOEUHLC1jrg56fJQmjXUKNbBuwZObGO8U8ExKcXsmCZjaZFo-nc5Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1sPK_mdBmlm93MBjIg8I_EZnriMg_O4bqhWItBZYbl2A2A7v2Whn-k7DUNQUA6liFFAJumuXZW5SKUYPillD5hepTjCgtfiD1kMqn6GF3FVXXD-4Lr_ZgEsu5KV4BM7EBQP7PyjVonwX7JT-DA_PoRIWXAB75y5Ra6O_J-dY8YqFZZiN58Zf5HkxFEk0qfhKdezJxRBMGG10qEEonyZndXnVcdyUybBFwQ4Bs6VSVWmtZbboviCsFF4KkbNTA7C-l07hUV04clbZqFk7FHHLvS6wFN63gNiBZwcpmxmwGVuP6lsX-rFH3qKsGcnth0H4XmAu7MaGkjr81HBStLs3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=E8s5rLq45RiE9BLqCtgDrb6kXcNqwKWLtjK6nK3Pn5bysW4nRGJuBqKvKyKxjQhaXxmqaBYje9Gch3c-OjpMcCavbwVQOKYj3a1dY5uWpV7KlLtd1V_dKAzsY0WESqlvCZuI9bPT4HHqrj4VHsBwKXOYLFLhVJYpPGFZ3YPvEsFNch170ffQI2mJ7YTYf7CfQ_thENA5MbKhgRavMGbh8GiqmNvW5I3OJ6tFSyh1sNcOsnncy0hQawqGERsGqYiUHBcRz9fb0jzcrmi7so4_XH7AdCxlkAhE-r3EcwBOiCZFefMAHf782e90dU5VfQjSb8vPzg5UD9U74EfoQAVJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=E8s5rLq45RiE9BLqCtgDrb6kXcNqwKWLtjK6nK3Pn5bysW4nRGJuBqKvKyKxjQhaXxmqaBYje9Gch3c-OjpMcCavbwVQOKYj3a1dY5uWpV7KlLtd1V_dKAzsY0WESqlvCZuI9bPT4HHqrj4VHsBwKXOYLFLhVJYpPGFZ3YPvEsFNch170ffQI2mJ7YTYf7CfQ_thENA5MbKhgRavMGbh8GiqmNvW5I3OJ6tFSyh1sNcOsnncy0hQawqGERsGqYiUHBcRz9fb0jzcrmi7so4_XH7AdCxlkAhE-r3EcwBOiCZFefMAHf782e90dU5VfQjSb8vPzg5UD9U74EfoQAVJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=rQf5bqAoAAeWuCZoX2wr1o_xANgFZ8Oc_BJ-IPFwlOZsegxWK4PeyPBh689n88yrUX2_dFHxO9a9SHioHFg-biv9lSxsv7vM5TesoElDK1T6otrWnQAXRpg723JpRSWCK9uWnw29oPZFemdZLw1cdjr155Fzx8ainiNb3TlvU0wkiqiCjKJU3ss_Kza9pm-Hs8nh14SUp8TAX-DIviiqacMKyljfwG_5CZOOYUWMldN0FjpkKnUVvhhM00Je3KJCmxvdMenjt5NJ4P0miWEXOeGBe_7Zx2B3ultsl65tr4p1M7S610n-DIT276Q_HmILzqnXm8ted2_AVE58a2zEtIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=rQf5bqAoAAeWuCZoX2wr1o_xANgFZ8Oc_BJ-IPFwlOZsegxWK4PeyPBh689n88yrUX2_dFHxO9a9SHioHFg-biv9lSxsv7vM5TesoElDK1T6otrWnQAXRpg723JpRSWCK9uWnw29oPZFemdZLw1cdjr155Fzx8ainiNb3TlvU0wkiqiCjKJU3ss_Kza9pm-Hs8nh14SUp8TAX-DIviiqacMKyljfwG_5CZOOYUWMldN0FjpkKnUVvhhM00Je3KJCmxvdMenjt5NJ4P0miWEXOeGBe_7Zx2B3ultsl65tr4p1M7S610n-DIT276Q_HmILzqnXm8ted2_AVE58a2zEtIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=OK1eNmOYxW4GfX0Z3XWwg3_VPcYUXmFoh8niAWYgDsY_NqgGnzF4616gVddhk5c5PYt37ZPkwg0KRa5lkl8D3XDJyUZ8RKSQ-1X4m0fomtvC3k-2HcZubIEBWrOobFaeDwnjGEWlHwOjFBzmg4aEYtb4FLUQJGsVxEeNxAN5dd0MsqAkwrwtGD1yzxWTWyukb2WstSX7UpXhtqySpOzjIbrU9ArlRfFyksYSuL711_EMideDzSZjtbquGtprcLOjy9wt3pkrg-4d_YwGrHBG8inuuUbRzmYbV9I8xAX_nDJpHEvdkRxnHle7yVMDOP284OdGAyPHCnZJSJ43d-cdpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=OK1eNmOYxW4GfX0Z3XWwg3_VPcYUXmFoh8niAWYgDsY_NqgGnzF4616gVddhk5c5PYt37ZPkwg0KRa5lkl8D3XDJyUZ8RKSQ-1X4m0fomtvC3k-2HcZubIEBWrOobFaeDwnjGEWlHwOjFBzmg4aEYtb4FLUQJGsVxEeNxAN5dd0MsqAkwrwtGD1yzxWTWyukb2WstSX7UpXhtqySpOzjIbrU9ArlRfFyksYSuL711_EMideDzSZjtbquGtprcLOjy9wt3pkrg-4d_YwGrHBG8inuuUbRzmYbV9I8xAX_nDJpHEvdkRxnHle7yVMDOP284OdGAyPHCnZJSJ43d-cdpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=EjrmXkoQ0hkJtldp3SK-bqju7K_8cYbZlUyVCPwfwssG_JA46C0fpl6GyTANNjdsygn6Q1wRcOhDG6Z-2lFh0hfI3KDTTQ_XE0lDkXwzt-EFlq4UyHaIJsThKXcdo_fvB3x3idhgsWMrzpQm1qz_LkUwWw4SXTlLni4DNGMEXXwoQlW93t80i7IBJHafGzWfzD3Ndi2WAJSGfWijkc9pcTFCxl-Xkoz6-UVyOs5GEh1cXNlvcJL0CXOoOyPJMQEXrPiLT6LMfRDSWUdc5s-_aFzZal0Yb1vR1hwivZIv6wObjhO18GBnEFc5w6ClQWN9wMNWkFkVzgUJ8xwT_wAopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=EjrmXkoQ0hkJtldp3SK-bqju7K_8cYbZlUyVCPwfwssG_JA46C0fpl6GyTANNjdsygn6Q1wRcOhDG6Z-2lFh0hfI3KDTTQ_XE0lDkXwzt-EFlq4UyHaIJsThKXcdo_fvB3x3idhgsWMrzpQm1qz_LkUwWw4SXTlLni4DNGMEXXwoQlW93t80i7IBJHafGzWfzD3Ndi2WAJSGfWijkc9pcTFCxl-Xkoz6-UVyOs5GEh1cXNlvcJL0CXOoOyPJMQEXrPiLT6LMfRDSWUdc5s-_aFzZal0Yb1vR1hwivZIv6wObjhO18GBnEFc5w6ClQWN9wMNWkFkVzgUJ8xwT_wAopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrfF3XzNlfxBNOJfciONPPTDZrsPsM8kzUl5dxEw_7I8m9Ex_9K-cWeymAA81k98GJ_GykHlv4BxiP8-dluKwjKxMNrEPN7T1VrkWIP-5UZ7-t9fATE3CA1MutjSVDK7jxRtWUG7oPcwmfOj7lp-35RZb_9gEE2wYhKcZEXOk4sZa1lfvKdt1t7l1Gr9NGQmypZXUsCP2qYHKcbIHIvDyIB_PIckZVlzbhVjBal3XDZSgvm8EbKjbo2y05G432QQqmHAHverkC48QqS4oHZXzPlt5Es5BGonYIdMTfVqmAaeQ0pYjXk7W_FkasgmIzuLLToLcjiJVXDund8dVKhOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71177">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=Z7FqyC8wkwwLL3UlwWOpNRn3sKFknVhzcKe1T4ikzHViBWxtjm0jgJ1CJ8QAlH74p3ZTHgLFZB0wkZtiV1lZf49HwPRXvPdb0zEuiYgAcwNTGsJMq6oGP1K6n7uyjUVMZmz5BdYxWY0NUxzAg9-UeZbWWDzYlTY7ldNbj7tsS0wfA4i0Vhejviq663X9qBCP5bDOTWZom79zl3fDh_mt-tD5oUSaO2c5rUb_1vRYSRuB45pxnjnYc3FvSICrO5RlmZC-MDQnbQ8WG3BJFc7dP3iPGU0_JevB3zobhdXTehS2WVjIsfHvibbDOMlqKWLYoyo6z1a_U6kf0UawCKxfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=Z7FqyC8wkwwLL3UlwWOpNRn3sKFknVhzcKe1T4ikzHViBWxtjm0jgJ1CJ8QAlH74p3ZTHgLFZB0wkZtiV1lZf49HwPRXvPdb0zEuiYgAcwNTGsJMq6oGP1K6n7uyjUVMZmz5BdYxWY0NUxzAg9-UeZbWWDzYlTY7ldNbj7tsS0wfA4i0Vhejviq663X9qBCP5bDOTWZom79zl3fDh_mt-tD5oUSaO2c5rUb_1vRYSRuB45pxnjnYc3FvSICrO5RlmZC-MDQnbQ8WG3BJFc7dP3iPGU0_JevB3zobhdXTehS2WVjIsfHvibbDOMlqKWLYoyo6z1a_U6kf0UawCKxfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام ویدئو غرق شدن نفتکش ایرانی در دریای عمان را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71177" target="_blank">📅 13:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71176">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
آمریکایی‌ها باید دریافته باشند که دوران «پاسخ‌های متناسب» به سر آمده است.
حملات ما به پایگاه‌های متجاوزان تنها یک آغاز بود.
قواعد بازی تغییر کرده است.
از این پس، هرگونه تجاوز به منافع ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر در پی خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71176" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71175">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=kPJVdrOenaJX3yqRbUGp504V8RdG4xe-sjaoJTvLYe_PUvvcqoczlqhthXzUH44BMIaXo4kvLP1P2WgkhYse1o_n2Hb6nXyT_sjOAjpla6HnO6jlCuLSua573nS4kW2GjbdXj2KuovoFua9vshqDwI4X0p07mVXtMnrbwgKb9SPSBg4t1WR_PaUpN2WMYaRHqUUEhW782ADmrRtVsS01_qjQBMWc_9Mp8Vq3yq4chkLPUCd43JNcGeNDY8rzhdAfEX_YTcKSKPHTJRC79Di_qpqA58adVd8Mk1WquWbf1_OO56OeMBf7uCGhbjCgNRhJix_MWCMf03xXpczdK6ESUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=kPJVdrOenaJX3yqRbUGp504V8RdG4xe-sjaoJTvLYe_PUvvcqoczlqhthXzUH44BMIaXo4kvLP1P2WgkhYse1o_n2Hb6nXyT_sjOAjpla6HnO6jlCuLSua573nS4kW2GjbdXj2KuovoFua9vshqDwI4X0p07mVXtMnrbwgKb9SPSBg4t1WR_PaUpN2WMYaRHqUUEhW782ADmrRtVsS01_qjQBMWc_9Mp8Vq3yq4chkLPUCd43JNcGeNDY8rzhdAfEX_YTcKSKPHTJRC79Di_qpqA58adVd8Mk1WquWbf1_OO56OeMBf7uCGhbjCgNRhJix_MWCMf03xXpczdK6ESUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:بستن تنگه هرمز به ضرر ایران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71175" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71174">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=lhQEUB3HolcmXe1fadG2tzdnjnIsyS4Z_n9bKZTzevwTlivK5iYWo2ymZ4x4zJVaVdpYenKTIDRujQ3CkD840juZhdXUq6p-8UmE9TtDys_JRyXaUm1cOY7LJBEB8C-BMtYMWUmoycjBMLAJOeeuznqPd424SD3W71O1s5EtgeYy1I5P6UGdkMlQT3w9lPiAJRIg3v1S97xrSa19eZwoESru6Ek18BQKTOPdzxHYeeDwTHcdlEPZh8MHFtg4uZDgnHqI6_lPG1VRp16vDbpPDITzkhQQVx3qO5b4w35QI9g9UDeUr7BHu31GWlgdnV1mrDWl_eMp3Yo4WSUcYxmvhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=lhQEUB3HolcmXe1fadG2tzdnjnIsyS4Z_n9bKZTzevwTlivK5iYWo2ymZ4x4zJVaVdpYenKTIDRujQ3CkD840juZhdXUq6p-8UmE9TtDys_JRyXaUm1cOY7LJBEB8C-BMtYMWUmoycjBMLAJOeeuznqPd424SD3W71O1s5EtgeYy1I5P6UGdkMlQT3w9lPiAJRIg3v1S97xrSa19eZwoESru6Ek18BQKTOPdzxHYeeDwTHcdlEPZh8MHFtg4uZDgnHqI6_lPG1VRp16vDbpPDITzkhQQVx3qO5b4w35QI9g9UDeUr7BHu31GWlgdnV1mrDWl_eMp3Yo4WSUcYxmvhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
ویدیویی که در توییتر فارسی به شدت در حال وایرال شدنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71174" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71173">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=RNCU7dXRq7KPpmy83tfyIVClEqoOwKm9ZpUa3IZGIpPUBI7nA2f708EOX54Rsiq667uiKLEIhboYpST94TrFVn9QLIVkqXjLznc9qQvVRAGOAJaN9AgRr6UC2jFiQsLRxTJvU7Q-bbEt49M9ohA4e_6HI7ZiszH7q0z2zzNAa1wmsrx1XZFLhymM54lP555C7ZgEWWIDwZwVpPZVSHkogpbrSepXDm5WuLuN8Ey-ghNXFZ625myef9zUYXnKnR6OoQvDogVZkd23pEPYRFAlAZGq27GQZYIp9m6rwR7Gddex1nuaxA4pAsJoDzSElirmcL5QEn0IGdRVmHP4mMJTjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=RNCU7dXRq7KPpmy83tfyIVClEqoOwKm9ZpUa3IZGIpPUBI7nA2f708EOX54Rsiq667uiKLEIhboYpST94TrFVn9QLIVkqXjLznc9qQvVRAGOAJaN9AgRr6UC2jFiQsLRxTJvU7Q-bbEt49M9ohA4e_6HI7ZiszH7q0z2zzNAa1wmsrx1XZFLhymM54lP555C7ZgEWWIDwZwVpPZVSHkogpbrSepXDm5WuLuN8Ey-ghNXFZ625myef9zUYXnKnR6OoQvDogVZkd23pEPYRFAlAZGq27GQZYIp9m6rwR7Gddex1nuaxA4pAsJoDzSElirmcL5QEn0IGdRVmHP4mMJTjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به گفته آقای دکتر اگه می‌خوای سرطان پروستات نگیری، باید ماهی ۲۱ بار سکس کنی...!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71173" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71172">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b321711db4.mp4?token=W0AFhffkIgJx5WCY4-3sxFkw2B2WC4WPQ2pgdWcEL_2vp_ld3dEnjjtt5bghJbGnK96wDe2SW_Xxotfhjpoqx3kgcyHY1CCGQBot6ldxkhjdYz1Be9a5F_Lbuep3q3vprBGrExEEokH1H130vUAIgxLB_hFL-yTpWdlOTKQoDZ4FlDzKLJ7NX-X8wXGHGfE0VzY6a2yd7jAryXb6tfMtGYppuIxvPY048ToIoc4NEqCd4RE6RZgdS0X8Q_9NV504p4Dns-VmRR980x7G8gtzUwNHSoTYTHIxLByTA-trYTIqEx3zmxVyhpWICMKDZsIWI7kEJTB9YL1T4PrdVvq3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b321711db4.mp4?token=W0AFhffkIgJx5WCY4-3sxFkw2B2WC4WPQ2pgdWcEL_2vp_ld3dEnjjtt5bghJbGnK96wDe2SW_Xxotfhjpoqx3kgcyHY1CCGQBot6ldxkhjdYz1Be9a5F_Lbuep3q3vprBGrExEEokH1H130vUAIgxLB_hFL-yTpWdlOTKQoDZ4FlDzKLJ7NX-X8wXGHGfE0VzY6a2yd7jAryXb6tfMtGYppuIxvPY048ToIoc4NEqCd4RE6RZgdS0X8Q_9NV504p4Dns-VmRR980x7G8gtzUwNHSoTYTHIxLByTA-trYTIqEx3zmxVyhpWICMKDZsIWI7kEJTB9YL1T4PrdVvq3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇹🇷
این پسر بچه ارومیه ای که چند وقت پیش با ویدیوش که در حال آهنگ خوندن بود توی اینستاگرام به شدت وایرال شد حالا یه کمپانی بزرگ از ترکیه اومده و باهاش قرارداد همکاری بسته؛
فعلا این قرارداد واسه اجرای کنسرت های مختلف تو ترکیه‌ست
رئیس کمپانی میگه که این تازه اول راهه و قراره بزودی تو سراسر جهان کنسرت برگزار کنیم...
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71172" target="_blank">📅 10:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71171">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e529d142.mp4?token=eOb6GZ8qAsR5KGIO6_49p68b2BcCs3wrWhpyFqpBhhrbJav9DYXdMcUfSmyV3nR_074MfNQjXhlWgLMQ09uibCy7bIK_jeloGT_xg4nTKXPOVsUW_tXBqM_XxzE5lGucOD-43hyLZkTeseR7wAg_oHkPKhGLv2XYlB9S8vagNQ7oH6Zlqh4kNeNY5wQwXSk_BF9mh4aXn9Vf_MtxvOaUIR_XGy8I5_Tt1B6fqDMYSYXhBP28kAzA_R3IJAXAK9uxxUwOt82eUSD2YwueqoaahQ4oqjhPoOqbOuplGqQlmHNvco_XfjPQiUqssp77V3a4fkD6CiexE5Ppp1sy7QzOgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e529d142.mp4?token=eOb6GZ8qAsR5KGIO6_49p68b2BcCs3wrWhpyFqpBhhrbJav9DYXdMcUfSmyV3nR_074MfNQjXhlWgLMQ09uibCy7bIK_jeloGT_xg4nTKXPOVsUW_tXBqM_XxzE5lGucOD-43hyLZkTeseR7wAg_oHkPKhGLv2XYlB9S8vagNQ7oH6Zlqh4kNeNY5wQwXSk_BF9mh4aXn9Vf_MtxvOaUIR_XGy8I5_Tt1B6fqDMYSYXhBP28kAzA_R3IJAXAK9uxxUwOt82eUSD2YwueqoaahQ4oqjhPoOqbOuplGqQlmHNvco_XfjPQiUqssp77V3a4fkD6CiexE5Ppp1sy7QzOgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
خبرنگار جمهوری اسلامی در لبنان:
اعضای سپاه پاسداران در تپه‌های علی‌الطاهر، به دلیل محاصره اسرائیل، در شرایط عاشورایی قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71171" target="_blank">📅 10:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71170">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a662811c73.mp4?token=VYu0pQDJDtLR6CNBwTHWzvEGx_ErVEBi4VfVH23m6Qmx34gjZ7lHA8-4tCMg9rY1Ipn5UVxk6fBCyH3rD5h-uVqGat4n8U_kxHvJjFUBTJDCSg0DtguXDS2zRUYvWXHAIRzXsYx8SPTfQycR3MliH6q97qX0gx5RT6c1x9b3zkVdEKRZtJwCpXX2hCPPsDIIc-5YGidWn1mA-7kIph1WBnXGwVyhke-VfoUJY5pnD89Q7yIjYCcQfq11jd9WGnk4nEP76G5C-KeYNMg4aCAGIOm-G_TgfSPxgZ9HcqQQv8kZGM6dG2sb_Gix4BJLJDYQZAsmDVOE8bPulzsxkQouPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a662811c73.mp4?token=VYu0pQDJDtLR6CNBwTHWzvEGx_ErVEBi4VfVH23m6Qmx34gjZ7lHA8-4tCMg9rY1Ipn5UVxk6fBCyH3rD5h-uVqGat4n8U_kxHvJjFUBTJDCSg0DtguXDS2zRUYvWXHAIRzXsYx8SPTfQycR3MliH6q97qX0gx5RT6c1x9b3zkVdEKRZtJwCpXX2hCPPsDIIc-5YGidWn1mA-7kIph1WBnXGwVyhke-VfoUJY5pnD89Q7yIjYCcQfq11jd9WGnk4nEP76G5C-KeYNMg4aCAGIOm-G_TgfSPxgZ9HcqQQv8kZGM6dG2sb_Gix4BJLJDYQZAsmDVOE8bPulzsxkQouPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شاهین نجفی:
هرکسی رضا پهلوی رو مورد انتقادهای عجیب غریب قرار میده و میزنتش یه سرش وصل میشه به جمهوری اسلامی
اینا جوگیر شدن چهارتا شعار دادن و حرف زدن بعد دیدن اینجا خبری از سهم دهی به کسی نیست مسیرشون رو عوض کردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71170" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71169">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=s4HhLWMCGotr4CQbk2QeegfsHYM6bpWIbKEw2uA6v5eZM7v0OC9qdJShvKAnrh5LO09AfJofkob3-MfNM0MUf92L0nulIdHdtPEbssgIrp2WkglntQL2eMoKlIxus-txQvIKDdjkICalgOX5WV6l9B3uVOIYNfGwdZ2JLU1bjU5xXmfUI1-kWb5P9JfkHOGkcv3dFi3gW0WkNuomCoWa1sqPH1Vd2puBjY064JvuegTQCFahVigB01kAQh1iGuDHDgytNlw4efGEG71neUzyrFYsf9Mfkm_yEyPxIhuV4mXIs6PWh5Yt5CZHYMmaNogeOXR5SUUwKqMhUZgmR4Gf6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=s4HhLWMCGotr4CQbk2QeegfsHYM6bpWIbKEw2uA6v5eZM7v0OC9qdJShvKAnrh5LO09AfJofkob3-MfNM0MUf92L0nulIdHdtPEbssgIrp2WkglntQL2eMoKlIxus-txQvIKDdjkICalgOX5WV6l9B3uVOIYNfGwdZ2JLU1bjU5xXmfUI1-kWb5P9JfkHOGkcv3dFi3gW0WkNuomCoWa1sqPH1Vd2puBjY064JvuegTQCFahVigB01kAQh1iGuDHDgytNlw4efGEG71neUzyrFYsf9Mfkm_yEyPxIhuV4mXIs6PWh5Yt5CZHYMmaNogeOXR5SUUwKqMhUZgmR4Gf6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما آمار رسمی کشته شدگان اسرائیل تو سه روز اول جنگ رو منتشر کرد:
۶عدد ژنرال ارشد اسرائیلی
۳۲ نفر مامور موساد و ۷۸ نفر مامور شین بت
یازده دانشمند هسته‌ای
۱۹۸ نفر افسر نیروی هوایی
۴۶۲ سرباز و ۴۲۳ نیروی ذخیره ارتش اسرائیل کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71169" target="_blank">📅 09:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71168">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
سپاه پاسداران انقلاب اسلامی ساعاتی قبل در بیانیه ای مدعی حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی شد و اعلام کرد که پس از این حمله اونا خسارت دیدن، ترسیدن و از منطقه فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71168" target="_blank">📅 08:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71167">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71167" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71167" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71166">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smh2xdUNWArZCkUloQuiHjDdEbvV7pTy7rM2q6bwrRrjnFRLmyrJgI7IIejOvx2lruMhZEpYw5a3n5ixzS8MKMUAE3i8OjXWi48GbocEM5pyrTFzwK0cHEM-0LPySoN-lFBF0YFSayNoqoPohPt3ZVD8P7FtvTc60CK9b13er5Pe_wgJJ3JFhwAmxXllBsZ0vYsza8DQV8UTH553dLk2JAovNhRDG28s_kOniV3G0L2BX6diIi18WYGHDAQVh6Ap32Xc8zO2e8B4CMj5j3KDo36t4dWh_f8cx09efJmSYgaHPyfHAh_HvKllXquJW_0yRRw51vDUxto_51DXXvnicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71166" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71165">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/news_hut/71165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71165" target="_blank">📅 01:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71163">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=UC9UnoB2jaBWzwIe-qbdoZSIcK3LlXKR37rPxceBPYaJ_ecOz1HgdiGkKqMcQ-CByyZyTQ54CDjx-BdZKZNd4aqNdHD4rmOhFKQMQbWVXuddg0vVF63L24DYS1U0Zm3TtMfI4WPH86y9i8LDFg3QtuWKY4fxJTRmXmsrKaRnUGky5KekV3_CNhFkX_PvmeIyE1PbsXQm76bCBu1V1rdGieM8jLLGtYpwmOkDbpDgP9IXUykU8LgnsgEfs0nZ2VUnF5qqMX1ai5dFPveiMhEON9zE4RJLKZLx35NvLpfSXnMYZIWOZv9XeRGgs7LR7j7G1y9FHe9LALmbXwDdrDrgpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c0f365bbb.mp4?token=UC9UnoB2jaBWzwIe-qbdoZSIcK3LlXKR37rPxceBPYaJ_ecOz1HgdiGkKqMcQ-CByyZyTQ54CDjx-BdZKZNd4aqNdHD4rmOhFKQMQbWVXuddg0vVF63L24DYS1U0Zm3TtMfI4WPH86y9i8LDFg3QtuWKY4fxJTRmXmsrKaRnUGky5KekV3_CNhFkX_PvmeIyE1PbsXQm76bCBu1V1rdGieM8jLLGtYpwmOkDbpDgP9IXUykU8LgnsgEfs0nZ2VUnF5qqMX1ai5dFPveiMhEON9zE4RJLKZLx35NvLpfSXnMYZIWOZv9XeRGgs7LR7j7G1y9FHe9LALmbXwDdrDrgpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سپاه پاسداران تصاویری از «رصد و رهگیری شناورهای متخلف» در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71163" target="_blank">📅 00:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71162">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=qYIv5_zq-7UQ6EZ7gUlmIhbNnTg_QbAPX3guWG2j4KSqnK2DMScCobho4yNLAHjxE7evm6I_GJgVZjgCRNlqiYpUhs-bMafLfpUAd4K4QG0fUXq-ESEc1-0jK18hH86yAR_aK1LGuTEB8hbm6yRnZWCGRDCTxCA9dE3Vd8HQx3q0d4svwJhng0RtbTBZ1A-9kaaIdenqv2oUZrSA6rTezAS890bGON7CCPGnE9ra2BV1WIf25q7rP1wAu8l_mu-koyvl_9HZ-kkolJwEk1jOrv5UWbjHU77uZhGrmGSEsF8GIccC8NjdsSN_SV3fbr3wUDUowieFWvpKoCc37LxmTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9440ae83.mp4?token=qYIv5_zq-7UQ6EZ7gUlmIhbNnTg_QbAPX3guWG2j4KSqnK2DMScCobho4yNLAHjxE7evm6I_GJgVZjgCRNlqiYpUhs-bMafLfpUAd4K4QG0fUXq-ESEc1-0jK18hH86yAR_aK1LGuTEB8hbm6yRnZWCGRDCTxCA9dE3Vd8HQx3q0d4svwJhng0RtbTBZ1A-9kaaIdenqv2oUZrSA6rTezAS890bGON7CCPGnE9ra2BV1WIf25q7rP1wAu8l_mu-koyvl_9HZ-kkolJwEk1jOrv5UWbjHU77uZhGrmGSEsF8GIccC8NjdsSN_SV3fbr3wUDUowieFWvpKoCc37LxmTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
یک فروند جنگنده F-4 فانتوم نیروی هوایی یونان در جریان رویداد «هفته پرواز آتن» در پایگاه هوایی تاناگرا سقوط کرد و دو خلبان این جنگنده کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/71162" target="_blank">📅 00:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71161">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=BBnPO4dhCLgmMCEqWZljffioRuUOYYC2p2geLPTl4H7Jq1vuiAGhbQi2yiosdac_LYvB7zKnjgPRmGXKml75_pizGwo8ADh6_FYH5ls5yPIhvaodpfiPdPEqv1j9gfxmG1WyYq3clxzmHYl5Gs6DSDqKSVsh7g418jqQr5Cp9Afp1IRX7A_5LWaqrdQ_lhbl0IrRcOIgyuz47ObuRf4McIOUecI7cLfQK3NL4DdPPFAMsx0ztMbtzEkvc096Rm2-rnJA5iyxFwPWjA5g3MVj2mJCNl1Ur1FtxX13gyuD6FHWdrgyhQ5qGGuWSfVP7ptCTRZflgz6e9iYxl2lHy7pBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=BBnPO4dhCLgmMCEqWZljffioRuUOYYC2p2geLPTl4H7Jq1vuiAGhbQi2yiosdac_LYvB7zKnjgPRmGXKml75_pizGwo8ADh6_FYH5ls5yPIhvaodpfiPdPEqv1j9gfxmG1WyYq3clxzmHYl5Gs6DSDqKSVsh7g418jqQr5Cp9Afp1IRX7A_5LWaqrdQ_lhbl0IrRcOIgyuz47ObuRf4McIOUecI7cLfQK3NL4DdPPFAMsx0ztMbtzEkvc096Rm2-rnJA5iyxFwPWjA5g3MVj2mJCNl1Ur1FtxX13gyuD6FHWdrgyhQ5qGGuWSfVP7ptCTRZflgz6e9iYxl2lHy7pBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه خانم درباره اقتصاد:
چرا مردم هر چی گرون میشه از زاویه ی آدمای متوسط بهش نگاه می‌کنن؟
خونه از ۵ میلیارد شده ۵۰ میلیارد.
گوشت از ۵۰۰ تومن شده ۴ میلیون.
سود شما چند برابر شده.
مردم از گرونیا دارن سود میکنن، مردم باید دیدگاهشون از آدمای متوسط جامعه تغییر بدن و بگن هر چی گرون میشه خب ما هم سودمونو داریم میبریم
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71161" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71160">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=dKHCGQ4wNoGjxHN8y3yWoldxORbu2rx63tzpfvA8nZmcYxFzKSw3eNBdlYn7DfhMyoeWdMkznk60o3vOcmOKFqlJ1C12Vke0T-cotlptbFwbUGklk98Faf9MbGRIB9neO7R-dHKx6emL_vxnnTQaJJgAZLfwm0Ry3JRa16DvVP37MXrPXHFgMXQxwS0ERErHJonLdJTa_4TNTrtuz1BLroXJooXF2Mh18DOLlc7z3hxTHld9cev99VF0VsgOWrJKuB30fUj9HtLXk6HZYi0_jKFpOOqM2PMIH4LcSnvf4Bf3DpyHnL8MXFng4E0Z9pG_8oIjQUhNQ0RWAG3W4VjTig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=dKHCGQ4wNoGjxHN8y3yWoldxORbu2rx63tzpfvA8nZmcYxFzKSw3eNBdlYn7DfhMyoeWdMkznk60o3vOcmOKFqlJ1C12Vke0T-cotlptbFwbUGklk98Faf9MbGRIB9neO7R-dHKx6emL_vxnnTQaJJgAZLfwm0Ry3JRa16DvVP37MXrPXHFgMXQxwS0ERErHJonLdJTa_4TNTrtuz1BLroXJooXF2Mh18DOLlc7z3hxTHld9cev99VF0VsgOWrJKuB30fUj9HtLXk6HZYi0_jKFpOOqM2PMIH4LcSnvf4Bf3DpyHnL8MXFng4E0Z9pG_8oIjQUhNQ0RWAG3W4VjTig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جانفدای رندوم و حرکات جالبش
😃
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71160" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71159">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=k_wH_k9SHNCPIeIHLr6s47aVFJak7w-j7ucsBlAbUtpgq2A8BasFWI3WFTrr9SXil289qcu83QguxVn1YBGKXFeIuegNUdyYWRMVaPVLS95F0ew__ps9Uq9asE_u3DMv5MNNGDnDabliYAXqFOTOug_fT-IOtV1dA7jH5qoACngQwTKrrMjY_8OrNGX6S29O42aZkc8yQBT3MsVY6kuxmRFeozC_zLkgXNoO2R8WjZ1S5MMLwifRJiEMeupYiJPvlBIoOHxdcl3oFc_GnyzlpPK76Da1WSmEFZ5t4ZWtGuBZgQqioN-rMlHgHjya0AW_jKh-R2jOXXCKAmEcpnMGAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=k_wH_k9SHNCPIeIHLr6s47aVFJak7w-j7ucsBlAbUtpgq2A8BasFWI3WFTrr9SXil289qcu83QguxVn1YBGKXFeIuegNUdyYWRMVaPVLS95F0ew__ps9Uq9asE_u3DMv5MNNGDnDabliYAXqFOTOug_fT-IOtV1dA7jH5qoACngQwTKrrMjY_8OrNGX6S29O42aZkc8yQBT3MsVY6kuxmRFeozC_zLkgXNoO2R8WjZ1S5MMLwifRJiEMeupYiJPvlBIoOHxdcl3oFc_GnyzlpPK76Da1WSmEFZ5t4ZWtGuBZgQqioN-rMlHgHjya0AW_jKh-R2jOXXCKAmEcpnMGAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7  جونشون رو از دست دادن...
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71159" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71158">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=YDd3oYSaJIhh91w3B_z1Ptw76PfxkqspdTCJGWcn9Zh58Yc9rZCNj0u2vG_EP_qcRPg-l2_-Zfc-c8YMcMDsO2P7kjMQ05mPGFTmBylJdgk7rEVt3YRcJNf_ZWXYAFs_DNOVSssA3nf74RDLjaxSo2HKNKrYxSYnapPBmsJXLl08N_ynmGJDYgVX3ZDx9YqnQms-fFDI6ivUbmEp3fX20zS5ggMRt0TExabF1SVYRKXoVlDkKkFsZ7TyJHt0MrH1KyYHkWnZ6xN5XJAt0D_iAqJq7xYju5lmmnX1O3DZ2632BYg91xe18PCe2vpiC21HU8b1apTx89DnlaVyrWlXew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=YDd3oYSaJIhh91w3B_z1Ptw76PfxkqspdTCJGWcn9Zh58Yc9rZCNj0u2vG_EP_qcRPg-l2_-Zfc-c8YMcMDsO2P7kjMQ05mPGFTmBylJdgk7rEVt3YRcJNf_ZWXYAFs_DNOVSssA3nf74RDLjaxSo2HKNKrYxSYnapPBmsJXLl08N_ynmGJDYgVX3ZDx9YqnQms-fFDI6ivUbmEp3fX20zS5ggMRt0TExabF1SVYRKXoVlDkKkFsZ7TyJHt0MrH1KyYHkWnZ6xN5XJAt0D_iAqJq7xYju5lmmnX1O3DZ2632BYg91xe18PCe2vpiC21HU8b1apTx89DnlaVyrWlXew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر نیرو:
دیگر قطعی برق برنامه‌ریزی‌شده نداریم
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71158" target="_blank">📅 21:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71157">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=TV_GN_u6Txv0E7DNBKE7qAo_R4ociKXzKeV-0N5FaEq0Twmwbw8QTOMYOCDI4fbSFSfcHwv6RXIMj9UZHBwtGYef2A1yAbhfcstbmlGw4Z2UWRXWGhon1xviE1tn2XTTs1aYlJxbj68vxptIzNtcCptVicZEYvpu9fuzT3tcwTmRIxlWM-yRX2Oc6l_hvFismZ6L5853MuWvMjdfhKoyuOH8ybmkmDjbPt54swS8ujnXNJ3KOYQ5-22LIKkF8CkAcRJwiFuzE1jeXx4FXjc1YjgvJY6nr8KpIoNJnQEl9pZbk-JTRwSzMF9YfSgXS3b58BjExM9E1Ksf_NXtzlMHzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=TV_GN_u6Txv0E7DNBKE7qAo_R4ociKXzKeV-0N5FaEq0Twmwbw8QTOMYOCDI4fbSFSfcHwv6RXIMj9UZHBwtGYef2A1yAbhfcstbmlGw4Z2UWRXWGhon1xviE1tn2XTTs1aYlJxbj68vxptIzNtcCptVicZEYvpu9fuzT3tcwTmRIxlWM-yRX2Oc6l_hvFismZ6L5853MuWvMjdfhKoyuOH8ybmkmDjbPt54swS8ujnXNJ3KOYQ5-22LIKkF8CkAcRJwiFuzE1jeXx4FXjc1YjgvJY6nr8KpIoNJnQEl9pZbk-JTRwSzMF9YfSgXS3b58BjExM9E1Ksf_NXtzlMHzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
جان بولتون دیپلمات آمریکایی درباره ایران:
من معتقدم — و دهه‌هاست که چنین نظری دارم — که تنها راه دستیابی به صلح و امنیت واقعی و پایدار در خاورمیانه، خلاص شدن از شر رژیم تهران است.
به گمانم حملات آمریکا و اسرائیل آسیب قابل‌توجهی به این رژیم وارد کرد.
بی‌شک ما اشتباهات زیادی مرتکب شدیم.
اما اگر اراده کنیم که درباره چگونگی انجام آن به‌درستی بیندیشیم، این هدف همچنان قابل‌تحقق است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71157" target="_blank">📅 21:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71156">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
صداوسیما:
صدای انفجار هایی که در جزیره قشم شنیده شده مربوط به شلیک موشک ها به سمت شناور های متخلف در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71156" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71155">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=Y1evCDrMe4WU2Vev0u_xMbs3s-hDpBl31R04gJyupxa7uVZAg3Szlra1N7yeXi637_AHSCWY97DYDej4iJXgtuLT8QfAe0RujsBVtXl1cDG-NZfGeZy3s7xjiZ3tIaMScXUqlCaXCeTApS5ZXXiOaquRbC3Ppxi5j5oIb6OP3_E-z50FY9qG9kduhDVvxWjJ_Tk6nRUQ3lAgaZggn_qxJAI3mzVgDHsSzy0dwsJH6gacXQ8IbHxAwKBLRt-1nm1WOCaWBoehZwNGg-WO3NNrCsKy6ciG8_NNaOxObDVwSVMyvumZa_diCt6PwW98wR1x2um75I9H0FdJ9y5Yl9oeUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=Y1evCDrMe4WU2Vev0u_xMbs3s-hDpBl31R04gJyupxa7uVZAg3Szlra1N7yeXi637_AHSCWY97DYDej4iJXgtuLT8QfAe0RujsBVtXl1cDG-NZfGeZy3s7xjiZ3tIaMScXUqlCaXCeTApS5ZXXiOaquRbC3Ppxi5j5oIb6OP3_E-z50FY9qG9kduhDVvxWjJ_Tk6nRUQ3lAgaZggn_qxJAI3mzVgDHsSzy0dwsJH6gacXQ8IbHxAwKBLRt-1nm1WOCaWBoehZwNGg-WO3NNrCsKy6ciG8_NNaOxObDVwSVMyvumZa_diCt6PwW98wR1x2um75I9H0FdJ9y5Yl9oeUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تصاویر منتشرشده نشان می‌دهد یک کشتی کانتینربر در اسکله بوشهر تقریبا به‌طور کامل نابود شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71155" target="_blank">📅 20:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71154">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش‌ هایی مبنی بر وقوع حوادث برای چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71154" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71153">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=WVG8lTxEBecLCThGcwxl4jJS6S2Uaf78A4pG1wx4mFg6M-f5AhL0V4-XxvpatjXZ-aIJiLRW4DcK8XfjWKfP3wj416SXo1vcS86yOVeca7Ba34-HQygE7jIymvL353BV0K_x16eV5Gj3Ivp0x5hDNMFnu5eo9b_OK0YEnaK2-yLpVWJnLEpX3whWq6D9uotoOieYl8jn9lKC0Jkpt96vOlZ0wJTUtLA0dBeuylakj1umEO5VfuCe8UQD-3vDxyUcLmQna-jfCoTEUdiM0b-lyqahIQzB0bW41NKN3Qrwn9bb-mZerwFG7dONr6-ipR4uBFOheQQAGITy4kp290duTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=WVG8lTxEBecLCThGcwxl4jJS6S2Uaf78A4pG1wx4mFg6M-f5AhL0V4-XxvpatjXZ-aIJiLRW4DcK8XfjWKfP3wj416SXo1vcS86yOVeca7Ba34-HQygE7jIymvL353BV0K_x16eV5Gj3Ivp0x5hDNMFnu5eo9b_OK0YEnaK2-yLpVWJnLEpX3whWq6D9uotoOieYl8jn9lKC0Jkpt96vOlZ0wJTUtLA0dBeuylakj1umEO5VfuCe8UQD-3vDxyUcLmQna-jfCoTEUdiM0b-lyqahIQzB0bW41NKN3Qrwn9bb-mZerwFG7dONr6-ipR4uBFOheQQAGITy4kp290duTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
✈️
ویدیویی تایید نشده از پرواز تانکر سوخت‌رسان آمریکایی به همراه دو جنگنده در آسمان جزیره کیش استان هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71153" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71152">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71152" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71151">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYD-j_3denYteufX7uEwd0fC6CzSFIEvsXerlkFp0dzaMTDtdCMx8PlTgfyD4oj3qjBYm4QU8FZ5s6PRClWUROL9EUeTU7F3PcagHYhseJsAG4IaQzpOiVn-YcttPzsRWNA312d6Le6t0aeEl4GiRNnkEHv2VNZVx7K2MKS9Y6zosaS-l_Gl03NoIR8R3O2LvRWOgjgtBXG8NtXxzdkfVuGVgILJlkIEiNi6Iu4eXAgbIr0TMZTExvjeQXUaSOnFGoqBJ-vcW9SjvPBwn2n7_Wgmc3hFjPgV4H1QJQ640KyU92NPtAD52iObuKj-uvXPP2G2LlfVpPySY73MQH8T0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71151" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71150">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=CBmc5EhAVc-rGfpRREQ3D7fI09ff0OOgkxlatSAqur8P2_5-vZAnz31zrPC-0FvaRqdaDuNDSLSeXAd-IqQOTqRGhtalvJF-58uDa2R-LoF00QQfMubbnBcKB-LjtkgVCrBz1kR64b_tdOILMuAnMed3KkRnCF7QMdWZmiFjiQW7fAxFGYq86KtVEIHyIiyE-sfJydmbJH1Qfd4whA4RorDeqjiYXFicELDVyW24JekZ5_iNx0FBbqcbMCBfljhMPtzykCUnC8ULP8Kf66UFqxdAtBu0UTPPY6tukgS3Ph1i8EkFTshw97yjLkOLKdQfmQPGEIgPgMa-UATdFHnBHEjiI3qcyxp7cE6aoyjwdSQOcSJTTfd3Cy6dvGZrWQB8QdiX1PKI7mZ7C6qnhuuJalv4Yh5VwIt_UFoblLzlK6iZcCJAPRs6Lvqo_-MO1m2F8xvDLAjDUq67uERpPd-7JAn0p1F34VWOnwgX_eNyz7z4IvzJ_wQU-Py_SHZXRKKtmczvpbnCpVJuZib9pVMhejefNT-3cBo66tTWhMABQ8p32O5AyqOwqRHd-pttZ_9M3fWlEk1d59cLqr-0qkaw3YRIzYiFqjoOWrRmT_DQfRJiJlTtXMUU7O8KaJXyerTm_wWiigP2N4KnDhU7FD1N1WiLGbVPQzsYEiEVL1txI90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=CBmc5EhAVc-rGfpRREQ3D7fI09ff0OOgkxlatSAqur8P2_5-vZAnz31zrPC-0FvaRqdaDuNDSLSeXAd-IqQOTqRGhtalvJF-58uDa2R-LoF00QQfMubbnBcKB-LjtkgVCrBz1kR64b_tdOILMuAnMed3KkRnCF7QMdWZmiFjiQW7fAxFGYq86KtVEIHyIiyE-sfJydmbJH1Qfd4whA4RorDeqjiYXFicELDVyW24JekZ5_iNx0FBbqcbMCBfljhMPtzykCUnC8ULP8Kf66UFqxdAtBu0UTPPY6tukgS3Ph1i8EkFTshw97yjLkOLKdQfmQPGEIgPgMa-UATdFHnBHEjiI3qcyxp7cE6aoyjwdSQOcSJTTfd3Cy6dvGZrWQB8QdiX1PKI7mZ7C6qnhuuJalv4Yh5VwIt_UFoblLzlK6iZcCJAPRs6Lvqo_-MO1m2F8xvDLAjDUq67uERpPd-7JAn0p1F34VWOnwgX_eNyz7z4IvzJ_wQU-Py_SHZXRKKtmczvpbnCpVJuZib9pVMhejefNT-3cBo66tTWhMABQ8p32O5AyqOwqRHd-pttZ_9M3fWlEk1d59cLqr-0qkaw3YRIzYiFqjoOWrRmT_DQfRJiJlTtXMUU7O8KaJXyerTm_wWiigP2N4KnDhU7FD1N1WiLGbVPQzsYEiEVL1txI90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
لحظه تهدید تخلیه خدمه نفتکش های جمهوری اسلامی توسط خلبان جنگنده ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71150" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71149">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛  پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند. دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71149" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71148">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5JTtG1t2JLTy7LS7Pf8tqsQiG-U0J4Bx_135Ax1QeCd732cmbAziFsVH3ybAZyUdQ-uTmrR-umtBMGxyaMNnIUiK2t31dcwCB9dSBurkUINvmCm6RCQ-oJSi3au2lEgLXi4aJgpjiEgXp4B0BJX-o5eJ2uJpX5fHb5ZJfU8j2lLP5yp_lVXJrnlYpNKkdAu-InCMUChPuB3QVzDW9S2uzXyYFH0LTF4veXKZt11e1o8Z9nOQqPRBzbG2QUkINy1YBhd7UazcH6OcqG1_qJwt6FhVUYS7dF8CnqcHpHhMMIZFBjKazlJQxjxdAObYOi5rgpVVIAiHPfS-2Nv1_HgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
🇧🇭
سفارت ایالات متحده در بحرین:
با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره اوضاع وجود دارد.
سفارت ایالات متحده به شهروندان آمریکایی یادآوری می‌کند که ایران پیش‌تر زیرساخت‌های غیرنظامی در بحرین، از جمله هتل‌های منامه، را هدف قرار داده است.
آمریکایی‌هایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم هوایی و اختلال در سفرها آگاه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71148" target="_blank">📅 18:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71147">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=sKhdOk9Y5DWnCE1UOXmIWG4DmU4p6dm7gnZsg3eebyp7RcjZou6TPPsBI2gkiQ-TWm0ItRmChWskJnRusn3DUOen9kYg_7m30hwL2bt6N0qDetNz1zhc-kO9jbbasHdGT5Gd6ewZ7i6fXQy76ZqO3G0qtr2GsESiMbSqyg31eM4cv7m4sk9_pv3kR41JK_Ria76CUiGgLXYFh82iRyQiKZicwJgAFpxgzwnaqExbEV1ti44FsX5Hqv9rp1ouy6-dgzDpGNMWTUeA7w7tgSucctAgQkNWARNGTN_Up28KEgdji-CVSYYvJZgCmtPdaogykR6FF_91cV4adGsZFGR2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=sKhdOk9Y5DWnCE1UOXmIWG4DmU4p6dm7gnZsg3eebyp7RcjZou6TPPsBI2gkiQ-TWm0ItRmChWskJnRusn3DUOen9kYg_7m30hwL2bt6N0qDetNz1zhc-kO9jbbasHdGT5Gd6ewZ7i6fXQy76ZqO3G0qtr2GsESiMbSqyg31eM4cv7m4sk9_pv3kR41JK_Ria76CUiGgLXYFh82iRyQiKZicwJgAFpxgzwnaqExbEV1ti44FsX5Hqv9rp1ouy6-dgzDpGNMWTUeA7w7tgSucctAgQkNWARNGTN_Up28KEgdji-CVSYYvJZgCmtPdaogykR6FF_91cV4adGsZFGR2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71147" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71146">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=SlonzzvFq7gXQa59Ekc_J45NhT4ZchqMTdUJ8gYmaYGow3TxKX7S-pLzAG9368jQrFXUGpAEwZlk97ab-08MyYclgw2azLmMpVLuQexn7-l0mNpvGjM9oeOh6gkDYTWahh7crjGtG5Lf5pJq_oF1J8hYOU9Q8LPjbExcmG3wI6juvLhFJw6a-OnobMaTKxBT05a02dkqptnu8KXiP5v2PRgMpyYnun187JVAY7ckcXWHf-2kDbwiuiTNhdwMXowpXekbnuafGLAevX9Z6cz1xzwbTrp2TuzIRz3YG-TAmoIWsYWISvi5e-obf8gKjbdHxGJNMeq71YCwCaQ1DPzi1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=SlonzzvFq7gXQa59Ekc_J45NhT4ZchqMTdUJ8gYmaYGow3TxKX7S-pLzAG9368jQrFXUGpAEwZlk97ab-08MyYclgw2azLmMpVLuQexn7-l0mNpvGjM9oeOh6gkDYTWahh7crjGtG5Lf5pJq_oF1J8hYOU9Q8LPjbExcmG3wI6juvLhFJw6a-OnobMaTKxBT05a02dkqptnu8KXiP5v2PRgMpyYnun187JVAY7ckcXWHf-2kDbwiuiTNhdwMXowpXekbnuafGLAevX9Z6cz1xzwbTrp2TuzIRz3YG-TAmoIWsYWISvi5e-obf8gKjbdHxGJNMeq71YCwCaQ1DPzi1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی:
به مردم بگیم قرار ما اینه که با قدرت‌های بزرگ تا بیست سال دیگه بجنگیم.
اگه مردم قبول کردن عالیه بریم ادامه بدیم.
ولی اگه مردم نپذیرفتن و راه دیگه‌ای نشون دادن حق نداریم نادیده‌شون بگیریم.
حتی پیغمبر هم با مردم خودش مشورت می‌کرد.
تو این کشور هیچکی از جانب خدا حاکم نیست‌؛ همه به لطف رای مردم اومدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71146" target="_blank">📅 17:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71145">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=cqj9hPFWrpvZ0igxLjGJj4rwnygMcewGDel7E9hPCi39vSAMcQopx6Tc4ujZ_MVFHOq-U1Aj_gagn_PWPiJzpOpuqw8H8Rk-REYj3LfxZKF9p0963sXdqVb05o5ki_fRY7Cc5UJmLOJppG0nQP-T0qAviYXMCV0hGKqlE7KZ4c2NjVBX3a74h-8x6XEmL85D4SuS7ULRc5bwIOs45zFPaXmRIfSqygzlvGhsGwwa4Cq5yej0mtQvfYkQAcDL_Wzj2kdVHhFKW2o_BsS_qvzsgdJ4LBPRa7PamGhHgk-PVSGmQszSwdICGsOqq2mcE-U2tfq-r-p1CL8OsdZ0E5uhsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=cqj9hPFWrpvZ0igxLjGJj4rwnygMcewGDel7E9hPCi39vSAMcQopx6Tc4ujZ_MVFHOq-U1Aj_gagn_PWPiJzpOpuqw8H8Rk-REYj3LfxZKF9p0963sXdqVb05o5ki_fRY7Cc5UJmLOJppG0nQP-T0qAviYXMCV0hGKqlE7KZ4c2NjVBX3a74h-8x6XEmL85D4SuS7ULRc5bwIOs45zFPaXmRIfSqygzlvGhsGwwa4Cq5yej0mtQvfYkQAcDL_Wzj2kdVHhFKW2o_BsS_qvzsgdJ4LBPRa7PamGhHgk-PVSGmQszSwdICGsOqq2mcE-U2tfq-r-p1CL8OsdZ0E5uhsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71145" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71144">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=KbsoACNMiVt0og5ckghKbCpNkYvjvni0hsRwwLjz-j-UrJb1iu6CbfWKkpL8eXZIOdZdeHjLilNv9qZTEUHsQ0MYqER1pfLy_5JhsnPnG4_XqTkSULeDUdyElhtlM_PlVJIDjizsfnyUeL38fKbfRYwr7ItwIh-k3mi4bdI9njtCeUw-4dcLZLldxVGENiL_9l9EbM283vTW_qF--wBjNB7j5WcBmVpu5e5jyvaX5DQb4Ytrc6XwhYnlF6bSpBJun0g5Ylew4FRZbv9eIQ2XSIiypnAamBMQscV0ezl9NDYvMuBPBZZ-39g6nGTjk9cf2-gmq1PG8zoU8WXbjR9RpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=KbsoACNMiVt0og5ckghKbCpNkYvjvni0hsRwwLjz-j-UrJb1iu6CbfWKkpL8eXZIOdZdeHjLilNv9qZTEUHsQ0MYqER1pfLy_5JhsnPnG4_XqTkSULeDUdyElhtlM_PlVJIDjizsfnyUeL38fKbfRYwr7ItwIh-k3mi4bdI9njtCeUw-4dcLZLldxVGENiL_9l9EbM283vTW_qF--wBjNB7j5WcBmVpu5e5jyvaX5DQb4Ytrc6XwhYnlF6bSpBJun0g5Ylew4FRZbv9eIQ2XSIiypnAamBMQscV0ezl9NDYvMuBPBZZ-39g6nGTjk9cf2-gmq1PG8zoU8WXbjR9RpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری ایرانیا هم انگار توی یه ایران دیگن و رفتن توی جنگلای شمال پستونک پارتی گرفتن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71144" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71143">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=gOegBY6RkrPmgnQcbbaecGI0oFDHbeJgAtfrc2EE-E-qbsXi-F8-Xl5WBo9u_a2hb6Wk_jU1dq8MnEx9sL_TZDpnGg1InIWcRwzaYW369_2kR4Bfz3D-z2oftjM8qNvRVBfohgER2K1kNKL2TkD_ludV4auCilF22SPAkP_HJd2SKpMyt6vMcdli8kXM8yM_iwclxH95V0FFykZ4knIsqn_t75D6_Lle4Mtam3b-3Do2fpDkZdGoFD7Io1D4y2iQFe1IBaes3SMxqSLQDglkz5Sb6PdVaAxz9YB447QiTwoR9fqSLpx9hXsksh4ykXFaAIb-LTm598hic2cFTRyROg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=gOegBY6RkrPmgnQcbbaecGI0oFDHbeJgAtfrc2EE-E-qbsXi-F8-Xl5WBo9u_a2hb6Wk_jU1dq8MnEx9sL_TZDpnGg1InIWcRwzaYW369_2kR4Bfz3D-z2oftjM8qNvRVBfohgER2K1kNKL2TkD_ludV4auCilF22SPAkP_HJd2SKpMyt6vMcdli8kXM8yM_iwclxH95V0FFykZ4knIsqn_t75D6_Lle4Mtam3b-3Do2fpDkZdGoFD7Io1D4y2iQFe1IBaes3SMxqSLQDglkz5Sb6PdVaAxz9YB447QiTwoR9fqSLpx9hXsksh4ykXFaAIb-LTm598hic2cFTRyROg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تو چین یه نفر بعد ورود به مغازه‌ش که به علت نشتی پر از گاز بوده، کلید برق رو میزنه و کل مغازه میترکه ولی خوشبختانه زنده میمونه و بعد از اینکه به بیرون پرت میشه کون لختی فرار میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71143" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71142">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=dF5U6oqNlFiO71uVGYRTkrpJANn6SNsYNh9zyXpg8stuSS-Pug4IsQGXuTyiM-SScZk62cx_T3j5CAB97EdtoTEVUZ6dpdoYOVIDbV4OprXo9PbIzYIPuZ-TJrWR4w-mpPT1aoNFby5xB4OgQDIGw_RYpLXKnbmMChRsyX5Bk96b5ZOYS5_sT39iPXVjcahaVh0PydFpfeDq6D1q9LUPbsiNtcgZ5qfW_93_W6nxJfYD4_7o107iFzFSf5q1YPZH1HeqEs3y66QZVaHaJYj-OnQG5vfeN97k15tYlFbBz1dUjNmYjYAqPD1__6ki7uVufV5bAz6s_AccP-vQHH6pZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=dF5U6oqNlFiO71uVGYRTkrpJANn6SNsYNh9zyXpg8stuSS-Pug4IsQGXuTyiM-SScZk62cx_T3j5CAB97EdtoTEVUZ6dpdoYOVIDbV4OprXo9PbIzYIPuZ-TJrWR4w-mpPT1aoNFby5xB4OgQDIGw_RYpLXKnbmMChRsyX5Bk96b5ZOYS5_sT39iPXVjcahaVh0PydFpfeDq6D1q9LUPbsiNtcgZ5qfW_93_W6nxJfYD4_7o107iFzFSf5q1YPZH1HeqEs3y66QZVaHaJYj-OnQG5vfeN97k15tYlFbBz1dUjNmYjYAqPD1__6ki7uVufV5bAz6s_AccP-vQHH6pZzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇺🇦
🇷🇺
یک مزدور برزیلی که در درگیری‌های روسیه و اوکراین می‌جنگید، لحظه حیرت‌انگیز عبور یک تانک از روی خود را — در حالی که میان علف‌ها پنهان شده بود — ضبط و در حساب اینستاگرامش منتشر کرد
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71142" target="_blank">📅 15:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71141">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=nUhIXYphMs4VSOSJ21nA_hNCI0qOmRJAVUOUpRHPAY_WY0fziz8ObLyJ1-OWMOtMmiZRUR3mClOsDW8i-T_X1izYCLScCIQGvV4DlQpCmGVEn26YY_jCZJwv2WqT_IpO3DyUzhDGxXAvh7CUQkfCu8U73H52CEFZJcbLbz1UeHU-eZvTgtarxdRqcGrvYwjlD9Xg0zNKHLdLr8wtVwyXo0vjFnUVZg6DRKwVhIVzk49lG3ThXoMytPoYGiqjS-DmoNia23ZpTk2d-ebCjgCtPx-c8dZ-Iob-NJaxCZjPhSDtOe-vI8KImtRN2qtEtXiBSMcI3DsLK6KP0Ibq8IfSyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=nUhIXYphMs4VSOSJ21nA_hNCI0qOmRJAVUOUpRHPAY_WY0fziz8ObLyJ1-OWMOtMmiZRUR3mClOsDW8i-T_X1izYCLScCIQGvV4DlQpCmGVEn26YY_jCZJwv2WqT_IpO3DyUzhDGxXAvh7CUQkfCu8U73H52CEFZJcbLbz1UeHU-eZvTgtarxdRqcGrvYwjlD9Xg0zNKHLdLr8wtVwyXo0vjFnUVZg6DRKwVhIVzk49lG3ThXoMytPoYGiqjS-DmoNia23ZpTk2d-ebCjgCtPx-c8dZ-Iob-NJaxCZjPhSDtOe-vI8KImtRN2qtEtXiBSMcI3DsLK6KP0Ibq8IfSyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه آخوند درباره شعار«تا آخوند کفن نشود این وطن وطن نشود»
؛
همونطور که رهبرمون رو شهید کردن یه آخوند دیگه جاشو گرفت
به ترامپ و نتانیاهو و منافقین داخلی میگم این حرفمو
تا آخوند شماهارو کفن نکنه ول نخواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71141" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71140">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⛔️
این قبیله ای که میبینید اسمشون موکو موکو هست
؛
این قبلیه در افریقا که مثل سرخپوست ها هستن برای اینکه زنان قبیله خودشون دعوت کنن به سبک رقص های به خصوص خودشون انجام میدن
هر زنی در قبیله شون مجذوب رقص مردی بشه میره بهش میده و اصلا اینطوری نیست که کسی حتما باید زن شخص خاصی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71140" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71137">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=S1Q3yTnLGuk0JSgjrvQZ-sYoIoZ-h4fk9eoWQUzmAYN_zDctTQbMMdS5oEpTKuhCt7suEQS_u0p_Q06kJflKg1gsRG6S3V7zA0KKpcgDhuIp-GTK2XW4z0Xhu3I4afzjD-uyGiv9YLSclNBuLnS2E_9reJ4qdSpVtrUQh8_aqSiVQva5Xc67A1Arfd0qBY9SQv4r5q504biSDdKgHE97sGpbKjrDm0IoFhoqMHrF8Ae8UYHaFgl2ogGrF3uwfsqA7MKwHsu9TQlq9k2h4tWOCPEOO887zawBCWI8HW9BnROlB4H8yjhlqFx5vwbJuvY3mrIqs5vdNCbxhYBTJ4A90g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=S1Q3yTnLGuk0JSgjrvQZ-sYoIoZ-h4fk9eoWQUzmAYN_zDctTQbMMdS5oEpTKuhCt7suEQS_u0p_Q06kJflKg1gsRG6S3V7zA0KKpcgDhuIp-GTK2XW4z0Xhu3I4afzjD-uyGiv9YLSclNBuLnS2E_9reJ4qdSpVtrUQh8_aqSiVQva5Xc67A1Arfd0qBY9SQv4r5q504biSDdKgHE97sGpbKjrDm0IoFhoqMHrF8Ae8UYHaFgl2ogGrF3uwfsqA7MKwHsu9TQlq9k2h4tWOCPEOO887zawBCWI8HW9BnROlB4H8yjhlqFx5vwbJuvY3mrIqs5vdNCbxhYBTJ4A90g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
تصاویری از تورنتو کانادا بعد از بارش باران و طوفان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71137" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71136">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=R471JuQZQtNLnP-cfroIF_vDL2mq07jelEwBR571BxtPjWCnTUPrLeSByCB0gXFRmouy-zgdWqpPq03hLSj1Vi0k_NSZTFJ2dXuyoGnlo11M7L2sXD09e4fzjrw887RpIK4y7P2-iPQzb1tzdlr0n22nOwa_LH52D-4cIbSAa90wgzAyggaijJeNmdL8-6X3su0ihPaQ5qVRUffpee5c0fKlegTZweN8uy0h6pLzliKI28z54mWZTOtVn7EbDk91lMOJBlr-I9uSL1uQcOqTOSFJ_ru4u2l_5E7jXT4bACw0dhQZN-H7Z0MvCDUpoJcYE4w2KcmmPAPUlXEZjQR2pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=R471JuQZQtNLnP-cfroIF_vDL2mq07jelEwBR571BxtPjWCnTUPrLeSByCB0gXFRmouy-zgdWqpPq03hLSj1Vi0k_NSZTFJ2dXuyoGnlo11M7L2sXD09e4fzjrw887RpIK4y7P2-iPQzb1tzdlr0n22nOwa_LH52D-4cIbSAa90wgzAyggaijJeNmdL8-6X3su0ihPaQ5qVRUffpee5c0fKlegTZweN8uy0h6pLzliKI28z54mWZTOtVn7EbDk91lMOJBlr-I9uSL1uQcOqTOSFJ_ru4u2l_5E7jXT4bACw0dhQZN-H7Z0MvCDUpoJcYE4w2KcmmPAPUlXEZjQR2pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیرزن طرفدار حکومت که میگه:
نه پول میخایم نه چیزی دیگه گرونی هم تحمل میکنیم مسئله حجاب رو حل بکنید خیلی مسئله مهم تر و واجبی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71136" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71135">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=EpP-1sqLzG0do-8RuQVjFGUIpjENz1UZh0ThZSD9v-Q3k8MHIJrrz6QNAYUtJnaUcijqHXVlopQgLekwiHqiEjEdcyqzuuW51nW6qh60y5_P0shoYwv_i9uNs-iINnzBiYXb5_colqRmjG7qW1kFmn_Q6Hi8CDDH8VsRCtjAoCuu7iXdHSBKXPK-BYybRjuB9mZWevYSqWhzeBWkCaXXHRj83rTbfINZMw5REmCDn8-iCkQMcgb-V_bo1Twu-XLy5OxV5UU4SCxOYcWVubXarZIAkDElugcrKLnHjXvO461Am1NFzEo9OziNP6ze5XtXeCjGBQ0gFSww5fJ7fZqfYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=EpP-1sqLzG0do-8RuQVjFGUIpjENz1UZh0ThZSD9v-Q3k8MHIJrrz6QNAYUtJnaUcijqHXVlopQgLekwiHqiEjEdcyqzuuW51nW6qh60y5_P0shoYwv_i9uNs-iINnzBiYXb5_colqRmjG7qW1kFmn_Q6Hi8CDDH8VsRCtjAoCuu7iXdHSBKXPK-BYybRjuB9mZWevYSqWhzeBWkCaXXHRj83rTbfINZMw5REmCDn8-iCkQMcgb-V_bo1Twu-XLy5OxV5UU4SCxOYcWVubXarZIAkDElugcrKLnHjXvO461Am1NFzEo9OziNP6ze5XtXeCjGBQ0gFSww5fJ7fZqfYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
تصاویری از نفتکش ایرانی که چند ساعت قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71135" target="_blank">📅 12:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71131">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=OfBPFc3-SM3z-jA0G1m9D_P4-n5UNzp87kK7AiI4lLsYqcbk1OrgBllgvRqtFroIgP3cHP0E3ufYRRl8o4ZP7M0n-7BMZqooPd_LAZmmksBLTrL8mvpIlP2GubBBq0r3_A7lGFrZbwXFu2JhBV2Ds81ePK4jCujIVNAarkTqZV26gH8qS12WM6K-FO375Qk0iwj7rXT1jU0tMolW5zHtStRuG3evOPFmU7EInz-tmN1wWwnF1GcpnLjBfpaEGasViknRCNtqFYDShcMy3ug0OoAD9fUUzgpeNYgmbRbJhEaxALTuLy53ryJ90JMElto_CX9BeGooJhATKOG0D4E5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=OfBPFc3-SM3z-jA0G1m9D_P4-n5UNzp87kK7AiI4lLsYqcbk1OrgBllgvRqtFroIgP3cHP0E3ufYRRl8o4ZP7M0n-7BMZqooPd_LAZmmksBLTrL8mvpIlP2GubBBq0r3_A7lGFrZbwXFu2JhBV2Ds81ePK4jCujIVNAarkTqZV26gH8qS12WM6K-FO375Qk0iwj7rXT1jU0tMolW5zHtStRuG3evOPFmU7EInz-tmN1wWwnF1GcpnLjBfpaEGasViknRCNtqFYDShcMy3ug0OoAD9fUUzgpeNYgmbRbJhEaxALTuLy53ryJ90JMElto_CX9BeGooJhATKOG0D4E5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇱🇧
خبرنگار اعزامی صداوسیما به لبنان سقوط تپه علی الطاهر در جنوب لبنان رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71131" target="_blank">📅 12:08 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
