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
<img src="https://cdn4.telesco.pe/file/fogeeeXndhxjkGs-GzOht5B7gFZYrvaeD_tkztzLFC_YSf58gBERtqi3c59FvbhdFgjMIxv6igspPGf97tRaHtwIo2WHX7BnGwAvFnvCpBEPRa2HcZFHNpYbDwMBiqM75DnE9zLfFbAnm_jfro79RU76rxPfXVo09ZiJi8dMSEMoodgFPtuttikzBWgipQOH21TOm8lwHQ1xQkP4fTjZmMa9gg0pFUOi_cpkYApy0DCSbtYY-aobFuImbzJiRYtQ7Xf_ccDLlpZcYGdNF2CDqi3FDkoywQy14IyJIUYsZ6MfMq-gUHobi8kWWHqcR1IWX3PkWROIahWRbLuwqngV_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 12:20:57</div>
<hr>

<div class="tg-post" id="msg-442263">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
ماجرای تغییرات لحظه‌آخری یادداشت تفاهم ایران و آمریکا چه بود؟
🔹
یک منبع نزدیک به تیم مذاکره‌کننده در گفت‌وگو با خبرنگار فارس جزئیاتی از کم‌وکیف اقدامات ۲۴ ساعت اخیر دربارۀ توافق با آمریکا را تشریح کرد.
🔹
به‌گفتۀ این منبع، پس از آن‌که روز شنبه کلیات یادداشت…</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/442263" target="_blank">📅 12:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnu5FzLm2iLxgDtGzrk-NwsQeI0tAs1TecixsRMtD7F0CZCqboUNNj-IFCFhIHVp2AaL1-m3oVCRCc5WKNBq-to0HAtB2HAeqiKWTNeDlLfFhh3xAcR7IMJgcxgDn1yxJNjiMePCDhzYid2Mh9aw0vC7RCpzvjAZQG2NvoHtpm-iZta6gN0AkVL4jdk2IToCsdmaFXF1qDLXs6BbzYxAHqGKP4fT3p7jXxSvMx4OiQ6C7mVkIFZVgoaF7CoenldKmLLcZYSEMNm4HGMkQgHkgAiQBlSKsKuXN1CMtcEwelghPO6I2hNTJ8KAha2hB14cvCYsvB63R27xM3uUOSiHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6eWd_TdgqmfPlz00o5nd-lttubRDXkYPqKuuLhJ4VYqKdsW86pLVgpDC7sJ5xDpTgAf2Y1JunqTmxJa74IQmmwsw0soN2W25tRIHYnlsa6dy0KWf2wivEI-FZDAAVu7wRJ43--fHBtTJ023TI-6XtWcGK81f4PkYa2qkaRyDfL6ug0A-026E-0P5rp9Nrl52fxH1Jhbv8mNZftFqVi_vaYA9QT99IUo7O9rNkmK237pf7U2MRrAopzeK2v91Zi2l358i8ZtNqm1A_Unw3AAtNkHy-cgDQAEKuGOXABFGO4pa7f_V6D44JXCH9g77S1o7AqHMI9mZgNeoWMVmSpucg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b075e3305.mp4?token=LHmGYLmJcWQfGh9w8v38SRnqXbNDUxCLn0FNbNVIjnDdejjEFJ3cD5vl97JwSAWC_xl2chVemcs3Ob7hE9LfC-gbo3Ey5ZJ-wiFfRKMFUZv3hwW3Tr7JL5AeRxvR9cIoeQjAMCvQGV7O-OSrqahlwnx2Fm8S9qSGHicXsIjO4OYSZt0386v3-YMjiOz09rJOwLpJ3iBIrp-j6VvI2Ldnr9HJAjC8D03l9AJHZNIKuktSdibEndzxGTEn8ts1h29LDaLPSPPVk9d0nXZ7dlg2Kal76KxQlTDur8BvAvd-n3pIMRf_6aWWtxY00BZf7ENvcwelgOmbA_3tMhNediDzbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b075e3305.mp4?token=LHmGYLmJcWQfGh9w8v38SRnqXbNDUxCLn0FNbNVIjnDdejjEFJ3cD5vl97JwSAWC_xl2chVemcs3Ob7hE9LfC-gbo3Ey5ZJ-wiFfRKMFUZv3hwW3Tr7JL5AeRxvR9cIoeQjAMCvQGV7O-OSrqahlwnx2Fm8S9qSGHicXsIjO4OYSZt0386v3-YMjiOz09rJOwLpJ3iBIrp-j6VvI2Ldnr9HJAjC8D03l9AJHZNIKuktSdibEndzxGTEn8ts1h29LDaLPSPPVk9d0nXZ7dlg2Kal76KxQlTDur8BvAvd-n3pIMRf_6aWWtxY00BZf7ENvcwelgOmbA_3tMhNediDzbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع لبنانی از حملات هوایی و توپخانه‌ای رژیم صهیونیستی به شهرک زوطر، مرکبا و شهر الخیام خبر دادند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/442260" target="_blank">📅 12:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg8qaR5Fbq12NnUS4vEwGcdjHwu8Rx7E07buIEDMkbFJmIz5TxhMMFcKENIdO-eaCVCd2aVGt3FiFMtoDvpIKZStEB4k1ZCV-23nOq7hzxNyroAc_LMfTPD8cQmkRt565s0y7J2j-tCu2p2e219PjePO9qb8Ynti_spnDTS2YeXeUB7YJ0ruiBv37AjwmgAshz1ZsSKqCOkU5ZMYkRdZowTKBZYhmgScZ0cimWksCXaG8IeKSwoITtwRO3NhWZn_HONkA4q1lv_WeiFTF_vDEAIcM0CJObsubobzvqu3gh46LLoiNdy4wgpEE_EO8HlFQvr49HgEgmgTbx0WGthDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ اسرائیل: قرار نیست از لبنان عقب‌نشینی کنیم
🔹
اسرائیل با وجود همهٔ فشارهای کنونی و آینده، با خروج ارتش از لبنان مخالفت می‌کند.
🔹
من و نتانیاهو سیاستی روشن را دنبال می‌کنیم که براساس آن ارتش اسرائیل برای مدت نامحدود در مناطق امنیتی لبنان، سوریه و غزه باقی خواهد ماند.
🔹
این سیاست شامل تخلیهٔ منطقه از ساکنان محلی و نابودی تمامی زیرساخت‌ها، چه در سطح زمین و چه در زیر زمین، از جمله خانه‌های واقع در روستاهای مرزی است.
🔹
نتانیاهو این موضع را به رئیس‌جمهور آمریکا و دیگر مقام‌های ارشد آمریکایی منتقل کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/442259" target="_blank">📅 11:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c004074d.mp4?token=UMKRjsE9GMM15T8lBfm-bbHLkqWSmhEqHBdDOYjdRqIsAdtc6VJXAcytKdA3l7fwxK9SMPuHGm3XXkGOMDU_vnZUBgwNvxiGw-HRnzO5oe11VTd_1tdGFYBRva_OEpttjaSzCJ8Htyvxgf2z6Zr78RMq3bsi2iTtknHLG2Q6fudcxdPG6Ymmdn3gU6IBmCNGOjOpllJVu4DLFdmAMzIj69yVhV3ruKn3aMQ7U03r72yIll78hzEY5lx2g6ilKVqz9GdGo-f8jPMifpYf20OlBYO6st5CPC_EM2FQTEF90bYe-4P3q4npmBB2JsnPxOLvaC1vEQOCEwwZFbCxtbNsDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c004074d.mp4?token=UMKRjsE9GMM15T8lBfm-bbHLkqWSmhEqHBdDOYjdRqIsAdtc6VJXAcytKdA3l7fwxK9SMPuHGm3XXkGOMDU_vnZUBgwNvxiGw-HRnzO5oe11VTd_1tdGFYBRva_OEpttjaSzCJ8Htyvxgf2z6Zr78RMq3bsi2iTtknHLG2Q6fudcxdPG6Ymmdn3gU6IBmCNGOjOpllJVu4DLFdmAMzIj69yVhV3ruKn3aMQ7U03r72yIll78hzEY5lx2g6ilKVqz9GdGo-f8jPMifpYf20OlBYO6st5CPC_EM2FQTEF90bYe-4P3q4npmBB2JsnPxOLvaC1vEQOCEwwZFbCxtbNsDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امیرالمومنین(ع) سیاه‌پوش عزای ماه محرم شد
@Farsna</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/442258" target="_blank">📅 11:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442257">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">جلسات شورای شهر تهران علنی شد
🔹
سخنگوی شورای شهر تهران: جلسۀ فردا در صحن علنی شورای شهر و با حضور مستقیم اصحاب رسانه برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/442257" target="_blank">📅 11:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e70803c3.mp4?token=chdhlfkIwZ8aaBSUe82oX_3V158SndW7F8XjtK68_oq1bTyQcBvPxKJnaI8SBA-kBnHNOgf3oace9lb2SPNDIfsaQZwTUhPqq7bXWA9l9SAY6HcK4KUVk1W5dzWPX2BRXIuGnva0eOInYfp9VcpHRsFhQPMx3PmQxcb10Sb42ECOAArRIh-NbH7PA00eCfoZeAvP3sfwbh5GSD4ONCaSFz9oyMSwATUAKT3oRwskvvM9StKypIhqDOYP_eVLQnO9PddL4gXahrHzCJr1KjivinzgpaYD7htnOy0t6i9JGV71wskCCb4ZNfQhSzTrG9dVvE9agWuDTcrz47kWCUAPQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e70803c3.mp4?token=chdhlfkIwZ8aaBSUe82oX_3V158SndW7F8XjtK68_oq1bTyQcBvPxKJnaI8SBA-kBnHNOgf3oace9lb2SPNDIfsaQZwTUhPqq7bXWA9l9SAY6HcK4KUVk1W5dzWPX2BRXIuGnva0eOInYfp9VcpHRsFhQPMx3PmQxcb10Sb42ECOAArRIh-NbH7PA00eCfoZeAvP3sfwbh5GSD4ONCaSFz9oyMSwATUAKT3oRwskvvM9StKypIhqDOYP_eVLQnO9PddL4gXahrHzCJr1KjivinzgpaYD7htnOy0t6i9JGV71wskCCb4ZNfQhSzTrG9dVvE9agWuDTcrz47kWCUAPQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زیر بار زورگویی آمریکا نمی‌رویم
🔹
ما که تسلیم نمی‌شویم تا هر غلطی خواست بکند. آنها منتظر بودند ما در کشور با قحطی مواجه شویم.
🔹
اگر دانشگاهیان به میدان بیایند، از بحران‌ها عبور می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/442256" target="_blank">📅 11:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در مبارکهٔ اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای‌ کنترل‌شده تا ساعت ۱۳ امروز، احتمال شنیدن صدای انفجار در مبارکه و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/442255" target="_blank">📅 11:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442254">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXCkyM04dxnrxMVbDHtHYYiu3BLD3lmQ_-Gzc_ipsX5x3Zh6KM4uCLKK_vVl5JKOPlGYwOdNQdJcsDKXDNlSP5b2QUGpDTX8DMUFiZkZ6rUG7kvDa8Tk__sOspBfAr0fXCHXlAGWmulp1U3TMlkEJEvfi2zXX9sqrZCUcWaISy9iU-YXMj2gd09P89HU9g01P5DmyopqMjZ4sQO3sS6WBzHSeutLKjI0BfxoERM5ddhnOhJAk8s8rTYkoYayxu_dujvTNgdyWd84Gd8yYgK5uA6A4Y96lY1gPbtCL1Pkb2Rh1I9AoLvdiWmeOZSTt1mku4EGEWLCIdCDx0I_F2eVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لَا یَوْمَ‏ کَیَوْمِکَ یَا اَباعَبْدِاللهِ
🔹
به‌مناسبت فرا رسیدن ماه محرم و غم فراق رهبر شهیدمان از جدیدترین دیوارنگارهٔ میدان ولیعصر(عج) رونمایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/442254" target="_blank">📅 11:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442253">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7fHKIAF4o-dRussQUfdbvYoo6MvpOpIH8pIoUW-wJIZbdxl7H57X-G4Zu60hIJ6zVkcLhBvHjz2VQbAxB4AUXVdr5VJtMKzaJGoWFQp9Y9BC-B5XGiR7tIiV1V3zP7NM5rNGITXutmOWyDjmT9hwZ1diprh9jW7OqCb3TVohlNMxg1n83njRSiOLcQSfJ3cplogekvtxSuvgnQTDKRMA7YJGMhrfEQydABUKUCJbF_Rgpu5C54jD1e-mtt7uXenXh6-p2LcMOtBvXYxUyHeCwG_iI7BhHykMp_clGMB4Pt229i-enFxMf7iC2tKT7TYst8boLSeCK3gXHAVm1A8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با وزرای امور خارجهٔ ترکیه، عراق و مصر
🔹
وزیر خارجهٔ ایران در تماس‌های تلفنی جداگانه صبح امروز با وزرای خارجهٔ ترکیه، عراق و مصر، با اشاره به مسئولیت آمریکا در قبال اجرای توافق، بر لزوم توقف کامل تجاوزات و حملات بی‌ثبات‌کنندهٔ رژیم صهیونیستی علیه لبنان تأکید کرد.
🔹
وزرای خارجهٔ ایران، ترکیه، عراق و مصر همچنین بر تداوم رایزنی‌ها و همکاری‌های نزدیک در خصوص تحولات منطقه‌ای و ضرورت تقویت تلاش‌های دیپلماتیک برای حفظ صلح و ثبات تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/442253" target="_blank">📅 11:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442252">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حذف وثیقۀ خروج از کشور مشمولان غیرغایب در محرم و صفر
‌
🔹
سازمان وظیفه عمومی فراجا وثیقۀ خروج از کشور را برای مشمولان غیرغایب در ایام محرم و صفر حذف کرد.
🔹
متقاضیان زیارت اربعین می‌توانند از ۲۶ خرداد تا ۲۲ مرداد درخواست خود را در سامانۀ
sakha.epolice.ir
ثبت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/442252" target="_blank">📅 11:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615a222da0.mp4?token=oxgYpQXf_rCRz9nHQ_6OPCCEdF94xzekqBJUD_BY8PWiExsqVmrIiQRiXxRxDfotfNSzSmPDLEItW69tH4iR_U2BM6TaKravjtSXUOvPvfIN8k7FAmo8j_o0a1oEiIl8IRDkVdau_XG7V9Kzj0JtLF7QaNroFYs7HnQdk-V0WG9QIH9p2JfGA1AB1vICAJRPhrjOHq0uyJnbJvA51AL1mm7fzNp6rKg1Ul8sALFREUj6gJ9NvCJDJLc1Uq9eAN7i0a5jsi0wE_DGbznUluPMSgvR8ts5pcdxK-33NkHqq6P6m4nMEu0KOHof4YeXoGUqgPjJXHVRagPf_B-h_VhxTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615a222da0.mp4?token=oxgYpQXf_rCRz9nHQ_6OPCCEdF94xzekqBJUD_BY8PWiExsqVmrIiQRiXxRxDfotfNSzSmPDLEItW69tH4iR_U2BM6TaKravjtSXUOvPvfIN8k7FAmo8j_o0a1oEiIl8IRDkVdau_XG7V9Kzj0JtLF7QaNroFYs7HnQdk-V0WG9QIH9p2JfGA1AB1vICAJRPhrjOHq0uyJnbJvA51AL1mm7fzNp6rKg1Ul8sALFREUj6gJ9NvCJDJLc1Uq9eAN7i0a5jsi0wE_DGbznUluPMSgvR8ts5pcdxK-33NkHqq6P6m4nMEu0KOHof4YeXoGUqgPjJXHVRagPf_B-h_VhxTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روایت جذاب از مسئولیت‌پذیری و همدلی؛
این انیمیشن یادآوری می‌کنه که صرفه‌جویی در مصرف برق، یک انتخاب کوچک با اثری بزرگ برای همه ماست.
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/442251" target="_blank">📅 11:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEQptnWAtHyd7uKOGoWSG1PvKsOBareR47kaMJFnsvs5AFKd_RwMHsmR-0jMlwUWgslgNuIrVXL7DAYSFuk9FqOc53rJR38dn7jgl1k2O9fxe-zfvA9T_HEcoArwD0RTVKl1Ufev5rsJKx-W0gCThweSugyHdivLduA763SdXNDEDWgnhr8mnNx5VQ561RFzzcurQHDx_YsG-8L3ios4Gas0r_Jnm0_MLCJHLIA7SVZZyN_Z35fjCj149Wr5dnaqQx3HWFhLHeYav5n1TYkli7bSGFopmn4yahuPpcjXhUbdGdOR6QD0XkSoOmwrou5WgSMy8800RWJQYGOfJojbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مبلغ تسهیلات قرض الحسنه بازنشستگان به ۶۰ میلیون تومان افزایش یافت
🔹️
مدیرعامل بانک رفاه کارگران از افزایش مبلغ و تعداد تسهیلات قرض‌الحسنه بازنشستگان خبر داد.
🔹️
دکتر اسماعیل للـه گانی با اعلام این خبر گفت:  بر اساس تفاهم نامه با سازمان تامین اجتماعی مبلغ این تسهیلات در سال جاری از ۵۰ به ۶۰ میلیون تومان افزایش یافت.
🔹️
وی افزود: برای این منظور بالغ بر ۲۰ همت اعتبار برای پرداخت ۳۴۰ هزار فقره تسهیلات از سوی بانک رفاه پیش بینی شده است.
🔹️
این تسهیلات با کارمزد ۴ درصد و بازپرداخت ۲۴ ماهه به صورت کاملا غیرحضوری به بازنشستگان واجد شرایط پرداخت می‌شود.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/442250" target="_blank">📅 10:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/442249" target="_blank">📅 10:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442248">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083b61f28f.mp4?token=gQ1v2sGIprF8iGEUEKhTMkKW1qwcbkzci11dcifAEy7kEvLVimL-5peAogA0f7b9VUBnNsvP8J2000hICLZyp_B2111PrGh2rNAsiqJF9eaL4t_EIMFpDVncR_d5tSULnIlEoac30NlDScr9-aAes2TtUy0Gd8tLc4-tZQmevPEaxS4x0yHrgJn4IHL23kke5thLpwuyvDP8plL6xgul3naDVqUK3eXia1qYnIpEEWtHYxDayPjElYfxV2t9qLajhy56KXecE8guVVTG1BsvHj-VY9ncG87IvUrO2TiCoEhMaVoOWmPaNFkMmROJ39RSFFtZOVDAzZo-Il4Qn9CScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083b61f28f.mp4?token=gQ1v2sGIprF8iGEUEKhTMkKW1qwcbkzci11dcifAEy7kEvLVimL-5peAogA0f7b9VUBnNsvP8J2000hICLZyp_B2111PrGh2rNAsiqJF9eaL4t_EIMFpDVncR_d5tSULnIlEoac30NlDScr9-aAes2TtUy0Gd8tLc4-tZQmevPEaxS4x0yHrgJn4IHL23kke5thLpwuyvDP8plL6xgul3naDVqUK3eXia1qYnIpEEWtHYxDayPjElYfxV2t9qLajhy56KXecE8guVVTG1BsvHj-VY9ncG87IvUrO2TiCoEhMaVoOWmPaNFkMmROJ39RSFFtZOVDAzZo-Il4Qn9CScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهروز رضوی، گویندهٔ پیشکسوت رادیو و از صداهای ماندگار ایران، پس‌از تحمل یک دوره بیماری درگذشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/442248" target="_blank">📅 10:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442247">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1NEfPnbf1oNLwIS5wvNZjwcWNJTtH-dvjd5bpDszuDh8D38ueJvrqnwXfCzNGNf0htkwbpErMMMs5ibu3owpdysoJZTqMRtIC4YRIQ0708GSYvzIKnBkaB1K2xjGHSDiXqZhoVNfBIdcBfcggwEcc7dTWWiZCrsbjL-RHbfjIu3OpZmOPLlJzVCjbTL07-DREUsh1Wa5enepSSM1CjrGNlZubviuAnMe1Tb5HJpRbIBjk7j586cLsDjwuwyX9hMOG3jSZVrPnXQ2Fu62F96Htkkvmk8QfgcEee7XlJYsCav6OZm5EohPEb2WDAi6FMrbsEGaHRglHvznjpktAA4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمال محدودیت و خاموشی برای بدمصرف‌ها
🔹
وزیر نیرو: اعمال محدودیت و خاموشی باید متوجه مشترکانی باشد که الگوی مصرف را رعایت نمی‌کنند، از سقف مجاز تعیین‌شده فراتر می‌روند و عملاً بدمصرفی را ترویج می‌کنند.
🔹
باید با استفاده از منابع و ظرفیت‌های موجود، شرایطی فراهم شود که مشترکانی که الگوی مصرف را رعایت می‌کنند، مورد حمایت و تشویق قرار گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/442247" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442245">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDqsfXL4nbrG1HwQmiki3sMPPpD_EhJwec_2BmQSFQY2wkuFNZFA6GBGL6XoMK10xzwCUQohPMXgUPTieWICJro3TwiFa3IPFNWl-df84fV18qp3fp0d_SEkjZvTbrkfmyCrFa-cLGmSARnH0bp0E5h6VxYmqto0DpoRJFDnQyc9AQDk0RmSq4_Mr4ttKuB7bL74QOQl7shu5Oyv65TRIy1L0tXzKhw65R-LIfCoHPnMvkcW7DSdf0Qe-5Qq9xphaPM10cEh-hxTIyZe9P5n8CLRqq7RVdzw4f6T9LZHgbtYEeXxB_fFSZuZGHweOFSD_YdKaoTRZ49d5Y-U1rDwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلال خدمات بانکی ۴ بانک برطرف شد
🔹
شرکت خدمات انفورماتیک اعلام کرد خدمات خرید، انتقال وجه و مانده‌گیری بانک‌های ملی، صادرات، تجارت و توسعه صادرات به حالت عادی بازگشته است. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/442245" target="_blank">📅 10:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442240">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmrUKiDOr9pK3NxPCeQzK-t0Tb6OmzPr6ZlM7reWJz72Mzo2c-qslnPSSd0WpDvHFxG41tEfRedLcamFBVuuVSm1WNqrZifWSvaXlc2Yo69zHmGwehe7Z8WHTY3rFPA_gA9qz_-DhH--f9KTHTljrdohmlMb2HUxCJ4ocg2jGHIa2ZWAdSkiJYf2sroHVcr5FQTklhX6N6B75Fge2f8K6GgjLYbxPAZZO_3VUZiaXzaGWBgV_WthFpB1EKirwjZJsfm6AXj5PoUUhGyxSILf4J1I2xt5YL7u1nhEpU0MSNj45bZjfUteJzp1msFtAbxdJNdNJ0z4zHR5T__x8LLfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهروز رضوی، گویندهٔ پیشکسوت رادیو و از صداهای ماندگار ایران، پس‌از تحمل یک دوره بیماری درگذشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442240" target="_blank">📅 09:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442239">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bc8b1da1.mp4?token=WsGzDV0gSZ4kcfwp-jxiKZUXA2nzyupQxbeSopWxeMrPzaNGA6Et8YNXrCesX0U0PEy9x0TC0jhFeZtGNAPNvsIpxKny1u0PUmbJvNBtwihcMY5GhfdSW8AgJiv-F18TomBkP0pLdIY0SmRww7e5i77-8E3VhwibsZtzUBGmusXy79rT4FiFgFsI8rTWalkInJnbyskQSVPKJn6IxrYlpzECkPaOP6Ri7My501PnehOwCOoLmobGZqqwDt1n8BGnzcXaIGHEjLahSygX5TyDyfFDb2ObACXe3LUwyPr8104wpAne0uNBBCnguG-p26yoRKKs4DqKy6Pm2ejeWNWGog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bc8b1da1.mp4?token=WsGzDV0gSZ4kcfwp-jxiKZUXA2nzyupQxbeSopWxeMrPzaNGA6Et8YNXrCesX0U0PEy9x0TC0jhFeZtGNAPNvsIpxKny1u0PUmbJvNBtwihcMY5GhfdSW8AgJiv-F18TomBkP0pLdIY0SmRww7e5i77-8E3VhwibsZtzUBGmusXy79rT4FiFgFsI8rTWalkInJnbyskQSVPKJn6IxrYlpzECkPaOP6Ri7My501PnehOwCOoLmobGZqqwDt1n8BGnzcXaIGHEjLahSygX5TyDyfFDb2ObACXe3LUwyPr8104wpAne0uNBBCnguG-p26yoRKKs4DqKy6Pm2ejeWNWGog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صهیونیست‌ها شبکۀ‌ آب‌رسانی در کرانۀ باختری را تخریب کردند
🔹
منابع محلی گزارش دادند که اشغالگران رژیم صهیونیستی شبکه‌های آب‌رسانی در مناطق «عاطوف» و «راس الاحمر» در شمال کرانه باختری را تخریب کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/442239" target="_blank">📅 09:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442238">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6dDUU8XGAVpYVhDdFp85zHxWZ-hjWK8wnpd4dlzJCB1q-wktjvWZZD2dsMkK021cazmBup6NcSFEFNtd0gQBO9vmQnCJUi7_mKvYoKRo2qMmOn05v0EZfo1iy_q-B4Filfuz6jVid_L8sK-oPEBTQmPc2rQjv8QcL-oEazAPDoit7UsI9bVr96lKYOAX2hZUerj46L2nrM8VL5iv6zT3jlRq-GHYYjkDwWEy84FgZy_zjdTR-prhUiDAs0sMpvjqHWnG4ZVzo_43mwxuSMW2zSX_o6WkFA3T-zpfDSoMO8DAOt6CO-YCjFjokYQo3wxtE3BJRBo5Pct-THiwZVgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی: از کشور بزرگ و قدرتمند ایران به آمریکا آمده‌ام
⚽️
نشست خبری سرمربی تیم ملی پیش از بازی با نیوزیلند:خیلی خوشحالم از کشور بزرگ و قدرتمند ایران اینجا حضور دارم و امیدوارم فوتبال وسیله‌ای شود که کشورها و فرهنگ‌ها به هم نزدیک شود و خوشحالم که از طرف…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/442238" target="_blank">📅 09:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442237">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/653e3beb68.mp4?token=GE_GTmX9ND8yb5nxsYdkHQeXat2nqL9n4wbrdwFCEYtGmaRw_V-8Bhc5E_oALBIUGeBcK9G-s0OaOTUsC5jLn1DkaQ98Xy3hmZYtVhrKktaW_nJweYIXSDZTkF4LjEh0O_2jN8GJy5370oH0dDYRfiFseFo5R9fkM1yfjdtgYDuc5ykaiytEH-wApfRHkaxO_FF-n9Pp8agcXv7taL1gdsPTLtUNg_wvZ5NuKntqhU1sal2TW3jeqn0K7oRFadpLaiUsi5vw2sxxwvD1dB5pWEEBenfhdAnJ0gqo_rPZttdE7T4bWrnrflaLCe-PBy1IMrmXeI7FDVKGWyi0UVm4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/653e3beb68.mp4?token=GE_GTmX9ND8yb5nxsYdkHQeXat2nqL9n4wbrdwFCEYtGmaRw_V-8Bhc5E_oALBIUGeBcK9G-s0OaOTUsC5jLn1DkaQ98Xy3hmZYtVhrKktaW_nJweYIXSDZTkF4LjEh0O_2jN8GJy5370oH0dDYRfiFseFo5R9fkM1yfjdtgYDuc5ykaiytEH-wApfRHkaxO_FF-n9Pp8agcXv7taL1gdsPTLtUNg_wvZ5NuKntqhU1sal2TW3jeqn0K7oRFadpLaiUsi5vw2sxxwvD1dB5pWEEBenfhdAnJ0gqo_rPZttdE7T4bWrnrflaLCe-PBy1IMrmXeI7FDVKGWyi0UVm4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر به لرستان سفر کردید، سری هم به روستای گردشگری ونایی بزنید.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442237" target="_blank">📅 08:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442236">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPW2F-g1JDDq_p6j_3TNOmlY4ZCYloG6nky0m74PVOLU8wI-KnJFHi4dG6W5gD6mkiyzGzLL8eRs86Ctqx-oitJEY2MaCevhgvvGFuzJuGad9ORnXsFk4lXrVdOr7w5CudxctpqRrtA41UpX55d7ugjvvvTGHj9bVchRhxHCXbrGPDVfWdmNagbbhZ-NBGRsXBpirezKyzD0oqLSJeOTxIEsu-gSZ_aoc8DTURjhvEwTw47Q74DpxAZ9E3C_24Q09C9EvQhSzHrPjQW3IA_794yTjuhjklrUgRycaps9xKlv-j_BJ15KbhgV0Ngz7XNGooGX40KQuIVTC8auFPkiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بازدید بازیکنان تیم ملی فوتبال ایران از ورزشگاه سوفای لس‌آنجلس
⚽️
دیدار ایران و نیوزلند فردا ۴:۳۰ صبح برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/442236" target="_blank">📅 08:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442235">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649bfa6d78.mp4?token=Lyg0SljSuHfUyCQ7ZEGZLX4lGq_3_6mWTrEg36G-qvJca9BWL_gyyYnIRpV9krYJmhzhgfsh3IUna0QTgwbRawNco_4Z7uGb6AIKvFOkop-u_BTcSvbp3RQcRtcaz6THSGhCXezvPTquqCkf02_GvDrdT_Pa2ypFjJSkIHUomCcg89TiAXKSESL5HJIez5Jmukfnrk_IPlvXkTrDNxeYFcRpwmKr_1jjML8Raj-ifNZsekczdZJTyxBdbjDm54HyxMwLvc-A8qyo2cYX3tBrxMjqbJiHNGJ4-LpNWK39-P2oy2cXwC2e7wCqrWlwceBdWQsaqHebHj-qe5PjH-f94Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649bfa6d78.mp4?token=Lyg0SljSuHfUyCQ7ZEGZLX4lGq_3_6mWTrEg36G-qvJca9BWL_gyyYnIRpV9krYJmhzhgfsh3IUna0QTgwbRawNco_4Z7uGb6AIKvFOkop-u_BTcSvbp3RQcRtcaz6THSGhCXezvPTquqCkf02_GvDrdT_Pa2ypFjJSkIHUomCcg89TiAXKSESL5HJIez5Jmukfnrk_IPlvXkTrDNxeYFcRpwmKr_1jjML8Raj-ifNZsekczdZJTyxBdbjDm54HyxMwLvc-A8qyo2cYX3tBrxMjqbJiHNGJ4-LpNWK39-P2oy2cXwC2e7wCqrWlwceBdWQsaqHebHj-qe5PjH-f94Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدور پروانۀ ساخت برای ۱۴۲ هزار واحد مسکن ملی
🔹
مدیرعامل شرکت شهرهای جدید ایران: روند تحویل واحدهای مسکن ملی سرعت بیشتری گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/442235" target="_blank">📅 08:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442228">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khKcoewl5wFtzdaT5Z5jzPKScETziFse-3UO8ukZhs9OroKhoGV-oIEndkhrVk_nvA6LqXup8TqfyU4Ky0jVX8eYTgXq4dn8KtHBSZh0Tov_UKiVZM3ZBfM4lR0abOxgxCLSwWpJ-CZpu-QT6d-H7DySiVknhd2a4YLDAhgVoTCRcFoVsV9ipPJ8SGSY7hkdqNVk_OTj41FIznN7nynfiPXZjgTZR-s0AvtsFtpoWUPs94DnFGxcZioppTgCqUdmR6EiO60zXtvOonsRu6RNqfswS6dwGTY6ThE8CAzH-5xQcawIJo3OkypVfJ2zF4Y-mOmhpAAGYN91k7R-C8_Qjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QApovq6GEvqMXtP-bo-SZjzp-P5MJH5QrUBO-unC42CU-KMcmYbJEouBDRrJkaMQkDXRsDFo09KuWvtWOriQ8JbLfSIF74d3jd6WQ247UttNxdZca11QUBVxw_duRpkQZzOf_eHFN3PmZb0hosVBAAZXfP69kPdST4FMdTpHpmorfXSLtMIO4NBgV_Tf0Iy_luI7nH_62mBK-ygn7y9TEQ58inz92oJmWuZ_hjLpEytLhXYRJSmD4Bsdv3B4bXKc-UoFo_-9Ch6SbqPccDvuf2yS32-pZn_VizmeGo0rM1umiJlNPbWaBanjOs-kSp0tNN7QBmnMxB1F8edJ3QZ-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ta5Di7olFxEoW8KctCgW9H9Zbf9U1ercY7YI45srSqAzxGm9RLHq8F1zH6jgpvtL00QNY_L1VpBq16tdZBmhdmiTKLh8kbx5qBaoNm6cu-ajqxHbU-Ye_3RoAg9PRpyAcOuszswcRrbdWsHZPXbJNDW2kT-gfZ6V24y1AnXzTDKbU4EywfF1Oler_gVBcACZdNRtC6L59uMfSd9OUCRgzISqO1JRflA66t6e5lLAFNepUeKXqCp-X_GvA8e-UjqdOZ7QZuoUvdMWFkCi76Bw7wcWuHDcwSoAGzslak66M_0rpdfbxM2H_o6zEEuKgTqguF9DEdYsal1QAJb8m5K8Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nx219rLBClpL2LIdqsMpTWt1poiww73jO5NIT8p9HXGQOtnUxiyR2ve7v9OLS6UpxQkFwlG4db4OpKzzwTJ2lr6uGdcYH-69B1iRK0fG4YwYcNfH9h4LOa9d-JQQ5dJuWJjxq0sWWyGIGpJTpakSfpvSKMpj_0w05v7pioW33enp3hsC1RN0LM3KbAO14BpueKZHIcWiSYZjBsVdo0nZTY4YwIeSuLEhkR-Yqojw2UJUh0uDCZIZgyaMqV20-E9IOjNskAWy64x0hLJa2CGkF_m63FaNSUooemzxo9HttdMD-5EJ9jKr28nJXc-aMASxUZecJKrIWLVMtmUi1HQG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_-Xlhc6TqHe6PSWlY2gmNLNBBBn11htBbOhZYS2LdWcKPJZdWDK5vmYcAbmoUAuPE_IuAJMUCZGrqw8aKjF9Yb47uF6o8rzEfi4-mZa-I_WYMXIKU9S-BTf4Ndja0obxded8JibvyvH3r2B_lO0jZq1TSA7q3n771loXOuynrSXGUj7USxtYkCaNFvdraD5_jDWlTdsyOCCg3Lh_6FvQYC8628CjHQ4FKi9OqNS5qPCuT2iI5qZYcnj-amhBgFdtTfbbwBt-QZDknKgrwyP8-97ZEKDxp46n6ssvzuUUx626burAs1fg_T005LeKUf0UvXI1-iqQXEnuiF6yl-a2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mSsoXNHc6NUp3aTZhVeltSM7H0_sQ-yMocpl6qJciAcxGgRpB4dlzfABM3nnnT51h9NgWAc8uTOcAmuSvJy48_QBN3svYT1XUXzbrEeF5TqpLAdMOgEJsDyCFb4MLkGcYB1kDsMQI-2J79hySEMeK0r1ZgCe569T90Zoiohrp0xCRWCFRESKx65ZWPaWomWyrQsvaYZrKYQLAUdvFWGL_vKMO55K6oGo46zF6SQO8v7jA6WC4Ld5ffuoyKRu625TJNWXOaE6H-pvT4RlPHvYIQYis0f9RmpkakSHRa0u0O81g2X9nT6GNtte0MjhhSDFAA9F-Xl7NvYfu7DSZmjYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDsJd-k-7522aOHdQK5NHkGBP0plf3ckord6_QoP2W0a0ilwfItaALL2cqZVTqE3ElWrMcQUajtlcin2HjhDmQbbXx9gsSf4W_MbqvOBq9bHX0VnvW2DxQXmpr8NV6fr9r9lqO7m7vOLGMHRsK6hiFd6HxdG4nsSbT91QCe0ronWuQB-Qfqk6imGoC75vjwQ-NRiOQ1aaBU-idovMts3zFPsJgicMJ1sWy0S5OjWfXiEcWCPR1cxuDHl6WaQgXbmDR6fdtXakBIciwT_Ic4H3F3y68TrzUD-SwKffbt5ctoIJugho1roBswQnSLQzAwVq_T267LNPW_rMS3v5mu1KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید بازیکنان تیم ملی فوتبال ایران از ورزشگاه سوفای لس‌آنجلس
⚽️
دیدار ایران و نیوزلند فردا ۴:۳۰ صبح برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/442228" target="_blank">📅 08:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442227">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Muz1oAGtMqaNB6QwDca7SOejLph1WwLelWsSCmkSd7sIiNoxSDrfY3MiCx4oaOghYstCa1s56D38db-zbtUPcxmuc_ra_MIkgdWYbGFxwSx7I7OXaKQB1wcqgiXp7X19-fRnWLEMnmyEJ9n6cuzrtYgv-0k7Q96gtr1FlAcDHp1KjYNsP34jxFCujechDRndsmw2uWYPIIjJT5Imqo6agfLVy8V8NpndFhMlZoIDG63cCW-KqiZWXKOiFDA4vwhpHjT_JMIXaUygidIAnCPrLiDzweyk_evOroJXgARWa9JNcSSWBbhZuHa9IX4qsq4JxE_8CGwb_O8ubr4eF2iKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی پرگل سوئد برابر تونس
⚽️
سوئد ۵ - ۱ تونس
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/442227" target="_blank">📅 07:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442226">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8obnbcc4YNelFK2NcONaSiTrpCtSLKBXZu6NIEYjfwURDJPjmm9qG0YLKDgxtFYuo4J9fkD4TskAXpla5upv9m-KhNCD2iR19ARFvdEEUSD5zqyVuv0Z9amf7SQqP4wSXhXpoN9HEeBtHLGiSwUGdVTbDSpWGYFg8OMuvtqDkmrOZfCDgoUeYv2H6zNwFwT6A5Zo8ZgFmjdhvjz9L5rar8_eGcxPCGx0CCH4oMPjVTFwcRBrjAR2xikqR1M49s8SluLdeo31u_8Tj3mAiZFQPkg7E8oQnPMhhyOzG4bwCH-FpPARQtuf6gVkAV8X-F_dcYu_eV10u9w3OdhFM3yCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان واردات برنج‌های بی‌کیفیت
🔹
برنج‌ پاکستانی، تایلندی و اروگوئه در کیسه‌های عجیب‌وغریب، خریداران را گیج کرده است؛ برنج‌هایی که اصالت آن‌ها معلوم نیست و گفته می‌شود کیسه‌های آن‌ها با محتوای داخلشان تفاوت دارد.
🔹
حالا با بخشنامۀ جدید وزارت اقتصاد، ازین پس سلامت، اصالت و مرغوبیت برنج‌های وارداتی کنترل و نظارت می‌شوند.
🔹
براین اساس، سازمان ملی استاندارد مکلف به تعیین اصالت برنج‌های وارداتی شد، و گمرک نیز بر صحت آن نظارت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442226" target="_blank">📅 07:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442225">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCg4voeNAuSX0jXFlwFF2eiQxEyg1ulo6WoDs6kGjCm84xhQ3OlFbtGYyY00yvKQbECSXz-Aq87MDKT4IpKvwBU6chDaVwXFYS7ebWVVTlxEAuJspushT-MafVmbb_1mTd6CONYYiSu5WUZZHcMvaIrN4KuWUPNXurVGK4kTtDLykFLe2d2YtIJoNaVmxmrUW2X0Bru5EUrhPLGtJf4K4_x_6eYNxvG03B1Xkc-sWrtjcuybM5fXxUwX_hUFnJ8DDpYJPeeg9ZR-9teuBGURw19EehUqi4y7mWerm_WUs5mrG9S8oGHH6YU8fBz0r0g9KYSLjzBCxfLWXszRWYLy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۷، ۸ و ۹ شارژ شد.
🔹
بر اساس اعلام وزارت رفاه، اعتبار کالابرگ این دوره تا پایان تیرماه قابل استفاده است.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/442225" target="_blank">📅 06:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjjwbpMuOzfrb-YWmFMrPYMLOAt_tXUfuidoEoOMD3DPj6YugFKRLVHDjtZNyxw9NhJ-2Q_sgDhQHXrV_OdTkQ6Wkhc2JteOaDm3XYvN5l0Z-r0zvek3rm7OhifSDP31GaqujDMcEfHYsfJSpNCJ5ioh-8EyPKkQfteCDuxhOGFh1EF5kt78Lv_K9Xc6XEjE5qAnA1rhrUPiYUZYY3xBAN9Ml5bj43hIDjC38CTFa3Ykl7htMJV_mJsujsrP7m8SMiZcNGMa41kEO7TiyoVpmY0nisOOp5iPKxy2YBSlkWLBLrEMkZRpt-WyqKM6kY02qHzMDvzJTxHtKf1KYUHvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frLAaJooRjqBCDCxg4Gxd_kho670PHRUcajVH_OV-xWFmKLoKqBQNe3iX_dkbzEvOBCCb3zEh1mVpXK3s7tUs7KT27j5iAyTKxEV1W_OIDaaSCpKuKyNL50ncaLhHfs62lzKNpl4Sbzu3hunk9XfmtK-DQq01mS7sVx8d9Ufh_qCcksrwORDhwjx7iFPd7QWOFZX4CLO2qHD5sd3N5tj__68YTc46gwTljvfNjiRJ89JP3sB6pDhVK7Zic3l_ZrOJ3Aabi4Kb0mdfRE6kCjYJuhAHB-qYDgcKoMplOjr28Y78oJKT304cvv74dFU94Yt6p-PjXiDkkSgQKqPUyrHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DccR9j6nGVV7tmP4PznlUGA4bmeuu3S3JIUkz1l-hnGbaXgoGt3iPEXltgo1EqsQg9BlKOFtAsW7u65U003XObFEzrlOsvNBoh6xBPENzkIXA1UmPt6TOL9EfLksGhZq9mGh05VGX_P7lFWzb-a6ElN73kERnd266KS52NTA-srAWFqJpS7B7qVm3F01r400X0lB2hovxB0tsrvSMhDaa0HGiEodO-Y0Xmcj6cIlVoVQwzrevI8bQ1jXM_3Tjg_PdcCp9lqZpS73qclSyb-ybN5GRt0-lAtmaBL2yFB5sBQ3u64UPIworRw2i94GkSWecqI86Wj8rZ3XQc8nRMAJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbS7icAlNH4bMT5kL2k2REQbVl1VzbfhVxCeJvZDD-UnZNHyqxKpooKXq6mG7TmjXRFLvfUb6lwZltLnoV5oHWuSQ4rk1CJIxg9uCoN5zWhka5uNFW28J9JMvRux6-jUuaMJD0zl_ejvN_cSwwR0ARD8jkIH1ggAodvWTFDFPit9yZNZuu2WtzGvg8k0wAQvh9xqi9tX93iOSOiMJJFbBFenLv2-WzhtK6uNHXiwMmjpTfbQMseHsDumYB2nDrJUBvZQ2fIFufTBwRvvb460i7JZoqMgk5PDEtzgAUwLf8a1Khs74rziIP7WNgpUE3-2S3g0WvwzloPbdqf52oV7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGCmSwJa3ZFcvLO7r9WJSUl2-dV45-dYO6jpmJnMb_UQYy_FF7Ao4xUVQvxPiAUIxdDnnlPVvhCdHHmEQDa9YZuGPSglD_IXI4uql_l1AOAWDSbiwRogCePPI0pqbTNG0ZX0AFIRowkqX29eMe8Zfi9QeLp2hK3Q-jsNIdhc5w1sBxmJEz_NJV_Z0bv5z_O2SCcwZ_Z5_Nu5P303bK3XYV5PF2SaKkZ_VlvTY0fLI7II2y52HjmwQzkNlZCgu9_KiftTSWE08yvfiMQgnrvEyFLOiKodgSCGvQ9iCdAXg8I6Xz9tqSvmvFL99CHEpw8DrujR4cMjmCAFmv5iV-ckvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTXlPV2QCGNM5U741O8N7Kos6aO6HJWk9pki-ZrGetcSFotxT3CmkOtfoZZ8T_8zApjO5LUnKAgyUtAM5ySy4IXHRWpJ7Y-i5kpo6CtCRhsdoWrrfCEU_p9e5nAF7f_G3GOQOHUXWjjWtq-O6RbDxroGjQ6D1CMP6K6yqrQY-pi8P7IJLvuD9mTb2azPwtXpF_SUvFyDStQLAji2GcSkvliO3tCID5MFBoxm0F3vEIgQox_fNaw7Ez4zJE8ILTyh3xNCKbOcTSwpA3LTlEghsP-OJ6hTgLbzkt3iFbKvQmyAkNEk86I3pvagxP2bek5jai4ILShoQA3CNvg1E3NVYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طبیعت زیبای بهاری در مراتع جنوبی چالوس
عکاس:
غلامرضا شمس ناتری
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/442213" target="_blank">📅 06:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442212">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLo2ppiJK0oYNiDbVw8bQHrZGad2zMfaI0vFvDPbx4XjRTuTLQn5yW_AuwoBF4_2npl4ZJAFeD4gAr-NiKRKHmfOr2fruZ9rFfq8bm6ZMm5aFRhDRxh7Cqck7TD6pHju-rzf8GhBHNddekgpOef9lp9cRSmz76ll54zd5TkssdKXLaSuFLSV7ch8i0IveNpP_A3zrdjAITqhCtX5e4vkpQtB4sSZcv27S-ruEIDsEHzYq_cqd1AYc7UuwhSl4WvimfNEsfIfAYqWQuEyeVI9jwN-k4WdyXc_1-8qfMXkR-Nj5qCZCxNPfX1m21W-H0n4_RaUTzuRPwiTaK4HdlKwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۳ درصد حجاج به خانه رسیدند
🔹
رئیس سازمان حج‌وزیارت: تا پایان ۲۳ خرداد، ۹۳ درصد حجاج ایرانی به کشور بازگشته‌اند و عملیات انتقال زائران در مراحل پایانی قرار دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/442212" target="_blank">📅 05:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442211">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-gu6dWS7yVkmFQ35KLHvqdaQx49sod286CDsVHgS8xeVITYIqRh5K34Ip41d_zOQM082Qjx07rIAdD8qOTzKPlVvzBGAgrc0EOMgObEYSIB9vHggs-TtRQazUF3aeEdMRYR6rM-tlu_NDHxX94jCCOsZfkOlKQhhsZQq7NhaqcKgxjXOW08LNK3_jkY3wYXBRsc-1ML6_Cax4H8M-Tl7UibEPyhVu6Es1cBZfTDSibqT7GZn3fKEEKOhQ0xSxnA6UQT8Gk4vP1EBqC-vndfN9TkVmTZ_srj8Ac2gKgZfPmYgp_A-AzKoM20kHUptZx5Bs_ZDwFYq2k4F2I9_WEoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساحل عاج با نتیجۀ یک بر صفر، مقابل تیم اکوادور به پیروزی رسید
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/442211" target="_blank">📅 04:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442210">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5914235d7.mp4?token=hzU3EkI_pyK_x1pC8VoaQ3Axi6To0NEgGj2IeC4v_NASB4J952-UzdOtwgyyqMu0SizMwNW9AoxxUmKd-Uk4qSoxCaVSTV1FIgvnPfCcYYQilulWdIPcUwnF1HRD-kQJ7cXP36DQ6eRZeSLF8lC2doP-Xdu7YBz8A0LwdcKZYfpP5TQ0Q0BRSMjnoUyt56FX6Yg3f3MGDjIcoFVsMqNPMzUrPXA-suQt6bHsQ-ykZfu40zR1kOh6trvMQpF2GKwcKqpBP99xHQxQ20cM9_WCT-Pt3scR382ydL0i72sNOBmOU6oUk42aluBfac3lq5v7Iv4uTzhNmQWQcwowAwzJgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5914235d7.mp4?token=hzU3EkI_pyK_x1pC8VoaQ3Axi6To0NEgGj2IeC4v_NASB4J952-UzdOtwgyyqMu0SizMwNW9AoxxUmKd-Uk4qSoxCaVSTV1FIgvnPfCcYYQilulWdIPcUwnF1HRD-kQJ7cXP36DQ6eRZeSLF8lC2doP-Xdu7YBz8A0LwdcKZYfpP5TQ0Q0BRSMjnoUyt56FX6Yg3f3MGDjIcoFVsMqNPMzUrPXA-suQt6bHsQ-ykZfu40zR1kOh6trvMQpF2GKwcKqpBP99xHQxQ20cM9_WCT-Pt3scR382ydL0i72sNOBmOU6oUk42aluBfac3lq5v7Iv4uTzhNmQWQcwowAwzJgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای سفر آخرت محتاج مَرکَب هستی
🔹
امیرالمومنین(ع): آه از کمی توشه و درازی راه و دوری سفر.
🔹
آیت‌الله جوادی: سفر طولانی فقط به توشه نیاز ندارد بلکه باید مرکب هم داشته باشی.
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/442210" target="_blank">📅 04:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442209">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1Djjo7BzYDkx3CxlbbkpnmlHdmsozsZxQdmzL58QLLiCsz8y_9u7N8nQRL52E1hXUvazVrncLkLioa1mwTW_JzwZTXW9YP4b0_SaahFtPJxC_ST4CKgpJkzaGII3bpJh5eq_6E9g2gB--hcRa1pXmBAtM824I84Pd_trb0Q73yqYTRNsTyQRvS2i7YdD5UHIWF4-z1ap1xVMH26sl2hKRCBF2PK98toVQZPxh4E7CNhTsF6RYyrEa8pPxpSiIN8ipwq6bXfAN0OrFFFE6jQM4y6-gKvG5goQilW5YXBXtQ9PEGEY1D0Yi5lkRscWgIbcJSLn-QgBDnYe49Z3m3UMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طارمی: با فوتبال، کشور متمدن ایران را متحدتر می‌کنیم
💬
مهدی طارمی در نشست خبری:  ما برای همۀ مردم ایران چه کسانی که داخل هستند و چه کسانی خارج حضور دارند بازی می‌کنیم و فوتبال می‌تواند همه را متحد کند. دنبال شاد کردن همۀ مردم ایران هستیم. با فوتبال کشور متمدن ایران را متحدتر می‌کنیم.
@Sportfars</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/442209" target="_blank">📅 04:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442208">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6V3fYlK4RqxoyhcyUvn1eZxDwfgpRzg0h7IE9jU5EE21rGL3bAcO5jCJ1ymZ-PcwdF7a81gnFNdCoJ5SuK8gssPvk2gzYJO3XHxWufAYWVoj96lqjTfK-EqKqb7rFBb6sv80V3p7rNO3VwUAk-LcyryFLUGjuo8_JtYIS_vWBUMP8DB22w-4xc0z2Twgg7P2fyC9-w0HF5_qGbn0RJ-QI0Su643b57sezEDwsHi4YKCUcY4chOKWPbkeDSswb3JGfL8urrIhSRIzqlWyR1cRs4Tx1QXmVkjOi3goAicLOICoJ5ckAzQNkzzVa-0pos62D1hqCaBHtlphj7J7Of48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس، معاون ترامپ بعد از اعلام تفاهم با ایران: مردم آمریکا از افزایش قیمت بنزین رنج می‌بردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/442208" target="_blank">📅 03:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442207">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
سنگ‌تمام مکزیکی‌ها در بدرقۀ تیم ملی کشورمان به لس‌آنجلس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/442207" target="_blank">📅 03:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442206">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou5Bm0EUq2wQdhSSj9SLMWoulhvhU4dqfScQirS2qVRQYQIYk5vjhDhGORiXx_94PShZQeGtmqpgXR-bYuwXp5USCxTPJEFm-GY_eIlUSzbHSfK9SyFnc0WatkOuw-N_bbvnRuFsHGO_FtwEnR-PknfMQQgVi3bm8cJWAz_6TiLLT5myliZZ6FFiH4krYO3LXkJJG8iKMD3PcpNtKDQovGnkyixxwcekhbCSSMWF5Nd9Dr93s4fr_BPArBktX86M8Y2539ShKapaQA2kPnzW5BGBVddBNC214uuTFAhO7F3EAl-SEAidS2PUFtFGjE4MMyyDOfwqWkMqdcZEM8vyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در مصاحبه با نیویورک تایمز: اسرائیل باید قدردان آمریکا باشد
🔹
هر توافق احتمالی، ایران را به غنی‌سازی در سطوح پایین محدود خواهد کرد.
🔹
در صورتی که مذاکرات به توافق نهایی منجر نشود، واشنگتن حملات نظامی علیه ایران را از سر خواهد گرفت.
🔹
نتانیاهو فرد بسیار دشواری است و باید بابت اقداماتی که انجام دادیم از ما قدردان باشد؛ زیرا اگر ایران به سلاح هسته‌ای دست پیدا می‌کرد، اسرائیل حتی دو ساعت هم دوام نمی‌آورد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/442206" target="_blank">📅 03:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442205">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLpqhZp8TQFP3cd-TNOj3aeO3qiPeKqCzrjVOfbI6s0nnXFtG167lch9s1lbC92MtynheWaNohM_7MRv94krFit_P_0cNM6QSh6BnEqoVZPghKEfuulkGuMwQ6GIY2EOlSY61ImIQDwD_aASfcAys3d9AmYe365nRxoGaqVmeoeoJ0CHOro91M6kdSeI4tqJokJ-7ccxR1O_OlJf-uOGkQsQ6pdbAiHDRdO1X_nJbi3Z99TBX9Onpf4Tz6ZfRXoGVkzH-vjP9kXSMco2QLRUHQvIs_G_UqLy_G_cke2pCAQkyrcM9JQDcEJ_-RIct7C97o9BeFsnknleA9oRu2_HGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با فشار ایران حرفش را پس گرفت؛ بازگشایی محاصرۀ دریایی آغاز شد؛ اما بازگشایی تنگه بعد از جمعه انجام می‌شود
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا ابتدا در پیام خود در شبکه‌های اجتماعی نوشته بود که از این لحظه هم محاصرۀ دریایی ایران پایان می‌یابد و هم تنگۀ هرمز بازگشایی خواهد شد.
🔹
با این حال او دقایقی بعد با تاکید و فشار ایران، سخن قبلی خود را اصلاح و تاکید کرد که بازگشایی تنگۀ هرمز بعد از روز جمعه (روز امضا) انجام خواهد شد. او در پیام خود چیزی درباره تعلیق بازگشایی محاصرۀ دریایی نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/442205" target="_blank">📅 03:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442204">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNkYkz7bNfXfrVoi1a5uQetFKbeWBN6tqspriufjiFKZoqP_pAdEHiy5tam6b34pmdFBSZV3jZLfwe2HB7ghwYrlkvrfNyjRVcQY3h6zi8ndz6_7CKQ_ZbcxLbVUvAz5r5965U4sJ2d3FPGqXXJL9bGa75PbagwyRSyqMHRrta6qEgSY3Q5MJgZFwu3DpQkw_qaWCQ8uunqtuPQUCdQj4MAzN7WH2NCGBpk8jlxM_Qmj60y2bFtJ5S1Bj1F0bqryYJ2D5RFSN2zXYj3Jk5MmG3O7ZqUUdtoTh8thC2NQuWNMfJ_6DV_ecfdBjywAwvX4oLyroQNAIICeeWQpKwo9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس: تفاهم احتمالاً منطقه را به وضعیت پیش از جنگ بازمی‌گرداند؛ اما با این تفاوت که ایران اکنون با توانایی خود در تأثیرگذاری بر کشتیرانی تنگهٔ هرمز، به اهرم فشار جدیدی دست یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/442204" target="_blank">📅 02:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
ماجرای تغییرات لحظه‌آخری یادداشت تفاهم ایران و آمریکا چه بود؟
🔹
یک منبع نزدیک به تیم مذاکره‌کننده در گفت‌وگو با خبرنگار فارس جزئیاتی از کم‌وکیف اقدامات ۲۴ ساعت اخیر دربارۀ توافق با آمریکا را تشریح کرد.
🔹
به‌گفتۀ این منبع، پس از آن‌که روز شنبه کلیات یادداشت تفاهم در شورای عالی امنیت ملی تصویب شد، از صبح یکشنبه با ورود تیم قطری، برخی مسائل باقی‌مانده مورد بحث قرار گرفت. به نظر می‌رسید که این مسائل لاینحل بمانند تا اینکه حوالی ظهر امروز، اسرائیل به منطقۀ «ضاحیه» حمله کرد و عملاً از خطوط قرمزی که ایران تعیین کرده بود عبور نمود.
🔹
در این لحظه، ایران آماده می‌شد که از چند جبهه، حملات گسترده‌ای را به سمت رژیم صهیونیستی آغاز کند و مذاکره به سمت تعطیلی پیش می رفت. اما با ورود مجدد ترامپ و امتیازهایی که در ازای عدم حملۀ ایران به اسرائیل ارائه شد، تیم مذاکره‌کننده قانع شد که این توافق در راستای منافع کشور و منافع مردم لبنان است.
🔹
مهم‌ترین تغییرات لحظه آخر عبارت بودند از:
🔸
برداشته شدن فوری محاصرۀ دریایی (به جای بازه ۳۰ روزه که قبلاً توافق شده بود)
🔸
پایان جنگ و عملیات نظامی در همۀ جبهه‌ها و همۀ مناطق لبنان و ضرورت احترام به تمامیت ارضی این کشور
🔹
نهایتاً این رایزنی‌ها تا ساعات پایانی شب یکشنبه ادامه داشت. در حالی که همه چیز برای حمله به اسرائیل آماده بود، با تمکین آمریکا در برابر خواسته‌های ایران، عملاً موانع امضای یادداشت تفاهم برداشته شد و قرار شد روز جمعه این یادداشت تفاهم امضا شود.
@Farsna</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farsna/442202" target="_blank">📅 02:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBeX7Ln8n1e7uOaFuslsLOcT5YDEtEir0nvcntU2ggdPydEVcqnkwe1p58jA1tZtHbW5ivM5fKYUEIpnvK1Qm0tkf9Mut3j51Avlk76WpkyQ_CzF2HlxIxaV0NvEZR-lOlkA48xH9aR-OUEhgypOj717t0T_75NJpDiQyrmyWmzdhTJ3JcTrk5JwEF4fuiwQFb6ieSgB6GnOlD4CCmV0PfgSIpHYVJ8bfHGKEZ5uAFbQuVv9az-NmlAfQLI0l0sJSscq-R4d7TwbFGPsEiepNL2q-8Ork7VGNFnkAgwssCRFSpTUEYEAIr8OFD3tmI7r3VlRlVKIlWmEG2c6Dz6Bkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بیانیۀ دبیرخانۀ شورای‌عالی امنیت ملی دربارۀ توافق پایان جنگ میان ایران و آمریکا
بسم‌الله الرحمن الرحیم
به اطلاع ملت شریف ایران می رساند:
🔹
جمهوری اسلامی ایران در پرتو راهبری رهبر شهید خویش، تفوق خود در برابر دشمن امریکایی صهیونی را تکمیل کرده و ذیل تدابیر رهبری عالی قدر نظام (حفظه الله تعالی)، حمایت های آحاد مردم و تلاش مجاهدانۀ رزمندگان اسلام، به‌دنبال یک‌دوره مذاکرات دشوار و فشردۀ چندماهه، و براساس مصوبۀ شورایعالی امنیت ملی، متن یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه ۲۴ خرداد ماه، نهایی کرد.
🔹
بر اساس توافقات انجام شده، جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به‌صورت فوری و دائمی پایان یافته و به علاوه، محاصرۀ دریایی علیه ایران بلافاصله و به‌طور کامل خاتمه می‌یابد.
🔹
امضای این یادداشت تفاهم در روز جمعه ۲۹ خرداد به‌طور رسمی انجام خواهد شد.
🔹
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد. جمهوری اسلامی ایران از تلاش های جمهوری اسلامی پاکستان و دولت قطر قدردانی می کند.
والسلام علیکم و رحمت الله و برکاته
دبیرخانه شورای عالی امنیت ملی
@Farsna</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farsna/442201" target="_blank">📅 02:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ریزش قیمت جهانی نفت
🔹
قیمت نفت با کاهش ۳ دلاری به ۸۴ دلار در هر بشکه رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/442200" target="_blank">📅 02:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442198">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVxFBLytce4XaMh_DSeHO55Kzxhog23juQp1cAfF5dR0C5hxvC_m6ZfkW7vlc1MnIpd8MWGyb2Ufc9jCAzCCrgWWzXm-8cMfR6Rhp-b_c_qww9qTfoPSthVPLq75xfo6UrMYbRRKSdqrHATCd5e-NXhfjCo94LtZrNDxuJnU3G72x9hyynCT7G3pPhQHG3Uv8913zU08hHeB0KWsbJIJvOa73cOsI00s-eRjY3cKVSJdhqgm7rbHspGqmZDKfQjDDeYHy94gIqfvLJ_0olGmJr-TBh04dlAI-v78pD2qdnubayOl5FRUyzGnSr3D8E4jdEu8IJNg1vijKKjhtvX9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مرندی: حماقت نتانیاهو بن‌بست مذاکرات را شکست
🔹
برخلاف برخی گمانه‌زنی‌ها، تا پیش از حملۀ جنایتکارانه او هیچ متن نهایی‌ای وجود نداشت. این حمله بود که ترامپ را وادار کرد خواسته‌های ایران، به‌ویژه در مورد لبنان را بپذیرد.
🔹
حماقت نتانیاهو نتیجۀ معکوس داد. این یک عقب‌نشینی تاریخی از سوی «امپراتوری شر» است. هرگونه نقض توافق با پاسخی سخت و قاطع از سوی ایران و محور مقاومت مواجه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farsna/442198" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قرارگاه خاتم: مردم و نیروهای مسلح ایران ثابت کردند که دشمن راهی جز پذیرش شکست و تسلیم ندارد
🔹
بیانیۀ قرارگاه مرکزی حضرت‌خاتم‌الانبیا(ص): مردم مقاوم و سربلند ایران و فرزندان دلاور و شجاع ملت در نیروهای مسلح مقتدر کشور و جبهه مقاومت با عنایت پروردگار متعال و تحت تابعیت فرمانده معظم کل قوا مدظله العالی با تحمیل اراده الهی و پولادین خود به دشمنان زبون آمریکایی و صهیونیستی با قدرت ثابت کردند که راهی جز پذیرش شکست و تسلیم در برابر مردم مبعوث شده و جنود پروردگار متعال ندارند.
@Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/442197" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c3048e7ee.mp4?token=ikt2LKm8g-j1D5quwWgqvD7VMcq9aC6CPHtoR1dvL9JbHZ0TYuqtxo1lF44YZC1-CA7B42VmHh9qnAMXWQTIb45w35fzejl53pSU35NiynUQIy9W9Q4CtvTj713AM2fOw7GJcYpdTppnAA-mvlmlDLNckxDMRkcfsUHjkoTr0IMhASS26NdYsdsNMppFhYum0qlb2Ir6spYqBK-k3h15eq6HwNdnnJleiGbU4eg4UtFiBqQTrbvqgTziUPkJlZdoP809_EEe-7C5MAMvQTFuQTHFrbzsRmASzoYmgP9O7036dJtUaFEGof-iwqIObk68A-L2Rzb62LPZV7q7RbvOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c3048e7ee.mp4?token=ikt2LKm8g-j1D5quwWgqvD7VMcq9aC6CPHtoR1dvL9JbHZ0TYuqtxo1lF44YZC1-CA7B42VmHh9qnAMXWQTIb45w35fzejl53pSU35NiynUQIy9W9Q4CtvTj713AM2fOw7GJcYpdTppnAA-mvlmlDLNckxDMRkcfsUHjkoTr0IMhASS26NdYsdsNMppFhYum0qlb2Ir6spYqBK-k3h15eq6HwNdnnJleiGbU4eg4UtFiBqQTrbvqgTziUPkJlZdoP809_EEe-7C5MAMvQTFuQTHFrbzsRmASzoYmgP9O7036dJtUaFEGof-iwqIObk68A-L2Rzb62LPZV7q7RbvOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: ورود به مذاکرات ۶۰ روزه منوط به اجرای تعهدات از سوی آمریکاست. @Farsna</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farsna/442196" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442195">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: روز جمعه امضای رسمی تفاهم را خواهیم داشت و روسای هیئت‌های ۲ طرف درباره تعیین ترتیبات آتی مذاکرات گفت‌وگو خواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farsna/442195" target="_blank">📅 01:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: تا زمانی که آخرین نکات مدنظرمان را وارد متن نکردیم با تفاهم موافقت نکردیم.
🔹
گفت‌وگوها تا یک ساعت پیش ادامه داشت. @Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/442194" target="_blank">📅 01:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: به‌زودی متن تفاهم را منتشر می‌کنیم و مردم خواهند دید چه میزان دستاورد داشتیم و چه میزان تعهد دادیم
🔹
تعهدات ما در قبال دستاوردهایمان قابل قیاس نیست. @Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/442193" target="_blank">📅 01:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: اقتدار نظامی امروز به پیشبرد موضوعات ما و نهایی‌شدن تفاهم کمک کرد
🔸
نیروهای مسلح ما آماده پاسخ به صهیونیست‌ها بودند. @Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/442192" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🎥
غریب‌آبادی، معاون وزیر خارجه: هرجا نقصان اجرای تعهدات طرف متقابل را داشته باشیم، متناسب با موضوع، اقدام خاص خود را انجام خواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/442191" target="_blank">📅 01:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e31d731a.mp4?token=Rjle7hZLsFz1lEvesAiME_qOQGbEI300J788vfyh4iHEnpKWr47d2Jo8KzERFpLUaAks3_tY5BDn16LcLDV5OfLLUKyDQwwM-nWCRDcJFLb2WGgdGSOD76f5HteqyZxRF4Dmj045_i_OwvEpFYWS5_sc80Y53shD36VEqzCB2g497AX2YKZp3xuN1SLOEN51n32F8uFq_W7ez7Lqkf3YkmUJaiWg9pFWvdU0SntPDVbGcs1brhs9_EbBUI7CTQChuBINaIitNwNiAy0POZRy_5vKqAFh3uPLzt2dSqHV3ntla8WwBewTjcf-qgLKKsDyJvuNKQyQ4QoM8pOQl-t1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e31d731a.mp4?token=Rjle7hZLsFz1lEvesAiME_qOQGbEI300J788vfyh4iHEnpKWr47d2Jo8KzERFpLUaAks3_tY5BDn16LcLDV5OfLLUKyDQwwM-nWCRDcJFLb2WGgdGSOD76f5HteqyZxRF4Dmj045_i_OwvEpFYWS5_sc80Y53shD36VEqzCB2g497AX2YKZp3xuN1SLOEN51n32F8uFq_W7ez7Lqkf3YkmUJaiWg9pFWvdU0SntPDVbGcs1brhs9_EbBUI7CTQChuBINaIitNwNiAy0POZRy_5vKqAFh3uPLzt2dSqHV3ntla8WwBewTjcf-qgLKKsDyJvuNKQyQ4QoM8pOQl-t1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: در پیش‌نویس تفاهم، تمامی مواضع خودمان و موضوعات مهم گنجانده شده است
🔹
پس از امضای رسمی، متن تفاهم‌نامه منتشر خواهد شد. قبل از امضا نیز از طریق رسانه‌های عمومی، ابعاد مختلف یادداشت تفاهم را تشریح خواهیم کرد و دستاوردها را خواهیم…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/442190" target="_blank">📅 01:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🎥
غریب‌آبادی، معاون وزیر خارجه: پایان فوری و دائمی جنگ و عملیات‌های نظامی در جبهه‌های مختلف و از جمله لبنان، از همین امشب اعلام می‌شود
🔹
اتفاق دیگر خاتمه محاصره دریایی است. @Farsna</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farsna/442189" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ffc4fe9c3.mp4?token=GYk1C0bDRuAM0BPul_blE4_RG3GXTsDSCT8t5k-mDpooIsOn5uCCLI7IuXuugpveDKpPG6pMB16SyP-ce4u_A2ciYVxk_VmsJKlnQmFh8c1GwIbL3yEbnJt6FdUC6xvNgKJDyzqX17M24ag-rlj_WPFmYdjZhf8ib7w9VYj8OoFFaGMRRj4eeC337ydyRNWqQELNeftflRzh-5vfT3y36EWlrw7UqGUG29Z-1hrYnVIzZ_sy2PQq4cpsgbh4nQw-LBq61_35mhBlMZ-zZBwPfDc1Hxg5v9fwYx5hHXlt-iFdwRus15INo4YGpHWBF8RmfRr8F9AWB3geHweiEU2oyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ffc4fe9c3.mp4?token=GYk1C0bDRuAM0BPul_blE4_RG3GXTsDSCT8t5k-mDpooIsOn5uCCLI7IuXuugpveDKpPG6pMB16SyP-ce4u_A2ciYVxk_VmsJKlnQmFh8c1GwIbL3yEbnJt6FdUC6xvNgKJDyzqX17M24ag-rlj_WPFmYdjZhf8ib7w9VYj8OoFFaGMRRj4eeC337ydyRNWqQELNeftflRzh-5vfT3y36EWlrw7UqGUG29Z-1hrYnVIzZ_sy2PQq4cpsgbh4nQw-LBq61_35mhBlMZ-zZBwPfDc1Hxg5v9fwYx5hHXlt-iFdwRus15INo4YGpHWBF8RmfRr8F9AWB3geHweiEU2oyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
غریب‌آبادی، معاون وزیر خارجه: متن یادداشت تفاهم نهایی شده و امضای رسمی یادداشت تفاهم اسلام آباد روز جمعه در سوئیس انجام خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farsna/442188" target="_blank">📅 01:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc9f565e0.mp4?token=EdQD0CO7XO0ZoM7AxU0AtGNzIa3Y6LfadxCYg6X753r3zoLgDncxE-NghqaaEm-0VyBXS8bU2C12brmTl_DHNGG6WyJtqxNT7tLirza5B9UZO9ibqIhUzHhFCCiIYD_NcmLby-lzg3p4geDJ_2XwRvhun7A4fZq0BXBeRjNUrJtzNATxfz87fuZacDEFcnzydEpxlZlOH4zVkjfCcksnB3Dsy6taMhROn7Tu8iElDsGkli-fLnAnuJ33gEc_7MgPUkWEm1-RcMZ-gh0Bd8A_jX_mDK2dSQfFokEhkL3c7ew9wZjFWglsdgowZxqdqzjKJQ07FtcU9m5qcSylJ5O8dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc9f565e0.mp4?token=EdQD0CO7XO0ZoM7AxU0AtGNzIa3Y6LfadxCYg6X753r3zoLgDncxE-NghqaaEm-0VyBXS8bU2C12brmTl_DHNGG6WyJtqxNT7tLirza5B9UZO9ibqIhUzHhFCCiIYD_NcmLby-lzg3p4geDJ_2XwRvhun7A4fZq0BXBeRjNUrJtzNATxfz87fuZacDEFcnzydEpxlZlOH4zVkjfCcksnB3Dsy6taMhROn7Tu8iElDsGkli-fLnAnuJ33gEc_7MgPUkWEm1-RcMZ-gh0Bd8A_jX_mDK2dSQfFokEhkL3c7ew9wZjFWglsdgowZxqdqzjKJQ07FtcU9m5qcSylJ5O8dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
به گزارش فارس، دقایقی دیگر بیانیه رسمی دبیرخانه شورای‌عالی امنیت ملی درباره توافق آتش بس منتشر خواهد شد.
🔹
براساس این گزارش، ایران پس از حمله به ضاحیه بیروت، مذاکرات خود را لغو و آماده حمله به رژیم صهیونیستی شده بود. اما در نهایت با امتیازهای لحظه آخری که…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farsna/442187" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
به گزارش فارس، دقایقی دیگر بیانیه رسمی دبیرخانه شورای‌عالی امنیت ملی درباره توافق آتش بس منتشر خواهد شد.
🔹
براساس این گزارش، ایران پس از حمله به ضاحیه بیروت، مذاکرات خود را لغو و آماده حمله به رژیم صهیونیستی شده بود. اما در نهایت با امتیازهای لحظه آخری که از سوی رئیس‌جمهور آمریکا ارائه شد، از جمله حفظ تمامیت ارضی لبنان و عقب نشینی اسرائیل از مرز لبنان و رفع بلادرنگ محاصره،  متقاعد گردید که از انجام حمله خود صرفنظر کند.
🔹
همچنین مقرر شد نظام حقوقی تردد در آب‌های خلیج فارس با همکاری ایران و عمان  تنظیم شود.
@Farsna</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farsna/442186" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">متن کامل توییت ترامپ دربارهٔ تفاهم
🔹
«توافق با جمهوری اسلامی ایران اکنون نهایی شده است. تبریک به همه!
🔹
من بدین‌وسیله بازگشایی بدون هزینه و آزاد تنگه هرمز را به‌طور کامل اعلام و هم‌زمان با آن، دستور رفع فوری محاصره دریایی از سوی نیروی دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های جهان، موتورهایتان را روشن کنید. بگذارید نفت جریان یابد!»
@Farsna</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farsna/442185" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442182">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ: به‌زودی بیانیه‌ای صادر خواهم کرد که تایید می‌کند آمریکا با توافق با ایران موافقت کرده است
🔹
این توافق به‌صورت الکترونیکی، یا توسط من یا توسط معاونم ونس امضا خواهد شد.
🔹
توافق شامل تعهد ایران به عدم دستیابی به سلاح هسته‌ای و بازگشایی فوری تنگه هرمز خواهد بود.
🔹
ایران هنوز موافقت خود با این توافق را تایید نکرده است.
🔹
هر زمان که آماده باشیم، مواد هسته‌ای را تحویل خواهیم گرفت و این اتفاق ظرف یک یا دو ماه آینده رخ خواهد داد.
🔹
من خواهان پایان یافتن حملات هستم و ایرانی‌ها هم می‌خواهند که جنگ تمام شود.
🔹
من هیچ‌وقت به دنبال تغییر رژیم ایران نبوده‌ام.
🔹
بازرسی‌های بسیار دقیق و شدیدی از ایرانی‌ها به عمل خواهد آمد.
🔹
در این توافق پولی به ایران داده نخواهد شد، اما احتمالاً تحریم‌ها لغو می‌شوند؛ باید ببینیم در عمل چگونه رفتار خواهند کرد.
🔹
محاصره دریایی اعمال‌شده علیه ایران موفقیت‌آمیز بوده و تاثیر آن از حملات نظامی هم بیشتر است.
🔹
نتانیاهو از این توافق حمایت می‌کند؛ این توافق برای او خوب است چون تحت هیچ شرایطی اجازه نمی‌دهد ایران به سلاح هسته‌ای دست پیدا کند.
@Farsna</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farsna/442182" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌ اصرار عجیب ترامپ بر امضای تفاهم با ایران در روز یکشنبه و آزمونی برای تیم مذاکره‌کننده
🔹
ساعاتی پیش، دونالد ترامپ، رئیس‌جمهور آمریکا، بار دیگر تأکید کرد که «یادداشت تفاهم» با ایران روز یکشنبه امضا خواهد شد. این در حالی است که مسئولان مذاکره‌کننده ایرانی…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farsna/442180" target="_blank">📅 00:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442179">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT2PuzRqddz21upClgWL_7Tk8dvV9X0ZY9NT8uJXwp_hT1rtfucZJnlTCDzFvR77AaOu6amoZ0cTlLqWiZv3MxGCQ8M0rtxt90p2OBVcy1J0H6JsQV16g1yKKh_eY--yUnbveI-DtjMzH215kTQMlakSjjrYNIjiJLlv60ipacWF1VI4ZnHqr8t4AZ4I8CjVLfdyh8E0_tPPJkgO3CKMpZ3D5FvJTOdk15kdC7q-TRc9byuwTNv3M4Nw6b2kRDdFEVRbxOS8REqtc2_h2u8F8La7P3EWbjXZNRK23xZ_JT0N4Dcy5TOANsNca71UOpkLEf9KoXzruRgp86rs3yA_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بمباران‌ها خاموش بودند، امروز برای باخت تیم ملی فریاد می‌زنند
🔹
طی ماه‌های اخیر، گروهی از افراد که سال‌ها سابقه فعالیت در رسانه‌ها را در کارنامه خود دارند و در جریان تحولات تلخ گذشته، با ریزبینی تمام، هر گزاره و اتفاقی را حتی در کوچک‌ترین جزئیات بازتاب می‌دادند اما در کارزار جنگ رمضان و میانه اتفاقات تلخ خاموش بودند، ناگهان هدف جدیدی یافته‌اند، تخریب روانی و ساختارشکنی تیم ملی فوتبال ایران.
🔹
این جریان که با هزینه‌ای سرسام‌آور نزدیک به نیم همت تجهیز و راه‌اندازی شده است، با برنامه‌سازی‌های فریبنده، مصاحبه‌های جهت‌دار و تحلیل‌های شبه‌کارشناسی درپی افزایش فشار روانی بر کادر فنی و بازیکنان تیم ملی فوتبال است.
🔹
آن‌ها می‌دانند که فوتبال ایران دارای عمیق‌ترین ریشه‌های مردمی است و ضربه زدن به تیم ملی در مسابقات جام جهانی، می‌تواند بزرگ‌ترین ضربۀ روحی به جامعه ایران باشد.
🔹
به همین دلیل، با صرف بودجه‌ای سنگین کارزار وسیعی راه انداخته‌اند. از تولید مستندهای جهت‌دار گرفته تا مصاحبه با چهره‌های به ظاهر بی‌طرف که هرکدام سنگی در مسیر تیم ملی می‌گذارند.
اما هدف این افراد چیست؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farsna/442179" target="_blank">📅 00:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c0d096897.mp4?token=JMDWimDMFf73soLK3zVLH99uzqOAJIqjM88dRulp_hga0IF4R_FsRDcSObrONeq-MwCG-leRzXAsVJlo4WvDi23fIKTmhffoCUYr44q_faTlzYnnA-DE93Jd-rcCHazHbHbc7kZdEq0_0Fnnn96w2xKiT1L1SSsST_hgqXwRMkCQHPf8n_LoX_I3Uw8m1MYDQ-7FmfN6P_m5qX8jiOHSEgkEEDIij_YJ86Q9MUMqCjQ0j64j0zxPm4z-Vnne11Ln26S3Uirygh0cJnMwZt5aVJ_FQ_gi-RSg0YpHxVEm-J7te0gdWd_Cj8a4M1Y1ZWvxKu5I3F1piLBFoY0oesda-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c0d096897.mp4?token=JMDWimDMFf73soLK3zVLH99uzqOAJIqjM88dRulp_hga0IF4R_FsRDcSObrONeq-MwCG-leRzXAsVJlo4WvDi23fIKTmhffoCUYr44q_faTlzYnnA-DE93Jd-rcCHazHbHbc7kZdEq0_0Fnnn96w2xKiT1L1SSsST_hgqXwRMkCQHPf8n_LoX_I3Uw8m1MYDQ-7FmfN6P_m5qX8jiOHSEgkEEDIij_YJ86Q9MUMqCjQ0j64j0zxPm4z-Vnne11Ln26S3Uirygh0cJnMwZt5aVJ_FQ_gi-RSg0YpHxVEm-J7te0gdWd_Cj8a4M1Y1ZWvxKu5I3F1piLBFoY0oesda-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یمن: نتانیاهو بدون چراغ سبز آمریکا، دست به حماقت نمی‌زند
🔹
وزارت امور خارجه یمن امروز شنبه در واکنش به جنایت امروز رژیم صهیونیستی در ضاحیه جنوب بیروت، تأکید کرد که تجاوز امروز، گواه جدیدی بر این است که رژیم غاصب، خطر واقعی برای امنیت و ثبات در منطقه و جهان…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farsna/442178" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442169">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/baq0hdXZRGvUzaKLnCSsQydRIbqIViG-hKzQUxWSVASsKWorEu1oRv9kZmrAwCKb-Kppm-ngVcI5pGxruLSU1jGCNyom9BHM1LdsP_eJEGeGAMtyoArXVVDf2LdL1DnpG_wuIbbcq-4J7gFP0NooEG-D9zJPGiXSVXjdzioFTO1kQ1-1aZz7RwAyWg9eqLhv2ak8gpN0AD2rk_3Prch3BoFlYK7ssEKovN9Hbx06Z-D66fLRqVKryCFvDmg1myz_ppPFV_hIueClURkeq0_5qpLZNlo5Rq3DjQgDCQryxopZ_v7z5XxUKYAzeDZoB-gBN3ZqpObovFTKqNVnTOnP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFVBwngFiNDS-lA3DKoxjsX1YNlJxnHf2T3fN8Z5oEaToi8j7uKaK3yo5R8rj534REmPTxMWvYbz0y0vxTKIoNNVUJDyoyA7AY6eBoEak3YtTXP10BD7TyOmlw-4K_uBLXzJ9nfs2pTXnx88DWeOPMyJuhn6WYTpOks81QvFJuKcrXL-qz6tEDaRiAnoY01xd42lnglV6PcevrPnLhhKT7p0-vwv2eijqaK5A40rEjb39QaMvxM9nFnB7NV1MCmcV6olmkOXDbrWf2pMuyOgfmp_fZAPqbe6HU0rjxub0_adDARWcAJBJDrQgIA6kUusjroDGZzo6wfsNa5LSd_3HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6X3jxg0EbaHCvG8enuFJbT5qthxlRlVE3Km5Q_TRr-Ynawdekv0XNpy7oBT9hRYpVZiQWjTxHmYj29gLBNAaptyDPRST4YGa19qhvD-rWOB92xu6q96U6LIvCIKjR-0qbP1W0q_T7vaHI0P4XvMhIIsD5VIKQ692JxSUFb8xJzg-lDLfA6sTMg7tiJF79qkp1KMMixUbrEQErqFb5qRn4Vy2KrZyL-jzhZTUmZLotvouRehsybnUHhHJ0QuWWp09IkSNQOohErmE47tMGafveJLCTg0W6wZzuLIA-RgdkCRz5EDGRhUg2D0pj8i9SEl62svglMmAaSJzbwYvDUFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qx4SppWdHTsIyj0X2uqTD48OOm5W_jjMad1Qp3ONs7kmakdLgND7iL3p3r1EREdw1Ppk7iPa5U6-t-Ssf1dtvcD3PDBopW7YrRKIfwbAb5gGITDO4ZsLgIIwjtn3ug7aLqbJmz_ag7xtgNmqAsvyVOXJLQ4P62hm9rUuskzKkRCWWwkIRFO3CZantvjfuygfxYFBrG2R8ute8EEa_Sh7AJgocpHikdDrVzWiFUD1HEVo8hEicY-kDb_-Y4tZuNnIiGT3EoYa5ReLHF47JMW5HR7i88kZYSt0kYhRq8KFANRApRyPdHrIXs9vcc5MU9xbTiDxW9BGRFxj8CshxCdY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pw9m_oNsvb7E_S7DJMsZUgR-BBrKI1PSN_WQyWuHQZco8HujUnEF9-huR7UjaWEA3ZIGvnH316-NCk9wh2xJWXN_UCF4QROd0SD9dfAKIs9tvJZ_5zvQmnK3nJcqWS4c-8MWw4IBX4rJSIRevL7cH8rzUCLo32g8hIiqq6Xvs-vUDP4-dQt1GQkkJMMAQs45gMaiV2rhcwF-lzboGR40EaJT9KfjkevpIkqAhCkxYhFuPO_-zlpT2j8NaPz6uaR1N86PCFoXHiW-eK09LvjmsB8EzPSm3AMfxTUNGF8qWUVAKkP4T62jBdplIxpXp4bzhY-Wh0WsWJaJkbfssVqXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItXn89iZepTMb6XG9jRgMVVHKbZb4QdPtV_gie1RCfy4gqsfp_R0xe8oilDjLNgq-EQR5WLkmO1m9_T-afAllq_AuWev47Rr76leNezS3alfYejD7M_8yZDGJl66cqLvYdhA4zqhXypxjX0CQHNFB3OxbZMseURxs51ik99hyi0U2mYJ4vHOoOI9WpaPD36muyLKF5qn0RqO8elBg6CotPP3LSpAelEb0k8_I2kCF7MCKmUv_Dt41SvIrDAXCu7LCgrahm9XL5moEfWM6X9DiMYEzqdWLJXUV5kLen3CXBsBLHsQ3qsk2NcT6A-JJ8O4aMc0cd8yXk56emaHmUX8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Juuo71Xc_3vWvUiv4rpmbq9fzrvhm-xZRYfqAOXlrCTctRicEljqrL3GiYQbFVBOELosFCpesoneihOsUUZrEeQhx1t0wcwUAikMax0YpbDOYrp0e-jCuilbVfeKKcgSuarnyZ8cw3A0xNag2PYrmT4xp-Tw6ZNKkLBq2XL7o8R7VB5ASL0xB3ZY79UZWaFX6tYdNDyVkKaHrnS4v-c6xrRrgiREaHz2jridUkDuE6h3WRdSER2xmALmz7AG3tjh9g82bzn_5mlvfW3J7Mn276AJOdFl8Z9zDto_EDPhUFpiT1KFFNA5nd7XmjDLOR_xD8KcOhJJZkaB0sayJnqVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPYZf6nIabZLYr6rNrSY5my1XJvKXpsYsMl0scqN_twpB325UbC7fC75m-vr9G3FowSKQGchqs5ARAhGijdl3nP59J5NkmZClXt4e4vxaIIDfJU5Drq4ZqUkEO0qL-nRvxdgzcAE3NL_qnsf5X_4Hbb1azYyu20x5Vv0_KaXbIaK7vi7a0YWKIzfjXu--V2DBswjviAi0uyJ9bn0rzbvD95d0ytQgMRIHOFePtmF-dQAJEb1pcRTL-ulbCyAsjp61zQ_sYiZ7-1gbQgWr9XVxZii5JSuVmNKK49BvkbNCfNML8w3U5dlPeU7XiX7zdlFcHbPTM_ADQfazQqCo75goQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ra7oh0kqxi3wPBrBCzzx4Cc0VYJckzANLERpwKym9X3RdUFRWGA__khCojPlRL-VELCkHm8p7ee0EIA-eek4LGR-8tZPvW2Ky-uvxjEuHI9-MJRaanjCTIufccbSrTMFFnD9WIlVGvkfmgt0pH_-pWzKEv6CzrESu0XjccetJxZEuSFX1i5CAJ55mOjD2Z7iLXELb492QmHlzWkauZP-f1qMwsjr25c-YiRFg0glTIIgE-3bBM2WB11E0_Qv2Wh1b_w-T1qW_IZwLB_PQrA3G1FweyXzifknj0RtquMefMfTeTnum1T9ZJ1_Mgo3L3UTM3oWChoNtqwj2BkoZLmJxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌های ماندگار به‌جا مانده از روزهای جنگ ۱۲ روزه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farsna/442169" target="_blank">📅 23:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442168">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-text">❌
تکذیب برکناری سعید جلیلی به نقل از عظیم ابراهیم‌پور
✅
عظیم ابراهیم‌پور، شایعه منتشرشده در برخی کانال‌های مجازی مبنی بر نقل قولی از او درباره «اخراج سعید جلیلی از شورای عالی امنیت ملی» را تکذیب کرد.
عظیم ابراهیم‌پور در گفتگو با فارس:
✅
اولاً: بنده سردار سپاه نبوده و در کسوت بسیجی تا سال ۱۳۹۸ مسئول ستاد قرارگاه پیشرفت و آبادانی بوده‌ام و هم‌اکنون از خادمان ستاد جهاد تبیین هستم.
✅
ثانیاً: خبر منتسب‌شده به اینجانب درباره آقای دکتر جلیلی از اساس کذب است و چنین مسئله‌ای هیچ‌گاه مطرح نشده است.
⚠️
دشمنان و معاندین با طرح چنین شایعاتی در صدد ایجاد اختلاف میان نیروهای جبهه انقلاب هستند.
@Fals_News</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/442168" target="_blank">📅 23:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442167">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXHfTTvy6vL_VBjcC-JxElHt0QtzLMMKm2S0GKdqqmzL_CymSNGuUreH1zxRc8DL-vLKrTLExmTxnQA2ruiQYHAl7fZgLE__9Txqy9zeEVhpHPi353oUruTqoR3wRG39XfJLCHNMhsGpEd0ldUGTtjLLgF1RmaD39PZevZAglPnRwEEA_EfYvzDODm8b21sjtVfnA1gxRuXYEIEM0TELvm6a-p3rdpONgt1oXHyxOesMcwemhCAXAHGr3nqnjFtEnaVE7GlxxMxmFQVGRwKMAhvM2d27IlQhysiaN1eOtfJ18Ntz_ylQOzhXqFT4hN50d1nRG6uwrlM3vTEGGfrzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی : ساعت صفر فرا رسیده و پرتابگرها درحال آماده‌شدن هستند
🔹
اگر آتش شیطنت در لبنان خاموش نشود، ۲ بازوی قدرتمند جغرافیا یعنی «هرمز و باب‌‌المندب» شاهرگ‌های اقتصادی‌تان را تا خفگی فشار خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/442167" target="_blank">📅 23:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442166">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inNs8MXK4G_IqQ-dMobhUMySDeQKUJcM5hSPcJQGGrESawH1DVxOL9gKzTCqwFM4rEwB1PLWy0DJeG5p2GhG3xlgjkTRvJgDJ_cbIAeGHRLTzL9UslfQHWinQPiLuvBzkHJ3RxZP41daq_v8hvF1RMGFhLeBK-bW689uY8-b4G0DUHqwa__-xcIKdUazZilgXvCdvPEp0w1FM4DxM1jhdH_Beqmxis6MEp_98jpyhOSGdyv9DbsDg9Tn9DS1zlOkH9DgAMlNi1xtTvUHEqU6MLjsWdR_djSboRr1vbp8yH0z1LyVhR40pLFVbUN_YSYDQqZIlkAQ0e69r6bzI2AAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حسین شریعتمداری: اهانت به مسئولان، در شرایط حساس کنونی قابل توجیه نیست
🔹
بدیهی است که خود حضرت آقای شهیدمان نیز نقد منصفانه و خیرخواهانه را ضروری می‌دانستند چرا که اگر خطای مسئولان مورد نقد قرار نگیرد و درباره آن روشنگری نشود، خطر انحراف در پیش است.
🔗
متن کامل یادداشت را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/442166" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442165">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b055d46b.mp4?token=OM9AuqYyQ26At0ZgIDuP0xAtY4HwDqiAy5JFGOlc7vPOjinFS_raUivRlOMs8TKZ_6IFCzCo18ILMbRnVqgZBsEe3HyNeDBHtVav5DDmZejcchk_2_nyWEw-wYHh2ybgo84pwgd4mhS_6YlFJNb97x_MchNnmTS6BhWiMGLPM7SuAJ51VpJzE2i00p56KXvuYE2TG7sdKEfSxjm16QsXY2J0g_WIwoLM4-o-07hQI22k40hVGN-U__ei3WicH6ooYdpV2VEh3etKeYQD7Ya_-pf6YXUTbDa-OMGrEazVd8Q9OYSCpSwmBoMQjaV0TxxZ6ph_1iH5fHnYr3MK7gLxRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b055d46b.mp4?token=OM9AuqYyQ26At0ZgIDuP0xAtY4HwDqiAy5JFGOlc7vPOjinFS_raUivRlOMs8TKZ_6IFCzCo18ILMbRnVqgZBsEe3HyNeDBHtVav5DDmZejcchk_2_nyWEw-wYHh2ybgo84pwgd4mhS_6YlFJNb97x_MchNnmTS6BhWiMGLPM7SuAJ51VpJzE2i00p56KXvuYE2TG7sdKEfSxjm16QsXY2J0g_WIwoLM4-o-07hQI22k40hVGN-U__ei3WicH6ooYdpV2VEh3etKeYQD7Ya_-pf6YXUTbDa-OMGrEazVd8Q9OYSCpSwmBoMQjaV0TxxZ6ph_1iH5fHnYr3MK7gLxRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۰۶ ایستادگی قمی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/442165" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442164">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffbe4213e6.mp4?token=uFmk7OH6DdnqtezjFn3GvsItAiyPh9WtZMNlDfdjsCHWjQYUFJJJldUmF19VPeq4LzZ3XssKBnHRtNDbgAS57Bw1GMFaKZJSQ2MLCf8lCVqnwhr08IQ7ZVxe8PApVGpk7FMLBLR_U12s2p4JQhbaT2hE-OgybrAGsTzBwngDpOAVK2GsS0x7GQW62mHB_5Q-tqVOT0NU0FYj8l4RBbYz6_cV-tO7o6bMPDXlQ82PqNg8-tlD7SkudC5Zo7ypbo1geQPkL2S3dzFPcHpgKMnrCm0BqCyCIyCM9cRWLrgzksaZKbUewjnayAS0_xEzDsNb2u3JBDzNUPiKZLaQkVjs5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffbe4213e6.mp4?token=uFmk7OH6DdnqtezjFn3GvsItAiyPh9WtZMNlDfdjsCHWjQYUFJJJldUmF19VPeq4LzZ3XssKBnHRtNDbgAS57Bw1GMFaKZJSQ2MLCf8lCVqnwhr08IQ7ZVxe8PApVGpk7FMLBLR_U12s2p4JQhbaT2hE-OgybrAGsTzBwngDpOAVK2GsS0x7GQW62mHB_5Q-tqVOT0NU0FYj8l4RBbYz6_cV-tO7o6bMPDXlQ82PqNg8-tlD7SkudC5Zo7ypbo1geQPkL2S3dzFPcHpgKMnrCm0BqCyCIyCM9cRWLrgzksaZKbUewjnayAS0_xEzDsNb2u3JBDzNUPiKZLaQkVjs5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۰۶ میدان‌داری مردم بندعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/442164" target="_blank">📅 23:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/El5sxq7c1zI2cSSSDKV0A338CuY19tw9LTaPtV4gnk1a3K2vweLU4HBW7VokHHU1KeZWNzhzdhanEX953QXjCTuxsjwyxdJpq2imkSyAKqFopiuZyKbd3Zl5BCdG4bl0GifVof0OdjYTihaU3pkJ417TGc8yunZvnri6291zJ4mR9XEaguBlJgN5JxvY-PeU_qLpkrIOv_H7zGbsPpnyxSVlVgLc_za-d0PWv9VM8JBH1npSIA4UrFYwqTiPNcMlvueYLYpXZiBqnY6ZxM5zsgYA6tBzlXPUrLAkWOIdqb0tlBsooYwvlPwp9cNwKiiJ4_f7JIFxIwaJRInQ_H4y0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVNUDzA7Q44wx2VyuXIZnSAHfZLnRoorwHLKMrx2l7Qlrt5EYUh_B-TZ31edFUcgHsg9ZzmkOz0R8WUVCfn1_b6PZWVwStRNe-DFuRU3d7wsY6tiVxptCOyZTZfQ_1DgOsJ8xpB5XVR2UFCeLEDSQ8n2zT9ci-3oZb-hN0JKA-vqprx-84DCoAWh8GPwdnmSUmtHbkLk6AOsL0bWEoJXOV4L--wXBGSnMhSme5lHRxCxR3eEfbZLItVc64EmwjGm-IhIjXuFpQeLRxh-l0IAV-Gyr__EvCtEAi1SpZYT3VlH021FYud71cr65g2XSFgOgkqeA6nbQ2sRx15mXx7JBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULWNu0JeuR2XBcIsJy6KZ1O9n1YcRSpX7FY8zVX1IVqWrKL2MdVfSejk0R9f1y3oEl65RQlXy9Seh4WkGQxvUssQ2u8CWfD12Z1wjK-n3vQwI8KFU7p4UghF09hc2QUZdu81soiAVwxMEMq4JuMeIp-UY-qtNiCqr61NDf8cWoH6FQLZVS93qxbvGhDC3Sb_bGVgPc9qDrZIjMd8zKDuo-mqUtfdbW_FGF8Tm5QpteGj9AZej1IiMZYXcy9oYKlohNKeZh5QLEVBQ9-qBLJW1bY-sn1daYixekd1j8nQoW9It0pvmhZjrVB1yOPMBj3YNCvPZbqv27b9Dwu3oFfoZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PaLNwuzN_rL2XdjABWKXRH9IahBoOAFrw2v9x-8kqnnMBhZUPPS89mN2q9Eiqs2GC_24Qet3yALZkCvtiTuNV0QggPzXAGXiYyDdycPyfMIyW-O-Q8bsRAng90m9_qrpssKLDPhEgy_b6F97kGHU-uBgFSFcnzyJxwdHWidppzRH7qLALykSqSAFIzxbtq2Rt0KWEdg9NZq7ZrcTx5INani2SxmOXV7xBo24oDfTnIM3ZUDkqvjGCCOZxAyVeFRrj4eRGn8Ta4wEisq4GXJmKVCkBHdfJT5fwHjrZwP6xyoobyCe6-RHPsEJpeGExLoTaDQklineFYLCcVaMF5-80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAGFYxAqUBqBKLcSOH5N_dBpCu-u-OR86A5VkivZAhzN-Qs_-Ay8NwMVXfJgj6rEnbqK4gFpZ3p4-Q5_TilvcrLJ0tVtxURW32THeA6h3_1A-sSYiwPusDTWjosBWct051aboqlo9hIupT7-ctaRORd1q3RdeLLCYiqhmEJMEKYTF3-EpMgMlnGU_bkfRzFrFFCsmCmc7tIslSR-f-CTkszNRKlo94Wqr8MqVvhngo--wS-B4qd1FiP5O8TJ7mcY-rkVuFnK_gpEm0tiQlphiWfM72wy8hhgOHsM4_dmbybrEiADU9H_bp2rjKy4oTbLwoxFvLftSmDtFO02Clo8bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با فریاد ایران
🎥
بدرقه  تیم ملی فوتبال ایران به لس‌آنجلس توسط مکزیکی‌ها  @Sportfars</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/442159" target="_blank">📅 23:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442158">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88aa74817e.mp4?token=ijx2oZwiWwnx0jpItnvb-chcEB_aHrsKcg70YujEn3S-G-pN09qd9gZ1V1sMgP0rmVtJrjO08bts32IUR60dovoIcB0ZzDRHtz8zr-9J8qX1KJ0ytT2eoD8ffGwO-QZljJwlfT7QFA2gNHXSNy1B4oq0l-f9epn7YsLGd_T8v3os2uorZjekV66iAI8JrANWR-S9uhLARbFBNMVkLKRqYSxYPl0a_cPSKV2sYVi2FeD0EEd-He0cQ31kfg_CYwMHmyYGlTwhGvJN8dZsRvDH02OjF1nMJjRUUbKhG-cjgboxHXK3a6HP3yRX-w-1eO2Rv2OfjDtIXU4EjWhm3EoQhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88aa74817e.mp4?token=ijx2oZwiWwnx0jpItnvb-chcEB_aHrsKcg70YujEn3S-G-pN09qd9gZ1V1sMgP0rmVtJrjO08bts32IUR60dovoIcB0ZzDRHtz8zr-9J8qX1KJ0ytT2eoD8ffGwO-QZljJwlfT7QFA2gNHXSNy1B4oq0l-f9epn7YsLGd_T8v3os2uorZjekV66iAI8JrANWR-S9uhLARbFBNMVkLKRqYSxYPl0a_cPSKV2sYVi2FeD0EEd-He0cQ31kfg_CYwMHmyYGlTwhGvJN8dZsRvDH02OjF1nMJjRUUbKhG-cjgboxHXK3a6HP3yRX-w-1eO2Rv2OfjDtIXU4EjWhm3EoQhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مواظب باشید هنگام خرید لوازم خانگی کلاه سرتان نگذارند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/442158" target="_blank">📅 23:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442157">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf32fb4c1.mp4?token=um9bz7kVWfyKMnCT1V4cg2w34sZXA450vDDCSQgAZG2S60mBf1jPE-__NU5lyybm8MpIBvjqYLOJDHjhBsqfydo2NZWdV_L0OScRhjM2jJHp2z6YNMxwYG9ifFaYaEl7GoMN70Vx-bzPl6fZqDvsnnSCcuOC6CYS3D2k0gj59ndXdlqux6Yc6RIaChVw0GxgwLdxsLnXBUJ7wKQ_g27dQPpv5Kp0Gnn44TjCpGBuaLjf0vowZJLc-taD4ZfWci2bFL47LClZnn8-hH8HE2XKZoyQrAQf6uH4dF7NNI9Ee82bOTRK-IAw6yjxP_bPhUuyj6UF_RCFJ-p6ZaaVCWnfmX46LA7PFvAnvSBuMFlfyu3JKaGAITFYkTnGNCcZM1PfbrZxc2cAJ1efeehaJJy9g58MfJmZmAsQjb9O3EvvqsjLjVJyubm_UOA68C5Z6d5c1Jsf4MtVWgDcVsjtZS9gcIrmMvpm-jPGPgRulPAGHy4eUQ-D1MoPosZHZkA6jk51fEnRWvXc0DDrVYeBd7bwyXmTS-c9CX8T0Qsb81Mw-xjYG1_g6v2HKgcp2OwHcVIV4OR3HtW3R7m2pbiRZfe4WF-__WM5zHVZTY0bRPtHl8UMwFtCpBUJFdO-Wspihnv37g1kNZk6B3hfY4yg_WRbJKCMASy_-pxt2tILlrlgURY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf32fb4c1.mp4?token=um9bz7kVWfyKMnCT1V4cg2w34sZXA450vDDCSQgAZG2S60mBf1jPE-__NU5lyybm8MpIBvjqYLOJDHjhBsqfydo2NZWdV_L0OScRhjM2jJHp2z6YNMxwYG9ifFaYaEl7GoMN70Vx-bzPl6fZqDvsnnSCcuOC6CYS3D2k0gj59ndXdlqux6Yc6RIaChVw0GxgwLdxsLnXBUJ7wKQ_g27dQPpv5Kp0Gnn44TjCpGBuaLjf0vowZJLc-taD4ZfWci2bFL47LClZnn8-hH8HE2XKZoyQrAQf6uH4dF7NNI9Ee82bOTRK-IAw6yjxP_bPhUuyj6UF_RCFJ-p6ZaaVCWnfmX46LA7PFvAnvSBuMFlfyu3JKaGAITFYkTnGNCcZM1PfbrZxc2cAJ1efeehaJJy9g58MfJmZmAsQjb9O3EvvqsjLjVJyubm_UOA68C5Z6d5c1Jsf4MtVWgDcVsjtZS9gcIrmMvpm-jPGPgRulPAGHy4eUQ-D1MoPosZHZkA6jk51fEnRWvXc0DDrVYeBd7bwyXmTS-c9CX8T0Qsb81Mw-xjYG1_g6v2HKgcp2OwHcVIV4OR3HtW3R7m2pbiRZfe4WF-__WM5zHVZTY0bRPtHl8UMwFtCpBUJFdO-Wspihnv37g1kNZk6B3hfY4yg_WRbJKCMASy_-pxt2tILlrlgURY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت مردم بجنورد با امام امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/442157" target="_blank">📅 23:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e105871c7.mp4?token=Z6dYavOJkv5chBcDxZqZFXlm5pBVSP2JYwwkT17FczyirjaCqCzH39MzG1Ux0oTeLDgqgQO4LAdXMvPOxUmh1ifzR4VNMzjr4coPGHdG2HEzqaWg7XOKdm8sP4AedYqdN1VqDzYtHBflmFYtQYpOCkDODbqslPhqeyo01c9TM0KrOrGxVe1K28So_mR-MmGI6L_BTnQns3e_qHmSe_vJMdWgZqb95_kWWu28b98hVS-G4sJZqCOfHLGFqMw6erKqrS8izJ-bAo5zgNVJQ1gGTuI7zze1ZmwVHOYJwwMtmUrHTjzn0ew5KMuhuhM6A2Y03D4wScEfJf3ElbfHYhVOnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e105871c7.mp4?token=Z6dYavOJkv5chBcDxZqZFXlm5pBVSP2JYwwkT17FczyirjaCqCzH39MzG1Ux0oTeLDgqgQO4LAdXMvPOxUmh1ifzR4VNMzjr4coPGHdG2HEzqaWg7XOKdm8sP4AedYqdN1VqDzYtHBflmFYtQYpOCkDODbqslPhqeyo01c9TM0KrOrGxVe1K28So_mR-MmGI6L_BTnQns3e_qHmSe_vJMdWgZqb95_kWWu28b98hVS-G4sJZqCOfHLGFqMw6erKqrS8izJ-bAo5zgNVJQ1gGTuI7zze1ZmwVHOYJwwMtmUrHTjzn0ew5KMuhuhM6A2Y03D4wScEfJf3ElbfHYhVOnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهدی‌ها همچنان پای قرار شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/442156" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442155">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7mw3iuKbj3Zeo_q_ClcOeLOzy9106Cf3yCgU3WSm7rzpq_h5s5V_Y8qXXqt8nhUij2aa9r5lIyW17rOpu9SFLqrEMsw1F7I9OMC0JkcoxQ4dPO8Tl-e9iNCeZLEhO9QaGnSvkxTWnFgyHq-F6912CV90yXUkMZttSD9-eJDZPpQ_hYQG2Lbfr85CdTQqjN9komti2JCq6MBAsuNWnq-EndygOv2XOp1vthoojwQ7O5ip_Isan_yH2uAt6Fm1Y0xq5JlENutOmfitS9A_uHQNEJJkqj6weBtAJIwcJVs8HDCYyFaB-9fUoaNLlqgze3R4EQOEB0m8dUyZ6b4SmT3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
وزارت خارجه: پیامدهای آتش‌افروزی صهیونیست‌ها برعهده آمریکا و اسرائیل است
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/442155" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442154">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">محدودیت پروازی تکذیب شد
🔹
سخنگوی سازمان هواپیمایی کشور: هیچ نوتام جدیدی درباره محدودیت‌های پروازی در فضای هوایی کشور صادر نشده و امشب اصلا پروازی برنامه‌ریزی نشده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/442154" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442153">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bddbf1f2af.mp4?token=J4VDllwt7sZPehlx-TuUpWfvrF9DZxmIRWrKibr1O2TX9Q42UOB2CWbUZj2F20oU8yrYBk8vsEnwj-AIW8SBs74XYNp587lpihea5Nf5RJP5Su3vXFX2i13TdXDPdOLf7ZDoO4VEsC2qtYK4PpqVMORyuwM_ZzQeI-AAiC_L1Z9o9RDEFSmOFuProxBwudjgOYlHrAJnppc307q1P_1yYnpl8nnHYDv4BXOkTix2q8-gEC6u7JpEWPKgz4jAsQA8x358PW2H96eVRK0VAV6bwN3c1DK2rtKLrTwdacltv5B7H3ew7xHcGfHk2UPPiSVxfs8nSQ4bG20PZTOxWDQH_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bddbf1f2af.mp4?token=J4VDllwt7sZPehlx-TuUpWfvrF9DZxmIRWrKibr1O2TX9Q42UOB2CWbUZj2F20oU8yrYBk8vsEnwj-AIW8SBs74XYNp587lpihea5Nf5RJP5Su3vXFX2i13TdXDPdOLf7ZDoO4VEsC2qtYK4PpqVMORyuwM_ZzQeI-AAiC_L1Z9o9RDEFSmOFuProxBwudjgOYlHrAJnppc307q1P_1yYnpl8nnHYDv4BXOkTix2q8-gEC6u7JpEWPKgz4jAsQA8x358PW2H96eVRK0VAV6bwN3c1DK2rtKLrTwdacltv5B7H3ew7xHcGfHk2UPPiSVxfs8nSQ4bG20PZTOxWDQH_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجات‌یافته از نسل‌کشی، اولین گل استرالیا را در جام جهانی زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/442153" target="_blank">📅 22:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdqjh1xCeVU6I2x74-bijUwnmbFFIO58Pg40_GOOkF0kHGxwCGIlZB_SL3VLRv7Xx2eZC_xD-cao1CMHyOGFvy9CmeoIHcTx6rdqXUlMhTjGCiOpC59CaD1Wb0FQkc_BeF-xu5Gs07bGgU7efcta39CLT4_BFr5joZHsb-G-Xg_K03vrQplX4bkrQfdPzLPIT5uBt7AElzTUgM4kWKthcnzo0Fw1XwDNt3ELTBBYy0OQnriFOPhlRspEnA5c0XBozOKheMznCGe2ZAISkpQYeULxe1nV3H_58iJ4gOqfm3mybLvdaBT-Qb0cUugw9INMHPJ7UjSxkh8F25SzeGMtJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژرمن‌ها کوراسائو را تحقیر کردند
⚽️
آلمان ۷ - ۱ کوراسائو
#جام‌جهانی۲۰۲۶
@Farsna</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/442152" target="_blank">📅 22:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442150">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a155cf709.mp4?token=IWwjQeN-4y1nZbUwlT-38rxqGxwNWuGffxBkEJuXVGpO0aIZwGsXSuSbqhxSyn8SqeyNUTlu2mWLsgpA-xAR0fIBIxw5Gt-DxcuAUh333UtjbXW72hqatb0YDLsqcJJwNRl3zYvGcH0sEil98j0ScHbB8Ja04PlMGnKjAhwOFCXPdtZWrGrud0bjh6--NEUeMZg1dNU5a_RMz0KAL0Upa44DbJnjmN5kF66G27eIrmZtgFvx8CbbVf-sUrAwMtcj0AuAR7yswKnX5GAzgCv1oSFpj3-NHEQBqwkKnYaWXSOGi9OFfcZNv40FEYJS4IwrwYelC4XLv77C0r2nVMxulA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a155cf709.mp4?token=IWwjQeN-4y1nZbUwlT-38rxqGxwNWuGffxBkEJuXVGpO0aIZwGsXSuSbqhxSyn8SqeyNUTlu2mWLsgpA-xAR0fIBIxw5Gt-DxcuAUh333UtjbXW72hqatb0YDLsqcJJwNRl3zYvGcH0sEil98j0ScHbB8Ja04PlMGnKjAhwOFCXPdtZWrGrud0bjh6--NEUeMZg1dNU5a_RMz0KAL0Upa44DbJnjmN5kF66G27eIrmZtgFvx8CbbVf-sUrAwMtcj0AuAR7yswKnX5GAzgCv1oSFpj3-NHEQBqwkKnYaWXSOGi9OFfcZNv40FEYJS4IwrwYelC4XLv77C0r2nVMxulA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۰۶ حضور دشمن‌شکن آبیکی‌ها در سنگر خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/442150" target="_blank">📅 22:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442149">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxx6ozDV2An8YPSugLkJm8NldYSWVgqJVl_m9bfAIXfUJLYZg-yPY1LmjB_wNGxuUCp8Ov3IePziScQbVPbbOuzlHt8T2DITtOa1mLva-7ewZvAFujoerLspQWknvJtrtjZ4wp4l1_UPRVpv7GQQc2eH2TeixPaG1krbB6-Lw1oBijXPLJa4KsKIbgXeSan7tqjFuJEJEnhDVqi0ArpbAUas13yT8XmlyWCXkM7a9S1JsCeCc1MQ7W8T2OA3oESv0OAYr5u8upzcht7sRhM8_4SDu6q8Lrzx7-F3f0ctw49YYzP6WBBEcZ_7uYD6wN1OMDHLdtbKU9z97q0mS6uraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: پاسخ رزمندگان اسلام در پیش است
🔹
ذوالقدر: وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
🔹
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farsna/442149" target="_blank">📅 22:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442148">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e401ab5a88.mp4?token=e5U8cGXkJSTLRb_qL8Ky7_7sjN7CuOaCZpCaQlYaxm_TjFEqjhsfsU0ROxjGr8HXNQv4CV9JoYUj54a-QwOY1L4ojr7rTxvmMER09CBTGJ08J1IofScf4723JMbruwJ2KuXjIT1lRWqwLfTIgBGIzlC8mkD7UEwS5Vib5LdaO1qRhsGK_o-xLl4VJB4ssQBlMj4Fd9KblLHSrwHKvJSoaXOyJoL_H3B_uKgoTQzgCxQE6FpfI8sjvGTIbitplgAVd2PUzKMlS6V_ARzSoP67-MzOgYVh--rlcyIIEYOE1vW9C3s-iseE0LikobAL7C0r69eGSEmRDkFfMgW_XPIKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e401ab5a88.mp4?token=e5U8cGXkJSTLRb_qL8Ky7_7sjN7CuOaCZpCaQlYaxm_TjFEqjhsfsU0ROxjGr8HXNQv4CV9JoYUj54a-QwOY1L4ojr7rTxvmMER09CBTGJ08J1IofScf4723JMbruwJ2KuXjIT1lRWqwLfTIgBGIzlC8mkD7UEwS5Vib5LdaO1qRhsGK_o-xLl4VJB4ssQBlMj4Fd9KblLHSrwHKvJSoaXOyJoL_H3B_uKgoTQzgCxQE6FpfI8sjvGTIbitplgAVd2PUzKMlS6V_ARzSoP67-MzOgYVh--rlcyIIEYOE1vW9C3s-iseE0LikobAL7C0r69eGSEmRDkFfMgW_XPIKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: قسم به آن مشت گره کرده پرچم زمین نمی‌ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/442148" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442146">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f707aedfb7.mp4?token=QCG3DXlko4Vab0Vv1Nod5WuuacRDQPtooT-SAsAsq8krtP5kDzGlALzmCP3ncXPcQeIrh_7B2BplcxgDXu9sVwimyTic5wmYNARa4fmi_DKKB6l7ZgErtvlQ16VuCxJ1n358U-9sjn-D3Sm3AJElYyxN9xmBge-4uL7fcBPBGzqFYh1DToLvjBWk90BhL1ZLEC9kjil6T4dFE-LhZfzd3NmbQyzq6lTnZt-z3cbekrlcVto4XIRa04ELxVpUu-7lMeBZ8D4nJO4QweqLDKY7hsszm23cRNt3urX3n2DPN6U_RTZzaWnaZ6qaKceSTjkWOzVQ1bkzn3Jv97PEtOvSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f707aedfb7.mp4?token=QCG3DXlko4Vab0Vv1Nod5WuuacRDQPtooT-SAsAsq8krtP5kDzGlALzmCP3ncXPcQeIrh_7B2BplcxgDXu9sVwimyTic5wmYNARa4fmi_DKKB6l7ZgErtvlQ16VuCxJ1n358U-9sjn-D3Sm3AJElYyxN9xmBge-4uL7fcBPBGzqFYh1DToLvjBWk90BhL1ZLEC9kjil6T4dFE-LhZfzd3NmbQyzq6lTnZt-z3cbekrlcVto4XIRa04ELxVpUu-7lMeBZ8D4nJO4QweqLDKY7hsszm23cRNt3urX3n2DPN6U_RTZzaWnaZ6qaKceSTjkWOzVQ1bkzn3Jv97PEtOvSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سانحهٔ هوایی مرگبار و سقوط ۲ بالگرد در برزیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/442146" target="_blank">📅 22:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b40936e07.mp4?token=Zv_-DCspf6fCzTJd8B78w-3AgiKsJzxDnfJWcbzRBTbUAT3XOS0T5tPTRcwmzZiQicz6hlzv88BXpTkXiTOTgQFeMYGMxxh6LQ6dw4Y9xBtSqZU-XDnyseQZONUq2z-Y2l9U4rLRZ7bSCC8uXxgXYjxgs8bIFmZEc8WAE8jPw_rFlAVEe9-5SpVEMugmz4IHJ1UeaEPK2TBkCgleap8viIBEcqyxPoYGnNHjbX9lZ8vkS85hZZh-zVZEa032CPkPUNadaqZZvnEhJAcX0y4EM--akFZLOhCsfYr3tUDklNdNIpWhGexRHgchen6F5-dpzX55Bvtahna59vaT7v1_sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b40936e07.mp4?token=Zv_-DCspf6fCzTJd8B78w-3AgiKsJzxDnfJWcbzRBTbUAT3XOS0T5tPTRcwmzZiQicz6hlzv88BXpTkXiTOTgQFeMYGMxxh6LQ6dw4Y9xBtSqZU-XDnyseQZONUq2z-Y2l9U4rLRZ7bSCC8uXxgXYjxgs8bIFmZEc8WAE8jPw_rFlAVEe9-5SpVEMugmz4IHJ1UeaEPK2TBkCgleap8viIBEcqyxPoYGnNHjbX9lZ8vkS85hZZh-zVZEa032CPkPUNadaqZZvnEhJAcX0y4EM--akFZLOhCsfYr3tUDklNdNIpWhGexRHgchen6F5-dpzX55Bvtahna59vaT7v1_sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیا خانم‌ها برای اهدای خون محدودیت دارند؟
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/442145" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442144">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">با فریاد ایران
🎥
بدرقه  تیم ملی فوتبال ایران به لس‌آنجلس توسط مکزیکی‌ها
@Sportfars</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/442144" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442143">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0afa7a9107.mp4?token=Y0i8Ya451X_uhUVhpOW0B6QfOlwiXRuE7IPFmJMgrdNlOufr_Q7UfmOMIYF7YwZIiQJVZAOQDKT3WB7z2aSzrHfAiZkEPnSqTDBl7PeVOPrHDhFMnr1TKIlepY48EzVCTh_odA2eYn6loIiJkyDpL7O6gaBAy2pWs0lQOB42DOalHtz5Z5fe16GlTBfvEbtUrrqgw2ZcI7dE2r8x-z1EYaAm3h-FmbrhI1Fzr_F8LHfBHzI3O0jwSkBomO_cFNPuPz0r6uZ8Qq_jRV5iUQSexNefgPU7-xifgwAH9piD6gJ1Ktsg8i6Q5KFnFcVWr0DMQ9FCVhcCjSSLHY3Je26UQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0afa7a9107.mp4?token=Y0i8Ya451X_uhUVhpOW0B6QfOlwiXRuE7IPFmJMgrdNlOufr_Q7UfmOMIYF7YwZIiQJVZAOQDKT3WB7z2aSzrHfAiZkEPnSqTDBl7PeVOPrHDhFMnr1TKIlepY48EzVCTh_odA2eYn6loIiJkyDpL7O6gaBAy2pWs0lQOB42DOalHtz5Z5fe16GlTBfvEbtUrrqgw2ZcI7dE2r8x-z1EYaAm3h-FmbrhI1Fzr_F8LHfBHzI3O0jwSkBomO_cFNPuPz0r6uZ8Qq_jRV5iUQSexNefgPU7-xifgwAH9piD6gJ1Ktsg8i6Q5KFnFcVWr0DMQ9FCVhcCjSSLHY3Je26UQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادای دین گنابادی‌ها به مجاهدان انقلاب در شب صدوششم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/442143" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442142">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e45b95dfe.mp4?token=LS7xBFDDLdt5uZ5EfJVP9lT2lWnhfWyWLhjG_oQVW43P5ZrsJEHiV0JC6Qb00kWWHh-CA8c4B-1VQl4bCjHZ3tVq_KyBVjVxij1-oK9CEr5t4suDgJt3sP2yvnjiiyaiAkmBcqFgTgqij1zw3sPI-O8FaurWRPor1w0wM4yC2BrWv4jNMkn2h3sKQRkqP0sZdCWNdeh_eE7HAoXhPUBVvz32WtN-rcgQBomLT12Du2ZSoDY9AN-vRondBte4cEHUKqDaGTi11ex__3hBsw3fbUjduVr1efWUTuuQ-LJKcULpE5G0SSL0Lr5EIV-ePgKItgGSSvnYGkjYp7x2qBb_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e45b95dfe.mp4?token=LS7xBFDDLdt5uZ5EfJVP9lT2lWnhfWyWLhjG_oQVW43P5ZrsJEHiV0JC6Qb00kWWHh-CA8c4B-1VQl4bCjHZ3tVq_KyBVjVxij1-oK9CEr5t4suDgJt3sP2yvnjiiyaiAkmBcqFgTgqij1zw3sPI-O8FaurWRPor1w0wM4yC2BrWv4jNMkn2h3sKQRkqP0sZdCWNdeh_eE7HAoXhPUBVvz32WtN-rcgQBomLT12Du2ZSoDY9AN-vRondBte4cEHUKqDaGTi11ex__3hBsw3fbUjduVr1efWUTuuQ-LJKcULpE5G0SSL0Lr5EIV-ePgKItgGSSvnYGkjYp7x2qBb_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط مرگبار هواپیما در آمریکا
🔹
در پی سقوط هواپیما در ایالت میزوری، ۱۲ نفر جان خود را از دست دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/442142" target="_blank">📅 22:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442141">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e51f6432ac.mp4?token=HRgLJBxWz2nPNJCokv7GuCdVucNwcheOkAiZ0TuCcOvQelDMf-Chf9aWb841zM0aSO458NLumsZTJ49nOBWmuo90fz8ZzpgneT3z1oWIm5HUPfhGRnajxuQ0K-rZX_aaaGIArKAn6j3yK_gb16zivt8vVwg1ZppA_q1Znn_gPd-3ET0J5TXY8MOCT-UVVeTAwVn0xG0rHrAQTYPF1NMsR6corYy6G5IKcwNQvm7AOhyE_xh-EKcjNT3HcWytsQQ1RXqET1sfnRFUtkPJKSQVe4F7DkQ2Jv-WtfmKH9KMofbRevYty8w_HtpgBlYLzeXTUPLxoaJpWB4MeKiN40LCAyj_Cq8Wtn2rO9M9JH4zqwwQKU1qJKDbAypmLUO_IpwuEML54zFqNeWtr8JTP4YU9UJSTanVHLp6idocTC3hUjy50nTWr-ryczjYGREo7Uv2OkZtz6-ISi8xP4ZsYg-MYXNUPb2vSZQ-JtySpdSUzwITIp-jEBAof84_jM5CubiJWByGblas1TiJUNZj5mt2Mi1wGiuGWALhQB4SXWpFDn9TZJZCjzIpgjSrua-1WHgjMFJglhjuWciYy2XRDAfk43KFtLIKFa27e8kwwxITTJD3uc_TurU6h-t_q3Mv4vUarTldo7Kg-d3IW9Tmu1VLhP0sMMQz2kDmzRO2QEugLF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e51f6432ac.mp4?token=HRgLJBxWz2nPNJCokv7GuCdVucNwcheOkAiZ0TuCcOvQelDMf-Chf9aWb841zM0aSO458NLumsZTJ49nOBWmuo90fz8ZzpgneT3z1oWIm5HUPfhGRnajxuQ0K-rZX_aaaGIArKAn6j3yK_gb16zivt8vVwg1ZppA_q1Znn_gPd-3ET0J5TXY8MOCT-UVVeTAwVn0xG0rHrAQTYPF1NMsR6corYy6G5IKcwNQvm7AOhyE_xh-EKcjNT3HcWytsQQ1RXqET1sfnRFUtkPJKSQVe4F7DkQ2Jv-WtfmKH9KMofbRevYty8w_HtpgBlYLzeXTUPLxoaJpWB4MeKiN40LCAyj_Cq8Wtn2rO9M9JH4zqwwQKU1qJKDbAypmLUO_IpwuEML54zFqNeWtr8JTP4YU9UJSTanVHLp6idocTC3hUjy50nTWr-ryczjYGREo7Uv2OkZtz6-ISi8xP4ZsYg-MYXNUPb2vSZQ-JtySpdSUzwITIp-jEBAof84_jM5CubiJWByGblas1TiJUNZj5mt2Mi1wGiuGWALhQB4SXWpFDn9TZJZCjzIpgjSrua-1WHgjMFJglhjuWciYy2XRDAfk43KFtLIKFa27e8kwwxITTJD3uc_TurU6h-t_q3Mv4vUarTldo7Kg-d3IW9Tmu1VLhP0sMMQz2kDmzRO2QEugLF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بسطام: ما ملت حسینیم، ذلت نمی‌پذیریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/442141" target="_blank">📅 22:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442140">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
گروه هکری حنظله: طی چند ساعت آینده، غرش آتش‌های سریع و سهمگین به مکان‌های تازه‌شناسایی‌شده توسط حنظله در آسمان تاریک سرزمین‌های اشغالی خواهد رسید.
🔹
فوراً به پناهگاه‌ها بروید. چه‌بسا هنگام فرار نیز حوادث دیگری رخ دهد.
@Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/442140" target="_blank">📅 22:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442139">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ce3b0a1c.mp4?token=fVHm5wOoSiTk3TjRB7hUp2swlj4dyzx-mJ24qM48ZBgsM24gf7lRusX7jMt7IdUJW1X3W1N4-6qKNTAHab9Out5TlnoS3gLF4DJ3VQJA8J16h1rxtMoU9pUMjRzy8Pn3U8WvSIYviV-Q4F2IZEQeGOBf324vYoVi2Qqq532YzfEpdHJnnkr3hoqTgmXqV1WQVLcFhzHtEl1IzNkSvZsmadBariUYubOe2WqjuokxCvBysuA9MeIjXZLe3XXH3aQ7_UmgIKUXe0jscMTWWkWtpFTWtSv4pmiTHAD17Kwdoink_z7TTriyz8c5LfIP7Ew4MeL7WKlPHlZeGQAyk7GWRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ce3b0a1c.mp4?token=fVHm5wOoSiTk3TjRB7hUp2swlj4dyzx-mJ24qM48ZBgsM24gf7lRusX7jMt7IdUJW1X3W1N4-6qKNTAHab9Out5TlnoS3gLF4DJ3VQJA8J16h1rxtMoU9pUMjRzy8Pn3U8WvSIYviV-Q4F2IZEQeGOBf324vYoVi2Qqq532YzfEpdHJnnkr3hoqTgmXqV1WQVLcFhzHtEl1IzNkSvZsmadBariUYubOe2WqjuokxCvBysuA9MeIjXZLe3XXH3aQ7_UmgIKUXe0jscMTWWkWtpFTWtSv4pmiTHAD17Kwdoink_z7TTriyz8c5LfIP7Ew4MeL7WKlPHlZeGQAyk7GWRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرصتی برای تثبیت یک معادله در برابر آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/442139" target="_blank">📅 21:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442134">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJim-X4hSbOzb0a68IdHKYPKTyxn8QmeFWJ3g4wyRJaunBGY6pP8pUkeuYl_gFIsfuLMdJAqsxKPZdVJkp3P40-7w54MBcVot_XT-qjvMBZINQIrujiGfMGBe7khbWy8fOe20VBrBGEtMpPvAc8qyC6swvUSRxAi6-_5vqk4rCQcKGPN8CdztXwU6kUdsgKJ4kxV7ME7_WIhZouy9JUxvc6ZfFO6ZD0xmnjpbmzp12sQZ8iX3mzyCzCbrEw86zCETlNAPGAUHilWJ0fV3ZQPTcO7pZe3nrY-zlLGIepwLr9Sb0mYrbGQZJYxUKyWtFRyGpJON-mFnlcU9h-PVeLSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0HRQskC2g1LxgB4FnO4g5KyXSfLGzGJEFzgY5Fp2QhOOEdySOB_G9A8vxsM2gs-YxtMyIC9jM9EWrO86nXRWJj-mbWgwll1AbU-M6ElDwV4ktz8VIITwBQQR13tHtcFBjyIiKrKpzkKoF6D6NICBAbvbA6c9NWACNqn6nu2NSb4b9EM0aMHw40JMb_rL1CzjYii5ORjmMOCB_sxYEKpPnOXI0ZfODd0Sue_Wdb83YEeizT__rXBhADnjnGXUqZF-u4KbQmVoie1k5LHEhGRt2IHo97yW0CWVTifxm1fD9OCftjtEc8GQ_Bi5iGSJHOGLSU4_qNJem1qshefY0zcLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3xKg1UPGudnsdvlp4x26_XdjMVTIO83Fj-FPosPTjLyqBH5pA33VlJAJ1OhS7Kf-VLnJtpevVbsLKlzy3o00QQDKK8y1m6bIGGpirz0eenodO9SjZ2Xu072I03hPt9PSwXwKRWuGcEGsSAGClwfYPCD8K139E5JfWtecBtlTf-RP_QQh9XTercLEb9ec2vTa6yLIA4jOo3HHH_KWIzDV9Q9qaeK0eTeJ4TtrcSJURKyAUC_CVbOkZVAsghTkFCwvYrQ3DYcTPMKtA0a9DlNWlIJl_g29VPTZdfNlbun3hi8k6tic9jzLUN8y90F46r41zAvON88WqjiXyIU0gZJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HT97QrsB9dNF85l0gOCeFPVn22-YyMIBhO7dRO6Lkqyjbmjmdr_kooRetQOaDTduXmsDBTPYsSzVoG-6ZBTvcUJHuUJVGbqi6O4SNpildIzf1Tx4La9NH85pMwDwWbXiYWDqAWre2nmSodOC_CrQDFYYu-_zwD0p3nB_nJW9rHz8hb5at9tjM0hOiPB8scBZW0n1FCMEf1ndM9BhuJ1ogh_jYCxwAQUFoySLTq36vAxf3KQKJRcFhuoHfMTR0H5WpdGf2tMaF95j8DGrkDafW4ze48ahzx1o4Gr6ByGWy2DrW14f1DC-RHwUxeUSOR8NIhUoZCNaO50MUMPfTn_4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYVFHJX9WgztKVDjGdlX-jVQnOV8Tx6QWVDm4EDDqT2vUv21iwVl027JMzR9HVLUY2jTRixwTc47Jz5Uok5432d58fx8_uxQl1GBnKHZE79AWzkdHbL0EH7QbFQJUSHcQFejJyz1vHYISYj-JdnP6jHSrimGBwHxw0YKxtsbXl-IjNZ2QLfeEDjfeQhaFMykKqFQqK_CkKN569b4a4-BYLt7-uuRzDIbcahnjUNrSkC65B9SYCq6bJ31iHmh-9bHRXI3HFhELguGUchVNGBitk7dI_pTX26T63RAiz5t4PAWyJ7uWQ9_iUFMZ-nZZZ-M7ffutw1OiBym-iSWku98nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رونمایی از کتاب‌‌های زندگی فرماندهان شهید هوافضا
🔹
به‌مناسبت فرارسیدن سالگرد جنگ ۱۲ روزه، از مجموعه کتاب‌های «آسمان‌دارها» با موضوع زندگی سردار شهید امیرعلی حاجی‌زاده، محمود باقری، داوود شیخیان و محمدباقر طاهرپور رونمایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/442134" target="_blank">📅 21:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442133">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWtPVzusp42VqYl-RvgnK7DLRZQ01EFM08T4jlrU3uhOZdmw2I27CTn9NrFxtf1IG55aBq91V-Cies8lQvU5jU49DwtCpeh_u6R3eBIriP1CO6smcT2lJKrZsTj_Le7uuzN_7f4bmTIWLeKFTCRrSYe-bnPhXMV51qEB1jEtNTvV5XawqMNNHISP8mD9A1uDMZOfRh0WEwCdEe0C3Q5vWWNzen7NIUw8E947p6czcDoTTbsombKejpXmaOO4O-6KUdDAYAJuBLmDruEj9TncDdt13o7IZFlBmCRiBqfGjGL2L1hM3GZTXQkKmFqG822cX9GhV6zBacPfb6COzH5hJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: پیروزی مقاومت عظیم حزب‌الله در راه است
🔹
مردم دنیا، استقلال لبنان را با عظمت فداکاری حزب الله می‌شناسند نه با وابستگی بعضی حکمرانان.
🔹
همهٔ دنیا با چشمان بازتر نگاه کنند؛ پیروزی مقاومت عظیم حزب الله قهرمان بر پست‌فطرتان صهیونیست در راه است. ان‌شاءالله
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/442133" target="_blank">📅 21:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442132">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr3wfyUviT0QgjXuSP47fZnxOa6Q3zt4TVCJtOBc9qWwaQo9JXFuui6lRz9Kh-HFsEb5y01v4IHnLhSjOVy99zOyT1EJ2AJY-4HGjUnGvancMuMF9_l1qNnb684f2lLwIA-qtXieOoUF0rNA9OIBys7uwhB1zICQrqAu9darDYCMqHQX3xNYRxuo3chP1orpwi_D1k0YXYmST-yVvkp_x5f9ZkTuMJdDfUPjec6iFhP8HoSLNSEPD0hJsv7EVrJpTVwcBciZTLQt8OBPVninqWbmZNwTuBvf1iFRR0E23oso4aQ6tCZFSahD46HGgH-uGQoRUCMd8MkBEKNR0ETa6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: نتانیاهو بدون چراغ سبز آمریکا، دست به حماقت نمی‌زند
🔹
وزارت امور خارجه یمن امروز شنبه در واکنش به جنایت امروز رژیم صهیونیستی در ضاحیه جنوب بیروت، تأکید کرد که تجاوز امروز، گواه جدیدی بر این است که رژیم غاصب، خطر واقعی برای امنیت و ثبات در منطقه و جهان به شمار می‌رود.
🔹
صنعا در ادامه گفت: در حالی که دشمن از امضای تفاهم‌نامه‌ای شامل توقف حملات در همه جبهه‌ها از جمله لبنان سخن می‌گوید، رژیم صهیونیستی بیروت، را هدف قرار داد تا معادله تجاوز افسارگسیخته را که پس از امضای توافق آتش‌بس در غزه در پیش گرفته بود، تحمیل کند.
🔹
صنعا با بیان اینکه نتانیاهو نمی‌تواند بدون چراغ سبز آمریکا دست به هیچ حماقتی بزند، خاطرنشان کرد: تنش‌زایی نظامی صهیونیست‌ها در دوره اخیر تنها به لبنان محدود نمی‌شود، بلکه غزه، کرانه باختری و سوریه را نیز در بر می‌گیرد.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/442132" target="_blank">📅 21:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442131">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqEfkZQnpXkMDFKeaGQijW4IXzFH9Aw4fhcLbxi5k6cAqs5vIPwp8A6B16VY_Ldep-4hFLPswkZhm-P0ZuuYKDhk2Rw5vXJ6EUfDnak0zZVUHZI1de-vj_tbbq-ppok8Pbsu_5-vASoIA3GIcY5GqIbMokwNKJPgBQZLuNvZKtiXmOUnMx3Pq7cc_ltkU1MzQ-luoiUk2WQ0k_pN1DDnDKoyN-UtnTEqOT7sdojkumrR8b77VJh_Kl2-idhgX2XLg1cT5e35_RwnSoy77REIhcs7ZsIirbJr2oy288r3cygxkbbH41aBmK6z7rtCU96YqcEiWs-YaLFpD--Vcapm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۵۸ کیلوگرم موادمخدر در سیستان‌وبلوچستان
🔹
فرمانده انتظامی سیستان‌وبلوچستان: ۱۲۸ کیلوگرم تریاک و ۱۳۰ کیلوگرم کشف و ۱۲ نفر از سوداگران دستگیر شدند.
🔹
۲ اسلحه کلاشینکف به همراه ۹ خشاب، ۲۹۶ فشنگ جنگی، یک دستگاه استارلینگ و ۹ خودرو نیز از متهمان توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/442131" target="_blank">📅 21:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442130">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4302e6bf30.mp4?token=ktnhByTaGY34T5t6q513Y8jTr6MdPXI2dvGkiY7QbvDFR2RWctDX9zCGakLzwFhX1MAWmtzvx1txSelxW5i7Uo5TOj3jyYFUgtTgKnYIuOYUo-h2wq0ldL-E15wVFNVgkIwwbe6Jz4YIcQHujLTeMcpkARGOpQOZbrYe9l7ahq4G7XJPukesDwEvaXgAbEwBXy7VoVT0MNJPjkx8wvgoJDjST95E6xLnqbI2LpfTl-c6klxLJOaefeWVblJpXc8dWrhaOA-i0qP-PBSbxQHPT6k2qUXixUUDpfvvv0tUgSnXUHkXfLsmf2p0yU91p5cUmN5edXtOMjRnGjOR9lILBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4302e6bf30.mp4?token=ktnhByTaGY34T5t6q513Y8jTr6MdPXI2dvGkiY7QbvDFR2RWctDX9zCGakLzwFhX1MAWmtzvx1txSelxW5i7Uo5TOj3jyYFUgtTgKnYIuOYUo-h2wq0ldL-E15wVFNVgkIwwbe6Jz4YIcQHujLTeMcpkARGOpQOZbrYe9l7ahq4G7XJPukesDwEvaXgAbEwBXy7VoVT0MNJPjkx8wvgoJDjST95E6xLnqbI2LpfTl-c6klxLJOaefeWVblJpXc8dWrhaOA-i0qP-PBSbxQHPT6k2qUXixUUDpfvvv0tUgSnXUHkXfLsmf2p0yU91p5cUmN5edXtOMjRnGjOR9lILBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازی‌ای که برای ترور کردن ساخته شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/442130" target="_blank">📅 21:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442127">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzArSgkzJ946fsC9_EDloYmlBSiTwNmv6rxBZO6im9ejEqU7l7rbVumuUZq7aB0SnxsncPwt8P7pW_RtO1JVPE5NfkSc0PWYE7N2Yg8Tj1y1W41EuT-WfzNEBNZK1fgYhRjKhABmI35pmmPeGMv21PLD6uGV6a5tklPkxVgD7KnYSw9msr7_axYutRm6enjYAunmDS5QWzbMwsvtEW67x_tmZCPvckpMJbtFaz0S5LSGw8T8t-e1k4_fwjKCEnZabHTH2f3fTrYEfmA9GLuB0Yn8OtWeNLsi47piMI8jz9P70-AdkzewUWZ5AW4eNl2Z4Db9dJKRWeLEWE1qYPYN5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: پاسخ رزمندگان اسلام در پیش است
🔹
ذوالقدر: وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
🔹
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/442127" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442126">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS6wced02vbh2m77pGrIyCvGIwru9FLnLNhudFDNyuKZ-BYA0ObQbB9_juiwHNAM1-9pS4Xah2NLPGH48g5rnWCkomuVEYdGFWyvei1BniIkng3dCIoz6JPdGqaDj7ZeF35fRGCJhRcan4uN0u2asO3UgxDQExXXwzdSlwfWG_giTahyHP91X9UOwnSr0g_vdcF6v1B1O_r_Pb_ZhfFdvWl9TteEiyEl75FoPTV2phwZYRAZ3xVuG8hF8auvxFOZX4kwgjHlHkyheeW8f_TSiHhk_FCU7yYH6CUv-pOYx7yXthnQPQrkOQ2TgGf0LskOiUVqPHfrRiQgXbObbFn6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مدیر روابط عمومی شرکت خدمات انفورماتیک: سیستم کارت‌خوان بانک ملی تا ساعات آینده فعال می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442126" target="_blank">📅 21:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442125">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8574d680a3.mp4?token=KBJvVUb24o5pFCqjyiPMw2Ax1vVQ4-Z5y08dA94uzzkvVHGfLIEZLXR4yby94XKLDaJ-Z1So0BGZdZyzPDXQHznT-4K-ltpn0zygi3mC335Qf1rKhmIXBAMOE3clHFxzr8qunMAq6Fgxm3hM4TpgLoNPuo9fvJkcSuWQRanGF1GwK60I6vBin3rMQNW3A-RnOm_jgDxYtrxI-gpIO6b8Ya6OxapOaajt5ss1mvaCfm8gTrgdT5Z0QWntIp3jSZbeL2UA4yBNMJ42UHKCU4_bS52W3dAYnij-P31OLUXybitvFr9zY37qETMceziSukLpM1KmtbMUtuS_jRP0b7cQPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8574d680a3.mp4?token=KBJvVUb24o5pFCqjyiPMw2Ax1vVQ4-Z5y08dA94uzzkvVHGfLIEZLXR4yby94XKLDaJ-Z1So0BGZdZyzPDXQHznT-4K-ltpn0zygi3mC335Qf1rKhmIXBAMOE3clHFxzr8qunMAq6Fgxm3hM4TpgLoNPuo9fvJkcSuWQRanGF1GwK60I6vBin3rMQNW3A-RnOm_jgDxYtrxI-gpIO6b8Ya6OxapOaajt5ss1mvaCfm8gTrgdT5Z0QWntIp3jSZbeL2UA4yBNMJ42UHKCU4_bS52W3dAYnij-P31OLUXybitvFr9zY37qETMceziSukLpM1KmtbMUtuS_jRP0b7cQPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۳ شکار امروز پهپادهای حزب‌الله
🔹
حزب‌الله: یک نیروی ارتش رژیم صهیونی، یک تانک مرکاوا و یک خودروی زرهی امروز در جنوب لبنان هدف پهپادهای انتحاری قرار گرفتند.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/442125" target="_blank">📅 20:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442124">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a7d56e42c.mp4?token=lBPYTHmyffO9C3rNf8am9tVdrwI3XwQAXcRDpNi1Xz_z_tmqcFO_lwLqIja6tUpOjcpqnESwcpiZNC8-rOsZqfWSWKxx2o4Q3fmvVef5GLlCX9clGoRgrqYWCjlIni3gpIf-5xDnVRYZwYzvcjHz-L4HLktTvf32OaH2OTDgzIGIVsbVL6QK9Xik4UKzYFxQZ15i6x7NCZTKFJjaleXSI8XrZla9toPQY7S680n0q5wh-3nrN37oOyamoNpT60Y8-9QxsnNnarJBa0OEfIeZSWaZU9lpEODOlrTh8DGfvANu8Rv_PNMFh8tsgohK9mjHmp-eoL-7eWtxzigxnshyKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a7d56e42c.mp4?token=lBPYTHmyffO9C3rNf8am9tVdrwI3XwQAXcRDpNi1Xz_z_tmqcFO_lwLqIja6tUpOjcpqnESwcpiZNC8-rOsZqfWSWKxx2o4Q3fmvVef5GLlCX9clGoRgrqYWCjlIni3gpIf-5xDnVRYZwYzvcjHz-L4HLktTvf32OaH2OTDgzIGIVsbVL6QK9Xik4UKzYFxQZ15i6x7NCZTKFJjaleXSI8XrZla9toPQY7S680n0q5wh-3nrN37oOyamoNpT60Y8-9QxsnNnarJBa0OEfIeZSWaZU9lpEODOlrTh8DGfvANu8Rv_PNMFh8tsgohK9mjHmp-eoL-7eWtxzigxnshyKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
امروز به‌صورت همزمان گروه‌های سرود جان‌فدای ایران، به‌طور نمادین سپر انسانی در اطراف زیرساخت‌ها تشکیل دادند.  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/442124" target="_blank">📅 20:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442123">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9637adae92.mp4?token=Tb2uhkKaiCNgPPdkoCC9cghAqlQqfOZeUt8802N7IJhE-rQGgeB8De7V33-sGzRpoFkg-_tliAObT7FWIh-wc3_eggSKspL6uZMwOnLx6wC7L3bS5j99DREQkIh3sGVQgfpLgGrkx66V3UkYRRXhWCI1cUjF7dHYlSES6lb3DcqQZmPKUoV6SVNXsvzJ2EHSaCdIIHnoGtCZLnTZzAlUvQyeojsIwwuCCtG7vQvpbRUjxWL2McbqwzB3M6HXI15hBdCrIuFoS0OzJZ_ceHQhr53VTGsO2wxIwOp_jUyGQDR-70UTD-hHs8Ad-AhuB2GgyBWIXunighlBnJJlN2Ziiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9637adae92.mp4?token=Tb2uhkKaiCNgPPdkoCC9cghAqlQqfOZeUt8802N7IJhE-rQGgeB8De7V33-sGzRpoFkg-_tliAObT7FWIh-wc3_eggSKspL6uZMwOnLx6wC7L3bS5j99DREQkIh3sGVQgfpLgGrkx66V3UkYRRXhWCI1cUjF7dHYlSES6lb3DcqQZmPKUoV6SVNXsvzJ2EHSaCdIIHnoGtCZLnTZzAlUvQyeojsIwwuCCtG7vQvpbRUjxWL2McbqwzB3M6HXI15hBdCrIuFoS0OzJZ_ceHQhr53VTGsO2wxIwOp_jUyGQDR-70UTD-hHs8Ad-AhuB2GgyBWIXunighlBnJJlN2Ziiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست.  @Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/442123" target="_blank">📅 20:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442122">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8b423b02.mp4?token=p-qFu6T0YOO7V7WKGcKPOKABY7mf0cJGa6AoLj1W8vi-5-syRXtF9jp860SG_QEbQCCPwxT2oNEyc0B3RdtjrpSvhqRcrUb6dLMmOXdRDFvkMdKNdrsO-20QVb1rHPdUysrw6tGtUeAHwbZQ6F9eBJqAQkruPLTEZjNEBhqHpkDy5cqxQVK8jdHzOfhgBru1iS99wKbaeoP4ThSaBaW4HDs8ZDnuHbGhK-dY01aPrPtRK3Zu5YLDk5usOaccpG7LHZCCG_q8Ic6sJrppXaSsmn7a9iX9kyhiguf_vogDWNFM6EpbrCZ3Ptf9Teiec7i8zvKtrnykwGCQmDCWIY3SKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8b423b02.mp4?token=p-qFu6T0YOO7V7WKGcKPOKABY7mf0cJGa6AoLj1W8vi-5-syRXtF9jp860SG_QEbQCCPwxT2oNEyc0B3RdtjrpSvhqRcrUb6dLMmOXdRDFvkMdKNdrsO-20QVb1rHPdUysrw6tGtUeAHwbZQ6F9eBJqAQkruPLTEZjNEBhqHpkDy5cqxQVK8jdHzOfhgBru1iS99wKbaeoP4ThSaBaW4HDs8ZDnuHbGhK-dY01aPrPtRK3Zu5YLDk5usOaccpG7LHZCCG_q8Ic6sJrppXaSsmn7a9iX9kyhiguf_vogDWNFM6EpbrCZ3Ptf9Teiec7i8zvKtrnykwGCQmDCWIY3SKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/442122" target="_blank">📅 20:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3o6BuduX72mYvYnYEnO44a5dU4axRfJ2m_en5jt8Gzhn0c_oC2vrdloQ18rToY7j5nwFmBBTfCoeJNspevRajQtGWOpn7s-lBkeZCG1F9CYPYqKnbv1-V-JSvXdWA69gTfHlNZ4D7is9dyZWTL29crjRIFH6SAVg3Wh0eBlBbpO-cYkEjoedaiJr_elz5iqAGdWjEaVtCCudZ5M4DQnZphFJvr6Xxxz9Ecah5ihlh8rdzb097-PgKBVZpgJ8YFb9e9GZD9jFEnbrape747-1_zhttd1o5keXDNJm8QHVDWvyv97QYQUCwwexzVADg80YqI5677UFCjM1-FJAY9UpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ9aVNk_-5wefvNglk3tZZPCDtqewLS_8-CI3JFDAhwaMQFtfqo_eDXS1H4CbSTHGoPsk64MUV-XHS9sc0nTm2xbwy2BQ8C0INeeJNhTV-73jricVrdtatIrECZ8meXEfpoVQT1q120jyWAhtJhq8jHSvb6lly5Z98fk38m7ILU-d5dlv1jf_oWmM9_BS6EsGP8168jSgBv_ihLBlUFjc3tefbiP6KH7JDXHcoiA_1_-nxQC1rUQdNlSMM504lMY84jqeUpvFiTXxMEwgNcCtYIShzgy6QMvqqsL71qdVVJYyCLthrR7XvfAew1roTJ1KNIgjuflCFhrtfx7Kgs6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofbSOlNqDrb0I5nUmy1X8sR5pSVXzZrMPMwT-4r_WFSuYIjpPml7mjFTFizIVCKEisLYpArVRFBbMDLTfkqEr39Q7DqgdHXRsQTEDsMUhuWks9PgpvZbUuI7OxYbkm71g-7BPeLnq99MO-HuqShJtpXTetmS0v4QonGzL-Gx4Nxz0tRYVJnu7qPxsnSsE3FDUMzw1Hv5iDfE6a9SAUQHNcE_2_-jLlb_1RG2Ip0bt33ByPMCfcP7fW-a0BHgjpItK9ooeIp3DjSerHnrGr2zSUbxZomhAL9NHgS2ctpxJRgQ-QFDFUkSYgTN2jayZnSdlkXg-dLlmZNCAZjWAymVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDn7PusdF1D6pVGCQgKGfpqPMOaeI9X4LoE0HKBM4BJQ5XnXCMlO2RWlO8O7cQJIlRS3LnTS6kTuNymo6PdSNDbYTyNZcCwlRpdmnUni7uyeGGJGyYZk-YwYd6eC3l0sU_T5ZU6ugTBK4zF3h4yq8MeWQdWdoyJemwywMwp5YdfDBgKvqezXEvB0S0CXRMc8qRpRjZjAWFr6oUwHG4QzPQRduccpKJLpLVwJ_j8sl38-2ZUm3e83T8trzzGpwcorNqftdoqUlAInLixzkjqq99fgi0e2-FkSruNJQ31nTh0pRJ4jYt5Sw_oQV37lxaLZKbpwKMrFPNGgoiQJwXbGeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرمانده قرارگاه خاتم‌الانبیاء: فرزندان ملت دست به ماشه آماده شلیک به قلب دشمن هستند
ملت قهرمان ایران
🔹
مقاومت و بعثت دوباره شما، فصل نوینی را در تحولات بین‌الملل رقم زد و جمهوری اسلامی ایران را در قامت یک «قدرت جهانی اثرگذار» تثبیت کرد. فرزندان شما در نیروهای مسلح، به‌ویژه فرماندهان شهید که تربیت‌یافتگان اصیل مکتب امام خمینی (ره) و امام خامنه‌ای شهید بودند، از روز اول نهضت، بغض و عدوات با استکبار و صهیونیسم را جزئی جدانشدنی از ماهیت انقلاب اسلامی می‌دانستند و می‌دانند.
🔹
اتفاقات یک سال اخیر، از جنگ ۱۲ روزه تا «جنگ رمضان»، علیرغم خسارت‌های سنگین و داغِ جانسوزِ شهادت امام شهید، فرماندهان و مردم بی‌گناه، یک فرصت بزرگ برای «تسویه حساب تاريخی» با جنایتکاران فراهم کرد؛ نیرو‌های مسلح به پشتوانه‌ی مردم و با عنایت الهی بر سر آن‌ها آوردند آنچه لایقشان بود.
🔹
توان رزمی، دفاعی و قدرت موشکی، دریایی، پهپادی و پدافند هوایی ما پرقدرت‌تر از گذشته و تحت اوامر فرماندهی معظم کل قوا حضرت آیت‌الله ‌سید مجتبی حسینی خامنه‌ای مدظله‌العالی، ارتقا یافته و فرزندان ملت در نیروهای مسلح «دست به ماشه»، آماده شلیک به قلب دشمن هستند.
🔹
آرمان مقدس فتح قدس و انتقام خون امام شهید هرگز فراموش نخواهد شد؛ ما منتظر کوچک‌ترین لغزشی از سوی دشمن متجاوز هستیم تا درسی فراموش‌نشدنی و پایان‌بخش به آن‌ها بدهیم.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442118" target="_blank">📅 20:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442117">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81dda67827.mp4?token=GZdwWQIQVVNfMVSc2_T-4EaZ9QOoPTSszF4jvNIHg0ynB3nh8c02F4KbbbzJnhkTTwWNdPS2KJte9lMGn9G5V9QLjeKZTTXpINkqE9ph4nKcckPeBPdoI2LY2M3FZiH7j1ZKSXwyYK4RRxpDrBjnUha30oK2ydCVIt6xH4xK3sRo9Nd0aakhZpEl25B1jhZRNF0MkXtPEU_ey1l413GMx4G0-4zfKbDopfVA0992BR4CGGlLcZWlo443LuViLU88QOotsbHjXoz2Luw5LVgPQHpabNS3aZPv4GAeZtVLquM5o8yz1HkSaD4qig4E90xQe28zIPhjAvSXj1tncSdavUzldlsFAbDy3z_LHQSJaPvQLJnlCTWsWx5L-o5pVfH1jkpeG90ugZayHluWnafKycOkDAW2flrURYEYvIXEE4bSrek7h-bHeNA8zo_gxFF4CaZblueW0y3PLWFKzt1MllqOqNKJgwg-HcpxB6O30fDRinpFxGscf46Iv9O5P0Xea6wQIfP7LBxpad9wEDp9EBBmlc58Vo03AtOIQzisLR0u0buAR2-TgyI5vGSUDoCFNCEr1ckJI0hnGFTqhWDS23NCZC2Vcc9RVFzYOWycmHfOsgR-1E08pigTcKXB0uXdIGGE7Oiu7k8xrjHML4pnDHQHjE9DAsejzx2F37pwsUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81dda67827.mp4?token=GZdwWQIQVVNfMVSc2_T-4EaZ9QOoPTSszF4jvNIHg0ynB3nh8c02F4KbbbzJnhkTTwWNdPS2KJte9lMGn9G5V9QLjeKZTTXpINkqE9ph4nKcckPeBPdoI2LY2M3FZiH7j1ZKSXwyYK4RRxpDrBjnUha30oK2ydCVIt6xH4xK3sRo9Nd0aakhZpEl25B1jhZRNF0MkXtPEU_ey1l413GMx4G0-4zfKbDopfVA0992BR4CGGlLcZWlo443LuViLU88QOotsbHjXoz2Luw5LVgPQHpabNS3aZPv4GAeZtVLquM5o8yz1HkSaD4qig4E90xQe28zIPhjAvSXj1tncSdavUzldlsFAbDy3z_LHQSJaPvQLJnlCTWsWx5L-o5pVfH1jkpeG90ugZayHluWnafKycOkDAW2flrURYEYvIXEE4bSrek7h-bHeNA8zo_gxFF4CaZblueW0y3PLWFKzt1MllqOqNKJgwg-HcpxB6O30fDRinpFxGscf46Iv9O5P0Xea6wQIfP7LBxpad9wEDp9EBBmlc58Vo03AtOIQzisLR0u0buAR2-TgyI5vGSUDoCFNCEr1ckJI0hnGFTqhWDS23NCZC2Vcc9RVFzYOWycmHfOsgR-1E08pigTcKXB0uXdIGGE7Oiu7k8xrjHML4pnDHQHjE9DAsejzx2F37pwsUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای ترامپ کیک تولد گرفتیم!
واکنش مردم را ببینید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/442117" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442116">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ex9LI-gOF9VVxkNY39vVF13B1CT17dsdTNP_X0fTHwvwbSE1mlh7k87HUZcyvlm7I4PCYHezc7aDMnDqxL4wNgl78EMpbBLrxTQeZ7T-SBqSLdW098DQOkivd7UgJD4ZtVaKUhTdJjkIg-2Pl4bhSNjDhgHMc5f8dnFhjy5DReK5efwn-smeACO9gUrILpzfgXgB83kCLUEQFs8zbJx6rK_0NupKsNO5Ptb5zaP2ACuOYbffTCtn6cTSbR8Tanmlhq_VivleLAlOi91lElHVsb_RcPHK4SnYnzSsQeUIeDQ_8UCfXqR4aebfJJysEvuYdfOKFgqlYohKEUpgRXHRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامبک شاگردان پیاتزا تکمیل نشد
خطاهای فردی کار دست ملی‌پوشان والیبال داد
🏐
لیگ ملت‌های والیبال
ایران ۲ - ۳ بلژیک
🇮🇷
ایران: ۲۳ | ۲۲ |۲۵ |۲۵ |۱۲
🇧🇪
بلژیک: ۲۵ | ۲۵ |۲۳ |۱۷ |۱۵
@Sportfars</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/442116" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442115">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۳ شکار امروز پهپادهای حزب‌الله
🔹
حزب‌الله: یک نیروی ارتش رژیم صهیونی، یک تانک مرکاوا و یک خودروی زرهی امروز در جنوب لبنان هدف پهپادهای انتحاری قرار گرفتند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/442115" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442114">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd60451a9.mp4?token=YZ1MqffZMdA8-tYkQRjU6Yq_SlFXDH6thWqVO-6v29vv43gCB5bWlL4wfD7fLHVygttVDLlFfjLPsb5w7_yBY1Y8wk1zrwBcjNmR-VEPeDOm9oxtUsZbx3UmKzDQ-qNvEKe2BUOabz9EpMh2pmgl7Zp-YmYJGrkymrdNsevjKaJnUVIOUiSTnz3V_8afTVWMhWOLR7uQHr7BZ544lYXRnSrSwFWYYhOSD04klKeeXBZxGeQKaOxoDjVfz8zkT29L48VsB3SVpRUfbIO4zgPhOb3CMfp3bz_fG61OyNDhqAAeCiwUvfHTZHMBZ1ojheBRNv8VgP467zv4d7Twv7oOJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd60451a9.mp4?token=YZ1MqffZMdA8-tYkQRjU6Yq_SlFXDH6thWqVO-6v29vv43gCB5bWlL4wfD7fLHVygttVDLlFfjLPsb5w7_yBY1Y8wk1zrwBcjNmR-VEPeDOm9oxtUsZbx3UmKzDQ-qNvEKe2BUOabz9EpMh2pmgl7Zp-YmYJGrkymrdNsevjKaJnUVIOUiSTnz3V_8afTVWMhWOLR7uQHr7BZ544lYXRnSrSwFWYYhOSD04klKeeXBZxGeQKaOxoDjVfz8zkT29L48VsB3SVpRUfbIO4zgPhOb3CMfp3bz_fG61OyNDhqAAeCiwUvfHTZHMBZ1ojheBRNv8VgP467zv4d7Twv7oOJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ دندان‌شکن سفارت ایران در کنیا به سنتکام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/442114" target="_blank">📅 20:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442113">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
🔴
پزشکیان: هیچ فرد یا جریانی نباید خود را فراتر از سازوکارهای رسمی تصمیم‌گیری بداند. @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/442113" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442112">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
پزشکیان: برای من پذیرفتنی نیست که در جایگاه مسئولیت قرار داشته باشم اما بخشی از مردم با مشکلات معیشتی جدی مواجه باشند و شب را با شکم گرسنه به صبح برسانند. @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/442112" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
