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
<img src="https://cdn1.telesco.pe/file/GWK2IRUXOrwAyR_lpgRwq1nUOOvMxm6UIG_WGIZMA-A3wNDfmLEAQCa5ZdQvhZ7dln3U63GBezknmdNgmLPLAWWx_UGP59WsRmSE44YO9s7O6fiLKmyBT2jQ-SwvQv-3Hp9hYkpyAzlJi1ku-KXc5jdAudCL6eLjOxFVHBAcFoX9NEYq-Gt_ZRuyjHKbXbFASy3bL4uwgY_aFxTXg2eSJN6NAzDZrTgqnHTYyrqFw5cXFovSZe-V2FSYjC_rbkBVUhdQETuUpYSQp7QofhMsjTOAF6PxSGoLTuwfVKumd1SC8zdszt3oXLkwdhmDNnQ0RcNi148nEY6cVGNy7VI40Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 93.1K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 16:50:58</div>
<hr>

<div class="tg-post" id="msg-2318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V7J-8IYL8pfVPi5EeT4L0aNieIPsAjSnXG0qAYFFb-8caKdRXTmvv7qPM2zWhebyaHjDdwvhhJwmTie1faBFyGI3kv0qZdllkhBzSA34OvAjAMGjvYMgB7cyQoJ76mCaN2lOZe3XOWdT26aVDRP_7gEikRLTQmFOowuII1fqYeaF3VNoZj1aNkSqKV_ubfnMm24aCfaM8_Ccnk9MlcaH4yIy53hT7tpw_fmKT2g1uCXyi3kNIU7Hjvs0f89lGNzXvnRH1cdto9TPqTN4Ba8yuKwEsyU_X0ANjU3LQVU-vb_LhA6-AP2GVUzypGUd8AVjOEaqvvr4Bqy77PJFMZ1dwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
👉
github.com/MaxiFan/TunnelX/releases/latest
💡
t.me/PersianGithubMirror/4816
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/ircfspace/2318" target="_blank">📅 16:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2316">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jDjQhHoWgKM2QNVrZ8QY4whLgSSxyTenGofABpkQHek9vc5aA-R_0jm4d9U3krXjEoHeZVof56hgz6lmamrE8SGbnOPnH-LfKHzoGjnB0nPL-ClE2py0kgbJjhQ9DPbI8aENgme87CzPyjWnoOuQGMBLF8Qi2aRbYUknpptvyEkiG4XPu7Sw0UigiV-bwPst5as1avsoxz59EbJa703kvQWPR-xzE478-cwVzjmI7Cn2c0-9CYFeJtptVju1KVOhMyIBdbqvllxkQO-R9Y-0LMVTqRnLGWeZs4r8g6dpI-WQo6SKSs8l0cOeR47xjZ1Pgsx5ykap3BFjgF5Ph2Km1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام "اینترنت پرو" را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/ircfspace/2316" target="_blank">📅 10:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jo_dO6ExvUqnbs-29BGnArHRwJOlVFsD-Mv2dP4XW9BRFzAitZt0O4yNy8B1JJJH-u4QS4prChN9X-Ax6Tyl4vxhD1mb_y1GTgq0rObLeESJmcG0jsHHHbpgmfP5wOGeKtktzifSarBTDOeD7aoBoxIIWmRdyWeOpyhsk-XlvVsw-HVqJQ-xmmvIU5HVYWKxDBm9EvPLOGJ6WC5u-doRIpCTq-Lr3INOeBU2M3thhTZB9Pekwk6cnuwl3vh7XJMMt90u8HtGLJ6GAgASspvB-sgMJ0znAnju8P84PdaxLH24t5JaCCZquWHByQDA-BGZKyl3l1oBQWum8GInv_ycsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در روز ۷۴م از قطع سراسری اینترنت هستیم.
وزیر قطع‌ارتباطات گفته "در تلاش برای برقراری اینترنت بین‌الملل در اسرع وقت هستیم".
نتیجه عملکرد و تلاش ۷۴ روز اخیر این فرد از خروجی عملکرد یه مترسک داخل مزرعه هم کمتر بوده و جالبه با اینکه از بی‌خاصیتی خودش آگاهه، حتی بصورت نمادین دست به استعفا نزده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/ircfspace/2315" target="_blank">📅 08:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2314">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B3O2fBqiw9QBfdtyM5rc6GkQC1e2mZkMUjU6Rzzrv-i9qS8tjOcXY9XuggsndvtFGeOZg6oeLySehx7_f_ySwYUMPXFjA_hEm71fHk4dCV6y8H9nYLQz5sQfgJhoSAMi1ZcO1CVkkWmNSUunxEh_gTEP43FzLXVpFxRxCWj6xhhhy6i1l9hFvFPlpN0tf-5t1-oKs5QkM2eGsCIkiDmyNo7MB2UmHnHX17hwsIc5tSJiBXGRmmtmRiUOVMR7q2oGhmAo8K1WE4BmM6yeKKtwwkLU9oMT-UiLQWOjW8Erg7BKN2W8ehW-fEKmleT6OieT1-Bt9y_K8Km-VCZ8b5or7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روندی که نشان می‌دهد تصمیم‌گیری درباره اینترنت و سطح دسترسی کاربران عملاً از دولت خارج شده، وزیر بهداشت برای رفع محدودیت دسترسی به پایگاه علمی «پاب‌مد» مستقیماً به رئیس مرکز ملی فضای مجازی نامه نوشت؛ اقدامی که بار دیگر نقش کمرنگ وزارت ارتباطات در سیاست‌گذاری اینترنت را پررنگ کرده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/ircfspace/2314" target="_blank">📅 08:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2312">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KtEE-uxpJdNCbsFAwA5BY-CGHTNSn5L8ceDL-wlF-jc-X_NmPyGU7p3NmXSM33lFRLNYzR4Pq-LGIZBcNStMqo4li1oew0bLe8pyScS0QduOqTMiXUBCC_HogovYNEimUsJdgt9ZQ3y96n5SBbN2UnpcgDHSQ1ysiYxboHWxFJIUt464104sTveI1TsbYChf3ckCpB9_FYXyL9MGB4trjslKQ5YCy4q5pfzeXzcvzGRh_RJhAR-fxGPQt2zwzCutA9a8ghXxXURRxASImw1a25K-ogaqvXE-1k_AvEQWIGcQQex-Z2etSqg8KZ3Z7vbpw2QCYqmCbtpDbVHjcILF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت AIO Downloader یه ابزار متن‌باز و کاربردی برای دانلود فایل و محتوا از سرویس‌هایی مثل یوتیوب، گیت‌هاب، اینستاگرام، ایکس، تلگرام، گوگل‌پلی، تیک‌تاک، پینترست، ساندکلود و ... هست، که فرایند دانلود رو از طریق GitHub Actions انجام میده.
این ابزار طوری طراحی شده که در شرایط محدودیت شدید اینترنت و وایت‌لیست فعلی بتونه بسیاری از فایل‌ها و لینک‌ها رو دریافت کنه، بدون اینکه نیاز باشه سیستم یا سرور شخصی برای دانلود داشته باشین.
با توجه به اینکه این پروژه به GitHub Actions متکیه، بهتره برای استفاده ازش از اکانت اصلی گیت‌هاب استفاده نکنین و ترجیحاً یک اکانت جداگانه بسازین.
👉
github.com/ProAlit/aio-downloader
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/ircfspace/2312" target="_blank">📅 08:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2311">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aaCUzaGiIz19c4VD1pmVSGWSiu9WwlGz6SLhNrZ5e2oh7EhtUzN_eelRzMhVGIibxmjWvSD-f-d8lX3x6G8gHlty2IMThofOjILt-PBuiWx1ZKJan7l9ScG036uxDkFhVbN1a_4uWAcxvy01ublw5CwtCwV-IkZ23jY1e2jiLqfKt5huZ9F6KjOS7NaaLNEQ3vV_ICUbxw4TPqGnMjSEFUto_-krykWEVp82oY3t-p0u_tQuwAsRe6n4Pnd2doPdoZN7R81FT9fIHdh93wFczicqFjdOq99h_aUTroFoXUUp3mHVsSHUtMVd5T1dUUYWHAiUQpalyL9DdbmBC2x_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پیامرسان_بومی
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2311" target="_blank">📅 21:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2310">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/olnx2j-f1lXMFLRXjS-5rOLEZtZ7J34Dt-7I7WczSJfl-nXpfC9tmYuvqZEpxaZOF_yGrxoG7DIa1-tB_VEaeGsSNzFyzpG_3zKCWjXieWGXn0klw9vhhML1N_a0Iq4saX1MDNMjPjWLFaDIvpJ1L_qkX0qSva1u5pab9lkZeoqDyFqwGOhWRaWUaPvhe2kaUvX1lnl80lMHKU-O95n1NArdaP8PthMgP39cZFl9qjUotS-09bQ8lMk-5Dy9pRMeqqs5W2iosV0Ac4GFr0MyfmHWyWYEnhNQLCycqfbm0L7s5aXcANiiEEpkfhNRgTl72rUUzQi1pX1LzIXF47kPxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه رودربایستی رو کنار گذاشتن و بدون ثبت‌نام و بدون احرازهویت، بابت پیوستن به پویش جان‌فدا ازت تقدیر میکنن
😁
کی به کیه؛ اگر آمارش به ۳۰۰ میلیون برسه هم تعجب نمی‌کنم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2310" target="_blank">📅 21:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2309">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تا الان توی هیچ پستی نگفتم که به پروژه‌هام دونیت کنین، چون حس خوبی به مطرح کردنش نداشتم؛ ولی شرایط همینطور پیش بره احتمالا سر چهارراه نشسته باشم
😂
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2309" target="_blank">📅 21:25 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2308">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قبل از شروع جنگ و قطعی اینترنت درخواست فیبر نوری دادم و حالا اومدن نصب و فعالش کردن.
با تشکر از شاتل بابت سرویس خوبشون؛ در واقع قبل از نصب اینترنت نداشتم، ولی الان با سرعت خیلی بیشتری اینترنت ندارم.
©
itsmralii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2308" target="_blank">📅 11:45 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2307">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/egcAqcGiIFCC8SHQerlGmjxjZWOtw0-J9lgFq6DZoX3jC55uvPkqIyI1kwwdX5cbIMngK5KzVH2J1yNekN3SRzhg1qEdg3Knhg35_rccrl48AmRT1SxU1d5rjiTuJxpy-wQqS8_k5WY358WCBOle2z9lXW_0nKTCNr7UiSzMZXjysOCdF4h1kJgiuXHtxs7dC2-3-eq04hc3MDaVeAFEyiQ9drbOydAteRWV1OMax1S6RzyqY6Djd9J1_MP8Kk3O1lqfOpgywJj9cv15YK306FdlPsWKvSj1GvRiVt1jOqulmALWpTaB66LrrlBizhRS3Q3NMbvBC6TLgUPl9mDXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور از وزیر ارتباطات بابت هیچ و پوچ قدردانی میکنه، بعدش همون وزیر از رئیس‌جمهور قدردانی میکنه، بعدترش همین بدردنخورها دسته‌جمعی از مردم قدردانی میکنن؛ اما تهش می‌بینی ۷۳ روزه که اینترنت قطع هست!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2307" target="_blank">📅 08:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2306">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KwyR_6Iut1dDWdwOo2fap1avv9OHsv4LV1oGE4XjmHbylWFsGiVY3lE2jTixjcAVPAQutSdoicplWllUQ-D7VoNhVBOdMNhlaCS8UxIb3J_9IUFHxKqRtENcCR4dZjLLAHt7YAgL5IH8GAC1VirctteSI8xYA80g5R8Q9Rm_hkLmA_18Yo5y1KUtX-zm5hS-up4uqyoblZmS2wshsU-bMQ2Ohs_XzjJzNEu1x7giKFtqROWxrd_WSu8TXKRBNO99xnZtegOcWqZRabkbBiOIzkNkmrpTJq1xKETv55qgfhj19aLeNDU8KA10FuS-jb77rwpElVj1NNV2HV0TYykVAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteDNS یک کلاینت متن‌باز و رایگان برای اندرویده، که امکان اتصال از طریق DNS Tunnel رو با دو حالت Proxy و VPN فراهم می‌کنه. این برنامه با تکیه بر MasterDNS و StormDNS طراحی شده و میتونه بدون نیاز به تنظیمات پیچیده، ارتباط رو از طریق تانل DNS برقرار کنه.
👉
github.com/iampedii/WhiteDNS/releases/latest
💡
t.me/PersianGithubMirror/4637
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2306" target="_blank">📅 16:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2304">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MEmk5NBEN0iSkn0yUD1oPEgCkV1tsBklKx1j5z5eSLOzcucQD6DF1utpJ9a-BpEq0ChU7d3oGlEVXExbuLsPrUsyZG7dEJBUuNV7rB3kXarxFMpHXspbJDSeW9j5uk4SGcXFRFIMKyVu35A9fkX9G__Lc2Ga0U3JBwZCzHEDcFGpDHpCVzpniCo2-CAcbKQIoXnEv1hul65_mlocc7yR3GRla3bdPUMVcEkoFYcVSjRGydc3nFbMKdmPf-Q22Nr96pObC09vDwn9I_zDRCsiu5nJo1k1W324dWG09CpcZi5SRMUjvj36i8DDHwdLEaEo-PIT9y0GCqPBVQcyiNVy2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز که نت‌بلاکس عدد روزهای قطع سراسری اینترنت در ایران رو اعلام می‌کنه، یه عده میگن "خب شمردن که کاری نداره، خودمونم بلدیم".
ولی مسئله فقط شمردن نیست؛ مسئله اینه که نباید این قضیه عادی‌سازی و فراموش بشه. اگر فکر می‌کنیم راه مؤثرتری برای اثرگذاری وجود داره، خوبه؛ ولی سوال اینجاست که چرا تماشا می‌کنیم؟
۷۲ روز گذشته و هیچ اقدام جدی‌ای برای کمک جهت اتصال آزاد به اینترنت انجام نشده، کسب‌وکارها نابود شدن، آدم‌ها شغلشون رو از دست دادن و سفره خیلی از خانواده‌ها کوچیک‌تر شده. مردم برای یک اتصال معمولی باید میلیون‌ها تومان از جیب خودشون هزینه کنن و در عین حال بخش بزرگی از نهادها و جوامع حقوق بشری نسبت به تداوم قطع اینترنت، سرکوب، دستگیری‌ها و اعدام‌ها سکوت رو ترجیح میدن.
در فضایی که همه‌چیز خیلی سریع به حاشیه میره، استمرار در اطلاع‌رسانی خودش یک کار مهمه و همین گزارش‌های روزانه امثال نت‌بلاکس حداقل باعث میشه موضوع قطع اینترنت در ایران کامل از توجه‌ها خارج نشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2304" target="_blank">📅 12:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2303">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این هفت کابل اینترنت جهانی در خلیج فارس رو اگه قطع کنید خیلی خوبه، اونا هم مثل ما اینترنت نداشته باشن، بلکه دکان‌های حقوق حشری صداشون برای اونا دربیاد و یه نگاهی هم اینور بندازن و دل ما هم خنک بشه!
قطع کنید.
©
ehsan_369
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2303" target="_blank">📅 12:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2302">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qlDyKLkr8Y98ABW5kwpz7mU8N_PdzDErvXpK0wgNblcQbYONbq_RLkDkXjSnmUzyEX6gjCyJ2aI6zbgR2DpMjlD4O1bU1jqqri9qx-9qPuRlwN1k1Q40ovesI3TPQ8gaMxtLmDj5ROMwROwVMzJRNyz2a22Ji7uiVbQYjIjcGdAUSXzMRnPLO7iNJH3SywADzW1jEAZX2ZGBili31vt1bnfsMGHWs0b98AUv4DQo3tq5Ynxeyge9sXOa14Zr6TjaAqzs4h-ehLx_XcjUOnKvn82Ci4CFz2r9cbvuGJl2QytR6jtANntoXLJrInoX0SIh85IspIO66-9MaV5uhjtt_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسنیم نوشته تنگه هرمز فقط مسیر نفت و کشتی نیست؛ بخش بزرگی از اینترنت و تبادلات مالی دنیا هم از کابل‌های زیردریا رد میشه، که از اونجا عبور می‌کنن. پیشنهاد داده ایران از این مسیر پول و کنترل بیشتری بگیره؛ یعنی برای عبور کابل‌ها مجوز و هزینه تعیین بشه، شرکت‌های بزرگی مثل متا و مایکروسافت مجبور بشن تحت قوانین ایران کار کنن و تعمیر کابل‌ها هم فقط دست شرکت‌های داخلی باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/ircfspace/2302" target="_blank">📅 12:17 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2301">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lVr_mgbWrWy0kzgKEK-HmYRBkreN4DDAIQzpYP2uyPMmjLMSEKthYc2CCO2dnin2ZoKaXa_Z72Npbx5uhbA6mLd1I_XbsyxzA7uYySLPDCnJKy9D74cBHL6kwa7KcLt5WBjLy-fWeynpFHKj8GDZYVwSmBLBuSaEd_aGEgijgBM-321qSWLhj8_vCd1HypRwsV92TsdaNt12HinutQg23fvdswhKxZIK1EFhtVTIFWfdPCc07gAIJZ3CCymACrZTYrxn259e5bx_TUimjhMtb3gwmcmTsmIP_vuxh6qOtlxCyQ4jpwQ6k8VGXW9mp4fOIumNkfNBaRuNO7Z0OmF7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع سراسری اینترنت در ایران وارد هفتادودومین روز خود شده و هیچ نشانه‌ای از بازگشت گسترده اینترنت دیده نمی‌شود.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/ircfspace/2301" target="_blank">📅 12:07 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2300">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cq3NxIaXPK09r3UfmOdDuuFqL0ToSqQ_mP9fPSOjYBeSzDYP2HNCn8V70BDTbkGj68HuEziP2PwbKHdGjEn2Gm4Fagg6dp_9VP7XmAa5IFA8724Nbplxpq2X6B2sb_IPboiXV7NOl2p115ZpPBYJgj4AJbmENV83RIphWxStSTsBQb_rgw9o2-LYsG0INYV8BOLGdhRuRw5Ou7nACeSad6goUecWFGkEc-IghZjcMzkHjjXDZxLr9GmNp2aIWo4X9TLQ0O75t4cCMRR9L0v3hMzzUD_2_ySXQ9lKMmsAsII6nyo51RVkWFs6vd-w5lJQtkd-oFoFmyQbJAV6nMBdIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۳ از اپ متن‌باز و رایگان TeleMirror برای "دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت" برای ویندوز، لینوکس و مک منتشر شد.
در این نسخه نمایش پست‌ها بهینه‌تر شده و مشکلات مربوط به کش تا حد زیادی برطرف شده، بخش تنظیمات به برنامه اضافه شده و امکان بازگشت به تنظیمات پیشفرض فراهم اومده. لیست کانال‌های پیشفرض افزایش پیدا کرده و علاوه بر نسخه Lite، یک حالت Normal اضافه شده که تلاش می‌کنه در صورت امکان تصاویر فیلترشده رو هم نمایش بده.
این برنامه فیلترشکن نیست و بر پایه دسترسی‌های فعلی وایت‌لیست اینترنت عمل می‌کنه، بنابراین ممکنه روی برخی از اینترنت‌ها قابل استفاده نباشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4599
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2300" target="_blank">📅 18:57 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2299">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">افغانستان تست خدمات اینترنت 5G رو در کابل استارت زده، عراق تلگرام رو رفع فیلتر کرده؛ اما جمهوری اسلامی تا دقیقه ۹۰ درحال آزار و اذیت میلیون‌ها ایرانیه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2299" target="_blank">📅 17:52 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2298">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGo1DGhYSBI4iZPACBbhJTtcPb12WSNkEpae2baEMsCCbv4GQx_2zruxOeiH6PlIQN4qMlbrGIiP9PvN3MpNvOOf07Tosgvhwcf6eSw4mP6ySnKSwA8I8KOt-TQ_KCd4PodR5ob8K9h7-OV2tmvSpP8M7HdkmQ-CbCT66AGxf8fv3_TglABhdtNQocjOMZwrvNgcNMj3Q9QkTvrsppDwAzGejlrKrRmcVRED3i5OmA49gD5Qvykn8pPj7-ECOhtNrQChY2pmHZWjnTmMnxQSFZM1eQb66Kca8FduEca4DPIsZgYgLqh4sV1FdiKaPt_AcMPDzL24GViaN54hIRpYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی خاک بر سرتون (پیامرسان‌های بومی) که با اینهمه حمایت و در میدانی بدون رقیبِ جدی هم عرضه ندارین کیفیت خدمات دهی، پشتیبانی و توان زیرساختیتون رو ارتقا بدین و بعداز اینهمه سال سابقه، آدم نمیتونه ۸ مگ فیلم ارسال کنه.
بعد از خودروسازی، باید شماها رو هم دومین فرزند لوس و بی‌خاصیت کسب و کارهای داخلی دونست!
©
kamran_falahati
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2298" target="_blank">📅 17:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2297">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جمهوری اسلامی ۷۱ روز هست که اینترنت رو به روی مردم خودش بسته!
روح‌الله مومن‌نسب (تئوریسین بارداری با ۲ گیگ اینترنت) گفته شرایط اینترنت به هیچ وجه نباید به روال گذشته برگرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2297" target="_blank">📅 17:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2296">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fic7PmbI4KuS9YrwB2S8r6CkiNb10O714uMp9L0YaJdBo9Da2ZsVqXbauYjds21p-6LPdWH1FbSOZedehUNdSuMEFl_ql2glJeHVd9TTLzaNkaa31Am5pB6VUt-lliwMaUK0rUBviOU0QGeuQZa__xYH9vi-WLSGgUaMNhgMMzNMeckGU1JGDne-Pq8GbR7RE2GMGxhBj6COhGgNMvvdwh-sScQn1EF36_erVb3kGbl33XsBgbByMwloJeXf9gCW8ZGr1DvRHssLjC8GS_LZVmxcS_TXABhi-00BM2iklYnSgucVUaV-fszo2ltPLAF6PAcFHMe8FUF72QdBSK_SDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ متن‌باز و رایگان Pigeon یه فورک از پروژه تله‌میرور برای macOS هست، که از طریق اون میشه بدون نیاز به فیلترشکن یا لاگین در حساب، به محتوای کانال‌های عمومی تلگرام دسترسی پیدا کرد.
👉
github.com/MaroMushii/Pigeon/releases/latest
💡
t.me/PersianGithubMirror/4500
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2296" target="_blank">📅 17:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2295">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ibs0i6sgqBEPLPn9FZYXAynyyCDDzKGyS9y1HI4CHo1liTW9P0EotcVUHGo41SniTCmR71j_80PGW4mwkX8UWe9D9DGYdBY7wAjSXpImJQh5L1KVzi2hlv-uaynj7vvOapDPhAjumhWahksf7xok8zBdDITzZvty467X3B87aFxodwYt5ocG7K8jvHsFkvEDFOt7UVPI_WJgiDuQAEARY_7cKugJDqBHXag8pskx_r1dXzdiIIKK3tQn-_DknuNGq18bg1wP3RnEH8YiRROPgG59Jfq3ngexoud01A7MwWi35XPwv23qsEy898M5kM8QfzFzCULvwoGHI7lUsSsHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Youtube Sandbox با استفاده از GitHub Actions بهمون اجازه میده که فقط با ارسال لینک یوتیوب توی کامیت‌مسیج، فایل ویدیوی موردنظرمون رو توی فولدر Downloads (داخل مخزن) ذخیره کنیم.
👉
github.com/iphoenixon/youtube-sandbox
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2295" target="_blank">📅 17:36 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2294">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xc_w8zYlfaDvRv8WxWn1DHcojpRA6f1rTFnCjRH2q2Qq5omtUionakLlLAszTIwLiEnwlDcCFd8X_GXGpI-Hz7_VZAVzMdfWkRRZaGrL8o37ofN5MJ_3nptdO3T5F8BiastUlDQYpZNPbA7x7_gt8wolvtuzDSbXznYzGG0Tanz0i7no7uYxJc7WNyi3Y3Ba_ufkXPhFWy0Oi6mpBOGUSsy3FM9u1ipQoxlq864x3RctcqnnIx11mR_X48Cno-KEI5BPCSsd1OmtHZ2dZ47IVa3rmhe_EyHjoksKEKt3U4Psekgdd7PTgg8zMTEUhMNnTXWqm4PB9S_WNLCCA4RdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه گوگل براتون باز میشه و در وایت‌لیست اینترنتتون قرار داره، می‌تونین خیلی راحت با نصب این کلاینت اپن‌سورس به گوگل درایو در اندروید دسترسی داشته باشین.
👉
github.com/aleskxyz/Round-Sync/releases/latest
💡
t.me/PersianGithubMirror/4489
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2294" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2293">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jVqix4ueFxSNCQpAiIMNqThETK1I5IHQn0cUifLLuE_6pwAouuDkQNGgrOODf7RkD08fHVl4rDWWOX69McklxRUUfiO_oWLwuW3OVV_jLkKcAzLUhJXv8DTGxkS7rNNs8IRk7NxeFLJFmzXbKxDkCEUo8fu5OXYNbP69fs0EA8h-n59aQZYZQFRL7rSIun9SAlbpSkFeqXjrXHDGAkrgskNKuThxOvkF2efwtW6XtKMSVzayf5s2M0OSH6qTWtnMqoEp8LSemgRxUMf_ee1aCmGA9G5iCxb6HWT5lQlU7xxLOUyZPpipNZLNuv7ByDB8-gNbtI3t2a4ZVGlRxFRQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید کلاینت ZedSecure از طریق گوگل‌پلی در دسترس قرار گرفت.
در بروزرسانی جدید این‌برنامه پشتیبانی از پروتکل DNSTT اضافه شده، هسته ایکس‌ری رو بروزرسانی کردن، بخش تنظیمات تکمیل‌تر شده و یک‌سری از مشکلات برطرف شدن.
👉
play.google.com/store/apps/details?id=com.zedsecure.vpn
💡
t.me/PersianGithubMirror/4496
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2293" target="_blank">📅 17:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2292">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۷۰ روز است که جمهوری اسلامی با قطع سراسری اینترنت، میلیون‌ها انسان را عملاً گروگان گرفته است.
این یک اختلال اینترنتی نیست؛ حمله‌ای مستقیم به زندگی مردم است. کسب‌وکارها نابود شده‌اند، معیشت خانواده‌ها آسیب دیده و ارتباط مردم با جهان قطع شده است.
در سایه همین خاموشی، بازداشت، سرکوب و اعدام ادامه دارد؛ بی‌آنکه صدای قربانیان شنیده شود.
اما بخش بزرگی از جامعه جهانی همچنان ترجیح می‌دهد چشمش را بر این فجایع ببندد؛ چون واکنش نشان دادن هزینه دارد و سکوت، ساده‌تر است.
For 70 days, the Islamic Republic has effectively held millions of people hostage through a nationwide internet shutdown.
This is not an internet disruption; it is a direct attack on people’s lives. Businesses have been destroyed, families’ livelihoods have been harmed, and people’s connection to the world has been cut off.
Under the cover of this blackout, arrests, repression, and executions continue while the voices of the victims go unheard.
Yet a large part of the international community still chooses to turn a blind eye to these atrocities, because taking a stand comes with a cost — and silence is easier.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2292" target="_blank">📅 16:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2291">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قطع طولانی اینترنت تحقیر اکثریت بزرگی از افراد کشور، یک‌جا و باهم است. اما این بین، گروهی که شغلشان به‌هرشکل به اینترنت وابسته است، تحقیری عمیقتر و نفس‌گیرتر را تجربه می‌کنند. با آن‌ها طوری رفتار شده که گویا شغلشان "مهم" نيست. حرمت ندارند و می‌شود با زندگی‌، زحمات، اهداف، آینده و برنامه‌هایشان بازی کرد.
©
DevYara
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2291" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2289">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بر اساس گزارش جاب‌ویژن با عنوان "تاثیر جنگ بر بازار کار"، محدودیت در دسترسی به ابزارهای اینترنتی موجب اختلال یا کاهش فعالیت در بخش قابل توجهی از گروه‌های شغلی وابسته به اینترنت شده و بیشترین کاهش فرصت‌های شغلی در گروه شغلی دیجیتال مارکتینگ و سئو (۸۳ درصد)، طراحی گرافیک (۸۲ درصد) و ترجمه و تولید محتوا (۷۹ درصد) ثبت شده است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2289" target="_blank">📅 12:07 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2288">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FsfNnuyky_a5U0xMdDc3Ge4pD8iWUM_lwIt7obWMLwOcgCTAWWr7I1mhfkIy5dY8miMLw8JRfhwr50E1C0IL5z1Mq97X9jJOh_4bYbyVIqduttpdott6aeRRH8qWAR5ijwZzJH6Oi3d3e8dMzvq-rEezNaboHD9uT1Oi_I4fjhcb0HmTgqqNbnK-wPwc61DFlWiUL2YYE5qDlBwy-wmvMW4BlccWKgd913eix2-UMNjoboogtPAIyw8eZF7clyHzGdU3M22Y9JgFm-BDN5HLoA-dRX8DmgFPt6g37lCpSwzUbdn_rRxq9vhWgP18oSj0u25yWoHPsRekKYR8fG95QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی شاکی است که چرا با وجود اینکه که پول داده، تیک آبی اکانتش حذف شده و ...
در همین حال میلیون‌ها ایرانی پول اینترنت دادند، اما بیش از دو ماه است که یک شبکه داخلی که فاصله زیادی با مفهوم اینترنت دارد بهشون تحویل داده میشه و از دسترسی به هزاران سایت و سرویس محروم شدند. سانسور اینه!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2288" target="_blank">📅 12:02 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2287">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وحید فرید، کارشناس اینترنت گفت: ما تجربه قطعی اینترنت را در دولت‌هایی داشتیم که به ظاهر حامی اینترنت بودند. خود پروژه شبکه ملی اطلاعات یک قدم به سمت ناامنی دیجیتال است. کسب‌وکاری که اینترنت می‌گیرد از نظر مردم رانتی است و روی حقوق مردم پا گذاشته. حاکمیت با قطع اینترنت به جامعه سیگنال ناامنی می‌دهد. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2287" target="_blank">📅 11:58 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2286">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سمیه توحیدلو، عضو انجمن جامعه‌شناسی ایران، قطع اینترنت را از منظر اجتماعی خطرناک توصیف کرد و گفت: در زمینه قطع اینترنت حاکمیت هزینه-فایده انجام نداده و متوجه نیست چه میزان خشم تولید می‌کند. آنچه در این وضعیت تشدید می‌شود، شکاف دیجیتال و محرومیت نسبی و شکاف حاکمیت-ملت است. /کارزار
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2286" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgzJ88VwMGV--gA8IypGjhU58IcjoxObDDhWKUeGfB9xck8d032XOUyhI7I4bxaOHEPLUQFDQt5j6yY8C2UUymA0hB6gXana8vSkIyxRPajMmusZcLp2jZ62nmxUeJTKl6AQYySEKWB8I3dFeYnsjpeeuIPYX4QFYjesJKZBqWbBeSqLQDUUBdGoSNKurNzMsDIfO7FSv4NowYe_6lCyBUZ7-ue9BYegpnW6hZRQyd0AM8nXfLj3eypAR0RZSO2zRhvv3UCPzLRDoO-5AKz28NlLjNLb-ISG_kwiAs8Aochcon4PJezI1Ak6nSZYVb6RvSl-sRG8RYvbfu0QdAUooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شرایط فعلی اینترنت ایران که روش‌های عمومی دورزدن فیلترینگ عملاً کارایی ندارن و اسکمرها و کلاهبردارها زیاد شدن، مدتیه یه مارکت‌پلیس برای خرید و فروش کانفیگ راه‌اندازی شده تا خریدارها و فروشنده‌ها در یک بستر متمرکز و نسبتا شفاف با هم ارتباط بگیرن.
طبق توضیح تیم دیفیکس، خودشون فروشنده نیستن و تمرکزشون همچنان روی ارائه و توسعه سرویس رایگانه. این بخش صرفاً برای وصل کردن فروشنده‌ها و خریدارها از طریق این فیلترشکن و حذف واسطه‌ها ایجاد شده و فعلاً هم برای تراکنش‌های رمزارزی مرتبط با ایران کارمزدی دریافت نمیشه.
در این سیستم، مبلغ پرداختی نگه داشته میشه و برای مدتی بعد از تحویل آزاد میشه، کاربران میتونن به فروشنده‌ها امتیاز بدن و تجربشون رو ثبت کنن و کانفیگ‌ها هم بصورت رمزنگاری‌شده تحویل داده میشن. البته محدودیت‌ها خرید بصورت رمزارز رو دشوار کرده، اما افراد خارج از کشور میتونن برای خانواده یا آشنایانشون داخل ایران خرید انجام بدن و فایل کانفیگ رو براشون بفرستن.
👉
market.defyxvpn.com
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2285" target="_blank">📅 11:26 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2284">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=HlQg6u7feQ9sDg-SorvEHH76_SsIFwuzFvIHQNAsRRdLLxSzP1ol_myTNc-GfExDpQT006Bm90tv2nRhqPvH09CFsSqUj_rUStHtDuv8TGqqSv5kmhkdEgSkVhhnjnLPHqLe9iUliNT5rrt8E_41evArKrcarJNZVVzUY7JxrFXs-vdMOqGUDCXdjClM7RXFIEGkih0HIRdy0LVLjE09WG4s1KC-ctxc8HTSFw9Xl7xLaUSAbpUw_2bgQU_NwNfx7S5EBUl2M6us2bcmRXXGTiq6uwooJrCfEctq6JfPRcdMpcZBZpMFVOzYT6DBXTooujw4sqOaxORr6VfqR_oDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8db45e7.mp4?token=HlQg6u7feQ9sDg-SorvEHH76_SsIFwuzFvIHQNAsRRdLLxSzP1ol_myTNc-GfExDpQT006Bm90tv2nRhqPvH09CFsSqUj_rUStHtDuv8TGqqSv5kmhkdEgSkVhhnjnLPHqLe9iUliNT5rrt8E_41evArKrcarJNZVVzUY7JxrFXs-vdMOqGUDCXdjClM7RXFIEGkih0HIRdy0LVLjE09WG4s1KC-ctxc8HTSFw9Xl7xLaUSAbpUw_2bgQU_NwNfx7S5EBUl2M6us2bcmRXXGTiq6uwooJrCfEctq6JfPRcdMpcZBZpMFVOzYT6DBXTooujw4sqOaxORr6VfqR_oDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبقه اشراف و طبقه رعایا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2284" target="_blank">📅 11:01 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وارد روز شصت‌ونهم شدیم. میلیون‌ها نفر رو با قطع سراسری اینترنت گروگان گرفتن و بازداشت‌ها و اعدام‌ها در سایه خاموشی دیجیتال ادامه داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2283" target="_blank">📅 08:16 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/So9xGQU6VrU-wDZITiCkmiL4E271xtzUML0Kb5VG4KW-hXJvWzxv1rbYqRYiwz-FUFKCdov5QqrYau4ccppLe-XuiOQkni_OKGMfK1xCFHDC8yGOYzz_OfHFXb4kPvsDDwa9Gbnf1qO_GUsbdtrc9-X6h0aTJ-tomrbMNrvUV_Di3njfuzg8U3xzacxdzRifyKGOJcKkPcclZ8R7SCIlv2LWG4szi8V_he47cBRxLPDF64XFMw03_wuQAIk8oJ80QHOFPt77p9Y6FGuHa-uiGWnjr1GWHBT0CumnVSuor9yf4FsAWu9HSKg4enk2uJZeuFPkMEgeawY2sGPI4-1KHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از اپ theFeed امکان فراخوانی محتوای کانال‌های عمومی دلخواه فراهم شده و پشتیبانی از اندرویدهای قدیمی‌تر، حل مشکل رندر نکردن نظرسنجی‌ها و ...، بخشی از تغییرات جدید هستن.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/4273
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2282" target="_blank">📅 18:20 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/upiX33bnDc09lpEssEl5Kh7uGfL2OY-R2F0bNBMy2LDNQSZBAZkjhOi9FuS2uNGmlUBTi2dgOoYluMWsbZodCooRydMvXTJzt7ucIL-WHCkpxVRzywfMyqIs6XzG40_qLJqDRibXvDAg-c1QE7ULBCnvxFRy-lAhxxyLlu1Ozv6hF_Low99bttvHkgEaLM5qKdQw5Xj3OBih75lR7l7jfb_gtXwvRbXKQeHpq02fa168ngp3sXSNbBBr5A2nQM2X7N037DHa7SwMShRDo_6PVQXgDU33KLv2TPAhS4-z2JwV-VbODsFW7As6-a6YbsLm6-BXpb0ytR1VzRLsZiLbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای آسیب پذیری اخیر کرنل (
Copy Fail
) فارغ از اینکه آسیب پذیر هستید یا نه، آپدیت کردید یا نه و کدوم لینوکس و چه ورژنی هستید، همین دوتا دستور رو واسه محکم کاری بزنید و تمام:
echo "install algif_aead /bin/false" > /etc/modprobe.d/disable-algif.conf
rmmod algif_aead 2>/dev/null
ریبوت لازم نداره، ضرری هم نداره؛ چون به صورت معمول شما به این ماژول کرنل نیازی ندارید.
©
tiosus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2281" target="_blank">📅 18:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قطع اینترنت به بهانه امنیت ادعای مزخرفی است.
پشت پرده اینترنت پرو و سود حاصل از این رانت در جیب “ستاداجرایی فرمان امام” و “بنیاد تعاون سپاه” می‌رود.
حدود ۹۰٪ سهام همراه اول در اختیار شرکت مخابرات ایران است و مهم‌ترین سهام‌دار مخابرات هم “کنسرسیوم اعتماد مبین” است. این کنسرسیوم متشکل از “گروه توسعه اقتصادی تدبیر” وابسته به ستاد اجرایی فرمان امام و “شرکت سرمایه‌گذاری مهر اقتصاد ایرانیان” وابسته بنیاد تعاون سپاه است.
در واقع گردانندگان اصلی این مجموعه و به نوعی مخابرات و همراه اول دو نهاد ستاد اجرایی فرمان امام و بنیاد تعاون سپاه هستند.
©
yasharsoltani
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2280" target="_blank">📅 09:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2279">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۶۸ روزه اینترنت بصورت سراسری قطع شده و در همین تاریکی دیجیتال، بازداشت‌ها و اعدام‌ها ادامه دارن.
قطع اینترنت فقط خاموش کردن ارتباط نیست؛ پنهان کردن حقیقته، اما خون با هیچی پاک نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2279" target="_blank">📅 08:21 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2278">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tZ4ES7jcvZ0q3EddonM-rXCjakvC10zsh_KtvvANwVgdJcto4GhOTsJ2vY9sooqhYbnetdCkyUpr88i13zuJjueNzBBSu8Y1bpk0Gr16JqWKU_qU9OiIEQFMFqWOrsHhuEiUUgsz4CpnwWoVvYrAT_aokqBC57e_gH3qwyzAZtpLWKwF3pGOjm2QzvX7cwgEGBZBChP_jtYtt0Pw_m77Z1H5ez7ShKmTl6Y_LGxUe26jaPRTp-D5xKRR3e-_I04Js5EnhmjPgN_e3Tn5FvBhfUEGpELpGhuQ5P8OzAQim2MLYBKZS5KuuzGIu0oLOqogeXVeqcQbFRp01WzII7hamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۲ از اپ متن‌باز و رایگان TeleMirror برای دریافت آخرین مطالب کانال‌های تلگرام در شرایط محدودیت شدید اینترنت منتشر شد.
در این‌نسخه بیلد لینوکس و مک هم در کنار ویندوز اضافه شده، برنامه چندزبانه شده و یه سری از مشکلات برطرف شدن.
این برنامه فیلترشکن نیست و به وایت‌لیست فعلی اینترنت متکیه، بنابراین ممکنه روی یکسری از اینترنت‌ها کار نکنه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4295
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2278" target="_blank">📅 20:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2277">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jkKvjgiC0_WIrz2REdBbkQHZhR5g_htwgl4fX1-6b_2AlN9F972yeGnvCsozSQBQ03Nwd0IabTcVD14Oc1ZKU2MbtTt5r6JyWSGfTbNYLWGEGTjBgk5_kwXX4VP8lHuTVQPZhR6ZbI8ea6WrFYJLlPJTfayXgaMnevM0N2-BH90u7w4eyLXalFJCSomgXNBd7foSc6MjLU6_Qz89W7bxVwz4DLHHqtfQra4eMuZ421p-pqgpntkDVSCDR_HHozI2uZanu32uNJj95ImBz0MtN6FPz35aebw4HDEMzgVt8cTkfmDLq5Fne0punvClU86bX4LWgUEYYsLazyTjZLRnkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک آسیب‌پذیری بسیار خطرناک در هسته لینوکس با نام Copy Fail (CVE-2026-31431) شناسایی شده، که به کاربر عادی (حتی بدون دسترسی sudo) اجازه میده تا کد مخرب رو مستقیماً در حافظه (RAM) فایل‌های سیستمی تزریق کنه، بدون اینکه تغییری روی دیسک ثبت بشه؛ به همین دلیل بسیاری از ابزارهای امنیتی قادر به شناسایی اون نیستن.
این حمله به سادگی و با پایداری بالا اجرا میشه، میتونه برای فرار از کانتینرها (Docker / Kubernetes) استفاده بشه و تقریباً تمام نسخه‌های لینوکس از سال ۲۰۱۷ به بعد (Kernel 4.14+) رو تحت تأثیر قرار میده.
اگرچه با توجه به وضعیت فعلی اینترنت در ایران بروزرسانی کار دشواری هست، اما توصیه میشه در سریعترین زمان ممکن سیستم خودتون بروزرسانی کرده و وصله‌های امنیتی هسته رو نصب کنین.
©
Bamdad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2277" target="_blank">📅 17:02 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2276">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcDulw43GSSkYDQsMT9rNaloWWxkN-jGztkXij9ov0mPG-G1bu8AwBnf6MfQyDVMme5doP9rUCti_D7yrIVSrUMHzu4sfaNrVjeJ6L-5tqw8iS4SU65kTBbq7hgVqGJYI7qGjNMDn88bARNXJY9n8lcNJU3rvMrkowzL1902rGD4WRlWYhYGS_ZH3HK27Z3ox0pNqsX_MibymNzgzWA-R5Sn_c3EWF_Td8foWRo3urszRL8NPz-XMqnj0xnCJHLqpPS-u8J-ZDXwD4Ptzjij07vGlN_eeOsZN2qyJr2H1DDxbjYHJpge9apzaFIE7xGFOKf07s94SEzWzFPEmArF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل آموزش ساخت فیلترشکن شخصی به کمک گوگل و کلودفلر از طریق متد MHR-CFW منتشر شد. اخیرا یک کاربر فورک جدیدی از این پروژه رو به زبان GO بازنویسی کرده که مشکل سرعت پایین، لود نشدن برخی از ویدئوهای یوتیوب و همینطور یکسری از خطاهارو برطرف کرده.
👉
github.com/ThisIsDara/mhr-cfw-go
💡
t.me/ircfspace/2259
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2276" target="_blank">📅 16:49 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2275">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">توی خبرها دیدم که دستیار ویژه وزیر کشور گفته "محدودیت‌های اینترنت احتمالا تا ۴۵ روز دیگه رفع میشن"؛ بنابراین بنظر میرسه باید خودمون رو برای کابوس ۱۱۰ روز قطع اینترنت آماده کنیم!
😐
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2275" target="_blank">📅 16:42 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2274">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EqIXCi5TD3Slpw-14QeqGaMTLwbJ-2g8MXRaA4b-YozlmLHYNxn4LPfCboKcHw5ARZucipKqmZS9cJQRV8udmu8rFgUjUKKb0k7ub_JPDJXKXEjUB5IqQhO7Mh1w_w3noqNy4wbCy5p1rKLt1nRfdRnQHEwTxqgFQ9Ki_a-C1KMrTxn4pJ2CVg-GLLsOLeXTaNXsSf7k-q1KZuxGdh-9F0PiEEHtfpm_nfwRcH8jGfGt-dFhbU2FcQGv8LZQ2zlcampn-OlpJdnF42onZihudtFPRZY4Cz3EwbIxmPwMmGfa2Gm4rxGk1GLY0fieZxGBMW6VpnqJrF9aojrg1Q0xSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز خبری در رابطه با قطع اینترنت سفید خبرنگاران توسط ایرانسل منتشر شد، که روابط عمومی این اپراتور گفته نقشی در این ماجرا نداشته و "هرگونه قطع احتمالی دسترسی متفاوت برخی کاربران به اینترنت، لازم است از نهادهای تصمیم‌گیر پیگیری شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2274" target="_blank">📅 16:38 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2273">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CDEjmjJX2NvSK38e_ku9IkM5Mbv132iju17awROKoADMi8ly3LOuy2UqHLGxcgeqrTPimxju1gBHBTYdxqLHpprNDokOto7U9Oquver80C7DlFEHawrJCrfCAvKDaCKxGfn6Qr-KY2z6BfAncix8HwxXlBlm-1SvVBz3u5tSiZC9l-sR0RXJIi17ZNPouJ5JLg4UYoxeEPQzgG8LTK5xNcUU1xZowZxFqFkZUnQgvHInjzZeFYvGCf8oUEq2Wrl8FPh5geOwmFLm_C2LitUFxJCJwqg-tdELpWEdN9UV_pAZ1EbcmL2zOlRKq2lKkMB6Fnvcncc1DGflvTSmT4tK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: قطع اینترنت در ایران اکنون وارد روز ۶۷م شده است. اقدام به سانسور دیجیتال، پرده‌ای از سکوت بر افزایش گزارش‌ها از اعدام‌ها می‌افکند و قربانیان را از دیده‌شدن، پاسخ‌گویی و حق ابتدایی شنیده‌شدن محروم می‌کند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2273" target="_blank">📅 12:26 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2272">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">توسعه‌دهنده اپ SlipNet متاسفانه از توقف توسعه این اپ کاربردی خبر داده و در بخشی از توضیحاتش در مورد علت این تصمیم، نوشته که "توسعه ابزار آزاد، رایگان است اما بی‌هزینه نیست. متأسفانه در جامعه نرم‌افزاری ما، فرهنگ Donation هنوز جایگاه خود را پیدا نکرده است. از سوی دیگر، جنگیدن همزمان در دو جبهه (فیلترینگ از یک سو و خشم و کامنت‌های تند برخی کاربران در روزهای اختلال شبکه از سوی دیگر) توان ادامه مسیر را از من سلب کرد".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2272" target="_blank">📅 12:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2271">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کاربران میگن ابلاغیه‌های مشابهی رو از قوه قضائیه با موضوع "پرداخت وجه و تسویه اقساط"
دریافت کردن
، که توسط "نوآوران پرداخت مجازی ایرانیان"، یعنی نام تجاری دیجی‌پی (زیرمجموعه دیجی‌کالا) ارسال شده.
با توجه به اینکه ثبت اظهارنامه آنلاین از طریق سامانه عدل‌ایران امکان پذیره، احتمالا تعداد نفراتی که پیام‌های مشابهی گرفتن اندک نباشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2271" target="_blank">📅 22:24 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2269">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V57HnRDmga1sYtcR_FEPNtUnEqLBV2W7kHVIEFMaoGeFVC1TAHpYt7szdAi8tG-0Sbm5gMABe3acexAbRNWjNoqAeiF3UYTQHRDgK0xHztmY821CXPHKY33Lecj8hIDVSVV4zGDwWTkuVoRC6nxzZZwsCfvge5_yyrDkWZRAO5Z_uNi3n23XxS1xmcs5BtVsNdawJzWyb12Dze9ZF71QHPgY3pDyrs7ZyUZwRrGfCFh1bSjG_x4ie6SZ-gefRn8RgTS_9Iau-vSc7OPPMuDJPEaNVycUTE1aiuRXk36zUI41JnRWdrcplMoChrsDbg1NzlCywEwheWLf_lzoDJGgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبری که امروز در مورد "ثبت رکورد ژاپن در رابطه با سرعت اینترنت" در صفحات مختلف منتشر شده، مربوط به حدود ۹ ماه قبل هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2269" target="_blank">📅 22:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2268">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QP0q4ksOKc9ioeoUCItIdyKvElK7CzHUWSAZreg2EwNL-yv1RVyuOG8k3pxGuY3DkkfVKYn6jYwOsm4_qBldHKYTRfT02I1_IJ5yg-3NNoHZAhlqlVqltwigVECBDjp0SF19AtK005BmbglsSrWMPeZSvkYkjB5rnuDRanvvq67ApZa6qlbisTJSMDZCYW2Abzp99pshu2_LgSwfmUJdiXbKXiOmAqve6QI_sIaqLpKA3fY2_kbowGzlAN-kjK7m-10d-3IKpuM_UOSpGTMyC9FoBJj4cStb4zYVLO2bfZ91cUxda2ebcxe7eQPUKCiwlMI-u5rH9qzdqEurjS8Q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیجی‌کالا خیلی اوقات در رابطه با خسارت‌هایی که بصورت مستقیم و غیرمستقیم به مشتریان و تامین‌کنندگان وارد میکنه پاسخگو نیست، اما در شرایط جنگی از طرف سرویس دیجی‌پی بخاطر ۲۰ روز تاخیر در پرداخت قسط اظهارنامه قضائی میفرسته؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2268" target="_blank">📅 21:57 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2267">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eiQzyJaA2WaJPC2QjVwbzWe5h5ODx9ye93QtkcfNVcsBSqiRwWAjRojLgJF3D9zE8zTo-vVet4zNM-lGTb4lk48VjA3gANqwwAM2tH_ZFpGH5YrQyLXexrRSxrZ7rq-Ae1hqXN-XOaLRRBuppvHQMnCD9ZGbAbPUt95QNVbmWshbBpEUmJmaAo3RoYmV1SxDLKBCxPJHogR-jNZI8cfsRx1WAboTrXQGV3RfZMN5WcnEqmasfvtdRSHIcNRxiWQz-3ljtp9-SjzMRCFG6vykOiasVOorjT2jpvKN7Nnt0har7fW-zU0FDgOV0oiQb8fu2pyJndAJj2pt5ixvvIwbkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ TeleMirror یه تلاش آزمایشی برای دریافت آخرین مطالب کانال تلگرام خودم و سایر کانال‌های موردنظر در شرایط محدودیت شدید اینترنته، که سعی می‌کنه با چند روش مختلف پست‌ها رو بگیره و نمایش بده.
این برنامه رایگان و متن‌بازه و فعلا می‌تونه برای دنبال کردن اخبار تلگرامی بدون نیاز به فیلترشکن، یه گزینه موقت و کاربردی واسه دسکتاپ باشه.
👉
github.com/ircfspace/teleMirror/releases/latest
💡
t.me/PersianGithubMirror/4128
۱. این برنامه رو برای کانال خودم نوشتم که در لیست بصورت دیفالت وجود داره، ولی هرکی میتونه سایر کانال‌های موردنظرش رو وارد کنه
۲. برای اینکه ریت‌لیمیت نخورین پست‌هارو برای مدت کوتاهی کش میکنه، که با هربار مراجعه یک درخواست به سمت تلگرام ارسال نشه
۳. به وایت‌لیست فعلی اینترنت متکی هست و فیلترشکن نیست. ممکنه روی بعضی از اپراتورها جواب نده، یا خیلی زود از کار بندازنش
۴. برنامه دیتارو از کانال‌های پابلیک میگیره و به هیچ اطلاعات شخصی‌ای واسه تلگرام نیاز نداره
۵. در حال حاضر نسخه ویندوزش رو منتشر کردم، اما اگر بازخوردها مثبت باشه برای مک و لینوکس هم ارائه میشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2267" target="_blank">📅 19:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2266">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">در شصت و ششمین روز از قطع سراسری اینترنت هستیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2266" target="_blank">📅 08:59 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2265">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ipMxwftHRFUoUFbXm9TuZ1h7cNDjgY73CDX_eB4soZ9KgekRZaw67SpAChSNlxxbxiYRwhp3T_vcOcrU41FE42RzDQorcU4ZyEtnfP0IfccPv8GsTVU4pjmq9PF_aQIC0QytV8zSjb2OG9Pk2M5cRwnBifWvTS9AAgRqyYfmERtZeO-AWJ0dgp2C2GNpxITu9KScExkdAMQXvORg21GP_YWqaX56kV8PrUZ-LCaYD7tOhk2EY8eusWkttaoquf2oBCJ-Rgiljqbrdf6QeGPCZH-GegF8cDXfXrILbqhf3Dif_gd0eb3Bgbyz0hxEoK8_rdE8BTHvH-tJ9V2P2Ynhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌بی‌سی در گزارشی گفته که شبکه‌ای مخفی در حال قاچاق تجهیزات اینترنت ماهواره‌ای استارلینک به داخل ایرانه، تا کاربران بتونن محدودیت‌های شدید اینترنت رو دور بزنن.
در این گزارش اومده که افرادی در خارج از کشور این دستگاه‌ها رو تهیه کرده و بصورت پنهانی وارد ایران می‌کنن، تا دسترسی به اینترنت آزاد فراهم بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2265" target="_blank">📅 08:53 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2264">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انجمن فین‌تک در بیانیه خود استدلال کرد که رویکرد ایجاد اینترنت طبقاتی، گره‌ای از مشکلات زیرساختی باز نمی‌کند و در عوض، اعتماد عمومی و پیکره اقتصاد دیجیتال را با آسیبهای جبران‌ناپذیری مواجه خواهد ساخت.
این انجمن از نهادهای تصمیم‌گیر، به ویژه وزارت ارتباطات و شورای عالی فضای مجازی، خواسته که به جای تعریف طرح‌های تبعیض‌آمیز، بر بازگرداندن کیفیت به کل شبکه اینترنت کشور و صیانت از حقوق کاربران تمرکز کنند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2264" target="_blank">📅 08:51 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2263">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nptbbRRQOayZauiaEiU77sAh1_DubUmtu8iIbjT8DVMSr28cpQOiBAj7FagufKTnWskNZEmjFVTano98csqA6mZcjqd7Ny4GpNfW_KvtGmfBdDIarfT7gzkkzuVpxGasvbtiEnSkb0gyqmE7T_thOmKjaQP0JLdqe6H1IpPBp3HMyVopRrIUT8q2aw0Pser656eqZEY8Ku-lQeCtvMZvRsx-zOS3gOa5sprjbN470NLAZE6woCpGiYr5LrkcZmIFfumtxw8QGHCqcP1IOEvLyacZh1HE9qWh2biyeDQmTqUlA9tSmj3iohvWWfw9ymp9OOl3svpCj8MpuqMEOcbCpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت‌بلاکس: داده‌ها نشان می‌دهند که قطع اینترنت در ایران وارد شصت‌وپنجمین روز خود شده؛ این در حالی است که نگرانی‌ها درباره وضعیت حقوق بشر در کشور رو به افزایش است.
از طرف دیگر دسترسی گزینشی و سطح‌بندی‌شده برای عده‌ای خاص برقرار است، اما عموم مردم همچنان از ارتباط با جهان خارج محروم هستند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2263" target="_blank">📅 11:13 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2262">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بلومبرگ در گزارشی نوشته که قطع طولانی‌مدت اینترنت در ایران دو پیامد اصلی داشته؛ از یک‌سو توازن قدرت رو به نفع نهادهای امنیتی و نظامی تغییر داده و نقش اونها رو در مدیریت امور کشور پررنگ‌تر کرده، و از سوی دیگه فشار قابل‌توجهی بر اقتصاد و زندگی روزمره مردم وارد کرده. در این شرایط، دسترسی محدود به اینترنت نه‌تنها ارتباطات و جریان اطلاعات رو مختل کرده، بلکه کسب‌وکارهای آنلاین، تجارت و خدمات وابسته به شبکه رو با رکود جدی مواجه کرده.
برآوردها در این گزارش نشون میده زیان اقتصادی این وضعیت فقط به تعطیلی مستقیم کسب‌وکارهای دیجیتال محدود نمیشه؛ اگرچه این بخش به‌تنهایی روزانه ده‌ها میلیون دلار خسارت ایجاد می‌کنه، اما با در نظر گرفتن اثرات گسترده‌تر مثل اختلال در زنجیره تأمین، پرداخت‌ها، تبلیغات و کاهش بهره‌وری، مجموع خسارت‌ها میتونه تا حدود ۸۰ میلیون دلار در روز برسه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2262" target="_blank">📅 08:37 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2261">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">روز شصت و چهارم از قطع سراسری اینترنت.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2261" target="_blank">📅 08:35 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2260">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کاربران شبکه‌های اجتماعی از جان باختن حسام علاءالدین، شهروند ۴۰ ساله که گفته می‌شود «به‌دلیل داشتن اینترنت ماهواره‌ای استارلینک» بازداشت شده بود، خبر می‌دهند.
بنا بر گزارش‌ها، او که پدر دو دختر بود در اثر شکنجه در بازداشت جان باخته و پیکر بی‌جانش را به خانواده‌اش تحویل داده‌اند.
©
indypersian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2260" target="_blank">📅 19:31 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2259">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نحوه ساخت فیلترشکن شخصی رایگان به کمک گوگل و کلودفلر، از طریق متد MHR-CFW ...
📽
youtu.be/L3lJZrAqqUQ
💡
github.com/denuitt1/mhr-cfw
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2259" target="_blank">📅 19:22 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2258">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tTxUx9Tm3zj3nUOZKxSbrtzbmExZk9B9joBSDXhRx2-MKDJo2LVcrP1M6FDP4hDC3YzMylDnedadRs81a77wkCMwbJM5ICf6DFG2s51pX7S1TR0VBmFvZdBGjvDPZY40wXrp7XlJAXb7eYiOASBS89E6U8U-50GDWH9uz6lI4TV0DeWXsw2TEeQrAF_Wrk2vCQ5tHSkV5GCP2TGeijPN7_vQ7cRac_prwY4oaCNeoTTUlIxQrLeaZLmZFNeYHceaYogBo0mHloYkDK0FMPGoRvOHu5uYEWw868BsbSvccZKMIXYtf0K9jkjvkZ5jsxuvA2LbUPp6GY7cEJYuh5caKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با روز شصت‌وسوم از قطع سراسری اینترنت در ایران، گزارش عملکرد سه‌ماهه اول سال ۲۰۲۶ شرکت Meta Platforms منتشر شد، که بر اساس اون تعداد کاربران فعال روزانه این شرکت به حدود ۳.۵۶ میلیارد نفر رسیده و نسبت به سه‌ماهه قبل حدود ۲۰ میلیون نفر کاهش نشون میده؛ هرچند این شاخص در مقایسه با مدت مشابه سال گذشته همچنان رشد داشته.
متا اعلام کرده این افت فصلی عمدتاً به دلیل اختلالات اینترنت در ایران و همچنین محدودیت دسترسی به واتس‌اپ در روسیه بوده. البته در پی انتشار این گزارش، سهام متا با واکنش منفی بازار مواجه شده و در معاملات حدود ۷ تا ۱۰ درصد کاهش یافته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2258" target="_blank">📅 19:13 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2257">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بعد از ۲ ماه قطع سراسری اینترنت و شدت‌گرفتن تعطیلی‌ها و تعدیل نیروها، پایه حقوق وزارت کار بنابر مصوبه شورای عالی کار ۱۶ میلیون و ۶۲۵ هزار تومن تعیین شد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2257" target="_blank">📅 17:39 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2256">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران در
موضع‌گیری
خودش نسبت به اینترنت طبقاتی و حق دسترسی به اینترنت آزاد حرف‌های درستی مطرح کرده، اما خبرنگاران جزو اولین اقشاری بودن که به اینترنت سفید (یکی از
سطوح
بالای اینترنت طبقاتی) دسترسی پیدا کردن!
واسه همین این بیانیه بیشتر شبیه یک موضع‌گیری تشریفاتی به نظر میرسه، تا یک مطالبه جدی و فراگیر. اگر رسانه‌ها واقعاً به این حق عمومی باور دارن، اولین قدم میتونه شفافیت و انتشار فهرست کامل خبرنگارانشون همراه با وضعیت دریافت یا عدم دریافت سیمکارت سفید باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2256" target="_blank">📅 17:33 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2255">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iUrlfjFdpNv_dRMhnH4H1R-edWTDSyMDgW01U9nWLR9nci9qN4zq_yddH2zwMyjKJV5eAkoQ7U0wCt3f4poJy-qp-WIoyNQixHqcXHxMxRgJRry-DxAPtx9YSAqkIPXg9kM7ou9C77UickLlXegoW-lVGVDqA61Sk-GFC0BKy2NChdZVOhsLEIQlUoSiSVJPVAmy9pdSZhDUwfX1rsjglqFgm8uo68462Fzd_ehJIHVnywtEW_XQAekqrccxB7F-eKVESG_-kpyKf8M2x0ayihhhnC4YxNjhPcBuaLCv8laNGDyoJ-KlwceqMqJQpHRylxMvhv4SSRKvEPpKUB-tUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن صنفی روزنامه‌نگاران استان تهران با صدور بیانیه‌ای تأکید کرد: دسترسی به اینترنت آزاد، باکیفیت و همگانی یک امر تشریفاتی و لوکس نیست، بلکه حق عمومی است و دولت‌ها موظف به تأمین آن برای همه شهروندان هستند. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2255" target="_blank">📅 17:27 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2254">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7BYhtuu2pgazHXB1FRDwD5cT7Q4GsqR1FpCVKsmMLVQt7B-_4DQ3IXdrftcJlTQ-AVqadXtbTdtYJYx7MVhBZUvjwbo0BqXnhfFxonw3QCA-I92Ch55fzVOV2SUqPmOTBqqPFKQsApuQQJVBpZ4roIhrQyyQrkUcM1rSjyhpU5SuUOymzWRUXYOG3R8Auv866aveEslV3Vl9yzc8YThRaSWoOICqjJ3_jU747fid4_es6BDEbvluzhMUnH82zPsUOGVsmUMRbFdauDtRK4S4DR05HQc9EpP5cKw01pLC94JIqeGNwTfsn2s4dr-94fUYC_EYYzV49f_YjC14wqQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایفون در بروزرسانی جدید اپ اندروید Conduit گزینه Personal Pairing رو اضافه کرده، که میشه یک لینک اختصاصی دریافت و با دوستان یا خانواده به اشتراک گذاشت.
این لینک رو باید در داخل اپ سایفون از طریق بخش Pairing URL وارد کرد، تا مستقیما به ایستگاه کاندوئیت کاربر موردنظر متصل بشه.
البته با توجه به قطع سراسری اینترنت، فعلا سایفون بصورت عادی برای کاربران ایرانی قابل استفاده نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2254" target="_blank">📅 17:15 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2253">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjALbj45vVT2v1nnWEowt-Q_DsTv4FhIHEq3D4dQDspA4YRBw7kL8F4W1eC3KlA763jzwPghyi6Ahe7jYzDjmdFwQ3N_J8w0au9tyaMbcQyL1NplFR7qqSmoiFDo22CVt_8xUtmFTR_NswDwb7m0gR0OcFfA7gWP4_blcP5JYCE49FbAPyACy33X08eDxvrESXj1TD6kGRb4dtbZUdB_QO3cY9t0hFLehL0dYIarOq1SJw0i6xhv9-DK6M1JAyLfwmtzAJTx_DV-snkA5NqNXGGrEOjzw4Dop4puX0SZwgCXFr7zHZkbGkQ8h6EKXx3G5epr1W7Ftm_8-JvUXmnldw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش تازه سازمان گزارشگران بدون مرز نشان می‌دهد ایران همچنان یکی از سرکوبگرترین کشورهای جهان برای روزنامه‌نگاران و رسانه‌هاست. جمهوری اسلامی در میان ۱۸۰ کشور، در رتبه ۱۷۷ قرار گرفته است.
©
dw_persian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2253" target="_blank">📅 17:03 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2252">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">روز شصت و دوم از قطع سراسری اینترنت در ایران!
میلیاردها تومن پول داره توی زمین VPNها میچرخه که بخش زیادیش میره توی جیب جمهوری اسلامی و حامیانش. شیرینی همین پول‌ها باعث تداوم قطع اینترنت بین‌الملل و تمرکز روی اینترنت طبقاتی شده.
جمهوری اسلامی ده‌ها هزار نفر معترض رو در دی‌ماه قتل‌عام کرد. یادتون باشه بخشی از همین پول‌ها که بابت
#اینترنت_پرو
هزینه می‌کنین، قراره خرج گلوله و سرکوب مردم بشه!
©
Maroon
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2252" target="_blank">📅 08:35 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2251">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZC5slR7IR5Q__XodHeaXfj4Mn-vro_uK4mgGmUX0lesSD7VfBYGWRw97NbI-A6SBzdRB_bnWH-PFoKdknHyxBOSo4Q7sWzp_ZLHjkWr6It9kzu801VvgajzUKisXQVMy_fT5ean6nb-D7iPIpFme5S9rFdbgwLw_RIh2N6U5p_ROoeT4JzMx48o8QiYlUwvUbbhUAw-HHGvpgU2ejN4qsA7WXukqVAWJfIEfN-lPqKHumKqnDoy3abg1KccRmniY63q8yVcqeK99zm2Whg5w8RoQPA7W-42jCnOTXfs6SMNC0NVkmUclWc6KsUZktN661sLb72DyGIUZIgVb76VgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلیمی، یکی از نمایندگان مجلس گفته: رئیس جمهور و وزیر ارتباطات مطرح کردند که ما مخالف اینترنت پرو هستیم؛ پس چه کسی این تصمیم را گرفته؟ رئیس جمهور بورکینافاسو و وزیر ارتباطات افغانستان این تصمیم را گرفته‌اند؟ رئیس شورای عالی امنیت ملی، رئیس‌جمهور است و باید در این زمینه که می‌گوید ما مخالف هستیم پاسخ دهد. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2251" target="_blank">📅 18:05 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2250">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ISADKK0t8151vPko3eGeOMFEn6gjx5u5jizNo16u2Mf1dwqYxgZRXhdqjXYPrSOj3jwKzcz3ZCnAHHTtOsK-JQNGqDDm08LY7wz9iqUq3ndFCV_CjI36wYDwGCefLrnnNHpFnZZ9XBwPkw985O-7INXtcMSS_e5h7TcJVELQTQacPS84L2BnutrWD6dcxQVIzAzujpZslmRq4c5lZ7baXeMNlr1Gc0N3-nSo1A4SZ_yXtTx7JeKvghrDovbY32mwb32HtYJSjBkgnK6gc6BO99PQupumcZdm4nbov0oPGf1VyEGDkr25Bs9zHF0iGoeDFKLW3iJYjaKpAxv_5Tpz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت ما را به عصر حجر می‌برد!
انجمن تجارت الکترونیک در بیانیه‌ای اعلام کرده که قطع گسترده و طولانی‌مدت اینترنت در ایران دیگر قابل توجیه با ادعای «امنیت» نیست. این انجمن با اشاره به بیش از ۱۰۰ روز قطعی در یک سال و بیش از ۶۰ روز قطع پیوسته اخیر، تأکید کرده که این سیاست‌ها نه‌تنها امنیت ایجاد نکرده، بلکه اقتصاد دیجیتال را تضعیف و جامعه را با آسیب‌های جدی روبه‌رو کرده است.
در این بیانیه آمده که حتی در دوره‌های قطع کامل اینترنت، حملات سایبری مهمی رخ داده و این موضوع ادعای ضرورت این محدودیت‌ها را زیر سؤال می‌برد. همچنین هشدار داده شده که گسترش «اینترنت طبقاتی» به معنای تبدیل یک حق پایه به امتیازی محدود برای گروهی خاص است و شکاف اجتماعی را عمیق‌تر می‌کند.
به گفته این انجمن، مسئله تنها دسترسی به اینترنت نیست، بلکه حق دسترسی به اطلاعات، ارتباط و حضور در جهان امروز است؛ حقوقی که با ادامه این سیاست‌ها نادیده گرفته می‌شود و هزینه آن را مستقیماً مردم می‌پردازند.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2250" target="_blank">📅 17:46 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2249">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CwYaEQSblMO9FTS8vP70L5aXwLLqZI6JnwXpzbC3ItPL4MPSLNFQ2yC-e4wsdxb099dLCi5PlWLRX4iV1T_56hapaBn4t4xoDcwqFqLNvHucKnISBZGUsJ53lUQbSb2e4PBeaF9Tv6ZdlfPBx7HRDYoQi2ygSavSjfNmzU4QK_dbhyefHTTeNfDy-dbu0yqWKCP9RmDmlCyxybK8O7qEZwJYORJNGg6V_98_N_6ZmxduVhfOMqOA0p9-hMZDpY3yYhyI8vdSgnUXgW5pbqtkfIdYagAqXzfnof3DyHuTGp9wWzc38KQvKXlmNRdN7Zj6gfp4LsAHMvO8tq6uLMhbHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نسخه جدید CFScanner، دامنه‌ها آپدیت شدن و هسته ایکس‌ری به نسخه جدید ارتقا پیدا کرده. یه قابلیت هم اضافه شده که می‌تونی خودت دامنه‌ای که برای Fronting می‌خوای رو انتخاب کنی. همینطور پشتیبانی از Xray توی اسکریپت bash اضافه شده و نسخه Xray تو بخش پایتون بروز شده، تا همه‌چی هماهنگ‌تر و روون‌تر کار کنه.
👉
github.com/MortezaBashsiz/CFScanner/releases
💡
t.me/PersianGithubMirror/3624
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2249" target="_blank">📅 17:28 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2248">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPhx6gGyXkYA1ZFOWka5LUMXmEueVkx5L-u6Q-gq9cQlrkefb7vtqDBKK1PWXqefi0Ybeiz7kM2B2Ua66Os3IjEdNI4oaCh5JJDrbTtKwIb3qE8X_BODVt8CZP9DABfn6L_OoJp__kjwA_zXqprtH0mh-HFKIjEelWOPFMsZxcW5Dje9SMCgZ0mg5ANrdpWZfB8sB-5SxSGObzTrdPfYyQd3lk4JgDSOF5Rc9rJm8qqT500Mik4cDlrbtrA_1k5K26KgtEBurdoch4MUehxOlu6FOZ5Pmea9UK0yT5O46TcOJbWU0WPfoEjHrNmiuGhM4Jhmnq8nv9RPzvahJ0tEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن علمی روان‌پزشکان ایران اعلام کرد "اینترنت بخشی ضروری از زندگی امروز است و محدودیت یا دسترسی نابرابر به آن افزایش فشار روانی، احساس بی‌عدالتی و کاهش اعتماد عمومی را در پی خواهد داشت".
©
shima23972921
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2248" target="_blank">📅 17:08 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2247">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روز شصت و یکم از قطع سراسری اینترنت در ایران.
لعنت بر جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2247" target="_blank">📅 08:48 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2246">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aj6bvq3GrlzdmhguTpeNmPobboEqERA0W0g9XWAlWPwo9ywUaI-OsfVaqWOdF9NDxauoruN79kWYXvJR4z0vCBysUrbySS4kUwgUoPGrSHg34_UWXWyPefXPs1zywTZ7xJce8OuFmy4toHFmYiCvKIu8a58-qCPZvwSaQGZIGx49j4J7n_qJu_JYqxJUHsjvnHiaAY43RC0lIxU7khm5SuG8HC8mddDYA5WtEReOZRu0z2BP3oIczt9hPcX83rrDLVcDXmHjLljK4CZn6RsQJNW1bsIRkMUWzFK1jrVbOQK23u62GN3ZtZPyW-EjLQPsVeF6NX1zfOFQIw4jv3IXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به واحدهای قضایی دادگستری نامه زدن که میتونین از
#اینترنت_پرو
برای انجام امور جاری و تخصصی استفاده کنین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2246" target="_blank">📅 08:41 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2245">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هیچ‌کس از هزاران فرد دارای معلولیت که از طریق اینستا آنلاین‌شاپ و درآمد داشتن حرف نمی‌زنه. قشری که نه حمایت دولتی دارن، نه جایی تو فضای شهری و نه سهمی از استخدام‌ها‌.
©
Mtherofcatsings
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2245" target="_blank">📅 18:35 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2244">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اینکه می‌گویند قطعی اینترنت «روزانه ۵۰ میلیون دلار» ضرر دارد، یک مغلطه است؛ این عدد فقط نوک کوه یخِ خسارت‌هاست. ضرر واقعی در نابودی  کسب‌وکارهاست، خصوصاً کسب‌وکارهای کوچک و استارتاپ‌هایی که شکل‌گیری‌شان سال‌ها زمان و هزینه برده. با هر قطعی، بخشی از این اکوسیستم از بین می‌رود.
از آن بدتر، این خسارت متوقف نمی‌شود؛ وقتی درآمد افراد قطع شود، اثرش به کل اقتصاد سرایت می‌کند و یک زنجیره از رکود ایجاد می‌شود. بنابراین مسئله «۵۰ میلیون دلار در روز» نیست؛ واقعیت این است که قطعی اینترنت، در مقیاس میلیاردها دلار به اقتصاد کشور ضربه می‌زند.
©
hiddify_com
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2244" target="_blank">📅 18:33 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2243">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رکورد ثبت رزومه در جاب‌ویژن شکست و بیشتر از ۳۱۸ هزار رزومه در یک روز در این پلتفرم ارسال شده. این مسئله نشانه‌ای جدی از تعدیل گسترده در بازار کار و تقاضای انفجاری کاریابی در پی اونه. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2243" target="_blank">📅 18:28 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2242">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C3A5kM8AEg1W50DtwjL6i_meh9jhaG1NuXPe0xIHQ4q5AbVqKRvp_OE58xq4RFhW-PHx-pSUbXd_HiIHhcBAING_584ZA64eiFEieCMrJErtc2JmRXuoYykDoOMjw8cO9Jjm04DBMWrl-D-j6C3EIEFAaj3BYDyXE_oz5ESBy5ySbmNRjm_IspNuDF3D4sNsmaPcjLJwwhRDz_3x-xkQd7PGDbx6rZBU7tJqyTphqJfN5yPuM-OKncI0BQbsQub8rTUID-GDpOIWG3EEMXDQfx4xCxMP5BcGUNGuQDseo193GPYKo9Q86PHM4LEMzWAlR-XZEVfYfsBzWZFpvkkjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی وزیر قطع‌ارتباطات رو از برق بکشه!
۶۰ روزه اینترنت بصورت سراسری قطعه و بازار
#اینترنت_پرو
داغه، مشخص نیست هاشمی در مورد کدوم تلاش حرف میزنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2242" target="_blank">📅 18:22 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2241">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZXu7Q3D08gRhYBDf0pS2zhoUnXTIMLtI3166zlryMk2DRnl6tokFiKgpA1diRXbpaV8_nKSyuwCdx4BXBBP4VSNsH4j9FdHDAABh_sPH-nFUeDvQ6O_9PBFNkvnZ8vteJ-4dD7GncRjFl7N5BC4LCcN8OJJ2h1Oan__m0OJ6SSoAFfmG24_DAY8j2iL7javVD-ks57w9z80M4fYkt_kSba77mN-4Ytj2hqb3aYO8TAzHBwDq3RRT-u4EdNODdLub6TBfNR3srdn4eJUpYKM41VzyP7YBjW9LzXilQP1jowRJnRj2hJjzJY99GKdYd0exEtZm_zdbDoWgnIn0_ebdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد روز ۶۰م از قطع سراسری اینترنت در ایران شدیم.
وقتشه اسم وزارت ارتباطات رو به وزارت پست، تلگراف و چاپار (به جز پیجر) تغییر بدن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2241" target="_blank">📅 08:58 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2240">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به بهانه‌ی امنیت اینترنت را بستند و حالا گروه گروه پول زور می‌گیرند و باز می‌کنند.
این یک تلاش برای خرد کردن یک ملت به دسته های کوچک است که راحت تر خفه کنند، بیشتر تجسس کنند و مردم را آلوده‌ی بازی کنند تا دیگر حق‌شان را طلب نکنند، وگرنه امتیازات یکی پس از دیگری قطع می‌شوند.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2240" target="_blank">📅 18:12 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2239">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیام‌نرسان "بله" خیلی عالیه، پیام که میفرستی باید بعدش اس‌ام‌اس هم بفرستی که بله رو چک کنه؛ چون اصلا چیزی تحت عنوان نوتیفیکیشن نداره‌.
©
aboIfazI
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2239" target="_blank">📅 18:08 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2238">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uI_9hJotP29RZfrlSqvqOraDn6mknnvwFAM-J25oTOOkxeeMMxoJQfXbuHf5lm9urVzpQ-To7qtbe573_XLDqTY78FsiXs6YcP6--rkO1-I8g0GCtfgViaJcFdZSOexo-AjOTZ5cjVT9yxUyOtsyF-4wAuQZA287TxOaQpWmWK7lyyhZY0bbQbbHj6m56eBy6njTxpMaLvzWsP2zLxdkDGa5Y8Zzq_NHfmgZCSLdSEF0_q11tJODeD9d1SZ7tkmB9LfYLCLci5T8nYNPe8v5QgV-mjB3FAL-onh2bWg2GkQKh5V4_1ULJJDCj57UHgFWUVo0w9ey11tRKT13AWCAJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت
#اینترنت_پرو
در بازار سیاه حدود ۱۰ میلیون هست. مافیای
#اینترنت_طبقاتی
لطف میکنه ۵ عدد اشتراک رو بصورت عمده به قیمت هر عدد ۵ میلیون تومان (یعنی نصف قیمت) عرضه می‌کنه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2238" target="_blank">📅 17:59 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2237">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qAmsaTBdKq0U9UX-R5Rdx5YXhA4RyNJxY8NbJLKrhMVyCxO4iV97g_cvsmWWDn4VGNBVB0Qw7d05FwdDZSqC3DO89aBP03cPIyhgLs_m5L4glqMLVhRntyN-gqkh_n5ghWucEge6lfQVhxWVb6ddm9U8rilcDxBlSSKFH8JNg3zv5Krd9ih0R3F29tz7MXtWw7hSAFnnb_BEZYxV2-VMQ5EhtkNSmfWs1gejmLURr0Q0IpeD4mTdMQ-sLNf0dKzTfiUp7WC_xpbWMjnJG_DDnHh-fbuzzkmruIgL1aFFgeyUAW7C4_KXELZPJgTWaj0Wel5IfRdbwdBF7XdAnQ1fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت حدود ۲ ماهه اینترنت رو بصورت سراسری قطع کرده تا طرح
#اینترنت_طبقاتی
رو جا بندازه. بعدشم با کیسه دوختن برای مردمی که دنبال حق طبیعیشون هستن، یه بازار سیاه برای فروش آیپی رانتی و
#اینترنت_پرو
راه انداختن.
قبل از اینکه روش تازه‌تری مثل «پرو-پرو» برای خالی‌کردن جیب ملت پیدا کنن، چندین کانال مختلف دارن هماهنگ (حتی توی رنج قیمت) همین اینترنت سفید رو به مردم میفروشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2237" target="_blank">📅 09:17 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2236">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">در آپدیت جدید theFeed مشکل نمایش بعضی پست‌ها به شکل نظرسنجی برطرف شده، باگ هنگ کردن اپلیکیشن رفع شده و امکان اشتراک کلاینت روی شبکه اضافه شده.
پروژه دفید یه راهکار مبتنی بر DNS برای دسترسی به محتوای کانال‌های تلگرام توی شرایط فیلترینگ شدید اینترنت و مواقعی هست که همه مسیرهای معمول بسته میشن، اما DNS هنوز قابل استفاده می‌مونه. ایده اصلی اینه که بدون نیاز به اتصال مستقیم به تلگرام، بتونی آخرین پیام کانال‌هارو دریافت کنی.
سمت سرور (خارج از ایران) به تلگرام وصل میشه و پیام‌هارو می‌خونه، بعد اونهارو بصورت پاسخ‌های DNS از نوع TXT و به شکل رمزنگاری‌شده در اختیار کلاینت قرار میده. سمت کاربر، کلاینت با تعداد محدودی کوئری DNS میتونه این داده‌ها رو بازیابی کنه. طراحی سیستم طوریه که مصرف کوئری پایین بمونه و در عین حال در برابر محدودیت‌ها و فیلترینگ مقاوم باشه.
برای اینکه ترافیک قابل شناسایی نباشه، از تکنیک‌های مختلف ضد DPI مثل padding تصادفی، تغییر اندازه بلاک‌ها و پخش کردن کوئری‌ها بین resolverهای مختلف استفاده شده. کل ارتباط رمزنگاری‌شده هست و هر درخواست بصورت مستقل پردازش میشه، تا ردگیری سخت‌تر بشه.
کلاینت یه رابط وب داره که امکاناتش فراتر از فقط خوندن پیام‌هاست. امکان جستجو بین پیام‌ها، کپی گرفتن از چند پیام، نمایش لینک‌ها، ریپلای‌ها و تا حدی نظرسنجی‌ها اضافه شده. اگر سمت سرور اجازه داده شده باشه، حتی می‌تونی پیام ارسال کنی یا کانال‌ها رو مدیریت کنی.
یکی از تغییرات مهم نسخه‌های اخیر، اضافه شدن بانک Resolver مشترکه؛ یعنی دیگه هر کانفیگ لیست جدا نداره و همه resolverها یکجا نگهداری و امتیازدهی میشن، برنامه هم بصورت دوره‌ای اونها رو بررسی می‌کنه تا بهترین‌ها استفاده بشن. یه اسکنر داخلی هم داره که می‌تونه رنج‌های IP رو بررسی کنه و resolverهای سالم پیدا کنه.
👉
github.com/sartoopjj/thefeed/releases/latest
💡
t.me/PersianGithubMirror/3393
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2236" target="_blank">📅 09:01 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2235">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tv4-PGHtkrYXuvJLGirenyd3FBKUhKEKGTBLBAkQSF58o3TY-Cr_WTvMJ7xPdwqIi3-tafRSIZbzRzmC3Djf8--h4Q9twrJc-TcxVzgj1noMOcyDEHV4G8n8-D-pB2mY7dn096CTbPf2H0jxN-LUFOPVK1RpwsTRIBVzHZvD1AIBGT2WMmfbji77JUC30xuxwHbOP2JX_CISmzTrSVgcV13Akdf6Ok7f4t-yB97KHnmE4yBW-JjQ0pTi9viQWepmmGyf4YldjBaHYASqt_u17_WedvpEX_mHIqfzVk4hSXixYQfRTj2c4haty9r08vTGz4zsDd3s3MXqZfLi-Gv2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Loole یک ابزار مدرن برای مدیریت تانل SOCKS5 در سیستم‌عامل macOS هست، که برای عبور از محدودیت‌های شبکه طراحی شده و با استفاده از Google Drive و روش MasterHttpRelay، یک مسیر ارتباطی پایدار و کمتر قابل‌شناسایی ایجاد می‌کنه.
فرآیند راه‌اندازی بجای درگیری با مراحل پیچیده و زمان‌بر، از طریق یک ویزارد ساده انجام میشه که کاربر رو قدم‌به‌قدم هدایت می‌کنه و حتی بخش‌های حساس مثل تنظیمات Google Cloud رو با راهنمایی دقیق و لینک‌های مستقیم پوشش میده.
👉
github.com/g3ntrix/Loole/releases/latest
💡
t.me/PersianGithubMirror/3455
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2235" target="_blank">📅 08:52 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2234">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من تحقیق کردم، چون اینترنت پرو گیگی ۴۰ هزار تومنه، دیگه برا جاسوس نمیصرفه جاسوسی کنه. اینجوری امنیت تامین میشه. ایول.
©
SMoslemi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2234" target="_blank">📅 08:40 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2233">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یه تشکر هم از بچه‌های سوپر اپلیکیشن روبیکا بکنیم. واقعا ساختن برنامه‌ای که فیلتر نیست، ولی از اونایی که فیلترن ضعیفتر و کندتر کار میکنه کار آسونی نیست.
©
danyydrinkwater
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2233" target="_blank">📅 08:39 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2232">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwxkVdRvzgD63796E6Xnkzh7QDDxP6aF1Rhb_FkwicrYbe65BLTIx44eyNg5sBu8Zuffw1cB6ZvA3yAya9Rgr2hhsg5PrOlYnuN6VDu7CBR8crpRbMboVEWulTeRQWw2snfLfuAcDfX2owYTTKuBZkP6mugLL4JtezM1HYKiJ_CQFd2QVAK2b91Sujk35Im4UojUSOE54ED1FtsJejA1ukLVz_sj-h7jYSM29Xzb36up6GsAaShHeo3jmhQX3oyiUqoLrVn16Z1YRpsW6wKYhF1Gez-uSF6UcEgQFUA4AoKNMeBtOTXwEDLYeuTy3RpWCtLahtDFDL_ho-EnwWGjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۹ روز با قطع اینترنت مارو از جهان جدا کردن؛ به اسم امنیت!
بعدش اینترنت رو سهمیه‌بندی کردن و گذاشتن پشت باجه فروش.
اسم این دکان‌بازار امنیته؟ یا رسمی‌کردن نابرابری؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2232" target="_blank">📅 08:36 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2231">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJV9fY4eu-BZ4LNdGYW5SXp32Vjd0E171fTY05kC2KtlAqq8ccEZkei49ZFg8E1fpkzpeGv1pLXgniWE_XlpTmIc4VQZz_e5auKac-yLtO3-rNFQcPb9tM7vESeByHwn4UPekfJ9Q6KFotDuWchTb3KT5Nxm7BlkTIj_A-m14BM1TbpUnTTftcTdh8GezqkVgNKQ1yexYNeRfSnSc2ji82sQJbmeQW_7M_0UWe4p1uVIlCplSxRXHdWELKOImhX2PaUGZOCc850NO9MN8K7suhUy6rXIIzpdtQ8tC6mEbSnB7Io5b7ju-nguvi_2pm1zjmrwiQ2r4dgtWlsbH8BSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبقات مختلف
#اینترنت_طبقاتی
©
mamlekate
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2231" target="_blank">📅 19:03 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2230">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دولت همچنان بر مخالفت خود با «اینترنت طبقاتی» تأکید می‌کند، اما بررسی‌ها از چند منبع نشان می‌دهد طرحی که امروز با نام اینترنت پرو شناخته می‌شود، نه‌تنها به تصویب نهادهای بالادستی رسیده، بلکه اجرای آن به‌طور مشخص به دستگاه‌های مربوطه از‌جمله به مرکز ملی فضای مجازی سپرده شده است. /شرق
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2230" target="_blank">📅 18:28 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2229">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ej7Frqi57NQ-Mek3No_TFtEIL3H0QAOqzP0G3pgb2iIqgxNr1FtrNPbVXmBV7iQiq-OKMvAnb-MLpdlTROmAcVSDNSmpMyVHW0yPukfJQEt3F1zlqNeYHHlcfjvFVFkKJHRh0LWQoi6jCfvVTDIyqIN2SgmWk0a3TlVLeoS2gjLWdQ2qP2oMJvlhMWF7fnSucZOgqng7o0kAkrIM0C_NvTmurm89wuNPD6aHmvdP1cd0pdqNRZY4ISQ6bp6TTR3K4VDRvo5TMdxz0-G6ITwZkOUzLyD5FaiMS_X0Kgq3JmBXk_JgmzawqO21jyfDFi_7C4IG5VJnmQFbuXPUPyguYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا جمهوری اسلامی یه بخش زیادی از بودجه پدافند غیرعاملش رو‌ هزینه خرید لایک از پاکستان کرده. باقر و عباس هر مهملی میگن ده‌هاهزار پاکستانی براشون لایک می‌ریزند. قبل از پروژه لایک‌ریزی صفحه بزرگواران سوت و‌ کور بود.
©
SGhasseminejad
حدود دو هزار حساب Amplifierهای پست‌های قالیباف رو بررسی کردیم، که همه‌ی دیتا و لوکیشن‌ها رو اینجا منتشر می‌کنیم:
۱- بیشتر این حساب‌ها از کشورهای ایران، پاکستان، آلمان و یمن هستند.
۲- پنجاه و دو درصد این حساب‌ها بعد از هفت اکتبر ساخته شدند.
۳- سی و دو درصد این حساب‌ها رفتار بات گونه دارند و انسان پشت این حساب‌ها نیست.
👉
github.com/goldenowlosint/Islamic-Republic-Influence-Networks/blob/main/Data/Ghalibaf.json
©
sabber_dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2229" target="_blank">📅 18:13 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2228">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قطع اینترنت، روشن‌ترین رفراندوم است. فقط حکومتی حاضر می‌شود میلیون‌ها نفر را با قطع اینترنت بی‌کار، هزاران کسب‌وکار را تعطیل و میلیاردها دلار خسارت به مردم بزند که یقین دارد طرفدارانش در اقلیت محض هستند.
قطع اینترنت ۹۰ میلیون مردم ایران، بزرگ‌ترین گروگان‌گیری تاریخ است.
©
SharifiZarchi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2228" target="_blank">📅 18:06 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2227">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cqEtDNWtlJXaajTzRD2O6lZMmtUgYcMVwKBKue3OYO9yDkDMN0YSuGFK_TJrjWQf-bJ3KOCF5VN_2lR4NX8WRTRvgoAHjjssCFCs9k_WyJkFrOasyQiwnJoZ3Mfp45SHfZu6bhY5G42Zix6vjZcSFeQrM76NYRXE6haCXcC-sWd1NuI-lne51sIa5l68gMAwz6sRlqNYc7uvQH4x_doa1-EzTNoOWtoDmvh_Hm3q4o_LlWf9Cy2tGaXAywMpEZBlMpHYfgc5GgJGL5SmmoRbsl8G67YXK8JSKVIdZlFB4fxKmrgdRa1H0ofBxtqJLrBK-4lowdEAV2NNzMcnIKg_oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی فرماندهی انتظامی تهران بزرگ از پلمب ۳ واحد صنفی در شمال غرب تهران خبر داد. بر اساس این اطلاعیه، دلیل پلمب این سه واحد صنفی "استفاده غیرمجاز از تجهیزات اینترنت ماهواره‌ای" عنوان شده است.
©
dw_persian
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/ircfspace/2227" target="_blank">📅 18:05 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2226">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K-CwknKZKgJvWJa7y5_xOJP4QDp0iE1_dM2oOGN4oW4GGyZGw9wEDpW4Z_3FeUUxd8W9pXTPUJbRY1v52jUFWC0fQBkXHI5hsWeNZDVJLjcWCAO0ST8-1nipsGvl_bh7Fi0PWPIf5W4B_bqixBRO1knHRT6bvx9ujlyn3662ZzL1mmNQpxDnSsn9hmplXtG30nd4eG-hvN5SjsJmjbbnevDqijv-t3P5w5Qye1i-FjugonfpLWwd2OqMT2XkIlDV2DHk0061W8x5fi1-8sCoC9wd0NdiEZGyw2a7-gp851e9AiA79HjcFmoQHLHnKkPsNsqen4QgpQ4riXODue5WjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۲ سال پیش یه پروژه تو گیت‌هاب راه افتاد، که خودکار هر هفته حدود ۱۳۱ هزار تا دامنهٔ ایرانی رو از نظر TLSv1.3 اسکن می‌کنه و یه لیست از اونایی که این پروتکل رو ساپورت می‌کنن درمیاره.
قبل از شروع جنگ، حدود ۵۳ هزار تا دامنه فعال بودن. بعد از قطع اینترنت، این عدد رسید به حدود ۱۳ هزار تا. بعد از اعمال NAT سراسری هم رسیده به حدود ۱۲۰۰ تا!
👉
github.com/aleskxyz/iran-domains
©
aleskxyz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2226" target="_blank">📅 18:03 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2225">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مسئله فقط اینترنت نیست، ما از مدار روایت جهان خارج شدیم.
بی‌سر‌و‌صدا، از جایی که فردا ساخته میشه، کنار گذاشته شدیم. جهان جلو میره، ما بیرون قاب موندیم. یک حذف تدریجی از روایت‌ها و اتفاقات جهانی.
©
Mardetanha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2225" target="_blank">📅 18:01 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2224">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VBtUYKCmj3KGjBh2vRDEXG_yqnC26nW-muZuJow-rtNMhER5E8Lb-pPEe3nnO361WPK38iv3xrYwW05yE8bVYNEcD9iPOXPRZys7QNU9NJtxYs9pzyQkRzD3NTpkdI6UGt2I9MVQpKS_SbICg20D7TiI38NE75r1-FvbQkwRIVyU4QJx-74fdc5O5nncerh9NPoo85ykGjZ9_HnC1dk1Fgx_rOGtBI6Qq6qoN14j_amnGayVL88AwZWkXmNFeyN18dVIyQtrjwYuNQJf9s-8vLMAtnhf_Qu5vZw5GNAu8QZhwCgyX2DgJKRs59SXAgzzX5vp_I88YGkURTFJDeV_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان نظام پرستاری گفته با وجود امکان دریافت امتیاز اینترنت پرو، تا زمان رفع محدودیت‌های دسترسی عموم مردم به اینترنت بین‌الملل، درخواست هیچ امتیاز ویژه‌ای را برای اعضای خود نخواهد داشت.
©
ardalanmousavi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/ircfspace/2224" target="_blank">📅 17:57 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2223">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jGrMgPIuh1ONGPwR35oxqiOHZM6qWxH8G-Pf1hK9-tD8duPBLZRgz9-H_jH9A16VH6n1BiKpa8A4CSvBu-vs4AkSrGlyY8eBR2vbOMO5klN0RWSEVsXZDoNA6YbixdaU1OEIcn29XEeaGXBoRPNbdEdbtpyzCfyT1bMqwfKfJqrpc3GOvQkhy_RO8vFZJWmUMhiuOJn8j759-KpXbwpMNpxwwHFsnIBWQaZmRO-MaY-u75AsZT_5Wt08ffHYk5pjnGXGHxmAksidWOh9xKNzR-yiweJqehvw-PKwDBoXxeB3H4sAvo0XYlPgJYH-U8UgZaObDmRGVUGxTP0yssEHEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۸ روز قطع اینترنت
۵۸ روز خاموشی سراسری
۵۸ روز سرکوب دیجیتال
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2223" target="_blank">📅 17:50 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2222">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در شرایطی که اینترنت کشور (به جز نورچشمی‌ها) قطعه و هر تلاشی برای دسترسی از روزنه‌های یافته شده زود مسدود می‌شه، یک سری «سرور» اینترنت دارن و روشون VPN با ترافیک بالا می‌فروشن. نمی‌تونن این ترافیک رو در شبکه ببینن؟ حتماً می‌تونن.
پس چطوری بازه؟ TCP over corruption
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2222" target="_blank">📅 17:47 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2221">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/paQLDQBhH-AxYfZkPhHPNRoSUC1F9RB5GrAScvHePd-yvLy-FdJYiYnsNiviBtzV8OQvm8JiHRpRbvRVGcOWPtp_y8y6-srpBvnTXyTsRxEIF4jBlsfwnpt-GMbZMis7_abDv49fpR6fGiR8SXQqEJuKS0y5EE7h9yV95Eut9DlHbN4Y7uiItSKuxIw3OrbXZfvy8LNgFWKmeo3UkPJ4rIOQRB5yXcnbOfouxBJCh7B6NGmcDQ82V2kx7LX8XUkFt3TIXrXIYWf5gHIykXeJUU_qPheaL7jQ5SN9SBg-WW6vGRAB75NuEYMktqcv2_RMQkznQThWk1kLiIS0Dd28Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، ما الان چکار کنیم؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2221" target="_blank">📅 17:45 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2220">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rn3MlpMWMyc3FyJU17tEvYRMLWB_c3C2BhP3KmgACv4Z8_BTFOZGSQ1-zImFMa5ApgTcDCAPNxj_Xko4fL5dfScQnWtBLN-kaVjN8kq4ZTyzcHogYXpgY9vj5K1YLFHzpJKa506S7sFygc0bvqcJi3TtU6d5tISaiAAf8IE8qhiM5t6NCMGNUEgudQYaEZmUFpkvn5LJcFzBUDYPuQEOvwzLSGfFpjQp1HkUHdGPtItsCxcnfvuJdLS0lW-d8KJWDt4Upm9mFPSS397-iPyHElC1RGhDyiYHZYJKbFabfOknKK4R5WSit7_nWFmon6DeXHibOWFbyERk1sf4rXTX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو تشکل دانشجویی دانشگاه شریف به
#اینترنت_طبقاتی
و ادامه
#قطع_اینترنت
انتقاد کردند.
در بیانیه شورای صنفی دانشجویان و مجمع انجمن‌های علمی دانشگاه صنعتی شریف خطاب به وزیر علوم آمده که "امروز دانشگاه‌های ما بدون دسترسی به اینترنت آزاد، حتی اگر درهایشان گشوده باشد، در عمل به بن‌بست شبیه‌ترند تا یک نهاد زنده علمی. ما نه می‌خواهیم مفیدترین سال‌های عمرمان در قطع اینترنت بسوزد و نه می‌خواهیم دانشگاه و نهاد علم به سکوی دیگری از دریافت رانت تبدیل شود".
©
Citna
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2220" target="_blank">📅 22:36 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2219">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قطع اینترنت امنیت ایجاد نمی‌کند
قطع اینترنت نه‌تنها امنیت ایجاد نمی‌کند، بلکه آن را تضعیف می‌کند. امنیت واقعی بر پایه اتصال، بروزرسانی مداوم، ابزارهای جهانی و معماری‌های مقاوم و غیرمتمرکز است، نه ایزوله‌سازی.
شبکه‌های بسته با ایجاد تمرکز، اهدافی آسیب‌پذیرتر برای حمله می‌سازند. از طرفی، تهدیدها فقط از بیرون نیستند و می‌توانند از داخل شبکه یا زنجیره تأمین شکل بگیرند.
هدف جمهوری اسلامی از قطع اینترنت، امنیت نیست؛ بلکه قطع ارتباط مردم است. تجربه هک‌های سریالی سامانه‌های داخلی هم نشان داده که ایده ایزوله‌سازی، رویکردی منسوخ است.
حکومتی که صنایع فولادش به‌خاطر نرم‌افزارهای قفل‌شکسته هک شده و سامانه سوختش به‌دلیل استفاده از ویندوز سرور منقضی از دسترس خارج شده، چطور ادعا می‌کند می‌تواند با چیزی که اینترنت ملی می‌نامد، امنیت ایجاد کند؟
👉
telegra.ph/Internet-shutdowns-do-not-create-security-04-25
©
AManafii
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2219" target="_blank">📅 22:28 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2218">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">از صبح با خودم کلنجار رفتم که امروز نگم چندمین روزه اینترنت رو بصورت سراسری در ایران قطع کردن، ولی واقعاً نمیشه سکوت کرد. یه عده که یا شکم سیرن یا خودشونو زدن به نفهمی، با چسبوندن یه مشت توجیه پوشالی مثل امنیت و تدبیر و از این مزخرفات، چشمشونو بستن روی این همه فشاری که به زندگی مردم اومده؛ کسب‌وکارهایی که خوابیدن، آدم‌هایی که بیکار یا تعدیل شدن، حقوق‌هایی که عقب افتاده، سفره‌هایی که هر روز کوچیکتر میشن، و دردسرهایی که برای کار و درس و آموزش درست شده.
بعضی چیزا رو نباید گذاشت از یاد برن. مثل ده‌ها هزار نفری که دی‌ماه قتل‌عام کردن؛ امروز هم پنجاه‌وهفتمین روز از قطع سراسری اینترنته. ۵۷ روز خاموشی دیجیتال، زیر سایه جمهوری اسلامی ادامه داره.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2218" target="_blank">📅 22:12 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2217">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نحوه راه‌اندازی SlipGate برای مدیریت تانل‌های DNS و راه‌اندازی کانفیگ‌های DNSTT، NoizDNS، Slipstream، VayDNS و NaiveProxy ...
👉
youtube.com/v/lRYVud1TKQU
💡
t.me/ircfspace/2074
©
iranux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2217" target="_blank">📅 17:15 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2216">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NT6eGlRo66jMutCZNJpBkdocov-cnaz9bYJRTshGP4pWT7q-h3BIjxz811vf-GSHBteIeHCGJexXY0wTtu6zYEy8WDOG94XSEOm0TvtWTrYndDrd7JvOfcnvAWL4-_-bqVLG5wGeZZVQCxmYY0sHf6PBLa9X-1eyHKyuGXzYHyl4qb5UFMBa5xSMo-w190KvCjHRKx8pmz52JzzWpoYmvvUCZEGzHv73pS_LoFBOWVhl7Lnd9FYQwBmVWD1xNicyJ1pLcJdxhzbC16vAuo0Rr2_F9-ML8Jl3UrXlaHkc_feBKh597XFHCR4yv-_-_GjUfR8pTbDe2j9SbxJZ9NoHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اندک کاربردهای پیامرسان‌های رانتی بومی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2216" target="_blank">📅 16:43 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2215">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z6rKkJue8LYx6qIaTiCCjqH9Uy5HFCF0R-T0JKF8vcanENiRbHiRV7NHC278y_AmzoPfkttKYsIYaTS4LBjCZexM9zofSQef50OXT3OfNr-CjaqZHlyVAdWILZKe8--8HJ5IGrBu1oVyzzcj75GZYhoKNCjrcDPP8M_OLWyGmutbnMtx4gE29n7qux5ekRQkqzhnpIP-Owm5aTn3gd3cq1L8JGJf0Ny0iGcEuLauITvYzxW9iIyrDhG3BKWCI72AGm-7KSdEl84n9jWZtLw0hoXejN2hElXkSTDO2ZzjnAT63X_fcdzrZdfg-gs9vNdWZDWMHJlJoHr844bOYIh1_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرتون کدوم VPN فروش در این شرایط می‌تونه حداقل ۶۰ هزار کاربر رو پشتیبانی کنه، پولش مستقیما از صرافی ایرانی بیاد و مستقیما به صرافی ایرانی واریز داشته باشه
و به تخمش نباشه
؟
©
mah_azadi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2215" target="_blank">📅 09:21 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2214">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قطع سراسری اینترنت در ایران به روز پنجاه و ششم رسید.
هنوز بعضیا منتظرن همون کسی که این وضعیت رو ساخته، خودش از سر لطف حلش کنه، اما واقعیت اینه از ظالم نمیشه انتظار داشت با دست خودش بساط ظلمش رو جمع کنه!
این وضعیت اینترنت یک شبه ساخته نشده؛ سالها قدم به قدم، با سیاستهای تدریجی، زیرساخت همین اینترنت طبقاتی رو چیدن. هر گشایشی هم اگر اتفاق بیفته، نه از سر مهربونیه و نه دلسوزی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2214" target="_blank">📅 09:19 · 04 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
