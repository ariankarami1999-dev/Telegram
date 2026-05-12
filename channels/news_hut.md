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
<img src="https://cdn4.telesco.pe/file/TrEjqWgMaauxzy-gDr05EfZ5RbaxYGAMpSrvwZZBsmVPwvLEYBin5bRqGy3SPlyiNstqtRrWxcZJc1fWfbzrXIyCbqqJ3TS6mAJlM5IvWeTfdNdB8cob5xrXRqwx36_VTpUpHqTE8KdrI4oZB8M8ZhyWQZqBnepPWCHRDXn-_ETiByDolgABXDzfgQHgcGE769o0zOZcvGb95Fzp0Gdstg0fJ2yx7aSpsITJ198uccPNQhw3JnFNfYONCVRaq1N0SFdOytNNdU9TgOQPuDCyC234-BNdMBvK0AN4vUPotnWltCA44xMD_dr2L4jd9wBC8UtXGUUvgUWqHhI0XzAQlQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 148K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 16:50:58</div>
<hr>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9YXVOjBGwDqIl9YmkfmX9INKyq0dd6Sc5_B7FvRnN9W1ln1ATwDwk3rlvsKQNHb-AOTyfGdfAcxfcJgP6xSmRNNhGtMZKPkNRjJl0P7VIclsj9_hE3Y3Q-nrS8Q8fHWFyxJ9_ZDL6gL1K9KVVimXd5h0x6LlBtns68Hd6sG4z7uxsfTmJ5HvYBToBQY1LzvhmyrpYD_SI817AVGVJ-8cIiGttoKXu1c1q4XfWXbvRbMD4O_BcAPbW7Xu0K0CO_XpzVSgSnKKHjqfLPUr2s36P1NfhUkkGcOYT8wHHKpbyhFZEl5TqBZXL1R6PCCgGIiOsSNXa9sDjcPhwW7kZH7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=DAH77JyTyRlsfmkJ_B3SqBA2U3KB8YulZgrqRXWWO9LkMx8f0687Ki8BNrZY0O3oY740NXTwYK1UdoxHsLks8Im2GvI26ogJzvVDCvUa81KHkULfW0AjGH7YWhybl_K4koD3uYgGXwBxchrG5hFDc_52owELJ9AnNIZZ3rPFUATgFApWUUULOMTfJ1cbysw-en6gTuj9XFHHmK07iri_pRAoM3tpHhoRhdlazw-O7BgzEY3dmMM3FN2nhdmVsLDXJ_X5Vl25WhGR5x-N0QTZvgBE-FBmi_g7vRPY7UovmQslF12HRRy360yuIgwIlcWNJLyq0BpquJERzxgLUIIvsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=DAH77JyTyRlsfmkJ_B3SqBA2U3KB8YulZgrqRXWWO9LkMx8f0687Ki8BNrZY0O3oY740NXTwYK1UdoxHsLks8Im2GvI26ogJzvVDCvUa81KHkULfW0AjGH7YWhybl_K4koD3uYgGXwBxchrG5hFDc_52owELJ9AnNIZZ3rPFUATgFApWUUULOMTfJ1cbysw-en6gTuj9XFHHmK07iri_pRAoM3tpHhoRhdlazw-O7BgzEY3dmMM3FN2nhdmVsLDXJ_X5Vl25WhGR5x-N0QTZvgBE-FBmi_g7vRPY7UovmQslF12HRRy360yuIgwIlcWNJLyq0BpquJERzxgLUIIvsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=O098DWCZ1bPw3YMcuEQ5dMeHxaWfR1qq85akoLEEMbBcohaQV1i0hdFaAFhFCTUJ7GiT4DpjT-TbM1j8uVVFDPxVH9cfFKjz46coiR1s1YjHGi_PKYzrNImzrjud8Z6T2Nf9iAmGSWnak3u-z2GeLcHi0A642pxxk1cxNf7mYm3os9XpOGB2sYKQbjp_VFbiHJZljJtmxvhfiwXkbqXx6PhcX83TinwJOnIhfA4zdE_xLDQVv_-hICOeip_m2agHB_3GQpaPwt-r-wp8lAIbSzOrJbprjTVFyD05AIpSgOWjWBGubstfrzjJIk_qBH4kArAK9P6hfc6Y4hwZ3UjD4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=O098DWCZ1bPw3YMcuEQ5dMeHxaWfR1qq85akoLEEMbBcohaQV1i0hdFaAFhFCTUJ7GiT4DpjT-TbM1j8uVVFDPxVH9cfFKjz46coiR1s1YjHGi_PKYzrNImzrjud8Z6T2Nf9iAmGSWnak3u-z2GeLcHi0A642pxxk1cxNf7mYm3os9XpOGB2sYKQbjp_VFbiHJZljJtmxvhfiwXkbqXx6PhcX83TinwJOnIhfA4zdE_xLDQVv_-hICOeip_m2agHB_3GQpaPwt-r-wp8lAIbSzOrJbprjTVFyD05AIpSgOWjWBGubstfrzjJIk_qBH4kArAK9P6hfc6Y4hwZ3UjD4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puY_PXyNfAmJTYn_-G9TQ4frA80b4cSGIyGfKJ9ZHzVKYMFyN_UdPcswvkb5yc8-yi-y1-X-WSosXf_zWoXRN8aaVUFqrU1OMXRv7z7Zffg679YfhKUbUeQJnp9bT8_5SQjHzZWG4s7xRjoF-QJx_zToveNJ1tz1UH-Z8-JyiEfcdxy50iDjkC3hPpyTWqmxEDZvMAfWj1CUpU6kKl0v5wDvTZqoICI0Ov3qhlJVThV-6sv6f2puMZSjYRw7YIsYsaUqwzvwLmcftPOHriu66zIg_xyCTpywIJk-GfYxKJAJlQq2ASrj2FgcMrazbQFz7pUy9nNrS0a1mDcfcqA9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرَک | کوتاه فوری</strong></div>
<div class="tg-text">پلن های اقتصادی موجود شد
🔥
10 گیگ => 1,700,000ت
20 گیگ => 3,100,000ت
40 گیگ => ‌5,600,000ت
درسته که این پلن اسمش اقتصادیه، اما کاملا جوابگوی تلگرام و اینستا و یوتیوب هست.
سرویس ها محدودیت زمانی و کاربری ندارند و بدون ضریب هستند.
خرید:
@SorenaVpnRobot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SZ10BblTmDg8nmJtTBcsz6p-Fjkz8_nH78mBogehhJ9zk6XrirWaneX7KAg3dw3HQaoxiNWVN85j_qm1XejlkJNOjmvTfa2_bjjAZVOLtlOp6mQqlpl6wFZl2n8rC5gKIw9CR_21KI6eMBMpXr1xx2DK3M_uqbPuj5dt_363AwxpCjkIxeTe20b_MfI1H5_Gjsjauuuu8by1w5l2BIPxXh0yQyhjKhYnA3vd9baW7dK_Ew4e8JRa_wF_icS1rXIUfCDrTWaY_RrUMieC2mM9xUUULOGHI_NJhf_utwYR_nOrM3WxD08UPKBXxlXidl3QYQUPmqhniPLsPvx6zdchOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBD604YOn2QEDa-Z8wYqvzA3_vgTTvCe2mHfJskdz_vKvh9pZCD01CSzhWrjcLcEitWenPQsNNhI7hz8U9s23OwnqKdUDfWJvY677qe3YnskCX1i_UAB4xNogPpL0D47YJByL_kHhFt1Hj0pjCZBiZ1i3s66_g7s1C7rwk8jzZkXifZK4pyjr00z07DPua-Ss3bN2DuAIjffcGXSd1Da_gBYBp02AMZa_uYfrA0FBNDsM4FHm2rfJ0rpqwxwmVeOPG7dSiN86-oXDhEQyZbYan8w5iSstDGgzwS6fzu88f6sSujbS3SS_R9G95Gkl-xeubqhGjcC56iBQgVfP3MFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJwKSdyBf6wW9w4SMf_s95Q5k45YrGZ-D6Kpx5dKD3kqeeh0NptosA6d-0g6E6KH5YQxlOrLGcllOeAVCJ9X9LKmtOHshkvCfAmzrwsTQNkTvGaotdMP5BtEyXYzZeqC0pGQZOofzUbKyjMS0ADMpCThgj1lZby0XTpsgOrXxBtNZbzyGB1opslw988wcO0xKeTC7tz1adcS1JlM1stqLnMiZ6TzkTgEKjB-ok1-NaxAdHXIGZPhu-0WqugMDs0Od0959jdpa46J6axc2-YgoIk1oebx8Hey0ZXzqOJq-r_StwM68GWQT86PuWhyNngkIp13n5P20KsCU_B0pK3fZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5eFKWVUFJu0j34tuUCALoknLdSdplxvFkcEpZfQJpNZhnw5x-O48aLfZkTk4Lj5_b0_uPjb1KyM-dPAu5zvxhaFwHSgsm1u8IzGPaNoVu4Y-wf6q0mD0cJymYRynhV_rD83CRXOGhie-nEYMXlCE6RpWQBrD7M5r9XdDmSYlWwLdCWOtTshOsK7L-fxAam81pQowGAhKG0xlVo40caco_e2yi4TgzDC9M9M8j51e6cXvv84BJR152ZMIuFSislV6Q8wvnOORcmGZ-wJw9dXiFzmoQc7Pe4xBsKUBkR3fly2VwmMM058YcDFU73cosaq_MtMDcSEojpirNJzkeqMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=YduwnEEs14zhFXoTxOBR1kjDIi87MX1AlgIS25dxt95wavhMuDHuGQkQ9fZkdHNC6Qjh-41SsAyLuCcr7ZVwxkqd_5aqGm5CCNkqW2O2Eu0Kg6I9YFiXCib4-NhSDpqiGCdYw1E9SgIepCleOBHg2tWKF1_fhQpb8YtFz9fMpa49M6bUqxpYYpkRjiimFR1QOqyPTBsmFhKnUBpf1sIW7H3darzvW2PFCqES20TUUrWVAm8oJvUShjiVXfnL3LBm1un6lljXTCNbavLmwSyfHgDgzO1sf8SEBvQ5fBasOTtpEKBWQ3cKRmeDbWkw0JznA8_FTo280AqifGB38UnTBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=YduwnEEs14zhFXoTxOBR1kjDIi87MX1AlgIS25dxt95wavhMuDHuGQkQ9fZkdHNC6Qjh-41SsAyLuCcr7ZVwxkqd_5aqGm5CCNkqW2O2Eu0Kg6I9YFiXCib4-NhSDpqiGCdYw1E9SgIepCleOBHg2tWKF1_fhQpb8YtFz9fMpa49M6bUqxpYYpkRjiimFR1QOqyPTBsmFhKnUBpf1sIW7H3darzvW2PFCqES20TUUrWVAm8oJvUShjiVXfnL3LBm1un6lljXTCNbavLmwSyfHgDgzO1sf8SEBvQ5fBasOTtpEKBWQ3cKRmeDbWkw0JznA8_FTo280AqifGB38UnTBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=rMa7kXJP7xaJXaHqb7MaV1godjC46PGgciJOxafyAo3fiHwBKQBRPbih7zF-Ko2CoU0koViEzKhTuFCTtL5QURphlBCDLgXvCctWyPjQ8xu4xyEQIEY5lqfye7cAItRt15wekGePTGhedFbR5Y-Uww09fNuxF2o0nCebQz8u8YnYXJ7cU3Zmr4Yv2VSzGEHWGMGpspKUN-ok7F5YHCmDAvNZM8pG5hpv-cFZk39H9td1L6XFKN73VLXc5wtjHVbmNMz7fQ-qBE_4KVW8mEUvDvltzlJ3TSno_jtdrBfblNr37JzNl4tsZ5tb2E4C4teNzOLc5GkSKl2S1aZ5aV3yeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=rMa7kXJP7xaJXaHqb7MaV1godjC46PGgciJOxafyAo3fiHwBKQBRPbih7zF-Ko2CoU0koViEzKhTuFCTtL5QURphlBCDLgXvCctWyPjQ8xu4xyEQIEY5lqfye7cAItRt15wekGePTGhedFbR5Y-Uww09fNuxF2o0nCebQz8u8YnYXJ7cU3Zmr4Yv2VSzGEHWGMGpspKUN-ok7F5YHCmDAvNZM8pG5hpv-cFZk39H9td1L6XFKN73VLXc5wtjHVbmNMz7fQ-qBE_4KVW8mEUvDvltzlJ3TSno_jtdrBfblNr37JzNl4tsZ5tb2E4C4teNzOLc5GkSKl2S1aZ5aV3yeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FPACZaywg41I7qdV5c_coRTtAdzqzcKWhynfKHJ1ZTvui8QdbF3b7xSFeFQydejp18wPXPaIyjf6LmkFNUIGB7AOtPhnl6c0HqFfzfcmg9_TD7qhce8Amuw3VJg1YCUZ0iP0qNUuD1bMEvBfBlRN3kLY-m_O0O6rn6R8Mjg80c2R684vVOWnukDPsQR51ptC7JBGiw_8JaNU-k5SvihwKfX2Q8XPdE-kq6XRI5ZdYLOdwNp0wtdZWjXRmfAKr2PX8kxwzBAR4Kb_tJgCsptVw3t3sglS464RacsEmbgV1lHlUWKY-WYBWFlfyqzJuaRBMb-J5RK23KsXlFKIWhSsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rVC-oNC4e5V9viWA_53Z3sgm_ebk21oEpqJ4ZS0IbdXie_DpRmFBv9GfX1PV88w7sbF67C3a9R9U6zG80QUquqUGBM9UxJqoglCfO_nL0sOCCzwRMbe40FLOCe-jPAXullLMdb0kD8FwcGrkZGzRkZNvKFVnNaUOdfPv60AkoISSTZ5eZIOHPfKXuk1jrR6Nx7hQkRSnP_cQn3Dl22rD4m9LWlk2zp7gbdnv7pK4h1lDmxnRTYvt0RRPzctiBpQ_bciNgbJsmUJTVYFyxt1kP_2CYtYcXr9THro2vcjbXkfu50rgsnqLkwDeZQM-BATGYymqVzuacTU9-HEGMLl7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt6MVqDEgIczVpzbitjGtGablON96ehbWdnZp_uRq8foIOZK1CIcAA5VHmx6RHSIDp75ZrR-6GevcI952ROlWxiSlBr5BG7iQEmQ5Igx1mJ6NfaLjPgqQVCgNHZlgaph9QK3VjzIYGYeeLYK-pcfp1ir71IWWm6oWlFXN7Kcey-IqCVZHcu4joIfBzj0Fq9yUdQVSpURiyarfcLUkWnA4NvSD93bjoKxOQoDSJI66lhO6G0JT5ZbAFtO5liiOJ9YaXm9pfyzBH7RJDuiLP2a65NDh0RoPgnUbPE3pGCbWtCqeUl6Sno4xUCzUNoBqXkmXkJy5gmA1ZkNKuUKhfI3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5-4orRUxxKaKY9cznehPeMC8Fkyf0r9kI8OmIAhbA2DuyupQ5ojuczUslL4hGZO69x4YMpM4pEbLobqKxVLQk8Joi6SeuJm_xnRs1pWjiAfELVK7JKCoRPFESA1KmcA9VrWqhwaKUuqao-vsIiuFxCA7LmlWcm272uH0bsNdy1-H1v_5gCqUIXZeQgRGIXBs6GacVYept5YPPfe3ZP2gj2Ujf7khy2BMdtfL8U3HQaay78Dd-vWU7uKjMI18ukrFmYfInFxg0DKT9molDyFDIg3veBBoZbZj9tgxboMxfiB5x5UD3x21AR5kztImFbhpU8cfXA-wGVrCQDQ0vQBQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=qGxJUrxs6kV3pW-SAfwe47Ur0KCDDa5gZpYmH3WMdPa5CpcajCRGqrpIVdNUJHFBMBbyaqPQ98Bbc93p_0KfJp1RYWGDnM_Nw6aGfO0OnjAYQ8B-oBOaCbCwhGYZbia0DmWMWvTwhRQAXt2D9OaUl1T7JoVff5Bwb-KXImfvhD5ifK2_k_7xiK93DwYbsKy15kThe7zEkf4wryt8aGcMOpROofAQ_IsLqnWND_IhmShJcBnhUVPiXr6BiyPjoFB2UgJhepTO1GljoTnVwhfWkpVUn7AlFp3UA3Kuj7uL6_6PUy89bM9j9uP7IGnrCbN75_s0u_FrRauQH0ZESQS-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=qGxJUrxs6kV3pW-SAfwe47Ur0KCDDa5gZpYmH3WMdPa5CpcajCRGqrpIVdNUJHFBMBbyaqPQ98Bbc93p_0KfJp1RYWGDnM_Nw6aGfO0OnjAYQ8B-oBOaCbCwhGYZbia0DmWMWvTwhRQAXt2D9OaUl1T7JoVff5Bwb-KXImfvhD5ifK2_k_7xiK93DwYbsKy15kThe7zEkf4wryt8aGcMOpROofAQ_IsLqnWND_IhmShJcBnhUVPiXr6BiyPjoFB2UgJhepTO1GljoTnVwhfWkpVUn7AlFp3UA3Kuj7uL6_6PUy89bM9j9uP7IGnrCbN75_s0u_FrRauQH0ZESQS-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyxr_grGrR1qR5C5EoDpAoUAOSiKdaK9Lk0dmbjrAKPVTeT2fTPkGIvX-CNcXKCQ-A9vuZiz3NSUzTkYxKiSDvGv8mPbox6pd3kpVD-M5BXDyNlwuGKkhYrLefh-xCtOOBVwhJB9ZRH7Oa8IBH-cNyo5h04lXigUnm1YB8cn9oHaTlb3q_4qtZ7nfi2FoSCZlhcDthSDuRAyQyL0KYWrQ2S82lpmL-Bf4lyLoS6T2MMlqzEmLowgc_ywlcFiWVv5lADpNmI_Rn4LL_WwoEVrU1Bu1AkqdsHMW-jkF1skHch9zrrp44pLv4OLULpvrsKRMVom_NuzMa8RO6HfRGph7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=NTd_3I6ydasQ-Ta0ltuIohaXWue8dYbNmG10N3IXxst3BebcBfY7qLjobH6AUpdP8PF9KvCLlL22y3A9oe4N7DiJPerYPdDjI_mZeWQW9yVBjZTYFmFG1K7nTPVgISxKBIjVcP00V-2VOKFBaJhkKNuEBI5MSNyPR10IbRNVTKfHYOxHnD-pqb47vGuHGuCap5oRcIxxtXzaTezn8MCF3U_gj9-4L4j1_GNpzgYlblxAXRFa3-xH65YukYj_BzQEEz8Qx9H6TcIQFrgFhnHqckOKXObtUulCnzAV8na1ePuGEdhY5bgbpU6a22z-jw1TRbdfzH-nyFiR2N1BbMQ-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=NTd_3I6ydasQ-Ta0ltuIohaXWue8dYbNmG10N3IXxst3BebcBfY7qLjobH6AUpdP8PF9KvCLlL22y3A9oe4N7DiJPerYPdDjI_mZeWQW9yVBjZTYFmFG1K7nTPVgISxKBIjVcP00V-2VOKFBaJhkKNuEBI5MSNyPR10IbRNVTKfHYOxHnD-pqb47vGuHGuCap5oRcIxxtXzaTezn8MCF3U_gj9-4L4j1_GNpzgYlblxAXRFa3-xH65YukYj_BzQEEz8Qx9H6TcIQFrgFhnHqckOKXObtUulCnzAV8na1ePuGEdhY5bgbpU6a22z-jw1TRbdfzH-nyFiR2N1BbMQ-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=UReSsdS9PqAPfYQ5fJvdQaxYrVebVDyOhijaCJm61YTYbWUTEvLkdQKrb1XV5727NlGW4ssuWR1La94P5z3ytvZMXR657rVB_eOMXjTKecAsGUySUiugZIbVSEaOhORXwMCBTHm9R0vErws-AjLYQqrh1FR86tiz6qVSyIV5MpI_6AMSb9dpdr5B4iHVZO8ucqnqXCkWG-Zv-suQaR4j18Sxu8uy_DCn1tKb9SQkqVLyorEsWhzcVacygqfl-9Q2WkeYB7C-5vlKO4CAxvbSSPsEl9rBO9vRYZiGSoZNquLDsUpKsHDN2hBHJteR_jUdUio1T88OL_4xSxtmrG8FhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=UReSsdS9PqAPfYQ5fJvdQaxYrVebVDyOhijaCJm61YTYbWUTEvLkdQKrb1XV5727NlGW4ssuWR1La94P5z3ytvZMXR657rVB_eOMXjTKecAsGUySUiugZIbVSEaOhORXwMCBTHm9R0vErws-AjLYQqrh1FR86tiz6qVSyIV5MpI_6AMSb9dpdr5B4iHVZO8ucqnqXCkWG-Zv-suQaR4j18Sxu8uy_DCn1tKb9SQkqVLyorEsWhzcVacygqfl-9Q2WkeYB7C-5vlKO4CAxvbSSPsEl9rBO9vRYZiGSoZNquLDsUpKsHDN2hBHJteR_jUdUio1T88OL_4xSxtmrG8FhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf7l2K_YJGjDLEtuAFBr2oj4B89vrDvgFV7j8LY0cIGTRiBkm5EW9uS1Q4w_jIy2P9vQGnnDSardggrkoMdvNQsqOtXAdmBPctSzwwZuFp8cSEAknOP2AuQ7Yc6MY4-msmfgD8rbzX4c5qL_GnA1Vh8AFG59oCaKZeOtHx4Q9wvZbgLfhhCTOdWlX5oDsSZcuFAUuB0BWcg8YDGHl8gFqWnI12eXPaMiYoW_IyjSuWrLtLwg52Tc6LNNbI7LS3mJPZKZ_WUXzvKErKxtwoiJIwRaDZUNt9wFLstELyxGL13KvpGKowjRdbZUDl-_3yEJeNB88r6OPkfmQuHp8vGk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UReUwBwcZ3jfrDkwWZ1CR6IBP61IiQAfsLajRdKvQKtWusBTVdkZPogoygiQQfOR30hjg0KtpZ8EPNZb0MFGt0yS96P9ApjyUAiF24tPbOouQm1kYI1xFr4Gy010hsw0iY58qKDsMSMtIbbAnowsaxALArI1-8ltuD-iAtsAUGS1MBH0KdJ_araReSDmQDrEvuBYjjCD6Pyma6vC3Goy_XiM-uNBlqhcrE-sA2uSyM5b42sW2iCxDG2pNp2EFuikUtRtGJ2hVNqyO1VTRwdy2FNpwDc7pfO9-nttc5sdzBynOnxeqShYx1YrvF3bJ9upZpYUVG9Pipe-L0vTlX3eIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=KfjOzIhw-EL12Ih2S-LtKPhxuEvOVC1aobqMwAmGsEMB7RaJVfS5nWPBlG-rHdO8Apz1X18F3fUbXoXFGlz5-WWFTxT5v3AtGA_xxQrR9LqO885eX7kUbZoaeIKoz2ea1ymCQsoy1rR4Dc2OGHC2X3WSObl67KdhQfGQDIcZg2GRQ9uvGqxFLb1t3LAEsFridHQ65dg5zDIwBxlayxG2i50anCw8bxMWflKz4SJmEjpJFUJBTDojMaFg7NyOcYhm0jCdwKJu7L_VBSAWdGywCJxCjlN9n57zBx5KkvFCVgFIqw2Twf3d1qhDRyIU-_xt9QJ2U_Sk1x6NxbRI0y64nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=KfjOzIhw-EL12Ih2S-LtKPhxuEvOVC1aobqMwAmGsEMB7RaJVfS5nWPBlG-rHdO8Apz1X18F3fUbXoXFGlz5-WWFTxT5v3AtGA_xxQrR9LqO885eX7kUbZoaeIKoz2ea1ymCQsoy1rR4Dc2OGHC2X3WSObl67KdhQfGQDIcZg2GRQ9uvGqxFLb1t3LAEsFridHQ65dg5zDIwBxlayxG2i50anCw8bxMWflKz4SJmEjpJFUJBTDojMaFg7NyOcYhm0jCdwKJu7L_VBSAWdGywCJxCjlN9n57zBx5KkvFCVgFIqw2Twf3d1qhDRyIU-_xt9QJ2U_Sk1x6NxbRI0y64nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=oYGK82kHHZk373jVberZ0CbCZqPOZ-EAFe7gQTwMeF51FJrDV_uI1eZteUszodH76YL3IH6n9r_UN2HLFWPULVoCciAl92CJ0gMNhJ68Aj_1gZfWGPXCc_vD-4LWxvUwUaBHhNGgSQJ5u10Hu40ImUidc5EDSVca3vcdVZh7M44imLNjdgYuFRwYz5HRTtJ1LlGGZtmz4AxzbhtzsaMHW9WZB6EIq-bhWHYGQD8osWfEHSu2zJcpyxhk1INu0lri5Z3ctan_Abi60u3db2vxa4t47IV7phybCqPV-6UFBFnZ2CVqqTMyMHn_vzLUX2-sED2SMLJN-u5jFc5Diuh8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=oYGK82kHHZk373jVberZ0CbCZqPOZ-EAFe7gQTwMeF51FJrDV_uI1eZteUszodH76YL3IH6n9r_UN2HLFWPULVoCciAl92CJ0gMNhJ68Aj_1gZfWGPXCc_vD-4LWxvUwUaBHhNGgSQJ5u10Hu40ImUidc5EDSVca3vcdVZh7M44imLNjdgYuFRwYz5HRTtJ1LlGGZtmz4AxzbhtzsaMHW9WZB6EIq-bhWHYGQD8osWfEHSu2zJcpyxhk1INu0lri5Z3ctan_Abi60u3db2vxa4t47IV7phybCqPV-6UFBFnZ2CVqqTMyMHn_vzLUX2-sED2SMLJN-u5jFc5Diuh8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnxPxcLLMtpAVi9BZSn-wR81Dao64erNS-IZU1gzFE2cdVwnZvW13L-AMqm_lDa9jSADTTx-LkaU0RX2QJzQuviu32Otv_OoSMEH6oxgP2MYfloj-IkT_glq8mNApIeRLEDo0WhnOmEkIY6NtcN6mnJVIcf10ni4hp1Ob3u2ihs04EE2cul5hqy1wMvXzL5W9D2_w9-vrg0JdeURVyCTlGWcIGgSFa8WP2S0Zc3ANHfcFz2YwqM41zNQy0JP3X5OYqIpFXPnHoQvtw6xvr9Mh3KJ7Vov1fSl38E1Iv3l_LwMlB5G5pDw8mh2qOjSY8bvI6B3HKJmuc3fi5RNjTLQhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ul-JiFcu8quUFacsZ18VAdenER7zjaR0iOAHXIxjCpZ08MxtKpV2Ef4zAveQwMQ0jhZRrH504ijUC4p_sq2u6BXOzgQ_yM4w9OovbKjEhxKKJVjqcNX2IC2d4E3eg3sE6nyEZC25ef4SVdzdvsMABRB7HM-zQzzaU3jZVLhjIpxGzvNzrxUvQlxtCKJHbug35ZwKiff2QhkZJ1oMA4m9WVlIAsNj3UJWxbhOKUU1iASVWFddZTqsCtqpccEIpFY344ilvFp6E-bNklIBfyQAVOsxDQtGO9JSajjtzRwh6d99q-wxCHwFKnyvrcMxz_Ody3-ZhqexLH_0BozWxyMjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8hPYBSSgulcpwx85djs33ju_K_o1jKmG09sPj0kuoI0SVaaBp9-SVETBA67D8DmwGjDN8mGRY8ZitTSX9CmarlbMSiLl08HYO_KVdcTQV-AnAzl5WupMQgpsi24jjF93x0spNenUAiguD1py8ezD_3CSsD5W0umKQbVID4RV5MjeFzIEqaFd2AjDNNMeuibawRGNE40M4o-4ppG2vb4hWvPpVBwB8rnYwsaudOu-cVQnHV5-B5NR7SmhVB4hJw-sPkgVPYVQ4VItsmsF5MWgS6qhbSWIVvjXIEbYWS5Asgjwlh84N2BIB-cE30krd2hL0_0rWLpmAbycFMkqFHGVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDapX_D9-G5lXQDNtRYcxWF5_QqRMT21ePuUXQdwCfx7a25_XvmYHthqf1FtmK8Xk4wzRWX0J0XJ2wZkBX_3sP5gXY9kS-nrHq3F8DyWxXSiXYIm_i7E9S36pZMNJDlcxPm9GF3nsMnMGUkIzoO7R_t65qaIHd07t4eDE_lptHa1h1qUwRXdformlTTM1I97GPQ4VavQlEUDXhQ91CsgAqRF7Yr6YvVhKkhK40zFy0smekebSSrpbF6IEexNbGfMzuZUA8GLdlh8o3OdI5YAFEUrngUZBF7CqMRTPOAd1uRlCY5l0S2T_Dt0IzwkP4QT2GoR6bk8KLxu7mmuSaf2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=U5UOmPs3TqGgy7i1Q70hMhXCavp0p5RXQCMUF79HzcBr_K8MgjvkvYCHUvly6KU-oC1Jm8MyT5mgx8JQrQoMH8lpFdkS-kkbHEcJjXW0Pr82zn92clnXvvBdlldjla9_ePkk1lZKIegmMQa2JBNo14elkA5323RQv07Sd4m5G56zVhpN5oTQOWp2y6gj7nEe-1q8A-4vWW18KKVnXo5SIhiRaxydzQrk3DyRhxlF22HT1FRLHh-16P6etMxLEjen1Rj8jzlgU8pX6hqYmcGxnSANCr6WAJhW8eJjiOPlYJz92f-9N12KhD_Hzx69vMmgE098MwA0O-okhd2G1MS8Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=U5UOmPs3TqGgy7i1Q70hMhXCavp0p5RXQCMUF79HzcBr_K8MgjvkvYCHUvly6KU-oC1Jm8MyT5mgx8JQrQoMH8lpFdkS-kkbHEcJjXW0Pr82zn92clnXvvBdlldjla9_ePkk1lZKIegmMQa2JBNo14elkA5323RQv07Sd4m5G56zVhpN5oTQOWp2y6gj7nEe-1q8A-4vWW18KKVnXo5SIhiRaxydzQrk3DyRhxlF22HT1FRLHh-16P6etMxLEjen1Rj8jzlgU8pX6hqYmcGxnSANCr6WAJhW8eJjiOPlYJz92f-9N12KhD_Hzx69vMmgE098MwA0O-okhd2G1MS8Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
مارکو روبیو وزیر امور خارجه آمریکا: ایران به توافق جواب رد داده است
👎
خبر بالا فیکه و روبیو چنین چیزی نگفته
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64840" target="_blank">📅 00:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کشور عراق، تلگرام رو رفع فیلتر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64839" target="_blank">📅 17:21 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64838">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏ترامپ: ۹ جنگ را به پایان بردم و در زیر دهمی زائیدم
@News_Hut
#Fun</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64838" target="_blank">📅 16:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64837">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adrR3yRs3wu12A8nkY6L7D6rhAoJ3vCC1zYehzXrFjeiVoTsMYx-N4YGlympzbBuLQ2RpkoLZ4X9Mm4USuTFjlCGdy3CayGIrlZKr-U7u8ciRun_VwUIhAELQIDzqfuc6oWSSgIloQETpA7q0o-NDnWBAEv0l80gAmypTEIdWgqmtlPApjb2vrtGnYUyEGuA4R3CozZKIhx0DS9KeRvBySLw9HXWCXZ1G0BfrA09EguTW0C2SCys_J1t8r4hsYeqbVQpr-5fVMtN72K6iiubgpNaAh630cxRFOurJMQW3RG-TUEz_Lt9dIK-G0gO8rRObK6QOocXJAnL5tskrk52eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#مهم
؛ این لکه نفتی اطراف خارک نشان می‌دهد جمهوری اسلامی به‌ناچار نفت استخراج شده را در حجم بالا، به دریا می‌ریزد!!!
اقدامی فاجعه بار برای اکوسیستم خلیج فارس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64837" target="_blank">📅 09:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64836">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=vCB_62WUkJyD5HRUi1mTLhQbnuLAfOOor9ajuPrEXVt7VR5YvSfP9uiaY-HwU0Xbk207omKlG7eApa7O-Wou4pVvbTh0RJa2_DnwYaNBzTTGYiarf8U3TCABo_o78Y-Dn7eWcdvGCdo643MZXK4To4kERC8KNNyHE68uK5a95kodmKEge6U7wkRqQTTD7GpHvNjfa-ocBmMO9ufoBE3skNXMv_qSGuDn3mcsem4yAzWLRvpaNpQjiC8XQYyWt8zU4opzdr_rAKQgtDhjVdw1pLhaZ76tW0eHZw8Bst6JQTgYicn6eAPe_8YmxDq02_GcbgJBAU5A3yAjMmaoVBc-zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=vCB_62WUkJyD5HRUi1mTLhQbnuLAfOOor9ajuPrEXVt7VR5YvSfP9uiaY-HwU0Xbk207omKlG7eApa7O-Wou4pVvbTh0RJa2_DnwYaNBzTTGYiarf8U3TCABo_o78Y-Dn7eWcdvGCdo643MZXK4To4kERC8KNNyHE68uK5a95kodmKEge6U7wkRqQTTD7GpHvNjfa-ocBmMO9ufoBE3skNXMv_qSGuDn3mcsem4yAzWLRvpaNpQjiC8XQYyWt8zU4opzdr_rAKQgtDhjVdw1pLhaZ76tW0eHZw8Bst6JQTgYicn6eAPe_8YmxDq02_GcbgJBAU5A3yAjMmaoVBc-zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آقای رئیس‌جمهور تقریباْ ۱۰ هفته از اصابت یک موشک به یک مدرسه در میناب می‌گذرد. چه کسی آن موشک را شلیک کرد؟
🇺🇸
ترامپ: این موضوع الان تحت بررسی است و ما به محض اینکه گزارش را دریافت کنیم آن را در اختیار شما قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64836" target="_blank">📅 09:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64835">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
ترامپ: می‌خوام کل ماجرارو تموم کنم
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64835" target="_blank">📅 03:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64834">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
ترامپ: خواهیم دید چه می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64834" target="_blank">📅 03:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64833">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مارکو روبیو: متأسفانه، تندروهایی که دیدگاهی آخرالزمانی نسبت به آینده دارند، در ایران قدرت نهایی را در دست دارند.  @News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64833" target="_blank">📅 00:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64831">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGDO0dYa93ZBESdm_pCPxsdkzha3RRHDtSunnurJXEl_S7dSK_4fi2ooxO5zVd_IBC0RvYb2gi3XyKBFdrztitAbbq-9n7Dwp-1-ar-OVSmp_I1hCQSovQKJoUI7cELDNIrR-8avpOHeUFQ3Mh21UD96-xwjrP47TkyAS4Oss2xAIXYivSCqBNixiqQvoOrMNonCPq9hy-70Wq6JgtpFPzavgsS-c_Hjz3676eQVgJaGNYu7kkJSeg9QJ7s54D9Oz17I6oN_u0m32M89BnXMMB8Ggl6Yb2sTYFZUzHI2WQm6Zb8LBu3x7AK7PA6NC1ZGhGAY-qJ6i-r7OA2FOFQPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9BEgY2uS_gEE4vMEjMfshQbp-OdMtP_QlxxaBXFo5bvArh7uQ0xc0YtksYyHXI90GLyVjlNJHlrUtcpt1efj4u8yCJj7k24CgOYrHQMS_FkO0dNrI50dKbWkLuNf88LpnDmrGy1y2zqFt2fivFGdYyUjxbdGSHXf1RaiY2PKVZUj8ZAdLA6B_mTbHFzNWPXrYbxyI-XvR8APaUanl35BXA-hISn1vj5LIwttV0TfGDnbG0chDwnNcapPCDhHcMsVSYkqcQYNT1hz3hx-aCrdZg_1PJFHKjMm9n0pnCJhU3GUzxvUdpo9vs2OcP4UsXSDudn1LchUBafcV7ihQ4xAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnaXZn2Mw58WvrLTn15UascQ1hc118BjvgxEgT_HVmt2l8EQ37k8PdzcF4aHsSal0-W8GzZZTDelZuvXb0uRyVnYe4o2-AgvOYiEL4WpXLKSSlD7GtvJbudEZQo-Q7M-vWkUS4tTIP1i3x14EfJ022gIrWrvu8mwbQJgrC_VyiwskBbfosnGoEyS0tMAMdGPBe2IxTVwlj8z22faEM3U11ZuCKl3uD67nh15gi7jUZr2drdcPFA1mrRPmpfbDPXrYJOwG31v1LCTYOWG-2glFR5Bvqvs5OFD7V2W_5HUsqNtxkD86N-yRP5FvOC_eD7Ff8i2LJzEgSmfyghaIYxDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rGzu0vwhCNEeo40gfhfxeY_WGJ1z9x-QQjVdqPai6-Hpas3yZrrxLbTWM5piCKI6hyXy4DwPAxadWACxKrmAVw535kNVm8JGLbH5ExIHmAVGFP-sOrqYcYjgXeJIKGjtYFUN4RNsVwyfxzCqv3HCCim2XtVMP0M9_2qYoxtpmfStynzlNYLY-4rJtByA1e5SMwPeWFxW7xsXq5SsjVcbg98Ak18ZoD-zTHk04_BkFy2is_AmToKj2QLRQZn_8gNKQ-bzD1FV7Fefyz5MDGNOetMwUiI-UbY35WcnUhDFxvfOSSFw3_n9lPTjyMzN6vpptmgNaCPsx9ZjsyYmopZEew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فشار جنگ کم شه
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64828" target="_blank">📅 00:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64827">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=LvK22qcl2IhM79KCOCVdt4SEXSPyFNZVrT5ibv1V1xEk9632xFSfKuS7LP8tvL3RYJuGgJ3aOhKuRpNU0Ak0Lm2fTojd8Goidry0bJFyTaO-3zkGT2uMlXUK2wasbeEzpQOHpCdN39xEoSOcPLE9rKBYm68zLnHCuHIZvKhjlAmx04rvLAOscrL_83Am2QpIZkigYVY6eFmbQkvVmMxpDTxmCI5swbu6bSLPmzDkaIeYOtHC0940RFppwV7VlYrihVbJ9KdfpAWObl2W2hP7amvtwiqngk_8eNF-ufJqITjsglRntjoMagLbAbSxeLDZhhHaXM62XeioAi0lyLiJMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=LvK22qcl2IhM79KCOCVdt4SEXSPyFNZVrT5ibv1V1xEk9632xFSfKuS7LP8tvL3RYJuGgJ3aOhKuRpNU0Ak0Lm2fTojd8Goidry0bJFyTaO-3zkGT2uMlXUK2wasbeEzpQOHpCdN39xEoSOcPLE9rKBYm68zLnHCuHIZvKhjlAmx04rvLAOscrL_83Am2QpIZkigYVY6eFmbQkvVmMxpDTxmCI5swbu6bSLPmzDkaIeYOtHC0940RFppwV7VlYrihVbJ9KdfpAWObl2W2hP7amvtwiqngk_8eNF-ufJqITjsglRntjoMagLbAbSxeLDZhhHaXM62XeioAi0lyLiJMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی مسئول دفتر علی خامنه ایی درباره مجتبی خامنه‌ای:
خونه اقا مجتبی رو زدن ولی ایشون تو راه پله ها داشت میرفت طبقه بالا و فقط موج انفجار بهشون خورد و افتاد زمین.
فقط کشکک پاش و کمرش آسیب دیده که کمرش که خوب شده و یه خراشم پشت گوشش برداشته ولی الان خوب شده
مردم صبر کنید دشمن الان میخاد یه فیلم و عکس ازش بیرون بیاد که کارو تموم کنه به وقتش عاقا خودش میاد باهاتون حرف میزنه
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64827" target="_blank">📅 23:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64826">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwN4tI7mGoyZCuKembcbwIFdhY1C_Lkv69YwN14qexCPch80m6cBRjZPCCrlw5ycwfr08-Ay5AgASfLfr2--Vipyv-I3V199c2msfFZ-eTtuUbyvFMOSLkAXFlH_21EAKucRH2O6KD9ApXOCrXJnFSF93QPtsVV7s6MHJaTIFIUk-3fd6eH7s-Ymh5vYB3TwKxR0RwjDOUi_nKPY7zsyqw0qMA9YxpDIvXQWcyGrHx4ByzHPhng5QVPpxyMp40kQejtzXKCwOs3RqlGUZ6F8XuC6qP6fGk-JSkWDJE4zIx_RoTpstFtcJ_2JXG0CdF201cWGnEbqyZAR_2k5gsFQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ ۳ روز آتش‌بس بین روسیه و اوکراین اعلام کرد:
خوشحالم اعلام کنم که آتش‌بس سه روزه‌ای (۹، ۱۰ و ۱۱ مه) در جنگ بین روسیه و اوکراین برقرار خواهد شد. جشن در روسیه به مناسبت روز پیروزی است اما به همین ترتیب در اوکراین نیز، زیرا آن‌ها نیز بخش بزرگی از جنگ جهانی دوم بودند.
این آتش‌بس شامل تعلیق تمام فعالیت‌های نظامی و همچنین تبادل ۱۰۰۰ زندانی از هر کشور خواهد بود. این درخواست مستقیماً توسط من مطرح شده و از موافقت رئیس‌جمهور ولادیمیر پوتین و رئیس‌جمهور ولودیمیر زلنسکی بسیار قدردانی می‌کنم.
امیدوارم این آغاز پایان جنگی بسیار طولانی، مرگبار و سخت باشد. مذاکرات برای پایان دادن به این درگیری بزرگ، بزرگ‌ترین از زمان جنگ جهانی دوم، ادامه دارد و هر روز به هم نزدیک‌تر می‌شویم. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64826" target="_blank">📅 23:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64825">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hah3lJMqu2AtFfTVPAQEaiaa2GFVuSeHEM5SQTgdBvSbv6xe3ScLeByzYK99B-EJOUAVeaLADgSQsb1hIpBvxub2iU_n4hC2DtGBNZWFXxxzDIbLH2ieVuFUz7pnzwv8TXqdmfPvvV_jCeTYgEOCtHM4-F-FbntofXgTvg57lxZgGam5yagWwGMT0ipQh9D6XD-EzfO48w_CENODf-l6LeyIj6EbPV4IFf5wBz-sgY26FkiLGytSLFvpxWPzUamBFb5BIcRRu3JHPEkd6b4SZuiO-xUgrmlxPi8-PpWL_gPX0VgPjJKAnMDsqWT3vcp-OAsHDPyV_oiRTNcZR6YtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
در مورد وعده من به شما، وزارت جنگ اولین دسته از پرونده‌های یوفو/یوآی پی را برای بررسی و مطالعه عمومی منتشر کرده است. در تلاش برای شفافیت کامل و حداکثری، افتخار داشتم که به دولت خود دستور دهم تا پرونده‌های دولتی مربوط به موجودات فضایی و حیات فرازمینی، پدیده‌های هوایی شناسایی‌نشده و اشیاء پروازی شناسایی‌نشده را شناسایی و ارائه دهد.
در حالی که دولت‌های قبلی در این موضوع و با این اسناد و ویدیوها شفاف نبوده‌اند، مردم می‌توانند خودشان تصمیم بگیرند که «دقیقاً چه خبر است؟» لذت ببرید و از آن لذت ببرید!
war.gov/UFO
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64825" target="_blank">📅 22:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64824">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
چندین تصویر افشا شده دولتی از اسناد بیگانه‌های فرازمینی، پدیده‌های هوایی ناشناس (UAP) و اشیاء پرنده‌ی ناشناس (UFO):</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64824" target="_blank">📅 22:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64822">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=roimxjDYuf1_KaPhqIGtKOWiKKsAvm4KqYY1faa-dsqnCtMiJSjNu3ZnjoSO4DhY1wLxpvEi1tq3FwWInCOV-4TJT3pxtctlWBAitlj_DhE8dbz_oqttyaYN0N_8VVCSuNpqTPFC8pTF_H9ny3Aln_Oy6lVKBuG8VjEmSwRwcn2NHV_xbM4fBifEpKPgGCzMVb0wedV3Ev-UlXEF6lUB1hl2kZ29h1d6yyEnO7qsh26GP4FhE_o5UfRuyIR1IFqNd8dExOB6IyUxjcWvzTwDfmEWi6EShTUgD7WOPccAyeaIxMizHQXdJM4G7wY00wYlxB-mlPXJe9jPN5g1vV2oWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=roimxjDYuf1_KaPhqIGtKOWiKKsAvm4KqYY1faa-dsqnCtMiJSjNu3ZnjoSO4DhY1wLxpvEi1tq3FwWInCOV-4TJT3pxtctlWBAitlj_DhE8dbz_oqttyaYN0N_8VVCSuNpqTPFC8pTF_H9ny3Aln_Oy6lVKBuG8VjEmSwRwcn2NHV_xbM4fBifEpKPgGCzMVb0wedV3Ev-UlXEF6lUB1hl2kZ29h1d6yyEnO7qsh26GP4FhE_o5UfRuyIR1IFqNd8dExOB6IyUxjcWvzTwDfmEWi6EShTUgD7WOPccAyeaIxMizHQXdJM4G7wY00wYlxB-mlPXJe9jPN5g1vV2oWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیو سنتکام از حمله نیرو دریایی آمریکا به دو نفتکش ایرانی M/T SEA STAR III و M/T Sevda که سعی داشتند از محاصره عبور کنند؛ این دو نفتکش پس ازحمله متوقف شدند.
این دو نفتکش تلاش می‌کردند در یک بندر ایرانی در خلیج عمان پهلو بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64822" target="_blank">📅 21:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64821">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
📰
فاکس نیوز به نقل از یک مسئول آمریکایی: ارتش آمریکا امروز به نفتکش‌های ایرانی که قصد شکستن محاصره را داشتند، حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64821" target="_blank">📅 16:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64820">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: امروز پاسخ ایران را دریافت می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64820" target="_blank">📅 15:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64819">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcRAGzGbkxUzteP6h7Xhi2tXcyfDiqgNhZwRL1edcJG5VuhapkaJruhauLLbi16vFVDpsyTbe_9o35a-z4gE-8WG3cK5yuq3Y-HVSKBbm7waY1-6FtKiEzkSc4GHhTT0QeSInouR3HQo-B81XkC-KfllpvjQU6-LtamGwONwzW9hxn6CV7yD12Hoye9zHUrnwMO0rr5WaHm4o2o2_5QMu3UyMNYZbqErEsmiROjAEugQt_kOT_4DDQHrKYJu5Lg9l1IjD9CiH-KOZlQVHxGKmmOop8PZNkJQpI6WLwqSk0iOqJbnVU5DZVsBwKVIfLRRZmXoNUvLKq8epQnGUR3z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات که نه، حتی اسرائیلو هم بزنن ترامپِ کاکولدزاده وارد جنگ نمی‌شه، چون سفر و دیدارش با اون کیری‌خانِ چینی براش مهم‌تره #hjAly‌</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64819" target="_blank">📅 15:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64818">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده  @News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64818" target="_blank">📅 14:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64817">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64817" target="_blank">📅 14:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64816">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">باورکردنی نیست آخوند ۷۰ روزه که مردم ایران رو از داشتن اینترنت محروم کرده، چقد شما حرومزاده‌این که دارین رکورد می‌زنید
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64816" target="_blank">📅 14:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64815">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=fhHnadTSNBm0JMS638l8ixZgntysgXOXDv8yZ2uldF6HOWdoShkcHBRFF22SnL6TAIgJsuOir0CyWpRstOOyamDr4BRlia7mgb1DowGqoPCqyBchSMpBmerL0xuJpmoR1k7Mgb_jI_TQCLzLz0_HFqnZLouwsAWVcVSWGJKxK6sX0pOiel3RINZzSM2D6DSrEaUBDiTixPPzezGJJ2_Wlnw-RzP_-Y5Z2fh7i46IEp-FXz84PbZFcz_LHbn1CJQ2GkOzSzptnLHx2HmuYW1LLB1_X1Dv_10_UjdWAMa7lzoyQYGJrrDd_3JZ1KP14k7KmI7_AhlkQYS9Aws4ftU4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=fhHnadTSNBm0JMS638l8ixZgntysgXOXDv8yZ2uldF6HOWdoShkcHBRFF22SnL6TAIgJsuOir0CyWpRstOOyamDr4BRlia7mgb1DowGqoPCqyBchSMpBmerL0xuJpmoR1k7Mgb_jI_TQCLzLz0_HFqnZLouwsAWVcVSWGJKxK6sX0pOiel3RINZzSM2D6DSrEaUBDiTixPPzezGJJ2_Wlnw-RzP_-Y5Z2fh7i46IEp-FXz84PbZFcz_LHbn1CJQ2GkOzSzptnLHx2HmuYW1LLB1_X1Dv_10_UjdWAMa7lzoyQYGJrrDd_3JZ1KP14k7KmI7_AhlkQYS9Aws4ftU4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دلیل اینکه عملیات “پروژه آزادی” را متوقف کردم این بود که رهبری بسیار خوب پاکستان و رهبرانش و فرمانده فیلد مارشال و نخست‌وزیر در این موضوع خیلی عالی عمل کردند.
آن‌ها از ما خواستند که در زمان مذاکرات این کار را انجام ندهیم.
اما اگر لازم باشد، دوباره به آن برمی‌گردیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64815" target="_blank">📅 09:14 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64814">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64814" target="_blank">📅 05:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه  @News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64813" target="_blank">📅 04:53 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64812">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64812" target="_blank">📅 04:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64811">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چالم کنید جاکشا.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64811" target="_blank">📅 03:03 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64810">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QiuqY4cgBN8liSoRGHJmyii5sHYBavKgDtPyZOr-HTLsYlLwYYUmgyzmlymc95iGDqd3lhjf-cJxH39K9ufqNWSMmCNWG_pm9B12oslUGMB3qUMoElggrWzFhdCMdAr_DSMwesOl5fSvoIo2V89VQHt6cyZG4lmQTHOqFdmgjnLZdXuNm9pajEo50wk_cF1AFXFuY4NMn7D3Qk7jpN_bRhjChrRRWxnStwYtSGAWl_thzMbD-BYZ3KL3NsHllDqIy37WwF95yYRyH9CIPpuCl9eGGoCPjQQd3zEXnxa0S8TLuX0dZ7NJh7d3PkHUVQf7-KGjDMRsKPUZ95TsouM8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
سه ناوشکن جهانی آمریکایی با موفقیت کامل از تنگه هرمز عبور کردند، در حالی که زیر آتش دشمن بودند. هیچ آسیبی به این سه ناوشکن وارد نشد، اما آسیب بزرگی به مهاجمان ایرانی زده شد.
آن‌ها کاملاً منهدم شدند، همراه با تعداد زیادی قایق کوچک که برای جایگزینی نیروی دریایی کاملاً از پای درآمده ایران استفاده می‌شوند. این قایق‌ها سریع و مؤثر به قعر دریا فرستاده شدند.
موشک‌هایی به سمت ناوشکن‌های ما شلیک شد که به‌راحتی سرنگون گشتند. همچنین پهپادهایی آمدند که در هوا سوختند. آن‌ها بسیار زیبا به سمت اقیانوس سقوط کردند، درست مانند پروانه‌ای که به سمت قبرش فرومی‌رود!
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند، اما ایران یک کشور عادی نیست. آن‌ها توسط دیوانگان رهبری می‌شوند، و اگر فرصت استفاده از سلاح هسته‌ای را داشته باشند، بدون تردید این کار را می‌کنند — اما هرگز آن فرصت را نخواهند یافت و همان‌طور که امروز دوباره آن‌ها را از پا درآوردیم، در آینده خیلی سخت‌تر و خیلی شدیدتر آن‌ها را از پا درخواهیم آورد، اگر قرارداد خود را سریع امضا نکنند! سه ناوشکن ما، با خدمه فوق‌العاده خود، اکنون به محاصره دریایی ما خواهند پیوست، که واقعاً یک «دیوار فولادی» است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64810" target="_blank">📅 02:28 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64809">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yt4fRW6-z2AY2sIKx1iBNgxTytMnzSBpnStwCQPbes0WP7E7tVWd290V9TBWXZOaynWonxj3znO5GH8MQZeTWFeDDHZWqof_Or_rPHIJ3Oa3UEruLHxR5F643FJ05-CKTTe_L8UAo4un6g1GIv8LAgGq2_rhdmjFn2SbpMdm3ElHEM3-l9ruMflz1WD37_SuL1qDNOxJUNXdHBCzAo5goNHvF2Q5T8yzO6aXKWyiKCuJ1BkJA4fJx0P_LKm2Y_kveyBt-zV4PzKDBrq5LoCTdSxL-YTxuH0Y1PaJo5HRVnACeSaerX8VthbzbAiDGejUdKSJc5BsbIDXAdg6PTPZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خلاصه: چند تا ناوی که تو عملیات آزادسازی از تنگه رد شده بودن؛ خواستن برگردن سمت موقعیت قبلیشون که سپاه بهشون شلیک کرده، بلافاصله نیرو های آمریکایی تاسیسات محلِ شلیک رو بمباران کرده و ناو ها هم بدون مشکل رد شدن و قضیه تموم شده!  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64809" target="_blank">📅 01:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64808">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64808" target="_blank">📅 01:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64807">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇺🇸
#فوری؛ سنتکام:  نیروهای آمریکایی حملات بی‌دلیل ایران را رهگیری کردند و با حملات دفاع از خود به آن پاسخ دادند، زیرا ناوشکن‌های موشک‌انداز نیروی دریایی ایالات متحده در 7 مه از تنگه هرمز به خلیج عمان عبور کردند. نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64807" target="_blank">📅 01:44 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64806">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64806" target="_blank">📅 01:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64805">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdHlLNdVobe58hwzjiIw0H3hYcdaewP5U4ZOO8Xx59dFkVYc6x1ACqMk_8FFibiFmewj3d9feWpPx9bQeZNtWuObGW9l8fy23_4HoPj3HXdYhS2DLMdW03DrNgK6_6cfkFk-fl1SRZ2yCtK7iHwE_KwsaTT7FtNgAPArrUSVYP3ezuRxTBms0YcSZ08fwm6KyEuOaQNdUzfRYaakwZfT8CDp5F77S3L0Az1q8mrD4D4v55js4SJlvYSEFT-lORNcrfcWORuHwKxguAcswZ-J_V5JLXUPoW2EVKGv1KYWyP1k7pHk0M-YRWmqq-6XZ_SjtgFhaQ2bFupSTczyw2IhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای جنگنده زیادی مدتی پیش از بریتانیا خارج شدند
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64805" target="_blank">📅 01:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64803">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64803" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64802">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eQN0kILsx_8YHRaurr03e2m-sK1YJZxUlNC-ceUgo4Nfkw3zWx-y1RenNfm6i083YLNUFppIwlvZlbHBlyXSQZRqu6SryTp4bhuWisjxGzVvSWFAUIbIHOdLXBMy4dcBDCEllQhkJ0hgKPmL4Uyk-FF3l6KP3gku34Dvg6Cae3LZEPNsdsIEPfxl8_D1ELjE6IM5LhgbUKVE3FW-z0EVLhWjE4ucltKo4GvetZ3RA_9QFCa-Df5Hdef5offvFBXdIyP5rRRoVSbOmGIpIhZgW8AuOc1Gjg4tZnS6N3e2qVDEcLYHHpIl096DE2Gv2RLqh8t4SV5Si3JdDtNEISClnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ سنتکام:
نیروهای آمریکایی حملات بی‌دلیل ایران را رهگیری کردند و با حملات دفاع از خود به آن پاسخ دادند، زیرا ناوشکن‌های موشک‌انداز نیروی دریایی ایالات متحده در 7 مه از تنگه هرمز به خلیج عمان عبور کردند.
نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک را در حالی که ناوهای USS Truxtun (DDG 103)، USS Rafael Peralta (DDG 115) و USS Mason (DDG 87) از گذرگاه دریایی بین‌المللی عبور می‌کردند، شلیک کردند. هیچ یک از دارایی‌های ایالات متحده مورد اصابت قرار نگرفت.
فرماندهی مرکزی ایالات متحده (CENTCOM) تهدیدات ورودی را از بین برد و تأسیسات نظامی ایران را که مسئول حمله به نیروهای آمریکایی بودند، از جمله سایت‌های پرتاب موشک و پهپاد؛ مکان‌های فرماندهی و کنترل؛ و گره‌های اطلاعاتی، نظارتی و شناسایی، هدف قرار داد.
سنتکام به دنبال تشدید تنش نیست، اما همچنان در موقعیت خود مستقر و آماده محافظت از نیروهای آمریکایی است
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64802" target="_blank">📅 01:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64801">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇮🇱
#فوری؛ کانال ۱۴ اسرائیل: ایران اعلام کرد آتش‌بس نقض شده است!  @HutNewsPlus</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64801" target="_blank">📅 01:06 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64800">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حوصلمون سر رفته، کاش وحیدی چن تا بالستیک سمت برج خلیفه هوا کنه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64800" target="_blank">📅 00:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64799">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64799" target="_blank">📅 00:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64798">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تسنیم: داریم می‌زنیم
💦
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64798" target="_blank">📅 00:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64797">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این جفنگیات [
کصشرات
] رو باور نکنید توروخدا  #hjAly‌</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64797" target="_blank">📅 00:30 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64796">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تسنیم: سه تا ناوشکن امریکایی زدیم که سریع فرار کردن به سمت دریای عمان
💦
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64796" target="_blank">📅 00:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64795">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
هم‌اکنون گزارش صدای انفجار در بندرعباس و میناب
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64795" target="_blank">📅 00:22 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64794">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SI6JYi1HMRSKAho3mdncsqdG1Pue2Z0utJVwa7ew-Uu72a1Z-KUstZT3HEJgO3yOiJDT9vjQoc1mYdcMGdvaCmj-IfbCnycKdaugoOW6Luq6Lvcpix6pe9WQD3KWFWIyF5NQzxBglXV_piXGS54qmI9h2kH4w74Un7ZuKivBfLVKwmAWmmXgZuCnZZy7pqYUIaVCyHMgDiBT60E6rBS_VPlP2UOt5NV4H5WoCrn5o2TZIOiZQn1uvkPtpNg3yZ0nfWPAc2bwUoblME-29iB8GapqBVCfzg4u_g6kgEAoTrzoGfqMuN7Gf5r60NhG-0zVl4nJ5ICBKy8Uj6bmrqYMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جفنگیات [
کصشرات
] رو باور نکنید توروخدا
#hjAly‌</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64794" target="_blank">📅 00:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64793">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خسته شدیم انصافاً، آمریکایی ها یا زودتر توافق کنن یا طوری بزنن خزر به خلیج‌فارس وصل شه، این چص‌حمله ها مارو ارضا نمی‌کنه
🌂
#hjAly‌</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64793" target="_blank">📅 00:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64792">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1465e8fad2.mov?token=kZGReAckmZSGFlcj9a0K-GSczNAFZM1l_hqp3Sji2UW-oVXU87zQhh8tVs2j1zjT9oqZwNiKhRUUd-I0tDdBRffR3MPw4xgObnA9VSVBXGNXjoESkh30EI23DHVAN79gHcOEOgpK71EImt_4yKtc5NacWtQBm6oFTJ3INVxyIFFDn6P2ufA2FHuumlo65NI8c0gUnl2TNFmsmtb13q8f7qYu8h_23opPWwwU3KfJIxZYy0P_YdJyDUaJ9EDq1_lDG-Uj1Bm_UGzsU5jb5-1OZYHpoj2MTDPve6Myq6n7rBDvMYT-3bEBaIExuYSIHDNtzcXqjOcc6eL2MvNN3rUd5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1465e8fad2.mov?token=kZGReAckmZSGFlcj9a0K-GSczNAFZM1l_hqp3Sji2UW-oVXU87zQhh8tVs2j1zjT9oqZwNiKhRUUd-I0tDdBRffR3MPw4xgObnA9VSVBXGNXjoESkh30EI23DHVAN79gHcOEOgpK71EImt_4yKtc5NacWtQBm6oFTJ3INVxyIFFDn6P2ufA2FHuumlo65NI8c0gUnl2TNFmsmtb13q8f7qYu8h_23opPWwwU3KfJIxZYy0P_YdJyDUaJ9EDq1_lDG-Uj1Bm_UGzsU5jb5-1OZYHpoj2MTDPve6Myq6n7rBDvMYT-3bEBaIExuYSIHDNtzcXqjOcc6eL2MvNN3rUd5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت پدافندی تو شمال غرب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64792" target="_blank">📅 00:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64791">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f809f000c.mp4?token=l1sIgOvEurV3pfbVhHOErm2QRtj8o2VuxaA_OxdgTL8znyVi0NF03KlQ5FPfbATNLtIMhjnwYxQalQD7pKTh0Wv2XU7IqpohT9AwTfe29bUNhO65w1XbyiReNijnK73LckbqnyjfwSKu8N_0vYEDQm0HTtel72-vOf7lZCBy3N3Cn5W6lU-YszWeONgY3-MIXbwnKM20m57sS5kkNp7lBLUBy8EdLm5u_RCgsqyeMSb1RtpfQUS0Ldhyo76lut_XGYhmRMQhLUa1SbvDHoRyjC9adz2izezhNBXVv6nLxeAB4-vyh17WjdFNdlm2Cu2nRw-khHeMLpQUPb4b_PaWPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f809f000c.mp4?token=l1sIgOvEurV3pfbVhHOErm2QRtj8o2VuxaA_OxdgTL8znyVi0NF03KlQ5FPfbATNLtIMhjnwYxQalQD7pKTh0Wv2XU7IqpohT9AwTfe29bUNhO65w1XbyiReNijnK73LckbqnyjfwSKu8N_0vYEDQm0HTtel72-vOf7lZCBy3N3Cn5W6lU-YszWeONgY3-MIXbwnKM20m57sS5kkNp7lBLUBy8EdLm5u_RCgsqyeMSb1RtpfQUS0Ldhyo76lut_XGYhmRMQhLUa1SbvDHoRyjC9adz2izezhNBXVv6nLxeAB4-vyh17WjdFNdlm2Cu2nRw-khHeMLpQUPb4b_PaWPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما: آمریکا به یک نفت‌کش ایرانی حمله کرد که یگان‌های متعرض امریکایی در محدوده تنگه هرمز زیر آتش موشکی ایران قرار گرفتند که پس از تحمل خسارت فرار کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64791" target="_blank">📅 23:40 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64790">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امارات ایز دت یو؟
💦
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64790" target="_blank">📅 23:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64789">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
📰
خبرگزاری فارس وابسته به سپاه: صدای انفجارهای دقایقی پیش مربوط به تبادل آتش میان نیروهای مسلح با دشمن بود که درجریان اون اسکله بهمن قشم هدف قرار گرفته شده  @HutNewsPlus</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64789" target="_blank">📅 22:57 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
تسنیم: صدای انفجار دوباره در اسکله بهمن قشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64788" target="_blank">📅 22:46 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64787">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
گزارش صدای چندین انفجار در بندرعباس و سیریک تو جنوب ایران  @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64787" target="_blank">📅 22:29 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
مهر، تسنیم، فارس: منبع انفجارها ناشناخته‌ است به محض اطلاع بهتون می‌گیم چیشده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64786" target="_blank">📅 22:29 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64785">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
چندین انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64785" target="_blank">📅 22:16 · 17 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
