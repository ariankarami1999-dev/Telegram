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
<img src="https://cdn4.telesco.pe/file/dki_9AGfKzqq05ffQ6hyBlKPwjQnZdnmOaaR6AHJt_Pb7kqUw4IALCfZVpLGbMqpdn1vTMJnDajQ7vnIbGbP9kP01RobGblvHC1jfR_pEk2xGsW0b_jC6btOLTZniT37jljGizM5L1dqRl6jUyinBSorGqTKhM5liv7fYdfpAReNq-6L5Tj81Aizyg-HGv6eVrUqlkxGRtpqpRdmagI2FU2ddA3oeF8gFNbfYcZNrhel8QaqhK0xQisb6D9Jf59G_ZG09Oz6aO1UWC7i-cGKrw0DA-iIOjAkQWCpebMGlJ_o5gjdteVgCHWpWNwWzTcbuI_jn6p2M86mpBWuMZJIaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 01:44:06</div>
<hr>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HOGWW58Ca8r-IfC0ijyKWBEbOMY0OfGjz7IobZkHa-aFb8m-FOHAs580oxjfI-FLULgtoG-ornyIyE6DwdizY-8jXfwlEU96jGIkjEhRK4-uB62C8Uu5FxtP6EM3yTYj805it_LJZM-BBU2IGV_xlASohq3YLaMouLrpXlq4FtHiw97YPKktgC_kN5p2NOltNH62ffMmoGfdHTK4ISX_vAd0Kfe6QcXpqMmstJ5pXI4LRBg_Jxu9qhLbRR6MenRjkUEj8p4K7e3tUIDy73L7ZcW6eOrH_r_hmBpUgANFCbiO-dcOY_CuyWzvk9QIU9TO2DfIrggBBt5vWDe1aHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDHceAws_DgHKJfPyxY_hbQFOKydTvRD8S_cgOocirT6Wx-ywl0KRXHQf6OhMNN3zocsp_m-f-qXQ5LsVUrIyAVJFqfaNc5rw6pss_ec7QVWAkSntWb2KwTWP8YwjbBOOMihz8GGAkNdJ8ch25z8QrdZado7tnLzBnW5Qe5efpv584P6L5_V7miT_QLG-SBABYenMKGWGB1YzjZ8woeN7pf2VImgkxl39Tm3qZ9YAEcN39WQJMSSSDCbPBI85r5LMCrbsCFz60xSY9D4pxmoZcKLUvjGJq3yRKS9pgyas2mT1tB2gou46k1MEs9KDv2QarRE2KF4-LjKR8PvP9KJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQTm-GORMQsHyoQA2Jfe9odBDfnVbM5wg4V5gYjcyBNcP5-N-mcPzn6CoE9Wb0cNKNhboYrr5VmCWpbBjgOua9Da7F7pXnc9pWvx_vqb95Pfy8J98qtAB8y40-DEhbThH_fxPQLv2PYX4I9L13zNe27kGLwMlHl-GrBtyRKIA5R91UYA6PSdBGFbhCoCpBOhNRMWNP6cblMKBmYyAMdgwixCp0ghnR92N84suRuHUGRzNK65D8nvMayKqteTQavqfCoYy5TsGTJYAM7_EJxKtZl9BRA_QIDnyWNICKImpt4obdRBKdmm2EDSgv7fODc27_CpxORuOeWjHQR4hFgyyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIOQVfZhz0XXHmouuOFUMaUiXc2QtDnpHgcvJ_6lMyLvPvs8vAbQMS96y4x7Fu4lDImcltyaeO8qcsieUdVVrjqKvLhVz07RWiYvEFnCkc5oEGMA-lLoYN5cDatcaY-zGj6oPI7Qm46NNOvRDBhCi4U1Jlq8OEUBy_4XnOo1zaqrfKEbt0K5KwyvFFMkdEg4g67rxaIVirQN9_0UIn_o8wFWi8hihh2gx97z3j5bs0XutuWDNU7b4xStT6ya4yX8-Ag8dIL_Q6WPFsMnI9tyJXPXa5_fgJOgJpUDHnJ7_LSTh7ubMeAxPL1wUlAXvn9ggmQQZSi1SaUNzFZR-02frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKb2WoAYB2BfZWkNY37IBbkbjJc4SIQ1g5XruVQSrsNKs3qgofww7iRVf2qoHSMHt6t6iMSSSuI5_6vfGuhUR14Gj-tuEAUG7WOMbKyyWwtPM770N2Kf7em2Ts-reWnN13h58cs7C2vy2zGJaFZBJg9S4K7sWOw2xdY7vpCzU8FrGrZBPb4ZBv2JGSw1BdmJmBzcJ5JxWICl5QqD8l_FZ-hXN96hAPs-knwNk1QmApMnpJMp45YZSZiJZLYuw5X3NAHMPzlMKAR0HCu4nBM-LypbT-i9VR58PTd4ID9ZsTDQmszlfFOJ-ihl0o_I2WCB1dabJaw2OWhHUsecid3pIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltal-iHqkU0t-EHVYH8ZhpAgiCYVDQtn3wBr7TH3XJndSFkvIyRCPZ7zD4r5YX4kbOKH1uxuN0aLUrdvaiiZTEoSzNZpoffNDc2_btwlxDopv2nx1EuZK7zQKhImefrntwGTuCWlVk8JL3jrKujqo28IxRtltUndl-jkDKS6HthSH3-KuA9yb7C_HZNa1CcmWzIbu_YSpKmlDbatnlbpWPi5RndPAmT28vdaaz_DHYC652KN-h6kuBlgGPP0mmG6N1O3jrbzsdTdyzK9fn6dqim164x3MJ5s6xVPdUukpyCJQxYlLT0On-Pej-4U6cNmNE8H4PAstP0gws1XZx8qzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCvSTOYx0zKLF6l_OFyPakkn2mIljlAQ2ei1ijJNIOnMpO6xaZnv4HyU4NOOPb9DsmNH6A742oDAcg7myl5cYjcUh41dcTXPkl9NQ2ttOaIYpqXYhnwzc0ojH39gBYH0zKrTPD2GMgmwLRLIXNn5lZxeBhwhDrZbu1nW9caz59WbNV8ZpU-MY5tl5E8ajtUmg0QZjFeJ8eYR-LMARvphq0A4xgENyxI33uCge6fS5GDlw5svNmLNklBik2fhNgL2MpIvrBv1OJhoHCxDez6Uv_t6t6Xxurhw7bIrmsSO4uTfKGLbZ4ofTk7ei8NuevxjRE0WCp3yNGMGSXOkXU-xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuBAHLtebmp0i3zJGSC5DvPZLoX0F73DMm9ioklhszLVkTkQTTk7Ib6Y8n0sW50riJ4q-AXm3cOCek1gjlGdlp6GsdkJg4NfLJURDqngcNydiTooRjcG2OvbApBBXj6_rv6BXOT4qv5ZrAG7nzgi-hjSi1Hzef8m-7sFMZElJIU_6_x6ZoIbRBEinOBXPdNi7H1q-4fGeVbLxjPe8-kYr17fX4uxSmgV4lLXgS030geLc4v1hkkxcFTRdn0yBfFJ4p-Mqm1W3Rm6JqMK85quCs-k5rzVomzbggdxg07eI_XnruxRUNW5_u7eDYBpwyMsNKX392qK6JTH2RFBhBsV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaR9NCTrwfD3vNOBPEV_S02tSUAQxGTHYsaGqTZe8cxl3XZbk6-NYz9zE-j6TFbqoxXv4HH2e7VCHv88NCoIaAFhhf6afjvkUnMhtaos6_FaGu0E9qYBfZdAxwBL0Q_ffvrCzzWZmpOokMqfNNk1QArR4ja7PYyqgsghhU14YdlLRay263UIv85n1mSM-JY2k8eUKV1DEH3gpxS6vfrU1ljhrO1c7lHjmoqzCWRnc6AkVi5Vud_EiBR5HYC0_54Y9Go8yRMPJJ2swZ8500mFr45cUI7Zgu-7YnoG9dvg4MW0nscGvycALwwT_929FBdwfUGUPLOs4kHg6VnpQ7rdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8AZRKGj9Ovjcs4h8yJ0X4lk3H6JO8mZlo9-eJ0PDvHTHc3fu293F3OkD3p3WHQkwAVRPJnki3eEJzHZ_KAscF_JoNunjtqU_NjvV_wsDD-Ylzs_BNhueSwTznZR-rSmymsON8OIZSBXs56MTJ75DFfJen9VVnbxhA5loBmTAoZpzGxftCaKqeI-QG4QW6mE91DmkFsqKFinGqoecs6ZhJfwVmu3ATmyDuahB53gWa1SJ1Gh7JtiXbeFqRpT-vIHzlKOuSYDvwu9dnuhkNzWqjdo0p76I2AdpPbKqmm8QSfE1e5NPptmJeGMggMsJMpesnwqwMkqrzV-4J85L3-ufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta2xgiXeqD4i_-ZzEynp1yzcUTDsCHfyYCsKBn3mtm7MuYfmHEAr-QhhyQTKth7KI_Lx7wK8PE5dLITE9eqsO1oLcOigIMxz97lQywQxYRgqZ89edkpqSd9Kp1A4raUVYDnwWKn7niQ0vu5BqKgpep8XSbrAmh_mZ9Sw1htaui6dwL4wHqPr2Wr01Y9T80FRBRuMvqZOM1zUt8EXi4WnM69fE7NRLAvamBfP7FTf5GoU0hxqgD1r-lxcqvGh3fOOuaBXPuUxQGKdSC0RPd_IShM7RVnuY3EVWTrclYvagiK_6S4jrDz7SX_CcZAIat_wf8wXznBf9KqJVgdAqomVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiMjhhhtrO2LDBXF0H1t2qc-wN62OC_RpbEsByhJgtWePdj5CQqrv7Sipzgi0oKNX4sY_78VrMaAIKU8QiJ21qrHE9A814YiKEYe9K_CNTlU7Q4KN6W3VUlh7A7pMuHJZt3L85ZiIqwAquKGkEr5GavINnUIO3-hWPp2CmTEP-EmimAAO4j_gJZZjL_OmgHzSUEtfwdAk-TWdd5V3m97Wf0G1xWJtrxAbJFKpgA37VuuqDTPMk8NxEz76HF34EvKOKMa_gWOU3ZHBOBXewJq1sHSUEQd7X0N6iSBSY65SUQlfR9Bh4xWMddxfyIfkot75jZoCvRw11U7pXsTU37vAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqR22pa6JNorrkNN4pM7gPkskMZNXubaQ4wltAfDKwwnEyo-Fre2zbDX9KDTgDFFXXWxbpKm3_FzcJjukmTI0iXF7k1gjWTYnRhp1QN3WUgJzCHojwphXAWMi_A_6UH357ghz15UB2W-ZQtUqj8PltauxDdY1uniahT2Me5s1FpFgnVpr-Z2KpulNUyzrnG68yhn6_hUrOyTsdiUR-EfADUozLPfAZvR98d62ld1CMuHZ6hAGWi5QJJchcwx0RA44-qb56c9DQQEvuQXdCqZn15YdCKjdJ3LvZuB089LlZKa_suYjgMY2fG6nfCms21jf6Cn4E7EHuroe1y0StecYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx6xn0t5B2pzvzdzhq7C6sA-clatOxvUO_we0RCLbwcao0e9ETDb-HqW_5cKgHCKeG9n0j6lj4iRMFzTPvK-o_6uz-cgNdwq1aPvq7FAL5hf0RI4n7TBTAutveylXsMJT0ZM7__w3sv3bfMhjg0goTbtndcqwUF3kWYrj6ge4w6fY-3oNdN1NbmZke1-AMEuP_ewH9zwyWAGPjybDRqh1VXDHrwPH8i6LqaMf2juw4ivmyE7TUsjOp3KHkWseknh_7W--jQROI4tGAj9d3hnxGl19ipIbwuwRGolTjMMBLcQrQ8sC7Utb1MmraAWTYrGE4D27LjhcV-Soq5zXbWRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrNOt-CW2L5JLjxkZKkgl8EmF8BmWbcUU2ZKxDBKHXoXj5HG8dxXk4-6DSEvHjTjX0TSmxbfEeApMyrkSBOuiM_ZsdUqRQbl8STGj9VST-Em3rlUdt7ZfrAC3D6rzCF8O82XgMRsix1CcA1gc69Li53wxJdrvbpCUFy5_lvRNfmaYbRe336hXmbO43Ej_ZxY2N6mBmlsPGQg5-8AmiAGR11zPUNaGbw1FmnjvKjU77F9xNoBRgzikpZJZ9NiqLTeSpP1q3q0UelR9fbKjYmmLAwQZOTDaK3W9XfPBD4K2VrM3G4uSdacVqaeDbrTlq-RFPZlZqnNSm-7lLcROWs3JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxCatB0jEZlTHXZzCN_gBB2AV7Rmaw9dVBXoX5wvKCynPQLg_NNdCuX25SKWBNtSCkxHe9tPbsnLFZYYx46cVBI-UnXvnN7oAdSAgxv7pF06DxFtPBUfhnOZA2hlluEyB2CMuOlHFb7r1GsSxttJy2NSuxWN38sOBAnHlNQ3AvB-_V_OEblAqtPnnjkrmF-6AcDKAmRbOIwhmAfKs9yw3jZnKmQKMW37XfdKDFgzM0tHadWd7xlB20IKQGwoA8MX_DLO1r4WI6-uFWOV7QsUzUuFBtYmamvZbaHXjSwHVT0oCItCmbOwsBlAUe5CulbLRa8KhL12hscxuKMSN5eM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7gnYO1N3KnmJslW169kmCIPPsgaZ_sU0TchN47xJ-qts1cDGX-uajgzgmwgMV87ObY8Tc_egCJqB4CXBPgWmAEsCU8yCBvq_ePfDhkimIe3uUwZaIpMVZwjXbAWi4Ornn3a-Ie2XqFERKEW8fgORdZjzYfNA3AWecXzDXzlzXuK4lqZwuRc-H-x9yUbMk7SYR2V8zzL8VGThNtVxCuX9EVI_QZFOa0nQUA1wEqnWN2turSWBod0mzN3aQw9AovTCeSMn7d91YxDCOk4oVnwzg2yDb6YAEs5RGrfUboDRLSP067DRtoHd6OXTRHA31ROyUg6-1A5-6AQJwiblIxb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuNmZfNmved3fUp_8h7r5R7_970rkFlXtHzhqxWMz1ERczeLsj246i8ezuUJ1aew0WdcB599Gvy-V6l4cYp53qtVFxRl37FwS5woxyq-RlYs5jQqSmEVI7FYcOJzkS2OEqg5W_RBLpNKKIRcBxwo5fLIU7WiscS4KBG1VE3spZWTD5PQZ6jY30aDkxZMoh1pDucZK3L6nLqYXdNptnZ7e1lO9bSvBI_I73iaUVtBWmNOC4MsdMdJX0qmOhhS5EfwZ3Ua1xQgpbbM7-oDNUDV1LZo1HpXS65Z7Z9WmI8dW1vcHUP5Wari98lG0Z-88G-aDLwtejPXIVG_MwOq4Nazlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMFOmPa8PHoHLDs6ue1wTUFo-tlFgw07eLHEJed3SdOXvCb8PKmNul6NfiE-4NRRiMQLF5UjnvWhxdOKRdLwUwoYtqzPQ7yHhEkbpyL-vvPY8kfiEOHwDfncxT4cVvAda9xgAGmJFyT81bIeRhzUsG7aY74IDo7WVVYe-IW24UZ6HrXnpDUk21rr2qoRLbPxWTcL67rfnMp4VH7fTk1EmZ5d8DnRbmFXFG_EC-RgcR38x2njeRg4pgbOUSAs8tg8SQdVzWBEeVGaoM9ioq7CQK1wrntIA8XN-Xlc67QJJlvrBnPmPOyVK8pYCxvaBcmEy2mUA_hjjj2BTztm2uCWUBwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMFOmPa8PHoHLDs6ue1wTUFo-tlFgw07eLHEJed3SdOXvCb8PKmNul6NfiE-4NRRiMQLF5UjnvWhxdOKRdLwUwoYtqzPQ7yHhEkbpyL-vvPY8kfiEOHwDfncxT4cVvAda9xgAGmJFyT81bIeRhzUsG7aY74IDo7WVVYe-IW24UZ6HrXnpDUk21rr2qoRLbPxWTcL67rfnMp4VH7fTk1EmZ5d8DnRbmFXFG_EC-RgcR38x2njeRg4pgbOUSAs8tg8SQdVzWBEeVGaoM9ioq7CQK1wrntIA8XN-Xlc67QJJlvrBnPmPOyVK8pYCxvaBcmEy2mUA_hjjj2BTztm2uCWUBwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=cm2XE6ejB0K7p0DP-1qnTarff3DC_l7Me-PrPJU1uQcniWUeK0DOS130q3Kv-CgGGX4Uz2i__Pxsx8Z1e-w0Fd4OJFvZuGWkitIvzYR3AtKfiVR3oRtrdsFOBBq4Bma5aReafCTk4HhAW9Ol2-YJdyCgTW2hwneVjUyu7OItz3ATvbiSMu76Az3zrNnI8bcgRLxGE7jzIZa_j4GzhcZ6IStYL48Fw_t9-QMrOX9iuAOEpuCo81LMprtfQtCbPON4huPmcwwa92YPi7dMcwd9rhXWW5FPbOciAVFldURnvrEQst7mpZQUNgN4hT13t2t7mJA3z_kioWzZtaSb0NKn-LPgH8CG86M3EODdnp9BftiUskBbmzftgcvO55R4rP4xtrCyfZVCchkbJx33_OZ3GZoNvU7vFyYBUDbatre2OQFUsgV9TFS4k58rEnbHERUGHHKuTlxIRVPzjLkZp-uPSV0DEe8fgkERkVZcrFyFlMIwEqffuwX9DzQYtKEa-nlFG1ttUiwCFHuahGO_fc2D4RI8Jfi99tWr3kGTB4WUAmjMT4FTOJj7jlLSF38zjRrjkWMUWVubK_FpfSpYMt5CjiCQBI8p9IzgYYY6drl2zbPNYT4vjtOeCpp6FkkUTN74a6I1TESmPLONls10lxCQulh_vKIDHDYXL-pNs_MDm14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=cm2XE6ejB0K7p0DP-1qnTarff3DC_l7Me-PrPJU1uQcniWUeK0DOS130q3Kv-CgGGX4Uz2i__Pxsx8Z1e-w0Fd4OJFvZuGWkitIvzYR3AtKfiVR3oRtrdsFOBBq4Bma5aReafCTk4HhAW9Ol2-YJdyCgTW2hwneVjUyu7OItz3ATvbiSMu76Az3zrNnI8bcgRLxGE7jzIZa_j4GzhcZ6IStYL48Fw_t9-QMrOX9iuAOEpuCo81LMprtfQtCbPON4huPmcwwa92YPi7dMcwd9rhXWW5FPbOciAVFldURnvrEQst7mpZQUNgN4hT13t2t7mJA3z_kioWzZtaSb0NKn-LPgH8CG86M3EODdnp9BftiUskBbmzftgcvO55R4rP4xtrCyfZVCchkbJx33_OZ3GZoNvU7vFyYBUDbatre2OQFUsgV9TFS4k58rEnbHERUGHHKuTlxIRVPzjLkZp-uPSV0DEe8fgkERkVZcrFyFlMIwEqffuwX9DzQYtKEa-nlFG1ttUiwCFHuahGO_fc2D4RI8Jfi99tWr3kGTB4WUAmjMT4FTOJj7jlLSF38zjRrjkWMUWVubK_FpfSpYMt5CjiCQBI8p9IzgYYY6drl2zbPNYT4vjtOeCpp6FkkUTN74a6I1TESmPLONls10lxCQulh_vKIDHDYXL-pNs_MDm14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8znuryBIKJLVwNDDJAFKMt7Jm52qGAtVZs7DzCjqwi39zr7lYcU_DSh4JV7TIPTjUX_1-Sq_qz6kGiBAK0AU4mW9Fjm65FMGyC9yo-AX7knGwd4MLk0E_BvtTPH0a1B9oZUv15ET9BI_VBTFTPgpINsxUH_4DjeQEIxGZMQF6_fxl7Qhzhd_JzhtAGoA3JY8oOSfs95B6Pg1wOIrbB0cor423_afDbCTZ4iOnN357OsnDet54QV_CxaojQ2OOwPPFHBuaJHA8z0MIbcow-bOPhE0CCZUBIeRnAdAtb5zyvQi47xCREcfzmnSuHTeMYNm7lX51TPsbvI8LG6ITCcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=qULgkOyLKhEqqCg5OO_4MwBQeY9cvq54qiZPCxr3Bawzi__1GeoQ31H74aCVxLtaa6Lx2GdmvW0vTCYi4wdtQrnhMejrZxj5CudY62SClNLCQUfiWp6Q7LIB_b86cCw6w2J-em_BHyI0tB8baxhIesk2ql3rOG6-6yl895crMplBmuspqFBrIPpBY3ngNi3klRsf5PoIo4h4-YeomNG2_05t6E2n_UG8Mu-CITt2G_HWOzMmKw6vJrVHFNlE5t16ASttASZjZW6RlQiJBgPDRT9Z3qkXWospJKcokIex83Rg4zh3yezWXFj7otaUgnsOYmSP_bM-dVQ21jmitSqwTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=qULgkOyLKhEqqCg5OO_4MwBQeY9cvq54qiZPCxr3Bawzi__1GeoQ31H74aCVxLtaa6Lx2GdmvW0vTCYi4wdtQrnhMejrZxj5CudY62SClNLCQUfiWp6Q7LIB_b86cCw6w2J-em_BHyI0tB8baxhIesk2ql3rOG6-6yl895crMplBmuspqFBrIPpBY3ngNi3klRsf5PoIo4h4-YeomNG2_05t6E2n_UG8Mu-CITt2G_HWOzMmKw6vJrVHFNlE5t16ASttASZjZW6RlQiJBgPDRT9Z3qkXWospJKcokIex83Rg4zh3yezWXFj7otaUgnsOYmSP_bM-dVQ21jmitSqwTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=Aur4-aiZ8bwAzAmfwQhiRs1pCUaEywDsqnpySPGOTkSzIoXlyYwQEVsb5RpX76kRgLNdQ60jIwbfZFHYNsmk-f9YkbxFwHPgLBL8Ry8jZM1p4MT6sHjH7HGHa5O7t8kgGfXXytEEVuN4RWrB0oeQXwLHFXowxX35_xuopMa426rMsEio1Z8LsKOGgLoZx_gR8BjxgNEpRtagHfdMdwz1LF6WLgODNu-AiDzYq1DsmTV-8Jp6Td-zFHyinhaiG1nLqNvXWSWPRZS29ZF8cZvv276oR2-fR-V0z3GlgaCvAtVv0o78eoMP80HEVBit0Yk49cjCs9nmdQem9d7QLOtteQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=Aur4-aiZ8bwAzAmfwQhiRs1pCUaEywDsqnpySPGOTkSzIoXlyYwQEVsb5RpX76kRgLNdQ60jIwbfZFHYNsmk-f9YkbxFwHPgLBL8Ry8jZM1p4MT6sHjH7HGHa5O7t8kgGfXXytEEVuN4RWrB0oeQXwLHFXowxX35_xuopMa426rMsEio1Z8LsKOGgLoZx_gR8BjxgNEpRtagHfdMdwz1LF6WLgODNu-AiDzYq1DsmTV-8Jp6Td-zFHyinhaiG1nLqNvXWSWPRZS29ZF8cZvv276oR2-fR-V0z3GlgaCvAtVv0o78eoMP80HEVBit0Yk49cjCs9nmdQem9d7QLOtteQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgZnyMjr51tSicT2aELDEfKUjDbDBmbL0I3lS8KR7kKSoyFlXRoHzDzdxURPq_dcNjNsxerg35i1PTBqpe8s8Qw_sC_CkdIeGEBQcIvC0kddigHuQUsfloOhX7VIk9Tqsyt_fe3N7ss8_n2p9SDax8ycmncHALsarvc8r14J5mG0Iz67-wKrtpx0w7rrqpUpH4cN0J5wC-HWWAR-c2Oy7j_0myMH-zNcoLX9XQQiddbaIab0srlEztmlDPrWZGWRc3SiRUOdW4CFpgyKlsDzQwamX7IJfHN1ipEXgDlqwp9QqD4S6Mpi6v-6QhpKv_xsd-MmPE7PKo6nCO2OhwS0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7YKwpQpGBkUXSvOmLN-mdbpGvvIp7rfw9ZHneOVaArQrARmAOzispr_q5dsw9gg-t1bT5wg3rboIo-DQgzED8PspKuPlTKsHgnm20YyXDTOKZ7ezoHB9HTI-y4ChRY-Gvklo8UIb74PAFz-f6p9v_-sgExY5CcJWpvPlwzbecqopnMfas92tdoCHCm3ph8mkxfu2HR3YS5344G7ZjlP0lZefRFtq8SW3AgMaa-zB43sHp3QNu2TwBQfxqPr6SY2Kp7ErqkL--UXx6E_H0zPLRhpJdVEb3MmMbqLkfCf-52mJMBbdLWSvO0mdKXl_ltxRRclv6i3nX3Ad8H_ydTDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=Z-aP1T0cdDvT4fPnCR6mKekwokyzR0z60y0k0v3tQw_jD-oFO22uyND0O9cbq2RXKsk5Rz4DEzPuRqfex7QCMY29BYEg5qDvSXsMfctZvjX3uibvQzLDw4LqrZelDmBKqCezj8FF_h8wwnudKR1rpyXuhM7LIG-b2m36RQm5TK98BMcgl6F3LYW1xkRy4WU4XnTgGql9BthFnCuu9tve4op3ssYU6gvdonzBWWX1K5TfVpF8cRj4fm4Bae9EOTZz3lyAOZL6TaWnb3N7L3Yrf3OQVMwQtOUEurkxjnlxKHuHEi57sLNQjGUs5UhYpFj7GqYs0CoBFkMJfzVHIn-deIaPvub3jwCOK6hgi29bBpUx25qKHDRJrIzFpHqzcrQGSem5xp_hc9OOV_1uLpMmHC5fIdQj20oGIXeeQvuhVAcnh3uESA3hfPGUYjgz2pb6ySB6VSLz370eFhZ9_9ZgXjMPLx6IpOJKWzlP1hH9Jd01Z6aYngq6jCZs0cXIspr4UJfN4Ibi5gyZj_uzDhHOIMcY7Gf-mPSOPS5kO9aIvnXuU8H_c_d__LNe56km7dFTTb7UhmXPZAbgzJalqBzlUnmhqkqttqsLo88h7Yj_gCwZCbipekWBGn_j7sJEbQ4PbJA_x5G5k08KCxTO-0fFxzYTfdtiF66UoSLRwXVdVz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=Z-aP1T0cdDvT4fPnCR6mKekwokyzR0z60y0k0v3tQw_jD-oFO22uyND0O9cbq2RXKsk5Rz4DEzPuRqfex7QCMY29BYEg5qDvSXsMfctZvjX3uibvQzLDw4LqrZelDmBKqCezj8FF_h8wwnudKR1rpyXuhM7LIG-b2m36RQm5TK98BMcgl6F3LYW1xkRy4WU4XnTgGql9BthFnCuu9tve4op3ssYU6gvdonzBWWX1K5TfVpF8cRj4fm4Bae9EOTZz3lyAOZL6TaWnb3N7L3Yrf3OQVMwQtOUEurkxjnlxKHuHEi57sLNQjGUs5UhYpFj7GqYs0CoBFkMJfzVHIn-deIaPvub3jwCOK6hgi29bBpUx25qKHDRJrIzFpHqzcrQGSem5xp_hc9OOV_1uLpMmHC5fIdQj20oGIXeeQvuhVAcnh3uESA3hfPGUYjgz2pb6ySB6VSLz370eFhZ9_9ZgXjMPLx6IpOJKWzlP1hH9Jd01Z6aYngq6jCZs0cXIspr4UJfN4Ibi5gyZj_uzDhHOIMcY7Gf-mPSOPS5kO9aIvnXuU8H_c_d__LNe56km7dFTTb7UhmXPZAbgzJalqBzlUnmhqkqttqsLo88h7Yj_gCwZCbipekWBGn_j7sJEbQ4PbJA_x5G5k08KCxTO-0fFxzYTfdtiF66UoSLRwXVdVz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=p1t7XhF_i54LqgsEkjeig2SIa_u6tLiXR9CE7uIR5wNpNYd8EhOIPAwxGmFH1JGqVNNw7ckD6F1u0BhFB1uh6ij_STYnYbz-HvcbFAs5zfaldWpooJKr9cCSGFAdWqPICyB3YHuwCUh7B49OO7T4UwIQJi6VCaK8FfgYDf1i8D51gI2BbjiGyQdsMELGnMHF2MH-FG8FsHI16byNLEBoUxIA1sYfChkprvsI_BBVMD13G4SfYfSydqSE7Czmx3Vv7Wr32xugAGf477ov9qeogc0jDor3JkVC-suGatAXWanPcMR9wI56D7gHVygS_-kvpp2l7mdlJl3hoSk12f8sfpYeGSVMXSb1hm-Ih2bczjpShBq-vUhPnZm9KrfCwLRCPrR-7vklIvje6WSVRvVppcy49RhSNrWBhsSiTISfdkOoLajjsADttNHs48jh4LNFl-e885RvktibJPXmSxTU5HRBIRH0W4aTsFNAxAK9q6OqDQzJf8NgFZABL-wAhdZVg0VnZKns2snOW1gN76GLN1RKtCH0iZgPI6YlQcH8IS1XJEu6TabZC4dHeihNyc9YMixl1AIpEcFUhHIQQVbuNb4LdSKFpfN63cN9KQGI4kCYrKtYWEQnh2_5thLxrl_xcUhJZwk9Ibj-en4S_hqACMvuL8beRpPd3Wt0ymqbokw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=p1t7XhF_i54LqgsEkjeig2SIa_u6tLiXR9CE7uIR5wNpNYd8EhOIPAwxGmFH1JGqVNNw7ckD6F1u0BhFB1uh6ij_STYnYbz-HvcbFAs5zfaldWpooJKr9cCSGFAdWqPICyB3YHuwCUh7B49OO7T4UwIQJi6VCaK8FfgYDf1i8D51gI2BbjiGyQdsMELGnMHF2MH-FG8FsHI16byNLEBoUxIA1sYfChkprvsI_BBVMD13G4SfYfSydqSE7Czmx3Vv7Wr32xugAGf477ov9qeogc0jDor3JkVC-suGatAXWanPcMR9wI56D7gHVygS_-kvpp2l7mdlJl3hoSk12f8sfpYeGSVMXSb1hm-Ih2bczjpShBq-vUhPnZm9KrfCwLRCPrR-7vklIvje6WSVRvVppcy49RhSNrWBhsSiTISfdkOoLajjsADttNHs48jh4LNFl-e885RvktibJPXmSxTU5HRBIRH0W4aTsFNAxAK9q6OqDQzJf8NgFZABL-wAhdZVg0VnZKns2snOW1gN76GLN1RKtCH0iZgPI6YlQcH8IS1XJEu6TabZC4dHeihNyc9YMixl1AIpEcFUhHIQQVbuNb4LdSKFpfN63cN9KQGI4kCYrKtYWEQnh2_5thLxrl_xcUhJZwk9Ibj-en4S_hqACMvuL8beRpPd3Wt0ymqbokw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=jVs7mnSsOaTk3mtzZl8Re7H9uQcBOF2xLfjDYyPC1TweckywAgqF6_wq8qaPU1N8t1WL8rc1QxcJsSHt8s7XGyvNhJ-YYpaJdG6GWbSHMVxDzYjfWVHA9NVZ3DTXv8pfYKs15oH-h8ijA9XGFOu7XJ8QqfoOxLrc-MGt5zBflmcJQ3Ao2vWDnIZZ--xLUj_rzSmwJQV-gGsWfiMYGpj6ufmdqpdG4beWVnG-0VObdtFaoT4HGW4UKG9M7izIx9hGax9a9iu9CR9Fu8agsKRAXtpSCGXR6GHiAPTgaakC5kEj6HJYNxpVB1b8wr5WOn1I08_-r5l_pxhpma4v8NtHLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=jVs7mnSsOaTk3mtzZl8Re7H9uQcBOF2xLfjDYyPC1TweckywAgqF6_wq8qaPU1N8t1WL8rc1QxcJsSHt8s7XGyvNhJ-YYpaJdG6GWbSHMVxDzYjfWVHA9NVZ3DTXv8pfYKs15oH-h8ijA9XGFOu7XJ8QqfoOxLrc-MGt5zBflmcJQ3Ao2vWDnIZZ--xLUj_rzSmwJQV-gGsWfiMYGpj6ufmdqpdG4beWVnG-0VObdtFaoT4HGW4UKG9M7izIx9hGax9a9iu9CR9Fu8agsKRAXtpSCGXR6GHiAPTgaakC5kEj6HJYNxpVB1b8wr5WOn1I08_-r5l_pxhpma4v8NtHLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSosw1nqCiS-LT8aO2VKYLQJTQF-wV6cBcbmMu9i6CZBTkNGkLOP7Q8FSZDNil7v83F09GqlMykGIJKzGdkixU_96vFEqOc4as0zxCupMp42WQhMKOsSM5j1U6QKl966FrzhV8dRFX6M160eJRgpIK7FShSQnMwZE0e_xxEGcZ0g5qGgKQUCU2qfWvWohDe4qTgZaOktIMKvIpPBGfZ6eSSko0kCBsBacx5RlrR2W--PcWbZif4yqGPQu4jQBgbhBf_08g7mpc-NGpPKHS_AOqegdP0Uf-ICrjh682vxnL0ZhgYSTM-yHynN1mhSoLc2uNm1q3xVlKTN5ClAY-CFhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=ogtiqAPNTHPWuHqe_wEk_7pR0GOuXejenk1bbg6aZfsG9YKzU3jbHaEPQkx85mnYvgYF2EHGeSE_TheyLtAOZC0DDPaKuP790a6m_HpvlMYcHYF-VgST3JwSddxJ3LN0IyIgtCn0YEnsPgTTvVsQP7f8zptXHnbKhLOzUZsU0a6Ve2mtms4hiuXp3Rh4f2GvyZTQcPj_odLCwa3x1wikFhBqpbJpEL82LQcSKblX2gjdF7riytE5IgV98iAOpGVF1RtL6wGpqUMVIWsFyMwmjL--LWRhm7HmbhS2vcS5NSEtjK8w1zhpDWZgnkNtIv5CnAgx2lwnhiIFZYtCrTErcU1BGeAx2Zl1Y0jkweg_9M5vA6Gtnl_JX5FagYgu7c0Ejbc_sr6uq19v2Ftkh3linePPgPrKuNuwYMrVkHHP0g8tcOvb68hxsUSnmARnVKXct2-fvY7s_lqR4OuUD0IPAgxQ01dJq_0N6vz0ZMrSpsZJaautQLWsrpTS5Uuy94rS_seN4zYcziezPl9-4BvG88UgG63inL0pWxzyNAD47LkJVWbC43P2JMdB8H3QGf-lI7kx-enMO75z7d3TdXL42DSzUCJ8-7ap1zfBszzjtxNWAMM1LEilB88gm8ZZqqczZJjIDel2erWvYfM_BLFxXh9ANAqGNlEI3RHuxJR75-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=ogtiqAPNTHPWuHqe_wEk_7pR0GOuXejenk1bbg6aZfsG9YKzU3jbHaEPQkx85mnYvgYF2EHGeSE_TheyLtAOZC0DDPaKuP790a6m_HpvlMYcHYF-VgST3JwSddxJ3LN0IyIgtCn0YEnsPgTTvVsQP7f8zptXHnbKhLOzUZsU0a6Ve2mtms4hiuXp3Rh4f2GvyZTQcPj_odLCwa3x1wikFhBqpbJpEL82LQcSKblX2gjdF7riytE5IgV98iAOpGVF1RtL6wGpqUMVIWsFyMwmjL--LWRhm7HmbhS2vcS5NSEtjK8w1zhpDWZgnkNtIv5CnAgx2lwnhiIFZYtCrTErcU1BGeAx2Zl1Y0jkweg_9M5vA6Gtnl_JX5FagYgu7c0Ejbc_sr6uq19v2Ftkh3linePPgPrKuNuwYMrVkHHP0g8tcOvb68hxsUSnmARnVKXct2-fvY7s_lqR4OuUD0IPAgxQ01dJq_0N6vz0ZMrSpsZJaautQLWsrpTS5Uuy94rS_seN4zYcziezPl9-4BvG88UgG63inL0pWxzyNAD47LkJVWbC43P2JMdB8H3QGf-lI7kx-enMO75z7d3TdXL42DSzUCJ8-7ap1zfBszzjtxNWAMM1LEilB88gm8ZZqqczZJjIDel2erWvYfM_BLFxXh9ANAqGNlEI3RHuxJR75-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJaXc66nrVEOs0il9j-R3AIJ-GFmW-mEf2Q2vovyWPdTOkzyfwS_ye2g-kjoXqHAy0P0GR6a8Rp0h6S-f1_8U4o3Va7EQw-GOyeLnip1f2pAbM9x9fGTuBCJ-0PQjHR3dbQl_O37bFO3QenjzTniH5MWGSOgPWyUiVu_PtW7oVQaXtmZZqkoOcQaG_92dV1NaJAOqNtvBkLSC2lIgH77YreEqXewrWnXezsqjvIx1IAvOO2MXJ_wk_1aVM1IHIIYOvqpE4E6UfdgTVv_XnuNaYcv55ULyBRqSxmqiO6dhcV2gXthZ0lJu44lWc-Yg7l3eFm1KDfQlyrLCUyImoX9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_P3azebLg5kQcFkWPL5ADwo4YkD7edtSlKC9A_HH0w4SheVmt-jdKp6RP2TjZUFYDqG0oSIcDkwh85KSX5ITprNeUya2rFzKTSVidbyCwng06g5qgo1r7tBbwMPRaUxRM_H6ZtEIR95tKlSOKNxMT59Ovwp39jvDxvDcYtmUrBFxL0DH-YfxAoCm0VG4jLkANCVCIBwD8xTgn9hmombyUJUjjI0Y_thaLrVIVH97Q84xpcEW-uhgMS5PjD6v6X9eJOQ35U4tfD-PX9oQcaVvjR3fbMtAnqsTEfnXytTwQEhqB5EJOWXomk0Qy2WKEiAxYLBtBRBbqNQQIHsB_r-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=hLO60QzFqLXy4HwzGJOjRIUKgOsiW2pL1axokCoabEVIpO_WiQ2C02I-AV4StWCAd8w9CmMErjSeAhyDfYAc0PyDG1-CEmAmdHWjxDlFy_Xg1pW-1uz77FQgQ8mDJNXR9TjsqWbYsWNvtE7zRlr3qPnVI0Y1CB9NEfzzwYartECetuoNSeg_SQ4QtnwC7unysqpEX-hujlRnEFdZQvEhIwBCYydc1Sgr7I4gE5vXvFOnQ-TV4jj9M_lPhmIWNYkFmE0NBNmR-5Q_Vny4v8w99-vve1cStYuWozM2Lyv_czC8nFECSfh_ikig-cL-LNlcyXT2QmEyodfzDRqeW6wgBXd-DaJ1Z2i2LZAZZJrllYopk5hpiq9sDc-LGDE8fpxra1azR9CukbaSg47fGGVmPo14KnYbup5RdyoKytYdPclWwRiAoK-_yGbPDOI0q9YlxDdAac5RyFJ4tw7b3dynkPA8DIAylt-IS9JYqgOZJ7Ddt5EG5zFQkH5KOTKOt_pJQasBQpdwzI7fQ2L7iokbIfQtB-7ofhHQYgHYfoDBMoQWMnBZ5SB7xsDB2GFylaDIzlfj46qKHx7abBJPnZVfW2W_U1B_r6488YeoOFhN08nIXMpS-FzHxitSdtkTx-3A4ldTJDkdwgHmKLqDsxN1EesOl1woAs8ZT-fSEpXByWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=hLO60QzFqLXy4HwzGJOjRIUKgOsiW2pL1axokCoabEVIpO_WiQ2C02I-AV4StWCAd8w9CmMErjSeAhyDfYAc0PyDG1-CEmAmdHWjxDlFy_Xg1pW-1uz77FQgQ8mDJNXR9TjsqWbYsWNvtE7zRlr3qPnVI0Y1CB9NEfzzwYartECetuoNSeg_SQ4QtnwC7unysqpEX-hujlRnEFdZQvEhIwBCYydc1Sgr7I4gE5vXvFOnQ-TV4jj9M_lPhmIWNYkFmE0NBNmR-5Q_Vny4v8w99-vve1cStYuWozM2Lyv_czC8nFECSfh_ikig-cL-LNlcyXT2QmEyodfzDRqeW6wgBXd-DaJ1Z2i2LZAZZJrllYopk5hpiq9sDc-LGDE8fpxra1azR9CukbaSg47fGGVmPo14KnYbup5RdyoKytYdPclWwRiAoK-_yGbPDOI0q9YlxDdAac5RyFJ4tw7b3dynkPA8DIAylt-IS9JYqgOZJ7Ddt5EG5zFQkH5KOTKOt_pJQasBQpdwzI7fQ2L7iokbIfQtB-7ofhHQYgHYfoDBMoQWMnBZ5SB7xsDB2GFylaDIzlfj46qKHx7abBJPnZVfW2W_U1B_r6488YeoOFhN08nIXMpS-FzHxitSdtkTx-3A4ldTJDkdwgHmKLqDsxN1EesOl1woAs8ZT-fSEpXByWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=B9GcdKjyggJnMICDYEa67KmHjDLA056gPd219jeQsVkyS_HTZyTel2VXl1M3F8lU5frQnQu7kJZCKZtqRXHwsCLvJ3anEFugDQGlG54O_v2ngem_Up75PBRxXF8MzbOBA80YQgUGt-u1DxwGQHhconPiIh4Lbqpw_DwLGLSixpg0tBsRkyKs8zrXH54NAj-v_FQ3ty_TmWO6QvAI0iprqYW5MHyaT4dCXMXx7MJET_EKRRW3k3dNO7T5C2zk2Ro4fv8hkn6xx8Iyd11799OgqEaKs5TpEtHlMZjDnvx7cCcNImzjuE9esuWaCsySVCCNNAPlxH1axRri6gkV1wcDRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=B9GcdKjyggJnMICDYEa67KmHjDLA056gPd219jeQsVkyS_HTZyTel2VXl1M3F8lU5frQnQu7kJZCKZtqRXHwsCLvJ3anEFugDQGlG54O_v2ngem_Up75PBRxXF8MzbOBA80YQgUGt-u1DxwGQHhconPiIh4Lbqpw_DwLGLSixpg0tBsRkyKs8zrXH54NAj-v_FQ3ty_TmWO6QvAI0iprqYW5MHyaT4dCXMXx7MJET_EKRRW3k3dNO7T5C2zk2Ro4fv8hkn6xx8Iyd11799OgqEaKs5TpEtHlMZjDnvx7cCcNImzjuE9esuWaCsySVCCNNAPlxH1axRri6gkV1wcDRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vbdn_bFAWTvJZQ1_WD9hL6tZpJ0K28XxzpTVJUvyL62Gec7qX-dhoRnQka96FxAU2Q9g38SXc-DHBl1MxsfktWKs1WhLsMU2deYchjwsSTwphblXJy0PmIynONHqdtqGC9XvyxAct9sz-Vl6VyEyveF7ofoRjLTyPD4eOtNN2Q_UB-nHSlrszYf4ZBgtgLeNUlYfKMVMNqqbUamL6E5fbb0-z_c5yN3SZP2jYBPFxgfmOlPVN557tErzPSp7XDeeOh7Mv0RfY7JxEo0vqDXbl1UzSYT40q5F7cn6PyEdBgCzsJsWQVVDrbV_fC6FWACVt03VI5UxWKRqpg0UOj6aNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=tyitff8oykAm2-T-jjr7J2Ilpn0eZeZkVudH7b2RSK6lYcbDV7Zac1j3w4RwRkdPH7mS_qpgtoDFW0_XqwP1xIgClcZj7r_zTBQB0ou2l5QC5ATuhG_vbRkoVVFycK0pHZiBTZRQ95SR3mbBudRalW1emoOvBd_D8AcoK7knHLX2Hp6b8P9GB2v3dFJKqlO0BL-l6rPDBEyP_LwesZY-NP4KgYesQQoy3fM0qQ_91zxo27qPKfboPZNe3gXxrhNVRC7-wnrnqI5aScYQZdKua3h_fFYvwRN6Y-WjWlCYE1-0cUa18kBSkjMgjZx4hdxxLha3fLAHecRcuuUovloGvYUMKEQS04miMR0-LcjBxYSsD1K3uq8ePrYB0RayqDJLGUxNBfacF0T9_DVYTdBhVEvvJdMekKh_KYLviNySJNUbxEvqPx4YSLN4tIXXmU2X79f6kXEMgxH00vVL_siiFG2YzEZQ0Q4MxOHYJPRW1LxLpq7dDtFi-TrRtzX9wbLPLYnCSHWIYpb11zJi8nEcBFEhTnjTKDC1u5jotq_SDKwh1aVPlOOalgjdEo_nNKPb1Mj5l8rUq1eLk-hzKsrUX2Sp7kpPqnkoPXu7B7GKY4XeAbdS81iLASnRaU0KYY4fmY0ZUCCOt-ixbLEttKNxj90DmdsoSbqrnYGoYF6-reg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=tyitff8oykAm2-T-jjr7J2Ilpn0eZeZkVudH7b2RSK6lYcbDV7Zac1j3w4RwRkdPH7mS_qpgtoDFW0_XqwP1xIgClcZj7r_zTBQB0ou2l5QC5ATuhG_vbRkoVVFycK0pHZiBTZRQ95SR3mbBudRalW1emoOvBd_D8AcoK7knHLX2Hp6b8P9GB2v3dFJKqlO0BL-l6rPDBEyP_LwesZY-NP4KgYesQQoy3fM0qQ_91zxo27qPKfboPZNe3gXxrhNVRC7-wnrnqI5aScYQZdKua3h_fFYvwRN6Y-WjWlCYE1-0cUa18kBSkjMgjZx4hdxxLha3fLAHecRcuuUovloGvYUMKEQS04miMR0-LcjBxYSsD1K3uq8ePrYB0RayqDJLGUxNBfacF0T9_DVYTdBhVEvvJdMekKh_KYLviNySJNUbxEvqPx4YSLN4tIXXmU2X79f6kXEMgxH00vVL_siiFG2YzEZQ0Q4MxOHYJPRW1LxLpq7dDtFi-TrRtzX9wbLPLYnCSHWIYpb11zJi8nEcBFEhTnjTKDC1u5jotq_SDKwh1aVPlOOalgjdEo_nNKPb1Mj5l8rUq1eLk-hzKsrUX2Sp7kpPqnkoPXu7B7GKY4XeAbdS81iLASnRaU0KYY4fmY0ZUCCOt-ixbLEttKNxj90DmdsoSbqrnYGoYF6-reg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=LGQD4jM3IfH4bbj9gPjemDgj125jeXYAYWytWtFnGlcuJdtMXKsp1WVSy9Pe9nmE2XEiV0pZ7fa-mhY0qOt_vHByQJBfJ-MktEAYyj08c93acDyOt709HGEp_BwlgGw2G7_Pw1_D5QmLSR7VuHEaFKlvwUTu6Ok8dEwkamPE55hou5LSrjSqWf6FM0YGXFk7nTTuDryAMwHc7vyBhuuhx38NM9NRaprf-ybEoHX8HE9BXnC4cbyefH8rU9GXTf_XYDJoWDFBgNrDkQ1AXbh_nZuCRTBib92-tpWlC3-NjVkfdBW9d9XH9UtJ0A-iNNU3WbPl3i8SHHYK3vFnmw9uBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=LGQD4jM3IfH4bbj9gPjemDgj125jeXYAYWytWtFnGlcuJdtMXKsp1WVSy9Pe9nmE2XEiV0pZ7fa-mhY0qOt_vHByQJBfJ-MktEAYyj08c93acDyOt709HGEp_BwlgGw2G7_Pw1_D5QmLSR7VuHEaFKlvwUTu6Ok8dEwkamPE55hou5LSrjSqWf6FM0YGXFk7nTTuDryAMwHc7vyBhuuhx38NM9NRaprf-ybEoHX8HE9BXnC4cbyefH8rU9GXTf_XYDJoWDFBgNrDkQ1AXbh_nZuCRTBib92-tpWlC3-NjVkfdBW9d9XH9UtJ0A-iNNU3WbPl3i8SHHYK3vFnmw9uBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6175" target="_blank">📅 08:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6174">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=Zp4bIYW5pq457E_4eBxjRgyQvKRjRCW6dX5Iiwrcc9XqlbM_pT03nFLwa9KL--UHI9CVK_ZuPkG-_az3nxgpTBOqiyj23OWDJfmobX3wGIiyVzHS5j2JhtTBw7YsPxXGk7sGF8iT7g3JZL5baDOOc-x1UBx7sI22XzB_Bec6aJCfXfws5IikGJGTMG0wFGqirjoRZJReIWt-yi_NbMkpSfIsRDG-u52QkNgsgKW1GISqex4Ks6QMFx4rN2S5oKm-KabGSsCLmbNZRQCUg-U9rsyFfhg4zE83J9-ondaFM5yOOloEKdEd0IQ09b_UXYDGg9DOoqBlCo-J5JRVb2UurQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=Zp4bIYW5pq457E_4eBxjRgyQvKRjRCW6dX5Iiwrcc9XqlbM_pT03nFLwa9KL--UHI9CVK_ZuPkG-_az3nxgpTBOqiyj23OWDJfmobX3wGIiyVzHS5j2JhtTBw7YsPxXGk7sGF8iT7g3JZL5baDOOc-x1UBx7sI22XzB_Bec6aJCfXfws5IikGJGTMG0wFGqirjoRZJReIWt-yi_NbMkpSfIsRDG-u52QkNgsgKW1GISqex4Ks6QMFx4rN2S5oKm-KabGSsCLmbNZRQCUg-U9rsyFfhg4zE83J9-ondaFM5yOOloEKdEd0IQ09b_UXYDGg9DOoqBlCo-J5JRVb2UurQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLu-EaLEzZ_494vTInpSTFupE1kPfl_g8FYlkfuAFKI5lFn3mAWh8LWaPfyuQ5YqnYhlQWS5LE4GM38m3v5VIsoTKFl0Ufag_S_zkXq3GSpMUtjq7cwR6xjYtOMDbaEqXct_BTQt47nyEkTe7QR0MAI6yZ60OFCukrtlEtfk8Ky6VRwJjhwSTHOcRs_MeFAq3LO7F_JmJQGFrXLqpVEbykpg7xeiAIJhMUbvRJ1jIWoYNOHASXhu0wHf_7J-tQ5Xw3PGBstiyy99DTvNHey3qFztWFN7WykqloMM4mnYlC4n3yD3Enuh1tV7SGLfeeeSfZLLfnA5wQijyqPlMbzfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEx0UWcXNUQyguoRGucCrsGVEINnZKF3Biw4HI7NcVfjTwWeyQjOS5qSBU7keCzNSc-KtbMZ85WB2xYJM3fHS-SsSGDBWxhjWMlwf2De3WPka95R7TWt24zcPDFkW17x4De0ybInur_1Axc-DjxqbGG7VGj8h6G4yOWcRrZb5MrfD1BCwUUWXCe9diKfU0LH3PaH22LGwpIpL4oVXc-ibTIE24dVqT3xbr9Dxijl-vI7cZEY6Yyyv02LEz1POKCLlkBJ5lWoItNIccYdTu7A_TGFZAP24vElDX2tW9YemKI0s1M3VLMePoOh_W0MAS7NhgZlpaor_MfY58HPFlRMBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=KnvRdcsU4wEiuQM36tNseJT-Q5UQJiMOnHlL2gZ6g69Hs8ye2yDBGr1DMjQOsJFZ2cS-dj1QFcdV-EFU9yaZSES6IlUEQpbPRj5j54Zu1OMQ1bEvQEwt7TcvdezFIFDw0lZz4-qKtjKodk1z5EWNNInm7a31sDZqxuPa-aGjSS3-T82R3dGrV-GFoPR8TxkX_1Wc5fsHfAwwgiI_ghnCQCHgwCFKaiz0Lutvmnprfw15KXzn2BPCOklN1aKa4y-cHyqdcrszCebuf4lK3-Cx5ULwzZLErXgBwitZHqOFihdCoQyHYW5zg1emr6FsBcBr-T7xATx5MKnELL8vTQzZdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=KnvRdcsU4wEiuQM36tNseJT-Q5UQJiMOnHlL2gZ6g69Hs8ye2yDBGr1DMjQOsJFZ2cS-dj1QFcdV-EFU9yaZSES6IlUEQpbPRj5j54Zu1OMQ1bEvQEwt7TcvdezFIFDw0lZz4-qKtjKodk1z5EWNNInm7a31sDZqxuPa-aGjSS3-T82R3dGrV-GFoPR8TxkX_1Wc5fsHfAwwgiI_ghnCQCHgwCFKaiz0Lutvmnprfw15KXzn2BPCOklN1aKa4y-cHyqdcrszCebuf4lK3-Cx5ULwzZLErXgBwitZHqOFihdCoQyHYW5zg1emr6FsBcBr-T7xATx5MKnELL8vTQzZdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
