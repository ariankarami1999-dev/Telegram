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
<img src="https://cdn4.telesco.pe/file/EgDCOS65lr_9VKhDIC0xXSfsnC18aIFYGQZan4v6MCVTq6OLTbUD0ZqcAIihWSVoKknGC-HOV7fG07zjVZNTCVC3z-hhlBATq9vFclOixne5HTpC-hjp2ichRG8eT28ajpZfHnh29hpiI_58ExZVzRBloFMASohu08CRJStESWI6X9HG_Xg-Z3fOBWiJhs8OjyNDpWJFeH8koUKy0o6xP-LtsgMed3cet8a3MyMXOF3_93e7_fbowc79BiJXH8n3XDsDMNStji3b6udh8IBasiuVJ4aJJIIl36c6Yg7F9WWc8bvpM6QIXdJgDX74h-cLi5Aa4v-KNdP72tbDplRQWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
<hr>

<div class="tg-post" id="msg-140580">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II4iaU7qK0xCcYp5L8H7kwLMdKKs7OtVqMF0XebVjFSBgIuS16xHqyr9APHS9qSktwBS2JPI3C1-iHiau6_t9ghCk44U6E4EL0UaJRrevtut_aCmlyDakwoHUQoV0Mjoz74RVC9RZQVkH8Icyh9sMcqdKPDbP-qzIOPZuLsV1kPtYIjU26PflznNRHATudnHyLGYABJEUbWUbl-r3G0rOQO5E2atdIOQ7eRupEFC48aQ6tae5bdlLje37slB04eKlzi_oac1Bc-G-WNvBSUDxpAiwpWob_vL_g5kFPVHWoe3HesXrZmNNLYM8ZQJNbfjUYa7CCWJuiHFiEwEd-G_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
England -
🇪🇸
Spain
⏰
Tonight 22:15
🏟
Wembley
🇪🇺
اسپانیا با ثبات بیشتر در کنترل بازی و خط میانی منسجم‌تر وارد ومبلی می‌شود؛ در مقابل، انگلیس روی سرعت انتقال و کیفیت ساکا، بلینگام و کین حساب می‌کند. غیبت رایس، پالمر و چند مهره دیگر می‌تواند تعادل انگلیس را تحت‌تأثیر قرار دهد، در حالی که اسپانیا با هسته اصلی قهرمان جهان و اروپا حفظ شده است. از نظر فرم، اسپانیا در ۵ بازی اخیر ۵ برد داشته و انگلیس ۴ برد و یک شکست ثبت کرده؛ بنابراین انتظار یک بازی نزدیک با موقعیت‌های دو طرف منطقی است.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 497 · <a href="https://t.me/SorkhTimes/140580" target="_blank">📅 20:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140579">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/140579" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140578">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
🎤
بخش اول صحبت های حامد کاویانپور مدیرفنی آکادمی پرسپولیس بعد از دیدار با امید سایپا
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/140578" target="_blank">📅 19:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140577">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
قسمت جالب سربازی بیرانوند اینه که همین آقا دو ماه پیش علیه علی دایی استوری گذاشته بود: «من هیچ‌وقت از رانت استفاده نکردم»
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/140577" target="_blank">📅 19:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140576">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/140576" target="_blank">📅 17:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140575">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/140575" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140574">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/140574" target="_blank">📅 17:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140573">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
اوستون اورونوف و مارکو باکیچ هم اکنون در ترکیه حضور دارند و اگه مشکل پروازشون حل شه تا شب به تهران میرسند    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/140573" target="_blank">📅 17:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140572">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr_4U-1NAVTagh3XkoeppDbU72-N9KunROcnUeSIwjx6H9YENSHKCsfQZHJIRXBZUkpC43v7ZxYa0VvlWhdDYJVBi_5cBmlvBvIvQBygXucYQIDwCHgBxrTlw9U2Dt8ARmMnAF2dyOu-nOJ9ETiQ-1Bgg45RbGuF4zp56-S8wIQ7MwFor5HZs3x2_M1JK-4r-rDQ_XDNLsma01valLP8zuhqxEn2UNGILV2S7RYHqLqnk4SIA3MM8U9-4fdkwPKzXVEJPpu_XSs6hEm-UihImEjOH3uLukZLYqpYqFaNy6J80V5PjvXPPiw1bOr4RYbDTjT2UC6YVkIs6h3mFIfrVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/140572" target="_blank">📅 16:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140571">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🔴
فوری؛ معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/140571" target="_blank">📅 16:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140570">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_AyaFp9-t2D3tPxWX62E-Do4kT2NnOrsnd2vfFGZw261KVejjoshli0SihNhJ1-XFgCtnvrYiHAhmA3BDQsiKxG94F1lYj7c03SxnrAPcRStP1B_bClV1gbRG51GD9WjWOY2pM0bteGWDV0S8gFyoDPqUnH67jnNL3zJeIdHdVK3TZjz6VpfkqIivoHjg6-W8POhM7qJPD5kg20bBu3S4BhfbjGhwm2Y7C3V9WNM2NAFGWgRduhWj5cgQJ2sTmkQHb9-jDxgwDfNbRmQJiTEaaMVSxQPHdFoVC6pu61_d8VtZxJEKEn5CeAlgLBT1CnlDgr95Dme-mCYdmxi8Umlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از بدنسازی امروز پرسپولیس؛ شاگردان تارتار فردا استراحت خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/140570" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140569">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=XNchXJUmb_J-sudIRM2l-y_ScWg7IKoQ1qawOtkU1hfeP6tApGXmhf_6Bp0gadIQ51KaVV8ZMjlu1-UNVfJ9_-bnQElbIACAILxBCeC7HLu5hiezEXUDX8-LCA7M41c865HVjR59BucrULWUBaPOSrFHUv8sKR4-GRH-rm9Epe0wnDe5TamDR6nDDCHL4zX0ljSAA4VtMtHTZbToejLvRg2lKC_ZVqvVIWavPq9HJQyJzJjdoPWeBIPrj1GC-1WrYmrNik_E5K-eUd8crmBxoa9wZ7odDf8MHuUGWOXpBSMs9Cby6bEyZLc8zLXkwRsH3grSITTbyAVxy96B7gk51VrBs8bttPXuj_MuWXjjL1o2b7PwTOEElJ8orP1z9cjrszJnWS7kqLsRYXayjzvTsv47CQ5BEfPHw9UE6in0NT_Si8djA4bIC6PMowz1L08AeGhq93SsteeHIX8ugHEhM6Uht2LO1BL7irBHi8_zZq4fSxoyR7x0wrUDPFTcET85MSdTsXcPfRyq3ipBvjAyQweGOaPKShnIKXOih-fdn2xupIWkIsfx3UJrYlncFJmrowfJg6Ax2R50elH7D0LptSpDY8VxYoYRGIu4gKeP06SiWl5qXvLeiZ2ovVFHFqh-WXMoRdSbt2ln_OQBBQBeF5sH9tC9zA6U5sagFGf5emM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=XNchXJUmb_J-sudIRM2l-y_ScWg7IKoQ1qawOtkU1hfeP6tApGXmhf_6Bp0gadIQ51KaVV8ZMjlu1-UNVfJ9_-bnQElbIACAILxBCeC7HLu5hiezEXUDX8-LCA7M41c865HVjR59BucrULWUBaPOSrFHUv8sKR4-GRH-rm9Epe0wnDe5TamDR6nDDCHL4zX0ljSAA4VtMtHTZbToejLvRg2lKC_ZVqvVIWavPq9HJQyJzJjdoPWeBIPrj1GC-1WrYmrNik_E5K-eUd8crmBxoa9wZ7odDf8MHuUGWOXpBSMs9Cby6bEyZLc8zLXkwRsH3grSITTbyAVxy96B7gk51VrBs8bttPXuj_MuWXjjL1o2b7PwTOEElJ8orP1z9cjrszJnWS7kqLsRYXayjzvTsv47CQ5BEfPHw9UE6in0NT_Si8djA4bIC6PMowz1L08AeGhq93SsteeHIX8ugHEhM6Uht2LO1BL7irBHi8_zZq4fSxoyR7x0wrUDPFTcET85MSdTsXcPfRyq3ipBvjAyQweGOaPKShnIKXOih-fdn2xupIWkIsfx3UJrYlncFJmrowfJg6Ax2R50elH7D0LptSpDY8VxYoYRGIu4gKeP06SiWl5qXvLeiZ2ovVFHFqh-WXMoRdSbt2ln_OQBBQBeF5sH9tC9zA6U5sagFGf5emM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/140569" target="_blank">📅 16:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140568">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🔴
فوری؛
معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/140568" target="_blank">📅 15:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140567">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=nahicHSv8PO4m-D7GMZ0jOCe1otLKamaeQpXnpqFWoaG35OnepGs0JVYq7CRUHu-4fmMWuNgRf-Su5yrCmgh75AgfIv96uIeAyZkVSZ_UVBJ3I1iOJGRx61KZyo53-atGIskD8iurZbr9XAm7U4WobTwXnGt-qzHWmUcH-vrgV7b6uf6vyU8l8kmNTo6BENecco5dpvz6VT1UKHMEVnhMO7sKSu4s5xQaq2dosyVLQqfLcF8e_nTK2gDgwQEVhF3HeVqexIUR-kMpDax4367GyBe5myi6yK0p_GHJ-YPYFfe7wBj4O9eGNagiPUwoG5qoAaOJE7lGwMF2YpSzkeauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faac5ebeb7.mp4?token=nahicHSv8PO4m-D7GMZ0jOCe1otLKamaeQpXnpqFWoaG35OnepGs0JVYq7CRUHu-4fmMWuNgRf-Su5yrCmgh75AgfIv96uIeAyZkVSZ_UVBJ3I1iOJGRx61KZyo53-atGIskD8iurZbr9XAm7U4WobTwXnGt-qzHWmUcH-vrgV7b6uf6vyU8l8kmNTo6BENecco5dpvz6VT1UKHMEVnhMO7sKSu4s5xQaq2dosyVLQqfLcF8e_nTK2gDgwQEVhF3HeVqexIUR-kMpDax4367GyBe5myi6yK0p_GHJ-YPYFfe7wBj4O9eGNagiPUwoG5qoAaOJE7lGwMF2YpSzkeauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور پیمان حدادی مدیرعامل پرسپولیس در ورزشگاه درفشی‌فر برای تماشای دیدار امیدهای پرسپولیس و سایپا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/140567" target="_blank">📅 15:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boTm_NrIrZhts-okiQyEGvgNVHkIFZzYNKtaupVB_sogZFn5vcjaX61DR4htRpjbkkYCAyN2n5zTrWid3qLh7aSGHWgA8pV_DBGz3vIrYbgidCNxAdA-tPlEdcb_lJS-fo7M-oa03zmWKM_z1Z5Kw43rclYQjiOYuQzKzd7cfSsMnOWWxaFlHzp0_HoMao0lbbMRyzoyhJxYgMYbB4OBKjBwiuNhOVm0cmWfYCUruM3kOUTlLpJdGHqhhLosTxxh4py7NvnxZE6h-suNdMoc1fw0rFtQoOVTJj1urnd8rDa1Z6NEcsTvfmL2eZ9luunxtJjWbgzM1VxInHwe3eZuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد بزرگ در اوج هیجان؛ اسپانیا و انگلیس برای یک شب تماشایی
⚡️
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇪🇸
اسپانیا
]
⚽️
اسپانیا با میانگین مالکیت ۶۴٪ و حدود ۱۹ شوت در هر بازی، از نظر کنترل و خلق موقعیت دست بالاتر را دارد؛ انگلیس هم میانگین ۱۳.۵ شوت و ۲.۵۶ گل زده در هر بازی ثبت کرده است. با توجه به فرم هجومی دو تیم، انتظار بازی با موقعیت‌های متعدد می‌رود؛ در عین حال هر دو خط دفاعی در هفته‌های اخیر آمار گل‌خورده پایینی داشته‌اند. تقابل در ومبلی و شروع لیگ ملت‌ها، این مسابقه را به نبردی نزدیک و تاکتیکی تبدیل می‌کند؛ جایی که جزئیات می‌تواند تعیین‌کننده باشد.
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
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140560" target="_blank">📅 14:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEBu0rjJLzOzu3QhltTvMfxwAA4cY4LuEexJXYGGGIpdjlvHUPt_CSYJQQtcfqglv556sq9Hwk_-8q1dLaJPpp8tlOBnMa9ZHsHW7nfIkNyL0FPTfsZ1faV8lWZnnAiy4D12Zq_BdHkRScxhmv1vX9qBvrr7HTSpQ7Phbmm988ME4UyTpkb03v1VR8CFHaDc23XLdghkBBGNqWwY6XODdGH4UqJJxN30sPHl37hPAIX301pZdrBixHeCyBMPsuAjPoEsD3rSq35pBJKlva7kEeSCeyKM4WAsSlY7ftTqy9_SjwuaSHnL_FXJzz3MqPUo0i-yfCbdXxtNAL2pDf26Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم قلعه‌نویی واقعا عجیبه!
❌
بازیکنی که از جام جهانی خط میزنه رو کاپیتان میکنه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140559" target="_blank">📅 14:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚡️
⚡️
تاج اعلام کرد امسال دیگه سقف بودجه وجود نداره، اما فیرپلی مالی اجرا می‌شه.
⚖️
طبق این قانون، باشگاه‌ها باید قرارداد بازیکنا و هزینه‌هاشون رو منتشر کنن و اگه این کار رو نکنن، سازمان لیگ خودش منتشرشون می‌کنه. همچنین باشگاه‌های زیان‌ده فصل بعد با محدودیت…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/140558" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
فوتبالی:
✔️
✔️
گفته می‌شود فدراسیون برای جانشینی عبدی با گزینه‌هایی مثل فرهاد مجیدی و مجتبی حسینی وارد مذاکره شده و باید دید در نهایت چه کسی هدایت تیم امید را برعهده می‌گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/140557" target="_blank">📅 13:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
در صورت تشکیل تیم (ب) پرسپولیس، گزینه‌های سرمربیگری:
⏺
محمد نصرتی
⏺
اسماعیل حلالی
⏺
محسن بنگر
⏺
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/140556" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140555" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140554">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140554" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogs5jiDEi5j64Twf2pSJMQqzSpEXRnsZHr0wheJJ5SYGV8fAjMcYBu0-eEKzE8C_Ps01a3qYIXbft9zeLtaaIEGKPGfzyZNq2O7150hI_i2NzLHAFNBe_kNrcxl7cf41OfWhctGpE66E1b0QLPtYFaOwUM9807nU85dT0sw_v9vWVnUG_jTu5V5nuJHleZSTiv1Ma7RjNXSWfoV0MCyI4t55ro_k5sH36xlqMCEk0DBIYmfpgqmVIdqim9tQw6PF62HCr76qE8JTrBH6IbKvMOPgOVIRPhCWqYGAC9z6-UFzv-4SyPcTiYkR-m8rsrqMHckA27qBH-TJadHQd0YJHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
باشگاه استقلال در پرونده فابیو کاریله که فقط اومد یه سلام کرد و رفت به پرداخت ۴۰۰ هزار دلار محکوم شده است.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140553" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
❌
سه وکیل خارجی باشگاه بعد از دیدن مدارک جدید در پرونده آسانی اعلام کردن، درصد پیروزی پرسپولیس تو پرونده زیاده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/140552" target="_blank">📅 09:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQKvWrwWgEMNU9C8aqN80_lAm1BY7FzNKNM9wsmQmvprjK9k3f1xOcy2F2Unyg7JnYpQcAaNlX8jCxFMFG3x2bXCQPlbBvQwxFlJkZ06wqMy7vzocWUD09ZlPu8kw323CqTEONYXH2DUFAbDtL8m_b3QI3qIqmdVrIlj2hhGc0ZV0xZ6VsUbZgz9Q7q9SdwJu4UQKh04oIaZJYEB9Uc45oq34NyuceZUWf2TbONYiLHDt7CAtPyW2GEt0SsFfTpgLtc-DzYlLboV-wvcpt6eE938BP3BSh2qk5oC2dNYSEiXGI3cBWHZBsdn1YnbjHBTBATmHdZOSBBTDncnnkCv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140551" target="_blank">📅 09:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srsOVRUHnKj0nXd5s4aHrwXz-FifjpJq8VbMv7QtUh-0MNrEuYKEUZqJ7ioVwDi3XBxkLeUF7emJ2a97K9Ikr5rvsskXZebeHy5YgWETAYjsRGFs3fOojhrjHKZeSygyh1pGsOch0AqXPnF6_BYc3jSdKzAn5k9rEuuzznaQWODlTmjN-OX4owo3gS0Bgbo5CrAZvEcMxqet9kvx8IIxdHZ99EFO9ejFz8AwGsj2u0Jj8RwX_vpq5w4qpFUAoQURTd3TtwV7ZHebyLF8fX3SrcTFc3SFDYRdkqEMGsm9V9IU124uauCO4rgLRnTv-r8MNAxYVxCpKOO49yP32oIoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
شبِ حساس لیگ ملت‌های اروپا
🔥
⚽️
فرداشب چند تقابل جذاب در برنامه است؛ از جدال نزدیک اسلوونی و اسکاتلند تا رویارویی مدعیانه چک و کرواسی. آلبانی با توجه به ضرایب، شرایط بهتری مقابل بلاروس دارد و سوئیس هم برابر مقدونیه شمالی دست بالا را دارد. اما حساس‌ترین بازی شب، انگلیس و اسپانیاست؛ دیداری که می‌تواند از نظر فنی و نتیجه، متفاوت‌ترین مسابقه این کنداکتور باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140550" target="_blank">📅 01:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASINgTwpTewXrqY00gnelIcgmsPVystys_oEtuIX6yGqFn0sXgEalZ_nHekGFKwQWcUH3U0pw_28g_a0ThGgwDyDbYyA-x7vl_oCRBfx5YVqSm5R7i08tBSXx1_fISfMwnb4QtAuTzqP0vt7pRB9RdhJyxVWFly44ZLjuSQwh775eum5buy4EIVnhG17JkjY0cFZtv-vsBoqxkb_EmY5NjINf5K6-Kuba27UGLo_I8TE_6HPuJCfzbpAgAH08htqPjesnyUbsmGlY6oriMxJH7TCMFqlomMiQrL5AGBAy6poipeeXbKPZGSaxwToTGcTKaV0yJNE-BId6sihdjO3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
اعتماد ویژه تارتار به جوانان آکادمی
🔻
مهدی تارتار در دیدار تدارکاتی امروز مقابل چادرملو نشان داد که برای بازیکنان جوان و محصولات آکادمی پرسپولیس اهمیت ویژه‌ای قائل است
🔴
در این مسابقه، ۷ بازیکن جوان آکادمی فرصت حضور در ترکیب را پیدا کردند تا خود را در سطح تیم بزرگسالان محک بزنند
🔴
این فرصت می‌تواند سکوی پرتابی برای جوانان پرسپولیس باشد؛ حالا نوبت آنهاست که با ارائه بهترین عملکرد، اعتماد کادرفنی را پاسخ دهند و مسیر خود را برای حضور بیشتر در تیم اصلی هموار کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140549" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGWuBJOSh4B-f6A3iImAu-iGOvtp7CXMI1qDWyLEBJWe1HjYdbNwDP5mymvNZTmS6OwrUPs4b5Wz7xT6eRcvdICgylRdEtXUiTGAzXJv5aNlFeoNgXNbZJOvw5cgAVSfIGmSRjXrEg6fv-DaY55_hhmRwBsBhzmD5o6LgC_sna7dui3gu954KpNYJ6awRJZlQ2p0K2r1eujHBNSkL2jxjZaafCLZNfLmGMMqUtoHVC42pdNZGI4CVkKyIp7bjoJ3_rRF5Hjwg1wS_gcN5KQZjb9RWFWm5J35coxN5iBKUWx06CUmnBaATzvOOVtZEbD5J1DmmhQdSZHlcGDGlWVXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نتایج هفته دوم لیگ برتر بانوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140548" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140547" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpEu0j2WnzQZatAmA_jw0T2ZkQaqLQaZJaZIs-IMerye-5ylFsA9CMbLr276hnEPVHpqfZiuEfk1QCllyww44hr5OoPG3cW3bxLdppVlboSkc2H6ExVcDyJdCVilX5_NEne9k4AMJAVKFK5m-kmjhvNSCuX1fgA7e84dI9zSbRSLZ_AnqKC1amKraKK5ZVb3NbFvAB4uj59iShTPXRQIqyq4Qv2kpISByLOgY1Naaqyju7sYRy86BLddJ82Vo29_LwhtQPzRFhAHVz4W443vtM4asJPYIdfYB4tB1h4uSXz6-Fs3ccpG7w3dRlGbp5fBRF_5FG0qndyQsRRwZOww7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم.
/فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140546" target="_blank">📅 23:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
نتایج ۲۰ بازی اخیر ایران با قلعه نویی ؛ ۸ برد - ۷ مساوی - ۵ باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140545" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140544" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⭕️
👀
صدای پای اسکوچیچ به گوش می‌رسد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140543" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140542">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
چیت ساز، معاون وزارت ارتباطات :
🗣
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
✔️
✔️
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140542" target="_blank">📅 23:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای  جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140541" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140540" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeDcdfPp3doXZwDJ1OalD5uZUne9obUHCeZVmmVqEFOfRlkM4Y35b8XpS9yQiUFiYtyINaOoXaAziPuYRvDpN9CwslILh1ThSfoLy5v86BnCjMmcdXJsFAJ9HegExS-PiDgXIecw1eAk6eWxSxChD2w9EQCWPTPwdu82USngUXxXoNUYIDprx789_nIZbshd6FAjjA24ZrDsQMclhVDjgcVUo6c63tOiewh4aJb5ZqpnhsEUF0v1Kn1oS-Bk_fnHy8pc2INML4iWlwjf0cnU6Y3SQq2A-ffJJeFaa1h_urAnom0Pd1fb5_8U_mnFBf0fE-K48PPk7dxP1zkrOzvLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تولد مهدی تارتار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140539" target="_blank">📅 21:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
مهدی تارتار با بازگشت میلادمحمدی مخالفت کرد/تارتار همچنان رزاق پور را میخواهد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140538" target="_blank">📅 21:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140537" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140536" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHNCCMJPC92g2KlzM7v8Gjd2Bhndja6DSnpGQi2_UAlVTDPM1-VHwziY_AgTWBLs_5kZn9vejTUSX3-hchJ-NvpWnPqJHH1Amj0DmRUtUu-VtW64aLcyuF-s9ByxbJq40p7Ffv8T1AKU7hqjPG1K4tWm264iqcHc4OOb184Jchy12c21FNczNcO0SUPPjdzidamZFtIKAF2NBu_8z9CzFvecPHwrl0OAVkvSWi39hkxNLdYDSv8XD_9ZVpdYTpOGfG4U7-xvS_D3JzHheJ_Qev2noqA8ey38X-avPgy99KZt8ofCASk64OMy4pdQG5W3BCkjBr7zy1LRE1BuVOGifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
ترکیه - فرانسه؛ جدال پرتنش در قلب استانبول!
[
ترکیه
🇹🇷
🆚
🇫🇷
فرانسه
]
⚽️
ترکیه در خانه با تکیه بر فشار و انتقال سریع می‌تواند فرانسه را تحت فشار بگذارد، اما غیبت چالهان‌اوغلو و ییلدیز روی تعادل تهاجمی میزبان اثر دارد. فرانسه با حضور امباپه، دمبله و اولیسه از نظر کیفیت فردی دست بالاتری دارد، هرچند اولین بازی زیدان و تغییرات ترکیب دفاعی می‌تواند هماهنگی را تحت تأثیر قرار دهد. باتوجه به فرم دو تیم، بازی می‌تواند نزدیک و پرموقعیت باشد.
سناریوی محتمل: گلزنی هر دو تیم و برتری نزدیک فرانسه.
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
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140535" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfMxPowuGdHu4bis8atvJNSzdkxdvc5dbcxyM8_3myfNLQFRnhRYKR_LHPK0rPwDGf4nCwYCZwJ7mzytyMInVZkrRwHqjY3FMljDhXbJlcUuZPmnCq6RrIA08Vp1Q9oXjzeEXTUViOZUk3QXPDkYXb5W0-cu-anorzCai2mhUmFkse7cPZRZL3ed-oxOUBEOUoGkWCUdLC26-ysToyXT4D4gVGbB8u9p5bFVx-fJp0_gYDKbah_WsQDqF-3semkMPgOkKE-shog5QSGSEXBcd2oMk4uKYuLY_z0TzNfp7ViKhs3FYFd5Im_5TAaGnOO1v4xp_gqIABnlBREblIS8KarPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfMxPowuGdHu4bis8atvJNSzdkxdvc5dbcxyM8_3myfNLQFRnhRYKR_LHPK0rPwDGf4nCwYCZwJ7mzytyMInVZkrRwHqjY3FMljDhXbJlcUuZPmnCq6RrIA08Vp1Q9oXjzeEXTUViOZUk3QXPDkYXb5W0-cu-anorzCai2mhUmFkse7cPZRZL3ed-oxOUBEOUoGkWCUdLC26-ysToyXT4D4gVGbB8u9p5bFVx-fJp0_gYDKbah_WsQDqF-3semkMPgOkKE-shog5QSGSEXBcd2oMk4uKYuLY_z0TzNfp7ViKhs3FYFd5Im_5TAaGnOO1v4xp_gqIABnlBREblIS8KarPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
صحبت‌های کنایه‌آمیز توتونچی، مجری برنامه شب‌های فوتبالی به تیم‌ ملی فوتبال: دمتان گرم! در کمتر از 48 ساعت 7 گل از کره شمالی و ازبکستان خوردیم..!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140534" target="_blank">📅 19:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140533" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140532" target="_blank">📅 19:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18169032d.mp4?token=SoWQWG8UQLzSMvkfjKwL9YCYsnCnB9eLr5jnhOlruzidNCu80BfxeXzu9GW0pC7Ffbjf00zJ4crE8W11UMqNKZNR3-8oBrd46m93o6jCoKZcjCuN1Df5M-9_q_tj_c-wzka8i0KjS5tjOozYAB_WpfvbNmsZiGZdwtDOPNdsWRBvKC_mt-CSS-0kekEDp8hQPAnImlePcIx0V4dGiDqNf047bFxEHrsm4EIyZgF8jrBaM0Veg9yIA3yf7bEcIC4XSvZF-jOu-wvuMIQIvthHKd5VdMl0tWzP4rsDCxSpMbMlcw_fbFdnRGuHC38JqTJhnQB6duGK43AN-Da07hPIVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18169032d.mp4?token=SoWQWG8UQLzSMvkfjKwL9YCYsnCnB9eLr5jnhOlruzidNCu80BfxeXzu9GW0pC7Ffbjf00zJ4crE8W11UMqNKZNR3-8oBrd46m93o6jCoKZcjCuN1Df5M-9_q_tj_c-wzka8i0KjS5tjOozYAB_WpfvbNmsZiGZdwtDOPNdsWRBvKC_mt-CSS-0kekEDp8hQPAnImlePcIx0V4dGiDqNf047bFxEHrsm4EIyZgF8jrBaM0Veg9yIA3yf7bEcIC4XSvZF-jOu-wvuMIQIvthHKd5VdMl0tWzP4rsDCxSpMbMlcw_fbFdnRGuHC38JqTJhnQB6duGK43AN-Da07hPIVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140531" target="_blank">📅 19:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
پایان نیمه نخست  بازی دوستانه
✔️
پرسپولیس صفر ـ چادرملو صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140530" target="_blank">📅 19:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140529" target="_blank">📅 17:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_b0P03H5w2FOOZhwD6Y5canlF5Xkx6ocdVl8QapPZ-bGjyhN1mSDD1T-RsLxVvgARQ5GDn2o7VGX9gRNc3LH-HIWo1C4xJcKnlE2wHpJfyf1SEb458e2kbLglg6R5TMuwqA423yJ4NO42DGJ-GmVpmep3e-GdTK9NscwwSOAhSTVbiImlTzSQ45UxT_zjxyd6Uh7bJPZH6gN2EFa67RHgztP4VCeYhbY6EXvjQInXxtA5nC58Kdnto2CpQWE_RKygwmSjhrsPELCqgmq0QxkcY2KykcsPfyQ8r-0Hx2MFH8Y78HdV51clvLwD7HVH8kPpcoYXUjaIJgELBFlx5-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پیمان حدادی که بازی پرسپولیس و چادرملو را در ورزشگاه کاظمی تماشا می‌کرد همزمان بازی تیم فوتبال بانوان پرسپولیس با ملوان رو هم با گوشی دنبال می‌کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140528" target="_blank">📅 17:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdOCJsRLWHPvkGVy_4Sx_d9FZEhIxFxnlfwG-op7R0Gjhiuhks3uImF4jw2BDAwjPFxPOE6As6Wo2ckcRYB35WURx_veuxV5LXUggmYMDzft5m_-FDve4UxnsvgwVX8yCXKU-I8LA-E65S-PwYZqknWfqqcayqb8fmWGruNWL8u9lhho4zj5GiOhSP7_e6Cm7L7VBQPTpXaXpQOawFkX1jjq74ov9C-rFa3XGG1A3o1jgN8eb47znHuV9yLFEcgwFQi3LB7xeiqPVZWkd8iMeAGav5LZK8tWaZkhUAkQwd4_6XhEYNPO8ScXca3nHTQvuD1GsnZG5FBq6xuoDkgwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140527" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
پرسپولیس فردا بعدازظهر در دیداری تدارکاتی به مصاف چادرملوی اردکان می‌رود. با تصمیم کادر فنی دو تیم این بازی پشت درهای بسته برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140526" target="_blank">📅 17:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyxNT7as-zSQ8SKah3Qskmhwte6cS-ysPaaJ4gXmxHGmiUJ0t1k2x-w4hDIjK1roJrJw7emEMR_XQHnKfDfxkRaj1FfNV1S2YAnaM9ZNDAlASG7s8fHl1Y4UbBRr6f03Nwu_Q126Cj4xS8brt7aVeolbahI6Kd9blUwbkRYXx1MejOypRBY2PFGeMh9ISnGC1uGlvrprKANNKxcw44R97UkzhPI9oKp0BcdjZXwI9z6RrSwmmJ5Vbd01cdjThPVTlQ88bcXev_Ut3i2bX_i6QP_n3hqO96KGqv5s3_8e4uj9fohBX9z2bDR0k8GGK78I2Sy_W8kW_U4xc-XJDL6svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با توجه به حذف دیروز امیدها؛
❌
❌
میراثِ قهرمانی «برانکو» با تیم امید در بازی‌های آسیایی بوسان ۲۰۰۲ دست‌نخورده باقی ماند...
❌
❌
این آخرین قهرمانی امیدهای ایران بود و ۲۴ ساله هرگز دیگه هیچ مربی نتونسته تکرارش بکنه تا بزرگی کار برانکوِ کبیر بیشتر به چشم بیاد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140525" target="_blank">📅 15:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140524" target="_blank">📅 15:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
🤩
فرهیختگان: بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140523" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F71u2EOPF3BOnyWT1sNM7F6GzYWxhKSHjUqfhVpXc4d4Xs1_CZgMhHviQu6P2WeNh9Ne5LjBIv2NHVjHyVPfQ2kWN0SCYXyvhyS0OhX4UHzeJPl8PWOEg79Do54frvGPj0pJfc_htQSzU5-VKfRTFEeC1hishPqBbxttxSposo1ZrXnhtuTJGqeXFJkL5VqHdWnW_rhV4N-_BUOY8bsLPkHSwvPgmalrx5NmAVyA5jGw3dLRctbHN3x-TM3PC9f24QSeO2XryRNINFMiqhRjvgRPMdS_m9JufoYwcu9yddGfzFbU6effc-1kmDGarEqtX3YBV8uQNhJ8Yd0SatMVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140522" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140521" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140520" target="_blank">📅 13:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=mEVENvHSE-tI0s37EiQXp39InyWOYL88EMF4G8JAR-QHelStTKuSn5O2p72B3hJuqnPS8ioDE3Rxma7sfhtP9HWHG6ar-nprIWzWyBAQYu_CwX0-Gpwjb_iPYaFpkDdb8TRFba6pD8OO85cwpQRw_J6BG2cG39_4gg9_Q3HLN_YLb3yOHb41F-g6VTxV0HGWStD2jyruZwgCjAixrXmSBSJ-QvqkGMX5ov8DFvKPsvWwGe7FQG4_GGVq-amiS_avE0upe80M5ba2xAgJiTIPXYf-GHCcz2VhHm0RCIuI4tDLdcekmYb5dvOg6lyuBhCDWghbG4LjU4ON-jyit1ZVTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=mEVENvHSE-tI0s37EiQXp39InyWOYL88EMF4G8JAR-QHelStTKuSn5O2p72B3hJuqnPS8ioDE3Rxma7sfhtP9HWHG6ar-nprIWzWyBAQYu_CwX0-Gpwjb_iPYaFpkDdb8TRFba6pD8OO85cwpQRw_J6BG2cG39_4gg9_Q3HLN_YLb3yOHb41F-g6VTxV0HGWStD2jyruZwgCjAixrXmSBSJ-QvqkGMX5ov8DFvKPsvWwGe7FQG4_GGVq-amiS_avE0upe80M5ba2xAgJiTIPXYf-GHCcz2VhHm0RCIuI4tDLdcekmYb5dvOg6lyuBhCDWghbG4LjU4ON-jyit1ZVTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140519" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsS-u5KKUi699-SI3pu2caFM-ck9zngCkJoYRQaB-hYwD201ieudykJD8SsTf_W5Nlt_YcjWtQDL5HcNzl7ec__1QtLoAtNdGOm9ZRouBH6DpV9FQYoDSjtmxCxYABN6Pne6NothEFTF0znwgFceEMS2UWyO8K7Sg3oBK_vOFxRN5MbrCc9jkd_0OQ3ptHicVNkweYgarQrQkXqtNYJuFx1FporcslVRuIgYW-tw0jrEFjMeHKxeF_BfaZN3hmTcXM4RqwYbS7m_trs3GwOK3LsWsNy1vsslHxegXdXsQcJQupm38v4D3bcHbgv4FlfTF_u17qmtUoKaAc-7hi6QRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140518" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140517" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdypnD1WmigIu_vIyzD8YWfaH1_3Qg39FFp44QOxEstBCA_L2OadRSXkfs9cgJd4DPDZkS0-AM4_BZWMQToRndvH_a-jUTcZjos3kuK5HgQvKD0XsGvgUOnKSTTP5GorzITbM9Xc-6lnHUPPfT0YJZ1wNacNb4SHTblnEgWNQSeinITtFs0Dkntw4Ho1GMtMnVsVcA0ZlD2wxHG2jaURZWBMGhLs5ovfKAU-EtcH_glfVi44zZuYZUMBVXnPOJdAgwZh7XKZPAj77ehiQfktSiWmH-NJtrG_Lsee3XCUXS5gbDfJspSbHL8zV89OUX70qKEFvooNYqp95oOorSngFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای
جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/140516" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140515" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140514" target="_blank">📅 11:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚪️
⚪️
⚪️
مهدی تیکدری در غم از دست  دادن دایی خود عزادار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140513" target="_blank">📅 11:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140512" target="_blank">📅 11:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0dc3-mPIMcn1W3romja03uzsQ-7tcWpwELkAYni3JTtjTKpBcfOkwtoeQi6thhNCobRaDlUHyTq8Q4_yo9aWg3h3gf5iYeTGQw7rhI46iAPi-eY_szllCuMZmjm5__kx-dXA_khZ9Ury8suuIO9y8sV8V9DL1SZNDD8lt115T9noXteqLmEfu7PNOe8GL9G31MZaplbJj4AGnGkA2cj1mz3sql8R-f42YM2R2jgMzzwNwGeZEJjOlA-oPQfqemBAaMgnwaVLCEHb3_qeidCDyLbNL9LyFEpA-m6RH2VdcqvIGDKAisrmVsjcwbvVqWFk4LG1FotAiRrtSGalAs8NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال اصرار داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140511" target="_blank">📅 10:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an5oHaKt1NWcrgVRqSXZGI-QZ5RrEnhCToxv-GhRFJadnP360beRvExUwjPxbFdgxLG4N19ILuHeGnj2Wr4SoaPiKLlCx1UyULO51lhOspq000uzD7py1hAZV7GxXmjVJcBaRp6xy0Ux0JBU-vGWzuNwd3YaEsPL2AuZwhHo823WGz5DHQ5istvJ7MItI_QfJ_tKvy4Ggk7Fht9Hk2yrMT19HB1i8M4N5OcLB3TdZU9qeeMRn_jCMk7Lrp7MgBmecbBmJCMf12664WkM1IVniJlCwHoJDwZ6XGbTkmKNZJtu95SLptQycqa9BQ0uXS48RAgKZRCxL6xY9OQ5g9b_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140510" target="_blank">📅 10:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140509" target="_blank">📅 10:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140508" target="_blank">📅 10:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140506">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kggLS8M8iSLRBsQcDw471FwGevmhPF6pEdpwEuXlkAkQzKwFGPgwtWwx5yMMC3aZQWqILTlGu1jJjS21S0ZKeitJuouwwvNaz2CEs0Vijnw0Ep4Te4ckiBpx2mYDdEmkRqgQwHU7EQDtlTipVc9QC01HToMmXIWkkK1xmRhabDV7T286F9z7EI8wtAcdfMyoz4U7pwotrf37dEf5mWgW36C_JKivyyt8M8NR_t6vNH5s4IUU_9G0Gwy2AtqZ7C58VCMFumHUBU9CA8EwO8coWT70mGA8a27DqZfRzvMy0WMcSfFcEZEEdslBsZrhbq4MpEfHuFQSj3ImpP-icbbU8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ITALY -
❤️
BELGIUM
⏰
Tonight 22:15
🏟
Stadio Olimpico
🇪🇺
ایتالیا با بازگشت مانچینی و ترکیبی جوان‌تر، بازی را احتمالاً با مالکیت و فشار از کناره‌ها شروع می‌کند. بلژیک با حضور بازیکنانی مثل دی‌بروینه همچنان در انتقال سریع خطرناک است، اما غیبت تروسار، دوکو و کورتوا روی کیفیت ترکیب اثر دارد. آخرین تقابل رسمی دو تیم با برتری ۱–۰ ایتالیا تمام شد و تقابل قبل‌تر هم ۲–۲ بود؛ بنابراین بازی‌های اخیرشان نزدیک بوده است.
نقطه کلیدی بازی: عملکرد ایتالیا در پرس و کنترل دی‌بروینه مقابل ضدحملات بلژیک؛ احتمالاً جزئیات و توپ‌های دوم تعیین‌کننده خواهند بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140506" target="_blank">📅 01:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140505">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭕️
⭕️
⭕️
فوتبالی: جام حذفی به‌دلیل فشردگی تقویم مسابقات و برنامه تیم ملی و امید برگزار نمی‌شود. سهمیه‌ آسیایی هم بر اساس جدول نهایی لیگ برتر تعیین خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140505" target="_blank">📅 23:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140504">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg8VY_Il1oWyUv-nI4ME_6n_irL_Z1Np2jUrJukclnTaOMJuuWj-F-henjkGMed-l1M0LQrC8d4uAGOw0UVfaTdsBjf-uJv5U_HM2U1IyUaJQTP0MOUR3tyzi98pz7CwPUtdmpGcbxkshUqOSOCjzrdgMQoZPiWd9kEGBCXi8xcWUJ1uc84QUBiU3WvIZgoTZjiVmHGde8CHofuvLJD-xqPnJNVNzBGbf8dHs1mF7SHTvnhgaoYTlv7wgfPmKPctWnsC5bwR17G0-0xUGhv8O0u0BqrpYROfMQZUtB3YU9T062r1mO9n4rs-aEUGOmJZEk7Lvot0so_7VZwe4b-FRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎉
جشن تولد آقاکریم برا محمود خان و آقامهدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140504" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140503">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199c169158.mp4?token=MKKATqDlwFDV5Bi5bNd-6Jcj1yzUl_lC8P8WXnMPd2Wzq2wQW7u9puEhAprBQ5qc1M5wviLrzA_ClJzQ8GaflmnHsRzjoWnGG2mIfiq9Krxiaq9ITrwCGlZ7kLO4oO4ZKZIFB2vEtEijGbTFUn00Zu8E0_z-UwqEq-K3W4nXZGc7RPpsxwauPZEnXoxyDhUlnIQn6w1AKEA_uZtj_7bD82vjYeT1v7Hu0CuO3IklzmY0kSQ8I_kZviY-lAiWUv2EUf7lac7S0yTzxeVf9aQ0uRLOSBTxO4N1SPWnAjy_hoWMnNdtZNEKTGjvTstHmb9Iuq8bdE_Suymmi0r3-Mn6CnNFZp5U62l64NJsJiMXdK5jEgAQVMjf3SCpXjcArah8AT24dde3FcrDoRQrAd5qQ8b66G1_UlYIL40z-C9ffJUSe1UHIFwQf7QVnVqMa7rm_dlQi50xpk8_Qgx6YibHSH-3QRmP7jp_RFMmStKnoF5afbDfR-ujqLId8mEo6XT6C6g2ea2W1U5at1tnK3-4J0rTc2fFhOHhBcNd7VgcynCcFJ-VGgcIpnxnul52gE98Yc6jUqnQix4XONg3KhKyglGx_UDKQoL-8IdYcRWxYHuOwYvkedViXc3KaqbLocZrHPz2KKc2wOneNYK3sjbBEOTo3KHpx8qg6oLBqkbwkBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199c169158.mp4?token=MKKATqDlwFDV5Bi5bNd-6Jcj1yzUl_lC8P8WXnMPd2Wzq2wQW7u9puEhAprBQ5qc1M5wviLrzA_ClJzQ8GaflmnHsRzjoWnGG2mIfiq9Krxiaq9ITrwCGlZ7kLO4oO4ZKZIFB2vEtEijGbTFUn00Zu8E0_z-UwqEq-K3W4nXZGc7RPpsxwauPZEnXoxyDhUlnIQn6w1AKEA_uZtj_7bD82vjYeT1v7Hu0CuO3IklzmY0kSQ8I_kZviY-lAiWUv2EUf7lac7S0yTzxeVf9aQ0uRLOSBTxO4N1SPWnAjy_hoWMnNdtZNEKTGjvTstHmb9Iuq8bdE_Suymmi0r3-Mn6CnNFZp5U62l64NJsJiMXdK5jEgAQVMjf3SCpXjcArah8AT24dde3FcrDoRQrAd5qQ8b66G1_UlYIL40z-C9ffJUSe1UHIFwQf7QVnVqMa7rm_dlQi50xpk8_Qgx6YibHSH-3QRmP7jp_RFMmStKnoF5afbDfR-ujqLId8mEo6XT6C6g2ea2W1U5at1tnK3-4J0rTc2fFhOHhBcNd7VgcynCcFJ-VGgcIpnxnul52gE98Yc6jUqnQix4XONg3KhKyglGx_UDKQoL-8IdYcRWxYHuOwYvkedViXc3KaqbLocZrHPz2KKc2wOneNYK3sjbBEOTo3KHpx8qg6oLBqkbwkBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر جا رفتیم اوت شدیم؛
🎙
درخشان: مشکل، ساختار فوتبال ماست
🟢
سال‌هاست فوتبال ما به قهقرا رفته است
🟢
آیا لژیونرها فوتبال ما را ارتقا داده‌اند؟
🟢
بی رو در بایستی ما فقر فرهنگی فوتبال داریم
🟢
ساختن 10 برابر نیرو، بیشتر از تخریب می‌خواهید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140503" target="_blank">📅 22:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140502">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=vcx3i966jmfOkQc76b6vtSC0wKGR4r2XwYgg8TJttYY-FI7AZDGLNAv8EeTEmUvFZ9XzVTc-PZivf1AoLW-sJvZqwumuBffA9GaJH7CEZOk_eUMLOCSPfsuunl067PzLFEAUFsXT6B5C4iWq_tPt3fzy-OoKYbySiUtzPs3yGfbLIXKNob0clBN30Vi_x-9FAZy0MPvmNbJmpyOmqprFoNG1BoKpGPMwu-CY3o9JM4C6naXQN3MBFr3XBeGLeBlx3a2pmlVGpORidpjs8kuGpAXaq4aTjQm5-YXcUn6s2H9n9_cVpVIAxXbXGbBIxn8-RNahW7vxh7K0k31U8yLStxqjwoONQhVe8rCi1-dSlOxRuST2MgeaK1ki-JvlRk90-U4np7xSCZHCtRPtRdMzmJI4XEhNkGOqrb1eZGgsnGhDMa-eS6V6zG2EYd0WSZzayJssGvdbKagRkRg2lOnbVYlxGipg_STUl3FVnYPEL-dx5CiVvklcRn4e3LTw_RB46nXYrIucKFUSu2y4SUjL7UycKyGX8vhnaoqtvR6r89Mym6Uav77p-4vd09YnGBDAUtPBN3TrrLGlI6QLaETT4xekDMI4zychiOD5wckVKNguwOQSUCs6oIrQIFarIpCKvRQ1vH8VDd9LM0G8GZl6Xws_qab66eBf-D31va7TkIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=vcx3i966jmfOkQc76b6vtSC0wKGR4r2XwYgg8TJttYY-FI7AZDGLNAv8EeTEmUvFZ9XzVTc-PZivf1AoLW-sJvZqwumuBffA9GaJH7CEZOk_eUMLOCSPfsuunl067PzLFEAUFsXT6B5C4iWq_tPt3fzy-OoKYbySiUtzPs3yGfbLIXKNob0clBN30Vi_x-9FAZy0MPvmNbJmpyOmqprFoNG1BoKpGPMwu-CY3o9JM4C6naXQN3MBFr3XBeGLeBlx3a2pmlVGpORidpjs8kuGpAXaq4aTjQm5-YXcUn6s2H9n9_cVpVIAxXbXGbBIxn8-RNahW7vxh7K0k31U8yLStxqjwoONQhVe8rCi1-dSlOxRuST2MgeaK1ki-JvlRk90-U4np7xSCZHCtRPtRdMzmJI4XEhNkGOqrb1eZGgsnGhDMa-eS6V6zG2EYd0WSZzayJssGvdbKagRkRg2lOnbVYlxGipg_STUl3FVnYPEL-dx5CiVvklcRn4e3LTw_RB46nXYrIucKFUSu2y4SUjL7UycKyGX8vhnaoqtvR6r89Mym6Uav77p-4vd09YnGBDAUtPBN3TrrLGlI6QLaETT4xekDMI4zychiOD5wckVKNguwOQSUCs6oIrQIFarIpCKvRQ1vH8VDd9LM0G8GZl6Xws_qab66eBf-D31va7TkIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
نتانیاهو تقریبا برای یک سالن خالی سخنرانی کرد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140502" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140501">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
حین سخنرانی پزشکیان، نماینده‌های: ایالات متحده آمریکا ، بریتانیا ، آلمان ، فرانسه ، اسرائیل ، سوریه ، لبنان ، عربستان ، مصر ، امارات ، الجزایر ، لهستان ، سوئد ، دانمارک ، کانادا ، ژاپن ، جمهوری آذربایجان , مالزی ، نیوزیلند ، استرالیا ، جمهوری خلق کنگو ،…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140501" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140500" target="_blank">📅 22:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140499">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
#فوروووووی
❌
با اعلام حدادی جام حذفی برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140499" target="_blank">📅 21:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140498">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=P7qfokm5VwAORng06fukKEPQF1GUSeJI3JH9ckkNcdOymnooCy22mL9A6CcBHSkhkbqQq8IlXdlNWcyZ_wLEdE-c992lMRABX5Fa2J_Ktd7cWDbPi8qCv187uZGaw9dVda9JL1uPZf0V5kkZ1gT5MCvjRlQlLmPDtgUslrX7emzUM-pPeyGzJ0RpWdXDyGuuH7ggLpkjwj2KH7bA7yRo5-sAkkUgVtz9ks35ntivgNOhoWZY-1MfqKl9f6CxFfCt3-h7MRD8u2A29lQlb-xjuzQAxKEXXgl7kbVPuAcnF0n_7xJbRB8MWhMEfT4D54m1NqpCJSPThfMEbviuJQbp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=P7qfokm5VwAORng06fukKEPQF1GUSeJI3JH9ckkNcdOymnooCy22mL9A6CcBHSkhkbqQq8IlXdlNWcyZ_wLEdE-c992lMRABX5Fa2J_Ktd7cWDbPi8qCv187uZGaw9dVda9JL1uPZf0V5kkZ1gT5MCvjRlQlLmPDtgUslrX7emzUM-pPeyGzJ0RpWdXDyGuuH7ggLpkjwj2KH7bA7yRo5-sAkkUgVtz9ks35ntivgNOhoWZY-1MfqKl9f6CxFfCt3-h7MRD8u2A29lQlb-xjuzQAxKEXXgl7kbVPuAcnF0n_7xJbRB8MWhMEfT4D54m1NqpCJSPThfMEbviuJQbp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/140498" target="_blank">📅 20:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140497">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpN4CaBgdBJt-lEXFENupOf3Ou9TFmEwH7RmqmObFFtQWyNJUoS7V0HijvVgURq5TE7yRBUGZLoh3g6kvehIPylyMfxskABPBuZ27o56IVTb5f_l3tqsvcbIP3OEzRkZq7ohteIQ-AclF7GxGwWKxno12spebwoWQsl48It_jwiZnzJcqvlgwSVYPu7fuNck9ETWEiWPICqvFYn_gxW0FEOvE-OfzhkfXuuO4zuMpzAanPuuf-wF8n-sCp5W4QTPrd7IV_vpoSbkAHQx0k-pWqXPmFXZwoeKPpbWYEdJVx3TzVzzVzINY5p8M-zK-PydnJsJz_zx4XNdAmP_wbBNZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140497" target="_blank">📅 20:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140496">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=Acn9-IZOuWcFDUvBvVP3F8yEWQF5oVnyyiyu94biNCpWbuSJKnMUHZJsn3BPMwB-MVcrTymevMBJnp4J8ivyK6vthuxInCqV2WublhM6CsxBwoJ8l-gSH_c4hukRF1C5yYdKiEI-MOXdJBDx1cnnc9fRtM8wLX-0LoCVp4h64jl3lK9ZaHFQameeDrlrfSYUi345NpXhFtmp56cHogsVoq0AsYMSISqYeELTgROoUKZAolprulLg9GvBfqcbsmYLazH5ix9b6w3wDzfvtDSDZT5Suph3U-S8cTPGCqW-11mDlfH0GshaWHvy3llxkXs-bFktEkNXGNGUJPcYfEedhJL-hO3OG8dUE4txlOFFj29jj05pWSccHUOskSUrsJRlNqg55U-kS72jjwOzanWzSxRswOz7jUn4A8UN_rzixcOzhu0TWOkyA6Fx4Nx9RJvwUDLbfpquDlZIgM04U_02Mxr1i-5NRxS2hPTeZiymxUR5X2wuUGnVEgsHG-NyVb7fvxijBu9TDPfK5EyrpBm2xKeyqkNXYVudtYC8lrO76Xf-mRt7ucRS6jAyQmRDI38152MloNjehoqRr5m7iweVsk_4d-hlADNLAUilXY82dESEpYqe5EmZIbz7ijDgNihOP2ZWz37wdYqKphAR0OcljHVMaliFcjiid51Vv4A2JXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=Acn9-IZOuWcFDUvBvVP3F8yEWQF5oVnyyiyu94biNCpWbuSJKnMUHZJsn3BPMwB-MVcrTymevMBJnp4J8ivyK6vthuxInCqV2WublhM6CsxBwoJ8l-gSH_c4hukRF1C5yYdKiEI-MOXdJBDx1cnnc9fRtM8wLX-0LoCVp4h64jl3lK9ZaHFQameeDrlrfSYUi345NpXhFtmp56cHogsVoq0AsYMSISqYeELTgROoUKZAolprulLg9GvBfqcbsmYLazH5ix9b6w3wDzfvtDSDZT5Suph3U-S8cTPGCqW-11mDlfH0GshaWHvy3llxkXs-bFktEkNXGNGUJPcYfEedhJL-hO3OG8dUE4txlOFFj29jj05pWSccHUOskSUrsJRlNqg55U-kS72jjwOzanWzSxRswOz7jUn4A8UN_rzixcOzhu0TWOkyA6Fx4Nx9RJvwUDLbfpquDlZIgM04U_02Mxr1i-5NRxS2hPTeZiymxUR5X2wuUGnVEgsHG-NyVb7fvxijBu9TDPfK5EyrpBm2xKeyqkNXYVudtYC8lrO76Xf-mRt7ucRS6jAyQmRDI38152MloNjehoqRr5m7iweVsk_4d-hlADNLAUilXY82dESEpYqe5EmZIbz7ijDgNihOP2ZWz37wdYqKphAR0OcljHVMaliFcjiid51Vv4A2JXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140496" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140495">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=B2pd5h2XdwNCAZ3SesDwDfJpT0LFrdE9BfedGFoozBmvtOLUM4q7nnwhgM1jZsWOi9z3leZqtQzguKP4DVAoug9bwM-ZpQrhGuKmZpIWDoAP2555pZvebfNYuoB8bvaeNJ5ffxsGj0SVhinbRAD4S1ccHi5-yUAp0tUOisVlRkwAcduuvEQiskb8w_PTUGqcsttJjauDaLPBQufz4YHUp4JFAYhzR56G3fz2wfzQnXHahVHSI9qXErXq1-Avb-InCMiWg93ByXZh7uE7vLkL-pMFdKC1KDJvmdfYc7PMRuFxbdfQQnVgmHeWW8j4itwrLny_neAy6Ssf_PARN_716EBa1Y5rznoi8S66977DhXF0k4eOPD-Ck3M9FaVqpAWMRXwjkD4PCaIjvusfKTPYYexDSENNwY_8nECtIBBKadbJwLpSRjxPq25SI1IA6SRgc_75LCjeKPZjOPP0aLAOl8zewoOOh6t6DUUtcCFceTCT0ftvT-10QU01hJtAlom_DvZdC5EAN_Xo3hAXHpaqv0PplHhcmwpbBPXohsuBKUff9E6yQVkhaQnD75V26goyqdxqUUJGAouGwqKe2r4shOX9YMLFMl4zje0aMTYAg-uPa6kL0e5RMiA-N1vVSBse6Bkbj5i4LFXWECCpI8FsjQF1g1fUP2P0NV6nXPwaNmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=B2pd5h2XdwNCAZ3SesDwDfJpT0LFrdE9BfedGFoozBmvtOLUM4q7nnwhgM1jZsWOi9z3leZqtQzguKP4DVAoug9bwM-ZpQrhGuKmZpIWDoAP2555pZvebfNYuoB8bvaeNJ5ffxsGj0SVhinbRAD4S1ccHi5-yUAp0tUOisVlRkwAcduuvEQiskb8w_PTUGqcsttJjauDaLPBQufz4YHUp4JFAYhzR56G3fz2wfzQnXHahVHSI9qXErXq1-Avb-InCMiWg93ByXZh7uE7vLkL-pMFdKC1KDJvmdfYc7PMRuFxbdfQQnVgmHeWW8j4itwrLny_neAy6Ssf_PARN_716EBa1Y5rznoi8S66977DhXF0k4eOPD-Ck3M9FaVqpAWMRXwjkD4PCaIjvusfKTPYYexDSENNwY_8nECtIBBKadbJwLpSRjxPq25SI1IA6SRgc_75LCjeKPZjOPP0aLAOl8zewoOOh6t6DUUtcCFceTCT0ftvT-10QU01hJtAlom_DvZdC5EAN_Xo3hAXHpaqv0PplHhcmwpbBPXohsuBKUff9E6yQVkhaQnD75V26goyqdxqUUJGAouGwqKe2r4shOX9YMLFMl4zje0aMTYAg-uPa6kL0e5RMiA-N1vVSBse6Bkbj5i4LFXWECCpI8FsjQF1g1fUP2P0NV6nXPwaNmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💛
🎙
حمله جواد خیابانی به امیر قلعه‌نویی: باید چیکار کنیم که کادرفنی تیم ملی تغییر کنه؟ نتیجه افتضاحی بود. آقای قلعه‌نویی نمیتونی تیم رو جمع کنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140495" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=RkdyGjFauAHpVTWcTZBv3G0jxBHSFxDN66bHjL22sYMuI5k51P-Cxha_dovj6hV794A9IpNrWtslPJDzI74Mj1p4agnaJSasU6L_pxnPomDBE_TbNyJmJinSi7fv9dbhj0gPgkpbpZ739OQzpQCayJjMqZtQxbdkkzO5USobeUxEPKMd_JK78Bh4USY_pkeLy9-ZNPFdJA61rovHcVVyxplGUY49LRaRO9YuQ1f_fg6SVIoMba02XJA1ZXAdyBn0GVkXzVWoL1vO5WNaL12-G731sjEv07MByM-GomBWJaou09BN8JzpA0U-RrFfRWglLqWKe6KpsqU7NH9gXXcVzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=RkdyGjFauAHpVTWcTZBv3G0jxBHSFxDN66bHjL22sYMuI5k51P-Cxha_dovj6hV794A9IpNrWtslPJDzI74Mj1p4agnaJSasU6L_pxnPomDBE_TbNyJmJinSi7fv9dbhj0gPgkpbpZ739OQzpQCayJjMqZtQxbdkkzO5USobeUxEPKMd_JK78Bh4USY_pkeLy9-ZNPFdJA61rovHcVVyxplGUY49LRaRO9YuQ1f_fg6SVIoMba02XJA1ZXAdyBn0GVkXzVWoL1vO5WNaL12-G731sjEv07MByM-GomBWJaou09BN8JzpA0U-RrFfRWglLqWKe6KpsqU7NH9gXXcVzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💚
حمله شدید خیابانی به تیم ملی امید و کنایه به قلعه‌نویی: بازیکنان کره‌شمالی نه مدل مو داشتن نه قیافه آنچنانی می‌گرفتن ولی اومدن مارو درب و داغون کردن، بازیکنان ما چی یکیشون 20 میلیارد میگیره یکیشون 800 میلیارد میگیره اما دوهزار بازی نمیکنند و تحقیر میشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140494" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140493">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5kf_XmlyHv74pCy1mlXl3Wvi-LwUG_NHTCuv-wPuTyDmPojeM_rdvkExj71EW6S3iLiNQGNBpDl9Mj97KzqAloH_rH6ZUoNT1dLgpbcjP0dfV8kdzB5Jg75CodAkEUt5c9kirgn0dGeJ-FdQKfyf5N5Jn8EJVhDvjIAuiP3ZBPzdG1LJpSI6fpHNFeGX15QQvXMjwkwsYVHlP0ENCPmpPnsAcQOiaRmXuefJ8-NVaM7xAWBm8TycymuK2hyltTuaCHNRwGLfvOB8uVZ4dbOV3N0Dj0O-T4a-8gp88jLUwRMiqCgyWqMWZDiNPC3Eb1wdJQp9M_tnKD5TuCOatPElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Netherlands -
🇩🇪
Germany
⏰
Tonight 22:15
🏟
Johan Cruijff Arena
⚽️
آلمان و هلند در شروع لیگ ملت‌های ۲۰۲۶/۲۷؛ دیداری که از نظر آماری کاملاً نزدیک است. هلند در ۱۰ بازی اخیر میانگین ۲.۲ گل زده و ۱.۹ گل خورده داشته، در حالی‌که آلمان ۲.۴ گل زده و فقط ۱.۲ گل خورده است. در تقابل‌های اخیر هم آلمان دست بالاتر را داشته؛ ۳ برد و ۳ تساوی در ۷ رویارویی اخیر و آخرین بازی دو تیم با برتری ۱-۰ آلمان تمام شده است. از نظر روند گلزنی، هر دو تیم پتانسیل بالایی برای گل دارند؛ ضمن اینکه تغییر سرمربی در هر دو تیم، یعنی نخستین بازی رسمی یورگن کلوپ و ژاوی، می‌تواند بازی را از نظر تاکتیکی غیرقابل‌پیش‌بینی‌تر کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140493" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140492" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
دو گل خوردیم .اونم آقایون شجاع و بیرانوند تقدیم کردن و دوتنه تیم ملی و نابود کردن   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140491" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚡️
⚡️
⚡️
عالیشاه از دو سه سال قبل با خانومش هست، مثل کریس و جورجینا و حالا امشب عروسی میکنن، قرار نیست اتفاق خاصی بیفته، عروسی صرفا یه جشنه و قبلا با عقد رسمی شدن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140490" target="_blank">📅 19:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
این بازی ساعت 17/30 انجام میشه و بلاخره روی ماه اقای درگاهی رو میبینیم ...ببینیم چه جور بازیکنی هست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140489" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
✅
✅
با اعلام باشگاه دوا یونایتد بانتن اندونزی، اوسمار ویرا هدایت این تیم را برعده گرفت
❌
این تیم فصل گذشته در لیگ اندونزی هفتم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140488" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
سعید الهویی : قائدی چون گفت بهترین مربی هایی که باهاشون کرده مجیدی و استراماچونی هستن دعوت نشده تیم ملی
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140487" target="_blank">📅 16:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
ترکیب ایران مقابل ازبکستان اعلام شد
⏺
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس درگاهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140486" target="_blank">📅 16:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140485" target="_blank">📅 16:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
مهدی ترابی بازیکن32ساله باشگاه تراکتور که دچارپارگی رباط‌صلیبی شد هفته آینده پای مصدومش رو به تیغ جراحان خواهد سپرد و تا اوایل اردیبهشت ماه سال بعد دور از میادین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140484" target="_blank">📅 16:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140483" target="_blank">📅 16:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140482" target="_blank">📅 16:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140481">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
گفته میشه عربستان و چند کشور منطقه دنبال فشار به فیفا برای تعلیق فوتبال ایران هستن؛ اتفاقی که می‌تونه باعث حذف تیم ملی از جام ملت‌های آسیا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/140481" target="_blank">📅 13:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140480">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adJqxZrp85LFxNJk6pvMBvJKmuQFwRBJGMGvfLlU410RSDBRxl2F4g_OZRJ0ulKiFQRrNm_1RtFdRmZEP8hxrkmBsGqt7m6Sgnhhm2Nu2Lm7EBfNiz2AZSc-8g62Aw8J_82s8fd68S7PXRGVkHOIf7ERTlMlK9E2BDCaL-EEt4w46S5rHOgwcPbwHmPAOPQHPkyceS1Mx81f3QzjPWnTTTft7oWKk-2HCuPBzF5FkJAmCcRZ3zP9XTpSUoG83qpnz3YD6qgyb7b6Jyr5udiEr3hOn0OJHaGPe6FSNwOCJ6VPdJqRJRxlbZEh4OrIqoNHkcIVjCFqJeg9StffEZX8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140480" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140479">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzYjprZMe_Hjx-4jY8KKsFA4Q2jRu-TBJ3e_1HzwUVbOLocBjTVpbDK3AJwfKi5TErm1QeTRbXQKhSvdezNAdcz3d7wBarGH_n_Kn9pbant-pvKXr2jLHj5AWk7yjZpYvkgdhi3HbWRYCiVltCWhjrSt1Yyfbx_GaF0oZTk8Uk8Z-fFUXUllv94F-RS2D4c5wVmlH9mPdLuOm0zEzjY0aOfDnOBc_fm8oXQq5gWo87kQ3sak-DNRUxfu3mA60QUEPaBjXgVcHkCxKSA6FlP2E4Y4qsMNVvuyRD9C4iX-TF8d3LxGpYEFXGyg4lZNmeIOh4pL-FVtPV802NRm4E4Klg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
از ریفوی ژاپن تا لیسبون؛ شبِ دوئل‌های حساس
ملی
🔥
⚽️
فوتبال امروز با دیدار ژاپن و اروگوئه شروع می‌شود و در ادامه، ایران وارد یکی از متعادل‌ترین بازی‌های روز مقابل ازبکستان خواهد شد.
هلند با آلمان و صربستان با یونان از دوئل‌هایی هستند که فاصله تیم‌ها در ضرایب هم کاملاً نزدیک است. در سوی دیگر، نروژ مقابل دانمارک و پرتغال مقابل ولز؛ جایی که پرتغال با ضریب ۱.۲۰ واضح‌ترین برتری این جدول را دارد. یک روز پر از بازی‌های نزدیک، ضریب‌های متنوع و چند تقابل که نتیجه‌شان می‌تواند جذاب باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140479" target="_blank">📅 12:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140478">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
✔️
بیرانوند برای فرار از سربازی، این‌بار به بهانه خالکوبی، دست به دامن کمیسیون اعصاب و روان شده تا شاید با برچسب اختلال روحی، کارت معافیت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140478" target="_blank">📅 12:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140477">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
چمن شماره ۳ آزادی به مشکل خورد!
❌
❌
بعد از دو سال تمرین پرسپولیس در این زمین، چمن سفت و نامناسب شده و قراره به‌زودی زیر کشت بره. احتمالاً سرخ‌ها چند ماه آینده تمریناتشون رو در شهید کاظمی و زمین شماره ۲ آزادی برگزار می‌کنن.  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140477" target="_blank">📅 12:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140476">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140476" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140475">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFV6gLqUVagDgk9RzEQ7_-FwbKxWcfat2fTKktyHEe57lrOv0WzQt-f4y9RFUh-ItTGZJIVvXdLyfaFbr3zfI8f5ZX6qOTfNgDP_4T-sH9GHCiPunWFWB6_z8vUk4oskPK8fBIYXW-CV88FwxvWBvtTcmZaUS3Qdogc_PjV_AH0CZv_6MMEjglZXNDmRN6E7xU2Vf82CnGJGL1kkzlueKOyUyu16JF0e9VgHUC0Mf2XFWg-HjPWAAYakd_smtQ3hXF1UxlYVFHTVdFNt3I7khlYT9bl6QlEAstdQr0C4dbatbdCunhBvWHZSKjBsidQQVDjxLaeuv8CLXGdud0JQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
| طرفداری:
🔴
⏳
🔄
تارتار اصرار به جذب رزاق‌پور دارد و ولکن این بازیکن نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140475" target="_blank">📅 11:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140474">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی : کمیته انضباطی به باشگاه گفته مدارک شما برای محکوم کردن آسانی کمه و اون چیزی که ما نیاز داریم ندارید.. که یکدفعه باشگاه مدرک جدید و آس رو کرده و فدراسیون آچمز شده و هنگ کرده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140474" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
