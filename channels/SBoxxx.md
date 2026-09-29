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
<img src="https://cdn4.telesco.pe/file/KWrhVlbphxxMnhiH4jxwuIHnBlc7YzKAWiinJ8KT1tHFz-Ee0A1N_6AlLMTQT5-FmOX8tnE1E07p2GcbexkVFk2svkw9ruwwKrtmBwwlP--3kt5DE_Qw-OW3LSqA8Ayhq0LonqSECIVE1q4PDW9xgofdmwECHQ7HkmA5FxjQKjENDavG8RrJXd8XDd1emlljbbGI6UZDuuq3kYC7WKPEbD_q1WfU1bFeCBIA-hUclPYtgYuHYm5IIAOOeFM--ZCWqhmur7s4bxiIUuMH1uEfhYC1nTO_T43PrQ_U8ovG8JLxbAeRZmb6BcRpbp3dXc5k2f3X5aNyJDQQx7gmTiBp6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 03:20:11</div>
<hr>

<div class="tg-post" id="msg-21337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آکسیوس به نقل از یک منبع آگاه:
هیچ پیشرفت ملموسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها خواستار مواردی هستند که واشنگتن نمی‌تواند آن‌ها را بپذیرد.</div>
<div class="tg-footer">👁️ 471 · <a href="https://t.me/SBoxxx/21337" target="_blank">📅 02:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21336">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بوئینگ مسابقه F/A-XX نیروی دریایی ایالات متحده را برنده شد و با شکست دادن نورثروپ گرومن، قراردادی با ارزش بیش از ۲۰ میلیارد دلار برای توسعه جنگنده نسل بعدی ناوهای هواپیمابر نیروی دریایی را به دست آورد.
پیش‌بینی می‌شود که این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین F/A-18E/F سوپر هورنت و EA-18G گراولر شود.</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/SBoxxx/21336" target="_blank">📅 01:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21335">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فردا ساعت ۱۲:۳۰ با نیما درباره آخرین تحولات مربوط به جنگ گفتگو خواهیم کرد
لینک تماشای نشست Live</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SBoxxx/21335" target="_blank">📅 01:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21334">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تتر = ۲۵۷ هزار تومان!</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SBoxxx/21334" target="_blank">📅 00:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21333">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روس‌ها همیشه موقع مذاکره ایران با آمریکا کرم میریزند</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/21333" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برخی منابع روسی از احتمال قریب الوقوع جنگ با اسراییل خبر می دهند</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/SBoxxx/21332" target="_blank">📅 00:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">برخی منابع روسی از احتمال قریب الوقوع جنگ با اسراییل خبر می دهند</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/21331" target="_blank">📅 23:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21330">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjQri5U0LSva0AuquEWtaWkP41P7OBfNROEH3SQxFVccBGd2UK7bCMiRhUivFCSl6sHe7owYHMYtZtWbm33TnjijxA2PWvP5dVOiv3-XzlBZyZlxC95RZqAnlw2PO6bVdweoNd5-ivqp-rchXzLYl_PSalTbYgwyVFOAZTPkA6XRFuEB_roq4EEC4AGeKiMbHvvm3xj72X2qGiZFETulU7H1Fz4OEwviICiDgDEWwluevP0c5LpgS6FlZpvoI34bKfdV_ngABgnnkLP3toSWnCjcwnsfEV63iB3Tl75GSOx6fUsORRc3ZvbyJHm5unnUXRtXgxIVhSjDs8Lp1YNI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/21330" target="_blank">📅 22:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21329">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آغاز دوباره حملات موشکی و پهپادی سپاه به سمت کشتی ها در تنگه هرمز</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21329" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اظهارات جی.دی. ونس درباره رهبری ایران:
در ایران شما جناح‌های تندرو را دارید، محافظه‌کاران، میانه‌روها و روحانیون.
و همه این افراد در فرآیند تصمیم‌گیری نقش دارند.
و البته، رهبر عالی‌مقام جدید نیز حضور دارد اما بسیار منفعل است. او در امور روزمره دخالت نمی‌کند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/21328" target="_blank">📅 20:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اعزام دو اسکادران جدید جنگنده‌های F-22 ایالات متحده به اسرائیل
خبرگزاری‌های بین‌المللی و رسانه‌های عبری از جمله i24NEWS تایید کردند که ایالات متحده در یک حرکت بی‌سابقه، ۱۲ فروند جنگنده رادارگریز نسل پنجم F-22 Raptor را همراه با ده‌ها هواپیمای سوخت‌رسان پیشرفته (از جمله تانکرهای KC-46) در پایگاه‌های نظامی اسرائیل مستقر کرده است.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21327" target="_blank">📅 20:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21326">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21326" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">باز تنگه بندها ریختند تو فضای رسانه ای!  احمق های نفهم شما تنگه ترمز را ببندید اولا چین زیان سنگینی می‌دهد و شما را برای همیشه از فهرست متحدین خود حذف می‌کند و ثانیا دو هفته بعدش، جزایر سه گانه را از دست خواهیم داد.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/21325" target="_blank">📅 19:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21324">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درگیری مسلحانه میان شبه نظامیان بلوچ  و نیروهای نظامی در ایرانشهر</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/21324" target="_blank">📅 19:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">درگیری مسلحانه میان شبه نظامیان بلوچ  و نیروهای نظامی در ایرانشهر</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/21323" target="_blank">📅 19:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بهترین محدوده مقاومتی = 4169 الی 4175</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/21322" target="_blank">📅 19:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21321">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq6txJUk4fHGGq6aV6NalRTNGaAHy_z1DfCGcalvAa_s_2evUoIJ6Y20OHMCZpfHk0oKptU5RhW8DEwl593oMuCbDT9mHDCJ2GOJKQhLEXpYwwHjlku_tdKodoStO1cQ6dYYkRjq3BZX28YGkpPlCq3atrt9lWcN2wYPk_HWp0qj1jw-y6CUzEhclp92-Wgdd1wthV20Sec9Nyng9VrCrPgUQmP-SagGhsVuBi3QlyknHONQS20i-9lY7nMhIRpiBqzA98AR4LC7fvqmAJKbKCq7Kd6TsyrCp9nW3-3lQHoUhIQ7Pj3u8vhT1bE_H2yyKY7bczDLwZu4LE4vQ6IazQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
🥹
🥹</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/21321" target="_blank">📅 19:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سخنگوی ارتش ایران: اگر تشخیص دهیم که یک حمله دشمن قریب‌الوقوع است، قطعاً یک عملیات پیشگیرانه را انجام خواهیم داد. - خبرگزاری فارس.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/21320" target="_blank">📅 18:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: ایران به شدت در حال شکست است و به زودی از بین خواهد رفت. قیمت نفت به شدت کاهش خواهد یافت.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/21319" target="_blank">📅 18:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دیدار بن‌زاید و نتانیاهو در ابوظبی در قالبی «گسترده‌شده» برگزار شده که شامل کشورهای عربی دیگر و برخی کشورهایی که روابط رسمی با اسرائیل ندارند، بود.
بر اساس گزارش کانال ۱۴ اسرائیل، نمایندگان عربستان سعودی، مراکش، کویت، بحرین، لیبی (حفتر)، عمان و مصر نیز در این نشست که در روز یکشنبه برگزار شد، حضور داشتند.
نتانیاهو و بن‌زاید ابتدا به صورت خصوصی با یکدیگر دیدار کردند و سپس مقامات سایر کشورها به جلسه گسترده پیوستند.
بحث‌ها بر روی ایران، همکاری نزدیک‌تر بین اسرائیل و کشورهای خلیج فارس، مسائل اقتصادی و سیستم‌های دفاعی اسرائیل متمرکز بود.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/21318" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
اطلاع داریم که کشور های عربی حاشیه خلیج فارس با تأمین مالی آمریکا و اسرائیل برای جنگی تمام عیار علیه ایران موافقت کردند و در حال فشار به روی ترامپ برای آغاز هر چه سریعتر جنگ‌ می‌باشند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/21317" target="_blank">📅 17:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نامه سپاه پاسداران انقلاب اسلامی به مردم آمریکا
این دولت خودکامه، کودک‌کش، هوس‌باز و نادان را کنار بگذارید؛ امور خود را به اندیشمندان بسپارید، نه به زورگویان، و به آنها یادآوری کنید که جهان تغییر کرده است.
مردم جهان بیدار شده‌اند و دوران غارت ثروت ملت‌ها با زور و شمشیر به پایان رسیده است؛ این، قرن پیروزی اراده ملت‌ها است. ادامه دادن این مسیر غیرانسانی، سرنوشتی دردناک را برای آمریکا رقم خواهد زد، زیرا روزی که مستضعفان علیه ستمگر قیام کنند، بسیار وخیم‌تر از روزی خواهد بود که ستمگر علیه مستضعف عمل کرد.
هفت ماه پیش، ارتش متجاوز آمریکا —با نقض قوانین بین‌المللی و ارتکاب جنایت جنگی— جنگی علیه ایران آغاز کرد و با حمله به یک مدرسه ابتدایی در میناب، 168 دانش‌آموز را به قتل رساند، در حالی که همزمان به دفتر آیت‌الله سید علی خامنه‌ای، رهبر انقلاب اسلامی، نیز حمله کرد و ایشان و خانواده‌شان، از جمله نوه 14 ماهه ایشان، را به شهادت رساند. از آن زمان تاکنون، بیش از 3600 نفر —که بیشتر آنها غیرنظامی، از جمله 400 کودک— به شهادت رسیده‌اند، و هشت دانشگاه، سه بیمارستان و هشت مدرسه بمباران شده‌اند.
اگر در صحت گفته‌های ما تردید دارید، می‌توانید سفری کوتاه به هر نقطه از ایران که مایل هستید —حتی تنگه هرمز— داشته باشید تا از نزدیک صحت اظهارات ما را بررسی کنید.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21316" target="_blank">📅 15:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">علت تاخیر در ارسال GRI و FVC این بود که در نشست لایوی با نیما و امین و پیام بودم.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/21315" target="_blank">📅 15:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">#FairValueCurve  نمایه FVC اندکی از محدوده بیش—فروش فاصله گرفته اما حباب ندارد و کماکان زیر ارزش منصفانه است.  در این شرایط بهترین راهبرد، فروش در مقاومت ها است.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21314" target="_blank">📅 15:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW0mEMAR3IgNE0FIZzHl0I87p23Nmm-sqlUI7bVHzkfy2-iYlEyuWFzrdH_0qVpF2qbJPR3NtY9Olijf8Uy1nkFyCPqPKw5EOlXqio4iMX2NJOL7pDsaCByo2BbnRbdYCE2R7tv7W8Xf1gGYZMgaynC0O_-JC6BExYO-8CklWSPm_qsY0jnOEkH_FlMpzey8hAzf8ilG9u2tqrRSmPPWMB7Y5JSETQN-QsYHDmDJ6huX6Ap_dQcS--sHKpLtWvmK0gKeYUNVW2xYiDoFGsx0Hlc7xBpHR0iXbHMRXtC-il_TtV2PqkNh9IQAV4lj6jAQvrPC66zJhZ3OTdGoG8xoog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC اندکی از محدوده بیش—فروش فاصله گرفته اما حباب ندارد و کماکان زیر ارزش منصفانه است.
در این شرایط بهترین راهبرد، فروش در مقاومت ها است.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21313" target="_blank">📅 15:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoIzzbGl5WHKoBQ4h3jtv5wzsgAp32J0jy7PlValwrRrJzgO8CXC6r08pe4RasU0W-gy25eh4S20zN3cj-XFpCtF5FEQzt43-7evCO66opC6e_gDlONA5NmNpCgBY9Ar3HTGvttb4YX0kh4uG_RplqGhW8FkQVgJxC7yBT8vhKyA1T-FzDPjIX8G6Ep1AxZvVp6rzw39rpVTw9owVIom9VSS_ki-BAvvsDllFuKaUddxZ66ir3DFHGK70JFLd8YeaGHWVxWhDpNxzXJ71ujvLlI-mOc79hxNfTfncb8bCw1ulL3zqirv_Qp448i1RYO4TAiyFV-hqEkqfVOwtNxNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیکی + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و بالاهای طلا سل دارد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21312" target="_blank">📅 15:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21311">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn9E_vnE1xf-fMjJZ8PPla811EK0ER34Zcn1kMk4mYFigql5xUmLSYBRBYiDkqV3OfZt_En3EzDKO1RVJ35XRs_WvKonkg6t4PeTIETEwzm5TLRi-AiF97h4_dfvli-b8KaHd_W0Sz6j7cuRj565gfdfi8WMbc5t1Cmu53Qv0KDeQ8fn2RMJ3hpWZL1SRxqyC97XlrebAhDYldJuJwd-11Mxs6EECfGAKYyF1uOmMVrqHygypw-IFBR4lNGgTyfrzeOj4D9gUZS8xJp6Ifxiu6YjwV4GmiOwtjXhbN82YtyivawCZLvabi_ABZHoihkM_PBowKJpPr964VjREFzcSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش امت مبعوث به حکم حبس حاج آقا رسایی!</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21311" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21310">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">حبیب‌الله سیاری، معاون هماهنگ‌کننده ارتش:
مردم جنوب آماده باشند و اجازه ندهند دشمن وارد خاک کشور بشود</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/21310" target="_blank">📅 09:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21309">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تتر = ۲۵۰ هزار تومان!</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SBoxxx/21309" target="_blank">📅 08:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21308">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عراقچی: پاسخ آمریکا به تهران از طریق میانجیان قطری منتقل خواهد شد</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21308" target="_blank">📅 01:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نماینده امارات در مجمع عمومی سازمان ملل:
«امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و بوموسی توسط ایران است</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SBoxxx/21307" target="_blank">📅 01:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21306">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عراقچی: پاسخ آمریکا به تهران از طریق میانجیان قطری منتقل خواهد شد</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21306" target="_blank">📅 01:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21305">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزیر امور خارجه ایران: تهران پیشنهاداتی را با میانجیان قطری مورد بحث قرار داد تا به ایالات متحده ارائه دهد - ایرنا</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21305" target="_blank">📅 01:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21304">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگر عراقچی به تهران برگردد یعنی دیگر مذاکرات شکست کامل خورده</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21304" target="_blank">📅 01:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21303">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ اعلام کرد که گزارش Axios مبنی بر اینکه ترامپ پیشنهاد لغو تحریم‌ها را به ایران داده است، یک "دروغ" است.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21303" target="_blank">📅 01:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vsea13CIJLt0Xap-xb46ObjjuQzxGVNwiIERY2iXEaAgtq78tGZvaxYPK4Y0lVePwlrHQiO_WvwRjfBOKlTykf2JbWjQ-idIBzuKbTJnhc9vs0hJoy7k8zeQCQavg5hnZhE2a2H7oD_Dp8dsMhPDz6YTs1dKbd4gtAQ4qAEoEdZVBM_ZYorIn9bpyI1pipdZu7pILSOd83wMW096Ah6-uw9PHqgKusXn70S0kmfitvBEYL-57giTQF49jbBy7K9V0G-DyP44v7IW474RrRcmVBhnFjYuVPvCGYmizT9F5k3z5XP9epTGliH8Lkq-0FInZ1u6ByItUjh3__Xgxg3NiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدای کعبه سوگند که دروغ و فریبی بیش نیست! همه اش فریب و نیرنگ ترامپ است تا زمان بخرد و نیروهای بیشتری به منطقه بیاورد!  خواهیم دید چه خواهدشد!  عجالتاً طلایمان برگردد حالا خوب است</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21302" target="_blank">📅 01:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4jXdnjHJ_lAue9YGyaDMu9PRCCP0zF4n5Y3UcWJ54lmQdiwfxKfZ9r7T93RbSySFka6xuRwjYc4IbCYvEtkvC6RxSPUylUrOg-iG2nsPSkjhTOOiNpYaoUz4Y8Il0ma_MuXdFvJsrYKTkhdeP1Hc3xw0FT9RUnsibTuIMLjwQGD9AIXU4Pclyd5GFMNE_k5PnLnjLhRPeBaqAhEvKHs6i7j8ZF_52xStfhbjONVaikD3hQMw4Y-KDVI9NXiwlMe9Emi3ozPOK2Q7MXzuMNZmk42Ynu9XlapvJuHNDpugZ7lk3XyZ9xClCYE0l-aEvlZxphVQFhwgG_U-dSBNU3wvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   برای اولین بار موشک خاص و ضدناوشکن ایرانی آزمایش شد  ۴۸ ساعت پیش برای اولین بار موشک ضدناوشکن ایرانی را بالای سر یک ناو آمریکایی آزمایش کردیم.  این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21301" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ درباره ایران:  «آنها دیوانه هستند. هیچ شکی در این مورد وجود ندارد.»   «من همیشه به آنها می‌گویم: «شماها دیوانه هستید، آقایان.»»</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21300" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ درباره ایران:
«آنها دیوانه هستند. هیچ شکی در این مورد وجود ندارد.»
«من همیشه به آنها می‌گویم: «شماها دیوانه هستید، آقایان.»»</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21299" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:  فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.  بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21298" target="_blank">📅 22:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وِس استریتینگ.، وزیر دفاع بریتانیا، درباره جمهوري اسلامي ایران:
فکر می‌کنم حمایت از اقدامات دفاعی انجام شده توسط ایالات متحده درست بود.
بی‌شک درست است که بگوییم جنگ در ایران جنگی نبود که ما آن را انتخاب کرده باشیم. اما از سوی دیگر، هیچ شک و تردیدی هم وجود ندارد که ایران یک نیروی شرور است که بریتانیا، منافع ما و متحدان ما را تهدید می‌کند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21297" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">احتمالا امروز ترامپ خواهدگفت مذاکرات خوب پیش می رود</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21296" target="_blank">📅 21:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بخدای کعبه سوگند که دروغ و فریبی بیش نیست! همه اش فریب و نیرنگ ترامپ است تا زمان بخرد و نیروهای بیشتری به منطقه بیاورد!
خواهیم دید چه خواهدشد!
عجالتاً طلایمان برگردد حالا خوب است</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21295" target="_blank">📅 21:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ایران با توقف غنی سازی موافقت کرد!</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21294" target="_blank">📅 21:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRTy5eVz94rJ_mQIUfAAzwsBTXAoGhAExtHB_PCGvd5mA-IavvWXpknE-eKWRm3EpwSp_WAJPl8IeqniYPHETKhw13L1ngZiDGpVoNFFdGpXngFObnYMTgDtflCQ79CqIMvRdzzDnzgo_y2dIzMVRhVSCEi5nkYinY_9osxcrjHMKeadfR_3K5Nap-QCrWCVPXB6aymIR4kyuNcDyVXeqYkbjRgTEsHvGg4dZYUd0UVkzyS3s_VWmKXasyD8rKYmVakCYLfhIgJxXrOS6cUFagunvwIn6YxpqQmTnQj6ri5lGtatA-tel1myRnmOQupKJo0hC7gIHjlyHdSdCKI-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران ارزشی تازه دارند می فهمند چرا دکتر پزشکیان آن روز در سازمان ملل از ماتریکس خارج شده بود!
یا ذی الجلال و الاکرام!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21293" target="_blank">📅 20:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">در ۲۴ ساعت گذشته، دو اسکادران جنگنده آمریکایی به پایگاه هوایی اوودا نیروی هوایی اسرائیل در جنوب این کشور رسیدند و به نیروهای آمریکایی دیگری که از قبل در این کشور مستقر بودند، پیوستند.
مقامات امنیتی اسرائیل اعلام کردند که این استقرار بخشی از تحرکات گسترده‌تر نیروهای هوایی آمریکا در سراسر خاورمیانه است و نشان‌دهنده آمادگی بیشتر یا تشدید تنش با ایران نیست.
یک منبع امنیتی گفت که حضور نظامی فعلی آمریکا همچنان بسیار کمتر از سطح نیروهایی است که قبل از عملیات «خشم حماسی» (Operation Epic Fury) در این منطقه مستقر شده بودند.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21292" target="_blank">📅 20:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗
عربستان سعودی پس از تعمیرات، صادرات نفت خود را از طریق خط لوله شرقی-غربی از سر گرفته است</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21291" target="_blank">📅 20:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دیدید؟! این کله زرد حرامزاده را من بهتر از پدرانش میشناسم!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21290" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش‌ رسانه‌های عربی از شلیک موشک‌ از خاک ایران</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21289" target="_blank">📅 19:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترکیه یک هواپیمای ایرانی را به دلیل تحریم های آمریکا توقیف کرد.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21288" target="_blank">📅 19:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کار طلافروش آنلاین به شورای عالی امنیت ملی رسید  پلتفرم فروش آنلاین طلای میلی‌گلد در نامه‌ای به محسن رضایی، دبیر شورای عالی امنیت ملی، خواستار صدور دستور فوری برای رفع محدودیت دسترسی به طلای کاربران در خزانه‌های بانکی شده است.   این پلتفرم می‌گوید محدودیت‌های…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21287" target="_blank">📅 18:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ4M22qAnHQ_I-Xz43eeZX9vzTLkrC1peLMBAW6mCYj6RHl0su0wQyqnGRk6m_g3VbPlvf2Hk_V8zyS3NRqwmSmx4prQWhq--zxtxXtyP1mwoET7zaIb0UtRGKYS7VfWkDlDiqOAML76scME3b_cgBB5g0tVUs_V4T1mUbvR-e1_GB6DbWmFZlaf3PaYXaqBbnNEgCuC71m8cVPNijnC4326jsN4Jhhvsu2Qa865FkTVQDQ12cEIAPw-0MGPKUmGKvNrTUFX2_wpe8BxMMZji0x7UyYifay1_BHddVK2OoIljlUgoEr7HEeUG5isKk_7E6N7SvPRE1tILchQ071seg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
صادرات نفت خلیج فارس به ۸۰ درصد سطح پیش از جنگ رسید
🔹
خاویر بلاس مدعی شد: صادرات نفت خام عربستان، عراق، کویت، امارات، بحرین و قطر با کمک نیروی دریایی آمریکا، به ۸۰ درصد سطح پیش از جنگ بازگشته.
@khate_energy</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21286" target="_blank">📅 17:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21285" target="_blank">📅 17:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فوری | فرماندهی مرکزی آمریکا:   ایران کنترل تنگه هرمز را در دست ندارد؛ شواهدی مبنی بر عبور بیش از یک میلیارد بشکه نفت در طول چند ماه وجود دارد.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21284" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فوری | فرماندهی مرکزی آمریکا:   ایران کنترل تنگه هرمز را در دست ندارد؛ شواهدی مبنی بر عبور بیش از یک میلیارد بشکه نفت در طول چند ماه وجود دارد.</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21283" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:   دشمنان جرأت ورود به خلیج فارس را ندارند  رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.  او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21282" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هیچ کس را امین تُِن های ماهی تان قرار ندهید.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21281" target="_blank">📅 15:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21280" target="_blank">📅 15:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21279">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">طلا تارگت روز جمعه را زد (ما زودتر کلوز کرده بودیم)  امروز اما اندک اندک وقت خرید است و کل این مسیر ریزش را برخواهدگشت.  بازار جنگ را کامل دارد پیشخور می‌کند اما ناوهای هواپیمابر آمریکا هنوز نرسیده اند و آرایش جنگی تکمیل نشده و عباس آقا سعد اکبر هم هنوز برنگشته!…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21279" target="_blank">📅 15:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب شیشه — یدید پتاسیم — پنبه — روغن بنفشه</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21278" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب شیشه — یدید پتاسیم</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21277" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21276">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب شیشه — یدید پتاسیم</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21276" target="_blank">📅 14:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21275">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21275" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21274">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:   دشمنان جرأت ورود به خلیج فارس را ندارند  رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.  او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21274" target="_blank">📅 14:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21273">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پیام تند آیت الله خامنه‌ای:
دشمنان جرأت ورود به خلیج فارس را ندارند
رهبر جمهوری اسلامی ایران، در بیانیه‌ای اعلام کرد نیروهای دشمن جرأت ورود به خلیج فارس را ندارند.
او همچنین گفت دریای عرب به‌زودی از حضور «دشمنان» پاک خواهد شد.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21273" target="_blank">📅 14:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21272">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ایران شکایتی را علیه ایالات متحده به سازمان هواپیمایی ملل متحد (ایکائو) ارائه کرده است، به این دلیل که آمریکا محدودیت‌هایی را علیه شرکت‌های هواپیمایی این کشور اعمال کرده است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21272" target="_blank">📅 14:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21271">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عملاً همه دارند نفت صادر می کنند جز خودمان!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21271" target="_blank">📅 11:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21270">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔥
جریان ۱۲ میلیون بشکه‌ای نفت در کریدور عمانی
🔹
موسسه HFI: افزایش صادرات نفت عربستان از مسیر شرق می‌تواند جریان نفت در کریدور عمان را به ۱۲ میلیون بشکه در روز برساند که در نگاه اول می‌تواند نشانه عادی‌شدن تردد نفت در منطقه تلقی شود.
🔹
بخش قابل‌توجهی از نفت…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/21270" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgrTrubRzyKjV40xPFtyBv8_wHKajD3yMso-x9OtK4wCfyhLAqL9KbXNHTn-GVC9FZiqTgwaeS1d_1goNDCglI3z0FdDUt43HOZJurAD_v15DIZyxefk5Mf-pE9EbWvkYPLNmogIMufvcc7Z-75BxDt8mCYS7-qlvCLuSwarO0HqIaV-NdD2SJJVezLP1jDQ93XhMMyQzOtozznTHKLDcNkzRi30N1gv1GHvetVxyX7qt_nUwQ_WN8SQ-8oKw17ujDa6XQVH8IMaWlCSpcV3C3s_IAFtRzjwNRLxRS4Lnb8IBjcgI66fJrRp-PcMP_QfrRcvT_nLdPpUAtzOD3o_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جریان ۱۲ میلیون بشکه‌ای نفت در کریدور عمانی
🔹
موسسه HFI: افزایش صادرات نفت عربستان از مسیر شرق می‌تواند جریان نفت در کریدور عمان را به ۱۲ میلیون بشکه در روز برساند که در نگاه اول می‌تواند نشانه عادی‌شدن تردد نفت در منطقه تلقی شود.
🔹
بخش قابل‌توجهی از نفت عربستان در این جریان راهی چین می‌شود.
@khate_energy</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21269" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21268">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سراج، نماینده مجلس: حرف‌های عراقچی و پزشکیان درباره هسته ای و کوتاه آمدن از قصاص قاتلان رهبری بی‌اساس است و ربطی به سیاست جمهوری اسلامی ندارد
آمریکا می‌داند پزشکیان و عراقچی تصمیم‌گیر نیستند و محلی از اعراب ندارند
سخنان عراقچی صرفا اظهارنظرات خود اوست و هیچ اعتباری ندارد
اجرای انتقام و قصاص ربطی به دولت ندارد که نظر مثبت داشته باشد یا منفی
محمد سراج، نماینده تهران با اشاره به موضع گیری های مکرر پزشکیان و عراقچی درباره شرط ۷ روزه و باز کردن تنگه هرمز و رقیق سازی اورانیوم به دیده بان ایران گفت: « صحبت های آقایان عراقچی و پزشکیان در خصوص کوتاه آمدن از سیاست های نظام نظر شخصی بوده و نظر جمهوری اسلامی نیست. نظر جمهوری اسلامی ساز و کار خود را دارد و در سیاست کلان خارجی رهبری تعیین‌کننده هستند و در سایر موارد نیز مجلس و قانون مجلس مبنا قرار دارد. در حال حاضر محسن رضایی، دبیر شورای عالی‌ امنیت ملی سیاست کلان خارجی جمهوری اسلامی را بیان کرده است.»</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21268" target="_blank">📅 11:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21267">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">طلا تارگت روز جمعه را زد (ما زودتر کلوز کرده بودیم)  امروز اما اندک اندک وقت خرید است و کل این مسیر ریزش را برخواهدگشت.  بازار جنگ را کامل دارد پیشخور می‌کند اما ناوهای هواپیمابر آمریکا هنوز نرسیده اند و آرایش جنگی تکمیل نشده و عباس آقا سعد اکبر هم هنوز برنگشته!…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21267" target="_blank">📅 10:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21266">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmchzvAYEr41qtbsOPOKzn19VcaH7qZzNjXIh5mhArlnLps8OneNsu0LYj9mikGCZonlI5fbBy2s9qk2Mz3nRVZQpbuhGTuT-I_LMVr3Vjk57bPvEe7NLXruUpcHL7KlcQBBX9fqgIdMnaDLu6gefLH9xflIHm1b3GlnFU_pKF4PHw-QTHCAqKd2jwAuaMcuBhtD8GJPUfnf8EAinEjXLRESy95s-sevLXLHD99Wx14rwvkA5tsKEgziwEGAamT1CAmv8Qio9zWh9FhQGlkNzf2qOmUV6ceEGEh0cYOpEiAsMSSklPYLSR4FEXYyR8qq4PQd21ZRzHu3G0IHXrwcYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21266" target="_blank">📅 09:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21265">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZARaqlrQ8gLCeLsJVU6zDiikQLGKY4DMNYh4tBLn7Kv6P67BLJkR8xgJndZoThjCXukGG7KRdPE0HE-emH8WRN154T-ztLF5Vw_lz252aBk6i4GU9BbIp6PKJb4bwPDa57XrRWbvWiSrriaPdqIci4JglZoOn-hdK3VycYumfb0Ltt3GdZvwTWbfJZlgjbGirGseuVLNQ5zhAHftR1ykXD1zIk8LoIMXalrtJgJpRkKh4IwJodwgOhygL1NlFf_DnpE-rDvDiFaUYwVtWTlC_Du7NUEAnQHDre9oi1pNPv_uAucYT5_7nMUNypfWJnzMYLvWGZtC0WfeOrQsqN8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نیز به کف محدوده بیش—فروش رسیده و خرید توصیه می کند.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21265" target="_blank">📅 09:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21264">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCrrk7W8ObVartyoZ5edxoQrsXbA7ufUd-V9xZS7DcC-aWXVea_nnwVR7gxG8XvliCWi0XDH4wYDyc1SNeztlmebvudxo5JwUhIld0RmCo1eYjVrSFdsXN4wZzfjpIz0UOpIhxV8zlzYPya2BCwyJPghYwwZL96WlZN9IiTRqsbZdF6uwA_gz2HLMe8DK7axfHzgQghwwRemtlqgRtzR42uslgX3yAqI0j5zs7rY4tQNPtEPI4rWWrLvP4ioc5TWCujODUFtuUMn3-3DQy07Qu_U05I5mnhQAfz6IxqlwJ7PN53-bGKzmhyfNHpoTEZmc1iE-s5bO7nb1VzNV-zqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی است و از دید این شاخص، واکنش بازار به تنشهای هرمز مقداری افراطی بوده است.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/21264" target="_blank">📅 09:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21263">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B74ja7gHGFxvBsKwrsR5cvrh6dzofn1EOkyLnhPY9oxy6vtLl5jg6-2Lcx6OXftbUEf5pys1p2Z_juRQ_aXE2V5lXVMtYLbZ4kjVEXdLL8CsRtkKXf3F0fMQt8QC8DRqQmlqSkniowWwWJc1MWcbGxUBUYa2o8jZDKuwyhe0bcNfqp8nGxkyPe3t9SgYIgfvrh5ayAA4bfevUWSwWRZyh3eqCwugC7vYP-SSPOW_KGEKezI4nR1PhFA42lGutbfDTaA_g6w_kjGZvDVoOqH223kT6rPdwpesBJ9sBR8heS7v5qVbs3vZyR_6MsmqI6e21CxaFfI-Ry_Rjw5_Km7o6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ژاپن بزودی بدجور موی دماغ چین خواهدشد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/21263" target="_blank">📅 08:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21262">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جنگ ایران و بن‌بست فزاینده آمریکا؛ از بحران انرژی تا تغییر موازنه خلیج فارس
بر اساس دیدگاه‌های مطرح‌شده توسط جان مرشایمر نویسنده پرآوازه کتابها و مقالات ژئوپولیتیک، جنگ ایران و آمریکا وارد مرحله‌ای از بن‌بست شده است. از نگاه او، آمریکا تاکنون به اهداف اولیه خود دست نیافته و در عین حال ایران نیز حاضر نیست بدون دریافت امتیازات قابل‌توجه از جنگ خارج شود. تهران به‌جای تلاش برای شکست نظامی آمریکا، به دنبال افزایش هزینه‌های جنگ و فرسایش توان اقتصادی و سیاسی واشنگتن است؛ به بیان ساده‌تر، راهبرد ایران «دوام آوردن تا فرسوده شدن طرف مقابل» است.
یکی از مهم‌ترین اهرم‌های ایران، موقعیت آن در تنگه هرمز و پیوند آن با تحولات دریای سرخ و باب‌المندب است. اختلال در مسیرهای اصلی انرژی باعث افزایش قیمت نفت، سوخت، حمل‌ونقل و مواد غذایی شده و فشار تورمی را به اقتصاد جهانی منتقل کرده است. هم‌زمان، جنگ میان حوثی‌ها و عربستان نیز جریان صادرات نفت عربستان از مسیر دریای سرخ را با اختلال مواجه کرده است. مرشایمر می‌گوید ظرفیت عملی خط لوله عربستان به دریای سرخ پیش از حملات حدود ۴ میلیون بشکه در روز بود، اما پس از آسیب به ایستگاه‌های پمپاژ، جریان آن به حدود ۱.۶ میلیون بشکه در روز کاهش یافته است.
این وضعیت برای اروپا اهمیت ویژه‌ای دارد، زیرا هم‌زمان با کاهش عرضه نفت، بازار جهانی گازوییل نیز تحت فشار قرار گرفته است. روسیه صادرات گازوییل خود را محدود کرده و آمریکا نیز درباره محدود کردن صادرات گازوییل بحث می‌کند. از دید مرشایمر، تداوم این روند می‌تواند فشار قابل‌توجهی بر اقتصاد اروپا و اقتصاد جهانی وارد کند.
محدودیت گزینه‌های نظامی آمریکا
مرشایمر معتقد است آمریکا گزینه نظامی مؤثری برای دستیابی به پیروزی در ایران در اختیار ندارد. به گفته او، جنگ هوایی اولیه که از ۲۸ فوریه تا ۸ آوریل ادامه داشت نتوانست اهداف آمریکا را محقق کند و یکی از محدودیت‌های مهم واشنگتن، کاهش ذخایر تسلیحات پیشرفته و گران‌قیمت است. بنابراین، تهدید به حمله گسترده پس از انتخابات میان‌دوره‌ای لزوماً به معنای وجود یک راهبرد جدید برای پیروزی نیست.
همین محدودیت درباره حوثی‌ها نیز مطرح است. عربستان چند بار از ترامپ درخواست کمک کرده، اما آمریکا از ورود مجدد به جنگ با حوثی‌ها خودداری کرده است. استدلال اصلی این است که چنین جنگی می‌تواند منابع تسلیحاتی محدود آمریکا را مصرف کند، بدون آنکه تضمینی برای دستیابی به یک پیروزی پایدار وجود داشته باشد.
فشار اقتصادی و راهبرد تحریم‌ها
راهبرد اقتصادی آمریکا برای تحت فشار قرار دادن ایران نیز، از نگاه مرشایمر، با محدودیت روبه‌رو شده است. طرح وزیر خزانه‌داری آمریکا، اسکات بسنت، بر تشدید فشار اقتصادی و اعمال تحریم‌های ثانویه علیه کشورهایی استوار است که با ایران تجارت می‌کنند. اما چین، روسیه، ترکیه و امارات حاضر نیستند به‌طور کامل از تجارت با ایران خارج شوند. بنابراین، ایجاد یک محاصره اقتصادی کامل بسیار دشوار است.
چین در این میان نقش کلیدی دارد. طبق ادعاهای مطرح‌شده در مصاحبه مرشمایر، چین بخش بزرگی از نفت ایران را خریداری می‌کند و از طریق شبکه‌های تجاری و مالی به تهران کمک می‌کند فشار تحریم‌ها را دور بزند. همچنین ادعا شده است که چین در زمینه تجهیزات نظامی و ارتقای توان پهپادی و موشکی ایران نیز کمک‌هایی ارائه کرده است.
در نتیجه، فشار آمریکا علیه ایران صرفاً یک رویارویی دوجانبه نیست و به رقابت گسترده‌تری میان آمریکا، از یک سو، و ایران، چین و روسیه از سوی دیگر تبدیل شده است.
نفت و خطر تشدید بحران جهانی
یکی از نگرانی‌های اصلی، کاهش توان اقتصاد جهانی برای جذب شوک نفتی است. ذخایر استراتژیک نفت آمریکا در این مصاحبه حدود ۲۸۵ میلیون بشکه عنوان شده و کاهش بیشتر آن می‌تواند توان واشنگتن برای مقابله با شوک‌های بعدی را محدود کند. چین نیز که در آغاز جنگ واردات نفت خود را به‌شدت کاهش داده بود، اکنون دوباره واردات خود را افزایش داده است؛ بنابراین یکی از مکانیسم‌های اولیه برای کاهش فشار بازار نفت در حال ضعیف شدن است.
اگر صادرات عربستان نیز همچنان مختل شود، فشار بر بازار جهانی نفت می‌تواند بیشتر شود. در چنین شرایطی، اثرات جنگ دیگر محدود به ایران و آمریکا نخواهد بود و می‌تواند از طریق انرژی، تورم، زنجیره تأمین و هزینه حمل‌ونقل به اقتصادهای مختلف منتقل شود.
مرشایمر هشدار می‌دهد که در صورت ادامه جنگ، خطر رکود شدید جهانی افزایش می‌یابد؛ هرچند خودش تأکید می‌کند که نمی‌تواند با قطعیت پیش‌بینی کند بحران تا چه اندازه عمیق خواهد شد یا آیا به یک رکود جهانی بسیار طولانی منجر خواهد شد.
تغییر محاسبات کشورهای خلیج فارس
یکی از پیامدهای مهم جنگ می‌تواند تغییر محاسبات امنیتی کشورهای عربی خلیج فارس باشد. اگر این کشورها به این نتیجه برسند که آمریکا در شرایط بحرانی حاضر نیست مستقیماً از آنها دفاع کند، ممکن است به دنبال ترتیبات امنیتی مستقل‌تر بروند.
مرشایمر معتقد است عربستان و سایر کشورهای خلیج فارس ممکن است به سمت نوعی تفاهم با ایران حرکت کنند، زیرا اتکا به آمریکا، پاکستان یا ترکیه الزاماً نمی‌تواند یک چتر امنیتی پایدار ایجاد کند. در این چارچوب، کاهش تنش مستقیم میان ایران و کشورهای عربی می‌تواند به یکی از گزینه‌های مهم آینده تبدیل شود.
خطر مسابقه هسته‌ای منطقه‌ای
یکی از مهم‌ترین پیامدهای بلندمدت جنگ، از دید مرشایمر، افزایش انگیزه کشورهای منطقه برای دستیابی به بازدارندگی هسته‌ای است.
در این تحلیل، اگر ایران به این نتیجه برسد که سلاح هسته‌ای تنها راه تضمین بقای حکومت و جلوگیری از حملات آینده است، فشار برای حرکت در این مسیر افزایش می‌یابد. همین منطق می‌تواند عربستان را نیز به دنبال کردن یک گزینه هسته‌ای سوق دهد و در مرحله بعد کشورهای دیگری مانند ترکیه، مصر و عراق را نیز تحت تأثیر قرار دهد.
این مسئله یک تناقض مهم ایجاد می‌کند: جنگی که هدف یکی از طرف‌های آن جلوگیری از دستیابی ایران به توانمندی هسته‌ای بوده، ممکن است در صورت شکست مذاکرات، انگیزه ایران و حتی سایر کشورهای منطقه برای دستیابی به بازدارندگی هسته‌ای را افزایش دهد.
پیامدها برای اسرائیل
در این روایت، جنگ الزاماً به تحقق اهداف اسرائیل نیز منجر نشده است. یکی از نگرانی‌های اصلی اسرائیل، جلوگیری از دستیابی ایران به سلاح هسته‌ای بوده است؛ اما ادامه جنگ و فروپاشی مسیر مذاکرات هسته‌ای می‌تواند احتمال دستیابی ایران به چنین ظرفیتی را افزایش دهد.
هم‌زمان، توان موشکی و پهپادی ایران به‌عنوان یک تهدید مهم برای اسرائیل و کشورهای خلیج فارس مطرح شده است. همچنین جنگ نتوانسته پیوند ایران با گروه‌های متحد منطقه‌ای خود را از بین ببرد و حتی از دید مرشایمر ممکن است این پیوندها را تقویت کرده باشد.
جمع‌بندی
تصویر کلی ارائه‌شده در این مصاحبه، جنگ ایران را نبردی می‌داند که در آن مسئله اصلی دیگر صرفاً توان نظامی نیست؛ بلکه زمان، انرژی، اقتصاد، ذخایر تسلیحاتی، انسجام ائتلاف‌ها و تحمل سیاسی به عناصر اصلی قدرت تبدیل شده‌اند.
در این چارچوب، آمریکا با سه مشکل هم‌زمان مواجه است: دشواری دستیابی به پیروزی نظامی، محدودیت در ایجاد محاصره اقتصادی مؤثر و افزایش هزینه‌های جهانی جنگ. در مقابل، ایران می‌تواند از موقعیت جغرافیایی خود، به‌ویژه در ارتباط با هرمز، و از حمایت یا همکاری چین و روسیه برای افزایش قدرت چانه‌زنی خود استفاده کند.
اگر جنگ ادامه پیدا کند، مسئله فقط آینده ایران و آمریکا نخواهد بود. بازار جهانی انرژی، اقتصاد اروپا و آسیا، امنیت کشورهای خلیج فارس، روابط آمریکا با متحدانش و حتی آینده رژیم منع اشاعه هسته‌ای در خاورمیانه می‌تواند تحت تأثیر قرار گیرد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/21262" target="_blank">📅 08:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21261">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتجارت کشاورزی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zarrrg1dtDdgVz15w0Jr7fwE8JVWeiMx1EdpXUcvhGY-Vqi05evfnK5llId92t9i6tk4ZpdUha5FO9mvzQL0Ra3Hp9c4YiZ0UbK_JudHE3csOEGSLXRmsWST6zkzJQrS-SKBPcKOvjKCHbdpfyxf4sZG1w7qCJ2W0dyYVXatml4BPgRkkbJyo7C294e6Gs62ChRf7eh4T9Gq8bOXIu1ekKc-st02_cjeb-jJEnpKKfhjfPB_mRBorfnRwZxP92NBe1HYwsD3FvRP_TTjP88wyEa10gHCs7HrMgDPD72kFVbTy7z4244T_TGCPJxKEkg2unv1W_P9AcTMISn0docpqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغیه دولتی
به اطلاع کلیه بازرگانان محترم می رساند
دولت الزیدی تا پایان هفته آینده مهلت داده است تا کالاهای وارداتی جمهوری اسلامی ایران به بازار عراق انتقال یابند.
پس از انقضای این مهلت صرفاً دو گزینه در دسترس خواهد بود ۱-پرداخت مالیات مضاعف بر کالاهای مذکور
۲- منع كامل ورود کالاهای ایرانی به خاک عراق
⚠️
این تصمیم در راستای اجرای مفاد مشارکت جمهوری عراق در تحریمهای ایالات متحده آمریکا علیه جمهوری اسلامی ایران اتخاذ گردیده است.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/21261" target="_blank">📅 08:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21260">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.  در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21260" target="_blank">📅 07:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21259">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پنتاگون مصدوم شدن ۸ تفنگدار دریایی آمریکا در حمله موشکی ایران را پنهان کرد
به گزارش NBC News به نقل از ۳ مقام آمریکایی، ۲ هفته پیش زمانی که یک موشک کروز ایرانی به شناوری که تفنگداران دریایی آمریکا در تنگه هرمز در آن مشغول به کار بودند اصابت کرد، ۸ تفنگدار دریایی مجروح شدند.
وزارت دفاع هیچ حمله‌ای در تاریخ ۱۴ سپتامبر علیه نیروهای آمریکایی در منطقه را فاش نکرده بود.
موشک کروز ضدکشتی ایران به شناور دریایی که تفنگداران دریایی در آن مستقر بودند اصابت کرد
🔴
تفنگداران دریایی — ۷ سرباز و ۱ افسر — دچار استنشاق دود و احتمالاً آسیب‌های تروماتیک مغزی شدند که علائم ضربه مغزی از جمله سردرد را شامل می‌شد. آن‌ها بخشی از یک تیم پیاده‌سازی گردانی بودند
مقامات از تعریف نوع کشتی خودداری کرده و آن را تنها یک «شناور دریایی» نامیدند
در حالی که ایالات متحده در حال خارج کردن دارایی‌های خود است و ذخایرش بیشتر تخلیه می‌شود، گزارش‌های مربوط به تلفات آمریکایی‌ها همچنان ظاهر می‌شوند — و همچنان کمتر از مقدار واقعی گزارش می‌گردند.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21259" target="_blank">📅 07:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21258">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار دوباره نزدیک ۲۴۰</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21258" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21257">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار CBS:   مذاکرات روز دوشنبه بین ایران و آمریکا لغو شد  مارگارت برنان، خبرنگار سی‌بی‌اس نوشت: یک دیپلمات که در جریان مذاکرات قرار دارد به من گفت آمریکا روز پنجشنبه پیش‌نویس ایران را بررسی و آن را همراه با بازخورد و ملاحظات خود بازگردانده است.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21257" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21256">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خبرنگار CBS:
مذاکرات روز دوشنبه بین ایران و آمریکا لغو شد
مارگارت برنان، خبرنگار سی‌بی‌اس نوشت: یک دیپلمات که در جریان مذاکرات قرار دارد به من گفت آمریکا روز پنجشنبه پیش‌نویس ایران را بررسی و آن را همراه با بازخورد و ملاحظات خود بازگردانده است.</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SBoxxx/21256" target="_blank">📅 22:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21255">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بنیامین نتانیاهو دستور داده است که یک تیم بین‌وزارتی و مقامات حقوقی پرونده‌ای علیه رجب طیب اردوغان، رئیس‌جمهور ترکیه، در دادگاه کیفری بین‌المللی (ICC) آماده کنند.
پرونده پیشنهادی عمدتاً بر «رفتار ترکیه با جمعیت کرد خود» و ادعاها مبنی بر اینکه دولت اردوغان حماس را تأمین مالی کرده، تمرکز خواهد داشت.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21255" target="_blank">📅 21:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21254">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21254" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21253">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عراقچی:  ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SBoxxx/21253" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21252">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">عراقچی:
ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21252" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21251">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پلیس ضدتروریسم بریتانیا در حال بررسی این موضوع است که آیا ایران با طرح ناکام‌مانده حمله به پایگاه هوایی در پایگاه نیروی هوایی سلطنتی فیرفورد (RAF Fairford) ارتباط دارد یا نه.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21251" target="_blank">📅 19:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21250">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=Nu4gLMRZQb_T59BTuI6apf7y5jGHPbSeW3CCiKPFcm2XOSfm9idP1Ky1vrHhdUXOtRCGVoTKqiXxNJ3zDyw6usMnknAKiNx2zoYWjSPlt0Ln25q6_9k90BAeGgyRikWGqZm6nI5S0tDUM36uIkLPeis4tf_pBS-NdxNT1bnrW4VJBAFCrS71R743xS50FC4QxBD9C1zv-QiZSWNSkyFbPc-LR-UaWX1YjuDU_NeZDXNWP19j9uM9eD6aLjgp5j1-yNL27szrfzY-H-6sDwr2Ej3-OKi6KYK_Z95XWRlf5pSGgY7bBEDduQzkfOx52RfWTrFjCsMldXqeC20e6yKlew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=Nu4gLMRZQb_T59BTuI6apf7y5jGHPbSeW3CCiKPFcm2XOSfm9idP1Ky1vrHhdUXOtRCGVoTKqiXxNJ3zDyw6usMnknAKiNx2zoYWjSPlt0Ln25q6_9k90BAeGgyRikWGqZm6nI5S0tDUM36uIkLPeis4tf_pBS-NdxNT1bnrW4VJBAFCrS71R743xS50FC4QxBD9C1zv-QiZSWNSkyFbPc-LR-UaWX1YjuDU_NeZDXNWP19j9uM9eD6aLjgp5j1-yNL27szrfzY-H-6sDwr2Ej3-OKi6KYK_Z95XWRlf5pSGgY7bBEDduQzkfOx52RfWTrFjCsMldXqeC20e6yKlew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21250" target="_blank">📅 19:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21249">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kahFnY4_Wr6kim2Ww9ibX7KUljExJxpXbeo4OZXCi25n_1k72I6biptDFvj45V7S9pgSSW4y-EjFZUxlnMUnUOV06uUVSiXjcb5lUzontPKM8InDxn_bJ89thjM_ACIM55vTI0vXUOQVDDmqMS7ZiAQMvy83lz1XOGCAYVzftew6g96l6HhJ89poOiiAbwxTvvXw2XBRBh0V_d4T_Q16VKDxae50DesWIcZowqR4I1LFQyk9nrcJtwuRFAnysWQ01cV8724VOncoAIc7RREorACkX0tdD5q9f-nERjuMvNrCY8qJJXMYmEXyW3BTtvUD8MIKg9icBwHlQ_3aFgpI6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21249" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21248">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21248" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21247">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حرف درستی است. به این پفیوزها گاز و برق ندهید دستکم خودمان اینقدر قطعی نداشته باشیم.
زیبنده ابرقدرت چهارم دنیا نیست.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21247" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21246">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXVfDaFH1KKvGATiDYh_N-TWDGSx7qLUsaWO-XZskqysTFSTOIbqKxtSeAqwESOCvtU6UGfdUFoCoQKXVz4e608WJnZCf34V7K9dOfL9SttwFaKZT_8AHQcOZPGeTjCYqnx5UXU4fx1BpwWkNEsGYNUBgAdK-hPH46H8x5PIXh8Zbjs_eGsfoU1_UlnDYytAJeJJgeTRB8FzCJ3AZg8LKmYnELhiDt6nhuhmHIlaV97q5Bx_M4GgmNLfeR5lGP3QJwrXyOCpdPBuT2QznmBTSc91HawPruL151iS1Z8SOQ-nYI1ljiCjCLgxzu_7Oxy_oAYf8FrvWEibSM8WJsuY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران امروز مدعی شد که یک پهپاد زیرآبی خودکار ساخت آمریکا به نام Remus 600 را در نزدیکی تنگه هرمز به دست آورده است. نام‌گذاری نظامی این وسیله توسط ارتش آمریکا، Mk 18 Mod 2 Kingfish است.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21246" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21245">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رابرت کیوساکی (Robert Kiyosaki)، نویسنده کتاب «پدر پولدار، پدر بی‌پول»، به دارندگان حساب‌های بازنشستگی هشدار داد که ممکن است فروپاشی‌ای در مقیاس سال ۱۹۲۹ در راه باشد، و بیش از یک سال بعد، این فروپاشی رخ نداده است.
کیوساکی در ژوئیه ۲۰۲۵ در ایکس نوشت: «آیا حساب 401(k) یا IRA دارید که پر از سهام است؟» او به وارن بافت (Warren Buffett)، رئیس برکشایر هاتاوی (Berkshire Hathaway)، و جیم راجرز (Jim Rogers)، هم‌بنیان‌گذار صندوق کوانتوم (Quantum Fund)، اشاره کرد و مدعی شد آن‌ها بیشتر یا همه سهام و اوراق قرضه خود را فروخته‌اند و پول نقد یا نقره نگه می‌دارند. او افزود: «اگر نمی‌دانید چرا بافت و راجرز سهام و اوراق قرضه‌شان را فروخته‌اند، ممکن است بخواهید علتش را بفهمید.»
او جایگاه خود را متفاوت توصیف کرد. کیوساکی نوشت: «من محکم روی طلا، نقره و بیت‌کوین می‌نشینم» و سپس افزود: «ممکن است در آستانه فروپاشی دیگری مانند ۱۹۲۹ و رکود بزرگ دیگری باشیم.» او همچنین هشدار داد که بدهی آمریکا از کنترل خارج شده است و این کشور فقط «تا مدت محدودی» می‌تواند به چاپ پول ادامه دهد.
البته این پیش‌بینی محقق نشده است. شاخص S&P 500 به صعود خود ادامه داده و در سال ۲۰۲۶ به بالاترین سطح تاریخی رسیده است، نه اینکه فرو بپاشد.
کیوساکی همچنان درباره سهام، صندوق‌های قابل معامله در بورس (ETF)، صندوق‌های سرمایه‌گذاری مشترک، حساب‌های 401(k) و IRA هشدار می‌دهد و در همان حال طلا، نقره و بیت‌کوین را تبلیغ می‌کند. استدلال اصلی او ثابت مانده است: سرمایه‌گذاران نباید صرفاً به این دلیل که دارایی‌های سنتی آشنا هستند، فرض کنند که امن‌اند.
تمایز مهم، میان آماده شدن برای یک رکود و تلاش برای زمان‌بندی دقیق وقوع آن است.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21245" target="_blank">📅 19:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21244">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caFhtzKolnmSrq5u0VXtyb9-blzYB0W1xeN1E3Qf3y4jRKDdItf7gAxL5iCA50WiCCWMt4EBS_zuCNzkF_HXuGW7aNNgDoLisrY3ovhDMAUOL2bz7KzFIA28iQQeIF-6ubSrWJfPcNa6caJIg1vUPSshzI6iWL1LczIh9p72rWOUWWj8M1hNc1hgSDsP_qI7VcdmwMBiNeni0qVQDeNvgK0TFmDtO6_ZKoYMrVPOHBPhWRXH5no0NdUh0OzfE0_AwR36My3wKR0pAMf2DA2T98FugmveT0kO7Blozf7TDCWlgoMWR4CaGdgbczAvTPD5EjixTBZ4NWJxiBWCe1DvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SBoxxx/21244" target="_blank">📅 17:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:  ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس  نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21243" target="_blank">📅 13:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:
ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس
نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در آن غرق شد؟ آیا آمریکا در منطقه و در تنگه هرمز در نبرد با ملتی که خدایی فکر می‌کند و توحیدی فکر می‌کند غرق نخواهد شد؟ دیپلماسی با قدرت امکان‌پذیر است و ما باید حرفمان را از قدرت و اقتدار و جایگاه قدرت اقتدار بزنیم.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21242" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">باز هم تاکید میکنم خواهرمیانه جای مبتدی ها نیست :
حکم ۱۰ ماه زندان حمید رسایی اجرا می‌شود</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21241" target="_blank">📅 12:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm0NKigwUzffuC-2DG1yympaag6B1mqATYVdymeXH3w_MP6PuNei5B0s6WiGT7hWpv5ekos5_7LHn6G9834CewtGyKTxIL0kXchYc3hQ9AdPDwVBvdK_qV6wiDxr-PeZ1FaCFhszAnIXowbO4vAt9dDm61j8ulXb6G9VV9zZASNkP_Ljv8z9dzJq3ZnHL4CFDMtS00YV_oVhliBnJgxJmnMNsbe00mxnd8vNnRHTKH2zCYBEA1HvTp-Fo3ilryeI5j03vXaDqySKhRQpGra5NDHLhro5N8a_HhrpKJJxlIvD0__OlPSNO2oNjwEUtcNDRa-vSW91S_kx3JFFULcORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهرمیانه برای مبتدی ها نیست!</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/21240" target="_blank">📅 12:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21239" target="_blank">📅 10:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سپاه
پاسداران:
در یکی از بزرگترین عملیات‌ها  دقایقی پیش 7 نفتکش اماراتی در تنگه هرمز مورد هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SBoxxx/21238" target="_blank">📅 09:15 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
