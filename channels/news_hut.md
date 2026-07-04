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
<img src="https://cdn4.telesco.pe/file/oQEi69z3ULo_fds4nRrRbpvuByIXQ9rDRbpu3m2Oe4BKb5g_7rPCjDN6aaql_y2uuOcF_8dJvI-HxezUzicOda-sPsU-C8Il3XbwWDyQ5GszK99uWSSYg_TKr_N5exytDJ85NwISRTNqAqcRIz2CWRcR_GFNSDAfmezR3JP3CHVWUHRtXWyUl5z3uKxFSQ4-LuDcHk0ZG-MfmV5ghglWRyxbFCXgrBrIIiWUCKMZcUkniYYn8-_JyM7qncouf-qj9WVfdi0vhA3blkGu16wgpfXleqi9gNUIm4gycOGL3HCX2N6FtplN0aEtu6HTPxRRDwLOpKWDJy_tip8tycqoaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 208K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 20:24:41</div>
<hr>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=WQUwWoz99UiGmztqBwkNl7jbE_mpCO7WnsYaNBL5hJ9uvmK_PyP5ewc-TrNOqU860OnjrARTOjdE1HYEMoIUfb1vGS6-FEiwd4XKQGt35MW31KBGLOvsIJ3ReS3OUAXjSHdwZbNxcMv8f9yhCGHxBJ1eLIyE70SbyrGfJ_YjV6aYk14TLdyOn2Rx_S6KzsN0wVtiO6u04X_7MDStIJ1mNqMb27MGMA5Guwm4NODnb64ipJo_9lMM6s1S2lzfhERwJn1_JS1ZEARdFiAGNLJt4ziQFDT9so5LtmGIo3Cjt2p4kyh00Lk2ULzzaaJBH3wK23n3W_-HJn1rJ6GGpAualg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=FmBhrhVutt1Qzz-dVQKGQLZ6wz-3lLvUIenIpYPvNCmsuvhn5glaMzKmyC3o7qxmmLn6pGBOWWo1dGcbCs3-H1YhCP0djhEr1q3RDoPiV-LYZtD4W98CpJDAzuagXIDjqTpMQkEzFfvPLTLL7s7o9XOMhLoR2bJSlR9T8uAmy4jvxizcG4XJy0X4u5Kwv9Prb8UG69Vn3L8ArHZY3c_zmNdU2-vsrhhwo-clixiB7cKxOdoKYqlBBYDt85g6NZZX5PFL882sqGiVXl1eP353-MhlUJMzKH5OT4WYjhrK2xs9bhC1c-BmlFEInPjr0a72sA0ORyzZcqet0fEUP2hjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=FmBhrhVutt1Qzz-dVQKGQLZ6wz-3lLvUIenIpYPvNCmsuvhn5glaMzKmyC3o7qxmmLn6pGBOWWo1dGcbCs3-H1YhCP0djhEr1q3RDoPiV-LYZtD4W98CpJDAzuagXIDjqTpMQkEzFfvPLTLL7s7o9XOMhLoR2bJSlR9T8uAmy4jvxizcG4XJy0X4u5Kwv9Prb8UG69Vn3L8ArHZY3c_zmNdU2-vsrhhwo-clixiB7cKxOdoKYqlBBYDt85g6NZZX5PFL882sqGiVXl1eP353-MhlUJMzKH5OT4WYjhrK2xs9bhC1c-BmlFEInPjr0a72sA0ORyzZcqet0fEUP2hjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MgiucSsvFFl0NOL7cy7_Qe4XJETURcKemrVYsPiqs8GvHGkGe7lriQrXgue2iU2Cvkm0N_IMpIy2Og2IR8q99aLGT7hrXcVy4BNw9xlVhhDXBZJYCt8RcSSzLbH1iJezs71Y5bYOQxhX_FKdIIvKOPwbq-xljUPP2OGGPOp5iLSRMpkGwbgiymZy9A_0TUHCmMhPuw8o66aMWAL7_ZdQRnU4ZZEkiUpmD3WLspkt0SEYCBUUmYSB-EhMO7tSkGRReQRuUmmdEr0zUFJgZtLdgCtAIk8JPglxlgGCNgl-WaBE2lfHdPufNLvJN1dyU9sE_ZUK-xccR768s61U3PoHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=MgiucSsvFFl0NOL7cy7_Qe4XJETURcKemrVYsPiqs8GvHGkGe7lriQrXgue2iU2Cvkm0N_IMpIy2Og2IR8q99aLGT7hrXcVy4BNw9xlVhhDXBZJYCt8RcSSzLbH1iJezs71Y5bYOQxhX_FKdIIvKOPwbq-xljUPP2OGGPOp5iLSRMpkGwbgiymZy9A_0TUHCmMhPuw8o66aMWAL7_ZdQRnU4ZZEkiUpmD3WLspkt0SEYCBUUmYSB-EhMO7tSkGRReQRuUmmdEr0zUFJgZtLdgCtAIk8JPglxlgGCNgl-WaBE2lfHdPufNLvJN1dyU9sE_ZUK-xccR768s61U3PoHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch4uks0s2zIVQQxXW699xzRqEv254JCxDX8v1oXz6EeHET-fdEUTVkQEF9MDnvBZVIZ2S5FkSv54CSz5wSXel_7u8X2FA3JAIasdfUfWUKXCiRqL5l1f5ZIVYklj1zmAz5PSgYNIN5O46175NnQOKZ_XchNnG5fZEuxD6ximpI3N6Qlm0fzuM_buZqSqwU82LPgPZtc0Zwur3T2OpuYpbqrTTDd9AMe5qBXsMLyGfw2b8LQBgwZuIoKAJvdIUZ5EhVfz860B5BMqbHrAmyCgrhmCxtnbbQtwcmRodEIv-8Wa8G91kDV29lvXTh-vHw7fKqIRlCbpDrcAagCUX9autA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=jYf5GfRilneeIpeA0ARnlENbCLUHiyzElTKZQr6r4pL_kaQ_ENC0_n4T3IOcT9YmDG-mnigud0A31H3XPCScAzoJNPjX4Uacw9MeiKusXsfmm5HBQ669dWe42USG1HrJ1PPDtoAAXo_oE51uIfAQLsoh9Xn0Xb7Gh8vm6_AqFC7ys00CPpFhO_0iBn-c8YTbcpbhLaJoB2iFs6WoqHLRlolERH25o0yis5-P_KsIBPlOihckVH3GwdEPNBXRSe8lOl6QgI-ifPOcOFjrdgGWJAl6jpacBgR9M29ipgn6dgltDI7NBR4FBefG2RxSMFLBrWW7Vt5KCPxswHu1oyCzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=bgyz3p1ptKzPwxTIjoUf8lPs1x_B8XUbToXqN0ViV6RnRmB6e86m4djJGCTDAprjslFuWODDDZiO29ad-IeOnlU0jlfrcrsRY6thlIKoJiZ5RvOrsVn3e2a5R4hTwpCtbI0ClEhbtLQZBpyv4ErIq9BQ7EN2wsLE108yM6tat7uzBhTUJqLktEd8GRaRY6GO70WwvQgFYxU3FX680Fiw6RPelzOsUKYBF6na8F5Dw-c0ROpFUPEJ-z0m17AkQuFo_KW8SBjgKCCTDmcFDqHroiolLeNaV9-G4k_PJAiRbGj8hrl8XM7i3vT81QCqo4CG9inWWZFPhxsy7u1k907Myg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=bgyz3p1ptKzPwxTIjoUf8lPs1x_B8XUbToXqN0ViV6RnRmB6e86m4djJGCTDAprjslFuWODDDZiO29ad-IeOnlU0jlfrcrsRY6thlIKoJiZ5RvOrsVn3e2a5R4hTwpCtbI0ClEhbtLQZBpyv4ErIq9BQ7EN2wsLE108yM6tat7uzBhTUJqLktEd8GRaRY6GO70WwvQgFYxU3FX680Fiw6RPelzOsUKYBF6na8F5Dw-c0ROpFUPEJ-z0m17AkQuFo_KW8SBjgKCCTDmcFDqHroiolLeNaV9-G4k_PJAiRbGj8hrl8XM7i3vT81QCqo4CG9inWWZFPhxsy7u1k907Myg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=nUhlwvNj6Y2a34NR6AnbAvy3KL_RisINbxHoi4wswDnH1KlUC-w5tLPAUIweUQhtnxUjw25X6BiDPpa_w-MGZ_rbmhoJ-WsdHnhk3j1U7IiaMQU--AOcgAf7dp4w0pf3NY7EwQDUTkzJZtHAle9r5etxDrvapeSXXhF55MQtCiKFlnWf_qQy-HEs-kPJKG9g2UjSpPink0OK18eZoe7Q4BqvTcVQ-uz_PRRzJdppqiRaGx3tSzz-touW6vAIN13pt5trZR_VZSXMf2xcy3Xgr40PtV5c4onWjTqZGGhKZTim6fNoBdcn4KJAxs87h13gvQei6hfuRx4kvMTrmXHnyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=nUhlwvNj6Y2a34NR6AnbAvy3KL_RisINbxHoi4wswDnH1KlUC-w5tLPAUIweUQhtnxUjw25X6BiDPpa_w-MGZ_rbmhoJ-WsdHnhk3j1U7IiaMQU--AOcgAf7dp4w0pf3NY7EwQDUTkzJZtHAle9r5etxDrvapeSXXhF55MQtCiKFlnWf_qQy-HEs-kPJKG9g2UjSpPink0OK18eZoe7Q4BqvTcVQ-uz_PRRzJdppqiRaGx3tSzz-touW6vAIN13pt5trZR_VZSXMf2xcy3Xgr40PtV5c4onWjTqZGGhKZTim6fNoBdcn4KJAxs87h13gvQei6hfuRx4kvMTrmXHnyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhNQxvXJGp96qQSWVsHq_JCN2Sqi59dUcD787YkK9b0u9usp5v9RiRN7KCa8vQDHYdwfSirN5GBN0f-GAk9U8XMZVFa52hu0Z_XcsAgpBhfeYEoz0jcm0NpxOpfwvhMCVSqRLsyTfcUbySsCKffZp2PlWCNqT7ZnWV4955FubEBgG9-QdT3o2Uz8T3dCZ47U7p_mZ5zQ97j7kG7K-DVPMelDc5qrNuxkMjY0Zd-632wq_HRCoplE4-XdvaQZT4vq4ZuluDyEzW6oAx4ZCn5w3dEKTVEFXrAVtNbCujkVIVF6SI-Gzujww2YiF8lrHVsTvpKMb4-6EhWrakY8YkFVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P32dGYapydeF8T0wd63U16X9S5pQz-lzDzeDEJZq6dEefPDS9WMoLsqIrpUuS5y2VESmyPJcKQ1_9LtsJf0HE8mH_HRs2U6kEYVFLAqROU49jzXs9RCfujqedTr7F62EZMUdwp5d6R_YvC91TeAs1RAikaw8gCyh2KFn-Psn1E7hQMuRygYMII4HhfDE6t58yJ7eMeE8qXLZ8S_0DHunpvclrAweqj6PjMA4H1W8wnPGYgjNr7hwfi0ryZrcWtAZHNUPCQLvXvTD9dZaHTXZpYq2Y8gKIqCaIb1O6aH0VR_NgwLKR8MPTTfOMA6mz0XBP8dAyKjLvWVKxKgQFjBWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C0B2YH9flLjdZ_146yiq3Wu0HWds5iZkNxFCgENccArUHKTbyr1wOgVE_MTG-tnIQVCL9GFn5w6L3cZaswBSu81l22MuU9V3-SSxbs15ts0xdgzwHWcslaXwf7VxL_7b7d8K5SKazPkrNBfwKysGY8ajtjylZ2pk1OZmeW1zu_x1F_Kd9-avtByPr4Dx2ggSuMGRgaxzI-Tj9QwFanJeq72DMcpx9ZbLj8iDKOxLt8jC5LDRKS4aAUnANF0LLI7Aqj5UH51v7h_kd6mP3TYPrP1GO_s3R3BCMPb3c4H2G0_OPeDwQyjmQjWfsy39PqWD9x-QEJd12p-d9bxDBDm5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6-d_7sjQtSjaJbjAwgK192HMan55eY65mziUAErcSMXzTxOQ0p_XsYKX3IQnKxO5bHYDgoULkXRuQlUd2tqoH5fdi8hW6uolGwSoQLe3o0NlfGA5bEexbFS7FdTohMkz_RWz8epEWEqWyyPqBiQaGK29xY5GlPhci3TqfntiKCHGIHQ0fwxH64T005do1Otu4Iggi9NspbPvMmKxtqOLNXh-W-ZEw4ZD-R9_ORAK2CulsE89W1_AH9gp8thH5_j4pUgfT0nMxwjxj4W2UTyI2npoq70SA8_uv9vBaqrlmNnvsY4MdHsO7c3HPH-7WW5co6aWp6mnDeNrtaewFwVPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=c-VqMxYHk8bAx_XSiq5GPuLKk8E2VnINdxfWVAKLxXLNfg5BwEKEx4Pvx2s7ma_19qW4HIgsmaNXJ9GpiuFkPqmSyQYqDYaNy9rkoZy4Ysei1lBqNjWDDDw7c6x-S0xZil8pIlGXfA6hWzsopB8SFKX7nokEdEI8NX4I7wiXIAiNtFVWQ8TZLMy5exT6sglIYSUYzEAQzQ8A-l6lr_UtlH5OQO52NKX4eulVmNoJK_bU1DijD2AiLdR3sCyNz-8xB_0xDkXXKQkUgwo3UfjwDgYgsgoTdKZZ_S-ZMpJcCCmiIr-jfkH3T1wot6ntZcY0FLS7HWpS92I363XauRsP_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=c-VqMxYHk8bAx_XSiq5GPuLKk8E2VnINdxfWVAKLxXLNfg5BwEKEx4Pvx2s7ma_19qW4HIgsmaNXJ9GpiuFkPqmSyQYqDYaNy9rkoZy4Ysei1lBqNjWDDDw7c6x-S0xZil8pIlGXfA6hWzsopB8SFKX7nokEdEI8NX4I7wiXIAiNtFVWQ8TZLMy5exT6sglIYSUYzEAQzQ8A-l6lr_UtlH5OQO52NKX4eulVmNoJK_bU1DijD2AiLdR3sCyNz-8xB_0xDkXXKQkUgwo3UfjwDgYgsgoTdKZZ_S-ZMpJcCCmiIr-jfkH3T1wot6ntZcY0FLS7HWpS92I363XauRsP_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eak7R0FXUkNxsieiZlmub8hdxKF_A3KYB1vRwxeZkK3y46AdcXL3iB0ByRa5z-EeZ2ZN2GZpesVv9qbivqGdeoCZp6gtWimWF4R0BM-mDfk9kGdAAaEosKoRp6XxyWWHiqdyF_617gsfd6C3aiNojYWWTvWA4KgkQfxLiUXvxweUh7-fUFM6qezDrJ7q31sHR-bNn8VhhhT_zjuvvfwJ-Tcv7vvniolgsbZIrgkaohomG0UzFzY-ASXnP_WsJQ50aT8cdzobSt3q-TBlivSMVw1aYPoYQLLvcUZ6eFKAOd_xrA8DrVBYJ99NgzTb5eGFycJpucRE9dqmWu68hMHPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6T4xuzwHyquX2gmfs4tUJjFv9pQ0j59wrnpon7yybAdAL8bO9_YwfR4BPNVr1zObVntL4vI7jqwJkrWsI_RM4Oy7X3SXL47bsUsBjAhLHB5_kghJ-ZnALCCtdXcCxljbQ7wvmnJ9nrE3y7gls6zU9DW54qRiRV3-V6imkepMBXuDFjdHSAX6vVvTyCSvfuPXGrJomKyYgdN6RzMkylrrjX97uDgIjUZymar7c4S6DHvpyFZHX6MesUhu4ho9zyiO2_0eX8QAeHcK1OrKGrc_BRZJz0oglJTWCq9Xw6Eldom4-gHFourw6N2Twp9wYxg7K_Ce7IGTpp9OfFrYB7KOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBQAoWe53VRAs_nSCpUpveb7Z4tZegMKXHRKAJZ9An1ycGqgpfFS3W3xWFoRibr9cRPHHJ3r7jDmTojekZqpBJompfBka0F5BQXOnXgGIJMjw-QKKQVdeKo1AK1vuqm0d3rfzBaiVEYm66Tc0WiGe9gIymF01ST4hRVnozErrdRwiNlWZU5o0kWSM2CC7aQ7RsQZHnS7ghB3ex0v_k8B6BDJj0XQs5NOge-dYCdZ-in1hlRmNzQIVtFNmyZHfejaHgLttQLbwY2P6h1W4_J0uW_dtfWQib7l-YJmlV1VMGMH3fe4dGB3TaudrywSyMULCLfWojOSjX9D5-GOTEvQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=cNzTaMO0Tu0tJQ7HfzpZG31OqzEEKXpIho1Qa6SyG5nuXPJ7aInzwuAhh3Tjf6ThItStYx1liPdzqlRydx0sAN3N-bY2_3BLrVFZvRpcCUvsVipopjZ-WmW_bYwBdDCioel88KIvDPoZv-VxpV-mPGR7PdM14MOJz7ibjuB0MQeoDf7iRd6wSH8MhyiHNnacgoYvo4GyD9SSPUDsPigH4weranspoMR_w6Wy7FF_wI33Z691hIQZ6SKbMutse6r1AwxVDBmxosy770g88iGwXay3acOz_dH16o-l_LGYfQQdxROPv_X6s-TA6mwPFuUBZwnphQjzQo0NCZEN0Y37GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=cNzTaMO0Tu0tJQ7HfzpZG31OqzEEKXpIho1Qa6SyG5nuXPJ7aInzwuAhh3Tjf6ThItStYx1liPdzqlRydx0sAN3N-bY2_3BLrVFZvRpcCUvsVipopjZ-WmW_bYwBdDCioel88KIvDPoZv-VxpV-mPGR7PdM14MOJz7ibjuB0MQeoDf7iRd6wSH8MhyiHNnacgoYvo4GyD9SSPUDsPigH4weranspoMR_w6Wy7FF_wI33Z691hIQZ6SKbMutse6r1AwxVDBmxosy770g88iGwXay3acOz_dH16o-l_LGYfQQdxROPv_X6s-TA6mwPFuUBZwnphQjzQo0NCZEN0Y37GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN1iX3Dj1ejxYuAiEbe7JJwfvrugjvL6IbsGjau7PNlnxoLO1TJiW5jzNcJGZOwbg4dVkb_RMiNf2w_hfWEa6BnVw6HJy8t878wC3-wTwaYtokbYDpS2wEhoxQFram6c4Dp-Y9RXXrev5IUDmVN2GOzKLFGMO9RMppcLQCHgDdkTnMRK3wjzcIYbm6srCQg_4_IbpSSimFo_sghDfmY652B-YhrF84QXy8ElaWmki0O2xTqXYHpXYrvJTo9Wfnv6PGl8zLOdQ2NBcEYYqj6VAG6sczHIaoDPfO_eJGAp-PTWOMD8CWoCJJfCvhJYjawDFujik7kqLd4QvwqmAfzckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=paXbUW5nWx391-Jv5M85FfS7aBJlUt6oY7bKWIdBwm9lmSR0yblaJUH2WT_iYBZABEh9nAUHnEma6ZyIpmKnMgScL2Hr7DlAtvHKGxncgoqHVSICBib7RI_j-N6dx91jwwAfPEAp5Lngf0hRvHplYAPWfyRd3UIrUWILES2c_4pGodDFzEHNTxW-zhETMxkcwwkpofcjDeDAiPUWgOiILv6ccYALOGlm3BkWU3Dxyh-llJxjnqeJA-O3B3eTy-wBONb-Y5luJDU8sSWyUmnMSntuggGh65EcXz_uvGMvB9JWeLu4mf3m1uJVsHhVyF3SiiD4sW_dXHRYjQqi1HZhFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=paXbUW5nWx391-Jv5M85FfS7aBJlUt6oY7bKWIdBwm9lmSR0yblaJUH2WT_iYBZABEh9nAUHnEma6ZyIpmKnMgScL2Hr7DlAtvHKGxncgoqHVSICBib7RI_j-N6dx91jwwAfPEAp5Lngf0hRvHplYAPWfyRd3UIrUWILES2c_4pGodDFzEHNTxW-zhETMxkcwwkpofcjDeDAiPUWgOiILv6ccYALOGlm3BkWU3Dxyh-llJxjnqeJA-O3B3eTy-wBONb-Y5luJDU8sSWyUmnMSntuggGh65EcXz_uvGMvB9JWeLu4mf3m1uJVsHhVyF3SiiD4sW_dXHRYjQqi1HZhFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=NR8Fxk4_CgCbtaLhTrK3GEgB2eBkOldtKg2TnEqTeOv_p7YaflnIXiqKjOvkpD6u1LLwc2RHApivs2QjiuhTtGMMpuDdf_Nh_9YY5_XvEnmOM2zxqBZqv9MQHZvlM6K2ySa43cc3mcydrcSM4mPdjsECrCZ8WXJYbFLksHsJM5Ebr18qFzj17l4cy9RCJFWzJPNbWtnX_JCVtJA8LjtqL_rWp511dKFG2XzyAPDMoxeJCWvpy-rjk7mjxqJDeROC_EkZ1Roy7p_Vso5hJt9NBqOzwLqL7wDMzw1XBuqq12G-yORdbgavCKTF_fbRFI1qWHuj5Jc9aRl0_LUkMmXpuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=NR8Fxk4_CgCbtaLhTrK3GEgB2eBkOldtKg2TnEqTeOv_p7YaflnIXiqKjOvkpD6u1LLwc2RHApivs2QjiuhTtGMMpuDdf_Nh_9YY5_XvEnmOM2zxqBZqv9MQHZvlM6K2ySa43cc3mcydrcSM4mPdjsECrCZ8WXJYbFLksHsJM5Ebr18qFzj17l4cy9RCJFWzJPNbWtnX_JCVtJA8LjtqL_rWp511dKFG2XzyAPDMoxeJCWvpy-rjk7mjxqJDeROC_EkZ1Roy7p_Vso5hJt9NBqOzwLqL7wDMzw1XBuqq12G-yORdbgavCKTF_fbRFI1qWHuj5Jc9aRl0_LUkMmXpuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=uv5iWYkStHwjOYuu7H9LO-wpf14oE62VboJwWYVFFdQpG9tm1LMZpjkBqfnyft0Rubz-uzl9wTgrqo9b2ITt1vdyiiHle_6KcG9XTQN5cHmU7HwcNj06LpDpCCG34zjL1ynmXvZ-bCUFplM7vxJ_3VRKcbbkBRFj0dShiqGcLTQCelixEMa2x9OncWioN4RRZsG_G22gnrhynpVOqvLsKh8vRPgrgSQjS4kOpXifdAK7uSLHk6PHTL_IfQv338Q0rTZnGEQbgMTmrJSPhovIik2LgesJ7kD3yVjCnSbsX9HBqmm7kbI8qZR4Fx_SS6UeHGwQ8P27iw4czDkqE-GksQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=uv5iWYkStHwjOYuu7H9LO-wpf14oE62VboJwWYVFFdQpG9tm1LMZpjkBqfnyft0Rubz-uzl9wTgrqo9b2ITt1vdyiiHle_6KcG9XTQN5cHmU7HwcNj06LpDpCCG34zjL1ynmXvZ-bCUFplM7vxJ_3VRKcbbkBRFj0dShiqGcLTQCelixEMa2x9OncWioN4RRZsG_G22gnrhynpVOqvLsKh8vRPgrgSQjS4kOpXifdAK7uSLHk6PHTL_IfQv338Q0rTZnGEQbgMTmrJSPhovIik2LgesJ7kD3yVjCnSbsX9HBqmm7kbI8qZR4Fx_SS6UeHGwQ8P27iw4czDkqE-GksQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=vjnL6rQSmmKXZWF0mm4phur1Y5DcF_Jr1hhXVV-anSFm3nRF9EOkYEERCmGJA5JzLk4m-WtjWJO_IAhrltex9akHkqQh8bqQs45EAkmYHWupHy4lCbhe1OUOFqppjl_IM2POHaaa_JdcE4_dm50bTuTr3mXYBjkf6gIKzeNZHpUpsx1BncX1kmw2vxeS08S74LuclmoR9WhtYi7Jz6F5uciqp7TNhNWtwMNYktk697jITRfhI57j0x7JOzucAzhXEXt7YrOwqwZw9QbWowJv-ckW0WIedRgl-bv7svOnWllL5djTPnW9mCw7YLJReWIZeIGC17-GPpCQemkjcJV5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=vjnL6rQSmmKXZWF0mm4phur1Y5DcF_Jr1hhXVV-anSFm3nRF9EOkYEERCmGJA5JzLk4m-WtjWJO_IAhrltex9akHkqQh8bqQs45EAkmYHWupHy4lCbhe1OUOFqppjl_IM2POHaaa_JdcE4_dm50bTuTr3mXYBjkf6gIKzeNZHpUpsx1BncX1kmw2vxeS08S74LuclmoR9WhtYi7Jz6F5uciqp7TNhNWtwMNYktk697jITRfhI57j0x7JOzucAzhXEXt7YrOwqwZw9QbWowJv-ckW0WIedRgl-bv7svOnWllL5djTPnW9mCw7YLJReWIZeIGC17-GPpCQemkjcJV5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=JSZII4__NY8RAFKgS-AB_KDMpyQt9sGPV0WiBxGwqM3kHd0qyOsLQOWyUn8oUsk8bY75JyYaT9e-y-ttpKxWiIGvHndeUFFXd1D-sutrmp4edNr3Ai26KCEl4Cf11qL1ptcxjuVVSHcZ6-E-0QrA_V4dZGU5_niihcaWMGEzpg7pVfvbgA0pgB5J1AWWcEYE9LuNE8k4Ns9P7aDMtaCHyhLnHNpUf34KYPCLSJ-uy9Hc98hEbH3bJtwDePMc12NDZlcgIsnFTWn0N86IDXSbiJmgdXMk4chFl2skvVHF3O-f7nECx4rXU1--un6ckAdRr3khppI9Hoj-144nauk_MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=JSZII4__NY8RAFKgS-AB_KDMpyQt9sGPV0WiBxGwqM3kHd0qyOsLQOWyUn8oUsk8bY75JyYaT9e-y-ttpKxWiIGvHndeUFFXd1D-sutrmp4edNr3Ai26KCEl4Cf11qL1ptcxjuVVSHcZ6-E-0QrA_V4dZGU5_niihcaWMGEzpg7pVfvbgA0pgB5J1AWWcEYE9LuNE8k4Ns9P7aDMtaCHyhLnHNpUf34KYPCLSJ-uy9Hc98hEbH3bJtwDePMc12NDZlcgIsnFTWn0N86IDXSbiJmgdXMk4chFl2skvVHF3O-f7nECx4rXU1--un6ckAdRr3khppI9Hoj-144nauk_MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=H9fUbzcztJFawHoH6hyGuYpAhpiH3Hghs3qE7zLB47s4hCaDHjfHAIpuRPiqwk-sgbk7jqkgKtG2j7LwdwuHuUsN3mSNYOjmQnZy0F29UH7XzqSDFUGaaB1Q6-O12u_wNA38KZiiGNxLfqdOtmcEDM3YJaRYkAzO0QBoLBUDhgrAgWXqjLSUpyO5xl6N-yUY63zrRnLuLFeBGO64XrKPiGlsIT1kMJcMohEFtNEIxCxyJj4UDPLJ_gegZIcY31unPnc0c0TXYONxWjq5WDRYztHrCJ2w0qoQsQiGWKj7a6Z5XPnk0t4hlZavs8x-Sf2C4pqMEWIsLcQ293p6kZFSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=H9fUbzcztJFawHoH6hyGuYpAhpiH3Hghs3qE7zLB47s4hCaDHjfHAIpuRPiqwk-sgbk7jqkgKtG2j7LwdwuHuUsN3mSNYOjmQnZy0F29UH7XzqSDFUGaaB1Q6-O12u_wNA38KZiiGNxLfqdOtmcEDM3YJaRYkAzO0QBoLBUDhgrAgWXqjLSUpyO5xl6N-yUY63zrRnLuLFeBGO64XrKPiGlsIT1kMJcMohEFtNEIxCxyJj4UDPLJ_gegZIcY31unPnc0c0TXYONxWjq5WDRYztHrCJ2w0qoQsQiGWKj7a6Z5XPnk0t4hlZavs8x-Sf2C4pqMEWIsLcQ293p6kZFSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=CocrshvbFhAX5cjUFFwnerLQpd6VkZR2RrGfh9MRMK4Z1b_xU6CGNYFjD7yKSZzpU3B3co3LfYwPKSOJ69CHfGY7LwMpdME66z23BRycReWi42Bwfbk-rIXUU_6Zvz9fEgQRr05DG-w7BJVLauR-Jc45dXKS9CY5TOcporXPnz8deYb4WP2i3kPAqdp1gAkvLHjrKYqgWqo-HDpW89sUX1vISVWUN3E6WvFz_eIb5CDnA2cq82JBV7Je1lLtouaReWnL3IibRN7LU03uENV_0XcjI3wNl7_ehpseZrqaYVgCpGJ6B5kJ5y9vyFSykFjC36PCpodWZdmCmPFPLDruAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=CocrshvbFhAX5cjUFFwnerLQpd6VkZR2RrGfh9MRMK4Z1b_xU6CGNYFjD7yKSZzpU3B3co3LfYwPKSOJ69CHfGY7LwMpdME66z23BRycReWi42Bwfbk-rIXUU_6Zvz9fEgQRr05DG-w7BJVLauR-Jc45dXKS9CY5TOcporXPnz8deYb4WP2i3kPAqdp1gAkvLHjrKYqgWqo-HDpW89sUX1vISVWUN3E6WvFz_eIb5CDnA2cq82JBV7Je1lLtouaReWnL3IibRN7LU03uENV_0XcjI3wNl7_ehpseZrqaYVgCpGJ6B5kJ5y9vyFSykFjC36PCpodWZdmCmPFPLDruAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OutxxGle3mtfwXHEwXsCxTgSY1EirC9nRYihqiP8e8LnPZFPmciOEympaVs1ZvwHb9sryBRA7N-Eo4FUsJ3Eg9lNcSSFGN8ff4IYCetMiXf3W_yCd6XjkaA64BKkaLKxiAw4RA81y3vhl0rYcmvBZBKQFn1Ra1YC_KIKws3BH6gSqcQB6Cdn0QEf9lwcG-VuqYVuqmv7MNE-7cvKs2Np4xj_VRXRSLgxq6J-cyYM58cDePxpIGtLXwE-xRooqCuFyCxJA8g-hOAVW6un45Ci5p3INDv9mRFlPXGvweMIoB9tBgAfNiauj8qcIDk9EihpJfxdQuHyDnpLWQLJD9zwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T-hMriPJjHMPfCvM7Am00div2hjYjUpbZBobq_VyGw-lYXPIvelnsFjzM2VNQeNYVimkWV4dI2YHBMZjgh2LQlOEQ4L6G5XWh1q4xHzkeOUMdRKXu2UQi5XTC0RIbae1NIc2YHVOd0crcOpHlWhsJCB9CQYjiJf77-I7oNU3ODwuleDW-Twwczc4C4rG-WWG5PwephVUT16r0EaLgI-t9OkVec3oacDjKRn0ebHfd_IJC3QHzYDLa6NM0j6SJKhrfk6Trl8OiQCwneGVQvmqi1lWqd9cLmGitmp_c9E92dz2-XpTLVLZJ-munjg1dCnvrVefa-S-jEkYKthlI6MAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=Uf7vLI7XxCIMDSZ76T53S7eI1i3N7Jjqd-Ww8F3j0TzOITuwDtqHLmHOSPVel8CvLV4XMXEYFKEvQpBG7jmuMxgGvMd_9iWWS-B6Te-4t-Le8UoQpclJSP1QxwcHOiPIfz16NtuUi-dhPM75x3xQOCymdxrUbCYawieUHzlsR5hVPAqAQIapZ5VMDr59O3IR4cfYUaoXJTWx9pZP7pEQuaDNVDEtYLrdnfM-N_ng5GDHq8UPPzqvNkmfhyXV10o1Y0DFY8gO65OdVzcbtAgYYJ2eYprSrEqn1FUFxeNfYGF878ip32v4nKjyfEb2qbkPeGl8rjGcU5q0Eel7P4ADYrBwyvlLXsqtwJiPUQgpy_MCYh7RDU-RLThF6ZgOxyirTRZw3kKP8b7tMPdwCrvqQRYnVuqUDl0_XIlvM_9J6DSS4QGg9U2EvBqaeaq0CR0ssdWoRU4LTRjdoVx1ca3DPq9DbU_sPB1gqL42S-Qzu-uIvCLJ9BFHnezoGWPLN000MmBZI6weyyX3jMEyfEXmk6WkX_F_QjcjmJWLKopenT33JmcEsXOvwD2eHAVcwqHByJNHAhOYMWffvfZgSAF27X1HCtsp9YPhPflBnmUymIrBlZAhi_kSRSwN-9o1GFdi1aXZE-QqI4WPi6CIYeO871O95Xwk69Xo2JIsp9TfHZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=Uf7vLI7XxCIMDSZ76T53S7eI1i3N7Jjqd-Ww8F3j0TzOITuwDtqHLmHOSPVel8CvLV4XMXEYFKEvQpBG7jmuMxgGvMd_9iWWS-B6Te-4t-Le8UoQpclJSP1QxwcHOiPIfz16NtuUi-dhPM75x3xQOCymdxrUbCYawieUHzlsR5hVPAqAQIapZ5VMDr59O3IR4cfYUaoXJTWx9pZP7pEQuaDNVDEtYLrdnfM-N_ng5GDHq8UPPzqvNkmfhyXV10o1Y0DFY8gO65OdVzcbtAgYYJ2eYprSrEqn1FUFxeNfYGF878ip32v4nKjyfEb2qbkPeGl8rjGcU5q0Eel7P4ADYrBwyvlLXsqtwJiPUQgpy_MCYh7RDU-RLThF6ZgOxyirTRZw3kKP8b7tMPdwCrvqQRYnVuqUDl0_XIlvM_9J6DSS4QGg9U2EvBqaeaq0CR0ssdWoRU4LTRjdoVx1ca3DPq9DbU_sPB1gqL42S-Qzu-uIvCLJ9BFHnezoGWPLN000MmBZI6weyyX3jMEyfEXmk6WkX_F_QjcjmJWLKopenT33JmcEsXOvwD2eHAVcwqHByJNHAhOYMWffvfZgSAF27X1HCtsp9YPhPflBnmUymIrBlZAhi_kSRSwN-9o1GFdi1aXZE-QqI4WPi6CIYeO871O95Xwk69Xo2JIsp9TfHZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=asDJXVhOXpY9kbIPT8mIMPWvg9g_NvUGxQVc-NhTBtDFghnHYUqC0MS97EQciQc23XAA_7Fu4A6CpLa9dsL8iENb0f0Y9lSSuSgRjvo6IHFJ0aDGv79Agk1oTOqp1kWLK8jdqBDOrffC1_4__v_US0ggeWSZNe1mcn7QbHRG8lhfAXhhEB2mo8hOI6W8NR7WpSIUJu4yiTVAkK-GOwqCJOWXikDpvUDoB_A5ndJCL2nx_qB8EjG2W5tNPnH3e0W7jZ3MLWnH_ggtbkAfjJ9jTk70kNdNuE-gQt22SxZQg0ifChXiCLEdFxlO5Ifl84N26LDofzpfWyJnZOlksAK2dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=asDJXVhOXpY9kbIPT8mIMPWvg9g_NvUGxQVc-NhTBtDFghnHYUqC0MS97EQciQc23XAA_7Fu4A6CpLa9dsL8iENb0f0Y9lSSuSgRjvo6IHFJ0aDGv79Agk1oTOqp1kWLK8jdqBDOrffC1_4__v_US0ggeWSZNe1mcn7QbHRG8lhfAXhhEB2mo8hOI6W8NR7WpSIUJu4yiTVAkK-GOwqCJOWXikDpvUDoB_A5ndJCL2nx_qB8EjG2W5tNPnH3e0W7jZ3MLWnH_ggtbkAfjJ9jTk70kNdNuE-gQt22SxZQg0ifChXiCLEdFxlO5Ifl84N26LDofzpfWyJnZOlksAK2dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=dgttWbNvN6m9W86w8la-dCIdtOJEJENZ_AmYYIdvWSv2m3X1E9aP1HH5VsP56_GY2RnbFSqe-wF5WnkhGbZUrtB2rN9cEvQJjHhv805qHgPkbo4_PCe1mcWnzFcoVhE4ilKRXfcGRELY7ebxAWb1WyJXMn7XdiOyD23M_r-LIPmOx0HtqMwDugOf1ydEZxzqVq27a-0oNqV3ljftYxYxRCTT_jc14sPdZSW024yLqeOblFbQkrBZDxJtEpW7zyF91DG6ZUa05voUxpqQUdT2PrXp55hGMB-IIUaFQcTEOe2vANd5Zqc3phweaj_d4HVqxgnr6QhX8l_I7Hzwi5h0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=dgttWbNvN6m9W86w8la-dCIdtOJEJENZ_AmYYIdvWSv2m3X1E9aP1HH5VsP56_GY2RnbFSqe-wF5WnkhGbZUrtB2rN9cEvQJjHhv805qHgPkbo4_PCe1mcWnzFcoVhE4ilKRXfcGRELY7ebxAWb1WyJXMn7XdiOyD23M_r-LIPmOx0HtqMwDugOf1ydEZxzqVq27a-0oNqV3ljftYxYxRCTT_jc14sPdZSW024yLqeOblFbQkrBZDxJtEpW7zyF91DG6ZUa05voUxpqQUdT2PrXp55hGMB-IIUaFQcTEOe2vANd5Zqc3phweaj_d4HVqxgnr6QhX8l_I7Hzwi5h0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=sxfPvfa1X0GTuVuuRUBo8bNp8qf2gmjUVMdriSQ00on26wL_-YLTD2rcO_daVmALkAxLXGYWIlSk843Tm4JKKdFbGL1-9NwhkxNGoC6-a-8ciKsy2ycq3TVJKf-sQrubpp-akd6sR4B30Ul1vghJtB52_Xp18inScZrpC6AiftSLSGhH8IxsITved2hYw2J3Xy_YEvBbK0ebJ7TEdM1J4XILseGlVsWt9GaZklJbQCTNbig_Wg3zs33hvX3fj4tBe6Hc6c_-stGP85c-4vJYJ2Oco8MixiWZhXu9RUJizKo3g_jF69au37M6GCuNY7Rj6iLTaViROPC7s4TN3oNpzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=sxfPvfa1X0GTuVuuRUBo8bNp8qf2gmjUVMdriSQ00on26wL_-YLTD2rcO_daVmALkAxLXGYWIlSk843Tm4JKKdFbGL1-9NwhkxNGoC6-a-8ciKsy2ycq3TVJKf-sQrubpp-akd6sR4B30Ul1vghJtB52_Xp18inScZrpC6AiftSLSGhH8IxsITved2hYw2J3Xy_YEvBbK0ebJ7TEdM1J4XILseGlVsWt9GaZklJbQCTNbig_Wg3zs33hvX3fj4tBe6Hc6c_-stGP85c-4vJYJ2Oco8MixiWZhXu9RUJizKo3g_jF69au37M6GCuNY7Rj6iLTaViROPC7s4TN3oNpzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=rHHiDxAR-7ByFoV-IdeUJ9mv_MniOBh8g-OKJuUIVNIX8cQmyU4HPhEjD7VgsrGS5DGpkjPOBf2F5JUStOMLAQOKdIIc4CE22Veeo-z-4Q4_KaOuV-oLJxNca5g1lJWGRcTW5eScVRBa5yvFbDoCS9pIScSUbiyx6hm8OYHZUw1o3irFhn-xlVA_BSs1CxTAbINCQgTg013OMCwKR2lOs-mBBbrNSph12Trks8iM-ukbxVP0fEpn4HuBZcOkZLbln-sK9QPubQ6EeuqbwF3r2WCdjwtPu3mlpHkw0TbcslAX_q8UXtZFfDOhgpE-vlFpo_DcGc5I8qqg6XAEUBDBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=rHHiDxAR-7ByFoV-IdeUJ9mv_MniOBh8g-OKJuUIVNIX8cQmyU4HPhEjD7VgsrGS5DGpkjPOBf2F5JUStOMLAQOKdIIc4CE22Veeo-z-4Q4_KaOuV-oLJxNca5g1lJWGRcTW5eScVRBa5yvFbDoCS9pIScSUbiyx6hm8OYHZUw1o3irFhn-xlVA_BSs1CxTAbINCQgTg013OMCwKR2lOs-mBBbrNSph12Trks8iM-ukbxVP0fEpn4HuBZcOkZLbln-sK9QPubQ6EeuqbwF3r2WCdjwtPu3mlpHkw0TbcslAX_q8UXtZFfDOhgpE-vlFpo_DcGc5I8qqg6XAEUBDBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAqhq0BIjCQPQ3cRGUXeJbHpI9vilg530-C6a9LVSwET3Ebmd6cMo8d9ldWU0-r1EhiZ-KhkazygL8ZMj1DvH_0fgP5F3GEYfyNWVm-MVoSG6nOS93ZGDYDj1SKcT6eDqqJA7EkzCpdspFBafOd7s3DggNHKxfc19d9kRhr_pmdBkhkrpqeGwPA_b3ej1EHnsHUjL1PLgwt0C9WaIWLetiyDYDKIDYXocpotViVstyH0VPKIiguNJgUalpT5L3kO6nktnH-FJDGDF_UYXtKDQYmIaHaRUs-H7Rp37b9oH647FbXFw6TF7nU-ZFqrszomfPip_zQgxLQDlS0Ho4c5HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvOozurPtJdKFiyHLxJQphemzX-b5m45_lkFoCNIa76wYVNdbdL3S6nwTztYts8gfxXKar0YPb4KjjoBQAYV7GP80em0x4EGecARD2tAeNLVxb3ylg1ZTwOo9thw8UJHAfVYBNUrlT5PS-6tBWr_oFURMSIYLi1V7g-bA4ceUWzFd8WgOzUe84TjqSxWzp_8MFoNQ5pJbOVNaRQapreGW_ZLVAnFFFeyrxSfoyNJyarzFmoFe0jI_V3j7D0rCEomAy7D5f-VryPf7MG4h0vguSij5vw4SLWtAXY88WvFggxADnhA0j00YQM-dA8i73xsFL_g2eh_iutQu-8WFjkvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is5U7Uh8PZbSG7Qh4p9fJk_i0nTJoUk-ma3_e65Dyc1KvSQ1xsm70gygYEL7gpnhL6W_65DKoAaOpvyeQRQpdqjuWttbjsa0F4gzlb1KvtB4HpHBOvmUDuhAMWqZiCka5dmr2XCbqOhkv9fFmLego9qaJDekw5spgF1FHPX7jy8OE_UEOXiA1L1FJ5XX_s9H_snwpnusN8J8ps1Vjw1lJzt8QKQj66Be1iCZhLfLPy7uqdnJBELX0k2g8PAv_opd-edB5WrlSBi7h20lqwxxLLDAJFkQRlzyCb4ErQKAa2Ycf7nqiqVQntE_dZWdB_HvJIJLNEx52Aui4yO7BT_TTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tETMuSsgAxSY0ruUbeNklVgnXUWMQqhJjVIwRSalaC1eBQ-9xHahgVzfc7OO4BwQM46BXKK7rCEvF_WFlL6ZvA9idgVARxH7wYMoPqwHWbGSJl0ldUUiVqD06UR1MSjkDMzBgojOFXJeFWowq4rW4tqN7VIv_EjwA2DSbR-V7n3y6nYfpANOxh6bMBxa4guOfkgAOnXnMKrbcS2p08DQomr1OpT5Fqz7rVY6PVdO04EAzO4Or0eK3RAgsbh3Ttj95w0liw0K0Mo9tnFuPSQJm_JLU7zdiwD5F7HXxSpwORHaEzkJ9-wX4rti2s5lekdMdxIDCKjpgRFexr71tYw3sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyh2BlS_CZr7XJ43S9Rt1RSQyX-sbxdJL7PZmsvUJVqwUvKQqsQSWmWbuRKCEIgpy78XAu_-fQuMVB1qCzF3oY6BAGil-steO4ktnbBH_KnioKygszE9OSr4VuHPRgw2AM9RYha7w-I_EjlghD0KZ_QW7ienzxfVGPnNonINR4q5Jx0nSC0Y2LZ__MkL4fA7rEpbD1bkPbwFvT7p8qsGt0ibSXYfUafXNBbMtlyDawjmpo9UcgBa3-ZFEiNnpeD5v7lUqEQ3p7WWP6UcAvBpUmT1xoM-fmY07ibFzoCckxXxBUfdyHRLxbj-hPw1k5XskFMNq0FLR-87ZulXCW1W6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLoM_QCteXs-g8_T5kep7vFT4j7HKAHdz6cShETY41BLriS1S2EnaBpvpqmzUreHFZ3tI0zwAWXGSiEh2nqi5hfQssm6T5g_al4O2oZw4FCN2WL60CsCg0K167QYt7cnIFDBv9YUzLg6dUl6plcgHyYWXDvF06WH_jwYM2nHquHhW5Yiq3yjKv0I0MtTZ7jOLxV_lYWs43fAk3yugBmqVWvt4Ct9_96aE-QdGqDEJ0alelUIjf73zSgBFUNejO9Ukc0-azAP17haowj5d43BAVp01dsr5hOwN4LUKD952Ao7I3GOOJI0cag0p4RKLcq79D-JRI2oGzrF4UOiUzxmxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=fqMNQCrYrY24loxw1fEO1NSFw02fH2u9sXwnddg8Yo4ks8fxl1s9DDQm9ReFd902Z20ouQD0B3PwRxoE65k3Q4gY0PFGQqqMIGR5kZBdqQP5AI4tS-ghcsHPfZbspKMjpb3ioW7_m1tkygTl0bs6aQuC8zUHf1huBj201xwvu02tza1Exv-lzn9bWyYncxulbmoDtbBmb3QZvTc9IHFrGZXLzvakV10_5mlBDHCgyX8kC6VUbpZwEEJ0BonSgpyfHJuXkJ-3mGTE-5cRoX2G4sJDFemX8Gkm9lcsqQR6eZIMcPOe1MSg2kvQOSEPAgHHs38otduolBOw8NftbXnKcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=fqMNQCrYrY24loxw1fEO1NSFw02fH2u9sXwnddg8Yo4ks8fxl1s9DDQm9ReFd902Z20ouQD0B3PwRxoE65k3Q4gY0PFGQqqMIGR5kZBdqQP5AI4tS-ghcsHPfZbspKMjpb3ioW7_m1tkygTl0bs6aQuC8zUHf1huBj201xwvu02tza1Exv-lzn9bWyYncxulbmoDtbBmb3QZvTc9IHFrGZXLzvakV10_5mlBDHCgyX8kC6VUbpZwEEJ0BonSgpyfHJuXkJ-3mGTE-5cRoX2G4sJDFemX8Gkm9lcsqQR6eZIMcPOe1MSg2kvQOSEPAgHHs38otduolBOw8NftbXnKcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ys70ujEpL3KRoNDTybqgitFbQqAUZhjG2kT2Pood6pTFPSBMlioFktfjsaqro3tqJUpt1fQJgoqNR5Pe6qARDDu862WxKw6HRomwOZeisnlhfNPmhUp3laCqfT7MimMUnwyDFAmadhJBFTn58_RQJvAOXqQPquGu9LeS0I78H1o6puVwcCAp5xjlUz4-TkQb1pME2i6VdC94qwQL88BP3y_IwctiKDp1gFcUera1fG9uicOYx7MClPcbGDHiTlY5mCMIkakqnnKMtEUP84d6KZUrL5Fd6SnDpHKTw4qCPNXiRrkZprjW8DgBl0UtVkGg8OEhvE6rFWcJM4DmPUD-rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=I_DEXaplvxz2gZFpW2AtY1kK5pCSIzpqiHPkmqk4LoDnZR11g3f-08iC26v44gGvOYZefW2oyiC6iG5gJid3jWh5U9hC5FpF0BmyAoPiZmNhGEM-F_vqjFUj71iXmmI8IWun6tsJmUegTHaGGyeeZyneiyTmqaoNhw0ezPsvOXdjK3-GUmcf-9XzvRER0Q2zpioTtjeaSgG1TIGex3k4lQ0Q0yLws9ZChWoh7FDPiM_wfE6dV1jqPyYzaVN1tA0t6xneKvfULScJUIFJ1L90y6_Qgy5qEdczWa_gV0PXKukAfCnuA97V7rNI33zFpBakulKckl5RWA7mHSl0nMa9aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=I_DEXaplvxz2gZFpW2AtY1kK5pCSIzpqiHPkmqk4LoDnZR11g3f-08iC26v44gGvOYZefW2oyiC6iG5gJid3jWh5U9hC5FpF0BmyAoPiZmNhGEM-F_vqjFUj71iXmmI8IWun6tsJmUegTHaGGyeeZyneiyTmqaoNhw0ezPsvOXdjK3-GUmcf-9XzvRER0Q2zpioTtjeaSgG1TIGex3k4lQ0Q0yLws9ZChWoh7FDPiM_wfE6dV1jqPyYzaVN1tA0t6xneKvfULScJUIFJ1L90y6_Qgy5qEdczWa_gV0PXKukAfCnuA97V7rNI33zFpBakulKckl5RWA7mHSl0nMa9aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=CX7HUc1MqfDRN5WR1opM3DK8sQi9K9b8BiC45PZ9ARNLqZ5jcjewmq3YxaK_9BBiHrajyHrM1QRKQikzgWgW36SaaqC-gskXde4cUAN2B6u3Novw1OouVjJ5c6_H5_2bzNURZeL475f_USaUxiw37i6c37QPZltjLdV8TDmo4mgO1oCz4b7QEQfiMw3I8C8j4UyZnQ9aal3jfXqdUs_zkaFT_V07GESTa1eRxo1VYJ-OMCMrgquIEzu--3hTfXJeKzwqAKHKi7cIEu8cgc8iOsA3BegzrQ8lKzuk_KwxDfGjUU0VsFFxVxEhQk3EarDIXA5MSDK3iWnHwD35s-nqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=CX7HUc1MqfDRN5WR1opM3DK8sQi9K9b8BiC45PZ9ARNLqZ5jcjewmq3YxaK_9BBiHrajyHrM1QRKQikzgWgW36SaaqC-gskXde4cUAN2B6u3Novw1OouVjJ5c6_H5_2bzNURZeL475f_USaUxiw37i6c37QPZltjLdV8TDmo4mgO1oCz4b7QEQfiMw3I8C8j4UyZnQ9aal3jfXqdUs_zkaFT_V07GESTa1eRxo1VYJ-OMCMrgquIEzu--3hTfXJeKzwqAKHKi7cIEu8cgc8iOsA3BegzrQ8lKzuk_KwxDfGjUU0VsFFxVxEhQk3EarDIXA5MSDK3iWnHwD35s-nqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=YvuE8I4XGukkAUF4SZE2x1lplVlkOPsR32lGfGypnkpQBGpwGmBm-AesmlRiiUKbFh-TbXckoiwXWQDPE8NNWb37e8oOWf3ZEqLnnrwWNAmd3sXZePkhWdHYXfMLUxZTxRD7iXtIPFm66L1ZYKIMx598k5XyDY9rUkvr8TV7lDai7_d0PZWQK-mEkxYilW1VCbpRIwu7J_XdRvUpalORCRN-N2bL4KvTVncWbD_HNTdmvRCOqdrmX5c_E_T19-2KY2qEy2_gcENHwE-DWWIWImroTKPDGedktskXt9uIuMNFtXIysieiIDT1Ce8cIr-TCV7kJ7H5JpjDUD0nf7dB8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=YvuE8I4XGukkAUF4SZE2x1lplVlkOPsR32lGfGypnkpQBGpwGmBm-AesmlRiiUKbFh-TbXckoiwXWQDPE8NNWb37e8oOWf3ZEqLnnrwWNAmd3sXZePkhWdHYXfMLUxZTxRD7iXtIPFm66L1ZYKIMx598k5XyDY9rUkvr8TV7lDai7_d0PZWQK-mEkxYilW1VCbpRIwu7J_XdRvUpalORCRN-N2bL4KvTVncWbD_HNTdmvRCOqdrmX5c_E_T19-2KY2qEy2_gcENHwE-DWWIWImroTKPDGedktskXt9uIuMNFtXIysieiIDT1Ce8cIr-TCV7kJ7H5JpjDUD0nf7dB8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNBcA1fs9PN4xScl_kLzaDVEHYIrTuSAZgX4W2tN9Qa1qIfCE4MM9mj0JTWtwLCuegBo2V-rjQJk4g4PFo_FXFJqqvQhSvpERF96012yeL-EiVpmGRbzW_H_tHk2F5iqFNi-YEZFuWnZyfem6TI4a4mpG6uwTjbeCcDeWQt2KMXj5Yxi-OF8BAqeplW3G97c6L9hCqPRFREeGhpOSM5jzriz85VHWGmGN81kZQdMUpXfeTXcW4q5oRkK5Lzd31Ei4quK3RxEJJBHrrL1Ki4Q_rSvEqsUDqgZBX2lCbho_Es2HKssKMkFIBWTV9apHoOZ7g8MeVjHbMKgzK53Jv1cOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=Ui64vEGK_vdWALt-TQ3WBmsaXRnats6a20gdBBf2fuFqxT1JrOID4wG995EJc2yBLhNTfechqIYEOlrPmithFWi7fXOGhJP-15L0BJUDYL7b1mZB3mSZHynyLHDMjGWv3LxT8Op_kDu8vl25cKpeA1n-7Ig7VWN17obp2LCHxXtSXoh3PvWS6N0tJNqi6F0whcTRJQ1XTi5l9DXjngPlncs0hufVAQVXrazSO2v1Dp58S0JZgW5BQZuv7lSTDipBnRZn-d_NZ5kQIbufWRfOxzEB57g78CWHsZvcx-cIuWtBLK734GLL05NNVL-wcadJCP7X0qdEIMZ2bxp6ZQxq-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=Ui64vEGK_vdWALt-TQ3WBmsaXRnats6a20gdBBf2fuFqxT1JrOID4wG995EJc2yBLhNTfechqIYEOlrPmithFWi7fXOGhJP-15L0BJUDYL7b1mZB3mSZHynyLHDMjGWv3LxT8Op_kDu8vl25cKpeA1n-7Ig7VWN17obp2LCHxXtSXoh3PvWS6N0tJNqi6F0whcTRJQ1XTi5l9DXjngPlncs0hufVAQVXrazSO2v1Dp58S0JZgW5BQZuv7lSTDipBnRZn-d_NZ5kQIbufWRfOxzEB57g78CWHsZvcx-cIuWtBLK734GLL05NNVL-wcadJCP7X0qdEIMZ2bxp6ZQxq-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=L9z_638f9nr6c8s1R712B8WVqhYfWaW-h76PIDM484ZcUQMBDbOQvFloApn7kXxNOLyVvzGb9E_qpMxu-K8ba67mbPrFmxBDZnlgKc9I1ZDdl54-hI7mntinf2FzV79HJZO2Uhb3PoW3qmwc9n30BFSBtBeL-J2YKUWk09uDTdKIuEkVqXHnabaJ6aCb9DTsqUHXchxODeXIpSPywXjUEs8SiaQlJDrSrN7DSJizWz8Pf05UFmeYQOeBF1I1r5hWQ-ECc4pnpi7BG6G-0bq08ljUpUlzVGrGEwvB0ofSv8H8aCSV4Hv0B-5GZThhElHSdX8B5r4baLoswJhutWPg9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=L9z_638f9nr6c8s1R712B8WVqhYfWaW-h76PIDM484ZcUQMBDbOQvFloApn7kXxNOLyVvzGb9E_qpMxu-K8ba67mbPrFmxBDZnlgKc9I1ZDdl54-hI7mntinf2FzV79HJZO2Uhb3PoW3qmwc9n30BFSBtBeL-J2YKUWk09uDTdKIuEkVqXHnabaJ6aCb9DTsqUHXchxODeXIpSPywXjUEs8SiaQlJDrSrN7DSJizWz8Pf05UFmeYQOeBF1I1r5hWQ-ECc4pnpi7BG6G-0bq08ljUpUlzVGrGEwvB0ofSv8H8aCSV4Hv0B-5GZThhElHSdX8B5r4baLoswJhutWPg9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=KDd91t62W-yw8Pwsm9SngFI0kOYtripT6kGSEmeGC29iGGyqruWnvC4WAOSy-PXJwxepr4D-Z4TUNDGGdZTmkwqo9kXIfKJd4UofgQXVKUvgg2UAISzh_piri-s2odRL2dg2fzeaaCuHN4kVTPqBjrfp8PT6y8a6hpb5TUclsip3yhidl-ONuk2Eu_5d-wUunX5LDuLoJNKD6-R2o0KHrREb_ilxdBxj1zZjjHsPrKHcX5j3nPpztkBJanvycvpXmRk2oiKnRqM8uV6uaBqmmj3eh7HUhcn00oXLLb7Ws9E3QqQ3wtXdUkJeinc6C_ACKb_LouuZ-j_5xR-ddZk0WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=KDd91t62W-yw8Pwsm9SngFI0kOYtripT6kGSEmeGC29iGGyqruWnvC4WAOSy-PXJwxepr4D-Z4TUNDGGdZTmkwqo9kXIfKJd4UofgQXVKUvgg2UAISzh_piri-s2odRL2dg2fzeaaCuHN4kVTPqBjrfp8PT6y8a6hpb5TUclsip3yhidl-ONuk2Eu_5d-wUunX5LDuLoJNKD6-R2o0KHrREb_ilxdBxj1zZjjHsPrKHcX5j3nPpztkBJanvycvpXmRk2oiKnRqM8uV6uaBqmmj3eh7HUhcn00oXLLb7Ws9E3QqQ3wtXdUkJeinc6C_ACKb_LouuZ-j_5xR-ddZk0WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk4He2UCQSvPeAhu1Gfmz1kuvE-snI7DDohvoe1TfO_vdmrTmYwBKB0n2kS25MXGBVFMx4IglReHNY70Z3GBoCmEb0UCjDSq0EI9SJfjpTsh-JRPbht1qLmPeEae3VPOZG2rahQZhmoN5PAGUq25kgOgoGoU3FGGxqrG1mftPyPwH-7xgssmnMtAtB1dgiaLQeuR0K74xBGbPjhR__xYDDADmQpd3f-MyWIQoTdgXDqg4mMlLJRA-Qdkm1Z0qwi_KSDossBJe3MIHIxkhMUM8a4Xs5_qFrjaiS6FKn__pQWnzu2hgcgZ8HoCEc3Ip4KH5bVjrP-2RhT_OJUMeVni7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rugXfUZBASIuGv1VyXGsSrqVcOdqxfeU6VZN9PqMwGtWinUqzDdtDo3jtKMYHn0tGeeckCIDmmcZ8lpZNfWYgPiCC9g7RsKVoybfyc-WmbIV0n8JQwKMBNo2qo46Oh4fVQpetZ-ukwKeIUyrSyo-qC5TlqOWn9_3uH76P8H_Rty4Yt0MsBftzhxT4fwo7h80TLNhH1ooBM1ChRmgeSdPUKRxxlEQgR-ES3PTG7BbCwBhb-Is5LIpb_j9joxnz6_zPmUdzGsTc8FURzYQaQ1cfwCFyUtdmPwUbruHy5GsuHXWnYi3ZD82Dg4kJ87SCyXqBKMX8nF7GaMkqK-ILEB1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=VutL7OsKpbhKxhRPUgeJ3Yov44lCIPHvRs6Cj3v611--yCu0jN9H7GlXjdSg9M4GS_l4hOwZsT5P06E_ErrniSesbSac9vqrJpz8WeNTMk-vyclMqA9VFJh99bI-PLVn5XZem03587uLcsQLOCJEEqj66xLhCaQqClk37mCjPtXmwxCmlWrGf04GNAEroVE5HgwokRRdCZ3BYvpZPq60W9mMmNqC9vDU67LegvDzvTsSoQ0oy605zql5wZ29e84pC9uzQWqULpr-KZVwdLPINrM3FjiXD3wrp-9-mBUfHvqJq2JDTPaRHB_xZspdj-NQg6VoJSeh3xzM9XwqUzTSXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=VutL7OsKpbhKxhRPUgeJ3Yov44lCIPHvRs6Cj3v611--yCu0jN9H7GlXjdSg9M4GS_l4hOwZsT5P06E_ErrniSesbSac9vqrJpz8WeNTMk-vyclMqA9VFJh99bI-PLVn5XZem03587uLcsQLOCJEEqj66xLhCaQqClk37mCjPtXmwxCmlWrGf04GNAEroVE5HgwokRRdCZ3BYvpZPq60W9mMmNqC9vDU67LegvDzvTsSoQ0oy605zql5wZ29e84pC9uzQWqULpr-KZVwdLPINrM3FjiXD3wrp-9-mBUfHvqJq2JDTPaRHB_xZspdj-NQg6VoJSeh3xzM9XwqUzTSXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JsRf1qZkA0wcOJkg5Te695y2qNNBxJpjRrSi-7rioJ_pM5iDR-2Sp0W7FpSzXDie95QbHh3iguuxVuBxKxlG6h-6iecBs0O9uvWuXamK-G9zCjBne-cdYWiLKDuH7Ug1OOx-NkcRsbbitgKs9VM_W3pYpeWNBaFpxAlrtkCwON6KRIXD2lGjAHnqVhC02he_VLAYM4kMrTWYgsqrN0Vz90H9AGpcNVx-xVCjuqPVmv5--xIF_hgZiSBDbKEsJYhElywc5_IHZcXq82CJAojOWPHtEUjGqDCHQyzKheeoqKlaoHX_1-q4IkkLR7P2iFotaVTQ9CXd4cv9jWzvv5eRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=cGF---2cHsXHTZlbLUfefKJmZFrJpWA-wCJtIKWFr371cU5FIc5RivbPW2-n7Q-nJYlti1DkMvq5D5KoHG356wU_CfE6KJpRuWnQSvhNIfKRLyR4OK3aeIH0_8hqXLZ70vjmJUvdAfmRS8t0bG-UxPI3Or6VfOMEkD0kNAwTe7T5ifSxEn9o04ujz902Z0pziB_esrBmDdPmCkshLKvYlSfJ4sIcOHFpo7qhOS_F2uDwCJpg9CPCj-geNmgieuLMcMGFUb-FImmMZS-mQ2_uoToXdqpvip6vjPakTSwUdmpLAhm6CzI-v93Nv1O0l_HCj-DXcnc3Yy_nqx-yELHx2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=cGF---2cHsXHTZlbLUfefKJmZFrJpWA-wCJtIKWFr371cU5FIc5RivbPW2-n7Q-nJYlti1DkMvq5D5KoHG356wU_CfE6KJpRuWnQSvhNIfKRLyR4OK3aeIH0_8hqXLZ70vjmJUvdAfmRS8t0bG-UxPI3Or6VfOMEkD0kNAwTe7T5ifSxEn9o04ujz902Z0pziB_esrBmDdPmCkshLKvYlSfJ4sIcOHFpo7qhOS_F2uDwCJpg9CPCj-geNmgieuLMcMGFUb-FImmMZS-mQ2_uoToXdqpvip6vjPakTSwUdmpLAhm6CzI-v93Nv1O0l_HCj-DXcnc3Yy_nqx-yELHx2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaULi-_t1_abyJHefz_kVRigMCEUwtePvHu_41tePksdR3XJeKxtsF1NuD6HCFSO6iGgqyBC12b9tlaBLgRoAToYjwFQfcp8SUiOgr30ZQhdfaJQmS950b0pepx_I3JjZh55TKuiyMc0kdE0dTBf5eqzAy91t2zwaTWc-Eo9nyrWKBmKV9h7vpWPw1xOxFtiN_aiHVp8saSjeSf2hUefozjaOQ-9npT62NWnWGt9ncW9uLqsN6Y_3NGj8xB_2fumfR4isCnpF1zAYxkRpJnzoLglwnsZK1l8YXbHlgfady3p1n4uE0JTbd13b_kUJDVjxWZO7Vkzp4mn2Kr3_T9P6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=u5igqMNAgeGouaAYxrMpmNC7GF9NxJ2waVTH2oOeTcxAydoR3oTIV3tH3-aifNJwo8DgaFxS9F6YPMixEIpiKWp-orWzzlpYuMP80tDId7bQV1bX-VW1seQ67bWq5QuA8K5qYRMwlWPQQc5ec-YBtCe5e0yoXSYcAyqxCJx8A5bf0hZ84lScyZBhV0Fvy3ZkzwDvaCrhihA3y096FoNyeQ4CdmaloTr78NAMREhTKUkCzR2yu5zaxGYYQacFDLaZU03iyOpKOCUw8zisXc212JhBM6yXyvYQBRMLNBTWwACSn520PDL5_lBsYMAD74cG3LSpVP0j5hzFs1MWCQR_wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=u5igqMNAgeGouaAYxrMpmNC7GF9NxJ2waVTH2oOeTcxAydoR3oTIV3tH3-aifNJwo8DgaFxS9F6YPMixEIpiKWp-orWzzlpYuMP80tDId7bQV1bX-VW1seQ67bWq5QuA8K5qYRMwlWPQQc5ec-YBtCe5e0yoXSYcAyqxCJx8A5bf0hZ84lScyZBhV0Fvy3ZkzwDvaCrhihA3y096FoNyeQ4CdmaloTr78NAMREhTKUkCzR2yu5zaxGYYQacFDLaZU03iyOpKOCUw8zisXc212JhBM6yXyvYQBRMLNBTWwACSn520PDL5_lBsYMAD74cG3LSpVP0j5hzFs1MWCQR_wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=QRFtJgnNWemHZqU5H9QJx0EZUshJ0irIZWUJ0MK-LfE0QM7eJYun1kQYLOa3K_NZUPaW1IT9fDfTDCJe1NhY-mvyEo1EnITV8f6W7Igqnkbamd9usfrllceHF5eByXV0MTnNzjk5AZJ7l8bYB-p5U53mpomIdGR48YTBbTUXt_EVYMBwitUKnFcbxE5jQEkTpKODNv45NJXiVpJnFhKvekCUQNvs49mSO6lhjmDNtYtPsTd5Q7sE66Z3xbseg5wqG_VoJ_QJ0q5tZrCwUfrIV-K-X4hXiLHR23IHhU8KNUR8CX8iRIhfcwXomuGQEP0Uben0yLLN6M5TMLWkGByAxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=QRFtJgnNWemHZqU5H9QJx0EZUshJ0irIZWUJ0MK-LfE0QM7eJYun1kQYLOa3K_NZUPaW1IT9fDfTDCJe1NhY-mvyEo1EnITV8f6W7Igqnkbamd9usfrllceHF5eByXV0MTnNzjk5AZJ7l8bYB-p5U53mpomIdGR48YTBbTUXt_EVYMBwitUKnFcbxE5jQEkTpKODNv45NJXiVpJnFhKvekCUQNvs49mSO6lhjmDNtYtPsTd5Q7sE66Z3xbseg5wqG_VoJ_QJ0q5tZrCwUfrIV-K-X4hXiLHR23IHhU8KNUR8CX8iRIhfcwXomuGQEP0Uben0yLLN6M5TMLWkGByAxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghRwxSpewPg1K2s-OCIpFFZQWizWpAMPXBX1GfBA4l_JZsEz3lmD0MWnHj8nbzJqdNTrY47rrNhnWcY3uEhbxCXTP-ZXuZcnvN9wSJk4Bjj_VrVTMlQ-pmHjvgPClMfXc7_EKNiR3VS-sOAh4ksKHVO6pYXHNr0k8NnBywBlRf9JDc517vwp4rWdf6rJ7vfKP5ci2O_sFetrZGtmc0CHQ_BeKe0gduSbp0AtFkwYS-ASnqKWtHlXrq0Xha5XCgR0_2uxyL1jkEedjHK7TjOzi0EuYCj01qE_Uk0NFWwBOMyxCYwenTl7FR1WwVC8LdWwOhi2Q5iuNBaDLgU1Ob7DpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jk4mgjvY3JWpm3I4kxAvYKYYP3Sdif7sq4umDqbRKh2VBy6tcUw9MgzLZQR6FplwnDY-K_spLbvxZYBw-WsMdgJuTTrMJ0x9OQwts2M1qJllxuLowExOksvVqSQcR7EnYxOsgJoVeogXqga_78I7PHdKtRDOax2zXO0NmHf1nbDxxUaNUj94XW14mjrQFFsXiKp3tOMe8NRC_wsG_nFCwetUYhUXU71SxHLSSmNIjnm18ixyMh1uwDbi8G3mjAg4BBGs1niE335hEToP8-K65_DXwSovqm1DTuNAwfUtKtaI6HGU4eUcUG7UTRFUxZV8j-29dSumdiVAQ-aBMxxGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sU4VBeGeNRfhXK1onl8fUrB774UZCeg44wOi860EXtWbJ_HSGBBH1krv5ijSPDqivovJ-BJ9A1f04GR5aKKHlniX8kmwuqwCe9Da_yXBA5yum0gMCqByiu7UJHiAqbEajLttzfEslNWqSlwWGibw0ImGVeaJZE7IcPc6eT6UufRI2SgVdplcIyTzwVJP-XBlZQyZkECvosA02o02bGnWWcNt6A9qZxaALLa9Ysq4En83j9TltXbsjucDZVGEqpjt5IPPNZ8nyPy8HM-GD4HQ12B45ejBySqa-nC7ALrLHzIOyxBFTVj2rJK62h-nitmb_dB71uKndt3l8Cuw1O9qSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Tb6cKjJEU4M8gmvi6pSpFHjTAAhs21ILSCURVeH6DJ0w1EF2nXkhEQ-967aXtVev3T4Ni7RZ70phQzXrvWD0O_mmm51DtcvUpHngpgpUHLT2hl_JK7RJH_Fy-QGNQMb9EZfYIk6WHZbmYlxlUb56NFJ-BM5GxqvidnviXmW7ohs7thPb0cPIhvUxwBmj12Qa2Qg6huseaRP-OWgqbkxdaQK6QQ8ApkjdArhPlwBMDLNuIR69_CmDORJXPnvS_bW7Hi2dFmTs3uZVjAVKY2FPoTfuUlLzyBzQGV0qelRXHahM9meM9LpYR6A__3w5ctx3_GadLgtcmdc6bM2rYvNMgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=Tb6cKjJEU4M8gmvi6pSpFHjTAAhs21ILSCURVeH6DJ0w1EF2nXkhEQ-967aXtVev3T4Ni7RZ70phQzXrvWD0O_mmm51DtcvUpHngpgpUHLT2hl_JK7RJH_Fy-QGNQMb9EZfYIk6WHZbmYlxlUb56NFJ-BM5GxqvidnviXmW7ohs7thPb0cPIhvUxwBmj12Qa2Qg6huseaRP-OWgqbkxdaQK6QQ8ApkjdArhPlwBMDLNuIR69_CmDORJXPnvS_bW7Hi2dFmTs3uZVjAVKY2FPoTfuUlLzyBzQGV0qelRXHahM9meM9LpYR6A__3w5ctx3_GadLgtcmdc6bM2rYvNMgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=BUXWNf9VjAgbgMhYoHkfsTk-HyT96ZS8vCwZ1Ni_UddDsWaHJzFqgQoyau3nYG7F5jRXW5CvuJ0EAnWvfD93kFvX-s4eBRrZOgEXkTHdoMhzx4GXskuC29ZXXdw7jOqgCK_XcPhRnpZQfje6UIERIRcBK0typLwWiVEFW0HKOUyqQnHEJsFMMYJV2gK5mKbvrEPK-xrOoe04X1Ndm-NJRsktG6P7VocyY4jnHIqWEcJgQBbE7tu6D9MtuDlfFfQuTCUwRHLDGbLp-LSQUekZqxqQRCtGPmZhfRFQi6s9RSBVB9cysY0HRUYK3vGbK2Q09vl0yMwm77hv4yaoCwYPqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=BUXWNf9VjAgbgMhYoHkfsTk-HyT96ZS8vCwZ1Ni_UddDsWaHJzFqgQoyau3nYG7F5jRXW5CvuJ0EAnWvfD93kFvX-s4eBRrZOgEXkTHdoMhzx4GXskuC29ZXXdw7jOqgCK_XcPhRnpZQfje6UIERIRcBK0typLwWiVEFW0HKOUyqQnHEJsFMMYJV2gK5mKbvrEPK-xrOoe04X1Ndm-NJRsktG6P7VocyY4jnHIqWEcJgQBbE7tu6D9MtuDlfFfQuTCUwRHLDGbLp-LSQUekZqxqQRCtGPmZhfRFQi6s9RSBVB9cysY0HRUYK3vGbK2Q09vl0yMwm77hv4yaoCwYPqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMyCH0sOd-l9Birj0uJ-5EtBCElneH3SFbNohVORzIQz9MS_AP04C1dfcmwp03xjLBEmFsUJSP9Rn-4lwDIGRFV2si925KTcBlDhajwSN13G6lquBgcojOIlB5WyynnRn_CVHFNF9DDo6ThnT1yuMmRmpZW8YH_d1x_IXXFa0s94FZ9GKpJQDbmtSIG1ATK3dhyny0u2ae3O4IKTofqn0TJArcBFWmOQC8Ti1TAHDZiF30lZE6FOmakWu7vieuvMYlxKi29s3hAmgHs7imNhdFRF1A7ZtUrE42khSlpxUWxlKOeSXZmaHN7iLF1BDXTNTy_WTtdgPdHMdckceOr1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=KxpasriNuEUrPgSNU9DWXs0uth3UZYmpEnail0bwm6Bi2c7etHSvlqg5KGw20UjoyPdwxWFWk9j8oN0tseESsh9gF6CLxwrSVsuj7fdP8bn6U8fjuF6YsGt7doSPNPPzb1HEqItW20UQ5tL32_dW1LpPQkpsosfyyQI_6Cxh23-g3rdhenRLHOLmthP2w-lznUNrFSJvzStc7LMRzxQFX7iTfpnfu60AfvA8EcKO4jVJX5SqZ9aXeicIX3qtp-JMXpvClH8JVGWlzdOgGJhcLOYh4E4_Sw-2SRBTkwfBIAbUauEgpA8VjXzciSgQjOr8vqbHyag_nntFdS3l8FHr3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=KxpasriNuEUrPgSNU9DWXs0uth3UZYmpEnail0bwm6Bi2c7etHSvlqg5KGw20UjoyPdwxWFWk9j8oN0tseESsh9gF6CLxwrSVsuj7fdP8bn6U8fjuF6YsGt7doSPNPPzb1HEqItW20UQ5tL32_dW1LpPQkpsosfyyQI_6Cxh23-g3rdhenRLHOLmthP2w-lznUNrFSJvzStc7LMRzxQFX7iTfpnfu60AfvA8EcKO4jVJX5SqZ9aXeicIX3qtp-JMXpvClH8JVGWlzdOgGJhcLOYh4E4_Sw-2SRBTkwfBIAbUauEgpA8VjXzciSgQjOr8vqbHyag_nntFdS3l8FHr3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKtBaM3LldeT9v88uQNM14JrGW9T3PM3baRqAx5ILn_qcgTedejDmDBieuksLJDGLtcKQtWnaKk5JU16jq5A4Rqn3PQ8TorFx3mmGjtJBpqF7jUriz8GIHw3RPpm8MZcY8sQ9CKnOqbSlsAuWBHCH8jkKOxhpPotmkCtxevNilDfBG_Xab_fZxu2KSwHobU4rjKVUHqPESev85teOqGlPWIUveoBKP_6SBWPNxebNRCbT1MLqUbTxQRvUwcspuG00lFNR5XzN_3xtZvdOO_YszglDThaCykG003zm8YDSmyn6A60dO-P6zAMt1FXaY_V25amHnLIwG-sl04LNumuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=of6zy-yxAI20vrWZB6CwW-kK6DlPFPOEYWniOfvH7JCfCdHJhNZwBG1DSSkWGwQLe9FYBR71x8PyCPWNPAAo5m6SJL2YgQ0Zh6gIvqhUKEPxPMiqe9XLit4X_UZWUDrCj9MQN3OkDfv5EAMknHoMxtb4-9ZvOcKzrFXEcFdIqmqrAKA2jj0slwzGDpeuWoPilTmWVQbyR3PMN7IOf4dOEnM2omuuy-Mgakq-2zymjbWOngGl0lCrnvDJL9jWXDhfYVJ7A3wpJk7rckFOVO-Emgiu_FS-Dm3874Hm8m7W4-3Ajjix-BXexxVv-N8nJW9CwnnydCxR8kzb0B6zzuxWAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=of6zy-yxAI20vrWZB6CwW-kK6DlPFPOEYWniOfvH7JCfCdHJhNZwBG1DSSkWGwQLe9FYBR71x8PyCPWNPAAo5m6SJL2YgQ0Zh6gIvqhUKEPxPMiqe9XLit4X_UZWUDrCj9MQN3OkDfv5EAMknHoMxtb4-9ZvOcKzrFXEcFdIqmqrAKA2jj0slwzGDpeuWoPilTmWVQbyR3PMN7IOf4dOEnM2omuuy-Mgakq-2zymjbWOngGl0lCrnvDJL9jWXDhfYVJ7A3wpJk7rckFOVO-Emgiu_FS-Dm3874Hm8m7W4-3Ajjix-BXexxVv-N8nJW9CwnnydCxR8kzb0B6zzuxWAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-mB3ny6qSninpzsBRz_LKHWqHOpkzcU45LJ9lrQ-YpwZ2qBpBfkitKtYYL-vXJWPfk-KCZsq-KovZrJE5CY813y8xlPh_1b1BKmBzE1riCsNocX5EmyecIMqHeGm6S5DfN16HAi_Fr13D8P-2voA2gwRLlvwgnaPvhzIWPuo3hVduRRFbxUKwKKuaKDsLDPvHqYN9WpsmEF4CqSzcANjHB1_n0PfA5PQcS2-9pvrEboQa5OFpYZ_D03OmRLJDUkJBq7dD6TZZwPH04j-dgPa8dcmOEIy6NIn-c_m4Av6r46WB7lqOpNZKIBcVwsU7MyUIyqLDTWXb1KomWpmEcaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=kIHDQ4tCiyvDWdirArw5XgQGC_twfsb4AG3MZEzCdjLjoNUmVeEu01NjDnzqsrggFhQzn4FRWjmmtGWVlUAt3Oh6rNi3iGXP2JzsvbaCvCwi9vvwpjcshh9XhmqiuB-lff75A_sU08XHWmuMHr_Yz9c85aqqUdPBlbc3RLodfsQoBOEVGCO5zH1EFoJ6DdIH1xDj5OQ2mgBc7UoXurHyB0IoZL_WwwlRCatxwyNokQXPobmjI4Fr9g-U19hPBKx1xx18rjHQ2E_ZywURM3rBcGs5Q1PfJo-gGERWCCc1fgMcye6DJNEyzzZsKbi8mq_NerSexlAI4ZvhFyPnymD4cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=kIHDQ4tCiyvDWdirArw5XgQGC_twfsb4AG3MZEzCdjLjoNUmVeEu01NjDnzqsrggFhQzn4FRWjmmtGWVlUAt3Oh6rNi3iGXP2JzsvbaCvCwi9vvwpjcshh9XhmqiuB-lff75A_sU08XHWmuMHr_Yz9c85aqqUdPBlbc3RLodfsQoBOEVGCO5zH1EFoJ6DdIH1xDj5OQ2mgBc7UoXurHyB0IoZL_WwwlRCatxwyNokQXPobmjI4Fr9g-U19hPBKx1xx18rjHQ2E_ZywURM3rBcGs5Q1PfJo-gGERWCCc1fgMcye6DJNEyzzZsKbi8mq_NerSexlAI4ZvhFyPnymD4cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=r-2hMS6XrgpAXkMu9AfLT7S1rcmhNx1vhC6lZrRANu8_4UQyWU0X8qmeuOVWISHsBjnyY_XGsKxgaiwhXSAazdpcuxt2xy_5B1AQz_aPSYjfw1gbYGAHv__esXcQco1LxzAdgfkuhMBKF-n_bwH8dQ-t6lKgOQ4zT-uyOEEzsvmUA1ZtIJPKV5pGGsPgdLM1EXulWtsEOK04rks3vph_bu3GGZ6lPcB0ccvr9xUneOUJL0o4DMWzf520z08xKR23ByiplPbPIo1rPAnKTUr7F79nbwXABOQzOTqvzjwa_YG6V8w3NQ4xDXxKkblsvsG_Kz4Q2erJj8l3ZeeysMJHfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=r-2hMS6XrgpAXkMu9AfLT7S1rcmhNx1vhC6lZrRANu8_4UQyWU0X8qmeuOVWISHsBjnyY_XGsKxgaiwhXSAazdpcuxt2xy_5B1AQz_aPSYjfw1gbYGAHv__esXcQco1LxzAdgfkuhMBKF-n_bwH8dQ-t6lKgOQ4zT-uyOEEzsvmUA1ZtIJPKV5pGGsPgdLM1EXulWtsEOK04rks3vph_bu3GGZ6lPcB0ccvr9xUneOUJL0o4DMWzf520z08xKR23ByiplPbPIo1rPAnKTUr7F79nbwXABOQzOTqvzjwa_YG6V8w3NQ4xDXxKkblsvsG_Kz4Q2erJj8l3ZeeysMJHfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=QzsVWxIdCWR2DW0oB2hS_HOptSnhcuuo6FPYJdxU8l53uAdXDcCHYEpPpbWI6f_kBO1T6xm0qAT7DtIthmy1zJCxpJi7onrX9GZjXuRVpPw3viwxTimZYWEteZf3KJzUY5IYT1iHW8XrKzsKzsJsm-QuuB59UTVnul1lbgdyQM4FBOJuxwcub82jv8GSkaC6mMBDnouj_1OQssqbbB8rb4uL3xQJ9RrjMdkul8Cq4eoLiClTgZZjmtmK3C9yhMt5NfvEhzOIVMeSZX9whoNSv-N-yBO2q_O8IeId6FHd6NEyDtq-LmDjTmDJ5zIiY9FBkrXMcIt5LAnJM2PqEUlAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=QzsVWxIdCWR2DW0oB2hS_HOptSnhcuuo6FPYJdxU8l53uAdXDcCHYEpPpbWI6f_kBO1T6xm0qAT7DtIthmy1zJCxpJi7onrX9GZjXuRVpPw3viwxTimZYWEteZf3KJzUY5IYT1iHW8XrKzsKzsJsm-QuuB59UTVnul1lbgdyQM4FBOJuxwcub82jv8GSkaC6mMBDnouj_1OQssqbbB8rb4uL3xQJ9RrjMdkul8Cq4eoLiClTgZZjmtmK3C9yhMt5NfvEhzOIVMeSZX9whoNSv-N-yBO2q_O8IeId6FHd6NEyDtq-LmDjTmDJ5zIiY9FBkrXMcIt5LAnJM2PqEUlAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGVbznCAZ-2JrARnvZwCB7vzr1ASs0a9FEfSwFFG69iqzOpnyWlb0ZlOep80xovusloPm56ozbWLpr8omNPtNT2ytNPvqcTBiNK2wlfgMWhSVIN882nmcyo6N9vIN0xI0_rdM-l9xzdzzjOpg-S2YrAcVINkoAJ2uq84ii3nspdwiA6KwcR2WVV-U-VEj-B0Wd0WsWr-ZFlo9D_QHBZMb4niYfYd-ClJzRiC3VbLZF1ajeFjBy5_XoeHrXVcDgVKOtSFtwCHUvP-KHTFnds4njDl_ENqezi8vrIJU4j51M0dnHOsdPVQMaVeBr2X2E2Bgi8njviunZnj-19-ksmwEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIpTIiFVnShAUG36b4Z1UqZ2iZ86ZNYM784A-rAzyRg_HFb0cQGT8Js3WJgDtLeP9ov2SDIZ69fIONgkJwppRDyPSjxZdQVy5SijA6FTA3kidpj0bydVuPDlKjQKINtEa74j83bvBH8_YinVgc1FcyECaN9Kds88ac8VuVgfoK7bZHgW9YZyBf4d00b1F_tfOHNT3FaFd5qNVXvTfcB5nxj4VuYlNM4vw6WqpJSfquDLdCyhzn3Tw5k6FNygmxjoVpf_UNsFd0Nh3ZNgDgdfm9WW66Qw3-3wmPiN3FNKQvhSZ_ZSXJ19e1aa_LzUgO5weXj9aOX56ZI7sOfBz1P_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn-AVtAvnfH9P-tvinmE3iji8DX5ImaOlU5Ch13R1AEzqAa0rug55eLkWgtqGPDm6wmnY7j26ZM9bXTcpWmXUX0Nr9ch6pnxLdWqX4q4VD_ScVJUlc57Cb7avTvijlK5ATq34Pl9OgEjyLpKDmY9aB-sflHw0HGvCEKxhw9pvJGvjZ6GCvk-C9flLMkZyAwVPkqY7PTSOOEKDMOUwWXPDGnGHTvdI0Pxh__cBZhp3sziV-JNerVedGv-wyvIProicJCC-O6EmR9WuOkbnBtALgqoGB8g4IYLcSAUA4Qh5uhI_z_hW1Npmb_yDYCX24as7LXNY1ufoQOLjDsUjqSuyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=EsX-YmMJGJMOsh8pTU9kYjdLmdA3d04D1kHEtVPr7czyXu84ql_laZ3T0iLWxWvMwaRsd_cQk8zFZUoP5YHgneYa8gFvvUqB7otk_5jAMW-toRdAPGc-EX8VLLl1yPjmA8yRuBtGnFdFXzSCfZEHE0OzwpOk_2g43UFxjx72E1_39vJd6tHgkPfuciDTQb8gnlA9ZeaFR-zgu5ZQTOXe07Iqn3PyCkNiqI3VLWUqe0zWILvsS8rrM746XIOjqeFXcqvOd3cDBkD429D04wxFiaiiDocvuUjrv-LeTzpwJkZM0c5hHvlENhen4ZejF_yEaIDE3MM_V5GSr-GA_4cYJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=EsX-YmMJGJMOsh8pTU9kYjdLmdA3d04D1kHEtVPr7czyXu84ql_laZ3T0iLWxWvMwaRsd_cQk8zFZUoP5YHgneYa8gFvvUqB7otk_5jAMW-toRdAPGc-EX8VLLl1yPjmA8yRuBtGnFdFXzSCfZEHE0OzwpOk_2g43UFxjx72E1_39vJd6tHgkPfuciDTQb8gnlA9ZeaFR-zgu5ZQTOXe07Iqn3PyCkNiqI3VLWUqe0zWILvsS8rrM746XIOjqeFXcqvOd3cDBkD429D04wxFiaiiDocvuUjrv-LeTzpwJkZM0c5hHvlENhen4ZejF_yEaIDE3MM_V5GSr-GA_4cYJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MWo3W7A5nATcCvd2wYxWnvq4v03M0vPxQv7z-AZaojLnksVJxBsubC_ff87uTB6jPQTaT7ZI6texh_DjdJXwpeFBvQJcbuSN6wJ4Dgea4T5pESt0FZqMGjmtVEm-FyjJmql93jJqN0M3K1MqUsXhPx4pt-zijeySzeQCNm5JzZDu76EF8Vr8syfPUqzAbQogKnf-eApj6SBRahrcASLV-qPW7QFLOPnRRRhzUjIlTpVkKjg6Ap5QoFut9C3sfaZdXI5fwYpteyZMM7qGMhXL0jt-pKCV9HyeBAC2svYeTjkEHGf45Ag4c48ogzU14NsKG7-g5UaUS7zL50LhL8lnbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mphUB3lKqBVt5hbzHM3In6ernlzaUVuCtZKU-bIAa7EZCYoLEnJmyOgkaqg1N0nqXfZh9LV3Kp4NF1Vhhb-tD-btT2XWpuPXCUZdqH9hHey4D47fz45U9yrN9DGNhgmA12ZMJLSyeQ4lr3U0Dvf4dw8ZlELwnBiuWr485QHTsW2wuC_46--TB3mLE-KyCK0Moh1PWhVrFLJL0pUTImjOaSgLXMVmfKAIwq7yJauSAVkh6U5qQewLkfR-E78d1XLyZWuM5PYDYjDXMDE97guqGrujJaJto7_MxiEwcEX6waAFT_VsH3wgmP9utFcKzeJG3L4vCdlJ-J-Eb3Zq0wBWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mphUB3lKqBVt5hbzHM3In6ernlzaUVuCtZKU-bIAa7EZCYoLEnJmyOgkaqg1N0nqXfZh9LV3Kp4NF1Vhhb-tD-btT2XWpuPXCUZdqH9hHey4D47fz45U9yrN9DGNhgmA12ZMJLSyeQ4lr3U0Dvf4dw8ZlELwnBiuWr485QHTsW2wuC_46--TB3mLE-KyCK0Moh1PWhVrFLJL0pUTImjOaSgLXMVmfKAIwq7yJauSAVkh6U5qQewLkfR-E78d1XLyZWuM5PYDYjDXMDE97guqGrujJaJto7_MxiEwcEX6waAFT_VsH3wgmP9utFcKzeJG3L4vCdlJ-J-Eb3Zq0wBWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1DqIyEhbjF0gpUCSbPYa8gw6d4N8XZMlqSEDE4mPWap6VsiiAUcqJqS_s2_s6hv0Ilg13KAVFvevPvPkbP-K5ftxyPn9lbkxZxW3relml6QwDD_hhz3jikCyOzA7i3-qIhmvlRX38J_z79SZJGcdKqMvaCox0WBV_rs-zHmrtxdclM684z4Wy7Bnk4xXPUy-u1DYjKQIM61dcLQ-Nt9IDXDdP_wO37zrek1x3_cfiyXks9NtbU7kp43b6EmYMjLIUnJhN2uGwqnQpxy635mtOaecKNPkX1hq0FalSy74s5mMNMJtdoF0NOt7YrvNyOHoohZifJ7hmg2KVypSOgjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=CmGg9DPyIlr_yY5rvahqj3K6Yxa_1zF9XtR2OjrCcYPwBQryV_VZ90RIEpdahDxE0zbtrpcPVY-BVW7xpyYs1QdSaHsihws34SMDuuSynyjObUjFDhJLph_EiVvIMAfrBQCFfn9CReBZfVvt7HSkMeX3osBI7LbqqvmKeEV-elpQxiMa_MNY48o6X8WzSXWrvhUZKk_OOnsGQfSm2DDsFo59iLC34O6TpnorKxbrZgBWztn8HpU_m9IsSqGO3EqJxt8dHAsX7kzVczlP3z-Bftc45MtvdvCLajluB1guFzSugDDiggGCXbSUnVQSABNGpjAfdDNeDTgLKrc1w79kuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=CmGg9DPyIlr_yY5rvahqj3K6Yxa_1zF9XtR2OjrCcYPwBQryV_VZ90RIEpdahDxE0zbtrpcPVY-BVW7xpyYs1QdSaHsihws34SMDuuSynyjObUjFDhJLph_EiVvIMAfrBQCFfn9CReBZfVvt7HSkMeX3osBI7LbqqvmKeEV-elpQxiMa_MNY48o6X8WzSXWrvhUZKk_OOnsGQfSm2DDsFo59iLC34O6TpnorKxbrZgBWztn8HpU_m9IsSqGO3EqJxt8dHAsX7kzVczlP3z-Bftc45MtvdvCLajluB1guFzSugDDiggGCXbSUnVQSABNGpjAfdDNeDTgLKrc1w79kuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g98NfopnrHlgJWrvJPXLIlZJq2_wvQePe0NB9oA3P643xuDdKxc2kj8ZNrTPPfOrgvUWioElclEVoNcrhBKzvDkqLz7QWcPdeCrj52f8TNMlHou4Org1qojQFzRPNOKHIVSvZaVFfaSkEyAelvMyDAq9O2IRTf6SJSFQ-Yp-Iq2iSlxSMD6lUpIgcce-WOg6QGHwxG-Q1Is2X3aVpAjMv63UicWTuQBw6fvPyhxBLwDSJixBT9N8RMmN4eYsfl_0wpzg_bMnMfKo8D50ZGjiywt3DlCo0Lo3xsYI8oosWHaj-HRG2IjTvyLhRHU91Y12AClecUU0lkifGNk_yrFlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzujuAXx6FtNhyKDMjhMXC_RcVoYo86rOg4lWcgQfQL2ywAKWmoBDib90PmChMZbXsVKyPfx_pH29IbqqLc7Yl_GEvkmehXrOKd_gsaozyJOcghEBRjpMSbbkSZkV4ECEBMhBNuzS-VaOYhmy2IfuwS2m-5PMMeFL6D0u-ZxF3kY9PM2xX_oeYLcOiDIZVwt86V_TC3BFSD-ktNWjdyCRgDEV7oM3EuwXfKrqSsfIJtnTnrgK5E4fFd5XmkX0E80IqrdR6q-5vb_uciUdDrUQxQsmfo2AAPG_TpXvQt7X-9Ys0lYcRQB6bRPYOXbs_Dc0_5b19BwRtbrloJR6Rkp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C21aydqSMR6oPSN5jd068jhcVi0e11tJ2PB2eorZEbUkFunoMGqWf5qDxh7CNIx_ojESBXlEdwvdwlbRU_h_uuOdBeFH2ZlxyPeJN9k7P-u4CrrBM4bzYTe-1xdkKMVhcDWNJInQWn2EDYkQP5PTv-_iO-PuK1cxey_Q5DZEOTWCB6DDdiTs7c6MIRWjFiHQE01JC2amu4hDCZAYWr5BJEzRFFEu9mYidrOCmD4xD1rNI_bCTJ9y5uvVU4nkAqQ35BPGLtmkomAGz6AzLopv6q5PBBdCoIY4bvw6zMWjU87cXyNECP0LZ6qhrEZu7Kgk-c0fTWMpiyzCsNVApt_P5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIrneRqHxrF0_vedcj5haBHxoA5cMYzoKpHmvw54JHltovLxAH3kf8JZmrFLwFMO40YldDgnFjtDQssAYnqv8xEMw26FSxKEbdfG9Zos0Ty9i7-fmzOyiV3314sc_Bcaqn7sEMnra9btjHGdBlfIxUUOW2Ev1vLcJtXvnFKpkKmNZKgG_8hcFdUyYkpaL1V-dIofgILFl3ztxTt5IRwMF60_bNz8rtnbOT4o-TsLjo2VghfpJMCUEowrAJCtsjqn6x8tQqVsmxykjXUki5ibyd4GTR3XbWgdVUzGUV0qFO2T91_Wws7_6-1MKxt6oQ3NdD7GIfsNG_2evxo_tEXcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi3BjdUyWHFdL3hZuPpjGu5HmwCUNvr8twKgjO29-QvGqsQGzIFHP35MjGkG0oZA4aYw3aqwH2cAhNgd1UEyR44cNFYlZRFiay1G2v-BdjtF420BapYhoRVuIVZnqYlVztZR-HveIMvc0WklVbPRI9m4-vs8zrSrKDK7ZL5VwXLwvBvkbVtwckChp-xfL9x2fbqI-97J5kYOED3yK-YLV9O3O-Q4cPU6z8DVod7ynFV1GqkBVAvXKCjl8K5bBUtKLwxG5PJ15aQHlog8uNEeLj3kQeK8iJdA4IdT0-rAdgW-GhMIQuMEkBMUU6wN3Rt1QTiWM0suBxojRPU2U1cShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=EnUri5fPQ-S_bT783Ohpd7NjoofwmjL5gfWJ4YQELML6SshNmNEcBTlkxudtziOYhuK2qbhNX6QpRPJSN8NPPcIu1DaeG81GK1OApz9Nyrbs2x-bx6CpAj8ltCtXDlccqC6Cu_-Fs280bJD_bsTqjHGHPEaAuT4gUxBPE3CcXB8sSL3bJBhfpTBUJpBO4p1ONWIIdFoV_djain3YC3jaLiXN5RT_OE1WnpkCcD5bcysoVwiYpJxIOa3ckR8QAj-6IGKbI_HRG2bDwqh4swmyQpjL0yO98nSAdeixr9WzZnG_OLcc0hUIRgcc9a9tJ7VAxAFUtqYqPrOKM6lITl-ZRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=EnUri5fPQ-S_bT783Ohpd7NjoofwmjL5gfWJ4YQELML6SshNmNEcBTlkxudtziOYhuK2qbhNX6QpRPJSN8NPPcIu1DaeG81GK1OApz9Nyrbs2x-bx6CpAj8ltCtXDlccqC6Cu_-Fs280bJD_bsTqjHGHPEaAuT4gUxBPE3CcXB8sSL3bJBhfpTBUJpBO4p1ONWIIdFoV_djain3YC3jaLiXN5RT_OE1WnpkCcD5bcysoVwiYpJxIOa3ckR8QAj-6IGKbI_HRG2bDwqh4swmyQpjL0yO98nSAdeixr9WzZnG_OLcc0hUIRgcc9a9tJ7VAxAFUtqYqPrOKM6lITl-ZRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=AuLp5N53I5cxa1YRVdbDWkkd1XJq8tNIPo9MM1rCR99W3iH62B77rIojKQ5mDcoZHBpHFTlpolh1ERFiZ9-p_pIPS9p62zQwF9zGUsTZ-4Q_s6TTv3mc_-BMqnjXkkTABvUNXAiqL_lERlke74m-d3KAhy-CbwOYb7VqkmtwtWXT3EQ-2iD29GTraXZ_EV_wl9h2tNFaVJqPnRVbbEpT7fScZCtIOBLJQmquOzcnWC_cRHMdKa6FYOQhklYIx3B2cUXY-aSKCK3u3or7jslEukPBu4YStb89_NQlT-L1si9U35L33tjjcHI9necRYhJUrYy5bxAYEtEfXNZ7cVOYLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=AuLp5N53I5cxa1YRVdbDWkkd1XJq8tNIPo9MM1rCR99W3iH62B77rIojKQ5mDcoZHBpHFTlpolh1ERFiZ9-p_pIPS9p62zQwF9zGUsTZ-4Q_s6TTv3mc_-BMqnjXkkTABvUNXAiqL_lERlke74m-d3KAhy-CbwOYb7VqkmtwtWXT3EQ-2iD29GTraXZ_EV_wl9h2tNFaVJqPnRVbbEpT7fScZCtIOBLJQmquOzcnWC_cRHMdKa6FYOQhklYIx3B2cUXY-aSKCK3u3or7jslEukPBu4YStb89_NQlT-L1si9U35L33tjjcHI9necRYhJUrYy5bxAYEtEfXNZ7cVOYLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=gOhvcBkKRD8LExgu9FQJcxvstSBELksZo1fuzXTZxKJ_lNccjY09yrmrRaLrxHnhAyCHb6GR2LR0oY367HKkFjjESaNGVwJrkd9KPWoG0zouEnhDUxpM1u_ECaAWw6AcnV4nX8fHTn323DJMNsATXe20DxAsi08Kc5bIz0TXHkV01apOOxlE8GIYQ8YtnI8iU5swTowbPtjFpclobkmQt0VKM69iIbjcfOphI5pAafzCxlIlOUrSz9KH0IjxJwp9JyEanNCnsdyhqODEUecyfc2Uv1uSXvXgKkAy3SS5KOQHkubOn0zw_483UK43tlFLcKA8JBMLquDDLsA3w7ZYbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=gOhvcBkKRD8LExgu9FQJcxvstSBELksZo1fuzXTZxKJ_lNccjY09yrmrRaLrxHnhAyCHb6GR2LR0oY367HKkFjjESaNGVwJrkd9KPWoG0zouEnhDUxpM1u_ECaAWw6AcnV4nX8fHTn323DJMNsATXe20DxAsi08Kc5bIz0TXHkV01apOOxlE8GIYQ8YtnI8iU5swTowbPtjFpclobkmQt0VKM69iIbjcfOphI5pAafzCxlIlOUrSz9KH0IjxJwp9JyEanNCnsdyhqODEUecyfc2Uv1uSXvXgKkAy3SS5KOQHkubOn0zw_483UK43tlFLcKA8JBMLquDDLsA3w7ZYbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsqIkvYo_NUgtSjJw3bg0irVDi5h0hTn-jCnJhpcHIjIm8f7IZiQqWAjcY4dVkdtS_tm0FWMiuTlx_XDTgJMe5MJMYkhDjXNb3aUmS6ROsXslmjEAlCPgpVBlvHAFZW8wVIEFbnvVua6y_kCaZBMaA28-LFa_acUV4xdGevKf-OG_gWtV5GNJUbY5MpVsOFnE3IJd9DYWm62c0oBUqHn1D1fS_DO2Blq1_BtGy4NrOXmtOcvOS_k8A6ZpgUmtozAZLkTPeIrJviWVXNbkHKPY3n43Xk-hEKOCFVXxuhJHpn4gjq1wxjZ0F0h98ZlsPisbd50wF88FoEris19RTDGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AgA-bDzGv6DCVXyE67vh801yYLj3gmdTu1EspP8Q9bCc7kSWc4DCrBlEpHc4MmyyOv38nJ4k9_byjxtWd08MspXnKxjJLYN4wWB0rboONZsrDiPLKYRJWamc2jqgDP7CGM7eC7wUfGB0i4lIHBuhLd_aCeGtEuKSiC5nr6SKiqdgOT9ZEx1448CEYDUs2dU_ZA0zqtY5hY5SVpmE17Cxd-uw1S3XYqs-Lk2DNz27K0nghwdhm4geeT-3QYd-b2JAF847vM0gudsBiR-mSB2o2jDYIB6yFcOI9dABr3suBG6N251NI09immvK1Z-mmg0TwYwKkxwv6Iy1Pc-s07q6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNvXLZNKHeWQva2SNwdQQor2ojiNMfgNRjUhaQVqUtpPWw2363kMr1RPhg-tjU2FKTuMiUEQPN5rtEtVpT2iG7wPgnK7-HvE7MqMFZKn67_oZwYJzzMUsdHe_taj-U8Fpb-LmErzGAx1IdoXdCJWvv8td9uyWEahcb3V7NLf3yhOujlfn9M23lQMyaOTcQUdeLQm1aNzi73Us3NXp3ferq7o1u7U_RTQHLyhuQBKJDK3JIG3dJ5Aqjl9KKLzv1xY2EnTGGdnF9b4CN2pz8CkcPqj30p8bjUIsIraauL_LksagX6TixxF_j4SG_9IvR6_a4n4y0elhn_MqEueIRrJog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=rAeg9N0whZJKHd3lv-h0igA3_KOPTBFvX3MurwIq5O0td8r-3X1fa5xLXS7H0QIwXoqw1uAVZmNYila1l1QAyYTKQNe1nJ9MNpQW9m-CYLz-lf52LEva7oVbyP0mfe9ugZNldT7TTNq3yTyLSOKmbLZY90Hc8d4a2AsqhZzJVeLEe_JQyeYaAs7f5e1onkYrCYwvrussspOdlk8w4uhac9ikSeLbmdr2C0WtZZkFM1cDyDHy-LCyxRVd0M9BJCD6Jbj4uLtJJNNzCV4J-V9SoCZdcZscV65qn7eNcLtoe8kIaHDfX74LtBlXhV1F3D51m-pAVS4VsNGWZjllibPjXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=rAeg9N0whZJKHd3lv-h0igA3_KOPTBFvX3MurwIq5O0td8r-3X1fa5xLXS7H0QIwXoqw1uAVZmNYila1l1QAyYTKQNe1nJ9MNpQW9m-CYLz-lf52LEva7oVbyP0mfe9ugZNldT7TTNq3yTyLSOKmbLZY90Hc8d4a2AsqhZzJVeLEe_JQyeYaAs7f5e1onkYrCYwvrussspOdlk8w4uhac9ikSeLbmdr2C0WtZZkFM1cDyDHy-LCyxRVd0M9BJCD6Jbj4uLtJJNNzCV4J-V9SoCZdcZscV65qn7eNcLtoe8kIaHDfX74LtBlXhV1F3D51m-pAVS4VsNGWZjllibPjXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=E12qfFINi28e0uyWo-7To-dUOAsxDBJyheVSD9zdrQ8EPgsua7oi-5cwQdgIdADd-klw2Jy4Vk0c34F6lJ-6ZPWytTkQb02z4LVWHlL-jnqv_OprsP40D6fu1aM0aw6WastpZFOqjrtxlUj8bRGnDvXSFkgUeWsHqcDDsFeBc1hitJv3D52-Z4rSs3a8ZSqzNte0iqM3p3_CkrA_ivlcBMJwX12sNU-YpYI-pMUtrvxRSRacUwL1SEHL9asHkLP6PYwt1AnUKp89Kp649INGJSBVQz50Y5I8yfPNImmhZiE0nj4YcK3l-2eCJQKsPC4XQRdjYyEy9fQ_8ZRKQuF1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=E12qfFINi28e0uyWo-7To-dUOAsxDBJyheVSD9zdrQ8EPgsua7oi-5cwQdgIdADd-klw2Jy4Vk0c34F6lJ-6ZPWytTkQb02z4LVWHlL-jnqv_OprsP40D6fu1aM0aw6WastpZFOqjrtxlUj8bRGnDvXSFkgUeWsHqcDDsFeBc1hitJv3D52-Z4rSs3a8ZSqzNte0iqM3p3_CkrA_ivlcBMJwX12sNU-YpYI-pMUtrvxRSRacUwL1SEHL9asHkLP6PYwt1AnUKp89Kp649INGJSBVQz50Y5I8yfPNImmhZiE0nj4YcK3l-2eCJQKsPC4XQRdjYyEy9fQ_8ZRKQuF1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=ashza1jWdtGf7lvbOCo7oQow_YKs7XWj5uLxy051ZuBFQN2yqT4eqQoDDolaKXakrbKOyHMu-d0wWwHpRDdxz9LbKApI1B8O_6usPArXK55_PEJOvGo8-z9pzwh9QwEdxJW2TKNtd4ltbKDXxiQmszkf51nWB8XS86T7xDK_FVVzZ2Pu8o11frOfUNtoy07Um_d0r1j5b-o0xkMSh_mwYaKSR-DsDewpmRQnqT-pCEnSWqW5-9aUJQ3d1CHwHNsxGYd1Mrs4OcBYdbnNc1DUKdP7w4YAdErjIZofaUWUuB7L6kdagUlbAKNyQH_ecS-79iNvSPnZkSHWn6TLIgGuTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=ashza1jWdtGf7lvbOCo7oQow_YKs7XWj5uLxy051ZuBFQN2yqT4eqQoDDolaKXakrbKOyHMu-d0wWwHpRDdxz9LbKApI1B8O_6usPArXK55_PEJOvGo8-z9pzwh9QwEdxJW2TKNtd4ltbKDXxiQmszkf51nWB8XS86T7xDK_FVVzZ2Pu8o11frOfUNtoy07Um_d0r1j5b-o0xkMSh_mwYaKSR-DsDewpmRQnqT-pCEnSWqW5-9aUJQ3d1CHwHNsxGYd1Mrs4OcBYdbnNc1DUKdP7w4YAdErjIZofaUWUuB7L6kdagUlbAKNyQH_ecS-79iNvSPnZkSHWn6TLIgGuTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=AfvjSIneNUDGw7LYD4Ehl6ktOkpBJIlUn6EPkjPK3Rt2Xj-Ol71xv5x-yQaHJVE0Z4v8vQ1HvLa0PsM_ny9cMCEIcUiHyEwXOgqJDwUFn25R3Qtio-OZ9861hDvuV-Bu_6fufRnywcfzAbNZboNTD_13A1RN-oJ1oxqc7RH_vTz1Oi4zxNQzQ8Bg7gjsw_sQo2dcDzbtX1DymtD3yAmSR91T6w7bTOvqbO7VUyRTVO_IiRv-d5R6FP6QA5mF8oQ5gtfk2roG4e5brBApKBqXpOaR3y0JaLb7DVTFe5YdzxVp_bcdDgcX5oZ7gMPRMcZsNtfv3Ph8R-_Wziz3MUaou0QadjrII4Cs4CQk0Y8ZHyEBAnDLf4q0GYj4LGsJiLtGC28dB6DXBSHzDSv1Qqs3l2YHMQIsypnxHbqeCTHQRS3UOpzOCZSdIeqO83Mg9HP5Ohqs9QHF9DUzz05hF429ouyo13bb_f9F3xPeLM8xTQ3XWhQGaOwdxKrDr9LTM0dbsMR8z3suiRm3DMosLx3CvLmcRoDUyR8r26Kg7ze8Vpn6NzpPsSgBUNx5QTKeP5ujjTOEQKyTwbY30BalbDaPC6Q_528SQpgtRs6cll72If9ST7Hmhp86RAu81hyq3aCCJrSsBrYfc4FFLxrhD3INGqPRWb6JDkKyaSW_wTUhc94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=AfvjSIneNUDGw7LYD4Ehl6ktOkpBJIlUn6EPkjPK3Rt2Xj-Ol71xv5x-yQaHJVE0Z4v8vQ1HvLa0PsM_ny9cMCEIcUiHyEwXOgqJDwUFn25R3Qtio-OZ9861hDvuV-Bu_6fufRnywcfzAbNZboNTD_13A1RN-oJ1oxqc7RH_vTz1Oi4zxNQzQ8Bg7gjsw_sQo2dcDzbtX1DymtD3yAmSR91T6w7bTOvqbO7VUyRTVO_IiRv-d5R6FP6QA5mF8oQ5gtfk2roG4e5brBApKBqXpOaR3y0JaLb7DVTFe5YdzxVp_bcdDgcX5oZ7gMPRMcZsNtfv3Ph8R-_Wziz3MUaou0QadjrII4Cs4CQk0Y8ZHyEBAnDLf4q0GYj4LGsJiLtGC28dB6DXBSHzDSv1Qqs3l2YHMQIsypnxHbqeCTHQRS3UOpzOCZSdIeqO83Mg9HP5Ohqs9QHF9DUzz05hF429ouyo13bb_f9F3xPeLM8xTQ3XWhQGaOwdxKrDr9LTM0dbsMR8z3suiRm3DMosLx3CvLmcRoDUyR8r26Kg7ze8Vpn6NzpPsSgBUNx5QTKeP5ujjTOEQKyTwbY30BalbDaPC6Q_528SQpgtRs6cll72If9ST7Hmhp86RAu81hyq3aCCJrSsBrYfc4FFLxrhD3INGqPRWb6JDkKyaSW_wTUhc94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=eVoQkfA-RvlYItSmRIn-nusgAmC_DM0UvSGSvloPnN2Xq2QyDpzDgmdougAkwBvCj03rU37-eWBY0b3uQnk2J1kc7f__yorMoSZY7SV96E8_l9kElfBRMM3h97-kUiFjuPT-nLcYCIkG8LlU4ZLUzUCTaJvm-eRn2KG7SSFh-akTayYBtK75eA4W0Z7fJ908kzJueP45xNAM1Aa-w8ALsioFfwPxfW_7DjUgNYyi7rx6NxempjPrLdz1Rcv6Vy9l9_XBY7r_N1SCZqvNKyuABzTMl10eTBdLebNirCLZaGVq9sK39CAFjS2F1SJrKpi2k5Ixey3wrEadzDNQJGQ20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=eVoQkfA-RvlYItSmRIn-nusgAmC_DM0UvSGSvloPnN2Xq2QyDpzDgmdougAkwBvCj03rU37-eWBY0b3uQnk2J1kc7f__yorMoSZY7SV96E8_l9kElfBRMM3h97-kUiFjuPT-nLcYCIkG8LlU4ZLUzUCTaJvm-eRn2KG7SSFh-akTayYBtK75eA4W0Z7fJ908kzJueP45xNAM1Aa-w8ALsioFfwPxfW_7DjUgNYyi7rx6NxempjPrLdz1Rcv6Vy9l9_XBY7r_N1SCZqvNKyuABzTMl10eTBdLebNirCLZaGVq9sK39CAFjS2F1SJrKpi2k5Ixey3wrEadzDNQJGQ20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=c9g1-OqnztjhmZ3Ticw7w5IHLYkl6N6IUunhr9i6Gz1Nsm4o5YJpFcjEndcY7Tr2_m16tfKrP_dqDQWa8vJCF0rXH5FJ3Dz08KZrCYGla7DHgJGNPqA0vA2OrOK9oZQOJrKf14xBAQ2OUBNjTXcYvoUdZQi_LaQg8X-Int0LLocRGxZywoISLC6xtXa9-IwRve4msl8aoqHU2Z9RlmDwS-d8HAARRk7qVvf-VrsnX9efLHULt4wJSltDhPC45okKNMK-iMqj7ziOMD-QLXfuiM0XXCg7QrxYRdPjxM6PJ0xdOPF6xx8sTGcOlCgD0huBY0ZFdglnYObFpR7jrIvtqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=c9g1-OqnztjhmZ3Ticw7w5IHLYkl6N6IUunhr9i6Gz1Nsm4o5YJpFcjEndcY7Tr2_m16tfKrP_dqDQWa8vJCF0rXH5FJ3Dz08KZrCYGla7DHgJGNPqA0vA2OrOK9oZQOJrKf14xBAQ2OUBNjTXcYvoUdZQi_LaQg8X-Int0LLocRGxZywoISLC6xtXa9-IwRve4msl8aoqHU2Z9RlmDwS-d8HAARRk7qVvf-VrsnX9efLHULt4wJSltDhPC45okKNMK-iMqj7ziOMD-QLXfuiM0XXCg7QrxYRdPjxM6PJ0xdOPF6xx8sTGcOlCgD0huBY0ZFdglnYObFpR7jrIvtqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpbAzGI5c6SMUjZxVGnVF9DTrmeLQdXZjAnySu1NMu8ulRN9XnAbfYODyMB3M3w_HR96ugq0Z3XMUYyBxdqnvyWd6RMoUWreZMbdecsoqLCmL22SzxkFN-dSD7NniTdOB1LeHcll94sC45roo1CuBHYKnWNmGm47C02OlrYLsDjN0RM63l0bvlxND0bTm5h4UnilTzcUk1AgUXrY761DQsiaG8r5KxADsDGVRxNajz7B15IMzdpCZ_IP3z-ZAaq9O8ZoKnoYdC998dLpOjebVKz6keyBGZV13QWFKCPvsvUnrwtUKLoQQUYiMN-FAp8GNn85IXAhNesXpQn_r5xgGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFNRo1zkmHx473ZPntFF4ObbaWm_QORENrg0i47a2ACJ5Rf858lXodRaeNhNE7-pce4dxtEcv-YEI9cOVMTcP2pp_BB4qbq6v1Io17RD2otwXRhDFnpfUJkn0qzVvirCBEwSDsjC44F5fGG8lnQ1SDonCXBrtoti4_AIUnFgGXFh5ilDRaHoRE1nnHlj5aIQcyj3O2-BKy3joKFbmklkJ8oQfiFGanTHYdIWQhQhCEcSGmxrtow5tabP-qapo87rt-sb8ifbW74zcatKdP3aftRwsZGxUXj3M9JHzYwJsb5TZY-EvFLTJeQNwFr3Q8gs57EyJa355zTiFcaQYdscYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=Q-mCUIb-XgopVP41H8pyT1OWzH1kcDVzrmEysiq3wXpitxrvFCENa62fxePXVlcS96b8QwtnLD4XLMt9du5vA_1Ke31vG911ulGCl9ZKqNnCfBE0iDWqlYiGln2rVBshIKOaG7nC5n64Vmdvsjd_BlmKdXhUxC6Nkw5cL67_Wd9XkAfOicuAYEJox4CIvkQYCyUk_UGlTSjPyootIot325SKruKTfzf2u4uSf-1jgMjNzUDDmf5sTABnVyyj3qe8PqDZD2ASwDVUM58trGztKOgAWugo3jjhrqYWGOjO1cbrgXGigfeCILaih0CJq7dgCTR2B9BNMXX26dnAZ5nePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=Q-mCUIb-XgopVP41H8pyT1OWzH1kcDVzrmEysiq3wXpitxrvFCENa62fxePXVlcS96b8QwtnLD4XLMt9du5vA_1Ke31vG911ulGCl9ZKqNnCfBE0iDWqlYiGln2rVBshIKOaG7nC5n64Vmdvsjd_BlmKdXhUxC6Nkw5cL67_Wd9XkAfOicuAYEJox4CIvkQYCyUk_UGlTSjPyootIot325SKruKTfzf2u4uSf-1jgMjNzUDDmf5sTABnVyyj3qe8PqDZD2ASwDVUM58trGztKOgAWugo3jjhrqYWGOjO1cbrgXGigfeCILaih0CJq7dgCTR2B9BNMXX26dnAZ5nePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=YNfBiuwTymG9u5kZ8P6NbpF1Y9SHOsPEUOWn8upyblZRy87uEyRs4zJpfvxE6F6zTYEuaizbc1rc5erRB-pfZWEQhtQAL2w-ofvww0Vrf87bG1ZqG6Kyxz2GNhZJdrMvBY_6Ejzc-_82kl5Lf0rJZGWWccEdIOE3m9d5ldiBY0tXK_cLJO8Zlisi1y2i9szqICzHO9k5r80JdsavriceBASdunnpWf-AhIMGS66D98Kh-bJmr2_uPkhWjviVWnWZt1cYCzEptirfd1SBQFX5-MuCN96FHHHfKWUuTLOF-G03SMvoR00CnLmV84j7Rrudq770HlJ6L0AAFYn2-eznFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=YNfBiuwTymG9u5kZ8P6NbpF1Y9SHOsPEUOWn8upyblZRy87uEyRs4zJpfvxE6F6zTYEuaizbc1rc5erRB-pfZWEQhtQAL2w-ofvww0Vrf87bG1ZqG6Kyxz2GNhZJdrMvBY_6Ejzc-_82kl5Lf0rJZGWWccEdIOE3m9d5ldiBY0tXK_cLJO8Zlisi1y2i9szqICzHO9k5r80JdsavriceBASdunnpWf-AhIMGS66D98Kh-bJmr2_uPkhWjviVWnWZt1cYCzEptirfd1SBQFX5-MuCN96FHHHfKWUuTLOF-G03SMvoR00CnLmV84j7Rrudq770HlJ6L0AAFYn2-eznFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=DtDhvxUbO1nWFAoVvuKN1A8l2vR9ya3bsC2upISzU8Ws9bkaAUgjJtviSfhrm_rGKKJzN1iclhtDYJ0h1z9aULQuXclCj69DSB9dtJ4Tdm_1OlqZynJ65DTrO4EO4H5vMeLVW48_3kA2yXU_h5LUiAQKt3WcInpDSAfCo0a73XX8YsbqV--Q4wjahaDVvfslmBh-4iNi2c_7eSCLf2lc3t-NK5avLOyOHmhaJWzlDBANVvl5UUAk2pxpcpcxUGt3F_BJ9npIQF17NVTVAHAaZBw_vTDP-s2KFR1BGJoKuAJRR50Qr8gfKClCteWvVRL2WFnZHO-s88sPKamsLh4FxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=DtDhvxUbO1nWFAoVvuKN1A8l2vR9ya3bsC2upISzU8Ws9bkaAUgjJtviSfhrm_rGKKJzN1iclhtDYJ0h1z9aULQuXclCj69DSB9dtJ4Tdm_1OlqZynJ65DTrO4EO4H5vMeLVW48_3kA2yXU_h5LUiAQKt3WcInpDSAfCo0a73XX8YsbqV--Q4wjahaDVvfslmBh-4iNi2c_7eSCLf2lc3t-NK5avLOyOHmhaJWzlDBANVvl5UUAk2pxpcpcxUGt3F_BJ9npIQF17NVTVAHAaZBw_vTDP-s2KFR1BGJoKuAJRR50Qr8gfKClCteWvVRL2WFnZHO-s88sPKamsLh4FxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
