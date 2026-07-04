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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 19:08:54</div>
<hr>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhNQxvXJGp96qQSWVsHq_JCN2Sqi59dUcD787YkK9b0u9usp5v9RiRN7KCa8vQDHYdwfSirN5GBN0f-GAk9U8XMZVFa52hu0Z_XcsAgpBhfeYEoz0jcm0NpxOpfwvhMCVSqRLsyTfcUbySsCKffZp2PlWCNqT7ZnWV4955FubEBgG9-QdT3o2Uz8T3dCZ47U7p_mZ5zQ97j7kG7K-DVPMelDc5qrNuxkMjY0Zd-632wq_HRCoplE4-XdvaQZT4vq4ZuluDyEzW6oAx4ZCn5w3dEKTVEFXrAVtNbCujkVIVF6SI-Gzujww2YiF8lrHVsTvpKMb4-6EhWrakY8YkFVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P32dGYapydeF8T0wd63U16X9S5pQz-lzDzeDEJZq6dEefPDS9WMoLsqIrpUuS5y2VESmyPJcKQ1_9LtsJf0HE8mH_HRs2U6kEYVFLAqROU49jzXs9RCfujqedTr7F62EZMUdwp5d6R_YvC91TeAs1RAikaw8gCyh2KFn-Psn1E7hQMuRygYMII4HhfDE6t58yJ7eMeE8qXLZ8S_0DHunpvclrAweqj6PjMA4H1W8wnPGYgjNr7hwfi0ryZrcWtAZHNUPCQLvXvTD9dZaHTXZpYq2Y8gKIqCaIb1O6aH0VR_NgwLKR8MPTTfOMA6mz0XBP8dAyKjLvWVKxKgQFjBWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6T4xuzwHyquX2gmfs4tUJjFv9pQ0j59wrnpon7yybAdAL8bO9_YwfR4BPNVr1zObVntL4vI7jqwJkrWsI_RM4Oy7X3SXL47bsUsBjAhLHB5_kghJ-ZnALCCtdXcCxljbQ7wvmnJ9nrE3y7gls6zU9DW54qRiRV3-V6imkepMBXuDFjdHSAX6vVvTyCSvfuPXGrJomKyYgdN6RzMkylrrjX97uDgIjUZymar7c4S6DHvpyFZHX6MesUhu4ho9zyiO2_0eX8QAeHcK1OrKGrc_BRZJz0oglJTWCq9Xw6Eldom4-gHFourw6N2Twp9wYxg7K_Ce7IGTpp9OfFrYB7KOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBQAoWe53VRAs_nSCpUpveb7Z4tZegMKXHRKAJZ9An1ycGqgpfFS3W3xWFoRibr9cRPHHJ3r7jDmTojekZqpBJompfBka0F5BQXOnXgGIJMjw-QKKQVdeKo1AK1vuqm0d3rfzBaiVEYm66Tc0WiGe9gIymF01ST4hRVnozErrdRwiNlWZU5o0kWSM2CC7aQ7RsQZHnS7ghB3ex0v_k8B6BDJj0XQs5NOge-dYCdZ-in1hlRmNzQIVtFNmyZHfejaHgLttQLbwY2P6h1W4_J0uW_dtfWQib7l-YJmlV1VMGMH3fe4dGB3TaudrywSyMULCLfWojOSjX9D5-GOTEvQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN1iX3Dj1ejxYuAiEbe7JJwfvrugjvL6IbsGjau7PNlnxoLO1TJiW5jzNcJGZOwbg4dVkb_RMiNf2w_hfWEa6BnVw6HJy8t878wC3-wTwaYtokbYDpS2wEhoxQFram6c4Dp-Y9RXXrev5IUDmVN2GOzKLFGMO9RMppcLQCHgDdkTnMRK3wjzcIYbm6srCQg_4_IbpSSimFo_sghDfmY652B-YhrF84QXy8ElaWmki0O2xTqXYHpXYrvJTo9Wfnv6PGl8zLOdQ2NBcEYYqj6VAG6sczHIaoDPfO_eJGAp-PTWOMD8CWoCJJfCvhJYjawDFujik7kqLd4QvwqmAfzckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=LOs0diW-0H25y81hP3OSLAVqWAsLZ6HW7rGvtHmgwJoL-sCPzp6KkJZ7g4e0nfiYEbJUetmkGgjKn6fKx9x9hgosvyIerYQ9vnefqflPppKc0wKz1cfltL4UWHbT6TYLat74B1a1KzHx-__55y0vU_SBfzVqfNq5-0UpbeoE483_XhBfKdmMqDuNb2tWwcLQHsUdDkVNWN3NVqMwctzCmdurxATfRz6Pb4CHICgcid_fu0ZVpYOHbkHw7hnj8CKb-rMc14f4lIyrkZmWz4QXEvLfAeyp0lVpRG6DeF2r-H41a1IlWI98-Cc3F9XkBg7PL13z_8lna5kfeB5HOlx0Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=LOs0diW-0H25y81hP3OSLAVqWAsLZ6HW7rGvtHmgwJoL-sCPzp6KkJZ7g4e0nfiYEbJUetmkGgjKn6fKx9x9hgosvyIerYQ9vnefqflPppKc0wKz1cfltL4UWHbT6TYLat74B1a1KzHx-__55y0vU_SBfzVqfNq5-0UpbeoE483_XhBfKdmMqDuNb2tWwcLQHsUdDkVNWN3NVqMwctzCmdurxATfRz6Pb4CHICgcid_fu0ZVpYOHbkHw7hnj8CKb-rMc14f4lIyrkZmWz4QXEvLfAeyp0lVpRG6DeF2r-H41a1IlWI98-Cc3F9XkBg7PL13z_8lna5kfeB5HOlx0Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=ILCZeFxAI4s_F2-rS32UHeR1rgN43SDGMIHwQW3mHFLoeA9KETtDMl8nei-mi7IlqACZm3FFV8QYrq7AIOW61tHy0XI_oNfzk-hm9TNU1r4si-r4N9NFOoGtoCkNLRPXjKXjmzAqdGEoGEfBYFEz-OFvEuF9biw1wsUq9tYPtDC1yhD5lKCU049Zrx7lkOTcrr86Jlo5RlaB0516MXLMNvNkAB28bh1T1DD0pBLemHft8-SboNQOWiWR5ScCB4TVd8Eiy1wu7WrmahNmUBJ03o42YHlcm2WA5t-i88rQzZoi_lG1fsIQMkQL-iguwKMADBv6ixxaesiYa896BGcWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=ILCZeFxAI4s_F2-rS32UHeR1rgN43SDGMIHwQW3mHFLoeA9KETtDMl8nei-mi7IlqACZm3FFV8QYrq7AIOW61tHy0XI_oNfzk-hm9TNU1r4si-r4N9NFOoGtoCkNLRPXjKXjmzAqdGEoGEfBYFEz-OFvEuF9biw1wsUq9tYPtDC1yhD5lKCU049Zrx7lkOTcrr86Jlo5RlaB0516MXLMNvNkAB28bh1T1DD0pBLemHft8-SboNQOWiWR5ScCB4TVd8Eiy1wu7WrmahNmUBJ03o42YHlcm2WA5t-i88rQzZoi_lG1fsIQMkQL-iguwKMADBv6ixxaesiYa896BGcWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=cqcuHo-bCFQm5DV_oAW7uZI--MpP5ujfmBx5P-Pmc11b8As5drQjngRYyyD-tEOhrXePLowJn4tT5UypUzAbYWb1KjH_BAVYrSkm-6fGxHd_XlNm2j1h4M5rDOJaxR9cZQcKrzcoINc1zC-xy9kvkSxZjznxNzEoOlTqeDQ9DbrtKsOAozRSHDA4Y3bE1kpMI_m4NsmSYtSKDPjoxuZtgc8cndpFXoYdz0dJj70DlHJyYmN70u4aqWsB5sz0ADUqEr5Tc9Wbx1stW4z9l6GrrOUZo125LROZrqgxOYnj_09uAj_X-0B1RGpCq1ry2Rmgd2qQosOGlG1aeQtIanrY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=cqcuHo-bCFQm5DV_oAW7uZI--MpP5ujfmBx5P-Pmc11b8As5drQjngRYyyD-tEOhrXePLowJn4tT5UypUzAbYWb1KjH_BAVYrSkm-6fGxHd_XlNm2j1h4M5rDOJaxR9cZQcKrzcoINc1zC-xy9kvkSxZjznxNzEoOlTqeDQ9DbrtKsOAozRSHDA4Y3bE1kpMI_m4NsmSYtSKDPjoxuZtgc8cndpFXoYdz0dJj70DlHJyYmN70u4aqWsB5sz0ADUqEr5Tc9Wbx1stW4z9l6GrrOUZo125LROZrqgxOYnj_09uAj_X-0B1RGpCq1ry2Rmgd2qQosOGlG1aeQtIanrY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=prSH689w1qAoPCbcQ7rKAFcWlq6UYBjUIJPdW5xGB_3opKQb5ud2IE_S6ciOQw5VwWAj4NnyEzYXAkoU9tc1C_qZfHxeIfOxnmYQGNUHKM_vZNjWAfvocPXBPcGZrm6U6eFQy1ykTnKMafV9FrifGzY-d5k-VBuD7eA9P0C8MVXcuHHExwR9-LKQ5hW7J2wKTOOaK9b0O4GhQgJYN41Mysp-BmSzkx0XKt4A1InWfVBnXztg5vMwFHI0siaOZQwROrCOzIzc0tJ7IG9h-FYHFFVng9703kiyKSIS7gIi1H1VpZ1ljqxYexC4YZMtqlji27YL9_IK0cTp3c_0xtnXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=prSH689w1qAoPCbcQ7rKAFcWlq6UYBjUIJPdW5xGB_3opKQb5ud2IE_S6ciOQw5VwWAj4NnyEzYXAkoU9tc1C_qZfHxeIfOxnmYQGNUHKM_vZNjWAfvocPXBPcGZrm6U6eFQy1ykTnKMafV9FrifGzY-d5k-VBuD7eA9P0C8MVXcuHHExwR9-LKQ5hW7J2wKTOOaK9b0O4GhQgJYN41Mysp-BmSzkx0XKt4A1InWfVBnXztg5vMwFHI0siaOZQwROrCOzIzc0tJ7IG9h-FYHFFVng9703kiyKSIS7gIi1H1VpZ1ljqxYexC4YZMtqlji27YL9_IK0cTp3c_0xtnXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=pQlMgORhrqBKaCIMczIpoVJn2YrMqhGKDwc8sHsL5huW1-SByElTIPNf3mJHoA0qtySoV_KQU1kHjuCZXXuDmO6VaFwp7rM-AxeiKw0EkkkP6lZR6MFG1dZzIqcSmMBjTaqzh8dNnR_QJ9OMEdK3RmJIjsFlTs5R-6YjFmxNJ475D7-7qcRkN9eBEPFUXt_GwQGq_Cmq90Wancd0hVUjUw2Bo20MISJQhMwTNCyHj6Qh4f858PMW0aNJ83kbFQXD5lYNUqcuf980x5YrMLuAgn41DAckkcYd4dgKW3FctlHrmLbXYZW5ZKtHjnNaC_NGuGGKGL95QTMMRgTLLTSH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=pQlMgORhrqBKaCIMczIpoVJn2YrMqhGKDwc8sHsL5huW1-SByElTIPNf3mJHoA0qtySoV_KQU1kHjuCZXXuDmO6VaFwp7rM-AxeiKw0EkkkP6lZR6MFG1dZzIqcSmMBjTaqzh8dNnR_QJ9OMEdK3RmJIjsFlTs5R-6YjFmxNJ475D7-7qcRkN9eBEPFUXt_GwQGq_Cmq90Wancd0hVUjUw2Bo20MISJQhMwTNCyHj6Qh4f858PMW0aNJ83kbFQXD5lYNUqcuf980x5YrMLuAgn41DAckkcYd4dgKW3FctlHrmLbXYZW5ZKtHjnNaC_NGuGGKGL95QTMMRgTLLTSH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=oPKeDi6eYW5Rzc5T6KWMs0lX3ZxuX3xDkHwdwNiCIXJ02Zor35BG9EtJp8EBHMjfktlTMH4NsVcZ0_MQ8ja5V-6fO2M0-qmPP-6m1RgvQwOMvKpoCtTvc0u3Lv8Pc8yVxS_UmN-XxCpwUnmuPgAOHKEgWfpdyBvhFoyXCC7nK2pfH8didl2eoj_Q0lDQ0YCp2_FRuIJOSLI_g616SCAGWzlEFlLvuPpNJGiLZCeeyPo12sRzFcVuGHB-Gi3rTSGfw5RSJAIQM6lbY8_dbdA6jnHHjMrojP0n2SiGgF4m_uvdeqsjtXMeLqF1LwCNjA3IqpqMwLPaZ4jvt1j5hfhj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=oPKeDi6eYW5Rzc5T6KWMs0lX3ZxuX3xDkHwdwNiCIXJ02Zor35BG9EtJp8EBHMjfktlTMH4NsVcZ0_MQ8ja5V-6fO2M0-qmPP-6m1RgvQwOMvKpoCtTvc0u3Lv8Pc8yVxS_UmN-XxCpwUnmuPgAOHKEgWfpdyBvhFoyXCC7nK2pfH8didl2eoj_Q0lDQ0YCp2_FRuIJOSLI_g616SCAGWzlEFlLvuPpNJGiLZCeeyPo12sRzFcVuGHB-Gi3rTSGfw5RSJAIQM6lbY8_dbdA6jnHHjMrojP0n2SiGgF4m_uvdeqsjtXMeLqF1LwCNjA3IqpqMwLPaZ4jvt1j5hfhj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/W6fZjvEJcMp9D7TXH-tqS5phNCktm5a13S5gpF4f0i2gb9Hm6kd1SGeBU5zxHq5R5HVjK_n9Bp-H1KLmrN6hg5S1GmVDcSH48p-sZO38s0I64tzE7gvbhR321pR7_tYYWVj2m2IulNTJpxZAexVl-PpiMQwZh1KiPHVwhvozy57_Fc416SPstg9KCzecxh67TiVIHVcuhuTDCvev0Zb6r2xryYZCpXXudSiPmosXfT1hEderm8RsFCzcZlVxg4lrHSi2hfZ9KgNs4L0sTh3Ei9RDaN-AfQ3YZ3pUe5zwvC4aQSfuGT3XjcVUx5-yn85WdUidK8Mb6PpcseDtPydyYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q1iCsAGmHRkg3SQGI_ZVGHEnGc5wBrHeHCAcotVplSd09Q_3INQUMVCG00E543m1Yf7MpxCIpW7D7-yV1coWk9VgG0-HHzWWA7_Fmxj7r5Y9cLphfuYfpN36YAyT81ifzInHGqeCjaIaLKvbJN2_aXv_nDFFZpnjta7Cl0cVTShYu1oim39j8lkELjbrkQZCyS1xeQPkpWWQrGkAyvk6cOFrfFez2ElDL4xgl55pkV_KZB1ng6-292dsHi55mws7DhLNw3uNK-cnQKUg79Vh9qrCNpCKCIPN18B_oJaOxPK5O9ASFZZh1r7UVhZiH0nLIuJ0F4T4DQ2ar5CQuigBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=QM-mNUjBZX337UkozIQLyBalZy2XSxDyqORPCzCyByVCYWoxv1yinY_F2_ovNPf7Rt88YE3k24uRR9NcSY3n-0qorR5o4yxVh1zl_SzRBY1bZYGPTqt0p5AZ2s1dFmXx0gDs6wyZk3zfw_FrIf7GDud6J65h7CCy0LeCNsADwoX_LM35sLflJUAs80A-FSnEzR4DzWeJt1r2vnB2ojdGhlXww99F5YpjqeGM_FJkCEE0sZ1MafdqvzUSr8tuZjbR65zdCrCXAjYglBA4NL2WWrp0CfR8ifY47n_cb58W3A9x1XPawgyK_iNi18OyN3qsZjLEkAhZ3XeImvG_VdlHdkw4tUz9odLpLEHDgGxeNyNWFz3vN9HlWyzBGzIiY3O7st8Dk4MBpTY7CisHE6TpcgAfTYPFBH7mK6QDKu8dsYC2MA1yfdu6Xd7N8TcAImq6zxZAhnQbJ0rQwCabH5XTQLfJ3IuKMOPgB0ixh7hOpICfxIeLmtaad1gjns0cijiB4DNgF8-_yd2224uQdVXvcfPhgy81ne9OJc_9LP6hNKHwewhquWs7DI-grZz-vs7u3_9WqVw8k9Y8DeSXxELouzef5xYb0CJMt2vSeFfW3jKSHOZsI6iJVnmmXb1MJ0W3qZ0hdUd-mMs6PqQOmNpuOP8c8cUlkedKfqAQFeVsfqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=QM-mNUjBZX337UkozIQLyBalZy2XSxDyqORPCzCyByVCYWoxv1yinY_F2_ovNPf7Rt88YE3k24uRR9NcSY3n-0qorR5o4yxVh1zl_SzRBY1bZYGPTqt0p5AZ2s1dFmXx0gDs6wyZk3zfw_FrIf7GDud6J65h7CCy0LeCNsADwoX_LM35sLflJUAs80A-FSnEzR4DzWeJt1r2vnB2ojdGhlXww99F5YpjqeGM_FJkCEE0sZ1MafdqvzUSr8tuZjbR65zdCrCXAjYglBA4NL2WWrp0CfR8ifY47n_cb58W3A9x1XPawgyK_iNi18OyN3qsZjLEkAhZ3XeImvG_VdlHdkw4tUz9odLpLEHDgGxeNyNWFz3vN9HlWyzBGzIiY3O7st8Dk4MBpTY7CisHE6TpcgAfTYPFBH7mK6QDKu8dsYC2MA1yfdu6Xd7N8TcAImq6zxZAhnQbJ0rQwCabH5XTQLfJ3IuKMOPgB0ixh7hOpICfxIeLmtaad1gjns0cijiB4DNgF8-_yd2224uQdVXvcfPhgy81ne9OJc_9LP6hNKHwewhquWs7DI-grZz-vs7u3_9WqVw8k9Y8DeSXxELouzef5xYb0CJMt2vSeFfW3jKSHOZsI6iJVnmmXb1MJ0W3qZ0hdUd-mMs6PqQOmNpuOP8c8cUlkedKfqAQFeVsfqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=J-8hxTr5CTW5NfFzOSQmNwOBanJQASeI13qfziZEwHOIuZVPQ2NEYd5nJ9PQR8CWRWrTqcvAGDJQSd0fTv1vnEZRRe2gsc_vJhDWRZ3ED3XXLL3RiPgLXhfr-BKoPmw2g946bjhA370vBNWLBVZS06xXf-gf3l0GXRprDTSThE0ki0bOPAJ8IuVBVm0m1SXEce_BnC2kRntMUPuREOnNsEAwh7tmx6pRWqHcz_asUxskJVVOggN5aquhJ1Qo656L5fey7mLilyyQM9npA6eWkuVvyx7NZhY6AV5qt2Vm7tt_iWdILhXq3BRuz67manlnUke8e8uklm1SIHZglZYXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=J-8hxTr5CTW5NfFzOSQmNwOBanJQASeI13qfziZEwHOIuZVPQ2NEYd5nJ9PQR8CWRWrTqcvAGDJQSd0fTv1vnEZRRe2gsc_vJhDWRZ3ED3XXLL3RiPgLXhfr-BKoPmw2g946bjhA370vBNWLBVZS06xXf-gf3l0GXRprDTSThE0ki0bOPAJ8IuVBVm0m1SXEce_BnC2kRntMUPuREOnNsEAwh7tmx6pRWqHcz_asUxskJVVOggN5aquhJ1Qo656L5fey7mLilyyQM9npA6eWkuVvyx7NZhY6AV5qt2Vm7tt_iWdILhXq3BRuz67manlnUke8e8uklm1SIHZglZYXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=oMVEJEW1CItvAJX1FfZfwP2q40yLZCfk1HRlq9Yv9mE3_Ddbjxt2I5SQn_iAkzCDKGQGTOYWLOQYntBOH5--t22Pz3U1lJRT91scnI-neY-81YfRtsEuSoj7NJIv0H3t49ig2PK-8KFlMDLymvMYCkGZbjbYocAwEEigSzdkoqwzuwEX0lsJrF5TCqO7CycjaNQ9PlBWvvYXfd_VYJvPHQwu6jpwcTmMncIVJ--JAt5blY-92w6B93mSyFoG0kkx_jMI_yjRPRJXKCgyZkC0cMA7rG8AK1HPEOkb79ROaaVKjTNd5uek-_4HDU1hck7KpcENTv9vrIWk-xMRm5WZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=oMVEJEW1CItvAJX1FfZfwP2q40yLZCfk1HRlq9Yv9mE3_Ddbjxt2I5SQn_iAkzCDKGQGTOYWLOQYntBOH5--t22Pz3U1lJRT91scnI-neY-81YfRtsEuSoj7NJIv0H3t49ig2PK-8KFlMDLymvMYCkGZbjbYocAwEEigSzdkoqwzuwEX0lsJrF5TCqO7CycjaNQ9PlBWvvYXfd_VYJvPHQwu6jpwcTmMncIVJ--JAt5blY-92w6B93mSyFoG0kkx_jMI_yjRPRJXKCgyZkC0cMA7rG8AK1HPEOkb79ROaaVKjTNd5uek-_4HDU1hck7KpcENTv9vrIWk-xMRm5WZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=jlix6Nrb35jPb9gOdWZPIUG-1CN7_YS_IJOiH2nhX_vjKskT66ozPwWzw_tL3cCoExbi4mmBNatZWfySu_-97bULRNP6kJ_pVCxVGxveNT4GO6dza5v7nie1xI_B7JFQBYRAR_OZNipXjWUO1DMMy-abWJDKUxzcHZKIdWZ2JL392pT5bgJUWuEiwjVsVfN3kZBUkO8lQ7cLnC2zNd7fYWFVgJU7XhT3Gmyuuw1XSdbebUb5gDhSnjtrrFsk6RoSb-tC6U_DarBfeh4OhVvgJIKaQ89cRnPEhPTH5vj177cuwalhII2-DyY_2etJwAQR5xFfUekEZciJGFDdRb5AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=jlix6Nrb35jPb9gOdWZPIUG-1CN7_YS_IJOiH2nhX_vjKskT66ozPwWzw_tL3cCoExbi4mmBNatZWfySu_-97bULRNP6kJ_pVCxVGxveNT4GO6dza5v7nie1xI_B7JFQBYRAR_OZNipXjWUO1DMMy-abWJDKUxzcHZKIdWZ2JL392pT5bgJUWuEiwjVsVfN3kZBUkO8lQ7cLnC2zNd7fYWFVgJU7XhT3Gmyuuw1XSdbebUb5gDhSnjtrrFsk6RoSb-tC6U_DarBfeh4OhVvgJIKaQ89cRnPEhPTH5vj177cuwalhII2-DyY_2etJwAQR5xFfUekEZciJGFDdRb5AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=evHV3ucnTx0LTRXG5JpWWkADx4mkXXtzqUpVmezeNF8il08gng11Qd2MNVs0_W2b16L8LBcdi8cGwUAIzAYvldXDp-RAjhjJbja5jEGzvrKEoRzhhwdVloVrE3BFK877EhtWTCcwoNs9XAt0HL_qgKJ_i_s3gIbQ_YzK_prWXr1agog0my42yj_NInBkRw7jap-_IBs6RaNKvGnWONxmNUW9eUerwZG95TY8XKkv1C0Q1J5HF6JRitK7IPG8LDW_cPIcKarVrLydScqFbocwzZ4tvzAeYGXV2ARiUusbMQ4U2xgaH4jgxdz2tfAdv1_15NIBxDX3j6j5oDTkXTV1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=evHV3ucnTx0LTRXG5JpWWkADx4mkXXtzqUpVmezeNF8il08gng11Qd2MNVs0_W2b16L8LBcdi8cGwUAIzAYvldXDp-RAjhjJbja5jEGzvrKEoRzhhwdVloVrE3BFK877EhtWTCcwoNs9XAt0HL_qgKJ_i_s3gIbQ_YzK_prWXr1agog0my42yj_NInBkRw7jap-_IBs6RaNKvGnWONxmNUW9eUerwZG95TY8XKkv1C0Q1J5HF6JRitK7IPG8LDW_cPIcKarVrLydScqFbocwzZ4tvzAeYGXV2ARiUusbMQ4U2xgaH4jgxdz2tfAdv1_15NIBxDX3j6j5oDTkXTV1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3ENSkopgj3JXfFSeEOYbqo2eruKq5Edd6uXeXvu_pj1G3br8DcKRbTZ0tHhq0y0l0eW2H6P0LG3qUbxg99ag38C9Ksb7_MCB9om1jESbEyB_fTJNx28yKneO9ckwN5X3MV5T0ad5Jmc8QJqwRNSTC8ZK7X5B1bbx9MqESLbAkDISRA-7Tju_8v_nyQoQF5YVNViGsEKVj0joFJRSwfA_yJBsyGzKIFUSghqZPXSDAIAo7K--WXXVc9Cq2No9X0oySGYziZix4OU4T9Y8rIMdn6PBOIF0PSWxe5oFtEVs99hoKOtZHhSBpjCEm_6XPQ9xkilXiVmnvywHGzq2dmXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyrM_b_XCOK2IvpO_UtxfdYuZzUjU1NJ_umw4cgwCNdN4dWfVU-0bjUSVNBw-e67Bp1p-tvcgPD2F9Sa03oobo-UQBRdl2shbP2YzvXVsVZjrxu2y8kL-sNiRD5V77BI5G20bhbjyY-ZoRT2ZgTGtFXJTVG-bHtZi-oe8SBUcl47LJOn4_ZWx_ns0MwF6LUraCLp2wwmNixH3TcEMcBiAOxLnadAuF_wki-7GEvc6qGOX3hryjnc5hyykwMM3nyWlvjO9SR8wsGEPvMUnRceOzwA3ZcuALb7kl_6PCb1glI-8s87VG4Q5pNrcu9OzktZ07SlLwJ1s33Ia1OkIm1y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYTprXPTu2o2ZCk06HrbFMnGOhKqrmCFcSk200pcUDZHAIojksCPSAnWGhX7Sz58mYxUi0wW2ZCXBecdiUqHM-f_e7LlTzRmI5OL78lOGUG5Ez4PYiZbsSjpJEP0a0Pp8D81IS1cxjZiFAuFp9KHcu1QyBrv05-GP0bKLPqJEzkxpRx1NDvzbKzJ_SAAwvp2MXS72LNBpGQsbh6is-L8n1TZIWizyWu4NXQUyHiOYs6-YMPntIL1jN6PrNVyaCJTXtBu1H-4YJNr2wdz74sBBSSsjXQPFEQ7zRlhmE9QRrVPnzhzP4xFcV7MrAxviC7OQtNQkMQIU3r1IRfxwIr7fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfb7i3vKjbMXa19xtT2ohmM62JvwU5v_xC57UlCYTptHJgGVGcIECy1v55bNxPILnZWuLIyGwTuQt_TyjvH4e24PfmWeDgYka0uw3RsRg2xhIO0H1PMK6r4dSW10ZbVJsRslyQEqJ94S8BBl3UBnXgP15DOXAb8C-YnxvoxvmL21qNJheOqbq7XmcAm5vXOt0GuCRjw7RzjVHU6xbj6aLQcUWIbSRAZ3LsKK-4jsEnHRN0NtQpMOP-TWs7xO3SLdmiWtTDenYbYRXHJnJL3EU68sD32g6qLZROghnrCL1cX3KFt-mDYk06I1giUqGyXs3ewRKENxCyXHS4WisPtAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUavKjwEezKvp8yxDjk9f3K-ucBsScwQlwnXUmmtxzWc3_tsBb9QqmtVZipj8kY5hE3R1Dwb1S7o98X4Wmou_kfZsMIHdoNaPhURpBZmNBdNY23l3kaN4WhEbDetNkZsLehKmqQnyFNQEQSGLsXTvIAKHn_B9pLEWYedjCRYdXNT6NJQSbbSdDbjli0wDagNU0WQNXH2ytn-J69JjotIawSW-_ytk_OMzFvwpko06yKyAbcD_-L5-pXMORwfqFEWNLTB2h_zdgUz_RFEFd90y7wTf7cMqQWlYq58cYU1AeE-3MxNCBWuWI1BdfjS2o0WOoQFDUqRMYnv7kwXh7m44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX-KVTAozy49v87QUUhWa8kjJOAtHAK-MUK1XhCgGRMC-CfxSrc0K48yMTPM61FkNtEmtpkkHrqX2BI2mRpuuFsYV6KcmeH2KSaKgk5n0TSvWYXqYpqGt9KAiDqLOV2goTR4IE4yJG6ud2syrCltLANszQ3MQ9QAx4d7_Q4XpDnnvRFw_ZhI3s34eOCF2oHh27j8T8OL7T_jD0ZkrDH4asWm0-dsunwqnOF0G5FrjhQ7cmd8SdsZCk0uuP_jhNOb5STaIi_3sDOEezPe8NkIykg-WenFOoRfmtnJ_P6ip67hzu9Srzt5K48keyPojEMjlgfNXHHS7BoIhXNWxZZDYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=USMXu0kIwIpRpmLGd3jy8oA_kMo2FzmhZZlSW0_Gc4w9bxyrFB-wvVJ42ssf_SsyqNisYjg4iLptR9-n2DdjsTq6EDO1TwAOH6fNyjafm2i-2VISn2bOvqP_EfEyp4wk20cDKAaWPIBDfCRU82qFUneVn2n7XOPPbCYCQ68Q_ws1nzbnR7vijWTnjVqkCZPQJlzqZsS_o9r_5cSdSzIrICqIONbPwy2erBPM0NtvWwYhXZ6FgjMKQxKqPQfMEaLznOTC0yTkBrvC1pNP5cqJWkKDuRXaCn31WL-VGbRbzvn0I8mAdY_Fiy38U541lN8U6FnS2D5Qfz1NoG_X5Tm_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=USMXu0kIwIpRpmLGd3jy8oA_kMo2FzmhZZlSW0_Gc4w9bxyrFB-wvVJ42ssf_SsyqNisYjg4iLptR9-n2DdjsTq6EDO1TwAOH6fNyjafm2i-2VISn2bOvqP_EfEyp4wk20cDKAaWPIBDfCRU82qFUneVn2n7XOPPbCYCQ68Q_ws1nzbnR7vijWTnjVqkCZPQJlzqZsS_o9r_5cSdSzIrICqIONbPwy2erBPM0NtvWwYhXZ6FgjMKQxKqPQfMEaLznOTC0yTkBrvC1pNP5cqJWkKDuRXaCn31WL-VGbRbzvn0I8mAdY_Fiy38U541lN8U6FnS2D5Qfz1NoG_X5Tm_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZkAekz2byn97aQVIZl1MU764FKZbczf-pBPxD2V3-UQo3T4NjBbVsaQZbLGo82GyX_OrsrK2xbc-AVSaeEqDYFf4CPqnbAmkBuQCUJ_-wC7FmT14dpp64bjdZRehzjZnmnZbAdSjuRvwVrLMwQKY3pLSow-zykpgqRH8vSXiX3SK8k7mdVHzC5RmaLIcf0nkdyff3FP9ui0mD4yVrA6iJkh1IqfHsAHRjRKa6eiO-hC0SkOc8XNjB7iavrrbIR5PmLbWmRQknXoBpaKVZaE8LZ1Iqel_QY773mi4iL_ajd5v8ClhcLoJJzJme7a-bIPskUlzHYf-I3jZN8h77nKXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=nICBwalFq3igT9Tw0eg2RCKUS-okA-8Mdl5DE88OZ_OTDW4eZoH2oUbyP0NltsBQUA1paXGF3jSFRjIImn67ctkRo_pgBNBoINmllKt6HsgKoOl0UzF6ekALUl-KtDNNRpTQbGwN-fY5ZZfJuIhLIDToC_XbrpryyCjtUxmJ0neGaeaKQl-l452aF3BoV0g04c453er6IN-gR4yaul9KO7WCCIkwr3IsLuXy1nYlVgm6SUPQyDXMzwP3MgCGYlcVKopDgvuVw1Iq5mzWYm6asGLZSeUiXgQ1dpFQbJ6-IF_tA4YPVuDEsVySLcboOru7jh6t9RbHXmnxrnBm9JoX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=nICBwalFq3igT9Tw0eg2RCKUS-okA-8Mdl5DE88OZ_OTDW4eZoH2oUbyP0NltsBQUA1paXGF3jSFRjIImn67ctkRo_pgBNBoINmllKt6HsgKoOl0UzF6ekALUl-KtDNNRpTQbGwN-fY5ZZfJuIhLIDToC_XbrpryyCjtUxmJ0neGaeaKQl-l452aF3BoV0g04c453er6IN-gR4yaul9KO7WCCIkwr3IsLuXy1nYlVgm6SUPQyDXMzwP3MgCGYlcVKopDgvuVw1Iq5mzWYm6asGLZSeUiXgQ1dpFQbJ6-IF_tA4YPVuDEsVySLcboOru7jh6t9RbHXmnxrnBm9JoX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=V7eYyYWZDkQcmCE2v6KNyamlicfDbU328yAEmE0RHbrCv2FXEulyvOOhPpG0GvjwkohWyHwTDEEhCigV3YNwfXto5wAYmElrfoXo-Xehi3-gJnZ8xsN6qlBLn3CooSbMb1pVudp98FdoCJAstF9D4ZY9QjMm-UqAfu3iBfizHXh-Eop4ZQfSpyYGx-vOrm2lUJiIRy12u_oRv9d3VJacQqywdC1pGdCysoXT2j3S83yI5Vek2pxTEe6Du_4lbpPCumauYOvanxV-Q2YjjmonChs76imB8imM9LgDm0EJSwllwxH7Fq7NjWd7RNqBG4-1Jy7T-i8kWCw-AImnwpd2qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=V7eYyYWZDkQcmCE2v6KNyamlicfDbU328yAEmE0RHbrCv2FXEulyvOOhPpG0GvjwkohWyHwTDEEhCigV3YNwfXto5wAYmElrfoXo-Xehi3-gJnZ8xsN6qlBLn3CooSbMb1pVudp98FdoCJAstF9D4ZY9QjMm-UqAfu3iBfizHXh-Eop4ZQfSpyYGx-vOrm2lUJiIRy12u_oRv9d3VJacQqywdC1pGdCysoXT2j3S83yI5Vek2pxTEe6Du_4lbpPCumauYOvanxV-Q2YjjmonChs76imB8imM9LgDm0EJSwllwxH7Fq7NjWd7RNqBG4-1Jy7T-i8kWCw-AImnwpd2qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=ZMB4JjmrXjmL4QT9B-Ka6sYZbTfzkiflfiKFeQ9U2OTrcldyuNkUydhED7gdIsLQG2zuNmA66DzO2ZsK_xpnKp5oOqY3phYZXpiP1nLejXZRBAtS8BNNsxKyx43juh8PfnUCwg8dHtWnn2GorSmz7tQjTLIMPNoq-r3p4mCb9cKecrLvYZ-2xB-ma3AkMvb2XQrV14pM7rhYPzbJdlrfz1fj2Ti3Dc4m1ll_b0tZAwAyO4X2Q7zCDmJuVCwbNIa5kRDzbN9R348rMuzo8izkzPp9z_5tE-e7x-XOi-5WvPfbRhiEb54CY1p7-hUVXyX3bECnQUvvOvyCL3QoL91ABg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=ZMB4JjmrXjmL4QT9B-Ka6sYZbTfzkiflfiKFeQ9U2OTrcldyuNkUydhED7gdIsLQG2zuNmA66DzO2ZsK_xpnKp5oOqY3phYZXpiP1nLejXZRBAtS8BNNsxKyx43juh8PfnUCwg8dHtWnn2GorSmz7tQjTLIMPNoq-r3p4mCb9cKecrLvYZ-2xB-ma3AkMvb2XQrV14pM7rhYPzbJdlrfz1fj2Ti3Dc4m1ll_b0tZAwAyO4X2Q7zCDmJuVCwbNIa5kRDzbN9R348rMuzo8izkzPp9z_5tE-e7x-XOi-5WvPfbRhiEb54CY1p7-hUVXyX3bECnQUvvOvyCL3QoL91ABg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsWK1bwa-GZ5d9uupHWmgKjfWoji_ZZq2vVkjKf0DO0UwjFvel8H5k9jghKkntwCqGw1zJ9iSjc569yw8BpyjoZWpU0YV75HnwAS-p1MeX4ACHEEqL0BZIwOu3A6sNq0E3CEdbg7ivRb-84d8nG5qLDn08sKAo83aR1_a82biPiaPn5mJQ3msKWvHyUGznKFlbWwwPkKNOfGvgxOIDzizP7GbJilBsPUOE-BXmJREilPn6Mjp6zAUm6DMKXDDFlbCu37rk_7o6-JRjt2bU1KnRlqR6ueSHuHPhrhzvghfRcAfrxxMlkrSydwA7-JwZQ82p7App-QJQTjVOjzwbv1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=h10u74E8YAaITJeS_eWp17O0IPy6pr30gItDES5MFMoVQPV6CDNS-1tFMd6CpZb3qSqCAhcJMJXIn4oBd5-kn5yCeDJa9B3_vOKSqblsx2FReRlBu4J9TtYGJApzCPh57IV9Tuo_Hzxpncaj1xMYGeTEBRmn4TpmA5lpXuUusjzSNdKuzMHDLV-rOL_KCZ6mE4H5lBYeoOhBM8HD6NzEUmceVblWtEYBGz6tK_Rcme-ni7mjC2wQ9fQxvlj3gcCjEvs8UNDKFxuZBzJUjJDFL32-5aFKCD3wGB2slEO_JM_f121uBZ6h3pxYYVAmVpY6Z7vx-0P0nAe6H8WmOB7Uyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=h10u74E8YAaITJeS_eWp17O0IPy6pr30gItDES5MFMoVQPV6CDNS-1tFMd6CpZb3qSqCAhcJMJXIn4oBd5-kn5yCeDJa9B3_vOKSqblsx2FReRlBu4J9TtYGJApzCPh57IV9Tuo_Hzxpncaj1xMYGeTEBRmn4TpmA5lpXuUusjzSNdKuzMHDLV-rOL_KCZ6mE4H5lBYeoOhBM8HD6NzEUmceVblWtEYBGz6tK_Rcme-ni7mjC2wQ9fQxvlj3gcCjEvs8UNDKFxuZBzJUjJDFL32-5aFKCD3wGB2slEO_JM_f121uBZ6h3pxYYVAmVpY6Z7vx-0P0nAe6H8WmOB7Uyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=dFG3x9uNMM3aRNaAIEU114rjmk57XfKQ1iVMU4_6ScRHhFaWGUM1bGRymMVjU5teg75HZVfabOjIDnvWpfprUQnkEQa-PZPKgVVHTRLMjqLblkb8wqtml6uW0eCjvb608CLVedQeo4tWl0zIogqgFnC_D3CLnj30w37nWS-bYY74LbXSuoxm0AziWPpSKZ4dS00QQKEj6KShbdaQ80Oya7Gn-uqRG58GTAzgrQlKTTwCnDhq6CauhT9ZSfz2R-NpGPeIcBytoPeStlMa5hcQfXiev4G1AGGEuk98EYNXNpdj0U71QEItulhWjDE5YYI5vIs4OyJZFOdBodWAYZ4IMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=dFG3x9uNMM3aRNaAIEU114rjmk57XfKQ1iVMU4_6ScRHhFaWGUM1bGRymMVjU5teg75HZVfabOjIDnvWpfprUQnkEQa-PZPKgVVHTRLMjqLblkb8wqtml6uW0eCjvb608CLVedQeo4tWl0zIogqgFnC_D3CLnj30w37nWS-bYY74LbXSuoxm0AziWPpSKZ4dS00QQKEj6KShbdaQ80Oya7Gn-uqRG58GTAzgrQlKTTwCnDhq6CauhT9ZSfz2R-NpGPeIcBytoPeStlMa5hcQfXiev4G1AGGEuk98EYNXNpdj0U71QEItulhWjDE5YYI5vIs4OyJZFOdBodWAYZ4IMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=P5uswDa-N2s9LWH2zLcfxsKETVdYU1mxGoaDJIoEuRuQnnIA62iZvgURgp7Hy-e3Mb8BJBEwmZdsphlMZ8d-_0z-85G34BXmEem8nRz4ck0cAvQbDZZAShd9H7KTtBrWxuvyl45IG80t4mEXO68nDPVPClab4BzUTSydn6X86DvZfyaA-t8zxxB4ZCyRc_Ot1E19TKDKC9lll-2CEsc1vJ-Nt824hlczBSJCrCStIr1Ww5pq5AyZN9QKAAydxPjoE2UeDJPoSQQ-CHTtJcz07kFhxKbpIBQwHvz3kMDLW4dJAnGXI23Cmuf_wajgC-XycUJbO5h7JvyH_-JM0leS8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=P5uswDa-N2s9LWH2zLcfxsKETVdYU1mxGoaDJIoEuRuQnnIA62iZvgURgp7Hy-e3Mb8BJBEwmZdsphlMZ8d-_0z-85G34BXmEem8nRz4ck0cAvQbDZZAShd9H7KTtBrWxuvyl45IG80t4mEXO68nDPVPClab4BzUTSydn6X86DvZfyaA-t8zxxB4ZCyRc_Ot1E19TKDKC9lll-2CEsc1vJ-Nt824hlczBSJCrCStIr1Ww5pq5AyZN9QKAAydxPjoE2UeDJPoSQQ-CHTtJcz07kFhxKbpIBQwHvz3kMDLW4dJAnGXI23Cmuf_wajgC-XycUJbO5h7JvyH_-JM0leS8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfXFZ2csdMXDQVCXuDnvyZSfXCvwjrJBXmQCQDpOxMWzS5PzYlEvDsrK26-cCddr2BPT3dIDarVJhE_71LogBuHUt4fVXM6pgYaCUz2NS99KjW-8_1F37lG-w243cjMfgQPPXfzGWzknREeWJrsRzgC0BCHj_NYRWWyrXFWsFv5Qj9ceCkD_6i1XCvRrfWAesOzRpsEDuNrLL_4YGLb7-V_R9hR_CQA4kG45aRADTwmBvMKcacUQXOG9bq31HOvZ4PRBdNt6UJLnsjywFyRQ7B47Yd-YwBdC71uAMiVjJR4Pf1R3L9iGjKSQkB6r2YTA4CZtjSDrmf9IVLwNmhFYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeGNCkD5HWYtC5uo0AxzNQp9nWz5IKoFxkFwZrvaZEJBKngTQSD4Me7KQN2W-B4Dc8bNOWTG-hN4fEwxBPFZVNReHBkes-LjAftCnK_hh179LYwYjnd5ICrCE2cKGK_3Ze_U0CvGKS-NV-U8cGkOBqW-gg_W3uh2W_ueTmvJC_c2lhkk5IbNGlatplGXUU6QKc0b1GMp-_N-5wttaRjrlG3-EG8l84VPyFWdL7SdPo4nns6hOg1jOg3fkAEr6i-8xomEALjujFs-yVAvuKAZB1CXqpGlZYZogEYnv8bsiIEhpZtixpllcyqIEXbsV1hFALZBS2_YudFs9821YRBZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=Lm0E5rK1Znu6_Cd-x97e-hga295JeIl7VEVXSwH0faTuvmfQeJ91IybM7k7vF-wTQy8n8H1UnIma5KMv2_kQ6BblUo_qy5Z1oari3JsRC8IXfoGf-uwS8QxNO4h2dfkkjwXTvl15xJ_eLGahRIv-Qbi_tWKGd3eX_gETPnm8AEJGC-az98-Yl07ynGci-P-d6ZOEIFu1HP0CzgZEJzdUdFccvhsbLiY1yNyQ5sHfgfhQWYerBeAdtWZK_5GDQ95sf0gDME2x1TDJFYK0Z8cf1nsypiG7cykx6WBaDVWQkmd9tR33zWLH390GcEemRlZuNsx-eNDuLJfPzxIm2fiC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=Lm0E5rK1Znu6_Cd-x97e-hga295JeIl7VEVXSwH0faTuvmfQeJ91IybM7k7vF-wTQy8n8H1UnIma5KMv2_kQ6BblUo_qy5Z1oari3JsRC8IXfoGf-uwS8QxNO4h2dfkkjwXTvl15xJ_eLGahRIv-Qbi_tWKGd3eX_gETPnm8AEJGC-az98-Yl07ynGci-P-d6ZOEIFu1HP0CzgZEJzdUdFccvhsbLiY1yNyQ5sHfgfhQWYerBeAdtWZK_5GDQ95sf0gDME2x1TDJFYK0Z8cf1nsypiG7cykx6WBaDVWQkmd9tR33zWLH390GcEemRlZuNsx-eNDuLJfPzxIm2fiC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/st1qJGPwZA29mEErwvwtRltTDGtIo4p1N3RzPYl06ePSOjGrJXq-pBtNenlAUURJLYCUmTfMM3s8FzYNkMmtLNFiM6RP3yE9lnt4jWZN-bQ0L_0JA_9nqRi-jlWxsmxy3PTEqkXh1vhJdU21XXqCNn4U48RY09exrUiAyOu6Nj4nB7nuInI4Gqzu92izPCKnKlhHoeOgQGpWgbhhK-R7d8zIC1DbbQQ725n29M5Ov9fM697yPwx2PGGESPs7BV89vAoi0hUZa9KySw-YhAnsP-dtx3Eshh7dWuGbYRNX6jaXAR-0t5kI0iqJL1jL4fxWK7uGUWMOJ8CZ_-Z6lT39pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=mhqX65TG1D6-urpe-lzeLgHmU5MXuf-PVuL8u2nzmH5fS5RRTrohY2Gah5nAeyHizGHSjifyf-igdJ1wdRJ4vNNgxiRC8wYBA-P1zYLJQRbkk82JFp40S8cDQN14GNikzdizT_ZugNEOlKja_Ey4Varj6XoA97t5aK7qGdbU6fYwoqT7qoN2PDpKReVGLOi1QInBtLYmNY-o7W_KV8lLvyDyx-F2W4pVzHJAoT21VuK-6u41P_7BKGQ8VA3ffGPYJ17-TvjqHg4pCtJyCFxiTRvRnDgfIyPATaNCW4PBDlCRsPZhxbIJQw2yZfjYNbQrC70q2d7tB_C2YzahDsPYDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=mhqX65TG1D6-urpe-lzeLgHmU5MXuf-PVuL8u2nzmH5fS5RRTrohY2Gah5nAeyHizGHSjifyf-igdJ1wdRJ4vNNgxiRC8wYBA-P1zYLJQRbkk82JFp40S8cDQN14GNikzdizT_ZugNEOlKja_Ey4Varj6XoA97t5aK7qGdbU6fYwoqT7qoN2PDpKReVGLOi1QInBtLYmNY-o7W_KV8lLvyDyx-F2W4pVzHJAoT21VuK-6u41P_7BKGQ8VA3ffGPYJ17-TvjqHg4pCtJyCFxiTRvRnDgfIyPATaNCW4PBDlCRsPZhxbIJQw2yZfjYNbQrC70q2d7tB_C2YzahDsPYDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHHz3uWVRbnw_gZyrhyMemWPwX_mpeLXDKUsaQwneIu7wX0nUviaJAUZ8RT4GYLnDlNXfUNK_d9Eg7oR5CnEn3_LfIpSm009adpceK9HOdMV63gvzUIaExvKSR-s0HPAbIPYDjbmUViiLAdtRar-WHafYl6mWk8hW80MnK9YZgkXqcQy2XUl64eBMninLFVzuCGoWgg1Z_mkl-3Yc9vjqJNKDushJvMF6i9CXuO4IctmoWxjdnGeeA6Tft0ebSXiYegnGJoc5KiEFXlMpHDm-dGyE2ErBlvE0je12tMQOWvBp3LOQMs5T1RtzpLC-d3eI8cNA1RY80sioYNTlLqdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=kPkF90a8g7vZMAl3yDAodS-LB_OqmuFEbJlLfhO62GtXxezbVAaBzqT3eaA4qpaC699r_HNsldxyCV5Qlc7rXPJtAvOXEkU-sn_8FMPsIAOBXHHx5GW51ZO2m4o-yZhWqqo09PWw37_WoKpId3n9V-vBII7T70jDl9Vdq42ZqkqdocGBrE_kqR6zySDqgXf5JgDKEAGHX4TSzJLXx7-oFZWOJ4bDbEbwJyV1GqohG-xNTRqnFrrzuPcLBgkoM6HnxWTpIl4JQA9WIv3astOENAiN0t6T_1-9nVncfNJCCrbTxHWSDG1sDY6eln90EE_MhGnToDgvc66BonnWomHv3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=kPkF90a8g7vZMAl3yDAodS-LB_OqmuFEbJlLfhO62GtXxezbVAaBzqT3eaA4qpaC699r_HNsldxyCV5Qlc7rXPJtAvOXEkU-sn_8FMPsIAOBXHHx5GW51ZO2m4o-yZhWqqo09PWw37_WoKpId3n9V-vBII7T70jDl9Vdq42ZqkqdocGBrE_kqR6zySDqgXf5JgDKEAGHX4TSzJLXx7-oFZWOJ4bDbEbwJyV1GqohG-xNTRqnFrrzuPcLBgkoM6HnxWTpIl4JQA9WIv3astOENAiN0t6T_1-9nVncfNJCCrbTxHWSDG1sDY6eln90EE_MhGnToDgvc66BonnWomHv3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=hgopdsKNLmDJ5A7Hc-IdGglzH9KL833mYHjj4uNWzNy-XL9zn4aPbcJUd0_A-OiEtryOdQTbvek-1mNJMD8Sx-NRT86jnAbASvKcwb-vZx-iYfe1X1UIPYV87TH60GXx18t5LsV210W5I_0YLPwGZOye_TjDstsq85HR8iQwFFzjfSgG_l9C80aO5v-N_8xICCwhWP6aSKiBSO0sX0sOjU4QYe76fX2Bb0ZTVPD2WBJWcU7w9vfJag-4DWBvR2pdqzTqHVo7eN3D5l3s_bGWdg_M-HxsY4BmrPnR2q8OPMkba4cPe78RpTRwDubxBL40MUMJn_SyNNdy3utLMi_Sdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=hgopdsKNLmDJ5A7Hc-IdGglzH9KL833mYHjj4uNWzNy-XL9zn4aPbcJUd0_A-OiEtryOdQTbvek-1mNJMD8Sx-NRT86jnAbASvKcwb-vZx-iYfe1X1UIPYV87TH60GXx18t5LsV210W5I_0YLPwGZOye_TjDstsq85HR8iQwFFzjfSgG_l9C80aO5v-N_8xICCwhWP6aSKiBSO0sX0sOjU4QYe76fX2Bb0ZTVPD2WBJWcU7w9vfJag-4DWBvR2pdqzTqHVo7eN3D5l3s_bGWdg_M-HxsY4BmrPnR2q8OPMkba4cPe78RpTRwDubxBL40MUMJn_SyNNdy3utLMi_Sdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZA4TcazxfQ-Pt9Cb9-iYKdeJC0EvgTB5Of1cOyBmK3ln298ez8uCgbezbT54LHbWdcDlUco--BIuksJEBfLaiFdeZtlfw5Tv3q2xwXQKwV-MWddJuajfEqlUxwXRaRzaymAPQgfNf5JmpdSxRWzzmEjfYpbe2Ngqrue-EeCKpe2FNTTKxv2AXtZIzbJ9LLlkn0p8U8rgKj6UjBEnY7aORtHVvhl81IdeNhvgN6LEhcglA4eRgdmgHpPZVSd_LzR-AWqwpCCDaww0K9BNV12BT4MGIp38YJY28Dkjr2XLyNuovlz0jV3nbYCnagwvG2ak2eKLVqgKL7EcNhYwffZbSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNsF7YY40s_KeVGbKrluqugN4Ru-VwJngo-MA7wtz1r7R8HH_pausBk3lb1EJVTZGKAK6Gcz6LlthEzXi9mE4Y9Ne4ONTeze7HQRYnFUns5sqvkA9G1W4ja7vNDf-GXDAtvsBKNN3cETCm-ej0DVvnbhwV-O_GFTXBkswzxwY_eD7i_Yzyq5QPeyXA_mpx1C-oFAB6RBkhlUmr96e5-Sk5wzW5RWIhEnGqfh5eaD1J5Hf6odNVNgHTRaakzh6QFAZXwI5qU6kZ6Rhw1tDE5VgnmaOqp7GZuDnBTmUoVeL4dMRGMxYTJcpqqyZH46PwW50cAS2R-2JffkCnFQXBdstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KElswo7rPxkWygE6_PXM-1TyIbUlrOSyOYNrt9rjqzoopDjF0F0HJ4mCqj4jlzKkzeiLYUkJKL_xqs-qhPP6hoF_2TfnwS-2yMykPhchyf3oZymDBQoSBthUVL2WWvUYK6n5eh7HvERJ52iJGfB4KV9F70wcbYq-_27blMNzbxCL2H7TLEH_B59Ipu-NWFbNwLTpAtqaeQAFGQkYLNnMEksCU6gd-gdxWAMiufMuFFOPnHM3Gtmj0aDR0a3WJ1Ez49D99c2NipIQcjce4AvXPMYdwxPtVLkuBJX8zdlSyJyshp0Waf7VVSjCNHrGqswMPPToizR_zLCDwDVDMb39EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=V1sGu5wBtxhF0sXtZZbNwPlWbx79u0NwSOP7waZy0corGp9Di0MeHN0Y3o_DAvxzXBU7FpY7s8vdLv8Ygzm-q8aIK72JGdUfmue92qbRKZ7jttQe4XxEVz-HL5L6XC3TH6r_zHKMzZiKlAkuE304sxpQvLtVIkcKXMGrJFlcUGoLuC8Q78yO-5dudogFT3ReVk2Z0mcxOCYg-hKWs5hZzJg9t3EtjcFdEcy3Dcbdvd05YlD5mCCGXhik4YGupsq8_ZGKah1y5QwQ-_H5TX9UHVyL5jablNX4YWktC7FIgRn1dGO2IjnHjaaTX6cb-Lf2Cm76lkXK9e2akUr4ddB3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=V1sGu5wBtxhF0sXtZZbNwPlWbx79u0NwSOP7waZy0corGp9Di0MeHN0Y3o_DAvxzXBU7FpY7s8vdLv8Ygzm-q8aIK72JGdUfmue92qbRKZ7jttQe4XxEVz-HL5L6XC3TH6r_zHKMzZiKlAkuE304sxpQvLtVIkcKXMGrJFlcUGoLuC8Q78yO-5dudogFT3ReVk2Z0mcxOCYg-hKWs5hZzJg9t3EtjcFdEcy3Dcbdvd05YlD5mCCGXhik4YGupsq8_ZGKah1y5QwQ-_H5TX9UHVyL5jablNX4YWktC7FIgRn1dGO2IjnHjaaTX6cb-Lf2Cm76lkXK9e2akUr4ddB3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=fugZcVl9tW_0vD7JBgcIMY75DdE4fPk2BGOCw4oZngwplpjpSmBDEVTpKlQ61RhhG8u78FxFogrmqMOIm2qL-T5C1uhxHTXXHyzIw_5Gx2YuamMKfrmUcL2LEgnoOUbcCx4D9MTdWj6OCUeIB_iDm8Sb3Ui7GcI2NptPqq1o_o6LmALGLC_Ho_n-qxx_lRB6m9098l0qDFIFshsACvny3V_KTuZuSTPEFqOuuu0BMMYDMRGdtP6Vn0-UtHBSEQULXh7VE1OqN-_SV5i2Ghpje_fJY2PzaYfVRRtjKyPLIWhflXPUzjUCUMxmNfGUGlCGadBmLhAFtNUjOFoIvDCWXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=fugZcVl9tW_0vD7JBgcIMY75DdE4fPk2BGOCw4oZngwplpjpSmBDEVTpKlQ61RhhG8u78FxFogrmqMOIm2qL-T5C1uhxHTXXHyzIw_5Gx2YuamMKfrmUcL2LEgnoOUbcCx4D9MTdWj6OCUeIB_iDm8Sb3Ui7GcI2NptPqq1o_o6LmALGLC_Ho_n-qxx_lRB6m9098l0qDFIFshsACvny3V_KTuZuSTPEFqOuuu0BMMYDMRGdtP6Vn0-UtHBSEQULXh7VE1OqN-_SV5i2Ghpje_fJY2PzaYfVRRtjKyPLIWhflXPUzjUCUMxmNfGUGlCGadBmLhAFtNUjOFoIvDCWXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vze5_dhoPbAW6d06EPDQXX2m5grmmXJiCIblODGtXj5KZsNRP3mCMJxXqx2iYmxgWpFYWUfMQLy4lKbVm_P7kk4bLT-pJCJFWMv7hNRq1UnrxldUugdTX4arnkkkF8wqha6i8kBLeiXKp0BGtw2EcD6hMj2naiOG9gJlsL3bgvvDJ0CWZN59rfhPcSYxw2K0m3QJql-ietxUIA-HuD9EHVNvgzJ-wJG92RjYYMQO1ZO7O1EQbM7BwvaH430oW0rMRvQTZhFss27CTmPpuPGkdEXG3liZ7YKWywNvdrEzhLNw5fYgxAPF4v8ELucIj9CWoXdVra1MOdytETppZBJzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=b-Uc4-4r1TuiMPSrYOKlVfJWnOl5maRz6qE0oC8azju9vRja-kf-RnpwLbrslHVDvtvgbtx3yn9oZI8ELhnsN-GJgyV8s6gmP6LcOn37a3AaJFW-M8Mvtka9rB6GRXMRmnlc2ezSVxoZOdGf_c9Srk3C_deHmSl0NQMydU8BCyr4VMZEoWoFogyDS9FCw_Huhr80kdW0-X_mJFq-1UxOoOcO-schkU1YxF1b6Q2YJz0Zsxpo5Mr0oFovX-VIs7pPus9DfHonDUPqo6-Q6p3TlSdQz-59dQrqyiHrCMyYjGVqfbly2IpXkI-11ejwAYmWmW_z5GFSszREJR2V-njnzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=b-Uc4-4r1TuiMPSrYOKlVfJWnOl5maRz6qE0oC8azju9vRja-kf-RnpwLbrslHVDvtvgbtx3yn9oZI8ELhnsN-GJgyV8s6gmP6LcOn37a3AaJFW-M8Mvtka9rB6GRXMRmnlc2ezSVxoZOdGf_c9Srk3C_deHmSl0NQMydU8BCyr4VMZEoWoFogyDS9FCw_Huhr80kdW0-X_mJFq-1UxOoOcO-schkU1YxF1b6Q2YJz0Zsxpo5Mr0oFovX-VIs7pPus9DfHonDUPqo6-Q6p3TlSdQz-59dQrqyiHrCMyYjGVqfbly2IpXkI-11ejwAYmWmW_z5GFSszREJR2V-njnzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkJpyEmhKQ0RtwrfYDPy0QiVFKrZtnVpYkAMq8MSFwK3hBYOB69unHITdywZItas_ogsuo1c6rwX9UpstD548UJvTAz73g8ISgfMYB_Vv-LO6Il9Fmj5cmoS7UQFYOYeLNOesV56hAu9Gi2qj607WsJqoHbi2_BKSb9ptVsy2dWIPh53Fx_lDb61HcaU6BHyDhququoYWA8LtyTODT3OJ6gQlXMnStnLtbQnJeqvLtuXND4AQQxDWNUkJx2GRyN-xPSaqKj-cYg_8fZOPTW8ZFbLj1TGb_x0rVRT61knYcETA3PbIJeJ-ni4x9wUo0BbGoj5ULzyqRw9IhzS_7NVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=lLLTmRF3lyBzoNgldTRMWlvKm88GIY79OTOqppNE9IAWH2ijcc8rSMBIiM9Beqgs-VD9gE-oZfGcpD1A1_3Kxo6kGYT5r1F20u8vmU1bOzFfrTXrD3YjvTOX3Xir5USZafyWJM6Xz7emPgbCZh-fon1qe88l_rmmT7qnw1A9ExKraEEULRK-cn7M22A0i5aeGrSsI72uPt3jxKTFbKPQhrSTDS1X2LvgX52Cqu_KtdEPxkJ2vBxu6MOl2PqxbXdK7ooEMpuFpXTZZG9D-CqgOWZ__K_6CtgtEYf7wu4IumEejSB6VC7YxUqExWVeAVIq0tPXLBQGoHZZ_EoIf3V5cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=lLLTmRF3lyBzoNgldTRMWlvKm88GIY79OTOqppNE9IAWH2ijcc8rSMBIiM9Beqgs-VD9gE-oZfGcpD1A1_3Kxo6kGYT5r1F20u8vmU1bOzFfrTXrD3YjvTOX3Xir5USZafyWJM6Xz7emPgbCZh-fon1qe88l_rmmT7qnw1A9ExKraEEULRK-cn7M22A0i5aeGrSsI72uPt3jxKTFbKPQhrSTDS1X2LvgX52Cqu_KtdEPxkJ2vBxu6MOl2PqxbXdK7ooEMpuFpXTZZG9D-CqgOWZ__K_6CtgtEYf7wu4IumEejSB6VC7YxUqExWVeAVIq0tPXLBQGoHZZ_EoIf3V5cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPE2hB0Wh5ZhdmHjFm94yXOC1Xs1irtLqQzSMoX91JLzCyZR-XO5odzHzN8Ihk1sG6om6fQ8N_l3ZgxyF7aCf0H1yEJvyr_fAm15Ec3p_xpEZzRPPPJd7b0R0JQ-qBB4zp9KoHaN_YsBiiFbr-D8lBKQJ3viy9a_Ui8g_jcGy8u8qnXBsQsbfAChxMDrLgRksfq8BJpjOmU0krE6NcdRl3-wu7VyctzF9pu6KYE1TEwsA7l9WnlX_6YStSEUuusVtkqNShpcG384tsk9EuhafxaKbPiKCi9AhCPfWdBJQjquVP877zfiCz5X8Warn5mrWXvxxb50Qqsc0vltNdktxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=tnuD8YjqeAtVRNDdh4ct8SRmPYXd9Qo7GY6V-0R4A4UQfUazpZaGBmTKzB1L7FAJrwqOuELl1QgrUXNgLf-rHwC-NbyhttpYDjGyvrreRKiSjcnQoQc2V_9615dXJzudL1JtZreirgyevoVd3hXlqJzjBgKWYT37LXG5nt9LYxU52aaLg0RfdO0j1HfTkwuR0rQdspR1pBl-tzgFohpxelysYIQVp0A6XLXPCphJPq22iBquqVMErSSJTA09sHK5dzRZofc_rpu91cUQr-imLFkAnqkhpV-KIc38oKBYQuxThaWQa5-isuVx7RZmhZ13cQ638NTss_Bh5zX6fDsBnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=tnuD8YjqeAtVRNDdh4ct8SRmPYXd9Qo7GY6V-0R4A4UQfUazpZaGBmTKzB1L7FAJrwqOuELl1QgrUXNgLf-rHwC-NbyhttpYDjGyvrreRKiSjcnQoQc2V_9615dXJzudL1JtZreirgyevoVd3hXlqJzjBgKWYT37LXG5nt9LYxU52aaLg0RfdO0j1HfTkwuR0rQdspR1pBl-tzgFohpxelysYIQVp0A6XLXPCphJPq22iBquqVMErSSJTA09sHK5dzRZofc_rpu91cUQr-imLFkAnqkhpV-KIc38oKBYQuxThaWQa5-isuVx7RZmhZ13cQ638NTss_Bh5zX6fDsBnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=WHOwJDS5hnLFiqEOByjwlo9_fLrAecY6hRN7JpCYXyadg-U45S2EutLXxTB8YkWM5fi-i97o-zNBJgYQiKknVoWkUGaElKgBe48qlqrQma3yPIoQJ-E8tuKaN6aZBUgiViwGpiRNe5Z0IJLa4xfzF9lILEVqAbabDGFJKJinUVv0cg9BOcdTS6QKhvHExrgVSfSNk-EqJDfYnbRjuCQWq8xsdk7wJp6vknvbH5keXZGQuNAc2nmxrI5WVfOC6vsDNO5Ahv0DF-vl9EE90hDwfOwgsk7SmOc3TBAY_JkaslZFO-QVsKPgcQF3xbmgYIyR0hijv-1CFjN0J6vUJkzxPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=WHOwJDS5hnLFiqEOByjwlo9_fLrAecY6hRN7JpCYXyadg-U45S2EutLXxTB8YkWM5fi-i97o-zNBJgYQiKknVoWkUGaElKgBe48qlqrQma3yPIoQJ-E8tuKaN6aZBUgiViwGpiRNe5Z0IJLa4xfzF9lILEVqAbabDGFJKJinUVv0cg9BOcdTS6QKhvHExrgVSfSNk-EqJDfYnbRjuCQWq8xsdk7wJp6vknvbH5keXZGQuNAc2nmxrI5WVfOC6vsDNO5Ahv0DF-vl9EE90hDwfOwgsk7SmOc3TBAY_JkaslZFO-QVsKPgcQF3xbmgYIyR0hijv-1CFjN0J6vUJkzxPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=pKdVDR--1gydOM9BVkHN-gmF5fp4trrXE1WXaRz8cMvHKPPGszM2YACblvqD3Iy_nHkxpj-7-8R9L_IZ8i07cfhu6mcU8k7ypp9XoDNDa66eFah2PVR3VCbk4FpddcsCpiUg78ix0nC6SMxUQb_AWq3vB0mZEWwg1lwoSUYcAws1cccb-0T9zkULyIO0ztj9YfUvXWSGEMDt0GdDiSKxi1tvvzJxExNaK7A9l9wvWAdy6aEueTQDgk2uRJX42UnoL3BMCl71qO64kMqUeEGZHziern5ONee6ZrSwtyh0LJnHcvdgQwFpK3X3aHL9NfH02Ivq4LJgqb1aAPLRk8oSxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=pKdVDR--1gydOM9BVkHN-gmF5fp4trrXE1WXaRz8cMvHKPPGszM2YACblvqD3Iy_nHkxpj-7-8R9L_IZ8i07cfhu6mcU8k7ypp9XoDNDa66eFah2PVR3VCbk4FpddcsCpiUg78ix0nC6SMxUQb_AWq3vB0mZEWwg1lwoSUYcAws1cccb-0T9zkULyIO0ztj9YfUvXWSGEMDt0GdDiSKxi1tvvzJxExNaK7A9l9wvWAdy6aEueTQDgk2uRJX42UnoL3BMCl71qO64kMqUeEGZHziern5ONee6ZrSwtyh0LJnHcvdgQwFpK3X3aHL9NfH02Ivq4LJgqb1aAPLRk8oSxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF_M8BLHrgSOkv2B08iqdnqX42shxhKsvD3kjpORbnwDeydT0TGhLGikYvRgBaQ1cvxGVSlG6NotQICfFZQTGQy5JlxcIMAiDsS1tweVgCg31N0IiXP5TcUZOoMhsKK9pCNLPvkklTZ1nddcWQjSA6OadYV7txZqEsraPpqvwUMn3FI4ADNUnrgRSYXPXRfKucy9AZhaevidWebYnVWDxycm_yeod7GJLk_2lNrhgqaLm322rvy1pp6-IRTAYTGnKXAYGL-0DImiH5do3g7aT7qlU0HQJ_UjOESG7gqSSUCWWdc4KJYRJNxdzPd5-8KpoCby3I48ODpNnyv9lkFv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImsrnmFcMEnAsmC_K2tclkox4nkXAMFh6Grnwm849j6NPiEvNFcb9dudWtpW2A1EpjZ8WdJRMSaZchsxCk8CB-jH4pu8EaXjvIROpGL5reNrM6r9Z7EEP8PygaLx_NsJzy8y8fh-1gywkl6Kf7ViAH5sO4QbrMRgzLGUnNH6_T7ZJLefNYkTYTvl2CFdR-qNroY-lw2VVw1bnqeSGmo7bBiRN0KrSWWOvmIiAs-cLqwIzV9AaBu9FlnSVdD42Bg8ahTeVFsShgGl5p0pI4ImKuNAVKw_WXTPEPHvxahnqFxqk-dCBN0BAZ-_IY2DnbD0PRF2NQ7f7iImR5fgSGHckg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys-xZcx1Z6KrlLkm3K5YRJ_PlXa7j5miiNcoOtwbQL5QoLlhRFJGX7S8cXVe5u8HVa9a7Be8Dp8YwQJj-PuBd2JuWwYwcVBgTrTSZ2lZnvaR0eqVH4j44RcNN-gjh2tMY4tafmiLRHZ9_Ket-OacqHIJzmrf1a97KJnSmhsFWwt_lay4_QbzTnRrrKqUnw-hFof-yJ6wnixriIXseGAM7FXa1CA6M5_SHiy8mAKjaS6c_GwM_-T3oOZrZmZ3kmGO2rAcBQiLd2HqmXFvfFqrBehWEVjAV3wTjZ4gNMQiFVy70tjsz20SyQwICAZVbC9dHGvns-7fwDdfJGl1FXKw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=QIwHRxSzbCpTQU8UfnVP4RpAqOCYm5bSTmX6q47RNDGW_J8XpwUDEbo1WP6FEYRSm3ggLeQnD4HS8Wq0aNq4Xmd36GJMcJiHDNSd10yiHNCz5tJUbkQy3R5XpEvu3764RO-LRXZfSWpMMenUVJy4cEldY5OwvzZrmmzH5rFxKyOPwLKU9RU70rxaWSEXx-t4gPXGMnL7WZoKXsmZJMNeWcpBSOpc4Csuv-mqy_K0midRqheXzOKgzDUANegEvV4oXT1oNBarhv45S4C8Na_gpmmdNb2em4MPJbjq2rwM1SGTafkkEBm2SZbX9VjaxPMZQtb7c6zqoF9WZrL9wCElKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=QIwHRxSzbCpTQU8UfnVP4RpAqOCYm5bSTmX6q47RNDGW_J8XpwUDEbo1WP6FEYRSm3ggLeQnD4HS8Wq0aNq4Xmd36GJMcJiHDNSd10yiHNCz5tJUbkQy3R5XpEvu3764RO-LRXZfSWpMMenUVJy4cEldY5OwvzZrmmzH5rFxKyOPwLKU9RU70rxaWSEXx-t4gPXGMnL7WZoKXsmZJMNeWcpBSOpc4Csuv-mqy_K0midRqheXzOKgzDUANegEvV4oXT1oNBarhv45S4C8Na_gpmmdNb2em4MPJbjq2rwM1SGTafkkEBm2SZbX9VjaxPMZQtb7c6zqoF9WZrL9wCElKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HmbRB4XH5bQftpAt4VvN0cZUOtqjHZVYY5U3EdNj-0mU7gZuTfkCUnecAnJ4fhPwpyzHBeGgB9zZdyI1F6T1XgLroJZcO7jEJy5b9lxqVIBzqimoSfeCaNJS7yN2Pa4WKCycIWZAO3e6diBw5TpfjJv4WrG2Jgk8eCnH__dospuI1Qf8lfiNpN8Py9Q4Xb_M0g6cQNASRVrk3i1LmUH3ijJGWausQm4xS8bhf6FdMjpEuMCKvSzkMksqDBwozmYsycmym1FsNt94p_14wJMqtlIP_yrx8q3vYx9k48hWerCdGcFwqnDDrxEM1Yj2zaBxW2ibnctSxMbglZQOd3bWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=pPXw20xbInkVSSxsP_T1M40nlfELsP5zmGh8ZShHjjoIL-fU3fBCk6-CfwyJmZdHjAClGLNe4AYlnUlqnGsXrHS_4WlAo0JaZytIGrIpLu50WDfkKZyovoFTjJmBpkhdvuwXpvgUv4CsbU5ujrGBYO7A5xWLFWQANXhw9zext9Lt_EGvcJsyol6ryQn1zgz2-8V3PRI2kICXtrGlJ4DmPEs39VDU4XNuARTzwxxip3AB0h0dr2ml2dpyr3K6tRYFefC5yUvT7RkS34u41ov-oGs83CVlURwYZHz25Pixr-8g4sjmUKik2sZoUSpk80B0-LOsVgNuW-Ym8XYM3f4azQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=pPXw20xbInkVSSxsP_T1M40nlfELsP5zmGh8ZShHjjoIL-fU3fBCk6-CfwyJmZdHjAClGLNe4AYlnUlqnGsXrHS_4WlAo0JaZytIGrIpLu50WDfkKZyovoFTjJmBpkhdvuwXpvgUv4CsbU5ujrGBYO7A5xWLFWQANXhw9zext9Lt_EGvcJsyol6ryQn1zgz2-8V3PRI2kICXtrGlJ4DmPEs39VDU4XNuARTzwxxip3AB0h0dr2ml2dpyr3K6tRYFefC5yUvT7RkS34u41ov-oGs83CVlURwYZHz25Pixr-8g4sjmUKik2sZoUSpk80B0-LOsVgNuW-Ym8XYM3f4azQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VK8P8Z2bLw-GtHYczIGdL2I4rw4NHcYK8-3UuJbU4pl60e_0JQ6cUElhEdplpQKl8w7AVJNH56SmLLY-38UeG4sMsF0DSn4A5ztxx5DKXcezBT1qSJAuyDKde2PE_wO04rdthaG-h2TcoalfjMPN6kOGzxCopJtOUZsrVVA4qikuhV_l0ZMPZpHggnn8oysq3RM0yYJraJIFvN0IzfpCd_gWAUZ54nMJgJVRn1_p35lWhfQI3b9-ArEhgHQWXs0yZchEqPnlaRLNjDchP6vVnXYdCZJof90CHIEmmC4pOy6gQ5LZN5tdTazpTDk-VZXffHFubLjh2h3ZNmqPS5q_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=hTLj3-0lxmUC1QpB6MTrX7sXE5NKUjImdQLlcFHGPCjNCrBhlp27pz2VO32x6fyiuzhkFYAKAMT5W0SNj32ar8Gr88r7EqIrdu6-1PHvuotZeUmQd82ar9GvDztPLXq60wSxLC0QqiLRZ3aifsWVz82Ovg9kPdYd_C70sZHxbzx3QGioL0vfOAbhGWbpYtToSr8cLaoPxF0IwTt1mRuvYnkvhi0mLSFs57RQMcAbBvr-8hTsmSvWWFEspkVwDQ0YFxIuwcvnediGQp1lSTLO9mqh8ZVQDaijolu9u1KeQWH1dQrFMmK3FqVcbReknFGdp4FH7U3UAmRvtdd8qj3UNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=hTLj3-0lxmUC1QpB6MTrX7sXE5NKUjImdQLlcFHGPCjNCrBhlp27pz2VO32x6fyiuzhkFYAKAMT5W0SNj32ar8Gr88r7EqIrdu6-1PHvuotZeUmQd82ar9GvDztPLXq60wSxLC0QqiLRZ3aifsWVz82Ovg9kPdYd_C70sZHxbzx3QGioL0vfOAbhGWbpYtToSr8cLaoPxF0IwTt1mRuvYnkvhi0mLSFs57RQMcAbBvr-8hTsmSvWWFEspkVwDQ0YFxIuwcvnediGQp1lSTLO9mqh8ZVQDaijolu9u1KeQWH1dQrFMmK3FqVcbReknFGdp4FH7U3UAmRvtdd8qj3UNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz8EHBmRx6KlJmqf-4cdQOpFo10gmnMal8Ii_zpS1JTSnURX4l5cxWvCar_MHBwcKOvx-zvQuVhs1PxVB5YEYj1ojm3P7X9YQ94P1j-qnN9r3DmkBocfrxRZjHcGo4odasMRQM0Yu794u78NMMz7mIEcYDQW32zP_z5u3QTmGU3uSuZjDdvFf3GBnJSr58QuqhNocfJyHnq1yPsyGkXirW0vBDYfOk4skw8_lgVUHX4ijF5dZw2ssEJCMDh4YLeL9oBPL5sfxa8j4Xh8OpB78fZt5v4UXODL33ZYeumqm5ovR7ZgNN-QnHHYHB6pSJITO7_Dbe_Trg0DKiN1rABkuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1qvl8P8tulGIM8p2fSlmrs1IqN1TV7aebnnozLsAqNiOG9atAALlEwuzyNFFjEyJVTLnn6pJASBnx7AK67aK6x65zkTmB9fr8hC4HAPlqb7vg0leVBNMJOS7DlwrbCYADpgEOCdeMWTlEXpfgydIdObkujgFZxtv4ustjwVD_oQnmd7bPLs8ncaMkMfGYYkcoiPO9HIOr1U_EfJljUj6nQvCL1P9gbwjn8tszT8nBno-2AoHkFJiKZ_t3DACyR5jDYZPxPXNIeKNTs-lvUCkrTsqp2fSFHtW20d_Ch8qn5XhvV7JwbzW2G5uVqAwSVN0DnAPXfi8XgKhjHS6hLSbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJiXVcF0ov62o3q0ddl5g6_v9JilQifofMzxaedujJxOP0WTNWydCeHmbdU1_P9s4sPkF2Amatj2lIOa0jw7v6jWEJo4mrBkakXqRmZWVOeR77twD8ls7xzy6vr-sjH7F8QW966GysRapKpxscGXhY5Q0TKoCEABuiQcg4FNKBh7k9VaKyjFnzPF-nWifr4PSTQeod0kkmHp8oWn6dIBnj8Ad1twxW109N2eq2gBUoUR0tXeTZpPABjBdmprYoBtgewglave-tCklZe-yMieuIwSywl8WbEFe7-1vx-W5mc0qX1WwM0qvpmFAqlCL9EbRW_u-AcEBV1OrnHSfsp-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7WFmmhxXfGZPl38tNFsYH84TzWWH5ErqsQG_4OMJ29GSQzGkSXlMxUV1ynkafqbEAiKLXT8IbdZE3dCGp7WFUeV0Qfa_jAS7kxaLgGGNmXyL9aEUKoHF9FF7HXWer1mVkTh04mADqk4F04hG7IdDZaWF4Y8xKoCQujiRvjDoJZSQeR_NYfcgwmI6-5XjF1C_cmgi6rJASt7Uz1NJhCEEpeHAVKWIR_4PwD_b2A_i8Bf3epBTnkWBiOyFTx6RKcbtWP2abY6kCaPo6lI_BZ0gY_eB40IwMXMjKVpJegjDl1ZPf3m9CMP1az8-89j9fgGR8UhBvNnfQyMXICj9KNovA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyiBoKeTyKA2yZz_TUd9QVnQ-OW7QJzceRp77Ybi7cQVEZsRJO4W-SXieKmBHhIwyMILGMhcZoQPXKLCEu5y_GULUkXUdkYk3lNAlbdzAmnf0l_9nK1rj5sLrO0cBqL3BTrJtJE_-1qdLhZilmniu7U4OTlAS7NUCj8m0lv2kXfGj0eAjuw2i0NZy4UydxmbLkw_J6Dm6rhRg1NAnWgHh63th_7iF0a6nXE5rQRxigH4wSeg-nPBclfbxaIqw5R7DQftojIfFEY7Xsj5MbYLr5uTwq-ZTxBSSiubRRdH49ZuVTVhxuJaBw3QIAmn5s0gSDiOc70cRayK5oFZ-j7aaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=Doxu3NZM2WuRUC9gxGe07As-fBlKmtIdEkuu6hSKenQA15Oq9J_7KI-tZ3WcMO-nx2n7oNrVKnV3xNyM82tK1bu_MNgHTMjAWSfCIKfBNzWSX9l1vO_nrUuyg4MgwLfb78UaTpxrCatjaIpy2fEnmSCc7GkFPTyyDB9pZNgIoJV_DjIPGyrJClEqpcQI3nfyBdwKTqbU03dNTV57VM_ri7j3f2G0naHYb_Vz4VJpsnMjBHjKkbbZXY2r3eMBVV0ovPnVD5-V_SEihBG4EHErOtHcDi1XceFrGRsoZ5W4aeVXd-DqlyVelcsZ-oiRCUOVLtRAAx5Pr8iQUb05YDdcbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=Doxu3NZM2WuRUC9gxGe07As-fBlKmtIdEkuu6hSKenQA15Oq9J_7KI-tZ3WcMO-nx2n7oNrVKnV3xNyM82tK1bu_MNgHTMjAWSfCIKfBNzWSX9l1vO_nrUuyg4MgwLfb78UaTpxrCatjaIpy2fEnmSCc7GkFPTyyDB9pZNgIoJV_DjIPGyrJClEqpcQI3nfyBdwKTqbU03dNTV57VM_ri7j3f2G0naHYb_Vz4VJpsnMjBHjKkbbZXY2r3eMBVV0ovPnVD5-V_SEihBG4EHErOtHcDi1XceFrGRsoZ5W4aeVXd-DqlyVelcsZ-oiRCUOVLtRAAx5Pr8iQUb05YDdcbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=evs5N3mtnvBSAMk4Ttbw8KZS90tU4tDofSsG4L1RNEYghbGOpsJ6QPwJTq5reYGAcP8-nrYanj5hxqfjfY6KWugczbS2iY1pS8cF68EO2Zl3OE7_DxNMx7SHAcwbj7RmbDqLGUnmyaGuR6zox3YnO0aSMZ4-rhs2LnS8VxUwhNnqD9DGJI0-Lu79TJd7FTplWHliL_8rkrjSZs3rLtDUd81494H9X3u1FaPEcd1I-LXjGWJDghe6P9JzyHphKP5ppuU_AMlD9nBXx6FiI7hzBlf3g8N58zGAMfiEhMIbZb2BVnCq6C7JM6IeRJ601kXSERH1v9vip07SMDobyDgWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=evs5N3mtnvBSAMk4Ttbw8KZS90tU4tDofSsG4L1RNEYghbGOpsJ6QPwJTq5reYGAcP8-nrYanj5hxqfjfY6KWugczbS2iY1pS8cF68EO2Zl3OE7_DxNMx7SHAcwbj7RmbDqLGUnmyaGuR6zox3YnO0aSMZ4-rhs2LnS8VxUwhNnqD9DGJI0-Lu79TJd7FTplWHliL_8rkrjSZs3rLtDUd81494H9X3u1FaPEcd1I-LXjGWJDghe6P9JzyHphKP5ppuU_AMlD9nBXx6FiI7hzBlf3g8N58zGAMfiEhMIbZb2BVnCq6C7JM6IeRJ601kXSERH1v9vip07SMDobyDgWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=sGWTB8id9hhqHVUP1C3v8GQcNFp8UuOKr0AqbnOgy9EmeOZDevCG0Cu15iHAOoUFKewPvpocvC7XPubL43vyUPKRBYBYsPdwQ3bcs7U_8GPTCG2z_kKgxCF44ZaPwAsZLAVieXbZfvkF10Zt-9YDLpw4H5Nc-RidobZdTPe-1HD0py3u7t4D-Zh5rJtWieW13Bvcuk71PEJFn3TUqX5brDBWqFxvIHSBou5qwmpUI_ksQRNai696CajvTG9g52M8w_LchonI-E0RuGswfLGD8xma5CBcwFigZyN3c2uTwRee8q8W4Z4fELCjMOTNHzYd7vVP6a-H8qyn0-NZuPgtAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=sGWTB8id9hhqHVUP1C3v8GQcNFp8UuOKr0AqbnOgy9EmeOZDevCG0Cu15iHAOoUFKewPvpocvC7XPubL43vyUPKRBYBYsPdwQ3bcs7U_8GPTCG2z_kKgxCF44ZaPwAsZLAVieXbZfvkF10Zt-9YDLpw4H5Nc-RidobZdTPe-1HD0py3u7t4D-Zh5rJtWieW13Bvcuk71PEJFn3TUqX5brDBWqFxvIHSBou5qwmpUI_ksQRNai696CajvTG9g52M8w_LchonI-E0RuGswfLGD8xma5CBcwFigZyN3c2uTwRee8q8W4Z4fELCjMOTNHzYd7vVP6a-H8qyn0-NZuPgtAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqIea2ubQW-K7qc5ZAK94JCjQxtBDLt-3jlOR5NTsupdcPMuoHLcLaRfvSZQ4NpgyTKXak6x0WmyXQ1YaYw2Rr-BCtKbFrqGCFA3rvjmPhRN0jRVP2N0_hh0gWBlW68zhfRcMFKg25Ef398jgO2p4CDQk-EmJQr7MycDS1UhGyCHZEEGz-AwhfQOYHRW_375lLRvkIHcuwjxo-RDTPVfqnt5a9P_eqVg4p2FZ8j_gbKM8412FfqbLgE5nkyxsFSAOJQ9DBFWiNxS_rdlLU9qJtQPDfcbJY0dlj1-OFocEPHLtOb2FhSN2Opx7k3npE0rDlTC21JRRtUBU4taL0i2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJC3HMKAD7pjSTo5Qe_TRbtUDsClDJoGpNCcNdmySlK5PFsbs2_tyWYaxtkpUZEjmu_wqt3c-JPHSzKW9TcUry_QeCW-g1Ek-b7aMWFx0UyVqlQs2UjV9HuuPHEFkYL1h1NCnceHETDiwBmk2DBJoQrHCGNBHaw7oUuPupeQaOqvT0dY4m6vrUNy9sq52Wp1T6LnPZ7_rXEz07j--E0r_546IoOMeIUlgY7WenT1fDa0fJ_KGNgyZbem4RMO2PiIPa4gIrUpZRrtXDNiX-k7SRKm5Hb4DVTfHYaZslXuKAQKcKwVf3Wf30PrZWAMrzFYlZw0eJcoUn8hf7t5U8XI8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EevcTaKu-2_W6lNWsmSD5_LCo2egkoolHgFWca7-w1RiWTKum6DP50U2xUld8nTlJRZvkqBNjJ78b1yWLJaiV1ghGNJf6MscHwxkpPpOXO1qgm2Y5VVgnAFLpfPvpKbZlkYbJNnDhQXVJEOV_hFpCt_pCRHUxLYQPPNJpQqVvmh__bFwlGItzME-1ni3uNE7zRO8wG98glF0dwtf7MsKp24kubI4XjDCh8sCBcOnmzvlXpMxdL0aQWG-FPKzs1giJQvcJefNRxl5UKFdlLMlUnLKZuneBTDwFcJ2-w_GQXjbgMSrovjsI-Uv2I1IUiMzWcnAFUFGZQcLiWrXy1bgMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Wp22zPTF765P19DxDAXGUB9u6vljh7DQXAp63Nt_JbuD6usrhQXveQcTAbIPUptBslKXoQo6snxcJPoc4TQGrctRF6sc6oLP7I5_Ti0Yk2LT3q6OXcDGNLLGpgu9bndRhv3DzuGk9JZNqy5slLbxeGTKONNfUNUCoTMRUYBFWMS81zgTWQSFB6g4Em4bX5ROoGU3GzZ3BcHk0nWZAysdA9CuabClmGt8VVAiSsxRx1oJDnKgEiZ2OeIXr0laPyKGKHptRSNBipaaHgNTNc0RMQbSso6TdWiyH4YM3sG2z5nAfOr8Qmmtnf8SbeQ8mH0-7yfgDvjrFRQM0NagYSy9JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Wp22zPTF765P19DxDAXGUB9u6vljh7DQXAp63Nt_JbuD6usrhQXveQcTAbIPUptBslKXoQo6snxcJPoc4TQGrctRF6sc6oLP7I5_Ti0Yk2LT3q6OXcDGNLLGpgu9bndRhv3DzuGk9JZNqy5slLbxeGTKONNfUNUCoTMRUYBFWMS81zgTWQSFB6g4Em4bX5ROoGU3GzZ3BcHk0nWZAysdA9CuabClmGt8VVAiSsxRx1oJDnKgEiZ2OeIXr0laPyKGKHptRSNBipaaHgNTNc0RMQbSso6TdWiyH4YM3sG2z5nAfOr8Qmmtnf8SbeQ8mH0-7yfgDvjrFRQM0NagYSy9JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=cNkOn6oWziNIPJ0tjI4-TN9t4_8UgbAfjBqybq-zABuDuAuVVlID7-8cGG1_Yphs0kL0TFtgO98RG5aFw9Uur-Em6oCV7vnI77B4qlbDF8dZIEL-ienUelzP8AfJmS5hGe99r7_x2TAd5ngFfQsBDeowQQ5V8Oz3IaQ4YpmrCq9vbh0fRkLJ-QVoSCtVkV7XTOIJSBqROerGTv0Rw9yr5-o8rdTX2L_UmAIJvmIeyapPLE_RF3ZvclYxnTRhOSy_9NDKt1qbUtSNNVsZdGai60jgkTGA2iiksL12VWR_QhOqO_tuSHS89Dua1sL2IaaBDiTwOHeKnlQS6IKMC96Ymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=cNkOn6oWziNIPJ0tjI4-TN9t4_8UgbAfjBqybq-zABuDuAuVVlID7-8cGG1_Yphs0kL0TFtgO98RG5aFw9Uur-Em6oCV7vnI77B4qlbDF8dZIEL-ienUelzP8AfJmS5hGe99r7_x2TAd5ngFfQsBDeowQQ5V8Oz3IaQ4YpmrCq9vbh0fRkLJ-QVoSCtVkV7XTOIJSBqROerGTv0Rw9yr5-o8rdTX2L_UmAIJvmIeyapPLE_RF3ZvclYxnTRhOSy_9NDKt1qbUtSNNVsZdGai60jgkTGA2iiksL12VWR_QhOqO_tuSHS89Dua1sL2IaaBDiTwOHeKnlQS6IKMC96Ymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=lD-6DwY4ELZcFxvZGxZfL20lQhyuyD4yEf8FJSN5hUl6mBo3MRvWetDMvXvyQuOt9KIgthL55KqvslLR3hkuEZagZL43LTljc19EUmJwLl9TBB78r8gv-YZobOB3qrr4D1NH3hByP0qZOeFY_Dwia8NQJ2gZy7X7v6Ezr6-WY1-qPcq6cUoXWhwvq6Qb_5uhNo4PeaJaSYvsubCD_xQS_czCjy8nlVg6Q0lA5v4N3-Cj6cokgAkLlvQnRp4A0KiusV17Cqm_ZLo0GJolOXH65u-RmeohxkEJ6PtJO-1rQfr6orIlpSY4jqYnWmDrVpEI_hBuWYwUie1b2yjlTDvMbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=lD-6DwY4ELZcFxvZGxZfL20lQhyuyD4yEf8FJSN5hUl6mBo3MRvWetDMvXvyQuOt9KIgthL55KqvslLR3hkuEZagZL43LTljc19EUmJwLl9TBB78r8gv-YZobOB3qrr4D1NH3hByP0qZOeFY_Dwia8NQJ2gZy7X7v6Ezr6-WY1-qPcq6cUoXWhwvq6Qb_5uhNo4PeaJaSYvsubCD_xQS_czCjy8nlVg6Q0lA5v4N3-Cj6cokgAkLlvQnRp4A0KiusV17Cqm_ZLo0GJolOXH65u-RmeohxkEJ6PtJO-1rQfr6orIlpSY4jqYnWmDrVpEI_hBuWYwUie1b2yjlTDvMbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=PX-a7Z1CAFJ3KX_ghYDVSmPf1xXBnlNpqsxPKU-ztaazmBR8JO6meJ72EZtMDSRI1y1_cdeOi5Sxp-QpHDlhZqVs0Y8LoOUZ924uiyEnz29GisnQe1-e2LS5wbhOGFgqeuM8fOQtj3cetgCZxkP3sYsvcEp-lnGrjjDjVyM3rWhKXp3ZGjNrOU3bYS--5M2lWi3-mX0zOSCS_4r5BYPP61V9FjcEhJ0vOLq_lEgDf3HCLR-xat7oMt6i1CemoPQv9kntGirdFgeU_sfBbtL4D5WQFuMQTavpEYEUHC7lGUZwozjrQPSH4kCuWScIL-xR_g5_h0pht6ng0TIMd2QTpaSgO0P76YneGZ7nBTdKHFcIeNwvm5AYo0-yw5l9P_FwOQymBtN5pofBt-mwH0l9M8_5sMEWgLCdv9Oh2NbkXEUxHHUWbRTX_y_A3Pd06QaLjSpCdqb57YbQugfr_QTnM-aYF9zIr0JE_GrRkC1Yeq4wgkraYQays3yKv3G8Roa_A0ixYGsR5fjdIh7pTox4SZKmO2WKUUufHuwuTwZ_usQH5P41oRfcsy8IcZBUYYbHSGMerbwMY6N4j1x84zIISqxKZvrzc9xfDtYSsjsD1fnRCEoyHJ3zse7PjuJ7A5ABJVkvyn0k_Fb_JWCq5oE6zgymaHiV5iw8uTe9t_tgjUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=PX-a7Z1CAFJ3KX_ghYDVSmPf1xXBnlNpqsxPKU-ztaazmBR8JO6meJ72EZtMDSRI1y1_cdeOi5Sxp-QpHDlhZqVs0Y8LoOUZ924uiyEnz29GisnQe1-e2LS5wbhOGFgqeuM8fOQtj3cetgCZxkP3sYsvcEp-lnGrjjDjVyM3rWhKXp3ZGjNrOU3bYS--5M2lWi3-mX0zOSCS_4r5BYPP61V9FjcEhJ0vOLq_lEgDf3HCLR-xat7oMt6i1CemoPQv9kntGirdFgeU_sfBbtL4D5WQFuMQTavpEYEUHC7lGUZwozjrQPSH4kCuWScIL-xR_g5_h0pht6ng0TIMd2QTpaSgO0P76YneGZ7nBTdKHFcIeNwvm5AYo0-yw5l9P_FwOQymBtN5pofBt-mwH0l9M8_5sMEWgLCdv9Oh2NbkXEUxHHUWbRTX_y_A3Pd06QaLjSpCdqb57YbQugfr_QTnM-aYF9zIr0JE_GrRkC1Yeq4wgkraYQays3yKv3G8Roa_A0ixYGsR5fjdIh7pTox4SZKmO2WKUUufHuwuTwZ_usQH5P41oRfcsy8IcZBUYYbHSGMerbwMY6N4j1x84zIISqxKZvrzc9xfDtYSsjsD1fnRCEoyHJ3zse7PjuJ7A5ABJVkvyn0k_Fb_JWCq5oE6zgymaHiV5iw8uTe9t_tgjUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=e3A91x-nEU7-q_pLJbRONLj0o_2JqoC6jLLLf0ATKgKRYRi6q-LHbtDNHhPf7Cu_NGY9XswtdVw1g92Cl8WLobCUF5y1KFFuFIacpb351GNdiv_fObZAwiWkSSsrdBeOfJu-RBPvubmRFQTethn0zMeSR69AFlwv5GQTwPgzFDLD3BNlgqU4EAotmBP2iUkdWpKepRSMp25MFm6DNBrmFa7AwvutZjFwH8Rd2wYJ1RdmGReQwBpoFEr8-LgdSFGgImZFjDmdMdISsAC9XZPWoN76ySvOHV4l32_lffWYamk_K5rmDJ3iOx4F5XvA-ZwtWqpKK4jFPXPrsjWz0xWQmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=e3A91x-nEU7-q_pLJbRONLj0o_2JqoC6jLLLf0ATKgKRYRi6q-LHbtDNHhPf7Cu_NGY9XswtdVw1g92Cl8WLobCUF5y1KFFuFIacpb351GNdiv_fObZAwiWkSSsrdBeOfJu-RBPvubmRFQTethn0zMeSR69AFlwv5GQTwPgzFDLD3BNlgqU4EAotmBP2iUkdWpKepRSMp25MFm6DNBrmFa7AwvutZjFwH8Rd2wYJ1RdmGReQwBpoFEr8-LgdSFGgImZFjDmdMdISsAC9XZPWoN76ySvOHV4l32_lffWYamk_K5rmDJ3iOx4F5XvA-ZwtWqpKK4jFPXPrsjWz0xWQmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=ghbE6wWfFobGM4ll2yPVy8gvRwoQfxQSoxpq1i72iCAqu-evf2JjWpdmyFfIiuXS1ZeOfN9Cvp3LaumCW_0FXrgvR0lMjduSbjquC-CGmEfEDymLE_34Y_JUyASS7bl_AfFtJ9_0GH2PqvCR9FZSaiqqz653fR6rLzkdlgzfxMvj9YNh_TLepxOe7CMQ0dcay5WAlUsAPn6806QUf-tE78yS-6COlPJHVoZPQWkFWAJfUZsjymkP8p1ZFkD5x6fXfT0p-E7RjUpCrBevkP82e0yJsF84nVqv5glzC2ojxie4uGivpCvR_6cWrUwXrahBzXOTft1jePCuf4IhUR9v1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=ghbE6wWfFobGM4ll2yPVy8gvRwoQfxQSoxpq1i72iCAqu-evf2JjWpdmyFfIiuXS1ZeOfN9Cvp3LaumCW_0FXrgvR0lMjduSbjquC-CGmEfEDymLE_34Y_JUyASS7bl_AfFtJ9_0GH2PqvCR9FZSaiqqz653fR6rLzkdlgzfxMvj9YNh_TLepxOe7CMQ0dcay5WAlUsAPn6806QUf-tE78yS-6COlPJHVoZPQWkFWAJfUZsjymkP8p1ZFkD5x6fXfT0p-E7RjUpCrBevkP82e0yJsF84nVqv5glzC2ojxie4uGivpCvR_6cWrUwXrahBzXOTft1jePCuf4IhUR9v1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMQzgUspftqjwO_01WJ6aCsxmVe1PjBzdf9KEGL6MiOY4sL_6sZYSqqsURO5bJWjdMDZuMoYfr7D5C17y2a2G4nnI1830whPpizCNr9kMYcVEUmwuDkNa1Kk92Jf8wMNG42LXwF6viK25S7Ab11OF4EfLPzC3-mjWgLbXlM1-8abmKt7SVVCw8-W3ZKtkMRQZsXofC94EOgwwnEThBDcNATcDwxOlSCllxEFpOZOqFCnBE-feqwze6bAhUYh9cliPDKCSBwl3HgKbAOkqbXrJT3GXf54BHXJQgvnwwRZn9ONTvIBDeLl5_w6cQLoABr7jk3RriCoKFUerLFEQE3CvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeVZN_Bqctk-WGjdkFTjU6fZHflW2hDnlLqUV47zsUS_-aOU8uEIAlUCDeQNBAHmjGcoRq9RAQbSjZoaOc3-cfYF215QMvt0g0Y7vW6PgdmUXMAHoA-lpT7v3c3LLc7iMc-bIgwUvZPE7W-u2nQ4Dx71cgRSzxQnNZZKYrjcZEV7hXjHQ1sbEnmWzaOT6dY7Wk46h3Qyx2TARDdDViFpcntrSuLO0R0Kly4IX3PFDUN9EM6ZagYGHNMxysRD2mFd8GZ6sWd9aVh7ckH2CU_ZpRTx7zzDAbNox9ot3ySA15ovn59rWdwKnTHYL-m2K17Nnv90oUKIEYq3AdwnRgVTgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=YztgawJw4Ol0JI7IEpWlaVYMwvd2IdRu39fAUobiCyT6GJp-mf1cJPRY-cNUIAOJ8tkqmxGCWBc4oX3DMpuN6XReEGk2MXmJ43jMDDvJP_jICWAtrREYGDVSFjHgEqO72cGk-8hi7TqK5FKQEPLwrg9v5AGy2b0Wk4SnCNPLASvZdBVvAOcJQ-xePjxXG2UT7SmlDJyfmBt6APLyMFphoh4P1wH4MDHlKJCuSoJJXWtY8OI0P4Duw7t9Ut4oNBDKT7V7sfEPXt6_SBscL5Wpyney2v4wDCj88TncFFnzzSbr8tmCsUBf6Ylff-KIpG38NeK1K7e5JlZbESHWp2dQkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=YztgawJw4Ol0JI7IEpWlaVYMwvd2IdRu39fAUobiCyT6GJp-mf1cJPRY-cNUIAOJ8tkqmxGCWBc4oX3DMpuN6XReEGk2MXmJ43jMDDvJP_jICWAtrREYGDVSFjHgEqO72cGk-8hi7TqK5FKQEPLwrg9v5AGy2b0Wk4SnCNPLASvZdBVvAOcJQ-xePjxXG2UT7SmlDJyfmBt6APLyMFphoh4P1wH4MDHlKJCuSoJJXWtY8OI0P4Duw7t9Ut4oNBDKT7V7sfEPXt6_SBscL5Wpyney2v4wDCj88TncFFnzzSbr8tmCsUBf6Ylff-KIpG38NeK1K7e5JlZbESHWp2dQkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=aWWrB8EnSBVez0vxbbpfgj6Qf3SYJ3lRucv6tUzdw00foblZZLMZ3gUC-_jtyFTJJizS9Le5PRrXXtdm_uYLyZcYmzJplRnCUmvMaOCMJqRjStg-OPEp5rlzukv4y7Zp4vD4R_1V73OLHd2YA8Yqpg9Z8_KYdDM0uDFYfwgDsOnDDKb1n1iQ0KtCXTAMPbprCkoSSCQjIAiH8yY52TItrjaGMeSGeThQtkYVorU5QlqcAuWIKRUBkxeJG8o4YfMWGHSlKsmblw4WnYqeb1ovTIKOi4QahtL0_m7MZxHfk-0mljGgPqP4LmtzDsJxmFcWWMZzl9dT-fPm2v5CHXUadQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=aWWrB8EnSBVez0vxbbpfgj6Qf3SYJ3lRucv6tUzdw00foblZZLMZ3gUC-_jtyFTJJizS9Le5PRrXXtdm_uYLyZcYmzJplRnCUmvMaOCMJqRjStg-OPEp5rlzukv4y7Zp4vD4R_1V73OLHd2YA8Yqpg9Z8_KYdDM0uDFYfwgDsOnDDKb1n1iQ0KtCXTAMPbprCkoSSCQjIAiH8yY52TItrjaGMeSGeThQtkYVorU5QlqcAuWIKRUBkxeJG8o4YfMWGHSlKsmblw4WnYqeb1ovTIKOi4QahtL0_m7MZxHfk-0mljGgPqP4LmtzDsJxmFcWWMZzl9dT-fPm2v5CHXUadQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=RxiXa1RINuCzd1Qu4TxEHIIetcQIKW0sDY0dCRpV1SKnaAvgehL6VaslmgaWKxT4sfHG4CLmLk3re5jOshDj2-vFH8PfSd9hRNkIEPyzCBn5anNRbt01XQrmRKV5Jlq2YfbOCevQ30ToWAQ_t9sVdqfuoetBrkceUCXApGY_HCHU1CTL4YSVyOt76sYABxqvfECXGWcia4x6dyG-QWG59Y7Tea3-xAOF1ksM-WPvHRPIAne1WmSCQnRVlmpmnArewZt54QE_GBYMBseQYaXP3bebVRJMe5pAybbizCDdGotEdCHWhu2kY5bjgmqDapFxwP6XO8ekx8lnGq2d--M5xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=RxiXa1RINuCzd1Qu4TxEHIIetcQIKW0sDY0dCRpV1SKnaAvgehL6VaslmgaWKxT4sfHG4CLmLk3re5jOshDj2-vFH8PfSd9hRNkIEPyzCBn5anNRbt01XQrmRKV5Jlq2YfbOCevQ30ToWAQ_t9sVdqfuoetBrkceUCXApGY_HCHU1CTL4YSVyOt76sYABxqvfECXGWcia4x6dyG-QWG59Y7Tea3-xAOF1ksM-WPvHRPIAne1WmSCQnRVlmpmnArewZt54QE_GBYMBseQYaXP3bebVRJMe5pAybbizCDdGotEdCHWhu2kY5bjgmqDapFxwP6XO8ekx8lnGq2d--M5xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlCX-KBhD8Ef5pxroqosdRBcZ5iwBDeu893A0l52COACT2C9PlRIslftWJhy5pxniBia-1w_p4AcH4WPQNX14xSkCeN6I7bs8ZCeD0H6jd9-ceoonD76Vm76JJ2kX-hXwcc_XWxsb1NahadH-3O8ozfUkVx2dR5cDIt8vgdSoryOxSQbf3tvu-tGnbxy4i3WsrqFHqwz1uZhdzPtdR3WQjYXqbqOGjTnhvJrFUmvUqO0kehDSp7hwcKbIs0Ac3IzG7JamvRlsyQH-MJZYhskMPh7s26LicRsnAofvv7o8V6aOtnLhfr33bOrfDC7q_qQnR88EyfVQRkl3R3608_3uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=Aw3o0w31g8xleBqiv0Ug6ZBDm01rf6KJfFOwx-DeqNrky-pFxivT4E7f8yMzcV_qaROEXlT33ZNXRTOFQdKaGQ1B4csfetRFwBH11xnycN8bu6XN8SMsLbnHpvzJwpOkpN-8Dbc65U3t72WXorPh50MviOmLTSwrCcrmnFm_YMwPbigGOXfcNBq7ycpmqtgS7m-uDpDPUjFoubmo-gQc2PAwvQr9vAkzwKnPS7Hn7Pm-i8T4A4SbE6BtG_0YlH3Vo-xDg_d4MvDT0la2nNVhv2fBdTFV-XMnkCKTllPOTVisj0kJPZBQq8PXBC2BMqCHvyHE66N0H4vjGj2ayt73RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=Aw3o0w31g8xleBqiv0Ug6ZBDm01rf6KJfFOwx-DeqNrky-pFxivT4E7f8yMzcV_qaROEXlT33ZNXRTOFQdKaGQ1B4csfetRFwBH11xnycN8bu6XN8SMsLbnHpvzJwpOkpN-8Dbc65U3t72WXorPh50MviOmLTSwrCcrmnFm_YMwPbigGOXfcNBq7ycpmqtgS7m-uDpDPUjFoubmo-gQc2PAwvQr9vAkzwKnPS7Hn7Pm-i8T4A4SbE6BtG_0YlH3Vo-xDg_d4MvDT0la2nNVhv2fBdTFV-XMnkCKTllPOTVisj0kJPZBQq8PXBC2BMqCHvyHE66N0H4vjGj2ayt73RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
