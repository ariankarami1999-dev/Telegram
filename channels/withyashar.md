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
<img src="https://cdn4.telesco.pe/file/G7J3JlQJyOWqGwW9gmEPfk266KskkodQXgBst_8eUCNTE4c5O_Wsbxn5DEiysRzzhrFp2QlAneYL6JYaJZ4wYdtwEtBE-gnSDfIekk0CYgHEfA_C3602W60nBdclu_KpfmZ_GcDr_HHxhDh5eBztVv1HQ37nxnJVSpGxAdFzX9FwZCSBQLwVSiMpH7HLpj0KtRYWME_lwXmjy2fzkB9aTGyXgvXvOAOCamfJ_CE8CTVqWQmnXqYNaoWFRYK39RUMqoMch0u62iVXIgSDBB2DZEhQCmS_09bkOX96AJfZpj-qNI9Gx6UjkTd9K1rr-ia1_aTfw01gRmlj5szFrv0tjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 260K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 12:58:16</div>
<hr>

<div class="tg-post" id="msg-11191">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5f2c74f17.mp4?token=ltYMt0bMON4iQrCniafuH8wJmRsI3boJC7JTDhSUcFy1LqoW4BOJ0fheNXfq2E421bOX_uf5fXTZkts45alUr012ocgP9xB4TvIuGMQN3CEgTzsa-Exd-eb62daUO3gO7jKJJh8me_WdOwLNDNX3YGooxK7ui1onaktj5mPzIuRpCHR_8uqHFgyRi4of8ECdr2VayCViDoqZpU_S_KUkAX4xa8wZPzmLOsn0tsBYMQ8ZQFkkZrzKf-jwt02p6ylL7L27NOEpSOqgLJufZB7W-_RnAZUBYW67orENPgzDJykMPXpD1UXgYtUzl86ECUaVFHpn9TfEZsq9IjVnj6Yl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5f2c74f17.mp4?token=ltYMt0bMON4iQrCniafuH8wJmRsI3boJC7JTDhSUcFy1LqoW4BOJ0fheNXfq2E421bOX_uf5fXTZkts45alUr012ocgP9xB4TvIuGMQN3CEgTzsa-Exd-eb62daUO3gO7jKJJh8me_WdOwLNDNX3YGooxK7ui1onaktj5mPzIuRpCHR_8uqHFgyRi4of8ECdr2VayCViDoqZpU_S_KUkAX4xa8wZPzmLOsn0tsBYMQ8ZQFkkZrzKf-jwt02p6ylL7L27NOEpSOqgLJufZB7W-_RnAZUBYW67orENPgzDJykMPXpD1UXgYtUzl86ECUaVFHpn9TfEZsq9IjVnj6Yl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از ۵۰ سال، اولین رئیس‌ جمهوری شد که به معبد آسمان چین رفت
@withyashar</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/withyashar/11191" target="_blank">📅 12:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11190">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کاخ سفید : ترامپ و شی توافق کردن که تنگه هرمز باید باز بمونه
@withyashar</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/withyashar/11190" target="_blank">📅 12:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11189">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7505bc627.mp4?token=E5sJ8IY79twftZbAObRN9Hwwo1T1osPtx-H8hAseBw8dBulLFs4-RUaFpSlVnmaZVFGiNUojBCkoPWZgdCE5opCqO-GkCcTG0l762-GO1YbPwT2bzNQpQqDfQvpSU23Vo6kP14EneqNpUVL64DGxLsnIJAgf1SZapqr_fVN9syVbL7Sl2BMm3iZv7UFsaPquWXpUvMeJHeaTIIsuyWz4AbQpBFe4AIyQMvrRDu74YsCP-M150T8JQBorwvbLPfIuj_-ioqw9jdrh9gBAieRybkmBTrmz8JfNPWWOcSN0p2JinyGxNSYhfyhQTi2zkisxoj9QC4NGxrOS_35fSOdODA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7505bc627.mp4?token=E5sJ8IY79twftZbAObRN9Hwwo1T1osPtx-H8hAseBw8dBulLFs4-RUaFpSlVnmaZVFGiNUojBCkoPWZgdCE5opCqO-GkCcTG0l762-GO1YbPwT2bzNQpQqDfQvpSU23Vo6kP14EneqNpUVL64DGxLsnIJAgf1SZapqr_fVN9syVbL7Sl2BMm3iZv7UFsaPquWXpUvMeJHeaTIIsuyWz4AbQpBFe4AIyQMvrRDu74YsCP-M150T8JQBorwvbLPfIuj_-ioqw9jdrh9gBAieRybkmBTrmz8JfNPWWOcSN0p2JinyGxNSYhfyhQTi2zkisxoj9QC4NGxrOS_35fSOdODA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز با حیرت : داداش بزرگه نگات میکنه ، لبخند بزنید شما با دوربین ها رصد میشوید
خبرنگار فاکس‌نیوز گزارش داد که خودروی آن‌ها در چین تنها دو دقیقه در محدوده «توقف ممنوع» پکن ایستاد و بلافاصله پیامک جریمه ۴۰ دلاری برای راننده صادر شد. به گفته او، در این کشور دوربین‌های نظارتی همه‌جا فعال هستند و تخلفات رانندگی در لحظه ثبت و اعمال می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/withyashar/11189" target="_blank">📅 12:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11188">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هند: حمله به یک کشتی ما در نزدیکی
سواحل عمان غیرقابل قبول است
یک کشتی هندی توسط افراد ناشناس دزدیده شده و به سمت ایران اسکورت میشود
@withyashar</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/withyashar/11188" target="_blank">📅 12:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11187">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بر اساس داده ها , شرکت تتر مبلغ 344 میلیون دلار USDT مرتبط با بانک مرکزی ایران رو فریز کرده و دلیلش هم بخاطر دور زدن تحریم‌ها بوده که شرکت آرکهام کیف پول‌های مرتبط رو شناسایی کرده
@withyashar</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/withyashar/11187" target="_blank">📅 12:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11186">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تسنیم: کیفرخواست زیباکلام و مدیرمسئول خبرگزاری آنا صادر شد ممنوعیت زیباکلام از انجام هرگونه فعالیت رسانه‌ای به مدت سه ماه صادر شده
@withyashar</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/withyashar/11186" target="_blank">📅 11:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11185">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FI61v_B7lcOcgPlz4SSS4YkQz5q__Ru-LcMlPRQXQk6M4Lf2cBTvwI3H9Y1865SZAsh4nlslAZOOGvfzqG5A9_MHddSNhmd5vzZYOLdj22eTe6UpZv_aMeTn5FQlVNoyRVFZFzcW55JLcW6WHekAhyRnfcfGmegYqMPfFMSVgh3tO5y58k_qp0tRqDUHIFJ_XxvGL_CrjfWUsYVZxZgQeWgtLwMAyx2ny9six279yGCICacSiUAjvht_KrbiV6CMj4Zb8nc1H8idoyPir_V5FHyqIXJEX7ziBIzHw4HXB4x_zb-nASwP90lwtB9_H49fHZFQ5VKYmcAWLe0c0_Gn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی پیش زمین‌لرزه‌ای بسیار شدید
۵ ریشتری در عمق ۸ کیلومتری بردسیر کرمان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/withyashar/11185" target="_blank">📅 11:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11184">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نتانیاهو در دادگاه حظور پیدا کرد و گفت: «فیک نیوزها گفتند من به بیماری لاعلاجی مبتلا هستم - این یک صنعت دروغگویی تمام‌عیار است»
@withyashar</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/withyashar/11184" target="_blank">📅 11:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11183">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تاج : در جریان آهنگی که معین برای تیم ملی در جام جهنی ۲۰۲۶ می خواند هستیم  @withyashar</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/withyashar/11183" target="_blank">📅 11:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11182">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اتاق جنگ با شما : زمین لرزه خیلی شدید کرمان یک دقیقه پیش
@withyashar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/11182" target="_blank">📅 11:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11181">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed5af14a6.mp4?token=N3TX0qz2UmzqbTRZ7g5k_fWq-rXoTZulOnFHvZqF7pTlN3nHmVT6bIj4CiuYfakIOKR7kXR-V733x38H-D1P0VN8hq2zizZfmK0gqJBC5uTavQV6Fh2rzQtVB5-c6Qa6HgTCdCE3_mxcvkDUMs9a595JZfg6NZjm9BpYXEd72u8TIaWpCBCqItHp-w9rxRUZQOAWW2mLiSxXgKDD9KGXx1lsybckSjAWQT--85kSDa9DT36al0EXzf30U49RzAnKi0VXf4T74F6oHNFpLPU1Eqj1eAPs9L6da05EW9wAaeVfzuNf1V7tXyFFICnmv_vTLho5EYGEDXhRceCEwBnyOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed5af14a6.mp4?token=N3TX0qz2UmzqbTRZ7g5k_fWq-rXoTZulOnFHvZqF7pTlN3nHmVT6bIj4CiuYfakIOKR7kXR-V733x38H-D1P0VN8hq2zizZfmK0gqJBC5uTavQV6Fh2rzQtVB5-c6Qa6HgTCdCE3_mxcvkDUMs9a595JZfg6NZjm9BpYXEd72u8TIaWpCBCqItHp-w9rxRUZQOAWW2mLiSxXgKDD9KGXx1lsybckSjAWQT--85kSDa9DT36al0EXzf30U49RzAnKi0VXf4T74F6oHNFpLPU1Eqj1eAPs9L6da05EW9wAaeVfzuNf1V7tXyFFICnmv_vTLho5EYGEDXhRceCEwBnyOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویربرداری عجیب یا اسکن ۳۶۰ ایلان ماسک از موقعیت با گوشی خودش
@withyashar</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/11181" target="_blank">📅 11:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11180">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2386995c2e.mp4?token=VkZ5OUlLHjTfidkZ_1m6CQRy_8BzrEUDdypM1FWLM1nmksRbhPQSBqnB8LEtC3xBrXiYuLTPyaA0xSXQSI80qlDYHIplYKTWdDjI0NnD7v2Ck14SBtmFg_ywTlTkBSzwvNdrQx5aK9Jlfc7CA7b2nyQOEYqbUM3Odw55zjXjA6mbkehFUUX9Fq9ypU9Wux6EPuqmI9fGvuJlhnLSOkgGHmTWz67D5qxMksY1G_CJo2HZECxnkk2es0ote9cFnWkwx7j5J-XD52oZG7ZeoaWWogoPXg5TeJE2JdiS7UFYDW8f-OP5_q_I3UxDu8ycE3E_w14AU6dhG9KvsZE6UUoydg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2386995c2e.mp4?token=VkZ5OUlLHjTfidkZ_1m6CQRy_8BzrEUDdypM1FWLM1nmksRbhPQSBqnB8LEtC3xBrXiYuLTPyaA0xSXQSI80qlDYHIplYKTWdDjI0NnD7v2Ck14SBtmFg_ywTlTkBSzwvNdrQx5aK9Jlfc7CA7b2nyQOEYqbUM3Odw55zjXjA6mbkehFUUX9Fq9ypU9Wux6EPuqmI9fGvuJlhnLSOkgGHmTWz67D5qxMksY1G_CJo2HZECxnkk2es0ote9cFnWkwx7j5J-XD52oZG7ZeoaWWogoPXg5TeJE2JdiS7UFYDW8f-OP5_q_I3UxDu8ycE3E_w14AU6dhG9KvsZE6UUoydg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه ای زیبا در چین که کودکان به ترامپ و شی خوشامد میگویند
@withyashar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/11180" target="_blank">📅 11:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11179">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38a96c0966.mp4?token=mFVRrMy6JJLS61iHNZh3PgLMCdzPlRQeD6OgLZtopsB8K7CjiHZ8w8BQGa8cduQhiSI8aRzdc7gi5nem4JAH60gDBxceCnurR3uV5bvVFgagqOz0gatXvrLV_PZp6GMIH5L3lguTAR5zcT31SYgwcmxqXVDFUzTtYhmBPEk9cvWoaY7k0W9gbG3yP69pT_NNjSFTrtwo0MjIVxK2_vGZNQLm3FraAMoZXnSpdRPkJl3qdAGXmJgwYXOhLlaQHd1oWEPUXdIXYlfsY_LlmSwzK66oYTy-Fh-sHKA5GleLvwzjpbi58UncVHQ9nvizU_QjWQqCb-Fvy4BA7IJlLj7xoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38a96c0966.mp4?token=mFVRrMy6JJLS61iHNZh3PgLMCdzPlRQeD6OgLZtopsB8K7CjiHZ8w8BQGa8cduQhiSI8aRzdc7gi5nem4JAH60gDBxceCnurR3uV5bvVFgagqOz0gatXvrLV_PZp6GMIH5L3lguTAR5zcT31SYgwcmxqXVDFUzTtYhmBPEk9cvWoaY7k0W9gbG3yP69pT_NNjSFTrtwo0MjIVxK2_vGZNQLm3FraAMoZXnSpdRPkJl3qdAGXmJgwYXOhLlaQHd1oWEPUXdIXYlfsY_LlmSwzK66oYTy-Fh-sHKA5GleLvwzjpbi58UncVHQ9nvizU_QjWQqCb-Fvy4BA7IJlLj7xoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آقای رئیس‌جمهور، مذاکرات چطور بود؟
ترامپ : عالی بود. چین زیباست.
خبرنگار: دربارهٔ تایوان هم صحبت کردید؟
ترامپ: (پاسخی نداد)
@withyashar</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/11179" target="_blank">📅 10:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11178">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مارکو روبیو تایید کرد چین و آمریکا به توافق رسیدن که ایران نباید تو تنگه عوارض بگیره از کشوری
این «توافق» فعلاً در حد موضع مشترک سیاسی و دیپلماتیک گزارش شده، نه یک پیمان رسمی یا قطعنامه بین‌المللی.
چین هنوز در بسیاری از موضوعات از ایران فاصله نگرفته و حتی در شورای امنیت بعضی قطعنامه‌های ضد ایران را وتو کرده است.
دلیل حساسیت موضوع این است که حدود یک‌پنجم نفت جهان از تنگه هرمز عبور می‌کند و هرگونه عوارض یا محدودیت می‌تواند قیمت جهانی انرژی را به شدت تحت تأثیر قرار دهد
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11178" target="_blank">📅 03:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11177">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">@withyashar
سفر قاهره</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11177" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11176">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قصه بگم ؟ شایدم بهترین شرحی ‌باشه که لازم دارید بشنوید …</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11176" target="_blank">📅 02:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11175">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11175" target="_blank">📅 01:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=K9nKOM8tgP5kELIk8bNtacjvRITXi1q7mA1eS7BYaB4pNOmnhfc6S32B-vN3b6ZoS10OABcKC0hJvX3i47xnTlx28kBR2n8_mUGpAgPX03WUfauYqgZBnBK8adi-53x675Xk2CyzMOIrcgWi1rqxBUY1w0GlNzxbYsz7eXI2a-jMpbvXW575-L8hzv4HLix6RXvH8gruHIVEreHeqX1WXvpXCEZsslcKmJyEKwjqLH7XMPPqA5zvxXRDjbmxRtXWiR4CH6uFtRMYkquJc89HFAsYWQrcSxAceToFYy10YtEHpstibNZXQGVHHBiaR5gcTh5yQaXdNVD0jwxYQHNPEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=K9nKOM8tgP5kELIk8bNtacjvRITXi1q7mA1eS7BYaB4pNOmnhfc6S32B-vN3b6ZoS10OABcKC0hJvX3i47xnTlx28kBR2n8_mUGpAgPX03WUfauYqgZBnBK8adi-53x675Xk2CyzMOIrcgWi1rqxBUY1w0GlNzxbYsz7eXI2a-jMpbvXW575-L8hzv4HLix6RXvH8gruHIVEreHeqX1WXvpXCEZsslcKmJyEKwjqLH7XMPPqA5zvxXRDjbmxRtXWiR4CH6uFtRMYkquJc89HFAsYWQrcSxAceToFYy10YtEHpstibNZXQGVHHBiaR5gcTh5yQaXdNVD0jwxYQHNPEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/11174" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm.rh</strong></div>
<div class="tg-text">درودی دوباره  یاشار جان
میشه سوال منو ج بدین چرا ترامپ وقتی وارد چین شد نیومد ریس جمهور استقبالش در صورتی که  باید بیاد ؟</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/withyashar/11173" target="_blank">📅 01:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال N12:
ترامپ داره به صدور دستور برای از سرگیری درگیری با ایران فکر می‌کنه
@withyashar</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11172" target="_blank">📅 01:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ائتلاف حاکم در اسرائیل پیشنهاد انحلال کنست در تدارک برای برگزاری انتخابات زودهنگام را ارائه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/11171" target="_blank">📅 00:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11170">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFhGKTWQRG8TsYJaMY4nc7S08l6fnVh9TorjB7eyUtU7PVveor0gK9qj79rsWoPtGg9Bpmjlnsun2UGnyIBuxgXLWewAvB0HLN6XyiH30iEbuzUTVUkbWWrL9TG-jvTe6aNjhvOdXie2Loq0e2g13IrLSuSXzyovYTTADBzLYkzzFpSS_Elp_lXxz4VBBJhK64HUrBnvl6b8HCHUDEpdCh_y2wLnny-VLpNk7sROSZDxLCzcWvJCBZmf6lBMOGBxXzszud8gJiYXC4FGobt-qpf9hpEDoJyx4spcCn9_a-vjD3xrMVP3nfrkge-Cj_kLlvBq6TSvwdJycf2bbtp_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارن تحلیل میکنن چیکار کنن
😂
😅
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/11170" target="_blank">📅 00:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11169">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خوش‌چشم: ترامپ رفته چین التماس کنه تا میانجی بشه که ایران جنگ رو تموم کنه
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11169" target="_blank">📅 00:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11168">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کامنتم زیر پست ترامپ
https://www.instagram.com/reel/DYSl8QEMZja/?igsh=MTNieGh0eTQyOWtnYQ==
بترکونینننن
💥
🙌🏾
حملههههه</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/11168" target="_blank">📅 23:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11167">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246f928b9e.mp4?token=bK30R-Oodc8C03-eE8-v940hI0dNDG3HojMkzFRZ52-3fHUqqF5u46UF7D67FquONdEpR5orEOMvXtyGQO2V5OBel-4Wgra7h0o7QfsBGr7pBVpaibu4qCW7HpMGLFrhzmimab2hhyeSSMJnz3EA0Bbq1MKscKOAEgaNqtr7sVcI4mcrEOTdnVuP2Kl5CMBGaT4cxWAfjyGRWrHvkfETbyNQ1q7Yu5lgIFLb3unYu7cZ50RdW-m516-PD9-VW6MLfEknhrUkI8tTf9JNTxLh-JMrGooCcVhH1s85MYpkxC0d3eJG_SswK22MzOSuIhzlIhzNaVNvjMLiiSVhr57Z_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246f928b9e.mp4?token=bK30R-Oodc8C03-eE8-v940hI0dNDG3HojMkzFRZ52-3fHUqqF5u46UF7D67FquONdEpR5orEOMvXtyGQO2V5OBel-4Wgra7h0o7QfsBGr7pBVpaibu4qCW7HpMGLFrhzmimab2hhyeSSMJnz3EA0Bbq1MKscKOAEgaNqtr7sVcI4mcrEOTdnVuP2Kl5CMBGaT4cxWAfjyGRWrHvkfETbyNQ1q7Yu5lgIFLb3unYu7cZ50RdW-m516-PD9-VW6MLfEknhrUkI8tTf9JNTxLh-JMrGooCcVhH1s85MYpkxC0d3eJG_SswK22MzOSuIhzlIhzNaVNvjMLiiSVhr57Z_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه استقبال از دونالد ترامپ در پکن، چین
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11167" target="_blank">📅 23:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11166">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/11166" target="_blank">📅 22:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11165">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/11165" target="_blank">📅 22:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11164">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پیام سد مجید موسی ، فرمانده نیروی هوافضای ۳پا تیم ملی رو هم بردن وسط میدون مثل میمونای سیرک  @withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/11164" target="_blank">📅 22:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11163">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad1f53604.mp4?token=lkzU38hfwnQuS64eICAB2PPZDbviVls9T8mxVU1FODkGd2-VB5PBgFp2A_aU9-yx5c-Y1HL_FQOIeqxPJMBj_UZuXEvwI27SoCVi0uoHfN0d-aEMOdJKuP6F6UtAhgDlPNSlk9O6hI1lZDtIA4wxi7YfQWm7brc1cMX9Lv8QuY8F1DnlzJukThQW9c8k90rf7rqySG-Em4lNhXno9-Q_qUouVNx3dBjCNbpCD0XxO-hRtA6n2Hv7nWwV9eomoc5HJ_DMEYrBT-xL_QnthCFj0INAV0pnuUGym38fkCqlbYA5ZXeiV-hn8NeXzyKpUaJcyh7DOMXK24io33XMMdN9Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad1f53604.mp4?token=lkzU38hfwnQuS64eICAB2PPZDbviVls9T8mxVU1FODkGd2-VB5PBgFp2A_aU9-yx5c-Y1HL_FQOIeqxPJMBj_UZuXEvwI27SoCVi0uoHfN0d-aEMOdJKuP6F6UtAhgDlPNSlk9O6hI1lZDtIA4wxi7YfQWm7brc1cMX9Lv8QuY8F1DnlzJukThQW9c8k90rf7rqySG-Em4lNhXno9-Q_qUouVNx3dBjCNbpCD0XxO-hRtA6n2Hv7nWwV9eomoc5HJ_DMEYrBT-xL_QnthCFj0INAV0pnuUGym38fkCqlbYA5ZXeiV-hn8NeXzyKpUaJcyh7DOMXK24io33XMMdN9Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام
سد
مجید
موسی
، فرمانده نیروی هوافضای ۳پا
تیم ملی رو هم بردن وسط میدون مثل میمونای سیرک
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11163" target="_blank">📅 22:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11162">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8efa0d4403.mp4?token=cNa8Og7RO-1gWvRolAMvVkvf2Kd4ky0pHwkakP81NzaL54PYzGLkhHG_OvYZ5TP_C2SfdxSHI4gdBYfwHL3dyX05IbtflOpTBnmgjQ0oXkL1Co5TQD89eodqp6_I8kYiGBxMLxJtjBnCQhwf_2bQq07EvO2EpObOUEf_8q-kBvLr42P0aaKCGBA2rGCTgsLFroBHHoxYpYf_7S2d5AP2tft2AaeN2bMOYkWw6haq32-xv3NSVXPkDwzzL_8jLBmNXzhdyYxVYZ1KLykveBPMcJPjkjvDcUWv7XooLEhJZlej2jXr746eewEfuHJQRhPrUN5I41gMEUWyp0et2oMcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8efa0d4403.mp4?token=cNa8Og7RO-1gWvRolAMvVkvf2Kd4ky0pHwkakP81NzaL54PYzGLkhHG_OvYZ5TP_C2SfdxSHI4gdBYfwHL3dyX05IbtflOpTBnmgjQ0oXkL1Co5TQD89eodqp6_I8kYiGBxMLxJtjBnCQhwf_2bQq07EvO2EpObOUEf_8q-kBvLr42P0aaKCGBA2rGCTgsLFroBHHoxYpYf_7S2d5AP2tft2AaeN2bMOYkWw6haq32-xv3NSVXPkDwzzL_8jLBmNXzhdyYxVYZ1KLykveBPMcJPjkjvDcUWv7XooLEhJZlej2jXr746eewEfuHJQRhPrUN5I41gMEUWyp0et2oMcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقص امشب از گلشیفته
😅
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/11162" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11161">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تاج : در جریان آهنگی که معین برای تیم ملی در جام جهنی ۲۰۲۶ می خواند هستیم
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/11161" target="_blank">📅 21:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11160">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">طبق گزارش NBC که به داده‌های ناوبری استناد کرده است.چندین کشتی باری و نفتکش مرتبط با چین در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/11160" target="_blank">📅 21:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11159">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شکست هفتمین رأی‌گیری سنای امریکا برای پایان جنگ علیه ایران
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/11159" target="_blank">📅 21:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11158">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d2e0e1e0.mp4?token=NTc8jvfn4C6Vrb6mWna1CmO1_rotf6oMH8HkKYB7KZ4BBzrxlVcA0V-_HCsST5H0Fi4d5lygWoiQLETSJFGp7vEl4hwA-bGttGbNJwY4XSjsSAknGh-tFMInzAdlxl2zS4fbHLOZfcuaknzLG23IJ0kkka6uF4JBxVo3xNL9bcr9rsG2LRUIV62wQfwsMPoPm5RhX3ERQtLA0AoFoH_NgGTH_UErTvmq95VCXiNbQ2QcYlKs3OXNhCwBHsDMqQMkSFzFwCKGlkPlAFfSnWv80a2eOuC7o6ECUTskG58qyh29810N96Xb6sSd8rPUxSN0wqFD-biAVHmSN1k-ntf8iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d2e0e1e0.mp4?token=NTc8jvfn4C6Vrb6mWna1CmO1_rotf6oMH8HkKYB7KZ4BBzrxlVcA0V-_HCsST5H0Fi4d5lygWoiQLETSJFGp7vEl4hwA-bGttGbNJwY4XSjsSAknGh-tFMInzAdlxl2zS4fbHLOZfcuaknzLG23IJ0kkka6uF4JBxVo3xNL9bcr9rsG2LRUIV62wQfwsMPoPm5RhX3ERQtLA0AoFoH_NgGTH_UErTvmq95VCXiNbQ2QcYlKs3OXNhCwBHsDMqQMkSFzFwCKGlkPlAFfSnWv80a2eOuC7o6ECUTskG58qyh29810N96Xb6sSd8rPUxSN0wqFD-biAVHmSN1k-ntf8iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب چین
😂
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/11158" target="_blank">📅 20:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11157">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bf96fe02c.mp4?token=cQmqRKmYVcpmd67zVuJFEbds8vTM59Y48CPtZ6eedt-hqc6AWLjbifJUBeJi2fQWNqs2PlWW3vi8nJfQboLCGiMqEOPxhnxZxxkqAJJfC935W3dTiPqu8MS48DGhU8fGztANo6tyTf7JSdL8BxaySLinxzVg30dnRiRHZlBfVybg5bBgnkR2b1jc7GN7RZkhGCiOaKUC7Xi4B0uPhOQQx2mzVQ66c678EF5DRoCqGAP5FEKseFq__sSAbl4xUa1Aq8gbCxFciHPUboSAMSG6ylaT7q01eNosmTRGaCuJyvyNCVjWIee_VNZv5Y5MyGqy9mgyHK6sSBfP6wMyjCnepQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bf96fe02c.mp4?token=cQmqRKmYVcpmd67zVuJFEbds8vTM59Y48CPtZ6eedt-hqc6AWLjbifJUBeJi2fQWNqs2PlWW3vi8nJfQboLCGiMqEOPxhnxZxxkqAJJfC935W3dTiPqu8MS48DGhU8fGztANo6tyTf7JSdL8BxaySLinxzVg30dnRiRHZlBfVybg5bBgnkR2b1jc7GN7RZkhGCiOaKUC7Xi4B0uPhOQQx2mzVQ66c678EF5DRoCqGAP5FEKseFq__sSAbl4xUa1Aq8gbCxFciHPUboSAMSG6ylaT7q01eNosmTRGaCuJyvyNCVjWIee_VNZv5Y5MyGqy9mgyHK6sSBfP6wMyjCnepQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همراهان ترامپ در چین
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/11157" target="_blank">📅 20:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11156">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سد عباس چپقچی وارد هند شد
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/11156" target="_blank">📅 19:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11155">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">احسان افرشته، به اتهام جاسوسی و همکاری اطلاعاتی با موساد اعدام شد به گفته رژیم وی چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند بیش از ۳۰۰ پیام بین آنها رد و بدل شده است. افرشته در ابتدا در پوشش راننده تاکسی…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/withyashar/11155" target="_blank">📅 18:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11154">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d224c82b7.mp4?token=WRCzjAimrpgONLygF_cvG4zhK7WCXMsG3vDRlzQuPBY_tbPLXCQObk3i3QjilV1zGwx94Vg7rJc0tVMIPIdrW_Iu6VMbHfioTznNF7SZ6EeFY1EeoYlVbNYSuGcJ9wC9M5XwqKU5iiGeWU3PnWDwr4Fq6xIh-vU5lGRubT5KPhdROffhxBfdmND7ViNsgiHnM9EW7gwB-tbbWnChD7aPMOs_AJhlURFuvd4G2kGDiwqmB9Yqs5wzGCclm_jF1LMmkAs7sJ7anfrhe4bVVPBvYzPELr5_XlURjb6sFzB7chGd4DV_vx1ME3FAlPNZ9ghv_DA9IO-E36mLjHOVnC_dMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d224c82b7.mp4?token=WRCzjAimrpgONLygF_cvG4zhK7WCXMsG3vDRlzQuPBY_tbPLXCQObk3i3QjilV1zGwx94Vg7rJc0tVMIPIdrW_Iu6VMbHfioTznNF7SZ6EeFY1EeoYlVbNYSuGcJ9wC9M5XwqKU5iiGeWU3PnWDwr4Fq6xIh-vU5lGRubT5KPhdROffhxBfdmND7ViNsgiHnM9EW7gwB-tbbWnChD7aPMOs_AJhlURFuvd4G2kGDiwqmB9Yqs5wzGCclm_jF1LMmkAs7sJ7anfrhe4bVVPBvYzPELr5_XlURjb6sFzB7chGd4DV_vx1ME3FAlPNZ9ghv_DA9IO-E36mLjHOVnC_dMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌حرکت ایستادن کامل افسر چینی هنگام عبور هواپیمای رئیس جمهور آمریکا (ایر فورس وان) در چند متری او، توجه بسیاری از رسانه‌ها را به خود جلب کرد
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/11154" target="_blank">📅 17:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11153">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک مقام ارشد کُرد در گفتگو با کانال۱۳ اسرائیل:
در واقع خود پرزیدنت ترامپ مانع از طرح اقدام ما علیه حکومت ایران شد و اتهامات او در مورد ضبط سلاح های معترضین در ایران توسط کُردها، ناعادلانه و غیرمنطقی است
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/11153" target="_blank">📅 17:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11152">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اتاق جنگ با شما : گزارش از جنگنده های ناشناس پرواز در ارتفاع پایین در‌ ارومیه و انفجار در شیراز
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/11152" target="_blank">📅 17:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11151">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایال زامیر ، رئیس ستاد ارتش اسرائیل:
نبرد تمام نشده است، ارتش اسرائیل آماده از سرگیری نبرد در صورت نیاز از کرانه باختری تا تهران است
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/11151" target="_blank">📅 17:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11150">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH02efNYZXF5gHa4Usa_Qyp4XOOTgJ7SkXWMcDQ-mkMzKSVprCrF5QJxVV_aEony0tC7502VYL0JxwvVEoQk4H9RywYRT8v3qcYoH7sniXrEMWKI53F2lT_-W7mL1HHglJ3bCc0QcX5wUQEnfnnUD5pfGYm2oDqbZ4RJS8S-Cm1v1w3dXLLCvUmZPJu_iiSlgg-q2R4-tOKnak4DqzROApYI6vy4GBmlTkdDSLOP62cjjQBhoJxZu8aLkT1jqHHthR8q93lXMU53cxpLITefQDXFe_4twXJNITEHZWmDWqKCJ5u23Ird59Ow-6sUlSUVLLI2U5z6AdkMonehL56i4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه های ترامپ با حاکم چین به این ترتیبه : مراسم استقبال تو تالار بزرگ خلق
چهارشنبه رسیدن به پکن ، استقرار و استراحت
پنج شنبه ۱۴ مه
- ملاقات با شی - ضیافت دولتی با شی
جمعه تاریخ ۱۵ مه
- جلسه عکس با شی- چای با شی
- ناهار با شی و حرکت از پکن به آمریکا،
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/11150" target="_blank">📅 16:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11149">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5924e9f0d5.mp4?token=aTG5RYHXqyxmUVp2Pdt897MduAOq3i7LR1-a_H8wOcyXWcDwOJ8Bh-LofHFPcqYPQwIZokwkikndmoW3bvo1wjG1SEI2-Hk7z_R_jqJdsUWKx9kwihGH16RszZDrxs9FXgoMuCjHMd9nk53rn5Pmn6O9vkpe4L__lnHV4tSoAaaguF47sEbLtTsljivFnAFN8ADy5OFDK2glTUvhI0V7PereE32xbIinwPsDUHY9KAWonqXyLR8wRBSliwOvhrsjxAbf8urHmizyQJvbKeTCEzi0EBasUy1blK1ZrqCGSxJotjmCg3xpOqwGEL6Jh7boPC4Rp7g8SWOA7TgWgZsSrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5924e9f0d5.mp4?token=aTG5RYHXqyxmUVp2Pdt897MduAOq3i7LR1-a_H8wOcyXWcDwOJ8Bh-LofHFPcqYPQwIZokwkikndmoW3bvo1wjG1SEI2-Hk7z_R_jqJdsUWKx9kwihGH16RszZDrxs9FXgoMuCjHMd9nk53rn5Pmn6O9vkpe4L__lnHV4tSoAaaguF47sEbLtTsljivFnAFN8ADy5OFDK2glTUvhI0V7PereE32xbIinwPsDUHY9KAWonqXyLR8wRBSliwOvhrsjxAbf8urHmizyQJvbKeTCEzi0EBasUy1blK1ZrqCGSxJotjmCg3xpOqwGEL6Jh7boPC4Rp7g8SWOA7TgWgZsSrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ورود ترامپ به چین-پکن همراه ایلان ماسک و همراهان
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/11149" target="_blank">📅 16:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11148">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بلومبرگ: صادرات نفت ایران از جزیره خارک برای اولین بار از زمان شروع جنگ متوقف شده است و تصاویر ماهواره‌ای نشان می‌دهد که مخازن ذخیره‌سازی نفت تقریباً به ظرفیت کامل خود رسیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/11148" target="_blank">📅 15:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11147">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDp85xdhEDXq5wB10-H2ukXWGCBuK7UvJClliKe6oLPs1z2skhCgt19WqSrNpXEbYcA7OEEG-RtDrbi-QTjwNKHHZ318qkvSLpsXIbQfpPZMkeLNHhICzQrdALSTGCyk_ks491gO4UxoW48hYb6KseDLITfCpjP8tb_fvDVnGsleObxnON30lsV-MzfbJ1AiUQmjGz2QOOUu4R8-W04ZPcgfm9GpVE73lJ-RKP1Y6SB8Ai5OR1zc03O96HGuIOCRKTypzghrpDQlnfFWkWGLacJ8iJ4Ljt3bXAZ48h_AW9bJgYHhL8C1-OEUcOVYf6bVJIGsDfaqqHeBu0R7Tv4Tlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به پکن رسید
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/11147" target="_blank">📅 15:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11146">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0Nf2vw4nHtFaRYZArWBX5fQPpBllv99uprP1J8SIagb2UjM7Lnv3iGZizfZ53nyQX1nyiBamRYXluPeJyCEPCqnFD2uhyAplXn46rWcqjqShl_HLyTlBw1algUJiKRcb2Tk9Qgd2ZEXqrF1yDUhZHhNp-yaZvd3uoAI_1QerG6msCc-uTyP7xl2TolubYx-kD2VgFvPvvBI_MFdkPeZuJrHAMykkFLA5BL1deMk1y5sb5A_meiuvNO5U7nsDQ3DQktQp2SJ18UU7U1istKlrId25TAxzw5WaCjewYfuDwkzkoptbsi28tgVO7M-Gy8qIbnlsab8MFa9I0G3DHXDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امانوئل مکرون ظاهراً برای چندین ماه با بازیگر ایرانی گلشیفته فراهانی رابطه‌ای داشته که شامل «پیام‌هایی بوده که گفته می‌شود تا حد زیادی پیش رفته بودند». این موضوع ظاهراً باعث تنش در زندگی مشترک زوج ریاست‌جمهوری فرانسه شده …گفته می‌شود سیلی‌ای که سال گذشته بریژیت به امانوئل مکرون زد، به پیامی مربوط بوده که در تلفن رئیس‌جمهور پیدا شده بود. بانوی اول فرانسه ظاهراً گفت‌وگویی با
یک بازیگر ایرانی دیده که در آن، امانوئل مکرون نوشته بوده: «تو خیلی زیبا هستی.
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/11146" target="_blank">📅 15:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11145">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این پیری رئیس باند medea benjamin از باند نایاک و از مهره های ماله کش ظریف هستش شخصی هم که به سخنان شاهزاده حمله کرده اسمش «بیتا» هست  … اطلاعات تکمیلی به زودی … @withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11145" target="_blank">📅 15:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11144">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B37wSO7S8XJvHaxDO2CyMV8JFvUXQZoynRxPnvhlG37KcA5cxH3gJFmtDrDagnDvV6Qh3JoBiwqHeXfyi0kMjRcFthQX52FGda2lZjG_G1w53TiyJwr5HzUJ-2rAHcQfqlmEpZXi6hhVkg_4BGs2Hpk6289qojKN8EO20PMFfqAavbfTrq3rttNFocAQvDD6xvP-NxnhOY_bNaamJH4nEd3p_u9TTJBSCX3Xd-5iwl0JsZ1kxl7Fq4QDmq7s6rZax_8vXYLu9zb9RPobiGd33uWybZqDjrMOveUjcCVHiM2-7IIBXyvL-4gIxxl9n5hrFmGmK9bMm9Q6Bj-KzaJy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پیری رئیس باند medea benjamin از باند نایاک و از مهره های ماله کش ظریف هستش شخصی هم که به سخنان شاهزاده حمله کرده اسمش «بیتا» هست  … اطلاعات تکمیلی به زودی …
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/11144" target="_blank">📅 15:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11142">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/691ecb2a9a.mp4?token=nAVR_ISsnFWa_xeiPu60IGlhJnApXeYy0JFLvA5e9azyXb1mpaHL15JsIIIe5XwTqto3u_FBEjzJGumX-hWLBWdJXQVDiuNpIIQQFBKPJP949g4lD9mXsbF0NExr6LORpxcvzX1FlyW8xQeHGYtaemsrqmW1pa6yEO5U6VlKTcT6GyIeFEOotnBjBJGmtH8SKzj1hFyoBtFHfw2B3qqBSpV1ohmqFsioSWudJ3F-k50Fa7-frN5f5vsF2EP0GC2zknczk4frhPptp0UXelhimIM3bw9gTjMHf7LBTaH9gaVY0QRpaNtXob-Eg2rUDCe9AjqQIm1qXMEWKhubxv4pVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/691ecb2a9a.mp4?token=nAVR_ISsnFWa_xeiPu60IGlhJnApXeYy0JFLvA5e9azyXb1mpaHL15JsIIIe5XwTqto3u_FBEjzJGumX-hWLBWdJXQVDiuNpIIQQFBKPJP949g4lD9mXsbF0NExr6LORpxcvzX1FlyW8xQeHGYtaemsrqmW1pa6yEO5U6VlKTcT6GyIeFEOotnBjBJGmtH8SKzj1hFyoBtFHfw2B3qqBSpV1ohmqFsioSWudJ3F-k50Fa7-frN5f5vsF2EP0GC2zknczk4frhPptp0UXelhimIM3bw9gTjMHf7LBTaH9gaVY0QRpaNtXob-Eg2rUDCe9AjqQIm1qXMEWKhubxv4pVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیروز گروه «کد پینک» به سخنرانی شاهزاده رضا پهلوی و وزیر جنگ هگست
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/11142" target="_blank">📅 15:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11141">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN9FvDjLWukIt5AhQZogxCQe9Ph0D2xxCgMzidMhqIsf03sRheBshA8voXPu5M4yWUqJyyTdLhfw0LrafSYgWVEPVluP3GPxlIcIk7ql_WxMIeCjcZGHb3GL82RNlUzFUIstiSHy6sRsOUlA-jApHu5-SYaLTj_SLRrPU8ffmT21v21C7AMXjHC7CXzOVNG6yxCzApIhrXhjcBtfVbzzTIaYVOZrDX1B_e8pnTb6Jf53SlZMqLra1pmFl_M-eyVdyebSC26nUwrY0OthkRmpvcPA8r88C98U90dDH0dpdjaGqMcvZ_UwVFLGh2ZbmLrUB-nnU1-Dl5aZYReCljZmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گروهی اومده بنام « کد پینگ » سر دسته شونم این پیری هست
Medea Bejamin
حمله کردن به سخنرانی شاهزاده و وزیر جنگ
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/11141" target="_blank">📅 14:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11140">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایتالیا اعلام کرد که کشتی‌های مین‌روب خود را به نزدیکی آب‌های خلیج فارس اعزام خواهند کرد ولی شروع مین‌روبی‌ ، به دستیابی به یک آتش‌بس دائم و پایدار بستگی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/11140" target="_blank">📅 14:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11139">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلام یاشار جان خسته نباشی
❤️
تو یه اتفاق جالب با همکلاسیم نشسته بودیم تو سلف دانشگاه غذا میخوردیم،دوستم پرسید اخبار چک میکنی گفتم اره،بعد نشون هم دادیم گوشیامونو
😅
چند روز پیش کانالتو براش فرستادم،البته از اینستا میشناختت ولی کانالتو نداشت،و پیجتم دنبال نمیکرد…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11139" target="_blank">📅 14:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11138">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2Dh05-0PFQ7XHX4t3CVaalw1-uwlX7sUetu93D3722dCCeSWJn8CbWD8f2D78MVWYgD3YEE4urMALktBLsBbQkixARLOKHFwwYbffgZUpW_IsQtOjUas81oIa81WoME_Tk8wOxFoWzLgPuh4vodltb9xuCO_aSYGujYg0czHADbQBPFNgpqqZG8-qK4QAqgRNKz4jftx-aHh0aQ8UyN-qd-o-HaVhdaXby8kxHp5satxmm2YR4MLgXwkrg-b8W6lysh2ZWzV_Hze9cu3Fhme2vveebzKlumtcU_VeFfa0YHQssgtL1xxIcLu4bXwpKL-MmCaS8t02WiLSpNazvlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام یاشار جان خسته نباشی
❤️
تو یه اتفاق جالب با همکلاسیم نشسته بودیم تو سلف دانشگاه غذا میخوردیم،دوستم پرسید اخبار چک میکنی گفتم اره،بعد نشون هم دادیم گوشیامونو
😅
چند روز پیش کانالتو براش فرستادم،البته از اینستا میشناختت ولی کانالتو نداشت،و پیجتم دنبال نمیکرد فقط چندبار دیده بود.
دوستم‌گفت بهت بگم‌ همش اخبارو چک میکنیم و منتظر اخبار بعدی میمونیم
😅</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/11138" target="_blank">📅 14:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11137">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adfgznRVh8JTey0GeNnSMX0jgWetN9Ew9wbCmC5nIV92Q-pS5XUAFTnZ35c1xNmA83ni5SanvjqSn7XB_m4gA4DWIm3QbZxdISQHdHCra5AwzD-Puc5PJv7OxjpM47HaCFM-Pi8OH0JCopSzTj0vAby6U4q4fQfbTbLMwwbXQ_LChHsmWE2xPQnDj5gnKpmJW5yyhlj6RSnL94QgYlDF0ckWMQhVDlCnmVG4bFjlJ-Vg2AzoNdBLZlGLpcN5EZ_9-EQ1rsruLCNZZWQC7l2uUIPMyO_dLhhZUmULfVxxVGax3InSb3HExx-KMP2cLzmE7J3eI42rBp3dbuGX99tM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین «نمایندگی رسمی مجاز اپل» یا Apple Authorized Reseller در افغانستان افتتاح شد
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11137" target="_blank">📅 14:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11136">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیو دی‌کمپ، روزنامه نگار آمریکایی: شاید ظرف یک هفته آینده شاهد بازگشت به عملیات نظامی بزرگ آمریکا علیه ایران باشیم
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/11136" target="_blank">📅 13:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11135">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیویورک تایمز: قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید ۶۰ روزه حمله به ایران شروع کند @withyashar</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/withyashar/11135" target="_blank">📅 13:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11134">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سخنگوی وزارت خارجه: ما عملاً در یک آتش‌بس اسمی قرار داریم، اما طبق حقوق بین‌الملل، خودِ محاصره یک اقدام جنگی محسوب می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/withyashar/11134" target="_blank">📅 12:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11133">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کانال 13 اسرائیل:
نتانیاهو امشب جلسه امنیتی ویژه در مورد ایران برگزار خواهد کر‌د
@withyashar</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11133" target="_blank">📅 12:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11132">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYashar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN8lUyfNw-FRTapOyeRVuhs0tDQZ-RVqJOX03BhXhXb-lIuIQiv-xSYqjUr1PdwG4tDzrBdJ2alvaaRs999IFJN9R4fl9aE7Tp3lyLvx8fngm1H2yCl5bFDRbWe10KhHOWzcWIRhb-QbhFHGZGztxT2ESfapKTsRGn_pcEmm2IgAD7OHI3p7ottKsdjz98qyyAaL5teI0z5GjDO71KVPf-loxQTOiKHOTXbavMtAoS_s4H1Ezz6PeqE8NM8N0S43YrrIH5h4clBs4OJCOevjfeV_C4wi86zIcccGd49-cEVrSBKKvq1DJa7HMYJ_JlK31mjWcPIo9ObjjAkTWTYQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/11132" target="_blank">📅 12:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11131">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فدراسیون فوتبال: امشب مراسم بدرقه تیم ملی فوتبال به جام جهانی، در میان تجمع حامیان حکومت در میدان انقلاب تهران برگزار می‌شود و قرار است در این مراسم از پیراهن تیم نیز رونمایی شود.
@withyashar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/11131" target="_blank">📅 12:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11130">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عبور ابرنفتکش چینی از تنگه هرمز همزمان با سفر ترامپ به این کشور
داده‌های مارین ترافیک نشان می‌دهد که کشتی
یوان هوآ هو
صبح چهارشنبه در حال حرکت به سمت شرق از طریق تنگه دیده شده است.
برخی بر این باور هستند که عبور این کشتی نوعی اقدام مبتنی بر حسن نیت از سوی ترامپ برای جلب نظر شی جین پینگ است.
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11130" target="_blank">📅 12:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11129">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یک مقام ارشد سابق موساد: ایران ممکن است ظرف چند ماه از نظر اقتصادی سقوط کند اگر محاصره ادامه یابد
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11129" target="_blank">📅 12:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11128">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11128" target="_blank">📅 12:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11127">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پروژه هارپ یه پروژه برای تغییر در آب و هوا بود طوفان میتونست درست کنه ولی زلزله نظر اکثر کارشناسان بر این بوده که امکانشرو نداشته و فقط تغیید در لایه های جو بوده به هر حال دهه نود ساخته شد و ۲۰۱۴ امریکا گفت پروژه کنسل شده ، ولی تئوری توطئه زیاد هست درباره این پروژه
@withyashar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/11127" target="_blank">📅 12:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11126">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-text">سلام مرسی از همه زحمت هات
زلزله میتونه پروژه هارپ باشه؟</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/11126" target="_blank">📅 12:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11125">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">درود یاشار جان، خسته نباشی. مرسی ک تحمل این روزای سخت رو با حضورت و زحمتی ک میکشی، برامون قابل تحمل میکنی. داداش میشه توضیح بدی ک چرا اکثر مواقع حساس کشور، ایران میره روی ویبره؟! قبل از خشم حماسی هم این اتفاق میفتاد، طلوع شیران هم همینطور یا مثلا چند سال قبل…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/11125" target="_blank">📅 12:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11124">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSadegh</strong></div>
<div class="tg-text">درود یاشار جان، خسته نباشی.
مرسی ک تحمل این روزای سخت رو با حضورت و زحمتی ک میکشی، برامون قابل تحمل میکنی.
داداش میشه توضیح بدی ک چرا اکثر مواقع حساس کشور، ایران میره روی ویبره؟!
قبل از خشم حماسی هم این اتفاق میفتاد، طلوع شیران هم همینطور یا مثلا چند سال قبل ۴۰۱ بود فک کنم.
بنظرت میتونه چیزی بجز گسل و دلایل طبیعی باشه؟</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/11124" target="_blank">📅 12:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11123">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw78CKgz9qQ8POxpFq1fAsbBErYUnSA5kjT1ckt60h6DtiLI0wqQfiO7hJFrb05WLUwCfnahTjTyjETrRAKWWOuoMua-WQl4RT88l75ranQbWQi3jikowGOSYy-p-yU3SHfq8b1E0BTqTdYvyrTvdnoIXM5w5jhtRm9s4vF2XxMGiTryTCvUKK1drGp8WPYSJMlACTvrwTGRYSTCfaE0hHKO_a5T6fNgaYYqxszgPbbL0vrQyy-hO8AZNJ97bh3WNCZjcUZIrirXjddaEPyrqWMuJRTfaK_V_9Jl983Fvr09isPdV83ZZHNRFsC-a-WjAGYE_N-c2x6kO-T5Sg_yog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهندس ارتباطات حزب‌الله که متخصص فیبرنوری بوده و پشت توسعه پهپادهای انفجاری این سازمان بود،   توسط ارتش اسرائیل به هلاکت رسید.
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11123" target="_blank">📅 12:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11122">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نیویورک تایمز: قصد ترامپ از تغییر نام عملیات «خشم حماسی» به «چکش سنگین» این است که یک عملیات جدید ۶۰ روزه حمله به ایران شروع کند
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/11122" target="_blank">📅 11:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11121">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش مرکز ژئوفیزیک از شدت ۹ زمین‌لرزه بالای ۲.۵ ریشتر در پردیس از روز گذشته تاکنون
ساعت ۲۰:۴۱ — بزرگی ۳.۴ ریشتر
ساعت ۲۳:۴۶ — بزرگی ۴.۶ ریشتر
ساعت ۲۳:۵۰ — بزرگی ۲.۶ ریشتر
ساعت ۰۰:۲۰ — بزرگی ۲.۶ ریشتر
ساعت ۰۰:۲۶ — بزرگی ۴ ریشتر
ساعت ۰۰:۳۲ — بزرگی ۳.۴ ریشتر
ساعت ۰۰:۵۴ — بزرگی ۲.۶ ریشتر
ساعت ۰۳:۲۹ — بزرگی ۳.۱ ریشتر
ساعت ۰۵:۵۷ — بزرگی ۳.۳ ریشتر
@withyashar</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/11121" target="_blank">📅 11:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11120">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">غضنفری:شواهد و قرائن نشان می‌دهد که آمریکا و اسرائیل قصد انجام یک عملیات گسترده برای تصرف برخی از جزایر جنوب را دارند
@withyashar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/11120" target="_blank">📅 11:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11119">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f62701b581.mp4?token=rsCjudOPDIWZEXDNDVnei1chk4Y6A2ckcjzOUZag4ExFsyBCdL5FAZDFA4C5CTkrnAaBhTBN-zpPh8qflAJTxnJ_HZRnBGMH79lCB8G5ujWg4F66Yiq_FxfE29Y28hoUQDZ1IJ6Mnd8YThSZMAXXWtJ2pYS28TWTiQiV5zERKGABChfxZ_lrRlsYZviyrN4KpO5kW6EPWOYDg8YMhVbCW8aUFsDenGTEzOsKXyG26Mgt3F5InJTP-INciMEkAQNrinssOpEMjC8q0K0zbc0DJLdiVAg6krEaU70TciEWfiXxZ5D_DeoymmduHRD12YH0SgpMFqFoPgdvErfedtJpwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f62701b581.mp4?token=rsCjudOPDIWZEXDNDVnei1chk4Y6A2ckcjzOUZag4ExFsyBCdL5FAZDFA4C5CTkrnAaBhTBN-zpPh8qflAJTxnJ_HZRnBGMH79lCB8G5ujWg4F66Yiq_FxfE29Y28hoUQDZ1IJ6Mnd8YThSZMAXXWtJ2pYS28TWTiQiV5zERKGABChfxZ_lrRlsYZviyrN4KpO5kW6EPWOYDg8YMhVbCW8aUFsDenGTEzOsKXyG26Mgt3F5InJTP-INciMEkAQNrinssOpEMjC8q0K0zbc0DJLdiVAg6krEaU70TciEWfiXxZ5D_DeoymmduHRD12YH0SgpMFqFoPgdvErfedtJpwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور 53 جنگنده F-16 آمریکایی در پایگاه شاهزاده سلطان عربستان  هواپیما جاسوسی آواکس هم که دیشب نشون دادم از این پایگاه نظامی بلند شده بود
@withyashar</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/11119" target="_blank">📅 11:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11118">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">احسان افرشته، به اتهام جاسوسی و همکاری اطلاعاتی با موساد اعدام شد به گفته رژیم وی چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند بیش از ۳۰۰ پیام بین آنها رد و بدل شده است. افرشته در ابتدا در پوشش راننده تاکسی…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/11118" target="_blank">📅 11:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11116">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgbb-99Mptg-oKSLlxnLBu2INwGxrjTwops0N45Ez599qV1VmCCrgiSxAoLFJAoO8QTja6pC4hH49WVOu2E1trH5Js_iN_OaGxBaqAkDMCBJAyJfoZTpziVDf7ZjEbmMgFyOgPexHDOnW9fchziWbpFUZ6LZW8N2vw1Ceqydi7ygZtlKk9N22Qjo6apkcefzv_GMWeq749GxPdRoOauN4NaqmWcCZGxXUW2DlxekYre4-WJfYnr3aZzldlzg8DO9QyA5IyWohSftN8BwaHvJe5voCsEve5i3N51P1klJ8mvwtd7-BT9pZSrhTI8UzOSKw1TG8U8Z5iBafSuQV1Kq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس وایرال شده مارک روبیو در هواپیمای ایرفورس وان که همون ست گرمکن مادارو را پوشیده. نکته ای که کسی به آن توجه نکرده کفشهایش است که مارک آدیداس هست.
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/11116" target="_blank">📅 11:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11114">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZmrVnZX8mTAY4IF5bNjFTrz60mDn2hyQzZJywIDEDqxZi1XzsVGEEj00nBqCH8w14FwlNRRny_3jpIPP_wOlvTxQ0CMFgomRIcx6CVP-URj3ijhmyKslpeIPPzjx7b8J55QHRTeadt6gClxAKgfvpciSNMTqxHIJI8S-wsYQgjcP3urXoWNjssDOI_uCac8eQ-r1O-kBlx4USL8wHZ07REb7Th87L94EQJzbHNp57zc9VQz1IVS5ZGlP_H2w7UzJ36sJj06wKd176K4eTIVUXkydPgoeX8JiZD2t7lfflkqwM6ux1dA_QhjPF-WClezk7jsA_g8IGEhAMfcwB5Jwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان افرشته، به اتهام جاسوسی و همکاری اطلاعاتی با موساد اعدام شد به گفته رژیم وی چند مرحله تماس از طریق پیام‌رسان‌ها داشته و در ادامه از طریق پست الکترونیک باهم در ارتباط بوده‌اند بیش از ۳۰۰ پیام بین آنها رد و بدل شده است. افرشته در ابتدا در پوشش راننده تاکسی اینترنتی دستورات افسران موساد را اجرا می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/11114" target="_blank">📅 10:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg_2I-hRhXBntOOFPFRB7BRS2Hq-462UuozCb3axfXwGda9mz1YywC_bSyuty5gDxdt6qhQTb8V3AmWjh4cfHS0AXR5Tas5W6p3Niq2LgmDKPNSP7tKrKqELJbQjaa5AwxsD4fwt2kNurOy4hLlS7IGDPZ0fdsPJ8ppeCLhVGQyRdoqiGaxfJSqgnoAHpTcE-jsz51VE9YxxAMv-p5UBwj54jrQ_4oEl8A1Ki9J7jM43QAw3Ic213kc6k77nxDXBfJOpnPt1lFUAnpMrv3jRBPUU_P1xU000TRrf-J2LaeJNu9aJuwG7os89KNx7N-uQrh-q5Wc5RKkrl94bAoo5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای نشان می‌دهد که یک هواپیمای باری جمهوری اسلامی مدل C-130 در پایگاه‌ هوایی نور خان پاکستان پناه گرفته است
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/11112" target="_blank">📅 10:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11111">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الجزیره: منابع دیپلماتیک می‌گویند که ۱۱۲ کشور هم‌اکنون از پیش‌نویس قطعنامه پیشنهادی آمریکا به شورای امنیت سازمان ملل درباره تنگه هرمز حمایت می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/11111" target="_blank">📅 09:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11110">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کیهان: اگر مذاکره کنیم جنگ می‌شود؛ مذاکره نکنیم جنگ نمی‌شود
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11110" target="_blank">📅 09:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11109">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ویزای ۵ ستاره عراق برای جام جهانی رد شد!
آمریکا در تازه‌ترین اقدام خود در آستانه جام‌جهانی ۲۰۲۶ ویزای ۵ بازیکن کلیدی تیم ملی عراق از جمله علی الحمادی (ستاره لوتون تاون)، مهند علی و حیدر عبدالکریم را رد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/11109" target="_blank">📅 09:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11108">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ در تروث : شبکه سی‌ان‌بی‌سی به‌اشتباه گزارش داد که جنسن هوانگِ بزرگ از شرکت انویدیا به گردهمایی شگفت‌انگیز بزرگ‌ترین زنان و مردان دنیای تجارت که با افتخار راهی چین هستند دعوت نشده است. در حقیقت، جنسن همین حالا در هواپیمای ریاست‌جمهوری آمریکا حضور دارد و مگر اینکه من از او بخواهم آنجا را ترک کند که بسیار بعید است گزارش سی‌ان‌بی‌سی اشتباه است یا همان‌طور که در سیاست می‌گویند: اخبار جعلی!
مایه افتخار است که جنسن، ایلان ماسک ، تیم کوک، لری فینک، استیون شوارتزمن، کلی اورتبرگ از بوئینگ، برایان سایکس از کارگیل، جین فریزر از سیتی، لری کالپ از جی‌ای ایرواسپیس، دیوید سولومون از گلدمن ساکس، سانجای مهروترا از مایکرون، کریستیانو آمون از کوالکام و بسیاری دیگر، در این سفر به کشور بزرگ چین همراه هستند؛ جایی که من از رئیس‌جمهور شی، رهبری با جایگاهی برجسته و استثنایی، خواهم خواست که چین را «بازتر» کند تا این افراد درخشان بتوانند توانایی‌های خارق‌العاده خود را به کار بگیرند و به جمهوری خلق چین کمک کنند به سطحی حتی بالاتر برسد!
در واقع، قول می‌دهم وقتی تا چند ساعت دیگر کنار هم باشیم، این نخستین درخواست من خواهد بود. هرگز ایده‌ای ندیده یا نشنیده‌ام که برای کشورهای فوق‌العاده ما از این سودمندتر باشد!
@withyashar</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/11108" target="_blank">📅 07:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11107">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3i69YEoe57ojV9nPcOLCvC-p1lcbtUY7UeZckCcR30e5onGEl9FCObTuXWOVb5-UN0PWT4UiHhkPen-M6GNZDgTLhJ2Fx1sI3AdLaQ-M2OnJH5PBuulgeKE_HHfGItWhaMMNfZdxOFmsw2TSdZQUMcFbYO4wVlAfQgmrEh8c4s2PjGkOniqrFhiZ-1CcRLrofatBPJTwHe4ldYBIZSxNtAT9ZVNqb2DNfmP0Ja0Gnas5Yyk69Sts413F3SG466Cdsv9L4GSzkseZe28DAokjoS3kmB1KEFUCFr90oAbz1HtrsOy9UsvWpyFaIH5xsX2d4yY0NmijpAaiduB4oSrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث پستی گزاشته که ونزوئلا رو به عنوان ایالت ۵١ ام آمریکا نشون میده
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/11107" target="_blank">📅 07:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11106">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نمیتونن از قصد ی جوری پس لرزه اینجاد کنن که نفهمن تست اتمه؟</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/11106" target="_blank">📅 01:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11105">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجان فدای میهن</strong></div>
<div class="tg-text">نمیتونن از قصد ی جوری پس لرزه اینجاد کنن که نفهمن تست اتمه؟</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/11105" target="_blank">📅 01:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11104">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش مقدماتی زمین‌لرزه  بزرگی: ۴.۶ ریشتر  محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس  تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07  عمق زمین‌لرزه: 10 کیلومتر   @withyashar همچنین اورژانس تهران اعلام کرده در پی طوفان و باد شدید با سرعت ۵۵…</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/11104" target="_blank">📅 01:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11103">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc26774daf.mp4?token=hanGVzO3rSOxk6O_sAvrRwQoQZHQicx_dUpn-aK9A4NKAVwOgmEssMmeGXYdeyZQW2O5KdxNgU2CewotZLDaLjpvimBld4Klm168MoVi0UFfgSIjcND9OUlvcY6Zagqbm6MqOKAdK9Wje8xBXSp8JMz3ndn_FoNU05v_AkPML9o-cC_YgF12woY2GSh5A0iCJ_3Je3_QFoDVTrfJCFoi61wjVwR38VcobGuwLKvNrl0rFly5a4QseSfhGT0LpGn8gTYpcTBVq7rTc0EHh0Th6RQnjCC0CctVitUNb5Z4yEhitsJ_AgCkpZHKYVodgEjyDiu5F1Ehke_RcPgfmDJmPjDTfIWejT_NcJ4fjS3MKa-A069SsVfy5JA8s32YjaHtIWvAefPUlxte6q8govu1HYP5nfQYQDosJqr06RqdEtS1X2qdNcdrHH2pr_Yi3JpuAfhq4WgWNhk7yGl0sINDJpABbcdvsj-ntoE0Wq0clS7BWbaEL6a01af8YHiR25iaKQa4od-1cT-HtyYtmZpW6N2NkVjavlPzuiZGe4ZXq8D3QJQR2gRoog49I1kPbYGk4I46TkGEfLsW8DHwyiGWtclVxmcbVZyT8tMXM4eXbEo1XeP_abaDVF_SmK8bQIxttcvNsTtsCIvCvxtYnDec8lmgo5RIboP2rP8oey-8Xo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc26774daf.mp4?token=hanGVzO3rSOxk6O_sAvrRwQoQZHQicx_dUpn-aK9A4NKAVwOgmEssMmeGXYdeyZQW2O5KdxNgU2CewotZLDaLjpvimBld4Klm168MoVi0UFfgSIjcND9OUlvcY6Zagqbm6MqOKAdK9Wje8xBXSp8JMz3ndn_FoNU05v_AkPML9o-cC_YgF12woY2GSh5A0iCJ_3Je3_QFoDVTrfJCFoi61wjVwR38VcobGuwLKvNrl0rFly5a4QseSfhGT0LpGn8gTYpcTBVq7rTc0EHh0Th6RQnjCC0CctVitUNb5Z4yEhitsJ_AgCkpZHKYVodgEjyDiu5F1Ehke_RcPgfmDJmPjDTfIWejT_NcJ4fjS3MKa-A069SsVfy5JA8s32YjaHtIWvAefPUlxte6q8govu1HYP5nfQYQDosJqr06RqdEtS1X2qdNcdrHH2pr_Yi3JpuAfhq4WgWNhk7yGl0sINDJpABbcdvsj-ntoE0Wq0clS7BWbaEL6a01af8YHiR25iaKQa4od-1cT-HtyYtmZpW6N2NkVjavlPzuiZGe4ZXq8D3QJQR2gRoog49I1kPbYGk4I46TkGEfLsW8DHwyiGWtclVxmcbVZyT8tMXM4eXbEo1XeP_abaDVF_SmK8bQIxttcvNsTtsCIvCvxtYnDec8lmgo5RIboP2rP8oey-8Xo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بلرزونش ، هواپیمای جاسوسی آواکس و زلزله… حجم کم
@withyashar</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/withyashar/11103" target="_blank">📅 00:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11102">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رویترز: دو تانکر حامل ال‌ان‌جی قطر، به دنبال توافق دوجانبه جداگانه بین اسلام‌آباد و تهران، به سمت پاکستان در حرکت هستند
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/11102" target="_blank">📅 00:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11101">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش مقدماتی زمین‌لرزه
بزرگی: ۴.۶ ریشتر
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
عمق زمین‌لرزه: 10 کیلومتر
@withyashar
همچنین اورژانس تهران اعلام کرده در پی طوفان و باد شدید با سرعت ۵۵ کیلومتر در تهران تاکنون ۱۱ حادثه به این سازمان امدادی گزارش شده است.
سخنگوی اورژانس تهران نوشته تاکنون ۷ مصدوم که ۵ نفر آنها سرپایی درمان شده‌اند، در ماموریت‌های امدادگران ثبت شده‌اند اما ممکن است آمار مصدومان بیشتر شود.
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/11101" target="_blank">📅 00:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11100">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کاور @withyashar</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/11100" target="_blank">📅 00:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11099">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHdOxyVq5TFL3vZqcgGk9wsrTByBfup1pVPFDMvjstiiGwrH64Qj99vUQlhfkCZcdwJXTHTiLIUe0XSQpx3SYmbeq9zXljuAKYQA9gKE-1fCsgKbzGvuXDhXtEjvzsCz7O8L76SdaNfuLfy-JkYw8SqVL5DnuYbK1Bmx-1cQlF9kXPOWm8QVJiwocSc5cYtaDycur2KvL49tKOPDOZkWSMnnGtjVkCadSZ_QGfafxLgNzrHqGIhseAYp9OzKL2d6xlHrxVodtg5nHApp63o_R0lI0VZVyXNarw7L8N0VvfLcAJjTgzG-otIcGcZbxbpUbq3Jr2MR5zaM4as1VR9oJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
وقتی رسانه‌های دروغ‌پراکن می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً نوعی خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آنها دارند به دشمن کمک و همراهی می‌کنند!
تنها کاری که این حرف‌ها می‌کند این است که به ایران امید واهی می‌دهد، در حالی که هیچ امیدی نباید وجود داشته باشد. اینها ترسوهای آمریکایی هستند که علیه کشور خودشان طرفداری می‌کنند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت — اکنون تک‌تک آن‌ها در کف دریا قرار دارند. آنها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان نابود شده، تمام فناوری‌شان از بین رفته، «رهبرانشان» دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلال کنند!
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/11099" target="_blank">📅 23:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11098">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزارت خارجه آمریکا: با چین توافق کرده‌ایم اجازه اعمال عوارض بر عبور کشتی‌ها از تنگه هرمز داده نشود.
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/11098" target="_blank">📅 23:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11097">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اتاق جنگ با یاشار : جابجای‌های غول آسا دو شماره یک «AirForce1» هواپیمای ویژه ریاست جمهوری و «B1 »بمب افکن اسطورهی آمریکا و خبر ویژه از داخل ایران
https://www.instagram.com/reel/DYQCr39RJ4i/?igsh=MThycjJiYWZmbnJ3dA==
کارای اداریش رو انجام بدید تا بعدش بریم برای سوال جوای</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/11097" target="_blank">📅 23:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11096">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhYDo8LgT6OxippuygmAlSZMYu7wExYXxZ1oggFKulyr0Dz-UWMJg00tutN_fpbNzinS6NWhil9mvQVyB9cGLALgkghCEPlrzkiz0qHRyHw5p5JFr-ih49QcIyq-Vky3dACpk5-IkLF0kKd7iBhqzrRM2h8GSlA1a-UevysW_ZrNAe90JXrqGU1eFsZiljYFiWnC3GbNc7vYFjbQETogYFAGYT6Z1iK2lxW_v0bjwvoSEFDDxtlMdKHk-cp10CZsfjwefUhKB6VKLyQ1it9c9W9GIxPBPsgL4v2r2bjBF7iMDoKoJP2hSEin7GbMj6vHTFWg0das9-E1qQCZoeZ_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/11096" target="_blank">📅 23:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11095">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/11095" target="_blank">📅 22:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11094">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd1ee7151.mp4?token=VOsf4GQ8qxym-H0spxqkzH2Gr8sA1p5q0_vf8DxjSHZsLngYc2HoDclaz0K31UX7tfjkXVYxZSWgPDwUQRzAdQZjmZseuuDfzji-_egGLIz0gnOU22mYuOyoWf8YHnBeJhzEsMjifz5VZ7CpXEybcaKqvH7dgZLI6hzY2-rgyrBPIQifcuLzUo-29GjIqfYGiBjr5Jh1aiKd_Gi4M3EmxDFhVg5EcoGghXbaBnz07meqQ_-uu1UQTSkGr9KacW8rG5nlZXookxl3FI0d19JuYdB56YjDCbQzc5MFrQQd5YW_NlxS261TJf4J5FkQEH9tgOgPWiXI3qgL1MBSD82b5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd1ee7151.mp4?token=VOsf4GQ8qxym-H0spxqkzH2Gr8sA1p5q0_vf8DxjSHZsLngYc2HoDclaz0K31UX7tfjkXVYxZSWgPDwUQRzAdQZjmZseuuDfzji-_egGLIz0gnOU22mYuOyoWf8YHnBeJhzEsMjifz5VZ7CpXEybcaKqvH7dgZLI6hzY2-rgyrBPIQifcuLzUo-29GjIqfYGiBjr5Jh1aiKd_Gi4M3EmxDFhVg5EcoGghXbaBnz07meqQ_-uu1UQTSkGr9KacW8rG5nlZXookxl3FI0d19JuYdB56YjDCbQzc5MFrQQd5YW_NlxS261TJf4J5FkQEH9tgOgPWiXI3qgL1MBSD82b5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ سوار ایرفرس وان شد و رفت به سمت چین
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/11094" target="_blank">📅 22:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوباره ترامپ یک خبرنگار دیگرو هم فیتیله پیچ میکنه اعصاب نداره امشب این بازیکن
خبرنگار: تورم الان تو بالاترین سطح خودش توی ۳ سال گذشته هست. آیا سیاست‌های شما کار نمی‌کنن؟
ترامپ: سیاست‌های من به طرز شگفت‌انگیزی کار می‌کنن! اگه به قبل از جنگ برگردین، تورم ۱.۷٪ بود. اگه می‌خوای این دیوانه‌ها سلاح هسته‌ای داشته باشن، پس تو آدم احمقی هستی و من تو رو خیلی خوب می‌شناسم!
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11093" target="_blank">📅 22:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ یک خبرنگار رو به توپ بست
ترامپ: ما یک سالن رقص داریم که هزینه ساختش کمتر از بودجه هست. اینجا ساخته می‌شه. من اندازه‌اش رو دو برابر میکنم چون مشخصه که بهش نیاز داریم.
خبرنگار: هزینه‌ش دو برابر شده
ترامپ: من اندازه‌اش رو دو برابر کردم، آدم احمق! تو آدم باهوشی نیستی
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11092" target="_blank">📅 22:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/11091" target="_blank">📅 21:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11090">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoni Ami</strong></div>
<div class="tg-text">Yashar jan, Chera enghadr faaliat kam shode top Paget? Aghaaaa enghad zahmat mikeshe Like konid</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/11090" target="_blank">📅 21:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11089">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ به سیم آخر زد و برای با ‌چهار هزارم گفت :
من به وضعیت مالی آمریکایی‌ها فکر نمی‌کنم.کلا به هیچ‌کس فکر نمی‌کنم!
فقط به یک چیز فکر می‌کنم: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. همین
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/11089" target="_blank">📅 21:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرنگار: فکر می‌کنید شی جین‌پینگ باید اصلاً در موضوع ایران دخالت کند؟ یا می‌تواند به نوعی کمک کند؟
ترامپ: فکر نمی‌کنم ما نیازی به هیچ کمکی درباره ایران داشته باشیم. ما این موضوع را یک‌طور یا به‌هرحال حل خواهیم کرد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری. تمام ماشین جنگی آن‌ها از بین رفته است
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/11088" target="_blank">📅 21:39 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
