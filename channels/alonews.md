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
<img src="https://cdn4.telesco.pe/file/i8YK43z2eXTE5KeXgvS0kEYH8oPa8dGmhvM80gb9P29YPlqClGS_c4-i2J0OfNveJcQ7c59vgN8dWHk7aDJnyVQ4mZFyKX1QXt9paeD83s0lrfBdTw_--B5dOr3VWZa1Yc2722IYxri-xn8KqqBu3D1Tcz4vZ4UUt6a_v4a0xzXmWhYeuZ_j3YZ-ChAeyrgzKOvBVBzEeR5baLietXKMi_Zs3BjZqU6oQtpDrendq0UHLfoLDep_yqjGSEFjW92ofFrETUnJaKPwIMs6lSbabt4Hgb6XVvJk14KQee_PfQRVomAycKTMpFpPBfG-DTRCp2ZILHOqP6OvjD2P4jMsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 919K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 11:40:09</div>
<hr>

<div class="tg-post" id="msg-133686">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آمریکا با تحریک کشورهای منطقه سعی کردند مسیر امن تنگه هرمز را دور بزنند و بند ۵ یادداشت تفاهم را نقض کردند و امنیت کشتیرانی را در منطقه به خطر انداختند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/133686" target="_blank">📅 11:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133685">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ایران با درخواست آژانس برای دسترسی به تاسیسات هسته‌ای ایران موافقت نمی‌کند
🔴
ما به هیچ کشوری در منطقه حمله نکردیم و حمله نمی‌کنیم، ضربات دفاعی ایران صرفا علیه پایگاه‌ها، امکانات و مواضع آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/133685" target="_blank">📅 11:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133684">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96903b5d85.mp4?token=qwYcaEQuNNfmBwKTF3VmLlPEY1J3BDqvyWo66eW79UHU6JHnHPsOdwp05Z8LR9FbFOXEUVx2YaGzMK8hK1Sz_E957JnmdgOmFIaEXuqIeuRn8lT6tkOQTes1to2HNh9h_XKYGMAx4V_KSC8iwD_F5GRG6nXOuJzw_d141yx_KzxVHdl_m-WFUTdtsD_sfdLTQMzWTHrOMgY35CMwacc09CCoPlEhdsWOqzFAvCtN-QqqSB6NsN2RpdkB75ebf4BtYEwKphpUEOO7epo5ySkHA7f1Srs5AcFfnqbYp8XKlR1u30PIwbqszXTd1aphRKnoFQjL3tv8DOd7xc1P7ORVWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96903b5d85.mp4?token=qwYcaEQuNNfmBwKTF3VmLlPEY1J3BDqvyWo66eW79UHU6JHnHPsOdwp05Z8LR9FbFOXEUVx2YaGzMK8hK1Sz_E957JnmdgOmFIaEXuqIeuRn8lT6tkOQTes1to2HNh9h_XKYGMAx4V_KSC8iwD_F5GRG6nXOuJzw_d141yx_KzxVHdl_m-WFUTdtsD_sfdLTQMzWTHrOMgY35CMwacc09CCoPlEhdsWOqzFAvCtN-QqqSB6NsN2RpdkB75ebf4BtYEwKphpUEOO7epo5ySkHA7f1Srs5AcFfnqbYp8XKlR1u30PIwbqszXTd1aphRKnoFQjL3tv8DOd7xc1P7ORVWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در واکنش به مرگ لیندسی گراهام: حضرت عزرائیل، عادل است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/133684" target="_blank">📅 11:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133683">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
از ساعاتی قبل تصاویری بسیار منشوری از آرام جوینده همسر سپهر حیدری، اسطوره پرسپولیس درحال پخش شدن است
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/133683" target="_blank">📅 11:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133682">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ادعای ترامپ درباره توافق ایران در مسقط مطلقاً واقعیت ندارد
🔴
دروغ‌گویی بخشی از الگوی رفتاری هیئت حاکمه آمریکا شده
🔴
مذاکرات روز شنبه در مسقط صرفاً متمرکز بر موضوع تنگه هرمز، در چارچوب بند ۵ یادداشت تفاهم، بود
🔴
تلاش ما این بود که با مشورت عمان به سازوکاری دست پیدا کنیم که عبور ایمن کشتی‌ها از تنگه هرمز را فراهم کند.
🔴
متأسفیم که به دلیل فشارهای پیدا و پنهان آمریکا بر عمان، این امر محقق نشد.
🔴
ما در مسقط راجع به هیچ موضوع دیگری نه قرار بود صحبت کنیم و نه صحبتی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/133682" target="_blank">📅 11:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133681">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2509b9fff.mp4?token=Zo4DT4s5JA59kD3r_XOqnullrnrJZKucmWrDvA3fpSHCvDsseonJXZEk0T7KrRlPjJX5I0k22iFs3OwvOcAxrksh8u6akt7VF1ShLU4xP0rx2XUvG2yKpPBqSuBwOV4pjrhzUtgg8YocowpelNr400CAH4ca7sSCYZiQgtCZabhL-b1lzEe5nhFUUAlHhZ_z_3XJ951B4dDKWDujXsGet8MfClcdS4E6w-KmzxcnSawjnVEEGAWMADUpKU_qjbC6AnLoo8qidBTOTPAogNhknhIiNlpBS55wUxRPA3p_n7Km3CLGmaFdXBPV2xBv8g2Mr-CRGXURpN2QUBXRYLYgKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2509b9fff.mp4?token=Zo4DT4s5JA59kD3r_XOqnullrnrJZKucmWrDvA3fpSHCvDsseonJXZEk0T7KrRlPjJX5I0k22iFs3OwvOcAxrksh8u6akt7VF1ShLU4xP0rx2XUvG2yKpPBqSuBwOV4pjrhzUtgg8YocowpelNr400CAH4ca7sSCYZiQgtCZabhL-b1lzEe5nhFUUAlHhZ_z_3XJ951B4dDKWDujXsGet8MfClcdS4E6w-KmzxcnSawjnVEEGAWMADUpKU_qjbC6AnLoo8qidBTOTPAogNhknhIiNlpBS55wUxRPA3p_n7Km3CLGmaFdXBPV2xBv8g2Mr-CRGXURpN2QUBXRYLYgKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: بیانیه سه کشور اروپایی مطلقا هیچ وجاهتی ندارد/ کشورهای اروپایی اصرار دارند که واقعیت‌ها را وارونه ببینند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/133681" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133680">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه در نشست خبری: هیچ‌کس نمی‌تواند جمهوری اسلامی را متهم به نقض عهد کند. در همه موارد، تکالیف ما و طرف مقابل روشن و به‌صورت مستند قابل اثبات است که طرف مقابل با بهانه‌های گوناگون بخش‌های مختلف این یادداشت تفاهم را نقض کرده است.
🔴
در ادامه مسیر هم به همین نحو عمل خواهیم کرد؛ مادامی که طرف در روند استمرار نقض تعهد باشد، جمهوری اسلامی  نیز متقابلا از اجرای تکالیفی که برعهده گرفته، خودداری خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/133680" target="_blank">📅 11:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133679">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه درباره تفاهم‌نامه اسلام‌آباد: در اینکه [تفاهم‌نامه] دچار مرحله بحران شده تردیدی نیست.
🔴
ایران هیچ وقت پیشقدم در نقض تعهداتش نبوده است.
🔴
طرفی که مستمرا مرتکب نقض عهد شده طرف آمریکایی است.
🔴
اینقدر کم صبر در پیمان شکنی بودند حتی اجازه ندادند حتی بازه زمانی یک ماهه در بند پنجم درباره تنگه هرمز دوره‌اش انجام شود.
🔴
از همان روزهای نخست شروع کردند به دبه درآوردن.
🔴
اگر ۱۴ بند یادداشت تفاهم را در نظر بگیریم اجزای مختلفش را آمریکایی‌ها در این مدت کوتاه مثله کردند
🔴
ما از ابتدا گفتیم تعهد در برابر تعهد. مادامی تعهدات خود را اجرا خواهیم کرد که طرف مقابل به تعهداتش عمل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/133679" target="_blank">📅 11:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133678">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما در مسقط صرفاً دربارهٔ تنگهٔ هرمز با عمان مشورت کردیم و اصلاً قرار نبود موضوع دیگری مطرح شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/133678" target="_blank">📅 11:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133677">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
هزینه هر واحد از پهپادهای انتحاری دریایی آمریکا در حملات اخیر به ایران بیش از ۲ میلیون دلار برآورد می‌شود
🔴
سنتکام همچنین از پهپادهای هوایی «لوکاس» استفاده کرده که نسخه‌ای الگوبرداری‌شده از پهپادهای شاهد ۱۳۶ ایران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/133677" target="_blank">📅 10:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133676">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا:
تفاهم‌نامه وجود دارد اما رعایت نمی‌شود
🔴
اروپا آماده کمک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/133676" target="_blank">📅 10:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133675">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر امور خارجه فرانسه: تحریم‌ها علیه ایران لغو نخواهد شد مگر اینکه این کشور برنامه هسته‌ای خود را کنار بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/133675" target="_blank">📅 10:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133674">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
مدیرکل امور مشتریان توانیر : اطلاع‌رسانی در خصوص برنامه‌های احتمالی اعمال محدودیت برق در سراسر کشور، دو روز پیش از اجرا صورت می‌گیرد و بر این اساس، اطلاعات مربوط به قطعی‌های احتمالی تا روز چهارشنبه نهایی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/133674" target="_blank">📅 10:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133673">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر خارجه بلژیک اعلام کرد که این کشور خواهان تحریم کابینه اسرائیل و شهرک‌نشینان به دلیل افزایش خشونت‌ها علیه ساکنان کرانه باختری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/133673" target="_blank">📅 10:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133672">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر امور خارجه فرانسه: تحریم‌ها علیه ایران لغو نخواهد شد مگر اینکه این کشور برنامه هسته‌ای خود را کنار بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/133672" target="_blank">📅 10:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133671">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
دولت مرز ایران-ترکیه را برای واردات خودرو باز کرد
🔴
براساس ابلاغیهٔ جدید گمرک ایران، گمرک بازرگان از ۲۷ تیر به‌عنوان گمرک مجاز برای ترخیص خودرو تعیین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/133671" target="_blank">📅 10:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133670">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
آلن ایر، عضو تیم مذاکره‌کننده آمریکا در برجام: نظم جدید در خلیج فارس نیازمند گذشت زمان است تا به تعادلی تازه دست یابد، اما قطعاً در این تعادل جدید ایران به مراتب خطرناک‌تر از قبل ظاهر می‌شود
🔴
واشنگتن برای دستیابی به توافق هسته‌ای جدید، ممکن است ناگزیر از پذیرش «افزایش نقش و کنترل ایران» بر تنگه هرمز باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/133670" target="_blank">📅 10:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133669">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4CSUSBPPaG8Atdo6PSWOfYH0dRj-cj_68-51TJlmFi-eigEx3A1SvaI7VsSOp_I5fGA81zLSoBgOs5Q4UzfbQF-RCjE5Txb1KersgiKC00UUFQDthLgu5F3aHRf2IAm-HSGwiOtTH6eHFjbKR6Rb4J3F_vFZdczJhANP6DLUM8_YBBN9x3pGsHrtEzeR2CgCPaimKdhR9sGkfRMnjRH_Zxi8GcnAaHzRnlZ1G_kRtsZojbfx65X2xNErES4968Jpvpwq8UmCQzuc3xLpOvx9wP92yUOGWXauxa_Apc39InEi9JaKSE4AHPVPyBAI1GyP6rnIL8I2u1gEXw8bt0kLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: ضروری است شعام یا مجلس مقرره عملی را مصوب کنند که پاسخ نظام درصورت هرگونه سوءقصد علیه رهبر انقلاب، مقامات لشکری و کشوری از قبل مشخص شده باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/133669" target="_blank">📅 10:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133668">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEr51HYyzhCLrxe4DzASKFMzSYntwCVCEYTVbkI8lMOMeHUuzVfmfEicGtjP6ReclaKkvLuAz4c1hLKOgJb9zfLScZuTxVKSfRvRHhcP3-Iienjbf0JesmIQORsXoMU4tD2zwo9mh85_JrjhGkHR2tgZFuSfJExiRaSnN7HzVEau-KFnElV7EGePzHuMowSZNsNE9bnbh1aa-ID9A3w_o_nv5CRQofx944BkrlJ3g-ork2zhoi_qeZ0nD5z0jfmpqXY26YsctNTIm2MJ1NnrANaUgBEVW4OZGVXNwAxdUpaVTDuJGWrZ9uLyY0l9v0UeNhbB2w6skMUFqHp8ewgRFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر عراق عازم واشنگتن شد/الزیدی طی سفری رسمی و در راس یک هیئت بلندپایه عازم آمریکا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/133668" target="_blank">📅 10:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133667">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
انتقال سهمیهٔ سوخت به کارت بانکی کلید خورد
🔴
براساس مصوبهٔ جدید هیئت وزیران، وزارت نفت و بانک مرکزی و وزارت ارتباطات مکلف شده‌اند که زیرساخت‌های لازم برای انتقال سهمیهٔ سوخت از کارت هوشمند سوخت به کارت بانکی را ایجاد و بهره‌برداری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/133667" target="_blank">📅 10:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133666">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0Joor5jZr5SKfXgK8917ElP2hXBJ8QrvlyGU8wOhAlKZPTRxdglTVUuf_Q0Cb2wScbIxpuipSUUjCFrGKvVZaamVuJ7AfhdFg4qDTax4S-pUvIvnp4MtTRsHv5EoX_qXPseu0zZoUuud4yffw5dya-tC1-kfA4sVjMkXZV-hyT3X_p3Xp_59K_iAambB8n9tbzlQtg7HgD_AoCw9KWaOKHpSsILPxfoOuwaLzvtvTtGmnXy66cjqtIaiXhe8iI3KCFDudzrkVQDHOSMdWNkdt3EApzjN6PjesG3Rsh8kG8u6673847WkewYpl5RVWnlCRPx9P2PW5mcO8MfZdO-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارس: تو بندر پهپاد پیشرفته آمریکایی زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/133666" target="_blank">📅 10:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133665">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9627a64323.mp4?token=n1vDZJNkwbnohvrvzL6kGKxHmxQLiyhtpBWUJ-CPVJ5DNUOgpkaXd4pwGf_ABZrU5U0xY1rwvZIQ20Zof-XLvl6mkOBXRZadzAWMf5edq46jSey9R2jFW1NABXkos4xrZghIRi4lhCncPVAou5VmHYx_3dKiia93H4H-7IDnaCJ8IrWYGSuniDpEhFVtG0ERsuUUaGwHhx51LFNx6mgmhyUBUjH905t-Np-VSgLc3sR91GSPekubuhmv7n3mDdcL8XVM7SEA0Nx7V5cA4sw4D-a7ga3ZK0a3pvHmSDCkf6RC_sffOAbrxme7drNzIlouYLoclBfZdZMYZWap_s4CdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9627a64323.mp4?token=n1vDZJNkwbnohvrvzL6kGKxHmxQLiyhtpBWUJ-CPVJ5DNUOgpkaXd4pwGf_ABZrU5U0xY1rwvZIQ20Zof-XLvl6mkOBXRZadzAWMf5edq46jSey9R2jFW1NABXkos4xrZghIRi4lhCncPVAou5VmHYx_3dKiia93H4H-7IDnaCJ8IrWYGSuniDpEhFVtG0ERsuUUaGwHhx51LFNx6mgmhyUBUjH905t-Np-VSgLc3sR91GSPekubuhmv7n3mDdcL8XVM7SEA0Nx7V5cA4sw4D-a7ga3ZK0a3pvHmSDCkf6RC_sffOAbrxme7drNzIlouYLoclBfZdZMYZWap_s4CdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از مراسم ساده تشییع جنازه امیر سابق قطر بدون هزینه میلیارد دلاری
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133665" target="_blank">📅 10:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133664">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سنتکام فیلمی از حملات جنگنده‌ها/پهپادهای تهاجمی یک‌طرفه و موشک‌های کروز به اهداف نظامی جمهوری اسلامی منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/133664" target="_blank">📅 09:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133663">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLf4VdWpMBDHCr5hiXLLlkP3PQmQlka1s7fhNqkHPk8UzOEmC1eg3zl7Ii0gxyYE5nTSDYKfQGxO00OI-jT2QZ0Lt-rYJx8T1cBKVwdzbjFshtcWR2lvFV5gSrK6LzmpFsK1rCgYaAlyS4DaNuLSqMYcTOZLLmOtOCIuHeEKFepTkqkwih8v4rnHP7Qv42ZS9yBDdPYH7T3k8g5sR2Db3zuoaK1jakn4aQ7Rt37VQG2lalOkaWq_XgiqY2TzpU1RzaOxw4ATk3AyY8dBupRXqaXLb4DYwp0ho_e0t0V9s2D3CM-QFe0hFNJvKr--7oPLV7fZAy6KEAAYARit_iqhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنگه هرمز همچنان بسته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/133663" target="_blank">📅 09:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133662">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سپاه: تاسیسات و زیرساخت‌های ارتش آمریکا در بحرین، رادار دوربرد هوایی FPS و رادار کشف شناوری در پادشاهی عمان منهدم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/133662" target="_blank">📅 09:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133661">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/ وزارت کشور بحرین از به صدا در آمدن آژیرهای هشدار خبر داد.
🔴
این وزارتخانه از شهروندان و افراد مقیم در کشور خواست تا به نزدیک ترین مکان امن بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/133661" target="_blank">📅 09:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133659">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e6c1cd43.mp4?token=Hst6eLgymkmi5YUsDXsY1l4XmbXj5v9ZFaIQE16-Xt3VJ4BN4A5K-eMV-hTXY990jKAlxGIo-HfcNTykpcT0qgpXUY1mvnd9ESZdiAqhBHsfzVZlSmsdhC18hqcBer_jF9dLQNEB5F4xcYDKY-1_2YC_KDWEaG9pKxGqSgK3JN8O1B5K24GFrjuMqpf9h0ZEYyDnt3J8GVelGkshQacZ1NE_XQOWyOM5b0Wnc32645LocbxYSOgxGCqoVpVRiP_hcstMMs0OmJSoyoyFRtzZA-YiMDE4TXtZABNN2U-H4-cLvrCqfYm0LbV29_00_CEX5I2F237_7Ebw5SFDnpjtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e6c1cd43.mp4?token=Hst6eLgymkmi5YUsDXsY1l4XmbXj5v9ZFaIQE16-Xt3VJ4BN4A5K-eMV-hTXY990jKAlxGIo-HfcNTykpcT0qgpXUY1mvnd9ESZdiAqhBHsfzVZlSmsdhC18hqcBer_jF9dLQNEB5F4xcYDKY-1_2YC_KDWEaG9pKxGqSgK3JN8O1B5K24GFrjuMqpf9h0ZEYyDnt3J8GVelGkshQacZ1NE_XQOWyOM5b0Wnc32645LocbxYSOgxGCqoVpVRiP_hcstMMs0OmJSoyoyFRtzZA-YiMDE4TXtZABNN2U-H4-cLvrCqfYm0LbV29_00_CEX5I2F237_7Ebw5SFDnpjtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای شاهد در حال حرکت به سمت پایگاه‌های نظامی آمریکایی در منطقه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133659" target="_blank">📅 09:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133658">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaYaPC6r1Zwdmq2e7qm0VHpvHFGbELg4R3dqm9XEyfjaHOmN0Jq3h7m5Deuu6y-ZJAWoBFWJnP12Zd76pPC-oHmrNOtnBSbFpbnYVLlLOMS2GmEBxbc90HvWH5FuumSQi-AyJbOjIr-m_SkBNDOcvTvk6X5bTIZyUwIb8zRo8ZKnWZ2WkPBIDfbA86azA7CMkk2cWBpxN8EZkcMQZAPz0_NzP7nI21Fm5qDQ-b188ThSK6-fvurZSEedQAeoaeGd2M6V8yXS1qMguHmFDTCewe6RXHFC5THVxWhSOHVI-aOlnUVCpfoy3LNQu2KLKy4eca_lxGpIKVVUsx9EAdZpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نامه برادرانه شریعتمداری به عزرائیل!
🔴
شریعتمداری: ممنون که پیام انتقام را شنیدی و جان سناتور آمریکایی را گرفتی اما گله‌ای دارم که چرا صبر نکردی ما خودمان سراغش برویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/133658" target="_blank">📅 09:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133657">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
شرکت کپلر اعلام کرد روز یکشنبه تنها ۶ کشتی از تنگه هرمز عبور کردند که کمترین تعداد در پنج هفته اخیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/133657" target="_blank">📅 09:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133656">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/133656" target="_blank">📅 09:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133655">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
تسنیم : پدافند هوایی ایران، یک پهپاد انتحاری یک‌طرفه "لوکاس" متعلق به نیروهای مسلح ایالات متحده را در نزدیکی بندرعباس رهگیری کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133655" target="_blank">📅 09:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133654">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8c21ebc3.mp4?token=YwHvffiN-kK8WXRiYfrg7l03fJvfNvrU_uumFk_ZvzbVPABVDh9ymPm8iAFJotV0C3EEwJeVbckA_npysFN6jp8o9WFCCZYLdpmNWr-12HZNTTtArT1A9Wc7RoE9f7R3X5lFeE5IeSYpMRd0dBB1KAN94gSpezrmZpbgYtUS_QSOd-moz3z08sktJ3vZm0KigWVfnrKZbROiWAjJqkwsheN7BEmMP33B7tPpwXKPN0z8dTA7Tfk4QeXnWCFa5OwPafISzi8eYEkIUTC20zqGydrVx4PMw7s6eNMvzIPKIA1E_sJdVmwKK2eUAgfrRtPOE1w8et09FdVjTOHIofzRcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8c21ebc3.mp4?token=YwHvffiN-kK8WXRiYfrg7l03fJvfNvrU_uumFk_ZvzbVPABVDh9ymPm8iAFJotV0C3EEwJeVbckA_npysFN6jp8o9WFCCZYLdpmNWr-12HZNTTtArT1A9Wc7RoE9f7R3X5lFeE5IeSYpMRd0dBB1KAN94gSpezrmZpbgYtUS_QSOd-moz3z08sktJ3vZm0KigWVfnrKZbROiWAjJqkwsheN7BEmMP33B7tPpwXKPN0z8dTA7Tfk4QeXnWCFa5OwPafISzi8eYEkIUTC20zqGydrVx4PMw7s6eNMvzIPKIA1E_sJdVmwKK2eUAgfrRtPOE1w8et09FdVjTOHIofzRcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی عبور و برخورد موشک بالستیک سپاه به‌هدف خود در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133654" target="_blank">📅 09:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133653">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ارتش اردن اعلام کرد که چهار موشک بالستیک ایرانی که به سمت این کشور شلیک شده بود را رهگیری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133653" target="_blank">📅 09:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133652">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الجزیره: حرف‌های ترامپ درباره تنگه هرمز با واقعیت زمینی تفاوت زیادی دارد
🔴
تناقض در این است: رئیس‌جمهور آمریکا مدام از چیزی می‌گوید که آرزویش را دارد، اما واقعیت در میدان کاملاً فرق می‌کند.
🔴
واقعیت این است که ترامپ گرفتار شده است. او سعی دارد القا کند که تنگه باز است و این موضوع بر بازارهای مالی جهانی تأثیری ندارد، اما ایران به‌وضوح بر موضع خود پافشاری می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133652" target="_blank">📅 09:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133651">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1591411fc9.mp4?token=V03JY6R-8vrtelkw02NRNwq0umdgLjp1vgDkC-D041UON-Nyz4J206Inf46Qz2PvFK1MIJEQ6MkPHsA934XEkSMupCKTWEKDDmIMi6vX1-wtnWi65FOVP-l4_4lmi1-b6ulrA5QxsQAFNulT2yGXGi8wSXrW8ZOY9hxUxfZgzGM5lzJMijt_oyJK_YLkEIQPovWkbVscJ799lQIR3G4tEvDUxXfECzue1c4WxmD3duGwVB8-a5ON8aXUm8aLVTwKSLw_k-jrkxFfJmuFbdW9JwHwc6kvgnjVzt_KkVMwnI7A6yaRDsHqqn4NhWaeuxpogOZ06fAw34j58TVZIoLsiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1591411fc9.mp4?token=V03JY6R-8vrtelkw02NRNwq0umdgLjp1vgDkC-D041UON-Nyz4J206Inf46Qz2PvFK1MIJEQ6MkPHsA934XEkSMupCKTWEKDDmIMi6vX1-wtnWi65FOVP-l4_4lmi1-b6ulrA5QxsQAFNulT2yGXGi8wSXrW8ZOY9hxUxfZgzGM5lzJMijt_oyJK_YLkEIQPovWkbVscJ799lQIR3G4tEvDUxXfECzue1c4WxmD3duGwVB8-a5ON8aXUm8aLVTwKSLw_k-jrkxFfJmuFbdW9JwHwc6kvgnjVzt_KkVMwnI7A6yaRDsHqqn4NhWaeuxpogOZ06fAw34j58TVZIoLsiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد های اوکراینی شب گذشته به یک انبار نفت در شهر میخایلوفسک روسیه حمله کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133651" target="_blank">📅 08:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133650">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBqZjNhPY9uRH5g_Owj18JxbL7PRls8NmeSoxH4rRlQuiAhvX_16JGhtL0FzDx_mEkKhpUdDpet5J_L9v0l43ckLPa7_IriKzgc5YfF5n1yRG6X95IM1tVnYS-YAWBRoKKb7tOWV7AhxPbo2GpIMse7XcXFUI71bFrdTjQxBHIdkAG_48KfvM_A_g_jXpCjDqz1PyfNCHAV-QH-2gKhldvkw_9hj4U1y7t6QXalaURVxiuMbyLyUHR6UXB2BWNDqaWg84uYSUyj60TpUFmZXvnUYjYZTBboYAf3s-t7WvLBBH2MZkzyoQYgHxTI4mVeXOY743gWIbGCxrLNQlqzj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
59% امتیاز تایید. کاهش قیمت ها همراه با کاهش قیمت نفت و گاز متشکرم، پرزیدنت دی‌جی‌تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133650" target="_blank">📅 08:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133649">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzZHPHmI-BWBtDYTpAu5jjI2pKe82HaJvB671OUm28RF25i82KuZgLntnGJARi5ir6e1etAMuZ0UU06VHalzCGAuN-a1zcJJ1hhqlFz4_7Kpacff0onfmB_jFPj4Kmj7vC-1TTZFdKUPgdSo320volC-6F15lKxmktHqTEQvYRBlxH853HQQgs_xs18ai3WPT5icetvnvgjetf5jpxONQ1_KtMIz5j6j0AbYOeNieFRm3jlA-y15EU4cN38GW9W5GutfIA29yOUSt678M5YZLReFBP4gKjxUejVb6YStfepTGPxfVIwZ5zIV0VUkjnxfbGpudzLIPJ5bLPfmw4yzsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت به مرز ۸۰ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/133649" target="_blank">📅 08:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133648">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
منطقه المینا کویت هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133648" target="_blank">📅 08:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133647">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
تکذیب شایعه قطعی برق اهواز و حمله به فرودگاه اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133647" target="_blank">📅 08:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133646">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دفتر پزشکی قانونی واشنگتن: لیندسی گراهام بر اثر پارگی آئورت ناشی از بیماری قلبی‌عروقی ناشی از تصلب شرایین جان باخته است.
🔴
پس از تکمیل آزمایش‌های سم‌شناسی و بررسی‌های میکروسکوپی، علت رسمی مرگ و نحوه طبقه‌بندی آن به‌صورت نهایی مشخص و در گواهی فوت ثبت خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/133646" target="_blank">📅 08:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133645">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
برخی منابع مدعی شدند که مقر یکی از شرکت‌های تجاری آمریکایی در بحرین مورد هدف موفق قرار گرفته و درحال سوختن در آتش است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133645" target="_blank">📅 08:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133644">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
منطقه المینا کویت هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/133644" target="_blank">📅 08:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133643">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwR0IV7L7aWYEvOws7hWl0bitN9GbEWsCuv4_J5LzqPFvj8ceoeT-OFaCDHv8xesXesMDNlT_ccyT_Dk2B3OdBlLTfsvLnWTy7HDRpF7-i0YCYmTA0fv_fEpL0mTEJsWfIzWNiUZ61Ienp7120pJL7xuUVV1r5rD-BgGIn55SkE_IDqC66XDReTNHboW1zBXmZ4lHqbugpAxfy2yaVe01MqaQFMVlCOZI4b7hSEMHMgmRvIbHrILkD3w7m1930NQRUWT46-NOloR_G8kZYfMgxb8M03j7d0SThSc5UdbleUZay5YqjNVwFhe6I--6QHS9lZPokTVYO48Q0hu1Uc6fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه: حملات امریکا به ایران در ۲۴ ساعت گذشته را به شدت محکوم می‌کنیم/ آمریکا با مداخله در اجرای ترتیبات لازم در تنگه هرمز توسط ایران، موجب بازگشت ناامنی و اختلال کشتیرانی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133643" target="_blank">📅 08:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133642">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
صدای انفجار در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/133642" target="_blank">📅 04:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133638">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-1L2PB_hOU6Q9tzL0Jm8N9T0nB_x17oO-AZUU5WjEjMtts53xItQvcJcBsK5zI9AYsFUKYiKL9YROA98HtG8DBHTAW09yR41VfDXRU5b3sPy4RozH4Uegg5dBIOn-RxCYTayfcsKdkRS4es2onDX24j6wObWWu8sNs6la6TlLtdUtmlGvWfeFGxXrKZDL4YXyEcGSZzOF8Ybgyl9SeiBtt-sa2ufx7ekUvgV98XaN8EfNYOAZIPQCB0imaOA04DsWnLmeODQimKOhANISpbpbTlQLjhgk2ZmXx74pzdNJ7Q4WfkZGA78Ie_M95u9kcFJFsCjrZzPqLKCFt5Hwg4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsi49wdMK9hRRB7QOd0So41GNUo9PCZIoxDbUnB6G3pUurIQ6gGTDVaH_AN9OxnP0PAKhcm3UlBFytAT0qtX2M72zb8WrnEh7_T05UQiU79365OKpeOyGtibeiASkccTxZ7uka4XunX8RBf-Ib643fQepyx5wYyyFtUkgPrYcE_1Hjghl6qYtE-7Vdb3lYfrbSL855dnG5U0EKx4lmMKxalALGfugbiS8Upd8M8FoF1clg8jZq-WrvQK_0xfoWfa_hccmQ3YQLGh4LMsPVwxhQwo6UAUFKqEmWEfsNRB7gNI6RKOV1242XYAKcnLP0zrN0g7AsOjyj8u-2yIlnTuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AxyD6jTdBa6huPYl78mpZrLBpDwTWuoPDXqFhhMk5sZnr_zDGN9QemOKuPHEZ6e9VH3nhVJDnl1waNvNkF7SrleNnhDDm80K9rWku1MU3O_UsVP2vdmpwussY5dvLDTEl0QrpD74FjDTuax0eGJoz87ZPv0Q83lU0VRMOcrSak3Td--BgvPV6gJ7Ob5mLUG8HpMTs6EJAM2tpX7voWMvGRZvKjqN2O9hCScKwlCVVgl7tHXquFjvAtlAkhdNoYLGKSzsOwCMpAAG-PNqCfS1l28DzNuiaxlbL4WWt5QqJr22GnxJvG0aXbxwo_9axjF7ciwKwPmegyvaeDN_CRAdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6odDisTAwp-Qmz9bOIcLguqP5HNSyDswkfv_c8MGnBU6Q7iUrf-8yqIDTOlNCpzv4z2JaN5GYVIDE1bOb6rvMuXKrHRbVrcPM1veFI9_vn9BERjkBb0cOxt85-DutPjCp6qfZte-WNw1KaEG4fsmKAKH4Lm_K82EzkODpY1CfG0scOgEu11H1RMspKhPZKPo63tBM8vEOEvG67Eih6-D6xRsxYgb5Rfnt_ZpM4tg6d6Se6TKP-peTHMLo-H1YsJYMXTsYCLGPr8-gs-HOyfuC3PI1opbN1giD4NqMgY1G6MvYARLZiGBeRsu9otard9_0wV6rq4xD5Qx_74kH0K2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگری از شلیک موشکهای سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/alonews/133638" target="_blank">📅 04:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133637">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فعال شدن پدافند اردن و صدای انفجار در آسمان این کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/133637" target="_blank">📅 04:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133635">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qYdSE_MttnKoF1P6gDtI169-q2lO0bTkwFAiVW03VcVWlHF7G6rHHI4OzRWUMdvCeGydAy2-3n3eRDO3HnU-ZPItrue0gDnTRJiH5h-_li3JcZdP8qVdd9dO24OiQBynJ4gE8PYRVzPiAIyV0BXNUWVoAO2rY3hVvRQo-ZQD_4yZDf7zXZY-rJJWm9A_Dkk_tKb3GzHFtEWpieGQB3scgndOhZo7IQW2jHN43xQFg7em5lOgX9CbQKMQGl0VVPqskH425k6ludmPx96oOEDNJO80kTCRghI332tSBMwORZ9QM_qXzIGWuCaFtVIjQjYiXEMcLOsTfVwJRK09kF_BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_jxFE34kYopIc1TEPyQ2IC9dHHbLdOQ_jq6ESv1xD4YH-3-E1B8hcOpJqkmh0XEXBECTRk7b955EFmxJO7-LXqMPWlgZeHFFm38ARnfQlA-zQHEunuEHoDxkfi-zmmZ2kkammMX-ERdq3tLoQoCqringatlotdW8yAK1jSbbBRe9cB4HNKNp_FZHEMTgI-nV9IDntJnsSR7MT7u843tWhWD_iqAP5aXduwOIWzveKQnw8eVMtVKoqx-oNKH_tCBWRRUfKBqPS3Z5pQ40woPkWLzGaLvuoelSuaAcGhGAld6DLrcwjoTGwkzpHjKaRSiRqumOkbTecwiimW5dD2J4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
از خمین هم موشک شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/133635" target="_blank">📅 04:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh0q1daGIoto5UJXQ63GWAq_dP8MQZsoT_ngf-vigwixMYKo7dpOxk7rP9qEdtLigAZU77L64p9jeQIp--RFZ8wTJRUb44zpIuAPXZNqtvk7hS2g4rYprQyKsh01onDUXmInFrhmfjCuLz7mF0b5ynqYPu2ad7GLouO_n9h6sld1wBYQtD77wMIVzurYuVsdm4p6cpWjnun-3hUtoGS6G4Hs0mdTATYVNzYq1tJ-aNc0nbDyYnfVW_oSbFw-v9WZi11s7-cedTpkGnVowRtgLuklVLMIWpt1_UUOisXT_taYX8UUw7og-it7iR5Pgmm6HmqWryTL3cIog-6xAlhizQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ پیت هگستث:
خداحافظ، لیندزی گراهام.
یک قهرمان بی‌پشیمانی برای ارتش ما، کادر نظامی ما و کشور ما. یک میهن‌پرست تا در اعماق وجودش. او از خط مقدم رهبری کرد، هم در لباس نظامی و هم در سنا. افتخار می‌کنم که او را به مدت دو دهه می‌شناختم.
کار خوب انجام شد سرگرد، از اینجا مراقب هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/133634" target="_blank">📅 04:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c43c2d219.mp4?token=r9OEG-3IGlsfzPEE8JOXKhHITliXJLYaExmtv4BJSOsR8tsne_SOsadQVkNR41_iq9jJQDfR56fD4Pvm74koIMfDt-dMexXWFTVb6MmT3zIiD7siXYkfiHtbX-3EJsRB3OI8FEvGELTuL9iTHHr0bnBIjDXjMCaod7CKCnie_ysOCehBFiAujU9midwFWx7puS8f2epr4MoggqcQkGItxE9GKDRmFhLGAXnmhI-C28Cd3mdCft3mf5G-T2Kp446ZFEgPlnTv497D7wRrZSwjgV2Q-A9Wf4kN2krZ02T0BCBHJA0gRG2XzSI-GgeR2ClG3z8YrZ7yiU4TEPlrUS0AtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c43c2d219.mp4?token=r9OEG-3IGlsfzPEE8JOXKhHITliXJLYaExmtv4BJSOsR8tsne_SOsadQVkNR41_iq9jJQDfR56fD4Pvm74koIMfDt-dMexXWFTVb6MmT3zIiD7siXYkfiHtbX-3EJsRB3OI8FEvGELTuL9iTHHr0bnBIjDXjMCaod7CKCnie_ysOCehBFiAujU9midwFWx7puS8f2epr4MoggqcQkGItxE9GKDRmFhLGAXnmhI-C28Cd3mdCft3mf5G-T2Kp446ZFEgPlnTv497D7wRrZSwjgV2Q-A9Wf4kN2krZ02T0BCBHJA0gRG2XzSI-GgeR2ClG3z8YrZ7yiU4TEPlrUS0AtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی کاربران/ زنجان، سه موشک فرستادن یکیش افتاد نزدیک یه روستا خودمون
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/133633" target="_blank">📅 04:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b8eec877.mp4?token=hT68DHQH16PFtfSmkeQqRpaZ46ufCuq_ozbsD1j7WiQ1TYu3Eza1beC22noVKSyxZQaF9k2CCsG2T9Z0SfbMtJbDbHvL14UnNb5ALu83LYB0ew3fE7DZXkTiIwD4IzV63DRLz0mODBCfDY4YL_gak95NN1OIkDkXn1k9pt-Ap3x6InPOLwGYn18Ua2z-NM45AzCmn0D2zuh5tcPWAqEsaTPGpfsEC7ER-KfgMjt78_Dt6q88BbzbfCYIWZid4zuQm08nhf4gzjfVIqcp1X_e_YBqgtEoZHwTBhdwpZaoIkr5Nr0bAtbP38L_bPeYH7cd9y_lxbq_c45JCc-caqf2Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b8eec877.mp4?token=hT68DHQH16PFtfSmkeQqRpaZ46ufCuq_ozbsD1j7WiQ1TYu3Eza1beC22noVKSyxZQaF9k2CCsG2T9Z0SfbMtJbDbHvL14UnNb5ALu83LYB0ew3fE7DZXkTiIwD4IzV63DRLz0mODBCfDY4YL_gak95NN1OIkDkXn1k9pt-Ap3x6InPOLwGYn18Ua2z-NM45AzCmn0D2zuh5tcPWAqEsaTPGpfsEC7ER-KfgMjt78_Dt6q88BbzbfCYIWZid4zuQm08nhf4gzjfVIqcp1X_e_YBqgtEoZHwTBhdwpZaoIkr5Nr0bAtbP38L_bPeYH7cd9y_lxbq_c45JCc-caqf2Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/سپاه موشک شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/133632" target="_blank">📅 04:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری/گزارش شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/133631" target="_blank">📅 04:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سی ان ان: حملات به ایران هنوز تموم نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/133630" target="_blank">📅 04:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c70af372b.mp4?token=W67Gn4tahi78GdcBzMbOPDv_36jnlVO1qAAIwYk7Qx39eiI5K-b2gKA5mowosxi94f2nSDgPXEk5270P-fYal8p4kOyB85n_mlufmQo5b1wtOqIi8rhktHB6hRzL6Lpci77H8SkoH8GDyp01gQBgeM1EEe9dVIqT6-JF4i72bB0pzVegxntaGlurCZsbJYIfC8e8l4DIUlFlp4sUr_CYsUmb0wjxacDTqee_r1C3RwWPfD7SXFsQxQXz-AFcZsom7u0SuTG3OSngC_WAjJUEbn_ICSfjhsJ5j9lujsYjkMGh_q5xdub3rizTOTL377B31H_r00hUuiLZ5lzyID1gbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c70af372b.mp4?token=W67Gn4tahi78GdcBzMbOPDv_36jnlVO1qAAIwYk7Qx39eiI5K-b2gKA5mowosxi94f2nSDgPXEk5270P-fYal8p4kOyB85n_mlufmQo5b1wtOqIi8rhktHB6hRzL6Lpci77H8SkoH8GDyp01gQBgeM1EEe9dVIqT6-JF4i72bB0pzVegxntaGlurCZsbJYIfC8e8l4DIUlFlp4sUr_CYsUmb0wjxacDTqee_r1C3RwWPfD7SXFsQxQXz-AFcZsom7u0SuTG3OSngC_WAjJUEbn_ICSfjhsJ5j9lujsYjkMGh_q5xdub3rizTOTL377B31H_r00hUuiLZ5lzyID1gbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پادگان باکری دزفول در حال سوختن
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/133629" target="_blank">📅 03:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HglBZvMDvDw-RDtbcVlkWzSpTqBWrhxFHQ609ahho_z2k2Xizzwz-yzzDUEn5clXKh4WyiwSQcX3gjxEofa-nyehUcbgXND_k8suYt9q542Nvh5jE1HEqwYuRprO4PnlOdgWK0VTeY4uy8vGmjygCGCAixbCn4C4ocbtY5goYCvq_f52d1739a_rUJueHSpHvOOu2O0InH_0OLyTUuSX8mI0nTWwpVrBjuCPV5Hy1BzWW64kaxES7_hrfwAyHcqCUkbkCVaGTthb6MO-XvD9t1Ikfj8-MRjtp8q_XChXxcbBmG8-g74AVfMKkncZ-H3qpE5QAkH41MHdnEHBl8PhMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از انفجار عجیب ساعتی قبل در امیدیه خوزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/133628" target="_blank">📅 03:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
خبرگزاری سی‌بی‌اس:
حملات امشب آمریکا علیه ایران تموم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/133627" target="_blank">📅 03:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133626">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f41a3af54.mp4?token=QA5U_yuZQ46TRK8D1qrtCg4BN4yuXtkLiflP3f1ROXVJoYzYODkJnyBu26ttIhXHctbOH1sIos8rPGow1F5Jg-zcu2uZVIt9mEoIk6CFwGvkbSIGDA7tvdu4cdqCELGP5i5GBnGHdfQwyhI4OxrHYM4l3qm5RIEL5LaUbqXqGnTLcZxE8-CoN2Wmy_Yah99xS7PbMlTDHugP0ssQLYjf7rg4UiaMRs1ZKcZo59jDzSknS8aHFITcIsdX7szAo6U7uVqmlYXRvAaw1dVFkH9QtpFDfDILu3NJY97t3JC6Emd70ari1BXSxlgj4fA-p186c252_-IIxHv8Oc9vLQTkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f41a3af54.mp4?token=QA5U_yuZQ46TRK8D1qrtCg4BN4yuXtkLiflP3f1ROXVJoYzYODkJnyBu26ttIhXHctbOH1sIos8rPGow1F5Jg-zcu2uZVIt9mEoIk6CFwGvkbSIGDA7tvdu4cdqCELGP5i5GBnGHdfQwyhI4OxrHYM4l3qm5RIEL5LaUbqXqGnTLcZxE8-CoN2Wmy_Yah99xS7PbMlTDHugP0ssQLYjf7rg4UiaMRs1ZKcZo59jDzSknS8aHFITcIsdX7szAo6U7uVqmlYXRvAaw1dVFkH9QtpFDfDILu3NJY97t3JC6Emd70ari1BXSxlgj4fA-p186c252_-IIxHv8Oc9vLQTkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به امیدیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/133626" target="_blank">📅 03:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133625">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDiWFdkGiv-w-G-buomGJPT7LO8sKBLhpphtKoWf086Dr9Hpd_xzWhH3SVWS9gRDavS_49uA78jGLkJIAKB2i31pHBfvLbF-p8hCyhAsxF-zhsSJKby2Wp_WN3JF3dDax6du1_04w2rPpN7OwlQzTFx_0zGm3iZcGtwymCCPe4K6tUcehh_80atdMLd96VtnDv_iMt3ZZILo1U-hJOFyiin59GNW73HGMt7lqYqYusl1og7hlwpjMfJPu2jybhYf7dKEWhKHU36N753VCbuqyTOLagRbD-veaV3Bb0snrcwsAelkMMrsh990jSsS8BMjr0zHJ8YS-WhIxyDdZHtbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون پرواز ۱۰ فروند هواپیمای سوخت‌رسان ارتش آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/133625" target="_blank">📅 03:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133624">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
گزارشی از انفجار در فرودگاه آغاجاری خوزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/133624" target="_blank">📅 03:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133623">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc7be2cab.mp4?token=azTT_0gPu94WccIV9BaK9B8SdZ6RDE0nkJpIxjUwIGdDwkC9tN_xPQKwI6NXtO6Ethv_TQ5ywfUnlrfV2Og0fBuJsyV92Rs5c6KCK2_p41B4L6yuF5IvdlFhWlq6ZrI_FRGFo_MPhpxz92eyPA1XH_2-NULdVoC0QVtKcHETX2dqZYA2We0nQP_DOANpsa3GuYZYaL9uWjNxzeBF8-yi-x2y4ZpO4VaRT3w_ODC7UlsPQ--Bpn5p-WK6Aa0VAq0fC_sjwJVMBG5CDWM1UwENpiiA6KJxfUTxmX3y-vm6KeCnx3mKX2_YXkNrve99bwV1wpWo1BNUDYCNyohdIpAiQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc7be2cab.mp4?token=azTT_0gPu94WccIV9BaK9B8SdZ6RDE0nkJpIxjUwIGdDwkC9tN_xPQKwI6NXtO6Ethv_TQ5ywfUnlrfV2Og0fBuJsyV92Rs5c6KCK2_p41B4L6yuF5IvdlFhWlq6ZrI_FRGFo_MPhpxz92eyPA1XH_2-NULdVoC0QVtKcHETX2dqZYA2We0nQP_DOANpsa3GuYZYaL9uWjNxzeBF8-yi-x2y4ZpO4VaRT3w_ODC7UlsPQ--Bpn5p-WK6Aa0VAq0fC_sjwJVMBG5CDWM1UwENpiiA6KJxfUTxmX3y-vm6KeCnx3mKX2_YXkNrve99bwV1wpWo1BNUDYCNyohdIpAiQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی که تو ایتا منتشر شده مبنی بر هدف قرار گرفتن آبراهام لینکلن، فیکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/133623" target="_blank">📅 03:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133622">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گزارش‌هایی منتشر شده مبنی بر اینکه کلانتری روستای مالحه (شوش) در خوزستان در حملات هوایی آمریکا مورد اصابت قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/133622" target="_blank">📅 03:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133620">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
تعداد زیادی سوخت رسان از ریاض عربستان بلند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/133620" target="_blank">📅 03:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133619">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مقام آمریکایی به نیویورک پست:
انتظار می‌رود امشب شاهد حملات گسترده‌تری از سوی آمریکا علیه اهداف نظامی ایران باشیم، حملاتی که از حملات قبلی نیز بزرگ‌تر خواهند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/133619" target="_blank">📅 02:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133618">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
اخبار اولیه و تایید نشده‌ای مبنی بر هدف قرار گرفتن گذرگاه مرزی "چذابة" متعلق به ایران در مرز با عراق منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/133618" target="_blank">📅 02:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133617">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
شهر هایی که مورد حمله ارتش ایالات متحده آمریکا قرار گرفته اند
🔴
قشم
🔴
سیریک
🔴
بندرعباس
🔴
جاسک
🔴
بوشهر
🔴
خنداب
🔴
بندر ماهشهر
🔴
بهبهان
🔴
اندیمشک
🔴
دزفول
🔴
اهواز
🔴
آبادان
🔴
خرمشهر
🔴
گسترده تر شدن حملات ارتش آمریکا نسبت به حملات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/133617" target="_blank">📅 02:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133616">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
6 انفجار بندر خرمشهر را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/133616" target="_blank">📅 02:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133615">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
جنگنده‌های نیروی هوایی ارتش ایران از پایگاه هوایی وحدتی دزفول به پرواز درآمده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/133615" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133614">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تقریبا کل شهرهای خوزستان انفجار داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/133614" target="_blank">📅 02:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133613">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
انفجار در هویزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/133613" target="_blank">📅 02:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133612">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوووووووووووری/جنگنده در آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/133612" target="_blank">📅 02:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133611">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
انفجار مجدد در دزفول
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/133611" target="_blank">📅 02:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133610">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
انفجار در سوسنگرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/133610" target="_blank">📅 02:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133609">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/عمران عقیلی، رئیس واحد ارتباطات عملیات ویژه در فرودگاه اهواز ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/133609" target="_blank">📅 02:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133608">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
انفجار در اندیمشک
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133608" target="_blank">📅 02:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133607">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
چندین انفجار در بندر خمیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/133607" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133606">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
تیپ زرهی ۲۹۲ دزفول توسط آمریکا هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133606" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133605">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
لغو پرواز های مشهد به تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/133605" target="_blank">📅 02:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133604">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
به دلیل نبود پدافند موثر، هر موشکی که شلیک میکنن به هدف میخوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/133604" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133603">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوووووووووری/پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم
🤩
@khabari_18 | پروکسی متصل</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133603" target="_blank">📅 02:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133602">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
حمله به امیدیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133602" target="_blank">📅 02:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133601">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/133601" target="_blank">📅 02:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133600">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/133600" target="_blank">📅 02:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133599">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری/انفجار در دزفول
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/133599" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133598">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi1go8E-kMFX3RUo4KzvY21FC7rG9IJFc5G9hq4G67DEfDjMwa2KWPb6Xjfd8MK-e6r9C2NYaOBeusQxeHeQ-yI3V7sZp6C3CCyMB-cbPecf6cR8FTgC3zS3_44epwUux90CHgLmXg08BoA_n0KnDxAYYx3gD7bbqdUjiduYOt_-E8PK9DH3vHV9UL_nprO_C-phoAx2maIj-pvS7tsiCLdqG-NcLI9IZlHNJbu8NPQI97wituwgQdCQj3u-VBwRuRzIXPTv4umFGpHh0nUde3shBDuG37pJsJcKcTcaSenLRz7XscvFkK9lN-SNYi9vMspYvULWTKBibz8rD4qU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به فرودگاه اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/133598" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133597">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
جنوب ایرانم شده عین جنوب لبنان، الله اکبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/133597" target="_blank">📅 02:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133596">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
جنوب کشور زیر حملات شدید هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/133596" target="_blank">📅 02:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133595">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
انفجارهای شدید در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/133595" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133594">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری/گزارش شلیک موشک از کویت به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/133594" target="_blank">📅 01:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133593">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پرواز جنگنده در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/133593" target="_blank">📅 01:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133592">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
به گفته یک مقام آمریکایی، نیروهای مسلح آمریکا یک موشک کروز و یک پهپاد ایرانی را رهگیری و سرنگون کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/133592" target="_blank">📅 01:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133591">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/انفجار در سیستان و بلوچستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/133591" target="_blank">📅 01:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133590">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فرودگاه اهواز رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/133590" target="_blank">📅 01:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133589">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/133589" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133588">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-mxTFe_Xis-l1O4_hXexKpciPPDcKix1CqFnpPJl4dPH2IMzEdp4K1fyoztDk_sa1G4T7KYS6SqWzWw-XJeOp0vo0tkP2cBOjHH_g50ObXhLTBbDDmHZei6GHwHAkyWD-z_scXztvJZf7Ny7MBx7ashWbrCafXFAs4JxjcFCAqj0w7G-x8R1KmKPEbBDQjlNhOcfh0IwWz26DC_t1lkReVLOs-hFAa9LSw05EUNVBIevqvdbjpkPadPYVfmNpPLpD3p-7TWeh9d5nOg7-v2aNYxBg7S7AiPRprTrM5paHdu8rhQMqeJNOqJypI7ODUkWfdpbwsHkXpdcrOch22bPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/133588" target="_blank">📅 01:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133587">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/133587" target="_blank">📅 01:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133586">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری/اعلان وضعیت قرمز برای فرمانده های کشور ارسال شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/133586" target="_blank">📅 01:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133585">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
انفجار در شهبندر هرمزگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/133585" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133584">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری/انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/133584" target="_blank">📅 01:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133583">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوووری/حمله به خنداب اراک
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/133583" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133582">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYhqV0jOpBtv6-h6kuwJGo64bBo6fhXTtnYhcojo9CEkqeBhG7HQWFoLCYP07YQg-0R3pPDRzYkQHn45qiMZBgdHxCps8lret3s5t63GgUTMH_o8GTq7moC9AsK26xtTgfaffiiGuQ9NJzH4KuR5acLLrNuF8KQouNQNVqNnSL07uwmCb2c9ezbGwPhux_ZSKpCy99mRLI4Dc_Ll3GSwoRF0Fk0xmMF__u0vmGQ0t5p3aIc2SGbkGTQbWpzm-m3sbxay5oBuEYlqQGX2fsi9jDWBKE2E2mU4DPFARTPBRf2qDjf-N_W7UZDGvvkEFepTz_tAQCijlyHCuPe6S08yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/انفجار عظیم در سیریک
🔴
خورشید از جنوب طلوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/133582" target="_blank">📅 01:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133581">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری موج جدید حملات به جنوب ایران آغاز شد
💧
Rainbet.com the #1 Non-KYC Crypto Casino & Sportsbook @rainbetcom
🗞
@iraninterpshm</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/133581" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
