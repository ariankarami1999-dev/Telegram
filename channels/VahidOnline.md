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
<img src="https://cdn1.telesco.pe/file/kiJZpLApdaHsvydG61pV_hYeFislCrBgh3Psc5QXYsiL8fzB0RxR6XrdtfI1xI4S1WUMsVvchVcpsO4JPuPWR-VHxyDF5v4cm9mYP1Xn8QMiAgXIoJX67hl9Jzje1RfqDZKhyjjO9ZBbpA729pEazuilb_J03JYf24vEl8xxTKdr0hX7UQkpfwKO_kYpvQ4_cjm5TPXjnVDg-2Q5NtgFcZON54Ic0HJfRTaVsr9O-0kfsShEnoT4CdT8L9O36wSPBxd7nqyUofqHo9bz7mc3ytLFTWPvj60kep436_DbCCYXexsnaBDIEQwn5A_LYXnGzgXB9xo8AJ_7u_qTyV10LA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 00:02:19</div>
<hr>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=H8b2MVd0zJ8qrtB34Qg8YKC9jDSIb5sKASqXwuPkJX_oUe2S_TnF3YA0s9zS-tV8uABXrDgWFSaXB511K1yX8-g44wk5rDE5VJ2F2TNenRigpRPxHj4PRg-NLfiFbuWAV7eYYXpzBj8GU-u8WXMyRQl_H6O8ei08OZz0ZNpubZ1ME3a0ZqrR4M16XXeiKdsL4QOlsYkCsqRw12Yj2znHWMnwfNtZVCjburE47I_Oas3eOa-O5PSq9gsp_P0-QC-V6KHtHt29FkarocXdIUFOYN-fUa0yaJGFKZZlcQfOkbt9pzCgDltFqt4z52b_h5F6L-RWjYy-OTAplnsAUZEOBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=H8b2MVd0zJ8qrtB34Qg8YKC9jDSIb5sKASqXwuPkJX_oUe2S_TnF3YA0s9zS-tV8uABXrDgWFSaXB511K1yX8-g44wk5rDE5VJ2F2TNenRigpRPxHj4PRg-NLfiFbuWAV7eYYXpzBj8GU-u8WXMyRQl_H6O8ei08OZz0ZNpubZ1ME3a0ZqrR4M16XXeiKdsL4QOlsYkCsqRw12Yj2znHWMnwfNtZVCjburE47I_Oas3eOa-O5PSq9gsp_P0-QC-V6KHtHt29FkarocXdIUFOYN-fUa0yaJGFKZZlcQfOkbt9pzCgDltFqt4z52b_h5F6L-RWjYy-OTAplnsAUZEOBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR-EOjyiuv9uB8zu5-FCZiEUf_WchAWBK6S74J5tE6257va03ijFvqmzWsOPhNU_-w6jS2qjZKhOhS-8tUpleIBkgh1gAyEphawqDKv9ExeaZZ7vvLFv7kh2wC9NkIq18-NtDjdK8ttTy0DJlaxLnmoOWSviGknVL86U5MEJs3AfkBYYk50y85fuvxWLrKddU5T6Ruo-Go6efIMFS93y9yyMJ7p_L3PugItqSHMoHeeGH2vZpLVYr9Hi9YXDxl24d0wFZ6qJzYQ8Z2gTeEIhOZWpBXJglvPlPtNQ-EdrLLfWn44SgVBFDEHBjbW800BMRlfTW3wy2GaJmC4C2u3mPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 192K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KB2t251ILoC3Wc3cK-3gOwnin4VfFsnNJHA-em9Qq1W9YggxrWfVPN0rv8c5Dw23nfEk5QAv7cEEqajSHf2CAg1_UbGg8XJu_tbsQ_G2Yy-YZc6foqbJtohCfBKj1ZoODntp8m4u8qduHZR3YIuwVmhkq9lGBXY1ffUwkyM8SRYJMPlqpNHQTdrvHZAnhdWuOk-8Yvji4ciKpTq64xwtxQxn2PMmEam0aOpk5rtdcaF57wEkNdSd5CoEmv20yXgzPcQJ2SU2ZVWyy0Z8smpg502BGfer1qvIbABa03Ujal-b0XRpjqRlXdv6kisuPx-vIE71sIWUbsvZcoSdld7CkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8srkHCOK55tJkIal2pRh_dcg2zQEEAVfIaeCnQ41i8hT9kN_uljxApPailh2jT4ntrBf7Ts7rfXRKpITHz-c2WKORGeuvAE2vmofL24hlfb9e7Gh24-2Q7b59GjY7P2OC7t1gMMcQDNc1DnJQfCdAnNemlL2kGaUKnZ7F8HNmLd0qz-g2LXpBYNowZSIQ6hFdIAf-fiA6k8nmFS5RfATdKo6ZTa9Igg4RdNpu73i9A8Ne_6IQ1OH-vOFc0R4fH_nyKcgWuak1pNQkmSKMCz8b0KJys48QovQfWgDVByfHYnhqC45toXLX5V3yVuAg2XcwvMg3r6BY-1JfmLmDpCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LllBxdqlaqbOD7lBHNwRVG3kfQbJD0N_DcsOk7_H954qDrxs5Iu4OoLfO-APmtSSS6yyCRG369yB73J3ZvFEInsDU1U0A-inV5yIROzT0WW5HnuIQha0sQTxGxQgih1Q_wCPMnTWPh0fBpHgUijqgUON5SNMh0Nt5zdaxrvAOvU6vwJeMp52EyDUKgxEZRCj0lDSfKy1UVXteqEGRG_47jiBzcIRCudcKjnzgJiTM3DEB1LNwtFmSONyWIkngkrKbDiSXcKFuqiPls3IiPutwOtP1hnQhOvLBYOfE2qyHpPd_ASIiweo7TW0-ueFl6yqLsLDfKGbaIX1t6f44nW7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rfQSzeSaQabevMZLx3Rz_O4kqnPuNrmwMvgMZza8TxdykBShLdAO1ad6cn12OSSokWfuTmObzz_VPyGEVcdxPO0cDYKe1bAE4Njly_PvpXKneXNLQ63s3K53s03YCGmo1Y0DsM4DPy2GbezZKzRWapaNn6wSeqJbmes6J_ZAOOnKch7aCwLMr5okQFyJ5jj7YwQDekau4kpjZJIOMjrpzDwbvSIZlSI_UyZn407Fi7jC2afCk-hkNCfHaSzmbQA7IiDQ4NSPJcOCjP4ABGFhrMAlv6GTRLNDQGM8el4EOywSl7RHlxfYz3yiTJ_aZOko9wmdzBkb4wf58P2zQoz4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=iRy6Qf0q7ot-StHyJdCtWpbiH_Ri8Wvi564wigqdYPD9EJ5ElHM6bwv9atmjeeP8VKTwtCDTDHvBoXsxMXdluL5S12SF7mJuM9Is2E9bTh59LlwRYw9Bq57tT7A3a8k241oB5BkXKsItyiqqSvfGan4Yz_CTwKXpM2UEUytPV1KYnhplSEN1vG_oLmXWIQsBX_zMyxAgDdYsndj1nTtAtxM5uJOkNlJtQyUuIbnid8riLakVmpeXy7BB4G0DOAKPNDDunovrFK--3xJeG-SbzQip7iAARA5T_FwOM0TrDX1_5Ng3kakrwP111u2Wk_lwdgTXBzPggDEU8w96bQwB2rpjuhPL5cGttA-zioPbnfwxA_qNQcvx2D1D0e8CwDQ61lua3yf1BIEUGhAWptc62-zicSYBh9TXVpYw7KKH6V5FyOcu_wrYS6VWFAVVho5NLYwLU_L6U7D9EkXWy5ZgYLCmkEJtAYjZKlMEOPXA63tmjeaFr7OjaEPy9_NVlzJi7FoftX4RMud2MMFUvOu2ezHbGE9e4ih3gNatW4Xe8vF1l52BnbopKx9_DKZnZyHoBYqf67S-tcnqR7d570__HyZ2uT3RGuXTUVQr8mFFP0nIKthjUJ1kyc8QHnpJAw1j9S779O0zIyG7LyTHY6Akw7B46lF_gIiofO9jg-tyUH4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=iRy6Qf0q7ot-StHyJdCtWpbiH_Ri8Wvi564wigqdYPD9EJ5ElHM6bwv9atmjeeP8VKTwtCDTDHvBoXsxMXdluL5S12SF7mJuM9Is2E9bTh59LlwRYw9Bq57tT7A3a8k241oB5BkXKsItyiqqSvfGan4Yz_CTwKXpM2UEUytPV1KYnhplSEN1vG_oLmXWIQsBX_zMyxAgDdYsndj1nTtAtxM5uJOkNlJtQyUuIbnid8riLakVmpeXy7BB4G0DOAKPNDDunovrFK--3xJeG-SbzQip7iAARA5T_FwOM0TrDX1_5Ng3kakrwP111u2Wk_lwdgTXBzPggDEU8w96bQwB2rpjuhPL5cGttA-zioPbnfwxA_qNQcvx2D1D0e8CwDQ61lua3yf1BIEUGhAWptc62-zicSYBh9TXVpYw7KKH6V5FyOcu_wrYS6VWFAVVho5NLYwLU_L6U7D9EkXWy5ZgYLCmkEJtAYjZKlMEOPXA63tmjeaFr7OjaEPy9_NVlzJi7FoftX4RMud2MMFUvOu2ezHbGE9e4ih3gNatW4Xe8vF1l52BnbopKx9_DKZnZyHoBYqf67S-tcnqR7d570__HyZ2uT3RGuXTUVQr8mFFP0nIKthjUJ1kyc8QHnpJAw1j9S779O0zIyG7LyTHY6Akw7B46lF_gIiofO9jg-tyUH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3okoglNWK6mwTcNxx4WLTumrIFDHxaQnPqDsKF0lblWHlQZ5U-W32GRL7HwtNvXCgu_Qq-UW-g-6YS81fgHYHEk9xDmYIK5jisSjHPyQAY6jPEOqAONL3cOqFh1NXQ9F4O0PWx2Q2jhtRIwfpPpL71S9XrL1GWoY8Crulu4zutA93DOY7J7viob4pCMF2ZlS7n7gLD9zS8e-lTovoVxZ_bkPjOOsaTxPgkDw8snbeR5A6_SkGaX_Ov9yYVIcBxnUWKXO4Baryuy2otmEE1-BD4c_uSSygUL8BbHUkoL_gAgNXnL_Tu1ML-cRtDH1SlSGtgckSbkEt6qkBTUVerTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=Hsuth6daWQUJJCOOVrp7cPbvTkMC055F1oFVeVCaUZOySn0Dj279POZkUWViOZlHAJUBy0t4S_fxHX0oP2rURR2ZBu1Bo9b974nCnYUDC__lPN-jqkHHxmvRqrFu4WuU67oLQb-lqiwPscInIGAzZAIVUCvAzvOq7_BxXLV_eY9Ksax2x_jMI3WRfnhfB6JKBAD6rf6KkxWpbvtpNDFTwxDTfPV03s0bqFpQGY8hOlB5qKem7fHkkZ6G2xzHmbrNZeSBGm0YOKXtq3Puw2StJjv4HGJlsZT9B5m-AsBiikpJne_oApCMSDVFmREucspWHZwqx9kSpCxFxjHEZV02-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=Hsuth6daWQUJJCOOVrp7cPbvTkMC055F1oFVeVCaUZOySn0Dj279POZkUWViOZlHAJUBy0t4S_fxHX0oP2rURR2ZBu1Bo9b974nCnYUDC__lPN-jqkHHxmvRqrFu4WuU67oLQb-lqiwPscInIGAzZAIVUCvAzvOq7_BxXLV_eY9Ksax2x_jMI3WRfnhfB6JKBAD6rf6KkxWpbvtpNDFTwxDTfPV03s0bqFpQGY8hOlB5qKem7fHkkZ6G2xzHmbrNZeSBGm0YOKXtq3Puw2StJjv4HGJlsZT9B5m-AsBiikpJne_oApCMSDVFmREucspWHZwqx9kSpCxFxjHEZV02-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=XaBwH6yrdxcxH5ZNVdTpB6S23R8cTOWlhvtHkrm8cmc4gSPXn-Lp1MWzoQPZwhFnipGru0VCRyFxuVMjk9JUsVGA30J-b4S65cg3qBuykIq6bJt2iHKhwk8hLYM7OI9dwb4lfRhMy5rsdA8GIz3ZCdsWc7edjUAYwMSDeRJ_Mao9FD9kPtuOMhxyDO_YqYZeLpYk5T1SVVAHlAsGnHE8ZyjWZO9s4blMI5jWqD2AgHx0hnLEYA6AqBLxn4A27pNtHuhyyEtlB03oigr01r4iZUHNuwq5GM_DVnJk6k-qjF1qmWxb_XEskAxp3YPTNWvsW6GOWFObI8KCKxUcbue6Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=XaBwH6yrdxcxH5ZNVdTpB6S23R8cTOWlhvtHkrm8cmc4gSPXn-Lp1MWzoQPZwhFnipGru0VCRyFxuVMjk9JUsVGA30J-b4S65cg3qBuykIq6bJt2iHKhwk8hLYM7OI9dwb4lfRhMy5rsdA8GIz3ZCdsWc7edjUAYwMSDeRJ_Mao9FD9kPtuOMhxyDO_YqYZeLpYk5T1SVVAHlAsGnHE8ZyjWZO9s4blMI5jWqD2AgHx0hnLEYA6AqBLxn4A27pNtHuhyyEtlB03oigr01r4iZUHNuwq5GM_DVnJk6k-qjF1qmWxb_XEskAxp3YPTNWvsW6GOWFObI8KCKxUcbue6Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=Rk93BOnROMUZXLUkGecpmD-wvtXSIWJSHEpEjm2C5O9z1WYKL1krij-c--gxLZEmLja6vdQir4QvND74GSWJ5YrE9GuRBRRsh97Qhr2fZATYs2vfLVgl3FTBW0gAar_KE13XVDXe5rKIX26_0Fa4iPtTZ_83JtvsP54_2r5T5tk_MNCZM6jVTiNuD_JwiLLNaqJPDx_7PAIAsZhn903KhiBB5HSqR9R9iPBbYbLK5tE0EGBURP1fmE2FzVMH6LARlSOKy6AeRuZorSo6Z2toMnZFosPziR4y8nqEA59Oyq23mfGZAYcJaV7FlGZ4pPeXg_j1sz4oM368zMKLha5QoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=Rk93BOnROMUZXLUkGecpmD-wvtXSIWJSHEpEjm2C5O9z1WYKL1krij-c--gxLZEmLja6vdQir4QvND74GSWJ5YrE9GuRBRRsh97Qhr2fZATYs2vfLVgl3FTBW0gAar_KE13XVDXe5rKIX26_0Fa4iPtTZ_83JtvsP54_2r5T5tk_MNCZM6jVTiNuD_JwiLLNaqJPDx_7PAIAsZhn903KhiBB5HSqR9R9iPBbYbLK5tE0EGBURP1fmE2FzVMH6LARlSOKy6AeRuZorSo6Z2toMnZFosPziR4y8nqEA59Oyq23mfGZAYcJaV7FlGZ4pPeXg_j1sz4oM368zMKLha5QoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=eFZJk85vNxYiDbbUCYIlgJerzlHDSo4oRL_QNFxOwgEvGtJRq_1vJjF_JJIbZB0x2kMtMoXufTSXU5w4m5EGaySyPY4Oyk1TXOqTImckONjfH4AJIGZmZoHvU0oibas_xbxS4ZS-BJ_I5RHcFvVHzQLOR1qveehnRWVfGbxZQqBvl-SJ16UF4EqEWJFcIXILnJfQkJ1HJN9_P_-8XzG531WpGcQU3m4it71MFqE2DnD0SB1zT8q_o7d2t8VYy8y2ctPFm4TyEYv21U7SkNk-alJosgRUh7OExlKFHO7iW3OrbfYv5G-vOS-5AT9B4hxNQjuGEB1PjjRsaLF7vD7I7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=eFZJk85vNxYiDbbUCYIlgJerzlHDSo4oRL_QNFxOwgEvGtJRq_1vJjF_JJIbZB0x2kMtMoXufTSXU5w4m5EGaySyPY4Oyk1TXOqTImckONjfH4AJIGZmZoHvU0oibas_xbxS4ZS-BJ_I5RHcFvVHzQLOR1qveehnRWVfGbxZQqBvl-SJ16UF4EqEWJFcIXILnJfQkJ1HJN9_P_-8XzG531WpGcQU3m4it71MFqE2DnD0SB1zT8q_o7d2t8VYy8y2ctPFm4TyEYv21U7SkNk-alJosgRUh7OExlKFHO7iW3OrbfYv5G-vOS-5AT9B4hxNQjuGEB1PjjRsaLF7vD7I7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNxVLDTnIx7tkjrRUtRtWWzASNqmXbWziJ-kFqaw78boGyAiz2e-s18-mruDdbfo1pIKv-gh0-mpFD-BEiJyf_KXY9pU4y163Rvx4s97VYBY5TH9sNNFdd1e7UJMlP_JHuvY9AE-e2JIcP711qw_FGcCf-_xYjqvBdnZqYTRtd_-ymlr61YcEhvuJb-COsgG0CqP7H8qhvHuDTIGm36Ir3PejyCI4yEMTYzQdgNkaZAv7FCK-jp6pQ5iLcXYYbRYQ0zeKd9KYQWrzlx2QRBgRCRnTpQX3-_uuLkWdrZFemMeDn5ZkF23lHFMfy74ZRsZfTjDA8MOJTg7pPFbW7e-PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgzrSJYlJnjxyc3mRvS2GbYNGMrZDxQmfYJTyvI0EudDguZVLj_o1nw13yBBJGfldqdKWuDx0qqkq8iZ1HH71ezLNE876PcZFtI4UZW-4L6iM_Amxx1hhlJq-wERAgP21rQo-CqiriFL2yhQ4_oaGLfBR22diD47HXG5_ptTRJ3D3ND4ZZJ1IsxnQrR7SQqEdFhea0oIZFXmyWm9gi9Xfq4CnOL9y68XiJyWhvN5xEWonW_p_bMF1jJtlyobO2OCVWu0fuDt8xQATb2KxxwuH2XWSnT_ujMzwI2AzYcaMjAdmJpPjv775yb9VQhheuVktC-h41KkV_TxJVj4fSoddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLWfbmAarCj0Nuf253vgF7GVBivjUHsECqQQ7ephP9FYyJG_aIMN7lJDd6E53OFL2EoWLw_hsZokY5nN2fUxsdT309UZejLQIw65xTJ4wgpnRP95dbVAhVKN__cZOdOMPgYj6Nug1C1TvCP_XILDkGRJZtO6-x1f2m0g1IoRkma17MxM40YF9PD1qoKM717_aQKi8RpcicBMIrb7XlxfWpgpoKX5fd-659Nl5wew6uWToBpgeLikOsDuAlOVNsu_AKRxmNZYXyirW96s95tD7kM9sKpFIKCv9wJRHxR4PVEoTouqOPwOLwFsHKG7C-msmaydqVyaaFTH2DMwU7mXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP5lPKOb2VioddVInMn2XV8-BHCPH2MnSLHOB-Cxh2Mr3dewvXp1WkKDS3C2WVTcjjJfmIJ-c8gYJBZzFNkpxSwrpaUkZFKjNteeCZzwLxm62EtMMIWKBv65BknKOv2s459Kq713uL3ELUW0o7gW3oHahMDJIGLY_k-qcpbKWgjMo46rC-SeaEEtd7cuPjInHx9G9Gcj3FmaTtUGNm720d7Upm0skJZ8wKZyVg-gBxT-v8avUSdJML_NQZ3b6dCU5MNX9TfJKnmtr8ISqhCok89oTU9NcFvpuNuUNnMjlIDNKvCWsEOzPDMjqjWOi0LDKTOxGgKT-wd_s-_QaY0x6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lx_gLOdYjSFu3aMUIHNpaRpqIe5ct7zWkP6HCFZPaaq66Dmxh45pLTeenDY08e6Lv56gBPgNy1CM9TXtdVb8vI4vvqP661ZOg6LI0iIZlrbO3Uxx2lzuUkIIGNgvIGIpRxCh9grY9yW2qK18OSJ739kVEyVAQyer8O0xMIbrY0zivwtWhMlpOkHYUUrXFmzGK4_v_X9oeA5GK_lqqatu3YO7bEU8NeVFoAimF1wFELpjC2MinvT5nBuP6bHDeWC1eJPsUIwszaZnqeQBVZtoVWdH5RBNqHrWfmRMzJJuSAhXNuopnNMr-3mo50FivX2VNQMQme9DGpd6wY6c9Hzajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZamD-p2H5kCVPuy84_5g0d_tPAzZOGmlkCasRc1HLFyPLiGIPI7juQqP8PlMHACWGsU0xcNb8YiBdiDAWmzB-euln6eBKgnXcbtFRkZ3fdwNQs-YMLdqMzSx-e3ske-OyresxcvUDEJiJMIHl1qfkUs4UaTKGwZmSscCLx9nfB6KUThALGvONcwF28FmttigUYen1jRNYiNqPOiz6UmsITTG9C_KIvbiNTD6vgcMv2dhfSD3VCQy3H1GF_myWozUiGOORKrmBzGsagj8KQoNQqLDopPCUDGq2jUHqxqX7Cmd3zOfrl_1coVCfG5KotJNAKNqZUY0KDD1_R0R4JcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pk8a7VV5nI9bmDAQDal84Zo4WCuK7RIOdXJsk9mBldyxgZGhjL9oU-xxkGt740o_TxNIYabXXNrpW-DcFiUmH-1RzmOZRlSHHie--gZCyfN-TR1ZlBB1W8KFxuiN4ahiaTQPW2T02JdNradzW-Rri1THqkEd2kabxnIX0HJ-7GSA-tVcASNemaHmG3sy3hSVY2mmvzrjKC2UJHztlhv643wRptmGblkX8CnKgjzLXfYVFLFE_z9bKCaL4ulzwll5WaOfAETIHXLgdXGQwzN7HjT0qlCmKT_D5_b7JcB600c9pJWVAOPOkZ2XahWNCocKHY9wPILiQsPKvMY7H53oLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uPCMrUH5sVCTYNg3txa_-jyxMfUKead3jvpiZy36w_4nLt1CdQZJp1YIAt5E52LjQhsGAerDsdCnAI2-0DLD4Pr_Ks46OuadEfMvZLpT8tes4-FT2JwSESIsGF5Inz8M5iIXLFqWt_67K-6lVkrty-8O6_AVIRf1LCCinU8RAhnkkG0kvsp-sTrCW_Rdg3n8zU7lCK5kKzPhfle5Aa2UNsQoF4rJWcptzUMewMgbXeE1J0oxd3j6ZRauXq_45c5FS18E9R3Nl9qTKsJgQiKWP3IzK9o3D0tqvozraQuGKEcnQICm8mXYOnQjWx3Y0CY4gvomfRw3FB_Hdf3AfOajZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMeGJKsIDRpqivmjGsMuzJm7FyjqVfMNz-XohzSpKLYQXHYTaa4dorxDKSP50DQD9Ied1IfyqJGNe9dIkB1udvA491uYIiXW-7u6ycZfEhho44qOOSz7meD1MabgO7hNca9NaFtxM9irb27xR7_cAtitZ1vb28QGuR0HyV17pJhRG2GpPL7bFr1ct5oGWcBPYUg44Tia8W_Kfd6fRPH0RzIOhTfwpJsLkzT__WcKrHnrP-H5Q31oOrMHy0dg1dRNfLv8aEWKAqW4bsj3_brWuSkpH6zz1skVbneGakLBU5fXQ73hQA0t_n9w0w__2bwibRGtGEdBurdyC9lTFZTshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etsiufiEzF7PyD7iyXaELAnclwVfMtFabGsDdFt-KXS30Lprk_-MB0aEj8Nl-zAjc2lJsb-SPBKQimd5lgjQpaUiCkmcKkVX7jfy6OfXxP2zOkZXezejv_Txe_e8LmFUldGU-2VUgKCo1G6R6dy-4igUUC9b80B7kBfqwX4QBpxq_5yURyt15MOQdjuKo2TwXM7JM8boVy0Q8fGdJGirszYJLdXUB1gmk4vbgIhaGsl8P42tXk79JL9r3T1ieWT5GZa4bVWfYkF2Vfy_wb26PUG0fmQgHdc_GqogNQIVmSUTy2bW9MxyQx-On1aS61CQBlueKFv356jFBZ6Px4e97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/poM0NV19-6NZcmio2BOTzRiOKf3RDkWL8Ym6otF396US_7tj2ZAvFE_hlMewECGmw7-TyDfLqQhRLY_ZdgiP4gX69U31TJ9Au9Is9fVobU-hzlCf22sMb8zocIJ2lcVjYiTlAaXMXEjwH9MHKBWd8A5ygvjji56xn8NJaejdlmC6hfBQXm4y-oZlsrA-dnU1f_ZNJkIlo97rk7Jee3heK03dZARF9bGH77aGg1Om1JX_JrEzkabMl6RriaF-Y8QddFg4Ot4SFgzATIutj5fZS9RwqqPcP8ZmdbhPTChkeKT2GqYm6_DSD2soCSOVYhTcN78vNk9C01LofrE3wl59gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgu2ATQXj14r6QaRZYuiCZfR1WtE4T06_In8vN_dMoGS6QWyjOOpJ9hRDh-OU5bRhxnXu4ZgPPNThFqPCCRN7uazEVU42xVao7DNutnSCqgmiz2FLuo4L9T7AbxHhJamun-B-PQrzanDNKu-Azi_L900F5yjNsMnlSdRwvWh0vahP6CuMtvIr2QLSldIzC91mzBdEVc_IN6ZVrqZE3O7z51M04ryI_hBfJ9sXCXJz8fgEHXYqhCXH6fOdddBQPMGcoU9VjgaqdY4d0RRowjkKpjsMIVRnO1o9XDezxulKyl5aPFE-0QrSkP501DW5R04ySugyw5cgRvDkLkYolvVdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmWJLHU1XVrrgsA_7v3PqTYvf06E5wmXXCE9HEoJCZtGKPqytP_oESrGNnrLpj2IdtVD2m7Kcnz2zkPaLyjl792imYxN37n14dpVxkIXKSBJ5QKsMoXTUml96C0jUhMYXTZNeOtljMhwxyDKcBVe2I5D8iv6Iz9X1Bb2wFJkDG41F-QWlQRThnNpHRYpGibhQAGCwH3ND7K7sMtsXSMQHuuenrObBkTpqa0HJpbBDBX7mMVLaVUdFFTz-dySXEFnLQyeSVdLLedkYRiQzt3DbEiJqsToXkZsEnNII0tvwyz5ju8IyRZfd-TC4VRC8vvqnBDS2nJqtBbbEKjvfw-spA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQ5PljJSBmyivAxFIwN7goKsXIqD9rfDJ6HQwKGZfR4OlZ97q3xtIH5QHcsyixGXhkgQCcmntRSjeJjWIRGbgHnRoE9q0oJkp_CW4OuHGNZc4foyt0miSBXU_ItH2mhAgMmMe9YceWucThLnCgVIMZ_DDu-tHjUD-3kWLzCJDQ0g9RVy9Zc-FQrxMuGwXuiybMKxBe3UJg__Vy50U_i_RzlVS9l0fX9r9LhBHWwFmb4OaAL3_0HS6GhNmQTc8aIZfKFJ_-3ROtHSN3xGdWPz5jPoghRFQiSZNlFVST7Z6SYTkqnqTz4C58RhmXT2K9xel9aNzrtjoqn5F6SBX1UJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4JPn4A9VxaeIP5tEUftcPWWNQKvhmUf-voleuUvaNo07RZh-bRuyFU8bk2aPJNWBbSqDsV5i0b9cYy7U-hwJe7Vx-sTahkBj3qitD9IJG02GhXec5lefvOQ0SnhjX2C2Pb1so5N-bUA37Rhk0kZcf2MfYSDcadXCOOEPhQUoEEuPMOZyFJd0iTsNlTxwWStB8afLUu7SxWn4vVjPvRFVRisJC5d9CU-Y1eL1FUEGoZgFys7kciBcLg5qtDmdZ9X0AJ5Qv8bsqrUjnH4pD9fY3hATRQJTJhRI9t7RTJxvbi-kvLANlSQxqWZZ9KWk21tqUXdoNcyVNENB6_rCtMjWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=krYHf8ybHAG6tp3NpywuM0DqNcJWDRB8Y4OrvmZ5sFl7H6_lEK4GKfe1YANYcHh3Wu04rmCsAdaMUuQm5UjQU423VNhs6BQHtDchvFra023Q_rr8Hz1SAzzeVj6vUy6sSajNE-Fpv-s5p0g8XMvq7XKRtXb6HMr90d7gWZCP70qdKOBoNE2Jqv0FO_jLZY5_UefRgpgRJkFpJNp9fVzwKIj2SilRgC2-9ddN_XZ8fvUMh7_Xxv5wi-grAZu6npPA5TM3IGe7knSHiy4537EOJrGkTXlJQImhqOmoRfVXFi0Aq_BomoXgw6Cw69et4NV38meugsyiZjhKF574RIfE7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=krYHf8ybHAG6tp3NpywuM0DqNcJWDRB8Y4OrvmZ5sFl7H6_lEK4GKfe1YANYcHh3Wu04rmCsAdaMUuQm5UjQU423VNhs6BQHtDchvFra023Q_rr8Hz1SAzzeVj6vUy6sSajNE-Fpv-s5p0g8XMvq7XKRtXb6HMr90d7gWZCP70qdKOBoNE2Jqv0FO_jLZY5_UefRgpgRJkFpJNp9fVzwKIj2SilRgC2-9ddN_XZ8fvUMh7_Xxv5wi-grAZu6npPA5TM3IGe7knSHiy4537EOJrGkTXlJQImhqOmoRfVXFi0Aq_BomoXgw6Cw69et4NV38meugsyiZjhKF574RIfE7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/To64QwGvGyMizWCLVcrXiHGcW1xbHpJ_2jKXeCgzkgTUrbWiwVkN_z4wWkV54oxlzC2xJbg_sDcaTxonhPJlqXUEZl4vlHOc0zXXiPSS6gHI1QI4LutBPjhnb7hgNP3tRyTTp6M1wcuVHzlrOytxPk-6a7pdSJlfwiGJ1pbL6b2ixVyMXUVnebO3pja9r1T1qIKbyef2DbNoqTHWbzK70dWUJKZOwjh4B4vsKQ8Yl2M-ZwxxwnBHPNjvTST7Gb5Lrqhg45260YhVPOC-ALyvtc__aLWxjHPutDv3V6ZxUw1P4ABFF-f6fH0MXD2ak01DKN5263Byu2T2fB8CUJREew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SX1YAFbpkOJAwZVgvJH2Hg1yy08d2kV0zA6ym_FaYbic12zO68eEuvmqci9QXAcD5eUfhSnLzmMI1oIeudbKUr6VX_OmnCOng8MvwJoBUI6OkRzpxEWKiy6tlEycVQyIhKcO17BlIddkpwlTk6DoSTNBgRTGpHS0jezBMmSGgmxJeNeSn6QiUmY6DWKZMNrGJ0V4pDFJJxUXVPwcnywHONNd0kSf_L_XilVVCgKDJnwqNo9AvnYpqFaye9sTn9TLPuu-5iLDDmHeUy_f0jDrOAwFUzfcQTlqqzwFAjm9EqSieEEAPgexP75KOG2j80YbpowwLhz7YhqT1-U6qyUWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=EwXWLjBIBPLxDGcij4mOSEZbSr3LF2zLo2HVmkC0FiVRWqbULsPZojZ3vOx4keOOD0I3CkJ_69p1RVUIC_sl0Cl8DxE9r7ftpbUecSmkVOjG-TtcQakZmfBNqfUUJmQUCceIRuOPIpvny__q4OrblrtNzk4SZsKBWRSuYFxgrgqrtzWtMmm3vHNH6X3k5hLd2X0yJ1GM0KOf4QsGJx0YBa1-qhO53va5LHltpHliFMiS0dF2an2Z6S0CEOiu7i3AqviaMgAUE40Ew3q58bAQGNrNJuiVdCDjdn7-mDgaflTR5Kn3Jzfj3550FqROeYAuY0s4BpnZTOQQjq-MScEcTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=EwXWLjBIBPLxDGcij4mOSEZbSr3LF2zLo2HVmkC0FiVRWqbULsPZojZ3vOx4keOOD0I3CkJ_69p1RVUIC_sl0Cl8DxE9r7ftpbUecSmkVOjG-TtcQakZmfBNqfUUJmQUCceIRuOPIpvny__q4OrblrtNzk4SZsKBWRSuYFxgrgqrtzWtMmm3vHNH6X3k5hLd2X0yJ1GM0KOf4QsGJx0YBa1-qhO53va5LHltpHliFMiS0dF2an2Z6S0CEOiu7i3AqviaMgAUE40Ew3q58bAQGNrNJuiVdCDjdn7-mDgaflTR5Kn3Jzfj3550FqROeYAuY0s4BpnZTOQQjq-MScEcTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=TedjtPkPcAsW6wpF_hQkdSFl2do_l3AO-XyMYSZLyvQFe5CzBKIKoYweS3EJsk4fOTc-PrbhblXTm1qE8pP0TbCcf9kFq2pagndHvjEGX0sj6Wxx2oidr06Gv5VPIlWJQtNH-h-gDOoWm5fupQIT5Almc3Tl9ka7GGnLhmW75KYsGXPX-TUhk1Gz4wpnBm88vLTuubJkWLqLV3p41pR8FUdsKihdb5Exs5hCVNUlss6ix7nF8Z8dqXxgu8VBC9U693huJ_HOudQI0ZuGTRi5_cJYMZqstMaR4hEbpifGuC2KYzxAqTawejo1XILizzlsMwmZBSTagRXXMKSk5dvEMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=TedjtPkPcAsW6wpF_hQkdSFl2do_l3AO-XyMYSZLyvQFe5CzBKIKoYweS3EJsk4fOTc-PrbhblXTm1qE8pP0TbCcf9kFq2pagndHvjEGX0sj6Wxx2oidr06Gv5VPIlWJQtNH-h-gDOoWm5fupQIT5Almc3Tl9ka7GGnLhmW75KYsGXPX-TUhk1Gz4wpnBm88vLTuubJkWLqLV3p41pR8FUdsKihdb5Exs5hCVNUlss6ix7nF8Z8dqXxgu8VBC9U693huJ_HOudQI0ZuGTRi5_cJYMZqstMaR4hEbpifGuC2KYzxAqTawejo1XILizzlsMwmZBSTagRXXMKSk5dvEMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMgms13NlkUu9SO3aBpsY-TNxTfZ3LooXB1owm-IF5UX9xlmKwCDZL6LGSup1b6jo2vWjn84IFdpGlovcsT0by0VqHuETcAEEYMcK4VmvYjTQ-Ccv0-mQqjnnE4RZKfAXm0E3_wATO_2brOx4PRydEaSCClSEEJem0jSDA9YU-IzhFmh42nU_OHmKeFW3rn9TsbDv46NfqB81OlfFdjUzMFPdfiE37Pn9SxZdJ_Z8T5DMzCssh06upXckdLkG8XunL7iz43uJ_-2q2fCJjHD76AZ5i4_5aXcC5iAdFVGwpaPcWqlklHyDOjMFk_D7CFIIiBb4ZZ0_xzpi66w86HgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=RG1shbVHe6JIdk9GR6jfRHzDVP_ekIJLG32cusN7VyO0BG87jKzHJ1JH_L6EFheUp1a6mFczn-h9ibrZAkgVwPWU2kW7fabjoLc5HYLCaHj4LUhJRkLvDy6gi46oTddTTkIx5Pg-g22PtE91b5ALaG0uTeN0m-sI_ZTySSlYdNHuglcda2epohKL6FIP-mVyWHUy5jRimJ148G2Bo0cIwGosi_d79rSlDX9RlPq32Zek8f0klywGrJ3t1vqCjWQ2-Hmkv4Pz6M9aKACdHAN9gpi-asDWGhQmi60w6PyZ6JyFR2qzUUUkroBNY6T8zuEAAbtlahb1TOxxmVCSlvRPEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=RG1shbVHe6JIdk9GR6jfRHzDVP_ekIJLG32cusN7VyO0BG87jKzHJ1JH_L6EFheUp1a6mFczn-h9ibrZAkgVwPWU2kW7fabjoLc5HYLCaHj4LUhJRkLvDy6gi46oTddTTkIx5Pg-g22PtE91b5ALaG0uTeN0m-sI_ZTySSlYdNHuglcda2epohKL6FIP-mVyWHUy5jRimJ148G2Bo0cIwGosi_d79rSlDX9RlPq32Zek8f0klywGrJ3t1vqCjWQ2-Hmkv4Pz6M9aKACdHAN9gpi-asDWGhQmi60w6PyZ6JyFR2qzUUUkroBNY6T8zuEAAbtlahb1TOxxmVCSlvRPEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc96kz27xeZRsMzHWCiJPXXDAaUu6-TaGmZf-NvjtWkwPUBBq-ojX7MM-g1lvCw6EPO-v2kelbWMX6J9gAEJb2JxN7s7uayCrrFQitxvoJBtkC2owFAlDxFwLuB06ICTyRGcLGzwUDSMn458c91gWUmFTeWuJ38zEVlwqahpo1gOkKuOEnBcJyKRr4hSPj3eqgVnSE87R-zEvOi14kmnta9rXOhLa-MOpPuUI2DpW_eNwDFC8fHLCBsUzjkiN2j3dVwXZ6VCYjxBCh3lafu5rZCzHRdhx3sB91II2ndrEYEI48dTV1sGrEplEU_J1s1x_LSZtKSZUPlfMLUrALc3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jjFkQBMgzZo20kkJS07UPHRR7JcxQUUFX03UsaInZtwwBMFQ1pW0wru0i7duR7jqYvAXGj59XvKTkzEZRIyh5tLQ0AchPIEamPtdpKA0u4vsstjOHwJtZc2OCm-SQJ6kT9_H0MEjdcvetLxjBObZIeDzsu0ted_3YOGIZe_xfrJQHbi6JBRqW5jiKFYMhEzBDnOPPG52ZPhazsdpquPkNHZax36T8kE5yKrf5iYre4EU7t4gcxfYhnsmpeu8Ta89Xx-4Y0_Uf2XIdtKBm_X9xCEcDrArd8wGoZIHKeLRreDoMFYkw300SrvqYqKfe2gney3qJo18b5UysDQKyrIqcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=QsTAZcuTt9q31xtdZHIXrXcaqAo4JoS2Bd-y-NN5xTIzLXtOhQgCNLcWm9AVMG9BG5vj3--lT4QKjaMDLoG25dE-20rZBTM2_8NJ_lVmrBkAmV0H07RXGt9ZY4ikXuabNNN7zLxLGJDAGGlmSDKjruLtjMNV_mk0MYaOlJL-QzUq4reV3-e7GMKjPWVqK7BoiedIFleOAfB1ZlH0iYSdU5FOtOrmdysq77mepiBGtm1068_h5BVqkJ6VblNJEANYIp3s-nMd3jpczFAYwRF_jInmSt9fZOz8-p4aHVaNEq4SvJr-4gWQQpZtwNccr8q6W6Q0DsD4KJLOhZ1UwJoiZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=QsTAZcuTt9q31xtdZHIXrXcaqAo4JoS2Bd-y-NN5xTIzLXtOhQgCNLcWm9AVMG9BG5vj3--lT4QKjaMDLoG25dE-20rZBTM2_8NJ_lVmrBkAmV0H07RXGt9ZY4ikXuabNNN7zLxLGJDAGGlmSDKjruLtjMNV_mk0MYaOlJL-QzUq4reV3-e7GMKjPWVqK7BoiedIFleOAfB1ZlH0iYSdU5FOtOrmdysq77mepiBGtm1068_h5BVqkJ6VblNJEANYIp3s-nMd3jpczFAYwRF_jInmSt9fZOz8-p4aHVaNEq4SvJr-4gWQQpZtwNccr8q6W6Q0DsD4KJLOhZ1UwJoiZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv5cfLF7HUn_jbJ_Tp6TN0z1hfXlchplgbB9YWyWylkG5frIJNNw3_kfzYVYV8hlYWVh5VcvC-QEtwt0j61qB52omovaB0ofqmCM7STzO_xKxoeE_ZKdFPsdyvJY_z7LgjVrZZmLqZG7lFJ18Q-gvmZJU9j1mX1DB-IIywjRrnaloBCVJ0sJHfu5QtwxAcUpxR_XjPOioVM0d1pHw7Po8zJsfm7z4eDRQviSejkWJxK3sJFKEZm7zYXKgrtaZaI8fS6Z8WevOqwJ62I2XejGTD9U7tWjrq1mYxniq7JAZEpHJajiOvn3UJCHgMviq0lI5ZJUnHX3GGVJqJrxP5cTwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTrw7MLeDSaj6Xt6Uw8z7IcBe6vC33HWNpWxpbMkOL-I4iqUcWhnLZ7pqxftIYHwDjqR38yIw5BsHuWnJLPHKG2JsZfWcJNxCNB9LiOC0ROaXGT3JV5-yBIPdCvts6GwPxZSSivez2v-5UKaZ4ez3TrdufG6zLQPg_gVKszcGpdvELkY3II17g0N-HBfDhmc36rPbq_D2ImeesXaCF_DsbH_cxsbf_TkbyRLSNYFOkSZL9JoFmxF1g2Y58t7gJLGdPczcmVSOCRDsBkzHhg0my6auWfVwXkzDvSZfcOXCqJHF4BvBeIuvXBHsVJwdMmuzsJN_D-hQ28AVe7rk3hhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XMkKJYRXU3GqMeTERkqI-uEX3zQ8s3NjcpvBowZdBNyOOM29AawCHqWwUdmJKY8CEq8hS2gnb_Y6FjTlY10w3oJ4SYCQFB4u9IVKvybVCabbZuuRAU_lIXZF2yQNZFWeb0OFby4AcyTB-HItX4t_QIAaDsYY5JIIY6I3HaBBt-aIODjE-pRUUhIqpSpoj_eKZIJi4wy2tgt0IE0gYggfIJ8RW7jqdOJ_tlraCPdwS1SWiBeLddrTVz4Vc-Gbcqe46VQgskXbRjODt7wNeR1MMRT4JtXsXq1DBfbcJdTY5erP55vkXaKqYWwO5kbsU3PMPqoL_8iKsuws834AcYISmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/feRtgaWG5lppLUu--7LAgYxCTt8qrSZ-1vzMuPLS55N9somX5dNJnCJ5bQD9dau6kc5ylobY5nsfOHWm1LEzxjqwQcfGlJ2JqonDJCqJFVKsqYieyKN28c6EonU580d774YPbRnCi6gTIn8V2bKc3r49UpzbKyorihJnbvNeOfpAWnT-kDM2UJXw-ApJZ1l1Jvx7t4cXvdQX1ZHmXD2XGflhHmBS9vl3gnJCM2HVFb88_Xq_7uJTD17awaLJMuYVbEfFlYn_Akl7QV21hoRCuXekzhQt8eMCgFo0gSAi4YUjo404eBtNm0nSq6g61rwY8rDeamygzWrGwMilSPD6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pmyAtupiXNU_dpI9MKjnYJCU08HAZJYyuXyxGYis3b03Cv848axOmOci9fNgzXqwQsrUDX9X4zJe5yD3mmxqnvH4Hxw3CbhL9s1m9UKsqkazwIHc2GJ93hd9QXQDBucVWw243LzosSE8cqYOnp_doi8Xy3nkNHkpWNl56CSz2yks4dAVLRBq4lYEGjV9mH-mcahPhwzFS6felTdtqygeeGGuBE7FjD4ZsoKqxeDNBN9l5PRZwU-jZatm-F78acCS1cq2wrOrUOtKNHe9EBEps8LIdkmAMh9U2B8sk6b240zXHVB6uSq1VyIAShjicwQHyIystUsFYrE9gpkldL2dng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EGC6PQx4GeYCVnlNPzpivUUmz-AlJze3Gylhbi0jcHfAj9ZE34DjpDhgn0nTPzEZEln6u9tbkU1ox8utZ2U34cccUAw7V5E5kS3RIaPWHFbRs8tu4qAsS7tC7vq9CC8nUUbPsXmQ7sbRrpA6PKkVRqJR4lwULo7LnOK2mIR1icdRdmtk13B9-Z0cqGxOltmko5W9KExlEfV_yaO2KP-21jrku0x9FxZ0f_IBYhMsFcRO_wcgIBUr4TpPxEKAqQvPH3wbnlvzSIcX9Uo3NmHsi33RG6sXExdBP9WS8Mc-PvJCY3g9GWFD5pp9wvrASU1S2bhyBCGR6aowd334_zCpxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpSaTXAcxOjBX0u362uRa8BQOcRRlFBDnsP0k4eOld8nYLADvF0cryNxIyElgJR1obaPxoXc1bjTa8DtaM-bG4Qm3j5GTEDrKE0bZoK48k1a_ZwG4q8vxidN2shrjypvsnp94ieReQGEuCMEOOM15_9HwmIuUN5Ta_zU4QNtokHa4pKmVykClEwP9JtFBmyhtar19g5q2uzTj_hwc6aftRlFY68iS2Aiq3mOLYYNpkUUpcyWUrA48viIzaGJicTxSP64qW05I6oE0x_r5WzQi0U65tXq2aIzPU_znSaSumyVl7xZjt5FRtupm46HKB8FWkq7iy2CRJDVbLgOzRFEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qECBAh8D8rqBlA6fZdhkTHtiqO_Oa3RYXVVUxHi3eu5Wqs7ApbAanO842tS2MrNtyngkwa8QYG1thadZ7YySP_t_tAIsyecoCrPJxiVbvg3BCCBsPmaxFQ2JtxD9-CJvRn6UoL7DA89ZpNneV6FkU6bDCRd1d7WGG6KOfT4roNoTPPgvnzK08SvltE3T_e570vo3mYo8LnV7_w3vYdKemt4EYw2TCunVxEkCaulFrQCbZhvzOB-366FEuAj9-_yppkfjqw9FgH2ds1F1VPPbgdp9n9eX-XThpM6jPtI7eRLKywnQMi6u7AAGzyppncsmoEmInIZK3HFPR5j2AHS4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=UIR64-pkt7AtAdBaVVsVZrmgF4vFz_MecnTHj6g3dxoZ07elbTXAdneN24pjbgiRSuykySjjKQdtdPXlzyKmzoRTqkQaj96ZJCMn17vmlIw01vuU39arLFOadJRR7GFsHIQso1QjWCfrPYwoKF3Q6Dx9OsJvI_hZTLzKg5srBXC4t3NLBV5ny1F29O2pm3ni7HUoBIxyWnIkA9-WjoclS_8nPVhFnKOArmJ9Z_HFIoNSXKYSCxhtTWdL6KVgtzSHdA0AEmYCRytQk6JPPhW5N48IjRZNPXSmvt2U14E4uSvULo-9DCl5-PKwn2YRzaN5NxM9URiAMOVzIllgFuIILQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=UIR64-pkt7AtAdBaVVsVZrmgF4vFz_MecnTHj6g3dxoZ07elbTXAdneN24pjbgiRSuykySjjKQdtdPXlzyKmzoRTqkQaj96ZJCMn17vmlIw01vuU39arLFOadJRR7GFsHIQso1QjWCfrPYwoKF3Q6Dx9OsJvI_hZTLzKg5srBXC4t3NLBV5ny1F29O2pm3ni7HUoBIxyWnIkA9-WjoclS_8nPVhFnKOArmJ9Z_HFIoNSXKYSCxhtTWdL6KVgtzSHdA0AEmYCRytQk6JPPhW5N48IjRZNPXSmvt2U14E4uSvULo-9DCl5-PKwn2YRzaN5NxM9URiAMOVzIllgFuIILQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامران غضنفری، نماینده مجلس شورای اسلامی، در شبکه اجتماعی ایکس از برنامه شماری از نمایندگان برای «تحصن» مقابل ساختمان این نهاد در اعتراض به ادامه تعطیلی آن خبر داد.
او نوشت که «چنان‌چه مجلس بسته باشد، تا باز شدن مجلس، در همان‌جا تحصن خواهیم کرد.»
شماری از نمایندگان مجلس به تعطیلی این نهاد طی ماه‌های بعد از حملات اسرائیل و آمریکا به ایران در نهم اسفند ۱۴۰۴، اعتراض دارند.
حمید رسایی، یکی دیگر از نمایندگان مجلس شورای اسلامی، یکشنبه ۳۱ خرداد با انتقاد از ادامه تعطیلی مجلس گفته بود در صورت ادامه تعطیلی، همراه برخی نمایندگان مقابل ساختمان مجلس جلسه برگزار خواهد کرد.
حسین صمصامی، دیگر نماینده مجلس شورای اسلامی، نیز در پیامی جداگانه در شبکه ایکس، نسبت به ادامه تعطیلی صحن علنی اعتراض کرده و نوشته است: «بیش از ۱۰۰ روز از تعطیلی صحن مجلس می‌گذرد و نکتۀ تاسف‌بار آن است که در سامانه قانونگذاری، امکان ثبت استیضاح وزیر و صدور بیانیه مسدود شده است.»
انتقادها در این زمینه به خصوص از سوی نمایندگان نزدیک به جبهه پایداری با پررنگ‌شدن نقش محمدباقر قالیباف در مذاکرات با آمریکا، افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3dAxIiCqNAshm5-ePrwcnvIZpNY3B9XtXn_rqdqheFRqvi3d_-WDuCd264CybqT0GZPN4ZVizjs6ml-0VE8FgGlCRbbFf-ktMPQzhcYbrB-yL2vos9FjsPLyzTOpby_3l1tIEVnGyv2oGp94_igm6dCHy3UQ9SqYPm1Cd-9svBLtutlGL5sNV9thHvCsKTkPNLLgZqawdJ1wWYlxNj3cJL_6UsTC8jTks-iFELDAxvND6ltXtrvgj4vte6HFoDIFLm__vzz9TXcBSqwrL8b-FBZssFjjBPRQajLJJRRzYFMmGRT4mMz2LZrrUlxhaTvwn5BDIt50omOSvRCSA0KTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CZog3R4nxrGMWq3mVuOzit4UhAtwQ5ptxr96yKDGZeOr1I0Q-Un5D4O2g785ox_vhswdvP2l3jSeX5br4QQ01gQVURJV80APMRkgXKO07u8SkijwiOcEG9sAWBLTT_8bihNjbInyKi4vfH-ZutgxeASTHVgXxXlTzWuOfPIqzI5WwQ_JhUnQ1nLJEszcrVfO49YHf3rX9fEPiW6yfC-RcbGf-7t22-R2VGKUED6nzFYX3FlliM6uuHD4-mBAU553DaOESXp0cTglWlZC9HRt3f3DFst-EkOM_HZbAWsFNuReKtb3ALT4MjWrGJfPUPlrpEVkE7J2K_KMpuowIANAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=bWDv1hND_CGMPFGsM58ePiTAeoCDbpqD-WlURH_x7FS41rCaWqVFQokXr1KxaHRpX6mTdxxaxgPc9NaupLn80DHxihp6Dysm5BiK_N6_Ocj_o9z1qoQoNS-pVdY9hGGR2CwKEr3L09C-cECG9Ikg3MuRjjMy5EWBCHLxzUCxZagfKc37Ojy-k-_8TrXVcLcoJlm5S2mWPI_DC0JKOvGs8_wZhNVC9PPSQsh5RCTdQ5up0qNiNx6akBr2LRjvRSC4JFtr6YEoLiW_s-W2NflYOvu6ybOsCqbmRkqP4txpFJ3ePbzWN9Vwai6Qt59S-0n0024wuJpMyoD23CEYl4VD_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=bWDv1hND_CGMPFGsM58ePiTAeoCDbpqD-WlURH_x7FS41rCaWqVFQokXr1KxaHRpX6mTdxxaxgPc9NaupLn80DHxihp6Dysm5BiK_N6_Ocj_o9z1qoQoNS-pVdY9hGGR2CwKEr3L09C-cECG9Ikg3MuRjjMy5EWBCHLxzUCxZagfKc37Ojy-k-_8TrXVcLcoJlm5S2mWPI_DC0JKOvGs8_wZhNVC9PPSQsh5RCTdQ5up0qNiNx6akBr2LRjvRSC4JFtr6YEoLiW_s-W2NflYOvu6ybOsCqbmRkqP4txpFJ3ePbzWN9Vwai6Qt59S-0n0024wuJpMyoD23CEYl4VD_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه دوم تیرماه بار دیگر تکرار کرد که ایران با بالاترین سطح بازرسی‌های هسته‌ای از تأسیسات خود موافقت کرده و این بازرسی‌ها «تا ابد» است.
دونالد ترامپ در پستی در شبکهٔ اجتماعی خود، تروث سوشال، نوشت که با وجود اعتراض‌ها و «ادعاهای نادرست» ایران، و «هم‌زمان با جار و جنجال رسانه‌های جعلی که هر کاری می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند»، ایران «به‌طور کامل و تمام‌عیار با بالاترین سطح بازرسی‌های هسته‌ای برای مدت طولانی در آینده (تا ابد!!!) موافقت کرده است».
به گفتهٔ او، این امر «صداقت هسته‌ای» را تضمین خواهد کرد. «اگر با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد!»
نخستین بار، جی‌دی ونس معاون رئیس‌جمهور آمریکا بود که روز اول تیرماه خبر داد ایران با بازرسی از تأسیسات هسته‌ایش موافقت کرده و این امر ممکن است در هفته جاری رخ دهد.
با این حال، مقام‌های جمهوری اسلامی بویژه سخنگوی وزارت خارجه ایران هرگونه بازرسی آژانس از تأسیسات هسته‌ای را رد کرده‌اند.
@
VahidHeadline
پست‌های ترامپ، ترجمه ماشین:
با وجود اعتراض‌ها و اظهارات دروغین آن‌ها در خلاف این موضوع، همراه با هیاهوی مداوم اخبار جعلی، که هر کاری می‌کند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهد، ایران به‌طور کامل و تمام‌وکمال با بالاترین سطح بازرسی‌های هسته‌ای برای مدت بسیار طولانی در آینده، یعنی تا ابد، موافقت کرده است!!!
این کار «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این موضوع موافقت نکرده بودند، هیچ مذاکره بیشتری در کار نبود!
بر اساس این موضوع و سایر امتیازهای بزرگی که ایران در حال دادن آن‌هاست، من موافقت کرده‌ام اجازه بدهم تنگه هرمز باز بماند، بدون هیچ محاصره دریاییِ دیگری. با این حال، همه کشتی‌ها در جای خود باقی می‌مانند تا اگر لازم شد، محاصره دوباره برقرار شود؛ چیزی که در حال حاضر بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که وزارت خزانه‌داری آمریکا آزاد می‌کند، به حساب امانی منتقل می‌شود که تحت کنترل ایالات متحده آمریکاست و صرفاً برای خرید غذا و تجهیزات پزشکی از ایالات متحده استفاده خواهد شد، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما.
این‌ها چیزهایی هستند که ایران به‌شدت به آن‌ها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است همین حالا، پیش از آنکه خیلی دیر شود، کمک کنیم.
گفت‌وگوها به‌خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد؛ رکوردی بی‌سابقه در تمام دوران. قیمت نفت به‌شدت در حال سقوط است و جهان جای بسیار امن‌تری شده است!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bDeFsvTosMxA0MI5HGB8mJbZNF7ZJG1eGahiGn1mTgJAZAQ6cwcreCWVqWT1kEoFDZMSd-JryZIV6gzdzAYVtMFIBo4z_B_QsCFeS9HVFWhMDuA08LDcuxbrpiqPNLZ_4LUvvoCUdX_6ajSSMXJWAqg_a4xFIp-FfL27JabzNR-CjXNJ9nsI2ZowHAfCOIwjChI-Z6I-ka1eqZ2axSFWp4prVVHMe72LurivHu6IDRhBSeuBpdb2QxxoepEXpab-Vfms02Fi-onYsUp7NiCi_paTA0hHIKcQeEMNwz3UYmWaUmn5M56ppGKUgQodeS1mRNJWTHqTvg2BmXDEEXSpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت  [نان یارانه‌ای، نان یارانه‌دار] در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
بر اساس این گزارش، قیمت‌های جدید از سوی استانداری ابلاغ شده و از امروز روی دستگاه‌های نانینو در نانوایی‌ها اعمال شده است.
بر اساس نرخ‌های تازه، قیمت نان لواش به دو هزار و ۷۰۰ تومان، بربری به ۱۰ هزار تومان و سنگک به ۱۵ هزار و ۵۰۰ تومان رسیده است.
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران، نیز افزایش قیمت نان را تایید کرده است.
در ورامین نیز رئیس اتحادیه نانوایان از افزایش ۹۰ تا ۱۰۰ درصدی قیمت نان خبر داد.
بر این اساس، قیمت نان لواش از هزار و ۴۰۰ تومان به دو هزار و ۷۰۰ تومان، تافتون از دو هزار و ۳۰۰ تومان به چهار هزار و ۵۰۰ تومان، بربری از پنج هزار و ۳۰۰ تومان به ۱۰ هزار تومان و سنگک از هفت هزار و ۴۰۰ تومان به ۱۵ هزار و ۵۰۰ تومان افزایش یافته است.
مسئولان صنفی افزایش هزینه‌های تولید، از جمله دستمزد کارگران، خمیرمایه، حمل‌ونقل و اجاره‌بها را دلیل این افزایش قیمت عنوان کرده‌اند.
رئیس اتحادیه نانوایان ورامین نیز گفته است اصلاح قیمت‌ها با هدف ادامه فعالیت نانوایی‌ها و حفظ روند تولید و عرضه نان انجام شده است.
این افزایش قیمت در حالی اعمال شده است که نان از مهم‌ترین کالاهای مصرفی خانوارهای ایرانی محسوب می‌شود و در برخی اقلام، نرخ‌های جدید نسبت به قیمت‌های قبلی نزدیک به دو برابر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dKQgiFTzbc8ZIQegteEZYNsoevAVVWTeYmfiTFQOUeyt-EsROn_P2pXsPXna179nN6NxfB2XzVLFBFpa8GTkP8xlk9OVSC_LsnOHS00NFQkrnLkKnw8HMp40at5Xftmvm2IahYg-LlIjfwHKX5rKT6BZfiKv6U9PIdNzXjSSJMUhml9vpsxL5zDrX5Dn2JBZVfARXwXmm5HbudWb-pe-BMC3uqRtirF0DtPeCx3xosU3bymQIMbJm3XruLeViAPoKuIBnbWn1PRCQcP4HWcuOV2ghW_dHeEaVZDsjLBSdWKFeGSad5xcHYwChNi0FMf9CTDcayZCe1Zm-ZNm0tAxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TG2FVxNQWJLLC6AIFRt3gcltYhLSMBPnpAV0VJHUIa4CStFGuqJFLevgDnHfqbSQSUS6WGqZkjeSV7LSHcOD9n-5Mtq5mLgLLSoVxNLwBHnWHmLZJG2yE8wCBfUc2J0yVk3kJWUxg3VKq5wxd2WNHqAjOmgJ2NMAuOUx9a7sZ0-fe7zkhZYA2rnSQ3AtEs33CU1GgXJi9pruFfQ0hsEWxM1iN1Jk6XIbNFcJKuvlR63J8FRAkgvi0pWFg3ALkKBvQoc4qjWjyV0ZYwXBcY0OEx3vrEZRMrGf1LbPzmRTLWdO-uMuzB2r-1zJfe2j2wwufYXrklFCgBBozPBDbJhvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XuGYhXTrvUT30TdqQsGJi5XKoKI6pGKO2upZ_EGYfDNjz6rd-h2DNlNlUe_iZDEpdcfPUKlXbLxPyPDsr0W1rtqsfUm0drTWCgatb5NR689AgdUYUKAUqkK_OcCGO2B8Ig_SL-otPCP_LUsAAOHQejVDJy7KzthjsnB1UlsLebGkWayZaiaG3V7eS8AixvW7ufd8WhInn_oIlO7E5K-vEL1tHgo7WcRcBiI7_Bha1rgqRmH6KQgMB9VKzm9Yc-9fRj0ERINfjH_zLVVzoU8PYYleaU5cqeWuC4vp7gMGkXaXzYliQjXR5LrJHEMBN04U5x8lC5G0m9J6rjS1uw1hdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=HPd4GW8hp_NpO2l4kceV7S-UzQfRiyRTQCmvUQS4EZ6Jsvjm5OZFhBcgRokftWUzL0kcw7VFsFz2THgrL1I27nsQHcVcRhuTkyJRAhPHGZypWLNa0zNGyz0bAWRoG9qo4Lyh22SBRDXOsh1QuAH8MYbYX-oP8nmq4HceGCUWn23aY-P9G06lWutajRnj5pbmHoUHMW6MNS9H73NImWlf5EzFDmGaqzemvxAeB3Q_a0eOUdEWx6WuxOHLQoZ5hN4drS5t6kSG0Dk4tgpfbugPO-27hfjSd0-hY2M6UkxV-6yGtx2vhYTAuSWVGGWEwYzHetCeR03y-p9Fqab2VVtP0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=HPd4GW8hp_NpO2l4kceV7S-UzQfRiyRTQCmvUQS4EZ6Jsvjm5OZFhBcgRokftWUzL0kcw7VFsFz2THgrL1I27nsQHcVcRhuTkyJRAhPHGZypWLNa0zNGyz0bAWRoG9qo4Lyh22SBRDXOsh1QuAH8MYbYX-oP8nmq4HceGCUWn23aY-P9G06lWutajRnj5pbmHoUHMW6MNS9H73NImWlf5EzFDmGaqzemvxAeB3Q_a0eOUdEWx6WuxOHLQoZ5hN4drS5t6kSG0Dk4tgpfbugPO-27hfjSd0-hY2M6UkxV-6yGtx2vhYTAuSWVGGWEwYzHetCeR03y-p9Fqab2VVtP0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pu8-rI-kKE0dfDcS2gFIsHFezUMYbaG2y4ZzZleP-oKycfZMO3kkvWOeUbcwYal5nEqnzmJ6_68LELxBjFu9ajEY8KKmSPtQY731DyEc3XN6L3MAkZOGp7h9Ojg3foWKzW4CvI9Qf06Wb6GDno_tTVQlFHosuhbSdrRf_VsNAGqzQGe88lDZiNirOPbrB9tBy2YomWhzYhAAV-ERGCieI-Zxit8ReS3NtIy9AFhT5XW3u1P1A5Mk0oh9yVCmx1dseDX1lgffkqcVQIGQPBwrz7JHxlI2P-hzj5n6pxQej1d-CdIUBgHpjQ-ZXcrpZMk5yAKwbZYWGa-9b5iDMssSjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZWp4Q_zLxdcvHJN0N5cClvyBl9hURpvHHv8GxbXs2_3FjVBiB7hdhcDqYyhNyeFY883c09BzMWPl7gpDwFIGt1-cd4krQfE84L1TSlojWQl6fJUznwznJSzXTFhIrol-rU0j0gG_sSPX6e_NlAGPqSnQCjaNxOWt2yGxwWiv1Jlzc7vgMwuDa8bAvlIMwLQ9GvDH_g8tcZqN_iBO1P6Jew9ElVePAqT3-9GumRvIlUP_PjM-Aq1D-Uzg7_wek6nNMqKK1ssqXN9On_laN8P06sV7FKpTJwoE98ymwsI9mzztgdwdayDMl7LUUZau9y5qYWVet2A_GgpRkGPKgjqD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gky_QzI3x-_1iVb8_foJ3LPANkLLsB6TKWEG2gUIAg6pCwHy7Ruyr_oKFokD9SVbNPK6vbL9lMgnXGy9m2XE9hYA3j_OJNGFGARJzawEGz_8h5gr6t6ERcJ1oADXHinTzpu5xmuuQFs-JEfjMDDV3pXCa5_02-3mM7PUDF_kpOrKuUkx6nSqgClLw7Js2JukuGiYFd4IkqkqnC3pt0-asAsz1om4gnmDHB3yYyk-dL2ki9RJVCspGWg6syS2Cm1S2H0ShLeEtYKPFaHLo7K-yfModwAWVTv3ZaIOZsZM1OyoKGvzxVd3YNt7fbPqUIZHFQpz3Gm13YKl1MLGOlwlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SXcxEGlI0F0hUfjcGgUU6ohGlKwKR8ylShV7qtloPGZ_wK7TcwpvzunUv3rq3m5BMO9hyHVPWriG5uARuMsYbtFZAh3MJOlopmLW2499194FSGa94cieAqZxzH-90ijkuxSdfZE4QWfKtffYLfHZYL0FmmVz_8xIsEs7HyTPe_IlO6goX3F4W-gekEZSpAgvzgFX3J2IB4aTjQTXONfGUctTW-bOfbQAQlU1o1TdHSwTESbTxUXBuPbZhlcoBKxKunXJ2Skp40QG_bAqW2HIGRERg7_EPImxbsFie-9eUhPcTgWpooA1vGHAnKHmDcIdjd4SjfHAy9zZDha27YPhRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jjfEQxhQ_QM0KscnILbqS049hXbC5dsijSKHMn1vAPKbGJ_8qj5kBeELU7Vdnd_EY4ZZEid_HizO_GACdzfh778D3cAAzP02TBAsQ3KraMcJTabgaR0amjAK90hElZF8rtVnMCYVMuhhYekwWIRBRVb2ZIoSh-Lwvd2g34ZoTq9FXQwnifk0DsdILAoJVu4B82M0xZ82vueeF3Kbwc_9PUJWmbEWAT3IlxG34RfNb2yzc0wQhid1JgADcz9oUqyU_qOQ9JJuDzQDxsz9C6QsW1u6tPmiMctGFKA-0HdpzH6m1tYxQTWKKh8VTs8vKwHgP4OLkisrWPGzQ8y_5yWpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n8CoMeSKWxWZ0saKaE4rqgqwpmOFWo73TjgpPW8Vui2KiLuuSXJ6NcFaJYi9O97EpNjbu1qtQ4zDODyxbFA8uCkvr78oBKMkLxA_qEeq_19BilGmuFuHQu9Y4H4Opn-829VW_FgwyFVKP2kYOfiHq-2Lg5H6m-nvZjBSt-lyUUMqCJbL3JDD8I4oyyzbPzbjpc7Pgdv0Ms8hos-JftJ8H8PqiF_7rfdhYq9oc2n0dC5ummB9dGp_-Tz8tODkrsHmTlRoKdRaZChhmzCtWguJa3ipOTRIMkrB38xYwkOPH4nmmbNt3ObPFFCDQUHYmqy_A3QznlsDxJles5prr8o4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RbPQkD8iFnCDW9ldOaRhvnHAd8JLiVQ-BnFGcxKv7HBMxoHZj2m3Kw7IBGKtOzmRS0zyMzZRSqXfJKlAAxuGONetDs_Iss0PeYoIulq54-jOWs5jUHlAaoHITyQblIwXLocPm6uNxioc12v2kYMxc94aadzzTDk4aW6aNFAjQ-S3mNBxKs8k_hTO1dZp8lB96eN0ad1gXXdtOe_zYwWiAmuRjhzi7IKJVNc-GPrbQ1kj4mNyv8HGXq5l4UPstJet4VCAugOfqfqRaPthId5aowuYwnn_y17GQOQJvbYXHEBKMwDogH0rhZrNdeKNkfpJBB7PBieug446VaH6ML_CtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NPrN1REcG9-ekJmi5MIlqDF7zT24iqOJF6DjQ8GN20mSr2Slcgufjryv9_DVF1na-89SPeFCNZ3IATB551_w3RhWS4K6E9-b9rSE0BGvaATwcbNF3EMyf1A6daI5v09EZqaqcCnsa8ZYgrXnlTvS8hZdL_49NPUSYhGb7XBusS3py1qLAYMH3YXAec13FJ90BF19O3pmEJjhPopIAIPUk98fhhhG9OjdaPSSEFq0LB8He2qnzs1vHsct57IJJHxV4_3R7uMFAnksS2tzhj0Wt-bWrucAIV3_y9zZEiNmWuUTGMVvhaawwHeHmXRVQzcYQ_PfCpf5jx5yut6fLEw0tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد + ترجمه ماشینی
دونالد ترامپ، رئیس جمهوری آمریکا، دوشنبه عصر نتایج چندین نظرسنجی مختلف درباره توافق با جمهوری اسلامی را منتشر کرد.
از جمله یک نظرسنجی مشترک «سی‌بی‌اس نیوز» و «شرکت یوگاو» می‌گوید که به عقیده ۸۰درصد جمهوری‌خواهان، این تفاهم‌نامه «بهتر» برای آمریکا، و یا «خوب» برای هر دو کشور، است.
در یک نظرسنجی دیگر، ۶۷ درصد می‌گویند از تفاهم‌نامه اخیر صلح میان دو دولت حمایت می‌کنند.
در نظرسنجی دیگری نیز ۴۷درصد گفته‌اند که این تفاهم‌نامه اثر مثبتی روی نرخ تورم و توانایی مالی خرید مردم آمریکا خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uhe-DLtSQDyYHgkvOQYxv4TrkQVP2J97P8rhTzxjWRtkSpwG4vB2pptLsuorrwzIKCUXGTw_rmBfkFOcGGdwVehHGqyb79CdzUzgdILKoQFV2KbTn7MgMZUs0IieI1FCU0qqUyNRkNuDK2bp4RGMMSNxYze0nQb7IzHbiM6cpblg_Jp7LeW4A8101EN-oFMZyY1Xjh-yzFvxzEd3wQRKTssCvgihe5oayDBX6mK0a7TKiA1fXJxhF1e3Tx8N9EYfoszabMnxgqi9iAHBNGcbDVzDjp_LGV9pM9eHVLk1EpKWobyd2xTNO1p4gWC-TGdCY-ko8Yk6tO8-Smaicyun7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.  ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ویدیوی بالا:
به تشخیص ماشین، حدود ۱۱ دقیقه از نشست خبری ارتباط مستقیم با ایران داشت.
متن فارسی اون دقایق
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود. 8:15
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
5:00
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=Vnjl0PGW6rFTNpaAC7cHv24amrR5gf38JrxpF1a096UDUDhpiu-O-EI5A6zxVFsfscu85HXK8e45Se9l_1fcO4yTp0FcgeT_-VtQQpJkssn7aGgO6d36yTshkLZRzPNWiFtvfjd_YyBn2R_KptjHMfJORVcY0wDvdfjl6s4gEx2ReGRNXKk2f3xsgik-6HkpZjo6GCFmk5zJvR0lCbYmS5H7_sVtX5kO525w_h7h-Ndvgbclvmi-i8LZ31wm_iGqU5tfQDzCwV5y9DVD8qrDnnkN6Wlsj0vETsbp44HRJXHsBKp_CNT-Z666UHdDbMxe7tpim6_PWqjWnhkTb0JqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=Vnjl0PGW6rFTNpaAC7cHv24amrR5gf38JrxpF1a096UDUDhpiu-O-EI5A6zxVFsfscu85HXK8e45Se9l_1fcO4yTp0FcgeT_-VtQQpJkssn7aGgO6d36yTshkLZRzPNWiFtvfjd_YyBn2R_KptjHMfJORVcY0wDvdfjl6s4gEx2ReGRNXKk2f3xsgik-6HkpZjo6GCFmk5zJvR0lCbYmS5H7_sVtX5kO525w_h7h-Ndvgbclvmi-i8LZ31wm_iGqU5tfQDzCwV5y9DVD8qrDnnkN6Wlsj0vETsbp44HRJXHsBKp_CNT-Z666UHdDbMxe7tpim6_PWqjWnhkTb0JqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M4Vn2opOO5XK8pFhIq_QSnXbz8MqTR5aEjBUAfSX_CM-ajWOTy6Qomzt_GnUXm0UF3Ce2uq63xz_er5jnxxPVUmebJJT7MOcZbFigs-PbwPXGvD_Ozz0xRLz33XRFjHQQRcmVeRJ9iH0q472AgDORQtcKev342ELhfKA5CR5NqD6BL_ORlnMpkxYGahVncngZTUIoETIwFt9Sib6UCqa--L91c57OgvvOutcX_ZsgrjeDSP1eu9nL3fkydbUKP0KHJHDYSrB9vaG9Ht8l77CZNTw1vqakYk9Vx6RCwLeVniayXT1gvM7XoT6yAEzfAEjoeX5yNLJP46-W5XNwoyr5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdRJWUT_sM6wN6UsdI8c7u_AqZCfOfMGUHHoDs-BhiYM4lWpU9BNZeXMAVg0bm8arhwsPyEFuBQtHBTm-yHfw54rIsJyJFSKv2EyAxmGGFpUyk3PgMwh9qpEZGmPM_WYeHeggU01Ys0018SwRMy_zdlZn6fJ9nWFj091x9-bfLv1bUDwhsY0vjihrbw6AJ8tKGmQogwJ4hpBaaFWpCQd2Ft258c__jt78yCQ1fSEetXUA7GqyxVe9KWuTY5Bu9XAQWtNheOxdmCa1ItqWPHwHSfZD6PJGAakoBbCm-HGHpHRMi5ZloLg59exXUSPnGEp4ZcGBKwPwL69JgiFNDchGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، رسانه‌ها خبر دادند که محمدباقر قالیباف، رئیس مجلس و رئیس هیئت مذاکره ایران، که تازه از سوئیس به تهران بازگشته بود بلافاصله برای دیداری دیگر به مسقط، پایتخت عمان، رفته است.
به نوشته روزنامه هم‌میهن، قالیباف در سفر به عمان به همراه عباس عراقچی،‌ وزیر خارجه، قرار است با هیثم بن طارق، سلطان عمان دیدار کرده و در زمینه ارتقای همکاری‌های دوجانبه و تشریک مساعی «برای تثبیت ترتیبات ایرانی»‌ برای اداره تنگه هرمز گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76598" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76597">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HwIahOcflMmvG0oHDylMiK_MrnXF7_JZhA5AIdOC5CYCMJ6uHE9Sw8e6CpKNYbzs6goGHV3_rIjrHZYHgvqR-GXapcj0Ut-srkV5dZzfS23ov8TtgN_TKOLs47jOWq6KY2Ev88Q2v8GthV_Gy0g5hul3M16fEFQ6nprxWZqFsux6EINB-nr-0UBpQg6QOz5p8GQ1i9veftcm9i-4EJdKAGdjEnyycP-kUV2pxx8QebPJg6OlTEZMkSOFIncjfXVG8EWB2mZb3KxVzmZqr6p4dZaWx0uEg6wPaEDqBRBUIQsdElmDVFjnAQRgps9GjUh5aEbuX6ALzyJ7jQ63qmxipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نوشت اظهارات جی‌دی ونس، معاون رییس‌جمهوری آمریکا، درباره بازگشت بازرسان آژانس به ایران کذب است و در مذاکرات سوئیس هیچ صحبتی درباره حضور بازرسان در کشور نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76597" target="_blank">📅 20:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=WLH_dCer8wacp6o9Uu7w9mahgZw8MvPkIwZJuxIfZOUgJt6DptQ3NqB1MeUwLkD5rLeSM7O4NiPxPj5ujX17DoSl9bVRuo3FRoLWj5MemlnsCV7C5Zmouhh4AKgYm1R1QSZSWkSgLSwtaBcDeVtDqWbPKsGBl2zKNUw48kbWb2X_smEomv2STrRXdtGOHyijRCAalUWrnFxqnzRLDbSslf1gvu3m9vDlsl-zbu-Cm5cVR2024OAWLIpm6x2_S8aUTsIMH47_rEnt-eBnyPEBm_sXRUbOKxaMpyepnOfUA8KjBDLwnL9LQ9nrVhIh-zbLwFTgR3_BzTWzw3zjtkn4ug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f94ec11a35.mp4?token=WLH_dCer8wacp6o9Uu7w9mahgZw8MvPkIwZJuxIfZOUgJt6DptQ3NqB1MeUwLkD5rLeSM7O4NiPxPj5ujX17DoSl9bVRuo3FRoLWj5MemlnsCV7C5Zmouhh4AKgYm1R1QSZSWkSgLSwtaBcDeVtDqWbPKsGBl2zKNUw48kbWb2X_smEomv2STrRXdtGOHyijRCAalUWrnFxqnzRLDbSslf1gvu3m9vDlsl-zbu-Cm5cVR2024OAWLIpm6x2_S8aUTsIMH47_rEnt-eBnyPEBm_sXRUbOKxaMpyepnOfUA8KjBDLwnL9LQ9nrVhIh-zbLwFTgR3_BzTWzw3zjtkn4ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: تا وقتی که لازم باشد در جنوب لبنان خواهیم ماند
بنیامین نتانیاهو اعلام کرد که موضع و دستورش به وزیر دفاع اسرائیل تغییر نکرده است.
نخست‌وزیر اسرائیل نوشت: «نیروهای ما در جنوب لبنان آزادی عمل کامل برای خنثی کردن هرگونه تهدید مستقیم علیه خود یا ساکنان شمال را دارند.»
او تاکید کرد که ارتش اسرائیل «هیچ محدودیتی در این زمینه ندارد.»
نتانیاهو بار دیگر تکرار کرد که ارتش اسرائیل «تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان خواهد ماند.»
در مذاکرات ایران و آمریکا در سوئیس، هر دو کشور تاکید کردند که حفظ آتش‌بس در لبنان از موضوعات محوری است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76596" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cYMwsI1jRatjrY7chGSN7Z0cDZZ3kiYbNFHF67YCW8eEZFBvTL_1pI5L_NltOvI96U8IAQdJZ3-9fCQEsfVpsq4wj0yxSZEtb8P9H67baE3tViscLfId4JgMgGTjWVuIjq9eqBwbpH98E5E50-zx7bJoIBetYmlCHUe_69BS_7Yvs7uqeIVRCjNC7MeyPztPFAjn4O8ibL79Y_kpFrAJe1rY7czNX_dAwLQhxKXZkxUXDB2aRd7TsmguGFEBi1hDY3MhsaFlYyo8y8UH2YnG34Y_mOVD-Y0bjMP3ci8c5QuBWpy9LI87VAxxsIXvv6wEp5sMYdMrFKsFWbmFATNPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا با صدور مجوز عمومی، تولید، فروش، حمل و تخلیه نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران را تا ۳۰ مرداد مجاز اعلام کرد.
بر اساس این مجوز، تمامی معاملات و خدماتی که برای تولید، فروش و انتقال این محصولات ضروری هستند، از جمله بیمه، مدیریت کشتی، تامین خدمه، سوخت‌رسانی، ثبت و پرچم‌گذاری کشتی‌ها و عملیات نجات دریایی، مجاز خواهند بود. این مجوز همچنین شامل کشتی‌هایی می‌شود که پیشتر تحت تحریم‌های مرتبط با جمهوری اسلامی قرار گرفته بودند.
در متن مجوز آمده است که واردات نفت خام، محصولات پتروشیمی و فرآورده‌های نفتی با منشا ایران به آمریکا نیز، در صورتی که بخشی از فرایند فروش، تحویل یا تخلیه مجاز باشد، امکان‌پذیر خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76595" target="_blank">📅 16:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76594">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vErouvdAx5gffxkymJdtB-szdYpPH_ui9z-pDUHD7X6z0oK9Jp3gh8Z_FrNMnib-6QdPjZraJXZe-3-khoqVeqzXNe630RHV796WXzQZ1pDrnzyjl4JDle5ndICZAIJKN6VcCgsh0Jl2R3e6PVfGSsTb0SZSCWymDxwbO0NvURhZNhQkIODz2jt0fq3Xmttu6sIXo5JtV5YIZ8DFJoT73dQxSZUiV30Ajg-VwIRBim5Sad9zftfCkGmWGP9zzYZtUOzkW4BW9xdo5OW7_3dM83lrVfeg_jFX4BLiDiH0lATtth4jjZ0sI7RtxE_nLlNieOvrJmI6gK4UnnGNNUrvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس گزارش هرانا  در خردادماه ۱۲۷ حکم اعدام اجرا شده، ۱۹ نفر به اعدام محکوم شده‌اند و حکم اعدام ۱۲ نفر نیز تایید شده است.
هرانا همچنین از ثبت ۸۰۹ مورد بازداشت در حوزه آزادی بیان و صدور مجموعا ۴۹۳۳ ماه حبس، ۷۶۶ ضربه شلاق و ۵۱ میلیون تومان جزای نقدی برای ۸۰ شهروند خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76594" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76588">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OVThrJsdJgrCGEx4UfjbotWoePg-muyZAP3d-g3hKfnThLNEoc-Qxg0_8kYPi8HOBd-u1pHmx8AiMILC-utD_0su8F4XWzpMue4frZzX58uFoU1ZDaK1nUUu295WvQLdWyDL9Dk_10Dpi0HgThwyoveKmM5uLP0VBTT8WyNACj4xyNUKbahz3aR6rL5661SPFl6ubfxO9BA8XuTUi2kH3BVhansQjNfo02cKYvIybcGLN2bDtTzKvxq0GvbcNmrHchKh_wTPYpBhXmfqMWTqJRBsc8eTMjfcwXFyqXO0AFvPbeMYDeu4w8IXkcqhKJQDvsULWMPDoBm_mfCw-JKh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GZ21m-S26OOUFBEYSQThEYGITxQzL38BPvsIB7sd6Mh-xuLfSn8UqW706qEV2NsttLM7ayD_Ygc5HnOyoVHYywWaX9623s3IiKg6JNd-WQcUarWuhiW64QW-JaxQMefVEGsthLSshJ-AyaFmGZlBNdk1Tub73KQfu6OExLm9x1W0wpymY8dq-3gWL9rigAMnrpgUX2-KvYZfUVqker9NDIBHAf0Vg5a-qgGzj2pub5iTF05Uk38CpjKF-Rn8EaapJrtjUlH4pGCOggq0lEAE5iRZW0eBu_6Ujh3lscwYKf0ahhP74x5FsHnp18jqpeY9IzVtA7m72TXlLUGSfKfv2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lM8hwFyMZ16wCKkrkiBPwlknKq3jq8Odc8ePbXoLIsGkzZ9rKBOdTNJXJAV5_Oyvv383GSqnmKyrMGxmUDeELNtKFj90Y1B6qEFGytLgO9Qf5su7mjgfMgBDbKEn-Y0vYU3AcoDnc8EWpRBOLmrH9s1y2V6dHzwL-tIkPY3R4LOXIieYhK9Oax70o0gX0HQE_-MTRdX_qg-T1F0G6jO1S4DFPs0UrlorpsRU_m8t2xbZk1VKsPC3smwmEZE8iurSOgxKvdEsxQOQTgmxP1Sbc8EoFoT8HaWRb-B9-8zVTB0dDKpGG07CZD57P3vLrILQcSL9aL0UbGCZQZpGAQubtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DbzoL9LCXJHgFvHZu5_nGXDuwrXjtNM8jF6_WhmIVlhz26hBGjkiwG6X2Ni0Pi7_J13q5qhsAwaTOZt55zsCBL9-qfc1HxchHFkfVjfMlRtJ8oKRuLNsOjuJ1aa_32bxSEJGrY8bcJZ6TycuuizypgSMrK1adMMNHFZFW4kv_umCOEtJRLMTg046eGKhRW6Iss8ORobPO9rXa0JmU3BO-csn7c4iV-c2ZHuSLFw1W96GjMqPLUw6cQaIwYMDgWjW1mf-bvvCtko6CTKefhNKv0fam8f_JnudoM1147V0-_ib7OqXvNE2bTuLc413J68Bhh_IG1Chz8pns5EYbwZADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G8m8XQ1tCoPWICJV7EU3Rh2Busot1ho4LJqpeAqcdLArfOLtVAyowQhJvszEDnQfeykRkvmDyIS8IXdoZPui_2QFPHAg1C9eGZi78KrZfYhwB1RW3BQ9-5ZuEWvGcxpXgtzNJVt0er8MUv4fPiT3BUoq2Lr2_MYzNpbZ7nRb7vmrI62fEsAYjiJC9rB2Xq6o1EurZBXWTwZHp-ESRQIGSHk1_8RA01l0nVmZ759pOorNcGWh8T0pFr4HzExW0cV2xgs-PihwWnYMPaRPR85RhhcleV2xLluMUDTp-aTE8ogItUC-5GHDdba52-mA7CgJ8t177FbKZKuqrdyUpTvv-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=NOfdVHPMDILtSL5RcG77BAZi-eHtpiqbKb1IAA4djOne723_kFCvVb_5-NkRW-1m7tg2xaehVeB65GUIgXKbELKjp0_I4m1ASJ47JAFi2fj-Ewi7J1rCdaUV_bVK7k00Vfsh3EHbUuZKimUDKBlKbQDc45Aiiso8hyhFXVQmRJbEDeLgLpNstYPwE9GHaJedILgrVm7NTQ8rvM4nE0xoTmxMLoO53BlhuOf45J7YN8W-jW7QB3rGp8LsOC15NbLPhmRkQ0D4LrF5kYaYcbP5GVHiyVHhIlM86jWgFWDuUPe2LpYm2b-1ywWCpxDy0n1fRmy7bcXg9T8gCGJWQvLyQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a45f8c601.mp4?token=NOfdVHPMDILtSL5RcG77BAZi-eHtpiqbKb1IAA4djOne723_kFCvVb_5-NkRW-1m7tg2xaehVeB65GUIgXKbELKjp0_I4m1ASJ47JAFi2fj-Ewi7J1rCdaUV_bVK7k00Vfsh3EHbUuZKimUDKBlKbQDc45Aiiso8hyhFXVQmRJbEDeLgLpNstYPwE9GHaJedILgrVm7NTQ8rvM4nE0xoTmxMLoO53BlhuOf45J7YN8W-jW7QB3rGp8LsOC15NbLPhmRkQ0D4LrF5kYaYcbP5GVHiyVHhIlM86jWgFWDuUPe2LpYm2b-1ywWCpxDy0n1fRmy7bcXg9T8gCGJWQvLyQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه جمهوری اسلامی گزارش داد «تحریم صادرات نفت و پتروشیمی تعلیق و محاصره دریایی برداشته شد.»
علاوه بر این، عباس عراقچی اعلام کرد برخی از دارایی‌های مسدود شده آزاد و طرح بزرگ بازسازی و پیشرفت اقتصادی ایران اجرایی شد.»
آقای عراقچی این موارد را در پستی در حساب کاربری خود در شبکه اجتماعی ایکس اعلام کرده است.
@
VahidHeadline
معاون رئیس‌جمهوری آمریکا اعلام کرد که در گفت‌وگوها با حکومت ایران پیشرفت حاصل شده و جمهوری اسلامی با ورود بازرسان هسته‌ای به این کشور موافقت کرده است.
جِی‌دی ونس، روز دوشنبه در سوئیس گفت که گفت‌وگوها درباره بازرسی‌ها ممکن است از همین هفته آغاز شود. ونس درباره زمان آغاز کار بازرسان هسته‌ای در ایران تأکید کرد: «احتمالاً همین هفته، شاید از امروز.»
معاون رئیس‌جمهوری آمریکا افزود: «ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم. گفت‌وگوهای فنی در هفته‌ها و روزهای آینده ادامه خواهد یافت».
@
VahidHeadline
معاون رییس‌جمهوری آمریکا، گفت یکی از اهداف واشینگتن در مذاکرات، ایجاد سازوکاری برای نحوه استفاده از دارایی‌های مسدودشده ایران در صورت آزادسازی آنها بوده است.
او گفت هدف این سازوکار آن است که اطمینان حاصل شود منابع مالی آزادشده به مردم ایران کمک می‌کند و صرف حمایت از فعالیت‌های «تروریستی» نمی‌شود.
ونس افزود جرد کوشنر با همکاری مقام‌های قطری طرحی را ارائه کرده است که بر اساس آن، در صورت آزادسازی دارایی‌های مسدودشده ایران، ایالات متحده و قطر بر نحوه مصرف این منابع نظارت خواهند داشت و باید آن را تایید کنند.
به گفته معاون رییس‌جمهوری آمریکا، این منابع مالی برای خرید محصولات کشاورزی آمریکایی از جمله سویا، ذرت و گندم اختصاص خواهد یافت تا در اختیار مردم ایران قرار گیرد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در پاسخ به سوالی درباره تهدید تیم مذاکره‌کننده جمهوری اسلامی به ترک میز مذاکره، گفت: «آن‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم در شبکه‌های اجتماعی چنین تهدیدهایی مطرح شد. اما ما دیروز تا مدت‌ها بعد از ساعت یک بامداد در حال مذاکره بودیم، بنابراین آن‌ها جلسه را ترک نکردند.»
@
VahidOOnLine
گزارش‌ها از سوئیس حاکی از ادامۀ مذاکرات فنی ایران و ایالات متحده، به ریاست کاظم غریب آبادی، معاون وزیر خارجه ایران، است.
رسانه‌های جمهوری اسلامی نوشته‌اند که قرار است دوطرف روز دوشنبه اول تیرماه در مورد سازوکارهای اجرای یادداشت تفاهم اسلام‌آباد و تشکیل گروه‌های فنی مربوطه با یکدیگر گفت‌و‌گو کنند.
با این حال تیم اصلی مذاکره‌کننده ایران به ریاست محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سوئیس را به مقصد تهران ترک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76588" target="_blank">📅 16:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhItGPV2c6t6alXDRysfESyjSgKB-MpUDYnkP9uBiYC4qJkSYTVKxyrpwhzXGeiga2nT_avAK5orW0JXgTJaZZkUs7rplz3DrBXMzF4rptPxsIXuk4L2WB1tYmGy9wYfvFjNts-dtxFSduOq5U5BtPd36SyGzeEGKCm0E0FiGJE-Ec4kVE_LJl1XW7E0cJwqVV6cuLtQwJA4JriszxwFUpLPZWakaUG72d1Rbvvg_3EkGKGgiRLsjr-NSkAudXK06RdgXE2vm1N0XP3wR5f51T7_qskq5b1LE1g9SaAAN2XBYBXH61uXdkzIWIOyX75qWw5hr798AUkOv8ObvpYa_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میانجی‌ها اعلام کردند ایران و ایالات متحده روز دوشنبه اول تیرماه توافق کردند خطوط ارتباطی مستقیمی برای باز نگه داشتن تنگه راهبردی هرمز و پایان دادن به درگیری‌ها در لبنان ایجاد کنند.
بنا بر گزارش‌ها دو طرف از طریق تشکیل یک کمیته عالی مذاکرات، بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیدند  همچنین قرار شد گفت‌وگوهای فنی از همین هفته در بورگن‌اشتوک درباره همه موضوعات ادامه یابد.
در بیانیه مشترک دو کشور میانجی یعنی پاکستان و قطر آمده است که: «طرف‌ها با تشکیل یک کمیته عالی موافقت کردند که مسئول نظارت سیاسی بر روند میانجی‌گری خواهد بود. مذاکره‌کنندگان ارشد به‌طور منظم به این کمیته گزارش خواهند داد و گروه‌های کاری مسئول موضوعات هسته‌ای، تحریم‌ها و نیز گروه نظارت و حل‌وفصل اختلافات را هدایت خواهند کرد تا اجرای مؤثر تفاهم‌نامه و دیگر مسائل تضمین شود. کمیته عالی بر سر یک نقشه راه برای دستیابی به توافق نهایی ظرف ۶۰ روز به توافق رسیده است؛ نقشه‌ای که زمینه را برای آغاز فوری گفت‌وگوهای فنی بیشتر فراهم می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76587" target="_blank">📅 05:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q58Wz4G0JbRBRO7bkvaJ8gGUHmb2yLyCFTFxOd1yyeoDAHdLGnBMWRpza54YhUDlMW5xMjI2hL9UKmCtwfIZD7GqSSUtTLGrI7Vi7di25IsynyAVqNPIuiJXfPmQ2aSTMlTG7yxrbpUT8ZL8nFY9S2kuMTva3463slvBEJDiy5SubtNwy1ZX1j8RlbaCzNIqPkWOz-3InxT-ZJtgs8Bt6KULS2sVMUk0_kFHciyWU9dhadMRiAhPZePTVlVtLkP-nWW9DNmIArdIVQ_GO9IEaAQlarrtt6QSVSKmrbYMiVlQORP7e9FA5EHzlcuzAqK2-LQYgRnwLj4wjuedpZA8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین: ما این‌طور از سرزمین‌مان محافظت می‌کنیم. mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76586" target="_blank">📅 05:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e8eumKOjS2Ug4kw10o_ry0Q_9HZwAmm_xSK2msLPBIiMK3HXKizP-WU3q-ey7mKeqQ7y-Uoy5vIUEz340WPgMv57R5bk_Xojrbvknzc7RxwUlA4IJkYYImg7Z4Fwr-IFaa9xlUjQ5bLhgq0OlgfxMoTGQzHkREwoWWHTSafVZknLqm8ewLAo52uSviRCPWcixPTyr57fvi6saYMIr5NbAQM7jFVEdmMbLw6jMbAufJB7g6cwfRdtipUPrlJHVgBEFoti51veNFc5BtKj-K-o0KQ3LZ2gFP6iwqB3RsW8g4M6cfhTQMyAM8kGetOwKr09J20hWi9o_PMfDI3JRgcX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mqhxEME_QjUNZNnBS5kvQ8k_kSvvqqzYvqJFDuEUibc-W2OM7Km6NVnGgHTYEc2weCkA4cRzOQpp31ivjM7xN2xqkFHuQr7QVH8rKEX0Eg7-2xnWfOdQC6FVzr3G9Ek4L_JZpzwnZiVQs-wGNwjGbdC6v9gYruHqYv1m4VEGYCfPOdhQ1bhfWDwxAjB4gKU-xDgdtxkMtGcRjOyFRGTHgweEPDQdX578n9Qu0k_B5d7yAoU92wIZF8ZJafnaooe_5qkv1isbiJTlLoxmoycX8BHaoHZvxEolasDDDgjRvT9J2aRfTtWON6ORlL6adsVnIsQlb97Vjvow5dRb9vvEGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، اعلام کرد مذاکرات سوئیس با «پیشرفت‌های خوبی» همراه بوده و گفت‌وگوهایی درباره پایان جنگ در همه جبهه‌ها از جمله لبنان، فروش نفت ایران، آزادسازی دارایی‌های مسدودشده و سازوکار عبور کشتی‌ها از تنگه هرمز انجام شده است.
او گفت درباره صدور مجوزهای لازم برای فروش نفت و آزادسازی دارایی‌ها پیشرفت حاصل شده و قرار است سازوکاری برای موضوع تنگه هرمز نیز تدوین شود.
بقایی همچنین تایید کرد هیات جمهوری اسلامی پس از انتشار آنچه «اظهارنظر تهدیدآمیز آمریکا» خواند، از ادامه نشست چهارجانبه خودداری کرد و مذاکرات از طریق میانجی‌های قطری و پاکستانی ادامه یافت.
به گفته او، تهران بر اجرای تعهدات طرف مقابل، به‌ویژه در زمینه آتش‌بس و تعهدات اقتصادی، تاکید کرده است.
بقایی افزود گروه‌های فنی دوشنبه مذاکرات خود را برای بررسی جزییات اجرای تفاهم‌نامه ادامه می‌دهند و قطر و پاکستان نیز متنی را به‌عنوان جمع‌بندی توافقات حاصل‌شده در جریان ۱۸ ساعت مذاکره منتشر خواهند کرد.
@
VahidOOnLine
تسنیم به نقل از بیانیه مشترک قطر و پاکستان گزارش داد که نخستین جلسه مذاکرات نمایندگان جمهوری اسلامی و آمریکا در بورگن اشتوک سوئیس و با میانجی‌گری پاکستان و قطر به پایان رسیده است.
در این بیانیه فضای مذاکرات «سازنده» و روند پیشرفت «دلگرم‌کننده» عنوان شده است.
به گزارش تسنیم، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
براساس این گزارش، «مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.»
تسنیم می‌افزاید: علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.
@
VahidOOnLine
عباس عراقچی بامداد دوشنبه، با انتشار پیامی در اکس از پیشرفت‌های حاصل‌شده برای پایان دادن به جنگ لبنان در پی میانجی‌گری خستگی‌ناپذیر پاکستان و قطر خبر داد. وزیر خارجه جمهوری اسلامی نوشت: «صادرات نفت و پتروشیمی معاف شده، محاصره برداشته شده، برخی از دارایی‌های مسدود شده آزاد شده و طرح بزرگ بازسازی و توسعه برای ایران آغاز شده است». عراقچی با این حال تاکید کرد که اولین آزمون واقعی و جدی این دستاوردها، عملکرد «سلول مدیریت منازعه لبنان» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76584" target="_blank">📅 05:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76583">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx4EyHqaZvN1OvqHVMM-llT4PTJcbJpIBqgCmy6JUlK4_bsp3LaEerYEdXyyzDuskNemnKVsjQqpj3Vd0rnSCgQTJ940XAUePIHxk4evpnsTQ9IWuSQRh5oOdlL6JxUQYGjqPgHt82R-I2tEMspIhSAU1phGrdn0yscy-GPupyoM_J3ZK6i1OQN9EWeAyV-hH7VbNSiZBsvTSU2wlbozM0D_UzEYsMW-tqYBV9D3_oiCIZcBqGoFQCIaT0WnkjdbhWH3g0V6cYp_cNF6X55NkE0TYM-wnBBH5qoU__FqM0ZcpEPnXFaOzPRKP7tAW2mtgbZsudBjT-tjqiDlJvEpLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد مارکو روبیو، وزیر خارجه این کشور، از دو روز دیگر، یعنی ۲۳ ژوئن (دوم تیر) در سفری دو روزه به خاورمیانه به امارات متحده عربی، کویت و بحرین سفر خواهد کرد.
در این سفر، آقای روبیو درباره مجموعه‌ای از اولویت‌های منطقه‌ای گفت‌وگو خواهد کرد؛ از جمله:
تفاهم‌نامه میان آمریکا و ایران
تلاش‌ها برای تضمین عبور کامل، آزاد و ایمن کشتی‌ها از تنگه هرمز
اهمیت حفظ صلح و ثبات در منطقه
وزیر خارجه آمریکا همچنین در بحرین با اعضای شورای همکاری خلیج فارس دیدار خواهد کرد تا درباره اولویت‌های مشترک کشورهای منطقه گفت‌وگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76583" target="_blank">📅 01:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76582">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vcLJptwyt4xVm0WDYvQ0g6kc4O6TQ1T650JU9sc6--6GKoBcDpOESkvCfXKZ7ySl-XbcdPRi3i7FVxQ7DCZIXdgLH7eePueKBBkNuNhkKw2e1UbNOkXc8i9OGjS88G-8r9xRfqyk9bq9KKx8HP3VnjtRzdPbUik05MWESbgeqE2z_ZCcye2EhiDBKRLRv9utPFmOFhydyWgwyGsJpJ4Z501NGybySQePYraaq7dL_R-jP0kr2uHWq8VQX1cVLxFR7c8gbvoluupzBUJpzm3pWHDB2SqouPZEIay1ehAoNYTnF3d7aToNSh4fhnqbcCOuY_mpSH4cu7gezVP4YVbFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست قالیباف با فوتبال، ترجمه ماشین:
ما این‌طور از سرزمین‌مان محافظت می‌کنیم.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76582" target="_blank">📅 01:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76581">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YQ6S_5wkUVvVnqZZN6Vc_u-NZDEU1yFJ7v9Nx5J5Tp_KNC8lSX1mfPUozwWdECwiUYKekvz-wOWDpqtJwYuFCw0171rk6xP5TMQSo_5aSPRAMZrHxSy0Woy9lu7p4bYNiVHMM6s6tz_OEZOS2yqvF3X9gAzlYRMnHCM6ul2-sBKl02vHor0qMBFK4XF0VcoovuPLnmUzLF9AWJLFeI-pJpMQ3PpLla9xLERIEgCGIC6htLP3mQDOG-qFOrMOML2ZFs1J9hKp9NmxK5py8kOY1QJDqsIDOjVQzLwLP0mEmK_3RrL2kd5gxCBkX6H4IqJKXImugM1OCqm-q08LtZ_brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پست ترامپ علیه نیویورک‌تایمز درباره اخبار جنگ:
تیتر نیویورک‌تایمزِ فاسد و رو به سقوط این است: «بعد از تقریباً چهار ماه جنگ چه چیزی تغییر کرده؟ تحلیلگران می‌گویند نه چندان زیاد.»
واقعاً؟ ارتش آن‌ها از کار افتاده، نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان از بین رفته، سکوهای پرتاب، موشک‌ها، پهپادها و تولید آن‌ها تقریباً نابود شده، دو رده بالای رهبرانشان از میان رفته‌اند، تورمشان به ۲۵۰ درصد رسیده، اقتصادشان درهم شکسته، به سربازانشان حقوق پرداخت نمی‌شود، تنگه هرمز باز است، نفت با شدت در جریان است، و بازار سهام و اشتغال در آمریکا به بالاترین رکوردهای خود رسیده‌اند. این‌هاست آنچه تغییر کرده، ای ترسوهای فاسد و بی‌اخلاق، و حتی بیشتر از این‌ها!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
نحوه پوشش خبرها درباره ایرانِ بسیار ضربه‌خورده و آسیب‌دیده از سوی نیویورک‌تایمزِ فاسد و رو به افول، از طریق «واقعیت‌های» جعلی و ساختگی، به نظر من «خیانت‌آمیز» است. من همه گزارش‌های دروغین و مضحک آن‌ها را به شکایت چندمیلیارددلاری‌ام علیهشان اضافه خواهم کرد. آن‌ها مجرم‌اند!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/76581" target="_blank">📅 00:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HhJphmRMuHpJmdCctfUvMOALgfE6IrWowSjc0wMop9rxORpJ6_7IUia9ZJcAz-DetLF_NduuYqsqhFOyZwO0wKqiyCCuGkSyJ9kW8-yQImNOjNpjHHI5b8HO93DsFWlcDubz7vmx_PsEzoA-4rpYFU6Vw8-9JhUzAEbqE4jAhL1euLZL9H_vv1JeUYROCC4i5MYn_jEU0xJipuDFYRf6LnlLaXrmvSI50ivlToukPRulU2cYo0WkpBYvfk9hla-HYq0yiZyKTwSFXdN8VWLd_KVwtMZx44wCIPWfDZCBvpp1SqDmuysshWW_UbbkMe0kTk12r0oY9TTJ06IH_aoJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LxKG9G_uHni_2dPwUSs3ptMU2cZQbT6ZFrr5UQTsem9eelMLrHfXpFzcD1FKJ7ehc4LpvRWCRZVVD4O1oLT7MZHNWSo7YlCauKaWQebGVIG8zywqE8Ne1pmjYTzCqbC_mfRfjvWLwOKRjS3OaRK0JFZMgTuJ7I6yrgqZR7t2yi-xXa3mWSD-La_AvC1ApQcVU2FbeHjJRYxI635eitoKz4atJ6qwwSXAz1WRib3n-967rfk0-EsxofqCxrDC4pYG6i71Fje2BJpCTH2CkVh7GJD7f3M4ZYZVFgsq1qu1pB63cMKjlCSTOSo81nf5AlGxEUjUIQuV0_0O_Ees-GWM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JCufkJliSfGjFgCA2AFS0CCYGDIdEJv0J8cNCCU1dzCQCcR2ub5uRj_QbegX8Qh2c2PonvdztmQkUzppjWIfnoZJqwBDmOBKMpEVQOu8tIHs7zgWjflRODkss9A541u37yQ2WxSliqv8AHnyRkeunNKjRND_XtsByWnn8jYE56RlNad_J2CB4azaJdw0Tw91k3x_Wk3eYrUaxIFsH1L3hvF5D-W4DaTeCJ-c-Co_zCXv5-nWqunAbcGCx_DQDHmUXYrXCde9No5UlQrK8L4X8md_6JVPW4n3WA6trOyQAqC2MtSg7SF0qqvf213V2AQjjJ2I4N3yQ_eHaCVi3Vn9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mlAHJpkT8A7qPO3BL-C_0FnGMRZ9cb3oEIiV0szMDlNbqZrmV36CrHwN_Dhh42AAfny33qVQ5EbK8kMnAMMjt4ixc9T9Kcw0_rX3veLsx-ZhQeZA2sZLsFi-dOT2gkbGIx10FlKPrCFXviqxU82D1GpKyIiHscjpc2S0yvjm1PI5kRLnltFudnWlK9FD2BM-x-M1fDKoeceZrPK4GyhcrDXa7Ey_6m047A_yKPiw_LbnsGNzBNwEBpuP7aWR2aX2uIkL3Tz_MIRT07C3WjTyftS7RmXhwcGV6L89uWBa5Rab8SLGzxApsjydWOXyIbU1WUMOv00r8rO2Qylkag7WGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qIAUtelXCMcMLr0bA2HywODsasuv-JRBHbUHt_-0OYlRoGFR7akU80QWHsXzNaFoVNuwttXziDZRaz-X47pohua-2FGBgGlJ2L5dqIi3yyAXtM5wUlSAB3ISrkzCBatICDHM6g_YSQPJoPOCvbw1T86QTqcTS1bGfWXFqYqGOTYhfz6y64ZpXKVka1q_oVRbbi0Y8nxhjDXMhdwmfnUuwxGQk0jptVdMFZJGLy-aaQchUEaT4Mj96xe5aDuEAv9UkCzY0cuyuTrvzKuunu8kyiRdQ67oUhoWg9iGEX_fpEYTahQKiyFucuhF6D8zVphVd4XB-5HA_XBRe7KJRxz_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lw3caWH9t8COH8iKi5Xa_c9lSfiwQ8r28rGibx4ThwRMPcvc2hTnrSEvcSTQpiEt8CHcK9zHWnnxnmb_qe9AibzFddNDqntYU14RjDr_y-0jShv45INwsLfWBQhMHLIzuBgOwDoTUtWth1GytlgteS0ni5N4lBDe8Bjoa3yGtb1N8CY9Xmh4NOgGUUVnztiluWSF2vuAShMSbvRU_24293ulxnTPq6UJ005cyvb6MGGKvFdDrGahvwUWTagJK6GdHP-ZprXOsnJ-Zd5nOPf4_yOGBI9cM1rGUhZ29g5EX9O_gOdi6909HsrggmC_JDYa5oCAarQSVoQ-CDkbtsuzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q6omDHWxjj2PZggfaWDQ0bT5AdbnVZRj9LwMcSgzMjNntWwWreeLGwiUXeUwcDJMSdy9rK5__MQqr3RWdGfrWutKnA_53de4JrhukC19ZRoWjkZMFmiG-b-LgJclPCciJuFQd3CHKnL9ATnWPq1lzWnICk6aX2j1WJ93Hm0g8bT8dQm5E0ry1nVGcy6WXQApopKeFuWRr6vtU7VDGphHo6ac7Bx2HbDz3lCvKufShSXtEHSwG9o8o1fjJXrvtxRHTX-byb2XIMoeeVNhmJNkHxasmLpg4UWIbl64AI_IJbkSpGAR_ojHf_MGs5M111tL6tgitIzvkeHzqhuihjuuqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=a2q2lVxtyYC-WsKSE5SgTGsXKfvjQ7V7eo46lKXod2ylrZV0hY8OcYlaUj6DOBbXd7unszNp3FBFJUpQQ3xOuApidSDDTKbHUXE9a8P4wsSiUx6FH8mlaXsKckrTa7KcfLRC712htJ0kaAhtqW6ewJfPLx3Rjy0V3b6Wb8NmLgSGwwB3b1TwK9WqitLQBnX4bf0sOqRu6wxnZAEmy_LqhJo1IfaacGZkxSMVnowj1OSMRd-LxZUmMfEWksvS5RAvexm55L4GQBGXe3REInxdxOHaSesQF14QqE6TasfdxY5lvzOY8A6vIASQHL3QFGmoCrXbw2GwhjZG1ULIC016PA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ecd58481d.mp4?token=a2q2lVxtyYC-WsKSE5SgTGsXKfvjQ7V7eo46lKXod2ylrZV0hY8OcYlaUj6DOBbXd7unszNp3FBFJUpQQ3xOuApidSDDTKbHUXE9a8P4wsSiUx6FH8mlaXsKckrTa7KcfLRC712htJ0kaAhtqW6ewJfPLx3Rjy0V3b6Wb8NmLgSGwwB3b1TwK9WqitLQBnX4bf0sOqRu6wxnZAEmy_LqhJo1IfaacGZkxSMVnowj1OSMRd-LxZUmMfEWksvS5RAvexm55L4GQBGXe3REInxdxOHaSesQF14QqE6TasfdxY5lvzOY8A6vIASQHL3QFGmoCrXbw2GwhjZG1ULIC016PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال ایران در دومین دیدار خود در مرحله گروهی جام جهانی ۲۰۲۶، با ارائه یک نمایش دفاعی، در ورزشگاه سوفای لس‌آنجلس مقابل بلژیک به تساوی بدون گل دست یافت.
مدافع بلژیک در دقیقه ۶۶ از زمین اخراج شد و این تیم ۱۰ نفره به بازی ادامه داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76571" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GFvFbHNt9nfJD4DiRDFzU24632bvuIQfrFsq5McPbCYlxliv9Oem2XK5MaJqTmS3mjnIsDeYFUjHZKLcHITIOu1udO84VDxHZ9-bGdten1yCLeu5Rgv9_EoywrzbKZ1RkniV6zIGNLDzNPRMDgXtpAlEM9-O18WJRun2bOwIQmDBnF3tix5OAaDKmicozCufe5AZsMbnUunFXI0-e6L3uG8VqQvEwdYPdkBIZLvf_iAQJ-BFC_s-N-NZ_ujaHWfSzsTs1gc1rW5E33ud-o7dy3IJEq1pT8JyW7V7E7m7CZgIdWqEa4ZMtFQwlIe5jx_z31tupPIO_5uWOjlb1Dp7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
بعد از آن‌که تریلیون‌ها دلار خرج ناتو کردیم، ایتالیا و نخست‌وزیرش حتی فکرِ درگیر شدن با جمهوری اسلامی ایران و تهدید هسته‌ای بسیار جدی آن را هم نمی‌کنند. دهه‌هاست که ما از آن‌ها دفاع می‌کنیم، اما وقتی پای آزمون به میان می‌آید، آن‌ها برای دفاع از ما و بقیه جهان حاضر نیستند. خوب نیست!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76570" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mK6zmkdi2Kr1M2_QTzUD9iSiNybMdQocClBHnQ0AwJit5zN36E6YTiStfm7ERv5iHNaphUlKO1aDCtKCOmZlQFGObXerkVs_NeNuD553VSD9816FchZYc4yU0-1ZJrwVOsxY2cTBDkn9ZvkOWlXJOHFoZ6hAFjBUZqxJKVFNUFyUjYR6ULeWaVmhbKjYJ_FkR2PgJiQAide1l6G85N3EKQE5RVi9kf342MQREjkOl9jKa5n70QCmliw8qS-o9eqOwDXAHy9SD5wk9wnYOfskKxSYo1cFZ2vrzSLNjyWq2X1_qvl_TXZ-SZ_9t2WDulguwZYP0uLXhmlFALWpJs9csQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ک مقام ایرانی یکشنبه شب ۳۱ خردادماه به خبرگزاری رویترز گفت مذاکرات میان ایران و آمریکا در بورگن‌اشتوک سوئیس متوقف شده، اما پایان نیافته است. این مقام جزئیات بیشتری درباره علت توقف گفت‌وگوها یا زمان از سرگیری آن ارائه نکرد.
این اظهارات در حالی مطرح می‌شود که گزارش‌های متناقضی درباره وضعیت مذاکرات منتشر شده است. پیش‌تر باراک داوید، خبرنگار آکسیوس و کانال ۱۲ اسرائیل، در شبکه اجتماعی اکس به نقل از یک دیپلمات حاضر در مذاکرات نوشت که هیئت ایرانی محل مذاکرات را ترک نکرده و گفت‌وگوها همچنان ادامه دارد. با این حال، خبرگزاری ایرنا دقایقی بعد به نقل از یک مقام هیئت مذاکره‌کننده جمهوری اسلامی گزارش داد که مقام‌های ایرانی پس از دومین دیدار با هیئت قطری، محل مذاکرات را ترک کرده‌اند.
@
VahidOOnLine
خبرگزاری ایرنا، رسانه دولت جمهوری اسلامی، گزارش داد هیات جمهوری اسلامی پس از دیدار با هیات قطری، ساختمان محل مذاکرات در سوئیس را ترک کرده است.
هم‌زمان، یک منبع نزدیک به هیات مذاکره‌کننده جمهوری اسلامی به شبکه سی‌ان‌ان گفت گفت‌وگوهای میان جمهوری اسلامی و آمریکا در سوئیس متوقف شده است، اما پایان نیافته است.
به گفته این منبع، گفت‌وگوهای غیرعلنی همچنان ادامه دارد تا طرف‌ها به میز گفت‌وگو بازگردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/76569" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bafrb3AbiV25XQKgtsrC51ravyNxnvlxdwyI-Pa4EMyQuyY5erQnboLx7AiopZFDsvD6AIRj9ptgJN31-zt78TC3WJ9kuYAfaqapqOsOu5LWeC2AKjnNBBoWK-WsU3rBg64bYdhD0Ks6R2AjUgAzM_ctE4tzWpjpE-3s-k2RBxGks0z7lxArZxL4RXa0kB2VRe4kaFCgtTv4SZxjDbsR8RffYjP-5TsH92ZcJw7mM7pJuvV1ZSaVTMnwVMuEbortwX0UAx4RqM87jJ15tL3o1-8NK0cSaRJbX_73kPFNV0hF-rNQuctFRE_gH2_n9k2iM7NUvY4Ab8CqU_Axrl-5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
"
ادعای فارس و تسنیم به نقل از "یک منبع نزدیک به تیم مذاکره‌کننده"
پیش‌تر در
اکانت قالیباف
همچین توییتی منتشر شده بود:
با خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76568" target="_blank">📅 20:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YWLe1TH1we0dHUKL-BUy4D8aUF7z5easdN80mszjd94Cuwj-czVkp4P8XWlU_42X5IF-8S1hf7soMmOUwnWxIQAR70T3SMh_Y-0QgEYMMAmPHN3yVckSZ5hzCLY-t1Taf0wEE9SqKlVdpl0kufea0Aoh9xXScRdjXzKUbWf8hLh82O7UgSIb1g9kdM3dLE2Jvq43mfDr76U48v9M2tAoMsMtRkvqICAdiTTJgSSYMyeAJmrt0Em7U_onyeW_hdji5xALrwUXoB0YlmSGC3g267e7tuzgOIWnQowuLNFjYPtSvYuxwQz_08e-K6F68t6dkRtqfU9C5IW2BmtPmCeIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در واکنش به اظهارات مسعود پزشکیان، رییس دولت جمهوری اسلامی، درباره ناچار شدن آمریکا به پذیرش تفاهم‌نامه میان دو کشور، هشدار داد که تهران باید در مواضع و رفتار خود تجدیدنظر کند.
ترامپ در گفت‌وگو با فاکس‌نیوز گفت: بهتر است مراقب حرف زدنش باشد. بهتر است رفتارش را اصلاح کند، وگرنه ما کنترل بقیه کشور را هم به دست خواهیم گرفت.
این اظهارات پس از آن مطرح شد که مسعود پزشکیان روز یکشنبه ۳۱ خرداد گفت: آنچه مسلم است از حق غنی‌سازی اورانیوم هرگز کوتاه نخواهیم آمد و طرف مقابل نیز ناچار است آن را بپذیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76567" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z0jxVJQBSo5nm7XXW9CvYWor0LzeTJt25AwDogOGb_k-6880ZxRYEMCjKMVa8yZFKJHsujE0SWogLil_nPZIn1RPF5hx2JYz3aZR9B1aqUVL2IRwvdFZJk467c09mSIoH4U32cPD9cBJLd9k8Hmy7pWwYglOizapvpZsAT2U7BE-3ZrvmvvUA0jiIHkJmFWkitZFkzeYsXj-yJNIYccgKKzPsu9gZ0LNipDN86U1KSA3d55tTosUow7LblMs9kj5iNBRWzn411YzI5m1nISnJntxgjnHS3AwsxUZRNdL5SaH_6GvEoJRLprlD70URvGkwpxSr20kQMqDFMLGcjHCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، اعلام کرد همزمان با برگزاری مذاکرات در سوئیس، به مقام‌های جمهوری اسلامی درباره هرگونه اقدام برای بستن تنگه هرمز هشدار داده است.
او در گفتگو با شبکه فاکس‌نیوز گفت این هشدار شنبه شب به تهران منتقل شده و تاکید کرد در صورت چنین اقدامی، ایران با پیامدهای سنگینی مواجه خواهد شد.
ترامپ همچنین گفت به مقام‌های ایرانی گفته‌ام که اگر تنگه هرمز بسته شود، «دیگر کشوری نخواهند داشت و حتی امکان بازگشت به کشور خود را هم از دست خواهند داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76566" target="_blank">📅 17:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gC7H1hpqwJx8ApICQNnADGmmCDgZBL06GVF10Cw8eC1SZuwEEvWkW1ShlCWp8WtCyAQtFMUT7vvpWRgJXz4Apv4yHGli_Thtu7IiiWg7sscyI3qb2GtuUziuPgM51sN8U-ofIUU1-k6A-Ue5JRiQS7SXObAagBmLTTyHZGvXnp8NhgfaNZNSTtwQje9fDr5Cg4xsJJgXLz_j8tI2e-hqRdJdOPOeQjio7oeMS97f4znGC6aRIubHd_azA4EQdbpsrZz7h3uLVEFq_MzB_K3QB7hE5r0FVTbcMhYeOVizy3Cq6ojrAoly1Uh3LuH9HC3s63SKWfBKcfdscnUA6cO45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران باید فوراً جلوی نیروهای نیابتیِ بسیار پرهزینه‌اش در لبنان را بگیرد تا دیگر دردسر درست نکنند.
اگر این کار را نکنند، دوباره به ایران ضربه‌ای بسیار سنگین خواهیم زد؛ درست مثل هفته گذشته، اما این بار شدیدتر!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76565" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=B5D2YLrH4RI2Q2gkUQCkVMIBKvreqHOeUKzC7d3Ea3VvdMgvZEf6Gw1BnUTJhFY-GbrE2hLriekvktCFpqckSNvs8R4wwhQkUBNEhLzcyE-xAqu7U5EZauYumBA6t5M_t8lferKYeRNvy43cRk0oPOYGKHN0-LxQd8YiE6tOVH__7G-lXBxzKOiO9f3IcUi_G4CzMFYgEEBcUfdvq8qpWny1bg0RwJUWdi-wuw3_IYRcHMWprpck7Qi85bjKABdGP00zvk393dAj4FQ2MtK4FXq7zroZigLu3bUYP8k1GMZNvvAplTKJvLUwFJKUOfQzwbaiN-qKmLzVCCMkJ-bhMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e1422ca156.mp4?token=B5D2YLrH4RI2Q2gkUQCkVMIBKvreqHOeUKzC7d3Ea3VvdMgvZEf6Gw1BnUTJhFY-GbrE2hLriekvktCFpqckSNvs8R4wwhQkUBNEhLzcyE-xAqu7U5EZauYumBA6t5M_t8lferKYeRNvy43cRk0oPOYGKHN0-LxQd8YiE6tOVH__7G-lXBxzKOiO9f3IcUi_G4CzMFYgEEBcUfdvq8qpWny1bg0RwJUWdi-wuw3_IYRcHMWprpck7Qi85bjKABdGP00zvk393dAj4FQ2MtK4FXq7zroZigLu3bUYP8k1GMZNvvAplTKJvLUwFJKUOfQzwbaiN-qKmLzVCCMkJ-bhMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس و عراقچی در یک قاب
خبرگزاری تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده جمهوری اسلامی گزارش داد که هیات آمریکایی و برگزارکنندگان نشست ژنو قصد داشتند پیش از آغاز مذاکرات چندجانبه، مراسم عکس مشترک و صحنه دست دادن میان هیات‌های جمهوری اسلامی و آمریکا برگزار شود اما محمدباقر قالیباف مخالف کرده است.
به گفته این منبع، محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، با این تشریفات مخالفت کرد و اعلام کرد اعضای هیات جمهوری اسلامی در مراسم عکس مشترک با هیات آمریکایی حضور نخواهند داشت.
این منبع افزود در پی مخالفت هیات جمهوری اسلامی و خودداری آن از حضور در این مراسم، پخش مستقیم و برنامه عکس مشترک لغو شد و پس از آن هیات جمهوری اسلامی وارد محل برگزاری مذاکرات شد.
به گفته این منبع، هیات آمریکایی از هیات جمهوری اسلامی پنج دقیقه فرصت خواست تا خبرنگاران محل مذاکرات را ترک کنند. او افزود مراسم پیش از آغاز مذاکرات، بدون حضور هیات جمهوری اسلامی برگزار شد.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز یکشنبه در آغاز مذاکرات ایالات متحده و ایران در سوئیس، این گفت‌وگوها را «تاریخی» خواند و تأکید کرد ایالات متحده آماده است روابط خود با ایران را به شکل بنیادین متحول کند.
ونس در حالی که در کنار نخست‌وزیران پاکستان و قطر ایستاده بود، در اقامتگاه بورگن‌اشتوک در کنار دریاچه لوتسرن گفت: «این یک دیدار تاریخی است. پیش از این هیچوقت رهبران ایران و آمریکا در چنین سطح بالایی با یکدیگر دیدار نکرده‌اند.»
تصاویر و ویدئوهای منتشر شده از محل نشست نشان می‌دهد هنگام حضور معاون رئیس‌جمهور آمریکا در اتاق محل مذاکرات، عباس عراقچی، وزیر خارجه ایران، نیز حضور دارد.
معاون رئیس‌جمهور آمریکا درباره اهداف مذاکره با ایران گفت: «آنچه رئیس‌جمهور از ما خواسته این است که فصل تازه‌ای را آغاز کنیم تا روابط خود با مردم ایران را متحول کنیم و دست دوستی را به سوی آن‌ها دراز کنیم. پیامی که به مردم ایران می‌گوید اگر رهبران شما حاضر باشند از نقش‌آفرینی به عنوان عامل بی‌ثباتی منطقه دست بردارند، و اگر حاضر باشند در بلندمدت از جاه‌طلبی‌های هسته‌ای خود صرف‌نظر کنند، آنگاه ایالات متحده آماده است روابط خود با آن کشور را به شکل بنیادین دگرگون کند.»
او ادامه داد: «این بدون تردید هدف ماست.»
ونس همچنین گفت: «ما تنها در چند ساعت گذشته پیشرفت‌های بزرگی داشته‌ایم و انتظار دارم در ساعت‌های پیش رو نیز پیشرفت‌های بیشتری حاصل شود.»
او با اشاره به اراده ایالات متحده برای «متحول کردن» خاورمیانه، افزود: «ایران در گذشته یکی از عوامل بی‌ثباتی منطقه بوده است. اکنون آینده‌ای را می‌بینیم که در آن همه بتوانند برای پیشبرد صلح و رفاه برای همگان با یکدیگر همکاری کنند.»
@
VahidHeadline
جی‌دی ونس پیش از آغاز مذاکرات اعلام کرد واشینگتن طی ماه‌های اخیر بیش از هر کشور دیگری برای توقف درگیری‌ها در لبنان تلاش کرده و این روند را ادامه خواهد داد.
او با تأکید بر اینکه «صلح آسان نیست» گفت رسیدن به توافق نیازمند تلاش و «بده‌بستان» میان طرف‌هاست و افزود هدف آمریکا تنها صلح با ایران نیست، بلکه دستیابی به ثبات در کل منطقه دنبال می‌شود.
ونس همچنین مذاکرات جاری را «آغاز یک گفتگوی فنی» توصیف کرد که قرار نیست همه اختلافات را یک‌باره حل کند، اما فرصتی فراهم می‌کند تا طرف‌ها برای نخستین‌بار درباره مسائل اصلی به‌صورت مستقیم گفتگو کنند.
به گفته او، حضور رهبران سیاسی برای تعیین چارچوب مذاکرات و حمایت از تیم‌های فنی است و با وجود چالش‌های پیش‌رو، طرف‌ها با انگیزه برای ادامه مسیر آماده هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76564" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=X0xuv3Gco0GFI5yZKbjDsqn9YgrAK1fCdAgLuFC0Fi6DLpbXUXI8SqrTgic7jsu9WtUngh7FwCKVZ0am2CNe1yXcEyzeVxJI9fgMqxUZzjHqJsx6HsFpsgqbDO94jO2ns0-o_vLXudNs3wSlP1dPQh-BBuJs14O3CzFFQoxLx4vYdZRjEHeoQN79NJ37O9WZU4QOWinVKFhg-L927MtxG9h6PCNdR9JgQYmQ4RGgtjzMfF2rU0AMYYslQlMyPvo0-ZjhQRwpdbZKGDpLg0yb0wXCAtGVWpo-Fq0V8w_GXxWu6hxz291it_uKMDCQ9orCSRvYIxW31zd5FjYa2FhWhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/12a29862bf.mp4?token=X0xuv3Gco0GFI5yZKbjDsqn9YgrAK1fCdAgLuFC0Fi6DLpbXUXI8SqrTgic7jsu9WtUngh7FwCKVZ0am2CNe1yXcEyzeVxJI9fgMqxUZzjHqJsx6HsFpsgqbDO94jO2ns0-o_vLXudNs3wSlP1dPQh-BBuJs14O3CzFFQoxLx4vYdZRjEHeoQN79NJ37O9WZU4QOWinVKFhg-L927MtxG9h6PCNdR9JgQYmQ4RGgtjzMfF2rU0AMYYslQlMyPvo0-ZjhQRwpdbZKGDpLg0yb0wXCAtGVWpo-Fq0V8w_GXxWu6hxz291it_uKMDCQ9orCSRvYIxW31zd5FjYa2FhWhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، همزمان با برگزاری مذاکرات مستقیم میان ایران و آمریکا در سوئیس، گفت همه نظامیان در شورای امنیت ملی موافق مذاکره بوده‌اند.
او در جلسه‌ای به مناسبت تشکیل بسیج اساتید در دانشگاه تهران، در میان صدای اعتراض عده‌ای از حاضران گفت: «همه امضا کرده‌اند که این راه را باید برویم. حالا هر کسی می‌خواهد تفرقه ایجاد کند، این گوی و این میدان.»
او با اشاره به نظر فرماندهان نظامی در شورای امنیت ملی گفت: «فرمانده قرارگاه [خاتم الانبیاء]، فرمانده ارتش و سپاه، و نهادهای امنیتی همه بودند و همه یک حرف زدند و همه متحد بودند و همه آن چیزی را که می‌خواستیم عمل کنیم را امضا کردند.»
این سخنان پزشکیان در پی افزایش انتقاد اصولگرایان تندرو از دولت در پی انتشار نامه منسوب به مجتبی خامنه‌ای صورت می‌گیرد.
آقای پزشکیان همچنین با تاکید بر نقش دولت در حمایت از نظامیان در دوران جنگ گفت: «۲۰ میلیون بشکه نفت که مال دولت بود را به هوافضای سپاه دادیم. ارزهایی که داشتیم را به این عزیزان دادیم.»
@
VahidHeadline
مسعود پزشکیان، رییس‌ دولت جمهوری اسلامی، گفت نگرانی اصلی او این است که دولت نتواند رضایت مردم را جلب کند و نارضایتی‌ها به اعتراض‌های خیابانی منجر شود.
پزشکیان گفت: «از آنچه می‌ترسم این است که نتوانیم به مردم به درستی خدمت بدهیم، ناراضی شوند و به خیابان بیایند و اعتراض کنند. آن وقت ابهت ما فرو می‌ریزد.»
او افزود مهم‌ترین قدرت جمهوری اسلامی، وحدت مردم است و مسئولان نباید اجازه دهند کمبودها، کسری‌ها و نواقص باعث نارضایتی مردم شود. به گفته پزشکیان، بروز چنین وضعیتی موجب «خوشحالی دشمنان» خواهد شد.
@
VahidOOnLine
بعضی از جملات پزشکیان به انتخاب خبرگزاری دانشجو، وابسته بسیج:
🔸
اظهارات عجیب پزشکیان: من از این میترسم که نتوانیم مردم راضی کنیم و به خیابان بیایند اعتراض کنند
🔸
تمام مفاد تفاهم‌نامه امضا شده بین ایران و آمریکا به نفع ماست و دستاوردهای این گفت‌وگو و مذاکره عیان خواهد بود.
🔸
ترامپی که ما را از انجام بسیاری از کارها منع ‌می‌کرد، در سخنرانی اخیر خود تمام آن‌ها را حق مردم و ملت دانست.
🔸
۶ میلیارد دلار پول ما در قطر برخواهد گشت.نتانیاهو اولین ناراضی از مذاکرات است.
🔸
تنها نکته آمریکا این است که ما بمب اتم نداشته باشیم، این موردی است که رهبر شهید هم بارها فرمودند ما بمب اتم نمی‌خواهیم. آمریکا گفت همین را بنویس و امضا کن، ما هم امضا کردیم.
🔸
شورای عالی امنیت ملی در وحدت و انسجام تصمیم گرفت؛ همه یک حرف زدند و متحد بودند
🔸
مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده/ آنها پذیرفتند که حق ملت ایران را نمی‌توانند نادیده بگیرند/ قاعده عوض شده است
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76562" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8PTtHdkaDZee-pVy01OqfkuO30e3FfdPrXTCcgcjZ9Pr6XpCwNXvAKgWEX1QbW8PIfDc5z3IxDbYoBK9xHQu6QpiOSe9xk6HaVk9fzZL0x2AdHlVOMKh_RyTxo5HhoOsyk3fowqIPJ9g7hhCMJ7ly_2nzOmZzXzSP1oAYIYDELW-nA2W5QIQ63lpnqpvaeUyiAo2FLYlC5D3kWK5cduMc1skwykU7pifGgZ6wX-7_q5nyWSig4ryOpGr227e_HtEZpSjGYmju8NgaWdZ4yVg2QdKIV81klPn0TZFDR3hJ15ptdSlKC6Oeo88V3bS0lXiM0qWqXI9AYveb8683EstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از دو منبع منطقه‌ای آگاه گزارش داده است که آمریکا می‌خواهد نخستین دور گفت‌وگوها با ایران با دعوت تهران از بازرسان سازمان ملل برای بازدید از تاسیسات هسته‌ای ایران پایان یابد.
به گفته این منابع، این تاسیسات پیش‌تر هدف حملات آمریکا و اسرائیل قرار گرفته‌اند و آخرین بازدید بازرسان از آنها پیش از جنگ قبلی، در ژوئن ۲۰۲۵، انجام شده بود.
اکسیوس می‌گوید: «آمریکا در مقابل آماده است به ایران اجازه دهد به بخشی از دارایی‌های مسدودشده خود دسترسی پیدا کند؛ از جمله حسابی به ارزش شش میلیارد دلار در قطر.»
بر اساس این گزارش، ایران می‌تواند از این پول برای خرید کالاهای بشردوستانه استفاده کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/76561" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoYTlcX83-Bbt3YfHFMr73-_W7RiDZzOOzVFhlDsvGVRx6k_DdAlU3CYX6vUo8pyJ3MwnpFk059sXlwf9rRaTr_RxjxViXucOShITu9la0Bylh_uQr6JrdNZAXaGjMYYZU9WCC3l5m8WLZl9nGxiZ0Wg2IBP43bmFzr0e03BDojbT5QbBOcdlFYtP5TeaTxfZ3gWA-wVoMqgO2q6Xuwje9Q4x4fI6c3UM8KdDkMbS2qRvp0oLjknZBz42cH-8NXc6xM67_bL_VreDw09MuPeXk_yuUCcPMsXJlBOJHds-RIIlVbjrN_fYJPhb1hBwAI21Ugcth1VBpN5uR2pe8p31g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام‌های بهداشتی در غزه می‌گویند که دست‌کم ۱۰ فلسطینی در حملات هوایی و تیراندازی نیروهای اسرائیلی در چند حمله جداگانه کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76560" target="_blank">📅 16:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCP1hsPvY9p39dXPBWUVnNbLlf6jFdIgKhI2vVORMAN8tGAF6La6TYgexOrI-ByiBwVLtnNn-K7VDuUhZ5HyQOi1ZN5Zuvq160cz2GKoY0dAjIx3oYWDDO1KE8edDrOcBjl2F7vvhH07fv1V25jM46gzqggYEt_6l78nrvOG4c4brEjuJEiycdQp4ue8KHU8l9JidAWJ2OdjAjKi4ObjVil4wwKGN28UAXzx-G8eKEQ2IG2TmR-Veb_ye5yY_0zG11VgDHw61sLK5Zc4H8Tvsa_UpO6AzGb-_S_p5ICZM0r0y1lU8zHrna9SqiaT_yJrkSn405PABkFs0XoaytvT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از هزار دانشجو و فارغ‌التحصیل دانشگاه صنعتی شریف با امضای نامه‌ای سرگشاده خطاب به محمدرضا تجریشی، رییس این دانشگاه، نسبت به آنچه «تشدید فضای امنیتی» و گسترش برخوردهای انضباطی با دانشجویان خوانده‌اند اعتراض کردند و خواستار پاسخگویی مدیریت دانشگاه شدند.
انجمن اسلامی دانشجویان دانشگاه صنعتی شریف تاکید کرد که بیش از هزار نفر این نامه را امضا کرده‌اند. انتشار این نامه یک روز پس از رسانه‌ای شدن صدور احکام اخراج برای شماری از دانشجویان شریف صورت گرفت.
امضاکنندگان در این نامه نوشته‌اند که در ماه‌های اخیر دست‌کم ۳۰ پرونده در کمیته انضباطی دانشگاه تشکیل شده و ۱۳ دانشجو با احکام بدوی تعلیق یا اخراج مواجه شده‌اند. به گفته آنان، احکام سه دانشجو نیز در مرحله تجدیدنظر تایید شده است.
نویسندگان نامه تأکید کرده‌اند که آنچه در دانشگاه می‌گذرد، ادامه «روندی نگران‌کننده» است که به دلیل نبود واکنش مؤثر از سوی مدیریت دانشگاه، هر روز ابعاد گسترده‌تری پیدا می‌کند. آنها همچنین نسبت به افزایش سرخوردگی دانشجویان، گسترش بی‌اعتمادی در فضای دانشگاه و آسیب دیدن اعتبار علمی دانشگاه صنعتی شریف هشدار داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76559" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oGvU8sesAoL6r6rtyHZjLfKbWKW03Valh1f4iSvEWqPW-DmI_9bORkgFN8IwkliswnURZBuEsY7umbE4wWsx3eOiIQ_xMwd7ZLsVfZlNWGH_6g2MlmC7tImO_CxVjZEOLKTpl3L89NdOH6lMT5Sl0A44lVSZ60b4pWpIjBrw5UZQKLZfPfm7mpL7AFzveKLpb8XpuOVDqCVGezYPyCsqNmNM3yuMhw8gEaduVOd80Fp9S52V-xX2JlPFciFq4f3OVJXH6QUbC7xGIvghZKMgT1BrkE_TKMyufplyFqGaCpg3KBOC8zu1r3y4H6Szf6Hp-KETBFT5-pMQY6Zfa3Up6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5K72eKy7vyMg3jnd9FZDoYNXXH7vI7fAEwRHxl7-NCWGQ7sh8BHryHrZjUVqCmJdg09JFBvJx_AiLY6K8wWb4YkvkXznhZdDRg6asP0uXIE9Jx9xfjefXPia5d-sj0Kpcwup7mg_vtGpLMfmlJTaDJV6i60VTcaYk4Re_3jqkYI30SG3n4RNFmB2PasVv3RqaR_4uDUW6BrOElwIZX1ymZoXqoopkutna4lX8mmOsNDoHiBCjMzD_WS8Ae8QqF4x_3QPcs4jGbw_uz-kl5pobnr9cRCISMo554pmW8dV2Vh5b7ewFIyCMpQr8GX5ouZWNhF9OAia5Aj3gYZfsGqoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
جواد علیکردی، وکیل دادگستری زندانی، توسط شعبه اول دادگاه انقلاب مشهد به ۱۸ سال حبس، انفصال دائم از حرفه وکالت، دو سال تبعید به سراوان و دو سال منع خروج از کشور محکوم شد. جلسه رسیدگی به اتهامات او در ۲۰ خرداد ۱۴۰۵ برگزار شده بود.
🔸
به گزارش خبرگزاری هرانا، آقای علیکردی از بابت اتهام «اجتماع و تبانی برای اقدام علیه امنیت ملی» به پنج سال حبس و از بابت اتهام «فعالیت تبلیغی برخلاف امنیت ملی» به ۱۳ سال حبس محکوم شده است. پرونده او پیش‌تر در شعبه ۹۰۲ دادسرای مشهد مورد رسیدگی قرار گرفته و پس از صدور کیفرخواست به دادگاه انقلاب ارجاع شده بود.
🔸
جواد علیکردی در ۲۱ آذر ۱۴۰۴ توسط نیروهای امنیتی در مشهد بازداشت شد. او ابتدا به یکی از بازداشتگاه‌های امنیتی منتقل و سپس به زندان وکیل‌آباد مشهد انتقال یافت.
🔸
آقای علیکردی برادر خسرو علیکردی، وکیل دادگستری و مدافع حقوق بشر است که در آذر ۱۴۰۴ به شکل مشکوکی درگذشت. وی پیش‌تر نیز در پرونده‌ای جداگانه با اتهامات سیاسی و امنیتی محکوم شده بود که اجرای بخشی از احکام صادره
علیه او به حالت تعلیق درآمده بود.
@IranRights</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76556" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QZRH7OsdKRL6T0bfujQ7w2O_-Ub-wCIOR_TP20-TAJJ68sShXOG1qEPtRtyd5-gptWc5gxuRZYBPgeDedwzeZc4sIpPBPBbAWDTGZQKi5tKW9PunA2Z11bc7I5DyeCE20LG83gp4K7Hhnr7fI2gzMEfENYN_l97KD95Pzhkgdzaun9n1zi_b0lDjCiGyj-YZD10f-fOOEvYg8KqYt5HKstnV99zQw14r2OH7Vjs6Hw2utcrm55f5L3B-ZpCF8MSR1o7uDuHl_xl9lUyxcDRt9DuBOa0JOb5cmUhhbftL5k4dGlSaOl5QcxrmL3siyCid0j4-p_QA5wnKcHdeYJmK9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هیچ‌گونه عوارضی در تنگه هرمز وجود نخواهد داشت مگر به نفع آمریکا
ترجمه ماشین:
در دوره ۶۰ روزه آتش‌بس، در تنگه هرمز
هیچ عوارضی در کار نخواهد بود
،
و پس از پایان دوره ۶۰ روزه نیز
هیچ عوارضی پرداخت نخواهد شد
؛
مگر آن‌که، در صورت تکمیل نشدن توافق، این عوارض
از سوی ایالات متحده و به نفع آمریکا
وضع شود؛
آن هم بابت خدماتی که این کشور به عنوان «فرشته نگهبان» کشورهای خاورمیانه ارائه داده، برای جبران هزینه‌های گذشته، حال و آینده.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/76555" target="_blank">📅 22:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLzgxZ2RP4V1W4ouVtTFTt2ZaPW0ZZNdCuccYUDd7oiGwEh4UOQ59o1oTqi27tnbSZRIlUwXYFgDNazwg2dPz6JxjOUoZ9MHCcAw7E9xJuB5XjftN6KGgHrNGqf5VehYzGyScy26zI7I6Naj5G5YHnErBnu1Vbvjo05nXYNFcO-E9SLsq6CMEsRqpletnT7jOhLBaC7ktawzM_zIfvAaZlKuq9CHpriTiGcdlLkpouXNbzuJAGMQc3XOr6wd46boElu35ZuF-oe-ziIlqcICSX8SDWCdcxcZtuQmFJm50CdHn078zVHi-8Cx9acQeJ35UgoxZYTOarB9GvKMlYA5Rlzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35770a9ed5.mp4?token=brZ1TSvklYTiiP7f-7G9xLD-7HodOQJEZR3z7iqlIStGKPPg9iHpk5-Yg_Q-iPOzyHTahs0_DlZAK-U4gGAG-7wOdpaB0VPXftMIpldlOUMEKv8yNmO-a6dsyO8aU6qzT8XJBU21atkYVtGTSLwVDWY7O-GJ-gzhgCVeN1tV_vQRZ13CYGn_mD0WqdE8ZZ5gSPeut23hA_6A5sBEvFkeMx-Ss8DC7cIw_8wmoLStUE6ZWhvGzNnuQ_zGKcHINuyKxoswbx4lQITRPPkct2dYq4aChsOMOTk_-QgNfxi4UW0ihsmHNGseVMfFOa-6msVYbabxvE5p8Yc1T0gK5iPJLzgxZ2RP4V1W4ouVtTFTt2ZaPW0ZZNdCuccYUDd7oiGwEh4UOQ59o1oTqi27tnbSZRIlUwXYFgDNazwg2dPz6JxjOUoZ9MHCcAw7E9xJuB5XjftN6KGgHrNGqf5VehYzGyScy26zI7I6Naj5G5YHnErBnu1Vbvjo05nXYNFcO-E9SLsq6CMEsRqpletnT7jOhLBaC7ktawzM_zIfvAaZlKuq9CHpriTiGcdlLkpouXNbzuJAGMQc3XOr6wd46boElu35ZuF-oe-ziIlqcICSX8SDWCdcxcZtuQmFJm50CdHn078zVHi-8Cx9acQeJ35UgoxZYTOarB9GvKMlYA5Rlzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبویان: مجتبی خامنه‌ای نامه داده بود که چرا شروط من رو در مذاکره رعایت نکردید؟
07:20
صدا و سیما: افشای مکاتبات مجتبی خامنه‌ای از سوی نبویان در شبکه خبر پیگرد قضایی دارد
صداوسیمای جمهوری اسلامی ایران اظهارات محمود نبویان، نایب‌رئیس کمیسیون امنیت ملی مجلس، در شبکه خبر پیرامون مذاکرات پیش رو بین ایران و آمریکا را «مصداق تخلف قانونی و مستوجب پیگرد قضایی» عنوان و اعلام کرد «مدیرکل مربوطهٔ این شبکه استعفا کرده است».
محمود نبویان، که به جناح تندرو موسوم به «پایداری» تعلق دارد، روز شنبه ۳۰ خرداد با خواندن بخش‌هایی از متن‌هایی که گفت مکاتبات مجتبی خامنه‌ای با هیئت مذاکره‌کننده است، مدعی شد رهبر جمهوری اسلامی در مراحل مختلف با روند مذاکرات و بندهای متن‌های گوناگون مرتبط با مذاکرات مخالف بوده است.
این گفت‌وگو پیش از آن‌که نبویان به متن نهایی تفاهم‌نامه برسد، قطع شد و موجی از واکنش‌ها را در میان دیگر چهره‌ها و فعالان رسانه‌ای جمهوری اسلامی در پی داشت.
صداوسیما در بیانیهٔ خود اعلام کرد نبویان در اظهاراتش «اشارهٔ ناقص و مخدوش به برخی اسناد دارای طبقه‌بندی» داشته و سعید آجورلو، عضو تیم رسانه‌ای هیئت مذاکره‌کننده و از چهره‌های نزدیک محمدباقر قالیباف، نیز او را به «تحریف عمدی متون» با هدف «فرار از پاسخگویی درباره ادعاهای نادرست قبلی» متهم کرد.
محمود نبویان، ۲۳ خرداد ماه، در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا، در یک برنامهٔ زنده در یک خبرگزاری نزدیک به سپاه، متنی را که مدعی بود تفاهم‌نامهٔ ایران و آمریکا است، روخوانی و از برخی بندهای آن به‌شدت انتقاد کرده بود.
نبویان یکی از اعضای گروهی بود که پس از اعلام آتش‌بس جنگ ۴۰ روزه، همراه هیئت مذاکره‌کنندهٔ با آمریکا به اسلام‌آباد رفته بود.
مجتبی خامنه‌ای، که پس از اعلام رهبری هنوز هیچ صدا و تصویری از او منتشر نشده، پس از امضای تفاهم‌نامه توسط رؤسای جمهور ایران و آمریکا در پیامی مکتوب اعلام کرد «نظر دیگری» داشته اما «با تعهدی» که پزشکیان به او داده، مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا گذاشته است.
@
VahidHeadline
حمید رسایی با انتشار ویدیوی بالا نوشت:
نبویان در آنتن زنده شبکه خبر، در حال تشریح جزئیات نامه‌های رد و بدل‌شده میان رهبر معظم انقلاب و شورای عالی امنیت ملی بود که پخش برنامه به بهانه میان‌برنامه به صورت کامل متوقف شد!
ما که از یادداشت‌های آن امام شهید در این باره اطلاع پیدا نکردیم ولی گوشه‌ای از یادداشت‌های امام حاضر توسط آقای نبویان در حال پخش از سیما بود مانع آن شدند!
صدا و سیما:
🔹
روابط عمومی معاونت سیاسی صداوسیما: به استحضار مخاطبان محترم شبکه خبر می‌رساند اظهارات یک نماینده مجلس دعوت‌شده به برنامه امروز زنده این شبکه و اشاره ناقص و مخدوش وی به برخی اسناد دارای طبقه‌بندی و مکاتبات مسئولان عالی کشور، مصداق تخلف قانونی و مستوجب پیگرد قضایی است و سازمان صداوسیما پیگیری‌های لازم را در این خصوص در دستور کار قرار می‌دهد.
🔹
شبکه خبر ضمن ابراز تاسف بابت بی‌توجهی مهمان مذکور به قواعد اخلاقی و الزامات آنتن زنده، به اطلاع می‌رساند مدیریت این شبکه ضمن پذیرش استعفای مدیرکل مربوطه، برخوردهای انضباطی لازم را به دلیل بی‌توجهی به الزامات برنامه‌های زنده و سهل‌انگاری در مدیریت حرفه‌ای به عمل خواهد آورد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76554" target="_blank">📅 21:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fE2bF4-eyO1R-syvkZT4NMZHF8uqZ1g6tDZisbB56g_kYyfoFJPsoDRtd8VZYZrV6QuHl5WY4CBAq9oa94nn-1NT9N0iwQraHkNRblTOMMI65OvkcBaV1oB3ScdqBFzYV16Nnix1Y-z1xk7eDKsIRsJQDZ-trR3zeHomxI_WHYPRCklIP50pCN3KTu8jwIgYUydytJPnFVRLSOTzkItJ9C-WSDfrdSn0QqruNlvvCXxb33DoNUd4xSSzYNB-vbKlYbfRSU5_qxng5SoYlMsi8hPsijw5oVSfDetEVtNXuzNkc-4h0bOFx4h93R6uYRl0_PNA5vqFp7P-AQRfj0gf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VCWBZ0EH9v8ODR8d7pYA3LYKAliI7XwkxUu62FkCu6prHOO-J5xGvixL6wvC1wEo-7BhKWqNLLCPRQZgGRbyks__myQbasesCn5Gu5Nx-cP9iHKbEWumyHVXyfO9BOy9Zpls1Oy2qch0Eut2H6r4XKIBrsW2AAU2NFjJAtqsyr9e2PTbU_bOUipYNFsHTyUDcjWt185BQEfrZimPjMRRWy361IoNzJkUQB1PVVSiB4E25UWc5GmLktgBlYN7o1MVx3k4oqgf65AOVJOrMb6rmnnlLN548XVAYo2LS2to6GE11rG8oWx3oUs4JLBQCL_0WjrCv8HvVr5Qj7f_uMIzkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ در تروث سوشال نوشت: محبوبیت ملونی در ایتالیا به شدت کاهش یافته، شاید به این دلیل که او و ناتو در جریان ماموریت جلوگیری از دستیابی ایران به سلاح هسته‌ای، به ایالات متحده پشت کردند.
ایتالیا حتی اجازه استفاده از باندهای پروازی خود را به ما نداد که یک مانع لوجستیکی بزرگ بود؛ آن هم در حالی که آمریکا سالانه صدها میلیارد دلار برای محافظت از ایتالیا و دیگر متحدان ناتو هزینه می‌کند.
رئیس‌جمهوری آمریکا در پایان با لحنی تحقیرآمیز تاکید کرد: اکنون که ایالات متحده ایران را از نظر نظامی شکست داده، او می‌خواهد برای بالا بردن آمار محبوبیتش دوباره با ما رفیق شود؛ اما نه، ممنون!
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، با انتشار بیانیه‌ای تند در صفحه اینستاگرام خود، به هجمه‌های اخیر دونالد ترامپ پاسخ داد و حملات کلامی رئیس‌جمهوری آمریکا را «بی‌دلیل و بی‌معنی» خواند.
ملونی در این پیام خطاب به ترامپ نوشت: «محبوبیت من به هیچ‌وجه به رابطه با شما بستگی ندارد و دوستی با شما نیز کمکی به آن نکرده است. محبوبیت من حاصل توانایی‌ام در دفاع از منافع ملی ایتالیاست؛ یعنی همان کاری که همواره انجام داده‌ام.»
نخست‌وزیر ایتالیا همچنین با دفاع از تصمیم خود در جریان جنگ اخیر و عدم اجازه به آمریکا برای استفاده از پایگاه‌های نظامی این کشور، افزود: «نحوه استفاده از پایگاه‌های نظامی آمریکا در خاک ما، تابع توافق‌نامه‌های متقابلی است که ما همیشه به آن‌ها احترام گذاشته‌ایم. تا زمانی که من نخست‌وزیر هستم، این توافقات نباید نقض شوند؛ چرا که ایتالیا یک کشور مستقل و دارای حق حاکمیت باقی می‌ماند.»
ملونی در پایان نوشت: «در هر صورت، میزان محبوبیت من اصلا به شما مربوط نیست. پیشنهاد می‌کنم شما روی محبوبیت خودتان تمرکز کنید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76552" target="_blank">📅 19:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rUqYpmcmEb0MZ8MI6c0ap9xqvywMM8yTCQKqIHFMCx4nX-_C5fDi9433tt7UYV72nmWvAU0r74Xe6fFG00f9PwYUA6Myl9stXZlhoEAKl6P5mvLENl1Ye-YGLBT64xIh9rZJFV9HILrz1dIaiEvPQd9V2-MLscZ--78d4kuVZ57JlVCQ0j1JEig8vbMcCXxp3-D9TCNqb-8wEPaIk-XFMK0b-pDlBGw2f_WfUplhiM9ORQvEVwfbbX9jgwPRPoSVdek04397C10xtMNz1cmFWtCC6mwPp201yVwDnLgSCY-7gyBeigqK0ycEcndAf6J1XOa3rxovAEqWhsa8ISITqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که هیات مذاکره‌کننده جمهوری اسلامی به ریاست محمدباقر قالیباف و با حضور عباس عراقچی، عازم سوئیس شده است.
بر اساس این گزارش، عبدالناصر همتی، رییس کل بانک مرکزی و علی باقری کنی، معاون بین‌الملل دبیرخانه شورای عالی امنیت ملی نیز در این سفر حضور خواهند داشت.
همچنین کاظم غریب‌آبادی، معاون و اسماعیل بقائی، سخنگوری وزارت خارجه و حمید بورد، معاون وزیر نفت نیز این افراد را همراهی می‌کنند.
پیش‌تر وزارت خارجه پاستان اعلام کرد که مذاکرات فنی میان جمهوری اسلامی و آمریکا، یکشنبه در سوئیس آغاز خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76551" target="_blank">📅 18:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tE7U-QCF2oBdU82kgkBjv3XUMvWhWezz3JMJVemjtt2FbbGVswUDm_shJ_8IxAS3R_cpZi9XZwlXDbuyeh7vs1ZBrNpAqKdpG2trBEovP_5MRgRd4vFhi1NFR1TapLRvNOLLhlxd3cQV5YBD1W9Z1nHqk_9tyIqhkjl9v8vVD_Hs2OZzfC5kshZiMXhNfqj0ZZhZHThXuTYgbDCj100LBbgipGb-2CzSfbseqae-LH-k9IkguQHr4EU_gd3eqsguyyMt8hr0vKmNTGTCDc7szKLoKFzzKzKJIxDobqreOy912CjutFBoVo58P1yLe4270n3a8I-eJc5tp1UAK8vglQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: تنگه هرمز باز است
پست اکانت فرماندهی مرکزی ایالات متحده،
ترجمه ماشین:
عبور کشتی‌های تجاری از تنگه باز هرمز
تامپا، فلوریدا — تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت؛ همزمان نیروهای آمریکایی به عملیات خود در منطقه کلی ادامه دادند تا از آزادی کشتیرانی حمایت کنند.
امروز عبور امن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری از آن عبور کردند؛ کشتی‌هایی که حجم زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل کردند.
مرکز مشترک اطلاعات دریایی این هفته اطلاعیه‌ای صادر کرد و در آن عبور امن همه کشتی‌ها را در یک مسیر تعیین‌شده تأیید کرد؛ مسیری که از ادعاهای خودسرانه درباره الزامات یا هرگونه مانع، آزاد است. جزئیات مربوط به عبور امن را می‌توان در اینجا دید:
ukmto.org
نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیارند تا اطمینان حاصل کنند که همه جنبه‌های توافق با ایران رعایت، اجرا و به‌طور کامل برقرار و لازم‌الاجرا باقی می‌ماند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76550" target="_blank">📅 18:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=UbokxgjvoQrS3HUsqzAV5JDMWNUKzWgNDOGJiUtSfp5d-vLY_Ibs7oi2A9TFDYGIQsmEVTZw4Am94YDVEASYD-f_kPOL_a9pje1R81out0nqpbIj4uBo7OJj9CcRsD8Pcsv63gwdA9mi64WT8ozxLGya90WiaW2U1h9z3ZS-vIiXvGmqgURFvO9zTY6FTdDxhR5FVigptk2TJ4RNSpp8HizTyKvN0zTMVoMnxSRrr-ruRSorJNWqA7viqYSrLD2NiD1oASqnumXOxEhaefIym-67MOdFgrxSSrV-fyf5_MnclWCPQjgoeAxb8o8_QuRO8OB62f92DJ4tpe1Q5VpD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31b632aa9b.mp4?token=UbokxgjvoQrS3HUsqzAV5JDMWNUKzWgNDOGJiUtSfp5d-vLY_Ibs7oi2A9TFDYGIQsmEVTZw4Am94YDVEASYD-f_kPOL_a9pje1R81out0nqpbIj4uBo7OJj9CcRsD8Pcsv63gwdA9mi64WT8ozxLGya90WiaW2U1h9z3ZS-vIiXvGmqgURFvO9zTY6FTdDxhR5FVigptk2TJ4RNSpp8HizTyKvN0zTMVoMnxSRrr-ruRSorJNWqA7viqYSrLD2NiD1oASqnumXOxEhaefIym-67MOdFgrxSSrV-fyf5_MnclWCPQjgoeAxb8o8_QuRO8OB62f92DJ4tpe1Q5VpD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی پربازدید شده که مادر مانی صفرپور، جوان کشته‌شده در اعتراضات دی‌ماه، را در حال سوگواری برای فرزندش در کنار یک دستۀ عزاداری نشان می‌دهد.
عکس پسرش را بالای دست گرفته و می‌گوید «پسرم، پسرم».
مانی صفر‌پور، جوان ۱۸ سالۀ لاهیجانی، ۱۸ دی‌ماه ۱۴۰۴ با شلیک نیروهای حکومتی در محلۀ سلسبیل تهران کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76548" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76547">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sre3AbBpD3rkEWNe0Nyhq9rw4RITm4ANUAB69oniO5fGuvGJhijpNpy-_ShJbQgsPAx4_YZFDoDYrMv2kak78gO7vb2ErzCDwwqHhAChiEoPeibCr3kTuPC7_fTJNnIVY6h1ZnuySkIhmE-dw4Xgd1ynseDAShtUAd0308feHU7A_Uacu7vnRKuNP2HIhL3QhHqLZTQW3A-5njaCcRlTx5cgavXdMn6MY2i6BgrP8yoFC_M3M_yWRb_QzGhTO6mOr0RHjhfieqD8ILShM09HVCRr8iDOMqXCfsmqL1AHqH-iJljQB4YV9-TRNR8HfT05yb0OI6q-NMry4x2vAaxZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران اعلام کرد تنگه هرمز در واکنش به «نقض تعهدات امریکا در اجرای آتش‌بس» و «حملات اسرائیل در لبنان»، به روی همه شناورها بسته شد.
نیروی دریایی سپاه همچنین از شناورها خواست به تنگه هرمز نزدیک نشوند و هشدار داد در غیر این صورت، امنیت آن‌ها به خطر خواهد افتاد.
قرارگاه مرکزی خاتم‌الانبیا، واحدی از سپاه پاسداران هم اعلام کرد تنگه هرمز به‌دلیل «بدعهدی و پیمان‌شکنی» امریکا نسبت به‌عدم اجرای بند اول تفاهم‌نامه، به روی تردد کشتی‌ها بسته شده است.
قرارگاه مرکزی خاتم‌الانبیا روز شنبه اضافه کرد این گام اول «پاسخ به عهدشکنی دشمن» است و در صورت ادامه این وضعیت، گام‌های بعدی برای «پایبند کردن دشمن به اجرای تعهدات»، برنامه‌ریزی و اقدام خواهد شد.
خبرگزاری فارس، وابسته به سپاه پاسداران به نقل از یک منبع نظامی در نیروی دریایی سپاه، عصر شنبه اعلام کرد که تنگه هرمز از دقایقی پیش به‌طور کامل بسته شده است.
حملات اسرائیل به جنوب لبنان در روز شنبه دست‌کم ۱۰ کشته بر جا گذاشته است. اسرائیل اعلام کرد این حملات در واکنش به پرتاب گلوله‌هایی از سوی حزب‌الله، گروه مورد حمایت جمهوری اسلامی، انجام شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76547" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EK_PirSaNlTavn0xk8OPC0AIpCzUlRb6mJy-dBDarDTDzxGDpbiZ0fsJNAGcMQFC0r-q4mwT1_PdRVEB1umj-lls38P_7TEsRhOuMAwtqSmCdl-4KPLdCtxoUDemNqljdDV-gkgY_SRGUAjrAL7Wze0i8iT8enEZMLCLq6MUqPQkSYO7F5DQsvSGNOT_z895V4qNfjo1KajGpvnEBF9U3PCLMUyKsgap5B1bdvDErt_id9RtdBUL7XFpv_hQrBva1FEFt_Ab463XUSXvUpqFVIrsqkQmyT9BYbTlOR-h24TVeOfil5zamtzYK2fly0IIYqm1LflxHuWBTSw9M0NLtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، روز شنبه ۳۰ خرداد در گفتگو با فاکس‌نیوز اعلام کرد که استیو ویتکاف، فرستاده ویژه ترامپ و جرد کوشنر، داماد او، «چند ساعتی است» که در سوئیس حضور دارند و مشغول بررسی «برخی از ابعاد فنی این مذاکرات» با ایران هستند. به گفته ونس، کوشنر و ویتکاف در گزارش‌های خود تاکید کرده‌اند که «امور به خوبی پیش می‌رود.»
ونس همچنین از احتمال ورود میانجی‌های قطری و پاکستانی به سوئیس برای پیوستن به این گفتگوها خبر داد و افزود: «قطری‌ها و پاکستانی‌ها می‌خواهند مطمئن شوند که ما این کار را به شیوه درست انجام می‌دهیم، بنابراین من تلاش می‌کنم به این روند احترام بگذارم.»
معاون ترامپ که سفر خود به سوئیس را در اواخر پنج‌شنبه شب به تعویق انداخته بود، بار دیگر تاکید کرد که انتظار دارد طی دو روز آینده عازم این کشور شود. او با این حال خاطرنشان کرد که هماهنگی‌های این سفر «همواره یک رقص هماهنگی ظریف دیپلماتیک است.» این مذاکرات که پیش‌تر قرار بود روز جمعه برگزار شود، پس از وقفه‌ای کوتاه دوباره در آستانه ازسرگیری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76546" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvSWzDMERi3-EiDPyvNC_7Of0OLGUCryOgd62eDfNm6OqDtLaWc_FZdD3kxfXalzUIOR8c2Y4MqE3S7L5MgsDIscf_JrNz9QORJFAZp2sIm1Aa4CoKS1hjeoEHv9HTQi_mBWGifKmf-3nRluG_mL1cpJjVWU9n_WWjSe87G6sHrVS53s2MWS6QgjUTutiMBSRCvsG_cFU944xmQPnH-h9Ui4o18t8f7qZ6oiSJoxEQOIgpbzIaLjIu36qnR5olUmWc1WOf9mVmW3UfttEVZ4IftUZ3QCSJGB3fsUm7xvKKLp6tRVWIIYiUj3fS4-WOaYU3Ota-NodqC5nuSoCIdoSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«طاها نظری» معترض ۱۸ساله که پیشتر به‌دلیل حضور در اعتراضات ۱۸ و ۱۹دی۱۴۰۴ بازداشت شده بود، پس از  تشکیل جلسه رسیدگی به پرونده، به ۵سال حبس تعزیری محکوم شده است.
ماموران اطلاعات شاهرود، در فروردین ۱۴۰۵، طاها نظری را شناسایی و به صورت تلفنی احضار کردند. بعد از مراجعه به محل، این جوان ۱۸ساله به‌صورت موقت بازداشت و تحت فشار برای پذیرش اتهاماتی نظیر «ارتباط با تلویزیون‌های فارسی‌زبان و فیلم‌برداری از اعتراضات» به او نسبت داده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76545" target="_blank">📅 17:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sWZu-uBMScpbq7G_8zkudxGNq1xYeNBZDxGHAzDyNOzEExoaFo9wlt41qEOBOA8TlekSNrD8llhtFcOQfVaICzcBrjnDne8JppOeVUEUxXkk5-f4VWh98NZrH2tDLnwwa4LBgryOkgLbxkEfuYAxMG57wbH5Yf1a5C8ItK49aYYOvNykkPhpmKaPdhDYEiftR4_NC5P_95LoGU2l5XWLb35PYaJFfv4QXeEEXtFDXOUD5Prx9OzMz39_dqOje3CmoLm6k4En-Mo-dDIkQoLkkLdO18qAquIJtMMrI2XhKyG9LwBk-qjUbcR5yy4UDWI-3RNVGjOEiV-r5ep0IMv9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ilRKAWo7PdkJoV1vUZUdPEhfqcGZbKYrU0Hdj18LunVbB2m6E9d--xkL_3ocMaDtw2yg3CXwzRlda3Ylfw1mLC1sKifxe_y_iTvztYb_ZwzYPH-PlSgsGg9IWzws5jCfLByhw_7HvJ00FaFm40_Ereaph5F_A4FOiFNIVFs4yFIa5MEwAL0TaSczik1OzsmntQukLbVtuuHJwFDYJv6AoxUUelZHfMdgTCwGptz6b9Zfg6qwWsE74k5q286Yqu6BVIesw5NmXQG1a8mcgBwhyL2xxD97G1pa4J0MPr8gE0cPXqlmIBoEyopRqhVmzZbilEyTIH2j3YhSeQxeGQhAAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت دلار و دیگر ارزهای خارجی که در پی نتیجه موقت مذاکرات ایران و آمریکا کاهش یافته بود بار دیگر افزایشی شد.
روز شنبه، ۳۰ خردادماه، قیمت دلار آمریکا در بازار به ۱۶۲ هزار و ۵۰۰ تومان رسید. قیمت یک یوروی اروپا نیز در این روز به ۱۸۶ هزار و ۴۰۰ تومان رسید.
این در حالی است که در طی روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسیده و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شده بود.
روزنامه هم‌میهن روز شنبه قیمت سکه امامی را در بازار طلای ایران ۱۶۹ میلیون تومان گزارش کرد.
از زمان اعلام تفاهم‌نامه ایران و آمریکا در تلاش برای پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران شاهد کاهش قابل توجهی بود.
@
VahidHeadline
حسین صمصامی، عضو کمیسیون اقتصادی مجلس شورای اسلامی، در گفت‌وگو با سایت خبری تابناک افشا کرد که در هفت سال گذشته بیش از ۱۳۰ میلیارد دلار ارز حاصل از صادرات به کشور بازنگشته است.
این در حالی است که حکومت برای بازگرداندن ۲۴ میلیارد دلار دارایی مسدودشده کشور وارد چانه‌زنی فراوان با دولت ایالات متحده شده است، امری که نشان می‌دهد تا چه حد به این پول نیاز دارد.
در این میان بیشترین میزان عدم بازگشت ارز صادرات مربوط به سال ۱۴۰۴ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76543" target="_blank">📅 17:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76541">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V7Xodbg6T-s2GcrC_wvTFLzeuaQ0MIEdrGa3TJMuVEHDmquj_OCMrUdjwXbU_YcNASeajiwg37PnMXSAN7QwV-lTk56bCN_DwVQN2OnayKCoEPB0WWjX3XxuqG2fTtFxBwGc3_78nHmZeRBIQ9XL7tmGi7lZAP1Eqr1VpTzlBMMH5AtVm8mJNlXMey_sq45f5W-LA_0Mlr9s_PLHSDKy1GYrlYCQco3MTObTfUAVxSbIfi8tFwnPBv9j-NjRyzLq2Am-erQ8nPhNCYrWYUycu5s_QiwMsO-TqZkW7CF0QHKGkASjV_ki30dcueXyHcgd-DhONtxRU9bNSuoHmjFpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=knItpYKIjHdinPM5pfus3kftWwA7ZvYkyrgAKV2TwVexqCfVieACnmi0f2Pf-1nWdGPxmP5Wo7oss1DTVy6LW5Td7wFOz9y8-E91JQp0iXL19gPjiH2eDV3cDdd92sBx9ggwd6FNzvfFMGPw-8yugvDPilX7zDOH-e95X66DJPX34kLp28d2XNfxzswaJ_icJqSAI_nXTsyiued5ng9DK8pNjgGiGPwuW9RrTaZVyIkSnupJd50KYcNRJyjb65T6NDp8It3hySQXN7RcqCu_BYJ3s3VJfFEhbCgY6Ix27zp7EGWxkbkQx3WSWDXWXr2WknTy3O-YzngEyU5HM4F4Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddbc33926c.mp4?token=knItpYKIjHdinPM5pfus3kftWwA7ZvYkyrgAKV2TwVexqCfVieACnmi0f2Pf-1nWdGPxmP5Wo7oss1DTVy6LW5Td7wFOz9y8-E91JQp0iXL19gPjiH2eDV3cDdd92sBx9ggwd6FNzvfFMGPw-8yugvDPilX7zDOH-e95X66DJPX34kLp28d2XNfxzswaJ_icJqSAI_nXTsyiued5ng9DK8pNjgGiGPwuW9RrTaZVyIkSnupJd50KYcNRJyjb65T6NDp8It3hySQXN7RcqCu_BYJ3s3VJfFEhbCgY6Ix27zp7EGWxkbkQx3WSWDXWXr2WknTy3O-YzngEyU5HM4F4Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که هاجر نادری، مادر متین پرویزی، در صفحۀ شخصی خود منتشر کرده است او را در کنار آرامگاه پسرش نشان می‌دهد که می‌گوید «من به پسرم فقط یاحسین و تشنگی را یاد ندادم، به او یاد دادم که جلوی حرف زور بایستد»
خانم نادری در ادامه با شرح کشته شدن فرزندش در اعتراضات ۱۸ دی‌ماه می‌گوید امسال محرم برای فرزندان میهن که «ناجوانمردانه کشته شدند» عزاداری خواهد کرد و ادامه می‌دهد که «می‌دانم امام حسین هم برای این جوانان عزاداری خواهد کرد»
متین پرویزی ۱۸ دی‌ماه سال گذشته در سبزه‌میدان زنجان با شلیک گلوله جنگی نیروهای حکومتی به سرش کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76541" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2b1VdMvZEoZsGTb1xquObL_fbCPXOZ0wfEWQNNybTG7EZ6EZ5fNNhuZMb3hcw55cg8Gw5uHytGXZ8E7d4dfeqbWUe5hoF1Un0ellTKEedFgNwiMNwg9awTVozC8F9lyUdPkxva74abzcQMNSBcQn4v7yESS-LeTI8q-434mBgdorMZmFdIA89ExsYFfDCNb6OlzhWUPhRfS8eQ1itrifwgpX8aqiRw2ShgYcDEDMcxHDbPl_6t-yMY4DqmFVFSpyMW87r0tdKYPPTZ6T9fonYqc5Ogg2dW78GyO7Px9X_98Ua4UphqaksgH9Zh8EQRWmpYCgbg8h3QatZPu0PJeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، صبح امروز وارد مشهد شد.
ایرنا به نقل از منابع خبری در استانداری خراسان رضوی گفته است که او سپس برای گفتگو با مقامات عازم تهران خواهد شد.
بر اساس گزارش‌ها وزیر کشور پاکستان قرار است در این سفر در مورد از سرگیری مذاکرات مستقیم بین آمریکا و ایران در سوئیس، با مقامات ایران گفتگو کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76540" target="_blank">📅 17:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76539">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4TB5oCJ_sMElvoS_9aahKMOU2rDvrPD0b-wVwP7dWketzInCD7_rgiB1do4U4qJu0MV8hfjm5Kdcw6fbhOEhEZMgcqv6zDzaVsh42nBa0X-sueDJp7-Bk-MEvtbysvBmQHypOGE7cXh7jaCWJ3xID3v8qtJgAvxcEcCW-jPoo2rfm_sJKkOTUUR-y8BDYMZvKr5eYOEimm-k-ccJREDA2dl3p8jZVbbNJIebUMZ3I18i8lRX0ljNJ-SvkmJsHgJIV-MrjO1sDK-dNGClv0XLwzbjE72jhj1yCl85hUsWrxS8JFO9l7NtsxRy61ZAKThr1JEMZHRBxaev05mZNPZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز اطلاع‌رسانی پلیس استان لرستان از پلمب یک واحد صنفی و معرفی فرد متخلف به مرجع قضایی خبر داده و اعلام کرده است این اقدام پس از آن صورت گرفته که به گفته این نهاد، واحد مذکور «ضمن عدم رعایت قوانین و مقررات، اقدام به هنجارشکنی» کرده بود.
این در حالی است که تنها سه روز پیش نیز مرکز اطلاع‌رسانی پلیس لرستان از پلمپ پنج کافه‌رستوران و سفره‌خانه سنتی در سطح استان خبر داده بود. در آن گزارش، دلیل برخورد با این اماکن، اجرای طرح موسوم به «ارتقای امنیت اخلاقی و اجتماعی» و آنچه «هنجارشکنی» عنوان شده، اعلام شده بود.
در هفته‌های اخیر و هم‌زمان با فروکش کردن فضای امنیتی ناشی از تنش‌های بیرونی، گزارش‌هایی از افزایش تمرکز نهادهای انتظامی و قضایی بر حوزه‌های مرتبط با سبک زندگی شهروندان منتشر شده است؛ روندی که به نظر می‌رسد بار دیگر کسب‌وکارهایی مانند کافه‌ها، رستوران‌ها، فضاهای موسیقی، پوشش و نوع تعاملات اجتماعی را هدف قرار داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/76539" target="_blank">📅 17:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=rjjpWRp97IRqDTAnMVBYgORKxDtXwHhVoy-rY0bLgwSqAkPxUQczzw_a4XF9d_YQxf6JURWyhUlTQPGWcQpnrtLA6GyY8cwRKsAbQ-AeAHFP0nupJGsFnLd-03ydjAArc6vJBhBo2vafwirOXsoeUBxqC0RT22ZbOXu2UE17evgCjIZbIsFvJDb0rrWniOHOoZaySy6L-eU_c_MbsQp_XjS9RwlBistUHeFeiFHKQ9FYOSOdnTX9nmyyDBmN1RbIU5_uMrTzPAY0Es1jb66wxXbsoctep9prAb9BTq1eYLmofPmOsURgsqLmYxue_AyYgfTW2ybH45p5wt7rl-g3sw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f49d58cd5c.mp4?token=rjjpWRp97IRqDTAnMVBYgORKxDtXwHhVoy-rY0bLgwSqAkPxUQczzw_a4XF9d_YQxf6JURWyhUlTQPGWcQpnrtLA6GyY8cwRKsAbQ-AeAHFP0nupJGsFnLd-03ydjAArc6vJBhBo2vafwirOXsoeUBxqC0RT22ZbOXu2UE17evgCjIZbIsFvJDb0rrWniOHOoZaySy6L-eU_c_MbsQp_XjS9RwlBistUHeFeiFHKQ9FYOSOdnTX9nmyyDBmN1RbIU5_uMrTzPAY0Es1jb66wxXbsoctep9prAb9BTq1eYLmofPmOsURgsqLmYxue_AyYgfTW2ybH45p5wt7rl-g3sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع‌های اعتراضی زنان به فعالیت‌های معدنی حوالی دو روستا در استان‌های کرمان و سیستان‌وبلوچستان با حضور نیروی انتظامی به خشونت کشیده شد.
بر اساس گزارش‌ها زنان روستای پشموکی از توابع فاریاب استان کرمان روز ۲۷ خرداد در ادامه اعتراضات مردمی نسبت به نحوه واگذاری و بهره‌برداری از معدن کرومیت پشموکی تجمع کرده بودند.
گفته شده که نیروی انتظامی علاوه بر ضرب‌وشتم معترضان، شماری از آن‌ها را بازداشت کرد.
هم‌چنین منابع بلوچ گزارش داده‌اند که زنان روستای سرسیاه از توابع تفتان استان سیستان‌وبلوچستان هم روز ۲۶ خرداد در اعتراض به گسترش فعالیت‌های معدن طلای تفتان و پیامدهای آن بر زندگی مردم منطقه تجمع کرده بودند.
در ویدئویی که منتشر شده شنیده می‌شود که مأموران نیروی انتظامی با خشونت، تهدید، توهین و واژه‌های تحقیرآمیز با این زنان برخورد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76537" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z_AtBqs02_K_4jfNDLdhWF_d5VkpEsKfsWQzimgbhl_wXXijMe0K_iDaPyo0R2wwIK43AnhcK4cSg_X1XXtJIHcOoW3H313zq-A4VgM5X3omDiTwERhj92l7ZYEitQPVa_d-K_4KHNivjVeWoWLIAGJm3h01gOJitsKge3ls8CSMRv8WRjMBNDmp515Ulcd4tDK_9i2WGWTemMKpo0GKsxHCG2tPTBD86kqvATTkbk09cbW5T_vTCDU4SjdpU9AciCn4j7Y_NVOQsuNLKWTNRHEwjn43hpSryOxApoyeTyNI27nv3XACKPWMFrv27YN11NfWcXlLWzIjHyvJPO6lwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DX0M2YH1XUQfVTRb2MRByuAZwnbJOuaMoo_Ckjfp6rBMSZMOddExAk_2LxZBVJIguxTt_5WHg-V9EwiLos_9NKG-_j1Zp0fsTscftFiH7TqPrx0Z878FXmh53NImMvRs2PW_XQx0D7plQj3XmTmjq2GMpsbp3HDkRj7245XSXKSRYpnKlU5kWAJvZsZTOVE3BPKYASRmi4hBZvpcOEgAFIXE04XAFMjXVnH2kM35j5VXVFc7noYDVwIGY9MXeAba4VKHChnAPz4PjYNXoXEVSH0b9ylU36XV7TlQmuD1beUAlmof09ZZzIlEoXWjMqmD0OfK84IiAiXPDIeOBsWaUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام آمریکایی به اکسیوس گفت: استیو ویتکاف، فرستاده کاخ سفید، در حال سفر به سوئیس است، جایی که انتظار می‌رود دور اول مذاکرات با ایران در مورد توافق هسته‌ای احتمالی برگزار شود.
به نوشته اکسیوس، قرار بود مذاکرات جمعه ۲۹ خرداد آغاز شود، اما به دلیل درگیری بین اسرائیل و حزب‌الله در لبنان به تعویق افتاد.
@
VahidOOnLine
خبرنگار اکسیوس به نقل از یک منبع آگاه، روز شنبه اعلام کرد: «عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، در حال برنامه‌ریزی برای سفر به سوئیس در روز شنبه است.هرچند این برنامه همچون گذشته ممکن است تغییر کند.»
این خبرنگار به نقل از منبعی در یکی از کشورهای میانجی فاش کرد که عراقچی روز جمعه به چند تن از همتایان خود گفته است: «موضوع آتش‌بس در لبنان برای ایران یک مسئله حیاتی است و حکم برد یا باخت (تعیین‌کننده سرنوشت) را برای مذاکرات ایران و آمریکا دارد.»
خبرنگار اکسیوس همچنین به نقل از یک منبع دوم از میان کشورهای واسط افزود: «ایرانی‌ها صراحتا تأکید کرده‌اند که می‌خواهند پیش از سفر به سوئیس، شاهد برقراری و تثبیت کامل آتش‌بس باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76535" target="_blank">📅 04:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=kB0HJBUjUyPWn9iBKfUJiFJcQ1q5kmNraqx9hg3ESDgEhjDQTTz8YEepDCvYGpoQlSg1bRVXpuhql_Zgsoy7CR8bYbiOV4EXKNtOq0BzLj7L5EEhpE8gFXv3zM5rBjK8-vR332umFoDOhDmxigEEHZsT5WDU_gYSrg3dzcSUAt_BcDY4iPRCmJx-d205obKA_17rXXViFXkk_TperXGUX_AuFpjcx-oKtFkfqgjcUbNFGpc6MmnkbBb7s-24emJAhTzBYoXnRrZ1Ws5l7mva2DMzMrFlDAPNy9MZn5hSuzzODziEjDUtfa-Jph7MkE0hDewg70IhlSb79aW4wy4Pog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e1550d193.mp4?token=kB0HJBUjUyPWn9iBKfUJiFJcQ1q5kmNraqx9hg3ESDgEhjDQTTz8YEepDCvYGpoQlSg1bRVXpuhql_Zgsoy7CR8bYbiOV4EXKNtOq0BzLj7L5EEhpE8gFXv3zM5rBjK8-vR332umFoDOhDmxigEEHZsT5WDU_gYSrg3dzcSUAt_BcDY4iPRCmJx-d205obKA_17rXXViFXkk_TperXGUX_AuFpjcx-oKtFkfqgjcUbNFGpc6MmnkbBb7s-24emJAhTzBYoXnRrZ1Ws5l7mva2DMzMrFlDAPNy9MZn5hSuzzODziEjDUtfa-Jph7MkE0hDewg70IhlSb79aW4wy4Pog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو بخش مربوط به ایران از مصاحبه امروز ترامپ
متن کامل این بخش‌ها:
https://telegra.ph/trump-06-19
بعضی از جملات همان متن:
ترامپ: و من آیت‌الله را کشتم. یک مقام سپاه هم بود. و متأسفانه به آیت‌الله دیگر هم آسیب جدی زدم. به شما بگویم، من او را ملاقات نکردم، با او صحبت نکردم، اما دیگران درباره‌اش حرف می‌زدند. او شجاعت خاصی دارد، چون به‌شدت آسیب دیده است.
با وجود همه این‌ها، نمی‌توانید بگویید بی‌خیال. من ارتششان را نابود کردم. نمی‌خواهم این را نادیده بگیرند.
برای کسانی که می‌گویند شاید من به‌اندازه کافی سخت نگرفتم، باید بگویم من ارتششان را نابود کردم. بزرگ‌ترین پلشان را زدم، چون دیر در جلسه حاضر شدند. گفتند این کار خیلی قشنگی نبود. من گفتم پل جورج واشنگتن؟ سه دقیقه‌ای نابودش کردم. خارک را زدم، همه چیز را، جز یک چیز. گفتم به لوله‌ها دست نزنید، چون نمی‌خواهم به اقتصاد جهان آسیب بزنم.
بنابراین فکر می‌کنم خیلی سخت گرفتیم. به کسانی گوش ندهید که می‌گویند می‌توانست سخت‌تر باشد. کل ارتششان از بین رفته است.
پرسشگر: چطور تغییر رژیم است وقتی هنوز خامنه‌ای جوان‌تر و خیلی از مقام‌های سپاه آنجا هستند؟
چون افراد متفاوتی هستند. خامنه‌ای جوان‌تر با پدرش فرق دارد. افرادی هستند که بسیار کمتر از دو گروه قبلی رادیکال‌اند؛ و من هر دو گروه قبلی را می‌شناختم.
اما به این فکر کنید: همه آن‌ها رفته‌اند. بعد می‌گویند چرا سخت‌تر نگرفتی؟ تنها راهی که می‌توانم سخت‌تر بگیرم این است که دو یا سه هفته دیگر وارد شوم و آن‌ها را شدیداً بمباران کنم. اما این چه چیزی برای ما به دست می‌آورد؟ تنگه هرمز باز نخواهد ماند. فرض کنید این کار را می‌کردم. فرض کنید تصمیم می‌گرفتم این کار را بکنم. الآن بازار سهام ما فوق‌العاده بالاست. قیمت نفت در حال سقوط است. قیمت نفت تقریباً همان جایی است که قبل از شروع کار من بود. تفاوت بزرگ این است که ایران هرگز سلاح هسته‌ای نخواهد داشت. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت، روشن است؟ خیلی واضح و ساده است.
آیا می‌دانید در دو ماه گذشته، من کشتی‌های زیادی را از آنجا خارج می‌کردم و کسی خبر نداشت؟ می‌دانید چرا خبر نداشتند؟ چون ما رادارشان را از کار انداختیم. همه تجهیزات دفاعی‌شان را زدیم. آن‌ها قادر به دیدن نبودند. هفته گذشته، یک شب ۲۵ کشتی داشتیم، یک شب ۲۲ کشتی، یک شب ۱۹ کشتی، یک شب ۲۱ کشتی. هر شب، همه این کشتی‌ها بیرون می‌رفتند.
ایرانی‌ها مردم بسیار باهوشی‌اند. نوعی نبوغ ابتدایی دارند، اما باهوش‌اند. منظورم این است که باید جلوی آن‌ها را می‌گرفتم، چون اگر سلاح هسته‌ای داشتند، از آن استفاده می‌کردند. می‌خواستید ببینید؟ بگذارید چند شهر را در جایی منفجر کنند؟ مثلاً اسرائیل را منفجر می‌کردند.
اگر من نبودم، اسرائیل امروز وجود نداشت. چون من توافق باراک حسین اوباما، یعنی برجام را لغو کردم؛ توافقی که مسیری به سوی سلاح هسته‌ای بود. آن‌ها پنج سال پیش به آن رسیده بودند. به نظر من، در همان هفته اول از آن استفاده می‌کردند. اسرائیل دیگر با ما نبود. اگر من آن کار را نکرده بودم، اسرائیل سال‌ها پیش از بین رفته بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/76534" target="_blank">📅 01:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvk_N0XYEltU9h5-l-YLDsLGN0D5RXihPP0dTIN13pF6oNoVOf0I_c9REFXZapr5rcaT0o3fo92BgdQBIkPFDc2NDCaDswFibzzFECLOtLnOyLPylyb8i5Iw_nQCW_AqKxjBrfTiHUKRczfXHJbi4RubVvmCugdrwp1OQqmq9uuJP3oS3ok2JY5B-_DEjhPwKJc69fqWAL2Z4izMTxXD0CHH2R0MdHJphQf7D5wFMsEndrImxls0r0u2C3ffFZ5n4fapY_bJULmYbejR-pA0IC7oG5cmd8gp1O_HPW3WXvUwFEvhgqc7lDcyKrOgJ6KHndY5FnxUD99_93jjGpBtKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا، در مصاحبه‌ای با برنامه «آکسیوس شو» با دفاع از تصمیم خود برای شروع عملیات نظامی در ایران، مقام‌های جمهوری اسلامی را «بسیار باهوش» و «نابغه‌های بدوی» توصیف کرد و هشدار داد که آن‌ها در عین حال بسیار غیرقابل‌پیش‌بینی هستند.
ترامپ با اشاره به مداخله نظامی اخیر ایالات متحده گفت: «من مجبور به اقدام شدم تا جلوی آن‌ها را بگیرم؛ چون اگر سلاح هسته‌ای داشتند، حتما از آن استفاده می‌کردند و با منفجر کردن چند شهر، از جمله در اسرائیل، هرج‌ومرجی واقعی به راه می‌انداختند.»
او با تاکید بر اینکه اگر اقدام او در لغو برجام نبود، اسرائیل سال‌ها پیش نابود شده بود، توافق دوران اوباما را مسیری هموار برای دستیابی جمهوری اسلامی ایران به بمب اتم دانست. ترامپ همچنین با ابراز شگفتی از زمان‌بندی تقابل با ایران افزود: «چیزی که مرا غافلگیر کرد این بود که آن‌ها این‌قدر منتظر ماندند. آن‌ها صبر کردند تا من به قدرت بازگردم؛ البته این کارشان عمدی نبود. هیچ‌کس، حتی با وجود سلاح‌سازی ساختار حکومتی علیه من، فکر نمی‌کرد بازگردم، اما من با خروشی بزرگ‌تر از قبل بازگشتم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76533" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشجویان متحد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tj_oSE6OdUdUYaQ_3oythyXbssq9WlEcLpCztu8jtkWhrE9ETbk5ziBaIdn7HoULte70gjkl1R7Y297bWRcTRjklYQqY26U1ljWZqZOq-QqkFwrzByE90f7sOf5fQS_uPlUa4x1qUlfp37cwUPGHq8wki1wRdV45XxfvWQ79sEg528AI3pCZlqkNsjWSSb-UMQjwmt_QHrA3TV-wnDG0LHHm1gtVx80m4QXqXeE93MsPexbr--EGrwzmCVuN_d-4MFFqKSobfFXFtScIMC5bTvdyQKO-2Tp8zJI1fRSHe1uo__qqRWoYghFATdqLOodLmi1d-13gMu-RrgpZAuzosg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRrO4FnxnrSGVQh6iut2s3TpEAPlzbjapNZFfTGt1I1kopTFZ-MPeztGkX4MfGpj6spjEDqRmfP3lLG4qgituYbnSDxG_nQY5PTh-K1dF7E5AEuCehGIeiy4NcTFk4okpSCjDFDKXrGdPn_tlazGbV99P2tM38uheJfbeo3UbYJVuwFxBOBSBUfjl0WHSKE7Ribk324DHs3NI8ioUUy-jTCgKAzwVbh8m3nNS34a3k3O3qHw9PmwGdPfcyZuGMPT3CQKpJ7qBgv-x0n6k0cRwGnuMXZcAp_GTkEYZu0_9RsIKzUoUmMP874mwH3hx6y8HywQq0O10ueLrxrRTEU1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIEqgNi8ab0ev7lpFY5Sllp4yecKhsrERgoif88DH9vB1aCVEV2KqzlaeFA8Clt5kPfMbg2kL_d_tEq71GPyLK9GMa4gYv78HGBEdlb6Pe1O8kF36IUQbzruALiallyXiM3pHTSvZ97A5iNsKLBSsb3-hMIwGRG2i6A2fd4JtUMzj9CzxlYN7FMjPmsFVG1F3Gjjn64H_CRlgq0-zM513vWAD9ExK6_x67vaeGzmQzHgMDbRcXj5tZKh-UoMGPeCbcWsS400wJzxw6X1JyjvcZJ-EzVupOqr7KUdSLP6Y0idnd4fFV-FvfplmG3O-zmvLZeicgZcgZ65riD3a1EK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCrYMOE_3qZMWm74UJmQCESt5UrlksEgBNVlZT3TSEJa_F1OwJwaxLM8mvMyslUECuhaqp_nsXNpkS42vLyUZWDIsSj4Mreq9SjxPavBAiw8shtouxr_Yhj0RWotwNqCFvneDL08n6UgzzKMe4kMC1L0RI0v7u4N_hutxz43SmLmr4PWCG7rjcYsMS6aXOZl3XNMBMxL922HwFLPOKxVcRER8kZ9Mv3b4xkacfGE3rMnyUlcf25EI1yWWqMCDPF9vivt09TeanFf85u5fl_71yWcUpKHpvnSIFg5VNKOCTohLxYBe_mkKkqzJ6Nelt0pRS7ZBIPFNNrQHw1WIr8pjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgnadLKK5PopSh0RNQ8UK5raYBMd5lHS8F-xdbsz3TnOw89VYpSJ_pLV27T0HoAqNEiwbc_NfzsbDxjxWgz4FbRT5tZhMw-Rrzy05FyerT17DEFrAjjwLexvg3Kz4dN1y0udM0r5vqi8TN1A-j4Zcm8_5w_vUToVvimDAn1Fg8EALjc41BNqU8WTwbbJnCgVVo5S8jBM45u4pR_vBy5a2pqYFyXHItxqAvnGBE4Tp5juyj7u6792a3yB543oNOx6dEHxyJBq-QFRkpRHbN2hMTZ12K-LPcNTwTMQ_3ZKHcOuqQ3TO4lGCXHP6Su8RWTL7ZBy5eM0iL1WjWRgFhTghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbN3IIzIZ2u7o25tEUC9ixfbWuwXtD5NAvTQqRKphrA1dazfG3ERjqiRnLOjoOfY5BCA7ha_AOc_kcZbL5qDdTu7Fw1dJwzTXnEBfBYNP7CUjilpmPqaXBj-XLTjWLaFRHdyF-0NsDpr0xV1xmbpzSR4cPisCIhQwepuR_YbZa9mz2EW8tb7eNZONJ3aya_-9xfqZ-cfMh8dI-O2t_2lzz3mbmktmsySS8YMXK5R5ljY-DGUXZ43JolTJC78v6LTg6JkDFeAjWYpICpBLcTf4czeJYbrayQSuCHj1AA79XcgsRIS0uYXv3CZ_YiJkiR6Z0zkN61VnFJCgTls_-6snw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4anKvWFvmkmuBQq3Gp8GoDj5H2yVtwl-Ychl1Lve6oUiblxbeChICLuGCrWlpfeeaGFtClLmVJhv_9jMfGzEUWjW3AqBWr2-oZLI-kKHvSjpsUdc0gE9M-jiWQZ3nLYQ-HDfBIX-t8BupvMP3Gv5u_cCl8w04RgwSTajYStJ9iXOaEBb7IcXFxu1Ht1w1KCSDfK-OtjO4Q1R2X1Cx_jubxqa1vResUeuEi01j8mJcx3PVWrj7zxNDHqX4qmB7fPqqeP9YDuWLBHQAA4mu1rmpwFO3JYu2-d3NjJxqLILDjCvkxO2QifdXY2myBxamrJTCf1XwUVUcLZd6yQZ_kk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5INU8pmPQD2dIJxuhWxd-xkHolNky0segKOU9pM3whlbiX_8WfahWjBFpXlUtE0ZmdYclznl_66hDynjW6p2A05VgfdWse2k4_sR2t2t5jTVfcppuV9u5tzeFO4rBsnqMcyruEUzsPSBHaxIfohELcEI00I1VyEzFFMTbGeIiC3uC54GVbQN1PrCwUyNCmGuxjaEz6WeR0w93EonYp38XtTrPIW1ecKx1YORSqo3dUOpSUZImSUKULsDsjKWmpzxDKhjsfwAxHY3jJ_gLbimbMtVm7QiM5ut_EnOooP4gdukM_VFzjsgjoSWLvqFiCY_1d0phGFSE5QkdJfI1WdFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
صدور حکم اخراج برای هفت دانشجوی دانشگاه شریف؛ صدور حکم غیابی برای یکی از دانشجویان بازداشتی؟
🔻
بر اساس گزارش‌های رسیده به دانشجویان متحد، کمیته انضباطی دانشگاه شریف، برای هفت دانشجوی این دانشگاه حکم بدوی اخراج صادر شده است. اسامی دانشجویان به شرح زیر است:
🔻
رضا دالمن، ورودی کارشناسی ارشد ۱۴۰۳ مهندسی کامپیوتر: اخراج و چهار سال محرومیت از تحصیل
🔻
فاطمه خاکپور، ورودی کارشناسی ۱۴۰۳ شیمی: اخراج
🔻
حسین شادمان، ورودی کارشناسی ارشد ۱۴۰۴ مهندسی صنایع: اخراج
🔻
سپنتا سعیدی، ورودی کارشناسی ۱۴۰۴ مهندسی کامپیوتر: اخراج و پنج سال محرومیت از تحصیل
🔻
مسیحا باقری، ورودی کارشناسی ۱۴۰۲ مهندسی کامپیوتر: اخراج
🔻
فریبرز کهن‌زاد، ورودی کارشناسی ۱۴۰۰ مهندسی برق(تغییر رشته به مهندسی صنایع): اخراج و پنج سال محرومیت از تحصیل
🔻
پرنیان خدابخشی، ورودی کارشناسی ۱۴۰۲ مهندسی و علم مواد: اخراج و پنج سال محرومیت از تحصیل
🔻
همچنین در برخی رسانه‌ها خبر صدور حکم اخراج برای «آریانا کوچکی»، ورودی کارشناسی ۱۴۰۰ مهندسی صنایع، نیز منتشر شده است. هر چند بر اساس گزارش‌هایی که به دست ما رسیده، ایشان در حال حاضر بازداشت هستند و خبری در مورد برگزاری کمیته بدوی ایشان نداریم. هر چند صدور حکم غیابی برای دانشجویان بازداشتی در جمهوری اسلامی، پدیده تازه‌ای نیست.
🔻
لازم به ذکر است از میان هفت نفر یاد شده، کمیته سه تن(سپنتا سعیدی، حسین شادمان، مسیحا باقری) با محوریت فعالیت در شبکه‌های اجتماعی و کمیته چهار تن دیگر با محوریت اعتراضات اسفندماه برگزار شده است.
ارتباط با ما:
@Public_anjmotahed
🆔
@anjmotahed</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76525" target="_blank">📅 22:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=Q9y_UOwhHXBNNUcVkpsjtKBLulaP7BKw_G7_22Mi_m2y1RrpzHSz7LQrEk3Y0ctRjNGYAct3-4DwvbC7rkN2og6K6w5Yw_fZhadz77N3TZIlf6kkKjfAfuiaFs5wPatu3kpA29oR161ZqaWY6RbRl9MgHD32bLWGydQ6wMIUmZeVSrnFvJvPAJtE1IukHE4zHeoJ1Z-624K6zFZKxBUJQOQ2axQojcWHJeeS_MEg316ltbvFDchF3IU8lzBCp1yzOOhh9pwtEh5ahBNRftqeYhbdbfWqXY77L5B5QJ8WvKzW09CAJcTa9APEwNoxmKyTyjrwPRYHVGoOupS1Wb0HXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=Q9y_UOwhHXBNNUcVkpsjtKBLulaP7BKw_G7_22Mi_m2y1RrpzHSz7LQrEk3Y0ctRjNGYAct3-4DwvbC7rkN2og6K6w5Yw_fZhadz77N3TZIlf6kkKjfAfuiaFs5wPatu3kpA29oR161ZqaWY6RbRl9MgHD32bLWGydQ6wMIUmZeVSrnFvJvPAJtE1IukHE4zHeoJ1Z-624K6zFZKxBUJQOQ2axQojcWHJeeS_MEg316ltbvFDchF3IU8lzBCp1yzOOhh9pwtEh5ahBNRftqeYhbdbfWqXY77L5B5QJ8WvKzW09CAJcTa9APEwNoxmKyTyjrwPRYHVGoOupS1Wb0HXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه جی‌دی ونس با زیرنویس فارسی
گفت‌وگو با:
الی بث استاکی، مجری و مفسر محافظه‌کار مسیحی آمریکایی، میزبان پادکست Relatable در شبکه BlazeTV
برنامه‌ای که در آن از زاویه‌ای مذهبی و راست‌گرایانه به سیاست، فرهنگ، خانواده و مسائل اجتماعی آمریکا می‌پردازد.
او در میان مخاطبان اوانجلیکال و محافظه‌کار آمریکا چهره‌ای شناخته‌شده است و در این گفت‌وگو با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره ایمان، خانواده، سیاست داخلی، اسرائیل و توافق با ایران صحبت می‌کند.
یک ساعت درباره مسیحی زندگی کردن
حرف زدند
و ده دقیقه درباره نقش و نفوذ اسرائیل در سیاست آمریکا و توافق با ایران برای مخاطبی از اون نوع
اینجوری می‌پرسه: می‌خواهید یک مادر معمولی چه بداند؟
متن این دقایق:
https://telegra.ph/JDVance-06-19
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76524" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cakQ7QPnfnMf6DXywQzt1re4qJBEdnXxQq6xP-dd4NdMI5d7EGJ5ESYM-JoZhrmKCtN7jeth8UXQ9zSeX70ZCvm7n-cz429ED56srzeDr4Uwmc46OAlsWoXaqDxBNTEj19ZF79knVDwSQ239UF8BE7PXfeZon3TGif4h4GUpQDtspa9-F9Gb-F5MfzUPD8dPHD03bpJn7-EOzIxFakpdAo1NawBgjFZ2Ww-3oPllI9Sn1iwC5RTvmagdSXN2B-kxzMUZHgq09ac0haqATst2KjqlzKo27gOs9OHAK9y56eCQ7pHqk4K407nDcxn9OX_nu7_8-fTJaDp51ZZbp26__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در یک گفت‌وگوی تلفنی با شبکه ان‌بی‌سی نیوز گفت که روز جمعه با مقام‌های اسرائیلی صحبت کرده و از آن‌ها خواسته است با گروه حزب‌الله بر سر آتش‌بس توافق کنند.
بر اساس مطلبی که خبرنگار این شبکه در شبکه ایکس منتشر کرد، ترامپ به این مقام‌ها گفته است: «بعضی وقت‌ها فقط باید آرام بگیرید و از عقلتان استفاده کنید.»
این خبرنگار همچنین افزود که ترامپ مشخص نکرد آیا مستقیماً با ‌بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفت‌وگو کرده است یا خیر.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76523" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sdyhhSjf4fXA4sRrn5sCOmbsrgpab5ymHgw1fKqexkNkOQITJDSvPTCfN1EDFvFjXTcC2aIrht8y56FWfWtzPFOVyI9KeeTbQJagiBP34PC9GJnAMm8L48oepgOCrtwYGfqs2iFoB6vI7zR6rB4zxKBy1z26U5ppbCvi6_10PCTduuk9iyHnneArAV1R2MTfEQQfqtbDnt-dBSdLXEyxrpyHDjNv9tBMAJOPmpJNOL4HIu-OI4VAkVzPbtKTSQtl-y9yzZDnhI8UW5quQ6X2fD50l_r-ZvcO41I5jzKLhTk66nLqR6GqqhhNepn0TY7ntBvEEEqAT4OsSjjnA1mhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
او تحویل سلاح‌های حزب‌الله را رد کرد و افزود این سلاح‌ها برای مقابله با اسرائیل هستند.
نعیم قاسم همچنین گفت که ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
دبیرکل حزب‌الله لبنان ادامه داد: «ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76522" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW1rLSFt3VX93fxHJYwd7lglTwRJvyKEYOyaKCUOk84Tqe1AdgKXxt8QaFPHIuzTrHqNYGJqGGGwqWpOGeIF9E2e4WDVsKRpWXSFV6JNBtqT-dBRaWyY11WsGbxxePHewf400FGNQSvzoYQ8iAoZYuHXQEYQ4aa5XvgpAV95eMjh5IU5KlpHcz73O2rqSidLQEYksr0wrejeWRAActjZ9uz8yXg_WKeXMGqyLtu7Xhlauz-jt6oTPhey4UafXrMR5mXSYlnMRg8pq7ce8wEYV-W4CMOR2mgKF63Jdh2llJQMShsSdJQGNMAXHUOFu0pOkCKNz-fXvNCxAwBSMlRH6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه ایران، روز جمعه دعوت جمهوری اسلامی از بازرسان آژانس بین‌المللی انرژی اتمی برای حضور در ایران و انجام بازرسی از تاسیسات هسته‌ای را رد کرد.
او گفت: «بازرسی از تاسیساتی که دسترسی آژانس به آنها به‌دلیل حملات نظامی متوقف گردید، منوط به روند مذاکرات و نتیجه آن خواهد بود.»
پیشتر جی‌دی ونس، معاون رئیس جمهور آمریکا پس از اعلام توافق اخیر در گفت‌وگو با شبکه ان‌بی‌سی گفته بود که بر اساس تفاهم‌نامه میان واشینگتن و تهران، بازرسان آژانس بین‌المللی انرژی اتمی «قطعاً» به ایران بازخواهند گشت.
اسماعیل بقائی همچنین گفت در حال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
نشست بین نمایندگان ایران و ایالات متحده که قرار بود جمعه در سوئیس برگزار شود، لغو شد.
سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد: «با توجه به اینکه امضای متن یادداشت تفاهم در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد.»
او همچنین گزارش‌ها درباره بسته شدن تنگه هرمز را «بی‌اساس» دانست و گفت کشتیرانی در این مسیر در حال انجام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/76521" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76520">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0x8Duhh-xUlkkiq3-aUVD0ONnbDBLRQFZ6uLig9FSKOJuZPe7-rMw8WgGM-nw-0dkqBvBvL9T5vkLvbT2j1fumaed9TEa9LwA9eijhZoOD_sVLp5X1LsE3Dls3QADuMEr9ufQZ0lsoSNuBWCAAvqPlLyc2F4GcuFi6XfeVnFpERyn2KLqfGkrxNHdSfLqQy_wRNkJidx_q50YHfkEy3lFRt628_VkS5uL8IuyazkT6_oNTGxVugB3M6J60KebaSmQQAXAKoS0QFzEhVNyyLi3mEBCYi7vK1DkGKnR8SGULdghslfYPp2oBawc6iurnw0JtY3AgrYpeE5bDnSMO81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز گفت که اسرائیل و حزب‌الله بر سر یک آتش‌بس توافق کرده‌اند که قرار است از ساعت چهار بعدازظهر روز جمعه به وقت محلی آغاز شود.
این مقام که نخواست نامش فاش شود، افزود که مذاکره‌کنندگان آمریکایی و قطری با کمک ایران این توافق را نهایی کرده‌اند.
این مقام همچنین گفت: «درک ما این است که پس از تبادل آتش امروز، اسرائیل و حزب‌الله اکنون در وضعیت آتش‌بس قرار دارند.»
شبکه العربیه نیز به نقل از یک مقام آمریکایی از توافق برای برقراری آتش‌بس بین اسرائیل و حزب‌الله از جمعه خبر داد.
این در حالی است که نخست‌وزیر اسرائیل ساعتی پیش اعلام کرد نیروهای نظامی این کشور تا هر زمان که لازم باشد، در خاک لبنان باقی می‌مانند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76520" target="_blank">📅 17:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZzqSmsyiBLuhIHlTdour339nnsKyz-7GAKU5L62KQ0rFLe6KtvHI7XkaQGZpevG_WhC8jnUoPozyrXakX21gxqpyI_3yJnqiuEvEbklmpuBPpI3HE-GmgcU-ffwj2wCeL5lIvJDgnq-0P5bFOkFo5P4OgVkNya0cHfuvN9aiSCIfa_gWeUt-DHVY1vM3t-ar9OGKFGn7jU6hiGzAnhCawFBwRLNul6UrG9oEI7hEFMgVX6eMZF4SlBxd7rSuV7yPBEIjtvt2rwmCKGmDfjM_Xva96oIkEOcef7NpRkjmCZhXxOm3Bn3qbKGM2SDf89WbLXZ0xmRji7m2vgjCtgP_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957528437f.mp4?token=qY7zhINi-IoVJ6rzg6gYuw1mRvG5JC61KnsZC0yY1tfX71rxg9q--2N0g626So06EOoRWTGf_Z84zPWqG37zALcIq2C_MO52Deq7x-SzZeNWeNpGebDUtvGArRhcQy1y_LVV62zTySLfA2LBzwwJ6a8SxJTSW4p_lC6t9oeUKDGc6q1bcU3yn5IrUtMoXmVDr-NIJnec8qde8zeZNECasX1k91h9GLTj4utm4yFcx9Z_WU2KXMHYL1D4YJwpwUEVocMcnVCweKYZhOsGxY1Hy00nMJERNBz0Gptx1erRKOJ5jvu0EMl-oKqcAHnGh91aCfVwMbgnSzkRPK1XaMR3rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957528437f.mp4?token=qY7zhINi-IoVJ6rzg6gYuw1mRvG5JC61KnsZC0yY1tfX71rxg9q--2N0g626So06EOoRWTGf_Z84zPWqG37zALcIq2C_MO52Deq7x-SzZeNWeNpGebDUtvGArRhcQy1y_LVV62zTySLfA2LBzwwJ6a8SxJTSW4p_lC6t9oeUKDGc6q1bcU3yn5IrUtMoXmVDr-NIJnec8qde8zeZNECasX1k91h9GLTj4utm4yFcx9Z_WU2KXMHYL1D4YJwpwUEVocMcnVCweKYZhOsGxY1Hy00nMJERNBz0Gptx1erRKOJ5jvu0EMl-oKqcAHnGh91aCfVwMbgnSzkRPK1XaMR3rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه ایتالیا روز جمعه اعلام کرد در واکنش به گزارش‌ها درباره اظهارات دونالد ترامپ سفر برنامه‌ریزی‌شده خود به ایالات متحده را لغو می‌کند.
آنتونیو تایانی در شبکه اکس نوشت: «سخنان شدیدا توهین‌آمیز رئیس‌جمهوری ترامپ… به همه مردم ایتالیا اهانت می‌کند.»
به گزارش شبکه ایتالیایی «لا۷» ترامپ درباره دیدار خود با ملونی در نشست گروه هفت گفته بود: «ملونی آن‌قدر می‌خواست با من عکس بگیرد که فقط از روی دلسوزی با او موافقت کردم.»
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، در واکنش به اظهارات اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا، این سخنان را «کاملاً ساختگی» خواند و گفت از نحوه رفتار او با متحدان «مبهوت و شگفت‌زده» شده است.
او تاکید کرد: «نمی‌دانم چرا رئیس‌جمهور ایالات متحده این‌گونه با متحدان خود رفتار می‌کند» و افزود این نخستین‌بار نیست که چنین مواضعی از سوی ترامپ مطرح می‌شود.
ملونی همچنین این رویکرد را «مایه تاسف» دانست و گفت او قاطعیتی را که در برابر دشمنان غرب نشان نمی‌دهد، در قبال برخی رهبران متحد خود به کار می‌گیرد.
نخست‌وزیر ایتالیا در پایان تأکید کرد: «یک چیز را باید به خاطر بسپارد؛ من و ایتالیا هرگز التماس نمی‌کنیم.»
در ادامه این تنش‌ها، آنتونیو تایانی، وزیر امور خارجه ایتالیا، نیز اعلام کرد سفر برنامه‌ریزی‌شده خود به آمریکا را لغو کرده و این اظهارات را «توهین به مردم ایتالیا» خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76518" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Put5td7jr4T0KUyyuJ64lnd6qNFtxwrt4udQZEmgN8HbCr4WdB6js5IXJYrgjG7HtiKQ977s7uQOz7dlNhCNXLwQkcAM2l1Cx30OGgf84-TFyoe2YIPKeTsSh6eXBRNAYT0NLAH1zX6GlL664EYJPP7S62GJsP6z6QHA_qXGpCsQm_xtGU-X6W6iuPmg34cXGBkpVRVJbMyqXVhTnZxFAU80xihAr5A1o7UkmGQMPG86NgUBW6l1S4chX2L1mlZ11cVGJQI9-_Rd3GpfkFvA-wt5cSdD1xZ-JMcWyu78G4fXfOd5JssxCLcYeSRX7pDFuN0sGIq9_x6CT5goCgO94g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
#محمد_نوروزی
، شهروند افغانستانی ساکن ایران، که در روز ۲۵ دی‌ماه ۱۴۰۴، در منزل مسکونی‌اش دستگیر شده بود، توسط دادگاه به شش‌سال زندان محکوم شد.
🔹️
طبق گزارش رسیده به کمیته پیگیری، محمد نوروزی پس از بازداشت به آگاهی ملارد منتقل شده و پس از ۴ روز همراه با ضرب‌وشتم فیزیکی به زندان قزلحصار منتقل شد. او طی این مدت مدام تهدید می‌شد که رد مرز شده و از ایران اخراج خواهد شد.
🔹️
او در نهایت با قرار وثیقه یک میلیارد تومانی از زندان آزاد شد و سپس توسط دادگاه به اتهام "اجتماع و تبانی و تبلیغ علیه نظام" به شش سال زندان محکوم شد.
این حکم هم‌اکنون در مرحله تجدیدنظر قرار دارد.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/76517" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76516">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1pExJVXtuzcmUcrtKp_BnGeSXINjDozNKqKqwU4GqV9TfEzppx22uIEsURz8Dt5IbsJ0nIgs6Mn9HLaez2-1qDusME3BP3vRic5XhtWxBv2e1_z3MkdTJHAJkjbTz74PHHCeqqlIEB8N1dwOvQ1eZU1a_jTgse1QpxtABdMSjvpudyFA5dtFQvU-ugiIO2Zax3ndNp4IsnF0dfTYNFuPXeK64MUN21vc1730FJe-bbVioR1ao36yFgOTFi3KgaC-Adq02_OlRHmkrUZDaErFdtQjNwuo1x8ngw7SH8dME7bJvxo08aerefc0IswYJwjn6ilmbBN5aJ13aQKQzst6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز جمعه بار دیگر گفت که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در لبنان باقی خواهند ماند و وعده داد که حزب‌اللهِ مورد حمایت ایران برای حملاتش «بهای بسیار سنگینی» خواهد پرداخت.
او روز پنجشنبه، ساعاتی بعد از امضای تفاهم‌نامه پایان دادن به جنگ توسط ایران و آمریکا، نیز بر ادامه حضور ارتش اسرائیل در مناطقی از جنوب لبنان تأکید کرده بود.
نتانیاهو در بیانیه روز جمعه که پس از اعلام کشته شدن چهار سرباز اسرائیلی در لبنان از سوی ارتش منتشر شد، گفت: «اسرائیل حمله به سربازان یا قلمرو خود را تحمل نخواهد کرد و بابت این حملات بهای بسیار سنگینی از حزب‌الله خواهد گرفت.»
او افزود: «اسرائیل تا هر زمان که برای حفاظت از جوامع شمالی لازم باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.»
یسرائیل کاتز، وزیر دفاع، نیز گفته بود که ارتش در لبنان خواهد ماند و افزود که به هر حمله‌ای «با نیروی قابل توجه» پاسخ خواهد داد.
لبنان اعلام کرده بر اثر حملات اسرائیل در سراسر این کشور ۱۸ نفر کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/76516" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76515">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e-jc49QEsbjrl_0t06BcnuQ99hmkIpcNdhXXSRtVty3wmmzi7-YsUbLunn70v_3RkdkZ2pSHtyr5tAEnsVovsdTYtRGrllTEeMb__Nba5epBteRM46MW-p42P_4c8_MYTDmddWFI3Ee19HEqC4uX4nWQ4hrRXUxLYoTyiu0yd7FjYcUNmy6vpYjvfa8fGnbQN_ylVHzigVGoGlYOPitz-dBZLKc_k18XspSkX6EbxWAfjiAvj1nssgCe1MVQFlqER3MMz-oJWTvR1RK_s_Nua9QhMogliQIwrRC4-ejkdoL4KhGl7AMb1uCI91tfBskgzv7plRYlqoAhpbOUEVHBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینعلی شهریاری، رییس کمیسیون بهداشت و درمان مجلس جمهوری اسلامی، در گفت‌وگو با دیده‌بان ایران، با اشاره به ادامه «تعطیلی مجلس» گفت: «مجلس را بستند تا هر آنچه خواستند امضا کنند.»
او با تاکید بر اینکه تفاهم‌نامه با آمریکا در نهایت باید به تصویب مجلس برسد، افزود: گذشت آن زمان که برجام را در ۲۰ دقیقه در مجلس تصویب کردند. ما یک بار از این موضوع آسیب دیده‌ایم و نباید دوباره همان اتفاق تکرار شود.
شهریاری همچنین از اظهارات عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره احتمال رقیق‌سازی اورانیوم غنی‌شده انتقاد کرد و گفت موضوع هسته‌ای نباید در مذاکرات مطرح شود، زیرا به گفته او «جزو خطوط قرمز» جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 195K · <a href="https://t.me/VahidOnline/76515" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ANTzH1eOWy6O37Hu5EsEOpk8oj6p2Mmv2NmvtMS-gxdAxt72Q6psulaQ56iFaVXEmQjn47PGNVHwyBRBhem5Pn0fbtpSU90ynu6DncLEM6dy1NOC2r9idbcBMnYcL--wDi5riFviENRHOweuxUNmR1qOe_CdfbPRMvh8hzAc07EokwbsoSDo8S41SJpYWeAQKafvRmznll-pkyy7AkKQGo7YFbuTSmf0ksNfzQ-2Hjg-5cNiN3LJ8EhLAhPG852OVurKUVt-QUI_3w5TxfvDdPaTNAbDX3_XLf2VWL88hh89RXiMcwJuElPfZGqq2ACwjBf7fyJkMm6ZBk7o5LAQnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام پیشین مرتبط با تحریم های ایران درباره «صندوق ۳۰۰ میلیارد دلاری»: پیش نیازش لغو همه تحریم هاست که دکمه روشن و خاموش ندارد
میعاد ملکی، مدیر پیشین «دفتر هدف‌گذاری تحریم‌های خزانه‌داری آمریکا» در یادداشتی درباره موضوع «صندوق ۳۰۰ میلیارد دلاری» برای ایران که بسیاری از کارشناسان درباره آن ابراز تردید کرده‌اند، می‌نویسد: با کنار گذاشتن موضوع معافیت/مجوز نفتی و نگرانی‌های مربوط به عدم اعمال تحریم‌های جدید، باتوجه به الزامات برای اجرای واقعی بند ۶ (صندوق بازسازی ۳۰۰ میلیارد دلاری) و بند ۷ (لغو همه تحریم‌ها) به این نتیجه می‌رسیم که مذاکره‌کنندگان آمریکایی یا می‌دانستند که توافق نهایی ناممکن است، یا این یادداشت تفاهم فقط تصمیم‌گیری را به آینده موکول می‌کند.
ملکی که خود در طراحی تحریم‌ها علیه حکومت ایران نقش داشته در این یادداشت می‌نویسد: این چیزی است که «اجرای کامل» در عمل، فراتر از امتیازهای هسته‌ای، به آن نیاز دارد:
بند ۶ — صندوق ۳۰۰ میلیارد دلاری:
صدور معافیت ریاست‌جمهوری از تحریم‌های الزامی بخش ساخت‌وساز ایران طبق ماده ۱۲۴۵ قانون IFCA (معافیت‌های ۱۸۰ روزه قابل تمدید که در هر دوره نیازمند اطلاع‌رسانی به کنگره هستند).
خارج کردن سپاه از فهرست سازمان‌های تروریستی خارجی (FTO)، زیرا در غیر این صورت سرمایه‌گذاران با خطر مسئولیت کیفری به دلیل «حمایت مادی» مواجه خواهند بود و هیچ مجوزی این مشکل را برطرف نمی‌کند.
استفاده از معافیت مبتنی بر منافع ملی در قانون ISA (قانون تحریم های ایران) برای سرمایه‌گذاری در بخش انرژی و نفت.
در نتیجه، هیچ نهاد سرمایه‌گذاری حاضر نیست میلیاردها دلار سرمایه را بر پایه معافیت‌های شش‌ماهه قابل تمدید متعهد کند.
بند ۷ — لغو همه تحریم‌ها:
ماده ۱۰۴ قانون CISADA (قانون جامع تحریم‌ها، پاسخگویی و واگذاری سرمایه‌گذاری‌های مرتبط با ایران) رئیس‌جمهور اختیار معافیت ندارد؛ تحریم‌ها الزامی هستند و لغو آن‌ها مستلزم تصویب قانون جدید در کنگره است.
ماده ۱۲۴۵ قانون NDAA (قانون مجوز دفاع ملی آمریکا) معافیت‌های ۱۲۰ روزه قابل تمدید که در هر دوره نیازمند ارائه گزارش اجباری به کنگره هستند.
تعیین بخش مالی ایران به عنوان «نگرانی پول‌شویی» تحت ماده ۳۱۱ قانون پاتریوت: این موضوع نیازمند مقررات‌گذاری جداگانه از سوی شبکه مقابله با جرائم مالی وزارت خزانه‌داری آمریکا (FinCEN) است و صرفا از طریق دفتر کنترل دارایی‌های خارجی (OFAC) حل نمی‌شود.
تحریم‌های مرتبط با تروریسم، حقوق بشر و موارد همپوشان با پرونده روسیه: هر کدام مستلزم اقدامات حقوقی مستقل و جداگانه هستند.
ملکی در ادامه می‌نویسد: «لغو همه تحریم‌ها» یک دکمه روشن و خاموش نیست، بلکه پروژه‌ای چندساله در حوزه قانون‌گذاری و مقررات‌گذاری است و کنگره نیز در آن حق رای دارد. و این پرسش مطرح است که چگونه می‌توان اتحادیه اروپا را وادار کرد محدودیت‌های مرتبط با ایران را که در چارچوب پرونده‌های مربوط به روسیه وضع شده‌اند، لغو کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/76514" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAdFxXWAJL8bIhMgrvRfti-lxIUQX9ElDnEMEaeCT7rQeiBOuUFRfygS6csqEUDUkM6V_RIh33dgJryZvXISCFqKod371TJS9gt1kHi2183RztPxQHp9eso9znbNa2uzzq-Y9AZ0w86f_kejLg1vcgUvNmQlKnxdDIT0AnuJSGvhoyyLMwYb4cdZCn3bPwgpgmMwMz39dkIy42J4VqPY2j5rl5oZ2ZEe0Zh6ol8Vk0M-nSFotvVa8i_O8BNvOseo3XjP6Edcj6kMkCNLxSTzSZEBYx0stBo-XdMxRHpjobss2zdaUx7gfpiGfh8_CN0icC1GuThFHcmX55BQEHmqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه هاآرتص در تحلیلی نوشت توافق دونالد ترامپ با جمهوری اسلامی، برخلاف انتظار بنیامین نتانیاهو، نه‌تنها به تقویت موقعیت سیاسی او منجر نشد، بلکه شکاف بی‌سابقه‌ای میان واشینگتن و تل‌آویو ایجاد کرده و نخست‌وزیر اسرائیل را در آستانه انتخابات با بحرانی تازه روبه‌رو کرده است.
روزنامه هاآرتص در تحلیلی نوشت نتانیاهو امیدوار بود سفر ترامپ به اسرائیل و حمایت علنی رییس‌جمهوری آمریکا، مهم‌ترین برگ برنده او در انتخابات پیش‌رو باشد.
به نوشته این روزنامه، نتانیاهو انتظار داشت این سفر پس از «پیروزی کامل» بر جمهوری اسلامی، سقوط حکومت ایران و انتقال ذخایر اورانیوم غنی‌شده برگزار شود، اما اکنون نه‌تنها هیچ‌یک از این اهداف محقق نشده، بلکه ترامپ تقریباً هر روز با اظهاراتی تحقیرآمیز از نخست‌وزیر اسرائیل انتقاد می‌کند.
هاآرتص افزود توافق آمریکا و جمهوری اسلامی در اسرائیل به‌طور گسترده «فاجعه‌بار» تلقی می‌شود، زیرا ترامپ برخلاف وعده‌های اولیه خود، جنگ را بدون تحقق اهداف اعلام‌شده پایان داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/76513" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIGcLcgZ_Hj4H7TBSPyy1inG8ebx4ubs_whiTTtq1rM8wCOaGLo9WV6c5Aw1bV-g1qwzcDsOuaNhs7Yf0U6AKDQL2JSrTgOoQzlgvTDbgpzqKdk-qE5EkPRLzP9oJmNUp2ck0og3qnVLCQi1WgP_dh0AO6I_xFnylihbPqAe4y4mlLzrlmClM2oSq8DWueOHg7ozCLlVQwfAgYYGduvQwHt1-yvF-jbwmHFH3UCHStvTw6BiJE7dEQUZPsTdBGslUxUa2ektZrv8GnxJUo53bWWgqLnTTLx-V_6vxDcusXHB2fsg6aaIW_HXGZuFaHdeMgzL1i43SYnbOJkOyxiC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«معین بصیری» ۲۱ ساله، ساکن شهرک اندیشه تهران، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله از نقطه‌ای مرتفع و از روی پشت‌بام شلیک شده و به قلب معین اصابت کرده است.
او در پی این جراحت جان باخت و پیکرش پس از انتقال به کهریزک، به بهشت زهرا منتقل شد.
نزدیکانش می‌گویند پیکر معین بصیری را از بهشت زهرا تحویل گرفتند و مراسم خاکسپاری او روز ۲۱ دی‌ماه برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 187K · <a href="https://t.me/VahidOnline/76512" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DPRmGC98357CSDd-qYVIoeEyVT9gcaKFbc5dyadTEYivQ2PSKzgQyRvkIxupqRzlQ5YDEp2BottJKUyDxYUBwvAR5q8jjCeGpWHa_YMCCMT7Ch6GW1hVWHtQqrbD7qQoUzhxhDEumQdpoqB1QRbhIfkd9GuToJbTPj5ec4EGb_lNeSwJ6t38PINAmGuNE8o5UhAuHnWjqAliSjDfIZPo5caRZPr7_c9tZuKBhRo_vQNj2RrNoAWOzDt6W3pclGs-ocA9pfvJTqIwax8aCSidtolHHFZ1Jxnk9LkvIs3IQUafntrs2qDtPuOP5d6hd687M91Hr-6mm4Rcm_JYYMLMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
«جنگ، ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات ضدهوایی، نه رادار، و عملاً هیچ چیز دیگری هم ندارد؛ با این حال دموکرات‌های احمق می‌گویند ایران الان از چهار ماه پیش وضع بهتری دارد. اصلاً می‌توانید تصور کنید کسی با چنین حرفی قسر در برود؟ بعضی‌ها چقدر می‌توانند احمق باشند؟؟؟
رئیس‌جمهور، دی‌جی‌تی»
realDonaldTrump
«ما از سرِ درماندگی دیدار نکردیم؛ ایران بود که از سرِ درماندگی آمد. کارشان تمام است! این ۶۰ روز را هم طی می‌کنیم. هیچ پولی گیرشان نمی‌آید، حتی ده سنت!»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/76511" target="_blank">📅 17:13 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
