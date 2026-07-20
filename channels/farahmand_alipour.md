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
<img src="https://cdn4.telesco.pe/file/DhagzxL07yQhsjYeVb6Gs0aKX4GzOiQdpKhqv-EjXOUxuHVS55sxq4mM5JXB9cvkAAorSaJU1cVQ4ls4AYxarIGINnruzNKjr2rjVoDK43vWQ_dG6GB_M_NBlzEygyi92G2-TzbamMu6BJVLiKekOB6i0-DH0kVir0RziioBAAOKDXrFwAS30QYKRYmaP4e16SfwGy4lBmwUkfk0kt94upjrDDcamoX_rN70jGsTJ-Y_13HF5EJ56gb04UKFPDAb8Wfn9_3TURZVRd3p7R9dT5wZuvHX2YcnkDnjCfT9r-S8MgRxPtRWQu3xGdkNZwzkuMulOBSYX4jB1ZleeQAfRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 08:29:30</div>
<hr>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HOGWW58Ca8r-IfC0ijyKWBEbOMY0OfGjz7IobZkHa-aFb8m-FOHAs580oxjfI-FLULgtoG-ornyIyE6DwdizY-8jXfwlEU96jGIkjEhRK4-uB62C8Uu5FxtP6EM3yTYj805it_LJZM-BBU2IGV_xlASohq3YLaMouLrpXlq4FtHiw97YPKktgC_kN5p2NOltNH62ffMmoGfdHTK4ISX_vAd0Kfe6QcXpqMmstJ5pXI4LRBg_Jxu9qhLbRR6MenRjkUEj8p4K7e3tUIDy73L7ZcW6eOrH_r_hmBpUgANFCbiO-dcOY_CuyWzvk9QIU9TO2DfIrggBBt5vWDe1aHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDHceAws_DgHKJfPyxY_hbQFOKydTvRD8S_cgOocirT6Wx-ywl0KRXHQf6OhMNN3zocsp_m-f-qXQ5LsVUrIyAVJFqfaNc5rw6pss_ec7QVWAkSntWb2KwTWP8YwjbBOOMihz8GGAkNdJ8ch25z8QrdZado7tnLzBnW5Qe5efpv584P6L5_V7miT_QLG-SBABYenMKGWGB1YzjZ8woeN7pf2VImgkxl39Tm3qZ9YAEcN39WQJMSSSDCbPBI85r5LMCrbsCFz60xSY9D4pxmoZcKLUvjGJq3yRKS9pgyas2mT1tB2gou46k1MEs9KDv2QarRE2KF4-LjKR8PvP9KJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQTm-GORMQsHyoQA2Jfe9odBDfnVbM5wg4V5gYjcyBNcP5-N-mcPzn6CoE9Wb0cNKNhboYrr5VmCWpbBjgOua9Da7F7pXnc9pWvx_vqb95Pfy8J98qtAB8y40-DEhbThH_fxPQLv2PYX4I9L13zNe27kGLwMlHl-GrBtyRKIA5R91UYA6PSdBGFbhCoCpBOhNRMWNP6cblMKBmYyAMdgwixCp0ghnR92N84suRuHUGRzNK65D8nvMayKqteTQavqfCoYy5TsGTJYAM7_EJxKtZl9BRA_QIDnyWNICKImpt4obdRBKdmm2EDSgv7fODc27_CpxORuOeWjHQR4hFgyyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIOQVfZhz0XXHmouuOFUMaUiXc2QtDnpHgcvJ_6lMyLvPvs8vAbQMS96y4x7Fu4lDImcltyaeO8qcsieUdVVrjqKvLhVz07RWiYvEFnCkc5oEGMA-lLoYN5cDatcaY-zGj6oPI7Qm46NNOvRDBhCi4U1Jlq8OEUBy_4XnOo1zaqrfKEbt0K5KwyvFFMkdEg4g67rxaIVirQN9_0UIn_o8wFWi8hihh2gx97z3j5bs0XutuWDNU7b4xStT6ya4yX8-Ag8dIL_Q6WPFsMnI9tyJXPXa5_fgJOgJpUDHnJ7_LSTh7ubMeAxPL1wUlAXvn9ggmQQZSi1SaUNzFZR-02frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyuCq6tEiv8NQL36SMUIf6ZA9QmVBh8SCbwnL5bDZah_QiIqzuYa2DZqZUYv6w2wlal-eKGaYKY_bgFyXVslqJCEQlIxO2p0mgaDotC9QI6xJ6TgWcRy7yfZ_Eao7vev0eRndXnW3uzS3FgHwfbe24eB0Oham2-4aRyTdUaqFg_u2xvjHlvzEywVAs-V7t2-T5B9Od0diDdmUHH6fgZkL994Hn6-t58TdqGgq0md9BETc67g3OVakxf466Vp6v23kWISRTizM719UWroRY-PA8av6oi2Jh262UPS6QRsr8lCNK-tDOR7H1x6OiKC9Zp5tDWw2PIzBWQd_Ep3RirYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKb2WoAYB2BfZWkNY37IBbkbjJc4SIQ1g5XruVQSrsNKs3qgofww7iRVf2qoHSMHt6t6iMSSSuI5_6vfGuhUR14Gj-tuEAUG7WOMbKyyWwtPM770N2Kf7em2Ts-reWnN13h58cs7C2vy2zGJaFZBJg9S4K7sWOw2xdY7vpCzU8FrGrZBPb4ZBv2JGSw1BdmJmBzcJ5JxWICl5QqD8l_FZ-hXN96hAPs-knwNk1QmApMnpJMp45YZSZiJZLYuw5X3NAHMPzlMKAR0HCu4nBM-LypbT-i9VR58PTd4ID9ZsTDQmszlfFOJ-ihl0o_I2WCB1dabJaw2OWhHUsecid3pIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iGQ7uWuF4IVbYvQBAeK_vgUaE4-VNFQ-gV4mPYw-ZFL1BaoWz9I2FloV4rf_Nb-or4n6ZX_ASuO4PB_sbhewHP8KNgWxRZolYOvUNmd9Htb3L8I0ip88MHjoNBWAp2NrHrVaIJTUx4Ercy8-le1pv5vPWBeuAzXtfRMjtQ0Tp1BWQwW_6O7iTm2aTlcqp4IiWUxYpgENc_Q7iAHgYrtNgW8U4d9XRbCo-Hp8HovZiLInUONHY6yLY4vQtwVBcwX2ov4-WUGR1Ow6-de4wxvWnWr0bUsQm3glRxV042sOZlWAaYpgMCx3qzd5UofghkrX5Ahne90_XWKjZUrhfYeQcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=iGQ7uWuF4IVbYvQBAeK_vgUaE4-VNFQ-gV4mPYw-ZFL1BaoWz9I2FloV4rf_Nb-or4n6ZX_ASuO4PB_sbhewHP8KNgWxRZolYOvUNmd9Htb3L8I0ip88MHjoNBWAp2NrHrVaIJTUx4Ercy8-le1pv5vPWBeuAzXtfRMjtQ0Tp1BWQwW_6O7iTm2aTlcqp4IiWUxYpgENc_Q7iAHgYrtNgW8U4d9XRbCo-Hp8HovZiLInUONHY6yLY4vQtwVBcwX2ov4-WUGR1Ow6-de4wxvWnWr0bUsQm3glRxV042sOZlWAaYpgMCx3qzd5UofghkrX5Ahne90_XWKjZUrhfYeQcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltal-iHqkU0t-EHVYH8ZhpAgiCYVDQtn3wBr7TH3XJndSFkvIyRCPZ7zD4r5YX4kbOKH1uxuN0aLUrdvaiiZTEoSzNZpoffNDc2_btwlxDopv2nx1EuZK7zQKhImefrntwGTuCWlVk8JL3jrKujqo28IxRtltUndl-jkDKS6HthSH3-KuA9yb7C_HZNa1CcmWzIbu_YSpKmlDbatnlbpWPi5RndPAmT28vdaaz_DHYC652KN-h6kuBlgGPP0mmG6N1O3jrbzsdTdyzK9fn6dqim164x3MJ5s6xVPdUukpyCJQxYlLT0On-Pej-4U6cNmNE8H4PAstP0gws1XZx8qzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=pjKFM_g2BzC6PkoJ_mpKjPzwJXBmwAeTlKUK2QYYEQuyj8kZq69a2eMQBnLal6gUe1r28kiwkZO7M6NkxlFU4sALXxrnOHWSvf6aYqygft9k_YfycmtwU5q4hLkKQv5OsDR-T91ThEqRiuzGrJL0e5x2uyh1JGP_B-ygBlG02Qp1Jq6DtHm5D8T6yOgjOM1b-rQ-LiBfLSwlz6xN9sRXN1ZOOyYHC8K-GTSCFsbLXDDpUEvZp1e1RMvhEOvLfGepNv9PWYlosPwZlT3NmZtuLC7GhnX5wyR6137xsZXJBw9iFj0IMVWiCZt5dMAq-wisEvqmcLmnV5bslAI8TrvHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=pjKFM_g2BzC6PkoJ_mpKjPzwJXBmwAeTlKUK2QYYEQuyj8kZq69a2eMQBnLal6gUe1r28kiwkZO7M6NkxlFU4sALXxrnOHWSvf6aYqygft9k_YfycmtwU5q4hLkKQv5OsDR-T91ThEqRiuzGrJL0e5x2uyh1JGP_B-ygBlG02Qp1Jq6DtHm5D8T6yOgjOM1b-rQ-LiBfLSwlz6xN9sRXN1ZOOyYHC8K-GTSCFsbLXDDpUEvZp1e1RMvhEOvLfGepNv9PWYlosPwZlT3NmZtuLC7GhnX5wyR6137xsZXJBw9iFj0IMVWiCZt5dMAq-wisEvqmcLmnV5bslAI8TrvHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vePYIbbQEwynV-7B2RkzH5C3mr1Q5w7kHCHnK5PJCd4YY06NF-GY1o3h0SRArCsTzRt107NdjpYHEWMaBlBWQkbdv6njrX2PfAUMWv6v3SKai2D-jrv65yfZNIkT_aBoJpLZcvDp8_682xnjfPcM7Fq8DlbjmgKtfsky4QJ9qBG7rfJ9KAeSmqzbhu6OmqaE6aaTsvMaaFV9QCuPdooG3e8nEVJLsMcj81Gy2F87sHjCkO8tDh6ptnOup3dDPV03QCqG7_ftwwcbl2NVoWuEOmSdMsYlkchfJ1VOgBch7Tf-UqOX_lnRaczn-AcQZ8eO1ERyN9WRePy2hx2pA-iZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGL28nxqRl72dzJvRCB1QjfSfvzXqXHyOQ-TSOsFSyWdNUimWAwq0dNuOlUuPdbqr1VpstCOOcxlW9d3lllg0Sa55tcidKvAs4DHxy7jPUTH9TxDgbyK6UkofC237gxdTbfKzclOez6r0ydNp0LvlgPsus-uLlnZ_e9O7Co6LZIOdCGqZtRFlFtIKGdaXgob9Cdr_FSIyBju3rPuAWDPdrzWBcBi8clna0ahmSqiQRSruOQ6KKaiYDUstVlqJ-OBPS1JBL2fGWnwhX416irY7XjV2BFRxmu32abwX6krQfIoSDXeLV9NmglSPCpHO_V0wtT1PT5heNWgQ51eqjacFWdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGL28nxqRl72dzJvRCB1QjfSfvzXqXHyOQ-TSOsFSyWdNUimWAwq0dNuOlUuPdbqr1VpstCOOcxlW9d3lllg0Sa55tcidKvAs4DHxy7jPUTH9TxDgbyK6UkofC237gxdTbfKzclOez6r0ydNp0LvlgPsus-uLlnZ_e9O7Co6LZIOdCGqZtRFlFtIKGdaXgob9Cdr_FSIyBju3rPuAWDPdrzWBcBi8clna0ahmSqiQRSruOQ6KKaiYDUstVlqJ-OBPS1JBL2fGWnwhX416irY7XjV2BFRxmu32abwX6krQfIoSDXeLV9NmglSPCpHO_V0wtT1PT5heNWgQ51eqjacFWdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=NAFJtT3zz_ZCpAXOod8HoER1UO_jxXFb1-cWMuScsEJc6909wYikC9suYK3cT98sVfEst2HfrO1ipFCPUbyCFUBnRgBCS8AySS8UYW4rm_lWsVo5MwOZAh0h01zfK-wCEkbycdgFX8PcYMs11ddSXBxXipGVQCXZ7g8zZrWdnsyYzcvVcSzPXDMLPGXJU-6hzWlzRezqSMjYR0yagp1-1JFewIi3ihLQKYuXixfVzh6H-lO5EHBHSzoprh6tFQGkh45WhvPMrTevyRZIRfPguaa72hlT7n2hmh6_YzGXgCc7Z8cZ46LvAa5zBvTDNFMjoMKZXRkNAw-EO1FIR58cCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=NAFJtT3zz_ZCpAXOod8HoER1UO_jxXFb1-cWMuScsEJc6909wYikC9suYK3cT98sVfEst2HfrO1ipFCPUbyCFUBnRgBCS8AySS8UYW4rm_lWsVo5MwOZAh0h01zfK-wCEkbycdgFX8PcYMs11ddSXBxXipGVQCXZ7g8zZrWdnsyYzcvVcSzPXDMLPGXJU-6hzWlzRezqSMjYR0yagp1-1JFewIi3ihLQKYuXixfVzh6H-lO5EHBHSzoprh6tFQGkh45WhvPMrTevyRZIRfPguaa72hlT7n2hmh6_YzGXgCc7Z8cZ46LvAa5zBvTDNFMjoMKZXRkNAw-EO1FIR58cCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXC5Ix_IXsg9CsdsepoYgyEF-EXknSmsTkR-sjq4z8BDN9eeM6Hcvr7cU-pKcXL5HUcH8V12buag7yNQiHB2Ix9z32qN-3raXzLtxP1VJPUl3fweVtoeCQMWcK2ooHSIYgJ6t6LU1zCBQJJtO5v4vl9p1_NZ2Z9Rf2IFwsyV4QNjYJMrdFDsZTK-0fRnhtfd5679dE1gMfRcONBQw-CV9CIqJOopRUZK1XbRM4ZCi4zDQUAaHnmcWn-oQMboD0gZyfsk-GfZF3hYPV1u8naqxw4voSnAkxE5log14WpntcO3cndWgaeL1-P5_fwZnCqPmvPFVTpt1dYqqwZSFahSBlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BXC5Ix_IXsg9CsdsepoYgyEF-EXknSmsTkR-sjq4z8BDN9eeM6Hcvr7cU-pKcXL5HUcH8V12buag7yNQiHB2Ix9z32qN-3raXzLtxP1VJPUl3fweVtoeCQMWcK2ooHSIYgJ6t6LU1zCBQJJtO5v4vl9p1_NZ2Z9Rf2IFwsyV4QNjYJMrdFDsZTK-0fRnhtfd5679dE1gMfRcONBQw-CV9CIqJOopRUZK1XbRM4ZCi4zDQUAaHnmcWn-oQMboD0gZyfsk-GfZF3hYPV1u8naqxw4voSnAkxE5log14WpntcO3cndWgaeL1-P5_fwZnCqPmvPFVTpt1dYqqwZSFahSBlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCvSTOYx0zKLF6l_OFyPakkn2mIljlAQ2ei1ijJNIOnMpO6xaZnv4HyU4NOOPb9DsmNH6A742oDAcg7myl5cYjcUh41dcTXPkl9NQ2ttOaIYpqXYhnwzc0ojH39gBYH0zKrTPD2GMgmwLRLIXNn5lZxeBhwhDrZbu1nW9caz59WbNV8ZpU-MY5tl5E8ajtUmg0QZjFeJ8eYR-LMARvphq0A4xgENyxI33uCge6fS5GDlw5svNmLNklBik2fhNgL2MpIvrBv1OJhoHCxDez6Uv_t6t6Xxurhw7bIrmsSO4uTfKGLbZ4ofTk7ei8NuevxjRE0WCp3yNGMGSXOkXU-xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrbvwW5TFtN1xp5JsOyer-DdQvSbUfRuv19jr0R9qkQUDpk1TUOn5-PGGVZxwpSPlGE1cdjxXV42L1aehjOP-69ckQhXGMMr1mFhDY4bytXZTVwByDklhnNR3lEoF_dV3VL9FOBeOWY_aPf_ZyHkPuMbzRBDjMHxomcbVOfUwi0sDQDnFvdn2GGn0INtr2-74PenIpDe_BxhZhg_RYyHLRiUB57OoHWqAyOZQ_9NB5OBq0T6KxAIj9WYlLaN6WI-dT4CtfhtikNBI3RqcoOoUu5Ub7yOT3gWnQHNCsOE29jC14mT3uHaHITZFLsJtVZ7L7yfh50X01h1JMEsP8GZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td9i8uvGwxLXeXqyRK_7BL_11V8XGhy28qSqHQg48UtHBNy_9F8dBJdmZWN9gzmqQVrYEGjMcJ4XTsBAWBnbfGUeAHCrWZXCO5H0jXHw26fdrjGhZcf4I4N3W31YDLQoJw_uMN_WiIR86Mssj4NQ9Lmxfr8y4Lx3r9z-bwTac9djpM769DoyQfqukwwKa0C7JkGiNhCqlxc71U66CP3Fk4YQ4GYBjFIxDPyc-pogRYaCIFihw48uCsKTs7JShFyGGlF4PD1K63cO091sniRQii5_Qr_iyz_jRCXNjzfMC_is_W1vt0Ephu-kSDHmZoYaGup70WALWM6oi7H8pcPg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq4CZ1apj11KAd3wsQpOP_pT25HNXmBsaAba_Sa4MFjyTuWYyYuOcdkautv4yWWX4eYGkU6EUqcHbhUUCQfAVeAGmyXpE74MM0hHpxY2BLf8H4O5J_pNItjjkJqXnDz4Hr_t5Y6Ja30A0kes47e3E5ui0ZrzlEzLm93yKE3F46FPNPnqAmkpnDXDUiQqNJCyQkb7-3ZeVjHpcG-56gXGMVKcShzn7asifF_pfZiGjlKG2BMbxZ4Rd9iu4sumAna-8pEQPC2PRWLi51gt5BG_74uENSmDx6mVEQ6yebodOFaT9mLKjviyBU9UFM5rRYz0qQ3muZ9OR4GLIu4ynZsp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pl6jo-Jnh05x95gSSdIEIChndYRcIUXO46QKAtkml6V7QchvTsu_8xztTa5aa_ZeQGAVw9Nsn2ZVqyWrAv_dOMBHk-LIUUkX73GyytWMggND63goKtGWkCgMcEthhWn-_R_kbm8NEA58gWOPlhgf3thM1VTF_DVpgwaFGbr0JWF70zEmcwsa9-RdIzm5L-nhqGinFCjuT7mnlQ36kaa9moGee_L68gik4t2okpyVJmB-zVYag7JrrglRPcxFSidkqnMAhf51zed_fySwUA9UqYI2zm3B1HyAZ3Fs76UdUnCj4xseGaVZc7t1AgXQGBpo7EVeshhAdKd6GxpeyGC19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXvrvd9OGqJj75e4NYSEUMbUFHid5Yx4sV41qybk1uyi8FSEeWwXEoHePNTCAQurxr-O34BiwIpzwNtA6I2d_k8pxc_pfYjnFISMCQ1TOJVTDaPUu2SqZ-9yLxhMXUceIaFYvNdicwhRaBMio2gRVqATYqpZI92_ChqJ4znEWoSkQKqzCZC0uP6p9NGRIt-ywYVJoo7JdyU_9XpSyqgK8X0zLsSp48h0BafY7s_D4UyAbpolZG0K4cT30MuCSY0kt3sQGMDNLxGpH3x66WFvuxes3gdD1sjt0YXlxaa1Qi3KWVC3WaCtRp0mRCCn_M614sdNF5cN1ukZkPnGWxgRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5nUKXUOzQ-HvDdIqJ0nOpIcyAlA5raYJStVDAvLE_CUYNhUL2OQgIv0hcjGSEHFyKXFeRRhTs-Jf-GxOgDEN37Laow8GAUJ8f0hlM06weyx8nVo3oTKG-AHXWGozbMO2wuXXHd1vb2d6m8wB8IB-kOWRSEzGI-KnwRayJ-UyOmFHGKo2VlGPPJX3bn6-DfSXwyfrFBNQ3cmAv6uQ03n2Tp2aExjYEetajNXaTO2lavynPOhPXaES7tuYJqBfsTjWqNvoU9zPCKCGsj70pO0xaBVTG0GIacF1u696arOtIX7YqhEQaC25maRKa84gENqyCtZSwjWYwsooAIUmVl2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIUrfD2Vs9shJasfXDPbh__udNzLCKJdWsI3HZxPPuDwJzXUqXNxPxUHhJEDpuodYdqSD-JfMIxgIdTzh-m5mrO_cim7AkKAfRMLNcCyw8t-K8Eoonv5PoCeI8mCj67kesgysGkXiZxKXSdkYifdcXP6wAssDT-LVZu3OeQOCHLMtlwCAV5Ln-pLnrmSAr0Ow3iqkQU_gy7oaUdfzuMU1z4RPSa7Hv3zkAJpkQu5wQpbhQMETwkdd43qKxMEH3LGPaQ1gZY4FVPoJvCsrKG1YVXcnvArOfneB08pLM5_pUA28SqTb6tg7sJ_YXoZt4J0VlZO_amSjMEfQADbLXYb3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2Zkz2QXaaghYbD2mA8WsGK3m7H8_adB4IV8AAzH4hyAEt1Ht0WSNRdvY5AS-1BcKM0EOlxHKRmRA0m1BVK5Av_3dnSvc8ApWFAzpRDFrWdJYZd5GvVwVgChLH0zxfarZaOHOJ-wx0Dkte8OccBW0Es9DkLmZe2b-FJJEq7rELA1jUxFt6OJX3w5JJFTMXpdgNrB2x2AeCNV9nLRAd-GCxAFNkOIgyH6WKp1fO4hsKS1JW95uFRf_cL8J8dnDEpceBFHImM3kSkOGFdboAdeJGrnIdEiQYuy3B3rSJfYM-wuvPtZB21WDT7Viq6arjS7FgHxpkFTkVIALrL_xrYjew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAQAoj1JVoedZPrjF1Xru6fWqBd_WOuh9wgtV0WtkpXCq6Vc5yyLaTpYXQ4Lm0nXmx4GbK0sRPlpnpL3FJgxachEsRdHK3z9z75giUVyZxAHR97h_xGLaYvnBCgg5I7YRgsnxzZLpKfmQQTOETwmray4aQoSvddW7gdoPakjgTgqhx6zatt2IIHYz_1Q9AXI8FkZqdrKMrz3iP9DJNhjOfafpfV7A4YSCKXn7jsHZSFkZKMauZNOUEUyul5S78wLbofcpcKB0js5HIbWd31yOkudDkZGa0uKAbDxPegw7ahsGHsc_MXHuDQ4ATdo5_8y-8ps2WiMmKhfTuR4IcdEsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU-l_-mT6vnQEEKlOsj63Nd-kZY3_LV10vWlnuQeK7gJqenHQp3XFnIKpSru6xhlhfjPo6fBbLH_W_VIfTLvTLjVSOMG8NJLyM05zWtbQwUzOosf9BYCwI4TmMKPnAg1zD3YpzHVbWHRPC_Bod0ONpDnU9WhgHcYps-KzzZASTG_gzVglhhvmrtyHTWD8EqpJ3bCSpXUkgJ5r9KFTnsFatiUXMGzeiD0CX7vK8TNGj1cIBMy6l02Cvw7eZ5TMD3AuFe9GkV_xgyujeGnlNa6KpiX34r4rXlR5JQ3gnziKwXX-dwEDVI-mtiAKJlKnVpHWbJj_TEntZp2pK0Y6l1FgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZG9X06GJwK0gKOLgoMnIbfnkOM6GvV9L8yFyqbghAa-jdx_Hg5qtMP1bBIEbU5Fo6CtI1ep0rmBMircX0Gk_IxCoFWCXxR7fVo1UXA08jnuz5Y5pAADjskRWjOjkQmITW4O6OUAYUWMuUT69zoa7T1Zw3dnCCRYmqPuevHoV8i17t56xXZu9cM8EPW4b3RQYkFwFjeKR9aPLdOti9eJpvV2P3TXlz27I7BKOxLV38hsSYvfk0kqqBNDOeLRmoy5t93Rw5Kzv1zSHeQJb2ng55pmvJ05lYP8HCDUglnk6AJWFRqKMrhqZRUpcjizidP0yIt7s6iAJGSPx0hRj7ARNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDnqOmvpxEbIVc4zWcDYi3iTx1BQ56ln8rFL3mOn41RhFjcmSb2MCZMvbtREejuX3lfG3_0IPkVD_ocr91WiTJGb4z4Zwa039T8tQ1d2zvLptdITgo4Biv3hNtrrpVDwMhKOoj9KmHYDkCwI7dnX5VwRDNXIVEQ4xXjYSxPlXxunqE2RItMg96xaZ_dbPXD-YGOKkqrm9DJguBqHENlospm_Upb7xZiEDiAk7sS4IjFYEwjNN3Y0yrCMl6GIAx59joaVptfm_ZFu_Q-WwAaSYJtMElvUJ2VKxrwp5lOv81ygNb3JNSbIpBuhLAPzXwAgUzYhmIkxBsEUjdOKbmV_qcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMDnqOmvpxEbIVc4zWcDYi3iTx1BQ56ln8rFL3mOn41RhFjcmSb2MCZMvbtREejuX3lfG3_0IPkVD_ocr91WiTJGb4z4Zwa039T8tQ1d2zvLptdITgo4Biv3hNtrrpVDwMhKOoj9KmHYDkCwI7dnX5VwRDNXIVEQ4xXjYSxPlXxunqE2RItMg96xaZ_dbPXD-YGOKkqrm9DJguBqHENlospm_Upb7xZiEDiAk7sS4IjFYEwjNN3Y0yrCMl6GIAx59joaVptfm_ZFu_Q-WwAaSYJtMElvUJ2VKxrwp5lOv81ygNb3JNSbIpBuhLAPzXwAgUzYhmIkxBsEUjdOKbmV_qcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=Dt4UPFdHPc4ZzG83oHmnCY-ELQTL-RarQAaTRCx2ii54R7NLEKoPeSNNyyPsQX3bP0qwV7Puj6CxyFZzLN-1LxiJzNrHgbHK9yJfvnxiTzP6Xp8cahBzA0Jvx4qCr5GCCYUFPAwvfYezx5lc53Vv2xx3tqCw_oWVUzxIRxY7aaSlEqJFi9i6HIHthTmUiKk5Am6jjzN2c1Gsz2NKq3a6vcsn8fHjv3oZVuo4BAFDpQEnUAzar5LVSYnFtSFWo6u3e9usuCgtf-TSRxEmbosACMJNu_tYQQ4fEvdL_G53KPL4yLmx-Stjm4JjfHlWsFFA4wS4rGbdeQfyHGqAo5wRrC8_1jlmD1UwNQ05i94yUMGSGjgHES8tX3PrFhtHzFqZUYakJRPeqRTOcmhy80jedHM1yvt7DU9xIscTjXHsuIJAgGh9teJWbcP885MC_lRkKqP8zp-CTPWS15bZdcHYPjCqwgXethpnPNBVTVDhJDcO4OY78jzgRaSK4WvUxyOrfapLx1k4hHl0z05anGHAnWCoLL-7zq5PAEH2DCld5ryaTxGxBWM1O8-IE0HquruGWVlf0lG4li4qCYQiEjxPlEMFfroqPe8zF2LOL9oPcAiygYtfHIJ65ilBZs6A8xQ074ni-A41ENSSmIdfUCnjrj4iuSfs-NMcJY6LbxTaNxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=Dt4UPFdHPc4ZzG83oHmnCY-ELQTL-RarQAaTRCx2ii54R7NLEKoPeSNNyyPsQX3bP0qwV7Puj6CxyFZzLN-1LxiJzNrHgbHK9yJfvnxiTzP6Xp8cahBzA0Jvx4qCr5GCCYUFPAwvfYezx5lc53Vv2xx3tqCw_oWVUzxIRxY7aaSlEqJFi9i6HIHthTmUiKk5Am6jjzN2c1Gsz2NKq3a6vcsn8fHjv3oZVuo4BAFDpQEnUAzar5LVSYnFtSFWo6u3e9usuCgtf-TSRxEmbosACMJNu_tYQQ4fEvdL_G53KPL4yLmx-Stjm4JjfHlWsFFA4wS4rGbdeQfyHGqAo5wRrC8_1jlmD1UwNQ05i94yUMGSGjgHES8tX3PrFhtHzFqZUYakJRPeqRTOcmhy80jedHM1yvt7DU9xIscTjXHsuIJAgGh9teJWbcP885MC_lRkKqP8zp-CTPWS15bZdcHYPjCqwgXethpnPNBVTVDhJDcO4OY78jzgRaSK4WvUxyOrfapLx1k4hHl0z05anGHAnWCoLL-7zq5PAEH2DCld5ryaTxGxBWM1O8-IE0HquruGWVlf0lG4li4qCYQiEjxPlEMFfroqPe8zF2LOL9oPcAiygYtfHIJ65ilBZs6A8xQ074ni-A41ENSSmIdfUCnjrj4iuSfs-NMcJY6LbxTaNxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1LfTES1lzssXAQrMK-Z7x6aUbDDJLoce6s1heP1LG39LT8yLdKpSQmTjoFtNs3AUQvgYNkn1V1dbG7DQkaz-7xS8NfWUzxO9YH65wiJzsU9lauD5rGmViZQRZu2JwHSsn6tWNJw8KpHl7t8VHgZztwhY__MMvyjmt9s_x9Da1x_oKhe8UI8Pe0Ezv0u4yCzqIMVZGDLuzznQcL1ZPnUsVckQSsPXUylUVAsZjHd7_2bnU5R4W0HJsba01fBfB2yqRpKUUA15sJtYI0IPOUFS0zqbUf2O5Kvu_gFTtlG1lzLrBs6GN5UAir2PFfMAw8K3bKPdS3xPXExStH58MoJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=W6FFAT-1wRMb3GT8syZISz-r1lhlxFDCcaoYK8dluNCwHlX3kxAAzpg_wCHSy2gfeF4r93HEVo0VEx9wF97j1NVjDUIYb_P1-atpi3IQHZVjPT8vhah7GiEJWg5tajji6qkUfMgSDUqalfaaEMps06IsOEXfoJIufdTMDwQGgSqzCJLO6R3h4NZfue9PR5vLhk7R9yJPavH6o4IcrV32gzjAkyJ6V4m3wlGcU7GCNz0VtXU1jFJmEZorkEd7hCMUOqC3jysjZwadYUAnFACIwv8VQPCAZrph8OoR8-VsqqA6SD1KM0mtMNQwnuzhX8wa7-6Co1XW5WwjuIbMRZLdXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=W6FFAT-1wRMb3GT8syZISz-r1lhlxFDCcaoYK8dluNCwHlX3kxAAzpg_wCHSy2gfeF4r93HEVo0VEx9wF97j1NVjDUIYb_P1-atpi3IQHZVjPT8vhah7GiEJWg5tajji6qkUfMgSDUqalfaaEMps06IsOEXfoJIufdTMDwQGgSqzCJLO6R3h4NZfue9PR5vLhk7R9yJPavH6o4IcrV32gzjAkyJ6V4m3wlGcU7GCNz0VtXU1jFJmEZorkEd7hCMUOqC3jysjZwadYUAnFACIwv8VQPCAZrph8OoR8-VsqqA6SD1KM0mtMNQwnuzhX8wa7-6Co1XW5WwjuIbMRZLdXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=ucci7ypihUOglLni8fbL6gUuLP_zTUBalj0EseX4OBrfWvZrPfQGz-QbJliycSb-HTquIflTpw9U8JX7L3wSXTuBVZ3Ns7Ac1FKxfeiX22V8SAvD2RHld3bSHbRGOt6lEMyKBQluKWVoFKsH72uNEtSes4V2FBruO7FocKkU96GSnJW1Vo4g_0ps10uOhqmXhKPX3UIMyRPIkGC8buYHFGAssJlqQ1dm78oNtRhm-xt9ABaMgu7RbwBvwD3ilQuZjOsgvLi-5Nse4vMZo1pEVgH_eJXr_rkidv7kXIe6Bq9MdmtDezBXH9nR8pF5qoZsBI4SyN92hFWz5Mmv06KR5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=ucci7ypihUOglLni8fbL6gUuLP_zTUBalj0EseX4OBrfWvZrPfQGz-QbJliycSb-HTquIflTpw9U8JX7L3wSXTuBVZ3Ns7Ac1FKxfeiX22V8SAvD2RHld3bSHbRGOt6lEMyKBQluKWVoFKsH72uNEtSes4V2FBruO7FocKkU96GSnJW1Vo4g_0ps10uOhqmXhKPX3UIMyRPIkGC8buYHFGAssJlqQ1dm78oNtRhm-xt9ABaMgu7RbwBvwD3ilQuZjOsgvLi-5Nse4vMZo1pEVgH_eJXr_rkidv7kXIe6Bq9MdmtDezBXH9nR8pF5qoZsBI4SyN92hFWz5Mmv06KR5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VH9prakRqZy7x6ZF7zi2TpbMavtw-BYfXVTvJnpnJhinuiroYUwrnVMgw0sbCQb9qt32gmG5KMZxYRTY_lPUnFAgtsFUYKxdlo0nC2vkFeZGp4Y9PH2M4CFHN-pl8ZjkDCVXW146ewAPXELamERC_isvzVia_rmKyKCyyCgRaFmkW2ACE31_XU4ygATbW2xUHtYFhvLzT6EDr9BISqwyvMWJ4FYDOnl_ahLpeRtsIU0xZcH8Hq0csaysRiw0yNDyWHUG_FZtZe0FEo4-qQaBOoFOPGtCT8uh3328EMnbH8-4wCqF1K3BQC_rA__nf5wQFkvr-rHnddTdsWza5DjaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxGtMibtPPKX5GC4RWLJIud-NtHRErqCTsWrNgGzWZP4MyI0gs7DVWYhBE64nYyU_Nu29WyRKdt4Nbm64hFVwNGqaFLR_qGZ7za5oQbPsMoslKprlaZLUsLayVejGGLNapgXgtznWkCeK5d5mAo9Fp4v_rg5ruSJ6-5R2TX746ek3uppN85FMUAotvjPdtgLRvmKYGAcIQ3AFggF63o2T88XIFQqWB8w5aizpKSIhcEAkTTRpg5OE4LOtDfwQR1pQ8nkd7fTdzLqcPFOU6lyAX9yD8_ooJZXQqOuCgtS3rr-iEA0kjYtNQCE0yObFt-JX7DOFboUjmNvw42T0E5LhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=Zm3bKDAJSms7NSEaQX4BszciCkVAEmc-8D0E-aeQRoNxWd4CD9Ap4-m07VWeTjPFkaSDVIBFvQP27oBrpPusqvBUTgLSIP_Cj2qPLc409DoorbLoF1-MRwbq-fYMC1w-eAJLykATnQg9BxOet3C4FQDHoYrnHGjMhrLpNN1wZKiWfelnaFq8-SpUFsLybYWXR_Ug11cJcQfOrr67sQv8kjbnoLBSE2EYspnkR9sUd7px-khyowzxH5x4RkfUgKxSHCYdRTU1GjxDi4u0i3aLQh-maTg7AAvF04-bXhVX3Q4QY-xwYWbkeQJhUY9zbnayvZ4Bt2aON7m0n7hNqY0aBo0NrAsREhN9-A25W6O3j7rrhpQs7a9SBwVp7HOdbs4Zbv1Z_NbufJTHe0iwUlZ2neqxl531HepfDErHoJpR5tAZnotYrhUiVfhGuSxnprZxYqmzCnAlEb-g_-bQmQdqxm20tB7DX6VPOX-0FlQRcVEhVFYklins9GD5bN37ZC4L0Z8oKEBfhkSjgVVOjnH4rrpWMB6g6tw4oxpsvbifkTRe2QYqmHfWimWfPa4_jelDwl9DUeCcrTm80JYqh5cKQCQmIxKJLiP-Q1Awo4ck3-anQs6lhe75BSXl6bJhc_mHOADJYXXKcTfw7V6jSAX9Lh9zUsKH1c6M2B6GyMK56I8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=Zm3bKDAJSms7NSEaQX4BszciCkVAEmc-8D0E-aeQRoNxWd4CD9Ap4-m07VWeTjPFkaSDVIBFvQP27oBrpPusqvBUTgLSIP_Cj2qPLc409DoorbLoF1-MRwbq-fYMC1w-eAJLykATnQg9BxOet3C4FQDHoYrnHGjMhrLpNN1wZKiWfelnaFq8-SpUFsLybYWXR_Ug11cJcQfOrr67sQv8kjbnoLBSE2EYspnkR9sUd7px-khyowzxH5x4RkfUgKxSHCYdRTU1GjxDi4u0i3aLQh-maTg7AAvF04-bXhVX3Q4QY-xwYWbkeQJhUY9zbnayvZ4Bt2aON7m0n7hNqY0aBo0NrAsREhN9-A25W6O3j7rrhpQs7a9SBwVp7HOdbs4Zbv1Z_NbufJTHe0iwUlZ2neqxl531HepfDErHoJpR5tAZnotYrhUiVfhGuSxnprZxYqmzCnAlEb-g_-bQmQdqxm20tB7DX6VPOX-0FlQRcVEhVFYklins9GD5bN37ZC4L0Z8oKEBfhkSjgVVOjnH4rrpWMB6g6tw4oxpsvbifkTRe2QYqmHfWimWfPa4_jelDwl9DUeCcrTm80JYqh5cKQCQmIxKJLiP-Q1Awo4ck3-anQs6lhe75BSXl6bJhc_mHOADJYXXKcTfw7V6jSAX9Lh9zUsKH1c6M2B6GyMK56I8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=N3kl0FktElsHleIRCadSNVFdd8zI37CXoPH0-9LHhYKfVMrKScd3wiMas1PmK3YRZ5nPg8OJQmgMp982ZUUiZuBpj8pF9eBhFmsV3YLGXsIVPpKGz5xjqbc0Z5iHAcN1yhdwA6Ed0n2l8DhmiDIsSvRajrZCzWFoN7m7i9-jMBdUY44GPX7X2erQ8q8H9iSsVduj8XnkCb-Tlf-LRcMRgMikM9zd4nasvguHgQb69JZpgzO0T_aDWDXwvWwJ7Sr5M-iGc1QBaGp1WyViF_WGwdL3rx8ksI1rhPHwY8n-3RpKhPI10XFVpF3ED-v4UHgkBQuNr4NsEol-3ZeZG4zL_2yO39R5Yaehh0cVE-tnVueuLPwyQLq3EcOd_yqaCwZ2IHXAUDqxmJG0Dd_qd5gW4DUJ03f1H0INkhWHMk2U05Q72DTxnwMBpl44yCbFUNUeO-r-XIoAfjv3cb8NiDrHkHNKjW7mCtnm-GcsOUfEr4W5cq_RX7LVSKIdQKNYrxwpUhr3okcvewgxo1avfGBBu-e0DagT4Eln4vrsyZrd0z6pV5sBO0_LUP9h_-_rjeeOUaSxONKjB-5b-oQoEfQtRz1rB2_Hmwga3sUeMhcICF4Dq4zOnTPHjTdyufD9HMO3L3Eo3wQKIz8gpGOciPll8ddu0nv5Ri9x7d7lMPgUgY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=N3kl0FktElsHleIRCadSNVFdd8zI37CXoPH0-9LHhYKfVMrKScd3wiMas1PmK3YRZ5nPg8OJQmgMp982ZUUiZuBpj8pF9eBhFmsV3YLGXsIVPpKGz5xjqbc0Z5iHAcN1yhdwA6Ed0n2l8DhmiDIsSvRajrZCzWFoN7m7i9-jMBdUY44GPX7X2erQ8q8H9iSsVduj8XnkCb-Tlf-LRcMRgMikM9zd4nasvguHgQb69JZpgzO0T_aDWDXwvWwJ7Sr5M-iGc1QBaGp1WyViF_WGwdL3rx8ksI1rhPHwY8n-3RpKhPI10XFVpF3ED-v4UHgkBQuNr4NsEol-3ZeZG4zL_2yO39R5Yaehh0cVE-tnVueuLPwyQLq3EcOd_yqaCwZ2IHXAUDqxmJG0Dd_qd5gW4DUJ03f1H0INkhWHMk2U05Q72DTxnwMBpl44yCbFUNUeO-r-XIoAfjv3cb8NiDrHkHNKjW7mCtnm-GcsOUfEr4W5cq_RX7LVSKIdQKNYrxwpUhr3okcvewgxo1avfGBBu-e0DagT4Eln4vrsyZrd0z6pV5sBO0_LUP9h_-_rjeeOUaSxONKjB-5b-oQoEfQtRz1rB2_Hmwga3sUeMhcICF4Dq4zOnTPHjTdyufD9HMO3L3Eo3wQKIz8gpGOciPll8ddu0nv5Ri9x7d7lMPgUgY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=XM-rLipSMufE_7mLwQPhfBiHNf_824leM1SLbpidBmYMXb4QEj5HGY8HSMEFY5NGQZuGV-9LfBliLAPBA0cpQZXq4Q_jl60zD2naGXIsDCt9mEfn-lCOttvifKPN3F6sVE-SdVwKkYznyIdal7tpCJxtUjrhdCm8Zr7cKfriPu3MWW9mkm7Gp5K1G2cqNULT6m1izW674egHBXPtCj1PwxozexdAfBUnsi_u6fNOblczxgH6bS5DSkGNW7zPTlUVoxjOeMsQr4JZNO1_4nxqiL6gSiioD0g7abcbQigB38sbnz7OxHMZy3UZ3uVcuUlnr6-slWChX2xHihh5IZl37Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=XM-rLipSMufE_7mLwQPhfBiHNf_824leM1SLbpidBmYMXb4QEj5HGY8HSMEFY5NGQZuGV-9LfBliLAPBA0cpQZXq4Q_jl60zD2naGXIsDCt9mEfn-lCOttvifKPN3F6sVE-SdVwKkYznyIdal7tpCJxtUjrhdCm8Zr7cKfriPu3MWW9mkm7Gp5K1G2cqNULT6m1izW674egHBXPtCj1PwxozexdAfBUnsi_u6fNOblczxgH6bS5DSkGNW7zPTlUVoxjOeMsQr4JZNO1_4nxqiL6gSiioD0g7abcbQigB38sbnz7OxHMZy3UZ3uVcuUlnr6-slWChX2xHihh5IZl37Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af6klA1XDqR0KrqqJfSPnyQniL6jbKtSvFKhO2p-QRrV6Gxug9Xy1aucHN8FaV2D4g2wdr9H0i2PAYnuqiGbeM2R96OH6FPPJIBbGeLSxW-iyr-rnrKBvPPf-OMsX-d8bWo2Zm-EwsSrrSkjT4ZlN6tSMXXy8e23jF3kvOsE7MCwtjEQ5MdFVlP4vmZQbj1Y5Tf8k5EpxpDnuL1XfnZm2-cQyMLfpWFXGcwA3K7-u04Pv_krs72_uO1Lkah5ySVSIYh8H8PQzsrbph6KpItriIzOb5j2LFWPhehafO3_mdLDBkMKOioDpN-dCyrERKtCeEdtgXRUjU8snF9xGvxDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=rQ08clamsouut_DkbLxofh-Z6Bm4ETfDXdHPGyNpkb5AZlPjCmDyQVzyliCSooxa1WCQRhaJtnhVzQ-1bkSSw0dG_L5ia-FEXBZDstzjCJ5iH_2OI5X1-9XIEaqWSBK8WrKZRlWFM0zUwWkYve7eQEqLiYj7L4R9yC1QQ8NVKm55Jr9l5yaXMjexwQ4nZ2ffryrH2IxbSyV1xrFKOGe5qXyJeFXHHwVERaGrEF_L0VQGWHsgK358LYwNACh8Do03vQIEmPVYYTIZjxM7uATJVvpLbiIVL1_j3X3GevdTfK9ahpzcaWKbFS6MyLdXgLxljNiVmZZBSLJy0m2n2iNQvzIA7gFSBHe-e--j1Tswj5LMc30rpKDnLVH_L4Ha34fXcyJUSVz23F8k4J8RlLZQ-x8_WzJWDh96eNL7UGWPDH6zYADYglHk1mFlZtoOGLs3_7yjfmEq2OIvTkIkqwrhP0vw8l8BboYuM50W6wVSjHY3reuDbe6tEM_GiaSCkgyMrFPKClt5dsZ5VQwpnHqPRPtQU9aGoxS2Z-1DMv_muFCfxkjxfuGiZs1smr4E6ZFGlHfc0fX06ck2uibFGlLEoomrggFf66y_YHFc-gOVlqhAlTxv6UaYjgqbpv4Csj5dL5UlrQqai5JIIPFt2fUYlP3EO_lNQft6QrdqOcIK7v4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=rQ08clamsouut_DkbLxofh-Z6Bm4ETfDXdHPGyNpkb5AZlPjCmDyQVzyliCSooxa1WCQRhaJtnhVzQ-1bkSSw0dG_L5ia-FEXBZDstzjCJ5iH_2OI5X1-9XIEaqWSBK8WrKZRlWFM0zUwWkYve7eQEqLiYj7L4R9yC1QQ8NVKm55Jr9l5yaXMjexwQ4nZ2ffryrH2IxbSyV1xrFKOGe5qXyJeFXHHwVERaGrEF_L0VQGWHsgK358LYwNACh8Do03vQIEmPVYYTIZjxM7uATJVvpLbiIVL1_j3X3GevdTfK9ahpzcaWKbFS6MyLdXgLxljNiVmZZBSLJy0m2n2iNQvzIA7gFSBHe-e--j1Tswj5LMc30rpKDnLVH_L4Ha34fXcyJUSVz23F8k4J8RlLZQ-x8_WzJWDh96eNL7UGWPDH6zYADYglHk1mFlZtoOGLs3_7yjfmEq2OIvTkIkqwrhP0vw8l8BboYuM50W6wVSjHY3reuDbe6tEM_GiaSCkgyMrFPKClt5dsZ5VQwpnHqPRPtQU9aGoxS2Z-1DMv_muFCfxkjxfuGiZs1smr4E6ZFGlHfc0fX06ck2uibFGlLEoomrggFf66y_YHFc-gOVlqhAlTxv6UaYjgqbpv4Csj5dL5UlrQqai5JIIPFt2fUYlP3EO_lNQft6QrdqOcIK7v4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=cgLf35NGdpmvt0VtRMxOiX2a68B3NAQc4RE9GFhOgXeQJv0E_O_B8_9SqW7XoAcmfbXYJRZtCioEjcgpDv9maIeM8v8NH27DUvT6VCJpFsjMg5bI0_G2zPLt4BPnU7YemYK90hBP5EVn37RLZ39vgvA3EYKRWpmA2A7P2tohV5-bwKyeXaUqgxOogSbWmf5tVxTSDVK9CUERcCSup_6gqJjRXy1nTqVcI76gHqAOd8ACbGfVv9Hxqn2yxVcAhuGX3lEWamR4X7h5q7r7qh17IayJDobaNa0nx3szgVKL0AycLdO8-GpMOinTYt6f18GxBU9ZgsDJS75aPoP8yne00w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=cgLf35NGdpmvt0VtRMxOiX2a68B3NAQc4RE9GFhOgXeQJv0E_O_B8_9SqW7XoAcmfbXYJRZtCioEjcgpDv9maIeM8v8NH27DUvT6VCJpFsjMg5bI0_G2zPLt4BPnU7YemYK90hBP5EVn37RLZ39vgvA3EYKRWpmA2A7P2tohV5-bwKyeXaUqgxOogSbWmf5tVxTSDVK9CUERcCSup_6gqJjRXy1nTqVcI76gHqAOd8ACbGfVv9Hxqn2yxVcAhuGX3lEWamR4X7h5q7r7qh17IayJDobaNa0nx3szgVKL0AycLdO8-GpMOinTYt6f18GxBU9ZgsDJS75aPoP8yne00w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCNK3Z6zIjXxo5CSFCNCi6WCzfCQyYJg8mC6ZijSBDunN9t2yojzZkgdSZRkYwW2o63aS8F9WLFK6GPp_lpXJiZ6yLM4h-_wlbISuIj_Z1jrGuQtOFR7CFgXHooZN9tiqOxScQRGns6zRvQ49X73trvmPyFWJotRf4VZcJ-uhAYB43bDIuS8AiWYsRKZ2bTxukVj088iYs6OLxXaiN9coD7aQ5Z_uqum96XIDiTHmJ1H8FUaXD9FJEPEZ4xKXTduTsoW7MPRGgHbZLb8zdRv9PFKq8m6uz0xQLiLXzhhGR4MDGJEFyAAum-dwI9mFvr9uvr3tbEy5NnahYfIi3EWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJaXc66nrVEOs0il9j-R3AIJ-GFmW-mEf2Q2vovyWPdTOkzyfwS_ye2g-kjoXqHAy0P0GR6a8Rp0h6S-f1_8U4o3Va7EQw-GOyeLnip1f2pAbM9x9fGTuBCJ-0PQjHR3dbQl_O37bFO3QenjzTniH5MWGSOgPWyUiVu_PtW7oVQaXtmZZqkoOcQaG_92dV1NaJAOqNtvBkLSC2lIgH77YreEqXewrWnXezsqjvIx1IAvOO2MXJ_wk_1aVM1IHIIYOvqpE4E6UfdgTVv_XnuNaYcv55ULyBRqSxmqiO6dhcV2gXthZ0lJu44lWc-Yg7l3eFm1KDfQlyrLCUyImoX9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAUPAOO8Ei03bUSNb2SIodiE9VhLqosS9X2b9KAsOUaJgHy-pWyvRiFE-OgGXnAgTJO8EIpAESGSJKozFvhbksQm67x0dzcbmD1AzJINT1fdrF7VJCCkHbLylS1-JErhcmVi3n7z_uarC1kc8SSsHSQoV3Ldr2jN_iwY4VJBHOR0cTtWHAwUzAvIl9irF8PGEkgPd3yBHa3SDVVFrIroHnC7EPBrJ366s2FGiCQQlCFr38rUHGM8Jpz7I7xVO-wroIP5uK0Q-HEbPXJikFGpoxuWgG53gel3nj7kwdzZZp4ujuQ7LZ1SMmiwnIdqwGffGE00NclJwCsPsn5714UB3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JkdQz8Vn0j8_6fG0rgxFjMuSaN4UpGynnlna0JwpSoPi_QnJdaU4KarQMpKuRiibsu-rEqjsOjMJaAn_3Q9Vu1rb6yv7BHrwfBJbagi5tT2Mk2swYw3g7_t0W4R0UGrdpk6tvevEr8Jk42lsl9Q_A7JM2SIgwRJ9qZ-ifq2MwDA-GaW81b246Zas7mjjptzm3rASFkp4r3Jt3sMIEALnrp_udo_tzt1BQQXiNB5iCrGHqzpEzgZn9Yy9MG8EW0_iALT8YwYFm0bMAAhaIvp2G7OxSNhmsGxc5gNc3BOI5HLE5jF93xKlr9pvzz4tYb0Iz5sgy0XJK6BQiAPc5CDdUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JkdQz8Vn0j8_6fG0rgxFjMuSaN4UpGynnlna0JwpSoPi_QnJdaU4KarQMpKuRiibsu-rEqjsOjMJaAn_3Q9Vu1rb6yv7BHrwfBJbagi5tT2Mk2swYw3g7_t0W4R0UGrdpk6tvevEr8Jk42lsl9Q_A7JM2SIgwRJ9qZ-ifq2MwDA-GaW81b246Zas7mjjptzm3rASFkp4r3Jt3sMIEALnrp_udo_tzt1BQQXiNB5iCrGHqzpEzgZn9Yy9MG8EW0_iALT8YwYFm0bMAAhaIvp2G7OxSNhmsGxc5gNc3BOI5HLE5jF93xKlr9pvzz4tYb0Iz5sgy0XJK6BQiAPc5CDdUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_P3azebLg5kQcFkWPL5ADwo4YkD7edtSlKC9A_HH0w4SheVmt-jdKp6RP2TjZUFYDqG0oSIcDkwh85KSX5ITprNeUya2rFzKTSVidbyCwng06g5qgo1r7tBbwMPRaUxRM_H6ZtEIR95tKlSOKNxMT59Ovwp39jvDxvDcYtmUrBFxL0DH-YfxAoCm0VG4jLkANCVCIBwD8xTgn9hmombyUJUjjI0Y_thaLrVIVH97Q84xpcEW-uhgMS5PjD6v6X9eJOQ35U4tfD-PX9oQcaVvjR3fbMtAnqsTEfnXytTwQEhqB5EJOWXomk0Qy2WKEiAxYLBtBRBbqNQQIHsB_r-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=O0Lv7hRneEAl_AgUkZKzCoDZ4HANqKQb1ZQH15PCDgHXZ3K3jBRrHGHwjI3Z4he11W31ftb26eDL_ku_T3JmWKuWMIOGwBRxWY-DniCafLr8_jkZ1oGC70B8WYE_I1k0kUInmuOue-kucaBWzDk0pUQSrIghL21AntfdA3uXw80dhWG85mu1m9yMT1UifBICvvd6R10HcTUW2kRZVd0i9lx6GIP6pUkE15EwLFgeBVCP0sDk0cQpdto9edLzLCWtwNknSr6qCpkRiAU2U8fMw01EgDXFbvxThziejAYM_-ZKch0_ZsV5hh44k9667TcDj66irvhwYTWz_a6yALYUEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=O0Lv7hRneEAl_AgUkZKzCoDZ4HANqKQb1ZQH15PCDgHXZ3K3jBRrHGHwjI3Z4he11W31ftb26eDL_ku_T3JmWKuWMIOGwBRxWY-DniCafLr8_jkZ1oGC70B8WYE_I1k0kUInmuOue-kucaBWzDk0pUQSrIghL21AntfdA3uXw80dhWG85mu1m9yMT1UifBICvvd6R10HcTUW2kRZVd0i9lx6GIP6pUkE15EwLFgeBVCP0sDk0cQpdto9edLzLCWtwNknSr6qCpkRiAU2U8fMw01EgDXFbvxThziejAYM_-ZKch0_ZsV5hh44k9667TcDj66irvhwYTWz_a6yALYUEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=bpV3k6iF1yYtXcpHpwOnz6L7KL7WreBaILOxZ-iEphESWkI4Z0HgaT8BgEaFnZp3YXIu45g0wMC2bSJD2Y_ZFnrVcNywPeyJr48rKjNg_reEgcUJky4z9By7KXn1PeCbRPgmieQcj2dIKvy4WavNlKsZX6uIXzXawz7IMDbC4ZUUvNscjKhaGl62XZeB62n-VAN6HFKs6gVzITw4VCiyqYIezKcsTDOQpdEINFgef0OH5Xf0gvmGBfJ31Jj_tOjWfECQ3PxEnhpesiGmYPZZKydYbLIwh-BuvnN5NyyNiJte4sMfAlkY_s20oa43pPjuVjEfspJelQ1U7k2x1qBCpK-xHwtWANVzGR8c4LoADYmPSMhTe0csWgjhFY6wtVPFopRXUD54P73QXlEkmnxYCOrFW7VaILkGZd5vwI0gBn2vRR_21ABw_zMBhjC0ySe2eITnG5Myr0lagWCELZBS7dk0fgqgbmQlNimEQwc7J4OlqN2osNtLr6jx3u88wvmLhBYV4ajeuYgKubioRmscgxe2o15yJwKGHNTwxGdfKrw9PP65WnFGPrd6kD5frqytkg2QRzBlqMfAkMvJCb6uthuFNR5_slYcbwTne28HHchtp7qVde_Z7JqFTOeTzt9ocD-7myekYUBrNrJxPll-ZT0WSiNrzi_ommA2ecYUHEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=bpV3k6iF1yYtXcpHpwOnz6L7KL7WreBaILOxZ-iEphESWkI4Z0HgaT8BgEaFnZp3YXIu45g0wMC2bSJD2Y_ZFnrVcNywPeyJr48rKjNg_reEgcUJky4z9By7KXn1PeCbRPgmieQcj2dIKvy4WavNlKsZX6uIXzXawz7IMDbC4ZUUvNscjKhaGl62XZeB62n-VAN6HFKs6gVzITw4VCiyqYIezKcsTDOQpdEINFgef0OH5Xf0gvmGBfJ31Jj_tOjWfECQ3PxEnhpesiGmYPZZKydYbLIwh-BuvnN5NyyNiJte4sMfAlkY_s20oa43pPjuVjEfspJelQ1U7k2x1qBCpK-xHwtWANVzGR8c4LoADYmPSMhTe0csWgjhFY6wtVPFopRXUD54P73QXlEkmnxYCOrFW7VaILkGZd5vwI0gBn2vRR_21ABw_zMBhjC0ySe2eITnG5Myr0lagWCELZBS7dk0fgqgbmQlNimEQwc7J4OlqN2osNtLr6jx3u88wvmLhBYV4ajeuYgKubioRmscgxe2o15yJwKGHNTwxGdfKrw9PP65WnFGPrd6kD5frqytkg2QRzBlqMfAkMvJCb6uthuFNR5_slYcbwTne28HHchtp7qVde_Z7JqFTOeTzt9ocD-7myekYUBrNrJxPll-ZT0WSiNrzi_ommA2ecYUHEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=Q-A3M-lavpNWjx2-ANMSOCVRcX0bBWnmLeA22ZNHBtd0icAQfxWziboThhfH_BriLIcPFz0r6uZGWI36TtRjuxWJ0Z4VnHSat2TiKeegFvtbl2GCxs2pmMgtCVgK8tt-nBcZXhhxoKD83Y5qG2hGWBZOt53YDxTBUZKscBXk1hITyFJWUKZYyFwvhP5crfg_0bsULcxj_jvN-98wtL7KWGoSjz7APoexjcY6aWG_fljLgBdcrIjJjHDgpsKB2ouQqY80qrNKBtcETEqvT8eUxR_btDCC7yIHkYY9Xc-ZkhXbs_0FjZpqZN23_6BAnr8Arzyd0pLygQClJQjG1ZQcLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=Q-A3M-lavpNWjx2-ANMSOCVRcX0bBWnmLeA22ZNHBtd0icAQfxWziboThhfH_BriLIcPFz0r6uZGWI36TtRjuxWJ0Z4VnHSat2TiKeegFvtbl2GCxs2pmMgtCVgK8tt-nBcZXhhxoKD83Y5qG2hGWBZOt53YDxTBUZKscBXk1hITyFJWUKZYyFwvhP5crfg_0bsULcxj_jvN-98wtL7KWGoSjz7APoexjcY6aWG_fljLgBdcrIjJjHDgpsKB2ouQqY80qrNKBtcETEqvT8eUxR_btDCC7yIHkYY9Xc-ZkhXbs_0FjZpqZN23_6BAnr8Arzyd0pLygQClJQjG1ZQcLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q79-CR24dqCEnQZlT6zLThr0-4CcRErDX0fwltbEVTkwlLPGQFHPTF9q4EbHB-y5a_OAok3sidLpb2PHwnDuooJfLeqCoLWQCEMQRcCrkxVSjh7xKjwD16Va3INP0YLUp1bgkoWVUMYWxTBpvnx63bWhVsIvqN3JZoujEzcyBSqP6lQhzObromTBceei1K7rzn3lMr9kMjnsFHpGLabbn4Pdz_bmAdAaPPdFGhIMfvqQSyZLZ5v9oVocrEXvmyBZmt9I8JGgNTYfQLprBtLLlRff-bE3jBB7az8J-bNu4tUcXjWUXErrea_-dIgXO7zXkRPE48IhEY9fQSXOzCVO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=GaWunwtEwI0CLcnahi7nMIVgcZDkH6qW_tTIdzP6FUBq84ZmN2wvwsG0LPUGY_COX4ZiB2nJXB_RJDwnYgd5kp_C6kkwtuEjhYyNYO51GcNmnpy0-YegQtxC-p18K4KvOlyKupAk9kp2fb3cenCx0-5Ewn9Mb9C1WlgLaUDyttDAk-5GguZP2u-GbP9fRBanawQgmt4YHNEmJoanBPcCeduFwpVJY3NB5PzORw-VjpIDZHbn1qfpJUbZJC1tjdNr-LFPVruanLeTsI1iqi9hStdBtWEIPcx0np1wxxlo-dEqP9tj7Rimx_WV6WS9sBpHaQvvv3b-Wap_3uqBKe0E_QL1Mjiuc9GlnaBkfj6WZZCgzjed1mRDGR_wL2DAc4ASC5JV4Y_FsSbB_O4IqopQxBj5997DXDucZ67mCOPJuWGk2zlXr9RNt3VoTO2nVkLmjutesYwztP51fOrNopbPN-7sWVr3gAbgEebyMF1vhhe9TGZqPJrJcSBxO0TRvOp1GLW8nu4SrQGKJSfA_ASBwbO0nXLRAjfG5zJ4vr3ALCTH_vo0S57dbVGBVh0HogolRCm-uvQoaxtaPPcfOHqYCBMootzwbyPilDnIV9cf0h9mw0fzdEeHc9C2Pff_SQA1yJPfQ06qFK_WVx0UiLyV42iOLtuD0ejuBuux06UVGnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=GaWunwtEwI0CLcnahi7nMIVgcZDkH6qW_tTIdzP6FUBq84ZmN2wvwsG0LPUGY_COX4ZiB2nJXB_RJDwnYgd5kp_C6kkwtuEjhYyNYO51GcNmnpy0-YegQtxC-p18K4KvOlyKupAk9kp2fb3cenCx0-5Ewn9Mb9C1WlgLaUDyttDAk-5GguZP2u-GbP9fRBanawQgmt4YHNEmJoanBPcCeduFwpVJY3NB5PzORw-VjpIDZHbn1qfpJUbZJC1tjdNr-LFPVruanLeTsI1iqi9hStdBtWEIPcx0np1wxxlo-dEqP9tj7Rimx_WV6WS9sBpHaQvvv3b-Wap_3uqBKe0E_QL1Mjiuc9GlnaBkfj6WZZCgzjed1mRDGR_wL2DAc4ASC5JV4Y_FsSbB_O4IqopQxBj5997DXDucZ67mCOPJuWGk2zlXr9RNt3VoTO2nVkLmjutesYwztP51fOrNopbPN-7sWVr3gAbgEebyMF1vhhe9TGZqPJrJcSBxO0TRvOp1GLW8nu4SrQGKJSfA_ASBwbO0nXLRAjfG5zJ4vr3ALCTH_vo0S57dbVGBVh0HogolRCm-uvQoaxtaPPcfOHqYCBMootzwbyPilDnIV9cf0h9mw0fzdEeHc9C2Pff_SQA1yJPfQ06qFK_WVx0UiLyV42iOLtuD0ejuBuux06UVGnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6178">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=ZVGI9bmv5PDtuYMmqMtdlNywaoJoq9lc7SpazKZKjtG5JrMZ8P7vAUWICBC4mRDb37Lk-9go6zUJ9giGrsXh6qz_qjkl4KHH_W5SzB8AmT-cG1DzcFu5bqLuFKxWcBWV3NsnNh5fw8iNV_bYMGDzxKhOz-OfSxriPgf7xSPfn8xA-n2Bl3WkF-AXYsmpmzsiiStXq1TWSAQElcOoXYOdYRT-NyEeNs8uaaM1Buw2iEGO0kMqXmMPcWqGtZG5D3_scQ5kDMIN_VtK2QsmK64PH0wSy9-Q7o_JjFkJpU6rLyyM9SHHcO5252tl_QD1dAaSnMMqWqV0sUi4SEA3JxJdaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=ZVGI9bmv5PDtuYMmqMtdlNywaoJoq9lc7SpazKZKjtG5JrMZ8P7vAUWICBC4mRDb37Lk-9go6zUJ9giGrsXh6qz_qjkl4KHH_W5SzB8AmT-cG1DzcFu5bqLuFKxWcBWV3NsnNh5fw8iNV_bYMGDzxKhOz-OfSxriPgf7xSPfn8xA-n2Bl3WkF-AXYsmpmzsiiStXq1TWSAQElcOoXYOdYRT-NyEeNs8uaaM1Buw2iEGO0kMqXmMPcWqGtZG5D3_scQ5kDMIN_VtK2QsmK64PH0wSy9-Q7o_JjFkJpU6rLyyM9SHHcO5252tl_QD1dAaSnMMqWqV0sUi4SEA3JxJdaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=QNjofO-jSxjZaieYf4e2RkfWaQt2S8WojZPmtN-soh59RZkzrCAdPtHo3CDdy7eCYB1eyPdfcoGVcCqnq628AZqEnEFWJ1hvY7BVE88tvOdz17FOaAt49D-QVBA6Gd4muKv_aNbOYLTTC9lKUjrPsYvx25D-0pYnc9rq4yjKV0AXlWNwBTmQnnADJ370_Jc5W02IBYisuRe6EqahD2E7t6DqZdbu2XSoyG4Nrl-Hfj0CkXcPHqzhsPOCgMDOYqs_7FOLs0SxTpo6uDDcgcGc55xbjkwUfpSdHsJGKhLFjDp2hKprNDVKv6JweakImBMN9MKmw36FYTXi0MwxcMn6_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=QNjofO-jSxjZaieYf4e2RkfWaQt2S8WojZPmtN-soh59RZkzrCAdPtHo3CDdy7eCYB1eyPdfcoGVcCqnq628AZqEnEFWJ1hvY7BVE88tvOdz17FOaAt49D-QVBA6Gd4muKv_aNbOYLTTC9lKUjrPsYvx25D-0pYnc9rq4yjKV0AXlWNwBTmQnnADJ370_Jc5W02IBYisuRe6EqahD2E7t6DqZdbu2XSoyG4Nrl-Hfj0CkXcPHqzhsPOCgMDOYqs_7FOLs0SxTpo6uDDcgcGc55xbjkwUfpSdHsJGKhLFjDp2hKprNDVKv6JweakImBMN9MKmw36FYTXi0MwxcMn6_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpSvfsAuNIVNzUqP6gEk4UjWmUnMUErz7iYNFIrC0g__fQIZYt8ctl9w-WUF5wCHyQQCe_f4YKljND_3SCdBSH8Kc2hcsQjqF0m7K6EP6JcoTbcGY4_TfH7MOLcCod2G4-Y99G8txq_nacv-BScjPTbgVlhzWEDbWBfUT2QgXVryQ4xAUwe4GO0Dlzu6uw6d88uxiwsbMORnw9iMf5kmigxxY71sN5sJn1GSfvtWGFZn6TmaCMEs1TQc_et1Q28OmvArpmJhuWkD_rpJuJ8qxlywels6CHOvu77l6p2hp-1I3oiUiqClFZarDoxuLBAAVZkBc3wsGwPCG88I_GkS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار - شیراز
🔺
تعداد کشته‌های حمله به پل‌های بندر خمیر به ۷ نفر افزایش یافت
🔺
تفنگداران آمریکا : یک نفتکش ایرانی را توقیف کردیم.
🔺
دیشب برای نخستین بار جمهوری اسلامی به خاک سوریه هم حمله کرد، هدف : پایگاه آمریکایی در التنف
🚨
تصویر : آمریکا برای سومین بار به برج مراقبت دریایی چابهار حمله کرد و این بار آنرا منهم کرد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=R9veKlqG_Ri-lryR5A4_KYwvwDFeCzm_Gw-qttuyaMfbi8kpJaj9g_lsKU7KwIlzju8-Og8CKXlcNzfOUqs15oK_UR0U1Cl6yE8_oLzNsiNXbOnWAeZTBscVaU4CF7aPv5k_BunJO6v318JHaaVRLqWRTzi709f0LYeJgJp1lfGt7DlnwpULJlZcumO-hZqeuRx9EwFpVRom9F-euQ3DiuVx8GsCvKEXJRkbVs5PHvhl-WwBw6TSEzYJqtZuioezHe52DXddNmyWWPJF6pWfjtsub8J21CxS-T7S9BODyu5oTKNLA8VFrhqdF07Zw_14GZyVyXf14QIqpYWLc-vdfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=R9veKlqG_Ri-lryR5A4_KYwvwDFeCzm_Gw-qttuyaMfbi8kpJaj9g_lsKU7KwIlzju8-Og8CKXlcNzfOUqs15oK_UR0U1Cl6yE8_oLzNsiNXbOnWAeZTBscVaU4CF7aPv5k_BunJO6v318JHaaVRLqWRTzi709f0LYeJgJp1lfGt7DlnwpULJlZcumO-hZqeuRx9EwFpVRom9F-euQ3DiuVx8GsCvKEXJRkbVs5PHvhl-WwBw6TSEzYJqtZuioezHe52DXddNmyWWPJF6pWfjtsub8J21CxS-T7S9BODyu5oTKNLA8VFrhqdF07Zw_14GZyVyXf14QIqpYWLc-vdfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLu-EaLEzZ_494vTInpSTFupE1kPfl_g8FYlkfuAFKI5lFn3mAWh8LWaPfyuQ5YqnYhlQWS5LE4GM38m3v5VIsoTKFl0Ufag_S_zkXq3GSpMUtjq7cwR6xjYtOMDbaEqXct_BTQt47nyEkTe7QR0MAI6yZ60OFCukrtlEtfk8Ky6VRwJjhwSTHOcRs_MeFAq3LO7F_JmJQGFrXLqpVEbykpg7xeiAIJhMUbvRJ1jIWoYNOHASXhu0wHf_7J-tQ5Xw3PGBstiyy99DTvNHey3qFztWFN7WykqloMM4mnYlC4n3yD3Enuh1tV7SGLfeeeSfZLLfnA5wQijyqPlMbzfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=wBu2_cxKbHHYqHlECTJ-p6Us4WM741BPgIkKlBjp2vk9ESU-1GHhh9F5R4O44_vsvGvTGvrp6P1a4UL1X_VSnMN306MiJgTFI6hvKmwm5RdJfMZzUFPDjQWvCGPK-R5sP4i7Bx1q8slwFMmeKGuqmmFMf9r3YYFpWGSeMYM6lC_LPBsxYJ8Aptwoiu6nixcS5U1Mb6pGUlGyMYROwFPvTAL-zUHY0YN_npxCuPqn_hu8m9xo_komJyHhRAXxoRK7RDh9uk-ABBYuVn1913PTLimxQw8YUFTJE0Inav8z6lJ48x8gtdKJhia4yYl7mJ3pCGs-nQPA-gdWr0_6I7kc5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=wBu2_cxKbHHYqHlECTJ-p6Us4WM741BPgIkKlBjp2vk9ESU-1GHhh9F5R4O44_vsvGvTGvrp6P1a4UL1X_VSnMN306MiJgTFI6hvKmwm5RdJfMZzUFPDjQWvCGPK-R5sP4i7Bx1q8slwFMmeKGuqmmFMf9r3YYFpWGSeMYM6lC_LPBsxYJ8Aptwoiu6nixcS5U1Mb6pGUlGyMYROwFPvTAL-zUHY0YN_npxCuPqn_hu8m9xo_komJyHhRAXxoRK7RDh9uk-ABBYuVn1913PTLimxQw8YUFTJE0Inav8z6lJ48x8gtdKJhia4yYl7mJ3pCGs-nQPA-gdWr0_6I7kc5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i21cccKn0FvC-BjhGJklvqT4hermG08_JVq0nvt2MyFM2hmecLXu7s0pHPB_8TC2ilX28LqtW9X2lM8gL7JfedMuvK2NoD0P0--R7x7lwIWSfqp-g4vsJqW7rvrE59dDeYT4ZfmnczDj8DQfS4SalzAzsM5GiYbE1lHNuRxB4ZNBTCAaaK0xOmV9fCSUS18zC4rJ_gBXXOBGRCIrJ5LQSA5MUaFh5ZUzARoJMh9F6_HXbjHIjWAXFnpMPqgdZKTmwpXgfG_I97BzDCeteUpiikBV7i7kZoFdz6OXsdr4nadpyr7p9ckyOyvS6iRw5s1SvMn_zoGFPD8911J0KEIPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اهواز تحت حمله شدید
حداقل پنج انفجار مهیب در اهواز
🔺
انفجارهای مجدد در بندرعباس  و قشم
🔺
انفجار در بهبهان
🔺
انفجار در بوشهر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6167" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6166">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=OSztCEuiJ-oq3TmelzBTgqbi_2mZQA2j_na0JO5j6pI_nq3nt2w9jWibiwVIT-NUC7gTeI9npO_FjFexhWXv-zwrISKcZNg_dORxBYXzYYhawLlqC58Kcdbkc41IpNZ1HMogcybxJBPM783n9WjfAhTxEthIsog6OAeHXyDGCDfzD8aIjZ8obKI-D1HhmNCP6xbfo3lRqw5y0KZZjBAMInFG-VJ7OpUyV6bd5dFuVbtQ2iknZlgFe7MvkdvZTK4JpJXz9T-8cNrs-tL2gUeHOJOIl11YtJD9DJP1pkV26mvz43CmXle5vauZuoOCtxZIjaJx4K32lJGvw5hvjtylyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=OSztCEuiJ-oq3TmelzBTgqbi_2mZQA2j_na0JO5j6pI_nq3nt2w9jWibiwVIT-NUC7gTeI9npO_FjFexhWXv-zwrISKcZNg_dORxBYXzYYhawLlqC58Kcdbkc41IpNZ1HMogcybxJBPM783n9WjfAhTxEthIsog6OAeHXyDGCDfzD8aIjZ8obKI-D1HhmNCP6xbfo3lRqw5y0KZZjBAMInFG-VJ7OpUyV6bd5dFuVbtQ2iknZlgFe7MvkdvZTK4JpJXz9T-8cNrs-tL2gUeHOJOIl11YtJD9DJP1pkV26mvz43CmXle5vauZuoOCtxZIjaJx4K32lJGvw5hvjtylyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
🚨
🚨
سنتکام: موج جدید حملات در پنجمین شب پیاپی را شروع کردیم.
🚨
مهر: حمله مجدد آمریکا بندرعباس
در ساعت ۲۱:۳۵ نقاطی در بندرعباس مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6165" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6164">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=TIYfNq0XaMVPJzVDN0dGB8oa1e8EdP2h-16l1eyqYTaBWUrQi3SiclFOs_UuL_R868oaxI3RtlV7mphQa5H1yimishz7zaU08bumKUajytNxbl9WNnY8JL1_hkenmsRkvJimdu8wdHLsjl-NEOaCJzA2MBN_RaMSv21oeJpBqzu3sQZaYi1fMUbNT4E1e_QGe87-ttX88ZY2eUzQRhOYdSApQJAL4Ze4ZYYsLMryA0L2qGSdQTF9F9oTAzaL7kRkT7QlkEies_JeSN_cK57qOOMcElrNzkphsBVpy96ZDeCUSLUOun6w54G7o2i89v6Hk3SPmMPpi0-FvDMyAh0iBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=TIYfNq0XaMVPJzVDN0dGB8oa1e8EdP2h-16l1eyqYTaBWUrQi3SiclFOs_UuL_R868oaxI3RtlV7mphQa5H1yimishz7zaU08bumKUajytNxbl9WNnY8JL1_hkenmsRkvJimdu8wdHLsjl-NEOaCJzA2MBN_RaMSv21oeJpBqzu3sQZaYi1fMUbNT4E1e_QGe87-ttX88ZY2eUzQRhOYdSApQJAL4Ze4ZYYsLMryA0L2qGSdQTF9F9oTAzaL7kRkT7QlkEies_JeSN_cK57qOOMcElrNzkphsBVpy96ZDeCUSLUOun6w54G7o2i89v6Hk3SPmMPpi0-FvDMyAh0iBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
