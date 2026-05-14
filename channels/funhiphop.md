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
<img src="https://cdn4.telesco.pe/file/KJruVFYI-1redxzGQGWCpkvBkJDqsztibEMbusvAURYLQ2AZKZBHzpSAlk8jW34cU5xiq1GDUqk6uY7QeyyZ9LTRAhtQLDmln8ld_a91o2LL_hB3EohE4STV7nirjOGgJo-8hg5mNAFnCC3Mo7-zAGgft89LurzQn6U2IBG1YzBoJBeZKlzEcp-P6BzorpeCCVVZda0R9BXbz5lzT-WgDMu4UDzT_hu-FgQwDiB6m2wJxJRZv4Dq4F2rnFOzGhjK7Hq2WPMESuv260xBhsrnlIZN08O_zlsc88r2s1NCgSuUz37h7ni_b0jY2xd48IpxHgH4GtrjrM8T4Jy46WqQjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 141K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 12:58:16</div>
<hr>

<div class="tg-post" id="msg-74839">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کاخ سفید اعلام کرد دیدار و گفت‌وگوی ترامپ و شی جین‌پینگ «
مثبت و سازنده
» بوده و دو طرف
مذاکرات خوبی
با یکدیگر داشتند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 313 · <a href="https://t.me/funhiphop/74839" target="_blank">📅 12:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74838">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آمریکا به چند غول تکنولوژی چین مثل
علی‌بابا،
تنسنت،
بایت‌دنس
و
لنوو
مجوز خرید چیپ‌های پیشرفته
H200
انویدیا
رو داده؛ اقدامی که نشون میده
واشنگتن فعلاً نمی‌خواد جنگ تکنولوژی با چین بیش از حد شدید بشه.
این خبر برای
انویدیا
و کل بازار
AI
مثبته، چون هم
فروش انویدیا افزایش پیدا می‌کنه و هم شرکت‌های چینی می‌تونن مدل‌های هوش مصنوعی قوی‌تری توسعه بدن
.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 595 · <a href="https://t.me/funhiphop/74838" target="_blank">📅 12:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74836">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاخ سفید اعلام کرد در دیدار ترامپ و شی جین‌پینگ، دو طرف بر
حفظ امنیت و باز ماندن تنگه هرمز
تأکید کردند و همچنین برای
گسترش همکاری‌های اقتصادی
به توافق رسیدند
.
طبق این گزارش،
چین قرار است سرمایه‌گذاری‌های بیشتری در صنایع آمریکا انجام دهد
و در مقابل،
دسترسی شرکت‌های آمریکایی به بازار چین نیز گسترده‌تر شود
؛ موضوعی که می‌تواند روی معادلات اقتصادی و تجاری جهان تأثیر مهمی داشته باشد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/funhiphop/74836" target="_blank">📅 12:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک مقام کاخ سفید اعلام کرد
آمریکا و چین
در موضعی مشترک تأکید کردند که
ایران نباید تحت هیچ شرایطی به سلاح هسته‌ای دست پیدا کند.
این اظهارات در حالی مطرح شده که
تنش‌های سیاسی و مذاکرات
مرتبط با برنامه هسته‌ای ایران همچنان زیر ذره‌بین قدرت‌های جهانی قرار داره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/funhiphop/74835" target="_blank">📅 12:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74833">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5300919f86.mp4?token=sU9J2K61c-0267kvVwDUpO20YfgOqw9Xsl_iiFEbmIuEOy3qCLdqL9wFJEdkMim8wCxuLJIRF1kDANg5kNOWAZAmpYJSHhglRBN0CorpVJSCWnZ8Mj5UFazW9MOMVsz6tHqsEhp9LVshoHEVvRWKWGkFcDD3WB8VPT56rZnIUOXSpUh2sTamNubOTvd_KcgCBaXcPf3nKDcONHJbwDAAvt_AhG0C3wDxwYwynkZBps1HLTKV_enF77WKAvI4PspfkjmQPccW8y_Nvzsz75UNPEt5_6oIseLIvsQE-IKpMKlB-BOq87UZTfQPyQsrnPUrYwwik72O7G6U9CzmJqgCWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5300919f86.mp4?token=sU9J2K61c-0267kvVwDUpO20YfgOqw9Xsl_iiFEbmIuEOy3qCLdqL9wFJEdkMim8wCxuLJIRF1kDANg5kNOWAZAmpYJSHhglRBN0CorpVJSCWnZ8Mj5UFazW9MOMVsz6tHqsEhp9LVshoHEVvRWKWGkFcDD3WB8VPT56rZnIUOXSpUh2sTamNubOTvd_KcgCBaXcPf3nKDcONHJbwDAAvt_AhG0C3wDxwYwynkZBps1HLTKV_enF77WKAvI4PspfkjmQPccW8y_Nvzsz75UNPEt5_6oIseLIvsQE-IKpMKlB-BOq87UZTfQPyQsrnPUrYwwik72O7G6U9CzmJqgCWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با نحوه دست دادن همیشگی خودش خواست شی رئیس جمهور چین رو به سمت خودش بکشه ولی شی خیلی محکم سرجاش واستاده بود و ترامپ موفق نشد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/funhiphop/74833" target="_blank">📅 12:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هاردن چه مادری از دیترویت گاییده</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/funhiphop/74829" target="_blank">📅 12:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryFgPN6JFs0bg_ANd6x9lDES89GzzdkW7A5MIZsQV0CwOZJYhLwVL-kxT9dpgri_Gq7G9QyweBuRFRVSJTOwepyR0dsOMOaYdS_F6ivgrjctkvxif31iJ6PnewowxnrFzcZSZd29VT9tvbGMjxdBfU3OGszfibY_SwLpPx6FdeKzJp5Jzam1PTJwXjAF_CaRUnb3S8W0aDx4G5DJQUpPpr4oNbD8KzcUNNWJ7QqX1B-KO6HR4hjh0RZuY0F-Tyg_m1fPw51sZhN2WmNXJd-CgYxeesHkYmR1cIMjqxrJFbX2qqyEeJIxf2AGuh5koP0fXQAaoRUj8mzWHKhGwWawfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس
📵
قطعی گسترده اینترنت در ایران وارد
هفتادوششمین
روز خود شده.
این محدودیت‌ها حالا به شکل یک اینترنت
طبقاتی
اجرا می‌شود.
مدلی که در آن فقط گروهی خاص به اینترنت آزاد دسترسی دارند و بخش بزرگی از مردم عملاً از جریان آزاد اطلاعات
محروم
شده‌اند.
ساختاری که خود مقامات سال‌ها
مدعی مخالفت
با آن بودند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/funhiphop/74828" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به به  سازمان عملیات تجارت دریایی انگلیس:  گزارشی از وقوع یک حادثه در فاصله ۳۸ مایل دریایی در شمال‌شرق فجیره در امارات دریافت کردیم.  قایق های تندرو سپاه پاسداران یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند…</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/funhiphop/74827" target="_blank">📅 10:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74825">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1MwEXgLXMtSBtuHxWxbwHDtNyFU0ae3D3_qrNRoWflGsDPn49l3FwKQoplr3uBQSBHCnZrGh3RpCXhF2WRMA0tw9SkxxQKJcHV30AEXn_bs4YuTc2_F8Qi-MleavqD-PRVgjDzRH-w3sKlcnlX3tzXcRloRCGY8uTc11C-w-odsxjeb89mFZs_3bwTqef1Jjsvo0FRGyX3TgtigL6u0pciqZG20TAycpJvEHP0YSPpy95KDOfxNEmPFUdPySGYJXPDVPWqfGe9jOkJAhThVpXXwzgxkGqU8O5_4sJqwGSCG6MquEfxWgZPtgIwYLO35juRyd1i8cZeMTb8FOkYM7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به
سازمان عملیات تجارت دریایی انگلیس:
گزارشی از وقوع یک حادثه در فاصله ۳۸ مایل دریایی در شمال‌شرق فجیره در امارات دریافت کردیم.
قایق های تندرو سپاه پاسداران یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند و اکنون در حال بردن آن به سوی بنادر ایران هستند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/funhiphop/74825" target="_blank">📅 10:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74824">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDX6CsKmr2xuWTXBzQXJxxztiTTlq4UI5NumETUPh8qTtTK3WIBANWevw2mwOf_QUdUbjnGioSvXpuRdQP-5M__n5my_Vlyy_DGh1sKy5jWrgJEyiOqcddct_Kn5oXXiwHTcJzXHaWAuH03ze0mwqrAZM9GcppH0Ec9dSdVBrOSeaF2ovkBbhMml4uPNtfIO1MN90qG9gNoWrl39mAK80zLM28g_7gyYiMflKWsb0uiqqQeW4F980jYGKCQ0B1n-fAybTSUqQfJEF9jaw3Pe-V1MEIPlp14qjJ6IF9sLZngzS39oTLlMS5WUnq9hFwYSEIL61F5Oid2EPiIW0xT76A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی پسره قراره 6سال منتظر بمونه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/funhiphop/74824" target="_blank">📅 10:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74822">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حمید رسایی:
تنها دلیلی که برای تعطیلی مجلس به ذهنمون میرسه اینه که نمیخوان مجلس با نطق ها و تذکراتش تو روند مذاکرات خللی ایجاد کنه.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/funhiphop/74822" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74821">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سخنرانی دکتر عراقچی در کنفرانس بریکس: من به نمایندگی از جوانانی صحبت می‌کنم که نمی‌گذارند گرد و غبار جنگ آینده روشنشان را پاک کند، به نمایش از مردمی که تحت بمباران وحشتناک، تصمیم گرفتند استوار بایستند؛ به نمایندگی از مادران میناب که زیر غم از دست دادن فرزندانشان…</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/funhiphop/74821" target="_blank">📅 10:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74820">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سخنرانی دکتر عراقچی در کنفرانس بریکس:
من به نمایندگی از جوانانی صحبت می‌کنم که نمی‌گذارند گرد و غبار جنگ آینده روشنشان را پاک کند، به نمایش از مردمی که تحت بمباران وحشتناک، تصمیم گرفتند استوار بایستند؛ به نمایندگی از مادران میناب که زیر غم از دست دادن فرزندانشان خم نشدند.
ایران از کشورهای عضو بریکس و همه اعضای مسئول جامعه بین‌المللی می‌خواهد که به صراحت نقض قوانین بین‌المللی توسط ایالات متحده و اسرائیل را محکوم کنند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/funhiphop/74820" target="_blank">📅 10:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74819">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ و شی جینگ پینگ چه در نوشابه ای دارن برا هم باز میکنن</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/funhiphop/74819" target="_blank">📅 10:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74817">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlNnJjp-3D9LlzrLnG32hVRM0i6sVgC3lgJWzDzjozApeqZJeguS84E3ipMNvF6W6sEO8rTd7LoI9CkuMt_hyZ8llFGYCAnDRNGMoL1RKucLbC3IuLER2DrMJxrSCQyHWzINUbrczGKfQ-M589BU0ie5fbj5OzXNPI3idmK7usKbe_ZadWLDLS63G6GtIakxTw3UEDXwvp0oscPonoJVcoSuM9QqKkKc29hkxQbWQaw-PcHWvLTQmrxnzry4uPsOGxSjctTC3eWm4jxnsxEbIv2sSPO3_eUYSBumJgmBrBX-fYt86DLr_kSGRppu3LzKVyEwkqTp41SoleQUZX0qeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه معین قراره واس تیم ملی بخاطر حضور تو جامجهانی اهنگ بخونه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/74817" target="_blank">📅 03:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74816">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مارکو روبیو:
امیدوارم چین نقش فعال‌تری در متقاعد کردن ایران برای خودداری از رفتارهایش در منطقه ایفا کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/74816" target="_blank">📅 01:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74815">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoqOT8em754Dw1cC_ULCjDssi5MoaX1at_ZFxPB4-FnR6cmyQohRTiqHwEpLI39EescvoC47Kj0n6rIMC_oKB2UnV3nn8VNAcZXUdD62Cbx2pbMUSrB0BGVo2Pe63M5NU2NnbgQkgu5bibjIHdqpUC8j8bsvdvUI63RgvuOl85ZZ0SLx-wb2JBNOi7UHpP0eU9LTaRhtYpxR5L69YSg-3ksh1gNsirn6TVYUG5IPhnFXNv2zzsFv8ZjnK4V-7TBhyA2VI9bgqIBSyrRRpw8aWV5IlsbV3NFzdwigiW0IHgLn1tBa_yxx4qgp1XCXM98nFdV1hb-bLTKXMauqolOP8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز عصر دفتر نتانیاهو گفت طی جنگ ۴۰ روزه، نتانیاهو شخصا سفر مخفیانه‌ای به امارات داشته تا با رئیس امارات دیدار کنه و چند تا مقام نظامی هم تو این مدت رفتن اونجا که درمورد جنگ هماهنگی ایجاد کنن.
الان امارات کلا همه چیو تکذیب کرده گفته ما هیچ‌کس رو اینورا ندیدیم و اینا همه‌ش دروغه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/74815" target="_blank">📅 00:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74814">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مثل اینکه معین قراره واس تیم ملی بخاطر حضور تو جامجهانی اهنگ بخونه.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/74814" target="_blank">📅 00:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74813">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مثل اینکه معین قراره واس تیم ملی بخاطر حضور تو جامجهانی اهنگ بخونه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/funhiphop/74813" target="_blank">📅 00:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74812">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه بات زدیم که کاملا رایگان با رفرال گیری میتونید کانفیگ بگیرید ازش، چون جدیده کسی استارتش نداره و راحت با پخش کردنش بین دوست و آشنا و گپا میتونید چندین کانفیگ رایگان بگیرید   @SonicVPNRBot</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/74812" target="_blank">📅 00:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74811">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه بات زدیم که کاملا رایگان با رفرال گیری میتونید کانفیگ بگیرید ازش، چون جدیده کسی استارتش نداره و راحت با پخش کردنش بین دوست و آشنا و گپا میتونید چندین کانفیگ رایگان بگیرید
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/funhiphop/74811" target="_blank">📅 00:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74810">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جی‌دی ونس:
فکر می‌کنم مذاکرات با ایران درحال پیشرفته.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/funhiphop/74810" target="_blank">📅 00:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74809">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a5eb89bfd.mp4?token=TiyLK31CvbSH-CUbaz9fXXN11D_Q8q2f2REcLuYk_NeQIUi1TfLKK95SGRThgksyh8JrUH7agkyQ5ukhpLFrusQm9ElFTH9v-BUAHScW_rfgJCdoxtN_IgDSpZbBsLACJAcadCdyWo9KfHS1ODpDAag3Vug9bzoE3Twl4bS9tkHgFZ2HrDMEEA0RnIMdp7AmChhVt6wvBCJgZlH8GbQw0z-OmD1uoUeLL6QpsJrEHShV5qbahjf5tOTyCygXlSVuB2rULDqiTpwn0gMB9iEZONuXt8jg-6iIyWhVyg_gZRP81iAsAmMnhRUUBGo25yPWlnOKxmBc-pb4A56vz46wF2rlzrkTDUS_jKzZHBwc22LLW2LkfALhmx3zNUJGzthT6tAC8dpmENGt74I9x7yubR49ROaXuba48vCQ1JfgOOwuUbO1f1n-FGB2kYExvOmtosR9a2YfMzsoncAmPJU43uMOPI4K2VPeEcHKX0FmjpxRbszqvdHPUNTpL-f_UJJaZx3tfssTNaaEy583inw46wMcbIlJdQSKwPECLaOo4oDgLWHH_3alJd7WXIl_mykAM1Jz4kiXvLrGdpXhnNTk4UJih-LTjDZ1PjslihpjREId-Ukjv8dFz1UA47oUVzqZXhVF_P8duxlA1yKOVLrYpx4FtbjNSMJ4v9DGYp6F10M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a5eb89bfd.mp4?token=TiyLK31CvbSH-CUbaz9fXXN11D_Q8q2f2REcLuYk_NeQIUi1TfLKK95SGRThgksyh8JrUH7agkyQ5ukhpLFrusQm9ElFTH9v-BUAHScW_rfgJCdoxtN_IgDSpZbBsLACJAcadCdyWo9KfHS1ODpDAag3Vug9bzoE3Twl4bS9tkHgFZ2HrDMEEA0RnIMdp7AmChhVt6wvBCJgZlH8GbQw0z-OmD1uoUeLL6QpsJrEHShV5qbahjf5tOTyCygXlSVuB2rULDqiTpwn0gMB9iEZONuXt8jg-6iIyWhVyg_gZRP81iAsAmMnhRUUBGo25yPWlnOKxmBc-pb4A56vz46wF2rlzrkTDUS_jKzZHBwc22LLW2LkfALhmx3zNUJGzthT6tAC8dpmENGt74I9x7yubR49ROaXuba48vCQ1JfgOOwuUbO1f1n-FGB2kYExvOmtosR9a2YfMzsoncAmPJU43uMOPI4K2VPeEcHKX0FmjpxRbszqvdHPUNTpL-f_UJJaZx3tfssTNaaEy583inw46wMcbIlJdQSKwPECLaOo4oDgLWHH_3alJd7WXIl_mykAM1Jz4kiXvLrGdpXhnNTk4UJih-LTjDZ1PjslihpjREId-Ukjv8dFz1UA47oUVzqZXhVF_P8duxlA1yKOVLrYpx4FtbjNSMJ4v9DGYp6F10M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدرقه تیم ملی برای رفتن به آمریکا و حضور در جام‌جهانی ۲۰۲۶ با شعار مرگ بر آمریکا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/funhiphop/74809" target="_blank">📅 23:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74808">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خبر تکراری و حوصله سر بر
صدای انفجار در اربیل عراق
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/74808" target="_blank">📅 23:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74807">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رپر ایرانی از عجیب ترین موجودات تاریخه، یکیش میگه چرا از خون بچه های میناب نمیگی در صورتی که چندین هزار نفر کشته شدن و جیکش در نیومد و تخم نکرد حتی چهارتا پست بزنه واسشون، اون یکی میگه چرا از خون ریخته شده چندین هزار نفر نمیگی در صورتی که خون ۱۷۰نفر از کشته شده های میناب براش ناچیز تر از اون چند هزار نفره، جفت طرف جون کلی آدم از این مملکت شده براشون سپر بلای عقاید تخمیشون، اون یکی ادعای وطن پرستی داره ولی تخم نداره به کسی که وطنشو بیش از ۴ دهه مورد عنایت قرار داده چیزی بگه، یکی دیگه اونور میگه وطن پرسته پرچم فلسطین نمیگیره دستش ولی خایه های اسرائیل تا ناموس تو دهنشه.
اینور یارو تخم نداره به کسی که اینترنتشو قطع کرده چیزی بگه میپره به کسایی که خواهان جنگ بودن در صورتی که بود و نبود اونا فرقی نداشت و اولو آخر جنگ رخ میداد، اونور طرف میره کنسرت میزاره که کمبود درامد از استریمشو جبران کنه
خدایا کیرم تو این کشوری که مارو توش اسپان کردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/funhiphop/74807" target="_blank">📅 23:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74806">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شجاع خلیل زاده:
قهرمانی در جام جهانی سخت ولی شدنیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/74806" target="_blank">📅 22:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74803">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Waq8Ah512AEfrFVo_7H7fYGt_P2EdLKjYcnFBLr-w4PbSAYiWxkLEuxidIgEcosPUl90JIhscIFOsnZRbpzN4VbWPWl277v9szujSGWNhcbN7uQUsVn-VDtEBGmh-OcK16F1a0AZFdUXjVrja2BIBLy1jDAh9ai52SPoP2MXblqDwQsOThrco4WGYTs8lNe4qv020hUEvwyEwtKEmSVUEji4CzlOdOK5gkkRWZK9qAlFoeNi0uTX9-mf7KTCHNAqexims5QS5iDtNnPFk_yPANBJSegYpJ6bCtHyafL68rdVbd2lqkK-fVCgiu5v75TAStTk_8NnlPpaYNb09JfWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJJNK1S4TP2f9GsKeMOO255zqyBCI_niMSve2M-u9CsL2Y1LzPYhIni83va56bhXDKJoA8Hc2M5Zpf-4z90zc6rU0u_-JeQfuov63fRH3XXjYMZqjD_AUSClaUz2RmG_7WDTFpew5gyB-xmmDz56lhGjbr6BVsdiFeF607oAWWYFv2UVwZ7FHe7XLlBOPpRGwro9Ull-BhiqN0fbi2sPFfKPg8ZVavZrv8mL8ndOBqzzKM_UTiJ2HlJJHmAE9mdu-a-ZbYrCWxLlbg36fjO4E3bisCJv76MwLa4x6IbRlXZIX5IJVXm5INEGq8lzq2La7djtGUE9RpvSkVwd2fwJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1olaIJAGnY4x_XAfxMxu17TGjYIuN-6b3dvwEzSVDvDqtJRJAi5OU5AKG-8j8Pw1vz-BvUXkyXu7Q5wWB6O4RANdbDMeYgb-IdNBezD4SDGIrWruSAcwGvCwwRHtZsrT0Xwdurbe88xkhg9Og3G-rCcgL3qcgw_Lv_A2CPP25d51LvOkgt-bOP3gryirn-PlGLU7qYz-87xlfAsj2eDkqpkxP_rcu9QfhSD98TwYeV8Tg8rXS7LkhRUkny-6-6lftxQA6NFUo4iVAUbPfd_HTqCx2y1eLZVqV11H_9ss9p3SyxpXNbMnpTaNKUDdt15Kq-1ucKB_tikCHP8FtBl4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم من میدونم هم شما میدونید که قراره بزنن و امیدوارم از این وضعیت فعلی خلاص شیم
طبق اسناد از ابتدای ماه مه تاکنون، 50 هواپیمای ترابری آمریکایی وارد پایگاه‌های این کشور در خاورمیانه، به‌ویژه پایگاه موفق السلطی در اردن، شده‌اند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/74803" target="_blank">📅 22:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74802">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سوپراپلیکیشن ایتا:
امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/74802" target="_blank">📅 22:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74801">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJTvmc-YO6zuwzd0H4BHoZkQErNi-5DKpjhA358tCNQtsvQEJfi8ZU7ElZqGUfnR9smw8fCqBb1463xXYbiDL2Y5Ap7_ab5OWXjs6eNfzXBqMykm_jpkaYeKjRJaaFEVozOLEQpBWClY8nJAcXq279uGX30SgACLPhs9f4OxEDMggVPzCJU89tsPb64OuQQ0tbnfnOPoA3Qvr2t0Yd0Wb0eEgD8jUYCDl8tVq_FgrisKw6LTihmIX_ELIxy5Fwejo8-JCzEk_zQ7TBmreSikhLOJRqXQYwEK5wfC0U06O1nKD9khzlBoDO_-hX1i0bOncCo5CaNjA4kjisSq_MUG5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئالیا درگیر نیمار شدن وینی بودن، امباپه نیمار شد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/74801" target="_blank">📅 22:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74800">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 149 هزار تومان!
😈
( فقط 400 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/funhiphop/74800" target="_blank">📅 22:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74799">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 149 هزار تومان!
😈
(
فقط 400 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/funhiphop/74799" target="_blank">📅 22:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74796">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو تو جنگ 40 روزه دوبار مخفیانه به امارات سفر کرده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/74796" target="_blank">📅 21:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74795">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حاج صفی کیرم دهنت بمیر دیگه کصکش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/74795" target="_blank">📅 21:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74794">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">این جام جهانی خیلی جالبه
طرفدار های حکومت بازیو لایو تو تجمعات شبانه میبینن
از اونطرف ایرانی های مقیم آمریکا هم با پرچم شیر و خورشید میرن استادیوم
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/74794" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74793">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">امیدوارم تو جام جهانی کسی برای بازی های تیم جمهوری اسلامی فاز وطن پرستی نگیره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/funhiphop/74793" target="_blank">📅 21:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74792">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">داداش من خودم رضا پهلوی‌ام
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/funhiphop/74792" target="_blank">📅 21:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74791">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رویترز:
عربستان و کویت درجریان جنگ ۴۰ روزه به هدف‌های شبه‌نظامی‌های طرفدار ایران تو عراق (حشدالشعبی) حمله کردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/74791" target="_blank">📅 21:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74790">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سنای آمریکا بار دیگر طرح محدودسازی اختیارات جنگی دونالد ترامپ در برابر جمهوری اسلامی ایران را
رد کرد
.
تصمیمی که نشان می‌دهد این لایحه نتوانست
حمایت کافی
را به دست آورد و عملاً به پایان مسیر سیاسی خود رسید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/funhiphop/74790" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9tJ8d0mI1y4rgHRnO8FoiIbiyYC-puo2fRea8ySWFDLv9hQnCouKBM5DUYtl7s3O53_9tu4s-ejqbKqk6GTDMhOfX1HpEKv5P9IsL3mM50cC5VxM1EvilNHoDRnCiMm74C5PVWSdNBNzOFUxqmqVFmmQFnjmhkSKIOktipTh0_riZi_tTtKOKCn2w-8ew-MCvN-ZT8TNQectllRh8x4-22FPdlxQemM8Hpy0ptZC3xXJGtMYziXtKlQ7ofAPF7_6c4fcZ9qM59-4ZBjiOVO45xH_-ddbli0Yox20edF_J3Nyb9ykVLXjGjcWhbycmq-vaa8Q3mRxka0BMDd04L4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دیگه شب بخیر
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/74789" target="_blank">📅 20:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMhxqPnyIV7mFtLfUz06iIL5nq1I0_eS7CNhjvgNYEc0cyVA41mQrIXwL8ulnVrwonbEeJD0xIV2PgR72GJTOJprtCXu1uYJ1Ur2A-ASjtAdQrbLL7flj5Me67O1NE02rpVDUfUu4bnA0Cr4jkB1mmx6Ljdwh3YA-zdBazspF-n5lsW9lOVuak4NMfpZFIpOTqpQ4BTKnUULC5vQ8K-Ub-Q7Dexm0R_OmIgKrStukmvKynSJPwhJV8gpW3iYzAaDvzgEKiSvqVWrdgw-pbBf9FLJpiwq3mlbeRp8txDNdD1nEhE2VDCwnj2P-IYsxeC7EO1ranie7JeQUfg-kuNjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره خبری که منتظرش بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/funhiphop/74788" target="_blank">📅 19:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فون برند
🔝
فقط با برند میتونی آفرای ویژه ببینی
🛠
🔵
سرویس های V2ray    1G
➡️
230,000   2G
➡️
460,000   3G
➡️
990,000   5G
➡️
1,150,000 10G
➡️
2,300,000 15G
➡️
3,450,000
🟠
سرویس های open و L2tp     5G
➡️
1,533,000 10G
➡️
2,830,000   با برند، یه کیفیت برند رو تجربه…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/funhiphop/74787" target="_blank">📅 19:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMilbFakx51XTw-OlUgiel5ZyxBwJn8DST8SMp-A2xSmD5OW1qiO5yeG4PV1GjpfQHXp0RUb3tuqJsrvHtKwQvMgm40MSU86FKHhq2cl2lQGg5H-A4MrlfZX2_9xBVYZbDXoKgjKBfGhApnctZRTW51cTDJR0Vnh1Ql-FK3SznWAzYnZskyoIUbmZ5WyKvXZOAaeP3IphmHnVqyhqCzPkPuiePN1SB7eFW-u3YfN4Ibon1dyduJfH_a-1mYb2UnpR9CCloNQgL9sFQ9M1GGA61PhmW48rIPwUR3h8hUkOaIY6fbxYAWxY6Q2wqkOwXPGSRnsX8aX-deWX2Cb6TBAsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فون برند
🔝
فقط با برند میتونی آفرای ویژه ببینی
🛠
🔵
سرویس های V2ray
1G
➡️
230,000
2G
➡️
460,000
3G
➡️
990,000
5G
➡️
1,150,000
10G
➡️
2,300,000
15G
➡️
3,450,000
🟠
سرویس های open و L2tp
5G
➡️
1,533,000
10G
➡️
2,830,000
با برند، یه کیفیت برند رو تجربه کن
🦅
@phonebrand13
✅
@phonebrand_support
✅</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/74786" target="_blank">📅 19:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پدر احسان افراشته (جوانی که امروز به اتهام جاسوسی برای اسرائیل اعدام شد) با شنیدن خبر اعدام فرزندش سکته قلبی کرد و در گذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/funhiphop/74785" target="_blank">📅 18:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">روزنامه های فرانسوی مدعی شدن گلشیفته فراهانی و امانوئل مکرون رل زدن برا همین کله زن مکرون ازش کیری بوده  این اولین باری نیست که این شایعه پخش شده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/74784" target="_blank">📅 18:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">روزنامه های فرانسوی مدعی شدن گلشیفته فراهانی و امانوئل مکرون رل زدن برا همین کله زن مکرون ازش کیری بوده
این اولین باری نیست که این شایعه پخش شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/funhiphop/74783" target="_blank">📅 18:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/530c2c0a1f.mp4?token=Mpivqe9TimKgN3172anhfDpiFXagONP45Ns32YHA3CbP6k1H_AeVtRDHwldCnEbUSGpl0pf6vDeJf5wybUdYY6Jmyxg1Qjj7-HpRS_4FwkiX-MPaOJZJFK6gRfP-P9sJmS3LOKay_ueMh8OpVdplwBrstJOoCaIwRZ8LCeczNDv51_cV-CtnuC3EwCJcfK1TMzYncspVrq4rA8OR_GRJEqdL6aEiH3Qooa8p_Qhpq2FSEKXoOAH-FX4hYEPFhYQ8mIIe76addjNdT2D-PQDSJwXHyrN820mbJV-NSlS7QneunWDx3FdX96PhQuI7d0N0CqyBpKJad7mt69qcCcZTsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/530c2c0a1f.mp4?token=Mpivqe9TimKgN3172anhfDpiFXagONP45Ns32YHA3CbP6k1H_AeVtRDHwldCnEbUSGpl0pf6vDeJf5wybUdYY6Jmyxg1Qjj7-HpRS_4FwkiX-MPaOJZJFK6gRfP-P9sJmS3LOKay_ueMh8OpVdplwBrstJOoCaIwRZ8LCeczNDv51_cV-CtnuC3EwCJcfK1TMzYncspVrq4rA8OR_GRJEqdL6aEiH3Qooa8p_Qhpq2FSEKXoOAH-FX4hYEPFhYQ8mIIe76addjNdT2D-PQDSJwXHyrN820mbJV-NSlS7QneunWDx3FdX96PhQuI7d0N0CqyBpKJad7mt69qcCcZTsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز خیلی عجیب و خیلی سنگین دارن به جنوب لبنان اتک میزنن
جنوب لبنان تبدیل به یک مکان آخرالزمانی شده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/funhiphop/74782" target="_blank">📅 16:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b397b8f97.mp4?token=dd37Wg94kRBXlvyeJbzUBQdy5boWarhnZ3Xa0S2o0FdZvcQDtOYjIaOBKgf5lY9gdkDwfhKxRHSQuSuxbslxQT99lHVTUzjSQWKiFcT4Z_mzwJ1ebDa0qP59baosB8yUXY3JNcbErBQzthX80uL1l2aLOSY4vH77rk6lzlkNjz9wYJiThIjCvgtaqJzhD5ubjNJ8N_YjA8UkvoKiFZub_MmlYTgk8OfLSO9cByuioDBmz9a-3n2EyTmZlTtFqmhWfQUPsnZrnrssbzT6dvbrMXuBQQvsLkWhjPR9v2c9E4tB-_V4AtQxeJHQllyog9sOqOY80f99LecCHo1veZZb2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b397b8f97.mp4?token=dd37Wg94kRBXlvyeJbzUBQdy5boWarhnZ3Xa0S2o0FdZvcQDtOYjIaOBKgf5lY9gdkDwfhKxRHSQuSuxbslxQT99lHVTUzjSQWKiFcT4Z_mzwJ1ebDa0qP59baosB8yUXY3JNcbErBQzthX80uL1l2aLOSY4vH77rk6lzlkNjz9wYJiThIjCvgtaqJzhD5ubjNJ8N_YjA8UkvoKiFZub_MmlYTgk8OfLSO9cByuioDBmz9a-3n2EyTmZlTtFqmhWfQUPsnZrnrssbzT6dvbrMXuBQQvsLkWhjPR9v2c9E4tB-_V4AtQxeJHQllyog9sOqOY80f99LecCHo1veZZb2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/funhiphop/74781" target="_blank">📅 16:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74780">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISO-T0StdMlnqIe8YzcDGf3qGfooZ_NHshIhBCbvs61Lm61S_1mQfSkDkZGXK8CMF8IzrUYusewyenhWaslplBRSFuXzeJK8zgykZslclGFch9svdjTkLkF2Y5U6UDMuXd2Dki0sgbN9Fk4zZjtT1stEkmThXDAzndnDaQq4bdseYT0nNs6JgdWM1-kS6qO1KCewaBmonLB5rAfnFQDglCr-ri5UKQOYuHjz_tJLoZgVryJKR2jREfAgbDfqwNsSpnecq7hSVB2w6a1ssVvO8W3sxknjBz69EdVyW4oK0Ylk4QRM0jM-r8af6Jb_1p5xWNuGrjTn_UMZa9QGnHb1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید نقطه زن هواپیما رو با موشک بزن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/funhiphop/74780" target="_blank">📅 15:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMMd</strong></div>
<div class="tg-text">ژنرال رضایی وقتشه آمریکارو تصرف کنیم تا خالیه</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/funhiphop/74779" target="_blank">📅 15:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74777">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ریاست جمهوری آمریکا پس از
11 سال
وارد خاک چین شد.
ترامپ به همراه غول های اقتصادی ایالات متحده آمریکا و همچنین کابینه دولتی خودش
هم اکنون وارد چین شدن
.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/funhiphop/74777" target="_blank">📅 15:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74776">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این خبر نمایندگی اپل تو افغانستان هم فیک بود
ظاهرا یک نفر با خلاقیت بالایی که داشته یک نمونه مشابهشو ایجاد کرده
این شخص هم افغانی بوده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/funhiphop/74776" target="_blank">📅 15:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDeRBELNveFQydKQJCNKPxrZBMGZyl3G7CC47NhGkXA6YvjIKy3pX_prOvDZObqsPlh3jbT4Wqi1VB0aMIkezOYSetoBTsv4C0Lzhw_6XJmEU4Jtiksbo9eOnkVXtdXFQ8YpM3Co1-zHYCD5lV6KIQuv9Tt64AMHglFldDshcrgxK2sKLChxr3hX-Awl9ggbahzwQ3JAQOmnItHOscKjETqpcO3QETD5VMZteJMcMqP73aj2khujyGOYI_wXKKoMJ3d1t7f9wfC_PDn0vyLX904t1p2U-dtyfOfCVbjytzDX8l_S7kiZs-5LzHP_BH6Gbyw1t6bPNQuFoIaiXAq0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان رو سفت بچسبید
بر اساس ادعای خبرگزاری ترکیه ای ویروس هانتا باعث کوچک شدن آلت تناسلی مردانه تا 6 سانت میشه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/funhiphop/74774" target="_blank">📅 14:28 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74773">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411849ba8d.mp4?token=ns6s009qXMzaB6z6HDy61jeaFStiKEqgzhtAUb4VDjHQquFvfQ1zxGgMdYBCiYp1lk_AtS9ayY_qfwnDOqkmGT1lMiq6qOu6Khn0ErZmJQ4f6Qfd4UTmjKDYzuqOkut3aALG0IfG27KjUPUdZP_HyMK6n0cOpmOl1voojdygr0jSJ8y-qN33I4vJhUddbkCPKUNjMav2DEJY8TnLchXIVpGUEQLqOiDpXJOj69oyLauJN2v5eTuejRk021cy8u11YshOROoemS46-DfEwCs81HHDWXfmA2DyRrE8MPexilh_wiDhwknNiqwGt7xka76ArS_OCGcXnV06Z7tALGrwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411849ba8d.mp4?token=ns6s009qXMzaB6z6HDy61jeaFStiKEqgzhtAUb4VDjHQquFvfQ1zxGgMdYBCiYp1lk_AtS9ayY_qfwnDOqkmGT1lMiq6qOu6Khn0ErZmJQ4f6Qfd4UTmjKDYzuqOkut3aALG0IfG27KjUPUdZP_HyMK6n0cOpmOl1voojdygr0jSJ8y-qN33I4vJhUddbkCPKUNjMav2DEJY8TnLchXIVpGUEQLqOiDpXJOj69oyLauJN2v5eTuejRk021cy8u11YshOROoemS46-DfEwCs81HHDWXfmA2DyRrE8MPexilh_wiDhwknNiqwGt7xka76ArS_OCGcXnV06Z7tALGrwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/funhiphop/74773" target="_blank">📅 13:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74772">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کصخلا زمان شاه همین اینترنت الانم نداشتن ملت  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/funhiphop/74772" target="_blank">📅 13:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74771">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کصخلا زمان شاه همین اینترنت الانم نداشتن ملت
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/funhiphop/74771" target="_blank">📅 13:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74770">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">معاون ارتباطات شرکت مخابرات ایران:
اینترنت بین‌الملل نباید با همان قیمت اینترنت ملی عرضه شود.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/74770" target="_blank">📅 13:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74769">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فرق میرا و گراک مثل فرق اونیه که مدرسه غیرانتفاعی درس خونده با اونی که مدرسه دولتی درس خونده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/74769" target="_blank">📅 12:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74761">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmahdi</strong></div>
<div class="tg-text">فک کن ایران صعود کنه به یه طریقی بخوره به پرتغال پرتغالو حذف کنه
بشاشه تو جام جهانی گرفتن رونالدو</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/funhiphop/74761" target="_blank">📅 11:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74760">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ایران ب تو کدوم گروه جام جهانی افتاد</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/funhiphop/74760" target="_blank">📅 10:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74756">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpHvAiIIG79WDljEq-gVRMNluaEz1ytEcbnYne5GWBv6dT9zR7rAny8EAmoiKCszXaYDKMVByg3SmlyVP1xLUPe7GpFFAt1NBN_vKUzsTll48LHSgmigLy6SR0kLLMWc_NIWJ9xwa9cdIM5E5b8l73n7WaB_IyanIl68__YGbOYqXlz50NBuXmcmIIeVRW57zLhpSDA2253GgD4cyazL5STP6TCW3PVtNTrbttpJ8XqxhlUb6L8rRvE4gJC4NJPXUD4tj3oEKyarorm5FSIAisDmPkFtEeJ2v5cs177w0aOeytKfVMlYHmMoA3B77ZH7N829zm4XAss9HS7vjPVEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسشر ترین توییتای قرن همش مال ترامپه میگی نه توییت بعدیشو ببین
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/funhiphop/74756" target="_blank">📅 03:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74754">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDMNSWXC4oe3BYD0vafzIPrdqFMNBze536gis6vbhHYa7OreBuE7CLoi0P0jfTtVXXdnVpM6LUMrrpYot_4ip_5Q4nyTXw6OMSLLmG7Xj9Qr97qDu0BC3cnXUpQq_2FNL_RuhecOCmSTOrPJrYls1zv9vnGl6Jl09RVvdtUg8hdk_RBhslmOHrXTjU6PnCvEBtYLfRia7eTSxjQVnG7r95VlSS7Xmu2Nb5UfdadZHeuDOwakbvtdYrZEiwNXKYQNroEAAMsGRxhQrSpjMUeEmkmLtNOYTILN9fUcdcDlmRiduwYhpWKmLAY8EEgNM1L4ZONx0eM4WBBt2Pgp6lGmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPozDgl8JQxEgzdVfrYUJy6LznnkvfLlcToi4KUiPSPAotVadLH20WK7-I9DcpYJVEeX1z6KnXNdcXlN9u9gaNIjo6MbyFrLOKfQfyXBi37wjlK9eMPiB34jy75bgJo4lVVIXc0iwlGeNhOEnboijcXlv_ssbgVQCVJYXtfoeij_Ju515VKamjxus0YJxlJ-WAMGV9IKcPMw6plhrFeUlX3TWM9wD0wNcfIEJFaeJlHm2RqcwPqI2opL8tGjZxwtSnXlkwsTLNMP1VNb0aoBSc8h0HSrGYmfxyPpBFpQAcA6CA8geV6lNkq0DFCuluMha8_kPJQ8dGCRaxMiYTy3Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو تو هواپیمایی که باهاش دارن به چین سفر می‌کنن لباس معروف مادورو موقع دستگیر شدن رو پوشیده که احتمالا داره به رئیس جمهور چین تیکه می‌ندازه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/74754" target="_blank">📅 02:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74753">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اسماعیل بقایی در ادامه: آنها می‌گویند ما قلدریم؛ درحالیکه ایران ثابت کرده است که قدرتی مسئول در منطقه است و در عین حال قدرتی ضد قلدر است. ما قلدر نیستیم؛ ما ضد قلدر هستیم. فقط به اقدامات ما و آنها نگاه کنید. آیا ما کسانی بودیم که هزاران مایل دورتر به آمریکا…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/74753" target="_blank">📅 01:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74752">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هم اکنون؛ تهران زیر رعد و برق شدید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/74752" target="_blank">📅 01:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74751">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه‌های عبری:
آمریکا در جریان جنگ ۴۰ روزه با ایران، ۱۳۰۰ فروند موشک پاتریوت مصرف کرده است. هر موشک پاتریوت بین ۴ تا ۴.۵ میلیون دلار هزینه دارد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/funhiphop/74751" target="_blank">📅 01:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74750">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBdnE4xvanqmsJg_uoxXZsBHd_wlOuEBOgCTrbj2hTbeKl0uYAalZGvNbHTdx33CUT-jturt8S--VfZmMKgC01m05FrFliOXmjx6lZhp2wEZ9I955TS69uSof1wRrJpONt-kNVeBTQxVBMgXhKOl4Fpd6qkzA2oBMbGDyAfOwekB3O8HJROb6G5DFRHaZEfUQJBK2clDSThAI1pIh9re6LhnIVujfWXbnVyAtSgU9MX9-pyQpCzjJHkqIZQRbvV87J6Md-HOPVMaTIXzEFoQhQCLLPbM9-qC1QjS9Jo90HUIejx3ctYbo2quAlQLcsZu_S3seY2Wznoc7hrL1navow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هم اکنون کوین ترامپ
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/funhiphop/74750" target="_blank">📅 01:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74749">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تو هرچی کم داشته باشیم تو موشک کم نداریم انگاری
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/funhiphop/74749" target="_blank">📅 01:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74748">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیویورک تایمز به نقل از سازمان‌های اطلاعاتی: ایران به اکثریت سایت‌های موشکی و پرتاب خود دسترسی پیدا کرده و گزارش شده که ۹۰٪ از آن‌ها عملیاتی هستند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/74748" target="_blank">📅 01:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74747">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیویورک تایمز به نقل از سازمان‌های اطلاعاتی:
ایران به اکثریت سایت‌های موشکی و پرتاب خود دسترسی پیدا کرده و گزارش شده که ۹۰٪ از آن‌ها عملیاتی هستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/74747" target="_blank">📅 01:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74744">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هواپیمایی قطر:
بارها آقای سعید جلیلی از گیت می‌خواسته رد شه و هی دستگاه صدا می‌داده
میپرسیدیم چیزی تو شکمتونه؟
می‌گفته دستگاه خرابه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/74744" target="_blank">📅 00:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74743">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جلیلی سیستم گوارشش بهم ریخته</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/74743" target="_blank">📅 00:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74742">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">درسته بحث بحث وطنه ولی تهران لرزید باز
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/74742" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74741">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">داداش من خودم زلزله هستم ولی الان بحث، بحث وطنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/74741" target="_blank">📅 00:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74740">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رای قلعه نویی برای توپ طلا مشخص شد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/funhiphop/74740" target="_blank">📅 00:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74739">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سعيد جليلى: ‏من حاضرم 200 كيلو اورانيوم را لقمه لقمه بخورم ولى دست دشمن ندم.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/74739" target="_blank">📅 00:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74738">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جوری داریم یه زلزله ساده رو پوشش میدیم انگار زیر بمب اتمیم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/74738" target="_blank">📅 00:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74737">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش مقدماتی زمین‌لرزه
بزرگی: ۴.۶ ریشتر
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/74737" target="_blank">📅 00:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74736">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">من کانفیگم قطع بود الان لرزیدم</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/funhiphop/74736" target="_blank">📅 00:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74735">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">میگم تشعشعات رادیواکتیو از تل‌اویو به ایران میرسه؟
@FunHipHop
| Ali</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/74735" target="_blank">📅 00:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74732">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سفت بچسبید که نزدیکی شمال از سمت تهران هم ۴.۶ ریشتر زازله اومد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/74732" target="_blank">📅 00:00 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74731">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تهران لرزید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/funhiphop/74731" target="_blank">📅 23:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74730">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تهران لرزید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/funhiphop/74730" target="_blank">📅 23:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74729">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تهران لرزید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/funhiphop/74729" target="_blank">📅 23:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74728">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تهران لرزید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/74728" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74727">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تهران لرزید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/funhiphop/74727" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74726">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj7LM6Ng8Husl_qPZPB0gHIzKZL3Xe3OW-76dcDZonZhcn1os2upVybgeQGPkpZRKjM8iZhKY05WyfFOT12mPgZ6LM0q9ox41LAOSflGpm6h5yixf9mbkM1AOEGZ1MeCOR6xI9g-tOJAhNLsdi9sibO2vzRa081GevjtJvFFlcmjG1MpfuCEvcIkAoyrlTF8bSKos8mroiKvb2uB3hL2UDtwA7n1ibsjjeWrFnXi6rv7tazZQJZO7lw46idorVzs1cFAMxPUxX9wKTbRgXpW9UcP3i-MKzwdsDIV65w8OMh9y1d1i8Aqj_xEWu8rKk9d98cFt95R1EEmZna6kzkIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنتو زنت گاییدست
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/funhiphop/74726" target="_blank">📅 23:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74725">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e19475e71.mp4?token=IQQm_XUIQ4MZSS9v_nDaghdE5HfScxfvtIcakwSHOioDtvxxn8CjL7KbEPEMkyFAiXyhx2V20HK15RDh1T1w05x9-mVO6DlkSzz4KUgDwLunywwNRbffa5yGD0RAFfsLfJ8Qkmy5E465l3WMkAO_1ZZs5WWSEY1BTIHw0Ixis5SZUE8wD3ljrpmvZmWqnvuSP3lpUtV3zEK3p0qMP4tpnGUoygGokt4inDNliaI42wW7mnGBF868Sdtxese4pSkmfXE3hi2vd07e_PKMjCrDqz2ArzJkT3t9XuOXzaLrkCSKCl45gmSwWAlQlRdq_hGsMJx8e66p4-tOWLP8qoLoOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e19475e71.mp4?token=IQQm_XUIQ4MZSS9v_nDaghdE5HfScxfvtIcakwSHOioDtvxxn8CjL7KbEPEMkyFAiXyhx2V20HK15RDh1T1w05x9-mVO6DlkSzz4KUgDwLunywwNRbffa5yGD0RAFfsLfJ8Qkmy5E465l3WMkAO_1ZZs5WWSEY1BTIHw0Ixis5SZUE8wD3ljrpmvZmWqnvuSP3lpUtV3zEK3p0qMP4tpnGUoygGokt4inDNliaI42wW7mnGBF868Sdtxese4pSkmfXE3hi2vd07e_PKMjCrDqz2ArzJkT3t9XuOXzaLrkCSKCl45gmSwWAlQlRdq_hGsMJx8e66p4-tOWLP8qoLoOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممممم  آمریکا با بالگرد اومده تو خاک ایران خلبانشون که افتاده بود رو برداره ببره  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/funhiphop/74725" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74724">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjAaFRn-N2woKs_cKQC0D-dtlulgM8214NhQ0fit30uibo0QFde_KbWPPJUUG4reCnbDExEPP5mnepb9hrx4iOKzjjo4tpjoPymILrvU1b3nqVfqvoPi198QhHmIT2pZHDlj-bi6ro4ecLeMFmuswPcaU3ZI_jEY2Er1ebqBaoZ2I2PPzyPB2SbHjuGS8uSKxuPE1iXOu9CuNaxB_cl7Y4kz0G5t-PQe4yjw9XXuq0CCWpFVYChXJ5GI-GHLI4pO26vA4SVWr0GPcTyGs4g8t6yA_hTf8U-ARy4gdUHrt36K1lwiJ0_nJX2N-H9Kut8JhEnzWNY-Ny4VEjJIfkbBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/74724" target="_blank">📅 23:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">😑
حلقه قدرت ترامپ در چین
ایلان ماسک — مدیرعامل تسلا و اسپیس‌ایکس
تیم کوک — مدیرعامل اپل
لری فینک — مدیرعامل بلک‌راک
کلی اورتبرگ — مدیرعامل بوئینگ
استیون شوارتزمن — مدیرعامل بلک‌استون
برایان سایکس — مدیرعامل کارگیل
جین فریزر — مدیرعامل سیتی‌گروپ
جیم اندرسون — مدیرعامل شرکت Coherent
اچ. لارنس کالپ — مدیرعامل جنرال الکتریک هوافضا (GE Aerospace)
دیوید سولومون — مدیرعامل گلدمن ساکس
یاکوب تایسن — مدیرعامل شرکت Illumina
مایکل میباخ — مدیرعامل مسترکارت
دینا پاول مک‌کورمیک — معاون و مدیر ارشد سابق گلدمن ساکس و مقام پیشین کاخ سفید
سانجای مهروترا — مدیرعامل مایکرون تکنولوژی
کریستیانو آمون — مدیرعامل کوالکام
رایان مک‌اینرنی — مدیرعامل ویزا
⛔️
آمریکا غول‌های اقتصادشو برده چین؛ یعنی ابرقدرتا مستقیم دارن روی آینده دنیا معامله می‌کنن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/74723" target="_blank">📅 23:09 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74722">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جمهوری اسلامی عزیز، خشم و انتقام حماسی به شدت خفن تر و قوی تر و شیک تره
باور کنید نیاز نیست برید مزرعه دار شید داس بگیرید دستتون، یا چکش بگیرید دستتون میخ بکوبید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/74722" target="_blank">📅 22:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74721">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e71g_e5pdhi9-pdLzCpzbfFTJZhgCZoMzEy_6XvakRJSUXR4URmNeON2xumpktclcPbq3UOXXedp-_vCW6tD7arRaJgQlFkVgap3DLcYcguMR3Sax06M6quJZDEgbzGXw_emuEz1jb0RdLP7L1GYUB4-1Vx2XNGGUfkISPvRt2NYMLWmpyBBISfwNft1NYhtAEi5BXNybF0XcK4_FeSJDApRyMyVhOeaPlL3bmXHS6GF0oD42njXlfr2BEJyL8fVuhhVc5obGxJxNGwEkmlnopugwQAto_tMf-9rpis1YDHxTt3QwOJwOywhY3JBudo4NX0vaSm0qX9_fjKWruvRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">NBC News:
ارتش ایالات متحده در نظر دارد در صورت فروپاشی آتش‌بس و تصمیم رئیس‌جمهور ترامپ برای از سرگیری عملیات‌های عمده رزمی، نام درگیری خود با ایران را به «عملیات چکش سنگین» تغییر دهد و این جایگزین نام قبلی «عملیات خشم حماسی» خواهد شد.
این تغییر نام همچنین به دولت اجازه می‌دهد تا ساعت مجوز ۶۰ روزه کنگره تحت قانون اختیارات جنگ ۱۹۷۳ را به طور مؤثری از نو راه‌اندازی کند، زیرا کاخ سفید استدلال خواهد کرد که این یک عملیات جدید است.
ترامپ هنوز دستور از سرگیری خصومت‌ها را صادر نکرده است، با این حال مقامات اشاره کرده‌اند که محاصره جاری در حال حاضر اهرمی فراهم می‌کند بدون نیاز به اقدام نظامی عمده، اگرچه
یک مقام هشدار داده است که «وضعیت موجود پایدار نخواهد ماند.»
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/74721" target="_blank">📅 22:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74720">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اگه مادرجنده باشی ایران بهترین جا برا زندگیه پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/74720" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74719">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایلان ماسکم با ترامپ میره چین
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/funhiphop/74719" target="_blank">📅 22:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74718">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99d9c3f71.mp4?token=WLSgz-1Fd1fCS7ETqHdoit8XHtO5ZL8EOeOGDYZIVVgcEV-TojG91XSu9sVoZgi_5PoTuu1PJLVeR3rBKIRHCGZSlght78NFcA8R9vTvdGTzCCAgyKSA4VjAuOcko66Eixq2IdchQ2O9p73c0GdubrLOedJwsMjTc-St4YQE8SuvPlVoiXXni_R3JrITnoi-mwCXNsu4qJqZ2_QgQcI7KeHNAhtSOzvEUUSAEtXkteaZCypieQqCAokRRQqcERWi_qc2rzo2KxqZ7foz9s-9wMFziqgAfQuS_X24Ig0GwrkI6oMIlHtcr-3p1Q9N3Lf2KVlfIS4qLTVRjXJFhj5hQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99d9c3f71.mp4?token=WLSgz-1Fd1fCS7ETqHdoit8XHtO5ZL8EOeOGDYZIVVgcEV-TojG91XSu9sVoZgi_5PoTuu1PJLVeR3rBKIRHCGZSlght78NFcA8R9vTvdGTzCCAgyKSA4VjAuOcko66Eixq2IdchQ2O9p73c0GdubrLOedJwsMjTc-St4YQE8SuvPlVoiXXni_R3JrITnoi-mwCXNsu4qJqZ2_QgQcI7KeHNAhtSOzvEUUSAEtXkteaZCypieQqCAokRRQqcERWi_qc2rzo2KxqZ7foz9s-9wMFziqgAfQuS_X24Ig0GwrkI6oMIlHtcr-3p1Q9N3Lf2KVlfIS4qLTVRjXJFhj5hQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ما ایران را کاملاً تحت کنترل داریم.
یا یک توافق خواهیم کرد، یا آنها نابود خواهند شد. به هر حال، ما پیروز می‌شویم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/funhiphop/74718" target="_blank">📅 21:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74717">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f5582997.mp4?token=utztAHUVJPclOBlmRjmExUV2sSkjAHOXOT2qNMLR73caUB1ti1VFkp0tsIHrF_7vYHCs6-o39IkJucIFqduwwBo0EfxQVd5AmwiysHVNeY5oZxd5TsS39LQ0Zw-gICBm61W9dNef1HfsnCD4BxIuwV0IcO2R2H3LA6QcjuZv4CzhRm3IqoWrphaNy4vnMvIuWHgZvF6oLQZEuSy_uzxkD2Xs_torDebAmRPLt36dVO75y6PcdAIttfDQiM8do4hhthxDnEeBMQ6FdheabE7b_ylAuZ5m8a1Raqhzj-yaHWszjRrgmVHamZ8r8dUs5uPExNcZ2b0QG_6XDDMaaQ_skA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f5582997.mp4?token=utztAHUVJPclOBlmRjmExUV2sSkjAHOXOT2qNMLR73caUB1ti1VFkp0tsIHrF_7vYHCs6-o39IkJucIFqduwwBo0EfxQVd5AmwiysHVNeY5oZxd5TsS39LQ0Zw-gICBm61W9dNef1HfsnCD4BxIuwV0IcO2R2H3LA6QcjuZv4CzhRm3IqoWrphaNy4vnMvIuWHgZvF6oLQZEuSy_uzxkD2Xs_torDebAmRPLt36dVO75y6PcdAIttfDQiM8do4hhthxDnEeBMQ6FdheabE7b_ylAuZ5m8a1Raqhzj-yaHWszjRrgmVHamZ8r8dUs5uPExNcZ2b0QG_6XDDMaaQ_skA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
رهبران ایران یا کار درست را انجام خواهند داد، یا ما کار را تمام خواهیم کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/funhiphop/74717" target="_blank">📅 21:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74711">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رضا پهلوی: هر زمان که مردم توان مقابله داشته باشن، فراخوان خواهیم داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/74711" target="_blank">📅 20:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74710">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
انتظار می‌رود ترامپ پس از بازگشت از چین در پایان هفته، تصمیمات نهایی درباره ایران را اتخاذ کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/funhiphop/74710" target="_blank">📅 20:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74709">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انگلیس:
ما در مأموریتی چندملیتی برای تأمین امنیت تنگه هرمز، با ناوگان هواپیماهای بدون سرنشین، جنگنده‌ها و یک ناو جنگی مشارکت خواهیم کرد.
مأموریت تنگه هرمز چندملیتی، دفاعی و مستقل خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/funhiphop/74709" target="_blank">📅 20:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74708">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الجزیره:
رهبری ایران پنج شرط را برای آمریکا تعیین کرده است که باید قبل از ورود به مذاکرات پرونده هسته‌ای برآورده شوند:
— پایان دادن به جنگ در همه جبهه‌ها (خصوصا لبنان)
— رفع همه تحریم‌ها
— آزادسازی همه‌ی دارایی‌های مسدود شده
— جبران خسارات و زیان‌های جنگ
— به رسمیت شناختن حق حاکمیت ایران بر تنگه هرمز
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/funhiphop/74708" target="_blank">📅 20:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74707">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شاهین نجفی هزار پدر حداقل آنبلاک کن بتونم بیام پیویت بگم کیرم تو کنسرتی که گذاشتی</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/funhiphop/74707" target="_blank">📅 20:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-74706">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMuh8dkTVCc0UZaC_nmXQ_7HtGZeakE6-kziufUTKrvMXiOqmm8PG3AjptkPIw_HXy3Fod94DUPsDtGUpNXw4agz2lpGz_9aiL8N8rjmKukNLT3N0UY7NOYm5YG1_srhMMJ1_3X2o5jDjK6gTh7WDfIg4mxxqOWKLxS0tnjButJBWYFS_I-OqL9giZGqvds8avFHklb34Pk_SEn3cohzHGlMreDulgcsK0w_793S87WzLM9niKfrmFszgc47xDy2_s0gKRWKqKvrxKLUWkRGERSzMZqsxnWj2R_JEKLAPp9zGJVQjnaQH_wQffiAnpvwXmrwdKT_hN6h6a10REwesQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس، ابراهیم رضایی:
یکی از گزینه‌های ایران در صورت حمله مجدد می‌تواند غنی‌سازی ۹۰ درصد باشد.
این موضوع را در مجلس بررسی خواهیم کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/funhiphop/74706" target="_blank">📅 19:55 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
