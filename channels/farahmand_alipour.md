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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 22:23:10</div>
<hr>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIOQVfZhz0XXHmouuOFUMaUiXc2QtDnpHgcvJ_6lMyLvPvs8vAbQMS96y4x7Fu4lDImcltyaeO8qcsieUdVVrjqKvLhVz07RWiYvEFnCkc5oEGMA-lLoYN5cDatcaY-zGj6oPI7Qm46NNOvRDBhCi4U1Jlq8OEUBy_4XnOo1zaqrfKEbt0K5KwyvFFMkdEg4g67rxaIVirQN9_0UIn_o8wFWi8hihh2gx97z3j5bs0XutuWDNU7b4xStT6ya4yX8-Ag8dIL_Q6WPFsMnI9tyJXPXa5_fgJOgJpUDHnJ7_LSTh7ubMeAxPL1wUlAXvn9ggmQQZSi1SaUNzFZR-02frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKb2WoAYB2BfZWkNY37IBbkbjJc4SIQ1g5XruVQSrsNKs3qgofww7iRVf2qoHSMHt6t6iMSSSuI5_6vfGuhUR14Gj-tuEAUG7WOMbKyyWwtPM770N2Kf7em2Ts-reWnN13h58cs7C2vy2zGJaFZBJg9S4K7sWOw2xdY7vpCzU8FrGrZBPb4ZBv2JGSw1BdmJmBzcJ5JxWICl5QqD8l_FZ-hXN96hAPs-knwNk1QmApMnpJMp45YZSZiJZLYuw5X3NAHMPzlMKAR0HCu4nBM-LypbT-i9VR58PTd4ID9ZsTDQmszlfFOJ-ihl0o_I2WCB1dabJaw2OWhHUsecid3pIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltal-iHqkU0t-EHVYH8ZhpAgiCYVDQtn3wBr7TH3XJndSFkvIyRCPZ7zD4r5YX4kbOKH1uxuN0aLUrdvaiiZTEoSzNZpoffNDc2_btwlxDopv2nx1EuZK7zQKhImefrntwGTuCWlVk8JL3jrKujqo28IxRtltUndl-jkDKS6HthSH3-KuA9yb7C_HZNa1CcmWzIbu_YSpKmlDbatnlbpWPi5RndPAmT28vdaaz_DHYC652KN-h6kuBlgGPP0mmG6N1O3jrbzsdTdyzK9fn6dqim164x3MJ5s6xVPdUukpyCJQxYlLT0On-Pej-4U6cNmNE8H4PAstP0gws1XZx8qzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCvSTOYx0zKLF6l_OFyPakkn2mIljlAQ2ei1ijJNIOnMpO6xaZnv4HyU4NOOPb9DsmNH6A742oDAcg7myl5cYjcUh41dcTXPkl9NQ2ttOaIYpqXYhnwzc0ojH39gBYH0zKrTPD2GMgmwLRLIXNn5lZxeBhwhDrZbu1nW9caz59WbNV8ZpU-MY5tl5E8ajtUmg0QZjFeJ8eYR-LMARvphq0A4xgENyxI33uCge6fS5GDlw5svNmLNklBik2fhNgL2MpIvrBv1OJhoHCxDez6Uv_t6t6Xxurhw7bIrmsSO4uTfKGLbZ4ofTk7ei8NuevxjRE0WCp3yNGMGSXOkXU-xow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuBAHLtebmp0i3zJGSC5DvPZLoX0F73DMm9ioklhszLVkTkQTTk7Ib6Y8n0sW50riJ4q-AXm3cOCek1gjlGdlp6GsdkJg4NfLJURDqngcNydiTooRjcG2OvbApBBXj6_rv6BXOT4qv5ZrAG7nzgi-hjSi1Hzef8m-7sFMZElJIU_6_x6ZoIbRBEinOBXPdNi7H1q-4fGeVbLxjPe8-kYr17fX4uxSmgV4lLXgS030geLc4v1hkkxcFTRdn0yBfFJ4p-Mqm1W3Rm6JqMK85quCs-k5rzVomzbggdxg07eI_XnruxRUNW5_u7eDYBpwyMsNKX392qK6JTH2RFBhBsV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaR9NCTrwfD3vNOBPEV_S02tSUAQxGTHYsaGqTZe8cxl3XZbk6-NYz9zE-j6TFbqoxXv4HH2e7VCHv88NCoIaAFhhf6afjvkUnMhtaos6_FaGu0E9qYBfZdAxwBL0Q_ffvrCzzWZmpOokMqfNNk1QArR4ja7PYyqgsghhU14YdlLRay263UIv85n1mSM-JY2k8eUKV1DEH3gpxS6vfrU1ljhrO1c7lHjmoqzCWRnc6AkVi5Vud_EiBR5HYC0_54Y9Go8yRMPJJ2swZ8500mFr45cUI7Zgu-7YnoG9dvg4MW0nscGvycALwwT_929FBdwfUGUPLOs4kHg6VnpQ7rdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZiXrTQ7SbWFTYGt-ISF50z8dQUcWY13qDeYiPD2ddmdAS-WAnfIqxtm_f8K_z0BXWF0jU1K7dQU-_35j37WAlPoIBqn-I7xhBv2A2uFes3oWutiTahuNH7M-ou9bkSb-xbubaCy3faxnVzMsdMnXk7mVB_0AuEeM2C1IP_rvXKqaqSGZo__TIVSBFSH8dj9eUIomA37Xfm8TlS4wnjPzQWqp0Yvvy2jcEyXfIUZal3Qu5vklyVFOnGqDx22Q6V1D4xdtTVNWW4jZSGwqtxunPoP83AlHCSTxp85GpuM_P1VDnRJtXBUYfDMyHfE0HdsaNOFQ8yJSUx1_iwtmJotrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKJ4HzQmGUukaK2SOoS0nZMqIXq1oLpO7eY3wwGSmb-Cxtwukf22u7q0kMUzk5jzt-RAuWt_n8WZAILkqFSdSJMptQIsofkk1VV2t0b__g9shXjxrx502QVekeO2uMrEx62SR15iuXlEW4IiwL0Q7ZWkKc9Jq5Es_fvmTpmJpOzouQUOWfTsp03nImNmMdEjB6O09NSUa8uYYcJLUhtuzu_D8uDEF3XBqZNRHcf70OH7xLM_USA_Rr1KLirlNRSHX8if7bnad9Z3l_T7Gwom45j79DuTfCSTTwq_Iib6lW7kG4oIErYy6nuPgopZ8vWJqTrAyGSAWeRLkNTvmSQ8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3Z7H6AxPLkyH08Qs4N309MhQcJ-cfZczl-6AnA7GxAz2qm_AGmdBIHTqAucXON4WqK4aACb3gabC9cmvlX2PnzjO2550JDIkKGrb3OlPNXyRkD2tqBdU5eXp9ON-jv8w3bM7ALNaGiJ3KIUK8X0vodjwcT1JCl7fPkG23hQBA2k0lATISQGAIhXLRQzNQVYnTF99k4uwg7Wt98RiHwGO6GMHydnNfgcKnWnYEuSVBuBQFKL7T1gkWxRWL2lkBaI0Ny9FwFJOynrWsSfiMK1tuWxODNhMK_0ajpYZu02CE32yiVS_Ftg4EVi3SCoUcI0cajLTH8rNRikZU6CJRL4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqmkzr2MMTuM-mo2C9405WYaSC1iGgfauDoQpHgLPb6eOk1tp8LC9h8OReDxrCxvFHHnL4fffOQnr0d9z7Okq1Tqk4LGQxW75VFLfrwsEDbxpyQ3LeCx2Yla-cpkBiQCnfy9N4x2LBoKnh2Lr6u9O8EWuHb1FAuSxiRR97pTLXCspm4FDNFDZQJuRZ5qhLaMUXYJWldgPa8Ke86zjoR3UvVS-nYiY5lf8QvLxvjFocJjr6sNSbucG5Tb8lOVJIMwMG8RKdiMeitjs-qtyW3ErgKznBRtS4GWmpbTlntxeoEFCrpNnkp5iNnyJ8zzZHv0fuBAcHMEigGojQSOFDHEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zx6xn0t5B2pzvzdzhq7C6sA-clatOxvUO_we0RCLbwcao0e9ETDb-HqW_5cKgHCKeG9n0j6lj4iRMFzTPvK-o_6uz-cgNdwq1aPvq7FAL5hf0RI4n7TBTAutveylXsMJT0ZM7__w3sv3bfMhjg0goTbtndcqwUF3kWYrj6ge4w6fY-3oNdN1NbmZke1-AMEuP_ewH9zwyWAGPjybDRqh1VXDHrwPH8i6LqaMf2juw4ivmyE7TUsjOp3KHkWseknh_7W--jQROI4tGAj9d3hnxGl19ipIbwuwRGolTjMMBLcQrQ8sC7Utb1MmraAWTYrGE4D27LjhcV-Soq5zXbWRnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adBHmnvHgAE7VxExNA-Kp8Q5LAjZUbX1OX8VT1vxHtZtxQGzGLKtoWuUoe1haMsgAsOTKgebTkKGukx4EeyMQ-Hc0nTp8XUackwfQ0g-n0Xb7lWH8FGSkbj69P3p_bYm7ul8YjwLrLdhVlzRgPW49YGqBqT_-nGXvLnfvJnYidHa1Uz4SVxXU14knnz_gSv5yoKVATqVbkl8IPLjlXlCqs-6hRFtS4ExAZG3FvRSUSohwrZsfzzmcZRgdbzyWLQGjGsp6o0ykWgZehE-gQfFsNLQ-Xgq75rTUsq_93wf7a8z3YXWLnoyV2dhgEsfUnlPYxDDVyC94A4sA4ukBUMT2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlAZHYcW59VZftAd0Mdh5SNHIhVX-hRYVUwsYDTfZYkERnoxBRHHwuAQZA-VsoWmFNq-nFdc28iYIlGPXeuHCBSJvFHdXGrSDaba6heuuRD5GfQAYeoVV6OuBcntEG1qGS8QGRkcXUenOk7Ij2pG-PwP-Yv_l2kEAA12B3TCihV893IITLYWaOKWLN-9XZ9vtlS-iH1G_AzZB13AoelswxBn9fkmdkEhsIAtZ_SJRsPsjIprV0vm1BM6koPRC29oNDRkzo15nHnoTRvq8z3Qp4VAowD2BXSe9ombDGK-5y2r-ivZ0y4FBDKiHJ02ofTqf3qBGozpETNGX5b6z-WTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn-MatXdhT9G_bB48uUdKLHv9YBtY4vgaHglm5meGYGqXfAxONqy0xN8ptfEjDZfL5ZCBK9W6a8BhjK9GYFkwlJpfuLfKOWFu6nJPdJpJbDim_GfHmKxcgZoUp98DxIEcaBb4NRuTLT7-Baz7nchljxKoaSKcdHo1F7--LMPHOlYisOoshQiyJzPa_yRgig5pp36Nj0brLq90mMZTXL4FtDCzGl_spopu8a3RgdeNCt7Yo9Anjbunc2eeXC2YZwNeGvsdV17Q2TnQLbIKLtnu5mz8yYQIPBP2YDIq25MWy7vlW9vWW7M-bSkMmsevhsRG8wyHJT4fb6dx_VfUEnfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMECqOwn2RG4FjbZg66sNlV03Q9xyxbeG6xPwRQ9JGzvENT207LFdFdTdnEzP70vhWsIeU59uAMx18SyaHZO8rPZnlhxJLkE62PZPVLPEoCWX1690LetexRhM9pCO3YW_Xt2SlzhGmGn4qNwu37h-BGaKqaoijmwhmldtDP7Rnsf-MYoWMT4kR9OCm40diAe94m4Jf92X7rTLASsgfnVsVQmSh2O-bXclHIm8e19m0ruGW_61iYM9PnGhgpoXjI_xYlB1-d2AlZtZDRhgsLqBDPfwUovyXKVrK6EaR9qL6BJGFj-HZ7oM77dhSC4wz_JUNasot61bjeDypLj3LUSOHY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMECqOwn2RG4FjbZg66sNlV03Q9xyxbeG6xPwRQ9JGzvENT207LFdFdTdnEzP70vhWsIeU59uAMx18SyaHZO8rPZnlhxJLkE62PZPVLPEoCWX1690LetexRhM9pCO3YW_Xt2SlzhGmGn4qNwu37h-BGaKqaoijmwhmldtDP7Rnsf-MYoWMT4kR9OCm40diAe94m4Jf92X7rTLASsgfnVsVQmSh2O-bXclHIm8e19m0ruGW_61iYM9PnGhgpoXjI_xYlB1-d2AlZtZDRhgsLqBDPfwUovyXKVrK6EaR9qL6BJGFj-HZ7oM77dhSC4wz_JUNasot61bjeDypLj3LUSOHY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=RjKu4zI5aqjUxk9jGNQdvCbhx-F3-oiDyNfBOcgKvc_h7wyT6Kqq8zxNr_V08Gkf9YKnLR8smDTy5dNWXIn9u6iZ3F00Af7UUEhx8aGgUa5H8HXX57E0imIeEZx6BHMFP_whIaWTzyyMmu5_3VK_QIH6bIMeZuTjUwcy-XheFvc122ms6df64VkwV6tuqO0qak6ra4stz7DhE6KgoupXjdtZcK0ixY4rlxAM44FR7AmeJ9ZaLzCTGmO7d77yuGU5gE44MmqoZYhN7V8OoUNH84HPL3pEdikheVFt9SellNo4HizKmz-GRdPFKsyJXVO17EKgIt5JaToTOQR_8Jm9KguPISBxRdzqH0Issuasa9IfeJh4rTO0OhLwpcDnC_UGAmVY_Zt8Y3tTQ-W_qiAFB_0-fQUxJIY9k8uoapiQYZTNk3Uw1H67FSTnevqTeKSgKVbObUFhVl_HoMRh3w_QAbMBbZV85Hy_Zbu3pTmJMFW21EyScBWVqXNj5zmOQ5n9eOHfXTMhUFf2BNmYbEWjddgFk2chThtkJLzydpAwYKZ-sgSTZ2sAGIGmZgpIJvWZG9rOznFC7n_cvZXJbgSPHDao08B1hS4HZXGovNhY_KfweZE-31uHc-qYuVUW7kn8s9M8UW9y06j0Gu75cmKmuzheTPWbtoHFfHbboYvRGds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=RjKu4zI5aqjUxk9jGNQdvCbhx-F3-oiDyNfBOcgKvc_h7wyT6Kqq8zxNr_V08Gkf9YKnLR8smDTy5dNWXIn9u6iZ3F00Af7UUEhx8aGgUa5H8HXX57E0imIeEZx6BHMFP_whIaWTzyyMmu5_3VK_QIH6bIMeZuTjUwcy-XheFvc122ms6df64VkwV6tuqO0qak6ra4stz7DhE6KgoupXjdtZcK0ixY4rlxAM44FR7AmeJ9ZaLzCTGmO7d77yuGU5gE44MmqoZYhN7V8OoUNH84HPL3pEdikheVFt9SellNo4HizKmz-GRdPFKsyJXVO17EKgIt5JaToTOQR_8Jm9KguPISBxRdzqH0Issuasa9IfeJh4rTO0OhLwpcDnC_UGAmVY_Zt8Y3tTQ-W_qiAFB_0-fQUxJIY9k8uoapiQYZTNk3Uw1H67FSTnevqTeKSgKVbObUFhVl_HoMRh3w_QAbMBbZV85Hy_Zbu3pTmJMFW21EyScBWVqXNj5zmOQ5n9eOHfXTMhUFf2BNmYbEWjddgFk2chThtkJLzydpAwYKZ-sgSTZ2sAGIGmZgpIJvWZG9rOznFC7n_cvZXJbgSPHDao08B1hS4HZXGovNhY_KfweZE-31uHc-qYuVUW7kn8s9M8UW9y06j0Gu75cmKmuzheTPWbtoHFfHbboYvRGds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RS3iFX2mGqjUIgNV2KkdzREj4YGFYns07Hh8Gokub7v7qOpIoNWia8kdAnAYR3ODhhdkjPNXFHvF1QBoJYaJnzEP-ExD_QTz1ZJd8XefZpqk8UrCy9VXpIUNVLBJNQL7jFzv89i35-KspfG0BS358BmyxPLLHiOGkQegkeNS12fb3l0dqlTtJjjw-kCr-BHaWD_SIqn723oJlEs7fIQNWoYCPDzKEAUrb9tjrVztE9V2W5yMykd5xF5C_k0hKXuKRL7-ng3nrIoPhaskiHDpEL-4CNzUVRIhbNt4IL0v3SsXIswEqPg8i9hLIy9YDqOAcNW3TYY6cJzb9fDHUjaQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=Q2xHIZF2zNfSnDwuH_7_MjqxVSYwCwPBZweyb5zjyFkxIuRC626V8qdt8VFtJzIw0FT5AkC2vTqxgoO-pDLtyXqBwuqSRpnHFpfgmSX7icKol8GDk4-x6BqjrqFdtWA4kmZp0WPcytssXKYINrvj7CjUIPDfrPkOYDZV7ieZoJJRI2jwi10e6V_UNrRs9T-vxFwoNlaInNy0XcgBnoRWRafrxnVMM8FhzpFoHv-xwnxZf7oAz_saYfeVFTrR7xV4xVi1KLRP5UA3BXF7GPKa76kmCfa06cPviIdU88RerBR-O3fu7M34hGVllKvKdAvD6_XO_MnaqBLOBea_GLnw3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=Q2xHIZF2zNfSnDwuH_7_MjqxVSYwCwPBZweyb5zjyFkxIuRC626V8qdt8VFtJzIw0FT5AkC2vTqxgoO-pDLtyXqBwuqSRpnHFpfgmSX7icKol8GDk4-x6BqjrqFdtWA4kmZp0WPcytssXKYINrvj7CjUIPDfrPkOYDZV7ieZoJJRI2jwi10e6V_UNrRs9T-vxFwoNlaInNy0XcgBnoRWRafrxnVMM8FhzpFoHv-xwnxZf7oAz_saYfeVFTrR7xV4xVi1KLRP5UA3BXF7GPKa76kmCfa06cPviIdU88RerBR-O3fu7M34hGVllKvKdAvD6_XO_MnaqBLOBea_GLnw3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=TmYdZCHwCx6OPLaBdYKRKXpTrNBzBDGgQ_Dd2TD0whWBizyJp19HDKt-tws7NW7vsqGcXpwQOPrOqQwo0p2apQ4mLByO6FEFuDRhvRxMMT4DCphx6_KwW_a5eNnnivElpS7w-MlBcD8P3GuXKEu_7gLfzN41CT-Z-gt_i9a-qpMhND49IKq9BUQrIQnbO96UNLQQkO35_pQySsfCYJjKzCxdv_UudH5VxmnttwHmwUDYh4GywKszJK5o8SwvrTGN7oGoYE9E9ctB4N1UPiTFXlVJiJUO68lRvsR_ILEcmiEz4MLS8b2UCyfeLD5aLyzuJ4tSOgb9njBITg5DjKLJTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=TmYdZCHwCx6OPLaBdYKRKXpTrNBzBDGgQ_Dd2TD0whWBizyJp19HDKt-tws7NW7vsqGcXpwQOPrOqQwo0p2apQ4mLByO6FEFuDRhvRxMMT4DCphx6_KwW_a5eNnnivElpS7w-MlBcD8P3GuXKEu_7gLfzN41CT-Z-gt_i9a-qpMhND49IKq9BUQrIQnbO96UNLQQkO35_pQySsfCYJjKzCxdv_UudH5VxmnttwHmwUDYh4GywKszJK5o8SwvrTGN7oGoYE9E9ctB4N1UPiTFXlVJiJUO68lRvsR_ILEcmiEz4MLS8b2UCyfeLD5aLyzuJ4tSOgb9njBITg5DjKLJTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATS7l0bC8EtplUbd8Xzjw8ibrAuEIuSJosDtG7AFHUIffZSYUP7GZS1KoDqfNYE2A3GVtuOQhpJb3s-V9pNcoTTTLTRACmFWePOsHdl-4i5kZqiQq9jMUpAR7nxMUUQ8-5IPSR27n9zbZ8l8ZiS55XwycOLjGP_7fnO0GBe9knc8iIceA5Nx_vvNbBxmMGBdBTsSmoJVa7gQrZb2mybN7hmfdnDs-sgd0Sp5x6Qoh4hLSDSsvctne2sFcR55uIxj6ZHI8UCVPg79aeL3wrLStXewFyBUnol9HyWtzMvW-RQJW5DB3D5sG6l4XDxsvlz1wsaK3larcAvCIiWPIovt9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snv3LsVqpySOHc7kE6cchvx8w8r54MJKZfjrExVd_PagMHb1mNdZB94xDWgSi7yDmPrm1AWuGU3VDIxkkrujSlcus4HWPdBd9XHmozRAKCA8U5Rj9B7HAh4FoImSLuREFLOWSIQiHY2J-MmIB33Lnm-bjKL-TnTPvOk4OcyXlmk_lgHSWtYr6A4sQghk0U0dlPqegPDZSGj-RPA19SgN5qdRp9QN_DMyeufDTOFz9Ul94wStc0xCu1IM-fN265GGCsMbMblY-iweHjPOItooB-9qn60bZ7FoPk8h8bhNofZ--5EqgYU2GyM_t4KZRClIsSldwL7toytcoNSKVI28VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=X4roJU_Q2caXZKrWmzEF2C43tMaXxAE-gm0zgu21OtXkGkhjLCe_uydTQgQ39XXGCHfaHuLlDZFYjlnb2YmlPv79Z1EFIxkDCHDAMG1y6Z3jxJYqv5lKzqWkyXbAoZfAHmpFIHTSpdyPA-Rbj5QKd5_LLdC4pGts9hKwOBW9KZR0xwB_vlH-9WlzWHZguSAh5KtkbViN3JTP3zzzkvAIqb3tqL6Mc2lGrpFvqrJZDTA6fS_VXJo_6iKq6uhC3tlqvs7D-L1f1f5LZyn_ckXGh8WtsIRxJnSrh1MDMlth2cqonn9IWrbMaSgF-jtBHLnvO8GjS9_Nem66QvyKTEI4O7k4sqqQIGYLDikMdM64xbMapYqv6_OT2xNi6hQv1wBWp_tFdy15kE-mtZNtNMgfkH3WpKbeh6Yvmt20eITw0uUfLE4XP7fsv2JjnqhBuFTLXNKH9NRlsnA8Y1W8VoiS2U-05r3IT71Rm9aIm514vvUnkNPz_QAj9ntZQzXnEv3jYow4KOYnbBzJEcmQ8aaBw8VK5DDqOasFiZN3P-vrFtbZ2yyiGFuG-Ro9yhZt9QadXiDPR1_jX1OcqMIYotveokQR1Bq0g2xbRc6GstEJvIk3BiRwQSS9RoDgzOYjhUxvzrtykXIWOeZwzRrcdLr0Zt4l3fhyNRG7DxQQM8-D6U0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=X4roJU_Q2caXZKrWmzEF2C43tMaXxAE-gm0zgu21OtXkGkhjLCe_uydTQgQ39XXGCHfaHuLlDZFYjlnb2YmlPv79Z1EFIxkDCHDAMG1y6Z3jxJYqv5lKzqWkyXbAoZfAHmpFIHTSpdyPA-Rbj5QKd5_LLdC4pGts9hKwOBW9KZR0xwB_vlH-9WlzWHZguSAh5KtkbViN3JTP3zzzkvAIqb3tqL6Mc2lGrpFvqrJZDTA6fS_VXJo_6iKq6uhC3tlqvs7D-L1f1f5LZyn_ckXGh8WtsIRxJnSrh1MDMlth2cqonn9IWrbMaSgF-jtBHLnvO8GjS9_Nem66QvyKTEI4O7k4sqqQIGYLDikMdM64xbMapYqv6_OT2xNi6hQv1wBWp_tFdy15kE-mtZNtNMgfkH3WpKbeh6Yvmt20eITw0uUfLE4XP7fsv2JjnqhBuFTLXNKH9NRlsnA8Y1W8VoiS2U-05r3IT71Rm9aIm514vvUnkNPz_QAj9ntZQzXnEv3jYow4KOYnbBzJEcmQ8aaBw8VK5DDqOasFiZN3P-vrFtbZ2yyiGFuG-Ro9yhZt9QadXiDPR1_jX1OcqMIYotveokQR1Bq0g2xbRc6GstEJvIk3BiRwQSS9RoDgzOYjhUxvzrtykXIWOeZwzRrcdLr0Zt4l3fhyNRG7DxQQM8-D6U0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=R4d04SyhpjbY4iGb1zFBCsskF7Nm1-wcgQSHX2pvZ3HUV1BgHydY9FI52KjW8jISXenhmIfqv15CRn3FHyBit-SIro49hcXmzLh_QElv0nkZfTO4zUGiTOZ7vJwocS7x-dhqoOwSgETaNzARskXZZKZSCqkdVi-QIDmWOtlG-gStJRx-wODha3My1oRUyAOdU-UWaZW55zx9hVXZ_w_jmLpOrphP_dyGsNzmeNqfENSBe2zYcx5KaafhljAXjoXBXwl3oR5oAnVJw-FzRHsLHqYq1P-lQiCVCEWBVHO6TJc3rXq-akLmcGwN24JdK90070SpeV0tdmfBzieqeZCXiG56Ubw2Cs2T_p4sb5cYyvib8mL1LgCn6Cu99PY3hLewHtBn_EjCTIp7b6d7oblxr6iZngfHhs_VSYsqC5KrdWJHt52h1gNTeJrYono15K-Kg3go8ReKpjmK39U6LVI8K7CZsGPB-vJbgnviBmHbswquYFsy8qdUpLxB9rSlQ0zIeNgIAiWWVf6kzL-GDmbdR-wjVxpaOO54IigkQo3u4XbSvkM5qx4ACLFnkuOGprNS16N00ePvWETmK_Wzmov0kCT71DTGuGoD9F3z1LoWE0D_JjSmV8kwyoHhOeAuoubQKCFINq28DPMQwNA7ykecKle7SJzOG5GRpMMHVZIdFWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=R4d04SyhpjbY4iGb1zFBCsskF7Nm1-wcgQSHX2pvZ3HUV1BgHydY9FI52KjW8jISXenhmIfqv15CRn3FHyBit-SIro49hcXmzLh_QElv0nkZfTO4zUGiTOZ7vJwocS7x-dhqoOwSgETaNzARskXZZKZSCqkdVi-QIDmWOtlG-gStJRx-wODha3My1oRUyAOdU-UWaZW55zx9hVXZ_w_jmLpOrphP_dyGsNzmeNqfENSBe2zYcx5KaafhljAXjoXBXwl3oR5oAnVJw-FzRHsLHqYq1P-lQiCVCEWBVHO6TJc3rXq-akLmcGwN24JdK90070SpeV0tdmfBzieqeZCXiG56Ubw2Cs2T_p4sb5cYyvib8mL1LgCn6Cu99PY3hLewHtBn_EjCTIp7b6d7oblxr6iZngfHhs_VSYsqC5KrdWJHt52h1gNTeJrYono15K-Kg3go8ReKpjmK39U6LVI8K7CZsGPB-vJbgnviBmHbswquYFsy8qdUpLxB9rSlQ0zIeNgIAiWWVf6kzL-GDmbdR-wjVxpaOO54IigkQo3u4XbSvkM5qx4ACLFnkuOGprNS16N00ePvWETmK_Wzmov0kCT71DTGuGoD9F3z1LoWE0D_JjSmV8kwyoHhOeAuoubQKCFINq28DPMQwNA7ykecKle7SJzOG5GRpMMHVZIdFWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=Uy3uTJ-rNZSgiBpJAwOPHezlfHYPor2hJBX_yrWQ3rZ_SAb0MtRAtZaeIGZPT16_8JBVHn2e4coWJ1TrB1i9XtYHt4LkubyonSq-D-2edA7-Tn0hIqaCE-rY6m1bjezd03EgtW4ts3wpQy5uD_NfBYhQcsMyRo_opt52VTnpXqtquQqQq9pnDaxZ5RBnKr_v104d4tnb-JTILxUAuezltQDTQjdgZxvVOmTHDi26Zd0FdMIf6BQh1_mgs4VHYOJIvgRDK7pz7VPYIuOBw8QrOHhz-u95AYFiEfn6Of7Kgf0NarmDEObwlQnDBaG1p9udJGVNRgx5v5DlHfZ6eez2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=Uy3uTJ-rNZSgiBpJAwOPHezlfHYPor2hJBX_yrWQ3rZ_SAb0MtRAtZaeIGZPT16_8JBVHn2e4coWJ1TrB1i9XtYHt4LkubyonSq-D-2edA7-Tn0hIqaCE-rY6m1bjezd03EgtW4ts3wpQy5uD_NfBYhQcsMyRo_opt52VTnpXqtquQqQq9pnDaxZ5RBnKr_v104d4tnb-JTILxUAuezltQDTQjdgZxvVOmTHDi26Zd0FdMIf6BQh1_mgs4VHYOJIvgRDK7pz7VPYIuOBw8QrOHhz-u95AYFiEfn6Of7Kgf0NarmDEObwlQnDBaG1p9udJGVNRgx5v5DlHfZ6eez2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzfblKgv3n9c7YzUib6ReRLctpenszARal34cw2V6XKUfbvg-QYtKt8yBgdeaeO2SjCYeRuNgAuBn4lCbPvJwslUbDlGepQC2xzCrd20rH3Hv0oJCQQZCmoDIJs0HE8rWVmioo-aC9N0k93kOqDta95_Brh6aqQ82NEAdPLp3wsZJxmkQGo8ktj1kPx4ipletHyMxU0SfGjWkaKxeeqWXlHSKKjiZisKEkQz4onsxaJVb_LvMPVn8nIA89r-sjOgwzMAwVsL2StWRCpozEASkYh2i4qjtkxc-bo8xbqotofltauWEZ8rqC4PfousiCxYh7gMImGzh4l1qIeTq-2t0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=Byw7BrrGx54nbFJB-Dc9Rr5kdfRlFb511MiH0hRS6m0XQiY_SFIOEZ4VuUWVsOJ3cnYYT5ltG9tVcUv1LZMH5wrWWdGhDchqfkpdpJIdTNHs047pCG07Daa9AOXcma2IwkOP_oVHIquZZmujsvqHTxVJTbsiQAcvBg-KD0kfFJ-1pDR95G7ZgsmvGAz6L78bZE6MJnqYiJudj62XicctgRARmp_S2uDI7qPMCLked2HMs5b86CNAcw2ff33nD6U1vzZMz_B6o-26fWhh6L4suMrGA_91g6EhQ1chm08mXpncF3pWyoexk8cGu_BArCaz3qUZBBZyqVAqrmgqhoN1NyT1Cj1XPuJgowJPGVYdnjI2nSjrKtnrVwqhrmuU7eX4p7U6rpubYGhp7oNjEYfyiMQGZ6HVH4GJFaXVEgn2OmPyD5-l6Jo9wv627ccuzlgjVaPIqFGMQN4_pVYrHIglz9p_QJkMm1PB_QLNAsCUvWVOH4VGhPc5ParaGh62YWlGSTxZMiFG37CMqjzfMHqnPC3n5pltc513TwBS7aVMLosOenUw0rhYCit0gBRudE9mdrKzQSRbKJP9sEVrlNtdW9OeD4gsLjlFcDZGWjifrBHMbTtAWqzpREbMKNSOXYH820g7zSrAF6_BFQgKsfJsfIgjG_wYTk9PhpfOW_uxrlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=Byw7BrrGx54nbFJB-Dc9Rr5kdfRlFb511MiH0hRS6m0XQiY_SFIOEZ4VuUWVsOJ3cnYYT5ltG9tVcUv1LZMH5wrWWdGhDchqfkpdpJIdTNHs047pCG07Daa9AOXcma2IwkOP_oVHIquZZmujsvqHTxVJTbsiQAcvBg-KD0kfFJ-1pDR95G7ZgsmvGAz6L78bZE6MJnqYiJudj62XicctgRARmp_S2uDI7qPMCLked2HMs5b86CNAcw2ff33nD6U1vzZMz_B6o-26fWhh6L4suMrGA_91g6EhQ1chm08mXpncF3pWyoexk8cGu_BArCaz3qUZBBZyqVAqrmgqhoN1NyT1Cj1XPuJgowJPGVYdnjI2nSjrKtnrVwqhrmuU7eX4p7U6rpubYGhp7oNjEYfyiMQGZ6HVH4GJFaXVEgn2OmPyD5-l6Jo9wv627ccuzlgjVaPIqFGMQN4_pVYrHIglz9p_QJkMm1PB_QLNAsCUvWVOH4VGhPc5ParaGh62YWlGSTxZMiFG37CMqjzfMHqnPC3n5pltc513TwBS7aVMLosOenUw0rhYCit0gBRudE9mdrKzQSRbKJP9sEVrlNtdW9OeD4gsLjlFcDZGWjifrBHMbTtAWqzpREbMKNSOXYH820g7zSrAF6_BFQgKsfJsfIgjG_wYTk9PhpfOW_uxrlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=nKAADOgVIInd5cWmENrO9VzCCq_Rc8Q2pCLlXoYeOA1hBgjeXCwefxw278iCDnsM8_EAOkr_WOAfyhVq5fjfNB5YFMMcm0ft-8xZz_V0FBPtJibNYiWKHVwelYCqJsKt4TDnUS5BrCsQsWlXSSE5fDKhPG6BW4yJqN3pdDJ7MlpaKk2YBIWKKrw4_KmELb04MrtH7DOZJ52dKPlXavZTuWdCrByTjDkN9xKHqhOBHQov1pw8gArtRmldb-ESrFA9LliOo3PdWW5fFpqocBYS8Hw1jEYXMa62_IMJxaTzk6CimGuf_rBIQNcZwLNhZ-JBKH-lCSf91Eqa3nEC1W1MVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=nKAADOgVIInd5cWmENrO9VzCCq_Rc8Q2pCLlXoYeOA1hBgjeXCwefxw278iCDnsM8_EAOkr_WOAfyhVq5fjfNB5YFMMcm0ft-8xZz_V0FBPtJibNYiWKHVwelYCqJsKt4TDnUS5BrCsQsWlXSSE5fDKhPG6BW4yJqN3pdDJ7MlpaKk2YBIWKKrw4_KmELb04MrtH7DOZJ52dKPlXavZTuWdCrByTjDkN9xKHqhOBHQov1pw8gArtRmldb-ESrFA9LliOo3PdWW5fFpqocBYS8Hw1jEYXMa62_IMJxaTzk6CimGuf_rBIQNcZwLNhZ-JBKH-lCSf91Eqa3nEC1W1MVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnY-jVQaebZxIo9ExDpOoXvaMmhfuR8y8FT17OwPlw3gatRQzNp6i9tLcNlEG41E7WsxDeIN-zfUEEPQ58Ow6ruwef1eKrIAr7WMMxOwoWDDQEEVBGbqVIfvno0whsCkhm1iC0ixy2GG44l5a6dzyStLH6hhMWd7iTMJJVsrZvzbXWa6WQevU20oECH0N5RDXGNEvyJcSukATAaaP4t62AUNifJc-2fRmI1gx8lKJba4ykujLqxVqbVY4IR5JCgRLmHY0Hx8RdR2uHyBUnvd5z7r1E_6MNpD-_4bYZKH-XTG8DvbxPbPizeXtlN0hU_hanR2dD4eBi93FxkrGiB6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxBhTgs9Ec4HCayj0Ys-XDH7SD6d86_Q3gCtEVNKv0zneQzjm0yUjvajGUfzHfWj2nrRe8i6mfgI5xOrhZTfm5D9suGSjoFhu6AlZs_Nwywr3-bfVoOZzmt-s8z1t5QKTsiYovjuSU6ARfZShiIRb2JX9pAc2hkX8sqFXQZT5MeIE-H8XDzzSB_v-2ok6JjgB41s73PNPZsZNggNI8CAK8yzNOLgAZtYbHgULg0u2GJccLIf0rSejs8qVmnrLK3kM9AlAL0uHPJPmqUQeZ7wq2mcoPm4pVJNl1EdqQtgQraqP2tUDDEdpucCcqBTKtUyrc4eqILToNGdRlKEY6gdQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlyS3n_aUNi-oQ0gdWVTI3kB6XkFsbKJgOQxE0BEFdUosomY6SPMDbmqSHNUUFHKWISK0MJk5VpxMOQpMKcxMeDmv6VIuVRXGaKrEe1XepRCOoZjHYDme0HKfizG-jyUsGAbQLKvXtsQ3tDB6wCzCG_FLTz-FSDkjmgZzwW4Np_eaDPPiU-9W4w_2z4oodN-jyAPqXNauHNuGp1_3l28tdD4FYqWYdhhlvHjOcyyt8vstInjzNZj7DK4KyBYJP9zqyqJ_8SVPPL8q5eUl-VtWtAGOaBFUA9CbQ19DADBDRfNneXReHaFEN4G6jP0OZkpBREOEy0dQec_kXnW6kNNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JmRcjBAvo_lRhWqg1_Hk7pCMXi55rH6vrvomJUYWDSj9uuMrdWhhjrT3FpiiBfR20gff331Je245D21VGKnwOQteZmi9JguCXXekG2OJjE5we78aUb8OaNE5u3IhhqdYnlr2j5a48T7KDBVamKArIbGODWEKZiJTLvRGmKh__AOjRxEr1ZC0ZKKhaWXtzdqoTEpLHBjNZDvqzhj2vok81mxq6XcBC4W_PUi8Fitdj8lG6d2m_W-zZl_772h61YEReobuCEksywbSukHAYmP9L2wEkVZIh6lawvMJLPEzX-aCKfhP09nFdwJ3d9-LAqeJmY2R-yQtzbSmGBKEkBlracQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JmRcjBAvo_lRhWqg1_Hk7pCMXi55rH6vrvomJUYWDSj9uuMrdWhhjrT3FpiiBfR20gff331Je245D21VGKnwOQteZmi9JguCXXekG2OJjE5we78aUb8OaNE5u3IhhqdYnlr2j5a48T7KDBVamKArIbGODWEKZiJTLvRGmKh__AOjRxEr1ZC0ZKKhaWXtzdqoTEpLHBjNZDvqzhj2vok81mxq6XcBC4W_PUi8Fitdj8lG6d2m_W-zZl_772h61YEReobuCEksywbSukHAYmP9L2wEkVZIh6lawvMJLPEzX-aCKfhP09nFdwJ3d9-LAqeJmY2R-yQtzbSmGBKEkBlracQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svHoekx-hNUAvPFrRI9d0WG6bXtXqMDYYXsrH_MkfnewbU6ouounAELuyOKy8eUxFv90nqOtVSEI_cL7uvH8zPiOMNCltLGMRA4J-UR97elxYXy7LdEU27-8-2No-Ni8Pj2SKp3-i3a3DJ-SWUL6NSBUewXfB7oNnn8HVht33eb1Z_Uure61nwI1I7LDuUFd1153pGw96P_14Ulb3qsYeYDBFeVqWNBoxAvm5oDYL2jUv_exVVdjdKGn0Brd7a8Se4ffOleVsEXmX5kEu-LDUmLZmLFDwGtzEcO7vuNbiWOUJvvaqfKoFPmz8KO76grWFHjXXyTKGnaOLvXSII1HIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=rCSNeRYW4vTNYGjLqaWR5IIiaMctPti6Z_sQwNhc6j2ZLgcLnlqlCYEHqZ1VJKl0l0u1blHa48Hix4qKFNuWuyNbxaJwN_-zpuLWB4oIMr_n21HAUOqAPbP7Gydp0EBiFiIaImbxmVi7j3BDYgOa_9yoz0AwWYC0tEJkBHiFNvZT9_41gBUpWDoh4HRCNe77OSIV_Yp84MbJsgFFhZlEF2PRIDrLe2x5itAYtYMNzLiIeIul7bDludFRKKGOx--egF--zPfO9dg_bs_BcHHOSH0YF4OflXSWIcD9c9pgtFXJqJl_7SFffxtSNo5RGyFCRZtrpPpo0fI3up7zSH5yAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=rCSNeRYW4vTNYGjLqaWR5IIiaMctPti6Z_sQwNhc6j2ZLgcLnlqlCYEHqZ1VJKl0l0u1blHa48Hix4qKFNuWuyNbxaJwN_-zpuLWB4oIMr_n21HAUOqAPbP7Gydp0EBiFiIaImbxmVi7j3BDYgOa_9yoz0AwWYC0tEJkBHiFNvZT9_41gBUpWDoh4HRCNe77OSIV_Yp84MbJsgFFhZlEF2PRIDrLe2x5itAYtYMNzLiIeIul7bDludFRKKGOx--egF--zPfO9dg_bs_BcHHOSH0YF4OflXSWIcD9c9pgtFXJqJl_7SFffxtSNo5RGyFCRZtrpPpo0fI3up7zSH5yAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=XV2XuXm-JL3uoGtorPURl00FNkIf09REGni3zgYjweh3GU-PkVE73uNgkWibhzPu6lqowifuyHa1U-kdc2cNg4y0DSHrCUFaKVLLAd4IazRURJj6FWdAuJlwETaPaQraObpGy-nSxsYHV-d4LjGLWjOpPqhKaW1Kiaq1c5CpBEfmzo5Wp1wXGuoqDB2yYql7wNvcZ8GaCpARXnjvMmOAjA5RmSl4BwmR0b1bUkrlf2i-LqH3aqvNbJZa4N72eMdVo6Ta4jgC-DsVB-KJmmPxxhiJ7kq_HQPJfsBV_diNECJYF2WzVq1ginY0QppPwVK9YzD0iEcfBEo3zasXSxHwyi5ftW7Hj8lATX1eWlMvD_8JB1Aq3OKuzuyx1NdbhOTKbSGzqPeRQlSG_02ZKyFswkcoZhXrI8UUfRoQfA2nVKkaYTQISmtN4gtGNnba8ZScyIdAfkwtI0RciL0kZMs5eK63fsPlmj03Z5mQ14kT3y4FP03bvW-ZXYCEVe_W1Z7qOk3A_8ZuRvQMp4thj8G5OS8cLZs8ji787YpNfYpKPohquEGLhkOZ_qWE9YQC6KB4Bl3ryTE0kX5wlp-NyAIZG7MoA8-y8DlhH5Q6HXV7JFZ_yMLowJWZyIc3WrdwSStr9CQG9NdBfWdZYoHlpAPx8OLimU-gfrj-s7WBlFuLXGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=XV2XuXm-JL3uoGtorPURl00FNkIf09REGni3zgYjweh3GU-PkVE73uNgkWibhzPu6lqowifuyHa1U-kdc2cNg4y0DSHrCUFaKVLLAd4IazRURJj6FWdAuJlwETaPaQraObpGy-nSxsYHV-d4LjGLWjOpPqhKaW1Kiaq1c5CpBEfmzo5Wp1wXGuoqDB2yYql7wNvcZ8GaCpARXnjvMmOAjA5RmSl4BwmR0b1bUkrlf2i-LqH3aqvNbJZa4N72eMdVo6Ta4jgC-DsVB-KJmmPxxhiJ7kq_HQPJfsBV_diNECJYF2WzVq1ginY0QppPwVK9YzD0iEcfBEo3zasXSxHwyi5ftW7Hj8lATX1eWlMvD_8JB1Aq3OKuzuyx1NdbhOTKbSGzqPeRQlSG_02ZKyFswkcoZhXrI8UUfRoQfA2nVKkaYTQISmtN4gtGNnba8ZScyIdAfkwtI0RciL0kZMs5eK63fsPlmj03Z5mQ14kT3y4FP03bvW-ZXYCEVe_W1Z7qOk3A_8ZuRvQMp4thj8G5OS8cLZs8ji787YpNfYpKPohquEGLhkOZ_qWE9YQC6KB4Bl3ryTE0kX5wlp-NyAIZG7MoA8-y8DlhH5Q6HXV7JFZ_yMLowJWZyIc3WrdwSStr9CQG9NdBfWdZYoHlpAPx8OLimU-gfrj-s7WBlFuLXGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=KCoLJoMhhJUfAFG818lcsuMWVavWc0BA_0yu3ZbrUal-6K8CHfofII-9weNKyuo1hhNdZwWxfBHff3fp0TLL09Y7YWKj9YC6ln_on4QVbQKZp898rq78jW-AOKmboZuG5dQem7rdWUq_Hq9FRI4f-U9Qia5yCI6r7uTKVfY1S4UfJGux3EZnELqoNlOzw_PXc0ebPSlOGZ9Chr4_fIBeahphO8H04YCZY-ngz4mgrUhhBrl1RXvtvfcYka7f1nK7kFrc_d9NBJ--zr0Llbc91a9RpLTTLh8Pqe1Vl-A29ihzS_GQecUIrTCJUuu6WhPSAJp0Mlh4EElqDT-qJYTtpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=KCoLJoMhhJUfAFG818lcsuMWVavWc0BA_0yu3ZbrUal-6K8CHfofII-9weNKyuo1hhNdZwWxfBHff3fp0TLL09Y7YWKj9YC6ln_on4QVbQKZp898rq78jW-AOKmboZuG5dQem7rdWUq_Hq9FRI4f-U9Qia5yCI6r7uTKVfY1S4UfJGux3EZnELqoNlOzw_PXc0ebPSlOGZ9Chr4_fIBeahphO8H04YCZY-ngz4mgrUhhBrl1RXvtvfcYka7f1nK7kFrc_d9NBJ--zr0Llbc91a9RpLTTLh8Pqe1Vl-A29ihzS_GQecUIrTCJUuu6WhPSAJp0Mlh4EElqDT-qJYTtpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOUuSnqWj1y0P5aV8oHZNTpn_a3mHPZY0guC9SL6WdHjLBYgnKbYy3bx2DOByRgBoKiHHC1Z5zGDS8uBIBt638vVYOW9_CpDaATkds-nktEsCweY5hDk564wOy6NwylYcxDat1fd3V3Rexu-dz3LycWnJr5YLsQD-qWfdxPZCEvVuymQG0vB6GoM5NYD_HydIGJytXJBLHlgz2rdv6W2LFCsbtPwsuREqxsQx1v-GXrvJHJSNOCTjcEFjvsd4PEaIMBv4X5f_3FqukpnLGYwOCmX3MLjKWMwFfriHEaVq6Um1q1PTiNBzK-JM0P7J_627PYRDHBwrXqfykyPnEUS8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=P87OIgK2YK1NgozGToG5Aqy76_tYqI2ytDcgkBb2pwYa5vhs-Oc4G2p1Oy_5wMYa3nznnAjy6MSnpFEPmJr2jfPDP81-GStmeqH8UbdWSmzVMAs3dqJNWsDo7jcHQnpk2AWGenbsfdk7E7Z4ynP8qp6--04rp3PYnpXhS3wsF_4DjCFKo4D27caw0hNbzaKuw77kmRVBhXDfreqzO0lN8eGjBlNYvbXO4xavYEHpeKcC0dpAFOy06y4BTJygBJrUu1yzyPgy8Zrxeq-7DEpkbVTW9KjOqEUhGJhclE4Q1OnbWqKEghgsSrV54NS4H4mj36DBqVw1Hzlunj98utgla6mJev6oGCEoPn2iNj5JSln1TAId_3jqAKsYWaPVoorur3Wbt1U7HET01PL1ihf-q_uq-g-cAQQse7g3p0WnfaQ59RNEhpsxCSZMHHrcxflFUsUZXVxlcALvYfHEOwIeMCGO4OZElhZsU0dOdbzI7FSq8XWg2BeEpODpWoscgxYeLAQGmAIds_U4hObZdVHDmX1XhzNqabwghH_n0sl0FHuK-0j0gv-O8VtJKV0zBiXd7Jfj-I4LUAH9biH_h3EWXaTVIEsq3SGmE7-itgdgurVuKja54Sq1hsxkvjyXb-lzqdF4PdhDYhIpDROBue8s79vwldkR-exJeZknDxUk0bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=P87OIgK2YK1NgozGToG5Aqy76_tYqI2ytDcgkBb2pwYa5vhs-Oc4G2p1Oy_5wMYa3nznnAjy6MSnpFEPmJr2jfPDP81-GStmeqH8UbdWSmzVMAs3dqJNWsDo7jcHQnpk2AWGenbsfdk7E7Z4ynP8qp6--04rp3PYnpXhS3wsF_4DjCFKo4D27caw0hNbzaKuw77kmRVBhXDfreqzO0lN8eGjBlNYvbXO4xavYEHpeKcC0dpAFOy06y4BTJygBJrUu1yzyPgy8Zrxeq-7DEpkbVTW9KjOqEUhGJhclE4Q1OnbWqKEghgsSrV54NS4H4mj36DBqVw1Hzlunj98utgla6mJev6oGCEoPn2iNj5JSln1TAId_3jqAKsYWaPVoorur3Wbt1U7HET01PL1ihf-q_uq-g-cAQQse7g3p0WnfaQ59RNEhpsxCSZMHHrcxflFUsUZXVxlcALvYfHEOwIeMCGO4OZElhZsU0dOdbzI7FSq8XWg2BeEpODpWoscgxYeLAQGmAIds_U4hObZdVHDmX1XhzNqabwghH_n0sl0FHuK-0j0gv-O8VtJKV0zBiXd7Jfj-I4LUAH9biH_h3EWXaTVIEsq3SGmE7-itgdgurVuKja54Sq1hsxkvjyXb-lzqdF4PdhDYhIpDROBue8s79vwldkR-exJeZknDxUk0bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=ZiIQpNMcCqEn0OyfpaySN0PKPbdU10UQ-w1MDusfnW3NINZ7LObsbFLlOOEAHVfroYVMvnGSyF3R_4p1KA3nibLco4gYqLbBTu8jUfmuvsUQvbmorzXCTSlCnGZYIasWTPOoTYzMrjDmVt85Z9hKXkfGpie6itp9P-oAdm9OoCiqxud8J_NFdUbUHbfwkqwo586BoOc49gzwr9VPRWCaVT6r_vkNLozS4RidEVQZ3oZd9Hm4xUrrORJc5WFvTm9idO4RQR0mvbg-kQEQckeAOrOtUrR-gNxnDZnKOzxyuKZWqzvTUBbR0nTxG78cBysCD9XlTE1fJKBHmlS29aSLzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ef12b93f.mp4?token=ZiIQpNMcCqEn0OyfpaySN0PKPbdU10UQ-w1MDusfnW3NINZ7LObsbFLlOOEAHVfroYVMvnGSyF3R_4p1KA3nibLco4gYqLbBTu8jUfmuvsUQvbmorzXCTSlCnGZYIasWTPOoTYzMrjDmVt85Z9hKXkfGpie6itp9P-oAdm9OoCiqxud8J_NFdUbUHbfwkqwo586BoOc49gzwr9VPRWCaVT6r_vkNLozS4RidEVQZ3oZd9Hm4xUrrORJc5WFvTm9idO4RQR0mvbg-kQEQckeAOrOtUrR-gNxnDZnKOzxyuKZWqzvTUBbR0nTxG78cBysCD9XlTE1fJKBHmlS29aSLzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی از سخنان سردار نقدی : اگه حتی به آمریکا حمله کنیم، قدرت پاسخ‌گویی هم ندارند!
با کدام پشتوانه اقتصادی میخواهند بجنگند؟ با کدام پشتوانه مردمی خودشان؟ همه جا در محاصره ما هستند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6178" target="_blank">📅 08:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6177">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=NR5_UxbX50cfbR8sk2OqL91MJE4NYSrFgv5c1CCJbgtuyw8Y09D6UmNo_29nCV0qAc3eFaccnTmSAhfAZcqUB274rovKbyrz7a8PHKMm4su5KgpY46ftVQ1AMNCYIUWo9U0w0XR5cto79pqBpaiBiMsVy--9Ud5bNuf1LKzgJxe28jKQD_G3EjazofiVwdi_O3OMkWVz0RMZV3FOfHfJiGEmzSJzB8_DqnpZhPU8jloWohxFMioYdgATJBxdypuQ6OpIUJw04Og97X2fqnWkSFlQ75wZkg8sO_THrbwgFcWT7QLDLwvqFKjTr97Kj5Ze8J9bSFlSDOY4IzvbOiGECA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d050ea81f.mp4?token=NR5_UxbX50cfbR8sk2OqL91MJE4NYSrFgv5c1CCJbgtuyw8Y09D6UmNo_29nCV0qAc3eFaccnTmSAhfAZcqUB274rovKbyrz7a8PHKMm4su5KgpY46ftVQ1AMNCYIUWo9U0w0XR5cto79pqBpaiBiMsVy--9Ud5bNuf1LKzgJxe28jKQD_G3EjazofiVwdi_O3OMkWVz0RMZV3FOfHfJiGEmzSJzB8_DqnpZhPU8jloWohxFMioYdgATJBxdypuQ6OpIUJw04Og97X2fqnWkSFlQ75wZkg8sO_THrbwgFcWT7QLDLwvqFKjTr97Kj5Ze8J9bSFlSDOY4IzvbOiGECA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل  کهورستان در اطراف بندرعباس
که شب گذشته مورد حمله ارتش آمریکا قرار گرفت</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6177" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6176">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔺
معاون استانداری بوشهر:  شب گذشته ارتش آمریکا با چند موشک به پایگاه‌های هوایی و دریایی بوشهر حمله کرد.
🔺
خبرنگار صداوسیما: دیشب به تأسیسات برق و مخزن سوخت فرودگاه ایرانشهر حمله شد.
🔺
دیشب ۶ پل مورد حمله قرار گرفت از جمله پل‌های رفت و برگشت بندرعباس - لار …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6176" target="_blank">📅 08:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6175">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcFu9tFuXadTkSyIPH7uUBouC4tX76S_ciuTBdItyaJtVJUNLHtYUOoGU_q9NjwguQa-RPKlhEpsZEMvoEibhhYK9_887DJ1x8qrXYZLHk2xGJm3wHG2psHKXhUWtF027NhEJZJUs6UQdteDQGnuuABHOVjeuZzlPiuooU9uZNdY5_Gj28PBNaDxhNrylBYgJ66mlTG6V98WOXi_RgoJFa-aZ69zCjckzldj4lmKXlwZYQ62dBRyhLdn4_tCAiFnueK0w_inOJYP18A7N3KETqXPxbbeqopzf8liV9V2dRZqPyZeN7QAVeVMkgl2xLwzPMVI92KPv6kQ6MCUUw7kXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
حملات شدید به بوشهر</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6174" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6173">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=PM_8DNO7nQwXxXGwW1qBev71VLQybthKjCTQe1HYQE6KgoaLvs-h1y7o5QxzP6DmHQW-g0MX9e_cyfvbV1wvFmk-w-uiWiu5eX_jQ_ow0warFkd5GAG86GFmuyuVjSeY8g7JbXU89AlVR5XrKtl1W3DJl0iaO-nfLULiZv9828p_VVhnV13x22yoRTCiyFBJykG6a7Zfu8_fytOM2x1zx7SYUDG1j4bTW8gz-gK2DW7biIXkLXxnN5-dthSF-5bv7DGQ25FumjMVJbuSsDoKHqjL8cO5RNYKGr3wPbzLoUA0bdWiFnca8K3Nahk2KJjNOKHq41Bf3NIiKQc1bAmnrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0adb998b26.mp4?token=PM_8DNO7nQwXxXGwW1qBev71VLQybthKjCTQe1HYQE6KgoaLvs-h1y7o5QxzP6DmHQW-g0MX9e_cyfvbV1wvFmk-w-uiWiu5eX_jQ_ow0warFkd5GAG86GFmuyuVjSeY8g7JbXU89AlVR5XrKtl1W3DJl0iaO-nfLULiZv9828p_VVhnV13x22yoRTCiyFBJykG6a7Zfu8_fytOM2x1zx7SYUDG1j4bTW8gz-gK2DW7biIXkLXxnN5-dthSF-5bv7DGQ25FumjMVJbuSsDoKHqjL8cO5RNYKGr3wPbzLoUA0bdWiFnca8K3Nahk2KJjNOKHq41Bf3NIiKQc1bAmnrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏فارس: جزییات حملۀ   آمریکا به پل‌هایی در شهرستان خمیر؛ ۲ نفر شهید و ۴ نفر مجروح شدند</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6173" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6172">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idMaGV-a_AsCYHKT3sjLENKPQi4TdhWEeZrO-Nkt34EhNdsMzpPUYKygUMIFH19XrL0lcXvmV0sqZJ6Ff2FheC2Na48BYQw8F-H-FF9ao9peBciwcNdCpcnlAyRdTkeYUq3LdysG5fd6vqkFX1K5-VuVCSBdQqyzOXuekbelh1c7DGZgvn6P1_3AfsUTb9E9rFtBPO5840srlKKuHWiEdUo9gk8CP_6sL8xlMS0CniZfFT-sONz1-qQxUIIYyFQUEOOForBUo3PyMGXisQyn1A13617tBIHvHg4bo-5NjQDuuPJ7Pj3l5ip08PMX97VP10rOfbTxkMDOZkrjphNr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6172" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6171">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
صدا و سیما :دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند.
بندرعباس مهم‌ترین دروازه واردات و صادرات کشور است و شبکه ریلی بخش بزرگی از این حمل و نقل را بر عهده دارد.
این حمله می‌تواند به حمل و نقل کالا ضربه بزند و به آن اختلال وارد کند،</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6171" target="_blank">📅 00:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6170">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
حملات گسترده به حمیدیه و شوش در خوزستان</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6170" target="_blank">📅 23:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6169">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
حمله جنگنده‌های آمریکایی به فرودگاه ایرانشهر</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6169" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6168">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=e1JsMRu4bcP0YoSY8ElwDIz4LsvISN-PO7tVCudfE5Mdj0n4bY7tVlun00BgOOVcrE0Xjoah5QbArRMUv3KtGCIFIXPIrlY83nAxkl6yJepXY7Q4EJTlVKBdZpBlv90_ey_vXwhvq2PzF_gTUpklBPOieokJwFFbApUBMqEoEFmMd2u8Un2A0zMzYlKX0vwfeDeREBRsUbGT2xaw9DXMIv0y5Fsn-AUIclvyCZUR9VE5XXLZKS5KzaSHSN0Q0T9id-PCZZplXHVCXZZZ-xviyKqkEVk8L_F0glQtVZZL-E2yRnxjIA7_Tz4XqwKnry2K8ts5HAeA-L8HI4Nn2AX_lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067abcc49e.mp4?token=e1JsMRu4bcP0YoSY8ElwDIz4LsvISN-PO7tVCudfE5Mdj0n4bY7tVlun00BgOOVcrE0Xjoah5QbArRMUv3KtGCIFIXPIrlY83nAxkl6yJepXY7Q4EJTlVKBdZpBlv90_ey_vXwhvq2PzF_gTUpklBPOieokJwFFbApUBMqEoEFmMd2u8Un2A0zMzYlKX0vwfeDeREBRsUbGT2xaw9DXMIv0y5Fsn-AUIclvyCZUR9VE5XXLZKS5KzaSHSN0Q0T9id-PCZZplXHVCXZZZ-xviyKqkEVk8L_F0glQtVZZL-E2yRnxjIA7_Tz4XqwKnry2K8ts5HAeA-L8HI4Nn2AX_lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک پل در اطراف بندرعباس
خبرگزاری‌های داخلی : پل ارتباطی بندرعباس و لار و شیراز  بود.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6168" target="_blank">📅 23:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6167">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFslXjV7WvrnFlGgD4xrKUvPXZPktU6vrAhMoSMIlcwSk8vC64iXpJqlbthvClQQSNWHL7gknovMq5u7yn1M-mKfnZXC2eqn5EejvJAOvyt4ZZk8oWHvZlhD4a4Mhai5ULVj6xvDjmIEP0MzW9I2Sourax0-hGCGEooTMOrNp8zdwe0XRl2O3fCViY3sTFIti7dcCr2y7onHa6sIxjye6ZOJ_k6Yb936FGdtmZzEYEmXUP2F0kOE4nLmBByNrqsrJJri0R29tXpqtq3wlB8Hf9bRP0E_hWtx0GLJtxCLGRaPIFZEHaSFhxppmSgL8TFFHqZv0AD3aPugEduWoDHQyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=v_NcvBbXd18L7aSuYPSrTNWiMmjunbHVYRp8DOKwxxDO-NAF1I4epSGqZtpix46NBMxm704twsiWAjgQ1SVVhv-Pqz5lJ8tndMg5SkUD3R3WVZfRclEKWyxsbr7jXGEwQynqvtIBn-RmXmyS-J8I8sbU3r51KCn2sCo_3ZCQ1HbSfGTb5OXBSxkKJJ01P9rehoqbb0pvgvVES5Joq7wC6IE-t3bqMWCPpAwonmL7K13a0fHCnSFpLNM0_oNXmM131C4BdyHKdptRyP2wGRaGxce7qTfqmLt27XoVl97gzFiDF_SEwgCTTnLuUiu8KFMwbCFJR4NAOJEP7vKOOQMeEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ef79b3.mp4?token=v_NcvBbXd18L7aSuYPSrTNWiMmjunbHVYRp8DOKwxxDO-NAF1I4epSGqZtpix46NBMxm704twsiWAjgQ1SVVhv-Pqz5lJ8tndMg5SkUD3R3WVZfRclEKWyxsbr7jXGEwQynqvtIBn-RmXmyS-J8I8sbU3r51KCn2sCo_3ZCQ1HbSfGTb5OXBSxkKJJ01P9rehoqbb0pvgvVES5Joq7wC6IE-t3bqMWCPpAwonmL7K13a0fHCnSFpLNM0_oNXmM131C4BdyHKdptRyP2wGRaGxce7qTfqmLt27XoVl97gzFiDF_SEwgCTTnLuUiu8KFMwbCFJR4NAOJEP7vKOOQMeEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که گفته می‌شود
از حملات امشب به بندرعباس است.
دقایقی پیش بندرعباس ۴ بار مورد حمله
قرار گرفت.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6166" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6165">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=XiJUj1zSu7Hnn_9Cin4LcILFAKHkVgxb3zZwJcsRH4JsTcZ8NjSXpyTL8o15ctdwfKOeQy_rlPbZc7ZtoLMrmKw6m8ihywm0kLWWIEZ3onka7hhVa2b_DesxNaRXc7onVFnfmNthg3As3J5NiM7dr105kdrtYJ91WOg9HEGazAUX0VHmeRHq91oqOwcSrIHrr1ERFE_ngIdNIqWZX8JRFgSgMdt67auhuNkw-6JCBt_4H3VQrwwounFuxLoH_uBxxtHJE2wj4JmonceidH4M_3efxjN15FmHCZdxBCdU9fBmDHnw_XYQqD1R5jjEJFR-tvUdMwdRbKyE7jgErGDiCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd6cb3b5f.mp4?token=XiJUj1zSu7Hnn_9Cin4LcILFAKHkVgxb3zZwJcsRH4JsTcZ8NjSXpyTL8o15ctdwfKOeQy_rlPbZc7ZtoLMrmKw6m8ihywm0kLWWIEZ3onka7hhVa2b_DesxNaRXc7onVFnfmNthg3As3J5NiM7dr105kdrtYJ91WOg9HEGazAUX0VHmeRHq91oqOwcSrIHrr1ERFE_ngIdNIqWZX8JRFgSgMdt67auhuNkw-6JCBt_4H3VQrwwounFuxLoH_uBxxtHJE2wj4JmonceidH4M_3efxjN15FmHCZdxBCdU9fBmDHnw_XYQqD1R5jjEJFR-tvUdMwdRbKyE7jgErGDiCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازغدی : اگر میخواهیم اغتشاش نشود
باید با آمریکا مبارزه کنیم
(که حواس مردم به جنگ پرت بشه
و تقصیر کاستی‌های حکومت بیفته پای جنگ
و دوباره جنگ بشه «نعمت» !)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6164" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6163">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
استانداری هرمزگان:  در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6163" target="_blank">📅 19:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6162">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amUx9ZE9aXuQYY9vWU9wWtDTNfZ6_VPW_K1TvK6Bq6e0m8NKG6GbvCi_iezXgVW-gU19l5X3CWDQdf5V1P2Kirsf7Rpr6iwO7aiHSU5pM9khrthvWuJnBk3q-AnnCFJCDr6oQW_bPrRCZ8G5_qGLlSNx2uih1Kxa88DuoWekNmDL87wg0BP4u-8aC2HNsxtQzleaqJmmJzmtLZ-jfXz-ZEbGcIg8ynInEhva403fKzamKiAO80FMNumRhqDumc9sY01-7KP7BUwl78sh7hpogipXaFoWH0kQUaYqbvb6Y-9siwUtQIDVbbvAUd7gllh13kNY86WEu41wdGJ6NGClww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز :
پاکستان به ایران هشدار داده‌ که اگر به عربستان سعودی حمله کند، پاکستان آن را حمله‌ای علیه خود خواهد دانست و اعلام کرده‌: «این خط قرمز ماست.
»
پاکستان و عربستان قرارداد پیمان دفاعی مشترک دارند که بر اساس آن حمله به هر کدام ، حمله به دیگری تلقی می‌شود.
🔺
برخی اعتقاد دارند که یکی از انگیزه‌های اصلی تلاش پاکستان برای میانجی‌گری میان ج‌ا و آمریکا ، نگرانی از وقوع جنگی است که دامنه‌اش به عربستان برسد و پاکستان را ناچار به ورود به این جنگ کند.
اینک که تفاهم نامه کنار رفته، پاکستان بیش از پیش نگران این موضوع است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6162" target="_blank">📅 19:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6161">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
استانداری هرمزگان:
در ساعت ۱۸:۱۰ امروز نقطاتی در قشم مورد اصابت موشک‌های آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6161" target="_blank">📅 19:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6160">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-55mN3GBWusrR6khC7Dtx21ElU5lET66U0NiZLWXAJMuqm8wo58trqui9g0SO9PozMI0MK7i4RzklrovBc2XDFo9K5931LqQrDHmBAdKa_mvUo_vu0QpFqAyxBEAnXMl_2_R4hwcC0mSSpxRCwYiPoMQhRV7GAMfeqmKg3BlpUAMi4_h1hIY6X3NtWkl9ini5U-7dX4yXOXKVsunb3lWsLiq3WM4kZHvigDaNiKJ8F5iXvimT0eCyNzAmsjfcs57IP5ZsNJD3Kf_IDWXOsiRhmjZZG7_1mEZptwlbE0olD0PPuzpN3g2Sz0dn2E6X4q6DJvk0xeYDlyhjyUUqsoWSes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0a471388f.mp4?token=jImyMp-059WAcGn1XBh77Z-ypxcO5RsOppGVegn-I1UznT3UYMBIlE4YfQml8P2acQD5FIv6-lpI6f0IYn6dXORZBQ-y3lte-vKFR5i3vkKErOiXF_gIWIkV4V1q52e7lmQsz1SjZMxA7AvfiqUMGnpRsHEFaagzcOxoIQZsXCFKhkxPP5qVlyf8f4s3VCiKZfk_QLuXKA7YwqHZD76ku7CyOxK8UNnPvwM04SxC2WM1aFDxPFMuglqkEbLvmmvbPE0b_aOY3QoW6Ok1L8OXg_FxoAgPRLv2BMmavgMWGaK6kUMKnghlkrAYRnslePkQD3YDI_NB7ZfNNM1udxdS-55mN3GBWusrR6khC7Dtx21ElU5lET66U0NiZLWXAJMuqm8wo58trqui9g0SO9PozMI0MK7i4RzklrovBc2XDFo9K5931LqQrDHmBAdKa_mvUo_vu0QpFqAyxBEAnXMl_2_R4hwcC0mSSpxRCwYiPoMQhRV7GAMfeqmKg3BlpUAMi4_h1hIY6X3NtWkl9ini5U-7dX4yXOXKVsunb3lWsLiq3WM4kZHvigDaNiKJ8F5iXvimT0eCyNzAmsjfcs57IP5ZsNJD3Kf_IDWXOsiRhmjZZG7_1mEZptwlbE0olD0PPuzpN3g2Sz0dn2E6X4q6DJvk0xeYDlyhjyUUqsoWSes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرنمایی جدید جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6160" target="_blank">📅 19:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=fqsSNoj4399UwINrHTcJrChepjtgjzgqiWr1NNd_iQTTESex58JkILZXxHH7dNrneBya0t4CsmixrnJM7K92v9O4koB2YIJmBN3bYeaLaeqckYk3aE9VGeJO4UTsK-yQIWr4lOOASsBQx5KhDkOTqiAN11PKauI1Ni5NTRCCGg8CHA0s6szpLpL-NpL0rvzPp2FWyXb7Mxd_gXpZfck5bTeUnZTHvGpy7tpkgqYGpmLeBf8NohKuLkw1d7Irn-raoh_r0zjL1XetvQSxOGkh-HB9VOSPAeCb_hSMLrMCSKAyBbTV4l0YQHWoMoIgcSjNwADsUTDvTxOEPz51aaXhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfb27a8797.mp4?token=fqsSNoj4399UwINrHTcJrChepjtgjzgqiWr1NNd_iQTTESex58JkILZXxHH7dNrneBya0t4CsmixrnJM7K92v9O4koB2YIJmBN3bYeaLaeqckYk3aE9VGeJO4UTsK-yQIWr4lOOASsBQx5KhDkOTqiAN11PKauI1Ni5NTRCCGg8CHA0s6szpLpL-NpL0rvzPp2FWyXb7Mxd_gXpZfck5bTeUnZTHvGpy7tpkgqYGpmLeBf8NohKuLkw1d7Irn-raoh_r0zjL1XetvQSxOGkh-HB9VOSPAeCb_hSMLrMCSKAyBbTV4l0YQHWoMoIgcSjNwADsUTDvTxOEPz51aaXhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، تیر ۱۴۰۳:
ما غنی‌سازی را ۲۰ درصد کردیم جنگ شد؟ ۶۰ درصد کردیم جنگ شد؟
hafezeh_tarikhi</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6159" target="_blank">📅 18:44 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
