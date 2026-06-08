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
<img src="https://cdn4.telesco.pe/file/laffSY4yuB4hVz9J6dYcC2n365dmzAYqNKWIc3h2D1JSs-pWvsudktTYEZ_te1fdZOJfPBTIh3c2aek583FBi960ZI4Al61SqmZQJToiZhNXgZucqtkk3tkbf3Q-ZmP6iHcP4VhPB851UL_Qhjmu6jvNbL6__CD3Ev7IEyXq6krkdRGr8G76OMoCr_-9oni1LEu_7LEMPEpgxkulVajJ_cJ_SeL0mLhnn3V_acSLZxs_Al1D4pis5hQp7sa61O--xpwyKNNTgfw7BcsN5aSDerEvLxUyUtkXMA5r-aQy9Genbi860VH27LqCXrGpR7bthJvwIh8Fz54CLTiCI_BAXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-17151">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ گفت که او از نخست‌وزیر اسرائیل نتانیاهو خواست تا به حمله موشکی ایران پاسخ ندهد، اما اسرائیل بعداً تصمیم به حمله به ایران گرفت و تنها در مرحله‌ای متأخر به ایالات متحده اطلاع داد.
او گفت:
«آن‌ها قبلاً در راه ایران بودند. من توانستم دامنه حمله را کاهش دهم،».</div>
<div class="tg-footer">👁️ 527 · <a href="https://t.me/SBoxxx/17151" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17150">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نفت کش هندی بوده !</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/SBoxxx/17150" target="_blank">📅 20:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17149">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">توقف یک نفت کش ایرانی از سوی ارتش آمریکا!</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/17149" target="_blank">📅 20:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17148">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">توقف یک نفت کش ایرانی از سوی ارتش آمریکا!</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SBoxxx/17148" target="_blank">📅 20:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17147">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجنگاوران</strong></div>
<div class="tg-text">اسرائیل بامداد امروز به یک سیستم پمپاژ حیاتی در مجتمع پتروشیمی کارون در ماهشهر، ایران، حمله کرد و هدف آن یک قطعه گران‌قیمت و ضروری بود که مسئول انتقال مواد در داخل این مجموعه است، به منظور مختل کردن عملیات و توقف تولید
ای۲۴.</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/17147" target="_blank">📅 19:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17146">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آغاز حمله سنگین ارتش اسرائیل به شهر صور لبنان</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/17146" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17145">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SBoxxx/17145" target="_blank">📅 19:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17144">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ به نتانیاهو گفته که او معتقد است ایالات متحده و ایران در حال نزدیک شدن به توافق بر سر چارچوبی هستند که به طرفین اجازه می‌دهد برای رسیدن به یک توافق بلندمدت به میز مذاکره بنشینند.</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SBoxxx/17144" target="_blank">📅 19:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17143">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قرارگاه خاتم با ندای «لبیک یا دونالد» به استقبال خرید کریپتو رفت.  اکنون توپ در زمین بی بی است</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/17143" target="_blank">📅 18:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17142">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXeYFsl-S9V4OjOzxj6kIUum8lGNLioQ3Vce7Tzmg_NnSHYuMSpudbgvVdftZBjvywS_1kPwbiTkSE_NOzJ5UFn4MeESSKyCNwptd4DmjZWZv0PgbeeYMYDVulTuPrHAdFgNx9Ki8Y-DAkilgIcxKAlVEDSsoPQQzjcPIbhzJhsZanaeBZRA-0owKYNXaKgGErulNapexVo52_bHmnb_rjYW9RqYG7krZ2g5vSpgWHRwCCNwBMOif3kmJTgY7e6pX0xvhPK2pPtkZOcolyQtqyn5n9y4ekNaLFzGIh1XVQ-NfQ3DXO5irnk6HIu8uvaBmOIViHN98lCcjo5fbRmjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم با ندای «لبیک یا دونالد» به استقبال خرید کریپتو رفت.  اکنون توپ در زمین بی بی است</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/17142" target="_blank">📅 18:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17141">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">— یک مقام آمریکایی به سی‌ان‌ان گفت:  «ادعاهای اسرائیل مبنی بر اینکه ایالات متحده موشک‌های بالستیک ایران که به سمت اسرائیل پرتاب شدند را رهگیری کرده است، هیچ حقیقتی ندارد.  نیروی نظامی ایالات متحده هیچ‌یک از موشک‌های ایرانی که دیشب پرتاب شدند را رهگیری نکرد.»</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/17141" target="_blank">📅 18:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17140">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">— یک مقام آمریکایی به سی‌ان‌ان گفت:
«ادعاهای اسرائیل مبنی بر اینکه ایالات متحده موشک‌های بالستیک ایران که به سمت اسرائیل پرتاب شدند را رهگیری کرده است، هیچ حقیقتی ندارد.
نیروی نظامی ایالات متحده هیچ‌یک از موشک‌های ایرانی که دیشب پرتاب شدند را رهگیری نکرد.»</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/17140" target="_blank">📅 18:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17139">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): پاسخی دردناک به رژیم داده شد و توقف عملیات اعلام می‌گردد
🔹
درپی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SBoxxx/17139" target="_blank">📅 16:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17138">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، از تلاش‌های رهبری سوریه برای بازگرداندن ثبات تقدیر کرد و پیشنهاد داد که احمد الشراع رئیس‌جمهور سوریه، می‌تواند در برابر حزب‌الله در لبنان نقش ایفا کند.
او الشراع را به عنوان «رهبری بسیار خوب» برجسته کرد که مایل به کمک به ایالات متحده در تلاش‌های امنیتی منطقه‌ای خواهد بود.
ترامپ حتی پیشنهاد داد که سوریه می‌تواند در تسهیل حملات «جراحی» علیه حزب‌الله نقش ایفا کند و گفت که او می‌خواهد «زندگی بهتری» برای مردم لبنان داشته باشد.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/17138" target="_blank">📅 15:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17137">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:  «هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره 'صلح' در حال پیشرفت است، مشروط بر اینکه نادانی یا حماقت در راه آن قرار نگیرد.  محاصره همچنان با تمام قدرت و اثر در جای خود باقی خواهد ماند، تا زمانی که یک 'توافق نهایی' حاصل…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17137" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17136">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): پاسخی دردناک به رژیم داده شد و توقف عملیات اعلام می‌گردد
🔹
درپی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.
🔹
پاسخی که رژیم جعلی صهیونیستی و حامیان آن باید از آن درس عبرت گرفته باشند.
🔹
بر این اساس، توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما تاکید می‌شود که در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود./فارس</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17136" target="_blank">📅 14:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17135">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">— سامانه‌های پدافند هوایی ایران در شهر مرکزی یزد فعال شده‌اند و در حال دفع «اهداف خصمانه» هستند.</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17135" target="_blank">📅 14:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17134">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ:
«هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره 'صلح' در حال پیشرفت است، مشروط بر اینکه نادانی یا حماقت در راه آن قرار نگیرد.
محاصره همچنان با تمام قدرت و اثر در جای خود باقی خواهد ماند، تا زمانی که یک 'توافق نهایی' حاصل شود.
امور باید به سرعت پیش بروند».</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17134" target="_blank">📅 14:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17133">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بروجردی، عضو کمیسیون امنیت ملی مجلس:   تسلیحاتی داریم که اگر به کار بگیریم زندگی صهیونیست‌ها را مختل می‌کنیم</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17133" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17132">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بروجردی، عضو کمیسیون امنیت ملی مجلس:
تسلیحاتی داریم که اگر به کار بگیریم زندگی صهیونیست‌ها را مختل می‌کنیم</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17132" target="_blank">📅 14:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17131">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">— ارتش اسرائیل:
«برخلاف گزارش‌ها، ما در چند ساعت گذشته هیچ حمله‌ای به ایران انجام نداده‌ایم».</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17131" target="_blank">📅 13:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17130">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
— رئیس‌جمهور آمریکا، ترامپ، به آکسیوس گفت:  «هر کدام از آن‌ها خوش گذراندند. اسرائیل حمله‌اش را انجام داد و ایران حمله‌اش را انجام داد. ما به یکی دیگر نیاز نداریم».</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17130" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17129">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Operation Nasr !</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17129" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17128">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
سیتنا
:
سرعت اینترنت از شب گذشته با شروع درگیری ها افزایش پیدا کرده و فعلا دستوری برای قطع دیتاسنترها دریافت نشده اما شرایط پایدار نیست</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17128" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17127">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هرمز دوباره به صورت کامل بسته شد.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17127" target="_blank">📅 12:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17126">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJfM285RgL0YJB754-TKFeidMQ5NDQolI1gIwPwtH7Mp9pc7iE4MysVYxASW-pVQ1So5-6HfEBFA9J9fSSvvYzB0MQeu3ihDtHi03RpTCcLuSm5U-MmklNBkVMefqNBmZZJ3kvF2ErMKHuc7XUN83KDRytkbF7EuRhFQtVEEEHxQNL8L5nlCTRS1uTTKH8GGTHX8F9W7yd6PODckyEWjhRrKyme2IWy7Twixz_izhxdPqADh6BXLUSUpZDJAJkeiSC1EuWPSXunJstPsOIYt46RNhc_I3SDRUuIkg82A7-X16CJuE9xzMu5-mNkTsI3e0YrqhVCvGuIjLFKEXjNk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوکیلی ببینید گیر چه اسکل هایی افتاده ایم!
اینها برای فرزندان ما تصمیم میگیرند!</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17126" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17125">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ارتش اسرائیل می‌گوید انتظار دارد چند روز درگیری با ایران ادامه یابد و احتمال از سرگیری کامل جنگ وجود دارد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17125" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17124">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فقط نت را قطع نکنید ، بگذارید این لحظات را کنار هم بگذرانیم!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17124" target="_blank">📅 12:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17123">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7hEB-mmcTx6tk0-M6JTomOg_2qz5p7tw5xtAotHDJ00dsmFN_sg15T0D254J3tuiT2tfbNGZnAFYar_iHod19HqKFLzZ9BYYfzZa6hjLCDslVb_kiU7TwHa5yG4wKtNDEc-J1KOjFrJvnXb7OG8v2b9HguYUJCRgG1rSKPNv5BsA3bYxMwb2JdnlXISPK48VmlEFksoNhNgzOykuI1Bw8Y2FGZoXVUb9VdYSo_e8hWwNXQNUB9Eaxrgk-6K_yX134T9UCWi3xGPkAFJTSzSvvM5ngF_CzpYshFCfSn5GKaYfrgt2X5UqIAZfO-dyZOgio5osExiSItGEiye35qU_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بشدت حق!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17123" target="_blank">📅 11:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17122">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اصفهان</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17122" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17121">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسرائیلی ها مدعی شده اند که با حملات امروز، روند بازسازی پدافند هوایی ایران را مختل کرده اند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17121" target="_blank">📅 11:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17120">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کرج کرمانشاه</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17120" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17119">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجار در تهران!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17119" target="_blank">📅 11:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17118">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجار در تهران!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17118" target="_blank">📅 11:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17117">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجار در تهران!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17117" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17116">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کانال 12 اسرائیل:   انتظار می‌رود وزیر دارایی اسرائیل، سموتریچ، استدلال کند که اسرائیل باید به جای حمله مستقیم به ایران، در لبنان در پاسخ به هر حمله ایرانی واکنش نشان دهد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17116" target="_blank">📅 11:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17115">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
⚡️
🇮🇱
رسانه‌های اسرائیلی: گزارش‌های اولیه از سقوط راکتی در کریات هایم، شمال حیفا.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17115" target="_blank">📅 11:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17114">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال 12 اسرائیل:   انتظار می‌رود وزیر دارایی اسرائیل، سموتریچ، استدلال کند که اسرائیل باید به جای حمله مستقیم به ایران، در لبنان در پاسخ به هر حمله ایرانی واکنش نشان دهد.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17114" target="_blank">📅 11:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17113">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانال 12 اسرائیل:
انتظار می‌رود وزیر دارایی اسرائیل، سموتریچ، استدلال کند که اسرائیل باید به جای حمله مستقیم به ایران، در لبنان در پاسخ به هر حمله ایرانی واکنش نشان دهد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17113" target="_blank">📅 11:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17112">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دلشان خوش است که 4 تا فلسطینی فلک زده از این حملات خوشحال باشند! نابودی زندگی و زیرساخت های خودمان مهم نیست آن وقت شادی مضحک این یارو مهم است!</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17112" target="_blank">📅 10:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17111">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خوشحالی یکی از فلسطینی های مظلوم نوار غزه که میگه:  ایران الان داره می‌زنه، داره می‌زنه، جانم ایران، جانم جمهوریه اسلامی ایران آزاد، به عشق خدا. به هر کشوری که با موشک‌های شما مخالفت می‌کند، حمله کنید، حتی اگر پدر خودم باشد. موشک‌ها را پرتاب کنید.  @IRAN_CITYOFSUN</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17111" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17110">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromایران،شهر خورشید(رضایی)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4484d2171d.mp4?token=XXHAQBdkjeUrHoEcIYLMvqHcufsTbPDIA1L-qf6VWU5ri7D6oVxlKXn64qinrMF8GB5ER9oyU7DZ7Eyu45-dOjMdi2juqISheDyhvN2Fe3MJUzjcmFpmT_wqKxqjka_YIQrG0t8L0FnvGsJZD8WXM_9cQ4QiYttdy3cn6V8-eQkLQnvepuK8gkTC8F4YawMzDFiIOJwVYFm58egulphJrOjLUT6FLXdpbU4hIasEOQ14Q-5GSLHL3bA4PCFkhu7U_arVBc2h64ERV0Q0hWXoruhHooyYVQ2bwTQ_14Dggfvn6_0uITDxOrsFhvE1NXo5Fl18o-pu-OS4-abBYNFeAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4484d2171d.mp4?token=XXHAQBdkjeUrHoEcIYLMvqHcufsTbPDIA1L-qf6VWU5ri7D6oVxlKXn64qinrMF8GB5ER9oyU7DZ7Eyu45-dOjMdi2juqISheDyhvN2Fe3MJUzjcmFpmT_wqKxqjka_YIQrG0t8L0FnvGsJZD8WXM_9cQ4QiYttdy3cn6V8-eQkLQnvepuK8gkTC8F4YawMzDFiIOJwVYFm58egulphJrOjLUT6FLXdpbU4hIasEOQ14Q-5GSLHL3bA4PCFkhu7U_arVBc2h64ERV0Q0hWXoruhHooyYVQ2bwTQ_14Dggfvn6_0uITDxOrsFhvE1NXo5Fl18o-pu-OS4-abBYNFeAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشحالی یکی از فلسطینی های مظلوم نوار غزه که میگه:
ایران الان داره می‌زنه، داره می‌زنه، جانم ایران، جانم جمهوریه اسلامی ایران آزاد، به عشق خدا. به هر کشوری که با موشک‌های شما مخالفت می‌کند، حمله کنید، حتی اگر پدر خودم باشد. موشک‌ها را پرتاب کنید.
@IRAN_CITYOFSUN</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17110" target="_blank">📅 10:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17109">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WY5iyunnBTLkS5Vofh4xjtEfEQd0On6A9JFuujMRKZRsKHRewCAZ_5dViGR-UeUKjotNHNTNhWtZzHlbC9Q22zoX99WoBQajyX5kogVQe6RnJ8bgvUvQDljj-gSTsvnFYNhYHBanqvxJlLlV9oJh05c264dxNEG8OTYoCbq_KQVYvRFAseKKA5YL4j8OX8Qz-ku9mHrFvO7k3NaP9xQA2RbnGGBtPuikEKYKPScbmO6KUSGxdFX5-IXQsf0b-QgePFIBLqBPR6_JYixdZbv3lSHrNy63-jiLaIynkkoNb19UyOszijHR5_b0ZEKE6kdfGVyS43p4EeU76aqZJu-nyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایگاه های موشکی استفاده شده در حملات امروز</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17109" target="_blank">📅 10:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17108">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
⚡️
🇮🇱
رسانه‌های اسرائیلی: گزارش‌های اولیه از سقوط راکتی در کریات هایم، شمال حیفا.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17108" target="_blank">📅 10:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17107">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
⚡️
🇮🇱
رسانه‌های اسرائیلی: گزارش‌های اولیه از سقوط راکتی در کریات هایم، شمال حیفا.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17107" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17106">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پرتاب‌هایی از ایران به سمت شمال اسرائیل شناسایی شده‌اند.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17106" target="_blank">📅 10:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17105">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پرتاب‌هایی از ایران به سمت شمال اسرائیل شناسایی شده‌اند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17105" target="_blank">📅 10:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17104">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پرتاب‌هایی از ایران به سمت شمال اسرائیل شناسایی شده‌اند.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17104" target="_blank">📅 09:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17103">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیانیه ی نیروهای مسلح یمن:
ممنوعیت کامل و مطلق دریانوردی رژیم صهیونیستی در دریای سرخ</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17103" target="_blank">📅 09:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17102">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خب فعلا خبری نیست برویم بخوابیم .  به نظرم کریپتو و طلا و نقره یک ریکاوری و رشد خوبی فردا خواهندداشت.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17102" target="_blank">📅 09:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17101">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اورژانس استان تهران:  در پی اخبار منتشر شده شب گذشته، تا این لحظه هیچگونه تماسی مبنی بر وجود مصدوم نداشته ایم</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/17101" target="_blank">📅 09:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17100">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">Operation Nasr !</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17100" target="_blank">📅 09:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17099">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/17099" target="_blank">📅 09:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17098">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">در اسرائیل، تخمین زده می‌شود که این یک ابتدای شعله‌ور شدن یک تنش است که می‌تواند به یک جنگ  تشدید شود. آماده‌سازی برای چند روز درگیری.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17098" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17097">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سپاه پاسداران: «ما آماده انجام عملیات در تمام جبهه‌ها هستیم و پاسخ خود را بر اساس سناریوهای مختلف دشمن برنامه‌ریزی کرده‌ایم».</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17097" target="_blank">📅 08:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17096">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سپاه پاسداران در بیانیه ای مدعی شده است که در اخرین حملات موشکی خود پایگاه های هوایی تل نوف و نواتیم را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17096" target="_blank">📅 08:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17095">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سپاه پاسداران در بیانیه ای مدعی شده است که در اخرین حملات موشکی خود پایگاه های هوایی تل نوف و نواتیم را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17095" target="_blank">📅 08:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17094">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اورژانس استان تهران:
در پی اخبار منتشر شده شب گذشته، تا این لحظه هیچگونه تماسی مبنی بر وجود مصدوم نداشته ایم</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17094" target="_blank">📅 08:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17093">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شبکه ۱۲ اسرائیل : نیروی هوایی اسرائیل ۲۰ هدف تو ایران را زده</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17093" target="_blank">📅 08:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17092">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">منبع اسرائیلی:   ما به حمله پاسخ خواهیم داد، حتی اگر در بازه زمانی فوری اتفاق نیفتد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/17092" target="_blank">📅 03:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17091">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کارت نابودی حزب الله را سوزاندند تا کارت باز کردن تنگه هرمز را نگه دارند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/17091" target="_blank">📅 02:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17090">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: «حملات ایران هیچ  تأثیری بر توافق ندارد. ما قرار است یک توافق بزرگ انجام دهیم»</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17090" target="_blank">📅 02:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17089">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ از نتانیاهو خواست «چند روز» صبر کند تا ببیند آیا می‌توان با ایران به توافق رسید –</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17089" target="_blank">📅 02:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17088">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اگر تعداد موشک ها اندک باشد عملا همان حمله فرمالیته است</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17088" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17087">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایران پیامی به اسرائیل مخابره کرده و اعلام کرده است که موج جدید حملات خود را به پایان رسیده تلقی می‌کند و قصد انجام حملات بیشتری را ندارد، مگر اینکه اسرائیل حملات جدیدی را آغاز کند.  — کانال ۱۳ اسرائیل</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17087" target="_blank">📅 01:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17086">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c631c9b1.mp4?token=clUOBNaArRebYXD-7HMwqcM52xXHWYELeOYCbbFxdy2L5bkuGe1VYHmqCZKjztdP2PDqo3j7-ndrxOTqfxl9eXhH-5dyhbwra6OuYfafDmf9qy61o4vxEoBZRAy2mRRkxM7IVp6kIt4MmRHFwKrwTr6upxfkcJlV7ugxe_1ZlRw1fmshoqd6pjvYGHQMfocIjLfVxH363ePDIq-T2d1-LjhLXapRaphtr5p_edagDdmDgpy0BYdXgt97cUGJDGhShSq9gmnIt966ArGdbAjgpjKlfD-2Ug6DjiWUi6kFi3N0xhkHt1etEI4HQ3Tv2eiS5G6LTHlMPEfHz6bwifHnEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c631c9b1.mp4?token=clUOBNaArRebYXD-7HMwqcM52xXHWYELeOYCbbFxdy2L5bkuGe1VYHmqCZKjztdP2PDqo3j7-ndrxOTqfxl9eXhH-5dyhbwra6OuYfafDmf9qy61o4vxEoBZRAy2mRRkxM7IVp6kIt4MmRHFwKrwTr6upxfkcJlV7ugxe_1ZlRw1fmshoqd6pjvYGHQMfocIjLfVxH363ePDIq-T2d1-LjhLXapRaphtr5p_edagDdmDgpy0BYdXgt97cUGJDGhShSq9gmnIt966ArGdbAjgpjKlfD-2Ug6DjiWUi6kFi3N0xhkHt1etEI4HQ3Tv2eiS5G6LTHlMPEfHz6bwifHnEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقامات عربی به کانال ۱۳ اسرائیل:  «تلاش‌هایی برای جلوگیری از جنگ بزرگ‌مقیاس جدید در جریان است.  در حال حاضر تشدید درگیری‌ها پیش‌بینی نمی‌شود. ما برای جلوگیری از هرگونه بدتر شدن وضعیت با ایالات متحده در تماس هستیم».</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17086" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17085">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مقامات عربی به کانال ۱۳ اسرائیل:
«تلاش‌هایی برای جلوگیری از جنگ بزرگ‌مقیاس جدید در جریان است.
در حال حاضر تشدید درگیری‌ها پیش‌بینی نمی‌شود. ما برای جلوگیری از هرگونه بدتر شدن وضعیت با ایالات متحده در تماس هستیم».</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17085" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17084">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سپاه پاسداران:    عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17084" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17083">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک مقام ارشد اسرائیلی  گفت: «پاسخ مورد انتظار به ایران شدید و گسترده خواهد بود».</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17083" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17082">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، عیال زامیر:  «به محض دریافت چراغ سبز، ضربه‌ای سنگین به دشمن وارد خواهیم کرد».</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17082" target="_blank">📅 01:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17081">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو ترامپ را از قصد  اسرائیل برای انجام یک «حمله عظیم» به ایران آگاه کرد و ترامپ تأکید کرد که ایالات متحده در آن مشارکت نخواهدداشت</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17081" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17080">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ به اکسیوس گفت:  «همین حالا با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند».</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17080" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17079">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، عیال زامیر:
«به محض دریافت چراغ سبز، ضربه‌ای سنگین به دشمن وارد خواهیم کرد».</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17079" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17078">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ به اکسیوس گفت:  «همین حالا با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند».</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/17078" target="_blank">📅 23:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17077">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImIJyOBXnuKBYPD7jXaPYf6fawlYbS6C4F_bmk8YfyqhgkpE_ngDyESQ-fk-6PGtUj6Ll0Cpyfd93nfqsiyKHR0IcfWOh7D6L_qEip5A7qBH3juLiHxuxsb-_xcBMKNob9-R48vyZpdx7GvTztCUatcgt9G7sp8X2dbo08CdzVVFSUWnhbCmLRaJi5YuBbQ3iMDFDEJBOVdKBwz8ZVvYfC-6dY6vvhzuFfW3u6wMg3Au0H9o1E356q4b3M0qzPaul4WJuVrMc_NZBfdPvghzhn2lFnX0PpJzltUJuQEwJZJqh2yV-01Ym58w-BjMahS9qmB665wnFg9mDU7dMVRjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست حاج عباس</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/17077" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17076">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دونالدک نازنین؛ حافظ ایران زمین !</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17076" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17075">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دونالدک نازنین؛ حافظ ایران زمین !</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17075" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17074">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">— مقامات اسرائیلی به سی‌ان‌ان گفتند:  «اسرائیل در حال آماده‌سازی یک پاسخ قدرتمند به شلیک موشک‌های بالستیک ایران است».</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/17074" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17073">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">— مقامات اسرائیلی به سی‌ان‌ان گفتند:
«اسرائیل در حال آماده‌سازی یک پاسخ قدرتمند به شلیک موشک‌های بالستیک ایران است».</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17073" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17072">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت که حملات اسرائیل به ضاحیه بیروت امروز صبح با هماهنگی آمریکا نبوده و افزود که «او از این موضوع خوشحال نیست.»</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17072" target="_blank">📅 23:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17071">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:  نیروی هوایی تاکنون تمام موشک‌های شلیک شده از ایران را رهگیری کرده است.  ارتش اسرائیل اکنون موشک‌های شلیک شده دیگری را به سمت اسرائیل شناسایی کرده است.  سامانه پدافند هوایی به طور مداوم تهدیدات را شناسایی و رهگیری می‌کند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17071" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17070">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ به فاکس نیوز:  پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/17070" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17069">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیشنهاد من هم همین است.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17069" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17068">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ به فاکس نیوز:  پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17068" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17067">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ به فاکس نیوز:
پیشنهاد من به ایران این است: موشک‌هایتان را شلیک کرده‌اید، کافی است. به میز مذاکره بازگردید و معامله‌ای انجام دهید.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17067" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17066">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش‌های اولیه از انفجارها در تبریز.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17066" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17065">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سپاه پاسداران:    عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17065" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17064">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سپاه پاسداران:    عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-صهیونیستی در منطقه را در بر خواهد گرفت.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17064" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17063">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگر تعداد موشک ها اندک باشد عملا همان حمله فرمالیته است</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17063" target="_blank">📅 23:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17062">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پرواز جنگنده های اسراییلی به سمت ایران</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/17062" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17061">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امروز آتش بس ۶۰ روزه هم‌ تمام می‌شد</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/17061" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17060">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
نیروی هوایی تاکنون تمام موشک‌های شلیک شده از ایران را رهگیری کرده است.
ارتش اسرائیل اکنون موشک‌های شلیک شده دیگری را به سمت اسرائیل شناسایی کرده است.
سامانه پدافند هوایی به طور مداوم تهدیدات را شناسایی و رهگیری می‌کند.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/17060" target="_blank">📅 23:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17059">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسرائیل در تلاش برای کسب تأیید برای حملات به زیرساخت‌های انرژی ایران، در تماس دائمی با ایالات متحده است.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/17059" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17058">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پرواز جنگنده های اسراییلی به سمت ایران</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/17058" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17057">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">موج دوم حملات از ایران به سمت شمال اسراییل</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17057" target="_blank">📅 22:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17056">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdr39eupmcpr4BDOF-rov4hEnKX5LSXqA_oGzhD1A3dmI5nPaRjw0fuDbEJxnYFUnKdjgOk-WA625ZEp89iyTGuqMc1mkUFi1xv-EUlrzVTvk2rcSa8KbV9fn70WMD_u7yXBGuQ6VV6Lqb-vfdQNN-5VdHGjeUlq-yC8kyFD_6NIvIS6qwS7x_kc44_N7JGhg0jpU_EJmme-lm98_6KKU3JAdV-xrTy5MDcIZoklTE934Gh_ejuQW6R1aUD0VlYTikPkEp29q-RxyrPwRv1NgHjm8V0ziwJSxsCN_a13UIVXWo0WTciQPkUzj4GT8G5yy2g9DKQETJNpLpMfn7XByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست حاج عباس</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17056" target="_blank">📅 22:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17055">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به رادیو ارتش گفت:  «شلیک‌ها از سوی ایران به سمت اسرائیل به معنای اعلام تجدید جنگ است».</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17055" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17054">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر امنیت ملی اسراییل ، ایتامار بن گویر:
امشب تهران باید بسوزد!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17054" target="_blank">📅 22:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17053">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">موج دوم حملات از ایران به سمت شمال اسراییل</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17053" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17052">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تمام موشک‌های شلیک شده از ایران رهگیری شدند</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/17052" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
