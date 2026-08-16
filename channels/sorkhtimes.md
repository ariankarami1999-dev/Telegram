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
<img src="https://cdn4.telesco.pe/file/ZyQ-8UIjjarU2Dpxih-D7j1gGTPTuTe6Fuhg8MCLkiZ0GIikuuPjQsAmEM7YeOJqqRQ63sgLxqAIR7HbjJ3P79a17iStAv1RPfDiKsaA59qiB5Rfo4MUYNSGuwOH7IP90cm53dE58GZPXOCSgnNB1S9Uxqe4BS2EpyINrsIDr35knl3zNzGy_MOz-lYGihIdLMZCOmsoZDN5BCDYFdT52PeEkjsa7URGXgRfds5b4hNlCo7Ftvpv-glw16Jc2ancNiwuTMxPyJk-LuPP1AXk6WLQuzWb44jxU_DwdGFLAfmiySV7op_wy2RT8hN1Y5QSKQvwIx88wjR0M36h2EraKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 05:46:37</div>
<hr>

<div class="tg-post" id="msg-138295">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDjZe5ZGP7C5FguUjan5IxtxpFgAE5dG5ELvJQwF5IL8c0zwBLO5KMYFF6a59RPe2xl2m_1yoLTQPpY99tfeSlcpX-OnD8UNjdbQ-krJ3gK1JO0jRekeLAYjCQZAtRp6reKpF-fH-Ib7r4BR0iBRyHEQPBkwqBHyrX67EhXwZMTPDeRVB9q4yDfb2E_ty1rbaqPlxqrGsqxiKSB3y79sMuzCxD3zYVwBo0XoX0ByvsJoMXAB1nlOoFfCWe1Up8Y6tD8DtE8vkShl65PTEWE9SK9ZZJju1DnGbIfTEFvPyS2erIAC2lfOCMoVacbFqKOKuetsSUtInW8SyuoWPdUqMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نبرد غول‌ها برای اولین جام فصل؛ جایی برای اشتباه نیست!
آرسنال با فشار و پرس مقابل سیتیِ باتجربه؛ نبردی که جزئیات تاکتیکی می‌تواند برنده را تعیین کند.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فینال
سوپرکاپ انگلیس
[
آرسنال
⚽️
🆚
⚽️
منچسترسیتی
]
⏰
یکشنبه ساعت ۱۷:۳۰
🏟
استادیوم پرینسیپالیتی
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/SorkhTimes/138295" target="_blank">📅 01:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138294">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
انتقال محمد قربانی به پرسپولیس کنسل نشده و هنوز احتمال نهایی شدن این انتقال وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/138294" target="_blank">📅 00:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138293">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
زارع هم تو دفاع خوب بود ...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/138293" target="_blank">📅 00:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138292">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/138292" target="_blank">📅 00:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138291">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/138291" target="_blank">📅 00:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138290">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
با اعلام تارتار دانیال ایری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/138290" target="_blank">📅 00:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138289">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
ترامپ به فاکس نیوز: به‌ایران از لحاظ اقتصادی ضربه شدید خواهیم زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/138289" target="_blank">📅 23:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138288">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
مهدی تارتار: یکی دو بازیکن دیگر میخواهم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/138288" target="_blank">📅 23:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138287">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔄
🔄
تارتار:
✅
شمس‌آذر نیمه دوم بهتر بود/ باید از بلندی چمن گلایه کنم چراکه باعث خستگی و مصدومیت بازیکنان ما شد  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/138287" target="_blank">📅 23:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138286">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⚡️
حمید مطهری، سرمربی فولاد: رامین بازیکن مورد علاقه من است و می‌دانم چگونه از او بازی بگیرم‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/138286" target="_blank">📅 23:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138285">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/138285" target="_blank">📅 23:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138284">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
زهره فلاح زاده خبرنگار حوزه استقلال: هنوز استعلام سازمان لیگ از فیفا نرسیده و مدیران باشگاه استقلال با بازی دادن آسانی در بازی دیشب ریسک بزرگی کردن و اگه جواب استعلام مثبت نباشه بازی دیشب استقلال و مس شهر بابک سه بر صفر میشه
😂
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/138284" target="_blank">📅 23:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138283">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWXgLsQksusLMVJbM01NSz8CB69mNRAQE7YAHGYaxFcjQZd-3fxmSmjWs5fahKYGboQwVEC58jRvM5dU5Vwu83n2Yqm85urUPJ22PbII4hVHj0N1nA3XwMeQWDusEY5A9lDwRoYb3ULqytpqTnCRoEvL7MRdZwLuh2wHFZBt4PONatK758len_L-BYTZJcgrZmTIptbQs5JPg3Wlz7IY-DqIt-BeoNu5qWpfM9QulV3q5TvNSMSwvLmvcelhHGXsj1LiTghiKeoQNZQbCgG2sNEq3ltR1hzMP-eMoAjIQpwYwFexCgwf2-MHUqxJAy4n7YS_Y1v7RTA6aO-Qu_GyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚽️
بااعلام‌باشگاه پرسپولیس؛ مصدومیت ابوالفضل جلالی جدی نیست و این بازیکن مشکلی برای دیدار هفته آینده مقابل استقلال خوزستان ندارد. جلالی امروز بازی  درخشانی در ترکیب سرخ‌ها داشت.
سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/138283" target="_blank">📅 23:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138282">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔽
🔼
بازیکنی که امروز اصلا بازیش به چشمم نیومد عیدی بود، بنظرم باشگاه باید با جدیت سراغ رامین رضاییان بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/138282" target="_blank">📅 23:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
⚠️
امیر علی‌اکبری در مقابل علیخان واخایف از روسیه ناک اوت شد. واخایف با این پیروزی، کمربند قهرمانی سنگین وزن در سازمان روسی ACA را حفظ کرد.
سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/138281" target="_blank">📅 23:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d1929df98.mp4?token=XDe2a0j1QdBAcegQrxpct0qAcDTWFKeV45jP4xw_nMQPd2K53KpLYNiqxsRHtFhBFM5FewD9NqCNsFbL2b1z-PSMm7OWb8RO1km7J9vUY9XMl9FBHQ-4naR_6NLFz4Mhdf0I-9pNo-LDAN0w_xP1rs7XwHClwwHXYvw8ZUKBOZ8DZLiROIK7pgeKCv1spUcDnvObhGRbC3cKhRDZjNilZ4h1R6jGnfMb07-flH15FU2CGfElreFrStW4udVww4HtqyPKYe1IJGQF8OIcVL2bWxIqMIV-Tc5BcBncRFw2N-7gyos-OK4w0qcCtFTyjj5qzlKNfInJHVup8wpfnIiPRB8QDtRk8vtaQVlSlF6GDgfP3M0LBX0DqQAHnlNd5ZMMi43TrK2hu1ln_JsIWGWIEcWLdgsyRJSK-biKr_1vG4cgLKLiWyKzGbbE54i6CNhYxY6BkjxN1ngKv3wl2vuLjmt8x3I2v3uk-gdzYY76Bic5YikG34J9NhJUrQjTlgkWsHLjUEcA-aXHlxiBnefeSzlXnt2T24UBwpNb-FRRKM-YTzdgLw4-5BzwMUpCzGQu1DJMu1-SjaX97fFAvIqj5USOoVqF7ihWpClFvcaJW0ybTZbynabrZNZLrMYAd_7FuHn0LD-MKHAqAbv_BUcW4PwnL67fXsP2gER8qkIvqyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d1929df98.mp4?token=XDe2a0j1QdBAcegQrxpct0qAcDTWFKeV45jP4xw_nMQPd2K53KpLYNiqxsRHtFhBFM5FewD9NqCNsFbL2b1z-PSMm7OWb8RO1km7J9vUY9XMl9FBHQ-4naR_6NLFz4Mhdf0I-9pNo-LDAN0w_xP1rs7XwHClwwHXYvw8ZUKBOZ8DZLiROIK7pgeKCv1spUcDnvObhGRbC3cKhRDZjNilZ4h1R6jGnfMb07-flH15FU2CGfElreFrStW4udVww4HtqyPKYe1IJGQF8OIcVL2bWxIqMIV-Tc5BcBncRFw2N-7gyos-OK4w0qcCtFTyjj5qzlKNfInJHVup8wpfnIiPRB8QDtRk8vtaQVlSlF6GDgfP3M0LBX0DqQAHnlNd5ZMMi43TrK2hu1ln_JsIWGWIEcWLdgsyRJSK-biKr_1vG4cgLKLiWyKzGbbE54i6CNhYxY6BkjxN1ngKv3wl2vuLjmt8x3I2v3uk-gdzYY76Bic5YikG34J9NhJUrQjTlgkWsHLjUEcA-aXHlxiBnefeSzlXnt2T24UBwpNb-FRRKM-YTzdgLw4-5BzwMUpCzGQu1DJMu1-SjaX97fFAvIqj5USOoVqF7ihWpClFvcaJW0ybTZbynabrZNZLrMYAd_7FuHn0LD-MKHAqAbv_BUcW4PwnL67fXsP2gER8qkIvqyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واکنش کنعانی زادگان به شایعه قهر اورونوف
⚡️
حسین کنعانی :
اوستون پایان‌بازی برای هواداران دست تکون داد و اصلا چنین چیزی در تیم  ما نیست که یک‌بازیکن بخواهد قیافه بگیرد یا بگوید حق من است که بازی کنم‌ در پرسپولیس بازیکن چه یک دقیقه بازی کند چه نود دقیقه از دل و جان مایه میگذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/138280" target="_blank">📅 23:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔖
❤️
من از این تیم تمام قد حمایت میکنم،انتقاد سازنده باید باشه، حمایت باید باشه هوادار حق داره نظر بده و انتقاد کنه، ما باید روز به روز پیشرفت کنیم بازم خسته نباشید میگیم به تمام بازیکنان و کادرفنی آقای حدادی که واقعا زحمت کشیدن
❌
این تیم خیلی پتانسیل داره،جوان های خیلی خوبی جذب کردیم و تو آکادمی مون داریم، من خوشبینم امیدوارم بازی های زیبایی از این تیم ببینیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/138279" target="_blank">📅 23:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دلیلش تفکر مسخره مربی ایرانی که تا یه گل میزنن با ک و ن میرن تو دفاع و تعویض های اشتباه مربی وقتی بجای بیفوما ابرقویی میاد تو انتظار داری حمله کنیم؟؟؟ اصلا چه نیازی بود تغییر سیستم بدیم  به ۳۵۲؟؟؟ میتونست جای بیفوما ارونوف رو بیاره ببینم بازم دفاع شمس اذر…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/138278" target="_blank">📅 23:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138277">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">دلیلش تفکر مسخره مربی ایرانی که تا یه گل میزنن با ک و ن میرن تو دفاع و تعویض های اشتباه مربی وقتی بجای بیفوما ابرقویی میاد تو انتظار داری حمله کنیم؟؟؟ اصلا چه نیازی بود تغییر سیستم بدیم  به ۳۵۲؟؟؟ میتونست جای بیفوما ارونوف رو بیاره ببینم بازم دفاع شمس اذر جرات داره بیاد جلو</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/138277" target="_blank">📅 23:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138276">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromF_baj</strong></div>
<div class="tg-text">مگه گل گهره دفاع کنه</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/138276" target="_blank">📅 23:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138275">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">میخواد با ۱۱ تا دفاعم بازی کنه فقط باید امتیاز بگیره</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/138275" target="_blank">📅 23:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138274">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاَمیر</strong></div>
<div class="tg-text">میخواد با ۱۱ تا دفاعم بازی کنه فقط باید امتیاز بگیره</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/138274" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138273">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
تنها چیزی که درک نکردم این بود چرا نیمه دوم تا این حد عقب کشید تیم وقتی از همه لحاظ و مهره ای سوار بازی بودیم، درسته بازی اوله سه امتیاز مهمه و شمس آذر روی کناره ها خطرناکه اما اینکه شما توپو بدی به حریف بشینی عقب خیلی خطر گل خوردن بیشتره، شمس آذر نیمه اول…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/138273" target="_blank">📅 23:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138272">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
تنها چیزی که درک نکردم این بود چرا نیمه دوم تا این حد عقب کشید تیم وقتی از همه لحاظ و مهره ای سوار بازی بودیم، درسته بازی اوله سه امتیاز مهمه و شمس آذر روی کناره ها خطرناکه اما اینکه شما توپو بدی به حریف بشینی عقب خیلی خطر گل خوردن بیشتره، شمس آذر نیمه اول به زور سه تا موقعیت داشت، نیمه دوم راحت تا جلو دروازه ما میومدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/138272" target="_blank">📅 22:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138271">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔽
🔼
بازیکنی که امروز اصلا بازیش به چشمم نیومد عیدی بود، بنظرم باشگاه باید با جدیت سراغ رامین رضاییان بره…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/138271" target="_blank">📅 22:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138270">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">➕
در کل باید از این تیم و مجموعه حمایت کرد، همدلی باشه هر غیر ممکنی هم ممکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/138270" target="_blank">📅 22:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138268">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📊
تیم واقعا امروز شاداب بود، هفته اول بوده نمیشه هنوز با قاطعیت گفت ولی چشم پوشی هم نمیشه کرد امروز واقعا خوب بودیم،خیلی وقتا بازی هارو بردیم ولی اون پرسپولیسی که باید میبودیم نبودیم، این تیم اگر به همین روال ادامه بده و بازی که نیمه اول به نمایش گذاشت تو همه بازی ها به نمایش بزاره من امیدوارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/138268" target="_blank">📅 22:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138267">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🏅
این اولین بازی بود بعد از یک سال اندی که من کامل تماشا کردم، طی دو سال اخیر اکثرا خوابم میبرد پای تلویزیون…
😬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/138267" target="_blank">📅 22:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138266">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭕
این تیم به عقیده من بوی قهرمانی میده،همه خرید هامون عملکرد واقعا خوبی از خودشون نشون دادن و بنظرم ارزشش رو داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/138266" target="_blank">📅 22:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138265">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEjV2hVaz7UnZgZtnnoE3j6A0MrgFRAbjVTb0mEG72EwYtB44hjBFwBkSFWhD6Y2ptUFAnOmBehnxs4CiKXBbsNVoIv82sznT5gQ9Z4Eavuuea4rIjiFVShOd8b0oS9i6l-5BIuvwFoAHHVKl7RdhZPYMYAXnGFQ_yeyWjYSy4cO6X-TTIqvc0P4ckqU6iAebxMGO3Fw3X1oOtEkaIu-dEeBvBUw6mAaTBeG9B6FUGsfem5qkSjiWYtAUR_pd5u8SEE-TJRIm7KYsiISezDlqUDRB0NFHsgvYA_FngtVyeWifm1sD5EIY_i_zgdDW3mXFf77hhixJ8QETaZJF1GKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
برنامه هفته دوم لیگ برتر
سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/138265" target="_blank">📅 22:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138264">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
✅
مهدی تارتار، سرمربی تیم پرسپولیس: هیچ قولی برای قهرمانی نمی‌دهیم، اما هدفمان کاملاً مشخص است و برای رسیدن به قهرمانی تا آخرین روز تلاش خواهیم کرد. از هواداران می‌خواهم صبور باشند و از تیم حمایت کنند.
❌
هنوز کار ما در نقل‌وانتقالات به طور کامل تمام نشده…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/138264" target="_blank">📅 22:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138263">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔄
🔄
تارتار:
✅
شمس‌آذر نیمه دوم بهتر بود/ باید از بلندی چمن گلایه کنم چراکه باعث خستگی و مصدومیت بازیکنان ما شد  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/138263" target="_blank">📅 22:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138262">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔄
🔄
تارتار:
✅
شمس‌آذر نیمه دوم بهتر بود/ باید از بلندی چمن گلایه کنم چراکه باعث خستگی و مصدومیت بازیکنان ما شد  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/138262" target="_blank">📅 22:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138261">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
تارتار: در نیمه اول پرسپولیسی بودیم که خودم دوست دارم؛ تهاجمی و جنگنده/ در نیمه دوم شمس‌آذر تیم بهتری بود  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/138261" target="_blank">📅 22:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138260">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🇮🇷
🎙
واکنش تارتار به ناراحتی اورونوف: برای من دیسیپلین بازی و تیم بودن مهم هست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/138260" target="_blank">📅 22:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138259">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3867654e00.mp4?token=c2erhICy94qDkBxk3pgbG23Bwi_End8MdtgeSr4ZUEHlnRIoDW7a3kZkRjr7wXvW7lLJWgwzy44xOS774iAHgUA9yXai3c-3TZ7wnntIwUHRLHPQE8dI6BoQV0EW5d0MBEkUzxE_5mbOtRhUXG3ddqsWAjzL4Syfu10xxGuD3DYrMUumd0-BI_-pAg48-4uzEg0RDcvNy2T0hsMXFZ05JkOt9U_sDPliveSzoinKPCgx051dKZIQFlTLGs4Zv8xh204ZUhqrzMe_pA2mHLAFiD90yzZcdDHX5yrTrbXCcik45oPAR3UE6-2Id5WHoGntPfOkjS8Ul1X7hhLCNvPr2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3867654e00.mp4?token=c2erhICy94qDkBxk3pgbG23Bwi_End8MdtgeSr4ZUEHlnRIoDW7a3kZkRjr7wXvW7lLJWgwzy44xOS774iAHgUA9yXai3c-3TZ7wnntIwUHRLHPQE8dI6BoQV0EW5d0MBEkUzxE_5mbOtRhUXG3ddqsWAjzL4Syfu10xxGuD3DYrMUumd0-BI_-pAg48-4uzEg0RDcvNy2T0hsMXFZ05JkOt9U_sDPliveSzoinKPCgx051dKZIQFlTLGs4Zv8xh204ZUhqrzMe_pA2mHLAFiD90yzZcdDHX5yrTrbXCcik45oPAR3UE6-2Id5WHoGntPfOkjS8Ul1X7hhLCNvPr2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
واکنش تارتار به ناراحتی اورونوف: برای من دیسیپلین بازی و تیم بودن مهم هست.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/138259" target="_blank">📅 22:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138258">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
به نظر می رسد در فصل جدید گرا، باکیچ و سرگیف فرصت بازی کمی خواهند داشت. مراقب باشید سهمیه خارجی نسوزد.//بزرگ نیا   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/138258" target="_blank">📅 22:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138257">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1930bdf6.mp4?token=K3I32x_0rKhF1iWzwSjIRFwNvmOhtdTpdxXKblKEo-HqzlaxlQooumNzyMxOCJpxy2xw_RHeNxDhXFPVgV_4q-K7uz4P9vc9cFstyW2J2uOdSj6hst1Kt_daScgi5sZuCXSF3--05sjVldJYLhdcHS7_htxE8m4asDrEOuBJM5lpGujxltyO5n5TpWlczpdWijxOAzt0dBetC0Y9gg_G_tFroXJe-DQ1bGdUfKVeB9qW8uOo6zkO_meCymsp9V5rz8dUmAjFWxF00xVfT1B-T3og7wpI6sclsXbRi86ZUyE_YM53Zln_tremDW3-R29GOxkv6eHk8ZMBnv0rWeTiqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1930bdf6.mp4?token=K3I32x_0rKhF1iWzwSjIRFwNvmOhtdTpdxXKblKEo-HqzlaxlQooumNzyMxOCJpxy2xw_RHeNxDhXFPVgV_4q-K7uz4P9vc9cFstyW2J2uOdSj6hst1Kt_daScgi5sZuCXSF3--05sjVldJYLhdcHS7_htxE8m4asDrEOuBJM5lpGujxltyO5n5TpWlczpdWijxOAzt0dBetC0Y9gg_G_tFroXJe-DQ1bGdUfKVeB9qW8uOo6zkO_meCymsp9V5rz8dUmAjFWxF00xVfT1B-T3og7wpI6sclsXbRi86ZUyE_YM53Zln_tremDW3-R29GOxkv6eHk8ZMBnv0rWeTiqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
🔴
تشویق ایسلندی پرسپولیسی‌ها و هوادارانشان با رهبری محمدحسین کنعانی‌زادگان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/138257" target="_blank">📅 22:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138256">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQcwNXffOiXPXJOxxU4fhtIzzGU_lnU-lKdmF_OKE9FjLRZ1QuMGDp4hDk8oD2zi8mIL3K72rln0AEenc2ZkW2C3MKH331feg0iVxgLLMPBeOHuRBPEdz35EnPPeVzmo4z2mL6ahOb7Jp5sCnSm3PxmSspNG3XO4XRq6JWjPDVGCw3dUEiBZXoHGO0KhESbMTqn4lPebk0ddwvXhwunKzCeHuuScrMLnYGRzQ2vJYFG6WmhdLbK-BuiDUDQlYmp72QaDBHAMp_UgKtKe2mIHgpuLHq0VDRA25tC5iznB7VvwHqDVEeFasMqfa-zfVn_-Z0SUVIxoTeJ8-P9EgL0_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محمد مهدی محبی، محمد عمری و پوریا پورعلی به‌ ترتیب با نمرات 8.4، 8.1 و 7.9 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس - شمس آذر بودند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138256" target="_blank">📅 21:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138255">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✖️
✖️
واقعا بازیکن بد نداشته امروز پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138255" target="_blank">📅 21:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138254">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
دکتر پیمان هنوز مونده تو استودیو فوتبال و تکون نخورده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138254" target="_blank">📅 21:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138253">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
دکتر پیمان هنوز مونده تو استودیو فوتبال و تکون نخورده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138253" target="_blank">📅 21:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138252">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✖️
✖️
واقعا بازیکن بد نداشته امروز پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138252" target="_blank">📅 21:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✖️
✖️
واقعا بازیکن بد نداشته امروز پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138251" target="_blank">📅 21:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138250">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
بریم برای نیمه دوم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138250" target="_blank">📅 21:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138249">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
نیمه دوم هر کی بیاریم داخل..‌ بازی و در میاره راحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138249" target="_blank">📅 21:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138247">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF4tgCNN6qAiW0oNr1NFWDkuZig4h0Kdr719K8NdqIRfL6wchIp82s1ENaI1uLTkwJMuO7jxi1yRx4lx0Rp08qanLWRJecY9srBmGs8jGHcrBepDUA_tqWiA2Yvi56YMUrCNqt3dvkilZLFKX1ErmmlCgpXPTF5zWC2UmQUneKsYe2ITnyedT0k5k_bERDdvGJPQbPnvclr0ruexY0uqlBYZQiAfvTPmYD83NWNFL4E2mfEkbBhr0YJlPq7Zr21lsmSVVouhd_fQPlDfVLMpNuTcddPluBb2qMha4xJoTHTQ5HcS5j0BaU7syxTzqgHQZ9JbFzha2lSeHm4K21g6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرسپولیس؛ آماده برای شکار شمس‌آذر!
🔴
Persepolis -
🟢
ShamsAzar
🔵
لیگ خلیج فارس
⏰
شنبه ساعت ۱۹:۳۰
🏟
استادیوم سردار آزادگان
📌
فقط تماشاگر نباش؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/138247" target="_blank">📅 20:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138246">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هواداران اگه امسال قهرمانی می‌خوایم برین پست آخر پیج بانک شهر و پست آخر پیج پرسپولیس :
👈
جذب محمد قربانی
👈
اخراج اینانلو
👈
اخراج احد میرزایی  ( اینانلو و میرزایی ۲ مهره ضد پرسپولیسی هستند که مانع تقویت پرسپولیس می‌شوند و حضورشون سم مطلق است )</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138246" target="_blank">📅 20:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138245">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
دکتر پیمان هنوز مونده تو استودیو فوتبال و تکون نخورده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138245" target="_blank">📅 20:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
پیمان حدادی: در حال مذاکره برای جذب محمد قربانی هستیم و برای جذبش دغدغه مالی نداریم ولی بعید می‌دونم الوحده فروشنده باشه چون هنوز قیمت ندادن و شاید قربانی تمدید کنه!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/138244" target="_blank">📅 20:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736ad661da.mp4?token=GVK1tHUlX_1ILO-0xXqlddJMMB0GfUDJA7r1_mAKP2TiB_wyV1sRNDK701KqphzDaVq_oYVIDn83qVq3vEwDDK5gXS9Ch-pTWvxsSGAxSR87RG094-Erzxaha9t-CkAvn4Z03Kri4ObswzDQix2IyOKWzSl3imVOTzdhdVgmKXDGxwl2kuHfUF_MSyQ35FRE0hCUS6XD_JtPo9CH2PWONzcDuTzTGKv-ukgmR8MTM30BNokfxChjlLQFEBnBwKkkYxIiBORbfUbhZsfmXgzOWMuD8KPsgh-ZIsfAroVrxNeymbbMNaSwem2LYu1dC8Shvaa8RxM5RrZiS12j8llJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736ad661da.mp4?token=GVK1tHUlX_1ILO-0xXqlddJMMB0GfUDJA7r1_mAKP2TiB_wyV1sRNDK701KqphzDaVq_oYVIDn83qVq3vEwDDK5gXS9Ch-pTWvxsSGAxSR87RG094-Erzxaha9t-CkAvn4Z03Kri4ObswzDQix2IyOKWzSl3imVOTzdhdVgmKXDGxwl2kuHfUF_MSyQ35FRE0hCUS6XD_JtPo9CH2PWONzcDuTzTGKv-ukgmR8MTM30BNokfxChjlLQFEBnBwKkkYxIiBORbfUbhZsfmXgzOWMuD8KPsgh-ZIsfAroVrxNeymbbMNaSwem2LYu1dC8Shvaa8RxM5RrZiS12j8llJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#
منهای_پرسپولیس
☑️
گل اول صنعت نفت آبادان به ملوان (اولین سوپر گل لیگ امسال
♦️
صنعت نفت آبادان  یک - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138243" target="_blank">📅 20:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138242">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✖️
✖️
یازده تای اون زمین کی هستن که اینا نیمکتن
😂
:
✔️
رفیعی
✔️
ابرقویی
✔️
تیکدری
✔️
اورونوف
✔️
شهرآبادی
✔️
سرگیف
✔️
باکیچ
✔️
لطیفی فر
✔️
محمودی
✔️
همایی فرد
✔️
سلمانی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138242" target="_blank">📅 20:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138241">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
بهترین بازیکن نیمه اول از نظر شما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/138241" target="_blank">📅 20:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138240">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
خوشگل میشه به این تیم امید داشت و امیدوار بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/138240" target="_blank">📅 20:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138239">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
تیم سرحال نشون داده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/138239" target="_blank">📅 20:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138238">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/138238" target="_blank">📅 20:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138237">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
❌
✖️
جونم به این تیم ..چه تیم شادابی درست کرده تارتار  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/138237" target="_blank">📅 19:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138236">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✖️
✖️
دو گل تو بیست دقیقه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/138236" target="_blank">📅 19:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
بریم برای اولین بازی فصل با تارتار .الهی به امید تو   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/138234" target="_blank">📅 19:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138233">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
بریم برای اولین بازی فصل با تارتار .الهی به امید تو   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/138233" target="_blank">📅 19:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138232">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/138232" target="_blank">📅 19:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138231">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
در سیاست کاری ما نبود از یک سن بیشتر بازیکن جذب کنیم. عدد درخواستی او از پرسپولیس کمتر از سایر باشگاه‌ها بود ولی از سقف ما خیلی بالاتر بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/138231" target="_blank">📅 19:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138230">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
واکنش حدادی به شایعه حضور محمد قربانی در پرسپولیس؛ حضور او به احتمال زیاد منتفی است و با الوحده تمدید می‌کند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/138230" target="_blank">📅 19:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
در سیاست کاری ما نبود از یک سن بیشتر بازیکن جذب کنیم. عدد درخواستی او از پرسپولیس کمتر از سایر باشگاه‌ها بود ولی از سقف ما خیلی بالاتر بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/138229" target="_blank">📅 19:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
فووووری از پیمان حدادی: با رامین رضاییان مذاکره کردیم، تخفیف خوبی داده، انگیزه داره برگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/138228" target="_blank">📅 19:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
حدادی : رامین خیلی انگیزه داره بیاد پرسپولیس‌  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/138227" target="_blank">📅 19:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138226">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f6013dab.mp4?token=di3dyv6Tl-2Ra_YrzMBrfYWk-M91eCCAYLG0NW9SfQ3JLJD2WHth8eL7g0RpaMcP_hwbw2y9YikhjL2D4-StKOvZtVEhHWmjMSoqLORb9-SgNK1uWV78dHu-k2mSqw-s-h5unJsSPrekkNoZdzUQxSDhnarD8tEtViPUu5ij7F_k1YuGmmSsu1lEbtn8d9nHIYNGlhSwIDa8n1caktWToSmOOCo99NKwzNd2v-P51TEpHwf2HiPU4SEj9P-JQ2VwBoRd3cDj6vlJZhjbgHWC_dyXkSztbZOJGyN_jA3HId6bDP4B2oqpBALD6WQJM36xrkvuUCp08bokYsk-sbNfxpDtCpVQec1JFsHSWlQg9gesBbRIEr8uuxJ0AqQh1UNMTewEWkKJb-DSH_uNydfMzDrBS5AMln3oVM71hZRJK5HS5KcBmmnOObPCR5vyZ4eDk3q26ykaoi63o3AMs8h-HfHp6ESKiztULhUSCIcWRiQHsdW5lO-LFgi1sBepCZyuPVz-M-NTwFikOlid1v27vSaLQpNEm3YrZSGzFemZ201hhrGYEcHjLbK3flTbkP6ROAbpVQ-RsqReHIadPj9WoxK3CtX4nMl3VlhZN3tUoCAI-nTbiypawRHWIA6ohNZqjOa0xSFU1QQa30VD0KUMGrGSPalhgfwpgiY1eMDTu2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f6013dab.mp4?token=di3dyv6Tl-2Ra_YrzMBrfYWk-M91eCCAYLG0NW9SfQ3JLJD2WHth8eL7g0RpaMcP_hwbw2y9YikhjL2D4-StKOvZtVEhHWmjMSoqLORb9-SgNK1uWV78dHu-k2mSqw-s-h5unJsSPrekkNoZdzUQxSDhnarD8tEtViPUu5ij7F_k1YuGmmSsu1lEbtn8d9nHIYNGlhSwIDa8n1caktWToSmOOCo99NKwzNd2v-P51TEpHwf2HiPU4SEj9P-JQ2VwBoRd3cDj6vlJZhjbgHWC_dyXkSztbZOJGyN_jA3HId6bDP4B2oqpBALD6WQJM36xrkvuUCp08bokYsk-sbNfxpDtCpVQec1JFsHSWlQg9gesBbRIEr8uuxJ0AqQh1UNMTewEWkKJb-DSH_uNydfMzDrBS5AMln3oVM71hZRJK5HS5KcBmmnOObPCR5vyZ4eDk3q26ykaoi63o3AMs8h-HfHp6ESKiztULhUSCIcWRiQHsdW5lO-LFgi1sBepCZyuPVz-M-NTwFikOlid1v27vSaLQpNEm3YrZSGzFemZ201hhrGYEcHjLbK3flTbkP6ROAbpVQ-RsqReHIadPj9WoxK3CtX4nMl3VlhZN3tUoCAI-nTbiypawRHWIA6ohNZqjOa0xSFU1QQa30VD0KUMGrGSPalhgfwpgiY1eMDTu2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
واکنش حدادی به شایعه حضور محمد قربانی در پرسپولیس؛ حضور او به احتمال زیاد منتفی است و با الوحده تمدید می‌کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/138226" target="_blank">📅 19:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138225">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
حدادی: صادقانه با رامین خودم مذاکره کردیم ولی خب چون سنش بالاست و اینکه با تخفیف بالایی داده هنوز رقمش بالاست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/138225" target="_blank">📅 19:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138224">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
حدادی:تکلیف قربانی رو باشگاهش مشخص می‌کنه ولی بعیده باشگاهش بفروشتش   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/138224" target="_blank">📅 19:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138223">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
حدادی: درحال مذاکره هستیم با قربانی اما بعیده باشگاه الوحده قربانی رو قرضی یا قطعی بده
😑
😑
😑
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/138223" target="_blank">📅 19:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138222">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
پیمان حدادی: شفاف بگویم بازیکنان جوان را می‌خریم که رقبا نتوانند بگیرند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/138222" target="_blank">📅 19:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138221">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
پیمان حدادی : امیر جعفری دفاع چپ گل گهر در لیست خرید ما نیست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/138221" target="_blank">📅 18:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138220">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
درصورت تایید مهدی تارتار طی 24 ساعت آینده امیر جعفری مدافع چپ 25 ساله گلگهر سیرجان به پرسپولیس خواهد پیوست.
❌
❌
تمامی توافقات با این بازیکن و گل‌گهر سیرجان توسط مدیریت پرسپولیس انجام شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/138220" target="_blank">📅 18:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138218">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✅
✅
حدادی: ۵۰۰ میلیارد تومن برای شهرآبادی، محبی، زارع ، اژدهاکش، لطیفی فر و ایری رضایت نامه دادم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/138218" target="_blank">📅 18:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138217">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
حدادی: کسری طاهری رو نیم فصل میگیرم اگه نره سپاهان   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/138217" target="_blank">📅 18:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138216">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
فوووووری
✔️
✔️
حدادی:  به روبین کازان برای کسری نامه زدیم به ما گفتن ۱ میلیون دلار + ۲۰ درصد حق ترانسفر بازیکن و ما رفتیم شهرآبادی رو خریدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/138216" target="_blank">📅 18:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138215">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✖️
✖️
یازده تای اون زمین کی هستن که اینا نیمکتن
😂
:
✔️
رفیعی
✔️
ابرقویی
✔️
تیکدری
✔️
اورونوف
✔️
شهرآبادی
✔️
سرگیف
✔️
باکیچ
✔️
لطیفی فر
✔️
محمودی
✔️
همایی فرد
✔️
سلمانی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138215" target="_blank">📅 18:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138214">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔄
🔄
🔄
یک تیم کامل و خفن فقط روی نیمکت هستند</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/138214" target="_blank">📅 18:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138213">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/138213" target="_blank">📅 18:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138212">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/138212" target="_blank">📅 18:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138211">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0GL-onWLxm2-gWSUkHjZ6AO5nqPh7GP48LQcSvU_azUWbsHhKa4ns2y3WV1Pwx4xlMBsDiE9VztZ9sKeu4Rd9E4EcKw0VgiSXiDEuhoaQIYX8lyDngNHVUUdWbi2es21ixVI2PdhMs0H1hHsodzqeiAwbruWvhTO2tuVzeeQKxwCX-Crl_NY2seRLuKfyGfEj9eo2ph77Bw9_9HTvJZfonsEFNc9GMLdsnTmRKg2oydrjsEWM9FqhCK9IV0DSf8eZSFz1a2pobt9tB_aWCQvksj73Dov2XRBck4U3tTzuSP9I9p97HrQLztZaq7Pbu_OEv_R38xAZnSvP-lt090ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شماتیک ترکیب پرسپولیس برابر شمس‌آذر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138211" target="_blank">📅 18:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138210">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
فوووووری
✔️
✔️
حدادی:  به روبین کازان برای کسری نامه زدیم به ما گفتن ۱ میلیون دلار + ۲۰ درصد حق ترانسفر بازیکن و ما رفتیم شهرآبادی رو خریدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/138210" target="_blank">📅 18:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138209">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
پیمان حدادی مدیرعامل پرسپولیس:
✅
تصمیم گرفتیم کادر ایرانی انتخاب کنیم و پای این کادر بمونیم و از کادر حمایت کنیم ابزار لازم براشون فراهم کنیم و بهشون زمان بدیم . ممکنه در هفته های ابتدایی نتایجی خوبی نگیریم ولی از هوادار میخوایم به کادر فنی فرصت بدهد . …</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/138209" target="_blank">📅 18:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138208">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
حدادی: ممکنه پنج شش هفته اول نتیجه نگیریم که ایراد نداره
😕
😕
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/138208" target="_blank">📅 18:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138207">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
پیمان حدادی مدیرعامل پرسپولیس:
🚨
از زمانی که مسئول اجرایی پرسپولیس شدم روزهای سختی را پشت سر گذاشتم. قسمت نبود به مسابقات آسیایی برویم. پرسپولیس با پوست اندازی به یک تیم نوین تبدیل شده است. نبود در آسیا و نگرفتن جام در 2 سال آسیا برای همه ما قابل قبول نیست.…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/138207" target="_blank">📅 18:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138206">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
پیمان حدادی مدیرعامل پرسپولیس:
🚨
از زمانی که مسئول اجرایی پرسپولیس شدم روزهای سختی را پشت سر گذاشتم. قسمت نبود به مسابقات آسیایی برویم. پرسپولیس با پوست اندازی به یک تیم نوین تبدیل شده است. نبود در آسیا و نگرفتن جام در 2 سال آسیا برای همه ما قابل قبول نیست. امید داریم از شرمندگی هواداران پرسپولیس در بیاییم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/138206" target="_blank">📅 18:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138205">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
یک اتفاق جالب در بازی دیروز سرخپوشان
👍
در چند دیدار دوستانه اخیر شاهد لو رفتن ترکیب سرخ‌ها پیش از بازی بودیم، اما دیروز ورق برگشت و هیچ رسانه‌ای نتوانست ترکیب اختصاصی تیم را پیش از بازی منتشر کند. به نظر می‌رسد مهدی تارتار به وعده‌اش عمل کرده و پس از…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/138205" target="_blank">📅 18:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138204">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
علیرضا محمد، مربی پرسپولیس: چمن استادیوم سردار آزادگان بلند است .سبک ما روی زمینه و باید کوتاه شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/138204" target="_blank">📅 18:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138203">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
🔴
بازدید بازیکنان پرسپولیس از چمن ورزشگاه سردار آزادگان در آستانه بازی با شمس آذر   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/138203" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138202">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bfb0b88b.mp4?token=PRjS6W9GqV0_Vbma59bhZNh31DFL7ruXv1LAbQjSBnkQHGTX1ne4YytPjWiahfEk_WgITPPsHfZMnLult1qAgFWrNj0AG7WV4BAzICIkb_akOaE4TgN8o8CU7Y6AfUkRM06KFe1tB_UnKCJoh7Gf_GzKs72S77WstGV7CHdF_HXdm-qgX0E8d4O4CRa5l_BG0oFSJVKORxihTPJPRFsiEsV3wKnHN4BZB7R1JvP0I3sGlUtcs5iMg5RSjLIsa0s52WxSYsMlzb-wLXQU92cZTFLK4s_7tCg6CjZ1QvScPW9OMctcYo8MVyQQTUXzUCbhzh8jWM5f2v3L_qvZuZOZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bfb0b88b.mp4?token=PRjS6W9GqV0_Vbma59bhZNh31DFL7ruXv1LAbQjSBnkQHGTX1ne4YytPjWiahfEk_WgITPPsHfZMnLult1qAgFWrNj0AG7WV4BAzICIkb_akOaE4TgN8o8CU7Y6AfUkRM06KFe1tB_UnKCJoh7Gf_GzKs72S77WstGV7CHdF_HXdm-qgX0E8d4O4CRa5l_BG0oFSJVKORxihTPJPRFsiEsV3wKnHN4BZB7R1JvP0I3sGlUtcs5iMg5RSjLIsa0s52WxSYsMlzb-wLXQU92cZTFLK4s_7tCg6CjZ1QvScPW9OMctcYo8MVyQQTUXzUCbhzh8jWM5f2v3L_qvZuZOZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
حال و هوای ورزشگاه سردار آزادگان در فاصله 90 دقیقه تا شروع بازی شمس‌آذر - پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/138202" target="_blank">📅 18:07 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138201">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0a826af.mp4?token=i0VzmY_oMHZf0idhFTpD0ywMfXRko-O02VPaGTYzVtFf5SpzgkKndCtaM2jwk56pCf4X0GyEoj66XKjaZIIBoqjHtq2bGyXWa4ibbsFz5sB-XcJtbGB0TS4oYf2H9I7BE7PPV4UYmTkZAJ1rEkmMDqOZvVam-GAESsGVr986H0gOdJSHHVyiqIzoBuTHwvuDIBVp8h7FZzRZsrcUCdS3ovx4debCgx14BP_RWwp8Ml1DG5srg2BBDvCaB7EICUNtUzymf5ea1ULmlvvuQvFO09zBZNOezd6j5rvXcdAeNjBqscQtJ3ZkVY3DGDxqh2ZtXj1Bh--TfDcUHdC9HXkv7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0a826af.mp4?token=i0VzmY_oMHZf0idhFTpD0ywMfXRko-O02VPaGTYzVtFf5SpzgkKndCtaM2jwk56pCf4X0GyEoj66XKjaZIIBoqjHtq2bGyXWa4ibbsFz5sB-XcJtbGB0TS4oYf2H9I7BE7PPV4UYmTkZAJ1rEkmMDqOZvVam-GAESsGVr986H0gOdJSHHVyiqIzoBuTHwvuDIBVp8h7FZzRZsrcUCdS3ovx4debCgx14BP_RWwp8Ml1DG5srg2BBDvCaB7EICUNtUzymf5ea1ULmlvvuQvFO09zBZNOezd6j5rvXcdAeNjBqscQtJ3ZkVY3DGDxqh2ZtXj1Bh--TfDcUHdC9HXkv7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
🔴
بازدید بازیکنان پرسپولیس از چمن ورزشگاه سردار آزادگان در آستانه بازی با شمس آذر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/138201" target="_blank">📅 18:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138200">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
🔴
ورود تیم پرسپولیس به ورزشگاه سردار آزادگان برای بازی با شمس آذر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/138200" target="_blank">📅 18:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7899739a.mp4?token=T8yjpyFLdCbfzj_8ymoV9Fu6JU-0pA9_bNY6INktxANc2G771OK7v760L8ZLTIDTkDh18dT9gYpbfRQ12M12ojz05gZtxGyJTdLxu9LZ2MhkRVfi3nM0BbQYMfvmn3GRSqNKiPLry1mr88s6EsZd_w2vJYqlC1pOYtewaBCBo4yunAzHcUyRkWB_-QKTffqkkoMN1YatEGb6TH4G2XwqrBHEWEWEJZPL11-pVHf2CBMU1R3qc4oOCSB48RAgf0GrA24cZYdXikh-_9C3RDChn4GQq33Z2puAiNUCyEWmhoM0rqyOGCTuxqL8pLCcV6l4ux8ogg2YfLZjm3YKAg7Ctg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7899739a.mp4?token=T8yjpyFLdCbfzj_8ymoV9Fu6JU-0pA9_bNY6INktxANc2G771OK7v760L8ZLTIDTkDh18dT9gYpbfRQ12M12ojz05gZtxGyJTdLxu9LZ2MhkRVfi3nM0BbQYMfvmn3GRSqNKiPLry1mr88s6EsZd_w2vJYqlC1pOYtewaBCBo4yunAzHcUyRkWB_-QKTffqkkoMN1YatEGb6TH4G2XwqrBHEWEWEJZPL11-pVHf2CBMU1R3qc4oOCSB48RAgf0GrA24cZYdXikh-_9C3RDChn4GQq33Z2puAiNUCyEWmhoM0rqyOGCTuxqL8pLCcV6l4ux8ogg2YfLZjm3YKAg7Ctg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورود بانوان هوادار پرسپولیس و شمس آذر به ورزشگاه سردار آزادگان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/138199" target="_blank">📅 18:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138198">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
یک روز مانده به بازی بازم ترکیب تیم لو نرفته و کاملا مشخصه جاسوس شناسی شده بعد از سالها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138198" target="_blank">📅 16:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138197">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔄
🔄
مدیرعامل مس شهر بابک: آسانی فسخ کرده بود؛ از استقلال شکایت کردیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138197" target="_blank">📅 15:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138196">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⚡️
⚡️
شنیده میشه تیوی بیفوما در یک ماه اخیر برای ماندن در پرسپولیس زیر نظر پزشک تغذیه باشگاه 8 کیلو کاهش وزن داشته و علاوه بر اون زندگی حرفه ای شو سالم تر از قبل کرده و تمرکز اصلی شو روی فوتبال خودش گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138196" target="_blank">📅 15:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138195">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
علت ماندن تیوی بیفوما در پرسپولیس، کاهش وزن، آمادگی جسمانی مطلوب و همچنین تغییر نگرش او و اصلاح سبک زندگی شخصی‌اش بود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138195" target="_blank">📅 15:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138194">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⬅
⬅
⬅
حمید مطهری سرمربی فولاد گفته الی و بلی رزاق پور باید بمونه و اگه بره پرسپولیس استعفا میدم!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138194" target="_blank">📅 15:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138193">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
سینا اسد‌بیگی: بعد جدایی از پرسپولیس افسردگی گرفتم، دلیل جداییم از پرسپولیس فوتبالی نبود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138193" target="_blank">📅 15:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138192">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9CliBIsW7MMcw4BDolcG_dDUPENyfzsxUFEmtMuerh829UBhYzgh7IVC8Zv4khfYcALEQgBkYXpht4nGSElT_IZG4R4KxtYbU4v9WYn6sTQhjxMrtGzqbvjYJQ2YCoTPrjqu7WQE9rbWVZ0XBvmECr7aXlAd5p3nOnMijR7ibTP7n9gGU8bC8LQBS4_bHfJx9Nril8iS967shaXiWLLWfWq8KDjWqzP7_w-L4u0W4f_7XXfn-pJZjgLUpUwjxLq-aJO9PWvBbPPfGIJBjY-9z5FJGI3qxOlbNYhcv71iaXgAH0c3psYEcJgfw0gETPFhBLftKkrw3uGXXi54vIXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇
⬇
اگه ترامپ تصمیم بگیره قبل از شروع هفته دوم به ایران حمله کنه، لیگ دوباره نیمه تموم میمونه و استقلال برای اولین بار در تاریخ خودش دبل قهرمانی رو تجربه میکنه
😅
😅
⬅
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/138192" target="_blank">📅 13:51 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
