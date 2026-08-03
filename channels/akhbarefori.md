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
<img src="https://cdn4.telesco.pe/file/jG8lb3WrLKFdL9tZMulcP6Pi6-_bKDPMzqvTsBq4TLAj2tALaDJCEtYI27Fpln92udpfY-TVzldOw3twUQWFH6TEQyiMYGtGyvOvsalMrk9Schd5m8AF8o2BD2HjwViiRHoZlsfKIyTA5CymoHdTL6D8vPam_a4Yow9fffSYuyjoIuaW3BZT0wcld-mOOy14uSvCkyNQjWKGFGXK5q6ZctdloOFqwk77motg4-cqnvAzHDYswGtk3OtSOSPhTsxx-kxni0weC4ZCph3j_Ob8GEE-npklHVOeCzC2uYqrr8pFLtkgQDBBWwjfrIeggQq027KdTYCtQr6qI427q48nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.06M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 22:13:24</div>
<hr>

<div class="tg-post" id="msg-678179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcFAoyOOri4xJkbJVYMcpx0OXz7zG3v3S6apAG0IWNsRykERLNGTC5BWYmmT5t7aEhpcD9hS7ShKRtuEeWrEfOf5olSlKw9jc0YsM1fj_nNOB_yKRCnhOOIR6KDNEheRwpjcVGwC-DIHbUO89k94qUhsgneoACIi3Nnapv_vYQt5MCftlyF4tbPL2n0aAZakf1tjqRbGM0_kKkGnUbmCZqbSz2pa6KCyQWLUotnvoLK5vOGB2om7gqzsUfBU-LF-0MPCSSaI92uD1VFUUIDXjPogMGStwBKv89C3_SHYfxG4HXuNfRteJnxkgf-mitUwmNCDk8xywXPd8V5WjIwKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرصت‌ها مثل ابر می‌گذرند؛ آرام، سریع و بی‌خبر
🔹
در حکمت ۲۱ نهج‌البلاغه، امام علی(ع) یادآوری می‌کند که فرصت‌ها ماندگار نیستند. بعضی لحظه‌ها فقط یک‌بار از راه می‌رسند و اگر قدرشان را ندانیم، شاید دیگر تکرار نشوند.گاهی یک تصمیم به‌موقع، می‌تواند مسیر زندگی…</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/678179" target="_blank">📅 22:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeef354708.mp4?token=V2Pt6GySOmACanIRJUTzCPaUqBFUSG48eSr8Drl2j0nAz66QhS4lpY0KM8vwgZOXwpk7ICdEVcj4lB8V81yqHjNSAKje5xDnt-oalCK7_UW0roS8OZuis0z0YwNLjX7qHSLh3eKm_PqSWeAw0H_wPwlWoU4WB49s9SgTjSecn_FTSGuc8cB0QDjg1SqAjqmOt-439XQ8qmcxGLOKS8WJ5KTOAeAS6S3NopmEU9UZNMAVqGh9DcI2BYklDmWyE7cji4R2JYA1KtbkboH75ROp4qbH3HjQyE1a8EhmVWFVHYCNhhhXdzQvR0s60K_EBFT3P4S63Bp10jPvGiIRLCVoMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeef354708.mp4?token=V2Pt6GySOmACanIRJUTzCPaUqBFUSG48eSr8Drl2j0nAz66QhS4lpY0KM8vwgZOXwpk7ICdEVcj4lB8V81yqHjNSAKje5xDnt-oalCK7_UW0roS8OZuis0z0YwNLjX7qHSLh3eKm_PqSWeAw0H_wPwlWoU4WB49s9SgTjSecn_FTSGuc8cB0QDjg1SqAjqmOt-439XQ8qmcxGLOKS8WJ5KTOAeAS6S3NopmEU9UZNMAVqGh9DcI2BYklDmWyE7cji4R2JYA1KtbkboH75ROp4qbH3HjQyE1a8EhmVWFVHYCNhhhXdzQvR0s60K_EBFT3P4S63Bp10jPvGiIRLCVoMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف درباره ایران: به من زنگ می زنند و می گویند: لطفا حمله نکنید، معامله می کنیم
🔹
این حقیقت مطلق است و همه آن را می دانند.
🔹
چه کسی تماس نمی گیرد؟
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/akhbarefori/678178" target="_blank">📅 22:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678177">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65010e1c6b.mp4?token=J9TjtN6Q4Yv57OH0NQ3cb0wxe-bKkdo12937rfeW9YrLVGaY3sJnWbQRI4DteOSxieBdS84eyPsA6E8oeRykjXUKkA0wq2TylPBxKh6c38PQViLKk0hXq6avgN9WsQyzfkRfqIJiq4aOC4FB8ErumV65CyqNs--JGSjGAHERSx4xS5iy8gY9pRtZUVCq53bo0WsmEkOfjQwS0o_G0ZV3JBFkR4Htzkdavsd6bgp0Q_3RF-IUL1_np7h-sJqNf_XiBd65nnzgxM2GtIHHFOrnQn4XmrfRAF_rfwiexmqb9eFCdfSrCyQ33I2DDqdnSCYO4aakBGVxAQfJGNM6GCTjuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65010e1c6b.mp4?token=J9TjtN6Q4Yv57OH0NQ3cb0wxe-bKkdo12937rfeW9YrLVGaY3sJnWbQRI4DteOSxieBdS84eyPsA6E8oeRykjXUKkA0wq2TylPBxKh6c38PQViLKk0hXq6avgN9WsQyzfkRfqIJiq4aOC4FB8ErumV65CyqNs--JGSjGAHERSx4xS5iy8gY9pRtZUVCq53bo0WsmEkOfjQwS0o_G0ZV3JBFkR4Htzkdavsd6bgp0Q_3RF-IUL1_np7h-sJqNf_XiBd65nnzgxM2GtIHHFOrnQn4XmrfRAF_rfwiexmqb9eFCdfSrCyQ33I2DDqdnSCYO4aakBGVxAQfJGNM6GCTjuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: من می خواهم قبل از اتخاذ اقدامات شدید، هر فرصتی را که می توانم به ایران بدهم
🔹
امیدوارم به خود بیایند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/678177" target="_blank">📅 22:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678176">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isAqfNhZEddtR09UML9mY3nwhlx1cLY7KODtg3jNMCXwNW6wIWYyapstboQY_uDEzK2kwfwnaX5RCVmnrY6tXA2slKpEh4vGbmWJTCvz6X7xqUwTw2Dn_rNlTpoQ23zpEvLhBRjOJqXNeHNFhfguQAUy6bb2D1apeTEDLszbcwqBkABclyVuo1Xy9D-CfmuqBKIN1GSe--CVBkG7FX12ne-hBejLLDyYVU4FtDyEtIhFJXMqJL0UP6dNsIPJIdIDKPuwb6bRH7L7sRJsJwjaZ3BZeHSBfAcLIitSmF3kwYbyQEb0B67rJrVYYUMGdbieAOwTo64WV0dPDEp17_ZwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نوبت به بیمه ثالث موتور رسید!
یک موتورسوار حرفه‌ای همیشه برای مسیرش برنامه‌ریزی می‌کنه. خرید بیمه شخص ثالث هم بخشی از این برنامه‌ ریزیه که امنیت خاطر شما رو در هر تردد تضمین می‌کنه.
✅
برای اینکه با خیال راحت تردد کنید،
بیمه‌بازار
خرید بیمه ثالث موتور رو براتون ساده کرده:
•
مقایسه سریع
قیمت شرکت‌های مختلف
•
خرید اقساطی
•
صدور فوری و آنلاین
👈
خرید قسطی بیمه
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/678176" target="_blank">📅 22:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678174">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حمله پهپادی به کشتی تجاری ترکیه در دریای سیاه
🔹
خبرگزاری ریا نووستی روسیه از وقوع یک حمله پهپادی به کشتی تجاری ترکیه در آب‌های دریای سیاه خبر داد که منجر به بروز تلفات انسانی شده است.
🔹
این کشتی که حامل محموله میوه و تره‌بار بود، در حین حرکت در دریای سیاه هدف حمله یک پهپاد ناشناس قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/678174" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678173">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224327602.mp4?token=pKZz-yjhE-1_-HckiqFpcD24__1uWYbGzq5Hex9u5aktwGAGRWtUBOrC08AoowPEFyc_1aw2hyR-6muAy3L5q_HflCrBKQ42RoFn13ZDrctrYd4yL2T1KjAMWLt85c4jgOPA7OEw1O_cbcRJWCMiWnjCcNvSwnkDgNFEoNsL0-4WrdwjeCKEBmyBNKvWMYVgxEpk7IkLtfeojb1a-BEZrbpA3W6mzz8vQR-WXbUTDQSNXlSd6ZJjGu8WZpqZPIbCgnNrZzCmRbYQrZMQO5ztdroBUSe3Ci7nh_RvkKmsNT8NXhzQObMusEbONP_0uXj6ugLe7Ii9FcNzR_v32j-lsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224327602.mp4?token=pKZz-yjhE-1_-HckiqFpcD24__1uWYbGzq5Hex9u5aktwGAGRWtUBOrC08AoowPEFyc_1aw2hyR-6muAy3L5q_HflCrBKQ42RoFn13ZDrctrYd4yL2T1KjAMWLt85c4jgOPA7OEw1O_cbcRJWCMiWnjCcNvSwnkDgNFEoNsL0-4WrdwjeCKEBmyBNKvWMYVgxEpk7IkLtfeojb1a-BEZrbpA3W6mzz8vQR-WXbUTDQSNXlSd6ZJjGu8WZpqZPIbCgnNrZzCmRbYQrZMQO5ztdroBUSe3Ci7nh_RvkKmsNT8NXhzQObMusEbONP_0uXj6ugLe7Ii9FcNzR_v32j-lsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آسیب‌دیدگی برخی ایستگاه‌ها و پالایشگاه‌های شهر ینبع عربستان پس از حملات اخیر انصارالله یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/678173" target="_blank">📅 21:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678172">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moL1Sk-T4bRRZdfsfdMAXpE3Hc_1QezkgqQpVMqtscNICaWXmQ0A-T08de4z3Sf-UTp9AU1K-ThrWJV8Lphhm7pgPCb0s4s33yhXrnDo9DQVtsXXLNkWZg3rcatfwwPpwXHJ6DiQiKz2MtagcPo9ZVLi7P-SqzOiQNAitxt3Xrer_xigLYTGRqBF5c3euHgfyS1ngwK5yy1lxo4y2zg8TIu1wGK3rr7-4JQRikbZ0c9854hGFskGzv0qhRPuu8SVG6w_jSx9S2O9IeiAaJeQdtzdy8h5Yin9v4m0ysfY31F99Bn2WMyeAdvKfhd1CpwkH1KSpYyILVNkt3alXJH5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زهرا، نوه خردسال آقای شهید ما هم اربعین امسال این‌گونه زائر حرم سیدالشهدا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/678172" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678171">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
پروفسور آمریکایی: ترامپ مقابل ایران دچار فلج استراتژیک شده است
🔹
رابرت پیپ، نظریه‌پرداز، نویسنده و استاد تمام دانشگاه شیکاگو در مصاحبه‌ای امروز دوشنبه عقب‌نشینی‌های مکرر دونالد ترامپ مقابل ایران را نشانه‌ای از «فلج استراتژیک» او در جنگ تفسیر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/678171" target="_blank">📅 21:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678170">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a71f2f93.mp4?token=XYukc3qgeil8ByitIM6fuGnyZiLAkRF7HAdHMyGfuTbpj2u3ipCJ2TZ9-_t01iw9_Kd_qCmzzD6hHf6yWql9J5U_CmNUk_V8GBukw2XLjprpd_KOtbCWLNms_bPAY-LBquQe1SlvQElz5jOnNVEVCev0n5DzcCKAUExxBNk8Umy3lbxLijGeculZpGAst2JpTcr_3AI9KZv5CUXryNJb3mGY3xIlYXbyaon81y5Yoqlt2xRgWDz5ehFT39JIubjXnUfLGJUa1T3VARYmP9S0AP2w4tDFBSVhhL5r1DCZB-TRdIsEFpSvMKPxIU9CazRLOCBlCsBNvcjyqxtx7PcykA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a71f2f93.mp4?token=XYukc3qgeil8ByitIM6fuGnyZiLAkRF7HAdHMyGfuTbpj2u3ipCJ2TZ9-_t01iw9_Kd_qCmzzD6hHf6yWql9J5U_CmNUk_V8GBukw2XLjprpd_KOtbCWLNms_bPAY-LBquQe1SlvQElz5jOnNVEVCev0n5DzcCKAUExxBNk8Umy3lbxLijGeculZpGAst2JpTcr_3AI9KZv5CUXryNJb3mGY3xIlYXbyaon81y5Yoqlt2xRgWDz5ehFT39JIubjXnUfLGJUa1T3VARYmP9S0AP2w4tDFBSVhhL5r1DCZB-TRdIsEFpSvMKPxIU9CazRLOCBlCsBNvcjyqxtx7PcykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کودک کش: من به ایران اجازه نمی‌دهم هزینه‌ای دریافت کند
🔹
اگر قرار است کسی شارژ کند، این ما هستیم.
🔹
ما کنترل کامل داریم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/678170" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678169">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21c4ec7f1.mp4?token=VdgpN52-IzIxOSOznOnuFiaxAbA9poDNrn-ILtU-x1WVs043RQ-u79IiUZGTcnYN6bpBxZuvTjONgwbpAAYuQw3-ojg6kql0oisugKg3lmRVA9Z5e9FUheXMC5xpZDNRl7vicvdg5dFio9pmRbQbcTuW2AuKXEmvnRZRGQRHT7LqQ2x7Jb2gAcwrpYMC-REfOS6ic3e6LDSLeL6CV9jN5vmg3rGRKGEFUzs_GEu4KzfAM_jmYA6TOUGo9dd4Iah5C4r24voANAlENiUuKTHZOQsjB0VD5-3KM95-0t0-T87H3O19JQWeT7w5HW-ENABTMib3X6AExATnqjHKLQ1wyZDc7S_LZbxKOb_OsANSR3LAa5iIWATdnKADWJK2ZMexRJ5xoSofK1CXKR9U_ul7zxiSA3PHORTLh9snUIxTDpNcOK-CVJqoanSRe6Xm-BezyD7erhtPUmLAgZ9DAYXW6moJh6byMKCtaqw0PyCIMZVhKzEhusetxJRnAv5nGxDDlFHxI_8ILEs2YxQbMznLT-Ej8Pexxis3CsdzXP95ELcpBw1rn57OPLkxjScSUbYQ8KkSPLCCZebIh3eNXOTHLnmzaWZgoeAmDwdja3Arlaxw1iqp7hZZvTlv5ocD-PU8RxVaNfzddKaNEHaI5iqFBdjKlWu6Aji5YogW42M48TY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21c4ec7f1.mp4?token=VdgpN52-IzIxOSOznOnuFiaxAbA9poDNrn-ILtU-x1WVs043RQ-u79IiUZGTcnYN6bpBxZuvTjONgwbpAAYuQw3-ojg6kql0oisugKg3lmRVA9Z5e9FUheXMC5xpZDNRl7vicvdg5dFio9pmRbQbcTuW2AuKXEmvnRZRGQRHT7LqQ2x7Jb2gAcwrpYMC-REfOS6ic3e6LDSLeL6CV9jN5vmg3rGRKGEFUzs_GEu4KzfAM_jmYA6TOUGo9dd4Iah5C4r24voANAlENiUuKTHZOQsjB0VD5-3KM95-0t0-T87H3O19JQWeT7w5HW-ENABTMib3X6AExATnqjHKLQ1wyZDc7S_LZbxKOb_OsANSR3LAa5iIWATdnKADWJK2ZMexRJ5xoSofK1CXKR9U_ul7zxiSA3PHORTLh9snUIxTDpNcOK-CVJqoanSRe6Xm-BezyD7erhtPUmLAgZ9DAYXW6moJh6byMKCtaqw0PyCIMZVhKzEhusetxJRnAv5nGxDDlFHxI_8ILEs2YxQbMznLT-Ej8Pexxis3CsdzXP95ELcpBw1rn57OPLkxjScSUbYQ8KkSPLCCZebIh3eNXOTHLnmzaWZgoeAmDwdja3Arlaxw1iqp7hZZvTlv5ocD-PU8RxVaNfzddKaNEHaI5iqFBdjKlWu6Aji5YogW42M48TY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: فردا آخرین فرصت ایران است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/678169" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678168">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9041bec7.mp4?token=BY79VNZtkbqSV0OV99yfDSaG7t1R_MaIb5QcNdCa-xBsiLYv82X3YScHE_j503EUnGe7wkO9Z71IIuWF_pWomVgDP5-MvISPIZ-ZZjVlCALWMDuFCO9l8O4ducPG5n8Uk50EOvYyrexWbDdYmtUDwr2fk1Luc20hMvAgu0XxLqe24HqEbuEcvlVUH4UL0gMpPfowAU4MQW-EJ_o1q7Q5uu86bvyPMpLsaQ2b_f-D-GLL3XsZVBnV3MYL4n36ZkvFjQhHTB8tUs1QU0fgbmmLQA_EF03sV4wF9QhAvSmCeSKniOKgKcFMK9UM4nN6XOHel8XwR2XdKLc_Tdp3d4KIyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9041bec7.mp4?token=BY79VNZtkbqSV0OV99yfDSaG7t1R_MaIb5QcNdCa-xBsiLYv82X3YScHE_j503EUnGe7wkO9Z71IIuWF_pWomVgDP5-MvISPIZ-ZZjVlCALWMDuFCO9l8O4ducPG5n8Uk50EOvYyrexWbDdYmtUDwr2fk1Luc20hMvAgu0XxLqe24HqEbuEcvlVUH4UL0gMpPfowAU4MQW-EJ_o1q7Q5uu86bvyPMpLsaQ2b_f-D-GLL3XsZVBnV3MYL4n36ZkvFjQhHTB8tUs1QU0fgbmmLQA_EF03sV4wF9QhAvSmCeSKniOKgKcFMK9UM4nN6XOHel8XwR2XdKLc_Tdp3d4KIyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک پلید: مذاکرات به سرعت پیش خواهد رفت، این یا آن صورت. خیلی هم پیچیده نیست
🔹
ما در مورد باز کردن کامل تنگه هرمز فردا صحبت می کنیم.
🔹
سپس در مورد توانمندی های هسته ای ایران صحبت خواهیم کرد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/678168" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678167">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c6a2a1f36.mp4?token=V_pOxFL4IX4VednRZDkZyD1Agxw8E8N2EFu8sRFrEuwWjgF-xhOfc0Ij7plRkB-SJfcyBuGBiTDjN2FmyTfr5V6udmU39dWMU5Vrqkq_ljVhvvVZNOy38nfq8ffzuCxjKyA4aNLCUW7XP-Y4SAsIUGsWvy45kPKF4_FA04Jf5dXlxjxVMZWXaTURWdN8GJvvVu2vo9DrOKipiIHfrA03PSWktesYwAmIeG4betNHMXnoKbaHfd7wvMXMI2lidETau_N_h41UL7dNbyRFMUxraKr-ve_OGTT3WCfjD0AeywIupwbWxYUuRfo3I_g5-is9QPV7ySXDEmqAPnwTKXO3pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c6a2a1f36.mp4?token=V_pOxFL4IX4VednRZDkZyD1Agxw8E8N2EFu8sRFrEuwWjgF-xhOfc0Ij7plRkB-SJfcyBuGBiTDjN2FmyTfr5V6udmU39dWMU5Vrqkq_ljVhvvVZNOy38nfq8ffzuCxjKyA4aNLCUW7XP-Y4SAsIUGsWvy45kPKF4_FA04Jf5dXlxjxVMZWXaTURWdN8GJvvVu2vo9DrOKipiIHfrA03PSWktesYwAmIeG4betNHMXnoKbaHfd7wvMXMI2lidETau_N_h41UL7dNbyRFMUxraKr-ve_OGTT3WCfjD0AeywIupwbWxYUuRfo3I_g5-is9QPV7ySXDEmqAPnwTKXO3pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان پلید درباره ایران: این آخرین فرصت آنها برای امضای یک توافق خوب است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/678167" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678166">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7424851c8f.mp4?token=SD_90XmD_5CZddQdYPoOcaKTz6NOruvZPpyNONEXKcxukPezoPrkUm9v4eshBMxdk-A3XnXS9BIy7gSaSRQfM64iQxJRv1NsqkeHNzjqRTMtUE5HBrBs-d6CPt3hn_paJJN-JIkTJNF_4XF61Sb6YFvNJtB1oD0dDfGjFlAE5GyfRhdCaWGFvLE62LQeoN5cSpvMIcPtyVizwlkz-Ya51hnuWf2n0qB9hoH0cbHI3oj5s66uNMdtB3uUWYa-bprjLahuCF2tGVU2kF-9IoCGNQJrY8WpqXRrm-fhd9xY8t0uulKWlr8Nu_ZPLtwwCnp2WmByoGF0rxV2tLL4dkjiGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7424851c8f.mp4?token=SD_90XmD_5CZddQdYPoOcaKTz6NOruvZPpyNONEXKcxukPezoPrkUm9v4eshBMxdk-A3XnXS9BIy7gSaSRQfM64iQxJRv1NsqkeHNzjqRTMtUE5HBrBs-d6CPt3hn_paJJN-JIkTJNF_4XF61Sb6YFvNJtB1oD0dDfGjFlAE5GyfRhdCaWGFvLE62LQeoN5cSpvMIcPtyVizwlkz-Ya51hnuWf2n0qB9hoH0cbHI3oj5s66uNMdtB3uUWYa-bprjLahuCF2tGVU2kF-9IoCGNQJrY8WpqXRrm-fhd9xY8t0uulKWlr8Nu_ZPLtwwCnp2WmByoGF0rxV2tLL4dkjiGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ما اکنون به درخواست ایران و با حمایت عربستان سعودی، امارات، قطر و دیگران صحبت می کنیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678166" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678165">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e13546124.mp4?token=o_Jh6afnLUgeS8LUwso2pioiBmEaWtirjBgmkylWDxeUalx1N6JgBvVbPKXNOA8jV3uZytsndh1rq78NIJ2Z9rApwEE3nA-6H28m3z0gs_qKQ_73XLLuioXk8DN7Prnbqv3bj214tePqGv6GUaHM7w3AzJcun77NudeFyfMCoK3KQjthiwT_XWE9_JCCizUxv3zRR8OODxpKHwgoUCGfu_6lgmgjvhRMk4Hb36kTngnfYRlT-W43cHkbaUjrz4wxdTfvGZidmZn9ETWZu_TfbLOtqj1XNO5oe2zjGeY3FcvDaPm66E_ND4dgZ2_Fu1O2Eotg1vO0JWSxeXOZDPDqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e13546124.mp4?token=o_Jh6afnLUgeS8LUwso2pioiBmEaWtirjBgmkylWDxeUalx1N6JgBvVbPKXNOA8jV3uZytsndh1rq78NIJ2Z9rApwEE3nA-6H28m3z0gs_qKQ_73XLLuioXk8DN7Prnbqv3bj214tePqGv6GUaHM7w3AzJcun77NudeFyfMCoK3KQjthiwT_XWE9_JCCizUxv3zRR8OODxpKHwgoUCGfu_6lgmgjvhRMk4Hb36kTngnfYRlT-W43cHkbaUjrz4wxdTfvGZidmZn9ETWZu_TfbLOtqj1XNO5oe2zjGeY3FcvDaPm66E_ND4dgZ2_Fu1O2Eotg1vO0JWSxeXOZDPDqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف: دیروز قرار بود ضربه محکمی به آنها بزنیم. خیلی قوی قدرتمندتر از هر حمله ای از زمان جنگ جهانی دوم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678165" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678164">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735f9b35d6.mp4?token=C202C4xQvSHZEXEexic_ltDRKHqMcXut0kF9-iiVOLDivWPWDAxiz0wlyTSvxXHvgcUAEP0mBmbSJYR7kCLS6XdDOtbu5OH9YXvXx9In0YG5vcmY4YZCcEcMf5d4Tw5Ul60xT12UAundDy9RUIi3IuJApC7be66-PXeKh93fiFaYGsOtVbIgq5P_E8MfsOH6MLjjMsysVlJtibkwaB7o2kT2xOJuErZVpeKsXJtiL9y4sKl5cv1p0XcLvQwUZwiNSP1FC3jLYxVPUlySMbQNeput4IzdNjuzb19DbuUgMZw2CNqbVdhtfnX9PDYVaK5Xw5PeG3tp-1vG344r-QCnzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735f9b35d6.mp4?token=C202C4xQvSHZEXEexic_ltDRKHqMcXut0kF9-iiVOLDivWPWDAxiz0wlyTSvxXHvgcUAEP0mBmbSJYR7kCLS6XdDOtbu5OH9YXvXx9In0YG5vcmY4YZCcEcMf5d4Tw5Ul60xT12UAundDy9RUIi3IuJApC7be66-PXeKh93fiFaYGsOtVbIgq5P_E8MfsOH6MLjjMsysVlJtibkwaB7o2kT2xOJuErZVpeKsXJtiL9y4sKl5cv1p0XcLvQwUZwiNSP1FC3jLYxVPUlySMbQNeput4IzdNjuzb19DbuUgMZw2CNqbVdhtfnX9PDYVaK5Xw5PeG3tp-1vG344r-QCnzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: ما با ونزوئلا اختلاف نظر داشتیم و خیلی خوب تمام شد
🔹
ما با ایران اختلاف نظر داریم و این اختلافات خیلی خیلی خوب پیش می رود.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678164" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678163">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e26ecf0d2.mp4?token=MQeMT95AmKrH8LQBUtQKMN6rgpEPlzOGMK-AA6QeC6mmt_CGkPvyX-zR-uM4iStSuvJH-pP6c8ml9pPe2iT1c3EWKDE1gzsUsoThkWNWue1gFpxmneUK5vyCGslGDls_Zu13FcHIX0nXymYZN0z5ktAyNlbz5TmWIEjJq4BYQJ9DyrR0rOn6Z5CtiPzDmPzxwpYCUcMVEhTqix52iijbcxVvnak_6Pdo5YO0YZy4R-AQGgtU2lFlPiB-yl29yrJXIWPIqfqTDvNZkoiML3E8OON-zCnqrm_hbIVmLqSleU1Waj8sL30CAyLn1ca0UMVOEg06uYnsnB53a-S1Qy64Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e26ecf0d2.mp4?token=MQeMT95AmKrH8LQBUtQKMN6rgpEPlzOGMK-AA6QeC6mmt_CGkPvyX-zR-uM4iStSuvJH-pP6c8ml9pPe2iT1c3EWKDE1gzsUsoThkWNWue1gFpxmneUK5vyCGslGDls_Zu13FcHIX0nXymYZN0z5ktAyNlbz5TmWIEjJq4BYQJ9DyrR0rOn6Z5CtiPzDmPzxwpYCUcMVEhTqix52iijbcxVvnak_6Pdo5YO0YZy4R-AQGgtU2lFlPiB-yl29yrJXIWPIqfqTDvNZkoiML3E8OON-zCnqrm_hbIVmLqSleU1Waj8sL30CAyLn1ca0UMVOEg06uYnsnB53a-S1Qy64Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف خطاب به وزیر جنگ آمریکا: شما کار بزرگی انجام می دهید
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/678163" target="_blank">📅 21:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678162">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46daf284a1.mp4?token=K_hQSM3IYpBZkYOSaYDubHNFXjb_OFHyYdEJbbK0yKdhWAe-1lLT6w1j10K3YqqP9VEi7N4yMqzjNV33JwBVD3mt0FHO4M6bcwGpgRoQ7DR-IVLVwsIWnA4zfuZIqt-Rba3KeOOp7YA4-Tooas-YWGZR132cmKxo3XnBKu9M-W9pJyBy-z0ByKeQnfp_BMm11UfgkzIRMxhTi7GPJ9Xecd0qIej8yg9FoBsjb-gIOeO2uIwONaAi4b7kwcuSLG8bFqYgi5CP59-ExNlCODkGIju0z9YsaGcJ0lqKD3khx5a-Dd2UTSa_UIgT-pqfj9luy4S5ZpNVUC64T8Np6JfvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46daf284a1.mp4?token=K_hQSM3IYpBZkYOSaYDubHNFXjb_OFHyYdEJbbK0yKdhWAe-1lLT6w1j10K3YqqP9VEi7N4yMqzjNV33JwBVD3mt0FHO4M6bcwGpgRoQ7DR-IVLVwsIWnA4zfuZIqt-Rba3KeOOp7YA4-Tooas-YWGZR132cmKxo3XnBKu9M-W9pJyBy-z0ByKeQnfp_BMm11UfgkzIRMxhTi7GPJ9Xecd0qIej8yg9FoBsjb-gIOeO2uIwONaAi4b7kwcuSLG8bFqYgi5CP59-ExNlCODkGIju0z9YsaGcJ0lqKD3khx5a-Dd2UTSa_UIgT-pqfj9luy4S5ZpNVUC64T8Np6JfvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: مذاکرات با ایران در حال حاضر در جریان است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/678162" target="_blank">📅 21:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678161">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/678161" target="_blank">📅 21:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678160">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2240c9d4af.mp4?token=lld6OTuqxD6L_A5rRb8gCQOWQMEgouLz4GHrw76fnkkNjyBTS0TDrdbMRXZziKv3TUbHZaaZc_Jn7pQ9Pu6Z5Q47jxotGIXrunFNjBC-OZVJ6lUpR80SlPJP2xBZfn6MPaeYGpyNkg7XyO7MDFBqW11ye4HtWaeQOviZaQwBN5iJQ5LwEpK4JHk-I_u5n6fJMkvlmqd4eGvqYA8z0G2aKcWMNg41iubMxpY2blg92WZCnByB-mYWz3qVw3eB1vYeRUEzMQIXLLSqYGJJLC13pdVaJkTN7iVdNpNJ1p08BtDcx2ZDI6-i_JA3ZsxKQXJ11bfst_lozhV1CiZZC06dgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2240c9d4af.mp4?token=lld6OTuqxD6L_A5rRb8gCQOWQMEgouLz4GHrw76fnkkNjyBTS0TDrdbMRXZziKv3TUbHZaaZc_Jn7pQ9Pu6Z5Q47jxotGIXrunFNjBC-OZVJ6lUpR80SlPJP2xBZfn6MPaeYGpyNkg7XyO7MDFBqW11ye4HtWaeQOviZaQwBN5iJQ5LwEpK4JHk-I_u5n6fJMkvlmqd4eGvqYA8z0G2aKcWMNg41iubMxpY2blg92WZCnByB-mYWz3qVw3eB1vYeRUEzMQIXLLSqYGJJLC13pdVaJkTN7iVdNpNJ1p08BtDcx2ZDI6-i_JA3ZsxKQXJ11bfst_lozhV1CiZZC06dgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز
کارواشی که روزانه به ۱۲۰ خودرو سرویس می‌ده؛ فقط با یک کارمند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/678160" target="_blank">📅 21:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678159">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/678159" target="_blank">📅 21:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678158">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
عراقچی: روابط تهران و بغداد در بهترین وضعیت تاریخی خود قرار دارد
وزیر امور خارجه در گفتگو با خبرگزاری رسمی عراق:
🔹
مراسم اربعین حسینی، مانور بزرگی است که وحدت و پیوند ناگسستنی ملت‌های ایران و عراق را به نمایش می‌گذارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/678158" target="_blank">📅 21:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678157">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwuItrlySUmvFxuHXnlxU8tXdLnfwvupgCXM79pwQ4bZJnK-78ET-xMskPL_vcTN9Kh5wgtzCZzH5Qi7kI92Sb6SvIaGGhCqHog3K6J63hMJVvwpklB_4YtHhED1UH0kENHfybMAwcrNgEwYiQKRqVfaP2LUjKX93vhI10PhzzENC3n5Y_TjxxIPV9Dy12TDSjehv2A7i5t-1l3hik_Q9nGpjUg_2u6B5l4Aj3CwbzwKc2aHBRM1FKvS_dtxOmOX-JXKHZq0m-DMzhX74YyeR4XrbJBAuVu1tzZ5fZAJxxWx9OgDCrUIHllf8trG5Z1KhqQheJ4tU-pNnqbwbxt95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک فروند هواپیمای باری نظامی از نوع Il-76TD متعلق به امارات متحده عربی، با شماره ثبت 7Q-ASU، در پایگاه هوایی نیواتیم در اراضی اشغالی فرود آمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/678157" target="_blank">📅 21:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678156">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryTrV467Jq30TH6x0lLD5TXm6UyZ8mH1-QMrmuNOgMMH_S64ynhpxqS65RwpaCNCAgtkHx8p3R5lUULwII6NzFTTYvCvpJveIyUHjDcFUlazt8g-AE6b29DCnKo_uz6pnVkgIZbKWaHibkCh0S813d09MKhCyhLfFPxJrnP4Ri_7ZIkchaCu2GoM0AfzclNsFp3DisoDa1zbwEbfNXdMcIpXShmezutWUpo2scYcbj3TlqafPhN8VmT7fb0BsYtPVt30IaXg_rRuwaUFK8x63gize4Ex3f5NSiVAbsuVAQBrva9j5M_ypWY9muk4vIudyBRGLWdTveDaCQcl26vVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خورشید
🔹
کارگردان: مجید مجیدی
🔹
ژانر: درام، اجتماعی
🔹
بازیگران: علی نصیریان، جواد عزتی، طناز طباطبایی، روح‌الله زمانی، شمیلا شیرزاد و…
🔹
خلاصه داستان: علی، پسری ۱۲ ساله، همراه دوستانش برای تأمین مخارج خانواده کار می‌کند. روزی مردی از او می‌خواهد گنجی پنهان‌شده…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/678156" target="_blank">📅 21:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678155">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
هشدار سازمان ملل در خصوص بحران دارویی در غزه
🔹
فرحان حق، معاون سخنگوی دبیرکل سازمان ملل، نسبت به وضعیت بحرانی ذخایر دارویی در نوار غزه هشدار داد و اعلام کرد محدودیت‌های مالی، روند ارسال تجهیزات پزشکی را مختل کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/678155" target="_blank">📅 21:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678154">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=Km4cEehB1awTOEwAjdJfPtxAGpzJ0G0g-7nwFQA9zNBQGDz5fBoCusvUH7kN8LJ93eWVZYPZkud8lOzan3JaaiAmSwQYmjnbABC4yFkO8lX_poY-RpoPPjiVEhIocRrP_KdVyqay33a1EO6iloby0wTL2fQyqDW8JHoF7h6x6E31HxsbA--r4lXrBnkGB-P6uAZl1naT1NXCaMTYzWyLbjfxltiK9-yTcwFxmimrfTW5Qmva0Xa6i1sjNW5pwCTkFutKc31_U9hEstrZc0EzekAs6cCdrWpP1qkLNg9fJPsvbss_gA19QtbjdX8X7Ri4a6MMwogOo9Ani8eLf6hIgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=Km4cEehB1awTOEwAjdJfPtxAGpzJ0G0g-7nwFQA9zNBQGDz5fBoCusvUH7kN8LJ93eWVZYPZkud8lOzan3JaaiAmSwQYmjnbABC4yFkO8lX_poY-RpoPPjiVEhIocRrP_KdVyqay33a1EO6iloby0wTL2fQyqDW8JHoF7h6x6E31HxsbA--r4lXrBnkGB-P6uAZl1naT1NXCaMTYzWyLbjfxltiK9-yTcwFxmimrfTW5Qmva0Xa6i1sjNW5pwCTkFutKc31_U9hEstrZc0EzekAs6cCdrWpP1qkLNg9fJPsvbss_gA19QtbjdX8X7Ri4a6MMwogOo9Ani8eLf6hIgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این کلیپ از حضور قهرمان مسابقات مردان آهنین در اربعین و خدمت به زائرین، میلیون‌ها بار در رسانه‌های عربی دیده شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/678154" target="_blank">📅 20:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678153">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRJ068uBOUsiYyIYB08-nWEfW27yYLqU0g1cUTNDVrR4QffeyaxVKFPjSOyMhI7nhXKZW0A0a6VlQrKJbGhp1TLZbnIT0l10zw4jeHO70tRvVylYfESSSux8sMRui-Z5zwjOaqBjvwKzf3SN3BYYEAjh9BNDHI_0EmurK4lN2vwG1QClzTzOnZfLq2Er6UHlcioWn4ghsSIJJftPg_cBMBAGB3ILh8emDHBiIyRpySFAvdVAglvdgSVNWIgP2N0QnTmnQ5FFUipsOxBJ31PvQvRH_9yPf47haq7mz7Anwbrv6hFpg2XF-_iXUuTuMT63yTno3XV5nOS6-ex3s9i3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جالبه بدانید چه گیاهانی حشرات رو فراری میدن
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/678153" target="_blank">📅 20:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678151">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxhzzU3N_MrXs1SWwYoC30RMMRyAYuuu3bd0SczfKjmhexaqMKSlP6R81phDfQATygnDr53CIGd6RwC6K_2hECNO6Cm4AVWGo_XWXQdM0NbfCgN064S5IGECA9EaFeU2J-LCdgmDE0EewFoehtQZNJxLB5a8ioxmZ2w1dNgJhauaLek-UrOb2SvCRobLmwslxRwB8l8w7x7A5MULMemIlLk5uq3dV8mJQ1etORxuwkPCc8x50WLjiMYjbU_mbYKYqHk3eP4qy1-wZoqEtWfjESCA30tWs6pHq5LLXJk4DppSRye78cmxlMrTPtf3sQ2O89zX-qXmFdwikwLqeNQiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHLpk0qsd-1wuPxLUelyBEs60rlo6mLbp7pEBFkYGbD6l-0tI_p3Z8VNSKxF0fkPX9AvT7Y_nLK6KfIMDRslEcEJaW-gBWdkqA_DWKkY1J9x9NDhri7cN5Y2d0CdKQd2pM9PJI2ANSYpOOvSGcSar534uW5tuj-elfkM91TdCycMRKjiPUEHCffAuh6MwT7Bfc1twCbN3KeBGycuNzPBwad5mP84YPBwiFCcb-C0osv3uC2BAEdq6yPXrkFE5OScVLLdxLIc6AvUckhIDjiE4eetcWXxa3_UQp9VxQBWtWUGK8NflPMcpnRymFWDFKQ2Q2aBsiqgbyvUnO13-NorEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست جدید خوک زرد درباره ونزوئلا: حق با ترامپ بود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/678151" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678149">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiOsnEvMZpoo-8BLpm6mtBS9g1NuS_8f-GaGR3okppOF3V3JQK1DR87nvk-GKYg9Y38OEo3nwPCN7ryLC9EeMmFZiVIcIsRtkYDGsLEqhIGlYC9Rrbutgo7Ij0oNwvZfyXn8vsZosKblLF_ojjVkbwWEQHE3nXyLCm-W20aQ3LzVV8RtWRJckZQAm5ch2PJVzeTBc0bAX3r31bIrFweA9k9KZszm3VWeYQCUbxjoQGSulX1GE28EHY1QEfzRwoz_osj9bvpxEnQ8asfse9zL9OVg9pnj-bNuBxxmSC-ZZsJh8VS4N7M30wQfipWoIMcqPGxeF4doaTdzl4nSnO8fNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه نقض آتش‌بس در لبنان/ گلوله‌باران توپخانه‌ای جنوب لبنان توسط رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/678149" target="_blank">📅 20:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678148">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKD-cbSk20FLNSXWsF9Gjc2Mj-Via3sFy9deeNkHWRkewvktWjers8jNOWHvN1s46G5R_Oki_Nu6eJ_Gf8tETrk45N_Q268ib6NqtkL6DSJRAokbNmQDXnLyAdH4h2GDVVUA8RfkiPm8zclzWJ9VPHZ7emOIxRYLHqI7zzLrx3Zto7qMzQHGqHCmp1QFewJgdmNVA_-tHmpEKVMpviq_OIR_KvVjvbo9UXG-H1c2QNp3BKIoGsl6vmjfziOdSg7Axzo9hZRZs-N0d6Z9mXAHwMZPvce7TRHJYdLXKelVolN-7t-JgyPDIFZkKOpObs_MUMmQKl8x9_PcWjVB5kLk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
اعمال روز اربعین
▪️
فردا سه شنبه ۱۳ مرداد مصادف با ۲۰ صفر روز اربعین است.
#طریق_الحسین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/678148" target="_blank">📅 20:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678147">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
از مسمومیت تا برزخ؛ روایت مردی که بازگشت تا حقیقت را بگوید
🔹
00:08:30 هیبتی مقتدر، با خشمی لبریز از مهر، مرا به اوج آسمان برد
🔹
00:28:15 مادر با قسم به اهل‌بیت، جان خودش را پیش‌مرگ من می‌کرد
🔹
00:36:05 چگونگی پاک شدن تن از پلیدی‌ها در آسمان
🔹
00:41:30 طواف معابد تمامی ادیان گرد کعبه و تأکید فرشته مرگ بر اهمیت آدمیت
🔹
00:51:30 ماجرای شنیدنی از مددرسانی امام رضا(ع) هنگام صدا زدنشان
🔹
01:00:30 آزمون الهی برای خانواده‌ای با مرگ فرزندانشان
🔹
01:15:30 علت تبدیل انسان‌های مسلمان و شیعه به حیوان در برزخ
🔹
قسمت بیستم (یک آزمون، سه برنده)، فصل پنجم
🔹
#تجربه‌گر
: علی لعل یوسف
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/678147" target="_blank">📅 20:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678146">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
دبیرکل کتائب سیدالشهدا: هر که آرزو داشته در مراسم تشییع امام حسین و علی ابن ابی‌طالب علیهماالسلام شرکت کند، امروز در مراسم تشییع امام خامنه‌ای شهید شرکت کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/678146" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678145">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a59201c0.mp4?token=AtT5IFGEY7AgMLv5nDHtkacmonuZoBCawiCU6LQBtp8fZpeEdEk_r0Vyn3TF6BmL6w-l7cV6GImVvV5jG1Ii5kN2MyS70bphkr0mlIY9QubbEMx_lmdGpnx-wL0xuw2Lnuc7_y_XZ1-KIecKU9P7wh3NNfOuAcipcraYHVPc4GCi4Sx_PYEgNMEURMNJnGIdlC56pLFVBvZ6pbDuMMOaLrfKvkRgkyTqEUFESP9t0BK83xrJP-CjscEtYhkWHKMz_al0LvoG7ulytPaoq6a7Q8kanaCwyNoerEys9R_XSQIW76S7Kd-TLJIXWT3hEXOphHpI8Z6Rqzo1Amu4EWO_KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a59201c0.mp4?token=AtT5IFGEY7AgMLv5nDHtkacmonuZoBCawiCU6LQBtp8fZpeEdEk_r0Vyn3TF6BmL6w-l7cV6GImVvV5jG1Ii5kN2MyS70bphkr0mlIY9QubbEMx_lmdGpnx-wL0xuw2Lnuc7_y_XZ1-KIecKU9P7wh3NNfOuAcipcraYHVPc4GCi4Sx_PYEgNMEURMNJnGIdlC56pLFVBvZ6pbDuMMOaLrfKvkRgkyTqEUFESP9t0BK83xrJP-CjscEtYhkWHKMz_al0LvoG7ulytPaoq6a7Q8kanaCwyNoerEys9R_XSQIW76S7Kd-TLJIXWT3hEXOphHpI8Z6Rqzo1Amu4EWO_KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در آینده ربات هایی با هوش مصنوعی جایگزین انسان ها می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/678145" target="_blank">📅 20:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678144">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
سی بی اس: مقامات آمریکایی می‌گویند با وجود اظهارات ترامپ، هیچ گفت‌وگوی جدیدی با ایران برنامه‌ریزی نشده است
🔹
تماس‌ها از طریق میانجی‌ها ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/678144" target="_blank">📅 20:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678143">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
وزارت جنگ آمریکا: توافقی را برای افزایش تولید موشک‌ های پدافند هوایی پاتریوت  به ۳ برابر و ضدبالستیک تاد به ۴ برابر امضا کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/678143" target="_blank">📅 20:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678141">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YARfU4rBGmfrlwHxVQd95pmq2xHZtUT7LW2deCejXJqwKcX9ZYsRhXkZHvh6EOfMuzT9QILmTIEXWBaLTd9YLeoPv4a00Nh8tq5LMubZtg0_-rlHaAx3UaA6flVQmwSbO5dWiZTC8aNYOBAo3t5YYNPkEiFIoUoJLkaL7sJZAftQrxvjIvG_-AFwK24ZZV55b5-PqzN1aIoieFDEcAfb3RQeaT2BOBF-HN3PsoWwG60nWs7aQ-jgApO28PN95iHw_SBMz5KXxXiwAbqi_sw2mob2y8qyOdvDubeSXsa3TjZimvpMg8ql5ajajQzUK5IDzglJjiXNPOcE-YJLM9dPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/678141" target="_blank">📅 20:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678140">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
امارات به اسرائیل سفارش فوری بمب دقیق و پهپاد داده است
روزنامه اسرائیلی هاآرتص:
🔹
امارات متحده عربی از شرکت البیت خواسته تا به سرعت شش پهپاد پیشرفته هرمس ۹۰۰، که در ارتش اسرائیل با نام کوکاف (ستاره) شناخته می‌شوند، را در اختیار این کشور قرار دهد.
🔹
امارات برنامه‌ای گسترده‌تر برای گسترش این گروه به ۴۵ فروند در قالب ۱۵ سامانه کامل دارد که ارزش کل آنها حدود ۱.۳ میلیارد دلار تخمین زده می‌شود. اسناد، یک پروژه تسلیحاتی دیگر به نام «یاسمین ۳» را فاش می‌کند که شامل تولید ۶۰۰۰ کیت بمب هدایت‌شونده تنها در سه ماه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/678140" target="_blank">📅 20:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678139">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjHkmLjEMVMzMyZMXEpFH_-0eRN1ddODDHZ0eSm4xPEfBL61UHRr76NlXhRbGYU1ou7rp_qyjryyMVHFNUQPPv8S5Q08KKOX5l-RniPm4-SJwkUrlbA1N0YpeC9k2nEX7myd3atqLuaSXbK119cBsjztgqOKZ_59lxek6Mz1ctQ51rDmGGbv0_h7RC-gyHgw9CHozEfWG4xdm87baulqyHKNtW2OJgCj9nOLzTB94VlaycVsABmhRy6bPYu8nGDrV8hNJoQe7UJHJ1BwjIcr5dQly7Ls9X5k0e5Tb-mHm0BIgpzHKo7KzFw43i0zGSQe_3VAXpGRk9wJQ4Z5idmItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع غیر رسمی از جدا شدن امیر و رهام و منحل شدن ماکان باند خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/678139" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678137">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
رویترز: ذخایر نفت در آمریکا به پایین‌ترین سطح از سال ۱۹۸۳ رسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/678137" target="_blank">📅 19:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678133">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNis4YRMCqr23D4PPWtErjshrpkRZjejJyOf1o5Xju2Ca7z3Ww-WH6IDkbm_xz2Ai6TVUGfDsWCmSD0EEbjSw7IeGGS6Jgr_dCcqsuLb8HWuUgOkcCmJ9voDgr64749A5KcDSrclgwZAoG4f3nEhbp8E5JDffFHfIu0FESTWjk5F3odddIPX3SOVcon7JMQvAyZWCO98gOOs_6jDH1mWnRtdavFkJz9C2Qmd3hEYiuy9eq4d23S_a7F9lm7Ejsok7h0iw0BSBMLc_cCCarcvikRipzQEXYeWgtQkgTI1bqJsYhnulHuJQFhzCsO5efTCRfiyy90t-WLFWCFyQkkmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zg45gV_EJa6fCU6LXpGkNCgotc2rBpCtu7orGFZZDfz8oB-Bv-vkVNRM8XAvvqr0fK8e67Tyu5ctBQgJe2G0GN6FKvSrh5Uc43xyIBM3d8AzUvP360xiyoNwh4U5Dd0eYqAd9IuOqtAp3KitZMRchWlwVLPtAeMHDP5Yk5xXL_MbvkaSmyXPEpQDSshe_9AmManBUb1Bw15YVmEuPbij99fTkYXNM0qR8EzMo-MNXXmEGqtMdtl2nQuYPVrU2Ep_E_VkmcXVnOpXKhKuIO2xtLBbcobbeuRL5YU2FFaNlGpybwVmgLVnTfLLC3-m4CvC3xQ6-LIK_1xg2h6mKIIdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oxUwYkOGLFGNVTaWHwsu9Vf_fCoi7J__8-yWW6uZ7S7vOyNYoVjE-wM7iRi7UBzoGKapDCPgkeipPnSzvOyEBJZDaDMoe7bkZsNMeVhxUNmb7rAFDNOLwQy__57VX1VYG-sGXZm9XMX-2PndxmzsJKSBV0IMbXszxdTkF8cwaSbxiVZyFWVFNoMPNn2yXnMLdRTHnvpIhZlAUWInpjONV9IOOGdGYTkZBwHGc4M9cRj8QANfWU6pDZKC7kil4Snxp2s68yBtw_a6xKDw3b3Cxnl30xCYcH7yuH_4nJmc2FSGvj2WKgmyj_vyUS8_uRbAqHekQA9otNRVPhlefdIjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-x1yxOxDPS-hl7dnMoNeNDJ6VW0ovzYgoBPDeB_FOPyazlXNAnZ_kMh9_YTOp_DkDJchKqx2rgkDH7kFCb12bcQamTPylarbK8IAkKpH_RJ-XxadF5TiRK2EXn5fz-IwoVtY_1uqBPxZgzZd9xwv2hP9ZCj8wHCOE34SCG6B3fUWv5hMERtfBrDzkeSMEaYd_ATAziJSz1iSdn0YPxwbLMx4N7QjSFQh-JOeCkM1q6YbhXyFRv-nQTRmBV4eM3fEHZgnTJrWoaFBJH93896O-5Gdhp5kSn8KvNVbJrNvZXXJbM8VeiN38MEHQDfjg3ZLu3cohPYoWeW1fpYl91dtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
میدونستی
نیازهای مهم بچه‌ها که ۹۸ درصد والدین
نمی‌دونن؛ چیه؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/678133" target="_blank">📅 19:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678131">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebee8d7d54.mp4?token=JB6MpWvT_uAtpxpQE4HFWVKG8beCFdtUat-3cqrFauStC2NmJNDkq23wPuanBzI3gL-aHryvHPajUMMclCFhgYVdNJRDe8P6ky9_BCR4NuOE1mqHM3eh4-NcepyH2uu7xAMzloTpB6BH13vCSAj_LrYAJgHksrO4f3oyYRMrGBHnvwQroS2mw4weft3GTf6PqHVeDJcYWN84H9bbs_SL2BoN3Fp5nWzcE2cAA0sPt7hqOGQd6WWj6rSXEtcmrWT96vgVtUSZDyOjoqdJOEDvZhel9txc45HrkagfUvZbNuNctdnt8UmuWfzHSJMIub8zhXNxSOQ1erZw5gaJvUgdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebee8d7d54.mp4?token=JB6MpWvT_uAtpxpQE4HFWVKG8beCFdtUat-3cqrFauStC2NmJNDkq23wPuanBzI3gL-aHryvHPajUMMclCFhgYVdNJRDe8P6ky9_BCR4NuOE1mqHM3eh4-NcepyH2uu7xAMzloTpB6BH13vCSAj_LrYAJgHksrO4f3oyYRMrGBHnvwQroS2mw4weft3GTf6PqHVeDJcYWN84H9bbs_SL2BoN3Fp5nWzcE2cAA0sPt7hqOGQd6WWj6rSXEtcmrWT96vgVtUSZDyOjoqdJOEDvZhel9txc45HrkagfUvZbNuNctdnt8UmuWfzHSJMIub8zhXNxSOQ1erZw5gaJvUgdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت روزانه ۱۰ ویدیوی انیمیشنی با AI به صورت رایگان
🔹
سایت Digen AI روزانه ۳۰۰ اعتبار رایگان برای ساخت ویدیو ارائه می‌دهد که با آن می‌توان حدود ۱۰ ویدیوی انیمیشنی تولید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/678131" target="_blank">📅 19:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678130">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33d8fc781.mp4?token=DHUJFLqqarUZkf5K0KnCs5Oc5fdSZfB15G0fHQslU6qQ5ujTueGxcDoUmvVnza9UAWvlOAbA7DqteWtrA0qfVUizOIQUfc0E0svbpJszG0KnbPZukdL8Hxs5fkU1TJ9Dsal_w08OazTxMstgStzpNJBd35vCbRTq6gRUZPItc5oyBVM6YK0B4uOrdegXOzx1hKxzLu7gibmkG-NldPl_RAITpp1vdkkRFa7SXbBYkjY8-CndUzGf0QcBmJOvJHxiA7DplCCN-2vog748WHc6bAuj5QdD5gcuCoOW3c8rDk9wuSd0-owFdAr18dZ_Yl0ZhX58nT2BN1yW0DjngOQlYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33d8fc781.mp4?token=DHUJFLqqarUZkf5K0KnCs5Oc5fdSZfB15G0fHQslU6qQ5ujTueGxcDoUmvVnza9UAWvlOAbA7DqteWtrA0qfVUizOIQUfc0E0svbpJszG0KnbPZukdL8Hxs5fkU1TJ9Dsal_w08OazTxMstgStzpNJBd35vCbRTq6gRUZPItc5oyBVM6YK0B4uOrdegXOzx1hKxzLu7gibmkG-NldPl_RAITpp1vdkkRFa7SXbBYkjY8-CndUzGf0QcBmJOvJHxiA7DplCCN-2vog748WHc6bAuj5QdD5gcuCoOW3c8rDk9wuSd0-owFdAr18dZ_Yl0ZhX58nT2BN1yW0DjngOQlYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسنوند مدیر مرکز توسعه پایدار انرژی: عمان خودش باید عوارض بدهد، نه اینکه شریک ایران در تنگه هرمز شود، عمان ۴ پایگاه تامین لجستیک امریکا را داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/678130" target="_blank">📅 19:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678129">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
‏
ادعای خوک زرد: رهبری ایران به شکلی باورنکردنی فریبکار است
🔹
آن‌ها درخواست برگزاری جلسه می‌کنند؛ حتی بعضی‌ها "التماس می‌کنند". گفت‌وگوها آغاز می‌شود و حتی برای آینده نزدیک نیز زمان جلسات بعدی تعیین می‌شود، اما سپس با افتخار اعلام می‌کنند که هیچ مذاکره‌ای در جریان نیست، هیچ موضوعی در حال بررسی نیست و فقط با "عمان" در ارتباط هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/678129" target="_blank">📅 19:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678128">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-l7VXkezWazeonTwDMBK-WjfA5sXXkj_eaUWXlbYcdciy3CLnbyiyMJeqg-WRf0Ly-FsETLYso01GJxbW7HUaHN9H9jxug_0No-Of6SlOnD2mKbh206k-K5IH8P3fGNMWlINQw2NTJQSd0-e5gNmDILB0kxvxfWV5ykHyIMmsDux6aNW0_HWKcJPimieVHpM713bXBnJZkZ96FePvQVcyTBRIWFiVVxyTOO_ywe-WXcxrlQniumaM-n4_qn-73AcZlNVN0pqIW6TZIYgWIO3ZVv7M6H5r7dnyTUiMo3MHeecy2rlEryNZVm3NWF77cmrB9vpBJCW175PVutv5ImRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک نجس: هیچ چیز بدون خواست آمریکا به ایران نمی‌رسد
ادعای ترامپ در تروث سوشیال:
🔹
«در حالی که برخی حتی می‌گویند ایران برای برگزاری این دیدار "التماس" کرده، مذاکرات آغاز شده و قرار است در آینده نزدیک نشست‌های بیشتری برگزار شود، اما آن‌ها آشکارا و با افتخار مدعی هستند که هیچ گفت‌وگویی در جریان نیست، هیچ موضوعی مطرح نشده و فقط با عمان در ارتباط هستند.
🔹
سپس طبق معمول ادعا می‌کنند که تنگه هرمز را با قدرت اداره خواهند کرد؛ در حالی که این آبراه هم‌اکنون به‌طور کامل تحت کنترل نیروی دریایی ایالات متحده و آنچه ما "محاصره" و برخی "دیوار فولادی آمریکا" می‌نامند، قرار دارد.
🔹
هیچ چیز بدون خواست ما به ایران نمی‌رسد و تا زمانی که توافقی حاصل نشود یا ایران به‌طور کامل تسلیم نشود، هیچ چیز هم نخواهد رسید. ایران چه این واقعیت را بپذیرد و چه نپذیرد، ما در حال گفت‌وگو برای حل مشکلی هستیم که خود این کشور طی دهه‌ها ایجاد کرده است.
🔹
موضوع کاملاً روشن است؛
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
»
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/678128" target="_blank">📅 19:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678126">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سردار کرمی: در کمین تروریست‌‌ها و آماده پاسخ قاطعیم
فرمانده نیروی زمینی سپاه:
🔹
شمال‌غرب، سرزمین دلاوری‌ها و غیرت باکری‌ها، در کمینِ هرگونه خطای محاسباتی دشمنان فرامنطقه‌ای و گروهک‌های تروریستی است. رزمندگان با اشراف اطلاعاتی، آمادگی عملیاتی و بهره‌گیری از ایمان، فناوری و علوم روز، آماده پاسخ قاطع به هرگونه تهدید هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/678126" target="_blank">📅 19:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/078d1d0337.mp4?token=gZ-FWCP-qsPJQCu2czwdiGkHitHqqCbeWGOB_Y-E78nDcbsy9uI5BDzBnKFPseNhEkVn5cMEub13sly7fN0qtDV1Rm3RKf7pGkIKg5_aKoaO1hvv2IfbvL8vazgZrYIK5nRj2EDWcrPw9R2oyv7pSp5CNpQHq6Pc6YLhTXyeHz-jsiDUeLT5M58Wn7PvH6LiGn24MOMVHjGO4HPROk63ob3e69DR-uWlpdToFvhH4nTlDy0qaOud-RWRyS3uc5JVXxOeQkVMXJ_FdkMhfJb5rW9VE0VIjO_dm3W5L_xHQJN43p2kbWs3s9sg7PfWFMHJzbjblhYu2rGd04lIQGC3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/078d1d0337.mp4?token=gZ-FWCP-qsPJQCu2czwdiGkHitHqqCbeWGOB_Y-E78nDcbsy9uI5BDzBnKFPseNhEkVn5cMEub13sly7fN0qtDV1Rm3RKf7pGkIKg5_aKoaO1hvv2IfbvL8vazgZrYIK5nRj2EDWcrPw9R2oyv7pSp5CNpQHq6Pc6YLhTXyeHz-jsiDUeLT5M58Wn7PvH6LiGn24MOMVHjGO4HPROk63ob3e69DR-uWlpdToFvhH4nTlDy0qaOud-RWRyS3uc5JVXxOeQkVMXJ_FdkMhfJb5rW9VE0VIjO_dm3W5L_xHQJN43p2kbWs3s9sg7PfWFMHJzbjblhYu2rGd04lIQGC3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚿
ماشینت رو مثل روز اول برق بنداز!
با نازل کارواش سرشلنگی بدون نیاز به دستگاه کارواش، فقط با اتصال به شیلنگ آب، فشار آب رو بیشتر کن و به‌راحتی ماشین، موتور، حیاط، پارکینگ و حتی فرش و موزاییک رو تمیز کن.
✅
نصب آسان
✅
پرتاب آب قدرتمند
✅
بدنه مقاوم و بادوام
✅
مناسب شستشوی خودرو، حیاط، باغچه و سطوح مختلف
💰
فقط ۸۹۸ هزار تومان
🔥
قیمت قبل: 1,098,000  تومان
🛒
فرصت رو از دست نده، با کمترین هزینه یه شستشوی حرفه‌ای داشته باش!
خرید از سایت
👇
https://memarket24.ir/product/brief/58365/180124/</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/678123" target="_blank">📅 19:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd23435855.mp4?token=vsu1iLpZp6Sdo8kQ2cXdVozn9BKl1WuDPryFy-w8t4x0r3-LXhr5s-NsGQ8XYHXdzqb-RDHOcF-4jSkLItv55VmU9n6_FkKfm8Xga7XEQfcyr5exrNXgMfgqmSFFgM0t78hbgwq2bESKqrkajqPdb3SgJrvr6qGmv9Im-ujuP_un7YYtFUTZo12wyqfoPhfFOzg4IilJRtvexvqdT_GA-i5Qs0JCnrgvE50wtZg3WIxaPb25L_St5k5NUl8bg5MG_vFgEVjNdzZhdpb5xmV_vUBAYkr2uMbwlarwPvYBeDkrn4TU9J6RzYcRZq44958e5ftdyAqWGbWfiXqE6MI5uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd23435855.mp4?token=vsu1iLpZp6Sdo8kQ2cXdVozn9BKl1WuDPryFy-w8t4x0r3-LXhr5s-NsGQ8XYHXdzqb-RDHOcF-4jSkLItv55VmU9n6_FkKfm8Xga7XEQfcyr5exrNXgMfgqmSFFgM0t78hbgwq2bESKqrkajqPdb3SgJrvr6qGmv9Im-ujuP_un7YYtFUTZo12wyqfoPhfFOzg4IilJRtvexvqdT_GA-i5Qs0JCnrgvE50wtZg3WIxaPb25L_St5k5NUl8bg5MG_vFgEVjNdzZhdpb5xmV_vUBAYkr2uMbwlarwPvYBeDkrn4TU9J6RzYcRZq44958e5ftdyAqWGbWfiXqE6MI5uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک نتانیاهوی خیال‌باف: اکثریت  مردم ایران، اسرائیل را تحسین می‌کنند #Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/678122" target="_blank">📅 18:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a25ac02ca5.mp4?token=Ur16-GSvf609-JeQj-jAvj14QHVj2zip27U5Z8vlvG56CrG3Kd39nliTLaDjxGfJ0hItZNiegU5Jm3H24b46Pnc10JZzX3i6WxhEdFqpyrbc91CEAfnlAm1PYuMzY5LOVKggK85dAxYDcPOpRxuqu-RBuHeWMvFQQyv-Ifv6D69egkxbA9WSvichzhVhgs8hjPf0aoaDDXhXvTa3P7zxv64tTqm1W5kaI5gAfVoJeTIOygnui5VzNsmvROXgUg_OukmNe2LjMdCzauCbBrvx-a3Dd3hN3R1_n8aAzFGbiroJQuiMq0IqV22yu-2ZXszP4gZVVuTGxHpMTTdbbN9wSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a25ac02ca5.mp4?token=Ur16-GSvf609-JeQj-jAvj14QHVj2zip27U5Z8vlvG56CrG3Kd39nliTLaDjxGfJ0hItZNiegU5Jm3H24b46Pnc10JZzX3i6WxhEdFqpyrbc91CEAfnlAm1PYuMzY5LOVKggK85dAxYDcPOpRxuqu-RBuHeWMvFQQyv-Ifv6D69egkxbA9WSvichzhVhgs8hjPf0aoaDDXhXvTa3P7zxv64tTqm1W5kaI5gAfVoJeTIOygnui5VzNsmvROXgUg_OukmNe2LjMdCzauCbBrvx-a3Dd3hN3R1_n8aAzFGbiroJQuiMq0IqV22yu-2ZXszP4gZVVuTGxHpMTTdbbN9wSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری و تحلیلگر سیاسی آمریکایی: آمریکا نمی‌تواند از ۵۰ هزار نیروی زمینی خود در منطقه محافظت کند چون موشک دفاعی‌اش تمام شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/678121" target="_blank">📅 18:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORBKVVuYrbILwLlBJHJujcE0xl6e98IhoQ7FAPG6veLHSxYYA-2FFjNDTH-xp5cswaMKTraWT3QzRNOMwNnoguiVYDA3pefmHVC-w9IWxRanBqjbx7pQzHHx8zHdSUFCAtv6CATJLbIAJ27YcxCkLCLcUOW92ej02ko0DiycTVSFCCnzHz6MJbrvuB1ZWq8MW6bJGwPtqbl5FJ-es_tDH-npAuw3uaUULxQUJ4yRf6YuWIFE32J8-CEvJlevTjRD_US73kKEgRMOonPxa18IMlK3wrWPdUcNYwB8VFklUVvjGnAPeqATC9k4BgJcq_GGzo5QTNxPUUcyPJgCPX0O8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایده غیرمتعارف برای حمله به ایران | پنتاگون در جست‌وجوی گزینه‌های تازه برای فشار بر ایران
🔹
گزارش اختصاصی سی‌ان‌ان از درخواست فرماندهی مرکزی ارتش آمریکا، سنتکام، برای ارائه ایده‌های «خلاقانه و غیرمتعارف» به‌منظور افزایش فشار بر ایران خبر می‌دهد؛ درخواستی که به گفته منابع آگاه، بازتاب‌دهنده دشواری واشنگتن در یافتن راهی برای پیشبرد اهداف خود در رویارویی جاری با تهران است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235318</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/678120" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b886a5807.mp4?token=aaI-Nx_QgZ84BmRJaKsBEkexD4lfpx4ViGeKKvY55iG2FRrhOZVBWyOMyfmzIYMenrDyOwwdxBvotQ9un3SXlHqwX3fJuV7FDqEEinnWeTotoKEfXfau0khgs8MAoHn5gbcXGwTkbayI7oCIjmy_UI5q4w2I2UfiX18QfXP63pbjSg8X-IYdk5NPKF1Eh-8O6go2bYvOc5Mu3C2VQ-LiVZmHbIncPIPrCUPv8AJSpfiMfsZ5jcNTW4W6f46_LYsp_1oPrOddQb8ncfvTsdYfONRXGZonG_QH1ZGd3183ocVN3YzW5fbUfFbrNffBLEP97sx6F9aUZi25yvQj__YD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b886a5807.mp4?token=aaI-Nx_QgZ84BmRJaKsBEkexD4lfpx4ViGeKKvY55iG2FRrhOZVBWyOMyfmzIYMenrDyOwwdxBvotQ9un3SXlHqwX3fJuV7FDqEEinnWeTotoKEfXfau0khgs8MAoHn5gbcXGwTkbayI7oCIjmy_UI5q4w2I2UfiX18QfXP63pbjSg8X-IYdk5NPKF1Eh-8O6go2bYvOc5Mu3C2VQ-LiVZmHbIncPIPrCUPv8AJSpfiMfsZ5jcNTW4W6f46_LYsp_1oPrOddQb8ncfvTsdYfONRXGZonG_QH1ZGd3183ocVN3YzW5fbUfFbrNffBLEP97sx6F9aUZi25yvQj__YD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری | به نیابت از رهبر در مسیر اربعین
🔹
صدای زائرانی که در مسیر پیاده‌روی اربعین، ارادت خود را به «رهبر شهید» با قدم‌هایشان نشان دادند.
🔸
پیام صوتی خود را ارسال کنید
👇
#زیارت_به_نیابت
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/678119" target="_blank">📅 18:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbgb5NsG1H7hMTEEw93hA_edXoHlG-_SlIs5Dd6eOdfEeWQYTekfgJ7G0NmufRL9yG2Gzuouj6OnZtdkyruHlVNix45PCKRPzslgOmxbAzBkWXwqAsSm6q2ExiOUARf2DBviAujnyL3EnJCiZrycIMgVxGSa5q8DH_7F7goT8AB_H7zaMoIYTU4qKD53TSjYJG-mszY4_WOvajHj_DuvjlvpTbVGrQ1f7A-Ru75DGyFTxhZQcBmfQOzsAnszxnrvDTYOtbp4Tvnkck8j_zpKezYkKtTpef-jnIgBwdugNBhZX7mQ2j3HCW6CCnamEZQWayPN_kJjgzsbu5I4MbubzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر جای بدنت یه علامت داره؛ کمبود ویتامین‌هات رو لو می‌ده!
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/678118" target="_blank">📅 18:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ageWgMSaHM8-EwtASLoc8YAjr0EkSfMwHAe7F-TkWJALZZP7heL35ezw1885ZdQ6QpgRnLaZmtfEiO97BxnhtLRYABKi-dvydmgPTAkWin7Yb0oc9cQD94B6JnIzvVzRfiYm52KkFp1DLx4aY4dbOWpQOU08tVlSfCFIZp5TYI-efqxORlt3Z6Zy9zF1c_DM8oVDmceZn4dftN4lWYPtbXoq3lzhibFpzJ5RTIPV8KLJXbYku63xYIyUFjVzntoGW7mfAhO_HYbrmotfLhIBBkwdT8BK02qcS5VCYIfrld5sCc1cPULZxMjubDdNvZVcRwJi23bwSKRk-SgkbEuzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صنایع خلاق؛ پیشران جدید رشد اقتصادی در عصر اقتصاد توجه
🔹
نشست تخصصی «بررسی ظرفیت‌های تأمین مالی و صادراتی وزارت ارتباطات و فناوری اطلاعات در حوزه صنایع فرهنگی و خلاق» با حضور سید صادق پژمان، مدیرعامل مؤسسه کمک به توسعه فرهنگ و هنر، حسن میثمی، مدیرکل توسعه و فناوری‌های نوین و تحول دیجیتال وزارت ارتباطات، حامد لدنی، مدیرکل دفتر راهبری طرح‌های کلان فناورانه وزارت ارتباطات و جمعی از فعالان و مدیران کسب‌وکارهای خلاق برگزار شد. در این نشست، توسعه زیرساخت‌های تأمین مالی، حمایت از صادرات، تقویت تولید محتوای دیجیتال و گسترش همکاری میان وزارت ارتباطات و زیست‌بوم صنایع فرهنگی و خلاق مورد بررسی قرار گرفت.
🔹
سید صادق پژمان در این نشست با تأکید بر اینکه اقتصاد آینده، «اقتصاد توجه» است، گفت: «در دنیایی که مهم‌ترین رقابت میان کشورها و کسب‌وکارها بر سر جلب و حفظ توجه مخاطبان شکل گرفته، صنایع فرهنگی و خلاق به یکی از مهم‌ترین ابزارهای خلق ارزش اقتصادی، توسعه نفوذ فرهنگی و افزایش صادرات غیرنفتی تبدیل شده‌اند. ایران با برخورداری از پیشینه تمدنی، سرمایه انسانی خلاق و ظرفیت‌های گسترده فرهنگی، از مزیت‌های قابل توجهی برای حضور در این اقتصاد برخوردار است؛ اما تحقق این ظرفیت، مستلزم تغییر نگاه سیاست‌گذاری، توسعه زیرساخت‌های تأمین مالی، تقویت نظام مالکیت فکری و حمایت هدفمند از کسب‌وکارهای خلاق است تا اقتصاد فرهنگ بتواند به یکی از پیشران‌های اصلی رشد اقتصادی کشور تبدیل شود و برای این هدف نیازمند همکاری و هم‌افزایی بین دستگاهی هستیم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/678117" target="_blank">📅 18:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
ماجرای سیا ساکتی و صندلی کودک!
🔹
صندلی کودک، فقط یک وسیله اضافه نیست؛ «کمربند امنیت» فرشته‌ کوچک زندگی شماست.
#سیا_ساکتی
#راهنمایی_و_رانندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/678116" target="_blank">📅 18:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ec6b5082.mp4?token=H7fTFWcIUoo4N40UWLIzqIIjCXYyj9z_o6rqr3SrlXQ5CSuQoPTDRJktvoNUDdEG78SgdLr4BcH8-VzzYiNA5bk0Hrr7E5eBWU4d_ZuoOAUTozShKG6H3trsUSVKLiOZlt4_jIINgK6wW0zi2iWwCwWX5RJCE6KY2u00JNGgZ9UXTt_-dlXWzQb9EnXGhmuFLqsA7Itsbpvl5IrBu7ZAJc-WqmG4-3oJYbVgoQatPf-g6eqRaDxVqyjqW6JT2oYiuM6v0Dn_mdkKkXuukVMADcN-ohDYRQj6r9YN1QsTcmgdZHpu3CzDl8j4WDlIjT71BYs7CRTEc1yUHcafyqr0VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ec6b5082.mp4?token=H7fTFWcIUoo4N40UWLIzqIIjCXYyj9z_o6rqr3SrlXQ5CSuQoPTDRJktvoNUDdEG78SgdLr4BcH8-VzzYiNA5bk0Hrr7E5eBWU4d_ZuoOAUTozShKG6H3trsUSVKLiOZlt4_jIINgK6wW0zi2iWwCwWX5RJCE6KY2u00JNGgZ9UXTt_-dlXWzQb9EnXGhmuFLqsA7Itsbpvl5IrBu7ZAJc-WqmG4-3oJYbVgoQatPf-g6eqRaDxVqyjqW6JT2oYiuM6v0Dn_mdkKkXuukVMADcN-ohDYRQj6r9YN1QsTcmgdZHpu3CzDl8j4WDlIjT71BYs7CRTEc1yUHcafyqr0VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک نتانیاهوی خیال‌باف: اکثریت  مردم ایران، اسرائیل را تحسین می‌کنند
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/678115" target="_blank">📅 18:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
وزیر کشور پاکستان به‌زودی به تهران سفر می‌کند  منابع آگاه پاکستانی:
🔹
وزیر کشور پاکستان قصد دارد ظرف یک یا ۲ روز آینده به ایران سفر کند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/678114" target="_blank">📅 18:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678113">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5466c4816.mp4?token=HNiuoswXUJJlD90funrwe_xhsXeqDhpsWpqf4qdhgRaZsQHe3iT-sPozZ3TZy8jizvwvQtYQ3yOFXjWG7KKMIdcLhs2D7Le61sXwjA0f3TmbM58l2cZMdxnrpnZf7lf4_KjW4FHIwe1VFQuBepLgTHzINeuF6-k2UXMS_V9FgDT7q5TZnmajRZmSoKx2cFDpiTLuvoduiPnP-1fgLHC9-DF8cUF-O3bbp7VLtX6DensZxv_kWg0CaQa_Wnfun6bZQvitVUpWINbEL49A5X1kbX8kQULEOCJzwekHa_H3AiOsLlUvPh8OixJdUpWbZ-ozkBZpTXv8GaB4soQONy7Pdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5466c4816.mp4?token=HNiuoswXUJJlD90funrwe_xhsXeqDhpsWpqf4qdhgRaZsQHe3iT-sPozZ3TZy8jizvwvQtYQ3yOFXjWG7KKMIdcLhs2D7Le61sXwjA0f3TmbM58l2cZMdxnrpnZf7lf4_KjW4FHIwe1VFQuBepLgTHzINeuF6-k2UXMS_V9FgDT7q5TZnmajRZmSoKx2cFDpiTLuvoduiPnP-1fgLHC9-DF8cUF-O3bbp7VLtX6DensZxv_kWg0CaQa_Wnfun6bZQvitVUpWINbEL49A5X1kbX8kQULEOCJzwekHa_H3AiOsLlUvPh8OixJdUpWbZ-ozkBZpTXv8GaB4soQONy7Pdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
السلام ای شاه مظلوم و غریب
السلام ای آیه ی امن یجیب
السلام ای نور چشم مصطفی
السلام ای خامس آل عبا
فرا رسیدن اربعین حسینی تسلیت باد
🏴
🖤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/678113" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678112">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وزارت خارجه پاکستان: وزیر امور خارجه از عراقچی دعوت کرد در کوتاه‌ترین زمان ممکن به پاکستان سفر کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/678112" target="_blank">📅 18:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678111">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بیکاری ۴۵۰ هزار نفر در جنگ تحمیلی سوم و محاصره اقتصادی
🔹
بهار ۱۴۰۵، نرخ مشارکت اقتصادی ۴۰/۷ درصد، تعداد شاغلان ۴۵۰ هزار نفر کاهش، نرخ بیکاری ۹/۱ درصد (رشد ۱/۸ درصدی).
🔹
بیشترین بیکاری: کرمانشاه، خوزستان، بوشهر؛ کمترین بیکاری: خراسان جنوبی، زنجان، مازندران. بیکاری در ۲۱ استان افزایش یافته است./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/678111" target="_blank">📅 18:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678109">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7eWNDaLRqct5BlsA56U6mR7IrXXVX_uEg8D85bFfC4eEGEa3MnL-5VrI1a8ZP9q0Oy0tPI5lB_kl1I7S9wS4rdfObdbWJ7gwLyvvMB77NtI99OHOi-oF49RqJmBXiSdAWyPpOUXGfJEvdzrmf613HmeRt8diYkN0ooAcoybSK3Xq2nlkDfiuKM5fqYZpnhmtUL242Cfqsl-_-fNm73P-mkT-wf7ea3ZDYQLkEUiSwlnZyMYpv6VQqoieQu7gEn4yE6g_BGISN2G7TPtPs_X-aqYZzMSOCzQhXOCAvgmqY_QDVPk4NcvdX9dPxYATQQ0OqB77h_Hn-4Ov9T5a27G3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzG18SaRd-XVh61lrGUL99xqUmJHuJ40mVec33zPJuWf8ncYJeLUmLq7mXd6-WJ5r-3Y3lQ_5edzmqAUUP7HSCNqv4dy6vMzWFTR9UOG111GTmDNycthuB72A_XTkawC5UnxbI2EBPtAw8PRk6wq-PNitJZA9QTcR-wXN88oYjXdjClgrBBnilBgI4E4jggDFzxoxuTrol-s3-aCUj_-rhnTbNa8IiT-FD6LbZJrXQjuOChkVYSvQkcAQkLLTmUPoU4ycw7B87_qOnmfX7TUSpe51lqc-_8P_tkA8btdGoeh-ZP3laYUCVqWzC3miP33hsLFkkw85hxCRp9Ez08f6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر کشور چقدر برای توسعه هوش مصنوعی آماده است؟
بر اساس آمار، دولت آمریکا با امتیاز ۸۸.۳ از ۱۰۰ بیشترین آمادگی را برای توسعه هوش مصنوعی دارد و پس از آن، کشورهای فرانسه و بریتانیا در رتبه‌های بعدی قرار گرفته‌اند.
ایران با امتیاز ۴۸.۴ در رتبه ۷۶ جهان قرار دارد و کشورهای عربستان و امارات پیشتازان منطقه در این زمینه هستند.
نکته قابل توجه این است که ایران در مؤلفه «ظرفیت سیاست‌گذاری» با امتیاز ۸۴.۵ وضعیت مناسبی دارد، اما در بخش «توسعه عملی هوش مصنوعی» امتیاز ۳۷.۶ را به خود اختصاص داده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/678109" target="_blank">📅 18:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678108">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
جدیدترین روش پایین آوردن قیمت نفت: التماس سگ زرد به شرکت‌های نفتی
ترامپ:
🔹
«قیمت‌های نفت مصرفی خود را فوراً پایین بیاورید، همین حالا!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/678108" target="_blank">📅 18:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678107">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اعتراف بی‌سابقه در پخش زنده: ما کشورهای حاشیه خلیج فارس آلت دستیم، اختیاری از خود نداریم!
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/678107" target="_blank">📅 18:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678106">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNnpTC9LfUH3RM60Et8itoRy1DZ62d_qYwyWiS9MrNSsUAaR8FsnnUhrHxjIK7MLr4ktyCFMOyuF7r4NZNIqeWGFyRFk5DktXSEYehkv8WwqQP-VkSaKmnm7zulScE6iZEaSBU9FDiLZhWERYa_EmGM-IrBo_fxo2R9yTuf_BWHHgK6O8iPVVT3RSpKwnEhavkj64pA97b2NpQ_to6ri38KL_O0t4tyoeWWu2oEdvQp9BBAwCAgEewQIcvkzjLvbC4pF-K3PEJqvmC6mbAYdcCn_ZchC8Bj8PAc4NdMP7qo5-DZNwEpbqeBHQWCMlJvkfFz_9jy1AT61kUbKSAUWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا یا دلار؟ کدام یک پس انداز بهتری بوده است؟
برخلاف ارزهای خارجی هر سال به دلایل تورمی داخلی کشورها بخشی از ارزش خود را از دست میدهند، در سمت مقابل به دلیل تغییرات قیمت جهانی طلا میتواند رشد دلاری هم داشته باشد.
در سال های اخیر، صندوق های طلا ابزاری مطمئنی بودند که زیر نظر سازمان بورس فعالیت میکنند و امنیت بالاتری از حفظ دارایی های طلا در خانه دارند. یکی از گزینه های مطمئن، صندوق
#جام_طلا
هست که میتوان به آسانی تنها با چند کلیک آن را خرید و فروش کرد. برای تحقیق و بررسی های بیشتر میتوانید از این لینک استفاده کنید.
خرید آسان طلا</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/678106" target="_blank">📅 18:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678105">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
وزارت خارجه پاکستان: وزیر امور خارجه از عراقچی دعوت کرد در کوتاه‌ترین زمان ممکن به پاکستان سفر کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/678105" target="_blank">📅 18:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678104">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_n5_SGJ2GrkP4QWQrYp7PhwI9Jh9vLDukYpy8rAZaIGRuRD9fhdkyXcHnQUrrblV2xTCr2q5IUYA5O_6NYSssmh_3kapDJzcgE9HdBWadEOLFlnAJIhvKXxSgUHJsHVIJxWKhlfbmdlRu_wmRJkKdV28y-YlJvwunhFi_0jXnuN1b6xIhjid5J26spcAqA-B2E8gDxzunDYjvnBAk7KwNmmaIyYUh8oQzkD6B71sFgU05yXAgfFFP5i0eHu7S4vABsEeqSVY_CUldTVzCDyRyUnP5z4AG1zzQixBnO1hJgK4EF5RAzJ5-0BZ4OhFfgie6VixnQeJkCVxUGvFJSGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
♦️
بالاخره اسرائیل نابود می‌شود!
تصویری دیده نشده از رهبر آزادیخواهان جهان، حضرت آیت‌الله سیدمجتبی خامنه‌ای
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/678104" target="_blank">📅 18:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678103">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFUt9yZAd6CDy0siPdLTNH3Biaa9jYU4bopBOhent4m3J2TKq04EgQfOrG_y8dw5BN0LVZWZoGYEU-76D_0uX8BQQHYOGGMPUI2IlPRK5BpAXR6lpeIR-_dcv3UDx_kJDxuHA56ah0VTgH0d_dAno9yevtXIgA6WQjMk32AnlgBHsskigwBrGyomyZKRwcpKqDZ373UdoVj5U3nLp16h3QON5sV1avRDno4IFrVjdasx7x5xjXDcpLY8RUdRLwbwlNJyBmf4uLsiFAOBRqXOFbqHrQrADLAA_Lnszo0Yr0CuMSPN2HtjvlENF4RviolGdZl0Jd9KgPE2M2-sKxK37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک تایمز:
ر
ئیس‌جمهور آمریکا صرفاً در حال سبک‌سنگین کردن و بررسی گزینه‌هایی است که هیچ‌یک برای او مطلوب و ایده‌آل نیستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/678103" target="_blank">📅 18:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678102">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPfaKJ3h6hlx6a83ZezhNOLEiRCZkM3rrJj8vbx36IRrD3XnjcNjC6eerw2qxTm2cGRSEWu3UGDTuQPgViEkxVUNxjdw-dUkB3MBEK9xLTNJTDQOJyEYD_5ZmcR0B7mgMx8cTZ9SnjwqUiULGvrFrtFCt03hYzSY2ZaULs4nNs4rArJs8S1G1yRW7B9XURF6nIS5gU_pMmt_dkm3N8Z7x_hhyplEfgG5xHubVpmKgSAFn34KcdY211xpA3xcHb9XnXUUKVMNm_I-MfXHb9bBYcg7x0MuF4q9tMCILMOzlBU1LyKyjV34EtcOsVz6puIyORoSSCkqGL9Z7nobPY1d3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانروایی که از دل آشوب برخاست؛ نادرشاه افشار
🔹
نادرشاه یکی از برجسته‌ترین فرماندهان تاریخ ایران بود؛ مردی که با قدرت نظامی، تدبیر و لشکرکشی‌های گسترده، بخش بزرگی از سرزمین‌های ازدست‌رفته ایران را بازپس گرفت و دودمان افشاریه را بنیان گذاشت.  رویدادهای…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/678102" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678101">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/678101" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678100">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
انفجار کپسول گاز در دبی با ۱ کشته و ۵ زخمی به همراه داشت
🔹
ادعای سفیر آمریکا در ناتو: در حال حاضر ما دیپلماسی و مذاکره را انتخاب می‌کنیم
🔹
سخنگوی وزارت امور خارجه سوئیس: با ایران و آمریکا در خصوص مذاکرات احتمالی در تماسیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/678100" target="_blank">📅 17:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678099">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده شدن صدای انفجار در امارات متحده عربی خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/678099" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678098">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75305259.mp4?token=DQO8f6m02wxeTjc-dS63k-HN1_Z2sd3dzdvTa4YRwCDdW6jzFROM-brrFa_Obqwhn0lyvo8Yra8yms2QmLS4tBxPoKqEDehvsrElqveejCiRWrlozWQtXm2spAcKnTcvZPTHlBtq2YlnBZQsMwdnzkd45cHxqeGkMgKXTRYPp4KXiVQY8Y5gR67nBx5XDrAc9KE8CQkRLjWqyjkQUBXP3kr76aGs8zZAeD0eBfi4XIUQlMGJXssz6Gjq2BN225dCqlLs0ald3-VxkuhnHSfU25Oh-6Cm-i2QaeFpw90SNCHThDU9of72SfMhR6OmN1ZNTljZFe7cYPNJZyrOsTgcuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75305259.mp4?token=DQO8f6m02wxeTjc-dS63k-HN1_Z2sd3dzdvTa4YRwCDdW6jzFROM-brrFa_Obqwhn0lyvo8Yra8yms2QmLS4tBxPoKqEDehvsrElqveejCiRWrlozWQtXm2spAcKnTcvZPTHlBtq2YlnBZQsMwdnzkd45cHxqeGkMgKXTRYPp4KXiVQY8Y5gR67nBx5XDrAc9KE8CQkRLjWqyjkQUBXP3kr76aGs8zZAeD0eBfi4XIUQlMGJXssz6Gjq2BN225dCqlLs0ald3-VxkuhnHSfU25Oh-6Cm-i2QaeFpw90SNCHThDU9of72SfMhR6OmN1ZNTljZFe7cYPNJZyrOsTgcuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
هر آقایی یکی از این جاروها توی ماشینش نیاز داره
👨‍🔧
🎥
برای دیدن کاراییش ویدیو رو حتما ببین
❗️
✅
سه روز ضمانت بازگشت
🏠
پرداخت درب منزل
تعداد محدود! همین الان کلیک کن روی لینک زیر،
تخفیف ویژه
رو دریافت کن
👇
khabarfouritel.affdn.com/lead/44273
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/678098" target="_blank">📅 17:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678097">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0geMGIEh1G8ETTKnAArdBkzTjAuMMINHswIjg7QICS2chY1xdO4Cu2W2sfAk57R2F2a-8akUSj899HJnzr_BhnulF1PqhHAt8ZltNV1-KdMkXtUCKFIziVC6LuXqhDKZwB-9iUfO2477YN7ALrZnBJ0zjuPGgOv3LIKsnfe5T0bMKmu_UpfizmhZ88r70QqQmm_0wvB5CEUeLd_BiVNPtCdRHZwbTgVTFXzHstXvcdomO-g_w-mxB-s3y9hGViQ--FvITx27YDH_DVTysLuZlfbO6wyiaNaQljylUwMrlIWLLsEPgnJ1d3qh0gwjubStP8IeiwMCp_lvE_Yg_lzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت مژده لواسانی از اولین زیارت اربعین مادران داغدیده میناب؛ روایتی از دل‌هایی که سوخت
🔹
مژده لواسانی از روایت مستندی با حضور خانواده‌های شهدای جنگ رمضان خبر داد که اولین زیارت و اربعین آنها پس از شهادت فرزندانشان محسوب می‌شد.
🔹
لواسانی درباره روایت این مستند عنوان کرد: من هر ساله در اربعین حضور دارم و معمولا برنامه‌ای برای اجرا به من پیشنهاد می‌شود که همیشه استقبال کرده ام. اما امسال به دلیل ماهیت گفتگومحور و متفاوت این مستند، اتفاق بسیار ویژه ای برایم بود. به نظرم الگوهای تکراری مانند حضور چهره‌ها و مهمانان معروف کلیشه‌ای شده است، اما این فضا همچنان بکر و تازه بود و خود من نیز از آن تأثیر عمیقی گرفتم.
🔹
مستند راویان پرچم سرخ به زودی از شبکه یک پخش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/678097" target="_blank">📅 17:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678096">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک مطلع: نماینده ارشد شورای صلح و مشاور این شورا امروز با نتانیاهو دیدار کرده و به او ابلاغ کردند که باید حملات به غزه متوقف شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/678096" target="_blank">📅 17:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678095">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069f15d0bb.mp4?token=Ska2EqK5tWie-3eSgkGj6gXusKIgFg3zNdig7J4HaXS2tu10XG-IEBC-YSUDylrRaKbwnKTFXIR7fhc_dKcJKeXsANPDqqNZWEm8VNUO6f1tPGnqIJqsKO3EP3AZW61r5hkeSirHOnBkos712KXW-1-W3qiA6r8q2_BB_o-2odrqZHXvIcIE5DNtk7qpnSNzuv2BW4vB1tN5kEUKmb3EOC7B76xka87SpOV5b--5NOQlLaYGtfc5LnH6SXq2c-X0WtWbDDHHbkg4qv2ysNAqagDV1JvYN62i7VWQ_omOePXqU7uwXp4MX8EMZuU5t9K61AbBphj3J6wwgZ0VZQN8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069f15d0bb.mp4?token=Ska2EqK5tWie-3eSgkGj6gXusKIgFg3zNdig7J4HaXS2tu10XG-IEBC-YSUDylrRaKbwnKTFXIR7fhc_dKcJKeXsANPDqqNZWEm8VNUO6f1tPGnqIJqsKO3EP3AZW61r5hkeSirHOnBkos712KXW-1-W3qiA6r8q2_BB_o-2odrqZHXvIcIE5DNtk7qpnSNzuv2BW4vB1tN5kEUKmb3EOC7B76xka87SpOV5b--5NOQlLaYGtfc5LnH6SXq2c-X0WtWbDDHHbkg4qv2ysNAqagDV1JvYN62i7VWQ_omOePXqU7uwXp4MX8EMZuU5t9K61AbBphj3J6wwgZ0VZQN8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عاشقانه‌ای از جنس فلز و سیلیکون؛ اولین ازدواج ربات‌ها در دبی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/678095" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678094">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سی‌ان‌ان: سنتکام برای مقابله با مقاومت ایران ایده کم آورد
🔹
شبکه سی‌ان‌ان به نقل از منابع آگاه گزارش داد فرماندهی مرکزی نیروهای تروریستی آمریکا در یک ایمیل به تحلیلگران نظامی از آن‌ها خواسته است برای آنچه «مقابله خلاقانه و غیرمتعارف» با ایران خوانده شده است، راهکار ارائه دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/678094" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678093">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7hecKzL5HZyJblfWMFNcjCKeqEuQvQCRgUXh2zb4lYClIvR0QPbPfdWCR1zbN2VBvOcp9xJnNXVgbfPE3HEyPndYktZhcAaSRicIgiPa65Nl6Pgj2zQNHrfQay3WSgUp5vNVRr6FgeFiweoDmNMqKUzw1_kS40MUeoLgXhnOc9kOia-TsFSBBnh_TECaGgA3sQGAif21vjR2IMfbch2bg2hv9XqRvr1zb5zeAUMXf8M1or7abBxlJ4LSmhcl_uKETGXS2W7SRo0iv21HPGhJbWTN1JqpXaMydiSxHA5yy_LwqrIJXi5tFpjgEIyeh1EqZHP3Jg5KXoPKR9YF855VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست هزینه‌های ساختمان که هر مالک و مستاجری باید بدانند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/678093" target="_blank">📅 17:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678092">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تیزر قسمت بیستم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای علی لعل یوسف که با خوردن یک آبمیوه مسموم، روح از جسم ایشان جدا شده و توسط یک دست قدرتمند آمیخته با خشم و مهربانی به سمت بالا می‌رود و در آنجا آیه‌های قرآن را به تکرار شنیده و اینکه مهم‌ترین اصل آفرینش افراد در همه ادیان الهی، انسان بودن و زندگی انسانی قابل قبول درگاه خداوند است را درک کرده و بخاطر کارهای نیک و بد دنیوی‌اش پاسخگو میشود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: علی لعل یوسف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/678092" target="_blank">📅 17:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678091">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
نمایش بنر منقش به ابرمرد شهید تاریخ در بین‌الحرمین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/678091" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678090">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp8iE47rDGKBxbkD9LRFbamWUs9bo0k430iucY1T1IjKw1OyYpjUtec6lkaQIPAxX27A2jQGXtSvZd9n8FiQDs0KlEVefYU6b_VUmKqz_gEejYeM_I3ZpHsz9_SIGOF-P8MccZOLDjiDJVihThS69-bZJuhvKN86i-TLiFWN6IcGAGr7yh3i6MM9uHa0wY6Wtn5kJS8qumzn7YpzCrSn5stKYIebTqb_Qd9jcElrWlVLIJux6GbbJhbSJsXWxc9xHsxmHkrD16bPTR9hAWEiwL0xVahQ9oBk3BsIlLeL2YD1KQqhCDot4uvtaCm5FJwU-Rj6R6dVJSsfpNYynY7Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون شوراها در مجلس: خدمات شهرداری تهران در اربعین رضایت‌بخش بود
🔹
سخنگوی کمیسیون امور داخلی کشور و شوراها در مجلس در ارزیابی اقدامات شهرداری تهران، بیان کرد: شهرداری تهران در مراسم‌های مختلف، از جمله تشییع پیکر رهبر انقلاب، عملکرد بسیار خوبی داشت که جای تقدیر و تشکر از همه کارکنان این مجموعه دارد. واقعاً خدمات ارائه‌شده بی‌نظیر بود و آن چیزی که نیاز بود، تا حد امکان انجام شد.
🔹
بیاتی درباره نقش شهرداری تهران در خنثی‌سازی جنگ رسانه‌ای دشمن نیز گفت: دشمن در کنار جنگ نظامی، جنگ رسانه‌ای را نیز به راه انداخته است و موفقیت‌هایی را که ندارند، بزرگ‌نمایی می‌کنند. البته در میدان عمل دیده می‌شود که شهرداری و دیگر مدیران حکومتی ما به بهترین شکل در حال تلاش و کار هستند.
🔹
وی همچنین عملکرد شهرداری تهران در خدمات‌رسانی، برگزاری مراسم‌ها و فعالیت‌های فرهنگی مرتبط با اربعین را مثبت ارزیابی کرد و از تلاش کارکنان این مجموعه قدردانی کرد./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/678090" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678089">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8HDegnBjK6xrw1ChuBygfOrZVPIYZ0LZoeFrTUcsBRT88YCPGdgO2QoYJvaLpBO-OedoZTrr8dAjVk6HASJcPiwr5rUHmyjBZrlgOrFfzkzzw8D7lZYt0LHfj4klT8fPwpTIzDymKL1SiqWr0B4yE9Gw7dPuJIqshCStOwp3mHWhVGuvVbBCmaj62tHeUrx8WYI4CvydPEFJO2QLNfPaHkWQ4vb7ux1-FAE8_ibmx9Be0-qllJMX0ozPmQsT_mKrdAc4mKHdbFVWtslSjE8SRdSt0BH9XwEt72kYv95l0-CwCfaAZS26pDdtMU60tvBpJ-xme8yE784Ni9FI-rcmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲ عامل موساد اعدام شدند
🔹
امید بهزاد و پوریا صفوت، به جرم همکاری اطلاعاتی با رژیم صهیونیستی و ارسال مختصات و اطلاعات مراکز نظامی و امنیتی، بامداد امروز پس از طی مراحل قانونی و تأیید دیوان عالی کشور اعدام شدند.
🔹
این افراد در جریان جنگ رمضان و جنگ ۱۲ روزه…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/678089" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678088">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
به‌صدا درآمدن آژیرهای خطر در سفارت آمریکا واقع در منطقه سبز بغداد در مرکز عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/678088" target="_blank">📅 17:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678087">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHVPcwFcHQFW0HikVTqm8D70WbYW8PcXK8TuEeRUsHNmJmYyQ_kP2PdlXOWtIbN4PibWD2rKl45P8w9OzvPT8gWojzZMJ7_4zmv-3KvgHDtIGaReiQOGNaoaABDAxlSrXrno1g3e3R_WYpC_Lmx_yndWbqqJ0MRXdhciRIsNM86GNTbm8JRkDWaFoKSVR_A6qGkMCO8w9YTo4HPUNjLvajo4XNc4_r6-wDXPgnrLrIUGxdYc67EA8lcdlqDuOkblXqTN2WKdUCqH-q5Rup86kNIFKfdo3rvrQ_EWtAvFZmLZf5GZSQUP_JsiC-oWAcesf41fWZFW1xZJjOVk1OL8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هاآرتص: مشکل اصلی کاهش ذخایر موشک‌های رهگیر پدافندی است که سریع‌تر از تولید جایگزین می‌شوند. ادامه جنگ با ایران برای آمریکا و اسرائیل پرهزینه‌تر می‌شود و ترامپ این هزینه را فهمیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/678087" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678086">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای سنتکام: نیروهایمان هوشیار و آماده هر مأموریتی‌اند و از کشتی‌های تجاری مایل به عبور از تنگه هرمز پشتیبانی می‌کنیم؛ از مه تاکنون به عبور هزار کشتی کمک کرده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/678086" target="_blank">📅 17:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678085">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=ogLrwhtuEtVunXwTHf2CoxFPmxAhk1Wu7nWb7eLPWX8pC62hXjJIuuaIGhMdhoXVztfYneLS8yviGxioUy-MhOqBq8wtJnkaNwmVKp87SPbXGlAgco5yPnSsSvbk-JfnMURCTA9rufqJjCDOOKfqcOJAZIIYHuXHuRYq4orMlbr9LTaKNaPO6idfHRhkkLN4vofeJynSW1b3BHEPEkn2_r6wnRy7AJccyBSrNAmztcF1U5YAPl9kn9GGf15r7TO8ZR9HFN3bMErSVKyl2a1rJwc3YDNBt4Cf5VK9fC4XsEPubFZ7EIMt4Etz2QDK2ygkSQZi3akKQw3DZwKR-2kzlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=ogLrwhtuEtVunXwTHf2CoxFPmxAhk1Wu7nWb7eLPWX8pC62hXjJIuuaIGhMdhoXVztfYneLS8yviGxioUy-MhOqBq8wtJnkaNwmVKp87SPbXGlAgco5yPnSsSvbk-JfnMURCTA9rufqJjCDOOKfqcOJAZIIYHuXHuRYq4orMlbr9LTaKNaPO6idfHRhkkLN4vofeJynSW1b3BHEPEkn2_r6wnRy7AJccyBSrNAmztcF1U5YAPl9kn9GGf15r7TO8ZR9HFN3bMErSVKyl2a1rJwc3YDNBt4Cf5VK9fC4XsEPubFZ7EIMt4Etz2QDK2ygkSQZi3akKQw3DZwKR-2kzlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام شهاب مرادی در مستند راویان پرچم‌های سرخ: ایستادگی مقابل ظلم و دفاع از عزت مسلمانان، مسیر یاران امام حسین(ع) است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/678085" target="_blank">📅 17:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678084">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlxUoRSm0Uc8JxLABeXvzExPCg-QUDyX7LDXVC1OlFBofFI-KX8VANx_rOunsVJA6KtciUn2oJSlE-Ns-8KtyMakNa7je84jm9Y5lqlIRubBPtoeRKHgPX0giLxpYAhw4mrnn_FlP8y31jGQw1awSZzSq7gXGY2UamyQzNpk04QCEQZ3SHMW9N5wSw_CTyt0xE-ewOjFJ3cStRVN7IX2r3cfzvxoJk4lOY_zSH2wDDCmxTRG4hL21l4YhIhO17aQIP3T5UJemfvnVJYlzcT9rfrDZ9utgHnJs6J0C8r7jf5eUeCAqukOu1UaOTQUpDa9J-UKzz4JZnWnKC3TGF9X9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صفر تا صد ساخت پیج میلیونی اینستاگرام با هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/678084" target="_blank">📅 17:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678083">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
۶ نفتکش بزرگ سعودی در پی محاصره دریایی یمن، مسیر خود را تغییر داده و به‌جای عبور از باب‌المندب، مسیر جنوب قاره آفریقا را در پیش گرفتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/678083" target="_blank">📅 17:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678082">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
در حال حاضر هیچ‌گونه مذاکره‌ای میان ایران و آمریکا وجود ندارد و مذاکرات درباره مسیر عبور از تنگه هرمز صرفا با سلطنت عمان انجام شده است
🔹
همچنین ایالات متحده امتیازاتی داده که از جمله آن، پذیرش بسته شدن مسیر جنوبی بوده است.
🔹
ایران در شرایط کنونی تأکید دارد تا زمانی که جنگ ادامه داشته باشد، تنگه هرمز را باز نخواهد کرد.
🔹
گفتنی است اظهارات دونالد ترامپ رئیس‌جمهور آمریکا درباره وضعیت تنگه هرمز با واقعیت مطابقت ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/678082" target="_blank">📅 16:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678081">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
بقایی: پاکستان میانجی‌گر ایران و آمریکا است/ میانجی‌گر جدیدی از جمله چین اضافه نشده  سخنگوی وزارت امور خارجه:
🔹
پاکستان میانجی‌گر مباحث مرتبط با ایران و آمریکا است. قطر هم در مواردی که لازم باشد کمک می‌کند.
🔹
ما با چین رابطه‌ای بسیار دوستانه و همکاری‌ای نزدیک…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/678081" target="_blank">📅 16:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678080">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaXu1ZRt7McGADIs0w96CCtYKvXmjG9q6_kdDyjATIWEOo83haI3XKXXl855ti3rj6vXkkiRvkFmp_43BP7QY0_Wifl8im4gPQ_7sZ5jlirbHHv2HlQzYq3caQCObChN5-O-banLq7Pqa7ceHjJZn-LENEovHat7xn8gP5i6HHLoTGGcf50ZDV5Xg8_57YGJ8-g-28q9o3gv-C0zeADlGIfn67m-csByx-H8g3Yu5fN9d33Bgkb2YxEP_9ar-5wFvsd0DbyJa3edd_EP_fBcNWcGJv7j4aMdEczzEVk9TSnN1Lv9eJ0f7mmCQtQRM-bH79Lbk-4IDLfgQ6gigywCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از خفیف تا خطرناک؛ کبد چرب گرید ۱، ۲ و ۳ چه فرقی با هم دارن؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/678080" target="_blank">📅 16:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678079">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkRsxp94bNY6JU8X9MySi9Rsd8cHrFqPkXgMj_U4CUYK9NzMOrw3Vl2F_peXA6Hrod_kpeJecW_uCxabsQKejjRiS5IeW3wi1AyrlRv4mOdBQR_rgTVex-YpKqJzJfLjdr64WvnYFjfEsvu-4Yi0SE-Crcz6PD7MHEHMEmQcBnS5FiJpkcZ1vjIrh4mRYcRfyffG4if3IAn5ReF3SLUxUCIYhUSQDVskYT0gkrLY5pCqTlGZAFqa88XGsMUg-m0yXezeIfrDXuOqKNxXhgdPvlGPnT9FX4POm1IGwjZHAWb_AeTkn4cwVUMLBfU623uJNhEXDGR9nmSM7oLEeAxkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
نمونه واقعی کاهش درصد چربی بدن با تزریق زیکورپا
روند ۱۷ هفته‌ای درمان آقای ۴۳ساله، در کلینیک ایرانیان
⏲️
در درمان چاقی، مهمه کاهش وزن بیشتر از چربی‌ اضافی بدن باشه و عضلات، تا حدامکان حفظ بشن.
این نمودار، نمونه‌ واقعی روند کاهش چربی مراجعه‌کننده عزیز با
آمپول لاغری زیکورپا
هست.
در کلینیک ایرانیان، پزشک بعد از آنالیز بدن، درمان با
زیکورپای عبیدی
را شروع و روند درمان را پایش می‌کند.
👨‍⚕️
برای دریافت
مشاوره رایگان پزشکی
، اقدام کنید.
کلینیک ایرانیان
مجهزترین کلینیک زیبایی و لاغری ایران و خاورمیانه</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/678079" target="_blank">📅 16:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678076">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
جان مرشایمر: ترامپ دچار سردرگمی و دست‌وپا زدن بی‌نتیجه شده
جان مرشایمر، دانشمند علوم سیاسی
:
🔹
ضربه اصلی و مهلک ما به ایران از ۲۸ فوریه تا ۸ آوریل به طول انجامید و با شکست مواجه شد
🔹
ایران برنده جنگ شده اما ترامپ از پذیرش این واقعیت سر باز می‌زند و در وضعیت فاجعه‌باری گرفتار شده/او هیچ راهبرد نظامی معقولی ندارد و فاقد هرگونه دکترین پیروزی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/678076" target="_blank">📅 16:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678075">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: در آستانۀ سومین سال ریاست‌جمهوری، گفت‌وگوی پزشکیان با مردم به‌زودی پخش خواهد شد.
🔹
توانیر: از هفته جاری در تمامی شهرک‌های صنعتی کشور محدودیت یک‌روزه برق اعمال می‌شود.
🔹
نتایج آزمون‌های ورودی سمپاد و نمونه دولتی هفته آینده منتشر می‌شود.
🔹
رئیس ستاد مرکزی اربعین: یک میلیون و ۱۰۰ هزار زائر ایرانی همچنان در عراق هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/678075" target="_blank">📅 16:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678074">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbnOoze-MqooJBEJk_FluCkjHppG_x00Rd-JDgrPigDImzGi1Aawi6hLG0o0Oy_ojFDO3AiEvsSFpXVKbJ_nwxUwqRiR-HejWUa6cJ7mWUQ42HA42FWlc1S_koIAiUSkhKXs-be-R5BCxSV8TofOANSpzksbvH0CsB8_Dp4YJuyMgmvLRj0avuV84C4-EZXGt8lOHnAerxt0PfOuzm_lQcw2g8VwqYqdiuXwVyr07mQSkyBCXjq2ZGfRyHEA9d2BoFRDrHVKkidfT3Q5X2ovrLlu4pcGCHzYGT5pESwA2dYeVdhGUTQN9Mft5ywxUh5XJfyU5UGf2V2dQfzca2M_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی نقاشی‌های گمشده را پیدا می‌کند
🔹
یک چت‌بات هوش مصنوعی برای ردیابی آثار هنری غارت‌شده توسط نازی‌ها توسعه یافته است.
🔹
نازی‌ها بین سال‌های ۱۹۳۳ تا ۱۹۴۵ حدود ۶۵۰ هزار اثر هنری را سرقت یا به فروش اجباری وادار کردند.
🔹
محققان دانشگاه سانتا کلارا امیدوارند با این ابزار به شناسایی و بازگرداندن حدود ۱۰۰ هزار اثر مفقود کمک کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/678074" target="_blank">📅 16:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678073">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پزشکیان: ایران خواهان گسترش تنش و ناامنی در منطقه نیست
رئیس‌جمهور:
🔹
ایران خواهان گسترش تنش و ناامنی در منطقه نیست، اما در دفاع از امنیت، منافع ملی و تمامیت ارضی کشور با تمام توان عمل خواهد کرد.
🔹
نگاه دولت به اداره کشور، نگاهی سلامت‌محور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/678073" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678072">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0607e9ae8.mp4?token=bOWBZZX30Oa1mu3c0vkBcffcu4X4zucDXfkO20f4_EwVQLCSzGO5sBPXWvuLfXqkcL3tqTM6KRXJ6S9Sm-jhbpqf_wfL1w-HOFVSdCh2xvEbGmXqL5W_w2BWvHbHbje2HfMs3MUpfEGZmSTsovHZ9603ZrcsACYDm1uU2sUnkTqeteUiVVpaz9PbWStO135dvcuQ88nRb97mxcMsG2MjfMafQw4Pghy3izysyuRQdD4qxoOKVwo-nqZn9IopJT501ocDOuxyJZQoyUUs8-RLq4-2HdgRKhnf1qnJGmLaJMT2Wx2DHvzWWrz5_mAkPBgP3CCSQ2-4jp3NFVxl4bLXGE1C9CuF-n3EB4mbJ-W593A-yWEL0u4kiQPAZMi74yGQkxVWbg5KTycVkgA71i35JBMWWFhyB0XpLtsOSBBczCKI2VgJ_RBYX9hb1eODSarBdZKwVEmjZeXicJ7SZDi9SgCFb_yLW0t6kiKt3SvFV1HVA_VcshR7_ndl-rbF98qKmtgiZCcMaOIvu7AD1r8mYG91g3yG6YLrbrFXZhuFuYxP2iNEOTcDQ7mRPh_lymNoMG7L17eCUkEsnN5RidhmySefRmd3Hqnyyjwcj088af6xAakVRSnovzBa1rUqTJN3k2-P-uPAJahkOWtcyQIvlDVsWUcu8cs239Kx5cvCoNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0607e9ae8.mp4?token=bOWBZZX30Oa1mu3c0vkBcffcu4X4zucDXfkO20f4_EwVQLCSzGO5sBPXWvuLfXqkcL3tqTM6KRXJ6S9Sm-jhbpqf_wfL1w-HOFVSdCh2xvEbGmXqL5W_w2BWvHbHbje2HfMs3MUpfEGZmSTsovHZ9603ZrcsACYDm1uU2sUnkTqeteUiVVpaz9PbWStO135dvcuQ88nRb97mxcMsG2MjfMafQw4Pghy3izysyuRQdD4qxoOKVwo-nqZn9IopJT501ocDOuxyJZQoyUUs8-RLq4-2HdgRKhnf1qnJGmLaJMT2Wx2DHvzWWrz5_mAkPBgP3CCSQ2-4jp3NFVxl4bLXGE1C9CuF-n3EB4mbJ-W593A-yWEL0u4kiQPAZMi74yGQkxVWbg5KTycVkgA71i35JBMWWFhyB0XpLtsOSBBczCKI2VgJ_RBYX9hb1eODSarBdZKwVEmjZeXicJ7SZDi9SgCFb_yLW0t6kiKt3SvFV1HVA_VcshR7_ndl-rbF98qKmtgiZCcMaOIvu7AD1r8mYG91g3yG6YLrbrFXZhuFuYxP2iNEOTcDQ7mRPh_lymNoMG7L17eCUkEsnN5RidhmySefRmd3Hqnyyjwcj088af6xAakVRSnovzBa1rUqTJN3k2-P-uPAJahkOWtcyQIvlDVsWUcu8cs239Kx5cvCoNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی کوتاه اما ماندگار از پیوند اربعین با یاد شهیدانی که امنیت و عزت این سرزمین را با خون خود رقم زدند؛ یادی که در مسیر کربلا هرگز فراموش نخواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/678072" target="_blank">📅 16:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678071">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVO_oXiVO19dbwBruR2Cn3dIWhObePzHLF7RGT0vrw3OetMZtg_oykr4Ab6eM4Rgp6B28V6C5un8RK0VJpmCWnruTVjF260Eh-efJC32aGBafsdVuf_ItfB8hRfMALx8nMlEEDRdZfA7ai8m7QLWBEaPmn-UMKRhr2U2Yi7xvyPqDxKAK8RX-9Se2mvVKa8ou_rV_uC2x5mXvK04ZqVSbC_7RPqigbqrL66tVdH4BpROsFkIKfAZMwzxMEj49kciRvnvgvD_OvR6sdU7e5HdWcG7akL7479fYWo9FZEkIJhTyOm5mjOA0WyDDu4ykfl-bs_tKyUEk-tHYtdGgNAF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام الگوهای مصرف نیازمند فرهنگ‌سازی‌اند؟
🔸
در این نظرسنجی بیش از ۳۲ هزار نفر شرکت کردند که سهم روبیکا ۵۶، تلگرام ۱۵ و بله حدود ۲۹ درصد بوده است.
🔸
به عقیده ۳۵٪ شرکت‌کنندگان، الگوی مصرف انرژی و از نظر ۱۶٪ نیز الگوی استفاده از رسانه و شبکه‌های اجتماعی در ایران نیاز به اصلاح و فرهنگ‌سازی دارد.
🔸
اصلاح الگوی مصرف و تقویت فرهنگ استفاده صحیح از منابع، یکی از مهم‌ترین پیش‌نیازهای توسعه پایدار و افزایش بهره‌وری در کشور است.
@amarfact</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/678071" target="_blank">📅 16:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678070">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
چیپ مغزی ایلان ماسک، ویلچر را با فکر حرکت می‌دهد
🔹
شرکت Neuralink ایلان ماسک قابلیت جدیدی رو به چیپ مغزیش اضافه کرده که به افراد دارای معلولیت حرکتی اجازه میده فقط با استفاده از سیگنال‌های مغزشون، ویلچر برقی رو کنترل و هدایت کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/678070" target="_blank">📅 16:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678069">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4f484d0e6.mp4?token=Mb79eRDeNRoPOdRUqipQzC8UlJgXR5K_Ts-mIjV7HhUPBNKgS2A1lMKCSeGrgnGp9vvScEdBheZ2uZDULn_ZWSpDOTCmr9hNCmbay0FiyQ7pRxZ5h_n-3ZKqP48wNOaX91eYXSOZsYOcPUhaqn2JuZZRsdkbMj5U2dGkukRz5Zxh3KXpyaUSiz5LduNnJ9MhCNvgr3TNwiB4lBmXq79Qe8Ge5LrPEg1HoJpJtV24us40550g-GlEiAg9dj05hmt7mOzjTguhoq7WACdPJhc8ta0xlHUY50-HUyUUvidiwiFbtyGiaY3iyKbSeukyH5PTOs5aqFhOZHiskE7ImXq0JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4f484d0e6.mp4?token=Mb79eRDeNRoPOdRUqipQzC8UlJgXR5K_Ts-mIjV7HhUPBNKgS2A1lMKCSeGrgnGp9vvScEdBheZ2uZDULn_ZWSpDOTCmr9hNCmbay0FiyQ7pRxZ5h_n-3ZKqP48wNOaX91eYXSOZsYOcPUhaqn2JuZZRsdkbMj5U2dGkukRz5Zxh3KXpyaUSiz5LduNnJ9MhCNvgr3TNwiB4lBmXq79Qe8Ge5LrPEg1HoJpJtV24us40550g-GlEiAg9dj05hmt7mOzjTguhoq7WACdPJhc8ta0xlHUY50-HUyUUvidiwiFbtyGiaY3iyKbSeukyH5PTOs5aqFhOZHiskE7ImXq0JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزایای سرمایه‌گذاری در املاک دیجیتال در یک نگاه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/678069" target="_blank">📅 16:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678068">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxePGyUODxay-RS4XJ6wYAeGyu7a6WHdNNPZAcfgkQWhYRAaBUrXbbj-rUK0uo1eUSvNDKAm-3ZmP6AJSxF1xEDq2MbY0dwFk8ZAGDqS0ryZlcop9DsihGn75FoflQHSXAbfT4ic5nw8J8NMyH0f-L5QExj1pnVr3ZDJqA64a0Ni-J0Xe3PDVPpvgtF_IUUY2FaZFjJu1iVNhh4g8vtm00nUkVtjCUcEoL6mMUzCZvQC3oYjDbyPAqOrzcwzdlAyHycftMdl958kq-jFj2cw9ICpegyr7Jyy683Bg-eCVQksUk0x5-k2LuI61K9UZaTuzXYb_9Xtp4xCILJZK0IlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاسبی جدید با سهمیه اقامت برای واردات خودرو
🔹
با مجاز شدن واردات خودرو با ارز شخصی برای ایرانیان مقیم خارج، بازار خریدوفروش «سهمیه اقامت» داغ شده است.
🔹
قیمت این سهمیه‌ها از حدود ۲.۵ تا ۸ میلیارد تومان اعلام می‌شود. /خودرو یک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/678068" target="_blank">📅 15:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678067">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWdKWE6hm7OKtEOIsCk9JJ2o3RIzMCC4u6i3w8CWO7ePYfzkr-A1rz4Ge3A0Hmo9agpCDqoceGA1m_jMyebv3Bm1S3OK2A7xmGHSYVQY8r__1kzy3rf7WcOozhd5L6mXKjKQF9_sUemBGawX6ttohF_5O2MVugnEkru_6DqlJEhruf3al7gHxmqqwFURU0MvKmWvP4TvEjuli3OzQAqLcAYO7qh0vXlp_clzPaBekRzlwjatSrYljRvSehZyPAo6ATA5J3oWJybOwKniFEUHJG2GxJcjcp_0k9xwiS7Dqg09F3RB6y33ED_QvcjmHLx63CLzeNkqgATsr2rn3veiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو کمیسیون صنایع و معادن مجلس: قاچاقچیان برنده اصلی ممنوعیت واردات لوازم خانگی هستند
🔹
مصطفی پوردهقان، عضو کمیسیون صنایع و معادن مجلس، با انتقاد از تداوم ممنوعیت واردات برخی اقلام لوازم خانگی، این سیاست را عامل گسترش قاچاق، افزایش قیمت‌ها، شکل‌گیری رانت و تضییع حقوق مصرف‌کنندگان دانست و گفت:
🔹
ممنوعیت واردات، قاچاقچیان را به برندگان اصلی بازار لوازم خانگی تبدیل کرده است.
🔹
مصرف‌کنندگان مجبورند کالاهای باکیفیت را با قیمت‌های چندبرابری و از مسیرهای غیررسمی تهیه کنند.
🔹
ممنوعیت واردات، نه‌تنها به تولید داخلی کمک نکرده، بلکه بازارهای زیرزمینی و قاچاق را تقویت کرده است. درآمدهای گمرکی هم به جای خزانه دولت، به جیب قاچاقچیان می‌رود.
🔹
رقابت، مهم‌ترین عامل کاهش قیمت و افزایش کیفیت محصولات است و تولیدکننده داخلی باید با کیفیت و نوآوری رقابت کند، نه با انحصار.
🔹
تجربه بازار خودرو نشان می‌دهد، سیاست‌های انحصاری، هزینه‌های سنگینی را به مردم تحمیل کرده ااست.
🔹
دولت با همراهی مجلس باید هرچه سریع‌تر ممنوعیت واردات را بازنگری کرده و زمینه حذف رانت و مقابله با قاچاق را فراهم کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/678067" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678066">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/647dbbcc5b.mp4?token=e4xYvcXXsdLfrslCm_tMdwRgx-pmoVZpQkw-j1o7Deafe8Gf74MphIIs80H-c8F6C7y4AljxGmuMsZ-qLar3N_LKlVRhm2O7ESJ7saXULf0okI0MZiWWnpsb_FyIUtIHK0l4E4vkMZ6zvHMjtyvocRfzjE_w7MjTbcUo5RRj1xfOMypBDdRIBbCqD6XUueaRxj3Hiuhh0KsCwcT2h4yN5p3K48NWVOiRd7ZmKn-advB1yf3rCc-BW5P1cdPPzr3zbe60MDa88lkVe4KgNtTLOSxjazA2v-7agIYOIo20wUms6rxyfDgTxt3HcEVwAnroJV543kkuQzRNYtZJ0pvfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/647dbbcc5b.mp4?token=e4xYvcXXsdLfrslCm_tMdwRgx-pmoVZpQkw-j1o7Deafe8Gf74MphIIs80H-c8F6C7y4AljxGmuMsZ-qLar3N_LKlVRhm2O7ESJ7saXULf0okI0MZiWWnpsb_FyIUtIHK0l4E4vkMZ6zvHMjtyvocRfzjE_w7MjTbcUo5RRj1xfOMypBDdRIBbCqD6XUueaRxj3Hiuhh0KsCwcT2h4yN5p3K48NWVOiRd7ZmKn-advB1yf3rCc-BW5P1cdPPzr3zbe60MDa88lkVe4KgNtTLOSxjazA2v-7agIYOIo20wUms6rxyfDgTxt3HcEVwAnroJV543kkuQzRNYtZJ0pvfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از این ترفند کاربردی برای روغن ریختن داخل ظروف استفاده کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/678066" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678065">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
وال‌ استریت ژورنال: مثل همیشه باید ببینیم ایران چه می‌کند و چه می‌گوید، نه ترامپ و دولتش!
نشریه آمریکایی:
🔹
پس از توافق ۱۷ ژوئن، بعید است ایران وعده‌های ترامپ و آمریکا را باور کند و باید عملکرد ایران را سنجید، نه اظهارات واشنگتن.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/678065" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
