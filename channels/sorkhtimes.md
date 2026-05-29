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
<img src="https://cdn4.telesco.pe/file/H0vCTdyaImncXwWKXmmC-6ibB3SMiqccysdHMcXxNsSHHmJXer4a0Vp04G97WeHMf_dpsk3eE8MoypD2sfReHrQrUCzJVmllZCTnOmwNWu0RZA_q6EE6w-Fl_LB3vcpGfHBV6CkzvfYW6RQPoKTeymtcRdXlsLcMzrNVQpk1Tg3yC9R8ROBL_yyzTLzs5YzcXoXB7rg2ULAvLISH6uaWZDhUTl-SwvCRSBbA7Kq4YwDhNzQvZgW5dZuLjzeXg2p6W07vUEfZfaHBEolNSOHsW6Izp-Q-OsxFwJerEBvZ9kjHaPew0WZOTI82lcRxh7sPw3G3alB5Xpscs0Vd23IA4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.7K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 02:35:12</div>
<hr>

<div class="tg-post" id="msg-132456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJ2iNL9KYjuWSSbzYdOWdTd7NSwZSzxPUEH1mACxRc_v0j9p2FmjvuJAgJ332J8dqtShKSP-NjFXs1PcGXLqCU5zHNl-EOwOFnCLYSenIZk03HNvt10Ani_24UAT4HlfjvT7TqZWd67FmqFaSoORfyjUBxTYEze6f1coIDHhvLDC9mNWFSw82Q74JPdBBhuDW7cMPN4Pvp6jbiOLdioH2VndVeSzH7ti292TcJtXIJf2fQ9xrZaNBZmVCs_-T2ABiua8A9_DiwuNLtYPmtWK1-PUvE5O5r_1zg8Fg8WqG3svB18-xcEW0MUj5jrgVX-rhqmyDPDD81itZbRUf83BEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 520 · <a href="https://t.me/SorkhTimes/132456" target="_blank">📅 01:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
فرهیختگان: AFC مجددا با درخواست فدراسیون جمهوری اسلامی مبنی بر دیر اعلام کردن 3 نماینده برای حضور در آسیا مخالفت کرده و اعلام کرده ۱۳ روز وقت دارید که 3 نماینده خود را معرفی کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/132455" target="_blank">📅 00:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
فرهیختگان: AFC مجددا با درخواست فدراسیون جمهوری اسلامی مبنی بر دیر اعلام کردن 3 نماینده برای حضور در آسیا مخالفت کرده و اعلام کرده ۱۳ روز وقت دارید که 3 نماینده خود را معرفی کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SorkhTimes/132454" target="_blank">📅 00:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎙
پیمان حدادی:
🔴
ما هم می‌گوییم استقلال نباید معرفی شود؛ در حالی که نماینده پلی‌آف در آسیا نداریم؛ بعد از جام جهانی در کنار لیگ حتی می‌شود جام حذفی هم برگزار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/132453" target="_blank">📅 00:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
مرتضی فنونی زاده پیشکسوت پرسپولیس:
❌
آقای تاجرنیا از اسمش معلومه پولدار، بابای منم تاجر بود، ولی آخراش، تاش رفته بود جرش مونده بود
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/132452" target="_blank">📅 00:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚡️
⚡️
⚡️
برکناری با چند هفته تاخیر
❌
قطع همکاری محترمانه پرسپولیس با کرمانشاهی
⚡️
⚡️
فرهیختگان: یکی از انتصاب‌های عجیب رضا درویش در دوران مدیریتش در باشگاه پرسپولیس صدور حکم مدیر اجرایی برای رضا کرمانشاهی با رقم قرارداد قابل توجه بود. جالب اینکه کرمانشاهی فقط…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/132451" target="_blank">📅 23:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132449">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa86d2930.mp4?token=uORdh-kASO2HDE2irJOTcPz0kDGGVXNFyfCOj9r8PLfU1dKm-50SAqvM8zOJTCtp5n_V7gVbXzw7fJOji9b_a9sI_sOY2q0J-F9quUh9BF3yg_sR2T4YoVY5zD9NfOFbkpGUkwkwxAD5_OyVwq5hkg948rM_00RYlLpINLm5-165H8T_3atO-B5GQO1n4Q_Aq9t32M0VtB5gMXtpXIbwv1u6vLFa-rs_KHKZi2744P2Z_KhKJdcGfIqmaqrwO4aVc0oq8OqyG0-bh8X53SOQSF_5Jvj_yalLHHKr6CQ2x18Ai3ZkYEUp7nedonvuoAT5zPeHZzkT92d7rlrq4o0H-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa86d2930.mp4?token=uORdh-kASO2HDE2irJOTcPz0kDGGVXNFyfCOj9r8PLfU1dKm-50SAqvM8zOJTCtp5n_V7gVbXzw7fJOji9b_a9sI_sOY2q0J-F9quUh9BF3yg_sR2T4YoVY5zD9NfOFbkpGUkwkwxAD5_OyVwq5hkg948rM_00RYlLpINLm5-165H8T_3atO-B5GQO1n4Q_Aq9t32M0VtB5gMXtpXIbwv1u6vLFa-rs_KHKZi2744P2Z_KhKJdcGfIqmaqrwO4aVc0oq8OqyG0-bh8X53SOQSF_5Jvj_yalLHHKr6CQ2x18Ai3ZkYEUp7nedonvuoAT5zPeHZzkT92d7rlrq4o0H-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
ریکاوری ملی پوشان پس از پایان دیدار با گامبیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/132449" target="_blank">📅 21:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132448">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wms0LeQR4-6uIO9hhjaN27mqWgxitd0_nzrdScEzjd9YvygQ_d-jei3hPCUWWMiP7fuJDDJxudmogBD6pchl4VgYpTA2j6-Lw8LOG4r40eTEr-TOSl05erzns0BnuW0XXv5YIXSG_Vfe2fxfn41vT9H85fRKPSH_Am98cx6rzl-RmAKKveNzK3qycbEwZDG5Qc_S1B9s4rEYS2Qc7Fhq82JdD0gdk1trsjVubAKvhEHf_f-QKMxCK1NVmhm1fBjCXDfCtWMpQ8gBBXdPd2HTgUXxz3wf9J3j7_gGVGyUxsbBbeafLfSIbTjBK7ME5gfH4lGoZZ-orECP-gWZlLGr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SorkhTimes/132448" target="_blank">📅 21:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132447">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e547127cf5.mp4?token=TioVGhan7jT3Vlsn5BPZn7k60Ly7pjDVlw0mS-5t0xXg-B7XRSlcrGlVq2H14m2yBQy5Wi-tuZDJIDqlY0Tv1Uz2hgeAbGzsfQ78NDtgZHVT5IpFqVnQeDcmHVQ2SOayiMMpWMwQO_XwT3JBefaRlDtPJSsYeIF0BKqCHfqFVzEIOppwjB4zjfZ5meeJJwJHqtDAP5nnfD-VLe8aSneAiL35naG6-Cg4qA1TLyQ7dMCHfjE_8DoS2XVT2desn6oLIDlFYnlasubmWfSXJCOrDQ0-95rS9uQlphTWNmGh2Z6R_yF4F3EOA0Stj7B_5KRqTf9icO7cIDfE758YPxlTEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e547127cf5.mp4?token=TioVGhan7jT3Vlsn5BPZn7k60Ly7pjDVlw0mS-5t0xXg-B7XRSlcrGlVq2H14m2yBQy5Wi-tuZDJIDqlY0Tv1Uz2hgeAbGzsfQ78NDtgZHVT5IpFqVnQeDcmHVQ2SOayiMMpWMwQO_XwT3JBefaRlDtPJSsYeIF0BKqCHfqFVzEIOppwjB4zjfZ5meeJJwJHqtDAP5nnfD-VLe8aSneAiL35naG6-Cg4qA1TLyQ7dMCHfjE_8DoS2XVT2desn6oLIDlFYnlasubmWfSXJCOrDQ0-95rS9uQlphTWNmGh2Z6R_yF4F3EOA0Stj7B_5KRqTf9icO7cIDfE758YPxlTEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| رسانه اسرائیلی:
🔻
ایالات متحده و ایران در آستانه امضای توافق هستند
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/132447" target="_blank">📅 21:09 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132446">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
تیمه گروهبان از گامبیا گل خورده و عقبه.گامبیا با ۱۵ بازیکن اومده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/132446" target="_blank">📅 21:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132445">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
علی علیپور پس از پاس گلی که به مهدی طارمی داد به سمت قلعه نویی رفت و او را در آغوش گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/132445" target="_blank">📅 21:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132442">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1699b581.mp4?token=M7gWHjfroToOwJGbGqRX2r6ViWX_b87c3waImXK-kaYWOZtTJqbOuFA8Y56MHk53Gdg0-cKraGuTGQfp7Zk3i3ev0TPPX6klKOiG9sPsrD-gH_MGsE-vvVYkArReIJZYf_lNe-MDAgCNXNRDk2hDaoHCI3SHEneCUXcvXaOycaNnoBusN-Y5h4OM0jBhP_3-B3Vmws4cArAjor6DfASy5VBUF01Ijvk9i5a4aL7uwpOgjLlEPzpEgtqaHTHZxmPnSMGA7Yxy2u3FFvn2kr5WMi5BxNhdMGzYbRXmvDSBrcLWAbOcjfI7DP7czWmm8afVl_G37bPrw7kMU9EQz5YC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1699b581.mp4?token=M7gWHjfroToOwJGbGqRX2r6ViWX_b87c3waImXK-kaYWOZtTJqbOuFA8Y56MHk53Gdg0-cKraGuTGQfp7Zk3i3ev0TPPX6klKOiG9sPsrD-gH_MGsE-vvVYkArReIJZYf_lNe-MDAgCNXNRDk2hDaoHCI3SHEneCUXcvXaOycaNnoBusN-Y5h4OM0jBhP_3-B3Vmws4cArAjor6DfASy5VBUF01Ijvk9i5a4aL7uwpOgjLlEPzpEgtqaHTHZxmPnSMGA7Yxy2u3FFvn2kr5WMi5BxNhdMGzYbRXmvDSBrcLWAbOcjfI7DP7czWmm8afVl_G37bPrw7kMU9EQz5YC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مصدومیت شدید کنعانی در جریان بازی با گامبیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/132442" target="_blank">📅 19:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132441">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
🎙
سامان آقازمانی، بازیکن پیشین پرسپولیس:
‼️
اصلا دوست نداشتم جای بازیکنان تیم ملی باشم. راست بری، با دولت درگیری. چپ بری با مردم درگیری. بی‌طرف هم بخوای باشی بهت تخم‌مرغ میزنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132441" target="_blank">📅 19:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132440">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
گامبیا حریف ایران فقط با ۱۵ بازیکن به آنتالیا آمده است!  در بازی دوستانه هم به ما توهین میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/132440" target="_blank">📅 19:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132439">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/132439" target="_blank">📅 19:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132438">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/132438" target="_blank">📅 19:27 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132437">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
ترامپ: ایران باید قبول کنه هیچ‌وقت سلاح هسته‌ای نخواهد داشت
🔴
تنگه هرمز باید فوری باز بشه و عبور کشتی‌ها بدون هیچ محدودیتی انجام بشه. هر نوع مین دریایی هم باید کامل جمع‌آوری یا نابود بشه
🔴
کشتی‌هایی که به خاطر محاصره متوقف شدن می‌تونن برگردن به مسیرشون و…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/132437" target="_blank">📅 19:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132435">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
ترامپ: دستور دادم از این لحظه محاصره دریایی ایران پایان یابد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132435" target="_blank">📅 18:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132434">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
شبکه ۱۵ اسرائیل : به نظر می رسه ترامپ با یادداشت تفاهم با ایران موافقت کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/132434" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132433">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❗️
ترامپ: محاصره دریایی ایران از همین حالا برداشته خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/132433" target="_blank">📅 18:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132431">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
ترکیب بهترین تیم جام‌جهانی برای دیدار دوستانه با یه تیم ناشناخته اعلام شد.   علیرضا بیرانوند، علی نعمتی، حسین کنعانی‌زادگان، احسان حاج صفی، آریا یوسفی، سعید عزت‌اللهی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، محمد محبی، مهدی طارمی و کسری طاهری
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/132431" target="_blank">📅 18:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132430">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
ورزش سه: باشگاه پرسپولیس تو نقل و انتقالات تابستانی دو هدف داره: یکی پوست‌اندازی و جوان‌سازی ترکیب پرسپولیس و دیگری اضافه شدن چند ستاره مهم و تاثیرگذار برای بستن تیمی در حد کسب قهرمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/132430" target="_blank">📅 18:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132429">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/132429" target="_blank">📅 18:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132428">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/132428" target="_blank">📅 18:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132427">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
ورزش سه: باشگاه پرسپولیس تو نقل و انتقالات تابستانی دو هدف داره: یکی پوست‌اندازی و جوان‌سازی ترکیب پرسپولیس و دیگری اضافه شدن چند ستاره مهم و تاثیرگذار برای بستن تیمی در حد کسب قهرمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/132427" target="_blank">📅 18:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132426">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فارس: مدیرای پرسپولیس منتظر تعیین تکلیف رقابتای لیگ هستن و هیچ فعالیتی در نقل و انتقالات انجام نمیدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/132426" target="_blank">📅 18:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132425">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
ترکیب بهترین تیم جام‌جهانی برای دیدار دوستانه با یه تیم ناشناخته اعلام شد.   علیرضا بیرانوند، علی نعمتی، حسین کنعانی‌زادگان، احسان حاج صفی، آریا یوسفی، سعید عزت‌اللهی، امیرمحمد رزاقی‌نیا، امیرحسین حسین‌زاده، محمد محبی، مهدی طارمی و کسری طاهری
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/132425" target="_blank">📅 17:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132424">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
تیم ملی قراره امروز ساعت 19 با یکی از تیم های قَدَر فوتبال جهان بازی دوستانه برگزار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132424" target="_blank">📅 17:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132423">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎙
🔴
محسن بنگر: وقتی که نمی‌تونیم حتی تیم های اماراتی رو ببریم چه اصراری به حضور تیم های ایرانی تو آسیا داریم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/132423" target="_blank">📅 17:00 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
🚨
🚨
🚨
فووووووووووووری
🚨
سی‌ان‌ان: در این هفته خبر رسید که ایران با آخرین پیش‌نویس پیشنهادی موافق است؛ دونالد ترامپ به مشاوران خود گفت که برای تصمیم‌گیری درباره امضای این توافق احتمالی، چند روز وقت می‌خواهد.
‼️
به گفته یکی از مقامات، به نظر بعید می‌رسد که ترامپ…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132421" target="_blank">📅 16:03 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132420">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
شبکه العربیه از منابع مطلع:
🔴
جمهوری اسلامی میخواد اورانیوم غنی‌شده‌ش رو به چین بفرسته، به شرطی که چین تضمین کنه این مواد رو به آمریکا تحویل نمیده.
🔴
به گفته این منابع، خیلی از نکات مربوط به برنامه هسته‌ای جمهوری اسلامی تو مذاکرات الان حل و فصل شده.
🔴
بر…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132420" target="_blank">📅 15:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178f9cb33.mp4?token=Pp29hFLWj9DeMBLhiaYRCxF8NaCJ0zCd24eYKuGd1BL2L5NHNz0eM10qjRmj-HPcJ3hQm4TXM0NSiHQmr-y4pBZe0RGgfQUFDXYA1N0XSXTgim2cyPGCj8o6-qPdQabaDUSXZ9djFsIAuScesTwJ5JFB6xtxFI6PDTPMIah839Mhzb3ELEBd7obYM70NpojgpaezG0inCp-x8GICd9JGym82l9PMP25un4ltCBb3tCSJUF5zdf2KmGogc8Wr2urY-VcLMEkWFnguf7RNnNpzcHdzFFXVFxxgdvH4jYX-cfjr3hLHeuk4mSs30nSh5Yvk4-yJq5WnlZ-f1BYGRO-iCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178f9cb33.mp4?token=Pp29hFLWj9DeMBLhiaYRCxF8NaCJ0zCd24eYKuGd1BL2L5NHNz0eM10qjRmj-HPcJ3hQm4TXM0NSiHQmr-y4pBZe0RGgfQUFDXYA1N0XSXTgim2cyPGCj8o6-qPdQabaDUSXZ9djFsIAuScesTwJ5JFB6xtxFI6PDTPMIah839Mhzb3ELEBd7obYM70NpojgpaezG0inCp-x8GICd9JGym82l9PMP25un4ltCBb3tCSJUF5zdf2KmGogc8Wr2urY-VcLMEkWFnguf7RNnNpzcHdzFFXVFxxgdvH4jYX-cfjr3hLHeuk4mSs30nSh5Yvk4-yJq5WnlZ-f1BYGRO-iCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تیم ملی قراره امروز ساعت 19 با یکی از تیم های قَدَر فوتبال جهان بازی دوستانه برگزار کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132419" target="_blank">📅 15:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132418">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏆
موزیک ویدیو رسمی جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132418" target="_blank">📅 15:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132417">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فارس: مدیرای پرسپولیس منتظر تعیین تکلیف رقابتای لیگ هستن و هیچ فعالیتی در نقل و انتقالات انجام نمیدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/132417" target="_blank">📅 15:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132416">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132416" target="_blank">📅 15:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132415">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrsRNJNLyyZ-qnf16mig1FRxG9q7_tKji1iAU_vvriO1QFURtoM5hAL3rT_5BP70pbkQ3NGPtqDRbKQIjRUhqQYX7YUKHOcUbKMxPeumCwScGu1zr8AAux-pvb_5XGgZtecKaEJoUacVzG_36s5ZsrQN2HXzyN8lETpMFAa-kzSbJzPYuMKf9WMwQ6wn1vlLNxeKnF1UhEXCbfMGVdbG5JUcEZKqFKR7HhpY2D29IKDSFYRRjcnR5jX0TRteY-yowqjXJfYDo5MJXBVog5pQz7pR1eayri1pceXrHlnQjCRuttqdu4WTOvj0dyDC6T-ySI5vqdjcuk_x2rZeKlBGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132415" target="_blank">📅 14:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132414" target="_blank">📅 14:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132413">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7n0vBzYr9z5BDOp5EpoI-AdG6rNNxoWJLaqybXbBU8BpBJcvqaWqWgTEfCeSPXmJS0pul2TL-nDdxEcwluMt4rjbvYmNj103O0jRRIq8_CydWOUmFhMgcOpWV4bZQ428iqcfuMrdtO9enHw8cp2vZXAKbx5OgxtqiPo4vdNaLq1IBgatWjvuqgKI6ID5n_IBewFJDXmjlDsoQb5-s_oG-JkPJnmihBNwShnokc5hallTYi56LZ4SwGyBxYsSs9lHAZtXXU5kCTP5Wp4u2kkpXZjgymOIYFpBw2keSa-Xg4HtJGnMe3HzpJEuj74st5Yz4-lMmNrYBj0jEli4etESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132413" target="_blank">📅 12:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132412">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
*یک مقام آمریکایی به الجزیره:*  ما تأیید می‌کنیم که ایالات متحده و ایران به یک یادداشت تفاهم در مورد تنگه هرمز و مذاکرات هسته‌ای دست یافته‌اند.
🔴
توافق بر سر یادداشت تفاهم با ایران در انتظار تأیید رئیس‌جمهور ترامپ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/132412" target="_blank">📅 11:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132411">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فرزین معامله گری، علیرضا همایی فر، علیرضا عنایت زاده، سهیل صحرایی، محمدحسین صادقی و محمد گندمی به اردوی تیم ملی امید دعوت شدند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132411" target="_blank">📅 11:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132409">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
مدیر برنامه‌های اورونوف به باشگاه پرسپولیس اعلام کرده که حاضر هست قرارداد اورونوف رو تا سال 2030 با پرسپولیس تمدید کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132409" target="_blank">📅 10:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132408">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yq1caORF5HiDX7CHRI8WV_sFFBgFgICMmYqdZ4BDpXlIfciQTrc_3fHvEOn5d_apVoAOFuMUe1Ks_Q-T6nVX9XkShsm6u_XKQiOKsAnHBQjs6lk6f4hvy6solZz1NgT6DJTmxH2WGhNQ6tCxYEtZVBd1tVY_R55I1j8GFe6oD97Nk69_JJSVgPLSJ6mlDpIZ3XWlueHTi-62CSJY8vX6EZeDvux9sbrnuBMPiO5Qjgp7Y-5Kd5FFz_R-PYYvuCEKGUD5pGJfBHPc3wBFy_8QY67SY8YH7xDe9FF3weB967H2KdlWK5Nq9n-yRV10gvirqqGRX2otIyVzR2bAJk94vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوسمار ویرا به سبک بازی مهدی هاشم نژاد علاقه‌مند شده و به مدیران پرسپولیس گفته است تا شرایط جذب این بازیکن را جویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132408" target="_blank">📅 10:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132407">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M2FEPyv0irHgQ-0U3pnKuokRot8QbNCm1Bb-p3kZv5e-6GUeQe4O_4wUj4Q6m_VskF843-GeUSL3bk12085BYjf_58xe_Xe5cvbDZCc8pWUAz1_xQpWqvyKt6A_vmS0jZEVgdKn_gVxZhp0aUNV0d1MiW-Y2ye0WuQ8hOXTXWNQphe9asBAF9fG_xJs2K6EN7565AMtXcboSg4Sj7FO-ZCzSe0GB2qs1YOhDfxhePqdg3-HqHGl0g5Xqy3IbDd6iH05VOCxhjGAPSfhQ_nYjdsQvedOBA8wV8HrvockgSjv-IzccSOy61fAqiR7bh7Zm9s_eaU7MN6CpYg8pOwq4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آریا یوسفی علاوه بر پرسپولیس، از تیم الشارجه امارات نیز پیشنهاد دریافت کرده است.
✅
ترجیح سپاهان این است که یوسفی را به یک تیم خارج از لیگ برتر منتقل کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132407" target="_blank">📅 10:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132406">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
🔴
وقتی قرمزآنلاین فاش کرد محمودی از سوی ایجنت ها محاصره شده و برای تمدید قرارداد هر هفته یک ایجنت را به باشگاه فرستاده متهم شدیم به حاشیه سازی اما انچه گفتیم حقیقتت بود.از او خواستیم مراقب باشد.محمودی از برترین استعدادهای فوتبال اسیاست.
🔺
احسان خرسندی، سرمربی…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132406" target="_blank">📅 10:29 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132403">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR5XOjkMkyTE2cDQ3Nj9OtMRg_91mjwjAfQC9NPJK1iZKfjqbnKzccGuS4QWsjSHyQ9jQobf317EpZ09e10jGb4ijIQEtXn0z5NROoI1V74C7VuYtw8Pnfap7wbTWbPxhtRecdf9xuV4yAwkfy9ZcG45_c31Qfe7eVRF6JvfJ_HyZQlRsUwXEisvjBElGxXtsLK8h-KS9l8bpBBczvCsvTUx9EqqMVMgVDqp_rOO3gGbWyFCPabAQWcxqMZRXy5EQzjIlyl8ZuFFTKDRy5OV84Hf2t-CZGiKoGrmI-0bd0CoMoJ1Ilh-62_552EfiT44xllTTUYyHvd2QzT1EGp3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🤐
دیدار ششم از فینال کنفرانس غرب رو بین دوتیم سن‌آنتونیو اسپرز
📀
و اوکلاهاما تاندر
🆗
رو در سایت اسپورت نود با آپشن‌های متنوع پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132403" target="_blank">📅 01:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132402">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
خودمون رو گول نزنیم ، بازیکن خارجی با کیفیت نمیاد تو کشوری بازی کنه که ۴۰ روز جنگ رو پشت سر گذاشته و هنوز هم هر لحظه امکان متلاشی شدن آتش بس و آغاز مجدد جنگ در اون وجود داره
🔺
اما آیا این اتفاق و این جنگ باید بهانه ای برای انجام نقل و انتقالات ضعیف برای ما باشه؟ نه به هیچ وجه ، جنگ پیش اومده ، پنجره بسته استقلال و مشکلات مالی سپاهان  باید باعث شه که ما به سراغ بازیکنان جوون و تراز اول داخلی بریم
🔺
امثال دانیال ایری ، مسعود محبی ، فرهان جعفری ، مهدی گودرزی ، پوریا شهرآبادی ، بهرام گودرزی ، پوریا لطیفی فر ، کسری طاهری ، جوون های سپاهان مثل لیموچی و حزباوی و کلی تلنت دیگه تو بازار داخلی وجود داره
🔺
حتی لژیونر هایی مثل محمد مهدی زارع و امثال الهیار صیادمنش که جام جهانی رو از دست دادن و نمیخوان جام ملت ها رو از دست بدن هم میتونن جزو گزینه های باشگاه باشن
🔺
این پنجره بهترین فرصت برای پوست اندازی و جذب بازیکنان جوون و تلنت لیگ هست چون رقبای متمولی مثل سپاهان و استقلال در بازار حضور ندارند و پرسپولیس و بانک شهر در جنگ ۴۰ روزه دچار مشکل مالی نشدند و اکنون وقت خودنمایی پرسپولیس در پنجره نقل و انتقالاتی است تا سال بعد با شایستگی و بدون حرف و‌ حدیث به قهرمانی برسیم و به لیگ نخبگان بریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/132402" target="_blank">📅 00:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132401">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47978b8339.mp4?token=bxC-ypL4xk9dGhfhjUU7EAkeF83Jd5WX-8pPOaJghpFXYB9CyVYkEU9stNb6aY8SiJrpy22uhaAAnlIbCz7RtxGx8P06R2nqaTbnRRNRABNHybDfDDRK8glb3_AvvfQe26kYgbcVS5ciNMTjhOtKQ55Pq8vHNu4np_R6ldio-Ou3i8XT7ND3Yuix7bM8SjCJeMu6L6BF1l9diSLWBbHiYFGVVUdlcL__kTEwtHzQv6gJmanLDDHdrJKr5YYZVWb6B6MZ1Y3QebZcXkvSt1o0e_a8YPWXeHNXpiw2JBrUC6wtR_xORPHG00cJNoiSbgkYQJahWARV6xiOzknw4nm5qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47978b8339.mp4?token=bxC-ypL4xk9dGhfhjUU7EAkeF83Jd5WX-8pPOaJghpFXYB9CyVYkEU9stNb6aY8SiJrpy22uhaAAnlIbCz7RtxGx8P06R2nqaTbnRRNRABNHybDfDDRK8glb3_AvvfQe26kYgbcVS5ciNMTjhOtKQ55Pq8vHNu4np_R6ldio-Ou3i8XT7ND3Yuix7bM8SjCJeMu6L6BF1l9diSLWBbHiYFGVVUdlcL__kTEwtHzQv6gJmanLDDHdrJKr5YYZVWb6B6MZ1Y3QebZcXkvSt1o0e_a8YPWXeHNXpiw2JBrUC6wtR_xORPHG00cJNoiSbgkYQJahWARV6xiOzknw4nm5qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری صداوسیما:
◻️
آقای حدادی چه گیری دادی که باید حتما در آسیا حضور داشته باشید؟ حتی اگر CAS رأی بدهد و امتیازات تراکتور و استقلال کسر شود و سپاهان هم مجوز حرفه‌ای نگیرد، پرسپولیس به آسیا نمی‌رود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/132401" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132400">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
از بین شهریار مغانلو و علی علیپور؛ یکنفر از لیست نهایی تیم ملی برای جام جهانی 2026 خط خواهد خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132400" target="_blank">📅 23:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF5qKGphP3v4jJ52niOlVyS9osYjOX0PSbFlMsnECA8dijk-JNp6ksWINcjT_QXJURUCwNODiM9VQRAKZd0_t-BAONjCz3XrcQ-DplTlC-CLNfCMkdQhGWSEN6CrEmLrFppngleiLtuR54o_AfN7-7tgxUqHDoI-Cf5LjHaNKgfwQYEyklU-KqvKhJt4XuOcGk4s-A1BaX2Hv-FIbcDmatnOaqug677oyCV1PJiHcgnBnhl9oQNCR3SxueQogNWIeP4emdNjRdf0f7vGlCQ8ldpRTMyBibpAw6pCIo_E7QMfu_u56ngvaQJlgcQMnJxZy9ceo6zn3Qu9Deks5pnbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی:
اگر با سروش رفیعی و میلاد محمدی برخورد نکنیم، توهین به بقیه است. به هیچ بازیکنی اجازه ندادیم که سر تمرین نیاید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/132399" target="_blank">📅 23:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس:
🔺
بیشتر پیشنهادات ایران در مذاکرات پذیرفته شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/132398" target="_blank">📅 22:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132396">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
سی‌ان‌ان : ترامپ تو تلاشه قبل از تایید توافق با ایران، مشورت بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/132396" target="_blank">📅 21:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132395">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB9CD4iTRmiMRxkXqY0SWLtBHo1rzbrfyaBNoBMwVxR_LYQUp4Kg3JdhVb74Zi03PMwL9P0LMbz5YiK8Y4O_NJO7AIbu_bE67ZNQmIhoz92Sv871XhuiCxd4oXCPclkrjf5qLHNQ-HZ_Q-8zMEX2l431GZ2O-_aEU1V93nXdpK3W8lK5XU6RcxE-vlKZcw0xDd4agcMuZ4biChhA8gCgjxriZs8E5dIV7oMhiDK4DjHauUT52DflyoDLU4ZgWuGWkaPWGM3EdFJ--sklwVa8qe34BqG5EE7OpGhUYN2sTq3687sABWvZCwJOhz2SD_9TsnHd6eg3m3uPPK3stay-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کیت‌های ایران و هم‌گروه‌هایش در جام‌جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/132395" target="_blank">📅 21:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132394">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
*یک مقام آمریکایی به الجزیره:*  ما تأیید می‌کنیم که ایالات متحده و ایران به یک یادداشت تفاهم در مورد تنگه هرمز و مذاکرات هسته‌ای دست یافته‌اند.
🔴
توافق بر سر یادداشت تفاهم با ایران در انتظار تأیید رئیس‌جمهور ترامپ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132394" target="_blank">📅 21:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132393">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ll1F4DYF5vfhNwrgCn576ZO-OXb-B8QwdAbHtNvQGEK5Lct-YsvbF22x7giPWI7rvbhJOk17pI5V4JnvWQ2t64NtRF4GO-nVUZD1QUWpQ22OcnhriFN5_NqSQfsSQfFOFBvhStlJktMjdl5Jp_g81nCg0ylVQHak7xzttCgeR-bg-ttABH5PKkYzCIJzVPdpm6qgPU_WZjn_AlRNWmPHvIG1zBgpwqy_e1tOEwjO6of15ht53pNbIbhlnJe9AxBTJbBh3bZhl5Xnru9bUv0VaIQhWdVzDlhIYuurer_1OhQHWrXnH8B9SPsNAsflM03ns4sz6TZMnU4x3uVmreoBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کشور های دارای سریع ترین اینترنت موبایل در جهان
❌
ایران اصلا حتی تو لیست هم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/132393" target="_blank">📅 21:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132391">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
ادعای العربیه به نقل از یک منبع دیپلماتیک :
🔻
توافق بین واشنگتن و تهران در دو مرحله خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/132391" target="_blank">📅 20:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132390">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDfdpSbUxvTAUCjpl4mQrHUd-KJZQJ1eZcVlwIPLM_joZBzf4LuHETvflTl4meKc1QN7e_8bnJQzwhaMx1_tWzNpJkKMD0_2b6vjC9gV53GiGsdTeGgkJkIBH0U-II48IcZ1u80gp26WW4sZ719o72WQV8BNO1bdEpFBxIXfSHxX6kvjYa3LpEYPiFXkfLrxEkHGGSdmMkr0dObVBJn4JjipF0cIiX7M9qCu0lPTPh7qssA-PqdImli1Fs2voMJhb_ZJgRRvoge-KkeTcglsbj23XFMiffMcp9fV1OvW72xfB0jg_BYe6tvDaBSEtmh_ObYLC7WFyQPj_wDt5nfdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132390" target="_blank">📅 20:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132389">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gCVrsyPaf0s5Y9GgozxQbspKbPl4iwUbEUdpjP1mlQ_1wW_n7U1ZxHEIF-g1EU7TVt5PT_ou39Gml6a1VxAhRYUFFTdjGp3_snwqdPASPvj_gWn1I-XlToLZpLCxShizJ966uLxVcS16LiApS4CA06ExaSuYJjjXHIRDNMz-8l2Izacaauw5cx4uwkLOOvPAmtei-93AnChPhwxmZTeTuXxuH_gJdGoBcgAUqHhHpl-cE962Dcz4niJCXy_wrkOBVGeL013totlbTPmk1R0VpXCU6zf29ChTCyCUT7QhqFuT9XcPVr1E_97Bp9M196E2TVmfn_jYopkteS7Wp9euxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ادعای العربیه به نقل از یک منبع دیپلماتیک :
🔻
توافق بین واشنگتن و تهران در دو مرحله خواهد بود
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132389" target="_blank">📅 20:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132388">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
مبلغ رضایت نامه آریا یوسفی از سوی باشگاه اصفهانی ۲۰۰ میلیارد اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132388" target="_blank">📅 19:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132387">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132387" target="_blank">📅 19:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132385">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132385" target="_blank">📅 18:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132384">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132384" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132383">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132383" target="_blank">📅 18:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132382">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
طبق گزارش Axios، این توافق شامل موارد زیر خواهد بود:
🔴
دسترسی بدون محدودیت از طریق تنگه هرمز بدون عوارض یا مداخله از سوی ایران.
🔴
محاصره دریایی آمریکا نیز برداشته خواهد شد، اما متناسب با بازگشت حمل و نقل از طریق تنگه هرمز خواهد بود.
🔴
تعهد ایران به عدم دنبال…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132382" target="_blank">📅 18:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132381">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132381" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132380">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/132380" target="_blank">📅 17:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132379">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
آکسیوس: ایران و آمریکا در حال حاضر به توافق رسیدن و فقط تأیید نهایی ترامپ باقی مونده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132379" target="_blank">📅 17:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132378">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132378" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
🔴
🔴
و تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132377" target="_blank">📅 17:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">💬
🎙
🔴
عبدالصمد ابراهیمی، کارشناس حقوقی:
🗣
شکایت پرسپولیس از فدراسیون و سازمان لیگ زمان بر است و رای بیرانوند قبل از جام جهانی صادر نمی‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132375" target="_blank">📅 17:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
✅
خروجی ها احتمالی پرسپولیس:
🔺
میلاد سرلک
🔺
امین کاظمیان
🔺
مرتضی پورعلی گنجی
🔺
میلاد محمدی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
سروش رفیعی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132374" target="_blank">📅 17:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvlU3LT6D8Hf2jpgOQxaCBnrHojLqgAHcXFEIN7IbLTp6qSU6trFRstl1qeVJxsQZNrxP0h1YJtyO_wqH468K_UZNIpWSC4KMQWyCQTgbVcFgQ4RTp4uq-gC9_Wn98R-NNVEyZIJhPH27EwttVeNSGGnPSxq7D4Ta8-kKJ3sLHAY77U27gfh67VdFn1edAaYyYjJGPGx-RbGcTVRPqXpd1VFABwgDrK8F-goyfLosydUPN-8W4OWkJDZpTjgHG8vhXHHcpKcrIujyctp9mKDB-bJMrxwYTvn1fxAkpFi0z1-mwOP7enQEkeTqwhhwPCMUaZVv0op4SwtcRTKBbsKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132373" target="_blank">📅 15:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
فارس: هنوز جام‌جهانی شروع نشده اورونوف از دو تیم روسی روبین‌کازان و دینامو مخاچ‌قلعه پیشنهاد دریافت کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132372" target="_blank">📅 15:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
مهدی طارمی - شجاع خلیل زاده - دانیال اسماعیلی فر و احسان حاج صفی تا این لحظه به دلیل خدمت در سپاه ، احتمال صدور ویزا واسشون پایینه و به جام جهانی نمیرن ، البته فدراسیون درحال رایزنیه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132371" target="_blank">📅 15:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132370">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
سپاهان به بازیکناش اعلام کرده فصل آینده با کمبود بودجه روبه‌روئه و احتمال فروش چند ستاره این تیم بالاست؛
🔴
پرسپولیس و استقلال هم می‌خوان از این فرصت استفاده کنن و برای جذب بازیکنای کلیدی سپاهان وارد عمل بشن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132370" target="_blank">📅 14:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132369">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7O8-1TFGWbVo5OtP5YiQ5Z3OsE3gLhsKoO5PWAeb8GcNoYwTtfsxHMBPjKGTcXidK888PeQJDGxDXjmLcZOpgD_6Qvy7eo46aHbcJpft_4aZl_jdzTud1tN0ADfZRpGZIwTK_QRsPIwkI-wXzRPj8xsA17OedTOtxl8KSGNrmJj431JHvEN6xjnjWpg3eXcKMlLDxgASC1cIutuswD1RhWPJ2RDGOGqiUIOKs5wrdfpXLHmtH_VWyhocI0TJhQGXDpAkOG3en1O17pViGvfhc5hRfOhUvasXA5MOQjeNlyV4kEi9DtzU7GXBziWRgoRlzjM2akVu4g2vEmW9zBjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132369" target="_blank">📅 14:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132368">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
فعلا تلاش‌ها برای بازگشت سردار آزمون به تیم ملی جواب نداده.
🔴
سردار حاضره پست عذرخواهی رو منتشر کنه. قلعه‌نویی هم گفته هر طور شده سردار با هر تبصره‌ای که هست به تیم اضافه بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132368" target="_blank">📅 13:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132367">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🎙
‼️
پیمان حدادی:
‼️
🔴
برای بازی با ملوان به دادگاه CAS شکایت کردیم، سپاهان و گل‌گهر هم قرار بود شکایت کنند. امیدواریم سه امتیاز این بازی را بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132367" target="_blank">📅 12:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132366">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎙
پیمان حدادی:
🔴
ما هم می‌گوییم استقلال نباید معرفی شود؛ در حالی که نماینده پلی‌آف در آسیا نداریم؛ بعد از جام جهانی در کنار لیگ حتی می‌شود جام حذفی هم برگزار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132366" target="_blank">📅 12:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132365">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🎙
پیمان حدادی مدیرعامل باشگاه پرسپولیس:
🔴
با چند بازیکن وارد مذاکره شده ایم اما هنوز از آیین نامه نقل و انتقالات برای فصل آینده خبری نداریم. نمی‌دانیم بازیکن خارجی می‌توانیم جدی کنیم یا خیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132365" target="_blank">📅 12:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132364">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1izV-0aMC9WDD9eZg215QQ2A6yt7Afi9UUCMEKSMYmsCMWD4yc6eOJOxlFsx-wDaPRS2jd-mCuVP9SKR-chaAN1bRHW2SrNbxQTOanrAe8JkliDcGrh4tJHqBYr074zyiaPSii5pgrQjiKSRsvG6RNb7ZHw7FDLUbZhsnpI1P6-qEgocUDgdbBqGnmurSpk1EZpLrFNnRGng-pGkZyVbKCimKUSs65aLMJzimSnue8P0wuOeLePx_deCXL3wktTM_T8ut4lktcduI2q-dS_o9igD4QkdTnHKFKunpGerUHt4tVGDdU7OgKymeG1VUa2jMRDI8A47SSZWVE-y6IAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#روز_شمار_جام‌جهانی2026
⚽️
14 روز تا شروع بزرگ‌ترین و هیجان‌ انگیزترین رقابت فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132364" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132363">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#فوری_مهم
🚨
🚨
گویا سپاه امروز پایگاه آمریکا در کویت مورد هدف قرار داده بخاطر حملات دیشب آمریکا به بندر عباس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/132363" target="_blank">📅 11:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132362">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
🔸
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132362" target="_blank">📅 11:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132359">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
خبرآنلاین: سردار آزمون حتی با دستور رئیس‌جمهور هم دیگه نمیتونه به جام‌جهانی بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132359" target="_blank">📅 09:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132358">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭕
تلاش بیهوده برای رفتن به آسیا یعنی حماقت اون هم زمانی که حقمون نیست که به آسیا رفتن فکر کنیم
✅
باید بپذیریم که اگه شرایط جدول برعکس بود و ما صدر جدول بودیم و لیگ نیمه به اتمام می‌رسید حق خودمون میدونستم که به عنوان سهمیه ایران برای لیگ نخبگان معرفی شویم
✅
نه به cas فکر کنیم نه به تلاش بی ثمر. Cas تا بخواهد به پرونده رسیدگی کند سه فصل لیگ نخبگان سپری شده.
✅
برای فصل بعد برنامه ریزی کنید. تیم را بسازید‌ ریشه ای و بدون بازیکن سالاری...
✅
پس بکوبیم و دوباره بسازیم.
فرصت ها را از دست ندهید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132358" target="_blank">📅 09:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132357">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB8yBrQXsybYE43ZbK8U7oty1Nuf1UBmsTvT2GOFCfoA83B2cb3t9NWVmSuXoYaN6eAb7B41PO2PNx-BZ8Bl_dt7Jmy6LoSkSA0Fpo2xMgdKxs6cT48j0hLUUnJXaDJG3dSgxFxFcSmP1gOa-rp7cry_wcA8ZPcBHcWjFly7sIMzS2arJ4EQGEHbrVBqt4V2v3oWK7p2l_rnuMjRhRZv2YhoUy5jrF0IslrDmQsr1uPZXu01RkvKnaST0mKXGbMlqPfwk3b-cstY7ZmU2Ke985M_3-szcxO5FqKlEJLJlm2rSWYAT6cLG6ZyL9nVez4GhxgjuNVyCbQ3IdOuRS8SYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار برنامه ویژه‌ای واسه پایین آوردن میانگین سنی تیم داره و باید با اکثر بازیکنای بالای ۳۰ سال خداحافظی کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132357" target="_blank">📅 09:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132356">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
تسنیم: ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.
🚫
در مقابل، ارتش تروریستی آمریکا به زمین سوخته‌ای در اطراف بندرعباس شلیک کرده‌اند که صدای انفجارها مربوط به این ماجرا بوده است؛ این شلیک هیچ خسارت جانی یا مالی به همراه نداشته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132356" target="_blank">📅 09:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132355">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRwZowSKWTB-kwS2NxrAmGhigANyVzzAI0p3CmU3x797-F1_60JssrFft9eWRqkVru6BW3I2R6F7Ef5C0Km0mLXhBhXyLIrnLVfqKiL58BeiVZ5U5zJmQfOermm982ynJa4lS1oMf_ZMhEo9Nv132oiKWGhIAmdU8PjLT4DqgIyW-G_x003yn4TtSJdg0tNj0oxjre9igC91Pq2fH5dblMYe91P1OpMRL_XP4IaFjEqNt4uqZMg0jh5HuI_gNL28H8uQJ7VHd4tsiTwKM3p8sInM8f7hBfVQ6h4RCQuTl4Ps5EiLdYeZnIcnLezKE6VHO7s51B87VKqDobCTGU0PTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/132355" target="_blank">📅 01:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132354">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
رضا درویش:
صحبتی برای حضور در هیأت مدیره پرسپولیس با من نشده است.
🔺
در ورزش بهتر است هر فرد پس از چند سال فعالیت، مدتی استراحت کند. همان‌طور که یک پزشک پس از انجام جراحی‌های متعدد نیاز به استراحت دارد.
🔺
فعلا ترجیح می‌دهم دور از فضای اجرایی باشم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132354" target="_blank">📅 01:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132352">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
گوگل پلی رفع فیلتر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/132352" target="_blank">📅 00:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132351">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
خرید بزرگ پرسپولیس از اصفهان میاد./مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132351" target="_blank">📅 00:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132350">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
🔸
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132350" target="_blank">📅 00:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132348">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
ترامپ
🔴
کنترل پول اونا دست ماعه و وقتی اونا کار درستی انجام بدن و چیزی که میخوایمو بهمون بدن ما هم پولشونو بهشون میدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132348" target="_blank">📅 22:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132347">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
نت بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPNها هستند!
🔸
کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPNها…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132347" target="_blank">📅 22:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132346">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
بودجه سپاهان برای فصل آینده مشخص شد
⏺
باشگاه سپاهان بودجه 500 میلیارد تومانی برای فصل آینده خواهد داشت و به هیچ عنوان تصمیم ندارد از این سقف بالاتر برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132346" target="_blank">📅 22:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132345">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
🚨
حمله وزیر ارتباطات به مخالفان اتصال اینترنت:
❌
واقعا شرم اور است بعضیا نمیخوان اینترنت وصل بشه، اینها فکر میکنن اینترنت تو دوتا پیام‌رسان خلاصه میشه اما اینطور نیست
❌
من و دکتر پزشکیان با قدرت جلو میریم تا بهترین اینترنت رو در اختیار مردم که حقشون هست بزاریم…</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132345" target="_blank">📅 22:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132344">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
🔴
ترامپ:
✅
به درخواست نخست وزیر و فرمانده ارتش پاکستان، به ایران فرصت کوتاهی خواهیم داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/132344" target="_blank">📅 22:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132343">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
بودجه سپاهان برای فصل آینده مشخص شد
⏺
باشگاه سپاهان بودجه 500 میلیارد تومانی برای فصل آینده خواهد داشت و به هیچ عنوان تصمیم ندارد از این سقف بالاتر برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132343" target="_blank">📅 21:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132342">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
الان به نظر میاد خودشون دنبال توافقن. فکر نمی‌کنم حق انتخاب زیادی داشته باشن  اینترنتشون تازه دوباره وصل شده، اقتصادشون هم داغونه، تورم هم خیلی بالاست!  شاید مجبور بشیم برگردیم و کار رو یک‌سره کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132342" target="_blank">📅 21:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132340">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
بودجه سپاهان برای فصل آینده مشخص شد
⏺
باشگاه سپاهان بودجه 500 میلیارد تومانی برای فصل آینده خواهد داشت و به هیچ عنوان تصمیم ندارد از این سقف بالاتر برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132340" target="_blank">📅 21:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
❌
مرتضی کرمانی مقدم:اعلام قهرمان؟ اگر دست من بود می‌گفتم همه تیم‌ها به لیگ پایین‌تر سقوط کنند. مگر کیفیت مسابقات امسال بالا بود که حالا منتظر ادامه آن باشیم؟ به معنای واقعی کلمه هیچ تیمی مدعی قهرمانی نیست و از این به بعد حتی اگر مسابقات برگزار شود بعید است کیفیت آن تغییری کرده باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/132338" target="_blank">📅 21:36 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
