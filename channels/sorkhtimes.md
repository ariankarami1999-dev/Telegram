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
<img src="https://cdn4.telesco.pe/file/PO-jbnKWBj2iqPmITiV1CgPupG4rOVA_aPO2w-GBC1jgMa0MaN5kgX1nXJdfpO13ffmB3nlJa2iu8AxcuuNHtW9kAHxllrq-4uWZrc2nckN0pAau_rgFpG10FzvFVlSRO8giv9D4AY5c0OIrRVI_-HHkNaUqSnWRsrmEaNP1BQkZDxmrRNk68PJdOf4snc5jV3Lq-tzUjGmSRlrjIqpkb0dBbIPLpxd4AXRnxZa_YceGAcxoM_CHpTs94ytznp97pTmwRzDjLkunt2U7kn6s4ZY_ogAPa56Yp_pZMgzzfe1JA-25UtPCjXV_nyhJsHWGW7XAvcm4NUiIUGLttro0LA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 01:25:43</div>
<hr>

<div class="tg-post" id="msg-134500">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❗️
مثل دیشب
🇺🇸
🇮🇷
فوری از باراک راوید، خبرنگار نزدیک به ترامپ: مقامات آمریکایی حمله به تنگه هرمز رو تایید کردن و آمریکا رسما مسئولیت حمله رو به عهده گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 333 · <a href="https://t.me/SorkhTimes/134500" target="_blank">📅 01:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134499">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
خبرنگار فاکس‌نیوز به‌نقل از مقامات ارشد دفاعی بیان می‌کند حملات هوایی آمریکا همچنان در جریان است که باتوجه به حجم تحرکات هوایی در جنوب کشور ادامه‌دار بودن آن قابل انتظار است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/SorkhTimes/134499" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134498">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
برای اولین حالت باید ساعت 12/30 منتظر بازی غنا و کرواسی باشیم .که غنا ببره صعود میکنیم ..نشد باید ساعت 3 منتظر نباختن ازبک باشیم .....نشد باید ساعت 5/30 الجزایر و اتریش مساوی نشه .....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/134498" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134497">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2hT0Ky2GLuh7EEjJgyxravs-uDJdzFo4a04YmTxEn3Zv6EcroigurZoHwJBLo4qURlLGW0RwN8WEl5yhf1SSxHKRK6bRcXrzCpjooORxxbG59XxTDXmTofKWW6p3ksEWVJlIktYLccub7PoZ-Bkh9I_DHG7lRE5wURqg42WnNfsQOd1l5y5-aCykwNZ0ehetTxQodHBQPXF5X047wnlJfvJRTobsF6rXq9wET6_8-r1rh2een1raat8zHj0O_evxqEXp85dDI1W0MOpZ3pbqoT922rnaruMc4zcvio6KqAK7sseyBor8QdOIzna9J7mWBYwJaVvw4AI_T6w03DvLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جان سینا : ظرف روزهای آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/134497" target="_blank">📅 00:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134496">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
بعیدع کسی سه بازی و بیدار باشه .ولی امیدوارم صبح که از خواب بلند شدیم .بخونیم که ایران صعود کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/134496" target="_blank">📅 00:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134495">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚽️
باشگاه با سرلک و پورعلی‌گنجی تماس گرفته گفته بیاید برای فسخ
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/134495" target="_blank">📅 00:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134494">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/134494" target="_blank">📅 00:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134493">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/134493" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134492">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
جزییات تاریخ برگزاری آئین خاکسپاری علی خامنه‌ای (رهبر شهید )   ۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی  ۲۳ خرداد/ تشییع در تهران  ۲۴ خرداد/ تشییع در قم  ۲۵ خرداد/ تشییع در عراق  ۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد  پ.ن تخمین جمعیت حدود 25 تا…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/134492" target="_blank">📅 23:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134491">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
مسوولان باشگاه به موازات این تلاش ها در تلاش هستند توافقات اولیه یا اسکوچیچ را به قرارداد منجر کنند. آن‌ها بر سر مدت قرارداد یا اسکوچیج بر سر امضای قرارداد یک+یک ساله و مشروط برای سال دوم توافق کرده و تنها اختلاف حل نشده درباره بند فسخ همکاری در صورت بروز…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/134491" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134490">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
مسوولان باشگاه به موازات این تلاش ها در تلاش هستند توافقات اولیه یا اسکوچیچ را به قرارداد منجر کنند. آن‌ها بر سر مدت قرارداد یا اسکوچیج بر سر امضای قرارداد یک+یک ساله و مشروط برای سال دوم توافق کرده و تنها اختلاف حل نشده درباره بند فسخ همکاری در صورت بروز…</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/134490" target="_blank">📅 23:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134489">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/134489" target="_blank">📅 23:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134488">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
یعنی هیچ موقع تو زندگیم اندازه امسال اعصابم خراب نشد،حالم بده
❌
نیم فصلم استاد خلیلی و فرزاد پوفو…. دل و قلوه میدادن باهام دنده دادن تا راحت این دلال های دوزاری اوسمار و خود کونده خارش زن تیمو هوا بدن،اقای حدادی تنها اشتباهات اوردن خلیلی بود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/134488" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134487">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/134487" target="_blank">📅 23:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134486">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
#فرهیختگان؛ اوسمار وقتی فهمید با اسکوچیچ مذاکره کردن اصلا نمیخواست به تمرینات ادامه بده به اصرار ایجنتش این بازی رو روی نیمکت نشست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/134486" target="_blank">📅 23:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134485">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
باشگاه باید ابتدا از لحاظ مالی با اوسمار توافق کنه و سپس از اسکوچیچ رونمایی کنه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/134485" target="_blank">📅 22:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134484">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
نساجی مازندران به لیگ برتر بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/134484" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
باشگاه باید ابتدا از لحاظ مالی با اوسمار توافق کنه و سپس از اسکوچیچ رونمایی کنه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/134483" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134482">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/134482" target="_blank">📅 21:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEb1kY0lL2QAfaHs6aav5604nvzIGzwxlYv5v_BSl79Qu2zD-NiRn9jxBuFaODJu3ct_GIG2HmZjEOZFizCU33fF23QQ2PtQ_05PD-K-hdc09SLYDXuyHh0F3sdsWdlekGCotrZF47Cokn0VIZlXrp5XmvChzy9OciM8cbBax7E0NPndRj_fe69NYpgRj8zO6UhAJ4pxjwmHBGqZ6qdIJvrWZgclFq5XrFimGtkOOos21jccncWD_4LXAA0HckGMeUmKr7fL4oX_-cqLSzMieUAWtYmK3ff9CEn5LogjwwSvOdKZxVoD9Xw73svkRga4i6PyEijlV1m9C5qAx7MpHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شادی بعد از گل شجاع خلیل‌زاده که تبدیل به یکی از بزرگترین میم های جام جهانی شد.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/134481" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134480">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔸
بیرانوند و جایزه بهترین بازیکن زمین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/134480" target="_blank">📅 21:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
❗️
تسنیم : قرار است به زودی در وهله اول باشگاه پرسپولیس مراحل اداری قطع همکاری با اوسمار را انجام دهد و سپس به طور رسمی جدایی این مربی برزیلی اعلام شود.
🔴
🔴
پرسپولیسی ها که با اسکوچیچ برای جانشینی اوسمار مذاکره و توافق کرده اند، هنوز هیچ قراردادی با این مربی…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/134479" target="_blank">📅 21:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
اسکوچیچ سرمربی جدید پرسپولیس شد؛ توافق نهایی انجام شده و قراردادش تا ساعاتی دیگر ارسال می‌شود. او هم به‌زودی برای شروع کار به ایران می‌آید.
✍
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/134478" target="_blank">📅 21:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎙
کارلوس‌ کی‌روش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتوانیم کرواسی را متوقف کنیم تا ایران به دور بعدی جام جهانی راه پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/134477" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
واکنش تند زلاتان ابراهیموویچ به مردود شدن گل ایران: رؤیای یک ملت را دزدیدید
✅
زلاتان ابراهیموویچ با حمله‌ای تند به تصمیم داوران درباره گل مردودشده ایران گفت: شما فقط یک گل را مردود نکردید؛ رؤیای یک ملت را دزدیدید.
❗️
اگر این سطح داوری در بزرگ‌ترین تورنمنت…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/134476" target="_blank">📅 20:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134475">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/134475" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
نظرت در مورد بازی ایران و بلژیک ؟
🔴
ابراهیموویچ : نزدیک بود نیمه اول خوابم ببره و نیمه دوم واقعاً خوابم برد
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134474" target="_blank">📅 19:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134473">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134473" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
❗️
اگر اتفاق خاصی رخ ندهد؛ تا روز سه شنبه باشگاه پرسپولیس از دراگان اسکوچیچ سرمربی جدید و کروات خود در فصل جدید رونمایی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134472" target="_blank">📅 18:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134471">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
❗️
اگر اتفاق خاصی رخ ندهد؛ تا روز سه شنبه باشگاه پرسپولیس از دراگان اسکوچیچ سرمربی جدید و کروات خود در فصل جدید رونمایی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134471" target="_blank">📅 18:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134470">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
شنیده ها :باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134470" target="_blank">📅 18:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134469">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
⚽️
فرهیختگان : پیمان حدادی دنبال این است که با  دنیل گرا و تیوی بیفوما برای جدایی این ۲ بازیکن و فسخ قراردادشون توافق کند ؛ این درحالی است که هر دو بازیکن یک فصل دیگر با باشگاه قرارداد دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134469" target="_blank">📅 18:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134468">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیسم قبل تورنومنت 3 جانبه با اسکوچیچ بسته بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134468" target="_blank">📅 18:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134467">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahVlw0zpORZVVV4wxMWUQE2sizQBW_-ShjgSy4vtHrDTl_jZu0qPD7cq4H9qdUsrbuYhs2VTsG-41_Toet9UsannAAvmDfzm0Q6ntZeszZXJr6Yk2alq9wALxvX_D4TMyTqi5bzSwAre01LCOrRjN6W5QqFIYzYIOperAQQoMpR8yjPi6CkhLWgMTGQ08glTQi0mTG--OjObYOMv4EO8i4w5FdZtn1AD7o-l1GeFkujVDcOtVzIxS7VciZWX0EP5c25DJW_tZUQoDY4dUXmIoqvvly7tiocGvyU51oo212j9Yy28MYnHKj4JgLvcD24FHmuLL3eJM2CGYX-3KgQtog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها :باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/134467" target="_blank">📅 18:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134466">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/134466" target="_blank">📅 18:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134465">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134465" target="_blank">📅 17:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134464">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⚽️
فرهیختگان : پیمان حدادی دنبال این است که با  دنیل گرا و تیوی بیفوما برای جدایی این ۲ بازیکن و فسخ قراردادشون توافق کند ؛ این درحالی است که هر دو بازیکن یک فصل دیگر با باشگاه قرارداد دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/134464" target="_blank">📅 17:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134463">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f32365f3ed.webm?token=HcBbWToz5ysLyDI1Igvh260HUubpavQXVuDCS3cmkL-tPSfIf4oM03boWRuEOaOwh8-R12QqcfUMBDsOly9ZaJf95QZiQ-ogyfNOR7gzywEVyMaJehLfdxe2iX16ttpp-PbhEMTQHCvuWvTITzMGpRRH-4ANptMpP-1klhtUMx035vEg6U2zsDcvVZfhvcnBVB9Y5c5zmw68SOQ2zxjLi2rSJ7K2JcgT7wvje79rD-4xL77jSbNdYTzlyDGvN0Ldj1P21649n67HpCv6pBbwbLwF2cydJBcheQHWQemS_1kuOy-f09yYpNT0ZBTqrkepfKW8iBfIAfo7nUJwK1PwXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f32365f3ed.webm?token=HcBbWToz5ysLyDI1Igvh260HUubpavQXVuDCS3cmkL-tPSfIf4oM03boWRuEOaOwh8-R12QqcfUMBDsOly9ZaJf95QZiQ-ogyfNOR7gzywEVyMaJehLfdxe2iX16ttpp-PbhEMTQHCvuWvTITzMGpRRH-4ANptMpP-1klhtUMx035vEg6U2zsDcvVZfhvcnBVB9Y5c5zmw68SOQ2zxjLi2rSJ7K2JcgT7wvje79rD-4xL77jSbNdYTzlyDGvN0Ldj1P21649n67HpCv6pBbwbLwF2cydJBcheQHWQemS_1kuOy-f09yYpNT0ZBTqrkepfKW8iBfIAfo7nUJwK1PwXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چراغی در مورد نقل و انتقالات نیم فصل دوم درست میگفت اینکه داره دلالی میشه</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134463" target="_blank">📅 17:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134462">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehrad</strong></div>
<div class="tg-text">چراغی در مورد نقل و انتقالات نیم فصل دوم درست میگفت اینکه داره دلالی میشه</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134462" target="_blank">📅 17:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134461">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚠️
⚽️
چه کصشر هایی که ادم نمیشنوه، هرکسی برای خودش لیست مازاد داده بیرون….چقدر تیم سرمربی و سر حاصاب دار شده ما خبر نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/134461" target="_blank">📅 16:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134460">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚠️
⚽️
چه کصشر هایی که ادم نمیشنوه، هرکسی برای خودش لیست مازاد داده بیرون….چقدر تیم سرمربی و سر حاصاب دار شده ما خبر نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134460" target="_blank">📅 16:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134459">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
ابراهیم اسدی: شأن پرسپولیس حفظ نشد
🔴
🔴
پرسپولیس در حد و اندازه‌های همیشگی خود ظاهر نشد و این حذف برای هواداران قابل قبول نیست. ای کاش تصمیمات مدیریتی و فنی با دقت بیشتری اتخاذ می‌شد و تیم در مسیر بهتری قرار می‌گرفت. این سبک آسیایی شدن در شأن تیم بزرگ و پرهواداری…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/134459" target="_blank">📅 16:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134458">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🤩
صحبت های پیمان حدادی بعداز بازی…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/134458" target="_blank">📅 16:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134457">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qwcbprw7UpLFt0YSwrB33J78Qzb3YSTNQK05FaD39uulIDBvYKmaRcMvsya-T2QwOg3OTgLf4xw8MjjFqbXyggShgPTzr9qonjPGUIJkj-0-GBqkatX0TgJCrxRn_etc_bOuUdk165U9KLVLML9uoEufJBdgPAE3KsrozVW4-Z1xVtnl1uZTYDcWqE0J1oTcc7clljd1n9RyHPHwlRi2GQWkdD73nCd5__7v_zBVO9kjdMOJIAkFN05TvuQOBkZWExczJssALgOtvO0kwm_zD2oIhL8mFk5k9IEFN8tWr6c-wILfIsvsOQZZwppYl_ZnLG_MV1i95_m3uboSESK01w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134457" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134456">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFk4y5Ht6F35QzlMZEDOuBaWlgktuG55gXE4keV4fCmgFvpCy7mBGv0E51Dng-BVscvY5OfX33vodOrWZL9d3Xz2gMrSMDyWXN7FG41kg4Qj8tpu4HrAUG8t7bFnVtaY4WePovOS79XG5eB2H89hZ0YWYS4tkxInOUm0UGlG-LbP1GoFEEoa89qdKxivz0M8LCSEJM0nCIIWTt3Mc4X6qC0Rqk4DAPj4fB2NQMbez2qP0Ac9xmMQZfO38NxeDzqfXwTkAAcVhtujqt0FH-nVLGmgkveY33wsvcM5yimbVgHuQrExYNGMEP3PrX_YzVJu3LG89n-ldn64_zMbuRmlJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134456" target="_blank">📅 13:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134454">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nG-VaJSU5WUwBiHUlIuY9onq2G6SBPN4aETmShJcUuvyaQ0paQ1ZSzrJrRWKvGRNyscLRAwapQf7ESIvWF8scsaT32oizC3O0hx2J11wWv_bFj4CGkIigowQUeeu2w69Xgrvm_sxD2GEj_kirkj86PGlsExa8o36YmLv1Mkv5Vu74rdi2XF9OU3RPfSURV3_l1Lh_VTtKjfQnbOUISr_sCOj6mxPWzuyOukD69EIK6QD43CScbMO9U5ZXG5Plg4pVbdHsEsxM6kyYY3EXP0zEjHk9w2xBbIwKgy118Rn7Yk5rkD04dJtHwzRWdrs487VDJ8F34RTRKlGmLwFRXKlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رامین رضاییان بعد از وینیسیوس جونیور بیشترین جایزه‌ (بهترین بازیکن زمین) در این جام‌ جهانی را گرفته است. همچنین رامین رضاییان با گلی که امروز زد، به کافو اسطوره برزیل رسید و با 3 گل، گلزن ترین دفاع راست تاریخ جام جهانی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134454" target="_blank">📅 13:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134453">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134453" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134452">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5SrQ_l5VQSA8lxH326Pf4EEgH8Qs_7-SkQEDoJaMfHcE0mBVdFUQuLBwHzR6tBOJjKhZ7zld3oj6ztpTdTq9TGh-kkM2l7S3DyQMvKkyZDl7A4I0aFY9vgXQGpdN7PMzIauXkYV5oFJ90Syt1nAMBBGJjsEUtzHCCw0o2CDoYEXvlZRexYUXLaBnNyrbNS7_Jr43cIVPDJmEcysb2X0IVqDH2JtHOYNwQASQLSrBaMuPP7H9COw6YgZZpt4NPvFWuOX_TWiaZqUt4gQ0ahyS7AUF7LwisEeBJy3We2eKDGs_Kt0cpHfedPHUbLqgi6yTlpwLJ5cJNfO0z0LHcOV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کی‌روش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتوانیم کرواسی را متوقف کنیم تا ایران به دور بعدی جام جهانی راه پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134452" target="_blank">📅 13:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134451">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
همین امشب نصف تیم و بیرون کنید و برای آقای اوسمار پست خداحافظی بزارید ....به تیمی باختیم که پنج ماه تمرین نکرده و با تیم امید اومده بود ...لیاقت سطح دو رفتن هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134451" target="_blank">📅 12:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134450">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWQzUFAtVvP1zlgp4WaFjOy492De4hFLDeCkFnzsJX-ujkLFinctlsAirQawM2SJoGGmaQxa8HYUaUaq701oBShmbzBaA2AHBoQ4bp6WeNWdEyugn0Sol8W0dvVOlYhJ5R9th9jOUOhsFFHZpZo9KnEVEe6gXJJJXGZJajaej5Wm861Hajjn6-JBn_io7QL8JHUaomb6xXcG_bdiCO6lcG95iiR3HXEGss3u9RWXVv7qD_fAhIc9rrGyCG6G0lbJ6hm_bfXH6JvC3XhDvTIYjrD4tAos3huZW-GNqTHz4xOCYf_b5I9eSvUZ9QDHms-BvgFKkE7tgt_qUnmQeHmLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملاقات مهدی مهدوی کیا واینفانتینو درحاشیه دیدار ایران
⚔️
مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134450" target="_blank">📅 11:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134449">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
فقط کافیه بازی امشب اتریش و الجزایر مساوی نشه ..ایران صعود می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134449" target="_blank">📅 11:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134448">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Shllglmsr16yzJ8HJjrpLJrg_OrfR4v4LmLuAqXVzhovjeholLbTwJDaMbHc4aoPaCXHi_lHm-dnT5Mp9_hCQbfVqrqlXta4ZiLMx9OrlU_zhB6qoVDMbUngEFrrr3-ojX2jqdoDR2Q1yZc--LCjxRAWZk4JLYE4kxK-Bl1AaxoOhJXPIcvUahN2HYQdJ_mVG_lRdDuLxp9GSyWxRa544QRk0cmNoib32LzxdZyfsyeeQfPG0AV69qYhcq9gE2gJ2tSl0ICr1mCVnjZ1cv7d24HLGTj2_mTbBYTcri1kJ6WjeBIEd8emiOJsCHNu2SvVzIBZpfw7CXWvpXc7WlnabQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134448" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134447">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c8df3c29.mp4?token=YbXJr7pDUjEu0BHFNONDjlMXxzLVyPAr4jmNU2FZAKu5n2tu66gMpgw0BCPsqD-Vkrut2oWT9QS1kHkMMAO8MzeRMPMECK0HxThwWIkq6FH6x9XR0CDpzoPYwQ8EzNBfQK_jCEDh9-A-e0ZDBwURrxL2UtJZONyvxik7zljTW7Wq-17iUqhYoE0cxSiqcMvaoaYO3xK8b4-tXQjVLfiV6zcBQCmnOeMxp1yznpQZyWnJBA9kjHMc96eCXxiChUHnNw_DPHUZujzTKgW_BXOcLjoGQdmsRaKN5vyyZFMHyAiIzj7HqQcFjzw0EK_vrrRh1n4O9W40JgmJrPBwm-380ln61xx2btHQ7s1c2XwzcIX5H0bZpF-x_eN9kLA5ByWHcNVeyq-JiJ9PLGEWBex729GnIygx7GrucoZbxfjAI3eACpF_GPG7xR85Z6WhB0a2e-eBtIEseN02KbQbn0XyUQA2dAFqmlwnIA35BthUP468baoqqW_oFy9sHkqOpglpn4d_HP1Zld56tMUnhUvcm3LsPkG9BMLLVgI_uNa2EOleZRrl4ibtX1tZ46rSYWSjveLYoOEw-cM9Y-wptmszGhHnsHH18Qcn58366gY3p6vjXv7JydsXcJ9-r_h4fZcXVNZU_sbsgr5FJ3gJmcgKgfJIDYrCsQ8km3rX_gyarL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c8df3c29.mp4?token=YbXJr7pDUjEu0BHFNONDjlMXxzLVyPAr4jmNU2FZAKu5n2tu66gMpgw0BCPsqD-Vkrut2oWT9QS1kHkMMAO8MzeRMPMECK0HxThwWIkq6FH6x9XR0CDpzoPYwQ8EzNBfQK_jCEDh9-A-e0ZDBwURrxL2UtJZONyvxik7zljTW7Wq-17iUqhYoE0cxSiqcMvaoaYO3xK8b4-tXQjVLfiV6zcBQCmnOeMxp1yznpQZyWnJBA9kjHMc96eCXxiChUHnNw_DPHUZujzTKgW_BXOcLjoGQdmsRaKN5vyyZFMHyAiIzj7HqQcFjzw0EK_vrrRh1n4O9W40JgmJrPBwm-380ln61xx2btHQ7s1c2XwzcIX5H0bZpF-x_eN9kLA5ByWHcNVeyq-JiJ9PLGEWBex729GnIygx7GrucoZbxfjAI3eACpF_GPG7xR85Z6WhB0a2e-eBtIEseN02KbQbn0XyUQA2dAFqmlwnIA35BthUP468baoqqW_oFy9sHkqOpglpn4d_HP1Zld56tMUnhUvcm3LsPkG9BMLLVgI_uNa2EOleZRrl4ibtX1tZ46rSYWSjveLYoOEw-cM9Y-wptmszGhHnsHH18Qcn58366gY3p6vjXv7JydsXcJ9-r_h4fZcXVNZU_sbsgr5FJ3gJmcgKgfJIDYrCsQ8km3rX_gyarL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
واکنش مجری شبکه پرسپولیس بعد از گل دوم چادرملو و شکست قرمز پوشان در پلی آف لیگ قهرمانان آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134447" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134446">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTB8D_DVoFrwSuYr-AegqZqdOVqTSklxZmE0TbI06BDZLcStWs4KQhQ_6lXp7zfia6t7_vRTZRO_cnnsSHlQgHAKI7gpQvWSLysAYAr15HQIDqPd0b8h0TVqVvUjFD8l_9OzEiRQLsi1mYQQ3b7uOLi41x_5JQq4hXAgJMq9Phrq6RPBmgojHeNGokS5AStiwgzadZx0938oHq1lxMnj8PWxcnABW4ihDD-3ko2b6vDiIKiah1rWrgjpgcGM-X1JwTSMxEUEBJg9jMgyjdCsD648GmuzztxqI-vdQPSdajsrNwE7uUof-n_cxPYQo9P8uUndYgjW9t_mgeKGVhC-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا منصفانه است، خب اوکی، خوش به حالشان!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134446" target="_blank">📅 11:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134445">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134445" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134444">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134444" target="_blank">📅 11:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134443">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv54jkREQ_jIMzwaf5qVn3_wRQIye_-sYeKTtqOnMNoJheF3UJsVZ_2pSg5tnZBD5hArysPtoDKxRbSWM2YWZHCuXOdJsauhAJeMtqpRj0mkwaIENXP0YEZb38nOrhC_QNk55PCidU8BIOi8mvzfFLhGDBWYBlNmRZoPBfNUv8gtXLIE0HzIQLhoUs37VOg0UnQ2ZXY0hITd8GL5y2sGveHPHIJ10YlVSW5jd412OJGmhhICfdhHAjjuzFv0wdi3rNyQ2h7AYktBzpt1tmbIuNb_zDuHEMD67tAs--3gsnSjHLTAx_Wc4ts6DfIk-fMeV6nNtfRHMDytOgayx64T5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134443" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134442">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
فووووری از فرهیختگان: تا هفته اینده اسکوچیچ برای مذاکرات پیشرفته و بستن قرارداد با پرسپولیس میره تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134442" target="_blank">📅 10:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134441">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
امیر قلعه نویی بعد از تساوی ایران و مصر:
🔴
🔴
شاید خدا هم با ما سر ناسازگاری دارد. با یک موقعیت گل نزدیم. می گویند گل ما هم با 5 سانت آفساید گرفته شد. تیم مصر تیم بسیار بزرگی است ولی عدالت فوتبال با همه مشکلات ما رعایت نشد. شاید این آزمایش خداوند از من است…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134441" target="_blank">📅 10:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134440">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/134440" target="_blank">📅 10:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134439">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
سوژه شدی رفت شجاع جون
🍇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134439" target="_blank">📅 10:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134438">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/134438" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134437">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
فووووری از فرهیختگان: تا هفته اینده اسکوچیچ برای مذاکرات پیشرفته و بستن قرارداد با پرسپولیس میره تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/134437" target="_blank">📅 09:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134436">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
مهدی طارمی یکی از حساس‌ترین پنالتی های تاریخ فوتبال ایران رو خراب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/134436" target="_blank">📅 09:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134435">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57704b3690.mp4?token=LBaEOhUXnTdeGef25kQNfCahque-bRu55V-BvtNxEFdvyXEsi18vKinUZJT8XMUVwz8hEBrEaPB66Gn4RrTMn7_VSNyKys7-dfqlnWAehWWm_0Ew9_sW5VyavyT5NEVI-OwgpUX4Hynkm8_PjGQVHfueo6d_eE68lzRcIbzxc5huE1W8yZO84E362Z5kq9voA8ri97xGjVzouxDyhoHiJeev86iCcwWhSYB0m6QCCKLR0pNUivrX3Ifip_ryIFQuZWgTyrHK2mCCM1UZW4CFAhKa_bLvFTsmOHbFwMFWLNhV3mz3IlW-TgSg7Z1wbt7AvQ_W2ynOEQv9kWoYkkDokA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57704b3690.mp4?token=LBaEOhUXnTdeGef25kQNfCahque-bRu55V-BvtNxEFdvyXEsi18vKinUZJT8XMUVwz8hEBrEaPB66Gn4RrTMn7_VSNyKys7-dfqlnWAehWWm_0Ew9_sW5VyavyT5NEVI-OwgpUX4Hynkm8_PjGQVHfueo6d_eE68lzRcIbzxc5huE1W8yZO84E362Z5kq9voA8ri97xGjVzouxDyhoHiJeev86iCcwWhSYB0m6QCCKLR0pNUivrX3Ifip_ryIFQuZWgTyrHK2mCCM1UZW4CFAhKa_bLvFTsmOHbFwMFWLNhV3mz3IlW-TgSg7Z1wbt7AvQ_W2ynOEQv9kWoYkkDokA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134435" target="_blank">📅 09:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134434">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84ff37ffd9.mp4?token=Rzz4Ns7eOnfDhnCiqS8uXt2xYXDGKol_9x5hI5nft1kM6_8GaXQEmB3JKg352Xaa9bWHteJQy1Swbj4ydiJMrmRoj0vE1LugBn2OJITOJAUSfty4hn2ie2ZYtkSUXjUnyh86-Wz-qwAr29jhuYz30gnhenNSywerfjwqx4Dx_LtZ2BEzMAwP7EAHk1as4sLv5Mk47zY82W-hswGGw7zq-T3HyE863eF2w9MejwquEY-xRXRww9LRGugZXYwWgZ1i4SezDZUcAtVgrwLLuSLdidAICpWEOpqxQ8juQR9H-N-Nd_ZpDJaoItN5gfEm9psTCdOCQjwM1cvv4hGkgMeqrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84ff37ffd9.mp4?token=Rzz4Ns7eOnfDhnCiqS8uXt2xYXDGKol_9x5hI5nft1kM6_8GaXQEmB3JKg352Xaa9bWHteJQy1Swbj4ydiJMrmRoj0vE1LugBn2OJITOJAUSfty4hn2ie2ZYtkSUXjUnyh86-Wz-qwAr29jhuYz30gnhenNSywerfjwqx4Dx_LtZ2BEzMAwP7EAHk1as4sLv5Mk47zY82W-hswGGw7zq-T3HyE863eF2w9MejwquEY-xRXRww9LRGugZXYwWgZ1i4SezDZUcAtVgrwLLuSLdidAICpWEOpqxQ8juQR9H-N-Nd_ZpDJaoItN5gfEm9psTCdOCQjwM1cvv4hGkgMeqrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیر قلعه نویی چیو سانت کرده: همه 5 سانت و ده سانت و سی سانت
😆
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/134434" target="_blank">📅 09:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
جونم ایران ..گل اول و زدیم ...پنالتی و جبران کردیم ...رامین رضاییان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/134433" target="_blank">📅 09:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkDZS7-sty_eHQh5JaZ0D1fSkjAGB_b-1q4aK9m4A_nbfWNF1zMUBIeyej63mkA0fJaiFRCZdmx7VOJpLu5eHEwbfEevgi2cKuJoM94c6vreUoDAbu9Y1uJYX9CE4o84VzSTZPmammnhd-bUg18uJqF5KCCoAzlpNH1MkWyU2pp0f6oiBpyzGkz0ngFVNuzUL64HW84KfozRfmgC4nZEsYig-yVej0tWGBQ939nt9ybyC0xVqwrj7cusLFOw3c_snUtSUbg6fUbRLiIQSK8KMVF6WeOctIl15TIb0_bgYyrWPO1_0JJUvIG_pIthqxziDLDflyzkE5FFka1PS_sFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سوژه شدی رفت شجاع جون
🍇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134432" target="_blank">📅 09:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
امیدوارم امشب کی‌روش و ارونوف برای ایران کاری بکنن خیلی بعیدع ولی شانس داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/134431" target="_blank">📅 09:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
تو بهترین نیمه دوم ایران تو جام جهانی متاسفانه دو تیر و یک گل آفساید زدیم ولی نبردیم بازی و خیلی حیف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134430" target="_blank">📅 09:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134429">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
✅
ایران 3 امتیازی صعود خواهد کرد یا خیر؟
⌛️
در صورتی که ایران برابر مصر به تساوی دست پیدا کند و با 3 امتیاز در رده سوم گروه خود باشد آنگاه باید منتظر نتایج سایر رقبا باشد
⌛️
برای قطعی شدن صعود تیم ایران باید 2 اتفاق از 4 اتفاق زیر رخ بدهد
1️⃣
. غنا موفق…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134429" target="_blank">📅 09:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134428">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
❗️
شروع نیمه دوم ....حساسترین 45 دقیقه تاریخ ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/134428" target="_blank">📅 09:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134427">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2t0wD3_zoUP-9ipjwuoMqFx0mP-dGW-sGGBjtW3DPRlUNOH7iJqh8-exoBIo6ScQmIS-LlTtRycNWFOPg3r8GaiKPm_epS77u43Y1BPtg0wlEBpowTcBNeYUPjdw5K6kfEdCuLB4fFueE2QA_zoN69YPPD_PDLRGCayYy3q2Pjue6_A1AuARkxsBCLR5AU8Om71vOylnIyFqwmd8DjrKs8APCr2OiN69UyYOqBISAuytmSlCTjnvyziNKvXJwrZEpvh8a81hkScabScjBy4BgdiEnSpEUWsPM33D6rBlr0k2JZ518xpjH7aeyS5IGSIFvGmbB01uy617TcohFNK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدار حساس و هیجان انگیر بامداد جمعه ایران
⚪️
-
🔴
مصر رو در وینکوبت با بونوس ویژه و بالاترین ضرایب پیش‌بینی کنید!
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/134427" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134426">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
| پایان نیمه اول
🇮🇷
ایران
1️⃣
🆚
1️⃣
مصر
🇪🇬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/134426" target="_blank">📅 07:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134425">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚪️
گل اول ایران به مصر توسط رامین رضاییان 14
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134425" target="_blank">📅 07:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134424">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20439446e.mp4?token=njwgeit9Ymxy-WJImISzg7PlCLXL8_YVYdEjQ64UZPTyKPKVo2zTk_TaFZoorSs6GEDPlosSL1HnbdWziP72qkg2fP14YdWFXRVwvM12DcSQ28aT8qVv2mTv0_m5xMcZniK5LcJRJiT1jHUh1Uz3qddEri2cwkerN1DscvexAqvlQXGE1525kNpFQDElGSJ3VvhDtMmPPUWMsKiDhnloeq7vA25MYmyskYXdmsnU49UFzrCdqeIZeJJMc90hyxBR9q-4WYko-ckMz43RiSvShsks8JkEuzdXNAU1su_9phDxtTtYZ2j8x0eFcbqxn4NPIhYOSIoIfYo7llt20yVn-CHMKQf9YCcfqNHJohPY30JCJJh4ByViBBI-k5ogYAcTzDIRyLw2YGIP_HUUXUCDj16IsqnjD-FnCJr_E-I4sJcroF_8oz4A_mdd2xxFNqnbQrE03WACmqB_C30r2AAAlYbd7X_pIOiXH6IeIWBWVq-jD95y90sYSfENSkEiqKguwVyanerl7IbCtY1CGiPPJo5bQGsHz5z-VLAY9V2O9aUpahHxNIfkjAyB3b7MppMPcImzDzbV3z-v2j58ADvPivs2T1YEqw35BtkJaCykEcW_b5vUKfHFm56L-8KaZLcEnMBeRp6Rxnbjy8wH9KJ7yRah6RqEfga_UxEkWnGLw40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20439446e.mp4?token=njwgeit9Ymxy-WJImISzg7PlCLXL8_YVYdEjQ64UZPTyKPKVo2zTk_TaFZoorSs6GEDPlosSL1HnbdWziP72qkg2fP14YdWFXRVwvM12DcSQ28aT8qVv2mTv0_m5xMcZniK5LcJRJiT1jHUh1Uz3qddEri2cwkerN1DscvexAqvlQXGE1525kNpFQDElGSJ3VvhDtMmPPUWMsKiDhnloeq7vA25MYmyskYXdmsnU49UFzrCdqeIZeJJMc90hyxBR9q-4WYko-ckMz43RiSvShsks8JkEuzdXNAU1su_9phDxtTtYZ2j8x0eFcbqxn4NPIhYOSIoIfYo7llt20yVn-CHMKQf9YCcfqNHJohPY30JCJJh4ByViBBI-k5ogYAcTzDIRyLw2YGIP_HUUXUCDj16IsqnjD-FnCJr_E-I4sJcroF_8oz4A_mdd2xxFNqnbQrE03WACmqB_C30r2AAAlYbd7X_pIOiXH6IeIWBWVq-jD95y90sYSfENSkEiqKguwVyanerl7IbCtY1CGiPPJo5bQGsHz5z-VLAY9V2O9aUpahHxNIfkjAyB3b7MppMPcImzDzbV3z-v2j58ADvPivs2T1YEqw35BtkJaCykEcW_b5vUKfHFm56L-8KaZLcEnMBeRp6Rxnbjy8wH9KJ7yRah6RqEfga_UxEkWnGLw40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
گل اول ایران به مصر توسط رامین رضاییان 14
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/134424" target="_blank">📅 06:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134423">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
مهدی طارمی یکی از حساس‌ترین پنالتی های تاریخ فوتبال ایران رو خراب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/134423" target="_blank">📅 06:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134422">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d86c48556.mp4?token=cqfWkrA_HMwyurGNzVmlyyzPQqnslLp5neuM80LX9DQ0bb-GwWAsIH9fA7iN3rHRB4J4JGQ3VrG3vCOecSp_A5R7UOwqUi2XVUwNw2AIJW3AneKZL8EK9saqPONek894ZeLWqnVnUxyfgZDefvxmGc8Au09qTgNiIb6iO9Z1-49Gw1FUBCfpATS4T6y-HdfQ2IFORvSyZfxcCioBGt3OYFzgSQV_MgmE07_Le-p-Medi974mtFLyZp5Mf3UXoY9pwy-BKXPjcrpXofQuFpDJ0jTO4DcR1C6j_GAUxGhVUvql9uPl9_dLEP5pF_J_otctXyH-ZeiUaJI_POtnKqP_Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d86c48556.mp4?token=cqfWkrA_HMwyurGNzVmlyyzPQqnslLp5neuM80LX9DQ0bb-GwWAsIH9fA7iN3rHRB4J4JGQ3VrG3vCOecSp_A5R7UOwqUi2XVUwNw2AIJW3AneKZL8EK9saqPONek894ZeLWqnVnUxyfgZDefvxmGc8Au09qTgNiIb6iO9Z1-49Gw1FUBCfpATS4T6y-HdfQ2IFORvSyZfxcCioBGt3OYFzgSQV_MgmE07_Le-p-Medi974mtFLyZp5Mf3UXoY9pwy-BKXPjcrpXofQuFpDJ0jTO4DcR1C6j_GAUxGhVUvql9uPl9_dLEP5pF_J_otctXyH-ZeiUaJI_POtnKqP_Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مهدی طارمی یکی از حساس‌ترین پنالتی های تاریخ فوتبال ایران رو خراب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/134422" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134421">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e272e0aecb.mp4?token=a5Yo-hFHpFooFZrebrMfK5ymB0DELBZDXEZXGABK_icXXgCItL1PtdURZl8YpHypOnnokX96mnOM1SJR5zFe-k0OP27wN1uGoTYjvS1CGHwETcdmqRgI4ZdaTGw2G-mNnF4YIco3IRh2fgx59BNx7BaNKqnxI0ByVYUAl6Abpe9UT0mG5UpDB7HDve6vbHZRKVhuFYmMPLXpOtt5zO7X-YnKo8HfAnTrScdKvRO5vPaOlsMticOKNbCZGvCewO9okdk70epllx0jxJryTjniBsIvDdQiGiltk3wZNYttJlQpqQaE9blOUqT2r4513ZAtih-yKq5LATnR5wsCjiqfNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e272e0aecb.mp4?token=a5Yo-hFHpFooFZrebrMfK5ymB0DELBZDXEZXGABK_icXXgCItL1PtdURZl8YpHypOnnokX96mnOM1SJR5zFe-k0OP27wN1uGoTYjvS1CGHwETcdmqRgI4ZdaTGw2G-mNnF4YIco3IRh2fgx59BNx7BaNKqnxI0ByVYUAl6Abpe9UT0mG5UpDB7HDve6vbHZRKVhuFYmMPLXpOtt5zO7X-YnKo8HfAnTrScdKvRO5vPaOlsMticOKNbCZGvCewO9okdk70epllx0jxJryTjniBsIvDdQiGiltk3wZNYttJlQpqQaE9blOUqT2r4513ZAtih-yKq5LATnR5wsCjiqfNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اشتباه بیرانوند؛
🔴
گل اول مصر توسط محمود صابر در دقیقه 5
🔴
ایران 0 - مصر 1
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/134421" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134420">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
❗️
ترکیب تیم ملی ایران مقابل مصر
🔴
علیرضا بیرانوند، شجاع خلیل زاده، محمدحسین کنعانی زادگان، علی نعمتی، رامین رضاییان، میلاد محمدی، سعید عزت الهی، محمد قربانی، سامان قدوس، محمد محبی و مهدی طارمی.
📺
شبکه 3 / ساعت 06:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/134420" target="_blank">📅 06:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134419">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇪🇬
ترکیب مصر هم مقابل ایران اومده محمد صلاح فیکس و عمر مرموش روی  نیمکته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/134419" target="_blank">📅 06:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134418">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7s4bfxwJ4eKYBMeUJb7aSf5LUrui2e_QqcQgmqu_yOTozVi6DpaWRhGDenZwAL10QW4qGbVsUZ2YoInxI8XNWmy0cn65FZYBktUBYiD3MXRbp8YwpbNoEbRV4pZvStlY638-CnkHB-zYMHChxJt1s-hxV5q58hcYUb7vd4uy_S6NzNQuoUhRoMdbzTGQncHOAjnBL5lMYeuEm419MbQDoOXFPHxJcG8RupPHFpjGmMrEfQ-xjGC9neQjsx3dV1r0L3AP485CGenmVZ3rqDDmMhhFi5rPh2oEpo6YWzAQsAgCfK2PszCBbMTgSjdpLzfRvPwigAgUXllJb3X8Vni0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه H جام جهانی 2026 پس از پایان مرحله گروهی
🇨🇻
کیپ وِرد با مساوی ۰_۰ مقابل
عربستان با ۳تا مساوی و ۳امتیاز به عنوان تیم دوم صعود کرد
😐
👍
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/134418" target="_blank">📅 06:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
قلعه تو کنفرانس قبل از بازی:
🔴
حساس‌ترین بازی تاریخ ایران است. بچه‌ها فقط باید مسائل تاکتیکی را با آرامش باید پیاده کنند. مصر تیم بسیار بزرگ و قابل احترامی است. آنها قدرتمند هستند اما ما هم ایرانیم و برنامه‌های خاص خود را داریم. شاید بعد از مسائل ذهنی و…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/134417" target="_blank">📅 06:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134416">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
❗️
ترکیب تیم ملی ایران مقابل مصر
🔴
علیرضا بیرانوند، شجاع خلیل زاده، محمدحسین کنعانی زادگان، علی نعمتی، رامین رضاییان، میلاد محمدی، سعید عزت الهی، محمد قربانی، سامان قدوس، محمد محبی و مهدی طارمی.
📺
شبکه 3 / ساعت 06:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/134416" target="_blank">📅 06:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134415">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
❗️
ترکیب تیم ملی ایران مقابل مصر
🔴
علیرضا بیرانوند، شجاع خلیل زاده، محمدحسین کنعانی زادگان، علی نعمتی، رامین رضاییان، میلاد محمدی، سعید عزت الهی، محمد قربانی، سامان قدوس، محمد محبی و مهدی طارمی.
📺
شبکه 3 / ساعت 06:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/134415" target="_blank">📅 05:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134414">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
ترکیب ایران مقابل بلژیک
🔴
علیرضا بیرانوند، صالح حردانی، محمد حسین کنعانی‌زادگان، شجاع خلیل‌زاده، علی نعمتی، سعید عزت‌اللهی، احسان حاج صفی، رامین رضاییان، سامان قدوس، محمد محبی و مهدی طارمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134414" target="_blank">📅 05:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a18df2d4.mp4?token=NVnpKAsazr7oMHy4qhhirIUSTkRoMr8DMgrDfpHqmojUsm3V6vrcT1venajUnG29y5jxOIxltV2vpzhr8bfXXMxfBHQU4oWmfDS1vd3Mxzvpzm8Q9EdFnKek_9HlWa87HfGx9N0w7K341EDtWvmN4HL5JH3OgrkWsLVGjEgsFaSCTESDN0Tqf5NaKXCC0B_uzgAjUa1HEZmdCQ7gDWPrSI7X2N5K2n1H8w3j7iGLoLBucdF6iB1_AZAZBVMBuVJ2TMaHV7qY0MZI5ff9NfSEekWhsSKJPtAuCtfSNMjkoxZFDZUGO03xDYOWsD7xoLIfwzBnT_I-8Jc8Ztc5FYRTzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a18df2d4.mp4?token=NVnpKAsazr7oMHy4qhhirIUSTkRoMr8DMgrDfpHqmojUsm3V6vrcT1venajUnG29y5jxOIxltV2vpzhr8bfXXMxfBHQU4oWmfDS1vd3Mxzvpzm8Q9EdFnKek_9HlWa87HfGx9N0w7K341EDtWvmN4HL5JH3OgrkWsLVGjEgsFaSCTESDN0Tqf5NaKXCC0B_uzgAjUa1HEZmdCQ7gDWPrSI7X2N5K2n1H8w3j7iGLoLBucdF6iB1_AZAZBVMBuVJ2TMaHV7qY0MZI5ff9NfSEekWhsSKJPtAuCtfSNMjkoxZFDZUGO03xDYOWsD7xoLIfwzBnT_I-8Jc8Ztc5FYRTzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👌
👌
👌
👌
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/134413" target="_blank">📅 01:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVevqOLjJS3omTgF4PeTFxVHVpodXoaeMHDwQVEI2Lb9o3IgV9ATQhDLiT7IiLlXHF-IoTfhXjmvy_SUNnWW7ChWKMZA5g58hWbvuM-asj1kfNpSXPS_f1ehv_oyYzopq0DVUZ6wyNd2O_NXDuOpgcsjly3sgdm0fA9vQPcLWec9BG3GoS0jsjDLO9sGBkIflCVe6wMwiJ7GZ_Vsw1UJSw995boTjhEZbafL9B67jr3ckrYZb0BOiPxS3EppqzEIj-Iz_xW6ZrHq1DlX81Y2jxeVhM_QZisL7qWwpKMH_uXNSY64yHdG1jKdXsicx84Js4V3QJP1hyKSjuQKuP7n0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدار حساس و هیجان انگیر بامداد جمعه ایران
⚪️
-
🔴
مصر رو در وینکوبت با بونوس ویژه و بالاترین ضرایب پیش‌بینی کنید!
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
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134412" target="_blank">📅 01:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from7 .</strong></div>
<div class="tg-text">حدادی کوتاهی نکرد تنها کسی میتونه پوست اندازی تیم رو شروع کنیم همین حدادیه</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134411" target="_blank">📅 01:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚽️
تیم پیشکسوتان ما این تیم رو باید میبرد
❗️
این تیم باید پوست اندازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/134410" target="_blank">📅 01:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🤩
حدادی سهمیه مرده رو زنده کرد، با هزار یک لابی تیم ۶ جدول دو دستی داشت میرفت آسیا!الان مقصر باخت به تیم سوم چادرملو با دو جلسه تمرین کیه ؟!
❗️
تیم ما کل پولشونو گرفتن یک ماهه دارن تمرین میکنن، با سرمربی ۱.۲ میلیون دلاری که قبلش تپه نریده تو لیگ نزاشته بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134409" target="_blank">📅 01:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134408">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">#تلنگر
❌
❗️
پروژه بگیر ها و قالتاق ها دارن زیر پوستی حدادی رو میزنن خاستم بگم دنبال پدرتون بگردید… با تشکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134408" target="_blank">📅 01:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134407">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🤩
صحبت های پیمان حدادی بعداز بازی…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134407" target="_blank">📅 01:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134406">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
حالمون از این تیم داغونه و ناراحت .امیدوارم اتفاقات خوبی برای کادر و بازیکن بیفته .....بریم ی استراحت ریز کنیم .ساعت 6/30 برای بازی ایران بیدار شیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/134406" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134405">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkkCGeYyANQEn-Kry-FkWFLCOogg0YcQapavjKKfBDWVNImGiQnczz2MoPFbPVUVq8RfwemxuIqjruB9OvOGIsCPtnuEE8OHaTAgLbJupm5pQO4GhpWOvbAMmSecAj1z-a-DwHaegyBh8vLJlORJwhIqotl_YBT7ZnO2gE-VJvhiHHAE4zmbh8GqdXdozmBR4Jw_BQfeW0S3fcfUPwigfhBJeIbMLrSuQkHIg7GFVQHpOlNqiRAfGwYnLAXzx57JuVaNgYMtkT_bJ7Sqhg-CqDFgd6dnpOL8pMJjHneuu9zhubrZviXYoXMQNvU2N3zUaIbSqOxQwv3lTAVpRJwovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آپدیت جدول بهترین تیم‌های سوم گروهی
❗️
پ.ن: ایران با برد صعود میکنه، با باخت حذف میشه و با مساوی کارش به اما و اگر میکشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134405" target="_blank">📅 00:57 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134404">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
#فوری
🚨
هیات مدیره پرسپولیس برای فردا صبح جلسه فوق العاده گذاشته و درباره آینده پرسپولیس تصمیم گیری خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134404" target="_blank">📅 00:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134403">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
پیمان حدادی : قرارداد اسمار تموم شد و ما دیگه قراردادی نداریم هیات مدیره به زودی تصمیم میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134403" target="_blank">📅 00:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134402">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
فردا 6/30 صبح بازی حساس ایران آغاز میشه .کیا بیدار میشن که ببینن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134402" target="_blank">📅 00:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134401">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
❗️
فوووووووری/ارتش آمریکا در پاسخ به نقض آتش بس از سوی ایران، اهدافی را در جنوب ایران هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134401" target="_blank">📅 00:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134400">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
اخباری سرمربی چادرملو: 7 بازیکن با تیم ما قرارداد نداشتند ولی برای ما بازی کردند که از آنها ممنون هستم/ حق ما سهمیه آسیایی بود/ بر اساس آئین نامه حق صد در صد با تیم ما است/ به قیمت باخت و از دست رفتن سلامت بازیکنانمان بازی کردیم که نشان بدهیم فوتبال باید…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134400" target="_blank">📅 00:46 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
