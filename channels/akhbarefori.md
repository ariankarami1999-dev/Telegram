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
<img src="https://cdn4.telesco.pe/file/pGGFUxPvsnjDETcgdY9M_QgTzzwcPpgCZFDnYH1GM06Szm8wUgCdqwLHbN_dZRbRa_I_Dk2sfFkYYFLWsmeX76E4I0O_61SsahARHuVRNQwzmZFf9B_hxDStVFdSwRnmgdfUh48iSh1wJG2S0a7nFx01a-xEjfqXbavy23GXdoxFkUtBY2IEK-s3MuFlXBMeD1648AonkQY54krU0C9T-1Vy2bMZiH6dEMw0eTUdQjFnK1KRVa2F4vQqB2Th728hhO1jImNssffdaFtgJ9gOduNdjdFeciOpaFXHg4G8Hzi4HVOimKn5yOyCGj9yU31uTtuuc_JnZEWnVuCuMhyNvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-687166">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO5ybWng5eJuEUPpkKFncJO-1mqUpOSyiiMuTbMXCUZ01U9XbCsIAMGVFy4KEtjiig9oCOhvsKCr_apog4BjCsyU3Bx8uAp5mmJvcvIShO88BoCa6UY4aW78lTeaCmu1-pVJ2oquWHymFuo7f3lHx2eeHbw8gV1s1sYt4Y01DY7_wcHC-gUQhaD2x9dXGvNkZm9yhT3hw6324afuAKwG3V0i1yqsPdJ-aP9tSuiWq0Okt-Ok_J94q_LvbXHGpAio6dkMci-jLoV16uxIHcAzV-UN2c-AkBJxURaj74rFzD-Q0P_BU2iPlz7LRKXPkypkwTYWpdfcaiYfp1h1U5CosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر امور خارجه کشورمان به اظهارات اخیر همتای اردنی؛ ایران برای پاسخ به متجاوز چقدر باید منتظر باشد؟!
🔹
به نظر وزیر امور خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/687166" target="_blank">📅 17:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687165">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3GLjugEqLRPsq65aDZdrTMBnUIz6p4Gu3tanTtgGJmfyZPdwKK7LB6TwKIwC0LW5M4n6mR8TROazZgVGRLQfhLgQ0yVGQlzroDcuoIfWBfaX3SJYt6tzCgjkkyoGznA3Fs5peSKUWuvsTuRIKqvIeSMPm5gCPh8gTk_UvYGc6VLRh-9ez1iivhsS3MZ0U5CWDrIgJKKda4ZLzYRnsxnE-fwQusoajcw_biLWzws5I6IjTrapeGwyp2ksO8D7huaDnXuwS6sOvYGBPcKpAhPXMnqF2fgAHQTO5SJpZps1uh8ceFDi3Wns0pYh0lw_o2WWEOp_ahosDhCGE_jJA_k9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۶۰ ثانیه چه اتفاقی در اینترنت می‌افتد؟
🔸
تنها در یک دقیقه، حجم عظیمی از داده در دنیای وب جابه‌جا می‌شود؛ از ارسال ۲۰۴ میلیون ایمیل و انجام ۲ میلیون جست‌وجو در گوگل گرفته تا بارگذاری ۷۲ ساعت ویدئو در یوتیوب.
🔸
در هر ۶۰ ثانیه، ۴۱ هزار پست در ثانیه در فیس‌بوک و ۱۰۴ هزار عکس در اسنپ‌چت به اشتراک گذاشته می‌شود که تنها بخشی از فعالیت لحظه‌ای کاربران در شبکه جهانی است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/687165" target="_blank">📅 16:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687164">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyNKwpsGvTwfWpc22YYZTBbjI9LtjEmgtPRBaWltOMj1E01UEBGI6WMk8WjkVp2JItF-bYHcFQERpxhIbSMkU02t452D3XdYi-T3apJYdyX9H6AvS-6KSOxgRl5F8QAXR4l128WlL4TTfv41koqJdU3lrQxpGgMkbpWntdMbMlpqzqhgKKZphm9Ax3TQYQ-oGYco3EOlqoSiuSismP8IPZE1_kwrXwTcIfOm_-PKDkw0SfL0ilw7WDONoGDGt-fPsb2hnZ6f130ZPwiI9hu23iNCpViXEmWG5e5l-abaoCJ-kzLJrrymhMV_c30qR05ES_u3FDiIlt1U071XI4JdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره ادعای آمریکا را زیر سوال برد/ تردد کشتی‌ها در تنگه هرمز زیاد نشده است
الجزیره:
🔹
آخرین داده‌های ردیابی کشتی‌ها تصویری متفاوت از ادعاهای امریکا را نشان می‌دهد و تعداد بسیار کمتری کشتی در حال عبور از تنگه ثبت شده‌اند.
🔹
طبق گزارش شرکت تحلیل دریایی کپلر، تنها شش کشتی در روز چهارشنبه، ۱۱ کشتی در روز سه‌شنبه و پنج کشتی در روز دوشنبه از تنگه عبور کردند. این شرکت میانگین ۱۰ روزه را ۱۳ کشتی در روز اعلام کرد.
🔹
سایر سرویس‌های قاچاق کشتی نیز الگوی مشابهی را نشان می‌دهند.
🔹
شرکت داده‌های دریایی لویدز لیست اینتلیجنس، از ۲۶ آگوست تا ۱ سپتامبر به طور متوسط ​​حدود ۱۲ عبور در روز را ثبت کرده است.
🔹
اگرچه بریجت دیاکون، مدیر اطلاعات و تحقیقات دریایی این شرکت، گفت که آخرین داده‌ها ممکن است «به دلیل تأخیر در شناسایی عبورهای تاریک» ناقص باشند.
🔹
این بدان معناست که برخی از کشتی‌ها چراغ‌های ردیابی خود را خاموش می‌کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/687164" target="_blank">📅 16:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687163">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دیدار و ادای احترام وزیر ارتباطات به استاد خود پس از ۳۰ سال در اصفهان
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/687163" target="_blank">📅 16:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687162">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-9b2gsXrYKntHQ7jObtughy4sxm3ddb1EHhE2k55AvwL85V-mWYEcgJpaXSjFDeFwY8NogfEtxzhsSG2pA7JgsSvKrhhUQC2IkuFFqAPzxWit_9Ut6JxIDX0YrprFHq3EGm0A39rWTW9xiCXfdeEhk71OtTgDzX7xzc_Flg5V3i6tBP-JF8mAILqBskDkM-R4C47Z5FXcSpKHONMyQZsTwsfSezc7OXJTmsJZju-EBfyDI02QbJThFic09dNC-SFzvTvO3Qr1Hex7jSe4fVV1o_0rD9-pnI1AGoCc-NJEwuB85AlaTOxTqXTDTfmk8BI9lONXS5ptAB-2UcRBTzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نیم‌رخ» از امروز در زی‌ویژن
سریال معمایی «نیم‌رخ» به تهیه‌کنندگی علی طلوعی و کارگردانی رضا شریفی، از امروز جمعه ۱۳ شهریور، به‌صورت اختصاصی در پلتفرم زی‌ویژن منتشر می‌شود.
مهدی سلطانی، حامد کمیلی، بهاره کیان‌افشار، سیاوش خیرابی، شیدا یوسفی، مهرداد نیکنام، شهروز دل‌افکار، مهرنوش مسعودیان، مهدی رکنی، پونه عاشورپور، افشین سنگ چاپ، لیلا بوشهری، رضا کریمی، بهزاد خرازی، یوسف مرادیان و محمد شیری بازیگران این مجموعه هستند. سریالی که روایت آن بر پایه رازها و رخدادهایی شکل گرفته که به‌تدریج برای مخاطب آشکار می‌شوند.
زی‌ویژن، پلتفرم نمایش خانگی نبراس پیکچرز، با انتشار «نیم‌رخ» نخستین سریال اختصاصی خود را عرضه می‌کند. نبراس پیکچرز پیش از این تولید آثاری همچون «شغال»، «جادوگر»، «ملکه گدایان» و «مانکن» را در کارنامه داشته است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/akhbarefori/687162" target="_blank">📅 16:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687161">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سخنگوی ارتش: پاسخ به تجاوز احتمالی اسرائیل سریع‌تر و کوبنده‌تر خواهد بود
🔹
از بین رفتن سامانه‌های پدافند هوایی دشمن در جنگ ۴۰ روزه به‌معنای بازشدن مسیر حرکت موشک‌ها و پهپادهای ما به‌سمت سرزمین‌های اشغالی است.
🔹
اگر رژیم صهیونیستی دست به حمایت یا تجاوزی بزند،…</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/687161" target="_blank">📅 16:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687160">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d056894.mp4?token=LfBk4W6AKogc708DwM4TXNuI-jj_t2aHZkAwcN4J28YdiB4ILorzToorb94ISu_NFXtibPYkX3HTNPbo4UFXESCB7VM8bJ0r6OEVhGGFA8z3P6qmT3XaZ2R-BP_bEgLAt79W3GW85vYgdMuMJX57jZxDc3Ar6llhEpSc5gGfl2L-vCDKe9jyoddtU2ZjKZR7ZlZw7By06BUwsZvSxP7av7YT9MAysOQCCV9MsLDVQyivqMls01Is5vGtY7hC-2dpMfM7oRzB9pENM-dfGeJG8EPgHCHyVZBLyQY0FRpJJqnEL-MRESgEzLchFYr1sTa2HsHp3G-KAsbXwdHERtNy7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d056894.mp4?token=LfBk4W6AKogc708DwM4TXNuI-jj_t2aHZkAwcN4J28YdiB4ILorzToorb94ISu_NFXtibPYkX3HTNPbo4UFXESCB7VM8bJ0r6OEVhGGFA8z3P6qmT3XaZ2R-BP_bEgLAt79W3GW85vYgdMuMJX57jZxDc3Ar6llhEpSc5gGfl2L-vCDKe9jyoddtU2ZjKZR7ZlZw7By06BUwsZvSxP7av7YT9MAysOQCCV9MsLDVQyivqMls01Is5vGtY7hC-2dpMfM7oRzB9pENM-dfGeJG8EPgHCHyVZBLyQY0FRpJJqnEL-MRESgEzLchFYr1sTa2HsHp3G-KAsbXwdHERtNy7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه میخوای بدونی پنکه سقفی چجوری کار میکنه این ویدیو رو ببین
#موشکافی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/687160" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687159">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWCz4Ju_w2zLTDTqcMetitWaXzIZzloL2jEBokkoFxgKoLwQQy005D7Srj_IC2d8fRpQRj52lAaer4_SfTLt9CAZDojJhWHdlEEB5JETOIEiHge1Gaagt4672wQl6lPXBYcvf-NJ4YxrEtYiSbkHOUA_KVg3o_jol6awhyWiOn2JUgOi6bPMNvTORZ9XJi50AwpZOt3guVdyA5rCVO68Qbx6GiwMYgf1vt7NRvWlmTkkOVCrGOjL74GqETEXktQrh747XZS_8Kb2xyv5hJvjiwH2EGoHhol8E90blM6g2OHWGFLUfaBaCxLJwK3lh0oQAPT5L1iaIFcUfSGerYalXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمان با کاهش قیمت طلا، ارزهای دیجیتال هم سقوط کردند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/687159" target="_blank">📅 16:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687158">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
برنامه‌ریزی شستا برای سه وضعیت جنگ، نه جنگ‌نه‌صلح و صلح/ ستاره خلیج‌فارس در مسیر IPO
محمرضا سعیدی، مدیرعامل شستا در
#گفتگو
با خبرفوری:
🔹
شستا برای هر سه وضعیت (جنگ، نه جنگ و نه صلح، و صلح) برنامه‌ریزی دارد و امیدواریم توافق‌ها به نتیجه برسد.
🔹
امیدوارم توافق شود چرا که در سایه آرامش و توافق، کارآفرینی شستا در داخل و ورود به مرزهای بین‌المللی شتاب می‌گیرد.
🔹
سیاست حرکت از بنگاه‌داری به سمت سرمایه‌گذاری، رویکرد اصلی شستا است.
🔹
ستاره خلیج‌فارس در برنامه آی‌پی‌او (IPO) قرار دارد؛ ورود این شرکت به بازار سرمایه، لنگرگاه محکمی برای بازار سرمایه کشور خواهد بود.
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242509</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/687158" target="_blank">📅 16:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687157">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سخنگوی ارتش: پاسخ به تجاوز احتمالی اسرائیل سریع‌تر و کوبنده‌تر خواهد بود
🔹
از بین رفتن سامانه‌های پدافند هوایی دشمن در جنگ ۴۰ روزه به‌معنای بازشدن مسیر حرکت موشک‌ها و پهپادهای ما به‌سمت سرزمین‌های اشغالی است.
🔹
اگر رژیم صهیونیستی دست به حمایت یا تجاوزی بزند، حتماً راحت‌تر، سریع‌تر و کوبنده‌تر از گذشته مورد هدف قرار خواهد گرفت و آثار بسیار مخرب و زیان‌باری را متحمل خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/687157" target="_blank">📅 16:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687156">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1caa70bc30.mp4?token=oaXPlzu0kaWD4o-mzEu6imtMYthrHOISqGSedgv5BNWWyOG29YRhOMA1d6-m5_99s60IOO68ijohsSnyCaOhdjh2aJEbeaS8uvyW7y--RCw-1TiwmPANEdQw8HvS7qlFbuedBGCYu-oZsF42CHtfqUTcfj4EIx53dKQT-lFvmZynJ8nvurnWSaJVAIdVn_Fc7JrY9zaH9LTJuqqfXgQCrCs8MoESVnwjRhez1UivtTPZYEfZnKiG4SF4eATH25dNFEth6tPHqbJGfhhSKTVnoog1dVcR9b2-FyoVMH49302jh-szxzAUJzgSrcNyzb90nIzghHaayIGN9rqZN8fESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1caa70bc30.mp4?token=oaXPlzu0kaWD4o-mzEu6imtMYthrHOISqGSedgv5BNWWyOG29YRhOMA1d6-m5_99s60IOO68ijohsSnyCaOhdjh2aJEbeaS8uvyW7y--RCw-1TiwmPANEdQw8HvS7qlFbuedBGCYu-oZsF42CHtfqUTcfj4EIx53dKQT-lFvmZynJ8nvurnWSaJVAIdVn_Fc7JrY9zaH9LTJuqqfXgQCrCs8MoESVnwjRhez1UivtTPZYEfZnKiG4SF4eATH25dNFEth6tPHqbJGfhhSKTVnoog1dVcR9b2-FyoVMH49302jh-szxzAUJzgSrcNyzb90nIzghHaayIGN9rqZN8fESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاوی تصاویر دلخراش| ویدیویی وحشتناک از یک تصادف
!
🔹
هنگام عبور از حاشیه خیابان بسیار دقت کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/687156" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687155">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soQOHSB7rLJBkVUml_yqqnXIrzkoBUE_e5gle9LF6xJ6d51FMpA7R6-4HFvMSaZU15Y3qfZtmz7zfj9Va3zZGYr0J888IENkojfd68Fyp9U1Rxcsb6xH91TzsWSg4EtcwSo-rQBsf82BjlSDDcHPxNnRWbdmQQP0ipypNpGJYy5ZEIDBPiaTRpdApe9JRe3hSALm3wTn1t2JYXDTry1qC_XW5qWgP9JZkfbKBAkkPMy2mTnRHLNztPMg3nXsUA6yR3WpoEdxECceyI-KAw9YyfERX3eJDMOpJUyAA9RNsjcc65ED8RXAVXvLRtdsBeVDUzoxeE6cpeSm-JfKwLSNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
سایت گیزمودو تصویری از آیفون ۱۸ منتشر کرده که از وجود احتمالی دکمه جدیدی روی این گوشی خبر می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/687155" target="_blank">📅 16:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687154">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سازمان اداری و استخدامی: ساعت کاری جدید ادارات شنبه ۱۴ شهریور اعلام می‌شود و بانک‌ها نیز از یکشنبه ۱۵ شهریور مطابق دستورالعمل‌های جدید فعالیت خواهند کرد
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/687154" target="_blank">📅 16:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687153">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501dc301d9.mp4?token=M5XKBpxcoaOgsZnFA5A1upTyJQ3suQkhF3uEuJcjgQifubHYaNHAlXqn5ACPKBfnVM0NFdAlDDSD50-UP2vUfTRVzHVLEqirauUurSWYWQFFazH4Tov300IgtGsk5ReTUPjvWay8piYI84jFbb67Ue4nYHhq_eA0iQ-2CaMpA3pWyPGRknowveQLUX51yu46ZulToQ2bdVOD1Xp71VhMy70vL7f3bFXzSzV64rr_2d021umtGcPX7zjk4T_qwmeO43VxDim1K9zaokwPkd4YHBR7WLLf9PkA8Z0Luwq3a7awNG-bR8jntF9iib2ncOwq0s_uu-w_Zrj7krAg06Vy0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501dc301d9.mp4?token=M5XKBpxcoaOgsZnFA5A1upTyJQ3suQkhF3uEuJcjgQifubHYaNHAlXqn5ACPKBfnVM0NFdAlDDSD50-UP2vUfTRVzHVLEqirauUurSWYWQFFazH4Tov300IgtGsk5ReTUPjvWay8piYI84jFbb67Ue4nYHhq_eA0iQ-2CaMpA3pWyPGRknowveQLUX51yu46ZulToQ2bdVOD1Xp71VhMy70vL7f3bFXzSzV64rr_2d021umtGcPX7zjk4T_qwmeO43VxDim1K9zaokwPkd4YHBR7WLLf9PkA8Z0Luwq3a7awNG-bR8jntF9iib2ncOwq0s_uu-w_Zrj7krAg06Vy0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شورای عالی امنیت ملی تصمیم گیرنده درباره آغاز و پایان تعطیلی جلسات در صحن مجلس است/ هیچ کدام از نمایندگان از شهادت نمی‌ترسند
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
مجلس تعطیل نیست بلکه فضای فیزیکی آن بر توصیه و مکاتبه شورای عالی امنیت ملی، جلسات در آن محل برگزار نمی‌شود. پایان این ماجرا نیز باید با توصیه شورای عالی امنیت ملی باشد.
🔹
هیچکدام از نماینده‌ها از وضعیت مجلس به این شکل راضی نیستند. نکته در این است که هیچ قوه‌ای نقش جمهوریت مجلس را ندارد و جایگزین کردن آن هم راحت نیست وگرنه کسی از شهادت نمی‌ترسد. امیدوارم شروع برگزاری جلسات مجلس در همان صحن باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/687153" target="_blank">📅 16:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687152">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1daecf089c.mp4?token=G1EBO0aNQ6H2I2TQXZF4I9wFn6LTjldNLthO1C1eouHZuTNc6-88Zcp9voiQxhzALalJ4UoIgH0mwO2yDc6CtLchIcj_DxvXfFHqotIYzMtHqHqrkkgHBg0cAxMeOcDfG8v3i1AoWkBBR_48UZiKTlxfN1tohovnk58XRT5g5UHuO1TgjvvinGZNv4Oe3G-hpU8NQXhF2NBhvalYNGqYaH7eoAaH0NsINJy36WIOoTVdvrjTahzDbQYd4h_HAF-b5zPLtSLYKA_K7deERpgWuhwCdZkbGckiIuYUStZsfiLkPOzJGs98ZWSjNaEDH01GUZPYmnxs7z5wIRcah-izcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1daecf089c.mp4?token=G1EBO0aNQ6H2I2TQXZF4I9wFn6LTjldNLthO1C1eouHZuTNc6-88Zcp9voiQxhzALalJ4UoIgH0mwO2yDc6CtLchIcj_DxvXfFHqotIYzMtHqHqrkkgHBg0cAxMeOcDfG8v3i1AoWkBBR_48UZiKTlxfN1tohovnk58XRT5g5UHuO1TgjvvinGZNv4Oe3G-hpU8NQXhF2NBhvalYNGqYaH7eoAaH0NsINJy36WIOoTVdvrjTahzDbQYd4h_HAF-b5zPLtSLYKA_K7deERpgWuhwCdZkbGckiIuYUStZsfiLkPOzJGs98ZWSjNaEDH01GUZPYmnxs7z5wIRcah-izcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عرب نیوز: حمله پهیادی دقیق ایران به یک واحد در آخرین طبقه یک برج در کویت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/687152" target="_blank">📅 15:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687151">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
البوسعیدی: عمان از تلاش برای توافق درباره تنگه هرمز عقب‌نشینی نمی‌کند
وزیر خارجه عمان:
🔹
یکی از محورهای اصلی دیپلماسی عمان، تلاش برای دستیابی به توافقی بوده که آزادی کشتیرانی در تنگه هرمز را احیا کند و مسقط با وجود پیچیدگی موضوع، از این مسیر عقب نخواهد نشست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/687151" target="_blank">📅 15:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687150">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
هشدار سازمان غذا و دارو درباره ۱۳ محصول غیرمجاز
🔹
سازمان غذا و دارو اسامی ۱۳ محصول بهداشتی و مصرفی فاقد مجوز را اعلام کرد.
🔹
این محصولات شامل کرم حجم‌دهنده باسن و سینه AICHUN BEAUTY، کرم ترک پا زرین الماس، پماد ترک پا، بادی‌میست GALAXY، ادوتوالت TEA ROSE، ادوپرفیوم DELGADO، مایع سفیدکننده فرنود، ریکا سیاه، شیشه‌شور الماس دریا، پاک‌کننده NANO TAK، نمک ماشین ظرفشویی FINISH و پودر زغال فعال هستند.
🔹
سازمان غذا و دارو با هشدار درباره خطرات احتمالی مصرف فرآورده‌های فاقد مجوز، از شهروندان خواست از خرید آن‌ها خودداری و موارد عرضه را گزارش کنند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/687150" target="_blank">📅 15:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687149">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده پدافند هوایی خاتم: به‌زودی دشمن را غافلگیر می‌کنیم
.
🔹
وزیر بهداشت فرانسه: نداشتن کولر دو برابر جنگ ایران قربانی گرفت.
🔹
۲ ماهیگیر در محدوده سد تاریک رستم‌آباد رودبار غرق شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/687149" target="_blank">📅 15:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای اتحادیه‌ طلا: ۲۰۰ پرونده شکایت برای فروشندگان طلای آنلاین تشکیل شده است
نادر بذرافشان، رئیس اتحادیه تولیدکنندگان و فروشندگان طلا تهران در
#گفتگو
با خبرفوری:
🔹
اتحادیه‌های طلا در سراسر کشور با فروش طلای آب‌شده از طریق پلتفرم‌های آنلاین مخالف هستند، اما اگر فروش به‌صورت محصولات فیزیکی باشد، موافقیم، زیرا در فروش طلای آب‌شده مشخص نیست آیا معاملات پشتوانه فیزیکی دارد یا خالی‌فروشی صورت می‌گیرد.
🔹
برخی پلتفرم‌های آنلاین ادعا دارند ۱۰ درصد معاملات تحویل فیزیکی دارد و مابقی مشتریان خودشان تحویل نمی‌گیرند، اما اتحادیه این موضوع را نمی‌پذیرد و معتقد است هر معامله طلا باید با تحویل فیزیکی همراه باشد.
🔹
پلیس فتا نیز اعلام کرده حدود ۲۰۰ پرونده شاکی علیه این پلتفرم‌ها تشکیل شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/687148" target="_blank">📅 15:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687147">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ترامپ درحال بررسی اعلام پایان جنگ است؟/ مدیریت پایان جنگ با جمهوری اسلامی است و با تغییر دکترین دفاعی به تهاجمی، شرایط پایان جنگ را ایران تعیین خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/687147" target="_blank">📅 15:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687146">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EliObo81iGpe8Pn7CLnbPw8Tq1io6EkM9CC-iXf7Ux7g99pw_Dqaknjdn7SYcT0sKcYzgqflyCEimv6YwTy2JlWP6jvdUnbjbgfD_6fcJavXdpd6XSDQgJsw5RMKAB4empdsaILGiIvpz6b5oJxjZgQws2S4vs8eu58pNad5_aziErR62B-0FlWuOrjvlo74Z9H8IqtVjmuz2rddmovACj-JINRfpvHI7Jd9RA7xEu26XXL405v-LQj1PLqy7McXe54rXJbcj9ti4gk7nE54QZjW1e3wBQFrJOgz_bJGpzJoKKpItnoHcwvQWBgg9oQJ4qAU0xLGwohtSN1MPSd_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ارتش: راهکار مناسب برای آمریکا پرداخت هزینه‌ها و خروج از منطقه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/687146" target="_blank">📅 15:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=nwbgCRzN0_CRxQ87qjanL4idHm1admMr9GgipoMoygx-kuXz97PycwOMeZ4oITXR4lH_gF5dGVTu0ZsnK8hWN0ExvLYNNvCGDaZbY9pcEakVvs1wgGKreZLOjeI_iFLkPsCh_rzgg7r7IiULMLTM6X0DDSSDtqshawgZsiRSuXCOmslHCjZrjvmi4Q5iGFHiDVDKdgP1yHHWo8mR0uDa1uiLXYWSfD5BZ5kuq23WUXJJsUqz0yMf38BH2oNT1mCgeljQWrxa-RPvFqJtcX77CsiASmtAaamOwsx19px5ZxvGiFq-4IEv_NWOyo3bcQ0DrePSDEYUSKVkkaR6PDe7uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=nwbgCRzN0_CRxQ87qjanL4idHm1admMr9GgipoMoygx-kuXz97PycwOMeZ4oITXR4lH_gF5dGVTu0ZsnK8hWN0ExvLYNNvCGDaZbY9pcEakVvs1wgGKreZLOjeI_iFLkPsCh_rzgg7r7IiULMLTM6X0DDSSDtqshawgZsiRSuXCOmslHCjZrjvmi4Q5iGFHiDVDKdgP1yHHWo8mR0uDa1uiLXYWSfD5BZ5kuq23WUXJJsUqz0yMf38BH2oNT1mCgeljQWrxa-RPvFqJtcX77CsiASmtAaamOwsx19px5ZxvGiFq-4IEv_NWOyo3bcQ0DrePSDEYUSKVkkaR6PDe7uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی جدید از شرایط تورنتو کانادا بعد از بارش باران و طوفان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/687143" target="_blank">📅 15:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687142">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
دویچه‌وله: آمریکا می‌تواند مواضع مهم ایران را نبود کند اما دانش آن را نه
ادعای دویچه‌وله:
🔹
تهران در حال تعمیر یا تهیه تأسیسات راداری جدید، مواضع ضدهوایی و موشک‌های ضدکشتی است.
🔹
بمب‌های آمریکایی مطمئناً می‌توانند مواضع مهم ایران را با حملات هدفمند نابود کنند. اما دانش و پایه صنعتی فناوری نظامی ایران باقی خواهد ماند.
🔹
بنابراین، بازسازی می‌تواند به تأخیر بیفتد، اما نمی‌توان از آن جلوگیری کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/687142" target="_blank">📅 15:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687141">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5QQ5TmOKYmHQfqp4KphLTnQXOtgYHYV5OpmMC7V0DNnAm0PYsMjkox5hJiF3Kc7-tejS-HLRj5Z34RepignHjGc1RGX82qsHJnrLWh_8lrT4ZzJQtvzpoFIS2vh0OMwkraEymOLlAa5uzpT7TpeK_ZasOICO-a_bxbPRrYAJ713LEOz-AlPfZbg_hSbK3yXlVLAfsBG_4FSrySE78-pM-ZnSXYX7-dmKflRRa0rhmFcq1AR3mLfV5kTF5SUcjuNVXPWzSKUgZ1bF4N5vgkvfqOeGH4Txyd9y5jc3esqYUbLvFbx_k0irUK9Wk-sxjslkjZCfhwusvZHhHNzl_h1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: مهمات آمریکایی مستقیماً به مراسم عروسی در ایران اصابت کرده است
🔹
تحلیل کارشناسان تسلیحاتی از تصاویر و ویدئوهایی که رویترز صحت آنها را تأیید کرده، نشان می‌دهد انفجاری که روز سه‌شنبه یک مراسم عروسی را در جنوب ایران به خاک و خون کشید احتمالاً ناشی از…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/687141" target="_blank">📅 14:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Co6RXLXrZHdBpdQ3yf-nHZFS9NtlpKGhCHD1nlv4yhdYwWkV9w6vw7eyQ971nblAsNbBRhDDeWuHGhMF_L52Aa_dfaKHl4C4lQxJgmske6F5BLP4xE4UGf1U0fjqYKahIzAnlRlqu43XF-CaaHMxjbTsEJm1RzsqkV5Jj3lfTYfLgiEzIb2v_2EKZY63yR366WVFJWNPJvuCPIQ2ET6CPdyKiQfnOb3wZL0F-T3wFMnxwYUNQA-oLdefKgv3hxPr_LJvq-5J1rAShOfFh4w8Enqxa-lh5oOuF5ZeT2raSII14sYTucW7rS833PlsbvYbVO2xY5vnAUUOyq-hfH5QIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر گازوئیل نیروگاه‌ها به ۳.۲ میلیارد لیتر رسید
🔹
ذخایر گازوئیل نیروگاه‌های کشور به ۳.۲ میلیارد لیتر رسیده که بالاترین میزان ثبت‌شده برای این مقطع است.
🔹
مصرف روزانه گازوئیل در بخش غیرنیروگاهی حدود ۸۰ میلیون لیتر و در نیروگاه‌ها در نیمه نخست سال حدود ۷ تا ۸ میلیون لیتر است.
@amarfact</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/687139" target="_blank">📅 14:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
خبرهای خوب معاون عمران وزیر و رییس سازمان شهرداری‌ها و دهیاری‌ های کشور در خصوص توسعه حمل و نقل عمومی
نصرتی:
🔹
با تجمیع منابع مالی حاصل از انتشار اوراق مشارکت، طرح‌های مولدسازی و درآمدهای مستقل شهرداری‌ها، حدود ۳۰ هزار میلیارد تومان(همت) برای خرید چند هزار اتوبوس و چند رام قطار تا پایان سال اختصاص یافته است/ اتوبوس‌های فعال در ناوگان حمل‌ونقل عمومی کشور از ۱۲ هزار دستگاه فعلی به حدود ۱۵ هزار دستگاه تا پایان سال افزایش می‌یابد/ در صورت مساعد بودن شرایط، با احتساب خریدهای انجام شده و تعهد تولیدکنندگان داخلی با همکاری سازمان برنامه و بودجه و وزارتخانه های اقتصاد و دارائی و نفت، تا پایان سال، حداقل هشت تا ده رام قطار برای ناوگان متروی تهران و سایر کلانشهرها در دسترس مردم قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/687138" target="_blank">📅 14:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ffb4c5058.mp4?token=Hf0S65fn8YYvfxVhvVeQC7fbhlw378Y27JEJ5ssxNPLaXTQHtyGoihwtPfZVcxx74u1iQLAf9I2GdcwZrLqhoYWIZekQhjO_U7TBRo1Fm_1gHHzHTvc_hxdgz3A-C8cT7J-GksUc4aFj3VKjpcnmUbsMbqXgi6EaO5T9JQHfWQOa0dnRL3e_x_fphyHh60f0JytYjSOTTNGVHsClpsUlrYUPiV_mSD9sDpoRlGENVsNlBvNWzSjwCpPioFWnKmzmnyKLQ19iWWblwZZe0Fv4uPtkJzZ3Z-DUTht-GZsCOCoxyGMT33C-a04iY6ZRMfMXEBxk_UtD0ezWKe-7_2B9o4HMu0P_HKhjExZka_4PgqqtXFJRkt6A0BHYvnoFR7HGK9U9azukEzttUeKQysIlEMy86drPsMbFC3mtcx7S-PJVgVpOIm5NeNMBbZl3qAWwtEvovzdkOXI1MReloI_4JQi64gAo-zeTF6koPuCPFIGmuU1BdG6A0BWmYn64ilgUz_VCka5odaeAx-K4bSXFrQELEfMue7acYgrzHg6GvSU_wBwOTzYKvtrZUBVQWlzHL8NSa06ewvZDRYGE7OR45xNK3uOMkrSKQSOJte9uwSZTlRfXnlegVUmgHQtZUWE-_lN9OzGjScu7L7526IOf-ckvRvt0syqtPSzcrRLS1lM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ffb4c5058.mp4?token=Hf0S65fn8YYvfxVhvVeQC7fbhlw378Y27JEJ5ssxNPLaXTQHtyGoihwtPfZVcxx74u1iQLAf9I2GdcwZrLqhoYWIZekQhjO_U7TBRo1Fm_1gHHzHTvc_hxdgz3A-C8cT7J-GksUc4aFj3VKjpcnmUbsMbqXgi6EaO5T9JQHfWQOa0dnRL3e_x_fphyHh60f0JytYjSOTTNGVHsClpsUlrYUPiV_mSD9sDpoRlGENVsNlBvNWzSjwCpPioFWnKmzmnyKLQ19iWWblwZZe0Fv4uPtkJzZ3Z-DUTht-GZsCOCoxyGMT33C-a04iY6ZRMfMXEBxk_UtD0ezWKe-7_2B9o4HMu0P_HKhjExZka_4PgqqtXFJRkt6A0BHYvnoFR7HGK9U9azukEzttUeKQysIlEMy86drPsMbFC3mtcx7S-PJVgVpOIm5NeNMBbZl3qAWwtEvovzdkOXI1MReloI_4JQi64gAo-zeTF6koPuCPFIGmuU1BdG6A0BWmYn64ilgUz_VCka5odaeAx-K4bSXFrQELEfMue7acYgrzHg6GvSU_wBwOTzYKvtrZUBVQWlzHL8NSa06ewvZDRYGE7OR45xNK3uOMkrSKQSOJte9uwSZTlRfXnlegVUmgHQtZUWE-_lN9OzGjScu7L7526IOf-ckvRvt0syqtPSzcrRLS1lM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری نماینده مجلس از لابی‌های میلیون دلاری و خطرناک در مدیریت پسماند/  مدیریت پسماند زباله‌های صنعتی تنها در اختیار دو شرکت است که با ارکان دولت ارتباط دارند
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
خیلی برای من عجیب است برخی موارد مانند خودرو یا موضوعات اقتصادی دیگر لابی‌هایش مشخص است.
🔹
در موضوعاتی مانند پسماند که لزوما تمام تصمیم گیران نسبت به آن حسی ندارند و اصلا نمی‌دانند این موضوع می‌تواند اولویت چندم باشد. باید تازه تشریح کنید که موضوع چیست و با این کلونی ارتباط می‌گیرند و از منظر تامین منافع خودشان موضوع را در نظر میگیرند؛ این (اعمال نفوذها) بیشمار مصداق دارد.
🔹
مشکل قانون قبلی پسماند این بود که ضمانت اجرایی و جرم‌انگاری دقیق نداشت. زباله‌های صنعتی باید بی‌خطرسازی شود؛ شاید در طول تمام این سال‌ها شرکت‌هایی که این زباله‌ها را برای مدیریت می‌بردند فقط دو شرکت بوده است؛ شرکت‌هایی که مرتبط با برخی از ارکان دولت بوده اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/687137" target="_blank">📅 14:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0L_-5--2xowTT6SY3qbqidzCJNtURM-XldwK2mSBVMM1husgDpLCpRYlEko4UySxdbmDxGElICxmldsC0VxpqaDRtmRAc_gfnnZyrw6oUyywh_Not_IZOWN0_a3TTCZuo3lowJgvjS4uA7eHBIvuDTCc3Zuh2oRAjJsnUS4sF8IInYROPa7EpQ4yBbNnw0Z2cRMQyQ7BN4F0rQAgOj8AFNqvVJleSyMhBDts5qyOY8jz4FJrieqVq1h4mTMiIRNFFIX8DAY9jjLUGnjYLfZ-pmhM9xAXuXvb2AqVbJb1nMVKZAXIib_OeYA7VDon-mETP7TQg-1Rqn_G0CgzASWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در درگیری با گروهک ضدانقلاب
فرمانده مرزبانی کرمانشاه:
🔹
گروهبان‌یکم مرزبانی «رضا دارایی عمارتی» در جریان درگیری بامداد امروز مرزبانان هنگ مرزی پاوه با گروهک معاند و ضدانقلاب به‌شهادت رسید.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/687136" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687135">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmBChZcWxzAvyEvljfij_TD0F6SwCaU-5zU8wyrK3nTCw6bbtIBTvUx6DiE9feDaYKGjnkhD98iNMG6n8D-Yw8nCg5o5wVngjWrUm_ZC_bZKtT9ihAs_gcyKsTRF1WniuwHk-2hGmiG4EAImtBTX66K2W8nRd6U-GZ_zUuuCgcnx91rVA8c9NrT2cO5PgUipRpoadOO3haIM04EMuecjjnKaFN82VPHf42TTY8dOG9Tidl3OEzms9J7E12OPOoPpKoQGiRYXif8im3zfxv1UMzoEgJQleOSWOZ4ZLx0HiaCuntZZ6cNesr6otB1eWssTef_eVbGFfOwaoRFmHkAqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا برای دریافت اطلاعات از یک سردار ایرانی جایزه ١٠ میلیون دلاری تعیین کرد
وزارت خارجه آمریکا:
🔹
تا سقف ۱۰ میلیون دلار جایزه به افرادی پرداخت خواهد شد که اطلاعاتی ارائه دهند که به شناسایی یا تعیین موقعیت مکانی سردار امیر یاریاب، فرمانده عملیات سایبری فرماندهی سایبری سپاه پاسداران، کمک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/687135" target="_blank">📅 14:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687134">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
آمریکا تقریباً به اندازه بودجه پنتاگون روی هوش مصنوعی سرمایه‌گذاری می‌کند!
🔹
سرمایه‌گذاری آمریکا روی هوش مصنوعی حالا به ابعادی رسیده که می‌تواند کل اقتصاد این کشور را تحت تأثیر قرار دهد.
🔹
برآوردهای دانشگاه کلمبیا نشان می‌دهد پنج غول فناوری یعنی آمازون، آلفابت، متا، مایکروسافت و اوراکل، ممکن است سال آینده بیش از ۱ تریلیون دلار برای زیرساخت و توسعه هوش مصنوعی هزینه کنند. رقمی که تقریباً به بودجه پیشنهادی ۱.۵ تریلیون دلاری پنتاگون نزدیک است!/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/687134" target="_blank">📅 14:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687133">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Plj9vaEVMeaNZT0PiOeMdRaegFgXHOL_SDRjudGxFfy8RahTt46CSRqEugrg_wS3Cg42B_2-a6pgCf1eSsFIkn7N2W0QEu3InPeQLry2AdmHfUj3a8fTvy6yMeA9Zoxyz_bno0ln6QIG_HoJ7bsbdv_dDRt9t-TAxW5wee94-C-zDENQA935bcfqGz7zwPqkWYxAJuAo7ztF9E2Dphxbf4PWzM-TLePEVOuJr2Xijgf3yrehvOiAzmxEXlWK4y6zliTBpsunRvX-XP_KaWm6Kpw3P8vQg-n83cgwSJ3-Mj-pOLdV3pyOV6UFchsaeE_LmQ_VBo5pn4eYDlHIzBZ2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شتاب چادرملو در توسعه معادن جدید/ هدف‌گذاری برداشت ۵ میلیون تن سنگ‌آهن تا پایان سال
فرید دهقانی مدیرعامل شرکت معدنی و صنعتی چادرملو به خبرگزاری تسنیم گفت:
🔹
چادرملو در پنج ماه نخست امسال ۱،۵ میلیون تن سنگ‌آهن از معدنD19 برداشت کرده است. حجم باطله‌برداری از این معدن در همین مدت به بالغ بر ۱۵،۵ میلیون تن رسیده است.
🔹
در پنج‌ماهه نخست امسال، یک میلیون و ۶۵۰ هزار تن سنگ‌آهن از آنومالی ۱۰ استخراج شد؛ این در حالی است که میزان استخراج در مدت مشابه سال گذشته، ۱۲۰ هزار تن بوده است.
🔹
برداشت سنگ‌آهن از معدن چاه‌گز به‌دلیل حجم باطله‌برداری هنوز آغاز نشده ولیکن برنامه‌ریزی شده تا پایان امسال از مجموع سه معدن یادشده ۵ میلیون تن سنگ آهن برداشت شود.
🔹
همچنین در کنار تأمین، برداشت و خرید سنگ‌آهن، توسعه فعالیت‌های اکتشافی و شناسایی فرصت‌های جدید معدنی به‌ویژه در شعاع ۲۰۰ کیلومتری مجتمع معدنی چادرملو، با جدیت دنبال می‌شود.
🔹
مشارکت در محدوده اکتشافی زمان‌آباد و پیگیری فعالیت‌های اکتشافی در محدوده‌های بایچه‌باغ و کال‌کافی  از جمله برنامه‌های شرکت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/687133" target="_blank">📅 14:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c52S0-J1ErU9725-6z8PHy2jDUDFkqwgYwGplihS4LT3v5ecGJO2r2mn5r6vGchBtemtJkYaMt9LZuZKCes9ZHYMSWurkrJ37hgzd1hyr4wlHhwNXz2tecxmE59w_QIlvDfr2G3H0Z8Jk5FeVxlG01IHLjTSqcgjI7opLQ1SMVcs1x6r-EoXgJhN06jRVvzLHcqzleTjmKAzrFj1KjVfkd2yoR0SV8UFTJ9sngv6Sdu4SX2Nt5Cur5j2w0Q1eCwollAzizm8FOQsIsntkBw5pJWyR9Y4vtekpgjJBmLdGi7ST1oHcQaka8sTbxXeiotYouwOnHbqQaUit1fy3VqljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت چشم‌نواز حاشیه رود ارس
🇮🇷
#ایران_زیبا
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/687131" target="_blank">📅 13:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک تخصص ویژه ایران که آمریکا را کلافه کرده است
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/687130" target="_blank">📅 13:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر نفت: بیش از ۵۵۰ اصابت به جزیره خارک داشتیم.
🔹
۵۰ کیلو مخدر شیشه در آذربایجان‌غربی از یک خودرو کشف شد.
🔹
ویتکاف و کوشنر به مسکو و کی‌یف می‌روند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/687129" target="_blank">📅 13:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kv0NyOcuvWKC5Z_NB6lxdyKBD7Ho5nnNa--Upe1ikAiudWozS06rCdJY96df9Qxkq4c07UhsOKaJQzXK8j9a41k8hdhByS6WvKM12gjYHgLmE42Gcf3xJ-EuCAuPzoF7sL3gWiYjT-eBJbeCWWSG4as3fMFznMqOhbCXVx2IMYvDVGSlXmwTq-lZbMVZLGNA7iar9V-S0xaERstsYg3QbolTd46rf5wK1mbW6c8TGbHkOBjl2DAxuGSzWII68R_pioWb_XoW4hgbvjiuhNesK9dZmdFaI6xORozCmnjqib_z4lSBpwK6B-NMCPZfi1Mh04p_q8BhCzmn2mUrb_O2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIECXDwKyN5XQCbCPWxsujM-pfk7HI4p_cuqEUzJxWpunkloqG19STvWMptbcZaKjiZCXGW_7kHejcJE16tVY2EfKSZeCdeJPYqQz4ywT7deAFW6nwsiHQQKBxM7L_5YjvjTuJlkKKhYWurK1GZtTlRX4JKKAP0Czy4_boo8FuaPDJVwBP6gFu1ZgbNKi9hYNp75FNSf_ZGTJ0cX4bTRo5hOp2fFrBfqQ1M7wy3Z4rwCqXEkhGlIB3zNgfTBA0di48zTB06Wt8mPrkt0nmbI7gMCxqxR0vr32ROUmJnX9gys-wQnO8Hc8EVWigWmEA8qlq-ItNutEmoF3kuLhwAUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAq8FGbTUahtud22wvH5XR7BmIDO0mQ6h8RP2kvpsZTYXFJex6yFLvM1DArpTC0RsaS4R4db8b0b2HYDHjv3taadj5V02D0sqhwxDKtK_ghJj5jf7wasLD1BkywAHw8mJ3cFhK37B9fsyLmvGActiZX418WfXYsSBPnBSSyadr3DzZ7FSmvx1WH_e1RMAZrVl89CapNbgVMa68bvsqd16vW_bBYT9VSPnRj_fvTMFpSI_KRDQyegV3MKTxGWsDnfUyHvGVucFmFXY_JWM7w6wnKQ-FaEfR4Yl_MErvoU_hb3xQfPcR1PELHcsoVfqM_LFsehvl7SACc9bL61noR1uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در اعتراض به قانون ممنوعیت حجاب دختران در مدارس اتریش، زنان و مردان با حجاب در اعتراضات حاضر شدند
🔹
موج اعتراض‌ها روزبه‌روز گسترده‌تر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/687126" target="_blank">📅 13:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
حسن روحانی: صداوسـیما باید ملی شود؛ از رئیس‌جمهور تا مردم نمی‌خواهند این صـداوسیما را ببینند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/687125" target="_blank">📅 13:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687122">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a812884e.mp4?token=pYOCd5_uiFR09gdtb9iqMARB-QveAQdbyzTPXnRCUB-xbMBjbw4KgF7JMig5diXTAkw0tknO049ZAWIpdCZ7M5twEgL7U_I684R8T1NYu3_728MbbAgc1x26py-MBWZd43six7bzvrp6I-ZcKHAOObb336OxYHXVn8Ti_IlAEbIizbNeig-fRPjpU68pzxWty2kbLID9Uh5aDjOZl0BMZJ9mAksHoPv6zCtQxO5zeQRW7RV_2JnZisVEq_ATAYW3xjdyNh4fxi7tYFM3s_34JXXyIdWTqNTGaUQOqG5DTdwTb3hgSU_mxoSqOPhrX7VRH0OoLP3ROcu0YJd29XmMwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a812884e.mp4?token=pYOCd5_uiFR09gdtb9iqMARB-QveAQdbyzTPXnRCUB-xbMBjbw4KgF7JMig5diXTAkw0tknO049ZAWIpdCZ7M5twEgL7U_I684R8T1NYu3_728MbbAgc1x26py-MBWZd43six7bzvrp6I-ZcKHAOObb336OxYHXVn8Ti_IlAEbIizbNeig-fRPjpU68pzxWty2kbLID9Uh5aDjOZl0BMZJ9mAksHoPv6zCtQxO5zeQRW7RV_2JnZisVEq_ATAYW3xjdyNh4fxi7tYFM3s_34JXXyIdWTqNTGaUQOqG5DTdwTb3hgSU_mxoSqOPhrX7VRH0OoLP3ROcu0YJd29XmMwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رخ عمودی شگفت‌انگیز K2
🔹
قله K2 با ارتفاع ۸۶۱۱ متر در رشته‌کوه قراقروم، دومین قله بلند جهان پس از اورست است و به‌دلیل مسیرهای بسیار دشوارش شهرت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/687122" target="_blank">📅 12:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687121">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
طلا دوباره آماده جهش می‌شود؟
🔹
تصمیم جدید خزانه‌داری آمریکا برای دو برابر کردن بازخرید اوراق بدهی بلندمدت، موج تازه‌ای از توجه را به بازار طلا آورده است.
🔹
شورای جهانی طلا می‌گوید این اقدام دقیقاً «چاپ پول» یا QE نیست، اما می‌تواند دلار را تحت فشار قرار دهد و نرخ بهره واقعی را پایین بیاورد، دو عاملی که معمولاً به نفع طلا هستند.
🔹
از طرف دیگر، رشد سنگین بدهی آمریکا و نگرانی درباره وضعیت اقتصاد جهانی باعث شده سرمایه‌گذاران دوباره به طلا به‌عنوان پناهگاه امن نگاه کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/687121" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687119">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15209ee1b.mp4?token=GHV8pLiFm35kVGadv6tq_WbyZ3JiBRAGfmXKgSyTt99v0zdx_jManpviO6Zhe0EqOuAC8M9sfuV0aokjK4uHjEKYxFb95twRP_OVgXjUAaH0iShk4Hu9cxn7ixkoFX0WskZQ5E206tmzRM0_XGLrkP6ycgWxNTfJs7hJo5Bt2g0D_r6XHax63e8Ps7TiUJ_iPAMPv22FPp7UKSZZ2eHC923CCUH5lfakgJZRSxhwrjVaDyJKDyo6i3E7orRBSlmU9sjXyjUg55tV-15RgMtRWP8ZDqa4np8oNgXeRgffimEiCUiuUmOBYyaHEdHg4t9yG4p6-P8rKdhC77lT0JcXww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15209ee1b.mp4?token=GHV8pLiFm35kVGadv6tq_WbyZ3JiBRAGfmXKgSyTt99v0zdx_jManpviO6Zhe0EqOuAC8M9sfuV0aokjK4uHjEKYxFb95twRP_OVgXjUAaH0iShk4Hu9cxn7ixkoFX0WskZQ5E206tmzRM0_XGLrkP6ycgWxNTfJs7hJo5Bt2g0D_r6XHax63e8Ps7TiUJ_iPAMPv22FPp7UKSZZ2eHC923CCUH5lfakgJZRSxhwrjVaDyJKDyo6i3E7orRBSlmU9sjXyjUg55tV-15RgMtRWP8ZDqa4np8oNgXeRgffimEiCUiuUmOBYyaHEdHg4t9yG4p6-P8rKdhC77lT0JcXww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تسلا تاکسی‌های خودران Cybercab را در بخش‌هایی از آستین تگزاس راه‌اندازی کرد؛ این خودروهای دونفره فاقد فرمان و پدال هستند
🚕
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687119" target="_blank">📅 12:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687118">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده پدافند ارتش: فناوری پیشرفته دشمن، تضمین‌کننده بازگشت هواپیماهایش نیست.
🔹
کره جنوبی: تصمیمی برای اعزام نیرو به هرمز گرفته نشده است.
🔹
گرمای بی‌سابقه در فرانسه جان ۷ هزار نفر را گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/687118" target="_blank">📅 12:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687116">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3a7636f1.mp4?token=livCp3YvaZzojdRH67ZnWp59W464kDs-0UpGAcedFubLmEphPdBZgatP3orjNu85LSuLuU3Z0hZDOyvYWwVS67JRHGEXWHEtuJuv3KO7RCi2LmPbwyVDZ_sHm8CoCu5yTcwBSBOBRPcV9VK1uEVmJMr3G8MIFniy_2-JlpHoP-Oj5zCFcQ9HUOteHBPQZvrvplXw126dnj5eOEHIV1h5QSw39xyaZDj-2oPcAYQhna4Ylm3kQiDeN9UqnFUoinfO5cAG0N1mCEEtLCetNvCpap9OR8-B7Xgaa7eadcnadkSpIjRmclbQke8W-Y-CjPzadGIrQC9nU1SYZirXttbDDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3a7636f1.mp4?token=livCp3YvaZzojdRH67ZnWp59W464kDs-0UpGAcedFubLmEphPdBZgatP3orjNu85LSuLuU3Z0hZDOyvYWwVS67JRHGEXWHEtuJuv3KO7RCi2LmPbwyVDZ_sHm8CoCu5yTcwBSBOBRPcV9VK1uEVmJMr3G8MIFniy_2-JlpHoP-Oj5zCFcQ9HUOteHBPQZvrvplXw126dnj5eOEHIV1h5QSw39xyaZDj-2oPcAYQhna4Ylm3kQiDeN9UqnFUoinfO5cAG0N1mCEEtLCetNvCpap9OR8-B7Xgaa7eadcnadkSpIjRmclbQke8W-Y-CjPzadGIrQC9nU1SYZirXttbDDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروسازی که از دوطرف می‌خواهد از مردم سود بگیرد/ آیین نامه دولت را که حق مردم در آن دیده نشد بود از دستور کار خارج کردیم
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
بودجه‌ای در کشور بابت یک قانونی (در خصوص خودرو) وجود دارد دولت باید مشخصاً آن بودجه را به مردم بدهد؛ نه به خودروسازی که از دوطرف میخواهد از مردم سود بگیرد.
🔹
نظر ما در مجلس با قاطعیت این است که این پول و بودجه که از منابع بیت المال است باید به آحاد مردم برسد.
🔹
همین که توانستیم یکی از آیین نامه‌های دولت را از دستور کار خارج کنیم که در آن اصلا حق مردم دیده نشده بود، و الان آیین نامه جدید را که ببینید یعنی زور ما رسیده است؛ البته این کار تقریبا به انتها رسیده و هنوز ده تا پانزده درصد دیگر وجود دارد که باید کار آن انجام شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/687116" target="_blank">📅 12:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687115">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f56b44f1.mp4?token=sXdPCVVbBVMqAOSxyiVt0IA8YyBRZjT3EHRSHT-Dn6NhE83Xu-W9wwVw8kfruHOmLHeOPS5pBS82XZWhLVzxYFp0JRrCdN-P0zsButxtc36Wt9cQm7-BrWlf_HuC0mSvuQCGvLbh1Y7TVUkXrwS_xKlrRWVYB9GndK_vyNtT-i_ov_nQ9kXEldxiq_InFh6dT0kmgMeJR6vJu-DfXN62hEgQxP-zmvBd-_KG7t35ItidpYbqM6yszdee1C0MAZn1zCfCF1LtsHLgFLJn7ZLYH_avVHzTpRwlnACLZOyr7_eoxd1g-omITQQMIvFExmSRVUfJ6mT46T7goKq0d4SjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f56b44f1.mp4?token=sXdPCVVbBVMqAOSxyiVt0IA8YyBRZjT3EHRSHT-Dn6NhE83Xu-W9wwVw8kfruHOmLHeOPS5pBS82XZWhLVzxYFp0JRrCdN-P0zsButxtc36Wt9cQm7-BrWlf_HuC0mSvuQCGvLbh1Y7TVUkXrwS_xKlrRWVYB9GndK_vyNtT-i_ov_nQ9kXEldxiq_InFh6dT0kmgMeJR6vJu-DfXN62hEgQxP-zmvBd-_KG7t35ItidpYbqM6yszdee1C0MAZn1zCfCF1LtsHLgFLJn7ZLYH_avVHzTpRwlnACLZOyr7_eoxd1g-omITQQMIvFExmSRVUfJ6mT46T7goKq0d4SjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سونی ربات میکروجراح خود را با دوختن سطح یک دانه ذرت آزمایش کرد
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/687115" target="_blank">📅 12:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687113">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
تلاش عمان و قطر برای آغاز چارچوب جدید مذاکرات ایران و امریکا
🔹
فایننشال‌تایمز از تلاش میانجیگران عمانی و قطری برای تدوین چارچوبی جدید برای مذاکرات میان ایران و امریکا با هدف مدیریت بحران میان دو کشور خبر داد./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/687113" target="_blank">📅 11:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d791cc65d.mp4?token=oINMObo3u_j06S8bN1xQ4bQeCllDd2LlmgALxnmL008USvqpxClS8l_DkXffBfwM8d9npAIskduqDwEcbjKkl3IzluShtV6VTUsh-jOlJoc43jl_7SNbc3EIe5-gg7r68lboNH7-jH87vGIc5SW8nCToZcRpP8-TEVN-NGtqhsIGLMqdWvT3Dm0Pc5hDIlzakYYcL66LCanovToQ549Tk64OAHUEDYy25WQ1P7gK6DI2ui_36_E8lnkuj1SP8_GpLLI1xM15WMldUPxdOmwGOmZZFuw1FA9TJngSXTldtkpyBi5y0JJwYTuCo65FnPZnB8hw4L28WBTMoQUUymdqAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d791cc65d.mp4?token=oINMObo3u_j06S8bN1xQ4bQeCllDd2LlmgALxnmL008USvqpxClS8l_DkXffBfwM8d9npAIskduqDwEcbjKkl3IzluShtV6VTUsh-jOlJoc43jl_7SNbc3EIe5-gg7r68lboNH7-jH87vGIc5SW8nCToZcRpP8-TEVN-NGtqhsIGLMqdWvT3Dm0Pc5hDIlzakYYcL66LCanovToQ549Tk64OAHUEDYy25WQ1P7gK6DI2ui_36_E8lnkuj1SP8_GpLLI1xM15WMldUPxdOmwGOmZZFuw1FA9TJngSXTldtkpyBi5y0JJwYTuCo65FnPZnB8hw4L28WBTMoQUUymdqAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید لحظه وقوع سیل در نپال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/687112" target="_blank">📅 11:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیر عامل پالایشگاه تهران از راه‌اندازی واحد CCR که تولید بنزین کشور را روزانه ۱.۵ میلیون لیتر افزایش می‌دهد خبر داد.
🔹
صندوق بین‌المللی پول: اقتصاد امارات وارد مرحله خطر و کسری تجاری شده است.
🔹
فقط ۴ نفتکش از تنگه هرمز در روز پنج‌شنبه عبور کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/687111" target="_blank">📅 11:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687110">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
افزایش شمار نظامیان آمریکایی زخمی در جنگ ایران به ۷۶۷ نفر
ای‌بی‌سی نیوز:
🔹
بر اساس به‌روزرسانی ‌های انجام شده از سوی وزارت جنگ آمریکا (پنتاگون) که طی ۲۴ ساعت گذشته انجام شده، شمار نیروهای آمریکایی زخمی‌شده در جنگ با ایران به ۷۶۷ نفر افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687110" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687107">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuOczDEQGQmIKNNHvWnHVNH9UQngSwG-SZAoMOtlccAA4TyotT-0aezyc_y7uNi99SQHVXUPaoUIzKRIPbpBqNCDYsbWBRZjrI8t8Qd3kLSA5T2iYqGXA2WZzXiqW01YVVGvjeScQPD8LHV55acT44O9tpyszo_rWUjRv-ZIDxhEBrWL7rOQika5cI7QAkhCjXAfvS3HWxZtIrHrLf54D6PzW5DJrElQP6cqyQNYGoqx58dejmp4_sDRImCrPEjFi43BCQtsCPAhrnN-iQk4fzYJru-6IM_Ec9bJeEav5ZYfb-_PIjhW5_UWNQHK_6YZaIvTs74ZypLSf4MC7Dp2_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hmue9yMlsVdHQD9NeaW0oBvPnwmPnAFeqkYOgCj9JsxXm_UdEA80X3A4wphbPNnraSdnYc8ACGfsx-mGRyWo1FF7YnyRQsCqjfp5i_0BY55zN5jotkK55G-kiL2iP4siKNqWSfM0-Vk4Iqdb8GIyoZkt_W1OymPaAR_LwtPysidQDhhT4cwAIYhN_uG6gsycvVntTCRBQLY37TXo1F3-yqp4bawoXgn5tBu-VnTPNnh9VA-ehRXgUIArvQcWxq5JXYp1qs9G0loEStIdwrIMztbEQvDc751m0IqJ0au-omqafu1WeDu-jhG1OyzeITlZAMk-r1Ojh2ddrRId4fm9wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced1356087.mp4?token=kNkZmax53dvHriw1DEydK6JeRUnA5yxH_8KRjn97EA4LCucwF05opdh2Gme8TJOCKA8KBxl047ULKJkwFsN5ZV18tPEud9yS5r7CpvmInFoVuEH0vNDDD5MfjO4MVMlDJiMtsuGayzKlEdkCryaDcaUC6vd02VGGT84a15zoPwO7PyAWu7P_zySLImYdZNubq-Shuqc1-UGpkBdifKdm6pz0CoTnLK66GhW5uKwk1ns6qUlxSAFSvt0uqTb8KrROhYGlfQx6AVkHx8L-kxuv3OR737xymIoEDEo25U_4Bq08z3Qy58ln_nOtkMAEzk40VA02WQUONjbV-N5sMDBJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced1356087.mp4?token=kNkZmax53dvHriw1DEydK6JeRUnA5yxH_8KRjn97EA4LCucwF05opdh2Gme8TJOCKA8KBxl047ULKJkwFsN5ZV18tPEud9yS5r7CpvmInFoVuEH0vNDDD5MfjO4MVMlDJiMtsuGayzKlEdkCryaDcaUC6vd02VGGT84a15zoPwO7PyAWu7P_zySLImYdZNubq-Shuqc1-UGpkBdifKdm6pz0CoTnLK66GhW5uKwk1ns6qUlxSAFSvt0uqTb8KrROhYGlfQx6AVkHx8L-kxuv3OR737xymIoEDEo25U_4Bq08z3Qy58ln_nOtkMAEzk40VA02WQUONjbV-N5sMDBJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه عجیب برای هواپیمای مسافربری ایندیگو در فرودگاه سرینگر
🔹
هواپیمایی هنگام پارک با تیرک سامانه هدایت برخورد کرد و آسیب دید، اما همه مسافران و خدمه سالم ماندند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/687107" target="_blank">📅 11:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLca6cxZyA8EcHyMPhpjU31xnV9a6-9FWuboSMnarLXde3JxB8-zuuqbhijmY_Gm7TEKnoztFuSMoSnjxQVTlRUgRfutRdlC-ImCs5REOKfkqbU5wj94hLSdDUKytzRoXCqdMZOfkyNezlFWd47S_D9ulR-MyEfD_Im1xhJtEBQF-p_pt_IB0WxpDfhiY_EvZKUY4yScvUie2zBcqg9hfFAiT_oWfnYKtKJ71YWeU9h-4YtNTADG-31-YnXNOidPQ7YYz_whzx3YW11ji3oCRrwC80bCDSboPZCNjmtL9OlaxUzYfZwCffF6CEEscdnwPwJmV3y0t07_r2LAy27DwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر امور خارجه کشورمان به اظهارات اخیر همتای اردنی؛ ایران برای پاسخ به متجاوز چقدر باید منتظر باشد؟!
🔹
به نظر وزیر امور خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟
🔹
آیا او واقعاً از این موضوع بی‌اطلاع است که در نخستین حملات آمریکا، از حریم هوایی، خاک و آبی کشورهای عربی استفاده شد؛ حملاتی که به کشته شدن ایرانیان بی‌گناه انجامید؟
🔹
ادعای وزیر خارجه اردن: حمله ایرانی‌ها واکنشی نبود، چون دو ساعت بعد از آغاز جنگ حمله کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/687106" target="_blank">📅 11:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ca2b9ae4.mp4?token=j_g9-w1_MXyXJdgpRIgP7lZaWfmQg4hdWiPPAqOf6gfjL_mKjFNXMcIgbHb9lEs62JLTjvLA2_ogranIrBsJ1cXAOIvIEGoX0sNFzYrKD1eLppQsKXmTFipQtFE5Z590Gv9wK4K4yns1BgNjNY7YmBdWiSQGdzDsKtNL8YoOH-jC04xKpDyHtV-QECeMV9ac2Fx0jwSPOkPZgnoa2KUKRzb0iMOv07rSEvlOS__mroSQ0BLc6GQaDjIOzmST-bqLHTUeP2qkqOGEUCilxizr1NMlH1Afn1LjlcCMxB46IVRgMXh-FUN-Ic5SIKYydu7kEHQn_FcIZUKnH7w_h8oYQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ca2b9ae4.mp4?token=j_g9-w1_MXyXJdgpRIgP7lZaWfmQg4hdWiPPAqOf6gfjL_mKjFNXMcIgbHb9lEs62JLTjvLA2_ogranIrBsJ1cXAOIvIEGoX0sNFzYrKD1eLppQsKXmTFipQtFE5Z590Gv9wK4K4yns1BgNjNY7YmBdWiSQGdzDsKtNL8YoOH-jC04xKpDyHtV-QECeMV9ac2Fx0jwSPOkPZgnoa2KUKRzb0iMOv07rSEvlOS__mroSQ0BLc6GQaDjIOzmST-bqLHTUeP2qkqOGEUCilxizr1NMlH1Afn1LjlcCMxB46IVRgMXh-FUN-Ic5SIKYydu7kEHQn_FcIZUKnH7w_h8oYQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقابله با عریان سازی نگرانی زنان با پوشش‌های متفاوت است؛ نه صرفا زنان محجبه
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از مطالبات مهم زنان این روزها بحث به سامان شدن اقتصاد خانواده‌ها است.‌
🔹
همچنین مقابله با عریان سازی‌ است که دارد اتفاق می‌افتد؛ جالب اینجاست که خانم‌ها با پوشش‌های متفاوت این اظهار نگرانی را داشتند. نگرانی در این راستا صرفا مختص زنان محجبه نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/687105" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687104">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a98fd41f19.mp4?token=ID5eJyYU7ykeyFZJYeFN0TV9bupp_igNWyXL6jBPqhCCuUjraXdzOgaSTC7b3NJyKt_Qu4lumGpROJphpucVdFIh88-vo3uQw6PahjV93hzDuU91CDomVukeA0hJT8w-F9KB1AYZHBnvHzZZuThiFYeLIVXBcDQKrh9nLj3pfKLcctbrMS9JFFHvrCLchAzRz_67w-OdmSmJpOpFK-ntbiyfdCX-_1ntfBCOqvrWwQLWzN3g8ZWQ7XITIRYQMc_N5VVN7CXC2SJfuSh6Mf70lb74xC2n4R5XxPDc5tRgH2I6qqUChlx8dpLCo5GFn3o2iyhmVtJ2O8FZ1-hdO78AQClSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a98fd41f19.mp4?token=ID5eJyYU7ykeyFZJYeFN0TV9bupp_igNWyXL6jBPqhCCuUjraXdzOgaSTC7b3NJyKt_Qu4lumGpROJphpucVdFIh88-vo3uQw6PahjV93hzDuU91CDomVukeA0hJT8w-F9KB1AYZHBnvHzZZuThiFYeLIVXBcDQKrh9nLj3pfKLcctbrMS9JFFHvrCLchAzRz_67w-OdmSmJpOpFK-ntbiyfdCX-_1ntfBCOqvrWwQLWzN3g8ZWQ7XITIRYQMc_N5VVN7CXC2SJfuSh6Mf70lb74xC2n4R5XxPDc5tRgH2I6qqUChlx8dpLCo5GFn3o2iyhmVtJ2O8FZ1-hdO78AQClSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد وحشتناک قطار با کامیون در لهستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/687104" target="_blank">📅 10:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687103">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72545c257.mp4?token=LYtBv2ydOb1aatu91SXmupseUMx6iJZDzYR6kK_oJwp3rgJIlPaTpVJk71PlQVgJUcy9W5tEOMVGYlKquKit9RgLbWW3exoURg3zuNdYCbQs8tD0uxX-CrdmKUUEvVbvjQBXYQsU577OuPVV8K6uu3Bcu2xdfuvjjweLsz1jiXZ47_vMkscC9JCLkKVfPubGilLnBjK1BvgXzCf_wIHxq7juoSK0Hzg_LEiBB1BNnk0h82ZRAmHUdD6wR3LyxYawevRehtkeDiCD1D86ufz5yGBHI0S43cpwYjkU3hf949OIalyPewVD9HgdI-fYACwwzvBkrkgfGnrqEOekats6bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72545c257.mp4?token=LYtBv2ydOb1aatu91SXmupseUMx6iJZDzYR6kK_oJwp3rgJIlPaTpVJk71PlQVgJUcy9W5tEOMVGYlKquKit9RgLbWW3exoURg3zuNdYCbQs8tD0uxX-CrdmKUUEvVbvjQBXYQsU577OuPVV8K6uu3Bcu2xdfuvjjweLsz1jiXZ47_vMkscC9JCLkKVfPubGilLnBjK1BvgXzCf_wIHxq7juoSK0Hzg_LEiBB1BNnk0h82ZRAmHUdD6wR3LyxYawevRehtkeDiCD1D86ufz5yGBHI0S43cpwYjkU3hf949OIalyPewVD9HgdI-fYACwwzvBkrkgfGnrqEOekats6bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت صحنه لوکس‌ترین مرسدس‌ها؛ جایی که طراحی خودرو هنوز با دست انجام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/687103" target="_blank">📅 10:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687102">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
اولین جمله رهبر انقلاب پس از بیرون آمدن از زیر آوار بمباران
فریدالدین حداد عادل:
🔹
موقعی که زخمی از زیر آوار بیرون آمدند، گفته بودند: من نمی‌روم تا تکلیف خانمم معلوم شود. نهایتاً به بهانه‌ خطرات امنیتی و احتمال بمباران دوباره، ایشان را از آنجا بردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/687102" target="_blank">📅 10:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc132b42.mp4?token=Q7XlTPsSQFZA2ZopKpfN12SAmukX5S_2_7WCCbeEp-FAVghqbyCPHAvrfnYLLbjisGJcFHrOr9JCJclS-kKOjG61BE7PuoHBNLg5ced-TDbQ9TGujHN7V8lEF_mBjiY8rGU2US6ABvBWhPA9kH7cehozOs-bqo4stIZqJNGk9CbKnQB2EOtzzOKYbR-WhgaxMg8ft9JeZE87HqJKOs1ybC3A5daePyrirKcTmCJngAQlR2L2nKedTKlGmMLynyH-TEl_ID_idIQsQWjoYhGw9boRObgk1qwCJWEgV-Np0MuE1udXEWRDW_U9fnJrztjnbeHbpgFDUNBSSM1uEtOkgVixw0lfNVue3nETqf-OB3db_HGq7BS0G6tRMMfxqyQvBFWfP4mW3bzP3SXO7gSM66kE5YN0lZnvsXlQY7zEsU2GT4EJaXNFpp2kIRLALbreQJdHboukoSPlfxU3TaPtwKNYhgFQ_GUU89LlkhPluWblw9434JmpNPQYju76xb3t3ies43m9XHXucnh-wYezhM029S_qdQdNGhhfOU4ufpqyhXlhbsDIUkJ8Q8OJx7iOfTxxqgtv0TETqgXb4vtZdlLLJWqx1-XzzLXvE2_nEgUrbDPq6_bxoLK4wkVc9OWMutsLI-Xa-UQWJL-dFWRZEN8tnF491mnm006qk1F84Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc132b42.mp4?token=Q7XlTPsSQFZA2ZopKpfN12SAmukX5S_2_7WCCbeEp-FAVghqbyCPHAvrfnYLLbjisGJcFHrOr9JCJclS-kKOjG61BE7PuoHBNLg5ced-TDbQ9TGujHN7V8lEF_mBjiY8rGU2US6ABvBWhPA9kH7cehozOs-bqo4stIZqJNGk9CbKnQB2EOtzzOKYbR-WhgaxMg8ft9JeZE87HqJKOs1ybC3A5daePyrirKcTmCJngAQlR2L2nKedTKlGmMLynyH-TEl_ID_idIQsQWjoYhGw9boRObgk1qwCJWEgV-Np0MuE1udXEWRDW_U9fnJrztjnbeHbpgFDUNBSSM1uEtOkgVixw0lfNVue3nETqf-OB3db_HGq7BS0G6tRMMfxqyQvBFWfP4mW3bzP3SXO7gSM66kE5YN0lZnvsXlQY7zEsU2GT4EJaXNFpp2kIRLALbreQJdHboukoSPlfxU3TaPtwKNYhgFQ_GUU89LlkhPluWblw9434JmpNPQYju76xb3t3ies43m9XHXucnh-wYezhM029S_qdQdNGhhfOU4ufpqyhXlhbsDIUkJ8Q8OJx7iOfTxxqgtv0TETqgXb4vtZdlLLJWqx1-XzzLXvE2_nEgUrbDPq6_bxoLK4wkVc9OWMutsLI-Xa-UQWJL-dFWRZEN8tnF491mnm006qk1F84Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رول سیب‌زمینی پنیری؛ ترد، کش‌دار و بی‌نظیر
😍
😋
مواد لازم:
🥔
سیب‌زمینی پخته
🧀
پنیر موزارلا
🌶️
فلفل قرمز (پودر)
🫑
فلفل سبز
🧂
نمک
🍋
آب لیمو
🍞
نان تست
🛢️
روغن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/687100" target="_blank">📅 10:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687098">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cd469101.mp4?token=lxfFYiNp0j0w08Hwt8fbojJNZc88FLFLL2WXigCULQMjKIkUSJaX1xGej6EEDwd9S6snXcgeLKpL5ot95euevf7Y8AfW-Z8eqYLsmUz0ruKJw5opF7WC1TAIsw5pR5AELNMEBgAr3Yvl5XgVxq5w2rRlUk2zHV9M7xMZ7TNGEnyXyxWFGZp9K0MO9ugm2nFCb31vQEJNj-YxpgXcQ45kVWbJOkvAWSNCY3oE6LRDsuE0o_YASaQn9VqarHoLJPbPirvY7hpDp_PQRzpwQC11s6Stuqg9ZC5023DOllo2ZHQYz9Ev4HubTIXUkyDQKQDLoj8DvGlTSNz62tJJaLuXLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cd469101.mp4?token=lxfFYiNp0j0w08Hwt8fbojJNZc88FLFLL2WXigCULQMjKIkUSJaX1xGej6EEDwd9S6snXcgeLKpL5ot95euevf7Y8AfW-Z8eqYLsmUz0ruKJw5opF7WC1TAIsw5pR5AELNMEBgAr3Yvl5XgVxq5w2rRlUk2zHV9M7xMZ7TNGEnyXyxWFGZp9K0MO9ugm2nFCb31vQEJNj-YxpgXcQ45kVWbJOkvAWSNCY3oE6LRDsuE0o_YASaQn9VqarHoLJPbPirvY7hpDp_PQRzpwQC11s6Stuqg9ZC5023DOllo2ZHQYz9Ev4HubTIXUkyDQKQDLoj8DvGlTSNz62tJJaLuXLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمل شتر ۴۰۰ کیلویی توسط فرامرز رحمانی در آیتم پایانی قوی‌ترین مردان بازی‌های جهانی عشایری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/687098" target="_blank">📅 10:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687096">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
اهمیت احراز هویت و اصالت سنجی قبل از خرید در فضای مجازی
رئیس پلیس فتای فراجا:
🔹
ناشناس بودن هویت افراد در فضای مجازی علی‌الخصوص پلتفرم‌های خارجی، اولین، آخرین و مهم‌ترین مشکلی است که ما در حال حاضر داریم.
🔹
توصیه می‌کنیم قبل از خرید، از احراز هویت صحیح فروشنده مطمئن شوید و اطلاعات فرد را در همان سایت یا اپلیکشین بررسی کنید.
🔹
هوش مصنوعی در حال حاضر در جرائم‌هایی مانند مزاحمت‌های اینترنتی، اخبار، تصاویر و رسیدهای جعلی استفاده می‌شود، اما تعداد این پرونده‌ها در حال حاضر زیاد نیست./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/687096" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687095">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس دیوان عالی چین: ایران و چین با وجود مسائل منطقه‌ای، همواره از روابط سالم و پایدار برخوردار بوده‌اند
🔹
هشدار سازمان ملل: گرمایش زمین در چند سال آینده از آستانه ۱.۵ درجه عبور می‌کند
🔹
مرکز لرزه‌نگاری کشوری: ۸۱ زمین‌لرزه در هفته نخست شهریور ۱۴۰۵ ثبت گردیده است
🔹
فارن پالسی: چین از فشار اقتصادی ترامپ علیه ایران هراسی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/687095" target="_blank">📅 09:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687094">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10708a381.mp4?token=AGwrGOv3DiS-6HHoRjemTWLWA1WWDvsvs75LaOXwQz0tOR-cVSKTUOKHi0FqVhw47YE4PH3wtbtM7oxtp0T9ZIVjNmnAMageT1KZ2IP_ZrLbxQPlxPsdfNmhlRmx2uTn2w0MpeI0g86hz44luOl85A3KkQ7BfxaZK0zJ44tdACGUOeM6jnnYJsI5BkHyLfcGMfMykeAIxlEG1dAzdRS-xt3ArydqYpuWSfu4JEXee2nMG3CipFTVXCN8PaaSyG1hlGErYMsDoFrNfgjbcmZMIxxloBMzZcyXv9J5lxe3XXQKgaPp2L7MG4eKua1z_xPvgQW9KI2fbHSOcPsoWGwMsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10708a381.mp4?token=AGwrGOv3DiS-6HHoRjemTWLWA1WWDvsvs75LaOXwQz0tOR-cVSKTUOKHi0FqVhw47YE4PH3wtbtM7oxtp0T9ZIVjNmnAMageT1KZ2IP_ZrLbxQPlxPsdfNmhlRmx2uTn2w0MpeI0g86hz44luOl85A3KkQ7BfxaZK0zJ44tdACGUOeM6jnnYJsI5BkHyLfcGMfMykeAIxlEG1dAzdRS-xt3ArydqYpuWSfu4JEXee2nMG3CipFTVXCN8PaaSyG1hlGErYMsDoFrNfgjbcmZMIxxloBMzZcyXv9J5lxe3XXQKgaPp2L7MG4eKua1z_xPvgQW9KI2fbHSOcPsoWGwMsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات‌ها ورزشکار شدند؛ حرکات آکروباتیک خیره‌کننده ربات انسان‌نما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/687094" target="_blank">📅 09:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687093">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0800fdef7.mp4?token=f_AOpBJmqZlHEWXfuSpdgzqcGqm5uX7zUyVUunqmOBVw68CYMJNM6RLUa2_HDTOezTOMnbF-CtJlVBCbyq7lGwLvys2e1nCfaPFcwhv5wSSk6-VGBOjhZ_nsLdsQXPFnWMGaeAyWWlT8GWd6WWWgU7zP4fJhuikntgvELdlSz1jMa_hlniRsfbmupSR7u_kKk0sKI5YlwP-vPHyTwayH9eBwsL03JZxigMclKN0Y_F7EBSgGSgX-aVkeUned4CwNCADDVecX8BymvRJSnFj4pp7P34wiCidn6ijzxZY11zbqsY3s1ybPTE8vP5hD6DnFng1xC7x53NQQEwf2MydbWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0800fdef7.mp4?token=f_AOpBJmqZlHEWXfuSpdgzqcGqm5uX7zUyVUunqmOBVw68CYMJNM6RLUa2_HDTOezTOMnbF-CtJlVBCbyq7lGwLvys2e1nCfaPFcwhv5wSSk6-VGBOjhZ_nsLdsQXPFnWMGaeAyWWlT8GWd6WWWgU7zP4fJhuikntgvELdlSz1jMa_hlniRsfbmupSR7u_kKk0sKI5YlwP-vPHyTwayH9eBwsL03JZxigMclKN0Y_F7EBSgGSgX-aVkeUned4CwNCADDVecX8BymvRJSnFj4pp7P34wiCidn6ijzxZY11zbqsY3s1ybPTE8vP5hD6DnFng1xC7x53NQQEwf2MydbWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواشناسی: سامانه بارشی یکشنبه وارد کشور می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/687093" target="_blank">📅 09:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687092">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773498a3c5.mp4?token=K_3kVc5RXWC9ko5MlWL31dNk3vMsGBzqmfCGETE39uKfjtVrCUpPb1iFnl9OO8K1LC9QPHsN6yUCw2w5yiHNKuIPeGPGiZlvVvkj-rWVmqsHGo1J-IXz_fRTA0erERxoN1SGgecvQanufNKQ3BfY97f6y9g65A4jq4RXlF1oev6jaMZ98HW7AEzaQi30AzmoxT_qsA6moqYAewM5w08OV1XQZtdozj66yqu7g8kSKAY-_kGy0VittDGgEeEtdj4SWWoUO5J5pxYruTFt8PiUpJAH3azS6uxw5LTnMy5WqyQddLCMx8iEa8COu-uEzKBBwwsIi0D3eCGMuHcNboNIng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773498a3c5.mp4?token=K_3kVc5RXWC9ko5MlWL31dNk3vMsGBzqmfCGETE39uKfjtVrCUpPb1iFnl9OO8K1LC9QPHsN6yUCw2w5yiHNKuIPeGPGiZlvVvkj-rWVmqsHGo1J-IXz_fRTA0erERxoN1SGgecvQanufNKQ3BfY97f6y9g65A4jq4RXlF1oev6jaMZ98HW7AEzaQi30AzmoxT_qsA6moqYAewM5w08OV1XQZtdozj66yqu7g8kSKAY-_kGy0VittDGgEeEtdj4SWWoUO5J5pxYruTFt8PiUpJAH3azS6uxw5LTnMy5WqyQddLCMx8iEa8COu-uEzKBBwwsIi0D3eCGMuHcNboNIng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوچ وحشی بر فراز کوه‌های بافق خودنمایی کرد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/687092" target="_blank">📅 09:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lhor6esi2TEZiqvkI7db84p5qQGxa5l5sTP42PNBxvNjNp1edPIar3Gaok5xW-G3ZO-Ro3Es8BkOco9-dcjVLx2hOcwgv8fjix5aRMzBwZbo4jC3AXmh9Dn56NDYf6vRYFNzLrHSVT0lp4PF26YCbQYCf5lY3LMGsqmJ66ayO9Ybs1FFR45Pr4DBjmp_crUK5WURb5LsNSfGjxIC4u1WdksZc-ec1HLnVtq1a2PmUIXqYd0h-XzEQZI7gp9sBpOMxjRohwxq9LRis1pKzUHQWwKRDGg8CfaCz41L6d0fxDPpaYAaMKWofzBFkHqRid33VYzO4Jjpkq-u-djd-UIdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مفسر بریتانیایی-پاکستانی: بمباران ایران، منجی از آمریکا نمی‌سازد
مفسر سیاسی و فعال رسانه‌ای بریتانیایی-پاکستانی:
🔹
این دلقک نارنجی تصور می‌کند پس از بمباران ایران و کشته‌شدن هزاران ایرانی، مردم علیه دولت خودشان قیام می‌کنند و برای آمریکا می‌جنگند؛ درحالی‌که این همان توهم امپریالیستی است. او افزود: مردم آمریکا باید علیه این رئیس‌جمهور قیام کنند و او را از قدرت کنار بزنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/687088" target="_blank">📅 08:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687087">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: مدارس حتی در شدیدترین شرایط حضوری است
🔹
تمام امکانات و ظرفیت‌های آموزش‌وپرورش برای آغاز یک سال تحصیلی آرام، کم‌دغدغه و مناسب فراهم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/687087" target="_blank">📅 08:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687086">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
فایننشال‌تایمز: ترامپ توافقی شامل برنامۀ هسته‌ای و تنگۀ هرمز می‌خواهد
🔹
میانجی‌گران در تلاشند چارچوب مذاکرات تهران و واشنگتن برای توافقی جدید را ایجاد کنند.
🔹
به‌گزارش این نشریه، ترامپ خواهان گنجاندن تنگۀ هرمز در هر توافق احتمالی با ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/687086" target="_blank">📅 08:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687085">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzUmrO7gJzMEdBtP5NDqetshvaNyxU9uB3dcuo9NtkxzoCOMt-CYAAFQUeckgXCWyHufCESR_7RwOJHTcBp_bvJ1ZglrVJlnJhIwoL5AN0zJXXJglNgRx172sGImmYgGxQ2vi0MAMLTWyrhZ5LFy19IE8OdtbPD4FCE7YZMagOsFA9H_NRIkzSJAsue0IKPcib0N6OycMt-DIPry8UvYujhC-7_KX8_FsNUfJMNRh1_mXPAQxgHELlU08xL5j2ALXxnhxnzfxrguzh7__Xfl3ZJ1ltHPtgnLzpCcKMY9nmWgzfgNLd8YajegD2hBngH12UCaHDGpj8Ozs9mMjtdYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انیمه ژاپنی از حمله آمریکا خبیث به مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/687085" target="_blank">📅 08:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687084">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLuxgJxNWye7uNfqAU7GgM15MmEq33ytfRNhvv_Q1Whf2xz4zmetbN19XjffHcEpdaISFKesR0Ginn4Du2t1te5SWyvML637Fvh9vY81VBUPZJRvCIvapiAqftGPVvT5XobmaILiiQKuyyYS_WzKMeT0AL8D0tzVX_5Uj6y-7tks34hMeDfBRwo0biwBrf9pW2V6TONJXyeFlT5xBRakGVXUFUOrEIqhz1K2ki8cX18td21Yg2VgqfUP4KNc8e6qZers6KOqYdTLObXkKong5VGwxibnV98Xz5VyKOAWc5kyvFf5qr-UW6xE6wIO0LgTIu8mRd-CbU3J2vglnHtmeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۳ شهریور ماه
۲۲ ربیع‌الأول ۱۴۴۸
۴ سپتامبر ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/687084" target="_blank">📅 08:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687082">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
هیاهوی تبلیغاتی جدید وزیر خزانه‌داری آمریکا دربارۀ تحریم‌ها علیه ایران
🔹
وزیر خزانه‌داری آمریکا مدعی شد که اتحادیۀ اروپا رسما به روند «انزوای اقتصادی» علیه ایران پیوسته است.
🔹
اسکات بسنت بدون ارائه جزئیات بیشتری از این «موضع قوی و زودهنگام» قدردانی کرده است.
🔹
پیش از این رسانه‌های آمریکا گزارش داده بودند که جنگ اقتصادی دولت ترامپ علیه ایران، تاکنون ادامۀ همان سیاست فشار حداکثری با دوز بیشتری از هیاهو و جنجال‌های رسانه‌ای بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/687082" target="_blank">📅 03:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687081">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4bac92f47.mp4?token=UIW07X1XC6gVkfpTyyZNUHLlzPLbbVpK2aYMyoEXBP2Lekr4TsoWQqJCvkqINB_Mc6ZsIx3XVgfDVLGRAmZv8BQ68IyTF8BO8_ENTX9cRoY_JXoSRPkMeJQGRF8n27RTudrYvXTgJiwjtpNmJK7VDFbXROz8McJYNnv46NcC4L9FPmb2p5-4VbsGgvIZKDwWeKZjRCSdipUnA0V797nCe3A9bowuRdpdRTm2ySNtyYJTm4rYkCyr7CQiGkfWmWIL-NcEuULz2oVeCXfALebo-wKOF_73UViKVtyk_cWLV72ipxFqAInlKHwRVu903EXksUJEj13IbXcmnwh-BT-CmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4bac92f47.mp4?token=UIW07X1XC6gVkfpTyyZNUHLlzPLbbVpK2aYMyoEXBP2Lekr4TsoWQqJCvkqINB_Mc6ZsIx3XVgfDVLGRAmZv8BQ68IyTF8BO8_ENTX9cRoY_JXoSRPkMeJQGRF8n27RTudrYvXTgJiwjtpNmJK7VDFbXROz8McJYNnv46NcC4L9FPmb2p5-4VbsGgvIZKDwWeKZjRCSdipUnA0V797nCe3A9bowuRdpdRTm2ySNtyYJTm4rYkCyr7CQiGkfWmWIL-NcEuULz2oVeCXfALebo-wKOF_73UViKVtyk_cWLV72ipxFqAInlKHwRVu903EXksUJEj13IbXcmnwh-BT-CmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار درباره‌ اسپانیا: به بسیاری از جهات، این وضعیت بدتر از یک حمله نظامی معمولی است. آن کشور نابود خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/akhbarefori/687081" target="_blank">📅 03:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687080">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea9acc591.mp4?token=oPDRjehuNJrK9u-bw2CLuwVy6rWt_Ha_cPZG7JhXEAKrcPaLtYthi7oSbcNKM4rsQsEy-1JQ7KijT4-_OOdT3n2vCDIL7DwKEndkpmjhJHC3-zQmaXsYpHLFcZNl-8nxD-U3KIdihDapLvASR6dJkSLVp2t7JSa9kCq9Cf2CAKZK6AXLNaspyLV8R4jvRiPFNgIhiq3wiXta2JZ1YgX7-Suapapqgx-15r2yAvcwxoGmx_MoOCnbFsn6lAoTj4saQ4InpHoszvjuYvjYqpLH4JJev93OS0sfvUKsb_TIeLLjntc7rVzIUhMVOwDVe9zAnWVyb9DSUEE4g5khKjyBfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea9acc591.mp4?token=oPDRjehuNJrK9u-bw2CLuwVy6rWt_Ha_cPZG7JhXEAKrcPaLtYthi7oSbcNKM4rsQsEy-1JQ7KijT4-_OOdT3n2vCDIL7DwKEndkpmjhJHC3-zQmaXsYpHLFcZNl-8nxD-U3KIdihDapLvASR6dJkSLVp2t7JSa9kCq9Cf2CAKZK6AXLNaspyLV8R4jvRiPFNgIhiq3wiXta2JZ1YgX7-Suapapqgx-15r2yAvcwxoGmx_MoOCnbFsn6lAoTj4saQ4InpHoszvjuYvjYqpLH4JJev93OS0sfvUKsb_TIeLLjntc7rVzIUhMVOwDVe9zAnWVyb9DSUEE4g5khKjyBfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو: من به توانایی خود برای سرنگونی نظام ایران، یک بار برای همیشه، اطمینان دارم
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/687080" target="_blank">📅 03:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687079">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
ادعای نیویورک‌پست: عمان پیشنهاد ایران برای دریافت مشترک هزینه خدمات از کشتی‌های تجاری عبوری از تنگه هرمز را رد کرده است/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/akhbarefori/687079" target="_blank">📅 02:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ترامپ سرپرست جدید وزارت ارتش آمریکا را منصوب کرد
🔹
دونالد ترامپ، رئیس‌جمهور تروریست آمریکا، آدام تیل، دستیار وزیر ارتش این کشور را به‌عنوان سرپرست وزارت ارتش آمریکا منصوب کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/687078" target="_blank">📅 02:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
چند انفجار شمال عراق را لرزاند
🔹
به گزارش خبرگزاری المعلومه، همزمان با انتشار اخباری درباره شنیده شدن صدای چند انفجار، صدای پرواز پهپادها در استان اربیل شنیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/akhbarefori/687077" target="_blank">📅 01:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
سناتور آمریکایی خواستار برکناری هگست شد
🔹
«تام تیلیس» سناتور جمهوری‌خواه از ایالت کارولینای شمالی آمریکا در پیامی با انتقاد شدید از عملکرد پیت هگست وزیر جنگ ایالات متحده خواستار برکناری او شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/akhbarefori/687076" target="_blank">📅 01:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
دستور پنتاگون برای تغییر نام جنگ علیه ایران
🔹
ایمیلی از نیروی هوایی آمریکا که در ماه اوت ارسال شده و شبکه خبری سی‌بی‌اس به آن دست یافته است، نشان می‌دهد پنتاگون به نیروهای خود دستور داده بود دیگر برای اشاره به عملیات نظامی جاری آمریکا علیه ایران از عنوان «عملیات خشم حماسی» استفاده نکنند.
🔹
دلیل این دستور آن است که دونالد ترامپ سه ماه پیش در میانه درگیری‌ها با کنگره بر سر ضرب‌الاجل ۶۰ روزه برای اتمام جنگ علیه ایران مدعی شده بود که «عملیات خشم حماسی» علیه ایران روز ۵ ماه مه با آتش‌بس به پایان رسیده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/akhbarefori/687075" target="_blank">📅 01:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: ما قبلاً در جنگ با ایران پیروز شده‌ایم!  رئیس‌جمهور جنایتکار آمریکا:
🔹
با ایران، به محض اینکه پیروز شویم، که طولانی نخواهد بود، ما قبلاً پیروز شده‌ایم، زیرا آنها نمی‌توانند سلاح هسته‌ای داشته باشند.
🔹
اگر امروز ایران را ترک کنیم، ۲۵ سال طول…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/akhbarefori/687074" target="_blank">📅 01:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687073">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad8e63141.mp4?token=lO5uJgq4nxhB8VDPdNn-Gg-jyjXFwnMW4pWwW6wPXJm-xmy3hlL5zLbBm1Qg8ff2V6vs-mdl-Tf7Do-e4wIcBAYQhB0LabNZlUryS_6Mfp3RSw0shMjPiygk8YFlLUonoAitrQfB3-XWaICWUynjlrrlKMOz-WIDVhzncwIJ5vvoTN_jQGbDxF3pjNdN9SSISvH_Nqbu-xfJtHGVDTt1IwXSqMtnQrnUHKL5LaByOs3IZGYfHz5L-ydzGSRf5KnwDtPbrasb7qF3YwHnCSW_ZVpMW6SYo4kFl1nCwJSUX4I10UpkV2Bkl-zP-czPXH8Br0TriQbRgAXGFT2k_hJ0YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad8e63141.mp4?token=lO5uJgq4nxhB8VDPdNn-Gg-jyjXFwnMW4pWwW6wPXJm-xmy3hlL5zLbBm1Qg8ff2V6vs-mdl-Tf7Do-e4wIcBAYQhB0LabNZlUryS_6Mfp3RSw0shMjPiygk8YFlLUonoAitrQfB3-XWaICWUynjlrrlKMOz-WIDVhzncwIJ5vvoTN_jQGbDxF3pjNdN9SSISvH_Nqbu-xfJtHGVDTt1IwXSqMtnQrnUHKL5LaByOs3IZGYfHz5L-ydzGSRf5KnwDtPbrasb7qF3YwHnCSW_ZVpMW6SYo4kFl1nCwJSUX4I10UpkV2Bkl-zP-czPXH8Br0TriQbRgAXGFT2k_hJ0YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم همچنان به دنبال دستاوردسازی در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ مدعی شد که اگر ایالات متحده همین امروز از جنگ علیه ایران خارج شود بازسازی این کشور ۴۵ سال طول خواهد کشید.  #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/akhbarefori/687073" target="_blank">📅 01:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687072">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
طبق اعلام برخی خبرگزاری ها ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید مقامات لبنانی نرسیده است
🔹
همزمان با این ادعا، همچنان علی‌الطاهر هدف حملات هوایی و توپخانه‌ای رژیم صهیونیستی قرار دارد.
🔹
به دلیل اهمیت منطقه علی‌الطاهر، نتانیاهو هدف استفاده سیاسی و انتخاباتی از این موضوع دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/687072" target="_blank">📅 01:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687071">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f8db55a23.mp4?token=H9cdOMDYYTprFb_lAt0KyTO5dYswo4Eyinxg7aq1owooQzBeVd4rz7quXP3_0cLHnmyDVUzspejrOoWEL2HmuyCwFSx8QuD67bMxloJldI8qsdA63sEqrKsEGZ256arhiwWnVfpkAxMRbbrXwmWb_wOeWDcrgBUJ-rl8Czfu_NOZlIbus5Gnt1J_CWFvCQl0tfdI9gJQv5iIxTMtGVe549RJqfK1FBzkhmBhjN_ghooMU6nT7WIsAxStDNhIotLYaGnBwvW8_WoBMpk39aGejKgUCWBYiiFIbNb2xJUqE2kfhHU7869pB1c_yio2OJq_dY_mGxJgLMKT2McpqtJXAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f8db55a23.mp4?token=H9cdOMDYYTprFb_lAt0KyTO5dYswo4Eyinxg7aq1owooQzBeVd4rz7quXP3_0cLHnmyDVUzspejrOoWEL2HmuyCwFSx8QuD67bMxloJldI8qsdA63sEqrKsEGZ256arhiwWnVfpkAxMRbbrXwmWb_wOeWDcrgBUJ-rl8Czfu_NOZlIbus5Gnt1J_CWFvCQl0tfdI9gJQv5iIxTMtGVe549RJqfK1FBzkhmBhjN_ghooMU6nT7WIsAxStDNhIotLYaGnBwvW8_WoBMpk39aGejKgUCWBYiiFIbNb2xJUqE2kfhHU7869pB1c_yio2OJq_dY_mGxJgLMKT2McpqtJXAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اختراع جالب چینی‌ها برای تمیز کردن شیشه‌هایی که دسترسی بهشون خیلی سخت و غیرممکن
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/akhbarefori/687071" target="_blank">📅 01:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687070">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
مخالفت دولت عراق با تمدید حضور نظامیان خارجی  حیدر العبودی سخنگوی دولت عراق:
🔹
پیشنهاداتی درباره تمدید حضور نیروهای خارجی وجود داشت اما دولت با این پیشنهادها مخالفت کرد. حضور نیروهای خارجی و حتی مستشاران در خاک عراق تمدید نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/687070" target="_blank">📅 01:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اعتراف ناخواستۀ ترامپ به عدم پیروزی در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا در ماه‌های گذشته بارها مدعی شد که در جنگ علیه ایران به پیروزی رسیده است.
🔹
با وجود این او در یک لغزش زبانی جمله‌ای بر سر زبان آورد که نشان می‌دهد که حتی خودش هم به ادعاهایش در این زمینه باور ندارد.
🔹
او در سخنانی دربارۀ جنگ علیه ایران ابتدا گفت «به محض اینکه به پیروزی برسیم» اما بلافاصله سخنش را عوض کرد و گفت: «همین الان پیروز شده‌ایم.»
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/akhbarefori/687069" target="_blank">📅 01:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405e6a7140.mp4?token=PY6VQLuXWYnAG1pMGD6goqXjxITtlzYj06Ln6E9HPLXOvrhFZkrj11Cab6I6ifL2Fa5D4JYJV9j0usu68G_uJNy23FnRXZ-KCRFsmElMB6YlUiIUkbF_Rr8QyR1hoI3gLPInJvn-_RC5WYyhPszGWJuT-FCGAwaGcMapu5awbx8Cfdrqa3Rlyj6WOphiYn7o6SbfMREJ_gbGrPmsTBkpLBOnieetVBtzvHA6SoCkDagrrbj-r01OgLS2bRqgqMZzBi5qt5KVyD48JMS-Jr3Il5f3_0psdZWlMY5HtmdvXoghy7xoI-NX_QIsMxYS0ot0Qbdq3uNaWS3vnKKCgXJkhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405e6a7140.mp4?token=PY6VQLuXWYnAG1pMGD6goqXjxITtlzYj06Ln6E9HPLXOvrhFZkrj11Cab6I6ifL2Fa5D4JYJV9j0usu68G_uJNy23FnRXZ-KCRFsmElMB6YlUiIUkbF_Rr8QyR1hoI3gLPInJvn-_RC5WYyhPszGWJuT-FCGAwaGcMapu5awbx8Cfdrqa3Rlyj6WOphiYn7o6SbfMREJ_gbGrPmsTBkpLBOnieetVBtzvHA6SoCkDagrrbj-r01OgLS2bRqgqMZzBi5qt5KVyD48JMS-Jr3Il5f3_0psdZWlMY5HtmdvXoghy7xoI-NX_QIsMxYS0ot0Qbdq3uNaWS3vnKKCgXJkhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه درست کردن سس مایونز سیر خانگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/687068" target="_blank">📅 01:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687067">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای ونس: ترامپ شخصاً با رئیس‌جمهور چین صحبت کرده که به ایران امتیاز خاصی اختصاص ندهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/687067" target="_blank">📅 00:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687066">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb1538895.mp4?token=FstZE8uC5MdBHJUkdKzhJLVMG2yMMC9fGo3vd4K6PKMvwtZ1m630EiEANYjA7D18nUuCDytD2TpQRYNqTMIPq5SyfMQ3DQQNDKZjJqeb-m5gM07Ge3LqKQDssSZeuFTAqBwyaNZa8-_o1Ci7agEUZF2C2vT0pkG3PeJEa6SOG9II4bdZS_1IaXbfNoHNXxyvBTsPnbhstIaINR__O5_7qvyAI12XDPYXNz0kQbVaIUm6s5I-AKQOZD5HsYu1_SA7mBLHdbaEIaT3BuNb0py5mrVZDbHUMb67E5f-_NakdZREX7id-BLnjJs24C3jYUkshfhrD5NdbQ0jbN_0qIiNhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb1538895.mp4?token=FstZE8uC5MdBHJUkdKzhJLVMG2yMMC9fGo3vd4K6PKMvwtZ1m630EiEANYjA7D18nUuCDytD2TpQRYNqTMIPq5SyfMQ3DQQNDKZjJqeb-m5gM07Ge3LqKQDssSZeuFTAqBwyaNZa8-_o1Ci7agEUZF2C2vT0pkG3PeJEa6SOG9II4bdZS_1IaXbfNoHNXxyvBTsPnbhstIaINR__O5_7qvyAI12XDPYXNz0kQbVaIUm6s5I-AKQOZD5HsYu1_SA7mBLHdbaEIaT3BuNb0py5mrVZDbHUMb67E5f-_NakdZREX7id-BLnjJs24C3jYUkshfhrD5NdbQ0jbN_0qIiNhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم همچنان به دنبال دستاوردسازی در جنگ علیه ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ مدعی شد که اگر ایالات متحده همین امروز از جنگ علیه ایران خارج شود بازسازی این کشور ۴۵ سال طول خواهد کشید.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/687066" target="_blank">📅 00:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687065">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8VeSwlDRRnypUNsBNtuQefghKGeVrOmnQMrcS6ZR46hvntnRdAONzOGv1YW9QjB75wVLjg73FMi5icF8ESU4WM5w9KbKmAm-QGw5R2MH-IwSyE6ljWaA2fltHXQ3C1hyYiJJUR1RqENYAYtN0UjVRWe26ohGZf4f7ys_F9SA7fpYUX7MNBV_bh9OmHE3MhZ7DUbIro_TKYKDH17Tm4mDXE5D2tghD0QrXfaoMUPW3fzC7kaS67mXdNH4KEKYLq4UdiNnDUaWUOBJfLcadTEzO7ksB2GbjOT3cmtxkFuatGojb1UA0LWfT241kbPuhZyP-eNhdnVngjzwCkLxjGZHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشکل جدی لجستیکی نیروی دریایی آمریکا در غرب آسیا
روزنامه نیویورک‌تایمز:
🔹
حدود ۲۰ کشتی که تقریباً ۲۰ هزار نیروی دریایی و تفنگدار دریایی را حمل می‌کنند، هر هفته به بیش از ۴۲۰ هزار وعده غذایی و حدود هشت میلیون گالن سوخت نیاز دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/687065" target="_blank">📅 00:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687064">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
وزیر نفت: در زمان محاصره اول چند بار توانستیم نفت را از خط محاصره رد کنیم. نفت را هزاران کیلومتر دورتر می‌فروختیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/akhbarefori/687064" target="_blank">📅 00:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687063">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264181d47f.mp4?token=sVdg__1xa-9YcsqLlT_N481MgYLYVKdAeZtXkDDmu8iA5SrJiK2kLq7-NFB4MnnG7pdH04qNYViCU7GkobdjV1rX_cIO0bovcjYRylwD-AypF0o3KFT7JfVHWiZA2oTFUrNsGTmhJInh72Shkgj2jE07jbhML-0mLKHu7BPLCL27g7ncG4CIXsqe-B__2C6AR6ejKrtS9FNX9-XgVVdmrcr_8GFFt7ROBDrztb97BuSpRXvtBFsrKJtLk57gz-H6_w_Xe3_9PX5-0MZdCeMV6AXjGTdsGpxtdncVJ6gBIE0GDKUQNTccPL_nj_n8CW9xFwpiKcVbiJ0xbQf-b10IxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264181d47f.mp4?token=sVdg__1xa-9YcsqLlT_N481MgYLYVKdAeZtXkDDmu8iA5SrJiK2kLq7-NFB4MnnG7pdH04qNYViCU7GkobdjV1rX_cIO0bovcjYRylwD-AypF0o3KFT7JfVHWiZA2oTFUrNsGTmhJInh72Shkgj2jE07jbhML-0mLKHu7BPLCL27g7ncG4CIXsqe-B__2C6AR6ejKrtS9FNX9-XgVVdmrcr_8GFFt7ROBDrztb97BuSpRXvtBFsrKJtLk57gz-H6_w_Xe3_9PX5-0MZdCeMV6AXjGTdsGpxtdncVJ6gBIE0GDKUQNTccPL_nj_n8CW9xFwpiKcVbiJ0xbQf-b10IxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
الکامپ ۲۹؛ جایی که تکنولوژی، آدم‌ها و قصه‌ها کنار هم قرار گرفتند
🔹
ایده‌ها، گفت‌وگوها و لحظه‌هایی که ارزش روایت شدن داشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/687063" target="_blank">📅 00:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687062">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77c5f4cdb8.mp4?token=XKdFHb9Ynkn-Y7xCCPr5Ta0Jh_TbP8okyOUEe2k1qNBLw7YOWlVbtK2ZOeO96k6BHDcovC0RbfZnEiS8BWcmzDZLiEQa4xElGO3JYKu3wabBewWmggsVaiSLYqUhqjAlcADAB65vLz6b4cZCCR1DuT8DXLGCAyMWNAnMrQlc9NRm7PIGVO4Eb5Of1wR3S7kEU-YjKDksRQ1XHwAXUGSFvaHGBFMmRJZDpCw5vZ-2iXwE-lZNkKdBsanhVgPlxpR4VaoLiEkAig3uYlAFk11ST8CNoOblabTEwUXt8hwXSmPqiQqEeRKA4CnTp-i6ZFQJgXfhLuj8ZitdXXusDEainw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77c5f4cdb8.mp4?token=XKdFHb9Ynkn-Y7xCCPr5Ta0Jh_TbP8okyOUEe2k1qNBLw7YOWlVbtK2ZOeO96k6BHDcovC0RbfZnEiS8BWcmzDZLiEQa4xElGO3JYKu3wabBewWmggsVaiSLYqUhqjAlcADAB65vLz6b4cZCCR1DuT8DXLGCAyMWNAnMrQlc9NRm7PIGVO4Eb5Of1wR3S7kEU-YjKDksRQ1XHwAXUGSFvaHGBFMmRJZDpCw5vZ-2iXwE-lZNkKdBsanhVgPlxpR4VaoLiEkAig3uYlAFk11ST8CNoOblabTEwUXt8hwXSmPqiQqEeRKA4CnTp-i6ZFQJgXfhLuj8ZitdXXusDEainw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ‌های مختلف بنزین چه فرقی با هم دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/687062" target="_blank">📅 00:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687061">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افشاگری تکان دهنده نماینده مجلس از همدستی برخی دستگاه‌های مهم کشور با تراستی‌ها در فساد مالی
رحیم زارع، نماینده مجلس در
#گفتگوی
اختصاصی با خبرفوری:
🔹
گزارش حسابرسی که سال ۱۴۰۲ شرکت نفت داده است و تفریغ بودجه همان سال توسط دیوان محاسبات یک اختلاف ۴۴۰ همتی آورده است که مایه تأسف است. پولی که از سال ۱۳۹۶ اختیارات شرکت پخش پالایش گرفته شده و به شرکت ملی نفت داده شده است؛ فرایندی غلط است که رو به جلو می‌رود. این پول که با دلار نزدیک ۵ هزارتومان دست تراستی‌ها بود؛ یک نمونه‌اش در بانک ملت است.
🔹
در گزارش دیوان محاسبات بانک ملت از محل وجوه ارزی حاصل از فروش فرآورده‌ها (که تراستی به عنوان امانت در اختیارش بوده است) به شرکت اهداف تسهیلاتی اهدا کرده است تا سهام بلوکه هلدینگ خلیج فارس را از دولت بخرند؛ یعنی از پول شرکت پخش و پالایش به خود شرکت صندوق بازنشستگی و شرکت اهداف وام داده که سهام هلدینگ خلیج فارس را بخرند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/687061" target="_blank">📅 00:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687060">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a4dcb8c2.mp4?token=K7vT09Ch1qnLkJ3oi8sg05zj9QrBsXGKOD69jOgp-7M4jLHWMoPGp4gzrTmO6QJlJwkRqNcw2SMsrQQIfgEIoJtaFhBp2r-v8wEvNjvQgJGX4doIwYpPi990k2iu_l-I-DQElFc2YhAsav2fcJZB6q8pNqlwhnt07NbixpRwS3nigRkpIe86aqzHsQ6R9FTR9bt2LUpR0Rqge_oi0YtI4ggkXtu65mwIInbIxFwmPfOZjrgM4ZZ7FWH-VX21AhJ9EDbE6Bo-5FQ0L9KWNGsJ2M2K_CnglJPPwzg6B9jY-VbMVcDUArrT3gftMAnLE2fs1r27GBBQaXoNCGxSJru7GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a4dcb8c2.mp4?token=K7vT09Ch1qnLkJ3oi8sg05zj9QrBsXGKOD69jOgp-7M4jLHWMoPGp4gzrTmO6QJlJwkRqNcw2SMsrQQIfgEIoJtaFhBp2r-v8wEvNjvQgJGX4doIwYpPi990k2iu_l-I-DQElFc2YhAsav2fcJZB6q8pNqlwhnt07NbixpRwS3nigRkpIe86aqzHsQ6R9FTR9bt2LUpR0Rqge_oi0YtI4ggkXtu65mwIInbIxFwmPfOZjrgM4ZZ7FWH-VX21AhJ9EDbE6Bo-5FQ0L9KWNGsJ2M2K_CnglJPPwzg6B9jY-VbMVcDUArrT3gftMAnLE2fs1r27GBBQaXoNCGxSJru7GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمه ژاپنی از حمله آمریکا خبیث به مراسم عروسی
در سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/687060" target="_blank">📅 00:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687059">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D51WVqstVz0l4b7OkmVyYbsLTTkzDPwapl-fdZijm1IF1UkmFDLjlerAMt2Rz8vCsYA95Jnxl2zC565dn_9epy4WRTb6SWXIZVSgllNsiBBlo9EEwfryQi-ZjocVS65sCkxbA7bhkl0W_lH1zmV-D3RLENFMojO2gjabPWN2FA9Uc_EAEiJaw7H_ztREgX8VyDxcaF_7fw_IOaYNTGEm4NoqWbLy48YC94WFhdxNnVyIoDlFE__4crGwaqFu3YETv5Eerbvs47cTY_P4ffkwuxIGaEn55BDZKh2xqqT0A6_08FWSjyi-q8swUyYP6CYiyaIGJb0WS4sNiI6LDFfiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/687059" target="_blank">📅 00:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687058">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
مخالفت دولت عراق با تمدید حضور نظامیان خارجی
حیدر العبودی سخنگوی دولت عراق:
🔹
پیشنهاداتی درباره تمدید حضور نیروهای خارجی وجود داشت اما دولت با این پیشنهادها مخالفت کرد. حضور نیروهای خارجی و حتی مستشاران در خاک عراق تمدید نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/687058" target="_blank">📅 23:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687057">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سنتکام: در راستای تضمین پایبندی به تحریم‌ها علیه ایران، مسیر ۸۷ کشتی را تغییر داده، فعالیت ۳ فروند را متوقف کرده و برای بازرسی وارد ۲ کشتی دیگر شده‌ایم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/687057" target="_blank">📅 23:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687056">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d834f1eda0.mp4?token=nsyE7KUX3R_voviIbth-H10zaE4mFOS13E-9TUeIbs_oSzqwiEJYIiRjvEK_Uu2eZs-CgnfE5Yx3IlJeGs1WnvVci4A1vEwMJw2cvhGXYArUJQAsknEGfwG2ZOMhWQd-bs-FYW4kQwpMk22vUDGLZr9lhWw_Kpjd3WDVxpHmX6JwzMifE2Tz-1PkcoOBJmzGtzS7aoO3aNhrzJAbc03z31qk69DhQJxh7VTTKP_KU_gUmqAfTG7CWCXtsyKaEEMcAdl7jmb7aFm3MRGDa7rjsgdv9CnUxFfETGEb7tbHHQZ4zpRVDJF9BgJbfcLE9X-OsbHKa8N-W8LJXZjNS85V4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d834f1eda0.mp4?token=nsyE7KUX3R_voviIbth-H10zaE4mFOS13E-9TUeIbs_oSzqwiEJYIiRjvEK_Uu2eZs-CgnfE5Yx3IlJeGs1WnvVci4A1vEwMJw2cvhGXYArUJQAsknEGfwG2ZOMhWQd-bs-FYW4kQwpMk22vUDGLZr9lhWw_Kpjd3WDVxpHmX6JwzMifE2Tz-1PkcoOBJmzGtzS7aoO3aNhrzJAbc03z31qk69DhQJxh7VTTKP_KU_gUmqAfTG7CWCXtsyKaEEMcAdl7jmb7aFm3MRGDa7rjsgdv9CnUxFfETGEb7tbHHQZ4zpRVDJF9BgJbfcLE9X-OsbHKa8N-W8LJXZjNS85V4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات گسترده در پایتخت اسپانیا در اعتراض به بحران مهاجرت
🔹
هزاران نفر از ساکنان مادرید پایتخت اسپانیا با برگزاری تظاهراتی گسترده از نحوه مدیریت بحران مهاجرت از سوی پدرو سانچز نخست‌وزیر این کشور انتقاد و خواستار اقدام فوری دولت اسپانیا در قبال این مساله شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/687056" target="_blank">📅 23:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687055">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fab0b1b62.mp4?token=BVeLXUfuUJiOksNTBF6L1hyVxircbMXBj6TqFGLv7MVq3nGiR8kBQhm4hTQRQAJ_cc-rt-7wJgIrE-bFMREnRqOW4gCWjjosqqWBcnDSZBLAkcIOuzxHIBiy8OS2qUy7HKXO3tWEoKyXiIS_v8r8nKqIO8qPZEVI83xa72AvozKN-B41OExcX91D6ZiL27F-eLZmIVO-wRtuz8il2VKk7jF0SeH23apDRDvtXsI92_tX30JEc2195rkxiLu4yEMuOEpiOa2s3vBQ6wCCu5jLRxq-y9IasIRpfCeDCMG62ArBYDx4GergmZ6zGK8SbCSZG0aGX3KLMcGMMEcKR7Mmxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fab0b1b62.mp4?token=BVeLXUfuUJiOksNTBF6L1hyVxircbMXBj6TqFGLv7MVq3nGiR8kBQhm4hTQRQAJ_cc-rt-7wJgIrE-bFMREnRqOW4gCWjjosqqWBcnDSZBLAkcIOuzxHIBiy8OS2qUy7HKXO3tWEoKyXiIS_v8r8nKqIO8qPZEVI83xa72AvozKN-B41OExcX91D6ZiL27F-eLZmIVO-wRtuz8il2VKk7jF0SeH23apDRDvtXsI92_tX30JEc2195rkxiLu4yEMuOEpiOa2s3vBQ6wCCu5jLRxq-y9IasIRpfCeDCMG62ArBYDx4GergmZ6zGK8SbCSZG0aGX3KLMcGMMEcKR7Mmxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری ویژه و خاص از شهیدان حاجی‌زاده و باقری در رزمایش موشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/687055" target="_blank">📅 23:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687054">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1WQLwkNLE2HxrvSvpzy_okTcdTo8FptLrD7yD5dSEkYTyc3rx-YQDaOg2RxMmZddVhhzMP8XaUOw2-bWuRrDBjsaWZNxNLlr4j-7TKiTkg6KEn_86UkkIX3qkEIVIj9YQbMrkjzrEegovFdY1s_FuUTn5dFKsCfvDkjl7N3gmIA_AnVBynCky6hxCZhO2eEdcCIxIOuub-jjgcLIZ_ZSmH94R94LXPIdGTR5cbqnBo6Jd70vwSygpGY9MrcNMggkjMn4UhWNXzi9MKydXhMhH3JAfcLF7yhPeFQYzeTZMuTXO0jJXkLj6eSLi3WoaEOl23Co19GC7H4doJ78OB4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: بر خلاف آمریکا که حمله به اهداف غیرنظامی را تبدیل به الگوی ثابت جنگ‌های غیرقانونی خود کرده است، ضربات دفاعی ایران منحصرا علیه اهداف نظامی بوده است. گزارش رسمی قطر نیز اثبات‌کننده این واقعیت است
🔹
سخنگوی وزارت امور خارجه در پیامی در شبکه ایکس، با اشاره به سند ثبت‌شده توسط قطر در اتحادیه بین‌المللی ارتباطات راه دور (ITU) که در آن تاکید شده ضربات دفاعی ایران، فقط متوجه پایگاه‌های نظامی آمریکا بوده است، نوشت: دولت قطر در سندی رسمی که به اتحادیه بین‌المللی ارتباطات (ITU) ارائه کرده، تأیید کرده است که حملات دفاعی ایران علیه نیروهای آمریکایی مستقر در خاک قطر منحصرا «متوجه تأسیسات نظامی آمریکا بوده است. هیچ منطقه غیرنظامی هدف قرار نگرفته است
🔹
تنها استثنایی مورد ادعای قطر، حمله به یک تأسیسات گازی در ۱۸ مارس بوده است. اما در این مورد هم باید در نظر داسته باشیم که آن تأسیسات در آن زمان در خدمت عملیات‌های تجاوزکارانه آمریکا علیه ایران بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/687054" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687053">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giGlfyfLb0WNQf3pYVc9eKovmCVylZQ5D1dGctEUph5kTGUnJUIbbn8mOD202jynnJPco556Uo6QRvZS3V4Ss-70JVAa91oXXV_TASoOYcBG8vlSO_WL7hagfsmJ1o7Vaoh57HKECExvV4BDHc2--lt2mac1Fto68W7KSUuYIK6WH8fK1k7EJyTc49OFpegHNpvcGEd4ON96dDIF-nyeLriFGWp0X_8Wn0tcJ__tYeQvOIDkRrd_71FR0SBcCQzqqZ5am9YsnXDvgJ1IgiRLmjvbf3kLBoRXLvxTXx4ysS9nNkmGidCLCqa5Y5w87LDBOrtkZR3Ty4g2sJxaeea9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم: منتظر فروپاشی اقتصاد کانادا باشید
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/687053" target="_blank">📅 23:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687052">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GACZOJIFOqapW2SYh98vXjJ6JCVoBSMnp4gDyRrXRAlv1ztYWKgsGp_h7VZHqgqTCA4wvCmlH7agMbnaUUhSPtQ4piKXJD6bn56mmp-K_fx2JWYhS3o0Bp3KXex3TC_zjQoTKGpl1_gu1iCErzf4AQHRZEyzI5ix9Zivh2g4iP-URSAXCFc2QOY7YZou9nfw6rW07EZGL4C2aKfmg9WjqaR0YNkH5V8KvLjNioyifmqP62Uq_hBita7uX__-PPpDKa7L1Vgeaw5v7sZGy5IqQdCaw7qWjD11lFMaUC4vZdV34wpXy-_FCTY7y1ymMRPokNVnN3-Ze4rMjHIWTKYCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روی خون کودکانمان حساسیت بیشتری داریم
🔹
از انتقام خون شهدایمان صرف نظر نخواهیم کرد و بخصوص نسبت به خون اطفال و کودکانمان حساسیت‌ بیشتری خواهیم داشت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/akhbarefori/687052" target="_blank">📅 23:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687050">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromزی‌ ویژن | zeevision</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4193564cfc.mp4?token=ItV96GLooMJfZnAtdoRwuvKB7dTJpS7cRN2fFAvMDv7fiplFo23ZAH-SX-8YtnYRVXk68QkFiK-ms2AjcvfjG39jjRus5KHulzBcSXWrROjDREzea2J3S1eYoSZ6AheUctIHhaylKJCFsr8s3LVougpa-Nm_sJotILL23T01TOcaViuf0O6Oxw9GoQmF4ERtTr_qLeK7aOaydPymysVGBwdv1EgHpd5GHYv3izZs6InrQN8eHGbRrGQvQ74KuOR4JTlS8yFvJ7AlFAqvYHwY9M2Wot2kCi75K5v_OCoydKF5UQYswzTe9cQZ6OpqmWqnUxin-z8kBaS9wg8VNmoBiB8YFJtTjLcLB0t9vWb8oUGz9j59iJ7jhgEksi1ehGwY7oyrur0yvUk_iJKBFyHLfXwTLZXCBf6NzXslV8U6LVyDD2ZLOl7c2dVKwqXVKmc4kKRpDBaA4JRmAMx77szsWUQVH-Tk67giH5QRQRPgPqUrQ9PtrloiIZukoPGg6AsQZSSBzrKDk8WwEAX-zEdyNU-arpTnFZnbEbJp6OBeN6NYH1sw3ZI6r85rwCwnP9IN9GEh39sQNnh4bDW6EKhMduoCFtMTJWL_8DloRSHaun9DPDmy6mR-eAbiaE9oUVld09kucc19Uvv30Al8KmG8Tjg4WtpYoRuGHW3yfeFWyIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4193564cfc.mp4?token=ItV96GLooMJfZnAtdoRwuvKB7dTJpS7cRN2fFAvMDv7fiplFo23ZAH-SX-8YtnYRVXk68QkFiK-ms2AjcvfjG39jjRus5KHulzBcSXWrROjDREzea2J3S1eYoSZ6AheUctIHhaylKJCFsr8s3LVougpa-Nm_sJotILL23T01TOcaViuf0O6Oxw9GoQmF4ERtTr_qLeK7aOaydPymysVGBwdv1EgHpd5GHYv3izZs6InrQN8eHGbRrGQvQ74KuOR4JTlS8yFvJ7AlFAqvYHwY9M2Wot2kCi75K5v_OCoydKF5UQYswzTe9cQZ6OpqmWqnUxin-z8kBaS9wg8VNmoBiB8YFJtTjLcLB0t9vWb8oUGz9j59iJ7jhgEksi1ehGwY7oyrur0yvUk_iJKBFyHLfXwTLZXCBf6NzXslV8U6LVyDD2ZLOl7c2dVKwqXVKmc4kKRpDBaA4JRmAMx77szsWUQVH-Tk67giH5QRQRPgPqUrQ9PtrloiIZukoPGg6AsQZSSBzrKDk8WwEAX-zEdyNU-arpTnFZnbEbJp6OBeN6NYH1sw3ZI6r85rwCwnP9IN9GEh39sQNnh4bDW6EKhMduoCFtMTJWL_8DloRSHaun9DPDmy6mR-eAbiaE9oUVld09kucc19Uvv30Al8KmG8Tjg4WtpYoRuGHW3yfeFWyIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨ ⁨ ⁨ ⁨ ⁨ ⁨ ⁨ ⁨ «حالم از خودشو هر زنی که تو اون مطب رفت و آمد داره بهم میخوره…»
انتشار قسمت اول سریال «نیم رخ» فردا جمعه ۱۳ شهریور ساعت ۱۲ ظهر در
#زی_ویژن
📣
@zeevision
🌐
www.zeevision.ir</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/687050" target="_blank">📅 23:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687049">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اقدام جدید آمریکا علیه دانشگاه‌هایی که اسرائیل را تحریم کرده‌اند
🔹
مجلس نمایندگان آمریکا روز پنجشنبه لایحه‌ای را تصویب کرد که دانشگاه‌های شرکت‌کننده در جنبش بایکوت اسرائیل را جریمه می‌کند.
🔹
به گزارش گاردین، بر اساس این لایحه دانشگاه‌های شرکت‌کننده در بایکوت اسرائیل یا دانشگاه‌هایی که برای جلوگیری از مشارکت دانشجویان در برنامه‌های تبادل دانشجو با رژیم صهیونیستی شرکت کرده‌اند، جریمه می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/687049" target="_blank">📅 23:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687048">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoboDa8Ebgr8TLICbRf4VaAhy99rSZlmRoE_c5Yvp5G3N3hky3-v8xB2O8XPuF8-AnNWG-cwnvN28dzQao6RRj1PGpR5LZ5iQiYEZ3Nt68rzNefEuCbsQtgjDwlumtaWOzHvnDvGAo7rK0T1lPtUIeXDKZp_aK_ZWDdRGT7xwhWqa-wfq3mMVrKZWnUvzWCEuOf9Dxfwro_zsML7G-e2AXbla_ohq5_esqAglE8uGu7QGLU1i98GhtMQm7rvC4vBEJmH2tVBGCYPgqN-oGzQrQfYKfW571f7lLatvoiZ8MSHBUR7g9DBZ8DgSXi6FLvamCPgTDJ3GhovHqqSNTluew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت زیبا قره‌داغ ارسباران در تبریز
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/687048" target="_blank">📅 23:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687047">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مهمترین رفتارهای مجرمان در حوزه سایبری چیست؟
تبریزی، قاضی حوزه سایبر و فضای مجازی در
#گفتگو
اختصاصی با خبرفوری:
🔹
عمده رفتارهای مجرمانه در حوزه سایبری ناشی از کلاهبرداری رایانه‌ای، جعل رایانه‌ای و دسترسی غیرمجاز است.
🔹
بسیاری از هم‌وطنان فعال در این حوزه، با مبحث متا‌دیتاها آشنایی کافی ندارند.
🔹
برخلاف فضای سنتی، در حوزه سایبری مفهوم اعتماد به معنای رایج وجود ندارد و اعتماد باید در بستر داده‌ها و سامانه‌ها تعریف شود.
🔹
ریشه اصلی رفتارهای مجرمانه در این فضا، ناشی از خلاء‌های موجود در زمینه فرهنگ‌سازی است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/687047" target="_blank">📅 23:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687045">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/278fe1e4ed.mp4?token=hmt2vHgJVsSgJSGFhBNIGWT6aG3GlWQI7yPAgAGoLzrwAAZgim9fbzYwdsFfVHn7c7cJbPTfZnQg6oYUBkKOI4Z52xArtEKU0SwTWgryl12ePhEkPmU-c9FmLkTcfEO33ngRXDKl7Wm6hYlDDFyeLcokVxsAog_tCZARkdDHKxEclC55D8L2XQ7r29xLggSSKsfqFzpSrK9_kqKZ9dsmIQEaOANQN82wAot3Oi__zesS5i3Gg3OnCC0v_BWp3nJmsmbt5MRPjR5Wh9dbCHzCpSgNyGkZM2U2dqVMwjPlfEleiLfkVLgLQdtYnFyRG4VDXqTgPTRg-HlX5U659ND4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/278fe1e4ed.mp4?token=hmt2vHgJVsSgJSGFhBNIGWT6aG3GlWQI7yPAgAGoLzrwAAZgim9fbzYwdsFfVHn7c7cJbPTfZnQg6oYUBkKOI4Z52xArtEKU0SwTWgryl12ePhEkPmU-c9FmLkTcfEO33ngRXDKl7Wm6hYlDDFyeLcokVxsAog_tCZARkdDHKxEclC55D8L2XQ7r29xLggSSKsfqFzpSrK9_kqKZ9dsmIQEaOANQN82wAot3Oi__zesS5i3Gg3OnCC0v_BWp3nJmsmbt5MRPjR5Wh9dbCHzCpSgNyGkZM2U2dqVMwjPlfEleiLfkVLgLQdtYnFyRG4VDXqTgPTRg-HlX5U659ND4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلفی همسر عراقچی، دختر پزشکیان و فاطمه مهاجرانی| امروز
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/687045" target="_blank">📅 23:12 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
