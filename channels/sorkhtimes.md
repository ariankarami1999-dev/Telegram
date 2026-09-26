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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 16:46:03</div>
<hr>

<div class="tg-post" id="msg-140570">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_AyaFp9-t2D3tPxWX62E-Do4kT2NnOrsnd2vfFGZw261KVejjoshli0SihNhJ1-XFgCtnvrYiHAhmA3BDQsiKxG94F1lYj7c03SxnrAPcRStP1B_bClV1gbRG51GD9WjWOY2pM0bteGWDV0S8gFyoDPqUnH67jnNL3zJeIdHdVK3TZjz6VpfkqIivoHjg6-W8POhM7qJPD5kg20bBu3S4BhfbjGhwm2Y7C3V9WNM2NAFGWgRduhWj5cgQJ2sTmkQHb9-jDxgwDfNbRmQJiTEaaMVSxQPHdFoVC6pu61_d8VtZxJEKEn5CeAlgLBT1CnlDgr95Dme-mCYdmxi8Umlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از بدنسازی امروز پرسپولیس؛ شاگردان تارتار فردا استراحت خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 183 · <a href="https://t.me/SorkhTimes/140570" target="_blank">📅 16:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140569">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 245 · <a href="https://t.me/SorkhTimes/140569" target="_blank">📅 16:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140568">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🔴
فوری؛
معافیت علیرضا بیرانوند از اعزام به خدمت سربازی، ۱ ماه دیگر تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SorkhTimes/140568" target="_blank">📅 15:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140567">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SorkhTimes/140567" target="_blank">📅 15:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140560">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/140560" target="_blank">📅 14:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140559">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEBu0rjJLzOzu3QhltTvMfxwAA4cY4LuEexJXYGGGIpdjlvHUPt_CSYJQQtcfqglv556sq9Hwk_-8q1dLaJPpp8tlOBnMa9ZHsHW7nfIkNyL0FPTfsZ1faV8lWZnnAiy4D12Zq_BdHkRScxhmv1vX9qBvrr7HTSpQ7Phbmm988ME4UyTpkb03v1VR8CFHaDc23XLdghkBBGNqWwY6XODdGH4UqJJxN30sPHl37hPAIX301pZdrBixHeCyBMPsuAjPoEsD3rSq35pBJKlva7kEeSCeyKM4WAsSlY7ftTqy9_SjwuaSHnL_FXJzz3MqPUo0i-yfCbdXxtNAL2pDf26Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم قلعه‌نویی واقعا عجیبه!
❌
بازیکنی که از جام جهانی خط میزنه رو کاپیتان میکنه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/140559" target="_blank">📅 14:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140558">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⚡️
⚡️
تاج اعلام کرد امسال دیگه سقف بودجه وجود نداره، اما فیرپلی مالی اجرا می‌شه.
⚖️
طبق این قانون، باشگاه‌ها باید قرارداد بازیکنا و هزینه‌هاشون رو منتشر کنن و اگه این کار رو نکنن، سازمان لیگ خودش منتشرشون می‌کنه. همچنین باشگاه‌های زیان‌ده فصل بعد با محدودیت…</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/140558" target="_blank">📅 13:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140557">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
فوتبالی:
✔️
✔️
گفته می‌شود فدراسیون برای جانشینی عبدی با گزینه‌هایی مثل فرهاد مجیدی و مجتبی حسینی وارد مذاکره شده و باید دید در نهایت چه کسی هدایت تیم امید را برعهده می‌گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/140557" target="_blank">📅 13:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140556">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/140556" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140555">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/140555" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140554">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/140554" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140553">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/140553" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140552">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
❌
سه وکیل خارجی باشگاه بعد از دیدن مدارک جدید در پرونده آسانی اعلام کردن، درصد پیروزی پرسپولیس تو پرونده زیاده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/140552" target="_blank">📅 09:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140551">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQKvWrwWgEMNU9C8aqN80_lAm1BY7FzNKNM9wsmQmvprjK9k3f1xOcy2F2Unyg7JnYpQcAaNlX8jCxFMFG3x2bXCQPlbBvQwxFlJkZ06wqMy7vzocWUD09ZlPu8kw323CqTEONYXH2DUFAbDtL8m_b3QI3qIqmdVrIlj2hhGc0ZV0xZ6VsUbZgz9Q7q9SdwJu4UQKh04oIaZJYEB9Uc45oq34NyuceZUWf2TbONYiLHDt7CAtPyW2GEt0SsFfTpgLtc-DzYlLboV-wvcpt6eE938BP3BSh2qk5oC2dNYSEiXGI3cBWHZBsdn1YnbjHBTBATmHdZOSBBTDncnnkCv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/140551" target="_blank">📅 09:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140550">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140550" target="_blank">📅 01:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140549">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140549" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140548">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGWuBJOSh4B-f6A3iImAu-iGOvtp7CXMI1qDWyLEBJWe1HjYdbNwDP5mymvNZTmS6OwrUPs4b5Wz7xT6eRcvdICgylRdEtXUiTGAzXJv5aNlFeoNgXNbZJOvw5cgAVSfIGmSRjXrEg6fv-DaY55_hhmRwBsBhzmD5o6LgC_sna7dui3gu954KpNYJ6awRJZlQ2p0K2r1eujHBNSkL2jxjZaafCLZNfLmGMMqUtoHVC42pdNZGI4CVkKyIp7bjoJ3_rRF5Hjwg1wS_gcN5KQZjb9RWFWm5J35coxN5iBKUWx06CUmnBaATzvOOVtZEbD5J1DmmhQdSZHlcGDGlWVXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نتایج هفته دوم لیگ برتر بانوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140548" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140547">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140547" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140546">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpEu0j2WnzQZatAmA_jw0T2ZkQaqLQaZJaZIs-IMerye-5ylFsA9CMbLr276hnEPVHpqfZiuEfk1QCllyww44hr5OoPG3cW3bxLdppVlboSkc2H6ExVcDyJdCVilX5_NEne9k4AMJAVKFK5m-kmjhvNSCuX1fgA7e84dI9zSbRSLZ_AnqKC1amKraKK5ZVb3NbFvAB4uj59iShTPXRQIqyq4Qv2kpISByLOgY1Naaqyju7sYRy86BLddJ82Vo29_LwhtQPzRFhAHVz4W443vtM4asJPYIdfYB4tB1h4uSXz6-Fs3ccpG7w3dRlGbp5fBRF_5FG0qndyQsRRwZOww7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم.
/فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140546" target="_blank">📅 23:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140545">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
نتایج ۲۰ بازی اخیر ایران با قلعه نویی ؛ ۸ برد - ۷ مساوی - ۵ باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140545" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140544">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140544" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140543">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭕️
👀
صدای پای اسکوچیچ به گوش می‌رسد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140543" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140542">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
چیت ساز، معاون وزارت ارتباطات :
🗣
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
✔️
✔️
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140542" target="_blank">📅 23:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140541">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای  جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140541" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140540">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140540" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140539">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeDcdfPp3doXZwDJ1OalD5uZUne9obUHCeZVmmVqEFOfRlkM4Y35b8XpS9yQiUFiYtyINaOoXaAziPuYRvDpN9CwslILh1ThSfoLy5v86BnCjMmcdXJsFAJ9HegExS-PiDgXIecw1eAk6eWxSxChD2w9EQCWPTPwdu82USngUXxXoNUYIDprx789_nIZbshd6FAjjA24ZrDsQMclhVDjgcVUo6c63tOiewh4aJb5ZqpnhsEUF0v1Kn1oS-Bk_fnHy8pc2INML4iWlwjf0cnU6Y3SQq2A-ffJJeFaa1h_urAnom0Pd1fb5_8U_mnFBf0fE-K48PPk7dxP1zkrOzvLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تولد مهدی تارتار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140539" target="_blank">📅 21:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140538">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
مهدی تارتار با بازگشت میلادمحمدی مخالفت کرد/تارتار همچنان رزاق پور را میخواهد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140538" target="_blank">📅 21:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140537">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140537" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140536">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140536" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140535">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsk4D9cYZ9Ce-26zH5V8yGI3AVv3qOe-SP8Z6egUxujjiEdfukpjs3f58QkyHIRVw1izT0YbdlddNCoM2PEVdFjsr3DkrpnHjqh0AZl_0Yf1E9TgsKxudFAlWgVHC8T9FcGlAeT8TRzvmG38njMsyrY3eHrSYgADnwdPz7ug4U1xCZdbpJT6V4PLCgrWmbb6LA0hGz8QLzrA6LbBOaUVKSPvZCUOs_9So75MOYBRgN5-o91GTu1UxelK9SMbg2DUFJipSE1PZxrgAUU8Lm74WzF0ziX8aX4umRS2lkZK-HADnaUMg_KbtgXP6C6HVp5H2JWyYgK16li7o6Gum5g4ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140535" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140534">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfM72bhP-94jCi4NQuPS0K4GvMwyxcGCsDFJ0fo7ZZy38Ijkd7Nc8puSrDCAVPec4kDqwlkElo0i4r9LUe6V9OKUC977wUG3zvaWiDn5i45gOO5W-G_1Qz5WRpZWh0sRMhWpTwlEaqYNyXSGgmFIu2WM_fP_WLkiT2L3KlAcCUMAu1cS1Fb9Lx3LlWzgcJUVvJbxBUYei635fRL4ZKPturu19cu3Kht7rMa_hU95D8YcbJ_Zk63kEJPAUaMXR_p27FtUhNs22c1urwv9PtMlXJoXz26NBJ1RFA0D_hvI_gtaZw2xQLlFt91H97t5TJoKFHbyu76GiT5AKg7Z98gRmDAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfM72bhP-94jCi4NQuPS0K4GvMwyxcGCsDFJ0fo7ZZy38Ijkd7Nc8puSrDCAVPec4kDqwlkElo0i4r9LUe6V9OKUC977wUG3zvaWiDn5i45gOO5W-G_1Qz5WRpZWh0sRMhWpTwlEaqYNyXSGgmFIu2WM_fP_WLkiT2L3KlAcCUMAu1cS1Fb9Lx3LlWzgcJUVvJbxBUYei635fRL4ZKPturu19cu3Kht7rMa_hU95D8YcbJ_Zk63kEJPAUaMXR_p27FtUhNs22c1urwv9PtMlXJoXz26NBJ1RFA0D_hvI_gtaZw2xQLlFt91H97t5TJoKFHbyu76GiT5AKg7Z98gRmDAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
صحبت‌های کنایه‌آمیز توتونچی، مجری برنامه شب‌های فوتبالی به تیم‌ ملی فوتبال: دمتان گرم! در کمتر از 48 ساعت 7 گل از کره شمالی و ازبکستان خوردیم..!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140534" target="_blank">📅 19:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140533">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140533" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140532" target="_blank">📅 19:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18169032d.mp4?token=aQ-V_51O5Q5U87qkbXQaby-VhJkSKvdjRsjDCuUA4a1nsl8XOnMSZc4nX9Y_9YshbWB-RqRPHssCyy8fxiUtH7Jb8j7FHwJnjyPtKt7vYOEWmATDt0opXK_f986BAk89awvdDxqxKzoJf15RYtrGWP-QssSDKoOh-YKP_Prrx3s0DMsfvOWAzNmRaqJcCBsCOjJpvYQ5-hZwgn_s3wOUCoZXhDxPoHvnlraECmy9ndlFuIYTcQIdnTtTYTGYewmeYBPzNl_vBlqz_safBH-p5aJzgdbVdAyHvkdS9xh1cF3-sDBiNOhXLJvm8OC1CFywe37xJM3XYsanPJjyVYUQyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18169032d.mp4?token=aQ-V_51O5Q5U87qkbXQaby-VhJkSKvdjRsjDCuUA4a1nsl8XOnMSZc4nX9Y_9YshbWB-RqRPHssCyy8fxiUtH7Jb8j7FHwJnjyPtKt7vYOEWmATDt0opXK_f986BAk89awvdDxqxKzoJf15RYtrGWP-QssSDKoOh-YKP_Prrx3s0DMsfvOWAzNmRaqJcCBsCOjJpvYQ5-hZwgn_s3wOUCoZXhDxPoHvnlraECmy9ndlFuIYTcQIdnTtTYTGYewmeYBPzNl_vBlqz_safBH-p5aJzgdbVdAyHvkdS9xh1cF3-sDBiNOhXLJvm8OC1CFywe37xJM3XYsanPJjyVYUQyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140531" target="_blank">📅 19:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140530">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
پایان نیمه نخست  بازی دوستانه
✔️
پرسپولیس صفر ـ چادرملو صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140530" target="_blank">📅 19:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140529">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140529" target="_blank">📅 17:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQzyr6GxujyB607vbE7jbaOYE1l6q2KOOm4b_ugu9TybPc7R_SD8pSF5ZdwfG-21AG3sGQ3wwaJmldvwfGpp6hZFmrpC946gWm6IRgCoibzydkDnCXgh2FdGp6cGHKZKvm_V36e2Dox_rlqtRbxrQsPP4v7m4IbtD7Dlie3m2K8mW8oycpCvEbGESlf-3sWLXVtlpdRTFphaIkLoBiwsUUkO4UVu-PAu5BQeZ758MwJiAUlGJUDe5Mg5fHypkPoowE6cbbgqr1GRb6KrusuaT-bgPldFokOcBiur6GnXRyj8IsrcHjnjswW5SkF-t6WlllqjJr1ZKiI4FrDbl2eSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پیمان حدادی که بازی پرسپولیس و چادرملو را در ورزشگاه کاظمی تماشا می‌کرد همزمان بازی تیم فوتبال بانوان پرسپولیس با ملوان رو هم با گوشی دنبال می‌کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140528" target="_blank">📅 17:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFo4YSaVPVD2ha48NuS_aMr71zzL7dRbsSUg3M-pt2LFHtwUo3VPmVF9qAtw44xyJehqNeWi6jYOGREhyDbTifRJJS_PMM19QYsKyAkmWZWJVat6sMarSmom82dNdvsF5umRgSfnMmpARgR8ejTuheLxHYyAPvRkzVA6_nWbr41r-_YNGxbsqmUmdJ6EYBcMy5N_eH3ms8QQRtDNYpbOrNF7L2wtsKc8tGehytZiZH3yyXQhcFdD5b72k3edSWDmFtw7hgqGDjXDf9FNkVeUcrKShBBNbSejN2HJYn99ikB51j2y9VFm5OHlR_KDZEkQjjqXmAN-kCPR1jyJ_JxARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140527" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
پرسپولیس فردا بعدازظهر در دیداری تدارکاتی به مصاف چادرملوی اردکان می‌رود. با تصمیم کادر فنی دو تیم این بازی پشت درهای بسته برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140526" target="_blank">📅 17:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140525">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140525" target="_blank">📅 15:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140524">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140524" target="_blank">📅 15:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
🤩
فرهیختگان: بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140523" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSiD7YDd-jXMtA0C85_BqgDpFIjX6XljjGld7vXdXkfe7mStIcUepFO4sIVPciZbYbizWzEzws_GpqftmBjPyoBlLb4Ks8KrvarfSnhAhpxmkuV7pHXxoiWo-pyc5cJet7jrEgmUccI7unnj51t26aO0mEI25PksiH0xyM3lqJfc1ngB-INZRpn8GV6Ch0lEMkM8HQlsSIqyYktGSvbbltzVdxszYKCg8-YPpKxPsiMqXTQLSuF573if1gf-TV__Kqk1lZbhEY5_KFo3JhOp2MyRHfT45hUMQ8soI6c51NcrIGsl2Wepcf39_11VWLQxjVS8qPjA5RTAeE7efIncwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140522" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140521">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140521" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140520" target="_blank">📅 13:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=WqD2RukHa9zyFlr4s7yTvvd9R_MHErLpgLkuk7uKuhnP3qUvd6vvx9GlQY7tlo0XAjeGeNbB7hPrCgOFyJr6ZP4rfT-tJshtgnM9rlvMqRP0icb7n7OohfOrZHiu_V5AWTlJkvrzw2OjVJcqCiVW0rU-LNVobPR6RSvUfzbxjrgnEZNxvjDIohANcLEfwVU5dk_yrQb1ymfdt_S6L-rUJtOFCdAxzWMadDLSQy-PIgc0IRS2ZzYgqe38Fz9ErHyRqF2YtLLJwgVhkHc1UeChVjomnIf4TmdM3jlD_Fq_ptvtSAojLyCu3MLyWDsrsaPzAAi1WJ5Yxn28JJFMKWb8YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=WqD2RukHa9zyFlr4s7yTvvd9R_MHErLpgLkuk7uKuhnP3qUvd6vvx9GlQY7tlo0XAjeGeNbB7hPrCgOFyJr6ZP4rfT-tJshtgnM9rlvMqRP0icb7n7OohfOrZHiu_V5AWTlJkvrzw2OjVJcqCiVW0rU-LNVobPR6RSvUfzbxjrgnEZNxvjDIohANcLEfwVU5dk_yrQb1ymfdt_S6L-rUJtOFCdAxzWMadDLSQy-PIgc0IRS2ZzYgqe38Fz9ErHyRqF2YtLLJwgVhkHc1UeChVjomnIf4TmdM3jlD_Fq_ptvtSAojLyCu3MLyWDsrsaPzAAi1WJ5Yxn28JJFMKWb8YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140519" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140518" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140517" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7SK3zIkNmixf8pHfJB4l7173aiqbbq7uh6lsZgrVddFWrcrQn9dK6eOxIQmSEIBuCdb75vqo_aBqFVmlCrOorDZlE9OM1O9IEHcSC4afbMY_PhiKHmai6b3EAeH6js9c0TzbZgbi5I6BSChwyRrtHPPCwPcmsaHamFmpH98J_yO4OQMGk7zbu4EcPjJ8sAF3wqIyaNkczSQJRNWPzj4PWi3jfmp5nqlmWw4mhWjLjh47clcGZzPD-Ma4k-labaCZdL3aunCDH8B1nzfwudjU3VOzpzMY5zmoKgebQz0sqbCQDIbvRf5Zxa0IImd6Qn7mwjeFm5za5J4C8InCdCEOw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140516" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140515" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140514" target="_blank">📅 11:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⚪️
⚪️
⚪️
مهدی تیکدری در غم از دست  دادن دایی خود عزادار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140513" target="_blank">📅 11:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140512">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140512" target="_blank">📅 11:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140511">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140511" target="_blank">📅 10:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140510">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYMrqnBt8lvFYN7AXD_LJoc1t6fh8R7BF24Pv3IlOvagH-jpDsPrLFg6-ZLCKu3XgTJHE6fVEk4h77Z-woRRs7Nw-Abn8TpY-pQBvZ7HHGq2j3nPADQfzdq4ChwXDfZ0dOTJeoCZX9HtjubKsZ9povFLUWc-J0-6FdS1ShDCO08JI9_UniMC82tlNkEOoLzQLhpPgDcmrE-K-mGYZfTrrktP1qLmvLmHDgJM4MgjRv-q34xsNUVfC7HMjkkpsSspMpXmCrbkfDTuxoz8VmaTdUIR8FdD_0AqKaRjNYOC9sw96BOoX-Fd5R7GxnOkFYcZesKCsvRsFElF0DZu0_kCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140510" target="_blank">📅 10:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140509" target="_blank">📅 10:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140508" target="_blank">📅 10:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140506">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLTfuPhfvn7DfLJmrDxgKfbvMfag6X6R3wCV5Vxt00dJzx5n2yWa3VcrVZn2ZUrHtU6rx7cXl7NB4TMD25x3srqIeQ1_seNH1NA34AkLxW5i_hi8fFyJGjJDH1S3ZrRRPpnRG5B9QsZB5sill5lI01tfaUCEx24CF0SNLdSpemoPj78m1rWjL5Ijio84Q3qGkx6VRvmEXy_pV6qV2bl7r5PvudJ3FQAF69GGvcncD7Hj46-2eQUADpVme9GCTiYi_5VgHg65w5DvfbQCd_NzU2aa6Uy-ZYxUcRYDfQ2txfX5KSbYVGBwVIyBo9KFsisAapRKWIAglW_jZUcOSQcGYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140506" target="_blank">📅 01:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140505">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzipbcZHitNX3smBLfvwjAaVnrYv6bS1H7VaXkACCeozixL-ggDZmo8xQk0TQ9aK0zi9IhueCuBNTcgpS6WSKdK3CHEgGqoLWF8tHSeY_B86Rq8jpDctyBQz9cwBZfGxpuWPT1BzMdjKRqMRcPLQSeefGdJi_G0p6Wq1MsalMwkLj7HwFPTsMBT1oEyR0sqL8F34QzCiuNONvhPjwFiPTxdhpy3GdxdSLRdtVk4b1ZjuBYJAUVt9j_Cbazlhv4BVwaFDK4iOv2gdcybs7lXNtJtlihVeBQq8FDWG7KPhxWWc618bg4rsEZ-SaMK7_HzOaPdKo-z7FEkW84RqMZRPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎉
جشن تولد آقاکریم برا محمود خان و آقامهدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140504" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140503">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199c169158.mp4?token=pmHVyk23Kde9vL0kryvbXYtxQo6S_j7VIEi96va-f-29j34D0uDsa9XN5I-Jy7TVhqWC49F_q8SjMWIWNn8z7iHeOoFbmwIELo0lSe3SFYfz2pVtCPjaXdiRmm89cng8aFtFwBcm6DfBNPrNMTB_zyy0JU1BGr-MZi5FXHE6d8z-vc516D0WX7WSzQKZLFYzGKDvCG3Fe6GM9MfiGh2u-PeFdPskQtRMFwAAAt5dT3PqRWVln-QTKg4JV6E1f-MMKU8j8YouErNMhmZhgtqZQaakizTeZwS8MImbC9OUVbOYW_K9N7Auf8oICVOqsTZB1avWnQk5N6ylIScoaxE9lzOz1OwkdiyoVM5E9hcd2QLK9W98GdgYq8YP1pRs6gX594rba8wAKk5eBfpFX-lsu3rqNjLajbguZ1ycNaxFr6EKfihmwaFPaay7FDaz7fiZPXJTN7xJ5_vfWJ1RoaiEQWv-_QAqKY8HP17-Ur0Y6U5_a_w2vpKP2uQTwGPV98gbPBUjLDaSbgzA-6Uz7eL2thoaoeiRlqq237akxwuuz5otAg5y-8hsMSb4Dbdaxr0SC7z7CRp3FsGB7fnigwE3PQVbUCUSLG2N5r8rthaLRToTr_iCkRIhiYU1_lsJNdMTpqvXO4wRwbFmHCPGQOPTyKqoiZk04aEDS2bw1dcnH_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199c169158.mp4?token=pmHVyk23Kde9vL0kryvbXYtxQo6S_j7VIEi96va-f-29j34D0uDsa9XN5I-Jy7TVhqWC49F_q8SjMWIWNn8z7iHeOoFbmwIELo0lSe3SFYfz2pVtCPjaXdiRmm89cng8aFtFwBcm6DfBNPrNMTB_zyy0JU1BGr-MZi5FXHE6d8z-vc516D0WX7WSzQKZLFYzGKDvCG3Fe6GM9MfiGh2u-PeFdPskQtRMFwAAAt5dT3PqRWVln-QTKg4JV6E1f-MMKU8j8YouErNMhmZhgtqZQaakizTeZwS8MImbC9OUVbOYW_K9N7Auf8oICVOqsTZB1avWnQk5N6ylIScoaxE9lzOz1OwkdiyoVM5E9hcd2QLK9W98GdgYq8YP1pRs6gX594rba8wAKk5eBfpFX-lsu3rqNjLajbguZ1ycNaxFr6EKfihmwaFPaay7FDaz7fiZPXJTN7xJ5_vfWJ1RoaiEQWv-_QAqKY8HP17-Ur0Y6U5_a_w2vpKP2uQTwGPV98gbPBUjLDaSbgzA-6Uz7eL2thoaoeiRlqq237akxwuuz5otAg5y-8hsMSb4Dbdaxr0SC7z7CRp3FsGB7fnigwE3PQVbUCUSLG2N5r8rthaLRToTr_iCkRIhiYU1_lsJNdMTpqvXO4wRwbFmHCPGQOPTyKqoiZk04aEDS2bw1dcnH_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140503" target="_blank">📅 22:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140502">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=Mjid35eZOjzsocPQWhYjwQWAcQn91oIwW0oQK2nfRaWhh2D3Ilf11J7cxf95PghTZY7tYHEk3m7cLqmESZioBghsJIojXIsHk4DlapPDKdjhgBMiP6Bmrm7iiTPtBTkhE4p8N-dktblkuKwgJvc-gbWpO-9_ueLbQv-c-QO7CbQKtNTh4qm1h45I1nc8Fo6mPYL3hbcArz9AQVW9VZWgZNabARc8zEl6MNWajl08PbD4534i3vG6W20XD-HYAmOrKf8OmI-2qWguYwfh2Ah15MttLcD6Ly8tWlpdo582hLtZwlKISzCN0lhXPJ_ba1b2wb_xG7OB7QSpLlZ_THYq3Gc6pOUlPjunc6davRhggheKIxAR8ujvh7Mmqw2ub0Sqv6UmpU4zbM03ZDFC-jG5cUpDzrinlq0dHJ4AhMjwpHdmvce8Vm9QhabmKj36bd8-4LxZWhAiRoQ_RbUUsVxik8M-ug1seWKmSZaMavsb6J6PwWEuCHeD-GW7dvK_BUYi2isk5pzLdNofuJUQZ23clLPWb775_Voq4D3uOcGOCJDYCrEA1GTHpsUXCgn1i2JWXifluDImRp-VRKTJCoiRZZuYLSe_BFka2geiYOb_R303JMTunLuYDpYljpzSxFhewXgb9bSzZcuQSHU1_zjExANnIK8AK20wL0B0wylsijA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=Mjid35eZOjzsocPQWhYjwQWAcQn91oIwW0oQK2nfRaWhh2D3Ilf11J7cxf95PghTZY7tYHEk3m7cLqmESZioBghsJIojXIsHk4DlapPDKdjhgBMiP6Bmrm7iiTPtBTkhE4p8N-dktblkuKwgJvc-gbWpO-9_ueLbQv-c-QO7CbQKtNTh4qm1h45I1nc8Fo6mPYL3hbcArz9AQVW9VZWgZNabARc8zEl6MNWajl08PbD4534i3vG6W20XD-HYAmOrKf8OmI-2qWguYwfh2Ah15MttLcD6Ly8tWlpdo582hLtZwlKISzCN0lhXPJ_ba1b2wb_xG7OB7QSpLlZ_THYq3Gc6pOUlPjunc6davRhggheKIxAR8ujvh7Mmqw2ub0Sqv6UmpU4zbM03ZDFC-jG5cUpDzrinlq0dHJ4AhMjwpHdmvce8Vm9QhabmKj36bd8-4LxZWhAiRoQ_RbUUsVxik8M-ug1seWKmSZaMavsb6J6PwWEuCHeD-GW7dvK_BUYi2isk5pzLdNofuJUQZ23clLPWb775_Voq4D3uOcGOCJDYCrEA1GTHpsUXCgn1i2JWXifluDImRp-VRKTJCoiRZZuYLSe_BFka2geiYOb_R303JMTunLuYDpYljpzSxFhewXgb9bSzZcuQSHU1_zjExANnIK8AK20wL0B0wylsijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
نتانیاهو تقریبا برای یک سالن خالی سخنرانی کرد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140502" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140501">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
حین سخنرانی پزشکیان، نماینده‌های: ایالات متحده آمریکا ، بریتانیا ، آلمان ، فرانسه ، اسرائیل ، سوریه ، لبنان ، عربستان ، مصر ، امارات ، الجزایر ، لهستان ، سوئد ، دانمارک ، کانادا ، ژاپن ، جمهوری آذربایجان , مالزی ، نیوزیلند ، استرالیا ، جمهوری خلق کنگو ،…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140501" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140500" target="_blank">📅 22:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140499">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
#فوروووووی
❌
با اعلام حدادی جام حذفی برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140499" target="_blank">📅 21:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140498">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=gKsxxx5Ven1zF5kkvn2nnueI8m4YYAtR_xknrqeDEW1T2Dc50R9atMCtyUshcMOhNo05DNYrvbimYx8H2DiViVKvleV773wI8QSMD0QaoWJDaHmyBruzq2EPPEbg7DOX0t-jCCE8Ek99vZ6QJ4C6_EL9Nh8X5407tsfC7XXufOS38pCpk1m2H44_iK_d-Tb5W5MmF9Nvm3rPTMp-7TcXKubUmzU7IrJ4TTBBal0PmaNSHUoI4vnaBAz4LVuWrEPptpg1XSUsteGkr8X7KR-HsdvgVVmCpoz5Rc3BuwvM5w2gVJfMND50VtBwS43b2bGMOXbEDNZeeEGsJs3M51xlUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=gKsxxx5Ven1zF5kkvn2nnueI8m4YYAtR_xknrqeDEW1T2Dc50R9atMCtyUshcMOhNo05DNYrvbimYx8H2DiViVKvleV773wI8QSMD0QaoWJDaHmyBruzq2EPPEbg7DOX0t-jCCE8Ek99vZ6QJ4C6_EL9Nh8X5407tsfC7XXufOS38pCpk1m2H44_iK_d-Tb5W5MmF9Nvm3rPTMp-7TcXKubUmzU7IrJ4TTBBal0PmaNSHUoI4vnaBAz4LVuWrEPptpg1XSUsteGkr8X7KR-HsdvgVVmCpoz5Rc3BuwvM5w2gVJfMND50VtBwS43b2bGMOXbEDNZeeEGsJs3M51xlUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140498" target="_blank">📅 20:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140497">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_FRteG_aWp0sZYGaqaL9qRJF93MLnz2XzDIf3u5yAWHd56KUwuYKWj9Y5Lsjvl5CucbYGQiikW9V86LeUbLx-x2j5Nx7j9Lw0816acRju4GrAtbAdAHY73KxS7OgpXWxyUl5nAVXlmPpE0aaWRmWEPi6uW1_4CBI4OZx79r-21S36mGzHxtWKgHEzqrXoQkqhOlfqJG8r1kr-gupzYPOffrt7HwkGRV69ui2r-bBEJZoi68wFsM6H28Y3UP26NZkUdbc3j88_mP7okDr0D_JrTljMCrFcgaPyotgtl7JcAG7ciTkOYH7L_vimML2A2TYcGI59UhyVfwTiMUozHaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140497" target="_blank">📅 20:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140496">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=HCJYs2bR8bHc-UyKL-xIV0ci6NWkvBge8L4Zicmrh7HMs7GSIaU90g6eJ75HikfoHzMUmWgcLzr9NAXZwLQF2lC5Ly7WDRuh_mtkCDIEF9toXNuRUll1xL5_ln4UEq_YHCd3wyL6pUn2q24L737OS9heW_GFfQl50DTPcfqwY8kmiqP8DW8J6vq6QLLtASbW4Phx1JySVTWyiKRHXdCH7mOU2MeIFejGEWSVhNG1gLF78ALp2zpf-LcW7t1lcWbrehSy5N9V4buuwGAtphbJr_dOJ3JwhBzEbJTXva8qzc-aKFnaFyHhIZL5OMg-j3S0UHXYg4v04Bl_fft79u8Y-whneKTM_B8koDXfFRJ9Hm86gAHKtU-kK0gpUM3sR4MmgWfsf4HE9_jZnqTqN5h9ALtDXLYSdZNm01pCkrlx8rlQd30FAYewetxhXvIgvEtlJLChdZePu5FLrxMKIHhg47NW3FDuS7HJPt1LbiTY2M8FedrNUe-W5XH04mrXc-WZC7EPRWhaBTCw8bVaQ-0UTI978HLa1cXyTCQK_jpKW1_63tfJITQe6hKmI1xvTTGpQTaYNTWgDj9I1I7slQxuX9yRFQAURu5qPSf2iwiF4_NNxcCbLBNtB4vRltoa_3201mnLS_w6dWnjSeHMfziomjRZTMlzSNEn_ewgm0kfRag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=HCJYs2bR8bHc-UyKL-xIV0ci6NWkvBge8L4Zicmrh7HMs7GSIaU90g6eJ75HikfoHzMUmWgcLzr9NAXZwLQF2lC5Ly7WDRuh_mtkCDIEF9toXNuRUll1xL5_ln4UEq_YHCd3wyL6pUn2q24L737OS9heW_GFfQl50DTPcfqwY8kmiqP8DW8J6vq6QLLtASbW4Phx1JySVTWyiKRHXdCH7mOU2MeIFejGEWSVhNG1gLF78ALp2zpf-LcW7t1lcWbrehSy5N9V4buuwGAtphbJr_dOJ3JwhBzEbJTXva8qzc-aKFnaFyHhIZL5OMg-j3S0UHXYg4v04Bl_fft79u8Y-whneKTM_B8koDXfFRJ9Hm86gAHKtU-kK0gpUM3sR4MmgWfsf4HE9_jZnqTqN5h9ALtDXLYSdZNm01pCkrlx8rlQd30FAYewetxhXvIgvEtlJLChdZePu5FLrxMKIHhg47NW3FDuS7HJPt1LbiTY2M8FedrNUe-W5XH04mrXc-WZC7EPRWhaBTCw8bVaQ-0UTI978HLa1cXyTCQK_jpKW1_63tfJITQe6hKmI1xvTTGpQTaYNTWgDj9I1I7slQxuX9yRFQAURu5qPSf2iwiF4_NNxcCbLBNtB4vRltoa_3201mnLS_w6dWnjSeHMfziomjRZTMlzSNEn_ewgm0kfRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140496" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140495">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=f86yeAhXbWJXLQmnfHmMiynEjjfStR-Zzo51wn1vxtBzBd5p-LwIuLxfvIDWo3WPoZuNHMfz9d5dad68FAXYsyz80xcxdGbqGeaG8QNFCG2u7tiawC6OBCmOlPPrsg1koYdx3jEySyA-7-DcwM-CMHz8cVvCoAl4a7rQYnDYH1TcJcSF2Jvj5vqKtunLs9cBP8Hh-TQrPhCQ-rFFKeuMazqqAtNYm3NsUWwcki2WsCSNRRksZWNOPvub3sohosQ1caVE283chzcBs7xlV8X1wPOzEX_v5elhMhY8FwbXkpfrYlrHC5ATatn7SSkwyGEHm03MjErL0anz_X7DB_E4c0C_hoZ5Rt8snSe__lYQ9X1hGgN5oT73LRxLhlzPM5VOyoCDF3JQ7wrRtbhGdwgN80fa3GM79Pu2rtAl0ehQGdALPilfMMno1pRQybOmG0BIHMaKZ6qz7xyOVALuYTO-DB49k5xoR7ZRXdxojIZ04eBQm21CWeRQhUDsOYTsOKWmvxa791d3y9Nu05drETP8pb9CPCPHI99J6pfiq77tnFXCW8GsjRmg5vcsj6wikptSAn4LpkZT4Wf_yjJA_nR5MEPVLiBfDopepPFDohxc85CKB70nx5JMu7jRkGrfwNQNEHxjYaf1tEGyP1NT2oOZDduGC1ZSYgnZ37GmwANWnfo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=f86yeAhXbWJXLQmnfHmMiynEjjfStR-Zzo51wn1vxtBzBd5p-LwIuLxfvIDWo3WPoZuNHMfz9d5dad68FAXYsyz80xcxdGbqGeaG8QNFCG2u7tiawC6OBCmOlPPrsg1koYdx3jEySyA-7-DcwM-CMHz8cVvCoAl4a7rQYnDYH1TcJcSF2Jvj5vqKtunLs9cBP8Hh-TQrPhCQ-rFFKeuMazqqAtNYm3NsUWwcki2WsCSNRRksZWNOPvub3sohosQ1caVE283chzcBs7xlV8X1wPOzEX_v5elhMhY8FwbXkpfrYlrHC5ATatn7SSkwyGEHm03MjErL0anz_X7DB_E4c0C_hoZ5Rt8snSe__lYQ9X1hGgN5oT73LRxLhlzPM5VOyoCDF3JQ7wrRtbhGdwgN80fa3GM79Pu2rtAl0ehQGdALPilfMMno1pRQybOmG0BIHMaKZ6qz7xyOVALuYTO-DB49k5xoR7ZRXdxojIZ04eBQm21CWeRQhUDsOYTsOKWmvxa791d3y9Nu05drETP8pb9CPCPHI99J6pfiq77tnFXCW8GsjRmg5vcsj6wikptSAn4LpkZT4Wf_yjJA_nR5MEPVLiBfDopepPFDohxc85CKB70nx5JMu7jRkGrfwNQNEHxjYaf1tEGyP1NT2oOZDduGC1ZSYgnZ37GmwANWnfo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💛
🎙
حمله جواد خیابانی به امیر قلعه‌نویی: باید چیکار کنیم که کادرفنی تیم ملی تغییر کنه؟ نتیجه افتضاحی بود. آقای قلعه‌نویی نمیتونی تیم رو جمع کنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140495" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=lxRWpAB6fa1R2ZtszwmM9YoFsc2HN1W0k9JnFZYheXs6F8Fn4BNSxiS0yPkURrL3A1IL7e0-INizJMwImGPkHyV78KmK1OoG-eFCQRo9i89wDhrVtEqinYyKNETqTRFGI3YGftdTBU0ZQEiLVn81pB8C4cm_65qRq-yR8AV3kn3gw9YZ3xnfKv6mo4gnko9NuyBVsAtJ_Upo72EFVmehVqy5Lxk3_XDce7UJJON0qFfZa2pZNVsXbagF1oxqfF_hKa8AyHVcg5WS6WtyqppgvEjWJQTGo3A5yw-mbODo8t6EZyqgHnV1V4bjWDvF5At1U1rwWT1t6W4_QlCHymICTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=lxRWpAB6fa1R2ZtszwmM9YoFsc2HN1W0k9JnFZYheXs6F8Fn4BNSxiS0yPkURrL3A1IL7e0-INizJMwImGPkHyV78KmK1OoG-eFCQRo9i89wDhrVtEqinYyKNETqTRFGI3YGftdTBU0ZQEiLVn81pB8C4cm_65qRq-yR8AV3kn3gw9YZ3xnfKv6mo4gnko9NuyBVsAtJ_Upo72EFVmehVqy5Lxk3_XDce7UJJON0qFfZa2pZNVsXbagF1oxqfF_hKa8AyHVcg5WS6WtyqppgvEjWJQTGo3A5yw-mbODo8t6EZyqgHnV1V4bjWDvF5At1U1rwWT1t6W4_QlCHymICTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maqcnQ5gyOoD4JmlxMmt33VtMWpbgDMf_ZG2BvPStub-vHgyWfRw0Gh7FTWlprSMgKakUsN5wOsVIB-cU5_5lwa1tmHESm1UTFonJu-IokVPgDHJsohFwscmOPjWZ46KppQ3l44-5eYtapAM68lCZAvcI3pC8DFphSAL-G-uot0C71QMUnE_hvZMezPSvTJTBvjpAYnicm8i6z_RGUx5aqGmtO1RS_nCxVmieA560W_XxuFlNVOOCFiRhJfg5C2esJv7rbHGgTaHiLghUuPVNBAID7Qc-IKBQd1ya2oBswXCimWHW3N6pqDAF7kUcxF8d2K_1Sx_jWWwojhF7797zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140493" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140492" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
دو گل خوردیم .اونم آقایون شجاع و بیرانوند تقدیم کردن و دوتنه تیم ملی و نابود کردن   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140491" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚡️
⚡️
⚡️
عالیشاه از دو سه سال قبل با خانومش هست، مثل کریس و جورجینا و حالا امشب عروسی میکنن، قرار نیست اتفاق خاصی بیفته، عروسی صرفا یه جشنه و قبلا با عقد رسمی شدن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140490" target="_blank">📅 19:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
این بازی ساعت 17/30 انجام میشه و بلاخره روی ماه اقای درگاهی رو میبینیم ...ببینیم چه جور بازیکنی هست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140489" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140488" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140487" target="_blank">📅 16:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140486">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
ترکیب ایران مقابل ازبکستان اعلام شد
⏺
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس درگاهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140486" target="_blank">📅 16:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140485">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140485" target="_blank">📅 16:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140484">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
مهدی ترابی بازیکن32ساله باشگاه تراکتور که دچارپارگی رباط‌صلیبی شد هفته آینده پای مصدومش رو به تیغ جراحان خواهد سپرد و تا اوایل اردیبهشت ماه سال بعد دور از میادین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140484" target="_blank">📅 16:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140483">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140483" target="_blank">📅 16:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140482">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140482" target="_blank">📅 16:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140481">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
❌
گفته میشه عربستان و چند کشور منطقه دنبال فشار به فیفا برای تعلیق فوتبال ایران هستن؛ اتفاقی که می‌تونه باعث حذف تیم ملی از جام ملت‌های آسیا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140481" target="_blank">📅 13:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140480">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owL6ElTg_zDS1xvzoHvP49meOXQFKU88NxBGgvCYhEGB-kOVfPMeDroTAhyeA33Btv4qxTcuimGrCKA4EGxnAiSDgkYa0v3U0nFIs95CV1aMFbp4JkG31kPm26hEgZrQl4kRhXuqGCZ-hmwhScsrC5tupRJeFg03-7QuKx7eorLCrGIwyBWr--9PSdvxlOr8SaS3dDjmNwrReecL8yd3T6tXFAUgh2A2P1_UC3wZ9AQ2ZfrsQyt2ku7_xvxNkrgHM3-dqGRVl14EfqlgU5a4meKtCXE2kJCSh_SQRkyKSpOBQ3lR2ZesUzPRQp3NTK8WEitT_KYCdxDBxCYcrdTqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140480" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140479">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm1nCy79FEUUEzID1pWZ9NwfvELZI1T_pDy_6tY64_SL1klKXdzWTqDhfty7XwZ4e3R-e7M8x49tmIV0sJvCOm0ghWgbNzZE_2n0jLJiAB0G3Pyn_U_1go4NwCqvWFHzK5RLcy8wAxHRSI76UFrNasIqZyTU8O84R3EFk0AtNbfX3kwhXLeBmi8dsH1MnDvm-inXOXtx8bxF6mwH3crFAyoChkqmHkmCIznbLtKOa8tbtE3u8eYA13yDjK2EZEHU51W54qfJUGfS8vzUKX87VUz4SN87Apvb5rcBj3y6hukz4gk2-SNDTHZGZ5uTDOAYaJSoch3wEIhZwf0Py-NxOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140479" target="_blank">📅 12:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
✔️
بیرانوند برای فرار از سربازی، این‌بار به بهانه خالکوبی، دست به دامن کمیسیون اعصاب و روان شده تا شاید با برچسب اختلال روحی، کارت معافیت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140478" target="_blank">📅 12:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
چمن شماره ۳ آزادی به مشکل خورد!
❌
❌
بعد از دو سال تمرین پرسپولیس در این زمین، چمن سفت و نامناسب شده و قراره به‌زودی زیر کشت بره. احتمالاً سرخ‌ها چند ماه آینده تمریناتشون رو در شهید کاظمی و زمین شماره ۲ آزادی برگزار می‌کنن.  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140477" target="_blank">📅 12:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140476">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140476" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140475">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJbrBGDYTWoaC8w5eKRju0GftVYlXFCglwLNbNyaJcAfdliJOrvy2oKzgeHcox6TVOcObh_VT65IdUaNaR3Sq33odcs3_spsdJAhAbJmuQIvNEsDyf1VhmTjoe3iXk_nXyvA9Fwy1zVmTnotlS316Uy_6w4husydHDW58wXvHdKs1MytcHeI8viA87r02XXUIm6xDhip0Bu9c5JnD2_jewmXwc7KnFBOQ4bXMRnTEU98Aksxo-ZnTZVExht_Kxb3GDdAys76kaj8y6rYfnwUUWZXe5lTXij_dYgIlN7q-7W1llxte7P-mOMUWQWz2nwqp8dQbzpk-s3xZG_lKQgOvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140475" target="_blank">📅 11:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140474">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی : کمیته انضباطی به باشگاه گفته مدارک شما برای محکوم کردن آسانی کمه و اون چیزی که ما نیاز داریم ندارید.. که یکدفعه باشگاه مدرک جدید و آس رو کرده و فدراسیون آچمز شده و هنگ کرده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140474" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140473">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
بازگشا، سخنگوی باشگاه پرسپولیس:
✔️
از فدراسیون خواستیم رسیدگی به پرونده آسانی با حضور وکلای ما و آنلاین باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140473" target="_blank">📅 10:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140472">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140472" target="_blank">📅 10:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140471">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140471" target="_blank">📅 09:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140470">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmAoJvc0pSHJypt3gJ4lJvZiqY5JYoqaAvV-aXtL8rDNfpkkisfgMUOfDulp2bBobgsHwDTpEmGh1XBBL2f-XxMk9H2LeNeHiRgwO-DFlBsJ3qZCxJUzpjmN7TVjE8ZR3kg66psrPypofu0y31oBy_SnSPaVaoXdKhx7J3RqYY5LEnvlrgkbgvndcYykUs4l3Z_mNBYviMF2l4mNi8xMYNPoUcqBnXyRQpLhfulARbHUeRV9SZOwN25s8Ongl-OQRJ0MuXIAMF62ZXAhk8Lz5UGC3H9OuNUmOXEkAs4pfuUlArrvaZK8zaabL7eYuGt8A_bp8-7wohVlmC39o_-4bA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140470" target="_blank">📅 09:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140469">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUmsdPZNurA_KG_4EnNZclzKzGrD-k5E7b-lKYv_tfZpBTXW1VIslYcRGozgBQD5pYlwyedJfyTAU18pSi2QxA_209o4r2_jnOAtYJHVqMZvd4CAW2wqxXlka-2mvPXQZFVuTZdgduZ3Vw1NkNpFRN_tm11tc2e2uVKKjPdhHvDuxYUmNFnStitvsbyWi2phnfQJKDgc9qZp-3WyrS8UG-_w9VXZB6kKlsbAaAvInWL_yT4ns-omSGITETAL1kcNO14XYQCeUEeqIBSYh-0LuPz9qeg8xN1qRXlyzesoCVC91svEf4rKkPcjT8NKkVTI7Y1eHQN61CoVXjc_4NudhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ایران و ازبکستان؛ محک جدی در یک روز دوستانه!
[
ایران
🇮🇷
🆚
🇺🇿
ازبکستان
]
⚽️
ایران و ازبکستان فردا در یک دیدار  دوستانه به مصاف هم می‌روند؛ دیداری که بیشتر از نتیجه، برای محک ترکیب و هماهنگی بازیکنان اهمیت دارد. ایران معمولاً در بازی‌های مستقیم و انتقال سریع خطرناک‌تر است، در حالی که ازبکستان با مالکیت و بازی ترکیبی می‌تواند فشار ایجاد کند. با توجه به ماهیت دوستانه، احتمال چرخش ترکیب و افت‌وخیز ریتم بازی بالاست و آمار نیمه دوم می‌تواند متفاوت باشد.
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
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140469" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140468">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
🤩
فرهیختگان:
بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140468" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140467">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNUaRKP5KlLPR1WwyprMSauEJaJfJG5zbGqhV8HfiqLaj6gGxSP04gcOFnvJhFv2j97JyOrPXHzsBBxSC9x8B8bX8rIoyxELFIZhwVmLQyejvYhFdpZY5Vm6-_jotaGfdRoEfpknx3qWfpbqCyf3OjW5M1Litt9aq8M_pmRDl6j486v6W4GYwRlaQ_QhKjzr4iIjSr0ah2yVClAfzXygjYsQp2rmavH26a7pyYTMcg0FhJ9_O4rGU-6gUKpCKMzWYHi1o8bJpbrrX5TJuGmOic_tqKgatWmEXyuvZ_4Bz2eTWoiQ9uVtwQN0c9_twGjt-1K_Li_AZSGkPJToDmbyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❤️
پرسپولیس در نامه‌ای خواستار برگزاری حضوری جلسات پرونده آسانی و ضبط کامل فرآیند رسیدگی شد
‌
📌
باشگاه پرسپولیس در دو مکاتبه رسمی خطاب به رئیس فدراسیون فوتبال و رئیس کمیته استیناف، خواستار برگزاری حضوری جلسات رسیدگی به پرونده شکایت این باشگاه از یاسر آسانی، حضور رسمی نماینده باشگاه و ضبط صوت و تصویر کامل جلسات شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140467" target="_blank">📅 01:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140466">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🤩
👤
🔴
فوتبالی: تارتار بعد از دعوت نشدن کنعانی نگران وضعیت روحی اوست و قصد دارد جلسه‌ای با کاپیتان تیمش در این باره برگزار کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140466" target="_blank">📅 01:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140465">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140465" target="_blank">📅 23:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140464">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElBcFu8bpTfMRqZMo1ZMdTFY3Gty1dFss8fUM_XxSkX-fIN4KsGbOF_CkzbQk-LbfRtKmL8oRFYdCJ8f8fb52xDS7gRyZopu6yMRlvURfmRq769vSOx6n5kH8vesnlynyRNBquRXLrPEBJmh8i1I4qYY5MULiR5FpD5cE1Y6g6d7Vemxj5tjY9fdkRrdZK5SO5v7osmoYvb-Hpmu4M50dgaruhgmytXABiH8Ein9sgnPgjDYZ1wnjkmkicQlwKLtG_EIo-TkdI93ybBcekAoYfhvZMpY39B4HPXLQuivZeAEglU8zAjsm7FKVIuRh4ywLxAD7KfRmoQ2N8lh3FoL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🇮🇷
سه درخواست رسمی پرسپولیس در پرونده یاسر آسانی
🚫
باشگاه پرسپولیس پس از ثبت لایحه تجدیدنظرخواهی در پرونده یاسر آسانی، طی نامه‌ای رسمی خطاب به مهدی تاج و ارکان قضایی فدراسیون فوتبال، سه درخواست را مطرح کرد.
🚫
این درخواست‌ها شامل برگزاری جلسه استماع با حضور نمایندگان و وکلای باشگاه، ضبط کامل ویدئویی جلسه رسیدگی و فراهم کردن امکان پخش آنلاین آن با هدف افزایش شفافیت و اطلاع‌رسانی عمومی است.
🚫
باشگاه پرسپولیس ابراز امیدواری کرده است این درخواست‌ها با توجه به اهمیت پرونده، مورد توجه مسئولان فدراسیون و ارکان قضایی قرار گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140464" target="_blank">📅 23:20 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
