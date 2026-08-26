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
<img src="https://cdn4.telesco.pe/file/XjeLtBYYcbukWyZxQEsOZrPo92up8E-43-Y4Ed_F5q82qrJ4E7vmMjm7oBKaFmr8uj5Cd0f9f96N5vnVy7GrRV8mt1-gryKsEJ7GY_-uX4n54NV5rlN1xGO6Yxjcz5JcXPJPIhchfsjMjGqv6jdPhDv-Fgk198m3IqV5QjpWqdWTViIpqt5PC6CxKBauPuCCLi4CIC8i0214k-jv82m4ZcDxhNBPFegq3r3cDDqNImvS7zfO4HesJ9KoTHmiMohJN2fdCMztfmQAvreKB3XZlOmzuZAz95AEdALqFXtna_oMl0Nck-YtMxH2Yv2Zp9nOdlOiJJXzar7LFeZvGMAMsA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 623K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 21:39:48</div>
<hr>

<div class="tg-post" id="msg-28540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUV4cRuZb0yKpjHXQFYkfLTnKtqkgUspZPGUasg2TSPlhZfml-gPE4WYCW45Z2Bcqu4rRxIbAzHClqYhs49EfcdTyXMLDhbNB_y26mS4q_3LBCNxGzxZmgJpxn06ZYORhVJdbXV_41kHQqf3GEYkTAJHGGTobK7HOx05kpblgY8HBps4KVxczKRGiEu8wOj7RHZ5ZLlt15iM66_Ij3XMgVeCsDXkp7H5OWE5m0d86gr3Z22lEBwkpkcu6TjxTB5DkAIhFavMFYqDZtLlrXRFYyq4AC5w5pQWnZoVbqseqwZqU2tsACkZJx1e0L8K1vt34s5xVIq8e2kFIm7dL7fHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/persiana_Soccer/28540" target="_blank">📅 21:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28539">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l02FQgFFRp58fPQamp_-gzxzkDV_1AMtqikpMYSMUe5fE2xewN6OZyTJj3emkxEa3ROK4NX2K923wPX4yHk6kZVdLeiokP1ntYeHEXY13g6H_YgZJeZvS61IC5dPgwhRfaAKXFfFJAXE8BHcu7gonoW5RGSsetocQ7VhdAmCngYSdFlw8-m7ZOtP85YBZCEtMDwFtjFqe9li5FlO-kRU9lmLppcJ7WvB47-Kdmtf8qMGdtHb8KAerZPex04JU4JIE1QTnXXTVRgvm5bnVm8a0uT68LNnBBTTBTuDxO5PkhJ7Go5D6HPW4CJGgfe2HOyTZ1ZZJPMDCycSvRU118P4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مقایسه‌قیمت‌دیروز و امروز پلی‌استشن 5، آیفون 17 پرومکس و سامسونگ S26 اولترا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/28539" target="_blank">📅 20:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28538">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmSVsPABr6lPpmg0zm_1Wz1eV8z4jkF0PDfrQReCn0zZs-NOj9h5yKiP9gRmcJCDaNryMTLT_QT5igYl1QjZyZJ5zir1Z1ZK3OYYUGvuSRcKweSIQSq8zOQuBNDpUG9xfrJFspRd8QuJ-pc1sJoD5XtwpKsywuURDxwDBJa2ZTxHYR2vAPetdM1_7dgbxv9HVfpuQsM9hFudVop7Iu3MBTdt-l6RfzAO1EwEpyNtNRUFje2ePDbREbA5oTj0H2OHqpKEHO35QP3cgJ0x-FT29UFun0CIpvF7g8Nn4w4yML52NdPo-cEPTvqndRx8Ae8PODwQKb_qN_-Shn_9GoVQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/28538" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28537">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03aba91807.mp4?token=k28jhiiqlssoqoa1mucgyu6jZKhYZol7WNbrtrP0PqfdmvMoZwu4nDt4Ahcl7oPdXs0I-78jTRtIX-BAUsAhXlJ-uUwb-NbayuielTH-vR5RwBTHmLzWVu3Wmz07rn6x4__QNuY_h1_FGqaql-6ngPwLsxaMGswQdxILERA5G6vVMDApxQvNYyIoPEMbHsljBYFNTwiggHzxTD2omMsg3SCcYxpbXAtaIzQNlrcm84sA8ENwhktqVGW351NGVpd5zFFDC-i049Gjymc_8npD8H-mIZgms2_EGR2HdIjR9-UwIv1ZfndgMfnqHSGKHvMrAjS0nV8DbGiJ-ppfakEleQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03aba91807.mp4?token=k28jhiiqlssoqoa1mucgyu6jZKhYZol7WNbrtrP0PqfdmvMoZwu4nDt4Ahcl7oPdXs0I-78jTRtIX-BAUsAhXlJ-uUwb-NbayuielTH-vR5RwBTHmLzWVu3Wmz07rn6x4__QNuY_h1_FGqaql-6ngPwLsxaMGswQdxILERA5G6vVMDApxQvNYyIoPEMbHsljBYFNTwiggHzxTD2omMsg3SCcYxpbXAtaIzQNlrcm84sA8ENwhktqVGW351NGVpd5zFFDC-i049Gjymc_8npD8H-mIZgms2_EGR2HdIjR9-UwIv1ZfndgMfnqHSGKHvMrAjS0nV8DbGiJ-ppfakEleQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی از سیوهای حبیب فرعباسی دروازه‌بان بی ادعای استقلال در سه هفته ابتدایی لیگ برتر که سه کلین شیت برای آبی‌ها به ارمغان آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/28537" target="_blank">📅 20:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28536">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=pQ_vbqOBQypj-tqg-1ug3bdTqdecush-ortLKfqbu0BIZslYHPo18ddoxkGA1CDkLBk5fzOWyOPzrePiJ13pzb6NCK2DcVy6EFtLcExinkXU1e1Vn28zqcaGjy4UdSqHOG6iNLXZC4p-C3rOrW_aYx5Hb3mr64mOCfvbttvwFmxj2arA1GMe3miLyvxE177KxoCiFgjbXFTYd1OgeS8z2c_jMSeHd3-o4Zow4734B_RxTxxE624YTmnHqkdRFEzCuvWL_UMWrV-CjAGCcXRsUn6G94JPiwOSY0f0gbXrYa0WsGnnKpTLum4EKRJvUrwo4EzmaW6e8oHjfM_KWLcAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=pQ_vbqOBQypj-tqg-1ug3bdTqdecush-ortLKfqbu0BIZslYHPo18ddoxkGA1CDkLBk5fzOWyOPzrePiJ13pzb6NCK2DcVy6EFtLcExinkXU1e1Vn28zqcaGjy4UdSqHOG6iNLXZC4p-C3rOrW_aYx5Hb3mr64mOCfvbttvwFmxj2arA1GMe3miLyvxE177KxoCiFgjbXFTYd1OgeS8z2c_jMSeHd3-o4Zow4734B_RxTxxE624YTmnHqkdRFEzCuvWL_UMWrV-CjAGCcXRsUn6G94JPiwOSY0f0gbXrYa0WsGnnKpTLum4EKRJvUrwo4EzmaW6e8oHjfM_KWLcAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد رونمایی از اولین آیفون تاشو با نام اولترا باشیم. اما احتمالاً خبری از مدل استاندارد آیفون ۱۸ تا بهار ۲۰۲۷ نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/28536" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28535">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_aOKQRqVglyn6qnaNtDI3BHsVFmNpcudbDpXt-NuYJYMcZ8WoLS7H09vuJMoWFAZU7PMtUrv2zaC0pwYszLAWNYMrhLQ97AaBkFW-smLvXQ7eOtKICdI7mb1y7ZXe0TUGy6hPSnKy3sW7MN4bih4dUNM_dGsQETIpUMlzYtG5c1MKDimJ6mx6zay-LIjA7elcZPYFZ-RvhmPkO8ZDF7A3oJGZmKZYS6EcpHYQwBR3msNR97LW7U8SIIde_3-dfcFqyRs85N7vXxB2llkjscCKCBdNgSgNY4KYhezf5ftcCtNGsFGzgFuvd3BDlGLP4a_GxaeXpDFzzY5HG-I56xxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ هکتور فورت ستاره جوان بارسلونا در آستانه عقد قراردادی چهار با دورتموند قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/28535" target="_blank">📅 19:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28534">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=Ou---jP1bEGLeZBa4X6SQD6ld97iRKZEDUgrlWdfFjwZEhte6nKntAX59xCBx4xOBn4EhEo3qrJnMJE8uxE1_kTBrc4RBUvRPdS6mFemjNx2981ORDxP0bRKlzuv4SumvfTa4EoiYG8tK-Ey-BBhZeD8q89T0XtNftLiMovFEWVtqtW3ew8We7rAaK7I8XHdEobSQRsK0ZRlK6lrDmgcddXxDMpKsvxA7VwJcapGSkCNpfwJyduxDRvGjb61UMFLuTzmSXvQJfwf4g0vv5DhBaKdY5Vt4c9czPPjhjZ5smkM9nje4UzFGpWbydYh18a0X93fz8IMT2t7lkRN7Sr2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=Ou---jP1bEGLeZBa4X6SQD6ld97iRKZEDUgrlWdfFjwZEhte6nKntAX59xCBx4xOBn4EhEo3qrJnMJE8uxE1_kTBrc4RBUvRPdS6mFemjNx2981ORDxP0bRKlzuv4SumvfTa4EoiYG8tK-Ey-BBhZeD8q89T0XtNftLiMovFEWVtqtW3ew8We7rAaK7I8XHdEobSQRsK0ZRlK6lrDmgcddXxDMpKsvxA7VwJcapGSkCNpfwJyduxDRvGjb61UMFLuTzmSXvQJfwf4g0vv5DhBaKdY5Vt4c9czPPjhjZ5smkM9nje4UzFGpWbydYh18a0X93fz8IMT2t7lkRN7Sr2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صحبت‌های جالب عادل درخصوص یکی‌از پیمان کارهای ایرانی استادیوم 105 هزار نفری نیوکمپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/28534" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28533">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4qqFdrJFsCao6fUG-Lfu0OTBtT-8f7Z-rhFuoDzUOMylIn3xxx50rGTmwcRet8jpFOTSvytx3dnuWNuE6Z2K74XYfHYzuFOCsCb3toh7Jsd7tC4MBLmVxuedo8y8f4o5Ba048nqyJLgAwZk8mG5pGYOwjdOeod6fNUUQPZZN9gU4gOuefU0iSox-4Z0FvmwdjrFI2yh0fmLFtbYCI3AG7f7pnymq1SGnT_fqqv-PaPcTa3nDH9tcWsmbDThBiIRRIcqWJEbnUNpj9FXCBJ5LnTcVXmBvhBaOr_MxfcEfzmLw97ympH4CPCeOI6HzEyQkKi4ENDN1uYlQAO-dlL3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عمق اسکواد بایرن‌مونیخ در‌فصل‌جدید رقابت‌ها؛ این فصل آخرین فصل حضور نویر خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/28533" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28532">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLa1tLP_9rF6o9a2pMqB2gRwHG82tIoEWPgIFwhwo098nn4_WOrEj2pdQXPIA6wNeW32vfrfvB8Yw6yWtgjJsHb6bEEx2viXRmLWhVTfrB6RaiGpKPFNPOYxOVKyMsOWGW6sKyQaq0t3WIAZzmPCUUwp4JrxVd8HZYkov8k4i3gS6l3CJBBarAT00QWwdpjPL7gXYC3ItuDZRFQYCtfWMXtDCkkVSTQ-7qKjYro_ayuJRRvXwx2N9_Zmx4KsXm-Zl7tDScVQDa3gzmvHs7-D7jyh_xJFTqv1MSLkxTk4mlOXa4YSGOlse_TDw7ngI1N-LGB2YWRsKgbrv63dd_UxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پلی آف لیگ قهرمانان اروپا
🇫🇷
لیون
🆚
فنرباغچه
🇹🇷
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/28532" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28531">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSkzQQYTCdoqPOchKV0DhBo8nlhqCizIYQDdSHQF9zWDyEwjSULacmrooYyOMiFi0hUgMeHA9nCnK4feXAcJcklyKdcJuzHsnuLP5M_LppHGcF5jfqnQjBNwmFJdbwQhrDeB7_04cjD1aAX77laD92bkdjO_GeGeamhNuwWeFrw5nXK0OruwgGtZbT7Z_x4cNUSB0BQLIFx_Wvr1sP6dASIGv3_BQ11OunEMpm8x3kuzJbLI7ERlVqtXE2CIHZR6Bd8axBna5NbSPBhESA_qh8oT9UW8BGggka8wRg7o2rTftjs8Fs8imY7WzUcxUwTOA-iRFuSTPYT6E7yUMygCZIaj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSkzQQYTCdoqPOchKV0DhBo8nlhqCizIYQDdSHQF9zWDyEwjSULacmrooYyOMiFi0hUgMeHA9nCnK4feXAcJcklyKdcJuzHsnuLP5M_LppHGcF5jfqnQjBNwmFJdbwQhrDeB7_04cjD1aAX77laD92bkdjO_GeGeamhNuwWeFrw5nXK0OruwgGtZbT7Z_x4cNUSB0BQLIFx_Wvr1sP6dASIGv3_BQ11OunEMpm8x3kuzJbLI7ERlVqtXE2CIHZR6Bd8axBna5NbSPBhESA_qh8oT9UW8BGggka8wRg7o2rTftjs8Fs8imY7WzUcxUwTOA-iRFuSTPYT6E7yUMygCZIaj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/28531" target="_blank">📅 17:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28530">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7ABhuDYJDP1yAUhOcwFYZhbnXdFwX-GBP8oVT-imkZs_34P04gS0rHEYAHpC7l8XaO3Frer5z0X0wafH3bsdePt8pZcVlzBBo5DXYbmtTMDPiz4R3vXfoz57yWxnu17aqTIyE50JqUcbfxoQKX9M69SYEfemqeyTUVFBi5vVntSdTDFaAtiI67uMTy7qpWig0OnKV5FZlt-D9k9cjFe2h_a0X_8cvOTiyhhJw4PqlgDvHk5T7ChMdXs369enfL1X_p5NIhmp7JOb-EJyvirMtVRdYeD_8QWvqmNNhhYomCZieVndqXw6FpmZ9IpmJwMqAyLPMLCORnqelegQmi88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/28530" target="_blank">📅 17:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28529">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=lLbbdA1yQ4-tJqFLdNycbump89GA_lz8nI5ZWvHDzdzXmkHQqkFta8DGj8Ib3znZvI-F8IhrcIXHsiBV4hsY7DRSdA8riO7oTaSD-F8QLjGIkMRVRGhGQ80yug_BqRUefFtG0LYHEul19R5oH0YYby6Eo4_W1iDiCMMZmTLJICAuggZWBILjoYTVd-ayyYQTrtYJ8sMFeyapkBt-mEV1O0Zi5QyZXIftoirtNN3ATeH5vrBc074B8nKaD81ilyTMe71EfCUuMDFWh9fuvPm725sC9_gFbWzVIF3ygHGY9VfjSl0UQdAZJFXnZjxjaDQjr4QFLr0VaqpKe3K_he7IQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=lLbbdA1yQ4-tJqFLdNycbump89GA_lz8nI5ZWvHDzdzXmkHQqkFta8DGj8Ib3znZvI-F8IhrcIXHsiBV4hsY7DRSdA8riO7oTaSD-F8QLjGIkMRVRGhGQ80yug_BqRUefFtG0LYHEul19R5oH0YYby6Eo4_W1iDiCMMZmTLJICAuggZWBILjoYTVd-ayyYQTrtYJ8sMFeyapkBt-mEV1O0Zi5QyZXIftoirtNN3ATeH5vrBc074B8nKaD81ilyTMe71EfCUuMDFWh9fuvPm725sC9_gFbWzVIF3ygHGY9VfjSl0UQdAZJFXnZjxjaDQjr4QFLr0VaqpKe3K_he7IQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/28529" target="_blank">📅 16:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28528">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQngA9d8Hcnoc-fzENA_LtcDxjs2EPfpCAhTJEcuqUcpeHRjquKj3UiosdzuKCc9xNTupvBFnedQDTRpRiqccuPGgUndXL6qHaL3mA-k806mhI3DPIKaXz11PWBNq4_57Pdls9ueSkFLUFPyLREajAElEoKE41eugLTx_ujdF5OnWEdHBlBY8mrmzOSBVoYlyq86e_OC0rW1DrDhiqyCmQuvpA1ICJXFftgdHvL8qhFCKDuSQqMVL2QMXQA-bVfkUmEjYHKNeL0ABtkoBMbAUp2Dux_emB_LqA1v8yZ_earYBERZWaljYlpOM0WxgtqXHSHlFNFwuG7Y9rQt4dKhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌روزپیش‌گفتیم‌باشگاه‌خیبر قصد داره که ابوذر صفر زاده مدافع‌چپ‌جدید این‌تیم‌رو به شکل معاوضه با حسین ابرقویی‌به‌پرسپولیس بده که همون رسانه‌ای که خیلی‌ادعاش‌میشه که از همه چی باشگاه خبر داره تکذیب کرد و گفت اصلامدنظر مهدی تارتار نیست الان زده تارتار گفته…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/28528" target="_blank">📅 16:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28527">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWibeUhgeDsjs_N9EZH8BRvHxt8K45RS0tGRoyxWJ4Fsd6e_keoW32V6P6bn_gE4rvJQ934A2ncI1a6t8b6s5cjaOFhXCRr_YmyGhf50yekiyrzmhpVxAN2UCeacsb8_knc3XYGXstfavbqjyEedPJ7M8u_xsgcAF3sf9Ckwbv_MpmBWnXE_WGYWSJBVJAAQ5OsTbjlM5OrXqKR3T-irfuzxvJ1HwpKCNp--z3FmHr9GkuurmfKE6SNZbfJ1H7mg3O2LrD3vaCv-lHEVx2ONCYCZqMIiisHM8M3jvBJyUAlFuYHktkxxk3SE6gFerqcDJVdILd3nlgeCWL3usLnmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/28527" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28526">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhtl2nOFMkMnGtRB66siXdc8zamk7Cl0H-qO7A_KqJb-nPicql0CB7wWFe-TuoiD6jB0hC_DpLfMVNkK6vD6xxC-vRFcpgqhiiHQwIq4R7rg0WUItajx1p7H0jvz4dmUSEB9vhNUMwIB3iLf7ZgXIfoY-y5JdjkKIFKpX9drZM3FwEe15cyJp4DTJzqVLCWhvUQQ-0uPdQJOuEvuC5NQUL37G2yOf94LJ-hYbkHQiZucvOYbEJBSjKsiQF1uUP88p37wnhfGCF7hEEd_eUySbLNI2ReWUFMPQ1GDODQLDqvpg_y26pmfCgRDCtyFNRH-rZ6RezP6UtItSy2wflGq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل شده. زنده باد مادرید!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/28526" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28525">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDMSZhXqv4csaECS0RGzk0-kVgIozwKIJnoKxU6hrKYRdWLvZ3Xv6bwJ_tXUfOxQi6gJblV9DRqI93TNnY_eKFQBgYoejANdy8Z9FC1UBjE5tzQOsZ0k7a4wmfqYA1zbSKT_I49sEL-xK-HveRevS9WFwmb4Tc45yeNazm00VsEoTvpN--Ym6IaDZy_LQibNy5hl3buPJZvowdz3nnAmfmwK3DWANqwZFLQrsHgBs9NIbepgQMNfT4mtgz0zUx_xJM5y4qtlho2m69HeVtN2JhPtky8J-Mj8yRPefL100TTEbUmYt2plvvRRplsotXLZlqewOTwhXzQfNjuCNUalZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛نیمار اندرز مدافع‌راست‌سابق لگانس که اخیرا با قراردادی 5 ساله‌به‌استقلال پیوست بعد از توافق بین دو تیم باقراردادی قرضی شس ماه به اس. خوزستان پیوست و نیم‌فصل به‌جمع‌آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28525" target="_blank">📅 15:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28524">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=n5I0PIxC4SmTzyduawhy2ljSfOA8Z6K8XuOVU-pr8ImNfQsLq08DR4DFNEhwN4EplYlSqDVxLl_PLhtJB87QaJAfEM16gFZcGIVcu8rFkxCA1zGL-wjiPdLLELv6z81mX5ZBr45uQPul3qJt53eVY24kDq7BpD_YoNW9A5Am14dls-uwpsoJKdKwJWDYuvEW3ZcYgaDg0xgSoYrMKerghm5ZqrRdOWCmhBN2X_KpF57uxiZIz87Tly6MgdiggsVXTvSGarS-in2kUA2vTb1TRn1nReKlb46Wrx0ukoIcWKb2hOq7nT2g2lMHoXgVWSmqLhie4A5kF6qitJQyufKXnp6aiKUiQje3yJNscaqzH1ENHJlXLpA0x_jOdFxLIUoQh4KTiZ7nmUjUCj49lA2-9zEp0ytR2pNrdANqHjF6N0lBbjuyk2hlQC9ybhBXHJAjQOjIbHyIkBjwSHD7CHv0Km19LPLhQtVKyibku2ct4VpYIkuswv_j2apDI3JxAUquLWtMeHvMcbUGgGWxFYAtEl9BI0C-5CDRPc3beK9AQUl00k1JrP2-afuD9Kxbw-NSjlfPb8Wmzrn-GqJbNoVrdFaQzTXaFNjHeVSIc-bIg6P1WWKM0r-fHG9OqMy2_JtvbQxD5pv9_Q3_7t2OR1WWI7MHXK4_GgExSIFZfpwvSn8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=n5I0PIxC4SmTzyduawhy2ljSfOA8Z6K8XuOVU-pr8ImNfQsLq08DR4DFNEhwN4EplYlSqDVxLl_PLhtJB87QaJAfEM16gFZcGIVcu8rFkxCA1zGL-wjiPdLLELv6z81mX5ZBr45uQPul3qJt53eVY24kDq7BpD_YoNW9A5Am14dls-uwpsoJKdKwJWDYuvEW3ZcYgaDg0xgSoYrMKerghm5ZqrRdOWCmhBN2X_KpF57uxiZIz87Tly6MgdiggsVXTvSGarS-in2kUA2vTb1TRn1nReKlb46Wrx0ukoIcWKb2hOq7nT2g2lMHoXgVWSmqLhie4A5kF6qitJQyufKXnp6aiKUiQje3yJNscaqzH1ENHJlXLpA0x_jOdFxLIUoQh4KTiZ7nmUjUCj49lA2-9zEp0ytR2pNrdANqHjF6N0lBbjuyk2hlQC9ybhBXHJAjQOjIbHyIkBjwSHD7CHv0Km19LPLhQtVKyibku2ct4VpYIkuswv_j2apDI3JxAUquLWtMeHvMcbUGgGWxFYAtEl9BI0C-5CDRPc3beK9AQUl00k1JrP2-afuD9Kxbw-NSjlfPb8Wmzrn-GqJbNoVrdFaQzTXaFNjHeVSIc-bIg6P1WWKM0r-fHG9OqMy2_JtvbQxD5pv9_Q3_7t2OR1WWI7MHXK4_GgExSIFZfpwvSn8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
صحبت‌های محمدنوری سرمربی صنعت نفت خطاب به بازیکنان در رختکن به سبک نقی معمولی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/28524" target="_blank">📅 15:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28522">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUpdZTADbNCgdb6qvd3TD0Xwu9oawFYpA9cHZGYlMQYJsaOacqLYzcEbE2DbWd3TEXGJs6SPdscS8YW9a5iown4eV6WguVhCLqI2P6t2-aaXDKw6qN9LGx5JBlKhKkb7VNdrLagE4GCalbtR15j0SXldrOXcWUK3mAfufrrJQ7x8Cl5t2M5ehThnn-wPaT8swl0kZycG7Q-sJgRrVoj15GCIhw6aR5SchDiXmrb0m9Mk3fML5Yx3K0S53TgjhX7nsGqwV1M5WPfo2yzmtsYR3MHw1IGXu9aiPUOUnvbvtNqKB7bMqRBtQqGAbU9hYAruKu_oiPskYukUJzy9Sj66Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaHkp0q2ZpwPPIurcgvOvTUc8bEKS20fDwBBxv5HdYiA3vAgDQvX22duREQYIgzCCfL6EvXK52sonYgGRkj2KEqsvTjil5oIsKV_gv7perGKfnXVlnXpyziELnQNqS6bItXr7fbK2KprnXrL867RTYF4uv0FlFtotUEIyAJbErUkmqUlmBc_4fYRlIoREtWXkoRzBCt_yXvmQvEx1REZu21BFTQsfwTKb-e-o7k3aLGddYlDjUBAysbswGev1Pw_owzc5U1jBsVEXvQAd4nOEak2nPcW9PDiB8CP8lb8s0ZkzDB165RuMjsjOPhspGPo37gTnmRzYJMFU1OfFZCFkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/28522" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28521">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOzANpcasWpaDtG07eMpwY0QQbiXkczGsNXXCEY2aHAK5rwYWyQr_BsuQYo0SGqCXS6onmPSkK-dYdktXSr_NXUSAGOaO5x8oAd9Td-Vc_mlDQ3DffjOqBUXU0WYfWz27gp8LlZuxkxcEY5FVkFkEfz8ayyqTLwATEAuVIdxAwXQEevXlgxfuknFc9QdqMMe24KoV9NdvbyjcT_if_pLA1e9DrxSYW7XBDkrhINM68yNRDVADflos6KdRAgmpRSOdLvu8H5VnK95GIX4xDzXUjh7roo6jReBzY0Lqn1punff7sw7j0_vdqktt6DV2Dj4LPFWAnWbFBsSupoq5bRfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحاشیه‌دیدارهای‌این‌هفته لیگ‌عراق؛
یه بازیکن عراقی بعدگلزنی‌واسه‌تیمش لباسشو در آورد و دویید سمت جایگاه تماشاگرا تاباهاشون خوشحالی کنه ولی هیچ تماشاگری تو جایگاه نبود، بعدشم که برگشت به زمین‌گلش ردشد و بخاطر درآوردن لباسش کارت زرد دوم هم گرفت و از زمین مسابقه هم اخراج شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28521" target="_blank">📅 14:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28520">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8oTVhY6uLsn-HVeLuHRZA61VbUTC_4I02wYP4LE8S2TqXZ-o0rNeGBDED_cI6MfIzQn7xgBmSVVDFppze2WxYI_m_bGM6WPAhEVavnBZSEK6EZIghHwN8MxlXbCsCfT6MV2Q59ir1Hw2uL-0DkcWVgnKYbcdT01IBQ37j_THUrbEHCxIyc3QNIXR5L5UxKvrNJAzOvkgB6h_gZJKOnIbdBCTvfZbFYxzHAWLQ1OKN83Kz_MJdK7OiG2kOY6wyVmvZyov8FwCfSYpc2GQyUvnsvPfLU3tuw10QxiT7fALM4JP7qAkvvFdGtwvdYmTwbn9o8u0Z1YoGIA2Y2uajkqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان ستاره 36 ساله‌فولاد از هواداران این تیم خواست که دربازی روز جمعه مقابل استقلال کل ورزشگاه فولادآرنا روپر کنند و از مدیریت باشگاه فولاد نیز خواست که بلیط فروشی رو رایگان کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28520" target="_blank">📅 14:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28519">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTqvw8m0_mpT1dSX8YNQM2lTFAy6GEHHI_f3qmyB1oJxPFpyygW0-LS_QfvmmRYeDKjCxvuYuIwrETtR71gsqMERgeoTKb-UndQVUgxAu8iQBw4U3TJn45_zmxkNaSMeHeGRijCYHjB1DZFvnOW55MKmE9GitdmUoC-FHxNsFLbNjSKbOUqLd50-WKCd7JE4Ti2WR2Xss64IW_4OeA6fKw1zmBIYbu2eUcE3aAox6pfusyDvWLdQLZ8FCkh2UC9rmk_LF1pFqcJbAx5PokLFuK5WLrK44wWeBuAaiGYBHzOAXZfQrUIftAkMqWCKGhDDFrTQJQjH0kN2XDoXfr20Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دولت دو کشور آمریکا و امارات براش ویزا صادر نکردند و مسابقات‌جهانی‌مستر المپیا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28519" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28518">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSiQ3rEwatCE1nGxHOzkYZYOvrvHjIulvArJvsreg9K24jjQUBElEICILBcx7UIXHsGQTFA79b0Si8APVvLLCG-KCrSAL6f9FcFSDo74Pu4I8Fkt8jszHGnymj5JvNj8HIiighmZNd9BbLE1v8ZodT1UJSLMsEKupIvG8Bnq1AZbDHRbWbCBXUM3SLk2pADSD6QeNeGxNg42U5dRjw_Xe0-d0IzrJhSvJeGdM-SkGaiuTC9sE0tacFgVKik_JkPKRIlr2EZXgIrG7rLEl_H-0q3UuoQh5v-50TU0DZ9Y3hA69XPFth-VoZLIKtBsJTbg9_ePCxItjtWww9Bi0syUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28518" target="_blank">📅 14:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=YHcdiwNuUluOnsJtpcEtLk6-smcPHfSytAtEAEg_FAnOM72GyL4MHWh6AG0y3ojovhtSKGDLwBj9R6Byz7bX5UKxKAZHy88LRhEXF8avERCNQq1xAUA9yO11eFVUfKSwyxqp919ewgs84PV0mVe1ySHK27Hfe1coo_n0NAyhGDXJfOAxoxKXu6XSlEUbJ5HM1RdObQLuoHo7p6Qve1v9sPNdRGFJt8Wv3JxRzmdX0SUmWzay3-n7TMHi4cbBA4EKyFIkbeyV54NCjix-l4hW50mwREvSD9taeJVjLUYHZoZbFRGC3s0hyEFdZWp_HVJN7Qp7b9QVcbEEc1mTLpUgzilGoMexelqb-d5HxquFxcKL2z6NR8tRpkx9ub0xX_DSGSx_clCWeAQliv-t5SeTSIceDQNB8k3G8apmcEAHpHkOZaFsaBMaYz4lplDiPH3OvWMESu_LwLx9ADockprtXjgwxwmVDni_cWarFOhU4rXjzmM3J_bP2qm2-_9BnKH_PBrrYefDHr5oERHsGTxjGhB02dGg7B4QQ2txoAH_XXA9opPLwAEjx0tGU7GFMFgATt3SMvhz8LBeMxJoqE3cRJYwZ5pMG0VG3mujb0OgVysS9MHjJwT0AcybdA4a6prQFUuC_yZnxT0hNjJwB500VncC8_8HQCIEIM1hJKpqL20" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=YHcdiwNuUluOnsJtpcEtLk6-smcPHfSytAtEAEg_FAnOM72GyL4MHWh6AG0y3ojovhtSKGDLwBj9R6Byz7bX5UKxKAZHy88LRhEXF8avERCNQq1xAUA9yO11eFVUfKSwyxqp919ewgs84PV0mVe1ySHK27Hfe1coo_n0NAyhGDXJfOAxoxKXu6XSlEUbJ5HM1RdObQLuoHo7p6Qve1v9sPNdRGFJt8Wv3JxRzmdX0SUmWzay3-n7TMHi4cbBA4EKyFIkbeyV54NCjix-l4hW50mwREvSD9taeJVjLUYHZoZbFRGC3s0hyEFdZWp_HVJN7Qp7b9QVcbEEc1mTLpUgzilGoMexelqb-d5HxquFxcKL2z6NR8tRpkx9ub0xX_DSGSx_clCWeAQliv-t5SeTSIceDQNB8k3G8apmcEAHpHkOZaFsaBMaYz4lplDiPH3OvWMESu_LwLx9ADockprtXjgwxwmVDni_cWarFOhU4rXjzmM3J_bP2qm2-_9BnKH_PBrrYefDHr5oERHsGTxjGhB02dGg7B4QQ2txoAH_XXA9opPLwAEjx0tGU7GFMFgATt3SMvhz8LBeMxJoqE3cRJYwZ5pMG0VG3mujb0OgVysS9MHjJwT0AcybdA4a6prQFUuC_yZnxT0hNjJwB500VncC8_8HQCIEIM1hJKpqL20" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تقلید فوق العاده صدای گزارشگرهای فوتبال ایران همراه با نظر خود گزارشگرها درباره تقلید صداشون. جفت ویدیوها عالین حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28516" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28515">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLv0ZJL05F6gxH5HV1Cj1JGbBNB7zoRZ7lSPQejQ84vnyOqfkrn9WdlaKZTdvJxpci74qRSjHo47KTTZw0KpXwhiLWBz7C_D2J8hChAq7MbwpvfjNjew7PoVULNuHO01ikirx2GvGga2DKOGIXTn2HzdU3fDIHLiS7zMEfiVvjZNqInY7DE-1fiC3ISDvuJpgy0PdE70cik5r7FfLlheSyhJatZ5Uu8stIeZY95nwqqKC5XuxHTCyV6C9fwMraVGTvkfcZdRjG2CAegXWg_TPZZ8aiUmvNzZX3pxe7wsEmXE3aPxmYdGuLdcI_KmpU8agQJgOQLGOyphrGHeB4zpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
النصر دیروز درهفته‌سوم لیگ عربستان درحالی تونست سه امتیاز شییرین این دیدار رو بگیره که از دقیقه 12 بازی10 نفره‌شد و دو هیچ‌از حریف عقب بود اما در نهایت با درخشش مانع سه بر دو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/28515" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLamjnhyljdFRFYQ2Dmy5DFzKBr-1iPGsc96lBtx6TLPHGU2uR1ZsdWLEN0jdBxwpiG8fgzfqyHdVfjM8P67z_P6ggCNruOQzs23b4nSOGSZ6zfOKjehr9Vt-hCoGdncx2vNZC4rko8TqvrjxaJ9MZqEkYQiv5pwVc5fEC-OtHZlfsBYL5L_K59wa1ahTuFxWN3ZIVwvKHLjbBQMcly5gXEm5szGwIiSxUqRNdpk6LqSqOCFG3bM4ZPfxetkKfHCAI0c2S1dl-_5n4Hcob5IwCLxemea9aoTC5uvCT8f7N_a6zU3h3v15FG1OdLKj24E7Uovs1ev5bH5L9keltbtNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28514" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28511">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o29H2HI29GgM0P7rfBiOaSCSZ4_eu59mklRMzmV7VZUSuO-a9fzeRXxe65rKM6GHGXu_adx-8sjeoHe5MhVMTNgeRBdtx3ue4AEcnIBquktDbwt_ytu76x-uwbZuXar7MwL2xgMwAbunrH-CYRFBbWYloRjGInZoYAPq4921QVUH0dGelkXkj5Ii7xlNkB3D85fHjVOdobCLGPIrdKwIxyrtCQxIlsfynCiCzwkBfh50o2v-0IGFDSfIW-NjzOHbQ46e9Useo_KZyOQFh9uAMiboLfQQus_JeMi9YPrD-8upjMZSa4xsMX-s7jSjQG40FnO_CtDuyRcLiPuqBsGe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/28511" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28510">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi1tFuY05nnL_I9PHGOeP4dUSjMPAesYpnwCKAtA-277gnP8kSi9RduFdmlOYUgMrDDHEdTzGRgpYgQGzD6r7JOwZddRZfcV0AjXU1taA8-8Ev_nth4xLiPT5EggeKeRhOBz0s0kjx8zAC941KXL7HRKxkxs95aPs8z28xFKwa7YKr1SKme0HS5q7imcsD2JPVkWm1-be6V5xnkjC7b3d0lG6WAooy2n4LS3sU7Ttv0q19NVB3Or8C23TwkgY_7NM9bPbuiaAG9X7gGhEVesWGBXzdzC1fywbDl63iwHsmEfJHnmMdFJ647OpgYfYcl8XOBZd5CWPJlxmi1TMaVLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28510" target="_blank">📅 12:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28509">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBU5TEn6Qe80cAEkVyF7HdfldDIh7Nsms7dcdE852TI3UGUO0EsIrgttevzKOsqnibo2HlRRtHoghDNEsHtqHVVDpCxoscYF7oipaOIcK7Bvdx1aJG7uKNdijtnPAPTksvLbRmNb8mpGNnHbEWwHK1-dX5Ye5REfMkofXHiWK-ywxYSvJxF9246np2CUMRK7sT0lEkcbou38qAl1am4Buik8-QcqcoCrKXQ9DRsy9epmdAltJa3D48bO1_Y9X6P7xTGSc_wZJ57At-s7RsD0610T088d88eEped56uKJWkQAJeP6AmwYNL5wGjMQCZhy3UJiOZuH-7F665XA1qJcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28509" target="_blank">📅 12:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28508">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGz-JuqRUVxWXWN3lSfgxxEU7ZNHo03YmTqlxUaH47Bbipgaj9FB7VFzcIR6GY71tGHUxaqXla4eStS4BL-GQ3gI6ZVLe5k-EcVMp1Vy67dvs02aE-ZiiJF5X28kdWhVMYwkHGfWCD_RdX00rtZwrfz3MsiM7XGbNlVthCGQIpRJfv1gt_5qCT-DV5RdVhG6Bu0eUBybFEqcqtwUhAE-GuBJ_4RwlThTuiD6pJPtVZjEsHOFFjY5cyAXt3IzrMocjPUsWLC4U-rObtRalxGToPX10D32tySsYIguVZ3wLL1z3C65OiPTWi1AgjA8H5Rypt7xUzvPxEfVW2-v_EcLIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار کوپه:
آدمای داخل باشگاه میگن که تو خیلی ریلکس و آروم هستی. مورینیو: عه؟ پس تو یه منبع داخل باشگاه داری. خوب شد که بهم گفتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28508" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28507">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=gHcl8j2kHO7m2kiMm9rP-a5nwpHTh3fH7F-FMwvYiLJQXeHSjMdTZ7RrzgvnCfIMbt6Zj_QXZH7F79l_JZBg2qZNl3kOIaYOmpkNcuLrhlcZg36lJ33-7VJa4gbfvZeIduNcw94msaMkWSuLjpIbTC4Pe6f7qo6Bh1Gav8E-IfWpIaZH2cRrvCBqDGKI6Gl5508-ViHoo4t_kxxdIC7WUxMwiE3qVRzs3-QnTlOpr_tKh3R7rapMi17jnsfuWKdRRC6QVjAxxtCjJj4CrW7jneKJDPeGiouSy_JI1gjLUrBwasGFocYrAY8A1B2l0TRNKlQ57iHjWRsEHE6LIDjSrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=gHcl8j2kHO7m2kiMm9rP-a5nwpHTh3fH7F-FMwvYiLJQXeHSjMdTZ7RrzgvnCfIMbt6Zj_QXZH7F79l_JZBg2qZNl3kOIaYOmpkNcuLrhlcZg36lJ33-7VJa4gbfvZeIduNcw94msaMkWSuLjpIbTC4Pe6f7qo6Bh1Gav8E-IfWpIaZH2cRrvCBqDGKI6Gl5508-ViHoo4t_kxxdIC7WUxMwiE3qVRzs3-QnTlOpr_tKh3R7rapMi17jnsfuWKdRRC6QVjAxxtCjJj4CrW7jneKJDPeGiouSy_JI1gjLUrBwasGFocYrAY8A1B2l0TRNKlQ57iHjWRsEHE6LIDjSrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
گل‌های دیدار فوق‌العاده تماشایی و مهیج امشب دو‌تیم چلسی
🆚
فولام درهفته‌اول لیگ برتر انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28507" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28506">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-mMkNxyse1oouyD1PaOxJUJd24-ZBtlrE9WsQZ9dqpxehn7fVjq3ccDhkpos0LIQhHxS5NttOSFPfN5VehmxycDPJrry95dlyLCWD9-vrPvdDgOXO1YRQsWvp-M2M4ErCV77HeU6BedSElSLVD82-GAeUlokNe_HjEc_Uwf7nrcU_9VRcPRW85zsigOfEyIRkobW9MjSrXoxbJnTbBgEwTExjpKFo1jgYOO-x_9wCcilb_wTsD9_3IrzON-BTbIb8zFSuSFd_MRmSyQXDxZhr5jpT65R32nR94BjE-npNrd75MksGX30lLxurqEVFKItNJYdvJSrd2AbVfovPKYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28506" target="_blank">📅 10:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28505">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLNrgkQoDF5bQ34XVVWZnQUhl_uUFyn7tPwSQ-CK6iFvYs_NJGmiDTJ3i3SopwXofHOj38X1xWngmXSiyAQdfYItKXa7X28_N2CkwFCiey4Zbrg3TWj0vsdHYr_AOvYRgem4oljCEJlgwGo-Bi_9knlJIyYSAt8PIK7b6cCp3-mnt4CU-ZMR30Sd82faIC0AO9iRy-UYeJ3lmVFXgRdG9vbus8mMKeSapYoYGObA18V5iH0lP1VbGdv964xs47xbVSB1BtFEMt81CDhPZQ8IK8WZTKyT_Ug7-TMo_wGulnu7R8ReHGYTBLxZ-_2TPZKExdwEjwwN-ABvK59cTVPCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فکت؛درصورت‌پیروزی‌استقلال دربازی روز جمعه مقابل فولاد در اهواز؛ سهراب بختیاری زاده به تنهاسرمربی‌تاریخ‌استقلال تبدیل خواهد شد که فصل جدید لیگ برتر رو با چهار پیروزی پیاپی آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28505" target="_blank">📅 10:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28504">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtibm8SaIU1fMMxiYWx1fLP9gVkIj6D_xIitu8KRdsSMBnCilgwpcE3DtWPjcOdgCx2fKId0dxFR14wm0XW9e9GIT_r7yRR8k1CrhTHFJMcd285mM7yHKFYkozvOlx0rPqzi9eNtXpWw5sUwXkFeJ5Bnz76xxcJ1hFbbVKOuyTqsUwmMltQW46OywG2CQyrlf3L5ldy_GGXw34Rh_kDJG_a_ftyAxrBjTVVHoLDEulfgbZPExwONIE4X79mvdBqFp1VCXco0OMv3HrUzMw_k4pkStnT2sEZHbAvVzRadpoqyKCdw2FUFUoZIpCmnp4mj6u96zA9WndPW_nRU7gByQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌چهارم رقابت‌های لیگ برتر که روزهای جمعه و شنبه پیش برگزار میشوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28504" target="_blank">📅 09:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28503">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK9qoLumiXGP5QdW0mvQwrc5ySwaobZBdFdsmpc7a1AKsNtOUE3eiGYHqgq8pC1B4-MHTsAd2zTBStRqY0K9JX13PPYztX8umopQdAqlBnj9LZCOGyPpBKDl3olFpWS1CuKMdgKBUMjX-o_OboeAvCXSlVynU2m7_vEsRf6mOGBml6m1LQp3kA51kQMbWX7iEbbrJg5espz_gV35hLDsRsS9tH5JYEgMNHC6dqchJ8TemDNMmr-Yqn710ov-KNh6pW5Pnnym_nq-kdw12ixtwdR3D4fGtZE9vjB0m4ckleKrCtk7ctgaxxiINKLnbSMwiTPCSSRmUIdrYxt0KeROBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوانگی‌مطلق‌درسوپرلیگ‌بلژیک؛
رویال آنتورپ با نتیجه ۴-۱ مقابل خنک شکست خورده بود و تنها ۱۰ دقیقه تا پایان بازی باقی مانده بود، اما در اتفاقی باورنکردنی‌توانست‌بازی را برگرداند و به تساوی ۴-۴ برسد. سه گل در تنها هشت دقیقه برای‌رقم‌زدن یکی از باورنکردنی‌ترین بازگشت‌های‌فوتبال درفصل جدید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28503" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28502">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0UDle85qkdy9mCmvztQSVtuUgGKqmvlZdjJC6NlT1f7ZBfZMa8H2kRaFqovGpshuKXwiqRcCrRbkRBqjD-tj2Wlh7xyuDjRgu8RXJZIGUncLkC76Z_0OVGNtoVwGl5bXlrN_kk3CZZ25QzBky8-m9D_wg1zuVWgbnTsAsLPgj_rrCJVPQQwtmOG4zGlxLKx8JLOAOqBOfitwRaLTiC1K2UZk0ARCTdPeCbmLzQw-D4pqUrEbR48ZCwFg47IMlr0zFboK5UDTBON3W18S9aKg72TJHVX7nG8iue74ouhHvEI9DwMXm1VeJRZ8vCXz1mDix_Al04uaIpLXBWpiDj9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت‌تیم‌های‌حاضر درلیگ‌برتر فصل 1405/06
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28502" target="_blank">📅 09:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28501">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwTGlDUntWDXXype3Vsi7LegZwhKcg2RdOdT9j4TKxw6fwKQv4hK25dv1PIZ4IL1UghPAd8ZdyYwZ-xsg37v4mkUbODL3DSOudBVkiyxnuAHWi9kCiLrqrTKGOsLktZ8CHnZLm1Wo7MLLM4zTGSdLfocQtQ9OpvEPlofGRILZz87ASijhCkPsWwXxXKDgC7Pc9H44syY33aBBmf3PhzNJ490sm0dFNm83eTyqif4COVTmzU304ZzM9NCE8q-WcZcoqN5GkxWwAQRZuHSXf2S1dxOFUbWPVJzlwJezlzZUk3NtlpVlH2aoD2bCYtikeTnSz93z28E-5Cge-WFPtZNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
مارکو رویس در گفتگو با رسانه‌های آمریکایی اعلام کرده به احتمال زیاد در پایان قراردادش "خرداد ماه" از باشگاه لس‌آنجلس‌گلگسی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28501" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28500">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVCLYsSIur27S8xQ1cajbIX0Nw0o0mPgexdg01rj3TbZStFrIefi-gFdT-HIP6EAgqCVskEO0hvcwnMq6BUbwUpo9azOLOjgBJ0wloSay1UO77HJnYD6vg5T2fsJtf4td5Ub-vOtHMYSJgppTE8cvMKfjdm_BWR38ggl8YYTPaxctp2GXQt2MtaWod2dv5GbEf5cPO98oe8NztwheCVwWcB_eMrPSnkfxwqIXKdg6z7wGWQt9PMlKbgDBPH7jE4zbwsk-mhLnunB6VsaZ74J7PQ-BPQpU-St9iye1CdNdcgb43wWQdp-i8VQAFYWakHhI4cJexr9OGPtXlYv2IlHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
دومین آزمون مورینیو با نبرد کهکشانی‌ها برابر سوسیداد در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28500" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28499">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn4Cz7pCANg76ayc2R5JnC-hExskle0aHzH7cbU89hZtJUMojie3BlZ0mwySPbfFksDZ43bOjZMVb0q5eQURHNgfJdWIPgr2uI75VO-Obsv5-3z6uDXsdA0sdYy0Jc-M2Y3tyuUQv8omB67orfvfORpEPtpSr0I1uHoT-s1XyxTXhLabubbhCj5kDowB6QkYdZFlhjZX_kUcm2KR2iLn8K1mdDq8HX2Hww0kp7juu_ZGYKU1-D7svfMR1XRyuTGZTns-7FMRZgX2MVyoI2Y9QkyB_I_mn1DyCDi8lJd1xRtuGm2ifFmZJBMONrxiw_v0tZ3XEQYYUhQgae8QvSx62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
بازگشت‌دراماتیک شاگردان پوستکوگلو با درخشش ژائو فلیکس و سادیو مانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28499" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28497">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAwl_AEL3mzmy7A69V4Jl0IDWUNux1Qi_CbESZL-R2yQLV-4gdGrU5eDR7j5_me7LtX991fNBTMJdbRf_3aqwW3WDufOp1D8haCYP2iiFX5r-xozvvtxh5d611GOHNgyBq0ph3s7xU8-HWINkJou9Fz01aZzTJwC6WOSIn7uej64niWBtTxdbjYKlZBJejRgFhb2R9if0dL9XTPQC_1in-rO6SEf0wdTcWzrB1tJaG1gJSIMHU7yesY4CRM3hvjnOukYvKEgOWGVO5CV590ddZllYOrxmWNotPNFtD7tFnVFbnvYgAFCMzvufQTXfLwvLa4b0Gbf9xqFEsufLihGHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛ باشگاه آستون ویلان پیشنهاد 45 میلیون یورویی الهلال برای‌جذب اولی واتکینز ستاره خط حمله این تیم روکرده و قصد داره با 70 میلیون یورو این بازیکن رو به عربستانی‌ها بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28497" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28496">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=QR3ekZmK7FupDt3N_4qK6xPMMJx2KQALTPqcnwWlRU3Dgfo4oms-1QAUCy-qZfDBlPmyrVqC42w2DjY4TJ_jjB5z8T-LSgrT7N58Z1QSPfz47xb69V2FaV_BpHTsgUY9eJqtT7hSOasgrgBholQD7IAszZRtG_X6ONKNytdM3b7UP-gg8iIZhGOlL_wTGSvsb7xKQJTgTCtcZuYv57aaSu25rGTyYxPjj8zHiewA-N6hkwsfIV0fbBwE2FTPEhFzd17bDEiDjQ9Ftn7JoSPl90kqrg6iWjOv8cRCLJ4Kf0K2KOuRdyHeaPq4jzA5oQ5_oJ_Cf9VlHhZ_nn766AUr8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=QR3ekZmK7FupDt3N_4qK6xPMMJx2KQALTPqcnwWlRU3Dgfo4oms-1QAUCy-qZfDBlPmyrVqC42w2DjY4TJ_jjB5z8T-LSgrT7N58Z1QSPfz47xb69V2FaV_BpHTsgUY9eJqtT7hSOasgrgBholQD7IAszZRtG_X6ONKNytdM3b7UP-gg8iIZhGOlL_wTGSvsb7xKQJTgTCtcZuYv57aaSu25rGTyYxPjj8zHiewA-N6hkwsfIV0fbBwE2FTPEhFzd17bDEiDjQ9Ftn7JoSPl90kqrg6iWjOv8cRCLJ4Kf0K2KOuRdyHeaPq4jzA5oQ5_oJ_Cf9VlHhZ_nn766AUr8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28496" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28495">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=Fz-Qt-srgIKi5G7U-1MZGP-WUw-nrXEbualo2hU_H_arkudq8H_hQ7dJk5FUo-NMzRqrMIc9c9ZcMHHVXSoZ-QFgiiRbRfAvC_fs6Iv7yMs5nX0VR5LbKE1JBFACKw1O-ofI96OT12HpIbxid_IXHrbBD3m4Hw4BSQ4BjSGiJvdpgImAREray2LM2skW-36IwYZpObD4ZgimF5jrG7xXLXYXlDsdG-Jz_lRemhK2fU_rjZFQIm5zOsvqbL5CVis1GGrBJ-Jcv4KGgrVw9Xv6MC0zZSPnoShK2tyRV0c1PYy1GYwUEK8btu155ZqfqT5Fdg2z8sPwNKVXX0KYZqPZcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=Fz-Qt-srgIKi5G7U-1MZGP-WUw-nrXEbualo2hU_H_arkudq8H_hQ7dJk5FUo-NMzRqrMIc9c9ZcMHHVXSoZ-QFgiiRbRfAvC_fs6Iv7yMs5nX0VR5LbKE1JBFACKw1O-ofI96OT12HpIbxid_IXHrbBD3m4Hw4BSQ4BjSGiJvdpgImAREray2LM2skW-36IwYZpObD4ZgimF5jrG7xXLXYXlDsdG-Jz_lRemhK2fU_rjZFQIm5zOsvqbL5CVis1GGrBJ-Jcv4KGgrVw9Xv6MC0zZSPnoShK2tyRV0c1PYy1GYwUEK8btu155ZqfqT5Fdg2z8sPwNKVXX0KYZqPZcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال «مرد سه‌هزار چهره» به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28495" target="_blank">📅 00:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28494">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHPVWfyOdxrHcm5dVQeGzizw5KSvnY4f-zgwcVHb0mete7MI5X1iAgmcBZZZEhOKUDdPgjCP-jN6SvEYNt_DGhq251pmyG4ch35u6esbwxNO-yFzCvk7zetAdfSdDDudWHQOVI5DLf1hfi_Th9xtnP7b8sClAY1tK9SGSxTbjXo9vMZbgH1I0uwHi6UvGXd65kUKnzJZsMwn-LSS2E3p82wVkLkAmNCuTJA1P7m3MJO4lyLAvVDVVP9-UTXMrrLxj7Nn-Tp2nRVEF9pDyx3BPF1D6O9MwsoM0eaU9VrvHeGDdnt-ba4Tq3vPq3ZS6XRU4UBETOlYMF8Vv_CetN7HtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28494" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28492">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckeY8EjScoE2ixNOlps4ecdMNxy4m9sTw4TNGU1paJSZMJWRJ_B6sUZBjvXejLrCC4HEzymXyYjJuax3zajWuJDYoxVHWmO2KBTiiL7mG2W2eawV6n7FA1_sfxQkvGktrg5kOIqxz9a5ji2nuFtuID4ZS-6J1w1n3npJkOdN4quHFU-XVXdYA-iF5BOKY7kWNv8VPNZWezzHR9zYQiODZf-a5SETvbsuikkJCEOHhznyAKa1ZQXRZR6ly0IqnLzTFiN0g0XvyCa9gQC_kje84iU6BS312d702pQ66f4e0JQog0UWmuY8lGHMep5sPLDYBvNhMBzR_p4wzjwwMujUkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1xkUmXMgVDCPzZhcUxl5_ZfMlExxNkxtZjJwZndWarCkZ5oozALgeocA6AJJ7djDaD8XVT5uv__cwuo-jk8lAEYk7gDgSIw4ziKhA8PGFUT7xByUYNBb-5JIXaNRUu7v2Hl2F51HDpqX1d7VhUCG0k4i2HVO6yjZ9rWDS9oCQzSsrBM5PkvLyIyUSU4NhGtflb3yzkZVeWMWbhCcq3yKfgBAHOqT-lCmabP0tK1k13wHVUQkbeZSw9kP9SCUPoqArYuhvRwhCmMAeee-48s-V4fK89RwXm1qYWVdubBc8PIga5G-qMeqvaZDf8ICSu5vagY0hH0HoFh8YeVjikNFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28492" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28491">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIzbyxrKKksyowwLFDk2CqfteBLNHt38oA0gNgJR_lAonzSsBnfuFWnSu8jtlDgi5yk1SCbXRDYVd3jPko4gnAXDudfo_DhcWWefgkC7ywfCBOwvmMLdPDjULqjdmXdOJ51cF5jnSQll-LJbbjmy2vH07xAC_-VPuUoQCUBGgdp8u02FBPdFFmZG_kFdX-mj23KR0M-jXC_-2Pi2CME7Wh7Vp7iI9P5vX_Sy5X3yZ8Bx33j-RLpX-qTKVwZq-4bi4DLof0fMM-AlUl176QjmIs2faRhzMavg2-c1zj2HCS9unFZLK5scPBmX6hWt5M_e8oR7RmqYm3qFigrh71S0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مصدومیت اوستون اورونوف از ناحیه‌قدیمی همسترینگ بوده که بارها در این ناحیه مصدوم شده. فردا از او MRI گرفته خواهد شد و میزان دوری از او از میادین مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28491" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28490">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d926debd47.mp4?token=hw1C7dBY4ZD083Ka1bqsce2no06zHsSu_7Bf4aBZJbnsy7fNP4RXXyEQeGZkd6n6TdJqseAe5-v0JupyVft_aj3_F3HjDbRmVk6gmMcfDNPLPRJllZ7NoimuP7Mod4qo7zbd9vTjl-1VI2BKUzRF_1kgL52TWyp3vxsELFB3tMuwNLAPyjdLy8llF3NnUXmHiiyIzLX-Jo_RR07UMIUMrWVOMuApGqZSNbpnLjMyi1_Cd-REoD_jcYYT5ea-tu2G4-obXiNfLo88Lt-nEjw0SSJl5fcJq34EaKYoy3GxbHicifaxncNncKUkVTUubIRaL9J0uep4EixqG9LMq-dkiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d926debd47.mp4?token=hw1C7dBY4ZD083Ka1bqsce2no06zHsSu_7Bf4aBZJbnsy7fNP4RXXyEQeGZkd6n6TdJqseAe5-v0JupyVft_aj3_F3HjDbRmVk6gmMcfDNPLPRJllZ7NoimuP7Mod4qo7zbd9vTjl-1VI2BKUzRF_1kgL52TWyp3vxsELFB3tMuwNLAPyjdLy8llF3NnUXmHiiyIzLX-Jo_RR07UMIUMrWVOMuApGqZSNbpnLjMyi1_Cd-REoD_jcYYT5ea-tu2G4-obXiNfLo88Lt-nEjw0SSJl5fcJq34EaKYoy3GxbHicifaxncNncKUkVTUubIRaL9J0uep4EixqG9LMq-dkiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28490" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28489">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28489" target="_blank">📅 23:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28488">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4elalfaGQcanB09lkM6OfuAVJU8fPcQ3H2oFzY6ZpUw39ZJzqyGg1HB6Pk-iTaK00ZBegqg4x0hvVoEsMIjFA2nORKBCS2chbARLYkZrrZIUR0eS-Zhbd2JLRkvTLGjSXwB1lSCi2tT70m9eXXi5Uln3VzKWcB0QNwP1PqqXCYhQmOMT43AwQVZoe9p4XJkGm8zoS6IuBRVmoS71MYqWFQkwTRxXxdKB-NDWtGQKCM6lZ7Du4j-s9cfw54a9fz_jM3o38PV2m_ta6JP6a6tvezc02tfnvn4Qy8n0RcTA2rBIV-6Nm4BW6VjHAs9awbamCo_eY7puBDLGT4j1pr8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
برونو فرناندز ستاره پرتغالی منچستریونایتد بعنوان‌بهترین‌بازیکن‌فصل گذشته لیگ جزیره انتخاب شد و جایزه ارزشمند خود را نیز دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28488" target="_blank">📅 23:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28487">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv7zvPFIlr7uS0lYVUNTAvfaMA_YOPkfPphbRydj6ERCm7KxSlPZQ_GZv69TpbanoLYP6a6sgDU8VclyU_gGWozec2_keTBkaf64IcYvUmA-bDyMmTQC0t9MJ-7Ci2hKqsctyV2P_BJn2xn3qwX9vVqNmIuz9t_3AlZsvp5726L5j1OvcIBQHbzXVES8dqeG-1tNQV1V3FbtJ2Jlh9KxbM8GSS9_zbOQ2HM5LV4-LDwr4t_8oBWvjk4SpMNruK6AjbS8ha5jrQTFuQYs7qbeZ4zGdiLdd-Cqe1v8P4CRZNgplAO6nWal-g6vw4Y1YRUGU4_oYqDgrx96UuTCNykGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ترکیب‌تیم‌منتخب فوق‌ستاره‌هایی که فوتبالشون رو ازباشگاه‌پرتغالی‌اسپورتینگ لیسبون آغاز کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28487" target="_blank">📅 22:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28486">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=aiMUOCVP13bQsz-NYJ2jVD4ypPK5Ae-x4aZjB4iNIHs3fzhGZjLEz81nS0xPEVmpfluV7BAmgKJO6oEjZGR7u16WWbOKjsXHXPolddRIlT8AQvfXVHO1aZNHqdUc2mHhHcLqGhl5oSuizPbaFas2DCnR2JAp5oS1JWfS7dl_GSBmvQ0ioob5rh8LGuz_cuK1OC-bmEIZ5zBmbiEd-3QlR84vt25VMlWLvI9QVrxGTIj1E6zbJVSPTR3j5Qd2l_gPcxh_-m19TpuxpQyvmK2ihISHU2EVihkGUxapGlG-vO3BpSqPJ5GckcrQSV5HgaMYn8pIoOOzarTBug3_KVipflaQ7_iqOE5oABNJjwgDYn6cML7506p0xFpjUGp9W6MtGhJ78IUDrYVsuzMDVVQZcAqmOuKFs0oS1maLaAj3LC_ooYVoT8b04E9tpLxzTttamw_Ear-pM2rjb99m03tBkC7sbv_EeLjXOPies26gfL839SLbfSiZdguiE6iAQR01XB9BRI_Tr-ZS_FIkT5YUkIRshI4LrMI_aMnZGdb7OrrcnWBD5KK649MbzfNepjSc1CyrNQYV1ZzrmdV7myjkTFTIWFlOmgC5GMO9wTTSjMz7yIRNm3_8zApVMI_0wjtT9afI3h_DupJc068P-jsL69wQcDy3oQ6Rs-wbmB9-iSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=aiMUOCVP13bQsz-NYJ2jVD4ypPK5Ae-x4aZjB4iNIHs3fzhGZjLEz81nS0xPEVmpfluV7BAmgKJO6oEjZGR7u16WWbOKjsXHXPolddRIlT8AQvfXVHO1aZNHqdUc2mHhHcLqGhl5oSuizPbaFas2DCnR2JAp5oS1JWfS7dl_GSBmvQ0ioob5rh8LGuz_cuK1OC-bmEIZ5zBmbiEd-3QlR84vt25VMlWLvI9QVrxGTIj1E6zbJVSPTR3j5Qd2l_gPcxh_-m19TpuxpQyvmK2ihISHU2EVihkGUxapGlG-vO3BpSqPJ5GckcrQSV5HgaMYn8pIoOOzarTBug3_KVipflaQ7_iqOE5oABNJjwgDYn6cML7506p0xFpjUGp9W6MtGhJ78IUDrYVsuzMDVVQZcAqmOuKFs0oS1maLaAj3LC_ooYVoT8b04E9tpLxzTttamw_Ear-pM2rjb99m03tBkC7sbv_EeLjXOPies26gfL839SLbfSiZdguiE6iAQR01XB9BRI_Tr-ZS_FIkT5YUkIRshI4LrMI_aMnZGdb7OrrcnWBD5KK649MbzfNepjSc1CyrNQYV1ZzrmdV7myjkTFTIWFlOmgC5GMO9wTTSjMz7yIRNm3_8zApVMI_0wjtT9afI3h_DupJc068P-jsL69wQcDy3oQ6Rs-wbmB9-iSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تومیسلاواشترکالی
؛مردبازی‌های‌بزرگ؛ اشترکالی مهاجم 30 ساله‌تراکتور که شب گذشته در دقیقه 80 بعنوان‌یارتعویضی‌به‌زمین بازی اومده و در دقیقه 90 گل‌برتری‌تراکتور روبه‌پرسپولیس زد. سال گذشته نیز دردقایق پایانی‌بازی‌برای‌تراکتور به میدان اومد و در دقیقه 90 گل‌پیروزی‌بخش‌پرشورها رو بثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28486" target="_blank">📅 22:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28485">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alwrlOefa3BvSeha1-brXE_kf1Cwv5Dxb_67e-Yijm4UsPMlaO29MRuNoSeGOyb-wjRvjFwWa94win2e6bGa96O_brYwJkOOnA_cnvF9Hx7v83fjcNzg8lJzvNK_jAnMjnXOkomGl_zK1Q_NmuWmPM-_BBZz2rmAk81kycTL4o4hBvggkZf2Qxw-jd9mFcK3yh1EVMob1W2kHo51ZNZKoppH2QB7RzcA-gl1vluCG_iyGdmtoToEiT-mCXro22b_hdoOjBR50dFlO9PYD5NbL3M0N98zh6SXY-emfViNc691SXEPMBPRNyb0q52bNvjmRF2PQ4Gn2wPWuSaOWauP5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ انزو فرناندز ستاره25ساله باشگاه چلسی در یکقدمی پیوستن به منچسترسیتی فاصله داره. آلونسو گفته دل انزو باموندن درچلسی نیست پس بفروشید و 140 میلیون‌یورو درآمدزایی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28485" target="_blank">📅 21:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28484">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKwpFFVZWIC37HF-sDjLwmPiPpolXuAvQwQf1VVcQclMrj2oImHnTHuwAHQz0wlyNu2_ZamRCQQwMgOTwJllj63FnxN_C0CGZKWMnHHKfhM_V3RuQj084tVfxKv8gv6nT8LjmFMpLeGwFj1c8t8Rp2xzCRS-CtFmfuhlYxvoB_7oaNrj-TYj1p_veNN3pNDxPYIznLFXARPwvAvk09TggowWcmS-LUuKEbuiiBpSoIUDaft2bHpDbCJZ7xC9QC1rQw2mfgNEIFdvBegksSssgc26NCcDeSLwdlg1ceUx8VUt-OIkfr8ZXZevsqzxbEiS8R7o2X-ljO4MnM6vUxKVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌میلان باموافقت‌روبن‌آموریم؛
کریستوفر انکونکو ستاره‌فرانسوی‌خود رو با قراردادی قرضی تا پایان‌فصل به لایپزیگ‌آلمان داد. انکونکو از ستاره‌های فصل‌گذشته روسونری بود که روبن‌آموریم نخواست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28484" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28483">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2NktHT8hdvbpkX5rCcY7eRmKItsPGboG3EpXP0HNx9t2E3r4KBPpdoy70eHAzXru-WaTDRINAe0P2K34eSCQbaTW7KaWP7LWN2Rv0I6wjGed1J4CcJTdtlK0iIud1ul24XZ_alcZBS9-c_q5-yolG5GdGLfQ6ij4JgUvEnrBpz7z-PbyZfUtwjsMj1ufeRiJ7svvCE7YwJlra71S64GvQOHHzAw7SMYFsR9L4u2o3HbB06SV3FJ7Jp76Dj0iGRbc_l7Ze45u0X-5kTSr4L3-yos8y5ykLnH3-nQHY1AavSae2VzQle4k_6T3VkS6iC0Br4PnBG8LsDgA63mdSKr-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28483" target="_blank">📅 21:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28482">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNMPWmH2J26GOgBkTxyDu-fx7VFSnlok0DjTY6QFZ_4d1MT9khVCn2Y_MCEozf_TUvWKEIWgeteZt_nbePSthhj0x-t7TcP1KNAZud9PnCxXEGCpOHTzEJd-KmYIsJ8oaPkrxjYWDbo3FJI0m1m1gF82_DuCu7J4vVOqNyjPB2CeHDs6pZ7DwpDCOvt23sGvuOuQlKURvoHZqFIv65nO1N57BcpnXlrzhfaAWCVU8qVtGRTWTiKgdMc9aQeqls9VmyeP0x0ye2clGZStmquJDYZRbpKiUS02mHtOjFp19pXiiy3z89cxvS6bZITtpFmzkKilcNykbyS6XJ7mOiG0JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛
با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28482" target="_blank">📅 20:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28481">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCI7G-IOycn-ILzyjwtkyuiw01NvTqRY14poSJHE0-HmZPP4KPHTlH2e1rlnh9C_UGuxJoQtVBsx74qARK1CShLDGVw4fxRw2Vvq6zArI5lgSiXl_Pl6ZXo9w74NkE3hH7BG31gqZ1qHdh9DIb91JHBk6V-LOIzn1XcAHkCXBM9Y1UHxCSp6y2mTtLjKB90RNDj_mdzAil8i3Vge3bC2MEAat1ah5WgIGocM7VztNS2Qfn6GfjSVBhjUGtWxPItdDECqmtXAwQBd1B45bZTNFCzyIt7w7Y_nSNT68I-1ZjYtwS4hwVqwXYALDa7t9_8GoSMw9rjbUG_r8XB3e1p1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28481" target="_blank">📅 20:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28479">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMr9sCAHS7xHPPjqN2qD0TtaA9ZjKwAV-voJ3mxwwaLyjp06HYKOCCODzx5rVQiA-d8Wm6Fj-9RLvI2WEmDn_OrwcXaYC4w8FfJwfQUXi3_lpG40ZZVNCtmh2G0DxFDunSUCrSLpm1SDax3bKb-z3MC4o9OnvUF84ARYNpsc7M-R_5XxLNcwseJWJSo6RO0KtpLoLV4OEPYifghvhlU1UKrCOhXj_tIPl7ATtR3FGjJl5s7kIHlvaxKOPH3ex6-erwuCune9W8JqGQmoZg5tdkPbIR0GUVNJJCHXa6aV45AP8WjGTCvqesDRWAZFkBdE6U-y7hyAIFPXSclrv_1tzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7yYOJRff6KcbJDKnV0ifFWyBjs998PBooG252sv9jXyjf2E8hU7iDHN-OacwXrZC27nl0SCd9PF25x3wTtgzlgJg7qSqcrUeT3OrwG3HMgTrawnLCeQ55XTPjyGgt25CbmPBevY8uM-gEsPYpHfrp1Q03l7cOcQGqmS6ffA_mIjUstJAtJRcyahlUuXGhTRHHQQ86_uiYDu-lHNKKTD4p9sAoaZ0yMfT9HYqaWQyLgMg6BqoCPCWj3v0lv_FmgEPwGv9Goecpsb8SDu9oWc6XJOh_tBXUwST15gW6QUzOuAR_zscAbPYww__bOz_CSX73B0kOKhcAdbVZ89uBrIkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28479" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28478">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxuy3tq9jjgYr5ecQuujBHUqBQcg7QLrvzSrXrKhtBhKOM523bZQg_lmgl19CpJY5ly0I-vV-Sv1EWpjP7EClSLTxMdmXFLVJ0PuqoDxRDZUrzlTLauFHxGUa6TqGJpjDywKyr2mX5HmKFIRrxTCQsiDqxkC89BdKsffheqjt22tmTHzsmjg9R8bzh5OW-_N_2xeuBLV8exztTLSY1xKGatwtZkBdGO6cM2Tr27JiRfDHzD7Zrk_MEfC1pAHdRzH2qEKJRJV5-5sp8p0wZw_9LkbeXGjVKaOQooSOFswL5mjKQ6CFJSFovOI4EWxpbhCpx1BhYRjoQWMFosLHoZBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ هفت روز تا پایان نقل و انتقالات باقی مانده و هنوزسرنوشت بازیکنانی مثل بارکولا، آلوارز، انزو، مینته، امبایه، گاکپو و پست مهاجم نوک برای بارسلونا و وینگر برای لیورپول مشخص نشده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28478" target="_blank">📅 19:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28477">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM_I7cj_apypiZBpYZ7vlkdRSTJVWznYE_eK9bo40v8fpSIwoI9PVD55GZbbgwuioi316ez-oEEXibsTXtG5ODdZ5h0xVO0m6DN_AXYSL4S4vYJx4x0JizccUHPEUQ8zC9mD1eGYAvp8KBq_Fj4DApddXh6pA8uP1G46se9137C24q0JEErGqHBVHrlruLzIcMB_kd-A52fPLS6gvPBlt7-e_-g7vhMUTfzbnY4nTNBS7BPoWgp6faZBKTrSIcyUxWpwzA9eKGDLr8ZH9Yb5e5MA1lwXqy8i0eGBYU81Y0zZT9yS6A-WQ7_8rkboLtVfZPxcAcIEbheuzwqN6lGvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28477" target="_blank">📅 19:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28476">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0TGuJYunIT4XGDPkiwhxAM6yjikiLGjtisYRykOxLXwKlbQHl-7MMWwwTJtL8NF3cUKEoduNe0MyZZ6QsumzYcgwfupTwGHPPP2TSr36wECGX6b04DIsG4RJ6gd1KJG5Lombx6QGHrLnozZluzFBBYo18jGjxxeABS_yI1IgOTNFGnRXsqdpY1U29ceSZH3_ir1eW0e-MM_nQ9cv1tO8GlCZdCrcBJpbh4WWQDDMapc9jWEzJpIuNLMgQdQwCfP0Cf_07jECIw1C-KLD5XQ12lkwduMaSFaDkau4zWNi1gQ79SCWw2WuDSCENfYtNcS6yoYmmmiiniVlDVd5OAM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28476" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28475">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
قیمت‌موادخوراکی‌درتنها 5 سال‌اخیر رو مقایسه میکنی آدم‌کرک‌وپرش‌میریزه. کسی ندونه فکر میکنه 50 سال‌گذشته و این‌قیمتا تغییرکرده. قیمت خودرو هم که بماند همین امروز روهرماشینی 50 رفت بالا.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28475" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28474">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTrk7WAlVDraeVWZkcbTShsCRi3k54jM7dDI9_qvDh-xMGPf2n3A8jMiPxbuBqJoK-T9Yzug8R5BN1qoy4dOW4I-96UETXtCKK5hTZKl6GR9LPcESW7iYBXF-cbWvS5CqCZSk62cSKRft258MQF3Zeg0TsCaFgDrdy4Radtjw6DDfi3YCKOOtjxkt6OirNf2g-3-4o23xwlZ9ekWjtyoLalAl13bMWSana1W_NA-isL88iW7r0y_bCMxmNhFV0lBnQuqsJxwU1DQo09T93SyHGhS_KTo0i6fYDFGohIh3PmlJjoedt1eLyXWddb54GZc2-S1PR-jlRZC340vibC-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2017 در چنین روزی؛
بارسا باپرداخت 145M€ به بورسیا دورتموند عثمان دمبله ستاره جوان‌فرانسوی این‌باشگاه رو به خدمت گرفت.
عملکرد دمبله دربارسا
: 185 بازی، 40 گلزده، 6 پاس گل، 141 بازی رو به دلیل مصدومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28474" target="_blank">📅 17:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28473">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyrQjnqKxVfpLpymZUalSX6pJVbP3wNI-1MxhPK24GkNv-VlQvh6mHcizbOYo23wdhBtmBL2_o59Tr49Bf-7nZ_qTNJ2rpiMH5QOZt16RFXCTQXI_GkXa1dWMzmqgBJZlThK2ffpsa5p-eME_fDkwoaiZalswxMZLsKL8vr1SpGtF2tb989rLASdur-kmSMaVRAHCiv4j8U8Zi4tUkW4yk-cKt1wo9BJCoLy7eHXD2guM1UhtKoqDkjUNzE-Uq6ZaDqR5AhiRMNLRNDVRbYnpZ2DJq-ygmxmY6bXp_YZbBBpeKHdWrmHBDfiSZ36iEunQAd3wZ3u6TSxT3TMVbq9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28473" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28472">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjYgvcfMir7JngeXPcCA78hn2IWxttZq8WNSd9qcRkm44pYKc4XbJqlGmebTbGMe5ZFmxKHVW7MF5rpOveV14g7AWA3gTUpJK9ByhWba1hMIs6XA0oJGeyVjCz2PKTPKfDbUIoKX1F5x6T-ZJYiLFGShxQms7adoceDTPMvmtak15G73nP8Oe2iADQ5mqrNlEDJ9MmJrZ7mF_S_IdB-8M8KQUO_LylXDuwHGXqWxrNPLERaJaVxGxUi90E1q10FJUp91b_-aDV3eKkVHRWyQJlLG5pGZMcKM5rRpt1yzKnGw3tKmeXhyWN9DetO0pxYcSN64MO5IXoPdQammaa5U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ترکیب‌احتمالی تیم‌اینترمیامی درفصل جاری درصورت پیوستن‌پل‌پوگبا و آنخل دیماریا به‌این تیم؛ دیویدبکهام‌مذاکرات‌خودرا بااین دوستاره‌فرانسوی و آرژانتینی‌آغازکرده تا درصورت توافق‌نهایی باهاشون قراردادی دو ساله تا سال 2028 امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28472" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28470">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chnXJDx1iQIShNlLjKROLK_teGrGSekQqv7jRREBHjiGOl14FZsuE7J06nuk1sRQF3JLC6fW5INJ5FVRPAZtSH-h86VTAwUlN5A94GPBMPsMMSYUqFteABnpV4hNOhAWy972CuA11_Zwmrc7-IYUF2rUf_a0Ka-EHtcp-_J2bY07DI6HTIEm4hJ03Nlwe2uZDilJ5hbPJMR-objYSWqyEZS7FLOxpxbjA8DgwvtUjaZIfREb9E7KptRQT_CGiv_O1nqvXdnY9Ovysj8mC6oqITewnzyP0HcIq1oDAPC0hwCOwQsC5RT_iDXPaYQSLEE5hNc5ZwBNVJ_9PZW2TF7hCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28470" target="_blank">📅 16:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28468">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=sqC-XbU9eTWXTSGrv-bbaM6iwGLWEFTYD-R_58qjYOapsQDBq1mvWKXYXscV10X3Ph8EWwKV_n_EUbnTvPzDZgH09HodHv8DtNM1gExfPkNzUs84yktXD68NX7ZGBzhCypaz-jXpi7SXQXzoCXAQZOgm3HP0Z6oEuv53CzZaZuBRG5nG19WuchvyncxWiTAEi3ZUOeXhMWlEHNTRpGQxF2rEYZEjAw2Mgrcbz_4vHvp2qHci5AiTCvcu9Bz9PFumOM9jJRq7eRXrzdlEmR7HlJudMjeNrn_3CXaX3UgqpOwpZu2Zf0id6oqn6ud4MSY2b5LTpWYPkcq2-4C8DiXf2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=sqC-XbU9eTWXTSGrv-bbaM6iwGLWEFTYD-R_58qjYOapsQDBq1mvWKXYXscV10X3Ph8EWwKV_n_EUbnTvPzDZgH09HodHv8DtNM1gExfPkNzUs84yktXD68NX7ZGBzhCypaz-jXpi7SXQXzoCXAQZOgm3HP0Z6oEuv53CzZaZuBRG5nG19WuchvyncxWiTAEi3ZUOeXhMWlEHNTRpGQxF2rEYZEjAw2Mgrcbz_4vHvp2qHci5AiTCvcu9Bz9PFumOM9jJRq7eRXrzdlEmR7HlJudMjeNrn_3CXaX3UgqpOwpZu2Zf0id6oqn6ud4MSY2b5LTpWYPkcq2-4C8DiXf2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28468" target="_blank">📅 16:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28467">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml0vBHeIyIDYBdOPj26XWWlCMp9ug8OOtU3eb_a1U3WsdM2MCVQFuiTx1CZYMWB11Q54QDyI9Gy_9G1da0-aH8YwkmfqvbC7Cx_wUctT01KTwHUpd98nra43bCPSNXyYLvAXJP0BZ16F4eE5Qlr9Pc40MZaTHyaePi4YseuteFRVJLg92ivjtVZtDRnJZy70Ca5JRi30eyTn_I9EkEnJFrHeh72uPv89UW3AXG3fuWpAPz7AVUfahhAZBFUOKCcE4bk-hxZDsyIBr7ojwSsa-Mkut3Zbb0dGkBQY9rmBnO1VJj26RLbvVNFM6qQpcoYBfDCg0Cj_bbshtfMNq_KesA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قانون 90 به 10 در دربی بالاخره اجرا خواهد شد؟! بااعلام‌رسمی‌سخنگوی‌سازمان لیگ، طبق قانون باتوجه به میزبانی‌استقلال در دربی 107ام 90 درصد ظرفیت ورزشگاه در اختیار هواداران این باشگاهه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28467" target="_blank">📅 16:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28466">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWZDmQ7SWjYiObTHRzue9ik6Avzw4C4eVbjzDE4SvxelhZf8ssOZwqZtAogHgwV89wgLtB0rtvcQbK8yqddaSnJHvN9ZlhJlu_BQNdjlFBgePFbgrh9usiRnTYj_QHMn6w9oNRuAMhsqloO3j7gV49tBhtP8Qnoo74kkf492HxOyout_VuCqAB34L3SeHS5EJwZC-0hW3SlG0IrhXCikmjNSzjLvfCW9Zd9_F7hlrc6yX8xNmwxnvNd6wocpcSqXImLPLfBYk946dHhnGW5eJIYewVKyMc_r8wLN-XdLm9jbkakeSH_QOJosi71CfC0UF6zHbyV7DaAyW-g3AzvP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عارف‌غلامی مدافع‌میانی‌استقلال با قراردادی یه ساله به ارزش 8 میلیارد تومان به چادرملو پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28466" target="_blank">📅 14:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28465">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHRxbjD4p2BXeR3PEM6d6m0ZPH6qABKYXhxUnRORrwXOOmWryEAEvpzkVO5ji2z0Fu0S_-5Jo0djh4JN7GmsxA-8EqMWtdwL2MfyifHDyO7LZLp73mnBdATt5Gi_orTLu5QjIOX4Hgl_s0J0Si4fu4_AO3EIAb7n_sdAbirwuJjMBdxK6UFBpVbRjqoM8TwOlxagTwNmYCVSZL2fkV1OGdu7yTXlNsj_rzDCvtuRL15r9-BsPvUyL8GtLv8ddT8czn5UUfvuIqFFIczSWhWUo1742rqoYRRR3kee_rZAUj0I3GfLdaD90AXDcZ97nGbyQG-6Depn59uHQeL6JxVzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28465" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28464">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HE3wC87dIzL4n7Ht6vHhqoDEAtitwGkYSv0Mypt94nj46Weh5e-ab3POutOmKPLwE54aPGIZHzWb58LUX4zGM7LeogYv-TVQ6MwbigNKKcx5CXjhPqMhDPtJnDjc07ReCSiLqAb9mYWJ6YsuDeYG9bO6S5BN7o5Ditw-izF8I3cWlNl9koLnONoUqZDFabSazwbFPYNg0NH28WjX0VSQweKf2jdg3LGdZ6jL0dSMuZ6IStkk1YXWMDHpw_t4JrseKhFz-3PO1C1FodZN7daf1Bctb7kf-Nknu_FN3Y3BdHpGN9Vf9h0OryjdSu_4-_U5pYv_-1vdZW9Xg0iUvd61qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28464" target="_blank">📅 13:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28463">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQM6GHje4EtOSHzLfHEtNiP905die8rvfqAq_2bNc88xYJqUqrG2AAdK7vfIWON_m4aC9nqKDR1Czd_uWZfmHCv1RxneTdGDE5AXn6vWtJs54QtN79-DpdQty6sdl0Gf07u7DnWX29DgMtPVf79A-hN-bBd-7c3-OnFSD3GWR_IRayORGbJ7kVrtCysK2-6xg7nyi04zh5GyQZARlbgeWFlUVs2OI-NmkhZk7CFEKp_PRKZUNWE-2eJzRTMLtyOfgEwnbr0zbT4HtsYElHZKRNuW19PPliVEitaCw3L6sMf_B8vtW97PXenjglFHcp72_VzGSZ0r3kdGIooq4KypCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توورژن‌آمریکایی‌فصل‌جدید عشق ابدی یک دختر ایرانی رو دعوت کردن که همه پسرها عاشقش شدن؛ اینم رفت همشون رو به ترتیب بغل و بوس کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28463" target="_blank">📅 13:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28462">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=ZWp5FbRxWM935jIPS_yFUhaLlacCHw4WjFn2VAOZnfcWW63MjqkSv51z76-m2RLZFPsqORpLVSmrQs2CIOP6MJ0i11c-K2QlKtadJfvxGS_uwxEtCJ_z3pUaX8Xc-w9a_Pyb6itJMfXWHesi4uVB1_g90d7qtF0blCih-PdzyrYmNrU5KQGzsEPypweUilwAHtFytidZoOqnA5JwL56YxRhBf1j6VdvvYEPU3mQFrTR15eBST3_2iEjB-MraNJuhhE_Ch1q4xumRdVVB_N2gQA8TIIyU84nPN2V7VB1tdXllsknr2chOordsSeepwCgzpOm7sjRi5GqzHSLrApPo6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=ZWp5FbRxWM935jIPS_yFUhaLlacCHw4WjFn2VAOZnfcWW63MjqkSv51z76-m2RLZFPsqORpLVSmrQs2CIOP6MJ0i11c-K2QlKtadJfvxGS_uwxEtCJ_z3pUaX8Xc-w9a_Pyb6itJMfXWHesi4uVB1_g90d7qtF0blCih-PdzyrYmNrU5KQGzsEPypweUilwAHtFytidZoOqnA5JwL56YxRhBf1j6VdvvYEPU3mQFrTR15eBST3_2iEjB-MraNJuhhE_Ch1q4xumRdVVB_N2gQA8TIIyU84nPN2V7VB1tdXllsknr2chOordsSeepwCgzpOm7sjRi5GqzHSLrApPo6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28462" target="_blank">📅 13:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28461">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifPU2GGCnGADIP4jyD8UEWXTBiSX5nMEm2NJBySO7hbqb-PRSCLeQgYXpqFxo-Gt0JWQPhRGK_j9j-YcGIfb8AsDysY7qvRSGcsaDrZU1IILVM6XcyyeN1FAFB59gg9FtbHsIgs2o9ntJ9O98P79ABiHMkVGe4V4KJHXT5TBwD_L78Au0VB0xTeFH9abrVHRj40W1D2RUZ5M6-lHL-Kq37CacO7e1tZa5sGw79R0Bv1N9WwRR_2otMauI1HC5amuGcK4ccm_5PB9AtiOfxn7aqVxQWM3aQifzY9qLCnOCnINgvgioEMk3Dtox-XCoIxe44EAsz1ZD959h2Dbs1FhCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28461" target="_blank">📅 13:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShkRJBtWBAewHF1kCBCDZLiTRjFFD2Q46PbACg5RgNKNgjoF-ark8LCG293lkqfcnWQqQgh06OM2N4qIERaCvaomk3jDrdUIhU0WwkBYnHjU5heyv3toiDbnRDPUbQydDu9-M-eTAKNo05f-N_tKpZD50_8DjEPp1xpJ9LnKfdh4-cfi2senxV7txQIeC7MPnwVDK74vEWmSPCxpwdZVC61dK35irdH_jCSlD0qb65QlwKzCRepuaXPBFdcvpcZpOjnYUMSUivKxqJ-cK5Y7HM5CyXejtUCgW1sbpniDhpHK3cKoHC1zzox5cviTaa9ApAVdyV2X_kt3Xego5v8mXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n32me8-EoOEnOqzus5lpwBxdk3mcKDQ9j9N7Vxba41U4_VVp6oUWdGxnSO4HDaXrLd1i1IhwndNvvMGGFzWGwCbc8AHuCcnT3G9cGET0lVblNZINZS05qPGlvwhNzN2lxxtHpOWh9AhuW01voaW81haeTPRqrOtwXfSa3vOgaGX4UwhahkAFZhafpRZSF8WZvy35WuQfzaRc6xduObwM3xPrve1NEJalF2LMQRkU5ki0tdTQRPdZK53vBK2aLdNW0cUOjjaNqmRtz3jh8ZbGQI8EqnZNkZt1jcs8UJRd34kNUQg2HTBkRUAJy2FMjWYAahsZ50_XgfK3nCuY9o3sqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
از مربیان آکادمی لاماسیا؛
که حسابی به بازیکنان این آکادمی رسیدگی میکنند تا ستاره هایی بزرگ به تیم بزرگسالان تحویل بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28459" target="_blank">📅 12:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=naj5x5MWwpyLaXeejV69dt-bntoZJXrdUfQXITa_bjyzyGc2Nhe54oU-dM71g6mj1CuZbxGoMabGTDLKBhtSFvwH9M_Lz8Fkvzthz-slk5PNhQy2ztF7Oz8xHMecjwOCABlKpHHFPiU6MyO43TC5k7iQYzsXUKU7RcepkML8ORWdFUNbliUvfLEkmA5-HnMHQUv4f5lJFMB6Big2wzCWbmQpcxzakgJL8VWQN3GfV_oFsDIwrGNz5AmBlP-N3fZ05Ezht8oyXYYAhyJOPb8eushbB5QPWaeaMgRf_w6K2eyuPltynsk4YlW_OGjQSja7zrFmlZCF2xK0guVD2ijwog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=naj5x5MWwpyLaXeejV69dt-bntoZJXrdUfQXITa_bjyzyGc2Nhe54oU-dM71g6mj1CuZbxGoMabGTDLKBhtSFvwH9M_Lz8Fkvzthz-slk5PNhQy2ztF7Oz8xHMecjwOCABlKpHHFPiU6MyO43TC5k7iQYzsXUKU7RcepkML8ORWdFUNbliUvfLEkmA5-HnMHQUv4f5lJFMB6Big2wzCWbmQpcxzakgJL8VWQN3GfV_oFsDIwrGNz5AmBlP-N3fZ05Ezht8oyXYYAhyJOPb8eushbB5QPWaeaMgRf_w6K2eyuPltynsk4YlW_OGjQSja7zrFmlZCF2xK0guVD2ijwog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال:
باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28458" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_6TgjCgjUhP0wOTvlFBv4UtIJyZDIyB5pFOM82crV3CxFZLYG9Kd7xn8Jx42aenD4d6cbDQI1jWJsrtLL8-lbtBgMr7Hp1oFrO4x3pNT0I4AeolS2gzKdZg5WYLH4pzq8UKcLIaHVDROMFsOLSsJKNoj0m2KuvsVhNr2aHAYD0edWzgbVQic8AlVA0uLsfTRwLziNVOoQwxeyE7p_LWOcjDAjG9YToR4F-mpKkDiDsu8RvTYhp_XAlKCCyWkzuliRi-A9j-ncDdoaVlX5pVQWJeA2UxAOWYdquYZu2XJA3_LEj2vdkraJ5O6Sqs5m5Bvfru6OhMlwOHAKZoItMIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام خوزه فلیکس دیاز خبرنگار نزدیک به پرز؛
اوسکار ناسی مدافع میانی 21 ساله گرانادا با عقد قراردادی پنج ساله به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28457" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufrtOF3anIKEqI6M9OcFlTlUaSOXbQFAdwPdAn3atWnYUgWONklc3QB4fNgQgBdEhDLUXx7vRVDI4spE2nA_E8rRz-CIr4KOYPMuNyhrV8YlZ-yXIx1Kc8AmBE-j60wsFo2tLk-Mmiq9HnHdXiOUae2D9FyqSobuThB6Y84gVNJBqW8viIOKaW7qlr-EXkFQe9UnUwRcQEq3hCALSAIeEcOF3zBGJ75988LrTsZXdMEsjA0rPUz0Ajm2bqUge_5eF9okZwKlRKSnIFIv8PnqA1hIWr208k7o3aTS4UMtwSInrmzVfxRVTdcjB-hbmPDmYAZ2o1DQEOD2J0Kp3-9RUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی‌از حرکات‌خفن‌و‌فوق‌العاده برای در آوردن سیکس پک‌های شکم درکناریک‌رژیم درست؛ تو‌ کانال دوم تمرینات‌بیشتری گذاشتیم اونجا هم جوین شید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28456" target="_blank">📅 11:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki0i_i-HW7woVwOfVChhUBLkozgR-0uBjBI3rv6orp0O9Eg6hSOJnJNm7Mx2_t23-y293-ZnnGmN5zmukZbYZ_zWlts-8K1z4V1CPM3Xgm03xhoF6dl9LU0Itg8Ii6NAy6LbjewG-C2uFPCXw_uaDT7SURbplua2DOpeyIttzCd9M1RsbLSYAQ2Jq8-h8fKa1hBbi0OlAWtIVKq3yOwShyo7efXixp2FKFVIG48Q8hL1CQLmtcr3Pu02a13VVtJK9QWUs1oUbVcSGNbOVADDAMLxSktqcoVfc-K2TEMBIkkIt-xGp7jYW4rs6694mVbu6QdexVDestq0DtZNZrLSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمیدرضاگرشاسبی‌مدیرعامل تیم فولاد: باشگاه استقلال یوسف مزرعه رو میخواست و مذاکراتی هم بین دو باشگاه انجام‌شد اما کوتاهی باشگاه تهرانی در پرداخت رضایت‌نامه و تاکید آقای حمید مطهری برای ماندن مزرعه باعث شد که این انتقال انجام نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28455" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFVlQ7c6iMHNm_Kn3cpidQ9BTDZ498QU2OUu306uI29HqGCd-jLH24onoIbFEUDZy_8gFC1Qc7XoHCyUUbFc7auH4sFQaTDgbfFTwj8Hj-oAwx6Ml-Yz--zY2ZLmrQJvGXYLKsgcf65NGt7a_9ZoMQ4Rl2I9Q0ujRggY6MOoPKI7OmRJpJWRgpU9V8oXsYnkUi5fHZZC6XfJSxk29KDz-AnJHlMuDnUN4KrJY8UVPFmOyWxQKhkktWfbyHz0uODu2-YQ7jCZPHmNVjRvDfV42yjYVuNOku7LbzuKrS1SMbCfaNBGjaddsvZV_F5JNP5ZWq57ZEV8wFMElfqyRKaSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28454" target="_blank">📅 11:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZT5yERb0eNRIM6XlEEYXCqoxBSyf9Y9YycQ9cocub2bgj1zJ25O7r0wPh6Qbc2X6_2Y_XnYW0-XsO26qsUdSL7JfSmtf9tU9j6AegLs9TEUWmB5u_YPvz8jJxfHpVIdUmvPHaq8kNHx2HBsIkObXNXvoeL8jEOHTKasEl2tRCDm0T82FFpvZLb-ThQXa_MPA0LH5AUFFACu2e4GzgF6nv3BfY6Xn0u6eq68x0tSZihkUjQTKt3-v_lL4v9cVUHeVNBDhiqmDdiNrbrWdj6Er4YUIkJwxR67wVodU3RSH4Nm_NG-_Ma_tu50JiTzHACdEi9YvNcwb2GocJj25ii6UlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛‌سران‌منچسترسیتی‌بیخیال انزو فرناندز ستاره آرژانتینی چلسی نشده‌اند و مقصد دارند به هر شکلی که شده او رو به خدمت بگیرند. انزو در بازی اخیر چلسی از سوی هواداران بشدت هو شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28453" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1cD1UTRqvLD-T7hXf6ngkVA3QJpUNNFNjmMMossLCdBzxcvj4o1u5Lym1zqrZBRBZK4Ey-lYLd9oYokUzoLNEIVjYPL4924WbpSuXAY2MjPTSRpRCbTZmw4WMmmfNKWHUYUdwhvTNwCMRGNulSMPn21x_0Y1cVWWn8q2GjCGifeEJ4P167po79-e1rpg5lR3aPLwd5BKCrdeRaJFX_6D1poC7Rq0F-DP3cefmH-y1a22eyuNAJeOExcAyN3l3GX2JvoSVrwY5YobEvIFAu0xLO2H-ntKrUY1PGwdcdEZR5CnMWqMJzU2n9xRaZJ2fH_O9Bpcy_d6D1eJuABXGdRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی‌تارتار سرمربی‌پرسپولیس گفته ترکیب تیم‌من تشکیل‌شده از بازیکنان 22 23 ساله. براساس امار رسانه‌ها میانگین سنی تیم پرسپولیس در بازی امروز مقابل تراکتورِ نکونام 28.5 بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28452" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28450">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYGCEwKB9bNASv0gzrQoi1yg0KW9gp8iUC2xrj9ecDHILS1fzko-IFkVhW6e4sRqWxYe42FejpUo_-TJRhsAdGkMtHgeqBTAFigp1knzh_HDHKEVDHhJUQ8CG-mQlJ4OhPl0nCw9gDvCtCBcg3Uw2xafy-QGbTUZG3XE5lzFRHakxWgOOvwoQtO4At8qNk9eHb-X8tUAl8_VJGje3FsUJkg72uDP3QmyFzAv1EV4yNKxQ68kIJRukOwVVEEzQtrF7wekoPQeRo72ZTdHfAKCchvGe5__h67wCgbj8rcSIMcaByrPYiH7HP7qIfU-GpN1ndxGpnuKtZRIvaP6E1JFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28450" target="_blank">📅 10:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28449">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=fzK6-dXZV-76UqCvslpmahQEhPMcvthh5WJq3LZPLFP4DuTfWFWiPFiKbAbRP233TBydwFCJkxwP23gVTXyT-zapGHeBtsaHgSRtBpPJ42BVPTpaEK7kzR0JnOexHIJv_h0YZhsKdnY8QhW4AZctBS_pKn-sUSGxrlLavfjndid7g36wLxcqCIAlrffuGwaKyJgkRzE1fOjJpXK793NWYXIYHiIK92N80vH4UipvIMT-IFFq0_mAOYHxChVti57Uz06v_UwAC8b8T-lZG5D7Ldmb7BO5-OsIeuRH6XLH2G-jwc3n8JbO9fvuSQVZ25UvwYWzDnKTSINoP-6IHWjdiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=fzK6-dXZV-76UqCvslpmahQEhPMcvthh5WJq3LZPLFP4DuTfWFWiPFiKbAbRP233TBydwFCJkxwP23gVTXyT-zapGHeBtsaHgSRtBpPJ42BVPTpaEK7kzR0JnOexHIJv_h0YZhsKdnY8QhW4AZctBS_pKn-sUSGxrlLavfjndid7g36wLxcqCIAlrffuGwaKyJgkRzE1fOjJpXK793NWYXIYHiIK92N80vH4UipvIMT-IFFq0_mAOYHxChVti57Uz06v_UwAC8b8T-lZG5D7Ldmb7BO5-OsIeuRH6XLH2G-jwc3n8JbO9fvuSQVZ25UvwYWzDnKTSINoP-6IHWjdiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
مجری‌شبکه پرشیانااسپورت:
جدا از شوخی سبک‌فوتبال استقلالِ سهراب‌بختیاری زاده یه شباهت هایی به‌سبک‌بازی منچسترسیتیِ پپ گواردیولا داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28449" target="_blank">📅 10:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-RDWzR-lG_qZZRU6vAOJEWTbbORzP7wAe-1Yk5KY-Y4KNn-bX5qSlPm3IeIH9qQ_vDhaRgjXqlVI3Y9L2JtI_S_vzWbrT13Xe4lImGfuVDWdRah62ieshGY0HuOFOwQVO_9IHy2mugBmeDkQ26DB8ICdanro6OF--_Pto3nMrn8HaMXeOBvwWH-0X1NcdSigHG5a0ofK4IGOBL1trMnBfCoo-RIIPPiQAmJXNL0etN3MR8hS1V0VkX54GEfbCVE9SZWL9QbOiaPi4V-3OTpffMKErgsSXYZB0gXaM2NKO-lYjywN4l6_pkFIMGTLekkiO8kxRv1CtLzKxdzce7KBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه سپاهان به‌نماینده محمد حسین صادقی وینگر جوان تیم پرسپولیس اعلام‌کرده درصورتی که بتواند رضایت‌نامه‌اش رو از باشگاه پرسمولیس دریافت کند حاضرند که قراردادی‌چهارساله با صادقی امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28448" target="_blank">📅 10:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28446">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hTqDSGxdCZetIHcEeGXGGvnex10z--YzG4v25nrFo-UzuKENb-ijWy8t47FNuNi0dn1uh8qwSfvbdhDs8XR6OVsOFmZyErWPNK9ssEeeaJd89qWyHJG57GrKE7lGQ3J2CTw8Lsatcp83gZwtqAaBbg6VRuZuBDo3SR2_W9j3ZOyzjQTTUQ0_kj8GG3_q9Zlse19skrn_N6Tlzb3kLDJa9OH2rKUfeylB7U3q3Yfw1jnVy020HaLWoxx1hBua_ldNWfRij-TOD2xGEeHD8ZslO0Zc9Z5c446qfs0JEDfuaxX6KwpleWsZqWcWV0ZkTC07Uxs4mCOXna1kfu_ZqcVL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRPFboU3mpbXPuesMQfMVbAnB8Gm4F0SrjHVPD8wupd7s8Tqtzfa-8Lb8yDgr-dDWe2sXp8tw-xoxs7lNvXa0dWk7SJe5LudmwlQ5r5CHH8ybRzdkogD0k_qZXddcESxRBPoxRdxkO8rzuNySs8PY3_ebCn6KYOgbjhiBb4uK23znf0V_ekstnLFfk4yZjMtUljuTN-CkcXvlWZypDLbkvIwV7aUXYHoEvukHMQCumDX_uo0d-agNPR0bG1yBEBppGqzIxUvX-K2E3-ORYdWZyaUEVutK7qvXIdoGQWN7wLcFMN-HIj4Zoy_A6-Je3bcTNrNMacM2xGAwpfd9kdbWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
برنامه‌وزمان‌دقیق برگزاری دیدارهای تراکتور و استقلال در لیگ‌ نخبگان‌ آسیا؛ این پست رو یه جایی سیو کنید و برای دوستانتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28446" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrKylIO3gD_qzviTiibB-Oa8VDixS8Ypt1X7MqyeGe0UmHqU-sqXZhh8RBh9HUAOviBP-cp5fZc4ubRLYRzytnNrv78YlMrgiMUIhUX9aMxdayb1BJXxFJu14IM-BiPHF0C8SOBSDwt7bVDKEvn9CDROzl64d0Aq1ISr96McyDuVY_HlpU-MpmfWRJfTdAQ022xCE3UbeBe_ivmpIYtmBOHfP_yiJuulbGEww08fe5c5gcbfTOUYBpSCjAOlMfwax2o6hhEfMeHJoGbLd4aLZte3PXwj7jZ3xYihe4xT4MkkUsxz7-aKZnMbm7CZIGGWA5Uax_7rybO44z2QyELm2CtYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrKylIO3gD_qzviTiibB-Oa8VDixS8Ypt1X7MqyeGe0UmHqU-sqXZhh8RBh9HUAOviBP-cp5fZc4ubRLYRzytnNrv78YlMrgiMUIhUX9aMxdayb1BJXxFJu14IM-BiPHF0C8SOBSDwt7bVDKEvn9CDROzl64d0Aq1ISr96McyDuVY_HlpU-MpmfWRJfTdAQ022xCE3UbeBe_ivmpIYtmBOHfP_yiJuulbGEww08fe5c5gcbfTOUYBpSCjAOlMfwax2o6hhEfMeHJoGbLd4aLZte3PXwj7jZ3xYihe4xT4MkkUsxz7-aKZnMbm7CZIGGWA5Uax_7rybO44z2QyELm2CtYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
موقعیت صدرصدی که دیروز شهرآبادی در دقیقه 90+6 برابر تیم‌تراکتور خراب کرد اوستون اورونوف فصل‌گذشته دقیقا اون موقعیت رو تبدبل به گل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28445" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdbJ_jGNxlmz4pMlIptPJQIpRiUKvCB0ACZ0CubKqe_fnyP087nRHJEDplOdvJHfVnA8qYnWKWxM_23PqO9Fp6jYQwUPriBPDMaeP1ul7UN1pHAuYYC_ybcwjEFOBbECJkjGjm-dv53nZcSm6ilu8UChsK_jqBaTILnfK7bSFdny8XOqomRgxwlhtfZGS7GUevFADu65qboCH8PijtdoToq6RzMjY-TSDQg0sgBaEq67rQAix0oOKkfaG3yy0FIsOSltvuVvNX6jHeiiSnnrSQ96kjmPRpyVnXoSE-0DRRUqNPC11KBI8BZUtTLyslBHV6WTCxo0aPdb32h3fe2TZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی:
کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28444" target="_blank">📅 09:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdxqE6z-FrnWvT-9TQvuINwTyuKb1QfP_vIhHjpqVKexXo4mTnu8tCH9rBmffqJsqBefikZQ8UKkx88VrSBNoSghN52jxQBHEirhtoEs62jMtSjGHR9C7Jo6_FHRFTc0v5L0xWjXAjQvHtSB6Y3NDJsHhCwtrN6gHKN9Y-4vGPRb0PEuCFt3gjCd_lI08zE-sBcpS9Xa12Thnz6k7LFSXizA4LAhk-j4sgAP_jE3H6jLD8xC9tcv64vP4kJMEsU3VhQ7AkZk1exM4Xf0VE_nQknOlr9nZp_U0JoJEXYbX3W6IEnJmeEFwA_CEQZOjcKPJgMGJVOh6-pxULAfTVgzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28443" target="_blank">📅 01:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=Ldel7drWStYvk1gW2WH-uiMHvaU9JMM5Lx9V5RPymhu3jAWRjkxra1uSemBbjz-VjDQJA9ZCRnsE7FceClqRafFlee667sGnNoZYXU3OVtOWPmQw5xoIhkxIb0zZew6POp0OrEdCDzXxxDvB3mKvRz9qTlB5c7q21RywFNEHRnq5LNivbf5WJL1uNfY8tuMeP_F5t7S1iBkn1bGLoJjvej4J3AdV3mJ0F7ntG4YSD8BZlg1uiBDjf2ogWalqP9W8jftowJ7drlz8WATZszDBPuDemp0ghmNGSCKDcoTA4Q0hkM_lkADvU1FbHXH9Kc-oKl2bxHUfjpenl7erSSBRV7tBW-Ygiyo4l5vrWAS_KCONQKsUvr5Xtobmu0yQ4JKl-2HcSpHA0TpWAT4xT-QFecowXLqekEFDD5RiPj6KozBq1d63DM0dIJdBoEnnaIg8Kx34dZx-JZ4DmViI2hP8ePSK1GkO2aXB0V6A45ZyrPB0ZPvWi2fmSNjbZJJHwQYCH8y3BxGgf6u1SAdXLYhxoABmn5Bf85OT-pik7cZHnGV1S--cB3uxE2dSz6GUkyTTJy5uFRB8yIyHmeCuJPw8qIUceD1l2AJO6VRlx5owhDOW9EhtSNaHajSaBgdwdSTWVwz7YC2WORTgsBIKUISr7bQ5dqljMqLqhRQ5u6m0_RE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=Ldel7drWStYvk1gW2WH-uiMHvaU9JMM5Lx9V5RPymhu3jAWRjkxra1uSemBbjz-VjDQJA9ZCRnsE7FceClqRafFlee667sGnNoZYXU3OVtOWPmQw5xoIhkxIb0zZew6POp0OrEdCDzXxxDvB3mKvRz9qTlB5c7q21RywFNEHRnq5LNivbf5WJL1uNfY8tuMeP_F5t7S1iBkn1bGLoJjvej4J3AdV3mJ0F7ntG4YSD8BZlg1uiBDjf2ogWalqP9W8jftowJ7drlz8WATZszDBPuDemp0ghmNGSCKDcoTA4Q0hkM_lkADvU1FbHXH9Kc-oKl2bxHUfjpenl7erSSBRV7tBW-Ygiyo4l5vrWAS_KCONQKsUvr5Xtobmu0yQ4JKl-2HcSpHA0TpWAT4xT-QFecowXLqekEFDD5RiPj6KozBq1d63DM0dIJdBoEnnaIg8Kx34dZx-JZ4DmViI2hP8ePSK1GkO2aXB0V6A45ZyrPB0ZPvWi2fmSNjbZJJHwQYCH8y3BxGgf6u1SAdXLYhxoABmn5Bf85OT-pik7cZHnGV1S--cB3uxE2dSz6GUkyTTJy5uFRB8yIyHmeCuJPw8qIUceD1l2AJO6VRlx5owhDOW9EhtSNaHajSaBgdwdSTWVwz7YC2WORTgsBIKUISr7bQ5dqljMqLqhRQ5u6m0_RE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛ پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28442" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28440">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmODgK-EMB-bm-WR9c24aV5FRpbTNVgB3aKIrKEAZrKgmwURglN_MVrBYV_OAFOIirLCx_X8uUsa3abYdFi60dFm06CNyPhvoO7_ygZdNw2mAjilBZzJqJHvHa08YtzgazQtOs6QfR1cr7qcbXD2X2i_jwAGUjt1nHwi2EMOLZNrIZZEq09iRS_ZO0nWBVzAeHsr6m8eeb-c6dzMsyy64A1sC2X7j5UcKfwbcHyiiyXwp2HX_oPYaf1JZCGfIiDoxOOgBFbLeitpDBqNVQQYvADhjW42HH-4yuyMKEx95WnNRD3LXhjaNB9f8zBnatIedYwJfFXt0iSfEoTtkgOaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
فرصت صدرنشینی یاران کریس رونالدو با جدال مقابل الاتفاق در هفته سوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28440" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28439">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emUuphzOpmI7Nh4agufNZVtlX6syAUleJmxYNXI4UK8evULXlHeAhIBwcizxg9u9sHuoakWjb9pQ8pgbE-tQrMD9mcQg638OPMLL1FyP58M73XFuG5xO4msiemeEywal47TInynecwHOmec8Y0-obd_DJzl5kCMavHbcz6aKL_fRXuIyD-UCI4NIiZWG6gIUmi8_ivzBt_z3aRXqQQkJaibSUVG1UBKPufwTNUso1HzVLZmf0fOYqLUYDHzpGIdFXzJk30ar_Mj2pVgFlRoVJfIZVugRJ_l9vOc7zJk-nL1h75xf1LYaxdPvlNnX79h3XjZkWID4CKV6-bRl2xTyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌‌دیروز؛
شکست پرسپولیس مقابل تراکتوروبرد ژابی‌دراولین‌تجربه‌مربیگری درپریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28439" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=OfrE3OAdPb2yB6dx2mJazMPTd3kkWxA5BIGtNd4tJd9C6WRLlzM2sHf0ezpNhc1qIMsOAq-me-ItCvdA-iRbpMt6AFXYQ5Nd1UA_y2ZpsA4y7U9s6rl07kmYFxX_nkNzHAMl0RFJ2McoQRxMyt40CPfQjuHPdTQd_gjEkooSJUNXb2rxByp83Fp7IgyqK1x0AnT-dN_Iez9MkPYBV8KKDLrhLB3NxikqyjDAft8kMdtsY2caFIWb-VaOQARLB3xvJgbjUjQR_FI746Hd4uulgowTEggL68aSK83ZIUXvC5OJ7tbDDOuosWYGHdq45SetSZQB2PfoAr93Py_DhyCmIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=OfrE3OAdPb2yB6dx2mJazMPTd3kkWxA5BIGtNd4tJd9C6WRLlzM2sHf0ezpNhc1qIMsOAq-me-ItCvdA-iRbpMt6AFXYQ5Nd1UA_y2ZpsA4y7U9s6rl07kmYFxX_nkNzHAMl0RFJ2McoQRxMyt40CPfQjuHPdTQd_gjEkooSJUNXb2rxByp83Fp7IgyqK1x0AnT-dN_Iez9MkPYBV8KKDLrhLB3NxikqyjDAft8kMdtsY2caFIWb-VaOQARLB3xvJgbjUjQR_FI746Hd4uulgowTEggL68aSK83ZIUXvC5OJ7tbDDOuosWYGHdq45SetSZQB2PfoAr93Py_DhyCmIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
رامین رضاییان در اولین بازی‌اش برای فولاد به این شکل پاس گل داد و فولاد به گل دوم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28436" target="_blank">📅 00:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28434">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sgUanxSdlblGal2llXzVqkwPnwA6ev3P2jPe_MRB2ZkdXmEs1A_MatH5o_n0EIT0ajFN2MeGGYZakN-ahfpkJanQ1bwfPz9lLKviOUV17syUsf1peUFamN-qNVwTu3s26iePMaOrH4uEwafQtUie_MGEdoXOUdtmjamfMXbhy_7K_KTrJn2EvxlOW-r8GS2aJbvhDrAy3cNAR0ryStfwEZSD3UWZBeFQ4vVIX9IWZ9ff0SJmlG1epAvAX0vb58Z9eFopv8cCogDkRDDpTiB8P4x0ngrh1UtTIsgdqhR4HfnPLVaGjbyibbw4PQG7Yw4_Q0_goIN9ZQIsbeg7FOiOzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IV2Ufn9k6GrvWebHgEZXjTNl8sUor1p4vhtL1m2Hnly1dcgPRsX2oZTpb5Tj5lhJyk0TziVt6ucpCSU-qlAGtXcltbMeup38-djTSQB64j3vieJZGhmNPo8z7ktoOY7E1VB2718euUG3y8KPShKjTHwSuWEKbW1mrN1gruP803n4xoo1K8Oq_anpKcjrLb8GsjMNlbIOS0-VsH8L-nwsqeFaSU_tVFjgwqJOzvUR3LEuXAccAe5nYF92mjBggraCqUi4ao7bKF6hHyCIFKFrC4DrsgW-jJqhLiULIya6y6e7q56mRWalSOajWUC7yCcydGJ-2SvwrwYDanHj6zpTYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛
پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28434" target="_blank">📅 00:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28433">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBNu3bmRo35fd2gc8-jjIEeYCKOkZMFmevnsDgQP1e-lDV9-BwVB2gnwfumyAWaUcR8OQcHLEDyQgTuiGPbPuUT4tv870AGp2sZRSIgqStkFs8kAx6HozApFbyv58TQe2F7HvtZcdL-RZyJhzZUWqSWt5-NZHK9apRBV2ym1n6Vgmq-SHSm4xpPzcV8pHp5kvWaBtbfQlzqFe1ZrnCeXoFBjwUIaREqUOQmEIdLaweZCEhRJrJ19Ag-3LA_CBGncXRUnx1QQHSlicEp8dnMfkDwIXCrE9Xc3V9gIqpMXF-3GTT3Jqe8cVTZk_qETizE3Qb3WEBBMeS6L1RA2IFOUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/28433" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28432">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdOGYnVyYGbLPCfdGZqiLgE3xgOHVKUvF7XQ9NV5eUrcELOlKkqsOArI15wEcPbc6L992GLtPrKqfO_gvTY_0hedb7akAlhvlBXkO8h_j_imh0lHekXBfuybk6qvH2xYNgjaQ3XfJ5-Pt1G36Cp62PvQ9D_EHuznzXgGB7W-yoZllkQxYbNN1y4GfQSwkr2mA58FODO6S9owA8FpQgHRkbGJpKUIClC3DKRz-qJnWYP8VGY7PmEs0eClI69aNOtX27p0J2rvJhacODRFwiAlyBrIsC4CIDJmld1RncSwFMlAleml5f04dwf5fnyPju0SV-nfh44QrSeHa_gf73eK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مدیریت‌باشگاه‌پرسپولیس حمایت‌کامل خود را از مهدی‌تارتار سرمربی‌سرخ‌ها بعداز شگست مقابل تراکتور اعلام‌کرد؛ حدادی مدیرعامل تیم پرسپولیس اعلام کرد که کادرفنی تحت حمایت کامل اوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28432" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28431">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0zP6Xo-IiRI8jM-vR4x1HUw1G6cJnAhwn-RyzMEP7u62lCk6PCQuCOD4n6Jzz9GeHvGaBFAeAqIn7CSzPgZtJTrMiF8B8grBhHBM_qNaN7j26H9bfvgf77Ml2kBpJMyMtTJnttRKEFY-1w-Sv59xcXA6jiiL3uGwurytJ8HLahhAHPkBL8XSsyWSMqrNF5gmMOKHZkqTvdrxszxT0znwS77Z0THZnIxNppwy9GkEKCYmzK44HA3lq5OPx43-xAytIAaqbzL9V_5ObsS3RYqnLBBklxH-FS7l4hBUts5HufvtniXKTzPVYpI-B5e4HSfIdvF_2EW2n4m5n1yGkl6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28431" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28430">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206c65214b.mp4?token=dk8i3Ea9TlrAILmi03ir28A8KpMcbfJXocIbPWcKBM5AAy1e2pSe4fjRX-HkOrWDF2XZ9cEL90JaoPJFBi49rPwBYz6D7wYzxMve3zYGXvmTISMWtJWALMwCFrrXnSyTTdx7A4dV2puB3EiRFTD6eTklkwGh5-Y2qH7Qsy0gIfjzr1cn-Li_xxPRMNgo4Hz2ivVacb6to7OQYDWK3TtOQG8LEgI41sgrgJ0orm-LBmzR1NbWCPLFbJMWRwAqboOQ0Nj-JrfN43E6yTp0BOJTpQqbiJZNsRr9C8MVBGtEByRrFUBGUCvpz4t005eLkAXxLQjv_o7VW-3LjxAIho0GZ3NW1lN9KjbN803Kq9pas1kOt9ytFTMRDHAuUNMzYh8e_SzXVyRpe6yl2ejUTD8scQTzARZ6u5pb3frJP9ZInyB6Xycyjk3CvD60-7KLImkt1tKVlUtlD-1KkDkwXclENkMwCLdDcvIznBtqjRDdqQq1shptW8hb9j65L8NxhFKUgGZjlZh6sriCQwrA5xINfKbQrwJmvvDskP31DFtq41cQuHUtJs8Xb2nal74eFPGhtU9v8NOMMP678EdYZ1eyaVhXcr7g847sw6KyryiZHJ_35H8LAB83ycmuusCDSds6jKBZYtehh0lBWukvDP-hb528A6Stssgqd52BPzp7Lc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206c65214b.mp4?token=dk8i3Ea9TlrAILmi03ir28A8KpMcbfJXocIbPWcKBM5AAy1e2pSe4fjRX-HkOrWDF2XZ9cEL90JaoPJFBi49rPwBYz6D7wYzxMve3zYGXvmTISMWtJWALMwCFrrXnSyTTdx7A4dV2puB3EiRFTD6eTklkwGh5-Y2qH7Qsy0gIfjzr1cn-Li_xxPRMNgo4Hz2ivVacb6to7OQYDWK3TtOQG8LEgI41sgrgJ0orm-LBmzR1NbWCPLFbJMWRwAqboOQ0Nj-JrfN43E6yTp0BOJTpQqbiJZNsRr9C8MVBGtEByRrFUBGUCvpz4t005eLkAXxLQjv_o7VW-3LjxAIho0GZ3NW1lN9KjbN803Kq9pas1kOt9ytFTMRDHAuUNMzYh8e_SzXVyRpe6yl2ejUTD8scQTzARZ6u5pb3frJP9ZInyB6Xycyjk3CvD60-7KLImkt1tKVlUtlD-1KkDkwXclENkMwCLdDcvIznBtqjRDdqQq1shptW8hb9j65L8NxhFKUgGZjlZh6sriCQwrA5xINfKbQrwJmvvDskP31DFtq41cQuHUtJs8Xb2nal74eFPGhtU9v8NOMMP678EdYZ1eyaVhXcr7g847sw6KyryiZHJ_35H8LAB83ycmuusCDSds6jKBZYtehh0lBWukvDP-hb528A6Stssgqd52BPzp7Lc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ سردار زاهدی معاون‌نظام وظیفه عمومی: علیرضا بیرانوند ازمهرماه سال 1405 سرباز خواهد بود، و باید ازیک‌مهرماه‌به خدمت سربازی بره؛ زیرا مهلت معافیت تحصیلی این بازیکن هم آخراشهه و بزودی به پایان میرسه./ حالا اگه یهو زدند معافیت تحصیلی بیرانوند دو ساله…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/28430" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28429">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkfevpUv2sawhjFj6jJCUbB8F6guorQPzUPUpZdxgwWwHYyoSRTLbYNKSNIXz3hSCcihhIfvSVQywICAYatLcf7NGm6GcfL5oC5u1gYnANGWX65_Jw2sGZNWiZgRG4vGcbnCMvp0KZ5W9xERq-9uLxwgL87_gwcM7lWrXqRUmnTOMfMb97bVcqrsk48Qo-vLrR7pKPktSv5qlQZ-eM-SvBKjIkx3yabIA2U_O-HvYOreRXwaoXfAaXXnx11-ANv74itwULcYcQ84_X4b2JP49NMpvIXsUyFicXeiQiBWFCyyiHU0LaE3bvKIbYUnMMeMQThzyqA0u-fxSRxmoAMRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28429" target="_blank">📅 23:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28428">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkGDr4tFXcY1eSRs4pgYk15UHUnU4KQ2l60Pjf7SpmVYul52x7DGbV_i9FT3YzHBUwipHxePa-TvT9T2tAlszFFqD_CLZIwLqVpLhWjrj-E55PBIDV6W6ib-b0zw6BohGbx54U4gGRMsNsn6mf5JMIKExru8XHscNyAyKSESzHzw8Ms5OsOC4mfq8DRwxlYBllgF8EY5tUJL1pUu7TkwrJRWukzLhaHbnVSS0-oJ8urJDh9xRj4LHmhbOQJ85ZaLjD_bVNtL1iLY7JHgSdWAmznUYDEvDAly0hzXFRp_3DC9aOwML3spHZInmoXCg18OJyZ0TeqMSciTBYstIz_L8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل مارتینلی ستاره‌برزیلی‌آرسنال که همسرش گفته بود رویایش‌پیوستن‌گابریل به رئال مادریده حالا درآستانه‌عقدقرارداد 3 ساله با رقمی نجومی با الهلال قرار گرفته است و موافقت خود را برای پیوستن به الهلال نیز اعلام کرده و تنها توافق بین دو باشگاه بر سر رقم فروش…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28428" target="_blank">📅 23:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28427">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9vNtIRylKOjD-orrXD_evEniqa28QZgwPhWUrWRkc-Tmd_s4JSKHLXy8dnrMZrrPgtsxbSblki1IDxEOR15WKOPWbbGjFKiJ30vY2bfk9yEIEuZQozgoAlpDPR5vgOWcLynF5QKnRgDaSWW7dBtB0HIU77AMJslYC-f7EVdJNSvpCTStV6dUesbuduL9Kaztf4RgKRP5TvUyZKcByhpm6H3ZcDS9hZqKG29NNoMy-QYhMzikYU2YeonKXeGiThD55_grAbu4JjJbn9qb8Jv_vi-D9i1E_AVj7veLnAxHIyJaXz4y9fue_9JJYlXfXMh2rnd31C7RMlDrUTqYZtfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28427" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZkPlqamnrGyhaE6fFR8lo2pxfrbqbuo_bBDim5wemgn_HDaBtjm0JaTu8ve7gDQYTg_pBbtJ0h5e6AcgSFlo_nJxqZu8dmqX9qzJc9G2MdmzwLUXouBM4xEGF-jO3ROS9Ht0ohbLUid18ZzLwI7ypkgAbs191QBJippEEm6NqNPVEiOI0Zvi6u4dha4ofxq8_s_QGj8IILH5L0UHB7zstYmkIrz1NJwmP6S_rJ-1qvMt7CQld-qxInwYYOyw_0gkC4OZuo22WWw6WZuXhVfDsXaWFQHKMwumJPBGvVy85LR4GoRABuHutXfLupbvy02EMa51MiXTWTmFEgpuA9ywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvzC2BQ-ZCqJyJcrlgt382Fl-hD_EbWgQCzgVEUudJA3XKPZmBNAsz9gwncZH7bl5Ei7mFHpMaO8v3k2fq7f6v3FRIvahdiW0rxpxOieJHXkS747f08uv8PZKnFshl1VMZKJhEmb9CB_EcH_hfRHBkyvM897NSf2UAvkbLZxEDCFJvxneSXu5NiW-q29QWyeQXrQz3ZxZLvOjJf1gvco07yJ7gfUMHatCgLaeoTPtugyAuWD03MLb0DzAajL6Gv599tBip3za0opKSBlW0m437zj3ZfhTRKN0TEbcS3iNLutBeuibHCr1f0pof_r743s3UQ2a8c8UPSA9dRzyl46vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28425" target="_blank">📅 22:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28424">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-YnZPacc7Wsd_G1yIvqLfIkchcqxJs6bqRrFtTEfsNVOVNIrwiH5UvrxpkJnuNtqS6vtPwk-hgh3hG_z_avIsNJ2HVkbgNkNFYlQx3pF6MxsESTqWkOHoiCu_XW0iQ5G3a9Ja7BnKe5xH4BpMkD4YHUZMLGSGL19QVQESoE-sHWF7CGXWrTCYE0gwtyYIyQXtDjhkaKQSyk3I9sD8b5cIp_9gNTOP0SaBmk189NFFHVJCInRvpp6bO6frNOTJ78yzz4JRkUwIf__oawJ1cUfF5lKD4NbsU8jEvjN2jCxZKwX1pJ2Mtaolzg2V_Y3cgN5NOt5HEYHyk8RQXZl_8NhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندم خدمت سربازی در تیم نظامی وجود نداره. علی رضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28424" target="_blank">📅 22:07 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
