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
<img src="https://cdn4.telesco.pe/file/Wzhl-aKSZpAi4BFsU16T3sS3utwzg_OMZ6DIeStStyFK4sTG-DDpqVzE_t8Ztx5Zl40Ui3iHbRBWwX4W5I5yQ81TvcMW-Jmxny4XwB6lWCuDa3IrYt-V0t3cZX_4B3G2AK8eEi1XeR2xF4QD7_kBk2eAr-moeP5KDStIKiqRb933ZqZSIPNrLUX4JnG0D3BLCPCpj78FKOUsRWgK-GjJ3c8uJ6xmLDXKEl-Uk4mZPmih-kY8d5wcKZbkdw0ugP-H-_1k1gbKX55cjpa3zeP-u8Wu7lhRkqiMWjMwylf6T0pA3atrfnWQvLB_7NX5aG-n10UEZR2TPwiY7xMjRn3oqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 473K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 06:13:59</div>
<hr>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1529c155.mp4?token=XVin5omvW2qgXA2PjWr-z9W4C5BDWYlnHHYHm-1XzMe_4vv04Hqsggdb_pgPWe58NWEstbj5L1VOEY8IEaU2J-s9gIeXA63a0-WQXZDj9PrWgfmqyZEeS7uxBlBWwf8VD_SZUDnt0uA1nnP2Sv2VkC8WTeXwEf7v03BOhhWZmvrMn4GDy2726sHM7lOINTLuf_ulHSXhIJJ2Uuk2MP_oTAb4hTFh1I1W1qQQgqTq35E3koxwjgp8YduXxcbEVUy87iqtyPWkYLpsGH5TCNK0u_BNiOL79q4Obcj5JYtdEQ_-T_-x_zXS-8oJ0elPqPdZZUFZ4keH6MTZ4hVDUl_mARIz19Zro-XQ1kIMS6QdFKa09kzDon9jZGtRv9ZmOSwqIVqMiMFpWtIFwvHhVhTXUW8YUhqXpyRfcY40yHHZQBc0TzE9hc5k3TJr1CM2t1z19HtgUMHii8nXvZiW3VCN3WTwNaM8vFBdIAQ5m9KWB6Eqmw9yzh_gljT28EbzF8GIbsoshlinR6VYTbtsuuw7K5qO2lPqwDRS_SFAmi87IfFw9cJQyKcdyFvuIhvDQBLnK1q84BGLX8h2d5htRflQea1PcDHw1obOLmQZ_xs8j8vRmi4qEJsVKEodYMEpOxqtk2wEXHfbi49OkkmbDINI12uZMcQt92G7lj_MJBzMjPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1529c155.mp4?token=XVin5omvW2qgXA2PjWr-z9W4C5BDWYlnHHYHm-1XzMe_4vv04Hqsggdb_pgPWe58NWEstbj5L1VOEY8IEaU2J-s9gIeXA63a0-WQXZDj9PrWgfmqyZEeS7uxBlBWwf8VD_SZUDnt0uA1nnP2Sv2VkC8WTeXwEf7v03BOhhWZmvrMn4GDy2726sHM7lOINTLuf_ulHSXhIJJ2Uuk2MP_oTAb4hTFh1I1W1qQQgqTq35E3koxwjgp8YduXxcbEVUy87iqtyPWkYLpsGH5TCNK0u_BNiOL79q4Obcj5JYtdEQ_-T_-x_zXS-8oJ0elPqPdZZUFZ4keH6MTZ4hVDUl_mARIz19Zro-XQ1kIMS6QdFKa09kzDon9jZGtRv9ZmOSwqIVqMiMFpWtIFwvHhVhTXUW8YUhqXpyRfcY40yHHZQBc0TzE9hc5k3TJr1CM2t1z19HtgUMHii8nXvZiW3VCN3WTwNaM8vFBdIAQ5m9KWB6Eqmw9yzh_gljT28EbzF8GIbsoshlinR6VYTbtsuuw7K5qO2lPqwDRS_SFAmi87IfFw9cJQyKcdyFvuIhvDQBLnK1q84BGLX8h2d5htRflQea1PcDHw1obOLmQZ_xs8j8vRmi4qEJsVKEodYMEpOxqtk2wEXHfbi49OkkmbDINI12uZMcQt92G7lj_MJBzMjPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
به‌جز نفت، که قیمت آن از دوران دولت بایدن پایین‌تر است، دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم، چون آنها کاملاً نابود شده‌اند.
اما به‌جز نفت، قیمت همه‌چیز در حال کاهش است و روند کاهش ادامه دارد. ما بدترین تورم تاریخ کشورمان را به ارث بردیم، اما تورم اکنون به‌سرعت در حال کاهش است. کشورمان وضعیت بسیار خوبی دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/withyashar/24378" target="_blank">📅 05:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e4b6efa2.mp4?token=Doj-T78308Jj_rzBUVd6tggNTQqFZWNxtn5bmIqbkSoR-saRaA1yKWigOu9tGw8fWwXlGfMgYxCInUH-JXb-MuT_a6lijTzfni1ojTqsjChk5-lNSsCeil2CA4oLKs81co-_69Y8a6JJaJsLrHR9Bp2rKg3IjFeUlUnRo_e9WXazb26QNpZ2xi0L3z8rkVf6jkiPR8_clOtgF1ydvBL9pJx4Nk1ENGzrccZlQyNf_iTlocmKgStSQegWhM0AQGrhSAO6l2T1dYvIlCOLcnjeol12wmrTVORW_icmzLMUd9jMxTxO7cc3GdJ6RNBVMmQ9QUziHx7yuJG5yNsE7JqZYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e4b6efa2.mp4?token=Doj-T78308Jj_rzBUVd6tggNTQqFZWNxtn5bmIqbkSoR-saRaA1yKWigOu9tGw8fWwXlGfMgYxCInUH-JXb-MuT_a6lijTzfni1ojTqsjChk5-lNSsCeil2CA4oLKs81co-_69Y8a6JJaJsLrHR9Bp2rKg3IjFeUlUnRo_e9WXazb26QNpZ2xi0L3z8rkVf6jkiPR8_clOtgF1ydvBL9pJx4Nk1ENGzrccZlQyNf_iTlocmKgStSQegWhM0AQGrhSAO6l2T1dYvIlCOLcnjeol12wmrTVORW_icmzLMUd9jMxTxO7cc3GdJ6RNBVMmQ9QUziHx7yuJG5yNsE7JqZYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
می‌توانید درباره حملاتی که در بریتانیا رخ داده و مظنون مهاجری که در این ارتباط بازداشت شده، اطلاعات بیشتری بدهید؟ آیا ارتباطی با ایران وجود دارد؟
دونالد ترامپ:
ما همه چیز را درباره او می‌دانیم و به‌زودی اطلاعات بیشتری درباره این موضوع خواهید شنید.
ما آنها را گرفتیم.
@WarRoom
یاشار ، تکمیلی: تمام رسانه های جهان به اتفاق میگن کاره ایران بوده حتمأ سر نخ های پیدا شده و  عملیات توسط یک زن کشاورز که به ۳ ون مشکوک میشه و گزارش میکنه لو میره</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/withyashar/24377" target="_blank">📅 05:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74dac714cd.mp4?token=as-ojRXLu7LuMteXIY68FOro2N_UZmuUzCcmjx33NH62cNvmJ4_g1_NBcqUdElvsdFzQybEx0HKcFz9CzHEjh-ypaJf8xUMrWpo7yNns7Xvwqc7bgMM_teoaIyLA5RiGDwPaZS3dkZtQIrXGErOzIDx5SHrvqjtkKo0ZExPNlaRYOPaDd0Hf3_B50ayiZkhgH4g0Q3DnyBY-nadpatQVI3GONzvgz3HjvUnoqkp5sLW2dPYcuzom6jL0O2wuH03Rlr_FnvMp0M-C2VRbmWo51vCpOUmsbSLTE9pi92sxhebfwrC8aruK7Ve96UKZMWviy6yX-uaf041XmRVf6Vc-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74dac714cd.mp4?token=as-ojRXLu7LuMteXIY68FOro2N_UZmuUzCcmjx33NH62cNvmJ4_g1_NBcqUdElvsdFzQybEx0HKcFz9CzHEjh-ypaJf8xUMrWpo7yNns7Xvwqc7bgMM_teoaIyLA5RiGDwPaZS3dkZtQIrXGErOzIDx5SHrvqjtkKo0ZExPNlaRYOPaDd0Hf3_B50ayiZkhgH4g0Q3DnyBY-nadpatQVI3GONzvgz3HjvUnoqkp5sLW2dPYcuzom6jL0O2wuH03Rlr_FnvMp0M-C2VRbmWo51vCpOUmsbSLTE9pi92sxhebfwrC8aruK7Ve96UKZMWviy6yX-uaf041XmRVf6Vc-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ژنرال جک کین به مارک لوین در فاکس نیوز:
آمریکا و اسرائیل همین حالا
توان هوایی لازم برای تغییر چشمگیر روند درگیری در داخل ایران
را در اختیار دارند.
او پیشنهاد می‌کند معترضان ایرانی علیه
مراکز سپاه پاسداران
دست به اقدام مسلحانه بزنند و همزمان هواپیماهای آمریکایی و اسرائیلی نیز از آسمان از آنها پشتیبانی کرده و
نیروهای کمکی حکومت
را هدف قرار دهند. او می‌گوید: «
ما داریم این کار را سخت‌تر از چیزی که هست می‌کنیم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/withyashar/24376" target="_blank">📅 04:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT0ggtGAz60JZyb5-RMkQco_ZO7Wx1tTotc7tDyhn7Lt3ORcr5M_DuwcYBp5PUaRYI94fgQVMLTsANVzhYnOfNSCYzx3ebV6OXxbl4uXgxrUwgDF_LOh-0Yyfiu-XkJevxgNDYV6Ip0Sj9FXf5le8VCjnwfSQolKrSpRq48dNZCfPRfQY5AYj-gjMjjpLkOW9fbYaA24_gkLPAJV0LiDJhG338fFbJyAF3SzI19GN7Y5KcGDcR7c_jt8oJCqoJ4M3slm4BYYbZdFLXVeGEj6MVU3sggEZSAvK8Sd_b8WfmhkeJCaYabdYEnXxvJhzrfRuq6y-NvDFYcuOw3JjFDDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : بمب‌افکن‌های راهبردی بی‌-۱بی آمریکا در پایگاه فیرفورد بریتانیا؛ در انتظار فرمان احتمالی ترامپ برای دور جدید حملات به ایران! یک بالگرد رسانه‌ای که برای پوشش عملیات تیم‌های خنثی‌سازی مهمات انفجاری در منطقه ولفورد به پرواز درآمده بود، بمب‌افکن‌های…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/withyashar/24375" target="_blank">📅 04:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از تبریز دارن موشک/پهپاد میزنند اربیل عراق  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/withyashar/24374" target="_blank">📅 02:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">از تبریز دارن موشک/پهپاد میزنند اربیل عراق
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/24373" target="_blank">📅 02:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/withyashar/24372" target="_blank">📅 02:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a7eec46a.mp4?token=NARDOvGrWU0n7TJNtI_6GsTguODHrORZNz4noOZR8YgHgpRckOu1WOmXcCQy1LPohZAIIHDJ9GvQWHdBL379UrISc2ohoRU9IjHVFDczI-87rVrXiCIveG6F3Wvg41_lShTwKUu1V0ysR-v7AlqHwMB5wB0dCLd71wsfT7IMJ-4d7IH3_J7Pp0B12sb5s0Yy-ucrogTHTMPmCArtrL_qa6yXWD4c2Z83OjUTOOTgK-ZSMLwZcDUzkH4wqtbT9j0t8_DZEA7k3-k0z1V9KrWegfgnSweyJ6XB8Ijv9Kif06W_2XT8RxxK2G_7L9zoHuPL4ebgtKJluZmvYFjmS5Yjk7oSYnth-F6R5HlBgp40BYhYQKi81J05cNbQaErDOSCdOt2VwPw6EHkwnYBscSk1MJEXfko1ZmJL9RjDISmFv9TGiHTbgrUj3WjNuT16pFGLDfm8NMbW5eg1MC9HHb4i0pBL-ZudxSJZ6Y44E2irs5b_zRSW5v0842h_JaktBozt8yiJr_0r9Y_vTsfiyjFaPH_Mx8ImKEkUOnmQqaW5EDUBN-vdRK1boe2TmryovyTuvYbpQ6FtN3jzyiNR1rnItb8X0dm-UQbL8t_YHd8uAGF3FJ9pA9XAQan0FDg32PqfAXYBlV0Rjdk69fRyqlYpAMGeGRgijT-nNCu-waxEN3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a7eec46a.mp4?token=NARDOvGrWU0n7TJNtI_6GsTguODHrORZNz4noOZR8YgHgpRckOu1WOmXcCQy1LPohZAIIHDJ9GvQWHdBL379UrISc2ohoRU9IjHVFDczI-87rVrXiCIveG6F3Wvg41_lShTwKUu1V0ysR-v7AlqHwMB5wB0dCLd71wsfT7IMJ-4d7IH3_J7Pp0B12sb5s0Yy-ucrogTHTMPmCArtrL_qa6yXWD4c2Z83OjUTOOTgK-ZSMLwZcDUzkH4wqtbT9j0t8_DZEA7k3-k0z1V9KrWegfgnSweyJ6XB8Ijv9Kif06W_2XT8RxxK2G_7L9zoHuPL4ebgtKJluZmvYFjmS5Yjk7oSYnth-F6R5HlBgp40BYhYQKi81J05cNbQaErDOSCdOt2VwPw6EHkwnYBscSk1MJEXfko1ZmJL9RjDISmFv9TGiHTbgrUj3WjNuT16pFGLDfm8NMbW5eg1MC9HHb4i0pBL-ZudxSJZ6Y44E2irs5b_zRSW5v0842h_JaktBozt8yiJr_0r9Y_vTsfiyjFaPH_Mx8ImKEkUOnmQqaW5EDUBN-vdRK1boe2TmryovyTuvYbpQ6FtN3jzyiNR1rnItb8X0dm-UQbL8t_YHd8uAGF3FJ9pA9XAQan0FDg32PqfAXYBlV0Rjdk69fRyqlYpAMGeGRgijT-nNCu-waxEN3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">WarRoom with Yashar : Winter is Coming
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/24371" target="_blank">📅 01:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc92790f11.mp4?token=M3VIgMydN71VOa2-r-IlGsSHrQCkbaimLfLBpr-kfUMmRM65r1tl82W1i3C_eqfPw77bJnWSbKkJuPM0r--OPpV-MXILqpU5TeNJgUlE-fD3G4wdT7M-sFGraINpzOr64kVTug4Kz9OSgL5gJEadPrjenKQAPEjand8mWAwfwSEbLy6eVG2Vw49qNCB01tpEOA9zUZQpKAG8n_vcPMYOYmw3ZiAC7vYG26Rn308AOFpkIkMS480s9TIF-zbi2W0d87duYj7mvGxhprn43wXkDE4FbVHnkaSYU4rF21xhDzJ-SJU0_f6ofMFBxDYZuqiVl-xElDGs4TXyyoA-zPwd-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc92790f11.mp4?token=M3VIgMydN71VOa2-r-IlGsSHrQCkbaimLfLBpr-kfUMmRM65r1tl82W1i3C_eqfPw77bJnWSbKkJuPM0r--OPpV-MXILqpU5TeNJgUlE-fD3G4wdT7M-sFGraINpzOr64kVTug4Kz9OSgL5gJEadPrjenKQAPEjand8mWAwfwSEbLy6eVG2Vw49qNCB01tpEOA9zUZQpKAG8n_vcPMYOYmw3ZiAC7vYG26Rn308AOFpkIkMS480s9TIF-zbi2W0d87duYj7mvGxhprn43wXkDE4FbVHnkaSYU4rF21xhDzJ-SJU0_f6ofMFBxDYZuqiVl-xElDGs4TXyyoA-zPwd-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاسالار Daryl Caudle، رئیس عملیات نیروی دریایی: ناو هواپیمابر یو‌اس‌اس تئودور روزولت (CVN-71)، از ناوهای اتمی کلاس نیمیتز، در حال ترک سن‌دیگو برای اعزام به خاورمیانه است. این ناو به همراه گروه رزمی خود و بال هوایی یازدهم ناوگان، قرار است برای یک مأموریت طولانی‌مدت به منطقه سنتکام اعزام شود؛ مدت این مأموریت دست‌کم حدود ۷ ماه برآورد شده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/24370" target="_blank">📅 01:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX8IfMa84jl5uw12RXXS-nlOIPmlwA-nQ14qJP3mj7ML_1FL54AjqZP9rkWYlogUNBZ2I7-FyuoEwqPzVDkESu6sL_4hv0f3-gvQpPHU-7jWXg-ZeKIRhxnviPQzlmH5CDX3xKL4Jfp-qIfkk18zFlqY2150vD41iFZ0D6E4dJp4aWWYJV2MNezitMOAg-DLoqdltAW9CNmq7LYObTSFfHKEy9rGxIYPYwTS4DNhSWH0VpOBeTelZF0I5KGEq8-zzyeoP4655iyR7edRuIcDYkkY5wXQx0_Uo_vXRJmOyOsQjVdNv_i3YlVWIfXA9HoNHZZGuEpIgfqq5BTOZ_VWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با خرافات : تمام دایرکت پیغام اینه که ترامپ کلاه جنگ سرشه ( البته واقعا هم ترامپ اکثرا اتاق جنگ
مارالاگو
میره این کلاه سرشه و روز اول جنگ هم بود )
@WarRoom</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/24369" target="_blank">📅 01:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52b1b75b8.mp4?token=ghnGv6k7QYb4HTcYyTZJh0kUp5OCgp9SotDBcjRGtRQz7uz3VDcUAHqLZvKRC-VESrBqlHDfqlwuquIpSh6VIL2oEUvFBXgyi1Rw5F21CxkRdHHlbq-qEn3-1LUvf1srX8iVove9HS0tMzCIKaMo_8S9E9psT09P752LyRY4fVyaMDv2H_EyLcta3zfFm83lZY-Pl743YdamqZohs49H6tg5l5K8OXN7VFfNjxfRNKPglOqTXqT_mH89M9476pdlycueKBd0r0jNiVFJsjrSZHj-jxBp4CDvwFaDb3v_bkzgIytnBaWpRDQrvZFbBPlbewGo1HVC6PFcH_FHiDPuFVT3Vf_M_AkRyJzB_Twf8SeBHSRbxk2ZmrvOSmCgCJ-YqQZQULtsKUrzjPqpnZhE01VUmEfmD_m5_sKruejeOtdYAnPNlcE2DHomd3cng4v4a4vIVNW0igGeiZqqdNFMUrjh7VFYjiGKQ21l-9KfBgl1XggwpcsP_QhlY4iJu1Hfatwl4d0ovSQYGmi3hXHs1yBQadVbpYI0mPb7AxNuIxi7TbpcUeS-bJRsrkbbNWXn5ueP6S9mKPSsyIR3wcde55h93k3uHKQ36Axwkhg2OMluJELewD79_7ClWKVdDSshaCB-6H8Kl9W69L772KsXjmj5FqYSZgPOyMRjo_8H8o8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52b1b75b8.mp4?token=ghnGv6k7QYb4HTcYyTZJh0kUp5OCgp9SotDBcjRGtRQz7uz3VDcUAHqLZvKRC-VESrBqlHDfqlwuquIpSh6VIL2oEUvFBXgyi1Rw5F21CxkRdHHlbq-qEn3-1LUvf1srX8iVove9HS0tMzCIKaMo_8S9E9psT09P752LyRY4fVyaMDv2H_EyLcta3zfFm83lZY-Pl743YdamqZohs49H6tg5l5K8OXN7VFfNjxfRNKPglOqTXqT_mH89M9476pdlycueKBd0r0jNiVFJsjrSZHj-jxBp4CDvwFaDb3v_bkzgIytnBaWpRDQrvZFbBPlbewGo1HVC6PFcH_FHiDPuFVT3Vf_M_AkRyJzB_Twf8SeBHSRbxk2ZmrvOSmCgCJ-YqQZQULtsKUrzjPqpnZhE01VUmEfmD_m5_sKruejeOtdYAnPNlcE2DHomd3cng4v4a4vIVNW0igGeiZqqdNFMUrjh7VFYjiGKQ21l-9KfBgl1XggwpcsP_QhlY4iJu1Hfatwl4d0ovSQYGmi3hXHs1yBQadVbpYI0mPb7AxNuIxi7TbpcUeS-bJRsrkbbNWXn5ueP6S9mKPSsyIR3wcde55h93k3uHKQ36Axwkhg2OMluJELewD79_7ClWKVdDSshaCB-6H8Kl9W69L772KsXjmj5FqYSZgPOyMRjo_8H8o8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«مشکل بزرگ این است که
پالایشگاه‌های روسیه در حال منفجر شدن هستند.
این در واقع یک مشکل خاورمیانه نیست؛ بیشتر مربوط به
روسیه و اوکراین
است که با یکدیگر درگیرند.
اوکراین در حال
هدف قرار دادن پالایشگاه‌های گازوئیل روسیه
است، چون روسیه بخش زیادی از فرآوری و پالایش را انجام می‌دهد. بنابراین این موضوع واقعاً جالب است.
من با رئیس‌جمهور زلنسکی صحبت کردم و گفتم:
«باید در مورد حمله به پالایشگاه‌ها کمی دست نگه داری.»
او هم گفت:
«احتمالاً همین کار را خواهیم کرد.»
»
@WarRoom</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/24368" target="_blank">📅 01:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee5f4fc33c.mp4?token=Ub2wd0575knzowBjoectZQ_qNeBlYNClp1PZ-lhgaZOoAwm9RxUlzgXBFT_qdYVlEMOdRIEp25cKZoa6_6scOIpXdHSY7L8vML6jxIf-UeVMNwwMD7Ec43TiuugkcCnDvPQf4f80Xqj4f2pqR2wCQW8531HcrEQZg4Cu1KfrurMv5HdKhNIBxOFhImTszx2ifG_DiacVTrH2NiRCZ19RfC2liRiLXoSWymav15tGJm8MaugeeVp8UdHBiGJ9B9ktXW1ReT4arAqn-05QxjZld7ZpZBG7sBlMOXnmHdihG-LqPPPVtbVABLM9ze-B8hTHzr1UARirC6itd5x63hcZVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee5f4fc33c.mp4?token=Ub2wd0575knzowBjoectZQ_qNeBlYNClp1PZ-lhgaZOoAwm9RxUlzgXBFT_qdYVlEMOdRIEp25cKZoa6_6scOIpXdHSY7L8vML6jxIf-UeVMNwwMD7Ec43TiuugkcCnDvPQf4f80Xqj4f2pqR2wCQW8531HcrEQZg4Cu1KfrurMv5HdKhNIBxOFhImTszx2ifG_DiacVTrH2NiRCZ19RfC2liRiLXoSWymav15tGJm8MaugeeVp8UdHBiGJ9B9ktXW1ReT4arAqn-05QxjZld7ZpZBG7sBlMOXnmHdihG-LqPPPVtbVABLM9ze-B8hTHzr1UARirC6itd5x63hcZVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
آیا انجام حملات پیش از انتخابات میان‌دوره‌ای هنوز روی میز شماست؟
ترامپ:
«نمی‌خواهم درباره آن چیزی بگویم. منظورم این است که
ممکن است چنین اتفاقی بیفتد
، اما نمی‌خواهم بیشتر از این درباره‌اش صحبت کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/24367" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc59060499.mp4?token=EdxcjjFLC7Ff2iRK0hMhZXOj_zmhosFD72x8hCd4H7-wbYUHExm_qWcNOi1JY8hZziQn4CfEhzedleg-noVW3it-B-bIUjF1q7ggG6QSDzUe3vXj1uU1a8mo6xV3Twfim4CxKHE6XGE9Hdu-E3bdI38wgclw6EH6YeAyP960eJxxP-qgc7qiUtdwh7jI2A05iQyGiK4P1G-jSOJxtwcM_GinPFDb8mM-NkLOvw8VioxRnaKHnfwL7oVdoXu2OBOd2LeDscanw5w37wFdSXrozhBUtt3dCu9eju_MEIrbjBKybJ7Kw3GqCxPccE4lgE9bxbygsOVDLiRnA4fHK-7NXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc59060499.mp4?token=EdxcjjFLC7Ff2iRK0hMhZXOj_zmhosFD72x8hCd4H7-wbYUHExm_qWcNOi1JY8hZziQn4CfEhzedleg-noVW3it-B-bIUjF1q7ggG6QSDzUe3vXj1uU1a8mo6xV3Twfim4CxKHE6XGE9Hdu-E3bdI38wgclw6EH6YeAyP960eJxxP-qgc7qiUtdwh7jI2A05iQyGiK4P1G-jSOJxtwcM_GinPFDb8mM-NkLOvw8VioxRnaKHnfwL7oVdoXu2OBOd2LeDscanw5w37wFdSXrozhBUtt3dCu9eju_MEIrbjBKybJ7Kw3GqCxPccE4lgE9bxbygsOVDLiRnA4fHK-7NXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
درباره ممنوعیت صادرات گازوئیل چطور؟
ترامپ:
«ما این موضوع را
خیلی جدی در حال بررسی
هستیم. چنین اقدامی گاهی می‌تواند باعث
افزایش جزئی قیمت بنزین خودروها
شود.
بنابراین با جدیت در حال بررسی آن هستیم و
ممکن است این کار را انجام دهیم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/24366" target="_blank">📅 01:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آکسیوس: تحرکات و آماده‌سازی‌های نظامی آمریکا در منطقه، احتمال اقدام نظامی جدید علیه ایران را افزایش داده است.
ترامپ نیز گفته همچنان گزینه ازسرگیری حملات علیه ایران را در نظر دارد
@WarRoom</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/24365" target="_blank">📅 01:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f7397463.mp4?token=TC77PPT3TjdmzlIqZ-oti6wRdLcN3CQVeCEmRh9qFUGH4d-0Okv2D_Rk5DU2O5iXHF58whtB6PwDn5KVRR8jThLHMwmGm3Lia_HNTuRBO3cq9RxALxSXsHTMyFvgPER38WQFhdnrhUpJ3fHQ3OHvKrwni0figsON9VO6bpvmFNLnaAQBeRfQkOixi-HQo5Dq0BC2V02t2U_OrIY_yiPYWSfASbxUHtfXL1yqi7dfoo_QRpjJV3DBupZAi0b3e-uRYm844qD95qsZl_JTeaypxe26-4uXn-Wn52oRshEt445Tak5-A5rj0IQji33Qvi_PL58WGUmSLMKsdG6VpSq47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f7397463.mp4?token=TC77PPT3TjdmzlIqZ-oti6wRdLcN3CQVeCEmRh9qFUGH4d-0Okv2D_Rk5DU2O5iXHF58whtB6PwDn5KVRR8jThLHMwmGm3Lia_HNTuRBO3cq9RxALxSXsHTMyFvgPER38WQFhdnrhUpJ3fHQ3OHvKrwni0figsON9VO6bpvmFNLnaAQBeRfQkOixi-HQo5Dq0BC2V02t2U_OrIY_yiPYWSfASbxUHtfXL1yqi7dfoo_QRpjJV3DBupZAi0b3e-uRYm844qD95qsZl_JTeaypxe26-4uXn-Wn52oRshEt445Tak5-A5rj0IQji33Qvi_PL58WGUmSLMKsdG6VpSq47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار فاکس‌نیوز:
فکر می‌کنید این جنگ با ایران را از طریق
جنگ اقتصادی
که وزارت خزانه‌داری به راه انداخته پیروز می‌شویم یا از طریق حملات نظامی؟
ترامپ:
فکر می‌کنم
هر دو
. از هر دو طریق پیروز خواهیم شد. از نظر نظامی، واقعاً
تا حد زیادی پیروز شده‌ایم
، اما این به این معنا نیست که حملات را متوقف کرده‌ایم.
ما قطعاً
با اختلاف زیادی در حال پیروز شدن هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/24364" target="_blank">📅 00:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852e1be8f8.mp4?token=kC2HXh6827Yqjtc8loYycJWmjpyS5pf1eGgunKm_SUmoDfuEiceiLFI6aETVbzkUAfiTswYnESPHVUsPa4WS7n8as0jVTrbsgeUCPLjg_rqkma364woXUNHonBDHRO7wcewxxM84M6mcrD03OtwR3MYXRYrQRf-SnA5Wj0-NEODiz1x1KmhGDNo1MK0iEOACwuup45xTf1zpjVVwbnmAtCgD1w7c00ErfutDF6XfNytPvw8mxqZ0rdDe4MggRS7xGHCZzxwy-h7MaTbEkFjzk070ElzXm-IpprW-JjLeZWqUabDhK4R9aEhkONR8cFoxncrfId8F5dtdPGDSol-Jkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852e1be8f8.mp4?token=kC2HXh6827Yqjtc8loYycJWmjpyS5pf1eGgunKm_SUmoDfuEiceiLFI6aETVbzkUAfiTswYnESPHVUsPa4WS7n8as0jVTrbsgeUCPLjg_rqkma364woXUNHonBDHRO7wcewxxM84M6mcrD03OtwR3MYXRYrQRf-SnA5Wj0-NEODiz1x1KmhGDNo1MK0iEOACwuup45xTf1zpjVVwbnmAtCgD1w7c00ErfutDF6XfNytPvw8mxqZ0rdDe4MggRS7xGHCZzxwy-h7MaTbEkFjzk070ElzXm-IpprW-JjLeZWqUabDhK4R9aEhkONR8cFoxncrfId8F5dtdPGDSol-Jkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«فکر می‌کنم اتفاقی که خواهد افتاد این است که
خیلی زود در این جنگ پیروز خواهیم شد
و به‌محض اینکه پیروز شویم، قیمت نفت
به‌شدت کاهش پیدا می‌کند
و به سطحی که پیش از جنگ داشت، برمی‌گردد.
و نکته کلیدی این است که
ایران سلاح هسته‌ای نخواهد داشت.
این، کلید حل این مسئله است.»
@WarRoom</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/24363" target="_blank">📅 00:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">معاون پزشکیان: برای عبور از زمستان به همراهی مردم نیاز داریم.
@WarRoom
Yashar : Winter is coming</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24362" target="_blank">📅 23:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الجزیره : تنش در تنگه هرمز پس از رد پیشنهاد ایران ادامه دارد.
الجزیره گزارش داده پس از رد طرح تهران، نگرانی‌ها درباره ازسرگیری درگیری مستقیم افزایش یافته است. همچنین
گزارش‌هایی از انفجار در
محدوده
تنگه هرمز
خبر میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/24361" target="_blank">📅 23:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صدای انفجار در تنگه  @WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24360" target="_blank">📅 23:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a093c8ddbb.mp4?token=I9jml45BQFP-p8RJxGUl7b9Pn6A3aqNVVdW150NJWZsYKuIJfqTBDbeNHRbCXYRWoOQ2CajfgEGi2v07qqrTOrQzVdsZcGXHIfZ84s2lxY1zy2FoX9Pzao8NPbC_0y2_7RnCiWg5GlAn05tCC-6ip93cyjLXhhoSUTnRlOeTlNt3XEHgri5jT9YuHmHQHJ1xDHcd-ydvTqJt1vgog-39WmcZKleU1iihHlNlsqQaRc4qvwtVC4wOkrle1F555NSzMKGmkUJ-zj-ibnPGqaTEmD0YN7QYOiDVozTAZvIEEBG3ryXaTqSRKCFc5dkWoE7-sinUt0nWe4o1quMbqTcX2CR53dUpZXyMByfVyvJZ9LhEh1-Dcqwjxd64gea_9tMG8UyUIqcW5Z7Gk3l3TXcNCjRG3SZCji8SPhcCeJzkBy3TDHK9AqeUFOOsOGVe0CUKJrKFfmWVgRMHd3ghNXDWNFuP2iaALgyRF3lkrgCa5UYXuaqEQCze7LhHHiS87MBrfOOhwWlRVuM-MDQPtiuNGhuzi7MN_hs9WdzgOP2PEapIqi17TcwuDltmWW31XyCK_r7Gkbmg7OOUDgFNX03c_FLtaW4raOm_w3odFOcUJn75LpxEZxE4vgrdyjsopMt2Eo0M4stvIrCZnIvYR8-8IjafPfVoAfWOURO1BnW9WQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a093c8ddbb.mp4?token=I9jml45BQFP-p8RJxGUl7b9Pn6A3aqNVVdW150NJWZsYKuIJfqTBDbeNHRbCXYRWoOQ2CajfgEGi2v07qqrTOrQzVdsZcGXHIfZ84s2lxY1zy2FoX9Pzao8NPbC_0y2_7RnCiWg5GlAn05tCC-6ip93cyjLXhhoSUTnRlOeTlNt3XEHgri5jT9YuHmHQHJ1xDHcd-ydvTqJt1vgog-39WmcZKleU1iihHlNlsqQaRc4qvwtVC4wOkrle1F555NSzMKGmkUJ-zj-ibnPGqaTEmD0YN7QYOiDVozTAZvIEEBG3ryXaTqSRKCFc5dkWoE7-sinUt0nWe4o1quMbqTcX2CR53dUpZXyMByfVyvJZ9LhEh1-Dcqwjxd64gea_9tMG8UyUIqcW5Z7Gk3l3TXcNCjRG3SZCji8SPhcCeJzkBy3TDHK9AqeUFOOsOGVe0CUKJrKFfmWVgRMHd3ghNXDWNFuP2iaALgyRF3lkrgCa5UYXuaqEQCze7LhHHiS87MBrfOOhwWlRVuM-MDQPtiuNGhuzi7MN_hs9WdzgOP2PEapIqi17TcwuDltmWW31XyCK_r7Gkbmg7OOUDgFNX03c_FLtaW4raOm_w3odFOcUJn75LpxEZxE4vgrdyjsopMt2Eo0M4stvIrCZnIvYR8-8IjafPfVoAfWOURO1BnW9WQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس با لباس غیرنظامی از داخل خانه‌ها خمپاره و موشک شلیک می‌کنند.و بعد پس از کشته‌شدن این افراد در حملات اسرائیل، آنان را غیرنظامی معرفی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24359" target="_blank">📅 23:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تایمز آو اسرائیل:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل،
امروز به ابوظبی سفر کرد تا با شیخ محمد بن زاید، رئیس امارات متحده عربی، دیدار کند.
این سفر با یک هواپیمای خصوصی انجام شده و نتانیاهو روز را در ابوظبی سپری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24358" target="_blank">📅 22:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حمله درست و تند مجری انگلیس به وزیر دفاع انگلستان پس از خنثی شدن طرح حمله به پایگاه هوایی مشترک انگلیس/و امریکا فرفورد:
‏“باید میان اعزام تروریست‌ها از
سوی ایران
و ورود آنها از طریق قایق‌های مهاجران غیرقانونی، رابطه‌ای مستقیم برقرار کنید. به شما هشدار داده بودند، اما شما به‌جای اقدام، برای سپاهی ها هتل گرفتید. این افراد احتمالا از جای دیگری، مشخصابا هدف اجرای این عملیات، وارد کشور شده‌اند
‏هنوز متوجه نشدید که اگر یک دولت متخاصم باشید، یکی از بهترین روش‌ها برای وارد کردن عوامل خود، فرستادن آنها به‌صورت غیرقانونی با قایق ست”
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24357" target="_blank">📅 22:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه سعودی
Ajel
به نقل از
سخنگوی نیروهای مسلح دولت یمن، سرتیپ ماجد عبدالله النزیلی
: عملیات ۷۲ ساعت گذشته ما باعث کشته و زخمی‌شدن ۲۳۱۶ نیروی حوثی، از جمله
چهار متخصص ایرانی در عملیات پهپادی و موشکی در استان تعز
شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24356" target="_blank">📅 21:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کانال 15 اسرائیل:
مذاکرات پیشرفت چشمگیری نداشته و میانجی‌گران از مواضع طرف ایرانی ناامید شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24355" target="_blank">📅 21:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">لحظه هلاکت و متلاشی شده تروریستی که نوآ ارگامان را در ۷ اکتبر ربوده بود
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24354" target="_blank">📅 21:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رویترز، آخرین وضعیت فیرفورد : بامداد یکشنبه، ۵ مرد پس از مشاهده سه خودروی مشکوک در نزدیکی پایگاه هوایی فیرفورد انگلیس بازداشت شدند. ترامپ اعلام کرد مظنونان از قبل تحت نظر آمریکا و انگلیس بودند و پس از نزدیک‌شدن به منطقه پایگاه دستگیر شدند؛ هرچند جزئیات عملیات مراقبت هنوز کاملاً روشن نیست. در جریان تحقیقات، مواد مشکوکی از خودروها توقیف شد و تیم خنثی‌سازی بمب ارتش وارد عمل شد. به‌دلیل احتمال انفجار، حدود ۸۵ خانه تخلیه شدند. فیرفورد پایگاه مورد استفاده بمب‌افکن‌های آمریکایی در حملات علیه ایران است و سپاه پیش‌تر درباره استفاده از آن هشدار داده بود. آخرین وضعیت: هر پنج نفر همچنان در بازداشت پلیس ضدتروریسم هستند؛ اما وجود بمب آماده انفجار، هویت و وابستگی مظنونان و ارتباط احتمالی آن‌ها با ایران هنوز رسماً تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24353" target="_blank">📅 20:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c011d84cee.mp4?token=ggqhPiZY9NONVkHkts5f9QWoCjNqMXbZ_Y1OWnhH-Gz5GM2fiF8YWOsfkuG4wHxr_LtxQ1jMVRvVZk3IDC4z-NO_E0N9F8vXL1e6XshxU94iPpZfev-ZY9n3rOrzuTThEypEUBSAbUcDaMNdPYm_1QCLczoS32FhWFKCEjG9DowpH14JUXF64_8rykyulEufyNTC9m-mVQ9ycM0DIA4EtqyEhAqEpGudOQYBrNVNLGuyTwXLdrvv89zyoFCExKM_XNdVMc1PUP3_FnsYkBs-H8t2r06b-RJeqbQogLseSfH5gjPh5rRxk4XlN5zDs6ZEVtGduwmAKed94g1X9RIWIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c011d84cee.mp4?token=ggqhPiZY9NONVkHkts5f9QWoCjNqMXbZ_Y1OWnhH-Gz5GM2fiF8YWOsfkuG4wHxr_LtxQ1jMVRvVZk3IDC4z-NO_E0N9F8vXL1e6XshxU94iPpZfev-ZY9n3rOrzuTThEypEUBSAbUcDaMNdPYm_1QCLczoS32FhWFKCEjG9DowpH14JUXF64_8rykyulEufyNTC9m-mVQ9ycM0DIA4EtqyEhAqEpGudOQYBrNVNLGuyTwXLdrvv89zyoFCExKM_XNdVMc1PUP3_FnsYkBs-H8t2r06b-RJeqbQogLseSfH5gjPh5rRxk4XlN5zDs6ZEVtGduwmAKed94g1X9RIWIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری‌که سپاه تنگه رو بسته و دیگه خودشم کلید نداره مونده پشت در ، و صدا هایی که هر شب میاد
@WarRoom
😂</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24351" target="_blank">📅 20:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صدای انفجار در تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24350" target="_blank">📅 20:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5a52224fd.mp4?token=CsHhd_fWddMNWw22uHbKFgjuqZDE_gunK4V1xsxzAXoA5vvppIk2XIwx1yedW3SVjdYVFu2g7jhiD5npNOHd4xbszV53e37kPelYEAqwduwmCXbzZdNJG1CXZd5cxInYpda4nS-40trNMf6YpyUSB601rQaZy4QYobugBjLCmgbXoii4CNCJJl8Vche9Zw7QohW_K4PJUdojqENvGpK20gxLDbN8vkh8FJVV4h3dxAF1CqCO1KD6g_bbE9qAP6_Q5XQH_3r8ti9x2L5toBSwh7zXHM4_Q6wlu-g0ihVSG-AV_cziGZrxxlRLOUYObt0pmil4kNJ5jTpp2MWSJy4Cxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5a52224fd.mp4?token=CsHhd_fWddMNWw22uHbKFgjuqZDE_gunK4V1xsxzAXoA5vvppIk2XIwx1yedW3SVjdYVFu2g7jhiD5npNOHd4xbszV53e37kPelYEAqwduwmCXbzZdNJG1CXZd5cxInYpda4nS-40trNMf6YpyUSB601rQaZy4QYobugBjLCmgbXoii4CNCJJl8Vche9Zw7QohW_K4PJUdojqENvGpK20gxLDbN8vkh8FJVV4h3dxAF1CqCO1KD6g_bbE9qAP6_Q5XQH_3r8ti9x2L5toBSwh7zXHM4_Q6wlu-g0ihVSG-AV_cziGZrxxlRLOUYObt0pmil4kNJ5jTpp2MWSJy4Cxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلاصه کامل صحبتهای ،
عباس عراقچی، وزیر خارجه
رژیم
، با شبکه NBC:
ما
کاملاً آماده ازسرگیری جنگ هستیم
و در برابر هرگونه تجاوز جدید، حتی اگر به
«جنگ آخرالزمانی»
منجر شود، ایستادگی می‌کنیم؛ اما همزمان
برای دیپلماسی آماده‌ایم و انتخاب با ترامپ است.
ترامپ در جنگ قبلی خواستار
تسلیم بدون قیدوشرط ایران در دو روز
بود، اما اکنون
هشت ماه است جنگ ادامه دارد و نتیجه‌ای نداشته است.
یک
طرح منطقی برای توافق
روی میز است و با وجود اینکه ترامپ آن را رد کرده، ما همچنان منتظر
پاسخ رسمی آمریکا از طریق میانجی‌ها
هستیم. ما به
انتخابات میان‌دوره‌ای آمریکا اهمیتی نمی‌دهیم و منافع ملی ایران برایمان مهم است.
غنی‌سازی
۶۰ درصد غیرقانونی نیست
و برای اهداف صلح‌آمیز انجام می‌شود؛ ما NPT را نقض نکرده‌ایم و مسائل باقی‌مانده را می‌توان از طریق مذاکره حل کرد.
جنگ راه‌حل نیست.
برای بازگشایی هرمز نیز
طرح هفت‌روزه‌ای
ارائه کرده‌ایم: آمریکا طی چهار یا پنج روز اقدامات موردنظر را انجام دهد،
روز ششم تنگه باز شود و روز هفتم مذاکرات برای توافق نهایی از سر گرفته شود.
همچنین در داخل ایران
چند مرکز قدرت وجود ندارد
؛ دولت، سپاه، شورای عالی امنیت ملی، مجلس و وزارت خارجه
همه در یک جبهه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24349" target="_blank">📅 19:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782b0a03b2.mp4?token=jiCBOQNPV_IsPjQtqPn1NR5wKRIk4NAdqaFkdYQYdB87ABPO1Omg3RBDM0WSjm7kW0jwUsGZkGojlxmf8GsqgGlGEU5nVuJEhpXz_50G6eJT4VQXHIaDvBWl9_S3EZwyfgYunpvIrUGk2RSt2VWTwNEj9hDIfZQkQrA6ZhcwsuEM0VjJLJ8Yi1a_pB7R9y-UH23YvW05m6_lVP3_dwU8KHBPXldf1KzQxwK8m0nCoEB9YbrfJhfvGBCd_5NFEKiEAro9cI4yTpAZppsaGXLG7Ec-ZEiGqnMatBPB1h7x7xVXRiwl9iejalP6p-nw2qxKLUkJQM1DEulTTog918kMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782b0a03b2.mp4?token=jiCBOQNPV_IsPjQtqPn1NR5wKRIk4NAdqaFkdYQYdB87ABPO1Omg3RBDM0WSjm7kW0jwUsGZkGojlxmf8GsqgGlGEU5nVuJEhpXz_50G6eJT4VQXHIaDvBWl9_S3EZwyfgYunpvIrUGk2RSt2VWTwNEj9hDIfZQkQrA6ZhcwsuEM0VjJLJ8Yi1a_pB7R9y-UH23YvW05m6_lVP3_dwU8KHBPXldf1KzQxwK8m0nCoEB9YbrfJhfvGBCd_5NFEKiEAro9cI4yTpAZppsaGXLG7Ec-ZEiGqnMatBPB1h7x7xVXRiwl9iejalP6p-nw2qxKLUkJQM1DEulTTog918kMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل گیتس درباره جفری اپستین:
بعد از آشنایی، اپستین گفت می‌تواند برای
سلامت جهانی میلیاردها دلار جمع‌آوری کند
؛ بدون دریافت پول یا داشتن نقشی در این کار. اما این طرح
کاملاً به بن‌بست رسید.
گیتس گفت وقت گذراندن با اپستین، مانند بسیاری افراد دیگر، به
اعتبار او کمک کرد و این موضوع بسیار تأسف‌بار است.
او تأکید کرد که در آن دیدارها
هیچ زنی حضور نداشت، هیچ ارتباط مالی وجود نداشت و هرگز به جزیره اپستین نرفته است.
گیتس همچنین گفت ناکامی دولت در پرونده فلوریدا برای
اعمال مجازات و شناسایی اتفاقات در حال وقوع، یک شکست باورنکردنی نظام قضایی
بود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24348" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24347">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مجری NBC: آیا درست است که ترامپ در حال آماده‌شدن برای ازسرگیری حملات نظامی پس از انتخابات میان‌دوره‌ای است؟  مایک والتز، نماینده آمریکا در سازمان ملل: این گزارش‌ها بر اساس منابع ناشناس است.آنچه می‌توانم بگویم این است که رئیس‌جمهور همه گزینه‌ها را روی میز نگه…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24347" target="_blank">📅 19:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24346">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bae950f91.mp4?token=RAY7M8bolfeeZGeyxsYDiMUoCui4hHsUIBlcifDR7d-Y8AIGceDuYdo9kMr5Jxrw_0oLi7e2FHjM6uA1F7KTJQL3nRxcUu9XEeD44w9tmhxEymKpTz_apslHOTwMRhjqMwMlpLTo-zXX0UeV2NC7uehbX9O30r7VduTBS60UyzVbzFWyL23h5yWZCp16bPh00xB9hsqgkrmsJr0HjF2royGZ6kp0YXsNKH3LSOJLD6TgXrK9etnG09jrQIvnq7hZVWYImlCEOmxDXCK_8O_23rzMKOYhxlQVfvIrw7RTmULckkWFlT5DAVJ9-xho2KILtGoPXiLJ_MVscdi7ftVJPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bae950f91.mp4?token=RAY7M8bolfeeZGeyxsYDiMUoCui4hHsUIBlcifDR7d-Y8AIGceDuYdo9kMr5Jxrw_0oLi7e2FHjM6uA1F7KTJQL3nRxcUu9XEeD44w9tmhxEymKpTz_apslHOTwMRhjqMwMlpLTo-zXX0UeV2NC7uehbX9O30r7VduTBS60UyzVbzFWyL23h5yWZCp16bPh00xB9hsqgkrmsJr0HjF2royGZ6kp0YXsNKH3LSOJLD6TgXrK9etnG09jrQIvnq7hZVWYImlCEOmxDXCK_8O_23rzMKOYhxlQVfvIrw7RTmULckkWFlT5DAVJ9-xho2KILtGoPXiLJ_MVscdi7ftVJPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری NBC
:
آیا درست است که ترامپ در حال آماده‌شدن برای ازسرگیری حملات نظامی پس از انتخابات میان‌دوره‌ای است؟
مایک والتز، نماینده آمریکا در سازمان ملل:
این گزارش‌ها بر اساس منابع ناشناس است.آنچه می‌توانم بگویم این است که
رئیس‌جمهور همه گزینه‌ها را روی میز نگه خواهد داشت
تا اطمینان حاصل کند جهان از اینکه ایران با در اختیار داشتن یک سلاح هسته‌ای، جهان را گروگان بگیرد، در امان باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24346" target="_blank">📅 19:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آکسیوس:
میانجی‌های قطری در آخر هفته به‌صورت جداگانه بین مذاکره‌کنندگان ایران و آمریکا در رفت‌وآمد بوده‌اند و درباره
تغییرات متن توافق پیشنهادی
گفت‌وگو کرده‌اند.
انتظار می‌رود مقام‌های قطری در صورت ادامه روند،
از روز دوشنبه به‌صورت جداگانه با عباس عراقچی و استیو ویتکاف
دیدار کنند
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24345" target="_blank">📅 19:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران خواهان توافق است، اما توافقی ایرانیا میخوان با توافقی که ما میخوایم فرق داره
ترامپ همچنین گفت :
اون ایرانیا در مذاکرات «زیاده‌روی کردن»!!!
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24344" target="_blank">📅 19:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آکسیوس:
ترامپ درباره احتمال ازسرگیری حملات آمریکا به ایران گفت:
«همیشه به آن فکر می‌کنم.»
او در پاسخ به این پرسش که آیا حملات مجدد را بررسی می‌کند، این جمله را بیان کرد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24343" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24342">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آکسیوس , باراک راوید:
منابع مطلع می‌گویند مذاکره‌کنندگان آمریکایی به ایران اعلام کرده‌اند
تهران حق ندارد برای تنگه هرمز شرط تعیین کند
و آمریکا معتقد است ایران کنترل انحصاری بر این آبراه ندارد. این موضع یکی از اصلی‌ترین اختلافات فعلی در مذاکرات غیرمستقیم است.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24342" target="_blank">📅 19:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پروازهای ایران همچنان به ۱۰ کشور برقرار است
چین، روسیه، ترکیه، افغانستان، پاکستان، ارمنستان، بلاروس، تاجیکستان، ویتنام و مالزی
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/24341" target="_blank">📅 19:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرنگار سی‌بی‌اس:
یک مقام ایرانی به من گفته است که
مذاکرات ایران و آمریکا که قرار بود روز دوشنبه برگزار شود، لغو شده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24340" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24339">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران: «ما اکنون رئیس‌جمهوری داریم که چینی‌ها برای او احترام قائل‌اند. چین کمک‌های خود به ایران را به‌طور قابل‌توجهی کاهش داده است. تنها حدود ۱۵ میلیون بشکه دیگر از نفت ایران روی آب قرار دارد و پس از آن، ایران دیگر…</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/24339" target="_blank">📅 19:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24338">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ در مورد حادثه رخ داده در پایگاه هوایی بریتانیایی فیرفورد: دستگیری‌ها در بریتانیا فوق‌العاده بود. همکاری با بریتانیا شگفت‌انگیز بود. آن‌ها قصد داشتند آسیب جدی به پایگاه ما وارد کنند، و همکاری با بریتانیایی‌ها به نحو احسن پیش رفت @WarRoom</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/24338" target="_blank">📅 19:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bac83090.mp4?token=HQI1uegmYHbzJTTlTe8dXloK8-mv0Ki1kwllm-vGAdcFL-iWcCDgQohIIVLSZ04keKcNhVrLy0kUCbcSEmCRb9DWeBGAyn8zYNm643DZKMRIkZw-mY5wgwMlrtvWV03LyePEGrxT1vdtw0dbpKEem2rZMClZyPMj2W4sQGrwwQ2AQ2emQhGzxErMtSm9hXrEbue4KBhwpm-ryNx1IGKzXU9kkGJkhtb84HeLeY2rW2em9CfT-zRpZ86vlKGBXAREp0JUYQ21iw8LtIPkd-Fw9bq-anlDkMbmBW025eIrLplk4SwKXNsSWA6YiFftzjwOuYg5kS-kruyoKq8rAbNMEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bac83090.mp4?token=HQI1uegmYHbzJTTlTe8dXloK8-mv0Ki1kwllm-vGAdcFL-iWcCDgQohIIVLSZ04keKcNhVrLy0kUCbcSEmCRb9DWeBGAyn8zYNm643DZKMRIkZw-mY5wgwMlrtvWV03LyePEGrxT1vdtw0dbpKEem2rZMClZyPMj2W4sQGrwwQ2AQ2emQhGzxErMtSm9hXrEbue4KBhwpm-ryNx1IGKzXU9kkGJkhtb84HeLeY2rW2em9CfT-zRpZ86vlKGBXAREp0JUYQ21iw8LtIPkd-Fw9bq-anlDkMbmBW025eIrLplk4SwKXNsSWA6YiFftzjwOuYg5kS-kruyoKq8rAbNMEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«ما اکنون رئیس‌جمهوری داریم که چینی‌ها برای او احترام قائل‌اند. چین کمک‌های خود به ایران را به‌طور قابل‌توجهی کاهش داده است. تنها حدود
۱۵ میلیون بشکه دیگر از نفت ایران روی آب قرار دارد
و پس از آن، ایران دیگر چیزی برای مبادله با دیگران نخواهد داشت. احتمالاً طی
دو هفته آینده
آخرین محموله‌های نفت ایران به چین تحویل داده می‌شود و پس از آن چیزی باقی نخواهد ماند. ایرانی‌ها می‌گویند در صورت دستیابی به توافق، تنگه هرمز را باز خواهند کرد؛
تنگه همین حالا باز است.
»
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24337" target="_blank">📅 19:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6805c8bfd.mp4?token=PLJR-z9UCZRRnfv2KBaZJuENBDhFSXyn-uf-p08evZ13__gG6mHhIf3I7EuMEMpgKlaKfAW1mnUJThuXc9W_q06oguA6UNXUswCZIeY2IhrJQNYqg8BZVGGCq8rPafmnVBBFYKmIMkD9mQhO44OtUN32CnKyAtipE-8Z0tHPKp9zNa_pDEhkyPqCFscfZXPIDhr7q2EoKNB8PkHeabb0pWkhwh0mic3Kdshzj8h8AfaWO1HarBo6uHokaufL2q0m5Tp1G-5gQYgn0Wj3VS7dt98sMTdgmxlTef3NNmETNqPynRPltjUKRrFfvzeLfc8hMpQVmHazL602dx97Vzhdsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6805c8bfd.mp4?token=PLJR-z9UCZRRnfv2KBaZJuENBDhFSXyn-uf-p08evZ13__gG6mHhIf3I7EuMEMpgKlaKfAW1mnUJThuXc9W_q06oguA6UNXUswCZIeY2IhrJQNYqg8BZVGGCq8rPafmnVBBFYKmIMkD9mQhO44OtUN32CnKyAtipE-8Z0tHPKp9zNa_pDEhkyPqCFscfZXPIDhr7q2EoKNB8PkHeabb0pWkhwh0mic3Kdshzj8h8AfaWO1HarBo6uHokaufL2q0m5Tp1G-5gQYgn0Wj3VS7dt98sMTdgmxlTef3NNmETNqPynRPltjUKRrFfvzeLfc8hMpQVmHazL602dx97Vzhdsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد حادثه رخ داده در پایگاه هوایی بریتانیایی فیرفورد: دستگیری‌ها در بریتانیا فوق‌العاده بود. همکاری با بریتانیا شگفت‌انگیز بود.
آن‌ها قصد داشتند آسیب جدی به پایگاه ما وارد کنند، و همکاری با بریتانیایی‌ها به نحو احسن پیش رفت
@WarRoom</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/24336" target="_blank">📅 18:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f3c2ed42c.mp4?token=cPH1E78UAgN5SEf2iTCYRyDc7z7msy-047JOoM_nhAf4ft4LajxPAWTSd4SjqqUCr13okJWs5wwPT_U08k-AXKU3V3_VShrdAlGmkFm1SZf4H8CE_gEWU2bswhFd-aaYSJbPYAWO_wdJ7q__Rc9adX8yLBh77ea-AJ9KDepHY-zUly1STD9iI9NFElAUBEvMTdGWD7ZaZjVqxxh37nfGPImp5RSZ2c9fia0r79-meK66JNkOlJaJ46Sv8GDh0OmpNneHSzVfKkNBbGSe98Sqi8xtfWgM-m7v92V5BryecOtLXTLUeWLBFHet1Gv2Ta_kQpuEetcn87VODXil3rsUmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f3c2ed42c.mp4?token=cPH1E78UAgN5SEf2iTCYRyDc7z7msy-047JOoM_nhAf4ft4LajxPAWTSd4SjqqUCr13okJWs5wwPT_U08k-AXKU3V3_VShrdAlGmkFm1SZf4H8CE_gEWU2bswhFd-aaYSJbPYAWO_wdJ7q__Rc9adX8yLBh77ea-AJ9KDepHY-zUly1STD9iI9NFElAUBEvMTdGWD7ZaZjVqxxh37nfGPImp5RSZ2c9fia0r79-meK66JNkOlJaJ46Sv8GDh0OmpNneHSzVfKkNBbGSe98Sqi8xtfWgM-m7v92V5BryecOtLXTLUeWLBFHet1Gv2Ta_kQpuEetcn87VODXil3rsUmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
شب گذشته، رکورد تازه‌ای در انتقال نفت از تنگه هرمز ثبت کردیم؛ حتی بیشتر از میزان نفتی که پیش از آغاز جنگ از این مسیر عبور می‌دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24335" target="_blank">📅 16:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8efbe7394.mp4?token=g03fXxAhdgZrpCCqfhtCslX7RsGLuhcv-4705zu3OuNUb6eKVhQljOa4W8lIFTx5OdterccrfARAMgzbzcRXhtCV8mLweSwIDlF7oPcvKFJPCnbyld_oCi4RcTDLjWEC4HwZXJ2UwRkOZBLCA6xC2S4vyfN1g52zBPJpbCK53MH7hCLtc8BL51x1xYXNhuTMXLw-1OhWJt2nQo7P8URCVecRHn-0f9XlXdkRJBF_tCdL49TeaEfl9GQL3_JHkByzZUEzjQXNdW8f1IpUxorwkFbPyc4Oq7jSaGKmiPATLmbn9vjQ7Cm1Qkj73uV-FrMjOs-tcvQtdrr3MHdPa7dlv4T2vPTRM3X4_oBQcmdlNn9A3pVFTlDpxI2M2ps4TujHqkOuXkTr7r6UeWQWHIWUaVyiurbaxZ2nMHykU6daZFFjOPnGCoS22EPTrrm8l4ES8aBF6LvRiWuQM15p5LBSIGb4lRDBHyPYD9tqBb6kDdlN2Due_NSivK4mBGHamVt6mtXfVRzdepOBg11mfmgwxI3hWaJ3_14U3hnJ-pV_euNHEtVZOO0c5xY_gJ3OjOFbd1mrxfXVTSd2xCd7r1xRD3RdswRKnIlEwPkY8omjjKiI8HnYM3nHcTG0gh8pZG9B7-i_Z-duJCBvP7IxFtK8c3f43yEuQNvEQ1h33G1XMd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8efbe7394.mp4?token=g03fXxAhdgZrpCCqfhtCslX7RsGLuhcv-4705zu3OuNUb6eKVhQljOa4W8lIFTx5OdterccrfARAMgzbzcRXhtCV8mLweSwIDlF7oPcvKFJPCnbyld_oCi4RcTDLjWEC4HwZXJ2UwRkOZBLCA6xC2S4vyfN1g52zBPJpbCK53MH7hCLtc8BL51x1xYXNhuTMXLw-1OhWJt2nQo7P8URCVecRHn-0f9XlXdkRJBF_tCdL49TeaEfl9GQL3_JHkByzZUEzjQXNdW8f1IpUxorwkFbPyc4Oq7jSaGKmiPATLmbn9vjQ7Cm1Qkj73uV-FrMjOs-tcvQtdrr3MHdPa7dlv4T2vPTRM3X4_oBQcmdlNn9A3pVFTlDpxI2M2ps4TujHqkOuXkTr7r6UeWQWHIWUaVyiurbaxZ2nMHykU6daZFFjOPnGCoS22EPTrrm8l4ES8aBF6LvRiWuQM15p5LBSIGb4lRDBHyPYD9tqBb6kDdlN2Due_NSivK4mBGHamVt6mtXfVRzdepOBg11mfmgwxI3hWaJ3_14U3hnJ-pV_euNHEtVZOO0c5xY_gJ3OjOFbd1mrxfXVTSd2xCd7r1xRD3RdswRKnIlEwPkY8omjjKiI8HnYM3nHcTG0gh8pZG9B7-i_Z-duJCBvP7IxFtK8c3f43yEuQNvEQ1h33G1XMd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:به محض اینکه ایران تسلیم شود، به محض اینکه جنگ به پایان برسد، که این اتفاق به زودی خواهد افتاد، قیمت نفت به شدت کاهش خواهد یافت.
قیمت نفت به طور چشمگیری کاهش خواهد یافت و تمام قیمت‌ها پایین خواهند آمد، اما قیمت مواد غذایی به میزان قابل توجهی از زمان ریاست جمهوری بایدن کاهش یافته است. تقریباً تمام قیمت‌ها به میزان زیادی کاهش یافته‌اند.
ما حجم بسیار زیادی از نفت را خارج می‌کنیم؛ شب گذشته، ما حجم بی‌سابقه‌ای از نفت را از تنگه هرمز خارج کردیم، بیشتر از زمانی که قبل از جنگ این کار را انجام می‌دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24334" target="_blank">📅 16:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24333">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ در ‌تروث : در حال حاضر، شمار افرادی که در ایالات متحده مشغول کار هستند، از هر زمان دیگری در تاریخ کشورمان بیشتر است!
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24333" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امیر حاتمی، شهید زنده، فرمامده ارتش جمهوری اسلامی:
جنگ هنوز به پایان نرسیده است و ما باید برای وارد کردن ضربات قوی به دشمن آماده باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24332" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d096c16704.mp4?token=E_GLTAFBBq_RxfyJvFbTKQ8aJK6gXNz28vR59hc26IGED7ZZoRWk03qoXAeaU4paSJ-xmYbjOQKeJUmtxMVyKzipcuyF_NouLMUyziz2n7K9zLn2vEhLGV08A0muY9Jb731GcLE8NZOCgNLIhsoD1Rca5ILneSQhy87-QF1KDg3ZBTysQOkdJDBEbRFN0qnKjIjVx4fYJ_raeXa5uWyTbSmWrpvJR_uFRxzEVd88bqZSw7LZ4KXPzefMVxeIu-jDOymG8itwKykf6hEbS44iGDY-TRdq0229eUedVwJxAiKM98XQS61wEWjoE6rPN_ENPsZBBs5FqGgWjBmp9dLwS7R7NYh5aL4reAvT0ylYhFecWjnfqpuGi_KY-6Wu_c0M1hqiKq_fhYG_vtC5u_k27IpgfqLX1VMWjFditv7_minB0QFUpxatSmV6rysvmQRf0oIyZDU2B5OoXOnr7snea9EHnj8R1grS3wf8QejMie7rc5INg2v8K2zl-ttFzdn1JBoJq5ABFneItqYlyI7FRJfalQaHohb7Q9Gg7B5LUhnDA_dWzUt-QgX3gnDQ9Pk_db78e2TfG5GR1h4Vbtj0QKL8Hy3B4-efwoTCeUnOZKDlTNF8BAH2HpYJK0QpL92A7R3Z2b-r3kcuVQ49he81Pt_t6nlHDqekJeu7pIdvJbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d096c16704.mp4?token=E_GLTAFBBq_RxfyJvFbTKQ8aJK6gXNz28vR59hc26IGED7ZZoRWk03qoXAeaU4paSJ-xmYbjOQKeJUmtxMVyKzipcuyF_NouLMUyziz2n7K9zLn2vEhLGV08A0muY9Jb731GcLE8NZOCgNLIhsoD1Rca5ILneSQhy87-QF1KDg3ZBTysQOkdJDBEbRFN0qnKjIjVx4fYJ_raeXa5uWyTbSmWrpvJR_uFRxzEVd88bqZSw7LZ4KXPzefMVxeIu-jDOymG8itwKykf6hEbS44iGDY-TRdq0229eUedVwJxAiKM98XQS61wEWjoE6rPN_ENPsZBBs5FqGgWjBmp9dLwS7R7NYh5aL4reAvT0ylYhFecWjnfqpuGi_KY-6Wu_c0M1hqiKq_fhYG_vtC5u_k27IpgfqLX1VMWjFditv7_minB0QFUpxatSmV6rysvmQRf0oIyZDU2B5OoXOnr7snea9EHnj8R1grS3wf8QejMie7rc5INg2v8K2zl-ttFzdn1JBoJq5ABFneItqYlyI7FRJfalQaHohb7Q9Gg7B5LUhnDA_dWzUt-QgX3gnDQ9Pk_db78e2TfG5GR1h4Vbtj0QKL8Hy3B4-efwoTCeUnOZKDlTNF8BAH2HpYJK0QpL92A7R3Z2b-r3kcuVQ49he81Pt_t6nlHDqekJeu7pIdvJbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: در پی بازداشت چند نفر به ظن جرایم مرتبط با مواد منفجره در نزدیکی پایگاه RAF Fairford در بریتانیا، تدابیر امنیتی اطراف این پایگاه افزایش یافته است. چند ملک در منطقه ولفورد تخلیه و خودروها توسط تیم خنثی‌سازی بمب ارتش بررسی شده‌اند. گزارش‌هایی نیز از…</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24331" target="_blank">📅 15:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faaed5699e.mp4?token=Jz0pAcci77betc8KgjmZZNfl2KwiCknOAOVuCyYHREgly7HlbbjIaWzBAEYs15i81fny9qRrdQP1CqCHyL2TEkDZwIpbMK1bGMQzpGab1nKG0p784zBpdMWsJ7Uu14c5jFFdAM-ga6TQoCwEwqE4PXTuZFkDyMtk1gcWn8T3UIGOcQ3IEm9LB2liTSUyRoyTIw9XPQU8xbcYp1go9ByllOHtVZZ1-NxEf-FrXUgNKgVekcqxGhMDyGBq0mqB0vFLFwOrKwpJlAoEr17ztug4mXctS4t-dHGjCj1A-Vq9t98dTCsunlCuL0XdgG0pShKYG2xQtptdcrRYFZxsBOWaZhCGmgWpYuhS8M-J5tuYpWuk2q80oxwqxac20dVCJYDb_8jNpmKM5BQdgzngxmBibA1xH9tTINHHXrnOWUdHVwzC2CXaC9Lxkn1QC77NTcBKUokhVI-8ZasQ6gGRKSrsLaNDiZv_wT1Eoi92XQoqALax3dWWyuptZm5lVY6fI8WosZq5x_WqZwemnu-TEzPbubGyqBMEQ21yCSyZr4hUKYa1uMbrnxXWM1udlmsyw6BJvDytWWgpPC7SsYLmHUQqlrJxcx6_UxUscHDPiWI9Iqd3zoIgsqJqJ3aqw4fWEswOwhf1NYHcY0lLKqTk97figjA3yQpTkRmHQmh1Y7s6mKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faaed5699e.mp4?token=Jz0pAcci77betc8KgjmZZNfl2KwiCknOAOVuCyYHREgly7HlbbjIaWzBAEYs15i81fny9qRrdQP1CqCHyL2TEkDZwIpbMK1bGMQzpGab1nKG0p784zBpdMWsJ7Uu14c5jFFdAM-ga6TQoCwEwqE4PXTuZFkDyMtk1gcWn8T3UIGOcQ3IEm9LB2liTSUyRoyTIw9XPQU8xbcYp1go9ByllOHtVZZ1-NxEf-FrXUgNKgVekcqxGhMDyGBq0mqB0vFLFwOrKwpJlAoEr17ztug4mXctS4t-dHGjCj1A-Vq9t98dTCsunlCuL0XdgG0pShKYG2xQtptdcrRYFZxsBOWaZhCGmgWpYuhS8M-J5tuYpWuk2q80oxwqxac20dVCJYDb_8jNpmKM5BQdgzngxmBibA1xH9tTINHHXrnOWUdHVwzC2CXaC9Lxkn1QC77NTcBKUokhVI-8ZasQ6gGRKSrsLaNDiZv_wT1Eoi92XQoqALax3dWWyuptZm5lVY6fI8WosZq5x_WqZwemnu-TEzPbubGyqBMEQ21yCSyZr4hUKYa1uMbrnxXWM1udlmsyw6BJvDytWWgpPC7SsYLmHUQqlrJxcx6_UxUscHDPiWI9Iqd3zoIgsqJqJ3aqw4fWEswOwhf1NYHcY0lLKqTk97figjA3yQpTkRmHQmh1Y7s6mKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : برای چندمین روز متوالی حرکت دسته جدید هواپیماهای سی۱۳۰ هرکولس به سمت منطقه و اینبار هم ۵ عدد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24330" target="_blank">📅 14:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سپاه: یک فروند زهپاد پیشرفتهٔ ارتش آمریکا را که به منظور جاسوسی در تنگهٔ هرمز فعالیت داشت، به دام انداختیم.
این زهپاد از نوع یکی از زیرسطحی های هوشمند و پیشرفته با نامRemus 600 «ریموس ۶۰۰» بوده که توسط رزمندگان نیروی دریایی سپاه به غنیمت گرفته شده و اکنون در اختیار متخصصان این نیرو، به منظور بازیابی اطلاعات آن، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24329" target="_blank">📅 14:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24328">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه : یه شهپاد زیردریایی خودران دیگه آمریکا رو گرفتیم
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24328" target="_blank">📅 14:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGRsw9fpbkG4A6-3qs_ClUw7SAh-e7vW-uiDpprtboznagGh6cQ44hfovcIML4gBiIw3wEDkXrXagh5EZaMRUO5L1kVdlBJHYSHiUYlzMc6FxiRXT1giFwezGEerEg_vhyWaHMrl-9Rw1w_5Tfp9QFKKmviwFH5Vymfbw0H04mochfpkyr60OVhLXXZcQGhwsU0z83vC93SWrleCBlV5dhnrmkDJSlhrUO7qlEoG5kiF__txpBi-cy41Jdok5bzzlN7MlY9fG-2xQD6_JKPpGgMNj6bZ5ftfjs2qeiVfI2xyzJ5uZUDwXYT2rKsCeS1pmPD2jpa6k4-H7CevXLQFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبراهام لینکلن به هاوایی رسید ، چقدر با RUDY11 خاطره داریم یادتونه ؟
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24327" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مدیرعامل شرکت ملی نفت ایران:
بر اساس اطلاعات به‌دست‌آمده، اسرائیل و آمریکا برای ضربه زدن به تاسیسات نفتی برنامه‌ریزی کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24326" target="_blank">📅 12:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNbg6bzwLTlmBF9veEK0nvTO9V4XsX3T34x7Yldcuo-b8pPGokRCd2C2lDhtM7YtXTZr5n5gh7ezaqiN9jEsRAHAw5562VACSxRmlZTBSxv0g9qqyKEIV5OAzEiL1dHiQAfZe5JlitM8zdK-MzJt4IZJQbkTVvT6MX-5e9rcyzeDxxq1cXzgev1Toyzag9yT4P7mk7029pHi-0x7X7KVLLmiguYRJid3hbSpton2UHluDXrtqrCXlNGn-uisdTn6rzIdQLO_234va_SDcDaeDSD1_EzF6F8y-s4jYoMsjnNwjUX2MwRY_raovZqm5ywilRPDkuil7mFD69g5mxbZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpBHTca8zzzJ2vmdR3l-ejIO5qLGhDDymvqxKyFKts6IYtZTHE_EL77BMXf9u7GSk9pEstzVrW_TUf7oNVbu0SBAIer4uZuHyF9k-uaGrZgeELNu6CQDfrBsm2GgMvzyG4WRZx-s30GKin83MOL7PRpAr1t-dX9i-xRKjvWk5VeUPH7CWtnhc2gNSGTjjGCYaDsdZY-wX-X38K3tsT7NquGunGW3eq-XYTrL52xLTtM-Uh7uQ2QUPes_gwdP1vZRyASaiMQeQ8Ms2XzzKmV9dpCuoHVn9bXo7hkEHIPu4L1eR5IWCqVoppxJ5tF1syBV6QRpWlh8Vp7ykxGpD9GpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wvwlon2k7_tmDNEXTivBbF4BEMYugqv3Stcz_mqU0MGbPWfV7W9SiGj9xK6--l1Xxmh0Xq9RK5FxIFXS8IOyl9k6qXY40XKlKwqo9C56YQcsbURgZZ1Mpx4Jn4ShD03oICKosAMeco8rVB_y88vb0O4r451ak2mDH7-VwKbDqTVSa1Eg9DC-ic1KgFMbxKNm1zN15O2vfTTB5mrq1w36fgQOtmdnXm0cTHAiXuW1CWxc5dB57TjeGawnyWUd3hpJxmbH0xhQV_knlLbOh_hRVlTj5F-1vEF9gxkRcD19jnR456mX3Nj8ITIllg5RkCxC8xjMe5p8ObPbPTC8BJkaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPIzshVPx4TTidR4PFxyJiHV1D7aCrpvaYbwMn3Ms2Vyslu1zxJPAaYq9YecItJL2EkO0i-k-948zKzJkMIodpCy-hqQePHxipG2uA_JzXns8_JoNu_DTWvb--NjmuDYT9kTzwAsVB9rGYc-kVn1jYGchQUbaj3lvLwQupnh73I0xNZVLYrY0a3FAo6lLS5DL1P7PYMIbWK83wXYlY98_i2soByX7hDB7uczY-Yzwk8cZosh9CNQnCSGMwch1qqQeoWhpMF2N-Jk1jVgbnrppMJh-dhZghxoTv-8Eznvt966Erfd2xSCRI2qIVC8_DHkv9jQbNhQdCUfGNu9CaIVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XP2Cta1tgOnkRPwP_DKWrkZtlUMEAe5kCPC1IeJ0f34b3ebHo6VXd9DrOxGgWjSMK-Y_85nmPYQ0AaUBoYRnzLkQgXAfKVG0g4QNnD9CSmAVIT7yGTbwYHebwDWFwdyORTgivRd6c_-DXk-oLbz5CZTrcRIVb4MDBMC8eFSxynICYCOEnnivk8HNLavJ4mt3dU8v8bKab7IizmnxRCVXYZ4RlPiQz7Fis8MpkmznHe8aC-vHje2YM2r2GzP004bNR2LRbSKanjTxZWPTeRMEsSm0nAC7cKKjLiMiHGMV4ygsWYGBwqN66qCjFDevYnaOh9MSZ1qZS7WiDYpm6DlnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBLCMLAbKA2jarW8HLzFKbROdQX3qzV6hUPnkEyX2Q2pDy1xyRNbigV6ebINfp8ChVbKW0MUrPuSl1yeUPx3GLFv3vU136t869qR77nr_YnfVKGA-fHHZEFf1a47SAtjaIAUSYUvOiLQFYDwGT8UyKORrKFOeAWP_lLZeE4vmnmsa2mmo8bU_h-JFWLi4v8JED66m6ochdlnRCsIo4mN5tFZ6e6bwNd_6ywHUsBAbirxozwkDvbZHwb89cxe8HFj__gjhG_Keb1e5CNZJ1NNJM6os7TYLAsurMGOliiAo4U1GGw4LRH39mp__EFneLn01p0WlFm4mCMUYOcOu-4ukQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQG2AxRShTIx6qXxbutnPSUYh-0fxq56oCUWfBMcwk_eKMonAZvhySiAf9yW69-b6K5tZffReqgecvQcMJOAvtIHb6nWaUbZcf0h11nTjLZdVAu3fp9PhppLQ9Nf4373o0MbsdBMNalXuUaKK778cHCbqytka7evRZQfnqHBXSnjH3N0YatOgoromdFzKM58x8JTl1l1faYE9vGIQ3l34J5nMsvJr6BaiFJmHc4PHH_EHgBUzvW6bBDIRyfZVD1xD4M6-axDqY71ynj5IxI_e_AYxFAhbz7Nl_OXlQw6LoldZHG9Ii9-tR68mBpbI3HlAoCEdxy9pZOZHDz_kCGsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIyVMi5eQ0Zs4RdWHzvQiey3qudJWMwXeJxkiuoTjJtwDOJ1gi4c4ExDYHCase7mggKHVUd6Hz3g3ddMjgE5dg2AVO3Rsv5sH1iQQk1MbtL5Ngz3-OQ12QIKga4C7yFB4FbuicWchBRVIENBOIAnX8HoLo7kUWF7PMtdaVclNGcohpd-SPG-D9gFBJKxa-V3_aztG9KwKQz_07csars8-A7UbTD-VUd-u3V8-KB7C6Ab-9rnnBONwANh1rf6uDg9Yx3TvGiz9u6VDTQbiw4PC9jJnUKXU5lLtDNwJtJ-_Psi2t3uJmxZRw7ntvbNNLWx4xNyHgt2Rb7kQUQ6yKRkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvGR6-yPyEWEoBtimFQBYKFxOcNcDuHn0asrZXEmdCDGSXIFASoxI6OviTjoVzG_vHf01tcrQZ10Xvre7DEPZvAXolXaeIbm1tv5CJntFWv2yv1EX1UH6UYuVU-WRX3CyFYvfoZMP2H6eorcImJADhEWU1xW-B3Bn-OZcgbuPA54wsEeN6huO3XY2M94OvNrjPG4JOY_4CeuRyf7LR11j3iiiJ38hAeTY4CDZpTNntuY_EcavAEjFCmcdvPd_LGq-Au9z9-WaFlEJdCIWWRjEZY2YNZB_9A1MZ5HKAJqbxEj9USE6pKsgMXejGpPovflMidqPw9XDbDiGYjB3bCgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9a-FkPzbQUkCwngaFGINELu-_MDzDif-GVHws8IdVwNJZWLZafflZGVm5ll1eOoNDCANx7lp12O4X6HZjsGFtNS1xmpTynBPQu2Lbvvq_IqCfOnZjT5kDfyPvzRGINTJ1UFbfp_K4_RnQqRhp60fp9apc9R2wX9pp7NfOYUic3_vIaibUO9TMlweupmgYUx4Zla1K66gIxZ_HQzEIW2IW6Yj3p1danYo7QJXD17DpGn1eXRMH_SPDk4lH1dkrMwRn8UxZduTNfmII6LZslReWNbC8Uk5IaBhziJxNkCaBCBXx2ZkJ3qcmlqJENeXzOWDobQqJPBSbzzgoiaSSu4nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آوییشن‌ایست:
۱۰ فروند جنگنده
اف-۱۵ئی استرایک ایگل
نیروی هوایی آمریکا پس از بازگشت از خاورمیانه و مشارکت در
عملیات خشم هماسی علیه ایران
، در پایگاه هوایی
راف میلدنهال
در بریتانیا فرود آمدند. روی دماغه جنگنده‌ها نام و تصاویر شخصیت‌های بازی
مورتال کامبت
مانند اسکورپیون، ساب‌زیرو، لیو کانگ و شائو کان دیده می‌شود. همچنین روی این جنگنده‌ها مجموعاً
۴۵ نشان انهدام پهپادهای شاهد ایرانی
و نمادهایی از مهمات استفاده‌شده، از جمله
موشک‌های جی‌ای‌اس‌اس‌ام، بمب‌های GBU-39 و راکت‌های لیزری APKWS II
دیده می‌شود. این ۱۰ فروند، نخستین گروه از مجموع
۲۴ فروند اف-۱۵ئی
پایگاه سیمور جانسون هستند که از استقرار سال ۲۰۲۶ در خاورمیانه بازمی‌گردند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24316" target="_blank">📅 12:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏در دومین سالگرد نفله شدن حسن نصرالله، مستندی از لحظات جستجو تا رسیدن به جسدش رو ببینید، ارتش اسرائیل اعلام کرده بود بر اثر خفگی مُرده و درست بوده، اسرائیل اشتباه نمیکنه ( با زیرنویس فارسی )
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24315" target="_blank">📅 12:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یانشا, نخست‌وزیر اسلوونی: تغییر حکومت در ایران و انتقال مسالمت‌آمیز قدرت به مردم، برای توقف صدور تروریسم و ایجاد صلح و ثبات در منطقه ضروری است
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24314" target="_blank">📅 12:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رویترز:
در پی بازداشت چند نفر به ظن جرایم مرتبط با
مواد منفجره
در نزدیکی پایگاه
RAF Fairford
در بریتانیا، تدابیر امنیتی اطراف این پایگاه افزایش یافته است. چند ملک در منطقه ولفورد تخلیه و خودروها توسط تیم خنثی‌سازی بمب ارتش بررسی شده‌اند. گزارش‌هایی نیز از قرار گرفتن پایگاه در بالاترین سطح حفاظت آمریکا،
FPCON Delta
، منتشر شده است؛ نیروی هوایی آمریکا از
افزایش هوشیاری نیروها
خبر داده است. پلیس می‌گوید حادثه مهار شده و تحقیقات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24313" target="_blank">📅 12:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75be4777e3.mp4?token=mWD01sebagnAPPxJhMm3ErmvJMHozxMvFYh8sc4nEtlgHphdKn20Ocv_2yEML3GX6lF4Y8s1MfGONz2hDLXcfINp77JNc-aG8yURAaOCXTtiz_RMMXySQclRkClGUO0HIsqjTP1APkQQZmSZV88ZI5FM7EEfkQaIbJkvG_n_GM0pJsB8S_PFpKf_KMP8IxRiki9b-PJyC8v3Y6bqGSm4oa_dkN4RdPOX2Jg6fu3H3iWE5SfAjUw678G56RrpgaPo0I1zwMa9ZipybkGDKwGWZ0tbUHKC3OQsDCqugz-VLEHzREc_I1Zh1kVeWjFJmEvSZ7YNGnKxJrkOhnBCSipLvVZNdioKQjZhmMbOLdZPUb65eSBPL05vdb73OwS7l-k-vkMNhdHXeeTQBXLlQC_Y7v5yMAlpWHXE5waVpsboZL1Hp-6xr_WLYZE9sUT4_Mw_ZZQ__GS2ZjNsdotL4Esdxz7Q30wwbUrBRSftFjcXpFNTj4R1ERvU4p6mXz8x3POO6JjbQYzLqORlM0c_Jw2AnAxZEkXqNGnIv5jCbjSj5TX9ee-_6HD8ekNzWgxOpiMVIixwfzNk3ersE0KlXjkvIofbmbResI-gLY8RiY5Nhk7ErrrgQ8i88WqBiZ7geUypGhweoVlT2W3W2VKkBqpc_e0xTNW3FN-vwE7SvsB078Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75be4777e3.mp4?token=mWD01sebagnAPPxJhMm3ErmvJMHozxMvFYh8sc4nEtlgHphdKn20Ocv_2yEML3GX6lF4Y8s1MfGONz2hDLXcfINp77JNc-aG8yURAaOCXTtiz_RMMXySQclRkClGUO0HIsqjTP1APkQQZmSZV88ZI5FM7EEfkQaIbJkvG_n_GM0pJsB8S_PFpKf_KMP8IxRiki9b-PJyC8v3Y6bqGSm4oa_dkN4RdPOX2Jg6fu3H3iWE5SfAjUw678G56RrpgaPo0I1zwMa9ZipybkGDKwGWZ0tbUHKC3OQsDCqugz-VLEHzREc_I1Zh1kVeWjFJmEvSZ7YNGnKxJrkOhnBCSipLvVZNdioKQjZhmMbOLdZPUb65eSBPL05vdb73OwS7l-k-vkMNhdHXeeTQBXLlQC_Y7v5yMAlpWHXE5waVpsboZL1Hp-6xr_WLYZE9sUT4_Mw_ZZQ__GS2ZjNsdotL4Esdxz7Q30wwbUrBRSftFjcXpFNTj4R1ERvU4p6mXz8x3POO6JjbQYzLqORlM0c_Jw2AnAxZEkXqNGnIv5jCbjSj5TX9ee-_6HD8ekNzWgxOpiMVIixwfzNk3ersE0KlXjkvIofbmbResI-gLY8RiY5Nhk7ErrrgQ8i88WqBiZ7geUypGhweoVlT2W3W2VKkBqpc_e0xTNW3FN-vwE7SvsB078Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسخره کردن پزشکیان در فاکس نیوز : آقای پژاکیان ، یه سوأل ساده هم نمیتونست جواب بده
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24312" target="_blank">📅 11:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24311">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE-PnIxKwVj-Nk6glSuMk5AbEFO5_NIqodfoiDY9VxWk3D6Kfhti8fA8VPnxN81WCMdLOk14ezwi7Etz5OrEZY3arBqFx5eDDiuDar8QDJjbYc5PwyttQtNI-BX37if5zpf5j1oDHUDpyXeepBrppzHgCTTiASj7rjvN9gT2SIAjtFtNt0ZbtwY2_eS9hC73fBc_dY_zOLmXIHHKcjczl8khz-jGyK8QJSNPT5sJLmuvdk1w0Nenn0YIUBCw-f4tLDT8D6pMqh9VQC9ERE_1K5VH26aL1JphezHKnmwme66yiZSn94Xhr8kRJZ4f8vXp_89u67qKV7VcsIAZ-0sE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نجات ترکه موتور یه پرستو نشسته قشنگ ارشادش کنه ، چیکار که نمیکنه این رژیم
سردار سرتیپ پاسدار
محمدحسین زیبایی‌نژاد
مشهور به
حسین نجات
(زاده ۱۳۳۴ در شیراز)، از فرماندهان ارشد و شناخته‌شده سپاه پاسداران انقلاب اسلامی است که هم‌اکنون به‌عنوان
جانشین فرمانده قرارگاه ثارالله
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24311" target="_blank">📅 11:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: تمام بانک‌های تجاری بزرگ در امارات متحده عربی و ترکیه انجام تراکنش‌های مالی با ایران را متوقف کرده‌اند. بسنت گفت فشارهای اقتصادی واشنگتن برای منزوی کردن ایران در حال نتیجه دادن است و آمریکا برای اجرای این سیاست با بیش از…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24310" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoCoIlbXWggPXG7iqguCo6dR638d0Vcx2IUyHsu_jYaS2C1X2b1NBkocak4kkNvuLLNH31_kJRBVULiZHU1VkBxv87R4_03GdboyGOIuYZDO86-wzf5NLkTkPeI3uG24uwdTAVPXR-7TWh7CMDeXCSFTVDs1CuD2O5QJSFEuqiqQfzgy2AwLm-UUjpXguQ5F8kDgxTTIzHCxh2k1eDTYPSzCZ_W1iVkvkTBNchnZZMenXSRMZD6djyIlCBbeRLGn1BGgYQDVqWlaILnDeu0hE4df4J_keclTUM5g54FZ7fdYvWfzLzVGwvpF7pVq6SdwsjQP8HCae4qwlsunqYKtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی : من جام خوبه نمیام ، مرسی اه
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24309" target="_blank">📅 11:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcKi86nMcED3shsn-EPbc1eEIjfA3r3KEC4Sh0tIoWJedIFMG6twyic1pz5hAeeoUMczKQckwyE2WmMH9aZd9rONg7C4Kt5OUK2CwgRabq9IIo4XubO7zx2PKNgE6PkXKAk2YFFYGl8-fbhlUA4AENVPyq7y-M9lE39RFO5zBtUon2AzVz5_WoiOhPXtp3T_aeFG-vOnxKgw4yHRwRm4C4rRrySFpMf3yLqoLYLI9g1FO68Xwy4DqMYmkkU5Mn1pIMphup36-NYj_z2z0SnE5AwFWWlBd0G3lQgWcbA3RQOlaZbq7fzZOCQ5r0TNZOxyA9NLE5kD8bWM8WdMqRLj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های رژیم : سرهنگ دوم
مجید بهرامی
، رئیس پلیس آگاهی شهرستان ایجرود در استان زنجان، روز پنجشنبه ۲ مهر هنگام انجام مأموریت برای مقابله با
قاچاق کالا و ارز
جان خود را از دست داد. بر اساس گزارش پلیس، در جریان عملیات، خودروی قاچاقچیان با خودروی مأموران برخورد کرد و سرهنگ بهرامی بر اثر این حادثه کشته شد، این یک ترور سیاسی نبوده و
عاملان این حادثه کمتر از ۲۴ ساعت بعد توسط نیروهای امنیتی و انتظامی شناسایی و دستگیر شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24308" target="_blank">📅 11:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
تمام بانک‌های تجاری بزرگ در
امارات متحده عربی و ترکیه
انجام تراکنش‌های مالی با ایران را متوقف کرده‌اند. بسنت گفت فشارهای اقتصادی واشنگتن برای منزوی کردن ایران در حال نتیجه دادن است و آمریکا برای اجرای این سیاست با بیش از
۵۰ کشور
وارد رایزنی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24307" target="_blank">📅 10:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyjoNdHZK5N142iNk1Fxp3LSmT7lkkUDQu_FaLnm3uNGznvjpqFp38CoiJDUp5LvoUHAhfsyT-j7U7bHFRNzPjxvECW_ZpRRYufydw27uShNJkRwqHm26sH83g4J9oAPtHEKKHcDxEk8iT3_Um674GV3HcN9B-PQRisf7St1K_X8yBiDJkd6nYpMdR1bA-WTA7ZtDbua7zjSI0UzdvdijZlFaUqHiBDrZdRthDDbm24EGfzdaRbOmFadIhJmfbC2bUI8ji_n8NTW5CJge4HZZ1-qpPReKtBT8orItu8V8f0w74_GDEd7twEfjLl-mBf8xw2_E7TyKbjDQxlK7USWTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۳۰ دقیقه اخیر ۳ انفجار بسیار‌ سنگین خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24306" target="_blank">📅 10:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تام کاتن، سناتور جمهوری خواه:
یک درگیری جدید با ایران در پیش است
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24305" target="_blank">📅 10:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgZChXC8Ydja59fHWhw6WywmCEex9Il_oiwNAbVcVBNEDRAhnbfGJEI5eUCV9ZK0oDe7yvfFPpqZfy134RYq7D-KyWAm1Y8fCsSL6S_ndR3GK0jiQcHfhChah8eDi7_wsfequjVv3ldf4-gZq3hluV9-E18Q0AK8ms9h77ZP2O9SmfrnXdF73uHUbOn4yOG9SuCwuzv18hSwXP6YnckiFWIK0OC9o7aAtc2o3wA1i4L-po3aAOUyJso1kSrnbqyJFaY9SHEbFW6VlLOWb6JdSKhResl96k-7pbfCDX_3q3v6N2D_dwx5ZPUC7ssceuYNLWUv_NR-qx6Ww-kG_Lo1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس:
چین دو پاندا غول‌پیکر به نام‌های
«پینگ‌پینگ» (Ping Ping)
و
«فو شوانگ» (Fu Shuang)
را پس از دیدار شی جین‌پینگ و دونالد ترامپ به آمریکا فرستاده است. این دو پاندا بامداد یکشنبه ۲۷ سپتامبر از فرودگاه چنگدو با یک پرواز چارتر عازم
باغ‌وحش آتلانتا
شدند و قرار است حدود
۱۰ سال
در آمریکا بمانند. این اقدام بخشی از چیزی است که چین از آن به‌عنوان
«دیپلماسی پاندا»
استفاده می‌کند؛ یعنی اعزام یا امانت‌دادن پانداها به کشورهای دیگر به‌عنوان نمادی از روابط دوستانه و همکاری دیپلماتیک
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24304" target="_blank">📅 10:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فاکس‌نیوز:
سخنگوی سپاه، سرتیپ حسین محبی، اعلام کرده ایران تا زمانی که
هفت شرط تهران
برآورده نشود، به عملیات علیه آمریکا ادامه خواهد داد. از جمله شروط ایران، رفع محاصره دریایی بنادر و آزادسازی بخشی از دارایی‌های مسدودشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24303" target="_blank">📅 09:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رویترز:
عباس عراقچی اعلام کرد ایران در مذاکرات جدید درباره
برنامه هسته‌ای خود امتیازی نخواهد داد
و حقوق تهران از جمله غنی‌سازی اورانیوم و نگهداری اورانیوم غنی‌شده، قابل مذاکره نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24302" target="_blank">📅 09:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار:
برای بررسی روایت انتقال مجتبی خامنه‌ای، ابتدا باید به سه بیمارستانی نگاه کنیم که
در ۲۸ فوریه و شب اول مارس واقعاً آسیب دیدند: گاندی، مطهری و خاتم‌الانبیا.
۱-
بیمارستان گاندی در شب اول مارس، در جریان حمله به ساختمان‌های صداوسیما در نزدیکی آن، به‌شدت آسیب دید و بخش‌هایی از بیمارستان تخلیه شد؛ تصاویر و بررسی‌های مستقل محل اصابت و خسارت را مستند کرده‌اند.
۲-
بیمارستان مطهری نیز در همان موج حملات آسیب دید؛ این بیمارستان در کنار مقر پلیس تهران قرار دارد و تصاویر قبل و بعد از حمله، خسارت قابل‌توجه در اطراف و داخل بیمارستان را نشان می‌دهد.
۳-
بیمارستان خاتم‌الانبیا نیز در گزارش‌های همان روز به‌عنوان یکی از مراکز درمانی آسیب‌دیده ثبت شده است؛ گزارش هلال‌احمر ایران از حمله به محدوده اطراف خاتم‌الانبیا و مطهری خبر داده و بررسی CNN نیز خسارت به خاتم را مستند کرده است. بنابراین اگر روایت انتقال او به چند بیمارستان درست باشد، هنوز این احتمال وجود دارد که یکی از مراکز درمانی مورد استفاده او
یک مرکز نظامی یا حفاظت‌شده وابسته به سپاه، در مجاورت این بیمارستان ها
بوده باشد؛ اما این ارتباط هنوز اثبات نشده است. همچنین بیمارستان سینا در گزارش‌های مربوط به مسیر درمان او مطرح شده، ولی طبق همان روایت،
پس از حمله اولیه
محل انتقال او بوده و نباید آن را با بیمارستان‌های آسیب‌دیده در حملات ۲۸ فوریه و شب اول مارس یکی دانست.
در نتیجه، سه بیمارستان آسیب‌دیده را می‌شناسیم، اما فعلاً هیچ مدرک مستقلی نداریم که یکی یا همه آن‌ها همان بیمارستانهایی باشد که مجتبی در آن بستری شده و سپس زیر آوار مانده.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24301" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24300">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">در جنگ ۴۰ روز قرارگاه سپاه در محدوده چهارراه آبسردار با اینکه کاملا در منطقه مسکونی بود با این دقت شخم زده شد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24300" target="_blank">📅 09:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏افشاگری محسن حیدری آل کثیر عضو خبرگان رهبری در مصاحبه با تلویزیون قطری العربی تایید کرد که مجتبی خامنه‌ای همراه پدرش بود و زخمی شد و پس از زخمی شدن پی در پی به سه بیمارستان در تهران منتقل شد که هر سه هدف قرار گرفته شد و در بیمارستان سوم از زیر آورها او را…</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/24299" target="_blank">📅 02:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اتاق جنگ با یاشار: پیامی که در برخی کانال‌ها درباره «تحریم جدید ایران توسط گوگل» منتشر شده، نادرست و گمراه‌کننده است. این پیام عمدتاً به ارور Too many accounts created مربوط می‌شود؛ یعنی وقتی در یک دستگاه یا از یک مسیر اتصال، تعداد زیادی حساب جیمیل ساخته شود،…</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/24298" target="_blank">📅 01:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرنگار اسرائیل
ی
: حملات امشب سپاه پاسداران به کشتی‌ها در تنگه هرمز گسترده و کم‌سابقه بوده است.
گزارش‌های دریایی از افزایش حملات و کاهش شدید تردد کشتی‌های تجاری در تنگه هرمز خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/24297" target="_blank">📅 01:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اتاق جنگ با یاشار:
پیامی که در برخی کانال‌ها درباره «تحریم جدید ایران توسط گوگل» منتشر شده،
نادرست و گمراه‌کننده است
. این پیام عمدتاً به ارور
Too many accounts created
مربوط می‌شود؛ یعنی وقتی در یک دستگاه یا از یک مسیر اتصال، تعداد زیادی حساب جیمیل ساخته شود، گوگل برای جلوگیری از ساخت انبوه حساب‌ها ممکن است از کاربر بخواهد
شماره تلفن خود را برای تأیید وارد کند
. این موضوع می‌تواند با
استفاده مکرر از VPN یا IPهای مشترک VPN
هم مرتبط باشد؛ به‌خصوص اگر از همان IP تعداد زیادی حساب ساخته یا وریفای شده باشد.
پیش‌شماره ایران (+98) نیز در حال حاضر برای وریفای حساب گوگل قابل استفاده است.
بنابراین این پیام به معنی تحریم یا مسدودشدن جدید دسترسی کاربران ایرانی به گوگل نیست؛ ضمن اینکه محدودیت‌های گوگل علیه ایران موضوع جدیدی نیست و سال‌هاست وجود دارد.
اقدام جداگانه امروز گوگل علیه حدود ۶۰ حساب مرتبط با صداوسیما
نیز به دلیل فعالیت‌هایی که گوگل آنها را مرتبط با
فیشینگ سیاسی و پنهان‌کردن هویت
عنوان کرده، انجام شده و ارتباطی با مسدودشدن عمومی کاربران ایرانی ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/24296" target="_blank">📅 01:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ : این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.  گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها…</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24295" target="_blank">📅 00:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24294">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ :
این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.
گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها را بکشید، اگر در هر نقطه‌ای از زمین آمریکایی‌ها را تهدید کنید،
ما بدون عذرخواهی و بدون تردید به سراغتان خواهیم آمد و شما را خواهیم کشت.
ما این جنگ را آغاز نکردیم، اما تحت ریاست‌جمهوری ترامپ،
آن را به پایان خواهیم رساند.
جنگ آنها علیه آمریکایی‌ها، به انتقام ما تبدیل شده است.
ترامپ :
ای مردم سربلند ایران، ساعت آزادی شما فرا رسیده است.
زیرا ما آماده‌ایم دولت شما را به دست بگیریم.
این حکومت متعلق به شما خواهد بود که آن را به دست بگیرید
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24294" target="_blank">📅 00:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبرگزاری محلی هرمزگان:
هم اکنون فعالیت‌های نظامی در امتداد سواحل جنوبی هرمزگان، به همراه تعداد و شدت انفجارهای امشب،
در چندین ماه گذشته،
بی‌سابقه است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/24293" target="_blank">📅 00:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اتاق جنگ با یاشار ، وضعیت قرمز : ۹ سوخترسان در خلیج فارس و یک دسته سوخترسان با مالکیت نامشخص به سمت منطقه ! (دسته دوم ممکنه برای جنگ یمن باشن) ولی موقعبت الان کاملا جنگیه ! @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24292" target="_blank">📅 00:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیدبان اتاق جنگ : پدافند شهید رودکی قشم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24291" target="_blank">📅 00:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بابک زنجانی:جلوی استارلینک رو میگیریم، تکنولوژی در برابر تکنولوژیتون داریم
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24290" target="_blank">📅 00:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24289">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ew3yJvrNj3uM2RkyojgjUVwxuX_0c7r3ZGqKgFU6eUO089dJuD7-1nyJyidlBw6_PMGdBQE29xOpcH-oDmwFFj69kuCgqbY5lUK-fN4HtY7xSRaaj6NOCXKdDSBzSuvDZRCjFGauTZpEp8ELA5IbjK8w6Uo0ICMzMaFexHy0IPl_RlBg8IsksfeO7-QBimJbUkxKwATbxzSRXsuMokxWfCjONf_ThMt1Vs8ZGAlSKg5_iCXLc75e_M3fsHOw2yOOTrq-T_Q-ZxkRA9cyxfPAIL9Pt13mAfxB2q1qYYWqzy9PPidFQE901l4gdL2jwNZP-manU211AZ5MmsbxjC2Pcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست: دادستانی ایران پس از انتشار ویدیویی از اجرای نمایش «تهران پاریس تهران»، علیه گروه تئاتر پرونده کیفری تشکیل داد. ماجرا مربوط به صحنه‌ای است که در آن فاطمه مسعودی‌فر، بازیگر زن نمایش، سرش را به سینه مهرداد صدیقیان تکیه می‌دهد و او دستش را روی سر این بازیگر می‌گذارد. مقام‌های قضایی این رفتار را نقض «هنجارهای اجتماعی» دانسته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24289" target="_blank">📅 00:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سیریک زمین سنگین لرزید دیدبان اتاق جنگ میگه ممکنه زده باشن حتی
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24288" target="_blank">📅 00:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزیر خارجه کانادا : ایران تهدید اصلی است و نباید به سلاح هسته‌ای دست یابد. هرگونه حمله ایران به کشتیرانی در تنگه هرمز را محکوم می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24287" target="_blank">📅 00:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سخنگوی نیروهای مسلح ایران:
موشک‌ها و پهپادهای ایرانی پیشرفته‌تر و قدرتمندتر شده‌اند. این بار، ما یک غافلگیری برای دشمن داریم و در برابر هرگونه تجاوز احتمالی، از فناوری‌های نظامی جدید استفاده خواهیم کرد.
هر کشتی‌ای که از تنگه هرمز خارج از مسیری که ایران تعیین می‌کند، عبور کند، امنیت نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24286" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۳ پرتاب از سیریک  @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24285" target="_blank">📅 00:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۳ پرتاب از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24284" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">موج پیغام های  شما از گزارش عجیب ایران اینرنشنال توسط مجری افغان این شبکه مرضیه حسینی که مجاهدین خلق رو مردم ایران میدونه و پرچم جعلی اونها رو پرچم شیرو خورشید عنوان میکنه ! و پروموتشون میکنه ! @WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24283" target="_blank">📅 23:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24282" target="_blank">📅 23:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏افشاگری محسن حیدری آل کثیر عضو خبرگان رهبری در مصاحبه با تلویزیون قطری العربی تایید کرد که
مجتبی خامنه‌ای همراه پدرش بود و زخمی شد و پس از زخمی شدن پی در پی به سه بیمارستان در تهران منتقل شد که هر سه هدف قرار گرفته شد و در بیمارستان سوم از زیر آورها او را بیرون کشیدند.
‏محسن حیدری آل کثیر نماینده منتصب این دوره مجلس خبرگان از خوزستان است که در گذشته مسئول بخش عربی سپاه تروریستی پاسداران در خوزستان بوده است.
‏افشای این اطلاعات در حالی که پزشکیان در مصاحبه اخیرش در آمریکا مدعی سلامت کامل مجتبی خامنه‌ای شده بسیار قابل توجه است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/24281" target="_blank">📅 23:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ
:امروز روز بزرگی برای کارگران صنعت خودروسازی آمریکا و خریداران خودرو است! من به تازگی استانداردهای جدید بهره‌وری سوخت را تصویب کرده‌ام که دستورالعمل احمقانه مربوط به خودروهای برقی که توسط جو بایدن و پیټ بوتجج مطرح شده بود، را لغو می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24280" target="_blank">📅 23:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/24279" target="_blank">📅 23:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK2</strong></div>
<div class="tg-text">اونهمه سوخت رسان تو یه خط نمیتونه چتر باز باشن
یا پوششی برای ب۲ ها
اف ۲۲ها</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24278" target="_blank">📅 23:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صدای‌انفجار تنگه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24277" target="_blank">📅 22:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پزشکیان: اجازه نمی‌دهیم تنگه هرمز برای جابه‌جایی سلاح‌های آمریکا باز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24276" target="_blank">📅 22:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صدای‌انفجار تنگه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24275" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ_HcP9oMbIPKYIpQS3rrXS8e-7z_JbJlGrK3woXb1I7wHk4WN5vhIegPjb2copHvYTZrIgP0xlg5Fxf49il-h-TDNo2T03UhNPXuV5Y2ncuMfhfkcTNdZJCATldZKh_SLwE8ceopYHy3XpawqBSt0O_8V_gItBKdAIvwt5EXR_cg1iGzChyul2kilBhW3g7jgHVcYdTBIUmNbj3GUQZ7v8WrTMxGphRLg9qu1I6sCTw6-BhzIbtVMgjOD4o05YacORxhDDK5NNHAkd9luG-zTr7jY8lySDhCE_AAM2s1sbOupFVb60Mqlg6-nqx_biElnT7p7drVd4uP34D9cq2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث
: ایران نمی‌تونه سلاح هسته‌ای داشته باشه
@WarRoom
یاشار : پست باحروف بزرگ در چت و نوشته اینترنتی به معنی با صدای بلند و پرخاشگرانه گفتن اون جمله است</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24274" target="_blank">📅 22:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOoe9eDnZqVd-CHOnL2jcFjIgUmlaorHwUw9b-Mj2Aa51Xj43FO-OpXeO2w81cxkpGl9qDyEjtzjF7IBMuvHHwskcMzpRgsLcw38Dn7wc0p6RimXwn1ZVaRIcVT-MnL03x4DzITi2dbGnSUJWllgyONTT12WpzunTslwKIFfVzLZDGXds_EvKzKyfdbEo0PBPAz54Xh5Ssw2rqbrOdg2cld_oX4w-RtTA5T2D1lZgn-ErczCcpaYfVvb_wqfcYeUaPzNnB5jT-E_GmUC7CP_5UIZ3yi4E-LbUvlSSUFJ11KPwu6Zm7O3MHaTEtMTEholeghJc2vTyWRRKXp8UzUf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار ، وضعیت قرمز : ۹ سوخترسان در خلیج فارس و یک دسته سوخترسان با مالکیت نامشخص به سمت منطقه ! (دسته دوم ممکنه برای جنگ یمن باشن) ولی موقعبت الان کاملا جنگیه !
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24273" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پزشکیان لشش رو آورد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24272" target="_blank">📅 22:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جنرال جک کین به فاکس نیوز:؛عملیات نظامی علیه ایران اجتناب ناپذیر است. با شکست مذاکرات جاری میان ایران و آمریکا، مسیری که در پیش داریم شامل ادامه محاصره دریایی و هوایی و عملیات های نظامی گسترده از سوی اسرائیل و آمریکا علیه ایران است @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24271" target="_blank">📅 22:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها می‌خواهند تنگه هرمز را فوراً باز کنند. می‌دانید چرا؟ چون دارند از پا درمی‌آیند؛ می‌دانید چرا؟ چون هیچ پولی وارد کشورشان نمی‌شود. آن‌ها پولشان را از تنگه هرمز به دست می‌آورند، بنابراین خودشان خودشان را فریب دادند. آن‌ها گفتند: «بیایید…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24270" target="_blank">📅 21:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جنرال جک کین به فاکس نیوز:؛عملیات نظامی علیه ایران اجتناب ناپذیر است.
با شکست مذاکرات جاری میان ایران و آمریکا، مسیری که در پیش داریم شامل ادامه محاصره دریایی و هوایی و عملیات های نظامی گسترده از سوی اسرائیل و آمریکا علیه ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/24269" target="_blank">📅 21:54 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
