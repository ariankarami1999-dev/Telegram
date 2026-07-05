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
<img src="https://cdn4.telesco.pe/file/gmu0VEvnl7kkk6B3DNeqq3ZS-pldL5X1bIP7IpaMYvIuGHesme0UIMMNKxWBvnHo0VS_gDXoNGZt8PuR7wIdo-zNGnb8FBqQH-tOmqyeXzKkVHZgImNnHMbMGdvrVDMf2MS15TLYCDYfhQdY-ZFnqjZbwE71FJMg3hk0Grg_sTIIOl2uqOXHSAIA-1ai4yg2QiuC9u_hqnvIFb9i_u_2P13ju8RMktUp3Arg2N1dGg9uQUgMjYH_lkvHRLOGU5AEZcXLrg4D7K-xaijVA5his3rrIR_UwXB5lAW0oV9aRhhH6iZk4XQiHnfJw91B0kGgOAe0wpKJYTlNa0bJlclluA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.29M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 15:39:41</div>
<hr>

<div class="tg-post" id="msg-666966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1becbc856f.mp4?token=oCf31ZrxI090qeAGgVt68k4a3Z4TxpdWhXkJkZP9Yj0oikQ0YK0QaHF48Ypc_VwLloT-PvlDSh112TZTS9y_5MfNwjIFAyensZPlWt23Hcwg48jDB6Yy7SkLNXdof7BRhumpnZSPG7kPxyZpxoUbQp6aKY5cFtyo4RD74vA_MkhdtORPoSGuz6fjr-lPz0SOwwX3ggMf0CymvSjh-S3wRiuryMF5KyZbR7PTaPJPlFBkk1ZocVtbX13L5KbGONQS8mhIJr9o9b80Jhf-F0s8yn1X0DiyDaNQyMF_9iJGlE9LRNnLMhQqmMlLO1LOON5-MZ69sVwjo8X87BFDZr_XVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1becbc856f.mp4?token=oCf31ZrxI090qeAGgVt68k4a3Z4TxpdWhXkJkZP9Yj0oikQ0YK0QaHF48Ypc_VwLloT-PvlDSh112TZTS9y_5MfNwjIFAyensZPlWt23Hcwg48jDB6Yy7SkLNXdof7BRhumpnZSPG7kPxyZpxoUbQp6aKY5cFtyo4RD74vA_MkhdtORPoSGuz6fjr-lPz0SOwwX3ggMf0CymvSjh-S3wRiuryMF5KyZbR7PTaPJPlFBkk1ZocVtbX13L5KbGONQS8mhIJr9o9b80Jhf-F0s8yn1X0DiyDaNQyMF_9iJGlE9LRNnLMhQqmMlLO1LOON5-MZ69sVwjo8X87BFDZr_XVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقا، مثلی لا یبایع و مثل یزید یادم میمونه
🔹
لحظاتی از نوحه‌خوانی کربلایی محمد اسداللهی در مصلای تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/666966" target="_blank">📅 15:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWNfQDz633kLR_cMxrr3Ghb2xh4gYtROwdv1knjhECcN_BaptRKnn97F9LoFOQlfH_eHLXBPWD6lVH3o5VG-s0cPyTxWbj6c1PU3YndjQzIVxNDWqUejrIfhmME0K98TdXcbcRGe8FIY05k1So_x9CVJOwSaO4IHH9OweZLxs71fULd7ZxqsVca1rjh1V_U1PD6do-CxGJlSRJD6OI89yTT38bi-SLoT-YztZJJKYPbm4wBC8YQou4Xe44rR20giFkFKqONqsQyQWLOjs6YIF1h3t8EaW3mK4f3tVjBW5Xei_WPNFGiRN3dkf2h-nZ-ZSde9Y9ZzUTQf9mRmZZ6lMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهدی تارتار به‌ عنوان سرمربی جدید پرسپولیس معرفی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/666965" target="_blank">📅 15:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666961">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEP9mQfmyFI6ExIyStPBKb4H8oyuBG2O9McpLqblqcEqFsMz7aoTpKuu75Jc0jq6jwEMut7x9xvPzzAFhCjzHuCYRBO4dmxi0jJdEQAYIu4Q60n8-DerAKVITiemJHWAR1cx_3UJoggeJiiCBueArgD4gMA3SnX_RdYCoaZ5KUjIItvbwTzRamrWYfADVq5_nD9D2DzOMda4o6YB7XBIARl-JRZxdj_z3Cl6GhnvLSV9Sf9qBrClYWqcPQic3TuEGSwZ-UosAW36ch58ssBQOpYo5-NlpO0S4joPpv6FwISCC6y8VY9WJm6oYjcoHam994YIrJYZSB9kOvUM2U4dgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a44gcgkXDVbhWlDw4bumR27QX3R6lzCS5FT1w1D4bMeGAVPIn3S2vJT2yTgOhjOWndwrFX8P_7sXb5WxSs1afX-hlHdJXwRDkNOjJ0eOr6maB0vgGMZfBEdgCm73_3yEModYJ4p1cPE53tZCTzu89rWCR7x-VIsyF5QqUj4IuaQ95aggepZDwvU149Jc_rG-1JcuDvRLm8Ndxjn2QP0WkdvD71Spuw2G9wg04gL0cRy5BKgUYFAWjehDNI7jNKQ7HW3bZfiBGuWZfSlI_J-W88etK8FymTRbZjB26xi0F9ef20GaqLhINdpTDKIyc7G1Jy15P5gmVVR89-YEiQO_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U2wbM-KAdCLE4Wi34GD2MW6ZDZCRPUuOjCYQWPqYnpSwZ86TUw7MGBkQ492ovyUqwC0PhuT2n-_EysDHn1uIhZFGs5AlBLUG3JeOPcla3zBAeOMD98JbmfmzB0qd3YYz1kXLzH1Ko3bV91f2kIGyU-_pjaumEaiuA2LYZcB4Pa1d7OewLswN5RaMKgLRu3CxdUSrwpBBSz7KdoLqb2ZwnzaK5nQUiwd1OGaujYYQu8pPwWTnyxhHAlT7aAyODYptn-10Au9WpoZvViCUysKckvfmyZO3fb-_AvJg5ryZJ43rRdH8pVc1u74RYZ24xpP0f9zb8eboeUBNJWYRp5uXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAGIACk8mIrqT2-jJf3uppTdf35s5MapAoReQ8ZlkR-u7Zp5DsgyK1Fjz-5VNJCPRAV61_Y1qYQm33k8JS1Vf8oyW0JDqlxHDjPtKZSJY2oJ9FjFEKGMOcgtLCvxxrGffwUMSYqnOjQThe07v_YViGVv4x8X2ut0f_rzRv-t-cLxvS-ZyVW0Dn8mA-ix5-hdbIDQgEUcXUPDm4_Q-65IVKkqF5Mt8ddxcrGuflCmI4t3oFOy3quOkmRBb-y0V422MrWEWeNDVWYqqHt1raYIiyv76xyaYp0bHTyGHIZROnBe5JqC71EmUKHRU2JVy4swAFfyCKX9_IQPJuj7Clcnpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر پر بازدید روزهای اخیر در شبکه‌های اجتماعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/666961" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666960">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
کالابرگ دهک‌های مشمول از فردا شارژ می‌شود
🔹
از فردا اعتبار کالابرگ خانوارهای تحت پوشش نهادهای حمایتی، نیروهای مسلح و سرپرستان خانواری که رقم انتهای کدملی آنها ۰، ۱ و ۲ است شارژ می‌شود.
🔹
مهلت استفاده از اعتبار کالابرگ خرداد نیز تا پایان تیرماه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/666960" target="_blank">📅 15:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666959">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD5YjxF0ypUXeLZ0Wff9jtL_wQqbq2K8ZIH9Sksq31zYMOuReKr7JGJu3a1-QNuYSSCT4b6d3iBIA-MdCk1Nx1XPi6es2JfrqVlnoGoYwFDGchFIW9qUlSZlhSanJtFNvdNQwK2ZUqf6Z0z7w9DZ8qS39n69z-sBnGpHxVY0tiLKXcXifTOeY1nkeTjqcNAGVCdOeIWoQsUH4UsX849Wv3XJweXmWMTIFa2aCzF_CgdxXu_B9ZH4t7U0pRsQUQMPpuTZKMLUcB9oi9-bFFydx8CRcdQQow_KPkLuINMJJUpngSqX7MXRLQbXSyPbMhzkZ_6mMETI0TjVwl4pTRejbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید مدیرعامل از موکب‌های خدمت‌رسانی؛ نوراللهی:
#بیمه_البرز
تمام‌قد، پشتیبان زائران است.
مدیرعامل
#بیمه_البرز
در جریان بازدید از موکب‌های این شرکت در پایتخت، بر ضرورت ارائه خدمات در کوتاه‌ترین زمان ممکن تاکید کرد. در همین راستا و با دستور وی، علاوه بر استقرار شبانه‌روزی تیم‌های تخصصی ارزیابی و پرداخت خسارت خودرو در تمامی محورهای مواصلاتی منتهی به تهران، اعضای ستاد ویژه برگزاری این مراسم نیز جهت ساماندهی فرآیند خدمت‌رسانی منصوب شدند.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5056</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/666959" target="_blank">📅 15:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666958">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دفتر ریاست جمهوری سوریه اعلام کرد که رئیس جمهور فرانسه به زودی به دمشق خواهد رفت
🔹
معاون مسافری راه‌آهن: برای مسیر تهران - مشهد و بالعکس قطار فوق‌العاده پیش‌بینی شده است
🔹
نتانیاهو: ترامپ از من نخواسته علیه تونل‌ها در لبنان اقدام نکنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/666958" target="_blank">📅 15:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666957">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6isCCRac7qRi4qSJ5KwYpw16UpmVZDQyojaHXvGthsDIhrcm2yhN4Kx117Hk09JuvCNpO--X1QMHhVvaouuM6pZ12-Y1VYK-G5mdz-Z1nTeVyFLJ102YvhMhw27tM3hfVVATi4WVlwQfbkaeQCrjMngKeukJVJzoku_TYLKsB24yMHu1TVglLzYgxVtEssyRpgj1FOj4NZ3as7jy0JoVvCk52lER6v5rgQk34UxUYeK6_EYo-coRaz2tnYGeRJXbLpKU44UFb1QiUvUQDIb0o6zE8Ka___gmpsh2VcPCEnV_3-hXgp1c26QZ2-SMOa94vDdKqVNMJlZlQMpdGC1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳۴ درصد راضی از تیم ملی، ۳۷ درصد ناراضی!
🔹
تحلیل بیش از ۱۴۱ هزار پست منتشرشده توسط ۳۵ هزار کاربر در شبکه اجتماعی ایکس، از آغاز جام جهانی تا ۸ تیر ۱۴۰۵، نشان می‌دهد واکنش کاربران به عملکرد تیم ملی ایران عمدتاً احساسی بوده است.
🔹
بر اساس بررسی یکی از پایگا‌های تحلیل دیتا، تحسین و اعتماد با ۳۴ درصد بیشترین سهم را از احساسات کاربران به خود اختصاص داده است. در مقابل، غم و نارضایتی با ۲۰ درصد و خشم با ۱۷ درصد قرار دارند. این سه احساس در مجموع، بیش از ۷۰ درصد واکنش‌های کاربران به عملکرد تیم ملی را تشکیل می‌دهند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/666957" target="_blank">📅 15:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666956">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94fbae993e.mp4?token=ULBgNhYztoEDhUncARHmF_PW1UmdBNeeF3LEVdN4a2h54_KrjU-640GtFZkk1hWsWOnqo3NczxwZaG9lfgok9aQeKKPTfzLGNTAVT6x4XUFbEWOmMe4eA1xpbtb7V3CwkfjAs_JMrUFxcVddhKEMKnb8_Cq0Q9Ym_iinLZ5fnFh5FiIIJ2Jo834QgVNg9HEV73t73dEJ_9U5Iobypuo5ofxGpZvZdnZgO6l_zAhByr6Aw2Pwj34KXwJpOY6ReVxurY5eRlJbtodl8qxnY0Ou1h9cdJ3aacoS--nk3tWaiB6QFtkxA-RNCSqsUgx3oGf4rETxNfAgFUbakrS43wS-5VWz1zvq22CS93Z0s9PhtMpNEwtlHrhwPDz45BWqXWEeM9GvAS_ltUZRmaClSYQ0DX6DszN9bFdICdjgTEMqnA06u11Q-2gDF4hCi6dmK44AQ0aXsJqHH9H7ek4jbxqaDJKwhpEuXeXjeVbZkP1vAzcfg-QMpgJ_-N3GpdufZTFlmVsFmlxjVU6QIZNfbqwkiWDrDychdFQdK8zQhAoLjDEVBGAgoIzt0cqr8m5xuTo7JLncvXOQoFX3e6SGqVftDnR5p63kXylhOld7Ndf_svBI-iiEWBKC-V-NjgbF30ceSyL9IDiFM7JdoOoYAdEtIWOP22gigz4X6BtArZikkaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94fbae993e.mp4?token=ULBgNhYztoEDhUncARHmF_PW1UmdBNeeF3LEVdN4a2h54_KrjU-640GtFZkk1hWsWOnqo3NczxwZaG9lfgok9aQeKKPTfzLGNTAVT6x4XUFbEWOmMe4eA1xpbtb7V3CwkfjAs_JMrUFxcVddhKEMKnb8_Cq0Q9Ym_iinLZ5fnFh5FiIIJ2Jo834QgVNg9HEV73t73dEJ_9U5Iobypuo5ofxGpZvZdnZgO6l_zAhByr6Aw2Pwj34KXwJpOY6ReVxurY5eRlJbtodl8qxnY0Ou1h9cdJ3aacoS--nk3tWaiB6QFtkxA-RNCSqsUgx3oGf4rETxNfAgFUbakrS43wS-5VWz1zvq22CS93Z0s9PhtMpNEwtlHrhwPDz45BWqXWEeM9GvAS_ltUZRmaClSYQ0DX6DszN9bFdICdjgTEMqnA06u11Q-2gDF4hCi6dmK44AQ0aXsJqHH9H7ek4jbxqaDJKwhpEuXeXjeVbZkP1vAzcfg-QMpgJ_-N3GpdufZTFlmVsFmlxjVU6QIZNfbqwkiWDrDychdFQdK8zQhAoLjDEVBGAgoIzt0cqr8m5xuTo7JLncvXOQoFX3e6SGqVftDnR5p63kXylhOld7Ndf_svBI-iiEWBKC-V-NjgbF30ceSyL9IDiFM7JdoOoYAdEtIWOP22gigz4X6BtArZikkaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه خبرنگار خبرفوری با جلال ملکی، سخنگوی سازمان آتش‌نشانی
🔹
خوشبختانه گزارش هیچ بحرانی نه تنها در مصلی، بلکه در اطراف شهر هم نداشتیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666956" target="_blank">📅 15:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666955">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d69c6c7d.mp4?token=Gz9nZezs-glrqtidi29NHurO2uFD9TbPPHwi9z3XFqUJs2tCnawxRpIeMhZkPPI2RDDCGLHWj9shEOrtjVH32bFNBM6E6mSeHPKXFGTh4Z0RXw0CSHYMNSyq2Tky7I4APACrCP8kdPf-W0lpNT4MAxjXjjIldMtelhVEkk-ZCi9liY7-wNpvLDLrlMXbjkoa6ilx_ajZ905Yu0HLKzH7TPpPfgAoPYDuRZOeCZXp4D3wBlKCwvWus4YbqiXAFL0T1oMMej3V_znH2NLg-aUb9RN5_dKFbBf09x5LbhK4wDagPK-ca7MxkB0XUWQusTkRr1sGotpQIllx7SrUxxUPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d69c6c7d.mp4?token=Gz9nZezs-glrqtidi29NHurO2uFD9TbPPHwi9z3XFqUJs2tCnawxRpIeMhZkPPI2RDDCGLHWj9shEOrtjVH32bFNBM6E6mSeHPKXFGTh4Z0RXw0CSHYMNSyq2Tky7I4APACrCP8kdPf-W0lpNT4MAxjXjjIldMtelhVEkk-ZCi9liY7-wNpvLDLrlMXbjkoa6ilx_ajZ905Yu0HLKzH7TPpPfgAoPYDuRZOeCZXp4D3wBlKCwvWus4YbqiXAFL0T1oMMej3V_znH2NLg-aUb9RN5_dKFbBf09x5LbhK4wDagPK-ca7MxkB0XUWQusTkRr1sGotpQIllx7SrUxxUPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعید جلیلی: خونخواهی رهبر انقلاب مطالبه مردم و وظیفه مسئولان است
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666955" target="_blank">📅 15:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666954">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
کارت ورود به جلسه امتحانات نهایی تا پایان این هفته منتشر می‌شود
آموزش‌وپرورش:
🔹
کارت ورود به جلسه امتحانات نهایی تا پایان هفته جاری بر روی سامانه
my.medu.ir
منتشر می‌شود.
🔹
دانش آموزان پایه یازدهم و دوازدهم می‌توانند، کارت ورود به جلسه خود را به محض انتشار از طریق مدرسه محل تحصیل نیز دریافت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666954" target="_blank">📅 15:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666953">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
افشای همکاری نظامی بی‌سابقه امارات و رژیم صهیونیستی
🔹
میری رگو، وزیر حمل و نقل کابینه رژیم صهیونیستی، در گفت‌وگو با رادیو اسرائیل، تایید کرد که رژیم صهیونیستی در طول جنگ چهل روزه با ایران، سامانه‌های گنبد آهنین را به کشورهای حاشیه خلیج فارس منتقل کرده و این سامانه دفاع هوایی را در امارات متحده عربی مستقر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/666953" target="_blank">📅 15:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666952">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تعطیلی تمامی پارکینگ‌های حرم مطهر امام رضا (ع) از امروز تا اطلاع ثانوی
رئیس اداره اطلاع‌رسانی و رسانه حرم مطهر رضوی:
🔹
تمامی پارکینگ‌های حرم مطهر رضوی شامل پارکینگ‌های شماره ۱، ۲، ۳ و ۴ (خودرویی و موتوری) و همچنین پارکینگ خدام، از ساعت ۱۳ امروز، یکشنبه ۱۴ تیرماه، تا اطلاع ثانوی تعطیل است.
🔹
این اقدام در راستای اجرای طرح اسکان و خدمت‌رسانی به زائران و عزادارانی انجام می‌شود که برای حضور در مراسم تشییع قائد شهید به مشهد مقدس مشرف شده‌اند.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/666952" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666951">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/644bfd3a32.mp4?token=c6Stoz-RGfHxhwiF6clWrBGM5zhbHImD1ouV06Vpy6xq26qXb_lk4mcR_FiLjWrl5HRV52PyoZFo77FP6J46daQtNBe-Cm8l4jrFLfRSW4F2Zc4BOluUsEuEoEKQMG5oE0dSfRptBSik24YkTlBQKrZ_3I-BsQs4GU46hkX28WOj4NbGvsoypLFOcIVFYG4sveba9I2rS25tdKu9yPkfBxLmVEkCztB_dAtkAvfrCBS-XoI66pTdcfEeORA4z9JKmokC_MECuX5EAQRrc9D6V4pcbuZ_r6OgWzLMhy0_AgaUIi878xI3S-a33euwukI96epYDGMpaXMWz7rqELCMITdiWNyhyFuFCxPsgF-9r4KniQ2W_n82kN7oglmtOKmqxbzrxXtE_AOacBnVODskbuLSXV0acEQcS4HV6oyn_wemjQ_jjSHIhI7wNqu51BrXNpCBiMNeHeBK8zcZh_DJB70rYZObnDg3sbWRl-x1EXz7H5xQ-MIH-tjyuKssrkej-ihn5rZ8iu04ieLNnKBb3tjP7LhfZdcMNqmokjJDZ1FGYUm-NG8RwG2L7YyzBPnFZ0d6vh0W8Rwdb4_C_ktRuQ5vmd4S3PjYPMaRDsZWKofi_zzWktZQzuIOp0aQDgSf8XmKCKgaG5XkQZxcAI0-3IBw6esNVlC5jlE_J0ltxgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/644bfd3a32.mp4?token=c6Stoz-RGfHxhwiF6clWrBGM5zhbHImD1ouV06Vpy6xq26qXb_lk4mcR_FiLjWrl5HRV52PyoZFo77FP6J46daQtNBe-Cm8l4jrFLfRSW4F2Zc4BOluUsEuEoEKQMG5oE0dSfRptBSik24YkTlBQKrZ_3I-BsQs4GU46hkX28WOj4NbGvsoypLFOcIVFYG4sveba9I2rS25tdKu9yPkfBxLmVEkCztB_dAtkAvfrCBS-XoI66pTdcfEeORA4z9JKmokC_MECuX5EAQRrc9D6V4pcbuZ_r6OgWzLMhy0_AgaUIi878xI3S-a33euwukI96epYDGMpaXMWz7rqELCMITdiWNyhyFuFCxPsgF-9r4KniQ2W_n82kN7oglmtOKmqxbzrxXtE_AOacBnVODskbuLSXV0acEQcS4HV6oyn_wemjQ_jjSHIhI7wNqu51BrXNpCBiMNeHeBK8zcZh_DJB70rYZObnDg3sbWRl-x1EXz7H5xQ-MIH-tjyuKssrkej-ihn5rZ8iu04ieLNnKBb3tjP7LhfZdcMNqmokjJDZ1FGYUm-NG8RwG2L7YyzBPnFZ0d6vh0W8Rwdb4_C_ktRuQ5vmd4S3PjYPMaRDsZWKofi_zzWktZQzuIOp0aQDgSf8XmKCKgaG5XkQZxcAI0-3IBw6esNVlC5jlE_J0ltxgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه خبرنگار خبرفوری با مهمانی از نیجریه:برای عرض تسلیت و به خاطر عشقی که آیت‌الله خامنه‌ای و به خاطر فداکاری‌ای که برای امت مسلمون انجام داد؛ اینجا حضور دارم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/666951" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
اردوغان: اسرائیل معتاد به جنگ شده است
آناتولی:
🔹
اردوغان رئیس جمهور ترکیه گفت که نباید به اسرائیل «معتاد به جنگ» اجازه داد تا توافق آمریکا و ایران را «منفجر» و دوباره جغرافیای ما را در بوی باروت و خون غرق کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666949" target="_blank">📅 14:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
کدام فرودگاه‌ها فردا تعطیل هستند؟
🔹
در روز ۱۳ و ۱۴ تیرماه پروازها در سراسر کشور بدون محدودیت انجام می شود و برنامه پروازها به روال عادی ادامه دارد.
🔹
۱۵ تیرماه همزمان با برگزاری مراسم تشییع آسمان تهران به طور کامل بسته خواهد شد.
🔹
۱۶ تیرماه نیز فرودگاه مهرآباد فعالیت عادی خود را از سر می گیرد و فرودگاه امام خمینی(ره) نیز تعطیل خواهد بود.
🔹
۱۸ تیرماه همزمان با برگزاری مراسم تشییع در مشهد، آسمان این شهر و فرودگاه هاشمی نژاد به طور کامل بسته خواهد شد.
🔹
در روزهای ۱۷ و ۱۸ تیرماه نیز پروازها در سراسر کشور به جز مشهد بدون محدودیت ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666948" target="_blank">📅 14:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کولیوند: هلال احمر با اعزام نیروهای امدادگر به عراق، مراسم تشییع در آن‌جا را نیز پوشش خواهد داد
پیرحسین کولیوند، رئیس جمعیت هلال احمر کشور در
#گفتگو
با خبرفوری:
🔹
با وجود جمعیت گسترده، مراسم تاکنون کمترین میزان مصدوم را داشته که حاصل همکاری مردم است.
🔹
همه دستگاه‌ها از جمله شهرداری، وزارت کشور و سایر نهادها همکاری کاملی داشته‌اند و هیچ گونه محدودیت یا کمبود امکاناتی برای حضور مردم وجود ندارد.
🔹
هلال‌احمر با اعزام نیروهای امدادگر به عراق و هماهنگی با هلال‌احمر عراق، وزارت بهداشت و حشد الشعبی، مراسم تشییع در عراق را نیز پوشش خواهد داد و تدابیر لازم برای قم و مشهد نیز اتخاذ شده است.
🔹
۶ میلیون داوطلب هلال احمر برای حضور در مراسم اعلام آمادگی کرده‌اند و از همه مردم دعوت می‌کنم فردا با حضور خود، قدردانی از زحمات رهبر شهید را به نمایش بگذارند‌ تا حسرتی برای کسی باقی نماند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666947" target="_blank">📅 14:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3d5f474f7.mp4?token=UMGTeUNCT20osQ1Jh6zsA6FQ4L5UOPI39gOoIpleXHUigSuWim4A1mSl1YFWHZFsmuk6A7ftbMNCuxrCEe9PNOU_DfluGl-NBrTLq4YpZ6Sluc24-dgHDIEk4l2oPNdMIF8cD3U2HfU667dvCrmlL0Ta-tPn7Q-BGh1ujgpDQSLBv7KDt-q2AiKx3JnoYmF0YawTc2bfqxZTYozzsas0_hZJKNSaJ8BhmAFEoGWWvUKXOWiFvqoFHNZQDliFgOmQIZMPZu667iKCMgZkzkAAPxXuyJtDcoHnNtQoC3NGwKzg1hJCrg0_gkX3Rd7BGr9x0Rw-uju0RQ-PXxAWi96Oew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3d5f474f7.mp4?token=UMGTeUNCT20osQ1Jh6zsA6FQ4L5UOPI39gOoIpleXHUigSuWim4A1mSl1YFWHZFsmuk6A7ftbMNCuxrCEe9PNOU_DfluGl-NBrTLq4YpZ6Sluc24-dgHDIEk4l2oPNdMIF8cD3U2HfU667dvCrmlL0Ta-tPn7Q-BGh1ujgpDQSLBv7KDt-q2AiKx3JnoYmF0YawTc2bfqxZTYozzsas0_hZJKNSaJ8BhmAFEoGWWvUKXOWiFvqoFHNZQDliFgOmQIZMPZu667iKCMgZkzkAAPxXuyJtDcoHnNtQoC3NGwKzg1hJCrg0_gkX3Rd7BGr9x0Rw-uju0RQ-PXxAWi96Oew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام قرائتی: خداوند به ما توفیق دهد مثل رهبر شهید آماده باش و با ایمان باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666946" target="_blank">📅 14:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666945">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsBatCTh8lD6S2RbSpXVNFaoQQ6DQjC0wcYkeLGjTimgRgIODXTZ83aw-s--dIekjqeSx0I4HeIUFbvfwKeIWTmAHwL9lqjLBUTUedYUV9wd44g8QtRlpDykgzD_Q_YcHjN3RU_l-sgJ3YGgKKSkAL_281ni8U3NCH1i9TmH6srWT8uwEtOtuFHrd1GE1DK6Vq0bJo53P73DkxFTcw9vqKqWNsmdOxgUG7SHEoUnQulmvbUGky79q1zYeVflVLD-1sg0jaVT1JMaif-H1Mo_z-OwOCzqyiz-7ZKkpKu3etqEn54_rUe4O7LCj58bz3jAjX8yqKCbAIKwlqSuqSC2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواهید دید چه خواهد شد...
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666945" target="_blank">📅 14:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c97ee6575.mp4?token=hGm5v2vx_mT4YuoTi7-FwZzOZM5UXrFhECE1Gz_ZS1FkfEDEX3jNdCWOBfng6Oh_SJcmx7BzsrIP6kCGSpOig5j5gmn_PcaHE9TWI6098k2jG0fAL23FKbfJLfjpXSDrR0sF8egq5cxbdNb9pwR92KkKFf_zCywNCrLXPbnaci9FgeGDexhbdzTycPRnzB3QS7QgmnWbsa-7g1mlSDIdKY1pChtGnCq8X14wJR_InxIx09644j5-dMp33rwCqgJK3L4Y21-gW3t2aVwI5xDYnlison0telnNhP4JVB7ht1Zd2I8E68p60K7ocgLaVDjwHcOrRbZ04kbHflhzMRz77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c97ee6575.mp4?token=hGm5v2vx_mT4YuoTi7-FwZzOZM5UXrFhECE1Gz_ZS1FkfEDEX3jNdCWOBfng6Oh_SJcmx7BzsrIP6kCGSpOig5j5gmn_PcaHE9TWI6098k2jG0fAL23FKbfJLfjpXSDrR0sF8egq5cxbdNb9pwR92KkKFf_zCywNCrLXPbnaci9FgeGDexhbdzTycPRnzB3QS7QgmnWbsa-7g1mlSDIdKY1pChtGnCq8X14wJR_InxIx09644j5-dMp33rwCqgJK3L4Y21-gW3t2aVwI5xDYnlison0telnNhP4JVB7ht1Zd2I8E68p60K7ocgLaVDjwHcOrRbZ04kbHflhzMRz77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار قاآنی: شهادت رهبری نشان می‎‌دهد که ما باید چه مسیری را برویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666944" target="_blank">📅 14:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666943">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34e15eb8a.mp4?token=s9qJcAgPgYOcb0WxA1Q1JFmLFiIiVNct5kVZe2dJVOtXAH-1dv9HlahK5__al5AnbbimzTU5gjTbTa5iusK1SYA4wGqY-nSaIIDQ8oA89omdm4oW4WZd14LyiBamK2UkuLyZmp9GhXQs9ncBB_uZYM6DeFaDgEC-hk76t96aBgkFsSPIfrXF4WAtJF8437CR8Ugc4p41bnEAmsGK-n1N2v0JBYbX3rZWJczLYyF_4Q288YmGUpVmTLCHThzQ0OmXPV2Knm-8szndR6Kq_0boJ0L1f6fh2E-wys9uKvtDWmfGTXr2pa4w-qbeRiDkA4i7f5XMYs5oREWh7CsyOu35fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34e15eb8a.mp4?token=s9qJcAgPgYOcb0WxA1Q1JFmLFiIiVNct5kVZe2dJVOtXAH-1dv9HlahK5__al5AnbbimzTU5gjTbTa5iusK1SYA4wGqY-nSaIIDQ8oA89omdm4oW4WZd14LyiBamK2UkuLyZmp9GhXQs9ncBB_uZYM6DeFaDgEC-hk76t96aBgkFsSPIfrXF4WAtJF8437CR8Ugc4p41bnEAmsGK-n1N2v0JBYbX3rZWJczLYyF_4Q288YmGUpVmTLCHThzQ0OmXPV2Knm-8szndR6Kq_0boJ0L1f6fh2E-wys9uKvtDWmfGTXr2pa4w-qbeRiDkA4i7f5XMYs5oREWh7CsyOu35fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمد مخبر: قاتلین امام شهید به مرگ طبیعی نخواهند مُرد و نظام انتقام خواهد گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666943" target="_blank">📅 14:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666942">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7985e8023.mp4?token=sV79dPnd4jmpf7YEzQBmZM2756NTpJnZukqJz3V89dcr4ujHqbbQypaNOETk9Ilo5bba9gud32vaZaByWy3hFt2N15UHxNGerYkINOPB-WZECix0pumZb1-9IP5sH6vEz2K-_qiV1nyOOjc-rraFhuGQeqi2Pxy3h2mPnv_OQnMgR7ysIIk8WejAFZGScb0J-U8bItjHyBNPlR97RCKcqTz7KNKMmlQ2QWKDzQIdyDHlYRBgFYUjFl2JdHONCEMvafGlheZFKg2MWoUEUn6WVNaCIysHCP8cvDZoifWxZJfNAq2y795uoXBcttrdEOYztPRocyrSHdASlwf5woUNlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7985e8023.mp4?token=sV79dPnd4jmpf7YEzQBmZM2756NTpJnZukqJz3V89dcr4ujHqbbQypaNOETk9Ilo5bba9gud32vaZaByWy3hFt2N15UHxNGerYkINOPB-WZECix0pumZb1-9IP5sH6vEz2K-_qiV1nyOOjc-rraFhuGQeqi2Pxy3h2mPnv_OQnMgR7ysIIk8WejAFZGScb0J-U8bItjHyBNPlR97RCKcqTz7KNKMmlQ2QWKDzQIdyDHlYRBgFYUjFl2JdHONCEMvafGlheZFKg2MWoUEUn6WVNaCIysHCP8cvDZoifWxZJfNAq2y795uoXBcttrdEOYztPRocyrSHdASlwf5woUNlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار رادان، فرمانده کل نیروی انتظامی: برای ما سخت‌ترین روزهاست/ امیدواریم این وداع توام با سلام باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666942" target="_blank">📅 14:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666941">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6562a415.mp4?token=JGQKjvCROT9eajJPCfap099wHQ9nxBfoO-nzttNHg9pTL1t9o5WWaojNrRaA4oJXCTDn_mb-ynuCrlyYmuRWgw_GRyzRI07CDuk0gL6kjdyrAmfJ3sG9gNqfSq_PkvYZrLRlidWBEX4PutcTB2dak3wD08J8L-rDcG6iGX1tfFZmY1yweDTqZK3eWbWwF9mfS8DexsC_AfUvcx7gXZ22vtsOd2uJ2fKeWQjQuLqhaNNKQDfYx9qhg4kfjG1D5NcW_zqNjtn_9oevaPfWilUEXbyI3DXLZJqr1w_gxYRuNf91ANM1ZA3lK0yeA64ZioAF0pyr7BeBsnxl6QaNieUMVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6562a415.mp4?token=JGQKjvCROT9eajJPCfap099wHQ9nxBfoO-nzttNHg9pTL1t9o5WWaojNrRaA4oJXCTDn_mb-ynuCrlyYmuRWgw_GRyzRI07CDuk0gL6kjdyrAmfJ3sG9gNqfSq_PkvYZrLRlidWBEX4PutcTB2dak3wD08J8L-rDcG6iGX1tfFZmY1yweDTqZK3eWbWwF9mfS8DexsC_AfUvcx7gXZ22vtsOd2uJ2fKeWQjQuLqhaNNKQDfYx9qhg4kfjG1D5NcW_zqNjtn_9oevaPfWilUEXbyI3DXLZJqr1w_gxYRuNf91ANM1ZA3lK0yeA64ZioAF0pyr7BeBsnxl6QaNieUMVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون‌اول رئیس‌جمهور: مسئولیت ما برای پیگیری فرمایشات رهبر انقلاب پس از شهادتشان بیشتر شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666941" target="_blank">📅 14:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666940">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e90c430708.mp4?token=A8tH4BAf6QVobgULYwM6PgR5rk-dIpgKg2EiJDRibm2c91IfqGXhQADdKEODSDS6xaMx2vw3tKZvKi6ja3Ux8jQtRUMwCaxW4DAO2RxYSp8eS6NNNGpVSkYNQzr4i7jsg5M1Z1K0pjcCb4vYIdkNMBrcxVYjDMK2wYI-ExJ2IQLicxeVZbTCDnau3SBd5J25ALE3AzeKDJ6pWDeNxxTNyIViKxJ_tt6hRadozvAEG3Z3iCRWr1zkMJF8tdyrRYqNwr9lcr5hq_qs6RNdKAvNcQMlLJrZXOSAQevo8v9QBlYUsTasc2Akj_sD7TnxRCrzCR9kYM4LCM3waHZAkGHhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e90c430708.mp4?token=A8tH4BAf6QVobgULYwM6PgR5rk-dIpgKg2EiJDRibm2c91IfqGXhQADdKEODSDS6xaMx2vw3tKZvKi6ja3Ux8jQtRUMwCaxW4DAO2RxYSp8eS6NNNGpVSkYNQzr4i7jsg5M1Z1K0pjcCb4vYIdkNMBrcxVYjDMK2wYI-ExJ2IQLicxeVZbTCDnau3SBd5J25ALE3AzeKDJ6pWDeNxxTNyIViKxJ_tt6hRadozvAEG3Z3iCRWr1zkMJF8tdyrRYqNwr9lcr5hq_qs6RNdKAvNcQMlLJrZXOSAQevo8v9QBlYUsTasc2Akj_sD7TnxRCrzCR9kYM4LCM3waHZAkGHhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروش مردم انقلابی در متروی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666940" target="_blank">📅 14:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666939">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe1MThZ7jh5hxvhuLtiaTu4LoRguQ2e4W9uexgiCCi8hgMnmfTCzdVCUbrG72BRTh6DDy7MrMsSRZlgzFMWqBXNaWIvtSHAtNXMQPcKrDS-W8hbQHAstP8omignYxwOsmZlb5ggmTcFWH1OU009bGMy-67iPqvtJglctex_iZBylpn3ZUlT3go_PTcfZdpq0YqcM7g3nZXNOTfGcJKsuMMjSw0rf8jJNk5C_pcFB9td3jbrx0sJgwlOhM9Ede7gfGAkJB3wxMIFyFQFTWyMgMXkE_gVjV3_Nzt6HpdaxCv1uFHnB_M_joeMS7Ej2f6gsTEV-26OrhcYGVuxGZbnQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پابرهنه، روی زمین داغ؛ آخرین بدرقه یک برادر...
🔹
تصویری از برادرِ شهید مصباح‌الهدی باقری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666939" target="_blank">📅 14:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666938">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f432b1b38a.mp4?token=dhEQ9DHjQyxv2c2pLKBZeAO8nXetgQd1fLxfuI0tKnCtk3BxyQIZahwNmHuR23rNubXD8bTdkawawFPfpqkxxAWmB_tZjB-ZTQzclV5rwCxojjtHxifrmbwsr49gKqvFzp8BBS4mojRb4rnwPQ4KsuzQeTnTN4YAAY0Qs689DwHpI3x_yzAgcaHkkgHoIn_nUMl8CTaCk2IrijRA73n3A5j5XjRSGEbaPsX3Wl-aZgolpOzpK37Zh1S9ZPbj0StOdYGEJM6hEYnc3AQMyE1gi-NNFp2ewDgjOoOjy8BXiB2ZJ9R_T52ujLRgJCW6pr85zPVpxqGelUxfXWU78_4itqFg-ot5CENgjgN1YW4tdJGREmY3Z7dbZRpbTtUYB27BPGXAQIKdskxq7B6UWSUBSSU7u2ONbW15gvm-lfy09YRuu_IPm0BvdbHJXMPU_SWTu9954wwj2DrYfz1WZXCgRYEICKeDLN3jpkXOgQZ8UOjV-C9NWi9aEMjp7Xqe8QH8ISS5tLQH7Q6yhnWaA4-0fPxlh6CVc69tFWgb1WrTUbME3YirA1-Or359aACY-yKz50ti7FjMOK26mw4ICIeLmgJ3UvNbE6NUNfz5cA2Mw3ambNPE80AR-7xKtkIRWSEYp8FmiNQcK_Ina5B4ryZm_Z0IAuNqcd3oxrbMImktSyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f432b1b38a.mp4?token=dhEQ9DHjQyxv2c2pLKBZeAO8nXetgQd1fLxfuI0tKnCtk3BxyQIZahwNmHuR23rNubXD8bTdkawawFPfpqkxxAWmB_tZjB-ZTQzclV5rwCxojjtHxifrmbwsr49gKqvFzp8BBS4mojRb4rnwPQ4KsuzQeTnTN4YAAY0Qs689DwHpI3x_yzAgcaHkkgHoIn_nUMl8CTaCk2IrijRA73n3A5j5XjRSGEbaPsX3Wl-aZgolpOzpK37Zh1S9ZPbj0StOdYGEJM6hEYnc3AQMyE1gi-NNFp2ewDgjOoOjy8BXiB2ZJ9R_T52ujLRgJCW6pr85zPVpxqGelUxfXWU78_4itqFg-ot5CENgjgN1YW4tdJGREmY3Z7dbZRpbTtUYB27BPGXAQIKdskxq7B6UWSUBSSU7u2ONbW15gvm-lfy09YRuu_IPm0BvdbHJXMPU_SWTu9954wwj2DrYfz1WZXCgRYEICKeDLN3jpkXOgQZ8UOjV-C9NWi9aEMjp7Xqe8QH8ISS5tLQH7Q6yhnWaA4-0fPxlh6CVc69tFWgb1WrTUbME3YirA1-Or359aACY-yKz50ti7FjMOK26mw4ICIeLmgJ3UvNbE6NUNfz5cA2Mw3ambNPE80AR-7xKtkIRWSEYp8FmiNQcK_Ina5B4ryZm_Z0IAuNqcd3oxrbMImktSyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردرگمی غرب در برابر حماسه ملی ایران؛ جنوب جهانی تمام قد ایستاد
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/666938" target="_blank">📅 14:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/354e7251e1.mp4?token=s5YY_OjURb16ht6aJBU19cVv6feGWFNeIce8TT3kcmmHYhBeLo1O_2C5H6iGYf6XtPJBM4xiBnYRD8PLarCCcrYTtWKCr59dQBGWbnXQImJCFSuT9D92yGPVlttUQyLyHGwxyupY4q_3AssJHqk_xZQna-ijntnMFU1vKmarhWS24kPNAfsNlrAwZgLO6SXCjs5j_2tsyy02d3mZueW2wSFTTYDihwAVQLiFZOG1IZmK9dte2yybMV8kg7d2lAG3-hSBZNeM2mjXkVeDrjCXItKUvNRvfTF9AWasmcZiBezsELPSorYD90vnJV2LVWP5woW4TJotaSxEeT5cZqfQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/354e7251e1.mp4?token=s5YY_OjURb16ht6aJBU19cVv6feGWFNeIce8TT3kcmmHYhBeLo1O_2C5H6iGYf6XtPJBM4xiBnYRD8PLarCCcrYTtWKCr59dQBGWbnXQImJCFSuT9D92yGPVlttUQyLyHGwxyupY4q_3AssJHqk_xZQna-ijntnMFU1vKmarhWS24kPNAfsNlrAwZgLO6SXCjs5j_2tsyy02d3mZueW2wSFTTYDihwAVQLiFZOG1IZmK9dte2yybMV8kg7d2lAG3-hSBZNeM2mjXkVeDrjCXItKUvNRvfTF9AWasmcZiBezsELPSorYD90vnJV2LVWP5woW4TJotaSxEeT5cZqfQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیرحاتمی فرمانده ارتش: یقه کسانی که رهبر ما را شهید کردند، رها نخواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666937" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efH5E6tWRXsnpE1UM6AJTSNQSBdrLRF0redSbGoWdq3eZnbZK0Hm56HJ7X26MXLjdmd2TkEYERVGXUMeemyvvkNTuG3C_trF9hfJoU-_gXKuuQywEeOUG65SWw88ioxiLvBtDKrS5j3xaoI9Lc6dkSow839nqntFxYYRFeBlh5bT03G1F7CgBcLbZBSu07Qjp_jCCRvsplvmg1ltBxW5nrpCxuO6mEe39QV-aeHH__DDngzGzkHrHzQN8pc-MJGGeiUvmY1OrhE0XGSsWn8LzZ5czFRVxMBST4zTDnDNnE9ZfDn0aHNAwj8nuBdZJD6Kl38ycTPIP1fCmI8uDBct5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از پزشکیان و فرزند رهبر شهید انقلاب در مصلی تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666936" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
احتمال شنیده‌شدن صدای انفجارهای شدید در بندرعباس
استانداری هرمزگان:
🔹
امروز یکشنبه انفجارهای کنترل شده و شدیدی در شهر بندرعباس انجام خواهد شد که ممکن است صدای برخی انفجارها شدید باشد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666935" target="_blank">📅 14:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lhoz0DhIyQznLsXsgDG0lpNwu3rol_sWihHMGckbeslAoad8VIrDns0ZOTWa-XqTrmtU5suDVm-VIQPfXJECAoqXJX2zwbKxNbYi27Uw_qp1CO0PwBDiv1SFDGtKQM_zd7xNwlekYqlgHwYaikCu6wXh-wyMH8RvwEbA2i5nhTawYdn4-slcTGQ16_8wOk_A3dA1wZ4n6pCRMgcqGK1zDbiCjYQRrVFbhJHhLqujn0lxuUx3sljVXelI-jg2L6yNCcqdQNyFbAZFW-h3ITl3-8J5fXW2fijNrSDAqJkTAeQdwn03cZaavDCbONnxeCgu-p8UJBe4cqMPdC0yG6tQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از قالیباف در کنار فرزند رهبر شهید انقلاب در مصلی تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666934" target="_blank">📅 14:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f252fd36.mp4?token=BafxhV6QrpkKs1X5eUk6FLukp6vuV8eVVFOb-QqsWhrkblq74NQ7hIzNnZZCzditiyIXaHSzGYDkosxaRL-f_LarRsMDhE4FIWmZqrQwP3xeQyEpmDHd1vl5TQmMDne-tQnQdO-pIc_VyMpBfmEd-voW3SQTX8FgtRuWxUZkQp629UrXHkqQM4c9QsgwhbYZffr_9C-X_ZE2iSKvnRrXJvfmTKdalzKJi5c_1FSkcMOh2PI9cTW-XMRj_qreWRZuB1vv1d1V9WX-fmLI6jIFBa9fv5E8HJXdQFoxEA_9jD8W1hLf1jogCMwpMavPXCMd4OL9nBsXPK6MPMChft_aHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f252fd36.mp4?token=BafxhV6QrpkKs1X5eUk6FLukp6vuV8eVVFOb-QqsWhrkblq74NQ7hIzNnZZCzditiyIXaHSzGYDkosxaRL-f_LarRsMDhE4FIWmZqrQwP3xeQyEpmDHd1vl5TQmMDne-tQnQdO-pIc_VyMpBfmEd-voW3SQTX8FgtRuWxUZkQp629UrXHkqQM4c9QsgwhbYZffr_9C-X_ZE2iSKvnRrXJvfmTKdalzKJi5c_1FSkcMOh2PI9cTW-XMRj_qreWRZuB1vv1d1V9WX-fmLI6jIFBa9fv5E8HJXdQFoxEA_9jD8W1hLf1jogCMwpMavPXCMd4OL9nBsXPK6MPMChft_aHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسنی اژه‌ای: رهبر شهید ما بعد از این همه زحمت و رنجی که در راه هدایت مردم و انقلاب کشیدند نباید اجری به جز شهادت نصیبشان می‌شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666933" target="_blank">📅 14:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهشتم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای محسن حسن‌وند که شکارچی قهار بودند و به هیچگونه حیوانی رحم نمی‌کردند در سانحه تصادف به کما رفته و حقایقی برای ایشان در عالم برزخ پدیدار می‌شود و تنها از میان ۴ نفر در حادثه، جان سالم به در می‌برد و به زندگی باز می‌گردد و تغییرات محسوسی در زندگی و رفتار خود ایجاد می‌کند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: محسن حسن‌وند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666932" target="_blank">📅 14:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUqJQ7Ncs1H0YtBK1xvFo0npJ1wcGDL3CNLil9hXOj_T1f0Lk2TlGqXEptFTYf0DXvnJkkVu3w2EshWO8cdxFD8QI6JFAA8CgkWCNvCbm3xh92sFy7RaeRQkX7OMFEs2W4l591RE6JYkoS_52NufZ6TBQBupXi3AxoQe4U26LG6YUzl17N4hlU_al9CwLg7Xm4ARWRaxmNr1rDhELfa2vHiv2JdqRi8arvmCsL7OrhaMYQR-7vD-XKLJLHfJrSJji2USpdVKfS2BrA8FuM33dzbLO6PDIh5ox2uh_qBlUi0Vk8yuZvdHcgQ2g5vHItD1fCFDDi40vb51Ub3oD8gr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از شهید دکتر مصباح‌الهدی باقری در کنار رهبر شهید انقلاب اسلامی در حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666931" target="_blank">📅 14:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXCbwV_GF-bIjDIGJIKeFP9HGlKGGJaoiBBF-M6Uu-C7L1gXIjibpptU3wPV9O5qyQYWIayUPrtqTA_6TjytLq5eaTS1bCAmzDi8keZWyLbruVCf0ZNACtEzpmVVKR_Vgu2eQ1lUKJZoGYPBtQycs_Gv6rYnJTQsv6e1yaKNOXv8VWYKUIKgtOLH1iw6k9txGyP9U8UvV4jUiHTaNDM4FchzaFaN2gaVxeiyjYnrYrQTEbERQAB2Lmp2vq2kIfHq7J5HANqPsj218_-qX8-Ezr2_EfBDoBCfx4YvK4NjwtuZU-LFDqlMWl8BDLQ4wLilEiPjagVQtqWk8eWej4BNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منطقه بندی مشهدالرضا در میزبانی از زائران و خونخواهان آقای شهید ایران
منطقه ۱      فارس  و اصفهان
منطقه ۲     تهران ،قم وخراسان شمالی
منطقه ۳    لرستان ،کردستان وچهارمحال بختیاری
منطقه ۴     کرمان ویزد
منطقه ۵    هرمزگان وبوشهر
منطقه ۶     خراسان جنوبی وسیستان بلوچستان
منطقه ۷   کرمانشاه ،ایلام وخوزستان
منطقه ۸    زنجان وهمدان
منطقه ۹     آذربایجان غربی وآذربایجان شرقی
منطقه ۱۰    اردبیل وقزوین
منطقه۱۱      گلستان وسمنان
منطقه ۱۲   گیلان ومازندران
شماره تماس راهنما: 5151-051
لینک ثبت نام:
bayadbarkhast.ir
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666930" target="_blank">📅 13:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6405b893a6.mp4?token=JMR_c0FEo-z7HF6zwDpng4BMsXVLHbfJ-_8ouyS-cvsZ-Fq1_FMQv-PLEHWz45Yd5LCvDAT7MB1uq14Yf_A2bzPSOg_5m7e4HNUot4OOinBDW3Me-GqImhl7hpozughq1ONHbA8bYoVpSQh4L5L1VRFBuaKk3l9o651rikxsjKHhGLPENWtjnrYVr9QBuHT9nuLMi4UydUQptC5y5k7kDk1bO54bTmgjWtWPrABqypRCI_WyetgMPXKGhfzXR6a-GZmhc8EBO1CD1TCKXuOvLLZrl-lM0prQ3htRs-HVafL_AP-QbKtT5d6R9miumZqm4LO1iOzgdzPwRc7ksFqGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6405b893a6.mp4?token=JMR_c0FEo-z7HF6zwDpng4BMsXVLHbfJ-_8ouyS-cvsZ-Fq1_FMQv-PLEHWz45Yd5LCvDAT7MB1uq14Yf_A2bzPSOg_5m7e4HNUot4OOinBDW3Me-GqImhl7hpozughq1ONHbA8bYoVpSQh4L5L1VRFBuaKk3l9o651rikxsjKHhGLPENWtjnrYVr9QBuHT9nuLMi4UydUQptC5y5k7kDk1bO54bTmgjWtWPrABqypRCI_WyetgMPXKGhfzXR6a-GZmhc8EBO1CD1TCKXuOvLLZrl-lM0prQ3htRs-HVafL_AP-QbKtT5d6R9miumZqm4LO1iOzgdzPwRc7ksFqGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: قول می‌دهم راه امام شهید را ادامه دهم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666929" target="_blank">📅 13:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXIw129mXjT8PuQG__NOxP9v5S0AmsclnP65JLKkmIaSxXtviE88dXH5_1Pb_cGfdZrNYgIFWY-O90rtVRuuE8X2edrApbFei6ymBs0qfGOEwPbZ4_wFMuz6pKbm4c3MBR2WC0JNPUggbO4lCtrWRAXsh3W50M2mDCZb2WqbO52uV_mTxJanXewIaeIEykujCVrr_-3QscrtI2U3Bid9DiI5g85zKTuQ9ONsshp1LctPUZuqw58rjKdx0arR74zXzRZTkLs05Fy0Z6bUkr3xb6hwPSQWMbldicu4Nk6Ixpseqk6qLkXZUuQqXneZRepl1Xs4N1HYs4g4LIL8xEIawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ملت شکست‌ناپذیر ایران امروز یکپارچه فریاد یا لَثاراتِ‌الحسین(ع) سر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666928" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666927">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شتاب تورم ماهانه کاهش یافت
🔹
با انتشار آمارهای جدید، تصویر تورم در پایان بهار شفاف‌تر شد. هرچند شتاب تورم ماهانه نسبت به اردیبهشت اندکی کاهش یافته، اما روند افزایش قیمت‌ها همچنان نگران‌کننده است.
🔹
تورم ماهانه خرداد به ۵.۹ درصد رسید و تورم نقطه‌به‌نقطه نیز با ثبت ۸۸.۶ درصد عدد جدیدی را ثبت کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666927" target="_blank">📅 13:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666926">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb3d9b321.mp4?token=SUR_WVBCc6G9ulQzer59D4j5BX_io3DWxjUYqpBykdq7qz75RzXWpQsz8QYJOzxdHp3Y4pCRCdkf0ooK7TrzG3350SyrXSC6M3_2M-G8kMlbSIU9MPN75PrGFNPyDDdkkobPESJx8FErbZWuDxu3c2cS5CInnAhYRK_2dQ1Q2RVKmlCgH4WCihiIVQPZ8zIWskiXp3BPya4Xtl4y3BJMhSOMN1pkUaUzDUike4OqVvTniKLFQr9DEiv8ZeZW8aKLQls7Na3itYB18ixBUdKdZJGjHCuLk_TQ2Ro6SdWborrHb_fVTWQe9Jla2jw18JxOU5SXV4Y7DevNM4L3rBxTxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb3d9b321.mp4?token=SUR_WVBCc6G9ulQzer59D4j5BX_io3DWxjUYqpBykdq7qz75RzXWpQsz8QYJOzxdHp3Y4pCRCdkf0ooK7TrzG3350SyrXSC6M3_2M-G8kMlbSIU9MPN75PrGFNPyDDdkkobPESJx8FErbZWuDxu3c2cS5CInnAhYRK_2dQ1Q2RVKmlCgH4WCihiIVQPZ8zIWskiXp3BPya4Xtl4y3BJMhSOMN1pkUaUzDUike4OqVvTniKLFQr9DEiv8ZeZW8aKLQls7Na3itYB18ixBUdKdZJGjHCuLk_TQ2Ro6SdWborrHb_fVTWQe9Jla2jw18JxOU5SXV4Y7DevNM4L3rBxTxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش موشک بالستیک ضد کشتی از سوی ترکیه
🔹
تایفون، اولین موشک بالستیک کوتاه برد ترکیه است که پیش از این در آزمایش‌های خود با اهداف زمینی را در بردهای بیش از ۵۰۰ کیلومتر هدف قرار داده بود. این موشک با سر جستجوگر نسل جدید یکپارچه، فناوری‌ سوخت جامد و انواع برد افزایش یافته (بلاک ۱، بلوک ۲، بلوک ۳، بلوک ۴) است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666926" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666925">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسِدخارجی</strong></div>
<div class="tg-text">سلام به همگی؛
خیلی از ما این روزها و روزهای آینده، بخشی از یک واقعه بزرگ تاریخی خواهیم بود.  قاب‌ها، تکاپوها، بغض‌ها و تصاویری که هر کدام از شما با چشم خودتان می‌بینید یا با تلفن‌های همراه‌تان ثبت می‌کنید، تکه‌هایی از یک حقیقت بزرگ هستند که نباید گم شوند.
🖤
«
به همین خاطر، برای ساخت یک مستند بزرگ و مردمی، به همکاری شما نیاز دارم.
»
از هر قشر، با هر نگاه و از هر کجای دنیا که هستید، می‌خواهم داستان و روایت خودتان را برای من بفرستید تا در کنار هم این تاریخ را ثبت کنیم. اگر خادم هستید، اگر میزبان، میهمان، مسافر و زائر هستید یا حتی اگر از نیروهای تامین امنیت مراسمید...  هدف من ثبت یک سند ماندگار، واقعی و کاملاً بر پایه تاریخ است؛ نه صرفاً یک کلیپ.
📸
چه تصاویری برای من بفرستید؟ هرچیزی که فکر میکنید!
🔻
اگر خواستید جلوی دوربین بیایید، اگر خواستید حرف بزنید، داستانتان را بگویید و از حس‌وحالتان در این روزها صحبت کنید.
🔻
فضای اطراف خودتان را نشان دهید؛ شلوغی‌ها، موکب‌ها و حضور اقشار مختلف (نوجوان و افراد مسن، پاکبانان عزیز، نیروهای هلال‌احمر، آتش‌نشان‌ها، پلیس، سربازها، زائران و مسافرانی که از راه‌های دور آمده‌اند). حتی اگر دوست داشتید باهاشون مصاحبه بگیرید.
🔻
تلاش و زحمات دیگران، دلداری دادن‌های مردم به یکدیگر و هر صحنه متفاوتی که توجه‌تان را جلب کرده است.
🔻
اگر به هر دلیلی امکان حضور در مراسم را ندارید، از حس‌وحال خودتان در همان جایی که هستید ویدیو بگیرید و برایم روایت کنید.
🔻
حتی اگر فیلمی رو از روزهای گذشته و برنامه‌های مرتبط قبلی هم در گوشی یا دوربینتان دارید، بفرستید. مثل راه اندازی موکبتون، خاطراتتون در مسیر رسیدن به مراسم‌های وداع و تشییع (تهران، قم، عراق و مشهد) و...
🔻
گاهی پشت‌صحنه‌ها و حاشیه‌ها از اصل جذاب‌تر می‌شوند.
✨
نکات فنی مهم (که خواهش می‌کنم حتماً رعایت کنید):
برای اینکه ویدیوهای شما قابلیت استفاده در مستند را داشته باشند، خواهش می‌کنم به این چند شرط دقت کنید:
🔻
حتماً افقی فیلم‌برداری کنید (گوشی را به پهلو بچرخانید).
🔻
فقط ویديو بفرستید. عکس، صوت و متن لازم نیست.
🔻
ویدیوها باید کاملاً خام باشند؛ لطفاً هیچ‌گونه موسیقی، افکت یا واترمرکی روی فیلم‌ها نگذارید. من فیلم‌ها را با صدای محیطیِ خودشان نیاز دارم.
🔻
فیلم‌ها را با بالاترین کیفیتی که دستگاهتان ضبط می‌کند ارسال کنید.
🔻
در ابتدا یا انتهای ویدیو، یا در متن ارسالی، ترجیحاً ساعت، تاریخ و مکان ضبط ویدیو را بگویید.
🔻
لطفاً ویدیوهایی که در کانال‌های خبری و فضای مجازی پخش شده و خودتون اونا رو ضبط نکردید رو برام نفرستید؛ من دنبال روایت شخصی و قاب‌های اختصاصیِ خودِ شما هستم.
✨
نکات تکمیلی:
🔻
برای من سوژه، نگاه و داستان واقعی شما بسیار ارزشمندتر از حرفه‌ای بودن تجهیزات است.
🔻
با هر دوربین یا موبایلی که دست‌تان است، قاب‌هایتان را ثبت کنید و برایم بفرستید.
🔻
برای به سرانجام رسیدن این پروژه، همت همه‌ی ما لازمه. خواهش می‌کنم خودتون پای کار بیایید، روایت‌هاتون رو بفرستید و حتماً دیگران رو هم از این فراخوان باخبر کنید تا این قاب تاریخی کامل‌تر بشه.
🔻
لازم به ذکره که ارسال فیلم‌ها به راه‌های ارتباطی زیر، به من اجازه میده از این ویدیوها در ساخت مستند استفاده کنم و به معنی اعلام رضایت شما برای انتشار این قاب‌های ماندگاره.
✉️
راه‌های ارسال ویدئوها:
لطفاً فایل‌های خودتان را فقط و فقط از طریق مسیرهای زیر برای من ارسال کنید و همچنین در کنار ارسال ویدئوها، مشخصات خودتون (اسم و شماره تماس) رو هم برایم بفرستید.
سایت برای آپلود:
https://upload.sedkhareji.ir
ایمیل:
Contact@sedkhareji.ir
تلگرام:
T.ME/SEDKHAREJIPM
اگر باز موردی یا سوالی بود بهم در
@SEDKHAREJIPM
پیام بدید
خاکم؛ سدخارجی
✔️</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666925" target="_blank">📅 13:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNXe4zE0O2qrD_DiKPRmPR6kiNSwzWAeqybVN7XPTdHQ0MGoXOUwXGaUwfgpmLY3apuyh1xmXbOJZbV_g0f_SD74zxJH3x7G42ZFQWVly16bFdvmin80ZPwFhujbOTExGHH1LU5kyWXjuH9CJjy1sntxgTffWbm6yT2mEaIES9u_IzK8T3u9rrrV5ahGPrvF0kRKnTzH5oFv-Dh-8FIbL6LQz6lxcaCaezva1gi6RfFcz1I_Kzf7Y7s3ODmVPmxBFa3-Izq0n5Utc9oFjUAtcuABltK6BJTKDIhh30RncLwl3cOgle9TMEwLri75fpu_DIoZ8myhwFOdYzjuw9dDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/akhbarefori/666923" target="_blank">📅 13:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkNqVPFy9gBKAEPsNWFq9Lb4qYT-1BE1HkcxCeqJkCs0n1Cir5RjMwCtjJEHUaLmJwoVzPZgeNntCYP9fF9EF7zhXo-wHnNYMQeTE9bllnfVE5LZbbmPviNw_dhO7zVg5e6Yj-G-sK0lL4c5zvVCdJ0xBwRCQ7B3qAwHlzU1FF0TklXInpjN5R7bJBFxv6JaTFQu3qXfG_WcZtc8jb9p_bCxIGkkqf1vncyTJZK9mYWjigLVC7Qgg8xHWdvTihyYYSd-Rp_PQkUXnQxo9IqjTm8lRaq3GgoueGxNQaSIriA2IY3RZDJBGnTy_AmJQ_Be176GZ8_7FHkM4QuXhz6xKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذوالقدر؛ دبیر شورای عالی امنیت ملی خطاب به دشمنان ایران:
این چند روز چشم‌تان را به ایران بدوزید
این همان ایرانی است که خیال می‌کردید چند روزه می‌توانید آن‌ را از پا درآورید!
این دریای خروشان جمعیت، حالا در وداع و تشییع رهبرشان دو شعار را فریاد می‌زنند:
مقاومت در برابر دشمنان و انتقام خون رهبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666922" target="_blank">📅 13:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
قول رئیس‌جمهور عراق به ایران؛ نمی‌گذاریم گروه‌های مخالف ایران در عراق باشند
🔹
رئیس‌جمهور عراق، روز شنبه اعلام کرد که بغداد در حال اجرای توافقنامه امنیتی خود با ایران برای پایان دادن به حضور گروه‌های مخالف ایرانی در خاک عراق است.
🔹
نزار آمیدی در مصاحبه‌ای با شبکه الحدث گفت که عراق روابط خود با تهران را بر پایه احترام متقابل، منافع مشترک و احترام به حاکمیت ملی بنا خواهد کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666921" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
جمعیت خیره‌کننده در مراسم نماز بر پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666920" target="_blank">📅 13:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAl-wGQNmx2uiarrtDs-KUnhipGWqirNOgsphhAOgkpX7RH4jDI45KXp5zV5L6-17hCswIbY-sOfBMkWDwoiizDMaAU6E85Zcqye4qRCtIj1hN2gAZaSoLMHYjfh7vYvkPtsZRdPP9DrLsvR1j4Mvkel7DPZOsXd5GXc75xjDFk_mypwleO4xyF5xrXPR7wQJMkuL2cCwSwVBWZySkoTRVoTqEGttu5TiuLchcwcueZ0uL_eYwrz7wDqdA1NzLY_Z8SFiex-ky-aQRbeQht_sSBf5cYU6lmcQI3E2g_qXXC8agJyfsuCdPdmB81nbZSPQOZ_IXOKPlJ5UqImawJi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویندوارد: قایق‌های سپاه ۶ کشتی را از مسیر عمانی خارج کردند
🔹
داده‌های هوش مصنوعی شرکت دریایی ویندوارد نشان می‌دهد که از دیروز ۲ کشتی از مسیر موسوم به «کریدور عمانی» به سمت مسیر ایران تغییر مسیر داده‌اند و ۴ کشتی هم به خلیج‌فارس برگشتند.
🔹
دیروز بلومبرگ نوشته بود ۸ کشتی قصد داشتند از مسیر تحت حمایت آمریکا عبور کنند که به ناگهان تغییر مسیر دادند و تعدادی از مسیر ایران برای تردد استفاده کردند؛ خبری که تصاویر ماهواره‌ای هم آن را تایید کرد.
🔹
حالا ویندارد می‌گوید این تغییر مسیرها با حضور قایق‌های گشتی سپاه تلاقی زمانی دارد و نیروی دریایی سپاه به کشتی‌هایی که از مسیری غیر از مسیر امن ایران استفاده کنند، هشدار رادیویی می‌دهند./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666919" target="_blank">📅 13:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یورگن کلوپ سرمربی تیم ملی آلمان شد
🔹
رسانه اسرائیلی: ترامپ احتمالاً دیدار سه جانبه‌ای با نتانیاهو و عون برگزار می‌کند.
🔹
المیادین: مردم یمن امروز با تجمع در مقابل فرودگاه صنعاء، از اقدامات ایران برای شکست محاصره تقدیر کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666918" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4a7bcf2c1.mp4?token=MVIHshbvSYn6UzKADmaOE3gTUcDY8OEfV3fhjhrdeO9xwyjHWJarv6Aj6fiVq4GYPLabULYPJS3KYlqck9dSgLBFQg2DPKkm8JqH5oCQ7N4_dgBjCXRQuUUEuonmdbQp7iibfQp0_C-DxfRcd4hTETDPFqnkvw58b881L5-PbWe_0b4FcHA2750YoAoZKhsoYRXgE0dl3cPjq_fqgH-MvczZz0a7Sib9DqgzHF3WJqHzJj-Ea4MulzsMyLTw8FkZC4ifpzdMFC0Grod5IZ3AuQQM_PUEhI44mnrB9f7oGk9tgV9u2Bzx_hV1eiN81D_kKyo6KG5YnkMrxiwa7AOwNoFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4a7bcf2c1.mp4?token=MVIHshbvSYn6UzKADmaOE3gTUcDY8OEfV3fhjhrdeO9xwyjHWJarv6Aj6fiVq4GYPLabULYPJS3KYlqck9dSgLBFQg2DPKkm8JqH5oCQ7N4_dgBjCXRQuUUEuonmdbQp7iibfQp0_C-DxfRcd4hTETDPFqnkvw58b881L5-PbWe_0b4FcHA2750YoAoZKhsoYRXgE0dl3cPjq_fqgH-MvczZz0a7Sib9DqgzHF3WJqHzJj-Ea4MulzsMyLTw8FkZC4ifpzdMFC0Grod5IZ3AuQQM_PUEhI44mnrB9f7oGk9tgV9u2Bzx_hV1eiN81D_kKyo6KG5YnkMrxiwa7AOwNoFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت خودجوش و خارق‌العاده مردم هنگام پخش سرود ملی/ احترام نظامی به سمت مصلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666917" target="_blank">📅 13:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_sIhBR6RIqgK4zhRj9y9XXpRJxSl-Ueiaq6dToNOL0v7AtayymLakZbxo1NkRpxkBGQypIFIt1i-G3CsaeXLmLps7pIG9rjwvtybDl7GWb80NObeN78JglnbjXDuHj8R_fVrnwsvQ4Vuj-d09_81uXvUULzGknOivDBc2ky4-2T5xNX-eYRM6BnglRH6Pb8i9xzXb2EyOyv5W52_7S9Bvj26ysVLAyK2_o2ObpCYQZlsiKN1XN0caQA_Bc-U2T5R5S0l2o9TmcrVL_w3oH1Vrp9mSPLRGGkjZS3yKMHG2ZEyUjrtyzu2AFueSY3rS4MD-X9QJoovqtGm5bz1KTFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالان اقتصاد دیجیتال هم در مراسم تشییع رهبر شهید موکب‌دار هستند
جمعی از فعالان داوطلب اقتصاد دیجیتال، همزمان با مراسم بدرقه رهبر شهید ایران، با برپایی موکب در مسیر مراسم، آماده میزبانی از مردم و دیگر فعالان این حوزه هستند.
وعده دیدار:
میدان آزادی خیابان برادران رحمانی جنب شهرک شهید فکوری
موکب فدا
https://www.instagram.com/mokebfada?igsh=MWg5bTV1dG5nd2IyYw==</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666916" target="_blank">📅 13:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تا انتقام خون رهبر شهیدمان را نگیریم آروم نمی‌گیریم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/666915" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666914">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تلگرام از مرز یک میلیارد کاربر فعال ماهانه عبور کرد
🔹
پیام‌رسان تلگرام در تازه‌ترین آمار رسمی خود اعلام کرد شمار کاربران فعال ماهانه این پلتفرم از یک میلیارد نفر عبور کرده است. کاربران تلگرام به‌طور میانگین روزانه ۲۱ بار اپلیکیشن را باز می‌کنند و ۴۱ دقیقه در آن وقت می‌گذرانند.
🔹
تلگرام در سال ۲۰۲۴ به ۵۴۷ میلیون دلار سود رسیده و با کنار گذاشتن وی‌چت، اکنون پس از واتس‌اپ، دومین پیام‌رسان بزرگ جهان از نظر کاربران فعال است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666914" target="_blank">📅 13:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufsLgIpy2b2SQ2gypItHjs1bGkdBs48Y_EpFqLszUTYuTDRKZ1oeYHk03OHRp04wGjF9xUyrcI_b4WBntSYutZuZTVrtJPoAEcEXXdS6vkVDvJVwxWvGLTpt_VxjLDmPysIcVWP5b95w7VEj-sifHiwZkjBFriJWTYq0dg9tismsuH_2IbobVzQ4V7yc4pdjBMncSM9Ny8N4BIUS0vmNEjG5oiNDBuUp4PRShzBNmEaKOSGBRlIfnevO3dr6fe-li5ofFAs1FvEiRbgS3xiboFXA3S00pk_SXWVF0qMcEcsh-b0K2zFxLNCyssudluSR6IQ_SnHcUwgI1VFUhYcMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgacVcrZalF3Zic5kWpQdYTizRleLB1KjPG_jrnNYMZZMtetMnhbO4XxSw41k4rClotGYmi6Qftc4qzR3WNLQUnkRdX91zfZUhDCIKkvEdEbfVx3oSSM0cxpGTy2JNXAdYm0lRMM0Rusl-ldtEpJsnNiudCzupRol7stELIhFo-RpYlmcC7IEtPr4gX34UAl2Kx6Q1UVlsmpvshKybEmTIWybdQIy0qnDYcdCWGw-4ftFzPT68YKXI9BgM_Jzv4-6WuafkZiLaFFfjzOMzVwcK2Oe_QwAIQlVeU5RD_py9QOjqXksZW_x9siPIKyY1Sle1XyVPFZqrSplgZZ_lXFEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0KfPWMLmMONmt-uxWdKK0Kxn04eKh8duu47R1BmommXadwVbDfEslkAA4YD6-x7jZ3TIXpETdG93BvzRXxDpFZK4xryXrqSKqYn81rx63C0MAQYMapyF5BwwB28OXys0eaA69GUj6eHZicNgk_F-Py25AvSai96x2u8zUr8X-p1sNpbOFI16p1ZQFioRR8DMpJ6ritoa0U7MXq0tDC5QMqmk2IqiSusUAMuEF0B19Uinvdd16r3-_1Shoq-vearN_X-rALsz3nBa8w6rveWmQN48qMms0NyXL1rHI9iLGslKGjVVDmV09Diu-VXf0SB9uHeFvJnaRrc-yDJSa_Tlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازتاب وسیع وداع با رهبر شهید در رسانه‌های جهان
🔹
روزنامه «گاردین» با انتشار عکس و ویدئوهایی از مراسم وداع روز جمعه نوشت که پیش‌بینی‌ می‌شود مراسم ۶ روزۀ تشییع پیکر آیت‌الله علی خامنه‌ای میلیون‌ها نفر را در ایران گرد هم‌ آورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666911" target="_blank">📅 13:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
راهشان تا همیشه ادامه دارد...
🔹
بانوی شرکت کننده در مراسم وداع با رهبر شهید انقلاب: آنچه برای خودشان نتوانستیم انجام دهیم، برای فرزندشان، آقا سید مجتبی، انجام دهیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666910" target="_blank">📅 13:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666908">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7d6cdcd1.mp4?token=UDcaWTSFk_Q9gVNTryKnI0Ycw_92mPYEeT0Mp330F-pwLh84xfSkWbT1H-oGQ6DvYf2YdQ6VfvvoZoonbCvoYh4eKZXAhAhU-8y84RGjXLiZQI_k0_4yYBeRLg_bEl4gvIl_fcgbBmb10Z0kSdOmaPtnO4-b-ySoRV_6yJpESrtD1NHrfFeI4tlOQoFQBhSE_N1Ssv6_QWo6XmzwJzDPhTvSuuIHKg6WUVx6Dkr5i-DeEIj5VCprhMDX3GCqKXsPNzc7ZSJKsSYEH2NNUjiwKdjyai2JUK4mscSyZhQkZHgrxVkso1WmZkQ99_NWdzWWPvU0k4kQkMiYIRYn7KZsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7d6cdcd1.mp4?token=UDcaWTSFk_Q9gVNTryKnI0Ycw_92mPYEeT0Mp330F-pwLh84xfSkWbT1H-oGQ6DvYf2YdQ6VfvvoZoonbCvoYh4eKZXAhAhU-8y84RGjXLiZQI_k0_4yYBeRLg_bEl4gvIl_fcgbBmb10Z0kSdOmaPtnO4-b-ySoRV_6yJpESrtD1NHrfFeI4tlOQoFQBhSE_N1Ssv6_QWo6XmzwJzDPhTvSuuIHKg6WUVx6Dkr5i-DeEIj5VCprhMDX3GCqKXsPNzc7ZSJKsSYEH2NNUjiwKdjyai2JUK4mscSyZhQkZHgrxVkso1WmZkQ99_NWdzWWPvU0k4kQkMiYIRYn7KZsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وفاداری تا پای جان/ زائر رهبر شهید: تا آخرین قطره خونم مقتدا و خونخواه رهبر شهیدم هستم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666908" target="_blank">📅 13:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666907">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Miu8Sg8ZiChuGLOKKi7UfP7bo-H5gUCBjpl388coMVpaFNvyyq6Vi6rbH4_SI4S8DSkfx3_4V6Fv898t0Q6RH5eFKPhb1DVeHGXPc7yz_lrNsdk3o8W4B8yP-F-j56HbBY4ZF1W-uN39KmWkoGd30XBHvjMFMLmpM3PzggIQwDTMwc9TcGmzGtZQ4MTev_ZDiWgVNkb6eTOepEJnq5SK3a_jnLcQ52AwNtgOiuDnmg77sjvBRQzyA0x8wkWske5Rh4TzSUj2XaaBw0BOcUIPZzWUngrJ_ghkvWHH0a5S00cVEi0Eut5fiK-CgItER3ncZUpwfTYfL94pRH9iaCix_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون، کارشناس آمریکایی: برنامه آمریکا برای سرنگونی حکومت ایران چقدر نتیجه برعکس داده است
🔹
محتمل‌ترین نتیجه این جنگ این است که حکومتی در ایران شکل بگیرد که از قبل قوی‌تر و با حمایت بیشتر باشد و نفوذ جهانی‌اش هم به‌طور چشمگیری افزایش پیدا کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666907" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666906">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFt_ms3kd7eUaGNH1eP1eFvY27q5Hk5PGSFFpJ6KyCsjW_uuRftCf0FaxHfWjhlmQXMvfHb_Pztq5lT01QN6TmcDyUFTQJW0vDKvQit-4CfhiLN12I4j0nk_2OlTUy0ehUoFOZWgrCnQyK1AQusPPgS2GLpBwFmHWKaqP40_hjyZsThrkPcasGUcy4tsKVMLyERtQuwIjJMWrGTpACHmJ4PCFiHILGIpknVfshklai0JmET1malIBhN1BV-o5jvMhesZEyltzea4cbU_hDiAnQh8RteMNV1z8wExZ_KYdoPHqyU39wvrRwZ0H7KF9GOJLijG3QVKYE4T__bAW5EpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی دیگر از حضور فرزندان رهبر شهید برای نماز بر پیکر قائد شهید امت #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666906" target="_blank">📅 12:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666904">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تیراندازی در نیویورک در روز استقلال آمریکا؛ ۸ نفر زخمی شدند
🔹
به نقل از ای‌بی‌سی نیوز، اداره پلیس نیویورک اعلام کرد دست‌کم هشت نفر از جمله چهار کودک، شنبه شب در جزیره «کانی» نیویورک هدف اصابت گلوله قرار گرفتند.
🔹
در حال حاضر از جزئیات حادثه، وضعیت مصدومان و انگیزه این تیراندازی اطلاعاتی در دست نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666904" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666901">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
بابل عراق هم روزهای چهارشنبه و پنجشنبه را تعطیل رسمی اعلام کرد
🔹
تاریخ به قدری عجیبه که: اون شبی که صدام گفت فردا ناهارمو تهران می‌خورم؛ به خواب‌شم نمی‌دید روزی بیاد که به علت تشییع رهبر ایران، کشورشو تعطیل کنن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666901" target="_blank">📅 12:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666900">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d47a64a2.mp4?token=pz01kDo1NdtoLQ-cKkUDw8yWzpK53ZOdl_Uw3BkUpShUkagVz33CigR2XU0G9scXRg6EwNZRbbUacsivlPQpMiqFgTraWN2aE6F2zV28ZQEeOVK7A_plm2Q6BmaHf4txNCWjpmGnjPpB6d4TgwD951DHXSl-i5BJGZSfWjwG8N7TEhSW8ZYZWGYcUnRC2Y0Qef8t_qmQ0mTfOhhmD-Sp3n-rO9VyrKJ2Q4kKjZy9HPXE2p5NgvNnXPuKVoEdDboNDo8Jg7euxepOMkUliXWzCa1YZnogjbgZXQCrUgcBKipoz2IR4NzJONAmosM0CW8xjfQAIT089A0bdFz_iX8cFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d47a64a2.mp4?token=pz01kDo1NdtoLQ-cKkUDw8yWzpK53ZOdl_Uw3BkUpShUkagVz33CigR2XU0G9scXRg6EwNZRbbUacsivlPQpMiqFgTraWN2aE6F2zV28ZQEeOVK7A_plm2Q6BmaHf4txNCWjpmGnjPpB6d4TgwD951DHXSl-i5BJGZSfWjwG8N7TEhSW8ZYZWGYcUnRC2Y0Qef8t_qmQ0mTfOhhmD-Sp3n-rO9VyrKJ2Q4kKjZy9HPXE2p5NgvNnXPuKVoEdDboNDo8Jg7euxepOMkUliXWzCa1YZnogjbgZXQCrUgcBKipoz2IR4NzJONAmosM0CW8xjfQAIT089A0bdFz_iX8cFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خدانگهدار و به امید دیدار آقای شهید ایران
🔹
امروز تیر آخر را به همه ما زدند، اما ما هنوز باورمان نشده که دیگر جسمتان کنارمان نیست.
🔹
امروز همه باهم شهادت دادیم که جز خوبی از شما ندیده‌ایم، این همان جمله‌ای بود که شما سال‌ها در رسای یاران خوبتان گفته بودید و امروز هزاران نفر ایرانی برای رهبر ایران دوستشان سر دادند…
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666900" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666899">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e935df3aa8.mp4?token=iigZ7j0Clo3rL394o4NWSjGqHyULIeTgyrYY8ruqpaLoSRUOkT5Tuft_-S-Qky-GOO1HW6Jj87hgb8U_fwHSKC9UpGOwV7KS3n6Vj5xskdSpfxvR1IIMB8JptWqz2MuU6CWc3j7oBowaElYR02WAka_jU0wNXCaq0XdUtnx-voxvPpnsbERhJ9_2T06EkVhlGFhwswevdGLhekDReAhZCcw0Cn7sSIxxgI4elB9rQIBEjBlpcRqS29OMFuCVu4lBcGjyYd-8ObOlrSLbPtIDdLEYzkrGHqF4H4cRMt78C4JZKjFz1ryJU_z6QD-DKX4d3F-7omY5iYyVTNQpuhgwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e935df3aa8.mp4?token=iigZ7j0Clo3rL394o4NWSjGqHyULIeTgyrYY8ruqpaLoSRUOkT5Tuft_-S-Qky-GOO1HW6Jj87hgb8U_fwHSKC9UpGOwV7KS3n6Vj5xskdSpfxvR1IIMB8JptWqz2MuU6CWc3j7oBowaElYR02WAka_jU0wNXCaq0XdUtnx-voxvPpnsbERhJ9_2T06EkVhlGFhwswevdGLhekDReAhZCcw0Cn7sSIxxgI4elB9rQIBEjBlpcRqS29OMFuCVu4lBcGjyYd-8ObOlrSLbPtIDdLEYzkrGHqF4H4cRMt78C4JZKjFz1ryJU_z6QD-DKX4d3F-7omY5iYyVTNQpuhgwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقا حلالمون کن...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666899" target="_blank">📅 12:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666898">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUpjScpSgSscR2Ksjh6aagthIN0ghlpthC235EjyFRrmSMMrrJ_853jOlmlU0d6Xx-qllcvXoFU-5SSHkAFAH4Xwk6YdIhccM6EHUP9GN0hlIfqqqW3wmSIy_Ri9Cl16U8jstRwZcIW6HTH0ELMNpwgyuJUcS8KYAX5TOZu2dxMdKt24mVKxjLntooZX5YM6O66SZtZq4QSluFZuLwpK8_eDSm6WuEk1YxV4zCbpSQU34HBcl-nmlpPBrKGu-OcyHXzH8fwsat6wFbgaR3o-BVGyowB2HvJ-HPGqZtPqg6VBCBfbu2iifO_yIj3nNtrmy2fn5UOJB96AtpfdATy4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثۀ دریایی در نزدیکی یمن
🔹
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثه در فاصلۀ ۳۰ مایلی جنوب‌غربی الحدیده در یمن خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666898" target="_blank">📅 12:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666897">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWE7KFc14PkKYfUUA2nuIY7aEs_fi-ZmpzbEjVWmI4aZHg7pHwSeVj2f7SN3i1O5ntbwkjBiOH3Whf0SqPVqtZSvq2GggKOJZ1-xCqY1XgrXXOvvASaCbI1FN_yXoxhHTxz8WFtzw-G3PpVvDnv2ISNjXPQNGodo2oyo2vuxFc87sr9sJDs6h0IaiZzM3G1_vEaQPpPQVt-mjj54LneintLJAVYdWxx_D01Mr1d1iXxIDlvzAXMXJApizq0cRmg_aB3lBlJiC5C4HODfd8sHP0U5hcVzoyhvquiFbj4ZNw2eBZyJs0-ycxdNnufc3vvhLs9u6bo1MqfMhCezz7hvvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: تردد در مسیر عمانی تنگه هرمز شدیدا کاهش پیدا کرده است
🔹
خبرگزاری آمریکایی به نقل از «گزارش‌های دریافتی» از ترددهای دریایی اعلام کرد که میزان عبور و مرور شناورها از مسیر ساحلی عمان در تنگه هرمز در روز یکشنبه به‌شدت کاهش یافته و به حداقل رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666897" target="_blank">📅 12:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666896">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f817e286a.mp4?token=VuSXq7SU-9lf-kg-DxudgT3ppwu75KYsPtAnX--h6W8QDkqzyDN0YEVcxHk6KZORkcdF2AFjm-RCX_XCtGe_hwAW8yUJnUnobxwdstb9YGT1qNm_tzp8xx68-kBQFhvzFqtwCAGcXCt3-nTr7YoNcz2CeeAi9QU73vAAXlizn_WDxTJKKr-R_EOEFNCFNy3Ff7tQgOkr8_P89f74yWG2iITnUMkxabeJ9QPTgWjgsK5eGw44_m9jJQzS9P-p06qB8LdK08DKXrYiFmqU0ROq1rg976_SevAbvzjBR76W47itwiiC-NM0lpwFq5U8tkVkG2Jgo3tcHOJu6BvYvBZuow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f817e286a.mp4?token=VuSXq7SU-9lf-kg-DxudgT3ppwu75KYsPtAnX--h6W8QDkqzyDN0YEVcxHk6KZORkcdF2AFjm-RCX_XCtGe_hwAW8yUJnUnobxwdstb9YGT1qNm_tzp8xx68-kBQFhvzFqtwCAGcXCt3-nTr7YoNcz2CeeAi9QU73vAAXlizn_WDxTJKKr-R_EOEFNCFNy3Ff7tQgOkr8_P89f74yWG2iITnUMkxabeJ9QPTgWjgsK5eGw44_m9jJQzS9P-p06qB8LdK08DKXrYiFmqU0ROq1rg976_SevAbvzjBR76W47itwiiC-NM0lpwFq5U8tkVkG2Jgo3tcHOJu6BvYvBZuow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه یار...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666896" target="_blank">📅 12:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666895">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSw_4_lk-ujwzPESPAZFgMEMnrknMM1kiq335BKSU3dqIejVuILGpHQKthEoqDwnDN6w_Cp_T9o4s1zpt94Szf7eu2sn0Vw8_lKpYneQTJ_twuCBfXDbUmByGh3QACgiLjW1WkHIfjols3gmMwxKDIe5PvHwio063i1m2fqTHnkplpNu-DRxvS_GfehjqLOUGJG9y0MqGgkuRYTt2KTtmLnauqQkYqaUcKvdmUwvXgf3p7JLIGvPpilly9FMVJ50LVeuOe4U97-ph8w66vEUAdLUcXvx3NU4iUd5kJtaqqhAW9O0lXuE0Q7EA2bBLTX1CkbA7wqg1dhZiHByjtNF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام آیت‌الله مکارم شیرازی هم‌زمان با وداع و تشییع پیکر رهبر شهید: قاتلان و عاملان این جنایت بزرگ‌ مصون نخواهند بود
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666895" target="_blank">📅 12:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666894">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🏆
خروس‌ها با تک گل امباپه به یک‌‌چهارم رسیدند
؛
فرانسه به‌سختی از سدِ پاراگوئه گذشت
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666894" target="_blank">📅 12:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666893">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOEjxr-X76Ju1w5jxhYjJfUM-qTkaU3wwdGCPIWJbXzVT1DAp4OxTUU3jpsPgjRcWJDZF_0R7TslE3d4ffB7SqFAe8y6Ra5bDNVKu8cVpG-AzUx4-gUpqQlZQhAXu_yLyowpL-VHXKsQHmDkkCLqJSEx7_rmKgbZK-JOowKwKczbUihNhIVuIjBLIGdn7c3hNeopM1thV2NVARoBX8HkttkbMQ4HQE4CyZYn_nj_PjVVo77NucL9HsPer3OBJRXlBJDJ9_gRPFu7arLNWyEdocip00FR0SrC8R5Bf2eURHz09VT1O04wJHVO7XEnKPhLDUk1gXI0yBw_ckB4h3CwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: آمریکا هنوز یک قدرت بزرگ است، اما دیگر مانند گذشته بر جهان مسلط نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666893" target="_blank">📅 12:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666892">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تاکسیرانی تهران: تاکسی‌های ون تا پایان مراسم وداع امشب فعال هستند.
🔹
استانداری هرمزگان: احتمال شنیدن صدای انفجار ناشی از خنثی‌سازی مهمات در امروز وجود دارد.
🔹
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان
خسارت جانی و مالی نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666892" target="_blank">📅 12:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666891">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cbb8c8226.mp4?token=lTCu_9wbHT3OQBicUuQa8vwGme90jARx4B49HqyCV5Wotxjhsgb6Ow0kZT2ogX0FFdlPCKE33DN5FiOTLf_LJqvDf7twcHFKg92ydzAMA0wexMttsud1XtSrPLkZPNHQjZlprxcfAv1BGtzlqIyjbvB3Kw_wZVnbAIBfXBU42vI4RRMDprZZoeaPWpRtPnCqJFFhnCd4-REwvEmtqlOP5kOrfHoiVWXdJ-r6wtJ7uIDPvCkSWYt6uj9tBNxNkfgYBLysj_ElJW_fiCXfrTcoN8xsPB_Db3uBNQ6T0lmJgefGf88oZ7BWU4z37fFyRPaf31HdNEedXjaHthyuwWAwUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cbb8c8226.mp4?token=lTCu_9wbHT3OQBicUuQa8vwGme90jARx4B49HqyCV5Wotxjhsgb6Ow0kZT2ogX0FFdlPCKE33DN5FiOTLf_LJqvDf7twcHFKg92ydzAMA0wexMttsud1XtSrPLkZPNHQjZlprxcfAv1BGtzlqIyjbvB3Kw_wZVnbAIBfXBU42vI4RRMDprZZoeaPWpRtPnCqJFFhnCd4-REwvEmtqlOP5kOrfHoiVWXdJ-r6wtJ7uIDPvCkSWYt6uj9tBNxNkfgYBLysj_ElJW_fiCXfrTcoN8xsPB_Db3uBNQ6T0lmJgefGf88oZ7BWU4z37fFyRPaf31HdNEedXjaHthyuwWAwUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلی حقیقت به دروغ‌پردازی شبکه اسرائیلی اینترنشنال!
🔹
دروغ‌پردازی رسوای این شبکه بار دیگر نشان داد که برای پیشبرد اهداف خود، از تحریف واقعیت و طرح ادعاهای خلاف واقع نیز ابایی ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666891" target="_blank">📅 12:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666890">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0lWLCMkiELifCe0IyMDyP-QH6oAL3DFSwwon4ZD0952Z9N-7rvzjuBZRosEZHVi6xl-45BlxZXsrokQj8sqEiqub4X9LbC4n0r4yxwHHuWrFjEcDiea5v29HcpPed4JE3BCGjumTUZT0GQZD5JsyuttmErDVd7BAoLzVF0G-K-un4jHziI7gSwnzPlg5cE9LhMGoTjOWYycrfhUrMOEZEu1wpDOb6qg179aW7J5DlClRe0AshIrWP3o63Hz_V2-mzhV2_glDZK1AL9b1BTgJBuUNSV6wEnIwcuiY3VT7vulY8S1ctdGL8LHr3FP4gomlO5ZXBQ1YOmrZtg91MPG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدیو ترجمه آیات قرآن که در حضور نمایندگان آنان قرائت شد
🔹
عربستان سعودی: آیه‌ای درباره دو ارتش که در جنگ بدر با یکدیگر روبرو می‌شوند، یکی پیامبر به همراه مومنان و دیگری مشرکان مکه
🔹
ترکیه: آیه‌ای که کسانی را که در راه خدا می‌جنگند، بر کسانی که نشسته‌اند،…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666890" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666889">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
به جز دوشنبه؛ اصناف تعطیل
نیستند
رئیس اتاق اصناف ایران:
🔹
به جز روز دوشنبه، هیچ‌گونه تعطیلی سراسری برای اصناف در نظر گرفته نشده و تمامی واحدهای صنفی مجاز به فعالیت هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666889" target="_blank">📅 12:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666888">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6cb3a28d.mp4?token=p0Jl0853NFEM3NV_1s8UatfhZ1J-EGChayHyLhch_djardkmvRRbro269JM1We4Z-cFxK5sscknOawYe0bwxcNDRuu850MF6NMqz45DgR6fIJCgIfbNBRztjHKpgukiwQjPww1RYVoCR2k_u26NJXRH151ZkV_SS7Kh1qHwfAJnZaHu50f8qMMF3IsAyRGiNr4-972e2ZhJggMYAmzOvh4B1GYUIq-2eTs9sZuOoCoNmDQk01HnDVBr5SL-74pQlaj6oYn-LgiNQLtW7Kt996UUxgtGg4Yt1_IHQLXfzCR8sgET6ROQalQ6gU_yO3qsXAeC85s8eMzdszT5AJj_rdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6cb3a28d.mp4?token=p0Jl0853NFEM3NV_1s8UatfhZ1J-EGChayHyLhch_djardkmvRRbro269JM1We4Z-cFxK5sscknOawYe0bwxcNDRuu850MF6NMqz45DgR6fIJCgIfbNBRztjHKpgukiwQjPww1RYVoCR2k_u26NJXRH151ZkV_SS7Kh1qHwfAJnZaHu50f8qMMF3IsAyRGiNr4-972e2ZhJggMYAmzOvh4B1GYUIq-2eTs9sZuOoCoNmDQk01HnDVBr5SL-74pQlaj6oYn-LgiNQLtW7Kt996UUxgtGg4Yt1_IHQLXfzCR8sgET6ROQalQ6gU_yO3qsXAeC85s8eMzdszT5AJj_rdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه آخرین سان‌دیدن فرمانده معظم کل قوا؛ شهید سید علی حسینی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666888" target="_blank">📅 12:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666886">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb70a25114.mp4?token=JWxP2kvV-uEZHt6Gj2sIUmMDZH-0IAb0AgPN8Du0i96JlWLOtYvNqmeD-j-RjZm0kV85ob1_SmRI3Y6I0yEe2Qp5Raz3wznPiktaPSgooFOyYQYkfWrtg8Bt8XC1pPPoXrE5D9Qu570tPx0L_h-SO9l4aElLKuAJ2Ui6uYMqZrtK1KLAS0y769rQIcdhPmiRJiVLmdSLgAmaaGVZRUvRJdb-yJ8BE0d0Dr0FaXxw-l2X0mmew_vkhrwtEYMDX-Rqcn-GGN_nVjqjX1SU0y5YITBuRI5vOrrFxpXRBvmiO8imsVrjLaK-alK6u7JGbG52dDW3crqyqpwsLfyiJajvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb70a25114.mp4?token=JWxP2kvV-uEZHt6Gj2sIUmMDZH-0IAb0AgPN8Du0i96JlWLOtYvNqmeD-j-RjZm0kV85ob1_SmRI3Y6I0yEe2Qp5Raz3wznPiktaPSgooFOyYQYkfWrtg8Bt8XC1pPPoXrE5D9Qu570tPx0L_h-SO9l4aElLKuAJ2Ui6uYMqZrtK1KLAS0y769rQIcdhPmiRJiVLmdSLgAmaaGVZRUvRJdb-yJ8BE0d0Dr0FaXxw-l2X0mmew_vkhrwtEYMDX-Rqcn-GGN_nVjqjX1SU0y5YITBuRI5vOrrFxpXRBvmiO8imsVrjLaK-alK6u7JGbG52dDW3crqyqpwsLfyiJajvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دل نوشته عزاداران مصلای تهران در آخرین ساعات وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666886" target="_blank">📅 12:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666885">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
زندگینامه مردی که وجود خود را وقف انقلاب اسلامی کرد و اگر چه او را به خاک میسپاریم اما خاک ایران را به ما سپرد که نگهبانش باشیم. به رسم امانت میزبان مهمانان آقای شهید که مهمانان ایران‌اند خواهیم بود
موشن گرافیک زندگینامه رهبر شهید بصورت خلاصه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666885" target="_blank">📅 12:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666884">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
برای راحتی و آرامش سوگواران رهبر شهید انقلاب در تهران، مجموعه‌ای از تدابیر جاده‌ای و حمل و نقلی و خدمات سفر در نظر گرفته شده
🔹
قبل از حضور در مراسم تشییع رهبر شهید انقلاب در پایتخت، به این نکات توجه کنید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666884" target="_blank">📅 12:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666883">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91617dbd5.mp4?token=gs2J4Df6ZZABylzW9a8L3wobl35c0tOF-vcubbYba3skuBCfGCDB7fuApGRztHdB1p19Cu2iRqK19Cvpjx62QdTyt3fQ3-YbMZOfK37SMqwKNb2MAZYuaMieBuBwsX6x3AQFug2NgG_K_PToa-6TnChAvFEdnT5sTqNX8YpdBbz89OKSP7NeEyKJsA2Z9iIu9ozX0fxcb8f4xxI6BnIMeT_gOKuXP-S394JY_ZEngMcooWeFKClcWGHMOcaqtg_d41upMMQcX5Ya4lVDxw0ChjjTaGWx8829zU7IByTnmsj_NuEnr0SD9EvHlukkY7hdpCIyoSabb9o-xPtEP6vNWF5NvlxfE5MLiJOYOJ_w6a89QEdrj8CnmXw0EeLnrQC3DJBlJxut0jhdRq5j5jzXysa6AlgGgoIF-PuwJYzeu5jHYkWS4aqEUFpg36ceejUo0HGmCijwohw8cwn3BhfYQalCxWH0JuMO_Vjn8B6qe6JPdZtDZaA62i1r2cM0jbjetTuaU_B0iHMvMR6dsLpSGbkmpkXStnqSSfK_qhhaCcErF5XnVoHZ2Z_ffXIL65zPPDQZw-jj4Qqy9Z9ThDa0TZih3WzjnnN4JDbiJHdLnD45lyKlGRx67awZZ6Ckj1EpaM8FShaC0-6OYF1Y3ZvpmFluRiokynh4dzj_JlyhCUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91617dbd5.mp4?token=gs2J4Df6ZZABylzW9a8L3wobl35c0tOF-vcubbYba3skuBCfGCDB7fuApGRztHdB1p19Cu2iRqK19Cvpjx62QdTyt3fQ3-YbMZOfK37SMqwKNb2MAZYuaMieBuBwsX6x3AQFug2NgG_K_PToa-6TnChAvFEdnT5sTqNX8YpdBbz89OKSP7NeEyKJsA2Z9iIu9ozX0fxcb8f4xxI6BnIMeT_gOKuXP-S394JY_ZEngMcooWeFKClcWGHMOcaqtg_d41upMMQcX5Ya4lVDxw0ChjjTaGWx8829zU7IByTnmsj_NuEnr0SD9EvHlukkY7hdpCIyoSabb9o-xPtEP6vNWF5NvlxfE5MLiJOYOJ_w6a89QEdrj8CnmXw0EeLnrQC3DJBlJxut0jhdRq5j5jzXysa6AlgGgoIF-PuwJYzeu5jHYkWS4aqEUFpg36ceejUo0HGmCijwohw8cwn3BhfYQalCxWH0JuMO_Vjn8B6qe6JPdZtDZaA62i1r2cM0jbjetTuaU_B0iHMvMR6dsLpSGbkmpkXStnqSSfK_qhhaCcErF5XnVoHZ2Z_ffXIL65zPPDQZw-jj4Qqy9Z9ThDa0TZih3WzjnnN4JDbiJHdLnD45lyKlGRx67awZZ6Ckj1EpaM8FShaC0-6OYF1Y3ZvpmFluRiokynh4dzj_JlyhCUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های پربازخورد زائر رهبر شهید: از سازشگر متنفرم/ من فقط انتقام می‌خواهم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666883" target="_blank">📅 12:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666881">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
هر موبایل یه رسانه‌ برای ماندگار کردنِ بدرقه
🔹
هر لحظه از این بدرقه، داره با دستای مردم نوشته میشه.
🔹
هر موبایل یه دریچه‌ست به حقیقت.
🔹
احساس‌ها موج می‌زنن، اشک‌ها حرف می‌زنن و روایت بدرقه رو در تاریخ ثبت میکنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666881" target="_blank">📅 12:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666880">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7144b2b2f.mp4?token=HI_SJASOebYQO5UZlsZ2ej06Yzp29Llk5GV-8KlRgNbz-pfHy0ngc0ggNn8QQe5D3xDo6e6pA2sonxjcp5faMSVtE7pjLmaDEOvc9MY7MLBVsd3OpDYZeFTkjJK0NjOjGcrtuHo9vBPvjpUAumgApwRp6iCVmscRR2THDPQUHPacakFrJuAjrGwNZJxWlatPnOMRR93uuU0AGX8fKRhN9clJpITQomcKmKCCwaYWsvzJrPez4D8-jvCLwsKKhFS1hgMpWRKRtKi5qf_7SDJA9Jb3fD2c7KbM5glVHDR6xzjePXYGpJYm5lDME19M2-fjcntD9377hjmjQjMPs3ubZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7144b2b2f.mp4?token=HI_SJASOebYQO5UZlsZ2ej06Yzp29Llk5GV-8KlRgNbz-pfHy0ngc0ggNn8QQe5D3xDo6e6pA2sonxjcp5faMSVtE7pjLmaDEOvc9MY7MLBVsd3OpDYZeFTkjJK0NjOjGcrtuHo9vBPvjpUAumgApwRp6iCVmscRR2THDPQUHPacakFrJuAjrGwNZJxWlatPnOMRR93uuU0AGX8fKRhN9clJpITQomcKmKCCwaYWsvzJrPez4D8-jvCLwsKKhFS1hgMpWRKRtKi5qf_7SDJA9Jb3fD2c7KbM5glVHDR6xzjePXYGpJYm5lDME19M2-fjcntD9377hjmjQjMPs3ubZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری پزشک رهبر انقلاب از علت مخالفت صریح آقای شهید با وارد کردن واکسن فایزر: بعد هشت ماه مشخص شد که ماده‌ای در واکسن فایزر هست که مانع بارداری دختران جوان ما خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666880" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666879">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc59f37b8.mp4?token=C1o-VBD8Volb3ptHlohajMFd6UVvmh5f3N3UK2sT2mqLNI-msHFU-dWlGST0wxXBpLa6TPQYL0OQVOSH45blItTGSF_znfC9L7x13hiiklxCU4rZncwKmYCLFPdjhKdUm0f7TTqX0QD0a18B2JqbIa5wUlTtV3Qk_DvdCP2VPmYxJPaa9-tbGm0XeE-gt2pqBiKNKiXcC90kF0ZFpnAyjyXvlakom-TprljULiyENcva64nvSaUGcnr4hEcS5L-iPRHtXk5f_yEOSTCx_6Bqf5Iiwlzqd6gmexNxyZOE4QwW0Bu_BYDggXsS0XWChmxFYmW3eXjq0MMK6pZiN96bjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc59f37b8.mp4?token=C1o-VBD8Volb3ptHlohajMFd6UVvmh5f3N3UK2sT2mqLNI-msHFU-dWlGST0wxXBpLa6TPQYL0OQVOSH45blItTGSF_znfC9L7x13hiiklxCU4rZncwKmYCLFPdjhKdUm0f7TTqX0QD0a18B2JqbIa5wUlTtV3Qk_DvdCP2VPmYxJPaa9-tbGm0XeE-gt2pqBiKNKiXcC90kF0ZFpnAyjyXvlakom-TprljULiyENcva64nvSaUGcnr4hEcS5L-iPRHtXk5f_yEOSTCx_6Bqf5Iiwlzqd6gmexNxyZOE4QwW0Bu_BYDggXsS0XWChmxFYmW3eXjq0MMK6pZiN96bjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در میان فوتبال، غزه را فراموش نکنید
🔹
صفحه «m.z.gaza» با انتشار پیامی همزمان با مسابقات فوتبال جام جهانی، از مردم خواست: رنج مردم غزه را فراموش نکنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666879" target="_blank">📅 12:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666878">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28bfb2f159.mp4?token=ERY4aVpluuxpGEPQloZZ88r3UUuXnkbpcebK_lMxJH9DKhsZGTOlh9tqY_Ju4pAv7EFT_BQFqKbSbGq14kKmPrmuizFCK1noXemJEH0Rh9fqijesy_IhlizXB_C1hsLi17V6eTVPTqfASeRjewyOC762ZJZVuHmb_ij1bFYJSSalSeo0O35ILfG_qvvbTinaPkXF-u0UEP6sSkw4rICl3W3pfN0ghKlGILADxK-ujWm3pUdo7WIlBbeEkscq-Z9sP5tzmXJQEqb2YUIvb3XNyqdRcZLr-iGb3x5fbHBm6DXl3liAfSmk8cfltG_ubEsS-27fCaMB4r-me8WE00D1eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28bfb2f159.mp4?token=ERY4aVpluuxpGEPQloZZ88r3UUuXnkbpcebK_lMxJH9DKhsZGTOlh9tqY_Ju4pAv7EFT_BQFqKbSbGq14kKmPrmuizFCK1noXemJEH0Rh9fqijesy_IhlizXB_C1hsLi17V6eTVPTqfASeRjewyOC762ZJZVuHmb_ij1bFYJSSalSeo0O35ILfG_qvvbTinaPkXF-u0UEP6sSkw4rICl3W3pfN0ghKlGILADxK-ujWm3pUdo7WIlBbeEkscq-Z9sP5tzmXJQEqb2YUIvb3XNyqdRcZLr-iGb3x5fbHBm6DXl3liAfSmk8cfltG_ubEsS-27fCaMB4r-me8WE00D1eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ پس از تهدید مردم حاضر در مراسم بدرقه رهبر شهید، از ترسِ انتقام در پناهگاه ضدگلوله سخنرانی کرد!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666878" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666877">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjnMI71BRGyTqQL4oz9ajGCynPP5Md8k7hA-DlwnliW7NPAHJsTFqS1LZ7bU1QWK2ibQpeL82SUbWlLHb4MRDbccDoopv9vD0ttFqK0y-Q2wCv6Bp8cDCNEtJxvL1wVbJEwxz4xgWRmSKA2ElXZJoj7fhtZe05v7Xnke_dqQecQbkUBVuCmMzOE2w7VBTueGteRgWvp6XKiO7ggkw6I-Erjq-N7ENuZxPiwUnKoimMALPBdN4_Q62qBsJnjeWteHV5L3v1wqO5OkQfxrJRnvmcQOZHj7kA_Dod5cIkmEtBvg31xUTl-GxY5XB_S_-GJzcXXI643JACoqvbI8_cNCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥀
به امید دیدار
آقای شهید ایران
ما پا به رکابیم پدر تا برسد یار
ای رجعت تو ناب‌ترین لحظۀ دیدار
#رهبر_شهید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666877" target="_blank">📅 11:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666876">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
هشدار انصارالله به ائتلاف سعودی درباره هرگونه تحرک متجاوزانه علیه یمن
🔹
محمد الفرح، عضو دفتر سیاسی جنبش انصارالله یمن نسبت به پیامدهای تشدید تنش هشدار داده و تاکید کرد که یک حمله ما علیه عربستان می‌تواند آنچه را که این کشور بیش از ۱٠٠ سال رویای آن را در یمن داشته است نابود کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666876" target="_blank">📅 11:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666875">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس‌جمهور پاکستان، هم‌زمان با روز استقلال آمریکا، از دونالد ترامپ برای سفر به پاکستان دعوت کرد.
🔹
حشد شعبی: تمام آمادگی‌های لجستیکی برای تشییع قائد شهید فراهم است.
🔹
داروخانه‌های کشور در ایام مراسم وداع فعال هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/666875" target="_blank">📅 11:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666873">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
‏
سخنگوی ارتش: هر خطای دشمن با پاسخ قاطع نیروهای مسلح ایران روبه‌رو خواهد شد
سخنگوی ارتش:
🔹
اگر دشمنان خطایی کنند حتما با پاسخ کوبنده و قاطع نیروهای مسلح ایران مواجه خواهند شد.
🔹
بارها اعلام کرده‌ایم از فرصت آتش‌بس برای ارتقای توان رزمی خود استفاده می‌کنیم و یک لحظه را هم از دست نداده و غافل نمی‌شویم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/666873" target="_blank">📅 11:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666872">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdxsKpBANhH7xoYinj-J52OjRpPLAL4qPp9r-bOxlGj2lWCNTS72OUvoynYgYcLVVOFFWKKPY_fesBLRt_F0GrxFg1R2tj7Xbu29gEJwYWj6Tw0nQZ7wbwAiIO3M5kLYIK5jsD7PgBp267opgDYEy_mRTfePp9moDydqZIZ9qYZGtMawIfKnCFetREGRPJV2iCJf7hG3QxjGgtM6L5Fat1fxje9YmSZSuFYLVzoa3yl9VY2J94EaDPxshR6z3keoYfkIwteOGehIz2wOYU7kE505dXaxUEOqdKJsehvsQn_bi-ST9-AOWcQXI1FCuHt6KjVrGxFGfc32Pnos65r9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باشگاه پرسپولیس مذاکرات مثبتی با مهدی تارتار، سرمربی فصل گذشته گل‌گهر سیرجان انجام داده و این مربی در آستانه امضای قرارداد با سرخپوشان قرار دارد/ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666872" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666871">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/666871" target="_blank">📅 11:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666867">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tExnkx7dxBQ-RWsNI7N1vQl9Zkz3EK5jGsbYZ4ZjkjT_p_8OJfKwNjc4xdNG7qcTo4QLiIbxbXuwebnOURMmzLgppEPw5aeRoYOscGosw1v0eoAoBcfzQiezxbS62f8jBermgZu9dkEbf0DBlS1LWjuZkllLSVdKtBm1CT3v6brg4oPN3P5IW7_WcVgPZxPqrGVYaXuRXBJcYaG_KvdCQvrZSrNhN7PLhsI_IHgJEXSE9NR7uFfVLL_cx0U2EwnFmTuo6iGZJX5ZQrDBO1xoGPhF0eAfOmWcmeP0efJgpxDwWsYc07mkOO05ImqoW0L9aAHMo87qrR2eBVZ_Fcu1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqWgsQhSR26Ph0xFMyy0AIPaE4wStCam_Di3vxYIr3z7YfLFzWPfh87scoAbGdTBDnvLMqYwCRxs377Se9YaIyPQEJcqnfARXL1sV7CBhtom1mIIz6wDHTjCpT0nQR3VYaHc1dxjExCAGwNYNVe8rYqV3JAz1NRNebO5BvZ2WGn8qgMx1kZuw7bK8XrCKjTol8ldrD3TVIdFKWEVLPEVZXVUkebpAAOrzhqmC9MYG-7xIYLeJ9_poZHSfZBSclggxQpG-bCpq_6Eic4y4qg0HOpBtMwyMtz9ytk7uGUNZjMahBTIgsBYbEZo4wqxCyOaquykBwRUUNb8ATMsMuDkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_Z0fPTsh0TVMzxjTvcTqD1Pm9DM8iEq-qSrxi-hAY2lpwLyG5AoRi39ob7REPlAAcoYYmMVp6ZWcSODAjL6bIFfeAzxrKk6kd6Xa-IRAqZgY_lxxNjKvCk-6mpaaWZP15qJ2SAmzN6ujF1-hqrh5iwaGAL9d_fwYWgy7vZ5z99mr-GuDr5YUJ9JHzy3aXFFMBPmf6mKwcSvYm4Pm4yL37YwL3ETFqwRJ1rojmQF7IaCyrfQ1oJOk36nXJXCX0AE7Uy28CTxlEJC6oa_vtrBsWOFTZdN1iSE8QmKxgMkp04R976huTclW-SrPbpNb821z2dssWryxexZEABcEtrZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoHXi6rcBY7fw6oy-a3ra-weS0TRYsb73s0E-HBTdochJH6Mo0mlrLj9VXZmtqiudkO29r9GysKJQIVvNqHel_bZh3HGwgYnqH9QJCDfmIfndslR8ddWtTE7TybdqzG5Vo7zM48Vz_HJoU8ZU2MwxN-9vS8vRH_eHtyYQ_LCUWHhiRuLuSpDIDh0owMrVodsPwOcpcqTstwCIlByjx8I7_1Pv6gcevIiki3YqmWo5hiBTpjYVqumvl7fNAxjy7UC9842kqP481F3ACNJdpTk_iszEnpYVtDc-qIdj9iZ9E60Miq7vTUmBEKSYPOLNccNcdQN0br0LiiS7-ntXxSjOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از یک حضور تاریخی؛ جمعیت باشکوه مردم در مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/666867" target="_blank">📅 11:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666866">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9429f0e319.mp4?token=CpxYIFbo7QOODcEr7R9o516ZYnlRgHWmJHkBc-2NkXE3Am34MY8PMTVaR-I-5JRCwOWyoTgbBro7fBEcZFN6znUXt4Ql9DmVhmMWJFMAtAFSkqfmpm5aP-zO8QLbXejF4yd-jkm5Y626v_Sih8BCCbKPf_FujDxF8wsRuyNSw04igA4todffLdvHWKnRWrYih57axs9BqX2gGgBl7bhzEnKS9ZJWe-lAhkdA3vf5kcxOE5nZJhZnxP2QssCUUyk2y3Gvfn2SKzF_IbGBCiY3W676Enq7urkiWcK9naRJ7i5_8-JYzDwTEY97GzyzG6SxttNMCftsIyi9P-83Y9K-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9429f0e319.mp4?token=CpxYIFbo7QOODcEr7R9o516ZYnlRgHWmJHkBc-2NkXE3Am34MY8PMTVaR-I-5JRCwOWyoTgbBro7fBEcZFN6znUXt4Ql9DmVhmMWJFMAtAFSkqfmpm5aP-zO8QLbXejF4yd-jkm5Y626v_Sih8BCCbKPf_FujDxF8wsRuyNSw04igA4todffLdvHWKnRWrYih57axs9BqX2gGgBl7bhzEnKS9ZJWe-lAhkdA3vf5kcxOE5nZJhZnxP2QssCUUyk2y3Gvfn2SKzF_IbGBCiY3W676Enq7urkiWcK9naRJ7i5_8-JYzDwTEY97GzyzG6SxttNMCftsIyi9P-83Y9K-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی از شعر خوانی محمد رسولی:
‌ کسی که کشت امام مرا چرا نکشیم
که ننگ ماست اگر قاتل تو را نکشیم
از این به بعد کفن، جای جامه بر تن ماست قسم به خون تو، قتل ترامپ گردن ماست
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666866" target="_blank">📅 11:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666865">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSTt7Gxjr-xN_ksWvhxrRxNqCez3y2ZIeL5PIfHSzI4nsCcOW5mlkZ_BSk4eH6mlGRYNVOGCSGvVxgKEtcnneWfdSSex33YuSF0-oXVxh7WALhzGXWveoA1L43QkaOZruXJdZRoXwp-udN6DvLb4hBKiA06R0_HP99TAnUYnNief-ueRgPW83AGkmc1EmYLn1Be6td4M04w_x9o-1O_MvsqOxdCC8t7GBABM1dmh8nEK08uwDAhVdBlt9e-AZ-nM_0xaJV6AFbdKRayDxI8aJ_xL1T822XT_TWbCUdc3crMTiPs3IlkEInw1Ka4qgco3lOpZVE0W4vOW56f1MROC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری امیر قلعه‌نویی سرمربی تیم ملی فوتبال همزمان با وداع و بدرقه میلیونی ملت ایران با آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666865" target="_blank">📅 11:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666864">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خداحافظی اولین میزبان از جام‌جهانی/ مراکش متفکرانه و مقتدرانه در یک نیمه کانادا را برد
🇨🇦
0️⃣
🏆
3️⃣
🇲🇦
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666864" target="_blank">📅 11:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666863">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3235b035b4.mp4?token=Ja9G5UO2HcB76E1yv5_5fPs94Hw7gz3jrDTJ5Ek1hIMStR34l8Z4dxNwOJx5xabwk_2eBEVmt0WtiDBIaT5QExSM7LSH2eV663ZqVk0214j_ijD24u6qwXPt-YPWG_BJGDWeVzbcj5Db_uoXTwA9NMs9MH3n-luzqAsNn6olJ40jHVkahPrrg65Fdg5FzW-40BQEH2fgIDxSzay7NTr9oeINs7r5VDz1zk2Nj9qpiKQEVhpnlnPspf3Wuuwyj9n_LpOZ4mBCmlNz3udCL65G0gc7lVdKU2YK8F7ckZ1q82aVsWo19HNKFwgaIYJRgKDsiCVyiUApoijah01HZiJRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3235b035b4.mp4?token=Ja9G5UO2HcB76E1yv5_5fPs94Hw7gz3jrDTJ5Ek1hIMStR34l8Z4dxNwOJx5xabwk_2eBEVmt0WtiDBIaT5QExSM7LSH2eV663ZqVk0214j_ijD24u6qwXPt-YPWG_BJGDWeVzbcj5Db_uoXTwA9NMs9MH3n-luzqAsNn6olJ40jHVkahPrrg65Fdg5FzW-40BQEH2fgIDxSzay7NTr9oeINs7r5VDz1zk2Nj9qpiKQEVhpnlnPspf3Wuuwyj9n_LpOZ4mBCmlNz3udCL65G0gc7lVdKU2YK8F7ckZ1q82aVsWo19HNKFwgaIYJRgKDsiCVyiUApoijah01HZiJRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویرسازی با هوش مصنوعی از حضور شهید علی لاریجانی در آخرین دیدار
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666863" target="_blank">📅 11:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666862">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553d716180.mp4?token=NfILKZPz43tYuLlXnKlDbpyVepLMwdz1FSM8ZIsuTteRwisQJU2ukiWV9ZwrKPKL26iMLItv2raWc_ZcD1m9SFAKGSsVXgSI5CqgZgj7bdqYHk2OVKIycwJMSa8mzHMtyS0r-xT0QJpBXcDrMOkKVOVifV_gjDcQh8V-tAqxuWWT2OR5F54jJxjcOT98Cilc6ClaSKAbxCvuVe94igvbgUxiIgIn_t64w_0VyL-Kid5K8ejmCKG68FM48mEUn7mP7XNamwIIiOvatEnXfojlxR0r642OEJfUHBUxPi-Zq8wi1LTYM_8BeUFog4ufIwYrjsKc-ivELVGonpY8ZMjyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553d716180.mp4?token=NfILKZPz43tYuLlXnKlDbpyVepLMwdz1FSM8ZIsuTteRwisQJU2ukiWV9ZwrKPKL26iMLItv2raWc_ZcD1m9SFAKGSsVXgSI5CqgZgj7bdqYHk2OVKIycwJMSa8mzHMtyS0r-xT0QJpBXcDrMOkKVOVifV_gjDcQh8V-tAqxuWWT2OR5F54jJxjcOT98Cilc6ClaSKAbxCvuVe94igvbgUxiIgIn_t64w_0VyL-Kid5K8ejmCKG68FM48mEUn7mP7XNamwIIiOvatEnXfojlxR0r642OEJfUHBUxPi-Zq8wi1LTYM_8BeUFog4ufIwYrjsKc-ivELVGonpY8ZMjyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات انتقال پیکر رهبر شهید انقلاب به جایگاه اصلی مصلی پس از مراسم اقامه نماز امروز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666862" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666861">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c4042f3.mp4?token=s7ZvWgOL9UgrxHFc1uCxssIpBdvM5wac74fB5DnB-UgsFElW1JCkxxDFrfoaxDyRIWX1K58vBa3W8QjDdYC-ePFBlHGTEDFVWLj-PvwlJKiRIXapFuJy0euaKwE_IXwQSSSLL1yPfb7YlGVoxtIPlSC43Znr5NQvrUh2jP-V9PBivbe8SWd3zVYRVdoDj6-y3Q0OL71dzj1pu0GWac12yrC7OumVgsVYd96mIKiylEbfExvpmzfspr-1Qvl2f3CqY3l3B_zo0oe4PGCBGhU0Na0DMhexi6RjI2xx3vsnyv4dh5SOwMKRi8IBAstAFv77AwXmTmstbFYJDy4y9IJqwFG3g_c5NfYpsoqUVNb_d0gy1tKTSAVNXbky7kFYwUxNgCv_0_OytbHfMUB8IANwJXzRXSOm4x-I-8S4HiCDuGwErc3vu8A5TVItEGutnt1p6nWjvkOOSO612gXws0VPS6P6oB_SQx9VXtAGPvziQqI2DWULyuoOuZBFPcUyykdMJRTk8LKAKq3Ij_eE7On28SrX_O4AKm1epg53d_b6n2DWPn2FUyrIsJM9Ti0HhvLILGq-I4mJSIaktCIxE8Zaqx0InAeipumK4APscZVADvdPqaaWDrCiMGFk8u5QOpG2JgyQj4qtFvYr5qz5ZfBEdAPx4SyzNhS1c2URUI_hUGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c4042f3.mp4?token=s7ZvWgOL9UgrxHFc1uCxssIpBdvM5wac74fB5DnB-UgsFElW1JCkxxDFrfoaxDyRIWX1K58vBa3W8QjDdYC-ePFBlHGTEDFVWLj-PvwlJKiRIXapFuJy0euaKwE_IXwQSSSLL1yPfb7YlGVoxtIPlSC43Znr5NQvrUh2jP-V9PBivbe8SWd3zVYRVdoDj6-y3Q0OL71dzj1pu0GWac12yrC7OumVgsVYd96mIKiylEbfExvpmzfspr-1Qvl2f3CqY3l3B_zo0oe4PGCBGhU0Na0DMhexi6RjI2xx3vsnyv4dh5SOwMKRi8IBAstAFv77AwXmTmstbFYJDy4y9IJqwFG3g_c5NfYpsoqUVNb_d0gy1tKTSAVNXbky7kFYwUxNgCv_0_OytbHfMUB8IANwJXzRXSOm4x-I-8S4HiCDuGwErc3vu8A5TVItEGutnt1p6nWjvkOOSO612gXws0VPS6P6oB_SQx9VXtAGPvziQqI2DWULyuoOuZBFPcUyykdMJRTk8LKAKq3Ij_eE7On28SrX_O4AKm1epg53d_b6n2DWPn2FUyrIsJM9Ti0HhvLILGq-I4mJSIaktCIxE8Zaqx0InAeipumK4APscZVADvdPqaaWDrCiMGFk8u5QOpG2JgyQj4qtFvYr5qz5ZfBEdAPx4SyzNhS1c2URUI_hUGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای کمتر شنیده شده مادر رهبر شهید انقلاب
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666861" target="_blank">📅 11:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666859">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8236b59e.mp4?token=It3LF9zYQ7hbTjMuaDeNcEv9f7F1Ji9AmNwlEzbGiro-q1Sg-ipKlHUqI7JPlerpma-nScn3HyKV-y9Dk2Tox-og9mPbcU67KaA5xR4fIFRXsiDcNjaeIIIdwjdfpeV8u9IIp3RUQ9J1ZOdYpnjee9oOTOMb61kuH1kbUA-zV3IMD4gSotsUpksXlw5r3-x-yQtKkkGUdw_4NUrlim86KWPMfi-tdC3PtOry1nQlB7EB7ojU8luLAaOo8vs5SympgZvDfX6XdAj9-WCDni_5_QIm-a1Ezf2uOF54LdJuwCgcHkk8IxmviZFEbUVyIDmjQ67X60WzEt83P360slH_Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8236b59e.mp4?token=It3LF9zYQ7hbTjMuaDeNcEv9f7F1Ji9AmNwlEzbGiro-q1Sg-ipKlHUqI7JPlerpma-nScn3HyKV-y9Dk2Tox-og9mPbcU67KaA5xR4fIFRXsiDcNjaeIIIdwjdfpeV8u9IIp3RUQ9J1ZOdYpnjee9oOTOMb61kuH1kbUA-zV3IMD4gSotsUpksXlw5r3-x-yQtKkkGUdw_4NUrlim86KWPMfi-tdC3PtOry1nQlB7EB7ojU8luLAaOo8vs5SympgZvDfX6XdAj9-WCDni_5_QIm-a1Ezf2uOF54LdJuwCgcHkk8IxmviZFEbUVyIDmjQ67X60WzEt83P360slH_Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اختصاصی خبرفوری از مراسم وداع و
نوای حیدر حیدر مردم خون‌خواه رهبر شهید در مصلی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666859" target="_blank">📅 11:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666858">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b347366e52.mp4?token=mmo1-xdX3sdY2gh2puV63FWSLL9nLgP-hgPJcaUZAsQEyP0Es3UCScMFo6d1bijNaz-P4Aocebwlu4sQtOnAxzXyqxKVBmCzLr6qzUVOFd86c87a9fE6fLYrr11txF6deYm6RxUR46heZznMI8HKhS9-Hox-OZ8iUhQW7LXXNWYrtVubQVZeHJlVcwetksITY92E3L6Adwivq85LAdsmQAwWUx94XJu36ZnijDJXsE_O1yu5S4xV3NCdC_xH9wZ-dCUulu8YIQPQdQGYs5faRFqJhiVwfKPkll9OGBPTB4jFgfOXw7g2m2hvljEqcXa6sYcYnMKfqOjPUQvXaTTiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b347366e52.mp4?token=mmo1-xdX3sdY2gh2puV63FWSLL9nLgP-hgPJcaUZAsQEyP0Es3UCScMFo6d1bijNaz-P4Aocebwlu4sQtOnAxzXyqxKVBmCzLr6qzUVOFd86c87a9fE6fLYrr11txF6deYm6RxUR46heZznMI8HKhS9-Hox-OZ8iUhQW7LXXNWYrtVubQVZeHJlVcwetksITY92E3L6Adwivq85LAdsmQAwWUx94XJu36ZnijDJXsE_O1yu5S4xV3NCdC_xH9wZ-dCUulu8YIQPQdQGYs5faRFqJhiVwfKPkll9OGBPTB4jFgfOXw7g2m2hvljEqcXa6sYcYnMKfqOjPUQvXaTTiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاطمه مهاجرانی، سخنگوی دولت در گفتگو با خبرفوری: تصمیم‌ها در راستای منافع کشور در شورای عالی امنیت ملی جمع‌بندی و اجرا می‌شود و نظر مردم حتماً شنیده خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666858" target="_blank">📅 11:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666856">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3jQgSXll7USUhu6n0DQc1sMvMsDcIopZ8cnPoWkaErkECOqXP_HcLREni-x3H6a22U6ZGrYOZGTnSc-_Id8Ii5JGi1rxtnyWvR82tmvXRUeMGxSs03NKaODx9z-aGlJdCe8bGsVhLqWBGuK4wuJX7Ttb9sEGM-SX_s-8FGeGTC5fvNVgWm1VGq2wZOatSw5i1AtESwdAo6Wf2MCq9oBS_2DNf9hQgaNBkeYcUsjJiicTIIQ9mCRdRbtF7U1LLs3UqdOrNOJGH5m8hFAQCOBjX6ZiBKsyVPwcGLcEL_7-M99R8A7kBA4l9Z0ZwABOkDWuK9vdLPfTUcEQBywKw0L8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hkj_NRuvu0jJAuMEeldJ6-2fK0GRxqHn8K_S-GbiFE4bZtLWmtklo_6dyzlRQZ8HFNaB4VasRlX6jtGAgWxQ7FeL2exfp21fX0hfnBYHS4aB0MA0YfJT_wfUA8SWlQsYBiLwAAcFBEMnXDIaOvyG96o6ICJpWtk8rwyMGXnREpUtfWbGZTTQ3kOe-6F_lRu8ZbtJfvoKgAeseoXh4_baF1MjZSx5AJkgLltl8KJnvi4BfKrZe88BJ4D4tbbgHKgX8KoGinX0l10w1WnmDvQWK81cye_F5T1HbJCMAp1WSW59ylvJGKbcpJzRGuyZs2E96VxCb_ARaps32zyl4fQCmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
📷
نخستین تصاویر از بوئینگ‌های ۷۷۷ که به‌تازگی وارد ایران شده‌اند
🔹
چند فروند هواپیمای بوئینگ ۷۷۷-۳۰۰ER (مدل دوربرد و پرفروش) که از عربستان وارد شده‌اند به ایران رسیده‌اند. این هواپیماها به‌خاطر مصرف سوخت بهینه و برد بلند، از مدل‌های مهم پروازهای بین‌المللی هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/666856" target="_blank">📅 11:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666855">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7pAsrVSjoDlTIhol-zODEohoZEfm9SfoZuLBg4OUx3SCZBGoALj3RnJmKH39naNnVDLXL-7n1gA9xGu1XnG0Vm8sLzqg96sd0xTVKfkKcq7AUmxagOyqpP4NlmbAo8o-qDjMlbH_YOawQk8dDx1O0jKZGNxoHgAL5Zo6rqRPoj0UoU3sH0GjHIr95hoaDx8zxtFEGqz40L2Y878kVNZXYW0F7vZTLAw46NOY10YdfOO0hM2oeWfC6AmXrNoOWUrfeLhbCeUzFWhtppxBHJ98GBarfDqE3T4FOaHbaV-DKHEVQB5lBvUbLaL3AyWZkink2zZPCJA8ORASLvXQXOVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور رییس کل بانک مرکزی در آیین اقامه نماز بر پیکر رهبر شهید انقلاب و خانواده ایشان در مصلی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666855" target="_blank">📅 11:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666854">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a7352771.mp4?token=g5HjOwoOGyFn_4TUcnomkAlOdZRWMz33C029xwezyvuQlawUP2DPXX8luZYQ8NU1jrFurTYys-MO3AW6u6vF97g-cYEj6Dy6MmnRhgE_MGKtYfikM4OPX8GmmkTlsVcphZ407IfdeWRGWjx-xlu7XUu0fZXJgb9Y36kbVVNfywrXQS8MHK5jBokbjUvPwZksMzjFfUmQgntF1DvXfO6itoY_K-CVKDKFm6oawxhO_Nkw_Nsz9151ctxRCLkZ4V-PA2YVjv5WLYEkgfcdxHCY6aMpS5u5MJ7x0fTLXYTuvkoV6LzvnKqSdXqkjYk2eDV0RV6jG8oBws19uDpCH8oXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a7352771.mp4?token=g5HjOwoOGyFn_4TUcnomkAlOdZRWMz33C029xwezyvuQlawUP2DPXX8luZYQ8NU1jrFurTYys-MO3AW6u6vF97g-cYEj6Dy6MmnRhgE_MGKtYfikM4OPX8GmmkTlsVcphZ407IfdeWRGWjx-xlu7XUu0fZXJgb9Y36kbVVNfywrXQS8MHK5jBokbjUvPwZksMzjFfUmQgntF1DvXfO6itoY_K-CVKDKFm6oawxhO_Nkw_Nsz9151ctxRCLkZ4V-PA2YVjv5WLYEkgfcdxHCY6aMpS5u5MJ7x0fTLXYTuvkoV6LzvnKqSdXqkjYk2eDV0RV6jG8oBws19uDpCH8oXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمشین لگویی وداع با رهبر شهید انقلاب!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666854" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666853">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
مردم برای حضور در مراسم تشییع امام شهید نگران تامین سوخت خودرو نباشند
سخنگوی صنف جایگاه های سوخت کشور:
🔹
تمامی فعالین به صورت شبانه روزی در تلاشند و تامین و توزیع پایدار سوخت در سراسر کشور برای حضور مردم در مراسم تشییع رهبرشهید جریان دارد و مردم نگران سوخت خودرو نباشند.
🔹
توصیه اصلی ما این است که کارت سوخت شخصی همراه داشته باشند و قبل از حدود ۲۰۰ کیلومتری استانی که تشییع برگزار می‌شود خصوصا تهران، از پر بودن باک خودرو اطمینان حاصل کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666853" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666852">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=Dv5ZcWnhuwOlWIur81_veGLDKn3y0s-xxnbPTiEhwkaJMgBuuY-fgiC5tFNbmHhYqpwOtS6-vOgiwUvAnaeLzb9kMK7Zal2b06Q9z44C8wkwVbehrZDUJ8FSAGnbpzrX9CxkGT_-EFD0Lhsm1LtQ4S23SNZ0E56xBgtFU8Vhj4A_IoIIz59XyLb8LSUgSeHhi8mOwUHoVPdZd8trYWF34h_5EwhSmsoAVFIoQDAqPlMlMcWiSMd8vJlsvUbYktXF7zOkhCdGXLE22p_k7oDNfb1WQdThtCHTN4jK3M_vQaYch77k85JmS7v_Jg8QX8BYxG9DB-GdetoRYxIB4gLEcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=Dv5ZcWnhuwOlWIur81_veGLDKn3y0s-xxnbPTiEhwkaJMgBuuY-fgiC5tFNbmHhYqpwOtS6-vOgiwUvAnaeLzb9kMK7Zal2b06Q9z44C8wkwVbehrZDUJ8FSAGnbpzrX9CxkGT_-EFD0Lhsm1LtQ4S23SNZ0E56xBgtFU8Vhj4A_IoIIz59XyLb8LSUgSeHhi8mOwUHoVPdZd8trYWF34h_5EwhSmsoAVFIoQDAqPlMlMcWiSMd8vJlsvUbYktXF7zOkhCdGXLE22p_k7oDNfb1WQdThtCHTN4jK3M_vQaYch77k85JmS7v_Jg8QX8BYxG9DB-GdetoRYxIB4gLEcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین تصاویر هوایی از حضور باشکوه و گسترده مردم و اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و خانواده ایشان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666852" target="_blank">📅 11:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666851">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe81201fc.mp4?token=F3TazMHN9BclN7HX55ZE7tfvavC0zsmYVWkpIgg9-HzC37oejjIyTfQf2yv5E4sgyK9cK09ubgne_nrCX5tLOVG0_x0c-xbQ3XikIQnM_8-C8NyhjNdHEHe-a1rfYgAsTBG1d8Uk8E-MzJRPaJ3Fvjec_s_bJThyTocCcIiKICTVHT3hEKRY3BHj-gQ1E0WHPLbwtjoEgSCB_QLoHyjjTuXpg63hoYdvH_pRUfJQFBfUm2WD7l__5rmAvWaZbe2sItd1Kc988AkoJgoqV2-wsEiRVGk8JKzNy-bPCF-kMMqzIbdaGk7HptTaLXmeDm9hmowpRpvcpnGhi6-7ajvGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe81201fc.mp4?token=F3TazMHN9BclN7HX55ZE7tfvavC0zsmYVWkpIgg9-HzC37oejjIyTfQf2yv5E4sgyK9cK09ubgne_nrCX5tLOVG0_x0c-xbQ3XikIQnM_8-C8NyhjNdHEHe-a1rfYgAsTBG1d8Uk8E-MzJRPaJ3Fvjec_s_bJThyTocCcIiKICTVHT3hEKRY3BHj-gQ1E0WHPLbwtjoEgSCB_QLoHyjjTuXpg63hoYdvH_pRUfJQFBfUm2WD7l__5rmAvWaZbe2sItd1Kc988AkoJgoqV2-wsEiRVGk8JKzNy-bPCF-kMMqzIbdaGk7HptTaLXmeDm9hmowpRpvcpnGhi6-7ajvGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ ای مظلوم جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666851" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666850">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b188edccc0.mp4?token=FeVUG66MqFslCm7UlulxZuptNrZbPQ96SP6Mr4qAuSHjBRcLaDhpTLZkzC76FxhBnRbPIaYxp4W3gl64QGJjjNTBU2g0CjR9eZARnEg-SvNtjIC7CT0ht7ZNGtLlGBTswBnNTmWQFmjDB_lVFEMWVqdgNrABlBLNl58-26oIDRIB5n0tjCwMlBfao9_ZPlwQxLGOmlwQU0v_kJWP01DPc6cMaT0d5HiD8TlbafNeRoRNWwft60_BTW7HNQsPmAB0nmPWr3BY9b1c2uCk69DtzzCZgmGkJEaoZw2aPArneEnDNZgA6CKoc1LuHYJBW3bnF_pcidCn84vKQN80Qb-K3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b188edccc0.mp4?token=FeVUG66MqFslCm7UlulxZuptNrZbPQ96SP6Mr4qAuSHjBRcLaDhpTLZkzC76FxhBnRbPIaYxp4W3gl64QGJjjNTBU2g0CjR9eZARnEg-SvNtjIC7CT0ht7ZNGtLlGBTswBnNTmWQFmjDB_lVFEMWVqdgNrABlBLNl58-26oIDRIB5n0tjCwMlBfao9_ZPlwQxLGOmlwQU0v_kJWP01DPc6cMaT0d5HiD8TlbafNeRoRNWwft60_BTW7HNQsPmAB0nmPWr3BY9b1c2uCk69DtzzCZgmGkJEaoZw2aPArneEnDNZgA6CKoc1LuHYJBW3bnF_pcidCn84vKQN80Qb-K3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب اقامه نماز بر پیکر رهبر شهید در رسانه‌های عربی
🔹
شبکه العربی با پخش تصاویر زنده از تهران، از ادامه حضور گسترده مردم در مصلای امام خمینی(ره) برای شرکت در مراسم تشییع و اقامه نماز بر پیکر رهبر شهید خبر داد و حضور پیوسته مردم را برجسته کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666850" target="_blank">📅 10:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666849">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSePMGwO54K2p4nEEm9-m9oih23UVxC8FDvVSXUpS_KEf-Rz74TPzTaZDS8jUtfYoojBj4zuVVI5F8-bKOVPOp0nI5yGof0bnFa4_jMzkFUDO7K19zqJXWsXP3C9DEOnS3bFpj8-QTDgDMo1yBo9Eegx8HcP6Hlh4oZY2d1vzWOvZjPpnDgeFJdHL6mtJUE_njP-8KLA27HYaPWTm_0GiYB84XuYuku-gRiyzoqnBXVG8IrSO33zA-hVU4X3svMyh0d9Z_h4YsLOmzZMPv2dzN7bRFMFOWBawTrMUI4Cw6QmfWJ-eCVqIdy5bf2DkvTbt9wAFeomP5a-l1LYvhMyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666849" target="_blank">📅 10:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666848">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAETXP9OHhIqpMF5zQFLZ_PjDDJZ2_J7danbjKQX8MFbF3N5XVT5ocjklzSgyT3APaC4MjOLwbXwdMM6DM8RtWucMAyMOMPc-Q8_AqrSwT6H9x1QQTzKAAxsZoL8gQB0AaYf3dozb3kGRwTlINZGbcJUjFaw-t-HA-awxiuK756UJRiS7ihDQNSnHPiKvmvcbrBsWg7-kGH9q3XFnp0eV4I2WBvSecEU8KIhjqwYnkW1e0yR0xj5k3XPIsuT1JhByerqX39OBHYSGEmfGYGZbdk9dMmyC7ZDhOazzEXVp3AlrymbemBlFnhWckjpcYF1CyFxQZQhlsDKkSruRbasvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیر صعودی شیرهای اطلس طی ۱۶ سال در رنکینگ فیفا/ از رده ۷۰ تا رتبه ششم!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666848" target="_blank">📅 10:50 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
