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
<img src="https://cdn4.telesco.pe/file/PajIn8sC6ncbg1xm2Er28zDoS-__FbOzQTxhRVE5yY4h_Vp2UKsfUfF5hsplu-4ZEfUxFVk4otLbD9onAqSMWpFzNwKqJ_Fx7befK_lqKZEfy48x1hAybN6OG7n85KvM-iia6rxuPoFyUZ1jsrc23ODJwdgfJU0tnpeUYqVIF2mhwokflMfIMZeRMaFhdBPcZpW-rL0PyDb-YcenxJeMrtXs9sm_jzU-9XdbRGHnnH7NaRpoAM5idjn7HE7wXB-lsPL0IATC9UDLcf_ARg8oqp4zvnKZCdRSOtUS5TCF7mM05Bt1GQ3e7v_SfH-kaZyOUTBXcaLYYCoQOgyPAmcuSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.4K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 14:34:53</div>
<hr>

<div class="tg-post" id="msg-18966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_t5GqjWDjxnPSejVLc0voyYNkPUMPtTjfmkqxInJQtRHwXzpBBnAq6QilKtKzjkWHDOHa92GpfcuzwPLblt9aFHog4M8zrNrK2evwzVzpA7NtIj8tSi-cJJcMFGK49HD10TskoTB9x9SWFligy6eb1mflwEkCaRxP5_-W2SVHDGHvKXm1BUxkl09Gqv5O1Lx6xMS34xLIsGln5b6o9JjHQHNOfT53aYgiYHRd5i9nA98uJOxC9VoPhEsNiEjXI6UFAPMXvSgUnxe4eHzMEHcfEDJduHht76wx5eoz7Rm8NEM7ad47fL6iKeXYtC7y7iONX9LONl57qRQQKY45ftGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپورت:
کاخ سفید به آرژانتین مجوز داده تا در صورت قهرمانی جام‌جهانی، بنر «جزایر مالویناس متعلق به آرژانتینه» را در مراسم قهرمانی به نمایش بگذارند.</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/SBoxxx/18966" target="_blank">📅 14:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:  ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت تروریست‌های آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه پاسداران، تلاش کردند تا تردد را مختل کرده…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/18965" target="_blank">📅 13:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی:
ساعاتی پیش، چهار فروند کشتی متخلف، با حمایت تروریست‌های آمریکا، با ایجاد اختلال در سیستم‌های ناوبری و بی‌توجهی به هشدارهای مرکز کنترل تنگه هرمز متعلق به نیروی دریایی سپاه پاسداران، تلاش کردند تا تردد را مختل کرده و از طریق یک مسیر ناامن از تنگه هرمز خارج شوند.
دو فروند از این کشتی‌ها دچار حادثه شده و متوقف شدند، در حالی که دو فروند دیگر از ادامه مسیر منصرف شدند.
نیروی دریایی سپاه پاسداران انقلاب اسلامی اعلام می‌کند که کنترل کامل تنگه هرمز در اختیار این نیرو است و تنها مسیر ایمن، مسیر مشخص و اعلام‌شده است.
همچنین تأکید می‌کند که هیچ مقداری از نفت، گاز و کود، بدون هماهنگی و مجوز قبلی از تنگه هرمز عبور نخواهد کرد.
کشتی‌هایی که تحت تأثیر اقدامات دشمنان آمریکایی قرار گرفته و وارد مسیر ناایمنی می‌شوند، قطعاً دچار حادثه خواهند شد.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/18964" target="_blank">📅 13:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خب جام جهانی هم امشب به پایان می رسد.
گفته می شود بازی ایران—سوییس  بعد از فینال برگزار خواهدشد.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18963" target="_blank">📅 09:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سپاه با زدن پایگاه های زمینی آمریکایی ها در منطقه به نظرم دارد می کوشد تا تاریخ حمله را به جلو بیاندازد و نگذارد آمریکایی ها بسیج و تدارک کافی داشته باشند.  وقتی می دانید حریف می خواهد حمله زمینی کند خب طبیعی است پایگاه هایش را بزنید تا نتوانند آرایش مناسب…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/18962" target="_blank">📅 09:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چین؛ ضربه‌گیر جدید بازار نفت در بحران هرمز  در سال‌های گذشته هرگونه تهدید علیه تنگه هرمز تقریباً به‌طور خودکار با جهش شدید قیمت نفت همراه بود. دلیل آن روشن بود؛ حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه اختلال در آن، نگرانی از کمبود…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/18961" target="_blank">📅 09:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18960">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXMFnh8KhmhNRu2xwgqhlQ3Z1_sZ4U90BjHcREmcdlpzY4MQiEMXn8RrXqua-pYt-eom4oeH-Zu1sKWDXIx6PzWT_9G5_xCMAbJgZ2GdZXWGOtdLwCKLecubXdBlWx5JV6Tor-rxH6sH39YTC6PcKStWUiBGKEJgbJKGVLBugK2YaqFkw_6C6SKiojXPEaP4m0jtgjILSGDIfIiMWHZ1pikGVeyDwDDt_z2j6QQWsvyIQWtRdxQJygfoXiiVW-nHKWplqf-g2_n7JnXrp1-TW-Bx29g5-Z83DMoGxatyWyTyhbbE5zrdiA4_pnQZvq9T09sw-kegN9YeMyKOz94uRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین؛ ضربه‌گیر جدید بازار نفت در بحران هرمز
در سال‌های گذشته هرگونه تهدید علیه تنگه هرمز تقریباً به‌طور خودکار با جهش شدید قیمت نفت همراه بود. دلیل آن روشن بود؛ حدود یک‌پنجم تجارت دریایی نفت جهان از این گذرگاه عبور می‌کند و هرگونه اختلال در آن، نگرانی از کمبود عرضه را افزایش می‌دهد. با این حال، ساختار بازار جهانی نفت در سال‌های اخیر تغییر کرده و اکنون یک متغیر جدید در معادله ظاهر شده است:
رفتار وارداتی چین
.
چین که بزرگ‌ترین واردکننده نفت خام جهان است، دیگر صرفاً یک مصرف‌کننده منفعل نیست، بلکه به بازیگری تبدیل شده که می‌تواند شدت نوسانات بازار را تعدیل کند.
گزارش نیکی آسیا
نشان می‌دهد که چین در دوره‌های شوک عرضه، نقش «واردکننده نوسانی» (Swing Importer) را ایفا می‌کند؛ به این معنا که با کاهش موقت خریدهای خود، بخشی از کمبود عرضه جهانی را جبران کرده و از تشدید افزایش قیمت‌ها جلوگیری می‌کند.
این توانایی از چند عامل ناشی می‌شود.:
نخست، چین طی دو دهه گذشته سرمایه‌گذاری عظیمی در ایجاد ذخایر استراتژیک و تجاری نفت انجام داده است. هنگامی که قیمت‌ها افزایش می‌یابد یا مسیرهای عرضه با تهدید مواجه می‌شوند، پکن می‌تواند برای هفته‌ها یا حتی چند ماه بخشی از نیاز پالایشگاه‌های خود را از این ذخایر تأمین کند. در چنین شرایطی، کاهش واردات به معنای کاهش مصرف داخلی نیست، بلکه صرفاً جایگزینی نفت وارداتی با نفت ذخیره‌شده است.
عامل دوم، انعطاف در مدیریت ذخایر تجاری است. چین در دوره‌های قیمت پایین، معمولاً بیش از نیاز روزانه خود نفت خریداری کرده و مخازن را پر می‌کند. اما در دوره‌های افزایش قیمت، این روند متوقف می‌شود و حتی بخشی از ذخایر مصرف می‌شود. در نتیجه، واردات کاهش می‌یابد، بدون آنکه فشار قابل‌توجهی بر فعالیت‌های اقتصادی وارد شود.
از سوی دیگر، پالایشگاه‌های چینی نیز انعطاف عملیاتی بالایی دارند. بسیاری از آنها می‌توانند برنامه تعمیرات یا کاهش موقت ظرفیت تولید را با شرایط بازار هماهنگ کنند. علاوه بر این، تنوع منابع تأمین نفت از روسیه، آسیای مرکزی و سایر تولیدکنندگان غیرخلیج فارس نیز وابستگی کامل چین به نفت عبوری از تنگه هرمز را کاهش داده است.
این تحول، پیامدهای مهمی برای بازار جهانی نفت دارد. در گذشته، کاهش عرضه از خلیج فارس تقریباً به همان میزان باعث افزایش قیمت می‌شد، زیرا تقاضا در کوتاه‌مدت انعطاف چندانی نداشت. اما اکنون، کاهش چندصد هزار بشکه‌ای واردات چین می‌تواند بخشی از این شکاف را پر کند و از شکل‌گیری موج‌های شدید سفته‌بازی جلوگیری کند. به بیان دیگر، چین علاوه بر اینکه بزرگ‌ترین خریدار نفت جهان است، به یکی از ابزارهای تثبیت بازار نیز تبدیل شده است.
البته این نقش محدودیت‌های مهمی نیز دارد. ذخایر استراتژیک چین نامحدود نیست و اگر تنگه هرمز برای چندین ماه به‌طور کامل بسته بماند یا صادرات کشورهای حوزه خلیج فارس به مدت طولانی متوقف شود، پکن نیز ناچار خواهد شد با کاهش واقعی مصرف، افزایش هزینه‌های انرژی و فشار بر صنایع خود کنار بیاید. بنابراین، توانایی چین بیشتر برای مدیریت شوک‌های کوتاه‌مدت و میان‌مدت کاربرد دارد، نه بحران‌های طولانی‌مدت.
در مجموع، یکی از مهم‌ترین تغییرات بازار نفت در دهه اخیر این است که دیگر تنها عرضه‌کنندگان بزرگ مانند عربستان سعودی یا تولیدکنندگان شیل آمریکا بر قیمت‌ها اثر تعیین‌کننده ندارند. اکنون رفتار خرید بزرگ‌ترین واردکننده جهان نیز به همان اندازه اهمیت یافته است. این تحول باعث شده تهدیدهایی مانند اختلال در تنگه هرمز، هرچند همچنان خطرناک، اما نسبت به گذشته تأثیر کمتری بر جهش پایدار قیمت نفت داشته باشند؛ موضوعی که می‌تواند بخشی از اهرم فشار کشورهای صادرکننده نفت در بحران‌های ژئوپلیتیکی را نیز تضعیف کند.
#ژئوپولیتیک
#بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/18960" target="_blank">📅 09:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWkc2tU6nL2uYrEdCLp02f08rDAWRorMklYrSE68a8YVucs1ToIWt7nrb5stKSPcnl1AzX6o2h1hRK3wrwNoL25BbmqSM7F8H5Xpg5FFw5rUltZbFnmghVEEe5hTkPal__gD4qsjeEgTQ0un-vaU_Pr3l1-6zp3kpFQoccW4sxsmyHdWTrjs-uOwXn6DjNGGZEnlaHAxBFr9jKqghlsOza_tpw_Ad4RfwVYV7Aiy4PiK-Or_tHlDfk29hyw4BXpt5fwpR0VxO9PFcAM-X_Bc58k8euuaOQqxnVPOwzjdXIPRb29miOU_T_PV1y61gEdXzqOOdliqZxU3bpZUhaDk-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیلی از یکی از نزدیکان محسن رضایی</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/18959" target="_blank">📅 01:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18958">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556a107e63.mp4?token=Hfs3wCk0ZdCGaIF6IXATbimjDIuhOCZ2smzZIbJCgMWxzH835EEDk0bnNNgiTlhHblI3G5lDV9u55R6YQYPDQ-8wutpC6ASoCyGqTg1E-RAxjfEE0wIpDSBTSeiLGiiQapxAMySayoV-PsechdYMb0StcbqP-4TQ5T6ekVsvMsk0qiZa4xYYhNHeEA3UQgcoZ5gu0NFS1eo3KTlCvJbvT0ouIWmYI2kD3J8xvBbY3NVJaryfQVIX4AvuzZoiZtZotNuKURiMFQGrrX7P41-4--MTnSkXsuSzanEgiBBawRdtHhIIalFHPCN6cOnk0ThTFZg8MccNsiKfOXq8-bKUdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556a107e63.mp4?token=Hfs3wCk0ZdCGaIF6IXATbimjDIuhOCZ2smzZIbJCgMWxzH835EEDk0bnNNgiTlhHblI3G5lDV9u55R6YQYPDQ-8wutpC6ASoCyGqTg1E-RAxjfEE0wIpDSBTSeiLGiiQapxAMySayoV-PsechdYMb0StcbqP-4TQ5T6ekVsvMsk0qiZa4xYYhNHeEA3UQgcoZ5gu0NFS1eo3KTlCvJbvT0ouIWmYI2kD3J8xvBbY3NVJaryfQVIX4AvuzZoiZtZotNuKURiMFQGrrX7P41-4--MTnSkXsuSzanEgiBBawRdtHhIIalFHPCN6cOnk0ThTFZg8MccNsiKfOXq8-bKUdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/18958" target="_blank">📅 00:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18957">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بندرعباس؛ گلوگاهی که فروپاشی‌اش فاجعه است   بندرعباس تنها یک شهر ساحلی نیست؛ گره‌گاهی است که بخش بزرگی از تنفس اقتصادی و لجستیکی ایران از آن می‌گذرد. بندر شهید رجایی، بزرگ‌ترین بندر کانتینری کشور، حدود ۸۵ درصد از کل تخلیه و بارگیری بنادر ایران را انجام می‌دهد؛…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18957" target="_blank">📅 23:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18956">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">—گزارش‌ها حاکی از آن است که جنگنده‌های F-16 نیروی هوایی ایالات متحده مستقر در پایگاه هوایی اسپانگدالم در آلمان به خاورمیانه اعزام شده‌اند. این هواپیماها قادر به هدف قرار دادن سیستم‌های راداری پدافند هوایی ایران و همچنین دارایی‌های موشکی هوا به زمین هستند.
علاوه بر این، جنگنده‌های پنهان‌کار F-35 از پایگاه هوایی لکن‌هیت در بریتانیا نیز به همراه تانکرهای اضافی سوخت‌رسانی هوایی برای پشتیبانی از عملیات گسترده‌تر هوایی ایالات متحده به این منطقه اعزام شده‌اند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18956" target="_blank">📅 23:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5GPktacSDQdoklim3WOHRBSiCHHZugnbNIAPuP6JiSq_xtzXUcmi2nTEpjfo99Eoy354BQJaRzh_t9I5ILgPQJDR5wZUtU3jbIjw-XQF9qY7IbMmhFZzFcxT9r0nKf_0KCmiwQW4FI_38Ojd_r8ligg-ZkjdAPNoC_5UK7rnM33xKf02_elYfBPkQmk9Puu9DKIxf6kFaRsYZVbjTwNdf5huIa8F_Yt1zUDbxOj0WNWW2YxbKM8mh8p-aecF1QHHFr5-8rqI1plLewbJDVkgOG8zd78WLC48TPv2Xd6HfsSaM13peCNd6_hsfipsYx5-AjWVWwFffBHiK5-lz88Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس؛ گلوگاهی که فروپاشی‌اش فاجعه است
بندرعباس تنها یک شهر ساحلی نیست؛ گره‌گاهی است که بخش بزرگی از تنفس اقتصادی و لجستیکی ایران از آن می‌گذرد. بندر شهید رجایی، بزرگ‌ترین بندر کانتینری کشور، حدود ۸۵ درصد از کل تخلیه و بارگیری بنادر ایران را انجام می‌دهد؛ سالانه نزدیک به 6 میلیون کانتینر و تا 70 میلیون تن کالا از آن عبور می‌کند. این بندر مستقیماً به شبکه ملی راه‌آهن و بزرگراه‌های ایران متصل است و همین اتصال، آن را به مسیر اصلی جابه‌جایی تدارکات نظامی، سوخت، نیرو و کالای تجاری میان مرکز ایران و کرانه جنوبی تبدیل کرده است. موقعیت مسلط بندرعباس بر شمال تنگه هرمز نیز دروازه ایران به مهم‌ترین گلوگاه انرژی جهان است.
اما اهمیت بندرعباس به کانتینر و اسکله ختم نمی‌شود. پالایشگاه ستاره خلیج فارس در همین منطقه مستقر است؛ بزرگ‌ترین تولیدکننده بنزین ایران که به‌تنهایی حدود ۴۰ درصد بنزین کشور را تأمین می‌کند و بزرگ‌ترین پالایشگاه میعانات گازی جهان به شمار می‌رود. پالایشگاه نفت بندرعباس نیز در کنار آن قرار دارد. افزون بر این، در دوره‌های کمبود، بخشی از بنزین وارداتی ایران هم از همین بنادر جنوبی وارد و توزیع می‌شود. به بیان دیگر، تولید سوخت، واردات سوخت و ترانزیت کالا در یک نقطه جغرافیایی واحد متمرکز شده‌اند.
همین تمرکز، شکنندگی خطرناکی می‌سازد. انفجار مهیب فروردین ۱۴۰۴ (آوریل ۲۰۲۵) در بندر شهید رجایی، که ده‌ها کشته و نزدیک به هزار زخمی بر جای گذاشت، نشان داد چگونه یک حادثه واحد می‌تواند قلب تجارت دریایی کشور را از کار بیندازد و زنجیره تأمین را در سطح ملی مختل کند.
اکنون تصور کنید ایران این بندر را از دست بدهد. پیامد آن، قطع همزمان ۸۵ درصد تجارت دریایی، توقف حدود ۴۰ درصد تولید بنزین ملی و مسدود شدن یکی از اصلی‌ترین مسیرهای واردات سوخت خواهد بود؛ ترکیبی که به بحران سوخت سراسری، اختلال در زنجیره تأمین نظامی و لجستیکی، و فلج بخش عمده‌ای از اقتصاد وابسته به واردات می‌انجامد. از دست رفتن دسترسی مطمئن به تنگه هرمز نیز اهرم راهبردی ایران را به‌شدت تضعیف می‌کند.
بندرعباس دقیقاً همان نقطه‌ای است که در آن بیشترین اهمیت و بیشترین آسیب‌پذیری به هم گره خورده‌اند و بنابراین حفظ کنترل آن برای ایران نه یک انتخاب، که یک ضرورت وجودی است.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/18955" target="_blank">📅 23:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18954">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مقامات آمریکایی نگرانند که چین یا روسیه ممکن است به ایران در حمله به اهداف ایالات متحده کمک کنند.
به گزارش وال استریت ژورنال، ایران اکنون موشک‌های مانورپذیری را با سرعت‌های بسیار بالا شلیک می‌کند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/18954" target="_blank">📅 23:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18953">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الاغ ما سالهاست در جهنم هستیم؛ دروازه هایش را بگشایی همه فرار می کنیم!</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18953" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18952">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انتظار تشدید بی سابقه تنش ها می رود...</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/18952" target="_blank">📅 23:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18951">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiKIDLZIAa-2BKPBwJ7cwvljsRsYBTNtKaeU6Ss04xqFo9A5pGsg3r0TYAh4QnUtbOD4BTrgLQfHKutZsTxMBNoplgfpP1zNO0pcM_HOpQNPu4Wn7Hx23s1IIoeuqYFt7oSVvhOXdTgoEvzzVo2OXvTDBzcSGcwek3dWXHqZrIPVf9uMb-fF-HXo0hIriTaLllJhH-OqFgLTSMvNM1gj_kjd59VPOVUKNOVqFH1d2NaSH5PhGF9Lqrc6phYDGfcWFT668IlrZUBGHeplV_4PaaM-oHlspR9fLTRu5kGS8QK6M9W037e57dA0GUZSMe_dWt06zEQe7afoUhh2uiVMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع آمریکا در واکنش به کشته شدن دو سرباز آمریکایی:
«خدا نگهدار قهرمانان. فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند.»</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18951" target="_blank">📅 22:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18950">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کریمه؛ از ویترین پیروزی پوتین تا آسیب‌پذیرترین جبهه روسیه
حملات مداوم اوکراین، کریمه را از نماد اقتدار روسیه به یکی از ناامن‌ترین مناطق تحت کنترل مسکو تبدیل کرده است. منطقه‌ای که زمانی مقصد گردشگران بود، امروز تقریباً هر شب هدف پهپادها قرار می‌گیرد؛ تا جایی که مقامات محلی برای جلوگیری از ایجاد وحشت و اختلال در فصل گردشگری، سامانه‌های هشدار هوایی را عملاً غیرفعال کرده‌اند. در بیشتر نقاط شبه‌جزیره، حملات به پایگاه‌های نظامی، زیرساخت‌های انرژی، خطوط راه‌آهن و مراکز لجستیکی به بخشی از زندگی روزمره تبدیل شده است.
تمرکز اوکراین بر قطع شریان‌های تدارکاتی، فشار بی‌سابقه‌ای بر کریمه وارد کرده است. حمله به پایانه نفتی کرچ، آسیب به کشتی‌های باری و تهدید کریدور زمینی از جنوب اوکراین، انتقال سوخت و تجهیزات را دشوار کرده است. خاموشی‌های گسترده، محدودیت فروش بنزین و اختلال در تأمین کالاها، نشانه‌هایی از فرسایش توان لجستیکی روسیه در این منطقه هستند. همزمان، پهپادهای اوکراینی پالایشگاه‌ها و تأسیسات نفتی در عمق خاک روسیه، از جمله اطراف مسکو، را نیز هدف قرار داده‌اند و بحران سوخت را تشدید کرده‌اند.
اهمیت کریمه برای کرملین تنها نظامی نیست؛ این شبه‌جزیره مهم‌ترین دستاورد سیاسی ولادیمیر پوتین پس از الحاق در سال ۲۰۱۴ محسوب می‌شود و جایگاه ویژه‌ای در روایت ملی‌گرایانه روسیه دارد. با این حال، افزایش ناامنی، کاهش اعتماد مردم به توانایی دولت در حفاظت از منطقه و مهاجرت تدریجی خانواده‌های مرفه، نشان می‌دهد که هزینه‌های جنگ به قلب این نماد سیاسی رسیده است.
با وجود این، نشانه‌ای از تغییر گسترده وفاداری ساکنان به روسیه دیده نمی‌شود. بسیاری از مردم، به‌ویژه در سایه تبلیغات گسترده امنیتی و نگرانی از برخورد احتمالی اوکراین، همچنان بازگشت حاکمیت کی‌یف را تهدیدی برای خود می‌دانند. اما آنچه بیش از هر چیز در کریمه و حتی سراسر روسیه به چشم می‌آید، خستگی عمومی از جنگی است که پس از سال‌ها نبرد، هنوز چشم‌انداز روشنی برای پایان یا پیروزی آن وجود ندارد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18950" target="_blank">📅 22:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18949">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mK31Ku86h5Pwss19jvRwcEb9ABX9ikkvLoV_33bvJmpQeF8WQBuw02ytF6RxQ2DyxS6bcG0SojlkLMPHpmqPoIsRRJcUz3IRQ76egDzL2Kh88u8ADugd3k2yiQhBIOx-tLrMWy6DXJ3sl3eQIRaR7fQH18B06aXV6hYsL5OuCM0pmSgsdYLS25bvjFZf6W7ObDTxlzNHvt4CuN7GuG5qbk_z0wTMfWOMaPgRWtr1YNJ01JxdpdemqOYmEESYB2QtKcOhnbbh9QdHVEsmyXQCJjPccJ9l51ilvKM6Gum3TkMZeiYUAgDi2eCeC7O-1_CiBFhq505b2UQndW_mcH2KCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولید گدبان سفیر اسرائیل در سازمان ملل:
موج آهنین درحال برخواستن است.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18949" target="_blank">📅 21:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18948">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ab73Aa7MNtFUD_sUlKtUj50_VWodQwu9nyChcayZlHDSv2k_KgJORF4On6cHS_rDNXJLLSBPlRxNNes3xaz0Jwy-KeO-fcvuxonLb3tLPDUJ6t1YJDeyD6yVS3d7P_ZP-cDPhh6uSAXZX--zHYVP_N7Fj_W2WdE1bmH-FG5IOG7XfVTCsf2NQES5qOloFGdUbmdu0ECcro_YV1sdgCz2vctjPrGkS9VzxRdmI_wG0b_GL8sgAYD4izT6e-AxmKeBF92__gdrhKtwf11WrK_lhfxmFkP_4_8cNuHpRdyqnvozxqHh14FZoQLm6QjDSG7macsKJ8XN_OND1Em20-EOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ممکن است سپاه پاسداران را مانند داعش نابود کنیم
دونالد ترامپ، رئیس‌جمهور آمریکا، در اظهاراتی تازه احتمال اقدام نظامی گسترده علیه سپاه پاسداران انقلاب اسلامی را رد نکرده و گفته است که واشنگتن ممکن است این نهاد را «مانند داعش از بین ببرد». این سخنان در شرایطی مطرح می‌شود که درگیری میان آمریکا و ایران پس از فروپاشی آتش‌بس دوباره شدت گرفته و دو طرف وارد مرحله‌ای از حملات متقابل شده‌اند. (
Time
)
ترامپ در پاسخ به پرسشی درباره اینکه آیا ممکن است سپاه را همانند داعش هدف قرار دهد، گفت که «خواهیم دید چه اتفاقی می‌افتد». او همچنین مدعی شد که ایران بار دیگر خواهان مذاکره شده است، اما همزمان تأکید کرد که واشنگتن حاضر نیست بدون تغییر رفتار تهران، مسیر گفت‌وگو را ادامه دهد.
سپاه پاسداران یکی از مهم‌ترین ستون‌های ساختار قدرت جمهوری اسلامی محسوب می‌شود. این نهاد علاوه بر نقش نظامی، در حوزه‌های امنیت داخلی، برنامه موشکی، فعالیت‌های منطقه‌ای و شبکه نیروهای هم‌پیمان ایران در خاورمیانه نقش گسترده‌ای دارد. آمریکا در سال ۲۰۱۹ سپاه را در فهرست سازمان‌های تروریستی خارجی قرار داد.
مقایسه سپاه با داعش از سوی ترامپ نشان‌دهنده تغییر احتمالی در سطح اهداف جنگی آمریکا است. عملیات علیه داعش عمدتاً با هدف نابودی یک گروه شبه‌نظامی فراملی انجام شد، اما سپاه بخشی از ساختار رسمی حکومت ایران است؛ بنابراین هرگونه تلاش برای «نابودی» آن، می‌تواند به معنای رویارویی مستقیم با یکی از پایه‌های اصلی جمهوری اسلامی و افزایش شدید خطر گسترش جنگ باشد.
اظهارات ترامپ در حالی بیان شده که آمریکا حملات خود علیه اهداف نظامی ایران را افزایش داده و اعلام کرده است که مراکز فرماندهی، سامانه‌های پدافندی، توان موشکی و پهپادی و زیرساخت‌های مرتبط با تهدید علیه کشتیرانی در تنگه هرمز را هدف قرار داده است. ایران نیز در واکنش، حملاتی علیه مواضع آمریکا و متحدانش در منطقه انجام داده است.
از نگاه تحلیلگران، تهدید علیه سپاه نشان می‌دهد که اختلاف میان تهران و واشنگتن دیگر تنها حول موضوعاتی مانند برنامه هسته‌ای یا تحریم‌ها نیست، بلکه به سمت یک رویارویی ساختاری درباره نقش منطقه‌ای ایران و معماری امنیتی خاورمیانه حرکت کرده است.
در صورت عملی شدن چنین رویکردی، آمریکا با یک انتخاب بسیار پرهزینه روبه‌رو خواهد شد: تلاش برای ضربه زدن به مهم‌ترین نهاد نظامی ایران، بدون آنکه تضمینی برای فروپاشی ساختار قدرت تهران یا پایان درگیری وجود داشته باشد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/18948" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18947">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGA3DXtgt4PX3aep6WJGkh1_BDqXZdle-X-jdyIJGqypWIrmI9Aravx3djFFCF0jA5xPOGt6fNQmZw1dFn4_SMlpDpxIBJOhyyC37AYLtil97Btd9NwzQAegETSMM-Xs9koSp41tTD8DEbAEMa1g65O2WWgbI_oQh3ck5Us9c-IqRaIkRBdNAwsLzSvrD3Hr-p1gTJxUl8lX0uXEOdJNnXjtu5s7fimQxNJL8GIID6DMXH7VFiiDCVBD_wfmyVifbl5yz83PdDDfoVsxJaEYr8l8wFhSTqXMnYmTZeJ9f-XkQe5fc8uJumGyx4TLu0RaAV4SoxxnOJAUZBj-_sbkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار تشدید بی سابقه تنش ها می رود...</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/18947" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18946">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/18946" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18945">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT1rMzf3aTnpqB7VoHLpmyZIeOaAmvROFJAdvUQLJzs8FhUGEY5aasQEVyv1helyLWAXaMqAbdP9a-tiZ34k0FZ2OLrf2YeEXOZ7cf1Zg-xZn8wQgafsMtb93jIrT74A6QecyIrvsAbF6hQlwUs_-ZmGIYDlE86bWnw0M4ig8G0EoD-ozfslJNikLnwK6qQ-IJ-jNlWNY18E8Xf9u-1CAVlFah1wk_x7jtLv0MNrq8PJ1VKAHuYDnlYeOp4BnEGSM9Hgo3h5SQ3HmCG8LQTZ-ld0zdWDkRGO3jEHus-wR0MZTai2_oxQYLp_YT_k3CHbGaTj2KYc7ef-3ugjX4v8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ که به نظرم به نوعی تاییدی بر حمله زمینی است.</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SBoxxx/18945" target="_blank">📅 20:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18944">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.  در حال حاضر، یک نظامی دیگر مفقود الاثر است.  چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.  سایر افراد که دچار جراحات جزئی…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18944" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18943">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فوری: دو نظامی آمریکایی در اردن در جریان حملات موشکی بالستیک و پهپادی ایران کشته شدند.
در حال حاضر، یک نظامی دیگر مفقود الاثر است.
چهار شهروند آمریکایی با بالگرد به بیمارستان‌های اردن منتقل شدند و پس از درمان، ترخیص شدند.
سایر افراد که دچار جراحات جزئی شده بودند، به وظایف خود بازگشتند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18943" target="_blank">📅 20:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18942">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rP4sVPts9uIqsUuZeskW_hFPLhauHVs6JzQvd6H6BCvZpr4PdirkR4pe4vrAqTl_0i4WmRWNDuLqiPrcLTyQiTbYaxrEdpql2ed2PLr76hrGGxfqv35XbHbFvW56yv_upqc-IIq7kcFnKB3K2-4MFzKTA1miDydxf-7y2UHnz2ESdo_BS19lcBnd0DYyGrVHeidgb-KEzgoXiMqY247ThMmsHjme1qG0LMZnpQnKkDZjyo1oKTgd3Q8duvTN_xqSePweDT_rcceVqA6jegc-LmpB_E9I18691XHwlHgI8ZPMBx85kBPWV3tfx7tx2qULFNIVWzS-pzYaq8SQP2SlqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام می گوید در حمله سپاه به پایگاه آمریکایی ها در التنف سوریه هیچ تلفاتی وارد نشده است.  اساساً به نظر من حمله به سوریه پیامی تهدیدآمیز به جولانی بود که به حزب الله حمله نکند ولی اینها جدی گرفتند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18942" target="_blank">📅 20:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18941">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4886d9a21f.mp4?token=f8o2ZK21ZxQb3iBZYjmufzWXr93cl5G7vQSvyXdYPr3z55hIGjdFfUHAHNJqrCRdaexSItRRhywKQVseEZdoptDM3P9tTY1k7ybRcOFfKSfSN8iNESeW5LYUr262Adp5ySk6-P3Rk4YCpIJSi0zrVAcoSTTmv8sgmvmIV1WcgPS-0CFDOWFt8B1bv53gcEkiHtCLtToD9mWx965NgDfJogDFxgO1_eJMvTFLRy99zvW7V_alNZB8SXhrMbFDdsJw0qJO5FtL-r0rs7pX6oBGOdSVMt4rfV6qnmYsN04FPhjHsej8D87iDIRJ7ZnqQKvEpkqq9NgDH7K_e67Q117vmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4886d9a21f.mp4?token=f8o2ZK21ZxQb3iBZYjmufzWXr93cl5G7vQSvyXdYPr3z55hIGjdFfUHAHNJqrCRdaexSItRRhywKQVseEZdoptDM3P9tTY1k7ybRcOFfKSfSN8iNESeW5LYUr262Adp5ySk6-P3Rk4YCpIJSi0zrVAcoSTTmv8sgmvmIV1WcgPS-0CFDOWFt8B1bv53gcEkiHtCLtToD9mWx965NgDfJogDFxgO1_eJMvTFLRy99zvW7V_alNZB8SXhrMbFDdsJw0qJO5FtL-r0rs7pX6oBGOdSVMt4rfV6qnmYsN04FPhjHsej8D87iDIRJ7ZnqQKvEpkqq9NgDH7K_e67Q117vmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته می شود این ویدیو مربوط به اعزام صدها نیروی ویژه آمریکایی به جبهه های جنگ ایران است.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/18941" target="_blank">📅 20:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18940">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarket Podcast -- 8.pdf</div>
  <div class="tg-doc-extra">210.5 KB</div>
</div>
<a href="https://t.me/SBoxxx/18940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 8  جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/18940" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18939">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 8  جمعه 17 جولای 2026</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18939" target="_blank">📅 20:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18938">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بلومبرگ :   قیمت بنزین خودروها در ایالات متحده با تشدید رویارویی بین واشنگتن و تهران، بار دیگر به نزدیکی ۴ دلار در هر گالن رسیده است</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/18938" target="_blank">📅 19:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18937">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عراق، قراردادهایی به ارزش 60 میلیارد دلار در حوزه انرژی با شرکت‌های آمریکایی امضا کرد!  شرکت‌های غربی فعال در حوزه انرژی، روز جمعه، ده‌ها توافقنامه را با مقامات عراقی در زمینه‌های نفت، گاز و پروژه‌های خطوط لوله امضا کردند. این اقدام در حالی صورت می‌گیرد که…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18937" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18936">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انتقاد شدید علی‌اکبر ولایتی مشاور رهبر شهید انقلاب در امور بین الملل از نخست‌وزیر عراق  سفری تأسف بار، بی‌موقع و تخریب کننده مجاهدتهای ملت غیور و مجاهد عراق در تاریخ چند هزار ساله این کشور بزرگ، توسط نخست وزیر جوان و کم تجربه، آقای علی الزیدی.  وی تأکید کرد…</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18936" target="_blank">📅 19:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18935">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟  قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.  در بحران ۲۰۲۶ نیز با وجود کاهش نسبی…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18935" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18934">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزارت خارجه قطر:
«ما مجدداً تأکید می‌کنیم که هدف قرار دادن نیروگاه‌های برق و تأسیسات شیرین‌سازی آب در کویت از تمام خطوط قرمز عبور می‌کند».</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18934" target="_blank">📅 17:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18933">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18933" target="_blank">📅 17:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18932">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟  قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.  در بحران ۲۰۲۶ نیز با وجود کاهش نسبی…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18932" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18931">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpBcXTcJuF4Mi-_e1GKy8mrOHzqmXL9IcMbKlaBFiRWI5zkJIcl7Ns8MDpUTgq4bDxT-oUf0fJzFxgwL9LY-oSwmKFF3fl4A-nIZjxtvlQ-P3S9lI7Lay4t77GZb1bjYcY94jPiqRDRf6rzcbQxSY3JJ8zERZ9pF0QaX9sc7zQFu4FhKkasyO2LmFww5Agy5udldB5Z8fMehZ7Zh2PWowCAo3iW_7YqVKDJ1Gq8Edih6yv0c7q9aLZkJ2k1JDQ2gpuSshVPt1T3IMf8P7CnP-48o8YCLHRslAF4HXII8XqSVwTGLGZnhLx73IWbkv_oZkvrmSm3recFK14WbcwDajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا قیمت بنزین بر نرخ تأیید ترامپ تأثیر بیشتری دارد؟
قیمت بنزین بیش از نفت خام بر محبوبیت رئیس‌جمهور اثر می‌گذارد، چون مردم هر روز مستقیماً هزینه آن را احساس می‌کنند و افزایش آن سریع‌تر به نارضایتی عمومی تبدیل می‌شود.
در بحران ۲۰۲۶ نیز با وجود کاهش نسبی قیمت نفت پس از آتش‌بس، ماندگاری قیمت بالای بنزین فشار سیاسی بر ترامپ را حفظ کرد و به عاملی مهم در کاهش نرخ تأیید او تبدیل شد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18931" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18930">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کارشناس صداوسیما:
آمریکا در مواجهه با ایران کلأ دو راه برایش مانده: بمب اتم یا حمله زیرساختی نابودکننده</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18930" target="_blank">📅 16:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18929">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaxyS9uqAMTaJVSApwPnEQRqaFTlF4aRdrBjy-2hNF9HOIv1P_NVzkqlYGCDV3zphY_rM1Umw6LGZ3ZXPdHjDw7-Y2c-3MzP1EWtSMpr137ByjVc3BK9f_FI1WkNX398bi7gI0jnQ2OmxNG0Oy9vYVe2ZCPBqNel6QLkuD1foesZBKEM5ixGY37JiYaDtCmFH347uHs4RwLm_V2YV_1rTVOSbJaMJnnP32uuci2L57lQQKrKVYUjggZpB3d3Gh4EnQJQQov9UStXBgHnD96SM5t83uSmR86CuhAx12PcuDvahu2bbfBIl9actaepuZFXZRVP-xSWWQ3R3nHHyaRPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهداف مورد اصابت گرفته در منطقه از سوی سپاه</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18929" target="_blank">📅 16:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18928">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">موشک‌های بالستیک ایرانی آکادمی امنیت کویت را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18928" target="_blank">📅 16:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18927">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18927" target="_blank">📅 11:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18926">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d467cc7c82.mp4?token=W87cWBW-cXsHO3Zx7DYA0Qv4GcTW2s1jNm7hh9B9_Dh-36TYDCRjbMmNmqOnzULF6VlUSp8QEFAxvYUJi5_bwrSMY2McorzrRqNj48zyBnX0aO4FZynlDaLW2HElfUOMcqrbQ06NWPhzSW2pmt-3k0Pm4xJ_Lty4UZ_DEFkT93bsVMovmc41yQaiigEe9UQKcwb46NG-V48BT7TK-dXFzKLqoYumsgAp6_oMPejYxh6f16augBHQ3jkTa35Z9ibIUvi9uxMBF-cvnCw8ezk46ZmU7EmeDg3FFDaU07R4Rgb9twCzQeGDvl-qFT6LI_wtnkti1x9HI3yUmri9fzLiKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d467cc7c82.mp4?token=W87cWBW-cXsHO3Zx7DYA0Qv4GcTW2s1jNm7hh9B9_Dh-36TYDCRjbMmNmqOnzULF6VlUSp8QEFAxvYUJi5_bwrSMY2McorzrRqNj48zyBnX0aO4FZynlDaLW2HElfUOMcqrbQ06NWPhzSW2pmt-3k0Pm4xJ_Lty4UZ_DEFkT93bsVMovmc41yQaiigEe9UQKcwb46NG-V48BT7TK-dXFzKLqoYumsgAp6_oMPejYxh6f16augBHQ3jkTa35Z9ibIUvi9uxMBF-cvnCw8ezk46ZmU7EmeDg3FFDaU07R4Rgb9twCzQeGDvl-qFT6LI_wtnkti1x9HI3yUmri9fzLiKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حملات پهپادی اوکراین امروز، بخشی از منطقه مسکو روسیه توسط یک ابر ضخیم، تاریک و هولناک پوشیده شده است!</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/18926" target="_blank">📅 11:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18925">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک مقام آمریکایی گفت که ایران یک موشک بالستیک به سمت یک پایگاه نظامی آمریکا در عربستان سعودی شلیک کرد.
این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه اخیر است.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18925" target="_blank">📅 11:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18924">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چین در این 4 سال مانند یک زالو، شیره جان روسیه را مکید و اکنون به دنبال زامبی کردن روسیه است.  ادعاهای ارضی چینی ها هم بعید نیست دوباره ضد روسیه مطرح بشود.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/18924" target="_blank">📅 11:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18923">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9oAUjY42Vfpn_fbYYR9V-9EePHdC3ikeMUNkdpz7tKyS_OyP3la0EcxynDEWuCudCwszEwN8_qUtZZXoPoXvUk4ZuIu7bT8GGwFqK5k8s4Go07D5xN7R7EykKqtb2-kX6dHnvhaeVIIn_zph7geLtd2n5fMd2Yfqq4f6Nht8BB1lkZkejXYvzFbLFmVu2OTk72i54Hx-v8OmnhdPo4u2P-fX5KXn7jYsfG1l2KnVgthcXjMaiEiZxcLO4XgA6H7wbr1AevN36eZXjghw4jQaXaOAsD1dTpPr5v3vYYewd_e8BzzH_mzAkqFFfoQGRlVF2BOcNXk1comDtItHiVXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه زمانی تراکم حملات ایران به کویت از 3 ژوئن تا کنون</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18923" target="_blank">📅 09:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18922">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پرس تی وی: نیروی دریایی سپاه پاسداران انقلاب اسلامی، حملات هوایی و موشکی را علیه اسکله پشتیبانی سوختی نیروی دریایی آمریکا در بندر الاحمدی کویت و همچنین انبوهی از هواپیماهای نظامی دشمن در پایگاه هوایی شیخ عیسی بحرین انجام داد.
این نیرو همچنین، مرکز داده‌های اطلاعاتی باتلکو متعلق به دشمن در بحرین را هدف قرار داد و یک مرکز ارتباطی و سیگنال دهی آمریکایی را در کویت منهدم کرد، در حالی که کنترل کامل تنگه هرمز را حفظ کرده است.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18922" target="_blank">📅 09:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18921">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">استانداری هرمزگان:
پل محور رفت سه راه‌میناب به‌سمت
رودان
بعد از دو راهی سرزه مورد حمله دشمن واقع شده است.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18921" target="_blank">📅 09:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18920">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سبحان الله!
شب خوش!</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/18920" target="_blank">📅 01:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18919">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">به نظر می‌رسد بانو وضعیت پدافند کویت را توصیف می‌کند!</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/18919" target="_blank">📅 01:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18917">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اثر جاودانه بانوی دو عالم — لورا برانیگن — به نام Self Control  که در آن میفرماید:  Oh, the night is my world City light painted girl  In the day, nothing matters It's the nighttime that flatters  In the night, no control Through the wall something's breaking…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/18917" target="_blank">📅 01:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18916">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اثر جاودانه بانوی دو عالم — لورا برانیگن — به نام Self Control  که در آن میفرماید:
Oh, the night is my world
City light painted girl
In the day, nothing matters
It's the nighttime that flatters
In the night, no control
Through the wall something's breaking
I haven't got the will to try and fight
Against a new tomorrow, so I guess I'll just believe it
That tomorrow never comes
A safe night (You take my self, you take my self control)
I'm living in the forest of a dream (You take my self, you take my self control)
I know the night is not as it would seem (You take my self, you take my self control)
I must believe in something, so I'll make myself believe it (You take my self, you take my self control)
This night will never go</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/18916" target="_blank">📅 01:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18915">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18915" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دقت کرده اید شبهایمان شده جشنواره خبر و روزها همه خواب هستند؟!</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18915" target="_blank">📅 01:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18914">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دقت کرده اید شبهایمان شده جشنواره خبر و روزها همه خواب هستند؟!</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18914" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18913">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ایران اعلام کرد که یک پهپاد MQ-9 ریپر متعلق به ایالات متحده را در نزدیکی بوشهر سرنگون کرده است.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/18913" target="_blank">📅 01:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18912">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">از کرامات شیخ ما یکی این است
شیره را خورد و گفت شیرین است</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/18912" target="_blank">📅 01:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18911">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سرلشکر رضایی:
هم اسمی و هم عملی دیگر چیزی به‌نام تفاهم‌نامهٔ اسلام‌آباد وجود ندارد</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/18911" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18910">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.  ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/18910" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18909">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اینفانتینو: فیفا تأمین‌کننده رسمی شادی برای بشریت است.
ترامپ: مگر اینکه تیم شما ببازد.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/18909" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18908">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تسنیم حمله به یزد و لار را که فرمانداران شان تکذیب کرده بودند تایید کرد!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18908" target="_blank">📅 01:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18907">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الجزیره : وقوع ۵ انفجار در شهر یزد، در مرکز کشور.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18907" target="_blank">📅 00:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18906">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این توافق اساساً نوع مهندسی و طراحی اش به گونه ای است که هیچ وقت به صورت آشکار منجر به حل کامل و قاطع اختلافات نشود. عمداً بخش های زیادی به صورت خاکستری و ابرآلود باقی نگاه داشته شده تا همیشه بهانه ای بر زدن زیر میز وجود داشته باشد.  عین بلایی که سر ما تریدرها…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/18906" target="_blank">📅 00:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18905">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مهر:
موشک‌های آمریکا به مناطق شهر اهواز برخورد کردند</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18905" target="_blank">📅 00:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18904">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چی بود امضا کردند اینها؟!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18904" target="_blank">📅 00:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18903">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Memorandum of Misunderstanding!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18903" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18902">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اخبار تاییدنشده از حمله موشکی به یزد!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/18902" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18901">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18901" target="_blank">📅 00:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18900">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شایعاتی تاییدنشده دال بر پیوستن اسراییل به آمریکا در حملات چند روز آینده منتشر شده.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18900" target="_blank">📅 00:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18899">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سپاه پاسداران:
اگر آمریکا به پل‌ها و زیرساخت‌ها حمله کند، ما دارایی‌های صنعتی و فناوری اطلاعات شرکت‌های آمریکایی را که در منطقه حضور دارند، نابود خواهیم کرد.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/18899" target="_blank">📅 00:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18898">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حملات ایالات متحده به لار، استان فارس، ایران.
گزارش‌ها حاکی از آن است که این حملات با انفجارهای ثانویه همراه بوده‌اند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/18898" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18897">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رونن کوهن، رئیس هیئت مشورتی کمیته وزارتی اسرائیل در امور شین بت:
«پس از ترور رهبر ایران، یک سوء قصد علیه یکی از اعضای خانواده نخست وزیر نتانیاهو انجام شد که در آخرین لحظه  خنثی شد.»</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/18897" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18896">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">همین مانده بود که یک راس دوزاری  دستمال کش  بیاید گه خوری علی دایی را بکند!
ای مگس عرصه سیمرغ نه جولانگه توست...</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/18896" target="_blank">📅 23:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18895">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">محسن رضایی: اگر حملات آمریکا تا دو سه روز دیگر ادامه پیدا کند وارد مرحله تهاجمی کامل خواهیم شد
ایران در مرحله تهاجمی کامل دیگر به مقابله به مثل اکتفا نخواهد کرد و هیچ مرز سیاسی در مقابل تهاجم ایران امنیت نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/18895" target="_blank">📅 22:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18894">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVnNOqn0DkOJrGx0ILanKluz9-pWKn5sTK92WhwySSmXiup2WXh50BXY6UPsMDVyazDewqdFBQLMaUABK12psqL83Ru_a7V2sX_vad2Nnkkp_oL4-D6YdFB9dVa-xJ2AxS2ho4BFb27j-M_4axHODcb9FKl48tfVQsmCr_RrsYOAUhdaz1LhG6ZTjcnuF8DbURZlOAywO9-Pm2DrqzVxr8MFjcm2K2JstqVG9hDQeVldUxJ-FVNgglfpCp2wcIQvwce38og1xQnRJJ1YRml47yorxCvMZnxwlNS_Q1rKyZrbfS409KPcOF9bjcwfeeSD0V99chJCNh19KgckqvghYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/18894" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18893">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">داده فروشی به سبک ترامپ!  شرکت رسانه‌ای خانواده ترامپ، Trump Media & Technology Group (TMTG)، قصد دارد سرویس جدیدی با نام Truth API راه‌اندازی کند که به مؤسسات مالی، صندوق‌های سرمایه‌گذاری و شرکت‌های معاملاتی امکان می‌دهد پست‌های منتشرشده در شبکه اجتماعی Truth…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18893" target="_blank">📅 21:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18892">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تحقیقات CFTC درباره اپراتور تله‌پرامپتر ترامپ به اتهام استفاده از اطلاعات محرمانه  گابریل پرز (Gabriel Perez)، اپراتور تله‌پرامپتر که مسئول کنترل متن سخنرانی‌ها و هماهنگی نمایش آن برای دونالد ترامپ است، تحت تحقیق کمیسیون معاملات آتی کالاهای آمریکا (CFTC) قرار…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/18892" target="_blank">📅 21:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18890">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YbmhwkaHlXUoxhgXcUbmgzzsVPFHhdCtZTDrOt7GedGKq7QxlyBBbmHdzqjlV2DJz7vXUO9M5BuaXQ6AIKLKBrSmN4eyoCjxFhuW4gN2VhUouHbPjyWv_hKEaCozJhwufV9m_g8FEn7Zb-U-PzsajfigpzD_DUFx2YLYvYF3JkDmihN9zLJ6qtJfMcTRAGVEGWgNTzBokuy026vPvckC7IzeMofCI11W5Se5DSeUXdF6xzf1AgJpY0iO1bCcUGYZCH1MZEl4ChYq-3phS0xxOAQfV3xlSuYsRqhBJWzySXIGlAEYC1J3UQxqtZGezqdNERGpdWgROoR49sRr0lCEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYIuzUMpk9MOhhRS7LXqOWXb4zLTJdrvqvImz0q0JqtqovVmoOp2pzP6fy_O0oyVP7zF7uQlrLGPpWmfBZOY_XQfTmTa1_9xKN8y2q_MkqJZ1VWIiV4hm9jpeNq5Dlcn0KIsi6NRAACZjziXuKTYoHPQGAgkc45WrI5PM0u_uva_wucgcVWJtA5tJL7nZbHPGGv9xtvtYjzEzHh8VnpAH2TA4oYkCqjY-sFZp4jQWAgfRDS6L8YLnZQ2pPwumq3ADu6j2L-sbLqcMKf-rYOZHKWpJBYg51AqArvoNVfQJV4aKwoAyDtdnUzJExmENZtg9-t8bBmnqkR9eZufQrew3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همبستگی عجیبی میان شمار اعضای کانال با قیمت دلار به ریال وجود دارد!
شاید چون اینجا هیچ گاه خوش بینی متوهمانه برای مذاکرات به خواننده تزریق نشده است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/18890" target="_blank">📅 20:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18889">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دولت ترامپ به اسرائیل اطلاع داده است که قصد دارد ده‌ها فروند هواپیمای تانکر سوخت‌رسان آمریکایی دیگر را به این منطقه اعزام کند، در حالی که  ترامپ در حال بررسی گسترش عملیات نظامی علیه ایران است.
اگرچه ترامپ هنوز تصمیم نهایی را نگرفته است، مقامات می‌گویند که احتمال افزایش تنش‌ها در روزهای آینده وجود دارد.
— Axios</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/18889" target="_blank">📅 20:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18888">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZERnUML0n7z2SMHVr_stkzy6XzDJvv3KSZiBE47P4ZqkSsYLL6Mt365QZaQX79AB7U2LWiYX_Z-HlMRfxDOSGP1-vC8HZx1gFjOS0a8Kr4Vq5x60q38ZbN79W_ZO806RQhQuJalCkNUfryVbqBNl5kMiQ5aIpRFiBDTqyB7VyRTwnZ0AEFT0nXD1pBkG-vxy72i4_qVnAqr_jh5z2prHz4m3nB6q43wWgt2ih0E4s3jJc0BDm662nyH-rvQXXXSuPCryCEQf_IEFwpNxq5LHK0Kw7SB7nBtUD54LESHhH5-ZG272q7W5BZq6UJMoC3Gxmwpl_p72CNH3r9F5cG7Xhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم شاخص #GRI به درستی پویه های ژئوپولیتیک را تشخیص داد.  #GRI</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/18888" target="_blank">📅 19:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18887">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk8kJnerFR1g09jXkUl_cBE4iptKCuvMguWXSbPzwREMS28KzIPLtlv8LrsjeHk_3AZSz5agcvQuUnh2zbTa5AMzw3_MuA6u7KH898HA3swVjzX-Q9eAm7VLlCUYOlX--nsw2zxqfyx7yXSPjaiPnz6mAZLpbpUTCl6uKYaZpcT8C-JhFWlm9g8q8yK-sf-QFDO7WV1R7vB1vkMPG-qV2gl60WA4qgyJ-54UPgdhKMYyspBPtv8Jwxy4ZVejAaG7WCoq2aIt2UKPnGqb1ZP7Bhz5mOLabQ_-XKoZc0wDia5gv5dzlushUtb5Zv8zQ5KmZK_fjpCJ5czvUNfUqfmVvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه به بالا قرار دارد و از دیروز کاهش یافته است.  پیش بینی می شود بعد از یک افت دیگر در دارایی های ریسکی و طلا، از سشن نیویورک شاهد تقویت میل به ریسک پذیری باشیم.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18887" target="_blank">📅 19:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18886">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnT960jaG1_SOOtdfODb6naYinebl-kRCbFU_Sc8cSCyflsV8yBIl3TReztti5UQHoiewzKeGA_FIipWrYVE97ceJWpCcOgx8otGYyqIMfnezxqWv_O3XlpWbtonYGaM4Np1gfAtVzuoXwZ62CdZYSmRLY6uU6Msr3f3KNLx8J-QflCyHNP5R5sGIMeDR0daQFSMJPd4cCv7nGGhr-3GoD38ehD7JhxGWQxVNHoBHaZLo_F4b0oB0FTcffUyxhnQ_QtRUNfe0fgDktBecbNYY-mUTzeDa-zxnZTVvGfe-e5aO2WTt9KCFQEOXPwMPjTcD-giE-WKtyLPqD9aHV6fvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات سوریه اعلام کردند که یک محموله سلاح پیشرفته را در نزدیکی مرز عراق کشف کرده‌اند که قرار بود به حزب‌الله در لبنان برسد.  وزارت کشور جولانی اعلام کرد که نیروهای امنیتی، موشک‌های دوربرد، موشک‌های هدایت‌شونده ضدتانک و پهپادها را از یک خودرو مشکوک قبل از…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18886" target="_blank">📅 17:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18885">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پاکستان و کویت در مراحل اولیه گفتگوهایی برای گسترش همکاری‌های دفاعی خود هستند
به گزارش‌ها، کویت به دنبال یک توافق امنیتی به سبک عربستان سعودی است که می‌تواند شامل حضور نیروهای پاکستانی، هواپیماهای جنگنده، پهپادها، سامانه‌های پدافند هوایی و سایر حمایت‌های نظامی باشد و در مقابل افزایش همکاری و سرمایه‌گذاری در حوزه انرژی را به پاکستان پیشنهاد می دهد.
با این حال، مقامات پاکستانی اعلام کرده‌اند که استقرار نیروهای رزمی در حال حاضر مورد بررسی قرار نمی‌گیرد و تأکید می‌کنند که این گفتگوها هنوز در مراحل اولیه خود قرار دارند.
منبع: رویترز
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/18885" target="_blank">📅 17:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18884">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XolV91h7dU6Edg5p-sR5WkqtMGDX54-NOZLPbyIP1xLNeeI8v3aFPh9j-c8iHx5le36E91PVrU3hgoUFNaqHTrRy3eW3sBAWAs_r6LhUHuDnU-TC3A_rpCYOuwJhlJ8c2BUAHlRDRgnH8FiRg17K5KyAXNIVx1HfOJUnz4FtHIqGeuuDCBWuFiDFNUqlmHza3FaazqJ3tmP16-kqeY9NRKvHm_B2G7Nxj7K5Kdm_Yv0D8Licy6IMZtfTBws6FGosSKcxLRQYOz_Pr5z8TxZjHJxSDYQmZujYl_jw9_BatkHc5vFXbNnsYlSzMXxpF1wB58Be2jDvORziO7c-RA5JAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی همسرت رو میخوای طلاق بدی اما مهریه ش هم سنگینه!</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SBoxxx/18884" target="_blank">📅 17:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18883">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نایب رئیس آرژانتین انگلیس را «دزدان دریایی غاصب» و «تجاوز‌گران» نامید و پیش از نیمه‌نهایی جام جهانی به مناقشه جزایر فالکلند اشاره کرد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18883" target="_blank">📅 16:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18882">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ در مورد نخست‌وزیر جدید عراق:  او جوان و خوش‌تیپ است.  من این را دوست ندارم. من از این خوشحال نیستم.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/18882" target="_blank">📅 15:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18881">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">علی مطهری:   یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/18881" target="_blank">📅 15:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18880">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">علی مطهری:
یک مقام قضایی سطح پایین دستور فیلترینگ تلگرام را داد</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18880" target="_blank">📅 15:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18879">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so7b4fJQtXGIWkIftVkWpTbjEm6kEPcSWCAssFvKYjE3WrohtwDUP2pa9c_OKynPiKvkLKKUt9DmCKRAt6OpvBJQY4f1E5QNaE7QM4pk6S5OM37uG5CdyFm5ZkN59BmOuaaA1ZcriI6MusdmvNd_qnP9xujDCMEHDXfsfzXCinAm9oy8fU7dGft9eKxQk-Xv2Y4NMv9iH1o8DJoyHx83__NkoPTb0pYzAEBvu_-i-iU_eWIsNDwohNIiwMQ6al4rgazWAftNy34F2gNMvZhIvwbRyP3DdVk3mKwN0wrQn_NeFdXRvIOrGZXd1kQ7Lv4H83gL8x62eE6wUeAeH5prhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات سوریه اعلام کردند که یک محموله سلاح پیشرفته را در نزدیکی مرز عراق کشف کرده‌اند که قرار بود به حزب‌الله در لبنان برسد.  وزارت کشور جولانی اعلام کرد که نیروهای امنیتی، موشک‌های دوربرد، موشک‌های هدایت‌شونده ضدتانک و پهپادها را از یک خودرو مشکوک قبل از…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/18879" target="_blank">📅 14:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18878">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بعید نیست ترور گراهام کار روسها باشد که در هفته های اخیر به معنی واقعی کلمه تحقیر شدند و در گوشه رینگ افتاده بودند. گراهام هم یکی از شدیدترین دیدگاه های مقابله جویانه را با روسیه را داشت.  روسها خدای شیمی هستند و هر مدل عوامل شیمیایی برای ترور را که فکرش را…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/18878" target="_blank">📅 14:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18877">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guHBs08RRXyYb8AXXW_aG2zFszxP59ACEwJdDK-ela660Z0eRcKqsu8jfYsU_6VOIicJD9xC1GYmxUQx7xpCdlmXo-LmfsM3LAi61Bhl_qZjKwLOmOU5y3nw9_t-NXry7VQKkAcXgUMboixmi5K23vrbOHIQja7tbhfzn52OyVeeM7DYE0T2l_ZCBOUIwcgOSOFmEsB97U_PKk8ILA__T456yHHHawnObaCzZzvWjeI4gW70dskU7wD7qwh-Wu_4m6iBFFs9Owg3eBm3LJ6uyCPRgvNZu8IADlTWDKtwlNGYfAn-cc9xjhwj7L6ojzcGuLbeL2gIgC9TWTSNesRLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراهام همین چند روز پیش در اوکراین بوده؛ جایی که اصلاً بعید نیست هنوز عوامل اطلاعاتی روسها در آن حضور داشته باشند.   مسمومیت با پولونیوم-۲۱۰ (در موارد شدید) معمولاً طی روزها تا هفته‌ها پیشرفت می‌کند. ممکن است فرد دچار ضعف شدید، تهوع و استفراغ، اسهال، آسیب…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/18877" target="_blank">📅 13:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18876">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMWWY9K0k9UPrrAMDiBDkWmriUce0TjMYsutGmmt3SLohbjy4Oa6sfPMvGEsxZ65UYQAayTSr-_15vkLoeBNvXqklTiPVDxnoIihsV2SCbAOt3o8v4j4_6mcvn6N76jNZpPwWWkwPcsmiNPBYz0KSLcgTzBgDEPmAGVf8_nZH3Yl2n4CItvNSYhpYXTu2cXySKbRUA4KXitecEBLRP-deW4Q8ZK1PKhKnmyz5yq4J0nZN33A1a8cBqdTeKTmBzcZ7RL3XpY9zSg0eqsucVIf9bO-_H5B-DIiQysrRDCnyS6vrlyHwFTB7shH8emtc9Tj4xqdZ5Jaf-ce8FDz-HtkjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توفان احضاریه‌ دموکرات‌ها؛ تلاش نمایندگان کنگره آمریکا برای واکاوی معاملات ترامپ و حلقه نزدیکانش  لینک  #بازارهای_مالی</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18876" target="_blank">📅 13:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18875">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الازرق</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18875" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18874">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
انهدام چند فروند سوخت‌رسان و جنگندۀ آمریکایی با موشک بالستیک و پهپادهای متعدد
در موج۱۴ عملیات نصر۲
🔹
سپاه پاسداران: مردم شریف اردن؛ مردمان نجیب سرزمین قدمگاه انبیا الهی، ای مردمی که بیش از همه‌ی مردم جهان با فلسطین قرابت دارید و با دردهای مظلومان غزه و کرانه از همه آشناترید، بعد از حمله سال گذشته ما به پایگاه العدید قطر، ارتش کودک‌کش آمریکا برای دور کردن مرکز فرماندهی خود از حجم بالای آتش رزمندگان اسلام، مرکز فرماندهی نیروهای آمریکا در منطقه (سنتکام) را از قطر به الازرق در خاک شما منتقل کرد و از آن موقع تاکنون مرکز فرماندهی شرارت علیه مردم فلسطین و سایر کشورهای اسلامی در خاک شما و دردسترس شماست.
🔹
علاوه بر سنتکام پایگاه هوایی و دهها فروند سوخت‌رسان، اف۳۵، اف۱۵، و اف۱۶ آمریکایی در خاک شما مستقر هستند و از آنجا به مردم مظلوم فلسطین، ایران و لبنان حمله هوایی می‌کنند.
🔹
شب گذشته ارتش کودک‌کش آمریکا بازهم شرارت کرد و از پایگاه‌های خود در اردن برای ارتکاب جنایت جنگی بزرگ و زدن اهداف غیر نظامی از جمله چند پل، محلات مسکونی و یک مرکز پمپاژ آب در بندرعباس در جنوب ایران استفاده کرد.
🔹
در پاسخ به این شرارت، رزمندگان اسلام در موج ۱۴ عملیات نصر ۲ با رمز مبارک یا صاحب‌الزمان(عج) ادرکنی جنگنده‌ها و سوخت‌رسان‌های آمریکایی مستقر در اردن را در دو مرحله حمله با چندین فروند موشک بالستیک و پهپادهای متعدد مورد هدف قرار دادند که منجر به انهدام چند فروند سوخت‌رسان و جنگنده آمریکایی و آسیب جدی به تعداد بیشتری از آنها شد.
🔹
اینک نوبت شما مردم شریف و ارتش غیور و با شرف اردن است که به تکلیف الهی خود عمل کنند و با ضربه به منافع آمریکایی متجاوز و ضداسلام، لکۀ ننگ آمریکاییهای اشغالگر را از دامان اردن عزیز پاک کنید.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18874" target="_blank">📅 13:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تیم ملی والیبال نشسته ایران با شکست ۳ بر ۱ بوسنی، نهمین بار قهرمان جهان شد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/18873" target="_blank">📅 13:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18872">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تیم ملی والیبال نشسته ایران با شکست ۳ بر ۱ بوسنی، نهمین بار قهرمان جهان شد</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18872" target="_blank">📅 13:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18871" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📌
تایید مواضع هاوکیش وارش از سوی همکارانش در فدرال رزرو  لوگان و اشمید تأکید کردند که تورم هنوز مهار نشده و فدرال رزرو نباید برای کاهش سریع نرخ بهره عجله کند.  این رویکرد هاوکیش می‌تواند از رشد دلار حمایت کند و در کوتاه‌مدت فشار بیشتری بر طلا وارد سازد.
🔗
…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18870" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6vJLFcB1UqChKJqPfCNLCc6K05LTSoCBLmNzqawVYp6OZ_ydvNVwII670fWFhvI6RQsoOdEIoq4yjPmFTZTcAFFfXHexWIAppC59EiLvDJ9AuCqDOBBTM5Vz4PNBZRxXebBw6YakoNwzUY3xB0rrvWaPYftOvOIbLzefQ5pXPd5CZrwYqahCbHV_S7l05PIK5-rUZEBXNOuo-BnYD7ZNophpvrmE0T-3bxzu70kelNz2jRXw6b28Che8N6pdO5v48Qu8abmwqmCUIwFFqSTaQ1K5nJ8uT_sahs_7H1iKInlF--WoPqA-EzgoTS8XPEL30NHR6lzVcJ-6NZtKLLJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تایید مواضع هاوکیش وارش از سوی همکارانش در فدرال رزرو
لوگان و اشمید تأکید کردند که تورم هنوز مهار نشده و فدرال رزرو نباید برای کاهش سریع نرخ بهره عجله کند.
این رویکرد هاوکیش می‌تواند از رشد دلار حمایت کند و در کوتاه‌مدت فشار بیشتری بر طلا وارد سازد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/18869" target="_blank">📅 11:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hzVDJ-NIWphKcYxjJviN0hXAmZgT1ATqx6lGEaPcvLtoa6vbYB2BscOr42PbaJp9fQfHyHnj3qHUEURGvk_7EZ4iHQJVi80u3rxkHb5twcQC7Nclbvsd6nnIi2TwJXu25AcvUTml6wi7vTi1AzwS0I1_U6S0U-kfA4DvIO3U3J_RZV0qF-RLNhLihmcSZ7-hGILZiIOrsdENe-v-nrwEkj7p2WdzVr4ws_As4am0uy5D9DutN3ki6uxOw6gPRtO80QieFwEsoB3jcUEtdmBnSJypZSbLA2mANxP7XVyxK9cwxIa0fs8CMgWWEMVxMHFUIR8rK4s2-qPBY91Ekih-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ـ
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/18868" target="_blank">📅 11:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18867">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8UIXTL4I6mZb7JFxlqIU1-0-l_tgTUsR5QO8zb2ekTx9X3jTc5BmaDAxEetRcyPpfoSYxb-TCbBu3FMZUn_VvE0QxSwEFdVR8WVM_7r2arRQOYlOAIbqFl1V4dOWBElYpG-rj0NIfMkt3GTz36PX45yEOeyI8ZJaCASNjPfRMfbx2fWBiPZJalvyrpdKZK8FEWBDdUsVtlxFaS0CffZKOcUGqdqRyYvfrtXnor5sgU1nfiNIYtwTkaYXe75nU9INZwNn-jDMAsTYld2SuT0AZ-NwJ_V7RtFnpeQ9zXneAyCWP3uyyYDe1DI9UvUY-RUBIDcXQ4m9I3PkFy5-LKXbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این نمودار نسبت بورس به سکه که دست به دست می شود و از آن عملکرد بهتر بورس نسبت به طلا در سالهای آتی نتیجه گرفته می شود تنها در صورتی محقق خواهدشد که :
— سازش اساسی — چندین بار بهتر و فراتر از برجام — داشته باشیم
— تغییر حاکمیت سیاسی در ایران روی بدهد و آن هم بدون جنگ داخلی و تجزیه
به جز این دو صورت هیچ تضمینی نیست که این بار هم محدوده حمایتی مشخص شده حتماً جواب بدهد.
تحلیل تکنیکال روی Ratio Charts هیچ تفاوتی با تحلیل تکنیکال روی نمودارهای سنتی ندارد و ممکن است همین رنج اساساً به پایین بشکند.</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18867" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6ntZTpxA5pwhpb1oZ77AXv43zwtXh3XlLq4TvO-bjuEAV09srXKy2fjLuPY6s4QMW4xjwn5VxUyTbZ3ZLgFWKNpVaMkufMCTB9jS0Le2lMe2kmWzl1SOTNQf6TvDJmXgvjts34bvEqYAsxCsYawosjjqwnKytk6jXX5gE4NB2i3GlHyASF52HfOGXM6aaf9PlN6LeceNcYvdcmntW6NTCbEJmJs2TKsKo0hO0JKMbnPbbrG2-t7rXcU5HtDK_Frmm_MqOimHQxjmc1sRkAsdvvQW8KmmiBfvPfUSMeg0aUBB9YZvFfckYl8fXdDDzY4HG1feRRGOJ7yB_Gda6nDmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ را در زمین ونس ترنس انداخت تا خودش را مبرا نشان دهد.  ونس 1405 = مرفاوی 1385</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/18866" target="_blank">📅 11:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18865">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy-izK5Y45rtvCIlqe1SmzgJHY055ARgF1Q_tmDMsTWTDm_IzCLmIVm54afj33SeZygEe3xY11pc6qvXbplmSgh_Xj-AvvO6P6LfbKIswOtKeQ6tR1lgC2JBfHtvNwe_HtchjTT4tUOCLg8Qr65BE8yxXVRfKt_a5ob99L5Wp-qBwlMBqTkEfcOuEJPy9wc0SbRusWwVveTWP4LgUG2OK8i6CgHD9wIMc9uFndkgQ5OYhSY9BXGvHgQu6pBOKpN2v9pc1-qTzNl2Of8k4t5G9yBRmf61OOCETt3nOr_C5TWkcww3ApTSvzG2sbzuR1aj4uoJj6me71SPiv0DRTGwIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه به بالا قرار دارد و از دیروز کاهش یافته است.
پیش بینی می شود بعد از یک افت دیگر در دارایی های ریسکی و طلا، از سشن نیویورک شاهد تقویت میل به ریسک پذیری باشیم.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18865" target="_blank">📅 10:42 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
