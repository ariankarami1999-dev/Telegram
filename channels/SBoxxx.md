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
<img src="https://cdn4.telesco.pe/file/mW05a8ZZpjk_bPxMIAO0NUbLo048hqXRttzXM7OowqK_Ki5tMN0dONylivFlObGv3sXVZE3nE0f-0i3Nh_C4wepIgN1mAKPpHwiLI4zaKomcBv-rZfVqrZG2c1EDRaA4HGfX1G3ptqHFjlgn3oQK9a1eC87KPrPS43tW7BXO4nsnszZUffcZZgFOIUXJlBNOalqiz-eQ3uOtZeuz_WCc0zd4ZnGPirkUKz8WPIJ11PjDBUKm0UUt6JuYoObOODQppW8IUeHrBDpa29c0mFu4LHPG8ohRJwyOpuiR7sxlpG1xQ22VTlooL3K-8k7vfSiQ6MV1sLS1XksMEWZWkG62yw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 00:04:08</div>
<hr>

<div class="tg-post" id="msg-19173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مصاحبه مایک هاکبی سفیر آمریکا در اسراییل با تاکر کارلسون درباره حق الهی اسراییل در تصرف و کنترل خاورمیانه.</div>
<div class="tg-footer">👁️ 339 · <a href="https://t.me/SBoxxx/19173" target="_blank">📅 00:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19172">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">چقدر حس خوبی هم داشته یارو که ۴+۵ را درست جواب داده !</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SBoxxx/19172" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خب اسکل جواب سوال دوم را میگفتی مثلا ۱۳!  ما هم خب ۱۰ خط لوله داشتیم و مخ آنها هم مثل مغز خودت میگوزید</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/19171" target="_blank">📅 22:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔥
خاطره عجیب اوجی از تماس موساد به او!
🔹
جواد اوجی وزیر سابق نفت: ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
🔹
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/19170" target="_blank">📅 22:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c687c4b9c.mp4?token=pgPYtcaBAJ7dGodIZ-mHzFuxUcjSUs65DanO85LSsvo00I8fZmE1PzEEXKR-5MoXCySinKBXtVAHgEur5x9sshVT743OeAhEWeSiQeza_idph55la9RQeconRQ2u8xFAiVm-go0RqCvS-BeRJ-x0e8PMVoTQLSgbk3Do2Kh5-X4-PUd7HaGfCkkhKm_TYnJILgasSEFKgi-ApqoMfbqmgbMXfxunAy0Fi-kyD3dxZjAJALGprMRPxVkmzz6VObnBD-XyIGrXk6m2XVvdN04iDTGRoL1ryLOMBcRcE1zj4qtA1NWEaJ1y7DCRO_bFI5gdg_ek5aekAENG2sbmWXn7ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c687c4b9c.mp4?token=pgPYtcaBAJ7dGodIZ-mHzFuxUcjSUs65DanO85LSsvo00I8fZmE1PzEEXKR-5MoXCySinKBXtVAHgEur5x9sshVT743OeAhEWeSiQeza_idph55la9RQeconRQ2u8xFAiVm-go0RqCvS-BeRJ-x0e8PMVoTQLSgbk3Do2Kh5-X4-PUd7HaGfCkkhKm_TYnJILgasSEFKgi-ApqoMfbqmgbMXfxunAy0Fi-kyD3dxZjAJALGprMRPxVkmzz6VObnBD-XyIGrXk6m2XVvdN04iDTGRoL1ryLOMBcRcE1zj4qtA1NWEaJ1y7DCRO_bFI5gdg_ek5aekAENG2sbmWXn7ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
خاطره عجیب اوجی از تماس موساد به او!
🔹
جواد اوجی وزیر سابق نفت: ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
🔹
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
🔹
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@khate_energy</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/19169" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7FpMYVhuO7ZJlBtKP4nOkOBGHQELE4qw9dblCraq80dC1vFfVYGRnsg8zuzhL_3JAkbWqlXg7ICley8We4v5PZwOagCVInynGc6gcxvZv5F7bqkfIBK7UuP4xf4j1sdqmHBhrUbGQYdx4Z3uUFC9zyNtUIqyFRs4_Ls5UAnU0Urreok9gkXWwe3IN19WmgDEcPUniJcf561EpbY1dDrsZqm4pEUgrvP9gZz2vkGIXoiTMOCdgyVTlEQ7zh28xw7slE4gR_KoijcJZ54NhEPU7rqJq39qagREfXkGX7TtDU3uyYLh7j1dY7T_4nFah05kxFCmJX2vDYP02b_QyebpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این حجمی که سوخت رسان های آمریکایی سمت ما می آیند فکر میکنم محتاج دعای خیر نیاکان باشیم.</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/19168" target="_blank">📅 21:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کارخانه‌های پالایش نفت چین، نفت روسیه را خریداری می‌کنند  خبرگزاری رویترز گزارش می‌دهد که در بحبوحه بسته شدن مجدد تنگه هرمز و تهدیدهای حوثی‌ها در مورد ایجاد یک محاصره دریایی برای عربستان سعودی، چین به طور قابل توجهی حجم خرید نفت خود از روسیه را افزایش داده…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/19167" target="_blank">📅 21:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jThisupqACCb8YrruKxlmMSWhhkAfFtxqW73jOfxfWqadfwAci6cKHhxEp84yvaf1gSyWJVGOYMKJtqN1wPjULdUspQAfBJuwEKloFn_1SW72jF8FQu1_uPcZrvVeswR9crCMZvhEnWkS1q_oS7Pr--ouBh644vHZ87WKgd0NQ7XXZZ6G5Axjz2jq38HrBk99K9zJULaqYWwNw8qjwkmkyAnJpH7TESrrLSoGH7ChUsrtt2ghhtxpUX0SQ7UL53jq6oBkigVPejh1-3RwSQojDV189vg8vArAMYWbubA3OTgyISDVWiN7V_UNzM6bZyl91FLpsQPE2fPOcKyzcp9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارخانه‌های پالایش نفت چین، نفت روسیه را خریداری می‌کنند
خبرگزاری رویترز گزارش می‌دهد که در بحبوحه بسته شدن مجدد تنگه هرمز و تهدیدهای حوثی‌ها در مورد ایجاد یک محاصره دریایی برای عربستان سعودی، چین به طور قابل توجهی حجم خرید نفت خود از روسیه را افزایش داده است:
«با توجه به اختلالات در عرضه، کارخانه‌های پالایش نفت چین در هفته‌های اخیر به طور فعال نفت را از بزرگترین تامین‌کننده خود، یعنی روسیه، خریداری کرده‌اند و همچنین مذاکرات خود را برای خرید نفت ایران از سر گرفته‌اند.»
نویسندگان این مقاله همچنین اشاره می‌کنند که دو شرکت بزرگ پالایش نفت چین، بخش قابل توجهی از نفت خام روسی با نام ESPO Blend را برای حمل در ماه سپتامبر از بندر کوزمینو خریداری کرده‌اند. به گفته یکی از مسئولان یکی از کارخانه‌های پالایش نفت چین، نفت روسیه در حال حاضر به عنوان قابل اعتمادترین گزینه برای تامین در نظر گرفته می‌شود.
«با توجه به عدم قطعیت در خاورمیانه، ESPO به نظر می‌رسد گزینه امن‌تری باشد. علاوه بر این، قیمت آن نیز ارزان‌تر است.»
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SBoxxx/19166" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">منابع اسراییلی:
بازگشایی درب‌های پناهگاهای زیرزمینی نشان دهنده نزدیک بودن وارد شدن اسرائیل به جنگ با ایران است.
تل‌آویو در صورت مشارکت ایران در جنگ قصد دارد اهدافی را در ایران مورد حمله قرار دهد که تاکنون هدف قرار نگرفته‌اند</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/19165" target="_blank">📅 20:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محاصره حوثی ها ضد عربستان سعودی می‌تواند ماهانه تا ۷ میلیارد دلار هزینه بر ریاض تحمیل کند
دیروز گزارش‌هایی ظاهر شد که «حدود ۲۰ سوپرتانکر بارگیری شده با نفت عربستان سعودی در دریای سرخ گیر افتاده‌اند.» این نتیجه محاصره‌ای است که حوثیان یمن اخیراً علیه تمام کشتی‌هایی که به هر نحوی به عربستان سعودی مرتبط هستند اعلام کرده‌اند.
آن کشتی‌ها دیگر نمی‌توانند بدون خطر حملات از سواحل یمن، به‌طور ایمن از تنگه باب‌المندب عبور کنند.
در درجه اول، این موضوع بر حملات نفت خام و محصولات نفتی تأثیر می‌گذارد.
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19164" target="_blank">📅 20:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گویا سپاه یک کشتی را در تنگه هرمز زده است</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SBoxxx/19163" target="_blank">📅 20:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19162">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر دفاع یونان، نیکوس دندیاس:  یونان از این موضوع که ترکیه جنگنده‌های F-35 را دریافت کند، راضی نیست. یونان از این موضوع که ترکیه موتورهایی برای یک هواپیمای نسل جدید دریافت کند، راضی نیست.  ما یک سوال مطرح می‌کنیم: آیا این موضوع به منافع واقعی ایالات متحده…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SBoxxx/19162" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19161">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو فردا بعدازظهر جلسه‌ای با موضوع «تصمیمات امنیتی» ریاست خواهد کرد.
به احتمال زیاد این موضوع به ایران مربوط است.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/19161" target="_blank">📅 19:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19160">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شلیک موشک از ایران</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/19160" target="_blank">📅 19:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ درباره ایران:  من در حال بررسی یک حمله عظیم هستم؛ بزرگتر از هر چیزی که تاکنون رخ داده است.  من نزدیک به اتخاذ این تصمیم هستم.  منبع: N12</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/19159" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19158">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نتنياهو:  آنها مطالعات ژنتیکی بر روی جوامع یهودی مختلف انجام دادند — اشکنازی‌ها، یمنی‌ها، شمال آفریقایی‌ها و حتی اتیوپیایی‌ها — و چیزی شگفت‌انگیز کشف کردند.  آنچه کشف کردند این است که همه ما، برخلاف ادعاهایی مبنی بر اینکه ما هیچ ارتباطی با یهودیان اولیه‌ای…</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/19158" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19157">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتنياهو:
آنها مطالعات ژنتیکی بر روی جوامع یهودی مختلف انجام دادند — اشکنازی‌ها، یمنی‌ها، شمال آفریقایی‌ها و حتی اتیوپیایی‌ها — و چیزی شگفت‌انگیز کشف کردند.
آنچه کشف کردند این است که همه ما، برخلاف ادعاهایی مبنی بر اینکه ما هیچ ارتباطی با یهودیان اولیه‌ای که اینجا بودند نداریم، دارای ژنی هستیم که ما را مستقیماً به سرزمین اسرائیل بازمی‌گرداند.
به این معنی که همه ما، در جوامع مختلف، این ژن یهودی را داریم.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/19157" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19156">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ درباره ایران:
من در حال بررسی یک حمله عظیم هستم؛ بزرگتر از هر چیزی که تاکنون رخ داده است.
من نزدیک به اتخاذ این تصمیم هستم.
منبع: N12</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/19156" target="_blank">📅 19:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19155">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبرنگار: آیا لیندزی گراهام حذف شد یا مرگ طبیعی بود؟
نتانیاهو: نمی‌دانم. ادعای آمریکایی‌ها این است که بررسی کردند و میگویند مرگ طبیعی بوده است.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/19155" target="_blank">📅 18:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شورای رهبری یمن:  «پروازهای شرکت هواپیمایی ماهان ایران که پروازی به صنعا انجام می‌دهد، نقض حاکمیت کشور و تهدیدی برای قوانین بین‌المللی است.  ما از ایران می‌خواهیم که از مداخله در امور داخلی یمن دست بردارد و به حاکمیت و تمامیت ارضی آن احترام بگذارد. ما از ایران…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19154" target="_blank">📅 18:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فرانسه کارکنان سفارت خود را از تهران، ایران فراخوانده است.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19153" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سپاه :
پس از از سرگیری رسمی جنگ، نیروهای نظامی متجاوز ایالات متحده از موشک‌های کروز استفاده کرده‌اند که از کشتی‌های دریایی خود در اقیانوس هند پرتاب شده‌اند.
با این حال، پس از اینکه آن کشتی‌ها ذخایر موشکی خود را به پایان رساندند، دیروز به استفاده از بمب‌افکن‌های B-1 که از پایگاه هوایی RAF Fairford در بریتانیا پرواز می‌کردند، روی آوردند.
همچنان که مقامات وزارت امور خارجه اعلام کرده‌اند هر پایگاهی که برای پرتاب حملات علیه خاک ایران استفاده شود، برای ما یک هدف مشروع محسوب می‌شود.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19152" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: درصورت ادامه محاصره دریایی توسط انصارالله، ایران و یمن مجازات نظامی سختی در پیش دارند
ترامپ: یک سال پیش، ایالات متحده آمریکا به شدت به حوثی‌ها به دلیل دخالتشان در تجارت و بازرگانی از طریق هدف قرار دادن کشتی‌ها، حمله کرد. از آن زمان و در طول درگیری ما با ایران، آن‌ها رفتار بسیار مسئولانه‌ای داشته‌اند.
متاسفانه، اکنون آن‌ها دوباره این کار را شروع کرده‌اند و شب گذشته دو کشتی سعودی را مورد هدف قرار داده‌اند.
لطفاً اجازه دهید این حقیقت، تأییدی باشد بر اینکه اگر آن‌ها این کار را دوباره انجام دهند، ایالات متحده مسئولیت آن را به ایران نسبت خواهد داد، زیرا حوثی‌ها یک عامل یا واسطه برای ایران هستند، و ایران با مجازات‌های نظامی جدی روبرو خواهد شد، و البته، خود حوثی‌ها نیز مجازات خواهند شد.
من از حوثی‌ها بسیار ناامید هستم، زیرا تا به حال آن‌ها به طور بسیار حرفه‌ای و هوشمندانه عمل می‌کردند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19151" target="_blank">📅 16:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19150">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 11</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19150" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 11
پنجشنبه 23 جولای 2026</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SBoxxx/19150" target="_blank">📅 13:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19149">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مارکو روبیو درباره ایران:  عراقچی می‌گوید سیاست آن‌ها «چشم در برابر چشم» است.  سیاست ترامپ «سر در برابر چشم» است.  آن‌ها بهای بسیار سنگینی خواهند پرداخت.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19149" target="_blank">📅 12:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19148">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q64P2Z5-MjeU0o0QwPAsDjB1edBHDzYLGj48IhUfNPBNUcFRh5Xa3Zg10BtUH95mjgQEpeH8OtjBLxFtjiMaEhYe2gx8JDKP258AHHFUGk3VJeCXwDjnWB19zM0e9ago4obMw7Nz1_jsBlJAJqaZG8ntuWs8bgISgpVce9J0IjTvWUKnam7GX5W3tyLKmarDHw7WuoNxCK-8NSbOqcAMzuA10xSMb_RmPSnwez8i7FiAUMgcQM0LjKqtJ58yhOs8DX9v04zHBDoIw3iz0yHeSpF9J1w6jQWSp9FJyHPR8ZJCgrMcIxHrFq9kLsgPvJPrCefdNtn4IY4AcLU0kB6n2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح بسیار بالایی قرار دارد.  توصیه می شود از تعقیب مومنتوم صعودی در طلا خودداری بشود و برای خرید حتماً منتظر یک اصلاح نزولی عمیق باشیم.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19148" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مارکو روبیو درباره ایران:  عراقچی می‌گوید سیاست آن‌ها «چشم در برابر چشم» است.  سیاست ترامپ «سر در برابر چشم» است.  آن‌ها بهای بسیار سنگینی خواهند پرداخت.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19147" target="_blank">📅 12:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19146">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مارکو روبیو درباره ایران:  آنها هر روز با ما تماس می‌گیرند و از ما تقاضای توافق می‌کنند.  هر بار که آنها به توافقی می‌رسند، یا آن را نقض می‌کنند یا پس از توافق، خواهان تغییر آن می‌شوند.  احتمالاً آنها هنوز برای توافق آماده نیستند، اما به زودی این آمادگی را…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19146" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19145">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مارکو روبیو درباره ایران:  با وجود سخنان تند و ویدیوهای لگویی احمقانه شان، آن‌ها به شدت در حال رنج کشیدن هستند و تا زمانی که به واقعیت پی نبرند، این رنج بیشتر خواهد شد.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/19145" target="_blank">📅 12:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19144">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مارکو روبیو درباره ایران:
با وجود سخنان تند و ویدیوهای لگویی احمقانه شان، آن‌ها به شدت در حال رنج کشیدن هستند و تا زمانی که به واقعیت پی نبرند، این رنج بیشتر خواهد شد.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/19144" target="_blank">📅 12:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19143">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجار در کنارک!</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19143" target="_blank">📅 11:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19142">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایران پیشنهاد آتش‌بس میانجی‌ ها را رد کرد</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19142" target="_blank">📅 11:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19141">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-nPLhXAyBbesuPN6CzlMUttk9Y8cjVv6QNRCOOzwbsbZ_LCMfSWIhDkyvLMrAAIp9k3WWpaZT4TzrNDJ2ZhfFkpoo-W_3y9OQ_x8bFbnKpK10hkgUWd287W3Z_qHkyZ2n3qrbgERl39IjKvGNdxfUuqiLYNZ3X-X4w9z_kVrKVxR8wHcvzJ5KF1haPYe1sDOAts2CSael6s7Q1RgNFPr83gAOkpBmFzrUHWnHxiCPo6ebpDx2B9G2hUJ70mUWz1-cN0tbZnbbKn3pHCoMFzgtRjwPhBvtD3zdOm1CYuUXiLX8G2C6g3NffcNXsvyEnlxJwzZsQ1bGLGZWHMNP5ndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/19141" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19140">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDJXAaPiZtaSzQQGR9cpqJQ42p25FRKE3qNXhlF_m3a4FvX5G2aagjpVMLp8zYjEB6bWU71EplPu0FrJMl6R3_D2vqFnc0jHJAUDT1Y0MMhEhFAYrCC5RwwO2rBsyQtLioeeYdi-VeiWpVBXM1KAkEvO5_7GMLvlv8vi-oJr92s4D-YxglUniCjC2xqs4en_F-T5NpKri6ygoRiv03biSTgok8WZVzXIq2v8dqlAY0-rdZmC9ubfc5_3bd2tkMmQmEqSNNPak7I59rjITwOH29of-vkxcLBNqb9rSy3y5jCvSGIvqd18ZuqfRBqJg0sbJDZo8VWs7bC0W1mcGOfvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19140" target="_blank">📅 11:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19139">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyViX09DnPtVfX-IxH5R0_MbV_i7FKzkDt6-sZ3CDL-ucfkyyjOwVLBDp7Jpqj6qcizWL4ka6vbPQ9eNGUpp9VqWs-oYUyF-t0M372jq1kFc1UTImIS-6Afhz6czHvv2TEqT48KMhYT-ERyb_TtBTeBoA8xsT6kIO2wHTozmPDU2_lblYOe4QHqxb8gWwjl3pbco-GrRiZj2ebph2qm2v_ImmMblro41hYxN-OnpsTbDc9zruG65HA6dJC8BzfhKm10Y_yzENq3irhVM5lnUfEcEYKDJbDP80oOKSJeBnEW-ruR2stGsnqM-pktIF4mcwzD5SPjskvAP607ccPbobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند
تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.
از آنجا که بازارهای آتی بر پایه انتظارات قیمت‌گذاری می‌شوند، جهش قیمت اوره، آمونیاک، فسفات و گوگرد می‌تواند حتی پیش از کاهش واقعی تولید، زمینه‌ساز رشد پایدار قیمت گندم و سایر غلات در بازارهای جهانی شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/19139" target="_blank">📅 11:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19138">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فایننشال تایمز :    آمریکا نمی‌تواند با مذاکره به اهداف خود برسد. بنابراین تغییر رژیم دوباره در دستور کار قرار گرفته است!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19138" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19137">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooeUmiiKXZx_N9utrz9dBv1SM3A3-E7zGXSKXH4wjJVJM0BmlD72etJjQ0AOY_TsYoPAPdn62nkWQHhm4WnVtFKfguz6axJNfWpdJs6A2nrQ50fWxhmCHAcMQQixtxYt6nY5jbcD9nuYtjMZF3otPnaEUFZ0h17jS29BpN9JnQZ9fTwI0hpvSwavzbXltyagK1BBgdCjsNYJwQWtZkG7R5U-sgumEP9uMN_d4GDynfSVYuhvKLew_0jJeftY3g5uzBlQOwlH3sSge3tTISHVFzoU4oL18fjEtubpp7OjbY2Ii2MOmR25vCyH9OE9CKZzVf-ABg2LXviPJgPNLvzf6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19137" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19136">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfMUEE_KpMPsNcsoSYvPGm1dtnE14R8-Vuv294kx1_m2g3aC0nmJo_HlocnNegiu1XjIQehN6x-ZNHOIpaPfeBPxVI-_fvYaDopTyux09e0vyZr8Q5TVSp0I-HV_7bMrMLMw_2tFb5LH3tBk87Db9StBMbNj2tM7oVx9vtyuOX0wvcJMF8ymeK3AlSdiBdE76BPkbFfAWipcRe685IsifvSOKSbBa82sxhwWftYtZ_3dkYF6v8XtcrIv8EMinpB3tJeMELumiIcNp_4eXmhsCq5TTmFX_d7sAkuXTFi6z_9UMB4I9hY09fRt7Q2HPYc223UDUFz6PomW2Fr6e6-ztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چند ترامپ می گوید تنگه هرمز باز است اما داده های بلومبرگ نشان می دهد که شمار کشتی های عبوری از تنگه هرمز (آبی) به کمترین سطح ممکن رسیده است.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19136" target="_blank">📅 10:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19135">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0PqiLyiFekKlyRgGLM_yjSPoF3JUtQHT_fGgSDzOfi3FkLaX3tBb9slYj0nnstZeeWmw0De0FNNGv4DpK9IYS8MhUFahi4cZtJ4wjc7oU2c-cC_LNlJp_FAzihKa1jySG6Gm9kC_amE4vZ_jY4KltQyCelTGhzAShdCRhtCrTQNMG_XcEZSwxJY18DuWGW7YHUncJ7QQC7K_gRSnekh9L9EkM0WME9dvSuZs9iqUxHl5REgUrQVVnE2g3AxvNDrcbm_Rl-G_2d34pMJn7Nx6TRmHBI91-RneBkY13OBFNqAybD0gkfo0W0S0O0N8GriWfclURgCmSwxvnGg180Ywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان، طرح بودجه دفاعی به ارزش ۱.۱۵ تریلیون دلار را با وجود مخالفت‌های جدی دموکرات‌ها تصویب کرد.
دموکرات‌ها از ترامپ به دلیل همراهی با حملات اسرائیل به ایران بدون تایید کنگره انتقاد کردند و با بندهایی که به تعمیق همکاری‌های دفاعی بین ایالات متحده و اسرائیل می‌پرداخت، مخالفت نمودند.
این طرح همچنین شامل ۶۰ میلیارد دلار بودجه اضافی برای مسائل نظامی است که بخش زیادی از آن انتظار می‌رود برای پوشش هزینه‌های مربوط به درگیری‌ها استفاده شود. اکنون این طرح به سنا ارسال خواهد شد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19135" target="_blank">📅 01:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19134">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سنتکام:
امروز، ساعت 17:30 به وقت شرقی، نیروهای ایالات متحده با دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند. این عملیات ادامه خواهد داشت تا توانایی ایران در تهدید ملوانان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه، بیشتر تضعیف شود.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19134" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19133">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قیمت نفت به صورت عجیبی رو به افزایش است</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/19133" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19132">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn7zhnMDc50YIpbJqYBMJ7CUuoVxhCV-aGjQTlSnJfqURSVfOTWM41_yX9g-E29Dls6jbVx4Vt1OwdEYuMXqiPe-JRe3KrjvaBL9qT19AkyA0FjVx4QbxkRqpTOQ8gALaY1_2RaWuM3YWE3nZi57QcAXfjh8NDfG3PrklOSEs7Erg9sMOeZ6QerGwMKZQRfWYiNCEfbkhsZk1V95dr9aDAAb0J2NyndI6BC3hkdJD3JEgV-CZbZg5SRzAz1OvvlNn_qfcF5HxAp6HM23EphiO0WsxLbaXayt3_2DSha4tZKAa25ZR73ErifNzo3sIYkUPV4ApGLXbwIzcCpZE1Nexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید نشده:  یک کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است  ظرفیت کشتی حدوداً ۵۰۰ هزار بشکه بوده و مبدا حرکت آن از ینبع بوده است. ‎ #بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19132" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19131">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جنگنده‌های نیروی هوایی ارتش بر فراز آسمان تهران به پرواز درآمدند</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19131" target="_blank">📅 00:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19130">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جنگنده‌های نیروی هوایی ارتش بر فراز آسمان تهران به پرواز درآمدند</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19130" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19129">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تایید نشده:
یک کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است
ظرفیت کشتی حدوداً ۵۰۰ هزار بشکه بوده و مبدا حرکت آن از ینبع بوده است.
‎
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19129" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19128">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">موج ۴ کامپلکص</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19128" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19127">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجار در اهواز!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19127" target="_blank">📅 00:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19126">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbIfKfQc6twlDIJDKwZfvRzllX69rg2GNJpgA8XEudh1tn34ciGSPM2bM_qhL_xBxbbpi8QkjVyDSxNshGRTuoB53nfg9AXiEcEuHKb2hFT6PtjWZ0keVEVrzQRxpXg5hIaIDe5Gfr2bQnj1fJfgAeFJDxCRq7sg6OYccpup8_lnVx_ckQtpC0y3EbCctMZlIkFkbwSTYL9FdyEVe1LSzpiTE2l7BRndlygC4Hzcj7dbnsb6qTYoVwpevBdnte2Cfr8TPxcqeID1JfHkVO97fXadWPlQNh6t0DeP8FdBpSYYEi1SgLUIEDetZRH8pvXMkovEhuVjxg9KfHSotRX-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح بسیار بالایی قرار دارد.  توصیه می شود از تعقیب مومنتوم صعودی در طلا خودداری بشود و برای خرید حتماً منتظر یک اصلاح نزولی عمیق باشیم.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/19126" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19125">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMdN9u8m9mX-k1u24-n2GUbOOA9QOeIYh3GNVBEKUThBzxRYtlVCyWDvPBALFn9S8C5ISLDkjAzfCrbLPVtn0mJmLOnTj-t__222uq9LxqT0RB2bIRiH17pORUS6TmbeKkxu8GE-C_trmxhJRp8Nmehjx0ImqlsZE-9lToRm-Rxr9w0AZ3kplIoEHTNKkCVzKYjvA_r0PqmmfCoTDK3th6WKSCLzM2QT4EWBIGG21SXZIH8OkfB3PPkh9bfEA8yR3kjZqybg6-4puISrPCIg89iV_Jjvv27WPHVrGoKc5cnL_3xBb_Jcw4QN4p4kC3nmVmdds5VmDrUeFWkAArf41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا قسم همین کتاب را برای ترامپ پست کنید دلش به حال ما می سوزد و دیگر به پل ها و نیروگاههایمان کاری نخواهدداشت.</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SBoxxx/19125" target="_blank">📅 00:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19124">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجار در تبریز</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19124" target="_blank">📅 00:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19123">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇰🇷
کره جنوبی از اتباع خود خواست کل خاورمیانه را ترک کنند</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19123" target="_blank">📅 23:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19122">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">واشنگتن به تل آویو اطلاع داده است که قصد دارد برای اولین بار در جریان این تشدید، از بمب‌افکن‌ها در حملات علیه ایران استفاده کند.
سازمان رادیو و تلوزیون اسرائیل</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19122" target="_blank">📅 22:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19121">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BG2RU-eDm2nk3gxN6vsZjvBoa_sFazgGwn3vgRxwINnkI_9K7XDSmy5F1Ra_jimtHzjvgE9giLlrCzgbd8Xu3ZFbgN5E7sDKiE--11egmW3oPhv3IMqaG8ObVcBQSg6QMblvgDFg-ppEPnKZOe-QbECkv5aoe6PkNLJvRbA0DKvlhYoMHRq9T36mjQ5i3K2U4ERbVTQJ3LcK2QDs_TcuXnUsBRiVBP8Qiuc_V22NgMKSWSbtr67J0pLQiKyv_0P6Z6IG9Ej7x16Q4WBFTkF8HaepMAmRqQbDn6SmJhilL8e_kFcmoqNFq8L3UjkcAyo7OkYJoSS4chTXPT5O5FuOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، امیحایی چیکلی:  ممکن است برخورد  مستقیمی با ارتش ترکیه در دریا روی بدهد.  این یک سناریوی غیرممکن نیست؛ ممکن است حتی فردا صبح رخ دهد.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19121" target="_blank">📅 21:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19120">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">محمدباقر قالیباف:
«معادله این جنگ روشن است: یا همه یا هیچ!»
«در منطقه‌ای که ما نفت نمی‌فروشیم، کسی نفت نمی‌فروشد. اگر امنیت ما تأمین نشود، زیرساخت‌ها امن نخواهند بود و امنیت تنگه در غیاب نیروهای آمریکایی است.»
«ما بارها گفته‌ایم که وضعیت تنگه به شرایط پیش از جنگ باز نخواهد گشت.»</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19120" target="_blank">📅 21:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19119">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305f8deeb1.mp4?token=cWSkgFXi4DWggLabyw1zDrUEHPZLuWwp5-MMqn4Mv_ageS1rXvzsGTGSHWPGy78k1YoTlkGZs_JS_pblv3mcfoyhlwQEh7BbXRcX0NiD_FPTsjZdmP6XuUMikmKYDA-0WUQbeIBYdcqM9gaf64H51-N9jTabRRKghZ3NFIRCDfh_fOHEg1pEfxRmgHol1ODMh00a4mW6WqTaPQY1gLTmkuJFHqf18-zKglYiC-mWX1iwCu4clCgEwawcWgKnr0_Vf_EC9zm6Zg3PhMQffC35X8PYo_6KIlGVelbH9a7nvtstm4acPDMeTYx8csOd_swh2H08eahtrutkIABNYPF2bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305f8deeb1.mp4?token=cWSkgFXi4DWggLabyw1zDrUEHPZLuWwp5-MMqn4Mv_ageS1rXvzsGTGSHWPGy78k1YoTlkGZs_JS_pblv3mcfoyhlwQEh7BbXRcX0NiD_FPTsjZdmP6XuUMikmKYDA-0WUQbeIBYdcqM9gaf64H51-N9jTabRRKghZ3NFIRCDfh_fOHEg1pEfxRmgHol1ODMh00a4mW6WqTaPQY1gLTmkuJFHqf18-zKglYiC-mWX1iwCu4clCgEwawcWgKnr0_Vf_EC9zm6Zg3PhMQffC35X8PYo_6KIlGVelbH9a7nvtstm4acPDMeTYx8csOd_swh2H08eahtrutkIABNYPF2bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام وضعیت!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19119" target="_blank">📅 19:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19118">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اعلام وضعیت!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19118" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19117">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اعلام وضعیت!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19117" target="_blank">📅 19:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19116">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0_U5DUUFL4ISV83Vfn1D8hlGlS4XW1Q8_wFpCTU87GnUNAW8rLWzoaMAKFDpOXbE7gRxw75DapOVfnaha08sNu885KKHpH9BMt0JJ72xr2RqhIFdwqu7wF61G_v4x2cXuQuxgCeEUIBnkHSnDEjgYTA1tZ-8NRmiRKVFB7blE0WBKeyVE5sFRsn4oq9tEtaGwlzYopCzkN55IhpEOZOuvs949TOiT-rjGntDv-GKCuNup3Hq-OeW8iOnweGFij4vc69_dx48t6p7C_tWxCZwJoCRnECQ4HRnK9hkQyInSWeMbMEFlVb71yPWiozAhoaoPWmKM6kXSPvMs3mNXtfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19116" target="_blank">📅 19:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19115">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پدرسگ مثل این بستنی فروش های قرمساق استانبول است که پول را میگیرند و اسکل هم میکنند و آخر بستنی را هم نمیدهند</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/19115" target="_blank">📅 19:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19114">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">منوچهر متکی:
قرار بود قطر ۱۲ میلیارد دلار از ۲۴ میلیارد دلار منابع ایران را آزاد کند و حتی اعلام کرد ۶ میلیارد دلار خود را بعداً پس می‌گیرد، اما آمریکا وارد شد و گفت یک سنت هم نباید پرداخت شود؛ تا امروز هم این پول پرداخت نشده است</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19114" target="_blank">📅 19:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19113">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD4WsELH22LM521JK4UUo0G7_AG2cNmt0AjyoSmc70amTWqZh1VMIB4PAN7ZkXC8A4otlkPXZpUNCTzURtZ5RjyQznckcb2u1nekSWUdknB6TX097R-FPRGf2I7CQA8bE_WfFGTT6KyPNfWK2wrr7fecxSo0S6jsIcIWGBFFilZiatjbVIYKqj6p5eC_ZxdgJ-A_FEfywvZdLVZQFOUlhzGkZX3HlIMJqjYJopW2FwKnbds4M231an0x8HzJX0XyQpdxSoe1eF1Emu4Npmoi8CC1NOaFlEignAxlFiP5nphpS4b-UEQEnPGvixHhEI4vCQa5v6JkiCviedIOizavVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکل ها یک چیزی شنیده اند!
ده سال زندگی در ایران کافی است تا کارمای قابیل هم پاکسازی بشود دیگر چه برسد به اجداد نزدیک مان.
رایگان، تضمینی</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19113" target="_blank">📅 19:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19112">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jlc1PNIlqOz4oVr_ZEV-XdfOuZ0QG7s-g5J4_bva_zLnoB-Gvo99FrYhCMEh9_heG8JJCHe3VzeldZ82fH_EXfospDq_IPtrhqYUA7PQtXd4VDEdOKQGCmZnVZf-k9aGR_oG9-5oflTVKI-gsN1bCalGBCd7SrlpDe2OLJfokbHA5xCuGb_SeAmCDi8Kk2pCrJKzwdbX6aBvVJV95ErRTr5CwH_TLH7_jCWBBOMW7aIEtclbNfFb6cW6JrVlaz7CNGqLz5B5-b5kDiO4p7aNGH90UGc6Jlgp1C8S7sU6ABxeHo7sji4zSrdTqfutmfZ9JBS4BW-a7gStZazQ5Z9XUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعت 12 امروز با نیما در نشست هفتگی به بررسی پویه های ژئوپولیتیکی موثر بر بازارهای مالی خواهیم پرداخت.  لینک ورود</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19112" target="_blank">📅 19:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19111">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، امیحایی چیکلی:
ممکن است برخورد  مستقیمی با ارتش ترکیه در دریا روی بدهد.
این یک سناریوی غیرممکن نیست؛ ممکن است حتی فردا صبح رخ دهد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19111" target="_blank">📅 18:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19110">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزارت خارجه ایران:   بلغارستان باید در اجازه دادن به ایالات متحده برای استفاده از خاک و توانایی‌های خود برای حمله به ما محتاط باشد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19110" target="_blank">📅 18:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19109">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرنگار : آیا چین و روسیه اطلاعات هدف‌گذاری را به ایران می‌دهند؟ این حملات اخیر ایران  بسیار ویرانگر برای نیروهای آمریکایی بوده‌اند.
روبیو: هر زمان که در یک منطقه جنگی مانند الان هستید، خطراتی با آن همراه است. منظورم این است که در نهایت، این واقعاً ثابت می‌کند که این همان چیزی است که ایران در ۲۰ سال گذشته پول خود را در آن سرمایه‌گذاری کرده است.
هیچ کاری که چین انجام داده، به هیچ وجه مسیر آنچه را که در مورد درگیری‌هایی که با ایران داریم می‌بینید، تغییر نداده است.
و در واقع، در برخی موارد، آن‌ها در مورد آنچه که به طور بالقوه می‌توانستند انجام دهند اما انجام ندادند، بسیار همکاری کرده‌اند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/19109" target="_blank">📅 17:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19108">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الان عرب ها بیشتر نگران هستند تا خودمان</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19108" target="_blank">📅 17:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19107">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:   از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19107" target="_blank">📅 17:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19106">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ:
آمریکایی‌ها مخالف جنگ نیستند.
آمریکایی‌ها نمی‌خواهند قیمت بنزین بالا باشد، اما مخالف جنگ نیستند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19106" target="_blank">📅 17:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19105">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ :
ایران برای کشتن سربازان آمریکایی بهای خیلی سنگینی خواهد داد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19105" target="_blank">📅 17:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19103">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbxqbQCgDnMPAocCIlWunlTg9WhsjHSWwYXnXIOjHLj1cGdvV1fNgteIcS_C9QRcdkICfVEI_juqIoR3ArvrWI97Gtjkd3hI7Ik0es2f19Da8WkqW1oawvFK-dYmhG5Ur6NiY6qL1Kw3MFfAaA0qlTfaKusXd3akOA2FXIDJSyk56MRS15Tm9xfWNg2Qx0_atWWZDv_6wJX6R7iWRJc3BQdqFvFczTg_FmVMMoMWSW0QBSeRm-RY9P7Dg1UqntTyMpo9alaeElIKBoMXnxRWO2axZIlgv3Mzc5eLvVJaTMPSakC3F3RGSREr5Azpn18ubn2qLbuKifDTdkNqR4QMbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
انتظارات تورمی مصرف‌کننده آمریکایی؛ آینه‌ای با تأخیر برای حرکت دلار
انتظارات تورمی مصرف‌کنندگان آمریکا معمولاً با تأخیر نسبت به بازارهای مالی تغییر می‌کند، در حالی که شاخص دلار زودتر به چشم‌انداز تورم و سیاست پولی فدرال رزرو واکنش نشان می‌دهد.
تداوم یا افزایش دوباره انتظارات تورمی می‌تواند نشانه‌ای از ماندگاری فشارهای قیمتی باشد؛ موضوعی که معمولاً از طریق رشد بازده اوراق خزانه و حمایت از دلار آمریکا منعکس می‌شود.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/19103" target="_blank">📅 17:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19102">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مرندی باوجود   حامی نفت کرود!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19102" target="_blank">📅 17:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19101">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دکتر مرندی در پاسخ به تهدید ترامپ دوباره دستور تخلیه شبه جزیره عربستان را صادر فرمودند</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19101" target="_blank">📅 17:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19100">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTgAaJZW5t_h2mmUucCkjNwGFpBKNxD90_Pt1PrfeloM4khGMNgikzWIFwWKbkYKSdBV6_DrMDDsPQt3N2nhr2w8F3Pr53-FUX4Y_n7UB7zVN-FbGJc64pufT413eBvmEhtEo6OXnh3eoMyiy0EA5CoP654YNCcPIzD18Mr8HzIYLxv7HNc93FupbLCYCWjv1GUlUc7Q0PM_CiWqINvb3PW2azFgPX7Z7zbXU98vTbt_3lQ6VYqhF4hwZyb7bNEjMqsXWEIdVyrWhMGwaNKQYdIU_b1SdHoQkth1KYJMQO9B9dAudi6SdKIRHSHTXEhHXl6cAFNJoETn3vlc47b8Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19100" target="_blank">📅 17:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19099">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ:
از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19099" target="_blank">📅 17:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19098">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پاکستان از ایالات متحده درخواست یک تسهیلات تثبیت ارزی به ارزش ۱۰ میلیارد دلار کرده است تا ذخایر ارزی خود را تقویت کند، روپیه را پایدار نگه دارد و وابستگی به وام‌های صندوق بین‌المللی پول را کاهش دهد.  این درخواست پس از آن مطرح شد که پاکستان در میانجی‌گری مذاکرات…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19098" target="_blank">📅 13:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19097">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پاکستان از عربستان وام گرفته تا بدهی اش به امارات را بدهد!  مستراح گدایان!</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/19097" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19096">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جولانی اماده حمله به حزب الله می شود  شبکه کان اسرائیل به نقل از یک مسئول سوری گزارش داد دمشق آماده اجرای عملیات نظامی علیه حزب‌الله لبنان می‌شود.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19096" target="_blank">📅 13:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19095">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">با این سبک بازی، چین عملاً دارد ضد محور ایران-روسیه در حوزه ژئوپولیتیکی عمل می کند که پیشتر به این موضوع اشاره کرده بودم.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19095" target="_blank">📅 13:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19094">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اینها اگر بدون پدافند درست بروند با A-10 قتل عام خواهندشد.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19094" target="_blank">📅 13:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19093">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این خبر از دید من مهم است و می‌تواند منجر به ورود باند جولانی به لبنان بشود</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/19093" target="_blank">📅 12:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19092">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ساعت 12 امروز با نیما در نشست هفتگی به بررسی پویه های ژئوپولیتیکی موثر بر بازارهای مالی خواهیم پرداخت.
لینک ورود</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19092" target="_blank">📅 11:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19091">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq20nUjrswuwK8Y_T_7x8JxvO7BXllx1YdDGeOwtw564IH4x0SMyddCJOi8JNP4nUSqwtX8X4E5fCU4kuecADXaGFz7x6SPwdEcserjGqGcl___9q4fTzNsQCaGn-HIueZsYUVgaPqcMjmgdNqRve2Y6GUo3_x-3of1spdY-idCC1ZXZvjnfYhoiqMv8qz13IFU7Q2C7vaL79EIFeCXIGu4XqXueolZFECfVLBQTbbnFVj4Nz0fQ4x1pa_6n4PFk5LrCglX6iqy2wFMLBnPx-5aSDmGLLy-n5zf26fpvrR8WnDb9AFPVrsTtQHr0mBgERzOPYRvspSh4chmpxz-WxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح بسیار بالایی قرار دارد.
توصیه می شود از تعقیب مومنتوم صعودی در طلا خودداری بشود و برای خرید حتماً منتظر یک اصلاح نزولی عمیق باشیم.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/19091" target="_blank">📅 11:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19090">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الهام علی‌اف، رئیس‌جمهور آذربایجان، در سخنانی پس از دیدار با فردریک مرتس، صدراعظم آلمان، در برلین، به خبرنگاران گفت که مقامات سابق و فعلی آلمانی و روسی، این ماه، در باکو جلسه‌ای مخفی برگزار کرده‌اند.
علی‌اف گفت که باکو هیچگونه اطلاع قبلی از سوی آلمان یا روسیه دریافت نکرده و تنها پس از خواندن گزارشی در روزنامه "تایمز" از این دیدار مطلع شد. او افزود که مقامات آذربایجان پس از آن، تحقیقاتی را در مورد این بازدیدها آغاز کردند.
او گفت که: «به عبارت دیگر، از قلمرو ما بدون اطلاع ما استفاده شده است.»</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19090" target="_blank">📅 10:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19089">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6JERtUfeq_B5C_ciVHvs0EL-iSdJJ_6VRFJSz1B_GV8Z1ibasAURt7s-woixsnjKhsOZuCFXGQuoPvFnq6Tijg4AJ7hvV1zl0wiBObq5xVkS5KZKkgcuNr-RHAZccNRAOd-HN3dSuBKEwp9UiZhK63qCIQ798Y3Lo_OsazS8PsCQqAV_Ov_pL5hZV501fpWAZ3jIFWX4vFG4Ka3taw2vOmeFxNunAimtEWQOK87AsHxVVOqHBT7nSHCdpG4L1EAhnxRPiWR5Zkenyq_bRqBxo23cjTckR9rpBhEGfR9iWZ3Z9ITj0WEo_GI1QZyu6M7BpH8jn8nPARuQHhCrjgjmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاواریش ها هم یک تخته شان کم است!  در خود مصکو بنزین پیدا نمی‌شود و مردم سوار هم می‌شوند آن وقت می خواهند بروند در ماه نیروگاه هسته ای بسازند !  لابد چون مطمئن بشوند دست پهپادهای اوکراینی به نیروگاه هایشان نمیرسد!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SBoxxx/19089" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ادامه حملات سنتکام برای یازدهمین شب متوالی</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19088" target="_blank">📅 09:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19087">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ادامه حملات سنتکام برای یازدهمین شب متوالی</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19087" target="_blank">📅 03:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19086">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ادعای منابع اسرائیلی:   ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/19086" target="_blank">📅 01:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19085">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هگست درباره ایران:  ما این جنگ را شروع نکردیم. ایران این جنگ را ۴۷ سال پیش شروع کرد. ما آن را شروع نکردیم. آنها شروع کردند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19085" target="_blank">📅 01:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19084">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هگست درباره ایران:
ما این جنگ را شروع نکردیم. ایران این جنگ را ۴۷ سال پیش شروع کرد.
ما آن را شروع نکردیم. آنها شروع کردند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19084" target="_blank">📅 01:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19083">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حمله ایران به کویت</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19083" target="_blank">📅 01:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19082">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BG_xoJuy2VMoIJeJ2J_U9ClvipTbnUoVzSPslMQ6LljLs2WRgS_oPYDksiLGFaA-dWDFdLvH87hxrI3dpF-IDebKQ9XM7mSGsxq2PQI2B8KhzMxahxzu4uD4qm2P6Q0pA8395TYKjp2Se2bGfF-SOkrbKwsL_7GbvRGE4MORY1a2_Y2AKYQpuY920OzXzlTPX7EtZrVYSxYt5ba_01AAvW2OThBrxGUPWRB7s9xd13h4sYNHpgZf5RTrnAFWHBry1Kkm7GWpSIyw7rVMpHAFtTPIN5Nyfy3RMdzAavVmpLHSwUgjKAYkdXne7zIDfRVIJADKxUIDS34--txSVp_-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://nuclearsecrecy.com/nukemap/?&kt=10&lat=33.6506104&lng=51.5503762&hob_psi=5&hob_ft=2207&casualties=1&fallout=1&zm=12</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19082" target="_blank">📅 01:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19081">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگر بر فرض چنین فاجعه ای روی بدهد، این دایره ها نشانگر محدوده های آسیب انفجار یک بمب اتمی تاکتیکی سنگین خواهندبود.  روستای زیبای جهق خیلی نزدیک به کوه کلنگ است....</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19081" target="_blank">📅 01:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19079">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ادعای منابع اسرائیلی:   ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19079" target="_blank">📅 00:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19078">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5MCOFYDbTEpaauwp5jqDFWeR4gRJlmgrihqiNBb5HvxsCKZefoEy07lMI7cRUe1DVo9oggYblhuUvd8cI3OztvXvZnk3jseaaemZA14_VjHS3WJ_9rqKJtZTvFnAB56Gt8offYrtjggTlhlrLvKdVcXNnzBvFBMhWx6g9wDY4NiU0qo1L_oEUHTIr5I41FttPY1uHN8esYDGcFeD-Y5oIEvQkK2MJz_z4V_iPiS-VSQCizjngI-oQeyzakeGCYiEbZ2aPmNAuB8X-3bY7jTHsia0erGPiKuLyoDGbzJCzr6xrTuP-sb0dERK0fhjqXVB6vVguOAn5GlScNhtfc04A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای منابع اسرائیلی:   ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19078" target="_blank">📅 00:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19077">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سناتور آمریکایی: آیا ما توانایی تخریب هر چیزی را که زیر کوه "کلنگ" در ایران قرار دارد، داریم؟  هگست: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/19077" target="_blank">📅 00:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19076">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سناتور آمریکایی: آیا ما توانایی تخریب هر چیزی را که زیر کوه "کلنگ" در ایران قرار دارد، داریم؟
هگست: بسیاری از قابلیت‌های ما طبقه‌بندی شده است، سناتور. اما اگر کسی در جهان بتواند به هر نقطه‌ای در این کره خاکی دسترسی پیدا کند، ارتش ایالات متحده است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19076" target="_blank">📅 00:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19075">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیتر هگ‌ست، وزیر جنگ ایالات متحده:
«روسیه و چین در برخی از فعالیت‌های ایران، و در سطوح مختلف، به این کشور کمک می‌کنند.»</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19075" target="_blank">📅 00:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19074">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUgHTT0GsCW9byMqTvaUTVGitPXBNt9ZNdMSEBFidaIRFGNvMBcWpBmTAPGlnaFiftsx0gMvI3omxaFGOhjVMF4gKu-kzQhEOsm-S8PGjnaV7RUTXv6Ge9GGjmCFP_PMQjaDNZruhOm34_krsMGLOaSP-fEFrubzgJNcu8-e6h98Og9oDqqugfsIQCzQ2CJlMBfnymnLoneSzBBOuqaol-iAQoDiA3PU74SowUSlmX71_EqeyZ4GHyWjqtLOwjZKUV-Ek2WQ5FiIWTpJ2-lC61Tr23F4_yVGR3W7LN5wMB4w7ukfQNHiFK0XcWJamnZmwmdzSHraV-bipOWOUVlPQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو:   در حال حاضر، ما کنترل کامل ۶۰ درصد از نوار غزه را در دست داریم و دستور من رسیدن به ۷۰ درصد است... ابتدا ۷۰ درصد. از همان شروع می‌کنیم</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19074" target="_blank">📅 22:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19073">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyK-Xi7jWUVmrsAEdorf1GHjK3YixTnOHaUbxhUDat089DupaE6zxs1ZbxS-hu3b24jPelVwaTFKxO9gqZe4AzN-BMRqIE5jinnHMLnGXDwB3dLecoiXSnbLYLRsMGPXlIWsl93QZuGBLPhQR57aBS0agRp59VQON422PHWjN7sc-oe4Xq3peinDO9_M13LdBaGfxzB6jQfVTIw4VtnrWpOMZ4jmrgVv8vf4BgYZyPlzYJRF1G4go4_ejrLGanVpCFIZujVUz6sNR0IFN3AjNrWSyrrxQw05-Rx0m1JbuLwHBOskgsXNCGOgb1n0m11-nfhpEUsuzvVMu_MGvdEHZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه پایینی قرار دارد و پیش بینی می شود طلا ابتدا ریزش و سپس رشد داشته باشد.  محدوده مناسب حمایتی 4015 الی 4020 برای امروز.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19073" target="_blank">📅 22:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19072">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بلغارستان از پارلمان خود می‌خواهد تا استقرار ۸ هواپیمای تانکر آمریکایی در پایگاه نظامی Bezmir را برای حمایت از عملیات ایالات متحده در خاورمیانه تصویب کند.  این اقدام پس از جنجال‌های مربوط به استقرار قبلی این هواپیماها در یک فرودگاه غیرنظامی نزدیک صوفیه بدون…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19072" target="_blank">📅 20:21 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
