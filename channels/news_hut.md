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
<img src="https://cdn4.telesco.pe/file/IyB3zwg63yVXxj-TvHvl4uTXH648JNkwsWEjyWXL4h4iHNuhSh0qhnvbHwmcjly3aLcKHNp5dSm7s35HJ0W2HUnMz0Rn0l3oftAfWieCAPcZ_4az6EDHp5fJVTjEpAJiTZjR7lazRbuoHe9FvfQez7NbH8SzhhkLPYT6pWUKeHGZif7ZY141EQtjTkcB9F6JQFidq0AF7_ig5CPsExUp1i921XuthlOylNMlaNTTiTx2bbD_66qA0e8ZqzM_cKwa5M0HMHGpi8VDMNaijFLR4XN0uXOsaf3fPqnt9L6JND-mafSBJPZoFWKWReBQxXf_kYwpOcbaaTJ7ZRZs6_nxLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 166K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 01:24:32</div>
<hr>

<div class="tg-post" id="msg-68393">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇸
ترامپ: مسی خیلی خفنه
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/68393" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇺🇸
ترامپ: رونالدو مرد بزرگیه
@News_Hut</div>
<div class="tg-footer">👁️ 314 · <a href="https://t.me/news_hut/68392" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68391">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 312 · <a href="https://t.me/news_hut/68391" target="_blank">📅 01:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68390">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/news_hut/68390" target="_blank">📅 01:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/news_hut/68389" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68388">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=uQ1ces81WBIcPZgUaj6SlbOpMug9G1gnnaOwfoFwtmc3Hp5NJfRhlzXsezKr7uDslJvXfwbH_ihSSp35GUuSvBz_9wmE8LkNhGe8vwuFnWKwrMfYObLhdKIja7QUC62_6bZJME6lh0B2YhL2uPlFkO-I1LlC4WkYWwnT_dkmaNIBvjblbCw1Rbap_FRba98cu8WkOxaEF55ubVQ5YrV-d5UAfmKKvEEY3YePfoM-dxi8h2yIQhcocQoS8MpY9S7xT0h7Vx6drxh3uRLQ5hcF6CQEmA-lFqq2KDOIH_PTU4Lqdk7X1nKjWKeKpZ5t1smmgRzd_jWeAsoe57KsJPTH1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1504ff042f.mp4?token=uQ1ces81WBIcPZgUaj6SlbOpMug9G1gnnaOwfoFwtmc3Hp5NJfRhlzXsezKr7uDslJvXfwbH_ihSSp35GUuSvBz_9wmE8LkNhGe8vwuFnWKwrMfYObLhdKIja7QUC62_6bZJME6lh0B2YhL2uPlFkO-I1LlC4WkYWwnT_dkmaNIBvjblbCw1Rbap_FRba98cu8WkOxaEF55ubVQ5YrV-d5UAfmKKvEEY3YePfoM-dxi8h2yIQhcocQoS8MpY9S7xT0h7Vx6drxh3uRLQ5hcF6CQEmA-lFqq2KDOIH_PTU4Lqdk7X1nKjWKeKpZ5t1smmgRzd_jWeAsoe57KsJPTH1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما ۵ دقیقه بعد از حمله به شهر های مختلف ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/news_hut/68388" target="_blank">📅 01:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
دقایقی قبل آمریکا به نقاطی در داراب حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/news_hut/68387" target="_blank">📅 01:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
فارس:
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی دریایی سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان بوشهر رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/news_hut/68386" target="_blank">📅 01:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=AC2sCGgU5xfdKMlzcc0IOyD4eGJl_qhV1abB0Fk5BvvAKjnIQ1P-PBH7GEko_wlBIDYzyxtpqD1eJh9ZtneMi5uU_DWrpYDc0sqva3hTgVomFqAMep-tcYJnJcszPSJXQm7vtKS0opSeVFfQBl-Ka-oTRJxRNcjGxWypf7hDMPWqL0Y_zbUUigpdRz5XzUM2PSpA5FopQkfkjt-wyV1td2dbAfv5Zee_SaZAvhdW5FmzSxNaixUcPPw8Sz-QOhEA_4ncCQfAD60NfiZPiL5F_Co818qnJTOcRfIRyCCU9MMuhmsUGpA6G1xUxdVzHUampt8TKAx4mrWmP1jjrFJSKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7dd90f1.mp4?token=AC2sCGgU5xfdKMlzcc0IOyD4eGJl_qhV1abB0Fk5BvvAKjnIQ1P-PBH7GEko_wlBIDYzyxtpqD1eJh9ZtneMi5uU_DWrpYDc0sqva3hTgVomFqAMep-tcYJnJcszPSJXQm7vtKS0opSeVFfQBl-Ka-oTRJxRNcjGxWypf7hDMPWqL0Y_zbUUigpdRz5XzUM2PSpA5FopQkfkjt-wyV1td2dbAfv5Zee_SaZAvhdW5FmzSxNaixUcPPw8Sz-QOhEA_4ncCQfAD60NfiZPiL5F_Co818qnJTOcRfIRyCCU9MMuhmsUGpA6G1xUxdVzHUampt8TKAx4mrWmP1jjrFJSKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به لار
@News_Hut</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/news_hut/68385" target="_blank">📅 00:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
معاون استانداری خوزستان:
دقایقی پیش نقاطی در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/68384" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=WYTIv1PmINwJJKYuVGs_MMaPJI95NxSu9Gy-4GIxioEvUYqy5-GY7xZH6hPAxtY58D4WuITVvgB4TcesaenN8zVUAvXGMzFQWLEQprxNFwHCuJ6n7NU9uQcD8VTsaXBjf6TuXgtayucQihdw62d7woxjdyHEE28I55j7X_5JW707mn2FuSG6j0lBm3fmAtE6FdubxCliluhkRQIjs_NSQ9yiKFq7qFAZ1FvgJXMUyqV9PJlWJMWe0Q5JDDeWjxk1J4wqMAzxiUegJSmdFS3ktJx8R9rSBGSTtUBKDEPhBc5Lv44uhlIVqRZZbNxWqcojnHGQdW3A2YZinp41D08uIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=WYTIv1PmINwJJKYuVGs_MMaPJI95NxSu9Gy-4GIxioEvUYqy5-GY7xZH6hPAxtY58D4WuITVvgB4TcesaenN8zVUAvXGMzFQWLEQprxNFwHCuJ6n7NU9uQcD8VTsaXBjf6TuXgtayucQihdw62d7woxjdyHEE28I55j7X_5JW707mn2FuSG6j0lBm3fmAtE6FdubxCliluhkRQIjs_NSQ9yiKFq7qFAZ1FvgJXMUyqV9PJlWJMWe0Q5JDDeWjxk1J4wqMAzxiUegJSmdFS3ktJx8R9rSBGSTtUBKDEPhBc5Lv44uhlIVqRZZbNxWqcojnHGQdW3A2YZinp41D08uIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا به سایت موشکی یزد
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68383" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68382">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ممکنه امشب، سخت‌ترین شب برای جنوب باشه
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68382" target="_blank">📅 00:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68381">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از چندین انفجار در یزد
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68381" target="_blank">📅 00:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68380">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428210a926.mp4?token=TsfEb0QTm9XXAG7Cf_dmf3YYxx6260bMeYsXvKhe89Eo0PykgUC-248Wc9lAhrG9sfGXubCiZAHq6L1_xd5YBD9HKGs9nEciIA3c-3nkw-tdsTRsBq4BdAGPDE_Us1HrJznHGvKLvfVTfJa3XHLrszz4qqMQNXiqtOYZuqU3TT3j5MQKzzEtsrNPNye3U5Z4k_AxUNNd18vXAy-PQrEqRGUk1WYY0K6kx1LWp_K3pwKSKQuHBQRT0UGQANOin9bA312XjyXTrsZ2AVoFe3e4A_RGgKyDHvX43E8JnxTscIDYRfhzGZ-T4Ah4tkxLdZDqwmGDpSa5LWFQ4-vExSQStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428210a926.mp4?token=TsfEb0QTm9XXAG7Cf_dmf3YYxx6260bMeYsXvKhe89Eo0PykgUC-248Wc9lAhrG9sfGXubCiZAHq6L1_xd5YBD9HKGs9nEciIA3c-3nkw-tdsTRsBq4BdAGPDE_Us1HrJznHGvKLvfVTfJa3XHLrszz4qqMQNXiqtOYZuqU3TT3j5MQKzzEtsrNPNye3U5Z4k_AxUNNd18vXAy-PQrEqRGUk1WYY0K6kx1LWp_K3pwKSKQuHBQRT0UGQANOin9bA312XjyXTrsZ2AVoFe3e4A_RGgKyDHvX43E8JnxTscIDYRfhzGZ-T4Ah4tkxLdZDqwmGDpSa5LWFQ4-vExSQStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حمله آمریکا به لارستان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/68380" target="_blank">📅 00:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68379">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
گزارش ها از انفجار در لارستان استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/68379" target="_blank">📅 00:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68378">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
انفجارر
بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68378" target="_blank">📅 23:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68377">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
سیریک و اهواز انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68377" target="_blank">📅 23:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68376">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
قشم رو وحشتناک زدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68376" target="_blank">📅 23:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68375" target="_blank">📅 23:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68374" target="_blank">📅 23:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
انفجار ها در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68373" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioZL8fXf9MwS-K3NRHY7QwXqjFOxyJuEXPWSTbqVtH_h-mOSq30yxS25WYWq3MFiLe0CID52RlTTd8xVeoBcZHejWwkkD7nUkWSA0tOY8rtnMEe3nUDPFNa61DNoO5vTi9LK_8vWt6ZIkBjfGosw-whTFd21xNjCbaaBZZMNms0ucZx9EACCoJQBh2vAlAt9RmyRRzpJb5sJkfJ8EWshTQedXHJZMt4I332CqPRCnnc5abRYNtFN6XCCdq9v_kmDxXOjqnzK7E0s_ZGs8Kz9EHOGfsCsfokIvN4-_oqzinsRoUlgv9seY4KtzlFGLq9FxA51xhE_JDHDJLBo7z830Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
سنتکام امروز ساعت ۳ بعدازظهر (به وقت شرقی) و برای هفتمین شب پیاپی، دور جدیدی از حملات را علیه ایران آغاز کرد. این حملات با هدف تداوم تضعیف توانمندی‌های نظامی ایران و بنا بر دستور فرمانده کل انجام می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68372" target="_blank">📅 23:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
با اعلام سنتکام دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68371" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68370">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68370" target="_blank">📅 23:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HftnfSSMsJg0my09wnU_gWoj7YBKJi9n6gqk6UAlK1HsYH6a8WqcYugE7Vdbah6Br_byWkbzWttbFST7NoFV2Xv3GtFWE1kicBoxVCGDP4_Wyw5F6c60oBcTXquTq6n_O84Ej9Ldo4IWzfgMyy9E06MdISQlYST4TadhWEEfPTnn8QRg3iDldk5TCSSjmK_vmiEsCB-EnZtBj-2sDblVQ3dPtEowZrI2LQ3dMbxxsT2wasakQLwGaRkiPxTQd90hPbeMEFEb7mSZxNOivIHTUY_fgYXbCNoM1ZuRqmty35b8LkjJ8Aond3hK7aJMNXGA3nUHlPN2IDfYUqJWDA7W6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV5SpthHiUKkyl_1yXcKj9u2x1xmXQJuKRsQvZ7AC7R6hItuwYGuDqKEftMMn5jCUwfEQcPC8279o0VjWdN1Ls9anijyVLLYDujdAGWrFhE6Ue3fjU4IWhThZHgel3UW4Gd8GwZvUea3L7Iz1yR0ZBWlvsX0vR0nQ7sJ6--vx1gTCOCwu-OZ4dZFJmLlFdTwYchnauU482KI6-VtRiAusZ29qIry4J7BSltezzV-5sl6uDxjGhcWRi58Hg2EY3l6GuYBticEmkeJKtReDk8oswdn3PC8K06LlYtCKTjzj4dAYwJ-SqKAYoqpIonUjJzDpvV21ZjmSqSReyXfqF2u1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عجیب اما واقعی، حمله‌ی گداوند به علی‌آقا دایی:
علی دایی رانتیه و آرزوی بمباران ایران رو داره
!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68368" target="_blank">📅 23:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qpgE5T8sTwDIAyKVesNghPGL2YZ3SrZBBDX8cqf3E6e4SwLwTe4ueBtTCo0kp81VWPPOzjjLS2XZV68Qf6wdbWy9fl7X11ATsFxH7a53vf-41Gb6hxqo1KpO54yXZQfLNqJ1YLmR0brxOwvFQYqv49eFiw4Ky2siLzlC25EtyKhYzUI1UNWOC9ugg1akqPL1cxsYIkWm2Oyc99qVhPUJr-miTSJ3eC7eSSkcK4yemoSS0qfFHbb5itMitlHjtmiJmJjSDW7byKg23x9R-oPXmhKiSibw9ZakCYGRNDFH-ExteNZJnb5-eQvv6s-XZYylduL0SDLjggpSF_4vNc1fww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2add3c110a.mp4?token=qpgE5T8sTwDIAyKVesNghPGL2YZ3SrZBBDX8cqf3E6e4SwLwTe4ueBtTCo0kp81VWPPOzjjLS2XZV68Qf6wdbWy9fl7X11ATsFxH7a53vf-41Gb6hxqo1KpO54yXZQfLNqJ1YLmR0brxOwvFQYqv49eFiw4Ky2siLzlC25EtyKhYzUI1UNWOC9ugg1akqPL1cxsYIkWm2Oyc99qVhPUJr-miTSJ3eC7eSSkcK4yemoSS0qfFHbb5itMitlHjtmiJmJjSDW7byKg23x9R-oPXmhKiSibw9ZakCYGRNDFH-ExteNZJnb5-eQvv6s-XZYylduL0SDLjggpSF_4vNc1fww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آرش اعلایی به جی دی ونس گفت مادرجنده
😂
:
جی دی ونس یک مادری داشته که هروئینی بوده و مدت بسیار زیادی به مواد مخدر اعتیاد داشته
مادرش پشت سرهم مجبور بوده از یک خونه به خونه دیگه بره
جی دی ونس یک کتاب داره که توش نوشته چندتا دوست پسر مامانش داشته و چطوری دوست پسراشو میاورده خونه و چقدر کمبود داشته
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68367" target="_blank">📅 22:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68366">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b27f10a.mp4?token=cSt_n_QetnViYX7nuS4jVvFL_3D4Zb6c74MW_qMXrWmFk0TsV1s_g340Ipc-ILRC6NchAOgZj_TNt767heMNxEOpjHYQTG3EREhwIoJ8ZbvHdYuiBwqRFZJhWBHJblpglq1KWzpM1nH4qS3FO5vOhaXv2R_OzN1cU5X4BK6-zYILxrTVrj9JBRS7M68zl_tzXM-eik3IiyJdCa_CBX3UkGm_8yAZ3OUZUgWc89ckPyktOTb9Ozxn0g63YkZHenVCRcLbigZ2b08cavyQ3t7H95jQY2SKbOQshvUs4B-nXVyVc4yc1U1cMobt1bRnxUj2Wr3IXL6yAoXgtPBnylMQiweLR95dAydlzng2UDJPAAnna8Omvh6bN9-LUQRpkXCf97oHkFckyycSo1-Lp59_hGHaG0sqJ1-nOvf8ZBeQdvU5Slff6Ia2yh7Z5E3dc3KAF3nQ7Edzh4sBvRrwReykl9Ek1HrrVka5GPdpS4WBpeIKNSP9gbPEvzXkcR1QwFEuS87fURhkUBBDtHXv8dl3P3U03tOuquzNRocAcy_d_upkdyfw94V_r80Kzn37lw4wc8xTbH-a3eDzDxeryC7048m4mWnwFeJHPSqOUZAZ8KLUkkHp6cZeR1kWOQ0AAI8-QsMo2heGJihA1rxLlN3_UK3ZDWDO2id35RtE5fy54rY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای که گفته میشه مربوط به کشتی تایلندی هست که مورداصابت قرار گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68366" target="_blank">📅 22:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68365">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68365" target="_blank">📅 21:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68364">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🇮🇷
یک کشتی تایلندی در تنگه هرمز هدف حمله سپاه پاسداران قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68364" target="_blank">📅 21:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68361">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b42e3ed3a4.mp4?token=aGIDZE1Dex3SpudYwMafYqR8fgeEHG6cLj2HsMZ04_VbaCbcB8S5kjng-wPRrzsC6bnC5zkju99CuTvIYGuVr7VFpElj7RnDK8V_K97xWkqoA7Wy9Z_WtTfQQ9Ax4CnigT_elayP7YiJp_Fv5OINx_ZWFidEhzTHLFNQmehsWTmYzRSN6H3CMqo0CuaMpueKVHU39eXAMDf-vT-ONup9MVLlrMD0ZXwiXazehdiOgV4vCY-kB1pWJNt5okY6voZOV3tNCVER_xkigtm-JanNmzB4Id-ZTARRRokILUM-8U3jt4IIsQzkw7tW8ZU0C5trFS6DTyhHPIspqZKkSqu6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت اقلیم کردستان پس از حملات جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68361" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68360">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68360" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68359">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raOYel0Gj_FV8S2WmMTDETKE5krbF0VO8ThVsoJ5rPcGHFjdkjdJEchu74ogZE3iy5BPHn1XLcO51zg9z2fK6vshMXttULa1Oj6iLJFpg3cpOBjoVQbwH2bDfxvtECMp_x-rA7IEtF-XlR7ieQYTbj1p7Xuk5arodyhssKeoK6TXyHqb0jgjf-QvIwUVIzVaNCfbFb3VPuw4mIk3wob7LyCDOnBsSR43DLKv_slTJhMnyWdVQU9mmxWPwR9AplECPBlgv6XSdQLRH88VCNBjfSwXXAMWostj-ngNl_Dw4XJTMy3AXonTaPW8Rq-VKb5W9fcbev4mnfhsQt_O1-zuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68359" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68358">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kowQ9Ujb1aFv7NE-VJ4O1UtrUiwvYn-Tp_gOYcCC9intS2vg_vcyPoS53kZnVHrgNNKK4cJIkg7148f1OWr4pfFVo4m6GPkI1FfYlj45ZfpG0unn8oBJg_y-bE8mBuRlujbTra7JSETafA5HxTWNRPsrnf6U7LwUcJf4JkNk7icVKrJEa5D1u4N5rGp73lSDZgJSV_gYf2AqNvx4R_xG65mdF_1XDLQK_nOsgAHyJMy4Q_dCYZgEn-xbKTQm6O90ORTEKij8RWDtsYMZ3FI_t9NY1TS601mHlmiTuf66eudIffJuu85qpOz78PyOu7ONcdbF9TaZfILpCATsKzoynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تعداد بیشتری از جنگنده‌های آمریکایی مدل F-16 که از اروپا به این منطقه اعزام شده‌اند، با پشتیبانی هواپیماهای تانکردار KC-135، در حال استقرار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68358" target="_blank">📅 21:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68357">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=GTL043_UKVTaB-u-pBOivCjJbs4PhUYnW4tbGegs3xppDQsH-B3FlyTZvdOUtKdkvA9nUc77Nhsq2-fesKPSQAprp8TCrJzb1BksOUCiwnCJBun6pKkOGnSKM7ZaWR71USShYNsLv9tLKiqi-rmzJTBGxbvPq3-JOK3BIbfzu9TBOPG4W_u2VUGtZbkYUe8ZwW7R6GX63Fz4Nl5m4zZ8fniSMZ5oywmt2H6zOvhN9L7fPOxVIBnjIDd6plqBJ1hWTUy3KqiwkTh-GHfKF_5OnBQ3BVHKLNRTNPCK7Y8o4r9AjgfFooBc85vKkjdn3hbySSMu901YYr9hBPexDnB3BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45585f31bc.mp4?token=GTL043_UKVTaB-u-pBOivCjJbs4PhUYnW4tbGegs3xppDQsH-B3FlyTZvdOUtKdkvA9nUc77Nhsq2-fesKPSQAprp8TCrJzb1BksOUCiwnCJBun6pKkOGnSKM7ZaWR71USShYNsLv9tLKiqi-rmzJTBGxbvPq3-JOK3BIbfzu9TBOPG4W_u2VUGtZbkYUe8ZwW7R6GX63Fz4Nl5m4zZ8fniSMZ5oywmt2H6zOvhN9L7fPOxVIBnjIDd6plqBJ1hWTUy3KqiwkTh-GHfKF_5OnBQ3BVHKLNRTNPCK7Y8o4r9AjgfFooBc85vKkjdn3hbySSMu901YYr9hBPexDnB3BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترافیک تنگه هرمز در ۱۶ جولای به کمترین میزان در طول سه هفته گذشته رسید و تنها هشت کشتی از این مسیر عبور کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68357" target="_blank">📅 20:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68356">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
تعداد قابل توجهی سوخترسان در حال اعزام به خاورمیانه است</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68356" target="_blank">📅 20:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68355">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab397d50.mp4?token=jFjQISafE_pX9Kso-Sd04CUMuuTYwu-P_rGxQOv_KqN4Z90wzzYHom5NBkykIdXySqxfnPVK_AbZx8On9IMRjOzeeb4ADn1zMXAh9J3zGpYbmfXtCThgUqn6B4F8e2NiNCMwmTYWQWvsL5Zg2x1Bg6__5Ow70FgJjN6EEK2aVH3BkAy_150prGhEvjSqsHXoL5h1ssGJ3bUUDi0d-HPCWmSJVTGva7TA0lVZVIEg1m_1h2sA9UN1adBCYeaqXDegzc0v2nsJOzXO0waIxfvQeZU5nKkh_luCgTPCwZUTzthoR0f_LO1YVlMR04QQtYw_OO0uAppTms1piOwdtGjeEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماهیگیران ایرانی یک پهپاد انتحاری آمریکایی مدل "لوکاس" را که سقوط کرده بود، از تنگه هرمز خارج کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68355" target="_blank">📅 19:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68354">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXXQjf6WRE1ISMxo9dagc4Krqqt_EAQ0eVtvezu1o13439Euwy7ZQcvmsUIvRcvyraR2l3bKsDluOVBul8x7rB2nV9dU5EkcqAmXQuqavlJ57qy8n6JZilycA9uNefLIpNQyLOyod1QzTgcNLA0p5hphupyG5dXDWYu9uisRQIo45s2Ad_a0T5Sshu-0ZIAQBAQO-DBD4xgOyUL6LFKcj0XUAgseDpNjSpcBnh7ILyxJSv2KVlGn8QkHzQL9CUol9n3MQFc7eYJAlTPCEe3U-Yc5LwyYzUtmnxtQ9lLq6FpCvbDiRHxdHiAV_Vx2PCTmNdYixg1nXP6geKPK5v_nrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.
حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن به این مناقشه قرار داده است؛
امری که می‌تواند نقش احتمالی آینده اسلام‌آباد به عنوان میانجی میان ایالات متحده و ایران را پیچیده سازد.
پاکستان که دارای تسلیحات هسته‌ای است و ماه گذشته در دستیابی به توافقی موقت در مناقشه میان واشنگتن و تهران نقش میانجی را ایفا کرد، سال گذشته یک توافق‌نامه دفاعی متقابل با عربستان سعودی امضا نمود و هزاران سرباز پاکستانی به همراه یک اسکادران از هواپیماهای جنگنده به این پادشاهی اعزام شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68354" target="_blank">📅 19:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68353">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_Tjs3yAObjwngS8Hv9lNgInYkyQ02hJegwsUiOdEc_5z20vF2frkrE2LQFcG5N52C_zBkT8rvq9hXo_4_XaTK9MkY0QHWz2cridtWL8dTKnmdeiO--4Id3IrnxjjuBGltKFwzbn5W8Ug_YtwPYZ7xfKoLVFz4sfssinmqEi3J3H3YAjV7B91f3dyDe-nhZWAZlUwJhKabqbNJ-k82BwS9aFggHOuFJlYrhol6CUABjU3FLhbrrY4JlrBb5xv3dicAnFAG8XUppUCUuqej23igycAJzswwGRhdYVru5XevEV727wBvnELQDVk_0yKW6olVfvcWqSAmFl38o9NZ7UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: نیروهای ایرانی مدعی‌اند که به پایگاه «التنف» در سوریه حمله کرده و در جریان آن، نیروهای آمریکایی را اسیر یا کشته‌اند. این ادعا نادرست است.
✔️
واقعیت: اخیراً هیچ‌یک از نیروهای آمریکایی در این منطقه کشته یا اسیر نشده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68353" target="_blank">📅 18:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68352">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3270052e5.mp4?token=HSMeJOLsNgbUEBVHsApLBZJZaZokoviHTNJs7ThQApwHoT-nCnnJiO60FgrTr59QYlaBuKELyzifNgNgM3plPa23PWrrM3aTZuQ1B3MhHNXka_YRUqMPUBX5eQxAjGVj1NJVgKTLI2DNVBYh0fjITrVNOUtcfvXEO2MjMTsYf_B2pfPdElTi-_gUicfyqTOMJvEsKlN16BaeOqs-iYbZZIzChmOdmeAcBzVr-VT_3WUMowt5-S9M8iqP_HvGejNNX-5d2pG2PG2o1XtpQ45Awri9t5m1-CCxbsDAQrD2Rf4X9BzT1v0F2J1q7lVQbw5zT0Oiww8UaldEsDcYTbsRSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در ۱۶ ژوئیه، نیروهای ایالات متحده با موفقیت برج نظارتی بندر شهید کلانتری چابهار را منهدم کردند؛
سازه‌ای که بخشی از شبکه نظارت دریایی در امتداد سواحل ایران در دریای عمان بود و دهه‌ها توسط سپاه پاسداران انقلاب اسلامی برای ردیابی و هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز مورد استفاده قرار می‌گرفت.
انهدام این برج، مستقیماً توانایی سپاه پاسداران را برای هماهنگی حملات علیه خدمه غیرنظامی و بی‌گناه کاهش می‌دهد.
علاوه بر این، این اقدام از آزادی کشتیرانی در آب‌های منطقه برای تمامی شناورها محافظت می‌کند، مگر کشتی‌هایی که قصد نقض محاصره دریایی جاری ایالات متحده علیه ایران را داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68352" target="_blank">📅 18:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68351">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c7b1cdf5.mp4?token=NqgATHzKZD3JhSVgdBvg7U91j5bpSOH03mqIs12uhf-EHBgfTCqGNpI7u-MOQotSxkocTh4LKUPA_FcaxHx6CJeXznuFntTKeKKNvWPiH7ElyuuDwmbox43x8v6L8DbIsEljO60z0ghx0O-Qy-SzEbWnCa-E6Uiv1UDeHuOQjBwsbdBW_8bv76tL7L5yhArfilfybgAzHqSL9e13d9K7r04B3cnK3lmGdNPcluMJesSOCD-7j5GjSLAUUAxLdR4nLq7sAy7fHC7jLZBg7UVanROLvR7BpBws8B_X51ZRdUNVk0kzRNJ_nCxwcREmiUAcZ_mbg5sld0cyRdNzx9u21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی باقری کنی، معاون امنیت ملی دبیر شورای عالی امنیت ملی:
برای آنکه رهبران آمریکا و رژیم صهیونیستی از وجود اراده جدی برای مجازات خود آگاه شوند، سریال «مختارنامه» را تماشا کنند
😶
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68351" target="_blank">📅 17:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHu-kqxgikpXkUo71iT_LhLcGkN0J7cDY6quTV1VBHam8KJk0SHLdHZ8F6h0ugKDqa_s73-QM3DEpwe8a1XbGeILNYA3SA0uagbT13Ce8UVZNozCuvaRG-2DQHMicflGTHGqb59g3xVVFRQidTLj2SalfC1hQLWTJ5NASEu3NURX2cWnhV6b39F_DG_YHGk4XZeuLVE31UTqJV4nyNOyxCq2qLKsmRjQBx2RjzmXfW7pGt70PA-mhNrdGxeq0szGIZ6wFWKXzrcejesdLiykBvpgCwIVQw8oXPN8hWY9If56LWvG3w2n8xQDHIzOG5aII_u_2PMl99cr32TR38LZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6De5kUpyXRL1NqiYJJ1cdw1R3GsR52uj2aLSEHocYqOMVxqM2NGSwxN8LVuH-yvnTuexfrz5BC8BJQR0qIqG5D8Z0OKzWKqpsdbTEOiPyTpt0egsAzQZkBxpJdIOx8VnzpQqoBCQcQ7p9z8odHyTFg8jWmyPQjhcTcyeBP1z7Dv59Jxo2ocmazhWwS_AOREShrHhDX55NmSoyK4RVlQz50NM4P8ogI4r9Mfuiw9bVPkPlxzsaolbLgf1J5nHusd9qrz3LUkJqTsroji_4FlehxmRvPlfxVoV0tLxrKIXX11BC8kPic6RhOQzZHb03Lz0rxBahT12NP3huiAGuM7Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeOhbH0igCJnnENwNcnp-RWLBwwNVLlGQL2l_8V5S7OC-G8X-wwYlks7T0GvscnQaTpueJZvGXX3iFJJnyGRSPO1dbh54LRoS1ttLDRi1V96Esxn-6DoplkT3AZ0U-hayGoGFCQOazGvC04UtOSXhIyzWq5iYT1S7GhwBL4RGT2SupYD5D8MxsUfemBmYke9qbpFXE-vvbrbjL22ndbEcTOv0DFqwlLXnbgd4qRRBgTUsX6OabdYdVhUffHm1Kj5AyUwu4PS3Wc1txn1gNtPmvtoLWqrDZHi-9BtXv7QHWZlo_25Vbz8aZ3xmeFSDSLKLqbKdIe2quavR8bFZajnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_AhHecTZ1NbIKLVSYm3DsEifTMZ_9TSU6kXO4fWXeMs3hD2_ArJEdaXy3ciQmNj7V_xzRcyn2FUO5V0g39cSHDBADV-Xai4_BRouYVE8U6yygCV9cTtAg987Hv9yf9ALYS5sJJE5L8Acaw3hsiF2geBJ0WGf0nonnKsuFDcT73kgHj6l8EMzzXd4IKPaTJPyvKF8O09x7HzzOp-FqykqyKjufanHl_T_SUCG7gnPluPs-vWjy-BvcaaxDYvh_SdSUEdadbxPDrq7VCS7LwyXEJAfSBvpyrsxZc3QHvoSewiDPYwWrZ1zITH82WAiw01Ejdk0Zc4o_FO6BKelrGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioxqVO2YppG9C8xOF16wAPWGeeIeVUjpgy4JKIhhW_0oG5I9As4S-VMBUIHlOpoN64_-75CAQVT4mEWKG0s7cha5LuQIJqrwCY5LxgAg9bOIjzSVyAlqbFQ0kH5VIxqotwyKX1eq-bZAGRvquGe4xihHZiKHTLgeEKUAWxv0WSEkYqR_qHW5_EYvm8NJpFlLv7G1A8IcvmHab66Ru2P4CHk_GS5Qa7NHAx-Ck-ti06QDEkiL_ANFU0oSnj9m3lgnpOQ4JuJKMajxiIS7Pvh1rs9Dy8lFUvbF_SK-Hq--SkMjccC3E9a8cli6etgP9owjMWvnZx1-vkHSM1R61lCmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHLLfoI3Z-JTjxWWm95I9LkWX-h0qaYZD9tzQbbZBcVUVaskEV20U7GAYAkr-mWh7bTu9gAgyfuxwwoO9Y457u08gXm5GL_w4T66QPwRdlhMAOZKWIss4cTCNk9fPTTukDujKarq3ssMwhlmo0f9_AILMwS8Bfk0R9Rpfc_BuWtgJNuyPexjfxXFHSSDTy3WdFIBGtzHMhpGb4C0WkZ1AJUEzdzG8ENIm3LwslmImhfTR-xjRVfHGeDcGINjPChJay6-oJEEkf_ZuGTvySLgyc2BnD5yUbjO77Z4mInGbr-zdlTyd8HSz91IQq3EuB4VTr87xTRVlbhUgGmDcKlaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn5TQD-dCgfuSV2W5TNDbOMbV_ZL2oVcg5TLAL9GxBVNqKusEMM8tlv5ljEs270YSRmN8wFu8weocjHqQcd4vjAdlYbfUlrMUCtURXbpEYV-W_5_2noEdWlCKg_Ic8avQgtkpX1AcdjajTtDMz0VwNSEsOyKflIUlHg0h1akTd0c0FkG7_Z6k_EEBFWGZd5N12amNZ2URAj9Q7ds3WEQzeliHhqcZlb-ChHGk6T37gHYGTnnkxu_6Crbfdb7sHkDGnh62wbPa97O5PcB9QMPXkrc7FUUELicyPz9y4tY73MTfe0BFOD4BrJ_IghbYTsA0WYP_ecy2rT5drznNsxurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mi7BttRD_VR5EK9QC8cUXdoDUzZbQ0xZBg4QqOiwpK3IABA-J3_7HhZloHFKXbAESOsKMS4CqnKhGsi_xUBigEaaf6fdE-MTGO-3q4xOzTDVm-NjoWJsVrGPrsDmoePIBg_9oInEiUG2QKu0-FUYGLoFpGLhgYrahJ3MNUqB6LBDxcmcrivse2lNotPKcAD8ATTCTDJyvxqhOqIRC0JrXI9StuySMbaakcCTFq9wi9G2k0blT1kuLQECiURV6PoQRbPRgUNRlox7aO3ggmyJ5PFfLIgCLKKMT7JTLwOxqTEpJJxQEAl7mfxQVRrLDD-ARQQyogmmBotlUkPWWDRgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcKRR0ukohSmu2TwdLkfo7lZRvoRYl46BVhrtxUkFtEwZAZaLO7j3cnn8HmfgLtNPq1lmLpWyOBz4k9yMfdw5OBwrNQibH-EKcEpVtpSvMb9yUSLuY-N5nBpCs1J_BaKxEBKGTe2l_QHuqk9JirdAsMmqBSsKqXjqo0aesRJDh1WuCRo5OolSsEiMlR7UcclQdwlIC-2Zj8nzMGSGUuFzWeIZj1Y2t2tDwCObfQKAlwmi_enpxfIQ2qHwMJSb0VtUcTLxrsYadD2DpOg0PR0YMz_XDXG2ZfatWHA8CsK4PqOlYuW7tgzGyrjT6fBTAMT_XabExl5riKocOWSbFKg3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2nxrlVHIFxVOibw0bcckepEoDzXIrdUVRkRcukWeAHF6I5N8AfeJdfoffFEzfOnwNevucUVv5bo6ZNH8jQ5Pzlq0KavZnpAeyP7qEhUIygfZZPyOao3_8UXFnzYXKr90Rks1emUunjWToC8pTHroe_C-_O3klGTun4J97LOiLfIx-KGy5h_cbE76tKI8x4Z3_Sf4jOoaG2i4hSwsU7U0XB2lH-t-AfwspayzfwnJsvhCpscuBYoPudNsKcWogs2QdHGLXuUjsh6CH1XRJSyRKu-bNdX-Gx1laEjKovJO_M4DDp9KihdDzMdpCLG3qK5pTdotBRYnbL0OAy2UDHRVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSEvhXWR_reVlvuXq34y4-0ZGZQPuSiLwOh5G5PsbaArkWlSjxCIhXgrVXyGIp7fgE9fLqmfCYRMIZsq9rbFO2B-PTFfa73PmQgastYVSrEIjyfTPRSe_1htFUkh2WdO4x9-QuefVDXFJjkXLH1jyNa0mgUVu-kKbcn6H036gbwBEcVEHeoYyAb4hNqLxbXF4V-SMTEimYpv9o1sooNJ5SIoIkhSNn_18obKJRpdWZi5vo051vtuZCRPDQXMxB3_vgxNrqWSQKCHxU37uHPquya7XmNGayQMDb_7p9vSjHgRbj04_g8hVnzvwgk25jqARgyhdnhtltYFlEx4UzOhWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=NOfUKKQP-nd_KxYuUU-3ZIVxQ1nqrLYld0j8w4OsN3A2mnMQuum-rWD9s3wfDPwz4T_EOfQTmn6yTDvSk8cQGkNWrSfM3bvMfapb4yMV-Xt-vtbUp1YvTM5SyRrKl6siCp3USwjyXHhw3zy3dic46KBpiT2C88MXzFZo3uZJjQqbDELJLedeXgfLdur-jRSr5c7Ogvy8_xQyEEcsn1oEUPvLSmrAm-KHnEei9QJCxJZUP7rTBM2eZpBAfM42qQaqfzwZE4axa8qxNJUKOjdCbQEfKlY6oCYpm9fe2HbKrdIa1RPFsQAGhCuhXjctqTvSuunD6Aj3tz_NZrCJ6Hj49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=NOfUKKQP-nd_KxYuUU-3ZIVxQ1nqrLYld0j8w4OsN3A2mnMQuum-rWD9s3wfDPwz4T_EOfQTmn6yTDvSk8cQGkNWrSfM3bvMfapb4yMV-Xt-vtbUp1YvTM5SyRrKl6siCp3USwjyXHhw3zy3dic46KBpiT2C88MXzFZo3uZJjQqbDELJLedeXgfLdur-jRSr5c7Ogvy8_xQyEEcsn1oEUPvLSmrAm-KHnEei9QJCxJZUP7rTBM2eZpBAfM42qQaqfzwZE4axa8qxNJUKOjdCbQEfKlY6oCYpm9fe2HbKrdIa1RPFsQAGhCuhXjctqTvSuunD6Aj3tz_NZrCJ6Hj49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khUIkCtQDwJtTPXDTO430S4btMi--AT8V0egBuU3LYRm5tv8U1jreuvWjNEqxl3fknLzSskmA9VQCnzhF7NWlQL_GSZZC9gASBSDFezsP6YaCXycC_6lwVo0fx87TsGmLk8y0-UZTx-H5To-CENzi_nHgqYirQD6-e2YImqMEOFQlEcIKSwV-O0vPwtxmR98ODTEBHu54EdHU64ReqTX4L3zYrtIwdEHPYbVvg5k4ZILMfw11pe4SPiLHg5uOUdhV1pYL7FAAiJR06nzWbP32pJpXE-FzFqoPuxTj2LMWvw7mYGqViDEKwQkxZ1KF5MKc590ojcJjcKDRMRbeYrOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=ZYiyA8zDit73TgPqjNZlrB0FmvxZcTRgqHRAEMwRnq7_YroOcnDJx_ShmuCVPO7xHOqWWSsPmxb86pQlIpaQxJaF_8NCaCazbegUnAtSI6iMcSi1F93PlY-E5Ke6Z7AR7yTe88qzKutd4zMEVEoxfHKuehSlF8axBNepJy8-RVMZ6Z0xQLVa036lGrJFzPiHBMuo5qj3OYFUQzVzjWGAPODkrJUggC3oO3dQE0CpFyMzZRrIFI5ZzrPTCskJhJDnXAtAyCP38XhiwDAqXhr4E9mwbryxTAyocbd57NKd1lrJ3Ma20ma8eMedMVrO7jinImL6vjjgk7soRVPPF6eqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=ZYiyA8zDit73TgPqjNZlrB0FmvxZcTRgqHRAEMwRnq7_YroOcnDJx_ShmuCVPO7xHOqWWSsPmxb86pQlIpaQxJaF_8NCaCazbegUnAtSI6iMcSi1F93PlY-E5Ke6Z7AR7yTe88qzKutd4zMEVEoxfHKuehSlF8axBNepJy8-RVMZ6Z0xQLVa036lGrJFzPiHBMuo5qj3OYFUQzVzjWGAPODkrJUggC3oO3dQE0CpFyMzZRrIFI5ZzrPTCskJhJDnXAtAyCP38XhiwDAqXhr4E9mwbryxTAyocbd57NKd1lrJ3Ma20ma8eMedMVrO7jinImL6vjjgk7soRVPPF6eqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=EhRN5ss_CeIpkE42hz2mr9MA6Be0fD4rHkOfKFkIgVptDMyY3UBst17q1JMbqdkS_0Zhgzpww3Dj9CeD7gj2jZZKk0Oqd08KjY1GpIZ5u-n9LwoG6F_bp_4FPWgxd1bi_jotIfMw25OvQzV4gZm4hxon46MQ3QBUQEw1TlP12t4jotXljm5huvhHTcR2ykFd6rK43oqkllmX5-mzhMhMftHHZhPjwehTeSF6kgYf-siR4Pl2p1BkqlP8X44NFwUWtqaIxqLtdFK8Y9JAlv2_Y1BQJlWUus1AecRAYZWC9DW1A4Yp7Oap8K3A6tIa5ZIVTIJ3YbggCBC-63UmCZCz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=EhRN5ss_CeIpkE42hz2mr9MA6Be0fD4rHkOfKFkIgVptDMyY3UBst17q1JMbqdkS_0Zhgzpww3Dj9CeD7gj2jZZKk0Oqd08KjY1GpIZ5u-n9LwoG6F_bp_4FPWgxd1bi_jotIfMw25OvQzV4gZm4hxon46MQ3QBUQEw1TlP12t4jotXljm5huvhHTcR2ykFd6rK43oqkllmX5-mzhMhMftHHZhPjwehTeSF6kgYf-siR4Pl2p1BkqlP8X44NFwUWtqaIxqLtdFK8Y9JAlv2_Y1BQJlWUus1AecRAYZWC9DW1A4Yp7Oap8K3A6tIa5ZIVTIJ3YbggCBC-63UmCZCz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPDkojMbdYkRpMrRAG_cbIiO5Nf5aM8J-a5ZdSqFosXYLocPrvP3wknkpBI7mT3FL99qeb84-zOlM4QM8K2NchcR6Bovb4-OZcK-lH7tDfHlqNm_tn2QfSxknVbzWcoPksRw7YjX52opnBVImGAePt4wkJT_tgdimueUISAyBWIJElLMX-YKRif_Pz5lEciP1yhs3QD5OeKeEgT1UU4iHM64eHNcAk84jK8umg4JKmcYcBTPU1Bvm6ZM9ESCC2OvfuYM-1yOjakj6zkRqOrpye4M1SeKLr3uBenW-FY_z91qgNOEklDLxLs1n_E_U3K1Gz_eQshrwsIV2qrk2SlZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=BPuYI6ElXeHUPjO0-r7WwtG6Y8PbvcnVLxxxHNNbIVPAHV2iJetCOuNgk3HMinvDrE1f9sdWbXSJKITeCMBy-21uWkXojzH0Sm_sZ-VM3hafviisLLWZRQZnvFUlW5Sm66ReyIDOVxyP9xUGYdcrrHjh5gRH4IPN1J0ooXXlWROTfuApbSXPn-0iNNjVOvk4T9dIZ-ZyIIxatA5Nf8hosWKtStw4oWsEP8yb_RAVOkRo90lplSnoZ4OnV0dWsNeUHH-NH3Q2cFQqEnH1khg-DWf3pQFveSgvtm2DD__YPrN6kSMHq6ndB5WYzYTFwG0LoBivIzK8kR78OoIrmqjlHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=BPuYI6ElXeHUPjO0-r7WwtG6Y8PbvcnVLxxxHNNbIVPAHV2iJetCOuNgk3HMinvDrE1f9sdWbXSJKITeCMBy-21uWkXojzH0Sm_sZ-VM3hafviisLLWZRQZnvFUlW5Sm66ReyIDOVxyP9xUGYdcrrHjh5gRH4IPN1J0ooXXlWROTfuApbSXPn-0iNNjVOvk4T9dIZ-ZyIIxatA5Nf8hosWKtStw4oWsEP8yb_RAVOkRo90lplSnoZ4OnV0dWsNeUHH-NH3Q2cFQqEnH1khg-DWf3pQFveSgvtm2DD__YPrN6kSMHq6ndB5WYzYTFwG0LoBivIzK8kR78OoIrmqjlHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6Nrjg9JoXKYJmLEHeqZKKJUcfapkT1J1BC8RN-6oh3b04OZ1M2FGSSNe9m4XVJdc8EqyDRuDOa5yQ4QbA_uYIsPFqRwJokZjzsSwk7lHewRxIIDGCeG5HaEGrTxf1hn4F715J4J-NcIDBPUC0ipNqb6diHAOOBYIpbxfz8r1NmTuYDNL4zV0uSXExB64SUacKZluydZxgFNhw9ddQSFMM-apnCxXBApVB013SESqYMsd6yQSLMZGriBcgicsvTjZZos5V4pKHYVAW7LofD6q5UsPOFqsTNkVwM_ozLCi6Yxah_Z8B1t4aBwhdKRgc1GRanINILIwwU6s0zofPrmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=RF8CriPC1Z0o3sLN9dbWVWtDPf4Hn7mops2VhfGAFOLmsh1OnhCeREAmUE0B3pswQszeqibtI91WznupEEQy3wQeZZjKBICWz7Je99PE0jwXhAu63cNupudP0l3BmKm9koNtJJiv6PBfKWszckaNmViAFdZIX0r6GuTX6goFMsOcyXno7YUF1koVLgKdFFm0JNIpioA8BkSrYD76mvSeatjKpHM0WOWBqsO49ZC2YHZC1J6PBDznVGjLyNkoWRRCe6k3--ShPuQbvvliK4frPP8_zvH9dEx-mwoDXlf3hcVtI99jpKTEY_vPVfy5XE2ehEswzOG2cCHyfLe8RizJcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=RF8CriPC1Z0o3sLN9dbWVWtDPf4Hn7mops2VhfGAFOLmsh1OnhCeREAmUE0B3pswQszeqibtI91WznupEEQy3wQeZZjKBICWz7Je99PE0jwXhAu63cNupudP0l3BmKm9koNtJJiv6PBfKWszckaNmViAFdZIX0r6GuTX6goFMsOcyXno7YUF1koVLgKdFFm0JNIpioA8BkSrYD76mvSeatjKpHM0WOWBqsO49ZC2YHZC1J6PBDznVGjLyNkoWRRCe6k3--ShPuQbvvliK4frPP8_zvH9dEx-mwoDXlf3hcVtI99jpKTEY_vPVfy5XE2ehEswzOG2cCHyfLe8RizJcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=a0BUYmg0AzG3gcoyHGjAjeUYYzV_K7BCppU1WZYp4_FF_VAIQB61GgKCHnTNBvjO4OqHfuQKlj8kPqFNonni2XIrKQjxBhFzRg3M_58PjlXbd46pECwbQn0j_fn1mqJFc2a4kO4ykxDy90VLyTm2lFMZpdVDax2aC6tGYNY-KRK7PDkUuDnirQiLXyJVsgrabbNJlrJRwqodtZ-_e1LECWR2qkRTa76hBbdW4ui0MRsjI49_QQYRYF0P4T-AaWK_6C5V-uZ94BcJOV6AHux8YPaSoSIX9Dd5INw40z0aNeFVUgWUzqfLj-Aq5mrEsZ5OS58d4QkE60WG896BSoV6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=a0BUYmg0AzG3gcoyHGjAjeUYYzV_K7BCppU1WZYp4_FF_VAIQB61GgKCHnTNBvjO4OqHfuQKlj8kPqFNonni2XIrKQjxBhFzRg3M_58PjlXbd46pECwbQn0j_fn1mqJFc2a4kO4ykxDy90VLyTm2lFMZpdVDax2aC6tGYNY-KRK7PDkUuDnirQiLXyJVsgrabbNJlrJRwqodtZ-_e1LECWR2qkRTa76hBbdW4ui0MRsjI49_QQYRYF0P4T-AaWK_6C5V-uZ94BcJOV6AHux8YPaSoSIX9Dd5INw40z0aNeFVUgWUzqfLj-Aq5mrEsZ5OS58d4QkE60WG896BSoV6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=lk7_cPbmnn46HTofmPmWggYVi_10QDou4bEZDqD7LBc8Ffx9N77l0gHdfimIcbmEg1YLTEHnR9PzXgjQg_TmElW7x2shmlYIAdwlDNVjmB3UvGnhrchFJL1aDfpqYKbVgl4SnnQkaWKeJPXsCCvgJwq9T9Kjd11-8UOLUToe4F37vYnWqsEm1lJu8NYhBhEul0NIMqI5QbqoAtJXG7-Mx5364_gfwMJPTlhuj8ADQ2_HC6ZRm5WeCZj9izIui31C-kcRIPRjFiGfw3_aCu7UGbPjhrL3rt3kt_8uHO-rAy9W5c9rMwSCSYVOq1-wdkvHae1EydijUtdEQl3wnOlg-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=lk7_cPbmnn46HTofmPmWggYVi_10QDou4bEZDqD7LBc8Ffx9N77l0gHdfimIcbmEg1YLTEHnR9PzXgjQg_TmElW7x2shmlYIAdwlDNVjmB3UvGnhrchFJL1aDfpqYKbVgl4SnnQkaWKeJPXsCCvgJwq9T9Kjd11-8UOLUToe4F37vYnWqsEm1lJu8NYhBhEul0NIMqI5QbqoAtJXG7-Mx5364_gfwMJPTlhuj8ADQ2_HC6ZRm5WeCZj9izIui31C-kcRIPRjFiGfw3_aCu7UGbPjhrL3rt3kt_8uHO-rAy9W5c9rMwSCSYVOq1-wdkvHae1EydijUtdEQl3wnOlg-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=HOU-1gFoVVO8cBL6zA5pYqIorXwsukwzmrU3DqOHBr_j_QJ0qGliiyuGcBtNHFVRKOx-44AocCmdpPVWwd0St8oRCK5fvVKvl98h6qYkQuKUzW5v-wohKs7B4wTPeqB_RgI8zkGC_ll6oafodhUSOE2m_swK8mUIBLW7aZqd_yX-V8-7aTKhpasQ-wxvpWtDvLPb8xGyap7UZeeL29W4x_rAIxH4BM3bxzlkXXB-bYjkj8TghHh6YU4cKdJ_VVhM8VgVGYT3-J2Ni3J7clgVcYoenuvHiWblFeCn1bsJSk-ojRHlDm77JM2eQWCTdeqXHff19iekXrfEEDzwe3Jcmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=HOU-1gFoVVO8cBL6zA5pYqIorXwsukwzmrU3DqOHBr_j_QJ0qGliiyuGcBtNHFVRKOx-44AocCmdpPVWwd0St8oRCK5fvVKvl98h6qYkQuKUzW5v-wohKs7B4wTPeqB_RgI8zkGC_ll6oafodhUSOE2m_swK8mUIBLW7aZqd_yX-V8-7aTKhpasQ-wxvpWtDvLPb8xGyap7UZeeL29W4x_rAIxH4BM3bxzlkXXB-bYjkj8TghHh6YU4cKdJ_VVhM8VgVGYT3-J2Ni3J7clgVcYoenuvHiWblFeCn1bsJSk-ojRHlDm77JM2eQWCTdeqXHff19iekXrfEEDzwe3Jcmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=v6AesZazjivN574kaYnOML_XZn0OIG_KmkG7fjIPmm9BxNRgrb70YoPbED57XqNUn4JLySYdrlG9-ANg5QjBYjVxxOn8oxKbnLnbwtphNLHt1l5hUlxOBRPOdMqlw6jXKdi-q07MOKdgkLV1rcTEuxxyTx8N0sUoEAhjigRzfKTaUuTJGkCJn4WGR8xv32fhixfFXdJUG7HddryPB5HxQhlUyEUMmk8z9Q11MuRhj_XUWFZusVXgnVF2e-PbnieSe2qAWSbeFqPaaOPWPMRjgqx3_9WiCIAUugX53vcwEpXQFLDq-_c8hePUbBZRizYI6RsuWvwAL2Neh-QzD89T9AlxbtBBt4PcDiqzXj5S37t_IjZroos9YNkuMjT7xuUTLvGlrrXzbMFUARHL8tSI7yKE6Rjb-2C9BL08bfzz8zzXflNvn6L6weXdLLKgJJGnwvsEhXZ0glfCaIvDaUNfp-srKJAUaiqBNwQDzI3fifGMZvnIcobo4rRNsKJQb_nkUnzAo9A-R361cWnRKTV0uP_5ABe-STP5SIQNrja9LBQlFY5YWW1z9cu0ZpEGIBvj5KZlKtuBgh8EfKuDvqkbB8ZDgOUw4f3w-01eVBUK9XrpGJn0_svJiuyKDtI9tUE2CupQ2OLqpcN22SZ4h-VycITGRKB9F54lDwnwttJyD1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=v6AesZazjivN574kaYnOML_XZn0OIG_KmkG7fjIPmm9BxNRgrb70YoPbED57XqNUn4JLySYdrlG9-ANg5QjBYjVxxOn8oxKbnLnbwtphNLHt1l5hUlxOBRPOdMqlw6jXKdi-q07MOKdgkLV1rcTEuxxyTx8N0sUoEAhjigRzfKTaUuTJGkCJn4WGR8xv32fhixfFXdJUG7HddryPB5HxQhlUyEUMmk8z9Q11MuRhj_XUWFZusVXgnVF2e-PbnieSe2qAWSbeFqPaaOPWPMRjgqx3_9WiCIAUugX53vcwEpXQFLDq-_c8hePUbBZRizYI6RsuWvwAL2Neh-QzD89T9AlxbtBBt4PcDiqzXj5S37t_IjZroos9YNkuMjT7xuUTLvGlrrXzbMFUARHL8tSI7yKE6Rjb-2C9BL08bfzz8zzXflNvn6L6weXdLLKgJJGnwvsEhXZ0glfCaIvDaUNfp-srKJAUaiqBNwQDzI3fifGMZvnIcobo4rRNsKJQb_nkUnzAo9A-R361cWnRKTV0uP_5ABe-STP5SIQNrja9LBQlFY5YWW1z9cu0ZpEGIBvj5KZlKtuBgh8EfKuDvqkbB8ZDgOUw4f3w-01eVBUK9XrpGJn0_svJiuyKDtI9tUE2CupQ2OLqpcN22SZ4h-VycITGRKB9F54lDwnwttJyD1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=owMtgKZH_z2-saG37qWzUXdxHx9Nu-QN0MI0qkRSZXtHgagEetU9iBUv6ly0hH5kjFm42YX6kVzEl4GcpAVJVXsTB1I155SMBakyT9nJh7hsO78wzwO05EqnvT3dNxMqMwl3FUk8IOpmEhXs-KHI08CyKWMAYCmWs04VoILgQMd4ZMz813iyAzaV1QcngIxya10I6KRvfLqrckizSf1NUp-YQ7D8Ye8yfF0Qpf8xoWQIsDdlodPqQh1blVbRo-_Qs5vkrt6ENoJ7aBHwtRFEzbx_Wsg_74191ePqnmyVUkDml-4VBNiv4AIPAqzvo6ejqKfFNn_JcK1sCelf1yMqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=owMtgKZH_z2-saG37qWzUXdxHx9Nu-QN0MI0qkRSZXtHgagEetU9iBUv6ly0hH5kjFm42YX6kVzEl4GcpAVJVXsTB1I155SMBakyT9nJh7hsO78wzwO05EqnvT3dNxMqMwl3FUk8IOpmEhXs-KHI08CyKWMAYCmWs04VoILgQMd4ZMz813iyAzaV1QcngIxya10I6KRvfLqrckizSf1NUp-YQ7D8Ye8yfF0Qpf8xoWQIsDdlodPqQh1blVbRo-_Qs5vkrt6ENoJ7aBHwtRFEzbx_Wsg_74191ePqnmyVUkDml-4VBNiv4AIPAqzvo6ejqKfFNn_JcK1sCelf1yMqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDjHWdzyyy9R5czwLZbIeGXYrK3dgVUiRihDSUdzpGMODyPoIKD9F7r5nnY8PZGHClCABpxIbFUr8v3Yu5-OM9fVA165ARcrzRN0pZYCUYcbKlVwTTWbuzjn2PF4fUyMtD6amS9Ur2fdYj7XM4YP5u0MpdtyQBSDYpqEvpxZFHitaa_dK6kbgHlIU7VI5poPlsAw7KFmUfHbsPZI5HsqOCh4QEhmyJoHhCse-lnb55H59SXVQlOb1GDiAix8_zpgqkaLi99mb9z2cISvl-Gpd2G6wGzYM7lKeih9f_YcqUn7lhb_pg3xWVpBbkWAmgnFf1vfVwfjIIS2Am44Q6KRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbTLRuFi7ZLw9uCsoaDH50V2VPS6rTPj60FflO8fxBZgAoLxzzAUrV9MrTa9v51pYhI1X4zeocFycZnI7ULJ6u-ajQQuRZrcQtKwEhRfgFuPvmnkjtPK1zYQAqRE4uVTpILGqH5qrIsl_X97rSNafANsST34r-jTkLh-cTcpVW3RlobVi_abCv-vWBpTpXrEmRrh53VTsdW4wH7CHgSAcbE8nPP8WlUTTfL2OK1zXaQWqB-iVTk1x7iupnZgYLwEK0L0IKpQJ4vUaZb1JO6yKT-KvhUmXC31r7lbEvrinZ1S3IWWbuZPA9d9bnwnPAHWOPBCBVd4nn6xFwUENGQSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap89vW4V5yozvX-RMrFM96VmlyU2xluEyeKSNmcn90wqArfW6wOKzId8Ujodap4TofmFF6WqchmHEc0VoZQqVXRnJB5vkp5fJjzzdZUBMMrIRPp6lyQYFYeOep8TPmrox9fqAjjnkYPNj2y8A-2P5A4ENE6uir9sAjhiJPSc3sstQsJmwOImc80M3Z-kCaxR7eokHNcZUmFckiNjuqwRRcpDBOLhUKqNsHhsTpylh6pz9OSeSE5dSXsJYtc34WSJ-pDNKhuzcNog1rNHqE4ih_9na3iL7oFpLOb4N8vJYeCmV7coUE458g_u-M62EByCZrx6NeabQ68bkSrzuhXpGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2906TSflmUglM-VG14LhL8Y15lLpCMVyovNpmJn_H0qfzyCF3GGMBDYKbiU3VID3pGZ1T4acWt6Ffa3z7T1NOcNd6NsAgakyxzsK8z-ZrrCqh-JlG9gLQl3uHHtt3R_gXF-kr-I3oHvIWwq_l2xjZn_t5F0JMtiQ-z4pcgMDekQ2OwVq4DLqcoLt3cUOURKIIWGGW6Xq6Wuwh7vOs930QYEvTE1F2tNceVRCh9YXJNCCdmuysAv0xuhQ3QcQGW99ZdV-UQrKT0qsN8BlWR2Ng5TQkiBagcVlQYWu40IkFoJwoqV8evURVc0I4wsI4JMVuLHHLAESVF4x7QGmiAlFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=l6zw2XeKHrHfc1Y4c3_pzd-jcVArqvmTvC0KGezDJcVYa7euvL7St2b__EQHx3dKFpo-v_CibNH0XgcbBcHkEtzczG1ZK_gIkhNiiCDq39FTX5APTn0YOAfL72gwP7OyLrbbpSqvBp2nrOgQrQf4yMeOoENOeyQe4yBDP_1nvVg3pafl4c8-TvJXYuYL7J7IW8wKksdbbJrl5rmHrPFQUjVMN-jTWwjR_37jArs15OCBY5Ic97laFZjz5-FYZp1O4XUpThC5RpDpIFvRh2UuWo02bs28rjKQcKirLhX9UtL_Y_IvBEWKraGvfn2c8lmu8npC4xpyy5ytSOoDNdSK9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=l6zw2XeKHrHfc1Y4c3_pzd-jcVArqvmTvC0KGezDJcVYa7euvL7St2b__EQHx3dKFpo-v_CibNH0XgcbBcHkEtzczG1ZK_gIkhNiiCDq39FTX5APTn0YOAfL72gwP7OyLrbbpSqvBp2nrOgQrQf4yMeOoENOeyQe4yBDP_1nvVg3pafl4c8-TvJXYuYL7J7IW8wKksdbbJrl5rmHrPFQUjVMN-jTWwjR_37jArs15OCBY5Ic97laFZjz5-FYZp1O4XUpThC5RpDpIFvRh2UuWo02bs28rjKQcKirLhX9UtL_Y_IvBEWKraGvfn2c8lmu8npC4xpyy5ytSOoDNdSK9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=m74_ciyCPAeGmOtQnHSZBvvFzmh7Z0oq1rGZ65xrtxALU6isG0QjMY5-9KBaWWNtCIJOPVxqtduwJq2h1uXS2n0v-rK1VqHNi1GCdjDioJCipVvisrsi_sHVyagfPNb_vRuPqeSb2fgIZH5a_1v3OkwMztA9NhKRq50N-POqgW71hX2Iz1gn_oMYvU1ImpNC0xT8pm0N28k3tR9qFqrpKGA2DcA-RVqt431CrYXTQ1mDacNd7JyjAtmvJs6O2mNze6DUib0UAkSapV8nGiL0xhqyfaWv48pF2wOQA9KhQM3SFU3dhVXKYsKm5oVfskJiYwkVw19E8HPHPVi3_p56gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=m74_ciyCPAeGmOtQnHSZBvvFzmh7Z0oq1rGZ65xrtxALU6isG0QjMY5-9KBaWWNtCIJOPVxqtduwJq2h1uXS2n0v-rK1VqHNi1GCdjDioJCipVvisrsi_sHVyagfPNb_vRuPqeSb2fgIZH5a_1v3OkwMztA9NhKRq50N-POqgW71hX2Iz1gn_oMYvU1ImpNC0xT8pm0N28k3tR9qFqrpKGA2DcA-RVqt431CrYXTQ1mDacNd7JyjAtmvJs6O2mNze6DUib0UAkSapV8nGiL0xhqyfaWv48pF2wOQA9KhQM3SFU3dhVXKYsKm5oVfskJiYwkVw19E8HPHPVi3_p56gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=Bxf3ljUmTk74m4EGv53yuRGwIHNwxc5PvXuLr3-DmgkG5o4QNHOcQxW7wMRr2Q4eCbwkwYqEDraCIrr6KnlH0jZY88J-npzZ30xwPtQlVsucsfR-6UPC5xxjYUlixhJH4KTHr9zBU9rgX_VatThmtNTorPX3bfaPa7cVfTAQ0R6n4RzJ8mK5nDx7JPguZv7Fs8e4qQTIfZCCn_g8lCKhbUsz7UpRx5uDVt6YCY273XsgoLz-gf2CIxpADXOadZZVik-2mVO_i8qQFkAZa7ozjJp2box1An1zQYMnG6xN6VS0lb0iuOYsb8sqfrEgZUJlZ92dRq0jwgYbhfKCtTjQcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=Bxf3ljUmTk74m4EGv53yuRGwIHNwxc5PvXuLr3-DmgkG5o4QNHOcQxW7wMRr2Q4eCbwkwYqEDraCIrr6KnlH0jZY88J-npzZ30xwPtQlVsucsfR-6UPC5xxjYUlixhJH4KTHr9zBU9rgX_VatThmtNTorPX3bfaPa7cVfTAQ0R6n4RzJ8mK5nDx7JPguZv7Fs8e4qQTIfZCCn_g8lCKhbUsz7UpRx5uDVt6YCY273XsgoLz-gf2CIxpADXOadZZVik-2mVO_i8qQFkAZa7ozjJp2box1An1zQYMnG6xN6VS0lb0iuOYsb8sqfrEgZUJlZ92dRq0jwgYbhfKCtTjQcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfSQf6x0B4QHpTayjpCRuh5HCdpc_ouZowqHcVfmZk-VMk4Z7iZL_tH1dZtL7jIZmaXup9n_fNAVLT9IlxYOH8JzCe8JiN5xJ0L7zrc5fJtLRUGNBVaG33i-ZiYGHVc4WRM7Xt8UA2l-Y9SwkvUgzlFmR2FFrgWfIUXT8341zkd6J_-niSJgSCGSs3l4pnr1IUIJlSz7T9OP6P-a65PykjtvjwkBmM0gzEZMoqZvVuXrcass4ki7T2iil2Qria3ZsXnTGmgctf-dIxlvSq75suODna9SDlwcMACieFzwGAdniBCFv4uS8f00YS2WTfRK-zYLRHHa1uQMaMARdwd32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFBJ-sHVI0MDJfokji9z8jOWvKUctpJ2OBTiIxWsuXiXMGVHAmZFYh4ggWqWBHlFh-b7vIp0NDbvoEU_NiEbc0h3RmqHIFIPScskOQCljJTo6kpnMOoES5uyjL2BsN830zKVcQBIpz0xxznU0PWBv9K54aC4FV2cM6RZlyz7zrWIZHhEqyswqgMnM4M3bmTPw-X8LMDgi-4gBTmjUNJkrl_5pbsQc7BykZkyhur0Dj1qDU-Z_i4wp42jLtV4e0uZ2MdR1JaYOGDpOyx8ZMphVuIRszm0V4bSWgGttZJwtI5Qyxg-XOOBbliPT0gTFXAS58_k8fEsLhK4AppfWXm9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=DrPmEzEEB7PEtNJeWqrXYjPn4I20A-s8g-yB8TT1ckSz5gPXmao3VVpLMs0MjPUbYVPLlybrt6-FK2PBBBg5rV8r56CINtWmMHFa7tOIzy6PbeBeVX2lEGl1pXjzNzE2RrR79aDr1Z5fS3uf0EbNVQHgkK5m_XhqrSrQYG-lzd5JVNcc7OTfyrIknSrJ7Tb2UW2k2SzUnYgNut2DyP133lCxPugjreOY769k-XY-VKY3YJhmVKDfXYUysggjnIn0dlv_37VgRhfd8nYAp1MVE0JEWFHnrRISWuXW158i8IJrWb4gHM-mDaeEpXp3EKqnGp1UkXV4E9AXpxTuuncL-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=DrPmEzEEB7PEtNJeWqrXYjPn4I20A-s8g-yB8TT1ckSz5gPXmao3VVpLMs0MjPUbYVPLlybrt6-FK2PBBBg5rV8r56CINtWmMHFa7tOIzy6PbeBeVX2lEGl1pXjzNzE2RrR79aDr1Z5fS3uf0EbNVQHgkK5m_XhqrSrQYG-lzd5JVNcc7OTfyrIknSrJ7Tb2UW2k2SzUnYgNut2DyP133lCxPugjreOY769k-XY-VKY3YJhmVKDfXYUysggjnIn0dlv_37VgRhfd8nYAp1MVE0JEWFHnrRISWuXW158i8IJrWb4gHM-mDaeEpXp3EKqnGp1UkXV4E9AXpxTuuncL-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
