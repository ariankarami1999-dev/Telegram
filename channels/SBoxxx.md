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
<img src="https://cdn4.telesco.pe/file/WU6BpnzJYukzp2zzjJTQE0Pe3Lisl0capAPMOHOYSMzCXTWTgoCetx5HslCwz09o7BrpZlAtryWTwFuE4y5SaJVDHXfMNF6QwzfgDZeIcZ2fmBDJMnuG4KEn8OA7Ot-bNBTTcxHLCuElcVH1b1onk5w6_pgEJ-y-PPGKYBBMJhczm-kSvlPhTXhfgxf5xAVRur3-4att_Qa3JFs_7UzqnQAKQxYhKugbjLu3Qemon35ZQNB8-OSjztq3a4mo6TF4hWKqU9I6s9SCfUh-8J2ESqo5ZzAtHESXHO8Tp9gXyEVe8WmbRnbyhfbrUs8PW8rUSPhY7fw38lMDDia4t9xOXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 15:23:35</div>
<hr>

<div class="tg-post" id="msg-19608">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:  در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.  گزینه‌های نظامی واقع‌بینانه در نظر گرفته…</div>
<div class="tg-footer">👁️ 632 · <a href="https://t.me/SBoxxx/19608" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19607">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:
در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.
گزینه‌های نظامی واقع‌بینانه در نظر گرفته نمی‌شدند. رویکرد غالب، آشتی با رژیم بود. اگرچه بسیاری از سیاستمداران ترکیه در کارآمدی آشتی تردید داشتند، اما این مسیر در حال پیگیری بود.
ترکها همچنین می‌ترسیدند که اگر یک تهاجم نظامی شکست بخورد، روسیه با حملات هوایی گسترده به مناطق تحت کنترل مخالفان پاسخ دهد و موج دیگری از پناهندگان را به ترکیه که خود با بحران پناهندگی روبرو بود، وارد کند.
حتی کشورهای عربی - به جز قطر - در حال پیگیری عادی‌سازی روابط با رژیم بودند. هدف تأیید آنچه اسد انجام داده بود نبود، بلکه دور کردن سوریه از نفوذ ایران و کاهش خسارتی بود که به منطقه وارد می‌کرد.
عملیات نظامی با وجود آن نگرانی‌ها آغاز شد. این کاملاً تصمیم خودمان بود.
منبع: الجزیره</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/SBoxxx/19607" target="_blank">📅 15:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19606">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 17</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 17
دوشنبه 3 آگوست 2026</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/SBoxxx/19606" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19605">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIh6rHP5rCsBMgVjo8r6jSNKy2ucVLxpfKYFqqnnKLdkqUXRAzjg_OpWzYit5docyZcDzbtHDTTOJJBiX6WKA9Zf4k5ERd7_lk6Tf2RfrdsqNIffOV0jUnK1o4ml849q1IWmB2Ay8KUxurUAaXvetS3A36Z0VCmF_DK3xGETnagv0aZ0noTpZy5gg7k5pG-fL4IZNSRHmkqzkBiTkFfTuyHyetq2RRoy_t8woUFk6tT-cm6ma7IThePWP32EuPJECQdDp7p53xPraMWW8ipWY2eCqlI75qfu5xb--qwpPQB2MWeWIG397PC_XKnfu_fr1RVUPIhYp8gZnr98pc9cUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رنکینگ مسخره ضریب هوشی کشورهای جهان را ناموسا رها کنید!
اگر میانگین ضریب هوشی ما واقعا چهارم دنیا بود باید سطح رفاه و توسعه اقتصادی ما هم دستکم در ۱۰ کشور برتر جهان قرار میگرفت (کشورهای دیگر صدر جدول را بییینید) نه اینکه رییس جمهوری مثل پزشکیان داشته باشیم که سطح ادراکش از توسعه برق این است که برود آستین کوتاه بپوشد و یک لامپ خاموش کند!</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SBoxxx/19605" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19604">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/19604" target="_blank">📅 12:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19603">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">توضیحاتی درباره روند تکامل صنعت دفاعی اوکراین و پیآمدهای خطرناک درگیری با این کشور برای ایران  #ژئوپولیتیک   لینک مقاله مرتبط</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/19603" target="_blank">📅 12:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19601">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رسانه‌های خارجی گزارش می‌دهند که یک مقام ارشد فرماندهی مرکزی ایالات متحده (سنتکام) هفته گذشته ایمیلی را برای گروه بزرگی از تحلیلگران ارسال کرد و در آن نوشت:
«ما به دنبال راه‌های جدید، نوآورانه و غیرمتعارف برای تحت فشار قرار دادن ایران و مجازات آن هستیم.»
این اقدام نشان‌دهنده درک این موضوع است که گزینه‌های موجود در حال حاضر برای دولت ترامپ محدود هستند و ممکن است از نظر سیاسی یا نظامی قابل قبول نباشند، که این امر ضرورت بررسی راهبردهای جایگزین را ایجاد می‌کند.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/19601" target="_blank">📅 12:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19600">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUborIMjQD8qc80cXd8F2_MOLA99Xy4HTwbkPH7GMUxsPFX1Yac29Up2mhOuGAsB17wvF9cmnWVGu7l6ydUZxeK13AN6uvzGCxJGUTc2Rh0TKb8SyVEalxDJ9z6vB9ErV5Fva82JIu2ei7qL-DyeEGE7Gxuj3qgcAQTI3Zqi41phEJQ_GKuhU_wW-qDELcHQjAlDS9mUQomqeGwM3dz3z2u0dGP98UuKOGzynhqKICJv025Al2rl4-gDjZrVXMyE_AhFCEmoqYeGTa777OcgluIA7G-_A2v4NYiRTjDZBUdc6L_dWSx5J5I-EGKV3k6UAW040v5wIXrF0Dg7aKtriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SBoxxx/19600" target="_blank">📅 10:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19599">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.  این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SBoxxx/19599" target="_blank">📅 10:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19598">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.
این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.
منبع: i24</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SBoxxx/19598" target="_blank">📅 10:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19597">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ ادعا می‌کند مذاکرات آمریکا-ایران روز دوشنبه آغاز می‌شود
او‌ گفت:
«خب، کاری که الان انجام می‌دهیم این است که در قالب مذاکره با آن‌ها صحبت می‌کنیم. این کار فردا بعدازظهر آغاز می‌شود و خواهیم دید که آیا این واقعیت دارد یا خیر. من عاشق انجام این کار هستم،»
ایران این ادعاها را رسماً تأیید نکرده است.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19597" target="_blank">📅 02:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19596">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19596" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19595">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19595" target="_blank">📅 01:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19594">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ درباره ایران:
نمی‌دانید این حملات به کجا منجر می‌شوند. منظورم این است که آیا همسایگان ایران با هجوم مردم (ایران) به کشورهایشان غرق خواهند شد؟
یک فاجعه. اتفاقات بد زیادی می‌تواند رخ دهد.
من ترجیح می‌دهم توافق کنم. به دنبال کشتن مردم نیستم. مردم می‌میرند. بسیاری از مردم می‌میرند. ما نمی‌خواهیم این اتفاق بیفتد.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19594" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19593">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ می‌گوید عربستان سعودی، امارات متحده عربی، قطر و ایران همگی از او خواسته‌اند حملات را لغو کند.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/19593" target="_blank">📅 01:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19592">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19592" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19591">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کشته شدن مامور پلیس در درگیری با اشرار مسلح شادگان  ستوان‌سوم شهید «سینا سیاه‌نژاد»، از نیروهای حافظ نظم و امنیت، هشتم مرداد در جریان درگیری با اشرار مسلح و حادثه تروریستی در شهرستان شادگان استان خوزستان، حین انجام ماموریت به شهادت رسید.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19591" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19590">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنتکام:
تا تاریخ 2 آگوست (و در راستای اعمال محاصره دریایی ایران)، فرماندهی مرکزی ایالات متحده (CENTCOM) مسیر 35 کشتی تجاری را تغییر داده است، 2 کشتی را غیرفعال کرده و 2 کشتی را بازرسی کرده است.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19590" target="_blank">📅 22:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19589">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترکیه با پیش‌بینی تشدید تنش‌ها، اقدامات کنترل مرزی را تشدید کرده و  مرز خود با ایران را با دیوار فولادی تقویت می‌کند.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19589" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19588">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک دیپلمات ایرانی به روزنامه وال استریت ژورنال گفت:  مقامات ایرانی از آسیب‌پذیری‌های سیاسی ترامپ آگاه هستند و در صورت لزوم، به دنبال بهره‌برداری از آن هستند.  در صورتی که دیپلماسی به نتیجه نرسد، سپاه پاسداران انقلاب اسلامی در حال بررسی حملات پیش‌دستانه است،…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19588" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19587">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک دیپلمات ایرانی به روزنامه وال استریت ژورنال گفت:
مقامات ایرانی از آسیب‌پذیری‌های سیاسی ترامپ آگاه هستند و در صورت لزوم، به دنبال بهره‌برداری از آن هستند.
در صورتی که دیپلماسی به نتیجه نرسد، سپاه پاسداران انقلاب اسلامی در حال بررسی حملات پیش‌دستانه است، حتی اگر ایالات متحده حمله نکند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19587" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19586">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19586" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فردا یک صوتی مفصل درباره این داستان قدرت نظامی اوکراین و بحث زیرساخت ها خواهم داد.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19586" target="_blank">📅 19:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19585">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یک حمله انتحاری به ایستگاه پلیس کابال در منطقه سوات، ایالت خیبر پختونخواه، پاکستان، انجام شده است.  بر اساس گزارش‌های اولیه، چندین نفر از نیروهای انتظامی و غیرنظامی در این انفجار کشته یا مجروح شده‌اند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19585" target="_blank">📅 18:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19584">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک حمله انتحاری به ایستگاه پلیس کابال در منطقه سوات، ایالت خیبر پختونخواه، پاکستان، انجام شده است.
بر اساس گزارش‌های اولیه، چندین نفر از نیروهای انتظامی و غیرنظامی در این انفجار کشته یا مجروح شده‌اند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/19584" target="_blank">📅 18:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19583">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">با گند زدن عبدالصمد ونساوی در حوزه برخورد با جمهوری اسلامی، اکنون شانس روبیو برای پیروزی در رقابت های درونی نامزدی حزب جمهوریخواه برای انتخابات 2028 به 31% رسیده که بالاترین میزان تاریخی خود است.  در سوی مقابل شانس ونس ترنس به 39% سقوط کرده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19583" target="_blank">📅 17:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19582">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نیروهای اسرائیلی در حال هدف قرار دادن ارتفاعات علی الطاهر در جنوب لبنان با بمب‌های آتش‌زا هستند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19582" target="_blank">📅 17:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19581">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YopgzJRXFafHj1BKPO63Rkr35p1EfL0KiTfgBcFyivhTiZVr0b2opDstirPfkQrxcTNGOOsu6SAV8sTsv_70CYUX7MkUp8wQjl3cV9ApMR0Wdk3E3sbWKOOTQveJoqMrh5HgfY7-ToPJlxdb2aRUMMrNW9Vl5H9aMJBWuEK1poxQaSEfFHZc57VeDZ7ZZvPXFNVwy5nR3FYN83WXZUJ_2j6MpEZvXI4KlLNj_2H2LTkLutp_mNmnWJ8_9ieDfDXYOn8GtpAa4pR_mvd-2lskUiMHx5YB2zvVD09aq0hcRXocvUP-wrBHibql4zBmTgl6KOW3JOZw_UCgoSjaNFBy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19581" target="_blank">📅 15:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19580">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بسیار بعید میدانم جمهوری اسلامی بدون لغو محاصره دریایی، تنگه هرمز را باز کند، حتی اگر ورودی تنگه هم در اختیارش باشد.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19580" target="_blank">📅 13:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19579">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:   حکومت ایران در طول جنگ سقوط نخواهد کرد.  مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.  تأکید باید بر این باشد:…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19579" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:
حکومت ایران در طول جنگ سقوط نخواهد کرد.
مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.
تأکید باید بر این باشد: اقتصاد، اقتصاد، اقتصاد، اقتصاد. این چیزی است که در نهایت حکومت را سرنگون خواهد کرد.
به نظر من حکومت می‌تواند به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی این اتفاق بیفتد، ترس دیگر مانعی نخواهد بود. آن‌ها بیرون خواهند آمد، قیام خواهند کرد و حکومت را سرنگون خواهند کرد.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19578" target="_blank">📅 13:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19577">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_9CdjKesT7LIPjTHd4RrEaZcmp87nBY5ygWkMXhjib8ZFDwdWqTY02s-mkGDO6h1OdqCJ1arsguxt0lvJjdP1utxzm0QXQ3lWXt9tM1pPI-EG_ULs24DxqeAggTYjfswhoG5ZHAkzf-Pw1zAVs09tIggl264BDKldCO-208TpQAFwtP0uaIKmNKUKViL5VaIgitlo14XDv18CJzVqQHVDGmIyi5T6eJCs6InQy-FO6OWKgtZ8XmnoA6WpAAEwp-mzVkD6Efbn2i9VCtp8Vsb8UlFM_ez6DqiGVueukRaoLhvPTRh2mkNZNcZIhYfkUOZWBPEnNS-IJe9JRAIBIS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarket Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19577" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19576">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آکسیوس :    ایران با طرح بازگشایی تنگه هرمز موافقت کرده است و قرار شده مسیر ورود از طرف ایران و مسیر خروج از طرف عمان باشد</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19576" target="_blank">📅 11:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یعنی موج 2 اینقدر کوتاه بود؟!  سبحان الله!   همه 5 سانت و 10 سانت و ....</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19575" target="_blank">📅 11:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19574">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیروهای مقاومت بعد از اربعین پاسخ آمریکا را خواهند داد
علاءالدین بروجردی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس، با محکومیت شدید حملات بزدلانه ایالات متحده و عربستان سعودی به مواضع حشدالشعبی و موکب‌های عزاداری امام حسین(ع)، این اقدام را نشان از استیصال و ناتوانی نظامی دشمن دانست و گفت:
با وجود احترام به قداست ایام اربعین حسینی(ع)، پاسخ قاطع و متقابل به این جنایات در زمان مناسب و پس از پایان این مراسم مقدس، توسط نیروهای مقاومت انجام خواهد شد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19574" target="_blank">📅 11:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19573">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آکسیوس
:
ایران با طرح بازگشایی تنگه هرمز موافقت کرده است و قرار شده مسیر ورود از طرف ایران و مسیر خروج از طرف عمان باشد</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/19573" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19572">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ گفت که حمله دیگری به ایران را به تعویق انداخته تا مذاکرات به سرعت ادامه یابند.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19572" target="_blank">📅 09:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19571">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ گفت که حمله دیگری به ایران را به تعویق انداخته تا مذاکرات به سرعت ادامه یابند.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19571" target="_blank">📅 09:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19570">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">باراک راید از آکسیوس، با استناد به دو مقام آمریکایی و یک منبع دیگر، گزارش می‌دهد که محمد بن سلمان، ولیعهد عربستان سعودی، نگرانی‌های خود را نسبت به طرح دونالد ترامپ، رئیس‌جمهور ایالات متحده، برای انجام حملات گسترده علیه ایران ابراز کرده است.
بن سلمان در یک تماس تلفنی با ترامپ، درخواست جزئیات بیشتری درباره عملیات کرد و از او خواست که حملات را آغاز نکند.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19570" target="_blank">📅 03:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حمله ایران به سلیمانیه و اربیل</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19569" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این شرکت Fire Point، بجز موشکهای دوربرد فلامینگو، پهپادهای انتحاری دوربرد FP-1 را هم تولید می‌کند که اخیرا در حمله به تاسیسات نفتی روسیه عملکرد درخشانی داشته است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19568" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دنیس اشتایلرمن، رئیس شرکت فایر پوینت، تولیدکننده موشک‌های «فلامینگو»، پیامی با تهدید علیه ایران منتشر کرد.  این تصویر، فلامینگوهای صورتی را نشان می‌دهد که در امتداد مسیری که اوکراین و ایران را به هم متصل می‌کند، پرواز می‌کنند و لوگوی شرکت و عنوان زیر آن آمده…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19567" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تهدید یک نظامی اوکراینی به حمله به ایران با موشک های کروز فلامینگو</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/19566" target="_blank">📅 01:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19565" target="_blank">📅 01:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6RIDgBDdbnHxDKE8BPwr-ekXkcsqxAjBYmLGEtl2kCPko_5pbw-2-6p_UnZMAoHpIOq1cem29aEvtss-efEhQ9q689oXsLJKVafVpSa7_Z3762_zOBib6oLf95YbazJlI59Hoig3sMRQ29ftDF4WzxXAid7Sn1Ac52hlmQd2Cyi4PdYP6oHCwwQ1i0w7FLOrfN1hYGT4mX-rAl0IR9zTaZze4ahwmJ3iZjRIQw2fp-iivTPMQkUeDUjB02YAXMu6oPb5l9tjxzKmfwEUCNH_mm5z6Ltf12e7Dj-loPUQw_KNKEl2MWvI6GcHsEsHrbp6BRswQE_o5Z-zHoMUxbqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت اتاق جنگ اسرائیل</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19564" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دکتر مرندی این بار دستور تخلیه کل خاورمیانه را صادر فرمودند.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/19563" target="_blank">📅 00:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19562">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGXbFQ614mNJLCQoUE3ufDnKtkpRpRhnmwcr6-Ox7qvukFFRUlD5GJYMI3bZMUfrp9s11YxTdQPgOjskB753hpU292AWAhdhNpggm_ofeceXfak5d-k9vuOuUzFl3N-pzb11YjMMkgxeHYQVM8ilGylo4JU_AgBueK2xLeNVdS2x2bbXeSZeEJKJd4M1eJRMqqIji-qmYzhDiWwfU7zdvHXR7iwv4PSCF6S-kYCQHPMpgiN-3lEdKCJKBTdm-TsVaDlK8Nr7iO4GMxcV5lI5iQ14nYn_CeAv0TeyHO967fA-EBO6C6RmBhOZbdnEBb1chOyfNQpDcjBud0s0s2WF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/19562" target="_blank">📅 23:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19561">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک منبع از وزارت جنگ ایالات متحده به شبکه فاکس نیوز گفت:
«ما برای یک جنگ تمام‌عیار علیه ایران آماده هستیم.
در چند ساعت گذشته، رئیس‌جمهور ترامپ دستور انجام تعدادی از حملات مرگبار و خطرناک علیه نیروهای سپاه پاسداران انقلاب اسلامی را صادر کرده است.»</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/19561" target="_blank">📅 22:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19560">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wtb38X4oK_pu62hEwKqGcMrdKSe8FNr41XVi1fS-ytJO3Qn3E2aMBzFNOnMIHjkrUiInXwbAp7m3xq87ANGeOJm2hdfRL_TMcj_buo5y3PCqbNFilx6gVH5nn1WqN0n6dH69qRvs4b7rwn6U3wxh0ZUBP74gEhIP5LcXvpJHz-bj98zGwnJISrpn7ZjBzpVzKZW7610EfMBT4PZOLhSQXewifrrq7w1KkJX1Qm0te9JwIz6NbmXEF0AWKrwKgsUxyS9KKIVZtHPxMJJCGH0KlVQ8wp3BMAB9MPnOH7Lt7qy4-hB00v06fLEJgSG4X9jUem7-vCCvkTcIFcHgQ8B0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ترامپ در حال نابودی ارز ایران است.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/19560" target="_blank">📅 21:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19559">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">برخی گزارشهای آمریکایی می‌گوید کشورهای خلیج فارس به رهبری قطر در تلاشند تا از جنگ مجدد آمریکا با ایران جلوگیری کنند.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/19559" target="_blank">📅 20:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19558">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">— مقامات آمریکایی در حال بررسی موجی از حملات سایبری علیه سیستم‌های آب در حداقل هفت ایالت هستند، با شواهد اولیه که به ایران اشاره دارد.
حملات برخی عملیات را مختل کردند اما آب آشامیدنی را آلوده نکردند و هیچ خطر شناخته‌شده‌ای برای سلامت عمومی ایجاد نکردند.
دونالد ترامپ نقش ایران را زیر سوال برد، در حالی که مقامات ایالتی و فدرال گفتند که ایران بر اساس اطلاعات موجود همچنان مظنون اصلی باقی می‌ماند.
متخصصان امنیت سایبری این کمپین را یک بی‌سابقه در هدف قرار دادن زیرساخت‌های آب ایالات متحده توصیف کردند که احتمالاً قصد بهره‌برداری از سیستم‌های آسیب‌پذیر را داشته است نه هدف قرار دادن جوامع خاص.
— نیویورک تایمز</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/19558" target="_blank">📅 20:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19557">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مکن ای صبح طلوع …</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/19557" target="_blank">📅 20:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19556">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wdz8QXSZLhhDlRj3-YdlMDd0PuBoVR5A7KYSxpC-NjZc110_d2MfPDxzrXEzq66a-H5gpZyKMxODOdPw_a3g-T7H1GxBxvrRPmMijUOcodSGRT6A8FE-o8sCJT8EH01xPG-heqvKoWTtF6D92_VG4GW8vG7lHsENfpdJ0bxigzVbAP3lZnhgsAywCPYpcA2UdT8JbtW_DU9xfE5sPEUgQq6dDkH6qZGO4U-uncWp5BX8pNa7iuNHTbFWB4-aTAPXbV1J8by9SiwdcSfF23sJQQ6mJtacl-6RM7dAZoyn-fFYsSuOQ49xnsHYBrXV0vDb8Y5hkyiZ4BVGjG28sNhf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکتر مرندی در پاسخ به تهدید ترامپ دوباره دستور تخلیه شبه جزیره عربستان را صادر فرمودند</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SBoxxx/19556" target="_blank">📅 20:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19555">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXojuZUbbV-XrG98shx_fCrlTb4Sm6bYRn3E4fO3F-c6iXTnVdxalX5S1dIawg5OLK25gw0jRKJb-CaOIDRpF5fjlA8I8SO4tEJ6HtvMa6bjXDzNr2gPxG0IDjpQhXeaoZlczdTGnCN-OkpdQ38V5zLxUdAQJHA8lJxGSKt1ulsb1oIiojHY2ZcS-QXrey6yUh62aNC4oimSR6ohnvxAQYko3W82wRpq69TU03GzTruw-zdN9n-BE90s13qQIv5ldxUsSv7VL2sTbdWe1j63wl0kEC7PZCVmnosDgC4dWZM6sziRkFGXoZaftp4cljYui1EWiIOMC9SQLw3TC0VFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه روسیه با پهپادهای ایرانی رقابت تسلیحاتی در حوزه پهپادها را تشدید می‌کند   رئیس‌جمهور اوکراین، ولودیمیر زلنسکی، ماه سپتامبر مجمع عمومی سازمان ملل هشدار داد که «ما اکنون در حال تجربه مخرب‌ترین رقابت تسلیحاتی تاریخ بشر هستیم»؛ اشاره او به بهره گیری روزافزون…</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SBoxxx/19555" target="_blank">📅 15:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19554">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به جای جای ایران که مینگرید، نشانه های بازدارندگی قدرتمند جمهوری اسلامی را می‌توان دید</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/19554" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19553">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در اسلام آباد غرب، کرمانشاه خبر داد.</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SBoxxx/19553" target="_blank">📅 14:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19552">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در اسلام آباد غرب، کرمانشاه خبر داد.</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SBoxxx/19552" target="_blank">📅 14:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19551">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd37ccbfd.mp4?token=IMoIRsuOmJ_Gli4BbItkeJ7yh_ucglDLlL9F6RS1CJM5Ozc4UZaz62axx-48V4A3-teiUqIvNsZz3tqS8i-Ccor32mvcwtt810YY8WorqyaJTkwK5ZXEMpd2cMUK2UUYR00QdNXGBbrWZKQVV6TeKS4AVItJ68whqcDp7gfqr_LUDYGMQVB1YD2W6MKnrKVMUtEhOtijMaTLhyVUCrNB0O1ytDZqnf-7oLrc984hYLbqfISk1ntuoTsfY6QyLpU5mmvqM20fah5meuHOr4U25dA7n9P7jbpJp-LIawDVimQntGcTfufCLIehRkMBfMlYuygxoZlkmN69OImWffj1C3O76knshVlUj2YoOJNs3sYQP_1wrtiomzPF-hbWjj9pf-DZHAqrtm5uuyMgMZSgyQ6JCNwqh20Bajkz6RCDjTM9lY7PgOcYlh1Enz9i-0VP--MNspdQjCaubwhELXgFZ6Z1NMCwwLAcpsjRYR4tlEUR2Z8k10zNFG4k979C2FP9xQ6Sg-yhBzxPrwFpFsAODiNAjFK5Csn-e2DLCKHOYLwLPDIExXiU4z95eyyqzVA2kWlH4JHYkw8hqvEsNqe1jEf31Ys2gws3L-dbcWgsAGii5t4bBvVx0dgqWQUjFhu8I0qv-BAvXuPZVt31MpNgaeUTOXcqEigXUROmZifN_3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd37ccbfd.mp4?token=IMoIRsuOmJ_Gli4BbItkeJ7yh_ucglDLlL9F6RS1CJM5Ozc4UZaz62axx-48V4A3-teiUqIvNsZz3tqS8i-Ccor32mvcwtt810YY8WorqyaJTkwK5ZXEMpd2cMUK2UUYR00QdNXGBbrWZKQVV6TeKS4AVItJ68whqcDp7gfqr_LUDYGMQVB1YD2W6MKnrKVMUtEhOtijMaTLhyVUCrNB0O1ytDZqnf-7oLrc984hYLbqfISk1ntuoTsfY6QyLpU5mmvqM20fah5meuHOr4U25dA7n9P7jbpJp-LIawDVimQntGcTfufCLIehRkMBfMlYuygxoZlkmN69OImWffj1C3O76knshVlUj2YoOJNs3sYQP_1wrtiomzPF-hbWjj9pf-DZHAqrtm5uuyMgMZSgyQ6JCNwqh20Bajkz6RCDjTM9lY7PgOcYlh1Enz9i-0VP--MNspdQjCaubwhELXgFZ6Z1NMCwwLAcpsjRYR4tlEUR2Z8k10zNFG4k979C2FP9xQ6Sg-yhBzxPrwFpFsAODiNAjFK5Csn-e2DLCKHOYLwLPDIExXiU4z95eyyqzVA2kWlH4JHYkw8hqvEsNqe1jEf31Ys2gws3L-dbcWgsAGii5t4bBvVx0dgqWQUjFhu8I0qv-BAvXuPZVt31MpNgaeUTOXcqEigXUROmZifN_3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کمپانی Boring ایلان ماسک حساس باشید. فکر می کنم بزودی همه ملل به سمت انتقال دارایی های حساس نظامی و حتی اقتصادی خود به زیرزمین بروند.  موفقیت نسبی و کم هزینه مدل عملکرد ایران و حماس زیر شدیدترین فشارهای نیروهای هوایی برتر جهان و گسترش استفاده از پهپادها…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SBoxxx/19551" target="_blank">📅 12:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19550">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سفارت ایالات متحده در اردن :
«آمریکایی‌های حاضر در خاورمیانه باید احتیاط و هوشیاری بیشتری به خرج دهند و برای لغو پروازها، بسته‌های دوره‌ای فضای هوایی و اختلالات احتمالی سفر آماده باشند.»
«آمریکایی‌های حاضر در منطقه باید به ترک آن فکر کنند، یا در صورت تشدید درگیری‌ها برای ترک منطقه آماده باشند».</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/19550" target="_blank">📅 12:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19549">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ویدیویی بسیار جالب درباره روند ایجاد و تکامل ایده ساخت پهپاد لوکاس که مشابه شاهد-136 است اما مجهز به هوش مصنوعی و توان رهگیری بالاتر  https://www.msn.com/en-us/news/other/watch-how-the-us-turned-iran-s-drone-into-a-weapon-used-against-them/vi-AA20tLa9?oci…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/19549" target="_blank">📅 11:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19548">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ارتش آمریکا یک یگان ویژه پهپادی در منطقه عملیاتی سنت کام (غرب آسیا) مستقر کرده که در آن از پهپادهای Lucas با طراحی تقلیدی از پهپاد شاهد-۱۳۶ خودمان استفاده می‌شود.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19548" target="_blank">📅 11:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19547">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">افزایش اهمیت اهرم فشار چین
به گزارش رویترز، با تشدید دوباره جنگ ایران، کشورهای عرب حاشیه خلیج فارس به‌جای واشنگتن، به چین روی آورده‌اند تا از اهرم اقتصادی خود در برابر ایران برای بازگشایی تنگه هرمز و مسیر دریایی دریای سرخ استفاده کند. این وضعیت در واقع آزمونی است برای اینکه پکن تا چه اندازه توان و تمایل دارد تهران را تحت فشار قرار دهد.
منابع کشورهای خلیج فارس می‌گویند تلاش آنها برای ایفای نقش بزرگ‌تر چین، ناشی از افزایش نارضایتی است. جنگی که در ۲۸ فوریه با حملات آمریکا و اسرائیل به ایران آغاز شد، اگرچه به رقیب منطقه‌ای آنها آسیب زده، اما هم‌زمان صادرات حیاتی انرژی این کشورها را نیز محدود کرده و آنها را، با درجات مختلف، در معرض حملات قرار داده است.
سه منبع منطقه‌ای می‌گویند از آنجا که ایران و متحدانش هم‌زمان تنگه باب‌المندب در دریای سرخ و تنگه هرمز را تهدید می‌کنند، کشورهای خلیج فارس از چین درخواست کمک کرده‌اند؛ به‌ویژه با توجه به اینکه جنگ محدودیت‌های قدرت آمریکا را آشکار کرده است.
وانگ یی، وزیر خارجه چین، ده‌ها تماس تلفنی و دیدار با همتایان خود داشته و برای دستیابی به آتش‌بس جدید تلاش کرده است. همچنین ژای جون، فرستاده ویژه چین، با مقامات کشورهای عرب خلیج فارس و همچنین ایران مذاکراتی انجام داده است.
اما این دقیقاً چیزی است که وضعیت به آن نیاز ندارد! هیئت تحریریه وال‌استریت ژورنال هشدار می‌دهد که نتیجه جنگ ایران تا حدی به رفتار و عملکرد قدرت‌های محور مقابل آمریکا بستگی خواهد داشت.
این نشریه می‌پرسد:
«با وجود اینکه آمریکا بخش قابل توجهی از زرادخانه موشکی ایران را تضعیف کرده است، آیا چین به‌سرعت به بازسازی آن کمک خواهد کرد؟ آیا روسیه که به دلیل کمک‌های ایران در جنگ اوکراین به تهران بدهکار است، به احیای برنامه هسته‌ای ایران کمک خواهد کرد؟ آیا هر یک از این دو کشور، سامانه‌های پدافند هوایی پیشرفته‌تری در اختیار ایران قرار خواهند داد؟»
در واقع، نگرانی اصلی این است که چین و روسیه به‌جای ایفای نقش میانجی برای پایان دادن به جنگ، به بازسازی توان نظامی ایران کمک کنند. چنین سناریویی می‌تواند جنگ را طولانی‌تر کند، رقابت ژئوپلیتیکی میان آمریکا و چین را تشدید کند و هم‌زمان ریسک اختلال طولانی‌مدت در مسیرهای انرژی هرمز و باب‌المندب را افزایش دهد.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19547" target="_blank">📅 10:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19546">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">CBS News:  آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.  ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/19546" target="_blank">📅 09:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19545">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هدف قرار گرفتن ۲ کشتی در نزدیکی سواحل عمان در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19545" target="_blank">📅 09:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19544">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_WWDLk3ir2TBxGcTNl7g05HhD1_9-Fw39syyvOL6l9OGM9fk6-foAtDNSwNLxYWtbad_fZDI2Slg6Le2pJJMMHQjjLOWncqUlxFGfJ8AqWE5w4On4UtkTFBPl56oWuNpH4UrdKjrDwPXzhrICAMC3ClNiUefGbVEMh_CmM2pZ1qtWVfU5lXE3IZ7AYQB41uZCf3fZV_q0ahD_NwXP_5v2AEH7mEyAjMlFF45GIpIWeZDP-RkSjMNvQTjmxJyt_OsejZ3xZVzW0TJ34i2fQn1Yw289XL5X3NVXi3--GoW38OqoLEDZYteERaMLY4hInC_q8ySCJ53nGCHTZRA4mQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار : آیا چین و روسیه اطلاعات هدف‌گذاری را به ایران می‌دهند؟ این حملات اخیر ایران  بسیار ویرانگر برای نیروهای آمریکایی بوده‌اند.  روبیو: هر زمان که در یک منطقه جنگی مانند الان هستید، خطراتی با آن همراه است. منظورم این است که در نهایت، این واقعاً ثابت می‌کند…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/19544" target="_blank">📅 01:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19543">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو خطاب به رئیس جمهور ترکیه:   اردوغان یک دیکتاتور یهودستیز است که مرتکب نسل‌کشی علیه کُردها می‌شود  او که از حماس حمایت می‌کند، مردم خود را سرکوب می‌کند و مخالفان سیاسی خود را زندانی می‌کند، آخرین کسی است که می‌تواند درس اخلاق بدهد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/19543" target="_blank">📅 01:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19542">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">CBS News:  آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.  ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19542" target="_blank">📅 01:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19541">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مرندی:  رژیم مراکش صرفاً ابزاری دیگر برای نتانیاهو و ترامپ است. آن‌ها اسپانیا را به خاطر حمایت از فلسطین تنبیه می‌کنند.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19541" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19540">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19540" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19539">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">CBS News
:
آمریکا و اسرائیل در حال آماده‌سازی یک کمپین مشترک بمباران بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده، اما حملات ممکن است این آخر هفته آغاز شوند.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/19539" target="_blank">📅 00:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19538">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ:   ایران موشک‌های بزرگی به سمت اردن پرتاب  کرد و قبل از اینکه نزدیک بشوند  توسط سلاح‌های فوق‌العاده‌ای که داریم زدیم: بینگ بینگ بینگ بینگ بینگ بنگ</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19538" target="_blank">📅 23:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19537">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📡
استفاده ارتش چین از هوش مصنوعی آمریکایی برای تقویت توان نظامی
🔷
خبرگزاری رویترز در گزارشی اعلام کرد که پژوهشگران نظامی چین با بهره‌گیری از خروجی مدل‌های پیشرفته هوش مصنوعی شرکت‌های آمریکایی «اوپن ای آی» و «انتروپیک»، سامانه‌های بومی هوش مصنوعی را برای تقویت توان دفاعی و نظامی این کشور آموزش داده‌اند</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19537" target="_blank">📅 23:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e924f93a.mp4?token=uiF29Kqen7Y9YosxajbCU0ajh0qVlllJY78XpH8n9w0RgGEjeWia5meBpl2OHUDi1ETej8cTsH7bNYsTTjr6nscNgt_11K5fPevnKwMQtCjOSdGT8Bw2tdnYvt3ImTJI6r1SKK0l8Y7Bq8IywJzyWfP4-3lbI1sR0LM1W78ot-HAd0TlR1RZb8DTGG_CVTf20pYnK-8eHNvLHjqwpoKk7ybJ_GWuAWboA2DbNCKMhRkavcwweNl2PhyxzPNaAtQ9Y2rlvEMhicKSiMt5n9X_oJoHlH9UsnpCY7riAWOgBYQq_8-1Gpdzch4dz6g3nZR-l2mK0Er5VJu4hgcHi1vbkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e924f93a.mp4?token=uiF29Kqen7Y9YosxajbCU0ajh0qVlllJY78XpH8n9w0RgGEjeWia5meBpl2OHUDi1ETej8cTsH7bNYsTTjr6nscNgt_11K5fPevnKwMQtCjOSdGT8Bw2tdnYvt3ImTJI6r1SKK0l8Y7Bq8IywJzyWfP4-3lbI1sR0LM1W78ot-HAd0TlR1RZb8DTGG_CVTf20pYnK-8eHNvLHjqwpoKk7ybJ_GWuAWboA2DbNCKMhRkavcwweNl2PhyxzPNaAtQ9Y2rlvEMhicKSiMt5n9X_oJoHlH9UsnpCY7riAWOgBYQq_8-1Gpdzch4dz6g3nZR-l2mK0Er5VJu4hgcHi1vbkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/19535" target="_blank">📅 20:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ درباره اوکراین:
تانک‌های روسی در حال حرکت به سمت کی‌یف بودند، اما در گل گیر کردند.
یک ژنرال روسی تصمیم گرفت به جای استفاده از بزرگراه که به خوبی در حال حرکت بودند، از میان گل عبور کند.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19534" target="_blank">📅 20:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بسنت وزیر خزانه داری آمریکا :
ما در مارس ۲۰۲۵ شروع کردیم. در دسامبر ۲۰۲۵، بزرگترین بانک در ایران فرو ریخت.
بانک مرکزی مجبور به چاپ پول شد و این باعث تورم گردید. اکنون آن‌ها قادر به پرداخت حقوق سربازان خود نیستند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/19533" target="_blank">📅 19:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/19532" target="_blank">📅 19:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ:
شنیدیم که در مینه‌سوتا یک حمله سایبری رخ داده است. آن‌ها آن را به ایران نسبت دادند. من این را نمی‌پذیرم.
من آن را به مینه‌سوتا و فرماندار فاسدش نسبت می‌دهم.
آن‌ها دوست دارند بگویند، «آه، این ایران است. ایران باید خیلی خوش‌شانس باشد.»
ایران مشکلات بزرگتری نسبت به نگرانی درباره مینه‌سوتا دارد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19531" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19530">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">روسیه حدود 30 هزار تن بنزین از مراکش وارد کرده است تا کمبود سوخت ناشی از حملات پهپادی اوکراین به پالایشگاه‌های بزرگ را جبران کند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19530" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19529">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdEv0JZ1gdK35vbTRlUtIPny2mfZmtlD4l5Akm0lXGNRiknEcmFkh3Ab7xu4wItASCPY3kSdiMSYXfOaUbMToO9-jqlb2nFNlT29jWcJqgWuFRfKaG8ngSlVRY1J0YUseh2A72T0Bydo201V_xpKRPaAuoEvvT40DTs2bUEZgh0O6LXBYmlDX7mVf9mHcnhe1rpIRjy1HLw5dy6g2o7lNOzyt4yMvTJvmm8bHCLZ_oiJm_QPV6lGv7BaanmyMLcvRK1tSM3FTX54pnfsj__suX1A71-dhwMJ1NoqrfkKxMhyNcxpnUEcExIVAO8Mh6mGgEBiEyzeQhlbj1079PDVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه ممنوعیت صادرات بنزین را تا سال ۲۰۲۷ تمدید کرد!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19529" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19528">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اسرائیل طرح "هیئت صلح" رئیس جمهور ترامپ را که هدف آن خلع سلاح حماس بود، رد کرد. این کشور مدعی است که این طرح برای اسرائیل قابل قبول نیست و اسرائیل هر حقی را برای هدف قرار دادن و کشتن افراد در غزه دارد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/19528" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19527">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این اسپانیایی ها 700 سال زور زدند تا عربها و بربرها را از خاکشان بیرون بریزند؛ چپ ها در 2 سال دوباره همه آن کوششها را بر باد دادند!
چپ = نکبت</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/19527" target="_blank">📅 17:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19526">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک زن وحشت‌زده در سئوتا درخواست کمک از نیروهای نظامی می‌کند و می گوید: "ما تنها هستیم":  ما به حضور نیروهای نظامی در خیابان‌ها نیاز داریم. آن‌ها اینجا نیستند.  ما تنها هستیم.  چطور ممکن است من نترسم؟ من می‌لرزم. این یک تهاجم است.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19526" target="_blank">📅 17:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19525">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/19525" target="_blank">📅 17:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0WpGmkLbjcTlE989iVbz6OSS7jtkaBiMUoj6Ku0bYWcMIyDmjH8SDyNxUIhu2t7DMc7JRnSM3Ytsvy-98NyiNbhLEuqo2hg_AQhbSgIKVH7bfrwEsAuBaF8BlIvyOFdrcbqow7Cdn5t3mPOpAm4jpskdfOQNGMQ9E0pTpIMVCCVVYE_MvwWeXTx-c5rrTqAHTdMX_3WOV0VjmOyP6kS2yrrnEHXb5g18--vWK-eIALa10djzrtFGmnN7Siad601DEk5zZRu6SPbHwnRlV9QAShMjpunn96_IevIuGMSogKk1maD4qN9m-FuQ9ROR2qPXbHEaMIfydhihuz9iUxFKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز بسیار بالاست و پیش بینی می شود طلا (و شاخص های سهام) زیر فشار فروش بروند. (خصوصاً شاخص های سهام)</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19524" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ:
"جنگ با ایران به خوبی پیش می‌رود. ایالات متحده ضربه‌ای سنگین به ایران وارد می‌کند و ما به سادگی به پیروزی ادامه می‌دهیم</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19523" target="_blank">📅 17:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/19522" target="_blank">📅 17:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تنگه ای که استراتژیک نخواهد ماند  وقتی گفته می شود ایران‌ استراتژیک‌ است، بخش مهمی از این‌ گزاره به دلیل اشراف جغرافیایی ایران بر تنگه هرمز است. چون دستکم‌ یک پنجم انرژی فسیلی سالانه جهان از آن می گذرد. ولی گلدن ساکس مدعی است که تا امروز ۷ خط برای دور زدن…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19521" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4NgQ-iSHD_VwXLjS8FeiRj0LmLSSHUxSqAZsf3mn2FB7mq3eBobVT3-UTkS-6gPIL8srIwlL2RZpuoa5EzH0O_-HwsDJVauONLZCgZ1Q5DyK07_kfW8W3UL6jCD3YNIum3ZMcqfqi79ZC__jJ6pUbMCm-aT2zW7W3NRIiA5alGzioQMlKsI8UL1ENbCgOg1-Sl5R6DFJh7UAtX-0u4Sd8h4wz6_S1MsoC6pa324SlS1LIMFajmoGc2M8X4YuPpo9YK-zdQN8F8m4mR5iZ12ltDTW6xOdVThR3Z1aJy0Q5QVqypn1DsBELnzyI9E-tqxYXkYq0y_UlSk29qLNLwOZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عصر اقتصاد دانش بنیان، تنگه بندی و گردنه گیری تنها منجر به انزوا و تیپا خوردن خود عامل می‌شود و اندونزیایی ها خیلی سریع فهمیدند که این لقمه برای دهانشان بزرگ است ولی خب.</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/19520" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19519">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9hzaXmrSi_AyN6AcSYNxo4iPi4DlDFysubyS5DJvIPNrs0OF30HQexiQhHlts7n0HNAjW8BDfqGxID-PmfgxRHfDjOpjtKfa-kb2nEEWCDgalNvVBYGGPr-vshJG5i0rUUGZBUYFY70CKi5wuT79FHeonx04puEMmXxqgbudW1KdXwf3a3_gpPHaXrXXLSFAsGVc_b_FzJyDCLTDTSkHpyW7QxmDNR_ICz-i37ckySD7Y23Ho1zBfzc2DGqNSUqG5zDnHds1DELDorkO0x1URuxTaooxRyT9eoHxmIKyVPiRgZ_2tOgFEM5IzPsISRtQMtVVaqqwAQBBIGmu_t-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری نظامی اسرائیل-مراکش و پیام راهبردی به مادرید  همکاری نظامی اسرائیل و مراکش دیگر صرفاً یک رابطه تجاری در حوزه صنایع دفاعی نیست؛ این همکاری به تدریج به یکی از مهم‌ترین مؤلفه‌های معادلات ژئوپلیتیکی غرب مدیترانه تبدیل شده است. از انتقال فناوری پهپادهای…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/19519" target="_blank">📅 15:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19518">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 16</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19518" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 16
جمعه 31 جولای 2026</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/19518" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19517">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک کشتی حمل گاز قطری که میخواسته از مسیر تعیین شده ایران عبور کند توسط آمریکا متوقف شد!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19517" target="_blank">📅 14:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19516">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ایالات متحده و اسرائیل در حال بررسی محاصره زمینی ایران برای افزایش فشار اقتصادی هستند!  این پیشنهاد به دنبال متقاعد کردن کشورهای همسایه — از جمله افغانستان، ارمنستان، آذربایجان، عراق، پاکستان، ترکیه و ترکمنستان — برای محدود کردن یا بستن گذرگاه‌های مرزی با…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/19516" target="_blank">📅 13:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19515">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ایالات متحده و اسرائیل در حال بررسی محاصره زمینی ایران برای افزایش فشار اقتصادی هستند!
این پیشنهاد به دنبال متقاعد کردن کشورهای همسایه — از جمله افغانستان، ارمنستان، آذربایجان، عراق، پاکستان، ترکیه و ترکمنستان — برای محدود کردن یا بستن گذرگاه‌های مرزی با ایران است تا واردات و صادرات این کشور را محدود کند.
این پیشنهاد در کنار سایر گزینه‌ها از جمله حفظ محاصره دریایی، از سرگیری حملات نظامی یا پیگیری یک توافق دیپلماتیک مورد بحث قرار گرفت.
طرفداران این راهبرد استدلال می‌کنند که انزوای اقتصادی بیشتر می‌تواند دولت ایران را تضعیف کند، اگرچه تحلیلگران اشاره می‌کنند که اجرای یک محاصره زمینی با توجه به مرزهای زمینی طولانی و ارتباطات منطقه‌ای گسترده ایران بسیار دشوار خواهد بود.
— تلگراف</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/19515" target="_blank">📅 13:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19514">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گفته می‌شود عربستان سعودی در حال آماده‌سازی یک تهاجم نظامی بزرگ علیه حوثی‌ها است که برنامه‌های آن می‌تواند شامل عملیات دریایی در دریای سرخ و حمله زمینی در یمن مرکزی باشد.
این اقدام پس از حملات حوثی‌ها به تأسیسات نفتی عربستان و محاصره کشتیرانی عربستان توسط این گروه صورت گرفته است.
منبع: گاردین</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19514" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19513">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
روز دوم تهاجم مراکشی ها به اسپانیا آغاز شد. خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✍🏻
Desert Eagle
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/19513" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19512">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار نظامی ایران و جهان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=GPeEWSFrcrmLPVRtNFPuvkW36DXMeC8IQ9QKQ6kMsgatac2aeDLff97DCUUGN8XAsMquy3eFv5yV--JhEE-8ygVCR3y480LLowgQgl4v9qm9Zv5FENhU1d1rsKRHIqadiQZjO2s4G1QJsu0lWPu_K0_NIqFe4Scx5aFrBIxP6Ye5wktDlyHVnzQXkzVizTTzdR5UPRJik-NZHlKaManoVyrQC28ykilNZID33M9-ZKCOuRiQrkgKXJ6LEtSGHvXNpNAerKACsN_o0UDeAc-Fxucfx66E19OpEgjsmVnpaESI8yartK7yhG9ezGXHjOAiIdXZuxxNY9yRlrspyoQ6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=GPeEWSFrcrmLPVRtNFPuvkW36DXMeC8IQ9QKQ6kMsgatac2aeDLff97DCUUGN8XAsMquy3eFv5yV--JhEE-8ygVCR3y480LLowgQgl4v9qm9Zv5FENhU1d1rsKRHIqadiQZjO2s4G1QJsu0lWPu_K0_NIqFe4Scx5aFrBIxP6Ye5wktDlyHVnzQXkzVizTTzdR5UPRJik-NZHlKaManoVyrQC28ykilNZID33M9-ZKCOuRiQrkgKXJ6LEtSGHvXNpNAerKACsN_o0UDeAc-Fxucfx66E19OpEgjsmVnpaESI8yartK7yhG9ezGXHjOAiIdXZuxxNY9yRlrspyoQ6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روز دوم تهاجم مراکشی ها به اسپانیا آغاز شد.
خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✍🏻
Desert Eagle
▪️
@World_Newsly</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19512" target="_blank">📅 12:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19511">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJzQOYv1eRPqeTtx7N1-jKiU7Qf4Y4iQO5nIhf-xMR1x25VBRC9C44eTgAyENf2QlSCbchfyEdtjEuMZTKdVygiyHGhJqM0t0t5EmZ32wy3kmkPbquc7C5RcCPyzkigi_p3QcUvmHbXCr6Wu-0kjnIPnzvnCV9cpjdwHhAmigXQlfGxOinyu5PTyuzn1ipj4MeTA0tZVRzCngKeOPjPQPIOhgjg4cAjukqrAqsRuJlcNxK8nHZ2RqoDKm4FTPcUnkeIqoq21lTKN3a8wsmBmX-bUvblzAfQaDZPxsXgeeBRBKIynJ38iHlpSYOpMaCPTgMF1Quxn6xmVg2q87KU5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19511" target="_blank">📅 12:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19510">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خب سیگنال پایان موج 2 از 5 دارد صادر می شود:
استاد خوش چشم: فک نکنم‌ دیگر جنگ بشود</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19510" target="_blank">📅 12:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19509">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پلیس:  زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/19509" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19508">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پلیس:
زائران بازگشت از اربعین را به روزهای پایانی موکول نکنند</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19508" target="_blank">📅 11:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19507">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صدها مهاجر جوان امروز صبح به سوی سئوتا در اسپانیا شنا کردند. بیش از ۱۷۰۰ نفر در یک هفته.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19507" target="_blank">📅 11:51 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
