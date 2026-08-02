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
<img src="https://cdn4.telesco.pe/file/DMbufwhNWVs3kY7FiJwsPL0X2BHS37_PSpRVEIegdQ4-vah5PTwd60Jo7BJUM3kOUUvZWwzEWfsehRi1krhM2UhcbM7YAvVuJPLNaXoiBA36D6J_GzTFJVkyKkxNpK-ECQnvBRMAxU9MbesR4Y6SjMUBebwVj7ADjPL12um68FQ3u0p6bpO3dcCfddelBo-MHKn_fea__-HMTgvbR5mTbauUwb3lgulNlcrFRxOehSqQdVshzhTI3gRlyvyYv079jyPZxdeYvw4nPI0EAdgEt9DMhv14Fq0iL1uMaan-xytx3QW56RiQxyi5cjJN3I5PsNge08GR41_1PksoyvtJ9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 990K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 20:19:35</div>
<hr>

<div class="tg-post" id="msg-139440">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت خارجه : در حال حاضر با عمان درباره مسیری برای عبور در تنگه هرمز گفتگو می‌کنیم که نه مسیر شمالی باشد و نه مسیر جنوبی.
🔴
واشنگتن اجازه نداد حرکت کشتی‌ها در هرمز طی مدت مقرر از سر گرفته شود و پیش از پایان آن، به ما حمله کرد
🔴
مکالمات آقای عراقچی با مسئولان پاکستان و ترکیه هشدار و تهدید آمریکایی‌ها به پاسخ متقابل درصورت اقدام علیه ایران بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/139440" target="_blank">📅 20:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139439">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: همۀ دوستان و همسایگان باید بدانند که تبعات هرگونه حملۀ آمریکا به زیرساخت‌های ایران، دامن همه را خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/139439" target="_blank">📅 20:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139438">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
عراقچی: مذاکرات ایران و عمان در مسیر نهایی شدن قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/139438" target="_blank">📅 20:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139437">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552a5e4a47.mp4?token=gibq9JVfhy6cZJ9U_dEXy_SIU9U6j0Kt8S-S0jjXFOwkjHhMGzKKln2JIkoVUFUQ7A8rzqBV_rSjzOMclUMgIADKJ7INS-uj44qBk17oc-vCOu7aNhUNo11KH9D-N4eDffhrunLnSERtATEuXnvHuJblkizvNhHpiAREBqbjaI-YYyFYF0YKoh14gwiOx8WvBsTYxYAYiXJ_bkfk473KtKRBCx9k7mmB5neYSX_0vuJWlyWtBr6ijwLGMmZ8ymSAuzlhs4FamX5nALZp9BcfIVHaywZ10FIrc0rGX7Y03oRRxdBzq92xIzvDnG8OctpN1qOKxBpq-BXK51miU4H3pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552a5e4a47.mp4?token=gibq9JVfhy6cZJ9U_dEXy_SIU9U6j0Kt8S-S0jjXFOwkjHhMGzKKln2JIkoVUFUQ7A8rzqBV_rSjzOMclUMgIADKJ7INS-uj44qBk17oc-vCOu7aNhUNo11KH9D-N4eDffhrunLnSERtATEuXnvHuJblkizvNhHpiAREBqbjaI-YYyFYF0YKoh14gwiOx8WvBsTYxYAYiXJ_bkfk473KtKRBCx9k7mmB5neYSX_0vuJWlyWtBr6ijwLGMmZ8ymSAuzlhs4FamX5nALZp9BcfIVHaywZ10FIrc0rGX7Y03oRRxdBzq92xIzvDnG8OctpN1qOKxBpq-BXK51miU4H3pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر زلنسکی: امروز صبح در روسیه، به یک پالایشگاه نفت، یک پایگاه هوایی نظامی، یه مخزن ذخیره نفت و مکانی که برای ذخیره، آماده‌سازی و پرتاب پهپادهای تهاجمی استفاده میشد، حملات سنگینی رو انجام دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/139437" target="_blank">📅 20:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139436">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش در تنگه هرمز مورد اصابت موشک یا پهپاد قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/139436" target="_blank">📅 19:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139435">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت دفاع ایتالیا اعلام کرد یک نیروی نظامی مشترک اروپایی یک نفتکش ناوگان سایه روسیه را رهگیری و متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/139435" target="_blank">📅 19:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139434">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
جروزالم پست: امریکن ایرلاینز پروازهای نیویورک به اسرائیل را تا مارس ۲۰۲۷ لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/139434" target="_blank">📅 19:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139433">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
حمله انتحاری در شمال پاکستان ۷ کشته برجا گذاشت
‏
🔴
پلیس پاکستان: در جریان حمله‌ای انتحاری در حاشیه تظاهراتی در شمال این کشور، دست‌کم ۷ نفر کشته شدند.
‏
🔴
تاکنون جزئیات بیشتری درباره هویت عامل انتحاری یا شمار مجروحان منتشر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/139433" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139432">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ اگر فورا پیشرفتی در مذاکرات و توافق نبینه، میتونه هر لحظه عملیات علیه ایران رو آغاز کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/139432" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139431">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دیپلمات ارشد ایرانی به وال استریت ژورنال:
ایران در حال بررسی حملات موشکی پیش‌دستانه به پایگاه های آمریکاست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/139431" target="_blank">📅 19:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139430">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سنتکام: از زمان ازسرگیری محاصره بنادر ایران، مسیر حرکت 35 کشتی تغییر داده شده و 2 کشتی نیز از ادامه فعالیت بازمانده‌ اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/139430" target="_blank">📅 19:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139429">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کانال i24 عبری:
اختلاف و ناامیدی کشورهای خلیج فارس از ترامپ، دلیل لغو حمله شبانه به ایران
🔴
تحولات اخیر، اختلافات فزاینده بین کشورهای خلیج فارس و دولت آمریکا را در مورد نحوه برخورد با تنش‌ها با ایران آشکار کرد، در حالی که احساس ناامیدی از مواضع ترامپ در بین کشورهای منطقه در حال افزایش است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/139429" target="_blank">📅 18:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139428">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
کانال 12 اسرائیل:
مقامات اسرائیلی خودشونم از پست تروث سوشال ترامپ متوجه لغو عملیات شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/139428" target="_blank">📅 18:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139427">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
احمدرضا رادان، فرمانده کل نیروی انتظامی:
من یه مشکلی برام پیش اومد که گفتم نمیتونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/139427" target="_blank">📅 18:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
مقامات جمهوری اسلامی به روزنامه "وال استریت ژورنال"
:
"ما در حال بررسی گزینه حمله هستیم، اگر دیپلماسی شکست بخورد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139425" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139424">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وال استریت ژورنال:
رئیس جمهور ترامپ، حمله برنامه‌ریزی شده به ایران را لغو کرد، پس از آنکه نمایندگان مذاکره‌کننده ایرانی (عراقچی) به پیشنهاد جدیدی از سوی قطر مبنی بر باز شدن تنگه هرمز پاسخ مثبت دادند. مشخص نیست که آیا توافق نهایی بر سر این پیشنهاد حاصل خواهد شد یا خیر.
🔴
در پشت پرده: کشورهای حاشیه خلیج فارس از فقدان یک سیاست روشن از سوی ایالات متحده ناراضی هستند. همه کشورهای حاشیه خلیج فارس دیدگاه یکسانی ندارند، و امارات متحده عربی از آمریکا خواسته است که رویکرد سخت‌گیرانه‌تری را در قبال تهران اتخاذ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/139424" target="_blank">📅 18:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139423">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
👈
وزارت خارجه آمریکا بار دیگر به شهروندان خود در سراسر خاورمیانه هشدار داد و از آنها خواست احتیاط بیشتری به خرج دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139423" target="_blank">📅 18:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139422">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf749ff64.mp4?token=YAEkYD9iI0P5y8XJRLvdy55VgtmEADkMJXScxLg4mmAcJ_B8X3RvkaXQQVWkdkcnfefZDozSDyjq9gkaiPO_sTz0sEfvBuEOO0QYXdJrjm-hBp2bnzehDEuhXKe60jj5BMLN9xWYc8FIRoIr6CBHqeqprdxatewjU5qEKfxFKNbV-SF1qbbZFtsyD8mcByumYmz2YeOX8sMjFawsnnRa7HgK5lthspOf_874Xa0Wf56NUUgiaEpd_LAw0AlkewpfPeD39mMN5kED0qGle1hDeJXhlHAt_4bF-X3UQNJdXXUn6w0ESyM6yWAi2Id8lrQZWxniey3HHlEN0sRUN2hjMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf749ff64.mp4?token=YAEkYD9iI0P5y8XJRLvdy55VgtmEADkMJXScxLg4mmAcJ_B8X3RvkaXQQVWkdkcnfefZDozSDyjq9gkaiPO_sTz0sEfvBuEOO0QYXdJrjm-hBp2bnzehDEuhXKe60jj5BMLN9xWYc8FIRoIr6CBHqeqprdxatewjU5qEKfxFKNbV-SF1qbbZFtsyD8mcByumYmz2YeOX8sMjFawsnnRa7HgK5lthspOf_874Xa0Wf56NUUgiaEpd_LAw0AlkewpfPeD39mMN5kED0qGle1hDeJXhlHAt_4bF-X3UQNJdXXUn6w0ESyM6yWAi2Id8lrQZWxniey3HHlEN0sRUN2hjMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: هدف هیچوقت تغییر حکومت ایران نبوده، هدف فقط این بوده که ایران سلاح هسته‌ای نداشته باشه. اصلا میشه یکی رو بدون دیگری به دست آورد؟
🔴
مارکو روبیو، وزیر خارجه آمریکا: حکومت ایران باید تغییر کنه، شاید نه به معنی تغییر رژیم، اما رفتار این حکومت باید عوض بشه.
🔴
اونا میخوان انقلابشون رو به کشورهای دیگه صادر کنن و این باید متوقف بشه. تنها راهش هم اینه که هزینه این کار رو انقدر براشون بالا ببریم که دیگه نتونن ادامه‌اش‌ بدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139422" target="_blank">📅 18:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139421">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اکسیوس: در حزب جمهوری‌خواه، جناح قابل‌توجهی استدلال می‌کنند که نباید رهبری حزب پس از ترامپ به ونس سپرده شود
🔴
بسیاری ترجیح می‌دهند روبیو نامزد آینده حزب باشد
🔴
یکی از بزرگ‌ترین حامیان مالی حزب جمهوری‌خواه، گفته در انتخابات از روبیو به جای ونس حمایت خواهد کرد
🔴
ترامپ توانست حزب جمهوری‌خواه دوران بوش را شکست دهد و آن را دگرگون کند؛ ونس باید ثابت کند که او نیز توانایی انجام چنین تحولی را دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139421" target="_blank">📅 17:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139420">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256951396a.mp4?token=LWv4_oEAhbdNiOmt_jIF3bXRqwC5SpdjhjfDYAA7u5laFsqwYpl3u4hDdtnct1hl7bLn0xhMLZrVeGHulSvcwjUALce2GK3GXHNDKhmxyYs6b7eYTGpnmXM_DiYwqs93gScvMKSbl_PYNg-rvYzgkgbwBWhJtWjkxfv89j_zNf6rHW1uUJMz1GXB3ExhbxDjLFBe3cQ__HvFt2f2P9Vq1sPd1KP1kmYQ3eQuLCPLTEhc_YdMMGPYLvrYc0gBBm0U-zBnnmU1GM2cD6RRBgVX-vuhLZ8kAkZx8IMbORnx6qobfFKIWH2bfBjYGuh4XkeJKMyEcxyFBZ54VyC_PrWVSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256951396a.mp4?token=LWv4_oEAhbdNiOmt_jIF3bXRqwC5SpdjhjfDYAA7u5laFsqwYpl3u4hDdtnct1hl7bLn0xhMLZrVeGHulSvcwjUALce2GK3GXHNDKhmxyYs6b7eYTGpnmXM_DiYwqs93gScvMKSbl_PYNg-rvYzgkgbwBWhJtWjkxfv89j_zNf6rHW1uUJMz1GXB3ExhbxDjLFBe3cQ__HvFt2f2P9Vq1sPd1KP1kmYQ3eQuLCPLTEhc_YdMMGPYLvrYc0gBBm0U-zBnnmU1GM2cD6RRBgVX-vuhLZ8kAkZx8IMbORnx6qobfFKIWH2bfBjYGuh4XkeJKMyEcxyFBZ54VyC_PrWVSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو تا هلیکوپتر اطفای حریق موقع مهار آتیش‌سوزی تو یونان سقوط کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139420" target="_blank">📅 17:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139419">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEuJ1a-6b7Usk6jSPKaTKMfaAQk5TKoBsVkk2bm5noPN-fs9qVvs3ZLSgsRWez-EeS_Vh0aGY3MH9lycJxN18e4wzQ78fauXdf2YT1xaWOQqvrAi9cmMQD3nyA7x7nK-JArdwnu3P1TeIGID2jYwURQu4OBJaI4lMFoxd0lzHTeWDWRmFsThZA68XQfJaiigqslbYrTLwNLrSoQ0tmqpeURgB6XI-HNVnQ7vE7bvD0U7wFjLSQtRKHbL7GGDokHWJar75N_f0y0JvqM47qqnsx7m3eTs-Xw_wSC9UXvhicacdRECU3Eq34iGtco9E8zwcssvXqmMi5zjGgSnpYA-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار بی‌بی‌سی: راهبرد ایران در مقابل تهدید آمریکا نابودی متقابل اعراب است و چه بسا که اسرائیل از نابودی متقابل دو طرف سود ببرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139419" target="_blank">📅 17:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139418">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سپاه: توطئه خلع سلاح حماس با شکست راهبردی مواجه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/139418" target="_blank">📅 17:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139416">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPRso5woSVyPE7wUqjXRy_CoVMiT0HwulBGqWUgJya0my7dOYQCuUZIucVURehqXzn4fzoF1t17DM2JoER26ByeppjPn_sdUQDh4dgqt9wGBon9yBp_CKAkPgWQJlnkX3pnJf8Ap4BTkwNILIT6rSeecYk-xWPQVPH8KZ_2q4L7og-Ey1812RKcmU7nN8tNY5e2yS6BcBMAGph6fF_DrhTBOBFweHU0Ny94-aYnp0_88IEM9YRmMyG3VfQDPL2s2l0XGBtyDKUirr6wQ6WHLw4LhxdipYCPmd33vV-wGoCo6pz5_-XnuVM490PU58ZTwaDuLfCgiYGiSu3wHUU3o6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTxN4tYsHV97ZiCkVQnhBtHy32-YR64BciHin9IreIeNw1MEDNNnkc-moUjPeh_R4o02flcz6vXKNALBT8X6y_ojK8TzHLNpQckwTCPZwuFY2v7zoql6dR8AEGw9MFayMji_F4c9zCx83-WHClJq53bU5Z__zie2l_vLjz39aLXIyI4VP_GtjzvvgrNohIGw-cGk-STbR9RaPnGmmEczObBgard-Qfo7fBChGss_ER-Q7UXj8myY7ix5ySZ_giy59n5n94v0o2y48heKqjzCCugP-qFVsaorhv52q-tS2jCcvV3c_VBR9HfAD2AmI4QFOEBVWAtLLAxApycpVyWm-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در حمله ارتش اسرائیل به یک خودرو در غزه 2 تن کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139416" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139415">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=IydkuAkv4KSyxSFh_Qlu1JwuRiq-xAR6k3ozV5eWvITQMQDoLl9DNfKybibZkN-jlQokGGg5DgDUBkETpEVrN2jKnjLwvySRaTSR5n1iR94k0I_BP1pVWjWnP3aRQUZbpprdirK3uX-RgcQ9SI2VHytsboKdHs_yyrQNJlnJphScZ1ihepvMwDbLK2UDsWj0SxE4Wy8GeNwNbFQqACVYonwhmXu9cFN14uvK0tXGByvFuzS3mGi97sxrZyKosvXlOzDnxf_B4nDYH8spnnNrZDEQMyZjudMbDzyb4d4sSNtdagkPUgvgj4XdRyEsWeDwZQfWMPkNiQ8QZ8nnBBXO_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe13b00c74.mp4?token=IydkuAkv4KSyxSFh_Qlu1JwuRiq-xAR6k3ozV5eWvITQMQDoLl9DNfKybibZkN-jlQokGGg5DgDUBkETpEVrN2jKnjLwvySRaTSR5n1iR94k0I_BP1pVWjWnP3aRQUZbpprdirK3uX-RgcQ9SI2VHytsboKdHs_yyrQNJlnJphScZ1ihepvMwDbLK2UDsWj0SxE4Wy8GeNwNbFQqACVYonwhmXu9cFN14uvK0tXGByvFuzS3mGi97sxrZyKosvXlOzDnxf_B4nDYH8spnnNrZDEQMyZjudMbDzyb4d4sSNtdagkPUgvgj4XdRyEsWeDwZQfWMPkNiQ8QZ8nnBBXO_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجارهای پی‌در‌پی در پایگاه التاجی به دلیل آتش‌سوزی در انبار مهمات ارتش عراق رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139415" target="_blank">📅 17:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139414">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk9G0fo94I8jIcXy7zQMI6desiDGouIGRjk4MkBhL5XvknElLFjzpc9UvsqxPNBbWjLhJ936qwr1mJT1fdmOYmH6tFQiPa_MlMVhIeHsA-6h6JA2R0U_kUcqodS-hDg5JnxnLWlsMqG8QwebOs4WJfvx2MiQGXCmMhFYWLFJHwgt174oGCRSq6O6DrUsez6I0jw1Tc_kqF2ctMqQ80jV1gXv0V6UfXve0PdJY8p9Dlq7B26_Wz6fBEnwUIn3TypVscheICym23MFIc6OfxHxyBnOabX3sMsC8gRLFkR1SFhvfq7JMU5P2Crep8UYJ1FI45nIl7pIwdjvPFp--JFzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همسر حسین رمضانی، ماموری که در ۱۸ دی تو میدون علیخانی اصفهان به قتل رسید : یکی از اعدامیا موقع اعدام گفت آب میخوام و بهش آب دادن و این اعصابمو خورد کرد،واسه چی به آدمی که اینقدر بی رحم بوده آب دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139414" target="_blank">📅 17:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139412">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gr5SG_C1V67rrMv28endwvuZ18elr2eUCE0rS44G3BPEYsZ3hT569mOZl3MvoinnbeQONRM-5oh1PqdOVdr4QehXr8dv6rQOnkMjzzisVXaUnAXo3vBJGm3I-yQ0ZdchZRrQ5wqIjDn1qFChqB0rCLGHSGLy3IBa3wMV5GZs8m19Qnoz0JWwBKjznsMo6DInxl7C1q2IaHLje0DjhYL1dAyGEJnivVXrPtJ_84HAWXzYvm7M3FJfNzwl1PPNs_kOl0u1mhQjtWQeKz1ZnhAI1EKiuOD_Xl1Die_VEcCOKNjGk-0eu1RGDhpSSLf5kOYovyfe6c1o15Y6HyvzRt2hNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUP43WZ9GfzyDROHIptdKqPpIWcJhbvzaX53ZbH1dFuTcmlqMJYO4F6D6iuep7uQGIad5Bi1zEhTC71KsRHseNwm4lKOSAIgTwb-ON_GPbICgDlInrZPvGF-k5zMWzNwiW3RZTF9JKWBZwieVvMRGKZE821LJdn_CSIn7OXE94BE1Be62TbhYLWNKH3IAgsgGUYEViejEjkyRA4wBXZ0oefHnchs_-Ydlhfrd7iOtkLhS-Gv4kH0qRKZs90Fr0F6526DircEZH_shpZyWVnxcl6NnJIDs14982Q7TSuG5Db2lJnRl2odQh8ucZacknfqVF2rubDkiCt2G3ljtsIbtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فروند هواپیمای تانکر KC-135 متعلق به نیروی هوایی ایالات متحده که در تاریخ ۱۳ مارس ۲۰۲۶ در یک سانحه هوایی در آسمان عراق به شدت آسیب دید، صبح امروز پس از انجام حدود ۴.۵ ماه تعمیرات در فرودگاه بن گوریون، از اسرائیل به سمت ایالات متحده عزیمت کرد.
🔴
این سانحه زمانی رخ داد که دو فروند هواپیمای KC-135 در حال سوخت‌رسانی به هواپیماهای جنگنده بودند که به سمت عملیات‌هایی در ایران در حرکت بودند. یک فروند از هواپیماها سقوط کرد و هر شش سرنشین آمریکایی آن کشته شدند، در حالی که فروند دیگر با وجود از دست دادن بخشی از دم خود، موفق به فرود اضطراری در اسرائیل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/139412" target="_blank">📅 17:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سخنگوی دولت: تغییری در قیمت بنزین ایجاد نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139411" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سی‌ان‌ان‌: ترامپ با وجود ملاقات با نتانیاهو، او را در موضوع ایران و غزه ناکام گذاشت
🔴
نخست‌وزیر اسرائیل به شدت خواهان آن است که آمریکا جنگ علیه ایران را با جدیت از سر بگیرد
🔴
تل‌آویو معتقد است که واشنگتن برای دستیابی به یک پیروزی عجله دارد و بیش از حد آماده مصالحه با حماس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139410" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En9FQkvTtIP8m6YXntWjiEAhV3nn8cnEMD5NFht47BPpIEqTm1rWpoO0zZ-_4NKY61EqmskK2AlqT8JU_IDJrBvd4EvE1EfClmHBmDrBgf5eMiE97wIVg976UlCZJ0Cxu4cCb98H5Aqc0C9RVSbdQGwwVOqbilhPAlTlw-mQcKRW8tro7a4HaNJSGY4RRBmAiwj6u5WpRGQPFYQlB-3nw8VcMRm8QF8gu21joV29rckB3AmzXgEQaP_fEAREVgjPgN1LztMX1ncUhw8wHPzA4mLoUM4fK5e2ga8IWElW5J4Tzih08-uoHAAtePT3mxOtarMke_CKA-wQKSNDBjs8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
🔴
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139409" target="_blank">📅 16:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTpPeBN-5cDf4rOh75mAxZxyUAw-9hEgc6Ek4pSix5SEB9zZH42zCIOo4y9pjkmq4zB3Curo7AIS4kEtZfq4tdpjgAIiU24EFhjFH9CujBhsOVGEA6rEGgkU51Uc7ewWOHezWmmCQIT1ITwf8eRA5a3dV0ToUOzZF15b0b5zBXo7jJfNYh4qpPBngRoQWXnESeoBtUpS1wDpKvdExW0aO9EbTrfhar7VitYJSnOVfbUleqrN_fIpE6Mo4hfqbELBq9Hs1qX7bAdODyYw46adf6DHOeKtOMLTuV1NGAtPnQKOyoTeVUGqIHgWhaY4YEDhWqnQx3B_UX38wOwZHyk4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایتالیا به طور موقت، کنترل‌های مرزی را برای مسافرانی که از طریق هوا و دریا از اسپانیا وارد می‌شوند، مجدداً اعمال کرده است. این اقدام در پی بحران مهاجرتی اخیر در سئوتا انجام شده و قرار است به مدت یک ماه ادامه داشته باشد.
🔴
ماتئو پیانتدوزی، وزیر کشور، گفت که این کنترل‌ها با هدف نظارت بر تردد شهروندان غیرعضو اتحادیه اروپا در منطقه شنگن و جلوگیری از مهاجرت ثانویه به ایتالیا انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/139408" target="_blank">📅 16:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139407">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قوه قضاییه: اموال سردار آزمون همچنان توقیفه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139407" target="_blank">📅 16:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139406">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBF2_9dJyoLrw-Wnoa_S3MJo9JvO7DZEeGwAI4to8CbRLcwKYjCqFap8nBWgmCqWk0W1UpzHnfPaE7Vme7370MLxpxKu4Q4mY-KWcCiprd4CwAuCiu46vWNxFqhItIZRlPGV-ExHe3zzGNQevKWTv_MaPkXskk-72ebOhf83FQYJA3fV0maTypNOPPhH6DA-Lo6QJCOHeR0ekW4eUfxOrT-WtpCVv48tXxNj3cnVWaTM_AIKJ2IIcFp2Lh_W5_L9KGAGCppKhS7axDs63gIcLFL7VRaMfh9L_auKG1e3IPL554ZgQMno9uK5aGOQpf1c8FMDE4grL1RVJiEz7iwoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین: جنگ آمریکا علیه ایران از کنترل خارج شده است
🔴
دونالد ترامپ به جای یک جنگ سریع که هدف آن سرنگونی حکومت ایران بود، یک درگیری منطقه‌ای را آغاز کرده است که خطر اختلال شدید در تامین انرژی و قیمت‌ها را به همراه دارد و باعث رکود جهانی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139406" target="_blank">📅 16:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139405">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی: در بخش برق خانگی، طبق وعده وزیر و معاونان ایشان، از اول مهرماه جاری به شرط تداوم شرایط فعلی، هیچ‌گونه قطعی برقی برای بخش خانگی نخواهیم داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139405" target="_blank">📅 16:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139404">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رویترز گزارش داد دولت ژاپن به‌زودی اعلام خواهد کرد که توکیو و واشنگتن به‌صورت مشترک برای حمایت از ارزش ین در بازار ارز اقدام کرده‌اند
🔴
این اقدام مشترک با هدف تقویت پول ملی ژاپن و کاهش نوسانات بازار ارز انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/139404" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139403">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
آناتولی به نقل از منابع پاکستانی: قطر و پاکستان نسبت به اینکه مذاکرات میان ایران و آمریکا «به زودی» از سر گرفته شود، به صورت محتاطانه خوش‌بین و امیدوار هستند
🔴
میانجی‌ها انتظار دارند تا پایان هفته جاری، نشانه‌های مثبتی درباره شروع دوباره مذاکرات ظاهر شود
🔴
واشنگتن و تهران از طریق میانجی‌ها در حال تبادل پیام هستند تا برای پایان دادن به درگیری‌ها به مدت دو هفته و آغاز مجدد گفت‌وگوها، به تفاهم برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/139403" target="_blank">📅 16:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139402">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVRdm_Buk-slthygA2N61EqB49geQuB0v2EBHES5wyNUH6OpeerMujoxNl23s0T0FlfGLjLRlGzYAvzsRLe_1IslkFnaUvSQw6bsV-0hbmEGZEB4SASCOwi1TZy55M9eabmK_yCIXIVvPIBB4BUIO_xgEpYX0fVT_uDXESipr5nSJ_MRoE3nDxErNJal8yWSWpHkwL8TPR-9zLlpJZPiCmvP_5QT0Hd1NgakzXaS04NbmN_cB_9FriU5uCJA5MUTG3htCqgC9dWMSSKQVYxz4pfzaVpm03dvF8AKx3stl1tqGCuJtSqHvfd3AW4ysRggsnJyn9zFOPj7C06U4wVAMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید نیویورک پست: انقلاب در ایران ممکن است «هر لحظه» رخ دهد؛ رهبران اعتراضات در تلاش برای مسلح شدن هستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139402" target="_blank">📅 16:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139401">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
برق ۱۰۴۷ اداره و بانک پرمصرف در خراسان رضوی قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139401" target="_blank">📅 16:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139400">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8KEiCzExkRZgzBXxeZDdrrhRlBsqVikBmssVBKb8QkX5GM9xCqlHdTQXJLUc_ddsGroB6uW4YxxkATPKEF2ryfFvPo4wbXcMiH9dewxSqKaONxx4QooRFvP3v7VLfomvePvNKsVB61LhPFUFZbgQtzMzVBMTXGlDpOThe-yv5K9fzapehD7h87oV8UopaVd9yoJMrRdg4avmt_BPhthm1tzzkgsJJopjEfsM61Cda-RVoCDCxKSMNU6XyrycrPt9uVAZKCfxoH4DuFAY3T35KdNowlEDWeVVG6vm1moZ5HA2HjwtfiFbihGFigynihIN-47lnMwjvLe7Tcst7KYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: یک گروه رو به رشد از جمهوری‌خواهان سنتی که پیش از ترامپ فعال بودند، معاون رئیس‌جمهور، جی.دی. وانس، را به عنوان جانشین احتمالی ترامپ مورد انتقاد قرار داده‌اند و استدلال می‌کنند که او بیش از حد جاه‌طلب، کم‌تجربه و بیش از حد همسو با تاکر کارلسون است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139400" target="_blank">📅 16:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139399">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c11034b26.mp4?token=MSCRJ8geJEjrYUKo6T-gQOwPXVub_r0pR65X3zdDxe7iKrY6noSqbGu4kkwHdN9orOIgE39CMNAMYvK3oDSWIszklx2NpioCNaxG6N8zzc72HVexoe64F9Qrw8bw4jIFJ7OKmWsp8VbHhZxR5WVVZNc_RdgplxiVhA-25uM_LeGLznV1ApQ03vDUP7pLhf9ER20fjVSr5svkIMTmJKN083FsmtvW3aZRTKueUu28QlBsDNQ7zGNabwFYe3JvXCF3d4altEWFWbwhLBlnBo0dawSEQvHZSZLR45XploP-ECrTSeTi_tIHn0mgrpJxnqntuW0fu-IHK5qZbGQ0uwPFCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c11034b26.mp4?token=MSCRJ8geJEjrYUKo6T-gQOwPXVub_r0pR65X3zdDxe7iKrY6noSqbGu4kkwHdN9orOIgE39CMNAMYvK3oDSWIszklx2NpioCNaxG6N8zzc72HVexoe64F9Qrw8bw4jIFJ7OKmWsp8VbHhZxR5WVVZNc_RdgplxiVhA-25uM_LeGLznV1ApQ03vDUP7pLhf9ER20fjVSr5svkIMTmJKN083FsmtvW3aZRTKueUu28QlBsDNQ7zGNabwFYe3JvXCF3d4altEWFWbwhLBlnBo0dawSEQvHZSZLR45XploP-ECrTSeTi_tIHn0mgrpJxnqntuW0fu-IHK5qZbGQ0uwPFCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بوسه‌ امام جمعه‌ طبس به چادر داور مسابقات والیبال کارگری
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139399" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139396">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrgqvXcx30_I6TPB3Tm2xQkA3gj_cB_aRh51hQkut_qg0-NuZTOVhIOaXJfzw_LxeH5lsYgUieT3jqMKOrQ27hT2mzXLpctir2sm1QmZUPvuD5NsyT4SljCAZS31StFUBhu-sKJiyiR_MVAl6_KF-ZWRt_kBFcQ0L8pdcwKahIabT-sWBM6dHwo-DYGMNJyp377BJlSYBeGDupEj-vSVAulL4_9fJvxL-DfFyUJy04qt5GHv_6UO6dB6O2Q7NfnkIbmX3LArYoeaYIo7zg52Akw7LyUo0p32uvMaXCNkrVTuCk9NvI_2YGD-5TZ4cbxwUzGon6cDoj51YW-S7wNcXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOpvOjhO_FkMHLHF73jn5IrgUqzRdpmNC8__k-B7vhtaGSi-JdINSENA3DeRtOu8t_wSkDCJ1BxWiIgp4A0KSIWqRlr4Lv4QFeuKgzzGjuJ6QhBdnt4h9mbFvLheUZhOpybCza9ezr9jTeG6joMG-CR-Rzbtf5y4ttyD3nxXLYnacxtc5VT_DWyxrjJQY1DeMfQY0MwdFp0KDpb3xKchiHX1vmCbm8bfO-Mz01AZSdhu3bu4EArerPfMQRVDY-6WnypfSrv-tftbQgwYUksHAlVliaBOib7eHnCgNhAauXtf87v3C-bKczDhfwceBYbuGJ1JvgW2zI6P5dUbG6-c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YveoN3uWsvYxcX7mjYdicVP_PdfrUhWmMCVQ2FIgJpkH71KQ42y0X9aqLs97a4fnvIbcKlIPAyMhYKVE66YkZNVcZ-KycE8vvvJsPCgzdyFf80Cu4utRY8oPiwI5doeqTSuIaB17qn8X7EIZKbXmFhoxy6s5rMAF7MW41it-Z-j84l5-7WJkOlZcYKuN4VLFEjH4w1sxekKWxGY6DN4WPYmqGXN5c5nrAUJ5hNd-5l2Cnr-r1KB8gCbWSrhdQ4Sft4o-nIgXoiERJ8bz-MdThhWeoGhGs2BbpBbiBRAAqgnh4rabkCTcdWoYmOuXA45Wo7rwG3AdOP7mk9MSsjbCHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک کشتی جنگی نازی که در طول جنگ جهانی دوم غرق شده بود، در رودخانه دانوب، در شهر پراهووی، صربستان، و در پی کاهش سطح آب ناشی از موج گرمای بی‌سابقه در اروپا، دوباره سر برآورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139396" target="_blank">📅 16:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139395">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c72ef2d60.mp4?token=I7S3OlnaDm3l5v8C2DF55T9mR8pvvdT9z8fLVQgAUAOblkoFvVCZJu0tAJyXrvfvw8IXVBqYl1Gj00Oyh_3D1wkhrpXedvMsUj_kJZYFZ1bxIn5OTxkZW7Yx8zg3HnTWEW0TeKvTRNQ06dyz0WGs4VPhqJRxctPrC3X-w5MfGeCOzAxaLUW15ogLah4M-Q-AGiPgAa2mJdNLIvcrBuoEQ3jZW3y1tHbXTGjnsUt4zhBkV-g8XbpYQ4J7N4vvj98iB6omiCoUmIw_gEB3t8wGYSR-qSX652qejx-WlvF1IY5gYZAZbXU6pTUc_FNVtqBzB4lpsAzbk3r0iLxv2s6v30TQtMgh2QUv507HR2FK3os40rrqHrotjVMP9e2cOSlRXaGje7ux-dC_4KuSF03i4bRIlaJ1fsN4Oh4n4S19LbIY6WsKPclJpMfPsJjsxyyOie20dhL99Oue6WKqrXsvOMJRrZJ_Doec-msq1L4yjvFFI0IrZ_qkfWQmGRf2GAXpD8aQPzZ5Y_prZWPzwA0Z9tTLhe79V31-_bUA_QESQtJ7o5bmHnJdSaMvL8sX1SRk0SZyhgJN31Nji6czeWTdveC3r3MEh1ISydoummltNNwWAwMFvJwIwAC05e2VS1dETLaIkg5d7wu9k2hwn5Vc8GpbNe9tuKGeCWuP7ofMdnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c72ef2d60.mp4?token=I7S3OlnaDm3l5v8C2DF55T9mR8pvvdT9z8fLVQgAUAOblkoFvVCZJu0tAJyXrvfvw8IXVBqYl1Gj00Oyh_3D1wkhrpXedvMsUj_kJZYFZ1bxIn5OTxkZW7Yx8zg3HnTWEW0TeKvTRNQ06dyz0WGs4VPhqJRxctPrC3X-w5MfGeCOzAxaLUW15ogLah4M-Q-AGiPgAa2mJdNLIvcrBuoEQ3jZW3y1tHbXTGjnsUt4zhBkV-g8XbpYQ4J7N4vvj98iB6omiCoUmIw_gEB3t8wGYSR-qSX652qejx-WlvF1IY5gYZAZbXU6pTUc_FNVtqBzB4lpsAzbk3r0iLxv2s6v30TQtMgh2QUv507HR2FK3os40rrqHrotjVMP9e2cOSlRXaGje7ux-dC_4KuSF03i4bRIlaJ1fsN4Oh4n4S19LbIY6WsKPclJpMfPsJjsxyyOie20dhL99Oue6WKqrXsvOMJRrZJ_Doec-msq1L4yjvFFI0IrZ_qkfWQmGRf2GAXpD8aQPzZ5Y_prZWPzwA0Z9tTLhe79V31-_bUA_QESQtJ7o5bmHnJdSaMvL8sX1SRk0SZyhgJN31Nji6czeWTdveC3r3MEh1ISydoummltNNwWAwMFvJwIwAC05e2VS1dETLaIkg5d7wu9k2hwn5Vc8GpbNe9tuKGeCWuP7ofMdnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک کشتی مسافربری با ۲۷۱ سرنشین، روز یکشنبه ۱۱ مرداد ماه، در دریای جاوه دچار آتش‌سوزی شد و عملیات امداد برای تخلیه مسافران و خدمه این شناور در حال انجام است
🔴
به گزارش خبرگزاری فرانسه، این کشتی از شهر سورابایا، دومین شهر بزرگ اندونزی در استان جاوه شرقی، به مقصد استان سولاوسی جنوبی در حرکت بود که دچار آتش‌سوزی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139395" target="_blank">📅 16:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139394">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc8c6cc96.mp4?token=RpLSFpsaoT8Liz4DkMDsHENARazdXS8OZ4jmamGg3mjDPe86dzoM-I6s4ds84Uf8Rcl1qo0JdlYdX8Xc6OqBOYgXXsTIEdtQwX4keZIkc_kOFcJF4wYNW8HesQdMceXNxr_HIbYH-TuVhSFbsUhvaaYXp3BfKmLwGzc1_HCrq2J-2GBo3mSUCgV665PFh1n-Uaarrv81kszLfDpTl84DjkTMZrduq7oUUXlANahy-evfgj8RUnbwg_I0uWVUioDRFTa7CpL90rlo3s6C4eTcQDUNcc0SAqUTatOYWmdCxHkBRm204AZwo0kGyQVumArFFwyf6i3EfogDBS_fXYF4-S2Ps8yOrBRaaj-wEtMozAbrwv7AKNpae1v3cBXKUuk9nkYDxTbuA-YjMnZwtFBk1OivgVNXdLVpSPm9YtdBOpr0r1Zx3s2nFBjqSbJuwR8Mp2DriU6beVRVu5RFF3RvTvU4KJzXED6mn8h3d5_vxfDBlp8wUfVNR336-0GQX5F5Z5ET3Si0i7TnfJaqVgpsBZOWDg1nopAX89JXD6Fsuq8uYFR5A6Ozem4h1WBZOVmRDWjwpoBkHYR8K5pkOVApHU7I7ZcZsG3Hn08LJdFRrjclqCrnsD9l5n_kdqg9g7hfchk526CC5GLwaEAeUN1Pbx_zbui9YpLQVVq7jJ2s7F0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc8c6cc96.mp4?token=RpLSFpsaoT8Liz4DkMDsHENARazdXS8OZ4jmamGg3mjDPe86dzoM-I6s4ds84Uf8Rcl1qo0JdlYdX8Xc6OqBOYgXXsTIEdtQwX4keZIkc_kOFcJF4wYNW8HesQdMceXNxr_HIbYH-TuVhSFbsUhvaaYXp3BfKmLwGzc1_HCrq2J-2GBo3mSUCgV665PFh1n-Uaarrv81kszLfDpTl84DjkTMZrduq7oUUXlANahy-evfgj8RUnbwg_I0uWVUioDRFTa7CpL90rlo3s6C4eTcQDUNcc0SAqUTatOYWmdCxHkBRm204AZwo0kGyQVumArFFwyf6i3EfogDBS_fXYF4-S2Ps8yOrBRaaj-wEtMozAbrwv7AKNpae1v3cBXKUuk9nkYDxTbuA-YjMnZwtFBk1OivgVNXdLVpSPm9YtdBOpr0r1Zx3s2nFBjqSbJuwR8Mp2DriU6beVRVu5RFF3RvTvU4KJzXED6mn8h3d5_vxfDBlp8wUfVNR336-0GQX5F5Z5ET3Si0i7TnfJaqVgpsBZOWDg1nopAX89JXD6Fsuq8uYFR5A6Ozem4h1WBZOVmRDWjwpoBkHYR8K5pkOVApHU7I7ZcZsG3Hn08LJdFRrjclqCrnsD9l5n_kdqg9g7hfchk526CC5GLwaEAeUN1Pbx_zbui9YpLQVVq7jJ2s7F0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آی ۲۴ نیوز عبری
🔴
بنی گانتز، عضو کنست : اسرائیلی‌ها باید بدونن که کارزار علیه ایران کوتاه‌مدت نیست
🔴
این یک نبرد طولانیه و ممکنه سال‌ها ادامه داشته باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/139394" target="_blank">📅 16:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139393">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نشریه اکونومیست گزارش داد چین اندکی پس از دیدار دونالد ترامپ و شی جین‌پینگ در سال ۲۰۲۵، ارزیابی و آزمودن واکنش متحدان آمریکا را آغاز کرد.
🔴
این گزارش می‌افزاید پکن از آن زمان تاکنون به‌طور مستمر دامنه فعالیت‌ها و اقدامات خود را افزایش داده و فشار بر متحدان واشنگتن را تشدید کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139393" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139392">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkvcLtMNKdF005yBHcTvKOeWUhgbEgj_VCW-dT7yJKb1hE4HIAzbKIVGjp63PUg4MCaHVQjD9ebRcBWQVwEp1VnL6ExjjdnWvroDlZKSZIAbaU6ls3e2cQppL6U4Gjml8CTcX3DKvQ6LMKRvjeDDA0PzipKSbS6xiq4UxOcYHDpopL8GlmVJbk51eHHHfo3da8KNYNWWvhzhSi3ooulVdPu8OSAdPFGtu-CNp4U4lqTGuH6OXuBIY6oEEmV0rwdGjcc31bheUr25o51C66Tt4hqOuw6oSuBCupyAc191u32yPcHWK8eFoB5cLGwHNlU0dt30_jfts9YFBkRPZNz5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چرخه مودی ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139392" target="_blank">📅 15:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139391">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق گفته است که توافق شده است تا یک دفتر برای نمایندگی ناتو در بغداد تاسیس شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139391" target="_blank">📅 15:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139390">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ادارات خوزستان دورکار شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/139390" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139389">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سنگدوینی، عضو کمیسیون انرژی مجلس: ۲ تا ۳ هفته آینده قطعی‌های برق تمام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139389" target="_blank">📅 15:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139388">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
منچ‌اوسینت: کشتی حامل گاز قطر که تحت اسکورت آمریکا حرکت می‌کرد، در جنوب تنگه هرمز لنگر انداخته و متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139388" target="_blank">📅 15:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139387">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
باراک راوید: جمهوری اسلامی با بازگشایی تنگه هرمز موافقت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139387" target="_blank">📅 15:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139386">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
مدیرکل فرودگاه‌های آذربایجان غربی از راه‌اندازی پرواز زنجیره‌ای تهران–ارومیه–مشهد خبر داد و گفت: این مسیر هوایی از هفته جاری آغاز شده و در روزهای دوشنبه و پنجشنبه هر هفته برقرار خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139386" target="_blank">📅 15:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139385">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epbC9OPS19AEzt5-Zs6pBQykEGplFMJkt6V9Hdj9DuUx1ANwvT2g7Ra6HlatQvWjrjEqm8NDJnMXZClVXwytodGpYWtAUVUe8mDDy9B0FjxaeN-LunLWe2XFgaz5_Xg3p7MHPTo4384U3tWbjUp9FI-45CkGPHLW3MA602K0rFCyulLMqvszDc_Ae9LAtuQoF4LoUbzDdtib1Brwh0SEXZIJIAeHMVwUetRP38JT-PeHyDf6bHDsal3mLq0LFzfqYK-IF3S2TIv8Mw9QPHH6rUKtAL5cYWZO7XMaf8IK-tn9PgLxETK0nk3amsvmYnMbq30V2y-0TipFf-q-d9rbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید: جمهوری اسلامی با بازگشایی تنگه هرمز موافقت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139385" target="_blank">📅 15:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139383">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jC5VcoyCl7NfpfcLWFMYiHIo8aV13vCGaro6hq_yYfsuSD_bsDxuAMnEHcJ2esyRFk5pROWcHyVoRR1qbsW-x8YCONWUj9u_CVHEmta5igH59Yvo-jTcoyJIowZYFUeFmakp-tLGE0Nsf10-t4JXXLORFg1S0OOrfApBFAucCf8eVd5cUvaIior_5lrkEsggrX6_V75iuWrIUMyCjVZ1zHFpNrvEzkm0vcoMEtOmv9V0prfmILnOw3n2K7Ohemrhcq0GQ2VUIheIk1F-3UknObp9Nix1ITzJE-sPfLfuUY4m00dvuHwRlX_5Sq5rJZekfEF3PuYjSQWTqrfQ9sE9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvQzIVqmbAiMoE8KStSZ-mhPTzHy69ufwCxrwjp9JUF9kffryNtpM7lqaEIZA28JC4q_Fv2KCJcjMl81ZaiERoL-yaXNyxthe7cvFkeSR-bCjkYKpMevqn0Ut4rYG8PJ-HQKn8HOHKyYv_-H4wZFNTkLUyzshaIBrrdFgh0l_cICbYj3S2Hz5bI0J-HKqDdZvzsNwJOg5j5ugFvHbkAI0BROf_4bc7Lr_6Fu1MaZF0QollOEdSiig9iiXArEbarT0nw2gtLQonZOaQCdosZd6VH6ICopY5P5DTkowuTs1Ff4W2-zuICrZMQ8KsYc06KcXHxILpi4HNDyTj9CVgwHcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تعداد هواپیماهایی که از پایگاه‌های هوایی اسرائیل به سمت عراق و عربستان سعودی پرواز می‌کنند، بیشتر از حد معمول است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139383" target="_blank">📅 15:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139381">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
عراقچی به نجف می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139381" target="_blank">📅 15:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139380">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / آژیرها در اردن به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/139380" target="_blank">📅 15:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139379">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12df834aa.mp4?token=AdrbHiFctJT1dFJjCkq0JA3re48izVN6ce1wsOiaK5avICjllRzUT2hr-QLSDsMcOGkj91oboJB5ANWPc5d1LLJBZNtG7da_W7LRV1qO5CIvspTh1BA80WEoOQ_2LQis10lohNxqMt5AaAEX4rKridoFrHXCpwixahcvZvW25txi5XSP9MsZB2yqgAMpTJAWzC_h4l_9tKxuW1qcMW5jljbbdKebWyURq1a7hpkuNgCGHT1Kq9sRCGBOQp4GX8CrCJ2IyIeKvlwbqnwowNhYADp6rHXty9PFY4zzuS77vAZGffD19i7UkI_hb8563i2N-WehpbwSDFWfQXtBpbgstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12df834aa.mp4?token=AdrbHiFctJT1dFJjCkq0JA3re48izVN6ce1wsOiaK5avICjllRzUT2hr-QLSDsMcOGkj91oboJB5ANWPc5d1LLJBZNtG7da_W7LRV1qO5CIvspTh1BA80WEoOQ_2LQis10lohNxqMt5AaAEX4rKridoFrHXCpwixahcvZvW25txi5XSP9MsZB2yqgAMpTJAWzC_h4l_9tKxuW1qcMW5jljbbdKebWyURq1a7hpkuNgCGHT1Kq9sRCGBOQp4GX8CrCJ2IyIeKvlwbqnwowNhYADp6rHXty9PFY4zzuS77vAZGffD19i7UkI_hb8563i2N-WehpbwSDFWfQXtBpbgstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: فقط یک پنجم موشک ها مصرف شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/139379" target="_blank">📅 15:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139378">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnjnwA3AaYaC7IkTRZ3Fu4cGzgJ6yqHRPCntVHXP_5Q65xx5pytT46vRDgb8uw0nlEMjAbow0ZhSM5_9NtMCqZFstFUMofedUGiAqkj2t5iF82ROX9wo8nSNa6rgi5EhW7Soc3YmI3qRzsVcq0xLfCXzoxE31n2uFebjKcLLW8uQQxc-uBYYQpA-iYpEN-cF78lmrymiWIuuhYv9WG3OABRyhnvV_8aLwXAOKZsvvH2xzKF9fsj7dXIx-vMUK_q5ndjTm9nCInUAulFyvJRLcqopU6eMBivm2eTDUL3lqrtcM0aDpnhG8l9iGI8ZYzD2Kgkr1m3bd_fHZD_QGv2-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای سومین بار در طول یک ماه گذشته، درگیری‌ها میان نیروهای انصارالله و نیروهای مقاومت ملی یمن (حامی شورای رهبری ریاست‌جمهوری) از سر گرفته شده است.
🔴
درگیری‌ها هم‌اکنون در غرب ارتفاعات البرح، در محور حیس در جنوب‌غربی یمن، ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139378" target="_blank">📅 15:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139377">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سازمان اوپک: هفت کشور عضو برای کاهش روزانه ۱۸۸ هزار بشکه‌ای تولید نفت خود به توافق رسیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/139377" target="_blank">📅 15:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeMn-2evDoExS-g7Bp8QpWmkHgJZUxtzShxJHdR6JTgWdmOcIyBw-dHmmy3_21VyuwCw18zDxpzhrlTUWkPcawh2uKnn7QdF-xk0s6CTfmtlbVhTel2sbkUZj4zNDGpV13uwyrhGnRRZ6CPrFEd3GSIYgEzBAFnPR5yA9FYnQIOlb1ZAhCnTp55ploW8qQBp9QkS5-PBXTMsFIGbfqvyjKYdAuN-P3cje_5EVDGzJHcWqYBdv1jc4cBfqpunkXudIys2Oa6WmQayXqoeiSOKgRG9uTYW5TRxB42Gz-pTsMRMqo3C7YkZudUwVcgWcUZmJmfG1Wl538EqSzlpAhJ-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان، نماینده مجلس: عده‌ای در ایران با انگیزه‌های گوناگون از جمله نجات دشمن مجددا به فکر مذاکره افتاده‌اند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139376" target="_blank">📅 15:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139375">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد یکی از فرماندهان گروه حماس که در حمله ۷ اکتبر ۲۰۲۳ به کیبوتص "نیر عوز" مشارکت داشت، در حمله‌ روز شنبه ۱۰ مرداد (۱ اوت) به جنوب نوار غزه  ترور شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/139375" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139374">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAfvcfa0nMZrpqYW38ydSry8J2m2yiBgeOkQrPyu7y5J4QY71qnytoFkQgRmdKR5DCVErE_4dXqNC7Jq7GGFXEg7WhqFn2W-1eSqTeHkO3aitZiqW_cIGU_Q0s22-y75YHVdwFW_s6zpoApaFfqT8pWMh2EoClldaelK212LKEpGRclG8L2BFyL1orL-oGa6d5J-BeT2l7BoKTMjfnmv_lEzfpQSuIwWkgs2ymCbe_AiqpTp4K7cOY-NfPwSEvuLFy0fVgTXgSoTn7Akd6U6psWQ8JXZ8T_0_ymXhn7pSzv376UHRnEWSPBWBDErS3hWd_gunaWT0AW8DvO-7uVLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسموتریچ: نتانیاهو به ترامپ گفته نیروهای بین المللی غزه را اداره کنند، یعنی غزه منطقه بین المللی شود.
🔴
من با این موضوع مخالفم. ما یهودیان باید غزه را اداره کنید، به نظر من راه حل دیگه ای وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139374" target="_blank">📅 15:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139373">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
مرکز آمار:جمعیت ایران به ۸۷ میلیون و ۶ هزار و ۳۷ نفر رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/139373" target="_blank">📅 14:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139372">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک نماینده پارلمان اسرائیل می‌گوید
بعد از تقریباً سه سال جنگ، 966 سرباز ارتش اسرائیل کشته شدند، 24000 نفر مجروح شدند، صدها هزار دستور احضار برای خدمت سربازی صادر شد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/139372" target="_blank">📅 14:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139371">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2t23kvCODhkx3IS9409q1SP2ETBQIESsi9NDMFq8O6YJlg9aVknTv2wp1KcWxvdczbEk-75iy8V-oh6EFRxhn30WmPjPouA9zgO-AoXWBHBYzXBEG52uhar3YdGrIgNFy1Y_wF8jcD3t6HBXFuSXCRMbRl5Vi8ByZEz19qYkJ-hSk5fn2160XXvlpT_R_LXAotllfODHcQK7Dv_5iWIyHsWXWc9DMEgsMWAtixg7hC64I-gsNaAZ85bQALtdnPM6CDFfynzjSx1S3Q37hcmTnzb1N0DOHHK6a-NjigewUA4cknIGfSOqhjKwyXf7lRK2sR3hj9njIPxwB1bAGiYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه های اسرائیلی با انتشار این عکس، تغییرات خلقی ترامپ در هر روز هفته رو نشون دادن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/139371" target="_blank">📅 14:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139370">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXhOoqk1Owh7RinlyJhw8GcNAR0LyesLaiAddkW3KgYIzURdYgl0Rmhiye5qk47H8DaSzn_9KFk7MEgeVoQWI3pYSz5f0-jzUZvlbUCYzdh-7yRJOqd0DIQRAL1jRNrtV77WZnIKUQdNalkvaZpb8Ya1RvhQizgtqMxkrRII7DmVs_8uYq8z38N6hFLWxtu4djXx6n0ZtrX03em8RhEIaxS_He2-48_AkhEbrGp9FPyDxC4v8w-shCqrJR_K8QwsrhpWmmuGB3mXv-rMvwIE6IeBLrt0fOm7GlJsYntv4cxbeB5emkcBKEXDKmuYSbEiJH3_LwwRiqleka-42L3KNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش لبنان اعلام کرد که در پی حمله‌ای از سوی اسرائیل در جنوب لبنان، 5 سرباز مجروح شده‌اند. این حادثه زمانی رخ داد که نیروهای ارتش در حال اسکورت یک خودرو نظامی به منظور کمک به ساکنان محلی بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/139370" target="_blank">📅 14:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139369">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
الجزیره: سیاست فشار حداکثری امریکا علیه ایران، به رقابت این کشور با چین گره خورده
🔴
یکی از نشانه‌های تغییر موازنه قدرت این است که واشنگتن پس از ناکامی در جنگ علیه تهران، برای آتش‌بس ناچار شد به پاکستان، متحد نزدیک چین، تکیه کند
🔴
با توجه به گسترش روابط پکن و تهران، فشار ایالات متحده به ایران، تلاشی برای محدود کردن دسترسی چین به منابع انرژی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139369" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139368">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر با وزیر خارجه عربستان سعودی درباره تلاشهای کاهش تنش در منطقه به صورت تلفنی گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139368" target="_blank">📅 14:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139367">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
آناتولی به نقل از منابع پاکستانی: میانجیگران پاکستانی و قطری «خوش‌بینی محتاطانه‌ای» نسبت به از سرگیری مذاکرات متوقف‌شده بین واشنگتن و تهران دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139367" target="_blank">📅 14:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139366">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
گزارش مرکز آمار از افزایش قیمت اقلام غذایی نسبت به تیر ماه سال گذشته: مرغ ۱۹۰ درصد، شیر ۱۵۰ درصد، ماست ۱۳۰ درصد، روغن مایع ۳۴۴ درصد، روغن جامد ۴۰۰ درصد و سیب و موز ۱۰۰ درصد افزایش قیمت داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139366" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139363">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJXZ3nKtH2NoE4ehPZGSVM44d4nAIppH42D509rFG0SHWq71uBjs6rCq7y13WSEl1l8wrRPkTalr_o9z7newBwAzqloYCDfrHYKY48c3P-oJ6KWI-yLrStk3uPfuySXmjM37b54FkmwUVrH1k8NIQUJWOA4N2Sf2YrueY5goGwsOGlUJv-ZEIC_tVRrrFD5ggGNVkEGWBF1kcB6WWdgJSJKH7ie437fuN-7uSzmtOJ3XQHa2VW-3lxrSNPMM3QNUo3zDeRyD8PmNXG2aS4XjJFbdGhjxythBTf0jM3ClTWZbkCwoDmCFJ9Ztd5wNPJ5N3Zf5q2eWXsORh1T2urvCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-3MCIQz6w4uTmV9aZRn8QZfjOQpPzCkZmVy7lOClNafu0v34WztNcL1J3kcKu8Nf_sUKlGYkrb5Ds2jibaDtp6iXejPlLZAw5EbvnoqLljCvPLTsHW_aWHMhrlhBXUl-A7M7c5D7t5icxU_LxreP2PEnbJg-yV9-3ritGX7CEnQP1WFvUQzNfbGDOPCJdrDYKyPk8WIVrTL9kWXaI9pQXikpOlvIQzs3tEBc_s1r-9k_V9OsAiYsX8-hID71FGOCIlDkKcyyOcA4UVRW7DkZvebKo6M9-oUqIitfVKzIrcFcBnku3byHUvtyXGCPFyPWZzZkQT-ufvpJuURU5rItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uN75FmSu4T9k8Nb1w6EKeuCsV1sGR0RPlnQzQ40s9S5IfNRsdwIM53LltHgmesxgwn_n9Ha4qIrc_VcT98U2b1YCBFSBd6bZZY4FfIbT321Y2UpQQJ62x7sXLLXXTR3VPqyf-L3DJUJC8T-YsV3WY5q2bWU4HZpV320lClQxrEK86TgOEBIR6uH9rnyy8ZpDls0kn8t0k7TLrta7i26vkDpS54W6_CCuwrtRZYgzHGvva7WEQuFtpB-WECH8gPNH4EQrf0i0Db0r0UESWgNb4FQ10AygdtoU1eX-NguU-scBb12G53AEek99UPE4npsJycEFxnKPXyMfOLM4y-HxXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جدیدترین
برآورد از انتخابات میان‌دوره‌ای آمریکا (۹۳ روز مانده تا انتخابات)
🔴
شانس کسب اکثریت در مجلس نمایندگان (Kalshi):
۸۴٪ دموکرات‌ها | ۱۶٪ جمهوری‌خواهان
🔴
شانس کسب اکثریت در سنا (Kalshi):
۵۳٪ جمهوری‌خواهان | ۴۷٪ دموکرات‌ها
🔴
آخرین
پیش‌بینی امریکانا از ترکیب احتمالی سنا:
۵۱ کرسی دموکرات‌ها | ۴۹ کرسی جمهوری‌خواهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139363" target="_blank">📅 14:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139362">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شبکه العربیة: جهاد اسلامی فلسطین با توافقنامه خلع سلاح موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139362" target="_blank">📅 14:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139361">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
قاسمی، عضو اتاق تعاون :
آمریکا با محاصره دریایی ایران، امنیت غذایی جهان رو گروگان گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/139361" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139360">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
شرکت هواپیمایی پرتغالی TAP تعلیق پروازهای خود به اسرائیل را تمدید کرد و لغو پروازها اکنون تا ۱۵ سپتامبر (۲۵ شهریور) ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139360" target="_blank">📅 14:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139359">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
تحلیلگر صداوسیما: هدف ترامپ از اینکه این همه تهدید می کنه و حمله نمیکنه اینه که حمله به ایران عادی بشه و دیگه قیمت نفت و بورس رو تغییر نده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139359" target="_blank">📅 14:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139358">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8wTQ8xQAyHlNTGflF1BQEmHQoCNX4i0KmUaX615504CbTEqcfYslZ1zaHsr8ldeKEHgQHrVSB-OHdnnkT4lJLk6WP70LrY3NuwAZgZDJnalNE7v6nEOTUwBZ1A-RBj9SydVcb66sHZDaMDLKxcX3WfBD8f6S0lxtw8qklypPhgZ5qeeCgOs_0ed3hf3237SrCk6CgI_ZKq1C-1FvxMy9739Kz9Rfz-Fvzu16gAVIsieECq-FRPlxpv2bzLFg8q3KIwSOe4fuL6jMxlcH-BuQ-X4IjujCioFAhxPrsaAXl4HId130VO15tv2ZBqdmaQhCSUsaijnq5eYySxuu7bTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک تخریب قدرتمند تحت کنترل اسرائیل در طیبه جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139358" target="_blank">📅 13:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139357">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خبرگزاری رسمی عربستان (واس):
ولیعهد عربستان با ترامپ درباره پیامدهای منطقه‌ای و بین‌المللی گفت‌وگو کرد و بر لزوم اولویت دادن به گفت‌وگو برای کاهش تنش‌ها و تلاش برای دستیابی به آرامش تاکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139357" target="_blank">📅 13:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139356">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=EDLLtraOh-0jhL98-dDgD9FjTwXgGsB8QV_hQ8pUdru1fbukD_7X1JqJOTKbD6UaL46mpHhjvjgbreeRrSft1OCbrLqPgdoFvPlNhSFVXBiy-vR7tg7srRurQGsuJ7e_69KyACdfDfKB8gxYHDyxa2ftshhO5L5W6WhmHxKOqlcrWuPh3wxmtZVMkRfqW8_U0vqBTwx5aY4TRy6AYYJxqb_2EUN7eBPEYKqoZ8ACYJ3u4QdtsZqiFA6IrPpDrrlx0dqemfez4epwVzf63OnYh2EUjlFehpWRwNnxGPF3yB6KbdQ6rq7wJRw1BSA9pfMhOpuTQYy0MQFu-LjA5gKfvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d8c47bc8a.mp4?token=EDLLtraOh-0jhL98-dDgD9FjTwXgGsB8QV_hQ8pUdru1fbukD_7X1JqJOTKbD6UaL46mpHhjvjgbreeRrSft1OCbrLqPgdoFvPlNhSFVXBiy-vR7tg7srRurQGsuJ7e_69KyACdfDfKB8gxYHDyxa2ftshhO5L5W6WhmHxKOqlcrWuPh3wxmtZVMkRfqW8_U0vqBTwx5aY4TRy6AYYJxqb_2EUN7eBPEYKqoZ8ACYJ3u4QdtsZqiFA6IrPpDrrlx0dqemfez4epwVzf63OnYh2EUjlFehpWRwNnxGPF3yB6KbdQ6rq7wJRw1BSA9pfMhOpuTQYy0MQFu-LjA5gKfvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا سیما
:
تنگه هرمز همچنان مسدود است... تنگه هرمز امروز شاهد بادهای شدید و ناآرامی‌های دریایی است، اما اراده رزمندگان ایرانی استوار و قوی است و بر این گذرگاه آبی تسلط دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/139356" target="_blank">📅 13:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139355">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
👈
شمار قربانیان مهاجرت مرگبار به سئوتا به ۹۰ نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139355" target="_blank">📅 13:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139354">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری/ ترور یک فرمانده از نیروهای جولانی در حومه شهر درعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139354" target="_blank">📅 13:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139353">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بلومبرگ گزارش داد کشورهای اصلی عضو اوپک‌ در اصول با افزایش جزئی سهمیه تولید نفت برای ماه سپتامبر موافقت کرده‌اند.
🔴
در صورت نهایی شدن این تصمیم، روند بازگرداندن تدریجی عرضه نفت که از سال ۲۰۲۳ متوقف شده بود، از نظر برنامه‌ریزی به‌طور کامل تکمیل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139353" target="_blank">📅 13:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139352">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بروجردی، عضوکمیسیون امنیت مجلس:
به احترام اربعین سکوت کردیم اما پاسخ به دشمن تو راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/139352" target="_blank">📅 13:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139350">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فووووری
🚨
به نقل از آکسیوس، سنتکام کلیه حملات خودش رو به ایران متوقف کرده !!</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139350" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139349">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnExKiKAQPnrwSU5pSp3XX6R4gR9cT-pXUncOXpLRIok9_UF2-aDbdgtppLSaMfuXMknlTfav5CacTqs5D86UcSaMy9N9AavLUxitgMBMMN4uOJ-cfIdcQpol-8qwEx3RpI9y89vg3RhFhJzv8dRueCkhzESTRt2qjky77J5ldO5t3ZKFTKxEtmx-8QIs-MOcSnQ5jjTFVbZYJCXV7aDaLGkBLyCGbnYCTsbSd9aybUjZWXrm0-l2E9RRoMyp0rn2iWUYkxLkx6EiqCoJMinLa4O2In4ipyppGkCIpKcmtwTDCTYsakANkKSbrOCaFezfa59sPbgNnOLTLO1-QD2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس‌نیوز در گزارشی با عنوان «وضعیت تقلا برای بقا» مدعی شد که ایران در واپسین مراحل یک «رژیم درمانده» قرار گرفته و هم‌زمان آمریکا قلب صنعت تولید موشک این کشور را هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139349" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139348">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd816c7b4.mp4?token=JLQgUb2_hpy3_Z-uApKgB1SEATkjM_ml6BSWfifyWE6K60jJByRuff7OV9LZi9zhdJ1wHi0vkRt26KAKSi7WtRZtAuTqmY9P4XlpO5_TGmf8b8YxheE2-8VoHK39wamhMxe_k9z_YvV1bSidINQf-NPA0o8DE5iMfhkI2LxVCfh2eyAIonHD4yCsohox2G5-9ccgEdnQ-YX0W6DqUQ0ceG0kXpcbSs6IoaOgRq0P10gflzBZIqWaJuIBSlc3zxHoLSWHP_gXoTxO9W-KhNF91VC5OH8BhCK2i-ERV9wns5khtDuExGlimzyVDvXEqxP9weudVjcp8SwIKTCZbW5L4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd816c7b4.mp4?token=JLQgUb2_hpy3_Z-uApKgB1SEATkjM_ml6BSWfifyWE6K60jJByRuff7OV9LZi9zhdJ1wHi0vkRt26KAKSi7WtRZtAuTqmY9P4XlpO5_TGmf8b8YxheE2-8VoHK39wamhMxe_k9z_YvV1bSidINQf-NPA0o8DE5iMfhkI2LxVCfh2eyAIonHD4yCsohox2G5-9ccgEdnQ-YX0W6DqUQ0ceG0kXpcbSs6IoaOgRq0P10gflzBZIqWaJuIBSlc3zxHoLSWHP_gXoTxO9W-KhNF91VC5OH8BhCK2i-ERV9wns5khtDuExGlimzyVDvXEqxP9weudVjcp8SwIKTCZbW5L4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که توسط ایالات متحده استفاده می‌شود، اخیرا تخلیه شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139348" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139347">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
العربیه به نقل از کانال ۱۲ اسرائیل:
اسرائیل قصد ندارد حملات به غزه را متوقف کند مگر اینکه حماس خلع سلاح شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139347" target="_blank">📅 13:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139346">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی دولت: حذف کامل کارت سوخت در درازمدت منوط به این است که به طور قطع بدانیم هیچ مشکلی از منظر کارت‌های بانکی وجود ندارد
‏
🔴
در مورد کاهش میزان سهمیه بنزین به زیر ۶۰ لیتر هنوز هیچ تصمیمی گرفته نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139346" target="_blank">📅 13:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139345">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی دولت: دولت در حال پیگیری فرآیندهای قانونی برای صدور گواهینامه موتورسیکلت بانوان است تا با رفع چالش‌های حقوقی و قضایی ناشی از تردد بدون مدرک، وضعیت این گروه از موتورسواران را ساماندهی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139345" target="_blank">📅 13:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139344">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
العالم به نقل از رسانه های عبری: جسد یک افسر اسرائیلی در حالی که اسلحه او درکنارش بود در منطقه النقب پیدا شده است و احتمال خودکشی این افسر وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139344" target="_blank">📅 12:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139343">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
یک منبع نزدیک به تیم مذاکره‌کننده به فارس: هیچ توافقی دربارۀ بازگشایی تنگۀ هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139343" target="_blank">📅 12:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139342">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
یک مقام ایرانی: ایران درخواست نکرده است که ترامپ حمله نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/139342" target="_blank">📅 12:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139341">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocppzBzxm0DvBtZTAmWaUO2PVIzaj4cbhMC-6uYlYUmqU0KVKICtWmRq8MuAXFr-Cqa1i2EXE4VILzJuu9L4VIzeJoesEc6Im0e9kRU7xeY2p9o4UHPLJBE3TgFLle30ftrdVm5obs3WV3Y8CL-m_0fTLT-uG2Ak_xuTgPQ5HcKlrrn6nDYsthqbnXlARZ8Yll7PsznQS_yihzgdrSgbeQWma6SPESBRx-DP6AHLfaoebp18fV0LkHN4hzieaWTMQVSjfDvRIgpDJMg3TDHVxCvuDLJnk_QXo_NxKdr5xUp2PphgYUDmUsd5ErBEbFnsytE0xF81lf3_Ev_JfcR6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جهش ۹۹ هزار واحدی شاخص بورس در پایان معملات امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139341" target="_blank">📅 12:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139340">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsDUaNiXT1TbdYiBWxkyP101zak0ItXjLwmufrLephuYIIjXSpKTHFkPV5TCFCN-JPBQBjdYj1Q0UvXk4VYClwt8zLy3fVF5lyeQuVOfWCX2C0rVmo8BRXN8cJWu72T7hI9vSEz8cYxamBLOHyllAmLQYZ_kEERkL21K_HGeNFgLD12m-3eb4wA-r3nMCKrhoO3EIKoNf7kzOJSkh_SNAKCxsSOzolf0Jz7lfJnEUa-iQOpMNfMn1aa8w2shlaoaZy94SVOVDFObN5fc_ilh5tXpCa58YSg_spJfOgtp1clOLHFoUULGrJnSZFToBiO2JVCDXxLjtjelavt7wtoafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هوش مصنوعی "گروک" اعلام کرد که از زمان آغاز جنگ با ایران، ترامپ حداقل 10 بار از تهدید خود عقب‌نشینی کرده و حملاتش به ایران را لغو کرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139340" target="_blank">📅 12:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139339">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نشریه Middle East Eye مدعی شده است که دونالد ترامپ از اسرائیل خواسته بود در صورت آغاز حملات نظامی آمریکا علیه ایران، به این عملیات بپیوندد و مقامات ارشد جمهوری اسلامی را هدف ترور قرار دهد.
🔴
این ادعا تاکنون از سوی منابع رسمی دولت آمریکا یا اسرائیل به‌طور مستقل تأیید نشده و عمدتاً بر گزارش‌های رسانه‌ای و نقل‌قول از منابع آگاه استوار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139339" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139338">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ستاد مشترک ارتش اوکراین: یک پالایشگاه نفت و یک پایگاه هوایی در استان ساراتوف در جنوب غربی روسیه را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139338" target="_blank">📅 12:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139337">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnWS3yUaAPN7HGjBinuqvEwO0i2Yzj0LwRDHF_nC0cKjILMIUhhddhajYlNElEo3n5RkTzNcQgcVYSijOYpJCL_2MEpz34waC1aKvhTzeKxu8ZO3CWaxrM4ZmVOOsLGqMHHPzZigN4C6ptPvATjQTxvoMn0BC0yFqEK-V5oivUNYWvsaD-AbCbRvfnuVwTUhjrEKJNwF9fsalGIc3LJ50UDqQcx8fv5i_dvmhx5lkUYW6ZtspYilf8zFtuV7UyasVZjPz2rgMl5c1anB5ytsubjcn_ApHnnOeAjR9LMmjqNUEqC2D5W6DxmImMCVfRIVdg2qLWkjmatElXxgmzbhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت تتر در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/139337" target="_blank">📅 12:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139336">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سخنگوی ارتش: از فرصت آتش‌بس و تفاهم‌نامه برای واردات تجهیزات و بازسازی توان رزم ارتش حداکثر استفاده را کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/139336" target="_blank">📅 12:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139335">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اسرائیل سه شرط در مورد توافق با حماس مطرح کرد:
🔴
اول: مخالفت با انبار کردن سلاح‌ها به جای نابودی آنها.
🔴
دوم: مخالفت با مشارکت قطر و ترکیه در مکانیسم تأیید توافق.
🔴
سوم: عدم محدود کردن آزادی رفت و آمد اسرائیل در غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/139335" target="_blank">📅 12:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبرگزاری عراقی «نایا» گزارش داد که نیروهای آمریکایی مستقر در پایگاه عین‌الاسد در غرب عراق، عملیات هلی‌برن انجام داده و سپس به‌سمت منطقه بیابانی «النخیب» در غرب این کشور حرکت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139334" target="_blank">📅 12:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139333">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn8zvsYdkmUJfHNixLCNMA5P2eEvm2adBaHgBJqNdI6Q4oTnFmUDXncSoIHsH8n3UJJT5nA2AbiZeMBFbO-bIjVpleMz2JYttMYNHIdv8LDjX0zV24uL-rBxGuQbDRAiKv50dPfNeHq9WjA45m6DwFUQV0FQ8Fuxmuio6sOFXftuAqfmb2DrRNWJLPlFufnBE1D9pOVkWluoFnH6kEw29E9JbijQ6iIDj8ALxwLj2QBI8vMnFN1E1PjKG79i6URohUcgG6W6GTdJJ8Il91M9oNPeKJvavyP4uurjkFh_4vrqf1cwvnHPuZhabTHaacYEzbs9-UKdPou6oxm8LrWO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری عراقی «نایا» گزارش داد که نیروهای آمریکایی مستقر در پایگاه عین‌الاسد در غرب عراق، عملیات هلی‌برن انجام داده و سپس به‌سمت منطقه بیابانی «النخیب» در غرب این کشور حرکت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139333" target="_blank">📅 12:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUPj6vo0XKJ8bThd8BWSHRsM6iM7UqQOdzcJF29D50-fx9LpmfPHrJjOV0eCnh4VvzvdY_iGPSbkV_o1nMRETw9DaXxaZNrqEMTZTvHoAFb-ALPwC0WWM2kDKyiuL2eIR4De_xtkDi2NsKDwJiIWfRgDzaPZr-tZG4X8HSdrxqrRbxNPahrkYDs5B85l9X5M7JiLzuadpdEeoK6MTYxyzViSLmKY8WwblzaM5CPVwaGDYRDXKG3cTTVtb5o6QoGuWpYEVyC2JRaXxxrI1UZYCViqJI5k-a2MzJdPqY41nQSq1sX-wkXpnbAZ7XnJLrTs-mK0lBKGpTMJ-ujjkUXe7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین یکتا: باید انتقام آقا رو بگیریم تا امنیت امام زمان رو تامین کنیم
#بدعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139332" target="_blank">📅 11:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139331">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
الجزیره: ایران در حال بررسی یک پیشنهاد جدید آمریکا برای کاهش تنش‌هاست
🔴
شبکه الجزیره گزارش داد که ایران یک پیشنهاد از سوی ایالات متحده دریافت کرده که می‌تواند به کاهش تنش‌های کنونی منجر شود.
🔴
بر اساس این گزارش، تهران با جدیت در حال بررسی این پیشنهاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139331" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
