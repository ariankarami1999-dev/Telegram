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
<img src="https://cdn4.telesco.pe/file/O-t1YSIPhP7zsgQaoqFWtpnbuxTGgDnmpuBfgh-HapyjnoG83LkaXzmEabjW2c8nNKzDWtsCZJmji8ReQ5mF9v0zPneLGDcozCvG8xhbJDF2YINzCVmRQymJKxKvV14FgufuVsafoGMdmkqrlW9phKGUxfplZKulpccrUcMFbkp7aiuewpTs6HDDlhyn1fFpBwt0V1NVMZjz1Fq4aHrn-KCOPmtNg4Dy6ph9NtNN9XjN8II5z6gLQnl8yMSGCHr3so8VBacfNnh3gC0Hlqt2a30nPEWdT_Vl2QNiCEBIQLMAgfr-eJevd-v9M3W6ZvkowatQsrNDBDOjr-PufcjSJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 10:20:45</div>
<hr>

<div class="tg-post" id="msg-137767">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5721545f.mp4?token=mc5EBc1r88f8Bk2_DKBk8qCLXpig3zu2Bhs-axFwlTc3qN7IhsDA29oJegr55RT871IKzTjCIzQMHIJ8ehr126wbrvXCzuoqHHLDc3CzETqz-mZxvBGsZRqsDuKm1KlE7rvKR3V3ymQGBSXigZIwK3mmn9fP1fKpnBUiJ6ChbbeNewNfgcFzJDkSz6u7paoH61foqiDE2oNx6K89mqzJYeibNLEcj9PTdpnOFQCFJSChVP8hnBsm5LfVnmzkhhkkDbaR1DqPMN-RR0ngm8VmT8gRJfXzdAffNNx43Kx4HVQ2OLD-qF5uPz5jWwjVvQeT2fBL_VB4aje00LUFeLk0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5721545f.mp4?token=mc5EBc1r88f8Bk2_DKBk8qCLXpig3zu2Bhs-axFwlTc3qN7IhsDA29oJegr55RT871IKzTjCIzQMHIJ8ehr126wbrvXCzuoqHHLDc3CzETqz-mZxvBGsZRqsDuKm1KlE7rvKR3V3ymQGBSXigZIwK3mmn9fP1fKpnBUiJ6ChbbeNewNfgcFzJDkSz6u7paoH61foqiDE2oNx6K89mqzJYeibNLEcj9PTdpnOFQCFJSChVP8hnBsm5LfVnmzkhhkkDbaR1DqPMN-RR0ngm8VmT8gRJfXzdAffNNx43Kx4HVQ2OLD-qF5uPz5jWwjVvQeT2fBL_VB4aje00LUFeLk0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
😄
دیشب رامین رضاییان وسط برنامه بلند شد دکمه لباسش رو باز کرد که بگه ببینید همه لباس و شلوار من برند ایرانی هست. ساعت هم ندارم. میثاقی هم گفت خوبه دیگه دکمه جای دیگه رو باز نکن.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/137767" target="_blank">📅 09:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137766">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
بازی های پرسپولیس در 3 هفته ابتدایی
🗓
شنبه ۲۴ مرداد
⚽️
شمس آذر قزوین - پرسپولیس
⏳
ساعت : ۱۹:۳۰
🏟
ورزشگاه : سردار آزادگان قزوین
🗓
چهارشنبه ۲۸ مرداد
⚽️
پرسپولیس - استقلال خوزستان
⏳
ساعت : ۱۹:۳۰
🏟
ورزشگاه : متعاقباً اعلام می شود
🗓
دوشنبه ۲ شهریور
⚽️
تراکتور تبریز…</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SorkhTimes/137766" target="_blank">📅 09:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137765">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
هزینه‌ی جذب ایری با دستمزد یک فصلش حدود ۳۰۰ میلیارده/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SorkhTimes/137765" target="_blank">📅 09:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137764">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
فووووووووووووری
🚨
ورزش سه: با انتقال دانیال ایری به پرسپولیس، انتقال حسین ابرقویی به سپاهان درحال نهایی شدن است
😐
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/137764" target="_blank">📅 09:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137763">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⚡️
هلدینگ در این مدت 500 هزار دلار به چیواله وکیل ایتالیایی پرداخت کرده بود که هفته‌ای یه بار به تاجرنیا اعلام میکرد خیالتون راحت پنجره باشگاه باز خواهد شد.
😁
😁
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/137763" target="_blank">📅 08:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137762">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWIzwjyp7bi84Q-N2rJOREWgTxmNHmQ06Tu10q7g0VHv6kK3Y3UvN1ArnKOGwUuDupUidwHa_leudEtGLLRnyuo61mymO7kAsG-Sspj0k3USN1RZDy4qQsx-Uz5hGCtJDl0EGTwZcpSIgl26UbbdwPLUINZGHa1mK5yhJ3eSEYYoqaY6aYIInSw1tG41c-LJps_z8gAEckDiq4PZJ8JH8Ov1aOLvogtCH9pEdXtxjO8TyhHdPL4OLFcPXMOGS1OsKilu7D-f8jwV0QmdCG3FSOvISveiNYyarWkL8ZKPR2UJVCLNjla6MTVjNcbmoZencaaor00GZmAd1fcbfHrTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/137762" target="_blank">📅 08:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137761">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRWromiEOSErLQyLzcvjWuh-iotnAiZdN0e6eQeu8yaTXfufNhXYDojEer2rVyF3HHpvIbdx0x6pHoGuK2pUdA3aObgSDr4JxegyWHmlaUvAXjzykHChqyAZFb9BlNNRgKnZV-tqTVs0GvkN06DVaiL_3bBrodnF6lRVn98UOEJZ1n40q493v1jtv5dJtKzHFgB2n24j4lHOYYgKFMkXC_-1wz-ACcB7vPjWcb-1b4jAVCE36_aDLmIKxbHRWu1g7nirmr3aL40MjRWUMo-MwDNiryOYcKknAtDoULfCNFlApDTW9rQWtxf2wwyaNJtBJxrA7LrRHShAJGdSvtxvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
چهار نبرد، چهار داستان متفاوت!
🇪🇺
فرداشب اروپا شاهد تقابل‌هایی نزدیک و پرهیجان است؛ جایی که کوچک‌ترین اشتباه می‌تواند سرنوشت بازی را عوض کند.
لیون و المپیاکوس از گزینه‌های قابل‌اعتمادتر هستند، اما بازی‌های دیگر پتانسیل غافلگیری بالایی دارند.
شروعی محتاطانه و نیمه‌ای دومِ تهاجمی‌تر؛ جایی که احتمال باز شدن بازی‌ها بیشتر می‌شود.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/137761" target="_blank">📅 02:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137760">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSJLk6WWHk3dNHnFAeVfF6IIZfQ4dMNusg7ccsXunOfLllNezOOinRZHKmwJGlyp8_52JYDtyTX44IIcmQhrzvPqj9oF513F9tS1EsusAPl45U2YyRkhwjNulYflgDBhgUTwdak7-GJwIas5YkRFcB4hRmxSa2o1hHpjkCwQuPVevysCC-yPir5yn2G65YZpqq_SPQcAiiicx-csZL1JtYt8kiq60ibA4eviKkn6t7eml1edqd_1z-8adQJUAAVh_I-hvKMknslUo1se_dE3RZheCJzSobi03EiQBr_5_YnRoy0IExe32YLAx4yvskkhvspPG4nVupYuPyBViUnTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شبتون بخیر سرخدلان
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/137760" target="_blank">📅 01:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137759">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
رامین رضاییان مذاکرات وکیلش رو با مدیریت پرسپولیس تایید کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/137759" target="_blank">📅 01:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137758">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
شنیده میشه که سعادتی ایجنت رامین که رفاقت صمیمانه ای با خلیلی داره قصد داره رامین و به پرسپولیس برگردونه !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/137758" target="_blank">📅 01:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137757">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
✅
شنیده میشه که سعادتی ایجنت رامین که رفاقت صمیمانه ای با خلیلی داره قصد داره رامین و به پرسپولیس برگردونه !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/137757" target="_blank">📅 01:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
رامین : آقا محمد حال مردم خوب نیست جدی من خجالت میکشم اصلا راجع به مبلغ قرارداد اینجا حرف بزنم، از مسئولان میخوام کمک کنید حال مردم خوب بشه و با فوتبال آشتی کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/137755" target="_blank">📅 01:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🗣
🗣
🗣
رامین رضاییان یقه باز اومده بود شبکه سه و بعد 2 دقیقه تذکر گرفت که تحریک کننده هست و یقشو بست
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/137754" target="_blank">📅 01:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9uCdVWBB1SgjHBjADxMOijpNxxm4zZWUe4kWgt4Wf029tnli3lo-l_-mPD1ZilZVoZl2xj_49VlwIGfpJcDQQgpqyYCI82mL2akOjQ4EML5WM46GN9wbxPeAQGty5yeIGc-YZbBX2UeSQgGrxlVpxAoP0P_5C8tbneepu8G3I204ju-5I4xk-5sLPWGcatakdyPb6kVqBgwNoD2qkLgU_pI7E_fveaqWpvAquWdlSCC-JEO5VPHeLOyq2h3lC4z1m4-x6X2RFQb16oIXCniSIYn7eymXx7vADrNXsUUDmrtITf-ChCqujyW7yA-BgQW16xIcrlIFarfl7UymxYb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
🗣
رامین رضاییان یقه باز اومده بود شبکه سه و بعد 2 دقیقه تذکر گرفت که تحریک کننده هست و یقشو بست
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/137753" target="_blank">📅 01:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281745dbc1.mp4?token=ob2coMVlRS0FZ7xKVmJk7Vi9WRha7jbISlpg9TROdJecrTUoBevXfPGHwQ1wntOsC80T-n_gXXaOqcppzK8o_fz_HzBmcsQ6PGok6QJn239m0WooTgfSKR18EACCmGfkDEgEcPlnCMRn7Vlhv2RovE_r2bb6XSiNeaFXGnLb2ZkpV6owyW_3nW85ETj6D9GxKKplgHWFJLNT-ng4CymU0Vbsn-hq6_XqPqdJd10R6bwuQOTgIS6fF4xUaTHLLzpby42DIwUeOKeiS4TxX8IHEbvev6LkyR4_A8LAQx_rsfSzLEo28SKmdGA0cmrfVjRG1o78UKxGmpcirihSnQ5amA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281745dbc1.mp4?token=ob2coMVlRS0FZ7xKVmJk7Vi9WRha7jbISlpg9TROdJecrTUoBevXfPGHwQ1wntOsC80T-n_gXXaOqcppzK8o_fz_HzBmcsQ6PGok6QJn239m0WooTgfSKR18EACCmGfkDEgEcPlnCMRn7Vlhv2RovE_r2bb6XSiNeaFXGnLb2ZkpV6owyW_3nW85ETj6D9GxKKplgHWFJLNT-ng4CymU0Vbsn-hq6_XqPqdJd10R6bwuQOTgIS6fF4xUaTHLLzpby42DIwUeOKeiS4TxX8IHEbvev6LkyR4_A8LAQx_rsfSzLEo28SKmdGA0cmrfVjRG1o78UKxGmpcirihSnQ5amA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رامین رضاییان: ما پرواز زمینی می‌رفتیم
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/137752" target="_blank">📅 01:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=NOvtxbT6BF0pddo8F3-AxeenoecMrZDZwGZaWUxlsRQphiVxp-hZnC05ZT-JigYCROyY_weS3KZZnnFT_i9xfNHCgT0vXxxcanRRYYaa1_nC5b2JbNFSVQcH6YPuCPrBuYqJQ1GevwlKN7_hKSlZd0gPyB9_Ev4R-QaaMVMs20ynw81BR-OqTyB_HR_5qo9DoOdsB30R6AmwdTxKj9wMwX8IaeMIMF4Bq_JGxGcgN2T5XffImw1ctAPgkhnQnc3DE3hVfPMTPkgCFkAzA9X5lCLLzJOkxGrDvWd4JV5VnUTPkdc3fvnLYj6z3ReOYiDaUEuqDlUpD67BAx54CB7y2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=NOvtxbT6BF0pddo8F3-AxeenoecMrZDZwGZaWUxlsRQphiVxp-hZnC05ZT-JigYCROyY_weS3KZZnnFT_i9xfNHCgT0vXxxcanRRYYaa1_nC5b2JbNFSVQcH6YPuCPrBuYqJQ1GevwlKN7_hKSlZd0gPyB9_Ev4R-QaaMVMs20ynw81BR-OqTyB_HR_5qo9DoOdsB30R6AmwdTxKj9wMwX8IaeMIMF4Bq_JGxGcgN2T5XffImw1ctAPgkhnQnc3DE3hVfPMTPkgCFkAzA9X5lCLLzJOkxGrDvWd4JV5VnUTPkdc3fvnLYj6z3ReOYiDaUEuqDlUpD67BAx54CB7y2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
رضاییان : ساپینتو منو تمرین راه نمیداد
همش تو کوچه خیابان میدویدم :)))
😁
😁
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/137751" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
باشگاه الوحده امارات در حال بررسی پیشنهادات تراکتور و پرسپولیس برای جذب محمد قربانی است و پرسپولیس شانس بیشتری دارد.    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/137750" target="_blank">📅 00:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
هزینه‌ی جذب ایری با دستمزد یک فصلش حدود ۳۰۰ میلیارده/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/137749" target="_blank">📅 00:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
✅
شنیده میشه که سعادتی ایجنت رامین که رفاقت صمیمانه ای با خلیلی داره قصد داره رامین و به پرسپولیس برگردونه !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/137748" target="_blank">📅 00:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
شنیده میشه که سعادتی ایجنت رامین که رفاقت صمیمانه ای با خلیلی داره قصد داره رامین و به پرسپولیس برگردونه !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/137747" target="_blank">📅 00:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
استقلال دیگه منتظر رامین رضاییان نمی‌مونه
💢
هوشنگ سعادتی امروز با حدادی درمورد رامین رضاییان جلسه داشته ولی نتیجه‌اش نامعلومه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/137746" target="_blank">📅 00:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
رامین رضاییان: دوست دارم تو هیاهو فوتبال ایران بمونم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/137745" target="_blank">📅 00:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
رامین رضاییان: با افتخار تو پرسپولیس بودم و لوگوی این تیم رو بوسیدم، من می‌خواستم بمونم ولی اونا منو نخواستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/137744" target="_blank">📅 00:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
رامین رضاییان: من پیشینه ام پرسپولیسه و پرسپولیسیم و تو استقلال یه مهمون بودم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/137743" target="_blank">📅 00:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
رامین اومد فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/137742" target="_blank">📅 00:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
فوری
❌
مهدی تاج: لیگ برتر با حضور تماشاگر آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/137741" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
💢
💢
💢
باشگاه برای توجیح نیاوردن ایری و طاهری قصد داره هوادارا رو با رامین سوپرایز کنه...
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/137740" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
تاج: هنوز هم معتقدم گل شجاع خلیل‌زاده به مصر درست بود
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/137739" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137738">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
سعید مهری : برای جلالی آرزوی موفقیت دارم؛ بازیکن پرحاشیه‌ای نبوده و به نظرم حتما موفق می‌شود و توانایی فوق العاده داره و هواداران پرسپولیس با آغوش باز او‌ را می‌پذیرند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137738" target="_blank">📅 23:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137737">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
علی بازگشا سخنگوی باشگاه پرسپولیس:
⌛️
قطعا به زودی سه بازیکن جذب خواهیم کرد
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/137737" target="_blank">📅 23:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137736">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚡️
⚡️
مهدی تاج، رئیس فدراسیون فوتبال: تلاش‌ می‌کنیم تا فصل آینده بازی‌ها با تماشاگر برگزار شود/ تمام بازی‌های لیگ با VAR برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/137736" target="_blank">📅 23:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137735">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔄
🔄
بازگشا :در ساعات آینده یا چند روز آینده  خبراییه جدیدی هست که باشگاه اطلاع رسانی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/137735" target="_blank">📅 22:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137734">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
استوری قدوسی  پ.ن منظورش رامینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/137734" target="_blank">📅 22:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137733">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn3S_LAYpWAXKPksGqCfr1KJBy3zP6rfepshRsL0y45DbW6QpHblyzYT8oJiURU2yOKVTd2L3xCJTsiQzzqxNF2op0ihHzAWOZPA-Oygx0kb5u6JomGgRbuzGtTPeYRgFLf20OCu9c7ObfnJA8hjcv2qLBHyRCqeUX4FDuT3Whk30j3_A5h64jaUlXCh8EfzHxw0CRtIUXNiZqq1VBMq6A9APoYLwqZbSUH4OqDlT8vK3BeFqvnZXpuidxXMVgTtayLg6wT-wjjBwcvEtwsaq27Spb20ItcfH2kRDesLnZROAWRBmskK48c_CQjFyACXmgMVYsF2U4gl9b4Mp3AY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/137733" target="_blank">📅 22:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137732">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
استوری قدوسی  پ.ن منظورش رامینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/137732" target="_blank">📅 22:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137731">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
❌
سازمان لیگ باید با این تخلفات اشکار برخورد قاطع کند.اسانی هم فسخ کرده.فسخ فسخ است ولو به فیفا یا فدراسیون اعلام نشده باشد‌.تاجرنیا هم این فسخ را تایید کرده است.مدرک بالاتر از این؟
🔴
🔴
کارشناسان با تایید افشاگری های #قرمزانلاین گفته اند استقلال نمی تواند…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137731" target="_blank">📅 22:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137730">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
حجت موتوری: سرباز بودن علیرضا بیرانوند؟ فعلا مشمول نیست و هواداران نگران نباشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/137730" target="_blank">📅 22:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137729">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
طاهرخانی ادعا می‌کنه پنجره نقل انتقالاتی کیسه تا آخر تابستون ۱۴۰۶ بسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/137729" target="_blank">📅 21:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137728">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❤️
عادل فردوسی پور: هر پلتفرمی برای حضور مهموناش چند میلیارد هزینه میکنه ولی من افتخار میکنم که سلاطین فوتبال ایران علی آقا دایی و کریم خان باقری فقط با یک تماس من به برنامم اومدند، به هیچ مهمانی حتی یک ریال ندادم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/137728" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137727">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚫️
⚫️
فرهیختگان :تارتار هیچ نظری روی دنیل گرا نداره و گفته باید جدا بشه ولی محسن خلیلی مانع جدایی دنیل گرا هستش تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/137727" target="_blank">📅 21:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137726">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
استوری دیگر قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137726" target="_blank">📅 21:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137725">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWAaDlB_dUAoMoEajU9Dlsioc2xG0hxi5CRkbLy2xfJyR38ALD2GTaRSZehnTW6lZvo0YB2In7SIddZ1r7KGKrfyav4OaLOpVhQl4lxF53l_mG3LVOz5cCy8e8zClsiSa3YuIutWVIeUAWooatSP1YukTjG4l_Z3K8nuEr9Jo8KPhi2hRoYiVkPJOIDOZSId_AKFmeT-JKTkqkKcbLtn2QPOCVEtpPAENp83OejXcUTe5Zp9Yu6IBErcwN16o5lPh0byeC9rrj_7xVcNw3TkDD7I7id6bftRy2vrZ6e89RSNajeU9rqm8U6gr6xERdofkcWfi7hPoBpB1cqT2EMWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
استوری قدوسی  پ.ن منظورش رامینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137725" target="_blank">📅 21:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sObLBZA-IU6IiX3Dfos2cu5YEndludk7LSTE2z5ddUQ7H025rmduMs6ZgHiVYkNksl5agc5cY6XpYFalthIvfAju-itI_TMAvXRY2tXrTiYp-4Gcdv7en0QPZsS1ZDyBUCoX1f5UVZyH5wOSfp_ngBljWTN2_4ylHzbqgn0Y4ya0Ouhoymgr1amPnZU0ebkyp_gw-DvHKp8gsdicl9R5Xwrr3724DaecqTfnf9KkGug5TeAR38lzHp0jwfR4w5LqIuecVNvl3X6D2zl_XV6Zs2Dkx-UToAmlobPHFOBh1VI5e0az_WFUKnxtRaWDlxVxyYGCfP4qSzie0uiLkvOnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
رامین رضاییان که هیچ تیمی گردن نگرفتش امشب با کمک میثاقی میاد فوتبال برتر تا از سگ دو زدن هاش تو اسپانیا تعریف ‌کنه که شاید یه تیمی گردن بگیرش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137724" target="_blank">📅 21:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137723">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
ترامپ: ایران خواستار غرامت خسارات درگیری نظامی ۵ ماهه است و من هم از آنها غرامت می‌خواهم چون سربازان امریکایی را کشته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/137723" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137722">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/137722" target="_blank">📅 21:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137721">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/137721" target="_blank">📅 21:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137720">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCWh3uA_PPgFDZ1R62JBF_jpJDBDxPPAtGX_vRgfqOk44b0ap8Fq_y8oJmccodUBR_U-ROLcSyiQrTzs8USt1CrTh9-nOUOp8c5XDyO9iRfgxw9bzKDFjcoI7azGX_oxNMth5qpbyBqzkpWMGrJKIdKCaLg-gMEgiXEYmPCjxYhwWql3_7ssEkC02wfYPIqSUUMyy9qdb0w4ikzUrszkt0O7UAZv5Ltr8Y1GKfyX2fZo5p-Jruagft4liagXMdXC1XbyjTcQsqZ9q0A3-6BmO_4pJgdczrTF_2VQ9HTWoVWRs-89Kneio7kqamXCmB2PQeGZG0Jid62NqpRd8GtZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎾
جودار و فیلس؛ جدالی که می‌تونه تا آخرین امتیاز کش پیدا کنه، قدرت و تهاجم مقابل ثبات و جنگندگی؛ هیچ امتیازی ساده به دست نمیاد.
🎾
رقابت رافائل جودار
🇪🇸
-
🇫🇷
آرتور فیلس رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
ربات اسپورت‌نود
پیش‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/137720" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137719">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
پوریا شهرآبادی: مقابل منتخب کرج وقتی 6 گل زدم دیگر گلی نزدم تا شش بماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/137719" target="_blank">📅 20:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137718">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ورزش سه:
🚨
مهدی تارتار از سیستم ۴.۳.۳ استفاده می‌کنه، برخلاف سیستم پرسپولیس در فصل‌های اخیر که ۴.۴.۲ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/137718" target="_blank">📅 20:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137717">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
رامین رضاییان امشب مهمان برنامه میساکی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137717" target="_blank">📅 20:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137716">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
امید عالیشاه بعد از 13 سال حضور در پرسپولیس به گل گهر سیرجان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137716" target="_blank">📅 19:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137715">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
|فوتبالی: رامین به دو دلیل هرگز به تراکتور نمیره، اولا چون تراکتور مدافع راست آماده داره و رامین میخواد فیکس باشه، دوما رابطه رامین رضاییان و جواد نکونام باهم شکرآب شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137715" target="_blank">📅 19:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137714">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🔴
پرسپولیس رسما قید حضور قربانی رو زد و مذاکرات رو تموم کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137714" target="_blank">📅 18:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137713">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
هزینه‌ی جذب ایری با دستمزد یک فصلش حدود ۳۰۰ میلیارده/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137713" target="_blank">📅 18:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137712">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
اختلاف مدیران باشگاه پرسپولیس با نساجی بر سر انتقال دانیال ایری تنها 40 میلیارد تومن است…!/ خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137712" target="_blank">📅 17:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137711">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
✔️
استون اورونوف در تمرینات پرسپولیس آمادگی بالایی از خودش نشون داده و احتمالا در کنار محبی دو وینگر پرسپولیس مقابل شمس آذر خواهند بود
🤤
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137711" target="_blank">📅 17:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137710">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
❌
لیست بازیکنان آزاد ایرانی با حضور محمد محبی ؛ علیرضا جهانبخش؛ رضا اسدی ؛ مهدی مهدی پور ؛ مرتضی پورعلی گنجی و رامین رضاییان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137710" target="_blank">📅 16:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137709">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⌛️
4⃣
روز مانده تا سوت آغاز فصل جدید لیگ برتر فوتبال ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137709" target="_blank">📅 15:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137708">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
فنونی زاده: با بازگشت رامین رضاییان به پرسپولیس مخالفم
❌
❌
من مخالف بازگشت رامین به پرسپولیس هستم/ بهترین دفاع راست های تاریخ فوتبال ایران از استقلال است و بهترین دفاع چپ ها از پرسپولیس/ بازیکنان الان فقط دنبال پول هستند حالا چه می‌شود دو سال پول زیاد نگیرید؟/…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137708" target="_blank">📅 15:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137707">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
اختلاف مدیران باشگاه پرسپولیس با نساجی بر سر انتقال دانیال ایری تنها 40 میلیارد تومن است…!/ خبرگزاری مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137707" target="_blank">📅 14:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137706">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
فقط
8⃣
روز تا شروع لیگ باقی مانده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137706" target="_blank">📅 14:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137705">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
آخرین شماره پرسپولیس برای جدیدترین ورودی
🔴
🔴
لطیفی‌فر پیراهن شماره ۹۹ را که در گل‌گهر نیز بر تن داشت، همراه خود به پرسپولیس آورده و در تیم جدید خود نیز آن را خواهد پوشید. در گذشته محمدرضا خلعتبری که پس از ترک لیگ امارات مدت کوتاهی در پرسپولیس حضور داشت این…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137705" target="_blank">📅 14:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137704">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🟠
فوتبالی :
⚡️
جذب دانیال ایری کنسل نشده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137704" target="_blank">📅 13:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137703">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
🔴
🔴
ایمن حسین مهاجم ۳۰ ساله تیم ملی عراق، در انتقالی آزاد با قراردادی یکساله به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137703" target="_blank">📅 13:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137702">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
سرژ اوریه به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137702" target="_blank">📅 13:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137701">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9oZpNPiP0jhmLQDCxWgghYkMM_6yjbL9tg9uXWb9PZZOto4ocVx7z7EfCj5rCgO_fxW-xIgorC8RyGFxpt30NGVZiQuH0aTZbo8Y8WkNut9UsGqjA5mwXuw6-uA47UFMxAEiIZE0QipDDY_41z0nTJ1RDwkowiuCHXuUVMpqTjeipOwfWCfjvqwZ7BV5JWpzXfqm1rhEwmx_iXWyTRWvpc4RVo5NMUDCrBdtChC36Trd767_wr4nOZPsSjrlp_d3YwjJxbBoyaX5-p_rLB8-Y0hQGcTyf0CNU3jBBvf-PWTAA_6VvclsLZV0PqPtwOA-4WfXLubvhXprouj_kNxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
جدال قدرت و ثبات؛ خودار مقابل فیلس
🎾
Rafael Jodar -
🎾
Arthur Fils
🎾
خودار با تکیه بر قدرت ضربات و بازی تهاجمی، سعی می‌کند از همان ابتدا ریتم مسابقه را در اختیار بگیرد.
فیلس در رالی‌های طولانی و تبادل ضربات از انتهای زمین کیفیت بالایی دارد و می‌تواند بازی را به چالش بکشد.
در مجموع انتظار یک مسابقه نزدیک می‌رود؛ عملکرد خودار روی سرویس و ضربات اول، می‌تواند تعیین‌کننده نتیجه باشد.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و با ۱۰٪ بونوس اولین واریز پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137701" target="_blank">📅 13:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🔴
پرسپولیس رسما قید حضور قربانی رو زد و مذاکرات رو تموم کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137700" target="_blank">📅 12:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137699">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0PnJCBl20ONTGgxyEV8D4IFlaY51aomV1pX4tY07Z-9tPhFAmbJ3-8SVwpFzVEcqfMvyCl7Hi1Y5L6WmixgbfZL_YxEEnip76Mpa_7zz_zFZiC567k9XsLBhtnxSa83dBW7rmg3_uZwYK42pvo5DTHjr__ghmvo9-HMOil0NWO93fjCsMIzFd7ol2DshlzU8tW8IDVPpCcdfyRrT52ZSrl2ZsUMDaRN3jBS33VSNtrc40Vbt6knt0Btls4sufwbU1iDyM1wz7waL5lYxGDWOuFrHRDbemwmRFzU2I3GxcE5vBbTbx01273lg-Ribtx3FBAjQGRU35cm5LyT9_0f5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پرسپولیس رسما قید حضور قربانی رو زد و مذاکرات رو تموم کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137699" target="_blank">📅 12:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137698">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
ورزش سه که دیشب گفته بود ایری به پرسپولیس پیوست الان نوشته ایری به پرسپولیس کنسل شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137698" target="_blank">📅 11:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137697">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
ورزش سه که دیشب گفته بود ایری به پرسپولیس پیوست الان نوشته ایری به پرسپولیس کنسل شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137697" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
پرسپولیس همچنان پیگیر جذب قربانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137696" target="_blank">📅 11:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137695">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
ورزش سه که دیشب گفته بود ایری به پرسپولیس پیوست الان نوشته ایری به پرسپولیس کنسل شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/137695" target="_blank">📅 11:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
❌
قاب ماندگار از اورونوف؛ ستاره محبوب ارتش سرخ پس از جدایی سروش رفیعی، حالا یکی از صاحبان بازوبند کاپیتانی پرسپولیس است.
👍
دیروز اولین تجربه رهبری او با این بازوبند رقم خورد؛ افتخاری تازه برای بازیکنی که جایگاه ویژه‌ای در قلب هواداران پیدا کرده است.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137694" target="_blank">📅 09:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137693">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
امیرحسین ریوندی مدافع چپ 22ساله سابق تیمهای اکادمی کیا، زسکا مسکو و بخارا کرواسی به مهدی‌تارتار معرفی شده تا درصورت تایید جذب شود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137693" target="_blank">📅 08:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137692">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
✅
✅
ورزش 3:
❌
دانیال ایری دقایقی پیش از بازیکنان و کادرفنی نساجی خداحافظی کرد و برای عقد قرارداد با پرسپولیس راهی تهران شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137692" target="_blank">📅 08:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
فوتبالی: جواد نکونام به رامین رضاییان علاقه‌منده و این احتمال وجود داره رامین به تراکتور بره و باشگاه تراکتور هم اجازه جدایی صادق محرمی و پیوستنش به پرسپولیس رو بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137691" target="_blank">📅 08:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ik6gkZFxePdRqLgZz7cHwYQknrWo8nRUEgJsWhpGLhIWqK9IY8bVuoMGhyKvw1_kGN0pKB_52IEYgqVaeiKlDyVXLuN-JEfNos3rm_4zM70NcVZ0lznVhWFTunB91lWP8iRkn94KCkjwEP4bEcppgVaY9a57YF8HylRBrt8d7BHiKYDLdTS25WDPEjPbfLnwKuxiyzx4iPbLVYLSupLBQLVJaFYcVdoMi-IRzfb7H6Ku9JxI1525zgwF2sErHPFBS5i4cIhFvz7n_slD9HxR2ioqdL4YP62WBaG98Q5aR3pNNcx_uPdjIBkVBP4he4HBWZt3NOAmyJljiiYXeSmgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇴
لوکاس ژوائو، مهاجم سابق پرسپولیس به پترو اتلتیکو لواندا آنگولا پیوست. بزرگوار از زمان ترک پرسپولیس تو ۲۹ بازی لیگ یک ترکیه، فقط یک گل زده.
‼️
🫠
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137690" target="_blank">📅 08:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUSYAldfg-BgG9pHmmdJira2V1Rt8rWjMtPMA5RgPvvBw7oD21pFlrbR71BzVJwDH-UafxzgBZRW41uZxoEtcERNVDCZOkdSYnZgO1hGBokm2dGQjv2PcMyeA9ZlI2bQHV0S6EqTmhIYPc5fdEC5DAQh_2qvaSEUBjxS3q3LRINAY9J5tGZN3xABisY8btTRrKJCXQW40LD2eqrlG-5CyLiEIzqg9QfXAi6N8um1z-mK05fbd6lM__fx6gkjl338UyhYZIemyv_Hvbh4rxRPE_onw33vwVz-pcfCWDjJ-NYXpEwZ8ZEQ8Zcm-qxxJgBby0Pqc60NBlhTtUXScVWVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137689" target="_blank">📅 08:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEgJXNQHFTsVY7b2Hk2ZS8co1WZlebuV_jYBvzoG146_AQ0RBrb0hDuQrxFUEOpdLuncmZ5sxaskY8pnS5FD5ZYHSWpFYLerPpcKSM0pMM_F_GroRjaTnubuj6qy3xRR3qF5Fh5WnIW6B2qXXFuTrTqEJCa9WiHbZCHUXkQZGBEtNOAUsswxA1cIMnVQGtgTKqfHPhpUUNl7zGkG-Fg3ch9YACSdbRCsseFoctErCgYHRxk2F8Pwogd1KarA-p7mGVvlR0p42UWU0WjWXbQS1J7d3KT4uQhQ5otrcclkqWWgd8lGeSO4W3H_rUOEOKQEJWd0fsEGngKPgDD5jkFx1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
هر چرخش یک شانس تازه برای برد!
🎰
اسلات با هر اسپین، ترکیبی تازه از نمادها و شانس یک برد هیجان‌انگیز را رقم می‌زند.
از بردهای کوچک تا جک‌پات‌های بزرگ، همه‌چیز در چند ثانیه مشخص می‌شود.
قابلیت‌های ویژه، فری‌اسپین و نمادهای Wild می‌توانند هیجان بازی را بیشتر کنند.
اسپین کن و ببین شانس امروزت چه چیزی برات رو می‌کنه!
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و با اولین واریز خود ۱۰٪ واریز بیشتر دریافت کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137688" target="_blank">📅 02:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1Fbe2siNSC3GuFM1jIL9Tuu-5TjH2D-CUUr6a5COAmni6Yry-Re15qVefI6exsKMq-1kKkyatMme0sLzxepi1db0E-XE5QI0vGe2Lfos6Y1AkB-cqAK6tunlB8htoPjETPjHHbbiYg4NfyI1YI0_IZzomF4xriuZ6xdrZ516AincR0swOe0AzeIdmndHnrZbdW5bT3e9V3AkVGJG6CEYDC_IJWIGR_1P9W1bniggT2JXwMBCdl_YASFYdPUCmhOmjDN_deVSNbC8YiQgBFhdU3-Eqo1P9Um6GQCWCmQSYj36Zj5sMkosjguS17hGxvQ1tHy7PdUwCAjC2q-TADnbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🤝
ردِ مهربانی، هرگز با گذشت زمان پاک نمی‌ شود ...
❌
❌
شبتون زیبا بهترین هوادار پرسپولیس
♥️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137687" target="_blank">📅 01:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3aCocEmHhUG3u9GwK9BlFwObYIcpjT2E72D6crmEj2gWX5MA3P2_TPkiIW133u1FbyIq9PGtH07mlKH1vqP3wnabm88CD5uRQtqrMwxNG3ofCUtd1blVNwxkaE7bnvgwqfyQkIOtFk9pCH4OoY9ZCkBDbitdHTYuCqjYobD7f77W8XqjJHWVHU0W-0KOVj82NNnecyEjkr7RdzNtztKyRfNxWg_LOOcRS5AV8s2GGV0AjTDzozwd0fPdicWXZ1kvcB8wYtwrgH1IXKoTJHsonfJXPT8TZGP9H4vwSnV3CJdrTMPVHFC894cGBapIEkcn82b4as-M3dkl2LN_Vz3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امیرحسین ریوندی مدافع چپ 22ساله سابق تیمهای اکادمی کیا، زسکا مسکو و بخارا کرواسی به مهدی‌تارتار معرفی شده تا درصورت تایید جذب شود.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137686" target="_blank">📅 01:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
❌
فووووووووووووری
🚨
ورزش سه: با انتقال دانیال ایری به پرسپولیس، انتقال حسین ابرقویی به سپاهان درحال نهایی شدن است
😐
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137685" target="_blank">📅 01:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137684">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
کوروش اژدهاکش، بازیکن جدید پرسپولیس:
❌
اجدادمان گفته‌اند اژدهاکش بوده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/137684" target="_blank">📅 01:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137683">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
❌
تارتار به باشگاه اعلام کرده که فعلا با جدایی ابرقویی موافقت نکنید و هر روز هم پیگیر جذب دانیال ایری است
❌
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137683" target="_blank">📅 01:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
✅
ورزش 3:
❌
دانیال ایری دقایقی پیش از بازیکنان و کادرفنی نساجی خداحافظی کرد و برای عقد قرارداد با پرسپولیس راهی تهران شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137682" target="_blank">📅 01:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">💢
💢
💢
💢
💢
#فوووووری؛ دانیال‌ایری مدافع تیم‌ملی ایران با عقد قراردادی به پرسپولیس پیوست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/137681" target="_blank">📅 00:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💢
💢
💢
💢
💢
#فوووووری؛ دانیال‌ایری مدافع تیم‌ملی ایران با عقد قراردادی به پرسپولیس پیوست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137680" target="_blank">📅 00:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137679">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
❌
مبلغ رضایت نامه دانیال ایری فردا پرداخت خواهد شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137679" target="_blank">📅 00:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137678">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137678" target="_blank">📅 00:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137677">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137677" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137676">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
بازگشا، سخنگوی پرسپولیس: تارتار کاملا از اردوی ترکیه رضایت دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137676" target="_blank">📅 23:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137675">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
✔️
شماره پیراهن بازیکنان پرسپولیس در فصل آینده مشخص شد
⏺
1_ پیام نیازمند :  شماره 1
⏺
2_ ابوالفضل جلالی : شماره 3
⏺
3_ محمدمهدی زارع : شماره 4
⏺
4_ حسین ابرقویی نژاد : شماره 5
⏺
5_ حسین کنعانی زادگان : شماره 6
⏺
6_محمد عمری : شماره 7
⏺
7_ مهدی تیکدری…</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137675" target="_blank">📅 23:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137674">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
بترس پرسپولیسی؛ رضا اسدی از گل‌گهر جدا شد!
😐
پ.ن نیاد جای علیپور صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137674" target="_blank">📅 23:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137673">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
فوتبالی: جواد نکونام به رامین رضاییان علاقه‌منده و این احتمال وجود داره رامین به تراکتور بره و باشگاه تراکتور هم اجازه جدایی صادق محرمی و پیوستنش به پرسپولیس رو بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137673" target="_blank">📅 23:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137672">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b26a5d521.mp4?token=AGyh8O0C2h7AEXMmNTjD-2Ti-AofDtCo99-SrEjbokHGA_fBOrIGDaYA8DuS2V6uupgBVTFwgWZFlwQILi4thqH_5VqRvef1zOQp0zbamXu-NXVp1z1L-dV4sqzUOsPxcRO_EHr39gYwUaCAIbYGaxm6DcJozHhD3SfVS3moPm58lsRoSu33Sn2q7GG1TMR-wzKf2czGCGJEXYnJznUdpb04ipVbfLLzyu0JxQ8Saaw8A86siYRYoMrpiI7xdfC5DMgphAIuvTOMeq6cD2O4D8YhD-w2EuN72dmAM4UztPcJziZ6roVIzZy5I3TdWJL3RVvSmx37ff-TfgNddAaw0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b26a5d521.mp4?token=AGyh8O0C2h7AEXMmNTjD-2Ti-AofDtCo99-SrEjbokHGA_fBOrIGDaYA8DuS2V6uupgBVTFwgWZFlwQILi4thqH_5VqRvef1zOQp0zbamXu-NXVp1z1L-dV4sqzUOsPxcRO_EHr39gYwUaCAIbYGaxm6DcJozHhD3SfVS3moPm58lsRoSu33Sn2q7GG1TMR-wzKf2czGCGJEXYnJznUdpb04ipVbfLLzyu0JxQ8Saaw8A86siYRYoMrpiI7xdfC5DMgphAIuvTOMeq6cD2O4D8YhD-w2EuN72dmAM4UztPcJziZ6roVIzZy5I3TdWJL3RVvSmx37ff-TfgNddAaw0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پوریا لطیفی فر: از بچگی رویای پوشیدن پیراهن پرسپولیس را داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137672" target="_blank">📅 23:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137671">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
محمد قربانی به مدیران الوحده امارات گفته دوست دارم برم پرسپولیس. اونا هم گفتن هر تیمی زودتر رضایت‌نامه رو پرداخت کنه، میری همونجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137671" target="_blank">📅 23:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137670">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVjoZ61YHqHccqLOF6Sooa6rLFwnXTIXELcvzbuXmqcbrh-xMnEGuTzRCY64dL7Jj8LZRHUUOvcINKBHmtU7NJoDdphNwIEV4SPe33407JagsSoxnR44dN4riMNKGVYB5O6YEcDvdBQa87MS8zIYJS-NcRIqZMVnnTjl1f9wKFQTSlRSeg6bGmSS0CIqJpT8PncP8XcJHbvw1azl90E-8QCMYU-BafMUCcNEtC_n0zEA6np0pJMivsOwGMz0CI_MtCCGmzVA6lH5uVhRG19USq0UB_UF_0X9QPjBKf2emwALIXoIukCfrWir0bBbFQOq9G2XRmcpGYexzqeZk5M5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏
مسی در مراسم ختم پدرش
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‎</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137670" target="_blank">📅 23:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137669">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87be55d80c.mp4?token=LnAyHRcshCuzd0o23xGwyVt3sLPgdzlIoeSzehS6o1xBVZKfy6SLOl-RO2jhoKDVhLZfrNWJcAGPU66abuvoPgojQQ27xu3UoWbqY_8rb_MsAYAt-QaMu5VctcHEFzUFWCqe4p0iL7BK6jibvhbAqj9RkaCqQva6-p5pM4y1Ri0Q7QmHVJRHM2pQzcWph0Sp6ALoV5B1I-BopJvutBvxfOq7rOqyipMKTgRLLZylrqsz69US8zPiPeGUuGpgJ2RFzd7P0deBvCZwUUYm23o2_B1O9-F0ELBuIufxBsc-JqlnFVgEyhmpfp9NfzI_aJIMZhOb7aPC2_h4IubyKMgdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87be55d80c.mp4?token=LnAyHRcshCuzd0o23xGwyVt3sLPgdzlIoeSzehS6o1xBVZKfy6SLOl-RO2jhoKDVhLZfrNWJcAGPU66abuvoPgojQQ27xu3UoWbqY_8rb_MsAYAt-QaMu5VctcHEFzUFWCqe4p0iL7BK6jibvhbAqj9RkaCqQva6-p5pM4y1Ri0Q7QmHVJRHM2pQzcWph0Sp6ALoV5B1I-BopJvutBvxfOq7rOqyipMKTgRLLZylrqsz69US8zPiPeGUuGpgJ2RFzd7P0deBvCZwUUYm23o2_B1O9-F0ELBuIufxBsc-JqlnFVgEyhmpfp9NfzI_aJIMZhOb7aPC2_h4IubyKMgdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پویا پورعلی: شهرآبادی کامل‌ترین مهاجم حال حاضر لیگ است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/137669" target="_blank">📅 22:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137668">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎙
⚽
محمدمهدی زارع: آقای تارتار به من زنگ زد و گفت اگر به پرسپولیس بروی موفق تر از رفتن به استقلال می شوی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/137668" target="_blank">📅 22:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137667">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎙
🎙
محمدمهدی محبی : اگه یه چیز در مورد هوادارای پرسپولیس بخوام بگم بازی استقلال خوزستان تو ذهنم میاد که تا لحظه آخر حمایت کردن‌. امسال تیممون جوون شده اگه به امید خدا این نسل بگیره مثل دوران آقای برانکو میتونیم چند سال قدرتمند ظاهر شیم و به حمایت هوادارا نیاز…</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/137667" target="_blank">📅 22:42 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
