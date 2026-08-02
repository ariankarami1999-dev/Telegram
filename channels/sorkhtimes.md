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
<img src="https://cdn4.telesco.pe/file/XNtvGQNRq6bS4W15dE53VcKLPbvsc43h6hOWtQym9qQDC-792LwZ3R7Cg40OOyTl516bm6u_SYOFz-fSmlgra1g0K1NgDix3sqXuCiCQ2ru7VyBE2wmVt6l05XJwkgF7KTxUi5uXv_YkeXlND_bZ8DJ84aWVGcytZNcA-tt4RPkOIXCFiUSOyDQvsnFuE7jTkO4XKfOoLf63npGB-vo7hB7w6sxHdjFVIF18iibNpk2Q-qe2Th84yEARqtyim17QcfwHC5yZJc-VHPdpw6rhA4Q6N30m5LUh0XFM5I0oMWvQ-Hm8hUStcVMEu_EdkJ7z00F5twdF4Cz_dNvTkcXZEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 19:05:01</div>
<hr>

<div class="tg-post" id="msg-137214">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f27def464.mp4?token=WGnHMarMRTAldweD2ycpvoNgW0oaUYqbOhJ5X0vT7W2ANlEdKkQGCWFCdVpCjTa9c0uAVKADQf2wjQho1c2g_13rW8rwxY3FMw9TbkJlO55yZ5CPunmdOPo3oNHuUPlpGMo5DKFCkoT-LU3ryZ0uagLK-viCCAWPo1jrScq_efeXn5FJyYXZuVRkG3GWycDCHQZUt0MgRVvFVDMdn6TQy2pU5izLag9IPzRh7zdFs6S4__Visia6OskbHjuOnUMbS4qz09rMIEPCYZV7bTg0Y7Qh4aCdq6-Fwl-_IpV62Y3ceKWI0cL6YUq0nKF7aJbCOyAjZKYA_7EuDrGslMhUeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f27def464.mp4?token=WGnHMarMRTAldweD2ycpvoNgW0oaUYqbOhJ5X0vT7W2ANlEdKkQGCWFCdVpCjTa9c0uAVKADQf2wjQho1c2g_13rW8rwxY3FMw9TbkJlO55yZ5CPunmdOPo3oNHuUPlpGMo5DKFCkoT-LU3ryZ0uagLK-viCCAWPo1jrScq_efeXn5FJyYXZuVRkG3GWycDCHQZUt0MgRVvFVDMdn6TQy2pU5izLag9IPzRh7zdFs6S4__Visia6OskbHjuOnUMbS4qz09rMIEPCYZV7bTg0Y7Qh4aCdq6-Fwl-_IpV62Y3ceKWI0cL6YUq0nKF7aJbCOyAjZKYA_7EuDrGslMhUeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خاطره جالب پیام نیازمند از شکست دادن اورونوف در بازی FC 26
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/137214" target="_blank">📅 18:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137213">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
با وجود اینکه همایی فرد از شمس‌آذر و گل‌گهر پیشنهاد داشت، اما بعد از درخشش در تمرینات اردوی ترکیه، تارتار با جدایی او مخالفت کرد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/137213" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
فرهیختگان: همایی فر عملکرد خیلی خوبی جلو آلانیا داشته ولی تارتار همچنان خواهان رزاق پور هستش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/137212" target="_blank">📅 18:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🔴
با جدایی رسمی مرتضی پورعلی گنجی حالا قطعا یک مدافع میانی باید جذب بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/137211" target="_blank">📅 18:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
فرهیختگان: اولویت های تارتار در پست‌های مختلف
✔️
گلر: گوهری
✔️
دفاع راست: محرمی
✔️
دفاع وسط: افسرده
✔️
دفاع چپ: رزاق‌پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/137210" target="_blank">📅 18:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137209">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
🔴
شکاری با استقلال مذاکره کرده و با باز شدن پنجره احتمال جذبش بالاست و اگه الان باز نشه زمستون یاغی میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/137209" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137208">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🔴
با جدایی رسمی مرتضی پورعلی گنجی حالا قطعا یک مدافع میانی باید جذب بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SorkhTimes/137208" target="_blank">📅 17:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137207">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5XI-dhZISQSHm4aDTVoCcq5PWHCwvDgyTX63EtJSt43cK2ZLU9jdRYHhVxu-H9WUbNxS2XVy2NhhFsC3hdKgee13w-89SEjwEd1gkaAqxBXmZZVjHH6Tl6i9lFVWCMah_BELGER_YSbCxeuUZ19c4d7F5Z-uIi0bGFA-7pnsQxw7kGyQsDgg9mkA_9oRZPdbXfiwKJUKUfyUsXEk5eX-n1RvMVZ9hNrWEmTOvBMwgGC7Q7vEZNKrXRkyqyeE4EgtK9Ze8cCuEBgroJrolKgtAwTw5m_Ny0OZiY8euWw_spdosOECQ2cOrCwf0FKSmzI3XTmah1bcVGShq-Bn9nImg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎾
فینالِ نسل‌ها؛ فریتز در اندیشه جام، جودار در سودای تاریخ‌سازی،
فریتز و جودار برای فتح جام مقابل هم می‌جنگند!
🎾
رقابت رافائل جودار
🇪🇸
-
🎾
تیلور فریتز رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
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
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/137207" target="_blank">📅 17:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🇮🇷
اعضای هیات رییسه فدراسیون فوتبال ترجیح می‌دهند در صورت برکناری امیر قلعه‌نویی، یک سرمربی داخلی دیگر جانشین او شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/137206" target="_blank">📅 17:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پخش زده بازی پرسپولیس  ارزروم اسپور ترکیه/پخش زنده به صورت لایو استریم هستش کلیک کنید همینجا راحت بالا میاره</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/137205" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYZo1t6u_GBd1WEu8wVMYZh1b7lNkrc6kGHejV8EVlV331ZGeRDWZLJToOO2IvJDteWpY7Sb77kVGt74y-pzbg2rCxoTDaYSNP2g3ZujNkTJOmLA4o0lCGcqrfnqNvU6YgZmsQdBXoKU85_MpsketUMn5haaDjBY1iZDLaZP0G45x-Fg1o6xzvvM6JH_LxfJRo8Njecax7y8w72xTFqj1Qj4dCZj2NdvEgBYMKznxi3RQw9gxu5CzlFM48QrZOvUVyBlLRPnWER0BE_SEpOnG1OBL8W3MOG3Ko5XcnwgUib56YeN5GyuwqFxZ_HJ4k2Eoz9aqIrTP33pTbKfF7Wc5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
💚
مهاجرانی، سخنگوی دولت: با خود آقای فردوسی‌پور در تماس هستیم و ایشان جزو افرادی هستند که به عنوان سرمایه‌های این کشور محسوب می‌شوند؛ ایشان و برنامه‌ای که خودشان ساختند تحت حمایت کامل دولت است و رییس جمهور دستور دادند هیچ سایت و برنامه‌ای بدون اجازه ایشان دیگر بسته نشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/137204" target="_blank">📅 16:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز بازیکنان باشگاه پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/137203" target="_blank">📅 16:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137201">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚡️
⚡️
شنیده ها: با درخواست مهدی تارتار؛ باشگاه پرسپولیس فردا برای جذب مهدی گودرزی اقدام خواهد کرد
🔹
پ.ن: گویا خیبر هم مشکلی با جدایی گودرزی نداره و به دنبال درامدزایی ازشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/137201" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137200">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtRimlOD1csA5dj8iAiqUFzSAwT_3iPc6Zvy0UT9o6g9E8cBf3XMsCijJUVY0bX-D3Aeo7DCMWxyMnXGdNkOOfZ3ZqTACSsH1f5WFiM-4b558CrVOMA4ZffBr486sAMDYUFXsWDxxRhdzbHTrUXWbNqrJSX_sCg2q67o-6KT6R19sbkiSLXEP0sgZl-08DFncWsHUPpZHvKIpx86W2KfQZ6y1HWqkwBF_DWCdUxMT5ZcE7KFi0vEzlF7fNdQivhg5P_jrqBKAeeL67-QiewTR_3QedpwQ35NfpTrwwAy5xrgpuwHLhqlY4bzGdvGqXwOGT5WwUh3bkEAw-CBYmD35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز بازیکنان باشگاه پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/137200" target="_blank">📅 15:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137199">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
قسمت اول چالش پرسش و پاسخ سرخ‌ها در اردو
⚡️
بازیکنان پرسپولیس در فضایی متفاوت، اطلاعات و سرعت عمل خود را به چالش کشیدند.
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/137199" target="_blank">📅 15:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137198">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
❌
تارتار در اردوی ترکیه به محمودی: با ادامه‌ی این روند به جام ملت‌ها میری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/137198" target="_blank">📅 15:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137197">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
در حال حاضر سه ورزشگاه در تهران و شهرستان‌های اطراف وجود دارند که امکان میزبانی از مسابقات لیگ برتر را دارند. ورزشگاه‌های شهدای شهر قدس، اسلامشهر و ورزشگاه پاس از جمله ورزشگاه‌هایی هستند که می‌توانند برای برگزاری مسابقات مورد استفاده قرار گیرند.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/137197" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137196">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
❌
تارتار در اردوی ترکیه به محمودی: با ادامه‌ی این روند به جام ملت‌ها میری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/137196" target="_blank">📅 15:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137195">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✖️
✖️
✖️
تارتار:
⬇
⬇
تمرینات بسیار خوبی رو سپری کردیم بچها با انگیزه هستن و صد خودشون رو گذاشتن
⚪️
از طرف همین جمع قول می‌دم تمام شبانه‌روز خودمون رو بزاریم تا هر سه جام ممکن رو کسب کنیم
⚪️
همون‌طور که گفتین ایشالا دو سه بازیکن دیگه بهمون اضافه میشه
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/137195" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137194">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msZxB_xDh-V2Ood08C_RXJDq7zAp_7CMvkYeqA4yTkG9CQyifLiI0N_HhUCqCmzIaK_LOxRhveXnWx4DStxxUTHIu9T3lbNPZnJP34BnT6seM5kSnaNIOz9dCTQrdEq5UMU7t-KxK6qvQoOKqsW8rpDN2qFobQjOIOfauew-LOxTbN1AHaXg7E7_xyWx3vTwZB4HxZT8_im1JOxUzQHqqc_Zg89ERsHhB7IuVuXW8dhTiYZo824RbqOGdE6MHQ714Bv-f6U4Gw7DUSnGUaF-38a-5ibjhjof3sodH_LvbcPdZr-Y6hm2sjUH4sSzaZ0tGMuKsjSoawPuAZEcijAvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جدایی به‌خاطر یک پیراهن پرسپولیس! امضاها با شست‌وشو پاک شدند!
🔴
پدر یک خانواده در شهرستان سبزوار پس از آنکه همسرش پیراهن پرسپولیس او را شست، تصمیم به جدایی گرفت. دلیل این تصمیم عجیب، پاک شدن امضای چند بازیکن پرسپولیس روی این پیراهن بود؛ امضاهایی که برای او ارزش احساسی زیادی داشتند و با شست‌وشو از بین رفتند.
😔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/137194" target="_blank">📅 13:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137193">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
❌
سه ورزشگاه تهران آماده میزبانی هستند؛
⚡️
ستوده‌نژاد: ورزشگاه تختی خرداد سال آینده آماده می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/137193" target="_blank">📅 12:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137192">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
گفته میشه ورزشگاه آریوی اسلامشهر هم به گزینه میزبانی تیم‌ های تهرانی اضافه شده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/137192" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137191">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: دانیال ایری درخواست جدایی از نساجی رو داده و باشگاه نساجی هم قصد فروش این بازیکن رو داره و اگه اتفاق خاصی رخ نده ایری پس از کش و قوس های فراوان پرسپولیسی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/137191" target="_blank">📅 12:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137190">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
پرسپولیس دو دیدار دوستانه دیگر را تا 24 مرداد خواهد داشت. در اردوی ترکیه برابر ارزروم اسپور و در ایران مقابل فجرسپاسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/137190" target="_blank">📅 12:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137189">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
الوحده برای فروش قربانی ۲ میلیون دلار میخواست و با رقمی که باشگاه قرار بود به عنوان دستمزد بده خیلی زیاد میشد و حدادی از جذبش منصرف شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/137189" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137188">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AH_obOGarBqp0UjXXRZ-J8SAOOduA00rofADKjLcRsWKjiDlwT216cMnLbq19glv5bFSRvS9rrGUHW62O5Ea4xK-90t-1qUvchhdFg4zz8aiU76TurnpLpC6Ic_bkakx8Ll0j6aB9P5WqsETvxClr4wtp-wTTaO7UD23WnvBAOtuadhrSHEX3SujIIWfEXkmAQ9tyDxg2PMSPicY775W5jcSoJbRQTIbIFfApENiC9eu8NKyvVCHwVweEqKdBh7g_4-nJnu2ELCQuSXAaSK51up0L8o-dMaycord_VJnQAkrF91WShtXJfhhnAStvkCcjXSCev4n72x-s4FJUwR5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس دو دیدار دوستانه دیگر را تا 24 مرداد خواهد داشت. در اردوی ترکیه برابر ارزروم اسپور و در ایران مقابل فجرسپاسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/137188" target="_blank">📅 10:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137187">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
⚽️
ویدیو باشگاه از تمرین تیم با کپشن:
😀
از ضربه‌های تمام‌کننده تا واکنش‌های تماشایی؛روزهای پرانرژی پرسپولیس در ارزروم
❌
پ.ن حال پرسپولیس خیلی خوبه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/137187" target="_blank">📅 09:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137186">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
محمد حسین صادقی امروز با مدیران باشگاه تماس گرفت و اعلام کرد مادرش دچار بیماری صعب اعلاج شده و اکنون در بیمارستانی در شیراز حضور دارد و به این دلیل در تمرینات شرکت نکرده است
🔴
🔴
مدیران باشگاه پس از این موضوع پرونده او را که به کمیته انضباطی ارجاع شده بود…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/137186" target="_blank">📅 08:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137185">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">💢
💢
رزاق آخرین خرید پرسپولیس در نقل و انتقالات
🔴
طبق شنیده ها ابوالفضل رزاق پور احتمالا آخرین خرید سرخپوشان پیش از شروع رقابت های لیگ برتر خواهد بود
🔴
رزاق پور امروز جلسه ای با مدیران باشگاه فولاد داشته و به صراحت اعلام کرده با‌توجه به شرایط حضورش در پرسپولیس…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/137185" target="_blank">📅 08:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137184">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
ایالات متحده آماده و کاملاً مجهز است تا با قدرت نظامی، ترور و توانمندی‌ای که از زمان جنگ جهانی دوم بی‌سابقه است، جمهوری اسلامی ایران را سرکوب کند.
❌
با این حال، ایران و سایر کشورهای خاورمیانه از ما خواستند پس از توافق بر سر طرح کلی یک معامله، هرگونه حمله‌ای…</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137184" target="_blank">📅 08:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137183">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
فوری/ ترامپ: به درخواست ایران و کشورهای منطقه، حمله رو برای فراهم شدن زمینه توافق، متوقف کردم. ما کاملا آماده حمله بودیم اما حالا مذاکره می‌کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/137183" target="_blank">📅 08:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137182">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
ترامپ:
✅
در حال نابودی کامل ارزش پول ایران هستم. در شروع دوران ریاست جمهوری من دلار ۹۰ هزار تومن بوده؛ الان شده ۱۹۰ هزار تومن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/137182" target="_blank">📅 08:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137181">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUrLOqeYtoVNu4kFmBqII4C5jwS5-FQlFFpsgWdYuUBQ3-pJiqHiLrGGGIokCWFaX3sfPNx_8hEuEnhBMogr3ztQ_rkKkTYlmHWI_ZCgyM-rPAOC8c64Tu0Zcdr9vvwpEzuvXlgnTzfj0SdBlX9c1ncrSm9AcczyJ_s4ASvByC1Io26KARQ5Fqi4qKhpCAPYAoVkwVftNn6po66FI5LalP5Uz378eoc9WDay2Gx0sTmDtt6VetvmX5TLJtCGPEQGLbqznRvKGd635AkT_eLLugWQT6SaOF8Pixr7Bg5V_RVVtqxsptxnbtvY1Lk4Of7wvtdJwz9B-lG9fEcWr5ve0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137181" target="_blank">📅 08:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137180">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQCCtnqI5r7rojzO8vuHzlLT5gQ7Ja_FC5pJv7sVCiLRMt7Qy8OV3oLETti0t-mQovuMdyEGn2eKwCCA2xLhZmiHt3xD2iYAgMjEqliN2qZc8KmoAf2ncbe2rBKMcU-AfHII96sDIG3QavjMQJFR2Wxj7NKpG5qNyuo0Swceh_wfmAUCqy1PUJfykIP43m4DTVJ5hUuWK3UvbtLnbaItCTzhOoaKjr4byM9yyP7AW0Z8B6HiligSXizcXWpJ5luOAKoFjLggEDgpGALrSaNCfTyqgkzrMHEndv_ES-znT_rlDDRsgudDF3CL39l3NBKrv4F0euuh1UVpY3BJQAhJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فینال غول‌ها؛ جدال لهستان و آمریکا برای تاج قهرمانی لیگ ملت‌ها!
🔴
فینال لیگ ملت‌های والیبال ۲۰۲۶ بین لهستان و آمریکا، تقابل دو تیمی است که با نمایش‌های کم‌اشتباه و سرویس‌های قدرتمند به دیدار پایانی رسیده‌اند. لهستان با برتری قاطع مقابل آمریکا در مرحله مقدماتی از نظر روحی دست بالا را دارد، اما آمریکا پس از حذف ژاپن نشان داده در بازی‌های بزرگ توانایی تغییر روند مسابقه را دارد. انتظار می‌رود کیفیت دریافت اول و عملکرد مهاجمان در توپ‌های حساس، تعیین‌کننده قهرمان این نبرد جذاب باشد.
🏐
اوج هیجان همراه با وینکوبت، یکشنبه ساعت ۱۵:۰۰ دوتیم لهستان
🇵🇱
-
🇺🇸
آمریکا به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی دیدار فینال لیگ‌ملت‌های والیبال با بیشترین آپشن، همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137180" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
✔️
مدیران باشگاه پرسپولیس موفق شدن‌ با اقدام جدید‌ خود به توافق با باشگاه فولاد‌ برای جذب ابوالفضل رزاق پور نزدیک شوند/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137179" target="_blank">📅 00:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ٫ اینترنت سراسری قطع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137178" target="_blank">📅 00:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137177">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: دانیال ایری درخواست جدایی از نساجی رو داده و باشگاه نساجی هم قصد فروش این بازیکن رو داره و اگه اتفاق خاصی رخ نده ایری پس از کش و قوس های فراوان پرسپولیسی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137177" target="_blank">📅 00:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137176">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
🔹
فوری از ورزش سه: خرید پایانی پرسپولیس مشخص شد؛ ابوالفضل رزاق پور و دانیال ایری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137176" target="_blank">📅 00:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137175">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
🔹
فوری از ورزش سه: خرید پایانی پرسپولیس مشخص شد؛ ابوالفضل رزاق پور و دانیال ایری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137175" target="_blank">📅 00:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137174">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137174" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137173">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137173" target="_blank">📅 00:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137172">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: نهایتا یک الی دو خرید دیگر داریم بیشتر نداریم که طی روز های آتی به ما اضافه خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137172" target="_blank">📅 23:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137171">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
❌
شاید مرتضی یک فصل دیگر ماندگار شود....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137171" target="_blank">📅 23:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_s_Ro-olZNk8dfswpL5e_B6cS7SMsecpR4Q01KW0EgCbsWZS_Lju-hsoHbLrIj8ZsjXYvjYBeimFM9eE2Hzpz32I4NJHqkqxM9hkgfkUDB3HbKof4hj2Lc62L7SdfWC2lyKVuIXT2fVqtANRAmj6dILvdYzYypsXtm0pOAFHewOvU5tBjqVsO2g_V7S76p7GnGw8OaSXqaWsyMjThx_0sDR-VddLhi5J0Z3Vy7BWTuDR3o8IwzsQHHsFTPcsGJjIj22DqsSeHdbOuN8KDFssigzjP6vZyLBy0nDOc9kDSOUhwy0wK23R_Uw9TaU7_GMVIlu7uiI3EaZLCE-kThMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
علیرضا اشرف به عنوان مدیر رسانه‌ای جدید تیم فوتبال پرسپولیس منصوب شد و بار دیگر به جمع سرخپوشان برگشت
💛
✍️
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137170" target="_blank">📅 23:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔄
🔄
🔄
حسین‌نژاد نمیاد پرسپولیس/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137169" target="_blank">📅 22:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137168">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
⚠️
باشگاه فردا میخواد برای رزاق پور نامه بزنه و پیشنهاد معاوضه بیفوما و 80 میلیارد پول در ازای جذب این بازیکن رو بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137168" target="_blank">📅 22:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚡️
⚡️
علی بازگشا: پورعلی‌گنجی فعلاً بازیکن پرسپولیس است، اما درباره آینده‌اش هنوز تصمیم نهایی گرفته نشده؛ باشگاه هم سیاست جوان‌گرایی را دنبال می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137167" target="_blank">📅 22:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137166">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
علی بازگشا: پیگیر شرایط دانیال ایری هستیم
⁉️
در مورد شرایط دانیال ایری از فیفا استعلام گرفتیم. دومین نامه خودمان را به فیفا زدیم تا استعلام بگیریم. فعلا نمی‌خواهم جواب استعلام اول را بگویم تا جواب استعلام دوم هم به دست ما برسد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137166" target="_blank">📅 22:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137165">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
🔴
🔴
🔴
دانیال ایری مدافع تیم فوتبال نساجی در آستانه عقد قرارداد با باشگاه پرسپولیس قرار گرفته است…
⏳
😀
البته ذکر شده که این قرارداد به صورت قرضی است و سپس اعلام شده باشگاه پرسپولیس میتواند با پرداخت مبلغی این قرارداد را دائمی کند…
🗣
🗣
شرطی در قرارداد نوشته شده…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137165" target="_blank">📅 22:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: نهایتا یک الی دو خرید دیگر داریم بیشتر نداریم که طی روز های آتی به ما اضافه خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137164" target="_blank">📅 22:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: نهایتا یک الی دو خرید دیگر داریم بیشتر نداریم که طی روز های آتی به ما اضافه خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/137163" target="_blank">📅 22:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
✔️
شرایط ایری از نظر حقوقی متفاوت با کسری طاهری است.
✔️
اینکه پرسپولیس همچنان دنبال کسری هم هست یا خیر و اینکه نساجی حاضر به انتقال فقط ایری می شود یا خیر نمی دانیم
✔️
تارتار بشدت دنبال جذب مدافع میانی و چپ است و ظاهرا گزینه ای جز ایری و رزاق پور ندارد.…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137162" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
محمد ربیعی هم  در تراکتور ابقا شد.و خبری از اوسمار نیست
🔴
قرارداد ربیعی بند تمدید داشته که در پی توافق با باشگاه تراکتور فعال شد.
🔴
تراکتور نیم نگاهی به اوسمار و طغرل ساغلام داشت و شرایط و وضعیت انها را بررسی کرده بود اما پیشنهاد ارائه شده جدی نبود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137161" target="_blank">📅 22:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
ترامپ: هر کشوری جای ایران بود تا الان تسلیم شده بود اما اونا نشدن، من اونا رو تحسین می‌کنم. شجاع و سرسخت هستن ولی خب تهش تسلیم میشن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137160" target="_blank">📅 22:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">📎
📎
تصویری از جلسه امروز پیمان حدادی و مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/137159" target="_blank">📅 22:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
❌
❌
فوری از ورزش سه: دانیال ایری این هفته با توافق جدید دو باشگاه نساجی و پرسپولیس سرخ پوش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137158" target="_blank">📅 21:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
#فوری | سی‌بی‌اس نیوز و به نقل از مقام‌های ارشد آمریکایی:
🔻
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است؛ اقدامی که شامل برق تمامی غیرنظامیان نیز خواهد شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137157" target="_blank">📅 21:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzLo8gHRXmT6FR-U2R6vzqBEoo1nqKlE3qIhQpHo9aivSjkD1-x9t6qvXZ3uGCEawr6lBkGcltnAfk4g8Peoe-gw9DfAmernE85uLwbWQQOcYl3HVa2z5VGAsNgEgI5VUk10R_3w7WGdTbMNd81WRHmlZABXyuS-1V3iCnKZ9gvRMH83HRfIl0gf6GrtI4NzxQZTZwyBoTign_1bEoc9M7EhpGI9yS5mWsk-yxDsa4ZBfF99Y36o391Ra1xbQzrwBaCRk5Oyymb0Mz0mCZrMEbgt9ckgzH9eR4ODgA0YPKjE84pSxnJ1QrMlC3Bg7ObWEuBII8kWrA3EFp-P5EdoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
گفته میشه ورزشگاه آریوی اسلامشهر هم به گزینه میزبانی تیم‌ های تهرانی اضافه شده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137156" target="_blank">📅 21:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137155">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚠️
⚠️
فوووووووووووووووووری
⚠️
⚠️
صحبت های جدیدی درباره باز شدن پرونده انتقال احتمالی دانیال ایری به پرسپولیس مطرح شده و گفته می‌شود این بازیکن ممکن است در این هفته با توافق مجدد بین پرسپولیس و نساجی به جمع قرمزپوشان بپیوندد.
🗞
ورزش سه
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137155" target="_blank">📅 21:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137154">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
با بازگشت مهدی ترابی به تمرینات تراکتور، پروفایل وی در ترانسفرمارکت به‌حالت اولیه بازگشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137154" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137153">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه: سیزده سال از عمرم رو با عشق به پیراهن پرسپولیس زندگی کردم. با کوله‌باری از خاطره میرم. برای همه شما آرزوی بهترین‌ها رو میکنم. کسب قهرمانی ها و کاپیتانی پرسپولیس، همیشه در جانم زنده خواهند ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/137153" target="_blank">📅 20:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137152">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16152d790d.mp4?token=MWVxNta_9kzEb-md2YcT4Ijn2St-2geIl_smshJl1ND1cFLqzGHlcaGK0Ki4JLXdBPeD8NttKB0q-10X5cNbsD45rii_0F7MwlAb27cz-NM8hcXKRRkkF9UdIaIucbpaBF71LC8asHgDEL4r4h5i5s2RLNFds5apghqcX278WcfOFLgP03d-4RPSkl9a86lnvnAqYuHwCL30XBtoR11PboBvAW_bDcPRyxt9jxnmoPeh1jYTCMAdaOe8-aMBj1StxemMFg7sJ28ZmLCx0zmsFwxGRZl8aj5tz2-jSaF3j11GtBpyyAVGrN10IStuICm0e8pemB0TTFv5UxMv5exM_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16152d790d.mp4?token=MWVxNta_9kzEb-md2YcT4Ijn2St-2geIl_smshJl1ND1cFLqzGHlcaGK0Ki4JLXdBPeD8NttKB0q-10X5cNbsD45rii_0F7MwlAb27cz-NM8hcXKRRkkF9UdIaIucbpaBF71LC8asHgDEL4r4h5i5s2RLNFds5apghqcX278WcfOFLgP03d-4RPSkl9a86lnvnAqYuHwCL30XBtoR11PboBvAW_bDcPRyxt9jxnmoPeh1jYTCMAdaOe8-aMBj1StxemMFg7sJ28ZmLCx0zmsFwxGRZl8aj5tz2-jSaF3j11GtBpyyAVGrN10IStuICm0e8pemB0TTFv5UxMv5exM_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
🔥
امروز تو یه بازی فوق‌العاده حساس ژاپن بلاخره باخت و امریکا به فینال لیگ ملت‌های والیبال جهان صعود کرد
🇯🇵
ژاپن
2⃣
-
3⃣
آمریکا
🇺🇸
🇺🇲
USA= 25 | 23 | 20 | 25 | 15
🇯🇵
JPN= 19 | 25 | 25 | 19 | 13
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137152" target="_blank">📅 20:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137151">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzpInDuG3tIEPCvSderuUFdp_MRW0vL82JghG-B0XKwqpA8JhbF1MsI2bSTdBQytnhDdX0G1hFIi9iTJOX19kektoVvEi3A7QkcoJgqxiWbnsp5eyYk0uDzcHqVPBn0gSinLrZCLMGZ1WlNzncyem9-LF00dDSIlO2yd8KtFyfNElJW91x1RZHY-MmYuE4dlP4WbcMC3EaQ5L3jA3ZsWOl2fQbFacAEZESopslNQogGSdVjNkrHxz353mIax0v7jip6Z8vJvCxkKr-ZToLqzvmxTY12_8ck6pl3L-WbVa60ImYk5QuvZuJXD9fWG-7WSGLCmyMER-CykudIdXROzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇
⬇
⬇
با‌ارزش ترین تیم‌های ایرانی:
•
پرسپولیس: ۱۶.۵۰ میلیون یورو
• تراکتور: ۱۴.۳۰ میلیون یورو
• استقلال: ۱۴ میلیون یورو
• سپاهان: ۱۲.۸۵ میلیون یورو
• نساجی: ۷.۶۳ میلیون یورو
•  خیبر: ۶.۳۰ میلیون یورو
• گل‌گهر: ۵.۹۳ میلیون یورو
• فولاد: ۵.۸۸ میلیون یورو
•  ذوب‌آهن: ۵.۲۵ میلیون یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/137151" target="_blank">📅 20:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137150">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJXjSO5vK086Ia3H4J94I6yCG8P5yozXJCeSCMgXAFfFTBasadlK2OBroRk-s5w5IX2Si_KdxbJyveRB6OkijAbsvM9tpc2WKZNEoSbhFQ50D5CVEzoa9Qj_bd_v_ELtxDgPJZW7mj10moEHxaOuapCmXVKqPgNlAVFDquW9AABEETZxdx1XJlOAJm7HtP1MKIV3GT2u_HGh_r8tLbdbLow5ykag6KA5Z4KEal7QW4wGdhI5vzLklcVqScRpcQ8MLDkPh5crlYj28z0AQqmXfDiO8VgPtI-9BuhXV5uG0OHfQJHSuA3zSiWNjYUcNKGpQvpB5VJLJgta5slf3-VHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
دوئل تمام‌آمریکایی؛ فریتز به‌دنبال اثبات برتری مقابل ناکاشیمای آماده
🎾
Nakashima -
🎾
Taylor Fritz
🎾
تقابل تیلور فریتز و براندون ناکاشیما، نبرد دو تنیس‌باز آمریکایی با سبک بازی تهاجمی و سرویس‌های قدرتمند است. فریتز با تجربه بیشتر در رقابت‌های بزرگ و عملکرد باثبات‌تر، روی کاغذ شانس بالاتری برای پیروزی دارد، اما ناکاشیما با بازی کم‌اشتباه و ضربات دقیق از خط انتهایی می‌تواند کار را برای هموطنش دشوار کند. اگر مسابقه به رالی‌های طولانی کشیده شود، شاهد دیداری نزدیک و باکیفیت خواهیم بود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/137150" target="_blank">📅 20:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137149">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
استقلال دیگه منتظر رامین رضاییان نمی‌مونه
💢
هوشنگ سعادتی امروز با حدادی درمورد رامین رضاییان جلسه داشته ولی نتیجه‌اش نامعلومه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137149" target="_blank">📅 20:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_FblTlf3jQRqNX1I691JQsyhyydHG_cmcTUoMOLMtErSYKyfOCsCz-px-hD2EZlG4Aq94xKsV7agrtfGjCP-l0PDU_OoibSSWYMkTS6qdtyu8J1cpA9hGfzF17Rqqroqi9Xyqyr3dDGGA3kJ2xRs7bElVkJUCq_Gnh8BoDuhNoo2-DaN26RjJDls-PEYtkHozNo_S-j7H9TaTmjRO7EHiteCRr-cVuHTxm0Hq4iBdRracPFj49FE_LTolvMWa91Add7EIL1D_wXFV_TjQwdqU_QyPQf7HRKwPT_IiZqfNO5hoItm6LuGcVydCBDrLCssUDTonppNRJRffWArZC-Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📎
📎
تصویری از جلسه امروز پیمان حدادی و مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137148" target="_blank">📅 18:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137147">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
کاروان پرسپولیس دوشنبه‌ شب به تهران برمیگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137147" target="_blank">📅 18:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137146">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gqq1Z4cYjpaty_2I8redDFMAt6joT4XDLWGwFnkihKGd3ChGIp9MVjJqsdK-7hvuNxyBA8_mwPgDtxKD8RnAksXE5RxEqhtf-EoV_TjUMvH0gMsbn2d3Aohd09e1DxVu9hqiudKI2N29oUiO-u7dz8MqRhi7S9SlBfX7z8v-9TB1gEkGg222ljtfscX3poc8QbHwD36kbpVJ6ZRiHO5Ms9sqfJ_xiPMRCO2GXpIyDOdSiEki5Eqy817b4VGilxfl0Bvsdq9P6rDmgAkBQtenHXAXJEPL195lhkgh1xaX4ypmOtbsR-yhlfFzz_-0AGjQhInkY6VPnWjVSK9ALi3qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاروان پرسپولیس دوشنبه‌ شب به تهران برمیگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137146" target="_blank">📅 18:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137145">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔉
دانیال مرادی رئیس دپارتمان داوری فدراسیون فوتبال: تمام ورزشگاه‌هایی که در فصل جدید میزبان مسابقات خواهند بود به طور کامل به پوشش VAR مجهز خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137145" target="_blank">📅 18:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137144">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
❌
بازگشت اسانی به استقلال و خلیفه به الومینیوم تخلف محض است
🔴
🔴
هر تیمی که با الومینیوم و استقلال بازی کرد بلافاصله شکایت کند.
⚪️
⚪️
همانطور که پیش بینی کردیم می گویند خلیفه به الومینبوم بازگشته و این تخلف است چون استقلال او را معارفه هم کرد و نمی تواند خلیفه…</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/137144" target="_blank">📅 16:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137143">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/137143" target="_blank">📅 16:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
ورزش سه: تیوی بیفوما تا این لحظه نتوانسته خودش را به تارتار ثابت کند و در نزدیکی درب خروجی باشگاه قرار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137142" target="_blank">📅 16:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137141">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/SorkhTimes/137141" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137140">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
✔️
شرایط ایری از نظر حقوقی متفاوت با کسری طاهری است.
✔️
اینکه پرسپولیس همچنان دنبال کسری هم هست یا خیر و اینکه نساجی حاضر به انتقال فقط ایری می شود یا خیر نمی دانیم
✔️
تارتار بشدت دنبال جذب مدافع میانی و چپ است و ظاهرا گزینه ای جز ایری و رزاق پور ندارد.…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/SorkhTimes/137140" target="_blank">📅 15:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137139">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6gIKjX-Deg8pQxRWHeWWbnGZvczHW_TCEM5n2YuyLj-DWudHoDCpmJiLN-ivUazkV40oEG1LvTpXvRltfyz0Bp-S3z5oP91uSsg_VEVodtZejTZZN4gPQr1K2Fql7t_p_QLFc9cnLX7qhvJdfSiA5R-j2vGmGRaF9W8riBgHmdJebDh8yuv895PL7BXvWz06E1PdwMocmftZGSUN0eNwvJHs7pPG2qGmgS3izRy1ti39Mghw7y-ElAURrVI-SPXupiiYPvlKSnbhDGI3EcxuapOxYHt3y0Q6_Wnv_I5lm26kyuNJ7ACDdMb1aeuYB6ciPKWuS2Bml7bGXOlRG-awA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قدوس در لیست خرید پرسپولیس نیست
❌
🔴
برخلاف برخی گمانه‌زنی‌ها درباره مذاکرات و پیگیری‌های پرسپولیس برای جذب سامان قدوس، این باشگاه علاقه‌ای به جذب هافبک الاتحاد کلبا ندارد و نام او در فهرست نقل‌وانتقالاتی سرخ‌پوشان جایی ندارد.
🤩
خبرگزاری آنا
🥈
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137139" target="_blank">📅 15:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137138">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
❌
آنا : پرسپولیس برای جذب ایری دوباره از فیفا استعلام گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/137138" target="_blank">📅 14:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
پرسپولیس برای جذب ایری دوباره اقدام کرد
🔴
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137137" target="_blank">📅 14:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
⚠️
باشگاه فردا میخواد برای رزاق پور نامه بزنه و پیشنهاد معاوضه بیفوما و 80 میلیارد پول در ازای جذب این بازیکن رو بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137136" target="_blank">📅 14:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
خبرورزشی : شنیده‌ها حاکی از آن است که با توجه به عملکرد نه‌چندان امیدوارکننده ابرقویی و همچنین منتفی شدن انتقال دانیال ایری، احتمال دارد کادر فنی در تصمیم خود تجدیدنظر کند و پورعلی‌گنجی در پرسپولیس ماندنی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137135" target="_blank">📅 14:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5ueK2RA4wspYfBvduVYL425JWjEBCcJrezph-YhQI5Gai87dgvLZn2AZiE7w8zyxSvcrh0JqFelqF9ZEkbXFJY6xkV_p4euVMYMsYWFqn2Vr6hHwY9CNsDXVv-8ELDELXhZRktQmZfYGqonFbPtYg39VjoDQ0Ny5IvyKW86ut0kJf66IylWditJnIORc2ay-gOjNXIlpcGREf8qxKmgBqZH56SKmZeQPX07118zitBc_FKNIt1AWbZabnMZy-1X64_i65pL9obm-jpe9uF2KuXDVJUenvQikXGLzj6xeo_CNdD7hT62olsOVFexR87BY63zYKHQtV1ecZejyil0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
آخرین ایستگاه تا فینال؛ هیجان نیمه‌نهایی لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
شنبه ساعت ۱۵:۰۰
[
ژاپن
🇯🇵
🆚
🇺🇸
آمریکا
]
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
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137134" target="_blank">📅 13:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137133" target="_blank">📅 11:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137132">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SR8p8s1m4fh8CZ-5bG1oTY5NtQzx3mORENhSC7rhT94rMoANpzEfLc_C01-rJ-p63V0bC1xce6pmnzXZrT9M2KlRL-udEsA_6163uJ3LPwkQhafhN2L6RJH7PkH01_zmDhfh6nrXUnJPq6wkTZtlWZlI1baVUB0YqYf84Xb1F7JCO65l1VsEeZmnDl2b2B2iIjSypSCdCHvji205o-i6FIgTL3jrxQNxIZNuKOCxjy_upVU-Re9F_CwmQ_9dyUUsDJmckcf_cyXlj_EcVhW9d5ZhWAWnfpDQNYeF7Owviwmc_UAJsf9Zj8bzJiul5gQL9I-Di9z52kZzqFktllmFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز: بمبی که دو روز قبل بر روی یک خانه در قشم پرتاب شده است حامل یک تن ماده منفجره بوده است
‼️
پ.ن خدا لعنتتون کنه ..با مردم چی کار میکنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137132" target="_blank">📅 11:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137131">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⬅
یکی از نزدیکان مهدی طارمی پیشنهاد پرسپولیس رو به طارمی تایید کرد اما اعلام کرد طارمی به ایران برنمی‌گرده/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137131" target="_blank">📅 11:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137130">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔽
🔽
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137130" target="_blank">📅 11:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137129">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
🔴
تارتار هنوز اعتقادی به دنیل گرا ندارد و دوباره به او بازی نداد، اما چون پرسپولیس برای جذبش هزینه زیادی کرده و قراردادش هم سنگین است، این مدافع مجارستانی فعلاً حاضر نیست قراردادش را فسخ کند. / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137129" target="_blank">📅 11:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137128">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🫥
🫥
علوی سخنگوی فدراسیون فوتبال: برگزاری لیگ برتر بدون حضور تماشاگران؟ این موضوع در جلسات در حال بررسی است ولی لیگ با تماشاگر قشنگ است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137128" target="_blank">📅 09:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137127">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه: سیزده سال از عمرم رو با عشق به پیراهن پرسپولیس زندگی کردم. با کوله‌باری از خاطره میرم. برای همه شما آرزوی بهترین‌ها رو میکنم. کسب قهرمانی ها و کاپیتانی پرسپولیس، همیشه در جانم زنده خواهند ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137127" target="_blank">📅 09:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137126">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس؛
✔️
آرزویم این بود روزی که می روم شرمنده شما نباشم
🔴
🔴
خرم آن نغمه که مردم بسپارند به یاد....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137126" target="_blank">📅 08:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137125">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-CYe0kWLh4KUUe_Mp24jLs5DvqDrQAMdM8ppYet1jktP5fuuA3s0FGhgySeEP1q8rEbytHN81YW3-7jyqSYMyeTIb2VcLK2GR7u-AWz75YZbr3ud2fcjmcR26nWr5JK7dKEABVb9gH1D5F84TaDpkhMpzLU3pBHT5IeNItv3OralIFmByz6iMXzIf97-XL8P_G0bCxL21H-UJ1gBFMaDgLLBHW18cVEASW09tSnDz-u7LF5750b-s8h4DpaALrt1AFo31xqzaYHWTlZswWeZOCSFc2h63PgeCQggnN651YrUssBVNSvpinRPEkOYg8txXqliF2JyLEs7ugGGL2u7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137125" target="_blank">📅 08:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137124">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsQUqnFodtabYba10YV7HaKWZ6mi-QRq4pOaMd5TEqzgDAkESuaRYMb_vPanhOcqYEtlWv5Z2-frE9g8Ye6yRKbBwm2Cb8lTLCPM364017xi-_Aer9m-ywYtWhh-If1u14wbpB-LDuUpR-RIWhlHDcJ-ZxCtopEHLx25_2fz8jADIJ-YdOM66_7vqzVroETFXMc87XbihJ1EdTOn4tJ4oH134tPewW7mTPjCygQSOyGw8h9aLW3AnLUZ9yoLVT0a5Xdq_IsxqJYOgAcbLUwzY3tfP2VoTpGQ6ffNP5U0cwvtgdXXA2G0xFbANiXkBa8IlX-hS2zJVoF91wvJBsfezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
آخرین ایستگاه تا فینال؛ هیجان نیمه‌نهایی لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
شنبه ساعت ۱۰:۳۰
[
لهستان
🇵🇱
🆚
🇸🇮
اسلوونی
]
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
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/137124" target="_blank">📅 02:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137123">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔽
🔽
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137123" target="_blank">📅 02:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
ترامپ: هر کشوری جای ایران بود تا الان تسلیم شده بود اما اونا نشدن، من اونا رو تحسین می‌کنم. شجاع و سرسخت هستن ولی خب تهش تسلیم میشن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137122" target="_blank">📅 02:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
❌
شاید مرتضی یک فصل دیگر ماندگار شود....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/SorkhTimes/137121" target="_blank">📅 00:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACiJrgYEbB6FwNk8Z4zlfh-mzNBTVKTTqVIjEmxQTDOl0wCW6TEYDdkidGpK0gFtr5Sv8QFEUCVoqEE2kq-KM8Ad6buBkgvyw0uOPKvdRldwc33HNu5eCsKVsHkFVEH_w9kTk0MAoCNXw16KdEVk8ybeKjkUOuRujWFTRrygcb3G_szQ_vj545EdKbP0jdZ5putjF8cSAZpPoEvqWWzgzF5wnOlZHcAGXZJ3xgkbqu-eRrM52Pja75bOn8ESUIXXpU2y18q7ScbpZ-Th2uIzMrpA6GOmhfWrRjb37LVgWb0x6_PqXr11CS_o1SPXxOW5Kqvt-t8uIBf3f7sFd-QhbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گفته میشه آخرین رقیب دوستانه پرسپولیس در ترکیه این باشگاهه:
✅
7 تا بازیکن خارجی داره با اینکه لیگ دسته اول ترکیه هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/SorkhTimes/137120" target="_blank">📅 00:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137119">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
❌
فرهیختگان: همایی فر عملکرد خیلی خوبی جلو آلانیا داشته ولی تارتار همچنان خواهان رزاق پور هستش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/SorkhTimes/137119" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
باشگاه پرسپولیس خبر داد: امید عالیشاه با توافق دوجانبه از پرسپولیس جدا شد
❌
باشگاه ضمن قدرددانی از فسخ توافقی خبر داد و برای او و سرلک آرزوی موفقیت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/SorkhTimes/137118" target="_blank">📅 23:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
براساس قانون جدید سازمان لیگ مبنی بر اینکه تیم های حاضر در لیگ فقط 4 سهمیه خارجی میتونن داشته باشن پرسپولیس در حال حاضر 5 بازیکن خارجی فعال در تیم داره باید با یکی شون خداحافظی کنه که قانون جدید سازمان لیگ اجرا بشه
✅
دنیل گرا
✅
مارکو باکیچ
✅
تیوی بیفوما…</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/SorkhTimes/137117" target="_blank">📅 23:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚫️
⚫️
فرهیختگان :تارتار هیچ نظری روی دنیل گرا نداره و گفته باید جدا بشه ولی محسن خلیلی مانع جدایی دنیل گرا هستش تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/SorkhTimes/137116" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔄
🔄
دربی افتاد هفته پنجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/137115" target="_blank">📅 22:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
شایعات؛ رامین رضاییان تمایل داره به پرسپولیس بیاد و تارتار هم بهش علاقه منده!  نظرات؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/SorkhTimes/137114" target="_blank">📅 21:58 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
