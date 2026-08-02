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
<img src="https://cdn4.telesco.pe/file/AfcILezzwYHZNbc0Dx8ZI4rh_G7jP7EZhqh2YyOliUjfgbcxjyJMKypq7wSKu4pSd-wrF4rtE_deyZJ6ctpkShhv0gmna9R2gJ0VAC7_qJgHwC08KcIhl8-8J3cMb8q2XhR3I8SXzVA90HaDHfRrGL-tEaD3PmjttuiPF7AWGsr8P3FadUyhsfo2VcCje4MmdnsPuw2mBcMPx7Ppm7Hy7OOBZZ4nJgj1i0u3D72tABB2DLJgnHbnnBbqcjjXNZYiagMlhg1Jpf1tv_0BEdG1FaUcvr1gdsURiJ-HbUojLzcCBBFmcPSKERcshazC4hgVaxMrpMDDnGHtxd74vBHF8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.07M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 22:26:43</div>
<hr>

<div class="tg-post" id="msg-677853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvNnmC6IG9KBmoQArTacDGRR_fC0d8OkGJ5ut9KSc_pJrLra3dT65NZBJxQNDECm-buoJ5d5UHAISlrGlzaBXw-TgbOtWu0EuhRc55_CxV-TeaullfpKrmctGAXP2fBKBZWTxtqId9cP5lf5JpUjf4BbR_VYrSmieWggnXN8vBD8vfEdOTZpN3HL1bz5xb-hk7Azo8H89FVAA379QfTQjA5eMftX1RHlTnEHF9zE6GcHN8CasbcvlgxNSKgmkFnsQtPuB5pQ2QjuBxRgn-At5vlOFfH_f-obrElRmdholCpBgOCwUIUzHXHyLNIYL891fVUPuF8EjkhYXfQXtUOvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت پیکر دریانورد جان‌باخته و خدمه کشتی تجاری «آنا» به کشور
🔹
پس از گذشت یک هفته از حمله اوکراین به کشتی تجاری «آنا» در آب‌های فدراسیون روسیه، پیکر دریانورد جوان جان‌باخته این حادثه به همراه ۸ نفر از خدمه کشتی و با همراهی مالک کشتی، امروز به کشور بازگشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/677853" target="_blank">📅 22:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677852">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مراجعه به بیمارستان‌های دولتی ۳۰ درصد افزایش یافت
محمد جمالیان، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
هزینه‌های درمان به‌ویژه در بخش خصوصی به دغدغه اول بیماران تبدیل شده است. مراجعه به بیمارستان‌های دولتی ۳۰ درصد افزایش یافته که نشان از ناتوانی مردم در پرداخت هزینه‌های بخش خصوصی دارد.
🔹
بیمه‌ها با کمبود بودجه مواجه هستند و ماه‌ها است که بدهی‌های خود را به داروخانه‌ها، بیمارستان‌ها و فیزیوتراپی‌ها پرداخت نکرده‌اند. پیشنهاد تزریق ۱۸۰ همت به بیمه‌ها برای کاهش فشار بر مردم به مجلس ارائه شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/677852" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677851">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2e000076.mp4?token=WVStMu0awa0rX1Z8a8w6r82JiDuFlhmyPYdl_Bugqphke6WYdy_3LrkFQwgvEWuV-w2dHtzn5hjGehx6FajsVyE74ILPzGg71gG-LfVP_KWUvuQiCbzSxd8vGXNlUfVB3oi6FMDuNqpknaIGJE2VFtm5MDUCqN70CeuEomw5eL_VuemIIf71A13a2AEHLaZcg-UBydUVsoSs--OdYIkE7MFs1tskttwmCqIpTLFsVigQVtqQvnkSaXq3YncVFxClkRr9vIC3cGN_lPmb7uEFVrhFSaieEM2wKfFWN4WdlrZAkjephKxUHqQJBYV42YofdOPeLGSqfa0l0kHmFy0kTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2e000076.mp4?token=WVStMu0awa0rX1Z8a8w6r82JiDuFlhmyPYdl_Bugqphke6WYdy_3LrkFQwgvEWuV-w2dHtzn5hjGehx6FajsVyE74ILPzGg71gG-LfVP_KWUvuQiCbzSxd8vGXNlUfVB3oi6FMDuNqpknaIGJE2VFtm5MDUCqN70CeuEomw5eL_VuemIIf71A13a2AEHLaZcg-UBydUVsoSs--OdYIkE7MFs1tskttwmCqIpTLFsVigQVtqQvnkSaXq3YncVFxClkRr9vIC3cGN_lPmb7uEFVrhFSaieEM2wKfFWN4WdlrZAkjephKxUHqQJBYV42YofdOPeLGSqfa0l0kHmFy0kTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش سخنگوی دولت به شوخی‌هایی که با او در فضای مجازی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/677851" target="_blank">📅 22:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677850">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=ZSaWjov-q5vJs-LeDJWGDH4fGYX19IET-9WcYGGY4ikqMN7OEKwyOEQskrgdDXVXswpJYxtCem4veiq7nDu-d6iel0ogYVPQelm5uiGAUNr0tcZjdbgPgmA4jG_Hx9km6Mr--wp-QDb457s96qJPO01wENG_JU6GBJpLeHzEitWkBFL1C2GKX78le7UfrwEkMEUCbcs1UyJgzR3Wg6D1HIRtSkIejyAYrkCimmkLaxkx9E_5c9PoLCa1sHfq57cCoGMyOJ8XKO5X-0sKDfcOvFFdmdQl1YkqiFwDbQQGSNrMX7-zI5UAKdw-v9Bp1U9MTpBJ-J2_lfLPVd3zKbBA5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40631b97ca.mp4?token=ZSaWjov-q5vJs-LeDJWGDH4fGYX19IET-9WcYGGY4ikqMN7OEKwyOEQskrgdDXVXswpJYxtCem4veiq7nDu-d6iel0ogYVPQelm5uiGAUNr0tcZjdbgPgmA4jG_Hx9km6Mr--wp-QDb457s96qJPO01wENG_JU6GBJpLeHzEitWkBFL1C2GKX78le7UfrwEkMEUCbcs1UyJgzR3Wg6D1HIRtSkIejyAYrkCimmkLaxkx9E_5c9PoLCa1sHfq57cCoGMyOJ8XKO5X-0sKDfcOvFFdmdQl1YkqiFwDbQQGSNrMX7-zI5UAKdw-v9Bp1U9MTpBJ-J2_lfLPVd3zKbBA5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نامه‌‌ای که دختر شهید مدرسۀ میناب برای پدرش نوشته بود: تو همۀ چیزی هستی که من دارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/677850" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677849">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کیف پول ایرانی برای کارمندان تصویب شد
🔹
امریکن ایرلاینز پروازهای خود به فلسطین اشغالی را لغو کرد
🔹
قهرمانی نابغه پینگ پنگ ایران در رقابت‌های کانتندر جوانان لائوس
🔹
خروج ۴۰ درصد خودروها از پارکینگ‌های مهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/677849" target="_blank">📅 22:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677848">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdWqTYwKv532hnweOwG0eflMi_TsYLghFIcKIYORIQ4-N1HXW5STKlgGGDsTxXpoBEW4HITQk2MGihEJBAOVkqVEYRet4qGzHV9T2ZyuqZkR9GxRMIlPtOG6Sl_fQ5AvBUJs3ugb75__U1ymZpnNGTy8iH8rPoxTG-Odccq7hwAliKeCV6T5ZflI-NLP9BM0Zfxdqc5bH_gEGZPXTIobTR4-BEyHualnFqmNi2qVml86O9vHb1jo2l98OzR_WUuLkSftXwDoKddK5L05IyckfJfQkyw3UdFWVUZ9LgewzHG8ufXTlQNZWxzRketD0bOUPPVk9_jeLoByWZWEQ3OsUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رسانه ژاپنی: پاکستان میانجی شد تا ۱۰ میلیارد دلار وام از آمریکا بگیرد
روزنامه نیکی آسیا ژاپن:
🔹
پاکستان برای تقویت ذخایر ارزی خود، درخواست دریافت تسهیلاتی تا سقف ۱۰ میلیارد دلار از آمریکا را مطرح کرده و در این مسیر از میانجیگری در موضوع ایران بهره برده است.
🔹
با این حال، کارشناسان هشدار می‌دهند موافقت واشنگتن با این درخواست می‌تواند به افزایش نظارت آمریکا بر بدهی‌های پاکستان به چین منجر شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/677848" target="_blank">📅 22:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677847">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Veglpo4S2--qrdGUkR_8vdcoS5IO0rvnLOiXB0dBhBy0XZDQ-Y_fqaYLNmWAn3-n_R1e5jKnn9nMMmFXR9pR5H_85-aarQGf7RwTllWEztN447DklOEqecGHrSHrmJIO0nCF7_YodZor4m-VoUJ3Cc5sNR4juTALC0CJvgoM-3w76UNCy5mk_eX4bUYyWCLFeI6EufY12oTZfR2k3UZQQL-CpUxtj5UPb8rY7t_F1-Q-3nZgJHCqHfIVrfTV1S8WFyKvVGsTV1k8wXfwIxmbkPBPDuIKiOKdScukChdP8UeND-4ot59ifWDHAxvsKi3Kho-OyLOLterprPbC6W9PgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارزش آدم‌ها فقط به حرف نیست، به کاری‌ست که درست انجامش می‌دهند
🔹
در نگاه امام علی(ع)، انسان با توانایی، مهارت، دانایی و کیفیت عملش شناخته می‌شود. هرچه انسان در کار خود پخته‌تر، مفیدتر و دقیق‌تر باشد، جایگاهش بالاتر است. این حکمت یادمان می‌دهد که برای ارزشمند…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/677847" target="_blank">📅 22:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677846">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
قاتل را بکشید
🔹
پرچم بزرگ دانشجویان ایرانی در پیاده روی اربعین و فریاد خونخواهی رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/677846" target="_blank">📅 22:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677845">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Fg2K4OpQ_x_KLZur2sQxk7ChX_JhhLZySPeLE5CQRsXHO2gM-24QPUu-hdKD1kka_nqa3Dow_RalIy3x4f5aP1DWE8x_LekPvdnsIYuLeJGHQgBEbUU1qvZdcKudmhdAl4xZO2TiM6kP-Jg9CuCnEX5duKM97RdjE43ovQ3vkW7K3U5MTqU14P_Pod7sPpKAht98LaMVcatXjmq4kEowHyKURi2mjw4UJ08RPSifxkO4YM-60BXT-WW4nGfdqRkIyFoCyF-NIsAJx3gSJlrya1dv08ky_TPVE3Vbmnyg1OPoStqpn6xZkD53xHXY3xmdBfnDUeztzkyUeibT-JXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/677845" target="_blank">📅 22:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677844">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2241265b.mp4?token=tAStjb-85Kg0WX22NSudcqzCnOFsFJOwDMzDKj8S-u7iMemLS_XN1YCbuT6nlXNUOwkqfdK-Fzyw8_1p35ho6qD519wa3JuenJieu6q8gZ0AIIvkPhntaGxiVSY2-wpzSe-6ik8IJlZ6-y7vUZ_B3skeUMHUxh0gnNPNthQPOcwD8qQvCSQoSgfgTQWkanfo9T6Rr2ehnnG0ni1SSslz2j6jCb4vmIgyRuMJizn6WcgLaCow23SydiDlaKpkdqxKqiBgzyIkPh2_tEHg-o6h1UgG6vvzpiWw2VZn1bkcOBwMC8_o1itBfHd7WcaSLLGmQNr_yxMe4MwRUlDoUYAf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2241265b.mp4?token=tAStjb-85Kg0WX22NSudcqzCnOFsFJOwDMzDKj8S-u7iMemLS_XN1YCbuT6nlXNUOwkqfdK-Fzyw8_1p35ho6qD519wa3JuenJieu6q8gZ0AIIvkPhntaGxiVSY2-wpzSe-6ik8IJlZ6-y7vUZ_B3skeUMHUxh0gnNPNthQPOcwD8qQvCSQoSgfgTQWkanfo9T6Rr2ehnnG0ni1SSslz2j6jCb4vmIgyRuMJizn6WcgLaCow23SydiDlaKpkdqxKqiBgzyIkPh2_tEHg-o6h1UgG6vvzpiWw2VZn1bkcOBwMC8_o1itBfHd7WcaSLLGmQNr_yxMe4MwRUlDoUYAf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوابیدن روی زمین؛ درمان کمردرد یا یک باور اشتباه؟
🔹
واقعیت این است که بدن هر فرد متفاوت است. بعضی افراد روی سطح سفت احساس راحتی بیشتری دارند، اما برای برخی دیگر، به‌ویژه کسانی که مشکلات ستون فقرات، دیسک کمر یا درد مفاصل دارند، این کار می‌تواند باعث تشدید درد شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/677844" target="_blank">📅 21:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677843">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/himWF_yAqspP3pZCyFR3Ch7s8BttPYmppw0Ltx63Oli01fS0Y7AuPYgGrGoKTX07xGbfwzEeEvjasiX-r-Y7t9F04okuI8dOyb1k99DyjO2bjALlyL4cVEbfRSjOW-zbxJxKNDtc8fciZpR4w_xbP-mxfPkYRTTm78aMQnT6gxd5ij5utXOtWq1SF-3p7qLbZ2mm2FZZPInFFFXgDDp_o9-EcRX8X0mH3ktwd9aWIkGfBXGDLhZ7ynn6rFCRPCVYJC5REKBdmuMKS0KPU36aeN492UIO4X51GEJLD-Ixg061NgNzb99XOpoBahS8fHTgC1PjVi6n0PiILRcAj786eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا می‌گویند «اشک تمساح»؟ حقیقتی که کمتر کسی می‌داند
🔹
وقتی تمساح غذا می‌خوره، به‌خاطر فشار و هوایی که داخل سینوس‌هاش جمع میشه، از چشم‌هاش اشک خارج میشه و این هیچ ربطی به احساس پشیمونی یا ناراحتی نداره.
🔹
به همین خاطر، به کسی که الکی خودش رو ناراحت نشون میده یا تظاهر به غم می‌کنه، میگن: «اشک تمساح نریز!»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/677843" target="_blank">📅 21:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677842">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f53b22d86.mp4?token=PXAZFFsVSXRPr0AjNp8KCA0-Ras-Ffehq8XTOEZKdJ1eE0RwrdxPeI5hn4pLEpNshmrBHon2E_GgGdiMGS9Wc-pYouLQBzrUbxjEdXGwFE6oojgHaLkbCLYM5NI9whFoULy6aMdbQuiKAvYA4Vqjxk17_tZBJzBF7NuabnA-wGynCflKAE37faUIwacOWe44mLN6zC26BoAz2HRmQxvbCRXM81RjxtCcrC_7dNBvHEqIvz9vk6OcfpuUz1IzpXE9cBrWw1uqqJ1-8UYKq_hckSULyIn8JabqdKwwxsXPFMp24A_FJmb9b8a687ZkrBOvse1P-Tb0SEHf1bs12VfxGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f53b22d86.mp4?token=PXAZFFsVSXRPr0AjNp8KCA0-Ras-Ffehq8XTOEZKdJ1eE0RwrdxPeI5hn4pLEpNshmrBHon2E_GgGdiMGS9Wc-pYouLQBzrUbxjEdXGwFE6oojgHaLkbCLYM5NI9whFoULy6aMdbQuiKAvYA4Vqjxk17_tZBJzBF7NuabnA-wGynCflKAE37faUIwacOWe44mLN6zC26BoAz2HRmQxvbCRXM81RjxtCcrC_7dNBvHEqIvz9vk6OcfpuUz1IzpXE9cBrWw1uqqJ1-8UYKq_hckSULyIn8JabqdKwwxsXPFMp24A_FJmb9b8a687ZkrBOvse1P-Tb0SEHf1bs12VfxGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری | حضور به نیابت از رهبر شهید در مسیر اربعین
🔹
منتخبی از پیام‌های صوتی مخاطبان «خبرفوری» که در مسیر پیاده‌روی اربعین، قدم‌هایشان را به نیت «رهبر شهید» برداشتند.
🔸
صدای ارادت خود را به ما برسانید
👇
#زیارت_به_نیابت
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/677842" target="_blank">📅 21:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677841">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083e4068c2.mp4?token=JhKMcqc5BI3gjo1bzD1FeOjIKIJywIZ6WIjC5Q1o5ZHKhw4g6UhISmgSGWVME3mIKGpT_zMl0j5dmSt9wS2WWQKlbL8doKAr8ZDikrRWg4-iYMDDRGWVGLdZf4jWSFxCsqoSekub4YNcUFA1jF43nIpdoav_VwW4NINzmMHMIX4hfNQPwH9xAij0bSz2sccuSNPfhUUoWQ5XB66t8aVAfcC1TT5leDq0VFMGxi_07sXX3uWGMfm17w91hDZya6XFEj_YN6gnwCqfeiqJZ8BPpUv6yXcSRMruOLdg7adttMDhFTspr1THtAte62HWkl511aKGrVmr4OWeZxwZIcINnFEaTZpkNsrKi1bQ3UYVYynvrbTSXcI4mLW9hATNkyWUoh2AdhvxvUQi2xd6ulvvxZabZz5YFMwNFyb5seHd-7plu8HhSkRxU0rGmvxOH7SLc1M0AoYhTcTgYXolidKrFA9FuAhRxyC8HBq9DZ2YzC-3WfH0lc0URuWW_lIEHHSHvd4OLwKu4NmlUzPV31EIcrAFGpzStxYu-BpzVGvucuhAIeg8QQAhEgvZRz6uz9G6A4e20i-nIcUPRaVN8yN0TJh6qYr2Hz2NM_13yWipWDhTjS6oCdteGItcvMDArouT4gqUMwU9kMbVkNJa-R-Vgp4Ow3XsR7oX6WneLHZqpVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083e4068c2.mp4?token=JhKMcqc5BI3gjo1bzD1FeOjIKIJywIZ6WIjC5Q1o5ZHKhw4g6UhISmgSGWVME3mIKGpT_zMl0j5dmSt9wS2WWQKlbL8doKAr8ZDikrRWg4-iYMDDRGWVGLdZf4jWSFxCsqoSekub4YNcUFA1jF43nIpdoav_VwW4NINzmMHMIX4hfNQPwH9xAij0bSz2sccuSNPfhUUoWQ5XB66t8aVAfcC1TT5leDq0VFMGxi_07sXX3uWGMfm17w91hDZya6XFEj_YN6gnwCqfeiqJZ8BPpUv6yXcSRMruOLdg7adttMDhFTspr1THtAte62HWkl511aKGrVmr4OWeZxwZIcINnFEaTZpkNsrKi1bQ3UYVYynvrbTSXcI4mLW9hATNkyWUoh2AdhvxvUQi2xd6ulvvxZabZz5YFMwNFyb5seHd-7plu8HhSkRxU0rGmvxOH7SLc1M0AoYhTcTgYXolidKrFA9FuAhRxyC8HBq9DZ2YzC-3WfH0lc0URuWW_lIEHHSHvd4OLwKu4NmlUzPV31EIcrAFGpzStxYu-BpzVGvucuhAIeg8QQAhEgvZRz6uz9G6A4e20i-nIcUPRaVN8yN0TJh6qYr2Hz2NM_13yWipWDhTjS6oCdteGItcvMDArouT4gqUMwU9kMbVkNJa-R-Vgp4Ow3XsR7oX6WneLHZqpVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف بی‌سابقه فرمانده سابق واحد ۸۲۰۰ اطلاعات اسرائیل: تاکنون موشک‌های بالستیک ایران عامل تعیین‌کننده این جنگ بوده؛ حالا ایران معادلات منطقه را تعیین می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/677841" target="_blank">📅 21:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677840">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
کانال ۱۲ به نقل از منابع امنیتی اسرائیل: رئیس‌جمهور ترامپ ما را در وضعیت ابهام و بلاتکلیفی رها کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/677840" target="_blank">📅 21:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677838">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
یک شهید در حملۀ تروریستی به یکی از مقرهای ارتش در مریوان
تیپ ۳۲۸ مریوان:
🔹
در ساعت ۳ بامداد امروز، عوامل گروهک تروریستی پژاک با استفاده از دو فروند ریز پرنده انتحاری و شلیک راکت آرپی‌جی به یکی از مقرهای این تیپ در مرز حمله کردند.
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/677838" target="_blank">📅 21:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677836">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۱۵۰ حزبِ ویترینی؛ باهنر پرده از «نمایشِ حزبی» در ایران برداشت/ خاتمی در مجلس به اصلاح‌طلبان گفت دو ملیون رای خود را بردارید و بگذارید من با ۱۸ میلیون رای خودم اداره کنم؛ احمدی‌نژاد هم با اصولگرایان همین کار را کرد
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
تمام نمایندگان، ائمه جمعه، وزرا و مجمع تشخیص مصلحت نظام عموما به دنبال مطالبات غیرممکن هستند.
🔹
امروز یک نفر در کشور ما رییس‌جمهور می‌شود بعد می‌گوید حالا از کجا وزیر بیاورم. آقای رییسی یک سری را از آستان قدس و یک سری را از دانشگاه امام صادق آورد و همه آن‌ها وزیر شدند.
🔹
آن بیچاره‌هایی که در مجلس نماینده ندارند مردم بیچاره هستند. حوزه انتخابیه سراغ دارم که در ظرف ۱۲ دوره مجلس ، ۱۲ نماینده به مجلس فرستاده‌اند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/677836" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677835">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74471ab558.mp4?token=s7NTc-TxI443QN42KpcYHFk7Fj1NO3Hag8XWpb12t7cC-i-I6qqlWo5v8F508nfwJo0SV5q-xSlKgFSf9MZ2StA2E45MnNno-Q1Gd2qtyPJbyCnXwhzxsCDf4iyofdkmlZFtpmo89NIZAziXXYMbowGxKRTQnVSgyUEckNQVQaGnJMUIIhxg48X-DwyV1AWg8K0fBfcI3hPohzVRFgPgyxPtrXAKmRGSMPXcRTbOXiZO4XeJHUiq7qUY8fnFDJpBlsWw0RjXNk3kdh086v4yL01v_X2HDDbYUxo-ypScwqun5wBbbX4pPXVIRa9aqDHFp7U0Gq7aKc7X61Ax_Fzdrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74471ab558.mp4?token=s7NTc-TxI443QN42KpcYHFk7Fj1NO3Hag8XWpb12t7cC-i-I6qqlWo5v8F508nfwJo0SV5q-xSlKgFSf9MZ2StA2E45MnNno-Q1Gd2qtyPJbyCnXwhzxsCDf4iyofdkmlZFtpmo89NIZAziXXYMbowGxKRTQnVSgyUEckNQVQaGnJMUIIhxg48X-DwyV1AWg8K0fBfcI3hPohzVRFgPgyxPtrXAKmRGSMPXcRTbOXiZO4XeJHUiq7qUY8fnFDJpBlsWw0RjXNk3kdh086v4yL01v_X2HDDbYUxo-ypScwqun5wBbbX4pPXVIRa9aqDHFp7U0Gq7aKc7X61Ax_Fzdrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برگ بو فقط یک ادویه نیست؛ از خواص باورنکردنی آن خبر دارید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/677835" target="_blank">📅 21:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677834">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b51a0ad3.mp4?token=hJxIwUYimOaKe_JWd8jBx5tcav9Y_UFFy7GMF-4LXOVOXYaJHGpUM2vpvYnB50tZqgRPH4XJjPAzPLWStkdlu4Mn2ObPUo31KsXxsudOgriTRvgImvdf6TQY654hFC1tpqG6GWLoN023jKBs13o-luSMjX-Qe9O-QrmW4mmFqR8dUK7ZWABVjZnmRH_GhY26YUKoswQIUUYBFfymMpmdXTpzMpM0Dzy-3UzVJevpRzq4qyBGibStR-n-dIQ7za0fF-r2-P_8AdB1CimfYq7C0TvA_0Hrgr3GF-4lvTIi4alCN5WH9JMVvWQg-q1DuYpaJBUgajATeiHVYGiaN4EhHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b51a0ad3.mp4?token=hJxIwUYimOaKe_JWd8jBx5tcav9Y_UFFy7GMF-4LXOVOXYaJHGpUM2vpvYnB50tZqgRPH4XJjPAzPLWStkdlu4Mn2ObPUo31KsXxsudOgriTRvgImvdf6TQY654hFC1tpqG6GWLoN023jKBs13o-luSMjX-Qe9O-QrmW4mmFqR8dUK7ZWABVjZnmRH_GhY26YUKoswQIUUYBFfymMpmdXTpzMpM0Dzy-3UzVJevpRzq4qyBGibStR-n-dIQ7za0fF-r2-P_8AdB1CimfYq7C0TvA_0Hrgr3GF-4lvTIi4alCN5WH9JMVvWQg-q1DuYpaJBUgajATeiHVYGiaN4EhHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور حجت‌الاسلام محمدجواد محمدی گلپایگانی داماد رهبر شهید انقلاب در مشایه نجف - کربلای اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/677834" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677833">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyTPSAER4K_vj7UkS3MJ0GO7h547LGAPwVAybW9wH7r3mLyhRZuoy7amrYK0Nufgjf8Ozl4v9heoi9jc42Hs0fOk5brTbzDVJMF2Ci7rnL6_7ZLrmCycRSXHlYcGwZPuw-rpHlWPbawPnkgDaQjTw1_pH5dXjWD-CfHaP8HJNHU4EBfvr7muxScEy_VHJ72Ge1yufGA2etzFy8Wz9RXEtDDKSniFiXWbdxMxk_ROmZYnCOJVc9yOr1p0Pp1eQxhcroPV9MXtuzuX-VW9-9uFh1s530JOgQGwZhYAzI1gX1joYMAq7mwSmz8koU0Oov6c6PJou52Jb3y92anF1qrf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه مرموز نتانیاهو و ترامپ/ همه‌چیز درباره احتمال محاصره زمینی ایران
🔹
به نظر می رسد آمریکا توانسته رضایت کشورهای عربی را برای محاصره زمینی ایران جلب کند اما این مساله (در صورت صحت) کافی نیست. برای محاصره زمینی ایران باید دول مهمی مانند دولت ترکیه نیز راضی بوده و با ترامپ و اسرائیل همراهی کنند اما اردوغان نشان داده که با ایده محاصره ایران موافق نیست.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3234830</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/677833" target="_blank">📅 21:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677832">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxJGp52zEahdHh7xYrPWVUTegrFSFasRcWEKn-w3TMhTFAeLI-UJRhdNm1WBEraIYmaiwb9EO2rOQFLtMtzUNOMYPm-O5lDfGesCDNR4T9R515DwWDk2KKzcGZ2XAIucwl8-aTHt7LNyELlwJj0lz68xswmHpIgxirdZ0dfElaP0bCL-Vhdm51ON4sNlsd4EO8ArEAhmO7JGREcryVT4eM3uJCfL_LV9qSgWY3Ei-02FQU8970mTSt30dH19kAGWtgqdTq71OnbwjRGt9Hsy2WTPHT70XSWbvg_Kl73tROOX8HeDd4aUKkXV3jyNuvBD6z4QEMJ96Kvusqh3rnOuGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعضی آدما مجرم نیستن؛ فقط در جای اشتباهی به دنیا اومدن
🔹
ژانر: اجتماعی | درام | جنایی
🔹
خلاصه:«مغزهای کوچک زنگ‌زده» تصویری بی‌پرده از زندگی در حاشیه شهر است؛ جایی که فقر، قدرت و خشونت سرنوشت آدم‌ها را می‌سازند. فیلمی تلخ، پرتعلیق و از ماندگارترین آثار اجتماعی…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/677832" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677831">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owQgHcKcoMYZyceRF_i3Dl73L7KlzcSqfg2AkTt_mOM_w2rEuTl6CkQFapz2RGSeAlDvjebKxIVnzjNea5gdKq97XMLCYZjZMutuOvT0b9gFo2FT2FGDRyssKmjo4BonYV0n346rIMXUQUaejbG7gG_KWE-kaC3tTNyCEMqfgmrt5dJalwrVybnEn_ozWWJsdkj1r6Qhi7_8i8RXFwrQxR401o34tq_WGk13Gpv2F5aFQxEa1qk9rMy5OLuO0bcNq8PLFO9t786dxHcGj-ZvOTGql973-ICuVBvDu9gYQk8Bh6kQdgf9e7qq8X9dltpykUy1EI5uz0ILopQATqbN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش ها حاکی از ادامه خروج نیروهای آمریکایی از اقلیم کردستان عراق است
🔹
باتری پدافند هوایی MIM-104 پاتریوت که در فرودگاه بین المللی اربیل مستقر بود نیز به کشور دیگری در منطقه منتقل شد و مورد اصابت موشک ها و پهپادها قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677831" target="_blank">📅 21:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677830">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bf5BHpjZZGi7WjD79C2SkGsu1sYpTn1HobBMAwLFtwfdBWLMc_S6WDq7Wpap9eN7BHkGdNCJfQM2tVg0zxpHdv6cnT6bsn5T5y4pLJDpAhA7fYv8j78Ij-_NAYYSOMjjZyZchv4Nm5NNuf6JK27BeCS06QPiTBxRt2F4ReX0DQY-V7z7TQRpZX9WOqgMe7tgkeyIGK66Dj4W4VslI9Mnl8x601s73JvwbE31YIhMMvv1SY_vjf5fAlqbgj1AH-s30PFEjCY9E8tUP1wJH1x56x7REO335A9-tpLSQ59wdMCJqUT76k9Jf7fNznolZXt8mK7eVClTFKunOzwBfV6JxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مدیریت راحت‌تر هزینه‌های درمان با بیمه تکمیلی انفرادی
بیمه تکمیلی درمان انفرادی می‌تونه خیال‌‌تون رو بابت بخش قابل توجهی از هزینه‌های درمانی راحت‌تر کنه.
خدمات قابل پوشش:
• هزینه‌های بستری و جراحی
• خدمات پاراکلینیکی مثل آزمایش، MRI و سی‌تی‌اسکن
• ویزیت پزشک و خدمات تخصصی
• بخشی از خدمات دندان‌پزشکی
✅
با توجه به تنوع طرح‌ها، می‌تونید گزینه‌ای متناسب با نیاز و بودجه‌تون انتخاب کنید و با درنظر گرفتن فرانشیز، سقف تعهدات و دوره انتظار، انتخاب آگاهانه‌تری داشته باشید.
👈🏻
دریافت مشاوره رایگان و استعلام قیمت
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/677830" target="_blank">📅 20:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677829">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
مارک کلی: رفیق املاکی ترامپ مناسب مذاکره با ایران نیست
سناتور دموکرات آمریکایی:
🔹
ترامپ کسی است که ما را بدون هدف راهبردی، بدون برنامه، بدون جدول زمانی وارد جنگ علیه ایران کرد.
🔹
ایالات متحده در حال شکست است و آنها گیر افتاده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/677829" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677828">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: کشورهای عربی از راهکار نداشتن ترامپ مقابل ایران ناامید شده‌اند
نشریۀ آمریکایی وال‌استریت‌ژورنال:
🔹
کشورهای حاشیه خلیج فارس در گفت‌وگوهای پشت صحنه از فقدان یک استراتژی شفاف ازسوی دولت ترامپ مقابل ایران ابراز ناامیدی کرده‌اند.
🔹
کشورهای عربی خواستار تضمین‌های مداوم ترامپ مبنی بر حمایت نظامی آمریکا در صورت طولانی‌شدن این درگیری‌های متقابل شده‌اند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677828" target="_blank">📅 20:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677826">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OqWMMTjB8ec9fG_46VUIwukoHBQH-laDWTuF5csdcYQXJ1I2CbVxxNrGdjOqo1GjLhF4cekxPsDgdUGy8Vo2YjoyDsA1ALqP3qkg_WPdAuq8SVj8em_CCPD7epNNVmTTcLJDcxdDqVp0Y3YfF2YT2ZN_BZF72H2jfdlpEDC7C6f8Fb1-lst5JmLKadEbypTlg8ZH55Mjw5HXomE9n5Tsf8ju8hnrldJS6I51Ij5VhNF8NW6k5N37xvbZBNi_-3ZECHzI_BJfUwSYONgabBswYurde6FyaBaUuoUFMa5ptIz5DWCCXBiiK9c9Nf50OHd6uJmXuB4kay605zS6e9jB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad9X1CP2_QvimpAhR_y9K2PrXyQdjRVStDSWiYEeovrSPVJxIsuqheYSHtAGp3616i5G8mlZZBrATipnhOHEVrjlwi9CbMJUztfSdhdn_FGRVWor_AmjXwenUJAAHupC8dadOjYTsuByieXDIvo63fk8K8_klLAWDDmOnwI8CJ9iVlyRtP2HD_tEoY-OWfz-nCT40AZyWO8Gjb-DjXX-DLISEl3jmxPVXa9Rbze86ft0DZrEOqLPx5743F4TZZ9U7RphBNuxlLJG5Cie5c-hD-yXJyG4qJETRxbVozt8_zTltwlIufi84K91hu_7jEG4CWce8Kb3-kanhpMujgKgIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران ۱۰ درصد گچ جهان را تولید می‌کند
🔸
بر اساس آمار سال ۲۰۲۴، آمریکا با تولید ۲۲ میلیون تن در رتبه نخست تولید گچ جهان قرار دارد. پس از آن ایران با تولید ۱۶ میلیون تن در جایگاه دوم جهان ایستاده است.
🔸
در مجموع، تولید گچ جهان در سال ۲۰۲۴ به حدود ۱۶۰ میلیون تن رسیده و ایران با تولید ۱۶ میلیون تن، حدود ۱۰ درصد از تولید جهانی گچ را به خود اختصاص داده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677826" target="_blank">📅 20:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677825">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
انتقاد پزشکیان از برخی روایت‌های نادرست درباره جایگاه رهبری
🔹
پزشکیان با اشاره به منش و رویکرد رهبری معظم انقلاب و تمجید از اخلاق، منطق و تواضع ایشان تصریح کرد: یقین دارم با حمایت‌ها و پشتیبانی‌های ایشان خواهیم توانست بسیاری از مشکلات را از سر راه برداریم. همانگونه که با حمایت‌های رهبری شهید و والا مقام توانستیم در دو سال گذشته به توفیقات زیادی دست یابیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/677825" target="_blank">📅 20:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX6UlAairqqvlnfUgaB8kBnjxkN_h8rcmD6puuA4tAb13LN3mnLAU-z2RrclBWI-Uykt2_04ZScwsekDTuWIN_bU-s2WEuim1ZOkMWbvWxNN4qEXHnttTCd89xABawo23hh9Nh5NyFl-AF2jOwOqP1tC1ivbnk2LaEsAkMwrDRHYi3GEY1tV6YSfbs3iCDOn5IndsvaRTCOaHzO5f8prwVe7y9WsQy4uFsL3m9QL7siQF18DumNdpZ8KQMycKsdYA8nFTPNRIFDdnYGsHb5LXoFzKw1Lja9wtHNJLo_z6C3I-aGOUbXCN6n0N7DBx8GwDzZHJtIq9SClpH7PFhbkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهتزاز پرچم ایران همراه با پرچم های عزای حسینی در بین‌الحرمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/677824" target="_blank">📅 20:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677823">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
بقائی: اظهارات مقام‌های آمریکایی بارها بی‌اساس بودن خود را ثابت کرده‌اند
🔹
بقائی با اشاره به انتشار ادعاهای متعدد از سوی مقام‌های آمریکایی، آن‌ها را بخشی از جنگ روانی علیه جمهوری اسلامی ایران دانست.
🔹
وی تأکید کرد تهدیدهای آمریکا علیه ایران در ماه‌های گذشته…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/677823" target="_blank">📅 20:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677822">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ اسرائیل به نقل از منابع آگاه: اسرائیل تلاش کرده از فرماندهی مرکزی ارتش آمریکا (سنتکام) اطلاعاتی درباره حمله احتمالی آمریکا به دست آورد، اما پاسخی دریافت نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/677822" target="_blank">📅 20:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677821">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۰۵/۰۵/۰۵ چند ازدواج ثبت شد؟
اعظم قویدل، سخنگوی سازمان ثبت اسناد و املاک کشور در
#گفتگو
با خبرفوری:
🔹
بر اساس آمار در روز پنجم مردادماه ۱۴۰۵، تعداد ۲ هزار و ۸۷۱ ازدواج ثبت شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/677821" target="_blank">📅 20:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677820">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c11034b26.mp4?token=jYGwoTqbblYyWhNrKjffDQ6MsUg-JDre0iZ9je8xr3ZaVZK1VkrmfIELbLZiTzs4O5iJ0YvgGoM5Xw4GFjEEvbHuBJ8dOrSXXC7unuCzVb0jGZOpnRSDcMXUwO6SLc90cbdvaPerpb69q5-gqK_SVyYeyXc0eKtjm0YXILr24y_F_UXvorQzVIWf2BV-eXmzmuRFoK3D3b3Kl0SNz_dWbG3zUonwNniJhL-OZojqjO-Phxu8LTVpdwR38VLmGYf_L9oVjte-8fbIL9iGRH4LGJnZJqj-mgkUerMLx6-NcwmZ3-t6o0TURDQpRpeaum5j2lAARzKmlZ_wpKFQcYefEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c11034b26.mp4?token=jYGwoTqbblYyWhNrKjffDQ6MsUg-JDre0iZ9je8xr3ZaVZK1VkrmfIELbLZiTzs4O5iJ0YvgGoM5Xw4GFjEEvbHuBJ8dOrSXXC7unuCzVb0jGZOpnRSDcMXUwO6SLc90cbdvaPerpb69q5-gqK_SVyYeyXc0eKtjm0YXILr24y_F_UXvorQzVIWf2BV-eXmzmuRFoK3D3b3Kl0SNz_dWbG3zUonwNniJhL-OZojqjO-Phxu8LTVpdwR38VLmGYf_L9oVjte-8fbIL9iGRH4LGJnZJqj-mgkUerMLx6-NcwmZ3-t6o0TURDQpRpeaum5j2lAARzKmlZ_wpKFQcYefEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوسه امام جمعه طبس بر چادر داور مسابقات والیبال کارگری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/677820" target="_blank">📅 20:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677819">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
روایت مردی که پس از بی‌حرمتی به پدر، عذاب برزخ را تجربه کرد
🔹
00:08:45 لگد زدن به سینه پدر، چند روز قبل از حادثه
🔹
00:17:20 اولین بازخواست بلافاصله بعد از جدایی روح
🔹
00:26:40 ناامید شدن از الطاف الهی در رؤیت لحظه ظلم به پدر
🔹
00:37:00 حضور حضرت ابالفضل با هیبتی وصف نشدنی
🔹
00:42:50 بازگشت دوباره پزشک به اتاق عمل و نجات پسر بخاطر حرف پدرش
🔹
00:53:20 رعایت حق‌الناس در شرایط مادی و کلامی
🔹
00:56:40 لطف خداوند در هنگام طلب حلالیت از مردم
🔹
01:10:00 باور به معاد مهم‌ترین عامل در عملکرد دنیایی انسان
🔹
قسمت نوزدهم (امشب پدر را میزنند)، فصل پنجم
🔹
#تجربه‌گر
: بهنام راعی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/677819" target="_blank">📅 20:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677818">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مسیر مورد توافق در تنگه هرمز، نه مسیر شمالی و نه مسیر جنوبی فعلی، بلکه مسیری جدید خواهد بود که دو طرف درباره آن تفاهم کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/677818" target="_blank">📅 20:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان منطقه آزاد کیش</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWZxq_0RM-B4Iug5yHxkXxrQ9Vxx6NjJbZMAC96RWAC4M022STUglDkD5-IEwGYWqhoN22HBZRToimHPYCvkjQMAfRjitXmP3HvRg3KI9FJpq-N28nnTBBG6-F0PjeV1bzSRHPZcjMJaihFzh5N-uwwHtsvP-1Xr_wpOe41M5UWLM9O5UlcPEP8-83u62_muCmuJB9zx3iBZSUKbjlLkIDjmkhqvzHRAjVuWiC147VzQRet3XHNZHXozWLJyoCmfatnyITUXKvJ5mQT6IJ7wvcIWtwwWW8E3ZHCuC5iSdMyZXNnm1FySzklxkD3aJvrKmhH3LUkn0jSnHuhgIXIpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*اطلاعیه عمومی: فراخوان تخصیص اراضی مسکونی فاز ۷ شهرک صدف کیش*
سازمان منطقه آزاد کیش در راستای توسعه زیرساخت‌های پایدار، از متقاضیان واجد شرایط (حقیقی و حقوقی) جهت مشارکت در طرح‌های سرمایه‌گذاری در قطعات مسکونی فاز ۷ شهرک صدف دعوت به عمل می‌آورد.
🔹
نکات کلیدی برای متقاضیان:
🗓️
مهلت ارائه: تا پایان وقت اداری ۱۴۰۵/۰۵/۱۸
🌐
ثبت‌نام صرفاً از طریق سامانه سرمایه‌گذاری سازمان به نشانی:
Invest.kish.ir
متقاضیان گرامی ملزم هستند پیش از هرگونه اقدام، ضمن مطالعه دقیق ضوابط و شرایط مندرج در سامانه، نسبت به آماده‌سازی مستندات قانونی و مالی اقدام نمایند. مسئولیت صحت اطلاعات بارگذاری‌شده تماماً بر عهده متقاضی است.
https://t.me/+Z7XNY2cgHjVjMDZk</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/677817" target="_blank">📅 20:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677816">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYR-SBqfa23e96gIcIKhEOUEsWYh11MTbNWY3HNk2aNJ1kOR46bKmrpPsG4cnGCfa_45CF6UnRk0UInxy1132lXBgHip5bEt1mwzEH9bwq6i2_as3_nDvLzIkQFJLVhdFlpmvHsyJN9Aludevb-GZS_kYzq2pFagwaWJ-TZ-WJ_TKs8gKi7xIH5WGfJYNnpK81bC7ZWyOnfMJOhvGH8Z44cgNLKZ6F2SDjel_SW5UcTnIqUygo661NJKDa7I601O-Z7V7vKuwAuUJRQ6xCT1e5Idey5avtqM9IZZ4hTdM12PNi8Aima-qxh6dLc2ErqMHQgJrfxX_1H3vu6O9mEwnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه به مناسبت دومین سالگرد شهادت اسماعیل هنیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/677816" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677815">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مسیر مورد توافق در تنگه هرمز، نه مسیر شمالی و نه مسیر جنوبی فعلی، بلکه مسیری جدید خواهد بود که دو طرف درباره آن تفاهم کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/677815" target="_blank">📅 20:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677813">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مدیریت آینده تنگه هرمز با ایران و مشورت عمان انجام می‌شود
🔹
بر اساس بند پنجم یادداشت تفاهم پایان جنگ، مدیریت آینده تنگه هرمز باید توسط ایران و با مشورت عمان و گفت‌وگو با کشورهای منطقه انجام می‌شد.
🔹
در ۲۲ یا ۲۳ روز نخست اجرای تفاهم، مسیر…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/677813" target="_blank">📅 20:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677812">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: مدیریت آینده تنگه هرمز با ایران و مشورت عمان انجام می‌شود
🔹
بر اساس بند پنجم یادداشت تفاهم پایان جنگ، مدیریت آینده تنگه هرمز باید توسط ایران و با مشورت عمان و گفت‌وگو با کشورهای منطقه انجام می‌شد.
🔹
در ۲۲ یا ۲۳ روز نخست اجرای تفاهم، مسیر شمالی تنگه کاملاً امن بود و کشتی‌ها در آن تردد می‌کردند
🔹
پیش از پایان مهلت ۳۰روزه پیش‌بینی‌شده برای بازگشت ترافیک دریایی به شرایط پیش از جنگ، «مرتکب تجاوز علیه ایران» شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/677812" target="_blank">📅 20:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
عراقچی: مذاکرات بین ایران و عمان درباره تنگه هرمز در مسیر نهایی شدن قرار دارد و مراحل پایانی خود را طی می‌کند
🔹
عراقچی: بسته‌شدن تنگه هرمز به‌ دلیل کارشکنی‌های آمریکا و محاصرۀ دریایی ایران بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/677809" target="_blank">📅 20:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677807">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba98212d37.mp4?token=FtHgIPmbUyaOuivC1ZhVPeotTydq7StfysJ4kwrB4Io95FHh6U0eeKMrHUBLn4iuADlkDCXGYlG95h8tz1MiCcef1DNJDmDreiarzXYVvQ4Y9o-1_vleuYbFoGn8R12Uuf3HmothbZr80zF1yuGPps-k_EE4UKVbO_Fpkwseljhmgqd5ujT27p-yIxPKML4YkwocVjn5FpoEAZOZntNwNhdqx1VMiZkrnZQMzauw5LhzUvnx_i7MwHH4eWoRmNMaUZlCecCx369LcTwotXuGT807vBzdj-MJRL_7gzORKk8xn_c2STdymq6-0-ikPnEkqN9Nmhof7NmRi8XOifTnAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba98212d37.mp4?token=FtHgIPmbUyaOuivC1ZhVPeotTydq7StfysJ4kwrB4Io95FHh6U0eeKMrHUBLn4iuADlkDCXGYlG95h8tz1MiCcef1DNJDmDreiarzXYVvQ4Y9o-1_vleuYbFoGn8R12Uuf3HmothbZr80zF1yuGPps-k_EE4UKVbO_Fpkwseljhmgqd5ujT27p-yIxPKML4YkwocVjn5FpoEAZOZntNwNhdqx1VMiZkrnZQMzauw5LhzUvnx_i7MwHH4eWoRmNMaUZlCecCx369LcTwotXuGT807vBzdj-MJRL_7gzORKk8xn_c2STdymq6-0-ikPnEkqN9Nmhof7NmRi8XOifTnAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوهای جدید از حریق در شرق واشنگتن؛ صدها خانه نابود شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/677807" target="_blank">📅 20:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF5o47x7NVoaUj4PXQkzpJbARy16HsUvoMTw4Y3h4VJHjd71U6GFUJq3VQCMTze-F6nZvkvSiujWUmOvi9dCkSDJdJnDzKz3ei89UcE0nuENjarsr-zcXXmPw8SGIPO677i397GCVKdE7qBuFLczZQ_I-tUUBJpRwf0Tm9aY7bgVW0gB8YXI-nKwPg8MMsQcooSeDr1-9kvT18HwaFTohFN3DamI9FbVnsuVW3ZNxH8cOYhA69snKEAdxggy3Yt1X9qzXyITA_51oKji6p88npJtza5zKDdaUSf2maX25iTZn0Q_7SNVWcd2mfKVuNix45B2hl3JzA87o7Ps0gneqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/677806" target="_blank">📅 20:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677805">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: جمهوری اسلامی ایران براساس منافع و مصالح کشور عمل می‌کند و تحت‌تاثیر تهدید و ارعاب دیگران تصمیم خود را تغییر نمی‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/677805" target="_blank">📅 20:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677804">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: جمهوری اسلامی ایران براساس منافع و مصالح کشور عمل می‌کند و تحت‌تاثیر تهدید و ارعاب دیگران تصمیم خود را تغییر نمی‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/677804" target="_blank">📅 20:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677803">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRa5JOjSG-c2uiJq46rEJXUqpuOiSi9x8hcynNehwYcU5mRKz4xofqLgJrEAn8GCAn8UlKNVaE2VAY-WP4E9kpvhPmr53oz1XmORS3RjVMXaqSTRhv_ObJmad0iEYk6ToJtHdiCmsp5A9RCqPwx2KWq95pyBKV03Y1FuhOYozxYE5gBFnmzLmzwN-4vXWU3GoOya27g_SQFq9KKGcvqUrs1VLtUBAAXpjX7rOLVvEBnlMvbYlXN5bY5saHX8gh_bFo7HrIDXQzZIjliYB_Uq_9fBMWejrBSx2-Ik2bXspNt3cSm61-bPA8Hl_Nv9Xd6YmScjqCfGttZhFokd_ttCtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمپول لاغری زیکورپا؛ بیش از ۳۰٪ کاهش وزن علمی
زیکورپا با ماده مؤثره تیرزپاتاید (Tirzepatide)، با کاهش اشتها و کنترل ولع غذایی به کاهش وزن کمک می‌کند. اگر اضافه‌وزن دارید، زیکورپا با تشخیص پزشک می‌تواند به کاهش وزن
ماهانه ۸ تا ۱۰ کیلوگرم
کمک کند.
👨‍⚕️
تحت نظر پزشک
در
کلینیک آئورا
، پزشکان پس از بررسی شرایط شما، مسیر کاهش وزن با
زیکورپا (تولید داروسازی دکتر عبیدی)
را آغاز می‌کنند.
✅
برای دریافت مشاوره رایگان با پزشکان کلینیک، «
کلیک کنید
».
کلینیک آئورا</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/677803" target="_blank">📅 20:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677799">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72ef27a54.mp4?token=GG9onbeUJwjoy7bQV6lMtLtGW7lJMDnLk7-cQ5nCfCJ7waXJ6FRZop5VEHzahYWPyf-LN-B-lgYCPvLc9JnePs1O8Ck6QJM8CssOlMrGFiZBZVr_4_b4zwCD3x8npwmGzGGMdcf23yZiqn5VoNYXrd3Qa_MQPAiIsctqmvLWsBn67YejiDeYSgm-PXq8sWHsYL7aSpa1F8klVjB6aiO418bgXe06vGWZDndfcQTgnRd3hqPGsYg7vp-MUSktozYii2gHpFZ19NA7qMjU15xKiWOrUD9OcW8VHtqE5jq1KW6xHE4mRhs-Z9GCJwCOBokFRQuWI49Hs3DTKqCkFiB4HGKFTFVpYWIqeIMFqGiXEBa5huNaxSijHVvUzC7rg3Q7jK2nW6jLUavyVn7ZmPhczPVa1a9knlVaYAOU8nLyRGfM5K6gsyZx4keAr56riW3qLhGGsF4HTTue-NDT_Z6upepV1chLosM1MPftgqqmxqY2oaVpAjBhJkyKrJUn_GmluAu1TgfDU2aweRwpoJn-_Y4xxh0cP0f4EhQfVBvsB1FdVL09Y1RlGmR9rCYqSyKLAossqD6dvX4X8Nh_o01lt3qAILFy-eEqqkS78m5mPDIICLpZ1eEA7tvTip388ySpvkPv3C9NJFqBH3plcopsxkS15o5-PhG2-AhaExFWN3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72ef27a54.mp4?token=GG9onbeUJwjoy7bQV6lMtLtGW7lJMDnLk7-cQ5nCfCJ7waXJ6FRZop5VEHzahYWPyf-LN-B-lgYCPvLc9JnePs1O8Ck6QJM8CssOlMrGFiZBZVr_4_b4zwCD3x8npwmGzGGMdcf23yZiqn5VoNYXrd3Qa_MQPAiIsctqmvLWsBn67YejiDeYSgm-PXq8sWHsYL7aSpa1F8klVjB6aiO418bgXe06vGWZDndfcQTgnRd3hqPGsYg7vp-MUSktozYii2gHpFZ19NA7qMjU15xKiWOrUD9OcW8VHtqE5jq1KW6xHE4mRhs-Z9GCJwCOBokFRQuWI49Hs3DTKqCkFiB4HGKFTFVpYWIqeIMFqGiXEBa5huNaxSijHVvUzC7rg3Q7jK2nW6jLUavyVn7ZmPhczPVa1a9knlVaYAOU8nLyRGfM5K6gsyZx4keAr56riW3qLhGGsF4HTTue-NDT_Z6upepV1chLosM1MPftgqqmxqY2oaVpAjBhJkyKrJUn_GmluAu1TgfDU2aweRwpoJn-_Y4xxh0cP0f4EhQfVBvsB1FdVL09Y1RlGmR9rCYqSyKLAossqD6dvX4X8Nh_o01lt3qAILFy-eEqqkS78m5mPDIICLpZ1eEA7tvTip388ySpvkPv3C9NJFqBH3plcopsxkS15o5-PhG2-AhaExFWN3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه این روزا درگیر پنیک شدی و حالت خوب نیست، حتما این کلیپ از دکتر ابوالفضل احیایی، متخصص اعصاب و روان رو ببین..
.
https://t.me/dr_ehyai
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/677799" target="_blank">📅 19:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677790">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qWs_kK53Gr74Rn9sOyjrcUgx4-M1mzZ-cRK-NKJ4X_JpLtHTtm7EcF2S-Mz4Wrk1sYQoqvpj60wrh1sxWi0C6_kpi1Zh0LQVaYLjr7U6ufGvW45nLbEHp88r7O9alZeZPOKWUrqSZ_vNdvY16Qm-t69HjzvX_u7M0ywppKYZ68UAnVBWyKmr881TkPzHENifopBvjE5_kr1KGLk592bGmnYWWHOn6r8ve7pYGsKYLYN3xyx2rh_YY-h6w2iU8SzLKBN9Hwk0BfKlhzCS1BIOuzVnTNIhDt_E-qlKm_VDLjR4Xr3UCjoH6W1kEi1lGA6yE3MYM2-6fyhBbhDR297Z3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mubKiYtE9O6Mz89DViZKrylRv4lzYNNIPdQsF_ycMpYCW0xbPri7aN3qSrCzp7R0p6Kn5lApGuPzKXRqeiLMCWZUdUo524ynmthR32-3Yb8R0TicDzmhndGEUeBVk4mfaVAJuIW95zw8yvN_x919UgwV8tF3Sc1uwi7kCoZmNJaGsloLLajCLviMHb7zLvH3Vq4jFDv2LSto7bayLZLYnElUKfxcVxtVn-hZDbbdSu4aNE36xX4B9L_ILnVnnn9mXUfbZyxvg95u8CkCtYgHAgeSO-X4_g6yWJzofTFzoSgfzJwW2OcXldVGjOcxAzmA3v4jSMI5-pjoHS2zpKrHAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XswOtduc8X-t2ewaCTNniVR_vL1St9SqJ3zweH2UVahwoBhiD6j3kBCxhQHNhRnvRHKgmhg10877Um-dsTSKgXAKtJtwpVafKGfOa__8UFc0HXRJ5veCmz_h_X6aAbwmTZuqgprBdqTwBMFhIVNH3odZ_wuDX-qk8CvMttGZX6rawNOb5QshsMVIvjCpS1r8z_ouReCnON0zyiv0eS_x6uiH88D3JSj0sz-h9Tz5ebGMZ8qgsIvYFLMvaYv_0JLAL_7Febww9Uz8q5xoP6FGdbbMTQ1vlQ5h_0ZJzM5JNDbrXQyNClOxeCh888RKilPcv2QZY1mwMHOe5ExLoVJZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_QH3EUZELPLtZpv6qQJJNTzgH2cvYX8nyjYMnMcLtjtj8WBGndPzI8LkCsMa7PABgeB5fQDLB4n0N7VvFoGCEijhC4CKv2VsjDMIv-_21M7i_4R22IwnTysAkwUHJ9JblD5OGh5m7QNoP2CNd_nGkm358n1eFEpr27VhKIZy-aBbSRbgPjCH5tjSHBO9Vn4UVzH5dz62x7GFyXbGa9qNffukuxCG-K8P-1TxYuZl5kn1pSUN_c_vB3_Mr_azv53Sh8w9-IHmlu1pWzEzsOkckS4ug3CEbAAixGLIvcrbjCe5577-FC55pJKVE60xxCeB-IVIT57NLKSqKhS6T1mXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbxyAN12lQ3k2ihuK9NMxpXXHcJF-92xVGsAoF4bhZyN_pr_8mXP2QzCCNtRakwtD6VL8LWWwgo8THUQA093o_DhVoRtKpr4T5P_FF3qvCxZbZCtskC8ZKIQMYoUDEYmRX_A940QMGJB1mLnakAgm-dx7OFnmRgw5VDO9rnpJijUifsN4oH-KN5XWPiGDWNE8E-7M2rdo5wgy3D1k_q9uB3sm45sOcifN9adsG3i9wj2ATCGSy6rPLywTfK0ACAJtwNRmOzMhB35LXM5ilruneAw7ubCDYWD_ljFgGmsI9iBIMw65T6Ch0KUh8UCxMuUxlkwPq5nnvgvca6_EkEOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quH8mbMa_7MBIfYv6Xfvn8sYRd7GBVr4zbsXMVafEzrMpa4B7N-1YLLcbLJequys348Mr-wVeE2JTpOehIjYA8dxe5PzxjI1xNZUD-J18EP36F17FWPthM7Fe0Ldbj_5L9IbC-WdO0ICFw_uam_E_s6NcOuVtfty4xJwGdKBi1sr4Md_GU-GP_1ZLl9LXQzH1JXolJoQ79c_IAeWNhVHc79m8kgpOmcuuzW7tXttaAQtYqetid7W4eHColP46lkP9yhm4c1Z2hwKHBlUrDzZjOiDsUcMa-OKNKs_BQdqiEpXMiiX1aibngcXpr8KXcUX4SWwcvtD60w4KMyCzZN4Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/up2BRHMSTOmjNCa46c4PZTB0lL08V2kXQo-yHsFdX5vDWDZtCb52cw1HFDyfSLg_F8QVpKddXyYl-mX6FyPFoFwu5I74O-1IuyxRDRIicBsIBXWeHvOF2S2-wKNJEu5vuTHM7ecIUP-X14ACzcI6-xKLj_5_r7Hp30l_lsHNY3zl43ZZn_o1439iLD66Xb8T3yrwIYSO-gAy0KiPtC9K5QWFCd_cAGRSENJUl_AAxKtkDQUbCqrOXk2E2-xj2ywQPa8MADpym8losSTDqWQDnRG34MQczgVIE9BPWz2ixPfbwKYJZLPf21HGV4IfA2TkaR3Vu5PMHqz1Bc9lDexERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_J78O1XfyUlXKMd1H8Nkeat-g0ObfliWOlPT84OcwtkO5nEqSKM2_sonVzK719kT1fjTTXGN2p_G5YRYZ-eYYd0sMisXTKHDtsgDaJnlypAp6jrii9n5ESw-0c5s-7J3Cuf5Q06X_NNCMoRKXg-6-e1FhMNmHJOZk393uqN2ajotX0IC-h5nq4RrI2bRztdi4agas07PoGoijYweHEmUP7OGpGgNAjfpO7MDrLw5rgp7WXfk_P1B52HHQWMLSQNL3MxfrHSELxcvA-2glSjQT6D52sFQUDwbeczM8QuiUPB9eEvxvVT6ynVxrSvYuUAeriGyKcK1xE8DT5JT5aGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fw70iV0qt5g5OeU3dZBP3QdSaU3OKV-tJzBcWH1xcVq0BPDS-NBcsB59dkr0i4ngHCJyeevsCdfcrOZ19GX0e6YFPB5LAeryGFRQgDKsoLyoIZDLItCLa0jMYffWIbuX0twJ4dCk8M8dxB8ei8qPjb1Tu-ZllfSceiUzZ_sJz4Jd9rawH97-x7IGKnDdY1ZrfDYV0IgvZ7cIXyM7Bf4on4-qwnHcbLOGpwiymY27PRPsly-eyv8gNFdcp_m10y2S06cXjHcRdxyRzGNeG3jeCFmqs43HCZnrbt-9j4zdJxDxhH-ffrpLEEsVRKlweAH3bujeVkUNGFTGZ1DkKbEPJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این ترکیب‌های ساده آب را از دست ندهید؛ هر کدوم یک خاصیت شگفت‌انگیز
🤩
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/677790" target="_blank">📅 19:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677789">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAaoGPvvOCwqoN3Es1cZSMd8bOIFDuNEzmci3rV28OMPk8KzJAJoc_9Zh2EWZ5_A4IvAqP8UATPsK4XuIevjnJo0PrC8UwByw9FIFRpox_MnBXKE8I8FrEsXeCXtTcFJ1UHKtCNY4_jgTcoM6DXq5z0qBbdyS61P4twWqrXvpYAfGeUwIW3B5umUDs7DwOZvN-WYn7IDvXZkbCRR7YDCa7uWgxOx3UygL3u5ZkKqglGgVKXpsgdVpd4MLwtqIX_EpOKrLjcpskDQ-E7wzvHNgyqQQPrHNaLUNZ5BWRfbphYsq1kms8-qC1dm1leCj40FsqISioibAQyQpZskW__4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
قبل از شروع سفر اربعین، یادمان باشد که ما فقط مهمان نیستیم؛ باید در کنار برادران عراقیمان، مراقب این مسیر هم باشیم
▫️
یکی از همین کارهای ساده، برداشتن آب به اندازه نیاز است تا چیزی هدر نرود و سهم دیگران هم حفظ شود.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/677789" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677788">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
دفتر ناتو در بغداد افتتاح می‌شود
🔹
منابع عراقی از موافقت مشاور امنیت ملی این کشور با افتتاح دفتر ناتو در بغداد خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/677788" target="_blank">📅 19:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677787">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxGfYKWRTBCl-LOoG-Lsqfzw8GCUj-spUb-FzlqRdKGCS_efKJfQ5tzJPCM_0zaG8RC_00LJk-b2_0Pdgxl_drIwsHBvHOu0gl_DjBV5qU6CNLD77l9TF-aQpIR_AEys5rtkZvoUTbExa0iYoN_Lnhz7LAyChGYRJQfjlPQJhzs5UEzHC58XnZdWoAFiS7r3mPRq7t9jZmKyrPtmgcrFH-XwDq2SfwVYlE5x07Cq-owgWxIcrUwI3Rq8fI3UwpkcJfj0x-9vnQz2WFIIYqI_87DUO6CQbnszi8gUZmbnmgG7Lp4-8j_uQ7KJPgRCORxdocMT-aS2AyAUXRxn46JAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواسته
امارات از ترامپ: به ایران سخت بگیر
ادعای وال استریت‌ژورنال:
🔹
رئیس جمهور ترامپ، حمله برنامه‌ریزی شده به ایران را لغو کرد، پس از آنکه نمایندگان مذاکره‌کننده ایرانی (عراقچی) به پیشنهاد جدیدی از سوی قطر مبنی بر باز شدن تنگه هرمز پاسخ مثبت دادند. مشخص نیست که آیا توافق نهایی بر سر این پیشنهاد حاصل خواهد شد یا خیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/677787" target="_blank">📅 19:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677786">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پهپاد اوکراینی به چند متری راکتور نیروگاه هسته‌ای زاپروژیا اصابت کرد
رئیس «روس‌اتم» روسیه:
🔹
یک فروند پهپاد جنگی اوکراینی به مکانی در چند متری ساختمان رآکتور واحد شماره ۳ نیروگاه هسته‌ای زاپروژیا برخورد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/677786" target="_blank">📅 19:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677785">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjcaECL7uBOxMC_HwLCERdIdg-swZL1NRodGHgBcf2Fq55T3Xc5ZqwiOsD3WVxLQTXYWG9sNJLMcQIsCXfpvLOPQxceu7SnOj8pf45AqhI5100fxm2nMenK4SN-3txXXjt2KZWVg8mD7a-EFuAEO-AXbsY7LJEpJZ30H1JncUV3h05kTxkmCAgcgCsVRjdT0b8-JYoh9Q1YUP6Y5j4HCIMtZIXb6bt1eChOTBLAQ6txoFTMPHXIakuNhGGom3OpVZse0bvHRRIculKOT1dnFDuAccxIulOk0Zj02AzEChbA3RxzfBLUcFc2OJY2KnXO5pep3VfW-lWzhvvtjlhEG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال درباره یک دیپلمات ایرانی: مقامات ایرانی از ضعف سیاسی ترامپ آگاه هستند و در صورت لزوم به دنبال سوء استفاده از او هستند
🔹
اگر تلاش‌های دیپلماتیک با شکست مواجه شود، سپاه پاسداران ایران در نظر دارد حتی اگر ایالات متحده حمله ای را انجام ندهد، حملات پیشگیرانه را انجام دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/677785" target="_blank">📅 19:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677784">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e0f1758b.mp4?token=Ckpy5cf_iI7TFId4vxGHt_RaFhEonA3l2P2Fb0kIan6A6j5JMpVHP6sbQ7JUc4Y-qlGxtEIemOYO9VhTfdQhJR4gl46EojV_At3J0gT_Mw2TW3_xdGHN4RDg6vqIknv7DhoWoJSIJhw-X971FjLNsPvfIlMSz55nKxOQVL5Dnps4qcKik9CuGOU_HF276A-Ly7G4o-zBhKbJnR6hxJy4UHaA7AYDXsflnZe-p_TgQAHkmmeZWd6EjiQxucx8R7mNeBr3aGmAtI_U-NL1SnqDLm2NPL6pUKcV1RKA7fqWaOvmElkNG9QAcDW77fxzcp2HtWjH1xXxtM4W-NQG_tR3-yJkKtrRJRuxK0pQX9pc1bGQuqxiwdlutf90s6rfkT1_cc-h1s3hXKoFrp1FB1U8uEoCFUDXfHMzOGBbL2h7jbg3fNME88Anz3IEERMzbaPV56tBWMC0G11LqJmJyJf8qI3Nb1O-_9-Y1zb9gk-4hSrN67xEHPbNg190F5WubJl_-BI_iTpX1XjaiIM-u0acHebxSzdLVM2zR6Fq3sL-DKK_UClILngjONWa6AezPKFYJ3lhF7d6rcTAp-A_kClsOxphjNzHKFlQzspy_oqG-3KmJAur6aW6O0x0LtPsQjXQBtDJsIb1D9ZjF-sAgPEi86jO_BpF_pTPIaIehi5Q6Is" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e0f1758b.mp4?token=Ckpy5cf_iI7TFId4vxGHt_RaFhEonA3l2P2Fb0kIan6A6j5JMpVHP6sbQ7JUc4Y-qlGxtEIemOYO9VhTfdQhJR4gl46EojV_At3J0gT_Mw2TW3_xdGHN4RDg6vqIknv7DhoWoJSIJhw-X971FjLNsPvfIlMSz55nKxOQVL5Dnps4qcKik9CuGOU_HF276A-Ly7G4o-zBhKbJnR6hxJy4UHaA7AYDXsflnZe-p_TgQAHkmmeZWd6EjiQxucx8R7mNeBr3aGmAtI_U-NL1SnqDLm2NPL6pUKcV1RKA7fqWaOvmElkNG9QAcDW77fxzcp2HtWjH1xXxtM4W-NQG_tR3-yJkKtrRJRuxK0pQX9pc1bGQuqxiwdlutf90s6rfkT1_cc-h1s3hXKoFrp1FB1U8uEoCFUDXfHMzOGBbL2h7jbg3fNME88Anz3IEERMzbaPV56tBWMC0G11LqJmJyJf8qI3Nb1O-_9-Y1zb9gk-4hSrN67xEHPbNg190F5WubJl_-BI_iTpX1XjaiIM-u0acHebxSzdLVM2zR6Fq3sL-DKK_UClILngjONWa6AezPKFYJ3lhF7d6rcTAp-A_kClsOxphjNzHKFlQzspy_oqG-3KmJAur6aW6O0x0LtPsQjXQBtDJsIb1D9ZjF-sAgPEi86jO_BpF_pTPIaIehi5Q6Is" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: برخی نمایندگان بعد از دوره نمایندگی نیاز به کمک مالی داشتند و برای آن‌ها زکات جمع می‌کردم/ ۱۰ درصد از نمایندگان پس از دوران مجلس، بار و بنه خود را می‌بندند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
یک زمانی در مجلس می‌گفتند اساتید دانشگاه دو تابعیتی نیایند که این ظلم عظیمی است. هفت دوره مجلس بودم و حدود ۱۲۰۰ نماینده را دیده‌ام.
🔹
۱۵ تا ۲۰ درصد از این ۱۲۰۰ نماینده از نظر معیشت خانوادگی وضعشان بدتر از زمانی شد که نماینده بودند. نماینده مجلس روز هفتم خرداد که رای نیاورد، همه امکانات برایش قطع می‌شود. ۶۰ تا ۷۰ درصد نمایندگان همان‌گونه که آمده بودند، همان‌گونه هم بیرون رفتند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/677784" target="_blank">📅 19:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677783">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای وال‌استریت ژورنال: میانجی‌ها برای بازگشایی تنگه هرمز پیشرفت کرده‌اند
وال‌استریت ژورنال:
🔹
میانجی‌ها درباره طرحی برای بازگشایی تنگه هرمز به پیشرفت‌هایی دست یافته‌اند و کشورهای عربی منطقه نیز ترامپ را به گفت‌وگو با ایران ترغیب کرده‌اند؛ با این حال، جزئیات طرح و مسئله دریافت عوارض از کشتی‌ها همچنان نامشخص است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/677783" target="_blank">📅 19:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677782">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی سنتکام: از زمان از سرگیری محاصره بنادر ایران، ما ۳۵ کشتی را منحرف و دو کشتی را از کار انداخته‌ایم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/677782" target="_blank">📅 19:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677781">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-pSS-aCdegKtdYa_BuyAr8UchWxMGfo0jiULz_WE_bttzbi9dMCpi_vykYg7b7-5Tw2rcxu3m3Ub7ccC6RDxxgBNr4Y9CiuSMjJGByHyX1RTwP2j1fJcKfN5nmxEcp9xMn7fyvQDTlnf1SnQmeSeI2xndSILwNQe1mVRFZu_0BQMZyJfWRnXb0ZxwQj-ZFH19X1qzM1e325oUk0UkEy4ihZVO3H1EBhXHX80Jy_ah3czoAftiU4pbxJeXrIXMDMs2_EoaTPtgSF91Gf19l8DjXBxew_fAZPAYV9Xx8OSuoqDlSqeOrkTYhcblr78vjknwHQjYFk_WnqqQ1ZqyK_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران با کمترین تولد ۷۰ سال اخیر؛ ۸۹۲ هزار تولد در سال ۱۴۰۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/677781" target="_blank">📅 19:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سخنگوی دولت: قیمت بنزین سهمیه‌ای تغییر نمی‌کند
🔹
سهمیه ۶۰ لیتری بنزین ۱۵۰۰ تومانی برقرار است و سهمیه بنزین ۳۰۰۰ تومانی نیز ۵۰ لیتر تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/677780" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677776">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5020d09a.mp4?token=bct_iioPp41etqO4tmX76BWbmZ-5pSqfqDpvczre8Myhh2Ioyxmeamo5l0NQk6ZjTu-pw5BfC9PnwlArRZFNNK8t01-u6ywaLtMPMmZTQyNqydS8c_PBgKegDYsu3f2pgdf2PUBXvQphRCecad7ciKksy-0QsQkJGeWqU5tQ4djCulFFONC52gpqvgszry1dMOCm6ZCQJwpQrXugY8cOdGLq8rLpHHN3hcNb5M8bvSZyabIYvgPP1vbSOdZb4ggg-tVmpi4Mb0H8Irdbatd0Wba1aMJytevi9qDGRaGiX7ktfissFLg2WKYhFkBlOpReemTNM81AhaEY1Y61pQn5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5020d09a.mp4?token=bct_iioPp41etqO4tmX76BWbmZ-5pSqfqDpvczre8Myhh2Ioyxmeamo5l0NQk6ZjTu-pw5BfC9PnwlArRZFNNK8t01-u6ywaLtMPMmZTQyNqydS8c_PBgKegDYsu3f2pgdf2PUBXvQphRCecad7ciKksy-0QsQkJGeWqU5tQ4djCulFFONC52gpqvgszry1dMOCm6ZCQJwpQrXugY8cOdGLq8rLpHHN3hcNb5M8bvSZyabIYvgPP1vbSOdZb4ggg-tVmpi4Mb0H8Irdbatd0Wba1aMJytevi9qDGRaGiX7ktfissFLg2WKYhFkBlOpReemTNM81AhaEY1Y61pQn5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت سرکرده کارتل مکزیکی و مهار شورش اعضای آن
🔹
در پی دستگیری «پانچو» با جایزه ۵ میلیون دلاری، اعضای کارتل او دست به شورش خیابانی زدند که نهایتاً توسط نیروهای امنیتی مهار شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/677776" target="_blank">📅 18:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677775">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZi7-0r28v8mPO_JErL01R80STkwTRC4_Srg0-RUkVicBRUuWWrpxG3awr2CB69EbispI-QB-KKPZS1D7LRgqu-fu-iujT9YlKI1CZuCfTUAU21oFEDM3FIO5pY5X5elF2AF9DPznGwoyhAAU0qiL0wNsP079MqL9tey_Ka2U-rkgDNV_3OhF1fEpaVHAZ7dvIlHsrxygPX6Q6EDhRvpe80q4Q5N2j7EDL8UBWkbz_annPPv_DuQawVhcrusQK8Cb2Tvjjx2S8GPblYqQEQ0wQNPWy0Zeg7pzbILDNmWfBulVGCZnMI4WXFuzcw2VVyjh0f1Wi2ARqaXzXcFjdYg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تکذیب خبر نادرست درباره حساب‌های مشتریان بانک صادرات ایران/ تمامی خدمات حضوری و غیرحضوری پایدار است
🔹
بانک صادرات ایران خبر نادرست منتشرشده در برخی رسانه‌ها درباره حساب‌های مشتریان را تکذیب کرد و نسبت به تداوم خدمت‌رسانی در همه بسترهای حضوری و غیرحضوری اطمینان خاطر داد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/677775" target="_blank">📅 18:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677774">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46424e6872.mp4?token=P1chmJip9RovsV4dPkBY6G69N5EBPshHrXss9UjxFLG2AZ3Gwp3Dq6J_wskKskNsVr2-uR5f53v7ArQnluV04ZitKm9hC_i9jtzw1KZ5frVbB0wKLrFULHNgfI4bI2-Yre9L_efJ6Ts5KeZQf2lqU-d61qexJshPKa4R6riNWuf9yqAFe6Uk-7j_wcngI_72EPGfdbd--Ecy8Ie7aWPBKO5MF1leYxacYOad0lxmStZymnn5XwvBk6zHtyRw7K35XcWDd-UqVvSRluJpofA8PbOrwYq-RL9ym_Mm6I74XXGamoZWaCuuj3z7ozaBVyRBy-4tknuOen_3r8PxWcQrOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46424e6872.mp4?token=P1chmJip9RovsV4dPkBY6G69N5EBPshHrXss9UjxFLG2AZ3Gwp3Dq6J_wskKskNsVr2-uR5f53v7ArQnluV04ZitKm9hC_i9jtzw1KZ5frVbB0wKLrFULHNgfI4bI2-Yre9L_efJ6Ts5KeZQf2lqU-d61qexJshPKa4R6riNWuf9yqAFe6Uk-7j_wcngI_72EPGfdbd--Ecy8Ie7aWPBKO5MF1leYxacYOad0lxmStZymnn5XwvBk6zHtyRw7K35XcWDd-UqVvSRluJpofA8PbOrwYq-RL9ym_Mm6I74XXGamoZWaCuuj3z7ozaBVyRBy-4tknuOen_3r8PxWcQrOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسپانیا خواستار نشست فوری اتحادیه اروپا شد
🔹
پدرو سانچز پس از ورود ده‌ها هزار مهاجر از مراکش به منطقه خودمختار سئوتا، از برخی کشورهای عضو اتحادیه اروپا به دلیل درخواست برای تعلیق اسپانیا از حوزه شنگن به‌شدت انتقاد کرد و خواستار برگزاری فوری نشست وزیران کشور…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/677774" target="_blank">📅 18:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677773">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a90068b7.mp4?token=VN1PJHMnBi_ArGzdnxofgK3o_Y6m32MROw9zyyO5hbM4adgxCX0BwJjdX86ZHPD-Vk4eeDf77xprZjxx98OX9z6xlwYEp-w0eIp7AOL-TUMfMeb_Ywg2LBDZIeo0qkbydU9rDyRDLaElTJ0y-2_IE8oy2KMCNiClE-JSKPhusrkD7gZBW7PoNaGTBs9peV1LvNyX9JXUk-YCEX_jIS7sSmdaFowB6SpjIO9x3iSE9QvMgVu2rlqMWntSeX62pprXClGGqUw6FrM0611wuKhug7d-M9TWCZsVcaZjtGQvV6Q2hkm1fWzkBj3wbDO_p9Fo2BxnoE-bMwMDAsvB0wBQfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a90068b7.mp4?token=VN1PJHMnBi_ArGzdnxofgK3o_Y6m32MROw9zyyO5hbM4adgxCX0BwJjdX86ZHPD-Vk4eeDf77xprZjxx98OX9z6xlwYEp-w0eIp7AOL-TUMfMeb_Ywg2LBDZIeo0qkbydU9rDyRDLaElTJ0y-2_IE8oy2KMCNiClE-JSKPhusrkD7gZBW7PoNaGTBs9peV1LvNyX9JXUk-YCEX_jIS7sSmdaFowB6SpjIO9x3iSE9QvMgVu2rlqMWntSeX62pprXClGGqUw6FrM0611wuKhug7d-M9TWCZsVcaZjtGQvV6Q2hkm1fWzkBj3wbDO_p9Fo2BxnoE-bMwMDAsvB0wBQfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هولناک از پاکستان
🔹
حمله انتحاری در شمال این کشور دست‌کم ۷ کشته برجا گذاشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/677773" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677771">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_YipcA89-9ZCFlVn2JfdxL2RbJH-p5tpsgGggYu4kHEUk0l7pXRCYCMbZaIwHRxtE0PjCLTCbacrjMMOxPar-7TrO4EbAcqjBMKhzLpiStoKnDSoqj98RuHkRMQKQURSby5sycMYcIPJNeeB25Ua_KfLxWT2Lcot5j7gYsU_JMOs5GJVWaSkVPDieWEs2pzS7Y6Wv0bS4OO45MMQ1z80MM2D126hfuu-V_9jxWWXAd4A7XseQCPwQUhlHWVdeNVXzgQ0y5AtGAyijZdSF_qm4eUsk4NLar04myqws0S2qAEUaQIDM2-FJrBvM03aLPmvy5D0Ne_9Fxl8dmfyvMjqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مناسب ترین نوشیدنی برای لاغری کدوم نوشیدنیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/677771" target="_blank">📅 18:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677770">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gijEyoFLDGHeX-_u6lyliNK0KxtKOL9ktbGuF9_vQCyzj6HogD38GyvmcRdRA2lZGzFVfxgS7JenMI_OXnsaxm3p6rMDVENdKttO5WSR93gBJZcxfgCo0hYGp1DlsZlFA2JXv-gh5g2yYLtiahUdjeFeL5I3PYqYA3oMUWCvuH1n8Rz3Qyc5HTgWV4vQlG0w_q1ueDZx67yjk8QHJbdCIClJeU3HL_1AtySAC51iOFO9T1hOzeOxn0l4huGzMReRYQeqUJtDKxYw8OS3C62fx3ANoXR3ZKoNQ0QHSGsPs_d-B4iFdtOmXB18Gejre7--nDn35YPnqylZkK1F8neDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚪
🦟
پرده توری آهن‌ربایی با قیمت اقتصادی
❗️
پرداخت درب منزل
❗️
✅
جلوگیری از ورود حشرات مزاحم
✅
عبور جریان هوا و خنک‌تر شدن منزل
✅
نصب آسان، بدون نیاز به جدا کردن در
✅
مناسب درب منزل، باغ، تالار و…
🔄
گارانتی تعویض و برگشت
🚀
عجله کن! لینک خرید اینجاست
👇
http://khabarfouritel.affdn.com/lead/45272
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
http://khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/677770" target="_blank">📅 18:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677768">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amg-1Arr6RxvM-a6OAFwqho1CcA235JXvxK_8v7MVDTvlJHKkIlOXpW1MDCz9gasXP9nleWaZL1h99d7XV-nPNb_EJB2Hzky9Onl4hmI_md65NtwpSbj1b9LHjO63ptfJLVdhdvYaRWIpxszxgF6OkSiq8pZqTCWXsPT9R1wDOD02k1z7ojvQLCUaHGe2henaLB2rA40fOYJ9-HjnGfErMJ4qSSgVe148BxLo_qe1_7dO8Wf7FnSosueVhHJ8lNV0TJzMDtA9keUpjFRH7xYrJGd_ZB7D-EoI3qagUsAAHOiu6iZvReSBaXE76Kw4clI7OPFoD5pTGnzmEKkJxODpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
موکب داران با دل خدمت میکنند. احترام به آنان احترام به راه امام حسین (ع) است.
#میزبان_باشیم
@Heyate_ghararr</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/677768" target="_blank">📅 18:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677767">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvtfB-tLbYdisusOGAV-eZGallVov507c7R8RaMuQXk3Tl6lvqSq34MwLhjOmb5d5_oaL8o_5bgyUi2sEImmniGnE4mlKDFiHVH3d-WyIe7XdHRJo-ZsPnifNA1oLgTMkxIzvol4-m8Vtq5uJEhBHqIn95YUEUFAhHIS7InMcxS2VdhQn4Xehe6K4xzOicJnJd91WOxOCu1azhUpyzYMQhY2DkFDSc4Cb6HSxZGBf-pm_dGG5ODQy-Nhu7w13XSil8V11wJ3BYPTYjJjOqou7Rw7Ij12OG4JROaR_nu7_oD-RCkHC560RGBnBwGw-UyyUOnAhwYrPzndux1SNGjBuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مردی که قرن‌ها جلوتر از زمان خودش فکر می‌کرد؛ ابوریحان بیرونی
🔹
ابوریحان بیرونی فقط یک دانشمند نبود؛ او کاوشگری بود که با مشاهده، اندازه‌گیری و استدلال، مرزهای علم را جابه‌جا کرد. از نجوم و ریاضیات تا جغرافیا، تاریخ و داروشناسی، ردپای اندیشه‌اش هنوز در دنیای…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/677767" target="_blank">📅 18:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677766">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a2f85ffab.mp4?token=Ks-iTw1dfuhTyIXmTUgUdx4POsSCzXDFNwyuDPXmKrSHfGS8x73BAYH21-Rfg-rcr43d4qLPANuU04CvMOVScfFsvodezcpHifFJSWaFqobj9YtuWt1Ng3-SSyMV5ZierwYBRohTJ7_-JAg0CnroSVf11t3rj5Plf6OZ3GkyknycBw-czo4eOv5UYEcU6sg-K_uQ4QMtg9XLVI_gETilC0XUA_1RBS1khlnrmtYmGNVuGU1yRNrAeypvywkXYdATiy1gz7BcA2NRJ9G9IAqMa72iU3xmY5SRd6roSCbdtrazJUR5CfMrz7QttK_CHnQExSLgr9GcgSv_iPLlZLI1M0hnGEXT6WRT5edyW2Y2XC9UdI8rVB55IHVy3ATXl_2AYk9nMMElofd66Pfmrz_E24DRtG6HZe8JtzpUSno5thU00nFjFF4prKzgjsIUaWMaAdfUEwkoPsI6NiEhQvdixnTxBHLYMN_GhmEJwBjT3HAGpIX3kMdiUg-aRzl-_mRchqTNaxKvRiPiVQuE9ERirksXMe6T4JuucjlnrBw7HtexSe-L0_X3WqtyyrEqm23GqtEbraBpax3mmoNcC_TfTmkFaAH_m4vtFr0EL_SEZmgqxMVc19y6eEQmIfDgqoRXT5Dsoj0V1UpSgI0ox6yJURaXpHx13855t7I-_pL5TH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a2f85ffab.mp4?token=Ks-iTw1dfuhTyIXmTUgUdx4POsSCzXDFNwyuDPXmKrSHfGS8x73BAYH21-Rfg-rcr43d4qLPANuU04CvMOVScfFsvodezcpHifFJSWaFqobj9YtuWt1Ng3-SSyMV5ZierwYBRohTJ7_-JAg0CnroSVf11t3rj5Plf6OZ3GkyknycBw-czo4eOv5UYEcU6sg-K_uQ4QMtg9XLVI_gETilC0XUA_1RBS1khlnrmtYmGNVuGU1yRNrAeypvywkXYdATiy1gz7BcA2NRJ9G9IAqMa72iU3xmY5SRd6roSCbdtrazJUR5CfMrz7QttK_CHnQExSLgr9GcgSv_iPLlZLI1M0hnGEXT6WRT5edyW2Y2XC9UdI8rVB55IHVy3ATXl_2AYk9nMMElofd66Pfmrz_E24DRtG6HZe8JtzpUSno5thU00nFjFF4prKzgjsIUaWMaAdfUEwkoPsI6NiEhQvdixnTxBHLYMN_GhmEJwBjT3HAGpIX3kMdiUg-aRzl-_mRchqTNaxKvRiPiVQuE9ERirksXMe6T4JuucjlnrBw7HtexSe-L0_X3WqtyyrEqm23GqtEbraBpax3mmoNcC_TfTmkFaAH_m4vtFr0EL_SEZmgqxMVc19y6eEQmIfDgqoRXT5Dsoj0V1UpSgI0ox6yJURaXpHx13855t7I-_pL5TH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باهنر: رأی دوره دوم انتخابات ریاست جمهوری به آقای پزشکیان و جلیلی رأی خالص خودشان نبود/ روند حضور مردم در انتخابات کاهشی است و مردم از ترس یک نامزد به دیگری رای می‌دهند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
متوسط حضور مردم در انتخابات مجلس ۴۰ تا ۵۰ درصد است، اما در انتخابات اخیر پایین‌تر آمده است. افت حضور مردم در انتخابات قطعا به معنای کاهش سرمایه اجتماعی نیست.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/677766" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677764">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2164949e3e.mp4?token=QclkYO-uhJNvLyFnlQO3WhZiRe3HQD8rLNol37ZYaNCwchkq3WHO6Bf_pYcW7XOvmvKb9HGR8U2rASR-mq5UsxObz7XkN9vjrYwdBnZSHHmVd6Yj2zNgvR_T98AP2w_gs0jr-gCIs7r45Bw_r61iW0zdaCue7HU--RSo9S53TJbmr-wyZR6MMc94S43KiFuMHsyY2L64tokinWOkJ3uyOez-yiPH7GJ3DZf97thiehsEY2QOi-LI74V39RCDViKI7whXY4nUN4rMCTu2_EAWjQ_PsgrgIHP0xGpJZncEk8YdyT8XvjaR9V-KClT2GtouBdV6k2VD0M4G-bl8bE_F_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2164949e3e.mp4?token=QclkYO-uhJNvLyFnlQO3WhZiRe3HQD8rLNol37ZYaNCwchkq3WHO6Bf_pYcW7XOvmvKb9HGR8U2rASR-mq5UsxObz7XkN9vjrYwdBnZSHHmVd6Yj2zNgvR_T98AP2w_gs0jr-gCIs7r45Bw_r61iW0zdaCue7HU--RSo9S53TJbmr-wyZR6MMc94S43KiFuMHsyY2L64tokinWOkJ3uyOez-yiPH7GJ3DZf97thiehsEY2QOi-LI74V39RCDViKI7whXY4nUN4rMCTu2_EAWjQ_PsgrgIHP0xGpJZncEk8YdyT8XvjaR9V-KClT2GtouBdV6k2VD0M4G-bl8bE_F_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنج قهرمان گمنام خرمشهر؛ رفتند تا ایران بماند
🇮🇷
🔹
اینجا خرمشهر است و این ۵ نفر آخرین کسانی هستند که در حال عبور از پل هستند تا مقداری بیشتر تانکهای رژیم بعثی عراق را معطل کنند تا مردم فرصت بیشتری برای دور شدن از دشمن داشته باشند.
🔹
نه پلاک و نشان داشتند…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/677764" target="_blank">📅 17:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677763">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d706f40be0.mp4?token=vSboW5qbQp20U6IpjekFCbE9k5HhSDCbrqhLgUNCXB2HiPB3UMtZwMlPK4Mq9i-ECl4fIAtSOgXciqiQKhKV6P3a5BDwzDn9NtQ-gq2VQDZlRtnXoRHs35bhBTaeJ7HhRfdsV96OiILsLcPgwiiaLAlz3RtOBFFc5B8nhkWaCoZpZ5NJjGOiPuZjRigoxzeJchV8UEh8EDXrBPSnhnFIUIprmgUMMnX8Ftv9i9hdb8e8RNJcTCrBskYzfoS5pVn9-aHkKVO50yUwW5Pmvy5ot2ld4H9Jl2h3qyyQZ1rLYCCAhsb9ihSxm7JD8KWVQP1Z4jOUPP1hCnHUC0pdU-CbBlvWeNr3x2zStUX20E6PYUnX8PwRy8IomuDVXmg-URpTLlBGUUm58VcYWPsptA6KMGIKH_hTmHtAGHb8Tic4C48gwu7lAzks4REUWhmlHQH9MQRgC-Hjn6RkboD-tHDGLfdBqOiqjIFKP6KHew2N3kZ4J6glxoXJfh7lX8drzzqTntdPQMWQUvopdy-es8YE8nMi-OKVZMVIM5yBgyL17HOmF0QTWHJQtlctXqW4LJQI0aw4cXJSQh_1Yh-DPMndBiA-yI7xy-WFDaF4ECNPCPHmbH-qWDJFDQkaxY7tym4YeT6JoKZL3G9SljgBmnNYcnaekVA-INZK6nsJIinRHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d706f40be0.mp4?token=vSboW5qbQp20U6IpjekFCbE9k5HhSDCbrqhLgUNCXB2HiPB3UMtZwMlPK4Mq9i-ECl4fIAtSOgXciqiQKhKV6P3a5BDwzDn9NtQ-gq2VQDZlRtnXoRHs35bhBTaeJ7HhRfdsV96OiILsLcPgwiiaLAlz3RtOBFFc5B8nhkWaCoZpZ5NJjGOiPuZjRigoxzeJchV8UEh8EDXrBPSnhnFIUIprmgUMMnX8Ftv9i9hdb8e8RNJcTCrBskYzfoS5pVn9-aHkKVO50yUwW5Pmvy5ot2ld4H9Jl2h3qyyQZ1rLYCCAhsb9ihSxm7JD8KWVQP1Z4jOUPP1hCnHUC0pdU-CbBlvWeNr3x2zStUX20E6PYUnX8PwRy8IomuDVXmg-URpTLlBGUUm58VcYWPsptA6KMGIKH_hTmHtAGHb8Tic4C48gwu7lAzks4REUWhmlHQH9MQRgC-Hjn6RkboD-tHDGLfdBqOiqjIFKP6KHew2N3kZ4J6glxoXJfh7lX8drzzqTntdPQMWQUvopdy-es8YE8nMi-OKVZMVIM5yBgyL17HOmF0QTWHJQtlctXqW4LJQI0aw4cXJSQh_1Yh-DPMndBiA-yI7xy-WFDaF4ECNPCPHmbH-qWDJFDQkaxY7tym4YeT6JoKZL3G9SljgBmnNYcnaekVA-INZK6nsJIinRHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خواص آب پیاز و بقیه مواد مقوی رو از زبان خودشون بشنوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/677763" target="_blank">📅 17:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677761">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a13c543b1.mp4?token=u1MYKRG7JREcPMcOfyxObUj_7N16TQQF7m0JUmHaDclnH0V9IKN-UgvQ-zW63rVh7WWYXkSkLB0D16yF3u31TyUDMqg0lByRskYC3A9xTqEXpY7SoKzXR17jOmKHnGpgllyZTUv5z1Ynh1QfJBo2A5i0bRXgWbQJ1gSF6SyBdBNQfvYhzLregpqZImxuH_4mrNCzejJeJ9rVX1SXR9-qEbvvOCVFAFA5O0mMq0XUrNrpFn5vnEpXI19exO38vscM9JSTyHdwhDhH44UY2Le9GcAgV6FjxqeV1OvOd97XfSE5Nq40rt8U4kCdwZQ9BU_1Brm8d5STR11en5tSxbAL-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a13c543b1.mp4?token=u1MYKRG7JREcPMcOfyxObUj_7N16TQQF7m0JUmHaDclnH0V9IKN-UgvQ-zW63rVh7WWYXkSkLB0D16yF3u31TyUDMqg0lByRskYC3A9xTqEXpY7SoKzXR17jOmKHnGpgllyZTUv5z1Ynh1QfJBo2A5i0bRXgWbQJ1gSF6SyBdBNQfvYhzLregpqZImxuH_4mrNCzejJeJ9rVX1SXR9-qEbvvOCVFAFA5O0mMq0XUrNrpFn5vnEpXI19exO38vscM9JSTyHdwhDhH44UY2Le9GcAgV6FjxqeV1OvOd97XfSE5Nq40rt8U4kCdwZQ9BU_1Brm8d5STR11en5tSxbAL-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لو رفتن نام شرکت چینی در مراسم افتتاح بندر آمریکا
🔹
مسئولان لوگوی شرکت چینی سازنده جرثقیل‌ها را با پرچم آمریکا پوشانده بودند، اما وزش باد نام شرکت را آشکار کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/677761" target="_blank">📅 17:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677760">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما کدام الگوی مصرفی در ایران نیاز به اصلاح  و فرهنگ‌سازی دارد؟</h4>
<ul>
<li>✓ مصرف انرژی</li>
<li>✓ مواد غذایی و آب</li>
<li>✓ مد و کالاهای مصرفی</li>
<li>✓ رسانه و شبکه‌های اجتماعی</li>
<li>✓ دارو و خوددرمانی</li>
<li>✓ پلاستیک و ظروف یک‌بارمصرف</li>
<li>✓ سایر</li>
</ul>
</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/677760" target="_blank">📅 17:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677759">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec84885762.mp4?token=VhCbzVESF87DLs0POOeamJ0dWq_y2P_tDZFOksBuxP82g5wTpvxHr4z5ObYJQbxQM5T111kZYX9TTWGqDYEHUBpKjKL8xk4WWBSPK6o4Bvfm217u374zCTqKiX4kp3m2f88N9aTU-27n848kRlLrTmtEcJLDRzmV5-RlVdvJWheO2rRFuSxtldYNhZsUgbEaP5nnMsImd_IgiceRRkmGtfu-iGlZMD1fhaYmBvILy4JBPRA2_BfZ2yf1wh6lkeOkBn7u2NlLPD_rXYxbdifgZMQlmK6AA-81sJUbaiQ5-C81zwTl3BG6WGGPBdLkicE8lWJhHwFJVd7aVGD6qk_NBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec84885762.mp4?token=VhCbzVESF87DLs0POOeamJ0dWq_y2P_tDZFOksBuxP82g5wTpvxHr4z5ObYJQbxQM5T111kZYX9TTWGqDYEHUBpKjKL8xk4WWBSPK6o4Bvfm217u374zCTqKiX4kp3m2f88N9aTU-27n848kRlLrTmtEcJLDRzmV5-RlVdvJWheO2rRFuSxtldYNhZsUgbEaP5nnMsImd_IgiceRRkmGtfu-iGlZMD1fhaYmBvILy4JBPRA2_BfZ2yf1wh6lkeOkBn7u2NlLPD_rXYxbdifgZMQlmK6AA-81sJUbaiQ5-C81zwTl3BG6WGGPBdLkicE8lWJhHwFJVd7aVGD6qk_NBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو بالگرد اطفای حریق در غرب آتن
🔹
رسانه‌های یونانی اعلام کردند دو بالگرد اطفای حریق در منطقه‌ای در غرب آتن با یکدیگر برخورد کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/677759" target="_blank">📅 17:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677758">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
خسروپناه: اکبر عبدی دنیا را شاد می‌دید؛ او سعی می‌کرد گره‌ کار مردم را باز کند، هنرمندان کار مشکلی داشتند او سعی می‌کرد به آنها کمک کند
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/677758" target="_blank">📅 17:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677750">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjONT8z716gQqRTMTWU7HfHsa5gIuXCGcU95-XpTR6mLSDCinNtnEeyHXsQCM-NS_EzGEuARZQHstGjxhrfOvcBKAuoTRWlDTsy2_dSXwg3cBBDUJMt9ojP3Jc5xE1opBFm6iOisax1xn0HmdfeqMe-KCIXYR1__x_FvnZ6qoGhlS2zUQl8EF6zJP1xrZNOSaVvxteIdJS1zxuHLfCN3nXpA1Yu4exiGtX7c6np5AhL82hoMkD6j2modWXO5Q52y-kkHwo6kez-s0yzE_qKQHtJZJyEU9PwHcedKGSyMxY_rle8znjjg4mwTzUnO7m5jyKnH9vefS58rRNN28uugrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یزید؛ عموی جدید علی کریمی
🔹
علی کریمی این‌بار در پستی از «یزید» به‌عنوان عموی خود یاد کرد؛ اقدامی که با واکنش رسانه‌ها روبه‌رو شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/677750" target="_blank">📅 16:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677743">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2KirR8g9MHP8WRwxckDq786LiBBLAu6HfMS7g7Qjl_ZeVeeojWf1pjNq1MuHyIYUiSiu3tQF-EQwVJmeEgL_9-5cMbyzf2pAK528S-zgFh6Zl28EC2WlzfBTSbiRPJbMaCxoZ9YfLSggqJfnO7ihgcNTqtmyFUxYEuuHPm3JaaL5_MWEWVz3OHvCNjYO0Os21x2tZTW9iM4hszfLLLKSFLIZwXtOR3Bd6uhAJyXX_uUFtGxWpN6OJXkNAKBArSVMn-M0r1fP-g45RWCLiHs6DHm97vPMT6GY3thsw-yVzTSsrvwvo3fbUZ-a-ObJWj0h-GvMeEMbRrNj5r-E-khhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEvO0KVkVcZIKHOz_CV45yt6GJJPZ2uLg1Ao-RNbH8XFFmRCQ44oWEHFCrNG79JpMTUJ66A9mv2q3RxIMQLNEtPXGomFh794YTcfdcr_C4Nl8XZlwBqBs60f91-5Wlf6M53B_tI8q0i5MeMFI3e1EsqxWGsYiEEKJ8-mlsoM7soScn5OsWiasbOziSyvU_4Y_Gk_E1IgivX3SuF81L-JffZBonYccaVrZDkaC5p95BlWcXB0nvViMUA7fO-AshXZnDO4_HT8x6Hy4xZJI8lFxT3vmJrSXOxAiXuAgEoR2HOrLYZRlM0xhhfu5WP_1EXq9NZZBhFXyoBQ0HJXEhun1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/slzyVqO4YCOgN_lf6-y_2OP94iPc1E8U57BbHQRJxLZU-y70tWE4dn_Cr-x9CxeVbg2rXCufhP_ukCm3oPSEXzZj0OtFMJUmRHykRtetlNeY5b4BnDm-OT14ZemIoOOim-aF-ms3cfHC3iIr7FEXdI8Wyw5anoaY11ALSRVL3hZGj_VTi9UaUJ-7w43HTpOzEwv8VID0U2VloIWU3xXYv4x0kkAAm_-yzyEQWsWzhYN76IwtZ4KaUMKo4NmIg8PKxMWzj4HvLVxVw8vsEOnhzw8JqQi63JhyURsGW9z-UDNsCYTNmfH2x_YvVa1Y3V7q8iy0v0JBRPfxDnuCfyM-GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sf1jyjt5ot4g6dzQp4rjIIGW5LArZ1OVD5x4uozLTZlbOWhvNBAmaGILBjuL-0YJALolUKSNPK0-Ry8CnLbLhm8Q2F77cusFtMfbitMtyNLWhDpFnohN4TKMTy5VdYF-LANxdo7X9xtvAHG1r1xtCiOkLNuJLSpADf47CH8uh9Gu1LGeJARJ8AxoteSMK-edyhY4AeM-tLbTCMBU1zGvWKCXjSpcw6PXmyZivjhpiWbVZC6WpRugeYABo9IKwhZeLOLuqVpRCK1PoOz7dYyYZjBimyV3l4YP7jHutZslauG3I_n0zYssgfUoh-dJc2rMsaXOcHpFZm4Q9ehDxPAtpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فوران تماشایی کوه اتنا؛ سیسیل، ایتالیا
🇮🇹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/677743" target="_blank">📅 16:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677742">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f9e79799.mp4?token=gtSxlacSWd874Yaa_jn1qYXMWqIsv4Me-2S0q0gYi_vgEzNxoaBzNW4niafwKV9MY78xLPMLawreFlzSkBasV6FOl18ga4YqvlI8DVCJEGGi8fJOeJA0jsG7_DqHT6LytTyhOrM0x6NbIlN0ncdAa3vO4yDKP6o3cGp87TW0oaeKVxUgg8HREXUaZYDj_QU8fGkGTxLdqAE05n5BDOTxQ2mZG3_-o8-YbW1L9BbHvbSXFH6vtfx7ua3LoYY-8siZjhaLEaJb86IxD1QafOO0N8w0tj7UnVzS4pt3CM14nj4-W9zGPt6KdRxr2utpzgvrDBYoWrVcPFHKBV04sd1Wqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f9e79799.mp4?token=gtSxlacSWd874Yaa_jn1qYXMWqIsv4Me-2S0q0gYi_vgEzNxoaBzNW4niafwKV9MY78xLPMLawreFlzSkBasV6FOl18ga4YqvlI8DVCJEGGi8fJOeJA0jsG7_DqHT6LytTyhOrM0x6NbIlN0ncdAa3vO4yDKP6o3cGp87TW0oaeKVxUgg8HREXUaZYDj_QU8fGkGTxLdqAE05n5BDOTxQ2mZG3_-o8-YbW1L9BbHvbSXFH6vtfx7ua3LoYY-8siZjhaLEaJb86IxD1QafOO0N8w0tj7UnVzS4pt3CM14nj4-W9zGPt6KdRxr2utpzgvrDBYoWrVcPFHKBV04sd1Wqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهران غفوریان: مثل برادر کوچیک اکبرآقا بودم و اینجور افراد تکرار نشدنی‌اند؛ امیدوارم من رو ببخشه که کمتر رفتم به دیدنش/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/677742" target="_blank">📅 16:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677741">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHxtvfhzajsgrO-eJH6tZJGJp1NMHq_iVZuHww4l7HCoipB63YaZU-txgQ8etHIM91eGQk_lVUUy60e25tgJVmlCXO7wMTbBqLrh_ct1UvmtnliaTEQHHFwKujzyi0FkJU-ildNHNHLh_ezHSx2-w4CggoxX3uxaCBL-wdDNFsl8T3TbcER2doz_c2FX_suAOxyUkxrwBdAdDbwqwxMA_aKkbJaJRHsDcx74eeaHP0BdPbg1FqHJD4mXrXCXxFGhcStJ82dSV6nzT763WjOv4jfFxkaZcLQBAZM6GD8YHUe3Afh7hKFX8xqSkfEbOB6pNIekFUIbdVYNjmx-zzk8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای جنجالی مایک آدامز درباره سرنگونی اف‑۳۵ آمریکا
مایک آدامز، نویسنده و فعال رسانه‌ای آمریکایی:
🔹
جنگنده F-۳۵ سقوط‌ کرده در کالیفرنیا در واقع توسط ایران سرنگون شده است.
🔹
او ادعا کرد پنتاگون برای پنهان‌کردن این موضوع، لاشه یک هواپیمای آسیب‌دیده را آتش زده و حادثه‌ای ساختگی ترتیب داده است؛  نمونه مشابهی پیش‌تر درباره بمب افکن b۲ رخ داده و ممکن است «سانحه‌های ساختگی» دیگری نیز برای مخفی‌کردن تلفات آمریکا در آسمان ایران و کویت اعلام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/677741" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677731">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKPRrbICgLXkiHKiaoqqE29sd0QiijTLenkEou0QvblGPVnTbDTPxB7XPtR_ZfCgC6cLhsflYUoY9IrOx0C0vgV-mPrqdZa8XlrgXOnyvKR7kgzvOQOZW8BuyhUFJhtZqUfFZhHPwZzXC_zMPWIelAbMX2gLXjMxv9M0WD56g7Tgof43V2AlJ0wDrLfRTC1lZqqrt4ycDqMoGJKddn8O5_JAg6pFij8sruguMTAve10IFq7CHAHzm7utvsk56AWKzbe-_UPAaUq1TdPiJ5nBwwVcFRB_Bja8--lsb4WmwYMWSSG0QabQNIBP31ayM6jtzAEkJEmHo4abyREaEjtM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPupgmM7uj7zDgyOMpcka_Alvts3Hk-yRG-BRpK-VN_1P7ooweK3PzKaR4xHJc1cPx95Wc47lOLRmpaa7kMGGM-uNLhYMlbWui1sarC-1jFJtZ2v1vlGGRRQO7QPTCYRI-1BkAzjjDsrLp2ZGkyAGDT6rZ5JR3L8lM2LbaE0gcys6nYdUsOx9_sDQUCIdopp3vZ4gmjKcfcqsjMWDg1Vvs3QXGI3FosHHTGp-sB55QpyGXmYwhNsZPIqyBvwmZDM9N4JBhG4QsJ2WNEw9WK3_CdmnrmofG3uK9XbqbOxurYWsgZeXG63uVPHUKfTGjeKD4Dza-6GDB19WLwBG21LWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJGc0gzP8Ns6XNY_jFmMtk_0pn2NHhyk2xFROIVjx6t_uxWI9jTbFmfdx92PdQ0dSaO4daoi09lB40VhWIr0LHNuge5Pzj3HNhLojocdiks9ze5oZutnRFhc6C3jUpQKbpiCuzCst3XcvpEmTPMHJOdg_Isw5h7BEzC4n9lf8k1PespgQE04R8ERy5Ms4VNg3GJhK1dtgVeQKpeJtyLyOoTn2yg_XWj-jerQGWCgd3fP96r45NKzdA-QF_ZnGrFwp-mo6YgAWipuXFTyAPt_ToshLHko1KrmIF9dLHkQqxFZTFXukOaK5CDpHsz-j170TgCoFlFv7vuIcnPnaEV2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q72aJ8hZy6LsZwuAcaFTNGPMfrZmetLpiLxdpxsfnHmLUCiQcPZu43wNzKAxxXXy3oCTCko17KA1iGEUIvr-6O1ZRpNyeqKY0xvIOli25aXpYSivJfGwt79X8j88VR1YoMq9VpbOiFEuJR6TkGox3WHInJ0nOqq7Q99UzEQ0SRO5k4QjBDDGupkiM02zlqPjExrNEbY6S6-5W3WWIqUAUgBP2O7VNARyJehKHnJhvA08lkkQ4OxP6eb6HYpzrwuqytgb3ygFPi00zjx9I22YPL5dL6FWQe1NzJJ6bxDcI03dzg6s08O9RdEkaCelHMlsRwcNv_q_wEU9VmH-Er4-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5l65uXuHYKfST6_3XChvvyTlkPrXF3dGOdpBFL3AS2sYLTbTXza4LrHtW4kEgbLi_jsM73MxoRfCWn86JAjOV3lJ5YJMDd2aq9KDHZxxAdhhud-7UAL09r2QlXPMFuhDpe3np7rExNr4tWuH-_Ga8GOtdqw9qdMv3SUtVf5XdgOPPWVEV57VIedecq2ZSaImOWiJ807-O0OCXHh9GbkiPOWQqgdFMMl9ISEsCkeJAjP6m4YiDFeAVHMVok99PoMNH0sx7ULjPUAe01_b0fU5xj9XKaKYSHiSBcmeh_43Hp91tF66p4NOqAy1mw_7hPziLGeF2Tek_pIFgP9Kew1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfHyY1fmN5e5UdCwqaMexHCboOKkdm56rMe3ADvb2GGKxzwRuirsetBy8LNfo-w2rX1vTQdqDAqwCDoaNLBxwFz1YA3PZT9X1Qkpc3Gq9pEruAmB80ZXi37ZiX666srLxDgTZiwSiNrUdeGkkb33nFsfaaqR_vcxgvuEDEELrfmOF4NuMbfqBPk4TglQrMLUsTKTSWp8LiMjpx7zBwl9VkiPDcJS5zuSpIoSxm0v6nW2UtjDH8mkWNym4VLiGxq-0se1J0-bUVVXHZV3xb8YAetWAzoRsyfzRbhM-FZqXiAnDKwAU5LST4ByrwWuOfasl5BsRswKnWrNTYI3sNqGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eT7myo-kaAlgfrTJ5wVtdtmK6jJlgnSIS2a-rEDI_0sTbuvjvQj60xQCWe-qIl7sxsUNJ3TYbwQcb2ETDhxFLuQCqyWBYFx2pA_d4Me1BBg7iGVJWKw46G6SfNDyESiG5yKCkrDW_1fXzVBuYs8t0axk2O8Mc0zVz2DrG9fDGYR83axD0xO0H2b_P0YtxbMVjAbdKLXHqLk00rP4a8_Jc2aKlyjVKYK0Eg_mg_yjg0h11BCsm6f0Omz0MJ1XuZ5KO3LTTAujirvDvge4Rg4UxBjlmHaQect_Epm_FWt6apbSv5Ipl24dYcsw3a91P-5v8Rg8He-RGGMR5tSgd4A0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrZ7Qbl57R0V_CbqWLEX8arRJS1GiiftlYd8j1-JVeL1-0eTRitgF4fhSqWtXay95KcBe4nmkm-zI1FKmgVXV6yrROdUh105i-xbC_G4RNVqPDf7IdoqW-0R0_X0Rp0IsOvsfoz0E33ZoohprNH7wlruCHwpT6G4Iwm1FXl__P3OgQJSULryw2ILW_7ABr1-ruv8DD3aveBVMbHC-LZTbfT2N3_Tk2oEmXQUsT0VUUDABWlF1R83Yu4QnM0X_g0XgxwrQzHruMFV1iOEyU7tOLg3OO5nr1MnVojCaolKJSSg4fKqtHwz476rP6kddSvpSt5tPRPbkR8gnV_Gysxlxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjzULQ94YmkNNnOA5_eMJGe1jzfbefU6X3-nebA0gygRyEpH7AMwdCuQQ4Lj52nSt225Z3e_LgWAPlOkXU7nhpFYXlEvuYaKuBl-u00y0ZGGVrJbpIgNCYYmLOHnfsVShQPk4Ux8-69-SzAlJke4x15elqnJzRy8wO-TVEt5pHmdgnBkqyyJqhq3WCsG5gi7-gnhaxHJJ7TeHGEs0R-0xV_sRrLtKugRbYN-zlONzvFFNzwL8WVIkzJ6iJ7OZ7ZnOPmqeM7onyumVzorXQFGTh2L85Gpc-rbj2if3Wa5u7VUWT-CqBcnfwzwJNgNtCXWPDnEBW2vq01VmZgpHBzY2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨️
قبل از قدم گذاشتن در مسیر اربعین، خوب است چند نکته ساده را رعایت کنیم:
▫️
ما فقط زائر این مسیر نیستیم؛ در کنار برادران عراقی‌مان، بخشی از این میزبانی بزرگ هستیم.‌..
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/677731" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677730">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzSGnsFbPkLYfbA4Kv_JbRgVd-9UuFSsZKfakdEigiU1m24pcADsfc9qIFGBb5zcHtI5Y8uSUPchqtouIAgEDCPPSZQcg6lZMOszC1fMsg7ENR7AwNRkie9Vdt6u8B605saAyH9kdqZ2Wdo2POzYMeyDW8jhn60HOWScA2v0EA9VApQITu_D8g9Vmew-353loyWHXE--37dDKfTjnA3cU6Km44BaxuirP6iQ855V5bWAiE-wp9Py_pb6X8iRfN3LvcAOLP9HPN0QOI34DTM9yFdmd0iEBfYmetzz4wQU-p80KyTBORiDjwNiU_2S1TuO9PCTnlqfLMp5tTdXi_9zEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس جالبی از خیابان فردوسی تهران در اواخر دهه بیست
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/677730" target="_blank">📅 16:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677729">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کشتی اسکورت‌شده آمریکا زمین‌گیر شد
🔹
منچ‌اوسینت، اکانت رهیابی‌های ماهواره‌ای، می‌گوید یک کشتی حامل گاز قطر در مسیر جنوبی تنگه هرمز لنگر انداخته و متوقف شده است.
🔹
بامداد روز گذشته؛ شنبه دو نفتکش در مسیر جنوبی تنگه هرمز در آب‌های عمان، یکی در ۱۱ مایلی دریایی شمال‌شرق لیما و دیگری در ۲۱ مایلی شمال‌شرق خساب هدف قرار گرفتند.
🔹
منچ‌اوسینت می‌گوید که این کشتی در جمعه شب ۳۱ جولای تحت اسکورت آمریکا بوده و هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/677729" target="_blank">📅 16:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677724">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEfR3UWD1loyeqOqjVzJP3XlWKQwi_cApRBHqATW6focAJVGghWmkpUaw9sjWvjwV5JnSnOkbohp5YGedFO-ljS8G-MRuc3k1cC5C1aHRVBIwvsJWEEnntPtjxF2MHDZ0jLxdPsn0TIbfJe05-SztV8fqMZ51Bia7jTvjciNdCQah1xLQsfxRVSf1kx8leGF5aGe4z0ETcqXi9fTnDmNPz6wAaZD-l7v23CwiU4k3Ld7sBQrDgHVTQ4RSR2L45bTpQjh1AeqOTDSVQz5BOhnkTEa4V21AJOjSIl1vZ63zWALOqWBzAJKqtG-XDNHYjbRepQ6NykJckVwn1yH93IDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umTNt5XWz2iUTsaBq7JbtNFJPhQ1C-BRenp3PMcfcCC8IKXzTcC2yzghDyhAY_Uvhg1EyPvN_QI1bzDDQtzAIvyddLUjd_xErsJR87BzlCRJrJp4qKgMSEmU9fRpplRdF-AndERfaKDPs1NOcDIC9rgr2W7sQ1lEi9qppH_hQQqfgBwRveZ0K4uFOc5PC3Agh6Fa309uXPRO1fp7RnGWmN5CcUFyVkvjrU2wedY6IEpyzMXQKKVSQN7jcRFW8pk8iO7PHtjmNTp4qqxDO-YYPu___M4Q7JJzO-vk_wBluBkBBn8XvaserbGPc9N2SEwEn4c_xbbulACIAeFq85EX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6owtfn1Ppsv4jE5PObdfiFH2mcvCQq4CAbIPw_lk25cIYTs6lbn0wxqfQGFBnnBDsjiZUa3taXlLNUTQv8HJ1XQtQ3lv45Qo8-27Z1vkt0UT3RrpGjdQPkMsaddio-mbxya5UENKo5E-OYFjlSP86db8NtLhyQ5qynITkgNqFr5bFG1EC-Qslr-K3uo24gpBP1WrWjU0FuQRY0DiswrzKKk46u793Fuu1nqd9tR70JxXx7cAHZM7-nkpsamO2o9DC62xFMr6dyPBdgTlpAMfC_eA84OqJJdSSyU5veZi5BVuRTmPpdNp6BgquG3OgEGImDgO_fV5UkkMDBih6AZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWL110ri8O82yZfmIl7fwaJ_6GZUgbZJbMUB0dHL12krOqlWMK6iqxiyQBeDu6q_GwU9vdu5Tk_3ePblHgGO51zyx1Ym9do2_dXqc191ehpClloeoNsFPpG5DfywnSptAmuFIWHmOLzcQ8gqi5K1IZ1w_i3RcR2YHA28tRKz7hV1qqeExzIQvHNhUFX_lcK6Rw76sgMhFy-so6320lDeWWN-IFm1xfi5ELDHE1qd09mNyW23zQ8w1iKEBMnLc85t691boUzTiExMe05GFIYi_5poqUaT1Usgy5Z1zhgYPF_1xKGlOjvbw4u6S3poEXt2TRudM3FNsbIrOuk-N6D86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvY8KlnUlUtsdnGCIh1ZmUnURiN5kZg3vqgdNTZeKLXJ-wzn3yE2XYw5nCx0x_iO8RDJpvCewVesuGpFyNKWFckcIQEQLQDy5SKVZBogtddXxt8UMyuuoJQljawI9ejSMLwGqfBNjY-MB62ldWMuj2M_Xqxe2ZGfXBYaHOIGCpGa9CuHhrjFvegYQUogOK0FpVdAisyHligBUfRg_VKV2a9b8ukgx0CxNDLVOP0Q2DH-9EObs094BabAOiHIV_O_wLkOupa0XQVwgE-zlMVD9DULSyTIe7b1PQfM-QVDT3mH3lPYR7AaAbCJUr1kjAxNT0bViMKW35PNiL8w7K1-YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا باید ملک سرمایه‌گذاری کنیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/677724" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c4ba95b5.mp4?token=krs3rlfDKHBU8T1nG4B6PagROwFlA-sV-TNac12BGJd2SJGWigdzn3t1SxL0bnte402VTGCOp2QFaTPQDNIKqy5t5qWqEpNrwUwH4FMiD7IaAgUGWXvZBN79D6zKd3slbsjsNtiJelYY2BDwpmqDxGG1DI4Hd0ZKm91vyh4t_QUpu1ndzk1CfIVkuRn9BmjhkoGCd_qxtGS2so630-yKPHAfoEi0oK_1TRYGEw8SDeArZK35sm9F5XA1gAfFpF7bV7AD3qdKDkY44JaUblED1s1D_oEatiujezTfHobIKDgzYzp8srhfQfFX16dTpMZzzJToW64eB-M0ArEiVDUfPw5TrTuAlU22YxIm-PuUZ8_jDCCFhvuD1niGMmklLj7jO-LY9WELZVMZpC2_xPI1LGTAXTpID-h9-5TsV1vG-IJAbJj5U-a62jGvhTC0CvSe-SEzk2vv2B1A3gQncrpUyKXrzajE1oFtjrFm7CzzDqfJPbnR-DHxp_ZvkUs_C7Iq9hZD8o0DHoasiowtYpwS_MGLloR7XUkWZtUoRIJ_0p5HbDxKaB0t-NKtlsTGzbJpcAFoKtM_LBC0thz006rgdUZd_nUOyKr7AlXSp0ATlC0Klkq0HjiPN6JS5IFZvya0uuvOV1aWTEeyWf9KSQ4CcIzb-e4PaBSSHpGQ_PCYdnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c4ba95b5.mp4?token=krs3rlfDKHBU8T1nG4B6PagROwFlA-sV-TNac12BGJd2SJGWigdzn3t1SxL0bnte402VTGCOp2QFaTPQDNIKqy5t5qWqEpNrwUwH4FMiD7IaAgUGWXvZBN79D6zKd3slbsjsNtiJelYY2BDwpmqDxGG1DI4Hd0ZKm91vyh4t_QUpu1ndzk1CfIVkuRn9BmjhkoGCd_qxtGS2so630-yKPHAfoEi0oK_1TRYGEw8SDeArZK35sm9F5XA1gAfFpF7bV7AD3qdKDkY44JaUblED1s1D_oEatiujezTfHobIKDgzYzp8srhfQfFX16dTpMZzzJToW64eB-M0ArEiVDUfPw5TrTuAlU22YxIm-PuUZ8_jDCCFhvuD1niGMmklLj7jO-LY9WELZVMZpC2_xPI1LGTAXTpID-h9-5TsV1vG-IJAbJj5U-a62jGvhTC0CvSe-SEzk2vv2B1A3gQncrpUyKXrzajE1oFtjrFm7CzzDqfJPbnR-DHxp_ZvkUs_C7Iq9hZD8o0DHoasiowtYpwS_MGLloR7XUkWZtUoRIJ_0p5HbDxKaB0t-NKtlsTGzbJpcAFoKtM_LBC0thz006rgdUZd_nUOyKr7AlXSp0ATlC0Klkq0HjiPN6JS5IFZvya0uuvOV1aWTEeyWf9KSQ4CcIzb-e4PaBSSHpGQ_PCYdnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: نباید دور کشور سیم خاردار بکشیم و بگوییم در همه حوزه‌های اقتصادی می‌خواهیم مستقل شویم/ در بسیاری از حوزه‌های اقتصادی نباید خودکفا شد و باید تکلیف خود را روشن کنیم
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
بالغ بر ۹۰ درصد مردم بر روی تمامیت ارضی و استقلال سیاسی کشور تعصب دارند. دشمن‌ترین دشمنانمان هم ما را متهم نکرد که تحت تاثیر فلان حکومت خارجی است.
🔹
می‌خواهیم کشور نفتی باشیم یا خودروساز، فولادی و یا معدنی. اصلا نباید خودکفا شد؛ خودکفایی با خوداتکایی تفاوت دارد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/677721" target="_blank">📅 15:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/677719" target="_blank">📅 15:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677717">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqKYMJULmBwAAz1Za5G8HBQXrhjXWQHR7fy9JRMyNeTapc22yZ_est8pDK3_H4HZu1qRvrIAFuySjTpxJzKuEgr6TRT5dmwn0mUQju76z3UdIexWbWg6ZNNaZlQ7JWW2LqfrEvpzjbUzhlpw8DGRFefIS0XpvYIp7VGGAKkFLb5ESHG9FySWn2tjB1QrWU8zSApPl-qQUOextwrWUMIerSoS-aEMQ1iMoHVOPAYBL2jNTwynR8AXPU1mL-erfq7-mugQj62v3zOJFYJOphdcW2KM2njxQjf_O7efHKIgk9OE15lH8ZAUy8WlsUBOQcxIqt0--kxQFfclitzh-PTCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکرار ادعای جنجالی اسموتریچ درباره تحقق «اسرائیل بزرگ»
🔹
بزالل اسموتریچ، وزیر دارایی اسرائیل، با استناد به متون دینی ادعایی، بار دیگر آرزوی خود برای تشکیل قلمرو این رژیم از «نیل تا فرات» را علنی کرد و گفت امیدوار است این رؤیا روزی محقق شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/677717" target="_blank">📅 15:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677716">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
نماینده مجلس: ۲ تا ۳ هفته آینده قطعی‌های برق تمام می‌شود
سنگدوینی، عضو کمیسیون انرژی مجلس:
🔹
تاکنون ۵۸۰۰ مگاوات برق خورشیدی به شبکه اضافه شده و تا پایان سال این ظرفیت به ۱۲ هزار مگاوات خواهد رسید. قطعی برق شهرک‌های صنعتی به یک روز در هفته محدود شده و تغییر ساعت کاری ادارات نیز حدود ۲ هزار مگاوات صرفه‌جویی در مصرف برق ایجاد کرده است./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/677716" target="_blank">📅 15:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677715">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d6b73bf56.mp4?token=bnQZ9sDBns0u7fUK3_9Gziheg6kt9nGxG-YzH5HzlgoXPOtv3EqPvN-rnSMznGOJjNcsLGzaZWg9GHjbC9UnzNdlBA7Ies2uaJFQ5krf944s7Nhspkfr-vAwae-o9lIT9-hz6I8x36ah4sql-F_ReeXgpoae2avRhq_i6dbSg_uLb7ATb3zagQCHLnD55rDUMlbTv9bsfiTMR7eGerksVqDtB8uV2Wt1Wq4kQV_wGhUBVpXSjQaomPWV1ZgEqEmipFV1P3eAHev8Qeu88qGtzG0Z1OQsvtriQYo0_NF928ZahZiitoGTRXQ4MTuvmlzeRWHvwIovU07Lznw8kxAU2JsaahVJ814WHJGOzZEB_feLPtgPxNav1DJhA8J0LvytgzpebdOQ4VVbcCgr9KvB4M-skEXnr6tYSSuRV-KApm-XCiAzQM6KikzBSFqSYLKRo5vgIse4vto7cSwOcxDsICS9hQ9-hN4MQNH1sPBrQstJALoLLwyq5avGFuqRtRZUGuphdiuepSF8CcXQEpW9YwN_Kv2GxCnQZpX3sX3ApwxzS0lwTUy6oDHabenUMzwwtauK8qhm0UeBpRcMj2HqH0PvVSXEuMIsEso3BIsjmgYAYjvFGQIPQeNJSdBd7x-5SvTzg_5lfgsQGkgJMgyv_5zhJlrWQ9Kh6GsOX6tKlTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d6b73bf56.mp4?token=bnQZ9sDBns0u7fUK3_9Gziheg6kt9nGxG-YzH5HzlgoXPOtv3EqPvN-rnSMznGOJjNcsLGzaZWg9GHjbC9UnzNdlBA7Ies2uaJFQ5krf944s7Nhspkfr-vAwae-o9lIT9-hz6I8x36ah4sql-F_ReeXgpoae2avRhq_i6dbSg_uLb7ATb3zagQCHLnD55rDUMlbTv9bsfiTMR7eGerksVqDtB8uV2Wt1Wq4kQV_wGhUBVpXSjQaomPWV1ZgEqEmipFV1P3eAHev8Qeu88qGtzG0Z1OQsvtriQYo0_NF928ZahZiitoGTRXQ4MTuvmlzeRWHvwIovU07Lznw8kxAU2JsaahVJ814WHJGOzZEB_feLPtgPxNav1DJhA8J0LvytgzpebdOQ4VVbcCgr9KvB4M-skEXnr6tYSSuRV-KApm-XCiAzQM6KikzBSFqSYLKRo5vgIse4vto7cSwOcxDsICS9hQ9-hN4MQNH1sPBrQstJALoLLwyq5avGFuqRtRZUGuphdiuepSF8CcXQEpW9YwN_Kv2GxCnQZpX3sX3ApwxzS0lwTUy6oDHabenUMzwwtauK8qhm0UeBpRcMj2HqH0PvVSXEuMIsEso3BIsjmgYAYjvFGQIPQeNJSdBd7x-5SvTzg_5lfgsQGkgJMgyv_5zhJlrWQ9Kh6GsOX6tKlTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحول دیجیتال در قلب شهر مشهد
🔹
شهرداری مشهد با اجرای پروژه هوشمندسازی کیوسک‌های شهری، گامی بلند برای تبدیل شدن به یک «شهر هوشمند»  برداشت تا دسترسی شهروندان به خدمات شهری سریع‌تر، راحت‌تر و جذاب‌تر شود.
🔹
تلفیقی از تکنولوژی و زیبایی شهری
https://samesh.mashhad.ir
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/677715" target="_blank">📅 15:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677714">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781b3315bb.mp4?token=XI5xkemZaQ9TirTz1eJdKOutRMyuMKvSzqTyTpkRvg5p71duKO4icPk3qQo6mR4eCdftfXjvrnXsrdYLNpz7-gW56_TOjxNs09NjZnKNrZm14cfd0yoQ5rarwxu4eg1xIBuT7b7-ZNuVs6z93R4IZJwt2M8JJRaKwFRFWJclwmy9G61wX3sZJwcd0eJGXqjhTsKv11YqzR43AY6nNgv9Mt9PBZYtHbjviHH7bvKJQeF-PFa7AZq1F7fnUlym6dN_Jn0IuNL_dx2pgTJqoM93Of4s-fDRd41gHMauyuufd2_UKY7HuAOWYh1fqsNnlMHm0VHbj6HLnWd_NAUIkWJtMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781b3315bb.mp4?token=XI5xkemZaQ9TirTz1eJdKOutRMyuMKvSzqTyTpkRvg5p71duKO4icPk3qQo6mR4eCdftfXjvrnXsrdYLNpz7-gW56_TOjxNs09NjZnKNrZm14cfd0yoQ5rarwxu4eg1xIBuT7b7-ZNuVs6z93R4IZJwt2M8JJRaKwFRFWJclwmy9G61wX3sZJwcd0eJGXqjhTsKv11YqzR43AY6nNgv9Mt9PBZYtHbjviHH7bvKJQeF-PFa7AZq1F7fnUlym6dN_Jn0IuNL_dx2pgTJqoM93Of4s-fDRd41gHMauyuufd2_UKY7HuAOWYh1fqsNnlMHm0VHbj6HLnWd_NAUIkWJtMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مترجم کوچولوی موکب اربعین!
🔹
این پسر، مترجم فارسی یک پزشک عراقی در مسیر پیاده‌روی اربعین است و با ترجمه‌های بامزه‌اش توجه‌ها را جلب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/677714" target="_blank">📅 15:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677713">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCRI5jrNYkBQrPWY-myyBT90gKo01EzAdwBIouQSRLHZEyFg6yP4x--CoGP5RQ32RA_5JmamTWoXuy1LnOjDlvpTUGwtj70o2O4j3lFV7CzuPYkgiJQTXWe6A1J3p3_tGkM5Qz8KLGVKcTxwgm1S7ackdHczt8TToK7z9SWdmhe3kUd8tSQ_tykeUiUtC6ZHtHv_hW9lfEU0PYl7RJ2VLFVakPEhKJAj3Ek6My5o3ykPrHOWB0eGTZhHXnWIerCo9Pqdd6cL2XG6bABpho19BTKfD3Wqtw1-LdRa5nqQR0zToktEMAvCOt3055rrK9MF2446eV60bloikR2xed1ajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
من حاضرم همینجا بمیرم  ولی با جنازم یک متر از این جزیره رو حفظ کنم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/677713" target="_blank">📅 15:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
جهش قیمت مواد غذایی؛ روغن جامد با ۴۰۰ درصد رکورد زد
گزارش مرکز آمار از افزایش قیمت اقلام غذایی نسبت به تیر ماه سال گذشته:
🔹
مرغ ۱۹۰ درصد، شیر ۱۵۰ درصد، ماست ۱۳۰ درصد، روغن مایع ۳۴۴ درصد، روغن جامد ۴۰۰ درصد و سیب و موز ۱۰۰ درصد افزایش قیمت داشته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/677711" target="_blank">📅 14:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcAwtxDyoLI9cRXl5QtRrdHJnivjK2JgxShj4FOqqBJebHFRbh7jDZ13nrZdsLCMaYdqiQh2sJ8IyIKLpvHWe_d6hiNiJv5Ic4WLJb95hJgjlNjFS_ikkAF8HwqFr6ytOGfbg1sgftOeb5p5bkQozHAbHozN0ZmMjvgDYksIjvNDQV_4OEXMthBAVM_FZ11e9zZdNky4rTUPJ-H3VrY5ELxnoiSVasE95kXY5QG4YxLEsLNIGnzWqD_iIBu5R2u-ysKvP149wJpgg7EaMcDZ1NDyJ_IoxmJS1P0yahROVcq60pLWsOaP2pj7uFaVL3XLYTO1CAcq7FrUZb8SDXBM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صورتی رو با کدوم رنگ استایل کنیم؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/677710" target="_blank">📅 14:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8ef43fde.mp4?token=jq0hD0x6nSRatk6yVQly6BKUFCCIsbV6hF2AaaFLRmwfgE0IK6Aq2b6jxguRYyoUwlCa29yFlMlrmVK9KpPvXODMBFEtNOd5xs9cr4nYF8ZRSoN7dvGzzu56hVXli0fxs6s7TuiTJbOQs-4hBshZqqd-xN71cOohrAKzRHfOM_IThWmm2T2Ipef0w2sO-co9-4P5s40s2dfia_0MsZwCgkX1jvkVPTwzI2wSKdHD9p307akvEHI47lVQo1zzRD01d_JT1rtsevKPtIgRzAKylmuac-ui8BJtfk_4cNpgH1NQBiVEe5x8QRFwFIrH2GApvZQ5UmlQI6e7uVoRuG5vKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8ef43fde.mp4?token=jq0hD0x6nSRatk6yVQly6BKUFCCIsbV6hF2AaaFLRmwfgE0IK6Aq2b6jxguRYyoUwlCa29yFlMlrmVK9KpPvXODMBFEtNOd5xs9cr4nYF8ZRSoN7dvGzzu56hVXli0fxs6s7TuiTJbOQs-4hBshZqqd-xN71cOohrAKzRHfOM_IThWmm2T2Ipef0w2sO-co9-4P5s40s2dfia_0MsZwCgkX1jvkVPTwzI2wSKdHD9p307akvEHI47lVQo1zzRD01d_JT1rtsevKPtIgRzAKylmuac-ui8BJtfk_4cNpgH1NQBiVEe5x8QRFwFIrH2GApvZQ5UmlQI6e7uVoRuG5vKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیافت هوشمند پسماند غذا در مدارس چین
🔹
مدارس چین با سیستم‌های هوشمند، باقی‌مانده غذا را به کود تبدیل می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/677709" target="_blank">📅 14:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📱
اینستاگرام تمام پست‌های عمومی را با هوش مصنوعی تحلیل می‌کند
مارک زاکربرگ:
🔹
متا با استفاده از هوش مصنوعی، تمام پست‌ها و ریلزهای عمومی اینستاگرام را از نظر محتوا و لحن بررسی می‌کند.
🔹
هدف از این اقدام، شناخت دقیق‌تر علایق کاربران و ارائه پیشنهادهای شخصی‌سازی‌شده‌تر در بخش فید و ریلز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/677708" target="_blank">📅 14:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac27ed8c7.mp4?token=Vq1uImr8EwJFWc4DL02e8ZyswjRHSQR4pd-81IrUUdFFWHTP2bHCUjkovVCDUSsg7ZU4ZwTMgJREgKC_Fbt62p8l99ixx8pwhZl13di5tQUw8JseSPfc7NU5DVDSR_Mc2Yi6XPYGTC_Ho4VcmniiN_dbhaSVucNcPr48mfO0RxUMtmRNc21OfZs5jq6ywYGqUyCv0Ic_6s9IzTZRRKMMi9mWJrVdXHDtk8PdCdtxBWugy6odQMR080Rt2Ullsxuy9i7IQYF_OS_zLEyj_ayTdPjT_K6FiOaFdLDdpojbnAsxr9hJ5p1gz4dR7I2eWMrtq20BDSm5siZfOF14MuOsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac27ed8c7.mp4?token=Vq1uImr8EwJFWc4DL02e8ZyswjRHSQR4pd-81IrUUdFFWHTP2bHCUjkovVCDUSsg7ZU4ZwTMgJREgKC_Fbt62p8l99ixx8pwhZl13di5tQUw8JseSPfc7NU5DVDSR_Mc2Yi6XPYGTC_Ho4VcmniiN_dbhaSVucNcPr48mfO0RxUMtmRNc21OfZs5jq6ywYGqUyCv0Ic_6s9IzTZRRKMMi9mWJrVdXHDtk8PdCdtxBWugy6odQMR080Rt2Ullsxuy9i7IQYF_OS_zLEyj_ayTdPjT_K6FiOaFdLDdpojbnAsxr9hJ5p1gz4dR7I2eWMrtq20BDSm5siZfOF14MuOsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تراژدی در دریا؛ آتش‌سوزی کشتی مسافربری در اندونزی/ ۵ کشته و ۴۱ مفقود
🔹
از میان ۲۷۱ سرنشین این کشتی، ۲۲۵ نفر نجات یافتند و عملیات جست‌وجو برای مفقودان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/677706" target="_blank">📅 14:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c6ee52879.mp4?token=GUgFYdZmPXPX7CS-46DlSBeHl2EOFAiGQEFAbgl5XMS0b8fb54VVyIOFydnyXQTtkyKuJdtz5p21n00-gGRFgaGUwvG6sRdOGGCe9a2dKyN3h2U-dyGfbKggjKxkHTNCq6AJpjfuYv-S841Exvg3S0h2NplRI983uemFJBR8bOlqPwxbOMSsx5wQRH0ZP_nMAhgQFyCdI5BzyrKHM3x62YbnSmg54KfayPezWGgmpDbokLBra8A1Z-GMY6eQpc9CeVDBO6D2sR3kzM0Djwp7dMRDfjUAPua0Ku1fhcs4ckqv9oT6dpznAHDXSzi1iNL2-Qp7JLzw6EjM9Am182Kc_ztxKHm_ee6JYvPWoPGytD8ZcnkcbVNMpt7jAK4uLhM61IEbVqDPoJxeNkVoAsnngIirBIcHyWN49Ji2V6TDTPqf4lUdkuV6Xaqfci-6E-8bNSH37F3KHUlyIqnS0owZ1uHB2NewMMopIJh1HDk7v0B45arPbUEOmtTq1ttLTUcbbCrtOj-yZu4B-S_uRKhb8CyA-EfO4RDu4ideO6-SMe77LOYKTuVhzgaa037KtdHSlQV7wbRtX1snAm0e9omUkYtLB4UyPHyzxgDgfg_emGaV2QZg6gfDLoPS2f10R1TYRHF2Ss9NrcL9Xheaue0hAKLKp3F3Qv82Hgqt1RpTaBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c6ee52879.mp4?token=GUgFYdZmPXPX7CS-46DlSBeHl2EOFAiGQEFAbgl5XMS0b8fb54VVyIOFydnyXQTtkyKuJdtz5p21n00-gGRFgaGUwvG6sRdOGGCe9a2dKyN3h2U-dyGfbKggjKxkHTNCq6AJpjfuYv-S841Exvg3S0h2NplRI983uemFJBR8bOlqPwxbOMSsx5wQRH0ZP_nMAhgQFyCdI5BzyrKHM3x62YbnSmg54KfayPezWGgmpDbokLBra8A1Z-GMY6eQpc9CeVDBO6D2sR3kzM0Djwp7dMRDfjUAPua0Ku1fhcs4ckqv9oT6dpznAHDXSzi1iNL2-Qp7JLzw6EjM9Am182Kc_ztxKHm_ee6JYvPWoPGytD8ZcnkcbVNMpt7jAK4uLhM61IEbVqDPoJxeNkVoAsnngIirBIcHyWN49Ji2V6TDTPqf4lUdkuV6Xaqfci-6E-8bNSH37F3KHUlyIqnS0owZ1uHB2NewMMopIJh1HDk7v0B45arPbUEOmtTq1ttLTUcbbCrtOj-yZu4B-S_uRKhb8CyA-EfO4RDu4ideO6-SMe77LOYKTuVhzgaa037KtdHSlQV7wbRtX1snAm0e9omUkYtLB4UyPHyzxgDgfg_emGaV2QZg6gfDLoPS2f10R1TYRHF2Ss9NrcL9Xheaue0hAKLKp3F3Qv82Hgqt1RpTaBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از حمله آمریکا به یکی از زیباترین سواحل خلیج فارس در روستای بنود عسلویه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/677705" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5TztulqKy8fytx3dU7ZdMUIExeZh1EHp0aqQWHuvp6vyHK5uRll5edBr-7qGrDvMqODXE4LDTJVejHFlJUGG_BhNYDZcID8jS27sBC0dOCHnb46h2Glh4gcN6Lwm_SetzGyQUzfaOvsrelLrBJVGJuDpFjbD8sOQ0hb3KmlNPu7mKo9xmTqOpaQQ1-OcjjaYLTFkzCr_x-eH-pT7adlQCO2-94rtUKukuFwNt1YZSN0fXOGbFzbIUXdIIt1y78ypR63FPKXth95tRWmkX8tLtpf86KidR12wvN5Lt5Rkirjzh5PpkHMO_w6WNUU9V0sZkEOhyO3h9CVB44M1vkA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲۸ هزار تولد تا ثبت جمعیت ۸۷.۱ میلیونی ایران
🔹
بر اساس برآوردهای مرکز آمار ایران، جمعیت کشور تا پایان سال به ۸۷ میلیون و ۱۳۴ هزار نفر خواهد رسید؛ برای تحقق این برآورد، ثبت حدود ۱۲۸ هزار تولد دیگر تا پایان سال ضروری است.
🔹
بیش از ۶۷ میلیون نفر آن جمعیت شهری و حدود ۲۰ میلیون نفر هم جمعیت روستایی خواهند بود.
@amarfact</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/677704" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تیزر قسمت نوزدهم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای بهنام راعی که با داشتن غرور جوانی روزی به سینه پدر لگد زده و چند روز بعد بر اثر تصادف روح از جسم جدا و در برزخ شاهد عذاب و شرمندگی به خاطر گناهان دنیوی می‌شود ولی در نهایت با دعای مادر و عشق به اهل بیت در کودکی و شرکت در مراسم عزاداری، مورد شفاعت قرار گرفته و فرصت جبران و زندگی دوباره به ایشان داده می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: بهنام راعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/677702" target="_blank">📅 14:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVvz2QPkRmjm3Fs8pbtvC94ttrFgzQVIWc9sEkbL3L1oGa7DIoh42zqRALWxrmVnoN3_42FGL2bAlDWwJ3cgXNpU-4K-0cGgGfcGMS3bPwA75KSYuH-eqkEBuxn1JH0hoUo7PjYVLgM7daAOIHWnDfmLziPrQrDHOWG-WLyNWyP8f0mGcMMXxn-dBS2dQ_9tBqjgMaK16s8Ou7lfHxJs97qy7q83hqRiEUe-NC7HUEpDu7_0pSBbgk21R2kH1yqD1WQLnbWiYI0W8iOo2rYWZ_53oSm9l0oyhLIeLXOqXiC7-hc5PI7zc5IPtfOB3Blqtn2khzP9H5lzhjnxYEW7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی با انتشار تصویری طنزآمیز، نوسان در مواضع و اظهارات ترامپ را دستمایه تمسخر قرار دادند :)
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/677701" target="_blank">📅 14:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677700">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8408da7d.mp4?token=bjfTp0rZAs0JMn4U7gwA25oxYR5WEWOfO2nuYJJH61L0rx4aAN6dBvZUchh8UfQB4hXf7eXlSqSd3JzeaYSPwpQTyJ4lY7JlR6pVcU8gtpqmDoJoYwrKmDPsNluIRaZBV5kUKA_53fcmo5Sl8_0YnE0c02hVjhoPpcKMGXBSxdShN5dGBn9zc65rhzP_QLJzbDDNljZWI4RTqWgEBJcYhB-mLV3BHvLzsJgNeKfG1BNicW157AZwlVTcaMTuk9pdRzklG2RPDaREBT-Bh3Up8Vpj9yjpdf9JfYaElBlkBvs60GkBxwg1S6VMJtjSJcqZe2FxxLRDFPq5I5lwmPaYwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8408da7d.mp4?token=bjfTp0rZAs0JMn4U7gwA25oxYR5WEWOfO2nuYJJH61L0rx4aAN6dBvZUchh8UfQB4hXf7eXlSqSd3JzeaYSPwpQTyJ4lY7JlR6pVcU8gtpqmDoJoYwrKmDPsNluIRaZBV5kUKA_53fcmo5Sl8_0YnE0c02hVjhoPpcKMGXBSxdShN5dGBn9zc65rhzP_QLJzbDDNljZWI4RTqWgEBJcYhB-mLV3BHvLzsJgNeKfG1BNicW157AZwlVTcaMTuk9pdRzklG2RPDaREBT-Bh3Up8Vpj9yjpdf9JfYaElBlkBvs60GkBxwg1S6VMJtjSJcqZe2FxxLRDFPq5I5lwmPaYwoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام: عده‌ای در کشور می‌خواهند مذاکره را ممنوع کنند/ دشمن‌ترین کشورهای دنیا هم در طول تاریخ با هم مذاکره کرده‌اند
محمدرضا باهنر، عضو مجمع تشخیص مصلحت نظام در
#گفتگو
با خبرفوری:
🔹
پاسخ‌های ما به آمریکا باید پشیمان‌کننده باشد، اما هیچوقت در مذاکره را نبستیم. تجربه گذشته نشان داده به حرف‌های رقیب نمی‌شود اعتماد کرد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/677700" target="_blank">📅 14:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677698">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/677698" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677697">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ff33ef79.mp4?token=N2bO_9THo5uDwRLzMGmnVypkFsP56Eu-ZD1gaVA7Lq576jZP-StjD8m0iOsoo_Gc1gmLR-gKVN_YSlYZWfL0aZLQqb-9bGcFIMsadA8Qx2Qs9W_5RYiIkxbpbIwGTS2cKjMvFU8CempUa_ukWd709sENmc_woykf-vWZ3xyGWsyGkv9W37pgG2h3BFopl37NplMYut-YWS9DfMlZpOda5c9_0pIpgEQW-NIFupQwX_S6UuEL3VZdy0nacWMTXuBcWT8yiduMDNg4cSnpcMXkaHx7aU6rXvLK1IL7SE_ByT9F3GiSks3BEk_ucv8tgyxpLlT5WYcp-sXmY2hz-PYziA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ff33ef79.mp4?token=N2bO_9THo5uDwRLzMGmnVypkFsP56Eu-ZD1gaVA7Lq576jZP-StjD8m0iOsoo_Gc1gmLR-gKVN_YSlYZWfL0aZLQqb-9bGcFIMsadA8Qx2Qs9W_5RYiIkxbpbIwGTS2cKjMvFU8CempUa_ukWd709sENmc_woykf-vWZ3xyGWsyGkv9W37pgG2h3BFopl37NplMYut-YWS9DfMlZpOda5c9_0pIpgEQW-NIFupQwX_S6UuEL3VZdy0nacWMTXuBcWT8yiduMDNg4cSnpcMXkaHx7aU6rXvLK1IL7SE_ByT9F3GiSks3BEk_ucv8tgyxpLlT5WYcp-sXmY2hz-PYziA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی «دقت» به اجبار تبدیل می‌شود؛ OCD چیست؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/677697" target="_blank">📅 13:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5GrWY_fnHdrYV1ga5VXVto3_fyBAfyY_eUzVLncOYqLyHtxPoeVWCMO80w0k8d37hjsIvEcmwdg-gNUfmTJQKpxFpWVbIiq6Z0ZaGqEJotxa4w-Pqqyl1aZF6pSSsRaS72rEQelANGPoApmxOs7di1MgRkjjp5GTQXrLS-IHdD3ao4BASslPWwJWM110FPtrVfAORPSNEOIBnftVBNyKMWYqGssVLCzgJWdk1bhI5QzKtUYGSLG9s3NqjRToCzbSwdWjMi9zZRJCu6vuvvy2i2z_xfKkQ1zV-f6n1RJYgySsAf7baQeBTYadc_aPRZyqBVpaaH8Nfux8Xw2fDstrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
شاید چیزی که اضافه برمیدارید سهم کسی در انتهای مسیر باشد
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/677696" target="_blank">📅 13:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s42DuIKmwa82Fjnbbf2mPji5r7i_ZMiWFK1JKg-foq04IxAD7rz0suLAFloy2AumMawBhDXtZE0ke4FtWJ3o9m-L1H_nR1w_qhQn83FxnuH8a6jsnIIliDxSNvW3FWmLH074oe81cG4_IrOm8btzofK7sRbTrevqiHMn0yo-1k3S4x7elbsTc43_U3jn7VfxRXtO3nYs7eZ0fsvB2DFFokTiIJOWA9bcRG_bjPkzvYFSLdvc6UPLGZnrOH5Thtd3R6b_pg5J6tyC03dZXVrGcLCdOzCfk9TYXvvKTi3iy4MRwUMEYphKsrWfvZqb_5ofnFzRfJ3h242fdd65AX3RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر اقتصادی: هدف ترامپ از اینکه این همه تهدید می کند و حمله نمیکنه اینه که حمله به ایران عادی بشه و دیگه قیمت نفت و بورس رو تغییر نده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/677695" target="_blank">📅 13:36 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
