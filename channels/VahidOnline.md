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
<img src="https://cdn1.telesco.pe/file/sNQ-Aljp-gfT6SLFp9FYPIp1aprCtnhv1swJT_QWv1Xu99NJjh5OeHIdB7mOnnWHxsVz40p6B01M7tObXohVemefqCfQLVlqlVGNl_bhwogmoh_EzOyhMIRkZXAIkPLkO0cp4V0X6C4fcMktUDRABseAy1a65WLk4ydJqKKQJ4i8cMQUQ7JKBr0piM249hO8BhlgdhdhLBMXd_PzMMt8Tqkr_mrxqxpYFY6dAfMEwcHv7iBbh5sgqWaDeQXgLJAgmQJXU5ltAz1Im12Xdhle1-S8B9-9EwCKXTng6YKB_4V25xG3mQs8IA7T4b-InFixOIsPu06z6cFS-Eh2gcSlew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 02:11:51</div>
<hr>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0baDs_PGvHxoUqO3Mn75mGyVtCdk6Fl3baeNgPkr0yYaA8lsHRCuxcbwC64pWU1A6wrmHlG4vSeD0vf0GvVfdvd3BmJVtHiAQ2Yd6dJr0WmB1kt5gL8fvrLgWVoTgIljWiA06vm_oFtwQFcX1obJO-hgNwN0ydKcqM5nq56A2CRBIP-CJCfUAD5HSYzT7w3mWh31f6VjcqS5vehSaYjmqnLL1Elvvh3XKP5KsW699VvzcJkXankZhyV1aW3ucP3L_L6NKLfQAEyD6UztqDUo-kJwgLF5JcBAoYftXdF6uNAQT2F3nzShJGMXMIwHPmWCO800mMZXTnHO-NPRGeLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hwxO1XK9wPN-psG4lEDK58G_F-OrmVHaj8njYVusmcaWqyjLEmzaF-eRj5NW-qpvo8qxQychrjM7baGZqYXmS2LL4h-7y1a3mbwEYnQ74fN_ZO_fnFayHWjrreiwJpTxl2JMxpR0agq4ima1nCjLHiz3h_Kn1I4IwS_av0b_pHDF9W3MuqPUcxxat6sgEkmMZbRnzE3rBFeKy2NQr9YlZaUeoyn3LTtTkfGFz15lDVci_m4PYvj7zd37ghuBsXaCnhjsNbsUgpuOyaygz91DGZdSXa-qnVqhDbhFE1S3aJBTjasF_CkzqpcRXLagWjil8SsXEChSn2APveEITQPIbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SWMCAPbwQUmQUlNQPlomtF-7oeU1NoZC7iLNwmESaTSIRZobueYEzkFhYhIAZYZtf6b0r20jmbICcA9u9TJdRMgJaaep3Rpq58ThqLUn_ZH18EonLDTbDB6DK1zLvA6mUyuJCkDovNoBmVTvYkhQyrakeBu_prS3L5tap12g95q6lzrnxpI3RXctrZeptWGaBEwbvQL1arVf33CQhjcfJXgbuhWoYf7vElHYos7VJlaH47jLyn3woIDIbT1Rc67U46wm4dCwMt7lTIvKpMtPw-9i4b9NaTZts5aYjUzvdIuke8n_8VEMH667jXLNrPDwcO8qgbJhcALM3m-_hHw_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OGIHi5Jf22_qfKG-8t4e7xLc6-7p7e3bUvcMZMpDS8YKla6E-DrgWuUJ0ZtkOI1zaMQMkS5eNvm8k7gYddLc_SELYzZehb9PfPzx3PD8qmUOFFDb1msSL2-TDFNtNFCr12wgDVS4e3bcQ0fLYuzMuQV4epWLh00aHhoqDZOc8V2kl4A3Wnkz3zCqE8p-WizQ94xzr8grbbYNpxVFvu7ofiWRnXqG_dyd0N0SOVUhJpmVKGN9J9bvkGxwHCwC7SFfczISB8F8KqOUTxlsKdH4p5nvBhbAJxufs3LWy9zQsEHs0_4MPRR5VsgIRAOugFs8j6IurBNaZAjIj7EsvDhqDXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OGIHi5Jf22_qfKG-8t4e7xLc6-7p7e3bUvcMZMpDS8YKla6E-DrgWuUJ0ZtkOI1zaMQMkS5eNvm8k7gYddLc_SELYzZehb9PfPzx3PD8qmUOFFDb1msSL2-TDFNtNFCr12wgDVS4e3bcQ0fLYuzMuQV4epWLh00aHhoqDZOc8V2kl4A3Wnkz3zCqE8p-WizQ94xzr8grbbYNpxVFvu7ofiWRnXqG_dyd0N0SOVUhJpmVKGN9J9bvkGxwHCwC7SFfczISB8F8KqOUTxlsKdH4p5nvBhbAJxufs3LWy9zQsEHs0_4MPRR5VsgIRAOugFs8j6IurBNaZAjIj7EsvDhqDXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tAKg3DYmClkoRR8UzAj7CdlJdvb5bYLEvBFUCpI2MqCgJPdBnXkyb7rLrmRsu6xs_43vG9TzxguxX6yG3BF_l0m-t5kgNg_kxsMs2Jj5ojHw5Hfm8jdTsGy9JzHfQ2JstCCNAq9K3Koy4EylUg1N6TCK1aMPk6HlHbmBy5a7NfQEZkZcnzKoC-SLhKXs35C8x5YxHcEubxlvkMHWHNiijKe7vJqicneWl9HXdEGYbQ4qY0YPgUF7hjjCNAcFw-wDsQRJz7wd3aIcSkVcCnYGc9Rf00Ck_FYf6rzGFr3YnCJrCL93MuQsQUD3M6PRB5H-uCHjBzoQQjhOgd-5CPWMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iYPRTKzMJeIi3aiNXbI1YRSI1FRvlHOktIKbeu5WcvE1E2aPdVg72x2iZ8RYJ0FOSEiYhm9OzOxQOY00cfoRgY5OXz84Zn-J5iQwSOaXE7ZG64q7iIA7YZ7tEq7Z5tCEGlEj41DV41KnewNm6zk4w1kahMK_AkrXaPyW9jgKHK0msZHNTqUH_mWm4P8tVscQQi_0Npg4Mf8yTIaSj7FBjGf8I7_2522Zou5InkasCEZeELwDNGTRsxXKiTWml9LhmTQ3fs-NVrhL_MHnZYhYXoVz654k-kumUR9YTS-YtlcV2om9cxI8LjcGtKLUM1kGSLegzwas4MEdRhFmljUkRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=kpArwTsQzr8OBU-ES1F7MjLwbhNOBJERP9-ZOtmXf0xUVoS6e0NvL8xwqc1W97J3wdnjkf2SCY0byEsgiCTI1H6MRuQCocAzKt66AUhCh_Ior99fxES0uwbevxEQ6uUBfEebBpqVeo4o49VyAJIhV9XFyVaBmTXWJzHY0v-HCxQpFtMCy1NXxQSUniDawKIh6_QUZYKKjeqfAUGmSLV5CE5ut_hfpjP_NSU9i6LTRbcuK5qq7INTXKE2DOff-YX7gS_doCTUVbN5Vf-_LEWlNQ13OD0HN5Y6ZCpkSJOOcamNZl-tytc0dJrUET8icjo_lA4lOC2usZ6ZThNVZbtfwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=kpArwTsQzr8OBU-ES1F7MjLwbhNOBJERP9-ZOtmXf0xUVoS6e0NvL8xwqc1W97J3wdnjkf2SCY0byEsgiCTI1H6MRuQCocAzKt66AUhCh_Ior99fxES0uwbevxEQ6uUBfEebBpqVeo4o49VyAJIhV9XFyVaBmTXWJzHY0v-HCxQpFtMCy1NXxQSUniDawKIh6_QUZYKKjeqfAUGmSLV5CE5ut_hfpjP_NSU9i6LTRbcuK5qq7INTXKE2DOff-YX7gS_doCTUVbN5Vf-_LEWlNQ13OD0HN5Y6ZCpkSJOOcamNZl-tytc0dJrUET8icjo_lA4lOC2usZ6ZThNVZbtfwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=ffMf1h7wUpLlAcij9hQugzfHwaEVGndlg7hfO5kt8aCuJc0oqgW135m_JyXm8a40_7r7sX6GVCY1nGv7b_7RuKXNYgAuhwULYs7zes8BWtOpFrQLC9FDduafvealVKY-ny1YhmgcFPFMVr8ITAIoQ_K3Ec3HIwyOIiwHRfeMrFNZc8s7FKakuaXbtXMwajSwwKGWyQ31gLuv_90oyEJFVbD5L219UaIxIV2tvZ35rLO1D_c_VPlcVAEBBFRtHb3i0X9J4hxyE2_kdVOPYdRYzQlTN-8JV4NTaFiN6__nifmFDJ6YFsbYwm6UztHHz_Orr7jXUcajnVow8-F428hl0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=ffMf1h7wUpLlAcij9hQugzfHwaEVGndlg7hfO5kt8aCuJc0oqgW135m_JyXm8a40_7r7sX6GVCY1nGv7b_7RuKXNYgAuhwULYs7zes8BWtOpFrQLC9FDduafvealVKY-ny1YhmgcFPFMVr8ITAIoQ_K3Ec3HIwyOIiwHRfeMrFNZc8s7FKakuaXbtXMwajSwwKGWyQ31gLuv_90oyEJFVbD5L219UaIxIV2tvZ35rLO1D_c_VPlcVAEBBFRtHb3i0X9J4hxyE2_kdVOPYdRYzQlTN-8JV4NTaFiN6__nifmFDJ6YFsbYwm6UztHHz_Orr7jXUcajnVow8-F428hl0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=FBsEE9s7-8tpDSNwWkKRpJ54O7ukFBCVKUDGIzznh9fkqfUj6PATa8OW-x4tLHwkbRlQ5Sn4q7xGJUOm526YEW8Ymcwu4ynbWhmFr_waavJhjUaO7EFRpSQ3gNzBrwYs2VbSXIatsbjn6VAMy2V9j0XGTPIok20Eyx2MMgbmujbUlhiwK_6pmOdKlazGZ-aXXvx2o4hteCtEz3MoZqcEx_ZLa3JaXxZop7FT07WOf-2TnRHah92tAK8qYClb1qQcM-XYaPLFfb_4RehFkQmxDLL1qZX916Tq4JoxgeI9I0kxD8TpemrXIJQ19__U8SyWrztzlzEsw9Gdjc80PkPcvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=FBsEE9s7-8tpDSNwWkKRpJ54O7ukFBCVKUDGIzznh9fkqfUj6PATa8OW-x4tLHwkbRlQ5Sn4q7xGJUOm526YEW8Ymcwu4ynbWhmFr_waavJhjUaO7EFRpSQ3gNzBrwYs2VbSXIatsbjn6VAMy2V9j0XGTPIok20Eyx2MMgbmujbUlhiwK_6pmOdKlazGZ-aXXvx2o4hteCtEz3MoZqcEx_ZLa3JaXxZop7FT07WOf-2TnRHah92tAK8qYClb1qQcM-XYaPLFfb_4RehFkQmxDLL1qZX916Tq4JoxgeI9I0kxD8TpemrXIJQ19__U8SyWrztzlzEsw9Gdjc80PkPcvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8qihro49aoK1z5CB0KzsFUDsexOqAbgeHDuG57g0l8Gep9Vw2TDW91vaEaugSPYi2iUCeV6pW2SL9ixMpXU7omTEb4Om6UD4fBKQ__fVROcQ_u2O5eyEczbYuPtd1zvcfHIf-NMNp36zM3IGoKzTvc_WOQS8S-L_qSf8M2EMIwGhAV46Z5BGQm3cAd6jSbMTpXLXJ--yZuIWsyM87Y5HzuU0otkR8HKjrM5eWqhpohOUV1pgmzLoCL8tsfBo26RWJnjNrryyaIZAQm-dDsIyNuUwWbx3kZX2kCdi-vB8-CmsrK3yJeS5m9nPQgI2Ylm5iXvWKqWQaX9FNpAx6G2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QhIB_yHg41cYSQ9Xfa9XCFJFq5iPPkqJ5jy43Ax95FIiJ5iEPdT4KaoiiKi4sCumkHMfPzfU3ddxkuPYvKkZWzKzYHc_M0-uuex7aKcLOcrVwoBSLNfd_JCKUPlt_wjSkuF0d-u1OGVetGJtD4-VKNOg1PuAmru637t9Xu_u0ob3E0gTElo0RqJUGoh_eZql1Rp8yRzmEJLZodubDojHyadvKsFFPxVNmuJSpmcRVr3ra97rmU7ndsDJvSHpZPw0Oj0OZUmFgnzuaAsemhmdriT59SJ_cPoc07k0cc5lBD2PUnCeOYww3pnEz881pNAugiwX7p-FlJNtAElUWSHrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKsQ9KD0rZMlk9JVfVQPqbkxCdgJCalkMA1_bPrCz1uSrW96LZmsoHk8mEiUP493EV6j8b5NteFN79AseyOzp75l00vLDfDsyJom7heGyTPwmxiRLwJpFDn1nLrJ_I5rWl8vTuRLmXS4WDdiqz44R_tcerSfioWqgPsdv0fhKMatB8xZqHmBMF8Rs0ubpL4UkogD_z4T-aMuHv7WPZJxBMLCsmSfocJsQCG7hEPkE6Oq5Lm-7bECTnnWfzzJSD1kDqRGL1li_MBHGGIbzKPPiOQ9njI6jDEQ_K0zRWZxHZTYh0HZxr6GK_iesJidlTlSBZX3YG_w9_Xb3Eklh8e0KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iwkZj25bdwDmGy9ifDAAbnOIQMlltiyxmCwtOjvkUNlCpPVdZ9o_A09UUmQVFybE9yl9m2jI5Bt7A8dfdIMtcF7iQ_g9ghE3NBTZK71YQrGIwnUciluk5IOHATzpCjSH6QBPkDhQgfKZCE9m8JyAqtan8XQEqse2e4qi6if2kLf4Hw0674qUFy9r_Dt8j69pfjTtqaxq_CeNA-ckjeA90FDZVe47Gthsvpr5eSn6dZvRV2QIU9Yz0fBcEvELp9thngJlpdRwNniRhp_192iPpu0s61Ia5_eiK_3B3KAjUz--fu-kL9i1gPHNwIY1YIqe_j-PJg_ZDEYr9rrrLENgsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uYvoAVnQnfGt6cbiyZ9FLBlNGlfoGZIro2_xYFGGwSg1j383wmoSa3-c_konr7jk0gfL_IMYHj82_kpjbOCrr27YLGeh2WdA_d5BT1l7MWOGQDipmRJhdWIBB2dNVtYhl3MeWxZCjUmvPwOdtYMQXB9QIugK9WcDv1Howw26wfb_D-eeWMJEVymeEZ_QzFhz91PU0Ow8oWwV6BhfyuujTGsaobbOH6j44VUmqUQ7KhkqQlfFvI1oGgiBYYFb0eA-SKaiawOzM7aKOzZnkx5oWDbFYw6uFFaVJ_P0BguT0goWYSum4zb75RAeJwfGPDIuME3QwlSX18ETmCeXQUl2GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tbgx3OKqAHi5mLDnCb53LeuNYfHxVoGFe7WkN_aIwUSGA2E4wwoyYZREWJ1-WxpvC-4LvjmS0ZXlLXcLNpN0NQSDJ1kqdI5KjJSedUP8Vx7NQFCr35WwiiVSU_8Zdr52AA8prvX9TW6Dc9B9Q27_JcMfNtiHkSmtNaq-v0gH7eub9doWBawtjeMB7t6M3cVOzd6Wtk-d1IkLoD81RFOPyy66irSBv43sQuE36IlAbwSEn8LVANa4GhYY0HEjwbZjxjd-cd7E5mf8gr_ZLMAGdyi-Tbn6REYNOd43gYxQBU-orHB3ecPeQ67PT0LRCUAbs8seRyL7O38ZvaWKEz7uiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bpFsZo594K-ah_H7VCG0Kc7bSkCZt6aKjcHFMEAs-Bz3fsBMUOXA5gcjbNFiGjPCnRRfmQtkhavqu0qmqO4FDslOXJHlSWDbZi-vZSkC8mXCmPe3Ht6oS129mAiDUynslvoFJ0bLS33hTTIjAg36jr3zkEUMTQ2E25PCtvG8hzE8tJm6BUKAaSbARrY2YhhNDTHDnOK7grIkaKm2QBKQ_dgvplbKnPUezNcHcmLZ8hZCLpVwGASDMYx5bL17gZfR2SMmDFYzxrPN5D5zsadt8X0WuVLQROgQW80W4F2OeQFlr5ISXQW9Of2-3BUbT0YC8tRsL05m79Fpdv6FJ581KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uQ5P2_k6imbIUrXs-eyZtEiPqDDcOERR4UfMhX4pIBZGnF3bYYijFAQi3x5-ex4C6kaE1KemIK1jGmFZHlrDxBIGlIWMlw2wGgoY5TFtFwGYOyIgLauIqQfPM2-UA2lx-BEZy4AwfTxelmf_-QAucKK5ZOgMGhDuv2istCSGRoF_mUwx5ZkIhqSpbUPx-h7_iyBK5zvs6X4ri5tzO7SPjiBuYnRsHilChzhPi1z6W6uBnwtUzTQZ14euZ9ICfpQETusij8PAv8t4n7TyveoBQ2YTFaSQGVKuKHhz6gCLEPStJWX3S-CXVu6nYOaEryOFfPPTCCCjDzPWMRkb0BUD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rCDgKHh4j6a_SZ0xLIkqu640xpPWR3c1lTMKGLwjBjRrG_6CgzoV24Q-ukpx65GnLy5niN19LO3HROWfkWp5Wj9wg05q2QudTHwQc1Nj2lV4UC3SfcsLYJOy-5rHltrEmKDlKxwdL-jIeT3avhBENqELWRSopGX6912RKTyfAIJfFYKi8d-Pxtiwge2Q9mMPm0RdVPf-4ABrvVDvG4Epy2K301Tfd8OXiFu9TlIbyTseBlzRt-oGFucg3cS46fiidfB1JBmu_fEmB-8hvHbiW3a8iggeS9C_GLTZmJLgX_RVbyTtto8YjDN_At9VYQCVqwDVd_ypWsALnbYXmZ4NCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QiqsHrcdae14HmViGGk4oNsNYMMRH8AVFY8sE55_bHJvcQCbFsc1RaHatbnOWLPeHrQW6uERgH-LqW9FfAB-0pL_486deGg0MbT8A9YGkzbkI4ij8brauiZZfn_yr8LGm0G2MgEUpUvyypRuLtb8e5_rdYyHDNq8N7a8BVkMoaPb_EkSbQR4VWR-9k1Xa4LwF6z6xD3TSHt-aM15uELFUSDdK0nMgBc5ip8Nw9KqkWcjRB_KSI_Vit4mfrepAxVvuPv25Ggls4idTyKo6o1JxT02wMQJZpTenxwo5Cr1Hts3rXEeFhXNaBCYwQPjfhwARBbVPiV5X171suQ4Nx0GbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dri4-dFt9TiBab3k2DLPPPBlRoMT6HhTJPtLERi4ToUS5gsOVxysno8PwbTVgmt8KxptJL21xBsnukVxVyXJzjUka1PoLDDJh2S_DO-xjp--u-Vb3SJ6iqHnh2qKgVWaf-cBiufajAoLrX_ccLuzG8_jDqSQCeWiAytlCsVFMABDLEqbw9n9c60JrqvsS2tM47rltWtPMZiJJaCX8mSiiDOEEZzIOw1x3EF3rBogOvvFSoaytHMCOpmy-9Ke2KOeOUoCnW4OI4PVFoMFAkOg9HjWzgfYplrhfKOSpKyXmWs7VhsPUooHfqgyi6IajKQziNoxJMrLjsJXtxVsQ88IHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hJ6AwYeMdh2-ZcG29ioUckNuaEIKenLArb-jIko7_XP2XikCTxZy8KhN-WFacAPlNrYVWalsKeymSpFcL8-H0T_yXUWeAZPcEYNt6E99afbuSIW3PgAyxH3kpwG1WULCTE4QCAjfVDUm-4Fkp4Wdw2WOJgMSqtpYkF50mkcY7qx0Ee3LeccLqFlkdesF3yMhrBjVcZrep-CnArwGQ6Kee3g1RRd2ltD2DvcZD7JA7OznkBRMI-MK7EyQA3V6yk5ATGUE9-yI60PXe_CCwI3GfzrjHegFbsAzxhDvXK-uN2m0yLGl2GhtzvyKsqS9t-toSP3-ImcawkB39Dr8k2Fk3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aapOBHnNC8ilb2F59TYAtxvCiHto4kLxg-T5XwfGYMQjIlj-oC9mS7Ace_vreJRvRGB5tB7RcEnF_Fa30DVj_WyHR3nPF1qfwP89WTdMjzgZlRqFJ8xsNxXT6HdKn-m2ygr2y-FfhAnFep-YskDl4BqSe-7pekH6k5gt4Sy17pTq7wl2TASOoySGKMITjE3vplhdaIcdtyh1zaUbo0J_N8cz8tcKZJ_O-cg-KM5L1HqpfO3V3H41h7TlLD9Wa693GurLzDIMiJ_bPxmGCbTc9lj8Ckw1bcsMNaAlntUZ_Ghh0gLTH6cnFM9frf9SKJvfhIsg3O-Fqns1uQ0E0vZ_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpPGOFYT3Fu23WnBXZT3DdmO3FSF1OS4FF2kGD3X70TbORTBceHScXntc9gs90FOJcBj1ayKFHEpObHUiq2Lyl2rqaFittLI1sOrXau-42eHBWJioWljoiV7GvhSxkxeF-j0uFwwICd5W9zK0HJAXpkTm4txfugdfEBYOcV0g1TDYXhEtT_SOAPFdetq49JNq5viBlQuuIL47chVoL3BNKyJ67KTDMQWKrNShdLPIzIVUKYEX52exuCXc3eX4BLANf1neVpThZtFos1j8whIL3KsoM7fGeBJrxssFnNdLV_RjZTyB6etIDhX0Ah1sS13MM6zgCTuGOokd5hg5_Botw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=Eb27NRgqnlHIB3druv-GRDBIFejGYeLcL3G3j4HMRS_Vn6h8ffA9FDUM80WavcM238L6VKeXXdZqljVTA74CCm7GjNRuk3TQRlJg8phjRvxCHx_bHD3Q_TV0muNggnOeuavrb2GYV9QN8FeNm_Z2pq3y2YnMggaLzi0Oi7DriNXffamTHNNyRhBrfQU23JYL4MBz9eJhQnHtaujuSAwhwH5HnJ4GNhFN8PBDdTAa2br_5gi_ws_5yWugNr6jcPFzoE0IW8oLU9L14SnJPMP0ecJXu-GUNAXboW_bW29ZnECop2iBEZHc-sucsXyuiCP_XyCRTe1F021yezuPfPO-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=Eb27NRgqnlHIB3druv-GRDBIFejGYeLcL3G3j4HMRS_Vn6h8ffA9FDUM80WavcM238L6VKeXXdZqljVTA74CCm7GjNRuk3TQRlJg8phjRvxCHx_bHD3Q_TV0muNggnOeuavrb2GYV9QN8FeNm_Z2pq3y2YnMggaLzi0Oi7DriNXffamTHNNyRhBrfQU23JYL4MBz9eJhQnHtaujuSAwhwH5HnJ4GNhFN8PBDdTAa2br_5gi_ws_5yWugNr6jcPFzoE0IW8oLU9L14SnJPMP0ecJXu-GUNAXboW_bW29ZnECop2iBEZHc-sucsXyuiCP_XyCRTe1F021yezuPfPO-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cDDct-XtLP3GTXUYFXOnt8yj3N4Uc7KLFkzxh4tWnHSzT-RqicfUjkLRnwKVeP88lMD_tLAAPaq79i44KrkQ3Lq54WoHt5B7SD1MmZj0aNW6161DKWRXAb55GKULoOdGpYpCS7DEEAdwd3j_SCJOZ8gEpL3cXcu8fltMsvnCgCDHqpQx3wNbDNMWVHnCXjlF9hFe4rdX0m7WkcHKTKTWRXGj7BerkFWQnEvMnlwiWE0gSpE-u9z7h-w4gcxx9WyTvl9r3ngao-ey0cE0Y-od55041ocT8UFjnF2hZswDZ_3SniBmnPN76ukexJBwfewbelDMVjXHyV0mNEp2bbL9Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lNs0XdumXPaiqKLFwNu5gouIH7dHScIk6pRCAVdklQzB9RMP2LyHB4sxtu2bdvwIzDHMMTqMK-oFCqnS71k1fuF8kDq95nSGLfDX7rpjV8hUKCZaVhMi3JayNhk7Tlv1osoyUcw5uUrMkGmvC8LLmOBm0sem_r8lgjlspyo77OJh4_a1RLivJRqyZDPuJZMFQL6eo2i__jGmNUz2_7QvYcVAdfMcGjumAc1ru29RlLqOmIp0KwcJPKdope3bT7x2nq4kck9Or9Zr6NQciCDrybqjFIIGUTJvtFGFxu-EBWbDql9M8kfVqPznpERDPWEhz053ZJrTIh0JZ3ZMTDoXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TvGyhs3V2t7pTqYNlmELmnSKHFUbH9rPlpEdFWFULcPpxCvdGATaviQeCC5SO05oLyQnKh2bF3G7ZmXu7jWvbgol_zeBpParQHk2d5oxfnDG_VNQxUrdukfyLrE5ewuprZC1yifxOuzk6fcNAuOZl-rYn0zxCNwONj6jXVAV-V2e4nUUg7KiY6VI15CJasA1BWfaiQsZaJ6x1Hi6YEWCTmUtkVxMXV9e6rwOzhlDgdt6q6U_3q-EVor3ijXc2qTlu6kI_3I3r5IVgyIYL6NC8J2rC5-g390ZyK1jrSxOdt5gdpAXr860ZzxWR0N6mg4XD26KDlFGbuRZmpdYE1anxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AL-AhYPV_pr0jUvD-O3xRrZlVc6T1XQgzJtTRr4Adpkkj4RJrJvJaUO9nZkA-7sKNgl1ualYEpwoGjMtZzvi0uFWtXF94as1x6CKqiO2kmRWLnkm4Lz650L7k1EBNWTLpnnULyoGYtg4Yx16DSqm-W5wHplQXj2V-7jjWbtNQZVD_O8GvuWZ8aMT0zOpTtFbm9yDCaCCuWjhZmZ7j50Cz_vlqJv4wFDBXSEp5DS0mNO1D3-s6s8SGwTSwl5Whp0E6WrFMibPMqY0IOuyRBCWyfvmjDz7xTxqHKoUririscRpirxq9djlnjAo0L1eXz72A7L_OTK7OwUkIC72e3lq1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a0mesFfMsbj_MFvRtSlOw0s-5g-TmYvG9oaVYQfqYaXDI8S0BZkCe9eEjokIvk4-sxyHn7iBTezGO0jO9lEyF5B9H0HLkvpqBoLXaURQNt0wWOS4ziX_6q6LcwFe4CocSI_wQLwqEp40FX7VRUqK536_P3pFhjBKCtm71OfV9Q4pBAylZ7-vWyPwjAZijTaRRdsqbC4o3JYvdG14_MDXzjVG_eyPcb_Hmihqgl7sJDFClwCLc0mtdgZhhWYWxfcc3bZiXikAsIOAK78yOPtOYNCShioTb0MDtzoLfS2qaG4m1iy76zssvvoZRnnbnv_BwcubTENi02sFo9aRbi1BMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hg_fDeEM114J_8v6dADCavIsHu1gO0RksMjnammnWpN4-4hDHvSaeabty9XoDFf3cnwo5qUojGwsc45gPTai_U5_bIyR4JWbFmdEptsv7DqYijWxSTLsBe4awFojCybwsVdqfVlf2rrtlQfENTf9MJhRC59vmVB79C77kI3hOIL-2D0VdxlxkFmPS5RfnEYDjaph3GaAAwbAol9k1od0brG7Pg3hkhjgMd19hE7XrsLQOLMDaway1aP_YxKCFoMTyQ7412FeCsFaJO7B3QZLi6vp-DQPnNEG5CVBN6FPMqaVGr6HDF2ganZr9SIfZ0zfMWlT-WxakrfcDJ02iwR8wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=kl-ov8H_1TMhdPKU1x4i3uURRujrSJ2vbMqM2AgCj-2_ovEkOPeXpanowXmiHfK9Tx4xKbjnzmWcN3yYdj9wIp8X5b1u8FCpkPf9DcEFNIC88aPBazIxDqR7-Zjh4uBKyWOM0FKLrAIv7MMFlyzpKLOlzpGpdh4ymYRtKPJZH4K_BF-q4dPxEIuOtGbldAex4Mh9nn_UgKvG5dEvNsGSGBgPHfaHUIHNwW3vxjhw3nU3UkPe98HjVY1TStdmJBIglogmFMv_bg9rRYCw9V6k0v0t-ktA90TV6g92wzZtknSz4EpS9zgQ5hDV15TqKCN_ihZAKetbBLHIFe-8mrrvng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=kl-ov8H_1TMhdPKU1x4i3uURRujrSJ2vbMqM2AgCj-2_ovEkOPeXpanowXmiHfK9Tx4xKbjnzmWcN3yYdj9wIp8X5b1u8FCpkPf9DcEFNIC88aPBazIxDqR7-Zjh4uBKyWOM0FKLrAIv7MMFlyzpKLOlzpGpdh4ymYRtKPJZH4K_BF-q4dPxEIuOtGbldAex4Mh9nn_UgKvG5dEvNsGSGBgPHfaHUIHNwW3vxjhw3nU3UkPe98HjVY1TStdmJBIglogmFMv_bg9rRYCw9V6k0v0t-ktA90TV6g92wzZtknSz4EpS9zgQ5hDV15TqKCN_ihZAKetbBLHIFe-8mrrvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sGUQIMxXTUMqnmt2EpcahKQGAFdE_Jbd3Ne-l7ojiq7C8Lv8SCjThH3NICZhEYCCSKrSqHJ6uKW6wwtf7_mAq_GbwdYrW_O7aqF7K1aspJn4xK3xy3WfZXOg8ThZB_E-JXUgL4VP4EK7JGY6dsafCPuZ8VGN5Y18xzxWmDIuG_fd07LjnyjBCkfqTq6y-3l3b1usbW8dCZVN_45zjSq61W4Q0sDcoxl9aNECJ_kf5T0K3Zz-zmdK-DJh5kgJwhXtGLGBJemaEY1L-hbgA-ucVRh1l9lsc2PW4UZffNlVMi3-xhSZ0dv0jIDZbzugldrCXFSZDCIIyUx0gsJx9d55AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=qHs2T4MQ4a8xHBhX__E3Aai_VDpXn1mpDJmlRFzI5HB_U76qxyKLsoZADIuEcKjLTFJLzIaAYi7bfkI-4Fu2L7ylW0WKXk1FxH-XusuXpiBgAcJF0Mg4D-WhNwv9NwxtyP3G716XxYruljtDjblY-g53AIH0xbTuz0hyMlUqYc0iQYYyWyuwMgoFaxiSZHD9c1piXTr4N_befqODQXiqeUm43VXBW_0zFdcKAnKHdPoKowSbCPlCx1sacG_yGu70-w1CuZNlFnUH7x4UJv6KyshWPtoH28HKcy6T5N0kKdOQqGF5W9jGTAfIJJggg9QpaAA1S0oNfB-5lVS0_Uo7ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=qHs2T4MQ4a8xHBhX__E3Aai_VDpXn1mpDJmlRFzI5HB_U76qxyKLsoZADIuEcKjLTFJLzIaAYi7bfkI-4Fu2L7ylW0WKXk1FxH-XusuXpiBgAcJF0Mg4D-WhNwv9NwxtyP3G716XxYruljtDjblY-g53AIH0xbTuz0hyMlUqYc0iQYYyWyuwMgoFaxiSZHD9c1piXTr4N_befqODQXiqeUm43VXBW_0zFdcKAnKHdPoKowSbCPlCx1sacG_yGu70-w1CuZNlFnUH7x4UJv6KyshWPtoH28HKcy6T5N0kKdOQqGF5W9jGTAfIJJggg9QpaAA1S0oNfB-5lVS0_Uo7ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGu6OmLGnOlodg8xcOph4wYApyvrXsJINsKSXap6K3DXShne201hawuhXNFD_HOvwwEkB1V8IKuswdKWkN2uDgBOzU8KQpsbc8ExMi85G0xj00wxqKJ5vaycski-156k8rtCFPz1604HBim2lv6IecEXKZDGRV8OBJDpmf2e3u_kOX4h43qcrqzk7MXmijL7rUwAlFBHYCdrwVG8WwMd_4awP7t-wFQy_3mvV1ujknwKcWy8rcJ3aNR_Z_3zLCuWhCKwMhCLunRo6df4vBUmVNLKDOFVGCU9AI6FHdDCzBPsGDR99Q8JbtLYsBIWhNKs6oaRILXUU7B5bSTfYRUsCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m_xaZ2KP9JcP1IdrpZUnhaSv8SovrWryCQdZEb_7G7UKdfMgNeHX5XX3SvF02-nnknx3TbZ335urauE5c-wkpIfzaEbbT1pFG35J-12352psTa3I6cqZ5AgAvC7nCLn3J9KR96O6rQXJnoESxsHfX9UbZU05Bb0Z2uYTSBdr2-uIELEzXdIP9F3HAcDFSLJgQHizr62xmkOXAyTEZfww4C__5mw-SKwGtjuiOuHzPKwbvbvBSkg2odYzuG2fSKBjJ5UCVnznttp0gLd03iE5cGUHK8fwo_XpaXJWAPhiufXfxi0vxYjFkHPT1KGQIKnjOj8Y58qDnZgXBSN5UF1btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijljZyRt-Gea_L16poI3PpRAlqgkTgcJkXBf3dT1E6oNBqzRZcpQ4YzvqceAVMKauihwx-ejK9xLnLVqbg9yuaMJkgtcDznaYI2QOvnVAyX5e6It11dI-bchK2BDFUwwIF3rj_fPuPwM9Y0eiSfc-Yoa7dYbhhDdHZyhuayysMK6Osl0m7qEejV8rNJO4g2Jvft7zOPJyu8mkUaJpyEqSZrn61teS8ANxmJcZtMLmTWfS3G5a7VKL1uPXndE8gwKEsFOZPLdjMD-zkfjeRFzGjRk8_i5vbzjkTEKBFtPtZj5geDuNki7oPzHosnZW6g6ZePwL_Ji3FcfGRYdNZ0uuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRurstPjYimkoWfFpT3gzAwe2RcRF4oLH1TcMRNLEsGvcAU9ZJ_TUJZzI4RBGiLJxp91pQx0UdggARNE2ZRfpf8UgUs3_qfgE94ktBpIgeGhcP964W2MCkvxJXbhESTzkwq2A9gZtBdoI93ihLWtFZIKsZszvw_oKneK4PbFsaK5EYIPARrbDmDxL0F4SD0sJuqoV5ApTtdEKbaQOy2wZSbB6_MPWpDlp-yy_NxUjbHbcty0IZZvqTkQEi4oMf4_4pH1gCWyy7fMTAMogsJz-7b37ZKsO00HCbnw7pYCYe5pHS6AKZuAtPhXk5GB8GTXkZHlgz6iLhrazXk5hZBldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kXg61VZ74acftTDlpcm9QFElmk8lQAgm4Dbcg7n4-DYuJ2P0Y3beiJLtE544vJoUggOJ8MFZQmSaz111XEVVPStg7pRoe-L0a_kL0Q2jkkvA5znCCFevANrDuG28mJLpdU4eqUx3jBUOODkvVa4MdGwE3Q-WWtFmVW4wykHAnU1-OVFRahhna0pq0mJULp6fBrIj9By6LlfiujBH4u3uo6xtOXfkcB6XpDDhufB9UwirvmL1O_O9CneiCnc-r7Rb9MdyytIu6lTrMStyKoVM1w2_PwjeyneViZtmTECPfFsIjV9ghFPZkUz0ojYF8m43PJoG6hq81Hlh694W6T-s_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=pkyNxO9ERyaJriF4BpDM9SQGD8OKWQGoa6bHWg2tydn7J53HI5zLHfj8IZXxP4o0ng9ZWGGN4KPfAdfRUwa6_xzCT2A16TuR4uL2ZhfSAzHJJCRnnMaYSf7O-e5lmR9pLesbw4yorBWqct3dLA6EKwwSCcQdb4rJ-kB3GhHqJ0y1vjF_uGINQHw86ilLoL8UZL2M1RUYWUzLKtSAGNx1cHZmlsrHBiKFGmuWJttetUeE4cKULmu_HMd8yVViOyMgTQKgEuHx1rbXK-NdpOs-64Ic_ljR1PCBN-XklxvSOawI-qoeVIqnNLrWYTZQUK_1Dn8R6ojOKzKqGc1rTROPfg7dcfOCH2iiHgiivWgph1Bhm-KAz_aPgVlc1_KwSBGpFqCWD3PfWQNODaEaN0xEB6r67IfUq56A3BA16D6i_9ygNjXnO1FlAAuShBf19kHIIP46eGFwpI3J_L-OBKnZyhzJ4zAjQj6UC_VKLWudQ8dH_hVmfkwUpCnZynUgb4o9FjD9LuCiJdpRpe-tWGRZnyi5MdPB_6Nah0IucdXcoB_ecqHU9yyhyRtyx_q4r4Zy0ocEu1QspKz3qJm_ztWNtRN6zB8Zk73qPXJ9TDE5lkLtOi7rKs5FT-odV53m1xX3DT0iwccRplKFhVNGjNjOPOpGF89TktxqB4VB1fKsMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=pkyNxO9ERyaJriF4BpDM9SQGD8OKWQGoa6bHWg2tydn7J53HI5zLHfj8IZXxP4o0ng9ZWGGN4KPfAdfRUwa6_xzCT2A16TuR4uL2ZhfSAzHJJCRnnMaYSf7O-e5lmR9pLesbw4yorBWqct3dLA6EKwwSCcQdb4rJ-kB3GhHqJ0y1vjF_uGINQHw86ilLoL8UZL2M1RUYWUzLKtSAGNx1cHZmlsrHBiKFGmuWJttetUeE4cKULmu_HMd8yVViOyMgTQKgEuHx1rbXK-NdpOs-64Ic_ljR1PCBN-XklxvSOawI-qoeVIqnNLrWYTZQUK_1Dn8R6ojOKzKqGc1rTROPfg7dcfOCH2iiHgiivWgph1Bhm-KAz_aPgVlc1_KwSBGpFqCWD3PfWQNODaEaN0xEB6r67IfUq56A3BA16D6i_9ygNjXnO1FlAAuShBf19kHIIP46eGFwpI3J_L-OBKnZyhzJ4zAjQj6UC_VKLWudQ8dH_hVmfkwUpCnZynUgb4o9FjD9LuCiJdpRpe-tWGRZnyi5MdPB_6Nah0IucdXcoB_ecqHU9yyhyRtyx_q4r4Zy0ocEu1QspKz3qJm_ztWNtRN6zB8Zk73qPXJ9TDE5lkLtOi7rKs5FT-odV53m1xX3DT0iwccRplKFhVNGjNjOPOpGF89TktxqB4VB1fKsMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc-5YclKj42T9UWVc8Ss-7nryC8faVhru6_ZiyEJt56vUhEGzGz9XrPKCXC9i0COliNGv67c6oyZq5Mm0mhJ2rW-91JkPYlTflUMfE1Gl-l5aedegSbsGJUeNikYYH-0kksMduXTDFjLt3I1pZz6ornVVJqoZ8JdS2isfGQXLUilUtOJSf3Fy76PiT2_jtPAyUNRDfDvDjUb9RdLpQX-0ZP3RhA8zIrWOWa60y6m0p4bWMZvHmih_4GMgPsnil1edatCE2OOYzD-ApFEFTEWIqvkRK2Zigrtqz_mohtu5Q_8CQ8OPw7SqYfk0eKnr9IOuxr6z7SeOUF-A4LiadG5Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=dxtl91Bs8x0p1uuZrIFWbEzhQp_jPNwzwxua2AVXbIUPxcuy76BvKi0Ycm1U-2-ORuU8zHfFUhEYhjZg_Hta5GTWpw2iCK1LgGYk8jMKFi7crV4BRrijzSuk1ItzNSC0RlmnD1DGjMxLc5wuEzP_LneVIA61sMAV3ujyVgGqSA7enyXxGsndx0y2DoMTxuWBNsG2uNHKa5j-2rHuv-IFiCiFSnhmrBb_AB2osDpeRNm3OjjkFo4_Ez3pTaysIOA6ZdBotvANc4TqX5aOcllyaWFqeXJ9cOwiGlm-azrZkEYjke2HF-SPLQaXKvX2LRG27aAXZ96LJwrbB0Dy8v_MhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=dxtl91Bs8x0p1uuZrIFWbEzhQp_jPNwzwxua2AVXbIUPxcuy76BvKi0Ycm1U-2-ORuU8zHfFUhEYhjZg_Hta5GTWpw2iCK1LgGYk8jMKFi7crV4BRrijzSuk1ItzNSC0RlmnD1DGjMxLc5wuEzP_LneVIA61sMAV3ujyVgGqSA7enyXxGsndx0y2DoMTxuWBNsG2uNHKa5j-2rHuv-IFiCiFSnhmrBb_AB2osDpeRNm3OjjkFo4_Ez3pTaysIOA6ZdBotvANc4TqX5aOcllyaWFqeXJ9cOwiGlm-azrZkEYjke2HF-SPLQaXKvX2LRG27aAXZ96LJwrbB0Dy8v_MhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=pJB9Wz_zWwOlM3faB-Tk4nRGNgrYvbPQiy8Z1XxHxPX27NcKorWNiaqZkkOwKCGVTmogquZzg2W4_Azm7DDftmCpdoZjOb3GeBizPVu-XYVoz9QgvO_0nGSul3jZDD2Bmb1MO12zZq539s3xVCeLxmWVtVlDPnzCz3xkoCTpczod-u_jrBOw0NJt-dznXO0NXoU7o22IBMp1Slao8K5XA48CIbVLkgmRtWD9cMwRTTPMiZ-I3hUkYzsPHVZDJoiTQQiPIIrRD1YOxx3DDX8b0NFgjKU1FFPGoLCpYHXjgdCk6G_arIoV92jqn5tGbBY30nM1FlPiqK1WkkqFg3SVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=pJB9Wz_zWwOlM3faB-Tk4nRGNgrYvbPQiy8Z1XxHxPX27NcKorWNiaqZkkOwKCGVTmogquZzg2W4_Azm7DDftmCpdoZjOb3GeBizPVu-XYVoz9QgvO_0nGSul3jZDD2Bmb1MO12zZq539s3xVCeLxmWVtVlDPnzCz3xkoCTpczod-u_jrBOw0NJt-dznXO0NXoU7o22IBMp1Slao8K5XA48CIbVLkgmRtWD9cMwRTTPMiZ-I3hUkYzsPHVZDJoiTQQiPIIrRD1YOxx3DDX8b0NFgjKU1FFPGoLCpYHXjgdCk6G_arIoV92jqn5tGbBY30nM1FlPiqK1WkkqFg3SVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=EPIPdjHNeVpsElkyIsKByEyQkWW8yIySQMR3UKNBUQKIFQ5D7QN07oXryucXj5z71Moze7yTYsdbkEx9Gv_WM9xI-qWSnc_SthZJy1-LS9gQs-wV10AIkuu2Qiza_9QL07nKXkY1_BeIsFvPsoVOYXNvzWsWmxJHrLGKndqCmNUWTP8HfXZuRMCin74WdOMUhwnEFFjPo7L8IOU7WwdMhO-rxcCEvmJNRBU-aQkEAWOnx_78ejWM6uvW63cOmRO56scWEOIATQRfU6ZKoMT_v37Ujq2BXaKtVzUqFq6gyxIDcIdG_qFWuUuyN_sPWO5tTlg_l6OrL46zXHtdxeyS7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=EPIPdjHNeVpsElkyIsKByEyQkWW8yIySQMR3UKNBUQKIFQ5D7QN07oXryucXj5z71Moze7yTYsdbkEx9Gv_WM9xI-qWSnc_SthZJy1-LS9gQs-wV10AIkuu2Qiza_9QL07nKXkY1_BeIsFvPsoVOYXNvzWsWmxJHrLGKndqCmNUWTP8HfXZuRMCin74WdOMUhwnEFFjPo7L8IOU7WwdMhO-rxcCEvmJNRBU-aQkEAWOnx_78ejWM6uvW63cOmRO56scWEOIATQRfU6ZKoMT_v37Ujq2BXaKtVzUqFq6gyxIDcIdG_qFWuUuyN_sPWO5tTlg_l6OrL46zXHtdxeyS7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=UpKrdUETbAs7mJH1NwflfCHFuSbRWT-j5raSmR89CIgaSYKVEzq00edgjUW2kFrc4vRWxt541UPwYcmcbvYRlWCI05HyoMNq2VVACtw5CpAIxdKdvvPlRrp4iE8JW27nTvYdTm885YIrHuyu2ettvIGkOibD9YZUyJ-ASNr-bpVY5RtYmXVnNRJALfLsikQYbV4tPD4Fgo4kgN5iqayR0QGu6IsgnxJDMX78Ruq8ITlmiLuAtxZ212Hw3ngPIaKYTqmK8Ds9zL_xpr4aZq9uqdT75t0vZVg6Mno-Ncc4Ax_NQxvl2DJUayW4avccx8S-eW2e8VTNe2B_ovNApF8_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=UpKrdUETbAs7mJH1NwflfCHFuSbRWT-j5raSmR89CIgaSYKVEzq00edgjUW2kFrc4vRWxt541UPwYcmcbvYRlWCI05HyoMNq2VVACtw5CpAIxdKdvvPlRrp4iE8JW27nTvYdTm885YIrHuyu2ettvIGkOibD9YZUyJ-ASNr-bpVY5RtYmXVnNRJALfLsikQYbV4tPD4Fgo4kgN5iqayR0QGu6IsgnxJDMX78Ruq8ITlmiLuAtxZ212Hw3ngPIaKYTqmK8Ds9zL_xpr4aZq9uqdT75t0vZVg6Mno-Ncc4Ax_NQxvl2DJUayW4avccx8S-eW2e8VTNe2B_ovNApF8_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC5Ajhp-uzn24lxpJ6k5b0MZJL1m2KSP4wPi5bGGySrpWLnZWNBhr6r_xXIYK1uhFrFZWk_1zK0PCEYs3EfvSy_sc91JZhr5II2odemjcdcNMuf0qgWtBmV17T-TpjsH_0PAGqPOlf5g6nqbv3PMbkoOWRQ0vvDA2nIyx7lg7i3_CG9YlFBSNR8Hc3mjA7iM3TKXTmctX76QTGw-ASvjs-EDN5pFPyC6N38RhwILZFNuh3xSmjbivwMt82pg-WuGkIVHlYx9I3EdUkQCsXumvHFS2eJhAneTep7WiAT7f652sg-riRbiTXHvdzUEoe6Da1Lise9VecxjtodtE3k2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS8pZwOowWBXZqY9joCRprnmucPWzui_qFwG8qkn0T4QK3mh09e4DrZjlhQDBatbiw7JQpehYhpM-YDUa1o22dc_t7bJbu3-SHY26cHpn73dXInANFS6diKsoqKvSZZzZFDWArVSjBYIPh6R3ZeoHxz9TCZpRyybEqRTsemMRntBR3DwgH2HWYOgZuXeYt4Y5z2-SpN-jDoj_7lqq4TQQmeTec7c9j3Xi8gsxRFF7oeGo2_ft8hW9XCI3wIkNHC6FxDM_qrMLvrTurjRV5zZ0KzrJ3jO75EGC53PmiFU7Vc2th5AQ5OkNwAsrLpB4-7XlOde8zwOcyF3Ysb3gf15cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPkMHw73PxW1NSUazrESjhWyvX3FUjhxcuUnOaPOMxILmNTc_tHeER3DRZR0N3IDEa1t_FAAsVOKM0hVqoO8aoSFx4IMj0bHRZElcU7BkcI4QU6wHB_viDEuIsZSAag5MOVmHcF1K0I6mIDDylCjjEInsTGNUHbgIlfKVHCYrSs0i7SxJIzExC-WETSbf98nWJpIRl8ln4_Ub6923plYLnqYI4WKui8AUNwjzxc2rCd7Ag7Yr3eUxgdxpjVLH8f4Sgib7nT7-VLBjiEsbQqiqHKI9DeqOS5ElpoQ7Un9NkAY2yFnECth6ln8AVAgejOk_I1K463Wgf3AEtvGWOW6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1ZkdZ6bHDfoeuDtvfJVyesNDL2O3eKfRFr1N3HJvZL-m00BXz2JWx6xeJuCp9pGRlU7xKSItpI01Uv0aLDVTaf-Vps0fB5v6UNGOmYIy2qd_0cPtfyiYe-GMfuvEJu2eLEDlpkTcmJAopMuVf0FrrzVMS-E6YGaM5S2eAcOShnxcHSVz1_t1nZy_KX0bOHudf_p7ev4KIkR_AE85dJhMvvgtnp99pruY96-rcWDGgL5WQyDA2Pn07aXdS2akyzSjGgCjEhzJkwrGbbV2Lwe8kTWQ0JlVdRA_xQCHDEsu1xl6UUbqfNEMvKEBGcour3084HljOKF2IkgTYB6BF5mtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zcds6EyBPsoYsEP_mpQXq31G7lEe4PMQSdr-uUK8KltyDQN2EfSKtH-JR2AUqfqwtUxRKYcwFeC7tcYBEGR_KbavocObwm_ehn4b_gF-58W8WFQhXVO0ZukFGCV0EKt9ebO3gwk_g_KhQ2xdHmgOR0_vBFBBqtQFERrHMatTLY7cAIdaKa9btMYLdWb5LHQacycTCTLn8bTIAjZNLPElRLKAFfI4lica0_KAlaD07AHbooj0Dzs1T50sgHpQppkSjoIEmqXBK7iwGCQwIrUHKwu2P78NeIImtln-hqR0xx9osBmaLB2zsByBacVfDXxtfvdcE2GGrydO13D8yyocKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiMxsDjZZ1Kw7Kzwj67jOFzOnlgkmusjk8cUYgY0m5yRqhAefp2L3zOtQZ2E4yFPI1t2sjR9YjoPuzhx-alhzaNO5aX0rxmqdhSMP2BBSEK_UIZRz18bZuGo4QzkZw4x6yWwLMydUTDdIMf0gNcqOsOXer6D-UrKSxD1lVKWt-OrLPLmLWc-fUuWLHpSYMVz2QVLggNLhKCGgkub62OCONRpW8cQvmt4IBm9QIgpxLpa1MkawM_PIp5sJMGM8u6ovC95BQrIBQqUEQ4VdkjK4n6diKvnhisy-J_Ih1aotWyPPwALI6JM0Nwghq_p8CWmQJaJ7_Eb4iO-R0AQv-sAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BR1AySHS6laixGdks-XJJ_7buhtXC9yd58BXWXMTrmfacM9uGFbQzZwy82QsGP72ENJAMrDMozEvSRokJHgZ_n60XdPugZPQiG_1zvDuS84aV-A24OIOTGlueHlG5kko1BQXJQWxCJJTX3B_zZXItXE_CArj9bFS2y0KqcyX9L76bGyEUGhJvFeqkSDNGxmGd8B9NSIpOc50sAoXgI5vqGFCcARXMqrfISB0D2_tMOLcGfql3GBOq__akS4-w-2ySJGzjJcC78Mpn-dI3VkPgooFmYrowd8XtfqJuTzFDRmmuOFrupA9gFIw5r87xRYUkL8KjZIEqEFrGMBT3GICRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNqEvqGwublKKaEmvAnEmhHZCARxpXUYzu4E18ydDcnjrNrykKl4EE-Dl01YjYG6HIzN0JozZh90-8u8HX4SwRiPQrEoeHPFSOwLVUPiMrXPz-wkJ_JJu-iwd5_y9RhuqKJUibeO3a6HR9mr8v5JqFVfiksiFjrlpySJx2IidL1h_0q4TeZioP1THvRqoziZRRRfcL70Zj5gJ7N5wXteBQdVPfqIW0YKMAUFBSnK9kLoj3Ir4uwwV6O-vr6ES5LWNE279OSKYz45fqdB08UINahyM68z9AjcsKURcZibmLYXJdL6vDANwXqrKiRB1oebqZvcKTYHt579dU9Z6KiM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLf-xdGESCjbbbMjMROADkspIi2xUWxqbFUM4wL-RfNBq5T2xWTU7IJLOpzkeZK0gMevYJ40mV42vo1XsKgo4-RtzcU1J1O5qyTmJQO91yIQDB9_nPGjHxu-4b8hhEmwmrq6CLHQ0-DTgAyCzQLTvUKpKlqapszlQDkqYL3cvo9wMpjv5jADDASX0umFFlLckKFnW0iSv1zlGgqNL2XQeaExQB_ENLKDoTIPwAB6gOzzp4r5_bI1BtePcia2i2Hwvs8XQnExBt_em1d2mscNjA7vDowF7VdXrLlVt4QFrmBiztV3FXK1GWNXHIKjg7f0K3CCYEL87FJXlTZxr0CycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gjEZ3Nrt-oeIO-A7uCJpY2Q0zU1cTK56M9QmV9cIYyuf4pUdlVImF7AW5RNTzIXgn51BrcTdi9tzDzPkltNu-fnxf46dAV-emz_QvC7uhDvdeiP2Qkc15U4hAkB-KLPTQaE1UCfcKRq6-J9LXzBzGqeq-QoOJFWXwKYY0X6l6IKjDw-R1noHlH8nbWL3_dTlLOjooeiWfz5lDIzi0DGHE-nZF6P-Trw1QRajseC-_qcH_-04dQZfnexkZ22kHaaWCDXfrqK-46Y6R61yCC6TXvea0Wemapfos7jbObJZgS4S9D5Y_EPVbhERgNsf3xBCqjEnnRyTkN-e-RMEIHFIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ob3RCddogKivZ01Iw6QaGPZEbdRU8hHDhUjbpT9MiclSHB7Qhw_o8ipsGxc7QlCt5YEFQYFSbyw-h17dXiYW_bGMoHTL_BJJOj6r7ZTfEKcm3OuyuGBlu9tpd0Z5y9LF2hGFPBal0-dNuc-A7yeE2l67pQqNIwiT9WPAnM4NyVHJer7PIDN_bTk7O_zA8_C4leR8PTAA4-_48LfzC1Ur0T8fuiTz-hRF5BE5bGJfhZtlmms3OR0L4s4-Gokj6H-WkaLrufdXB98VNovn-uQk4hL_B0LspN58yCf6L8Vw7cMMNBSQr_2ieO-DQW9kdQJxbPHJ2Iav1do6-7cxV7F9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErNnvfcbecZFgSUg15MFShsrg9VLcJBF1-TTzQphqC61nFm1FYcjw8eFmFMHnDdLzbBqYeLQ3th7LFxD1x0mToTj-JWiddEUTiWVTmhbNA7eU8IFPEq44xlhiPu8L04NTg3ZpUZkgu1AhY9HjVBounYnmSjKTtBswT2Pjqm1k5CFumWcFiZdEtiaLoHEXJdRWECcshhVze_z7NFSHTcufBs32KyxMY-YW224934vkCaeDhkY68uUWOEKu8sUaQiusS0s2B4E2_3NIDfU6_eEpfCv0VzK6RqysBL86bPz3hvyn7-QenHsw7AZj3sJxBEt8Ma-ZZaCp0L7ZTDtfH27rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/beSpP_bdGPZ2ssfAIX5yk6Vbx3ePLA-VfaUMZwFN1Jfu0oTG0E8ZPwK_BuO0C-YB4Tsia-y0zvhLG3JmNr4V5DWiMDRPD92bxP3wAXXfajCC_knaw_mbIwEQQH536TtGP2Qi1Hl18D8-314t12I6SBqRmWcy1Qx0v4ejK2VWYMCYYrlALuBfhHljQPM_1rWN2U9M-6mz7n4UcokiMpguEJoQjkh0OY80Yc02E9uY9yC6k_eH_q3aIc3IUHBKCHD_lelxcJW6xbrXb8eteiPbCUY5-1KYpY9c7CCTkHIgNijKEVNpfwmuilH7b2F9TABkoKlUHnyIGI1XHrdvNj36yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1HPGJCKc3yvRwrHTzYZLsi6IMtiUDLXfgFasa2j4DLoZzH03Qjv3rKjDT8wRPKbUdgXsIbZd8dCUyuay1Q3rp9smiFv5fWNje0UDFnpbCacWLbAJkATChOrTBA4KlnwaKFJzNHScMTTY3naIKZmuxsUiAI67apcr1hPtLRTIh3H5kI9C0HnPgU7NyLeKQlc2RR3t11lctBaDl4fBvIrB0ELiFhernln0Kv2-L05yZn8gh96SHw5OvksEiTJOVTKvt5sH3l3jmdwDwdX6BPNofKrcg_uuE3TVeq7Xq0ucgdZ3XPEil6U31S6e8MCnKZY2qYya6KKW2LVbWgztVnPsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7XKH-S8Hcy1cYFuBeK7-VGbd8Ao7BKKgEyDodWKTYsA4APZ-V3og3dSueDi1s17nKaLBF82J1W2qWxkPQY-AcRBC1RXdodN2ZZaazuX_KG0bzRa_Nzoq8K-l5Sd1F-3bSAzR61fDSC5mCu3Zfw3YlThcq4zQV35eh_rpUWPpXclZeVrljibNfiGvR2reqz8Z0pSXsQrSUnIiErAeDA863_9J5Snmz6vUsVYaA_oXSCzaxg0G3n4DEZ3iDc9_aKBNhXaoUvbybaS5RjsJ-iljqY4jy-uvoRBwyZtk-8WisTLKkdcCQVjMz0RYm3eVfIQSBe2vZ6RplSYGCEc3XhYuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=CPiXGKsGorJyM17rA1FM_ScBbG2DAa0bMrUOdrAkB9gywwfe2xpdU8Yss9Z_KeesKNRu_KOO1IGCVENUb_MCAPLQFzgjz5gJsMTF3JsKMp7eef6bg7uRculzNan9EMH7HLIbtsDH1wNBEPC3plgZyJja6wRTlv5YaiRJEEouISh4Qz1MAnwl9UZ8Oka9AHxXiX8zX0V_vmJLOaTHGUD-pTlKDel8XW2NW9w7Cn4XjT0a47U_LQ2c4BhUMAp9Wunp8I9kGzIJY0Sq7DXyS_CgbtbBiI-jupAUtl1vFdfBuicqLinBlcWFny3x8UmYidNa8P_CernBmiACRVHVECOnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=CPiXGKsGorJyM17rA1FM_ScBbG2DAa0bMrUOdrAkB9gywwfe2xpdU8Yss9Z_KeesKNRu_KOO1IGCVENUb_MCAPLQFzgjz5gJsMTF3JsKMp7eef6bg7uRculzNan9EMH7HLIbtsDH1wNBEPC3plgZyJja6wRTlv5YaiRJEEouISh4Qz1MAnwl9UZ8Oka9AHxXiX8zX0V_vmJLOaTHGUD-pTlKDel8XW2NW9w7Cn4XjT0a47U_LQ2c4BhUMAp9Wunp8I9kGzIJY0Sq7DXyS_CgbtbBiI-jupAUtl1vFdfBuicqLinBlcWFny3x8UmYidNa8P_CernBmiACRVHVECOnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ua8od5V9ld0ZOO0OXZxgtBkWcMSGJ0ZEBfWB5Irb-6XtTrfIwMr18vJ3KZX43q24lUv_Oz_IIXN9lXYSPy3ljL1JWnOdg4tZbjHeeycai0uZvJTc9Z369rTw4nkIcl4FkDbZWsY0eeCWXoFbfRCKaxMV_T89X57Ris5Mx7VFJww3SXPQlWcle2YKaUgGYkxsEZbQZm6otuk2WBoLrpDAyRQL83C_bX8TAvtLzRzs5OepK8IgUNxOFDCb26nGfaFZfPeslkbM08IHG3bVOZeCRP3_jgotnQb1hEcHygagtCFa3acW9nCYOojb38wDui1yi0wGjOLLmN65TF14tYEkUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oFbNGwSoRotRFKlrRxJklQ-mhazf1z4iTMSNHHrheoSidL_RUyaJwX9BhtMO0Ezpb6RviLqUabeRqaWFsxuRgnnoUWsFSDKNmbG-Zb8D1P5eJ6y-W3y6lcbQTJLvwDi2yq-WXTu8zP5EKued7rx-S03QLXmxe2NI7mL_wsXIGoxVcplynBlcK5evAOCs2hjNGkM3XLCiSkOpeI44NgrtASa53GnHMRH66zfky6Pv2_eO2m7mQosgMHbPT_Gqx5Q3gHvfI663mM6YSEigFS0tz1bR_AcPo2IIknUWYSG9l11dJj_gpecGRl1W0YszA8QIyePKcqDA6g4XSMpnKwcPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=aqwam12AS3iaJSLouARf1RxiOXaslDqaTAOtmaaEYHk9CETpvM1-ls2pcxyBWrmcTsaVG0dqkLTJVuzAbdNS0B2t9HxILx4_lIAW4SNkSs5ZTbdY3YuonRXCuVjD9GXM9UOOMH4dWnBaADTorr2DeljIt_nlA9kLXkjAenj8ARSr8FCiyJ-3WZn8wYV4fzVoM1CJW_CgJnS9GPs5v_j9e22Q_elKaDVRFYeV-HqpNMfmPXrorVVwgIMkp2vN_JPKeoez-kXnu6IOke3EV16fxsvaoGxz6Y6Ct6nViVI07i4M-2N0-TQ6WwZiAwfNP89JlDshr4SqcJp8Vp5f82p6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=aqwam12AS3iaJSLouARf1RxiOXaslDqaTAOtmaaEYHk9CETpvM1-ls2pcxyBWrmcTsaVG0dqkLTJVuzAbdNS0B2t9HxILx4_lIAW4SNkSs5ZTbdY3YuonRXCuVjD9GXM9UOOMH4dWnBaADTorr2DeljIt_nlA9kLXkjAenj8ARSr8FCiyJ-3WZn8wYV4fzVoM1CJW_CgJnS9GPs5v_j9e22Q_elKaDVRFYeV-HqpNMfmPXrorVVwgIMkp2vN_JPKeoez-kXnu6IOke3EV16fxsvaoGxz6Y6Ct6nViVI07i4M-2N0-TQ6WwZiAwfNP89JlDshr4SqcJp8Vp5f82p6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=UnYI0KxYnhLon-L-2pbDVPz98_o5-7VXZqWO7gTVhCaejRKs9roOdpJZeY10A_EuvWF67Dw2-mBqWalcB667cZDXNoA5FHz_MGtD2NQayV6BN-wJ2t0OQdMYZS6kvH6v1LS3tqQ0qNqNYl6bu2wvn3IHdeISkjRVwPhvCFrdfrISrIrmz_uERF-qDZMPI1-p5CCzwlsfhQbkQTvUxvUpCCAtlgBkTh9WObtgt5O2b0urtvXPc9T0Fd1lgpuO7oxTwup7sb7ytwyveoA2rQTh8TGnmEfTPHji6_MkXSYxEeTmZ1FhAxIbJKikN8QVxMFrBB9WCKL5X0JGVgAQPNMonw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=UnYI0KxYnhLon-L-2pbDVPz98_o5-7VXZqWO7gTVhCaejRKs9roOdpJZeY10A_EuvWF67Dw2-mBqWalcB667cZDXNoA5FHz_MGtD2NQayV6BN-wJ2t0OQdMYZS6kvH6v1LS3tqQ0qNqNYl6bu2wvn3IHdeISkjRVwPhvCFrdfrISrIrmz_uERF-qDZMPI1-p5CCzwlsfhQbkQTvUxvUpCCAtlgBkTh9WObtgt5O2b0urtvXPc9T0Fd1lgpuO7oxTwup7sb7ytwyveoA2rQTh8TGnmEfTPHji6_MkXSYxEeTmZ1FhAxIbJKikN8QVxMFrBB9WCKL5X0JGVgAQPNMonw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRI75wZDZcvQ_ht41QbadpMS9O3w4dAPudvKXqHUY6NR8jkm3v-xYqwME2MdS_Lq58Y3jNuR32pxFXPw-IJfXUEZY-yxee54iDBH2ZzJ88itmNTCEfgA_pmp_3j_04r61UhKnjgwLk8HqfpiugCdKgtbDqAylcOHKeuaL4NE8wf_kp8aY-bpBzQneOxV54ZNg1cd-QodwXe7wpwXGl096OmPu5hpgrgjd6BkKnNNNw-bLZOePSkdVm7qQpUKdNiwX8UMkNODWKgKpAZK0XmDuX18fX4A1XRRzw1XlyrXDsnA78XJ3ZyZiXkflK0GHROO_tnxf5BsgfZHl9JfMp-ZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=KmLA54tjHIZ884I0ESf6IHKeb2NbdscWPp3tkJzey-3ObL-pOuH4SoGxI5Ywu6Xgfe_DhMJh3TLL2pArGkR5Zcaleengx6hC7_e9HFpe6R9-NzjbV78rF2jBDenlYVMQWNf5jxYEhXCkI8hUv50Fiuv_f6u5QFvvjWkDd3ah3Bf14PcXE_lGjK38nde8qFy4kR8v5QKl1LzxhMQoN9XWqz5vUGK5ESDGQM-SsfHCnRVYiUzU132Vc6LuSUfuGHLaDzOeLYysQMofncxRM_o41EGhAmkyRnV_1Q9y4Xkyv3CRPhxnMb2PqvXDjmE8sTVnD2pQNpiKE2aGaHyWflMZwA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=KmLA54tjHIZ884I0ESf6IHKeb2NbdscWPp3tkJzey-3ObL-pOuH4SoGxI5Ywu6Xgfe_DhMJh3TLL2pArGkR5Zcaleengx6hC7_e9HFpe6R9-NzjbV78rF2jBDenlYVMQWNf5jxYEhXCkI8hUv50Fiuv_f6u5QFvvjWkDd3ah3Bf14PcXE_lGjK38nde8qFy4kR8v5QKl1LzxhMQoN9XWqz5vUGK5ESDGQM-SsfHCnRVYiUzU132Vc6LuSUfuGHLaDzOeLYysQMofncxRM_o41EGhAmkyRnV_1Q9y4Xkyv3CRPhxnMb2PqvXDjmE8sTVnD2pQNpiKE2aGaHyWflMZwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N15dFzw8ZU7vXzXty6bs8YGcBFVBYnMLLj6E-6eulPcTfHT7rXonFwUlnAC1dWP4M-p3T7NAhNzZNDVN6NzuGNPRxoEEvA18AeNE7DFPY2qJLkQoXzm23R9BP3MwBrEp77iIHghcUkfH_OkGoFyOrJfqeiva5c8lSZmMEbFc6d39pE7OynhKvrCpFg4CqizgF8qFscAi68Rh3z8uEnTNL_3vYWJ6ajT5P4PDpE53l7lylPXw8drbIA1EudQnUPgxO9vJEB2lHw52DO19ub-nETqm7S6THUjW2oTdWqRRZM1QWK1Lx96tly_Hz3gLvKSpOsPfErP4l6G4ozq_pqf82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PvIyaUOFoauzZhJs2DZ-W1HgocOa98NpqdbReojvDQ34566T3gmC10prbOvmXMJ49DD-RI1tHY7vBpgN2LtckYjh1QTqwj5JK5b0N3BprsK58RPVAWMBI1N1chkdXbdaDOvEttzK_N3yM92A0Hg8KLxEECYpn79zTImMGEUNZyWIaNQG98YVNdwpYLiMu_w5e-W5lF2kBr_gjAdXjnFQbxlT_e4tkk5k8fpQ-59W4C0Fyygx-OaRY75R2DnA4EmayftiJdY7fr1bCd09uDUgs0wGV1TEK98DOrRCp9lMhzqQbMK1BjxU4_wBa2eEJOOWsBFrX8HNVR4MsAEa6pyrTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=Ye3QWYF_tPpyi-eaTK9YIAS66GmdyAS2ntNirsLnRMfVei8rtkTjkXOcXvdB9xOsVLEPrA0fVfI3smdV3yASReDnnw0K4-cAhJsF8CSOZ3MZu6ju2wiSgXWzAviEqE0eF6B1DWP9_ybumA9rgsl05NMRj_gYnUTv_v4vYm6ha4AOQxvuOOqwWDvuN6ofq6ictMjdxqiuneLVrQFxQFOT2Yc14x0s7tebBsvA-6hIsYL2M_RlMXvVLXwA1w5A0_jrnCiRA5ah5lBi_OUztdLBJfShF6x-Llh3srFHIhiCizWo3l2DyU4vBc7WN60CeTfB4UNwbqnk5t9kbGAdsWQStw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=Ye3QWYF_tPpyi-eaTK9YIAS66GmdyAS2ntNirsLnRMfVei8rtkTjkXOcXvdB9xOsVLEPrA0fVfI3smdV3yASReDnnw0K4-cAhJsF8CSOZ3MZu6ju2wiSgXWzAviEqE0eF6B1DWP9_ybumA9rgsl05NMRj_gYnUTv_v4vYm6ha4AOQxvuOOqwWDvuN6ofq6ictMjdxqiuneLVrQFxQFOT2Yc14x0s7tebBsvA-6hIsYL2M_RlMXvVLXwA1w5A0_jrnCiRA5ah5lBi_OUztdLBJfShF6x-Llh3srFHIhiCizWo3l2DyU4vBc7WN60CeTfB4UNwbqnk5t9kbGAdsWQStw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdO7K5Df-BfTdMkQbPtO-dzNgyRi9tpkhu2BSQ6UPWN1S-TT_AZnZeZG83aB9CLe_LRu3yovgjz8XoZpLd6X9z7XkaNiJvieH-efyqad13URf1Ohr3EjjLqube0BREiplbvfwRWjmlCj93tgBJXEPpmzo1KuD47jrnn2C6mW_DL64fcVRlb44qdTORQEKdBbvsDyxh_3WIUT1d-JXyHspP4BU0H-8fo780fD1RN3JoBhKWW0ceUWaJ3Agk_19nqDhxWP61hCl5RxpNKLrkX8rtbrFoidfmm5vyEcbr3iGKvlofKoQey7xvYZK_FOpBPbSPkv1wLyey697YMXT6DjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IrHYEeFR9VRgPsPF_UxTECWhgM6XDG9ly9illxE689djY9ZNjUuzWpvDjjyOh3DnzXprpP1wLP8QmpeLBXSHpDyhkieX_s8JMWxtlfSee8Max01LlMoZPzMGlvZ94HFpfr1UqG36LdgvfJy21eIR1RMRiju5aEt6u6BhPefcbUTMhnMDhj8rCimR9WtyFCLab1yLjm4VRGstgJozt0RvEI_TdQ-W539b7HlHXHyiVulqJh0ksw-7xd7OIZUi59uauLQ0IIIl2lXZ_FG3ceZNilOhM9owkWbahJvTp6aU_J5UwkcbDjaQxmUPr_mcjXmy_DlEtigLu523oXoyJsa8HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DK3YqP8ROlFkrWct5Exx9NMVuAY4Q27-2WdoTcr_ue34uBodVIbWCA9vCT7E1G82lu1zQrMcxDVVeCiqCpiiMkfWeKF2Eb5eFKFQeo57hZoUf3HhIMAyrIMz8e9w3vAFhgxrj8Kp_xPFFj1EB9mDwgSySdw7tTNB4-bYrWPnG5A3Iw8Dl9CMpyWR1vdzSpi64-TTOnR7TBcsSpQANGvCFXmDdnXI3dfL52EpKTWWDnPBFz2kfhGzrd1QzftlLFLr9TKiL3NbFvAmFWsCNoqjgu2bc3QnDW__bFfaIT-iQRJ29BhIVkF_tgUStKwdyqzj2r0zA3PSb7xw4lsl62d3dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YZB-e5itdl-B2e6F4qM8ZGUgB2xJ3CZNJGmTP2AevWTQyHlGOzccO-VwAfz9CZ6XMO_4imteGBjHldvMn_NWkrEmFvY_mCYc1oL0vjO4hoWdIEUEhgJIF4SHWoMgqaRmqtLVpSed276Dw-7HRdxWaG2cZbe73CEBllkP0YEmQrUSW9AlGkKmu-YqRzh2sZMFQYecJcYd_iZjUH7ebdoz-4R0Z5wYqfoze2xLbA3Pq-OAEE_tUAbW7wOAEv6j3JPCLsusXPoDZismDtftn_ZaJURKGmMEAG2xsyDjnrL4AIlcNVP_P5svZ6FW3ecAM1KPVrdsmPIlCKucD06KUeBP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP7rLoH3M_LiGeiPkFlwB7ClGATREW5r1nQbYYpS6O-yi0JQqlUMqDdTrfpc0rPzcgHjCZ8m-1soEzrkWSl86kjNG9qNxXQDyjFCLiZv7K6At_IAy1QOHTuql5aHgoI4SfVRBe-fJhCIxuZ1d27clehfJcgTA3dU1avWIuxDVNhv6Np2AKtf5VNoOqGccm5v2BcdaAEtIzl3xPrMa6vvXaKB6YZsaobLRJs2-2zmTLznVleKk6Ii11gcsF57Gwl9IvQy9_Jzsd5iwyWAI9ti2Uc70S4MwUREo9ZyvqQNR4vm-31Hj05c7PaGiupZNrbLVQT8HMx53pahUWGL40on0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CHzY1VeuxntTkut7y6wsw6xCfEtU-wZlWbv2dnaTsJWBvL98MiTuS50_dEQIgyFzIkWukrxAWGzQem8ngZXxfZa9CpsROvE2F3QJ1AqIVktYaeTDesD2osjhWPrP7j5QGVXjereYqwmctf8tKaD5yxlLl-gNERIYKBRLiRWewRx_Ytv4CNiK3ICZkifrAfVLK4sjceY9hnUrDQVtooGB-M3kXCa7B7yfFbef0nb1HERTIQ0S7ItuSr349J0clETooyNjDGSLZQp9lIA2zLsXXoi66F2a-skGdW5T9uFqaifXpn3TRLLGWhBWubmtQ8Jh4hMik_XUpgLJ0AzLC-nPNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecK5rl3SNDrR2wDtZdyEVwyukVI6bIP42tI57uSzIGjJIF3mOjkAmbgOl_P46DaC1I2WUcC2a9UwCVv9VfiZ2RBaIG4o8WcP7T-2KYkv-XPLersJi4D-844JRMPy1QQpLiHPVPytYY7l-DNuPnn0FpTfgVIP2CKS8KQXt0qCpAwUG6t9juANziudiWV2HlQ_NFe4aIOR-1X-oyGzA-iv5DFd6-o-15UIuomX_x-0wPLaAEawOLuKcmsDqk6xTzKzYU19d398RuuHe-wHXcJS3VwB3zB0m-Gdl5O16uGTtBcs3T0KF8vq8RhWxDR-I8BmHx-JGkRh2FTpBjzJ9ubUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nI3kdJsPux6Xrulf2FwI8y1j7MyTgSQUIxu2as0BRZkBrhp9NSEGus6_jMwDp_Rem5tJjpxJmOKN30g2DRT-wo6S4ZFxhR_sUVjR1HaIkp3HzrWqqpO_fajgg5cspvuZDFkE_EECH0Rr_bibiRO0qKxzwHZjBj6nt6bJOmij1E1U_9U9fK5zVTQrjBg_9ix9vSmrXOcVQ3WZcIHFX_E_XNajx5Z5YMk9SMd7w6onDs4ha-sXVNjwX_aJwzEHUkRMwqsJ1vm2dOLdBSg_RLpTnhOzeuSqxUI1_Ycq-4GIsjRFqbpAiMJ2FnORmGrNbqT9HoZa8u1_aQ3vZZJXMzFCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=TIMhfL_uBGMLZOmSY91w_Lv_Vkj0eFLXN-DkOkAT0BdEiw3L-vPGjNq5yfhFV27KZKXWgax0EDqVPRTweIWdysv2Gkaq9WO7fA1Im9MroYMFi_E3ON5u8epoDAmuPEnMbLjc6q6KQkAXfRIKj5HujssTLUbW3pbs8T9m39XTL1U-EYGoheDToLhvFj_oldTGnLXECv0-RUV58VvcyaXWh_RU1V1J_yfCdBJizPRbJXlqfexiJcz1G1cc1f1kOrW_Q5hVOQ3L1S67wrV7o1PZRwberUhMemwCkuP6XOtg6YZBGdFt6Ec8b5fMi6iz-LXejfo1UN20qSei3qeVpVzY7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=TIMhfL_uBGMLZOmSY91w_Lv_Vkj0eFLXN-DkOkAT0BdEiw3L-vPGjNq5yfhFV27KZKXWgax0EDqVPRTweIWdysv2Gkaq9WO7fA1Im9MroYMFi_E3ON5u8epoDAmuPEnMbLjc6q6KQkAXfRIKj5HujssTLUbW3pbs8T9m39XTL1U-EYGoheDToLhvFj_oldTGnLXECv0-RUV58VvcyaXWh_RU1V1J_yfCdBJizPRbJXlqfexiJcz1G1cc1f1kOrW_Q5hVOQ3L1S67wrV7o1PZRwberUhMemwCkuP6XOtg6YZBGdFt6Ec8b5fMi6iz-LXejfo1UN20qSei3qeVpVzY7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامران غضنفری، نماینده مجلس شورای اسلامی، در شبکه اجتماعی ایکس از برنامه شماری از نمایندگان برای «تحصن» مقابل ساختمان این نهاد در اعتراض به ادامه تعطیلی آن خبر داد.
او نوشت که «چنان‌چه مجلس بسته باشد، تا باز شدن مجلس، در همان‌جا تحصن خواهیم کرد.»
شماری از نمایندگان مجلس به تعطیلی این نهاد طی ماه‌های بعد از حملات اسرائیل و آمریکا به ایران در نهم اسفند ۱۴۰۴، اعتراض دارند.
حمید رسایی، یکی دیگر از نمایندگان مجلس شورای اسلامی، یکشنبه ۳۱ خرداد با انتقاد از ادامه تعطیلی مجلس گفته بود در صورت ادامه تعطیلی، همراه برخی نمایندگان مقابل ساختمان مجلس جلسه برگزار خواهد کرد.
حسین صمصامی، دیگر نماینده مجلس شورای اسلامی، نیز در پیامی جداگانه در شبکه ایکس، نسبت به ادامه تعطیلی صحن علنی اعتراض کرده و نوشته است: «بیش از ۱۰۰ روز از تعطیلی صحن مجلس می‌گذرد و نکتۀ تاسف‌بار آن است که در سامانه قانونگذاری، امکان ثبت استیضاح وزیر و صدور بیانیه مسدود شده است.»
انتقادها در این زمینه به خصوص از سوی نمایندگان نزدیک به جبهه پایداری با پررنگ‌شدن نقش محمدباقر قالیباف در مذاکرات با آمریکا، افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXsEC9rQUwbEMV3CWoFvDoIJ3eARKVVVvW7ZFecLYB6yxUGc8PiINolT4nCZ4qV2hOuOt8NqOxfEHc02W6z-X6bLTF7pvig0cTBYUSeBPdIweCR3-L7VdtMRq4vEyXext3yA2k-2k3ecaq_dkkfTzGanLzGDAPw1M3uY_ogA5rnFQSbum7DS5wk0hRC7vWAtyAaXmdVhH5tShMggZ_z1P43DJ1JZPZDwERVO0-p7DGNvsuER8sA765r7U800kdhqhRdwYXifiriiLcQOmTmAYlHww4VJ7hhZWudnSWyaCsNvs7F_f6R05oCU_g-tWpG__Pv6CFlqT4oDOM2hXZjjCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUAJC745a21fEbW9oaRECVPMT89-H2wg5xdilFaSx7qBxQx4Um5kM4PkryMyG0awVY5MoU4q6sSbLGd6kj4lW2b-z31Mpc7RHhb8gJopOZRmSyKD9hX0E_1fMRN6-hf7Yd1VCV8iPHt_tBmwG64bQFqh1zLV8d1BoNs-HyluiCcgGt1Eve06IFfNGSwpjOwEdmvbkUgkHYxdR1b6ezSk5_LYuC3ApBktMjk6glBtrrCFccG-gTLWKtTNi_4llLsaRhquyPpMoDjgWvnia9OAgKLqglveXDo6979qgzDYGotGK-D9HHIbtu33nde_geMBQCiw-FrlCvh_gtVs_CRm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=Vli4wiyaWweXZhCDLnB8035wVg-xYc5eu-xbHTFAviwqfN-AZLiW7jcPyMuk9QTXMcaiGqzFhMB5hwaV4y_o5ufj9N3S4c2oi_U4jZ5oAhDlhNmag29P7cuC4Iu8XXdg0rjDc8R0aJjcqk_ju4jeNVmiG-TU_IyDgFIA5G6v6o8wghj6fbxDTGrLipbdkz0tMQ2N8emSG7AUT0LG05_HaYnh5pIGCgDdtNjTj8ZJuiRQ5zq_1f5xzplN2_AhATmdoGqQaq40gf54ijTds84xNKW8G-6JEqb--oveSWCtgEUUwcJiWyY1iMgAm0AJW-dgBaVHwXsMckkPLA_FKXgc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=Vli4wiyaWweXZhCDLnB8035wVg-xYc5eu-xbHTFAviwqfN-AZLiW7jcPyMuk9QTXMcaiGqzFhMB5hwaV4y_o5ufj9N3S4c2oi_U4jZ5oAhDlhNmag29P7cuC4Iu8XXdg0rjDc8R0aJjcqk_ju4jeNVmiG-TU_IyDgFIA5G6v6o8wghj6fbxDTGrLipbdkz0tMQ2N8emSG7AUT0LG05_HaYnh5pIGCgDdtNjTj8ZJuiRQ5zq_1f5xzplN2_AhATmdoGqQaq40gf54ijTds84xNKW8G-6JEqb--oveSWCtgEUUwcJiWyY1iMgAm0AJW-dgBaVHwXsMckkPLA_FKXgc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه دوم تیرماه بار دیگر تکرار کرد که ایران با بالاترین سطح بازرسی‌های هسته‌ای از تأسیسات خود موافقت کرده و این بازرسی‌ها «تا ابد» است.
دونالد ترامپ در پستی در شبکهٔ اجتماعی خود، تروث سوشال، نوشت که با وجود اعتراض‌ها و «ادعاهای نادرست» ایران، و «هم‌زمان با جار و جنجال رسانه‌های جعلی که هر کاری می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند»، ایران «به‌طور کامل و تمام‌عیار با بالاترین سطح بازرسی‌های هسته‌ای برای مدت طولانی در آینده (تا ابد!!!) موافقت کرده است».
به گفتهٔ او، این امر «صداقت هسته‌ای» را تضمین خواهد کرد. «اگر با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد!»
نخستین بار، جی‌دی ونس معاون رئیس‌جمهور آمریکا بود که روز اول تیرماه خبر داد ایران با بازرسی از تأسیسات هسته‌ایش موافقت کرده و این امر ممکن است در هفته جاری رخ دهد.
با این حال، مقام‌های جمهوری اسلامی بویژه سخنگوی وزارت خارجه ایران هرگونه بازرسی آژانس از تأسیسات هسته‌ای را رد کرده‌اند.
@
VahidHeadline
پست‌های ترامپ، ترجمه ماشین:
با وجود اعتراض‌ها و اظهارات دروغین آن‌ها در خلاف این موضوع، همراه با هیاهوی مداوم اخبار جعلی، که هر کاری می‌کند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهد، ایران به‌طور کامل و تمام‌وکمال با بالاترین سطح بازرسی‌های هسته‌ای برای مدت بسیار طولانی در آینده، یعنی تا ابد، موافقت کرده است!!!
این کار «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این موضوع موافقت نکرده بودند، هیچ مذاکره بیشتری در کار نبود!
بر اساس این موضوع و سایر امتیازهای بزرگی که ایران در حال دادن آن‌هاست، من موافقت کرده‌ام اجازه بدهم تنگه هرمز باز بماند، بدون هیچ محاصره دریاییِ دیگری. با این حال، همه کشتی‌ها در جای خود باقی می‌مانند تا اگر لازم شد، محاصره دوباره برقرار شود؛ چیزی که در حال حاضر بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که وزارت خزانه‌داری آمریکا آزاد می‌کند، به حساب امانی منتقل می‌شود که تحت کنترل ایالات متحده آمریکاست و صرفاً برای خرید غذا و تجهیزات پزشکی از ایالات متحده استفاده خواهد شد، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما.
این‌ها چیزهایی هستند که ایران به‌شدت به آن‌ها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است همین حالا، پیش از آنکه خیلی دیر شود، کمک کنیم.
گفت‌وگوها به‌خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد؛ رکوردی بی‌سابقه در تمام دوران. قیمت نفت به‌شدت در حال سقوط است و جهان جای بسیار امن‌تری شده است!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T116A0-XmyGCu-1N5p1y8G-fMJwc_4cjS5G0CJGwn3Qd4Gs70-6ubzQCzjfAlV6JMxYw8PHvKWk4kRZxQSryfBKB2mreuAE7TE32desjBrevBsUB41TjWZE0OsLVZJ0rfhXbLesc5nbQNuXjv5LLYbwGcBGfzw2nIKE9JSO6E53TuiGD01tONPF2QrCl0_boujJKM39i_RZpeH5qXQwcKY8dUFAYXICBjcIDYnxN1ipg4227E3r5ah46vL-0q9hCEWyfZwo-7Vkn0QKLrMgfc6qfOgOaq-5a1TsiGmyZSb_tcRAkNsXh_-4ERrS6PJySPnP9Qmt-_GStPMSgDn6nzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت  [نان یارانه‌ای، نان یارانه‌دار] در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
بر اساس این گزارش، قیمت‌های جدید از سوی استانداری ابلاغ شده و از امروز روی دستگاه‌های نانینو در نانوایی‌ها اعمال شده است.
بر اساس نرخ‌های تازه، قیمت نان لواش به دو هزار و ۷۰۰ تومان، بربری به ۱۰ هزار تومان و سنگک به ۱۵ هزار و ۵۰۰ تومان رسیده است.
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران، نیز افزایش قیمت نان را تایید کرده است.
در ورامین نیز رئیس اتحادیه نانوایان از افزایش ۹۰ تا ۱۰۰ درصدی قیمت نان خبر داد.
بر این اساس، قیمت نان لواش از هزار و ۴۰۰ تومان به دو هزار و ۷۰۰ تومان، تافتون از دو هزار و ۳۰۰ تومان به چهار هزار و ۵۰۰ تومان، بربری از پنج هزار و ۳۰۰ تومان به ۱۰ هزار تومان و سنگک از هفت هزار و ۴۰۰ تومان به ۱۵ هزار و ۵۰۰ تومان افزایش یافته است.
مسئولان صنفی افزایش هزینه‌های تولید، از جمله دستمزد کارگران، خمیرمایه، حمل‌ونقل و اجاره‌بها را دلیل این افزایش قیمت عنوان کرده‌اند.
رئیس اتحادیه نانوایان ورامین نیز گفته است اصلاح قیمت‌ها با هدف ادامه فعالیت نانوایی‌ها و حفظ روند تولید و عرضه نان انجام شده است.
این افزایش قیمت در حالی اعمال شده است که نان از مهم‌ترین کالاهای مصرفی خانوارهای ایرانی محسوب می‌شود و در برخی اقلام، نرخ‌های جدید نسبت به قیمت‌های قبلی نزدیک به دو برابر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zyl15JHh60MEY9RqJLz1d8dQzq-RyRhnqnJ5lr5ftI5G97wbEofsbrEKNfFmyDkI59OhT_Pn0YjO5fAk-wIQq2BqBuX49Ya9AlId83COvPHBefc897qHmRTzoNDNDyf7b8FEd5pS1bGxh3YD713nIogHlKXvB5NIEL-c6RFj8kl3asjoOOfuziaSn8QNCqmZ0KFG6HNe4e1ugCRkCzCLg_3puKXAH-6_kv-ORcuc5Km32TyuX8gK_A3ZR2phLkxNPYp4gSK62otL-EeQdtZPVsZVWAZ66CCsTBQXPmE-LpJns3h7AivBNEnXn6Mr32nCWkQ1y9H4BxoL9XDQ5K1jZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Eozu4pqBrb0q12NHE6HhM2NqcnGM0205TrAYCqE1AzUt15cf0yHsllk7ATh6YChy58zeR79VyCSfJinxA8C59ZfN5Mhw4dneo_VwhjPReO_jXtDaNtbnrcdTsfb2LhWjQgDPG5taU7pQquR3t6YpBoCZlNPsCSfLBWW1u40xcPp6sNDhFxPuIixMEuFFIwPnen0CqeXrJaPPJc84ZExBNh_vkeT5vcHXYsHSf0sz1eY5_O87Hr25sLMk82qt9q9k72uYPxijbBI92bZZ-Sl24tGpy4Qjena3lwvXz8NQTdGcWxN85L6Ry8kFFzgKaTDRVT9SI3Xs_VOlEgTiacbjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W8HQV1T4DBJW4KYMFQN5ZhqAdTR_HZIbFKJ5l4O_C03xe5IKF8X2AE4kskCh7fpDFVV1HIStUR28vhAij5A6ztExNfJKbNNlmOBFcq8Ljgu3EHRAo48PKz8xpriUK9yoC9trwS3ms8yhUkvsvxCRrfkDSH3q_3ufK0tTbtrKLX0XDv8v42RT8dej7Ldk9Ipt-zaedBMJx9NIj0BGLWroPWdJWtH_gTZd1lRvJoUKRytzL6NhNAF5r0yGRjhf4JsVuPxL4mHZXNYzNhdxvHY1sduvOtOpNLViCXm3Gp-M87JYRlD9yMFD-zt0GA_QCaRogsfojDewH3qSjBTDFXIdrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=vvfp8TViqw4KZx_X5C9Ji5rT15qT1NGKS3PSgb6KWQKeXMVuJP4DmbRaNkk-dBKkprYqOvMDQ1z5W3SkX2kN7_o87TnE9sCdkcs9bLR1ndlp4GSAqDVgk1MvXaZKX-Fjas_RtQTE2ls2PeSw_wgikbLexpuYr7lVXMZDfMB_NxAhZoYQL3ScYjxXKYC4GT0Ikq377-V-O0zUH0K06Vh4nO3056h_2_RUwd6yeUcleF1JaY3srJd0mBjesH7L-tracnf-dOF_D_TdNabhxxApuLgz7uxnC5zzuCdX4HaLGnpqLq8yrtTGriBZ4IZwaLFMfPBZNTPH3Jw1AK1GZ3ys9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=vvfp8TViqw4KZx_X5C9Ji5rT15qT1NGKS3PSgb6KWQKeXMVuJP4DmbRaNkk-dBKkprYqOvMDQ1z5W3SkX2kN7_o87TnE9sCdkcs9bLR1ndlp4GSAqDVgk1MvXaZKX-Fjas_RtQTE2ls2PeSw_wgikbLexpuYr7lVXMZDfMB_NxAhZoYQL3ScYjxXKYC4GT0Ikq377-V-O0zUH0K06Vh4nO3056h_2_RUwd6yeUcleF1JaY3srJd0mBjesH7L-tracnf-dOF_D_TdNabhxxApuLgz7uxnC5zzuCdX4HaLGnpqLq8yrtTGriBZ4IZwaLFMfPBZNTPH3Jw1AK1GZ3ys9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hs-FkuVBu53KdfPl-tRDcIKtDlqPm6zxbdOFMR7GZQMqAzrjXpk8ngDwLP3wSShozn2ts0a5rL58nWfRVefMZIzTdO-CB4JqXDLSCZR1U9xHZQfb5Mkz8xoMxhTwlykZRK-erQcZCjim4-GzdZdjNV4WNX-HULKuaHTLDB7H_pjCKXC3T-ugunXZGs4H8rsG0Pqc4u2Y_o-goikPt-VI9J4re7Hgda0RJcXuZVEFjoBMJU8pMcCcbfjOvaZmhsaokrTe9oPzeny5DbpIa1sLnuVAvZGMXw7diyJ4ZhvYxWGGENGA4WPUihMHMhk5mEHm6M1UvV2apMg_gTzdHQ8VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V0sf8n5vOL1D4oG4XZ7JSjeUK3wICqqy4njTF0cLv1A2A0cucHt2sTus9Tid8Nz1JPyEGfLWWCOdLuhMm7CLtyESudvHPGgJTKlVyjRbobaSQUEcC2mZyFIzSmmVSG3VNyynmfd0z5Ujpsf7mbw56-u3zbKn5ObQxeyKRFKkHexe46gNkQD8oKZeKwm-yjDwoxo9uHQOJ-d2HyExjNDD_WNR4cBlh3ZfUihJ0xqCVB8Q_WG6JhBBTUZ9xuu2gDgyBlPozQCmMR2-FMgSCs83YY9E4iLlBRko3gdKJW9acnE3H3DParRPnJVDVGd_fJHyZGopd6wlcbEbwMyKNQoDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X-bdoIxEAoggI-VQU1etfEds2eicfl34yAC29yQaCfrbcgKxlb8UPex5UPi5CHjZ8eZOEy7uoKzFdpzvAvx-tpYgd0JdvCiwCHxGtMbskGXZzApVEAujW3gOw8Sw-QbKpgm0URtDM_vfHZ21zHy1OeOsAjzska4Ankee7rVBYZ8Rxq_63d1ccHJbMXzKdh_DMv9FZOyREDXdxSbo-u3RFKBMcvzuRRxSmYiQEmLGKAA6g1282dsocrS0bcdK5UwPw9LbmzxfaB-QWB8OHbubKBr7eZWmd2jYBIale2ftzetCCjwPuDu0iBiNdaGnt-7AHRItZTrKVLxvqQHgCBPuqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tVHFDLlFwJpMZdbJB8rb_uwAJwr6hbZY8DhlVRNpaCoFGTXCYDj0qrJfF9mY3i9o3q28C7A99h-jgXcskMG4SSBISxOdWtomitrruF7PLXsy_lX7eTVFEiDQbaVw3SooQv8DALXR3XF5197WEaAKY1T5esMW7hhfjKpzXlXqEqpzRnZCyxH0P1ieSQnJXGLnv6LrHPEdwSYKHwJfvqmthoJ_OaEgWdv_QV6u2BmrvR27u76A8O6gEVOIFmoqAvTnQcaQdp_mHsjUKs1lxU-Ek5Zblt56uffmMlkKCYckJ86oDDVsP4uIrVDssPS5iYDJCbhe_iL4JndtekAdiV7AMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vKd-1G6s4UOr8MIxahBoEfNaKMxlXQ7pJucZ5SxsxY8rRCatdmhL_L9XRlBk-Q0so7fe0D7v-a6z_X4o1QyvG_90vGUUtG_4pxtZM5nOBZsEhFUlvBQall_8CcMETq3MODpq6SUgyvmzcs9IXEMm9P4s546qi1t9UHzAV_6-xo1QPFrwF7sMLQKzc2YJ0poyXFZGHzPdI2gIOa58PeGOTyrdysaQVrVry-PmHW84pdIPOULmlOQ19JcF_KN9JJYqru92SL9WZ5a6jZ541SrIi-dyKFLITv0EgOmtr5IWZ14VwZfA4GpAMiLZixosTQybgNh6fkqCLzmvBGhsIOzYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f17OK4BSafM19wiGHgaG_pX8YplNuSULuX21n-Yopm_Zl-0JW06YMPRqStlT_Aqj4_ZjWQ_7-TD-pVStgN0diOxuw4adl-edJluiCXrkCv-iHyyn8_Z79SmzG1IDTEdIsHLbQilzhhtv8WMvJwiHm3al_mhH3kDDoxA2vpIo4-kb-pr0jhupwf8NBfI5APpOz7U7qd7TnC5RN36CdLuhPgGS4UFeuZbzfQHrEzAdOYnDfF64_e0thxPf0O2W0WrrU-w-0rm1frGHSGGwVy-DJ5oKsis8Ym6zcaqkqw0VNVE_fn1WMMaG4YbuzTit6vbgfedZTU62T9hwnwUihK0JTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T_NFewh2kMocl8Oy232KXrxUkofvNMEqdUEUH45COgSwyhHDRFLdNSn9iCYM25LYoAo8W_VnvoN8DdaQjxsMe4UG74tWoq0sVSkWHqY8TNRN-pgSr4pxUEI98qZmalCePDylr04rmmJ2OmzKm4re-7Z0jEZ3rVIPKCumdJmNU1PxB-Ujdss3k8siyuH5QaroQ0mjoiM_FX7k241rcKMfYvcxWJkvHRt0KiKPb9g0gjyDR_E6IxmczgOyAsGWO3GcOGZRpAbxXmSvvhYL14cvF9RvKwL7OaCqFzIWa1i8dD3KxfC-MkQLAFnhAb80kiDei8oxyOdPjd7SOzDr0DiYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D5kqo2gp4gq5I8fuf5iw8EonFaGoicpZBHktA-F9FKIZSoz1wNfxOb2bIrsv1owZ57HpVGp3DpP9kJSlg_t7xxK_VKfHTRoQkpRkBYOso94UkE1nxthjiGUkebp76rAt4nvQAI3LduJ_NjfCWrnA6PfukQrXUmUnaEFR2rO0R0EUy_V7ieZgVRa8U1Bpef998VT7jBe3tsfuIt4tAihq7tm9_gDtvutJtTqMc5e6vmFwvJ4zSf48Xkn8SfKYLFrzawvQIsT2quj6tBwC_cIw89Dg6qBeJOF9r33v8zUapATxxDVA0CeN8wGcz_HpqPAl6IAjghR2Qiky3dHen9Iv-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد + ترجمه ماشینی
دونالد ترامپ، رئیس جمهوری آمریکا، دوشنبه عصر نتایج چندین نظرسنجی مختلف درباره توافق با جمهوری اسلامی را منتشر کرد.
از جمله یک نظرسنجی مشترک «سی‌بی‌اس نیوز» و «شرکت یوگاو» می‌گوید که به عقیده ۸۰درصد جمهوری‌خواهان، این تفاهم‌نامه «بهتر» برای آمریکا، و یا «خوب» برای هر دو کشور، است.
در یک نظرسنجی دیگر، ۶۷ درصد می‌گویند از تفاهم‌نامه اخیر صلح میان دو دولت حمایت می‌کنند.
در نظرسنجی دیگری نیز ۴۷درصد گفته‌اند که این تفاهم‌نامه اثر مثبتی روی نرخ تورم و توانایی مالی خرید مردم آمریکا خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9-KKHCBVMQzDpku899e2gn8CEUdnqBAzO2TKrdQqTLxp-3nti61dmYnq4xyYtFdM1zFWVJ6XugKu-_tm26LbHgVEqRCkI4pPZdZo8GLA1qdpo916xsNMwlBcT7Z8kKLBpfrMCedQNZtZTvUdpBg_YamfIFbWc6zFN0an7G-uM60vWrOTGx57T5URMyvckA9HtZCLEFhjdTd7GaQI4pxnbCZKHARAxe7gyIjbl8C7wIrhQvzCMCYBRV-ttWI7jI_nhU0pi9X8L33P9jdRi6Xaq0eSEqwvr29SscFHVC-fNgtwYwF6aeoF8IV232f1YRMcQ-t3eHTYrcIcCH5sWMg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.  ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ویدیوی بالا:
به تشخیص ماشین، حدود ۱۱ دقیقه از نشست خبری ارتباط مستقیم با ایران داشت.
متن فارسی اون دقایق
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود. 8:15
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
5:00
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=JxqNabbTXlB-MJXH8ywFN2IBzStc8Xxt4wibDwGifcvIlIHmoYIdsf4j7ABnAnBTSZqGFo_kD81QEXYuLwfmFAwGntO3fhVAzqIPboxPsH-76NUwHVQm11R8A2tAh6bKWoALH665Bkt9oTlshdy4S2Mfl-v-Vth7wC-nMeCsWslJKzQiEm_NgbcWun0LVvJlUkdZLOBTl4cMxtgSxJ4l7dORpRgnyw2kp41LGu2ghb7U_LT2TzOvfyma8FDIem17Xs1RNwid-xxBjK6PblDQKJrC_v9G1ysjdTSLaBgmolHW5QMQZk1ZHFkzyIJep0qKJPq7HMVudR93ifEaU-XpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=JxqNabbTXlB-MJXH8ywFN2IBzStc8Xxt4wibDwGifcvIlIHmoYIdsf4j7ABnAnBTSZqGFo_kD81QEXYuLwfmFAwGntO3fhVAzqIPboxPsH-76NUwHVQm11R8A2tAh6bKWoALH665Bkt9oTlshdy4S2Mfl-v-Vth7wC-nMeCsWslJKzQiEm_NgbcWun0LVvJlUkdZLOBTl4cMxtgSxJ4l7dORpRgnyw2kp41LGu2ghb7U_LT2TzOvfyma8FDIem17Xs1RNwid-xxBjK6PblDQKJrC_v9G1ysjdTSLaBgmolHW5QMQZk1ZHFkzyIJep0qKJPq7HMVudR93ifEaU-XpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z-VdM9iNr1UAfkliWVw2zYBiC3iL13wh2gPrNmW3uGJWrqkPfcNLASDRDvYUEI_tDZpLNx3rad_KI2aumXuaFB3UH8UCF0i0TXt5Dmsm7erIPBuSpEBvqwyOTyH0M7BDxIKd_EXX85qkkrJTOsyqfWhqlk_NzzNj1LZENVzFbvbgxox99nGEFvTXIAuQdh8a1OCD7YxkIFW4Uu1u3i3cB2NL6QBT91qNzDgrl17CahS51V-DcykLeYRs7-dh9Nf7Ymq9UozJhzypgh6srQJWrnULFyu-xpcxyr9fX3BoEdRBS9zl1BFIyFvg8qK7TQ2JcwQYGeSoPQzKdPnQuYoxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chsdh69bCGSWamysQV-nkPeu88H0eE63HYwMEHuHGhCGotmmqab818jJqqVGHN16MqA1h86LeoROyYOrvBKsAw6mBJ-s0W0TBaRD4sdqtbj1bGU_yKKteYjxj0-bYIf5A4wdXw4ApJZI2heMTIZ2Xe9P-VDkQ3HRh5ZdeF8ByMaPGPZrXedAmNgIxlHGifNsuk9G2e3uHNlNcdrFycJT8VtYhB3ADv5eEZ5Mu2oKmgX8pYZZYOqRA7OSZnXyzjH2ojGMCeZcmjbWYpELjYVpjCM3jfCIxLA96chwg_e51F4bPeoaarTPUc_bAqIQFFlsRg37RsS8H2vSLicNRspKvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cRB6F_x6kMdYLq5umgglzQa4aB0h_aIBvH81pQpW8bKnYvaIpxst6jKCmTZzfWkw4GYxU_vDLt5HFeZCalFRW5FVjHxz6AaG1qqOT36g4y7EFPy4Ih8iaO-fgWsELG28Q7Gq2NACCzZx2vc4NlRdjI3N_hT8PdMyKLn8zkF1w0oPF_R_z2rILz80x_xzYEyWgVXr3fhJjVHySQWlufJuMI2gPwyG1j_F9F7NN42lRKj1HghE_RPytIYMOnWmZ1pkkrvpnKZisaFYhczandPulHBN8cwGZ_uArCnmA9UNz-iTETSnXa58eNiPXBVOBBmaOHo5vOWnxXSHm4pc5kErAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=lrOE1MVS53Jsw1lzgUSzRA-MHyruoKraoWU5wrzo0MOb_mk4pPionZHH7cXKOLXzFQrNL-V7zvl5L-YT-FY2Xrh2OVwWNqzUVhLjDqoKj1yUXMe0ZYEJnAPyz1faeS4Gu7NkpQE98-brDDGGLVFRmR9T9vlMZJo3NIWtHOlHA62zLvll-2R6v3DflCW9AHbK5qDyYzJ9z35_ndfUaAVQVZK3cnn-_-_fw7_GjqUmbgpgfDNPjSVsDOWRC22UiOwOTLOdyQ0QonJlU_MfaBqAhnuIY1NCaEtyo8q5RXp1zq5mR6UZCqBPoQADxXCsbaPVYiFf8Pi4nqCpBOd5QBuPVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=lrOE1MVS53Jsw1lzgUSzRA-MHyruoKraoWU5wrzo0MOb_mk4pPionZHH7cXKOLXzFQrNL-V7zvl5L-YT-FY2Xrh2OVwWNqzUVhLjDqoKj1yUXMe0ZYEJnAPyz1faeS4Gu7NkpQE98-brDDGGLVFRmR9T9vlMZJo3NIWtHOlHA62zLvll-2R6v3DflCW9AHbK5qDyYzJ9z35_ndfUaAVQVZK3cnn-_-_fw7_GjqUmbgpgfDNPjSVsDOWRC22UiOwOTLOdyQ0QonJlU_MfaBqAhnuIY1NCaEtyo8q5RXp1zq5mR6UZCqBPoQADxXCsbaPVYiFf8Pi4nqCpBOd5QBuPVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تا وقتی که لازم باشد در جنوب لبنان خواهیم ماند
بنیامین نتانیاهو اعلام کرد که موضع و دستورش به وزیر دفاع اسرائیل تغییر نکرده است.
نخست‌وزیر اسرائیل نوشت: «نیروهای ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم علیه خود یا ساکنان شمال را دارند.»
او تاکید کرد که ارتش اسرائیل «هیچ محدودیتی در این زمینه ندارد.»
نتانیاهو بار دیگر تکرار کرد که ارتش اسرائیل «تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهد ماند.»
در مذاکرات ایران و آمریکا در سوئیس، هر دو کشور تاکید کردند که حفظ آتش‌بس در لبنان از موضوعات محوری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YhZ1IKJBfVnnRVfZXxaSTqujNtUreMQMAmI4SCYHLlV0yZpGvZfKmsKeIL0LW2rL97LDFsgnQOk7BJVuOw71HLuAnLV2lA5_rQelutSL68fj6TohryLu2QL4jPnNq_Lr_VfcdOGpYgTiw7Wke3PMpYbaW_xmG4sx0VfC8TKacGf0Q3LRIqU96jmWXGdVK1TmlnxY1nXkLatzSKeoBZ56Ev4XYGnO1xH1UqPipla-ThPV3XpJAiK4L9hptfsNUpBWgLkf3Y3LCzNTMRLRhSrOiCmPhAdiaZSz5X5aC-YkrFcYYm3-c5Lit3EhS3k_jG_jNKZazIxaNz1gVgb_VoVcQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vR_bZaRuDkE8CQBOwKjfqqHfA1hI6HFgbMH0XP0t6ph5fWxVnV86OqZa_2KS32pYKagovpdNCdmHqLkIxMBpf9i6WDYV1GfN109bVR9nIBw0BynuDfKH03xfd_itTFJXa5VMtIuYOkCHYNt6KSsPS2YEcjyL8jVJpQiYAqCDvlRpRG7wxeDl_ZHNGfLDGch5E39pBYWbAfd11iwzAXz6sTlIKNzeDNAqR4_0qBEAFkzxs9PaArtERm5g9UHNkiapFdgBtyfZ5mBMI4bVLqQZ9vsVRt9i0mtsWD-Tk_t1mU5xQZQrwliCVHBwKG71E9BP0NKxGmdLgx4bjrKEyTMCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dYHFeE3l8AJAzQz7k-RKm1XSC5RmDufxLTnfP_llXJQtJ6J59rRjMJsymaSO9jx6QqraB95VIMGPEWScGBA_aGJ_2ngrxsGqzlHYG4tLy-uQBih2wEi7k6ApmTm6IsAUaUDWxOzRH5DJkIl3uCkzxM43GAFwwa7X21qtJyPVp7L3KTCKAZpiM9B9oKotb5l0pQTrwn8-VPTH-ClEtc2UJwIhNolmIILO03aFLi2_wjuLBTr-CI4n3KA0sliuh5oiUNaJ_EXzwLrrunazQ0HYS_WGwcvIiLqcpgOK9W7VpQtNiAQCafoIZ7uQTLfd28av24twJ-MpDtyUlrsS2daOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k2ftr5rrup0ZDfOL08_CGyKEltY7GG5X9T3OO6y0kfFbG4LWYPWHPdtw93FbnKapKiItRLm_d14aYx9koJXbi9H27Di9bGmj-wWoDzGnW7TIRcvbySdsl_Qp0BAlKndYSZbvPVP3ee-_fhKxwjUBjKynK2JdaI4Nt9cafb43fo24GFXdQidSXiitcQ-jikkph7hfKpBefFg9U50F2uLWNcxYQa--8uJasQPL8n_KyuQUR8rOKg9Pzbq2GaO1CiU4jZyrthSccGWs849va0XhHMEAf7mHa7xYxlyosvr0JFQW0Y9xDzHBUGcMxhSFnkCvw2GbsxAYMUiyVjDBn6_KDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VK_u_AFqPRxq3Rs3O1-H7iUc7Ee-79x4aWd-uioSehl7AQl6pP_IxAFC3pn6vVoKw1e9NGjtj9gv8y-os5c62nBydRapz6AwPppBNRg5oz3Ab50fGCyfpLwhEEwRD9_p8CPkzJ76VbyZ6PS5oMiZVPT1ko9AZn9iqXLOFoIOfr61Oc8YYeY4mZK22u-mJE6lglzIpPGzDuhLgU8qwVzccohp3cmJkLTGjgMJe_7vOhqa-s7GQxBCQOitN3wwh_6poxeolKAfGHkkdJWep7YMXtKK7jT80l6_sc0AfiB2GMfi0fhWr5z38T2kZhF829g0-ZK--Wglo-8QZKpAnh-wMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h6a5hFlTgAeIR6HiAxtfVJ9FRdMDpflTIduzniGY89yc-_FlkutREWejBPQ7Ry60cTIrDJOW-Q7mQ0PGXFotDy0sNwendoSr6-OKDGrz0wOjFOQZUv6oNYuT0bL9liHIqS2qeZP22Nvo-rMpvDw1eXCF8ktf-hSmzzFThsd2LldDRZj_QDaxNREm0VADbOXbzlXDcTrojQbkPFAfV_SO1DgOvzk5cNmHvjceD-TgHnjeEtIFVsm3NUZWq4BfuOAV4uIXiJqJvRDXezCh_sEg9RD6rUqZT0NmWK2dT0qTSvputYS9FAZIe7MpL4VMGD9jYSgCwZFvrp5TmX0S807bdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k_bApK4UcLFhgzfM-rKD45EWmUMLKIikTheRhK15i8JXQ1SHT9xnMDwgM7pRh340JwIDdhn0S67Kr4QpwBCl4Vu8suZIBS6cRF5gT1AO4Ge-N15pWN66eox84GTcdtfG9gnKrNrq8_UO_7W2Attv7dmECk5-_axjXyzU2bmXnWTPdkSxh9NbX6ccURdVQcFDsOAn4N_0yKxVCbaTGGLcmPf8GcM7KH-EfCpggTSuJJO5pBG8A0sTsPrZjFusuhY-6H67Fb4n1KdpsiuBjZLxr5PniRpg4Z0Pet8t9u78xmP7ogBJC0UDQ6076-ylYBvkTNkvAi3J71a0Mk4WANaPkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=ooNDiVOfbZkkxZJ0lro4WWfMFook2seTbjNGuIAhuPoZKSvMiYaBgex0DeztTTS6TUWK7UGhENC9rZclfFjtXCjrYc_VkfL-YVdN99cWsLIqGuXBZ0yynYkizGAXrzWjkiHq-a03U5a304NxVMVckJqvItb0pTQrAk7v9giEYzw0ZJySPQYExPfIn_LC61mDgpvNe8eXT9CJVZcEZCVlpefUJH3uqjTOq0_Itf64A3mK2NiA39PvEfn3bGlXW5mdOwqxvt5FFqCa6RpqZUEvPMqUmV8w4_uM6NpwdMhYM3BqAvUdPOfu5L6OcjfVUcmQHRp5OJ2jv9FHsHJGfVsAng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=ooNDiVOfbZkkxZJ0lro4WWfMFook2seTbjNGuIAhuPoZKSvMiYaBgex0DeztTTS6TUWK7UGhENC9rZclfFjtXCjrYc_VkfL-YVdN99cWsLIqGuXBZ0yynYkizGAXrzWjkiHq-a03U5a304NxVMVckJqvItb0pTQrAk7v9giEYzw0ZJySPQYExPfIn_LC61mDgpvNe8eXT9CJVZcEZCVlpefUJH3uqjTOq0_Itf64A3mK2NiA39PvEfn3bGlXW5mdOwqxvt5FFqCa6RpqZUEvPMqUmV8w4_uM6NpwdMhYM3BqAvUdPOfu5L6OcjfVUcmQHRp5OJ2jv9FHsHJGfVsAng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی گزارش داد «تحریم صادرات نفت و پتروشیمی تعلیق و محاصره دریایی برداشته شد.»
علاوه بر این، عباس عراقچی اعلام کرد برخی از دارایی‌های مسدود شده آزاد و طرح بزرگ بازسازی و پیشرفت اقتصادی ایران اجرایی شد.»
آقای عراقچی این موارد را در پستی در حساب کاربری خود در شبکه اجتماعی ایکس اعلام کرده است.
@
VahidHeadline
معاون رئیس‌جمهوری آمریکا اعلام کرد که در گفت‌وگوها با حکومت ایران پیشرفت حاصل شده و جمهوری اسلامی با ورود بازرسان هسته‌ای به این کشور موافقت کرده است.
جِی‌دی ونس، روز دوشنبه در سوئیس گفت که گفت‌وگوها درباره بازرسی‌ها ممکن است از همین هفته آغاز شود. ونس درباره زمان آغاز کار بازرسان هسته‌ای در ایران تأکید کرد: «احتمالاً همین هفته، شاید از امروز.»
معاون رئیس‌جمهوری آمریکا افزود: «ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم. گفت‌وگوهای فنی در هفته‌ها و روزهای آینده ادامه خواهد یافت».
@
VahidHeadline
معاون رییس‌جمهوری آمریکا، گفت یکی از اهداف واشینگتن در مذاکرات، ایجاد سازوکاری برای نحوه استفاده از دارایی‌های مسدودشده ایران در صورت آزادسازی آنها بوده است.
او گفت هدف این سازوکار آن است که اطمینان حاصل شود منابع مالی آزادشده به مردم ایران کمک می‌کند و صرف حمایت از فعالیت‌های «تروریستی» نمی‌شود.
ونس افزود جرد کوشنر با همکاری مقام‌های قطری طرحی را ارائه کرده است که بر اساس آن، در صورت آزادسازی دارایی‌های مسدودشده ایران، ایالات متحده و قطر بر نحوه مصرف این منابع نظارت خواهند داشت و باید آن را تایید کنند.
به گفته معاون رییس‌جمهوری آمریکا، این منابع مالی برای خرید محصولات کشاورزی آمریکایی از جمله سویا، ذرت و گندم اختصاص خواهد یافت تا در اختیار مردم ایران قرار گیرد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در پاسخ به سوالی درباره تهدید تیم مذاکره‌کننده جمهوری اسلامی به ترک میز مذاکره، گفت: «آن‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم در شبکه‌های اجتماعی چنین تهدیدهایی مطرح شد. اما ما دیروز تا مدت‌ها بعد از ساعت یک بامداد در حال مذاکره بودیم، بنابراین آن‌ها جلسه را ترک نکردند.»
@
VahidOOnLine
گزارش‌ها از سوئیس حاکی از ادامۀ مذاکرات فنی ایران و ایالات متحده، به ریاست کاظم غریب آبادی، معاون وزیر خارجه ایران، است.
رسانه‌های جمهوری اسلامی نوشته‌اند که قرار است دوطرف روز دوشنبه اول تیرماه در مورد سازوکارهای اجرای یادداشت تفاهم اسلام‌آباد و تشکیل گروه‌های فنی مربوطه با یکدیگر گفت‌و‌گو کنند.
با این حال تیم اصلی مذاکره‌کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سوئیس را به مقصد تهران ترک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZnbEXqAswzaaYwfKwHBMDvjkXNv98ZtaRkMDbn_jpaPQyqBkvWATeaAmynKq_sqq5Y_Q_41tXmdNDAukDDFzJaTSoMxtL6hKr76iQoo2HWsU03-UvUzBfT1zMDfqrV5U24n6NOWSUaEl_LZKH2Y84tWxwGCw1cQpxiSKxZM-qV4PZF0LXvIBjIIQFxvkxCiwKSKHsX3G0jKVaXnGDDvqU8swS58xSKYD6vloLKLMeUL7jUU3zWNAojQR34EMOliO_op1THT3SSNWUGUGCtRZ5W1NK9tVSOR0OvoJl-EL-OEdWvU5lwptUF9HTChDcizohgnTiCZvWpuHFM2N_-Y4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sR5oz9JUpIzK8ibL7fbLlXrVG355VxYRkQ8DEW9_Jn3e7OgZ2Hg4KJAVvAwPoWMGOHS6n3Zppfa1nU2S5nZEXKeViH8Qu8iR7aBdD54IY--yFAKbpQSjjdVDzOXYGdXCGfAzf7VbCdPikCeSwlsgBpKTswor3bnjY-SZc_kKh-Ihp9GHr4UidBv3bARQZZ35ra9B7Y3eVTH5Bo6Tbzb5z6JeNdvCeKDh0mYzWEvSzE79N--B1edrgA00oW0cX-ga22HQK9UaEB8Y5eAkAgir7Dm1s3iks-xWkSli1Q2WTcj_zm8VoXayGZ3cb02wY_Aywea2G0El8h7wMd5Hkd-6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین: ما این‌طور از سرزمین‌مان محافظت می‌کنیم. mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76586" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GaFSkfGvW4OkpXwEb7Nu_9CPWpAnfQTs74SwwGFehzN6R_eAc7l8nBJ8HlUE46KyH4_RqaOPT390uLC6UjFBMzNEYhEzAcXA6MZzu_bUXZN9_HFAM66_nmrZhYt3jfFMyQ85PGY-IsmFADwYGD2HO_DVEqwMpjKsB7SKWKyj89LBLwBOS516qoFf2E80rT0ZHgGY0BjynMcEwZqg8GvL0fKrZchLNY_oV5wjUt6zB7fk256CS3C9OqDMvv3b7DNQCw5uMeHSJxJUdcmDPrLj_b3ZRczjD5snExwPUAl22JK2JJe45oHtN4eQiiBNN_icmoyyWv67kiPgNdprWUlw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BfQvca5QbzClC99-dtrd4GSQdhJ9hWOD6IMq4DZqGFPOGRaUmtEPorjDkVZXcXvkzh6PMdR6wfDezlu5R3drPxg4Rt55Gu7zpWAHPUg0Vy3CVkBkDYNiOqM6HkE-6vH-dkJ6LKmgUiHkINXaBus-MuYDtpy0XYaFrLhM6K-i2JtcrGW3wKPxo8FToN1y7-W6zVqJSbIjkp5wrbSSkziToUrBgveDxnNr6FCjhs66Fxu-X-cD9zdRKhPE6q-WxtZNceK20c7nsaSLph0cSDKAoKtkptioWtJPqLk5hMxVSHHMcANoOUfX1nzMPYPolO-mW-cwIu5RQr_HB_kracnLBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، اعلام کرد مذاکرات سوئیس با «پیشرفت‌های خوبی» همراه بوده و گفت‌وگوهایی درباره پایان جنگ در همه جبهه‌ها از جمله لبنان، فروش نفت ایران، آزادسازی دارایی‌های مسدودشده و سازوکار عبور کشتی‌ها از تنگه هرمز انجام شده است.
او گفت درباره صدور مجوزهای لازم برای فروش نفت و آزادسازی دارایی‌ها پیشرفت حاصل شده و قرار است سازوکاری برای موضوع تنگه هرمز نیز تدوین شود.
بقایی همچنین تایید کرد هیات جمهوری اسلامی پس از انتشار آنچه «اظهارنظر تهدیدآمیز آمریکا» خواند، از ادامه نشست چهارجانبه خودداری کرد و مذاکرات از طریق میانجی‌های قطری و پاکستانی ادامه یافت.
به گفته او، تهران بر اجرای تعهدات طرف مقابل، به‌ویژه در زمینه آتش‌بس و تعهدات اقتصادی، تاکید کرده است.
بقایی افزود گروه‌های فنی دوشنبه مذاکرات خود را برای بررسی جزییات اجرای تفاهم‌نامه ادامه می‌دهند و قطر و پاکستان نیز متنی را به‌عنوان جمع‌بندی توافقات حاصل‌شده در جریان ۱۸ ساعت مذاکره منتشر خواهند کرد.
@
VahidOOnLine
تسنیم به نقل از بیانیه مشترک قطر و پاکستان گزارش داد که نخستین جلسه مذاکرات نمایندگان جمهوری اسلامی و آمریکا در بورگن اشتوک سوئیس و با میانجی‌گری پاکستان و قطر به پایان رسیده است.
در این بیانیه فضای مذاکرات «سازنده» و روند پیشرفت «دلگرم‌کننده» عنوان شده است.
به گزارش تسنیم، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
براساس این گزارش، «مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.»
تسنیم می‌افزاید: علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@
VahidOOnLine
عباس عراقچی بامداد دوشنبه، با انتشار پیامی در اکس از پیشرفت‌های حاصل‌شده برای پایان دادن به جنگ لبنان در پی میانجی‌گری خستگی‌ناپذیر پاکستان و قطر خبر داد. وزیر خارجه جمهوری اسلامی نوشت: «صادرات نفت و پتروشیمی معاف شده، محاصره برداشته شده، برخی از دارایی‌های مسدود شده آزاد شده و طرح بزرگ بازسازی و توسعه برای ایران آغاز شده است». عراقچی با این حال تاکید کرد که اولین آزمون واقعی و جدی این دستاوردها، عملکرد «سلول مدیریت منازعه لبنان» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76584" target="_blank">📅 05:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN4TN841ye99dlgz5U7Um8haYZkOXVwTTmRMLab1FCp5pXhM6FMUGZ1xO7MVkKkcL4zmLOwqlV33XWVibnJsQcLocHGjLGG6eBXjcR4ryIR6DiDTCG2OattIi8j-OP7AYuy44z_mLcEoCXKVRMAv4ceV11xIjjPcpEwukj1JNaMjvCoA_IISsQc91-GVFal8Xk7Etm0KJbfWQ-dKtS3sba_ZK8FUOErAxKba8QQBYmMe2GIRqAUYkIOrJjg6JWrATZ7Ub1uoOKPA2XQ7RRGiPf_7UhM5sqMlHj2aj0SeQeHvhRCdYGLR8STKLW6qviyQ9SUIJoWhYgAT2lBiBQyacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، از دو روز دیگر، یعنی ۲۳ ژوئن (دوم تیر) در سفری دو روزه به خاورمیانه به امارات متحده عربی، کویت و بحرین سفر خواهد کرد.
در این سفر، آقای روبیو درباره مجموعه‌ای از اولویت‌های منطقه‌ای گفت‌وگو خواهد کرد؛ از جمله:
تفاهم‌نامه میان آمریکا و ایران
تلاش‌ها برای تضمین عبور کامل، آزاد و ایمن کشتی‌ها از تنگه هرمز
اهمیت حفظ صلح و ثبات در منطقه
وزیر خارجه آمریکا همچنین در بحرین با اعضای شورای همکاری خلیج فارس دیدار خواهد کرد تا درباره اولویت‌های مشترک کشورهای منطقه گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F0D1Mf2wbndxUMIAKQjyNfL6sG70CN41HW5D-h49KIDfwIyxA-sVUvc4fIeJeG7zHg5NQcJKs48VpInjy0pEimzMo6fWAL42SLGr4FPtqxczxOx6T2cL_tGb3Bu0qvDESUne5rFne35_ScBsV44MfNypSJBq0ol1UO-JNvqoW95lQRu8FGPPSgqKY8HpYpBpRCwXerS59BGUNhLIb6l_g35FJ2AKy5mv1FtkgGrjzWiBM32QLIYvgztYvOUDJ3jIMXyx_wAvIO_VuUm_4MjBZbH5Ld4GW6mc_ZTzB26Fe1Ukxx379pttarFLrgeXO8xKsBMxQSnjYmL_qpWEV4yTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/etjIr4m9pSkozZxDkebhS5gQAhUjBF8bHKcvMCwMWxKnPm0pzdAquUOu2RC2AvS-LvWymXR7NrHPbuu2MQZxZHCOce1RbQ2fcRg9F5FDr26O0oisAouimhq0Xt7xEuO5Hx-HxGMRn39iaNFdpgEej6q-eZangTMqYQF6x_mYHoc8jptXeJLJQp8wPtgJk3s6cLcUdHmSVD4KwxGxlrz5j0CrMywphpLEu91nP4PNR5keVN2g81ullKPx8V0N39dhvQoHomvyo_TFMkOqpaXKZzsYe6DMqYZBBnTHyPqA3g4o12m2bDL2RjqmhunVSUexIu7EeCIY5KbqKR4THyFVyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست ترامپ علیه نیویورک‌تایمز درباره اخبار جنگ:
تیتر نیویورک‌تایمزِ فاسد و رو به سقوط این است: «بعد از تقریباً چهار ماه جنگ چه چیزی تغییر کرده؟ تحلیلگران می‌گویند نه چندان زیاد.»
واقعاً؟ ارتش آن‌ها از کار افتاده، نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آن‌ها تقریباً نابود شده، دو رده بالای رهبرانشان از میان رفته‌اند، تورمشان به ۲۵۰ درصد رسیده، اقتصادشان درهم شکسته، به سربازانشان حقوق پرداخت نمی‌شود، تنگه هرمز باز است، نفت با شدت در جریان است، و بازار سهام و اشتغال در آمریکا به بالاترین رکوردهای خود رسیده‌اند. این‌هاست آنچه تغییر کرده، ای ترسوهای فاسد و بی‌اخلاق، و حتی بیشتر از این‌ها!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
نحوه پوشش خبرها درباره ایرانِ بسیار ضربه‌خورده و آسیب‌دیده از سوی نیویورک‌تایمزِ فاسد و رو به افول، از طریق «واقعیت‌های» جعلی و ساختگی، به نظر من «خیانت‌آمیز» است. من همه گزارش‌های دروغین و مضحک آن‌ها را به شکایت چندمیلیارددلاری‌ام علیهشان اضافه خواهم کرد. آن‌ها مجرم‌اند!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/etC4R-GmTZls_gpVfW1n2fb6Al1Bmo40WhfIg9qMPTAud3ajMplGKV6_0HcPt8_nv3O0JLM3gz5ImYeqHawBRZfHAx1NrPTvtrspDFFODATAcy6Y1ZqeuajBskYZAxt2tOO4IzxEqwG3qFFT5DTk4qnF2wq4ulzlSnYnqQB59Qq6QOvYnvrgkILsqAXRSBYmwV8dNxCZFkBaBkkrCc167LBKE2Wl0o_Tncs1PT6_gzStV9qB2ye5XC-KEUVRfXYUYJQzLmI29nAJ1eUJEvVrllTABdE7SqCZjJSrQUXuqwY8ODnJZ2ejwbwNFpAnHnEBMnic-lEKVYntYFdUGo5u8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tPDV5QJ_Gx6VTdFc1xsy9hk_tr6gz_hbYIBOfG6hcJny9e19icVo_liLa3WwGUlrm67a0kQiwFnes4WCwDEioCnZ7Jv3ZiXEHSIn9ic5RTWLqill_DcKvheGflQaeptl4sAsHO4Co-4prsKYG_gLej7lvGxWgl-DtFTzqOVhCWqWvOiT-X__IJDhfNEAiMAiFJm2QxNFvj-LTRriAuSGBzwi5BYK1wueGBioE8cJRibxlOqqFD2M7wW8UH9uJTAx4DuxIXbnpgKI4CKJx1R26GnWLmAB7YP6fZ792Afg6yxY0XGpPbGXKKiyCbhFdI7oc-r4sptYdnxnLo_PA9Jeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UVJRfFMIgMbM-SmDknZBfVofDGuXhBJV22IU_HWFBPI-6cjBpKMl1xu64IMSknz45_SaCxawuN9JiUF4ielpRZ_buSQM4_nVh8P3dCxioIVedydpDfv4OxaJJcjXjrWCyKEXY_rt1uwEmeXKe7Zeuaaff7f3QrHEydj_m1_Q-Y2ET38InLWP1fosx3HSDvGRlkx3pOFmYuU-VoiDJcgobr_owGaBmDqaejpYGNNxH8WMd3UV9A02GzXxa9LWk8hs9hYtAu6W9yc7fWzGMFOwP8RH7zanTSmswdsHASYWXf8dcG6c7rGMgnobf6zKFag6iOphw5mj2BIPeW4eUU70uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VTPqbYEz17yanO2N2wCIXxyX7wD3euHEevd6YK4dR1g_CGpo6ZeaLxg82mz2NNow6OcOLH18OB9Tbi68lwWCOPkoLBEJ7rB2tmO97Hts6amHVeWGeGeL6rDOt6iKjduU8c7Mfw_7VHPHV24AelhYS1V46Z5fZMVDQKjf8MtsQeQ03X-RnLjDQQbgXbTaDb3eNvamS5sF-wXwZacYXgeQnKsXZWcQm1z8qz6tSS61oduCURf2pjrJrABFZfrSh5L0h7mPpvozBhggp-eWLNVARuMt77G3H3-iCkfgb7V1C1TUSljrxOoIWF8Ah1Ct0983XHzzmge-MPWOlrcqiXCZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PaHf3F1wnDddD_zv5VrwcxhWiYPcptOiGiqm04tix000kK12R-n4Ntie6b7qJtbGORJ4N3vfk3go72Lml0JoRC1HRGbxqdJj_uNwvjzhzCeNe0Ke_LlxqbCIwkLeeSCpLMhpmm6iVHFC0HMytGTnAa51JN3pjcg-wrUZR6rJ39V7qQzXxiuOv5eJnMWbK8HJFhKZVPgH0HhAQBLPYQT4K4kTBI18gJ2BW81KX-uMaN5j3Q2VFrIV_slnKLh-4mSe3-2preeNST13Ak2abDRWgksw7JdNlL1b-wOArJUcooy8Rd3QVF4cGTxcJb6F_rk3rVSFeKVsod7jp6QFlv4fXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lu_uH4TpnI8pNwJnXqkVyeGj5TQGbqZgO3H8TKNo8rjl3HvwgK7ALKYJttAYVDlj4ilMBZoSzI05jl_lOyWc9RNojSv5q_iszhCtcx3CV_3SEDNHSu3L3Bet1a9AJ91LwInd-9E6i_-_z3zqzMWVwUZNF6Pg5TQExfDj4OvXQy3wp9E3VULyq2gQbAkd_qGwdloQfQc5JuAwPmEGweAPfiaZPMTtTQXjeIqzdVVCouzDOeN7h786BvTofzm6avy4P7yYggsNEuVu0L1bSBUw2oh4gW55PZ24RMtfTIX8ZudG-xlr_cPxG4K_-wCLDzbdKXmcUVHq-qMZDkkGjtWkZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lqphS0FTBYzFHPRR2r2zVSWzY5p1kIHlpV8zPjasclXTx0gvG88ews48k43CLwvppUVL1Fw4C0cMh3yaX8u0FkJ-knYNXJVOtMbg2mz_7hWEvhmQ5eH4Ohlcur7n4vAs-JQuYrph0YGcFlAgUxc3RaDUsBMctjBgREr8_Mmu97XufQV3_B3-JcjOYc-Ys_voIHuH4vcNhazSiI_KUgynX_39-Vpmlz332KFNTY_vAr3E8QozvKOZ43J7-2zUWlycpzVmNj3nNHWgku-g575P1KkRsXd0LCullU4OSZbdB24HUusz9kIxvJQTjstXTTOdRpITV_DKVwAoe1-WLyRUsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=g9-2_vKkzUs85rU1Z-wgU55KcSmpIq3nojKMjavUFTvSGuSVN2UqE6zgjgio_JNUEVkPMZIUlXa4HAIBn6Bjpz4vcXjV5gTu6rAaNghGwesiHyGLwWGC28_5DC6ITudSPqJzCLX_wyMIUHMOGw9DgHGHBUArxULZXzKSj2veXYce9ZiLfvQbXoatC4Y8lClYhhtueDE1I8UDFPZ29Tvj_oe-9gKkTKVxJcfsbkJXsPvcr2yfQaW1ZHn2DHtx3F8yQsaIw7QzakVfSeUdlbNaaniv8v94bQMe7DZ3CVVR9OCt2tSBnZNNKmj5YUYgF04tou5w9WNGkt_vT15kJUChew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=g9-2_vKkzUs85rU1Z-wgU55KcSmpIq3nojKMjavUFTvSGuSVN2UqE6zgjgio_JNUEVkPMZIUlXa4HAIBn6Bjpz4vcXjV5gTu6rAaNghGwesiHyGLwWGC28_5DC6ITudSPqJzCLX_wyMIUHMOGw9DgHGHBUArxULZXzKSj2veXYce9ZiLfvQbXoatC4Y8lClYhhtueDE1I8UDFPZ29Tvj_oe-9gKkTKVxJcfsbkJXsPvcr2yfQaW1ZHn2DHtx3F8yQsaIw7QzakVfSeUdlbNaaniv8v94bQMe7DZ3CVVR9OCt2tSBnZNNKmj5YUYgF04tou5w9WNGkt_vT15kJUChew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KMBSggCreyx5dsjxE0syYWoxm-6I8l13OTk0QWIjc7lD06dnEg_ejb-PqkwHZjRj3CmSiUxigggjUY8wMLex1lTse1zmnJ-32zZPuOsgWEw8zaF13VeYNwavpS6ZMgj8x2FPvgOyavrWPnrwYrhUK_wKrSTlj09vcr-TBFq7bkEHUWjrctCiKdMrijAwZ-_9o3Z8kr3cs4GZokjCw70LLKqGbd4vmph4jsC4e1Ldxncr3SzBjXtVJg85EWTVYXSScAkKPK_k_q1bSCgL1SyJ4JBydEZihDsoSi2Fup0JbC2EViE-7U5miUukspHRXsrGfOcUp64YyXF0e43CD8GdEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMVYYrA3Efaildne22u_Bl0yOJBUd7SxwDnJGsugYUZt5dK5uJ0VbO-drf2n4K-cbqbQGcOA2Ls5gXmlRbAHhZbcKjG0yX4Pd1kpH_EEie5s-eiGUHWAIbRwZOSsl6j_c3hkf33TwLWlbYG8uLUXSo6jk7GyhG744-pjV_LUKk5kxy4aVVQoX_T_zvC11VhE22Iair2BWIsralNABLdzvwMgFo86iUoxbeXF1e1jGDgItoPsAh7lfWHoiid8pPL8CNxFyHbNbcpdSQMROkhQ-2jhgAVZy-rCwtKWB9aAsQdVrkytQOplrwwq95Dte6hZ_ZA5KhzH8RKWDYAHhF0oqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ک مقام ایرانی یکشنبه شب ۳۱ خردادماه به خبرگزاری رویترز گفت مذاکرات میان ایران و آمریکا در بورگن‌اشتوک سوئیس متوقف شده، اما پایان نیافته است. این مقام جزئیات بیشتری درباره علت توقف گفت‌وگوها یا زمان از سرگیری آن ارائه نکرد.
این اظهارات در حالی مطرح می‌شود که گزارش‌های متناقضی درباره وضعیت مذاکرات منتشر شده است. پیش‌تر باراک داوید، خبرنگار آکسیوس و کانال ۱۲ اسرائیل، در شبکه اجتماعی اکس به نقل از یک دیپلمات حاضر در مذاکرات نوشت که هیئت ایرانی محل مذاکرات را ترک نکرده و گفت‌وگوها همچنان ادامه دارد. با این حال، خبرگزاری ایرنا دقایقی بعد به نقل از یک مقام هیئت مذاکره‌کننده جمهوری اسلامی گزارش داد که مقام‌های ایرانی پس از دومین دیدار با هیئت قطری، محل مذاکرات را ترک کرده‌اند.
@
VahidOOnLine
خبرگزاری ایرنا، رسانه دولت جمهوری اسلامی، گزارش داد هیات جمهوری اسلامی پس از دیدار با هیات قطری، ساختمان محل مذاکرات در سوئیس را ترک کرده است.
هم‌زمان، یک منبع نزدیک به هیات مذاکره‌کننده جمهوری اسلامی به شبکه سی‌ان‌ان گفت گفت‌وگوهای میان جمهوری اسلامی و آمریکا در سوئیس متوقف شده است، اما پایان نیافته است.
به گفته این منبع، گفت‌وگوهای غیرعلنی همچنان ادامه دارد تا طرف‌ها به میز گفت‌وگو بازگردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dflDetxyjZoRidQZUq_6YrxJ7f1G6azJWxJ0l2UwIlrZYDEi5dfU4cowRch1EldyGi8E8_lmMa2EtRhbZxzs-lIdm6p7g6T3YezZ_sZ38FKRp4o2Wvfce4K5huazP3ZL6seTBR_kJlmHjXmekc15T_8mir2n-ycjQWEYDCjPo4_Kj0wMI3XNybJzts5Sl0J6iCn7daKiCb-JicLeLVXu2zviiyJbaSLvOZTXwt3IIec1ZDYHUQYtl14UiGAVKfj07ioAoy_uLwelZRp1XbDKRMijWoP3aYm5Jk5rxPo7-iQ_GZwRtmEN81ntV11AXd3g93wnw3QxTFfFoaI-O4zNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
"
ادعای فارس و تسنیم به نقل از "یک منبع نزدیک به تیم مذاکره‌کننده"
پیش‌تر در
اکانت قالیباف
همچین توییتی منتشر شده بود:
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76568" target="_blank">📅 20:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UOsYOWKIw4hTIzl8xcVs9NvZfP4GXwjU43iZvBl9jaQOXtbobM-wTbeGttAX8MDty3UbPPByvNXIH59v3EQ02Ngi_9Ld6bUErt8xh_l-zJUEmJ414qi8XqNnrwFIEQ8Zr-BmM4y4Z8WjHrWFxbofWMOW5A6f5EfhjnLj2TGwnd-HjH0r_b8XHCBJiWbGGmu3FtDlMejd19xyWGom_ybi1Lnhxfwd4msZ8tH-K3GweBlgYdvaxMrEfxYjVTVfAXoBTLQOU9nc3xfv4AZXZ2RBoHN3sIqFvVn31EUA7eh_GejAZfQYlBgioBVTgtv8I_VmWhhwxNo_omii-R39UqA26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در واکنش به اظهارات مسعود پزشکیان، رییس دولت جمهوری اسلامی، درباره ناچار شدن آمریکا به پذیرش تفاهم‌نامه میان دو کشور، هشدار داد که تهران باید در مواضع و رفتار خود تجدیدنظر کند.
ترامپ در گفت‌وگو با فاکس‌نیوز گفت: بهتر است مراقب حرف زدنش باشد. بهتر است رفتارش را اصلاح کند، وگرنه ما کنترل بقیه کشور را هم به دست خواهیم گرفت.
این اظهارات پس از آن مطرح شد که مسعود پزشکیان روز یکشنبه ۳۱ خرداد گفت: آنچه مسلم است از حق غنی‌سازی اورانیوم هرگز کوتاه نخواهیم آمد و طرف مقابل نیز ناچار است آن را بپذیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76567" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TE5vBdzDWxDVkxDTJJRNk9tl7tfED2jfq0z6XBwzcp2t4Xfz-erp_1iONUgAnLnPkBcfZn46HTN6gEMyV1AYcIVO0RINd5xppdwsFtEhg8pTx8tuEm8vDKb9_ot05eLsYCiVAZVcnZ9CfU1kbgIQ0d39oHTjqHN6FSPlrJDr9kUn57Rf4oIeThqWkxmXzixcteUDmwxCXEvwwZPxwWp9aQaO0LABehe9L9rKuNeQtpc0b_K2EQNw5BJ9lmmcn7qhZNbUZclbgcMPSkl3Tbfll8iMklulh1kiEXbjSu-YA9EL9q2quf6zNUBGTQcPHydV6ZtVz3f-o6ezNsu3ZGZXyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد همزمان با برگزاری مذاکرات در سوئیس، به مقام‌های جمهوری اسلامی درباره هرگونه اقدام برای بستن تنگه هرمز هشدار داده است.
او در گفتگو با شبکه فاکس‌نیوز گفت این هشدار شنبه شب به تهران منتقل شده و تاکید کرد در صورت چنین اقدامی، ایران با پیامدهای سنگینی مواجه خواهد شد.
ترامپ همچنین گفت به مقام‌های ایرانی گفته‌ام که اگر تنگه هرمز بسته شود، «دیگر کشوری نخواهند داشت و حتی امکان بازگشت به کشور خود را هم از دست خواهند داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76566" target="_blank">📅 17:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/khtfxvD7Aa9wtj4IMfeZLXLuZ4oaKh5TfPjUNoHbIDNZU1euUfVcq7czwkQtHzkqx-NcW87rk8oadnaYZ6DYm_2fYepg2RHY6BLyBwSuMHLPBFvcPMwCYAWsJcrvxPcsQGz3M-ztvs1R2dwjirlUqoBsoOX39bHYn-44tJuqsMs1ya7DFaRAo_z_JI3W0JeDXJqXudYpLw_MmOdbb0y4tywYQLR6KStQ7oyFL-WupCgz0Uf240fdFbCuMs-bvjGPdzHAOvD-YTr2INPKshWUB3liE-rDl_LfzvjCYBsT0HqpYVOpQeR0Xm7Yk1MoOkO3hdQ-RhbCVm3ZmpeqrLagSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران باید فوراً جلوی نیروهای نیابتیِ بسیار پرهزینه‌اش در لبنان را بگیرد تا دیگر دردسر درست نکنند.
اگر این کار را نکنند، دوباره به ایران ضربه‌ای بسیار سنگین خواهیم زد؛ درست مثل هفته گذشته، اما این بار شدیدتر!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76565" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=thvY6KIFtP4nFzPCprjd2bKXz7bfmmqztEZ3Wah9x2v-dpzQBi9RYn7hDr2CAuaS1nfHJJLZMewgyVuPRgdIg5M7qF07jdwiCgeRcqWL1tm7LHSAxYQQDBq_Y4k_Ym-6CA4D3-h9NAwo-UT1P7hp21LUHcdApSTFE9cH1XrXlbDSTjCIkBu2Z61FKhvVbnKuZpyaFB0NW2TJOcsNNwlzyoxbBQWuAJN_18Mr7MeYt-bHEU6F8qmQqdARCh3l1IyQdMZbyiihc_yj7VSEP8tZWbrp90PSwrdgH1E_OugGOcAnANAOyGKwqTDaJ11uEmtxXuC_4NDEbeHJejS5AHvceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=thvY6KIFtP4nFzPCprjd2bKXz7bfmmqztEZ3Wah9x2v-dpzQBi9RYn7hDr2CAuaS1nfHJJLZMewgyVuPRgdIg5M7qF07jdwiCgeRcqWL1tm7LHSAxYQQDBq_Y4k_Ym-6CA4D3-h9NAwo-UT1P7hp21LUHcdApSTFE9cH1XrXlbDSTjCIkBu2Z61FKhvVbnKuZpyaFB0NW2TJOcsNNwlzyoxbBQWuAJN_18Mr7MeYt-bHEU6F8qmQqdARCh3l1IyQdMZbyiihc_yj7VSEP8tZWbrp90PSwrdgH1E_OugGOcAnANAOyGKwqTDaJ11uEmtxXuC_4NDEbeHJejS5AHvceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس و عراقچی در یک قاب
خبرگزاری تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده جمهوری اسلامی گزارش داد که هیات آمریکایی و برگزارکنندگان نشست ژنو قصد داشتند پیش از آغاز مذاکرات چندجانبه، مراسم عکس مشترک و صحنه دست دادن میان هیات‌های جمهوری اسلامی و آمریکا برگزار شود اما محمدباقر قالیباف مخالف کرده است.
به گفته این منبع، محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، با این تشریفات مخالفت کرد و اعلام کرد اعضای هیات جمهوری اسلامی در مراسم عکس مشترک با هیات آمریکایی حضور نخواهند داشت.
این منبع افزود در پی مخالفت هیات جمهوری اسلامی و خودداری آن از حضور در این مراسم، پخش مستقیم و برنامه عکس مشترک لغو شد و پس از آن هیات جمهوری اسلامی وارد محل برگزاری مذاکرات شد.
به گفته این منبع، هیات آمریکایی از هیات جمهوری اسلامی پنج دقیقه فرصت خواست تا خبرنگاران محل مذاکرات را ترک کنند. او افزود مراسم پیش از آغاز مذاکرات، بدون حضور هیات جمهوری اسلامی برگزار شد.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز یکشنبه در آغاز مذاکرات ایالات متحده و ایران در سوئیس، این گفت‌وگوها را «تاریخی» خواند و تأکید کرد ایالات متحده آماده است روابط خود با ایران را به شکل بنیادین متحول کند.
ونس در حالی که در کنار نخست‌وزیران پاکستان و قطر ایستاده بود، در اقامتگاه بورگن‌اشتوک در کنار دریاچه لوتسرن گفت: «این یک دیدار تاریخی است. پیش از این هیچوقت رهبران ایران و آمریکا در چنین سطح بالایی با یکدیگر دیدار نکرده‌اند.»
تصاویر و ویدئوهای منتشر شده از محل نشست نشان می‌دهد هنگام حضور معاون رئیس‌جمهور آمریکا در اتاق محل مذاکرات، عباس عراقچی، وزیر خارجه ایران، نیز حضور دارد.
معاون رئیس‌جمهور آمریکا درباره اهداف مذاکره با ایران گفت: «آنچه رئیس‌جمهور از ما خواسته این است که فصل تازه‌ای را آغاز کنیم تا روابط خود با مردم ایران را متحول کنیم و دست دوستی را به سوی آن‌ها دراز کنیم. پیامی که به مردم ایران می‌گوید اگر رهبران شما حاضر باشند از نقش‌آفرینی به عنوان عامل بی‌ثباتی منطقه دست بردارند، و اگر حاضر باشند در بلندمدت از جاه‌طلبی‌های هسته‌ای خود صرف‌نظر کنند، آنگاه ایالات متحده آماده است روابط خود با آن کشور را به شکل بنیادین دگرگون کند.»
او ادامه داد: «این بدون تردید هدف ماست.»
ونس همچنین گفت: «ما تنها در چند ساعت گذشته پیشرفت‌های بزرگی داشته‌ایم و انتظار دارم در ساعت‌های پیش رو نیز پیشرفت‌های بیشتری حاصل شود.»
او با اشاره به اراده ایالات متحده برای «متحول کردن» خاورمیانه، افزود: «ایران در گذشته یکی از عوامل بی‌ثباتی منطقه بوده است. اکنون آینده‌ای را می‌بینیم که در آن همه بتوانند برای پیشبرد صلح و رفاه برای همگان با یکدیگر همکاری کنند.»
@
VahidHeadline
جی‌دی ونس پیش از آغاز مذاکرات اعلام کرد واشینگتن طی ماه‌های اخیر بیش از هر کشور دیگری برای توقف درگیری‌ها در لبنان تلاش کرده و این روند را ادامه خواهد داد.
او با تأکید بر اینکه «صلح آسان نیست» گفت رسیدن به توافق نیازمند تلاش و «بده‌بستان» میان طرف‌هاست و افزود هدف آمریکا تنها صلح با ایران نیست، بلکه دستیابی به ثبات در کل منطقه دنبال می‌شود.
ونس همچنین مذاکرات جاری را «آغاز یک گفتگوی فنی» توصیف کرد که قرار نیست همه اختلافات را یک‌باره حل کند، اما فرصتی فراهم می‌کند تا طرف‌ها برای نخستین‌بار درباره مسائل اصلی به‌صورت مستقیم گفتگو کنند.
به گفته او، حضور رهبران سیاسی برای تعیین چارچوب مذاکرات و حمایت از تیم‌های فنی است و با وجود چالش‌های پیش‌رو، طرف‌ها با انگیزه برای ادامه مسیر آماده هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76564" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=SCVOPJBlmFscs65mi6CfuneBg08YIX9CU9cbFBleHFcBfsQKrZL9dePgBRfy5brqKvWCvUVhIxx5RLYEjk-2FAcRKDm1Xnq8y81t3RXaFiFBdZXLWj6M94Dwjk_zmxw7_Nu-ah3sFdkHDHV12F4Ex4f_XJRRzfTH1-wXbgOWDhCuFv_9K3F2zUqeJkBJoLx5KvmppG3-bt1xRWHXtYhgxFiHnbPGv04ZHqdmLPxYS9pXEtlQazGCG8tYf2TsMFqK_Deavw462wdEngokNSlGvZYsX47-iEIcIhg1bjQ4K8zsmnraCL0wo8_33VlqYtOyRXFfz8bXMrNI4WMvuqcsyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=SCVOPJBlmFscs65mi6CfuneBg08YIX9CU9cbFBleHFcBfsQKrZL9dePgBRfy5brqKvWCvUVhIxx5RLYEjk-2FAcRKDm1Xnq8y81t3RXaFiFBdZXLWj6M94Dwjk_zmxw7_Nu-ah3sFdkHDHV12F4Ex4f_XJRRzfTH1-wXbgOWDhCuFv_9K3F2zUqeJkBJoLx5KvmppG3-bt1xRWHXtYhgxFiHnbPGv04ZHqdmLPxYS9pXEtlQazGCG8tYf2TsMFqK_Deavw462wdEngokNSlGvZYsX47-iEIcIhg1bjQ4K8zsmnraCL0wo8_33VlqYtOyRXFfz8bXMrNI4WMvuqcsyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، همزمان با برگزاری مذاکرات مستقیم میان ایران و آمریکا در سوئیس، گفت همه نظامیان در شورای امنیت ملی موافق مذاکره بوده‌اند.
او در جلسه‌ای به مناسبت تشکیل بسیج اساتید در دانشگاه تهران، در میان صدای اعتراض عده‌ای از حاضران گفت: «همه امضا کرده‌اند که این راه را باید برویم. حالا هر کسی می‌خواهد تفرقه ایجاد کند، این گوی و این میدان.»
او با اشاره به نظر فرماندهان نظامی در شورای امنیت ملی گفت: «فرمانده قرارگاه [خاتم الانبیاء]، فرمانده ارتش و سپاه، و نهادهای امنیتی همه بودند و همه یک حرف زدند و همه متحد بودند و همه آن چیزی را که می‌خواستیم عمل کنیم را امضا کردند.»
این سخنان پزشکیان در پی افزایش انتقاد اصولگرایان تندرو از دولت در پی انتشار نامه منسوب به مجتبی خامنه‌ای صورت می‌گیرد.
آقای پزشکیان همچنین با تاکید بر نقش دولت در حمایت از نظامیان در دوران جنگ گفت: «۲۰ میلیون بشکه نفت که مال دولت بود را به هوافضای سپاه دادیم. ارزهایی که داشتیم را به این عزیزان دادیم.»
@
VahidHeadline
مسعود پزشکیان، رییس‌ دولت جمهوری اسلامی، گفت نگرانی اصلی او این است که دولت نتواند رضایت مردم را جلب کند و نارضایتی‌ها به اعتراض‌های خیابانی منجر شود.
پزشکیان گفت: «از آنچه می‌ترسم این است که نتوانیم به مردم به درستی خدمت بدهیم، ناراضی شوند و به خیابان بیایند و اعتراض کنند. آن وقت ابهت ما فرو می‌ریزد.»
او افزود مهم‌ترین قدرت جمهوری اسلامی، وحدت مردم است و مسئولان نباید اجازه دهند کمبودها، کسری‌ها و نواقص باعث نارضایتی مردم شود. به گفته پزشکیان، بروز چنین وضعیتی موجب «خوشحالی دشمنان» خواهد شد.
@
VahidOOnLine
بعضی از جملات پزشکیان به انتخاب خبرگزاری دانشجو، وابسته بسیج:
🔸
اظهارات عجیب پزشکیان: من از این میترسم که نتوانیم مردم راضی کنیم و به خیابان بیایند اعتراض کنند
🔸
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد بود.
🔸
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔸
۶ میلیارد دلار پول ما در قطر برخواهد گشت.نتانیاهو اولین ناراضی از مذاکرات است.
🔸
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم، این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
🔸
شورای عالی امنیت ملی در وحدت و انسجام تصمیم گرفت؛ همه یک حرف زدند و متحد بودند
🔸
مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده/ آنها پذیرفتند که حق ملت ایران را نمی‌توانند نادیده بگیرند/ قاعده عوض شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76562" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLTiv089UaHX8pk1BfYnqtRf0cufZT4h8MVuoFOOC1iciyPtRQlUuLCAvsIylTOkZg_IcGNbogwJnBKLLRO5kcXOlaOdH-QlfCTIrTBQLN0Vk3Gj0_L5uV3cgLNvVvbwZSmf9ff82qijQdH2OnoPqaJS9MEIa_5mdVMrvuWJRDD8ilAOtQ4VriMydGbHipCDrIDFtCDY0IBUWUdXjftSWJl0jQRJu5sjN0GtrD_9bONhe8WiuA4_LqJs3-Pe8URFjT68AyXPKvmtjaYYT-W8B6a-rdNa5_9EfM5nI-PGna03zEqNb6uOFlSJ57E-JkpSJmdSdZZV68ULz-7fc94jwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو منبع منطقه‌ای آگاه گزارش داده است که آمریکا می‌خواهد نخستین دور گفت‌وگوها با ایران با دعوت تهران از بازرسان سازمان ملل برای بازدید از تاسیسات هسته‌ای ایران پایان یابد.
به گفته این منابع، این تاسیسات پیش‌تر هدف حملات آمریکا و اسرائیل قرار گرفته‌اند و آخرین بازدید بازرسان از آنها پیش از جنگ قبلی، در ژوئن ۲۰۲۵، انجام شده بود.
اکسیوس می‌گوید: «آمریکا در مقابل آماده است به ایران اجازه دهد به بخشی از دارایی‌های مسدودشده خود دسترسی پیدا کند؛ از جمله حسابی به ارزش شش میلیارد دلار در قطر.»
بر اساس این گزارش، ایران می‌تواند از این پول برای خرید کالاهای بشردوستانه استفاده کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76561" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOMOqGFVogBlOeG32h1Bd9jwlKKnlwuaRvXw8bFHylg9mJ6UARCovRYttFQg_escdrNgHbCRA-LriadlvqEu6GvL_fx4cDMqMyKPP_vJMfsLe4YR5JF7EG3u7dT3r8VElNYiegkYKfUMst7KLjZs5s-4uAl-HEmt3uj3pJxg4MAgWxKxkGmuLohxGz4bi27qxav7_aQmmkmOUvBmjHyDOU-JHifsLHWPqI2lrcTAur4RzmDnSd3LXRpWfgbI_OmyG6K_kWjDRbE7KS5hfQAYDYQtWNwB0nxj2pYBYWU9CuEikiiJyhLb4wB3bKlf5TZ6fOG53sr9GTWlY8pLkF9OXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های بهداشتی در غزه می‌گویند که دست‌کم ۱۰ فلسطینی در حملات هوایی و تیراندازی نیروهای اسرائیلی در چند حمله جداگانه کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76560" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJtFyLH7ZteD47SPuqVBCbhH6HtanY7cIVf1V_EBD80o77OJ-PEMaKTCNYI9z2CybLvuRGDeHEvYPirjWdzk8EDhhThxwj9WDgNQ8q_XvDqWSoPqQHuh460Zwvj-H8VZ4mD7eBzQvhSBuJ-1dHAhRJGJQxOEp-dFm5FACbD_25A_Ud_rzQbZ8DhWLfuZ9exjVq99rt56e43JwNwlHxnXphmnJvP2I53g6qBlzzx1fIkle1_dE6KpKn0oEBFAk7nzdT80PAOjmxz9SyoRWDGCAbMiO6Rhk1BbTkw2asVa3YsRhsF1aX-3sICjiAKUqZJaJQPGRyUI3-QlwTpiclX6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از هزار دانشجو و فارغ‌التحصیل دانشگاه صنعتی شریف با امضای نامه‌ای سرگشاده خطاب به محمدرضا تجریشی، رییس این دانشگاه، نسبت به آنچه «تشدید فضای امنیتی» و گسترش برخوردهای انضباطی با دانشجویان خوانده‌اند اعتراض کردند و خواستار پاسخگویی مدیریت دانشگاه شدند.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف تاکید کرد که بیش از هزار نفر این نامه را امضا کرده‌اند. انتشار این نامه یک روز پس از رسانه‌ای شدن صدور احکام اخراج برای شماری از دانشجویان شریف صورت گرفت.
امضاکنندگان در این نامه نوشته‌اند که در ماه‌های اخیر دست‌کم ۳۰ پرونده در کمیته انضباطی دانشگاه تشکیل شده و ۱۳ دانشجو با احکام بدوی تعلیق یا اخراج مواجه شده‌اند. به گفته آنان، احکام سه دانشجو نیز در مرحله تجدیدنظر تایید شده است.
نویسندگان نامه تأکید کرده‌اند که آنچه در دانشگاه می‌گذرد، ادامه «روندی نگران‌کننده» است که به دلیل نبود واکنش مؤثر از سوی مدیریت دانشگاه، هر روز ابعاد گسترده‌تری پیدا می‌کند. آنها همچنین نسبت به افزایش سرخوردگی دانشجویان، گسترش بی‌اعتمادی در فضای دانشگاه و آسیب دیدن اعتبار علمی دانشگاه صنعتی شریف هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/76559" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fke9NWKEyNzNQsLqePw8siOxd38GoEPqwDuxobyZ7zO7PeE2xbMBGN0NvX729RbigTXUkXJYNLqq7RnjVPRduy_LGMvkZ0vHwnpPzjpLBf9R0NjzKemJsTiA-X5fEqX8VLxvh2oL97uSkdMqGMS0GsgiY75GKxyaQc0PLukkVym47IJwzx-oBvrlC4y1vMqBN7VQQoMPXfRQRtYbnc7-xLF6fUWN1kiyFmskMYfViVlzhzzOqLohsudM9ayl1JO7lTbb2G3ld2m6-GApc0Be2raOtWg4Bcn5tXFMiCUtg4984-JJK_ntck1QQirWgFw0iIDg8XcPWmqqJgRIw7Dyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_KUC1V5RzFR_ovpJjdAEmxSc-I-H-5oyMj1GNI7oANsrr7hJkzgZ_WyY_QP7iZ6JVH9uQKwB_MPKOUSGeI-Ji89uOiB4wLqO58KWsY2f6jdz8EQ8tjeTtlo2a1kxcUuv-bnfua5S5P1cIrH2ZWtmOcDSqL3Jhz-bEyoVdljdsNz7eUUbfb8b6PwE4t2ST2sdQShmpTPA1SlC4RaH5tc7hds6QaRzN3XNxGz6Kiv6uYMosCPyQczTzaykD-AchI7XG-t4Ixfe62KSxC005PkHyJtnAYV6jL9-oICvuWQYScoebYo7N26cPWCL4C8iiFaP_O3eaCjiSNZEtGhIeyrkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
جواد علیکردی، وکیل دادگستری زندانی، توسط شعبه اول دادگاه انقلاب مشهد به ۱۸ سال حبس، انفصال دائم از حرفه وکالت، دو سال تبعید به سراوان و دو سال منع خروج از کشور محکوم شد. جلسه رسیدگی به اتهامات او در ۲۰ خرداد ۱۴۰۵ برگزار شده بود.
🔸
به گزارش خبرگزاری هرانا، آقای علیکردی از بابت اتهام «اجتماع و تبانی برای اقدام علیه امنیت ملی» به پنج سال حبس و از بابت اتهام «فعالیت تبلیغی برخلاف امنیت ملی» به ۱۳ سال حبس محکوم شده است. پرونده او پیش‌تر در شعبه ۹۰۲ دادسرای مشهد مورد رسیدگی قرار گرفته و پس از صدور کیفرخواست به دادگاه انقلاب ارجاع شده بود.
🔸
جواد علیکردی در ۲۱ آذر ۱۴۰۴ توسط نیروهای امنیتی در مشهد بازداشت شد. او ابتدا به یکی از بازداشتگاه‌های امنیتی منتقل و سپس به زندان وکیل‌آباد مشهد انتقال یافت.
🔸
آقای علیکردی برادر خسرو علیکردی، وکیل دادگستری و مدافع حقوق بشر است که در آذر ۱۴۰۴ به شکل مشکوکی درگذشت. وی پیش‌تر نیز در پرونده‌ای جداگانه با اتهامات سیاسی و امنیتی محکوم شده بود که اجرای بخشی از احکام صادره
علیه او به حالت تعلیق درآمده بود.
@IranRights</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76556" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9o623XPjAVbBsvAPUF-XOQ3fulhnuvEdECm7CnCk_-N7hPVT1_XZ8lFHG0ORYOjJk2leSgQurmEiZx9SKQBJbHfqQXIfjg3q4SW9FXvqn5UyzZH4T8eTvLoir6C-MHYfBPI33Dqn-RW0qZ1NXNRzhlrKaglrY-LceXpQKezlFIOkVUIFYmbPysyXmkDYcJNaMZwqfGLqATMtOBUiBb_8pWQeap9lvXKbfWIy10TrJ0TRcfVjhTA2sN60TbrB8R0ao9TKTY56TX8Wo5UZrHkoRjZ0CYFnt7sgBWi1fhWyub4qNqCUo2proteugSqRW_6lp7_5v4z5dwmtfl8RAjwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ‌گونه عوارضی در تنگه هرمز وجود نخواهد داشت مگر به نفع آمریکا
ترجمه ماشین:
در دوره ۶۰ روزه آتش‌بس، در تنگه هرمز
هیچ عوارضی در کار نخواهد بود
،
و پس از پایان دوره ۶۰ روزه نیز
هیچ عوارضی پرداخت نخواهد شد
؛
مگر آن‌که، در صورت تکمیل نشدن توافق، این عوارض
از سوی ایالات متحده و به نفع آمریکا
وضع شود؛
آن هم بابت خدماتی که این کشور به عنوان «فرشته نگهبان» کشورهای خاورمیانه ارائه داده، برای جبران هزینه‌های گذشته، حال و آینده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLxXtovhVNnpE5u6mDY0dlFlC7eI2VSh5tfrl8X-Dd6as1jWu4chI9Cf9yGsCRoq-g9PLowcUL5rZbj57vRQT4Cd_qYWEq1E7ICBk8q5r1hzuQjqnujf3Y8nq4b2kOabx2neMD_q36-WaW8-eC0wocvzxtdyCu2LuvCW4utRfVFAmxkbFyXFyBS_TGfesUz7X1QtWwUvdjlECLY2zTpFgoUzEjbpTimmEfUV2TSQCaZAYf5lpH8mZ1F5ZqaASBLtBDH6jKWMzIssTiyv31TqeVfnjopdVwk73G0BBMdus4l9-o0UBvMx5e4nzc7qrs3_nuOUzIP6M5qn_NhUSy3AjXK8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLxXtovhVNnpE5u6mDY0dlFlC7eI2VSh5tfrl8X-Dd6as1jWu4chI9Cf9yGsCRoq-g9PLowcUL5rZbj57vRQT4Cd_qYWEq1E7ICBk8q5r1hzuQjqnujf3Y8nq4b2kOabx2neMD_q36-WaW8-eC0wocvzxtdyCu2LuvCW4utRfVFAmxkbFyXFyBS_TGfesUz7X1QtWwUvdjlECLY2zTpFgoUzEjbpTimmEfUV2TSQCaZAYf5lpH8mZ1F5ZqaASBLtBDH6jKWMzIssTiyv31TqeVfnjopdVwk73G0BBMdus4l9-o0UBvMx5e4nzc7qrs3_nuOUzIP6M5qn_NhUSy3AjXK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبویان: مجتبی خامنه‌ای نامه داده بود که چرا شروط من رو در مذاکره رعایت نکردید؟
07:20
صدا و سیما: افشای مکاتبات مجتبی خامنه‌ای از سوی نبویان در شبکه خبر پیگرد قضایی دارد
صداوسیمای جمهوری اسلامی ایران اظهارات محمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس، در شبکه خبر پیرامون مذاکرات پیش رو بین ایران و آمریکا را «مصداق تخلف قانونی و مستوجب پیگرد قضایی» عنوان و اعلام کرد «مدیرکل مربوطهٔ این شبکه استعفا کرده است».
محمود نبویان، که به جناح تندرو موسوم به «پایداری» تعلق دارد، روز شنبه ۳۰ خرداد با خواندن بخش‌هایی از متن‌هایی که گفت مکاتبات مجتبی خامنه‌ای با هیئت مذاکره‌کننده است، مدعی شد رهبر جمهوری اسلامی در مراحل مختلف با روند مذاکرات و بندهای متن‌های گوناگون مرتبط با مذاکرات مخالف بوده است.
این گفت‌وگو پیش از آن‌که نبویان به متن نهایی تفاهم‌نامه برسد، قطع شد و موجی از واکنش‌ها را در میان دیگر چهره‌ها و فعالان رسانه‌ای جمهوری اسلامی در پی داشت.
صداوسیما در بیانیهٔ خود اعلام کرد نبویان در اظهاراتش «اشارهٔ ناقص و مخدوش به برخی اسناد دارای طبقه‌بندی» داشته و سعید آجورلو، عضو تیم رسانه‌ای هیئت مذاکره‌کننده و از چهره‌های نزدیک محمدباقر قالیباف، نیز او را به «تحریف عمدی متون» با هدف «فرار از پاسخگویی درباره ادعاهای نادرست قبلی» متهم کرد.
محمود نبویان، ۲۳ خرداد ماه، در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا، در یک برنامهٔ زنده در یک خبرگزاری نزدیک به سپاه، متنی را که مدعی بود تفاهم‌نامهٔ ایران و آمریکا است، روخوانی و از برخی بندهای آن به‌شدت انتقاد کرده بود.
نبویان یکی از اعضای گروهی بود که پس از اعلام آتش‌بس جنگ ۴۰ روزه، همراه هیئت مذاکره‌کنندهٔ با آمریکا به اسلام‌آباد رفته بود.
مجتبی خامنه‌ای، که پس از اعلام رهبری هنوز هیچ صدا و تصویری از او منتشر نشده، پس از امضای تفاهم‌نامه توسط رؤسای جمهور ایران و آمریکا در پیامی مکتوب اعلام کرد «نظر دیگری» داشته اما «با تعهدی» که پزشکیان به او داده، مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا گذاشته است.
@
VahidHeadline
حمید رسایی با انتشار ویدیوی بالا نوشت:
نبویان در آنتن زنده شبکه خبر، در حال تشریح جزئیات نامه‌های رد و بدل‌شده میان رهبر معظم انقلاب و شورای عالی امنیت ملی بود که پخش برنامه به بهانه میان‌برنامه به صورت کامل متوقف شد!
ما که از یادداشت‌های آن امام شهید در این باره اطلاع پیدا نکردیم ولی گوشه‌ای از یادداشت‌های امام حاضر توسط آقای نبویان در حال پخش از سیما بود مانع آن شدند!
صدا و سیما:
🔹
روابط عمومی معاونت سیاسی صداوسیما: به استحضار مخاطبان محترم شبکه خبر می‌رساند اظهارات یک نماینده مجلس دعوت‌شده به برنامه امروز زنده این شبکه و اشاره ناقص و مخدوش وی به برخی اسناد دارای طبقه‌بندی و مکاتبات مسئولان عالی کشور، مصداق تخلف قانونی و مستوجب پیگرد قضایی است و سازمان صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار می‌دهد.
🔹
شبکه خبر ضمن ابراز تاسف بابت بی‌توجهی مهمان مذکور به قواعد اخلاقی و الزامات آنتن زنده، به اطلاع می‌رساند مدیریت این شبکه ضمن پذیرش استعفای مدیرکل مربوطه، برخوردهای انضباطی لازم را به دلیل بی‌توجهی به الزامات برنامه‌های زنده و سهل‌انگاری در مدیریت حرفه‌ای به عمل خواهد آورد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76554" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qROkNSAmy8qZK0XnyNe0WEAqtO0QP4TET83snJSJmA8I4UJf1lBAGXhMBrye76hYKFOlruBOhQiMGMxNCopohtT-tQrwr0lW8opelUwGTrbUoy1HXX7Xt7vUiHR8slVeJd6q7styl5zCIEJUk0JpDewWlVxFX6RBbu4AOyv1geliZrtGHIrBeCDIiPRYsdAZpbWNtUwJqULHkSofJ7_e9xrTxIR0GhifEjLUsjSgtp2CU9i97azQ3PnPm6m0cdHiFjU2hToVse4Md9N3wcqWJYLVIdVoLQiPDXTM9kh3poX_pc9L5V0xLylQa_M7wb1SgMBUWDaeA7FIF6LuagUlzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mWrZGs31cwjYHk4SAA_61TfLsdFrZtqyGK5sF7_ZSVxL8xNUMaq2M9_0gUq6glCnHYDW-JPBX0tweizXpwOjyrhrQJwr5rWZLXNunj6pr9WrxQLb5_HOkLJTlFO1N8e7rX7OPKtNhiCrUpr69e79-w4SkBqsTlBNIC4sJ_Mp3GTMFSyDZJXZwjHa8alR2v3Nob1p-6dlvznRcc-HuTmR5iRBX0NPMLYX0fxOAQ32yVUSdqg0P7J74yWfg-2C3iS4blFSc5bBSv_6lfx2HJB3NyQ_fKyl16Juab1OTZ0xu2Ezc4Hze3Iz3-w94kZvSsW9F_FVOC_4pw-tt9NWSFyp2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ در تروث سوشال نوشت: محبوبیت ملونی در ایتالیا به شدت کاهش یافته، شاید به این دلیل که او و ناتو در جریان ماموریت جلوگیری از دستیابی ایران به سلاح هسته‌ای، به ایالات متحده پشت کردند.
ایتالیا حتی اجازه استفاده از باندهای پروازی خود را به ما نداد که یک مانع لوجستیکی بزرگ بود؛ آن هم در حالی که آمریکا سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند.
رئیس‌جمهوری آمریکا در پایان با لحنی تحقیرآمیز تاکید کرد: اکنون که ایالات متحده ایران را از نظر نظامی شکست داده، او می‌خواهد برای بالا بردن آمار محبوبیتش دوباره با ما رفیق شود؛ اما نه، ممنون!
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، با انتشار بیانیه‌ای تند در صفحه اینستاگرام خود، به هجمه‌های اخیر دونالد ترامپ پاسخ داد و حملات کلامی رئیس‌جمهوری آمریکا را «بی‌دلیل و بی‌معنی» خواند.
ملونی در این پیام خطاب به ترامپ نوشت: «محبوبیت من به هیچ‌وجه به رابطه با شما بستگی ندارد و دوستی با شما نیز کمکی به آن نکرده است. محبوبیت من حاصل توانایی‌ام در دفاع از منافع ملی ایتالیاست؛ یعنی همان کاری که همواره انجام داده‌ام.»
نخست‌وزیر ایتالیا همچنین با دفاع از تصمیم خود در جریان جنگ اخیر و عدم اجازه به آمریکا برای استفاده از پایگاه‌های نظامی این کشور، افزود: «نحوه استفاده از پایگاه‌های نظامی آمریکا در خاک ما، تابع توافق‌نامه‌های متقابلی است که ما همیشه به آن‌ها احترام گذاشته‌ایم. تا زمانی که من نخست‌وزیر هستم، این توافقات نباید نقض شوند؛ چرا که ایتالیا یک کشور مستقل و دارای حق حاکمیت باقی می‌ماند.»
ملونی در پایان نوشت: «در هر صورت، میزان محبوبیت من اصلا به شما مربوط نیست. پیشنهاد می‌کنم شما روی محبوبیت خودتان تمرکز کنید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76552" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDa6BSHaXckdxh7rgq_WEDmtWjimPPksVKWvQx7EWzafYMs9Quz0YsGQBI2im56jMfEQ4EmaI7CIcM1v49YXqT_Yi9-BeSTO1FsSQSdjeWICCN2Cga_dllyQ2ECDAeW7SVmoJANAgrMqUXO7RVOgY7BWgiYsfVntIzGN2wZaMPFL7HyEkcmZxI96KYsLjAuZWxmR_ZCUz-vcjlS-pMeVWkQjxrrfPNO37pK0-0c49JjOJwvmMpSPdIsjbZmL_IsoJ7ImA0eKak2FSNKboEIntoTb6VNR_M_TR8MAZ1LLns-zONnG59WgRSQqNvAshVvzV-M0t1nlevdVdFzN5kadnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که هیات مذاکره‌کننده جمهوری اسلامی به ریاست محمدباقر قالیباف و با حضور عباس عراقچی، عازم سوئیس شده است.
بر اساس این گزارش، عبدالناصر همتی، رییس کل بانک مرکزی و علی باقری کنی، معاون بین‌الملل دبیرخانه شورای عالی امنیت ملی نیز در این سفر حضور خواهند داشت.
همچنین کاظم غریب‌آبادی، معاون و اسماعیل بقائی، سخنگوری وزارت خارجه و حمید بورد، معاون وزیر نفت نیز این افراد را همراهی می‌کنند.
پیش‌تر وزارت خارجه پاستان اعلام کرد که مذاکرات فنی میان جمهوری اسلامی و آمریکا، یکشنبه در سوئیس آغاز خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76551" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SAFJ1d-nmJl7JQCOLT-F-BBnDwLSjuxoaMiGcmXXAAvuZt2rqV1nayVX8YU76iJz7uFXQEWshL4bkdES_xsfxb_55tFy6TBnqk53z_E5tHxPMFVJQ94GKkJNwnvJ-lgZIIz9b0OK1JrHQUw6gC1dd2ktH_-99NZNav8cLWX4UxLiAipF5-WyHX9y35S_tduTOtHk9WP-Yms6cqrFvCWAHo9NSsB9C62zUiBRUdGYt26H0GlwNze6y5G22IHDf7z2Mu-dYnlY5CkCsrkX5HPQj_mM9bjzNupldtSsue9fWXq2Og1Xlx3sX-sScwk_50Hnil81eDHx3HOS-A8fp9YzYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی مرکزی ایالات متحده،
ترجمه ماشین:
عبور کشتی‌های تجاری از تنگه باز هرمز
تامپا، فلوریدا — تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت؛ همزمان نیروهای آمریکایی به عملیات خود در منطقه کلی ادامه دادند تا از آزادی کشتیرانی حمایت کنند.
امروز عبور امن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری از آن عبور کردند؛ کشتی‌هایی که حجم زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل کردند.
مرکز مشترک اطلاعات دریایی این هفته اطلاعیه‌ای صادر کرد و در آن عبور امن همه کشتی‌ها را در یک مسیر تعیین‌شده تأیید کرد؛ مسیری که از ادعاهای خودسرانه درباره الزامات یا هرگونه مانع، آزاد است. جزئیات مربوط به عبور امن را می‌توان در اینجا دید:
ukmto.org
نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اجرا و به‌طور کامل برقرار و لازم‌الاجرا باقی می‌ماند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76550" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=GhMiZmMO98iTlPK01nIEkFoFM1MiuW98z-LmtAdpvpSfNsPf9eE3O0qXjhahrXez7iuQMw0221H48K1LzRx7dhdcPjOsQMDXJ5zVUCr_-wQEB9zRNcsyrdT8fyH3cUytJFlodYCCS9OUkO-Io7UZ1XfeVTChfosaLZfvSipmABU3VfyjlCn6uazq7QevOPFJBOp4w74psaVInjhHKN7kuznpeClUVavOzQjZh1_j84pJsf1Ypnx1iNqxmB7VtzTczyLYFkuuex1XXHBcA53DRjUnTDugmyJmmUTtph9jm9BVlTzTSfb9adOavUD570nGqTeAcloNkDBOnnrfVjKoEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=GhMiZmMO98iTlPK01nIEkFoFM1MiuW98z-LmtAdpvpSfNsPf9eE3O0qXjhahrXez7iuQMw0221H48K1LzRx7dhdcPjOsQMDXJ5zVUCr_-wQEB9zRNcsyrdT8fyH3cUytJFlodYCCS9OUkO-Io7UZ1XfeVTChfosaLZfvSipmABU3VfyjlCn6uazq7QevOPFJBOp4w74psaVInjhHKN7kuznpeClUVavOzQjZh1_j84pJsf1Ypnx1iNqxmB7VtzTczyLYFkuuex1XXHBcA53DRjUnTDugmyJmmUTtph9jm9BVlTzTSfb9adOavUD570nGqTeAcloNkDBOnnrfVjKoEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی پربازدید شده که مادر مانی صفرپور، جوان کشته‌شده در اعتراضات دی‌ماه، را در حال سوگواری برای فرزندش در کنار یک دستۀ عزاداری نشان می‌دهد.
عکس پسرش را بالای دست گرفته و می‌گوید «پسرم، پسرم».
مانی صفر‌پور، جوان ۱۸ سالۀ لاهیجانی، ۱۸ دی‌ماه ۱۴۰۴ با شلیک نیروهای حکومتی در محلۀ سلسبیل تهران کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76548" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76547">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KbZHG5ZwQKvN4kXVlc1RhBX9_Q-o0AOtIbUER8PXnetGLHZ0KJrxwm-AwAEUqli30r8NSpoPL4MygP4ny3-m2y6N_AGqKE0BdOfiG-IJwIJM4vMbDKbtTIqDoklWYMDN3HG6j2xO8WZQH4nir5VV_x4PRWvMEqZHgWSCNLxvXXy0J0D6zC6c6FzhbPq0NIzBQt4QJQwUXzT6BxpSYHCezCnG7hgQ1P-lSPTTK6wtqgZEVIYfhifiHJmMrwfOhATOX1sjDi1zWu1ODZA_xdbo-9Hjnws8NayyiCld0BfPrfGwgdKF3KDFiQHrD1wAnvj6arrFrQO6yNoP1TRW_D0wew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد تنگه هرمز در واکنش به «نقض تعهدات امریکا در اجرای آتش‌بس» و «حملات اسرائیل در لبنان»، به روی همه شناورها بسته شد.
نیروی دریایی سپاه همچنین از شناورها خواست به تنگه هرمز نزدیک نشوند و هشدار داد در غیر این صورت، امنیت آن‌ها به خطر خواهد افتاد.
قرارگاه مرکزی خاتم‌الانبیا، واحدی از سپاه پاسداران هم اعلام کرد تنگه هرمز به‌دلیل «بدعهدی و پیمان‌شکنی» امریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه، به روی تردد کشتی‌ها بسته شده است.
قرارگاه مرکزی خاتم‌الانبیا روز شنبه اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.
خبرگزاری فارس، وابسته به سپاه پاسداران به نقل از یک منبع نظامی در نیروی دریایی سپاه، عصر شنبه اعلام کرد که تنگه هرمز از دقایقی پیش به‌طور کامل بسته شده است.
حملات اسرائیل به جنوب لبنان در روز شنبه دست‌کم ۱۰ کشته بر جا گذاشته است. اسرائیل اعلام کرد این حملات در واکنش به پرتاب گلوله‌هایی از سوی حزب‌الله، گروه مورد حمایت جمهوری اسلامی، انجام شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76547" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LBVaQWFJiBGD4BaaWljc1RXlomq3_VaPzTi0JrQhW7sPK2hN6b-5eiebuwFlt99UZxvpu4CeQ-_txemEFI6XpMQUILFumMcDQABcxxxXa4-Cw4QgiQ6ODorLgZaC8ASIzcwpnXxBqvURuuyF9-1HdEAAcA2CCsvk-KG_2_LRAkfYfe6ZjHPBS-f5H3PQZDPKFUXyWbQ1NvQ2YXP4WzGltkMrfrvGuNkjsCSAIgppm-pXjG0JcH1tzVRGEAHzyF9qTUI4ahrzAnSMVSw5xDCLxgAJqFYc5uW5TG2Ew6C1MJqap3kPqaLx9ebYcrkjIN40j-7n4FhaXhqvb-dI5dY0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، روز شنبه ۳۰ خرداد در گفتگو با فاکس‌نیوز اعلام کرد که استیو ویتکاف، فرستاده ویژه ترامپ و جرد کوشنر، داماد او، «چند ساعتی است» که در سوئیس حضور دارند و مشغول بررسی «برخی از ابعاد فنی این مذاکرات» با ایران هستند. به گفته ونس، کوشنر و ویتکاف در گزارش‌های خود تاکید کرده‌اند که «امور به خوبی پیش می‌رود.»
ونس همچنین از احتمال ورود میانجی‌های قطری و پاکستانی به سوئیس برای پیوستن به این گفتگوها خبر داد و افزود: «قطری‌ها و پاکستانی‌ها می‌خواهند مطمئن شوند که ما این کار را به شیوه درست انجام می‌دهیم، بنابراین من تلاش می‌کنم به این روند احترام بگذارم.»
معاون ترامپ که سفر خود به سوئیس را در اواخر پنج‌شنبه شب به تعویق انداخته بود، بار دیگر تاکید کرد که انتظار دارد طی دو روز آینده عازم این کشور شود. او با این حال خاطرنشان کرد که هماهنگی‌های این سفر «همواره یک رقص هماهنگی ظریف دیپلماتیک است.» این مذاکرات که پیش‌تر قرار بود روز جمعه برگزار شود، پس از وقفه‌ای کوتاه دوباره در آستانه ازسرگیری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76546" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwyRkZ3ss3w7vLnd_BGydOeNDD1Pk1NpwRCOY6dVc7wvJsas6qtBS_Dpjbonr0BBodYWxrOtVD_OLb097md5p1rTTdiuhJYIL5NxtUfnT3BAZJpnMDvzLlf9jvT3wvbgPBsoYvgvaNm5kjMY8KZlEgJt2AUJwWk1vBWZsfX7xMSNTWr40m0-rp7Uar2SNR8W2KVEkKC20KOvHq3w1bsIE8vltoAi3SEmdmiS60EBIxpF3aPHxF_MTb6yTTHIkVZ7BSJq4nVJpzHvHo59rFCV3LkBa5rj_UCdEKee5WIjo7OJZIVIw0dfl9tI08UOFeMG8ig6Jw-EgKppFnGK41CXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«طاها نظری» معترض ۱۸ساله که پیشتر به‌دلیل حضور در اعتراضات ۱۸ و ۱۹دی۱۴۰۴ بازداشت شده بود، پس از  تشکیل جلسه رسیدگی به پرونده، به ۵سال حبس تعزیری محکوم شده است.
ماموران اطلاعات شاهرود، در فروردین ۱۴۰۵، طاها نظری را شناسایی و به صورت تلفنی احضار کردند. بعد از مراجعه به محل، این جوان ۱۸ساله به‌صورت موقت بازداشت و تحت فشار برای پذیرش اتهاماتی نظیر «ارتباط با تلویزیون‌های فارسی‌زبان و فیلم‌برداری از اعتراضات» به او نسبت داده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76545" target="_blank">📅 17:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kex-QnjvAC-YNqAfARrfrD6ZFUki2sN4NNICQbUytscKhFRscVWKzIcB50EaiiBwwyuy4H7CuR5DO5x5ntY0qeoGhzGh_zAZowDKWcwqy9kOGbw5WoFq8SbP4LiOnPDSsUg7asRPBLTaU6ByK07dzudmPAKwbdmBk7AqtBYG0eldxzLVp57j4hhWoTA0xXvypBOajv7d6vsWhL6TWX90v0Xkar7Ww9CRk2hfZwGfe3uDyk2Ra1NWqppZkANtIg49LVqEOhH83wJ-UvJJ0MV5KNSL_tVl8itpUO2LDTKQU9im4zJxCQrgmVBOFHoe_maktJm2pOvonD2MXKtXLdc0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tu_i019ZQOkc0BN2lutbZFaXbzmx7MJ9AMMmYpqFt5lw7QR0g-ERGZgIqW0UPvxM7LxLHcncu-K7sqLTPO3Ilxk-wh0_7L84rkF54B7qajeSCFF24--54vWjw9s_D5pta41oQLD2wlSGIrhy9Hyd9VzLnhuckiaW9llvXZBj7dSIbmTK-M127H9h_ivSBpX1Z3Wh8f7UA1yLu-bNOiDLTifX1pcPgajEtlJc_z1-9T5gxAcvKYFMlSsGKFW9hcXczwM-pZiHImN14ahOh3Vhb7WXu27TswwwaWsjnlFCRHFhmM4f8bfli_tuHD-0W8AbnJIrByVYfTT7C96R5S8hpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت دلار و دیگر ارزهای خارجی که در پی نتیجه موقت مذاکرات ایران و آمریکا کاهش یافته بود بار دیگر افزایشی شد.
روز شنبه، ۳۰ خردادماه، قیمت دلار آمریکا در بازار به ۱۶۲ هزار و ۵۰۰ تومان رسید. قیمت یک یوروی اروپا نیز در این روز به ۱۸۶ هزار و ۴۰۰ تومان رسید.
این در حالی است که در طی روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسیده و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شده بود.
روزنامه هم‌میهن روز شنبه قیمت سکه امامی را در بازار طلای ایران ۱۶۹ میلیون تومان گزارش کرد.
از زمان اعلام تفاهم‌نامه ایران و آمریکا در تلاش برای پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران شاهد کاهش قابل توجهی بود.
@
VahidHeadline
حسین صمصامی، عضو کمیسیون اقتصادی مجلس شورای اسلامی، در گفت‌وگو با سایت خبری تابناک افشا کرد که در هفت سال گذشته بیش از ۱۳۰ میلیارد دلار ارز حاصل از صادرات به کشور بازنگشته است.
این در حالی است که حکومت برای بازگرداندن ۲۴ میلیارد دلار دارایی مسدودشده کشور وارد چانه‌زنی فراوان با دولت ایالات متحده شده است، امری که نشان می‌دهد تا چه حد به این پول نیاز دارد.
در این میان بیشترین میزان عدم بازگشت ارز صادرات مربوط به سال ۱۴۰۴ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76543" target="_blank">📅 17:55 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
