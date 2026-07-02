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
<img src="https://cdn4.telesco.pe/file/YI0GtSt8hTVbTAqnttD0ozQm4pszOccuYQS7N5l55qH5Px_ViJ04Kn5PvRar7_yLyWxoWPM-Mm2pcaZ-dJXiicUEct6eh0D8_jzHi2NJzBs7Ss9QATfHfdbXStRwaC5XPLaOmvToElmZMI3WHPyXGxWmJtxAjiKp3XVawBmRVcRFCUbboR3akn0YKTpFH1j1VqUqUSewsPwLACHUi23iRMI-04tuxwwQdzzW3QWOzPzQyAMoSuNyyq6ufeeB8rdWFqvS2-g-U-UIJgUEyv3uZBCJQ5dqS8428KLi6UsuP5sM0rl0aAB-GFxoUmLLOoj7qsy3LyS8wWDje21pTCWDrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 09:53:06</div>
<hr>

<div class="tg-post" id="msg-131388">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
آمریکا: در پی فرود اضطراری یک فروند بالگرد «ام اچ-۶۰ اس سی هاوک» در دریای عرب، یک نظامی آمریکایی مفقود شده و سه تن دیگر زخمی شدند
🔴
تحقیقات درباره چگونگی وقوع این اتفاق ادامه دارد
🔴
هیچ دلیلی در دست نیست که نشان دهد این حادثه، ناشی از اقدام خصمانه بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/131388" target="_blank">📅 09:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131387">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
واژگونی قایق گردشگری در پاکستان با ۷ کشته و یک مفقودی
🔴
پلیس پاکستان اعلام کرد که روز گذشته (چهارشنبه)، پس از واژگونی یک قایق گردشگری در ایالت «خیبر پختونخوا» در این کشور، هفت نفر جان باختند و یک نفر دیگر نیز مفقود شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/alonews/131387" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131386">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بلومبرگ: عبور نفت از تنگه هرمز، ۱۰ میلیون بشکه را رد کرد
🔴
یک مقام آمریکایی شامگاه چهارشنبه مدعی شد که حمل و نقل روزانه نفت از طریق تنگه هرمز، از ۱۰ میلیون بشکه فراتر رفته و ۵ میلیون بشکه نفت دیگر هم از طریق مسیرهای جایگزین منتقل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/alonews/131386" target="_blank">📅 09:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131385">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
انتقام روسیه از حملات کی‌یف
🔴
روسیا الیوم با اشاره به حملات روسیه به اوکراین اعلام کرد: حملات شبانه روسیه به کی‌یف یکی از شدیدترین عملیات‌های اخیر مسکو بوده و در واکنش به حملات کی‌یف علیه زیرساخت‌های غیرنظامی روسیه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/131385" target="_blank">📅 09:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131384">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سایت The War Zone با استناد به گزارش‌های محلی اعلام کرده است که هر شش بمب‌افکن استراتژیک B-52H Stratofortress حاضر در پایگاه RAF Fairford در بریتانیا، پایگاه را ترک کرده‌اند و احتمالاً به ایالات متحده بازگشته‌اند.
🔴
دوازده بمب‌افکن استراتژیک B-1B Lancer همچنان در پایگاه باقی مانده‌اند که این تعداد نسبت به هجده بمب‌افکن استراتژیک قبلی کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/131384" target="_blank">📅 09:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131383">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeVTa6l2K-TQxLZtxVZIf33FV-lQEpeY1wmaIt9fUsTIWQnmz2sI4vUJIvIcGjPr-_8gL3uKJ3iqsL6gIjUdM-tPVGj_nlJ7L2fxBrH7ZcZZ3VSg7mFaZNWh7bFd8pHrsFqAHD92TJrc7muTvGRawDHHfQ3RVk4NBlg5k4z3RVu9jqD2JiGWxvKjSuCMzEzATlY-QEsVU4DwlJIR_UFJUSahuJ_tZfSwwWBNJngUfvU4wypB6gVavXVDWhBePVUAW7JfYfPmSeSeaHeEmq1Ezk7xD8Yc6ExJ_IFmNCrFLNzQtB9poLhBMWOtAByTIcGp2GYZ6IIdIiMXXCxVgp2GcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی خطاب به قالیباف: هوچی‌گری هم حدی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/131383" target="_blank">📅 09:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131382">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سی‌ان‌بی‌سی: ایران از زمان لغو محاصره دریایی توسط آمریکا در ۲ هفته پیش، بیش از ۴۰ میلیون بشکه نفت خام صادر کرده است.
🔴
‌تهران اکنون نفت را با ۲۰ درصد حق بیمه می‌فروشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/131382" target="_blank">📅 09:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131380">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3197e89311.mp4?token=Cnw15RSRjUP8AIAX7sGlTmOKq-Elv59sPa0KG_Tj2PfnTE-TBDQ8L8miku2WxlRNyd_DRXK1SKAydIYJTqfyVhi4Wawk9qPVL9CDEjX1SsboY9Pj416zmH07_JrbYW9F87CpeXxdhVOoLxyfjAKJmZihnFPspNfYIYvPeH0Ppcsdvuk-LT5Ai2eb8oqCkqPwAuRg0hBa2fPTOIh7oN6zeBQ0Wg0nubQwMI6mHNfxmpsKyB-jZD1jURbMnM89d9OoxczN0LhXpy0TAPVJ0k2d6q134-qWWuwBeTZlE5FuxpA1dUm-Dy2YdaemlGON75ZPrtT0nfjBiiZ1v1sG0X77Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3197e89311.mp4?token=Cnw15RSRjUP8AIAX7sGlTmOKq-Elv59sPa0KG_Tj2PfnTE-TBDQ8L8miku2WxlRNyd_DRXK1SKAydIYJTqfyVhi4Wawk9qPVL9CDEjX1SsboY9Pj416zmH07_JrbYW9F87CpeXxdhVOoLxyfjAKJmZihnFPspNfYIYvPeH0Ppcsdvuk-LT5Ai2eb8oqCkqPwAuRg0hBa2fPTOIh7oN6zeBQ0Wg0nubQwMI6mHNfxmpsKyB-jZD1jURbMnM89d9OoxczN0LhXpy0TAPVJ0k2d6q134-qWWuwBeTZlE5FuxpA1dUm-Dy2YdaemlGON75ZPrtT0nfjBiiZ1v1sG0X77Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراینی‌ها پیش از حمله گسترده موشکی و پهپادی ترکیبی روسیه، در متروی زیرزمینی کی‌یف پناه گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/131380" target="_blank">📅 08:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131379">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رسانه‌های محلی فلسطین گزارش دادند : قایق‌های جنگی اسرائیل به سوی سواحل «خان‌یونس» در جنوب نوار غزه تیراندازی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/131379" target="_blank">📅 08:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131378">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از دستیاران نخست‌وزیر عراق مدعی شد: ایالات متحده انتقال دلار به عراق را از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/131378" target="_blank">📅 08:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131377">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سازمان امنیت دولتی یمن در سازمان ملل: حوثی‌ها با حمایت ایران بیش از ۱۸۰ حمله به کشتی‌ها انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/131377" target="_blank">📅 08:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131376">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lObHzGpiZY8s-Do_SUFGeU1EgjHPIsrobJrqrYxUvizIoKIyZlkXfDWsoXvhyhmacW6BFxaApbsuKsM7z-HFL0iOKoVf9LGF5JowJ4KIJDATQTUPbzFWX5KrxOj-_0xExavg4YUd3GLagjaNyT1-nskwAkDPPD716J2kZHBWJIhiIboNQlARX0n0Iw1bPeSoBFo9vCOrZq6O9nbvJut2l3JWA_QL5BHDq0K19gIKmOGBTdA5n2_NBFYl2GEbwDVTVbNIz4Zv0SL02chlpclQ6CaJIubAVjabSlFt3jg8awidMdKEPLXveutPkJ57w912C4ylVoMkVLvY5bpKUQv01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: تنگه هرمز زیر فرمان ایران تعریف می‌شود نه سنتکام
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/131376" target="_blank">📅 08:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131375">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
الجزیره: ایران پس از مذاکرات دوحه، کانال ارتباطی برای نظارت بر تفاهم‌نامه با آمریکا ایجاد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/131375" target="_blank">📅 08:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131374">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یک منبع ارشد به العربیه: به ایران اجازه داده خواهد شد تا محصولات کشاورزی آمریکایی را با بخشی از پول‌های مسدود شده‌اش خریداری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/131374" target="_blank">📅 08:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131373">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بخشایش اردستانی،نماینده مجلس: تجمعات شبانه باید فورا جمع بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/131373" target="_blank">📅 02:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131372">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_ZbgHv2lHsMpyX3vlm5JpROd0m9EVg7Gs1weVg6Ion3yv25rhU75HVE8PCZeafK2rGN9PbzJHoB2OyWrcXS_9z6tgUn6v4myI1Hja7eQfAxr4tL3ucIimW7RdkfcDEG50ME9Oop2ljnhj4E-Vjk3NdxsHEuYu7PhrCR6eF5AQiwJ0xzSLpKSt6GYnd9Uiv4JYJYJ6WjZ0MUaTZAhMJ0IA-eZD64W9J4LstRy14VTiYb96Pev-WyoXBXjAMtY25q_7hKtKucs0CKODBXfLmahXZoYNES1APDQfhHhKjOBxciuclpLcPOVd5_lzh4HSmLRgAutIbOVEeGE2A4tRF9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش ایالات متحده آمریکا اعلام کرد که در پی فرود اضطراری یک فروند بالگرد از نوع «ام اچ-60 اس سی هاوک» در دریای عرب، یک نظامی آمریکایی مفقود شده و سه نظامی دیگر خدمه این بالگرد نیز زخمی شده اند که وضعیت جسمانی آن ها پایدار گزارش شده است.
خبرگزاری «رویترز» به نقل از ارتش آمریکا همچنین تاکید کرد که هیچ دلیلی در دست نیست که نشان دهد این حادثه ناشی از اقدام خصمانه بوده است.
در بیانیه ناوگان پنجم نیروی دریایی آمریکا آمده است: «شناورهای نیروی دریایی هم اکنون در حال انجام عملیات جست وجو در منطقه برای یافتن یکی دیگر از اعضای خدمه پروازی هستند که همچنان مفقود است. همچنین تحقیقات درباره چگونگی وقوع این حادثه ادامه دارد.»
در این بیانیه همچنین آمده است که این بالگرد در منطقه بر روی ناو هواپیمابر «یواس اس جورج اچ. دبلیو. بوش» مستقر و به مأموریت اعزام شده بود.
فرود اضطراری بالگردها روی آب می تواند حتی برای خلبانان با تجربه نیز بسیار خطرناک باشد؛ زیرا بالگردهایی که بخش فوقانی آن ها سنگین تر است، هنگام برخورد با آب معمولاً به واژگون شدن متمایل می شوند و ممکن است به حالت وارونه در آب قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/131372" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131371">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
حادثه امنیتی در ناو هواپیمابر جورج اچ دبلیو بوش در نزدیکی ایران و دریای عرب.
🔴
نیروهای نیروی دریایی آمریکا در جستجوی یک عضو خدمه مفقود شده از هلیکوپتری هستند که از ناو هواپیمابر جورج بوش برخاسته و در دریای عرب به صورت اضطراری فرود آمده است.
🔴
سه نفر از چهار عضو خدمه هلیکوپتر با موفقیت نجات یافته‌اند و در عرشه ناو هواپیمابر در حال بهبودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/131371" target="_blank">📅 02:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131370">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzSsbHmXGVBdL-OuwLdzyCiWCLGXVKnVjUWNGg_pflJktJMXS88y1YEU93ShR_nSdVS_GRBOcGn5sY8YvPky5gZy34VTtqvtJiscr55TQJpHBuY1cQvTO9nVRzCttuYyeLbzyumJlBFI0LfUCWiNMmhwOcHiVX1OifAZWdUwCMdXi8s-jbpWoyKBq95kjXG44zBnMHB80lPNRcSXHX3pXd0JSyuykiyUujmdhfDdP-YvvExQ2kflver3JaLgiFa7fN8oxwLDsW-3UNDnv2_DApA7JrU6OKQbeivVYA-GwCDTEtZZjUdlKB-OrsSIO9Lk9Kz6Pcc8LeGhBCwZRGv63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: برای مراسم‌ تشییع، همه مردم بیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/131370" target="_blank">📅 02:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131369">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm.m</strong></div>
<div class="tg-text">کشور ایران از بیخ فاسده
میترسن یکیو برکنار کنن اونیکیارو لو بده
پس نتیجه میگیرن داخل ی سفره بشینن و بدزدنو بخورن
فوتبال هم اینطور شده</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/131369" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131368">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزیر ورزش عربستان سعودی پس از حذف تیم ملی این کشور از جام جهانی، رئیس فدراسیون و چند مدیر ورزشی این کشور را عزل کرد، همچنین سرمربی تیم هم اخراج شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/131368" target="_blank">📅 01:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131367">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/131367" target="_blank">📅 01:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131366">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbuJ6P6Qz9A0rSC4YAugnorBL2aKfW4akEz1B0BIbOJ9VS-fvMbnfhZh0zYA9PiiWakWlUDM3gtmpOCqN_dHd0bhoFS48fmZDb1Gh03Cl49x2btrfZ0jfavFlb3araqpwVnOsoEKMIMhR_WWWUqD4ub_Ax7P0LQwwyrSMry7940OPjEf_E5OnUAoBQCilvTr3RVDvx6skg1Kv4rDzkZTy1-R5_53ztd7dczXZdHgd-XS6YE8Vw-7MZjhDgEiX0-0gw9moyGKxxFugcM4NPst4FvMhWuxCf6dgJrR6-aDYU6LulvYPYNswCs9IWy8XgdMmwU8Wz8yl7MmO_4QNshNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به تاج و اعضای فدراسیون که رفتن به جام جهانی مجموعا بیش از 50میلیارد تومان حق ماموریت داده شده
🔴
فک کن بری جام جهانی و بهترین هتل مفت بخوری و تیمت هم برینه و ۵۰میلیارد هم بگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/131366" target="_blank">📅 01:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131365">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
تاچ: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/131365" target="_blank">📅 01:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131364">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il8Az0nSsXyAE-QrZ6Xw6Obilu2mO9QRVGqbFPWmycB6T9JJEMalCWulI-c94PFg8xx5plPthHkjMhtWheKBrrEZxVdZqpcAeWf5KBNRT3f1tRySrZKcYDtfYODNb_k0hgHNVm-yxP2HyJo-VhsBbgqXjSCGGAw9MEOCoeVOmho7EzWyVK0DPq4WN44Pz1MXk1m_jcBbNdT5aQxkqkg0aDS3CZOdQ1jec-AqMUAfRkhmLJJqW6nuYvL-V4afV-EbtxnLpRULdrvDTnbVWsjKLrg2fUhsEJF0iSEfjz_HpK6wcM3V6YS_4OedBedelagry4UIbIFCbuVwXw0ylErPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاچ: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/131364" target="_blank">📅 01:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131363">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🎙
فردوسی پور:
نکنه پس‌فردا صبح با سوییس بازی داریم ما خبر نداریم اینا خبر دارن که مراسم استقبال گذاشتن!
@AloSport</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131363" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131362">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3740efe365.mp4?token=QA-4ArkTyivfDjQoioRcpjkSd5BB7f4lUVZUDwNM4MkdOATp37tgLbmjC33M0fuuZRXOrMrVTjK6lbT2sa2G8N2rKDbGO16hY0B1IaaqvWxfT9jSdGqPvPSxmuywRBS4ZSanH1HV9B9rpLJ2vBp7GbAODn0DFKqbMIzRFZ9cFYNakFlVVptGfh1LqlaR4WDm9ewljXxyt9UQPsOeRCjWt7xy_gr0_cG8FTmQwou_bSNlq3UKz6zX5g--bGaOByOlE2ftYfFjFxhCbztVcQY7pL5dWZDqfdFXhcwsLqcCtGgGvwPKB4puIV5-uOQIAHdA9a8srUF8It2VLpJTtY0FoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3740efe365.mp4?token=QA-4ArkTyivfDjQoioRcpjkSd5BB7f4lUVZUDwNM4MkdOATp37tgLbmjC33M0fuuZRXOrMrVTjK6lbT2sa2G8N2rKDbGO16hY0B1IaaqvWxfT9jSdGqPvPSxmuywRBS4ZSanH1HV9B9rpLJ2vBp7GbAODn0DFKqbMIzRFZ9cFYNakFlVVptGfh1LqlaR4WDm9ewljXxyt9UQPsOeRCjWt7xy_gr0_cG8FTmQwou_bSNlq3UKz6zX5g--bGaOByOlE2ftYfFjFxhCbztVcQY7pL5dWZDqfdFXhcwsLqcCtGgGvwPKB4puIV5-uOQIAHdA9a8srUF8It2VLpJTtY0FoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صداوسیما جوری داره از قلعه‌نویی تعریف میکنه که خود قلعه‌ هم تعجب کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/131362" target="_blank">📅 01:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131361">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=sjdOGFYygPTdqgNIeCvoZUlaBfFj8cpQldwIqhetd-uSbPuccSXkE8c1SOEwAT_D4HLHw21h95pRO_jOYh2Zd7KnY27xDDtFfZ1ourZfgtL1qUBRGSyEA8kH-Z4ssW1Eua8JAafXlSFDKMVT__9z-iliQNm_6734MgPyYkJrqUFul8uUiZu-xXwK4EQAbLFxJvV6lYLSARI_gy71xO0UlKcAHCb-XdUuaOSAB5mUfyJWCPjfve6J2BVRA7jusSEk5yJ6qNCQnC2tv2Uawkycx_k-INm26ZySp-VcVcVwVBo0hiI5y3_YtbmbC-W768U38qC94C9ZBO_mKV9S5HahFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=sjdOGFYygPTdqgNIeCvoZUlaBfFj8cpQldwIqhetd-uSbPuccSXkE8c1SOEwAT_D4HLHw21h95pRO_jOYh2Zd7KnY27xDDtFfZ1ourZfgtL1qUBRGSyEA8kH-Z4ssW1Eua8JAafXlSFDKMVT__9z-iliQNm_6734MgPyYkJrqUFul8uUiZu-xXwK4EQAbLFxJvV6lYLSARI_gy71xO0UlKcAHCb-XdUuaOSAB5mUfyJWCPjfve6J2BVRA7jusSEk5yJ6qNCQnC2tv2Uawkycx_k-INm26ZySp-VcVcVwVBo0hiI5y3_YtbmbC-W768U38qC94C9ZBO_mKV9S5HahFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
@AloSport</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/131361" target="_blank">📅 01:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131360">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLjsyMHsXi00sW6WNi36AbN8gKhvktrcLQV81gCnA0c7DIFvyzbuChlIJzArcelqUrcrT8O5C7JR35Ly5ZAKzMqCV_v1WGYRkq_uXCEVyqZouXnHk8q2eM-BlBbKGLLhfvHXeAxlyB_mHagqyjQZWi3_T3dmKDcedOemAsa_dTpyTMUdsex5JSM5NVqEI7CN__p3YlI9Fs0O5jAELbsoZc8pPbR1Y0zu0436RMlxlzzN85DWdO5FhIdELVb8Jf5Cw-ECGLBxUJ0n_q3cgC2jm1A61ipKh2wGHMWlN8wBtWOIpzKoy508385LL2jkafE8MgZ9RB4yj0bF-EQT_jvbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع رسانه‌ای گزارش دادند: مقر احزاب تجزیه‌طلب در منطقة «ديكلة» واقع در شمال عراق هدف دو حمله پهپادی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/131360" target="_blank">📅 00:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131359">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
هم اکنون حمله پهپادی به سمت اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/131359" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131358">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ:  در مورد کوبا، پس از دهه‌ها و دهه‌ها، به سمت ما می‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/131358" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/386c345efc.mp4?token=cT95tthDFhXP6ibOcu9xj0FGDoVyAnxBiydgnytc9mJ8QpeHBTHLTQmijx0cdJS-0C2_G3J4sKUyD63kkhteBAPYAZVwl0IK6Bpi3nnO6b0m3oP3YiVlxg3Ux1EeuBnPzkCiuoKsYMCR5maAF-69gYlTtIbnCNuJkBFr1P5_uikPWHcJIcrMLyOJaXL363AJTyT4z2x2d2nNS1rRD1AvQSvk6R5_vn22sbIrJ5ALpwwoNFMaWdFvwEhfJceVGHtzUmKPu0of9xaUi1HWqQh-JspB5NBETInecI59VRLTbVBvS8nFZcXm7ArEaxTBt0a7wHFOfGhEW90t9bVc9QcNIxLLOsWTHr1MOk0l8kY0FfJxJsFBAyWDgFMZuywhDR7w010qfx2Gzs6RP5g8gAyVSslRoBnrw-yjtbIGcxhV7wdbmLfn98e9_jJ5rhoLE1SqGGTGcLVJ3874EQoU9CWd5z4CbQzu3cSWTord_tGs7wQB5yqb9nO0Qk9LORsjrIhMk7hpLhSSYfIvIfeYOD0bGLczvm4qh8Yoinu0JcvClJbsHr0SuT-XyMzwQZS8yknUVYcwa6h_L1UIt-FLou1rbVcZ_G_E4gAvixWt4zcHEd1fQzTVI4ITR1I-DRHejsCXb0YuIwRY9jlUI55wyb43Fo75QU9L4i1v129KNgzD6fM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/386c345efc.mp4?token=cT95tthDFhXP6ibOcu9xj0FGDoVyAnxBiydgnytc9mJ8QpeHBTHLTQmijx0cdJS-0C2_G3J4sKUyD63kkhteBAPYAZVwl0IK6Bpi3nnO6b0m3oP3YiVlxg3Ux1EeuBnPzkCiuoKsYMCR5maAF-69gYlTtIbnCNuJkBFr1P5_uikPWHcJIcrMLyOJaXL363AJTyT4z2x2d2nNS1rRD1AvQSvk6R5_vn22sbIrJ5ALpwwoNFMaWdFvwEhfJceVGHtzUmKPu0of9xaUi1HWqQh-JspB5NBETInecI59VRLTbVBvS8nFZcXm7ArEaxTBt0a7wHFOfGhEW90t9bVc9QcNIxLLOsWTHr1MOk0l8kY0FfJxJsFBAyWDgFMZuywhDR7w010qfx2Gzs6RP5g8gAyVSslRoBnrw-yjtbIGcxhV7wdbmLfn98e9_jJ5rhoLE1SqGGTGcLVJ3874EQoU9CWd5z4CbQzu3cSWTord_tGs7wQB5yqb9nO0Qk9LORsjrIhMk7hpLhSSYfIvIfeYOD0bGLczvm4qh8Yoinu0JcvClJbsHr0SuT-XyMzwQZS8yknUVYcwa6h_L1UIt-FLou1rbVcZ_G_E4gAvixWt4zcHEd1fQzTVI4ITR1I-DRHejsCXb0YuIwRY9jlUI55wyb43Fo75QU9L4i1v129KNgzD6fM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مدال افتخار
:
من پسران زیبایم را می‌بینم. فکر می‌کنم می‌خواهم یکی را به خودم و یکی را به آن‌ها بدهم و یک سه‌نفره خواهیم داشت.
🔴
من به آن‌ها مدال افتخار کنگره را برای چیزی می‌دهم... برای نبوغ آن‌ها در شکار.
🔴
و من یکی را برای پذیرش «روسیه روسیه روسیه» یا چیزی شبیه به آن دریافت خواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/131357" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ: کشتی‌ها با تعداد بی‌سابقه‌ای که تا به حال کسی ندیده است از تنگه هرمز خارج می‌شوند، ما در حال ثبت آمارهای بی‌سابقه هستیم و قیمت نفت در حال کاهش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/131356" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=MLZQATgGTHYVcYNCUOjr92B6lUERsGKDU6xOg2T9QLlt14Vu9got_yvlDq_CKga6erz5-8Ind7175mx3LAIFZsOnU0EDLYiL2SJ0BPmbDJ3o2CFtR_DEmoYMNRGI3Yyap56Fbd6QZSlNq3bvyLiiNjaxqwpRPiDZgYS7X3WPxHeuOedGVp3t_UtjRd256ARtcXfmZR1y8zAy2274tle5gNhtmPZdRslwJN78VmuYHu4HCfxC3xhwUYmjKYqpyLbH16LghiVQjv0onBuywL0NlNeBoxJLxNkLkUuGuG1ITCU6j5UuIxvcMHSZUbfI6vZy7zOqfdFsccuRKp2KaK7BY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=MLZQATgGTHYVcYNCUOjr92B6lUERsGKDU6xOg2T9QLlt14Vu9got_yvlDq_CKga6erz5-8Ind7175mx3LAIFZsOnU0EDLYiL2SJ0BPmbDJ3o2CFtR_DEmoYMNRGI3Yyap56Fbd6QZSlNq3bvyLiiNjaxqwpRPiDZgYS7X3WPxHeuOedGVp3t_UtjRd256ARtcXfmZR1y8zAy2274tle5gNhtmPZdRslwJN78VmuYHu4HCfxC3xhwUYmjKYqpyLbH16LghiVQjv0onBuywL0NlNeBoxJLxNkLkUuGuG1ITCU6j5UuIxvcMHSZUbfI6vZy7zOqfdFsccuRKp2KaK7BY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : کنترل کامل. ما کنترل کامل همه چیز را داریم.
🔴
این فقط آغاز دوران طلایی آمریکا است.
🔴
بهترین‌ها هنوز در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/131355" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=ZtbzlRBiShOYqk2cFeKfdgkl2_dpmm6I2t6CO0CXDCloIp966LAFz55b2rCg4zeJVZmlY--uSYi4AkY0g3UQmBP6U4mg54bd5r0a6X1JZZZWlCJaDCzptNc6vbRyuNU6HEz88EBNNjkdSyTgIFQGLrDb0xfv10ngv5NZJa3Ohs91oE5duuiD-S_kStqR0F0_g_RaQ3SiREWNnO_aXLkPyWtlNNEGSz-jjuZvG5HZVyCJO6ADKFjhi0NPaz7_pyPjpCL5G1XSQTP485jKF7pwnzVpyIuWrVVCDspNUY4zVcuwFSOK-GLim5EFuugnP2FgFcCRjW6hgZB0HTQtqmdi0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=ZtbzlRBiShOYqk2cFeKfdgkl2_dpmm6I2t6CO0CXDCloIp966LAFz55b2rCg4zeJVZmlY--uSYi4AkY0g3UQmBP6U4mg54bd5r0a6X1JZZZWlCJaDCzptNc6vbRyuNU6HEz88EBNNjkdSyTgIFQGLrDb0xfv10ngv5NZJa3Ohs91oE5duuiD-S_kStqR0F0_g_RaQ3SiREWNnO_aXLkPyWtlNNEGSz-jjuZvG5HZVyCJO6ADKFjhi0NPaz7_pyPjpCL5G1XSQTP485jKF7pwnzVpyIuWrVVCDspNUY4zVcuwFSOK-GLim5EFuugnP2FgFcCRjW6hgZB0HTQtqmdi0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما بزرگ‌ترین زیردریایی‌های جهان را می‌سازیم.
🔴
ما در زمینه زیردریایی‌ها و دیگر موارد ۱۵ سال جلوتر هستیم
🔴
ما دوباره با کشتی‌ها شروع خواهیم کرد. قبلاً روزی یک کشتی می‌ساختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/131354" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131353">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
اکسیوس: آمریکا تلاش دارد ایران را از دریافت عوارض از تنگه هرمز منصرف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/131353" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131352">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ae0f5149.mp4?token=fn9OpLVPtPHqiWWsVNOsPP1OJ9yd_w4TGB0S2lw-xj9Dg9i4oX-YXpT8MLmvSfzgv2fSXv-IpqoCJcFUj5vJu2QqiTLAxg6iaaAY5LlHLCDVH3p2P6JXj5Yh2N2p68YOWWdBQM56tjbfZ0S6VfCSCCulQ5TZZoWL1ojkU3NFtRnRrV4GinyBi-b-X86H7vb0AjzPfESSM8BEnhQigwO9Izn-bKK5wyRXPdXqaIo6MJfUKpaF-RiY-xTw3REXacy35vY0j4h2FldU0gGniuHiBOWCq2TCtjwqXaYCAqlSUrlAykYDS4vf5E2OggJjVNOCAoY0uTAfd0Ynx5tVu3C_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ae0f5149.mp4?token=fn9OpLVPtPHqiWWsVNOsPP1OJ9yd_w4TGB0S2lw-xj9Dg9i4oX-YXpT8MLmvSfzgv2fSXv-IpqoCJcFUj5vJu2QqiTLAxg6iaaAY5LlHLCDVH3p2P6JXj5Yh2N2p68YOWWdBQM56tjbfZ0S6VfCSCCulQ5TZZoWL1ojkU3NFtRnRrV4GinyBi-b-X86H7vb0AjzPfESSM8BEnhQigwO9Izn-bKK5wyRXPdXqaIo6MJfUKpaF-RiY-xTw3REXacy35vY0j4h2FldU0gGniuHiBOWCq2TCtjwqXaYCAqlSUrlAykYDS4vf5E2OggJjVNOCAoY0uTAfd0Ynx5tVu3C_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اسپانیایی‌ها — اعضای ناتو اما نه اعضای خیلی خوبی از ناتو.
🔴
آن‌ها به خوبی رفتار نمی‌کنند، اما یاد خواهند گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/131352" target="_blank">📅 23:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131351">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
جی دی ونس: در حال حاضر، مذاکرات به خوبی پیش می‌رود
🔴
کسانی که به دولت به‌خاطر مذاکره حمله می‌کنند، همان افرادی هستند که ما را تشویق می‌کردند چند بمب دیگر هم روی جاهایی مثل افغانستان بیندازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131351" target="_blank">📅 23:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ
:
عربستان سعودی و دیگران در حال نگاه کردن به چین و سایر کشورها برای محافظت از آن‌ها در طول دوره مدیریت بایدن بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/131350" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131349">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cca332fee.mp4?token=qDjcF_KsyJM6FZa9URbDELYmp5bMex4hxq7ANXVHBWBWAfmuv3AliOMFNwukUFn3zTwhIrEURna8XyNXMnVuutAm-WIBwjOvYg51ykcSEWMXZayiMYIAPnnc2HGLCAJDV76JX6hQKXQhGzLi81GLZkztxHfr5qr3dAuFQKrO95Nxn74Y4ry9IGWEBjW3qppOn7rLHDA_pYIlrOv_yWYrZUrkt3zTXXUBub_ivvvCnaRItkabM59uGMc_W6ZZkSf-E3XzlB1615PVTQcqBVLkMmhhFE4TYdQsNz_WWkLoyArFCULADErBhi6amJz1NulxMRYF94W9n-5Y_16sJHqJ7jEapxDyIgjeppOuVcuw40FJzKQI5bfagGMhL45DYNaiI-FjEjVLYj8YMjzkADATLMIr-lNPPNTAOMbHNaSRemJuSVyCk_16DXvQLVHxIPQK51iuWRKVtruIzePZQ1M2VHty-OpzSzk5g5frC-_kycbvtLNoj4QLEt6pBvQIKdkAcpfESOe-zbBh4buEu-CXBKK9AgyrBtCbTxH6nkluK9uY3ff2o5NGDiVl-D1Ekqogx5rX4bLPQBbMlFNoAhgKSnwN6EvyOpS7_IJ-63rASbUfXSrf9lTQrTl7_BF36GU6Y7wR6TlkozBL1DL6c4VOf_ssiq_XvOjmk4PJEetsl-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cca332fee.mp4?token=qDjcF_KsyJM6FZa9URbDELYmp5bMex4hxq7ANXVHBWBWAfmuv3AliOMFNwukUFn3zTwhIrEURna8XyNXMnVuutAm-WIBwjOvYg51ykcSEWMXZayiMYIAPnnc2HGLCAJDV76JX6hQKXQhGzLi81GLZkztxHfr5qr3dAuFQKrO95Nxn74Y4ry9IGWEBjW3qppOn7rLHDA_pYIlrOv_yWYrZUrkt3zTXXUBub_ivvvCnaRItkabM59uGMc_W6ZZkSf-E3XzlB1615PVTQcqBVLkMmhhFE4TYdQsNz_WWkLoyArFCULADErBhi6amJz1NulxMRYF94W9n-5Y_16sJHqJ7jEapxDyIgjeppOuVcuw40FJzKQI5bfagGMhL45DYNaiI-FjEjVLYj8YMjzkADATLMIr-lNPPNTAOMbHNaSRemJuSVyCk_16DXvQLVHxIPQK51iuWRKVtruIzePZQ1M2VHty-OpzSzk5g5frC-_kycbvtLNoj4QLEt6pBvQIKdkAcpfESOe-zbBh4buEu-CXBKK9AgyrBtCbTxH6nkluK9uY3ff2o5NGDiVl-D1Ekqogx5rX4bLPQBbMlFNoAhgKSnwN6EvyOpS7_IJ-63rASbUfXSrf9lTQrTl7_BF36GU6Y7wR6TlkozBL1DL6c4VOf_ssiq_XvOjmk4PJEetsl-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما اجازه نمی‌دهیم کمونیست‌ها راهمان را ببندند.
🔴
آن مردم، کاری که انجام می‌دهند، واقعاً احمقانه است. آن‌ها واقعاً احمق هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/131349" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131348">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709087d4a8.mp4?token=aK7xOaoiqPHEDi6lCIPjFatG7NXU6kaULhNqhS3OczjdKbRo75D6qMdn_RjQiA1AlYp02oPuGuYSMsXGbwllsv3JfrwGVi9L79kzK1X3wUJpoTo9hNE-6gnmRtdziMT8kcPcvn3Wpz7-wgDvGLQVS_5ZWI7R1lRWkItENpq6hkuKjlEz0iVuHL25PDhlNEZ7Ke9lUcLeXVKTbyhT-O6a-M7wHZjAHLFQKTVMOfprn4LH0OwW1MUuPjR9MaQBq2sXeGv9dCX8wCWDITBLL-HQH4QaMHHSY4G7cCmZSpLYExWpwLzY7ZchTFvGdhYMRtluc6u_ZOvzEgRo4lEaIBV07A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709087d4a8.mp4?token=aK7xOaoiqPHEDi6lCIPjFatG7NXU6kaULhNqhS3OczjdKbRo75D6qMdn_RjQiA1AlYp02oPuGuYSMsXGbwllsv3JfrwGVi9L79kzK1X3wUJpoTo9hNE-6gnmRtdziMT8kcPcvn3Wpz7-wgDvGLQVS_5ZWI7R1lRWkItENpq6hkuKjlEz0iVuHL25PDhlNEZ7Ke9lUcLeXVKTbyhT-O6a-M7wHZjAHLFQKTVMOfprn4LH0OwW1MUuPjR9MaQBq2sXeGv9dCX8wCWDITBLL-HQH4QaMHHSY4G7cCmZSpLYExWpwLzY7ZchTFvGdhYMRtluc6u_ZOvzEgRo4lEaIBV07A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
در 4 جولای، دمای هوا تقریباً 107 درجه خواهد بود.
🔴
و من می روم، و یک سخنرانی واقعا طولانی دارم فقط برای اینکه نشان دهم که می توانم هر کاری انجام دهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/131348" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131347">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600b8e0075.mp4?token=sI6IoD3V-EKRp9dWB570M0Wl2oDucLLoIjSnSbIYne_sGMmnClz4KL9LkNDkrk6CvtR60j3hZ58I592N_qJaKdlu6lAOwx6G8YtiiIMSWLEcflOiRp6KI4GoFFqDMFeJD0L1P6JqJuOMcubknVI7FDg5-8YdY6NpZGml-EtqCX7bnN0i8midsBDqzZvKOrH2Y3MTgu8N78ta7wk5kaVMLaCbS8OU3WiVJT7w4at6PoWotK5E56u9V9BdbOj7JVd2jLOIcNRSbcy4eW9d7bA9mLX0o-mgN6WkfRHxWw1p1Z-wnIxGobFjgIXp_6s6Ua9iVi3wIyRHTwmo0YpUCq_KBnlGC97IHFJeJqaegk_Xl4ztkUJr0EII4BtuosPFwRI_vz3tfAZXDOCPOkcmUM1cVAUoDeOoETz1NbO1DX5tNnzIBTagil-jyOlR2JzF78wq59Yqwn0AcfoZN2itIjt-zTnN9kUGzAtsWT0Q44adkTyhHeB6GHzYo1d4pJ_9pCcNgaNabDvCGFMbZsaQWLUHmJKi3CNCE8mIME3qs9HWRic0fDXltSGmARfu0-V_AiespE7zhQXa7ShHsUkcEfeg20lYddAezVqW0D1hDguVijjPfhmqsWy7C9EljEZh0KkGmGa0ujD6MjmXfbb-Aftc0M6ONDWSOekLhqsCJDWcBaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600b8e0075.mp4?token=sI6IoD3V-EKRp9dWB570M0Wl2oDucLLoIjSnSbIYne_sGMmnClz4KL9LkNDkrk6CvtR60j3hZ58I592N_qJaKdlu6lAOwx6G8YtiiIMSWLEcflOiRp6KI4GoFFqDMFeJD0L1P6JqJuOMcubknVI7FDg5-8YdY6NpZGml-EtqCX7bnN0i8midsBDqzZvKOrH2Y3MTgu8N78ta7wk5kaVMLaCbS8OU3WiVJT7w4at6PoWotK5E56u9V9BdbOj7JVd2jLOIcNRSbcy4eW9d7bA9mLX0o-mgN6WkfRHxWw1p1Z-wnIxGobFjgIXp_6s6Ua9iVi3wIyRHTwmo0YpUCq_KBnlGC97IHFJeJqaegk_Xl4ztkUJr0EII4BtuosPFwRI_vz3tfAZXDOCPOkcmUM1cVAUoDeOoETz1NbO1DX5tNnzIBTagil-jyOlR2JzF78wq59Yqwn0AcfoZN2itIjt-zTnN9kUGzAtsWT0Q44adkTyhHeB6GHzYo1d4pJ_9pCcNgaNabDvCGFMbZsaQWLUHmJKi3CNCE8mIME3qs9HWRic0fDXltSGmARfu0-V_AiespE7zhQXa7ShHsUkcEfeg20lYddAezVqW0D1hDguVijjPfhmqsWy7C9EljEZh0KkGmGa0ujD6MjmXfbb-Aftc0M6ONDWSOekLhqsCJDWcBaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: کانال پاناما گران‌ترین چیزی بود که تا به حال ساختیم و همچنین سودآورترین چیزی بود که تا به حال ساختیم. این ترکیب خوبی است.
🔴
کمی شبیه ونزوئلا. ما در واقع با جمهوری اسلامی ایران هم به همان اندازه خوب پیش می‌رویم. شاید شنیده باشید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/131347" target="_blank">📅 23:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131346">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: اخبار جعلی اخیراً نسبت به من بسیار مهربان بوده‌اند.
🔴
وقتی شما همان کاری را انجام می‌دهید که ما انجام می‌دهیم، آن‌ها باید مهربان باشند، حدس می‌زنم.
🔴
من حتی با تئودور روزولت صحبت کردم.
گفت: «نظر شما درباره کانال پاناما چیست؟ آیا آن را بزرگترین دستاورد خود می‌دانید و در مورد این واقعیت که دموکرات‌ها کانال پاناما را به قیمت ۱ دلار به پاناما دادند، چه حسی دارید؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131346" target="_blank">📅 23:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131345">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: اجازه نمی‌دهیم چین آبراه پاناما را تصاحب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/131345" target="_blank">📅 23:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131344">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8648b6f7.mp4?token=E4HU6PUhvRchw9Rx7BBtolGSemXYJdQLR0wiUzOhna7fFvil3HoFlDgX-7vcv5bH_HDcPTRFsaHNdvRQ4LcxfRoPVb49esK72pQLwkwb9uPXYW1RPEtO0vNh5rmKFoNsxlFNRmt7Nh64enN7nEl7IOj3ESdV73TRYjy9gIwVeCRbPrThaEUu1mcStdwAOKXiutuX6i8tOifj6dnPjiQUGSr5aB7vInpGI7cRcMv11kqnXlONYxe82C9jkBbqNnZpuRTtV6UOEnvyVUo6q5T_9QfWjU7bEK2wz8whnawP8oQtiT0SBtMWYYq_TEeb7NjRB4ZPRcNmvsTDleDNr801bkQ0SBxnpVpuSN_KmMzOePQhaa426l1MtYE85vxelWkgiykF8aeEpFhMmzPPxdnFHjfXWH9Ix5dtdRbjmvnwtg_Hz0RIavtiDWMUEdQz1Q7JzRFMAIGEcyaiwXCIBh-KrVYPPZQdL2bmczpmhMnDhDvz07edkY5jDjZMBkAr8KqW70eyl6zq0tTk7O1PVM98T6AFhSg8eZrGG62FBupnLEt4T-ytnUivTaJrM_ynPu8yHq4qbS-gr3gDENknO96W6mFio1qTUBM3T6yfQDB-CV-sDhVrMGj5Osp26ozt7ik3PJEX27IBmFqXWJoHtXDs5ms7GGGWqQGwopoVLvSqm-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8648b6f7.mp4?token=E4HU6PUhvRchw9Rx7BBtolGSemXYJdQLR0wiUzOhna7fFvil3HoFlDgX-7vcv5bH_HDcPTRFsaHNdvRQ4LcxfRoPVb49esK72pQLwkwb9uPXYW1RPEtO0vNh5rmKFoNsxlFNRmt7Nh64enN7nEl7IOj3ESdV73TRYjy9gIwVeCRbPrThaEUu1mcStdwAOKXiutuX6i8tOifj6dnPjiQUGSr5aB7vInpGI7cRcMv11kqnXlONYxe82C9jkBbqNnZpuRTtV6UOEnvyVUo6q5T_9QfWjU7bEK2wz8whnawP8oQtiT0SBtMWYYq_TEeb7NjRB4ZPRcNmvsTDleDNr801bkQ0SBxnpVpuSN_KmMzOePQhaa426l1MtYE85vxelWkgiykF8aeEpFhMmzPPxdnFHjfXWH9Ix5dtdRbjmvnwtg_Hz0RIavtiDWMUEdQz1Q7JzRFMAIGEcyaiwXCIBh-KrVYPPZQdL2bmczpmhMnDhDvz07edkY5jDjZMBkAr8KqW70eyl6zq0tTk7O1PVM98T6AFhSg8eZrGG62FBupnLEt4T-ytnUivTaJrM_ynPu8yHq4qbS-gr3gDENknO96W6mFio1qTUBM3T6yfQDB-CV-sDhVrMGj5Osp26ozt7ik3PJEX27IBmFqXWJoHtXDs5ms7GGGWqQGwopoVLvSqm-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره داگ برگام، وزیر داخله:
فکر می‌کردم بسیار تأثیرگذار باشد. راستش را بخواهید، فکر می‌کردم همسرش کاترین حتی تأثیرگذارتر باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/131344" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131343">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641158562d.mp4?token=iyPdCq15vn9pu1m3gdsyFoopuDW2BOCOZVx6pIQjpeTLSuvOIB8rk4MtlO8gMAUCVdf8U9lZfoTI3Q_yPEcH_PMzANJA0cqp0qxbApLFmdhMivveF0MadNtyqQs6UOfMZ9DVBnvDEJu3zVsWVn69SUgq1fncSMMrRYlH5pmgf4LJy216xgF6BCv1Dtm2NCawaCbBurvvHDS-UHfnTd4h9rX-FXDXw4AINmyxLIN_f2JSaPout5oDTqWJsNo9sf7BR2nAt0ADNCZL5hO1Q05qRVvrnxNuQGoO73VxmAJC920P9uH3UFvWu16XW4KdUFPzwDSKMC9FA5sQoO7oMld4QIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641158562d.mp4?token=iyPdCq15vn9pu1m3gdsyFoopuDW2BOCOZVx6pIQjpeTLSuvOIB8rk4MtlO8gMAUCVdf8U9lZfoTI3Q_yPEcH_PMzANJA0cqp0qxbApLFmdhMivveF0MadNtyqQs6UOfMZ9DVBnvDEJu3zVsWVn69SUgq1fncSMMrRYlH5pmgf4LJy216xgF6BCv1Dtm2NCawaCbBurvvHDS-UHfnTd4h9rX-FXDXw4AINmyxLIN_f2JSaPout5oDTqWJsNo9sf7BR2nAt0ADNCZL5hO1Q05qRVvrnxNuQGoO73VxmAJC920P9uH3UFvWu16XW4KdUFPzwDSKMC9FA5sQoO7oMld4QIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من دو تله‌پرامپتر (دستگاه نمایش متن سخنرانی) دارم که کار نمی‌کنند، و اینجا ایستاده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/131343" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131342">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
قالیباف علنا به تندروها گفت خفه بشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/131342" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131341">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید.
🔴
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/131341" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363ab4d62a.mp4?token=Wxa4r53ppiRPX-mPvddKiKmoGVwDG5NCvqfUPsYCVHxwHlZGBVdbbjuhEqXTVzK9JW9b5Z4IASXGifRYZM0fHFacGFzMB9lIQIqsa9OYuJ_HsiY0nxJJoBzEpcYdn8PwXdQWCM_H9NfAjy14Gish2yvlhvz37bD91t95UOBVxgfJF48CHw5RJfdVM63oeqydzfvp65yydclCqbNLYXGWHTa4eCU0lstSZRaWYM6DdJ3cSpPq8DpYLt9M7JO0m3Zqjxl6yPRBAib0WNzboJK-_teUVy5dD2i5Ij3r0HVshcj9PB_zplyNLqK8J8xV93nW8Kd51KXtG1SNFwlBjj6wFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363ab4d62a.mp4?token=Wxa4r53ppiRPX-mPvddKiKmoGVwDG5NCvqfUPsYCVHxwHlZGBVdbbjuhEqXTVzK9JW9b5Z4IASXGifRYZM0fHFacGFzMB9lIQIqsa9OYuJ_HsiY0nxJJoBzEpcYdn8PwXdQWCM_H9NfAjy14Gish2yvlhvz37bD91t95UOBVxgfJF48CHw5RJfdVM63oeqydzfvp65yydclCqbNLYXGWHTa4eCU0lstSZRaWYM6DdJ3cSpPq8DpYLt9M7JO0m3Zqjxl6yPRBAib0WNzboJK-_teUVy5dD2i5Ij3r0HVshcj9PB_zplyNLqK8J8xV93nW8Kd51KXtG1SNFwlBjj6wFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «باید به شما بگویم این پرواز افتتاحیه‌ی هواپیمایی به نام ایر فورس وان پس از ۳۷ سال بود. این یک هواپیمای عالی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/131340" target="_blank">📅 23:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
قالیباف: ما خودمان در مجلس قانون تصویب کردیم؛ شورای عالی امنیت ملی هم مصوبه دارد. بر اساس این قانون، به هیچ عنوان به سایت‌هایی که بمباران شده و آسیب دیده‌اند، دسترسی داده نمی‌شود. این قانون است.
🔴
ما هیچ امتیازی بیشتر از دسترسی‌هایی که شورای عالی امنیت ملی تعیین کرده، نمی‌دهیم. طبق قانون، تعیین سطح دسترسی‌ها بر عهده شورای عالی امنیت ملی است و آن هم چارچوب آن را مشخص کرده است.
🔴
در حال حاضر، آن‌ها فقط در دو مورد حق دسترسی دارند؛ یکی نیروگاه بوشهر و دیگری راکتور تهران. دسترسی‌ها فقط در همین حد بوده است و ما نسبت آن متعهد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/131339" target="_blank">📅 23:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند
🔴
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/131338" target="_blank">📅 23:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
قالیباف : می‌خوام تو سفر به چین
روابط تهران و پکن رو قوی‌تر کنیم و به سطح یه شراکت راهبردی برسونیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131337" target="_blank">📅 23:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131336">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
قالیباف: مذاکره‌ای بین ایران و آمریکا وجود نداره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/131336" target="_blank">📅 23:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131335">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
تا کنون رسانه های خبری گزارش داده اند رشاف در نزدیکی بنت جبیل و بیت یاحون در نزدیکی صور توسط ارتش اسرائیل مورد هدف قرار گرفته اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131335" target="_blank">📅 22:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131334">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ از هوش مصنوعی تئودور روزولت می‌پرسد: آیا کانال پاناما را بزرگترین دستاورد خود می‌دانید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/131334" target="_blank">📅 22:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131333">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0VTfWo03Ua2QYw-Wv8wn1-SvxaEklyY9_c_ZfHf3cX9w5TjF3AkBB0aX4lwf8qdJrqFUw5OB1Eq1dVlICBJcL7-inQnLf1zNQmRNI9xC_DeynczuNz7saQ7p1xQaQt1td_r0FwYYtdwtuSu5cdKAvi4IsSmB-7Abyf_Bsi_H0CeKAYzPc5Mrw9RiUeqlE-hih-DHJ9aYlCBsGtIzhxDCMOx2XZQPDin8R-4eqjRpXA1GJmntBqXPvZXiozMyb_tV4z4zpyAD3OsljCklfM8say4549g7kru44Iqo6T97p9_ws6f8eG67XwvD6ws5zoUTLgsTiir-tTs_9g18ftl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/131333" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131332">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نخست‌وزیر لبنان: به‌دنبال تعیین جدول زمانی برای خروج اسرائیل از لبنان هستیم
🔴
نخست‌وزیر لبنان گفت اولویت بیروت در دورهای بعدی مذاکرات، تعیین جدول زمانی برای خروج اسرائیل از لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/131332" target="_blank">📅 22:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131331">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نخست وزیر ایتالیا: من ضد آمریکایی نیستم اما در مقابل ترامپ زانو نمیزنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/131331" target="_blank">📅 22:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131330">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
قالیباف: مذاکره‌ای بین ایران و آمریکا وجود نداره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/131330" target="_blank">📅 22:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131329">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❤️
دیدار رضا پهلوی با گروهی از قربانیان سازمان مجاهدین خلق، جوانانی که دوران کودکی و نوجوانی خود را در «کمپ اشرف» در عراق گذراندند.</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131329" target="_blank">📅 22:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpXeq9fiu-R285Zd_xcFX7oN6oPYDREkBQ98sipskHeR1H0g9pBkmLTVXL8s76kSNYG78Eeb-C0_LEMKZ4cUmGcYkiTSDQHNSfE17p2TJIzeDc82SC_BglO2noA6bSHwsPWY5kIrgqVyF6wkWRxETqHIk3UA5V8nS4c57H8BP4q_bS_GOmfcFobv1kFlbdoQ5YnmfqKqe79vdYy35PlD7W2gxlYaVIlHVQwKdK-UTRWo230V764khaGbVh3Hj7GnZ7tfVtNHmziiwFVXuEsVVOqoid-MfG7_6z2kXQCxMMc8EJpBFeD4IRwqNMzBOpeYm_aHWqVXTkJcHEFIff5_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم ایران اسفند ۵۷ وقتی دیدن براشون قبض آب و برق اومده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/131328" target="_blank">📅 22:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
➕
قبل از خرید، کانال رضایت رو ببینید خیالتون راحت باشه
🌱
@vpn_express_supp
🔄
در صورت بروز مشکل یا نارضایتی، موضوع از طریق پشتیبانی بررسی و در صورت احراز مشکل، مطابق شرایط سرویس رسیدگی خواهد شد.
🤖
خرید سریع
:
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/131327" target="_blank">📅 22:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
سرویس VPN (V2Ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
پنل اختصاصی (مشاهده حجم و تاریخ انقضا)
✅
سازگار با تمام دستگاه‌ها و اینترنت‌ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
تمدید و خرید مجدد بدون تغییر کانفیگ
✅
بدون محدودیت تغییر دستگاه و IP
🛠
پشتیبانی تا پایان اشتراک
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/131326" target="_blank">📅 22:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131325">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پزشکیان: اگر لازم باشد نه 20 میلیون بلکه 100 میلیون بشکه نفت به نیروهای نظامی می‌دهیم، این وظیفه من است و به آن افتخار میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/131325" target="_blank">📅 22:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131324">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f1501b9d.mp4?token=tL9rxlh67rKkVY25H9ZmmxQjlK0l4jVZ1giljmZ5JOqTZmdCjMsDCBWJKjhfIMn0kDXe4C3oRNIA-vqGvNj4WK7YoBEo6NiK-8NbXd_ZCY4IA6iiBTQ0ZKU5580Uzs2kyYqAh9e35wLOrot026xFiTlmvSQXZu7nIjd3VL3GyFJoN9VZ00KVqnApl2qL85do55vXlZYbh03G1yZxImNN_K_w2CY_PsliNJmveDb9iqjQGhKAYgHkPuGzmWqcgBr-PWwi7_PWwxbsn0MasHMUfb08SLJHG_TW3vDl1ALNiMoS2A-nLB-haIlm40w79WPaaqFoTlm9g5FgrgER6sDo_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f1501b9d.mp4?token=tL9rxlh67rKkVY25H9ZmmxQjlK0l4jVZ1giljmZ5JOqTZmdCjMsDCBWJKjhfIMn0kDXe4C3oRNIA-vqGvNj4WK7YoBEo6NiK-8NbXd_ZCY4IA6iiBTQ0ZKU5580Uzs2kyYqAh9e35wLOrot026xFiTlmvSQXZu7nIjd3VL3GyFJoN9VZ00KVqnApl2qL85do55vXlZYbh03G1yZxImNN_K_w2CY_PsliNJmveDb9iqjQGhKAYgHkPuGzmWqcgBr-PWwi7_PWwxbsn0MasHMUfb08SLJHG_TW3vDl1ALNiMoS2A-nLB-haIlm40w79WPaaqFoTlm9g5FgrgER6sDo_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خورخه رودریگز، رئیس مجلس ملی ونزوئلا، گفت که تعداد کشته‌شدگان در نتیجه زمین‌لرزه‌های هفته گذشته به ۲۲۹۵ نفر رسیده است.
🔴
او افزود که ۱۱۲۶۷ نفر زخمی شده‌اند، ۱۲۸۴۱ نفر آواره شده‌اند و ۶۴۶۱ نفر نجات یافته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/131324" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131323">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dece196b7d.mp4?token=roDkD8OxJRORFRE8KXCZ5SZ-CkqBsWvDuDa8IaxUzKWyWpFDrNqKdnN-gHd0tIB0DT3vp0OnTqnnuxmphvsrWfEzmtyXNTifbMp5wIkefi4caQXuC0LhxHkDHgREeDFjk50Pq9JHCspMD0IvXiuug-65Ni24TMt6D5p_2obE7jSPM-GmYKf8H69-g0xBKMfqQpMhwlPXSLcWADsF2RcpOhyioEf1Ch7gmUIDiyKV40FY7iJ16gy0OTwC8JL-_DG97SNQ3Re7j14PbYY3Mtj16OogSk9lfvGqnqDn_vZ9JxMKSu28ILRnJeeF2s6lWQQTSqWKfsnObxxHT35myyMMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dece196b7d.mp4?token=roDkD8OxJRORFRE8KXCZ5SZ-CkqBsWvDuDa8IaxUzKWyWpFDrNqKdnN-gHd0tIB0DT3vp0OnTqnnuxmphvsrWfEzmtyXNTifbMp5wIkefi4caQXuC0LhxHkDHgREeDFjk50Pq9JHCspMD0IvXiuug-65Ni24TMt6D5p_2obE7jSPM-GmYKf8H69-g0xBKMfqQpMhwlPXSLcWADsF2RcpOhyioEf1Ch7gmUIDiyKV40FY7iJ16gy0OTwC8JL-_DG97SNQ3Re7j14PbYY3Mtj16OogSk9lfvGqnqDn_vZ9JxMKSu28ILRnJeeF2s6lWQQTSqWKfsnObxxHT35myyMMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ با قطار آزادی وارد داکوتای شمالی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/131323" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131322">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/131322" target="_blank">📅 22:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131321">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رویترز گزارش داد که مقامات فرانسه تجمع منافقین در پاریس را بخاطر تهدیدهای سلطنت طلبان لغو کردند.
🔴
خبرگزاری رویترز گزارشی از طرف نهادهای اطلاعاتی فرانسه را رویت کرده که در آن به تهدیدهای فعالان سلطنت طلب به بر هم زدن گردهمایی مجاهدین و حتی تهدید به بمب گذاری اشاره شده است. ظاهرا بر اساس این تهدیدها بود که دولت فرانسه تصمیم به لغو تجمع مجاهدین گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/131321" target="_blank">📅 22:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131320">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b73eec92a.mp4?token=lvAkTj0oPqqRpdcOYMt161BNO4w0en5qGQcqvo8c8zRy6zfhjPLHMFJsiAJOHRNdMbgPo3BfwnHtOTb-BLbXYHYYw8KO7cjZdohbxcxc00haDWKvc24BP13r3NKyk5RVoMIAEUryvlnUS2vr7YXz3o5zMgzLxPIiUBvbSclbRL3RazvHi1QF1ImdClLLJYRLRMxgbOQzcFPlCgG5QVcH3bgYB4bbfm7-h7sjbJSiscSGzPOmsIq_c5Y9DIAqyeQtttmqKYyrlJz9dIui5hXwaDko7BHsVjwGb_LQKusM29HPGcSVeMkALB7p3fA9761MJqRULo3CbUzbpGOHJ-F6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b73eec92a.mp4?token=lvAkTj0oPqqRpdcOYMt161BNO4w0en5qGQcqvo8c8zRy6zfhjPLHMFJsiAJOHRNdMbgPo3BfwnHtOTb-BLbXYHYYw8KO7cjZdohbxcxc00haDWKvc24BP13r3NKyk5RVoMIAEUryvlnUS2vr7YXz3o5zMgzLxPIiUBvbSclbRL3RazvHi1QF1ImdClLLJYRLRMxgbOQzcFPlCgG5QVcH3bgYB4bbfm7-h7sjbJSiscSGzPOmsIq_c5Y9DIAqyeQtttmqKYyrlJz9dIui5hXwaDko7BHsVjwGb_LQKusM29HPGcSVeMkALB7p3fA9761MJqRULo3CbUzbpGOHJ-F6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، نتانیاهو، درباره تیمی که در جام جهانی فیفا طرفدار آن است:
تیمی که من به‌ویژه دوست دارم، تیمی است که امروز در جنوب لبنان دیدم.
🔴
فرماندهان ما، سربازان ما، این ذخیره‌ها — آن‌ها قهرمانان جهان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/131320" target="_blank">📅 21:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131319">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8845591e.mp4?token=Q2zMhrbBfq2UihntIF_C919gmvp0GDi4ZTcayhcEO0M1VyZ23RF_ZiyRtnOBLspxnzxdDRlyyvSS-cmK2fX28eQ5W3n-gJv4VHSyLxP_fV7z7MEanFm0t11smqcnklLaihZ4YQXs1oyvCYwO9uv8y5pcIaGpMarbLCJU4G8CBJhp1MJEk_eeoStPgw4vjQk7Cadks47T0iO6dPkYgIYeGKpZqKyVOZ1ucuW0NSM3XqFupB7uF81lCSgzrV64Xb2_n3uPai921t2oCWn0mLM3DElvjsBTSZ6tDvDnW-UcWKqxIz_4KTtDtVdX-1kgPp-1cfE9krCpfGc8Wyxx9VZ-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8845591e.mp4?token=Q2zMhrbBfq2UihntIF_C919gmvp0GDi4ZTcayhcEO0M1VyZ23RF_ZiyRtnOBLspxnzxdDRlyyvSS-cmK2fX28eQ5W3n-gJv4VHSyLxP_fV7z7MEanFm0t11smqcnklLaihZ4YQXs1oyvCYwO9uv8y5pcIaGpMarbLCJU4G8CBJhp1MJEk_eeoStPgw4vjQk7Cadks47T0iO6dPkYgIYeGKpZqKyVOZ1ucuW0NSM3XqFupB7uF81lCSgzrV64Xb2_n3uPai921t2oCWn0mLM3DElvjsBTSZ6tDvDnW-UcWKqxIz_4KTtDtVdX-1kgPp-1cfE9krCpfGc8Wyxx9VZ-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: ممکن است روسیه امروز صلح را در اولویت خود نبیند.
🔴
ما آنها را وادار خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/131319" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131318">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
عضو هیأت رئیسه مجلس: حتی اگه آمریکا گندم رو به ما ارزون‌تر هم بفروشه، نباید از این کشور خرید کنیم.
🔴
نباید پول به جیب قاتلان رهبر بریزیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/131318" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131317">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/131317" target="_blank">📅 21:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131316">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی:
پیام آمریکا در دوحه به ایران این بود که «بزرگ‌تر فکر کنید؛ رفع تحریم‌ها در چارچوب یک توافق گسترده‌تر ۱۰۰ برابر ارزشمندتر از اخذ عوارض از کشتیرانی است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/131316" target="_blank">📅 21:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131315">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رویترز به نقل از مقام آمریکایی: در مذاکرات دوحه به تفاهم رسیدیم که تا هفته آینده آرامش اوضاع حفظ شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/131315" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131314">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خبرگزاری رویترز در گزارشی اختصاصی به نقل از دو مقام اروپایی و اسناد محرمانه گزارش داده است که آموزش مخفیانه نیروهای روسیه در چین در سال ۲۰۲۵ با تایید مستقیم وزیر دفاع روسیه انجام شده و دست‌کم چهار ژنرال ارشد روس و چینی در آن مشارکت داشته‌اند
🔴
به گفته این دو مقام مشارکت فرماندهان ارشد روسیه و چین در این آموزش‌ها از اهمیت راهبردی همکاری نظامی دو کشور حکایت دارد؛ همکاری‌ که در اروپا با نگرانی دنبال می‌شود اما چین آن را انکار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/131314" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131313">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اکسیوس: طبق گفته یک منبع منطقه‌ای، در جریان مذاکرات دوحه، مذاکره‌کنندگان آمریکایی به طرف ایرانی اطلاع دادند که قصد دارند به مهار اسرائیل ادامه دهند و اطمینان حاصل کنند که تل‌آویو به آتش‌بس در لبنان پایبند می‌ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131313" target="_blank">📅 20:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131312">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
معاون وزیر امور خارجه ایران: در نشست قطر تصمیم گرفته شد که بخشی از ۶ میلیارد دلار دارایی‌های مسدود شده برای خرید کالا بر اساس نیازهای ایران استفاده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/131312" target="_blank">📅 20:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131311">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5882311cc9.mp4?token=kYjeSqxcw1HThidhhFvfZiOqOKFvECDYZlSOtTASlSv_33Ps3X_EIcKwuXje0JBW1gJ2lIO9lnqUAEU7uZkVMWlax71HW2EnWRnYr5aPamIJHJ2vgiKFhcXCSivm7kPtRxXA3BwJMHU2z9eKkyw8MRcO7dOMG7e0pEisClutFXtlD__srjjbR7lrK3Dxnt-cUeY9zbj5gGZm0WDQO1fIkdpJ5yiOPbWxeZgcIwwyajXQ4xdtwv1zLguMC3WmNEOrBDpIdtg43x7hYWufcSHQMYF5Xf4MrL7gQRPkDU5Z_arfyH-SPCF6CUEo0FYWzb8MSuNkXQ61fj4JL5ZyDidKdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5882311cc9.mp4?token=kYjeSqxcw1HThidhhFvfZiOqOKFvECDYZlSOtTASlSv_33Ps3X_EIcKwuXje0JBW1gJ2lIO9lnqUAEU7uZkVMWlax71HW2EnWRnYr5aPamIJHJ2vgiKFhcXCSivm7kPtRxXA3BwJMHU2z9eKkyw8MRcO7dOMG7e0pEisClutFXtlD__srjjbR7lrK3Dxnt-cUeY9zbj5gGZm0WDQO1fIkdpJ5yiOPbWxeZgcIwwyajXQ4xdtwv1zLguMC3WmNEOrBDpIdtg43x7hYWufcSHQMYF5Xf4MrL7gQRPkDU5Z_arfyH-SPCF6CUEo0FYWzb8MSuNkXQ61fj4JL5ZyDidKdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اساس گزارش Kpler، تردد کشتی‌ها از تنگه هرمز بین ۲۹ تا ۳۰ ژوئن بدون تغییر قابل‌توجه ادامه داشته است.
🔴
در این بازه زمانی، ۳۴ عبور تأییدشده ثبت شده که شامل ۱۷ کشتی در هر جهت بوده است.
🔴
با وجود باز بودن و فعال بودن مسیر، رصد ترافیک دریایی همچنان دشوار است؛ زیرا کشتی‌ها از مسیرهای مختلف از جمله آب‌های ایران، عمان، مسیرهای ثبت‌شده در سازمان و همچنین مسیرهای بدون سیگنال یا ناشناس استفاده می‌کنند.
🔴
همچنین، سامانه ثبت حوادث سازمان بین‌المللی دریانوردی تاکنون ۴۹ حادثه تأییدشده در منطقه را ثبت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/131311" target="_blank">📅 20:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سخنگوی ارتش: نیروهای هوایی و دریایی در آماده‌باش کامل به سر می‌برند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/131310" target="_blank">📅 20:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131309">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری / وال استریت ژورنال: آمریکا در حال بررسی خروج نیروهای خود از عربستان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/131309" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131307">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سنتکام: یک گفتگوی منطقه‌ای در مورد امنیت دریایی در بحرین با مشارکت رهبران ارشد نظامی از ۱۲ کشور برگزار کردیم/رهبران نظامی ۱۲ کشور تعهد خود را برای تضمین آزادی دریانوردی از طریق تنگه هرمز تأیید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/131307" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131306">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkxOP_KvbsLKrb6l4IixYyb-AXeEh7hOgakMoqCUljQgdoR1zvBqwMQiQmGZQ-abXXbp81jlGEyrKyMCGkzmxO56jBU_QC5uGrltFI-U_IMNNNp3SO3wHNjK_hhc9jobMTE6HU-LCrMky7NkqDDfNXTlbj0J4VsIUhHPbkT94ekquKClSp-7tvmwzH9eCKanbll0OFJWJtRYwv3fbQX_HHabz324fYsvOQLfC9y8ul_e2stq0Yo7bXHAKEjnVSQ_PFN0-BUr9jGk_L2-Pw5na4ldjCaffJ3I4Y_9UvjfrW4MQGLPDLPNmuf1A5FiPUALIyNDKxFneUIG27fw9DiJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث
: خبر بزرگ! شرکت Micron، یکی از بزرگ‌ترین و موفق‌ترین شرکت‌های آمریکایی، اعلام کرده که ۲۵۰ میلیون دلار در Trump Accounts سرمایه‌گذاری خواهد کرد.
🔴
این اقدام تاریخی که با تصمیم مدیرعامل فوق‌العاده این شرکت، سانجی مهروترا، انجام شده، در آینده نزدیک زندگی بسیاری از کودکان آمریکایی را بهتر خواهد کرد.
🔴
این بزرگ‌ترین سرمایه‌گذاری شرکتی از این نوع است و به میلیون‌ها کودک و خانواده آمریکایی کمک می‌کند تا زندگی خود را با امنیت مالی بیشتری آغاز کنند.
🔴
مایکرون مستقیماً روی کارگران و خانواده‌های آمریکایی سرمایه‌گذاری می‌کند.
🔴
دقیقاً به همین دلیل برنامه Trump Accounts ایجاد شد؛ تا هر کودک آمریکایی فرصت بهتری برای موفقیت داشته باشد.
🔴
سیاست‌های من جواب داده‌اند، آن هم در ابعادی بزرگ. آمریکا از هر کشور دیگری در جهان عملکرد بهتری دارد و شرکت‌هایی مانند مایکرون هر روز این موضوع را ثابت می‌کنند.
🔴
این، عصر طلایی آمریکاست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/131306" target="_blank">📅 20:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131305">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b10b9afb.mp4?token=h-m5HTHEbJzbMh0kk8wECAAEI5CAQP_XFl1nDcghC9xilOUfkn-Z1-qQrVibgZToSFtb3bcvwCG5-qj9wPw0q722PS2Mw2zOnk8K01GsTiB79p8d5uXfBX_PT2yHQo6bPNlXj5Tvz4Hdy6R9CsJ6X5--XA4P2rBl1hMmtbeCqUnI5q4cIEUoilcAHKCaemhvKjcGhKSEJeHvwO1fK86tzC_rNeKOyG4mIyqyJ5Y8oUWpBHYaulI59CTFyQb33NqE9V3xnnxbKc8qVFV4QA7hBhbzGuq1RLW8nQ8IxYTNCPz0KCXx-HRhDwxN3Yv2owTZVIr1rF320COyxntn3qwFdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b10b9afb.mp4?token=h-m5HTHEbJzbMh0kk8wECAAEI5CAQP_XFl1nDcghC9xilOUfkn-Z1-qQrVibgZToSFtb3bcvwCG5-qj9wPw0q722PS2Mw2zOnk8K01GsTiB79p8d5uXfBX_PT2yHQo6bPNlXj5Tvz4Hdy6R9CsJ6X5--XA4P2rBl1hMmtbeCqUnI5q4cIEUoilcAHKCaemhvKjcGhKSEJeHvwO1fK86tzC_rNeKOyG4mIyqyJ5Y8oUWpBHYaulI59CTFyQb33NqE9V3xnnxbKc8qVFV4QA7hBhbzGuq1RLW8nQ8IxYTNCPz0KCXx-HRhDwxN3Yv2owTZVIr1rF320COyxntn3qwFdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل با یه پهپاد به منطقه «نَبطیه الفوقا» تو جنوب لبنان حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/131305" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131304">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3583560ed.mp4?token=mR4rwm_j5MZvqq2ae3B3GyMKZ0lNtryq6pDO996FzthD7NpIvfu9uo8gyTZT2FWbF2MOUbXa6nrp4cKrzbdiDa13tcQb_3DoT5J4nexuR3lVxbhmLo-wfSNPAYHlOr1NNfNa_p2ElJaQH4n5LpHjC4BzfvLsBd16YVCrOSx9Gc169ptEtsEZmWxjPtG4CXv6pdLV16OGtW2AOcINCvVk63RY9rz_Wn7Ou195OUOLrPkFmhs3MA8CUFnY0GMukNjPbdJjYlypzS0ZY6EmhYMIvJ8Rv2WlY3d-KU6T2e35FG8RkBbsR6VdMvvFrBo4vp0I2NV8voMVGtC_B3Rnxs83Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3583560ed.mp4?token=mR4rwm_j5MZvqq2ae3B3GyMKZ0lNtryq6pDO996FzthD7NpIvfu9uo8gyTZT2FWbF2MOUbXa6nrp4cKrzbdiDa13tcQb_3DoT5J4nexuR3lVxbhmLo-wfSNPAYHlOr1NNfNa_p2ElJaQH4n5LpHjC4BzfvLsBd16YVCrOSx9Gc169ptEtsEZmWxjPtG4CXv6pdLV16OGtW2AOcINCvVk63RY9rz_Wn7Ou195OUOLrPkFmhs3MA8CUFnY0GMukNjPbdJjYlypzS0ZY6EmhYMIvJ8Rv2WlY3d-KU6T2e35FG8RkBbsR6VdMvvFrBo4vp0I2NV8voMVGtC_B3Rnxs83Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیر رولکس: بعد از بازی با مصر خواستم بگویم فوتبال [با ما سر ناسازگاری دارد] اما اشتباهی گفتم خدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/131304" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131303">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرنگار: آیا می‌توانید متعهد شوید که آمریکا تا پایان مهلت ۶۰ روزه این تفاهم‌نامه وارد عملیات نظامی گسترده نخواهد شد؟
🔴
جی‌دی ونس: رئیس‌جمهور ترامپ نیروهای نظامی ما را دوباره وارد جنگ نخواهد کرد، مگر اینکه واقعاً مجبور باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131303" target="_blank">📅 20:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131302">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مقام آمریکایی در مصاحبه با جروزالم‌پست مدعی شد: همان‌طور که در تفاهم‌نامه ذکر شده است، ایالات متحده باید نحوهٔ استفاده از این وجوه را تأیید کند.
🔴
این در حالی است که در هیچ‌یک از بند‌های یادداشت تفاهم اشاره‌ای به این موضوع نشده و در بند ۱۱ آمده است: آمریکا متعهد می‌شود تا وجوه و دارایی‌های مسدود شده ایران را با اجرای این یادداشت تفاهم «به طور کامل» برای استفاده در دسترس قرار دهد.
🔴
مقام آمریکایی همچنین ادعای واشنگتن درباره خرید محصولات کشاورزی آمریکا را تکرار کرد و مدعی شد:‌ در صورت آزادسازی دارایی‌های ایران، از این وجوه برای خرید محصولات کشاورزی آمریکایی از کشاورزان آمریکایی به‌منظور تغذیهٔ مردم ایران استفاده خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131302" target="_blank">📅 19:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131301">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
یدیعوت آحارانوت:پخش اذان ممنوع شد !
🔴
کنست با قرائت مقدماتی بر قانون منع اذان استفاده از بلندگوها را در مساجد شهرهای فلسطینی نشین به بهانه «سر و صدا» ممنوع و آن را تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/131301" target="_blank">📅 19:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131300">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
فارس : صادرات محصولات شیمیایی، پلیمری و پتروشیمی دوباره آزاد شده
🔴
فقط باید طبق همون قوانین و مقرراتی انجام بشه که قبل از محدودیت‌های شرایط اضطراری وجود داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/131300" target="_blank">📅 19:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131299">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ونس: اگر ایران سعی در بازسازی برنامه هسته‌ای خود داشته باشد، همسایگان خود را تهدید کند و از تروریسم حمایت کند، رئیس جمهور ترامپ گزینه‌هایی برای مقابله با آن دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/131299" target="_blank">📅 19:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131298">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2eb6c3904.mp4?token=r97SjvT3lhFJBUuwRj6sywTzwIAV16lOCMrMNEIXmkmgYWBYxm57aKbkIzFrsdRByssB-f7qBXXHOdhjuT0-o-daYOQFrPhe0YShg2Le-IkFvum6NAtQPxJGwjn-KrBBaGz7g80x10WzSS7OvoEPt45fUPAeKdDHxcgWjEYSJYDq2c35CTje7TYKzffH_mnUvErFghRspmKGsnTkKXb4_bktMywK0EF6BOj_XQxE-XjK_9Iohrqzr7Pq-6ezGduaA41Q1jhXZIevkpn4KSMhEQpymxX8uXi9o313uN1ZO4pNkGh6pybSOIn03x2_gP748WX4O-ij-OzzX5b6jXligQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2eb6c3904.mp4?token=r97SjvT3lhFJBUuwRj6sywTzwIAV16lOCMrMNEIXmkmgYWBYxm57aKbkIzFrsdRByssB-f7qBXXHOdhjuT0-o-daYOQFrPhe0YShg2Le-IkFvum6NAtQPxJGwjn-KrBBaGz7g80x10WzSS7OvoEPt45fUPAeKdDHxcgWjEYSJYDq2c35CTje7TYKzffH_mnUvErFghRspmKGsnTkKXb4_bktMywK0EF6BOj_XQxE-XjK_9Iohrqzr7Pq-6ezGduaA41Q1jhXZIevkpn4KSMhEQpymxX8uXi9o313uN1ZO4pNkGh6pybSOIn03x2_gP748WX4O-ij-OzzX5b6jXligQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس درباره ایران: ایرانی‌ها از توسعه بمب هسته‌ای، از هر زمان دیگری در 20-30 سال گذشته، دورتر هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/131298" target="_blank">📅 19:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131297">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZvQzqcGEynpPnh5woP83FFX_C0cJpPUgrJgSOsrm8C-hVTpKmt_UQgtRWM8aNHtVCffKaXBmSdTXxBFH2mBOJREQyimKCSNUwUAlH9thFbpEBjF1zNqhzrQL7y7vMN8CBwvLdZlgcNOU9e74NWUWmXh4wHiYqfqHFYNDzeBEiVFzF8MeKImPV3xdi21iD9CT1l4uZbOKoyo3ud4E3lIj92shCrCoDQVIx_M1emXz4jAssDYML_z3yoi3F7TYSD6QsvfD9qaQG3FcIpicsqAxKqnA5WFh0r6Bqb2c-4gBPDRm4TcAMv05ZpXDa357iWiBNGBE_oqhlDIp5Q-eRtY0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمزه صفوی:
اونایی که میگن آمریکا درحال فروپاشیه و نابودش میکنیم، کصخولن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/131297" target="_blank">📅 19:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131296">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
معاون ترامپ، ونس : ترامپ از شما خواست توان نظامی متعارف ایران رو از بین ببرید و تا این لحظه که اینجا نشستیم، و نیروی دریایی ایران هم نابود شده
🔴
مأموریت شما این بود که برنامه هسته‌ای ایران رو از بین ببرید
🔴
طبق گزارش‌های اطلاعاتی آمریکا، الان ایران نسبت به قبل خیلی بیشتر از ساخت سلاح هسته‌ای فاصله گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131296" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131295">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
آخوند قاسمیان در نقد مقایسه تفاهم فعلی با صلح حدیبیه: شرایط صلح حدیبیه یعنی واشنگتن را اشغال کنید؛ ترامپ را دستگیر کنید و به ایران بیارید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/131295" target="_blank">📅 19:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131294">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک مقام کاخ سفید در مصاحبه با فاکس نیوز: تیم‌های فنی در حال بحث در مورد تمام مفاد یادداشت تفاهم با ایران هستند.
🔴
ترامپ راه‌حل‌های دیپلماتیک را ترجیح می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/131294" target="_blank">📅 19:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131293">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/131293" target="_blank">📅 19:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd8e12a39.mp4?token=IqG9fWQwEgzP1tx8nOU_6XwDr9zEGDotgwwdSBONvxepEI1KQeblEq2PpWxXriJeSEB1VV6ZMPmf4FFfPwbXw3Zv_Myf5TSufox5uzB5xEbCNGNc_v8_qvq5u_zgzIG_GBFVSdWNQxUU_meB4W8G9B3fTcum_W67l5MJQcLGi0-xIFFQyc4biHyt7bZ-_H3Ahk1y33MR6EWS_iy6g3PdjVy6V5iEYfvqlztjjOQn18UsIFkGcXs50Na26kyvRtpekLafeAdkJn5-zCXPBHTerSL2S-fSJDYOwWyTkz2mgydgHwkvfkjKORD74w4AkT64LGTUD6PWC6dc1LE58EuIcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd8e12a39.mp4?token=IqG9fWQwEgzP1tx8nOU_6XwDr9zEGDotgwwdSBONvxepEI1KQeblEq2PpWxXriJeSEB1VV6ZMPmf4FFfPwbXw3Zv_Myf5TSufox5uzB5xEbCNGNc_v8_qvq5u_zgzIG_GBFVSdWNQxUU_meB4W8G9B3fTcum_W67l5MJQcLGi0-xIFFQyc4biHyt7bZ-_H3Ahk1y33MR6EWS_iy6g3PdjVy6V5iEYfvqlztjjOQn18UsIFkGcXs50Na26kyvRtpekLafeAdkJn5-zCXPBHTerSL2S-fSJDYOwWyTkz2mgydgHwkvfkjKORD74w4AkT64LGTUD6PWC6dc1LE58EuIcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خداداد: تیم ما دستاوردی نداشته است
🔴
کره هم شبیه ما بود ولی سرمربیش استعفا داد
🔴
مردم خیلی فهیمی داریم
🔴
سه بازی نباختن دستاورد نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/131292" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtxqLLoAG3vANO_xJulyaQn7A4t_kHkg2M8t72uZ9dYpQ3WeyNYJdiGJZAzvVjdNYYmPcB0_k18kjOUZuOVa0slX9OqYrucopbKbeWXWi8GWMSCtWaePC0UnvPTZHUAoUXG8FVI-c8Oc5J8N8J_K19YHE35AlmRVe0hznC1O2EfwEPyBJqJ-UvWafY_9H33JhW5D1R5kg607WggB-SDXZay7quMu8y_wABl1gkLnqXqdXXJo_zvtl8emYCRK8dThhtccZo-_Cbh4bPuwSYEsXRDtnSU06Njk9o7LgZea2R-o93Jwyz3FO2YcMr9NBIvrtz7xDF123pHDMccRJbbxGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با حکم مجتبی خامنه‌ای، اژه‌ای برای پنج سال دیگه به ریاست قوه قضاییه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/131291" target="_blank">📅 18:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNqxeGQ30iYZ1EdxTrWXtl7yR5AsYAB28oZ3N2eI91WNw8xchpbpKQg_cPe6T3AMivAf4-HuPYRg_qqf4A5TmX9ByG00SdARi9akhhUEePQ9xA4WEbiWsqaQy4pKo95NEOAxOqKtAPgF0BUNbCukq_hccxkUi0dub2tHShxjM73mmgEu-lheFL6WIbgES5DLhiOLx_66bW_CLDOpDNMLUB6OdqprjdsuM1t3uwvx1daMKqOfwLlKsD2B_qpgDTwfUW9UwqVhhdu6U3ob6gGtinXi2XwuxMWO-zXklPFjW7cNTkOSaSI_KMYj_GhVtScAml26A2CUvvGpMbz4j-v4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا قراره به بازیکنان فوتبال به پاس وطن دوستی حواله واردات خودرو لوکس داده شود
🔴
پیشتر نیز به هر بازیکن حدود 100میلیارد پاداش داده شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/131290" target="_blank">📅 18:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131288">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3M1j-zWJnI18U4JqGTh7yK0vgBnQxhwGQVoFoqEAj0FT0MHvd6D9Hvknu6iU4iFu7FlLu4TZerTyyBbktK9INsggOeJUOsX-qygNI7I5mfWJ11zVvNfqVgCE-3R4q2e9vkubRc6qRnnjiyqc18EKPgqCn3NDu3JjdQnvG7DJGvoeHQ5VCsYqRC5G9JUWRRwyNl8XVGnDyiXK8CEmTUs5NYelN7NMjZIK1iyFd-baKlbsOo90edESvAn_GUFILQn5KLxBGNSXbnpSmSoIqvwDLn8TRs1bdApEOO4Gjs8nuLYogPIo5Uug9U_j194aWbuFvfYAtChQ1CpMWDfi-Sgyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mQ7a30iRgbg_aGekdEBP-j8lYxSdvnVEVIFLVv3cv_svrpZuTPsq0r-a1ZM-rzwxuRdck5lyucxCFBNIMQQeXMT6TL_7HwP7eww5FbDKk7r7gxtEJH0XH9_P-qADbHPsmEWumWP4gsTjy9tcw8kO1G_9mUP8RqihoSilYZb9K0q8GLl8XgAXwddjeHRSKGqGzBwUvIHuUymj7FIr7t5C2Yg4qWRO40pvlggRErggAHPBmsmjkBP3Jfy1P4LD1i3yPg9bp0lvRteSuzncO_VmaowYI_NE6VjgHA93SFT4bc6GKXAu_6nZBKuxv0tplrrhUGyFc_C8dSVbt9vq1dZtMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گزارشاتی رسیده عده‌ای بیکار توی خیابون به دخترایی که حجابشون رو رعایت نکردن از این کاغذا دادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/131288" target="_blank">📅 18:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131286">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0c588df71.mp4?token=lYyEWgkvsSJeSbqsUha_IOeljCDX8Ztw84Br1XVUyvWbe0d7tOUtcDMcUiNP53-X2wHAiYLmLCLcZ1zN0JEWaUquKLNK9ASdqBfZdeKLecRzxu75FYrT9inzn53nXmOE9GOQZyxRlbY3muXdQTpeb3PRnejmdWaLca3DLu7kBg2Hfq8wHtFtiiHidSiYiyukXks_GOzjnwpbjePUejWl6ImkSIL5eb9_kE-mDXTEppOkddLZawt1aLu-0249fvV_zySIIOsO3J7LSPnUIdtI672yIiqMW_p-N9JAi485sdg4aIsBONamX273-PX3IqZzpfV4-0PPn6eAmEzCPboR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0c588df71.mp4?token=lYyEWgkvsSJeSbqsUha_IOeljCDX8Ztw84Br1XVUyvWbe0d7tOUtcDMcUiNP53-X2wHAiYLmLCLcZ1zN0JEWaUquKLNK9ASdqBfZdeKLecRzxu75FYrT9inzn53nXmOE9GOQZyxRlbY3muXdQTpeb3PRnejmdWaLca3DLu7kBg2Hfq8wHtFtiiHidSiYiyukXks_GOzjnwpbjePUejWl6ImkSIL5eb9_kE-mDXTEppOkddLZawt1aLu-0249fvV_zySIIOsO3J7LSPnUIdtI672yIiqMW_p-N9JAi485sdg4aIsBONamX273-PX3IqZzpfV4-0PPn6eAmEzCPboR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین یکتا رو یادتونه توی اعتراضات دی ماه اومد گفت بچه هاتون رو بیرون نفرستین، اگه تیر خوردن مسئولیتش با خودتونه.
حالا فیلم تولد پسرش اومده بیرون، میزی از خوراکی‌های متنوع که شاید هیچوقت ما نخوریم.
ماشین های چند میلیاردی که شاید هیچوقت سوار نشیم...
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/131286" target="_blank">📅 18:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131285">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قلعه‌نویی: گل شجاع صحیح بود حقمونو خوردن
🔴
با آمریکا جانانه جنگیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/131285" target="_blank">📅 18:26 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
