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
<img src="https://cdn4.telesco.pe/file/D5_qugTFleMna3HFw6D_2CgoKA92kAeUpXf2mkGydU7E85J7NUrkQiNkyq8SqsFu1aIxX7cA8jVjwkE6OUIiTFXgMacGP2_aZiXL2t8AQvhUp_YyYq3U-zvdCB11M-jFSjpoc6tUIhsWrIk9qvlIZwfZtdUEQQgqVIlKUnbPL7VMMvj9lmy8SwCljnQ_kYWIzva6kcCXuz1NMy6_Ur_IUFVnHy5Bu6h1OQnZY2lZ34SjLmadegXz3sNaN338Hz3_yZzxCZZ1U-dhIrRqlX5VDwpgt3F2zJXO3blsT-lZ4-rnqfieXO-p18pyQQ2bWz9t4_P-7VO01zjLWCGSrIGK_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 15:42:41</div>
<hr>

<div class="tg-post" id="msg-134536">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 426 · <a href="https://t.me/SorkhTimes/134536" target="_blank">📅 15:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134535">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏐
برنامه کامل مسابقات تیم ملی والیبال ایران در هفته دوم لیگ‌ ملت‌های‌ جهان؛
❌
از فردا شب شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/SorkhTimes/134535" target="_blank">📅 15:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134534">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/134534" target="_blank">📅 15:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134533">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
تمرینات پرسپولیس به مدت شش روز تعطیل شد و قرار است از شنبه هفته آینده تمرینات پرسپولیس برای فصل جدید در تهران آغاز شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/134533" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134532">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⚡️
2- آلویس نانگ (Aloys Nong)
⚡️
آلویس نانگ نامی آشنا برای فوتبال‌دوستان ایرانی است زیرا عملکرد خوبی را در لیگ برتر ایران با تیم‌های فولاد خوزستان، نفت تهران، تراکتور، استقلال خوزستان، پارس جنوبی جم و سایپای تهران داشت. او که با سابقه بازی در باشگاه‌هایی مثل…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SorkhTimes/134532" target="_blank">📅 14:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134531">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚡️
⚡️
- سانل کونیویچ (Sanel Konjevic)
⚡️
این مربی اهل اسلوونی دارای مدرک یوفا پرولایسنس بوده و در زمان بازی، حضور در تیم‌های اسووبودا و اینتربلاک از اسلوونی و فرلاخ و استراسبورگ از اتریش را تجربه کرده است. او به عنوان سرمربی در باشگاه‌های اینتربلاک، برینیه و…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/134531" target="_blank">📅 14:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134530">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
آشنایی با کادر احتمالی اسکوچیچ در پرسپولیس؛ از مهاجم و مربی سابق تراکتور تا دروازه‌بان سابق دینامو زاگرب
👇
👇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/134530" target="_blank">📅 14:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134529">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
سایت اسپورت نت کرواسی مدعی شد؛اسکوچیچ و سه مربی از کرواسی، اسلوونی و کامرون در پرسپولیس
🔴
- آلویس نانگ بازیکن سابق فولاد و تراکتور
🔴
- سانل کونیویچ دستیار سابقش در تراکتور
🔴
- ماریو یوزیچ مربی دروازه‌بانان سابق رییکا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/134529" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRnxbRG9eRvjAuM_NIWu44OyasxUNZK62wnDKHWUiwS0fDSUKESg-JgCMg61IK81KfNvcnUe-6t-tCFpmSrd-KeyXINvaIntQjkL78l-5iR5Citztn36HrRhLo0tQxfEUHl8bJi6zQPD9m0szeFQ8caGzXejGtVxv75r4Tks2W7ouxmbzE6jn3cLH_02woMgd4_IMRTnASy_xGpz7f6fRMiBsZWUs_GsC-yKa7XwRG_6YOqrRNlCqvjy0R5QT2GXH3ISZTToFDIatd5Igfv4125-95XkR1tRb8CQhPg413WhA8ob8oNkk4oqE2LMmPxHuun5VYbtZBO5u65pllvrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویری پربازدید از اقامه نماز در رختکن تیم ملی فرانسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/134528" target="_blank">📅 14:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
اخباری: گل لحظه آخر را بازیکنی زد که تازه داماد شده و دیشب به تیم اضافه شد. او گفته بود روی من حساب نکنید ولی گفتم کنارمان باشد تا روحیه بدهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/134527" target="_blank">📅 14:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134526">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/134526" target="_blank">📅 14:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134525">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy5q3XXKB11Y4Ydu2p_kcSsxtTCUgvEnooE7QIkCONAhhG9tIMrtqyPZnChPvtaRgrgl0i163oh0TpXvpKrDp7oCm53ATZqfG2_4peYhxnPGh0UlD4PkSw2EFx5ENzjwp6EV_Xtl96ptnz2eBZS850Xhg4u5VO-zdTstxDtAkZnf2hPf9FGc6P3mfjuukSSPUI5VleSRnE-SZQN2EUE3nEEjYYDJPJZqMreeYak78rJXQSMBirFNFkxZS2AwF5kBIoWnNBVtf7SdIm8Nu8cPoH3ZWANHA4UHrQMX10HjeATqZ5SL0vTLpUjnc1Q68Y_8w3_q1rlvmB77myaLdEtXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/134525" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134524">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⚡️
تیوی بیفوما و دنیل گرا برای فسخ قرارداد به باشگاه دعوت شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/134524" target="_blank">📅 13:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134523">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69fbc8a47.mp4?token=W7kNWzmy_6gfqMzYHqHzN-oRpEXYKdCI983goFd2A22T5WXLYIKwxFsmsQtSKw7P94Dr30TeH38at6bZ5RWm1bwrar-lwaMyj6m-JESvutM66QaeGrtf9kygbeLcgUwFJCytiJW40QmxX-NhjIAfFmHQab3zxwnqF7wMrbTfEZhDbjxxauyYwVqg9jRutGgALqNZiK8DspeRjVrTA1qV8BQnJ-K0zuTK3u38pU5JxGEA2XGjyVA_d09ytpYGILyRWrLQGcx4PeDgaUz8Y5meU_FsyUwNIYCi1CjCwP-DJB3I8-hNQQwK-eH4Wx-13X1zvH8E_REVvcaYqQBQb19AcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69fbc8a47.mp4?token=W7kNWzmy_6gfqMzYHqHzN-oRpEXYKdCI983goFd2A22T5WXLYIKwxFsmsQtSKw7P94Dr30TeH38at6bZ5RWm1bwrar-lwaMyj6m-JESvutM66QaeGrtf9kygbeLcgUwFJCytiJW40QmxX-NhjIAfFmHQab3zxwnqF7wMrbTfEZhDbjxxauyYwVqg9jRutGgALqNZiK8DspeRjVrTA1qV8BQnJ-K0zuTK3u38pU5JxGEA2XGjyVA_d09ytpYGILyRWrLQGcx4PeDgaUz8Y5meU_FsyUwNIYCi1CjCwP-DJB3I8-hNQQwK-eH4Wx-13X1zvH8E_REVvcaYqQBQb19AcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مصاحبه قلعه نویی بعد حذف از جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/134523" target="_blank">📅 13:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134522">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNPpokaejv-9RGaAXR0sggNQee48dTOWNAz7bwyEOjAXWXPEvMGf_yy6-t_nNqs2sKf7L0zeCj4z0EEk9yVnQ8Pbcl1HNM5w1cI6DR0FCVK2dWMi4P1h0N1KiB0r4PJJq49p7lv574vbCmaQxeHF8nTRhtAQiecVOqWLzX1koH4ubR3xlEpzH1DM9ozyGFyOgrwBnh0ZM3S-WfkGEHruCfOc7tDCUE7vIBlNUad9VrIrEwnW-tIMfJXqBvSIViRABib7pdM0aW-Lyb5axw3S6V388QKSfAuddfseFTqxYSSmC66HtyYQEYvWlWgcxw47DBqts7PbpzzlE_X8F9KLnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
یک‌شانزدهم نهایی جام‌جهانی ۲۰۲۶
[
آفریقای‌جنوبی
🇿🇦
🆚
🇨🇦
کانادا
]
⏰
یکشنبه ساعت ۲۲:۳
۰
🏟
استادیوم
سوفای
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
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/134522" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134521">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
قرارداد گولسیانی با سپاهان 700 هزار دلار بوده و او برای فسخ قرارداد، کل این پول را خواسته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/134521" target="_blank">📅 12:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134520">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
ابراهیم اسدی: شأن پرسپولیس حفظ نشد
🔴
🔴
پرسپولیس در حد و اندازه‌های همیشگی خود ظاهر نشد و این حذف برای هواداران قابل قبول نیست. ای کاش تصمیمات مدیریتی و فنی با دقت بیشتری اتخاذ می‌شد و تیم در مسیر بهتری قرار می‌گرفت. این سبک آسیایی شدن در شأن تیم بزرگ و پرهواداری…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/134520" target="_blank">📅 12:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134519">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uitI5KiQFpRRg8rd8zqrBXZYSyftJfUD7Mp8GcpkyCRCRt_648uICJU1Z7ztwuu6PnRpDxxxaI7uR0eh-09vdHAwEdRDv2uHiq1bg4sz3oMJf2djK-3yHghUgArdVLwmTuAg4x5B2xSivwoMLeq0d1SlazaO06aGBMdE34rthOLt3ftJjkYCf3kJvi3hNO2XdBLCd0vKQoI1kitoM7lcGkPiDQ5mickLOXP6kslaiQ69o7DAG4bsJa2fZ57kWq2bdA1E_5ZSTcr6DUKxwPIeh-b8-u5Wg9Ng5v9Dh0f7LPnEFeMOlL40T1Jsf77pQQLGjNdZPO9rBRHtfssbm0XzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعد گل سوم الجزایر اینجا بازیکنشون میگه اگه ببریم میخوریم به اسپانیا و ریاض محرز تازه میفهمه چه غلطی کرده بخاطر همین شل میکنن تا گل سومم بخورن.
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/134519" target="_blank">📅 11:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134518">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/134518" target="_blank">📅 10:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
دیدید حالا نمیشه
✌🏻
🔴
تا وقتی به مردمت پشت کنی و دل مردمت باهات صاف نباشه احتمال ۹۲ درصدی صعودت هم به صفر تبدیل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/134517" target="_blank">📅 10:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134515">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">😂
😂
اتریش دوباره زد و ایران حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/134515" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134514">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/134514" target="_blank">📅 10:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
بجا مانده از امروز صبح
😐
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/134513" target="_blank">📅 10:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li_GCBNThAGCZRFuM83Ah0-eq6c7hFBgp8KLTiOzb14X1_ZpoFjH4vJnZG4vpobjq4fFM7akEHWPrpsEPMYIir7QRjFFuOIrTI6XnfjbAAKrSw7OubkpxoGTs8Q2Etr8UoHO2WJ9VG55wHOpSKFd4crYkP4iOOSc8oyckMVp-TdeccK0BOpJRAtZgpIXdAUL1xqBgm1EP_lImo_F_f01GJx2vVvoGFpkPl_rgSak1fq8ehZDVSqrX8XTn1kGYjkbZx7PNgEQAsG8FL65bfcrvj_JNslW5-kfRa8KxjjkVWyiYvO869GbtL3JZCV8Xe76RCuNCBFKVfNdlRPdWr1w0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/134512" target="_blank">📅 10:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
یادتونه ژنرال قبل از مسابقات میگفت تیم ملی یه کاری میکنه تو جام جهانی ایران یه هفته تعطیل بشه؟؟
🔴
هفته بعد تقریبا ایران تعطیله کلا ؛ ژنرال صعود نکرد ولی قولش رو عملی کرد
🙃
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/134511" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0mCnzZayxuFnyQcVCSz9sBKb7bOVhFh0SkSoip3AsYyso02j6I02SvZr4LPOAwNmEXB_pYHh8Pk8RWG9iXZsZDaMoefqB08fphquqMlr2XzmGIzBc4DclbbJMtyyfK_KAGKYGFEhwZE6hi3NCZZ-kbL07VvEeAgO3mw9j9iuYc10cU5h3CaXlGOzAkam_FjpODETSNaQZayKyYKW4Kqa_7vqfSQoK_qI-lRAogniHVuW2uG9nDVcaDFKS8IM4-SOnbP1b5aoTiAkiUOjXv6hGvIDGi9lub0k4yElnd70jnpwWGCobODSaBbMXgEHYdQFaqHs2qjCp19cKJqvq2i2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یادتونه ژنرال قبل از مسابقات میگفت تیم ملی یه کاری میکنه تو جام جهانی ایران یه هفته تعطیل بشه؟؟
🔴
هفته بعد تقریبا ایران تعطیله کلا ؛ ژنرال صعود نکرد ولی قولش رو عملی کرد
🙃
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/134510" target="_blank">📅 10:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
❗️
تسنیم : قرار است به زودی در وهله اول باشگاه پرسپولیس مراحل اداری قطع همکاری با اوسمار را انجام دهد و سپس به طور رسمی جدایی این مربی برزیلی اعلام شود.
🔴
🔴
پرسپولیسی ها که با اسکوچیچ برای جانشینی اوسمار مذاکره و توافق کرده اند، هنوز هیچ قراردادی با این مربی…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/134509" target="_blank">📅 09:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
دقیقه 92 الجزایر گل زد
گزارشگر: ۷ تیر رو یادتون باشه؛ یه تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد.
😂
🔴
دو دقیقه بعدش اتریش گل زد
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/134508" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/134507" target="_blank">📅 09:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b235a5b41.mp4?token=Vl013Ol-pMXrkH9B5MRc25_LatEjymUEdxrrfBIiwY-vtiJ9ZjtDktHmqrlLEuLQEi7Y5iDS2d77n99X1JTrw5B8qQbhZDliPYAnyB6TsyjxllE1Y_O9IPpfed3p67IeWK_NeBTwbkjGuWFVGVXMnjqkqmBPHTQ54ITRjG68NmoYnGfjZ3FbAm3R51og3pvF8eMJOgarRFyzepSbRk03_B8LqMydyKBbZ_ED6Q3R5t4PNE_20-gxZuYzDNkQ13Ow2-pzpHvA_dJdrFUR8jGkxRt0tc-fHJnB58n-aX7624aogKMsBW0PItM_PKTq5409vNrrpewsE314z_dTWy9Zq1P7Xbn0b63FzDNso5SKXSbdrhj2RQFQWAnxeAqmVIV8kGKVPADCLeNnQlZQxw6oeA7bZky2RsKrSElUZSR47SpQCpOVbN9GxxDRoKzhzPE_APTeB8cWKvaEqzlYlaxWe2cjj4uxnI2xxQyANwPg78td_btEeL3Bn0KEfyC8wk0b887sp1My2jXZzEXJeS0ExbTjTE4VLhua3svyYfLhJiPRyLa9yqTa7N9mvjZDbP8S15cyjCXZZDwdvPxEe8ix1nsu09HXf-s7NfhvRbccyX-wovc2brY1NTKRlIbL6j9uM9WDyvsMN5rcPV2STK6rl1DQcLNOq03g8szzAefSO2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b235a5b41.mp4?token=Vl013Ol-pMXrkH9B5MRc25_LatEjymUEdxrrfBIiwY-vtiJ9ZjtDktHmqrlLEuLQEi7Y5iDS2d77n99X1JTrw5B8qQbhZDliPYAnyB6TsyjxllE1Y_O9IPpfed3p67IeWK_NeBTwbkjGuWFVGVXMnjqkqmBPHTQ54ITRjG68NmoYnGfjZ3FbAm3R51og3pvF8eMJOgarRFyzepSbRk03_B8LqMydyKBbZ_ED6Q3R5t4PNE_20-gxZuYzDNkQ13Ow2-pzpHvA_dJdrFUR8jGkxRt0tc-fHJnB58n-aX7624aogKMsBW0PItM_PKTq5409vNrrpewsE314z_dTWy9Zq1P7Xbn0b63FzDNso5SKXSbdrhj2RQFQWAnxeAqmVIV8kGKVPADCLeNnQlZQxw6oeA7bZky2RsKrSElUZSR47SpQCpOVbN9GxxDRoKzhzPE_APTeB8cWKvaEqzlYlaxWe2cjj4uxnI2xxQyANwPg78td_btEeL3Bn0KEfyC8wk0b887sp1My2jXZzEXJeS0ExbTjTE4VLhua3svyYfLhJiPRyLa9yqTa7N9mvjZDbP8S15cyjCXZZDwdvPxEe8ix1nsu09HXf-s7NfhvRbccyX-wovc2brY1NTKRlIbL6j9uM9WDyvsMN5rcPV2STK6rl1DQcLNOq03g8szzAefSO2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134506" target="_blank">📅 08:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134505">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">😂
😂
اتریش دوباره زد و ایران حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134505" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134504">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
❗️
یا حسین ....الجزایر دقیقه نود و چهار گل و زد و ایران صعود کرد ...عجیبا غرببا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134504" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134503">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
قشنگ دارن دو تیم اتریش و الجزایر تو زمین راه میرن که مساوی تموم بشه ....و ایران عملا حذف بشه ..چوب و ضربه بازی نیوزیلند و خوردیم ..و خداحافظ  ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134503" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134502">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
ده دقیقه تا حذف ایران از جام جهانی ...هیچ حالتی اتفاق نیفتاد ...غنا باخت .ازبکستان باخت ..اتریش و الجزایر با تبانی و هماهنگی فعلا تا دقیقه 80 مساوی هستند و میل بردن ندارن چون هر دو تیم صعود میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134502" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134501" target="_blank">📅 07:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134500">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
مثل دیشب
🇺🇸
🇮🇷
فوری از باراک راوید، خبرنگار نزدیک به ترامپ: مقامات آمریکایی حمله به تنگه هرمز رو تایید کردن و آمریکا رسما مسئولیت حمله رو به عهده گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134500" target="_blank">📅 01:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134499">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
خبرنگار فاکس‌نیوز به‌نقل از مقامات ارشد دفاعی بیان می‌کند حملات هوایی آمریکا همچنان در جریان است که باتوجه به حجم تحرکات هوایی در جنوب کشور ادامه‌دار بودن آن قابل انتظار است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/134499" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134498">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
برای اولین حالت باید ساعت 12/30 منتظر بازی غنا و کرواسی باشیم .که غنا ببره صعود میکنیم ..نشد باید ساعت 3 منتظر نباختن ازبک باشیم .....نشد باید ساعت 5/30 الجزایر و اتریش مساوی نشه .....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134498" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2hT0Ky2GLuh7EEjJgyxravs-uDJdzFo4a04YmTxEn3Zv6EcroigurZoHwJBLo4qURlLGW0RwN8WEl5yhf1SSxHKRK6bRcXrzCpjooORxxbG59XxTDXmTofKWW6p3ksEWVJlIktYLccub7PoZ-Bkh9I_DHG7lRE5wURqg42WnNfsQOd1l5y5-aCykwNZ0ehetTxQodHBQPXF5X047wnlJfvJRTobsF6rXq9wET6_8-r1rh2een1raat8zHj0O_evxqEXp85dDI1W0MOpZ3pbqoT922rnaruMc4zcvio6KqAK7sseyBor8QdOIzna9J7mWBYwJaVvw4AI_T6w03DvLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جان سینا : ظرف روزهای آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/134497" target="_blank">📅 00:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134496">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
بعیدع کسی سه بازی و بیدار باشه .ولی امیدوارم صبح که از خواب بلند شدیم .بخونیم که ایران صعود کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134496" target="_blank">📅 00:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134495">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚽️
باشگاه با سرلک و پورعلی‌گنجی تماس گرفته گفته بیاید برای فسخ
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134495" target="_blank">📅 00:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134494">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134494" target="_blank">📅 00:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134493">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
ساعت 3 تا دیداری که روی صعود نقش دارن:
🔴
کرواسی _ غنا / 00:30 بامداد
🔴
ازبکستان _ کنگو / 3 صبح
🔴
اتریش _ الجزایر / 5:30 صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134493" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134492">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
جزییات تاریخ برگزاری آئین خاکسپاری علی خامنه‌ای (رهبر شهید )   ۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی  ۲۳ خرداد/ تشییع در تهران  ۲۴ خرداد/ تشییع در قم  ۲۵ خرداد/ تشییع در عراق  ۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد  پ.ن تخمین جمعیت حدود 25 تا…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134492" target="_blank">📅 23:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134491">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
مسوولان باشگاه به موازات این تلاش ها در تلاش هستند توافقات اولیه یا اسکوچیچ را به قرارداد منجر کنند. آن‌ها بر سر مدت قرارداد یا اسکوچیج بر سر امضای قرارداد یک+یک ساله و مشروط برای سال دوم توافق کرده و تنها اختلاف حل نشده درباره بند فسخ همکاری در صورت بروز…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134491" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134490">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
مسوولان باشگاه به موازات این تلاش ها در تلاش هستند توافقات اولیه یا اسکوچیچ را به قرارداد منجر کنند. آن‌ها بر سر مدت قرارداد یا اسکوچیج بر سر امضای قرارداد یک+یک ساله و مشروط برای سال دوم توافق کرده و تنها اختلاف حل نشده درباره بند فسخ همکاری در صورت بروز…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134490" target="_blank">📅 23:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134489">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a47998bb9e.mp4?token=Mme_wCrYH3-CO-vTzmfL51OkuJmkSx66ooeYSVwvFmy4PwW1vghhtvdmJP9juJNuiz-C8ktSTfQreU53TZKuYXy2ZvlLdJW47yN-nnuNNyONxo7i5gCHWVn0lyvepUiMtom9ps4OTKAlyHZcCBaQdWo1lh_w6DcjIfVypCSB5M4JNMeYmpa3RkDdMORoFpVPZZr6SSaJh8nSwoBGNB6cRhk72cGtNgdo7GfRY-GDBD3BZ4FE59M2XHDVFjV7815gsuDDRtUv6WteKbbcuiDB4BKMmMiTXVsv9tuiL1z7tiY0qsn3hMXQC-UIIvwxffWty_tEneundSeqgl27aGhh9QfjN3RsTS1xTL_nT0YP97E-NzOxt44-F0pazQMy33C1EwiEYIEg6T1FQn3kGGwhnt7c2Yxq_d2cP11B4STKPvj1HZfb-zYmCStq7KuETx9BHAJ38AxM_fHlWTnRGu1eVOeTF55d7ub7t7qDaEGtCIqqg6rX5ZK2DxdRjmbtZE00-vepQatuVwgYNzJZUk5MPeJmb4T7I6vIX2-Z9UxkXUT6w-r9eROXgtdVEoVzyLedfFrPI5fOj_jIOE4-2kdTyGZ7yFH39Jx-9AkfJM6Mg8IqAx4Kd9B4qF9oiSDKW7D1RJGBrkozsi4zNMr7aRTzB5yijrLSFi6xHJNWj3VB6u4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a47998bb9e.mp4?token=Mme_wCrYH3-CO-vTzmfL51OkuJmkSx66ooeYSVwvFmy4PwW1vghhtvdmJP9juJNuiz-C8ktSTfQreU53TZKuYXy2ZvlLdJW47yN-nnuNNyONxo7i5gCHWVn0lyvepUiMtom9ps4OTKAlyHZcCBaQdWo1lh_w6DcjIfVypCSB5M4JNMeYmpa3RkDdMORoFpVPZZr6SSaJh8nSwoBGNB6cRhk72cGtNgdo7GfRY-GDBD3BZ4FE59M2XHDVFjV7815gsuDDRtUv6WteKbbcuiDB4BKMmMiTXVsv9tuiL1z7tiY0qsn3hMXQC-UIIvwxffWty_tEneundSeqgl27aGhh9QfjN3RsTS1xTL_nT0YP97E-NzOxt44-F0pazQMy33C1EwiEYIEg6T1FQn3kGGwhnt7c2Yxq_d2cP11B4STKPvj1HZfb-zYmCStq7KuETx9BHAJ38AxM_fHlWTnRGu1eVOeTF55d7ub7t7qDaEGtCIqqg6rX5ZK2DxdRjmbtZE00-vepQatuVwgYNzJZUk5MPeJmb4T7I6vIX2-Z9UxkXUT6w-r9eROXgtdVEoVzyLedfFrPI5fOj_jIOE4-2kdTyGZ7yFH39Jx-9AkfJM6Mg8IqAx4Kd9B4qF9oiSDKW7D1RJGBrkozsi4zNMr7aRTzB5yijrLSFi6xHJNWj3VB6u4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
جواد خیابانی در ویدیویی به زبان عربی، از الجزایر تقاضا کرد اتریش را مغلوب کنه تا تیم ملی ایران به مرحله حذفی صعود کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134489" target="_blank">📅 23:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134488">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
یعنی هیچ موقع تو زندگیم اندازه امسال اعصابم خراب نشد،حالم بده
❌
نیم فصلم استاد خلیلی و فرزاد پوفو…. دل و قلوه میدادن باهام دنده دادن تا راحت این دلال های دوزاری اوسمار و خود کونده خارش زن تیمو هوا بدن،اقای حدادی تنها اشتباهات اوردن خلیلی بود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134488" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134487">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🫦
جمع کنید
کص کونتونو،ولدز
… ها دوتایی ریدید سر تا پای تیم برای ۵ ماه ۱.۲ میلیون دلار گرفته
ولدز
… گوه زیادی هم میخورید
🫦
کونده پدر
تو لیستی که به باشگاه دادی تو هر پست دوتا بازیکن اولت مال دلال های خودت بود کیر تو فیست
🫦
مرتیکه کوتوله تو بوریرام قهرمان شد…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134487" target="_blank">📅 23:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134486">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
#فرهیختگان؛ اوسمار وقتی فهمید با اسکوچیچ مذاکره کردن اصلا نمیخواست به تمرینات ادامه بده به اصرار ایجنتش این بازی رو روی نیمکت نشست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134486" target="_blank">📅 23:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134485">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
باشگاه باید ابتدا از لحاظ مالی با اوسمار توافق کنه و سپس از اسکوچیچ رونمایی کنه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134485" target="_blank">📅 22:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134484">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
نساجی مازندران به لیگ برتر بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134484" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134483">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
باشگاه باید ابتدا از لحاظ مالی با اوسمار توافق کنه و سپس از اسکوچیچ رونمایی کنه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134483" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134482">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134482" target="_blank">📅 21:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134481">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEb1kY0lL2QAfaHs6aav5604nvzIGzwxlYv5v_BSl79Qu2zD-NiRn9jxBuFaODJu3ct_GIG2HmZjEOZFizCU33fF23QQ2PtQ_05PD-K-hdc09SLYDXuyHh0F3sdsWdlekGCotrZF47Cokn0VIZlXrp5XmvChzy9OciM8cbBax7E0NPndRj_fe69NYpgRj8zO6UhAJ4pxjwmHBGqZ6qdIJvrWZgclFq5XrFimGtkOOos21jccncWD_4LXAA0HckGMeUmKr7fL4oX_-cqLSzMieUAWtYmK3ff9CEn5LogjwwSvOdKZxVoD9Xw73svkRga4i6PyEijlV1m9C5qAx7MpHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شادی بعد از گل شجاع خلیل‌زاده که تبدیل به یکی از بزرگترین میم های جام جهانی شد.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134481" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134480">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔸
بیرانوند و جایزه بهترین بازیکن زمین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134480" target="_blank">📅 21:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134479">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
❗️
تسنیم : قرار است به زودی در وهله اول باشگاه پرسپولیس مراحل اداری قطع همکاری با اوسمار را انجام دهد و سپس به طور رسمی جدایی این مربی برزیلی اعلام شود.
🔴
🔴
پرسپولیسی ها که با اسکوچیچ برای جانشینی اوسمار مذاکره و توافق کرده اند، هنوز هیچ قراردادی با این مربی…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134479" target="_blank">📅 21:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134478">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
اسکوچیچ سرمربی جدید پرسپولیس شد؛ توافق نهایی انجام شده و قراردادش تا ساعاتی دیگر ارسال می‌شود. او هم به‌زودی برای شروع کار به ایران می‌آید.
✍
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134478" target="_blank">📅 21:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134477">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎙
کارلوس‌ کی‌روش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتوانیم کرواسی را متوقف کنیم تا ایران به دور بعدی جام جهانی راه پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134477" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134476">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
واکنش تند زلاتان ابراهیموویچ به مردود شدن گل ایران: رؤیای یک ملت را دزدیدید
✅
زلاتان ابراهیموویچ با حمله‌ای تند به تصمیم داوران درباره گل مردودشده ایران گفت: شما فقط یک گل را مردود نکردید؛ رؤیای یک ملت را دزدیدید.
❗️
اگر این سطح داوری در بزرگ‌ترین تورنمنت…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134476" target="_blank">📅 20:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134475">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MimjR04UZtaE62AsMIesoZauqdF7Dj7LTLxiOl9Qn0SecJVZ2CI21O26RdUm0gMBtqrwzlCwKx95Cm0sVeYg5zxV4FumCQld_DMbyZSp_HtycuFzCgWS1vgs0GAwHCrM22RPj54ZwGc-iJ7IUU52LZlmwaGTeQ5kSbz4SUs3O2UZgceHb8W2l5sPi4WI1O61qk4iYSofwxsX5lTF2KWq8ZyBAUlNmkRIhDgRZWAQ_hJcGgreZ4h6uxlGBOo-7e4I67DSdJ5XhMU580MGyxe2c_Op9a9t-3LGXTeYaTnfnIwbdoFcBgG9R7nBlv_hKsrCuO_UkYqkiDbetZlsF04Ozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدار حساس و هیجان انگیر امشب پرتغال
🔴
-
🟡
کلمبیا رو در وینکوبت با بونوس ویژه و بالاترین ضرایب پیش‌بینی کنید!
⚫️
🔣
0⃣
2⃣
بونوس ویژه جام‌جهانی روی هر واریز برای تمامی کاربران!
🎁
تا پایان مرحله گروهی جام‌جهانی روی تمامی واریزها
🔣
0⃣
2⃣
بونوس بگیر و فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا پایان مرحله گروهی جام‌جهانی فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134475" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134474">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
نظرت در مورد بازی ایران و بلژیک ؟
🔴
ابراهیموویچ : نزدیک بود نیمه اول خوابم ببره و نیمه دوم واقعاً خوابم برد
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134474" target="_blank">📅 19:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134473">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از ایسنا:
🎙
اسکوچیچ سرمربی پرسپولیس شد و طی روزهای آینده وارد ایران می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134473" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134472">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
❗️
اگر اتفاق خاصی رخ ندهد؛ تا روز سه شنبه باشگاه پرسپولیس از دراگان اسکوچیچ سرمربی جدید و کروات خود در فصل جدید رونمایی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134472" target="_blank">📅 18:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134471">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
❗️
اگر اتفاق خاصی رخ ندهد؛ تا روز سه شنبه باشگاه پرسپولیس از دراگان اسکوچیچ سرمربی جدید و کروات خود در فصل جدید رونمایی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134471" target="_blank">📅 18:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134470">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
شنیده ها :باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134470" target="_blank">📅 18:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134469">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
⚽️
فرهیختگان : پیمان حدادی دنبال این است که با  دنیل گرا و تیوی بیفوما برای جدایی این ۲ بازیکن و فسخ قراردادشون توافق کند ؛ این درحالی است که هر دو بازیکن یک فصل دیگر با باشگاه قرارداد دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134469" target="_blank">📅 18:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134468">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیسم قبل تورنومنت 3 جانبه با اسکوچیچ بسته بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134468" target="_blank">📅 18:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134467">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahVlw0zpORZVVV4wxMWUQE2sizQBW_-ShjgSy4vtHrDTl_jZu0qPD7cq4H9qdUsrbuYhs2VTsG-41_Toet9UsannAAvmDfzm0Q6ntZeszZXJr6Yk2alq9wALxvX_D4TMyTqi5bzSwAre01LCOrRjN6W5QqFIYzYIOperAQQoMpR8yjPi6CkhLWgMTGQ08glTQi0mTG--OjObYOMv4EO8i4w5FdZtn1AD7o-l1GeFkujVDcOtVzIxS7VciZWX0EP5c25DJW_tZUQoDY4dUXmIoqvvly7tiocGvyU51oo212j9Yy28MYnHKj4JgLvcD24FHmuLL3eJM2CGYX-3KgQtog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها :باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134467" target="_blank">📅 18:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134466">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31578b475a.mp4?token=PDI-fStQVsdkKI53RAO4-K5oBZyOygfPOPZVSwR8TH9jE7ayetr_Roz5yL1lGzy4odjk6OCS5bkTbdIvoEc-zzh1MKoTSh1o9NBtAMJYMd2sweg7vVW1nLW5k5nHKF31WDiysHiTlB3TZRejrm22t2SOd_w00ByoDK14qQGF7l4Ys6g6oVCJBOFmVMWvVnMReK0F96EhHGlR887X0mnEenzJMR2wK_sSKjUoRiz1M8LpIFI-0q6mlZrQwKi5zgWvGoxOvfiFTdzFf11OLAO7ImPtSzBedaPFGyH6ig05cs7wKitQEY_ir2YNupF-ZFELYGDDPgTgkWNyGZ0diFBQc4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31578b475a.mp4?token=PDI-fStQVsdkKI53RAO4-K5oBZyOygfPOPZVSwR8TH9jE7ayetr_Roz5yL1lGzy4odjk6OCS5bkTbdIvoEc-zzh1MKoTSh1o9NBtAMJYMd2sweg7vVW1nLW5k5nHKF31WDiysHiTlB3TZRejrm22t2SOd_w00ByoDK14qQGF7l4Ys6g6oVCJBOFmVMWvVnMReK0F96EhHGlR887X0mnEenzJMR2wK_sSKjUoRiz1M8LpIFI-0q6mlZrQwKi5zgWvGoxOvfiFTdzFf11OLAO7ImPtSzBedaPFGyH6ig05cs7wKitQEY_ir2YNupF-ZFELYGDDPgTgkWNyGZ0diFBQc4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیسم قبل تورنومنت 3 جانبه با اسکوچیچ بسته بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134466" target="_blank">📅 18:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2feb948a65.webm?token=hsgjJZV1FcBH7ZrsFZMHRcPzXKT14engQNwRjfaLw8el2crqOVpgOnTP6xMPobZVWljFT1E3zJSSkAMXPAhjDBgnO0Kl06TZ7yfPeU19j4G-0i6IZWcGM6l5FGMKKBiiSawR492IyorzYI48iJZYuEzmIBm6Tq9jfra9Dru8eeX3zo6hjwBQcbCZUYmRK8xXqoFyiPMXb6NUkkwuuh7qCNu4gbWZymBkwtz9eFYs7DYpl0Yd-juY1CDqMU205U3A7VqH1we1vythVGbTsf-vkwl8VkB_qgQClQ26IqwBNbbMnSUDe5vMTzEBwInkQSi98jIJnsxiwK97dU1lZDsTzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2feb948a65.webm?token=hsgjJZV1FcBH7ZrsFZMHRcPzXKT14engQNwRjfaLw8el2crqOVpgOnTP6xMPobZVWljFT1E3zJSSkAMXPAhjDBgnO0Kl06TZ7yfPeU19j4G-0i6IZWcGM6l5FGMKKBiiSawR492IyorzYI48iJZYuEzmIBm6Tq9jfra9Dru8eeX3zo6hjwBQcbCZUYmRK8xXqoFyiPMXb6NUkkwuuh7qCNu4gbWZymBkwtz9eFYs7DYpl0Yd-juY1CDqMU205U3A7VqH1we1vythVGbTsf-vkwl8VkB_qgQClQ26IqwBNbbMnSUDe5vMTzEBwInkQSi98jIJnsxiwK97dU1lZDsTzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تلنگر
❌
❗️
پروژه بگیر ها و قالتاق ها دارن زیر پوستی حدادی رو میزنن خاستم بگم دنبال پدرتون بگردید… با تشکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134465" target="_blank">📅 17:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⚽️
فرهیختگان : پیمان حدادی دنبال این است که با  دنیل گرا و تیوی بیفوما برای جدایی این ۲ بازیکن و فسخ قراردادشون توافق کند ؛ این درحالی است که هر دو بازیکن یک فصل دیگر با باشگاه قرارداد دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134464" target="_blank">📅 17:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134463">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32365f3ed.webm?token=HcBbWToz5ysLyDI1Igvh260HUubpavQXVuDCS3cmkL-tPSfIf4oM03boWRuEOaOwh8-R12QqcfUMBDsOly9ZaJf95QZiQ-ogyfNOR7gzywEVyMaJehLfdxe2iX16ttpp-PbhEMTQHCvuWvTITzMGpRRH-4ANptMpP-1klhtUMx035vEg6U2zsDcvVZfhvcnBVB9Y5c5zmw68SOQ2zxjLi2rSJ7K2JcgT7wvje79rD-4xL77jSbNdYTzlyDGvN0Ldj1P21649n67HpCv6pBbwbLwF2cydJBcheQHWQemS_1kuOy-f09yYpNT0ZBTqrkepfKW8iBfIAfo7nUJwK1PwXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32365f3ed.webm?token=HcBbWToz5ysLyDI1Igvh260HUubpavQXVuDCS3cmkL-tPSfIf4oM03boWRuEOaOwh8-R12QqcfUMBDsOly9ZaJf95QZiQ-ogyfNOR7gzywEVyMaJehLfdxe2iX16ttpp-PbhEMTQHCvuWvTITzMGpRRH-4ANptMpP-1klhtUMx035vEg6U2zsDcvVZfhvcnBVB9Y5c5zmw68SOQ2zxjLi2rSJ7K2JcgT7wvje79rD-4xL77jSbNdYTzlyDGvN0Ldj1P21649n67HpCv6pBbwbLwF2cydJBcheQHWQemS_1kuOy-f09yYpNT0ZBTqrkepfKW8iBfIAfo7nUJwK1PwXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چراغی در مورد نقل و انتقالات نیم فصل دوم درست میگفت اینکه داره دلالی میشه</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134463" target="_blank">📅 17:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134462">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehrad</strong></div>
<div class="tg-text">چراغی در مورد نقل و انتقالات نیم فصل دوم درست میگفت اینکه داره دلالی میشه</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134462" target="_blank">📅 17:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134461">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚠️
⚽️
چه کصشر هایی که ادم نمیشنوه، هرکسی برای خودش لیست مازاد داده بیرون….چقدر تیم سرمربی و سر حاصاب دار شده ما خبر نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134461" target="_blank">📅 16:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚠️
⚽️
چه کصشر هایی که ادم نمیشنوه، هرکسی برای خودش لیست مازاد داده بیرون….چقدر تیم سرمربی و سر حاصاب دار شده ما خبر نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134460" target="_blank">📅 16:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
ابراهیم اسدی: شأن پرسپولیس حفظ نشد
🔴
🔴
پرسپولیس در حد و اندازه‌های همیشگی خود ظاهر نشد و این حذف برای هواداران قابل قبول نیست. ای کاش تصمیمات مدیریتی و فنی با دقت بیشتری اتخاذ می‌شد و تیم در مسیر بهتری قرار می‌گرفت. این سبک آسیایی شدن در شأن تیم بزرگ و پرهواداری…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134459" target="_blank">📅 16:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🤩
صحبت های پیمان حدادی بعداز بازی…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134458" target="_blank">📅 16:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134457">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtT-QksLiWQstaaHos1Vea4N2jcE8KSei1Fxhde-pJIqU8yqP2OwVNIc6WGOReIcNNt8zVsRCLjdjbddMk8wqDMLihwplT7ZALU8Sy7PZ59mQbO8iXXTViyDipVM_AEy-OYzBWmWsVN-3gaCLoSKSJu5zc5lJxyv-zDP1PyyySqWgP-EewTHtU0yn1w6ZCoLKfmI5jauVwpnWfPGB7MNvCCtYP9AaLqnDW3Tqb_HkCiSEQuHxHdW3JvbFoTF8Qi6Ny6ozyb19ptP552R7Mjjgr7gJ3wT1TE-TF8x135Exqm6o0mJf_f5jVWLh7Kk0vjXmk32RpOztOHnyafXe8vp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدارهای امشب و بامداد فردا جام‌جهانی رو در وینکوبت با بونوس ویژه پیش‌بینی کن!
⚫️
🔣
0⃣
2⃣
بونوس ویژه جام‌جهانی روی هر واریز برای تمامی کاربران!
🎁
تا پایان مرحله گروهی جام‌جهانی روی تمامی واریزها
🔣
0⃣
2⃣
بونوس بگیر و فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا پایان مرحله گروهی جام‌جهانی فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134457" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ascAvNVyiGT_9h3iwFk6SQucQs4hDY8ymmyuPImt0z9_UWyrVhv6twqe1Yo4V6mzW93KiD2j5mNNFOsGeu5jxl6epj5-RYC0zLq3GahhZwkNhWhjXJ6pbSMUGm0UDP41ZJ3UY2d1W4uyfW_qfyuGEuKJR365qxZkety2Wm085ByQwicOOSxlBBn-E_tKpuK1NY19ipi766bxghWKKU0YxhTHLZ0JMepmmImOvaTTWAU5qer2DANPF9Yoc_t8pu22Vf2af4_ecVW2PCa-9S5uR69vXowHAGS--j-He43Enfv-hn7ykoca1HAK-Joo_wQE3NnOQvYH68_WBRek5VULOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134456" target="_blank">📅 13:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134454">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B80-UgatMSgAN1ERFlwYDY4Ia7d7hqUGxeBnocwXlu5hr0emcC7Q6ngfruF64nTWVaMmoRSnJJg8uAn_qsbfiOVnCBvvNMPKeLnvm8yV8-0_d6iYqP8EentizvsVL8S3k1HVH-EhfwCq4wGt8HsNsLPl9j7IwPiQYoKXuo8nXJcZpM9FsTntn2qn5wJedfSyLd0FESUa8tiKxd3juzuszTVUq5MESwUXZFLEYmF3R7nUMueL4FJCefFntyOL3-ylKkSKdY_42q2K2HckEpBpFN3wE2CE2DJxZTtSP_0JD3BHSF7QfmjHCN2nk6gJ2C8Z8KJMNUUvx8auXXcCt4ZsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رامین رضاییان بعد از وینیسیوس جونیور بیشترین جایزه‌ (بهترین بازیکن زمین) در این جام‌ جهانی را گرفته است. همچنین رامین رضاییان با گلی که امروز زد، به کافو اسطوره برزیل رسید و با 3 گل، گلزن ترین دفاع راست تاریخ جام جهانی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134454" target="_blank">📅 13:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134453">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/134453" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134452">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIqRXXMkWOMYePOABFQk91gSGAPnlutdYh-SVl1x8dUBgC8oFAw4TJxRbkK3l-0qHh6hg2-jjkuGgY40ukmT2vuND_433vnpZpyOE6DIf7bUcz1J5t6xnJQMIYWJqSJZPYG_moYcAg59xvYrLAPBTQrbYArZCY5tFYr3xpPVD6BZ5Mxk8x-VCfa7LZxzvubB7JVupQF3vaI5AwB8byVoXMYH8bBPAq-h9a-1stKLnsJemXiyF8DReMeniqK_lRCAiiDhxjN-vLEtVVgJae8_1JkWCjHtyiqPPosLpoTfSPSvZlLilnv0MLycU1gyb4LVs4ONyi7b-pOI0edxJ6oqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کی‌روش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتوانیم کرواسی را متوقف کنیم تا ایران به دور بعدی جام جهانی راه پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/134452" target="_blank">📅 13:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134451">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
همین امشب نصف تیم و بیرون کنید و برای آقای اوسمار پست خداحافظی بزارید ....به تیمی باختیم که پنج ماه تمرین نکرده و با تیم امید اومده بود ...لیاقت سطح دو رفتن هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134451" target="_blank">📅 12:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134450">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTJHmYCj1sv0TTzVT-EpJLEI3FGKAciwujO0CMUSqgwoDMnv55x8jpaUCFH_3af4nhvX-csQY7Vcg2t-vxzXjqVlAOLT5JBCM1AyW_0XHkEoaj754vRWDd_FmCmkTQT9b8VHcbO-JbXhcVXbo9sq86o9jMN9Uko7hbAzP3gxy3e7VIeavxXRS4gVzVyq6R9pyCBj86LbMYdW0-voXXm0t7bqD4_0FRLrhduUJkUZ4Rn5mF7-PGCS0-vMr8R2Xswx9-NHpDIeSoYeF92hPspSmI8dekussHLe0qy8DFyAWt_mKMKiOTF4G8oa2NtWwE9Bp6RtImB-NOCbU1uu-gND5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملاقات مهدی مهدوی کیا واینفانتینو درحاشیه دیدار ایران
⚔️
مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134450" target="_blank">📅 11:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134449">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
فقط کافیه بازی امشب اتریش و الجزایر مساوی نشه ..ایران صعود می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134449" target="_blank">📅 11:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134448">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhmBK72F1UoxPe546GeHNj5u_eXMzr4AMz35EggaDe410xZuegWisTGxQXwdzY5Rh99OrDoAFblWsj89fx7d8m06jbIp2pGaGwcOnvQPfHZqUyM5NFkR0as4uiIa_yYx_0ZQ9hGg-9yEocZT1fbywTzwK5YMFlKC-JAiXktAHeT_p8NtdwKHKSer-o9IwF92rnRgi0yL2wC4BrJkI5mOd8z9grAc9dUVRUFK78IzWDxaRIuCU9OQHx3pt_ecaHnQjvfKPDp6QRPtJyyxNFanPvcbZ1x1Jj2WTFaDZdK0uPi7YbVm5H1Kjzsf_krusrr0no7u3SqDsD9BznS00gGevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134448" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134447">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c8df3c29.mp4?token=YbXJr7pDUjEu0BHFNONDjlMXxzLVyPAr4jmNU2FZAKu5n2tu66gMpgw0BCPsqD-Vkrut2oWT9QS1kHkMMAO8MzeRMPMECK0HxThwWIkq6FH6x9XR0CDpzoPYwQ8EzNBfQK_jCEDh9-A-e0ZDBwURrxL2UtJZONyvxik7zljTW7Wq-17iUqhYoE0cxSiqcMvaoaYO3xK8b4-tXQjVLfiV6zcBQCmnOeMxp1yznpQZyWnJBA9kjHMc96eCXxiChUHnNw_DPHUZujzTKgW_BXOcLjoGQdmsRaKN5vyyZFMHyAiIzj7HqQcFjzw0EK_vrrRh1n4O9W40JgmJrPBwm-380rz9hdGlKKV5ScVTbmzRWjgrX1I3zUpEn5RlsiUWrZ9mmZfjOkn2fGDIYMqxS-JdrmT954VLcldmIdrF8P8oedwb1h7b4wj4Bv-fGvlfJ0-3WMlZrapSSsAQXV8ibPvEvYPQehfrOqAuhfhKFr5T9slkmyRSdPG4qzmQsqNmE5j8ZxFfMXL66Sj1j5xWDc7RRnRMUETUkvos87PFDBSNqDjIFxF_Dwh1cVDSdm_W2ey3QN6tPDo8LlJPdC8Lb0d8RGxFlPOv19gJclEddRfwZJ_wf0Nr0eb5Ei1qd6z6z04RugZhArABJvUrc1FtX4DZ5OKKKku3DXEqYAQDMzzyLas" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c8df3c29.mp4?token=YbXJr7pDUjEu0BHFNONDjlMXxzLVyPAr4jmNU2FZAKu5n2tu66gMpgw0BCPsqD-Vkrut2oWT9QS1kHkMMAO8MzeRMPMECK0HxThwWIkq6FH6x9XR0CDpzoPYwQ8EzNBfQK_jCEDh9-A-e0ZDBwURrxL2UtJZONyvxik7zljTW7Wq-17iUqhYoE0cxSiqcMvaoaYO3xK8b4-tXQjVLfiV6zcBQCmnOeMxp1yznpQZyWnJBA9kjHMc96eCXxiChUHnNw_DPHUZujzTKgW_BXOcLjoGQdmsRaKN5vyyZFMHyAiIzj7HqQcFjzw0EK_vrrRh1n4O9W40JgmJrPBwm-380rz9hdGlKKV5ScVTbmzRWjgrX1I3zUpEn5RlsiUWrZ9mmZfjOkn2fGDIYMqxS-JdrmT954VLcldmIdrF8P8oedwb1h7b4wj4Bv-fGvlfJ0-3WMlZrapSSsAQXV8ibPvEvYPQehfrOqAuhfhKFr5T9slkmyRSdPG4qzmQsqNmE5j8ZxFfMXL66Sj1j5xWDc7RRnRMUETUkvos87PFDBSNqDjIFxF_Dwh1cVDSdm_W2ey3QN6tPDo8LlJPdC8Lb0d8RGxFlPOv19gJclEddRfwZJ_wf0Nr0eb5Ei1qd6z6z04RugZhArABJvUrc1FtX4DZ5OKKKku3DXEqYAQDMzzyLas" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
واکنش مجری شبکه پرسپولیس بعد از گل دوم چادرملو و شکست قرمز پوشان در پلی آف لیگ قهرمانان آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134447" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134446">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrIkbYHbe_aUkgjWwwIfNkZkw_fGgZlxwNW-6V3JhweRh9EKzQHrmUhjIwAQiiQt257bzUB5PEMswG6y6a2ojvpr1abcxQyh0Q4LGKdQcligVoXTzJYZgKTt0c1qjRBADbRlj4MuJTXQgW8XTHK5xZJwSGn8cGysNaddxNiDHkWYIk-Bs3AVfPsscQTjN6qe8X0xGda5DqhtpUCWMiZ6XJvPVjFKKnU3tzSW_P3GvfmUMdbDobxWM2p_AhoEYE3vCfkrEKAv4RPtsmpw8EmEgk28gqMJwHJyaf8rKD62tRYAhHZmOmUQba0FJ17eMvHzoutcjpaAKdthZL011gAPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا منصفانه است، خب اوکی، خوش به حالشان!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134446" target="_blank">📅 11:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134445">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134445" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134444">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134444" target="_blank">📅 11:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134443">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNrySZ4_Gy9-AU_uHI35kx1smULkEy6m7_wV8tJiV1qmPs3VXdeJWs6ZWfPDZ1vi19jE7ikten1EdRORoJMLlMdyDyny_RudHL2VBPkEIJ0EUTaNoAB4LqT_RgbMlowlA2a81Yq3HWX-ETAY5JNLJzOOKKqxrCcu7NLqnKl9Ets9cI3QDYU94nU3_EyqkhEg5kq4AKcmA0-vw8lpLjAUIKC373OCMkUc6MvtI6FnZPkd6426nKWOkcKG1lM3q4UiCY6ZZ_mvquTrK3K5FYFIrae7Dte9oU1yrwx6pHSC0PKL7Xa44ZLW9TCDMIYg72rfdqh5PxFr4rL1uMR0eO4g_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
دلیل اینکه گل شجاع افساید شد
✅
طبق قانون موقعیت آفساید بر اساس «دومین بازیکن آخر تیم مدافع» تعیین میشه
🔴
در این صحنه بازیکن آبی آخرین مدافع حساب میشه و بازیکن زرد مدافع دوم حساب میشه
🔴
دروازه بان در قانون آفساید نقشی نداره و جز مدافعان اخر حساب میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134443" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134442">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
فووووری از فرهیختگان: تا هفته اینده اسکوچیچ برای مذاکرات پیشرفته و بستن قرارداد با پرسپولیس میره تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134442" target="_blank">📅 10:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134441">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
امیر قلعه نویی بعد از تساوی ایران و مصر:
🔴
🔴
شاید خدا هم با ما سر ناسازگاری دارد. با یک موقعیت گل نزدیم. می گویند گل ما هم با 5 سانت آفساید گرفته شد. تیم مصر تیم بسیار بزرگی است ولی عدالت فوتبال با همه مشکلات ما رعایت نشد. شاید این آزمایش خداوند از من است…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134441" target="_blank">📅 10:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134440">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134440" target="_blank">📅 10:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134439">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
سوژه شدی رفت شجاع جون
🍇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134439" target="_blank">📅 10:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134438">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134438" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134437">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
فووووری از فرهیختگان: تا هفته اینده اسکوچیچ برای مذاکرات پیشرفته و بستن قرارداد با پرسپولیس میره تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/134437" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134436">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
مهدی طارمی یکی از حساس‌ترین پنالتی های تاریخ فوتبال ایران رو خراب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/134436" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134435">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57704b3690.mp4?token=ODvhjyVOYcsPMrrWEwuecG57107maGJ9RrACElOXEd3N9m2XIJHIbZ78y8Qi5S1zX-ga1YNWUAOUv7gMoZxi2V6njINb75dtTUphJepX70z1cGL0cqt3Cwj46LsJKIa43rPg1r0FSomyri2KEcjfBjb0P-rYLoNIY6sHUJ1zefumCDbMaw89Cgf7-RxGPDrtFnQZpj7kChlUnYLbLcTGzkMpMO4Vexc5LyiQT8n5u7O5MQy4LLtrhlmQpwOaqkv58lbyBAS1qyV3AwbrEnX05wPvQtrNdOAuoD04-HMHGDYeD6GQ3kB_epQ7YmlQ7UkIydN4mOOUSZLZT9boSvqTcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57704b3690.mp4?token=ODvhjyVOYcsPMrrWEwuecG57107maGJ9RrACElOXEd3N9m2XIJHIbZ78y8Qi5S1zX-ga1YNWUAOUv7gMoZxi2V6njINb75dtTUphJepX70z1cGL0cqt3Cwj46LsJKIa43rPg1r0FSomyri2KEcjfBjb0P-rYLoNIY6sHUJ1zefumCDbMaw89Cgf7-RxGPDrtFnQZpj7kChlUnYLbLcTGzkMpMO4Vexc5LyiQT8n5u7O5MQy4LLtrhlmQpwOaqkv58lbyBAS1qyV3AwbrEnX05wPvQtrNdOAuoD04-HMHGDYeD6GQ3kB_epQ7YmlQ7UkIydN4mOOUSZLZT9boSvqTcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
قلعه نویی:
اینم یه آزمایشیه، شاید خدا داره منو میکنه.
😱
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134435" target="_blank">📅 09:35 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
