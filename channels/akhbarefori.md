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
<img src="https://cdn4.telesco.pe/file/djbIAeR2SgH0QLY90ep8InQ7S2x7dTt7vaf_Hd-HMmhSscdnBW5BfC4NoNUSKPvBdhwvqIILWFpVpype44retZSXUP-l0ki5J8aLZjlzHvcDk2t7Bcwy656O9lFQJT4hzJP96DDam0LdYPoV5GVhFQHrQtqI9CTL9OC8Jxy6XBQZf6O4wWLLdBsFxWUpTrbihJ8TY_6Dvt28k5uFD81sGVsSmK19bIdlDuDuaAQ3GA640CBurIiBkQjllf7pU-6GkdusZiEGhfFyDeX491J7XFkfugg_6ntBAuIu-LoDR9ftQ6v7bi8nWt2PhsCmw6kc_k1edCcizgizQ7QSnYfQNg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.13M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 10:22:26</div>
<hr>

<div class="tg-post" id="msg-681885">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b679be5bc.mp4?token=m0V1vClKjWYr8D5t4-_CSuwJ6zXzB08YlvfsEqqsTLeyzBBRK5P4QaHWsKOK1fPm9O3rjk2nrqrduxcT_4gGTdElXjt1ArmjGjjBuqyvN4Gww2KzGNPkOG4JWxd-fWdpmvEmhS6CJQx_FZ-HBMuXlOpqmKXOhqjzZo8Iz6LNdcFMVn4Cq_pAQKlu706wUI7OWSXCBlYNxUMivfXHVL6jZW1q4SCJqGL_WIYATmCqpgS--uZTIpj_WpPubDBFuApARTRPaouly05oapISs4LlEBWVsJc83FzDvDeHI6jUWCfvbdJ5atXUdLHiBNHcCszpf0UO5K5my6_8tNOowQQBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b679be5bc.mp4?token=m0V1vClKjWYr8D5t4-_CSuwJ6zXzB08YlvfsEqqsTLeyzBBRK5P4QaHWsKOK1fPm9O3rjk2nrqrduxcT_4gGTdElXjt1ArmjGjjBuqyvN4Gww2KzGNPkOG4JWxd-fWdpmvEmhS6CJQx_FZ-HBMuXlOpqmKXOhqjzZo8Iz6LNdcFMVn4Cq_pAQKlu706wUI7OWSXCBlYNxUMivfXHVL6jZW1q4SCJqGL_WIYATmCqpgS--uZTIpj_WpPubDBFuApARTRPaouly05oapISs4LlEBWVsJc83FzDvDeHI6jUWCfvbdJ5atXUdLHiBNHcCszpf0UO5K5my6_8tNOowQQBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من چطوری می‌تونم پرچم وطنم رو پاره کنم؟!
🔹
۲۶ مرداد، سالروز درگذشت عزت‌الله انتظامی. او از حاجی واشنگتن و سکانسی می‌گوید که باید به پرچم ایران بی‌حرمتی می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/681885" target="_blank">📅 10:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
همتی، رئیس بانک مرکزی: مطالبات ایران از بغداد پیگیری می‌شود
🔹
معاون سیاسی سپاه: تنگه هرمز در صورت عمل آمریکا به تعهدات تفاهم‌نامه اسلام‌آباد باز می‌شود
🔹
پاکسازی لکه‌های نفتی سواحل هرمزگان به پایان رسید
🔹
رئیس پلیس فتا فراجا: ادعای فروش سؤالات کنکور کلاهبرداری است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/681884" target="_blank">📅 10:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
آیا آمریکا به دنبال تدوین چارچوب جدیدی برای مذاکرات با ایران است؟
احمد الرهید، خبرنگار الجزیره در واشنگتن:
🔹
آمریکا به‌جای تهدید نظامی، بر تشدید تحریم‌ها برای بازگرداندن ایران به مذاکرات متمرکز شده است.
🔹
ترامپ درباره پایان مهلت تفاهم‌نامه سکوت کرده و استقرار نظامی در منطقه به‌عنوان اهرم فشار ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/681883" target="_blank">📅 10:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73abdba8be.mp4?token=Cuu-LDL9UA-B91VSXAGwAuHME76qGgK2Q6p39ZiG3Y1G1s3nEGL_McO7Mo3V6zIj3fl1ShjcvbepfWgRz39e6Yw7NqifxhSjb3lNIdsL6Mn0LDQ90ajg2-7ajwiCXen2qUyS05rFRal1R2xNSxswG9LCo-bI4ftfJUH5EZhyHyJhL_vObruYqdKY6lgAIxWjqObT-50IF3lvcGKYqkEtNYeIOooiWT3WlnsnEv-oFCtRo_B685KV2DAfDwaqXc5lfHOGIWed4lW_Xe4eg6g63ZIwiadPTX6s90fJam5Dn7OJlmav46JfIsgo4h65RTPOciPX9PoOBoHGUr1eAVrdSKj8fMYntcdTXABPDmCslcFCpqU-7ri55EDSOXZsn4Av8O1atmDqzZpx4Pzzf9zqHpsKa4BgNnYop-9jtzgtEMQ4HNyHAFdG_Qb-JbgChL93X4wjE2Zjy-CFXVzOsewMDjCue5ilpMrr_dnFMbLA5_O3QQRm8NtQQfgsQsAwl-PV7Pp11Ox1zOhYW9Oix-_S91OUxyR_L6wu88c1QlycieSRtKh332wIfwFYME8xvRjQsuciiBK1FH7uuTAzJoDoWOzzB-ayUbB9Q2UtAKiIkk1KQIAKY-4sXiFjt5kI2P4BofbMxkvJl6mFYb1UBKPh6HJ3_wn8ZSYbXtSPsm8GZaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73abdba8be.mp4?token=Cuu-LDL9UA-B91VSXAGwAuHME76qGgK2Q6p39ZiG3Y1G1s3nEGL_McO7Mo3V6zIj3fl1ShjcvbepfWgRz39e6Yw7NqifxhSjb3lNIdsL6Mn0LDQ90ajg2-7ajwiCXen2qUyS05rFRal1R2xNSxswG9LCo-bI4ftfJUH5EZhyHyJhL_vObruYqdKY6lgAIxWjqObT-50IF3lvcGKYqkEtNYeIOooiWT3WlnsnEv-oFCtRo_B685KV2DAfDwaqXc5lfHOGIWed4lW_Xe4eg6g63ZIwiadPTX6s90fJam5Dn7OJlmav46JfIsgo4h65RTPOciPX9PoOBoHGUr1eAVrdSKj8fMYntcdTXABPDmCslcFCpqU-7ri55EDSOXZsn4Av8O1atmDqzZpx4Pzzf9zqHpsKa4BgNnYop-9jtzgtEMQ4HNyHAFdG_Qb-JbgChL93X4wjE2Zjy-CFXVzOsewMDjCue5ilpMrr_dnFMbLA5_O3QQRm8NtQQfgsQsAwl-PV7Pp11Ox1zOhYW9Oix-_S91OUxyR_L6wu88c1QlycieSRtKh332wIfwFYME8xvRjQsuciiBK1FH7uuTAzJoDoWOzzB-ayUbB9Q2UtAKiIkk1KQIAKY-4sXiFjt5kI2P4BofbMxkvJl6mFYb1UBKPh6HJ3_wn8ZSYbXtSPsm8GZaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا فصلش تموم نشده حتما این دسر لایه‌ای‌ انبه رو درست کنید که خیلی خوشمزست
🥭
مواد لازم:
🔹
انبه دو عدد
🔹
خامه صبحانه: ۳۰۰ گرم (یک پاکت و نصف)
🔹
پنیر ۱۵۰ گرم
🔹
بیسکوییت پتی بور دو بسته
🔹
پودر قند ۶ قاشق غذا خوری #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/681882" target="_blank">📅 10:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681881">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZm7XL63E8xsTMFRG705eRnD7VE4E1Pa053x-NkB2qErlWalSLuG5vkdJ1Qz_Arc0dmCa2yGDvb9hMo7LvB-2Z4Uz5ZFErcQK8OHD-bBZQ7AjwF2rpZTuiGkGDUZwbpgoyQsifzojH3ioBecdHN74tsZHMjjUi7DbFQZSyrYo8vGPOWsG3j6nGZDuVPMr93N2RVc-VPQaIWeI1GfWxplW5xQ0s0Ffkq8MuVbcvBqrHT4DVv3tM5WdBjn8Du2qyD2SFmeAq_vCWBCB0hLzMqZPWmtaBQ5ERY5bkoJTft-Szv9BM3l6QMplY-ROgN6LkReARt4telbE5kSIh391sZznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه در حال ایجاد پایگاه‌های پهپادی مخفی در نزدیکی خاک ناتو است
ادعای تلگراف:
🔹
روسیه حداقل ۱۰ پایگاه جدید پهپادی با ۵۹ ریل پرتاب در مرز بلاروس و اوکراین ساخته است
🔹
پهپادهای دوربرد پیشرفته، قابلیت رسیدن به لهستان را دارند، نگرانی از تهدید زیرساخت‌های ناتو در درگیری‌های آینده./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/681881" target="_blank">📅 09:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681880">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
وزیر جهادکشاورزی: به خاطر محاصره دریایی، جنگ با شدت ادامه دارد
🔹
در امنیت غذایی کشور و موجودی کالاها مشکلی نداریم؛ اما قبول دارم به خاطر جنگ و محاصره دریایی هزینه‌ها بالا رفته است
🔹
دولت طی دو سال گذشته هیچ روز آرامی نداشته و هر لحظه درگیر یک حادثه بوده است/ از همه چالش‌ها عبور کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/681880" target="_blank">📅 09:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681879">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coIxzxfAaJHZe6ukP3-tjERmmKgZhKPMEuVrcVX71O9qRBVbf8J9QSmlc-DyoO56h2pJmDlExWYbF7EUHCXDPg4BQxpH4tHaKQBJ-gfnm0wr9zqzRtyCL_WnwvgBpW4Jqne_IrYHDfc32uR7_Jnc2-105y5bgBevdp1mKg7KnQBv_nF2m8el6hELJHihQfjiCDE7rBOA2yQlnDVmXI6OPllQcwe3-LPbt15padpNxvHuDjzZeRn9u3GU5egJYCpJIYem4nQmuT8Bjx_1MywdJkjAyha1l5RWc-CwnbV-YGC6frN1PJfJpYD2MPWIXr6qKdfE4cEKpvH_4Tndjjx4sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس در آستانه ۵.۹ میلیونی شدن
🔹
شاخص کل بورس با افزایش ۱۲۸ هزار واحدی به تراز ۵ میلیون و ۸۵ ۹۴ هزار واحد صعود کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/681879" target="_blank">📅 09:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
کشت غیرمجاز خشخاش در کشور محدود است
معاون مبارزه با مواد مخدر ستاد مبارزه با مواد مخدر:
🔹
کشت خشخاش و شاه‌دانه در ایران ممنوع است و موارد مشاهده‌شده بسیار محدود و در مناطق صعب‌العبور بوده است.
🔹
با کاهش کشت خشخاش در افغانستان، قاچاق به محموله‌های خرد و مواد صنعتی مانند شیشه تغییر مسیر داده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/681878" target="_blank">📅 09:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681877">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqD3NkXFFRwN-ihcP9Ui0Ya_o4IpeHdvuNxk4i4kayLdbV8anlN0IrK8Xl3RewuBVRrnvKLisNZtCOriBGhdWP9wfV69_yu9Yd0_LgXWob3aeclllF6gPKHOfojrfi_4D1S_Plxbp2QkNj-9WwWH_bzRHj1jQ6s4OLm0Of-_rcI-UeoUc_dADdPKm3Y03Wjw1ozxT9lOolk0MW9J7Xq2xUOIGdSIfAmFVqhMetfHSio-KhtL7512p0NKpJq1_o6URin2rw6LNzoW5BCX4A8g5IfuW-KOkpPEYN7qKoryc6IRqZd4IRZO7gqy-8fpleHL65iYiKrZ-_AVaMWUb0te9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه سی‌ان‌بی‌سی: گزارش‌های متعدد حکایت از آن دارد که شهریه تعداد زیادی از دانشگاه‌ها و مؤسسات آموزش عالی در آمریکا به بیش از ۱۰۰ هزار دلار در سال رسیده و آموزش عالی را برای بسیاری از جوانان غیرممکن کرده است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/681877" target="_blank">📅 09:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681876">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70be46871.mp4?token=hXYG9Zoh9YdTq38OPR1heBHr-uBpVECoO30WBXo7gYrOA_4v1i6giQo5PTHzpPHlsVx3-JW3V55entitc1ySAJ3WaVCXADsQv3_2zA45clXqBFFN935ZRQmVb-Xwzic6PWLVKbuA7RRb04mw-AWp7f0EZI6HY8PzcgLiu7t_3VplKERAstzMZwK6cobcOekzlC-mLPoyV9f-ELaIM9yA169lFV-k3tqfbjCdlv-6J5hdGSlDKMDXgTm763wvc24IsSmyEJXprHrJhw-16BOLYMVqrIek5tSxRtu4uW_Tj7Wn_Ovm4eg56W-7Ko3FikoM1MJP-DLN1yrtj8ZlyP-ZTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70be46871.mp4?token=hXYG9Zoh9YdTq38OPR1heBHr-uBpVECoO30WBXo7gYrOA_4v1i6giQo5PTHzpPHlsVx3-JW3V55entitc1ySAJ3WaVCXADsQv3_2zA45clXqBFFN935ZRQmVb-Xwzic6PWLVKbuA7RRb04mw-AWp7f0EZI6HY8PzcgLiu7t_3VplKERAstzMZwK6cobcOekzlC-mLPoyV9f-ELaIM9yA169lFV-k3tqfbjCdlv-6J5hdGSlDKMDXgTm763wvc24IsSmyEJXprHrJhw-16BOLYMVqrIek5tSxRtu4uW_Tj7Wn_Ovm4eg56W-7Ko3FikoM1MJP-DLN1yrtj8ZlyP-ZTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از ۶ متهم پروندۀ قتل حمیدرضا رجب‌زاده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/681876" target="_blank">📅 09:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681875">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqlrsmm46evoSyyirpmgDme5mJ8h6u-oUBeWCytJTduWmoxa7H9Bgtm1HAinALtyPE3KwmayU1z95eLDOA0d257sv3qr0A8SLp2YyvHvJaHTXzyCrqddgu4yan-LTocGdozzgXFYN1CydtWCiFT280HcSjAQlJZ1LZZmVL6DHEMCP4GhP4ukEkJ2qz9DdGUsWTm5b0Un9vzTemQCHZc2EvuY8RFeJ_a_mPQTxmQDl6cbYjAmvzism5EkUzgaDp1HfLg8aFnRaIut5DdnjhmPiu6eJPp5g-FWgGp_1Ta-0DT35aHTrxQeel7LItYnW59lnT47qEi4LJAFFY7PmpP1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت با انقضای تفاهم اسلام‌آباد گران شد؛ هر بشکه برنت ۸۹.۴۰ دلار
🔹
توقف تردد در تنگه هرمز و بن‌بست مذاکرات، قیمت را بالا برد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/681875" target="_blank">📅 09:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اختلال در سامانه‌های فروش بلیت قطارهای مسافری
🔹
درحالی فروش بلیت قطارهای مسافری از ۸:۳۰ امروز آغاز شده که کاربران از اختلال گسترده سامانه‌های فروش خبر می‌‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681874" target="_blank">📅 09:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681873">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
قائم‌پناه: ناچاریم به دلال‌ها نفت بدهیم اما هدفمان جمع‌کردن کاسبی تحریم است
معاون اجرایی رئیس‌جمهوری:
🔹
در زمینه نفتی که ناچاریم برای فروش به تریدرها یا دلالان بدهیم، پرسش‌هایی همچون زمان فروش، چگونگی بازگشت پول و تامین سلامت محموله تا بارگیری مطرح است که این شرایط می‌تواند زمینه کاسبی تحریم را فراهم کند، هرچند دولت در پی برچیدن تحریم‌هاست تا دیگر کاسبی وجود نداشته باشد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681873" target="_blank">📅 09:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681872">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcaYcH-7AjisJUHn6mLTVupuFO7taZLDoQmwlJH0t0ilON6zBHtroxnH7UR9IZSLSDC__L3U86amtq8PVRRh-w8Aoio9TsCDlWGXpXibmvUH8anXE43lbzvxKDiUtWPh1fQRDGXL2UWSuXVw8lVmqnwsEqIpgKblvSV3rbQA0qRgzgm4mZW2I4GxsgSGDKTBiMWC4N-3vXlnN2oLaYYrp4J6WsZu9Ogot-xPkfUIJWn39j7Go38TsyAkOgqLizkHJhvnyMfJQkrmBbP8XKPjOgUKGFWIGxbzk9DFB5D2K-_lZwkS5bC59iEOl-uCXNvcvUVQH4UBmKvvnegzuTkF7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دریافت کارت ورود به جلسه کنکور از امروز / چگونه کارت آزمون دریافت کنیم؟
🔹
توزیع کارت ورود به جلسه کنکور ۱۴۰۵ از امروز آغاز شده و تا چهارشنبه ۲۸ مرداد ادامه دارد.
🔹
داوطلبان باید مشخصات فردی و آدرس حوزه امتحانی را روی کارت بررسی کنند، مسیر حوزه را از…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/681872" target="_blank">📅 09:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681871">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH37QUxeXoCk5V4iFGjiXkS9VnxeYgAjswyBpZYsQA4VB95APxQPPFYvkpUs0A5CWnRnb9K4Wxyv0HYak4r1m976bbkBT2s26tfAqC1TH_I_JvhesPgivMvEbstXnivRxFyfxmCx_jgBY3G2ijIK4Zg2sd3hPbnvVD3CzFAW8XgNwL9z-RO5roLlJ1XvNGeXSG1gvzeJ-b5SuWp0d-z13JM29o0633I1ioIs2j-tc-aPb7UY6acx1a8Bu28l4Cv-FDGEfL3DqJUzBC8T5cGl2oo0TsD6_gMG3pJLkixtNDDQgsJyGX7apPoXvYVpnCGNtgPSoIobnLLqmomZL7183g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی المپیاد جغرافیای ایران اول جهان شد
🔹
برای نخستین بار در رقابت‌های جهانی؛ تیم ملی المپیاد جغرافیای ایران در بخش Poster جایگاه اول را کسب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/681871" target="_blank">📅 09:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681870">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
دریافت سالانه ۱۱ هزار درخواست سقط جنین قانونی در کشور
مدیر کل امور معاینات بالینی پزشکی قانونی:
🔹
موارد مجاز: خطر برای سلامت مادر یا ناهنجاری جنین که موجب حرج غیرقابل تحمل برای مادر شود.
🔹
رضایت مادر شرط اصلی است؛ آگاهی پدر لازم است اما رضایت او شرط نیست.
🔹
سقط قانونی فقط تا قبل از ۴ ماهگی جنین امکانپذیر است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/681870" target="_blank">📅 09:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681869">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
شمارش معکوس برای پایان آتش‌بس ایران و آمریکا/ جنگ به «جنگ اقتصادی» تبدیل شد
نیویورک تایمز به نقل از منابع آگاه:
🔹
مهلت ۶۰ روزه توافق اسلام‌آباد بدون نتیجه پایان یافت و جنگ وارد مرحله فرسایشی اقتصادی شده است.
🔹
واشنگتن خواستار بازگشایی هرمز است و ایران آزادسازی دارایی‌هایش را شرط آن می‌داند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/681869" target="_blank">📅 08:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681868">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9a854ccb.mp4?token=Exf2etM0ZJnP9gZP-2Xq_1qVjy7CVcxS5VoE0KMdeJBmtIhLSuLaWhLlqG_2NwSIJ2BniKttrFaPX3n0kFe_rXNXv4MK38m_WBk4Yj1NHjcU02qdni3n6yV9yRNSgWiB7sOn67i4zM4P5GDuWKTjYPZbWvWilGq7QoTidTZAMLsJ9O2SXOtsd_xjy8RsTz0NXkSoFi-7u5PReWIWsJZmZjfEb9oip73689sncmgPgBpf2VyYoPmy6bMt9tFbnUFy_Jg8Go3GgJ_BFpJ9ZQnlj1GkLgdaBG_naQzW_cAtGBa242xQIcCEjoZ8fWyNhiHt2V_cNPcqF3fhMfCwJF2KNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9a854ccb.mp4?token=Exf2etM0ZJnP9gZP-2Xq_1qVjy7CVcxS5VoE0KMdeJBmtIhLSuLaWhLlqG_2NwSIJ2BniKttrFaPX3n0kFe_rXNXv4MK38m_WBk4Yj1NHjcU02qdni3n6yV9yRNSgWiB7sOn67i4zM4P5GDuWKTjYPZbWvWilGq7QoTidTZAMLsJ9O2SXOtsd_xjy8RsTz0NXkSoFi-7u5PReWIWsJZmZjfEb9oip73689sncmgPgBpf2VyYoPmy6bMt9tFbnUFy_Jg8Go3GgJ_BFpJ9ZQnlj1GkLgdaBG_naQzW_cAtGBa242xQIcCEjoZ8fWyNhiHt2V_cNPcqF3fhMfCwJF2KNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اردوغان، رئیس جمهور ترکیه: هرمز باید بدون عوارض و هزینه قابل تردد باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/681868" target="_blank">📅 08:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681867">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947f25d0e6.mp4?token=bQ4B5tdQQbri_AMPhv-YbAMdeBt-lwVR3yTH_bgi5Vdj-VnUncTtrgRzSrMnQqc3BhjoTdpntFeOT4rSMh8v0adx-X7l385n2xfpEmTSd6C0__yBJ6zB43Zlop2l_YpHm64ICfuSV71ptkCoGdNVFQ_LVB5o4u2BoR2lGF5I5Kej3NODaOrq2s8BNGpLLw6hP2kB2pewjqEsQ2CdLGr3jfpTdY2lF4e3hCUcENpUpfkPzD7xPqVUv_rdoSOCK7frdSnsUzI44XjRpk0GTGVN0V7mXiCQ0uPsihCj40NZZcSAtc6OFQgRmlmg0QabNX9hAYmQ6uRcdtR0OGsL1RHFZqxTe5V9PetpxqvZxw5v5j0VxjmrnYF7cn5lkgF47B1rp5ceknJ77yjyzFCrugoiLswUFPelwRSpyF0KfDOGGwVXzbk0ZUBsczfo0maH4o20QfUp08IMnsBTsSahYaLwSOGgSmF6XcrEa61APxaLPesD4WSlS5NdgFTSu1hXHJ4N11san_dXQcSoe2lwxwGvvRC175dmZXtXHbL7HjBEgtvmScUauEcnQQtBPUzOxA-BQx-iS_7Ej05MFtCIMvuwWL2wzuKZrcb2hdUUvzQ9ftz3WqZWNpuEfwwFUqFRIsMn787MyZ_WacKVzb-IjeQHIA4zNBQe6CsHPoTGygVdUgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947f25d0e6.mp4?token=bQ4B5tdQQbri_AMPhv-YbAMdeBt-lwVR3yTH_bgi5Vdj-VnUncTtrgRzSrMnQqc3BhjoTdpntFeOT4rSMh8v0adx-X7l385n2xfpEmTSd6C0__yBJ6zB43Zlop2l_YpHm64ICfuSV71ptkCoGdNVFQ_LVB5o4u2BoR2lGF5I5Kej3NODaOrq2s8BNGpLLw6hP2kB2pewjqEsQ2CdLGr3jfpTdY2lF4e3hCUcENpUpfkPzD7xPqVUv_rdoSOCK7frdSnsUzI44XjRpk0GTGVN0V7mXiCQ0uPsihCj40NZZcSAtc6OFQgRmlmg0QabNX9hAYmQ6uRcdtR0OGsL1RHFZqxTe5V9PetpxqvZxw5v5j0VxjmrnYF7cn5lkgF47B1rp5ceknJ77yjyzFCrugoiLswUFPelwRSpyF0KfDOGGwVXzbk0ZUBsczfo0maH4o20QfUp08IMnsBTsSahYaLwSOGgSmF6XcrEa61APxaLPesD4WSlS5NdgFTSu1hXHJ4N11san_dXQcSoe2lwxwGvvRC175dmZXtXHbL7HjBEgtvmScUauEcnQQtBPUzOxA-BQx-iS_7Ej05MFtCIMvuwWL2wzuKZrcb2hdUUvzQ9ftz3WqZWNpuEfwwFUqFRIsMn787MyZ_WacKVzb-IjeQHIA4zNBQe6CsHPoTGygVdUgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعمال قدرت ایران در بحرین!
کارشناسان آمریکایی:
🔹
حمله ایران به پایگاهی آمریکایی در بحرین به یکی از هاب‌های اصلی پشتیبانی و لجستیک ناو لینکلن آسیب زد و کار به جایی رسیده که برای مثال یک ملوان در پیامی به همسر خود گفته فشار شرایط دارد مرا از پا درمی‌آورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/681867" target="_blank">📅 08:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681866">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271fec4550.mp4?token=AOZSkrZOYO7zc1RVZG1JDKsTdH9Qnx9FoazjptRM5VljARY-Qd2dwasMqOpihQcX2xaR8QhztsXF1Y-wsiBXGvupsjvUTdFmKI5Dq_sR5peWDguWmkW2Vej4fmi6vQVKAJuRqoxDaaEWtygnQwgp7YSTR-ZAIHFWt85dq3OrQcbrdo_ruV0Hbo327Tmh_XpkQzKDIOKDqK4o1vRR2WcWw07iP8XKkKVCCxScMA1Dzg4Nj81LpSG_znwk7ZTFW37LHcBRMOizR750cvCn__oKt68MSJy6km1pUbLwiV_rEcChtg69bL17QQPV86RLOde3oeYOp5BHFWx61k8AyyHu8CSxvqMSQoMHdjmQkqfHznQzKdhKOPPDomlXHko0b5ObV1NGdLGBFGYo1HU31Cw0zmSVb51Z-FNGqr3vjInyA-fKmP_wjqxCv5D_11nVYuH1JMcINbk-yogg_x88McRN7xcguc1EYlF98XZyci4E9I-JHh5i0q69bFnoT1ld6XW3Wsrhy5PshuOZRiuUATH1Bq4IrNoXj-6ufe3O5o4w62AA5UBcEnMyi7wGudtSI0S_5Ixcv6y4aLHNIRhPKyqpIxxcw166mx0DTZr7ADyah6c3wANVaKZJNgflDkXSEqII0uNn1-01DsCWp0TXbXd0BaZLZOXsa5VmEVXTrvCabc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271fec4550.mp4?token=AOZSkrZOYO7zc1RVZG1JDKsTdH9Qnx9FoazjptRM5VljARY-Qd2dwasMqOpihQcX2xaR8QhztsXF1Y-wsiBXGvupsjvUTdFmKI5Dq_sR5peWDguWmkW2Vej4fmi6vQVKAJuRqoxDaaEWtygnQwgp7YSTR-ZAIHFWt85dq3OrQcbrdo_ruV0Hbo327Tmh_XpkQzKDIOKDqK4o1vRR2WcWw07iP8XKkKVCCxScMA1Dzg4Nj81LpSG_znwk7ZTFW37LHcBRMOizR750cvCn__oKt68MSJy6km1pUbLwiV_rEcChtg69bL17QQPV86RLOde3oeYOp5BHFWx61k8AyyHu8CSxvqMSQoMHdjmQkqfHznQzKdhKOPPDomlXHko0b5ObV1NGdLGBFGYo1HU31Cw0zmSVb51Z-FNGqr3vjInyA-fKmP_wjqxCv5D_11nVYuH1JMcINbk-yogg_x88McRN7xcguc1EYlF98XZyci4E9I-JHh5i0q69bFnoT1ld6XW3Wsrhy5PshuOZRiuUATH1Bq4IrNoXj-6ufe3O5o4w62AA5UBcEnMyi7wGudtSI0S_5Ixcv6y4aLHNIRhPKyqpIxxcw166mx0DTZr7ADyah6c3wANVaKZJNgflDkXSEqII0uNn1-01DsCWp0TXbXd0BaZLZOXsa5VmEVXTrvCabc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نقل قول دکتر لیلاز از شهید لاریجانی هم از جهت تشخیص و پیش‌بینی اوضاع هم تلاش نظام برای جلوگیری از جنگ بسیار حائز اهمیت است.
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/681866" target="_blank">📅 08:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681865">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScYmwk3_56i3MaGKJFZEoEReCDOhr5vWLsKzBoxvVfiJ6D0VI0ynKkjko_9AvLvnERQCma4ZI2Vu-x2PNE_jQm5D9KAwg5qBZCdJuL-feVPG0ZZag83cQT1jINh8ly-tGHTlV2rx72354WRPOrkxPpGKri-4cwZWh8pDGoSMbVUzmjGIQh411SYuJNagfmOoK3dX55OaDqQjfkusfoNXT0GNhLj-lO30MTOB-ZI0tqdBvYhPW0cMMvny1pgce2GBSV2i8zyHpx4oAafZSiJbkY7XOGF5WSxbTQmtefVqNIYIupo02EYjGoZEwd3hyge-8aClTSAFZVoWb_rZdXw7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دوگین، نظریه‌پرداز روس: ایران پرچم‌دار مبارزه با اسرائیل است؛ ظهور مهدی نزدیک است
🔹
الکساندر دوگین، نظریه‌پرداز روس، با تمجید از آنچه «وحدت و آمادگی ملت ایران برای فداکاری» خواند، از کشورهای اسلامیِ در تعامل با اسرائیل انتقاد کرد.
🔹
او همچنین با طرح ادعاهایی درباره «جهاد علیه دجال» و «پرچم سیاه خراسان»، از مسلمانان جهان خواست از ایران حمایت کنند و گفت:
«معتقد هستم ظهور مهدی نزدیک است.»
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/681865" target="_blank">📅 08:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681864">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b5d98ea0.mp4?token=RM4vpsW_4vi5bzFyVF5GdKjDhtWIcQza7vijfhA9l6n6onIejmiFmucCu2UL6qvOUVU-XC4UCO2qKty3fDn5-H_BalfapwQYRvOVed6rSLr0Ecq2jdNd3OEoUTxEQuITv-LIHgEk8vJnWUf1hHtsYcc-a8TSfpPz56X4if-nUexaaKg06jncam8rUruJsHzJ07oI0CHX2zNnrJA7yAlJxeCK-fCZt9xx2gxpu0tPppK07yUl7IaL2nEU5-GMyrH3XXWV1rDBv9g4qIPEERHw5l2MH4u3c-MD3dsNpvc3sA8oRk2UY0LBzaUrhDsY5CNX_EGjepLfvsBovxUl0fIdNXiYfPVMkR0hUTYPMgZ1K4DioHunTpboZyJVNnuTt07BkuuE2lxxeOpmAWdc6Ws4rsBHppywDb1I6ESNz1LhRug-SU2B3PTFHdISOaaAKKY603t-EwgFehW7xOSez0UxtwjJwAoll_Zx6lmX0OiJe1W6XU2R19kRyeQLeTdyyO6-k7Ezo_07GUEAzfkuD6WJXEhxRCLgEFFsYCVgEoZLvKaM_t9NdqrTdyoGJ3wWp3CpnALPQdSRcwXfeNEIopqjBcssqgrG7fH6lWveKZrh_urDURaK9LCSaCmcHa_eLFq9UhVHWJjvyu0GygTL_Dp7xHwwGgs6KvPojACkZtO2yNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b5d98ea0.mp4?token=RM4vpsW_4vi5bzFyVF5GdKjDhtWIcQza7vijfhA9l6n6onIejmiFmucCu2UL6qvOUVU-XC4UCO2qKty3fDn5-H_BalfapwQYRvOVed6rSLr0Ecq2jdNd3OEoUTxEQuITv-LIHgEk8vJnWUf1hHtsYcc-a8TSfpPz56X4if-nUexaaKg06jncam8rUruJsHzJ07oI0CHX2zNnrJA7yAlJxeCK-fCZt9xx2gxpu0tPppK07yUl7IaL2nEU5-GMyrH3XXWV1rDBv9g4qIPEERHw5l2MH4u3c-MD3dsNpvc3sA8oRk2UY0LBzaUrhDsY5CNX_EGjepLfvsBovxUl0fIdNXiYfPVMkR0hUTYPMgZ1K4DioHunTpboZyJVNnuTt07BkuuE2lxxeOpmAWdc6Ws4rsBHppywDb1I6ESNz1LhRug-SU2B3PTFHdISOaaAKKY603t-EwgFehW7xOSez0UxtwjJwAoll_Zx6lmX0OiJe1W6XU2R19kRyeQLeTdyyO6-k7Ezo_07GUEAzfkuD6WJXEhxRCLgEFFsYCVgEoZLvKaM_t9NdqrTdyoGJ3wWp3CpnALPQdSRcwXfeNEIopqjBcssqgrG7fH6lWveKZrh_urDURaK9LCSaCmcHa_eLFq9UhVHWJjvyu0GygTL_Dp7xHwwGgs6KvPojACkZtO2yNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک مهاجر از شوک‌های زندگی در اروپا؛ وقتی واقعیت با تصویر «بهشت غرب» فرق دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/681864" target="_blank">📅 08:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681863">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
کالابرگ مردادماه برای ۳ گروه حذف شد
🔹
از مردادماه زمان شارژ کالابرگ تغییر کرده؛ گروه اول پانزدهم، گروه دوم بیست‌وپنجم و گروه سوم پنجم ماه بعد می‌توانند از یارانه غیرنقدی استفاده کنند.
🔹
در نتیجه، سرپرستان خانواری با رقم پایانی کد ملی ۷، ۸ و ۹ کالابرگ مردادماه…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/681863" target="_blank">📅 08:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681862">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
آغاز دریافت کارت ورود به جلسه کنکور از امروز / چگونه کارت آزمون دریافت کنیم؟
🔹
توزیع کارت ورود به جلسه کنکور ۱۴۰۵ از امروز آغاز شده و تا چهارشنبه ۲۸ مرداد ادامه دارد.
🔹
داوطلبان باید مشخصات فردی و آدرس حوزه امتحانی را روی کارت بررسی کنند، مسیر حوزه را از روز قبل پیدا کرده و وسایل مجاز آزمون را آماده کنند تا از استرس و اتلاف وقت در روز کنکور جلوگیری شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/681862" target="_blank">📅 08:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681860">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ad9c2ab7.mp4?token=G8njM0GLLn1Qy8HxZIzDZLNQBxuZovdHyDFE5bVu8l4Na8HABub7mrF4HNYT6rswp0LdfmTdquxqAUbVhUGiSyCN18VwtNFCV4MKhd4yFqBlm6n9syWTK-0aXe1XIvzIr0833bly0HWSxx9IkX-BObFwb3KB3I7O2bs8Sjt9UdjU1cVpHKb6hgToF71etgNa7ZSLzIJLC7DwoysnmoOw_q0BbctC8_v1hlM2VwE4VHNQdafzoZJZ2FNv1OVSjCcf7iPXh5nKK985OEQ_lu_XCavor_IllliE4t_3nlNr5EGZ-_yjhX7ER-s5lXySriU6CQUJIuA0q5A3ke-ltj66KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ad9c2ab7.mp4?token=G8njM0GLLn1Qy8HxZIzDZLNQBxuZovdHyDFE5bVu8l4Na8HABub7mrF4HNYT6rswp0LdfmTdquxqAUbVhUGiSyCN18VwtNFCV4MKhd4yFqBlm6n9syWTK-0aXe1XIvzIr0833bly0HWSxx9IkX-BObFwb3KB3I7O2bs8Sjt9UdjU1cVpHKb6hgToF71etgNa7ZSLzIJLC7DwoysnmoOw_q0BbctC8_v1hlM2VwE4VHNQdafzoZJZ2FNv1OVSjCcf7iPXh5nKK985OEQ_lu_XCavor_IllliE4t_3nlNr5EGZ-_yjhX7ER-s5lXySriU6CQUJIuA0q5A3ke-ltj66KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌نوازی متفاوت مهراد هیدن با نوازنده آثار هانس زیمر
🔹
مهراد هیدن در حال نواختن یکی از قطعه‌های فیلم
Interstellar
در کنار راجر سیمور؛ نوازنده موسیقی‌های این فیلم که توسط هانس زیمر ساخته شده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/681860" target="_blank">📅 08:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681859">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bf7ebe59b.mp4?token=hFtndmPpC3EKSXRL_Ek6xuH6pJCx5PWt9Yv7ei5r_-nDneEUaEYBkqfs-l3E3wEbBZ-M4dpQc8BBrJ1OJJPtgEnyx2BPz-Ky-BCKpR57XpDPHa7lHqZqGGHUaUt41ICkSrN2rdtP6lQGcsWm455AUXnUz5h-V7vDSzYIPYBfDAiOKEiksGT2MbI9guIps9-XHRNwyWOjXNgOgzlb0ysfbuOB2zpUhVu2al2e4JkWOAdT2wyifWVgc2EayWarHtILV1M79RVjvRsHgPEiFknDL2BpEscGBsD-kLB89JLiAVOiq64TKi-fqsFflgnkXQitKMiVbzYxXfTbXzaxEPL1dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bf7ebe59b.mp4?token=hFtndmPpC3EKSXRL_Ek6xuH6pJCx5PWt9Yv7ei5r_-nDneEUaEYBkqfs-l3E3wEbBZ-M4dpQc8BBrJ1OJJPtgEnyx2BPz-Ky-BCKpR57XpDPHa7lHqZqGGHUaUt41ICkSrN2rdtP6lQGcsWm455AUXnUz5h-V7vDSzYIPYBfDAiOKEiksGT2MbI9guIps9-XHRNwyWOjXNgOgzlb0ysfbuOB2zpUhVu2al2e4JkWOAdT2wyifWVgc2EayWarHtILV1M79RVjvRsHgPEiFknDL2BpEscGBsD-kLB89JLiAVOiq64TKi-fqsFflgnkXQitKMiVbzYxXfTbXzaxEPL1dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر روز صبح چند دقیقه وقت بزارید این چندتا حرکت رو بزنید و معجزه‌شو ببینید
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/681859" target="_blank">📅 08:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681858">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQKrpZt8lArmKc45VjlBJ7dFSaT_qe35nwDg1MIAMmNavRwsFoVnP4uSV_WLwQNMYajFeqmquCoEJJput8bZcdE3lblDY8xn3oBUzYkROuD0dpQzAE123xnQZ1V0J3jZ-40MEmwjRx4PG0xwIknxbREyDLF1aLhSutGhnG44R7r7rO9Gis8rD6m1CYqW9sLL23I6JFIxQy1uXQF0iRqP9CCxEend1nDC7uhRE53rt0K6WqtB2wm-pRrTICVUt2CEbsZ3IlKgmO54xyXAsdg5CG5PVB-Wem1wUe2RxSKWXTdbS2KGnFGRf06LjfhdHrjrkboOeu5PhPXDMv-5PiqX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت کاربر امریکایی در واکنش به هلاکت رسیدن سربازان آمریکایی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/681858" target="_blank">📅 08:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681857">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omsSvL1EsqibtiHrEcThrKZO2dkTgC3kZe_0w103Ll3PyDbF4XwdhG625i7PxH5EHEySvTjTmlwgpGwaWCSTfsnV4_QmZyHBDrz9NWFgRZIG4idflNLvRILSvrrN-T8f-AZ4gTXFMx-MIwndC8ZPGve3Z_s-dRXUP1ir6U7bGfxGg_ESEiBB7AZryw5LRCBBsl81DvUoiJT6vO_j7exWLGQX4K4r0vCyTNGYZRFXc19WdSDk0AklYw_PX0FgRfLm_goWCqxIizmukjmj_mQZkN6KC0weUblAXGjLdkwzdfUiE-hNZ1u1WC5vwIiIqJpaJ8A2cRHDgVJK7mULycU3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با کنترل این ۳ عامل، مغزتان را سالم‌تر نگه دارید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/681857" target="_blank">📅 07:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681856">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
۹ نفر از عوامل اصلی شکنجه و قتل حمیدرضا رجب‌زاده دستگیر شدند
🔹
اموال دولتی و عمومی مسروقه در چهارمحال و بختیاری توسط سازمان اطلاعات سپاه کشف شد.
🔹
پیش فروش بلیت‌ قطارهای مسافری شهریور امروز آغاز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/681856" target="_blank">📅 07:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681855">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ایران، پایگاه‌های آمریکا را در خلیج فارس به لرزه انداخت
🔹
واشنگتن پست مدعی شد: عربستان سعودی، امارات، قطر، کویت و بحرین در حال بررسی امکان انتقال پایگاه‌های نظامی آمریکایی مستقر در خاک خود به دلیل تنش‌ها با ایران هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/681855" target="_blank">📅 07:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681854">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c9970f87.mp4?token=i6QqN_DW1SDCBMMj8ZHwyEtz3gH28VXIKxNhZQnDuZosflVS6qk7G6Oav4pjQmdpl_eA5-2w11E5waHIxxkst9W8be5FZ9ybOktF-Sgp-dsWHIUV9L6_TCcEdKcKRpyg_b9f1HCou14CEDUO_2V-guwGHawsZDkXxQemTPegM4WY4cpHoKK10_5ZKoWTMgJfoNu8uDifo1pR-n9DxWwP_CR_pDnGP_JXZ2FGK8fZ5e58DuVLfBcao5-f5KokHcjeSfaFlk-Gsf8oALR_ic9aEaIO9tZPF5MCEq_3wuQc6n5g01kJK2UIGCDVzv7EO2LrP5Ymr6PqWm1qXEI742V5wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c9970f87.mp4?token=i6QqN_DW1SDCBMMj8ZHwyEtz3gH28VXIKxNhZQnDuZosflVS6qk7G6Oav4pjQmdpl_eA5-2w11E5waHIxxkst9W8be5FZ9ybOktF-Sgp-dsWHIUV9L6_TCcEdKcKRpyg_b9f1HCou14CEDUO_2V-guwGHawsZDkXxQemTPegM4WY4cpHoKK10_5ZKoWTMgJfoNu8uDifo1pR-n9DxWwP_CR_pDnGP_JXZ2FGK8fZ5e58DuVLfBcao5-f5KokHcjeSfaFlk-Gsf8oALR_ic9aEaIO9tZPF5MCEq_3wuQc6n5g01kJK2UIGCDVzv7EO2LrP5Ymr6PqWm1qXEI742V5wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف فرماندهی شمالی ایالات متحده: ایالات متحده برای مقابله با حملات پهپادها در خاک آمریکا آماده نیست، ما حسگرها یا ابزارهای لازم برای مقابله با این مشکل را نداریم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/681854" target="_blank">📅 07:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681853">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
۱۲ میلیون جوان در سن ازدواج؛ ۱.۲ میلیون مجرد قطعی در کشور
🔹
مجردان قطعی؛ زنان بالای ۴۵ و مردان بالای ۵۰ سال
🔹
تجرد قطعی طی دو دهه حدود ۷ برابر شده، فاصله ازدواج تا تولد فرزند اول به میانگین ۴ سال رسیده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/681853" target="_blank">📅 07:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681852">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cf2931fe.mp4?token=uLMTgohR52D_YEg5CzmhyVehEyTp9yGz1PGYYK-7RQ2vguIly3Q9rIBYbZ4-MtJoATOQALD-sZI6PnaH1DGVFif-Id8yzXmgmlFEtsHAXP3dygDRxDGa-UpZ6P5bpN9sN6BKFXB45C4AdPlyG27A1Xu7R2CkDpXWGYxYGrkXmYI9d1QzCq26L9aQZcu06hrqZBGah2-8r7vuS9cbMljaISzLRWa_I-DkNaAknAFYWzn6Z1-6m7gZZ_WCxh3TG79q0V4NLVJkcd2fXCNxSDmF859soUh864AKc9CPjP4LdE0IWGOILFueKcnwjppZtF__KbkXJoX1084KJjRff0aEww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cf2931fe.mp4?token=uLMTgohR52D_YEg5CzmhyVehEyTp9yGz1PGYYK-7RQ2vguIly3Q9rIBYbZ4-MtJoATOQALD-sZI6PnaH1DGVFif-Id8yzXmgmlFEtsHAXP3dygDRxDGa-UpZ6P5bpN9sN6BKFXB45C4AdPlyG27A1Xu7R2CkDpXWGYxYGrkXmYI9d1QzCq26L9aQZcu06hrqZBGah2-8r7vuS9cbMljaISzLRWa_I-DkNaAknAFYWzn6Z1-6m7gZZ_WCxh3TG79q0V4NLVJkcd2fXCNxSDmF859soUh864AKc9CPjP4LdE0IWGOILFueKcnwjppZtF__KbkXJoX1084KJjRff0aEww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عواقب جنگ با ایران
🔹
ترامپ، سال ۲۰۲۴:
"قیمت بنزین به ۲ دلار و حتی شاید کمتر از آن باز می‌گردد."
🔹
ترامپ، سال ۲۰۲۶:
"قیمت بنزین روی ۴ دلار است. اشکالی ندارد. من هرگز عذرخواهی نخواهم کرد."
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/681852" target="_blank">📅 07:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681851">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kULte0CwWL_1yaxKiAGXkgyIYq48JQLglwhE7fm9ndsUVyYPnRruM7phB-TYFN4V4TpSRwuiWc486Mwk3mR6tTKO8CXGqZrtkFJBUZA_2W5L_njcO0-NL7Tt414olHTO5ccwgSz2F3SqyVTjYk0kutpjbsFlrXdrulFm0yF7dfij8Uywo2pWaE_GUMVzqD3mdJi-qciJ57b3sAN7uOizlWcssgg1igN5x380EuW0ueJroqz9nrgM0fXw18z6cKYacMuLAXvmBJCvYDHJgGYEX9ICFZjRMMt0V-HxEcU0-LD5DFpHWcj8aPc-6bAf7Qzaoq0IEqchsLNXNkRXlUSuZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون بین‌الملل وزارت خارجه: وزیر امنیت ملی رژیم صهیونیستی برای کشتار در غزه «سهمیۀ شبانه» تعیین کرده است؛ ۳۰ تا ۴۰ نفر
🔹
این جنایتکار صهیونیست هم‌زمان از اخراج فلسطینیان و شهرک‌سازی در سراسر غزه صحبت می‌کند.
🔹
این اعترافات باید برای روز حساب و محاکمۀ این جنایتکاران ثبت و حفظ شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/681851" target="_blank">📅 07:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681850">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1jbnmy4R0huHoM4akPrHnG6hcJhn2U6nf7hAdGzd7RScHjZsTdslPT_bUadH1h9K1sX3ulOWaYgJen1J3QS0wyymYH7J4HqC5SmlTp0v26OC2wjavEe2xbjxl8XZCJt9grpKU9t0yTjHOvGdLk2jmuQKmv-87WFk3DFTdbgUyD8WYYmLGgAE3OpnPDOKhTkK68tRVU1bCPKczQuFk9_787oK4O6H_EbVbPv2GkFOneVwsxavUcVVN3Iyz1r0zUN9o9dBF-0MnH3FA2M4uxfC6_P4Q1hYD3qvZ6Xz2zmZdT0_xMsKyitEv1t9bBkEysimjZ3ECoynUVji83HrTMBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۲۶ مرداد ماه
۴ ربیع‌الأول ‌‌۱۴۴۸
۱۷ آگوست ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/681850" target="_blank">📅 07:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681849">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taXJDbgsCzKZZBj_XcbH34yzo3MBTFzsQvVoQn0hNGLer4EyhS4lvzbx5VMNH0fuB66AWx1x1j2WMMevs4PZ-quvt6a5OE5YPgCAjXIKJJw9PVdOxTmnK7CcjtfWZH8DIvBgcH9XLd2bSAZP86xhervhBJ1eKGQIeRAc0h1cvfEHK8i8fYZe2hXQfXrn0chgVSU8LwjvtadYMkPinKEW_hBtioWFxAyu8rb-NcN1j2d-ZQOad4W81VcSrwQ_XVKbWNDXZsC4fFD_Q15gazqYFWBRJm_WM_Hu11u7wHQRcXkxUaDB69qQlz4e10huuCxNq1eYxQ7q9A1RYbokYrct5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
هر خانواده یک وام تا سقف ۵۰۰ میلیون
✅
بدون سود
✅
بدون ضامن
✅
بازپرداخت تا ۱۴ ماه
برای انجام ایمپلنت و سایر خدمات دندانپزشکی
برای دریافت اطلاعات بیشتر کلیک کنید
👇🏻
👇🏻
👇🏻
👇🏻
https://t.me/arameshdental
https://t.me/arameshdental</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/681849" target="_blank">📅 02:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681848">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار درباره ایران: اتفاقات خوبی خیلی زود رخ خواهد داد
🔹
دونالد ترامپ در خصوص ایران مدعی شد: اتفاقات خوبی خیلی زود رخ خواهد داد. در واقع، آنها همین حالا هم رخ داده‌اند، چون یک کاری هست که ما نمی‌توانیم اجازه دهیم انجام شود: ما نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/681848" target="_blank">📅 02:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
داماد ترامپ امروز با نتانیاهو دیدار می‌کند
🔹
ای بی سی نیوز به نقل از منابع اسرائیلی اعلام کرد که جرد کوشنر داماد دونالد ترامپ امروز دوشنبه با نتانیاهو نخست وزیر رژیم اسرائیل دیدار خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/681846" target="_blank">📅 01:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681845">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
کدام صنف‌ها بیشترین و کمترین مالیات را پرداخت کردند؟
🔹
با محاسبه سرانه مالیات، پزشکان متخصص همچنان در صدر پرداخت مالیات قرار دارند، در حالی که نانوایان کمترین مالیات را به ازای هر مؤدی پرداخت کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/681845" target="_blank">📅 01:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681843">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
تسنیم گزارش می‌دهد: تراستی‌ها؛ ابزار دور زدن تحریم یا گلوگاه جدید ارزی؟
🔹
واژه «تراستی» در سال‌های اخیر از یک اصطلاح تخصصی و کم‌استفاده، به یکی از واژه‌های پرکاربرد در ادبیات اقتصاد تحریم‌زده ایران تبدیل شده است؛ واژه‌ای که در ظاهر، از سازوکاری برای مدیریت دارایی و انجام مأموریت مشخص حکایت دارد، اما در عمل، در اقتصاد ایران به شبکه‌ای از واسطه‌های مالی و تجاری اطلاق می‌شود که مأموریت اصلی آنها فروش نفت، میعانات نفتی و فرآورده‌های پتروشیمی در شرایط انسداد کانال‌های رسمی بانکی بوده است.
🔹
شکاف در حکمرانی؛ اختیار در دست کیست؟
ریشه اصلی بحران تراستی‌ها را باید در دوگانگی میان مرجع صدور مجوز و مرجع پاسخگویی جست‌وجو کرد. در سال‌های گذشته، بخش‌هایی از فرآیند صدور مجوز یا واگذاری مأموریت‌ها در مسیرهایی انجام می‌شد که لزوماً با سازوکار سیاست‌گذاری ارزی بانک مرکزی هم‌راستا نبود، اما در زمان بروز مشکل، این بانک مرکزی بود که باید پاسخگوی آثار ارزی، نوسانات بازار و کمبود منابع می‌بود.
🔹
راهکار چیست؟ برای اصلاح این وضعیت، نخست باید اختیار و مسئولیت در یک نقطه متمرکز شود؛ یعنی بانک مرکزی تنها مرجع سیاست‌گذاری، صدور مجوز و نظارت بر این‌گونه سازوکارها باشد تا امکان پاس‌کاری مسئولیت از بین برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/681843" target="_blank">📅 01:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681840">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c501c9e4.mp4?token=vpJWFTekccdnp3eDzZb61EvGOlqLaRokVnXXzghmTlbh-HUGkEgCnNApO0e0KIJd9KLc9m9h1FYeFJoZF6zDe4prbFZrUfGwNbxHWkHA3b8ou-KNTDRohYpQ9yh1mr9IUl1b4buUWBjhSfZj-I1dbTpmHqoWdiLpke86dyOPZAXi3bcUxDWwv2JCtjp2zU4pU4yDRbN8wQL6l3qBUAQGVxY8N4vtBFOkbgnFgM9FfVslUizHN8BlbqPgQpH2juHPKjHoxsuyHVeKhL4y7EzXYGfgnxEdrTcYUZL0KB3s_sllvddXSLf_J5sEW0qQL3igb_iuw5MRS8gvUnwIiQbdFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c501c9e4.mp4?token=vpJWFTekccdnp3eDzZb61EvGOlqLaRokVnXXzghmTlbh-HUGkEgCnNApO0e0KIJd9KLc9m9h1FYeFJoZF6zDe4prbFZrUfGwNbxHWkHA3b8ou-KNTDRohYpQ9yh1mr9IUl1b4buUWBjhSfZj-I1dbTpmHqoWdiLpke86dyOPZAXi3bcUxDWwv2JCtjp2zU4pU4yDRbN8wQL6l3qBUAQGVxY8N4vtBFOkbgnFgM9FfVslUizHN8BlbqPgQpH2juHPKjHoxsuyHVeKhL4y7EzXYGfgnxEdrTcYUZL0KB3s_sllvddXSLf_J5sEW0qQL3igb_iuw5MRS8gvUnwIiQbdFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری شگفت انگیز از تصویرسازی ابرها در آسمان نیوجرسی
🔹
ساکنان ایالت نیوجرسی آمریکا، تصاویری از این پدیده عجیب را منتشر کردند که ممکن است نشانه‌ای از بادهای شدید، باران شدید و رعد و برق باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/681840" target="_blank">📅 01:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک‌سوم مبتلایان به آنفلوانزا زیر ۱۵ سال سن دارند
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
بر اساس نظام دیده‌بانی عفونت‌های تنفسی مرکز مدیریت بیماری‌های واگیر، ۴.۴ درصد مراجعان سرپایی و ۵.۷ درصد مراجعان بستری، دارای علائم عفونت‌های تنفسی بوده‌اند.
🔹
تست آنفلوانزا در ۰.۷ درصد و تست کووید-۱۹ در ۲.۹ درصد افراد دارای علائم تنفسی مثبت بوده است اما هر دو بیماری در سطح پایینی قرار دارند.
🔹
۸۰ درصد آنفلوانزاهای در گردش از نوع B هستند و نزدیک به ۳۴ درصد مبتلایان زیر ۱۵ سال سن دارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/681839" target="_blank">📅 01:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11395e9490.mp4?token=dN7qRlxQGTot_on_Ef_HFFEcdnzaIGHyqOZr2H-e-jXMgGtgz-XvJ5_oHtqeZeWuiUDzH4plERYbv6QHo0a9EnmwE5VzVAnjWz_E7-88SdPvfNKNL4MDgSydU8x1UPT4v2aKPLJHM_-FqtcqLERiefhHvGQ-WsH-rg4KQwqFcBEHoiYX9mRKtN4MiZgFGgUVoCN8sm4vEUX-G7B-izt12AsQbahfxkaiK47IPLrk28R94FKGjFdXwD_Z_qEBuwETb-ckhXPvpuffClHT1mnAbZgfZcZK8aE8bgUAqV9enydvcV8Dzd1CkapMfvNzW8-i01a__eOG0CF_PdYFm65AZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11395e9490.mp4?token=dN7qRlxQGTot_on_Ef_HFFEcdnzaIGHyqOZr2H-e-jXMgGtgz-XvJ5_oHtqeZeWuiUDzH4plERYbv6QHo0a9EnmwE5VzVAnjWz_E7-88SdPvfNKNL4MDgSydU8x1UPT4v2aKPLJHM_-FqtcqLERiefhHvGQ-WsH-rg4KQwqFcBEHoiYX9mRKtN4MiZgFGgUVoCN8sm4vEUX-G7B-izt12AsQbahfxkaiK47IPLrk28R94FKGjFdXwD_Z_qEBuwETb-ckhXPvpuffClHT1mnAbZgfZcZK8aE8bgUAqV9enydvcV8Dzd1CkapMfvNzW8-i01a__eOG0CF_PdYFm65AZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: هنوز نمی‌دانیم چرا با ایران وارد جنگ شدیم
روبن گالگو، سناتور آمریکایی:
🔹
ما از سربازان آمریکایی حمایت می‌کنیم که تلاش دارند ما را از این جنگ بیرون بکشند. اما رئیس‌جمهور هیچ طرح و برنامه‌ای نداشته و معلوم نکرده این جنگ چقدر گسترده است، چطور پیش می‌رود و چطور قرار است تمام شود. مأموریت ما دقیقاً چیست؟ ما هنوز نمی‌دانیم اصلاً چرا با ایران وارد جنگ شدیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/681838" target="_blank">📅 00:58 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681837">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hv2HkcIlK8S7TMtzOLCmoSOaWiD6KWrOegwC0a64yxQs_UNhT3QvTrEir2612bNPjgwuGYo-Oz6n2uNNj0PUHdTnPx2PAIBER3SGDtXEiPcAGf5A3NGGcXZ2wQWY8-lFAfg9I-BFKq2Xg8xkezmA3234sOKS6dXWDElURddtOX-pmaVA05JOt6muAE5KWFCYo_op5SC3omRlGYH9Ls0M82rCTNN6dJzWC9D8Yd5DQIa0oB1wcFF95RkXLXMT1736BgoHGKQJ0z_uSWO-2O-p3mSOdLrCkvKG091PaE1ukcHDLNd6BH6mpvp5lX-0yim3fdHfnza4J8l2XKHCSO6X_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: از رئیس‌جمهور کره جنوبی درباره تمایلس برای پیوستن به تلاش‌های ما برای خلع سلاح هسته‌ای ایران سوال کردم، اما پاسخ او به این درخواست منفی بود #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/681837" target="_blank">📅 00:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681836">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ترامپ: از رئیس‌جمهور کره جنوبی درباره تمایلس برای پیوستن به تلاش‌های ما برای خلع سلاح هسته‌ای ایران سوال کردم، اما پاسخ او به این درخواست منفی بود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/681836" target="_blank">📅 00:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681835">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b38253a8.mp4?token=UwXdD0VtsgUE9q7Qet5UuQS2m_U_5qXMuvIhry565P7L9oxBXyZ1tpMZ3oaq0X5eLoYzGXyN5xe0-RPzpH2jpAcRAZ0bMvzHXsq8n-AZtsgoU039OJwFI61qcs98eLoPy2YonwJ0fh63mCdKku_HAP_rs3al6FPZOGWnJDW-wc4W3wiOXeoXWou4WQEO1RGivV6IqskWV-zTE3fQq7PcoNwKBedhjQvd7UZ_5BnUwwErRMqMCefDVrRCL-fyRe4_v89P4ZwZLOZsg4zq0cV032XoZ79mrgY7UqLvnPFdv-nlJlYCCmtX50BP-oDFMtbv3fFY1YnYsl3XYwkhEGVxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b38253a8.mp4?token=UwXdD0VtsgUE9q7Qet5UuQS2m_U_5qXMuvIhry565P7L9oxBXyZ1tpMZ3oaq0X5eLoYzGXyN5xe0-RPzpH2jpAcRAZ0bMvzHXsq8n-AZtsgoU039OJwFI61qcs98eLoPy2YonwJ0fh63mCdKku_HAP_rs3al6FPZOGWnJDW-wc4W3wiOXeoXWou4WQEO1RGivV6IqskWV-zTE3fQq7PcoNwKBedhjQvd7UZ_5BnUwwErRMqMCefDVrRCL-fyRe4_v89P4ZwZLOZsg4zq0cV032XoZ79mrgY7UqLvnPFdv-nlJlYCCmtX50BP-oDFMtbv3fFY1YnYsl3XYwkhEGVxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند قلم ساده دستگاهی برای سوخته کاری بر روی چوب بساز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681835" target="_blank">📅 00:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681834">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBOMNB5TBg2WXw7nuqGiUW3YuDu11lGCuUlpN8NzsyB-woWDmeSrT1VmvfL-BJ1up570V2w0ctNU4AhmVBx7Ku-ADWfDkK3Apsa1n38-yUGuN55wL-qMeRPjhfxq_u6N8H8-xOQ2HGP2oXkXh-5BDFfg3RASNW3F3zBY6F9rlG-wgZJic_CPq2JNwdSZlNKbE24dhWmjGL41BKNlkgzIpEN3XzaptXWzvZecUB_COxHC18xPJoHSVrufigR-cKXwZUlyZERxgFhnGfYlADSyxmxDPQ4XyChn6VZybkMhUgLmiisAw7JLbg8grsjjHOkrwiO_VQIdzhjinSxlpTW51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمایت ترامپ از توافق مکه
ترامپ:
🔹
بسیار خوشحالم که می‌بینم عربستان سعودی، ترکیه و پاکستان اخیرا و سرانجام توافق‌نامه دفاع مشترک مکه را امضا کرده‌اند. این نشان می‌دهد که چگونه خاورمیانه در حال اتحاد است و چگونه کشورها سرانجام قادر خواهند بود از خود به شیوه‌ای معنادارتر دفاع کنند. تبریک به رهبری بزرگ سه کشور ذکر شده. این یک گام بزرگ، جسورانه و مهم است.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/681834" target="_blank">📅 00:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681832">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر خوب؛ ۸۰ درصد سطح دریاچه ارومیه آب دارد
محمد کوهانی، دبیر ملی شبکه های محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
سال گذشته در تصاویر ماهواره‌ای صرفا یک لکه آبی از دریاچه ارومیه دیده می‌شد، اما امسال بیش از ۸۰ درصد سطح دریاچه آب دارد و حجم آب آن به ۲.۵ تا ۳ میلیارد مترمکعب می‌رسد.
🔹
در سال ۹۸ حجم آب دریاچه ارومیه به حدود ۵ الی ۶ میلیارد مترمکعب می‌رسید. تجربه این سال نشان داد حتی اگر سال پرآبی داشته باشیم، بدون وجود برنامه انسان‌محور در سال‌های آتی مجددا دریاچه را از دست خواهیم داد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/681832" target="_blank">📅 00:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681831">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سناتور آمریکایی: ناو آبراهام لینکلن مشکلات عمیقی دارد
سناتور دموکرات آمریکایی:
🔹
واقعاً مشکلات عمیقی درباره وضعیت ناو آبراهام لینکلن وجود دارد.
🔹
ترامپ مشکلات را در رابطه با جنگ علیه ایران برنامه‌ریزی نکرده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/681831" target="_blank">📅 00:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681830">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
۶ دانشگاه ایرانی در جمع ۱۰۰۰ دانشگاه برتر جهان
🔹
تازه‌ترین رتبه‌بندی شانگهای ۲۰۲۶ منتشر شد و ۶ دانشگاه ایرانی در جمع ۱۰۰۰ دانشگاه برتر جهان قرار گرفتند.
🔹
دانشگاه تهران و دانشگاه علوم پزشکی تهران مشترکاً در بازه ۵۰۱ تا ۶۰۰، صدرنشین دانشگاه‌های ایران شدند.
🔹
دانشگاه صنعتی امیرکبیر نیز در بازه ۸۰۱ تا ۹۰۰ جای گرفت. همچنین دانشگاه علوم پزشکی شهید بهشتی، دانشگاه صنعتی شریف و دانشگاه تربیت مدرس در بازه ۹۰۱ تا ۱۰۰۰ قرار گرفتند. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/681830" target="_blank">📅 00:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681829">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573c891f09.mp4?token=k4p9qQruifrbVpi_dr5DhzOZhUnUngugiNa9Gil7R7lpYHgW3gd9qVeQNs2_zVbZPdlRGXdzmxVGANxUWZMdqQEzGpsov8go3YiVcoYk5ZvZ8JuKVUMQ2-1q5ZUvfyIMksrNRhwdSnFVS5kRJTVL0vh6uwo8_l_pDwTavFyBWZg-x0iIIyMsjT5l9M_IjrV1Z1DIE2HlQ-Mbud9E3aHsZg_zMK8OUA_b8o8V9SuXbWcduSbUwk_jJVaxV9jK5iMydL7UtkIHEAEmgonAfvp1B4lHkKmHj7GL1qLZ0ys_WMMaUMNslpnUiJMJa5EkfLozgAhh_os9qzoxIbklDnqv3iyRmR_yOZYqmcpBoCeaRuE6R5E2ozRF3AHrKnmmJeuyQBCT1n5b_Y6k7G1J2xz8HfeTb7HmTIJGZUuxwlKH6abYPclgfktoUoJBqBnHtqLWTZrquaG81nx8RzXZgguVizy2Y3YR_9y6Rys8cpZx2uSRczCOMG1rWjpNJaCAwvOxw4V7TCbo7C21ZB-rCazqVFsNZteQuM504pFmkEikpZdx6uHkCdvzsATuLK0u7Z0_K6Lla_WHQ5G_nkPzP_UnNvzMaDpWxPKU_rLL1itfOt__f9fk5t9JZgYVCwsTxjsc5QIV3NfQ6vqcAtE3JYOyMw49l07PmERh22h3sfDva2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573c891f09.mp4?token=k4p9qQruifrbVpi_dr5DhzOZhUnUngugiNa9Gil7R7lpYHgW3gd9qVeQNs2_zVbZPdlRGXdzmxVGANxUWZMdqQEzGpsov8go3YiVcoYk5ZvZ8JuKVUMQ2-1q5ZUvfyIMksrNRhwdSnFVS5kRJTVL0vh6uwo8_l_pDwTavFyBWZg-x0iIIyMsjT5l9M_IjrV1Z1DIE2HlQ-Mbud9E3aHsZg_zMK8OUA_b8o8V9SuXbWcduSbUwk_jJVaxV9jK5iMydL7UtkIHEAEmgonAfvp1B4lHkKmHj7GL1qLZ0ys_WMMaUMNslpnUiJMJa5EkfLozgAhh_os9qzoxIbklDnqv3iyRmR_yOZYqmcpBoCeaRuE6R5E2ozRF3AHrKnmmJeuyQBCT1n5b_Y6k7G1J2xz8HfeTb7HmTIJGZUuxwlKH6abYPclgfktoUoJBqBnHtqLWTZrquaG81nx8RzXZgguVizy2Y3YR_9y6Rys8cpZx2uSRczCOMG1rWjpNJaCAwvOxw4V7TCbo7C21ZB-rCazqVFsNZteQuM504pFmkEikpZdx6uHkCdvzsATuLK0u7Z0_K6Lla_WHQ5G_nkPzP_UnNvzMaDpWxPKU_rLL1itfOt__f9fk5t9JZgYVCwsTxjsc5QIV3NfQ6vqcAtE3JYOyMw49l07PmERh22h3sfDva2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
پست اینستاگرام نوید محمدزاده با لباسی با طرح پرچم فلسطین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/681829" target="_blank">📅 00:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681828">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادارات مهران و دهلران دوشنبه تعطیل شدند
🔹
با توجه به تداوم موج گرما و افزایش دمای هوا، فعالیت ادارات و دستگاه‌های اجرایی، بانک‌ها به‌جز شعب کشیک و شرکت‌های بیمه در شهرستان‌های مهران و دهلران روز دوشنبه ۲۶ مردادماه تعطیل اعلام شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/681828" target="_blank">📅 00:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681827">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89ae3291b3.mp4?token=AA5nppeA3WFQAaX_q6A3KlxJ6bOASbjJI0n9mrzjkohlmmoWClpSzVTI07xMZABsSkZr94RRwhwLvDaewI5ndA-l4WQBUoHdYD0zwEjMZkJePlT8ou3hejEFCVi2JvFz2MuL6ldIPzTe66VNXWzeU3wTYXHFxeGKeQr01bZWlRbApqQnwfHxrl0OIDuktoltQg-f6V5q2u-7U7cherb40X4UYGNTYfGj9l0CnbdNkitida1xx7JSPl9N1QGrQEYpKF-eMndrmttQDfRi0QEWQcZfEl20Yjrx4lixWsCX1VMRDySQSSze7ZDWl-bOXFA12oMcPTjrYpSZw7SIykp3Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89ae3291b3.mp4?token=AA5nppeA3WFQAaX_q6A3KlxJ6bOASbjJI0n9mrzjkohlmmoWClpSzVTI07xMZABsSkZr94RRwhwLvDaewI5ndA-l4WQBUoHdYD0zwEjMZkJePlT8ou3hejEFCVi2JvFz2MuL6ldIPzTe66VNXWzeU3wTYXHFxeGKeQr01bZWlRbApqQnwfHxrl0OIDuktoltQg-f6V5q2u-7U7cherb40X4UYGNTYfGj9l0CnbdNkitida1xx7JSPl9N1QGrQEYpKF-eMndrmttQDfRi0QEWQcZfEl20Yjrx4lixWsCX1VMRDySQSSze7ZDWl-bOXFA12oMcPTjrYpSZw7SIykp3Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش اردوغان به جنگ احتمالی ترکیه با اسرائیل
رئیس جمهور ترکیه:
🔹
ما در مورد جنگ صحبت نمی‌کنیم، ما در مورد صلح صحبت می‌کنیم.
🔹
اما اگر کسی قصد حمله به ترکیه را داشته باشد، ترکیه در آن جنگ تردید نخواهد کرد و از آن فرار نخواهد کرد.
🔹
من این را با وضوح و صراحت کامل می‌گویم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/681827" target="_blank">📅 00:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681826">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زندگی بدون سقف/ روایتی از زنان بی‌خانمان
🔹
زیرپوست شهر  زنانی زندگی می کنند که تنها سقفشان، آسمانِ شب است. این مستند، روایتی بی پرده از زنانی است که نه از روی انتخاب بلکه از جبرِ حوادث، خانه و امنیت خود را از دست داده‌اند و حالا در حاشیه  شهر، در نبرد با سرما و گرما و تنهایی به سر می‌برند. شاید تماشای این ویدیو، پنجره‌ای باشد به دنیایی که این روزها کمتر دیده می‌شود./ خبرفوری
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/681826" target="_blank">📅 00:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681825">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a31969da.mp4?token=E0aPyRbqrhb4-_bTg1e_6F-Cg0cLJsGQo6hcsXP0XWZn5oP7pxbd1ajAKk73z13PhhW1WSTy27rGggHRx7tamWXD0vL8PjH13wFSS0ViNmHXaCQcY7unQWss4P9yp8tff9Ptfj9E_Fx22SBz3K_VIsNhUfqXELcAKZn_j8jnNq2WU9W_hhsTKNa_00lYzGXaUP3RCLS-BO6MI_UbQljCuRHMV9yMvFwoPge3tyLuEHstYetrsdk2Kqnwe2A3QLRzVyvg20GaXvT2-7yX-D9FxDcr5xGvOaf7F4l7iaaf-8wG4mU7yqsLayqshhkIwDmuZ1K-9dpEcbxpAE1ogp_hqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a31969da.mp4?token=E0aPyRbqrhb4-_bTg1e_6F-Cg0cLJsGQo6hcsXP0XWZn5oP7pxbd1ajAKk73z13PhhW1WSTy27rGggHRx7tamWXD0vL8PjH13wFSS0ViNmHXaCQcY7unQWss4P9yp8tff9Ptfj9E_Fx22SBz3K_VIsNhUfqXELcAKZn_j8jnNq2WU9W_hhsTKNa_00lYzGXaUP3RCLS-BO6MI_UbQljCuRHMV9yMvFwoPge3tyLuEHstYetrsdk2Kqnwe2A3QLRzVyvg20GaXvT2-7yX-D9FxDcr5xGvOaf7F4l7iaaf-8wG4mU7yqsLayqshhkIwDmuZ1K-9dpEcbxpAE1ogp_hqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راحت ترین و سریع ترین راه برای درست کردن دسر با قهوه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/681825" target="_blank">📅 00:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681824">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای هیل: گزینه دیگر تسلیحات هسته‌ای ایران بمب‌های پلوتونیومی است
پایگاه خبری هیل مدعی شد:
🔹
ایران بیش از ۱۵ سال است که رآکتور بوشهر را اداره می‌کند. مانند همه رآکتورها، پلوتونیوم به عنوان محصول جانبی عملیات عادی، درون سوخت مصرف‌شده رآکتور به دام افتاده و انباشته شده است.
🔹
این پلوتونیوم هرگز قرار نبود در ایران باشد.  بیش از ۲۰ سال پیش، روس‌ها که رآکتور بوشهر را ساختند و سوخت آن را تأمین کردند قول دادند که سوخت مصرف‌شده را پس از خنک‌شدن و ایمن‌شدن برای حمل‌ونقل، خارج کنند. اما ایرانی‌ها این پیشنهاد را رد کردند.
🔹
اکنون، حدود ۲۱۰ تن سوخت مصرف‌شده حاوی بیش از ۲ تن پلوتونیوم در یک استخر نگهداری می‌شود. این مقدار برای ساخت بیش از ۲۰۰ سلاح نسل اول کافی است.
🔹
این پلوتونیوم یک مشکل بسیار پیچیده ایجاد می‌کند. نمی‌توان آن را بمباران کرد، زیرا این کار می‌تواند باران رادیواکتیوی با عواقبی در مقیاس قاره‌ای ایجاد کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/681824" target="_blank">📅 00:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681823">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5DfIkl2wVTB0qyHNK5nK9r9F-Y9pcgQb5Kom5LYjAABCrQGJC_aFp0souN0EVlgzh3VwfHRdBj68mGjh7-c4viDU8A3C_jPWpeBVNVwo6gfp6aDrzFfV76qar9VDhZO3UNpaa1V6p3qjgVUglZ5KsmxeR5xgvQYdfh3ipVeZN3l_FwAy-5h-ypGXhZD3gdB3boPvNDA6vxtdTipohNguiXaFADsZh_yUZRY97rjlhv4gyicGSCqoStQyd6SYUcta6tAoyNJJTLiHe0sCEZI1TYR-heyxLJ4d5_G6iAy31XaBDPSc2K5b5oXLKI35BmnQp5ttLQm3DYxMXJVZNfbNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسکات بسنت وزیر خزانه داری آمریکا از تحریم های آتی علیه ایران با هدف افزایش انزوای اقتصادی خبر داد
🔹
این اقدامات در کنار ادامه محاصره دریایی ایالات متحده در تنگه هرمز عمل خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/681823" target="_blank">📅 00:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681820">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q07vmieI57J91-4xDGASCElFQQ-5cR-KWdtxFr_BFmE1KkKED5-qjaL6i3blP_MgKLB87QE3or6Oex-BT49DAg9TyqL2Pw9yge-jOiN7Dsf2aPdJeaEfIls3qBseR1kRYpZZgUQ45yg2wGaSEOFC6_LnEr7NUWk-Vrt_aZY-gxAYQe-XFcThh2sf1VhLocOG1jEy4wrwbvdsZuJyX8Q79ai-ECvmYnHbKlZHmIW33VoEE9x4b3Vxjm5sTvKSoPiQ_gaSDeYEGZuzu4exeTrsyouFcU8raHP8VEWHjKyRfGV_4CuXm6jAy7G1LTJV4VyM81UD_uJ_PQUOvlRm1whnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/681820" target="_blank">📅 00:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681819">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
قالیباف: باید به نقطه‌ای برسیم که از چرخۀ تکرار جنگ و صلح خارج شویم
🔹
باید مراقب باشیم دستگاه محاسباتی ما مسئولین به خطا نرود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/681819" target="_blank">📅 23:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681818">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
پیام صریح به بازار پول؛ خبری از تزریق نقدینگی نیست
🔹
عملیات بازار باز هفته گذشته نشان داد بانک مرکزی همچنان کمتر از ۲۰ درصد تقاضای نقدینگی بانک‌ها را پوشش می‌دهد.
🔹
با وجود ثبت سفارش‌هایی در محدوده ۳۵۰ همت، میزان پاسخگویی بانک مرکزی از ۷۰ به ۶۰ همت کاهش یافت.
🔹
با احتساب اوراق سررسید شده، بانک مرکزی در مجموع نه‌تنها پول جدیدی به اقتصاد تزریق نکرد، بلکه حدود ۱۰ هزار میلیارد تومان منابع بانک‌ها را به‌ صورت خالص جذب کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/681818" target="_blank">📅 23:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681817">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2201eaa6.mp4?token=uqMLO9wgWtymsDLz-1zBL5huzNdrlFYpBc-jC91q2xBfLXwArUw4O7SXt5LyhblTTeIz8ORahX1YwxzziVLnRkkj4JrQqoAJT5o-ls1QDaW4O8z0ZIJU7FyuMIrR_oP_t8TQ-IcpRxlzh0ZiQ4-c2CsCzFsHw2NM3Sn2HLVRI5BotU93UvnnmGDHvfaGqCC0x1iPOYqoFfb2qCT7kz3Zhe99-4tEcL7_JBbuo_4DVlhR3mHvc4O4RaCBKw3x3AOdWVPqCqW7AF0Dw7j0QOvNtGJaoFBbI5bsCUf_eYVgK7XhA98tjOIa22eFRYnMIO5QyOvEHQqlvkEg_LX9RjC5LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2201eaa6.mp4?token=uqMLO9wgWtymsDLz-1zBL5huzNdrlFYpBc-jC91q2xBfLXwArUw4O7SXt5LyhblTTeIz8ORahX1YwxzziVLnRkkj4JrQqoAJT5o-ls1QDaW4O8z0ZIJU7FyuMIrR_oP_t8TQ-IcpRxlzh0ZiQ4-c2CsCzFsHw2NM3Sn2HLVRI5BotU93UvnnmGDHvfaGqCC0x1iPOYqoFfb2qCT7kz3Zhe99-4tEcL7_JBbuo_4DVlhR3mHvc4O4RaCBKw3x3AOdWVPqCqW7AF0Dw7j0QOvNtGJaoFBbI5bsCUf_eYVgK7XhA98tjOIa22eFRYnMIO5QyOvEHQqlvkEg_LX9RjC5LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک روش کاربردی برای تمیز نگه داشتن لوله‌ سینک ظرفشویی، که با استفاده از یک بطری پلاستیکی انجام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/681817" target="_blank">📅 23:51 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681816">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fba1d673c.mp4?token=fTQ4utrf3JK_QR0rIGIPkn757oW7Dr_V5CtbabNz8ifuHUPdvNl1vkIBs9L5w7N3hk8A0500f33QpYHdEHNpMYSoLHCOUExlyMB49tZt7eKhqFhoTZC_oTOC2moWvIRdwQoQAMHJAe5V8uLo-a-fUCPt_pSbQICVrxbmD54QbtnveWQFR4PUGEgJuSGie-I63HGsjt9-WclcPjywzxNVWScFy5-4RitxFCfgcQvkO4jdaxlLa11LJsktihgTWa66Tv71u2NSKrY4G0XKEoYo7DF5RyraSR48rywyY3xYk38ParA0DVNI3uweYVcRORmmgFzvjkd7SYjCAsC9rZq4iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fba1d673c.mp4?token=fTQ4utrf3JK_QR0rIGIPkn757oW7Dr_V5CtbabNz8ifuHUPdvNl1vkIBs9L5w7N3hk8A0500f33QpYHdEHNpMYSoLHCOUExlyMB49tZt7eKhqFhoTZC_oTOC2moWvIRdwQoQAMHJAe5V8uLo-a-fUCPt_pSbQICVrxbmD54QbtnveWQFR4PUGEgJuSGie-I63HGsjt9-WclcPjywzxNVWScFy5-4RitxFCfgcQvkO4jdaxlLa11LJsktihgTWa66Tv71u2NSKrY4G0XKEoYo7DF5RyraSR48rywyY3xYk38ParA0DVNI3uweYVcRORmmgFzvjkd7SYjCAsC9rZq4iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین هواپیمای برقی جهان برای اولین بار به پرواز درآمد
🔹
شرکت سوئدی-آمریکایی Heart Aerospace با موفقیت هواپیمای نمایشی X۱، یک هواپیمای تمام برقی با طول بال ۳۲ متر و وزن برخاست بیش از ۱۱ تن را آزمایش کرد.
🔹
این پرواز در شهر نیویورک انجام شد، ۲۷ دقیقه طول کشید و به ارتفاع تقریبی ۳۳۵ متر رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/681816" target="_blank">📅 23:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681815">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
معاون سیاسی سپاه: راهی که ترامپ می‌خواهد را خدا برا او بسته است
🔹
وقتی ملت ایران حق جهاد در راه خدا را ادا کرده، خدا هم راه سلطۀ کفار بر ملت ایران را می‌بندد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/681815" target="_blank">📅 23:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681814">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
ثانیه‌شمار کانال ۱۴ اسرائیل برای لغو تفاهم‌نامه تهران و واشنگتن
👇
khabarfoori.com/fa/tiny/news-3238221
🔹
تصاویر خلبانان ایرانی که در اسارت قطر هستند
👇
khabarfoori.com/fa/tiny/news-3238159
🔹
ترامپ دلیل کناره‌گیری سخنگوی کاخ‌سفید را اعلام کرد
👇
khabarfoori.com/fa/tiny/news-3238218
🔹
ماجرای خیانت همسر مهستی به او/ دوست صمیمی اش زندگی او را نابود کرد
👇
khabarfoori.com/fa/tiny/news-3238192
🔹
خواننده زن ایرانی در ۷۶ سالگی درگذشت
👇
khabarfoori.com/fa/tiny/news-3238031
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/681814" target="_blank">📅 23:42 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681813">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhQiwfVUbujw5gEtzY5SmxnAbzC9skJFvK_mWAjdkhUsQ6vc_ctVS0p3VZDL4Ffwu2bUwzogt2ZnYiRYQyyxL8vmuszQLRr_3JcufI3tnRbAnz_PWcbzU_4sHCjs43Dj1naE-k_nvxc3TIbIun9EXy6mFRI3nfAO5vGSF8wWhwfhUTr3NlMCJ1fZmP2wNRN-DfrCbHUU7nHJDB9Dfc5ic-3DBI0usBTumX_YVv19G5lGdzky9_DMFunub_pxu-0uyr_tKT8ODEZ6gh-37Jujet46Rqdks8Zy575cYTjvRUfUrQuR87ZAt9awX_EOpUY5r-pToTWO0D6ariwdFMvI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست: متحدان عرب در جنگ ایران از آمریکا ناامید شدند
واشنگتن‌پست:
🔹
متحدان آمریکا به‌ شدت نگرانند که ترامپ نتواند دیپلماسی مورد نیاز برای تأمین صلح با ایران را مدیریت کند.
🔹
یکی از این مقامات بلندپایه عربی گفت خشم کشورهای خلیج فارس به بالاترین سطح از زمان آغاز حملات آمریکا و اسرائیل به ایران در فوریه رسیده است. ترامپ این جنگ را شروع کرد و ما بهای آن را می‌پردازیم./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/681813" target="_blank">📅 23:39 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681808">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtqOk0yf_3yxhNT1VkiPFQj3kFDNSSsmsay4Co-HNsLH946kocmHh5x85ae_kGEfo8F5XHVuYpZfZUh8eMieWCWmUyr6xS0GZatTq30YCeD3fAB4RrfNyDEK8VJkE5QADGWMB33U3RtfiPvFIHbabO6rerB6PPGNMvmTpJZjSjX1Mvepfgb5vKS3WcE-y8ifurs3gpdnQVkrUxua4yxuo2XwQ-EOKHnOzs24sDruHh9Zs0iWuGq8SM1keyNWgF4Bpia2lyfF-6b7zQu-jjmjTYRfdp5pryb02hMIz3OUSxZZKf1unm-EOpPgKP8OYgLWTTzhN9fvjBOqfY6CtLCrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPaDjZ8mR8b1jSYupnW7mnSkUpB0Pgeos27lAc_dvrXTnOAAC9BC__Zc3iK3N__ZR_BpaVhyCEaWKryVhAAgAbopAmy0fQN-n2a47MPaceEkUoq5Tcst_lP-VZz4lLPA7HTNpf0gir31gQ4W5SDarJYZR-sa183MH1d2yFL4EvLASBQSuvgNsiLUmRTvATMvEzpdu7lOhXJALX406XRB8nDDZIaznlCEnbpSLkvW9-gVwzCjVRBc7giKkLligiX7rwcc2QlVxXTUxQgHlcgm_8RYzShazyuP2mZHL8V-oA4mSjzffEAUZLEtBoqOuj2YKW1pPUbn2KD_LWSg70Sdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfo47jPGcqTvkvA1uRnCnBEnQAOfPwn1lyfOXBL6Adr1Z97BsyNMUg_fbY5Hrw8olHno6kfNKsKIgeFebGO5QKPHum-O8buZgv0uf1p-tZhg_UrX2_JvtP0ehS3kpkk00w4WI79h3tRqPREx1ybkYuDF0NrcSqOfU_xwSCuvqfbWygY7tY1fdK_EuZBTeHFMzdK8bkzs1cdRdZ02LxHxvTMm3MKvOmt6jUuREyrp4N764-DTAq1kUFK2zchkzI4I91ao28xnMTaeDyt5P65s7JC9qgDpdTLjRA_4YnVu8AvU9Z2FUhaesbq7EtIABfWb1oJLvpZZKTmuFJKMXmvYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrQVOZogatYlQym5-Sc8KtFOi5asA-E6fFdOEcu7m8mr7ZLKBgbT3HCp0r4t9FlRlSe2pqkYrWSUOCy7O9tyq3s92jmmzoTZ-wL0f5jW-bra3smhm1sMlU2dY7DA1UOLdvkkJtwnu7iX0Wym5kmLy-TQHu5n_ruWzFantRH-Vnl-8KSoCNdO04VDZOJDpGt_teUZPSy2l2YYddMSDQ1AgqB8MV_HgPrRdM2wEUPLlq6CtxFGx_e9O-wcb8n9IxPG6vhBsitO5Dq2tUs9nCHkxxy5v1QnrSNgVB7flUnAcJYYvHAAgpZdKpW1e_iRjQS4DtXaoSG0Y52toNI02nB6sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYpkR_nhMeNxyDq5BAlRetF758M2X4G50qvrhsAQakx-5GG0SdZnA1MBiVUOGYArqh2p8ovKh4kJxtN7J0XlqPjYAddHUsCffHS4TPT2B4BZLMwVTgrZXmmLv0Lj13vIWIGIuVKmOlG2EEQQFOAS2Ya7S8MfkywFSzUJVIF6KEkoY1O82v_BLYvX-Avs8ZEGDIjDIEq-ntJSSnNKG6WLsmIDhEIEbC1k7KR-1V3Z7i219U4pycQZg7MyZDiEvwdOKhqGDZJFauEVPqOM3srHSSdHojgtlnvBQh2I8pjkHRA3c2sddCbDdnR5lc_XTZrQ9TOIrIoTJoh7Hk2Imps2-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
عددهایی که ترامپ را می‌ترساند
🔹
جنگ ایران فقط میدان نبرد را تغییر نداده؛ قیمت نفت و بنزین را بالا برده و حمایت آمریکایی‌ها از ترامپ را هم به سرعت کاهش داده است.
🔹
اعدادی که در این اسلایدها می‌بینید برای ترامپ خطرناک است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/681808" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681807">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=C5VfAmXGngFiTTx34bQMopEnexowGzMWj4g8N9RjqAO36_PDj5mC0pg3BOb85KOHWZlr4kA3vSir96BgoCDeZXzHz1ujMwGlB2Ex9FRlBo6_uiK5qUsFR79FkOhjk1Lmkp5JcUv9qATSKA1qJGvpliyKUcEUGvnCp5JyA52Voz_aw9AEkBSGs1E1ISvphy7Jndy5PxjL8rgDeoaNtdCB7Np-2ynZ0hG7_Xoz51aOuHzLpMEMRIyUc2fhou70M7u4XdOcfuC6SspTimhikvHSVVYDg0bTWKnqidcbQVHP-xwiEjajG9xKPGpqfzeN3VDm-pGGbN1thER5eNdYkEpX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b0e2e6f0.mp4?token=C5VfAmXGngFiTTx34bQMopEnexowGzMWj4g8N9RjqAO36_PDj5mC0pg3BOb85KOHWZlr4kA3vSir96BgoCDeZXzHz1ujMwGlB2Ex9FRlBo6_uiK5qUsFR79FkOhjk1Lmkp5JcUv9qATSKA1qJGvpliyKUcEUGvnCp5JyA52Voz_aw9AEkBSGs1E1ISvphy7Jndy5PxjL8rgDeoaNtdCB7Np-2ynZ0hG7_Xoz51aOuHzLpMEMRIyUc2fhou70M7u4XdOcfuC6SspTimhikvHSVVYDg0bTWKnqidcbQVHP-xwiEjajG9xKPGpqfzeN3VDm-pGGbN1thER5eNdYkEpX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حضور یک شهروند ناشنوا در تجمعات شبانه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/681807" target="_blank">📅 23:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681806">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4940f4d822.mp4?token=dW6rv9gNuMm2rc4LbvxSSdxqu-Ed5F02qLBa1lMDMZU6KoSmeM3huiAfFnz1BnIeQq2p3FbzX6l_p0-fxT_ho7uId6XMiytmBi4vBLQcP20NEB3qwE7C5Efya1OxdWyS9D11n8vg2x7bbD9BDT54qecpc4hQ_8yqYr5ARNNdohNotaWs6vf7ZWXJ0-Bu4EPdaTjlmTAbB2Tity70Puhqxujuv9vhS20LjDR5Ta4QKg8YaHtKGXoXMOE8Snh-W4apLJ0fE4Kt5u7xaaUSsNcxEHny274Uo72E1eXjnCxBNxkkghbQMI7-9azbnwxivgDUWA0a5KcG7cgh7DBhUdkQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4940f4d822.mp4?token=dW6rv9gNuMm2rc4LbvxSSdxqu-Ed5F02qLBa1lMDMZU6KoSmeM3huiAfFnz1BnIeQq2p3FbzX6l_p0-fxT_ho7uId6XMiytmBi4vBLQcP20NEB3qwE7C5Efya1OxdWyS9D11n8vg2x7bbD9BDT54qecpc4hQ_8yqYr5ARNNdohNotaWs6vf7ZWXJ0-Bu4EPdaTjlmTAbB2Tity70Puhqxujuv9vhS20LjDR5Ta4QKg8YaHtKGXoXMOE8Snh-W4apLJ0fE4Kt5u7xaaUSsNcxEHny274Uo72E1eXjnCxBNxkkghbQMI7-9azbnwxivgDUWA0a5KcG7cgh7DBhUdkQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هند نخستین پهپاد تهاجمی بومی خود را با موفقیت آزمایش کرد
🔹
منابع خبری گزارش دادند که شرکت فناوری پهپاد هندی «کاوا یوایوی» اولین پهپاد تهاجمی خود به نام «دیویاسترا ام‌کی۳» را با موفقیت آزمایش کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/681806" target="_blank">📅 23:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681805">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czej9R50dbOJXJ_mobRVXyuxpDQpX2Mx85T8Yff4NKNShmXhCFLTHs-FNNfeeumJdZVB0lKlNVEk8pVzzGJcm5cy1dQgjXukgQsqXNI7teRGKSTI1QnMZyjhpKT9vDFNht_8oT04WC085zcsaUMuEh1L7PBI49e9YD4_ciZeI03CcNnClg71E0Il7v3IeH2rTMS9EXZR4w0_uFaEvX4U7tzkWcRL6H_nX7JjzxTS7KDpyHnyQqySbgTnfLKQ5OVffsfFB8vCgu_vAQqFigxsIw1X3GJNEX8LXNH-9Vvg7oVSb3qKm7zMb3wLWYoza4Wlwbb6Zonz60FyKR5CqaBVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راشاتودی: صبر متحدان عرب واشنگتن در برابر راهبرد ترامپ لبریز شده است
🔹
عربستان سعودی، امارات، قطر، کویت و بحرین نسبت به راهبرد دونالد ترامپ در قبال ایران که «غیرقابل‌پیش‌بینی» ارزیابی می‌شود، نگران هستند.
🔹
پس از ماه‌ها درگیری و حملات، برخی از این کشورها حتی بازنگری در حضور نظامی آمریکا در خاک خود و جستجو برای یافتن اتحادهای امنیتی جدید را آغاز کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/681805" target="_blank">📅 23:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681804">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
امروز مردم ۳ هزار میلیاردتومان پول به بورس تزریق کردند
🔹
در جریان معاملات امروز، حقیقی‌ها بیش از ۳ هزار میلیارد تومان پول تازه به بازار سهام تزریق کردند و ارزش معاملات خرد به حدود ۳۹ همت رسید.
🔹
هم‌زمان، صندوق‌های درآمد ثابت با تراز نقدینگی منفی ۱.۸ همتی مواجه شدند و صندوق‌های طلا نیز ۲۳۴ میلیارد تومان ورود پول ثبت کردند؛ نشانه‌ای از افزایش تقاضا برای دارایی‌های ریسکی و طلا. /خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/681804" target="_blank">📅 23:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681803">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae83786da.mp4?token=v1CJN6cUrY4Wab5_ZZJnYyNT9jfhrUOkMeX8PbrN5gt5rrMICaM3vQ963Oy-7hUOS0BdPcUQsgk8jfKKPH7VPposGst-R_K9HLeWBbG_cuDrd6ZG29w3zesyQG_FxCO8IC61sYhYE2j0-uefTGYbvmM7RuzK5nZCXB0WcZfu7NISltes6VVSvCEc58R6JnivommjgjSffgQGwvzIeXnFE34sBXEh0sFWfHQMIaHeS1z4ZHeZbz3ZP5eif_Wa0Gd2gow5ifwf2Gpso3GXUn_-a4vATXy2pz0i3YY_Sa8bjDLJxWK6jPbICizMq_GZIMfHKIQQkPxqpHVaG7UyB-mp0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae83786da.mp4?token=v1CJN6cUrY4Wab5_ZZJnYyNT9jfhrUOkMeX8PbrN5gt5rrMICaM3vQ963Oy-7hUOS0BdPcUQsgk8jfKKPH7VPposGst-R_K9HLeWBbG_cuDrd6ZG29w3zesyQG_FxCO8IC61sYhYE2j0-uefTGYbvmM7RuzK5nZCXB0WcZfu7NISltes6VVSvCEc58R6JnivommjgjSffgQGwvzIeXnFE34sBXEh0sFWfHQMIaHeS1z4ZHeZbz3ZP5eif_Wa0Gd2gow5ifwf2Gpso3GXUn_-a4vATXy2pz0i3YY_Sa8bjDLJxWK6jPbICizMq_GZIMfHKIQQkPxqpHVaG7UyB-mp0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار جوانی: دشمن بداند که نمی‌تواند اقدامات غافلگیر کننده‌ای را علیه ما انجام بدهد، او باید منتظر غافلگیری‌های راهبردی باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/681803" target="_blank">📅 23:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681802">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سردار جوانی، معاون سیاسی سپاه: انتصابات انجام شده نوعی بازآرایی و کارآمدکردن دکترین دفاعی انقلاب اسلامی به اقتضای شرایط است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/681802" target="_blank">📅 23:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681801">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=RqeqNp1Mw7bvUZ3mDvZwkoiFSjSTOPNc89dIvCV38XJrPrtenS_6ftbyh8KtKFUoMmGBcO9HMWosqFe7MJxmpOXuXCjhoxzKA2bmP2tgS6T3QdItFGRcRNIj2HG1MyNxwOlKR2kWhkvnKoMnxE5RxNLtHbp2_bQPx6EfSAnYracL4weNrVu9d4G7LEHvdog-Xlyr5Eig0ZjHPn9p_KN24n7Uj-A3O5UNJmXq6OW-wkTb6kMHVnOD2rpBYzLbNclcTmuGqhy0hvYBNM_4jzD6f8fFuUHRkM4j8RgS4VK3vYrX0uYHn9WR6F2DK82z4pOxL2MEXlT6B3ykgXUmuI59Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edeccab51d.mp4?token=RqeqNp1Mw7bvUZ3mDvZwkoiFSjSTOPNc89dIvCV38XJrPrtenS_6ftbyh8KtKFUoMmGBcO9HMWosqFe7MJxmpOXuXCjhoxzKA2bmP2tgS6T3QdItFGRcRNIj2HG1MyNxwOlKR2kWhkvnKoMnxE5RxNLtHbp2_bQPx6EfSAnYracL4weNrVu9d4G7LEHvdog-Xlyr5Eig0ZjHPn9p_KN24n7Uj-A3O5UNJmXq6OW-wkTb6kMHVnOD2rpBYzLbNclcTmuGqhy0hvYBNM_4jzD6f8fFuUHRkM4j8RgS4VK3vYrX0uYHn9WR6F2DK82z4pOxL2MEXlT6B3ykgXUmuI59Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جوانی که با دست‌سازه‌هایش یاد شهدای کودک و نوجوان جنگ را زنده نگه‌ می‌دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/681801" target="_blank">📅 23:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681800">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
معاون سیاسی سپاه پاسداران انقلاب اسلامی: از سه منظر می‌توان به احکام صادره از جانب رهبر معظم انقلاب نگاه کرد
🔹
اول از منظر فضا و شرایط
🔹
دوم از منظر پیشینه و سوابق افراد
🔹
سوم از منظر مطالبات رهبر معظم انقلاب از افراد منصوب شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681800" target="_blank">📅 23:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681799">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee142e9f9.mp4?token=kM-gmF-iZ6kK8THI2VcqfjwXqp-J0-G3vqCs5_7Gy33YVwN7Q6u-fyql5w29gtk8SwDR2pENsPb3rwGUDDlWh9Erg6cIfMf-tatas4UCehxp3NswTzCMhDPiLk6pHvw8SnLyFU-1bA3ksZArWnbMwvW5zFHj62RU7xBX3dIj6HJJWrJZHiY_ntkpFhKuLnNdNT67luV4f7r-v-NKshai76OpK9xLFjTsWA9oynqsO-DvQSgcbMjSFl73IPU0notTz246FjSfW5tX9vGewioExwVm102hJUw_-2fUnd6RwkHUkaxcr0Yu1SJeAYkhGiPOOy_hBm1OYGV4szRly71DLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee142e9f9.mp4?token=kM-gmF-iZ6kK8THI2VcqfjwXqp-J0-G3vqCs5_7Gy33YVwN7Q6u-fyql5w29gtk8SwDR2pENsPb3rwGUDDlWh9Erg6cIfMf-tatas4UCehxp3NswTzCMhDPiLk6pHvw8SnLyFU-1bA3ksZArWnbMwvW5zFHj62RU7xBX3dIj6HJJWrJZHiY_ntkpFhKuLnNdNT67luV4f7r-v-NKshai76OpK9xLFjTsWA9oynqsO-DvQSgcbMjSFl73IPU0notTz246FjSfW5tX9vGewioExwVm102hJUw_-2fUnd6RwkHUkaxcr0Yu1SJeAYkhGiPOOy_hBm1OYGV4szRly71DLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم  رئیس مجلس:
🔹
ملت ما در یک جنگ ناجوانمردانه، مقابل دشمن آمریکایی و صهیونیستی شجاعانه ایستاد.
🔹
به‌عنوان یک خدمتگزار که به جزئیات آشنا هستم، با همه وجود می‌گویم ما در این جنگ، در بُعد نظامی و بُعد سیاسی، به معنای…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/681799" target="_blank">📅 23:09 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681797">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
معاون سیاسی سپاه: اقدامات ما تاکنون تدافعی بوده؛ ممکن است تهاجمی هم بشود  سردار جوانی:
🔹
نیروهای مسلح براساس احکام صادرشده، رویکردهای تحولی خواهند داشت و هر اقدامی برای دفاع از کشور، تأمین امنیت و خنثی‌سازی تهدیدات دشمن در زمان لازم انجام خواهد شد.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/681797" target="_blank">📅 23:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681796">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
خیابان‌های اسرائیل در سایه انتخابات
🔹
بنر تبلیغاتی حزب لیکود، حزب سیاسی نتانیاهو، با تصویری از رهبر معظم انقلاب اسلامی، زهران ممدانی، رجب طیب اردوغان و شیخ نعیم قاسم و این نوشته در خیابان‌های اسرائیل مورد توجه کاربران قرار گرفته است: «آن‌ها می‌خواهند نتانیاهو…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/681796" target="_blank">📅 23:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681795">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
پزشکیان: این‌که برخی از بیرون گود صحبت کنند و خیال کنند حل مشکلات کار راحتی است درست نیست
🔹
ما حزبی و جناحی عمل نمی‌کنیم؛ هرکس می‌تواند مشکلی را حل کند وارد شود و قسمتی را دست بگیرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/681795" target="_blank">📅 23:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681793">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
پزشکیان: در نهاد ریاست‌جمهوری ۸۰ درصد در مصرف آب، برق و گاز صرفه‌جویی کردیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/681793" target="_blank">📅 22:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681792">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSnQ_tzOHNjl3E5PQNcVAANVaNAYaBe_VjvA1nRXOdyiHUki3fWPNrf2To7FRiJvnyuBgnnhkm5gUJdIEd-w4mg6VDDxlNomkKrTbN6STmlnvzIKQf9w_wV2XC4bvQaUPNiVrW9yNPTEwbLbatuvskmQfXtdLAiXPchM7-1rLQKq6z1Gx-LVTzez6LpaY2rNyQpgqnpyHjC5yaAe6KS5vZ70ItOm73_5BRHyg9JLxD7tD-1pAO8B5hH-TSL7qM3gIiaRd5-W5mgtOFPqGdR-zscWLLY5NZXDhDmnwtSEBUtkXwUH4w9yTUyW0PngkK1LvR0VYLqy94cb3Z3RXW9vxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«هم‌پی» راهکار پیشتازانه بانک اقتصادنوین برای آنکه چرخ تولید متوقف نشود!
🔹
بانک اقتصاد نوین همزمان با بیست‌وپنجمین سال فعالیت خود، طرح «هم‌پی» را برای پاسخ به مهم‌ترین نیازهای مالی تولیدکنندگان و فعالان اقتصادی ارائه کرده است؛ از تأمین حقوق و مواد اولیه تا فروش اعتباری و تأمین تجهیزات نیروگاه‌های خورشیدی
🔹
«هم‌پی» تلاشی است برای عبور از چالش نقدینگی و کمک به تداوم فعالیت و رشد کسب‌وکارها.
برای اطلاعات بیشتر:
https://enbank.ir/s/mfa9aC
☎️
02162740</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/681792" target="_blank">📅 22:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681791">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d651a948d.mp4?token=OZJ-KVc5aYDsIUpjmioqehc60gJqXsNbHLHxcRgrJ-glthbD2dGvNIfGNzP5ZKHpp3ret_fl61ByYqo-o2wIqwr8eYnLNnNti0gsOeB2lTFyuNvMSDjmyUn6OptnlNUWcaiML2KdSFYCxVXlzS4c4DexxC4ZLH5L73bpbmNFWa278n277adB7ShXnvfzpjEB9zZnwGEb8T4kRd6lDZLOV6JKpk3eYH1ilUHDSn9twsN0sItECW1Xvt1CN5E64Ghs2wbaVlU8TpSDzXzugmBeOXKDmET2f54n2UdO_0gyW626xoKS1ShTmlY4jAnuBR4wsRwifInVDe6AG0sEoHfltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d651a948d.mp4?token=OZJ-KVc5aYDsIUpjmioqehc60gJqXsNbHLHxcRgrJ-glthbD2dGvNIfGNzP5ZKHpp3ret_fl61ByYqo-o2wIqwr8eYnLNnNti0gsOeB2lTFyuNvMSDjmyUn6OptnlNUWcaiML2KdSFYCxVXlzS4c4DexxC4ZLH5L73bpbmNFWa278n277adB7ShXnvfzpjEB9zZnwGEb8T4kRd6lDZLOV6JKpk3eYH1ilUHDSn9twsN0sItECW1Xvt1CN5E64Ghs2wbaVlU8TpSDzXzugmBeOXKDmET2f54n2UdO_0gyW626xoKS1ShTmlY4jAnuBR4wsRwifInVDe6AG0sEoHfltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سیاسی سپاه: اقدامات ما تاکنون تدافعی بوده؛ ممکن است تهاجمی هم بشود
سردار جوانی:
🔹
نیروهای مسلح براساس احکام صادرشده، رویکردهای تحولی خواهند داشت و هر اقدامی برای دفاع از کشور، تأمین امنیت و خنثی‌سازی تهدیدات دشمن در زمان لازم انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/681791" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681790">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
موافقت مشروط حماس با نقشه راه مرحله دوم طرح صلح در غزه
🔹
هیئت حماس به ریاست خلیل الحیه در دیداری با میانجی‌گران و ضامنان توافق آتش‌بس در غزه که با میزبانی مصر برگزار شد، بر مواضع خود برای دستیابی به صلح پایدار تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/681790" target="_blank">📅 22:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681789">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fae229f2.mp4?token=sZcAAd0gStZqrI4kH9EhEfqn2a2mjWKrCoo5rGZI91VyuYBgi4rjlqHSMnWcZ6OP1n63JDNwPvCMMLUV3qh7DPjLf4PYeEmLjXz4Q7AKzwR2F2Y1hVrvMTxSeqhOzNUs-M_TZbt-N8RTkVV7EuAlKO4MK3zgyKkbL4Pgkp0eVsfmKE7Tr7RGrzKV-o5NJeDrtnLX16RwBAexIeXnHZrcnqu0hqN5qzWgNGxjbzJ3HJ9P5WpSW-3655BgQgNZkIkMr5f-Hg0voLNlfPS14mkC4kRUMeId9IPan_eKDQU955CPagOwTsJnR0m5bKznFNtHDtE7XRQtsa0cT5zrSlMQjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fae229f2.mp4?token=sZcAAd0gStZqrI4kH9EhEfqn2a2mjWKrCoo5rGZI91VyuYBgi4rjlqHSMnWcZ6OP1n63JDNwPvCMMLUV3qh7DPjLf4PYeEmLjXz4Q7AKzwR2F2Y1hVrvMTxSeqhOzNUs-M_TZbt-N8RTkVV7EuAlKO4MK3zgyKkbL4Pgkp0eVsfmKE7Tr7RGrzKV-o5NJeDrtnLX16RwBAexIeXnHZrcnqu0hqN5qzWgNGxjbzJ3HJ9P5WpSW-3655BgQgNZkIkMr5f-Hg0voLNlfPS14mkC4kRUMeId9IPan_eKDQU955CPagOwTsJnR0m5bKznFNtHDtE7XRQtsa0cT5zrSlMQjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: ما در بُعد نظامی و سیاسی جنگ پیروز شدیم
رئیس مجلس:
🔹
ملت ما در یک جنگ ناجوانمردانه، مقابل دشمن آمریکایی و صهیونیستی شجاعانه ایستاد.
🔹
به‌عنوان یک خدمتگزار که به جزئیات آشنا هستم، با همه وجود می‌گویم ما در این جنگ، در بُعد نظامی و بُعد سیاسی، به معنای واقعی کلمه پیروز شدیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/681789" target="_blank">📅 22:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681788">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: یک شرکت چینی، تامین مالی تهران را بر عهده دارد
وال‌استریت‌ژورنال:
🔹
شرکت هنگلی توسط امریکا متهم به وارد کردن عمده نفت خام ایران شده است؛ این شرکت پتروشیمی چینی، تجارت با ایران را انکار می‌کند. این پالایشگاه بزرگ چینی، تامین مالی تهران را بر عهده دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/681788" target="_blank">📅 22:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681787">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBab2CkvoIwSJZ__tkPgbvg6fOunF8v_Or_pTQDwUHAvhI-ofMat6Nm6ZNRGE61cSKeKDzpELAz4FQjte6BlMwKKIcnNjpZ8jnnrsUmlpsi74L02dPm2AF-B-DKzTx0VpLXlMn9gnXSm2zUGvAyTPuoowwJRd0VGwFndH30KbIJBjM4UG3tHpCbkdAAEMMONBQY0cn095ggeRZON55lNth1_kXgpOx_NVxfYrIWjZI2lGITnhCKrvewvq06yRaDqx2zg_Aey6L7hp0_GLuWE86nXoxAgVSDUhthFUomB5bY42eM-rHQ98be4zeK9wzl3aPy8pL94rh_g72aOpCETFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر سی‌ان‌ان: ترامپ می‌تواند تنها رئیس‌جمهور ایالات متحده باشد که جنگی را به تنهایی آغاز کند و آن را ببازد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/681787" target="_blank">📅 22:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681786">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90cedd77f.mp4?token=G4gsqAtZ2KmjwaPT5h8VBPAJolDqEXoXZn8Uy-FTH7umDwRApLPGDiZ54Yk6oPGVKkXl2WvhAUHWEHC2mKcL3ezTXlbkmxR_Qa-TZtJ-VLSDPKueZ15DNhIqoiSKQ7Xy3AvTZiyPzqdmLZC0zTKgnc-YyhwHn58QhR-nCd8LoslG8maCVFftmYmErXq8GY-1aMrbOXn84tzRIygQNydcqXWFsJw4Kn9X92KHr_YOg75LBGRwTHJwvlTJIl9YRRS9qT_3E7N3O7OQefV3UalSgoABfYd_cBISGx8rx6FPVgQUsy_6DhgHm5-Qf_4mNKy1U396i39R_ZTk8w4oITJgjJvLTJHGsXKE8qyZJsU4rv4ftij4Rwab9iseG3uEI_lLiwyFJOrlY1mRruhqMZhXq6jZ0eY2zHw4yI9rgaiQX7vo6HML9gpCPb3a1nT-7GmRkbvPisqOl6tI4ziOEENSfMlPFVKYK5KK27cFX8oxr7_1MCr0Og2_gXA6ayzAxHHonEIJexISmQorufwMxtA35GQVQbwGU9jvJynOS6zTF6THRJrolyZ_DIfd1S07NcIVck3Rfif3XgDt9Zi1UzhNP2rQtBkxNw1XlPw2uiLl8DLX23CPLeKTfqsBebvjMy022U_loaNIzOTBZNsQG4A_EbMxDnLFzAHNAD6jiSiawAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90cedd77f.mp4?token=G4gsqAtZ2KmjwaPT5h8VBPAJolDqEXoXZn8Uy-FTH7umDwRApLPGDiZ54Yk6oPGVKkXl2WvhAUHWEHC2mKcL3ezTXlbkmxR_Qa-TZtJ-VLSDPKueZ15DNhIqoiSKQ7Xy3AvTZiyPzqdmLZC0zTKgnc-YyhwHn58QhR-nCd8LoslG8maCVFftmYmErXq8GY-1aMrbOXn84tzRIygQNydcqXWFsJw4Kn9X92KHr_YOg75LBGRwTHJwvlTJIl9YRRS9qT_3E7N3O7OQefV3UalSgoABfYd_cBISGx8rx6FPVgQUsy_6DhgHm5-Qf_4mNKy1U396i39R_ZTk8w4oITJgjJvLTJHGsXKE8qyZJsU4rv4ftij4Rwab9iseG3uEI_lLiwyFJOrlY1mRruhqMZhXq6jZ0eY2zHw4yI9rgaiQX7vo6HML9gpCPb3a1nT-7GmRkbvPisqOl6tI4ziOEENSfMlPFVKYK5KK27cFX8oxr7_1MCr0Og2_gXA6ayzAxHHonEIJexISmQorufwMxtA35GQVQbwGU9jvJynOS6zTF6THRJrolyZ_DIfd1S07NcIVck3Rfif3XgDt9Zi1UzhNP2rQtBkxNw1XlPw2uiLl8DLX23CPLeKTfqsBebvjMy022U_loaNIzOTBZNsQG4A_EbMxDnLFzAHNAD6jiSiawAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ سرخ بر روی پرچم‌های رژیم صهیونیستی
🔹
شماری از فعالان حامی فلسطین، امروز یکشنبه، پرچم‌های رژیم اشغالگر را در  «چهارراه روابی» واقع در شمال رام‌الله به رنگ قرمز در‌ آوردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/681786" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681785">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f90307c.mp4?token=ogZ4PZ-VLFvFSywSAJX1K3HIgtwPkjHo0HQkpAY7VhjBperJlH2p-UxlApk7RPtBpWOwjvjX_gDcrBjimvkXJnO265Sovc9TrmHRJo3YysOqGiC75b2SU9Nkl9p9E7ZArN7PGrytrw4iyVkWHIrW0JVv5pkP-MQi1B-mDVkuVWelUb-gd1bYbsTPQXai85vCXncDm2Ibkn9Mj3AZkD9J07X1a7galzQRbse34BH4bjCvwwpYtd9_bSI1QwPJzOstWKK91M0mGibNkD7xpLsU7_-Ij4CRu9faQdY-qfZn14Re4cCea1l0765KnsRnNl87HvCDVVZCvK1NTLHKYJax2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f90307c.mp4?token=ogZ4PZ-VLFvFSywSAJX1K3HIgtwPkjHo0HQkpAY7VhjBperJlH2p-UxlApk7RPtBpWOwjvjX_gDcrBjimvkXJnO265Sovc9TrmHRJo3YysOqGiC75b2SU9Nkl9p9E7ZArN7PGrytrw4iyVkWHIrW0JVv5pkP-MQi1B-mDVkuVWelUb-gd1bYbsTPQXai85vCXncDm2Ibkn9Mj3AZkD9J07X1a7galzQRbse34BH4bjCvwwpYtd9_bSI1QwPJzOstWKK91M0mGibNkD7xpLsU7_-Ij4CRu9faQdY-qfZn14Re4cCea1l0765KnsRnNl87HvCDVVZCvK1NTLHKYJax2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در نهاد ریاست‌جمهوری ۸۰ درصد در مصرف آب، برق و گاز صرفه‌جویی کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/681785" target="_blank">📅 22:43 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681784">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=HXpdTpJaJ3PBqnMMvP98W1k56wjTW6wdDT6RvS9lUqkSwat3g2xGY0y7uCd__eS70aArqJMpFMpdu71gt5IHCS_3flNJWlleOOanyNZRShcSGKa6P7lmhiwV-gM9IjXrCwbA8Mq3REZikMpiEHaA7pljVhy1u32I48-zgIr0NfpO4mdy7s3Kjo-JQ1JvGNJKkKYRpfqaHrGf1IhhZH5_asVMtJecFUXjYAC973Sre4JgkgQkf9OIj1Kub_i8cA-AZwIDsUXKjXpyBhKJ-MVZQlIi2TKqCe_2T2AgZXBN_RGEHYChxkrkTZVk-mxWH_EgnQilwscUCWhFTH6qj5XmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3a28d146a.mp4?token=HXpdTpJaJ3PBqnMMvP98W1k56wjTW6wdDT6RvS9lUqkSwat3g2xGY0y7uCd__eS70aArqJMpFMpdu71gt5IHCS_3flNJWlleOOanyNZRShcSGKa6P7lmhiwV-gM9IjXrCwbA8Mq3REZikMpiEHaA7pljVhy1u32I48-zgIr0NfpO4mdy7s3Kjo-JQ1JvGNJKkKYRpfqaHrGf1IhhZH5_asVMtJecFUXjYAC973Sre4JgkgQkf9OIj1Kub_i8cA-AZwIDsUXKjXpyBhKJ-MVZQlIi2TKqCe_2T2AgZXBN_RGEHYChxkrkTZVk-mxWH_EgnQilwscUCWhFTH6qj5XmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید رئیس‌کل بانک مرکزی بر پیگیری مسائل صادرکنندگان و پیمانکاران ایرانی در عراق
🔹
رئیس‌کل بانک مرکزی در دیدار با تجار، صادرکنندگان و پیمانکاران ایرانی در سفارت ایران در بغداد، مسائل و موانع فعالیت اقتصادی در بازار عراق را بررسی کرد.
🔹
موانع بازگشت ارز صادراتی، مشکلات تعرفه‌ای، مطالبات پیمانکاران و نیاز به ضمانت‌نامه حسن انجام کار از مهم‌ترین موضوعات مطرح‌ شده در این دیدار بود.
🔹
همتی با تأکید بر اهمیت بازار عراق برای فعالان اقتصادی ایران گفت این مسائل با جدیت پیگیری خواهد شد و بانک مرکزی برای تسهیل فعالیت صادرکنندگان و پیمانکاران ایرانی و افزایش هماهنگی میان دستگاه‌های دولتی و بخش خصوصی تلاش خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/681784" target="_blank">📅 22:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681783">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=qE1Surmma9HzA3L985A5JRoTelDxezhPMbMG377f2Gb3AhkHnn_DITbhMd4aqztELkNCGHt_cqYAKUPNU4TjPFYG0A6lCUI_kleDVLX58IqLeEQqBEzTVfviyQfBb_mzyce58g0aiZOXosIkr5GocuRkXRIBhvH9M3APeJdcPn6CM1YFN7iOwAqhSGFJlDo5ckkJ7kcEhmvjuevt3_V9Sk6RyKdcMp_xcfieznEB81z2BRPXzq_h7z4AN5KeQizO0EhHt1L-4aYVGyzUlkuWGgfnfl19Y9Be_TWweF2ryCPgeSVdCokiWWPpwL_iTCMGbUsA7wiC5MzDQCnCF7u5BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cd296c47d.mp4?token=qE1Surmma9HzA3L985A5JRoTelDxezhPMbMG377f2Gb3AhkHnn_DITbhMd4aqztELkNCGHt_cqYAKUPNU4TjPFYG0A6lCUI_kleDVLX58IqLeEQqBEzTVfviyQfBb_mzyce58g0aiZOXosIkr5GocuRkXRIBhvH9M3APeJdcPn6CM1YFN7iOwAqhSGFJlDo5ckkJ7kcEhmvjuevt3_V9Sk6RyKdcMp_xcfieznEB81z2BRPXzq_h7z4AN5KeQizO0EhHt1L-4aYVGyzUlkuWGgfnfl19Y9Be_TWweF2ryCPgeSVdCokiWWPpwL_iTCMGbUsA7wiC5MzDQCnCF7u5BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید با سرمایه‌گذاری روی فرزندان خود به توانمندی‌هایی برسیم که کسی جرئت نکند به خاک ما حمله کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/681783" target="_blank">📅 22:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681782">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b9644dc1.mp4?token=Ufp_gxiw_xHZQhLxE8yvOl8fyPxtXPI_IrYiPq0sy90sra7BF97i4kvrq7FCNbxfGkGUs5wvwy1MUTzoKqJkhZchwmwP6CBMWFzE-w0hS5vhOckEFVQyDRylij3jfGINSf12Zb9_E9bYN9BBZ3slHKLRVRoSRYLgUHP2nzJC8Ywcm7TBUJwpXKOYhEJzpMA7GUi8jy5gi3OqO0W2744oLirf50MmViqwl74CB0Nlsi1pa6_J6tZgX9FC8fQQlikebkIn4cgDUOVVPel-2-RQVFU1zU4F9t-9jWHXjUyYpmHgy7q-Q6e0pMQx-e82VRVgOcvnJSPm-OYUBQTwBaJJQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b9644dc1.mp4?token=Ufp_gxiw_xHZQhLxE8yvOl8fyPxtXPI_IrYiPq0sy90sra7BF97i4kvrq7FCNbxfGkGUs5wvwy1MUTzoKqJkhZchwmwP6CBMWFzE-w0hS5vhOckEFVQyDRylij3jfGINSf12Zb9_E9bYN9BBZ3slHKLRVRoSRYLgUHP2nzJC8Ywcm7TBUJwpXKOYhEJzpMA7GUi8jy5gi3OqO0W2744oLirf50MmViqwl74CB0Nlsi1pa6_J6tZgX9FC8fQQlikebkIn4cgDUOVVPel-2-RQVFU1zU4F9t-9jWHXjUyYpmHgy7q-Q6e0pMQx-e82VRVgOcvnJSPm-OYUBQTwBaJJQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان رو به مدیران: شما می توانید در روش آموزش تغییر ایجاد کنید
🔹
هر چیز که در جستن آنی، آنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/681782" target="_blank">📅 22:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681781">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3387030c.mp4?token=Mm2NIptUXtr21u7U3IA9-LbgmguRWjJR0wx4WaW0bt1vA4KLI5GVMBwqov8P30OR5VVZRt3bggYnyiLfRMeYagbdhity71-8pGaCDJ4dfWznjvUaLjKrqYDB6wNJICMNQ5rzjtvMGzcB7BbGrVFgkoTX8cu3L8ZVF73qWTtl8aPUmoBElMQEEuWEUprAtnTWwSmyUo_JPBesUv_ae5YtP6FHRp5Vm8svT8oD5dMPd6TeU5ktR64RLpzWC-bsACMNWT8CKYTPoDjDjkKpUyBp-qckVTzoPaeCFRgmM6wPhB1qokZwRJqCJtpme4uSClLqr-pD2UKsj4wuj0I9Bv2Jbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3387030c.mp4?token=Mm2NIptUXtr21u7U3IA9-LbgmguRWjJR0wx4WaW0bt1vA4KLI5GVMBwqov8P30OR5VVZRt3bggYnyiLfRMeYagbdhity71-8pGaCDJ4dfWznjvUaLjKrqYDB6wNJICMNQ5rzjtvMGzcB7BbGrVFgkoTX8cu3L8ZVF73qWTtl8aPUmoBElMQEEuWEUprAtnTWwSmyUo_JPBesUv_ae5YtP6FHRp5Vm8svT8oD5dMPd6TeU5ktR64RLpzWC-bsACMNWT8CKYTPoDjDjkKpUyBp-qckVTzoPaeCFRgmM6wPhB1qokZwRJqCJtpme4uSClLqr-pD2UKsj4wuj0I9Bv2Jbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جدال بلژیک با بزرگترین آتش‌سوزی جنگلی ثبت‌شده در تاریخ  این کشور
🔹
بلژیک با بزرگ‌ترین آتش‌سوزی جنگلی ثبت‌شده در تاریخ مبارزه می‌کند.
🔹
این آتش سوزی تاکنون ۳۰۰۰ هکتار از زمین‌ها را سوزانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/681781" target="_blank">📅 22:32 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681780">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6Nz0EqjrY6xU91-fsaoL1YygN78UlDGdctHhAa-br0LgU8FR-GTkP8B8y4fKYsVmcqK30i0RQx5dUcxjQK3QJA5jmM3jeya3tqFu3aHrvyFYZB5FxrVw7jjm4at-ofXcKnTHxO_bnRTTWNGXg1SiQrVaJTnzE1fWbEGe59IBRYV6aVSLbBE-fM502UTiZXV1bFLkP-pDjU6WKKPsX2Dr7JceWAweJ_M0muM-LvwuTwty4rhIoPSTMKg8c16Lb9poSdljjKHKWPceDLYjmgVGfhrYrrz_kQ0CSfTcfAmqSfi6RfPLQrdKrpUHQs5bmNXAPxm9vtp3U1d2XZ5cvA3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری کارگروه ملی امام رضا(ع) با حضور تولیت آستان قدس رضوی و وزرای دولت در حرم مطهر رضوی
آیت الله مروی، تولیت آستان قدس رضوی:
🔹
آستان قدس برای اداره حرم مطهر و ارائه خدمات در داخل حرم، به بهترین شکل ممکن، نیازمند کمک دولت نیست؛ اما آیا تأمین پارکینگ در خارج از حرم نیز باید بر عهده آستان قدس باشد؟
🔹
سالانه حدود ۳۰ میلیون زائر به مشهد می‌آیند و هر زائر نیز دست‌کم مبلغی را در این شهر هزینه می‌کند. طبیعتاً گردش مالی حاصل از حضور این تعداد زائر، رقم قابل‌توجهی است، اگر از این گردش مالی و درآمدهای حاصل از آن مالیات دریافت می‌شود، انتظار ما این است که سهمی از این درآمدها برای توسعه زیرساخت‌ها و خدمات مورد نیاز زائران اختصاص پیدا کند.
🔹
انتظار داریم در حوزه حمل‌ونقل ریلی و جاده‌ای، به‌ویژه مسیر مشهد ـ تهران، شاهد یک جهش واقعی باشیم و زمان سفر ریلی این مسیر کاهش یابد.
🔹
از مسئولان درخواست می‌کنیم برنامه‌های مربوط به دهه پایانی ماه صفر را به‌عنوان یک موضوع مستقل ببینند و آن را صرفاً ذیل عنوان و سازوکار اربعین تعریف نکنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/681780" target="_blank">📅 22:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681779">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41e1af3ee.mp4?token=vSF8fBgVOuLbYVLrX_zPDWfTKJXBleAx0FL6W6zM8ZiIq7ZM9m0QUqn9i8sSj5PRWZUbUR4VCZfJa9ok8HYg0dU1aYJZSI8MizhhN2ox8K9GiI74SaMOgPIMzCzMA28Y14cpOi2-i39idIK_DWsYc42SgJNO58_NNmMOFXm99DPA9I3OkDyj-q3a_SC8APJmayhOaMylsMetLS99gfxGkeSRNjmsVECbSl7n3fPLoIgsq5-HZ5F9hHdM6nNlxl2kJq0BX3eGHkzNZylYqZn6Y3xSYLPH5m1hvxnw_vgVtyNDoLajFfjlnKCNQ4W8468CBw59a8-aV1xjw0yefScW9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41e1af3ee.mp4?token=vSF8fBgVOuLbYVLrX_zPDWfTKJXBleAx0FL6W6zM8ZiIq7ZM9m0QUqn9i8sSj5PRWZUbUR4VCZfJa9ok8HYg0dU1aYJZSI8MizhhN2ox8K9GiI74SaMOgPIMzCzMA28Y14cpOi2-i39idIK_DWsYc42SgJNO58_NNmMOFXm99DPA9I3OkDyj-q3a_SC8APJmayhOaMylsMetLS99gfxGkeSRNjmsVECbSl7n3fPLoIgsq5-HZ5F9hHdM6nNlxl2kJq0BX3eGHkzNZylYqZn6Y3xSYLPH5m1hvxnw_vgVtyNDoLajFfjlnKCNQ4W8468CBw59a8-aV1xjw0yefScW9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی دندان آخری قصد بیرون آمدن را ندارد باید اینگونه آن را بیرون آورد
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/681779" target="_blank">📅 22:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681778">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
آموزش و پرورش آماده برگزاری حضوری کلاس مدارس در سال تحصیلی جدید است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/681778" target="_blank">📅 22:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681777">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnapptrip | اسنپ‌تریپ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAzVzMZ5ouN35IrEXIOFZGDanT2hKjPUKzGxVKlNEmN9sOWwvALxFRwjFHb8V8r2FlP6oP5ROMc_7QWAMXJFeu7i_ZgPSDezmtCPuJV-vKJANEnrOKEKW1Af70NMiSrVLlnxNCgCwXnK14xdPEvRaANyxEJuleBBGspNAfXayqoEmmx7WLLJzLs9yrm1BR3JptjZ4u083S_Giwdidwnls_m6gZ7ixvDUFpvmU1V--QN5KszIN3GzNUEUfnIVdm4Pf26Q5BkbVDqb1molvzc0MNWhDzZmzU2GOTInBbgjv9yqowDJKDRDYKLS93AeychctEs1xiIJ_qcTU0e2rMYW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
: پیش‌فروش بلیت قطارهای شهریور:
«
دوشنبه، ۲۶ مردادماه، ساعت ۸:۳۰ صبح»
🔺
تا ۵۰ هزارتومان تخفیف
با کد:
SHAHRIVAR
50
✅
خرید از وب‌سایت اسنپ‌تریپ و یا بخش «بلیت سفر» در اپلیکیشن اسنپ
🚂
خرید مستقیم:
https://snp.tips/40lda
🔹
@snapptrip</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/681777" target="_blank">📅 22:20 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681776">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
اعلام آمادگی جمهوری اسلامی ایران برای کمک به زلزله‌زدگان اندونزی
🔹
مسعود پزشکیان در پیامی به رئیس‌جمهور اندونزی ضمن همدردی با زلزله‌زدگان این کشور از آمادگی ایران به منظور ارسال کمک‌های بشردوستانه خبر داد.
🔹
متن پیام بدین شرح است؛
بسم‌الله الرحمن الرحیم
جناب آقای پرابوو سوبیانتو
رئیس‌جمهور محترم اندونزی
🔹
وقوع زمین‌لرزه شدید در شرق اندونزی و جان‌باختن و مجروح شدن جمعی از مردم آن کشور، موجب تألم خاطر شد.
🔹
اینجانب مراتب همدردی و تسلیت صمیمانه خود را به جناب‌عالی، دولت و ملت دوست اندونزی، به‌ویژه خانواده‌های داغدار و آسیب‌دیده، ابراز می‌دارم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/681776" target="_blank">📅 22:18 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681775">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9bvxX-Z8fn-xnLXxJkp8VfKeuFeugB48vzLFD8f_-8fFE6gI6CRLACRlcQjY-XaBeMDxKb4V-wzMdSV7oAEsHbDxkO492q17HRltCA7ylyQtImP37pA9CkDUQS7yFpgXAuZj4pU9K4LRWMW-g986UDOCd3YCVHmYPPpbn0it7xyEcdGpOBwyDPPqBU39naQmrtfq3Ujlb-Dc3pjjZ0hTQD1_-BxaR9r8sE7IcV3dTfn556WSRmuG7DaDZD4HpX3uyNt3O8qhf-xBy2PYnNin_JADu_uHbsm8TJVx5QMadhd7BdT3NtZnWYNvMXtK5xF9HFRsw6dGr4Z5TKH_3ymPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جعلی یک کاربر هندی درباره ایران سر از سخنرانی نتانیاهو در آورد
گلف‌نیوز:
🔹
این ادعا ابتدا از سوی یک حساب کاربری هندی منتشر و طی چند ساعت، توسط حساب‌های پرمخاطب اسرائیلی و سپس شبکه ۱۴ اسرائیل بازنشر شد. در نهایت نتانیاهو هم در سخنرانی خود به این ادعا استناد کرد.
🔹
فاکس‌نیوز نیز این ادعا را مطرح و آن را به‌عنوان نشانه‌ای بالقوه از نیات هسته‌ای ایران بررسی کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/681775" target="_blank">📅 22:15 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681774">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6162afaa76.mp4?token=GbZx-vXeVAzxXqtAQJ2sdWvxYH4TuWIP7OB4umn0M-B2UENMPoB3InqvSy-K9r_I0O_bt-qjK_vKksqsVcsk9fjxS6OO8DI1grHA-uFlYg40nMuf6BnbFeiPLO2IAUx35FBRvphyJ8cknxLx_iNyPneJ4Ar6RgbLalk_L1Z-uvcV57G-6YAymOWxcpdsMaSNEUWuHrr1V8kqGPib9W9WFqGNyLocBf4bR2L3Lm5taPCsgMUtkTMJeMTNdoAZj2YDZBijy1cP0woSVFob7jWEphEPBxiqJztriK6w5ymWoSt1Qg-Ja-z2kBqNrAuSyUpX7wJjEtKYCbycGMikaYIArA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6162afaa76.mp4?token=GbZx-vXeVAzxXqtAQJ2sdWvxYH4TuWIP7OB4umn0M-B2UENMPoB3InqvSy-K9r_I0O_bt-qjK_vKksqsVcsk9fjxS6OO8DI1grHA-uFlYg40nMuf6BnbFeiPLO2IAUx35FBRvphyJ8cknxLx_iNyPneJ4Ar6RgbLalk_L1Z-uvcV57G-6YAymOWxcpdsMaSNEUWuHrr1V8kqGPib9W9WFqGNyLocBf4bR2L3Lm5taPCsgMUtkTMJeMTNdoAZj2YDZBijy1cP0woSVFob7jWEphEPBxiqJztriK6w5ymWoSt1Qg-Ja-z2kBqNrAuSyUpX7wJjEtKYCbycGMikaYIArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش تشخیص کابل شارژر اورجینال از فیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/681774" target="_blank">📅 22:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681773">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
زخم اصلی اقتصاد
🔹
ما در میانه جنگ و تنش با آمریکا ایستاده‌ایم، جایی که اقتصاد ضعیف، می‌تواند به اندازه یک تهدید نظامی، امنیت یک کشور را به خطر بیندازد.
وقتی ارزش پول ملی زیر فشار است، تجارت دشوار می‌شود، هزینه تولید بالا می‌رود و سفره مردم کوچک‌تر می‌شود، دیگر نمی‌توان اقتصاد را با همان نسخه‌های دیروز اداره کرد.
🔹
اما زخم اصلی، عمیق‌تر از جنگ و تحریم است.
اقتصاد ایران سال‌هاست از بیماری مزمنی رنج می‌برد؛ دولتی که به‌جای داوری، خودش وارد بازی شده است.
فرقی نمی‌کند دولت، خود را عدالت‌خواه بنامد یا توسعه‌گرا، محافظه‌کار باشد یا مدعی بازار آزاد.
🔹
وقتی قدرت سیاسی از سیاست‌گذاری‌های کلان عبور می‌کند و به قیمت، تولید، تجارت، سرمایه‌گذاری و کوچک‌ترین تصمیم‌های اقتصادی دست می‌برد، حاصل اغلب یک چیز است؛ رقابت کمتر، رانت بیشتر و آزادی کمتر.
🔹
دولتی که به نام حمایت، قیمت تعیین می‌کند به نام عدالت، منابع توزیع می‌کند و به نام مدیریت، بازار را محدود می‌کند، دیر یا زود انگیزه تولید و سرمایه‌گذاری را فرسوده خواهد کرد.
🔹
در چنین اقتصادی، کارآفرین دیگر تمام فکرش معطوف به مشتری و نوآوری نیست، بخشی از ذهنش همیشه درگیر بخشنامه فردا، تغییر مقررات، مجوز، مالیات و تصمیم ناگهانی سیاست‌گذار است.
🔹
و درست همین‌جا، بخش خصوصی واقعی عقب می‌نشیند و جای خود را به انحصار، وابستگی و رانت می‌دهد. جایی که سود خصوصی می‌شود، اما هزینه‌اش بر دوش جامعه می‌افتد.
البته آزادی اقتصادی به معنای بی‌قانونی نیست. دولت باید قانون را حاکم کند، مالکیت را امن نگه دارد، امنیت ایجاد کند و با انحصار و فساد بجنگد.
🔹
اما مشکل از لحظه‌ای آغاز می‌شود که داور، خودش پیراهن بازیکن را به تن کند و بعد نتیجه مسابقه را هم تعیین کند.
🔹
رفاه با فرمان ساخته نمی‌شود با آزادی مبادله، رقابت، امنیت مالکیت و امکان خلق ارزش ساخته می‌شود.
🔹
شاید سؤال اصلی این نباشد که «کدام دولت بهتر اقتصاد را اداره می‌کند؟»
سؤال عمیق‌تر این است «چرا باید دولت تا این اندازه اقتصاد را اداره کند؟»
🔹
شاید برای نجات اقتصاد، پیش از آنکه چیزی به آن اضافه کنیم، باید دست از دخالت‌های اضافه برداریم.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/681773" target="_blank">📅 22:03 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681772">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-xZ8in2HVNPYX3JGuD4Ke53bhr9SYP11UNaHkqbdgnKOLzXC51Snhat4h_778VWq0kodT_E0ADEFNm7dRprXdWPgErlmOttHj2Szm2PG60UAq4-GXehEKGXeExZvW8FkPKXro5mtitGNx0h3EOi1z7qSLdzqfoNTmWhFaQB9VQcqZLW-uzEK7U3pcC1wj31K07mVrvGYf64uOdob3kArDJzZ3fSn5hQqxJXJhDTics7j3CZ2WJIWiV8k-4d9VUBOKdw50xn0i2uyrX5vhBIBvm4DFuvWMuuWgmY97FXhZrhPgFQBNbT_ATlGprE_GiajSCovOslZmrnUXL3fwsphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعضی رفتارها، آرام‌آرام فاصله می‌سازند؛ حتی میان نزدیک‌ترین آدم‌ها
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که خشمگین یا شرمنده‌کردنِ دیگران می‌تواند رشته‌ محبت و صمیمیت را سست کند. رابطه‌ها فقط با حضور حفظ نمی‌شوند؛ احترام، ملاحظه و حفظ حرمت آدم‌هاست…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/681772" target="_blank">📅 22:02 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
