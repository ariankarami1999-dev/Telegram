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
<img src="https://cdn4.telesco.pe/file/mNuyzeQRvIOwgdkpl7Xncvf1VRMNLccEEpUt8IKaLHFrhAyhSX1gMDO5RpGnP54hAtcjVMAk0w_CgDbRFK0NV4wYJpo3h3qnbnMiyr9whD3UoGl4c9JVlYDJsU8O6w4M6eX5TW-rLzP3VVz_yyYr11jw-GtESw1CqTN8gbyKEjjPqlnEsd8YVh1MIYdnr0Vm6qPEl3p4r1ePMEQoCkELM3XGejpnV1_1A6CkEEPMhuYpxOCW_zA8ZdaSZW204ISZZtJpbR2ksxIc_G2o6CKk6lv9AxZ6mDua9a-C95I1O5AMZHiKyfKZAwMz6D7odCVm2rId4qN4TI-LQeFrNi1GrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-140699">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=Q1YPy1whzvETzxGs4oQHqSH0j7PnSgvfna_iQEyTkXqmxyUO_zCAufBE5lrzgj6TSZc3vBHwNSHkNbeZ2MGlZhn3Y2QVVzYaIbdhh54NvFhNvq99noevDI9iOrlgkwK6nkL2WOzEDyGtpZ0SoVWyk-80IIR5wuoNJITPavnD6N9jUhvr0g0WKrJialRsV-yf7C-IsJIfDef2tIpnqj9E6YcZi4r0op7qfxT7u42GFbNWucJZikE_6Ss65uonenEe-wXJ-PMHDmn68ip7svWHGNo0TQQp7Uz0FwmmdHQc4qQ2sgCztVcribgDzTn8noPKEWIE5Ku7nont74eroTkMQiakmcnJ1Q5AqlQMWzztKsAqCkXQCU8CVOoAIXNQfL48uwgkcD1VSonQhthsNcVPBaabWkBgbMslWcm1p4B05NaLgfO5W_apVSDJ0UX9T83ZmHm8iHiyAHysvoh9U0VYjou7cqxAqbFqrY2y2tJ08JOvSWLDzgRde4DN7aNaTG2ehooPGNVFQrXYTwPtN1rEMd2PFGLYgvvpMKX_cWkbRZihlz1trxoR3cJd_sLDIo9SfaGB8RCsRh2QfVRJvxLhPBFOF0eR5tz_pxD6vZoBssiVd78uPFaFV8F2iQSV0OmRtvwYXCVfKvh-yG8p7oPjL5ssfvdvaPoNxIowWgc6d4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=Q1YPy1whzvETzxGs4oQHqSH0j7PnSgvfna_iQEyTkXqmxyUO_zCAufBE5lrzgj6TSZc3vBHwNSHkNbeZ2MGlZhn3Y2QVVzYaIbdhh54NvFhNvq99noevDI9iOrlgkwK6nkL2WOzEDyGtpZ0SoVWyk-80IIR5wuoNJITPavnD6N9jUhvr0g0WKrJialRsV-yf7C-IsJIfDef2tIpnqj9E6YcZi4r0op7qfxT7u42GFbNWucJZikE_6Ss65uonenEe-wXJ-PMHDmn68ip7svWHGNo0TQQp7Uz0FwmmdHQc4qQ2sgCztVcribgDzTn8noPKEWIE5Ku7nont74eroTkMQiakmcnJ1Q5AqlQMWzztKsAqCkXQCU8CVOoAIXNQfL48uwgkcD1VSonQhthsNcVPBaabWkBgbMslWcm1p4B05NaLgfO5W_apVSDJ0UX9T83ZmHm8iHiyAHysvoh9U0VYjou7cqxAqbFqrY2y2tJ08JOvSWLDzgRde4DN7aNaTG2ehooPGNVFQrXYTwPtN1rEMd2PFGLYgvvpMKX_cWkbRZihlz1trxoR3cJd_sLDIo9SfaGB8RCsRh2QfVRJvxLhPBFOF0eR5tz_pxD6vZoBssiVd78uPFaFV8F2iQSV0OmRtvwYXCVfKvh-yG8p7oPjL5ssfvdvaPoNxIowWgc6d4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
🔴
حضور پیمان حدادی مدیرعامل باشگاه پرسپولیس در ایستگاه 88 خیابان پارک وی به مناسبت روز آتش نشان
🔴
مسئولان پرسپولیس در این دیدار ضمن خدا قوت به پرسنل این ایستگاه آتش نشانی با اهدای گل و یک پیراهن پرسپولیس از این قشر زحمت کش تقدیر کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/SorkhTimes/140699" target="_blank">📅 18:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140698">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
ساعت بازی ایران و روسیه تغییر کرد
❌
❌
فدراسیون فوتبال روسیه از تغییر زمان آغاز دیدار دوستانه تیم ملی این کشور برابر ایران خبر داد.
❌
❌
تیم ملی فوتبال روسیه به هدایت والری کارپین، روز ۲۹ سپتامبر (۷ مهر) در شهر کازان به مصاف ایران خواهد رفت. سوت آغاز این مسابقه…</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/140698" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140697">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
🔴
🔴
رسمی/ صنعت‌نفت برابر مس پیروز اعلام شد
🔄
🔄
کمیته انضباطی فدراسیون فوتبال در پی عدم حضور تیم مس رفسنجان در دیدار پلی‌آف مقابل صنعت نفت آبادان، نتیجه بازی را ۳ بر صفر به سود صنعت نفت اعلام کرد. با این حکم، صنعت نفت به لیگ برتر صعود و مس رفسنجان به دسته پایین‌تر…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/140697" target="_blank">📅 16:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140696">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
😳
⚽️
بیرانوند: سربازی من نهایت ۵ماه است!
❌
فجرسپاسی؟ شاید اصلا به تیم نظامی نروم/ کل سربازی من با کسری‌ها 5 ماه است؛ در همان تبریز به پادگان می‌روم و با تراکتور هم تمرین می‌کنم!
🚫
❗️
۲۱ ماه خدمت چطوری و با چه کسری‌هایی یهویی شد ۵ ماه؟ بجز تاهل و ۲ فرزند و راه…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/140696" target="_blank">📅 15:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140695">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm_488PEIhIsL6fAfw5o02oUxA51H_0QoWToCaVkxeMMmbGydh09QkxTsgQc-me_ZRTBEgUm-nwkynhjOqi_VWe9anTH4P-k6cqv90TfZukOaVMvuitFvH19dDIWux1pSbBlvM4mgTiCRsTg_OQjTOGD56vrfg_uI9qKmQVUAMcOSFm3cdXPbw5oyOq3zKNj3gCGgUm91wPDaZdmHN2vrU5i2HkzaKgWHxyew5b2EN17HzxEhp9tckW0Qbhu-sxGBeMM6qFi_GkQ0ED0rqIivq2rxbnFzjpRJlxDAP7JCRyptDzLUw0xMvBOewDlAPtJ79Vm2zEZmIQOGyzo4z72Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری | رسما شرعا جام قهرمانی به کیسه اهدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/140695" target="_blank">📅 15:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140694">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
افشین قطبی، رسول خطیبی و پیروز قربانی به عنوان سه گزینه نهایی سرمربیگری تیم ملی امید انتخاب شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/140694" target="_blank">📅 14:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140693">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/140693" target="_blank">📅 14:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140692">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🟥
دانیال اسماعیلی فر از تعویض ناراحت شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/140692" target="_blank">📅 12:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140691">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/140691" target="_blank">📅 12:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140690">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
تیم ملی والیبال کشورمان با شکست ۳ بر صفر مقابل ژاپن نایب قهرمان آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/140690" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140689">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGElrNWomL1f9fjchE2P0eO8KF7HWEfaWClQvS7xnj3wTY5JOnA1aLjvPvoYJPSV7yUVLP2vh4mHkysc0BBrLf-StU8b7KUWFzC3M3V90QEgc0mQC4LxXQaOTZqpr3GjxCqAVrqvukOfKnwFyTZ7oGZpMCZ9_zFr5Uf5mJJ883e3TZ9kUOCwovtwPS2_1gc8a-Ekui3TF6-X8VA-MHUD8v2IstaGeZcFeWYDv7ffOqTDe5Pr1jB_s6xY5GVK5As8McABODNTTV6_d6_EhfrabRh5OlHJwkDpEeR3iR6GYu0yHBOSTeiSx_jLRJP4NCpSLiMVhwAd4L3UmCj95BDoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Spain -
❤️
Croatia
⏰
Tonight 22:15
🏟
Ramón Sánchez Pizjuán
⚽️
اسپانیا با ۵ برد متوالی و بدون شکست در ۳۹ بازی اخیر وارد این مسابقه خواهد شد؛ کرواسی هم در بازی نخست ۲ - ۱ چک را برده است. در ۱۱ تقابل قبلی، اسپانیا ۷ برد، ۱ مساوی و ۳ شکست داشته و آخرین بازی دو تیم را هم ۳ - ۰ برده است. مدل آماری پیش‌بینی، شانس برد اسپانیا را ۶۱.۷٪ و کرواسی را ۱۸.۶٪ برآورد کرده و احتمال زیر ۲.۵ گل را ۶۶.۹٪ می‌داند.
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
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/140689" target="_blank">📅 12:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140688">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/140688" target="_blank">📅 11:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140686">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d2810e6e.mp4?token=uUWyvZqF9zOewEIZbbkxzByKUSCuroidjjOiKZJU1No8UB8HzXSpTMbcxVzZ9l96VkFOoOKCmQxXBot36UFoOrt_YrOpifDxOui2yw_olflcXL6HZE6rM6otMqDH7Vej8wV02EgYNBkRzjvQqQXrZezn79CJFDBKz9lyOtmz4Ds2TNSGYLf3GOUVu4XPGGBTh9aRTwyiYcyBNknIHMLhuXymEW-e9VA8_RkPRYPQuaIQCuPotbamu3La6YbkqBcc0jqS7KwH5u0yRMjJDhzI9XThkDNW1zCFcUrQXAkXEJgGl_zvL2mx1oh_QkNLCemW6WqHPGeTwHoVUcZW-mlrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d2810e6e.mp4?token=uUWyvZqF9zOewEIZbbkxzByKUSCuroidjjOiKZJU1No8UB8HzXSpTMbcxVzZ9l96VkFOoOKCmQxXBot36UFoOrt_YrOpifDxOui2yw_olflcXL6HZE6rM6otMqDH7Vej8wV02EgYNBkRzjvQqQXrZezn79CJFDBKz9lyOtmz4Ds2TNSGYLf3GOUVu4XPGGBTh9aRTwyiYcyBNknIHMLhuXymEW-e9VA8_RkPRYPQuaIQCuPotbamu3La6YbkqBcc0jqS7KwH5u0yRMjJDhzI9XThkDNW1zCFcUrQXAkXEJgGl_zvL2mx1oh_QkNLCemW6WqHPGeTwHoVUcZW-mlrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
⚽️
بیرانوند: سربازی من نهایت ۵ماه است!
❌
فجرسپاسی؟ شاید اصلا به تیم نظامی نروم/ کل سربازی من با کسری‌ها 5 ماه است؛ در همان تبریز به پادگان می‌روم و با تراکتور هم تمرین می‌کنم!
🚫
❗️
۲۱ ماه خدمت چطوری و با چه کسری‌هایی یهویی شد ۵ ماه؟ بجز تاهل و ۲ فرزند و راه دور[سرجمع ۹ماه کسری]، چه سهمیه‌ای گرفت یهو؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/140686" target="_blank">📅 10:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140685">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
یک شکایت جدید از استقلال؛ پیکان این بار از ماشاریپوف شکایت کرد
✔️
باشگاه پیکان مدعی است نام ماشاریپوف فصل گذشته از لیست استقلال خارج شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با خودروسازان غیر قانونی بوده…</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/140685" target="_blank">📅 10:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140684">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
❌
تا نیم‌فصل بیرانوند میتونه به‌ صورت کاملاً قانونی و بدون هیچ مشکلی برای تراکتور بازی کنه!/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140684" target="_blank">📅 10:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140683">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
فوووووووری از بیرانوند: چرا فکر میکنید سربازی نمیرم؟ 3 ماه معافیت تاهل دارم، 3 ماه فرزند اول، 3 ماه فرزند دوم و 3 ماه دوری راه تبریز تا خرم‌آباد و یعنی کلا حدود 6 ماه خدمت دارم؛ اصلا شاید نرم تیم نظامی برم پادگان تو تبریز و بالا برجک وایسم موقع مرخصیم میرم…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/140683" target="_blank">📅 09:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140682">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
فوری و رسمی/ دلار 250 هزار تومان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/140682" target="_blank">📅 09:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140681">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
✅
بازیکن پرسپولیس نیامده جدا شد
🔹
فرزین معامله‌گری که از تیم شمس‌آذر به پرسپولیس پیوسته بود، با توجه به مشمولیت، برای گذراندن خدمت سربازی راهی ملوان بندرانزلی شد.
⏺
پس از پایان دوران خدمت سربازی، وضعیت ادامه همکاری او با سرخپوشان مشخص خواهد شد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140681" target="_blank">📅 09:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140680">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
زنوزی علیه کیسه
❌
زنوزی: کیسه خیلی جام دوس داره بیان من پولش رو بدم  برن منیریه برای خودشون جام بخرن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/140680" target="_blank">📅 09:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140679">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O34gyaIydpp1TqXrgW8IjqHlXCeACOp3DYilY49aYXpZ1lLYerorGI1zwci17rpdMd0IPyH9vnpvJv7kI5nzj7AVFhJCKWbqXoYMJhy-pDl1QiT46oenXDnr7ay-9rIOKQ9qtfFZa5hRMgIcfagEs2ghnnA76Kwn1QVnaSYLTRyXGYKWZJsg3_yObEwTkqWMeIJT_3_6jFbsKxj-1GUvL9ZxVrYdoYQKziYMBz8p7D2b8b4vKO0Y6uK1V7QUwPtclUVTk-tTddEY-tff956YxUOCOBDlmaT90P1-OhSe8tmNGdRw4Snd1WOPIteqVjrFwXGLmCR2Ug_Ucz7k_MUlkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/140679" target="_blank">📅 09:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140678">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O52zqxChJDLrhO8Cfee-8rvlPC3Nu0UGkngKHo53NwLnGnmPKNGTj0KSaLKZPEbGrycvdsbPr-NufQ0XyCtxJ2OcOm0W327d9mKj05IJV0UvsV2Lm2YkDVo9-Vya311HkBQlz5HO1Rr0-9uV_yiHAZGcn0XA7oWrphZRQwbraFF05hiAnvRbIzcXVheRTAE0LfZwTUS-RjjpeOpuiFWF-LkfHXSlK5ZBrtTjaZpDh9Gg5szkPN2SrbxDzfB_Socu-p1CkwtFEEqoE8z-aASRbrVpRxVwOKAJx7VhRWfp19GiT4VOgTnyMeenDHfjfY-wQcawBq0rn4D7WClZVNGPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Russia -
🇮🇷
Iran
⏰
Tuesday 19:30
🏟
Ak Bars Arena
⚽️
روسیه با فرم هجومی بهتر وارد بازی می‌شود؛ ۳ برد در ۵ دیدار اخیر و میانگین گل‌زنی بالاتر، نقطه قوت اصلی این تیم است. ایران در مقابل تیمی است که در انتقال سریع و ضدحملات می‌تواند خطرساز شود. تقابل‌های اخیر دو تیم هم نزدیک بوده و در ۴ بازی آخر، هرکدام یک برد و ۲ تساوی ثبت کرده‌اند؛ بنابراین انتظار می‌رود بازی درگیرانه و کم‌فاصله دنبال شود و سناریوی گلزنی هر دو تیم دور از ذهن نباشد.
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/140678" target="_blank">📅 01:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140677">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
فرزین دبیری عضو هیات رییسه فدراسیون فوتبال: تراکتور، پرسپولیس و سپاهان مخالفت‌هایی با قهرمانی استقلال دارند
✔️
✔️
اینکه ما از الان مخالف قهرمانی استقلال هستیم، اشتباه است اما قطعا مخالفت‌هایی در مورد قهرمانی استقلال خواهد بود چرا که سپاهان، تراکتور و پرسپولیس…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140677" target="_blank">📅 00:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140676">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🔴
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه کیسه، قبل از اردوی ترکیه تیم ملی بزرگسالان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140676" target="_blank">📅 00:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140675">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140675" target="_blank">📅 00:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140674">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=BfWW7BaevpbyHwpYGWvKy5_UXF1SNfz91ne_O84BumfcV_9bqwYoG6e-GR3cLbnqrPXMGey5UB_smMuPPsJxNPfeQ0jp6iFpCfn1XYb5ENH1lAQvu8ZIqB4j7X_U0_rWthu6SJfZFtj7wNmwiGHZlbhSXjhAk4D-D3F0eAYGMKUYjhwrMTPyKQRwRnMle0T3sc_JMhS7qRYFEV55DKGkoH3XHwXrer2mLR7bcCwyD8dol2_n4DiQORJh5enfTmju61cWz5ZUyMKjaG5X5HBRVQch8wlL8ON3IOVrXtLs-y4Xd9zgYrWUS2g-PxJPBmkRCH328fWzaAnxcuZJjUIg8UE7wp9C1dAkMjRLY7Ls5oDwc0TzVo90pYjXjW1OjjKp5O8MMmDJkh-xgrYapJbKQ8DauLnX0c5_W8TavqRNscfWm5xNOZuuN1PMQ_Tp3lu7-bYWstxCmy-VoVdwB4nYqE2qZgtetXBWiPL0f0sKPMiRqOBzyNa_NzGzXplBXWxE_jLLA5dIrw0cDOIMO60zRmyvzgQxNKxhm3sQ2ux7KumihZ2Djcg2qFqG43-nAo6B_lig9HWvTbeWsV5m8gm-_ASNO6OR0SvRPYO3g_h3Hb_RNB0D8Ed1lPhrtK8n4yWcBNUktqzlNJHqOmIOWxKeKSwLJTcW4R6LkMgvj0q5u2s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=BfWW7BaevpbyHwpYGWvKy5_UXF1SNfz91ne_O84BumfcV_9bqwYoG6e-GR3cLbnqrPXMGey5UB_smMuPPsJxNPfeQ0jp6iFpCfn1XYb5ENH1lAQvu8ZIqB4j7X_U0_rWthu6SJfZFtj7wNmwiGHZlbhSXjhAk4D-D3F0eAYGMKUYjhwrMTPyKQRwRnMle0T3sc_JMhS7qRYFEV55DKGkoH3XHwXrer2mLR7bcCwyD8dol2_n4DiQORJh5enfTmju61cWz5ZUyMKjaG5X5HBRVQch8wlL8ON3IOVrXtLs-y4Xd9zgYrWUS2g-PxJPBmkRCH328fWzaAnxcuZJjUIg8UE7wp9C1dAkMjRLY7Ls5oDwc0TzVo90pYjXjW1OjjKp5O8MMmDJkh-xgrYapJbKQ8DauLnX0c5_W8TavqRNscfWm5xNOZuuN1PMQ_Tp3lu7-bYWstxCmy-VoVdwB4nYqE2qZgtetXBWiPL0f0sKPMiRqOBzyNa_NzGzXplBXWxE_jLLA5dIrw0cDOIMO60zRmyvzgQxNKxhm3sQ2ux7KumihZ2Djcg2qFqG43-nAo6B_lig9HWvTbeWsV5m8gm-_ASNO6OR0SvRPYO3g_h3Hb_RNB0D8Ed1lPhrtK8n4yWcBNUktqzlNJHqOmIOWxKeKSwLJTcW4R6LkMgvj0q5u2s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت شکایت کرده است
🔄
🔄
در همین راستا این ایجنت قرار شده است مدارکی به پرسپولیس درباره فسخ آسانی بدهد و همچنین این بازیکن به پرسپولیس ملحق شود و مذاکرات حتی تا پیش قرارداد هم جلو رفته بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/140674" target="_blank">📅 00:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140673">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
علیرضا بیرانوند: چون من تو یک تیم مدعی بازی می کنم این همه فشاره که به سربازی برم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140673" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140672">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140672" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140671">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTZmV1rM0TGPSnnp1MOU9z-zTsViJVmMpfOqDoMKnZshuoT45YL0uEoE-kIe_pdsp5yMIuBS_U-hd0L4tHpvXDKqEFZKfWGHgF0wSJxQEueTyIyPSVkqFIgzWExrbZszwnviAmNjRDEpDNQcrvugc6PSO2u3gofCKYrT_1nYbwmJ41cE1n5mFIo1YxiqywkxfjGp8CYFf9Q_lnxQREaX2MJ2et2XAYNK7M5b_MnVgPpv7pKbeNPj0a0rvJ-kqSC4D6Gu2fbLEpAo2ucxdpmHVF3JDX_WKk8wx0CPHG0iqhR_X0J5gbKkdZK37RSgxCQdAzVbaldZDqDaEUN2pQKIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
وارد فیفادی شدیم، شخصا از فیفادی نفرت دارم چون پرسپولیس لذت دیگه‌ای داره برام
❌
میشد که قبل از فیفادی یک برد دیگه و یک بازی دلچسب دیگه از تیم محبوبمون ببینیم اما کارشکنی‌ها جلوی برد دلچسبمون رو گرفت..
❌
دم تک تک بازیکنامون و کادر فنیمون گرم که کاری کردن وقتی بازی پرسپولیس رو نمیبینیم بجای اینکه خوشحال باشیم، حسرت میخوریم که چرا چرا چرا یه مدت نمیتونیم بازی تیم خوب و جنگنده‌مون رو ببینیم..
❌
بعد از فیفادی میبینمت پرسپولیسم؛ منتظر بازیهای هجومی‌تر از قبل و پر‌گل تر از قبل هستیم آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140671" target="_blank">📅 23:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140670">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140670" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140669">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
علیرضا بیرانوند: چون من تو یک تیم مدعی بازی می کنم این همه فشاره که به سربازی برم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/140669" target="_blank">📅 23:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140668">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
علیرضا بیرانوند دروازه‌بان تراکتور : من نردبونم و همه دارن ازم بالا میرن کینه‌ای که بعضیا از من دارن کینه نیست علاقه و دوست داشتنه.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140668" target="_blank">📅 23:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140667">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
#فوری
🗣
خبرگزاری مهر : تعویق خدمت شامل بیرانوند نشده و او رسما از 1 مهر سرباز غایب محسوب شده و هر گونه بازی کردن او غیرمجاز است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140667" target="_blank">📅 23:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140666">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/140666" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140665">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
💙
💚
یاسر آسانی خطاب به عادل فردوسی‌پور: من میدونم که طرفدار پرسپولیس هستی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140665" target="_blank">📅 23:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1981c5068c.mp4?token=P06FT7WNnYVsZUCiU8-6heE0bbVHo0ezGocLXSvDQYqkfQuQGSfEp95BEX5qXbpJbnIZFUTUc4xNSvuFFL7UQqgJGeQWrwAqYYMiSURrr590LgG5KEbEvOB7mfk59WrBh85Bh42Kri71Ilzg_lybo0Zv3yiAc62vkOT7j8BOujknVmaeq0e4bWa7IVaMRCCtRJ__PxRo0-g8Ykg1sUz5rgowzey7aU1cGZDgXyJGQL-RG_W2VfcWx0DI6X1rB8DjxNp8BcaeIPIWUxsTkSKy1Yb6DiAG7XbZ1N_bT-VgVJfTwBdyoz6JXUSjqJH6GB7jLCmM7-U6jM5OWvcWWBGu-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1981c5068c.mp4?token=P06FT7WNnYVsZUCiU8-6heE0bbVHo0ezGocLXSvDQYqkfQuQGSfEp95BEX5qXbpJbnIZFUTUc4xNSvuFFL7UQqgJGeQWrwAqYYMiSURrr590LgG5KEbEvOB7mfk59WrBh85Bh42Kri71Ilzg_lybo0Zv3yiAc62vkOT7j8BOujknVmaeq0e4bWa7IVaMRCCtRJ__PxRo0-g8Ykg1sUz5rgowzey7aU1cGZDgXyJGQL-RG_W2VfcWx0DI6X1rB8DjxNp8BcaeIPIWUxsTkSKy1Yb6DiAG7XbZ1N_bT-VgVJfTwBdyoz6JXUSjqJH6GB7jLCmM7-U6jM5OWvcWWBGu-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💙
💚
یاسر آسانی خطاب به عادل فردوسی‌پور: من میدونم که طرفدار پرسپولیس هستی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140664" target="_blank">📅 23:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140663">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
یاسر اسانی: ابوالفضل جلالی بهم زنگ زد گفت نمیایی پرسپولیس؟ گفتم حاضرم از ایران برم ولی به پرسپولیس نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140663" target="_blank">📅 23:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140662">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
ورزش‌سه: پرسپولیس به سند جدیدی تو پرونده یاسر آسانی دست پیدا کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140662" target="_blank">📅 23:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140661">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
پوریا لطیفی فر: از بچگی رویای پوشیدن پیراهن پرسپولیس را داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140661" target="_blank">📅 23:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140660">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140660" target="_blank">📅 22:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140659">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
خبرورزشی
❌
❌
باکیچ با وجود عملکرد خوبی که در فصل گذشته داشت، به اون صورت مورد علاقه تارتار واقع نشده و احتمال جداییش کم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140659" target="_blank">📅 22:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140658">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚽
🤩
سپاهان باکیچ را می‌خواهد!
❌
گفته میشه سپاهان به‌دلیل عملکرد نه‌چندان خوب هافبک‌های فعلیش، دنبال جذب مارکو باکیچ در نیم‌فصل رفته و محرم نویدکیا هم تأکید زیادی روی جذب هافبک پرسپولیس داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140658" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140657">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
تسنیم:
📰
جلسه امروز فدراسیون که به گفته رسانه‌ها برای تصمیم‌گیری برای جام فصل پیش بوده ؛ اصلا راجب به قهرمانی و اهدای جام به استقلال نبود و این موضوع در جلسات بعدی فدراسیون مطرح میشه!!
❌
احتمالا درباره مربی تیم ملی امید باشه
👀
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/140657" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140656">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyplVDsZEI3SIgigvC5pM3TgZPUkqVyzl0_Df8VF9dHG3WofaQB3r5XqJ6YEtdIeMqqmdX5tocd44nH5MZqzE2Ko_QXz6MwmqBQkc4ymGVq_ZgWwHqfOitOBvXZfTZpUPZYLUCX95RxXEPSGP-RD84iGp3Q_NgNk8lzDuw18goH3eHHHNskUaj8Dii2m2bd8KlC4Jed4uzuqOBB8VrwquY0TjY_5iLrHLMQWk0XrQN9LYHB-_ZcOYEc_my4qYjkuTKtsWa7oeSGC7eQ_0tZVkCXoftmYmZsqPWojNrHmvhI2EeIZc2xMHiECc2bmi0HAiUv8TtrI2fV9TzDlymr-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Belgium -
🇫🇷
France
⏰
Tonight 22:15
🏟
Roi Baudouin
🇪🇺
بلژیک در بازی اول با ۲ گل و ۱۹ شوت ایتالیا را برد، درحالی‌که فرانسه با برد ۱ - ۰ مقابل ترکیه وارد این مسابقه می‌شود. فرانسه در ۵ تقابل اخیر ۵ برد داشته و در این ۵ بازی فقط ۲ گل دریافت کرده؛ ضمن اینکه امشب بدون امباپه بازی می‌کند. از نظر روند، بلژیک در خانه ۶ بازی شکست‌ناپذیر است؛ بنابراین انتظار بازی نزدیک و کم‌فاصله از نظر موقعیت‌ها می‌رود.
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
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140656" target="_blank">📅 21:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140655">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140655" target="_blank">📅 21:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140654">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
پاسخ مثبت پرسپولیس به برگزاری جام حذفی بدون ملی‌پوشان
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی حتی در صورت غیبت بازیکنان ملی‌پوش موافقت کرده و خواهان برگزاری این مسابقات در فصل جاری است.
❌
با توجه به فشردگی برنامه مسابقات و حضور ملی‌پوشان در اردوهای…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140654" target="_blank">📅 21:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140653">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMElwCyDA9h5geTnw6hKqJtriXbreLSWeoreLeN33lidYf6lVHfREShaXA37Q4O8pqs26qwVqtiFFYPh2S50I0L-AQgg2JoAO89B42cxkwIIReIumMoUJLmynf7keWTHRbklLtcZK9RhCKk6bmprkQ0VHThffoV-RMAojFQ2RLEheiFKnJVIZvDPHVZpgkKf-Ftpy52jkVkEFAw1Lwxz6Jho9nzxpj9hwx_OSpXefICiYVCTL8fPiDXCCWu-XfUgJuT_tQJq1y0HaI-5gpjTtONBY9rvpe_gP8iwLBaPTbp0ElzxDs4r-jK0IdsH_u6dewV1WvVV5oM3xMyG9Ipxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت دنیل گرا به تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140653" target="_blank">📅 21:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140652">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
رسمی:با استعفای حسین عبدی موافقت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/140652" target="_blank">📅 21:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140651">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
افشین قطبی نزدیک‌ترین گزینه به هدایت تیم امید است.
🤝
فوتبال ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140651" target="_blank">📅 21:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140650">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
✅
واکنش فدراسیون فوتبال به اظهارات تاجرنیا درباره جام قهرمانی فصل گذشته
❌
❌
اظهارات علی تاجرنیا، رئیس هیئت‌مدیره استقلال، درباره وعده اهدای جام قهرمانی فصل گذشته به این باشگاه، با واکنش جدی فدراسیون فوتبال مواجه شده است.
❌
❌
پس از موج واکنش‌های مجازی و اعتراض…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140650" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140649">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همه هواداران پرسپولیس از مدیران باشگاه عاجزانه تقاضا دارن تا ماجرای یاسر آسانی رو تا ته تهش پیش برن.
🔺
آخرش اینه که یه پولی میخواییم بدیم و رای هم صادر نشه به نفعمون، این همه پرونده بوده که هزینه کردیم و باختیم، اینم روش
🔺
دقیقا از روزی که فهمیدن…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140649" target="_blank">📅 19:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140648">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
پاسخ مثبت پرسپولیس به برگزاری جام حذفی بدون ملی‌پوشان
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی حتی در صورت غیبت بازیکنان ملی‌پوش موافقت کرده و خواهان برگزاری این مسابقات در فصل جاری است.
❌
با توجه به فشردگی برنامه مسابقات و حضور ملی‌پوشان در اردوهای…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140648" target="_blank">📅 18:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140647">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✖️
گفته میشود باشگاه پرسپولیس برای تمدید قرارداد 5ساله با امیرحسین محمودی و 3ساله با پیام نیازمند به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140647" target="_blank">📅 18:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140646">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
✔️
✔️
✔️
❌
جواد عطایی، سامان نقیبی، ابوالفضل شیرازی، محمد حسین پژوهان،‌ پوریا آزاد رنجبر و محمدامین دهقانی بازیکنان تیم‌های جوانان و امید پرسپولیس بودند که امروز در ترکیب سرخپوشان به میدان رفتند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140646" target="_blank">📅 17:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140645">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdp9CwRgUJvODhPv-PZg4ghhW5h0gunomP6-jo6w03i2_CrBirwFeg1OBEF6ZmtRgL2KlKl8r200TQ_WEpB2ArA46W2nr4SmlubPBpzAf4WTYUrKlYjGoVB_hZD97L5GpOmktPppKfHH9n0J5KDt_lLmrF0s7P5XofXqLMBgd9iV_kf5Q-YF3KzL7wDRe9OA23TIwv4y57coeheMp5TTeFwpvtN9heR8_2Iv7zT17YqRdaGdltxO4LD6QVAfczJzqOhHyrQy_Fxu_HxWudJ6FOKQV96ckd-JCqYtofnjlzK1OMf6XarFQav3yza1WJQLWrxpWivIykT2f1GlsqP5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
آتزوری در برابر ترکیه؛ نبردِ کنترل و غافلگیری!
🔥
⚡️
[
ترکیه
🇹🇷
🆚
🇮🇹
ایتالیا
]
⚽️
تقابل دو سبک متفاوت؛ ترکیه با بازی مستقیم و انتقال‌های سریع می‌تواند دردسرساز شود، اما ایتالیا در کنترل توپ و سازماندهی دفاعی دست بالاتر را دارد. باتوجه به کیفیت دو خط دفاع، نیمه اول می‌تواند محتاطانه و کم‌گل دنبال شود و جزئیات کوچک روی نتیجه اثر بگذارد.
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
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140645" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140644">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
#رسمی؛ صابری عضو هیئت ‌مدیره پرسپولیس شد
⚪️
⚪️
با استعفای اردوبادی، حسین صابری به‌عنوان عضو جدید هیئت مدیره پرسپولیس معرفی شد. سمت دقیق اعضای هیئت ‌مدیره در جلسه آینده مشخص و بعد از نهایی شدن در کدال اعلام می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140644" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140643">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
مدیران پرسپولیس آماده ارائه پیشنهاد تمدید قرارداد ۴ ساله به اوستون اورونوف هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140643" target="_blank">📅 16:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140642">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
❌
فوری؛ بیژن مرتضوی که چند ماه پیش در فینال جام جهانی برنامه اجرا کرد، پس از چند دهه حضور در امریکا دقایقی پیش وارد ایران شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140642" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140641">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
بیفوما با ساخت ۱۲ موقعیت گل، یکی از خلاق‌ترین بازیکنای این فصل لیگ بوده
🔥
🔴
اگه نصف موقعیت‌هایی که ساخته تبدیل به گل می‌شد، با اختلاف بهترین پاسور لیگ بود!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140641" target="_blank">📅 15:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140640">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140640" target="_blank">📅 15:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140639">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140639" target="_blank">📅 13:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140638">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
جلالی دوباره مصدوم شد
‼️
🔹
ابوالفضل جلالی در جریان تمرینات اخیر پرسپولیس بار دیگر دچار مصدومیت شد. البته شنیده می‌شود مصدومیت جلالی جدی نیست و بیشتر به گرفتگی عضلانی شباهت دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140638" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140637">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140637" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140636">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
اجرای بیژن مرتضوی در کنار ارکستر فیلارمونیک بین نیمه بازی فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140636" target="_blank">📅 11:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140635">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc2b8cd01.mp4?token=ZdG6LwF4PoHk7AK8WE-ajRaNuaGLPOUIP7fKkd5J6btd8F1IS4gVBEI8eIBTW_rnLYnrf5dpa7wuDwHSijSl-yytLCeXncawiCoa0eKaakBkzdu3aW1Byn-UNroRy4GCxJBpDctLykHFciGyfZ-OWnCqfaTuvbILSCD6_cCjZI-tDLJpTvDkVITyatJNvuJdf0IoYKWRaEA0ny0-UkE0ovl6a5PNdWR07_hA2iJbUcwBpkpqEA0nJ7b0D6GcfIPiGUsC6SNzH7i1vvEVQldOgzolPJOjAOKwUlEUBUVB59k9VoZmIkCxqMVf8L_0LXML_u3TKPUM9mNP91C0cUOqBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc2b8cd01.mp4?token=ZdG6LwF4PoHk7AK8WE-ajRaNuaGLPOUIP7fKkd5J6btd8F1IS4gVBEI8eIBTW_rnLYnrf5dpa7wuDwHSijSl-yytLCeXncawiCoa0eKaakBkzdu3aW1Byn-UNroRy4GCxJBpDctLykHFciGyfZ-OWnCqfaTuvbILSCD6_cCjZI-tDLJpTvDkVITyatJNvuJdf0IoYKWRaEA0ny0-UkE0ovl6a5PNdWR07_hA2iJbUcwBpkpqEA0nJ7b0D6GcfIPiGUsC6SNzH7i1vvEVQldOgzolPJOjAOKwUlEUBUVB59k9VoZmIkCxqMVf8L_0LXML_u3TKPUM9mNP91C0cUOqBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دلداری خیابانی به بیرانوند قبل خدمت رفتن
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140635" target="_blank">📅 11:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140634">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
فوری؛ باشگاه پرسپولیس درخواست مدیر برنامه‌های یاسر آسانی از پرسپولیس، پس از فسخ قرارداد با استقلال را هم به مدارک خود اضافه کرده و خیلی امید دارد که سندی بر فسخ قرارداد آسانی باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140634" target="_blank">📅 11:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140633">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
رسمی:با استعفای حسین عبدی موافقت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140633" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140632">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140632" target="_blank">📅 09:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140631">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
فوری؛ باشگاه پرسپولیس درخواست مدیر برنامه‌های یاسر آسانی از پرسپولیس، پس از فسخ قرارداد با استقلال را هم به مدارک خود اضافه کرده و خیلی امید دارد که سندی بر فسخ قرارداد آسانی باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140631" target="_blank">📅 09:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140630">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
❌
مدرک جدید پرسپولیس در پرونده آسانی، پیشنهاد رسمی اینجنت او به پرسپولیس بود.
❌
❌
بعد فسخ، این پیشنهاد ارائه شد با این مضمون که او با استقلال فسخ کرده و پرسپولیس می‌تواند برای جذبش اقدام کند.
❌
❌
مدرک از این معتبرتر ؟ / اگر باشگاه پرسپولیس با رقم عجیب و غریب…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140630" target="_blank">📅 09:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140629">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✖️
✖️
#فوروووووی
✅
سپاهان به جمع مشتری های ایرانی بشار رسن در نیم فصل اضافه شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140629" target="_blank">📅 09:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140628">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtWDTPJVF9vBYrJqzjH1jQMhyvhMmpzVZtnVA6sCMlc9BSlwtPyJKrx-4D35vQoxZkl3F-NrZtQb0TwOPrtZ3JQMpQNPJkpBB0MeFJ6Jo2eblHkxUtppaJsQs3Vwi1k8Y_JMrx0kEdaLxkYEDoSwz2SxB8DkA28RlupSU5V2ZxABo1PoTNPpMeKfzMf41DRULhomTSHlEFuJrqI-tfhWqmIJU_dBRLXcqhzx-VZv7xyqOI2-a8YYkiDmP1T8Q-avia8uI2TE7Y5C8JQk0kFEn92kq7ArLE7TbWeyxvfC_-J7towMEDCXke_VqKkFUtLLIuxsAYZHy8Vi2gGG-vDPeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140628" target="_blank">📅 08:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140627">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN022pdJ6ARgYuxPbwNULxtfJR-BGmFAabXa7dVSgKxTE_MdlrWWodH6wWzteEG9J7Nmg5gKwlUemnnd8jN0v1PbAeyURCCwmDBgWMKdbsIj0JGCWgC4wX8vYZ7q3S_rKe3MJkHWR2U61wMYe7IjzQ2Qon7T4kLwbtjKKNL9LdUtVVCSKi4H7w-e8eq6Py4T9j4J1NIMPckz45VNV9K8P47KXqlR7UDgEpVXv6HklJgVvsq-T8_WPt0xYM12gh0htVK5QZ88tqDpqHUSvwAasbqfYRbwX1PRfRVMV5kRzrUGHHWxwEMVDGash6tUlmpvIkXFjHn0Ts8zu6111xDkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد جذاب خروس‌ها و شیاطین‌سرخ؛ جایی برای اشتباه نیست!
⚡️
[
بلژیک
🇧🇪
🆚
🇫🇷
فرانسه
]
⚽️
فرانسه در ۵ تقابل اخیر مقابل بلژیک شکست نخورده و هر دو تیم هم شروع خوبی در این دوره داشته‌اند؛ بلژیک ایتالیا را ۲-۰ برد و فرانسه ترکیه را ۱-۰ شکست داد. بازی در بروکسل است و بلژیک با فشار تماشاگران احتمالاً شروع تهاجمی‌تری خواهد داشت، اما فرانسه در انتقال سریع بسیار خطرناک است. با توجه به ۵ برد متوالی فرانسه در تقابل‌های اخیر، سناریوی بازی نزدیک و کم‌گل محتمل‌تر به نظر می‌رسد.
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
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140627" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140626">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKikyZ7dl6v5Sr-YS3a2fYwBz77I4VN_n6jXGTIorgmROhviOrwR_HC4ZLcPxzMRSHVh1t6SnFoRJiE3nl0kt0IPzyLSCEkKPJLH3jqpRTiJzUeXxvX3dVylQZC6iv-f3lOx82XD8UZJRb8G_TNrhAqdQbRLbjaqkvtgtDD4R-UtOa5qmttwNQeIkLfcp7NFeNA_lXccegkeuiVPnoD5S7_s7we_Q5EKXREzTtJOvvPOzXD27X0QpZHb-k1qX6GHFgNubPdl-ZPXa1dXdIEC7tSyPzq16JwXBH5pyY43IcrDExLNkhESL5vERe8B8hAfrdQHprl-oRmex2ZyoKITtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
🔴
با دستور پیمان حدادی، شورای هواداری تشکیل شد تا صدای هوادارا رو به باشگاه برسونه و پیگیر خواسته‌هاشون باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140626" target="_blank">📅 23:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140625">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abF1shBtirCIuqAwkA8TBiYOHc6zvPbKVSApcpCHVYUg2ZutXmMdufcjm-owt3Y-0y4iZHbjbcXRdx1ifoMQysoRPuhRUbMGUZU3CJ4SOdHc7_iSBw2sk3i8P32A2XsUGhzwRXm4txuFOhorIUuIzvZnfHRv5hy4_yxplKsWSnFq_BRI9mzNHN3I3Pkr0dB89orJ2074HjBxq1jVwcjre6w7-XaKE__MLZYqdu-YhXcTMXUW840wXDg2lLqZETpCSQrQwPIecCJhlRGK6jnx-ubVtKA-E9_xWiRpF2Fv3WlfEVjx0TYJTZY1zxB13RB5q3fv_gQW7CMrUdmXpBvuIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☑️
آقای فکت رسانه‌ای شما خواهشا از آسیا و سهمیه صحبت نکن که خودت با اون باخت ۷تا مقابل الوصل به اندازه کافی آبرو ریزی کردی بعدشم از سهمیه ای صحبت میکنی که بهتون هبه شده مثل پنالتی های معیشتی‌تون
❌
❌
شمایی که باشگاهت که با وجود ۶-۷ تا خوردن تو آسیا حرف از تخصص می‌زنین ، هنوز ۷-۸ هفته مونده به پایان لیگ خودتون قهرمان میدونین و دارین گدایی میکنین، جام ندیده های بدبخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140625" target="_blank">📅 23:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140624">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
❌
❌
❌
❌
❌
❌
❌
🚨
اورونوف در تعطیلات موفق شده ریکاوری خوبی رو پشت سر بگذاره و از نظر روحی و بدنی دیروز  آماده نشون داده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140624" target="_blank">📅 23:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140623">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140623" target="_blank">📅 23:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140622">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfce03f041.mp4?token=QsCV_pex4Jn4Z6odMX4TdrCFlqET3-HHnVw6pibpfNpji5VmMNMOcbjb-7E29_Y2eBhZojf7O6D8QAKTMHpC4vivCeqK3r0-5lzegQFFXpCOb3zmNhr7Ph9surmtPtJP-M1BI99PXyTnDbbE3133bBI6N9wQlsCAeCHlHY3H-O2SwpaWCfIr2sEZVRKxNN2fWLQU7ipCmmUEBNppEy_CmhV4e3F9S9TeK-hEBCsvPR9ngIaFdWKv9FenNvN63krQ3JRHKLy7oZYqvG4NnvZZ62GrfVudbD5UdXAg987-62y_HZWXFnLau5vd5LdYk4AejlNwMCna0OaxJ2p2DJQgQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfce03f041.mp4?token=QsCV_pex4Jn4Z6odMX4TdrCFlqET3-HHnVw6pibpfNpji5VmMNMOcbjb-7E29_Y2eBhZojf7O6D8QAKTMHpC4vivCeqK3r0-5lzegQFFXpCOb3zmNhr7Ph9surmtPtJP-M1BI99PXyTnDbbE3133bBI6N9wQlsCAeCHlHY3H-O2SwpaWCfIr2sEZVRKxNN2fWLQU7ipCmmUEBNppEy_CmhV4e3F9S9TeK-hEBCsvPR9ngIaFdWKv9FenNvN63krQ3JRHKLy7oZYqvG4NnvZZ62GrfVudbD5UdXAg987-62y_HZWXFnLau5vd5LdYk4AejlNwMCna0OaxJ2p2DJQgQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
مدل موی عجیب و غریب یک بازیکن در کونکاکاف
▶️
#ویدیو
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140622" target="_blank">📅 22:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140621">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYZ1_UtSgb4tYyl_k3AWDPaG4wQS92V9JNXIqWsfytQy2tWd6IolX45mTQL8Do8M9L-itoLYRsuGf-BD7qxh_vEyHOAXYIdGCMK4oc6b6qCyeaQ_DhZJ_n5XIM9bdtz66cLuSQRo8RBnybxM_mGAEd-ChT3bcLBX8Nkq-4ZFEntOCvNh-ukM2zfEOWcdkU4T7YDBNQxjtWzLsuI12BW_LYkoPbNEtaSipJdriP4Cw-J0hGUe8cUCrU0pQRGq1nUFB8VlcWWr_BvSazvns_HJAYqaABHXH4jbSESe1W3S6ZZmH0P7VW28Thl5gZIge3M8nOG7L76bUu-xc59I3Zbkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
یادآوری
❌
وقتی قهرمانی پرسپولیس در کرونا درمیان بود‌، منطقِ اعتراض‌شون ٣٠ امتیاز باقی مونده و احتمالِ امتیاز از دست دادن پرسپولیس بود
🚨
حالا که پای قهرمانی خودشون درمیانه، ٢۴ امتیاز باقی‌مونده و احتمال امتیاز از دست دادن خوشون رو ندید میگیرن گدایی جام دارن‌. چرا آنقدر بی‌حیایید‌
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140621" target="_blank">📅 21:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140620">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
تیوی بیفوما:
✅
• سرعتم روی گل به ملوان ۳۷ کیلومتر بود/ سال گذشته اتحاد تیمی نبود و شرایط خوبی نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140620" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140619">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140619" target="_blank">📅 21:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140618">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🚨
هفت ورزشی؛  به استقلال خیانت شد؛ برگ برنده پرونده آسانی به دست پرسپولیس رسید!
🖍
ایجنتی که به باشگاه استقلال رفت و آمد دارد، مدرکی به دست باشگاه پرسپولیس رسانده که برگ برنده این باشگاه در ماجرای شکایت از یاسر آسانی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140618" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140617">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJxSkBey7Rk3sSNABbRSrHEWeIjENB5hy8jmEvZxB8KjBIasNqT9hVS9qO8OvuksYIDGEAKz2G9VS5HUdBgIV0vOcvApg-SheJDLV0M29HyEQByngGBKCjdJRR1En376sYAcBGBR9PSMXRa-9Snj_A6tcoT0TuqtrqkrwUdQHvX0V69V3zdlehtcaCM4oSfBem5yVh9EHoSG63cwYbyGZPdRSLtW-yqMs1KNgwsfAoZ9mfh3etKhZXKEgg0dK_dF-uI7BGizZyuqvQWGBoepUm0BenSbkBMJbULmOD6pZcJAKlirVi7IM381Hpd1gSuocOftiA6ShFZrXzuNU9rftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد ستاره‌ها؛ شبی برای تماشای فوتبال در بالاترین سطح
⚡️
[
نروژ
🇳🇴
🆚
🇵🇹
پرتغال
]
⚽️
نروژ با تکیه بر قدرت هجومی و انتقال‌های سریع، می‌تواند بازی را به دوئلی فیزیکی و پرموقعیت تبدیل کند. پرتغال با مالکیت بیشتر و کیفیت بالاتر در یک‌سوم هجومی، به‌دنبال کنترل ریتم و استفاده از فضاهای پشت خط دفاع خواهد بود.
سناریوی محتمل: گلزنی هردو تیم بسیار بالا می‌باشد.
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
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140617" target="_blank">📅 20:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140616">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
⭕️
⭕️
دنیل گرا مدافع راست خارجی پرسپولیس به تهران بازگشته و اماده حضور در تمرینات گروهیه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140616" target="_blank">📅 19:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140615">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
بالاخره انتظارها به سر رسید و دنیل گرا پس از پایان مصدومیت، طی یک یا دو روز آینده به تمرینات گروهی تیم پرسپولیس اضافه خواهد شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140615" target="_blank">📅 18:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
زنوزی علیه کیسه
❌
زنوزی: کیسه خیلی جام دوس داره بیان من پولش رو بدم  برن منیریه برای خودشون جام بخرن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140614" target="_blank">📅 18:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭕️
⭕️
فارس: آرای هیأت رئیسه فدراسیون به قهرمانی استقلال ۷ رأی مخالف و ۴ رأی موافق داشته و به این ترتیب احتمالأ جام به این تیم اهدا نمیشه :)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140613" target="_blank">📅 18:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140612" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140611">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140611" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140610">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140610" target="_blank">📅 18:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140609">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFzP0RtaSHFMJkMrRkTYIzsRjrIxpKusMREwZ7s33Y5hlkQxskvH-1UvEtgIZbL4tDTE1nDtfFiZUFpNKijreYWEpm6rb6DSbcM4Ud2RmAeQs8UdpxRECcCfDYh2BX4X1TDyCaZJAxNQN6FjOGbV3lgivNLbURA_PI7RpSs24RGzrQoS_lXLP7mdrLokzi-OZzEIsI5qyB6KeLxdhi8Fst5p6uhR7_h15KVO3gUyrLnilj4IvmMs8fxrgJrgRIywsD6Ql52ilB34GZs9dM-CzTmqYDf6ztSSmAy4QFksAVlfotpy10ns3V0qUboCIAY0LmpiwfmDQ1RFHbNTIc1V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140609" target="_blank">📅 16:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140608">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند سربازه و معافیت نخورده و هر بازی که انجام بده غیر مجاز هستش / مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140608" target="_blank">📅 16:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140607">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsCb3fcVEU54WTBR-Gi37X6exNmu8CxppvUYYU3jvWEDubl9KvtwHpbcVRV9samcK7XSj_SqIxuerp3u9wXcNgDbIshppbdKZdMXOKuwN1ug1aUExOG1LfucN8qEsSbAHPwT50mKGUb712AJC1SdvbyXmw5ZGaUi54wq_pvEszQTnmPBhxnqp7FS-I7DSELS6kimQaE9vi56i4srOY_yDFSMikAP6jln1l-wrc1g-oWSzAx1SM4xxTaWfzaLvDOhMvilrwUdrFljb76OtnGBv1XViiw2Lmflqhg0riFom2ZTULSerYZ9FPDPytmtHDMCRLI0p4GgBD0bmLF3zIVgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Norway -
🇵🇹
Portugal
⏰
Tonight 22:15
🏟
Ullevaal Stadion
🇪🇺
نبردی بین فوتبال مستقیم و مالکیت هوشمند؛ جایی که هر اشتباه می‌تواند معادله بازی را عوض کند. پرتغال با تکنیک و کیفیت در یک‌سوم هجومی خطرناک‌تر است، اما نروژ روی انتقال سریع و قدرت خط حمله می‌تواند ضربه بزند. انتظار می‌رود بازی با ریتم بالا دنبال شود و جزئیات در محوطه جریمه، تعیین‌کننده برنده باشد.
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
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140607" target="_blank">📅 16:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140606">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند را به مدت یک ماه تا پایان مهر برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان می تواند  در بازی هفته هشتم با استقلال تیمش را  همراهی کند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140606" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140605">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140605" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140604">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140604" target="_blank">📅 15:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140603">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
فووووووووری از ورزش سه
🚨
اولین خرید پرسپولیس در نیم فصل مهدی حسینی مدافع‌ وسط ۱۹ ساله شمس آذر خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140603" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140602" target="_blank">📅 15:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
طبق شنیده ها
❌
ابوالفضل جلالی مجدد دچار مصدومیت شده و بزودی مدت زمان دوری او از میادین مشخص خواهد شد
😰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140601" target="_blank">📅 11:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⚡️
⚡️
⚡️
رضا شکاری مجوز بازی نداره و صرفاً در لیست بازی قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140600" target="_blank">📅 11:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
امسال جام حذفی برگزار نمیشه و تیم های اول تا چهارم سهمیه آسیا خواهند گرفت!///فوتبالی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140599" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
