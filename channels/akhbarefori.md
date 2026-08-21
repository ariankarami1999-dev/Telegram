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
<img src="https://cdn4.telesco.pe/file/ifTA3EiV27UZq8zQLvkvwN_B6JfnNmcpm9BqRhbCQk263Kg817kKbsaVE_zuGZxLTxPz5W9e9xQVG9xNn3_bYYk_kItSCjYsuYcMdEc0g2Q5n6jS78zjsLW0Fv7IXaaXCEXcrYre5qyWPrGcWxQkYJQ5Qjoi8xAJs_Ony4DE_CPiNtmq0pb6RR9j1ceQxG-5m5-CS1KHcUt-MDWIHQ7pOsfWgHyM7nEWl3UwmYV290nQuREmorGJTUxMT2sIGbDHIPzZKooqRvVw-s6XCOBnhUm5brmVZtc7ZoOXr7QSd3Wk8W4BOEJ8wQH6ZKPTjDj33hvEih3Q_DvRagMA_ll5fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 13:28:15</div>
<hr>

<div class="tg-post" id="msg-683029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxhoYhCOHUXz924PL3_rULPilWyjVLxQDb3GP7ZAyCNeE3Kxn9ypvXCTFmWvympuvuGprhyU5SlaH3QVhBWvyLvRqMAJ86GD-RDM1W0kluS3X0GTQsgrdxgeqmAIPCipgowExpC6rjimcE1WMm-vt62aj2-QEmo2f7ajk-TkL-z3tkqTN_6L3pCuxuYE-VhTH3Y1NZcRozrx2YUwWei8mOiMmA13QhOHCfqb3cgO0fwJI1qVEXWwN6G0iqfTmN9RUhXJC-9IYB-Llw19tpC8uisVYqS82EpqNRgr_NhdhOGIefqSR1KpZrSDtpemMJLVAJeZGckOxzEoJpUtWqSYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبض جنگ با ایران برای آمریکایی‌ها صادر شد؛ ۱۲۰۰ دلار!
مرکز آمریکایی پیشرفت CAP:
🔹
شش ماه اول جنگ ترامپ در ایران بیش از ۱۲۰۰ دلار برای خانواده‌های آمریکایی هزینه داشته است.
🔹
هزینه‌های گسترده‌تر جنگ از جمله هزینه‌های نظامی، نرخ‌های بهره بالاتر و افزایش قیمت بنزین، مواد غذایی و حمل‌ونقل برای هر خانوار بیش از ۱۲۰۰ دلار بوده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/683029" target="_blank">📅 13:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OexPqmF3F1gyLiCySNifENxRLGYv1je0hVK2ZyzFaPbtktM7vTgcRo4mHdy_aOlvGTnAMDRRGGVT11h3SzFds6k1pIlycNRE38eDSja1i5uTQHt9kL18jo34LKvluhrNUZNP3jCmFySCEvNCVudLs7FNk3iW_suSrFlqt76evt-si3Hv_FrFnxjNQ2PCA_1qK9R2w5rmKQ_XAPEJzbTe53R36idwmVLX5DjWzjDv4TgsHh-ZEJgCAP0Mg755bHREsnvwgwfAm-ImXZ0-V2kyEjkgIUOZaUS1m9tPpf6mvK8pyrWV1zZoUgYrKCozECk8k9ogwM6OXhRrWLHOEGunlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ فرضی ترکیه و اسرائیل چگونه خواهد بود/ مهم‌ترین سلاح‌های آنکارا و تل‌آویو/ خطرناک‌ترین سلاح هر کدام چیست؟
🔹
اگرچه جنگ ترکیه و اسرائیل هنوز به واقعیت بدل نشده و بعید هم است که به این زودی ها به واقعیت بدل شود، اما بد نیست به مقایسه قدرت نظامی این دو بپردازیم.
گزارش خبرفوری دراین‌باره را بخوانید
👇
khabarfoori.com/fa/tiny/news-3238628</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/683028" target="_blank">📅 13:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83339bd471.mp4?token=lZWE_Ic-lvDQppPy2ROf0pN04kK_4ZfciNzamqooOMn5zto6dWh3X_1ZooD9u3FgFh_2LXVqCrZuRDC-jtxdIWMUun6EvYY6KPa8n12OtXZUi5ff3bC5LG39EYrYTGKbhzrJgy7qO_moA56JPRRhH7RNDwQ0eOo4naQAcjiOzbpDp1sd9gK06Wk_Kr5KlFEzljm44eVkI9ZV9QsewBvLzgQ_HDFyLstMgGgGIJxLATueikVGlZIpR8v3snF_Hn1BFCqyY_3vlQoygYu-9ITs0EVRYhAQTaCbo4My4eRM2kzzeg1MmrWNbEaoSkbHNpkL5oowlCQnftKK3yDZL5mbGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83339bd471.mp4?token=lZWE_Ic-lvDQppPy2ROf0pN04kK_4ZfciNzamqooOMn5zto6dWh3X_1ZooD9u3FgFh_2LXVqCrZuRDC-jtxdIWMUun6EvYY6KPa8n12OtXZUi5ff3bC5LG39EYrYTGKbhzrJgy7qO_moA56JPRRhH7RNDwQ0eOo4naQAcjiOzbpDp1sd9gK06Wk_Kr5KlFEzljm44eVkI9ZV9QsewBvLzgQ_HDFyLstMgGgGIJxLATueikVGlZIpR8v3snF_Hn1BFCqyY_3vlQoygYu-9ITs0EVRYhAQTaCbo4My4eRM2kzzeg1MmrWNbEaoSkbHNpkL5oowlCQnftKK3yDZL5mbGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس حضرت کی قراره بیان؟</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/683027" target="_blank">📅 13:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683026">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309bcedc5b.mp4?token=T-cGWtG7Q_rIlBr910P2W2kYQC25RvjiccJ3tPxs7p1DsbtHQtvKyf252MRATqWqX18gR9IW4WQS__x2HCVSMD9t3bpiFNAjrgzsCr_iAB4e_gbIa0j37EXkquEv_5zVK15NaOSzUoH-L5-iiyUAoBlzAXN7kTRXNG3LzjS9MdP3DT0BR6V8ayDbMHdv8jAneXWPHLZoPgbiT06I_v8B1IoOik9cXjQmIwv72pZMpqC9SqD4_qRE83JhYgrZrOBoY0wEW4rfXSKw74-l1U-K8xVPkf-kfKhkRcSgXzQrOzlZQ_bvJj5YbkVU4WOJ6nR8s8duCv8HSuHpy6IdmfOanENkECtVcvq_aEYW9pZ7bvxs4FfQFuZ7REIPmnEwCvtnDmNgObdRRZoZFb10LWJ_XUI1yj07hzcVi8Fj5--t0HgN7HRQrGPRajE3geCQZfiC2rzHGu2cWnR4YvAZQl5GfWxs4u3jbqWfxBCnCThLvsxMPchR7s6JrELYTn7oHpf7Z9rc2GViaiQx1m0UemnJMEVnWWnp5aqk9xKdkghce-YRksRl5RPHCzdp7Mq4_kzkp2y_gIJNMOLnwiHXGUPTCfDxSmTXQ5APkCvIMdFLleMQHeCPrVWdZH7Yh6ZsmpVu6zIjooRF1zQAegYj4dumHrghoRKrrVBC6RvSID0I6Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309bcedc5b.mp4?token=T-cGWtG7Q_rIlBr910P2W2kYQC25RvjiccJ3tPxs7p1DsbtHQtvKyf252MRATqWqX18gR9IW4WQS__x2HCVSMD9t3bpiFNAjrgzsCr_iAB4e_gbIa0j37EXkquEv_5zVK15NaOSzUoH-L5-iiyUAoBlzAXN7kTRXNG3LzjS9MdP3DT0BR6V8ayDbMHdv8jAneXWPHLZoPgbiT06I_v8B1IoOik9cXjQmIwv72pZMpqC9SqD4_qRE83JhYgrZrOBoY0wEW4rfXSKw74-l1U-K8xVPkf-kfKhkRcSgXzQrOzlZQ_bvJj5YbkVU4WOJ6nR8s8duCv8HSuHpy6IdmfOanENkECtVcvq_aEYW9pZ7bvxs4FfQFuZ7REIPmnEwCvtnDmNgObdRRZoZFb10LWJ_XUI1yj07hzcVi8Fj5--t0HgN7HRQrGPRajE3geCQZfiC2rzHGu2cWnR4YvAZQl5GfWxs4u3jbqWfxBCnCThLvsxMPchR7s6JrELYTn7oHpf7Z9rc2GViaiQx1m0UemnJMEVnWWnp5aqk9xKdkghce-YRksRl5RPHCzdp7Mq4_kzkp2y_gIJNMOLnwiHXGUPTCfDxSmTXQ5APkCvIMdFLleMQHeCPrVWdZH7Yh6ZsmpVu6zIjooRF1zQAegYj4dumHrghoRKrrVBC6RvSID0I6Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۰ لغت کاربردی زبان انگلیسی در آشپزخانه
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/683026" target="_blank">📅 12:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683025">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYCUCWKzZmBw7Fd-55ZMot1-IRSP37_LOb9yb6f3TsyVW8ZGlWK-L1pdA4ibG_S--f4jh59Wc59Krrt6HIQ6O0c7DkrjHFya8qnBwKgq0zJ5d481_3EZ4_muZwj_ht8oCj-kAUzvUVmF_2gFU10YRDKWloYAZeuranUMWjI7VG1FOVBwnuK4TDTGqhoqa839Ft9utJtDvdHfmgiS8R4flIEWUG8FcPsMjGPcSQAxogePQpadrmbn-Jp9MHdwCaYc2EB673jgkEA4GfTVaIRi2mu8uMTaC9vsXy7sn0-LENOLSw4virHqBCA4CZke6AWhJ7T6lJl71bwYlf_aOVxurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسارت به ۱۰۰ هواپیمای غیرنظامی در جریان جنگ
🔹
حدود ۱۰۰ فروند هواپیمای غیرنظامی در جریان جنگ آسیب دیدند که تنها ۸ فروند از هواپیماهای عملیاتی به‌طور کامل منهدم شدند.
🔹
حدود ۱۴۰ فروند شناور خصوصی غیرنظامی شامل شناورهای باری و مسافری محلی نیز در جریان جنگ آسیب دیدند.
@amarfact</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/683025" target="_blank">📅 12:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683020">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlEmdc_Kk2n8fmp7uLOfo-CPrbmQhkuo1x7X7HLWhWGlSNotS2cbSF6ZG5i0XXeQoyOjPN1Tw6ev66uHN3OWq8gPOnazjC7cOhzfc6zd24Y5JQU2wVNF6SVJWnEa6inLkdnM97WejvMjfr4m0cpn-AqEfzhpj8sVDXHS-_wrN4HJ4SIbTpdLSUAJskPD4Jl_-uoxqKaNy2CVCsuelozWbSu45Mp7SzY88ZksCccGLQedOBvYjcmqeRvk_aMJIRkPKTTWZY6jr9h5ZkMcXZOluYlXsvBMBQbvbQYHLPMRiTAFkKih9kpY7ICEvYhxUrhL7UX389cOlW2inA4JiY64gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K--CQOQX3yA3seY2YDe9FqvR9pTM9XDtNNVngW1ZLc7FEnZ2QccKdit4Ro5dFUAH7cZe2Ei65abtPK65Qfm3qc5NSAT-nj-oyt8FGYrbNYJO7MV_feSnRdaQfbX6zXujtfKVvczxB5MaghlxPKgWAwYOW_13wYNTsIcOXTHG1J4a6hONs1Dhx0x2UeG6gMpbiwJDQ4lUXV-BxyadUj8TFKe5kYiBy3QZtMQnwuIT-Zq6Qk5tgbegj8ByPCeV_3iv54fGQ7jjnmQ4nRRf6fG506yJ7LNVDcI7lzwNlXzCewJAdfcWL9YRc7Ob_N3Z9d0wB1D1gnpFTT_oeQ7aJr7BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfiJCSAPMolXsR4Dys-PIx474BMG6_rRwde6C8hnOIxhDI4OzQrXOD2yNjetAcZPbmsIxkEx_o3NogpWOs7pqi8PtTcit33QxbGcG_-rn_SN0r6LODyn6xlDH0K_POkd3-E0IyUtWPn8GawqTcFmy5cdjtkUTZ_bZlV-7vgGyedJ8I_pAOH6QvKCW70F_tPCTFsd_PYpxXCpzcMcvKvuy8oWyz7sp65BzXEAUcJ9ZCzlyf_VQq4Vj_vUqDdMQ2xh13urucQrWQZCXb2CTywGCSgxz-s1NQa2TxVbwiyWlERjCZenHvUlKzFnUnFvjcVwr8tfHcXel4VOyS0aPa-_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CekE95DMKd2F-ua4QquQCtGQ4O2e8JGstQZhmHuF5kd21WFFIgvn1cj9Ki5Cz6WYIzUMVauFxrRamlBtDeKDV8DygJ92_0iQynfAUX5ypvVrLOKIL1SkOKrkGC1l_LUHpyc2Rn-Ih-Q9ybKWdCZUpu152sKqoj225cjaiLf6LYajyFsTSFidpo29K6Lv5CIznZI5Q7U-41eJ0Dn-k87fPuVVnt6B28n5JVsUprNdRCthOvyHgnx2A5MiadcM7onwhLJKc8o5r8wafhE3TSJZqSoVmylruWOx3G1Ni9Oa0hv2_LBt_YA7rmHTcIUNTvuMycBR0Qo9QMVe6aQAKNTgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfPWN544NpW0fD-NDcRKfrdPVa9Wpp5be38DQA-8qVHQ_eqv-s4fLKcGPdgkMd_6HUyrU5keRhHERVP7yLyUleaf7vHtrAILCbUx5FOZsKM7QA0DfXtcn2DSGcBF-rhlQ6FP6ODhzYMe7HGOiOZ53VrOpDRSHB3QutLKhRMy3saF6II2EaEYv4vh7NCmGqS1joVyHWN1QUHX7d_BMjvJR_3g4o-FwQfwAUjsPsJL2Sk0PgoLYTzE7O0jThkP7PaSvUjws6WryPpF99s3lLi4q9kGtmX2FUnPTrSogd2YlZ2od7zVfCVmRpLy732PbbwmXenfUU-PRp_lF08o5mttUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالی بافته شده در عراق - ۱۹۷۰ که نام خلیج فارس در آن حک شده است
🔹
۱۲ سال بعد از دوخت این قالی، رئیس مجلس عراق به دنیا آمد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/683020" target="_blank">📅 12:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683019">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سرپرست وزارت دفاع: اجازه تجاوز به سرزمین و امنیت کشورمان را نمی‌دهیم.
🔹
عدم پذیرش کالابرگ توسط میادین میوه و تره بار تهران همچنان ادامه دارد.
🔹
ادعای پنتاگون: ادعاها درباره کمبود مهمات آمریکایی نادرست است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/683019" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683018">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b492a859.mp4?token=SgxGgP3KZBUhI_XmbrB6LIqmY_Bii8c3NR8-3hkN46sXFVX1MKw1Wih7qu49ShJ19VnC37gD7_z53JmT78AhGwRD3GTb-n5dnRUEWhzmJPBw3iI79x8W5-xt0N9A0lG28eYGIfobMrSvB2mYhrD26zkpBUA1OvYiaPwRrY3drYyDblKG5Ss6tCwYZk4d6CkpvY-UIE07Ups-WToQeEz3OUPivf9NXNo4Z3--CdgfKoCSIzMjLbA_KB3_ID1Hajh6R6BSkt7X51jLy65b8IGT2eebM-S3ZAxi-163ZHi1LJNJAkXCu4xlbTcZMj3sG9lbalH0A4q4XoIAzdhDelf5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b492a859.mp4?token=SgxGgP3KZBUhI_XmbrB6LIqmY_Bii8c3NR8-3hkN46sXFVX1MKw1Wih7qu49ShJ19VnC37gD7_z53JmT78AhGwRD3GTb-n5dnRUEWhzmJPBw3iI79x8W5-xt0N9A0lG28eYGIfobMrSvB2mYhrD26zkpBUA1OvYiaPwRrY3drYyDblKG5Ss6tCwYZk4d6CkpvY-UIE07Ups-WToQeEz3OUPivf9NXNo4Z3--CdgfKoCSIzMjLbA_KB3_ID1Hajh6R6BSkt7X51jLy65b8IGT2eebM-S3ZAxi-163ZHi1LJNJAkXCu4xlbTcZMj3sG9lbalH0A4q4XoIAzdhDelf5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور خطرناک جنگنده از فراز جمعیت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/683018" target="_blank">📅 12:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683017">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuHpfpuQso4eU3jvf2ptoLw6ELcT-lZHcg9skV7NyW8pt6GLf9oNQX6gzn2CB-N0HPOZfS8ITqeSLgkaJak8Inx7CxmrwED-cNGCnUoWzIlhhOerHGdmPNVseDNAZRn_e0mwuGHBj97ckMsWiPluxC8Roy-aX-gTXTmyrWDd9uCnCK2pld1aeoGXB3ArLMP-acEhxoO14yjx5Elgo1PMD7yYcWvKg-Y0WzIHqZp1vSiS6wFGtDFi5AUiAa7icgaEU8WW1HNqNdaVIT-vfz667lFWlwB5FcVOcmCCidujOoV83CCh_KZxEsDaGpn46SzmBQSAk6Fdyq7qsbmwGL5ksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ای‌بی‌سی‌نیوز: FBI از احتمال حمله پهپادی ایران به کالیفرنیا خبر داد
ادعای ای‌بی‌سی‌نیوز:
🔹
پلیس فدرال آمریکا (FBI) در روزهای اخیر به ادارات پلیس کالیفرنیا هشدار داده که ایران ممکن است در واکنش به حملات آمریکا، با پرتاب پهپاد از سواحل غربی آمریکا دست به اقدام تلافی‌جویانه بزند.
🔹
ایران ظاهراً در پی آن بوده است که در صورت انجام حملات آمریکا علیه ایران، یک حمله غافلگیرکننده با استفاده از وسایل نقلیه هوایی بدون سرنشین (UAV) را از یک شناور نامشخص در سواحل سرزمین اصلی آمریکا، به‌طور مشخص علیه اهداف نامشخصی در کالیفرنیا، انجام دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/683017" target="_blank">📅 12:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683016">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBr2NP3eMs4ubmf45VaaY4FLt9e-ZFoiGtaZJ5TAC8na0f2bmh_dTM81ofpp6wfEpsfwoL3uEgCs-8AY1LsWb7lNhacNrl06QDyQCf9yT4t8KyKKsyxYyyJ8Q_TyA89VoBCkZsyx4JM14esaqVVh2LihU-seYgolowLduZwDUMtUD817C8oOxFOnCQMULST8zH0dxqT4ObFRHcA86sPhR_hhfvlnGPjBweHKr16fNrXq84SXEw1NUcutpeex2oCzYqxaWpkPXelu6WWCqi7u4hcgH0glIsqVVvvUqnyacKdbQNdtKeG-wo7zTi8pBPN9tVt_nsLSf2ILzjg5f_qEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوسان قیمت نفت برنت در ساعات اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/683016" target="_blank">📅 12:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683015">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f30a0037e1.mp4?token=Lz5sVQf8hZUGhDVTpthU611Kr9vw4Xt-N_u7YNiLprl6Kg9MR52IubnSBuYgUvh-HxUTtDIxeXvX7iby_Rs5IpWow0OZQagGIaS09167kUoO3Whfl6a9Dy2WuBWuvvXJ6htYcBsTn-Ih1Ygkm4x3CV6d-Lc1Of5wcL-g_Fz8-3DwgXbQGL2CiscURsir0X2ZezrSpLDAiY6jCxdZwo7Lm3ULv1kJ8ZGcQgPxsbi0PegC6C76vr6tj9ApzatRUVNQzS92s7rDAPoR-Z-C41l2-OVM0FJ9DfFeNqxkcIfOS-6NcFlfaqteR_D3RH6mhFkk5tXEa6slsdrfQ6Eh44MkoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f30a0037e1.mp4?token=Lz5sVQf8hZUGhDVTpthU611Kr9vw4Xt-N_u7YNiLprl6Kg9MR52IubnSBuYgUvh-HxUTtDIxeXvX7iby_Rs5IpWow0OZQagGIaS09167kUoO3Whfl6a9Dy2WuBWuvvXJ6htYcBsTn-Ih1Ygkm4x3CV6d-Lc1Of5wcL-g_Fz8-3DwgXbQGL2CiscURsir0X2ZezrSpLDAiY6jCxdZwo7Lm3ULv1kJ8ZGcQgPxsbi0PegC6C76vr6tj9ApzatRUVNQzS92s7rDAPoR-Z-C41l2-OVM0FJ9DfFeNqxkcIfOS-6NcFlfaqteR_D3RH6mhFkk5tXEa6slsdrfQ6Eh44MkoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز «فرمول یک آسمان» در ایتالیا
🔹
مسابقات جهانی پاراگلایدر در ایتالیا با حضور ۱۵۰ خلبان از ۳۳ کشور آغاز شد؛ شرکت‌کنندگان باید مسیری حدود ۱۰۰ کیلومتری را بر اساس نقاط GPS طی کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/683015" target="_blank">📅 12:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683014">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw33k0QmzKbLbYa5u_f4cWZ3-fI-5YyN0QcR8QpHbqmWAVQFGXHC_CwLnqOEyiqW5Ftz7aWAIm4Iw9ohfQhg9yCsAZ_lzbH97jRYnc9BiAXP5TqZajkihI2SKOwOndXMK6EKdGh2DAT6_AOVPqkGpnmVcgYmAwM4t5h_R_xQVMPTbGIj_lV8BcZ8F8VyvfiCnL6zb4y-fuc7Co-MBCXzHuaoiM6eGSR6iI1JCYazIKZOzYWYd_llqDQmOlSO8lpVJNZcT3JABWoL_nT9QbcZ_u1LN_quM6D42gvlu_DebMbs60voQ2YSW2xv8rqVQv7ekiwI7b2YDbC9l_ZTInTdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۴ برابری قیمت موبایل در یک سال
🔹
افزایش قیمت تلفن همراه در یک سال گذشته، بازار موبایل را تحت تأثیر نوسانات نرخ ارز، افزایش هزینه‌های واردات و محدودیت‌های عرضه قرار داده است.
🔹
به‌طوری که قیمت برخی مدل‌های پرمخاطب طی یک سال دو تا چهار برابر شده و دسترسی مصرف‌کنندگان به گوشی‌های اقتصادی و میان‌رده را با مشکلاتی همراه کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/683014" target="_blank">📅 12:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683013">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=HF1dPgH_ztXqUjPO23DFmA19DML_ytkvGxgtT5JaP7NIvQ5p0VgsGaS6XLjHa55vDorca9hiSytX1IX0CgxK1uDPkoH_6b_kGdr8mDE07hIq9JMpc_7j40qFtwp6Yhf-Rj-4b6E2VaxyKZ49xoijFUlSRXYNpCAPdsI-eWc-rXs3JwdN75X9yzfZqNtJ-5FBntPBPSQy4Kc5bnHe68JlfKzqYb1YNLxCX6n1HG5BSEKzcW-SN46JVooVQk07dk5xeEStKCYgcO9no5CgalYKVBUFMxRO6iSPlmOTGDFHM3DrQHBms7UREPTpbprWK7smEGDK4TeUkFnJqaL91DRU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=HF1dPgH_ztXqUjPO23DFmA19DML_ytkvGxgtT5JaP7NIvQ5p0VgsGaS6XLjHa55vDorca9hiSytX1IX0CgxK1uDPkoH_6b_kGdr8mDE07hIq9JMpc_7j40qFtwp6Yhf-Rj-4b6E2VaxyKZ49xoijFUlSRXYNpCAPdsI-eWc-rXs3JwdN75X9yzfZqNtJ-5FBntPBPSQy4Kc5bnHe68JlfKzqYb1YNLxCX6n1HG5BSEKzcW-SN46JVooVQk07dk5xeEStKCYgcO9no5CgalYKVBUFMxRO6iSPlmOTGDFHM3DrQHBms7UREPTpbprWK7smEGDK4TeUkFnJqaL91DRU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساعات پایانی...
جشنواره ۱۰ سالگی "چرم مَنطِـ"
✨
تا %𝟴𝟬 تخفیف
✨
«تمامی محصولات»
➕
𝟮,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان هدیه اسنپ‌پی
با کد: PAYZ63R
حضوری و آنلاین
👇
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/683013" target="_blank">📅 12:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683012">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouT7AelUuh1jkEG4t9qZxWyv7NHEPJ6E4Ei_qqliaQTkFVKBWG5KDK9v4POV4ESyBqlBU5J3PkSd9tQMIHPTmV_jF_idLp0djz6vlXnJOmnB8ZAQ-EXyKI_uhKxQzcks2NXBsrOvzlP0SFV8zIarvwq6rBfWh4vzsHELCTfLDJYzfbt_SYQsnxj44m4bqmdKsx1WJASPPtdzV_AnpwtUtzi8nkIpCUoNDmh0JMSLPa7yq4JtvVgoBQQwQGk381IsugTlcQLgYUZINrkHf2GnBNDBn9xICiUe-uhOA7IRTYviFee2M0SD6grgU_yGkoq6fFiFHg1G2fA9GNdhuEtklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلتفرم چینی Bilibili برای رقابت با یوتیوب وارد بازارهای جهانی می‌شود
🔹
سرویس Bilibili که رقیب چینی یوتیوب است با راه‌اندازی نسخه بین‌المللی اپلیکیشن خود در اندروید و iOS، به دنبال جذب کاربران و تولیدکنندگان محتوای غربی است.
🔹
این شرکت قصد دارد محتوای چینی و جهانی را در یک پلتفرم ترکیب کرده و با استخدام نیرو در چند شهر جهان، فعالیت‌های بین‌المللی خود را گسترش دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/683012" target="_blank">📅 11:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683011">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کمیسیون انرژی مجلس: افزایش قیمت بنزین فعلا منتفی است اما برای پرمصرف‌ها نرخ چهارم اعلام می‌شود.
🔹
مذاکره‌کننده سابق وزارت امور خارجه آمریکا: تحریم های جدید علیه ایران نشان دهنده درماندگی آمریکا است.
🔹
معاون وزیر خارجه اورگوئه: اگر نخست وزیر اسرائیل به اورگوئه سفر کند او را بازداشت می‌کنیم.
🔹
چهار نفر به دنبال حمله یک هواپیمای بدون سرنشین در ایالت بلوچستان پاکستان کشته شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683011" target="_blank">📅 11:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683010">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQe3W5oIxbV7MYp2XNlEIeWHSCCNk6fT1aB_ngGRJnd6ps_cMxwKR-PgO8uWeU6zmwwWplGBivypDfxrectd4x6hQwD_yKV0IuSM06BeZ_P2JzNXAPgRC5Yut-WB44c6ztFjhqClfDG9uBK5v4EcA2vmSRfm0ya6CCZZRVZbtrbhuxaUJ-r4NGvqHqU7XqkhH5O4Vbi2S8w7UFOG0iOBwja0Tp6e9_l8ZM4hS-DxYdxQ3i50V0eGCMTBPHYspDb_Ps_hnyP5j3B50Uh8zRs7i7h2gccV96-QqJorwolSk006t2t1xl0bciD6vTA_RslbwT6TALzfuor1HRsHavCtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلتفرم توئیتر در واکنش به توئیت رئیس‌ پارلمان عراق که در آن از عبارت جعلی خلیج عربی استفاده کرده بود، طی یادآوری‌ای تأکید کرد که نام تاریخی و صحیح آن، خلیج فارس است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/683010" target="_blank">📅 11:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683009">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in_zX0PcppV-lQTjHV1GhfwvbKMHdie6GJME4T5uWLFjevj4IHPMg1gFy2zzX3rCRpglhXmdORXjEQ3ZsZJJGEUArSTf20bNb3QZdl9XUNAD4Fa29kwgcjmM_24cPxEGLKUu_FyomJbQiq2hn5_jCZODOBE8o1suzr6HFdUu4oqMA3YZaLLoCesx-Ko-fpksZ9HdLJmNaydHio-Xk_Zyp__uT-Jjzt2MZjpXFub1yVkNecIfjCAMjbr4h7DsHhPWZQatESbc5BB2KC29mjKCuUmq-aKjAPDW8OGpDK0-OEGkKzx4O1Yyvg2jBfCDkHDFJ-yG38ndtB82F_kyxi6pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ
«مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام:
حجت‌الاسلام و المسلمین سید مجتبی کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: محمد رسولی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما:
شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/akhbarefori/683009" target="_blank">📅 11:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683008">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
واشنگتن‌پست: ترامپ ناکامی مقابل ایران را بر سر عمان خالی می‌کند
واشنگتن‌پست:
🔹
ترامپ به طور فزاینده‌ای متحدان را هدف حمله قرار می‌دهد، چرا که پیروزی در جنگ با ایران دست نیافتنی به نظر می‌رسد.
🔹
از آنجا که قادر به وادار کردن تهران به تسلیم نیست، به نظر می‌رسد دونالد ترامپ، ناامیدی خود را به میزان بیشتری بر سر عمان و دیگر شرکای آمریکا خالی می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/683008" target="_blank">📅 11:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683007">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
خودرو جدید محمدرضا گلزار در خیابان‌های تهران؛ رولز رویس!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/683007" target="_blank">📅 11:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683006">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp5lcmmvBDMacDz98MDjK-0droc7_sin9suA32pb9vgRap4VOrPVxfIINZ72MBVPic6o2_vkgHJnYQbM639G67iRn4f_H8Tg-K6lbdjlSwFQzb_RwANa3ZevJuXPHuK5qt2FooJORGJr8ymTJekI9ZrTgUlpjPtp_ZLo5jhsvN8LT86e9Rm4EGgB3Uri-G3ErESaPdgWjf-mMADk7EjL55tL4J5ttUPIQ0V0yu93nBXXd5tNX6Qt4U87I0IsKFYzjXur-fZjwysIdFYnEMzgL0X5BWMs86RV_n2TTq9gBdZC7FzaWHV7b-qSciUcBU6hG-BdnaB3asIQJT6bdODp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارت وارد شده به یک کارخانه مواد پتروشیمی در دبی بر اثر یکی از حملات موشکی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/683006" target="_blank">📅 11:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683005">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNJWrtBPT00UQr-Z3oO7VWvNTUoVbHfntap9lSRk9-xeRB9EQrhFm9tlwjteaqagCY6sXGF8upBUgamvFOBcGzn2ugNwEhHko4r1fiE6M39_KI0-MEWLdX5omTeSk7c_vAFcCOLZExH-1Vqg-OWxtolIxSPgk7I3nBRHfA1Mj5VaivXOLRDwW4G38FXvji0XCBjKl4ftUy635QkNqdAg5vsIzrSocjaPbLqOv4FtHyZAQnwKhava7oNOWM-rsQ-HIfwaN08OXHtzC6rw6xI08HM5oeE-opZN2NMXysrrL-JgL1gCrinnWgNbH6d7buOnjdJUg9hffAfA5Htc-ZRnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجید شاکری: پاسخ نظامی ایران به حمله اقتصادی آمریکا ضروری است
🔹
هم معقول است؛ هم به موقع.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683005" target="_blank">📅 11:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQXOfzfA6LU0AtvdNGS6yy9sW02_rmU8ijdqtM2UyaqV-uzDwPOYwCPNjsWtcpkYvwdP6cKF-xnYJppfsidAhv9ZRXITEMMxAEO13R51VipFw0e-VI8O1Pfrs0uLhtJJD2ZXRqwJ34XnpKL7HGspm7gZMM5Raw4T7L7a6JIbutHoOTxWQlugG0t6NfLpmUGmoEuM2C3dFXSuptonjdYoeL2fw6lWwIB6AeiAZNmrGmOPgis7w59oEaIPbNVR9gBHKeaTvmvF4TzQ7PAtppXwCGoldOB_GhdciRzfqycdU5k7L5XTGO8hkaQR1dsowa-IJsvQIuTGKt1blZfuyNLWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بیت‌کوین از ۷۶۰۰۰ دلار عبور کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683002" target="_blank">📅 11:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683001">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtuLo6XkfsScl4PPogQUY7nNF8vJOtMzhmPyP3X82eV99sIcS153ceXS7QE-QF9hB18HWY9HEV6pbBoyQGpn_O8Y12XUGaQvMFpZoVYxjht60-n_UIfMJNfJOb-8oebIHrWEs6UflC1ubQ_css5963XVp0ymalU0X6e2PA4yLPObgYbK7r0s3XjrZ-yHiY3HMAEOOxDdwCxF1bq3nexO5EOvbiFC4CLaZhoRuoVXRnJVEQJdz6hCqjEi8ecyIKo7i0mhEyQuoQXwzwpF4aoUOoZiZJQbqBMqkwG9eu-ExANv2jz8ZR6NvQrzodiqtGD7dGQmjquxQSkxG6-RWsbCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/683001" target="_blank">📅 11:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683000">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=C8xHwdMWcNQFMQAx5ML36h-HVN6b2i6JSb5AASZWXtQ5hK6hKrIE154_rdk5wrIhWdAtqkBsUIz98dqjeRC3YStFenykyB_-Eqlzn3epik49TdVfkWRgHFSzPiWQBI0FPWNFkaCPx6OhlpGaJThrauU266JyoYijI55SEWsV3mtEaQkWn3lI4WuKp0QeFeAJFgXKBIhfMgYwMWlfGcl1rKysiYjznHvhmRWWoE80t08YQw_zbW9Kdztz6bzSZGaJ2AXy69h-6JQYNGMdjsRlNkk9-VzNNE3GGeRgoBdd265hIFuV4Yq3KgoJGq9_uRx7STEpvT4V1d_qwRZgQfqzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=C8xHwdMWcNQFMQAx5ML36h-HVN6b2i6JSb5AASZWXtQ5hK6hKrIE154_rdk5wrIhWdAtqkBsUIz98dqjeRC3YStFenykyB_-Eqlzn3epik49TdVfkWRgHFSzPiWQBI0FPWNFkaCPx6OhlpGaJThrauU266JyoYijI55SEWsV3mtEaQkWn3lI4WuKp0QeFeAJFgXKBIhfMgYwMWlfGcl1rKysiYjznHvhmRWWoE80t08YQw_zbW9Kdztz6bzSZGaJ2AXy69h-6JQYNGMdjsRlNkk9-VzNNE3GGeRgoBdd265hIFuV4Yq3KgoJGq9_uRx7STEpvT4V1d_qwRZgQfqzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایمان محمدی، کارشناس مسائل یمن: یحیی سریع از تثبیت ۳ معادله در برابر عربستان خبر داده است/ یکی از معادلات این است که نقض حریم هوایی یمن با پاسخ در عمق عربستان همراه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/683000" target="_blank">📅 11:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682999">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkyDTly7gfYqE_YmLXrKZo6jdoHC1w7rN_1cUkeuFSJLCbZXtBiPffkqnZ3rPGR43gENRZHj71msEZOABIv2Tl2_CMNpVJ8OcNcrVh9sBKkfylbf6rlT3W7Zo8Haaz58-fS8w5VrGk6aDl32ZikJA5XpW5VF4ugRbxVu1x2ewgCg_HJ0BgRtBBD-Qfsz_iFt7n7X3zQahVURaQlx3-kN9W8ma4Mzg-YiCN-W-6B878kEXgZaKtpN0lFvDziZWi7J2Zn6a6oCZApB_vZHt1DTxX_bq9XMtokDmsZSN1v84D1LfCL5G5kla62MTu_cHrSZist9-toDq_vljz2d1rXb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ
«مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام:
حجت‌الاسلام و المسلمین سید مجتبی کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: محمد رسولی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما:
شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/682999" target="_blank">📅 10:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682998">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس ستادکل نیروهای مسلح: پاسخ ایران به تهدیدات نوین دشمن ویرانگر خواهد بود.
🔹
الجزیره:چین احتمالاً واردات نفت ایران را با وجود خطر تحریم‌های ترامپ به صفر نمی‌رساند.
🔹
معاون وزیر خارجه روسیه: حتی توافق ایران-عمان هم تنش‌ها در تنگه هرمز را از بین نمی‌برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/682998" target="_blank">📅 10:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682997">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
نتایج اولیه کنکور ۱۴۰۵ اواخر شهریور اعلام می‌شود
🔹
رئیس سازمان سنجش از برگزاری کنکور ۱۴۰۵ با حضور بیش از یک میلیون و ۷۰ هزار داوطلب خبر داد و گفت نتایج اولیه اواخر شهریور اعلام و یک هفته برای انتخاب رشته فرصت داده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/682997" target="_blank">📅 10:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682996">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c13095e93.mp4?token=JB5wyj-wIsRCPrXZtD0ffE6sgQ9WkUILVwG-BEsjekBpitn0HB1gCt58xi5yp1K4t2Sx6--QXi3J04whOJaE2zVn8A_jDZj7duUh6LDRkRvcmZOs22VONtVt4M6nVmtMxdy2BDFpBROjlrLQrhqdA7QG0barHrNicP6JQNl-dS7QRoPnI0KM6YjU-6WatczT5irMk0wtV51xUOtskaTtrlckU_Lp3SCcehIUJ8-y-VN4NnPAWWBdgiPRtQohRoeYgVdAhy88FjquZlmGC8_6rtDhTEhPhfrrbYAmBl_Dnr5Rm2X21DMNTlG3ERK08lM9UqUHeJHZmH46eoiEa5oWkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c13095e93.mp4?token=JB5wyj-wIsRCPrXZtD0ffE6sgQ9WkUILVwG-BEsjekBpitn0HB1gCt58xi5yp1K4t2Sx6--QXi3J04whOJaE2zVn8A_jDZj7duUh6LDRkRvcmZOs22VONtVt4M6nVmtMxdy2BDFpBROjlrLQrhqdA7QG0barHrNicP6JQNl-dS7QRoPnI0KM6YjU-6WatczT5irMk0wtV51xUOtskaTtrlckU_Lp3SCcehIUJ8-y-VN4NnPAWWBdgiPRtQohRoeYgVdAhy88FjquZlmGC8_6rtDhTEhPhfrrbYAmBl_Dnr5Rm2X21DMNTlG3ERK08lM9UqUHeJHZmH46eoiEa5oWkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوش رایگان برای پارک جلوی پارکینگ!
🔹
یک مرد استرالیایی برای جلوگیری از پارک خودروها مقابل پارکینگ خانه‌اش، آب‌پاش مجهز به سنسور حرکتی نصب کرد تا مزاحم‌ها را خیس کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/682996" target="_blank">📅 10:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682994">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادامه افزایش قیمت نفت در بازار جهانی
🔹
قیمت نفت در معاملات روز جمعه بازار جهانی، افزایش ملایمی داشت و در مسیر ثبت دومین افزایش هفتگی خود قرار گرفت.
🔹
قیمت نفت خام برنت پس از افزایش ۲.۴ درصدی در معاملات روز پنجشنبه، چهار سنت افزایش یافت و به ۹۳ دلار و ۸۲ سنت در هر بشکه رسید/ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/682994" target="_blank">📅 10:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66d822e31e.mp4?token=n9CAOLeI66I4MULNdQ-NyMj3Bhg5cptxHSS7R6zuVXHntgVN63rWseeoqTwu6N_t2LerHNcLxnOiFBfTJEhIlhrfzCAE9xHFc6sTur5Hk6zkGP0l0xz8RtPAvgXg_-omH9l0fyhNA1tn534pRNOGU4BidWx7enMwR-KifPrX-r--oyOjQou_m3VVrr6MjE-4bw7bLmRGWLV9So2KmIAE5FdQ1ZH-i4xygXpD2LUS2m131kEDDM8al_2RrcBhSkCMg0tAhchVBsVMolCKLDznDWC6TfTVKD3SWS42Ufoo58dWh7s0K_Jz8Zaagx2Cu8C_Ot4MauzMj05gOiHsVVdtow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66d822e31e.mp4?token=n9CAOLeI66I4MULNdQ-NyMj3Bhg5cptxHSS7R6zuVXHntgVN63rWseeoqTwu6N_t2LerHNcLxnOiFBfTJEhIlhrfzCAE9xHFc6sTur5Hk6zkGP0l0xz8RtPAvgXg_-omH9l0fyhNA1tn534pRNOGU4BidWx7enMwR-KifPrX-r--oyOjQou_m3VVrr6MjE-4bw7bLmRGWLV9So2KmIAE5FdQ1ZH-i4xygXpD2LUS2m131kEDDM8al_2RrcBhSkCMg0tAhchVBsVMolCKLDznDWC6TfTVKD3SWS42Ufoo58dWh7s0K_Jz8Zaagx2Cu8C_Ot4MauzMj05gOiHsVVdtow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش خنک کردن کارگردان در دمای ۶٠ درجه عسلویه
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682993" target="_blank">📅 10:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682992">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC2rk10yGOr2PBg2I-P0sKpTodqfXbArphJB3m9JqyAJDFwb0NyNoqkiGYNo40yLyy-xl9gz6RdLMlgP_QVPzCjVh-1xajhghFC9kc56ZBd7dZywlIdJqb_V6DnUy4KBQDN0-uGgB-I2VlP1_1mSt06KQbyw6GjXqUwnHmQCEEcJlxMLtWCymxLHpducV1exaB4x0g1VuhG7IVZhOPm2RsfYHdpMK7XasyeC_pt9jpEvWgxwZFZRUdw5-1LQHd9aNfZTLGdh3xdRKYeKvUCMju1o4QdTQHLfo3Mx-j2HcmhFviMYnj9eX7rUtN1nX0zEpbkkkNzFCPbUo9ZkMgiEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکذیب شایعه بنزین ۸۰ هزار تومانی از سوی دفتر معاون اول رئیس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/682992" target="_blank">📅 10:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682991">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS3jVbc592u52QDi8071FdEqKTmpcDcNYLjSwcG1oYhnFEJaCOCTS7uo6w0vf9iYVdj3hPCnzfG0EvJYm8kzc5SsLY2UMpxTcyFtUd08-rMgIfPoxNypMXufdgs8tiaur4egpKOIKHaYajiK6UM7N4KTdmGCfmOxPh3Atb4qOtl7-F9HjOxJkhDzX5DMif_v3obzckNRmu2hSqnoYR_CrPhBo6UdpK5CRv_EIQ0XOIzn-fMkjNM4mM7cHTaVAdTtXuD4UJMu9mERcWib7TfDCyZqtZXnmBS1ZeeWyrY2cYZzduw_QbP2edYZowpz6VnTsuj0uoFlUKiFlMna0BIDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس جدید رونالدو در ۴۱ سالگی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/682991" target="_blank">📅 10:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682990">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02620d3034.mp4?token=YR0ZUZpLdQZRDkgy6Ov2771rECVia1L8rE6rMDZdE7AmomxxQyzYELnLNZWUijBhL1HoXYFyhlI5l-hNmSZ89p6SGiJ6m9WtYXocqjcv-NdtX67ZU2DHoKMNm7WyflhQPpFBlwkUYdmfs2pPZ8ZdZcwiBoxpXbjpD3sz8CrUlHtqeyQ9zJo2dSz1ATK7JRMz4ymLMEFVcg8k3gyMP1puKNEBqThdslnyrdSJhiPlr7tQR4VaNkWwsLEg8Cpy14ae-ZtiMmBROfZTj9V5V2ZVuwx1Xybu4mivlbTVfLXvIgRqMHTpdFCh1N16BMlYKXS7ONB5khN7lfEZMk_5SaotPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02620d3034.mp4?token=YR0ZUZpLdQZRDkgy6Ov2771rECVia1L8rE6rMDZdE7AmomxxQyzYELnLNZWUijBhL1HoXYFyhlI5l-hNmSZ89p6SGiJ6m9WtYXocqjcv-NdtX67ZU2DHoKMNm7WyflhQPpFBlwkUYdmfs2pPZ8ZdZcwiBoxpXbjpD3sz8CrUlHtqeyQ9zJo2dSz1ATK7JRMz4ymLMEFVcg8k3gyMP1puKNEBqThdslnyrdSJhiPlr7tQR4VaNkWwsLEg8Cpy14ae-ZtiMmBROfZTj9V5V2ZVuwx1Xybu4mivlbTVfLXvIgRqMHTpdFCh1N16BMlYKXS7ONB5khN7lfEZMk_5SaotPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک بشقاب غذا شاید جسم انسان را سیر کند؛ اما یک رفتار انسانی می‌تواند روح انسان را سیر کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/682990" target="_blank">📅 10:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682989">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس سازمان سنجش: ۲ هزار و ۳۴۹ داوطلب توان‌خواه در آزمون سراسری امسال شرکت کردند.
🔹
روسیه: در انتظار توضیح آمریکا و ترکیه درباره ارسال سلاح به اوکراین هستیم.
🔹
روزنامه عبری زبان: آمریکا برای دومین بار مانع حضور رئیس تشکیلات خودگردان فلسطین در مجمع عمومی سازمان ملل می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/682989" target="_blank">📅 10:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682988">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
الجزیره: چین و روسیه چگونه می‌توانند برنامه ترامپ برای منزوی کردن ایران را ناکام بگذارند؟
🔹
اهرم فشار ترامپ بر پکن و مسکو، دو شریک تجاری مهم ایران، محدود است.
🔹
روسیه هم‌اکنون تحت تحریم‌های گسترده آمریکا قرار دارد و تا حد زیادی خارج از چارچوب اقتصادی تحت رهبری آمریکا فعالیت می‌کند.
🔹
چین نیز بار‌ها نشان داده است که هرگاه منافع اقتصادی‌اش ایجاب کند، حاضر است تحریم‌های آمریکا را نادیده بگیرد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/682988" target="_blank">📅 09:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682987">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cffd8d88c.mp4?token=t6kjf7sivjul_9HnURns4o-dUWv0KmvVFsfHCS4_TTGjCFFjavTRSOTd10KY9YqibUPLJQQHgu7kEdNPdnIdTVaAIYC8xCdmz3NWl3sbDvFmMcVVpuNLiNq-0j-ninhl5PFxZoCivQU-34MEkWseXCmmRIK0YYl4QkQan7z-X-rItOK6zPC2xabBu5HSB2EuQxZzBIBSdY6VpcNk4Cf64KbZ_c31goLwt-sh1llIpdTDNyJfdNVEX-7fgCKwtgD0lrTDG6WCw0stZQJ78pKaYiKDrzsX-Zz18RNt7V9yyIA7EH5HCECPZe1zIc1Ehv_8h14rmo88VxV43ovzgQ3L9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cffd8d88c.mp4?token=t6kjf7sivjul_9HnURns4o-dUWv0KmvVFsfHCS4_TTGjCFFjavTRSOTd10KY9YqibUPLJQQHgu7kEdNPdnIdTVaAIYC8xCdmz3NWl3sbDvFmMcVVpuNLiNq-0j-ninhl5PFxZoCivQU-34MEkWseXCmmRIK0YYl4QkQan7z-X-rItOK6zPC2xabBu5HSB2EuQxZzBIBSdY6VpcNk4Cf64KbZ_c31goLwt-sh1llIpdTDNyJfdNVEX-7fgCKwtgD0lrTDG6WCw0stZQJ78pKaYiKDrzsX-Zz18RNt7V9yyIA7EH5HCECPZe1zIc1Ehv_8h14rmo88VxV43ovzgQ3L9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه عجیب در کجائلی ترکیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/682987" target="_blank">📅 09:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682986">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeXREZt33eC0hB_4q_U1JTOKg0tWEpTUrUcmEMeWUmXAGXQfkmc3Uuo5c0uBlU_8-fZzrFPXeXSJbkjcvNjLB0PeocgUYBFk_BZgsDJ_2g5cwzQk2N04sYTjhjftqY4wSiHzYxW5X7DBieSJO_R_-tSYf10YriaaB4q4zfE3frKj4V0RL1XwNAeMnqCfuHxlO4WL2cDWo-lBCSOfK64ITxh9xp4WrzBMgVN5wIYt5B9VCL_DkCK9zVEmdFAstsvoB555WR77ckKufHe9kxVUfGXL21KHX-_YiWcqx49lpquCqHDmbaXfyvLLfNBWqP3MXHoeySEhHzqXClE3zy3_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دماوند ساعاتی پیش
🔹
چشم انداز رخ جنوبی دماوند بر فراز دریای ابر و نور چراغ کوهنوردان در حال تردد در مسیر جنوبی دماوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682986" target="_blank">📅 09:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682985">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfb012d98.mp4?token=WwPZ_IMOLU5evsxGhw1dLQOT7rvTxaks5Cyuj79CS3-v2iCHLxjBggb1-5-cQlSp03Vf9HUwue9X07UQpKeupznY0Kuy8uVIq0Q2CYslZxemThwgCah5-izTNJiTG_gS9PeUl7aNkk0XIfosswVB-r0FAH_cBtywStjF6Ag1bCbOUTXofChoWPFnlSpytlS8bN8qYkR6yBhkoxoT4zFtrtmGIop9XwEWtpUcyV4MT-1bU7lcd7DCUevKpzhZdGXCmD83Xt4xadPJ_fuOKkmyypmbjJxGLJYup0_M4PcLkrNgyVyA74bMdVaMya8WzWfZjr6CjL6k_3A9OsPO85wnlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfb012d98.mp4?token=WwPZ_IMOLU5evsxGhw1dLQOT7rvTxaks5Cyuj79CS3-v2iCHLxjBggb1-5-cQlSp03Vf9HUwue9X07UQpKeupznY0Kuy8uVIq0Q2CYslZxemThwgCah5-izTNJiTG_gS9PeUl7aNkk0XIfosswVB-r0FAH_cBtywStjF6Ag1bCbOUTXofChoWPFnlSpytlS8bN8qYkR6yBhkoxoT4zFtrtmGIop9XwEWtpUcyV4MT-1bU7lcd7DCUevKpzhZdGXCmD83Xt4xadPJ_fuOKkmyypmbjJxGLJYup0_M4PcLkrNgyVyA74bMdVaMya8WzWfZjr6CjL6k_3A9OsPO85wnlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پترائوس: پایگاه‌های آمریکا در خاورمیانه دیگر قابل استفاده نیستند
فرمانده پیشین سنتکام و رئیس اسبق سیا:
🔹
ایران اکنون توانایی‌هایی دارد که پیش از این نداشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/682985" target="_blank">📅 09:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682984">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2abae3341c.mp4?token=RFAkOF3PA2IeT-cm0C2Nrz2BTJOkYMrTVMUYlcaQr9dx_78ZfTo9eK1C3DZyt3hh3en3K0-ILfLheKF7726m0tYRzzmMqdxFc2jSMH4wFlkRcdBQlpA53QIZteClTaF1V-WyFO0E_dvDnMBxIMT8CLINdVvR-OGJyzH-peeMTAP_atVNGszwGaAetdEkftrZzxYssub73vw6mZb5vLvS-55y5kR5dNrTPYUV5IP8EkRpDpPrCFHR-ntS5uw55MMTmglbx-jxuvR9ITi0vx5eQFWUHfJ1Of0IfQqpXvx5bk2at4pUxnSKI8IqTsi--bdq7YtEM4sUsBQsuW5NCn70OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2abae3341c.mp4?token=RFAkOF3PA2IeT-cm0C2Nrz2BTJOkYMrTVMUYlcaQr9dx_78ZfTo9eK1C3DZyt3hh3en3K0-ILfLheKF7726m0tYRzzmMqdxFc2jSMH4wFlkRcdBQlpA53QIZteClTaF1V-WyFO0E_dvDnMBxIMT8CLINdVvR-OGJyzH-peeMTAP_atVNGszwGaAetdEkftrZzxYssub73vw6mZb5vLvS-55y5kR5dNrTPYUV5IP8EkRpDpPrCFHR-ntS5uw55MMTmglbx-jxuvR9ITi0vx5eQFWUHfJ1Of0IfQqpXvx5bk2at4pUxnSKI8IqTsi--bdq7YtEM4sUsBQsuW5NCn70OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوری و مقوی؛ معجونی که روزت رو می‌سازه!
🔹
شیر نصف لیوان
🔹
کره بادام‌ زمینی ۱ ق
🔹
پودر کاکائو ۱ ق
🔹
موز ۲ عدد
🔹
عسل (دلخواه)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/682984" target="_blank">📅 09:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682983">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سقوط هواپیمای چارتر با ۸ سرنشین در آلاسکا/ همه سرنشین‌ها جان باختند.
🔹
آمریکا تحریم‌ها علیه کوبا را تشدید کرد.
🔹
قیمت هر گالن گازوئیل در کالیفرنیا روز چهارشنبه دوباره به ۷ دلار رسید.
🔹
هاآرتص: بیش از ۲۰ هزار کودک در جنگ غزه کشته شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/682983" target="_blank">📅 09:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682982">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: اقدامات امارات علیه ایران گام‌به‌گام خواهد بود
🔹
به گفته منابع آگاه، محدود کردن مبادلات با ایران از سوی امارات از پیش و در چارچوب تلاشی برای بازدارندگی در برابر حملات سپاه پاسداران به کشتی‌های این کشور برنامه‌ریزی شده بود.
🔹
مقام‌های اماراتی اقدامات اخیر را نه به‌عنوان قطع کامل روابط با تهران، بلکه به‌عنوان بخشی از یک روند تدریجی تشدید فشارها ارزیابی می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/682982" target="_blank">📅 09:28 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682981">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClNm2vLnWAhX39EYmPJHbKNJqT4Y2T-4yvPFeS1R7AgTQqFqTLcbkbFQptcsbidveAt1mU3pDMWl3QntqLgFld2yq5MAVcxOkqueqGuZSh-pQi7k0-cCPuYEIU7M-80bdOLlp-IjAh26Cpu47XdaunoF3N-kKa_6ZI9QudfXBzaZuP1U9K_H9k6huCQ16xVBL6FW-N41HnI9Ts8Lh3aQ2RJi1OAswid3HCo9dXbUahMj3IA_ThgDSLEFHXvCAjSPumqujlqzZW_XrA9JwoIM_nnn2XYoNOz25Mr8TuZwi9P1T38wUERnbponZs5wtzUByoPqe51aNmK1xIPnm3HIpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: ترامپ خواهان دیدار جدیدی با کیم جونگ اون است، کره شمالی به این سرعت موافقت نمی‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682981" target="_blank">📅 09:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682980">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4bbed5a7.mp4?token=fc_fCTErPvF6t_HOdYO9f_qaNpGkOhTPGAHHpooz5LYQmjPW0D_p5B-2RVn-JO9x8ulgSmhV78w_HP-d22edT6PSwfOAY0z51JHkMTMOOAnbbzRBR-nreztGfrwGoBgc2CkEH2VB7A5EgeG5K53sXwVFbnHCdfLaN7MffpfrB_N2Zu09IeE2lbgW5pJcNet4us6o7S4ir1ewMKPLCIvdgfCrdObu8Qo7SGYfj2OU3_Ns-HniadtOdu42Ei0HWRaGwC4KWDxcJ_3FsQjlpfnnX2uRXdYUFy_zlTNxEIttOtjUpKUP7ylendlqhiEJ53lPj9zCKyt1PvK-A73tYP24cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4bbed5a7.mp4?token=fc_fCTErPvF6t_HOdYO9f_qaNpGkOhTPGAHHpooz5LYQmjPW0D_p5B-2RVn-JO9x8ulgSmhV78w_HP-d22edT6PSwfOAY0z51JHkMTMOOAnbbzRBR-nreztGfrwGoBgc2CkEH2VB7A5EgeG5K53sXwVFbnHCdfLaN7MffpfrB_N2Zu09IeE2lbgW5pJcNet4us6o7S4ir1ewMKPLCIvdgfCrdObu8Qo7SGYfj2OU3_Ns-HniadtOdu42Ei0HWRaGwC4KWDxcJ_3FsQjlpfnnX2uRXdYUFy_zlTNxEIttOtjUpKUP7ylendlqhiEJ53lPj9zCKyt1PvK-A73tYP24cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان سنجش در خصوص قطع برق دیروز در یکی از حوزه‌های امتحانی: برای تکرار نشدن، تمام تمهیدات در نظر گرفته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682980" target="_blank">📅 09:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682979">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4aec1aa13.mp4?token=DtRVkouxvXkN3xfF0NahGubKrxuzQNwNbA-j5eftXBsQcJLp34cMppFG4xD43j7z37ddYHNEDkyJ3zSUZpzko7fSiEL2f9AfnPMzTiNXTziNTt95t8cWRGo8iQJ4tqdTb5qIjcywmJ8AwTtiajoDg96Kw4VInLe2kqYdpGzZ9wGoQgwFDTLCuX3nhszjgSEDwtmFOCI05kzCikR3Ey9mvq3cUHDtRl0rkUvagmhui_QO7fKHBZ0iS_e0nO_Ij6MGk45lteruLXADeaA30l_cAtyZFZhN5o8-U0UES_6UlvDRXJTKb86SWVEZwKBu8je5bzE3vTnPnHEeru6pN9R8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4aec1aa13.mp4?token=DtRVkouxvXkN3xfF0NahGubKrxuzQNwNbA-j5eftXBsQcJLp34cMppFG4xD43j7z37ddYHNEDkyJ3zSUZpzko7fSiEL2f9AfnPMzTiNXTziNTt95t8cWRGo8iQJ4tqdTb5qIjcywmJ8AwTtiajoDg96Kw4VInLe2kqYdpGzZ9wGoQgwFDTLCuX3nhszjgSEDwtmFOCI05kzCikR3Ey9mvq3cUHDtRl0rkUvagmhui_QO7fKHBZ0iS_e0nO_Ij6MGk45lteruLXADeaA30l_cAtyZFZhN5o8-U0UES_6UlvDRXJTKb86SWVEZwKBu8je5bzE3vTnPnHEeru6pN9R8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر روزی ۱ دقیقه برای یک ماه walk sit بزنی برای بدنت چه اتفاقی می‌افته؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/682979" target="_blank">📅 09:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682978">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
قالیباف: ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی و رشد اقتصادی نداشته باشیم، دوام نمی‌آوریم
🔹
امنیت و اقتصاد لازم و ملزوم یکدیگر هستند؛ اگر امنیت را برقرار کنیم و تداومش را با اقتصاد پیش نبریم پایدار نخواهد بود
🔹
ما به عنوان یک رزمنده، بیش از آنهایی که حرف از صلح می‌زنند، قدر صلح را می‌دانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/682978" target="_blank">📅 09:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682977">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aab236eb7.mp4?token=IrwqbuPvby-V_OcQz_DDb7WeJksQHTD5uZSklOoAoukzzYoOWwK9j07CpVjKalymv_VftWLlwVrMkDNncma9I7NkhONwNdD6BrlAGBa9Id3P8216W87blUTJY9Wz026r63QCrAvjPywdzJMEqrSGex2pwFEmMu7a8AGYSG_atY-GaKjHPFP1EP5sv4FMsrO2JVuhnn2zaNWjp5OBnclHb-hCua2yirsmuBxM3ugp0ncchzuQ4H7IWOFJH-OROZ7pFyolVC7gpnlzX1a3GjJtjobQUqKf9tKuvXdVdmZrUCbZ1jvwZ13mHK_kvGAbWW_3Sb2gkPryh75DN3VXZ7uvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aab236eb7.mp4?token=IrwqbuPvby-V_OcQz_DDb7WeJksQHTD5uZSklOoAoukzzYoOWwK9j07CpVjKalymv_VftWLlwVrMkDNncma9I7NkhONwNdD6BrlAGBa9Id3P8216W87blUTJY9Wz026r63QCrAvjPywdzJMEqrSGex2pwFEmMu7a8AGYSG_atY-GaKjHPFP1EP5sv4FMsrO2JVuhnn2zaNWjp5OBnclHb-hCua2yirsmuBxM3ugp0ncchzuQ4H7IWOFJH-OROZ7pFyolVC7gpnlzX1a3GjJtjobQUqKf9tKuvXdVdmZrUCbZ1jvwZ13mHK_kvGAbWW_3Sb2gkPryh75DN3VXZ7uvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیپ: پایان هژمونی آمریکا؛ ارتش دقیق آمریکا در جنگ با ایران در حال شکست خوردن است
رابرت پیپ، تحلیلگر مسائل امنیتی:
🔹
"آمریکا همیشه هژمون بوده و بزرگترین و قدرتمندترین ارتش جهان را داشته است، اما ما شاهد پایان آن هستیم."
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/682977" target="_blank">📅 09:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682976">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPzH9hArpvaa7DdhwOz_V6sIrSrxSInVxyQvwgIxSV7_G_8pL92u5XsYKtpY4qthtcFJdtJtmMdh340nYib7dRHk-pizvdz2B71uqIF5v3U5MTbDiR9ZUG4CeTyDKtHctNe9aU8XWYDnGABL6Aju93k7-l1ukqSlxIOEATVuLTqBg7FnIBan8XOoC7683bM_VuarNgcKDtYpnPwhoyQHn3ABiy3INhK_eCYHAh201k2sC0xg_73dsf9nBUayYoaNVjcX1djX8NoM278COOM2H0gBljgVmXrE5OgxAVmd9XQops_WuV5ntzibye2bBhvr1lSuq-jydEGmQtsCSLbx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جانشین اینفانتینو از آسیا می‌آید؟
🔹
رویترز گزارش داده که یوفا، ای‌‌اف‌سی و کونکاکاف درحال بررسی استفاده از سازوکار  «رأی عدم اعتماد» برای برکناری جیانی اینفانتینو هستند.
🔹
زدوبند اینفانتینو با ترامپ و پرونده فساد اخلاقی‌اش باعث از دست دادن اعتماد بیش از ٧٠ درصد اعضای فیفا شده است.
🔹
اگر اینفانتینو برکنار شود، طبق اساسنامه باسابقه‌ترین معاون فیفا تا برگزاری انتخابات جدید سرپرست ریاست خواهد شد؛ این فرد درحال‌حاضر شیخ سلمان، رئیس AFC است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/682976" target="_blank">📅 08:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682975">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
چرا عفونت‌های تنفسی در تابستان هم افزایش پیدا می‌کند؟
وزارت بهداشت:
🔹
عفونت‌های ویروسی بیشتر در محل‌های شلوغ و تجمعات منتقل می‌شوند.
🔹
برگزاری برخی مناسبت‌ها در تابستان و افزایش تجمعات می‌تواند باعث بیشتر شدن بیماری‌های تنفسی شود.
🔹
تغییرات ژنتیکی در برخی ویروس‌ها می‌تواند باعث شود بیماری‌هایی که معمولاً فصلی هستند، در فصل‌های دیگر نیز دیده شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/682975" target="_blank">📅 08:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682974">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFJ8fL3RRJmZb0vX323JdJHcyK0f_X0WTG2GWYMRW4RpdEu29GME6P_U1XMi3H89wxqMsI6SLPvUX7x8FSYYv2fDiFjkJJg0JlMuLax5bL7MgHLMy8Z6a5GBjkJOb0W3iWcj1LUGuq4ba9uh6srcLx5JNRTVSa8wDlTYuzdXPZ8jqiF9AIpBsXRrj9gX94ycSzpxx4OH9GUD-nqx1o9gzv9FAl0Qc1T0L6VFbeDdjhMaY9uAS1TCN3Tc83ifXUiR_0hYXUFVb9UuZh_csmAAXoktOe0NIGvJpvezmMKlxW5Y0gL4iXV_ybMq4KCbh2430Knt65e5v8iOT3bPhEYLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برد زنان والیبال ایران در قهرمانی آسیا با ثبت رکوردی تاریخی
🔹
تیم ملی والیبال زنان ایران مسابقات قهرمانی آسیا را با برد مقابل چین تایپه آغاز کرد و برای اولین بار در تاریخ به جمع تیم‌های ۱۰۰ امتیازی جهان وارد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/682974" target="_blank">📅 08:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682970">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b896b84a81.mp4?token=kpZqBaFHw16lUs5ThYxAt_ht2pU8TJPzD-6UWak2g8z6Dt90JLWBPxB1ezmsI558Ea7m_6ny_nIY8JEYcgmEsAyXrqCcc9gWPVTow5OmMzQfZAK6k5WihWG9rkzssEktsQCDYoceQSPKMtU1I3mHesRojM5nDpUtaWD49HuN9yyUHkJbLJlrCu-q5SIKYBQP2oZVq6BMX2rR0v82ics3Nc9vx8Ry9QyK3YGi1tifg6sxqPPbRCKURR6T0yrp1gOFuJFo6Ma8FQeaWVxXdc1-U8qh1-7ocr1cX4Wx5rhlcttbRg_M38SarYMgpj4lUWzlbE3lK4TM0aNgFk8nT4LKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b896b84a81.mp4?token=kpZqBaFHw16lUs5ThYxAt_ht2pU8TJPzD-6UWak2g8z6Dt90JLWBPxB1ezmsI558Ea7m_6ny_nIY8JEYcgmEsAyXrqCcc9gWPVTow5OmMzQfZAK6k5WihWG9rkzssEktsQCDYoceQSPKMtU1I3mHesRojM5nDpUtaWD49HuN9yyUHkJbLJlrCu-q5SIKYBQP2oZVq6BMX2rR0v82ics3Nc9vx8Ry9QyK3YGi1tifg6sxqPPbRCKURR6T0yrp1gOFuJFo6Ma8FQeaWVxXdc1-U8qh1-7ocr1cX4Wx5rhlcttbRg_M38SarYMgpj4lUWzlbE3lK4TM0aNgFk8nT4LKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گردباد و سیلاب در شرق آمریکا
/
نیویورک و نیوجرسی زیر بارش سنگین
🔹
طوفان‌های شدید شامگاه پنجشنبه بخش‌هایی از مید-آتلانتیک و شمال شرق آمریکا را درنوردید و با بارش سنگین، سیلاب گسترده و دست‌کم دو گردباد همراه شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/682970" target="_blank">📅 08:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682969">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
رویترز: تعداد کشتی‌هایی که روز پنجشنبه از تنگه هرمز عبور می‌کردند، کاهش بافت و تنها ۷ کشتی از این تنگه عبور کردند.
🔹
رسانه‌های اسرائیل: ترکیه قصد ارسال سلاح به سوریه دارد.
🔹
وزیر امنیت داخلی رژیم صعیونیستی: زندانیان زن فلسطینی باید رنج بکشند و اعدام شوند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682969" target="_blank">📅 08:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682968">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آزمون سراسری سال ۱۴۰۵ تا دقایقی دیگر آغاز می‌شود
🔹
امروز داوطلبان گروه آزمایشی علوم تجربی در آزمون سراسری حاضر شدند در این آزمون ۴۵۱۵۲۲ داوطلب شرکت کردند که در این آزمون ۶۹ درصد خانم و ۳۱ درصد آقا هستند.
🔹
همچنین بعد از ظهر امروز آزمون سراسری زبان‌های خارجی…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/682968" target="_blank">📅 07:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682967">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
واشنگتن‌پست: ترامپ گزینه‌های چندانی برای تشدید تحریم علیه ایران ندارد
🔹
روزنامۀ واشنگتن‌پست با اشاره به تهدیدهای شدید ترامپ برای افزایش تحریم‌های اقتصادی علیه ایران «در ابعادی بی‌سابقه» نوشت که او گزینۀ چندانی برای جامۀ عمل پوشاندن به این تهدیدها ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/682967" target="_blank">📅 07:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682964">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
وزارت امور خارجه چین اعلام کرده است که تحریم‌های ایالات متحده علیه ایران را به رسمیت نمی‌شناسد و چین با کمپین جنگ اقتصادی که این هفته توسط ترامپ آغاز شده، همکاری نخواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/682964" target="_blank">📅 07:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682961">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU1FEusBxAT9fMtrs5rn5ol7qp1yQPVfo4eQL4AiQm-jDIH6mmcYOALxMwXUabUUqkZZCLQkv0aLFOeHu7Hi0LkGKtdZlreedZKsLTl_M9MG8jM9cAXf7ahvFvU9rwWmr25WB4D_HDFdujYtOLU3Ilk_wJvp8SCnkTBU6adlym0d5OPoU9IDi9XW-GrOvLHSV1Xfpl3ArE5-KKFlu8lHobAYxsq6rLphIZ_KtAIEJfB8s14BTUtqEtJamTPOYdf8SJpanuiuvts_6IBDqI3tH8YFfBNhjJs7rghZ3Rs7xbrHTDN5TejiaMnlbxkQK_9-5tHZsrdNWuk2LArYHBHRRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جاه‌طلبی بی‌سابقه ترامپ برای ثبتِ نام خود بر یک ناو هواپیمابر آمریکا
🔹
نیروی دریایی آمریکا در حال بررسی تغییر نام یک ناو هواپیمابر در دست ساخت است که قرار بود به افتخار «دوریس میلر»، ملوان سیاه‌پوستی که در جریان حمله ژاپن به پرل هاربر به قهرمانی مشهور شد، نام‌گذاری شود.
🔹
سه منبع مطلع گفته‌اند که در دولت ترامپ، بحث‌هایی داخلی درباره تغییر نام این ناو و احتمال نام‌گذاری آن به افتخار خود ترامپ مطرح شده است. چنین اقدامی بی‌سابقه خواهد بود، چرا که تاکنون ناو هواپیمابر آمریکایی به نام رئیس‌جمهوری که در قید حیات و در حال تصدی این سمت است، نام‌گذاری نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/682961" target="_blank">📅 07:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682960">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEVcff4_MguixeRsx0OuR0y4gx1uL8T_xbPtmGZQZ_A-r0gjgEfIbHSsPH4pD17r8ArgbjPvDeDtn7hE0fQIUG7rQGyVenpJ_qqPOW_cONpPIpx0wX2tb7NV16i70zpFRmWd2VvVSJBlXz6Nc-PLsJgl01GYzjtCX28_1LtDr5KW_6TM27LRNrAIpTez_5_dWJpt-Lpz9WsOplmyFRz9c1RKgdYSMLMpnenthuUj7Rfe61Amk1FI99HCtSaJFYQkF9v4dooUZeSsISWKEjtwA3O7nm8ZW7PkrO-H_SFkpBf-9IjlRJUxDm_Unqu4upI7X_r0avl6o5V01C8g7gDmxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۳۰ مرداد ماه
۸ ربیع‌الأول ۱۴۴۸
۲۱ آگوست ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/682960" target="_blank">📅 07:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b985c5d06.mp4?token=GTfGqoCYfSIRYkO471JS1XVNy6PCeWy2oxX0wKIetjCroZEUdBz9G0y6oJMW961h6G8B4BcZiDNCynGRv2zj85rZjmKgVmieOqAdRYuwPN8r6mmjTgDEhCs47VtTfayqpAiNifjzWLvoGrhSAY8y4ef6we065ADJfSl_L5LqGIx16FHQgRS8WwwFLXA9aLa2JsbmmFTpeescwoVrfGp3hBAyhXA6AGXvkwzr9cktVLDzMuaD3Px3sDVIyHK7KCedyxr07rjdoKOKjHEz99uBu6iBqYLJwfObMSELSQsCUhuQdiu8YxrHCa14oHjxae_IVnA8ju0D38oV7-9TxGrMz6OrPOSTBD4Z0a3YTt96V3WnlHOT6fyhMaFv433F7KjkDPxmiCm2ieQM5NX4mg6wARY3cOl0pkBbCwf2kJsG_V1gm2buzo8nZu1rSATnFu5ReSUAq0_3ofMoPhVnmuF6yUM_QiWLFshBTjaWnNzGjL8TBoUVQQXRQDGr3XzdHH1ag2WR7JBLL2rsbWEFDfNdGXkFu7ITdjhOTSpf8zOVrdbgNnbrR_yWw-v2NreN8UxUEnEgzq2yNhXFXwNMvpdYmO_QUx_j9EXR4N14IVw9YLJNwSP2ZlVauTxEGnxDFSZwbqTYpixD8QbFjpgW6bvp-8Qf9fl3CmA78OLUxQVj6N0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b985c5d06.mp4?token=GTfGqoCYfSIRYkO471JS1XVNy6PCeWy2oxX0wKIetjCroZEUdBz9G0y6oJMW961h6G8B4BcZiDNCynGRv2zj85rZjmKgVmieOqAdRYuwPN8r6mmjTgDEhCs47VtTfayqpAiNifjzWLvoGrhSAY8y4ef6we065ADJfSl_L5LqGIx16FHQgRS8WwwFLXA9aLa2JsbmmFTpeescwoVrfGp3hBAyhXA6AGXvkwzr9cktVLDzMuaD3Px3sDVIyHK7KCedyxr07rjdoKOKjHEz99uBu6iBqYLJwfObMSELSQsCUhuQdiu8YxrHCa14oHjxae_IVnA8ju0D38oV7-9TxGrMz6OrPOSTBD4Z0a3YTt96V3WnlHOT6fyhMaFv433F7KjkDPxmiCm2ieQM5NX4mg6wARY3cOl0pkBbCwf2kJsG_V1gm2buzo8nZu1rSATnFu5ReSUAq0_3ofMoPhVnmuF6yUM_QiWLFshBTjaWnNzGjL8TBoUVQQXRQDGr3XzdHH1ag2WR7JBLL2rsbWEFDfNdGXkFu7ITdjhOTSpf8zOVrdbgNnbrR_yWw-v2NreN8UxUEnEgzq2yNhXFXwNMvpdYmO_QUx_j9EXR4N14IVw9YLJNwSP2ZlVauTxEGnxDFSZwbqTYpixD8QbFjpgW6bvp-8Qf9fl3CmA78OLUxQVj6N0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی منتشر نشده از دیدارهای صمیمانۀ خانواده‌های معظم شهدا با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/682958" target="_blank">📅 06:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
دلیل‌تراشی‌های ترامپ برای توجیه شکست مقابل ایران ادامه دارد
🔹
دونالد ترامپ در میانه فشارها بر دولت او به دلیل آغاز یک جنگ ناکام علیه ایران تلاش کرد از اقدامش دفاع کند.
🔹
او بار دیگر مدعی شد که نیروی دریایی و هوایی ایران را نابود کرده است. ترامپ همچنین گفت…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/682957" target="_blank">📅 06:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682950">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
دلیل‌تراشی‌های ترامپ برای توجیه شکست مقابل ایران ادامه دارد
🔹
دونالد ترامپ در میانه فشارها بر دولت او به دلیل آغاز یک جنگ ناکام علیه ایران تلاش کرد از اقدامش دفاع کند.
🔹
او بار دیگر مدعی شد که نیروی دریایی و هوایی ایران را نابود کرده است. ترامپ همچنین گفت که چاره دیگری جز جنگ نداشته است.
🔹
او در توجیه دلیل ناکام ماندنش برای توافق با ایران گفت: «انجام معامله آسان نیست زیرا سران ایران را از بین برده‌ایم.»
🔹
این در حالی است که او چندی پیش ادعا می‌کرد که به دلیل ترور رهبران ایران اکنون آدم‌های کاملاً متفاوتی روی کار آمده‌اند که با او تعامل می‌کنند و آماده توافق هستند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/682950" target="_blank">📅 02:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYlQzmQok7sjyl3AlhWqkqWGdm5CkM8GiA4QtJeYvZKxuK-hOLzuD0_tbPAuVHKHdonNDoJvWEVDpjHvTjimFM5WRcIPRdAdH4ld6kUrIgnucWXrKDnxipXuBhutR7_aMUBgiQHFeM8sefvEPATjs88ZXAOQubEPD0_QMgCBgtotcJ3FlJ5rllwhIxpEUyzYMFwldJxgGDQrJrZT-ecATSdt0s1yWBhNldJC7fBZtYzNtYQ9OyHfAx19jV-MRf47qkZMSyihfpZqdU3f92OQF8TtBcIhDOZohTLvb-Zn9nNrWsfDInnpe-iP4V7XJfP43NUZPYOP3KQ4vH1vNagX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به یاد آن سحرگاه جمعه‌ای که پیکر آقای شهیدمان در جوار حضرت رضا علیه‌السلام به خاک سپرده شد
🔹
ای تازه بهشتِ این زمین دارالذکر
ای آینۀ اهل یقین دارالذکر
ما هستی خود را به امانت دادیم
پس باش مراقب «امین» دارالذکر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/682948" target="_blank">📅 01:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682946">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0655d59c4.mp4?token=eGQxqONekQ9ib64Ny5ZPnl8BwgUBNmeVAyRLx6JM9009LJdEV_SEl1YoabrCMwKNTaFKtbwa9eJXugNgsi64K1v__3_TPCv-fZkMFlZ5WZg4D362vdB_yW0hQLRgtx583OISBiUUfxG9x-tCJHPSdcqyCtsUIGRosrUAGBeIZ7Pqr8UwdroxTtOk6BzWH5nKdYeueGc3m-ba3_Bw2IwGsWXC7xkq_gTlCwo-7mNGXSkEZMbE3ZnoPZyeWZEVFpmgZqgWGBux5QRSVpIIIumNQt7caIX1hYORv6-CoIq3s_VQ6l7-8lOF8O1Ocx6AzpeLH_Cuke2d2Se-TxO1VtQhxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0655d59c4.mp4?token=eGQxqONekQ9ib64Ny5ZPnl8BwgUBNmeVAyRLx6JM9009LJdEV_SEl1YoabrCMwKNTaFKtbwa9eJXugNgsi64K1v__3_TPCv-fZkMFlZ5WZg4D362vdB_yW0hQLRgtx583OISBiUUfxG9x-tCJHPSdcqyCtsUIGRosrUAGBeIZ7Pqr8UwdroxTtOk6BzWH5nKdYeueGc3m-ba3_Bw2IwGsWXC7xkq_gTlCwo-7mNGXSkEZMbE3ZnoPZyeWZEVFpmgZqgWGBux5QRSVpIIIumNQt7caIX1hYORv6-CoIq3s_VQ6l7-8lOF8O1Ocx6AzpeLH_Cuke2d2Se-TxO1VtQhxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای کشیدن نقاشی سه بعدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/682946" target="_blank">📅 01:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682945">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIbLD1euGoHSVpT3LG0I-a391wiEPlV2gwX_albnNEcT4U5e0xEi-5pPD0OPjk9mPYd4DMzaDNtb6SGUnTGrOumtHj5YfdkwWVFEMNIj6NxEeuHSoNCv66F6B8uF22AZCWbVW46UaD1WomGzgU1rU5HCrw81HczWgIZoLkKkObXNLtIOMeM-c8FrP0E2u27T_7EGxMXb7Io7bfMUA86fBN2cI_F0uTgFQ_Ekig0CAMdz4Y9P08mRJN4rmuTAONtB6VWjGPc8_ZeoEoEoLJftjeO7Ih-3ll_speFCOOVmLIRhpN-m9I7l0sBvqltWeMIyXdxfuOemSLao9vhDRcGHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی در واکنش به پست ترامپ: جمهوری اسلامی فرعون را به زانو در خواهد آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/682945" target="_blank">📅 01:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682944">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e460f436ee.mp4?token=T5Crn-TSUZgvlr_lBgTBv6G8y9Ux3dAJGvbFQUVkqf6iOrf5i64i5jqsqAyhyc2s9BWObvL1U0fnpZ2PCEUk_V9eTa0ni_PFQ7OURMUaFnoJyx539BqJ2vIvdLyU8aE0NooF1Hl7bht3VyT4MkKWJVMGRlzPTsJRZgLkzHvhU9u7Kj5quauaMMMHvWLWsAnc35E9ojh1S_BWcRBb6H3jGX3hCR0C8kk-op-TE3pCCHGtArhsPRPySDzAQTUtz7zhLxKfcjlRUQ8rigq8jTOzP_0oM2FohyS0q6qxW4UzfkToYQ8WyvPe08Hewj2jBl2C7OQ6tloW0gnqxSuLPT9AaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e460f436ee.mp4?token=T5Crn-TSUZgvlr_lBgTBv6G8y9Ux3dAJGvbFQUVkqf6iOrf5i64i5jqsqAyhyc2s9BWObvL1U0fnpZ2PCEUk_V9eTa0ni_PFQ7OURMUaFnoJyx539BqJ2vIvdLyU8aE0NooF1Hl7bht3VyT4MkKWJVMGRlzPTsJRZgLkzHvhU9u7Kj5quauaMMMHvWLWsAnc35E9ojh1S_BWcRBb6H3jGX3hCR0C8kk-op-TE3pCCHGtArhsPRPySDzAQTUtz7zhLxKfcjlRUQ8rigq8jTOzP_0oM2FohyS0q6qxW4UzfkToYQ8WyvPe08Hewj2jBl2C7OQ6tloW0gnqxSuLPT9AaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت کیف پول و کارت با چند تکه مقوا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/682944" target="_blank">📅 01:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682941">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سالی یک متر از آب دریاچه ارومیه تبخیر می‌شود
محمد کوهانی، دبیر ملی شبکه‌های محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
سالانه حداقل یک متر تبخیر از سطح حوضه آبریز دریاچه ارومیه را داریم که طبیعی است. اکنون تراز دریاچه به ۱۲۷۰.۹۳ متر رسیده که نسبت به سال گذشته، یک متر و ۱۳ سانتی‌متر افزایش داشته است.
🔹
همچنین وسعت دریاچه با ۲۸۵۰ کیلومتر مربع، نسبت به سال گذشته ۲۲۴۴ کیلومتر مربع افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/682941" target="_blank">📅 00:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682939">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ0jTfUliz_EeDtDTJEN5n6yow7LdFokZW0-GB8qpbljLmIbdOU1FKxqX4arhEF_VY1ZyZC2sl-6uYkozxSLibpGF4lDoyuiqs5AvCrtr0yKR8SXftLoggjLSVJGUMEEOjnoXlVI8L6P8zmo_Az6S5CG3Sc3ndh74YRBFWjKqrckkXkmUlUM2v_Q-BSqh4ZKhss_KGm8qIaOmzTYMoEUs-EzgcHndBnR7eT9S1vaueNPIQoRbRDTrGPTCsTUM79KspZzMXZncXp33qj_qvYtSTlHoXoyJ6X-oabhZZ7xD9VlSEBIAv48hfN37xDGSK3aiV2Cql3ZIxwbcXXHdbDQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش فارسی آلن ایر، دیپلمات سابق ارشد آمریکایی، به تهدیدات اقتصادی ترامپ علیه ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/682939" target="_blank">📅 00:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
افشاگر بحران در ناو لینلکن وادار به استعفا شد
🔹
مقامات آمریکایی به سی‌بی‌اس نیوز گفته‌اند که مسئولان پنتاگون در حال بحث و گفت‌وگو درباره برکناری ناشر قدیمی نشریه نظامی «استارز اند استرایپس» (Stars and Stripes) پیش از تاریخ بازنشستگی برنامه‌ریزی‌شده او هستند.
🔹
رسانه آمریکایی نوشته دولت آمریکا به ریاست دونالد ترامپ در حال برنامه‌ریزی برای بازساری کامل این رسانه نظامی است که بخشی از بودجه آن توسط مالیات‌دهندگان آمریکایی تامین می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/682936" target="_blank">📅 00:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec764cbf3.mp4?token=Sb7zjjyH4nlaWTwIKMC_G62GB_7vlR-3_R6BCbmhmukhRDuzUvfugAJBnmT_tA7PJFWIrllSteNnAQ88EhpVijlQDufqyPTk4GMwxj9Oks6kjGZsMw07C86FeRj6WsXSxtPNqvsaF5BSDQpa7boFxavL-MX1SKk_WEXYBfH7DtooiNXOt3HhWFwV1iwxhePGaEf6hiGLO-1mkL6jIR9xV6kizJR4UYGxFYNI-UC-Oto-8eFtnaFRQQ5mFb0lc48ghY8ZUxkuQLbhoKhx9id5zsadpikSszPOZKOQSnWYL8BoeAeAjpP3KBnfeIdQgII3BQlQXy7XzVJC9uQTGAbCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec764cbf3.mp4?token=Sb7zjjyH4nlaWTwIKMC_G62GB_7vlR-3_R6BCbmhmukhRDuzUvfugAJBnmT_tA7PJFWIrllSteNnAQ88EhpVijlQDufqyPTk4GMwxj9Oks6kjGZsMw07C86FeRj6WsXSxtPNqvsaF5BSDQpa7boFxavL-MX1SKk_WEXYBfH7DtooiNXOt3HhWFwV1iwxhePGaEf6hiGLO-1mkL6jIR9xV6kizJR4UYGxFYNI-UC-Oto-8eFtnaFRQQ5mFb0lc48ghY8ZUxkuQLbhoKhx9id5zsadpikSszPOZKOQSnWYL8BoeAeAjpP3KBnfeIdQgII3BQlQXy7XzVJC9uQTGAbCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غیبت ملانیا ترامپ از ترس ایران ۲۵ روزه شد!       وبسایت Wonderwall:
🔹
ملانیا ترامپ پس از انتشار ویدئویی که سرویس مخفی آمریکا آن را تهدیدآمیز و مرتبط با ایران اعلام کرده بود، ۲۵ روز است در انظار عمومی دیده نشده است.
🔹
مشاور او می‌گوید ملانیا آرام و قاطع است…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/682935" target="_blank">📅 00:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایرانِ فردا را نسوزانیم!
🔹
بیشتر از یک ماه دیگر، زنگ آغاز سال تحصیلی به صدا درمی‌آید، اما حقیقت این است که سال‌های تحصیلی ما بعد از کرونا، دیگر هیچ‌وقت شبیه گذشته نشدند.
یک روز سرما، روزی آلودگی هوا، روزی تعطیلی و حالا جنگ...
🔹
هر بار بحرانی از راه رسید و چیزی را از مدرسه گرفت. گاهی یک روز، گاهی یک هفته، گاهی ماه‌ها از کیفیت و استمرار آموزش.
🔹
و هر بار، آموزش‌وپرورش آرام‌تر و بی‌صداتر، یک قدم دیگر به حاشیه رانده شد.
🔹
اما مگر می‌شود آینده یک کشور را به حاشیه برد؟
فناوری را می‌توان خرید. کارخانه را می‌توان ساخت. ماشین‌آلات را می‌توان وارد کرد. حتی عقب‌ماندگی‌های اقتصادی را می‌توان، با سال‌ها تلاش، جبران کرد اما انسان توسعه یافته را نمی‌توان وارد کرد.
انسان توسعه‌یافته، محصول سال‌ها تربیت است، محصول همان کلاس کوچک.
🔹
و کودکی که قرار است پشت نیمکت بنشیند، فردا پشت میز تصمیم‌گیری این کشور خواهد نشست.
آینده یک کشور، یک‌باره ساخته نمی‌شود،
🔹
آرام و بی‌صدا، هر روز در کلاس‌های درس ساخته می‌شود.
پس لطفاً آموزش‌وپرورش را فقط یک وزارتخانه، یک ردیف بودجه یا مجموعه‌ای از ساختمان‌ها و کلاس‌ها نبینیم.
آموزش‌وپرورش، کارخانه ساختن آینده ایران است.
🔹
آموزش‌وپرورش این چند سال با زخم‌ها و چالش‌های جدی روبه‌رو شده و هنوز به ثبات و قوامی که شایسته نسل آینده است، نرسیده است.
حالا یک سال تحصیلی تازه در راه است و این بار نباید اجازه بدهیم بحران‌های امروز، آینده کودکان را هم تعطیل کنند.
🔹
مسئولان، پیش از آنکه دوباره تقویم را ورق بزنند، سال تحصیلی جدید را جدی بگیرید.
برای مدرسه‌ها، برای معلم‌ها، برای دانش‌آموزان، برای تداوم آموزش، برای روزهایی که نباید از دست بروند، فکری کنید.
🔹
کودکان فقط آینده ایران نیستند، آنها ایرانِ فردا هستند.
و ایرانِ فردا، از همین امروز، در کلاس‌های درس آغاز می‌شود
.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/682934" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjw2-82zcPNqvbl8J51waMZcAo6I0k9Eu20JweO1bSFx9i6e5a82rJtfcg2au3h2XBoTC8NIRSEVob7MarlQAWcJoU491m9EY6JiqExpy0VxkBNbLTIhBVuoLvVfXPJ-wc9ytmQSZsipdv3-4CrT1Vp7HSJ9uA8UrJbSJOk21kuCDbNv00fJZxMJKckayMMbVuT7jfJa0t2LFI_zUsgEjoPeW7bN21XQzD0ia4-3HrbYYYg9kML1FLzw8z8Q_xtK8RHZ4SMw7JBsyqjYpOFcg1n0BfKj9bYeWjwVQa06vkhNiaMFEsybSNorfmtnmmCWpcjIcIc3UPn_NHugaCMXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/682933" target="_blank">📅 00:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
ادعای جنجالی اکسیوس درباره کریدور مرموز آمریکا در بخش جنوبی تنگه هرمز | آمادگی اسرائیل برای حمله پیشدستانه ایران
👇
khabarfoori.com/fa/tiny/news-3239064
🔹
سیل خودرو خارجی در راه ایران | سقوط قیمت خودرو در راه است؟
👇
khabarfoori.com/fa/tiny/news-3239150
🔹
یک پیش‌بینی تازه درباره زمان حمله احتمالی آمریکا به ایران
👇
khabarfoori.com/fa/tiny/news-3239076
🔹
«فروختن گذشته»؛ وقتی آینده از دسترس خارج می‌شود | چرا عکس مهمانی‌های خصوصی ایران مورد توجه قرار گرفت؟
👇
khabarfoori.com/fa/tiny/news-3238977
🔹
موج تازه تحریم‌ها علیه ایران | وزیر خزانه‌داری آمریکا: فشار اقتصادی جایگزین درگیری نظامی می‌شود
👇
khabarfoori.com/fa/tiny/news-3239179
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/682932" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
میانگین روزانه معاملات خورد بورس از ۳۷ همت عبور کرد
🔹
هفته پایانی مرداد برای بورس تهران با یک جهش قدرتمند به پایان رسید؛ شاخص کل ۳.۷۷ درصد و شاخص هم‌وزن ۵.۱۱ درصد رشد کردند و به‌ترتیب به ۵.۹۵۲ میلیون و ۱.۶۸۶ میلیون واحد رسیدند.
🔹
در این هفته میانگین روزانه معاملات خرد از ۳۷ همت عبور کرد؛ رقمی که با وجود کاهش نسبت به هفته قبل، همچنان بالاتر از میانگین ماهانه ۳۱ همت بود.
🔹
پول حقیقی هم در مجموع حدود ۴.۵ همت وارد بازار شد؛ دارویی‌ها و فلزات اساسی در صدر جذب نقدینگی قرار گرفتند، در حالی که فرآورده‌های نفتی و بانکی‌ها بیشترین خروج پول را تجربه کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/682931" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=J1LIMwia6Qkam481EJVJQK9q0rAvW_fG8ByAOyCviB8v53Jfw5Xrk4bNHN6uwLrS5e6ldfz_a9ok4bQs92NVXEXPxge9kqT1fdxIXHmgQkZxcHnG25Ozyr-RBSe9MQd3WTviNbf4QfR_VXwhxkPbQpD7Ct4-HhFQo0oFh2nAUsra8BrwjBS7CPFpvhuZkl9ofbancfWFFZ3p1gOOFzEhfJkPiusLevQEtTzAOmcHYX4DLS3JQ9CeCurfVPvU5-0P-Jh5GM9c_sgcxJi2tTPySJjOCN6dcIHiTIm_5oDHC8L2dW3g9Vc6IxcyDw5fYIOn0DOJMg8sL50m2YEoq-HsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=J1LIMwia6Qkam481EJVJQK9q0rAvW_fG8ByAOyCviB8v53Jfw5Xrk4bNHN6uwLrS5e6ldfz_a9ok4bQs92NVXEXPxge9kqT1fdxIXHmgQkZxcHnG25Ozyr-RBSe9MQd3WTviNbf4QfR_VXwhxkPbQpD7Ct4-HhFQo0oFh2nAUsra8BrwjBS7CPFpvhuZkl9ofbancfWFFZ3p1gOOFzEhfJkPiusLevQEtTzAOmcHYX4DLS3JQ9CeCurfVPvU5-0P-Jh5GM9c_sgcxJi2tTPySJjOCN6dcIHiTIm_5oDHC8L2dW3g9Vc6IxcyDw5fYIOn0DOJMg8sL50m2YEoq-HsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزه مقاومت: با توجه به فشار دشمن، احتمال سقوط بخشی از تأسیسات علی‌الطاهر لبنان در روزهای آینده بالاست/ همزمان دولت لبنان به‌جای تمرکز بر اشغال جنوب این کشور، فشار بر جمهوری اسلامی و نمایندگی ایران را افزایش داده است/ آمریکا، عربستان و رژیم صهیونیستی به‌دنبال حذف و تضعیف جمهوری اسلامی از معادلات لبنان هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/682930" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682928">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f158b8bc4.mp4?token=NUl8qCOGQU45ome9H-NJ8GV-KfwG32yi8B50W6sRsSt_a0scxO_Mypb1l7Cv3mmxjn-Ja7Xw7_QW8Mybr01m0skrJiazUt0SxvE287wQHa2-dxqATi8VAF9t1elWZWB9EjwwRae0MRTGGtWbJnnaoPKRtbYDr3mixB0bd14vp9LnjDU5qURGGVtwVt1NxyaI9CihpCIb3CX9tulD1IKZqJgh1ucLMTT4hI3uawT7KnDtYx3UJ04oKneEGa9vmc3h1SHPz3j01KieLKMHcwb5I5F4FXF-Fx3chBOvLq2dF0YpiI1Tp2Kcly49ON9SQL5GTV5ne_snf9GIjPFm0SgNDxxXLtflncxcQFNq6kVESpRCx-et9GO6rEGSB6IjjIHd1sWgNNZl-ar8it9zX-UZOWiWBnbBlFSuO8cF5lAZuFXu13xCx1ppUobxf_FVAgx_L6SNFhfv7QEhnwTcYbqd5c_f-XqrzZtDWRChfxiXYLkwjYt556UomghbBaDKdw0dtfwYe4x4uBsMahCEJfZ7c_sKlxO_lff1eL8jSNRaf7gner-sSqOF1O6PF5TComPMaiZ9qulfrozbZ6hcubsgK7IlP4w87fv9Eo6d5vaNDoh_DJYq6pL96sqUcnuluVKi57iXpbn5embIH_DjKlRiBlgwdT9wftOJuSRdmlYE8sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f158b8bc4.mp4?token=NUl8qCOGQU45ome9H-NJ8GV-KfwG32yi8B50W6sRsSt_a0scxO_Mypb1l7Cv3mmxjn-Ja7Xw7_QW8Mybr01m0skrJiazUt0SxvE287wQHa2-dxqATi8VAF9t1elWZWB9EjwwRae0MRTGGtWbJnnaoPKRtbYDr3mixB0bd14vp9LnjDU5qURGGVtwVt1NxyaI9CihpCIb3CX9tulD1IKZqJgh1ucLMTT4hI3uawT7KnDtYx3UJ04oKneEGa9vmc3h1SHPz3j01KieLKMHcwb5I5F4FXF-Fx3chBOvLq2dF0YpiI1Tp2Kcly49ON9SQL5GTV5ne_snf9GIjPFm0SgNDxxXLtflncxcQFNq6kVESpRCx-et9GO6rEGSB6IjjIHd1sWgNNZl-ar8it9zX-UZOWiWBnbBlFSuO8cF5lAZuFXu13xCx1ppUobxf_FVAgx_L6SNFhfv7QEhnwTcYbqd5c_f-XqrzZtDWRChfxiXYLkwjYt556UomghbBaDKdw0dtfwYe4x4uBsMahCEJfZ7c_sKlxO_lff1eL8jSNRaf7gner-sSqOF1O6PF5TComPMaiZ9qulfrozbZ6hcubsgK7IlP4w87fv9Eo6d5vaNDoh_DJYq6pL96sqUcnuluVKi57iXpbn5embIH_DjKlRiBlgwdT9wftOJuSRdmlYE8sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌جای آیات و روایات نگفته صدای معین و مهستی و داریوش حرام است!
/ تلویزیون اینترنتی مدار
موضع عجیب یک روحانی درباره خواننده‌ها
👇
https://www.aparat.com/v/mkfc6hp
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/682928" target="_blank">📅 23:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682927">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تولید خودرو نسبت به سال قبل ۴۰ درصد کاهش یافت
محمدرضا نجفی‌منش، رئیس انجمن قطعه‌سازان خودرو در
#گفتگو
با خبرفوری:
🔹
تولید خودرو نسبت به یک سال گذشته ۴۰ درصد افت پیدا کرده که جنگ، نرسیدن به‌موقع مواد اولیه و کمبود نقدینگی از مهم‌ترین دلایل آن بوده است.
🔹
این کاهش تولید باعث شده حتی قطعی برق در تابستان هم فشار خیلی محسوسی به بیشتر واحدها وارد نکند، چراکه اگر برق هم می‌بود شاید کاری برای انجام دادن وجود نداشت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/682927" target="_blank">📅 23:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682926">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d2f9f680.mp4?token=NYgOZity48dVpueft7ONkt2ZPXqtp6cGHytuaEl8DjJKGWQ-33lrL7WwdDH589T7ifvzYah8LOlH8PymB4CcyiyFf-9Qfg2lfrDzy4CAlGiSAiPWfBZ5WReab70l7Ll1hSm9ly7AxSbHgibQo1JgNASitJcbH8yG9qFmjh3pCkJ3QAIHyIzMEAVuZxKWHluSfyOQlkkjMgjJza3em1ShikPsqY3TmT7D7fBECklQY_eUJzcZVFhK2mcS3Rjjpm50niLIIN3nvpET1sB4FG6VG9vYoricUbwR_hcQHHa8aQq8dzGuIFKNqwCgoASnyVruO6YSO9cn6HVNe949QoqVbXdusokFBNZXcUycs-G2tjIhyIwhZLHEJdbigRk9XfPRsRHn5-ZE1tpOsNM-IJ-MxOC9VQVeCjUgSrarORiwsSJJ9sSmvFi7MgXSgHK6HdHAC0A_wsYCq8uy_oh8RFhw1tLgRZNegT7R-8j0Lz2nFnwury4nA7a6H0IIDFbTzXDWLLaxbxcXfQu8kdQPuKAUjISmWq80QEi5EE1rbvx32VSEHCNbKNIRrtgoT5O3ynq4tvadRGGC12hlFn-3md08Siy81Sqt0dnilym4N67wplWWIXB3IlWPiByq169ltgle8y1BNdSmacsaRs0yksK6af7ESdgADuKW-uFmz2E_euo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d2f9f680.mp4?token=NYgOZity48dVpueft7ONkt2ZPXqtp6cGHytuaEl8DjJKGWQ-33lrL7WwdDH589T7ifvzYah8LOlH8PymB4CcyiyFf-9Qfg2lfrDzy4CAlGiSAiPWfBZ5WReab70l7Ll1hSm9ly7AxSbHgibQo1JgNASitJcbH8yG9qFmjh3pCkJ3QAIHyIzMEAVuZxKWHluSfyOQlkkjMgjJza3em1ShikPsqY3TmT7D7fBECklQY_eUJzcZVFhK2mcS3Rjjpm50niLIIN3nvpET1sB4FG6VG9vYoricUbwR_hcQHHa8aQq8dzGuIFKNqwCgoASnyVruO6YSO9cn6HVNe949QoqVbXdusokFBNZXcUycs-G2tjIhyIwhZLHEJdbigRk9XfPRsRHn5-ZE1tpOsNM-IJ-MxOC9VQVeCjUgSrarORiwsSJJ9sSmvFi7MgXSgHK6HdHAC0A_wsYCq8uy_oh8RFhw1tLgRZNegT7R-8j0Lz2nFnwury4nA7a6H0IIDFbTzXDWLLaxbxcXfQu8kdQPuKAUjISmWq80QEi5EE1rbvx32VSEHCNbKNIRrtgoT5O3ynq4tvadRGGC12hlFn-3md08Siy81Sqt0dnilym4N67wplWWIXB3IlWPiByq169ltgle8y1BNdSmacsaRs0yksK6af7ESdgADuKW-uFmz2E_euo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدری که چشم انتظار فرزند کنکوری خودش بود، قبول بشود یا نشود زندگی ادامه دارد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/682926" target="_blank">📅 23:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682924">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ce052442.mp4?token=Gc8-siZ2AYUgAQgBVERdxTQ1o4oMr9xJRbzq6gN-pvoKbhfcqGGFbVn8IQFbWSK5kb--6N38qbJUkzJ-3YjYT0wcLuJN1-Ri610V6iU3zAbAC-VfXeKnQGq2COSDUNdeaNC-m_ZPpLhEIvlr8W4EcwoEI2Thbo18G9_rLpO4qc6lHjaauJ8O1T9T7LHAWOIsKo-m4u4Ou-hlBWxeylkMbV__qXylLJjDFYRKOwrzKsbyhqBuVq1DXTw4-6bzdofh84K3oe5ZjYDFD7uNMvR75ViRCaJ8lwV-HOmF5KTyRtt3n6sd_HfAFIp30sCoSTgTFrBNkbYEYEJ8YEJA5uo6nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ce052442.mp4?token=Gc8-siZ2AYUgAQgBVERdxTQ1o4oMr9xJRbzq6gN-pvoKbhfcqGGFbVn8IQFbWSK5kb--6N38qbJUkzJ-3YjYT0wcLuJN1-Ri610V6iU3zAbAC-VfXeKnQGq2COSDUNdeaNC-m_ZPpLhEIvlr8W4EcwoEI2Thbo18G9_rLpO4qc6lHjaauJ8O1T9T7LHAWOIsKo-m4u4Ou-hlBWxeylkMbV__qXylLJjDFYRKOwrzKsbyhqBuVq1DXTw4-6bzdofh84K3oe5ZjYDFD7uNMvR75ViRCaJ8lwV-HOmF5KTyRtt3n6sd_HfAFIp30sCoSTgTFrBNkbYEYEJ8YEJA5uo6nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صنایع دفاعی؛ نمونه‌ای از اقتصاد مقاومتی
امین طباطبایی، استاد دانشگاه و اقتصاددان:
🔹
ما در تولید صنایع دفاعی کاملاً تابع اقتصاد مقاومتی هستیم؛ این موضوع تا حد زیادی به چرخه تولید داخلی و ایجاد اشتغال نیز کمک کرده است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/682924" target="_blank">📅 23:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682923">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تاراج ۲۵۰۰ مگاوات برق کشور توسط ماینرهای غیرمجاز
مصطفی رجبی مشهدی، معاون برق و انرژی وزارت نیرو در
#گفتگو
با خبرفوری:
🔹
عده‌ای با استخراج غیرمجاز رمزارز و مصرف ۲۵۰۰ مگاوات برق، فشار مضاعفی بر شبکه وارد کرده‌اند.
🔹
در حالی که کشورهای پیشر‌و مانند روسیه برای تامین امنیت انرژی خود و جلوگیری از اتلاف منابع، استخراج رمزارز را تا سال ۲۰۳۰ ممنوع و جرم‌انگاری کرده‌اند، ما همچنان در حال مقابله با سودجویانی هستیم که برق مردم را می‌بلعند.
🔹
این ۲۵۰۰ مگاوات، معادل ظرفیت تولید چندین نیروگاه بزرگ است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/682923" target="_blank">📅 23:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682922">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxy0ATacKUgrRcows8N2cRjIC2mTdfMpiQqnJkQxHYhQ9dLKuxVeOQ5GwqN8ArPAA5waJ2aQVq5KzdLt4gdalINh3kbUiUX7EQIPqGs1S65NGpDr891aShpD_n7Mt8wCh3eEQaHPjt3ZuPLf-NaDGwC1wii8ngjmokmykrZO5A9JGsXa235kUu9RQWynEJhRt82CbPDKAAfy5E_RmDb_w9rmkxHE94K2PMkxMukALi1mibLtmd4agK0QfbVr61BFt2UnFOOGoyR-ek2bApxjod2srZ0QgaV7mgp43dy0-3IWZyWntG_6hXP6AeJ-tjWkfZYj2e5b8FOW-4kn3zPM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای پولیتیکو: جنگ ایران زمینه بازگشت دزدان دریایی را فراهم کرد
پولیتیکو:
🔹
جنگ ایران زمینه بازگشت دزدان دریایی سومالی را فراهم می‌کند و تهدید پرهزینه دیگری را برای مسیرهای کشتیرانی جهانیِ پرتنش اضافه می‌کند.
🔹
جنگ ایران به دزدان دریایی سومالی که کشتی‌های تجاری پر از سوخت و کالا را شکار می‌کنند، جان تازه‌ای بخشیده است، تهدیدی که سال‌ها خاموش بود.
🔹
به گفته ویندوارد، یک شرکت اطلاعات دریایی جهانی، اوایل این هفته، گروهی از دزدان دریایی یک کشتی باری را در سواحل سومالی تصرف کردند. این پنجمین حمله از این دست از ماه آوریل بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/682922" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682921">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3f784dbc.mp4?token=H4LEBTocwx-PeaaNTH3IHKFgMtJkD_D_r_Emcmp9jDUinrx0dEyYtTfNsGnHufi99biwIW13b8XEj-aI_sXiIpA9wpPW5Lm1unQNGK5xUhM-eAdo_SdJW6FNvVymfOSD3ucGHVB16zbYFXZXibTayjdHX2CQv3_72FJ4m5lPP1USZkeoE7Q-8GJ62q8ihqrA5AY6yUZV4svPP67YPHqqj6IMzs0uqztdJavxie-fxzFN9rvOlHjsyLzMShrYa0FXzxOUsGSzNbDZi17adBQOxHg_5_ubY-8NpfOyypoSghyVzmUeRKjxoxgkfHxIQsaLYGBWrJQ1czVtGleMcU2BQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3f784dbc.mp4?token=H4LEBTocwx-PeaaNTH3IHKFgMtJkD_D_r_Emcmp9jDUinrx0dEyYtTfNsGnHufi99biwIW13b8XEj-aI_sXiIpA9wpPW5Lm1unQNGK5xUhM-eAdo_SdJW6FNvVymfOSD3ucGHVB16zbYFXZXibTayjdHX2CQv3_72FJ4m5lPP1USZkeoE7Q-8GJ62q8ihqrA5AY6yUZV4svPP67YPHqqj6IMzs0uqztdJavxie-fxzFN9rvOlHjsyLzMShrYa0FXzxOUsGSzNbDZi17adBQOxHg_5_ubY-8NpfOyypoSghyVzmUeRKjxoxgkfHxIQsaLYGBWrJQ1czVtGleMcU2BQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند کاربردی پاک کردن چربی از روی هود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/682921" target="_blank">📅 23:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b616f7192.mp4?token=L8QKf69H_QKNr-z2meWtMQVdJaudqoy1vdaL2LVr5Philwb2CldhHCeHUEpVZ6Yw4ie2j9PzTxyc_WmzY8hzU4pD1pxCIlvPuVfFRUi-fJzrnbwXpuqonV5TATr-3WhtWn8KcKYeMKPF_08hI5xNF4P5pnNvMvOWczS0E4kKOtq8eyKB-AE79vCiD2CDU5HXxDIbmT23_wGrkaWnhYpmOBSkx2UhpNny8lFYkY30gFzcZI0M0mRnT4l3oVwVDkf5BrXLBYBQT2NtGxC5hsdndVC84Um6mk3bB8-cUgCmoy3XZO6MPJ20-UcUsonAH_dc5sAAJcx30A28u9cxigud6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b616f7192.mp4?token=L8QKf69H_QKNr-z2meWtMQVdJaudqoy1vdaL2LVr5Philwb2CldhHCeHUEpVZ6Yw4ie2j9PzTxyc_WmzY8hzU4pD1pxCIlvPuVfFRUi-fJzrnbwXpuqonV5TATr-3WhtWn8KcKYeMKPF_08hI5xNF4P5pnNvMvOWczS0E4kKOtq8eyKB-AE79vCiD2CDU5HXxDIbmT23_wGrkaWnhYpmOBSkx2UhpNny8lFYkY30gFzcZI0M0mRnT4l3oVwVDkf5BrXLBYBQT2NtGxC5hsdndVC84Um6mk3bB8-cUgCmoy3XZO6MPJ20-UcUsonAH_dc5sAAJcx30A28u9cxigud6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
ونس متوهم: باید مطمئن شویم ایران دیگر به‌دنبال بازسازی برنامه هسته‌ای نیست
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/682920" target="_blank">📅 23:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682919">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c72520a86.mp4?token=Rm0TxykH_z8zcG6u8vaAZk9UgJl2A1uKU8bUiOk1Vp6CFwbe-BXIKGvtvxj7pdEeE751fi_64_kvHNnEQ7P9AWdsw19aKrwaqrOrIe93fMUKPVrs_AHhTnXrPH3i2rw9ywdKIIvj-xXsdMI1DaWc7GsKVro9-n0LFpAZKvJOIkS6u3fAMZoudcvUY8rXY6Aw5PQbjfe1mgXR8YzqyeHhI6-jBEeapYAtEveKSUXPi-LwnlnvEDYpNH_TL_TpXoc39EnwQ4EpLIczjLtDdKNbGHdivHvI6kl8uhDG-J7_3HKVJqwejJzMpOEfVPMe462W2pY3tdYVOOvRLSJ3sOhuEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c72520a86.mp4?token=Rm0TxykH_z8zcG6u8vaAZk9UgJl2A1uKU8bUiOk1Vp6CFwbe-BXIKGvtvxj7pdEeE751fi_64_kvHNnEQ7P9AWdsw19aKrwaqrOrIe93fMUKPVrs_AHhTnXrPH3i2rw9ywdKIIvj-xXsdMI1DaWc7GsKVro9-n0LFpAZKvJOIkS6u3fAMZoudcvUY8rXY6Aw5PQbjfe1mgXR8YzqyeHhI6-jBEeapYAtEveKSUXPi-LwnlnvEDYpNH_TL_TpXoc39EnwQ4EpLIczjLtDdKNbGHdivHvI6kl8uhDG-J7_3HKVJqwejJzMpOEfVPMe462W2pY3tdYVOOvRLSJ3sOhuEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر طراح سوال الان جلوت بود بهش چی میگفتی؟/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/682919" target="_blank">📅 23:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: عرضه آزاد بنزین بعد از اجرای طرح باید سقف قیمتی داشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/682917" target="_blank">📅 23:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای ونس: ما به فشار اقتصادی بر ایران ادامه خواهیم داد و در نهایت به هدف خود خواهیم رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/682916" target="_blank">📅 23:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682914">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b70v5t5qpl7qvfQr15InG57D0RX_2WauNXnHtSLSeeQUWjjdUNQddma2lWFDIhoi4VBgb3MbEGaR2EIzteOihI9LJoQPIlgfkjMM6l-Z7fsjEGxbJFstwjijWFpOwvwOhrgmkqb01LjJMsNG5LnbSI45VvYjqeEWJmq6SiwLtWmU7ZyXrqySDvxriR0affIj6j9XJ6XVe1mPB4Tp1IrPvl9jMuBLdYKFc7hg9Y_TuEdzPBLtJJQo2buqXHKTdz30xrZ3j1GcmqyvxMLm5K1QM6D3BtSqxo3zlklaAx8SdKOoq1EGI4qT6DCsqFazv84-QYz9sF0_ED__sFbcC6OCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین اقدام ناتو در بلغارستان از ترس حمله احتمالی ایران
خبرگزاری bta بلغارستان:
🔹
شورای وزیران بلغارستان در یک بیانیه مطبوعاتی اعلام کرد که رومن رادف، نخست وزیر با مارک روته، دبیرکل ناتو، گفتگوی تلفنی داشت.
🔹
طبق گزارش‌های رسانه‌های خارجی، این دو در مورد فضای امنیتی اروپا با تمرکز بر خطر احتمالی اقدامات تهاجمی ایران گفتگو کردند.
🔹
روته شخصاً حمایت کامل ناتو را تأیید کرد و از آمادگی نیروهای دفاعی اتحاد برای پاسخ به حمله احتمالی خبر داد. در بیانیه مطبوعاتی آمده است که هرگونه حمله به یک کشور عضو ناتو به طور قطعی به عنوان حمله‌ای علیه اتحاد تلقی خواهد شد و تمام اقدامات ناشی از پیمان آتلانتیک شمالی متعاقباً انجام خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/682914" target="_blank">📅 23:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682913">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ظهوریان، نائب رئیس‌کمیسیون اقتصادی مجلس: در صورت افزایش قیمت بنزین ۶ تا ۸ میلیون تومان هزینه به دهک‌های فقیر اضافه می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/682913" target="_blank">📅 22:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105f0ad8e0.mp4?token=kUZN0G2g4PDKyAmpShM2aTzZ4L7JEjJGFKpCWBi0dnWq9jE-pqLZzesHaLxawrz5THpbtUuyxojw7mudiIFlnw8HRvR6uT1Ua0146Io6z8akQkCOAx8s1Fiu1FgTCYmT2lnHH6t4BZenmKpGARtXArWloB7SEfpv62zljNG0iQcS5znMayFkKSak0M8lXzsumMn-4n1s5BUWqpI5mzcElQjtyanUw4KU7Vqaedc2y_Z1dwndTfZAd7xHh3wbJ0kXXhL0prjJbyWv5dAgjMaQDecPkQlo1O9KTyifqjP9geijqh2_p8OWwu9xhAMT60xMTSQrYx_heX_wpMyoN9kyMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105f0ad8e0.mp4?token=kUZN0G2g4PDKyAmpShM2aTzZ4L7JEjJGFKpCWBi0dnWq9jE-pqLZzesHaLxawrz5THpbtUuyxojw7mudiIFlnw8HRvR6uT1Ua0146Io6z8akQkCOAx8s1Fiu1FgTCYmT2lnHH6t4BZenmKpGARtXArWloB7SEfpv62zljNG0iQcS5znMayFkKSak0M8lXzsumMn-4n1s5BUWqpI5mzcElQjtyanUw4KU7Vqaedc2y_Z1dwndTfZAd7xHh3wbJ0kXXhL0prjJbyWv5dAgjMaQDecPkQlo1O9KTyifqjP9geijqh2_p8OWwu9xhAMT60xMTSQrYx_heX_wpMyoN9kyMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: طبق آمار رسمی روزانه ۲۰ میلیون لیتر سوخت قاچاق می‌شود که ۸۰ درصد آن گازوئیل است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/682911" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ظهوریان، نائب رئیس‌کمیسیون اقتصادی مجلس: افزایش قیمت بنزین مثل چیپس و پفک نیست که راحت بتوان قیمت آن را تغییر داد
🔹
هیچ‌کدام از ۳ طرح مطرح شده، برای بنزین مناسب نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/682910" target="_blank">📅 22:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682908">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93342efec.mp4?token=h4ng3ZUo-dwyPb93BcBdZaZj1kLJtJhvbXrBf0iq8kvON3a26BHA5VJmrSRBpnTppEJgseoSNwZNatwVUONsOGmo5gq2dH5RpaPiJSsZbX4iw0lqU1MLJR7k5tTZ24t2zZZF2PYPMknxYuqj2Kmoyoy1yPbv17VhRdloGx2Q1cGkF9K4LY3ceglTC7DQbtslLxPA84s0UQRiv_SLnnK2UzJ0ihqHUyQd3dUR7bLwin4pnsirKG_vFzmE8T3nzBR8RwyPvZc7l-g5y24wz6JWs4Kar_EMq2FuEHqlXu-WJjDkEofcfBAAQ-7rqMRHfvAp-9udbY4WDIIkzfBq8mP13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93342efec.mp4?token=h4ng3ZUo-dwyPb93BcBdZaZj1kLJtJhvbXrBf0iq8kvON3a26BHA5VJmrSRBpnTppEJgseoSNwZNatwVUONsOGmo5gq2dH5RpaPiJSsZbX4iw0lqU1MLJR7k5tTZ24t2zZZF2PYPMknxYuqj2Kmoyoy1yPbv17VhRdloGx2Q1cGkF9K4LY3ceglTC7DQbtslLxPA84s0UQRiv_SLnnK2UzJ0ihqHUyQd3dUR7bLwin4pnsirKG_vFzmE8T3nzBR8RwyPvZc7l-g5y24wz6JWs4Kar_EMq2FuEHqlXu-WJjDkEofcfBAAQ-7rqMRHfvAp-9udbY4WDIIkzfBq8mP13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: تخصیص سهمیه نباید به تعداد خودرو باشد و باید به خانوار تعلق بگیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/682908" target="_blank">📅 22:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682907">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنهاد کتابخانه‌های عمومی کشور</strong></div>
<div class="tg-text">📚
🍯
کتاب شیرین؛ مسابقه‌ای برای بچه‌های کتاب‌خوان
نهاد کتابخانه‌های عمومی کشور با همکاری شبکه نهال برگزار می‌کند:
🎙️
مسابقه تلفنی «کتاب شیرین»
👧🏻
👦🏻
ویژه کودکان و نوجوانان
📚
کتاب‌های مسابقه در شهریورماه:
۱. «سی قصه با پیامبر(ص)» | حسین فتاحی
۲. «روزی روزگاری ایران؛ هنوز یک نفر باقی مانده» | مهدی میرکیایی
۳. «روزی روزگاری ایران؛ با نام دیگری صدایم بزن» | مهدی میرکیایی
🗓️
شنبه تا چهارشنبه
🕕
ساعت ۱۸
📺
شبکه کودک | کانال نهال
لینک خبر
📌
@iranlibraries</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/682907" target="_blank">📅 22:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682906">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b118b3002.mp4?token=rFyHdA8e5ikZw9TtkW8_xmDJlyfUUuJc8NeHqsEB-BQ7ZV77RIrgzZFIhIJWaSB5scI8wJn3VTSrtOTqFaN8F5lJaATJxy4rUKP3cSMXc5qhslq5rwyuaRAf5CSBjbAMv7QInzfczggb-YzAqCEcXm4WS3rFPxq0S1CqJAzLpjQQy3MZnR6dFDMsfJlqkamMopsTxXDJZM-P1L3zKqVWLKQXfJ8ymH59Qflqm8WWHrVHzodJ4baY6tROJ5O1jwVCdi3ROiMMtxYGGL1qWoLzxJuo1OmZ9KfmGTQowkKEr1g76BgMv5fdq6V7g0xF0SvOLAEbdvdtYcRhsTvPeGXHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b118b3002.mp4?token=rFyHdA8e5ikZw9TtkW8_xmDJlyfUUuJc8NeHqsEB-BQ7ZV77RIrgzZFIhIJWaSB5scI8wJn3VTSrtOTqFaN8F5lJaATJxy4rUKP3cSMXc5qhslq5rwyuaRAf5CSBjbAMv7QInzfczggb-YzAqCEcXm4WS3rFPxq0S1CqJAzLpjQQy3MZnR6dFDMsfJlqkamMopsTxXDJZM-P1L3zKqVWLKQXfJ8ymH59Qflqm8WWHrVHzodJ4baY6tROJ5O1jwVCdi3ROiMMtxYGGL1qWoLzxJuo1OmZ9KfmGTQowkKEr1g76BgMv5fdq6V7g0xF0SvOLAEbdvdtYcRhsTvPeGXHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش‌های بهبود رتبه اعتباری برای وام
@Tv_Fori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/682906" target="_blank">📅 22:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682905">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4WgJtfHQXPD4fM6QeizzgsAAsunXDI71rVp4LUa3JDyMYtA85bixw_e7hmO3QzKLGNSnIQU_KdKVvMumyzLt1wnEJJ0fyY5mbSolqItxlag4_g0Guxj0oduBxO6mSNm2gFcuObG9jsVQPhFMFPyX23P0fIGWsFMjgCvuLWKG7hICSgNcKg6E5XizlDx27t7ONLOc2B2uNiJ5hD_WrTFKJL2bK8ZkrmSsBOS5a2d3khH0nr1RPOuz5nvyiN9U7-ndxUYECyTOwf1jE9eyW7lq1XrBg0IGZWYtE5sivXVf7i0vB6teokaimHWUfGRHi4G-QwvtX5kjUnPHyuioi5SFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار ویدئویی از ترامپ ۸۰ ساله با پوشک بزرگسال!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/682905" target="_blank">📅 22:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682904">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a47126c77.mp4?token=FvDmT_YkEdu6MOxDdkLfSOu1qiTjclhZv9PkhqbYR89GWVQONNEJaha-y9BYaeK8p1GXNOsiz7BdNRHcs3R-Wpm2Xnt655Bx5iNu2Okgo1Wj469wlbxoSgh3UqFTQY5vmUCdztL2Sbv6vhqyt1MS5AEbYMuIUzfGaI9yT2Na0BZJdMQFZ_WphspPg7WFSXwSlwxfMfnQqSm2uZiy7IG24ogCQuJ-u_1AjcTv1m3_pw62sxmbQ-ma_ZX3DxcgREUNcbSxIdZOPJaFxPp1_b9dKJEZ39hdEDVtyFqMSJkwuEo93RUpw-m7mgNq9msrv-IYXwypzWF-VQOwgnp6OJUfDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a47126c77.mp4?token=FvDmT_YkEdu6MOxDdkLfSOu1qiTjclhZv9PkhqbYR89GWVQONNEJaha-y9BYaeK8p1GXNOsiz7BdNRHcs3R-Wpm2Xnt655Bx5iNu2Okgo1Wj469wlbxoSgh3UqFTQY5vmUCdztL2Sbv6vhqyt1MS5AEbYMuIUzfGaI9yT2Na0BZJdMQFZ_WphspPg7WFSXwSlwxfMfnQqSm2uZiy7IG24ogCQuJ-u_1AjcTv1m3_pw62sxmbQ-ma_ZX3DxcgREUNcbSxIdZOPJaFxPp1_b9dKJEZ39hdEDVtyFqMSJkwuEo93RUpw-m7mgNq9msrv-IYXwypzWF-VQOwgnp6OJUfDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: در حال حاضر تخصیص بنزین به خودرو است نه خانوار؛ ۴۷ درصد خانواده ها حتی یک خودرو هم ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/682904" target="_blank">📅 22:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682903">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
بنگاه‌های متوسط، آب رفتند
🔹
داده‌های اتاق بازرگانی ایران از یک تغییر نگران‌کننده در بازار کار خبر می‌دهد. در فاصله اسفند ۱۴۰۳ تا مرداد ۱۴۰۴، کارگاه‌های ۶ تا ۱۰ نفره ۲۲.۳ درصد و کارگاه‌های ۱۱ تا ۵۰ نفره ۱۴.۲ درصد کاهش یافته‌اند.
🔹
در مقابل، تعداد کارگاه‌های یک‌نفره ۱۲ درصد رشد کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/682903" target="_blank">📅 22:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682902">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/410779a898.mp4?token=PRt7ss0C_q_bMhrf2FHGaZtpsELXO5CVDWH0Di2rny7Dj5O2fxYTFBrw0n3TrOEvn09_k5vC7-k3j1DxPLItRAP4R0gMORI1COOV5Ql30v0r62fw9cS4AxqcKzWSUfQ3AOZ-vAEyl1Mr-TtXYmt7btKlULwVaatAhTiF_tLg2inG3L5lrdz2ocrBgO0s-XIHqcoekL6W4NfG3NzU1mQoZteHLFFFECkCVSTFj7z3YYNlEpd8D8j2aCaqEFggjkhwjo546rB0I--VVNcNTFZqS2H3HgrJ-sQ96UiQ2-t4PDdnba8CMRSB-ZiyJvvfyukmJFYwyzunvxjGC05DiuINeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/410779a898.mp4?token=PRt7ss0C_q_bMhrf2FHGaZtpsELXO5CVDWH0Di2rny7Dj5O2fxYTFBrw0n3TrOEvn09_k5vC7-k3j1DxPLItRAP4R0gMORI1COOV5Ql30v0r62fw9cS4AxqcKzWSUfQ3AOZ-vAEyl1Mr-TtXYmt7btKlULwVaatAhTiF_tLg2inG3L5lrdz2ocrBgO0s-XIHqcoekL6W4NfG3NzU1mQoZteHLFFFECkCVSTFj7z3YYNlEpd8D8j2aCaqEFggjkhwjo546rB0I--VVNcNTFZqS2H3HgrJ-sQ96UiQ2-t4PDdnba8CMRSB-ZiyJvvfyukmJFYwyzunvxjGC05DiuINeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مالک شریعتی، عضو کمیسیون انرژی: در حال حاضر تخصیص بنزین به خودرو است نه خانوار؛ ۴۷ درصد خانواده ها حتی یک خودرو هم ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/682902" target="_blank">📅 22:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682893">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVHyObqFpxOSrEwq2NDxSo720JvRwX3JW049IWzUvDwK46uHERvWmG2ZbQGd9RktNrlGwGO1Q_9F5BgSYpB_CpIGa4JOf65xn4avANqjoB-QIMXVQGxtIm-mSvAO2z6k-djzdfCNsWWExR8augw000CQji01GIqclWPAn-Na8SDuGKTMAofokqFauzlWrxi5utizlEtLplbjw1N5y7dm_9j2aqq6uSvalyQgO7tNZ6kh_x7BeQVtrQYpShM_XI1FR_aQ3ayM2kF28bTn_vl4FpfYCvfZvgHq5dkU6P_WRzSG9wwoR1yGv83XcMwT2cHFxJ8mM5EAga4D8pjRhJa_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhlnAGZ1C8yntRiU_GCnt-lfBen88zkfmDkhC2Y9ORRiHWHOqMCXuOxpYh6rKD83DoZkwBU7jNTVTzrr2m--brdMv6NmaM5E0eEpZXzdoQmSiO5L4BmUbYC31tVdBLVc_tDtwnog7yb8kO1M5IWW3Y9bAHyjBVtmFbabsqcclH2mVs2QoK8WZWXa4qL_ZU9PVP3bCPXg0u3hx9Et3-cR_ep4mQtnzy0XSIhLg1EFKIM1bmzTgP3yMN6lhVTrHHMPEA36dRqrvTytKrxtqHRIQtVvMon2qBGmCaZpoaJhoiV0g5ji6z0KZn0e0xEF7l0iiIHVN_PWNj7CCzfvHHIkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhcDsg4L_T-iO8-dTDgP1J7eoIHzaENzLPbUGckEFMG8SlbehI9kuc_y2TPHvV8Rc_9mAr8maKHF6Su2hkkmbRQXM2NH2mGiG6FzdMCKHvSmU1P1lbGnXfPCu5iTtJ-soCmHmdyI8lz6uBEZd4TgZQ0y7kJeR89YxFvdPywIO5PenUJWPROX-Tm9CcqR2BGrOzOUxj5AIPvkth3zcB3eskQiKgEn37grnq2uxLkRNTKU_3h1omz6ZxkUjCbJdH12WFhklcg5elnpxVyqp54xKYLncG8iK4OoaTup4AYxlDEXYQSP3Uz8vbhOgjgHFQ1yGZUH7Qa3EVAxaeaEQawh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDB1YFH0I44EhrlGABgM4tZysLCLRRRu9jVObOgTdagN1mTjiqOccJK5pCnDMEz3Pef7FvhfgoE9kRSZhVcIZ6BMFruPgWfosjEGt3fW0oSI-zB9TmztF5v5STIqyol-jZI9aBP-_VQrVlxuaz5YAKKlvQI8mbm6FaJhbsQr07L5Je1JxMPMYBHQUAEzFN3QlLdc8aY_mFkPHa9v85gHXaLUM-9OJm23hUGf14yLzvljf-urc5F35OWbrocoikMGByShZExZVVEs6ohWY90vMGWiR25-JkkBvatTwbsbNN1t6yYLSxNYUrLbowPpFujjQC59CfZrqIxRAOwpDqY_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_vZFN1MNuibkFtUx8CQa3ifMRRJKSkTsuKkFXDtmNBwUbCsGs40cjzeYbkARyJRNNC-nd3qlL98q0lG-m9YGXzJj3pqgu_q2o2CTVwQ9peHbWs-7VtJCD-ZqwdixOn8OYOE2CDzfsN69pAYJvEEiZAxBLDx94fJSeOb3QaVc1ERR3nSiUEdwUziVcCbwXkH7Iif-VqLyQV6fPDk92OHieuaGgtKZI0p9d14KEHBDJomjR4z21uxmJkeWpBM7PFbBruOBBgQlI78jJBm-iM-pPVsz_tLxbzP2MPYwq1VqXL6eS7ptTFFbr8kLAKmKaPmU8AwQXkg3GhPKdMVy2OPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0rlIaxoiocDi42IYbu5iVHpCu28QHxjT_3PP3GYZrxtXgXCl8HNLo2BPMmJmcAprShE94S6Bjrmd3E1thwTKOVnUZcNBQIZ3StAGeT2ASz8GXeodPA-jnceMiMS_UwNtKbabhG-Yg9s0TWWfnq51x9FWLFT6egdBAfyfZxKoQo4kVcNlwuuRL4SA6WVMEiDABdvQphpJumhlaCNFsJxYmJW9ejz24ZuxASol1e-LPWNIkr2o3X0AJQtptNf7l69PlgRlsgbndepDSWac3wSILPth0mJxBqF2BaxB6HZ5kj6kuYE-K0bERzfKZ1UGxKIh40DSD2oTSSyXK9T44_xYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzvhH9zMzV3pZ6J4ssfkMN6LQ3sEyZ04eZP_NkJjMwoDcOvUPJZRlie4CgSWF8nqaR9AbhsqoHZCZDuFSyU3CQ-9Bf3YVD9fYGTSsUGuQ4mYTSq2gIKLJDPbtaunUUP846xIOq_xc4oPF9gOxkMROX0gQzsSpxY8x8_TYR2sOd4O-eWU7R2e5z9EMWRkkYVslEwLuPBeAuq-Y6AF3Wn6-3JnjoFDzeGBULrcZTiPhmF9SJtX7PP6v0fa3Bmrxloir6Ykepws-LQvsJlLegpwDtNV7_lb4wv8zNbS_laVzkOPYskZMEX-XEaJoHmZ915YYNNUQHlSAPvVyQGecd6D-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPxQjJEGqiE8EbvQrltFimEGWeQ_MzVlMrjcPwnxqJuzvqEK35qhUv38jL_uYTE5Ur-B3fUwymQrif9q2xK58eIi1XqK3GHUuNbeVHsELo42RHI4us8wtYCBpK3AkBmIYPZr-j3voZ_r21yINCpMIQut6vnWxPPCeU4Gapjs9MvdlAVU8yWv821SAYNilZ-9qbMcmH-BEOSwH44S0Ar4gyUdRKRLN6lKT81GnHuMUuqpBtyI2EYOOxD3UyhW5swBdHzLFOCm4n6RxcU38PRF3oYLHSWVAQwuJ4UxLHP8Oe3-I5a3AbWkpQBG0pWILr_6gRJy_SOVAw-Fr-ZBfPUX5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🥀
ای سامرا ! مهمان مظلومت کجا رفت
ابن الرضای سومین ، پیش رضا رفت
آه از نهاد مهدی ِ او تا خدا رفت
دور از وطن چون کشته‌ی کرببلا رفت
#پروفایل
#بگراند
شهادت
#امام_حسن_عسکری
(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/682893" target="_blank">📅 22:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682892">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj8biQJdiwWzI-V3QZEPZX9lu4Jc3RXDcU5sz4O9lG6-eC58OS-Xwzv9ccrdzJYT8Ili5RlQlcjQP77BJCMWi8bZrKeelYlB8Igt6-jAONgMVrz6quqJFYWOg1n9_C8p2ieVx9kbt5ZbwcqDqVcD4p1WeztFQDDiar_OYfgqB7ct2btgWluMAb3fOg9kg3B6SoKXFszl59peMyubqSRN1v_6lWfSA2QE4p-1kQKt7dEi-EMNL0o0MsZ8sFHR3MK8FhKoxkjUkSE3UDc_bGTbH7hVQZIufOybnoYvB3V2KzuBtTXWIUvK3SSz6FeOvm0-xil-cNtNA8tCdmx3vWNrSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قالیباف به اقدام مشکوک حلبوسی، همتای عراقی خود: درباره ما خواهند نوشت که ما دو ملتی بودیم که نپذیرفتیم پاورقی روایت‌های دیگران شویم
🔹
رئیس‌مجلس عراق در یک عمل متوهمانه اقدام به استفاده از واژه جعلی خلیج عربی کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/682892" target="_blank">📅 22:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682891">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRWs8NqFzglA25Gd6lcWoJc8C5dpM9KhgAom-cf_gsXTaGR05VLRtMdwQuFd7-2-3B1r7K-BE5af_n2o0c36QlNnZNnQNSMSLp9A0gvJF7DSLu1i5IHfEgRcqDzFbUD2fCcnjIEvwvBgtBTkpO_9d6qa5vV3EOJMKfMViFMmnIamR6Aa0Yv-36jFsYvLQX12Kx5pvG8esh24I67VDdJDXOdUOpuEkH253tq0j2mdaZdU_i90AL9CC4ErC4moTDFMo_-DHwMeRfGCwbcgvvpPUQvde4GAuozI-RcaOucVQJtgj9lVAPA0uETBEAJ1uyLJ17vV8CLZY2sOL7HuAXQeEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روستای زیبای آغویه در کلیبر تبریز
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/682891" target="_blank">📅 22:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682890">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">ششم ربیع الاول، سالروز ارتحال کوه عظیم‌توحید، استاد العرفاء مرحوم آیت الله العظمی حاج سید علی آقا قاضی طباطبایی تبریزی (قدس سره)
ان شاءالله عنایاتی از روح‌بلند این ولی الهی بهمون‌نائل بشه حمد و سوره ای برایشان‌قرائت کنیم</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/682890" target="_blank">📅 22:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682889">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdNc_TUmq91GdAvWos8NAsRnMDk4T3jogyin0yK81i9EaFKcbvEHWHKsiCSZBrVpx_ii8p1v8NLFISyR3sUq2rCDVwu6yJce6s0fiS2Ypn9zAaxwVj8RYFOHV1nwxny9jE57d06yPaWcui8qwU5dF2yoUgsxW2gZSdcUQh0j5Em2ngqykxZwBuvU4ARxmPpA3exFT8oMKoQaH5JxzvHybWbn3eQYfUvK0xUv0s-jA-g2uPpkWnaYTcsPcshbqwRv-4CV_Nn4CO9SQQfjhA-tFKcZVEPlCMTCf2hY74PQIZYFeEkLBNEz5GM0nY0sxH30CH6RqX4RsjHiVAonFb0EYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیدا کردن دوست سخت است؛ اما نگه داشتنش، گاهی سخت‌تر
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند ناتوان‌ترین آدم کسی است که نتواند برای خود دوست پیدا کند، و ناتوان‌تر از او کسی است که دوستانش را از دست بدهد. دوستی واقعی سرمایه‌ای ارزشمند است؛ ساختنش زمان…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/682889" target="_blank">📅 22:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682888">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f21d2d79.mp4?token=WAYPxMPc_FiHI46BsmzqumLK9ZsFVv54W7zQr9sMNwDLTNPXz2erKuBIDGgAI_N3tFZJ-i3P8jJ4yObvlnTFaWOy83jR8Jqx4NKsTm01Lg7mCdydxKo4JeyF59RLK0eaHlS_fiuET5Zvmp8XELcypyxdM_0kD6ijrY54WopQdgoGSS2pWUzf7dEmIShjylUucM0KRr899g4WQ3F7qp4mSYTdjJD3nt46pCK6t3bNC1g4mH_PvnSnwgY5wHSIFUko3o9OTlaUO7tCRU6FR36e5w4nAGhR97MnZSEWAAZAMfQdRFHo0smfrliK_FVgXegN81e5pKmcwmJcZDMqDlryoZ3MpjF8RzeEixURwWzvo2IhiuUW5sKPy9UzIDypcPOwOCVJ1lgSLSBi7NHFvSb5VZyWki_X52Fq5-Nio3oBouypf4qbUbZssDBUqMpQczw2UvRhCkVbmu7C3STmmUfllGffI33zIePittU3DRhWEgjQ5ooKpjIaYRKLmlMX1W2gO0BnjjQmHz_ixEogLThp9EigvvgZQRsMSqp3QComHyyrpXOGwvT3kcWEiBuG1-gVXRayV-y_kYcun1jWyjdHqddtE2WxBZ9Y5saM3GOEKmdbGB1ea1vWwDkKs3pCD5N_lWhjThB9wL4QhhkP4naimu4VkWAg9cfmMMQqJaiQ2DU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f21d2d79.mp4?token=WAYPxMPc_FiHI46BsmzqumLK9ZsFVv54W7zQr9sMNwDLTNPXz2erKuBIDGgAI_N3tFZJ-i3P8jJ4yObvlnTFaWOy83jR8Jqx4NKsTm01Lg7mCdydxKo4JeyF59RLK0eaHlS_fiuET5Zvmp8XELcypyxdM_0kD6ijrY54WopQdgoGSS2pWUzf7dEmIShjylUucM0KRr899g4WQ3F7qp4mSYTdjJD3nt46pCK6t3bNC1g4mH_PvnSnwgY5wHSIFUko3o9OTlaUO7tCRU6FR36e5w4nAGhR97MnZSEWAAZAMfQdRFHo0smfrliK_FVgXegN81e5pKmcwmJcZDMqDlryoZ3MpjF8RzeEixURwWzvo2IhiuUW5sKPy9UzIDypcPOwOCVJ1lgSLSBi7NHFvSb5VZyWki_X52Fq5-Nio3oBouypf4qbUbZssDBUqMpQczw2UvRhCkVbmu7C3STmmUfllGffI33zIePittU3DRhWEgjQ5ooKpjIaYRKLmlMX1W2gO0BnjjQmHz_ixEogLThp9EigvvgZQRsMSqp3QComHyyrpXOGwvT3kcWEiBuG1-gVXRayV-y_kYcun1jWyjdHqddtE2WxBZ9Y5saM3GOEKmdbGB1ea1vWwDkKs3pCD5N_lWhjThB9wL4QhhkP4naimu4VkWAg9cfmMMQqJaiQ2DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادویه‌های مفیدی که با چای باید خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/682888" target="_blank">📅 22:03 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
