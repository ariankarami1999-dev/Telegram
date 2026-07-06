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
<img src="https://cdn4.telesco.pe/file/b1nMRV5r8tXh8ehlKhEoSsS-y5dldVXZ1WGfe7cdItmu3I-bLk9aTAFfj9jZ0Uch3Ge72jVa1xa24DlFRFwixFRZxD0KXJWsfs2ldRnVmTleFLgDtx3653-w3ITJ2rJUrDZk0UPU_543LIe8fBN8t9LAumu5bIqp79ahMWLXj0FBhZ2coSPVLd1Ad-t-UgvIKMUuN9-tLjV0QyptTbfdXf3eRdjQk7f23iUwOtUo8P1FA8t1QlTH9D92RQ1_jlpRkdcDWrEgMvLhW3RbJh2P0_ayXyOdkw2i2tonBxup2ITVYzoPspNS98_Aj9tj1JkaK81h7CUcaFw3bzrp8KBh1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
<hr>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 377 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAyGsqwbpokvrjoakSU4xARjQ0TLcFvc20umYpP36eB_VFBEFdEJifP0-TcPAhR63t-5OKpiKxpdh7670pXjRbhMT3PCgMnooTvliYoOzRlgPYDPBGFH57kuXgOF6P1NHEQa5WYDli7ZRiEsy-4JNDfBO5H8bWpo6fd-SXwlWGDxNlAjVXW-RDin7AepRnG4Z4JbQNSbC24vGqvgcmbxDrMiQled8O_hqsut-rqGROhKVcV4vP63IGYORYj-Z3J5innuvPGXDJ7-d7KHK587x32n0lcvDDOoP_xjLv9o80dN6bwQhgmj7BuvynRVS-_elmnAgUjcIFdG6piIK4nhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 736 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 794 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=tEG0fcMic-94yRW889WJ8HjB7-ercLDvq3oSxqGxJUOsvoQkQ18gvsMP8pIPf3kxeYOfoTU5tvK16LVuPCo3AZ4UwWsTggP8_A2n8hYOW4MDIC1l2Ace_bLXMwZroPCkhNAHDN47Y7s5pJOTFzbfPy8fs1DAHWEhkINuMEfpPiBPh591nLQ6uWo45otiNblovUWT_NPKEWsUtgPD_pK5qjR4bt5reyZuqAEV0MWz3kHfauVMKfi4FgOfu8zNjdPFdwZGqRaYlbZDeI2notcN54B-vtkOiD59Yx40up-llOa28Wq3oEm3Ti3emsHbQlYW4CjGmgEFy_U8cpRXt7vzzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=tEG0fcMic-94yRW889WJ8HjB7-ercLDvq3oSxqGxJUOsvoQkQ18gvsMP8pIPf3kxeYOfoTU5tvK16LVuPCo3AZ4UwWsTggP8_A2n8hYOW4MDIC1l2Ace_bLXMwZroPCkhNAHDN47Y7s5pJOTFzbfPy8fs1DAHWEhkINuMEfpPiBPh591nLQ6uWo45otiNblovUWT_NPKEWsUtgPD_pK5qjR4bt5reyZuqAEV0MWz3kHfauVMKfi4FgOfu8zNjdPFdwZGqRaYlbZDeI2notcN54B-vtkOiD59Yx40up-llOa28Wq3oEm3Ti3emsHbQlYW4CjGmgEFy_U8cpRXt7vzzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvtjbph9S5fhM8FcqZ6XIArH7qM-NOUV5YshojBPa17hGzAZMjZsJCpcSMZ0vTuePzZsrYhpMxpWdjhAcq8bcQ2b52aB2rFDITpkOfSCXdW_bSD53tKBwL0jeQdIf-KTgqUgkTO5-DjdieBaUV5vEixkDmeoTR0W_SPYk8tEnYzTG3Sxl-2uBCdEhiwS15LaCFCnLrK7rofSR6edC2mjGYlH8deDRr1x3FLC7z_6HV9Ys9mBLDcHNAttruFGE6KAy7TOGrHWc1JTguNg5kHnrCb4FrmLs6QG8MrZs2F_AVMI9hxAE6dzVyfxQMHKKG9fIwnDV2lJPaM25AA6-qDpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 650 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 731 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 991 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPgJz-uwlfFpI0cuIocrdQogssWgWGDd4xh3kO3bDAs_VzxpBB_upIo4rCI4lugzlmRciOU32IOoRUqPiCdbLIvjW4V81ZlamWPmD2jJoIfyd6T_ykvbAbfIteUEexQwurVmkRctmzksQqcZJx3nQ8komS8Zclq1VuZeo4v7GMffAnPHiaGdCOMFkh6V9cV6vrYj38YxvwLAHkaOEe6eyD0RMfkG7eaCZBnYPbg10uQwRPFpJkgBkMGf8wrw59-Jf4aHVYWM8owjkQqVsGxxpFA0stBZUCjd97sfL0nGOUAslIQAim7K143Asg-HfADR1YNV9Oyoc1ylIN0rVREmmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSSabcoBIzVEPpR5hcCrEk4Eh9J3AcbA9nn0pdOyW2rerYpa0HT5HXbe7ALGPxy8q1ePhyjRYE7Eqc29lFqDy0JCuCw4lyQySJWlynaTFe6dJavm2GrjV_E6SMVPZLp65eDGn9zNivAstWJVdwpLc0orImccFNx5jGF5x0B5xJDNASg4OAyeoLjnk8X4Hir_6OOyxxC23lr-PskZ3DeNMsUvSc7At9P42yA1PEoSoUjX6UjQ0RKyb8UdwCw83xGgsaYcxu2vchBAkE1iaXPeCpQ2oQdrtFt6eys2xuLSHYc96-LL0NBosuaSOAOURpQg-ff1cbj-cjiP5_X7099-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhTjvSVsKDwF-GvXAIpm0jHi4BQ8VIFfAwxLEDbUAwgai44JDwkOQ-nfjy9_l7bDmj34nBYFtzHYwNqroxSpGIQHgD9w6DkEh1L4WR4ybvUpbhkHW0NOtABFO7AmZjSyO7ETmGZa2iKOEpwWQGM1EvUZmvoMvR8nQR7eENfn-DgrQ5_OgJUASmoaXk4rIdmMm5cwStNNxKAVCf-QWhDrlMXi1s39QF4YBizQx_KAffhkK9jRgabtOIXLs7AnNNBjCVhO3Y0RlP4if-xPGBofBwxplX288OIb7SOpVpJWpSZCFHMHIc5IO6LNpvu_A-IxssATn5AzbYs0CAZ1toHOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezPAGKpbON1v1vzcbGxE-cWjGfXmT511E67sjJIsCDdKuCkHhuIgIaEzrRpWfoE3o4Mf1or_ESTEGcxj4ZdZOZQ15irYt7TbEDJSbUH_lnOa-4tf5_L0Srb5IC8EFbkfHEN1153YgoJ-DfeGPRJPMaZmKrmgcHFJKtCZDSNr3HdUCzq1f3mUMcHTRr2NRgM43PrgOEHkzZr0V3kPL6AAwG4YmgRvd_APhFctruARUkwtIkOgJ1a3aKfhMDKl12WrL7o6L1CmQQCXa0zX48xy3uNJbiohafMlhIInaFwZi2cP-f4rb5H07UTzKq8frkBWBmbtpuwkhkjoS9sTnGM7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLF2DRoBTU-ZUezstkIKfsX2QG5jQ38r1W-hFsCdYy2rSs8PKgMImRNWNc1be9an_7bRHcTiz7VR286O3UOhTWj-ykR55x9um9wAzRG-5NpGGFod6zx2UaQ9FSTzkmlxvo8glWaXxbhBYgvciHRMoUsV77Qgg4yrUeaXTqPCXkSUfXefhoTy9L6TGK7rCievUBG63QegDnP6eV1IYChcTpMvHkIPlfBj_RNFPGRlMBGNCrNjXw4OPvm9HS9eNA2_JzBR1gzT8AchwInRisCt6FFWiwbDE3J7Aq-coaRk8gKvCAv8UpN1buoLlq6kPXC2ipoq17hfdTOgw9rebbg_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeJMNw8KzaFLYa7e2JaVfXHiXvDEeMBtzrKZZ_TDvdHvReBOCmAFsRheQW5eF2Rr3JDU7scXb3dZXdfhuxF3Uqtfv1Vqh8HZT2Y12A5Rdr5byeDFrFKaF38KFBve5aOlBibPU61uweMHXe3JYU6Hd6cX7_Pb9wIWEeCyYDKBvp6LleGrxctGTqVqwIKCJbXYsYMwiDmpla7wah2ZZrkkZF05TJN5EjCYLpZxUe24DsNbbYtUUcLRprv7vqnQyGmwyd0UasdU-5YfjS8IBfc7Bw4fx7HyozA-ans07hFy6ZNZPcA6kv1bp1wdA8xJjjcDOYq8xMGrLxtrvZE7Ho2pyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NVGGOvvMmz1D7ll1ORIlsvA_Oj1QDBvwbMRA6eLyLENkfCQc-WQsEyNpYXLFQj5tml_wRlVCjxIMtWmcXYF3nWgbsL-0Cb2OAZJrt1Zmuq4XARyeP5qWwD5k6kDK34sTWli8hZIZ9iqsGCeOjmhAaudbEEVH4YcFZICDBYWvXCi74193USbzVlcTV6-ei7irlNQZd0CaiqbC6y7mAhSkvqrHMtm4rZ7zFLi3nuBVE4mUjMlJEMvGrylubtUJ-5CRNsRa5IYQEB6dnJcG7nOk8PtmALrYPh8ykKsrd8BDiJVGRQOg8GTJcPAazdPA_pSFsEnEGFRhXTlWs6gtAkmoKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wm8iPBNHFwaCuLNg5u7oXHnawV8GXwy4CiM-aHSi_1UZ8C9yHUiWgdHmndMioKjog3XndhEoanrYWzUd7Lh_ov5WRrKLoA58CdaFvdAkKMihQtFkV5fHlt7d6iFwFDA9lrDQCgAjqd2_AtTOK0RCSTuAzs1IvwEKygrS-I6ddLgY5JsrEYynjBk6rJoYqvfw5139_vQ8lxM-K_NyavQlO1A1IHNLZzZEAIbtIgPXX7ISaAbY-lui59ozM1LDRGUWsfh9E3R7JyL4rjxmWqdcHCP-6L3G48R5_c0HY-exMmr2SMdp0AUvexalYncM5mU8S4GqJ1uPYXvUHKNrFe9D7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmQirAGY04HXSU6hITrLhgIr7PtHKW47X8aA_XdbQI-jjT8V7-rW66b0xURuxF8s7h1Cu2bLMcFlU5ND2pqcHDlPSnhKdUYSSIKSI3vM9-3kMz1WBxFEclCnZwzS0DXgOLFw5KzsFh948Lqh-0n-3NaZsR4EC9_Tq3ibRmnRpGeRG5rJvnYtNWt6KpTxU30ea50iN7GK2xwZbHOYUcteQ0FW3jcmoCPHFwUUJvwnvBO7L7od4bU0a9_qnEWS8PKAa_X2bwuy-5MMDPvgPSW9xP0GM3l_b-m9dJxWEX6w04g64H3ufoWmi_KNwYyTt7bFL0lyXt-N7BnBYdJC_QCZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 889 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 965 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 842 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGruuYukHMHAgXRFeROWHp2O_T36aNe0o8A6wUGMVN9bwqBE2MMoNIReDO2ARDb4_NLJWNv3_WzDIz21ThX1c25kKAcFY6C-kWmj8W1_GrbL4lUFp66JbJaJhM68bnegYji2yFYFCn0sHSL_fOe98QuZ1HGtxndPufq4hfngq2DhSz4zAd-M1fpzEDX5lhFiCAfN0LCglCAGUXv4-2nUnLMnZ-vcTs2x_Z7zXBzQKuYXTohIBX1f6AvHAw3o21ExMAQYxXAM34JiT_kAos0W7Ix1w_nU7iuLMH8tHaueafsOi4Z6PzzU4qqVcW2-f9S1Q2Vgingy9XiKMefUlLS0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 887 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 836 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 777 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFEZVEffigPIbS58vzCbTXk2Uzow8poaXlGkI_Im1jSV5_Zc0HgtK0s9U4sFnYlZ8rdEQudqzD4B1MFYo923EKEN6ZlW5-qyMjAopdGvtcBMWEjPBpaAiVjZK4MiSDTwrOE_FFtwZA08Kb5XSUm-yy52wJcdXE2ZccIaZh5IIO8pIEpX93J5W5Xh-9xh9GAvbCy-Scvd_R-UecdILGhxl8XOIHtH20kPPcU5j0OMzGWTe_zpylqpF-gJMd3k3Cx-WxnDjNAa9lF3rL5Ni-umfvS67aBY2t7bclN0qfTQHZHL4MuI7iE84Rk2FmOLFJ2i6PdSzMESvVww-BDHhGBePQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZxq1c_YUtpgrNs7hGS5edkZTz66T_i30cw2ixAiI_xf9rM6Odejrwg4v52aepKcLRAvMJK_MVbn45O76ZQaKz3Ft76gR_cnkqmTUoZ-YXfwZrPxalt9FHsq30hSw6T60C5sPfpzU6_h1lVPhTGNGe95TEzkUeqpH7D92uQKtksMWyTCv3Q9_QLK-tEMxUAaN3sg3AZx2g3MGz-Cvl6O1ZGU6GT_8-YSS2DNAen9xb5QyuwOFsaNhdvKQxpsZDX1CxNH5BRjzz9Xv0pbqluboeIfusAHM233iDzDKhJzsVv3Ovzq2K9GZt2cewQzq30glYvTPGAF8XDfJZJOlsvPlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJIrSZYnqi_W9BdX371mzJ2fX5J4Q-sckDjhAodml7F5Z22WNIgrgW-d35uNijYIOWmbQtA5dGVc9E5sV0R3v66cDuWn-6HCiMHqw9at9pqLHtZNU2pouy-UVEXpr1_sX5EkoVnqutrbIz5ht9hqBRvwfmsM5SinkhGDvhys9NvxCVLMiOM0tvfbZnM82pCv2MAcInIlppQSjITATQ5a5NfV3R2NUs31yq37rJvnvnGGJo534zHj7I_tDYjIVoyex630-9iJBPu6KLzn2JjEzF3JvA6wtyUv76AisqaTT88BNH8UsjiTvBmBr4yMYwp-ps-XmURczXfwx3gkIEZJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GehZw8QEA3ifTPlssS2XLOIJNxoN-iMJgdl9MzHzg7yHq31w4_Z41S78ArbFCev9R56RROOaFZe221jrmAsCqvZxkg9-hgVZleN7OVDAWFWDSRqbzUIB9Eo4PP1oR-h0p7eRYk3ltqrblkd-e0lf-HqBmTI88Sg7Hq-F5zZiJIQA9YeuAUAufbxQ6gwDH7IwKCKshFtfqmQvZCFcVO6m0hIZhCLK8CJUJQ2kdeuYl5xZO5uVUcKU7XS6cAffmE2BaUc8D1Sj1l-4QwpijZvyWxR1VJDoDGEH093MSH1JGfZCdP1Sd4Gxm8uKRtu99pKYp3gOZX_xudC3otHGAfSLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JY9Jmj0KgQu50xqJeqrG25XwRmGlUtRTKUyjuc2PPbRofu_INgCyVtvQJtjETH8IXr4uH1ObyO1jKd0Sjm731g36eYhk6Kgn_N0JHbAPsNlhTC0z5EfVjhwY_sJ30Ov-rjxOGrC7Nw-EeKLkYKQ-4khMZ9wmFFG9SIe4gHJX2QAB0-eKbzSSeGx9Gy-gBwOoTOO-Hym_e_u7uYgetxovZ30wjotmUkQ2osHaASBvcU4N7LKkkCgstUUeFBATQ2kA_7mfBu96atsng5agXI0gRQ6v7ghMtT-xMmk1dBq7V_33RpoJhcE5x_RhL7tgQhfyJBrVUQ5cfb4-dV0hCT7oKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzFSJnM5uwfB0rG21EWoidTtboXruKO2dnKm5OvpsD7a3lzBfFDmCyPDCNHsC7ntTCyjOrxwN71qxKbs0l4OvBn6RND9qBnq87E9Glop7zUZA9jvQCc2PgYQzvYNzMUEX_XVkrvNmAtqGNT-gQDZnmmNvE2m7CJxG1tUxAirOjCgCzhHYJ08X_15cj3SIIiAipDEX_gBZzNfUwAcrEOiE_9AtPx48kHSLeHp-HQyCA4P0XxVLCNmu3hzdopzSFX3Qk0JIB6wI8XPMTMZM0svOpw6GZHuicYFXKRfz5H01bLr5JxcO8sYgM1VumhvVjTvFpeA6CDzSEuLBlJEfoN-gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaV3b-KDL6eqN35b3rhOqDYIBCWNg6zx8q99_AfT8YOlCXS6nTLIVequxW7kM3y_Vg4IrvEu2YHUVYIe8X4g9as_BVK8ctX9hXfQNVXTxuGFjoghtuvlVHAOJed2fNEcaVK5KVibB_KO4Uv5TgG5edWgKKowL5C7oOMK9zdZ8yx0bwNY0L4t-rILIEJY8QU_c88a9VQHN0jV0ih4FIrz0wc5snZgbM5Y33iyvdTVG_vYlaWjLXWfVmH4nyvDoRTJJ_LKPdNg_FMtkpqJgT7z_jnmAW5FwgHKgwLp3w3ooJJ0fdOOpzdq0l6rG_hLEppYhoxsCL29doS8z9iqb5Ea7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 885 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=FQb-CfGTH_m4Sgx3bb1eONyz_LUHgC8mnZNQYfE5imFUMCKIj43CD6n9wO-WmfGeUQROIfagDsVpGFuM-TbMiwSM6iwLWF5WjaMEPg4DH6poscvKHwsqvJtv5K5UTjsX7K6thBfvgd0sA2rvHXjgCd2H1SL84bED7LeOH-nzzkDzOLrLLXRu4PqLTpgaU3Ps3_4en63z-LSl6J6-kpOSXH1T9VN9Jh_aJfnY5xVXzg3Bkh1GjE6acWiCD7L3mfxLnE_HBLK2Jd9Ml-noHjvvaVGHdD3FGrmOokEVwJf2auUum42r52WBnvfsm3PJT4qUYmad9GThR3SCv78JBdXd-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=FQb-CfGTH_m4Sgx3bb1eONyz_LUHgC8mnZNQYfE5imFUMCKIj43CD6n9wO-WmfGeUQROIfagDsVpGFuM-TbMiwSM6iwLWF5WjaMEPg4DH6poscvKHwsqvJtv5K5UTjsX7K6thBfvgd0sA2rvHXjgCd2H1SL84bED7LeOH-nzzkDzOLrLLXRu4PqLTpgaU3Ps3_4en63z-LSl6J6-kpOSXH1T9VN9Jh_aJfnY5xVXzg3Bkh1GjE6acWiCD7L3mfxLnE_HBLK2Jd9Ml-noHjvvaVGHdD3FGrmOokEVwJf2auUum42r52WBnvfsm3PJT4qUYmad9GThR3SCv78JBdXd-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjeuYFqm9RuV_EeOa76RFBSI4OkIcPSVw60HCECxTSVuJZX5Lghol8edToOi16OFfSF3ZVqGrCNXlm7W9HaaIXojc4Z-9skVM8O-HmOVa5Gacknu7GiC30GUqGA2DvLJOCdkFKH9jWtt-aGX31xPytBO-LJk9iG3xrXfpK9zGe9AVuxMAXB9Fv21-kEB-HH2O3WrQzPaLNdg02S9KWhsdLEEANh0k5jH7KudkdBS10AQwyqfgfqjsFQG4GGjantCbMkKKN20wzbl9DVY5J7wVB_yvVjhQpnYj1XrC5ZZyuZ-vOsA_d7pVzyZiqpTGJk7zZuHb7cXevufwjyiFTP9rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSskyJfD12ezSqcOnrq-rBpFu3mjkFA8NbfgKGHcL_0dkM3hrczTehKDjSUequSje9CtWMxTLpV64N10vhdAdzarpKReGqjpwrMS_74Nj4XSnSjybqaIhgSseyMg7QOyFr5auGXLN1KXNX2SwaW-FDFM36rQbqYIcdHCT91fA4ms_EdkeJPQEJjSxLziUZHUKxTF4hgR0G5oE4pRV0OIFmcjTa_gHeGlf9FQCw_nBl6BiJ4zTV9-10q8lUOsVzSKRw7X7YVf6Zm6NjbwBVrYj9EYNCyHX-ES6w_O3qb0NN139h8IPsJBD-i7qlDjqwYxeXW69lZIk2QtrusPAre3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAh4-VGokNsFmcbfCln1NJ9txia2vx1Ed36s--vccYcm-k9MZeVwkwCsmd8KpUZh4fSIHun-wmyXTOsGlvZblbDBqxPUG9OoSuxGUtRc8uUpTJqJcUK2_ipVvvUg1GQsFF2eOJihdVdrcDe4rNyCOsFOOhr1NOCPQHFPfgrWLMhOJtKu9OGWiuqCBVplohpFe7-PpejXfTuX-bkdnglknawnW-UULDrnMnBRDCtS6kc2477eaGIQOMoorgFyfAjeR3YJGh_KcNRLvb2zAxC13kET_hO22KaiQtt-bXgsT5KWlTN7shN9yekZrIIPPB3JQ0J0EW-HtJU5CGUNp_5qsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bFJEnIejO7uSLeftxCdo3twIPUq5yqCVAfcijDG9E0dJCQZ-7BdOtbq2RLWWWVEstNOrwtWFtJF7us6Tbf4kHk5acZcD28-L1SSpSjX0IHzIbopWSQXF45vkPX8sZtrfU43tLLm6nOGBewM2e5YJSSluHlW6HnAb7n-g3Sxr-ZBk3R9WXZ5nHhR9BhAs6SrxomdKj9UmzPiyqM7znE6JJZauze7nPNKTfsQ5n51ZUykLxJaeiqxO8x3IPwH4fePLOUUT5NVmC7kY6v7NNcyN8b2wRukM-U8pTxnjEh6lcwXR5BUkVUeo1bK58HZL41AAH2xwI-o6c7za7MgbtYLO6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 804 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 992 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chAaLK34Q9qi04PK9TllB3ySisMn2o6TRHA-yDr8bIZ6n4Qzn1PvSvZwhTw9kRwaNyigt_X9k61WUxbapcLdleGmxHgUT1VWxTEu3MHCfSwZfoLB12xBDMPbSIGHuCr89qhfCamDa8yCsdtKLO5Sf1qFpLUABrNcnTpiVgIBhb7QEq1q-Korsn6FEd0VS52itoY3GrQdQp2E-gKSr6N4gMmqUJBk9R42xlFqlGPY6WkXcpdU4Gm71IGwK1ieWRQ4W0OaZ7afwVi3dLZ5tDVAzUxJKgpWXd_EYedzy7ZPJQlwfS5sinrqeHGVySHvXKKr7flNjhTRAw_G3NAsop-BjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnI9nEjTyHsmjxOROe-UPuBdIXl411i_wMHNvOMsIU26--atbdeLijAjw4pE0ldxc13iA6yI849qyJhp2Xh2OyAYxH83VO73xk2WuWpEopSpz3WqYJSSUqlCQ5oB4dIeqdDX6W9HI2YYp4jjEovC9CFkCzVTLKXD0aNESXOoFlQx3gt2oeq6o3TqggF8XKJ-bCKl27eTYcY1WY1jnY8JpAzZc9TH79wK5DGLfJCntuABgT0jU9JeS5uVq764XHVh4Km87YErx6o5qSVSO6pG-Du9z7z66qNy9Vrh8yGOXRrn6aPf6h0RB8jkD5VrxmXaaVcJfFV_QHK2A39dfh6Elg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tP2Gm5f7k6U76RLtq-FC0oF-Q4jYSJzTeUuzcRaqcyIgDqbEIL10WCTO_wu8qGM-sEaG8cXwEt178pGllZW94TdHw7yfhD1fEW8XCKgqo0UR3f58skbeJIQkA6VIQOSUzP5-mexubP0J5wtTUU1lKuuWkaqArAeV9Rx6UTJgj_OzPFSn26ejc2GY-6IXfwdGsTIP9QkUZQaDwctUyKRScoefneuDFTmDJ3iUfJH0mHPHKTDxzWW1-QV1CWffYRff-lwLV_rOrQa0rhJPYLxvC-Ds8TpYknX17VEz7XOgsO1ANhZAEx8SJKT0UMo_rR8I7bF1CfhDfsFBBxZlCnpTZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3kS9lWqI_YsLppkdDXql0cTDwjV2EXKBkdSziu-EfG_945RMhmJL2vZrYD_lnZXB2e-Y-87qJMDBBPMWXYJLh7lFZNaYtinaQBPdheh_X_ukofmcwfnNV6cxAAzDrQXCtvyHyOtBD2P8uYLu-aIBiwofsgSLVBjNB_RSq_gSGB2Hv5EOGce71ctI4srBhS_RxK_MCNclY8EuDZFL3H9W0bskkJe5YN9RotgqiW7eLrwWW7Gea-yxWXYKqaKPGqBUztCfNjiLTHDqeaU7Lfs7HicrB5BsFq81qdsXUlN0tOlLJeF3HXEpu2j2MzYa3CXOeA72LBdAZ8rIP8x8TY6ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 757 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EItnCFCB76dTpSkRDvplS1nFFIDqQOYbzxsncBAHF77suYhfvyvQbS_0KOHWX81r-6q-ysLWlGW66LEYwtNv5ooluLKTKAuPXC7ZDkLpVH_diTNA2WdWuRt6F_-3m7vFpgZN3Sn-NAoRj4UvE7_HD9U-ePJiTpyM1UhCVB0CARqqgHCmnChb4Mq-dLWnMTFfZKbNzG5-G80ih05zNZYYfcnUlih7cniFAa-iBTTyiF5HAQ8qp7349g-L9Wi8DLh9qhD2JgYOHAHptwnNb0CS0yHOoThK0nfOi4O02tMzJS3pt_3dpY5F3wc22fIByOUoYUI5GJXy_zVB__9xKljx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 721 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBwTz2KApOnTWl5Bjtsw4hB4Nki5AN94L8rT5Vev3vdAnra0MPXZ_2AYiXNi95alpA3FeuIUPfkMidUcL3jMuBf1vFz74w0iJrjOstDNtZd3RAeRDqEOpOpPEs1RFz4AxlHepCfhDemVw9fcfNehTDSe2l5N9wAfhGn6uzQNExEBLceq_R3rLFlxwzuDhCa6ewDKbd95LZEaEs8YqifGalaXoX-uh4834b8puxelvZOptrx_9Jgw5TjjDJVNXjFJY9j62UtzDJ_-n4CC4mTPXE29WdBoIkX3hjezPsAYoH5nwWjsoNSK0mWDHLFaL5PFELQo3v8vP4kvl8K79u-7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6cDcWBp6dYy7HaSYy0hlrMNXKMfaBO52ePxksmA-YS067FAX2NaWKRsDzUm01R0F2ItEkBs_aqfg-Kx7_zKjidtNequXTeBbQVn3YdzZnrLMmyePXRXfgFQ_NYkkMLBt2we7LaNRRKJU_q9BomlYRmlYa4O5uIgUggpeY3d0GG9-6rQrzSLHJtuMNpxtAb9VJQhTR1Mo4nDulnSqSICkc7WwFmrbbNS9NAPhIMHkrfGZ1nwHZDJ9RPd0nQg6aWuOLmBUrpD2STzG5dCWOvQGGDpC2IavKc5Cj0ma7itQhXJZWdo2-fCgisf4mRGiDPCto73tqWy0cBWXCl0FSbarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 604 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZ6_25Bd1XuzbJYY-SijIacF7x4Awjg6_R-_QX1nud2GZfSeORt6nl7q-8EkGjcqeS1xKF2EG3h-tUnYbjabQCB63D1jQqveky2IuG5t66tl2KANC_vzT_vEYt8MpV8q86-zYSeM1IrdHJNolqQ9hW5piAK-7_BURV8rMy9_9yuEC2q8gzwh4gygm99j_SZoGYInG3ZadTTtovZRJJ54bA-sz-ko4ylSUWdU_34fBBW5aHY_ZZsEjggD92I9_P-BSk7sBdAwNHPgYXV4QSo6VO4iS5Zjh4TWfv2Q_bPn-rC9gYHLGUCdeLoOhtIFHQI4QzGtbLyhdMpMcWyRhIV0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 697 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 641 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAFx3FFB3HUfnLdH-CnOnbeMG1TK4gQ1PMsXoMH9Pl0clipAgaUo3-It70bl43GOrAudv5g7Pyz-0gujk3nYhtGBYewYDrmrlg7IZRIaUbtYB1nSJl4WPThTsv-OJ8qN2Vjm6SADWzH7rKPEe2Ay4Xb0ZQX83GeJytAoJRssJpIHuSGe7Xj5o6zRNgrBa8FkdzzFseYanCpT3dsT4WSt7ETs15-SljlbgUIuqe-OTkSdXHx8z5slPgmIuoFYgMBwJJ690v22DiYVjnUb3R5dEpk9oxZ6rk_qjE1JvgGyes6iXRalLCju7t1affUzD-E2pcRdwcLWKW9SCz1ny6ZZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WipBiSGR0Rgu8DOQkQp8Ba9QpkLFWKWFp7MDN5VuH1f88vCmO67oytHTf63PZ1CKgva2zA_SjDFfNBVfMiT2TFvLm4Zbhk_SUvUSqM8UxMFRGipS7gQPv6rodBeqnn7m8DWKejuA0tzRUF8FRBUf45YFdmQS4zqUewVLLOipojuQ22ZUlSTDBEKLebO6CKPnI5IPXwXCiHK9zc67nvn_UPFhvkKOntwg8-cvQFzbdr2istYMIkNu70lurNiDSzFXccvYpSoeBMxM28NNClpCBApRZ3U_cKFlM4iSUCrKvuG8mpL01LAtddi88UedjIJY-ekE6Xd8OQrla6xmRv31_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLHK2FHWMVZogcHOjHM4-vC98QDh4TmPwlyU078aZ6Bmf1ttj0R7f4HjMPGHAurOAWrTRNWjGG5tgHAMjU9j1Xxyp6IzH9Xa6qihP86vN2paD2Rqls5nRGqUzdQh804G4ZATqd7bqp5Rex3dD8AEg5bsPWTna4mJgBCU1W4ywYHwJ8bNce8rNNzEKIEuGGlSegF9bqXU06kYz_YdHDd06MhZTCTaRT88HfUk0zYO8B-rgz7oynIuu9Ne-DSns4lQz8l8GkImqTY-kcPIUpJxC4xb8mwnr_imYfVfV_2vx1E3q38yitBnIozEgF8J-36sDI1JsCH4Skemoo7yoss8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUjoVfvUDeCPvgwbp8_zIOuKMWNUhBgyXDyyaJv633KVnc9pkSMCxPGeuVI4lsGvaRopPuLCgJkp9THESppPe9pFLsFADLvqxhGjQmzPzAa3UK2GYQXGiT2eO45JQOvp5KROvE0wweFuWlIY1dXnt9UghCiDL035AAf_FdSXEF3024h2PCCJBHqp-TwVsAIz1K_YGdi4oNVHweqHQii-pQsmFX4o2d7c-4vWLfS4thWqbpMnoOQ6ZEcVU6fSujw96oIPCGs38Idak2ucfDqGPjElxKJ0BltT2F8swGlofc9M0QmKZ4kzr9IFjrRs_wSxiq8Xy-dMpjpGWz-GAK3l7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNhEX-3xkWB1DMbxB_gqkJoTZWtfyKTJMkNlQERrobszF_nC8WtLYveuREt5btS4ptpPdulDSFpuvpKgt07p9g4ALgOXT-dyRAxDNJcBa3PcnT0vRXyiMZs5SCvVprWCjMAujGBpVtg9DmWAhs0gf4m8rxo7l3XQof_Q8eM1u7z80enB-9o75CSl-xEDqT6RszYtY-dT4iFsLpcH-QjDZUxBps7xjC_JWoCZypLHnCvT3UfH8Lf66e9QcqF2ZQ1iwVtArD2yocmcjqoiDTCoeXQAsfOflrxb8qk17SIPtMszVPXi37X-Om5mXatnd7R7Q6L8bDzpACJGLwYmHsuCLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 786 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FT8tc21VGT3M-FtxtbqKuoT1T-CNbrVS5ZU4yGcAw0kFPIVA8doHqvbK9je44ZRh0AQHxBETBdmtw4LzOzAtTbxGODd9EB6ZQPWRZvMHe0hYqLwFsMLV3rfv0CXGZPvw-Cs4ddmxSiXlpxtSOyuuKOfHhVxobr87kmYPRLKM2tVUNxQBoDIG2WS_YMqJQ3anFj115LYS7Wc_kZMjh3dHU8qFMDqK4THACjoE-5HBsUgZrmHl_bOl6kLDqSqDNc6B06FA4rBau0DRRA6XRllYqD2vb0cnzWDevy1PoE1JKvb_nCspncJlw3wWVqriL9Tu5FqlGCU9v7giikiuUtxoBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 582 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbJAI033OU_v_D-v-fdYzOjKfD9CP8GB2QTh2xmFoxbhO78AFeuhMuKQnXhIeanKHdriBOzCSC3yK4ErNgJEQJL3gjf8Df_aATjDSkMbmyMz4qBHXFhHShYzGgC8upMqial8WWssF6Q_UamBRip1hPHiDqbVApGI1aT46s5VIuYsmfaxsVvI3U1U9fmgB5PkSvDRc-wH48milUP0tr5kQK96se1dYVZ4T9uLkxrGC9QcQJtFGTilSCPFZtaLuTvgmgOe_XgyLVf7TgUr9AgZ4psclSW10DPtGCD3x8npQVZX0pK8QN_PlsUIglfQtmVXUsiCbbh2o3_meXmTve3Nwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 594 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7KcVOLQ0HT0jD04LkjAke3-A5bWzPKK9-RJE8L3_T54uL1EjL77aQ_RI9HRMGNSYr0bL6ZqwSIjAyJESa3sAIdDqxbffR0-GyUIvgQMW-99DegqNT1dmeZZnRggenpsHtmWbbuz3BZZtK7FCXy4lzJlLVHDM6yLyNakHfK93Uej5Z3Rne6r839yEc6Zqy73ow-V85cnXVZ9fwh9bbI-jDQD3EXFtnR6RL2rM6dPwOkZQ6rTwVp55Wn-CZ2Pbn0m4m3Cp0cxZ65iSjxmhPbEd86A5HRA4AK1kZYUSLHLQZeElOtineMSBvjGWwNqbWv8rWkQAuiVgLKr9a3NdiIgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3huIGNqoFNRCzUI75FZEtYEYv-TiFNE32yyG3AOdVWOETbLBaOm8Pb0kRctj59cGElvlWksvbhJRE3uNyoPpILJhrr-ZSmt0b_tH_OQrae_4Lx082bGSIK5zaLAIkktaviMJgFusXc-0vCs0Nxz0_i4rlCsj6s_nLLk-GXjUsNZiSckD8Ir4qUIUd_uUlIQoensqnXmZb5gqMWg6dpnJJpk0bjuKsQxa7ELRONmSmh-NLDudjsQzfv5C3dmGsI5NSjF34zUIUGR9XhJh1oesQLtyL8ilW6DWvlq9-50WSXJmAAugeE1LiyLhtInBvOay53tUwHtCdviR3LXDY8GLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 647 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPe-vIyhwXeBsKRPWymIt7tHer8jklO6lM87YUOTv5CsoHd3Rqihhr5Rp3v4TCjJoTe9zF9hvCztuEBMRXUqfRy6ns3L98cG22t9df_dL6dMcJKDgNqmosZlUOIh3JaeShaGkmrqOyq5tA2VD4W94VFDLciYo9c4zZk2AwddlfefzXkAkby7XH6KMajboEY4w7xKFBtYWzUdKfcK1XMI1B6vf-tWqogYGqGPhFLl9LLLu12Ui7VVERK1uYDwAQJffV7fqE65uVbLwD1wewJ21phRI8xLnesKLVwwh_yfqHkfrSYSarohWZmpsGCy6L8w-FMsb14Bi30igFEasN-OfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 715 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWZOa6gh6jOXx7oOsUXnGcfLIsAgOy87MLrCc2AD0eIyJMryngfrSdb8Xc-8LFfeKh0uZ1FmXLHX1_KbxyvRBXoUQvYun16kV2zTA5ybvfeAb6_e-YBY4maAvxVFZ_r9x_QcHrzynExQnrsQckl_FUNUVyOJ47F9HhjNJjy9xO-xcEHLoJwpod4iaiiwN3NsooJYCL0O9McWNM-A7cOtprZ5ksuXCB1NJr1clvmgBX2eSWEG0NamRLZxUTSOsIvFMPabLXy5Cqwky9UaEBW2DaoY8DtihVwwDecMKuWi9_vbe1-8C2lFuamGrvPuGlzb84fH8YkyQC7iqK3YxztVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQxjyuB14JZu7f_nWyIVfl4uZfkSb8q9lBw7MbnkJdwYUEz5Ngveh5A9Y68lqdEUuAAXt_m6laNYgI-Az4XZL39sPcECJ_II2N9P02qdNzpCksnDYGWCwUOKk4r3MPyhgoyMobdhwigTvpC9UO5fYqAIZmagsOZBeB1Bfd1r97JBsGrRjrEOPR_ssDPSaYOPpN7aHxjR3xHK9U-YMz32js5GA0jpSpiYRODIa1poh8-dkWVQM0dLDT_Q8H-ROnCGmIu8yaX-qKnHAAhwyaz90d3bx0XCEX41Hz2wEB9xXU5pmEXxWsjtEirA87F39T2EYnfrkqOtvvgIDBO6Sjahgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q68JZt6VEXjEtAEODYLscVX1dGEJUGBW1hgCu-zRXffOrtdmPsCsm7dCs3RRynNPgiUSkzNUdUIZKk2RhSvb02u858wfilyPPpSxNB_Rnz5Pq_5Zh-fNxt6W474rld7i9L_ZsGaURo0IC9p0zIP4Q-PEWh14AMBrrKP1EaBpdpdzFiue2r4hiGJG0_tELceL7DJlrQlLOL58fP1x6yRqZZ6MvpQEc5I_uS-LlmT6uimDRn9niI2CnicPa7OhAjQee0YiGJiQ8yW05C-cpj-aqM3o2_HPXvY8hMQ4Ib9WAgk12xQ_DkJcu1REQHkCwmeYP9w2TJshdqb3X1_NKwliOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g2zwqwFSVy1ExnTvy8CutCZjHKDKQ-LEZ6G_w0TOV43duspu-xL0gtFzca8Xy7uI8F_y9eIFzpa7z797eiFcgLmOO1Ifh1X36m5HxoIIYlWXMFBPMLwyZKc0a_dfRk3RWPFLbcPK-vBeNtdVXJvCsDfokuW7vF20_HZWqTZggkDBYa_pa_JAxi6mQB3QexZTGQRPY5Dm8KQNoQl7jMOrxjlPWspC2t_aUkUKlB1lnl671mxb3Zs8ad8949Ev4UejK4G0z2uElN7NQnZQ56BswPjW0twQWoewq4AkwMmT--IGZ4CZuC3IUtZi0h-TcxaOpOGXYc51RYg89Ya0kUyvxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vec84WC1q8kWgVgPY0tj-biX8hQ6ULqCwGnlNOdTcyIPpDG7-yV6aYfMcTojj_2Px-fJZ9tFWDX56EoTTqybVf0fH2Ok_4-LR3_0_dLjkuDuX3vRV26KWTYTAssTUTawXGp-0RTQZO9zzrlJtNpMJz8eA3dfVDFR_8eOnnq58YybDtzOHCuvsfrsh-9QjISbdiKi1FWFIGxnVRfl4-q2KCn9T-Y1OaIphTwuEpo4Q67yErk32d1o6xK6k5ZKzaQyltkmVZv9vLc4ucNZpbeRZ_eqyFfECvVVtjIqd7MKPsVyME0k4KOJVTNc0uYKLCJcnH_z1o93-u1FQQKA3MdeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 546 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXjcoso5lknq2C7K9RkYbkGoSVg_kKCZRmFzlirJ3kIUIf00kbgN7msiZOJ7tsHdlkFNIcEDYID7sWpJxWEeCzjstV7RouQmPiTEibzTsdNONJ6zHyZ7rs-KLXWwznBx8Up_ibaO43K8CdvT4IW0UpsDzhW4B1DrbnllwIoQtmOnakLVA4DM-iLr9f3C4NuAkIsOm6idHRub8nW7kXaC6EQUWGg8Fho2I60kyI5iZhZei5VU6nwMmipiYIWv3u76ES_Yh6z5yPYqaaJPpV4wWl98UOFKziROKvEEvXddJBQRaa_ZkCB5MAjseItM4O77M2dsbaSSD4YBgnlQTeQWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 545 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlWbux-AFs-s8JqmLwD9TBd7akv_hPPeXTM68ToxbENzovvetxP7BUnPx53F3f5oLvrfixLWQnGoyhWw-NXfWl4X-Bw1CUQ1nVtP4nplhG5HlWuFjsnG1aLzJHSSeWRn5HVg0u7t1275543yL59On0XvR-uyljZsN3duxfi-ZI25otAvdySgxtlQWPk4cjhZvBPu_ai96zDwU9h6TPDxicFGosBgNjLxhOzmgeJkUQ4L8uXlkk3kIas9-wXGRhCiYhXdLw9fpZaQeoYN5BDNqqUwgai4hDsR3ze2LbLnVC-yR8CdWQb90X-xu3R2_QdDGRL8eKNb8ymXYoES5Z_PFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVE65fyLRKVgjIpga93ub9Ne6Qi6-J-9CjjoRvoI1bylhL2udg55_o9IVR4LLOon5aRFJ6f7a2UAnzdGeE8rN8ODY6H26t4WFr2H_KOr5MSQAaP0DsY-cSQ-PrF7zUQvYXA6D2yRtP9dWBUFE2U0AdfXlKU6Ds-xuhPGPL5-pInpQdXX18LJ6ZIugLhaNY9w_HxZ1ZcSSLbtdeHCx0GcA-d4DhAFQkgvRA5mlm89zB12rD6Z1vBvY0Uun5lc86HXKm0jmw4SwkfXyuhiN3HFrgxCMDW89aDsiSHVLKB-Ca_dyK8YdtpcotkQ7SYMtXFtsB-I_0XYHlOy1ARKWnvRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 684 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pidPCfTmoW2H6wuTEU2u6UQDaDiAwmE9nMYs8MJ68YdKcEUZa0NoMku5J-L1eJajRWQUrf7Y0wH8mDaTIwmyT9B2C-6h3VtT6be7B2Vi8UsRS7-ZJbWSDXS_F4dwmB3Tqku3GaevsOjOFJyq2oJzjiP3XxmGgMpui6wzJxM344mNEi5Lqbos2o0yLom4B-7hGGCtJTMwwoav089zJFViCLNq6H2Z9N2TIROOpRoYlIj88dxxeHl13vamL-IEKCgjFxHQKptxNR8ZrHNYFlbHcl6OsIeMh5FzFFVTt6V33Hg6ddAssmOUTyjgkbscoH_vP92tM-ONqpmHJH8xVr6Kxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSFAMsQtEKLKQTeynfQCKGSyBQok-7BUfK-tFkwvcBRvu3HY9DO2dDOYtaxMyfYQYNo--efzdLAy8jZmI0aYgmXE0r8mPnOH5gC8P1_RF3fM4TrDX6ec2DX420P6cjrS3BCIXZLhC7cFtD9WmYmcjbCcdAhkzvj-zLouZQN3fOrR0K_Iot75BvJROIvnXS_gvnS2cX3YVvYhW6S0G4hZA8HUNcnNvRcPHIAvdZyXxOLLvlFOW9oUYzFhfG0zACPv5TNjUw34jFPdOu-mN4cegBXRjZ9kuZeEky2WtUEAnhWk4skNltO0tsjOiUpB2KGrtQte3MiLwmtyfNkmG0-Ugw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1t59h5TF1g7SA3eqpzuH1SgGm1Fk3lJZFlSMT2GKv4xVyA7VNK8McqpbW3MA8WdOyrLkU6JGX87gIoOcy38I52V3Hkd0knOpvj8Az8iPWSnObO4x0Qv12504tQ8CIW2LWftB46wwvWudDNroFysR6LAtM9CdiJOt7Uzr1MLAUaQuqc_C9G4OkJsi_bAtbIRBovxYP_A4NsxYoQDyofVjN_s55alB7oP66LN2LFrD42olWOnCJ5fQ6sQBQOXdIhaOyKjqVdJPEcDMxW0Y3EhfIT5gwzKtO4_uSK3nGCai8hUgG-Hc0FbXpVGlp2mmDxo3XjefEBwU8CNdgN-_MnD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpSmE1uM55Rmewq18ACofDliyxHBdEGf5Vy2215kz4iagYORRzlGDJr0dgYC_4x6IbMWKYk94FtI-s7e7hBB2V3ZIxZeGcWJ_8DHUC0sdHIBkbzcGMOb5YrOnifLhaKvW-eukpC5_CIVK3IyA8g3bRe2Uj9qyqphCVJfZg5nf6Qiw9Q-LUz3eJ_2NaQP8z2JpZ1hwgWdGJo9UxsKiJY46GYWVFSf4UfMkzho44kw6DM7fB0kjubIcWze8hOQF_Edw7Uu2l9gou-Wae3Yn_dxdlHq0VLOMeD2b_1JUye35XVfsOJ7VIwBgr1v9Q8LUiw6OdQz7oRYz9OWjsxCvPfr3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqTFUYvu-aOvBP8Asv8slEk9p8SXhQNn8flF5HJE7B86-dzv0t3lo_1GFoZa1luo_1i1S9cgmN2j27mOrvMjMJcATysz3PM7bC-IiZXb7dL2AEpMVwZDsQGiiUQR4aQQJXJOk2Fb3egfq7b343ql3omh0k8kxmd9pP0Oi5npASRKValahtis2V5l66hc1cgMvrrXGILf-1zCQsrrmA4y7wnaRxT0BiWEKbjZ2EDXl5_tP8GDzclM814JlqsELraWWSc9dRQTci2nPsfy_SmkoDGx6vb25EA_noN6hJii89S9DrYYSttuW3212I_gPScBw4VODoTVxKqcbdpJLe1L1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpPzUG-ZmxnNm59dDzLeQF0hJ8WVUfXdc2U9gjGdH4a932VgVgamnM5sPSfuitsLqyRtbTJBft_6Mz7aEdH9EwW02IhP3M0qdhJYdMGjNu19w-rjwr04ZF7Kxg5y_7ybThp14UVRm60zLN_oYGhhM8XB_92m9Tbt2jT1u3sEeU5tcs4tHKQAle1_-Eo-BrwfhaAjyCphqgnDKXgBiBdRrGfUDBo6ou6d723pJXej8WO4jSl9zhAQJ3eI4acVQAvF8TE_CEbtm66CuYN80IRQdf6JFNNoD4BVxkX-xrCAtKi836SIpmXGnew45PKLKxd8TNJrH-suVlw8bKaobjVfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IccrCKvK-7NGB3xIAl3RiQ9mXcDuKPZUw2lRD7qWdIHuH2LTG7hJpH58T_-Urh5xvc70sgdpZPq6MCMgWaTaUhZTL-SScdJqyk59Whg731lKdAT32U6V2IX6-mL3_oyE1Tr_cg9HeVY_LMwNlH7dFPEok8ngPf0wBEPbOQI8R3oQiI5z1yhSM2LYGsNtu_wkFnnJzY9jjlymnvqLo-rJCwRilUMC4VNs_fxEq6NohdIH5ZIcOJfklsvjpm--qWwjQi7QvivcZDNTDiXQICJ-PrB4SoQ35evTNU_h8O3gouof6iC3YzL9Rr3knqO4mtWgUJtoAz3EcS-_YLi69svM4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT1KSkEJB-pSkzg-KlabMRWhjrRcaiczQbV0VmwkdrCOW1e7IRyTVZkXjXuMiv4JVO6GjNtvObnb6jOhnT16I8KlW91VWOvN73dGYo45CwQrALOvKNsRymkJLOxncVVFQR8HI61WzeEypqrieXcem6m7rWWtntHoQJ5KN96tBgLbsbsEyBVbbTS1WIzadb7PSJti1zidcU3OkoNPeTwa-c9Tj4YgLxdBxJXHmBIvggYm3DCabGD4BxIx9HnpVK-PmsDZuQXEGOA-M0Zeg8YthFCfM1DOFCW1trYvzq_UbTnBJk_DwkCH0ZAiZjCbsGWyTnLXpA08o6Mu24A9nVZ_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3AHX7wOyl6h5Xr0LARxaSLWCgylA3YQHpwnzUKLRJSzhuzUyywzThEVo5eLfOrkg8bhQGb-Y70O_BHg0YZLtGb0GlCXmxGGvFdHc7BfY6dCEZ-glnU8FV7tld0P8Bmw0GH07_LWS1H5mrsRChp8EMeqgJHCRA11slLK27rH94kLL48TIyukr9l754cQG9LNCgJX7jepx590afTfWNb0M5dRR93-9cp2Be3_q-Bu7P_2_sjV96h4ZipIjC0Hb8EpX-wt7CteU_NbVD1A3elZ3hSDYAKutjDspqUdq1CuCD0nJToh35DRCPLZQsaAJSgIoMJScgYmMV8VQPCml7VaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIoLXAdDM5jK4KUMd1-lnwxI38bZAmaf7ojKw1x13YQRKtNzo_4UpBLoUNQhvlRBwZiA9WvpQzj3KUn5BZJp-2aA6W7PgKaucZ8XDOGnnWVQCwrLWYihkvZH-4qel75ztqUTEQ88aztRb-P13qHzpTHbpmcoYOen3wnt3qOdnkN1ocK1iJBZNBq2btz5OqqBv4Q2_BltUnTZPjO_drlo0tqxljRnq-exQQvMtQQjyNYmwEmKoToWZOAs0WomE9Pii8zbYmQoHWGk13oFlEWGU0RtYq2Td1OOcQ8k8Uk2D-gawewhq_t7M9J5LURFT13YBBdai1bKNypoxyEcgO7D4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 770 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhPVUa-vJuNs0BUEo_cMsZzK9xsn7rblozag4rHRcJLGFrUnbNBFqTRIbt-Y9FxsCR17GxQVtTdPUQy0Gl8Np9tnv8ivOv6j6JKGNqWuuWQsSex8FoG0wr5lLOx23Vat3mk8awB80U7Begx1aVb4XJbsPik2uQyvw7EyDAS4Xjbz0NjcFDFrM8OJmhVq5-RLY03ui7b5N3-I3mbNOSsYso0Us1Tc_5UO2lD8t_I9JlmRjAYRY2mgl4XTA6KBXlumvxursgOdi44ED2V_hVlnhuS1bbGumUzBGAtZu3mbehHLkPdAUmJIQtCdSpshMNEcBRlITuZMpc4kRURhpc-uZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVOHslg6ZPiJ4rsKm1hpp-Ii3zKc3pGenaC01kdD8RJ99X3U_MyQOCqK4iKN3-yICd0cnezFVd8mkVoLA5lseT9w2P0gYPHPjLV03HUPL6WVclQebIg74ZFgMhl-SN04sbi6MBRvlOeUYLWUIOLwV78Cqx3-o_d_-m9JlOenVIGWvC8hKrdNvCaQ8R_8ywUEl86WnOFM3oOYUZSOXfs1xlJ-cKoy8o3fqRLxLoPJUMh-O2hsmS0yGevYn_gUwPVq9cfBKNd9IqeFv-TxbroXKbu1dpC6TNudhEokXY9duUs2TvhgNSpt3NNX8-I9ff-GYljL1Xyld96E9BTOfLOjJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3V9kkkhDdmgd20FWdH_aPJF1TKWXkzJpMB75GbAavFkXWRDDlX7Px8LpfKZtti66Qn8iGNLjjhrr9CVZcxpDJeJJolKHwA2nycTeMYxnWaipdVi13XikeRJ-7jEuafsbZNlyMp_IJ6JdiOdrUuwZUUN50auEakrAS4jxVbuHHgMZmRXBnPh0uLuaHX2EC-0DcxlIC6XbvT_vU9dZMrAo6bSsP7jPaXcxLNkCVh2xEj8tN7k9_pXzpiBZ0TwqChu8n0oGIVYVwH_W7JRLNJbU2hF0a-A-qZXkvGU8qCYHye2JkaTLEY0eXj3LrZkm1iVVejnSNnruezmXwJzcowXfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SthsefBbPNXxAlvGoSvOfxHyn-cSFADU3Ih5a-LjT9XRRTTzUuMDsN_zbAve9J_xX2scPas3Ft9odYjbKQC62A0VGO1y5xpDfCHk1kc7FPOvs3AVst7z55v_SaJWeMDwvVtbwRka8gijr4b5CaU2mJZxjM-58o2vAyAD6lmx48VDYS4jgFSNNgIsAHF_2kD8HY3pFrtXUFZBwnYLgLGXboyYK7ftGheryluyenOl2rZ7rha03i7GNd41jj2f3hW1WKvwtt-IDtZTjV9ux4vMQ0q7_Gr63vpLteh8QOoMdXy5Y0NW8rkNbnwkAUHqsp00_Q-9wtjpWTvTzILDiLkcQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDcNqqZOggmQAdgMObFT4mbVY-Tyg7SsVHvX_7yos6XtlzCYXYefojCqyd2fjwROIOatjY-i1rt9TaipAfr4uCsDlyIwEwPCuOwRfKQLmUM_gSZlDpt8Zt10h8auz7gkZsDQV8C5w1fbTpmd3Gwz1_UDQiVJsSuELcaLHFQ5OndnurFeyzlieUHQOdIHrmtdPmenY5nDrchx8LFvoAE78z_4BoLqtg2TS95ifP331d6HOOperve9nLTqiAChavQHHz83u07GavPMar7JCgLbeTS-CuLPcTK1kwORcd301oo-5vbJEnALLx2Nkeue-uRrbPVK4ljtNEmmWuIuv9Xp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUolH7xqj0iVxGRi8azelaDYzm7dDoxSPXN1p-Wf9DfXE4HiiAFq3t8PsnAEKkqcoLtjxD19KZyRY1colkaN70SfBOBi_L-DjyLK-8j4LB8fOk_I0aSCdmVZ1mloo_X4ARzGrvJlJCECbmRw2P32MzCdz8ExSwV38YcIw3ogAtB9HrI4m_v1NNCUkJVwbryLK2sdw9UqWh7Xtev5JZabi-vi4HT1aeBUffefv9V_K91L2X0ZkvQb-zb8HRZf4W3MjbeGNtWuAbK4Q8a2qgrnM9p7r2bcYPWg9JXaZeCt0WgQ1Ho0027WxA2MXymmeXeEB4pwzQC0GoHq1LqgWzwusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ajxYBfQjZMy-jfJkAMHRqMMXuANXW3Gns1R3dDw1vJt_SaF1b1kXbhLcU4x_hh8oE9Q5CRkJX4-csTHK6A8Jd8oNUf1ioEc90y_sXJyzE6vG7YHu7-ivYo5GyvtOH6YDiHs2RbI_kNKMaybGMwRanZQF8ngvWdS0Vjq7R5S_EOqezbtmc0SdxZG0HdqEt4EcdwIfM-cMKE06-ze8U5PLa1HAcWZIrQ5AorXhSph4GXPWYZLq1vaL-17dJMGxslgjpswy8NdyhbO63Fg5_cXNvJhxRQz3X0GIL80vi-1A8wo8Pj7wO1X5A8rgBeGaSpR-15KwRrsPQqqfGuLuHRL4UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=ajxYBfQjZMy-jfJkAMHRqMMXuANXW3Gns1R3dDw1vJt_SaF1b1kXbhLcU4x_hh8oE9Q5CRkJX4-csTHK6A8Jd8oNUf1ioEc90y_sXJyzE6vG7YHu7-ivYo5GyvtOH6YDiHs2RbI_kNKMaybGMwRanZQF8ngvWdS0Vjq7R5S_EOqezbtmc0SdxZG0HdqEt4EcdwIfM-cMKE06-ze8U5PLa1HAcWZIrQ5AorXhSph4GXPWYZLq1vaL-17dJMGxslgjpswy8NdyhbO63Fg5_cXNvJhxRQz3X0GIL80vi-1A8wo8Pj7wO1X5A8rgBeGaSpR-15KwRrsPQqqfGuLuHRL4UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er6iXX-f5_YudgccH_yVS0XbFkv9vkxovpAHKwJkAIBww5nT-iS1MLbhX-TRMZfVKIEYA2Jq5mpl7JsBVkdzi2y0GVpsUXJ2EOoQN21sT4hF1a8L7fAI58D89a1eklGA7vC8E5-ZFz6Luyj-mBdIoiOb9ozoD-87Nq671cbAmsjbJ-kKeYq6TVzR6e7q0_O3YzsDbrmHLFbN9Wayt67BfJoWtivGeCina6znMSZTp74VU5flYdih6WICidWY6erjO-XFNMQblk2zhzBpoiXxxnx4pEI5LJ-2Gn2cLFXE-eCpARyv7VZRigLp5vZEGPeoBxO8Xx66mkJHWKad32TX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZI00UsRGrmheuFzWLfIGTHFbmYhxBvacR2hUyUfDU7SourgPrV_nRChkGTbseQSD1pPPPX56FOCUA17xttn9g8Cx6GM-e0Xeu-iqlr9ZOjm5wZZPn0dxrAPNkvFq1kKze7956GSUAcCT979t84GexZ3Kyb0OfSLKyU_hynnh6TLygjCMijKWthEoptETqkGJ_4j8hCgzxQn9Z4WHRsZhEE4bSsLaw04YEgFgHjSJhB_MZGPv4n9LH2HYWjIvzTyItLpq_83GJKeqjxKyRHbayrwpKW-qvM6AEqcWy6X654OK20UbeBTM3v5uMmGIWQPm-ioGVNFmVYG3JyOqmQUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhDx1-vilJe00HNquUDH078FJbzVCsMJwVgn-jqkI3B2SQxm8DM83iiMB5YqSu-_OJwSPYaWUfAdo4MwH-gCae32-zPYJhKmcJXYdPU-3PPBLpMwtyDFU5LhCKuIe4QQeeh_D506wAc6gcWDbrQcOShiCLLDzAeDQ7vHviVAJTfCo17t6njP0Ltdlw1izRydoWl32nMxa2zdBNqg7ydtnpheaTAzmVa6bMicQCsNpSAF2tqRCgtJ31e9YGPGVz-k5QhIklb0oC2MMPu668_aShRln8QHH_v061yK9sxklzo72TT4mUCg4HxrpMevH6FVZgPz4ew3Aj2lFJfwtlCSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yu2xw9uHIN-RyrIgWmMzARXSNIUcBZpTbzpag29LwYnPOQ3bZQ3Sjfq_4fa6-cIf2RGuD8jVGGrA7bs3HA-YdYDy1N2GyQbowmJAd0eNfZ3i1wXpxrC_0d12wL5aeDZnr19Ytdwvwpdw7vyGlX2kWYL82KFOWLYa5N5Kp1yKAA1uhdW0Kn_whN9c49J5NHLMsl6YEc3zKZALDpQlN4UronzPqBDK01BFlm2nt3xZ-8s5ty3wV9i3AX9oVnfcVSdwGH_w4khvM4NLbp6ZHGCZfiU4acq_j-pENkKNJbtXk6AFN_7jc5AuT-R3Ls3JzuQQsf-hfK9PJDoJsJqHIJfhQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kmjfw4PT9-sIfGATP-G3TuvCv5X_WRto4AWtE8SG--oi_lAVgVqiEtv9JtWJgLlfdPtLOVv3_QA9GLGMO_CPWB7NuxNaHTSU6r85hc2te4I1o_ZoNqemmKs1pp5tyHl2oWnkIbODXfxtxc-UZrO7EaLBbXbzQKrOq7LKGJSdLXdhTmOyqG_rkjcMBmb97XGpVvycSp-_dZWFYubup5HIDKs-xURkB3AgB5LOJZ12NwuvmnNxOmeQEAzVBmaTqCpdci4mQRCxbMTXQ0ufmTEauSnRtxcL6qFI4M-BS8-rTp693xUYHkw_Db2Ji5RJlmuLhxZ6v486WWY10n6zpUpK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHPnggOZ2N1CNGxn1mgrINVDnNx7KNzpde4HorlD3u4ArRRSM9FtNCMK4nbJsmiGqPSKKpTMEJ-e9vJoo5Byp1jniU38Ybpl19qVuezfUKJOnLihGoGLIhzacsOzyxtB4s1WnqERVHVusXHsIgqXFK_Xb2yrlkBMpChEQblAX0m6a6TIpzeBXs2bSPmyoSdEh9SsPlvqAjHyXF8irGFOXrvMP6WfUFVyr03qGeb4vHqCuP5Fd4SzNtaeCSsUB5vuDafc9u2ddikRy_ZDRVLxuc-HxqCtgOl8VeH28BJRL_YyuP83sNeTohWBV5pccRFdGJPhYppsZKa_1tGbq14f2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOwXcRjfcrUisv_SQFbk6f0lQHPxI9ExFHfhP8FGqp_cCiOa9HrFq90Zm4LagA4przZoTjOPLJKTjaTNP_I0dL5p53-Dk9biAzpjBNCo9ZpwnXDm6gTAjvJpGJLSVMpeuPStkraBePuu9NHIpGZ0-_BR2mSd8171MdOB9Se6XTUUnpJQSx5R6iBXg6sMCfuxEV1R_rrx-2dp8CZU2-ko3NOoYW--Ib4VqfuSIet3T8WH2HginVE8KBtAfiryANxL1HIDUR_oUZF0uLsWcfodhyFXdzBKQLhThgdcPJk3tT7l061EuDGG36pW1Zuxw2tYNAGK2ySjYL0IPyVmGPKzSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=WE-FOsxvaLLQDQ6ypNAUjbuk2z3mb08ejTGTThGNz0j-2fKMIhFQY0lmxdAZty0SYiKLLp-1buwe6uMmbFpp78zq861WQGNfVjvbte_OOG-vGGa_O-ZX_SFa5YPIQFP_286P4z2DDVb-u3NohF0mmS8QzXU1QSLfb7G2g-4Q7aWf8OLhfbsGxzVaCFlC7kdaPefvvRpCK-fnIZQINdbg4JkiQMDKzffiPWZ9UCVzg7DlYCrm9PYjCBYDcx4l6DrzaWB-xVnSEV7NpBvJQWkByzwJj5FK7vhje4JngruYhBvius63EPNMT9yEoE-P0szZbmjKqBn3aSDQ5si9zXCkl5oHLp3LSeV0H0LdXCVeVBUOnuL3JaVzff1cui9BvT-xxdFC0cOqqIs7ZGv7S_7laYP5Vm91rdRkzqSF1BPEZO0Nd4EAYRvHU8SYnzPFWsbobycN1rL3O88XQalROvhdjf0_oA3NrLisZtU1UCI58YT0GIJez96TepBWRbJF6F6-I_fBajGOVK2XQrqXKCG8U9FeWKN3csk5YCPrlNGYsfHjCQ6v_4mA2t3JZ62T_vRLG7Ldr-nqj4QLirF68tW90T3LuLcKRcAVwSAcQuSjf20KAFZV9kmngfalYrdZ84R1uLYLX8pRQIDN_NRmnJNqht9ROmu-5al5aNRVRes3spE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=WE-FOsxvaLLQDQ6ypNAUjbuk2z3mb08ejTGTThGNz0j-2fKMIhFQY0lmxdAZty0SYiKLLp-1buwe6uMmbFpp78zq861WQGNfVjvbte_OOG-vGGa_O-ZX_SFa5YPIQFP_286P4z2DDVb-u3NohF0mmS8QzXU1QSLfb7G2g-4Q7aWf8OLhfbsGxzVaCFlC7kdaPefvvRpCK-fnIZQINdbg4JkiQMDKzffiPWZ9UCVzg7DlYCrm9PYjCBYDcx4l6DrzaWB-xVnSEV7NpBvJQWkByzwJj5FK7vhje4JngruYhBvius63EPNMT9yEoE-P0szZbmjKqBn3aSDQ5si9zXCkl5oHLp3LSeV0H0LdXCVeVBUOnuL3JaVzff1cui9BvT-xxdFC0cOqqIs7ZGv7S_7laYP5Vm91rdRkzqSF1BPEZO0Nd4EAYRvHU8SYnzPFWsbobycN1rL3O88XQalROvhdjf0_oA3NrLisZtU1UCI58YT0GIJez96TepBWRbJF6F6-I_fBajGOVK2XQrqXKCG8U9FeWKN3csk5YCPrlNGYsfHjCQ6v_4mA2t3JZ62T_vRLG7Ldr-nqj4QLirF68tW90T3LuLcKRcAVwSAcQuSjf20KAFZV9kmngfalYrdZ84R1uLYLX8pRQIDN_NRmnJNqht9ROmu-5al5aNRVRes3spE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyAjW2GTW70X50YRW2TKngaiPpvedgXPehbfNBCtFTATKkAn2pQG0pxjeu2FY-wkboPGfFbFaHitrjkeFruUftvaVxeptfGadHwKBbWOAxtxhZnntIgPnJ_mZmfrlLRJDQal-9Qcgvs17abUM519ief3fWQEOfRJ5latG3Whi4tqc6ItCXK2qisO8lWYO-Yw41muLZwYktBKiVgG-7ozG3iYh_jaIxCTwxU-6kT-GFgBxFaDtYru8tF_zhPGSfUM1uWzKDR2sN6e81ndwzOxEi7Dm6nujgfTQAVaEctaU54oDQVU_j9IaRgUcnT8_PPSkAHM5WE-1ehLzqgLU8io5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gINHAu39rb1JlKokU6IjTkXgR1aKayKK-fhtZgUsRTr08tJhpvTNxms1f6GjqUFXHoCcqRfsp9FZUnAOvvmIFU2pLsucHngHPJJabpKL7W4DMG13umIXtAZWtlPVH1Bai0V2vGfubQicnetg1nmoLXoDuQ7hbh6cqaxHvuQKxzSl4zY87_Of4fWuRJfRx8hwr7n46cFvbEAoIBA_oGbOs19GEd_y-ORb0CU7_gokQYjt6Uerc1IifrtkCtkVl5J3DrpF0Vpc_FdjRgNMF-IrGVj-oqHjtkJl7YIZHmjXo7U6yquMO3kWJk0jsaCHCqrurzc_QCeL9AcH0QPW6qELNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAuJ8tbeGy5LXL-aoVkpWjqKMxZXbVeup3ycuX9FeCdiy-jZUFBTOCYDRoqke4Cvg5S3Z7fPCRq1f_RP-AwnjNUroCKgbH18sPWtvRLI1QcooAC-8ifKOPTVxqAQo6HvvS2psYYtXAL2li2kXULBqrNKi2ceSrIkfccAIst4ExeFTsmuf47WfuocYETPyAjeh6_HR6e3c0eCzqpHsy72HHfgg9iylCnNGaZoZZkweMATwZ5-GFQR0lyuN-WavcLflwwotc9Obx1XMIxFidrxagLC7Ri1YBwijLHSWR_sTuxjUIf46WOsIr0N0EfcK0qp9mnyVAUbCYQ7ELcQyGijKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuGjPqc5FlGlgsA3eZNz_M9x0WjxvlGvLbMtWnaeiUcfYbnP4p0TU_hBAGYuF6BzDZ72CdXGo8bfE22zobAzlsSvm1LWhip6fePVfeyFhejDpSi1-uggw_UsYs8KhjouAL_6_HKeusYBHFsSyQ-AqFdy-jLJAck6YeOQ7gfhFFIN2i7Y0znwUzVpbU-kYQYb0vZZ8Xu9dpkHrO8oAJMRvArpJiqWT4P8iPz_IQ2WAoN9Yuwx-c1Nc3grzm_E7G5JgjGLAsfDATom2oBFdKkJdgKx6c_JJcj8rp6Y2XGduLHjHiUmjaxpazBKAv2qTcWBjeQ3Hp3Spx-llVo-AoFd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CrEE_IBNS018o_mEj9RPy72Ux9he1P37kd5WZliB--rgXEAKKfJktb2VDDf0989MFoHyOAEmnmyPO3SgKk1zLuYKnlstLp34ScRcKa7eUy1svTgZnCMz7uOnYGTqUrKujCuk5HDjS6xdwc8zLKx_VFZwjkzYYKx9O5KpG-Rkt-AbqzGju0BXvt4-rHunJ1NhyR67aGcLeXszTeVTMktD1uOO-TPCnInr8UyYYo_2s9SG1bET58DoRP_0b9GpMFNWUpQk8IzTLspfpuEwvlnBESZSX_wUpOaZAqv2u0l3XOti7Hklpx97l3VU8EE64Wq8hk7Uv_NvMCoEfHCn4DI0XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Svt_D_Hi4VZx9eOcmb0oqAJK86dYQ8vCS5-cLeM0BIIucCTS6hprV0IrCL6l9d-nMALMEoyT4CFLUaNe_a3XfPhjJqOS3O3h9ysgGVwjmXv_Bh5044a9eG9c0-cHuW_7eZFqhuPsRN-5ex5jbXcV4HcHUvpKghWTvM3fIWlITf87cexHhY34PLy6BHS7rindvAiMHUS7jyo3PgmhneUYLOnPusDXF7GIkmjfOT8TTcpZYBFO59r2phy3wJ2bIk1G8L_1PMYz1h21kmSOjU6jUy4zCziX8XR3gGCEkZl-65AkoVysjvPWT37Osu1Ldzl8hNoelpX7JrBwELoP5c1Lm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Svt_D_Hi4VZx9eOcmb0oqAJK86dYQ8vCS5-cLeM0BIIucCTS6hprV0IrCL6l9d-nMALMEoyT4CFLUaNe_a3XfPhjJqOS3O3h9ysgGVwjmXv_Bh5044a9eG9c0-cHuW_7eZFqhuPsRN-5ex5jbXcV4HcHUvpKghWTvM3fIWlITf87cexHhY34PLy6BHS7rindvAiMHUS7jyo3PgmhneUYLOnPusDXF7GIkmjfOT8TTcpZYBFO59r2phy3wJ2bIk1G8L_1PMYz1h21kmSOjU6jUy4zCziX8XR3gGCEkZl-65AkoVysjvPWT37Osu1Ldzl8hNoelpX7JrBwELoP5c1Lm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u--rW5mjYh7n3Ho0_U3gvNRizZ8JQZWGh7fVyleQLlHXkpoh18_6ZOzLXHMCpDMPgO4M_XoiSCs8o7g9HZNJySXkSanO5ZTSKbDQBAxF8L_rRxVbxzTcZtK2RMf4MzgXf5bt60rE2Y82iimeahEEaM31KO4Y9LOz-OkV1NcLipPBQPVGoGrZaDvhjFKnhYQCbIdULS5ZIeAgIbSXwWmvhKD0h-JoPiQesAaEdvSm2_lXYug3gXf-NbpCa8bXlrsZXlE3yeIbch9_fkwQ3QDQ2HF92ki_W2Gw2K6ah-8FruTu6RaD0O2FZjhe3A2hjBhSiE2OFM7C6DN-UFutM5f6yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
