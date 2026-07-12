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
<img src="https://cdn1.telesco.pe/file/XMImS0FEYKL3bGXE0_98yS4bozDezsuiB_KB8HrJow3tPsti2h3bnfBV5zxGp5TqMiKp0WREaC3VI7nMJmHOAic7qLvqRwBeV8srTF7m2teai-E8AO-rUCzRTGKYHgCTPfC5fXWeDqLGBidE2VoogPIN9_gI0nyj43ti4MQCuoJDHeGiB1TZ7ISVS8WJwNzQ0k9NlgTOATzkW5NBWR33EydWB5aovRMna2MBHnPvgv3bZ2yRQzdAakzBOWuqj9RcUhyy5WXD4ytu5rVqUXBpEeyuXABqvLDyqNmwvfPsYfyujIT92X9FzuiPF_KFuGztqFSqXUdrYc8b2Nlyvd7P-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 22:22:48</div>
<hr>

<div class="tg-post" id="msg-76973">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری مهر:
گزارش‌هایی از شنیده شدن انفجار در جزیره بوموسی؛ وضعیت جزیره لارک عادی است
ساعتی پیش منابع محلی از اصابت ۲ پرتابه به جزیره بوموسی در جنوبی‌ترین نقطه کشور خبر دادند.
در حوالی ساعت ۲۰:۳۰ امشب، صدای چند انفجار دیگر در بندرعباس شنیده شده است که به نظر می‌رسد مربوط به شلیک یا اصابت‌هایی در محدوده دریایی بوده است.
پیگیری خبرنگار مهر از جزیره لارک نیز حاکی از آن است که وضعیت در این جزیره واقع در تنگه هرمز کاملاً امن بوده و هیچگونه گزارشی از حمله یا حادثه‌ای در این منطقه وجود ندارد.
اخبار تکمیلی متعاقباً ارسال خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/VahidOnline/76973" target="_blank">📅 21:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76970">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z5mIE3ZgkI9eXiFu5RyVonNu1_DqwSwkXO_d8PF0Jc-xwOdHj8J8gmWbh68GNdSDmv6hISdpEil9W6VP-JOivRbaGxRHT9gY_vsuxFpB6z9TOB_D0bw9D5FFgQzh91v0x6ZSxkBUE6KEaf_ti-GU44BP-NJOTYI5q4S44XzIyVXTRp-efWC5AU6XfEuyLbIOuEeFc-7j9_A9OI34H6jNRmycbsLZNUv_3ofry45EKYVSucSfctMhk9ws4tP49-Oho4bt8n_EgaEwvQ7uEuA0AJSZxu_rEQcNEhacPD4z0CGZyJhuOdq6fW6jQazoeIhdMcjKunW59NK1iOLMTN3H1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v7MXxoapu_QGZNov4Sg7xeqwO0kf3WbrA-pvudddWHyqKEn4VTnCwJ2t3oFs4Vnou746C83x8AI8inEySJuc0QdqoLYQpYXGQf5bMc0maFNoDm7zfVyb27XKB1VgvNp-NF5QjuitW3jseB1mwX_p1NPGB0o8DUaUqKtwfsjRg9694-yGPfAK_yOzJAeiGTqYyRi4Mx-7Ewx2Ly60U4vUcyRoy_pl6OIK6YaEUmCvSw5Bkf11DJWVa3ak3tdsoVicAkjsD4aUcpsIqyWTjAV7rChEfesZlFKOt5uM6-mrQIGamEA2alMPzdstOJ2aJTJw4rQBfreFrERM_BgbIH5_dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83e7b96a5e.mp4?token=KfHrNDnXcPAvG2BJXWKDMMqfBeEkJizdvGhTx9fexNJFXREntfMRjtJ--PRClyftn0-rSOuGjsYrwGF76--pyGh8feKuVK3rIHQWOuJHGtJKKbymQGVVQvTVGyjqAG9hJfM1jsGuz0oakhRAReAXFXSNXvtFLQbB4eit3FWO2Ghv95p3FmvUj6w6by9-q_00DiEvOU7sZQ8z6eAkRxvbDDVMJPGwNEZZ9V6BJ6QfdhD2dGDzfbF3xg4IxYldboUQONmRE3oNLulqdKArVAyqXa8Ux3Xr_7cqgKb1AiSTTHT3ASwYN9LrpcPDcdWRLSb_iGRsR5NqvbLtCJOAYH4UMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83e7b96a5e.mp4?token=KfHrNDnXcPAvG2BJXWKDMMqfBeEkJizdvGhTx9fexNJFXREntfMRjtJ--PRClyftn0-rSOuGjsYrwGF76--pyGh8feKuVK3rIHQWOuJHGtJKKbymQGVVQvTVGyjqAG9hJfM1jsGuz0oakhRAReAXFXSNXvtFLQbB4eit3FWO2Ghv95p3FmvUj6w6by9-q_00DiEvOU7sZQ8z6eAkRxvbDDVMJPGwNEZZ9V6BJ6QfdhD2dGDzfbF3xg4IxYldboUQONmRE3oNLulqdKArVAyqXa8Ux3Xr_7cqgKb1AiSTTHT3ASwYN9LrpcPDcdWRLSb_iGRsR5NqvbLtCJOAYH4UMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای شاخ‌دار دکتر کلانتر معتمدی درباره رابطه واکسن فایزر با نازایی و عقیم شدن زنان
🔹
محمدرضا کلانتر معتمدی، دبیر فرهنگستان علوم پزشکی، در یک برنامه تلویزیونی گفته است: «بعد از ۸ ماه مشخص شد واکسن فایزر حاوی همان ماده‌ای است که در واکسن ابولا بود و دختران را عقیم می‌کرد.»
🔹
این ادعا صرفاً تئوری توطئه بی‌پایه و اساسی است که از سوی پزشکی مطرح شده که در جریان تحولات علمی روز قرار ندارد.
🔹
واکسن کرونای فایزر چه در ساختار و چه در عملکرد، شباهتی به واکسن‌های تأییدشده ابولا ندارد.
🔹
سازمان بهداشت جهانی تأکید می‌کند: «هیچ شواهدی مبنی بر تداخل واکسن‌های کووید-۱۹ با باروری وجود ندارد و هیچ مدرک بیولوژیکی وجود ندارد که نشان دهد آنتی‌بادی‌های ناشی از واکسن یا ترکیبات آن آسیبی به اندام‌های تولیدمثل وارد کنند.»
🔹
محمدرضا کلانتر معتمدی، پزشک و جراح است و به عنوان عضو، دبیر یا حتی رئیس گروه‌های علمی فعالیت می‌کند، اما اغلب اظهارنظرهای او در فضای عمومی جنبه اجتماعی و سیاسی دارد.
🔹
ما در منابع عمومی چند مقاله از او پیدا کردیم که عنوان موضوعات آن «اقتصاد مقاومتی در نظام سلامت»، «فقر و هزینه‌های جراحی»، «تجربه‌های دفاع مقدس» و «مولفه‌های فرهنگ ایثار و شهادت در جامعه سلامت کشور» است.
🔹
او یکی از امضاکنندگان نامه منتسب به «۲۵۰۰ پزشک» است که چند روز بعد از ممنوعیت واردات واکسن از سوی خامنه‌ای اعلام شد.
🔹
بررسی‌های فکت‌نامه
همان زمان توضیح داد که هم محتوای نامه بی‌پایه و اساس و تئوری توطئه است و هم نامه‌ای که به «۲۵۰۰ پزشک» منتسب شده کمتر از ۱۸۰ امضا با نام‌های تکراری و مخدوش دارد.
🔹
با این توضیحات فکت‌نامه به این ادعا نشان
«شاخ‌دار»
می‌دهد.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/76970" target="_blank">📅 20:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76969">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8bbd214211.mp4?token=lh8ApHNn3qrdfWLknfaHvfyezraaS4hbzz_nMpQ7wjDVWira-BTWagieLN15QA2-bYE7vI1XXiej6GxDutgUcoOaY5vMOfMjQyo72r9jhbwkPFU59az__nZmPtkQt67z-Z86Rz_qrrMnZDAl6i6ZBTRD9B58I1XdKN4qimsaG2ZkQXRtE8bo-NEiEMntB4d6rNNRlmgtk4HghaxhSezbIjtIEyhr7du8MDjJhFom0LZsZF7AEk5PounK11Fu8l2Ogp6z2Ak_yOxJCyurvtP8aj6ES8WwVjZT3tc05wJz9jeCTS5cr5mmNzOrNZrXvsd5TcUrKwbRS5EZ9KInqfd9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8bbd214211.mp4?token=lh8ApHNn3qrdfWLknfaHvfyezraaS4hbzz_nMpQ7wjDVWira-BTWagieLN15QA2-bYE7vI1XXiej6GxDutgUcoOaY5vMOfMjQyo72r9jhbwkPFU59az__nZmPtkQt67z-Z86Rz_qrrMnZDAl6i6ZBTRD9B58I1XdKN4qimsaG2ZkQXRtE8bo-NEiEMntB4d6rNNRlmgtk4HghaxhSezbIjtIEyhr7du8MDjJhFom0LZsZF7AEk5PounK11Fu8l2Ogp6z2Ak_yOxJCyurvtP8aj6ES8WwVjZT3tc05wJz9jeCTS5cr5mmNzOrNZrXvsd5TcUrKwbRS5EZ9KInqfd9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت دفاع کویت شامگاه یک‌شنبه در بیانیه‌ای اعلام کرد که سه پاسگاه مرزی زمینی در شمال این کشور هدف یک حمله «خصمانه و جنایتکارانه» قرار گرفتند که در پی آن خساراتی به تاسیسات وارد شد.
وزارت دفاع کویت افزود همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت در آب‌های سرزمینی این کشور هدف یک پهپاد مهاجم قرار گرفت. این حمله خساراتی به بار آورد و یکی از کارکنان زخمی شد. این فرد در حال دریافت خدمات درمانی است.
ستاد کل ارتش کویت نیز تاکید کرد نیروهای مسلح این کشور همچنان در آمادگی کامل قرار دارند و همه تدابیر و اقدامات لازم را برای حفظ امنیت کشور و تمامیت ارضی آن اتخاذ کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 209K · <a href="https://t.me/VahidOnline/76969" target="_blank">📅 20:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76968">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4ddjD7p3hQiCOWm85cLmU4Q8wFY9dNiK1uw_iRcSurhKEcaq54h2GCvyPAUk_X4myj3SRhHQeDekI7UGlMgVKKQLy9eIOKsNWMgC0uCsLWsN5P9YxzFd3VFBJQiuZGF4Wu0bTY94wk7lagKb6zYUK59kKmQx3O8Qz7FBtEs3P04SpjnhD7VNXhhLVdM_k2j6FDjk170CiZasAJBD-cCZ9baZtFDqNPYixu5CQjAEDn-eK6xMfUnJop5HWxq0TFhEpWEBE3u9oQbuMphuwg9M_xT8B1Po0JGbfE6v4jYXREvs0xKE1MNa3ln3Dgu33iiO53nsMxjRmWWydAOg2xeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی، یکشنبه‌شب ۲۱ تیرماه، به خبرنگار آکسیوس گفت ارتش ایالات متحده چند حمله را به سامانه‌های موشکی و پدافند هوایی ایران و همچنین قایق‌های تندرو سپاه پاسداران در چند مکان در اطراف تنگه هرمز انجام داده است.
حسین امیرتیموری، فرماندار قشم، تایید کرد یکشنبه شب حدود ۱۰ پرتابه به اهداف نظامی در این جزیره اصابت کرده است
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76968" target="_blank">📅 20:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1e454bd90.mp4?token=ECXsXoHEmKu1FWMMIbtLcJKK7_206O42bYoCvjt5ohuuzMBS8Bj62TuXjSwxWAs1Qns8O9cJyhXFoRQc3NJY-PQ9XzY4LeIu0bTVZahGYQTaZxouCM0szVrN37KgVmyGjymPiUvUIdXZZLMdJXtlToJdkXjBsGX4HRw_OPiVM9FQ6rKhPppIazZZW7Q95rcHYYN4feHVi_n5z7veNvbLT_MCY706t3lyjZGMmyieh-qBwHHb5e1dpSzFgRsvozdZO-2rdkYj8tOiBDXQ6c5cR_37C6yklE2_BfaFMwOPhvkjdM3I8pAF7v9QDI9Cno7AQpCQyhLYdpYqKbZkEGu6Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1e454bd90.mp4?token=ECXsXoHEmKu1FWMMIbtLcJKK7_206O42bYoCvjt5ohuuzMBS8Bj62TuXjSwxWAs1Qns8O9cJyhXFoRQc3NJY-PQ9XzY4LeIu0bTVZahGYQTaZxouCM0szVrN37KgVmyGjymPiUvUIdXZZLMdJXtlToJdkXjBsGX4HRw_OPiVM9FQ6rKhPppIazZZW7Q95rcHYYN4feHVi_n5z7veNvbLT_MCY706t3lyjZGMmyieh-qBwHHb5e1dpSzFgRsvozdZO-2rdkYj8tOiBDXQ6c5cR_37C6yklE2_BfaFMwOPhvkjdM3I8pAF7v9QDI9Cno7AQpCQyhLYdpYqKbZkEGu6Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
همچنین اهالی منطقهٔ مسن در جنوب جزیرهٔ قشم نیز صدای چند انفجار را شنیده‌اند.
ماهیت انفجارها هنوز مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
پیش‌تر نیز برخی رسانه‌ها از وقوع انفجارهایی در کویت خبر داده بودند.
@
VahidOOnLine
🔄
ایرنا:
اصابت پرتابه در جزیزه قشم
🔹
فرماندار قشم از اصابت 10 تا 11 پرتابه دشمن از عصر امروز یکشنبه در جزیره قشم خبر داد.
🔹
حسین امیر تیموری در گفت و گو با ایرنا افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/76967" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4ea69d634.mp4?token=wBQT8G_asAypbU6xH0f4GryIbiRjXAx5mbpGlJE3BrXzW-R_455dNahRg-7NMoMPJvBmp5A0hgSPd78y9-ar4tztgXFsn-txsUoz8rMA4J30J2VX9EBodGhJMVqTuMEfDMsdrDLBRqoujfBQBzm5jMBpN95wO0XqYugwOKcTkGFIQ9VZ7Fj2RrBkuGrBiPKfPdUrLOjCEoAkWioqAUzxO8ytO2wX7ShW5HSmV2PMynMulxwVQUvgL3_COYM7Xq0go9InLtsAsoxwvkK_qHFmS9wc0tl-m6jN7DVCkO4DIqMNZjBUFQLYmXbq_qXK8RT_7MYBp0uQhD45aowPMW1Ksg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4ea69d634.mp4?token=wBQT8G_asAypbU6xH0f4GryIbiRjXAx5mbpGlJE3BrXzW-R_455dNahRg-7NMoMPJvBmp5A0hgSPd78y9-ar4tztgXFsn-txsUoz8rMA4J30J2VX9EBodGhJMVqTuMEfDMsdrDLBRqoujfBQBzm5jMBpN95wO0XqYugwOKcTkGFIQ9VZ7Fj2RrBkuGrBiPKfPdUrLOjCEoAkWioqAUzxO8ytO2wX7ShW5HSmV2PMynMulxwVQUvgL3_COYM7Xq0go9InLtsAsoxwvkK_qHFmS9wc0tl-m6jN7DVCkO4DIqMNZjBUFQLYmXbq_qXK8RT_7MYBp0uQhD45aowPMW1Ksg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
شما آشکارا دور تازه‌ای از حملات را آغاز کردید؛ آن هم شبانه. ایران شب گذشته گفت تنگه هرمز بسته است. سنتکام صبح امروز اعلام کرد تنگه هرمز باز است. کدام درست است، آقای رئیس‌جمهور؟
ترامپ:
نمی‌خواهم درباره‌اش صحبت کنم، چون می‌خواهم به زندگی لیندسی گراهام ادای احترام کنم. بنابراین نمی‌خواهم درباره‌اش حرف بزنم. پیش از تماس هم این را به شما گفتم.
بله، تنگه باز است. دیشب حسابی بمبارانشان کردیم. آن‌ها آدم‌های بسیار، بسیار شرور و بیماری هستند.
تمام روز گذشته با آن‌ها جلسه داشتیم. دیروز با یک توافق عالی برای ما موافقت کردند: نه برنامه هسته‌ای، نه این و نه آن، هیچ‌چیز. از همه‌چیز دست کشیدند و بعد از آن اتاق را ترک کردند و سپس، ظرف یک ساعت، پهپادی به‌سوی یک کشتی پرتاب کردند.
گفتم: «شما بیمارید؛ آدم‌های بیماری هستید.»
بنابراین ماجرا از همین قرار است. نمی‌خواهم درباره‌اش صحبت کنم.  می‌خواهم امروز درباره یک نفر صحبت کنم: لیندسی گراهام.
NBC
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76966" target="_blank">📅 18:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc9b71e145.mp4?token=LXpwiCR6I0-d3odhJIr8em3LeLIMsFHn9vyu8swpWL1nGEdXb1yGA4I0f7sTxGHPD0WlhCCmaTcsFAJ1WFGDxp7RvoFmnVInLCU6NoR25igTMWA7l1aGyFINCxb28_w_zWc-QEZdOVDl1WPqfUKl9gGLeGv9JkDwXIIRTW8Z_LRby34YEZnQWzB26fJmHdYkMmJXtQqD0uYVQxO6f9pKKbk_HMDsjV10fUUU8J2r-e2FgL46ToRHi87ofiC_ifLSpAb4LXVn8M7M_-Gjzbo7BFMkoPhmIorkFfK8shiVeppnHDvvhA6OUww7ar68NVprsrWfF_vedrtvQykAg3YtSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc9b71e145.mp4?token=LXpwiCR6I0-d3odhJIr8em3LeLIMsFHn9vyu8swpWL1nGEdXb1yGA4I0f7sTxGHPD0WlhCCmaTcsFAJ1WFGDxp7RvoFmnVInLCU6NoR25igTMWA7l1aGyFINCxb28_w_zWc-QEZdOVDl1WPqfUKl9gGLeGv9JkDwXIIRTW8Z_LRby34YEZnQWzB26fJmHdYkMmJXtQqD0uYVQxO6f9pKKbk_HMDsjV10fUUU8J2r-e2FgL46ToRHi87ofiC_ifLSpAb4LXVn8M7M_-Gjzbo7BFMkoPhmIorkFfK8shiVeppnHDvvhA6OUww7ar68NVprsrWfF_vedrtvQykAg3YtSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
مجری:
ایران اعلام کرده تنگه هرمز را بسته است. آیا این درست است، آقای رئیس‌جمهور؟
دونالد ترامپ:
تا جایی که به ما مربوط است، باز است. درباره‌اش صحبت نکن. درباره موضوعی صحبت کن که به خاطرش از من خواستی حرف بزنم.
مجری:
باشه. از وقتی که در اختیار ما گذاشتید ممنونیم، قربان. پیش از اینکه اجازه بدهم بروید، آیا حرف پایانی دیگری هست که می‌خواهید مردم آمریکا درباره لیندسی گراهام بدانند؟
ترامپ:
نه، فکر می‌کنم بهترین لحظه‌اش دفاع او از برت کاوانا بود؛ مرد فوق‌العاده‌ای که دموکرات‌ها با او بسیار، بسیار ناعادلانه رفتار کردند.
هرگز چیزی شبیه آن ندیده‌ام. شاید بدترین رفتاری بود که تا به حال با کسی دیده‌ام. من را هم شامل می‌شود. البته، شاید نه من، اما تقریباً همه را شامل می‌شود.
با او به‌شدت ناعادلانه رفتار شد و لیندسی، همان‌طور که یادت هست، آن لحظه را رقم زد. و می‌دانی، باید به تو بگویم، جیک، فکر می‌کنم یکی از ده لحظه برتر، شاید یکی از پنج لحظه برتر تاریخ سنا بود.
نمایشی باورنکردنی بود. و آن را از ته دل انجام داد. نسبت به برت احساس عمیقی داشت و آن را از ته دل انجام داد و کل ماجرا را برگرداند.
واقعاً شگفت‌انگیز بود. آن یکی را باید دوباره پخش کنند.
مجری:
خب، می‌دانم که از روی احترام به لیندسی گراهام نمی‌خواهید درباره هیچ موضوع دیگری صحبت کنید، اما ما دوست داریم زمانی دوباره شما را داشته باشیم، چون واقعاً پرسش‌های بسیار دیگری از شما دارم، قربان.
ترامپ:
حتماً. این کار را می‌کنیم. این کار را می‌کنیم.
مجری:
از اینکه تلفنی با ما همراه شدید متشکرم.
ترامپ:
می‌خواهیم CNN را در مسیری عادی قرار دهیم و این کار را خواهیم کرد.
مجری:
خب، من همین‌جا در مسیر عادی هستم، قربان، و از وقتی که در اختیار ما گذاشتید سپاسگزارم و ممنون که تماس گرفتید.
ترامپ:
باشه. خیلی ممنون.
مجری:
بسیار متشکرم. بعد از این وقفه کوتاه برمی‌گردیم.
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76965" target="_blank">📅 17:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxO6IGYK05IF6DNxsRpGWYZTcDeaf2XB5SP8hBbfzsxoXY7UbeCjqNw3HAnUMmD0RgPtD4kC86f9v0eUzm03V2RNjXBuDr1AM32xwvF9tax4XGsQG8FkcR6dcN3VYXTo0QJoVHBaCQXZ08IktuAbcS_Cyu4kMBSwl7xxAtpqQBJpASywBgCHXRxwrII1LFjfL0jADkas9HKMhYZg1r8-fyXvGRyZJ3MnloGxgyLOUQqd0pJxc9wW6jbggFO5G4_AjYupctvjLyQ9TCgIbkunt0vLE7mqRgLrjaBhtrnEfrlT9j9rYzwiJlktzd61sfq7XFnBVsnECQFIjTPBsC0jTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد مدیریت آبراه خلیج فارس، نهادی که به‌تازگی برای اعمال مدیریت جمهوری اسلامی ایران بر تنگه هرمز تاسیس شده است، یکشنبه ۲۱ تیرماه با انتشار بیانیه‌ای اعلام کرد تردد از این آبراه در حال حاضر امکان‌پذیر نیست.
در این بیانیه، آنچه «تحرکات غیرقانونی اخیر نیروهای نظامی ایالات متحده در منطقه» خوانده شد، علت توقف تردد عنوان شده است. این نهاد افزود پس از برقراری ثبات و آرامش، درخواست‌ها بر اساس زمان ثبت بررسی و مجوزهای لازم صادر خواهد شد.
@
VahidOOnLine
پست سنتکام، ترجمه ماشین:
🚫
ادعا: فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی اخیراً در رسانه دولتی گفته است هیچ شناور خارجی‌ای نمی‌تواند بدون شناسایی، ردیابی و نظارت نیروهای ایرانی از تنگه هرمز عبور کند.
✅
واقعیت: ایران تنگه هرمز را کنترل نمی‌کند. این تنگه همچنان یک آبراه بین‌المللی است. نیروهای ایالات متحده مستقر و آماده‌اند تا همین وضعیت را حفظ کنند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76964" target="_blank">📅 17:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76963">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fcwrn0GUjHaZPWcgCyfRh9JDLC4RGslhcu19fnZzaBVyETWNn1n8mwMb0-UDDIE0wSTCHcdbigRqr9ii2hcArh7TZ5Q7-42Dw3YxxeA7x8tuMj2Bag7zz2D-qpPeAlUvmyuY8uOP8iAHSmFIzhS-uBQ2i3evwXp5OAg0R6lzJPEgCqNDQFsMXBuu_75M5SPpCQZ5SNpvNOdS8oapsafCRUSVkT3bDc5nV1pChnrSTAhgRnXQZHwVRie7PbortWvUeaAddFuG_ZyAmZ2mDdaGkt6M9_OpSmK2AZ0O3KUB1W6NUgOZS9bxFIi9JV40mH7LPW38Up6T6KgmaS7Zx08J0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی نظامی آمریکا، ترجمه ماشین:
تنگه هرمز به روی همه شناورهایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای ایالات متحده مستقر و آماده‌اند تا اطمینان حاصل کنند که آزادی کشتیرانی، با وجود تجاوزگری بی‌دلیل، آزار و اذیت، تهدیدها و اعلامیه‌های خودسرانه ایران، همچنان برقرار می‌ماند. ایران کنترل تنگه را در دست ندارد. تردد در جریان است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76963" target="_blank">📅 15:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76956">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gW7oZrZ6hXWK0GlGOXkbUcq3384y_dpuF_8guq3RTXihJYE4QwMyJOKa1VSpd_ZbY7n_y3apU8MmvQbDb7vB6XEztCmG4UpRHq7c0oc25xgMRh9dpI_uFamXW7EbvGcydQo7VeLerEGJtWui4CrvVubxu_uDuRcocFELuAmSicMreFPgP8K9MKqeQRIr8eZnRZEFCnjD9Y2P2l-1vcPwvTPUItDMhhfbeU6_s76okzOje4_rbQg5R6OK7zIkAv_oCeQU3n2mloL0pkQ_w67lQu0YHPvxeiNdbYWTNH8IwyRbPVNJPGrqGx5x8I2UrX7SXe7iUOUGXguWzxH4r4vfIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GQ6MEYaOYvo8zeifNDdbrMuQPSoG0WXhC3BeD018UI_cD06pnFEsRyJor2msJ_4GWIJn4CZryH51AJwvt3FRMsNIPcd3giwpiWRcDkwv8O2RM0Vf7icZmXJb35dT92zWawU9Vhw5mS480I_2Ri9bfhSt5vwQTdM64xWPxPlmv9_uLLh2wZzxjr2-cAzZFK3Knb2HX2eApqvY4F8VSMWhQ1xBjnXolUBeL4FkoBqOBgTGCnQhnTlK1JQND1SeO_6EBFq3f3ITbaGzYHQvYnRRB6nd0wrZIkr12GS4yHT7w1l5vhiBgtwOiAm9e-9HRUpoAdpw5d3oaV_yJuZQu1LqCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZkzQqcD2ANAXvkBI596IC0ctmJlk-hkwekAGZqRnAfZHjQDmWT9aURKPkaVqNefTGi1aVQzkiWEJYEewyyO299pGInDp3HHFc-5B44Iug3e9_cE8s6FM5y46mLzuSh5W1GbYbW6lcKJXkWbdOheMnWDwZIpykNXZPSGU9NPFyZxyE5WpU9KJjXg0H_cfWoJWWCvUHe63T-1c6r_s1v_qbebjzGC_igZyoI2_AXn4iQlZRfk05tO_MCKxcDNd_yGKdCDZMwtYvHN3B93OjjWpX5aq5dZ2quVxfQY4RjAnu5XMh2srEiqn3amoMNKdAkL6MsXVkNOo6ZqO_FN-KzKOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CrBFwgh3I5n18pnBaTQGSiLbgthbSqhwj2GZpw3eKk5Q8ye3ZYzOwIynDQ0qmURHooY0zIANgbLTL08o_dPrMsRmyFnyMu4fYRY5ICMx2RIAQxQePPBozKRStaDb6V_RYQGZAU02M1NFnS_DjLXpOLsJZ7hvGhjCQ0T32e-toQnl0wTB2yj3gH9N29_HmKze79uijc5fo94I-KzFKKJrkVsUD3dzO1UY0R6zRPOthAv2up4hDn7iDvVgBkp7ubZGtkWrPat-5AlTskk01CfCJ_KOjWF3Vf3KxCfSxo8X0BMBE1YkXF57O03S1MmWdDS-AEXObJtSYYq5qC50zPAjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LQBPYkBGC1rbchLQnL_Y0_SA_IgbThHeEVX9ez_RCpyWLjWD-jjF6sNebKNfI_x2xc5h6J1cELZ1KsxPk7CYemvPrIJiaIddyR-ya0KstbOwxhuIkT4FzvTq1OX-9fMEfVvO8hrr3T5jKCGsZdMLkmh2PkKUwyTz7jttUnHTJ1o7IgXhig1PPd9lK8r4nkaL17D7_WbkVz_pZpmqXINQKetUzj7IOj5KkIczOpWWmFxiAjdEEVIIqGnXO3yXi0srDo1H3WSeE-TgV_KIa2qt35pfjPt6CyGb9YLUAUzctIQmn50ObC8wcRsucIrY2xElFcn0WdJfqs2-SZaRlMV-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v23GPsyE263habVik_Cpatm_DKweiMywAoSZd1-7iUBZQ1YJG1kpa8xelnUo-EQfu5AI0dRPB1fD9rVGPR96WuZ2xX864L71KRwhxdtq66WzQhkHFZD-ekyQl1RTTjxK4esOpmGbwGOVs1qdQo4JViNb2Tt7gs44Yf5yAZDCOPfzzOlerPjD0h7WZpuqDWiyr9hptyAAo2LtA5t1eOYNxZ1Be1x8gy-gpGzDMYH-fHLZou_XYpoT07Mk52UKYkg-gZeF0wzKOR1UfSY84tjoTIB2gM6QSa31oud563dZHN29J_0wYnBBnUBOsixCtzKZGECPwx82-D-_ZwYndinFkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51caf6abe5.mp4?token=f0jHjCQ3Qy2E9J940n-MRK7sE8tYr0b2ZPBdPSqWQkRKzgEZ3E256nZBU1Usj-5UCyoPwPsqahRzTlxqECdC7kinoPgyNPbuaq6gAHdna_EoHwGkIbiv25BTo3au_HxW3XmPsqflxwCX4y-mKEjw057Vp5Vjpr21YUL4Sb97xhf_kBeIQvUAvUR5hOdvo79OhbWjLHLh8_HBnteVV-yhVF36wnivBuAxM4JPIWK6HlJLcxR4xJPu87Sge8JJx_HLfjE9NhN2o_fQ9bduNB7T3f4s_1gAJ8ran9pSC2sINOsLvloiitCPEe1kkGKOOfc1l8U9-cZiO0Ff79oKmZ_-uw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51caf6abe5.mp4?token=f0jHjCQ3Qy2E9J940n-MRK7sE8tYr0b2ZPBdPSqWQkRKzgEZ3E256nZBU1Usj-5UCyoPwPsqahRzTlxqECdC7kinoPgyNPbuaq6gAHdna_EoHwGkIbiv25BTo3au_HxW3XmPsqflxwCX4y-mKEjw057Vp5Vjpr21YUL4Sb97xhf_kBeIQvUAvUR5hOdvo79OhbWjLHLh8_HBnteVV-yhVF36wnivBuAxM4JPIWK6HlJLcxR4xJPu87Sge8JJx_HLfjE9NhN2o_fQ9bduNB7T3f4s_1gAJ8ran9pSC2sINOsLvloiitCPEe1kkGKOOfc1l8U9-cZiO0Ff79oKmZ_-uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران و ارتش جمهوری اسلامی بامداد یک‌شنبه ۲۱ تیر۱۴۰۵، از گسترش دامنه حملات خود به پایگاه‌ها و تاسیسات نظامی آمریکا در منطقه خبر دادند و مدعی شدند هم‌زمان اهدافی در عمان، قطر، اردن، کویت و بحرین را هدف قرار داده‌اند.
هم‌زمان گزارش‌هایی از فعال شدن سامانه‌های پدافندی، به صدا درآمدن آژیر های خطر و شنیده شدن صدای انفجار در چند کشور منطقه منتشر شد.
این حملات در حالی رخ داده که عمان و قطر طی هفته‌های گذشته نقش اصلی میانجی‌گری میان جمهوری اسلامی و آمریکا را بر عهده داشته‌اند.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، یک روز پیش از این حملات در مسقط با بدر البو سعیدی، وزیر خارجه عمان، درباره کاهش تنش‌ها و سازوکار عبور امن کشتی‌ها از تنگه هرمز گفت‌وگو کرده بود. عمان همچنین پیشنهادهایی برای حفظ امنیت کشتیرانی و اجرای تفاهم‌های مربوط به تنگه هرمز ارائه داده بود.
قطر نیز در کنار پاکستان از میانجی‌های اصلی گفت‌وگوهای تهران و واشنگتن در چارچوب تفاهم‌نامه اسلام‌آباد محسوب می‌شود. با این حال، سپاه پاسداران هم‌زمان با تأکید مقام‌های جمهوری اسلامی بر ادامه مسیر دیپلماسی، بار دیگر مدعی حمله به پایگاه العدید در قطر شد و اکنون نیز از حمله به اهدافی در خاک دو کشور میانجی، عمان و قطر، خبر داده است.
@
VahidHeadline
فرماندار درود در استان لرستان روز یکشنبه ۲۱ تیرماه از برخورد بوستر (پیشران) یک موشک به یک منزل مسکونی در محله بلوار تختی این شهر خبر داد.
به گفته این مقام محلی یک واحد مسکونی و پارکینگ بر اثر این اصابت دچار خسارت شدند اما کسی بر اثر این سانحه کشته یا مجروح نشده است.
@
VahidOOnLine
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه ۲۱ تیرماه با انتشار پیامی در شبکه اجتماعی ایکس، درگذشت شیخ حمد بن خلیفه آل ثانی، امیر پیشین قطر، را تسلیت گفت.
عراقچی در این پیام به زبان عربی نوشت: « صمیمانه‌ترین مراتب تسلیت و همدردی خود را به امیر شیخ تمیم بن حمد آل ثانی، خاندان ارجمند آل ثانی و ملت برادر قطر ابراز می‌داریم.»
این پیام عراقچی در حالی منتشر می‌شود که بامداد روز یکشنبه، نیروهای مسلح جمهوری اسلامی، مناطقی در قطر را هدف حملات موشکی و پهپادی قرار داده بودند.
قطر یکی از میانجی‌گران کلیدی در جریان مذاکرات جمهوری اسلامی ایران با آمریکا به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76956" target="_blank">📅 15:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v96TusR6Fi8o3xfr-G6jV3lpD-8ptoirkXpDvHRz5zgX7EZGim5dO1Dw-gB82xVN36UKYS8xtdx0upZnnBH89lwQcx_ehzfN5gmYOncmMLCCbTA02DRF0t57AHAN8xhwSRHTRJgsQJ_pAXJd6cqux1nnhM__3JeUQR4Iybt3P-02bTRVL-RlluucQ09Io4LVQN3K2PKJUPZsffPqN1b1Mdqg0B504tEEX3X8V_rtcUy8MAAt8LEKb_JnbPvWExcTs4lb-eIEmsc_ZZzywq4A4oYp9CBWjaC6VWlpr1R1JgWQ9cMgiOblc-adafoS2kjR29hZckDzlY8m1nCVlHFxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bv8eBF73rR2baeBaUOREl8LiRwP_0ckiU2pxZ8nl3lAYS03tyz_6AaucSVeKVrgYtH8zI1MRIOBgNJuxwywngxJQC7rksphBskHDrufySiYnS5hR_eaQueqeAYrthJfbVU9mYyMCJE3Alnn1gOUXQTzagFwJjKzx5HqwDmu4GvyKfWnGct0YX7yrLRDaE1bp92iBi-Z56ggu9fvWS8YEIZS8kBjgqTNb0f6s1Bq5y0_6hpINS65xqkvejCZWqNdaR_kaspu6n_3pYVvjc6N5hkgkk2IucLLYBzDtIzZMXiHUF40paKyTBhJxkpBLXVhoEDDchplJDQ4tP6VpBFq68w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون امنیتی و انتظامی استاندار کرمان روز یکشنبه ۲۱ تیر اعلام کرد ارتش آمریکا یک دکل ارتباطی در ارتفاعات جنوب این استان را هدف قرار داده است.
به گزارش خبرگزاری مهر، بر اثر این حمله دو نفر مجروج و با هلی‌کوپتر به مراکز درکانی منتقل شدند.
@
VahidOOnLine
معاون سیاسی، امنیتی و اجتماعی استاندار لرستان، اعلام کرد شهر ویسیان از توابع شهرستان چگنی در استان لرستان، صبح یکشنبه ۲۱ تیرماه، دو بار هدف حمله هوایی قرار گرفته است.
سعید پورعلی گفت این حمله تلفات جانی نداشته و شرایط در این شهر هم‌اکنون عادی است.
پیشتر و در پی حملات نیروهای آمریکایی به استان‌های جنوبی ایران، معاون امنیتی استانداری خوزستان، از اصابت «پرتابه‌های دشمن» به مناطقی در شهرستان‌های هندیجان، ماهشهر و آبادان خبر داده بود.
شنیده شدن صدای انفجارهایی در بوشهر، بندرعباس، سیریک، عسلویه، کنگان و بندر نیز از گزارش‌های مربوط به تحرکات جنگی بامداد یکشنبه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76954" target="_blank">📅 15:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuOQQWQw578xUIpLgcHlvNS_o0Zjh_vIvQR0ucxXkZkEwSyNsoLo-Td3CufAiHsSw0-6MSfrReEO815Z22azZ4tN3X7FKCDLJSj6ezmAfClsLanAXL_VUN3XjfJdmPlbHbAgD1D5qy4rq2nf6CAaUnor28NtVkZUrOr-thyG8whLvPxgQbRGSQMzcs0wnVwe5VB-E508rOsxSJ7yok9Eh5Hpdvdkqyevr-kjqa3QGF9ML2Zkuc0H7R3xLTIKQkc7QN-JFK_MiEwkKDENcs9I42ppbcoIhR2Tf7opMIgAvL6KjrDSMpU7mqn9pQ_siF24wmE5pXsWubvjAoT2laSeAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیندسی گراهام، سناتور ارشد جمهوری‌خواه ایالت کارولینای جنوبی و از نزدیک‌ترین متحدان دونالد ترامپ، شامگاه شنبه ۲۰ تیر۱۴۰۵، در ۷۱ سالگی پس از یک دوره کوتاه بیماری درگذشت.
دفتر این سناتور با انتشار بیانیه‌ای اعلام کرد که گراهام شامگاه شنبه در گذشته و خانواده او از مردم خواسته‌اند در این دوران دشوار، ضمن دعا برای آنان، حریم خصوصی‌شان را نیز رعایت کنند.
گراهام یکی از شناخته‌شده‌ترین چهره‌های جریان محافظه‌کار آمریکا و از اعضای باسابقه مجلس سنای این کشور بود.
او طی سال‌های گذشته به‌ویژه در حوزه سیاست خارجی، از نزدیک‌ترین هم‌پیمانان دونالد ترامپ محسوب می‌شد و مواضعی تند علیه جمهوری اسلامی اتخاذ می‌کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76953" target="_blank">📅 15:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uLKIJDqTa0glWKTTDQfylGXrOAaUsSjdN2J-QOq4GfB0xGwoCoANaQY61h67HajVj5TW_8TJ-aGJXXPgp4sXcdD4gkkiaEJAjo56H3PhFpVrFHNdOdiGixe9oHoHPWoh8ytBe2FbCMcEXgqbGZLX38-KROeCDEk7-2EFuak-F0rKvcbqOY_ieapoN84-eEjvGuWxkMyetOn2qbaEPuMWDTRpkciqn9tnjFV0zrOjWXadEUPjskliZVoDvlOFuGkhDK0keUkrf9lyPIJ7pEfdv19iLKIGsigO5ljIqojN8Hevq-FzaZlKTZa9Ou7p_xmflBQqoWxnRlnTM4It2w1Q8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۱۲ حکم اعدام در پرونده "میدان علیخانی اصفهان" به مرحله اجرای احکام رسید
🔹️
بر اساس گزارش‌های منتشرشده و اطلاعاتی که به کمیته رسید، پرونده موسوم به «میدان علیخانی اصفهان» وارد مرحله اجرای احکام شده و جان ۱۲ زندانی در معرض خطر جدی اجرای حکم اعدام قرار دارد. گزارش‌ها حاکی از آن است که احکام پس از تأیید در دیوان عالی کشور در روز ۱۴ تیر، به اجرای احکام دادگاه انقلاب اصفهان ارسال شده‌اند.
🔹️
این پرونده به وقایع ۱۸ دی‌ماه ۱۴۰۴ در محدوده میدان علیخانی، میان ملک‌شهر و کاوه اصفهان، بازمی‌گردد؛ جایی که مقام‌های جمهوری اسلامی اعلام کردند چهار نیروی بسیج و یگان ویژه به نام‌های حسین رمضانی، محمد همتی، سید علی خشوعی و ولی‌الله صفری کشته‌ شده‌اند. در پی این رخداد، ۵۹ نفر بازداشت شدند و برای آنان پرونده‌ای گسترده تشکیل شد.
🔹️
بر اساس اطلاعات منتشرشده، رسیدگی به این پرونده در شعبه اول دادگاه انقلاب اصفهان به ریاست محمد براتی درچه و محمد توکلی (معروف به وکیلی، از قضات پرونده «خانه اصفهان») انجام شده و دادستان پرونده محمد نخجوان بوده است. همچنین گزارش شده که کل روند دادرسی تنها در سه جلسه یک‌ساعته برگزار شده است؛ موضوعی که نگرانی‌های جدی درباره رعایت اصول دادرسی عادلانه را افزایش داده است.
در میان ۵۹ متهم این پرونده، ۲۳ نفر با وجود تبرئه از برخی اتهامات، همچنان به احکام ۵ تا ۱۰ سال زندان محکوم شده‌اند.
🔹️
در مقابل، ۱۲ نفر با حکم اعدام روبه‌رو شده‌اند که در میان آنان چندین نوجوان و یک شهروند افغانستان نیز دیده می‌شود.
اسامی محکومان به اعدام عبارت‌اند از:
علیرضا سپاهی (متولد ۱۳۸۰) – محکوم به چهار بار اعدام
ابوالفضل سپاهی (متولد ۱۳۸۲) – محکوم به سه بار اعدام
علیرضا رئیسی (متولد ۱۳۸۳) – محکوم به دو بار اعدام
قائم حسینی (متولد ۱۳۸۴) – محکوم به دو بار اعدام
گل‌محمد محمدی (متولد ۱۳۸۱)، شهروند افغانستان که بنا بر گزارش‌ها به معترضان پناه داده بود – محکوم به دو بار اعدام
امیرحسین صفری (متولد ۱۳۷۷) – محکوم به اعدام
امیرحسین ملکی (متولد ۱۳۸۵) – محکوم به اعدام
علی دشتی (متولد ۱۳۸۵) – محکوم به اعدام
امیرحسین ابراهیمی انالوجه (متولد ۱۳۸۵) – محکوم به اعدام
شروین باقریان (متولد ۱۳۸۶) – محکوم به اعدام
عرفان اسفندیاری (متولد ۱۳۸۶) – محکوم به اعدام
ابوالفضل ابراهیمی (متولد ۱۳۸۶) – محکوم به اعدام
🔹️
همزمان، گزارش‌ها یادآوری می‌کنند که در روزهای ۱۸ و ۱۹ دی‌ماه در همین محدوده، شماری از شهروندان اصفهان در جریان اعتراضات با شلیک مستقیم نیروهای حکومتی جان خود را از دست دادند.
🔹️
نام محمد توکلی نیز در این پرونده بار دیگر مطرح شده است؛ قاضی‌ای که پیش‌تر در پرونده «خانه اصفهان» نیز حضور داشت؛ پرونده‌ای که به اعدام مجید کاظمی، صالح میرهاشمی و سعید یعقوبی انجامید و همچنان از پرونده‌های بحث‌برانگیز سال‌های اخیر به شمار می‌رود.
🔹️
با توجه به گزارش‌های منتشرشده درباره تأیید احکام در دیوان عالی کشور و ارسال پرونده به اجرای احکام، نگرانی‌ها نسبت به احتمال اجرای قریب‌الوقوع این احکام افزایش یافته است.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76952" target="_blank">📅 15:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ea07cb43fd.mp4?token=sxwa9WusqHnpmkLfnTQz2fCbGG5YnX80dqmZie5dBZG4lVj6ZaXxJefI9_MTz27ooqlh3Vhs-PculWLAdC9orDknl9ZBhWsn9HkpUQCzamm_zncuohLFCH00IpC_FpI-0HlZ0xLqahNr6TwrO8Y8FkTXAFtbsJPIaMjDTQv7j7EI2CduGrlCQdheeNemBiQS5o-K2PLmvWRIv2AIOP7j-yZ9WwiuOsVZPuPWlm04OHFCx5ImVPf2hYRielh4WLQBoploQLT2onCRIXYT1esFPUV9u22hqMfz-U03UOYYCC6sd-NC9kjI6kTULCEiQxQ0B8UVXaYQTRV0heUpiHGM3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ea07cb43fd.mp4?token=sxwa9WusqHnpmkLfnTQz2fCbGG5YnX80dqmZie5dBZG4lVj6ZaXxJefI9_MTz27ooqlh3Vhs-PculWLAdC9orDknl9ZBhWsn9HkpUQCzamm_zncuohLFCH00IpC_FpI-0HlZ0xLqahNr6TwrO8Y8FkTXAFtbsJPIaMjDTQv7j7EI2CduGrlCQdheeNemBiQS5o-K2PLmvWRIv2AIOP7j-yZ9WwiuOsVZPuPWlm04OHFCx5ImVPf2hYRielh4WLQBoploQLT2onCRIXYT1esFPUV9u22hqMfz-U03UOYYCC6sd-NC9kjI6kTULCEiQxQ0B8UVXaYQTRV0heUpiHGM3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام:‌ حدود ۱۴۰ هدف نظامی ایران را مورد اصابت قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) روز ۱۱ ژوئیه سومین دور حملات این هفته علیه ایران را به پایان رساند تا نیروهای ایرانی را بابت حمله به یک کشتی تجاری دیگر در تنگه هرمز پاسخ‌گو کند.
نیروهای آمریکایی با استفاده از مهمات نقطه‌زن شلیک‌شده از جنگنده‌های مستقر در خشکی و دریا، پهپادها و شناورهای نیروی دریایی، حدود ۱۴۰ هدف نظامی ایران را مورد اصابت قرار دادند. این اهداف شامل سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی، تأسیسات ذخیره مهمات، شبکه‌های ارتباطی و مراکز پایش ساحلی بود.
سنتکام طی سه شب حملات این هفته، به دستور فرمانده کل قوا بیش از ۳۰۰ هدف را مورد اصابت قرار داده است تا توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تضعیف شود. عبور کشتی‌های تجاری از این کریدور حیاتی دریایی بین‌المللی همچنان ادامه دارد.
از اوایل ماه مه تاکنون، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۴۰۰ میلیون بشکه نفت خام از تنگه هرمز کمک کرده‌اند.
CENTCOM
منابع حکومتی:
دومین شناور متخلف در تنگه هرمز مورد اصابت قرارگرفت/ مرکز تعمیرات و نگهداری جنگنده‌ها و مرکز فرماندهی و کنترل  ین پایگاه در هم کوبیده شد
روابط عمومی سپاه پاسداران انقلاب اسلامی اعلام کرد:
بسم الله قاصم الجبارین
فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ
🔹
در پاسخ به ادامه تجاوزات ارتش کودک‌کش آمریکا به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران، علاوه بر اصابت و متوقف‌سازی دومین شناور متخلف در تنگه هرمز، پایگاه هوایی راهبردی آمریکا در العدید قطر در مرحله دوم عملیات مقابله به مثل هدف موشک‌های بالستیک قرار گرفت و مرکز تعمیرات و نگهداری جنگنده‌های و مرکز فرماندهی این پایگاه در هم کوبیده شد.
🔹
دشمن امریکایی - صهیونی بداند، استمرار تجاوزات او پاسخ‌های کوبنده‌تر را در بر خواهد داشت.
بجنگ تا بجنگیم.
روابط عمومی سپاه پاسداران انقلاب اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76951" target="_blank">📅 07:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76949">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkuvIlHfOqgld0B-fBtdf4aL_rp-NXgYGr5XhigJkMNO4xGY0xP2X3Q-94VGiwJl5EBsMxV1Cz_h1Fct-FxInjgD_uNt-2ZUnjp-cmdcPJAM9RbBpOFN_TSDyApd-v_keZJv-Phm9TsOqmTuGgKEGLpAK-F14fhbRcmErCWO0BPStW5bUIZVhRbOnvGfXGqXjCGAiYlj7Q122zx0UdVusYoKHVbFrTl9xyu7fszgC8tX0RN0UfbuPls0ElTvyt-u-8K2CMO2m0kTld1CjDLPnuOlppYpCApfyBK51M2oMTeydrWEEnpD_AhCSx251SvQKysuNXGlvJFZO4ap2PIyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از شاهدان عینی، خبر از شنیده شدن صدای انفجار در دوحه، پایتخت قطر خبر داد.
پیش از این، وزارت کشور امارات متحده عربی با انتشار هشداری فوری، صبح شنبه، اعلام کرد که سیستم‌های پدافند هوایی این کشور در حال حاضر در حال مقابله با یک «تهدید موشکی» هستند.
همزمان وزارت کشور بحرین نیز اعلام کرد که آژیرهای خطر در این کشور، صبح یکشنبه، به صدا درآمده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76949" target="_blank">📅 06:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb22334a3e.mov?token=eBtiUYtkynX3stlGMWCMon1YLB-QHOmzf04LJdJMXi8rB7jGhAEHnPt75uFmDtSedB9qAVk_bRtu5W6cMDhquvOiI_rW7EimqM70x35nutUt2ETY403cyC5ZY4RotL2zcXTBMY2uaVSDUQKV0ErqgOzXeNJ62JsP_FURik1N8FZVAKbTCHjAcZH9EtGK9dI6-i7PncNonajK17aakT61w9trlXCmyxJsm-6HdGneDo4w5oWIjx4c2fvv8FaHLz6CWRFSKD0BW9IsBi8vloH_M6SH0QGDRkT6ebT8jWJoPqPtHv7QPzT9IPU5UxhGy4q8YBeNqvXlfcvLFeurhyINxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb22334a3e.mov?token=eBtiUYtkynX3stlGMWCMon1YLB-QHOmzf04LJdJMXi8rB7jGhAEHnPt75uFmDtSedB9qAVk_bRtu5W6cMDhquvOiI_rW7EimqM70x35nutUt2ETY403cyC5ZY4RotL2zcXTBMY2uaVSDUQKV0ErqgOzXeNJ62JsP_FURik1N8FZVAKbTCHjAcZH9EtGK9dI6-i7PncNonajK17aakT61w9trlXCmyxJsm-6HdGneDo4w5oWIjx4c2fvv8FaHLz6CWRFSKD0BW9IsBi8vloH_M6SH0QGDRkT6ebT8jWJoPqPtHv7QPzT9IPU5UxhGy4q8YBeNqvXlfcvLFeurhyINxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی (به همراه تصاویر مختلفی از رد دو موشک):
همین الان از خمین دوتا موشک شلیک شد
درود وحید جان همین الان از خمین دو تا موشک شلیک شد
سلام،،ساعت ۵ نی دوتا موشک از الیگودرز شلیک شد
زنجان
۲۱ تیر ۱۴۰۵ ساعت ۵:۳۲
صدای بلند و ممتدی هم اومد برای چند ثانیه
وحید این دفعه هم از سمت خمین و الیگودرز شلیک کردن صداش زیاد بود ولی ۲ تا رد موشک بیشتر نمیبینم.
شلیک موشک از خمین
درود وحید جان از حدود زنجان موشک بلند شد دوتا
🔄
شهرستان داراب استان فارس ساعت ۶ شلیک ۲ موشک
یه موشک از داراب فارس بلند شد رفت ساعت 6:05 دقیقه
همزمان:
آژیر در بحرین
sirens in bahrain
5 دقیقه پیش قطر صدای پدافند اومد و آلارم روی گوشیا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76947" target="_blank">📅 05:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PI5s6oOyA8l0ILG2iltMK5ZwMx3PxxAzqJxLW4yY6OYFRsGVb6O77JJ1ztlZ_Gs-CbGSMyVgVk3njkSTRh6xtFKwxRy-gI5BDJWihdD-lWOY7bKKPz3Y_rjJPFUq-W8knNTAOE3aFPTcjWQKhQOthfk4ooG-3LYU1gOx_sOPAEHQsrF7dF0YjL7Go8sRN-GfyGayURq8JoHIFliIwC9-GKKIdn8Og2FfavcRV_ipm8p-D6VdlMUvft08237glPeFoOXduR257N7T_2XCmHumhYwa3NKMgOcQ7q7m9FG4Fd3o04vBXCgB6WCWA1KR7S9YpXc_-vCznj3qelU3pR-grQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی استانداری خوزستان گفته است که شهرستان‌های هندیجان، ماهشهر و آبادان هدف پرتابه‌هایی قرار گرفته‌اند.
هنوز جزئیاتی درباره محل دقیق اصابت، خسارات و تلفات احتمالی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/76946" target="_blank">📅 05:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcgpQp86re-oYKkHy8FFE_HK09PJjrWYx0wUQb43H2R_bo4gb_4EJR3klA8DaqdHjXy5yjh7Iy7L0f7TUQ5zRk1oliPluWs9OF-3O4gKnEI8U9Fa0MuA3p4h9iFITAQ5KI-7G3xnY3k5FGMC1V4FVs9MM-b4E2O3RpI7tc2XlE837J2bYkiPjUb2OTbyG7KQ3774g6_THHi5cIKwND-xDG4j0u0rsmjDqLv5bOZM6E6ZGksho637USPMTdImLydKuhzID25ogwVtALBcmfltosFXslmXOLRuwNY1IveG0MNNxtvWLe64SPwckhaKXhm7TWtvqcohQQKJmbLhWOxlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر و پیام‌های دریافتی تایید نشده:
سلام باز بوشهرو زدن ۳:۴۶
سلام وحید جان بوشهر سمت سرتل رادار زدن
بوشهر همین الان 3:48 دقیقه دو بار لرزید
سلام وحید جان ۳:۴۷ دقیقه بوشهر سه تا انفجار شدید شنیدیم
اقای وحید ساعت ۳ وربع صدای انفجار شدید اومد عسلویه از خواب پریدم
صدای دوتا انفجار  الان اومد  پایگاه هوایی بوشهر
۵ تا زد سایت موشکی چغادک-بوشهر،۰۳:۴۵
سلام وحید جان
ساعت 03:47
بوشهر سه چاربار صدای انفجار اومد
سلام وحید جان الان 3:45 دقیقه بهمنی بوشهر صدا اومد دو سه تا که خونه لرزید
🔄
جاسک
وحید ۳:۵۰ جاسک رو زد ۳ بار
سلام وحید جان همین الان دو انفجار وحشتناک در جاسک
منطقه نیرو دریایی جاسک
3:50 صدای جنگنده و چندین انفجار از بندر جاسک
سلام وحید صدای چند انفجار شدید در بندر جاسک
🔄
جاسک
خدایا بازم داره میزنه
دوتا دقیقا همون نقطه قبلی زد
ساعت ۵ جاسک
۲ انفجار دیگه جاسک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76945" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VUS1DVErAuWWFJWPWkNbr1FLQqzDFIfJzJ5V6zy19yc1WZMq_6Rbbox4WuUIv5gCq9r_ryvd4PsFzpF7wTRF4WyTc6RoO5k_nDStB9i9Qh67k-_HMCjsXBAweIIu8ismx_sQNSzt0hqfZhnqrPvINAYUMr1JP95VxyTXbNoArUPgBkHgBcmtN9ilvn37Z9Q36Xr-iSycsWqCfCaOyEChnXaTz1nOKeRvBFcXyYTbr4xIuxIzljQtQM7yiGYWLClI5IPkXVeFEWoxiCSjFmxHiRJ1iFAVhTcxoE0vnfJtTgfqFAE2Lug2TtlhnKr4uWl-vOxzlmYBEg1623A167LgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا:
"ایران انتخاب بدی کرد. حالا تاوانش را می‌دهد."
PeteHegseth
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76944" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پیام‌‌های دریافتی:
دوتا سنگین زد کنارک همین الان  ۳:۱۸
چابهار الان دو دفعه صدای انفجار اومد
سلام وحید جان چابهار همین الان دو تا انفجار مهیب
ساعت ۳:۱۸ دقیقه دو انفجار با صدای بلند در کنارک
همین الان ساعت 3:30 دو انفجار شدید در جابهار و یکی هم صداش خیلی دور بود شاید اطراف فرودگاه کنارک. ولی دو انفجار چابهار واقعا شدید بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76943" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76942">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سنتکام: سومین دور حملات این هفته علیه ایران را آغاز کردیم
ترجمه ماشین:
امروز ساعت ۷:۱۵ عصر به وقت شرق آمریکا، [۲:۱۵ بامداد شنبه تهران] نیروهای فرماندهی مرکزی ایالات متحده پس از آنکه نیروهای سپاه پاسداران انقلاب اسلامی به‌طور آشکار به کشتی کانتینری «M/V GFS Galaxy» با پرچم قبرس در حال عبور از تنگه هرمز حمله کردند، سومین دور حملات این هفته علیه ایران را آغاز کردند.
یکی از اعضای غیرنظامی خدمه مفقود شده و کشتی به‌دلیل آتش‌سوزی در داخل و وارد آمدن خسارت قابل‌توجه به موتورخانه، قادر به ادامه سفر نیست.
پس از آنکه ایران به‌دلیل حملات پیشین به کشتی‌های تجاری پاسخگو شناخته شد، بار دیگر فرصتی به این کشور داده شد تا پایبندی خود به تفاهم‌نامه را نشان دهد، اما بار دیگر ناکام ماند.
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی به این کشور تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76942" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aUclG4Y-f5rh6pAXcLxeY-XnG3BdRy0QhOF_cx5-ZChQd6Js9RFy8-5Ob273r0yCQpweuTkCOmDcDoWcbApbQxhd1j2eR2ctQd0u1X31Z3c3MdqqEkV1zc091mymKRHYs1GeygcYSY4cK_cqSQV7AcQ4CnkM2zjvb5W9v6VLQdSgLd5xfESFeY0Ctb9nzcuiC3feugv6roPYpi6BEJDJY4mTWWitR3EWp0XdyCOKKelPRsFMSAuNSQah9MIxyl82IrYUo24d00lIFOjD6-3IJjW_Nupac0kNHDP91CN_2SAqHB1204vNGJHmDMwnZo-lQTQQXouMoG7Mc_ZmH20m2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
‌
بوشهر صدای چند انفجار لرزش زمین احساس شد زیرپام
صدای دو تا انفجار بندر دیر ساعت ۲:۴۶
۲۱ تیر
سلام
ساعت ۲:۴۰ شنيده شدن چهار تا پنج انفجار در کنگان و حوالی آن
وحیدجان
الان حدود دو و چهل و پنج دقیقه صدای چهار پنج انفجار بزرگ توی بوشهر
شبشه های خونه لرزید
وحیدجان سمت نیروگاهه
من تنگک هستم الان دود و نور قرمز از اون سمت می بینم
سلام اقا وحید ساعت ۲:۴۵ بندر کنگان چهارتا صدای انفجار اومد
سلام ساعت ۲ و ۵۰ دقیقه بوشهر صدای چندین انفجار
۲:۵۰ بوشهر صدا انفجار
صدای چند انفجار اومد در بندرکنگان
سلام.ساعت ۲/۴۵ دقیقه شهرستان دیر استان بوشهر.صدای دو انفجار مهیب با فاصله یک دقیقه از هم شنیده شد.موجش شدید بود
سلام وحید
بندر دیر رو زدن ساعت ۲:۴۶
تو جنک هم ۱۰ ۱۲ باری زد یا بیشتر یادم نیست الان
اسکله نیرو دریایی زدن
🔄
همین الان ستا انفجار دیگهههههه.
بندر دیر.
وحید جان الان ساعت ۲:۵۶ باز دوتا بمب دیگه بندر دیر رو زدن
۲:۵۵ بازم زدن بندر دیر رو
دو بار دیگه ۲:۵۶ زدن
کنگان همین الان دوتا صدای بزرگ انفجار اومد۲:۵۶
کنگان رو دوباره زدن
🔄
تایید نشده:
صدای انفجار شدید بندرعباس
همین الان قشم صدای یه انفجار مهیب اومد
دقیقا ساعت ۳
ساعت ۳:۱ بندرعباس صدای دو انفجار پشت هم اومد
صدای انفجار، سیریک.
🔄
استان بوشهر
سلام وحید جان بندر بوالخیر  رو زدن
سلام اقا وحید بندر بوالخیرو زدن
🔄
عسلویه بوشهر
یکی که در واکنش به خبر  قبلی درباره عسلویه پیام داده بود: "ببین ۱۰ دیقه پیش صدا اومد ولی نزدیک نبود" الان پیام داده که:
وحید اینجارو دارن میزنن
همین الان صدا و لرزش خونه ۱۰ تا انفجار
عسلویه
پیامی دیگر:
عسلویه
حدود یک ساعته نه یا ده صدای انفجار اومد که دوتای اخری خیلی شدیدتر بود
ولی منطقه پتروشیمی و پالایشگاه خداروشکر خبری نیست
همه‌ی صداها از  سمت ساحل حاله و ساحل بنود یا بندر تین هستن
تقریباً بین۱۰تا ۲۰ کیلومتر با عسلویه فاصله دارن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76941" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76940">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQxulJH0yw4TqsALqk0C8A0D0IGib48nWqAX2p_x9XnWfOvaMM3EU9A5PvA3iB-_WoU7usa3a4k3xj-OdV2fX1IGrnRDPu-I0Yj-IKR-vnWfQ2XCF1eLPagt7s8w3TeboUWEWqgw8W6hkrul68XGZMAnNJIrbrhwpBheDIs4VO-nic8IQrQzG9rqxjrASSyBT_ILFcc-TNcDvDE41gp4W81WUbEQ_jNogFjgHlLHx5UF4V_plrQrjaTinrQXsjMHDAtbHq85RRHxFZm9vbc4t85XW08CgjAKHNZaZqB249xDbT0BqzEbzxm7D2M14vy1xYkdAj4NdOcG-v6MZUTTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با بیانیه سپاه پاسداران مبنی بر «بسته بودن تنگه هرمز تا اطلاع ثانوی و پایان مداخلات آمریکا»، یک مقام آمریکایی در گفتگو با خبرنگار آکسیوس اعلام کرد که سپاه یک موشک به سمت یک کشتی باری تجاری که قصد عبور از تنگه هرمز را داشت، شلیک کرده است.
به گفته این مقام، کشتی مذکور مورد اصابت قرار گرفته و دچار خسارت شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76940" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ve5tMQB7jntfPx4yyzfzfkhqz_UJuOzcQO-NgNxHOyYQMRa_-7mQotAhQPXPYlq3tlL2uQXmyAPYHE8s18C7vuY5Qrh_oq6A4IpoMTZ-7pqaCCVZ6edmjzOgWQvAZ_QFGTMDzDBG9kWmze4cFQLgj2uSY-04TbXD1cFO6ym8RwaH5ytNCEQ9EteJKB3nLO6HlZotitdRXevJJhwR23pVvezeB2hUehtXQGsoq57UNEyDZEvx_1h1is1_aUw2-3xLS-EJYGju8s8_pQLkT0HCacOcBN9cPvLyfZ0BspOSEEgptbKIaCUk9DADjof-xPt8jJJQ3QG-_qbgjdVbsI-AAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: یک کشتی را هدف قرار دادیم / تنگه هرمز تا اطلاع ثانوی بسته شد
ایرنا:
نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
بسم الله قاصم الجبارین
در اطلاعیه قبلی گفته بودیم مداخلات بیگانگان و تعیین مسیر غیرقانونی حرکت کشتی ها در تنگه هرمز، برخورد قاطع ما را به دنبال خواهد داشت و روند افزایش ترددها در تنگه را با اخلال مواجه خواهد کرد.
🔹
ساعاتی قبل، این تذکرات نادیده گرفته شد و با تحریک بیگانگان چند کشتی تلاش کردند از مسیر غیرمصوب حرکت کنند و به اخطارها و تذکرات ما در اصلاح مسیر و حرکت در مسیر مصوب بی اعتنایی کردند.
🔹
به ناچار یک فروند کشتی‌ که با خاموش کردن سامانه‌های خود امنیت دریایی را به مخاطره افکنده بود؛ مورد اصابت شلیک‌اخطار واقع و متوقف شد.
🔹
به دنبال این حادثه، اولا با توجه به بروز این ناامنی به سبب مداخله غیرقانونی بیگانگان، تنگه هرمز تا اطلاع ثانوی و تا پایان مداخلات آمریکا در این منطقه بسته و هیچ شناوری اجازه تردد نخواهد داشت، ثانیا اگر دشمن متجاوز به بهانه این حادثه که خود، مسبب آن بوده است، خطایی کند و تجاوز جدیدی علیه ما داشته باشد با شدت پاسخ داده خواهد شد و پایگاه های جدیدی از دشمن در منطقه مورد هدف قرار خواهد گرفت.
🔹
عواقب چنین مداخله‌ای بر عهده دشمن آمریکایی - صهیونی و کشورهایی است که خاک خود را برای این تهدیدات در اختیار پایگاه دشمن گذاشته‌اند.
و ما النصر الا من عند الله العزیز الحکیم
نیروی دریایی سپاه پاسداران انقلاب اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76939" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76938">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبرنگار اکسیوس:
‏
🇴🇲
🇮🇷
یک دیپلمات که در جریان مذاکرات قرار گرفته است گفت عمان در گفت‌وگوهای امروز مسقط پیشنهاد کرد که مسیر جنوبی در آب‌های عمان و مسیر شمالی در آب‌های ایران، هر دو به‌طور کامل فعال باشند.
‏
🇴🇲
🇮🇷
این دیپلمات گفت طبق پیشنهاد عمان، مسیر جنوبی بدون هیچ‌گونه الزام برای دریافت مجوز باز خواهد بود؛ همان‌طور که پیش از جنگ بود.
‏
🇮🇷
🇴🇲
این دیپلمات گفت ایرانی‌ها نتوانستند این پیشنهاد را در جلسه به تصویب برسانند و ناچار شدند آن را برای گفت‌وگوهای داخلی به تهران ببرند.
BarakRavid
سی‌ان‌ان:
یک منبع آگاه از مذاکرات به سی‌ان‌ان گفت عمان پیشنهادی را برای مدیریت تردد در تنگه هرمز از طریق دو مسیر با کنترل جداگانه تدوین کرده است.
بر اساس این توافق که هنوز نهایی نشده است، هر دو کریدور باز خواهند ماند. کریدور جنوبی که از آب‌های سرزمینی عمان عبور می‌کند، امکان کشتیرانی آزاد را مطابق شرایط پیش از جنگ فراهم خواهد کرد.
کشتی‌هایی که از کریدور شمالی، در آب‌های سرزمینی ایران، عبور می‌کنند، باید از ایران مجوز قبلی دریافت کنند؛ با این حال، طبق این توافق هیچ عوارضی از آن‌ها دریافت نخواهد شد.
CNN
علی قلهکی
:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76938" target="_blank">📅 22:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hgAxllljWi-aza55dK5rDG7SwatVu8C6GZdfpVEg8rTZc2LY7AEc-yc9ZET0YpKWeEJSVD8l4s2_WR1mTFUVIX1e6AOAGZYaHBE32HURzmPpy3jw6VZRIgSpY5U1n_kd_-YqLt2cDC20-mpBwgrLMrLXgU8O5ul87AO22OdiHUAjbFqdYwL3FYfTKtMxsRx-no2goeyQ18M_eZK3yRS8jtKTZKAGF1G0IVwsZMT96hlx4212wqHwTyWtOqFEdB7gKZvrtBOyHE-rjo28j-tUawKzy8tgwD8rXGsT2oQZ9DXFd0t99_I91R73sHGgBeCYil2dIbhElbusZQqCHUvSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا، طی روزهای گذشته پیش بینی شده بود گرمای هوا تا هفته منتهی به دوم مردادماه با میانگین دمای بالاتر از ۳۹.۷ درجه تداوم خواهد داشت، از این رو تمامی سناریوهای بهره‌برداری شبکه بر مبنای نیاز مصرف ۷۵ هزار و ۵۰۰ مگاوات طراحی شده و مرکز ملی راهبری شبکه برق کشور و واحدهای عملیاتی صنعت برق در آماده‌باش کامل قرار دارند با این وجود بنا به گفته مسوولان شرکت توانیر  هیچ محدودیتی در تامین برق بخش خانگی اعمال نخواهد شد.
اما امروز  ۲۰ تیرماه برخی کاربران ایسنا [و بسیاری از دنبال‌کنندگان اینجا] طی تماسی عنوان کردند که در برخی مناطق  همچون محدوده ولیعصر، مطهری و قائم‌مقام فراهانی [و مناطقی دیگر و شهرهایی دیگر] با قطعی برق چهار ساعته مواجه شدند و با وجود پیگیری‌های ایسنا از شرکت توزیع نیروی برق تهران بزرگ تاکنون علت این خاموشی‌ها اعلام نشده است.
به گفته مشترکان همزمان، حجم بالای تماس‌های شهروندان با سامانه فوریت‌های برق ۱۲۱ موجب شده زمان انتظار برای ارتباط با اپراتور در برخی موارد به حدود نیم ساعت برسد.
isna.ir
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76937" target="_blank">📅 17:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qmSFsatqS1FGl_rPxy9lu2eqR9j0iLnJ5cVr5eOtyWYU-96oENx307_fOiTk7eVFY46ndeXhKpdvnCDW3_Sc2msRHYqVzRKbWXbOMTgbC9P03jFD_LMsZPPBc5U0LDo-vHlG5Q2jxPTXjg9DJ8NTnUGJLaVJwhE0d7QsMwtWSiR0puSq0fyifDazv3vbi7GuPr0VIw9QJCsW-scgkifWO_9Fd8p6-wCTXaH9-Ev-9ZjZIneExhnnBZn-MtQ0nginWAZHPemW9pXX4xiAknRlSUJ7u97XU60atT0KoQSLdlJSb7ll3ggbCbOge7b3BkwG5JVdUbgNm6CRBmgtxbFUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه امام رضا اعلام کرد دو نیروی بسیجی به نام‌های «سید سجاد علوی» و «مهدی هنرمند» در حوالی میدان سرافرازان مشهد هدف تیراندازی قرار گرفتند و کشته شدند.
بر اساس اطلاعیه سپاه، این دو بسیجی در زمان وقوع حادثه در حال گشت‌زنی در محدوده بلوار سرافرازان، در فاصله حدود ۱۵ کیلومتری حرم امام رضا، بودند. این حادثه همزمان با برگزاری مراسم تشییع و تدفین علی خامنه‌ای در مشهد رخ داد.
سپاه امام رضا اعلام کرده است که این نیروها در چارچوب مأموریت‌های تأمین امنیت مراسم تشییع و خاکسپاری علی خامنه‌ای در منطقه حضور داشتند.
در این حادثه همچنین یک عابر پیاده مجروح شد و به بیمارستان انتقال یافت.
اعلام کشته شدن این دو بسیجی در حالی صورت می‌گیرد که امیرالله شمقدری، معاون امنیتی [دروغگوی] استانداری خراسان رضوی، جمعه ۱۹ تیرماه
گفته بود
تیراندازی در بلوار سرافرازان مشهد «اقدامی تروریستی» نبوده و ریشه در یک «درگیری شخصی» داشته است.
خبر این درگیری مسلحانه همزمان با تدفین علی خامنه‌ای در شامگاه ۱۹ تیر منتشر شده بود. آن‌زمان اما جزئيات آن منتشر نشده بود. اگرچه ساعتی پس از این درگیری سازمان هواپیمایی کشوری از اجرای «مجموعه‌ای از تمهیدات ویژه» در مشهد خبر داده بود. همچنین گزارش‌ها حاکی از آن است که برای ساعاتی، مسیرهای خروجی شهر مشهد بسته شد و تدابیر امنیتی در این شهر به‌طور چشمگیری افزایش یافت.
این حادثه در شرایطی رخ داد که مشهد میزبان آخرین مرحله از مراسم تشییع و خاکسپاری علی خامنه‌ای بود و هزاران نفر برای شرکت در این مراسم به این شهر سفر کرده و امنیت شهر در بالاترین سطح خود بود.
@
VahidHeadline
شخص همون معاونی که اون طور صریح دروغ گفته بود امروز آمار هم اعلام کرده درباره تشییع‌کنندکان مشهد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76936" target="_blank">📅 17:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JhPqz1IbXO5fUmZx5aJ-mqHvpsPWECBMl-gi4meA2NAgByj5rKY-c4FFyH73R8CKtE1NByXqWyGQYhsWmOXVwuQKMTd7daR8cFgBJ21Y8SlWu16p60YIGGyylbYFfHeox6Faj4fWuvh363GQ0UtGSwrwirZ1gJ_Tv1Obw_qCAMmO6m5fz1fxu7pAiuKtAlFji6MNcVrQHAyTl-cTs9BpNkohW1E3MIdwG1bywrPOQG3NsQyn_HYlyMO_vuPenxuTujfqww3ePjmwC0BQf1Xq2KoiARcSzhSnCHuz3NQPI60ZbLLnBp7EpRJP0rZjZrdbH3Lp8Dbu4BR9rxtpXoRpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، رهبر جمهوری اسلامی، در پیام مکتوبی منسوب به او که روز شنبه ۲۰ تیرماه منتشر شد اما تاریخ آن مربوط به دو روز پیش است، اعلام کرد انتقام خون پدرش علی خامنه‌ای «به‌طور حتمی باید صورت بگیرد».
خامنه‌ای در این پیام همچنین به «قاتلین» پدرش هشدار داد که «این جنایتکاران که فهرستی از صدر تا ذیل‌شان موجود است، آرزوی مرگ آرام و در بستر را با خود به گور خواهند برد».
او در عین حال تأکید کرد که انتقام «متوقف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقق خواهد شد و به‌زودی آحادِ آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد».
مجتبی خامنه‌ای در این پیام نامی از کسی نبرد، بخش‌های دیگر پیام خود را نیز به تشکر از تشییع‌کنندگان رهبر کشته‌شدهٔ جمهوری اسلامی اختصاص داد و به درگیری‌های اخیر ایران و آمریکا بر سر آتش‌بس، تفاهم‌نامه و تنگه هرمز نیز هیچ اشاره‌ای نکرد.
دونالد ترامپ، رئیس‌جمهور آمریکا، بامداد شنبه نوشت در صورت هرگونه اقدام یا تلاش برای ترور او، «هزار موشک آمادهٔ شلیک» به سوی ایران هدف‌گیری شده و ارتش آمریکا برای یک دورهٔ یک‌ساله، با امکان تمدید، آماده است «تمام مناطق ایران را به‌طور کامل نابود کند».
پیام عمومی مکتوب قبلی منسوب به مجتبی خامنه‌ای ۱۱ روز پیش به‌مناسبت هفتهٔ قوه قضاییه منتشر شده بود.
مجتبی خامنه‌ای در عین حال غایب بزرگ مراسم تشییع علی خامنه‌ای بود که بیش از چهار ماه پس از کشته‌ شدنش در اولین موج از حملات آمریکا و اسرائیل طی چندین روز با سازماندهی حکومت برگزار شد و نهایتاً ۱۸ تیرماه در مشهد به پایان رسید.
در جریان تشییع جنازهٔ یک‌هفته‌ای علی خامنه‌ای، بسیاری از شرکت‌کنندگان در این مراسم خواستار «خون‌خواهی» و «عدم سازش» شدند و گروهی نیز پارچه‌نوشتهٔ بسیار بزرگی با مضمون درخواست برای «قتل دونالد ترامپ» همراه داشتند.
مجتبی خامنه‌ای بود که کمتر از ۱۰ روز پس از کشته شدن پدرش در نهم اسفند ۱۴۰۴ به‌عنوان رهبر تازه جمهوری اسلامی معرفی شد، در هیچ بخشی از این مراسم حضور نداشت. در این مدت طولانی هیچ فایلی صوتی یا ویدئویی نیز از او که نشان دهد در چه وضعیتی است، منتشر نشده است.
این در حالی است که در مراسم تشییع جنازه علی خامنه‌ای تقریباً تمامی مقام‌های ارشد جمهوری اسلامی حضور داشتند، از سران سه قوه تا فرماندهان سپاه پاسداران و حتی سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از ۹ اسفندماه پارسال یعنی آغاز جنگ تاکنون خبری از آن‌ها نبود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76935" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fxf4mq74hHVm2Xm5Uv4CWDpOXFF7BZk166NaCOR48oc7ELE9dinpQt6V-C0AIRZrAKTl-Ag2BLXlkJ_Rby8uSx07wz9LvR-Zbwzcqpgdl1xzpimsmtb-rS_6PLe30ocsUdai671nIIr9RN-vK5iCRpT-28K3IaHbB57cqLVIRDDwbGdN48HjtrR42PZCb_vXpuwzUyyOmv2468IsdwHbNuKZen79IvpNojtqXYCS5pq96Y5YeGzJQcqATVVJol_6ragdrkA3jXoIJHvnWDzpGokIL-e4UTwT_e2eoamkHtqemBvX0MkuT-3_wux9WOy29HW5Z3Poml12iK-ahOOa5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، از صدور حکم حبس برای یک فعال صنفی معلمان خبر داد.
این شورا روز شنبه ۲۰ تیر اعلام کرد شعبه ۱۰۳ دادگاه کیفری ممسنی شکرالله احمدی، بازرس این شورا و عضو هیئت‌مدیره انجمن صنفی معلمان فارس، را در مجموع به سه سال و هفت ماه و ۱۵ روز حبس محکوم کرده است.
آقای احمدی به «اجتماع و تبانی برای ارتکاب جرم علیه امنیت داخلی و خارجی» و «فعالیت تبلیغی علیه نظام جمهوری اسلامی» محکوم شده است. او ۲۰ دی ۱۴۰۴ در خانه‌اش بازداشت و چند روز بعد آزاد شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76934" target="_blank">📅 17:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brc3jNkZ46gz0q8BzDBcI43CiPvDPqz_8iA3BHxCbRpAOm_XP86TDcDmsYi-eSYLflGxq9pVXbtFMr__JK7Vm8V_JMxoMwXL_Py-u98KaGJ6JqL7L2qxRX721IgHD8oRJyujLTI8Npa8rvwdfmqjdT43v_QO0ibs0dKmNeomElEwlhdHDaAZTIQh4FlzDquUsXxQb7vWj_NEdqcfaAwbcl1jvfMLhgwbfRGFxuhAITG6Gsb29EJ-v7SwSnApKxWLvhTrV_zNp7f3Ocws9BHPtSFBvjI-X2guH6mrLsMnCiCu9PViT4ac0ld5C6EQZipw0lgvZKI0_Gp7fTT5nG-2qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کودک ۱۳ ساله در پی تیراندازی نیروهای مرزبانی به سوی یک خودروی خانوادگی در منطقه هو‌رامان استان کردستان جان خود را از دست داد. مقام‌های محلی اعلام کرده‌اند که این حادثه از سوی مراجع قضایی و نظامی در دست بررسی است.
تابناک خبر داد که این حادثه در منطقه مرزی «ته‌ته» هو‌رامان رخ داده است. اعضای یک خانواده پس از پایان کار روزانه در باغ خانوادگی، با یک دستگاه خودروی تویوتا در مسیر بازگشت به منزل خود در روستای «دره‌کی» از توابع شهرستان سروآباد بودند که نیروهای مرزبانی، به ظن آن‌که خودرو متعلق به قاچاقچیان است، به سوی آن تیراندازی کردند.
در جریان این تیراندازی، گلوله به کودک ۱۳ ساله‌ای که در قسمت بار خودرو حضور داشت اصابت کرد. او بر اثر شدت جراحات جان خود را از دست داد.
استاندار کردستان با تایید این حادثه اعلام کرده است که موضوع از طریق وزارت کشور، دادسرای نظامی و مراجع قضایی نیروهای مسلح در حال پیگیری است. او همچنین بر لزوم روشن شدن ابعاد حادثه، نحوه وقوع آن و اطلاع‌رسانی نتایج تحقیقات به افکار عمومی تأکید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76933" target="_blank">📅 17:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76929">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/psNXqiUTWRGhpi-0ShMqOzwxw9nqsMJbVGG0BxlLWDbKvBMbWeV1WsQsNjQH6tfS86SVHAlD-ygNIxQyrQgSCxTqsmkYqeV9CB8zh4a0eoqu5FsFgfU8kaGHtzDZBng93dVV0Odu0Yu-5QK6kM4Ql2qfDNH0laGlp6Rhhz_Z_0OieZI2M3iCdxO6xUY5hiNeK-I9AHes0d1ujFg1klXaCap9FGlJUxCcgKlb5tK-Ka9AGJ3UGMks7HJ6bAUg2EpUbQpb3pKpnyN6_n_uDQj1hROP2y8EN7udSHTtF4nM7OregekAO8ITAn0cer0C8pKC68AUeYVnYBcghT_KuvhohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HXoSlrdqlfqAxZTL-Jmls3Hr_IvoIQCgNoY8MQojZusscfeLmUJV1ohMPlFKWj9JIU5HfETaFBlzv9NFOYjckl58W3YgtLQnVb9Yi8B2ufpN9j_SRhmZgSoOQ5wfqI-enMo0ocVTC3RTrkd-awwjDikLu1TZWjo1mddXz-ZBVM2LiN1ZBmif_o7naKfz_h9_7jNcHn4denhbRlOTlt5mZy3Ah6povRx7ZwMzAN0wYejXyhVS0l_Z04o2llG-tfQSjOGBAwKWiZ6x5mV9QO11Kw17815iVtcVI5vGHhxLviuoR1ysAxOXT4UUlfdMJhZ5JI--abdUpAA-vLQCoYUJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hzVoJfJevMwm6m1aMbzeNm1yLtHxKzIdevvfCIK6Ca0dw230OwVOYnKOXUY9gCKZeLuSe5PSaHS1k44-W98mQRp89TIqqEnIZNw5kS_cpkHOpV2LLiPzBRk_QK2JqFFFF1AYZsODzrpQ6-i5VmvzTIuMKzEUaCw9xD-YUTRwH9y1PunX1L28OfhZ8ARYroRW9Xf4Xq8_D8qj8mnZkTiiciBwHEpTqhtFoWJvGwa_Wm-DxYSO1m63wrtU8QbpaoSU_XTxHT7VG4WJUo11tqYE3hcX20LGErJGYUL2sdezD-UUnRGWr0AXr_RBwFDqFcWaBowEjdEJfGIqx5zXvo3VFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=Rx1a_NKQPwmhKVAkxtW4vOPBryElZLk3qRkEHeudmfqlJLxyvpj78BcwWMPeZV5cxO-toMw3KtTwW3F_HYHNJG8BUsjDTAeX3-YzEfYR_wU_0v6BYuJMfA7O8l1_mHKfuvSmEmy8h0HLdXtS-AVObtK5F2wEH41h0DeW0MTMhcUDW4Ecq5Ww-7OJi7UPNAKJjwjAGGrqivgyZrO3_2Gmr19a8Ugydgxo7QanMJVEWNougH-3T9Z9khyg5dltYk866Kl5qZfXxt45Kb4px2NyGW8lV7uRj21uA4AbwiPQnOgjnSGQdCTiIBzwbU-a7m2lmo89e3RfVjHcpStKoWs_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2993ded2a7.mp4?token=Rx1a_NKQPwmhKVAkxtW4vOPBryElZLk3qRkEHeudmfqlJLxyvpj78BcwWMPeZV5cxO-toMw3KtTwW3F_HYHNJG8BUsjDTAeX3-YzEfYR_wU_0v6BYuJMfA7O8l1_mHKfuvSmEmy8h0HLdXtS-AVObtK5F2wEH41h0DeW0MTMhcUDW4Ecq5Ww-7OJi7UPNAKJjwjAGGrqivgyZrO3_2Gmr19a8Ugydgxo7QanMJVEWNougH-3T9Z9khyg5dltYk866Kl5qZfXxt45Kb4px2NyGW8lV7uRj21uA4AbwiPQnOgjnSGQdCTiIBzwbU-a7m2lmo89e3RfVjHcpStKoWs_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای انفجار حوالی پارچین، پاکدشت و قیامدشت در جنوب شرق تهران و دیده شدن دود
شنبه ۲۰ تیر
Vahid
خبرگزاری فارس:
فرماندار پاکدشت: صدای انفجار ناشی از امحای مهمات بود
صدای شنیده‌شده مربوط به عملیات کنترل‌شده امحای مهمات باقی‌مانده از جنگ بوده و هیچ‌گونه حادثه یا تهدیدی متوجه شهروندان نیست.
این عملیات با رعایت کامل ضوابط ایمنی و توسط نیروهای مسئول و متخصص انجام شده و از پیش برنامه‌ریزی شده بود.
پس چرا اعلام نشده بود؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/76929" target="_blank">📅 09:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H2lWzuyL3-PJtwUk2M28sXKXqbJcqArx5kRinaXIA44CMxkHdKegrs-GWcSZxebjm483XbmWYQk0zzT4wuVX5CctJ5X7Qqb2XKqUmlb081qgO2k1BK7Cjty0-54rbhk-fEcEuXUfiZk7_q90hpsHrL5HNHqcK9OT905vMxRuW3_TNJYFDs2Oojcwj8Ylzlz_FlDbbrOYyZgs57v_wVz4TjiCIeo145gEPHEAu5-foVp7gSPM4zB5zKEsN6lBoesSmCyD0GNhLeMGpjF0l_4P6TbODlz-6eb2fvoTNi_tR9vRJpVG-3bZZemhbSGMEuErbr7U1nnujRMtpTBrqTeFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار در پاکدشت پارچین
سلام وحید جان
پارچین همین الان صدای یه انفجار شدید ۹:۳۱
صدای وحشتناک قرچک. مغازه لرزید
کل قرچک صدا رو شنیدن
معلوم نیست هیچی
ساعت ۹:۳۰ صدای انفجار شدید سمت پارچین
دودش مشخصه
قیامدشت کلا لرزید
شهرک صنعتی خاوران
شیشه های مغازه لرزید ۹:۳۰
سلام ما خاور شهریم صدای انفجار شدید اومد شیشه ها لرزید
صدای انفجاری محیب از قیامدشت به گوش رسید
به حدی مهیب بود خونه لرزید
سمت شهرری هم لرزید حتی
درود ، عزیز پاکدشت صدای انفجار اومده دقیق ساعت 9:28
سلام ماهم صدای انفجار پاکدشتو حس کردیم از خواب پریدیم و ترسیدیم ولی یک انفجار بود
سلام اقا وحید ما تو قیامدشت چنان حس کردیم که انگار کارخونه خودمون منفجر شد
کل قیامدشت و چهلقز شیشه ها و خونه ها لرزید
سلام وحید جان ،پارچین انفجار شدید بود،ما قیامدشتیم،موجش تا اینجا اومد
سلام قرچک صدای انفجار اومد شیشها لرزید ولی دود دیده نمیشه
سلام ما محله ی ارکیده های پاکدشت زندگی می‌کنیم
و انقد انفجار شدید بود ساختمان ها لرزیدن
سلام پردیس  شنبه ۲۰ تیر حدود ساعت ۹،۳۰ یه صدای بلند اومد
ما پارچین هستیم همین الان صدای انفجار اومد تقریبا ده دقیقه قبل ،الان دودش هم میاد
وحید جان پارچین یه انفجار شد ستون دودش معلوم بود. پشت تپه های پارچین
تموم خونه ها شدید لرزیدن
سلام. نارمک ما صدارو شنیدیم تا قبل پیامها فکر کردیم توهم بوده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76928" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vB26bJ260Wd5AmFyZYGLKe_Fzqpe1QCUlP0PQyjL9xa18lRgeMGeHsU1c9QCX-E1mosU-NIV5UPD86RMELxYhOiTQ9uf_78K-Pz7awOWSe1G9EIKdf-7vM72UEP92C_WhVahGuv_pi046LOY8nQ_Zf8C4aWPpUdM6V3hLC6hhJBBKUZG1R9E4BA5vuAMR2U8jum_AF2FkATk3v68ps1eLL8peBTW3S1EQsQxUkfkuD2QplJQWLUUe-l1RuCm8Fe2RrXF2ICbudNd6fH65m5INcRLXb79XHu5EpBBOWFz9FtLN_hhocZnQBkLVO1LXRja_tuw-kFnTgJ2x_lOhQd6mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر تهران برای ترور من تلاش کند، هزاران موشک دیگر شلیک خواهند شد
ترجمه ماشین:
هزار موشک در حالت آماده شلیک قرار گرفته و جمهوری اسلامی ایران را هدف گرفته‌اند و در صورتی که دولت ایران تهدید خود را ــ که در بسیاری از نقاط جهان اعلام کرده ــ برای ترور یا تلاش برای ترور رئیس‌جمهور مستقر ایالات متحده آمریکا، که در این مورد شخص من هستم، عملی کند، بلافاصله هزاران موشک دیگر نیز به دنبال آن‌ها شلیک خواهند شد!
دستورها از پیش صادر شده‌اند و ارتش آمریکا آماده، مایل و قادر است برای مدت یک سال ــ که قابل تمدید است ــ تمام مناطق ایران را به‌طور کامل درهم بکوبد و نابود کند — ستایش از آنِ الله باد!
رئیس‌جمهور دونالد جی. ترامپ
1000 Missiles are Locked and Loaded and aimed at the Islamic Republic of Iran, with thousands of more to immediately follow, should the Iranian Government act on its threat, pronounced in many corners of the Globe, to assassinate, or attempt to assassinate, the sitting President of the United States of America, in this case, ME! Orders have already been given, and the U.S. Military is ready, willing, and able, for a one year period of time, subject to extension, to completely decimate and destroy all areas of Iran - PRAISE BE TO ALLAH! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76927" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XB-TUw9A-Cl6eH5NeO_nuHkC6DYg5aau7XJ8fGUs_3L_0EHX-mSmL0MlToHqfg4zOIP48Zi4RGe48SeCFPpWP3oYDKTkr-459OhVv7mpehcvbwBX29lp4Sy_oD_Rv0RlE58sKxer6zGx0uczMPVBk-RBP-iDQi1UyFkeiK3hTVZbDGhhfqPHeNIguzpXoLrorE_J_MKnA8s3j_W49W98xwKZ76FbW6I_OctSFqEFO49G11HIaWBSTTCHWJstvRnHmWIj3SmPElQvfhfdJcczEBu8WOcpiBikOJpSzumQ3qgsQLGBY9J5dVez1p5WZTVaRNZKEVpfGvt36IeD6-sxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «سی‌بی‌اس نیوز»، مقامات ارشد آمریکایی روز جمعه فاش کردند که مقامات ایران در پیامی محرمانه به مشاوران دونالد ترامپ اعتراف کرده‌اند که شلیک به کشتی‌های تجاری در تنگه هرمز یک «اشتباه» بوده و این حملات توسط یک جریان «خودسر» از تندروها با هدف تخریب مذاکرات انجام شده است.
با این حال، کاخ سفید این اقدام را نقض صریح آتش‌بس دانسته و خواستار اعتراف علنی تهران به این اشتباه شده است.
براساس این گزارش، تیمی ارشد از سوی ترامپ، شامل جی‌دی ونس، معاون رئیس‌جمهوری، جارد کوشنر، داماد ترامپ، استیو ویتکاف، فرستاده ویژه کاخ سفید و مارکو روبیو، وزیر خارجه، مامور شده‌اند تا گفتگوها را روز شنبه در عمان ادامه دهند. در حالی که واشنگتن انتظار دارد ایران پس از این نشست تعهد خود را به باز بودن کامل تنگه اعلام کند، مقامات آمریکایی هشدار داده‌اند که اگر ایران نتواند به این ساده‌ترین بخش توافق پایبند بماند، امیدی به حل مسائل پیچیده‌تر نظیر تسلیم ذخایر اورانیوم غنی‌شده نخواهد بود و در صورت ادامه اقدامات خصمانه، با پاسخ سخت نظامی و اقتصادی مواجه خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76926" target="_blank">📅 09:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OGdhxaYVIRMCxHzwY15G6M83JoZmT37_TasfqayVBF_MzCL-zdv2bk6d_wkYwZysK_NN6a7MuweUy_RhoJjDDycYbL8j8OOd6xGymz41rcnrwfTNtgQhquHu2zkiQIxMtnKCzQkF9X1BiwZGlnMgjQ14196OjBGTYMiNmKkTMifOmUlfwFRFqOYzjwGyeNwH3vOzM5VxEKfw9AuAYF5LzDUWm7NsQ-Tl5M5GSwhzt3mMRceBW-2XSg2Fzy4h_yTDtoTbgK3xOAFrl1ro-6LOqEJ2HtJuFhdUDQ4MbO8LT7ELD5-h7ara45QGAxjTnaDEUO3PivG1CewkZpOYDe26_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از ایران خواسته است ظرف ۲۴ ساعت علناً متعهد شود که شلیک به سوی شناورها در تنگه هرمز را متوقف خواهد کرد
اکسیوس (ترجمه ماشین):
سه مقام ارشد آمریکایی روز جمعه در جلسه‌ای توجیهی با خبرنگاران گفتند ایالات متحده، هم به‌طور مستقیم و هم از طریق میانجی‌های منطقه‌ای، از ایران خواسته است امروز، شنبه، بیانیه‌ای علنی منتشر کند که در آن روشن شود تنگه هرمز باز است و ایران متعهد شود به سوی کشتی‌های تجاری عبوری از این منطقه شلیک نکند.
چرا اهمیت دارد:
ایران با چندین بار شلیک به سوی کشتی‌های تجاری در تنگه هرمز، یادداشت تفاهمی را که سه هفته پیش با ایالات متحده امضا کرده بود، نقض کرد.
این اقدام به چند دور تبادل آتش انجامید و توافق را در معرض فروپاشی قرار داد.
مقامات آمریکایی می‌گویند اگر ایران به چنین تعهد روشن و صریحی پایبند نباشد، این موضوع تردیدهای جدی درباره اجرای یک توافق هسته‌ای ایجاد می‌کند؛ توافقی که بسیار پیچیده‌تر و حساس‌تر است.
محور خبر:
قرار است عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، روز شنبه در مسقط دیدار کنند تا درباره وضعیت تنگه هرمز گفت‌وگو کنند.
عمان در هفته‌های اخیر، حتی پیش از امضای یادداشت تفاهم، با ایالات متحده و متحدانش در خلیج فارس همسو شد و یک مسیر کشتیرانی جنوبی در نزدیکی سواحل خود گشود که کشتی‌ها می‌توانند از طریق آن از تنگه عبور کنند.
ایرانی‌ها که معتقد بودند این اقدام اهرم فشارشان در مذاکرات با ایالات متحده را تضعیف کرده است، خشمگین شدند.
مقامات آمریکایی می‌گویند اعضای تیم مذاکره‌کننده ایران به آن‌ها گفته‌اند عناصر تندرو در داخل حکومت تصمیم گرفتند برای بازگرداندن این اهرم فشار، شلیک به سوی کشتی‌ها را آغاز کنند.
در مواضع علنی، تیم مذاکره‌کننده ایران، فرماندهان سپاه پاسداران انقلاب اسلامی و دیگر مقامات ارشد، همگی موضع واحدی دارند و خواستار کنترل ایران بر تنگه در آینده هستند.
پشت پرده:
یک مقام ارشد آمریکایی مدعی شد که پس از دو روز درگیری در اطراف تنگه در اوایل این هفته، ایرانی‌ها «دوباره به سراغ ما آمدند و خواستار گفت‌وگوهای بیشتری شدند تا برای حل برخی مسائل تلاش کنند.»
این مقام آمریکایی گفت: «آن‌ها به ما گفتند: “گند زدیم. اشتباه کردیم. بیایید به گفت‌وگو ادامه دهیم.”»
به گفته او، در داخل حکومت ایران بر سر اجرای یادداشت تفاهم و مرحله بعدی مذاکرات با دولت ترامپ، جنگ قدرتی در جریان است.
یکی از مقامات ارشد آمریکایی گفت: «افرادی در داخل نظام آن‌ها هستند که می‌خواهند به توافق برسند، اما ما نمی‌توانیم به‌جای آن‌ها تصمیم بگیریم. خودشان باید اوضاع را تحت کنترل بگیرند.»
چه می‌گویند:
مقامات آمریکایی گفتند انتظار دارند ایرانی‌ها پس از نشست روز شنبه در عمان بیانیه‌ای منتشر کنند.
یکی از مقامات ارشد آمریکایی گفت: «ما می‌خواهیم آن‌ها علناً بگویند که شلیک به سوی کشتی‌ها را متوقف خواهند کرد و به‌صراحت یا دست‌کم به‌طور ضمنی بپذیرند که گند زده‌اند.
در حال حاضر روی همین موضوع کار می‌کنیم. انتظار داریم ایرانی‌ها بگویند همه مسیرهای کشتیرانی در تنگه باز خواهند بود و هیچ عوارض عبوری دریافت نخواهد شد.»
یک مقام ارشد آمریکایی دیگر گفت اگر ایرانی‌ها از انجام این کار خودداری کنند، پیامدهای سنگینی در انتظارشان خواهد بود. او گفت: «اگر فردا موضع آن‌ها این نباشد، روز خوبی برایشان نخواهد بود.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/76925" target="_blank">📅 00:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76924">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IwlKnTZn7WGd0CeRNeCZcv0Fuve5UfUUwTZkZzmbWhs1NuffKZkFioOONtNP-eeY2wHplBO7H95tI8b5ZpZ8mM0Rr_kfA0cOqclU5AoRJ-B8fvHTOD26yQ80ohmDX4iAa0ftUtk7vBP50RGCFAlYusiwK7djQAwbiQgQyP6Dx-Irpp9v8LqaLDWluNQgCc7_PNCcCxtEKgu4a2r5zoAu1bAL0_X-SsrlCLIDM9S4RKj9AvTZX907v5wM-GEm8PoTw6O5pYMWlCc1XHTtsitvKa-xjhtiQWujDMOAA4czK8InAdn3X_aATfjdaVeG59S15ruTXaBwSDq9J-cWubiXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا در اقدامی که از بی‌اثر شدن تفاهم اخیر میان تهران و واشینگتن حکایت دارد، تحریم‌های تازه‌ای علیه جمهوری اسلامی و شبکه مالی آن وضع کرد. در فهرست تحریم‌های جدید نام علی انصاری، از چهره‌های نزدیک به مجتبی خامنه‌ای و متهم به فساد اقتصادی، دیده می‌شود.
وزارت خزانه‌داری آمریکا جمعه ۱۹ تیر اعلام کرد این تحریم‌ها در واکنش به حملات جمهوری اسلامی به کشتی‌های تجاری در تنگه هرمز اعمال شده است.
این وزارتخانه علی انصاری را «تسهیل‌گر مالی» جمهوری اسلامی معرفی کرد و نوشت او بر شبکه‌ای گسترده از دارایی‌های جهانی به سود مجتبی خامنه‌ای و دیگر مقام‌های حکومت نظارت دارد.
بر اساس بیانیه وزارت خزانه‌داری، انصاری با نهادینه کردن اختلاس در ساختار جمهوری اسلامی و انتقال ثروت‌های عمومی به مجموعه‌ای از املاک و دارایی‌های تجاری در خارج از کشور، خود، مقام‌های حکومت و مسئولان ارشد دفتر رهبر جمهوری اسلامی و سپاه پاسداران را ثروتمند کرده است.
وزارت خزانه‌داری آمریکا همچنین شماری از صرافی‌های کلیدی وابسته به حکومت ایران را تحریم کرد؛ نهادهایی که سالانه میلیاردها دلار را به نمایندگی از بانک‌های تحریم‌شده ایران جابه‌جا می‌کنند و با استفاده از شبکه‌ای از شرکت‌های پوششی، فعالیت‌های مالی حکومت را پنهان می‌سازند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از وضع تحریم‌های جدید گفت مجتبی خامنه‌ای «در حالی در انزوا پنهان شده که حکومتش در حال فروپاشی است».
او ادامه داد: «وزارت خزانه‌داری همچنان از همه ابزارهای خود برای جدا کردن او و دیگر مقام‌های ارشد حکومت از نظام مالی جهانی بهره خواهد گرفت. ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/76924" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=mnva2QJeX88lLVMZ-vIxvZsxG_5sGtyhp4DcfP6ybVcwp2xtsXtDzGSlPDzjWy-aN8RGpj0YXTImpyliOGOOcpYbgv2aHNVdCsvROczGv29rde02Hfwc1Rqi05ohKxANJEjOo5lVZ2XuIh8kfZgAClbsru9GVJEBnGFIBtP6oq0EuKj4sqyWFhhaAeu9mGsTENwdNvWPsvFIk5H5Olrt2bja-M0uqki1ZS05IIAjkRmCp0JJFYXGm8WEXcB-R0eOg6EzF-_vNEQ1MqVHLqQP7hyuhIHdsgacIbo14n9qpD9mzjASqsQK61mAqS67YPXXW1pPR84ks0-_5zfEsyAWhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb410e1088.mp4?token=mnva2QJeX88lLVMZ-vIxvZsxG_5sGtyhp4DcfP6ybVcwp2xtsXtDzGSlPDzjWy-aN8RGpj0YXTImpyliOGOOcpYbgv2aHNVdCsvROczGv29rde02Hfwc1Rqi05ohKxANJEjOo5lVZ2XuIh8kfZgAClbsru9GVJEBnGFIBtP6oq0EuKj4sqyWFhhaAeu9mGsTENwdNvWPsvFIk5H5Olrt2bja-M0uqki1ZS05IIAjkRmCp0JJFYXGm8WEXcB-R0eOg6EzF-_vNEQ1MqVHLqQP7hyuhIHdsgacIbo14n9qpD9mzjASqsQK61mAqS67YPXXW1pPR84ks0-_5zfEsyAWhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رسانه‌های دولتی چین، ‌این کشور برای نخستین بار با موفقیت یک موشک با قابلیت استفاده مجدد را فرود آورد که این امر پیشرفت بزرگی برای برنامه فضایی این کشور محسوب می‌شود.
پیش از این، قابلیت استفاده مجدد موشک‌ها در انحصار شرکت‌های اسپیس‌ایکس ایلان ماسک و بلو اوریجین، متعلق به جف بزوس، بنیانگذار آمازون بود. حالا چین با انجام این آزمایش موفقیت‌آمیز می‌تواند برتری آمریکا در زمینه موشک‌های قابل استفاده مجدد را به چالش بکشد.
شرکت فضایی اسپیس ایکس در دسامبر ۲۰۱۵، برای نخستین بار یک موشک فالکون ۹ قابل استفاده مجدد را فرود آورد و پس از آن در نوامبر ۲۰۲۵، موشک نیو گلن شرکت بلو اوریجین به زمین نشست.
فالکون ۹ حالا حدود ۱۵۰ بار در سال با پیشرانه‌هایی پرتاب می‌شود که قابلیت ده‌ها بار استفاده مجدد را دارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76923" target="_blank">📅 21:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76921">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ShSyrbSkRL0IQZOdUyH949V2skN0eOtSFEEAkRpSPWQZf7LevPIC5gC89Ge0yCQ5sQ-zdBGZmhHN6aUOZBF7DGPseuWPlLHTtSbZIWJMwKyHYA6E8KoM92RFkHGrjkMHIKStO-Ql793u2fO1owuT1goGj3cZVcICSKKKK6PMSR8RXVjFonDQFw2wg1oAJwNECN8tmCEOO-07Ib89hPuoU4duRBb18YtqQ8XFNT4VL75OtJhYuLexKj01xWOBJVLdfK9JLcsE3STIZEajiNgMLwEhQPQb_06GKbNve8MxErmOwrIECWvwoKaDpl2kpWSiGINFmBTUxyM4KmXYgW8-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=pXuacsoYnkJTO-VhH3VVizBu41yNiBawrz5-agA8KVVInn2DMCyxtM__ZpoJCV6dJ0cWU24QPSj57fN7L2WLeAq3e8JxCIQgYbO0A8h3K4tfCRgUforu3-p6I-kXF-YKinyofSj04uRTQbvcXydpzifYxx5Sul6MtNg7U26hSOdpVD-KYYCd6IU5UF_rQ1fhom04Tkkp867Bq2raVNFndU7Kk31mB4H87SYOdiq-8zkfRFvhvniilUPYO8xpmqRC14qxHtwbDorS1yG8WojllrrpQUoBMFxVSEvViUNJnLU7XXvF9CWhSaz7AQFIVyyRT740KHU6jU_gDGQ0J0WRfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf31c0a00e.mp4?token=pXuacsoYnkJTO-VhH3VVizBu41yNiBawrz5-agA8KVVInn2DMCyxtM__ZpoJCV6dJ0cWU24QPSj57fN7L2WLeAq3e8JxCIQgYbO0A8h3K4tfCRgUforu3-p6I-kXF-YKinyofSj04uRTQbvcXydpzifYxx5Sul6MtNg7U26hSOdpVD-KYYCd6IU5UF_rQ1fhom04Tkkp867Bq2raVNFndU7Kk31mB4H87SYOdiq-8zkfRFvhvniilUPYO8xpmqRC14qxHtwbDorS1yG8WojllrrpQUoBMFxVSEvViUNJnLU7XXvF9CWhSaz7AQFIVyyRT740KHU6jU_gDGQ0J0WRfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخواست افتخاری برای حذف صدای خود از آلبوم "بدرقه" [بدرقه خامنه‌ای]
علیرضا افتخاری با انتشار ویدئویی علت این درخواست را ضعف فنی اثر عنوان کرد.
این آلبوم با صدای هفت خواننده از جمله محمد معتمدی، پرواز همای و ... به مناسبت تشییع پیکر رهبر جمهوری اسلامی ایران، توسط شهرداری تهران منتشر شده است.
Koronmusic
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76921" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76920">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=JE080tFQCzujCfdYukHENy6Qqbl0U1rCTYa8efLso2l6MyW9xCimard_phjePvbY34q5tzmCLvqe_k4Jcou-BXlTNLBnZHDkyji25lJBaqQRTIoxCqUCLamPqzO49Q7V9Ci_xVg49rDkO7gs3Qj95oSJAGyLSxCkIFPJwqxLuVXRNsjDWK5NjkEk2jj51drKbvfOFmHmF6QtgxyYixQpUaU3AYrhUj_duSaMqKbaSN7fVGD0bdNs3uuv6ULG96hGHCnpHnpkPvTDUly8dECMEQTdLipoKZP0imFzW-ZL_dkRVFWHhiLGQ-W0qpuizB9kuUrxyt3Mp6Ta1F5iCOeOqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e9af1050e.mp4?token=JE080tFQCzujCfdYukHENy6Qqbl0U1rCTYa8efLso2l6MyW9xCimard_phjePvbY34q5tzmCLvqe_k4Jcou-BXlTNLBnZHDkyji25lJBaqQRTIoxCqUCLamPqzO49Q7V9Ci_xVg49rDkO7gs3Qj95oSJAGyLSxCkIFPJwqxLuVXRNsjDWK5NjkEk2jj51drKbvfOFmHmF6QtgxyYixQpUaU3AYrhUj_duSaMqKbaSN7fVGD0bdNs3uuv6ULG96hGHCnpHnpkPvTDUly8dECMEQTdLipoKZP0imFzW-ZL_dkRVFWHhiLGQ-W0qpuizB9kuUrxyt3Mp6Ta1F5iCOeOqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">PapiTrumpo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76920" target="_blank">📅 19:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76919">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pFVOj-qUO5BaMhOsRAboopsQzeCNTDwvyNk1smmWBa0DwgLfJWH7JnAFHn74n8cY06JhiHyta2LOFfncg0k9wSbzplyaHe-Y90tPypEUJNe-_z4SsYwlezeqerZg_giZ62OhSGl50kn8xcvfbvtrbgvJQq6odL3mO2NpBLlNXue3X05HcZg_JVVzkGygtIOxf3s0j0_OG9jrG9qC0P77IXQKKgf3YhMponqqkXLz0Ctli3cDsYXNvnLI3k1zQH0eM0xLmQMWj-nqC0_hOzaIbWPot4auLTYCPUUvUIoxf5J6RrCFPpa8oByiO9NUEu8OOTysz9cWdk2FptYpdDc9iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع آگاه نوشت که دور جدیدی از مذاکرات میان واشینگتن و تهران، احتمالا هفته آینده و شاید در سوئیس برگزار شود.
مقام‌های جمهوری اسلامی تاکنون در این خصوص اظهار نظری نکرده‌اند.
همزمان دونالد ترامپ، رییس‌جمهوری ایالات متحده، در تروث سوشال نوشت که با درخواست تهران برای ادامه مذاکره موافقت کرده اما به آن‌ها گفته آتش‌بس پایان یافته است.
@
VahidOOnLine
خبرگزاری فارس:
درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76919" target="_blank">📅 19:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By0fZ-xEduRdPE_c53aC7HhbBoNPwIv75qffre-ssxcKMKYNnjiTvAUQ4xmm2P1WFRymHhIpPNYSl_l0DeOZD54WxNUVoOYq-q8VUvUvqAIgtTubDbLWtFncfLaOBo7m6Q9n0C4a466IUCkZt8o_XcFM5NNO4G3B6JCWoD-c-DTTTIThQIuTxFbXxGKiiE9l0NEPb2qspj4TRzi6InHdq9Ht7oM664zGLa9a4VJkeKdehn66GEmc5mqsmXMb595fS5lLakwojN9flafBEWJxj40kPn0zOAhfcDxXBeLRS8TKs75zKWkRmhde79ZtFr8Wr3zQ2wsltopUkjsbnrV_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگویی با «نیویورک‌پست» اعلام کرد که دستورات لازم را برای واکنش به هرگونه تلاش احتمالی ایران برای ترور خود صادر کرده و در صورت وقوع چنین حادثه‌ای، ایران با پاسخی ویرانگر و بی‌سابقه مواجه خواهد شد.
ترامپ اظهار داشت که مدت‌هاست در فهرست ترور تهران قرار دارد و به همین دلیل دستور داده است که اگر اتفاقی برای او بیفتد، ایالات متحده باید ایران را «به سطحی بمباران کند که هرگز پیش از آن ندیده‌اند».
او در پاسخ به گزارش‌های اخیر مبنی بر هشدار اسرائیل درباره طرح ترور جدید، با رد وجود طرحی تازه تاکید کرد که ایران سال‌هاست به دنبال حذف او بوده است. ترامپ گفت: «من از مدت‌ها قبل در صدر فهرست ترور آن‌ها بوده‌ام؛ زندگی همین است. امیدوارم دلتان برایم تنگ شود!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76918" target="_blank">📅 19:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnBP8260NIYsPvXPddiTKfl8BL2z1sBLbScDtgxZ_GwblBXs_JLV7AGVeFZldlfG1kmCxqDRA_KSyFlgTPrBLjqa9sBj7ABZAbhVIfuSwHx7YgwKu6bFeKpRWcomssESVYKAzXTjaXm4dcYxFKpqc-LBHy2qLqHgl_ehZhPAib0FWCCsfMdgjl0KCb8zduMOFP9_RqgwMZU2xMdEqtz-nxuPGBwqASnVrCiZpQtZBfqRTyFYeKO9OcjvKNrmPH9iB7vRF0nlRTMWocBjjThn9spH60o9uJLO-aoYL_YhPhQJw6R2dY2eUD7e2KlYI_o0NUTNDSb4fmHkgcr5gOqkHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امام جمعه اهواز گفت: فریاد ملت ایران انتقام است و از هرکسی که موشک و پهپاد دارد می‌خواهیم که زمین را از لوث وجود ترامپ پاک کند.
احمدرضا حاجتی  در خطبه‌های نماز جمعه گفت: سایه حکمرانی رهبر شهید همواره هست و آن مشت گره کرده او بر سر آمریکا فرود خواهد آمد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76917" target="_blank">📅 18:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nf_vZSFCW62q4rB6xx1-GSydPjsI013WWCek8IlVnPqK4eqRg0itq-EMbsUP6VzA3uQJrBSFSP22GEyrjvOzQas_ysrmI_ZqOxj0v0Y8ej82viNE3yvcp140vW3p2EgQJdpiG0Em-LE6TK00SAfmCOhDMvW5FXLrPisul-YATB8P-o98adaQ02DjnRcFvq7b26yV3c3nTcGyztILoRNhfD1CXIFU3Y4AALsgPUsVmk0_KGNc42p46m4SggQ0_nHPSX1dvoWu3KaZJgAPyy2NFP9TwmcR8jYN55PtzyMyU32UrDDjgE_20ayZXx2cVCRJG4Fu2UYYTKWnII3D55r4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره زیر خاک رفت</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76916" target="_blank">📅 18:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76915">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qJkYOtztdGEOGT8Wi5dX7dkGqMhX9whXQTDmExT0iDs4MTWcUGQFC5gL8PFsrstqcKZUn0GuPBjbRMvpzWt4H-8bEsEibcbYkTiWacfKpM56UbnWooYvPpDi4A0xF0UiBq6J3pocNiurJGRSlAraen_nG8o1P8D3gt3zW0q8kxIQ6WUk63EsunEScFXp3LZBfntItLx5B6Uilk9yoV3kvFJn5rUIba7TXyT1HMMMkXP6_t4ekKy5bu4RcwqaF7KxnJJ0dRGkey4AtXFzyHl30GqbEKIGpEdnHopaDhkyI90Zr_axJrimEcB1zMrH2FaDz4l0vX4esrhc8lPfr1zkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران از ما خواسته است که «مذاکرات» را ادامه دهیم.
ما با این درخواست موافقت کرده‌ایم، اما ایالات متحده به‌صراحت و بدون هیچ ابهامی به آنها اعلام کرده است که آتش‌بس تمام شده است!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76915" target="_blank">📅 18:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jgSvBXrk4NJGnEeKKD45C-qwH9RjwWOGuxArm3LK92SqQsZ7U6KynGkUL9J-G53_IRY12vV9m0jDo7UjHCZiu-uiIDXoNIYK1LMkn9Dr0RCm9mtAEJyvamupHrBqYw_q6nGz7fBZ5R-m_ixpQvWxCNsbiQUGmp5_b62VlRCa13elnPcIKBR7HQ_R_t6DNhzQ-YDw_Hh41uVISzUassIt_s8Ga0_Tr82NBvlehRneObZzDVCqMjCbmQy7jSvROPknHEyZyaJXvAHGFbWYcTAYYLqJ2qLdK6XbqclHGXETpWKH6Pr06FbgYjImp5OTQ42vuDRNpqzWgF8p2SmC6fP0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت اکسیوس می‌گوید قطر، پاکستان و چند میانجی منطقه‌ای دیگر از جمله ترکیه، مصر و عربستان سعودی در تلاشند تنش میان آمریکا و ایران را کاهش دهند و مذاکرات هسته‌ای را از فروپاشی نجات دهند.
بر اساس این گزارش، با وجود آن‌که دونالد ترامپ روز ۱۷ تیرماه تفاهم‌نامه و آتش‌بس با ایران را «پایان‌یافته» اعلام کرد و دستور حملات هوایی داد، دولت او همچنان خواهان بازگشایی تنگهٔ هرمز و پرهیز از بازگشت به جنگ تمام‌عیار است.
یک منبع منطقه‌ای گفته میانجی‌ها معتقدند حملات اخیر ایران در تنگهٔ هرمز احتمالاً از سوی عناصری در داخل حکومت ایران انجام شده که با تفاهم‌نامه مخالفند و قصد تضعیف آن را دارند.
اکسیوس می‌نویسد مقام‌های میانجی روز چهارشنبه تماس‌های متعددی با مقام‌های آمریکایی و ایرانی داشته‌اند تا ابتدا بر سر کاهش تنش توافق شود و سپس تاریخی برای دور تازه مذاکرات فنی تعیین شود.
یک مقام آمریکایی نیز پس از نشست ترامپ با تیم امنیت ملی خود گفت دولت آمریکا همچنان به یافتن راه‌حل متعهد است و گفت‌وگوهای فنی برای رسیدن به توافق هسته‌ای ادامه دارد، هرچند واشینگتن حملات ایران به کشتی‌ها را «اقدامات تروریستی» و نقض عملکرد مورد انتظار در تفاهم‌نامه می‌داند.
@
VahidHeadline
خبرگزاری رویترز روز جمعه ۱۹ تیر به نقل از یک منبع آگاه اعلام کرد مذاکره‌کنندگان قطری برای دیدار با مقام‌های جمهوری اسلامی و با هدف کاهش تنش‌ها و فراهم کردن شرایط برای ادامه مذاکرات گسترده‌تر، در ایران به سر می‌برند.
بر اساس این گزارش، گفت‌وگو بین دوحه و تهران «با هماهنگی ایالات متحده» در حال انجام است.
این منبع گفت که هدف این مذاکرات، رسیدگی به اجرای تفاهم‌نامه میان آمریکا و ایران و همچنین موضوعاتی است که موجب تشدید اخیر تنش‌ها میان واشینگتن و تهران شده‌اند؛ از جمله اختلاف‌ها بر سر کشتیرانی در تنگه هرمز.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76914" target="_blank">📅 17:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kj3OT8MBMSuquz-B7F3X-DZvNb_HPQNe9qrHhW8pkMgjzlbyslDKnOaoJuFMGbO39hBY4LoW_qob2ghyiY3mI4-f0_mJz0igc5NBFIf3FQMfrUsz3zuA-MWUBNDg5oForWL-RVIDJZf5VnY8AXVu9ddPqvutsUYWj9x3eEQcMR94B6j4SEVLfxVbOHA313N1CIXezl0-ODXU22Vhh3li1LAWl2PPtEerqIfM9eAO0j5N5b6Cf5dkqGtcEWjRbUoBPo5w6KSH0iajHq-bx6CE7r-K1OvfTYRnVK2rTvB6i3bia_26nXzGQzEcz4eCtyS5hiAK4UKolL1EW_EXLNfT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KEZskgPn-xXrVMDJbJZ5IaCfI78rYzpvgz32MRCB_y4-m7Cyr6YCLShMEovvj12E80_DFlQ3hnDbzHXlT-ciFndXfnZiC3fPfczu6FdKTMkqpkI946B26nlbyaY3Lc-BelPZZISHfKOvZeJ7CPncF626YmiJ-VQs3bHUTApdg-mRGABtFqh_PlWCLsdZ08jkHPYzqtyjEC347D48LeMv2GCF2k4OEZU48MRGqaE350EZ78DQ7Ao7l35ylFfFAmaImnwBBS3zJggr7_0JrVcg1ac8pRCxkeN0uHDT9I0SClyGmW39dMwjlDSUiA2MXAJLYsLEYHsxj2vj0VuG6wRZpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش منابع حقوق بشری، نیروهای مرزبانی جمهوری اسلامی ایران با شلیک مستقیم به خودروی یک خانواده در روستای درکی از توابع شهرستان سروآباد، یک کودک ۱۵ ساله را کشتند و پدر او را به شدت مجروح کردند.
به گزارش هه‌نگاو، غروب پنج‌شنبه ۱۸ تیر ۱۴۰۵ (۹ ژوئیه ۲۰۲۶)، نیروهای هنگ مرزی مستقر در روستای درکی، بدون هیچ‌گونه اخطار قبلی، خودروی شخصی یک خانواده اهل این روستا را که پس از پایان کار روزانه در باغ گیلاس خود در حال بازگشت به محل سکونتشان بودند، هدف شلیک مستقیم قرار دادند.
هه‌نگاو گزارش داد که در نتیجه این تیراندازی، سام حسنی، کودک ۱۵ ساله، بر اثر اصابت گلوله به سر در دم جان باخت و پدرش، احسن حسنی، از ناحیه ران به شدت مجروح شد. به گفته این نهاد، پیکر سام حسنی به سردخانه بیمارستان بوعلی مریوان منتقل شده و احسن حسنی نیز در همین بیمارستان تحت درمان است.
شبکه حقوق بشر کردستان نیز با تأیید این رویداد از تشدید فضای امنیتی در مناطق مرزی مریوان، پاوه، بانه و سردشت خبر داده و به نقل از منابع محلی نوشته است که نیروهای مرزبانی و سپاه پاسداران در برخی از این مناطق، ضمن افزایش حضور نظامی، محدودیت‌های بیشتری بر رفت‌وآمد روستاییان اعمال کرده و در مواردی از دسترسی ساکنان به باغ‌ها و مراتع شخصی‌شان جلوگیری کرده‌اند.
تیراندازی نیروهای نظامی جمهوری اسلامی به سوی غیرنظامیان، در سال‌های اخیر بارها به کشته و زخمی شدن شهروندان، از جمله کودکان، منجر شده است. کیان پیرفلک، کودک ۹ ساله اهل ایذه، در حالی که شامگاه ۲۵ آبان ۱۴۰۱ همراه با خانواده‌اش در ماشین در حال گذر از خیابانی در این شهر استان خوزستان بود، هدف شلیک نیروهای جمهوری اسلامی قرار گرفت و کشته شد. در این واقعه پدر او میثم پیرفلک نیز به‌شدت زخمی شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76912" target="_blank">📅 17:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FxWT_7bEv70et9_Osa1T3tLB-OmnGDteYL-NZYoKlfsBb56Pzdy8tn0TX4AW8ushtL3ffd0J1waRr0toLo_GQSg_IU3ZIMCzq37j8LMVdNjC-wJHAnjSvw8U1DbvYp9sL0bzRGhH30i6ymou2H3fPVrPd_bGk59kpMzzxjXWvPyYZ1pZ7PLp1i5Hzssbx1mzaehxteZCLcZ44RbGDPEOQv3DTq9X3LXfaG4JqISFD6lFztiEfXpilPkY9ygP_UorYFMKO7P3k82ow1FoK7J5CUXjqKXMg1ZNqoCgFG4pRXtk7jiRaKt49nSTTYMX7OrPxfb5jWmhwK_HyAzxyCvVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از دو منبع آگاه گزارش داد اسرائیل این هفته اطلاعاتی را در اختیار آمریکا قرار داده که نشان می‌دهد جمهوری اسلامی به‌تازگی طرح مشخصی برای ترور دونالد ترامپ تهیه کرده است؛ گزارشی که هم‌زمان با تشدید تنش‌ها میان تهران و واشینگتن منتشر شده است.
به گزارش سی‌ان‌ان، یکی از منابع آگاه گفته است هشدار اسرائیل در هفته جاری به مقام‌های آمریکایی منتقل شده است. منبع دیگری نیز گفته نهادهای اطلاعاتی آمریکا در هفته‌های اخیر به‌طور مداوم اطلاعاتی درباره احتمال تلاش برای ترور ترامپ دریافت کرده بودند، اما اطلاعات ارائه‌شده از سوی اسرائیل جدید بوده و به یک طرح مشخص مربوط می‌شده است.
سی‌ان‌ان نوشت جزئیات این طرح هنوز روشن نیست و همچنین مشخص نشده که آیا دستگاه‌های اطلاعاتی آمریکا نیز به‌طور مستقل این طرح را شناسایی کرده بودند یا تنها از طریق هشدار اسرائیل از آن مطلع شده‌اند.
کاخ سفید در پاسخ به درخواست این شبکه برای اظهار نظر درباره این گزارش، که نخستین بار روزنامه وال‌استریت ژورنال منتشر کرده بود، به اظهارات اخیر دونالد ترامپ اشاره کرد.
ترامپ روز چهارشنبه ۱۷ تیر به خبرنگاران گفت: «آنها می‌خواهند رهبر آمریکا، یعنی من، را از میان بردارند. من در همه فهرست‌های آنها هستم. امروز صبح دیدم که در تک‌تک فهرست‌هایشان قرار دارم. تا اینجا کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد. اینها آدم‌های شرور و بیماری هستند و باید این سرطان را ریشه‌کن کنیم. سرطان را باید از همان ابتدا از بدن خارج کرد.»
سی‌ان‌ان همچنین گزارش داد تنش‌ها میان آمریکا و جمهوری اسلامی در روزهای اخیر، هم‌زمان با فروپاشی آتش‌بس ۶۰ روزه، افزایش یافته و دو طرف تهدیدها و حملات متقابلی را علیه یکدیگر انجام داده‌اند. با این حال، به گفته یک مقام آمریکایی، تلاش‌های دیپلماتیک همچنان پشت پرده ادامه دارد.
به گفته چند مقام آمریکایی، برای انجام حملات احتمالی در شامگاه پنج‌شنبه آماده‌سازی‌هایی انجام شده بود، اما مقام‌های آمریکایی در نهایت ترجیح دادند فعلاً به جای اقدام نظامی، مسیر دیپلماسی را دنبال کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 495K · <a href="https://t.me/VahidOnline/76911" target="_blank">📅 02:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCgJqubr0rxHsB6iGPAQDF_xn6Ilxk2hFjki0SLoFbPS_KdaOQ8j1gzUAFfuljFWL2_mHVXAxiBn0PEgkY4NwBO2HctUE3CK8gJrN0RohCeDXWGR0_c8PWwGvryCD8u32TSpaATWRnPtbRqVHTXGZ38DtavIw5fftqyssD7T18APystTT7VBVryCEckLKXd9i740E28eF7PONf7IwS4t-fN9oVVDLEh63-tTQZEt5Ckog0fy1m9q3XJEibBm_KbbOx2GNTiC7zmBoXsqghY-771HheXbahXbFBoxjcGFwz-yp03Dwrw1GZ1x9VtmlBypxUNMaIO2zjSVB-rjuoqwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی،  پس از ۱۳۱ روز بالاخره در بامداد جمعه ۱۹ تیر در حرم امام هشتم شیعیان دفن شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 489K · <a href="https://t.me/VahidOnline/76910" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bdeuJFPsFDEJcOCJY47gusH0kQfJWPDbQPlBd5VLpPd5OYznH3lwUAWD_ndgGfYSvFwBGeq_CSPnVbk57e44XHzQp3gCfG2vzCkLzCl_JVrPreF4W_e_dRPBzz-a3tw30gtQ-2q0HwvjfaCKiS835PjG_u1RpNq9MaVWUO4_vCuIqNNbcZ6Cl1GYtCdUJFbjs8mCX_lJXGYWRi9gtS_3FP6Oez4eH6MXG1wd-MX-B38ZBZseE6GF2QeQXDe6zREFr9l9ZwY12HYaGERtx09Ga7EOXNjp1cdU5mDir6-P-BUsC71HCWDtDCW-S3DqegVik6P0aYisn6R6ezLDeWxoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KsdU5RLdc2qdIISP4GkLJ_8k_vKXWDyN8oVGoVLkgi9R9d17frpfRLI4GfvCy3FLUDbwXMjqwsW0vNuMLNX-vpgZKvU7z1pwK_aZCf4Ux-oJTHnWcFK0NWv-tjPSxLsx65WiG_ZcySJoR-y014yiqtbf9_vwbevPtLXoxaksGQAc8LESbwa8pQxtTNkO5qiiZO6zA6GZyzlyya4G9t7G_Ql9fSCXoOCRHc0z60Zf9TXDhGAosAAkSxJVMNNsfsTo7E0E3LgCKvLzCt5si0sa9lbux-1vCvszYQH0HWENULBdb_Oyk3rA_h0xlaPVGpcMaXWMSOUbLU3WPGbTqjDcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aUSBX32zSv_IEuQ1RnacEgEr407nTVswKAIsRecCSKEy3s4Bp32PyPK0zfwZ9fEw05IHTPc1uLaEvr6gmfcP2P1bIImwQ0NqtlHt6NAdwf1VB8cIrqP_SprjIF_i3iR4fBJlrQjT6fmNHaAE7SUW6E5lff8Y8gmKc6m4E_Pw5ib1KoRAqW3l2Gq3GVU8DgWsK6M415kuVp-0hhGdm2H-Nsl7rzNIc0R7VVHr5ZUWAfbJd9-SmsL23tfUEvVJkMvJNcMgipj4wK9GHTF_v2hvQ_rMdTRGP7UytPlKTsMradCJ0iiEvq2veAxUNul9_p3MPfg6RbZKx-6cHZaTMY1ldw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری جمهوری اسلامی، ایرنا، معاون امنیتی استاندار خراسان رضوی وقوع تیراندازی در منطقه بلوار سرافرازان در غرب مشهد و کشته شدن دو نفر را تایید کرده است.
ایرنا گزارش کرده که امیرالله شمقدری گفته است این رویداد تروریستی نبوده و انگیزه اصلی وقوع این درگیری در دست بررسی است.
معاون امنیتی استاندار خراسان رضوی به ایرنا گفته است: «براساس بررسی‌های اولیه ابتدا ۲ نفر با انگیزه شخصی با هم درگیر شده‌اند که یک نفر از آنها کشته می‌شود و با دخالت نفر سوم، نفر دوم نیز جان می‌بازد، هر دو نفر با سلاح گرم کشته شده‌اند.»
آقای شمقدری تاکید کرده است که حادثه در منطقه سرافرازان مشهد روی داده است.
او وقوع هر گونه حادثه تیراندازی و یا رخداد امنیتی در محدوده بافت مرکزی مشهد و اطراف حرم امام رضا در روز پنجشنبه را تکذیب کرده است.
ایرنا اضافه کرده که بلوار سرافرازان که تیراندازی در آن رخ داده، در غرب مشهد واقع شده است و حدود ۱۷ کیلومتر تا حرم فاصله دارد.
@
VahidHeadline
تصاویر هم در همون منابع غیررسمی که پیش‌تر این خبر رو اعلام کرده بودند منتشر شده بود. از درستی‌شون اطلاع ندارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 518K · <a href="https://t.me/VahidOnline/76907" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFKOos9X67HLSMd83AuLbwE_pnGoSUvkq50nveYQ-M-HfzygbJI3hzCOj3ValYt3-vsQCq9_Gg79YLCyOh9_UU7liCzKyqs-jHpcxcV9aKaFJItYP4nN_t6E760_jSSRZlHHh0yludXvauY0oQ95IgRcKlWUuJCO4n7dROhGN3R6xoekz3WWoD4JDyTb1qnJvDWbZcjOR-Y838hBrEjr78v8YfQwPqJsMCBQ3UH7G1dwvrcm4NhVDPVY48B3viHxO2QmcGJs7SHFomzUo3RcwG62d4-poWjHnY7RhGJhOdF-S3ua9WNJtBcxmKe3aJV-F_U2XiA2jW4__v8S5v-pTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
فرماندار کنارک اعلام کرد یک منطقه نظامی متعلق به نیروی دریایی در این شهرستان شامگاه پنجشنبه در دو مرحله هدف حمله قرار گرفته است.
🔸
محمدیونس حقانی به خبرگزاری ایرنا گفت این حمله توسط «جنگنده‌های دشمن» انجام شده و نیروهای امدادی، امنیتی و دستگاه‌های مسئول در حال بررسی ابعاد حادثه هستند.
🔸
ساعاتی پیش از این نیز معاون سیاسی و امنیتی استاندار بوشهر از حمله به یک مقر نظامی در حاشیه شهر بوشهر خبر داده و گفته بود صدای انفجار شنیده‌شده در این شهر ناشی از فعالیت پدافند هوایی بوده است.
🔸
این در حالی است که صداوسیمای جمهوری اسلامی پیش‌تر گزارش‌های مربوط به وقوع انفجار در شهرهای جنوب ایران را رد کرده و اعلام کرده بود «تاکنون هیچ انفجاری در جنوب کشور رخ نداده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 478K · <a href="https://t.me/VahidOnline/76906" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hywWd0Nl6pjZSzJAB6C8FtIPGb9pwSktC4KArXBNQNZx5fPGGiFdA0fgOYdqGhVWnXYuXUFVRn3Ikfnxh1X0cz-Co2TU1P5_Fd33ndWAyeaf8902kk0yRGZ0sd1Yc0qMQJQH8EkzvAk3-T59Rgw48CqPtuZNRi2X0hYpeVyxMySw2LATS-uRbvkN28bBDL3TLCj1DJUqqqgkiJFCa1zW_s6Iid6o6Ep42F9FEDEQTQsJ-odygZzItilU4b5bssrQ7CtgSzakSOR-bKzD9oI6Zc5WUaP9g-WTSa4T7q_jrAzLZnLKmnJUf8ta8dfGhSTj37Qv17td_7TcR0w3l-59ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ایرنا به زبان فارسی سخت تیتری درباره صدای فعالیت پدافند نوشتند، می‌ری توی متن خبر می‌بینی نوشته:
"لحظاتی قبل یک مقر نظامی در حاشیه شهر بوشهر مورد تجاوز و اصابت پرتابه دشمن آمریکایی- صهیونی قرار گرفت."
irna
به نظر می‌رسه از روی صدای انفجار برخورد پرتابه، مدعی تشخیص کشور پرتاب‌کننده هم شدند.
احسان جهانیان، معاون سیاسی و امنیتی استاندار بوشهر، شامگاه پنج‌شنبه اعلام کرد یک مقر نظامی در حاشیه شهر بوشهر مورد اصابت پرتابه قرار گرفته است.
همزمان صداوسیمای جمهوری اسلامی خبر داد تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/76905" target="_blank">📅 23:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ujnVraq13dCqsq5Ne21L-nXmfGvX4e86lIeITbdbsboJC34pmU6sTV6-NQiMLAzotUCLR3PSSDXE472XF50NcDQlVjRSwDIzHO74M5Nm-9adVbbs5-7oGfyd9Mkj8iNUeQFXdseVMx2U5XW92jc4-ejfeeupel0NLngkg-KOJN6Eero0VDctT-hqzuKPDFmg_FypnKBhSBzhIKoyAP964gQyzWWCML-7_3CI3qIkJUUJI04BxOpvV8Tb05hReT_GTWDPQ2ThCRu-lq4yyvSgxecS8inUnemCGi5lTdaaHH6aB2XFXu4XCgzadmkEuTh-0q-lvmZWwUmzYo1jwFmpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی شامگاه پنج‌شنبه به سی‌ان‌ان گفت: «ارتش آمریکا در حال حاضر حمله‌ای انجام نمی‌دهد.»
پیش‌تر رسانه‌های ایران از شنیده‌شدن صدای انفجار در شهرهایی از جمله بندرعباس، بوشهر، اهواز، کنارک و چغادک خبر داده بودند.
همزمان آتش‌نشانی اهواز اعلام کرد انفجار شامگاه پنج‌شنبه ناشی از «نشت گاز» در یک ساختمان مسکونی در منطقه حصیرآباد بوده است.
@
VahidOOnLine
صدا و سیما بعد از تکذیب آمریکا:
برخلاف برخی خبرهای منتشر شده در  فضای مجازی، تا این لحظه هیچ انفجاری در بندرعباس، قشم، سیریک و جاسک گزارش نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/76904" target="_blank">📅 22:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOWeA6jdrvKWB8BfwnJqreofF0ZlW0rtp6q4ini-EOMq3Q870iTz_54oDnYW2GKfOqAPAMvE6N3BCeIB-RDDdfV96HYr_oRnGbP3cY3jowBnD9aDsueZpZ0pDnt_isndRhFlzEoUXTVI4JBmfpImNMNoUybElVsKkhVwm4KkGlBB4z2dntEhP0BvA7EaCwIsO5OLYwtxyn3SDJsyLPd2mZ_36EtqBUZq8y1_CeAVQ4MS62bV8ya1ccUmw-rMTWMz6cAgK3tWA8BvnFAuCU9gx2qyreqyQckUB4ug8TbdZcM1T-CVj8B65CenAtjpCuaJlkqutv4JEMnUiuC4EDH08g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر صدا و سیمای جمهوری اسلامی ایران نشان می‌دهد که اقامه نماز میت علی خامنه‌ای، رهبر سابق جمهوری اسلامی، توسط مصطفی خامنه‌ای، پسر ارشد او، برگزار شده است.
پیشتر تلویزیون دولتی ایران اعلام کرده بود که مراسم تشییع علی خامنه‌ای، در مشهد با نماز میت به امامت آیت‌الله حسین نوری همدانی، به پایان خواهد رسید. دلیلی برای عدم حضور آقای نوری همدانی اعلام نشد.
خواندن نماز میت از سوی پس بزرگ علی خامنه‌ای، بار دیگر نبود مجتبی خامنه‌ای را در مراسم تشییع پدرش مطرح می‌کند.
مجتبی خامنه‌ای از زمان انتخاب به جانشینی پدرش، نه تنها در انظار عمومی ظاهر نشده بلکه پیام صوتی هم از او منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/76903" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76902">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qxysQ4S9xJvB-u6kCPw-vPnkXFf9XQyYe1jVv7dbdZhexugUaafAO5Q-a6XQygm1A3effY68oYXZUqE-LvAguumLGMVBGP8agQrNXO4Cdz9cp4dsZTLpzTEi44tT-vhz-f8chPJ3sEyKyiHZk3t-HNDp76F7qkvTzWpKDvI4Mt0gcwn9KVGCRDH7kRafFE85_FYRMsHXpn3DHY0wO_CNUTCgLHbr-3DLEJNj4cW4UJ28rJD1MnfACML9f0EhTB9WiLW1vJHa6rwkDQgthGYEFLpdNfdkIxI1xwoVid5CBoykbqFSZ1nfU05HM7fEG9z7AdnlzTj7cSatbAWVOLSghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر شامگاه پنج‌شنبه از شنیده‌شدن سه انفجار در کنارک استان سیستان و بلوچستان، خبر داد و نوشت: «از جزئیات و میزان خسارات احتمالی هنوز اطلاعاتی در دست نیست.»
خبرگزاری مهر افزود صدای دو انفجار در اطراف بوشهر و در نزدیکی شهر چغادک شنیده شده است.
@
VahidOOnLine
من از چابهار گزارش از فعالیت پدافند داشتم ولی از کنارک نه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/76902" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76901">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw0_aZkHm_UWYTxoLrC9oC_Ld-8EQ3PjRgVTyhpdzOZNM9faddgFS0HoSdmarNVqS_gCVqt1IzsJUXvKHnUR7lhS-Sd4qhqelFpnDIY--ODI7S0X8OI1KqM_4LricUQN5SmYcbYmawZJOP_nkmKygB2b7bxZ1Ji3V2SJ4vV1lqv8cy1RsVzKjfK4s6vDXag-E5foEwo1WSFq4DmM9PEKVMSwOKgOH3rkP-ogVEYiMGsxtaRHPTwKFRZ4tSa0kRQ5WqHP0mSSx4BIE7eOcwBbBiM5vz54vWsmnIeUzpODUe4RJTgVPck8FjisDQt_1vVewkvUW7EYDbnfFTBdyXcHpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنج‌شنبه خبر داد که عمان رسما مخالفت خود با دریافت عوارض بابت عبور و مرور از تنگه هرمز را به سازمان ملل اعلام کرده است.
از آغاز جنگ تاکنون حکومت ایران بارها تأکید کرده است که مدیریت تنگه هرمز درنهایت با دو کشور ایران و عمان در شمال و جنوب این آبراه خواهد بود و آنها درباره نحوه مدیریت و دریافت هزینه عبور و مرور تصمیم خواهند گرفت.
حال عمان به سازمان زیرمجموعه سازمان ملل یعنی سازمان جهانی دریانوردی اعلام کرده است که با دریافت هزینه در تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/76901" target="_blank">📅 20:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76899">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ARjxWbKHWJ9i8fgMgBDg6bIRoc0fDYTRi8gWGfaOtcsQo81xKL9eqPEN8Ai27ieoJepirFr5_HGtYOTXNACruXkgaBOxB5K-DHq5tGEPR3vN1aVxoOk-my3MF_LUIu58-VOh4Ark6He0Xv6CMA6Hbd8tVxhpZYno66ciqrozHK8d_eMYvUQX7Wz1ppaek3W0mKKxfQ_j8IZn9lmhZe9-rZCNhR-qW-71ePdVK_Sd6v2hQrBB58nHZJTSy0AeyA1NwZfLQCO40QG75c7ongWUAXmfJuqD927fjO3aP9a0fFK3rSi90oLMnIHCX_IDh0GZkHnbro33xAtTAlW9A06ZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lJIb3uA0vxG5Frpm9HvX1oc2vYW87zWkEZ5CXJS0OdpBfDbuJeal0I_sAENVvcG3L_syl0oDmHoJIC95BOiHLMYMt_3fPTYgOwJC2uTmLmJ63DSIxvDvI92J0T9gujbYcEHm3plVJfnmlm7iCWzab7Q_v2RWTKSrF7zuFTpne-BZgLCq0NSOD3cg5NZytkkecnc35PMg9HI1ryeI_7mIX3pYD-vgo-GFyKQwxXoOfcN7H-2Z6no42gs0UFMd_PBK1FHqsz0R0Mr5q2SOW8MfL-sWeZFGh7-ik_3Q3kDjfJAoJcbTfuW__ygTz_ypXU6XJsU5ALYx9WRCeZzsY23j9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیویورک‌تایمز به نقل از فرماندهی مرکزی ایالات متحده (سنتکام)، نیروهای آمریکایی در طول دو روز گذشته بیش از ۱۷۰ هدف نظامی را در امتداد سواحل ایران در نزدیکی تنگه هرمز هدف قرار داده‌اند. این اهداف شامل سامانه‌های پدافند هوایی، انبارهای پهپاد و موشک، قایق‌های تندروی نظامی و زیرساخت‌های لجستیکی بوده است.
سنتکام اعلام کرد که هدف از این عملیات، کاهش توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز بوده است. این روزنامه آمریکایی افزود که تعداد این حملات، حدود ۱۴ برابر تعداد اهدافی است که واشنگتن در آخرین دور تشدید تنش‌ها در ماه ژوئن مورد اصابت قرار داده بود.
@
VahidOOnLine
سپاه پاسداران انقلاب اسلامی روز پنجشنبه ۱۸ تیر اعلام کرد که حملات نظامی ایالات متحده نه‌تنها «پاسخ کوبنده» ایران را در پی خواهد داشت، بلکه ترافیک دریایی حیاتی در تنگه هرمز را نیز با اختلال مواجه می‌کند.
سپاه در بیانیه‌ای اعلام کرد که تردد دریایی به ۵۰ درصد سطح پیش از جنگ بازگشته بود، اما «ماجراجویی و دخالت‌های» واشنگتن در تعیین مسیرهای تردد، عامل اختلالات فعلی است. با این‌وجود سپاه مدعی است که جمهوری اسلامی در تلاش است ظرفیت عبور شناورهایی که مطابق با «ضوابط امنیتی» از سپاه «کسب مجوز» کنند را افزایش دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/76899" target="_blank">📅 17:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oS95AZdUlg-n3-dHyFQQzaxnKdvivo4JD753cy6_Gcqd2hd3X-ojeUiLqeQLR5IG2scMqgTGiqTi43hD-BhWMYGUBpIOVTA3Gpyx3GT4GeuU2mULvvdMohPb-zl__P3ApM6ikrxlJ6W8qMBntbXi1K9RFMHPA0UPpoPDCUmbubfKmo5MudfMjhQRdSpemNm1Mjblh8_7bdiAmggn1Be-5IAn756tVfUj8Cb009zxo0t4vpvj8qkijZSfTDYH_O8V0RUaiL4GlZD6TTmeqPpQIxCr17CG_GXnzhTowOVGxEl1ilrojIAroyIdoVc8IBUxBUJh5I3fgqi_r6OyEzBpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q5doHvcMxmnb3NgzqHTDy7PHempZpe_hiCV_1APHyzKZJCkW0dICqJ77epzjcQ1RRD4RnyR8HYSr-LeL9vIkj5HHX5BuAeyt-GaSPsv8dKt0S6iY7BZorszlpqhYq9hz0r1NoptuaSqAzY_w8dc-4HQ3VcMxUjxwETxhwTCjSxEQ0OtSCWZShTjaEq2xLR4zTFQ8kR5e8ObUMD8xrpgFHmnMVmo-oOjK7MJjdui-mu5bXZYG0vNW9LBqItS35jGZlNnZA-gGO2AQzPildGJ4E-xlU1uRhdtne_ah0g2MTlLkRJGtelQEP-noPRO3DgRR-NzKWMCORqAOp8Ve6FhhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DVsVY0Jhl1yqC1Hf8-SdaYJd8_g0pfukqy3jPAzd10AowKR9FitHIsAOm8gz55T4_0QIyYJgkMSCO_jMBOpgsb-UJECB9aSpS-XyWTG78F7JDH9zs7rb3ZF26oOqgo69yvgYU-ASXGIXR3A6O_GzuzCgWhxa0auEh8XaOTAT0fMG957r59UOuYIaZjIpEEzEvzw6-cmBMLavqLtPSm71zsN9U1zdvUKdp3Y2ZEqVzaHtQbQT2_XosnKd5wnREvZoncr0jKuhBmzD2iROD_ZqUm6FbJcQ35z9W8DdDChTdCJznIubcfpgJVwhkEMsFOJJCYtNA0Md3cxKUfvaKNqK4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=OSWiw1eZxT3ocrmLBiB6IsH4uV4DI0_81mgFc7MTgHvnRgsewuM5g_dLa0PqxWRky38Cgj3k6fNnl0fFmxWy9vbxBXszmCjbPXUze7p8q5moPeQPVfucNcdiASpwsrei4GQpOvOQKmWVLayO2oItqLdZLWXaEm1kcifBPssNct2Ez0lF-pKI1Kgm0-69Cc-QrCCqJt56Y4RGyz6HykgBwXjY-u3pN_Q-8FRgUwfuuauzq2sy5YWokJNjfncJeDdzxEZ3T_G-1sFHEbLkPGN_Dwe6mB8DGX-pKWd2prX7j6INWEWCT89nqMP9HVqHEZxtFJwpwhK9hjKpIwjbfNHtrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/687c7e5359.mp4?token=OSWiw1eZxT3ocrmLBiB6IsH4uV4DI0_81mgFc7MTgHvnRgsewuM5g_dLa0PqxWRky38Cgj3k6fNnl0fFmxWy9vbxBXszmCjbPXUze7p8q5moPeQPVfucNcdiASpwsrei4GQpOvOQKmWVLayO2oItqLdZLWXaEm1kcifBPssNct2Ez0lF-pKI1Kgm0-69Cc-QrCCqJt56Y4RGyz6HykgBwXjY-u3pN_Q-8FRgUwfuuauzq2sy5YWokJNjfncJeDdzxEZ3T_G-1sFHEbLkPGN_Dwe6mB8DGX-pKWd2prX7j6INWEWCT89nqMP9HVqHEZxtFJwpwhK9hjKpIwjbfNHtrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان با ادامه درگیری‌های نظامی میان جمهوری اسلامی و ایالات متحده، روز پنج‌شنبه ۱۸ تیر نیز حملات متقابل دو طرف ادامه یافت؛ حملاتی که از جنوب ایران تا عراق، کویت و آسمان اردن را دربر گرفت.
رسانه‌های داخلی ایران از شنیده شدن چندین انفجار در استان بوشهر خبر دادند.
خبرگزاری فارس گزارش داد که صبح پنج‌شنبه مناطقی در استان بوشهر هدف حملات آمریکا قرار گرفته‌اند.
معاون سیاسی استانداری بوشهر نیز به خبرگزاری ایرنا گفت چند نقطه در این استان، از جمله حریم پیرامونی نیروگاه اتمی بوشهر، هدف پرتابه‌های آمریکا قرار گرفته است.
ساعاتی بعد، صداوسیمای جمهوری اسلامی به نقل از منابع محلی از شنیده شدن صدای چند انفجار در شهر چغادک، در نزدیکی بوشهر، خبر داد.
در همین حال، فرماندار عسلویه اعلام کرد بر اثر اصابت دو پرتابه به اسکله صیادی بنود، ۱۰ قایق صیادی دچار آتش‌سوزی شده‌اند. گزارشی درباره تلفات احتمالی این حمله منتشر نشده است.
هم‌زمان، رسانه‌های عراقی از به صدا درآمدن آژیر خطر در پایگاه نظامی «حریر» محل استقرار نیروهای آمریکایی در استان اربیل خبر دادند. همچنین گزارش‌هایی از فعال شدن آژیر‌های هشدار در پایگاه «ویکتوری» آمریکا در بغداد منتشر شده است.
در کویت نیز رسانه‌های محلی از وقوع انفجار در نزدیکی پایگاه هوایی «علی السالم» و منطقه بندری این کشور خبر دادند. وزارت دفاع کویت اعلام کرد در حملات تازه جمهوری اسلامی، دست‌کم یک نفر زخمی شده و وضعیت او پایدار است.
هم‌زمان، سامانه‌های هشدار در اردن از مشاهده چند موشک، پهپاد یا راکت در حریم هوایی این کشور خبر دادند و از شهروندان خواسته شد برای حفظ ایمنی، در پناهگاه‌ها یا داخل ساختمان‌ها بمانند و دستورالعمل‌های مقام‌های محلی را دنبال کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76894" target="_blank">📅 17:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AElBIRHIuN60g0k93b7jVi6gTV5rZ84LUm9tCUN30BRq2N9sAzrlUORod-O8eG34MsXHyxHfH-Pz-m1DfFRyZW0bFHuEZnTh5ss9M0bSVmdnPSo4M2IdJ3VTIn9LC05gGuCPg1ncD4hnjed5OodW6cDQ3nivBUg-0CAzgmG0SsMvkA8mqUfjMbU-X_Q_FUUBHX93gmOoQrBvz6Zx-TY8NeLgwfRTTGGTAs1x0qpRN_3yIj1UfK8SXh_3CFwCdGC9mmUdiBMroGDOtFfd7zyh1n1W-Oiwj_dsuIezncaeTlb6OEzWls8T38r__JXmBDQ_MN8pfPqICnSKDkrV4bR7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهران رئوف، زندانی سیاسی، فعال کارگری و شهروند دوتابعیتی ایرانی-بریتانیایی که در آستانه ۷۰ سالگی قرار دارد، عصر چهارشنبه پس از حدود شش سال حبس، با پابند الکترونیکی از زندان اوین آزاد شد.
این فعال کارگری در شرایطی آزاد شد که همچنان مشمول محدودیت‌های ناشی از اجرای پابند الکترونیکی است و وکیل و خانواده‌اش ابراز امیدواری کرده‌اند با توجه به شرایط سنی و جسمانی او، زمینه آزادی کامل از طریق استفاده از ظرفیت‌های قانونی، از جمله آزادی مشروط، فراهم شود.
مهران رئوف در مهرماه ۱۳۹۹ همراه با ناهید تقوی و شماری دیگر از فعالان مدنی و سیاسی بازداشت شد. با آزادی یا پایان محکومیت سایر متهمان این پرونده، او آخرین زندانی باقی‌مانده از این پرونده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76893" target="_blank">📅 17:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gwtLNjiyoZ3bVpHKrJZeFk6x2zE70_EJrYr57fwveBsvmSUQME4q9Vd1Wvt_DCudgu2CDBSB4WxWiFtLoyt51gtcP6IqIph-uJnvyR7d4KDAeowUelL_G3ztr6wJZr6lURtBQ2hOOxrYVZk2yaeiv10Y_N-0R8J2OHF4No1dciB1C9t5guYd0ePT9Q5ENL8pzYprxiGZeNoOId_mG2jBvqFzEuwq5REVrjJL-W7m2V4x8--u8TX2NZEHAhFALYp0LIZ9QooYEwY46xZjWek9Fj-GWw8k1e_RdcYvLDo1wUMt3G5TsXjuFMX6diUHlWUFaRrQzcJHFNfp9yQyvAkNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dQv-i8-wkGfE2SBpgom7TCyObBXzlAVW4VG8wmSsZIeITtvq6PaHZrNlz3H1ayuza3XsvGXxcl8rCp3SYA3xljZXojdNhanRpLR-nzY_MF_nPSa9zyEY77LivdVXaNt_NsCPVlnmzHQVLSRR7s21QyrcJY7nA-gYsAIH3frBGH4XxhjIX_PWhrsSewqvW6f22Ttuj_Bq_HXLtxtQjE2DM95FoID9pwcxfd4YkJ1DZDvSIJtgFxbCa7XpmLSEMjvHg6JU8nSYi9u_VO3JPv70T920ttOlP6HUXrwpGhxw_nWcUrv7T33IV-br0fMx-1s1e-ERkR7kYyLSJGKOq4OOCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری بلومبرگ روز پنجشنبه خبر داد که رفت‌وآمد کشتی‌ها در تنگهٔ هرمز پس از دور تازهٔ حملات آمریکا و ایران به مواضع یکدیگر، تقریباً متوقف شده است.
بر اساس این گزارش، داده‌های ردیابی کشتی‌ها نشان می‌دهد حرکت‌های قابل مشاهده در این گذرگاه حیاتی انرژی جهان عمدتاً در مسیری انجام شده که مورد تأیید ایران و نزدیک‌تر به بخش شمالی آبراه است، در حالی که کریدور مورد حمایت آمریکا و عمان عملاً بدون تردد بوده است.
@
VahidHeadline
راه‌آهن جمهوری اسلامی می‌گوید بر اثر حملات آمریکا به «یکی از ‌نقاط مسیر ریلی تهران–مشهد»، حرکت قطارهای مسافری در این مسیر متوقف شده است.
در بیانیه راه‌آهن به محل دقیق هدف قرار گرفته، اشاره نشده اما آمده که تیم‌های فنی و عملیاتی به محل اعزام شده و «عملیات بازسازی محل آسیب‌دیده در دست اقدام است».
توقف قطارها در مسیر تهران–مشهد ساعاتی پیش از برگزاری مراسم تشییع جنازه علی خامنه‌ای در مشهد رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 491K · <a href="https://t.me/VahidOnline/76891" target="_blank">📅 10:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=ZBHJHcqdxjssuGySRsDB1By7QPI_g3sGu2e7ScM0YTclHmrkpd50NTHsIz7O9kdQuSnpqUdM3rgYCs5xV7uJeus2HPJCcjrTCSvCTXNodpVOkHktuijMPWYyIGq8AIV0K-1TsPq38Po-MXRvuVRRvVDJG3Q6UrbVGHLfQ68gX9htymIyHxmOOT8o-K1-JutZATxT623PLPoCVLyIY_m1Qdwyee5uq7fr1gfBjOelcq43hGZEhfWid3l3pncoUbqRsE6DZQkNR5f9jp38GwqgH2sAgCpAkIkXJwVE5SlbFtWntIezrIiz090Rpr9yabKfiikpB05XGgxBxOuVTN0DfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86782c7f01.mp4?token=ZBHJHcqdxjssuGySRsDB1By7QPI_g3sGu2e7ScM0YTclHmrkpd50NTHsIz7O9kdQuSnpqUdM3rgYCs5xV7uJeus2HPJCcjrTCSvCTXNodpVOkHktuijMPWYyIGq8AIV0K-1TsPq38Po-MXRvuVRRvVDJG3Q6UrbVGHLfQ68gX9htymIyHxmOOT8o-K1-JutZATxT623PLPoCVLyIY_m1Qdwyee5uq7fr1gfBjOelcq43hGZEhfWid3l3pncoUbqRsE6DZQkNR5f9jp38GwqgH2sAgCpAkIkXJwVE5SlbFtWntIezrIiz090Rpr9yabKfiikpB05XGgxBxOuVTN0DfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در توییتر میگن 'ترامپ به محمدباقر قالیباف گفته محمد سامتینگ':
twitter
ترامپ: می‌گویند یک محمدفلانی دارد آنجا با بیل‌ یک کارهایی می‌کند. بیل‌ها شما را به جایی نمی‌رسانند. بزرگترین ماشین‌آلات دنیا هم احتمالا شما را نمی‌توانند به آنجا [محل دفن اورانیوم] برسانند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 514K · <a href="https://t.me/VahidOnline/76890" target="_blank">📅 07:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=dr3nnKLZnBTQJFRpeKoKwdXJp4HcmwCJm3DTzXqWhABgPwA7oTsDwUi5K9CBmm3-lxdROmIxdv1rdJBNdfe7gZBKfHiG_V8eTSN_IHvT_lj0Xjg1Wl7BBn4au0QTS_9vQi_8EoO_Bjkijbp-K2e_gzkSFq_eiUPvz-5xO53ov6S1jMeN_bXVt_2Qehdf8kB2hT2RAAavhSk_pzF4fuxICZThrWO_Qal81iPWanz6VPTvFNFr1Mw5QSsnIUhSKJhzfgRFf3pgCo2V4wKtlrpcHrtv8VDD3mYJtSw3ZuoOrHHwlpDZLBFkfzcGqNAegVtMiqTygwXTpR8F04c--bwYXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faff74c4ac.mp4?token=dr3nnKLZnBTQJFRpeKoKwdXJp4HcmwCJm3DTzXqWhABgPwA7oTsDwUi5K9CBmm3-lxdROmIxdv1rdJBNdfe7gZBKfHiG_V8eTSN_IHvT_lj0Xjg1Wl7BBn4au0QTS_9vQi_8EoO_Bjkijbp-K2e_gzkSFq_eiUPvz-5xO53ov6S1jMeN_bXVt_2Qehdf8kB2hT2RAAavhSk_pzF4fuxICZThrWO_Qal81iPWanz6VPTvFNFr1Mw5QSsnIUhSKJhzfgRFf3pgCo2V4wKtlrpcHrtv8VDD3mYJtSw3ZuoOrHHwlpDZLBFkfzcGqNAegVtMiqTygwXTpR8F04c--bwYXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا از حملات به چندین هدف مختلف نوشت: نیروهای آمریکا دور دیگری از حملات علیه ایران را تکمیل کردند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۸ ژوئیه دور دیگری از حملات علیه ایران را تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
نیروهای آمریکا حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، محل‌های نگهداری موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
این حملات تازه در پی اجرای موفق حملات تهاجمی در ایران در شب قبل انجام شد.
نیروهای سنتکام در ۷ ژوئیه حدود ۸۰ هدف نظامی ایران، از جمله بیش از ۶۰ قایق کوچک سپاه پاسداران انقلاب اسلامی را هدف قرار دادند تا به‌دلیل نقض آتش‌بس از سوی ایران با حمله به سه شناور تجاری در حال عبور از تنگه هرمز، هزینه‌های سنگینی بر آن تحمیل کنند.
نیروهای آمریکا همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که از سوی فرمانده کل قوا دستور داده شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 489K · <a href="https://t.me/VahidOnline/76889" target="_blank">📅 06:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اکسیوس: با «پایان» آتش‌بس ایران، ترامپ به نبرد بر سر هرمز روی می‌آورد
ترجمه ماشین:
کاخ سفید خود را برای چیزی آماده می‌کند که می‌تواند به تبادل آتش چندروزه یا حتی چند‌هفته‌ای با ایران بر سر تنگه هرمز تبدیل شود.
مقام‌های آمریکایی به Axios می‌گویند طول و شدت کارزار جدید کاملاً به اقدامات بعدی تهران بستگی دارد.
چرا مهم است: جنگی که با هدف تضعیف توان موشکی ایران و نابود کردن آنچه از برنامه هسته‌ای‌اش باقی مانده بود آغاز شد، به نبردی بی‌پایان بر سر مهم‌ترین گلوگاه انرژی جهان تبدیل شده است.
یک مقام آمریکایی گفت تشدید تنش فعلی می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد؛ بسته به اینکه آیا ایران به حملاتش به کشتی‌های تجاری در تنگه هرمز ادامه می‌دهد یا نه.
این مقام آمریکایی گفت: «می‌خواهیم کمی بهشان سیلی بزنیم تا بفهمند ما شوخی لعنتی نداریم.»
محور خبر: دیپلماسی فعلاً متوقف شده و فشار نظامی دوباره در مرکز راهبرد رئیس‌جمهور ترامپ قرار گرفته است.
ترامپ روز چهارشنبه گفت آتش‌بس ۶۰روزه‌ای که در یادداشت تفاهم (MOU) ترسیم شده بود، پس از تبادل آتش ناشی از حملات ایران به کشتی‌های تجاری «تمام شده» است.
سپس آمریکا دور دوم حملات را در نزدیکی تنگه هرمز آغاز کرد، از جمله حمله به اهداف زیرساختی در داخل ایران برای نخستین بار در چند ماه گذشته.
ایران با حمله به پایگاه‌های آمریکا در کویت و بحرین تلافی کرد، در حالی که تأکید داشت از ادعای خود برای کنترل تنگه عقب‌نشینی نخواهد کرد.
کمی بعد، ترامپ علامت داد که آمریکا آماده کاهش تنش است و به خبرنگاران در هواپیمای Air Force One گفت مقام‌های ایرانی «کمی پیش تماس گرفتند» و «می‌خواهند توافق کنند.»
مشخص نبود ترامپ به کدام تماس اشاره می‌کرد و مقام‌های ایرانی نیز فوراً هیچ ارتباط مستقیمی را تأیید نکردند.
ترامپ اضافه کرد: «فقط نمی‌دانم شایسته توافق کردن هستند یا نه. نمی‌دانم قرار است به توافق احترام بگذارند یا نه. راستش را بخواهید، یک جورهایی دیوانه‌اند.»
طرف مقابل: مذاکره‌کننده ارشد ایران، محمدباقر قالیباف، آمریکا را به «قلدری و خلف وعده» متهم کرد و هشدار داد که تنگه فقط با شروط تهران بازگشایی خواهد شد.
قالیباف در X نوشت: «اگر بزنید، می‌خورید. تنگه هرمز فقط با «ترتیبات ایرانی» باز خواهد شد، نه تهدیدهای آمریکایی.»
تصویر کلی: بازگشایی تنگه هرمز و بازگرداندن آزادی کشتیرانی برای کشتی‌های تجاری، عمدتاً برای تثبیت بازارهای جهانی انرژی، به یکی از اهداف اصلی دولت ترامپ تبدیل شده است.
برای ایران، حفظ کنترل بر تنگه به یکی از اهداف کلیدی در هر توافقی برای پایان دادن به جنگ تبدیل شده است.
این مسئله یکی از بندهای محوری یادداشت تفاهم آمریکا و ایران بود و برداشت‌های متضاد از بندهای مربوط به تنگه اکنون باعث فروپاشی این توافق شده است.
این یادداشت تفاهم ایران را ملزم می‌کند اجازه عبور امن کشتی‌ها از تنگه هرمز را بدهد. اما اندکی پس از امضای آن، مقام‌های ایرانی آمریکا را متهم کردند که با عبور دادن کشتی‌ها از یک مسیر جنوبی در نزدیکی ساحل عمان بدون تأیید تهران، توافق را نقض کرده است.
پشت پرده: مقام‌های آمریکایی می‌گویند کاخ سفید معتقد است فضای بیشتری برای تشدید تنش دارد، چون صدها نفتکش در هفته‌های اخیر توانسته‌اند از طریق تنگه از خلیج فارس خارج شوند.
به گفته این مقام‌ها، همین مسئله نگرانی‌ها در داخل دولت را کاهش داده که درگیری تازه فوراً باعث جهش بزرگ قیمت نفت شود.
پشت صحنه: یک مقام آمریکایی ادعا کرد تشدید تنش فعلی ناشی از سرخوردگی عناصر رادیکال‌تر درون رهبری ازهم‌گسیخته ایران است؛ کسانی که معتقدند یادداشت تفاهم منافع واقعی برای تهران به همراه نداشته است.
این مقام گفت ایران می‌دید که اهرم فشارش در هرمز در حال لغزش است، در حالی که صدها کشتی از مسیر جنوبی نزدیک به ساحل عمان عبور می‌کردند.
با وجود معافیت‌های تحریمی آمریکا، ایران برای فروش نفت با مشکل روبه‌رو شد، چون مؤسسات مالی تراکنش‌ها را تأیید نمی‌کردند و کشورها تمایلی نداشتند به معافیت‌های موقت تکیه کنند.
هیچ‌یک از دارایی‌های مسدودشده ایران آزاد نشده است، چون ایران هنوز گام‌های هسته‌ای مورد نیاز طبق توافق را برنداشته است.
به گفته این مقام، توافق چارچوبی که آمریکا میان اسرائیل و لبنان میانجی‌گری کرد، بخش مربوط به لبنان در یادداشت تفاهم را غیرضروری کرد.
آنچه باید دید: این مقام آمریکایی گفت: «بخشی از رهبری ایران از همه این چیزها راضی نبود.»
«آنها شروع به تیراندازی کردند و ما تصمیم گرفتیم وقتش رسیده محکم بهشان سیلی بزنیم. این یک روند است. ما صبر داریم. اگر احساس نکنیم به توافقی که می‌خواهیم می‌رسیم، آن را انجام نخواهیم داد.»
جمع‌بندی: معاون رئیس‌جمهور ونس روز چهارشنبه گفت موضع آمریکا ساده است: تنگه هرمز باید باز بماند.
ونس گفت: «اگر تلاش کنند آن را ببندند، پاسخ ارتش آمریکا را در پی خواهد داشت.»
«یا می‌توانند از آن تبعیت کنند، یا دقیقاً همان چیزی را داشته باشند که دیشب برایشان اتفاق افتاد. این فقط ادامه خواهد داشت تا وقتی که آن مسیر را باز کنند و تیراندازی به کشتی‌ها را متوقف کنند.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/76888" target="_blank">📅 06:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kOFlZF3eX7wLtATrK6W44Iw5qJeQsuaoiweEWJtykVRA_uL8WSDKwKqXVZkrzLWAWDrijGGy13RjHGDeQCOHJGyUKg3UXhFVrOaSLygFDrVSCC9EKB7-A0WgV7fYV_XZgVBBZ-wVSUZB_BudZeAQ9sqCod2Ik_Lxnd7asNto74w0bBf6cNtM6xdKN68fRw5IFK6yF4x6XhdIGjjmGQCPu4Hs2EEF-OVA-t3y6XvuzrdNm1LLmtNLxcswpf_dlYneQJbcke3knQz24WS_INhWggR1JcBAq9LC8LexVtrgo0cm8sPZDFNlfeQ4jce2zfLnnN9Ggj5RrqUMawqFaWsptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای که از صداوسیما پخش شد، اعلام کرد نیروی دریایی و نیروی هوافضای سپاه در «یک عملیات مشترک پهپادی و موشکی، زیرساخت‌ها و تاسیسات آمریکا، از جمله اردوگاه عریفجان و پایگاه هوایی علی السالم در کویت، و همچنین پایگاه هوایی شیخ عیسی و منطقه جفیر در بحرین را هدف قرار داده‌اند.»
@
VahidOOnLine
متن بیانیه به نقل از ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت شریف ایران، ملت کریم و مجاهد عراق؛
🔹
آفرین بر شما مردمان مومن و بصیر و وفادار که با موقع شناسی و تشییع بی‌نظیر در تاریخ جهان قدر و منزلت ولایت الهی و عشق عمیق متقابل مردم و والی اسلامی با مرام امیرالمومنین (ع) را به رخ جهان کشاندید و با شعارهایتان یادآور شدید که هزینه تعدی به مرجعیت و ولایت فقیه مسلمانان بسیار سنگین خواهد بود.
🔹
هرچند این تشییع باشکوه به ویژه ۲۳ ساعت تشییع عاشقانه در گرمای شدید، سرزمین عراق حبیب، مستکبران کاخ نشین را وحشت زده و آنها را به واکنش عجولانه به این قدرت نمایی مردم واداشت و آمریکای عهد شکن با زیر پا گذاشتن همه تعهدات بار دیگر نقاط متعددی از استان‌های ساحلی جنوب ایران و در اقدامی ضد مردمی دو پل در استان‌های شرقی به سوی مشهد مقدس را مورد تجاوز قرار داد تا اخبار این حماسه بی‌نظیر را تحت شعاع قرار دهد و این رویداد الهام بخش را از نظر مردم جهان پنهان دارد، غافل از اینکه این جنایات مردم جهان را بیدارتر و آنها را برای نقش آفرینی در مبارزه‌ با شیطان بزرگ مصمم‌تر خواهد کرد.
🔹
رزمندگان اسلام تجاوزهای ارتش کودک‌کش آمریکا را بی پاسخ نخواهند گذاشت.
🔹
در اولین مرحله از پاسخ تنبیهی علیه پیمان شکنان آمریکایی، رزمندگان نیروهای دریایی و هوافضای سپاه طی عملیات مشترک موشکی و پهپادی، ساعتی پس از حملات دشمن و نقاط مختلف کشور، زیرساخت‌ها و تاسیسات مهم دو پایگاه‌های استعماری اشغالگران آمریکایی در عریفجان و علی السالم کویت و جفیر و شیخ عیسی در بحرین را در هم کوبیدند.
🔹
سپاه پاسداران انقلاب اسلامی به ارتش کودک‌کش آمریکا اخطار می‌کند که در صورت تکرار تجاوز پاسخ‌های کوبنده ما به سایر پایگاه‌های آمریکایی در منطقه توسعه خواهد یافت.
و ماالنصر الا من عندالله العزیز الحکیم
سپاه پاسداران انقلاب اسلامی
۱۸/تیرماه/ ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76887" target="_blank">📅 06:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QPqPx43V4X0n0UFFbP8WFtkITZ5CZ7oElkk4UQEVRfh7Loe58SbOWM09JxDMmlw7RIjoK5A-Yw6mzp5uOCHbxPs5WRHTOFOSKx_Oj-CaGljV-hyNbP5KsG6l5Pd4YnDetXUfx3PP0r-j985Pi_4aKPNAXVCw4JTYY6TZ0BBTJshz5pAThIdgI0LXGDymo1-WuO3fvIwFjNZgtJ7feoXMrnbzEfFfn7JfDTnThuAeMHk8xih51MOA-ibS984BPj53b0roQQyGWS0fZ-7a-ftuoAwJwcq9rsIAx1Z8RmsHZ-UBJafnXvNWSI9RufS8TRg1xzCnWkNFi9-4Nhhi4vL0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی:‌ 'برج مراقبت ترافیک دریایی بندر
#چابهار
که چهارشنبه ۱۷ تیر  مورد حمله قرار گرفت.'
Vahid
چند دقیقه پیش هم دوباره از سیستان و بلوچستان:
سلام سمت کنارک الان صدای انفجار اومد
کنارک رو یه جوری سنگین زد از خواب پریدیم
۴ تا پشت هم
از بوشهر هم پیام‌های تازه‌ای می‌فرستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76886" target="_blank">📅 05:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76885">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=WnUfaK3Oj4VPBFxxj9kyDqyzjAgZzFWeAWoJMk1ent5WHWhW6AUL-gADsnJqus8Z22tFnDpP8_pamiUQE0G6eS35jFkboIhEa0nbIO2x_SBovt_r41Kb4SA7-QrvCoa-c-wJBTzbQKMr1FrW8X2bnLX-P-yGYiFI8Tsy0V8t6jdzbz6hk6bdFsKgoKqQZ4Z9IrH291ZuRjj-ibB4KI_hWLdg9Hc9nu5Yhuh0oDihYxg-BHn8Rmwo9to4lRodZFJ_eSQq99Mlfi1mJdNNrZGKOzU63BNZ5BdiE2RU_0fM7z1OK_C2LhyKncwF1xjiFz3UsWGREs9yo36jokF7T0icAg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1ee7dc63aa.mp4?token=WnUfaK3Oj4VPBFxxj9kyDqyzjAgZzFWeAWoJMk1ent5WHWhW6AUL-gADsnJqus8Z22tFnDpP8_pamiUQE0G6eS35jFkboIhEa0nbIO2x_SBovt_r41Kb4SA7-QrvCoa-c-wJBTzbQKMr1FrW8X2bnLX-P-yGYiFI8Tsy0V8t6jdzbz6hk6bdFsKgoKqQZ4Z9IrH291ZuRjj-ibB4KI_hWLdg9Hc9nu5Yhuh0oDihYxg-BHn8Rmwo9to4lRodZFJ_eSQq99Mlfi1mJdNNrZGKOzU63BNZ5BdiE2RU_0fM7z1OK_C2LhyKncwF1xjiFz3UsWGREs9yo36jokF7T0icAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد پنجشنبه ۱۸ تیرماه، در مسیر بازگشت از نشست سران ناتو در آنکارا و در هواپیمای ریاست‌جمهوری «ایر فورس وان» گفت آمریکا در برابر حملات ایران رویکرد «۲۰ به یک» را دنبال خواهد کرد.
ترامپ گفت: «همین حالا ضربه بسیار سختی به آن‌ها زدیم. هر بار که آن‌ها به ما حمله کنند، ما ۲۰ برابر پاسخ خواهیم داد.»
او افزود تهران سه کشتی را هدف قرار داد و تاکید کرد هر زمان حکومت ایران حمله کند، آمریکا «بسیار شدیدتر» پاسخ خواهد داد.
@
VahidOOnLine
پست قالیباف:
آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با «ترتیبات ایرانی» باز می‌شود نه با تهدیدات آمریکایی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76885" target="_blank">📅 05:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اکسیوس:
یک مقام آمریکایی گفت ارتش آمریکا در چارچوب حملات روز چهارشنبه، دو پل راه‌آهن را در شمال‌شرق ایران با موشک‌های کروز هدف قرار داد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76884" target="_blank">📅 05:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=jvAVcmpbrE6LUkLce1nROTaqUwQlr1uKSbcLzml8nLuXCs9noF4pFeiZkqi5j_ll0f2inpGPz4EFWkqwBDmeiYzJ1ED1jDDzs-ICzzOV0xlLliwdgz2tA2gEhxGGviaIZ4DPjQN5pIAAPAgEMnz2CgKVtaM3cFJyDXAwVsk8rB6p-2ltTskiTQNRLoPfGElDpuMNhVKs_KkpSOL94SYBN6xBEQkY6xoNQAiPJqFcM_YkZ6ZkWgJRXpk3tLiPROUS2sdQJcGbG7X3vn1b5lceuDUkVXhLDlLvUZX5BuWnp9ECx9BOqnkMkYOEIdVm1o3rwvz7guILMvydPonUQUfrug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a9c09d7a1.mp4?token=jvAVcmpbrE6LUkLce1nROTaqUwQlr1uKSbcLzml8nLuXCs9noF4pFeiZkqi5j_ll0f2inpGPz4EFWkqwBDmeiYzJ1ED1jDDzs-ICzzOV0xlLliwdgz2tA2gEhxGGviaIZ4DPjQN5pIAAPAgEMnz2CgKVtaM3cFJyDXAwVsk8rB6p-2ltTskiTQNRLoPfGElDpuMNhVKs_KkpSOL94SYBN6xBEQkY6xoNQAiPJqFcM_YkZ6ZkWgJRXpk3tLiPROUS2sdQJcGbG7X3vn1b5lceuDUkVXhLDlLvUZX5BuWnp9ECx9BOqnkMkYOEIdVm1o3rwvz7guILMvydPonUQUfrug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی پخش شده با شرح: 'بوشهر آخرین دقایق چهارشنبه ۱۷ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76883" target="_blank">📅 04:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EBetTlNgRVGl3jQIucKKptd3zwEAKIKyq0n5mZG7_PCla1KUU5H6VoYrSFDdF5pn-w-x6siI93_hkyACJaPPpyOW3uM4RJJS1tkaIGi8fb060jsUOBH3ZzdZGsd8oygejrZhucSSBRyb8AVi5W3_dwhu9o8lOQib9QEl5pkx6aM4ayQlpy2WgRCg0bpLqw1zdNvK2AuznEeuaDECitjH2JyWgs53SJeJ-oAJTyRz-KDVLhvV0EORXMZaUz6rcMFrHhx4mqszf6cbMbOGivEcUtbPh64k1LSUBIuAtwxToLzMKemTQBYp9m8bq1KSslXAZbPx2tjxZYD6rztnC7oyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلی پیام درباره شلیک موشک از اهواز و امیدیه در خوزستان
و هم‌زمان درباره اعلام هشدار در کویت و بحرین
در خبری دیگر:
برای  نخستین بار در نزدیک به سه ماه گذشته چنین پیام‌هایی برای ساکنان قطر نیز ارسال شد.
قطر همزمان از میانجی‌های مذاکرات تهران و واشینگتن است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76882" target="_blank">📅 04:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=L8LazVZ1_x90YWqP8Dh5MUm7bLS8P1hL7OBFpsJ3uhhIzu8ODVeyumkpNXSATEz7RS_bKDMRlQvFaHS8ZTLLKcmDSBG_mDooFpTR7fJBSXGXygGULTF31JLmxTgX0NiesKOrqljT5UKKMbIf_Yp_ZR-0CJKFxQj4-GPbdpvh4nnoJEMPHYYHA5hYDrGdO2bXA-DflHljBCZZH5Dgy5PQ9u4g1s7WQu5pQMXVEMVpnGskT3hK804AfmE0iHHdOc9a0zRP0YM0TBzDEvVqLVTx9ORyh3AnGA6zqcipr3hSlK83nv3mhmN2GdN5Qmx-DgH6Hhk05F2UBYkLS1sBD1BQvw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d485a6535f.mp4?token=L8LazVZ1_x90YWqP8Dh5MUm7bLS8P1hL7OBFpsJ3uhhIzu8ODVeyumkpNXSATEz7RS_bKDMRlQvFaHS8ZTLLKcmDSBG_mDooFpTR7fJBSXGXygGULTF31JLmxTgX0NiesKOrqljT5UKKMbIf_Yp_ZR-0CJKFxQj4-GPbdpvh4nnoJEMPHYYHA5hYDrGdO2bXA-DflHljBCZZH5Dgy5PQ9u4g1s7WQu5pQMXVEMVpnGskT3hK804AfmE0iHHdOc9a0zRP0YM0TBzDEvVqLVTx9ORyh3AnGA6zqcipr3hSlK83nv3mhmN2GdN5Qmx-DgH6Hhk05F2UBYkLS1sBD1BQvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای دریافتی و تصاویر منتشر شده با شرح 'انفجارهای حمله به آق‌قلا در استان گلستان'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76879" target="_blank">📅 04:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76877">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iv1_98ALTjrCRBCLyqkQk1TSnRXmNc5HM-h0EkdPX5HZUnoqk1I6x80LvnOuOQeXHAbryZjta0h8vtY8FF02b1EAGiZ9x82kk6fb8Ul6W3IZ4M9XXhAkAUbSCVPPT1Yxbi4VNKf5roEHERwWICekG2Ag38eOnhvr1D3b1UOQxb2ph8vs2aeJnFTiC-mDkmh1GCHmRXZt5bKwA0Cni1a9q-IJqh7VB8qFV0ijm-h5DRx3cUnoc4bnH6zRJ_rW9Ehrm-NwZzUPakCPwfKBkV1yBi-VF43tj_PzQeJzxdYKVBS_tDfRmNnu6JbzbftAkLApkf6mndUs8oZNkUhPNwhGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=WRMtRazSH3L-6m9fxtPw2NXvpkRLEdZyTKTZlxWaGqn4Ba3JylOPZmqMYxosb96avabOLyAxrIE26pCtOk2wZeZN65QoabdbhR10fhWl1xim4_Ng5AHzExW9ohZVMBAPQGZ7sfl_pH667HHHRJn6CHfj1o9CnT-yyHMrhz-6gORtFrCqcy9OJsNCExlh-AJAx3T672jMMneBcWC-kQjQSKAc2n_O4gBTu30XLofcIaYOkZlc4KLHBSvfsd_mbEjUxcg7AQm565b-yhT9VHxECA3FXs8MJrbBlKJD9krMZYfBOJBVlUBmFnpZ_2kpFX-jGQhU4OLumcU5cqqcTWm4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4761d5d8a3.mp4?token=WRMtRazSH3L-6m9fxtPw2NXvpkRLEdZyTKTZlxWaGqn4Ba3JylOPZmqMYxosb96avabOLyAxrIE26pCtOk2wZeZN65QoabdbhR10fhWl1xim4_Ng5AHzExW9ohZVMBAPQGZ7sfl_pH667HHHRJn6CHfj1o9CnT-yyHMrhz-6gORtFrCqcy9OJsNCExlh-AJAx3T672jMMneBcWC-kQjQSKAc2n_O4gBTu30XLofcIaYOkZlc4KLHBSvfsd_mbEjUxcg7AQm565b-yhT9VHxECA3FXs8MJrbBlKJD9krMZYfBOJBVlUBmFnpZ_2kpFX-jGQhU4OLumcU5cqqcTWm4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'شلیک چند موشک از جم در
#بوشهر
پنج‌شنبه ۱۸ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76877" target="_blank">📅 04:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=FsbDVvv3UI_LYCM3rxAZIY-4RaIX6tsEpLnjvSRARCdAXl_ohxs1fWqHrwVmqix5PKKoEidBIMr9ph62_msrguK6KkocsvJ3Ql3A-U48KIHcetW-_2dw06lHh7jaK3QqzjSu6Uz1EtIx5RIl__zsD_F7JBeVDhz4SZoOHhEWBgf2i7n9V5DJIGFZVD8QcWyfwVbSmdSajvQrdXdgCL90vD97G1MH6bgnueMePxu0zN5XQwSmPgqzTtTfaODNHUnIs5UQMvsJyZiwfZiDBxbhkoMosPRV0oTqxnU6ISXExr37oQBOpv1WgYQGz_V4RWOfEaVughf5-0nXVlBoBzoElQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6e40fe096.mp4?token=FsbDVvv3UI_LYCM3rxAZIY-4RaIX6tsEpLnjvSRARCdAXl_ohxs1fWqHrwVmqix5PKKoEidBIMr9ph62_msrguK6KkocsvJ3Ql3A-U48KIHcetW-_2dw06lHh7jaK3QqzjSu6Uz1EtIx5RIl__zsD_F7JBeVDhz4SZoOHhEWBgf2i7n9V5DJIGFZVD8QcWyfwVbSmdSajvQrdXdgCL90vD97G1MH6bgnueMePxu0zN5XQwSmPgqzTtTfaODNHUnIs5UQMvsJyZiwfZiDBxbhkoMosPRV0oTqxnU6ISXExr37oQBOpv1WgYQGz_V4RWOfEaVughf5-0nXVlBoBzoElQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدای ویدیو: هوافضا ی چغادک بوشهر رو زدند
ویدیوی دریافتی، نخستین ساعت 'پنج‌شنبه ۱۸ تیر'
Vahid
📍
گویا اینجاست:
GoogleMaps
via
Mitch_Ulrich
🔄
آپدیت:
پیام‌های دریافتی الان دوباره ساعت ۳:۳۵
بوشهر دوباره زدن…
همین الان پنج تا انفجار بوشهر
سلام وحید جان ۳:۳۸ صدای چندین انفجار، بوشهر.
سلام آقا وحید بوشهر سه دیقه پیش صدا انفجار اومد
🔄
آپدیت:
بوشهر رو خیلی بد زدن.
ناحیه‌ی بهمنی، چهارراه ریشهر.
ساعت ۳:۵۵
سلام
بوشهر همین الان بازم زدن سه چهارتا پشت سر هم صداش خیلی بلند تر از قبلی ها بود
۳:۵۶
وحیدجان الان ساعت 3:55 صدای 5یا 6 انفجار پشت سر هم اومد، احتمالا از پایگاه هوایی بوده
سلام وحید جان بوشهر الان ساعت ۳:۵۵ خیلی شدید زدن پایگاه هوایی رو
دوباره صدای انفجار اومد بوشهر ساعت 3:55
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
بوشهر از ساعت ۳:۲۰ تا الان ۳:۵۵ کلی صدای انفجار میاد، ۳-۴تاش خیلی صدای وحشتناکی داشت!
الان بوشهر ضداى انفجار ٤ ٥ تا
ساعت ۳:۵۶ دقیقه صدای حداقل سه انفجار در بوشهر شنیده شد.
چند انفجار هم بعدش شنیده شد که بنظر دور تر میومد
🔄
آپدیت:
بوشهر ساعت ۵:۲۲
صدای دوتا انفجار پشت سر هم اومد
۵:۲۲ بوشهر رو همچنان دارن میزنن، احتمالاً پایگاه هوایی
سلام بوشهرو زدن
الانم صدای فعالیت پدافند و توپ سنگین میاد
وحید نیم ساعت پیش صدا انفجار داخل بوشهر اومد نمیدونم دقیقا کجا بود ولی خیلی بد بود صداش
🔄
آپدیت:
دوباره الان صدا اومد ساعت ۵:۵۶
اطراف محله بهمنی بوشهر ساعت 6:01 صدای دو انفجار مهیب شنیده شد
ساعت ۰۶:۰۰ صدای انفجار مهیب در شهر بوشهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76876" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jhpF_Z3CTqTMSXGHFvDNUCkcaTlYyt5TBkm1iYOLqqThnAmz-LfSWkebx9nT22jLkHDj3mVrPlIvg2W-CCYU72IGqkB7dX34WbvuwVMfG7Ocf5QIUB3UX-MuRp4PRaVyj2jlG6XqXQfsZPikZD95iUbHHuUcn4vJaEnhyY00tTaMYVlTTB8xePyVwlpaFSvm7KzHQs95tlqrw3KsD1x28kVH8SsIRCQxZ7puwOsaB_l31sjbRt1NMYfYWKKkzssjZ6PSaiIs1LmoQPmk_6VOQPnGMerKK_ECGzSQM438bFeyFNFXhfCAaq29gVkjFGatb_6u9pG7XP8EqlLkhnsnBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aydrCl7R3WPTrlCqpiUWMi1awds0xuyky8tLJXOt68Qt1hoA7sa2jPk4x3vKkoF5rUpVjTgQc6kRPJ9yGy4ObglfcOsqwE1TxuNwm0YgR7g_VM2A30t4SSDH8JW99PDpB6Z-x5tGXRwuBmLEmyUEb5ere3cGZ7ein8qJMBxPnNT4vWTGOWpHtV6FrIggcemqyz6yzi2xdluEJSoGYDzNsR3jScXp4tNK5QljhFt3RAKwX5rIk_imv7tYLOlBfOOCijOeM9-jhaXeTVXqZaXdTd3j1wiWc_bvozuYZ5m47ZlSwLfI5GdYhbcQdFKH6oE_P1MqCmBHXPaTN4A-XnVAhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MhNb9k7e-ttGd8UGbbr9T6fyvC0k2W9hjRL3b5WTndqUfRf8yPY41SNdrpUE2l1jfH3gZKOENBCtpjKpvvS7NF89tgxDyc14z6yHI109kiqTCCx2ZM5BELI0GQR6NmOuj9IrWGNlZmuTjijn4CcLMURlra_A7QHZT40drauqLqlqY_gCe2iuWYSYTh09FEbmY_uLeQj5qCweT2c4I-Sk4gEd8t1eqVAixmnYozGgpo8zSVXru0i8aNI-_Sf7VFrXYbFo6LJEe1jNf3DAFuO_MsZGMScMs9DezDjB8OewLrtMpO2lUWDuCyZrOzFHbhF90cj2tHZaFSgS92pfaLcsDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=dc1zYRLR2tNOzlxafhE_-9sX4iWqBXrQvkepDy0cgbXHKtITR5Fx5HwR9gXK--xaj2y2QpA4_PQ2ZNvaB3Ngoi_plUnZvQEIr57vI9j0yPLT0qHI4JAukXSD4Dp1Uvs0ZMHEH065i3BO7YvboawfXcIZB3Zg2Iv2vH3tuSMULPeIoe7QJkJENbP35yEp6M_Krz4_lovG4bN6AummsbmD0SXvurvr3HXrP_LHWUC-N8zss_0d02RRCtvSEVhnHH_LrmCX8wVCCyTDxd4LLiCXsZQ8PvMd1TpPW8Eq7L2Xxhs9VUE-BpxSKEd70jy54BwE_RQRD1mP6QjjAb7Cl2q4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6c0e73ce6a.mp4?token=dc1zYRLR2tNOzlxafhE_-9sX4iWqBXrQvkepDy0cgbXHKtITR5Fx5HwR9gXK--xaj2y2QpA4_PQ2ZNvaB3Ngoi_plUnZvQEIr57vI9j0yPLT0qHI4JAukXSD4Dp1Uvs0ZMHEH065i3BO7YvboawfXcIZB3Zg2Iv2vH3tuSMULPeIoe7QJkJENbP35yEp6M_Krz4_lovG4bN6AummsbmD0SXvurvr3HXrP_LHWUC-N8zss_0d02RRCtvSEVhnHH_LrmCX8wVCCyTDxd4LLiCXsZQ8PvMd1TpPW8Eq7L2Xxhs9VUE-BpxSKEd70jy54BwE_RQRD1mP6QjjAb7Cl2q4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این تصاویر با شرح پل راه‌آهن در نزدیکی آق‌قلا در استان گلستان دارند دست به دست میشن.
آپدیت:
منابع حکومتی:
براساس گزارشات منابع محلی اصابت چندین پرتابۀ دشمن به پل آق‌تکه‌خان در مسیر ریل قطار در محدودۀ غربی شهر آق‌قلا در استان گلستان گزارش شده است.
براین اساس حدود ساعت ۱:۳۰ بامداد هفت پرتابه شلیک شده که دو مورد منجر به انفجار بر روی ریل راه آهن  شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76872" target="_blank">📅 02:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WC2aen7D8JlpGEAqGdBtK2vAeFW4Omn1_CsfzZfQvYhTqKTyoAgenoHb54talDMTIkTfoyRWVOlJhfHJWxfm7RMZlGURNCoCpITgy2NCGd1q1b8QoVZTcAXWMpJU7DOyo6MHlJqxMc9FAFem9Qs3owvaLxWTGgnm2oH3wPFPS26oHrfU16MMxbqc_d_IqvaFy6q7YEBk572_uVodszl3wrj_FzJoKTo4U4AEcWMT6GNuG621PB-2b-0Am-8SMZVlodt7Fio8SFvhfttVp4rM-OfKtg4HOEXiMhl3fMwieQm2lUokWpkPzByJSpqlfz0acP8P4ctKELgbV334wtui9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در نخستین ساعات بامداد پنجشنبه گفت که حکومت ایران پس از حملات مکرر آمریکا در منطقه با او تماس گرفته و خواستار دستیابی به توافق شده است، اما او نمی‌داند آیا تهران «شایسته» توافق هست یا نه.
ترامپ در گفت‌وگو با خبرنگاران در هواپیمای ریاست‌جمهوری آمریکا، هنگام بازگشت از نشست ناتو در آنکارا، ترکیه، گفت: «آنها کمی پیش تماس گرفتند، آنها خیلی زیاد می‌خواهند توافق کنند. فقط نمی‌دانم آیا آنها شایسته توافق هستند یا نه.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76871" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های دریافتی تاییدنشده:
استان گلستان آق قلا پنج شیش بار صدای انغجار و نور شنیده و دیده شد
سلام وقت بخیر ، استان گلستان هم زدن ، بالای پنج بار صدای وحشتناکی اومد
سپاه شهرستان آق قلا واقع در استان گلستان و حومه شهر گرگان رو هم زدن
سلام وحید جان
۵دقیقه میش گلستان رو زدن
شهرستان اققلا بدجور لزرید
۵بار لرزید ناجور
سلام وحید جان
شهرستان آق قلا بدجور زدن و مکانشو نمیدونم
کل شهر ریختن بیرون
سلام آق قلا صدای چند انفجار و نور رو ما هم شنیدیم ساعت تقریبا دو بامداد
۲بامداد چهارتا انفجار پشت سرهم آق قلا استان گلستان اخری صداش و شدتش بلندتر بود نور یه  لحظه دیدم ولی کجاخورد رو نمیدونم احساس میکنم دور بود سمت گمیشان رادار داشت قبلا
شاید باز اونجارو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76870" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ozZKe11uJVZ3ZMRjHnkqx7LIuFcbJLswFTfFEDrbrn-ZvNrmull5r35O0uSF9Qb10VlLdef67cMXexwXV94iXRNrW7WCDByM2hlEAi973qtR649uPV2H9mwwCfPjPRphI97OyJ9Dl0GVMl6tvwfqwSO7kcBwEdX9ZcVibVKauQti9MVk9_h1hTDq6Cpv5KT0yOz7CIlbNq9HZbYE8y4Ta3Ckzou2DeHK9-pOfuxUilihkLPqBNuwd7URueNshiZFHK2-QuzoR2uNznp1rermxDjB38Wxd0J7eRHQBFbaLNDXRq2slvwoGzQg7ZruaPGTrk-6-kntEn1FT_jt5qbBUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f66b394713.mp4?token=QD5SIQTu-PDlR_R_E-tL0BNYs0Bp7NSiw39D23plIIIg5YUFJ06y0c6-6Pt3Y2XY6OVmS-8SSWDfgq4hx7kzw5tcKqdJrmaJ356vrGXu2VUjcOOJmUjzMA1MxiwvABC7L20rbHlUfJ6-OKNaeriHRQ3vOrqo7XEZYB-GMzDfIbemCXgbTlJL039H1heNhDvBNoahf7N_2Yn4qEaKSsWuN_tNtdQkuuHILQtBwW7m9IfIYoXFZS9hQr4bJbmP2zc44irn6pFVWCsvGkZPYYP-X2E_ThiiiqT2kB_LB-nHACkeLhaqPgNWzzagrKVhWguvnBFq0q5xK0VL7XgcpsHqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f66b394713.mp4?token=QD5SIQTu-PDlR_R_E-tL0BNYs0Bp7NSiw39D23plIIIg5YUFJ06y0c6-6Pt3Y2XY6OVmS-8SSWDfgq4hx7kzw5tcKqdJrmaJ356vrGXu2VUjcOOJmUjzMA1MxiwvABC7L20rbHlUfJ6-OKNaeriHRQ3vOrqo7XEZYB-GMzDfIbemCXgbTlJL039H1heNhDvBNoahf7N_2Yn4qEaKSsWuN_tNtdQkuuHILQtBwW7m9IfIYoXFZS9hQr4bJbmP2zc44irn6pFVWCsvGkZPYYP-X2E_ThiiiqT2kB_LB-nHACkeLhaqPgNWzzagrKVhWguvnBFq0q5xK0VL7XgcpsHqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر گزارش داد صدای چند انفجار در منطقه شمال شرقی «ایرانشهر» واقع در استان سیستان و بلوچستان شنیده شده است.
این خبر هم‌زمان با ادامه حملات آمریکا به اهدافی در جنوب و جنوب‌شرق ایران منتشر شده و جزئیات بیشتری درباره محل انفجارها یا خسارت‌های احتمالی اعلام نشده است.
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام شهرستان ایرانشهر روزدن
سلام ایرانشهر هم سمت فرودگاه زدن
سمت ارتش ایرانشهر انفجار شده
سلام ایرانشهر سیستان بلوچستان ساعت۱۲:۵۹صدای انفجار میاد
فرودگاه ایرانشهر میگن بوده خودم ندیدم ولی صداش خیلی شدید بود
سلام ایرانشهر سيستان بلوچستان همین الان ساعت ۱۲:۵۰ صدای شدید انفجار و پنجره ها لرزید.
فرودگاه ایرانشهر
پنج دقیقه پیش سه چهارتا صدای وحشتناک تو ایرانشهر(بلوچستان) اومد در حدی که شیشه ها تا مرز شکستن رفت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76868" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYnthkbZtLcdiDOtYCDsedYhmdCleUMmHkDEmA4NRmuEGZMhuz3499eabFY5A94EEb1Anxh0-2n_JPFI6NflBgFb2cw5Ld8PWvVkt4G5yamcW2hvVoh43EeA3ILoPgcm-rKMLrsZYajJDO2dKOPEllIq418D02n4pX0PHcd-SwkHPt-WtjyHT_QZrX_mPlGkXTo_heAEMlVnmYQUPCh32R3zdIJzxRbC657ccwj2Qluu4cW1pQlxy9xfKGm06kcbfFmLhlP4KLjDC5SNaT-A24h1HxWz6pHWk2VBpHy8LsOE-AJix86YkBtLKHATBLng6KNz078w9wnocsZgQMdsbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ نوشته "این در تلافی بمباران دیروز کشتی‌ها توسط ایران است. اگر دوباره اتفاق بیفتد، خیلی بدتر خواهد شد!"
بیشتر از ده تا عکس و فیلم با شرح حمله امشب پست کرده. حتی عکسی که اشتباهی بعضی از منابع پخش کرده بودند:
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76867" target="_blank">📅 01:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=oStKEL3M2PvgcFcpBwrgnQZ0RBDrhWmIaThPX7dZRQe9Tmv05vxJRjaBwgeE5RzLaKGQBtmdehnZmqcEQDRnSE7Yx_sL1E5-V9JtETin1702ivnH3rrK_wcD6GEj8HVUl9qC1k7LRq0zgH0rjy-HvKq3wdxqtRFuBR89vp8m5CAUPCVmgY2wCsRLu0IfSqg499eWvQk7RajqD9llnOiZk8glrhH8kTP7TquBFSBNvBVe5jfd8aQodNw4ZB2LqugOk2FXt3WtfPmStmbP3aq6gi9-wBIv-ieL4lEYkpXS-moRMgjCUEvDtzB8o4SzuYasrNxQbVo_ntmIeKyRO9FnAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b103f9cf8a.mp4?token=oStKEL3M2PvgcFcpBwrgnQZ0RBDrhWmIaThPX7dZRQe9Tmv05vxJRjaBwgeE5RzLaKGQBtmdehnZmqcEQDRnSE7Yx_sL1E5-V9JtETin1702ivnH3rrK_wcD6GEj8HVUl9qC1k7LRq0zgH0rjy-HvKq3wdxqtRFuBR89vp8m5CAUPCVmgY2wCsRLu0IfSqg499eWvQk7RajqD9llnOiZk8glrhH8kTP7TquBFSBNvBVe5jfd8aQodNw4ZB2LqugOk2FXt3WtfPmStmbP3aq6gi9-wBIv-ieL4lEYkpXS-moRMgjCUEvDtzB8o4SzuYasrNxQbVo_ntmIeKyRO9FnAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'همین الان پایگاه نظامی بین چغادک و
#بوشهر
'
پنج‌شنبه ۱۸ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/76866" target="_blank">📅 01:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZUEWZZVylmfno1eHqZj4XEH9NiFgbF2WffDqv5e-FzfSWhW81_0bfxw38T3X17py-O1h0MbaPpJPKkyYrJoUTN6h36H7UPMTH6yDqLngmo9SqxGlLfdwQNCaqkq0IoT2rVUrlF26Z-ZDekGwB1hQLt-lRq81Wm7lwRn-y-izr8RDE3bz9OCSbsGgXPnZTvuRkhFO00oYpGmuWF957UP_FupJ2R-ld3hIgAVPF5kbwb35xZVwJFossJx4Jgo-zGsktNCs8NP9Iqmtjys-WSmh1aktYwOIQvPjAXp3wSBU8FkKdFe1nQith5loCZJP10rl-e-idZkIJaBOJEp6w0gY6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NGUQToCgVIWwgVDJb_XNW2QxD1hnixIiVKFkkCjCjw3sjc7Z6pCsFPyXcKtQVvJUHocYV3XdBqQQTNJeCPRl--wnEEtEHUQ2hzJo3Mj5V9czSWBy2-MvKqXFVADEr_aJVMwP7itEbPUUh7Iqk25h6nyZyWYVrORz6bDPTm6OS98nFuBJHzH-tg3MfeLCeHPLfaLzcJ9_-ef53h0h-y7hDi-T5hvoPnoY3rBf8V1VtxApB5srruFlug0_B3PQqGefA5kGHLxLAuICfcl8S6liT36Fwyy8Z6qpyepFGHZeSEY8b-lVqrfVV7gTbHuUO7v1WDZgcQnnv8_R3Fv5797XSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=DegoHbPJ1zMz0p-d3fPAXvIjX4BpG0KL0c0juWSsOsWIeO95UGOXlz0NuCrj4xSzZ9Vp0PeRxpATagN4PRRIBMDHjzLELBc_c3RVnwOenef8ABlpGlcvRGQvdPBZ2uJQJOIdLQdU3u_3zbDWdPQeM39R6gnkAPhMv8zJkXMImeDY1TSF-Ds_FiNhp2zgJRyehjCPDGnrBSu7I8-lkUXqHIUcqGyFH7zGOYq4CvRYyzHw0_XA4ja438jZWVSWYuQRwp598vtObz3oq9PsTpkK5D5JRkoSRQA1WLte2pFj6DwGFwEyaJYBz9GYWtDV2jYSeJJU6VTDcYPL7EamDOOdgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/349d8753dd.mp4?token=DegoHbPJ1zMz0p-d3fPAXvIjX4BpG0KL0c0juWSsOsWIeO95UGOXlz0NuCrj4xSzZ9Vp0PeRxpATagN4PRRIBMDHjzLELBc_c3RVnwOenef8ABlpGlcvRGQvdPBZ2uJQJOIdLQdU3u_3zbDWdPQeM39R6gnkAPhMv8zJkXMImeDY1TSF-Ds_FiNhp2zgJRyehjCPDGnrBSu7I8-lkUXqHIUcqGyFH7zGOYq4CvRYyzHw0_XA4ja438jZWVSWYuQRwp598vtObz3oq9PsTpkK5D5JRkoSRQA1WLte2pFj6DwGFwEyaJYBz9GYWtDV2jYSeJJU6VTDcYPL7EamDOOdgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر بالا با شرح
#چابهار
پخش شده‌اند.
در خبری دیگر:
خبرگزاری تسنیم گزارش داده است که جنگنده‌های آمریکایی پایگاه امام علی ندسا در چابهار را بمباران کردند.
تسنیم اضافه کرده که تاکنون صدای حدود ده انفجار در چابهار و کنارک شنیده شده است.
برق قسمتی از شهر چابهار نیز قطع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76862" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=KZnC5WH7XWoX7KKlSKff3jaMH5d0aHJzSpui3IMzYDmxd63oTXrz39ugDLGYKq36efqAWQTyQWR-D24Cnc-96nLhHOr0kbN07mKxYhpjJVL29hBd9rbvlAhEMv6nvAdy36aSQ240ULA4h4tAj8lKJ_50SXep55uH2Vd2RUHp7k_3AHOmw8Df0VY9SiJ2xOm30GofsC98fslE9HePTO2vjgbtuP_JU4H2EurE9oXyTDfP-kMb3pJei2Frtda5Z5iJ0deJBIcBNp6fgByfmJauteQuoJzs3rKkRRUfKwYawQh5zVG9gB8ZJzYcSEsyHRGdMHhG_efzWj89OF8CAcD89Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60aeedc6c.mp4?token=KZnC5WH7XWoX7KKlSKff3jaMH5d0aHJzSpui3IMzYDmxd63oTXrz39ugDLGYKq36efqAWQTyQWR-D24Cnc-96nLhHOr0kbN07mKxYhpjJVL29hBd9rbvlAhEMv6nvAdy36aSQ240ULA4h4tAj8lKJ_50SXep55uH2Vd2RUHp7k_3AHOmw8Df0VY9SiJ2xOm30GofsC98fslE9HePTO2vjgbtuP_JU4H2EurE9oXyTDfP-kMb3pJei2Frtda5Z5iJ0deJBIcBNp6fgByfmJauteQuoJzs3rKkRRUfKwYawQh5zVG9gB8ZJzYcSEsyHRGdMHhG_efzWj89OF8CAcD89Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'
#چابهار
، انفجارهای حمله ۲۳:۳۰ چهارشنبه ۱۷ تیر'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76860" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پیام‌های دریافتی:
چغادک بوشهر رو همین الان زدن چند تا انفجار خیلی شدید
سلام ساعت 00:28 دقیقه چندین صدای انفجار در بوشهر شنیده شد
00:30 هوا فضای چغادک 15 تا صدای انفجار
همین حالا بوشهر زدن
حدود پنج تا شش بار خونه لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76859" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76857">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RFMYLbqIpB9d-ln8Ob8Y8Gl4qMkETrilFq1pwycITWHYxNQakaphIefBGjLaBO4cbEPBcB9EQapHhlm45a_AJxSbx1lEPc9KUICL4glQwEb3SY72F6twQJBHa_8q8MrnCCxLn8LcApwaDozSillLWv2JZ5uPzuWy24k_qUS0P9KSDEMeLtqj8jh72HlUv6LM9M3dgA-XNPgJSN6Z9K84_h0vKF_y3ryg0LJxyU6-dnJ6LLPrgvg7YFL_HWS-kfrLUkRafOSzOJFUInXrIAwmzkCKEHQHl2pY5rnPKGrJVCunwaBYkfEIUirr-Hd97vEBe-g0uoQoYg8zM09UiVK2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=VnNNGV7aZ8QhXagSvjvjj9vgSMdcxGXMguGDwDfd2WvXEMw2FpqsRKhMiq9NfEYmnPaumLLS4oMuHhFpTfSMmF1C2NOnFZHsVL6LNacwjhYsUuNSg4SFIiqXhHpUu-d6kaBZu7jFhOIXlR7O91dQN1SomJmJrnQZU7tKZCfk7fBWGwl7VjG45xYYEP4euvdlqIEqA4ME3OTCs5eC1mLmNAYhcpi1GTid6Nl7VskPisqYTYHhbt5IAIXCeWR6AkUkwQaAv-iW7sLol_D0-3bCSPZ6r4ha9U7OWmOLyhVzrm-r9G89MJWH_9D3VVCo3hgJqcA__sUdLDd1meLsEnzE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2188a0f9f8.mp4?token=VnNNGV7aZ8QhXagSvjvjj9vgSMdcxGXMguGDwDfd2WvXEMw2FpqsRKhMiq9NfEYmnPaumLLS4oMuHhFpTfSMmF1C2NOnFZHsVL6LNacwjhYsUuNSg4SFIiqXhHpUu-d6kaBZu7jFhOIXlR7O91dQN1SomJmJrnQZU7tKZCfk7fBWGwl7VjG45xYYEP4euvdlqIEqA4ME3OTCs5eC1mLmNAYhcpi1GTid6Nl7VskPisqYTYHhbt5IAIXCeWR6AkUkwQaAv-iW7sLol_D0-3bCSPZ6r4ha9U7OWmOLyhVzrm-r9G89MJWH_9D3VVCo3hgJqcA__sUdLDd1meLsEnzE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون ریاست جمهوری آمریکا درباره درگیری‌های تازه میان ایران و ایالات متحده، با تشبیه تفاهم آتش‌بس میان دو کشور به یک «معامله» گفت:‌ «توافق اولیه‌ای که ما امضا کردیم این بود که اگر آنها از شلیک به کشتی‌ها دست بردارند، محاصره [تنگه هرمز] را لغو خواهیم کرد، اما ۲۴ ساعت پیش چه اتفاقی افتاد؟ آنها شروع به شلیک دوباره به کشتی‌ها کردند.»
آقای ونس با تاکید بر اینکه در صورت ادامه شلیک به کشتی‌ها در تنگه هرمز آمریکا ایران را نابود خواهد کرد گفت: «حالا، رئیس‌جمهور ما گزینه‌های زیادی را در نظر دارد. بدیهی است که من نمی‌توانم بگویم امشب چه اتفاقی خواهد افتاد، اما رئیس‌جمهور خیلی ساده به آنها گفته است، تنگه هرمز باز خواهد شد. این بدان معناست که نفت و گاز به سمت مردم آمریکا جریان خواهد یافت. به همین دلیل است که می‌بینیم قیمت نفت و بنزین شروع به کاهش کرده است.»
او گفت که تاکید ریاست جمهوری آمریکا بر باز ماندن شریان حیاتی مهمی در حمل انرژی جهان است و «این چیزی است که ایرانی‌ها باید بدانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76857" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان شش انفجار در بندر جاسک
ساعت ۰۰:۲۴
سلام وحید جان جاسک رو زد دوبار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76856" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B98YKYeX_7EA_E02yHy7KehIVuSl2vV4TQ4BPjHm920PNKVOKZGkbAbQC_gz4NQqABH3RrwakWNKEWJD3P7FUaTyQf_b3U8ba1o-1M9EzY7KEz2hMliGuC2fEGRLL9wVY8VSf2bJui1Lq9O4OepZQRKnFHt06hZbr8FxAViUxKC9mtrSf2QT2pz2ieMmOqMV9E5KO6al15itJX4l5HHJvhGngUTVQ28fVXH5RqVNsgRnZQe8j8sGL4qaNZLV5SAP86CQwjHNcySNTEdPYBj684p48lmxOAuKQQw2XDRjn6tm-QdC4qjd3aqTMqAF8J6bpZFKrdXbpMoo1E3DDVu2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=OFvhuZjz6gP94kMFa-HGm0WheT2yADI6NY2rB4cOeEiT8Fuww8tdAmEvBTfXki0ZQR_L8eU4HJJVm7U4ULI7Vnxoa026yFftzSu3AAezhkzqSLRTI4orKjgbBwWdwV0BmCCo_ZY36Anrv7qneiP5_Z7jOX0UmPd3cQH8yso1j2CXOWNdDfC7GzNTK_qcSgrRpqECebOSzuofOL1Y3GZZdQFZ8dzh2xL59coKTFi_YiJZzqoUQ6YlqIhY-9t_QzddtruanKtHOCwjD9Pl9haRrYf933jV1uKt1y_EBvZph0Lxm7RxUGQMJY1q_YIGtlWTSeQdf6sLsS_NKUsFfFfzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8512e0af1c.mp4?token=OFvhuZjz6gP94kMFa-HGm0WheT2yADI6NY2rB4cOeEiT8Fuww8tdAmEvBTfXki0ZQR_L8eU4HJJVm7U4ULI7Vnxoa026yFftzSu3AAezhkzqSLRTI4orKjgbBwWdwV0BmCCo_ZY36Anrv7qneiP5_Z7jOX0UmPd3cQH8yso1j2CXOWNdDfC7GzNTK_qcSgrRpqECebOSzuofOL1Y3GZZdQFZ8dzh2xL59coKTFi_YiJZzqoUQ6YlqIhY-9t_QzddtruanKtHOCwjD9Pl9haRrYf933jV1uKt1y_EBvZph0Lxm7RxUGQMJY1q_YIGtlWTSeQdf6sLsS_NKUsFfFfzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'بوشهر، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۴۵'
تصاویر دریافتی از شهروندان
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76853" target="_blank">📅 00:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=sDcE5wSQl2bRULkcYUXTrEUoNcO6Eie1Ir5PQBkIEFX4zi1EXtAExTpdpog8XZOubtQHU2pj_NanrMb9GWxXD4hkfaKW-hrXF8IVxemOYZrPtoytD6WrkSeaEqPQSHu9ysPAXrQo9CgJS2_3-4RNM887kKiA70OvOgYnkcLbZczStkqr2ylGIsxzatGvvqbEnJg-xxhXQvK_oF1lIKMgeNTspNXzdSy-YqwOPW6ORHRhCk57-3g1vNRx2AP438xym0zS8PYJm6nHkT2GwJfeaMZkjSlrO4DDWhz6OwVPHiUF7YCOyaQa9EtYAYDO5tT1oIjlsS1h04ub3AH2noJmMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f98b02764.mp4?token=sDcE5wSQl2bRULkcYUXTrEUoNcO6Eie1Ir5PQBkIEFX4zi1EXtAExTpdpog8XZOubtQHU2pj_NanrMb9GWxXD4hkfaKW-hrXF8IVxemOYZrPtoytD6WrkSeaEqPQSHu9ysPAXrQo9CgJS2_3-4RNM887kKiA70OvOgYnkcLbZczStkqr2ylGIsxzatGvvqbEnJg-xxhXQvK_oF1lIKMgeNTspNXzdSy-YqwOPW6ORHRhCk57-3g1vNRx2AP438xym0zS8PYJm6nHkT2GwJfeaMZkjSlrO4DDWhz6OwVPHiUF7YCOyaQa9EtYAYDO5tT1oIjlsS1h04ub3AH2noJmMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: 'چابهار، چهارشنبه ۱۷ تیر حدود ساعت ۲۳:۳۰'
لحظاتی پس از حمله آمریکا
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/76852" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان بوشهر ساعت ۱۱:۴۸ دقیقه بد زدن
بوشهر ۲۳.۴۸ یک بار انفجار
سلام وحید جان
بوشهر ساعت ۲۳:۴۸ صدای دو انفجار اومد که از صداهای صبح شدتش بیشتر بود
سلام بوشهر الان صدای انفجار اومد
اقا وحید بوشهر همین الان زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76851" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار بندرعباس
باهنر
بد داره میزنه
بندر دوتا صدای انفجار امد
بندرعباس منطقه ۴ انفجار های شدید و پشت سر هم
بندرعباس ۳ تا انفجار پشت هم 23:45
سلام الان ١١:٤٦ دو انقجار با موج بلند در بندرعباس
بمبارون بندرعباس شروع شد وحید جان
ساعت ۲۳:۴۷
اقا وحيد الان بندر عباس صدّا چند انفجار شديد كه پنجره ها لرزيدن
ساعت 11:45
چند صدای انفجار بندرعباس ساعت 23:46
سلام صدای سه چهار تا انفجار شدید بندرعباس اومد
بندرعباس الان چندین صدای انفجار پشت سر هم اومد
سلام
23:47
صدای 6.7 انفجار از دور
قشم
سلام بندرعباس صدای انفجار مهیبی اومد
بندرعباس سه تا انفجار پیاپی و مهیب
صدای بیشتر از ۸ تا انفجار این سمت باهنر و اسکله اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76850" target="_blank">📅 23:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cb_JQc_9bn7YQLvCLaPweCcrK1mf5nHc9t1iqevvIkFDa7f7xwCp2ozolxwWpCmOvfZffqE5Bnm_4dWs9kvhVzqSklSab6PRa2EUf6mivbDYomJeypAoFewW34LM5K1sIQjLC8oVAp4leTqhdz5F0rAvQRZSj4gMWspLLxrp9RkIRDX4OGA-AdpBly8bGFKvXNnjtqHvwLsWcr_WY0rrmRnTrA3jT-UzHjlAw3t31PcW6q10_JswDiNW-kg1IHheq2BGqjmGbOV23SQ0DW4jGeTnE12bBKCeuboTVDMS6e_u2kBJCHDIS8pgVmJXieWj4A1yoDTF_OfaXFwXXJ1XLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی آمریکا اجرای حملات تکمیلی علیه ایران را آغاز کرده‌اند تا توانایی این کشور برای تهدید آزادی کشتیرانی در تنگه هرمز را بیش از پیش تضعیف کنند. ایالات متحده ایران را بابت تعرض بی‌دلیل اخیر علیه کشتیرانی تجاری و خدمه‌های غیرنظامی که آزادانه در یک آبراه حیاتی بین‌المللی تردد می‌کنند، پاسخگو می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76849" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
صدای انفجار چابهار
فکر کنم کنارک بود
چندین صدای وحشتناک  10تا بمب زدن
۵ تا صدای انفجار شدید اومد
چابهار
داداش الان چابهار رو هم زدن
7 و 8 تا صدا اومد
ما تو روستای رمین هستیم برقا رفت و صداش اومد خونه لرزید
سلام کنارک وحشتناک صدای انفجار اومد
چابهار زدن چند تا انفجار شدید
ما کمب هستیم واقعا درهای خونه ما بشدت لرزید
صدای انفجار از زمان جنگ هم بلندتر اومد
دود غلیظی بلند شده که تو شب هم کامل معلومه
از سمتی میاد که پایگاه سپاه اونجاست
البته ممکنه نقطه زنی باشه
الان 3 4 بار دیگه صدا اومد
جدا از اون اولیه
مجدد زدن با جنگنده
فک کنم اسکله سپاه بود چابهار بود صدا نزدیک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76848" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fvTDsof6Uo2FwYR1fV78TZqs-ala0620lV24xDdul8MfFP-5rKWRN17EKluvAkx_Ksl2HUkl8pk7nyPKbXxBqvtxHAHTs3fhJdA5yg6GM6_pXDFpD1FjxKBHqjzeHCGJB2wDj1BCvla4t_B_FzwGA9a1w5FkZI2zP49ig3TT2eKS3FX79_NSEUa-yLsmB8ZhA7zDxUhr-cQA7MdDQkpWDYvJVekmmgZCKFK5zPvyHmy-C0JDMeoj_EBGmOcPD2_ZUAOdH5z4mEFhGqc2pHDgjrvZ8RbtzHs9DK0KmKMH0ru3jDmSPk8r8FAstwaiQq4m1URY0e49lK8najRsL26WkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری‌های فارس و مهر شامگاه چهارشنبه ۱۷ تیر گزارش دادند که حوالی ساعت ۱۱:۱۵ شب صدای چند انفجار در بندرعباس و شهرستان سیریک شنیده شده است.
بر اساس این گزارش‌ها، شماری از این انفجارها از سمت دریا و در محدوده ساحل غربی سیریک به گوش رسیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76847" target="_blank">📅 23:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76846">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">(
⚠️
۴۰ دقیقه، ۸۰ مگابایت)
کل سخنرانی ترامپ در نشست خبری اجلاس ناتو با زیرنویس فارسی ماشین
دونالد ترامپ، رییس‌جمهور آمریکا، با اشاره به رهبران جدید جمهوری اسلامی گفت «ممکن است آن‌ها هم از بین بروند». او هم‌زمان تاکید کرد که درگیری با ایران طولانی نخواهد شد، اما واشینگتن در صورت لزوم به حملات خود ادامه می‌دهد.
ترامپ روز چهارشنبه پس از پایان نشست سران ناتو در آنکارا، در کنفرانس خبری خود از نحوه مدیریت جنگ با ایران دفاع کرد و درباره رهبران جمهوری اسلامی گفت: «آن‌ها رهبرانی داشتند؛ دیگر نیستند. حالا مجموعه دیگری از رهبران را دارند. ممکن است آن‌ها هم از بین بروند.»
او افزود: «ممکن است من هم کشته شوم، چون من هدف شماره یک آن‌ها هستم.»
رییس‌جمهور آمریکا در بخش دیگری از سخنانش با اشاره به تشدید تنش‌ها میان تهران و واشنگتن گفت: «فکر نمی‌کنم جنگ دوباره آغاز شود. آن‌ها چند کشتی را هدف قرار دادند و ما خیلی شدیدتر پاسخ دادیم.»
ترامپ تاکید کرد هرگونه درگیری احتمالی «خیلی سریع» پایان خواهد یافت و افزود: «هر اتفاقی که رخ دهد، خیلی سریع تمام می‌شود و فقط اوضاع را امن‌تر خواهد کرد، از جمله برای نفت. ما به دنبال یک درگیری طولانی‌مدت نیستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76846" target="_blank">📅 22:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXQ-C-T_CXRMz8wjFyJiBcnxc4SmUxZrgAMyP9wSvwchPkcQZI7Qo_Uj55Mzz3PMukv5qrnaEnXwScXb1pvJHs2DCtUio9g7uCH78V6WBrR6qJ9jFt0Iuyq9lZBFNoyIC5JcYd8jN-0UoZIIM1vY8WXwdtJKxZyI6uTGSZEFyThwBXWsYy2Fl2uy9-tS6TFSsolVx9ZwFpV_ZBsSpg9SQBGaesetz0qXq4up1kN4QLjyoHjicokiVnKz8Kwe6N1SfRMxm2Eip3tSPu8gxcsEA8nps5jEauMIK0RAl-6_Z2n0t-Zjzlr_DtBR9fUe-TE6TbyDJ8SbnTD-bs7CCrO1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی ارتش جمهوری اسلامی با انتشار بیانیه‌ای اعلام کرد که در پی حملات آمریکا به مناطقی در جنوب ایران، هشت تن از نیروهای هوایی و دریایی ارتش در بندرعباس و بوشهر کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76845" target="_blank">📅 20:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AY9SiLhzooD-a3e_zAmaYYlVx3Sb2u8s-5XFcoTtJGYafwfIwPFQW3bnPH_ksqbTxKmvsNr3Ohj0r_sL8y4KkttHgYVB-z20Ytyh9ZbrSiv4MBH-YQR9TUjI_ldUBY0UrAGg8SxUlaC8eax1CLdAcK17Zwj7jSS3M5iqZCbB9kQoeRRkqYu3X4CLd00eALrzG-ugVlP7BF3cbsBDWuWt2nCj6s_p2D4RsA6m1Y51hCVMEviOAKr1bHfyoNQfiyknBJfPapR7LjbmClhtpxTF7vES0vGBQUubrp1alifM9YUxRnFTnGLHKzsA9ay5IOIDlrgPQ5GuGaivI1mVnrFKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=vNq0iZdkgU8PxEl21-2BCyvVa7A0tcQBOMkTQjoCXVFqnQ1bMZhv4PWqpQdTn8UGVgrrdgaiXh_ItxhfGNHvkyJXjHcNAgWf06R7fZ-T9BVBnOACrPlbC0A5Zda8L_8vJ-0vxa6k2fhr6vHSyZbfd-DjJdaB4Ci5K1JdnKTuqugNqBfRvBqMWaOE0iSNcfkE5PmEdx1MxAunffC3bcMopaKf60c5VxG9jVixH8yA6XY6dLEwzCgHFl2QibqZNW9Z18_xnWoz3zJJCTK4E65Jm1hQ8G3I5MwEQluW5xLrETrWD11_qyv75aNu6m9x23HT_qLnFqX_xhKipYR1T5bnwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffbf0a91d4.mp4?token=vNq0iZdkgU8PxEl21-2BCyvVa7A0tcQBOMkTQjoCXVFqnQ1bMZhv4PWqpQdTn8UGVgrrdgaiXh_ItxhfGNHvkyJXjHcNAgWf06R7fZ-T9BVBnOACrPlbC0A5Zda8L_8vJ-0vxa6k2fhr6vHSyZbfd-DjJdaB4Ci5K1JdnKTuqugNqBfRvBqMWaOE0iSNcfkE5PmEdx1MxAunffC3bcMopaKf60c5VxG9jVixH8yA6XY6dLEwzCgHFl2QibqZNW9Z18_xnWoz3zJJCTK4E65Jm1hQ8G3I5MwEQluW5xLrETrWD11_qyv75aNu6m9x23HT_qLnFqX_xhKipYR1T5bnwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری فرانسه، چهارشنبه در حاشیه نشست ناتو در پاسخ به خبرنگاران گفت حملات جمهوری اسلامی به پایگاه‌های آمریکا در خلیج فارس، توافق موقت را نقض کرده و تهران در انجام این حملات اشتباه کرده است.
امانوئل مکرون در عین حال گفت انتظار دارد نشست‌ها در چارچوب آتش‌بس ۶۰ روزه میان آمریکا و جمهوری اسلامی ادامه یابد.
@
VahidOOnLine
فریدریش مرتس، صدراعظم آلمان، نیز در حاشیه این نشست گفت: «ما به دونالد ترامپ گفته‌ایم که باید یک توافق پایدار با ایران حاصل شود، اما این ایران است که مسئول آخرین نقض توافق موقت آتش‌بس است.»
@
VahidOOnLine
دبیرکل ناتو، حملات تازه آمریکا به مواضع جمهوری اسلامی را «کاملاً ضروری» خواند.
مارک روته، پیش از نشست سران ناتو در آنکارا به خبرنگاران گفت وقتی آتش‌بس برقرار است و جمهوری اسلامی «عملاً آن را نقض می‌کند»، واکنش قاطع آمریکا اهمیت حیاتی دارد.
روته روز سه‌شنبه نیز گفته بود هرچند جمهوری اسلامی در حوزه موشکی و هسته‌ای تضعیف شده، ناتو همچنان باید نسبت به تهدیدهای آن هوشیار بماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76843" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LmOuIB3RObjABoryJGzY61R55qlw_H8ux3jW_UvyAvMkRYk8XJ0I2iz4J08O4i-XFVlgr8rOEVOQjwqbKvX0MZ2gEQzUPAwNOOUrX2CZMy0qPdHVmzXjzxCdzBlrqDuDaH-tT6tBhIyK_xqyjW-YP-GXVA__jNa1m-aZNOkBxjIgagl0d9EXKzQKQlEY11DB3k0-v-bdfpweYivhVQOv5nwjnup82BcU-6rgWIQnH7CpUIQYNHQqtllDo1adML1hypcLk8E6RIHDQmslE0uYmIeRG7TAda9BKoeyn4TWKYlpik_aAObKmgC2Se-kgG30FKoSjYMg77ddrtFJEdyFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TWA7sRSIaLbi4ReISRUfd6hMvkEeBVgbj1lzBKa-9mRxJLyoWBLO-HzGeSpGKCUeIpzC-TOdaq5LhwIyYJnJfLmhVGU04QZhg4xnekw78-5_grU46lTsfREGb2zb97Lq4004Rq7HdOGlfOfF1Vr7UZ5C41DnNPqTu1hhfU5j4fh10nHbWpUW_DFpPFNxt2mO23iwqgbBKv6R8gY-Tl5-TbzjqieVG2kXhuNNeVIRA7oBmaa3DPcJGy5lkPzkG1-_4zzNtz9m-2wcqe-k2N77cAevTfS59lEIo99itJ85d5mX9Z5IXCrWtU8zfmVOYeaX3ntRdQxjnQmz2x4lK_JsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GFs03B4iq-JhLxuiqu7toXFDnzYT-7vy1sJCOJkGgENE4ahS6Clnuu5wiagoxEpd39a4LclIONLTI-_yGMOkSWT2N7-D_-khTykuYH6S8DRpqb88vNxxlVcH5VFbjuLkAk_wPad6GU3tFtQbSlnZd_tQHaTs2ZC8pnSM5N5MFAT1axVXYis67Ailde8MrEqNrcguiMcAk47hCjFSwHK4SsSmtqt-I6axwRxOILF4docH5glMc3PqGHmWUp1GgTPNihUYXKEET2T4vCWL0-FcINw89JfHKNBooDKGtTWn_XDuBW9Vdf1ZvzosQ21joiic874VFAt_h_7f5eT_eQ0k6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cvwlA4Vi6l957V3DaVNyG2NAlANj7Uxy6ZQhIHZ24oz7qUdQMjrvcFQ_zrMjrvJZKj_vzZuT__mQYbbszt_Xa67vz0vWY7TQmL8S38zmTqDeC-ISDBgCjPXBvbA64hWqgdqfF96mZkzzGahBUsesmR8rWPlek1NllpQn_i415sjd0bS_AXe3Ncbgfm42T76zi8oFy1B7LBLUcLqueqkQ-UewFFKG4pnoNxIQOqS2xGveyfiYh6lmJkjTo2nnIzJgZ8Dy0DHuZTaGek_ybTNKHkUsCIZ1oAVPNhxNo5HDN5nJwD72e5nKu5TXp2ae1hOjZH5uI_bzAneEbQI2maIMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DHtYEJkqvLRwX21tR1-rfvg3iT-a_haBAbl1X-4TiDr8QG-C6FanQdXP7G64F9crh_qFGWszC79Bk0nbOBcsVJhUMgdpJjtK6C9M1XbJFEr2WcXkHKWrGixopl4to0D2zlr_SZNtJwsI7T0k66cI3s19bxRkQQvwjYPqpnkmStU0MCn8KLCWplYluxL-HKQKSI-vzoCdtVWWFY508rX89jym9k5lssEmz8vbYiHPKdvLaA1WWkEt3Te7S-bxoB3QmSYNOgkns6qpn28PEM2zROk7ePpmTKc1qxOJuVXwkM8ek73srQPtMnmQ-KSVX3Gnt9lkxcQilPFXZuNaJtaT7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=Ylm6iJe1yt41CfROZyKMnUDD0nBpNeO_qcL7lZdGByORavPJE6joHpx3DD7QX1qYuYn4tqIR1Kjuyg7RWWqgEhbNsJ4FbaxMBTfYRQFJUhy3kNr-PdtmHYlltH_kr7jYDyS_vU8AstaXBcc3y62tzJphi7RC9pTTeDphzBfYcybn1ZBtHwE7wo57DA6JGdz2UJz8VuQLUP_Niz0HsLMqLRJEC9n3Y1i3j1hlojRHSG6SUDEjoXpCpVaDjZs3NSjAKVyjrJtVvcq2I1DNLQOrvDH2rMC8DTyT35F2MJkWX1Rxttyyaq7QlnMznT35skc6tpuh6v58acfZiyrBSLN79A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6cd91b041.mp4?token=Ylm6iJe1yt41CfROZyKMnUDD0nBpNeO_qcL7lZdGByORavPJE6joHpx3DD7QX1qYuYn4tqIR1Kjuyg7RWWqgEhbNsJ4FbaxMBTfYRQFJUhy3kNr-PdtmHYlltH_kr7jYDyS_vU8AstaXBcc3y62tzJphi7RC9pTTeDphzBfYcybn1ZBtHwE7wo57DA6JGdz2UJz8VuQLUP_Niz0HsLMqLRJEC9n3Y1i3j1hlojRHSG6SUDEjoXpCpVaDjZs3NSjAKVyjrJtVvcq2I1DNLQOrvDH2rMC8DTyT35F2MJkWX1Rxttyyaq7QlnMznT35skc6tpuh6v58acfZiyrBSLN79A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، گفت ارتش این کشور احتمالا امشب دور تازه‌ای از حملات علیه اهدافی در ایران انجام خواهد داد.
ترامپ پیش از دیدار با ولودیمیر زلنسکی، رییس‌جمهوری اوکراین، با اشاره به حملات جمهوری اسلامی به شناورها در تنگه هرمز گفت: «آن‌ها چند پهپاد و یک موشک به سمت شناورها شلیک کردند، در حالی که این شناورها حق داشتند در تنگه هرمز حضور داشته باشند. به همین دلیل دیشب بسیار سخت به آن‌ها حمله کردیم.»
او افزود: «احتمالا امشب هم بار دیگر حمله بسیار شدیدی انجام خواهیم داد. فقط کمی از قبل به آن‌ها هشدار می‌دهم.اما باید ببینیم در نهایت اوضاع چگونه پیش می‌رود.
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، با تاکید بر نقض مداوم آتش‌بس از سوی جمهوری اسلامی، گفت: «آن‌ها هرگز تحت توافق ما به سلاح هسته‌ای دست نخواهند یافت. اما نمی‌دانم اصلا توافقی در کار خواهد بود یا نه؛ شاید این مسئله را بدون توافق حل کنیم.»
ترامپ گفت جمهوری اسلامی «هر روز» آتش‌بس با آمریکا را نقض می‌کند.
او افزود: «آن‌ها دروغ می‌گویند، تقلب می‌کنند و آدم می‌کشند.»
ترامپ بار دیگر از توافق هسته‌ای دوران ریاست‌جمهوری باراک اوباما انتقاد کرد و آن را «یکی از بدترین فاجعه‌ها» خواند.
او گفت: «توافق ما دیواری در برابر دستیابی به سلاح هسته‌ای است، اما توافق او [باراک اوباما] جاده‌ای به سوی سلاح هسته‌ای بود.»
@
VahidOOnLine
رئیس‌جمهور آمریکا با انتقاد شدید از مقام‌های جمهوری اسلامی آنها را «بیمار» خواند و گفت ما به آنها گفتیم بروید و مراسم تشییع جنازه خود را انجام دهید. آنها به جای آن، دیروز شروع به شلیک موشک به کشتی‌ها کردند.»
دونالد ترامپ که در کنار مارک روته، دبیرکل پیمان آتلانتیک شمالی، ناتو، در آنکارا با خبرنگاران صحبت می‌کرد با اشاره به حملات هوایی شب گذشته اضافه کرد: «ما هم دیشب ضربه سختی به آنها ضربه زدیم، خیلی سخت.»
@
VahidHeadline
ترامپ گفت: «آن‌ها درخواست یک وقفه کردند. می‌خواستند برای مراسم تشییع جنازه خامنه‌ای بروند. من گفتم این فرصت را به آن‌ها بدهید. و آن‌ها دو موشک شلیک کردند. منظورم این است که این دیوانه‌وارترین کار بود.»
رییس‌جمهوری آمریکا افزود: «ما می‌توانستیم آن‌ها را بکشیم؛ بنابراین فکر می‌کنم باید از این زاویه هم به موضوع نگاه کرد.»
او همچنین گفت جمهوری اسلامی درخواست کرده بود که آمریکا آن‌ها را نکشد و افزود: «ما گفتیم قرار نیست شما را بکشیم. هیچ کاری نکردیم. در واقع، ما امنیت آن‌ها را هم تامین کردیم.»
@
VahidOOnLine
ترامپ در جریان نشست خبری در آنکارا، جمهوری اسلامی ایران را به اشتباه جمهوری اسلامی «ژاپن» خواند. او بار دیگر اشاره کرد که در جریان جنگ، جمهوری اسلامی ۱۱۱ موشک به سمت ناوهای هواپیمابر آمریکایی مستقر در منطقه شلیک کرده است. فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از این اعلام کرده بود که این موشک‌ها رهیابی شده یا به هدف نرسیده‌اند.
@
VahidOOnLine
ترامپ گفت که حملات اخیر ایالات متحده به ایران «تاثیر فوق‌العاده‌ای» داشته است. او گفت که در این حملات، سامانه‌های راداری که تهران در حال بازسازی آن‌ها بود، منهدم شده است.
ترامپ هشدار داد که آمریکا می‌تواند تنش‌ها را بیش از پیش افزایش دهد. او گفت: «تاسیسات تولید برق، نیروگاه‌های برق... اگر مجبور شویم، آن‌ها را از کار می‌اندازیم» و افزود: «تاسیسات آب‌شیرین‌کن... اگر لازم باشد آن‌ها را هم هدف قرار می‌دهیم. دلم نمی‌خواهد این کار را انجام دهم.»
او همچنین اظهار داشت که ایالات متحده می‌تواند جزیره خارگ، جزیره‌ای با اهمیت استراتژیک در سواحل ایران را «تصرف» کند و گفت که در آن صورت، ایران «هیچ کاری» نمی‌تواند در برابر آن انجام دهد.
@
VahidOOnLine
ترامپ گفت جمهوری اسلامی «هر روز توافق را نقض می‌کند» و به همین دلیل آمریکا «چاره‌ای جز ادامه حملات» علیه ایران ندارد.
ترامپ با اشاره به توافق آتش‌بس، گفت: «آن‌ها هر روز توافق را نقض می‌کنند. دروغ می‌گویند. تقلب می‌کنند. مردم را می‌کشند.»
رئیس‌جمهوری آمریکا همچنین با انتقاد از دولت‌های پیشین ایالات متحده افزود: «در ۴۷ سال گذشته هیچ رئیس‌جمهوری کاری در برابر آن‌ها انجام نداد.»
@
VahidOOnLine
ترامپ بار دیگر تاکید کرد که ذخیره اورانیوم با غنای بالای ایران، تنها به‌وسیله تجهیزات آمریکایی قابل استخراج است. ترامپ با اشاره به حملات تابستان سال گذشته، یادآوری کرد که این مواد زیر آوار تاسیسات و زیر کوه باقی مانده است.
رئیس‌جمهوری آمریکا، با تاکید بر این‌که نیازی به اعزام نیروی زمینی به ایران نمی‌بیند، گفت: «وقتی که آن‌ها کاملا از بین رفته باشند یا توافقی حاصل شده باشد، برای خارج کردن مواد هسته‌ای می‌رویم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76833" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BUZAccBF5s05AkesZAKdjhVOWgPyGwWguLZm3WEmsyP-_dkKQ5sS_jfQkPgzIL_x4CykyaBg9mKT6Fu7tBp4V2HIJn3Oa6TiTdvvU3UPyON-4HD1DWYKCiRC9nYF2EhQvFu4R91A85mI-Slvyn7aGhNIjDm5a5ukJ0lcwMad_KglVIUth35kHImrkQx7wS1XiLNH1c46cG7n91eyyPRzL5M2fDIs_GmHJEdcQrq9M3EC_GutVlqRJngtGSK-rod7tKIYLX_qpumCpjQyc7RFWWiags_1XThOJ_zwY1bJJnSXTNTvJW4ruH0notSEF_MSFjUFm27_Hap0FW60h9S5pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل هم‌زمان با گذشت شش ماه از سرکوب خونین اعتراضات سراسری دی‌ماه ۱۴۰۴ در ایران اعلام کرد با توجه به این‌که در ایران «هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد»، دادخواهی قربانیان این سرکوب باید از مسیرهای عدالت کیفری بین‌المللی «به‌عنوان اولویتی فوری و غیرقابل مذاکره» دنبال شود.
دیانا الطحاوی، معاون مدیر منطقه‌ای خاورمیانه و شمال آفریقای عفو بین‌الملل، در بیانیه‌ای که این سازمان روز چهارشنبه ۱۷ تیرمنتشر کرد، گفت: «با گذشت شش ماه از زمانی که نیروهای امنیتی ایران طی دو روز، هزاران زن، مرد و کودک را به‌طور غیرقانونی در سراسر کشور کشتند، ناتوانی جامعه جهانی در برداشتن گام‌های مؤثر برای پیگیری عدالت بین‌المللی غیرقابل توجیه است.»
الطحاوی افزود: «این بی‌عملی به تداوم چرخهٔ سرکوب مرگبار کمک می‌کند؛ چرخه‌ای که در آن بازماندگان و خانواده‌های قربانیان از عدالت محروم می‌شوند و زمینه برای وقوع جنایت‌های بیشتر فراهم می‌شود.»
این مقام عفو بین‌الملل همچنین بار دیگر هشدار داد که تلاش‌های دیپلماتیک برای دستیابی به توافقی میان آمریکا و ایران نباید باعث نادیده گرفتن نقض گستردهٔ حقوق بشر در ایران شود.
به‌گفتۀ الطحاوی، مقام‌های جمهوری اسلامی تاکنون هیچ هزینه‌ای بابت استفادهٔ گسترده و غیرقانونی از نیروی مرگبار علیه معترضان نپرداخته‌اند و همین مصونیت از مجازات، آن‌ها را در تهدید به سرکوب‌های خونین بیشتر جسورتر کرده است.
به‌گفتهٔ سازمان عفو بین‌الملل، «با توجه به این‌که در ایران، به‌دلیل بحران ساختاری مصونیت از مجازات، هیچ چشم‌اندازی برای تحقق عدالت وجود ندارد، باید مسیرهای عدالت کیفری بین‌المللی به‌عنوان اولویتی فوری و غیرقابل مذاکره دنبال شود».
سازمان عفو بین‌الملل در بیانیه‌اش بار دیگر از جامعه جهانی و کشورهای عضو سازمان ملل خواسته است بحران حقوق بشر و مصونیت از مجازات در ایران را در صدر دستور کار خود قرار دهند، از ایجاد یک سازوکار مستقل بین‌المللی برای تحقق عدالت در مورد ایران حمایت کنند و از شورای امنیت سازمان ملل بخواهند وضعیت ایران را به دیوان کیفری بین‌المللی ارجاع دهد.
ماه گذشته، رئیس سازمان عفو بین‌الملل نیز نسبت به تداوم سرکوب داخلی در ایران ابراز نگرانی کرده و هشدار داده بود توافقی که صرفاً به‌طور موقت جنگ را متوقف کند اما حقوق بشر را نادیده بگیرد، خطر آن را دارد که به پوششی برای تداوم مصونیت از مجازات، اشغالگری و سرکوب تبدیل شود.
عفو بین‌الملل می‌گوید توافق ایران و آمریکا، موسوم به «تفاهم‌نامهٔ اسلام‌آباد»، تنها در صورتی می‌تواند به صلحی پایدار منجر شود که حفاظت از حقوق بشر، پاسخگویی عاملان نقض حقوق بین‌الملل، جبران خسارت قربانیان و تضمین عدم تکرار این نقض‌ها نیز در کانون توجه قرار گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76832" target="_blank">📅 20:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tTD2euJr0w66V9UzYeFiirfK2zt9puNP4e_7z-E12R7Y_8XGLBPzKfZVuTapG5MwNcXEEyt_l-Q5hcLSEMY-pssjvtvpg-GfR3_KSO3VubsNtFWZ2AcXxhNfZWtQcTPTzObXVj_Io4Mt_XskT9s8G1Njg8pjmkZJQYuT5PbWfJCZsvxC9awPSmc6tBfs5A3PSSnRkSdNt47LshUil1v5PtlTHqSEQJXnVxDUwjApnk_yAOqMih10n1AZMBVQy6d_04X1IFZDh1aO8o6s1dhPLK1ImVVfRiqqXtjfRvo_THLk-5aLXH-IV_5953v9bQgfolOCcG94SWmWHKBvb1ZJ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TDTjP9YcDcYL9Uqno39wBZvURtjRehPPUupE-atPChnQxIJTukXBKp4uAU9ZM_iUZ2lVwATS-hTEkzPLvU7q_wzxvW5aBs7ub9lE798HZ__azkyNxB_CkkRvQXuuZGrUXHWrC8n_e6FnzbjNGNOlZO9HjIlpbNyAw6zvj8g9DNfbUD-UK1HzQI3Jx_JGxItMpfzLG4mbxELKVS97-TRYsVvN_QNUJ8UIkzrsVS60LZ72h-Ctqd8Abff59nLk2UmUwzk5LKdWw_FfD9acbSjoyEhQpQ7CPEN1zeF_T8ykXQUyVXB11Rj6T0m9GFklqLGpl1sQYXKxbWFw8R40ANcq7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، با اشاره به مراسم دفن علی خامنه‌ای، گفت جمهوری اسلامی به جای حرکت به سمت کاهش تنش، حملات موشکی به شناورها را آغاز کرد و آمریکا نیز در پاسخ، حمله‌ای گسترده علیه جمهوری اسلامی انجام داد.
ترامپ که در دیدار با مارک روته، دبیرکل ناتو، در آنکارا سخن می‌گفت، اظهار داشت: «ما گفتیم بروید مراسم تشییع خود را برگزار کنید، اما آن‌ها به جای آن، دیروز شروع به شلیک موشک به سمت شناورها کردند. به همین دلیل، دیشب بسیار سخت به آن‌ها حمله کردیم.»
رییس‌جمهوری آمریکا همچنین جمهوری اسلامی را «بیمار» توصیف کرد و گفت: «آن‌ها بیمارند. یک مشکلی دارند.»
ترامپ افزود حملات آمریکا «۲۰ برابر شدیدتر» از حملات تلافی‌جویانه ایران بوده است و گفت: «باید سرطان را از بین برد.»
@
VahidOOnLine
مارک روته، دبیرکل ناتو، در نشست خبری مشترک با دونالد ترامپ، رییس‌جمهوری آمریکا، در آنکارا، از حملات شبانه آمریکا به جمهوری اسلامی حمایت کرد و گفت این حملات «کاملا ضروری» بوده است.
روته با اشاره به حملات آمریکا افزود: «این یک پاسخ بسیار قوی بود و من در این موضوع با شما هم‌نظر هستم.»
دبیرکل ناتو همچنین از مواضع کشورهای اروپایی از عملیات نظامی آمریکا علیه جمهوری اسلامی دفاع کرد. او این اظهارات را در واکنش به انتقادهای ترامپ از برخی اعضای ناتو، از جمله بریتانیا و اسپانیا، به دلیل محدود کردن همکاری نظامی با آمریکا مطرح کرد.
روته گفت: «می‌دانم که شما درباره ایران ناامید شده‌اید، اما به نظر من این‌ها مواردی استثنایی هستند.» او افزود: «پنج هزار هواپیما از فرودگاه‌های اروپا در حمایت از عملیات «اپیک فیوری» به پرواز درآمدند و اروپا به سکویی بزرگ برای نمایش و اعمال قدرت آمریکا تبدیل شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/76830" target="_blank">📅 12:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=A6DLOd_vwtFj_W8fEEzyTBYJRoldEYdGb7v4XVG34tFBL4feYUeCfTQP7LWoJBlKC_g9pPeevBQ2kkTJq7mC-Cwo_SfPRUoBT1F496WXC6jqMosU_ceuZfbRuUJEhQZE5e64sHqzfql_cSG12nTaJsbWouSeHEwxYhiAgvGHXOqkgnfu12zLvp2gn9Nlji6_9qFfIWEyhQhefTh_3X7mtC5VxlrEAN4HiFu-1wMITvdA0RXpFaQ0qVlKhtvpAtHOTI5-OYgfeg3XQI9FAyJC-eEyDLVO3bCrwwARJvARvI6FWRG3Hih5TplArYNSvqCUB8_U6yFuCH8yKY__hY7Dug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc9ddafbb4.mp4?token=A6DLOd_vwtFj_W8fEEzyTBYJRoldEYdGb7v4XVG34tFBL4feYUeCfTQP7LWoJBlKC_g9pPeevBQ2kkTJq7mC-Cwo_SfPRUoBT1F496WXC6jqMosU_ceuZfbRuUJEhQZE5e64sHqzfql_cSG12nTaJsbWouSeHEwxYhiAgvGHXOqkgnfu12zLvp2gn9Nlji6_9qFfIWEyhQhefTh_3X7mtC5VxlrEAN4HiFu-1wMITvdA0RXpFaQ0qVlKhtvpAtHOTI5-OYgfeg3XQI9FAyJC-eEyDLVO3bCrwwARJvARvI6FWRG3Hih5TplArYNSvqCUB8_U6yFuCH8yKY__hY7Dug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره مقامات ج.ا: یک مشت آشغال هستند!
نقل زیرنویس، ترجمه ماشین:
سؤالی دارید؟
ـ آقای رئیس‌جمهور، آیا آتش‌بس تمام شده؟ آیا آتش‌بس پایان یافته؟ آیا تفاهم‌نامه مرده است؟
سؤال بسیار جالبی است.
از نظر من، فکر می‌کنم [تفاهم‌نامه و آتش‌بس] تمام شده. دیگر نمی‌خواهم با آنها سر و کار داشته باشم. آنها تفاله‌اند. می‌دانید تفاله یعنی چه؟ آنها تفاله‌اند. آنها آدم‌های مریضی هستند. رهبرانشان آدم‌های مریضی هستند و آدم‌هایی شرور و خشن‌اند.
دروغگو هستند؛ ما توافق می‌کنیم. و اگر من با او توافق کنم، یعنی توافق داریم. و او بیرون می‌رود، حرف می‌زند. ما توافق می‌کنیم. همه موافقت کرده‌اند: هیچ سلاح هسته‌ای. ما توافق می‌کنیم. آنها بیرون می‌روند و با رسانه‌ها حرف می‌زنند. می‌گویند ما حتی هرگز درباره‌اش حرف نزدیم. یک جای کارشان ایراد دارد. آنها دیوانه‌اند.
آنها دروغگو و متقلب‌اند؛ مریض‌اند. آنها به مردم خودشان آسیب زده‌اند. تا همین حالا ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید وقتی مردم می‌گویند چرا آنها حکومت را سرنگون نکرده‌اند، نمی‌توانند سرنگون کنند، چون مرده‌اند؛ آنها را کشته‌اند. کسی سرنگونشان نمی‌کند.
آنها اسلحه ندارند و طرف مقابل مسلسل دارد و آنها را می‌کشد. رسانه‌ها این را گزارش نکرده‌اند.
اما آنها آدم‌های بدی هستند؛ آدم‌های بدی هستند. و صادقانه بگویم، نمی‌خواهم وقتم را با آنها تلف کنم.
حالا می‌گذارم مذاکره‌کنندگان فوق‌العاده‌مان اگر بخواهند به گفت‌وگو ادامه دهند، اما من چنین چیزی نمی‌بینم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/76829" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNRsNPhxm7xLtIPN-cDGcrOyCA0voMZX48JzxNzZT0donzoZrV0nFZOjAj63aNNI89kHKVgt58tgGxDQdIArM6odQpoYKLd7bWGSH06fYCpgYMBCf4_bBlrfAxqJEBoW80_J9xuXPt1EYmBOegZtTLno5p74sSn-DPtLP4Bp-qseAGyk0hIueieiZSEOwQ-tseF8C9uPhx2IcRhkqjmGqmRe-TahPX4cI2EZep1OSgRzxmnD2f2BnzJnBVEL9PPcyvtnpk8h3gx10cJKeo3OwWbiQdKdBHDeM5h5c_Uq1cBquv_nHt89_jXKYixt8zT703WkjKjgz9SxSwXkETxp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست پزشکیان، ترجمه ماشین:
رفتار دولت آمریکا به‌عنوان میزبان جام جهانی همان سیاست خارجی آشنای آن را دنبال می‌کند: دستکاری قواعد، زورگویی به رقبا، مانع‌تراشی و تقلب. این همان دستور کار MAGA آنهاست. ایران چنین بازی‌هایی را رد می‌کند. ما قاطعانه پای حقوق خود ایستاده‌ایم.
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76828" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76827">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
الان زد بوشهر رو ۱۰:۴۱
سلام وحید جان ساعت ۱۰۴۰ صدای انفجار شدید در بوشهر
سلام وحید همین الان ساعت ۱۰:۴۰ دقیقه صدای دوتا انفجار شدیدی توی بوشهر شنیدیم
سلام وحید الان بوشهر رو زدن فکر کنم پایگاه هوایی بود دوبار صدا اومد
بوشهر پنج تا شش تا صدای انفجار سمت پایگاه هوایی و دریایی ارتش
بوشهرو الان دوباره زدن
بوشهر یه بار حدود ۱۰:۳۰ دوبار زدن یه بار هم حدود ۱۰:۴۰، بار دوم نزدیک‌تر بود
ما پایگاه هوایی بوشهر هستیم
حدود ساعت ۱۰.۴۰   دو تا صدای انفجار اومد
دو سه دقیقه پیش هم دوبار
به نسبت انفجارهای روزهای جنگ معمولی تر بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/76827" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JZWoR-KVDHgeVUDUZQLdxja3IVee36uHByk597Fs1vrgwmtGvdftMF694RvuvSnOExGss9frfcqBdNakKK3h_LDFAeiHiLtiWohwBrPGykJP7uqPN9VL3zMDCJIaVOKCrFDFKC-6MVhZg-r_ykEESZFa_LbEXp9-pPS-_ifrhMxtLeG_ZfM0GFQ8y0CirFkRE9Luk5Ay9xMa2rzzGOCidR4MmbpxKOXRgZO_YSMiZ6r2Sp_kE9YWen27SMCoYrvoHnbUT2TVMFrQ3g6faDYMkfGp3pkDRZwILOqggeWHX37H-sXbrwnrkn5RxHVq0yZHbmrnEIHRPz0lGzV1g5gvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: پاسخ دادیم
منابع حکومتی:
پاسخ اولیه به تجاوز آمریکا با هدف قرار دادن ۸۵ نقطه از تاسیسات مهم نظامی آمریکا
اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
🔹
به دنبال حماسه سازی ملت بزرگ ایران در تشییع دشمن شکن و پرشکوه بی سابقه یگانه دوران و قائد شهید امت اسلام، رژیم متجاوز آمریکا که روز به روز ابعاد شکستش بیشتر آشکار می شود و بازتاب جهانی خیزش عظیم و میلیونی ملت سرافراز عراق در بدرقه تاریخ ساز رهبر مجاهد شهید را شکست بزرگتری برای خود میداند، بار دیگر عادت پیمان شکنی خود را تکرار کرد و وحشت‌زده برای تحت شعاع قرار دادن این رویداد تاریخی، ارتش کودک کش و تروریست آمریکا در ساعات اولیه بامداد امروز با تهاجم هوایی به تعدادی از پایگاه‌های ساحلی و ایستگاه‌های غیر نظامی در سواحل استان هرمزگان و ماهشهر به طور آشکار آتش بس را نقض کرد و تفاهم اسلام آباد را زیر پا گذاشت.
🔹
در پاسخ اولیه به این تجاوز نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی طی عملیات مشترک موشکی و پهپادی، ۸۵ نقطه از تاسیسات مهم نظامی آمریکا در بندر سلمان، منطقه پنجم دریایی بحرین و پایگاه هوایی علی السالم کویت را در هم کوبیدند و یک پهپاد MQ9 دشمن که قصد دخالت در عملیات را داشت، سرنگون کردند.
و ما النصر الا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/76826" target="_blank">📅 07:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76825">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWgDQeRArcAPsKq669XYdd18jBf5xbVdaOwoOtt_onSqLehxglZKHwLBkpLTr9yusee-JoZZ0m2_7cHTjkzHVRpkcwFcDkWiNTqU6W1EUVOJ5k_WIMFw9WIy9whWU_bUnZPi298AI3-FuNIPIPpdgAb4A75GTK6r4oYVkiTS_9d4EWg0H9DdFWofgRhREjATvTtnja6JoKKGWrTANbeiq88MCE8vI9zQWSAiIAUJF1t3tBOQXV52UC8Jp6XxAM00nwsX7C7_vupayaPvSx66WYVpl6i4ltLSchycEeJl8duVSGHTpOwLu1VIVfiU1Cf_MZT1SZWlNOjvB1xZk_V_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شوری اسلامی پس از حمله‌های بامداد چهارشنبه آمریکا به اهدافی در جنوب ایران در واکنش به حمله‌های دو روز گذشته سپاه به سه کشتی در نزدیکی تنگه هرمز در پیامی به زبان انگلیسی در اکس نوشت: کلیدی‌ترین موارد نقض تفاهم‌نامه ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگه هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار حمله‌های اسرائیل به لبنان
او در ادامه این پیام نوشت: «دوره قلدری و باج‌گیری تمام شده است، راه به جایی نمی‌برید، ما اهل کوتاه آمدن و عقب کشیدن نیستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76825" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
