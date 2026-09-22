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
<img src="https://cdn4.telesco.pe/file/h96nGzkQy63eRxG3JAWldUtC2NgiS2k6G2yVQfNR2JZNncjS-ItERj74JEQiXNNEA7_Lgmm36whuIAA5aR6HPrDMEuVVNlrACQk4Qkg7UpvTWejmxe1WQOsz6Ai2QdZm29nkluePeYL6bN4ewO6MA2KLZLp9LMb6S9mXqPRe9XFYamHbtTomtSF7_43tekxkSrN_aR1PxgLBpWH0U_4yI3TBAdEZFthqnkAIq0LSxLuPfsbtQACAlx4rPsksaGvcKuw0x9ppfLKIdmTB8Fz4O5vWqDX7vSnW-f3fH2eg4Y_o_416eLqibJSz0FNxs3h2Vxs6BVMQir4TCaKp0miN2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-140408">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🚨
🚨
⚽
محمد قربانی: بنظرم در الوحده ماندنی هستم باشگاه رضایتنامه مرا صادر نمی کنه
🆕
👀
چند بازیکن جدید قراره اضافه بشه اما من در لیست فروش نیستم چون الوحده هافبک ندارد  ‌
📎
اینجاست که مشخص میشه چه کسی دنبال فالور گرفتنه و چه کسی…</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/140408" target="_blank">📅 17:35 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140407">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: حسین کنعانی زادگان به تیم ملی دعوت نشده است که هیچ ربطی به مصدومیتش ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/140407" target="_blank">📅 17:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140406">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d84777f345.mp4?token=ujGeEeLoNTttbmaiqAZnStmgco0h0AalSmzf9Y7oU3AgW-Xs4erlkHLZzUNx5SGL79M0-GiseTqGuEfWejzMgIMPgs3d0K2_qqdYuM6Xyq-cubrypHxuW9dG_puofo50XDqxKxvIxtyztrmeHPXZlFkppBNMBRHABHARFZAWMvxx61ketdrVNjP7MCDl5wfzSJ_c7geSVjr-mQngWh9qAmFUI-L_LzEvpIpN69056PNZyAony9AYBCUDzZCVVvYCzblEqB7i5caSI3X2Go0VNKM31Oe28Uz-HpU08890P-Z7TMIT2UkVQxjQ1jYLVHKoSSiWuN3ntg87MfOosvgC4LAKM-s2FWoajD5VQzD3ofMBbz1Xvdc-wzJ6AJOUq3yDlugsPtz3ZYfykb-_qrLwXQsWwcTB0j-_d--1D73q06XEDQL33MfWNIn1bqQmyMiUg5f3aG8peWxVToTUvqlOlRKwULZgOqixzXNNi7PlYivJsthdhQD_RXYR6AolfxnbYW9-8AOWPdvhW7oJlnpeJ_AozSJoJj6KpzVH8XVTa8GXLjZ_TMo4f3RCqGhPGZZU-3yPVcYQpaCNZfS5UdbI-a_HzaOBOLR-vSqsxNAW9S8k27SJzTxP41SAC42fBf3S-7ghLBoiwhYtl3J7BxxIGRg-zDTpFucfgdA1tjmXxIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d84777f345.mp4?token=ujGeEeLoNTttbmaiqAZnStmgco0h0AalSmzf9Y7oU3AgW-Xs4erlkHLZzUNx5SGL79M0-GiseTqGuEfWejzMgIMPgs3d0K2_qqdYuM6Xyq-cubrypHxuW9dG_puofo50XDqxKxvIxtyztrmeHPXZlFkppBNMBRHABHARFZAWMvxx61ketdrVNjP7MCDl5wfzSJ_c7geSVjr-mQngWh9qAmFUI-L_LzEvpIpN69056PNZyAony9AYBCUDzZCVVvYCzblEqB7i5caSI3X2Go0VNKM31Oe28Uz-HpU08890P-Z7TMIT2UkVQxjQ1jYLVHKoSSiWuN3ntg87MfOosvgC4LAKM-s2FWoajD5VQzD3ofMBbz1Xvdc-wzJ6AJOUq3yDlugsPtz3ZYfykb-_qrLwXQsWwcTB0j-_d--1D73q06XEDQL33MfWNIn1bqQmyMiUg5f3aG8peWxVToTUvqlOlRKwULZgOqixzXNNi7PlYivJsthdhQD_RXYR6AolfxnbYW9-8AOWPdvhW7oJlnpeJ_AozSJoJj6KpzVH8XVTa8GXLjZ_TMo4f3RCqGhPGZZU-3yPVcYQpaCNZfS5UdbI-a_HzaOBOLR-vSqsxNAW9S8k27SJzTxP41SAC42fBf3S-7ghLBoiwhYtl3J7BxxIGRg-zDTpFucfgdA1tjmXxIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
7 سال از گل مهدی عبدی گذشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/140406" target="_blank">📅 17:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💢
مهدی کروبی خطاب به پزشکیان: اگر شرایط فراهم شد، با ترامپ دیدار کن و برای صلح پایدار وارد گفت‌وگو شو.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SorkhTimes/140405" target="_blank">📅 16:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140404">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
ادعای عضو کارگروه حقوقی تیم وکلا امید عالیشاه: خداداد عزیزی با شکایت امید عالیشاه می‌تواند راهی زندان می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/140404" target="_blank">📅 16:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140403">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔄
⌛
بشار و فرهان گزینه‌های روی میز تارتار در زمستان؛ پرسپولیس به‌دنبال پلی‌میکر
😀
درصورت تایید مهدی تارتار مذاکرات با بشار رسن آغاز خواهد شد و فرهان جعفری نیز گزینه‌ی دیگر سرخ‌هاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/140403" target="_blank">📅 16:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140402">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این دیوس یه کانال داره به نام پرشانا ساکر که اونجا بازیکنی رو که میخواد بولد کنه جوری ازش تبلیغ میکنه که کلی حق دلالی بخوره.اکثر خارجی های کیسه رو هم این اورده سر همین ضدپرسپولیس و بنفع استقلال مطلب کارمیکنه کانالش</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/140402" target="_blank">📅 16:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm.m</strong></div>
<div class="tg-text">این دیوس یه کانال داره به نام پرشانا ساکر که اونجا بازیکنی رو که میخواد بولد کنه جوری ازش تبلیغ میکنه که کلی حق دلالی بخوره.اکثر خارجی های کیسه رو هم این اورده سر همین ضدپرسپولیس و بنفع استقلال مطلب کارمیکنه کانالش</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/SorkhTimes/140401" target="_blank">📅 16:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140400">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/140400" target="_blank">📅 16:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140399">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/140399" target="_blank">📅 16:15 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140398">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5s1DbE0UUFN9G3s_eg2evXeci2LRtKx0qXO3OkwwUVmBVKVZ_So6a4TWtK6ENkDogYkiSWdvAR6xhp7sPQ9KWhjLBZrJw-201q22cr3nrgHgXqKyLsqki6CcwITaAL87KEBEDLydxkUCqjsYkrinOEnydJlBfD76mEFAbT9BeP25z0TidufWNR65mjIuutwUXgRqe4Mqso4a2jvYQpbINRSGGgwtSh0RRjEFOkawZwCKLqnxX9U4Rm7BoM0fBKM1B-lsfB4lXmhUa0w5oG_8h3C4i_T0azBNulMBV3QYk_Llk2dyIuZ1vnxzzzP3DxOFiAuGJ8uydm1z3BUZOmjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/140398" target="_blank">📅 16:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140397">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎙
🔥
تیکه
سنگین‌ ابوطالب به خداداد عزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/140397" target="_blank">📅 16:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140396">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4e645be8.mp4?token=oinRbbCWOQwoZ_dkLOpjPK0XSjw_cJMsH2PTSXGChsDqWrtNO8SW2_xURyLA3B75U138CVkPcxW6DL4jsJWjuTTk0OeIIJE7rA1uHiKEstycqaUHCexO_C0Vvf7WkwnBwpINWkYysY8taU6KrhPB5a_bTlzIhdBlzzfiUa-Q81HEtL4UDk03J8HPr_SVApGtteMmt4xdVnHMedmNCw2TdU5z6IteUTrSgCkbpSPyr9LEos5V0onYJ9htxWQbkDc72zf0DUXvz4HdYVE7J2tvjow94UzG7mxfCdHcBMX6uv8NIdVkYXxbZI7bmF-tyG4ZhOl6DDenSAqoMe6e2ci5tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4e645be8.mp4?token=oinRbbCWOQwoZ_dkLOpjPK0XSjw_cJMsH2PTSXGChsDqWrtNO8SW2_xURyLA3B75U138CVkPcxW6DL4jsJWjuTTk0OeIIJE7rA1uHiKEstycqaUHCexO_C0Vvf7WkwnBwpINWkYysY8taU6KrhPB5a_bTlzIhdBlzzfiUa-Q81HEtL4UDk03J8HPr_SVApGtteMmt4xdVnHMedmNCw2TdU5z6IteUTrSgCkbpSPyr9LEos5V0onYJ9htxWQbkDc72zf0DUXvz4HdYVE7J2tvjow94UzG7mxfCdHcBMX6uv8NIdVkYXxbZI7bmF-tyG4ZhOl6DDenSAqoMe6e2ci5tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
❌
جواد خیابانی: فصل گذشته باید از تاریخچه حذف شود و هیچکس نباید قهرمان اعلام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/140396" target="_blank">📅 16:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140395">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXwWAJGP-YQ_6d125HS4HSz6Cod8jfgabWHZggGaqEonvyaF4t4Le07z60bBUuIkaEMPlZhf135RW0cFabLP81PwcrVmadQymWU-6544JzMICkB32DmlFecXH4Rf8W6DWob7eqboTl2ssJqDSHn7_Z0JRWhiHm22HuzrVPID_EA1lGYo7L99G5XX2AuCSJtxm3tbtfRTg8v_zKhN-gG71F_XcxrchnE271vgI-SZ8yxd8Uw38jW52jVa2LPP-2S_5xXXKj-rVWkq8bxqwEKgAdMGVwjIsQbt23Jr5eplH5VfGaYKH1nVydJXH0pHuV9zMhYOSJ_-h_qw22LtdG1-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
مهدی کروبی خطاب به پزشکیان: اگر شرایط فراهم شد، با ترامپ دیدار کن و برای صلح پایدار وارد گفت‌وگو شو.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/140395" target="_blank">📅 15:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140394">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T0nko1ZQFHVQsBogzGIks93N36Y-rjz8BHQJGfipVBSCD5ibkMBo62Rn3YUrLiaLsLZQTD4F4AOr03PThini76bLg8G3tnldaZkEhRjwII4qhpoLMZsGlDZZioVKXZh6jDGBFJjofeDy02_0wCCd3KOKubAC-yguoQ_hKG9oEytMix4Oz-0WDkjP_P-z19XdepAFejUZxscsELSEv1DHACY5ZIp0EMJZDs5BXtW6sq9yCRIjFBSNeExgC-Q3EdSzTB-EStNwcYPBOifVbcY9PqE8i2MH6_gq0wU9RF0lXLfgDJ766S4ydGjDeuMIY6noHQdvs6hgvSh-V-_mrHkvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری تسنیم وابسته به سپاه نوشته
:
🔄
دلیل عدم دعوت الهیار صیادمتش به تیم ملی این خالکوبی و حمایتش از اعتراضات ۱۸ و ۱۹ دی بوده !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SorkhTimes/140394" target="_blank">📅 15:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140393">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
خبرنگار دولت: ادعای ترامپ برای دیدار با پزشکیان آرزوی محال است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/140393" target="_blank">📅 15:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140392">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
داوود رفعتی: بنظرم داور دربی کوپال‌ناظمی بود اما چون تلویزیون رسمی پرسپولیس یک شب قبل از اعلام این داور رو معرفی کرد،‌ فدراسیون تصمیم به تغییر گرفت!
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SorkhTimes/140392" target="_blank">📅 15:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140391">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2ClG_Zo4UOgUlIJEs2hTWhdRz9in9Y0WyB2Q1qNpAH0dF2DS2vGWbUegh0G4CuDJhw75qnbTahODz4HxRHLeOKfQpt-Uhm20foB3SehghFoq4yi2cB-MORFsNLNEXe2n4MsgCtOei5YXrwyEfe7QNwMKr6b_iOWavtCwLDjs2aGLnjVdM7gwFoFA9qxNU-yzfYiZk6_iglIzZtKw9n4TaWc0IBr2AuNa8WAUvy6QhT5MjWycrmLES0BTSpRRjsUhXUGpSs_JfUXAu4O65fnFpTnavnwEEGJUqJs1wkQ4JxL9aR6j9i1vePcHg0YEuqAYTmsCKVxukvNiYSgEWGFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آلمان و لهستان امشب در یک‌چهارم نهایی یورووالی ۲۰۲۶ به مصاف هم می‌روند.
🏐
لهستان با قدرت سرویس و تنوع حمله، دست بالاتر را در این نبرد دارد. آلمان اما تیمی جنگنده است و در امتیازات حساس به‌راحتی از جریان بازی خارج نمی‌شود. اگر دریافت آلمان زیر فشار سرویس‌های لهستان دوام بیاورد، ست‌ها می‌توانند نزدیک پیش بروند. در مجموع، کفه ترازو به سمت لهستان است.
🏐
اوج هیجان همراه با اسپورت‌نود، سه‌شنبه ساعت ۱۹:۳۰ دوتیم لهستان
🇵🇱
-
🇩🇪
آلمان به مصاف یکدیگر می‌روند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/140391" target="_blank">📅 13:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140390">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hb0yK93u6sw3YKgQQZ4w4A2xdyxWnRv-o0EhahSotfr0szlHx-P8ftOLMtDEyqO2ABcIa8mUTmgRaimIlfjk_JGPxftlaoSuI9YPWrRtHceCGY0byOiIDphjg7z_NTQAs0A28hDgQp35eXJbpXMZFPUIhpNFIBcadss6AYreGyoPSFexDJdlaXbf_eRfcaN0HDyYrut2Nx7-GwG95hNEL80jiCeWJgYGOFXOE1_D_whsgjxY1Y-ZtGejKQhmdsmEPfeMjR0MXoD91XJ3xur_88bb6l1hTqut_IzXkDHTdy4i3-cIyQjDQHNSTeb1YzMd3IgriIkWPu9E_rRwvMO7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
بیرانوند برای فرار از سربازی، این‌بار به بهانه خالکوبی، دست به دامن کمیسیون اعصاب و روان شده تا شاید با برچسب اختلال روحی، کارت معافیت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/140390" target="_blank">📅 12:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140389">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
❌
پیام علیرضا بیرانوند به میثاقی روی آنتن زنده: اگر نظام وظیفه اعلام کند من چه زمانی باید به سربازی بروم به جان 2 تا بچه ام فردا می روم سربازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/140389" target="_blank">📅 12:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140388">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/140388" target="_blank">📅 12:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140387">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOCZBy0pIiuj6yZAfh0RzfOo-uPpfavC6w-Vfe54agdTmDlNZCi6rls5uug-_EFPVXYmBsUvdDJ3mc7ENMndjg616mhUeTdEIxycBqESBfXA6VANFfowZ092GlDF3yfwuAVWVG3w-_aafPX1xnG-yLl_uM1e0U6uauxBG0sGHHiCI7fpiOYJkXiDR1jv1Q-n6d5u5vhBA34sY9VPAqr6HHwb9vJ6Qf6GVruaW9rNTUmNZ4ix5g1UuadXEAI6m9g_hUgnEVG3cvbrYwEXDrrpzC9GSkYReePpeoQ6hjSYwiRy5XKPivuGymtbFkcwe61L65YIGWy2FtbnwUGyBM712g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
پرسپولیس در تمرینات هیچ مدافع میانی تخصصی دراختیار ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140387" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140386">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
⚡️
⚡️
⚡️
❌
سعید الهویی مربی تیم ملی: هیچ بازیکنی نبوده است که در این اردو به دلیل مصدومیت به اردوی تیم ملی فوتبال ایران دعوت نشده باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/140386" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140385">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
⚡️
⚡️
⚡️
❌
سعید الهویی مربی تیم ملی: هیچ بازیکنی نبوده است که در این اردو به دلیل مصدومیت به اردوی تیم ملی فوتبال ایران دعوت نشده باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/140385" target="_blank">📅 11:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140384">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
✔️
فووووووری از فارس
✔️
خبر ابطال شدن کارت بازی علیرضا بیرانوند صحت ندارد و این بازیکن تا زمان صدور رای کمسیون پرشکی میتونه بازی کنه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/140384" target="_blank">📅 11:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140383">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚡️
⚡️
با درخواست اوسمار ویه را ، امیر قزوینه گلر تیم جوانان پرسپولیس به تیم بزرگسالان پرسپولیس‌ پیوست و قرار است به عنوان گلر سوم در کنار رفیعی و نیازمند به فعالیت خود ادامه بدهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/140383" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140382">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚽️
صبح آخرین روز تابستان شما بخیر ‌.امیدوارم شش ماه اول سال و با دلی شاد و تنی سالم سپری کرده باشید ....پر برکت بوده باشه براتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/140382" target="_blank">📅 09:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140381">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsCrWojCXdiB6dg787rAYoHbcD7bBrvUGUK-D6sqvbrUexXgyCimyPnU_WAYJ5t6-k6kX7ECRGwRgHo9mu-x88V4XrdqVV5BVbUGzusnTTTg0rgAffUtPp3poOVKtEhP-iKZcxO_5NGXyyRATI-o7BFgEDAJgWvVfXOajLFhu7ERdecRtrnucoPhc6RCiaq9s_7kmA57inRDwX__TIu2WBYv_BHdcDFMV2LklbSGdZYbBEZzsi_K5t058idL5lK_CFAn_wfZn-HBnIZ9KyLcg2Rt6kYbTcIs6n-nRumyXI1UvGNBzPWkhRacVttX_QanIC4xINdOx6Z7meerXOtHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140381" target="_blank">📅 01:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140380">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
احمد نوراللهی بار دیگر پیشنهاد فدراسیون فوتبال برای عذرخواهی از امیر قلعه‌نویی و برگشت به تیم ملی را رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140380" target="_blank">📅 00:20 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140379">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
پژمان راهبر: علت دعوت نشدن الهیار صیادمنش مسائل سیاسی هست و تا اونا حل نشه امکان بازگشت صیادمنش به تیم ملی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140379" target="_blank">📅 00:18 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140378">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⭕️
⭕️
⭕️
علیرضا جهانبخش به پژمان راهبر: تا دو سال میتونم معافیت بگیریم و به زودی برای بازی در پرسپولیس به ایران میام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140378" target="_blank">📅 00:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140377">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140377" target="_blank">📅 00:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140376">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی : مشکل سربازی ندارم و معافیت دارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140376" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140375">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
✔️
ابوالفضل جلالی: هوادارا خیلی بهم انگیزه دادن و تو تمرینات هزار خودم رو میزاشتم. متاسفانه مصدوم شدم ولی الان آمادم
◻️
من الان طرفدار پرسپولیس، عاشق پرسپولیس و سرباز پرسپولیس هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140375" target="_blank">📅 23:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140374">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
ابوالفضل جلالی: من سرباز پرسپولیس و عاشق پرسپولیسم، همه کار برای هوادارای پرسپولیس میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140374" target="_blank">📅 23:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140373">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
ابوالفضل جلالی مهمان امشب فوتبال برتر است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140373" target="_blank">📅 23:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140372">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ابوالفضل جلالی مهمان امشب فوتبال برتر است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140372" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140371">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
✔️
احمد نوراللهی بار دیگر پیشنهاد فدراسیون فوتبال برای عذرخواهی از امیر قلعه‌نویی و برگشت به تیم ملی را رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140371" target="_blank">📅 23:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140370">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
فوووووووووووووری
⏺
باشگاه پرسپولیس بار دیگه مذاکرات شو با احمد نور شروع کرده‌ بود تا بجای قربانی جذب بشه و احمد برای دومین بار در این مقطع پیشنهاد پرسپولیس رو رد کرد‌/ هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140370" target="_blank">📅 22:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140369">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
کنایه فردوسی‌پور به فدراسیون:
✔️
✔️
استرالیا با برزیل بازی میکنه، ژاپن و کره با اروگوئه بازی میکنن بعد ما برای بار N ام با ازبکستان!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140369" target="_blank">📅 22:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140368">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: حسین کنعانی زادگان به تیم ملی دعوت نشده است که هیچ ربطی به مصدومیتش ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140368" target="_blank">📅 22:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140367">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a200ac824.mp4?token=LAmzQafdtBYJ0xhkZXEJVk5exWEZhWnFqejLAszwrpWLKMfx6-ZJj0OuPTfFs15TT8rAsX8lkjXpZW36TplMQ9FcS9I8qHclhk2aO3omgCMpvHXupFVjpk_3vCgNnSO8Txp8Q1Shi6_kFcobx2ISR11PAM2Nr-N62oFe6YXRxkgUHcSImdTyBL2IEbs4RvuZUGqzP10xgXgw5aSIuh1hjvoL7oskA5QMSm60fg6XistQsMfEZcI4KnGTrAxncrNl2-CBJdJnmDIbV0YQ_wB6LwCdNENiZFWWP1OwXSytiGjTuhZyJqWeI9BTE1xTaDPnxUPcZKlG9Ygnc7900I3LJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a200ac824.mp4?token=LAmzQafdtBYJ0xhkZXEJVk5exWEZhWnFqejLAszwrpWLKMfx6-ZJj0OuPTfFs15TT8rAsX8lkjXpZW36TplMQ9FcS9I8qHclhk2aO3omgCMpvHXupFVjpk_3vCgNnSO8Txp8Q1Shi6_kFcobx2ISR11PAM2Nr-N62oFe6YXRxkgUHcSImdTyBL2IEbs4RvuZUGqzP10xgXgw5aSIuh1hjvoL7oskA5QMSm60fg6XistQsMfEZcI4KnGTrAxncrNl2-CBJdJnmDIbV0YQ_wB6LwCdNENiZFWWP1OwXSytiGjTuhZyJqWeI9BTE1xTaDPnxUPcZKlG9Ygnc7900I3LJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
میثاقی: حسین کنعانی زادگان به تیم ملی دعوت نشده است که هیچ ربطی به مصدومیتش ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140367" target="_blank">📅 22:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140366">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
حمید کرمی مدیر اجرایی تیم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140366" target="_blank">📅 22:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140365">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
✔️
فووووووری از فارس
✔️
خبر ابطال شدن کارت بازی علیرضا بیرانوند صحت ندارد و این بازیکن تا زمان صدور رای کمسیون پرشکی میتونه بازی کنه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140365" target="_blank">📅 22:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140364">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idNm6D0XNuKfC3Q27_IcQJzDqx0wJRThcq1s_0vrmB7k1bnJIuPG02Qcht47tacQwCy7WG5kUZgJFlE5DZ6Gn-lCM-qqr2cXYIhHk1wp8D2BMaOSTTxnAXPxnNJWR3bf9-kd9xEi6uS5lguHnmeSIy83z_lT00mUsjDGVUptQ42NS1DcggSpjyWk_uwFXFUtVySI5Ry58FCeI5kKfoQC-UyUPxvpBSv4wBuHhzLsFtXv_b6fmoUegiV0i_cXDlWERiZM4tOKfBJkxTQGFYK7LCLKc7iPekWgcdLnar5QyiWjffjLiW_g3Zw4JVTLbE5dzFS5U92Qr8wRd0z6u2s2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
به نقل از رسانه ها دنیل گرا بزودی با گرفتن ۲۵۰ هزار دلار از پرسپولیس جدا خواهد شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140364" target="_blank">📅 21:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140363">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
✅
تیوی بیفوما که بدلیل مسائل سیاسی دعوت تیم ملی کنگو را رد کرده بود دقایقی پیش برای حضور در تمرینات پرسپولیس وارد ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140363" target="_blank">📅 21:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140361">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyO4Huj436f_UnGZTWRHVFolWtrJ6yQLBiGTdUl3pBDYtpufqLJrn23nXN1nA4rpusM4fq5pZPvEv7my4nmI2m8sx1cvsNHKRTmjT2Oz2NmAW-bBJo4xTwaLQlo4O_yfwOg-JsDELWGNTkUVMi30R-LGwM0MZ3n8D3_OGZ5C0c0DHP1u0W46mf45yBBd8SSQLPY9HBseeh-zUGW3SEJsN0q8GTbhqMTeHCPedURhnypILOfVe1Za7H4P0JrbkkITK4KspNJB0uQk96-2rtZ30LkZeqUfWRL5bMBYyNdJJM8kYDSLa3EunJiRyTowgShVuu7HAj7Z410L5eLARbpsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی جام ملت‌های والیبال به اوج هیجان خود رسید!
🏐
نبردی حساس و تماشایی بین اسلوونی و صربستان در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با اسپورت‌نود، دوشنبه ساعت ۲۲:۳۰ دوتیم اسلوونی
🇸🇮
-
🇷🇸
صربستان به مصاف یکدیگر می‌روند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140361" target="_blank">📅 20:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140360">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
🇨🇬
تیوی بیفوما به علت مسائل سیاسی کشور کنگو و در حمایت از مردم، دعوت تیم ملی فوتبال رو رد کرد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140360" target="_blank">📅 19:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140359">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140359" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140358">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
با ‌درخواست تیم ملی علیرضا بیرانوند تا نیم فصل اجازه بازی خواهد داشت تا در جام ملت ها آمادگی داشته باشد سپس به سربازی میرود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140358" target="_blank">📅 19:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140357">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js1nFshKzHhXpyStPfZzPtwRv01XFDMaEuSaYnoVacfqm08TVIhxuMDpjlO1EJDBXW3XwALZj-WeuXayqqVw8n7jSu8nMnKimfFfI13IXzOZuKmpvZ66OBJEt8W7T6NL8oab7zA1q2J0fHnglDyOKaSH71ayY85LEf1h0Lq3kAW7CzUr3cEmooN3WAvDylyOO6ETli9AqXJ50i-225PY-vIZWY5WGRhLUQv_Nhq7_xtmfQyWmSx8g2_tL0KKv4hsn7PZkBVZSmIaJA_c8t__aHLsaVfci2923AvFFXK0Dmw0NkB0V8t8dxl_ASoOsKclL0gH4JuIVqzqBnz0gUfLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمید کرمی مدیر اجرایی تیم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140357" target="_blank">📅 19:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140356">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری از فوتبالی
🚨
سازمان لیگ کارت بازی علیرضا بیرانوند برای تراکتور را باطل کرد.
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140356" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140355">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIR-KNc2bvbC-wa8RP1wuAwNb8Ao6fGcx1xsCHlQY8rlg8X4-kZbq8nLodyBr-XKyNxu-8beTmMlbmkN2l5kltqTbsGy7KqJxTI9mCyv51DSqh4pCO05BawDtud0v8B_pnhC28rj8NIEtVA-TaOdPhfF4CQa-o4KtoEzYd4enUXjtzR8CBYP6ssnn0sntiAFgC4k5KfDj_8xkwkM-g75z1NC7h_1Yug3jLbkjV_3WBslWlJkXZVyhZiFnSZ2SbiYilJKfPA6hY0JZ_MHzkpPhrBsAssAwWP6qc_FBJJqf38mbMjxiV6b5V6o5jVqeGv_tNvISu1rrM47Houi29c6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری از فوتبالی
🚨
سازمان لیگ کارت بازی علیرضا بیرانوند برای تراکتور را باطل کرد.
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140355" target="_blank">📅 18:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140354">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140354" target="_blank">📅 18:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140353">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWZneXv_fQvUVgXUQ_VfKcL1xaL3KQrWbeDaF7SBlqINp12EqaDFdh7kcyD5tUrZa5iKmzlEM7vydG03pTwcbk8FOOxUWnjTwPcL1PYVNMQo-0ypTLQrRcoPG9Rp4rde2_lLY4XttHY5MLFMxwS3nOcV8ZpVQu3pKsCht3RPx1CieJJ0a-7cZjS3UEJiGlLrHr9NJGnU8DqVsPmHq1_Q1IJv8qd0PYR1YeRHynvR8CPc3Odw6USrrwUNbwM33u1iPG03KPd5QvOBeoLFI5GLzeSB4P50LkCsulGOuctvsaAB7MPtHwOUws5nHfvxSvWt8L0kjcsmcgKtVIeoOreEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بسته شدن پرونده حقوقی بانک گردشگری علیه پرسپولیس
🔺
باشگاه پرسپولیس با انتشار اسنادی، خبر از تسویه بدهی این باشگاه به بانک گردشگری خبر داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140353" target="_blank">📅 16:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140352">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140352" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140351">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140351" target="_blank">📅 15:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140350">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
✔️
از باشگاه پرسپولیس خبر می‌رسد مسئولان این باشگاه در مرحله استیناف مدارک جدیدی علیه یاسر آسانی را نیز ارائه کرده‌اند و امیدوارند با بررسی این مستندات، رأی مرحله نخست تغییر کند/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140350" target="_blank">📅 15:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140349">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140349" target="_blank">📅 13:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140348">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVxLEwDdUNbNPMlXt3S7rjWnNcI_WN8vd5WXOG_9FnzLTU0ZljPNudxCFlV3m0b6oYUgQPHPRF3k4sPxSaCiGLjZJbkUobqmKL7NT-86y-Sja1YmmrAAxybqO56xu7WFt_8yYCPLaB9ZkewxJiumYpXzMCAgjFzPMny7WASRiJ0qhA4x3hhPoIw75FTSoLWkadnKHbzEQUeskk6Q9Gr9gij-JYCCQ6CgfejxCJ3-yIAEox5DPXlt-yeCssOihyhAKGdBobzCcQ7tKZ5BzI-EWmoY3p6w2GWk6Ae8nwsHB101I09aJ8jp2vd72Fo41sPDYQZVPmAEUjA6MV988Gx5KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140348" target="_blank">📅 13:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140347">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140347" target="_blank">📅 13:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140346">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibCF6rIqdQdp4mr7CgZJqQB2IvExMgWKmWVrup1DFZ6HSYNW0tK_yL0nwy0N7pY0JgzxyptHQiirWBgFidKNX4T2quI4mMnG1BzvmWLQtrAjalUJUABWyGrh8yJShcjgol79GvHnT_VljZ7SQy4oDrQUDjcfalSfz6e2MTY-2Lz0gYq97t64SPTYmIOktuXlEGc_GRB2XNKX52K1Btlo_vW4sfFueNXzJrO6yBETMcS5JBHSh9B3Rlt3ywME0WjfG5ZRvNwQ859zso_zN6EnlfSdjLR88SbPfyoKHSdQiYMzwBxDPygxHEAuLTboRqMAbqQFUCl3I-2DhRq93amaXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام ملت‌های والیبال اروپا
🇸🇮
Slovenia -
🇷🇸
Serbia
⏰
Tonight 22:30
🏐
اسلوونی با سرویس و بازی سرعتی از مرکز، تلاش می‌کند دریافت صربستان را از نظم خارج کند؛ نقطه‌ای که می‌تواند جریان ست‌ها را عوض کند. صربستان از نظر قدرت حمله و توپ‌های بلند خطرناک است، اما نوسان دریافتش مقابل تیم‌های قدرتمند می‌تواند دردسرساز شود. با توجه به حذفی بودن مسابقه، انتظار ست‌های نزدیک و طولانی منطقی است؛ احتمال کشیده‌شدن بازی به ست ۴ یا حتی ست ۵ هم بالاست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدار هیجان‌انگیز امشب رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140346" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140345">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
✅
✅
رونمایی از مدارک جدید پرسپولیس علیه آسانی در کمیته استیناف
✔️
✔️
باشگاه پرسپولیس پس از آنکه شکایت این باشگاه از استقلال به دلیل استفاده از یاسر آسانی در کمیته انضباطی با رأی منفی مواجه شد، نسب به رأی صادره از این کمیته به کمیته استیناف ارجاع داده است. …</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140345" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140344">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
پرسپولیس قراره ۳ ،۴ بازیکن جوانش رو با هزینه باشگاه به چند تیم پرتغالی بفرسته تا تجربه کسب کنن و دیده بشن؛ در صورت انتقال، سرخ‌ها هم از ترانسفرشون سهم می‌گیرن.
❌
فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140344" target="_blank">📅 09:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140343">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
✔️
پیمان حدادی: به‌دنبال این هستیم بازیکنان آکادمی پرسپولیس را به پرتغال بفرستیم!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140343" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140342">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iawr11Y9p4KxeZZ5aHbnGGJWhb_1UTCJlMqXdKR2AVlJg2GhXmzz8fsOfbgPtQtYHNaMGe-RrgC5K7y1kMi85hqcrUeJ_r1bJjtLvfuNOKoDXmEdU-C3LDFd7rE_ZkEAf5vp_hAQ7tRy0t0IfJO8XT62BFUEYt81nF5yPjgjb6ZhHFW8BTtwzgHR0NeRXHi1Cp7dZpLnm8XKzVWRRFzvbiKr5JCn5dYizrM5nZJ0Il23GxcLvzsiROPO75oEoCkxu7BwZwa7g67lNI4Mg4anw1i1VEYrGQAudeGC3oSN3h0bNSUkbVImPSUdXqvP-OV30CsxvmuXxscReGCXSnMEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140342" target="_blank">📅 09:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140341">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLQyKBRY7aV07LnERGXwFwwMri4uV7-muxRNvuwpnDofx8lRwkfYfMAmx0WoXIhoNPhNg3zp6UTx_hfGGhHm8do-tUsPnYnH7mZ0uxSngdGKAGF57NbYq73j4YaxO4afHm9aY0AKaVbcbEgxAV8VPnSKRFBBXFkYSYMjWvG4Ue79tP5kjj0HtWe5ta42IxqLJcAaJvOAErMpaSuJ0PcvM9GhVufQGebRrdOJ0lPO-aIdlKSVCSZ1nGyqrNdgPB_0wHmI-PRIGgIkvk30xTzriJfkrxxdUPmsmKL-8NuG-5G99rolUgkhpxuCq4OOLqhTRS_V0Pg5q9qamM3MVqs2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140341" target="_blank">📅 02:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140340">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
تاج: بسته شدن مرز عراق مشکل جدی نیست و با AFC مکاتبه کردیم/ عده‌ای با کارشکنی و انجام اقداماتی به دنبال عدم خروج تیم‌های ایرانی از کشور هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140340" target="_blank">📅 00:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140339">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140339" target="_blank">📅 00:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140338">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9814f0d7ba.mp4?token=rE8c8Kpo5QCrc_JyyZR3XplL3K8-3J0JOa_fGV8K3yZx-RNzpjEpjXBm1gi_VcSeTVM_peJXrLBA-DYut75OAOwuIjaQP4gp65trsHhfG5mkrdTDPG3wyHhRKJJYNvFeyjlH4hXd-_g2dAEeXCafRdcXA710ffeO39egTkbguwFQd70ULHCT1tFFEJPBAeJ8yiwsyb_9djCmRNyr4utr2Nk9tznWyOCnRnMptL7rWbT4TUkSJYQb3ppSowZjgp-iVmgSEnonqy6N34px4cw2Ghgnit86Qz9eEvB37ZBY52yyFJGyEgk_geBJGeeChv89x9rEx7V44k-1_CVps3yomA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9814f0d7ba.mp4?token=rE8c8Kpo5QCrc_JyyZR3XplL3K8-3J0JOa_fGV8K3yZx-RNzpjEpjXBm1gi_VcSeTVM_peJXrLBA-DYut75OAOwuIjaQP4gp65trsHhfG5mkrdTDPG3wyHhRKJJYNvFeyjlH4hXd-_g2dAEeXCafRdcXA710ffeO39egTkbguwFQd70ULHCT1tFFEJPBAeJ8yiwsyb_9djCmRNyr4utr2Nk9tznWyOCnRnMptL7rWbT4TUkSJYQb3ppSowZjgp-iVmgSEnonqy6N34px4cw2Ghgnit86Qz9eEvB37ZBY52yyFJGyEgk_geBJGeeChv89x9rEx7V44k-1_CVps3yomA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فووووووری و رسمی: وارد فیفادی شدیم و تا 3 هفته خبری از بازی‌های باشگاهی نیست...
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140338" target="_blank">📅 00:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔄
✔️
✔️
✔️
🔄
سعید دقیقی بعنوان سرمربی جدید نساجی انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140337" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140336">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFJ0tW8lMp04BpqHGBDBYM5y_cPf6ryjzcFD4ER4NYmK7dRdmHpTW8sYZ847oZzQJidgPZES69TTDsdkkuvkQhxZ4u0eUTSd-JrUiw5jVjg1Gxi8zNwpyeQe615UV9mzRHiDlvqMJ9FZnlTFVx0gaI0VCRLvndOzj0ahYpf25kMnrwS6MHg1YViFpElyqSTd3kXS13ayy1u0B_oooUCOsdwnbzHDTFUAcSCH-IO227-ItIFkN_8QayeMLrpAoDyczTHYF2YTAoMbBwx1iwjeF7MuaTq_6rQbxNS7Iy3kuNKRp8ZoGAjF1vL9kVcG20p4-gHD7fwhYhCiM2_vMkqgVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
💛
🔥
غوغا کردی امیر قلعه ؛ جوون‌گرایی نوین قلعه‌نویی: ( جمع سن نفرات تو عکس : ۱۰۹ سال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140336" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140335">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140335" target="_blank">📅 00:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140334">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔄
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140334" target="_blank">📅 00:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140333">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lzVN6bgrDURydJaum-oQAL3LCca41I3NhgCxjMDEpImWdXRdZ8bfQxozSiYpuj39EsSbpECxGkNddqfepwQpi4c4Lafj5qt0-FiXy8-UOOimEMRM7kPdyh8TH36a6rU-Q1CtHs3kGmEOGlwhoweH9RX0X86IVRfcJ5URi44qF6hn2MiKp-eCU65H6vy3bm-ABXCgJ4Tpboaa7sUZ-Q-b1KHqUuodFWYedsTIrr_d9DL9IzDmtk7-q7_6XE6PVh3I_-pRHDydttwJoMVzhENttFUbvA6irB24Bca9pVb8pakqz2i1BM98I4sMWZNww5wfq_HeukhGplvSZY8kzV7-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛎
پپه لوسادا مربی پیشین پرسپولیس به عنوان مربی بدنساز تیم ملی انتخاب شد.
🚨
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/140333" target="_blank">📅 23:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140332">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9Kun6uEIQzD0cg5-Iq_CqRO6z3c87HXdcNueeOxzOAX8BmJyY9_bfuhAB8JiBMJrMS8vpYGyaeXjYl0fzEy6xDm0ZauC-5lXWG2JgP2d62lNO2dCQK7F-iZduscQ6o93Hr-X2A_wNGseIwBp4-kGsG-D-n0ZRTcaa-90bteEkhYyfteOW-euBIYkzcJnzatzey38uBiT5mZeDgggjDfOKJdOR01Y5DC6wJpsE0a039CJrhIS3BHAbcHgDXxPAG8cB_Erv5M4_2B4qc3f15mtnw0GSoDPO3AZjR2qmLywXCfutHdR23SWmDjVUnxCk2qiDp-vcnyYLMpaZwgjR5S1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
مهرداد خانبان به کادرفنی قلعه‌نویی اضافه شد
❌
❌
پس از پایان همکاری آندرانیک تیموریان با تیم ملی فوتبال ایران، کادر فنی این تیم با یک تغییر همراه شد و مهرداد خانبان به جمع دستیاران امیر قلعه‌نویی اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140332" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140331">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3Yli1e6LYEEgF16kCEDW3Yzx_LbCabFxY8ZB4aVEN7F5cR8Mxjq00fQnd8JGZO7soLQ7L2euEFDRUcyEWhViJCuYk426z-b1QkNeuEYLIVSqgzL56UDpPEGxIJUhmk1B9vD3-jUpbK77LRJRz1lXb2PydWmddUOnni6BmzU0_EAKFcFXR5TBxsBJTO1FW1wG0AGJ019MzqmuXB1X8Ok8b9_C8VFpop2MFwCwXVz3MYlhT_kJ7tEJzFW6-nGoKuKwRmbgRm2CypAw4CFVmy46xYGZt_SpfWEmYVvxHhV5DgvlzS5fVwhY0BXbEdcnsheVWPJE_kzkA0BEYYu_1wS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
خبرنگاران عربستانی: کریستیانو رونالدو نیم فصل در انتقال آزاد راهی فنرباغچه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/140331" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140330">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oA7pvuBz22oeuTwtWFuFYj9N3fZJ_j24w0GqiN3-iOkBEuVQ05Sn4kXRJ6jahZ7oD0hKyLnCj8hLECxR7GMmUX6hrSW2ajJKBZ3N4sy0SqeNM1xFzb2Bu4SGLb0xfddIgfRJJG-heQ3xJMFjdRn7dNBtT_MnxjUOyRewEu5OcVZ_DQPwkB01-cgA7UGdcmMY8-dCm2MJSy9y8ni3Is7Qz6krsrIyCL1ymP306I8b4DEEr44BNsAyv9NkfLhSQ4_bTPTE4y-muc9Co7e3RG1NpgPukE0bYn5Yl_iOHV5PBQufljynPVwDthtpw1HT1txLP-Yyw3v6_riRpyUQ8oKlCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/140330" target="_blank">📅 21:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140329">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔄
⌛
بشار و فرهان گزینه‌های روی میز تارتار در زمستان؛ پرسپولیس به‌دنبال پلی‌میکر
😀
درصورت تایید مهدی تارتار مذاکرات با بشار رسن آغاز خواهد شد و فرهان جعفری نیز گزینه‌ی دیگر سرخ‌هاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/140329" target="_blank">📅 21:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140328">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
رسانه‌ های عراقی: باشگاه پاختاکور ازبکستان با ارائه پیشنهادی جدید به بشار رسن قصد داره قرارداد این‌بازیکن 29 ساله روتمدیدکنه اما فعلا پاسخ مثبتی به‌این افر نداده. اولویت‌بشار بازگشت به پرسپولیسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/140328" target="_blank">📅 21:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140326">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYv2IEvoTtQOAFLIDhiQfCO-qkksofCxV6DNh0RtjwN_CI1OfF9c6Sf97H-9A8A9b9_u9BPdg-99SXEZikROu0dhxnoeE5EAt_92P5ZlrSfwA4Bcj54xYN9e3JO6qziGdf8SFdytsmfjYAnbuUQ6KLu8L33ngKwkZQCOPcWKnYd0a-aTisAAALLcsFHj9QbBw5xfQcK47m21zLSqsUq67cnFuwoSCce-UdsydceHAKK0LFz0_Sb6VFvvr930rJVD8pSlzN7jk6PCSfN4rxE7WUXcpEwNS779Sv_JVnlmhrM352b9tfu0Ocvx72oa3fvRQaSbTZMBdS_L0pFtjD50RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Marseille -
🔵
PSG
⏰
Tonight 22:15
🏟
CEPAC Vélodrome
🔵
مارسی با شروع ضعیف فصل، در ۴ بازی فقط ۳ امتیاز گرفته و ۳ شکست داشته؛ پاریس هم با ۵ امتیاز هنوز در حد انتظار ظاهر نشده است. در ۵ تقابل اخیر، پاریس ۳ برد، مارسی ۱ برد و یک بازی هم مساوی شده؛ آخرین تقابل هم با برد سنگین ۵-۰ پاریس تمام شد. از نظر تولید موقعیت، پاریس میانگین ۱۸.۷۵ شوت و ۶.۵ شوت در چارچوب در هر بازی داشته؛ مارسی به‌ترتیب ۱۳.۵ و ۵ ثبت کرده است. با این حال، ولودروم و حساسیت «لو کلاسیک» می‌تواند بازی را نزدیک‌تر کند؛ انتظار یک بازی پرفشار با موقعیت‌های جدی دو طرف می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140326" target="_blank">📅 21:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140325">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwdPxkZ0Es9FRkNrDi-0lQJ4Ykc-jbTtvf5hpF2763SOSa9GaJv3mixyB43byYFtcH4bRRzri3pMZkHwUAnW_9oP7TNLfvxae2TU_iGVoes6Ugu1_9khMMzL3jkhuEIjoGS7wMeFZYOs5moacgmC1hMPanIKScQw3gXp8kY1zysGODYnM3P9u3q4YPwMjUETzf3hBTkA4Urw0j_WLoKIhP4h1I8nym0QIaJZTM_cbdIQJNL_aWqVilc3O0-ponIXbfBVxKIykmXmuPnaTu_qOgT3FJbUt0uuHxKB0jWKraRCGKOjeZFX2drCkVcmezMh7Wj-iewKGtc4XceFdl5P0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140325" target="_blank">📅 21:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
✔️
✅
تصمیم پرسپولیس درباره اورونوف
✔️
✔️
پرسپولیس فعلاً هیچ برنامه‌ای برای جدایی اورونوف نداره و این بازیکن همچنان در برنامه‌های باشگاه و کادرفنی قرار داره.
✔️
✔️
شایعه انتقالش به تراکتور به‌خاطر نیمکت‌نشینی تأیید نشده و حتی اگر در آینده بحث فروشش مطرح بشه،…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140324" target="_blank">📅 20:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140323">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140323" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140322" target="_blank">📅 19:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRFr0Xb2NZRw-RWOHJHVw0iGxbiksTO13orbKoMEO-4f8WxYTM-caxxJtxd-NutkFyrJuUYjc5_eMDWCskNPKOE0zjuv721ahXdPFHZgF-jIdiCxfdqPhfNJ0xbej8vuzDou1Hvcvac91xWzRSGKQ0QN6Vfgw_FgVpA9NyVbSXYsatklBmfRgGRX1bVdg2t_7wcVq8ffySo3LSx7Ra6nMyfjKkjo9Usiot4Nkze2gd-eeDWyRLfrrF-jxMGr11e9tEpqC4_a_8CANBIVfJ2k8CKt6Ye0EvHLST-yaOqS7qNFtLsVGiNlqLI9YZGV1g0mOTjb2Uzi_z06DAZ2Isfiyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
گزارش تصویری از تمرین امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140321" target="_blank">📅 19:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A50mDBkWlVzbagqB7Mivgvdd1V95fbf54nRs7jTUY3I-iGnPov5ZPxPTFdpfJZDWQmf5koY5grUUiyOmGt_PMkkM6ANZpkWtbq3-6cYOEMLGK3tZc31ai8pyEvFe_iiLIFgWqpQ2AKEBwzmxEemqgoPsFf2mfRfpG19HVZqIysUMNfIOxTir6JoKllqVZe70FKanFqHBgQSyiWoXkirGwVGYDFuJTNao25Zfk2gsb-DdGUURQNewAqSiBZFPlieTDd9_rEKPmdDXl1OHiaitUJ7h0CXBMlUYZeZ88mTFW40BZEo1TDzekOdCJVLBMQEFSPfYhpgH5xTC2QGcUYsVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140320" target="_blank">📅 18:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✖️
✖️
✖️
🇺🇸
ترامپ به فاکس‌نیوز:
❌
من می‌خوام با مقامات ایرانی
🇮🇷
مذاکره کنم، ولی چالشی که الان باهاش روبه‌رو هستم اینه که اونا مثل موش تو سوراخ‌هاشون قایم شدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140319" target="_blank">📅 18:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140318" target="_blank">📅 18:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
فووووووری ...شنیده ها
🔴
قرارداد استون اورونوف با پرسپولیس با دستمزدی ۲.۲ میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140317" target="_blank">📅 18:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
رسانه های مملکت گفتن آمریکا مجوز لازم رو از چند کشور منطقه برای شروع دوباره جنگ علیه ایران رو دریافت کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/140316" target="_blank">📅 17:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140315">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140315" target="_blank">📅 15:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140314">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/140314" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140313">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
❌
⭕️
⭕️
فوری/کانال 13 اسرائیل گفته آمریکا و اسرائیل تو تدارک حمله سنگین به ایرانن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/140313" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140312">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=GQlsgq_-j_n1MpieVVmUTseQSsgC6xbuh1OhsHMCtqScUtuWnVrVlCSR8oAeFKSlGCrYYHWUxstbEWYA5NXp6_sZA5RpCVRzzlA0y64TLy5CUQJ3Qi5mfjuD9zYBZNQ7j5NpELLBkkrxxvqGbSfPlNkH3pZ1Ao0_Mi1GdfUGiBJZ4ZpQri7x8klhXul0ZS30vz_LVkJDEHQRlrGdixghcnXtktvuOPLgX-vRdofYj63HATM24yn7uFp-BIDYHgZN5TZHcF8ZY1LF7XJAYGnNu3xN9JI8RzWBsZ1DNJJRjFeN8ohEcsKiYNRMGRXv-QwnD4kp6KOziFZhIRBOAoCdFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=GQlsgq_-j_n1MpieVVmUTseQSsgC6xbuh1OhsHMCtqScUtuWnVrVlCSR8oAeFKSlGCrYYHWUxstbEWYA5NXp6_sZA5RpCVRzzlA0y64TLy5CUQJ3Qi5mfjuD9zYBZNQ7j5NpELLBkkrxxvqGbSfPlNkH3pZ1Ao0_Mi1GdfUGiBJZ4ZpQri7x8klhXul0ZS30vz_LVkJDEHQRlrGdixghcnXtktvuOPLgX-vRdofYj63HATM24yn7uFp-BIDYHgZN5TZHcF8ZY1LF7XJAYGnNu3xN9JI8RzWBsZ1DNJJRjFeN8ohEcsKiYNRMGRXv-QwnD4kp6KOziFZhIRBOAoCdFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
| فوری از برنا:
⚪️
❌
ظاهراً عباس کهریزی از ناحیه رباط صلیبی مصدوم شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140312" target="_blank">📅 15:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140311">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140311" target="_blank">📅 14:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140310">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVuXFcexyNp6gkIrdBY7AaX0rCMcK2JRsntmWzBOo_RIX7_t-Ef2v1Y0UV_vskPbdxlRYvH-N5cJfSwoqo7kSYc87GdCQU1WIo_1zDAgR9_oiOau1n3Hkl7qRhEGxo5EkISU0NBxtbnKOsTsJJtcN9Z1lIENJjNHUgAG39oyQhApZPm1xvxR-8sLw7KMzhTU4_fS6osL4YLumF2OYh8iRk4BTb9a_PCUh9XCQ3BBP08-J4lIQxuv7JT2-IAHmZmkNSqfUfNmY2-hQ3ZCvy-iEN2-ns3DZQ4YDNZ-tjd83J7qVIZtFC83AmtLnDX58JHHLf_m_Ac8-C36iXh6N-8q7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مادرید در انتظار یک شب داغ؛ اتلتیکو یا رئال، کدام‌یک حرف آخر را می‌زند؟
[
اتلتیکومادرید
🔴
🆚
⚪️
رئال‌مادرید
]
⚽️
اتلتیکو با بازی فیزیکی و فشار در میانه میدان می‌تونه ریتم رئال رو مختل کنه. رئال اما در انتقال سریع و خلق موقعیت از کناره‌ها، تهدید جدی‌تری برای خط دفاعیه. دربی مادرید معمولاً پرتنشه و استفاده از کوچک‌ترین موقعیت‌ها می‌تونه سرنوشت بازی رو تغییر بده.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140310" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140309">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
اوستون اورونوف و ایگور سرگیف از پرسپولیس به اردوی تیم ملی فوتبال ازبکستان دعوت شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140309" target="_blank">📅 14:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140308">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
#تکمیلی؛ فرهاد مجیدی سرمربی سابق استقلال ضمن تشکر از حدادیان‌مالک‌نساجی آفر این باشگاه رو کرده و اعلام کرده در ایران تنها حاضر است سرمربی استقلال و تیم ملی ایران شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140308" target="_blank">📅 14:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140307">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">😰
مدیران نساجی دارن با فرهاد مجیدی مذاکره میکنن تا این سرمربی جانشین مجتبی حسینی بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140307" target="_blank">📅 14:06 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
