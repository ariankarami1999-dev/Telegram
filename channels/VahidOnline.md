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
<img src="https://cdn1.telesco.pe/file/enz9m8tleyMHK7SypB_tnJey1VV9djvI15HIaK5pUp6yfWqL_MAdXciHjdZbmtWeaI8-VL-tN2dPnbV33Rr7P9hj1t9t-jXTnxY8r11NfBaxdRuSfRjxCMCzYxZBKi-oP1o8qfKYq8rf_1hKZIx1L8BAn9DZvGKPLLv9kiWz3MrWAcGyfNSWpJ5KXkd7CiNR1HNH0WdKq5J4WVypDaMbqiCBSBC-f5MtBV8GjcGSW_Sbzx0AfXm8_EN_es67lezKyyDr_wjhD7zqw8ADX2qTGOZQl1R4ezjmVqu9Fy6SSfwX5h2CDIDvnKyXpd5nVanXsBMWq7wz-l_4HDWuFtk-Ag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 23:49:58</div>
<hr>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=ppkv15pqt-KvAzDMBVggFnwXOMsSDfLvCLjVq7kBTUEbdZGJsBv_nyx7nx0KbcOeiPFLMrYUmecA8_tENKrc0MZBVbXe_4fD9b13d4xRhFg9z9vEKS54mNyHKIGmS9Kmd8BVbrp2MVbPYXwIDcFC_XDi23DoSHgw2L0cb7GrwRypFIf3jvbc80QpZhzfUwzww7m2o73NuC-LjH51biCC_Kkgi8lICcM_Q-nxgxS-6I2Rv9ehSYFuTxr6445_hrWquJqEzyKodQ1JR-MADm3my9yFQ8d4L-MwCGJcZ_2IHTKiIU442gkWgR04b_QEWR3IaImq_KK7xCI7VtQuAWSrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418508ca7a.mp4?token=ppkv15pqt-KvAzDMBVggFnwXOMsSDfLvCLjVq7kBTUEbdZGJsBv_nyx7nx0KbcOeiPFLMrYUmecA8_tENKrc0MZBVbXe_4fD9b13d4xRhFg9z9vEKS54mNyHKIGmS9Kmd8BVbrp2MVbPYXwIDcFC_XDi23DoSHgw2L0cb7GrwRypFIf3jvbc80QpZhzfUwzww7m2o73NuC-LjH51biCC_Kkgi8lICcM_Q-nxgxS-6I2Rv9ehSYFuTxr6445_hrWquJqEzyKodQ1JR-MADm3my9yFQ8d4L-MwCGJcZ_2IHTKiIU442gkWgR04b_QEWR3IaImq_KK7xCI7VtQuAWSrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
دونالد ترامپ، رئیس‌جمهور آمریکا، گفت که از جانی اینفانتینو، رئیس فیفا، خواسته است اخراج فولارین بالوگون، مهاجم تیم ملی آمریکا، را بازبینی کند، زیرا به اعتقاد او خطایی که منجر به کارت قرمز شد، عادلانه نبوده است.
آقای ترامپ در جمع خبرنگاران در دفتر بیضی کاخ سفید گفت: «تنها کاری که کردم این بود که درخواست بازبینی دادم، چون فکر نمی‌کردم آن صحنه خطا باشد.»
او همچنین داوری را که این کارت قرمز را نشان داده بود، «افتضاح» توصیف کرد.
این اقدام بی‌سابقه، روند رسیدگی انضباطی فیفا را در کانون توجه جهانی قرار داده و با واکنش خشمگینانه بلژیک، رقیب آمریکا در دیدار روز دوشنبه برای کسب جواز حضور در مرحله یک‌چهارم نهایی، روبه‌رو شده است.
اتحادیه فوتبال اروپا، یوفا، هم به‌شدت از این تصمیم غیرمنتظره فیفا انتقاد کرده و آن را «بی‌سابقه، غیرقابل‌درک و توجیه» توصیف کرده است.
@
VahidHeadline
در ادامه واکنش‌های گسترده جهانی به رفع محرومت فولارین بالوگون، مهاجم تیم‌ ملی آمریکا، فدراسیون فوتبال بلژیک روز دوشنبه ۱۵ تیرماه اعلام کرد تصمیم فیفا برای صدور مجوز این بازیکن در رقابت مرحله یک‌هشتم نهایی جام جهانی را به چالش می‌کشد.
فدراسیون فوتبال بلژیک در بیانیه‌ای گفت از روند طی‌شده برای این تصمیم «عمیقا نگران» است و برای دفاع از «اصول بنیادین اخلاق، رقابت عادلانه و منافع فوتبال» به پیگیری این پرونده ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/VahidOnline/76795" target="_blank">📅 22:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f07511960e.mp4?token=UPhaZm3_jFS9ZLzrHFcX_OCZLF0OcwKFDLKcCZNZUPEJXOhw_TyrqVsJZEvTnU_0vsQ6z3m1bXM-mUYKz2XNOkVz-CDUa2RHS2oPn0LYukZR7KocWv01BEkGMA8bqmfILxzmBcQ6YZ2-xW-zVQVpSM0CPwf3BHBwJIxpYdPJ_n8gvXtcYy1HL8hlF5vktQ-WXxQtaDJpBJz7xYiHIfi85riFGmIIqUqwUqTlpHLGiHW5HHCvzf037IKz1upb7CcRI7IcgksTvRKzqn3yQ71nWp7TkcSrJqcuWOW4tKNWxz1vLrxLsQuGX3XTsHA3H3wNQy7FB3uMessPYBs0bEHeIA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f07511960e.mp4?token=UPhaZm3_jFS9ZLzrHFcX_OCZLF0OcwKFDLKcCZNZUPEJXOhw_TyrqVsJZEvTnU_0vsQ6z3m1bXM-mUYKz2XNOkVz-CDUa2RHS2oPn0LYukZR7KocWv01BEkGMA8bqmfILxzmBcQ6YZ2-xW-zVQVpSM0CPwf3BHBwJIxpYdPJ_n8gvXtcYy1HL8hlF5vktQ-WXxQtaDJpBJz7xYiHIfi85riFGmIIqUqwUqTlpHLGiHW5HHCvzf037IKz1upb7CcRI7IcgksTvRKzqn3yQ71nWp7TkcSrJqcuWOW4tKNWxz1vLrxLsQuGX3XTsHA3H3wNQy7FB3uMessPYBs0bEHeIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه بار دیگر گفت: من به دنبال تغییر حکومت در ایران نیستم، هرچند این تغییر حکومت اتفاق افتاده است.
ترامپ افزود: حکومت اول از بین رفت، حکومت دوم از بین رفت. حکومت سوم معقول‌تر است. خواهیم فهمید.
@
VahidHeadline
دونالد ترامپ گفت آمریکا یا با ایران به توافق خواهد رسید یا «کار را تمام خواهد کرد.»
رئیس‌جمهور آمریکا در یک گفت‌وگوی تلویزیونی گفت قیمت نفت با وجود بسته شدن تنگه هرمز چندان بالا نرفت «آنقدر که ما نفت از آنها گرفتیم. مردم اصلا خبر نداشتند و همه اینها فقط در عرض یک ماه و نیم اتفاق افتاد.»
رئیس‌جمهور آمریکا بار دیگر تکرار کرد که کشتی‌های نیروی دریایی و تمام هواپیماهای نیروی هوایی ایران را از بین برده است: «در نهایت فهمیدند که دیگر رادار ندارند، چون سامانه‌های راداریشان نابود شده بود. بنابراین، آخر شب و در تاریکی آنها را هدف قرار دادیم.»
او همچنین گفت: «نیروی دریایی قدرتمند ما بزرگ‌ترین محاصره‌ای را که کسی ندیده اعمال کرد و در طول دو ماه حتی یک کشتی هم نتوانست از محاصره عبور کند. بعد نزدیک شدیم به اینکه شاید بتوانیم به توافقی برسیم پس محاصره را کاهش دادیم. نمی‌دانم، شاید هم به توافق برسیم.»
آقای ترامپ تاکید کرد که «به هر حال پیروز خواهیم شد. یا به توافق می‌رسیم، یا کار را تمام می‌کنیم.»
او گفت تمام کردن کار ایران کار آسانی است: «تمام کردن کار دشوار نخواهد بود. البته من ترجیح می‌دهم توافق شود، چون نمی‌خواهم ۹۱ میلیون نفر تحت تأثیر قرار بگیرند.»
«ما می‌توانیم ظرف یک ساعت پل‌هایشان را ویران کنیم. می‌توانیم شبکه تأمین انرژی را از کار بیندازیم. همه آن نیروگاه‌های بزرگ، زیبا و مدرنی را که ساخته‌اند. آنها پول زیادی داشتند اما حالا دیگر پولی ندارند. ما هیچ پولی به آنها نداده‌ایم اما می‌توانیم برق و نیروگاه‌های تولید برقشان را از کار بیندازیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/76794" target="_blank">📅 18:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qlm1-xaCItOLmNcCWUnAKTWWryr4Gtcd2LagvBQmryTRP9B9KBYuPJHS4_Hq4O8GauSDOeF893_38Dy_RNUmBdsyruju53oIKSQVTejG5z3rWVhiBqCsmkjLsCgh-7TLBycVLht-vG5jmAo6tGe73IOAzCruHl2rOJSqmOAtz5GZzHnkSxkdobgIYnzBCA93QYsy08DHKWlhkQc1DD3TY-6w-K1MxveJgR5R-nfj7NJxNtecQpltRMNuq_BcZ98ozZj3iRjKW69kZFlyRxmuucfxXUKMy2XC2WNX-wr44BB8MKMAH6JozQj9nPRZxMPGmDrXItBHQoB54MemPRVL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=hKB-fSYOuHwMokVFSa7qGhniw8gkIHr83Gl0GgUXsgSZSnm_Gy3TkugrBLL1GlAAlbMGAU8UUhmOvGDdR9cHArZbhByE-cIBPmI0npIVnvIW4ZSTgodgY53Q7OYLAPnjym7QXwshAvaHrfHoNtk0Ea5QnFWYHLl6-pvp2M7qgZmI7lWIqs1hQMJdM6aAumn1mPQyb304xKGif-HslrzhD4bjnPiSMhqSU97BDCaKJjQ5ih0KnQHJwZ3joZZvoNEsQJ-FPOJY_ql3P6xDXYQrXBcpJ19KqTv5RBTIxI6ujUhGvPi1TxRmvTdnz3vr1vsNcc27_WP2p60wp4vIxwpbCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26366fc1dc.mp4?token=hKB-fSYOuHwMokVFSa7qGhniw8gkIHr83Gl0GgUXsgSZSnm_Gy3TkugrBLL1GlAAlbMGAU8UUhmOvGDdR9cHArZbhByE-cIBPmI0npIVnvIW4ZSTgodgY53Q7OYLAPnjym7QXwshAvaHrfHoNtk0Ea5QnFWYHLl6-pvp2M7qgZmI7lWIqs1hQMJdM6aAumn1mPQyb304xKGif-HslrzhD4bjnPiSMhqSU97BDCaKJjQ5ih0KnQHJwZ3joZZvoNEsQJ-FPOJY_ql3P6xDXYQrXBcpJ19KqTv5RBTIxI6ujUhGvPi1TxRmvTdnz3vr1vsNcc27_WP2p60wp4vIxwpbCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیمای جمهوری اسلامی روز دوشنبه ۱۵ تیرماه تصاویری از حضور احمد جنتی، دبیر شورای نگهبان در مراسم تشییع پیکر علی خامنه‌ای منتشر کرد.
رسانه‌ها روز دوشنبه همچنین تصویری از محمود احمدی‌نژاد را در مراسم مرگ رهبر سابق جمهوری اسلامی منتشر کردند.
خبرگزاری فرانسه روز دوشنبه گزارش داده بود در حالی که مقام‌های جمهوری اسلامی تلاش کرده‌اند تصویری از وحدت در صفوف حکومت ارائه دهند، تاکنون هیچ‌یک از روسای جمهوری پیشین جمهوری اسلامی، که روابطشان با خامنه‌ای دچار تنش بود، در این مراسم‌ها دیده نشده‌اند.
مراسم تشییع جنازه علی خامنه‌ای پس از دو روز قرار گرفتن پیکر او در مصلای تهران از ساعت شش صبح دوشنبه ۱۵ تیرماه آغاز شد.
روز ۹ اسفندماه ۱۴۰۴، در موج اول حملات اسرائیل به تهران بیت علی خامنه‌ای به‌شدت بمباران شد،‌ به شکلی که تمام ساختمان‌های محوطه بیت با خاک یکسان شده بود و همین احتمال سالم ماندن جسد رهبر سابق جمهوری اسلامی را بسیار کم می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76792" target="_blank">📅 16:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5u5VPlyz2rmoZaMFAeDmKqHMBTolnk7yZKt_8iDh5Hc4FR22Iz_FNzf3wk_A-MOFMh6cs7ghT4-iIpr8FG1mRO6QtN9O9I90qEaZWXmDDt5kcZzR1rmPjxAy5GiVywEICDrzmQS_PXn-5hb0kdy0a5oszR1ivQQUe9dfyNzOrfRLExzghbXX9IgdW5HDcIt3LU0JAR0EkYfWgFkbSRzuyMzTFIBTWk3Q_mXVH06PUQ0GzTJzpiUN0aetw2Vroi881BysL9_Ch8YdC6cf9Hmb7dzuWXc0hgONLFqYrXPfzPFSJ0LLLR9OQJnIrMRYaoyHeXqOHNRX7iS_-71n7Btog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، آقای مهدی ناظر و خانم مهناز چاردولی، نامزد او، را به اعدام و ۱۰ سال حبس محکوم کرده است. همچنین خانم عاطفه ناظر، خواهر آقای مهدی ناظر، به ۱۰ سال حبس محکوم شده است. این سه نفر در تاریخ ۲۱ دی‌ماه ۱۴۰۴ در تهران بازداشت شدند.
@IranRights</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/76791" target="_blank">📅 16:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PSAaHbEjTI006Pd-Z6YAggNXDnPfF_6MGkxLF6Yi8X6emp1dyJPK54vOOfLGze2IO3Clf2E8f0M56Z4Q84U56OkIypQ56M_jzLd_YMEJdqdrYKAkPrI2vSd6igQMSnsV-AuOzjTTH9K2uXxQHTVEaCZLEmScSAZjh-3HXymHTFOWwJEgSoMJd-NJXkOlXLip4_WJTv5NOMzYG3Jpj-JrcwA-NcldlYAnzIWL_mgk-d1SM3mOOpv7U6seKyuQ6La3r6PT_Yid4947vx_ktkmu0QnmR47jFM1EyLnUjqhrSTNN07D1Mr8zuOh3iivpMcPNwE4wY7jFtru8K7GHRB4tQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه روز یکشنبه ۱۴ تیر متن حکمی را منتشر کرد که در آن مجتبی خامنه‌ای، رهبر جمهوری اسلامی، غلامحسین محسنی اژه‌ای را برای یک دوره جدید پنج ساله به عنوان رئیس قوه قضائیه ابقا کرده است.
محسنی اژه‌ای از دهم تیر سال ۱۴۰۰ با حکم علی خامنه‌ای به این سمت منصوب شده بود و مدت پنج سال ریاست او بر قوه قضائیه به پایان رسیده بود. حکم رهبر جدید جمهوری اسلامی با امضا در تاریخ ۱۳ تیر منتشر شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76790" target="_blank">📅 19:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aVMqzumkT9WLeSVb8O_-ibCBun-SR0Yy8M5Nr8mDYmECYcE2eVtevGyJdwmSIbnAtGH4ZDooPMbdge8HaYXZPrQ7VfMh79HasYFPdS7Cao2beG51OA_XaIlWWOkMgiv4pChXrmXjfP7pAKpOVrY2wBdAaG_l4rUXZTceAmueRmFrCYtvQsFb_TBY4XursgY83CQyVlEe_Sd-fZT4Vd9gxz5gzspKst3hn51h1Z6c3wC5FMfUzqeoGSkLhDDSD9GrrvRHJjS14WrrqivWjUhM6sG1Kfual8wvODOpclHB9JEVypbXdfFVnmqRTbJzD43tx7ktsM-oFXve1-q7N0vfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=ZvR-FUf8znl9PpVkJt_UVHQ8ZJMFtAYIDYmVfXh_5AAuPOcg6AohOetgAPQRmJ_m3iPcvtZ6cI7EMgPxY9bZW5ru-8ptpeIvhNfHjVrtvwttQBipL9KGMmqqR_4bRHd_Z7qxN-p624BivLAe7swhOhHcfkehHrjTr3MD7zn67sQUsSbYD-g8LQajb2TEP7qNk0j2vq1ULqhGQEedckX5ZuYTb5NDd0qQ3cbbWUefNuhgUyJqztfS6-cEqFJ_kkmVbVMk-ujrBNv6wpgEYKMc46Ou75BC43OtuOzzsfNQ-YrNvhrvEfD97CXcyxQLmL8BrBQG4b4rIiaCLOyn2hTcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/15ac8211bb.mp4?token=ZvR-FUf8znl9PpVkJt_UVHQ8ZJMFtAYIDYmVfXh_5AAuPOcg6AohOetgAPQRmJ_m3iPcvtZ6cI7EMgPxY9bZW5ru-8ptpeIvhNfHjVrtvwttQBipL9KGMmqqR_4bRHd_Z7qxN-p624BivLAe7swhOhHcfkehHrjTr3MD7zn67sQUsSbYD-g8LQajb2TEP7qNk0j2vq1ULqhGQEedckX5ZuYTb5NDd0qQ3cbbWUefNuhgUyJqztfS6-cEqFJ_kkmVbVMk-ujrBNv6wpgEYKMc46Ou75BC43OtuOzzsfNQ-YrNvhrvEfD97CXcyxQLmL8BrBQG4b4rIiaCLOyn2hTcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماز میت بر جنازه علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، روز یک‌شنبه، ۱۴ تیر رأس ساعت هشت صبح، توسط "آیت‌الله جعفر سبحانی" اقامه شد.
مراسم تشییع او بیش از چهار ماه پس از مرگش در حال برگزاری است.
اما نکته قابل توجه در این مراسم غیبت مجتبی خامنه‌ای است که از او به عنوان آیت‌الله یاد می‌شود و کمتر از ده روز پس از مرگ پدرش به عنوان رهبر تازه جمهوری اسلامی معرفی شد، اما در این مراسم حضور ندارد تا نماز میت را برای پدرش اقامه کند.
در این مدت طولانی از مجتبی خامنه‌ای نه فایلی صوتی منتشر شده و نه ویدئویی که نشان دهد او توانایی رهبری حکومت را دارد.
با این حال سه پسر دیگر علی خامنه‌ای، مصطفی و مسعود و میثم، که از روز ۹ اسفندماه سال گذشته یعنی آغاز جنگ تاکنون خبری از آنها نبود روز یک‌شنبه بر سر تابوت پدر خود حاضر شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/76788" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO66YeFGAIzC5UkZGi8BNwTyUqA5U-CF4E4FU-2XP-tiakGo7XvOfxCXEQcokxflXWPgBTMqlIc4fBrYYtTnjGZ8ajYT5LF1Rgfpz99quc6r5_XGpuT5r7Lk-Qsp3_unGNskUOooWezsDyjq22151vTVJZ3LUMs1RAS2BxqYZgg1z5-99ohlE7abZNKpY5yb7aD4ESxN0eltMaNbyn74OyKVLX2grhqyZeHw9EXut2iOhCrFqqXX_4bd2iS8eW1KIMzHU4JL-Jp20xpJQgityA3mTQQziEfVZxiOJ0b6SpGB2o3VKjqCesKlpTWWH-gR_IwyqsQ3YOdDZP8oNdC3kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا روز شنبه ۱۳ تیر، در گفتگو با وبسایت خبری آکسیوس، اشاره کرد که تصاویر مربوط به مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی را مشاهده کرده و از دیدن گریه افراد، متعجب شده است. او گفت:
از دیدن برخی ایرانیان که در مراسم تشییع گریه می‌کردند متعجب شدم چون گمان می‌کردم مردم از او متنفرند. شاید این اشک‌ها ساختگی باشد.
ترامپ پیش‌تر اعلام کرده بود که مذاکرات جاری میان تهران و واشنگتن، به‌دلیل برگزاری این مراسم یک هفته متوقف شده است. او در بخش دیگری از این گفتگو با اشاره به حضور اغلب چهره‌های سیاسی و نظامی جمهوری اسلامی در این مراسم گفت:
آن‌ها همه آن‌جا جمع شده‌اند. کار یک شلیک است! اما این کار را نمی‌کنم چون در آن صورت کسی برای مذاکره باقی نمی‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/76787" target="_blank">📅 23:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این مجله ۹ ماه قبل از سرنگونی حکومت صدام‌حسین در عراق و سپس اعدام او نیز عکس صدام حسین را روی جلد برده بود. معمر قذافی نیز از دیگر رهبران منطقه بود که ۶ ماه قبل از کشته شدن به دست معترضان، عکس او روی جلد تایم رفت.</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76786" target="_blank">📅 19:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=gFvZRdwLy-CAjc4IDJHuE2rHamJ8t2M_ucL52BooKg_lQiCojtnJFFQCwxaEVw0WOp4UZuYNX-RvwtzjA4gebzqnGm9_DpPj54GGxfO6-QNHmITA-XKKBQpc6RFo-ilszSHurRTazwUlynhWi-NL4a0tiVNOQd0LKeSxftigAbmqGupPhXZEl253FnFziE60MPFMXw43DSamNXLzoU3st2HaA4vrWQCSKZlWRHeEOcgHbWt9YRTD9ojjYikbl2LODpDAEfUJ14khkceo0-tQK59wgQFGagsYGgRDCFcJMUO2YpyE7NNMrl1Jm6J42CXjKv0_cIoBayzy7hHBH-7_NA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8eed8d3ddd.mp4?token=gFvZRdwLy-CAjc4IDJHuE2rHamJ8t2M_ucL52BooKg_lQiCojtnJFFQCwxaEVw0WOp4UZuYNX-RvwtzjA4gebzqnGm9_DpPj54GGxfO6-QNHmITA-XKKBQpc6RFo-ilszSHurRTazwUlynhWi-NL4a0tiVNOQd0LKeSxftigAbmqGupPhXZEl253FnFziE60MPFMXw43DSamNXLzoU3st2HaA4vrWQCSKZlWRHeEOcgHbWt9YRTD9ojjYikbl2LODpDAEfUJ14khkceo0-tQK59wgQFGagsYGgRDCFcJMUO2YpyE7NNMrl1Jm6J42CXjKv0_cIoBayzy7hHBH-7_NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رحیم صفوی: این یک جنگ موجودیتی است و مطمئنم که اسرائیل از بین خواهد رفت
یحیی رحیم‌صفوی، از فرماندهان پیشین سپاه پاسداران و مشاور مجتبی خامنه‌ای در حاشیه مراسم تشییع علی خامنه‌ای، با اشاره به درگیری میان جمهوری اسلامی و اسرائیل، آن را یک «جنگ موجودیتی» خواند و گفت دو طرف در نبردی قرار دارند که تنها یکی از آن‌ها می‌تواند در منطقه باقی بماند. او افزود: «من مطمئن هستم آنچه باقی خواهد ماند ایران است و آنچه از بین خواهد رفت اسرائیل است.»
او همچنین با مقایسه کشته شدن علی خامنه‌ای با واقعه عاشورا، مدعی شد کشته شدن او، «حرارتی» در میان مردم ایران، شیعیان و جهان اسلام ایجاد خواهد کرد.
رحیم‌صفوی در بخش دیگری از سخنانش ابراز امیدواری کرد که مجتبی خامنه‌ای راه پدرش را در حفظ «ایران قوی»، دور نگه داشتن سایه جنگ از کشور و پیشبرد توسعه ادامه دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 396K · <a href="https://t.me/VahidOnline/76784" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnRlXrk0-48af-AR2OkXp34r6SowVTo-hn836zvNMIQYSmWoKZI19Mc9-MIiBSFzoDQS5WbJzWEsgJrb3saI0iPhxTQLWB1bhsn_yxqMD24dirZXgLb-zzhmBGLEM8AXvfKJ47OqkhTx2PxxKukrhjhRzoqUKkYzh2nnLCWJoPmKIEVdHwoOB20mR3gvPF1TFf5u_TCNydf-GjXaLQMX-PbjkPzrJ9BATJFLiW7ImcusB9FvbSCltzyxbkb0MaYNfsbomluHg0R6VGTnN94w0zjN-InxFH1lULiDR3wH85bB40wk7-2GKSiszPrE2CRueGCF-zYrZyuQ7sAuFzZkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ اعلام کرد به‌دلیل مراسم تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، «یک هفته» به مقامات تهران فرصت داده است.
رئیس‌جمهور آمریکا در سخنرانی خود در مراسم دویست‌وپنجاهمین سالگرد استقلال آمریکا که شامگاه جمعه ۱۲ تیر به وقت تهران برگزار شد، گفت: «ایران را به‌شدت در هم کوبیدیم. آن‌ها برای توافق بی‌تاب‌اند. به‌شدت می‌خواهند به توافق برسند. ما به‌خاطر مراسم تشییع، یک هفته به آنها فرصت دادیم، چون آدم‌های خوبی هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76783" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2tK0F6DSsxiB9bL9-Y-1LO9wPGz1pBAEZQPr-NuT7q5IQq7PrJY4rBbrxZ-RczcUeVQEzzdPvhjhmPybaqxHKeXdPABryuxYGeCi0aAxo-VauQqm6WBVsQfE8RltByM_RTdsf17ZhV0wNxAOns_21m8KZvsHHKcqCz1tbMO_SKuF4pNX5TBkzaqwVWNNLw1Ng0_smmZUXrwDPJOi2ZWJBA355QfhEgf55nRBeBZPjGnipHyMDy_jqZ365zg_ryNtTN-Uojrt2dDV6Lda1GFfOB1QLVjNjNAR-u2D_-Reg9wUjRDnVXkuYVTdom5xQvRMBhUBxcoh2dQj2EqeKUf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگین کیانی، عکاس مستند اجتماعی و مدرس عکاسی، از سوی دادگاه انقلاب بابل به یک سال حبس محکوم شد.
رسانه‌های حقوق بشری گزارش گزارش داده‌اند، شعبه اول دادگاه انقلاب بابل خانم کیانی را به اتهام «تبلیغ علیه نظام» به یک سال زندان محکوم کرده است. این حکم روز ششم تیرماه صادر و به او ابلاغ شده است.
نگین کیانی ۱۹ فروردین امسال در منزل پدری‌اش در بابل توسط نیروهای امنیتی بازداشت و یک روز بعد با قرار وثیقه آزاد شده بود.
این عکاس ۳۷ ساله پیشتر نیز به دلیل فعالیت‌های مدنی خود چندین بار احضار شده و با برخوردهای قضایی روبه‌رو بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76782" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76781">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy6Di8lBV4bnDZMhMe_I2W1tw593P4zUHEVa8ZjbAfOMKW_I0kd4zJEnP8ucIAGdGGTKu9iCks6J9CL-ZjQhFyjjBGTXx_cmqc-ZncMlN8vkzFZXzbnsRpsQ0--RkJniEI2Wi7qMHINqhRXDnUJatbqRPvPhDS4eFE-FQDQb4S0uTd_i1y2m__HiHO5JTYGA_AGSK9XrC9OK2bj7x0mvJGkLy4geleUm9ro0aAmMXpcJ-oicmdQXla02ybztl8YVHWraUeB0qFpMn4xa2f8QD2gKbG0ZHwvHsNNTT9JctluXvihizYJu2VYLnVjRQiCaRVvCqBRxR0NWrLXc_0S0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرنوش پارسی‌پور، نویسنده، مترجم، تهیه‌کننده و فعال اجتماعی ایرانی، امروز در بیمارستانی در حومه سانفرانسیسکو درگذشت.
خانم پارسی‌پور که از دهه ۷۰ خورشیدی در شمال کالیفرنیا زندگی می‌کرد، از هفته گذشته به علت سکته قلبی در بیمارستان بستری شده بود.
او در سال ۱۳۲۴ در تهران به دنیا آمد و اوایل دهه ۵۰ خورشیدی از دانشکده علوم اجتماعی دانشگاه تهران فارغ‌التحصیل شد. نخستین داستان بلندش، «سگ و زمستان بلند»، را نیز در تهران منتشر کرد.
خانم پارسی‌پور در دهه ۵۰ برای مدتی در تلویزیون ملی ایران کار کرد و سپس برای ادامه تحصیل ایران را ترک کرد، اما در سال ۱۳۵۹ به ایران بازگشت.
او مدت کوتاهی پس از بازگشت به ایران بازداشت شد و چهار سال را در زندان گذراند. پس از آزادی به ترجمه و کتابفروشی پرداخت، اما فشارها ادامه یافت و سرانجام به آمریکا مهاجرت کرد.
خانم پارسی‌پور در سال‌های اقامت در آمریکا نیز چند داستان بلند و ترجمه منتشر کرد.
شناخته‌شده‌ترین آثار او در ایران «طوبا و معنای شب» و در خارج از ایران «زنان بدون مردان» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76781" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kRqRFv57dNfn0sLpChOwGX9RtCfY44WR8unSCS1eqZtNXeDQTzc4MExefijBVQ39AFSo05Nue_FI-0WtP0shvIOBQOOeUIc2Mlh-I-cmZBaIKJGZskYvhATH5xrapJ0zYbUhZ7qDrZNg1kYYKc9yrn1AhNcQZZ3I_j9nEF9_mcNgy7ILQXxylcse0s6I3NHjEjGY-3Y3RuoRByCIHVQOwo19kBC9a4FdZwkmyBCbY-AZi7GRSGaSf0wMYXrb9Nonf6v20sXc56gYLW9VKocGUkvnF8h1ggxLAkXA70hgRvnVIkbXVTW5061vUjCLA0PyvbwQI3TL55D3nc9x0GDXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bVsq2OeogldhQsoAeYBLZ-RRXpktQkXTE8Yp_outVUwfkTfWr_Jbssd4c-00zbW6zYBCEX5eAqvvAm3bScDkA5bWPVj5_nF4p2nzQk6jmbQAmRXjTemz4yApGRLvBLkxXXq9ndSy8H_nMpAbmmLNZHP21cm77lCynqolt8RzShmvwYifspO5b3cHlAbFg3STjZe8JcxZ3l2_AiUh0trW205gY7VKhSTGNwz62ULnIgl5OAnyT136345y3YSw9zl8jlnbyAqhEKlpiXbsB_MZsyQ6-dI8hzypwGSmsJhzSvLQsDzSbxPSUE9_vhQK_gJHpH-KtenVQQ3zY4qfls3nzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=PQtKqJlOjbjwP7b_D_9T2RkeHly83h0RCJLm8JsIwC2XX0CShnjxgEg6DZcRzD95AQD4MZ7pxYoNMRoXCvQgETD6oVGYmqQ9l6bnvIKwnReQyQhctDs2Wsrvks1406cFlr9PyTX8cYNiM6BKP3hQZFwSLrd3ggBUb6jN1kbuurL4NWe21n2BPyisFvOjJqQWfK_jhzyuzXT527wWhTlkbvtjzjD8nidX4woMnr5pZKIr-uTY2ANfSAmrHS4k8IZllXnkbRLytfyBZ99twZKk9ELkLFWBvda05v_XJZO_pU8z5yH2uaQD9Nj28-V2CLg_o25Zi2UleBDquwfW1KVq5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3b6da11ae.mp4?token=PQtKqJlOjbjwP7b_D_9T2RkeHly83h0RCJLm8JsIwC2XX0CShnjxgEg6DZcRzD95AQD4MZ7pxYoNMRoXCvQgETD6oVGYmqQ9l6bnvIKwnReQyQhctDs2Wsrvks1406cFlr9PyTX8cYNiM6BKP3hQZFwSLrd3ggBUb6jN1kbuurL4NWe21n2BPyisFvOjJqQWfK_jhzyuzXT527wWhTlkbvtjzjD8nidX4woMnr5pZKIr-uTY2ANfSAmrHS4k8IZllXnkbRLytfyBZ99twZKk9ELkLFWBvda05v_XJZO_pU8z5yH2uaQD9Nj28-V2CLg_o25Zi2UleBDquwfW1KVq5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/76778" target="_blank">📅 19:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/555882678d.mp4?token=pgpaOiFkzwFfgvhecddZTKPZcqiZIvLtQ-svIs_WVzhmTCw6KJeiXiovZqn-mfQiPGfVKxEBv4TYo490zn4skbnlT--Asjg7Iy5zLpF2Z_wN_URiDZm2sgA1dpJdbWwroJuVXOqJB41jl3tNJl5Ni5RfngxzgWfcVhEtm7t9ScKJonkPthry1Nzm8wWMyKNFcuH3oJiyIm4hY4U68_dBFpVx7kQeUAloEhErLNKQ2Ts-1Vy8NqR2aWCIgC2Vu99mdHcmTeDIVmxaO6O4P8vmSD3vP4IjiCAA3DgwBgvQUlSCYhu4g_lZLYTY7H1fzsLE4vx1qtn8KIwiZ9ZatlL7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/555882678d.mp4?token=pgpaOiFkzwFfgvhecddZTKPZcqiZIvLtQ-svIs_WVzhmTCw6KJeiXiovZqn-mfQiPGfVKxEBv4TYo490zn4skbnlT--Asjg7Iy5zLpF2Z_wN_URiDZm2sgA1dpJdbWwroJuVXOqJB41jl3tNJl5Ni5RfngxzgWfcVhEtm7t9ScKJonkPthry1Nzm8wWMyKNFcuH3oJiyIm4hY4U68_dBFpVx7kQeUAloEhErLNKQ2Ts-1Vy8NqR2aWCIgC2Vu99mdHcmTeDIVmxaO6O4P8vmSD3vP4IjiCAA3DgwBgvQUlSCYhu4g_lZLYTY7H1fzsLE4vx1qtn8KIwiZ9ZatlL7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">[بنا بر تصاویر رسانه‌ها، مقام‌های مختلف در گروه‌های چند نفری در مقابل جعبه‌هایی که گفته می‌شود بقایای علی خامنه‌ای و تعدادی از اعضای خانواده‌اش در آن‌ها قرار دارند حاضر می‌شوند.]
رهبر ترکمنستان، روسای جمهور عراق، تاجیکستان، گرجستان، نخست وزیران پاکستان، ارمنستان، روسای مجلس جمهوری آذربایجان، عمان، قطر، عراق، ازبکستان، قرقیزستان، بنگلادش، مصر، وزراری خارجه نیکاراگوئه و کنگو و معاون رئیس شورای امنیت روسیه، رئیس اقلیم کردستان عراق، به همراه هیئتی از طالبان افغانستان و شبه‌نظامیان مورد حمایت ایران در عراق، یمن و لبنان و همچنین دبیرکل جهاد اسلامی فلسطین در مراسم ادای احترام شرکت کردند.
از نکات قابل توجه عدم حضور مقام بلندمرتبه‌ای از کشورهایی مانند چین، روسیه و ترکیه به عنوان حامیان جمهوری اسلامی ایران در این مراسم بود.
تاکنون تصویری از اعضای خانواده علی خامنه‌ای به جز هادی خامنه‌ای، یکی از برادرانش، در این مراسم منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/76777" target="_blank">📅 18:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/esUp9cKtq0azTLZS5dwuAuhhwbAp3NAVGDF6-XVuqN4hucrqTS3G_0OrK0HL6uU5fqQhtOLWWyKXwbjxO28iRQlFUuNRm3bB13lZ16A5O4GnAfxwVv67Lg8ITmQbI6ywD4CQ4ylisSEcXj4KEbHJivROd5lz6w0J6LdCOxKGldwjEjXPZ4t4Oioo1DgUjbqCtya_YvnMyt__jjAZb6ICyzV-1g-nDohOPzHKv7dtTc8eE1ueYBN4zdh-ke467yeDRBLGeQSVivdPZFCCRzH_OOOEaWvzOHTSLWrNCi70ocgRJjWpYgnTU8bUdJsPW0-_sEtxri9lztsF_7HwONj63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سایت هرانا الهام زراعت‌پیشه، وکیل دادگستری، از سوی شعبه اول دادگاه انقلاب شیراز به شش سال حبس، دو سال ممنوعیت خروج از کشور و ابطال گذرنامه محکوم شده است.
بر اساس این گزارش، شعبه اول دادگاه انقلاب شیراز الهام زراعت‌پیشه را به اتهام «اجتماع و تبانی علیه امنیت ملی» به پنج سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم کرده است.
این دادگاه همچنین او را به مدت دو سال از خروج از کشور منع و گذرنامه‌اش را باطل کرده است.
الهام زراعت‌پیشه ۱۴ اردیبهشت ۱۴۰۵ در محدوده دادسرای اجرای احکام شیراز بازداشت شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76776" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlrSvnEuaZcp7OqD8qKFLHKA8YHBN7gsCOuf650tT4pDqK64-5h6TDqIULvtqpcRREdC2Q7jbUMdJdzbh1tMSLh-V9gxWLPfUVmD2_p2gEKFsHC8w8BJC-xGDYma_rpjSlEp7_PsTBh8IC3iPtBV6yCO_fZTNDDk9r1tdcLZGP7ZhCLKpf-Ns5C2IpcB9Jh7YmvU-d4uut1jNPebCh7R3WYCOT_zHCf7Wfa5o7XuBVhUqg8KQRWVWanxZBj01FZK8mdbBO6r2FE7s8wqYvzn2R-GVLWNwdFH_zvCWSrQpamYrX-WWkKU9Z8TB0Q3dMUWVdgeNShOzU71ODVWdVrShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارغوان فلاحی، زندانی سیاسی ۲۴ ساله محبوس در زندان اوین، از سوی شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی، به اتهام «بغی» به اعدام محکوم شده است.
خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، با اعلام این خبر نوشت حکم اعدام فلاحی بر اساس ماده ۲۸۷ قانون مجازات اسلامی و با استناد به اتهام «بغی از طریق عضویت در گروه‌های مخالف نظام و اقدام مسلحانه» صادر شده است.
ارغوان فلاحی در جریان پرونده‌ای بازداشت شد که چند متهم سیاسی دیگر نیز در آن حضور دارند. نهادهای امنیتی جمهوری اسلامی او را به عضویت در گروه‌های مخالف حکومت متهم کرده‌اند.
منابع حقوق بشری می‌گویند او این اتهام‌ها را رد کرده و روند رسیدگی به پرونده‌اش با محدودیت در دسترسی به وکیل و برگزاری جلسات غیرعلنی دادگاه همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76775" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3b_H3KEdiIeyMwQSchWrX9RBjJk95du9Pnk5fk7wOE02-3RvANWrQwvSfnmSU9FL0ZVZ70Y1TIHykK1NH1As18MyUeANMNDlH44EHmsfbm7hL4QNFiPsE747RleX2Ul3yfz0-vUcsALVi2XB4p_D7bzxOTRcZcbPBlAEMWeWuoJxshQigjFgzxONsMVDEtG6H5XKnVzy0-uCWiJitpKiGJfo1mXofdGEUdenbrZQDbmM1f0mnT0lsgUqWvi3s4ga_LqIpNEvpx5IyTGlLeb9xCagCsg6cuVJmG41GO3B_iqeNL5IV4qo_Qq5NSpMPDxaXJIU7oh49V9kcRlK3pOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، بامداد جمعه ۱۲ تیرماه در گفتگو با شبکه سی‌ان‌بی‌سی گفت جمهوری اسلامی از نظر نظامی «کاملا شکست خورده» و مذاکرات میان تهران و واشینگتن ادامه دارد. او افزود: «فکر می‌کنم آن‌ها تقریبا با همه چیزهایی که ما نیاز داریم موافقت کرده‌اند» و ابراز امیدواری کرد این مذاکرات به نتیجه برسد.
ترامپ با مقایسه وضعیت کنونی با جنگ‌های گذشته آمریکا گفت برخلاف جنگ ویتنام، افغانستان و کره که سال‌ها ادامه داشتند، در چهار ماه نخست دولتش توانسته جمهوری اسلامی را از نظر نظامی شکست دهد. او گفت: «آن‌ها کاملا از نظر نظامی شکست خورده‌اند. هنوز چند موشک برایشان باقی مانده، اما اگر لازم باشد آن‌ها را هم از بین می‌بریم.»
رئیس‌جمهوری آمریکا همچنین گفت هفته گذشته پس از آنکه جمهوری اسلامی یک پهپاد را به سمت یک کشتی فرستاد، نیروهای آمریکایی سه بار مواضع آن را هدف قرار دادند و هفته پیش از آن نیز دو شب پیاپی حملات مشابهی انجام دادند. او افزود این عملیات‌ها هم‌زمان با ادامه مذاکرات انجام شده است.
ترامپ در بخش دیگری از سخنانش گفت آمریکا با استفاده از نیروی دریایی خود «دیوار فولادی» در اطراف ایران ایجاد کرده و «حتی یک کشتی هم نتوانست به ایران برسد.» او ادامه داد حکومت ایران با تورم ۳۰۰ درصدی، کاهش شدید درآمد و کمبود مواد غذایی روبه‌رو است و در صورت دستیابی به توافق، آمریکا می‌تواند گندم، ذرت و سویا را از طریق کشاورزان آمریکایی در اختیار ایران قرار دهد.
رئیس‌جمهوری آمریکا همچنین گفت «قدرت و جسارت» جمهوری اسلامی از بین رفته و با انتقاد از گزارشی در روزنامه نیویورک تایمز که نوشته بود ایران نسبت به چهار ماه قبل در موقعیت بهتری قرار دارد، افزود: «توان نظامی آن‌ها از بین رفته، رهبرانشان از میان برداشته شده‌اند، فرماندهان رده دوم و حتی برخی فرماندهان رده سوم از بین رفته‌اند، بنابراین نمی‌توان گفت امروز در وضعیت بهتری قرار دارند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/76774" target="_blank">📅 02:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TOkhzmbLamEB4nLda9HRgWF4M3Vm7VBAnynJh6XBfdGzD0elwhb2wPmsKAiaXYpsx2mf5JXxcEPsN98rm2tmwoIIHSvVmVjV_191QC-MY-JcGLLlwKhY46Ryy0zfqXw85VRPRvvBFzl4Cl3ZPqfDbpo3ALA3U-5JSVkuo4zF51CdnSIT9hTCOur2QanKmkf1UASWy8fdou_re4Llpk0frp9i0uiXS3Hr5xPmm2S8Hy4J3UgCfKNYKqVAlRu_gJciHivdrYIv7GsRAGk3ZcDnHXNqn8ktzEB5CsEioDuWDZ3t89qP_OimmfC5Cn0JaePM8xDoFqGiksozwLjacwOqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"دارم خواب می‌بینم؟ سلام دنیای جدید!" ویدیو دریافتی از 'شادی جوانان شهر #گله‌دار در شهرستان مُهر استان فارس، یکشنبه ۱۰ اسفند' Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76773" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76772">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m3vL_jBqVJgOK_zzJMDPSsvMoqRG2eQy5mzXQf3M2e0DjdZrIBoldGK6DRANHmlSQC6RBGRWiJSCApnHac6M96oTTGZeOZC6lptKPErvJprXLpE_w-mLr8zRzh74FeFDiX_LL_EvxtFYR1VqTNTbPXT04yh-27nCIKZZyCI9pulbgazMrf7Nz4Z8nNW0l4t2F53_Ym2li-5y2MZe-Xnme-JC6WLCjO7oqdmUaIEeolDPShwRYTPRTYfFIm3CPDoUSwz7t3Ycki7TXu1SRBYwHgedj03bV9OliuuoEnvhYvfxupnTESD5taDkmc67uD857Hn68L8oYQTpqvmBftugbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی کرابی (برسام) شامگاه ۲۱ دی‌ماه ۱۴۰۴ در منطقه سلسبیل تهران هدف شلیک مستقیم قرار گرفت و به کما رفت.
این جوان ۳۰ ساله که متولد سبزوار بود، بر اثر اصابت گلوله دچار مرگ مغزی شد و پس از یک هفته، در ۲۹ دی‌ماه ۱۴۰۴، در بیمارستان امام حسین تهران جان باخت.
پیکر او برای خاکسپاری به سبزوار منتقل شد.
ایران‌وایر مطلع شده است که به دلیل نقش بستن عنوان «جاویدنام» بر سنگ مزار او، مسئولان بنیاد شهید خانواده‌اش را تحت فشار قرار دادند تا این عنوان را به «شهید» تغییر دهند.
پس از آن‌که خانواده از پذیرش این خواسته خودداری کردند، سنگ مزار مجتبی کرابی (برسام) شکسته شد.
خانواده او نیز تصمیم گرفتند تا «روز آزادی» سنگی بر مزار این جوان کشته‌شده نگذارند.
مجتبی کرابی مربی بدنسازی، ورزشکار رشته فیتنس و داور رسمی پاورلیفتینگ بود.
یک منبع نزدیک به خانواده او به ایران‌وایر گفت: «مجتبی چند سال در کنار دایی‌اش، روح‌الله نصیری، از ورزشکاران نام‌آشنای خراسان رضوی، به‌صورت تجربی و آکادمیک آموزش دید و با تلاش و پشتکار توانست به‌عنوان مربی و داور رسمی پاورلیفتینگ، با مدرک معتبر، فعالیت حرفه‌ای خود را آغاز کند.»
او از هواداران تیم پرسپولیس بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76772" target="_blank">📅 16:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76771">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=oFlIU1DokYiToVQc2aXpy9duPBOIcDA1oTS6mQ_4lzbX9qyjmX17rrihJVBZnY1y5LdFl3p8stL-NqfRQPTNuMgICj8N-8VRdZa0t1XI-jVB_GZd3fiSPoxkdYrfOnIVk2i2v-j7e0unKKRGSK9wmCJRTDJFpgejGwhUM7YPujy3zqSTZLEMsYEiKlDOrYvcHrkmJfO7jNruT8vYt-iWc_sg2vaxIMMScsjrI4LuPbVFwMJ-TFUfV2ube1z1Vxz4I5bv27cAer80uSSABn6VVF3FvqGfhH6DDf2Vq5zK6vYeYpm6djOjFKPZ1-UitRDr4Ie9o6i2533v-QJdn75lxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2c3ad4afb.mp4?token=oFlIU1DokYiToVQc2aXpy9duPBOIcDA1oTS6mQ_4lzbX9qyjmX17rrihJVBZnY1y5LdFl3p8stL-NqfRQPTNuMgICj8N-8VRdZa0t1XI-jVB_GZd3fiSPoxkdYrfOnIVk2i2v-j7e0unKKRGSK9wmCJRTDJFpgejGwhUM7YPujy3zqSTZLEMsYEiKlDOrYvcHrkmJfO7jNruT8vYt-iWc_sg2vaxIMMScsjrI4LuPbVFwMJ-TFUfV2ube1z1Vxz4I5bv27cAer80uSSABn6VVF3FvqGfhH6DDf2Vq5zK6vYeYpm6djOjFKPZ1-UitRDr4Ie9o6i2533v-QJdn75lxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مجلس شورای اسلامی می‌گوید گزارش‌های منتشره دربارۀ موافقت با دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به سایت‌های هسته‌ای آسیب‌دیده «کذب است».
محمد باقر قالیباف در گفت‌وگویی تلویزیونی، که بخش دوم آن، شامگاه چهارشنبه ۱۰ تیر از تلویزیون رسمی جمهوری اسلامی پخش شد، با اشاره به قانون مصوب مجلس و مصوبۀ شورای عالی امنیت ملی جمهوری اسلامی، تأکید کرد که بر اساس قانون، «به هیچ عنوان دسترسی به سایت‌هایی که بمباران شده و آسیب دیده‌اند، داده نمی‌شود».
به گفتۀ مذاکره‌کنندۀ ارشد جمهوری اسلامی تعیین سطح دسترسی‌ها بر عهدۀ شورای عالی امنیت ملی‌ است و فراتر از آن، «هیچ امتیازی داده نخواهد شد».
محمدباقر قالیباف گفت بر اساس مصوبۀ شورای عالی امنیت ملی،‌ دسترسی بازرسان آژانس در حال حاضر به دو مورد نیروگاه هسته‌ای بوشهر و رآکتور تهران محدود است و به سایت دیگری دسترسی ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76771" target="_blank">📅 16:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f0mk-j8JIEm3_rMFCEvLSq1lGM8jGj4qsolb5sEdW2ov0FpYy2yg-Ily8lzvaPmPwldlRL0-V_vWhwHOIN91HOiKwCnmKZ8Gr_5HiC-mihNE-NWpyrM3F_GL-DuAILEezQyvAwefjkbNNd0s5K4QwUNkpPJHIvnVOCxVUgY-edp9w1j7GJS2ugHMoWL4Use-3Fi9UwZV3jVSeQa9_pTnnXSoujpdUL5HZUzoVjGokX6jLLmgTvKYvYLZEPCCcMWnR7uQb0AtjZBpNss3Kw9DwcX2yFJrhaqfld02L9TVqz20MFU7KbnEWFMMvl8sZXgtYlcU5_BGxM970olS120ILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ridaojfeGgG_IjqMOs60lAjQ8QKZaCGFTJYOD2f43HwD6XN1UyMha-NETa4ZysIKA4nH-VQXgIlea4d7sKg_YlRDUl0TA9khWLdx2XRRZkeI3DhAEI7RxRGpqmOoRvzNwMkDtnsNcP7Ohj5RNQvrqKRxom7Fog51tu9coHW2UEqh8CeCvSKR6A4SZm8Yd06Nq2x6hxpashdlzXnVXxPHG4gMDaFhFJNeNxuSFXs9RgkUbNl1qvD6-eQApc0TxhqZjTB9wDg7TfshMiLeVwtZ831NcwNuVwGb4AuQFlqvzHNogsVRAlIG49v-KGlgXT8unLWKxr3LNI5v4hPi_rbF3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع امنیتی عراق از وقوع یک حملۀ پهپادی به اردوگاه گروه‌های کرد مخالف جمهوری اسلامی در منطقۀ کوی‌سنجاق در شرق اربیل خبر می‌دهند.
هنوز جزئیاتی از این حادثه منتشر نشده، اما طی روزهای اخیر چند عضو سپاه پاسداران و نیروی انتظامی جمهوری اسلامی در استان‌های غربی ایران از جمله کردستان هدف حملاتی قرار گرفته و کشته یا زخمی شده بوده‌اند. یک گروه مسلح کرد هم مسئولیت برخی از این حملات را بر عهده گرفته بود.
مقام‌های امنیتی جمهوری اسلامی طی روزهای اخیر، بار دیگر از مقام‌های عراق و اقلیم کردستان خواسته بودند که به حضور گروه‌های کرد مسلح مخالف جمهوری اسلامی در خاک اقلیم کردستان پایان دهند.
سپاه پاسداران طی ماه‌های اخیر بارها با موشک و پهپاد به پایگاه‌های گروه‌های کرد در اقلیم کردستان و عمدتاً در اطراف اربیل حمله کرده است.
در همین حال خبرگزاری فارس به نقل از «منابع محلی» از وقوع چندین انفجار در اربیل و سلیمانیه، و از جمله هدف قرار گرفتن مقر «حزب آزادی» با موشک بالستیک خبر داده است.
@
VahidHeadline
درگیری‌های مسلحانه میان نیروهای سپاه پاسداران و گروه‌های مسلح مخالف جمهوری اسلامی در اطراف شهرهای سردشت و پیرانشهر، شامگاه چهارشنبه ۱۰ تیر و بامداد پنج‌شنبه ۱۱ تیر، ادامه یافت و به کشته شدن چندین نفر انجامید.
سازمان‌ حقوق بشری هانا اعلام کرد این درگیری‌ها در مناطق مرزی آذربایجان غربی رخ داده است.
رسانه‌های نزدیک به حزب دموکرات کردستان ایران نیز اعلام کردند در جریان درگیری عصر چهارشنبه در نزدیکی روستای «قزقاپان» در اطراف پیرانشهر، پنج عضو این حزب کشته شدند.
خبرگزاری فارس، نزدیک به سپاه پاسداران، بدون ارائه جزئیات اعلام کرد شش عضو حزب دموکرات کردستان ایران در این درگیری‌ها کشته شده‌اند.
کانال تلگرامی صابرین‌نیوز، نزدیک به نهادهای امنیتی جمهوری اسلامی، نیز مدعی شد در دو درگیری جداگانه، ۱۱ نفر از اعضای گروه‌های مسلح مخالف جمهوری اسلامی کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76769" target="_blank">📅 16:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/unWUyJiOSjM07f1qFIibsAIsuHfOFNfPhAKtwn-miMWprg4B6kZzhbVEUigwI_Lsm69YJhVKsI6W0U2ZVwiMSGFib_4O961YvNWHWU3O-l_ij8dPaxeJaC1oQz3nTf38VP0fCGWtpkb54nd8qC7TyTt-m7bpE4FnRuTvGh9K4b44htW_8PFBD9J7tT4Sw_SCMBaCfzap2xWD_j-2oX__7nQDNrihVp7WY7GdwFWIGfFRoPgaBBSahUCyFUy6s3A4sY4_2N6g286rjV1alF9BCjIlmtWbXTqUjbkzpNT2UcAoRzGCd4H8n5NrXwxiUZ_mVrStJvKpYSDkGMoM7x8lBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت کرمانی، وکیل دادگستری، از بازداشت دوبارهٔ سپیده کاشانی و هومن جوکار، دو فعال محیط زیست که پیشتر سال‌ها در زندان بودند، خبر داد.
آقای کرمانی به وب‌سایت «امتداد» گفت مأموران امنیتی عصر روز چهارشنبه دهم تیرماه با حضور در منزل این زوج، ضمن ضبط تمام وسایل الکترونیکی، آن‌ها را بازداشت کردند.
به گفته این وکیل دادگستری، نیروهای امنیتی همچنین سیما کاشانی، خواهر سپیده کاشانی را نیز بازداشت کرده‌اند.
او افزود تاکنون مشخص نیست این افراد توسط کدام نهاد امنیتی بازداشت شده‌اند و با توجه به تعطیلات پیش‌رو و بسته بودن مراکز قضایی، نگرانی خانواده‌های آن‌ها افزایش یافته است.
از دلایل بازداشت این زوج گزارشی منتشر نشده است.
سپیده کاشانی و هومن جوکار از اعضای مؤسسه «حیات وحش پارسیان» هستند که به همراه چند فعال دیگر محیط زیست زمستان سال ۱۳۹۶ توسط اطلاعات سپاه بازداشت شدند.
کاووس سیدامامی از بازداشت شدگان این پرونده که تابعیت کانادا را هم داشت، چند روز پس از بازداشت، به طرزی مشکوک در زندان اوین جان خود را از دست داد و مدتی بعد سازمان اطلاعات سپاه پاسداران دیگر فعالان محیط زیست بازداشت شده را به «جاسوسی» و «همکاری با دول متخاصم» متهم کرد.
سپیده کاشانی در طی سال‌های زندان در نامه‌هایی اعلام کرد که در دوره بازداشت تحت «شدیدترین شکنجه‌های روحی و روانی، تهدید به شکنجه فیزیکی و تهدیدهای جنسی» و «تهدید به مرگ» قرار گرفته‌اند.
او در نامه خود نوشته بود که بازجویان این پرونده «ویدئوی جسد» کاووس سید امامی را برای شکنجه به او نشان داده‌اند، و همسرش، هومن جوکار، را برای تهدید و شکنجه به پای چوبه دار ساختگی بردند.
سپیده کاشانی و هومن جوکار پس از سال‌ها زندان، در فروردین ۱۴۰۳ در پی عفو از زندان آزاد شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76768" target="_blank">📅 16:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=AMBVubdQrNB4ZJeodH9Me7eNRUZ-7EJgzxthwg_tYYG-f7dateYm2_oayTBRtUzHYFrjCAXUM-VNBN1G26KIANS0_Mzya-6nSjbkE_1HOFRKNk_tnQt-wkfe3P6V1A9iuc4bJJAD0hHMwmVpFPCEFCgT3JYmV3BDHUDlcirAo5QWYW8i9876FXQcMr_0W5DsFNwpYtHEsuFVHg2QFwAwpWnQgfNvBicopO8dtAP9a-Zqq3AlqLWH7zVGl-DZv2sKtYWScw1BEdJ9beC6TvgavAey4wvAF9HWxwAp4uAOs7YDZEpCzMqYWNO-FUW7JcWKMsXL7BetnWfxFdyLhLErIg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cccd78df1b.mp4?token=AMBVubdQrNB4ZJeodH9Me7eNRUZ-7EJgzxthwg_tYYG-f7dateYm2_oayTBRtUzHYFrjCAXUM-VNBN1G26KIANS0_Mzya-6nSjbkE_1HOFRKNk_tnQt-wkfe3P6V1A9iuc4bJJAD0hHMwmVpFPCEFCgT3JYmV3BDHUDlcirAo5QWYW8i9876FXQcMr_0W5DsFNwpYtHEsuFVHg2QFwAwpWnQgfNvBicopO8dtAP9a-Zqq3AlqLWH7zVGl-DZv2sKtYWScw1BEdJ9beC6TvgavAey4wvAF9HWxwAp4uAOs7YDZEpCzMqYWNO-FUW7JcWKMsXL7BetnWfxFdyLhLErIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامرضا نوری قزلجه،‌ ؛وزیر جهاد کشاورزی"، با تایید سخنان محمدباقر قالیباف دربارۀ خرید محصولات کشاورزی از شرکت‌های آمریکایی  در دوران ریاست‌جمهوری ابراهیم رئیسی گفت: برخی از قراردادهای کشاورزی از طریق منابع ارزی بلوکه شده ناشی از تحریم‌ها بود و آن‌ها نیز به شرکت‌های آمریکایی مجوز می‌دادند و از آن‌ها خرید می‌شد.
محمدباقر قالیباف شامگاه سه‌شنبه در یک گفت‌وگوی تلویزیونی به خرید محصولات کشاورزی از شرکت‌های آمریکایی در دولت ابراهیم رئیسی اشاره کرده بود. پخش سخنان مذاکره‌کننده ارشد جمهوری اسلامی در همین زمان از سوی تلویزیون حکومتی متوقف شد.
رئیس‌جمهور آمریکا روز دوشنبه اول تیرماه در گفت‌وگو با خبرنگاران در کاخ سفید در مورد آزادسازی دارایی‌های ایران که در تفاهمنامه جدید به آن اشاره شده، گفته بود:
پولی که آزاد می‌شود قرار است برای خرید مواد غذایی استفاده شود... آن هم صرفاً از طریق ایالات متحده و از کشاورزان ما.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76767" target="_blank">📅 18:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FKPVz94N162d4-n-ABIOroBs10scJj0ZIeZTiWab3hFK2Ok-Yq6U_LmR2wemxLqdmsChNnJ0zqd0zsL--b9LreBmG7_UE4OdA6iXEVhW6NwP3TXHB4K5zBFn4By_6RwD0T5Sxx4TJ11cEaas3huy_f8yGazWB3_wFUJOS_Ljggy3vDe--GsIbIcpqmnlmnIduYi-GyOElxy6W3PkRt4bH0ASw-X7NdjKRUTgFzutn_Kb0QssZspBfozY6JWcvx9SpbG1eUCJJvAu8EnnZe8CytsYlBmg8gp3YgzqBSttXcgejMKog-okpvm19mm_IudbdkJ_4rqQJbl1DumhzR_NJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PhVX24nPhL7z3ACkJnkuPJzR697gXJb-a6Ohe2KACn_U2pYMESJ5_AfJW5JMVtWAK2ZC410HgE5SJ3ycH1ZAk7lPrbHo6TKMUn8InfpxqcguB3N4gqxN3Y4xe7bZPw5upL1DRFILwl2rCkuszkywLVbYhGndKaB0fK5tZ2TPCmKds2AXzneOt0kBat9lxqv7z2Oymvu8xEXAW3qRFbr4yqT4-98BzYovc_kHlFSCs0korlZT3QizmW7YH4qAvuqeUDe6v60K96CejJB4LeIZi32JyMYuKYM4vYJb4ybHqt2ZXzdjA_bsKzR5o8RbRnhMJ2rLSh84h-8kWPCJH4VZsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس‌جمهور آمریکا روز چهارشنبه ۱۰ تیرماه از روند مذاکرات ابراز رضایت کرد و گفت این روند «بسیار خوب» پیش می‌رود.
دونالد ترامپ که در واشینگتن با خبرنگاران صحبت می‌کرد، افزود که آمریکا چند روز پیش حملات شدیدی به ایران انجام داد، اما نشست‌های اخیر دو طرف در قطر به‌خوبی برگزار شده است.
او همچنین اعلام کرد: «روند خلع‌سلاح هسته‌ای ایران به‌خوبی در حال پیشرفت است».
ترامپ افزود: «آن‌ها نشست‌های بسیار خوبی داشته‌اند و باید ببینیم چه خواهد شد».
این اظهارنظر ساعاتی پس از آن بود که رسانه‌ها از برگزاری «مذاکرات فنی» غیرمستقیم ایران و آمریکا در روز چهارشنبه در دوحه، پایتخت قطر، خبر دادند.
این مذاکرات با میانجی‌گری پاکستان و قطر برای اجرای تفاهم‌نامهٔ اخیر میان ایران و آمریکا انجام می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76765" target="_blank">📅 17:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MkujWuF7A_HvpwCAAwGdCwuxCEscVzRJPpnOH5xzTnP8L5TK6h4g3RbIvf6ms7dI2RInyyMmPeFm0h3ZtcdW4v9W6zgdHT0DIDm98KxskAl7BquheZ6GfBYk5z-Kin8Kj3YWr5zi0pmOZCAwFFQDu5CmH1jQU0qfxKNcC10wHd8LewlijpuTgm53-b8qAnkdY5guMVS-HNQ2Jx-0c55Ig8eVOb0FuuOLbPQxg_wu5fnKPIj8k5XtBikoHs0pBJWcuqploED3onfS6xLkjLp19huJTXHgcKfXcCVdE3CmXd26gzc8S1p-cRNDmbL80vp27AiqQKOf-Q1ag2V5P6aHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YYe36IqHTioUJnKsabddHmZgf-YLbMrApYpvje_ThMB7ZIZZz4ui2ZOEJv7pqPRlv50ctMqa52VQ9R5xlmYoSyTuA5QL_9canEVfwJeQZqIvrIJ-8nbQRLOwkEwoC7UFRIk3DtFrVMBjClH51srTr4ZSUmXLy6lVzMVc_AkhLtFgPvNOZtXaVbZfx4_Irx8zZ-vlBiq7qExLKZgtiXUONwgKABtZfxRdkwm1cwM7kV4e546CfAK2gByLCBBONQSyrNhjqoxE9FjsKQ_u7xHe-CVakmilqmYF58y_QEeKnsWTibwIUXMg_m9xs46V2tssBePXPFLnib612wZ6cjGNrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی که برای شرکت در نشست‌های مرتبط با اجرای تفاهم‌نامه ایران و آمریکا به دوحه سفر کرده است، اعلام کرد کارگروه‌های پیگیری اجرای تفاهم‌نامه و نیز مذاکره برای دستیابی به توافق نهایی تشکیل شده‌ اما هنوز مذاکرات در این قالب آغاز نشده است.
کاظم غریب‌آبادی بعدازظهر چهارشنبه دهم تیرماه، پس از دیدار با شیخ محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، به خبرنگاران گفت رایزنی‌ها برای تعیین زمان و محل آغاز مذاکرات از طریق میانجی‌‌ها ادامه دارد و در صورت فراهم شدن شرایط لازم، این گفت‌وگوها آغاز خواهد شد.
به گزارش خبرگزاری ایسنا، پس از این دیدار نیز نشست سه‌جانبهٔ مذاکره‌کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای تفاهم‌نامه برگزار شد.
@
VahidHeadline
دیوان امیری قطر چهارشنبه در بیانیه‌ای اعلام کرد تمیم بن حمد آل ثانی، امیر قطر، در کاخ لوسیل با استیو ویتکاف و جرد کوشنر، فرستادگان آمریکا، دیدار کرد.
در این دیدار، آخرین تحولات منطقه، به‌ویژه روند مذاکرات میان آمریکا و جمهوری اسلامی در چارچوب یادداشت تفاهم دو طرف، و همچنین وضعیت لبنان بررسی شد. دو طرف بر اهمیت تثبیت آتش‌بس به‌گونه‌ای که وحدت، حاکمیت و ثبات لبنان حفظ شود، تاکید کردند.
در این بیانیه آمده است که امیر قطر بر ادامه تلاش‌های میانجی‌گرانه این کشور با مشارکت پاکستان و حمایت از همه مسیرهای گفت‌وگوهای ناشی از یادداشت تفاهم تا دستیابی به توافقی جامع و پایدار که امنیت منطقه و صلح بین‌المللی را تقویت کند، تاکید کرد.
دو فرستاده آمریکایی نیز از نقش قطر و پاکستان در پیشبرد مذاکرات و نزدیک کردن دیدگاه‌ها قدردانی کردند و بر تعهد آمریکا به ادامه روند مذاکرات و تلاش‌های دیپلماتیک برای دستیابی به توافقی جامع تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76763" target="_blank">📅 17:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rrjjyC9mjzNoYV9AqN4B4Fd4MDVPhcmaGqtT_HfICTTi8A1k4kI0ofiyxgz_XYnfrUL7082IRpMR4KDmQ22fywe_mOiQN1Mwzj7rXha0YvsZ8nsOZ1mmQ2Es7Avwh7UF_WSvIZwY5BDb8TVXcm7vD2pk9kRD7OsmpYq3h3hacm6DjoEvxfSmebfeJedslYcSBtOd7z7TiqBc0CE6f6ZQT2JOjjTHS4Y9E2i31M8rYY5GdBybySAJ5LL8hQc5MHqYTMl8y7Lx3W5_ZlY3wF56Q5UDcvlU5QW9YNx7ctVe6_ceyGFJ7tSs_3dYVgbrTRByn-uTdl8c3mx_xZ06z4ZdlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با ادامه برخوردهای قضایی و امنیتی با فعالان صنفی فرهنگیان، سه معلم  با احکام زندان و مجازات‌های تکمیلی روبه‌رو شدند و یک فعال صنفی دیگر نیز در استان فارس بازداشت شد.
بر اساس گزارش شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران، احمد علیزاده، معلم بازنشسته و فعال مدنی اهل آبدانان، از سوی دادگاه انقلاب ایلام به دو سال حبس تعزیری، یک سال ممنوعیت خروج از کشور، ابطال گذرنامه و یک‌هزار و ۸۰ ساعت خدمات عمومی رایگان محکوم شده است.
هم‌زمان، آزاده سالکی، معلم شاغل در شهرستان خواف و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، به پنج سال حبس محکوم شده است. بر اساس خبر منتشر شده، حکم اولیه او ۱۰ سال زندان بود که در مرحله تجدیدنظر به پنج سال کاهش یافت.
آزاده سالکی پس از بازداشت در دی‌ماه ۱۴۰۴، حدود یک ماه در بازداشت به سر برد و سپس با تودیع وثیقه سه میلیارد تومانی به‌طور موقت آزاد شد. گزارش‌ها همچنین حاکی است اجرای این حکم می‌تواند به اخراج او از آموزش و پرورش منجر شود.
این معلم پیش‌تر نیز در سال ۱۴۰۱، زمانی که در شهرستان تربت حیدریه مشغول تدریس بود، به دلیل فعالیت‌های صنفی و اظهاراتش در کلاس درس، به مدت یک ماه از کار تعلیق و سپس به شهرستان خواف منتقل شده بود.
همچنین جان‌محمد احمدی، معلم بازنشسته و رییس انجمن صنفی معلمان نورآباد ممسنی، روز سه‌شنبه ۹ تیرماه توسط نیروهای امنیتی بازداشت شد. تاکنون اطلاعاتی درباره محل نگهداری، نهاد بازداشت‌کننده یا اتهام‌های منتسب به او منتشر نشده است.
آریا نورانی، معلم رسمی آموزش و پرورش در شهرستان مانه خراسان شمالی، نیز در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ به ۱۴ ماه حبس محکوم شد.
شورای هماهنگی تشکل‌های صنفی فرهنگیان ایران با محکوم کردن این اقدامات، خواستار آزادی بازداشت‌شدگان، لغو احکام صادرشده و پایان دادن به برخوردهای قضایی و امنیتی با فعالان صنفی شده است.
در ماه‌های اخیر نیز روند برخورد با فعالان صنفی معلمان تشدید شده است. پیش‌تر شعبه سوم دادگاه انقلاب اهواز پنج فعال صنفی فرهنگی و کارگری خوزستان را به سه سال حبس تعلیقی و دو سال ممنوع‌الخروجی محکوم کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76762" target="_blank">📅 17:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uUXcNKDOEQd5PvFIV9UhgKK8UUhpaEAFs7D8_Jq-jzOG4ZN6mxZbQMXcHWsejh50AsPgSbGpXZbOXyQzW-GN6V6ngVrbOOMDrrnLqKH2uveifiR8hlJ7gmBA6wSdok1Vqj2WkBRamwslZd4ryToaOW0rMp2Kb5w8IjTjxJZWK3EtlmBlNA6753s0fdyZjAJCaW2HfewAkMAVYTEKrYxJzTXN3FgTqOJJs4bJE4gM2bMaDFj-ZyLO9gqdCwDVBmgbqPTWfkoPcongXWGN5Mzlrpy1xYV0btYkvbPGSG1VnUoA_Vl9cWL3sMRCA3h_eIKtqe93Ir6l73is9wETZrBCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون رییس‌جمهور آمریکا با انتقاد از منتقدان که خواهان حملات بیشتر به جمهوری اسلامی هستند، در یک برنامه تلویزیونی گفت: «دیدگاه آن‌ها این است که فقط بمب بریزید، باز هم بمب بریزید؛ اما واقعا نمی‌توانند توضیح دهند که هدف نهایی از این کار چیست.»
او افزود: «اما چیزی که رییس‌جمهور [ترامپ] می‌گوید این است حاضرم دستور حملات هوایی بدهم، و به‌وضوح هم نشان داده که در صورت لزوم این کار را انجام می‌دهد، اما فقط زمانی که این اقدام در راستای دستیابی به یک هدف مشخص باشد.»
او در بخش دیگری از اظهاراتش گفت: «یکی از چیزهایی که درباره ایرانی‌ها برایم هم جالب و هم آزاردهنده است این است که می‌گویند نه، هیچ گفت‌وگوی صلحی در جریان نیست، اما در همان حال مذاکرات فنی میان واشینگتن و تهران درباره توافق صلح در حال انجام است. این یک تاکتیک مذاکره یا شگرد ایرانی است که من آن را درک نمی‌کنم.»
@
VahidOOnLine
جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا در مصاحبه‌ای با شبکه خبری فاکس گفته است «ایالات متحده در رابطه با ایران در موقعیت بسیار خوبی قرار دارد.»
او گفت: «ایرانی‌ها در هفته‌های گذشته، هیچ نفت‌کشی را هدف قرار ندادند و جریان نفت در تنگه هرمز برقرار است؛ بخشی از آن به این دلیل که رئیس‌جمهور(ترامپ) تصریح کرد که اگر ایرانی‌ها به کشتی‌ها حمله کنند ما مقابله به مثل می‌کنیم.»
آقای ونس همچنین گفت: «اگر مذاکرات موفقیت‌آمیز باشد که ما می‌خواهیم موفقیت‌آمیز باشد، شما ایرانی را خواهید دید که بطور دائمی متحول شده؛ تروریسم منطقه‌ای و بی‌ثباتی را تامین مالی نمی‌کند و جاه‌طلبی‌های هسته‌ای را بطور دائمی کنار می‌گذارد و درنتیجه اقتصاد جهانی دوباره از آن استقبال می‌کند. این نتیجه خوبی برای مردم آمریکا و کل منطقه است.»
او همچنین گفت:«از سوی دیگر اگر آنها رفتار مناسبی نداشته باشند و امتیازاتی را که ما می‌خواهیم ببینیم ندهند، هنوز برنامه هسته‌ای آنها نابود شده، توان متعارف نظامی نابود شده و آمریکا در مقایسه با آنها در وضعیت قوی‌تریست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76761" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=hdcdcIe1XU_59RzpqirTLzedm9Ssb4rIwuJHwV83Z3IoQjjqXMgJfd_EByo_5gvMWXPfK3BaQqq5uno7s4Imr5FiQlqaTw9ml_PW8v6evaGMZ2Ii2wdDNKaBmsyKwWEKKmg0t-hBN0sa1HID-rJOe503VKfhwnff17FuFwmBaJChQgpIJebThieSQAynZQPn-Cnn2bEghG6bOWyKpHQs_aGBbnymP3-e6J5p2wH9tGqAVEDRdcsgmDAlg1XZFBqba5A-KCO3KBmXDzQQw46EEak-cGcSBKB2EuBfNzRy7McnVGuhVZitR8PiqdwtrcmGzPbd9G_YCgHQSMCa7EdGbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/150c916f8f.mp4?token=hdcdcIe1XU_59RzpqirTLzedm9Ssb4rIwuJHwV83Z3IoQjjqXMgJfd_EByo_5gvMWXPfK3BaQqq5uno7s4Imr5FiQlqaTw9ml_PW8v6evaGMZ2Ii2wdDNKaBmsyKwWEKKmg0t-hBN0sa1HID-rJOe503VKfhwnff17FuFwmBaJChQgpIJebThieSQAynZQPn-Cnn2bEghG6bOWyKpHQs_aGBbnymP3-e6J5p2wH9tGqAVEDRdcsgmDAlg1XZFBqba5A-KCO3KBmXDzQQw46EEak-cGcSBKB2EuBfNzRy7McnVGuhVZitR8PiqdwtrcmGzPbd9G_YCgHQSMCa7EdGbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی، شامگاه سه‌شنبه اعلام کرد در حال حاضر «اصلا مذاکره‌ای با آمریکا نداریم».
او در گفت‌وگویی با تلویزیون حکومتی ایران محاصره دریایی آمریکا علیه بنادر ایران را که بعد از آتش‌بس و از فروردین‌ماه آغاز شد، «شدیدترین نوع جنگ» خواند که به گفته او «مردم و نان مردم» را محاصره کرده بود.
قالیباف افزود که برداشته شدن این محاصره «از موفقیت‌های بزرگ» تفاهم‌نامه امضا شده بین ایران و آمریکا بود.
او اعلام کرد که مذاکرات فقط تا زمان امضای یادداشت تفاهم ادامه داشت و سفر به سوئیس برای گفت‌وگو درباره «اجرای بندهای» همین تفاهم‌نامه بود که ۲۵ خرداد بین ایران و آمریکا امضا شد.
@
VahidHeadline
قالیباف با طرح ادعای تسلط ایران بر تنگه هرمز در پی جنگ ۴۰ روزه هشدار داد که «نباید تنگه را به ضد خودش تبدیل کنیم».
او افزود: «تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود، نه کمتر.»
@
VahidHeadline
پس از  آن که مصاحبه تلویزیونی محمدباقر قالیباف درباره جنگ، تنگه هرمز و مذاکرات با آمریکا، در میانه آن به طور ناگهانی قطع شد، مرکز رسانه‌ای مجلس شورای اسلامی اطلاعیه‌ای به رسانه‌های داخل این کشور فرستاده و به این موضوع اعتراض کرده است.
در اطلاعیه مرکز رسانه‌ای مجلس آمده است: «به اطلاع هم‌وطنان عزیز می‌رساند در راستای اجرای امر رهبری معظم انقلاب مبنی بر پیگیری شروط مشخص شده در یادداشت تفاهم اسلام آباد، جناب آقای دکتر قالیباف، رئیس قوه مقننه و رئیس هیئت مذاکره‌کننده کشورمان برای ارائه گزارش به مردم، گفتگویی تبیینی را طبق هماهنگی با سازمان صداوسیما انجام دادند که این گفتگو بیش از ۲ ساعت قبل از زمان پخش به آن سازمان تحویل داده شد؛ اما متاسفانه پخش این گفتگو از میانه آن متوقف شد».
در ادامه این اطلاعیه امده است: «این در حالی است که این گفتگو به شکل ضبطی بوده و کمترین وظیفه مسئولین سازمان صداوسیما این بود که اگر خلاف رویه ها تصمیم به عدم پخش بخشی از گفتگو داشتند، آن را با این مرکز هماهنگ می کردند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76759" target="_blank">📅 00:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0ioFY3oBy9VwtrDW7xE0EvIRzUAzIRS7tDWYAc-UVbA190YNMXsYA53X6UMZJ_d-EEAcGi6DA5C6bnOhgLQ0p_tRZeh6yN2BFTo1bGk2a8OD_lUYO1_cgJaBdCMEn7Ny1vGJZZCa5WJYBd3hE-YvaSFhPtMzC7pEC9g0rASUn9yMbcoUjAa6LW90uNB5u1sCpiRJM7f3Dsuna3vMp6iMGBOkX8Mx5euwi0HNwLRBKhALwZnT5Oos4pXKPtD5BcQGPpWw7zasT4VmreJ7SkFow7Cl32conn-nVsj1jkbLwu21fuaD70NR9snODoD0BRz_i002eS1UUdRIW7kJBy_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌دیوان عالی آمریکا تلاش دونالد ترامپ، رئیس جمهور، برای لغو اعطای خودکار تابعیت به کودکانی که از والدین مهاجر فاقد مدارک قانونی در خاک آمریکا متولد می‌شوند را رد کرد.
آقای ترامپ و تیم حقوقی او تفسیری از قانون را درخصوص این اعطای تابعیت مطرح کرده بودند که تا همین اواخر هم در میان سیاست‌گذاران و کارشناسان حقوقی، حمایت چندانی نداشت وتوانستند آن را دیوان عالی آمریکا یعنی عالی‌ترین مرجع قضایی کشور برسانند.
با این حال، در نهایت اکثریت ۹ قاضی دیوان عالی حاضر نشدند سابقه قضایی ۱۵۰ ساله را کنار بگذارند و یا قوانین فدرال دیرینه و متن قانون اساسی آمریکا را به گونه‌ای جدید تفسیر کنند تا به نفع آقای ترامپ رأی صادر شود.
این شکست احتمالا برای آقای ترامپ ناامیدکننده خواهد بود و او را وادار می‌کند به دنبال راه‌های دیگری برای محدود کردن ورود مهاجران فاقد مدارک قانونی به آمریکا باشد؛ زیرا اگر این افراد هرگز به خاک آمریکا نرسند، موضوع اعطای تابعیت به فرزندانشان نیز اساسا مطرح نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/76758" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzF9NRIb5JPOGQC8dPdn2hFvq39z3znT3_p5OVzVbSr7JSyJwfeyiw-gJjPxKepl6Fo4rRTsOgarpbkXJp4xVaBHHspd4aBPh3SaRUwaKNEyuYituKp6qGV6t6_2zsMni5K2w2oaACJXkJyNQEFjdvOHhp_n3RDW-5Dfbn7VKFkCVXOUJCFxnqsSmkt518ATNii9UjWhiC-HPMu59T1c0B0yOKpx25253nYd6qc9HtB-o06En9K0bDRu_UEFW9fNQBdUyWtPRko25mqQSb-qS9dhQs-X1OzIytYFKA5k6tzzSKwPXuQT_1jBqEVG5g-6v_u1G-x3qtkKbS38By36pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه قطر، اعلام کرد استیو ویتکاف، فرستاده ویژه دونالد ترامپ در امور خاورمیانه، و جرد کوشنر، مشاور ارشد و داماد رییس‌جمهور آمریکا، روز سه‌شنبه برای گفت‌وگو با مقام‌ها و میانجی‌های قطری وارد دوحه شده‌اند.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، گفت این دیدارها با هدف بررسی «تمامی مسائل منطقه‌ای» انجام می‌شود و موضوعاتی از جمله روند مذاکرات با ایران و همچنین لبنان را در بر می‌گیرد.
او با این حال تاکید کرد که ویتکاف و کوشنر برای مذاکره با هیات ایرانی به دوحه سفر نکرده‌اند و برنامه‌ای برای دیدار با نمایندگان تهران ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76757" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMNlmARnhDXHvvWCUlt2pTE4xXSvXv642IgafjsmCJIdR_YyNZBbxBpFo8MfYccl96VReilD8BvbcNTVNlpUhsfOJLOTzkyt6AM9UlImcMQWVZftd9MaIuG26ch4fcOaJtzCnOvzW3tTTXwlWX7aUNskIqyuAGHEVmXHBCyq2LoGAA3q7qC703q6CQnd045Ty09gCR-ykvabXEwd6jEsnvKndPn58Z9LQBR_3gFFt2hfd4aIKXBC2vwo3nkcvBbfXgp-CVi3GSVnEqPdQ2hGKjMCa3wySu_cvnPq0iLztzD94BuKty3cYEkB77Z866FtRGhN_87MP5pVq9muCFTvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه به نقل از چند منبع گزارش داد جمهوری اسلامی تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدودشده خود را دریافت خواهد کرد.
پیش‌تر سخنگوی وزارت خارجه قطر گفت تاکنون ۶ میلیارد دلار از دارایی‌های مسدودشده جمهوری اسلامی به ایران منتقل نشده است.
محمدجعفر قائم‌پناه، معاون اجرایی مسعود پزشکیان، نیز با اشاره به متن تفاهم‌نامه با آمریکا، گفت که چند میلیارد دلار به حساب جمهوری اسلامی در یکی از کشورهای خلیج فارس نشسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76756" target="_blank">📅 19:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/onAfyCECQPx96HWkkgztLUlhvznp4wpKuf52Sn6fa3i1hQMVlGrW7avMseFG2ttkaoYLHf0RV2rJ5TMN_R1ODNWSo4TzFNszyxOBCwg1M98hxIIna5QS3oKdOBAqC2seTKgX96UBOG2eRZCZ2U97PRAeLAJPXM08OLP3d9dF_6kzQ8umAT_0chiK4nLNAQ4_SEYmYte3eWZSsTXUbM2nEoEgawI6j4Syx0LxydLj5bauJiPCjn7QlgrD44WCHmXoHTHqCrqYOJawMHdtPUPKCiVfyM6yBTfYgfCv6euPAFsUbSxQ1Ikko-gbOeKrZOgnk2YIe83r7T5MRlx3GzpMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ne1nmuJi0Ii2EeInLMixBPPgiyrw1PCVvidkICFb5iVnaYD2EZLNEr2D1dtJAubwCUqO521e_6i9cvOwdcyph0DOzknnah5FXC1RDRLkfLmPFtv759-1kOgJ2gKJs1CmGggg1rVk4GFQ8VTUh-bh6IzJApwP9MIv_QABf1oPWCi9ureiPy9dCENa0LbbpQul01P8FjUy1BI4qPGL3up60SH4eU70J2Wxz5aBLwEsiBgYEBfbQwJ4CPsDI_YY-KiSG8GrUJYYwVFrr0-7QinMycNd2LsJdmdwJ-bbFwbMxIiLrH0ZvqbF7_k1DTvdfP98jCoaodSBREj9VFsT99PfZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاون اجرایی مسعود پزشکیان تأیید کرد که فرماندهان نظامی عضو شورای عالی امنیت ملی ایران و دو نمایندهٔ رهبر جمهوری اسلامی در این شورا نیز به تفاهم‌نامهٔ ایران و آمریکا رأی مثبت داده‌اند.
محمدجعفر قائم‌پناه روز سه‌شنبه نهم تیرماه اعلام کرد در جلسهٔ‌ شعام برای بررسی این تفاهم‌نامه، رئیس‌جمهور، رؤسای مجلس و قوه قضائیه، جانشین رئیس ستاد کل نیروهای مسلح، وزیر کشور، رئیس سازمان برنامه و بودجه، وزیر خارجه، فرمانده کل سپاه پاسداران، فرمانده ارتش، و دو نماینده رهبر جمهوری اسلامی در شورا،
یعنی سعید جلیلی و محمدباقر ذوالقدر، به این توافق رأی مثبت دادند.
او این را هم تأیید کرد که مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده بود جلسهٔ شورای عالی امنیت ملی با حضور فرماندهان ارشد نظامی برگزار شود و در صورت رأی موافق سه‌چهارم اعضا تفاهم‌نامه پذیرفته شود.
اظهارات معاون اجرایی رئیس‌جمهور در حالی مطرح می‌شود که در روزهای گذشته، پس از انتشار پیام مکتوب مجتبی خامنه‌ای دربارهٔ تفاهم‌نامه، برخی چهره‌های مخالف مذاکرات از سعید جلیلی به‌عنوان «تنها مخالف» تفاهم‌نامه نام برده بودند.
@
VahidHeadline
به گفته معاون اجرایی رییس‌جمهوری، اعضای موافق این تفاهم عبارت بودند از: مسعود پزشکیان، رییس‌جمهوری، محمدباقر قالیباف، رییس مجلس، غلامحسین محسنی اژه‌ای، رییس قوه قضاییه، رییس ستاد کل نیروهای مسلح (که نام او پس از کشته شدن عبدالرحیم موسوی هنوز به‌طور رسمی اعلام نشده است)، اسکندر مومنی، وزیر کشور، حمید پورمحمدی، رییس سازمان برنامه و بودجه، عباس عراقچی، وزیر امور خارجه، فرمانده کل سپاه پاسداران (که نام او نیز تاکنون به‌طور رسمی اعلام نشده)، امیر حاتمی، فرمانده کل ارتش و دو نماینده رهبر جمهوری اسلامی در شورای عالی امنیت ملی.
قائم‌پناه همچنین از منتقدان داخلی تفاهم‌نامه انتقاد کرد و گفت کسانی که به این توافق رای مثبت داده‌اند، «کمتر از فرماندهان شهید نیستند» و نباید جایگاه یا صلاحیت آنان زیر سؤال برود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76754" target="_blank">📅 16:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLpU6pZmSSJniQdNerbfPyUczo67LkIVB_Vr6IV3tUlB83VnzAsRmNrspNncBzPBkvaz2amilRj9jUKHoEX67IRquP6R0kjGRsXI1j_AYxuDTMmQz6uvwWLK5Tw3NNWU3Z3xYE5eieSct6GhoJb4DwXRZnwaSPaH0Q-KNNXVrwq97X8jpmw8QD5joKkwwdAK_4STtoTKPJzY-vxE5hHQX5PJO2_Pw2JuINrFw9L5grvxdndoThDeuCsAW2t0Z8wTliuXMB_qOAj2tcHbFSIpOFC76K2kUXirsw95VQhmmaIzL6AvwC1QSKE6uptoUhlO5bwpCNbrdJWWJU2ddTMkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این تصویر، محمدرضا شاه پهلوی در جریان بازدید از بانک ملی ایران، با یوسف خوش‌کیش، رئیس وقت بانک ملی، گفت‌وگو می‌کند.
خوش‌کیش بعدها ریاست بانک مرکزی ایران را عهده‌دار شد و آخرین رئیس‌کل بانک مرکزی پیش از انقلاب ۱۳۵۷ بود.
پس از انقلاب، خوش کیش بازداشت شد و تنها طی سه روز محاکمه، با اتهاماتی از جمله «ثابت نگه داشتن ارزش ریال در برابر دلار آمریکا به مدت پنج سال»، به اعدام محکوم شد و بامداد ۲۴ مرداد ۱۳۵۹ تیرباران گردید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76753" target="_blank">📅 16:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76752">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9hXw4HCIydTdr0zC4qivVnad_Y2ISKv4K2Lb0qtK_6vnAmU_5dpao3mxbS1ufx6pFFdQG5ksYEM6DYO_bXLIu6bBlY7YLiubS_NjhXgvwFVjB5Onm_aqeNCnNcUcy51ryeQv_qzcRKgeO0ctuOuj-ViuVIfj6XDrIdCpplJIbskwDtRoGEQyXN3vsfOQabTk2zAVT5KHQ64MMxyHfn-ZNHY6LJz_wHgWiOKjndQlICgKt9Fua3PNeHFB7Cqgv8OR_MQWuTvWCLqUQGmZYSKg9VT0Lxb7xg0LMljaHwCIGDVWci4RsReB9rwWm9dOLbpszs9bkE4qes7Pyq5KmVMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان مخالفان داخلی تفاهم‌نامهٔ ایران و آمریکا را به «همسویی با عملیات رسانه‌های معاند» متهم کرد و گفت «تمامی مراحل مذاکرات» با «هماهنگی کامل و مستمر» با رهبر جمهوری اسلامی انجام شده است.
رئیس‌جمهور ایران که روز سه‌شنبه ۹ تیر در دیدار با اعضای جامعه مدرسین حوزه علمیه قم همچنین گفت: «با وجود محدودیت‌ها و ملاحظات امنیتی موجود، متن نهایی توافق پس از بررسی‌های کارشناسی و امنیتی در مراجع ذی‌صلاح مورد ارزیابی قرار گرفت و در شورای عالی امنیت ملی نیز از حمایت قاطع اعضا برخوردار شد.»
این در حالی است که در روزهای اخیر مخالفت برخی طیف‌های سیاسی طرفدار حکومت با تفاهم‌نامه بالا گرفته و می‌گویند دولت، محمدباقر قالیباف، رئیس هیئت مذاکره‌کنندگان، و حتی برخی فرماندهان ارشد سپاه برخلاف نظر مجتبی خامنه‌ای این تفاهم‌نامه را تصویب کرده و پیش برده‌اند.
مسعود پزشکیان این دسته از مخالفان «جریان‌های همسو با عملیات روانی رسانه‌ّای معاند» خواند و گفت: «این‌ها تلاش می‌کنند با تخریب تیم مذاکره‌کننده و زیر سؤال بردن تصمیمات ملی، زمینهٔ تضعیف این دستاورد را فراهم کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76752" target="_blank">📅 16:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76751">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgVcZ51KzBYcCJPqaxs-kjXm_fR---s84q2AVCfj1HyPLnPT_YlSaXM9I9mNz-oqj3UNswaCq2Ixg0N9tMj3aPClLm5ILF6xo7aoHVltwILNTKIw5ZfF2X87wZoNyGiElBJPjAGKoGQgUBk6kSgcfBsIoYJdYPXrHD2AaPBH1nudf7k1fn1kf4dexiVdsaiApkew67Juz_by5RPvHu7XBy41eKCmdEIDyhBKp1SVIVz0vKWp7UihVmAKoeTfLryJGIt-VeO3h2xt7iSHI0wdQ9Ueal4p4eOi6dRnh1ehyY8PattrgESp-GPp0l_bkWpyVOL80EyCadLtFdCQB8-xlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۴ روز از آغاز اختلال در شبکه خدمات برخی از بانک‌های کشور از جمله بانک‌های صادرات، تجارت، ملی و توسعه صادرات می‌گذرد؛ اختلالی که همچنان به‌طور کامل برطرف نشده و ارائه خدمات بانکی را با مشکل مواجه کرده است.
در این مدت، گزارش‌های مردمی از تداوم کندی، قطعی و ناپایداری سامانه‌های بانکی حکایت دارد؛ این در حالی است که مسئولان بانکی در روزهای گذشته بارها از رفع یا در آستانه رفع بودن مشکل خبر داده بودند.
ادامه این وضعیت موجب بروز اختلال در انجام تراکنش‌های روزمره از جمله انتقال وجه، دریافت حقوق و پرداخت اقساط برای بسیاری از شهروندان شده است.
هم‌زمان، کسب‌وکارهای خرد و متوسط نیز با مشکلاتی در دریافت مطالبات و انجام پرداخت‌ها مواجه شده‌اند؛ موضوعی که به گفته فعالان اقتصادی، بر روند فعالیت روزانه آن‌ها تأثیر گذاشته است.
در همین ارتباط، محمدرضا عارف، معاون اول رییس جمهوری، در جلسه‌ای با مدیران بانکی با اشاره به اختلال‌های اخیر گفت: «آنچه در بانک‌ها رخ داد نتیجه سهل‌انگاری در حوزه امنیت سایبری است و این موضوع قابل پیش‌بینی بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76751" target="_blank">📅 16:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76750">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uXhpTlW5mNEdZEcsQNAkftLMLauHfy10-9MdTxfgFWgsgziEXTRCTVHYH5EfxPtaUq5O9f84-qpD8qaexi1LTlYp_kKaueOmiYrKCrYuxYlDEXaXHwnILEebZVyYyLpHjmBTblNNhKy9VSdDKObRnrICLfwi-aQ1iPD3Xh7xoC-ebSQtjsIXlIcwlUMCMNX2VUPPIbmyAczw2WH1Jj9P7Ht3A4KL8NmMJxzhbtjz2hGpWtUKnFpMCdEQokLRNeN4XPVIRuqHq2XD7alUzLFOR1osCX9hyekeg8PLajwt2V0jOCbyrlSsBG1MdKnJb5oa814aBkR1G6tvV9EQMvxRsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضوانه احمدخان‌بیگی، فعال مدنی، جهت تحمل ادامه دوران محکومیت حبس، به همراه فرزند خردسال خود راهی زندان اوین شد.
براساس اطلاعات دریافتی هرانا، رضوانه احمدخان‌ بیگی، دوشنبه ۸ تیرماه، به همراه دختر خردسالش، مهفر لاله‌زاری که زیر دو سال سن دارد، برای تحمل ادامه دوران محکومیت حبس خود راهی زندان اوین شد.
این زندانی سیاسی در تاریخ ۲۸ شهریور ۱۴۰۳ جهت زایمان از زندان اوین به مرخصی اعزام شده بود.
رضوانه احمدخان بیگی و همسرش بهفر لاله زاری در دی ماه ۱۴۰۲ به اتهام اجتماع و تبانی علیه امنیت داخلی و تبلیغ علیه نظام به ۱۰ سال زندان محکوم شدند. این حکم در اسفندماه همان سال تأیید شد و بعد از پذیرش اعاده دادرسی و رسیدگی در شعبه هم عرض به ۲۱ ماه حبس کاهش یافت.
hra_news
فرحناز نیکخو، نیره بهنود، میترا برمچ و زهرا (هانا) غلامی، چهار زندانی سیاسی، پس از پایان دوران مرخصی خود به زندان اوین بازگشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76750" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp6MvWRs_DvnE8XnDtgfU_WAVhaMS9lmnAB7mrza3RD91PLEn2QoXCuWgcsicRhYMmTKFaTVOl5iIN28bNqKqKojbT8UKzepXi-oRfDAlqGxF6enE0gxut9on3CQcvKMmT1DrwdgdF7YiN_CP1WWh9IM5MHEJQBKsQRO3-gkY-YGSPAEbeExON2cmo2Ls1TD-giq1JPVMCpbjtyxvzVjhEfFPXZKqIirP0xN82DgNxGH4G_E19QXtDsAh57pASb_dg8LqgXBtVinBHfT82kOSdu8swRj1HalluiUiPIxSm7rgxjf7Rn05H85PFeqxtCjH4DYeec9UoZXfcgjrH5jCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه استان کرمانشاه اعلام کرد دو تن از نیروهای بومی سپاه در شهرستان پاوه شامگاه دوشنبه در پی تیراندازی افراد مسلح «به درِ منزل‌هایشان» کشته و دو نفر دیگر زخمی شدند.
بر اساس گزارش خبرگزاری مهر به نقل از روابط عمومی سپاه استان کرمانشاه، این حمله مقابل منزل دو تن از نیروهای سپاه در پاوه رخ داده است. در این گزارش، عاملان حمله «افراد مسلح تروریست» معرفی شده‌اند.
منابع رسمی هویت دو عضو کشته‌شده سپاه را برهان کریسانی و خالد خالدی اعلام کرده‌اند.
همزمان، سازمان حقوق بشری هه‌نگاو گزارش داد که این حمله را گروهی تازه‌تأسیس به نام «خوری هیوا» (خورشید امید) بر عهده گرفته است. هه‌نگاو نیز نام دو کشته‌شده را خالد خالدی و برهان کریسانی اعلام کرده و نوشته است دو عضو دیگر سپاه در این حمله به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76749" target="_blank">📅 08:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm0vHl9K35rlhuzguGyAHyDRlzRwpbOZb-kzbcvJW-ExyYTdt0aRq_KqKdJNmuD7jvXc8FvPW3UzkEKIT4ELPv2uoW8sBWdlO5m_Czmx2XBmA1Z9M41OLsyTzNXgrZdr7JcNNcPGSxBFNeWe7JP9vYHK4hoBevyiVteBigBwWo3K_ILfiEzDB422VGco_oRnN1xc17hvKXGhiVmZyO1F0T5OJKgqCwHhnKBqHXBH3la6R397YcjLM-6a0dHIj8Tvdu35sfV-rLlahbYSBWPhYaiZ7IAoKBi0KXS2VUdD2ZDM_fNuWMLJE1G5FWJZuySI-HuZBcKRVJgqGh1lgwRyeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز دوشنبه انجام مذاکره با آمریکا در دوحه را رد کرد و گفت در روزهای آینده هیچ مذاکره‌ای انجام نمی‌شود.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از درخواست ایران برای انجام مذاکره در قطر در روز سه‌شنبه خبر داده و سخنگوی کاخ سفید اعلام کرده استیو ویتکاف و جرد کوشنر به عنوان نمایندگان ایالات متحده عازم قطر می‌شوند.
بقائی در این باره اعلام کرد: «طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و این‌که نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.»
او در ادامه توضیح داد «هیئت کارشناسی» جمهوری اسلامی این هفته برای پیگیری آزادشدن دارایی‌های مسدودشده ایران بر اساس بند ۱۱ تفاهم‌نامه امضا شده میان ایران و آمریکا به قطر می‌‌رود.
ساعاتی پیش مسعود پزشکیان اعلام کرد که «شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/76748" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HIr_kSjHMoobPK2aCvc6c5X-B-e0Io1RlO0-vJ-7N9-Ga3W6tw7IiohUORsyHQhjdkH8i75VJ11OpCFuKkWW_aC0PM2d6Dgqk_hhUklH27IgNgkd6MVbGHsr_ycSpJPTUcQtV64UKKYboiYanXErvMh5SluO4xgrbVxNltZXkGU7eciKZvvGk3NLlH7q4YwMecwC-WM63Drpr6LXhVdZyhxtF88dERGAmlMBOy_wSKouGvCxyweemCLLMDysdeybkzmA5b5Vg8Zq75qpnMekTtWpfuopizsCKbFywmkgwqGHfIIhRQj267_Cj4VAY5H2QUxpQuJZLFGMb_LnsrMUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76747" target="_blank">📅 21:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS-4BeIhjq5mky5DllDb14Iti4se0Tn1inB61pT_GpKxRP3tpiaFavi0fP0B_fK2RQ4RXO9zCLbfleRRfULjIlTIqvIpV33KfPhfyvm4Dl7h4z9-ajJB4ksgP5oiyxGC3Bzcpp8PyoSXKW04geGzNtlYXPVXY1GLP2L4vcdEUIyNBLiynLRjI6OAvW69nb7E2p-eiQXK6vC5N8_ymdzm9ltyRySf5N813GM7ONnCPUSJFtNmC9-w2jx283c7ohxrd_gPllaaqv2ZClscDquwtiBuiHx3K9z57lmb6PzNPIUV3A5XMT7olWJBCgDTNp95bG4r5LWNzHPikpSkYhznfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف میری، ۱۷ ساله شب چهارشنبه سوری در خیابان حافظ اصفهان با اصابت گلوله بسیج به سرش کشته شد.
یوسف میری سه‌شنبه ۲۶ اسفند ۱۴۰۴ هنگامی که در راه بازگشت به خانه بود با مادرش تماس گرفت تا برایش غذا گرم کند اما پیش از آن که به خانه برسد با شلیک گلوله به پشت سرش کشته شد.
یکی از دوستان یوسف به ایران‌وایر می‌گوید: به مادرش گفتند به اشتباه به پسرت شلیک شده و اگر جنازه‌اش را می‌خواهی بهتر است سکوت کنی تا جنازه را تحویل بدهیم.
دوست یوسف همچنین توضیح می‌دهد: مادرش مرتب یک جمله را تکرار می‌کند که بچه‌ام گرسنه و تشنه بود می‌خواست بیاید خانه شام بخورد ولی آن بی‌رحم‌ها نگذاشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76746" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jRzkSlu0JJo68lkTR8Io1f9kdbqIbG5OE0WMxArJnYyMco-m11Vgj8Zq8XiGuFrsw7KncXFp-pW6yoe2fVryyccfvRSpLzk38gI_tDii08HGTFkgZqIveOZtvMcBk8h4muN_WCFHr53gnZZ-5NsTa5lIaUffmpn6nwukpJ4ZNz2nS0Plnsg-ojEAl1g3y02-F0T5RC9p0ck1X2NnqQupA5h71JhiM7QJEJN3jDWKn43c07IundAl57xQRH55mmmg4Pi6hg3Rcdc7yQrM1oLAYOfLjdwZsISsoHD2kQ3GfxLh8N_eAGhp7EZyVIpID1-VChYh9x6z3M-qtM8qHuAYNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدر البوسعیدی، وزیر امور خارجه عمان، روز دوشنبه در گفتگو با رادیو مونته‌کارلو بین‌المللی اعلام کرد که این کشور به آزادی عبور و مرور در تنگه هرمز و اعمال نکردن هرگونه «عوارض تردد» متعهد است. او تاکید کرد که اعمال چنین هزینه‌هایی به‌طور بین‌المللی ممنوع است و عمان به این مقررات پایبند باقی می‌ماند.
این اظهارات در حالی مطرح می‌شود که ایران نیز از برگزاری جلساتی میان مقامات تهران و مسقط برای بحث در مورد مدیریت آینده این آبراه، طبق مفاد یادداشت تفاهم ایران و آمریکا خبر داده است. با این حال، گزارش‌ها حاکی از آن است که دو کشور تاکنون پیام‌های متناقضی در خصوص عوارض و مسیرهای تردد در این گذرگاه حیاتی ارسال کرده‌اند.
وزیر امور خارجه عمان همچنین تاکید کرد که مسئولیت اصلی تضمین امنیت تنگه هرمز و پاکسازی مسیرهای کشتیرانی بین‌المللی از هرگونه خطر مین‌گذاری، بر عهده جمهوری اسلامی ایران است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76745" target="_blank">📅 17:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZnQCaYiLI2LWr-NONlAinhhnjNJcSEJ4EaYbtcv99wPavY-ilmu_qZ5mnRcD7fXnyC8tNh_h5OIOu0xLdMBMmfYZ3Uf9OhSXV8yjr8oYUTu_BfgBXFcB-R0wc0KdEnpFHpsvyi6Ayyq9PbZUdgMhJNsh8YhEvzO4z6ckWdf1Hhm59gexws3bnp_MwjS5s1-ZKoep5LHRXwLabqqYRMEAWHMlqZ68arQksj2ZlzcXBSV1M6s7CAN5pOyJGiONPXXjkdsBFgWq6uwJkAAwdCCfjTdGoLRADSZx6cruHX1wNnvsdIE1nC5mtndgi1doMETGDh0MEKLgsodlQlUxBvlmIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T2EwOSRwqCV7zAL_Nu0b_vEtk4CxTB60fo43Wsmn09buo8v6tBC-_qsGsR_p91awK-w0iEElLTJhw4ZQWJMHpoihDnUvBcsA39rydnYPT6SWmvJmZKqYQjqQ_12fB_H1IAj1EgxF6_FiI1jvIfrDO1LcC7EKz2Phrr0tvih9m14ZznyXNtlKAgXD_CQT4tp0IAV56Q6G4Vmv0Ubl3mJTvJcE0fQWn8ysRaWIfYSL_rdWh7tmO0AcRSprYuiTIeZVTB5WLaQDgZrEEK03JGv7O_n9_ZU5Ijg01tzT70Os7pfIKnQ97yizob1gOomZYtFU7_1vdChGL6flo5_V0WQLDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست عراقچی با فوتبال، ترجمه ماشین: از زمین فوتبال تا میز مذاکره و تا میدان نبرد، هر گامی که ما ایرانیان برمی‌داریم، بخشی از مبارزه‌ای بزرگ‌تر است: دفاع از شرافت و کرامت مردم عزیزمان. araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76743" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RovpTn8kEsD9DMPSzrgWWHDiz25ICPFXT9cXAlvqb21XSUo3f-8i_KaTNfW0F1RTVbs4sGWVzQqUvojJRtQct4ozD_4SS2stq1uxzYhz052HZWbCaPkpymRBhKTw2dBFu7G0Vo9DgVjanyEbSXuA9CviNhGzkEqjD66wlQOoYZJlN-WT_vsP2hNJFTwyPuNgkNT6Kwi2P7E0dGFcp7cvXN1_H3v-csV6HDbpjqfCOOgF8uVJd6pNli-myZCI5PG34JNDfgIQwJ5UjxpDmQ1qb-dDlmFeURZ3CcPl6z45eFQmQKtcpADK2idyoVRMMSMrEa3beq5bxdxlrgxgdoh_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FurAGuWpnvXQqu6wpIzibs7f2EELsL2Sq2zvguwjhJB3WxzAovlenataoCEbdcnsLTnRTVWcj_pEu8z4MKtJfSpikx3lTU0GaD-WxcgxovzaQcncHEptENKHiKeVY51hp6ky13T9yNiw1QrIRhJf1ulX1ea4Qd3HJznAPegSZ_4R_B35f42uQEuCKhTl_DUavCCGSG48SJOPEIgl5NREFNUAfkftw40wVlmuFipeLBWqBApa99ifCavaJ6pX3gazL8C7BEPTwL7s6KiAZr3J9J2IEg6NhAUxWQonlBb2Vg3Fo01XQZshWGkq0tBXwDCSixVnHvSaipJ77vTZ5MVCSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی نوشت: «ایران درخواست دیدار کرده است. (این دیدار) فردا در دوحه خواهد بود.»
پیشتر کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده جمهوری اسلامی، گزارش برخی رسانه‌ها مبنی بر برنامه تهران و واشنگتن برای مذاکره در روز سه‌شنبه را تکذیب کرده بود.
کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده ایران، امروز گفت: «هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه تایید نمی‌شود.»
او در ادامه گفت که «اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.»
@
VahidHeadline
«کارولین لیویت»، سخنگوی کاخ سفید اعلام کرد «استیو ویتکاف»، نماینده ویژه رییس‌جمهور آمریکا در امور خاورمیانه، و «جرد کوشنر»، مشاور ارشد پیشین کاخ سفید و مشاور غیررسمی «دونالد ترامپ» در امور خاورمیانه، روز سه‌شنبه در نشست دوحه با نمایندگان جمهوری اسلامی شرکت خواهند کرد.
@
VahidHeadline
ترامپ در پستی دیگر نوشت قیمت نفت خام وست‌تگزاس اینترمدیت به ۶۹ دلار رسیده و رو به کاهش است.
ترامپ در این پیام نوشت این قیمت از سطح پیش از آغاز «خلع سلاح هسته‌ای ایران» پایین‌تر آمده است.
@
VahidOOnLine
🔄
توییت خبرنگار اکسیوس:
به‌روزرسانی: یک مقام کاخ سفید می‌گوید فرستاده ویژه، ویتکاف، و جرد کوشنر امروز به دوحه سفر می‌کنند و روز سه‌شنبه با نخست‌وزیر قطر و دیگر مقام‌ها برای گفت‌وگو درباره توافق ایران دیدار خواهند کرد. روز چهارشنبه، تیم‌های فنی آمریکا و ایران به‌طور جداگانه با میانجی‌های قطری و پاکستانی دیدار خواهند کرد.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76741" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAVZfwQRttDyNbfGO1AkgtnYeYaUC8jMg7o0HIgwozPs-eOOMyZUdPC8p5eq2KsnGmMk5s-8KtWAS7OtjsmXnsUbyswCI8dV6X7XNv1TClQZT1BjQk1M4LOtZwU3xvrHf1RwJ81YpLHgGtrfBeJLLh0-jriC1cheCZHlWUKuYtt3GPytwLyjvzAEuRwZGQ-IpFbYKsaRYIdA-4gtK-KwfKSkiWWN5xdkauAyGcGSrPHmIsl0L0SBnTyWdVXk9UR2Xy7VO5LhaDj10FXRmW1aisPoMYu12soKm4kqYt6ZUoODYgKHT0E3vIyIKyaoznYpb-L_nBEG9TSaYYi0W8m1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری اسلامی ایران روز دوشنبه هشتم تیرماه گفت: «براساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد».
مسعود پزشکیان در دیدار با شبیری زنجانی از مراجع تقلید شیعیان در قم گفت: «برای بازگشت بخش باقی‌مانده این منابع نیز پیگیری‌های لازم در حال انجام است».
او زمان مشخصی را برای آزادسازی این رقم اعلام نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76740" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mV4lFD_11V8bv97n1x0kPEVDZmDftu1iqNfmFFz9qz-iawTjTyQ-Whqa8EFvvLvRNvO7MIg2RmU2jzr7keVVIJumOZtwMG0cZzkl8k0w04aLJvTHqDHzY24DtYPzUG5noFUrmXxB90vraYwPBU89Ibhmv6Gvq8-motyFaJVVfqcZLHrNhldK2mAuaZm7EM7KcGoRjXdBKGe1tGF3ebUu__10rKrD63XxmgZ2fKUSB8FsvGAZueHp9jChzsk4Hz7tD1o6WrKUl5pFJX-CAnl_-0Tcw4f2ByyRKCkfbFAqPXWTboP5kj1axn4ZvrdSGUSQaTlhzKxX43k-YaUxxmsYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REIEJkZnzFlDi_rFWZx7DNleVzsLf2g6Byb_m87W06jwnXIINSCCRrgIiQFkoVBza2IyXV6CqMzqrQzFbpGO00zYyu9zvufyAyhWIXMWzojBqDJi4MYayEEFsCgYv-CEH8q6ZrfsKyzHnbWiSkesx5dC1KGSmEF8YH-Y5ghA3GYhP6PUou6gMaF53z_23-17cA08aiKDD0s04GHXfqHHQ_38Ad2AEKNI0Vewl3QQYCxhZbXFyRp6cCmCh6iXU_myCdxRL8Ngd6t7wB1w8uaJKl3cCtV36qPRpR66f5GnwoXFsqrh4aahKc_GjDW1RIByCGpiGHYqwNu5zye3IvvcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvbvixAJwrSpLo_JcIrzJ8I8SLtcpgHvdE1xAM8BtztzNUHY49fna5RKWyPsPRmQ7SbRrOKsdYMjoQ0JQMFqqRTlqKsneCzfkf7JOl8HFmqul8yEwjfxpy40-YMS092QcgE-RMTD3lwk3y50nwSSrKfCv7VPmTqizG3xCam8z7nqzhjixacfdnSeb_vneXtg74CxzIro8Uf0LopBnq_hhGz-A6lbwc0xSZQzUhmVI0f6S4W5aJg6Jg5RBrcqFatT6_Rw_fxzLDGQZOiiTP3BxSfqTQIRGFoo_F62jNXO7_jUGAOnw88PiZqUqdopOnyaQx7ES0uhD--fBImiWywd7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=eDKDt8vy5P4Rlbn5a8B63H7zXprcTfxU2qdUT24ONGZTr6BsdqrL1rLdGSTI-uc3pxktP5YKRFXFNLsvpBj94NXDoYNOnAe-x6LUGpiNyVsgyy55kXL0sJhC2pd2m3sPPTtmzC-By8_2nAJW-e1zSMFdwMxR1vfvV9gHH0f7Moevbihl7oz4LdBf2UtqOPPMUztcFTbshEhEyk0U3jGHOIL6zEEWtmftoN77-YEJc2Kuw97KgeLyjOKO7IJCukb4682uD_cL9glGTE7lS--WBHqaE6IjXcbTKmcFl4ijwaE9FuyFvqJ4Adw65xXTKmj1m5QAUODMSkGWI8R1_mRN0UUb1ZNWBVCxREigUmHYobMPzuMzMrAd_nv52C3tGryIUGela99OgAC0oJg5PczvEzK6ea3eLsSCkq5Okxh_KXnFci0WqMUjl-pRgIQez_9IFvNKihpp_F-9LInMufNVdYdSEUtTE24tJmw2bSFMdiOq-CQNKqtWpdmb_Ygp-Dsw139BZFewdYdxK1gs6W4dF6t4jgQDRj0ouHX1NRtPfwE2f8XoNxUpvSTWBnGj-2GM1xZ4qfzwtZ3GoUBZSC5m4tF11DMLql15KfHfiKqVQ96ePOVRDxMyTbkmB32rqvAMX0WvoHoekbzhfGRgxvyoKDSfMHDbR7w-B8iuSCC7fS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=eDKDt8vy5P4Rlbn5a8B63H7zXprcTfxU2qdUT24ONGZTr6BsdqrL1rLdGSTI-uc3pxktP5YKRFXFNLsvpBj94NXDoYNOnAe-x6LUGpiNyVsgyy55kXL0sJhC2pd2m3sPPTtmzC-By8_2nAJW-e1zSMFdwMxR1vfvV9gHH0f7Moevbihl7oz4LdBf2UtqOPPMUztcFTbshEhEyk0U3jGHOIL6zEEWtmftoN77-YEJc2Kuw97KgeLyjOKO7IJCukb4682uD_cL9glGTE7lS--WBHqaE6IjXcbTKmcFl4ijwaE9FuyFvqJ4Adw65xXTKmj1m5QAUODMSkGWI8R1_mRN0UUb1ZNWBVCxREigUmHYobMPzuMzMrAd_nv52C3tGryIUGela99OgAC0oJg5PczvEzK6ea3eLsSCkq5Okxh_KXnFci0WqMUjl-pRgIQez_9IFvNKihpp_F-9LInMufNVdYdSEUtTE24tJmw2bSFMdiOq-CQNKqtWpdmb_Ygp-Dsw139BZFewdYdxK1gs6W4dF6t4jgQDRj0ouHX1NRtPfwE2f8XoNxUpvSTWBnGj-2GM1xZ4qfzwtZ3GoUBZSC5m4tF11DMLql15KfHfiKqVQ96ePOVRDxMyTbkmB32rqvAMX0WvoHoekbzhfGRgxvyoKDSfMHDbR7w-B8iuSCC7fS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مبین یعقوب‌زاده یک سال بود که مادرش را از دست داده بود، زمانی که  تنها ۱۷ سال داشت، در ۱۷ دی ۱۴۰۴، در اعتراضات خشکبیجار رشت، با شلیک نیروهای امنیتی کشته شد.
🔸
سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/-9117/mobin-yaqubzadeh
@IranRights</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76736" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=pS8T8rIKgryUuYH-mGyN1Xtd8h_TwyUwh7LUK1asimWfDGtsHkCwoij6nsSOUJRf3CICbKwXMnknmJnOxZEJDhPlEQiqH3XAbieD7f4sXInMvs-NTHdw464To4-cxbI9nAxtsxs23qN6I3YMNutF8hU1_2Z-UJt7a2Bq5vup2GrSTqqbL61m0aoWtQvPy7xLFD5xOrd-nRUUW9S5HixInml3zpZw1JOnf8GFOaj33EUJPUH5kpI0M6C0hETj5e4zg8EWw9MstDZ_5TGtytEmJ0cpoJCxeEN8EHexxnA_zytGR-3_jOVcBXfo7NjL-uuszhFJIpnaog0SiJYQudKFkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=pS8T8rIKgryUuYH-mGyN1Xtd8h_TwyUwh7LUK1asimWfDGtsHkCwoij6nsSOUJRf3CICbKwXMnknmJnOxZEJDhPlEQiqH3XAbieD7f4sXInMvs-NTHdw464To4-cxbI9nAxtsxs23qN6I3YMNutF8hU1_2Z-UJt7a2Bq5vup2GrSTqqbL61m0aoWtQvPy7xLFD5xOrd-nRUUW9S5HixInml3zpZw1JOnf8GFOaj33EUJPUH5kpI0M6C0hETj5e4zg8EWw9MstDZ_5TGtytEmJ0cpoJCxeEN8EHexxnA_zytGR-3_jOVcBXfo7NjL-uuszhFJIpnaog0SiJYQudKFkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
صدای بلند)
ویدیوی دریافتی با شرح کلی: "جنوب کشور، جنگ اخیر"
انفجارهای مهیبی در یک اسکله رو نشون میده.
از زمان و مکانش اطلاعات بیشتری ندارم، لینک یک صفحه اینستاگرام رو فرستادند که نسخه اصلی این ویدیو رو دیروز بعد از ظهر بدون هیچ توضیحی منتشر کرده و پست دیگری هم نداره.
Vahid
آپدیت:
در پیام‌ها میگن خرمشهره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76735" target="_blank">📅 04:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tExwFODdIu-Wl72JE65q_4qu1QN2aAGrCY9iIvT_Ot5rdHIR2BagodyG3wFP-l3_Psq1Z_XS5ds_J1LRaYCi7B8YHfYDu7P2SMI9Hg1urMllDu-1u7PljQ_SP-qe_e3QwbCk4fgjuK6HK-LRjBhmGw3QEYeGajrhZIQ5tyLmnCg8MTWvTtXRXe_s3ujk7aI3xkBHu-alcYJk8iNWPzc5zS_iqOeFgGW8EOgI4om9SAdkkZuYJNOCkDZbhha8mznGUCwUbLxjpc9o1J9NhvgTwaZrII7rpGUs_ruWRkL2DyqV7s7yA4sUhKn3E0i-7d5J9A2G76l_JfG0ti3vO-fjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ogQ8IVNImBn7dF_M1pkf03vZdVrb0zUxCgeTYo6nw-jUxuOkCyQzixpUiiGpQhhxHzasZRlGhczDmEUs6YoFJXy61oZ37mHrmVhXedJM6lknbQ9NDhK1cir_A-vt7-AJO3NpillWuOes-6LEEFq-SiNyx9T31PiO2VBzJ5aJfCE2AL4BSRYWfoIZfeBncvif3AzC3eK7ndg-6YGTDHH_gVgpMKQ2nyUWhQkxcMDXVyECf5LVtDVGb0ROGhXagJRpD8PSBBsi3CmZzdgvf3mKS9p9GjX5R6SbgrZMbdH05QOug2EtsN9-v_yACIzkcMkuT0HumNVuEtUQKVY_ikCJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آن که روز شنبه - ششم تیر - نزدیک به سه‌چهارم اعضای مجلس ۸۸ نفره خبرگان رهبری در ایران، در بیانیه‌ای شبیه «فتوا» خواستار گرفتن انتقام کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی از دونالد ترامپ،‌ رئیس‌جمهور آمریکا و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، شدند، دبیرخانه این مجلس روز یکشنبه - هفتم تیر - در اطلاعیه‌ای، این بیانیه را «نامرسوم» خواند و درباره آن توضیحاتی داد.
در بیانیه روز شنبه که ۶۳ عضو مجلس خبرگان آن را امضاء کرده‌اند، آمده بود که اگر «مسلمانان متدین» به این رهبران آمریکا و اسرائیل دسترسی پیدا کنند، کشتن آن‌ها «وظیفه شرعی» آنان است.
اما در اطلاعیه روز یکشنبه دبیرخانه مجلس خبرگان آمده که هیئت رئیسه این مجلس مفاد منتشرشده را «غیرمعمول و نامرسوم» توصیف کرده و اعلام کرده است که محتوای آن به بررسی و بحث بیشتر نیازمند است.
به نظر می‌رسد،‌ اطلاعیه دبیرخانه مجلس از اختلاف نظر و شکاف میان هیئت رئیسه و بخش مهمی از اعضای این مجلس حکایت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHE2Q3G7FNdNXoIhh7kOaE8Plg9KFNLcqev6rfkuM4jKhf7mum0IsCcE9N89EqkdesUupklXph_2eSmzj4ZAWyZTehgpuLCezgtr1OwYOWOIOXp7Q4ZkFyiZW-xTa9Nxn3AEDu6T3rdcinhiEoQAE4xKhJzlIkufkT_MDOjhlrZ8w8Sg57-o4vrBCIHy5TdjGtSajRChwo6ear081G8Rz3qPxScU6o4a5ur8rhHYc9SZInQr4FazGamonGk6HKxm807m3udk7OrDceWctUqgdzKgqfcx91EK63baDBcFfwYDt6cTkcVQWMxVjv6xkp5TrgA8ZQ_Kj0cxXtu_MrL7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RK5kxH7fH-m-iKbKLxX8tChTSTyxlrivUghRA0S5AyXCmZi9-7OlF22p_w58ep5C9ErnIqp1TNUHOmlnLNye7PGr-YeYnnTk_dBNHVUv4Rmudt5kO525JOhqbzxG0wzishnNVvPeZsfiwb0xIG03Prv_GYQUbH98s6_sTfdCDF_wIMTGVpTXOtUK7lR9xWDlHOfCDhZtXPxmIOPZ0g1y7Gsx8lk3YHm5Z4pPVAwt__-zFnyaf6HG_-Dlcf-Upqw_xzA4YJ-rCe--xVORXKb5IiCufjEKmhkzULKkqlG0in9X8_oRB-TkGuZDNynSRMh3-1h8llJlsuSlylzf701Mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_IfEWqXLm0k-yoa_eD2EnYlpkl6jJJF8RFGEOIF19lL3uK9ua1Mnm031BBPQpAHaDEBzisN0cRzub77mtSqdYhJ0go6yjcvYS50DZ3O7XiAgk42_yztVsYUbN8NOkE0nISjW4kMQgv-y64GxV0VvZWcUEPIFFu2siJLz0Oh2UR-NBQoCkhaxpXVsgNMt1vtxurYiNQBQfn5hT9JKQYi8njnQQXW_Ls5zOCMvCnSd0H6N4R2oNF94ctiecbnTMLl349GAX22u2x8Q87ZmgOP6_EV63TmEjjW0IqirXIelb_HuyAX2Oq-0P6herQSznAsbEEaTS-3jz8NIwi8AeNg1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1paxzPg8AJHdLdz7upC_4CQenZKuHRU8yk29SDlwtnn4UL-rkTVZ65Dbt3CIZEBhU0ZY2bsl9xvVGDRtOdwHsmesACamUoTAsk_q-QxFfKbY-4LBJ9YD9pJCIMNVElZWggoDuw7CX1uLkXiZFoglT50yBRzzeTDyVM048bebZ4IcMfiMM5PnY23BNbmeuBtUR-8qAxzPBlam9LYtpeUQTQmhSEacW7FyXGPrBUH2wFczIbpSMi60CJMC2O3ZnU6jkBb43zaUqMFkilHcpQQb3J-GpvvtBQq1vgLDjYt7JejNO-T-icsA-LFHA5FXeUnynQNz8lkQysn8qplr8f7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou38S5DS_33RxDEo1x1AuYG_naCg8g3Ob7iKtD1XmkrZ_wmJdWMjeT1rRRUQwXO3ktIYlH3z0vyY54z3r5X1naoUeHKXVOBF_W9sp7c-QPjvp9kpUIUdy5GdeDnr7zi7_ObzE8DNwx0rZ2NlmTqQIGDmdkh2OxpvP9n4vOjsX0wg7GJAvyWMNc6z3JGw6hd1h6zV_hNAG5qEBA7K6hpXRot-MaX2TbkrKbvFvwtME5o56XDo6RMfSnwdDEcNttueqnZ_6J_oAzm-CMM9BxDM1QTWrHQW_wEGD672VURfamXTCaUVOIU4Srbl3PNT2UaY0q1zxCfc5hBWMk8wQAYY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=WiXlHAc92aHXBB3v5NLOr2gKbBEaX4mucZL6XFZYiNw_I4IuboNf41zw2DHsfvVyJNe_-UjkkzLnX9603Q4eWkc24MjH0-Ktlf0gJlMKg_pXXdsSP_KLC4eHp1tHvJfG17dRHmhAgF-V9xPxqxiuCSL7khQWEod0T9C77v6eEWaw40betUlMGxtLIO0nY-eysKxX7v5JAcnnB822qvYL6fW1kMCCpUZs4TjE4Yu_sVEl3axb_NilgGG3PbqPahS-MozPS3qZn5MyzpHgyhllUStAwvv-jwSkpAtWheGxMOhaopo0Qo1ZGCQe5hh_1hZDWoYlCdjkV_4KgV1Y8z3PCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=WiXlHAc92aHXBB3v5NLOr2gKbBEaX4mucZL6XFZYiNw_I4IuboNf41zw2DHsfvVyJNe_-UjkkzLnX9603Q4eWkc24MjH0-Ktlf0gJlMKg_pXXdsSP_KLC4eHp1tHvJfG17dRHmhAgF-V9xPxqxiuCSL7khQWEod0T9C77v6eEWaw40betUlMGxtLIO0nY-eysKxX7v5JAcnnB822qvYL6fW1kMCCpUZs4TjE4Yu_sVEl3axb_NilgGG3PbqPahS-MozPS3qZn5MyzpHgyhllUStAwvv-jwSkpAtWheGxMOhaopo0Qo1ZGCQe5hh_1hZDWoYlCdjkV_4KgV1Y8z3PCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGHEnm95O5GfP5M5LIFfkeHYXPnVUf7M51KEIm-dTtk3NAw076kwng-oNuMgR-yH_RF4GHRWixKpOhjJGQgcdjrj1_E_pOEmNde_5zRUi8rxbv_AHFr0LSvuJWgiVwqPxlj91i2x2d1QmwAjsOjfjhDLSmHuWg6OhPHEdicmXx2JRcsSzB_pAZDHhcX-CvdLN3lpv0-n9dLqme_oWnaYRP_UWGWqIGrUscCNcassi3NaTmk6u-6jpeaah5h8a_-eeKpEKfnIovQsRqf5_T8p2dxhwaAZElfwBV1Spc7sLagtBHq40yCjaYJRZY3eJOyZiJOQPiF4Z8T-1-qdtjXiCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oGuAOISmA5PA0DvOBOvLyrtEw5BKz7oCtzgt_H6H3vU-ZS7RzehIa2O6_blLqUqgOY7ZyXeB3dmuzySBrl1EKrZCdTFwSh0Gjc5TN4y1qVekkuOLyPD0_LpJCUxB8f3dCXxpbvfE8hHdXOVZnp9BRwAZqzbLBE5IPgtKBQxKjUQ8dG82FaOwUs0qsU_KZVaOmJwLEix0TPhi2V1urZsxX0007AtUWGWcoIkcwmWr8AYq5CpeWExQMu7oDfFnjuvkM2RTsXVbxSi06ux0GMGCmBuJvF-wNwuTsOUwQjr49BIUQl2e_7iKXTaKe3AjIxqqFo30b3SvQ3TFMd8EBOLgmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZZ7wmopPDSxgL4Gve4xXkaC_2YsJKvegCbU4FSrzwC0NzxNajGush7GQkXKVFpu_3WhjxX0pcRKfmYsObh21GpUKJm0mx47o74vpCOSxWbPPQJV8ff9sSOKEZhvDlt5WmZKNkbY94fVODiskt578gV_7l-6NOwkXwuxvnWJNB_lIpGKfFrTnMmQHN6SpyrrYEHX1D6Tpznz02oD3WVweZRJx4FW267DF4ZWIfXGjCJ4cKSh3_24i-ifpBxcCiQ7UtpGa7X1j8ptFv0cLNbRI2I_PRgEeDrUtiJYu8b0G-QHntK6q4q8t6hIbjkz9ic0IHyV5dK5Vinsmfsk1TNcdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=e5a8VPFr8APG99Oti_e6IAYanB579YNA2a9aO54_novG9wzE7qUTMMtSl9SQVD8SJttnsGw50y3suURM9LjChFJqgIXe--mYAdXpUT_0Mfw2YeDWKiqW8BBwgoy3FaNvEI5X5d4kSnJWnB2TtVVi3Bf_tFrYLrE07u4l9eJXDDKUJGMK_-gJMR96VsM8I3D-9f0fedwSk4ia1y8nOLNcLUSTSIbC1FBnT_V2f3WP9gr39qLX4YrloP7Si5UeEoUagVrZY3HTguO23uEgj83G2veKDx2cUKB_NCF0Las7NVl6UR_LAIr83_kH220OLZW1tRfISTcZQIeA1GMIuL-0Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=e5a8VPFr8APG99Oti_e6IAYanB579YNA2a9aO54_novG9wzE7qUTMMtSl9SQVD8SJttnsGw50y3suURM9LjChFJqgIXe--mYAdXpUT_0Mfw2YeDWKiqW8BBwgoy3FaNvEI5X5d4kSnJWnB2TtVVi3Bf_tFrYLrE07u4l9eJXDDKUJGMK_-gJMR96VsM8I3D-9f0fedwSk4ia1y8nOLNcLUSTSIbC1FBnT_V2f3WP9gr39qLX4YrloP7Si5UeEoUagVrZY3HTguO23uEgj83G2veKDx2cUKB_NCF0Las7NVl6UR_LAIr83_kH220OLZW1tRfISTcZQIeA1GMIuL-0Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UqjCevox9lLBOnzsrIZoS520RPhLbJyAyE0kh4m4TYztSfWWlRULCFvbQ-oD_Aoguxw1IwZBx1jZ3KQDe_7d-ncv7iLGtTLpRJcqZLXbCndTktPxlz0rQgEb1Jz4-xl1f1ENty-uRld-OK5vxMgG0y6_N-l0juNShzOBO8qbvXHC395yEOd3zTvUJP04XSbMid0e68ICwKrYGuBe-Oc0mjvLYO8xoVJGaT7CArvXI_8Kax0f0JBBT28YMF0DOuxHwMi2BN4WepgO8qjY5xMdhFCkd-a3tNF8jyaBS3cghCqt3cw7dVb-BIUGMkjdELFFHbJmLN9wd440gdOJ0jSXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CrMIxIXo51BJGpq7wU0QwwOsljxLF83IRrUwBXbnXWASNIBUVBusV4m71yo_UMwbRq_MYmhsNrexflhzvA0F45Q47gOYHcg5LesjsVA6f2JPoFXsxhBUAiqGgSlF-1e5rszJ4KB7tBhdHowP5s1vRTQmnaVV8mAKR3AT0kfp-YZyQDnZWvPK7HH81Mg7qL5JI_HvlAo9BS8n_OTigRyE2pxyb69rx5OAWBJvvq4hjcyVWeYVFsGuuHI3pFauW1PkQYRmLNzzFX-CreSXvLK44QIVTkqiJQtWs6XTzzjzuJ8KIA4p1WUgjBFlVqJa_5Kdta7wXnZ9REaA_AcPJ9s6Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aRi16gwlfGa55OIgAQ7B-NQ3FhWKdeWtxR8BKFy9sKqI-qIgViI0asJewqDckAAaVQ99LtNZh8Jn3d3Ui1Gp6ffLrNj0ysWL-WaMcEg0dS9_NovQDRbMXGJRHpf0lTbFIGsl8AWOLIR7ajpNzoEbPj-dXsojGufDZtUXfkr3a6Q1fZ_8hcnJW_mhswJAlH294DXTK1z5LYumtij4V-Ln38_uFiWaONrZNOnnkxB9mpCxqlmWqFlSsgRV_-WOtatiSULAgCBQgqAYocmreOmBPous3Y7eUbqh9geONIo73Hu6pmk60ETBqsxx2dXURyVftSMsrUThxQAd5ry21Akjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=PY-U8helOwSlnTFbGYCuZjfeskf_K1atiIJEaiUxa9wAX4d2cl4rqrDfGz0EpYRsoYhc629eSVJ89X-BD9a4DBKkyLvEXjPxrXineWANBoJxmb2yIIvB_2LOS4vcbJohkGPaPCVI0uTAtGCjyi1O7VcC4U1yaYM2c64r7sQFwK99p1syGMA_AGgW7D9b-Cof545cxg-HO3up92xNuAWGgYfXoiYoO7bok52zeAKtSnyTtEby6Xo9UK1ECesKtDQBIn4iYxqcj4SSg-uALCROSjZIjSMTWb1wJumYymcBEk2SJp55C9X0Rp8vsuam4vLW8VXaTIMPtPPdgG9Fswpo4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=PY-U8helOwSlnTFbGYCuZjfeskf_K1atiIJEaiUxa9wAX4d2cl4rqrDfGz0EpYRsoYhc629eSVJ89X-BD9a4DBKkyLvEXjPxrXineWANBoJxmb2yIIvB_2LOS4vcbJohkGPaPCVI0uTAtGCjyi1O7VcC4U1yaYM2c64r7sQFwK99p1syGMA_AGgW7D9b-Cof545cxg-HO3up92xNuAWGgYfXoiYoO7bok52zeAKtSnyTtEby6Xo9UK1ECesKtDQBIn4iYxqcj4SSg-uALCROSjZIjSMTWb1wJumYymcBEk2SJp55C9X0Rp8vsuam4vLW8VXaTIMPtPPdgG9Fswpo4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=XLMQgOVXQO9NzECPFVnpz4QEtxrCHWsdhdv5s7SxcKXoW-vX3pH8SzyBIOP-U5yuqaDrrc-G2K0_fcxoCZou0F8Wkh1XeM_Ga1Ax6Kyk-owU1Hz4HHcgSkKu5ZDh6CwHWTkwsfectnC6Xaskqd3IV4DwLpYjKOaBMVCaWIC0NUkVU2aoZReXhyIGlWBcZ_tPwS6GwOc_mJU6wqfW_Lhei8Rg7D-NMs5NxLD-4Ra8aKk5E1ykCZPtkK3utbGrA6X8bX2EF3W2Fl2tBAe8JBN0sjvoFFTeyQFW3KVr19xAPx4jL6o5MQ4FOVbPQA5IK0n32kFQCJ8g3Zi_-V9fc2eYLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=XLMQgOVXQO9NzECPFVnpz4QEtxrCHWsdhdv5s7SxcKXoW-vX3pH8SzyBIOP-U5yuqaDrrc-G2K0_fcxoCZou0F8Wkh1XeM_Ga1Ax6Kyk-owU1Hz4HHcgSkKu5ZDh6CwHWTkwsfectnC6Xaskqd3IV4DwLpYjKOaBMVCaWIC0NUkVU2aoZReXhyIGlWBcZ_tPwS6GwOc_mJU6wqfW_Lhei8Rg7D-NMs5NxLD-4Ra8aKk5E1ykCZPtkK3utbGrA6X8bX2EF3W2Fl2tBAe8JBN0sjvoFFTeyQFW3KVr19xAPx4jL6o5MQ4FOVbPQA5IK0n32kFQCJ8g3Zi_-V9fc2eYLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AFcY2tKMx3HqEfJxfJNuK-l4iFfa5ZfRC0dQAzfDhJa62V6mwr7cdsVLXujLs3Y-bu-Ad7FQ6LetzHP0_kUSMN1E1GnYcoC4XhzKnt6mWzXafIgNVfDwMFP_Gn_ME0k4atIeOVbjdjVv7onXSHC1--wAX8mWvBCfR5cFi4qBAofIRDYmJMTFZ0oN5ZM9c9N0Og3VFK_QEVHAIpRqGYTZJji6VlKDH02eUh0YagXUIqbqr9LkM70shW7U56oasQVg48NjENrI8tDj8KYPZ666r48b0p7-0EkAB24GkFKFVWct5XPIM9L3ip0syM2-BBwZrASgKC35LGgT4T65MoVjXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XZMKYrcClxlcEbuXEVcPo4rCJZKc_RXiDRlG89cl5Ln0NL9_yntSr9WlR48tKFHaYZK7UVdS4qYMp0rN6ZlowCIIlizzjLu_Je3JYD_uIWbfrUA7rw94Dsvw4POGY-HD_2gto8_jUS40haKNjNIBX4z2tb_bIf2ceP66QyM7E-d51S_G1nSR8BrAjykqFyFbBqer9yKHNWxfFRAHKd1xQKOpjZ__onyMnS6DZbge10p_pZFCGHRecQHzFlKwv36qxYg5Xys4n4ivqZbuJa0_2LnrggxzZf8TStJECobG0DP8-5Td9Zapvrap4NGL4wq-4RqzQWOwiZDCswym5QJqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f5jcW_oOTyOlEJA2Lf9TI_GkK69Y6bQZUFnOTFMYCst4acX-zPmDzMPY_ClnWOdcxD-B7diTtkEoqZIcwDCiMnkty4Hfd5FbujaucTP9kIfA98-DoHKoEO2NucazO3bs9fVf00BLqDWtRte0fAiEbRaI0ex1KkoP3q7bSHfSo-59tf8EsUGfxetuspX9rG2Mj5sQp-RbSZDkWWHXu2fd9pEQH6U8uFb1Tcb57trcM6-NDIg2JE4kamXMoV3O-qP1dlYcqbLCnhYhpGm61gVPvaQjgR5S20S_mXACa0xE8IyVKGBN8Y4nfH4rY7zACj_gdFMsTKtSq2m3f_oPEDhoTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=uejTda3c-uUkPJQ2cGlTmon4Y67jHnHsjCzvp9C3uZmZEC1XCXCWl-Q1fARyuXrP3ZfMAHSjL_iY-ggQayrG0HQyKLC5PoT2nkbyyiHTYMT_FRv6qmiO3nKOIuMls78OUiVO9EuU_QbhlN-GyEx4OVag8dTVuCFwAhs-jn7PuWQ8IBoNxf1nqXlnz5lmbSKlDXH5HJEDku4T8bzoNbHlL3ms29RLGIn3un627ze9p3zgf2Bge7GMf9dySY4TfPJcdLDuJA2MM__xPWqihPQwhww3-uK0N_57xg5umD0aVhi2PbapZ-TTXclX3jGciGvxFmlMxVQA2lUrpGZpSmFqHg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=uejTda3c-uUkPJQ2cGlTmon4Y67jHnHsjCzvp9C3uZmZEC1XCXCWl-Q1fARyuXrP3ZfMAHSjL_iY-ggQayrG0HQyKLC5PoT2nkbyyiHTYMT_FRv6qmiO3nKOIuMls78OUiVO9EuU_QbhlN-GyEx4OVag8dTVuCFwAhs-jn7PuWQ8IBoNxf1nqXlnz5lmbSKlDXH5HJEDku4T8bzoNbHlL3ms29RLGIn3un627ze9p3zgf2Bge7GMf9dySY4TfPJcdLDuJA2MM__xPWqihPQwhww3-uK0N_57xg5umD0aVhi2PbapZ-TTXclX3jGciGvxFmlMxVQA2lUrpGZpSmFqHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c3KCZaWCwqpOCDouhreW2EHOqv7YJPjOQmZmaV4YebT8vNny40pM-cgZI0b_4bSNktix0MqhfnMlSXwZqtToOEHNVOkJ6Vcz_w6CbPBYbWNCHmfsfQ1ARlqBMK9IveVQ_sB0e7VQyu8Z0YtxUzVHOmm_xvUwo7i83nixkvV7RhwbHIZyKHTJiNN0OQeaiGbzEYux_6RBs8HP27PyDOYY1mZTTjx0Mlo4i32V0hCV1oj4-qIqWtPjRpYDHscLdoLSdeh4tWt109t92Eshd3KzCtd2RiRmLcUewTq6CqekKdSTV2m4MybVbCv2j5KrcMYTegkIpP4Hz0nUix0GcYrIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI8CcSfmESTqCRcu5vkeOeAEz4mcP4hnp9manxsmtd7tYcCuaMJC1aTh2UEiIPGhliYXhu-ulhkORSplUUa5gtqrVccqroqcwst6d23WQfde2Be-IRkr8WuT53SirLXlFYSYxmxWQQxc-rW4vnBSb4GeCN_2WfGaUyZmCUpnVi8L6DInTJHvBvfmjQjKiHPxNbWEjf0ZSYWsm2htaUGxdODV1C2GoUQADX2WB6tmH2sDunb3Jjcl5WNaZZuSKqSlucEJymTFtciVUgWbBxHJ8_oR-34IYoJVxclqvbf0acEoA1nLjda4p1Q_r1iBXqk7-MKjx7RPdU65u5FwCI8Oew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKj3kS6DZbo2ox2WeyvvfakJqSYdpjClWbRFuAnKksbXpWnfwAInZ87EYC9ixzjFC15zgA5kCeIB4nWbW6UCq3EH8BRqHKbdcup5bo3QafP4PpQqicXS5PBirwa17HAtRaH1Eno2FnMU-4YLGqYU9Ukz2L7voks8pSzFZiUQQTnynkbu4wnzqJlg2BUxWf9y0_d13i9raioaHBDGgThUaNjfayRFKQhFi0Car0NQLHY1ULPJp3mQESRuEQ_WoAozlgajUJdnynYwFL5YAMAbOn6_EU9rohy-xv6ZAdXGWxbRqO2-gY1GVhjuuQRqvi7lH4ly9jfNEXNYN5J3LStPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af8e8OzeCW5v1wNk11AQCei2zxfBa1GDiq9eFL3Ccs7Nw9WetMQje6uH7VNCFM3aOjhWmGGOKK4omFUKLczmhjNVh5zzoKsZp8f-7HVEASN1mWEX1RUvDPh2btJEtQmfW0HSgO67hAtJQi3kT_f3PNEP-vXl2qz4qUbRZu4PVO_I__W59LtqwGoLTrKJ77MyH7RMSZ73BFYlBNIKpGhuloEOKSFLvYqQD2vsg7K_6nd_Cy0UeFYGNiKUJPLFV8e22oMeVaJJxV6XKPnd0BxslNGXUooMCIRmmS8twAsfsqt1b2mtg_ZMyTdFH2KAMeBBXIVkhk-w3MW3BVaO6Fy18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mv5e9neELnNyY0wnfX8zTLociU4F_eD_yemGX3ii9RsDUnwuM5omh-t5orXUktvoOJ7hjHl_EwbAWU7A7SLiXzbtu44gCbKIAfqHhVEQ70S-xdZS6gpMYvKuVouMfODU3dOdOzyxm0vgfLu3_rL6EROHcD10QjwtgZFUBo1RGo8AV9eTqTFIhgRUq4DH8szvYiGb8dkyCRF6PwDeVFBFlVwBO1DTXKRY9kwhozC4mQz3Tm6BnyhS-lwJcKm_IcHgUIAn9FXAuHtwhXuhbkK6wKkxLknVy3KGAYdHRP_wVwzSvPbxymG05ub44zdhSMWBRS7KMgNtXzv-_TdcX5z0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKKZuWryi-ElATgZvvjzDT1_SdjzUjtOVL0rICrOY11_IjV0PzP2x3aqlA4eHZFx6rJO-863wJdCnMw8ayC_8q0aBfKSkRhY0TM9DFgxnDljBZ2MTz-FSjIGCF-5565hlf4X9impWUaVdL3RwqxayC8umW4SwWbC6jtFmvn5gSWGOqNpu82buo3tMrzkTrt-jX5DcHeVab6KWhwndYVROrRdWFabPFsSzdreJEP9GORhRmfhm1p65ekxrBMAz5i49yBD6F4KGpWgMs1udBTSu8pY1ll1yKsjLXYtuDjlh2SPCc34ofHI8MVtWuSQ3s8nrfLdw85uMlvrLebscP-T_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dk7g_zgC3Rk-75CLKaGvnEFzCZzXYdKIl7HJ3vD-2jipXDr1RiH1pdiw3sLd11veMLB4PdJG7fx8WH3qLHKFfKRjsYX9Ubr6xHXp7r-KDgaJhieXDAcb3a_OGwYRLYVzjDcxAMKfJeMr5HOLq9wiOEwnrqiMmHnZaJ0Mo5vzG8JNPJVb_VSeyKmUt9YHSAHxtYRFwIkp6-vI3ZZgEAt-bU8rYPuSrDkpDKH1bBoKIBvd0L-nfFZdZpnPNuMktsaZ0cnPdoYN2Dk5EOmj6H3bitJ7DsC_YYBnqesN0jrGXWzxQMGM9fiCEq2xYkY--tn6Aaya5i39-7_NhGrMI_lOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ep-_RURB7bS2jyU6y62trlYssaR2LWtfQqCuWppiTeAhErccDoFVj855ZRKIQzZk6GDVtFWhHYVhTm3N7X1hSFqjUBHmd0VhDfSGYxgTaJ0zOArXdkZ50Qw4CS59TiFSOjJxAR_Npb9gXagoV2DsAqlKRSyumqgFKr9p3iJAxwa24iI8zMzUyw8z1Fi8jc38P5gr9LTdnwQ_idA0ti3sGrtjdmgdozkHfWaQdT2GXV6jxrNVbK8Gh-Eoy1Mz8F8FmeMcGCgsaEuYAUhm9SeUItX4GlTN0aRZLohJjdf4jUgErsw4Zq8T3otvuFxC5fiCt10veum337tvghJLR48DFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=WpPLdnRcSXR1ic21I8t6C4PPilxQru23tFG-RT_0crJzWOEahqis0cQ6JvbGk-kb9ptHWcT_uV-TBXYGgMnpP-hYJFIRYZJUx9o9xtt5tHf0DCg5_nr7yUHEkgVZO9WsGuCSbdwBb_DZOl8OsdkPFHtljokQ2_Wq-ai5ANMDhstYmnF60PXoHJarPDV39V0q-Kgi1of__QelMzLkgd__vJ5laaas7T8rdjsNVRqoUxKRTCIgsiYXQsCJ7V4e9sJAvl-gK6hVmtHaXezhwa9Z7cUgpZeoiSPlxXBGuq3UDhogCcjF7_c1ha-StiDTUjojy-NA6KkWiJKiPgrWer8wuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=WpPLdnRcSXR1ic21I8t6C4PPilxQru23tFG-RT_0crJzWOEahqis0cQ6JvbGk-kb9ptHWcT_uV-TBXYGgMnpP-hYJFIRYZJUx9o9xtt5tHf0DCg5_nr7yUHEkgVZO9WsGuCSbdwBb_DZOl8OsdkPFHtljokQ2_Wq-ai5ANMDhstYmnF60PXoHJarPDV39V0q-Kgi1of__QelMzLkgd__vJ5laaas7T8rdjsNVRqoUxKRTCIgsiYXQsCJ7V4e9sJAvl-gK6hVmtHaXezhwa9Z7cUgpZeoiSPlxXBGuq3UDhogCcjF7_c1ha-StiDTUjojy-NA6KkWiJKiPgrWer8wuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZBgm4xcqwJeogcI8Bc0ouFKKB2e7tGH8CtrpxDA2NWsTenqFED0Y-qyfOE_Xs3yPGa7DCYyAhwf0Wg5AdX9QsWY5pR-EdULCi9UFCH5aFcX0wJGroUG3k89pbCJEw9OB7LacD5vsrOcWWny6fhyY_VmqWm47OtQGcv8dNNgEAMXkHLHlsc2j8birgwVusM6T5lEzDNfcEFW5ApO_db0u6OQEzxRUxl-d2Rkm7AWgsHYSm1i7sLvlQ0uM77uFZIuOeQQ4jhbPC2L-4d7qqxMYWUY6BRu9vidinjcCWVVJktTnUZyikUO5GyLLpW1-hKSU9tGwYhkQIqZrs2iUJkk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nHyQlSMjS-Gpt1ctNa8490E6ArktsfcrIc2p0nhg4Ts2fF_y7a5Ot8S5Qq5iLvcxOZylpI1KukIAw9KEGxG-VH4rEDrsPZVwyyYigau1SVa3H7KCSlWcF-N0NJfCVTycmtHekeFlb34Svm4My_Q4YS6wZ9Wkhf2_wWCz_QOVSw1A4b6_tnNYCqU-oFeDcBnvaqYDRevUqb6j7JNji3q6mu3yVtqw35dgzaJJsnXha9juuhPBgR8Y5pLG6oVsyFPwfu_RTTaoeNMlPThObxW3hgOb6WP_7lYHCStCvVNJCbMb-o-EDPJnTjV7n9L2RInZSG-7wThpl7PpN5UZ8kY0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qvaz0RbVJwHfWGLEIvzwRl1mgZlhN4Iaia5EjgxM49r-PMBjq-eNuEC_zU2GAuzG2rHqSAJEHQaMSLSavHqi00H9JxY0bErG1bJCbH08jjV0KN-q__mRhXSd61MjV49T-mjkmIR4LxuoRxYPPSJMQzuy7UfaVMd_oGiqQNxm4p_scq6MIT8A0n4m9i-tYFo3k_P4KLwCQRJ3XR37gn6NP734CmL4LPVHHFOYlrhDG54oK0GI8lx_nF-LrKMOnASZTbnyZ6qONK3UY_T26VTWWjI2ItdlNq09i07D9A0NWXFAwYl_v_cOG8YPiHl_O0CJaS7X8P6I6mQvn8SNli1Teg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N581F9R8zfeOpkINB-EOxyqUapyIcWmDcWA-pkXrbpRKW1J5G_B_MMSilrVrDgzlBRB_H1qfgsqhiXHuwBxRNvn2qiiG-sHTIi75Vgem1VjjoTXModRIosiQfcRtWsxpsr9j1Kx9-bv6DsLEWRxxxaqKADCWiNiCSW8DtFdtYqmuYjAeourSrdYMqtz6gqyxpW69oFS7p0S8aprTxWaFUJQMlOMdUcrDhsaba3tLfFXPVU-wFAyTDWoq4rZniQzO8AeD4EzOKYlQVbFRAqoHUQyYPLF6hw-urPSmOlTde0rGRw_kK14mj9EA4Fp5l1nHQN-nIAZQ6A3a5HHOZZZAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OK5xF5RKRqlrWdLh_iFQjUrwqNRkxLvJxzqKjsOloyv6egHu0ZwZO1d2hWPNlVfnyy_dYDsCTGatPCPKVfrxVLnBNS2bnfxEmyrPuMHBGlkKh2-Iir5V3u-LpKpib0_U9-3Qk6yrvdhPqn6V7a_gDNwaRiGjo_q-l1heZH7ZP-RCypH_A__K38W4XKyoljylZHXNhLvHi3VxBVIIBYlLNwtl_Pf_molOw1uvZNqBPS1OdChAdPlx2qEzwKfYTiSHYna-llsG12PzXVD4Z_Z_PL7KdizIsocd2xKWE8Jqyrz2pQTzghcz7gLMIZOmsPuSfJ0xZJ7C9bTJnRxiGjVCsjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1OK5xF5RKRqlrWdLh_iFQjUrwqNRkxLvJxzqKjsOloyv6egHu0ZwZO1d2hWPNlVfnyy_dYDsCTGatPCPKVfrxVLnBNS2bnfxEmyrPuMHBGlkKh2-Iir5V3u-LpKpib0_U9-3Qk6yrvdhPqn6V7a_gDNwaRiGjo_q-l1heZH7ZP-RCypH_A__K38W4XKyoljylZHXNhLvHi3VxBVIIBYlLNwtl_Pf_molOw1uvZNqBPS1OdChAdPlx2qEzwKfYTiSHYna-llsG12PzXVD4Z_Z_PL7KdizIsocd2xKWE8Jqyrz2pQTzghcz7gLMIZOmsPuSfJ0xZJ7C9bTJnRxiGjVCsjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YmISD0PogkjpKYc2-mYayEp2ZiaFRKqJgIEN9MC4Zfge7Z3ghSNTvv6RcjlJjRTOLeHz464SjkiIoV3mvPeySpsYehFY4tRBhi_E4-BEIWNSHM4y7RiyMmUV19aRm8WxsH4zzo5hi-aa5hZnaS8PJOiKp6iyT2X7B5ABZ61arg75awPRCvHVT3a9rxVz6T56ZqPUTfsLOu7z0-qptvxSVL55leF1_gBT0chLplytCFhKgc9jMm08yrOupajaPpmDcHqUNaMVQI9r0XH-3BMRsBqICTaxrdOC3sHuNPZWMTWBINllWlaKxKTCPMN2m21KGjnAWfpxBMGvRUWMAZK10g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HLMAJT4fpmUSSZWpS24eZkx8u2xnApPhQw-lRZeyJYB3NH_-dTR5r4t1qp3Cah_hCoUZUVKJI0D1HZkkfdRG61-DILdz-KZwbu0eI3udhwQjfE86IdW3YmiYXKdKlavv7Ho3oOycysmuSZixkQSd0-q0RBFUngKEqjjO97Hhz7a0LB-CNCHOUVq4kQUjJmGMMna3ifGmPXmbMZ67kkQBIelc6vwn9B_Mt6ZzgNWDNqDsjfoBvWJHSf6PzbRrNFsfl0GGX3iDdOKXAgnUTTiyKs03rvsXvWVpEpaqcf_-fVy_jce4TU_CY3i4de8pImOz7Fpuj2B-K-oPPu0ghRoVng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=L5dmJS13T2G5HdGqkpoyb0ZG8kjXdLbNUO81PGcWyxQBGGJSemQtb2HAheCpceUKIPHOrp9mIMLLpmlUpFp_D2RynO23XMQrAh0pRO7fwwtl3BZ1kM5zzYJmFUD9R5KDtws6_VvCB4FxJP7SqQcAl5EoEDCHfYNnPIesmbwiEIZcT_7BXiCUtEimNKauD5kIiQ1u3ZpiUBJJBYObTPuvtDRmpozwYet3pQluduGL1tVKzoUT1Qb-FUT9_xLbVxXSENqKVrYs2tIX0xQi5zsR6kXBEaEzg3JHTyUdAIhAZElqBgs9xETWChTsMnx24avn9AthjG4iYwcqx3AQj-_NZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=L5dmJS13T2G5HdGqkpoyb0ZG8kjXdLbNUO81PGcWyxQBGGJSemQtb2HAheCpceUKIPHOrp9mIMLLpmlUpFp_D2RynO23XMQrAh0pRO7fwwtl3BZ1kM5zzYJmFUD9R5KDtws6_VvCB4FxJP7SqQcAl5EoEDCHfYNnPIesmbwiEIZcT_7BXiCUtEimNKauD5kIiQ1u3ZpiUBJJBYObTPuvtDRmpozwYet3pQluduGL1tVKzoUT1Qb-FUT9_xLbVxXSENqKVrYs2tIX0xQi5zsR6kXBEaEzg3JHTyUdAIhAZElqBgs9xETWChTsMnx24avn9AthjG4iYwcqx3AQj-_NZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=bzvWRPzqu6MgpZwFBgCga2m-qS40kjr1L5WqIF4E9V7x7CQmsFec93NyZ6ns0VsV8YftxvUjdZnXovdzaqNyM1WVl-5eqjRDYYa6Vq7eNVxbzCnLlJ7_FLUlkobvHdcqlLfLapBzSHxg3uKvNv2b_3hPZFkS2NfL3X0CDPcQ6TWBpGd-WcLLLIwGmRJ-ooypgPjw7EY36LPXVKU4kdW6DGKnzn15R-OAex6lLOin-tXAQAd_GmfDPy8iVSR4jnivdq5nvwQ_JpcnPinri-O5FHghK-pMZ6dNMpGBGwN2dK23Motkz-EIHivUmPDfoouvCZ09X1D8uvtAksKNbFhNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=bzvWRPzqu6MgpZwFBgCga2m-qS40kjr1L5WqIF4E9V7x7CQmsFec93NyZ6ns0VsV8YftxvUjdZnXovdzaqNyM1WVl-5eqjRDYYa6Vq7eNVxbzCnLlJ7_FLUlkobvHdcqlLfLapBzSHxg3uKvNv2b_3hPZFkS2NfL3X0CDPcQ6TWBpGd-WcLLLIwGmRJ-ooypgPjw7EY36LPXVKU4kdW6DGKnzn15R-OAex6lLOin-tXAQAd_GmfDPy8iVSR4jnivdq5nvwQ_JpcnPinri-O5FHghK-pMZ6dNMpGBGwN2dK23Motkz-EIHivUmPDfoouvCZ09X1D8uvtAksKNbFhNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=O7ZLbdyejxpFNkqEjuZi-RnQJ8oLO2daxI_hNKTcXfqDUF1yMtZLIGVQQHvAfK6qNA9dBV4S89vFo3BQBgT3xYbAzB8_M0W_yht0lOA4ZPltHHqG4k93aNDM6oRMDGEvEftaLl6fU47MpwEIgA8AcKCn20UKBnx7WHsrDJa3UQYQmazc1l780RnFiHZTUvKHC0QjwEuL-srlJ3DiUtkzRTogWEW4psQGuIhsSbXun7oql2RujLfqVhUx2o715zAQnWRS8fzgbA-26Zac545cye5DQRpG-b2pvTbwmbyTvf57sw93vtC5BxoMqMxS1FSzgrKTDJ-UKtURlEM_2uJBDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=O7ZLbdyejxpFNkqEjuZi-RnQJ8oLO2daxI_hNKTcXfqDUF1yMtZLIGVQQHvAfK6qNA9dBV4S89vFo3BQBgT3xYbAzB8_M0W_yht0lOA4ZPltHHqG4k93aNDM6oRMDGEvEftaLl6fU47MpwEIgA8AcKCn20UKBnx7WHsrDJa3UQYQmazc1l780RnFiHZTUvKHC0QjwEuL-srlJ3DiUtkzRTogWEW4psQGuIhsSbXun7oql2RujLfqVhUx2o715zAQnWRS8fzgbA-26Zac545cye5DQRpG-b2pvTbwmbyTvf57sw93vtC5BxoMqMxS1FSzgrKTDJ-UKtURlEM_2uJBDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSWsrtmUuFzAzT9yHdX3DqkjPF4g2Qx60jKhZs5nWf0HndCCXDrmCxcnLDZn8a45pAFCuvtlb3Az8qWINn_qCh-24frTCObuCdmuyFF1VtZ6uL9TAJLOUCn8yB2zGT9BBMvV0Ugag07OHKxxaXZFATtpBs4pv7aHJZ95YMOIXsjzROeHxkIU7ZzJqqKRWcBH2HlYq2vKrWhmzzuP4D4IU7LKgE6Viz1HBd3CqR-OcofTpysnH2pO9kL9UZnnkIiEQjw0WJPFMpVpZICg_vCbDeBv_WvFQjg3mELYxMJtTvYgkHB-UxfneSXr2Uxzv744jIXuESW748nnKpT2mIlFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k9q0ds0utVlmZ29Q7HV5ZLJhuBnaxbv1ZbtS2aKW8_uIBu5lEGfr_ofMaSumInDBo3PBOPsonfvJdrUvIwHqTSAuqQF_AjnU5KY3HpRg8DwgwCfN2fUoCc7IzqYVqRyVhOAXTucN26_7VZUgxuyHb8Q4snpGPRlfEXV-Q2q6cgNA6cMwNwNUekx4qSJteGbHLNA39ctiy3655Ko4ocVNMe5wuzJMIoUlrIjU108EijpJrM8G-sWY2gyYRvW0QnNUqbmHZbST_Y4Epno9G1HEid1aRMpaBATV_h2qw5Z9IvvxWiU4vm8EyAsGrkrWMeSzRusbD4SEJ54ogmk2rKz0fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXK356Gg--2u_p4l3xyCMOYlIQn7YV3ZM9XsVfi2HYb0BFlaYb_vhDje75o8eg2gTKXOBvNJZyyrOgL3FHhNfPdBtPxqNJQm-AcD0VXUfeKnDJKVYWBGZsdiWATYZx3Dr983ou9xYvOThiDEeeUjeJEKErHjdJfpSxuQkFvA4g1NB1DiqiKMUZNpFJbnqc0jWFhpzYRI9o7_bycR69P0vr4SR-7XkprThn51yUatzj3QnF8RfPOb6c7dMSIHvjqZZBNNIaxkRSohJpcPYyILnLzMJIEcPsuGhAO7Xm1O0ga7T_5NutC81oaiBw1MEUzwwyVj52dXOpkFr9Zoks06lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fnGApjHsxx5iUmm4BjGvYdPaRdPMuW-3K5yzX_eF8yQUDcVTmqGsIJ_vL9uetlLFbK_Y3QOFY8VNk0fwZmph7H76yfi-8vCYf_xgrXPKON5tZ2hh_SqSHzHdpd3eItDC8_wnNjG5eOMuHXQuP_BwcPwhdlo_xvTo9Tf1AoRJ9UoHRvkXEg5A1F8UZtL0sQprNwtWHmKRgYqm-zKDBN-n9wZ9P9V5avIOZtFK-RnFbcfyFw3WVNmfy4x5en559r0OEfvvbwPfOWwsqzjov_abl4-ki3vcwJ3Jk9XY49ovK6QlkRVDI5jEaGFXAwRn1cZ9r6kL4W6HX0_VNV84tRgB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RwbrGj6PVt-KDVVKe61-vk3ivCbCUsIBDKLvJMOfUzX_edophImuDf1uApHlHdKcR8J8g7QPE6ASSwP90Ym7i657RfBAnkSQAn3gj_Ov44K7q5zgyeppy_8rrCSKUz9fXKLVSPmxeTcgI_6qJ9KmCY-X3nHzvURzX3LbRaYov7eQhtqi040t1pufxwalc2mdiII3-y_a3W-oX8qqgKuNvDhA28JcIrqVYSly51uKYzCX_UQV3qULoVczJoPTq1Xzuq9-AX1TmOrMnbNfCnlwFfc50ZevWCbtr3JuHh6v1r0Iw8olKzbg6XgmVKxoiCQE66thYqv3eX-0A7EtQzswuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v9qe6pMYM7MjFehogFvmV3Tnn131VbZiOL2VGO88FJ6Kh0afxE34U2RNutnqJB_S3s8L0GRJSCT3Ot_7EerYxNltBQXQ6S4ukh_kBV_Tmlw1amy9P7JlbOW-AxawOn8OK6u2S6-dvd55Ped8i2PpjV-uKLvqEYL7y5oUlWEuqx-WSgGjOBinPJ0cEkwNcOo15McqtRsM8t29cm4rqG3CCSu97ZXz5ZvsytEqyom4ZgPw7P9tipLB05Lf0B8a6jZrcTlTprulaR6oFF-uzr5tKOdPn6KzrGw90WObwWNS9pGpQA3tbxs7NBoqkzGMFbm8z6HCOFtEnTJu2gEI96Z8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ntQBHeYyZLSU3DnklNrU43AsYdboE7oNNC85tx_mVmEDRLenoV8gG2IFqEZwvF1ujWv0pNztN90oaPCvHsSZWhZJE-_3BCMFS0iY6MnW-Kzda7LJckor6cDfQ21ArvJvygEwFRYspQRa5joNZDTOiyT6LbcHIJq7WCagfdop7_f6oIlcINeS2H-MTtByfa10fFNddOEPOpoaqWlPyJzYcEkYHx7x_6yrGF-7OuA8_1WOYwg7KFMEkVHU03FgqAlpG1TzIpwXMcketvEPXZLznS96neayLtcv-TSw7pP8FjUsWfLXXVf-IcoeJQVCSSKV5RGvRJRFnPdod5SDz7obsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jvacb1gCe7b7NOH6-w10beOaAFzQkxGAMccaA2Y-ms50kKRd49Oj_NoDprEL7xWDnioB15Yhfju9wdExSpwTUb85znteS7SO2f5inMxG0Z6KwvYOXhNbmu7whv5TWPVvsrUFmwPuC7yzWAGpSdVo8c4NztruOWOMkFEKUAfXf4vEydGxa2G4EBeNjN9o0K9nXK4-OC9nPhONBFfJ6C49FquSyyUH5dlnlxin38Ek0R7kD11oquvU6cha-TP6hAyD7JkuuqVuPkrAEOr3Tm2AQ0gHbn22ty_psAObmF1NYIYRTiC_gI303x0J0sL4O1omUIPIiLz8GaB_iJ9CeJncTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q_GsPPIQE2kQ-_zyw5BGgdTpTb25MY-hqsZgyE0VZsQ_p3qeAkqPxdecbh222_QNdfeuBfVu_bMAs_dRLeoy7ricCOptqdFeOPHMecUamPvuuj10FtoEUXnfniWkMDkWmJvakzu2K0fJfCvkPXrAjAflatVjzAo7QfRpenGe89XGiQf3wZ8iX2NPpqwtq4dck5KCXcdzw2HWsbRhVOOEvUSEjtlk7MztAzPJh5LGhgCkdiTbGR0BcdVulxIxGIqZ3Y3ghtllXnom26FyI_5FwHyfyQtP3cCDtuIWYh11O5_sRvuXwHzXVV5fvrH7484QUxAnlsFyiBGvRykV2jgnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HEBlnacSjLDfY1a7hvKCM1RJOnq1bScojVclp1dbQ0NU8qvU7R-5uf7ALCQlm5Bc0dbaXUclYSOXvnjBwcoXlVRSNFl1XBw2YW9ectW034Zcc3yYt2ESCKmIBINs-LzZ9Dv0a7UY4Iq-EgQnSs6_0dtPJaGh4AhMPJ0LVzAxQ5m3rkbr_CQ_Z78K9sesokGUEljTuWIQBGvM0KXBrkr8Cf40dngDDXRsxsrz2jJBs6DtoCtJ_uyf7Jy8deetVjkoG6ijaBDZiR10QwBejxNOO5IuUECwTqQbzBRWxqutH9w0BtVJ664i8OxwFnYz-5KXCo6bsz0a-hY_0zAz8caOfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iQcxyMgVRyEN3wTGOg6rsGxUqjODRzjIZ9cpIRjv1ANuGAcgwV9QWS0lOchmZMqTSBY_ydjHI2pVUE8G5O1J0DMKEOQ4a0ponnDbP00T4OOK4mMpi8SmzMLgZ1OjraK2c__6o8QK2o0bswyosNzRcfaEGNIQhHBt-5IHBZyHHo04Awb1ymjPyqRHYdLtcviJCGjl9LaTyllr8hcpqEEX1O3C4ZF9EVicozoh6hAqfCS1eTnkA88ghQ8lyhYVdqffFqr93PT_JkXpuO7ljEKkTWa7iIGKz9CRBRDMIKHkudfHGHV5oLn8fS2lRqlm2fLl-Oky5xar8ivEW9CruJO6Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o8Bv6uQS-2HL7IzwXLsfDUBT_IGgfUEPfCInXIHlZnlYjEdNlOyCnv8O5ald5mrgQjt_iZe17ijCmOiAtdaqn2uNTA9hWQFOuxYT5ca3DETVOtvB1b4lI7njv6HneBINw7SblFLDQTVa0cI6q_ZUuqnemWIBe-sFJ7Kcah7ymka7_YVG2ULpgZ2lyzXSqtEKDKv16wEym9FCAc8cQu2ePqMYewgG4HLgU-5IIwYt8nyglCP3x8xIiBl3fdGl5Jzk--z4ktIRQxTPTvzl1GAbL8Fz97nEijrM4N-iWHKlkOSybwFx2j1_0_XZMdzphVn4J9w2BuOw443TaDKiqvpcRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkXW-jy7KLpHU_uiS2Rptzj84KLUh7J-MWw39a_Y6T1nD3NKEJACXAFCjJ2UyeftLs-sq1pGqFGGVS_pXDuCNc3QevUHR0yj8LydjagV5T5LGNObRzrRiNUBjyWzx_MYXhouc2Xcy7ql0xcc9EAW97ZSedDQOp3ybtkDivpuMliDYkrXKR4vIq1z0YOag2KgWg4w_8jXM4LhheYyfn5x3jOeKUdH3265WUBRF8BoB3I938TK1v2UtAdvkcEu6svPt9r5fVpn4FqlCEUJJeHobca8cnTTvMl0lEDAFToQQCFMsTADHvwTaoF0helv2x3qF8fi9P4T9Zb9fljqg72cXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM4PcFVEw0mJ54A-n6P9ibr9SH6Jkj2LycB7iYGUWWTKeXL7j2jvYOP4gQ3Khg2mqnH9Lnhx6mgPSVdU3iqS-cET5KaI1Ww4VULaPSovptzHa49ETPOmLkxKN4-65go2vJVPMvAndELa0ID-GC34w4-KcN5HsDZpPhnEFW7XY4klKN7tvVT00uOb_thwVJS8kG9PIXQn0oYCvgXpGXJD8k5s3bTvOsX7K1PidrEUgfvURX1G2ZV12zngRkKVeykU_qxK3oUXDUDklQm8VMg07T9topPnLgPs1ZMwcdqdvRcrwtbpKUiUM_i26OzdktO4c4G7IDvp0-SbMCZ3uY8XsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=akensltB5gDQ5xW3eeQLeTz4aaJMuBVZVn7LBAj--pj7kU9D-_Z4Y5DLJk8I92YfKEMPrd9O_q2o7cNIi5pwA23vpRllBzwm0s6CR6H4nEzEbQst8JLlaOhsGgy58oU7A7EVsLzN30YLDOLnP7GJxA72nAY3HN2QRgRlFo86ufPvYGQgVsAOoYCoR58-PcLIj4yfWEYMfqLXfao6bLqqeTtQmHhrvttrKeo4VGNvAovXGNc7sJc-P426SFr4yE44rxFqnbxmwRw6foT4zTKKlkLrIXHpfKNyuz02zwTEDl8ssYXTvzwKnLEcunNnCZo1rvUlvdgPnY-EcOvBvaz-mA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=akensltB5gDQ5xW3eeQLeTz4aaJMuBVZVn7LBAj--pj7kU9D-_Z4Y5DLJk8I92YfKEMPrd9O_q2o7cNIi5pwA23vpRllBzwm0s6CR6H4nEzEbQst8JLlaOhsGgy58oU7A7EVsLzN30YLDOLnP7GJxA72nAY3HN2QRgRlFo86ufPvYGQgVsAOoYCoR58-PcLIj4yfWEYMfqLXfao6bLqqeTtQmHhrvttrKeo4VGNvAovXGNc7sJc-P426SFr4yE44rxFqnbxmwRw6foT4zTKKlkLrIXHpfKNyuz02zwTEDl8ssYXTvzwKnLEcunNnCZo1rvUlvdgPnY-EcOvBvaz-mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qyfpB0qMlip1B48yzC1rImUA2Lf_PtWQ2f3fSioa6h3evo0ujdZ3yZWUPENAzAoaVce-UGbnFITyPmU74no7DJ1Wt4vEon8hb9Ubcw5IabK4AIm4YTpAMJy0QcQw9GlPM7BSrWjIOT0OQv6Wa9AQssLgiDVZAz9IvjRW-KQHKuAfItNfgHx9nZBKAT7zBTHsmdGIw0PbmbIar_nfaTqD35XHcWgUovOfQxOY02w-Wgv50Bvoin_GJ43fA-H2peTcIBRge_ESqmLUKDPVnHZtJW8i9UqaqU20K9dBnIr3z5iHYJdXPV3XDtxhIyTB4q0QLeHV4Zuk7_YSQNai_CAo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mIXR3kZJJjRcaeA-DWAS4haWrV6qSzhdetmuKGHusOp-a2tnDocbVzqgEBIZiOyun2kUI1n4cii6rykFvXwq6UKOZ7F657Uyl1ldZcnMcBEgzJGMKkVr8doGWMBvy4Br1is_y-jDb-zyH-WNermKQ-J1hhH-AjVc0WBdFc8vo70VgwZP2B3qae-UE5Gl45qnXCpqXOtS1QMlK36R2VQBAH-R9w3PxH2bpE5cTWuuYJiNmjYjPVecHophAUu01ltLT5yqGfdsxQI5Na2WtTv3O8Rg2IMsZfAHX2pbrcDjPLKTyXbIMvtKRzGXUUU6I1B36072AVUvAn3fyoS87J5Ehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NSvTYoPmQKRoVfFAuUQ4f0o-HgbOcjR2DY5JQ1Eqt89MGAxYP6G5wYW14eTnh54F9ckCjcAw-9H1VKdM3H8skse4GHQ6D2MgsRfRUVIwc5wLeLCl2ZJ2eBNx8gCkgADHLWVT7VmuApUxyOBuAT_ek5dUy88VsHDcLtFyp6k8OTH_rSUNXWONonoJ0IA1rLfnVq5E_qMOQeKOxlt9EspjcDlyA_aBkWxeoi26w-I9tBvhGE0hMVtKUi2Fbga0ocenvpC6eNAmsLackTCA96fF06OPC76AT0SS563huFbhDxv_XNbPMBcK1BDpjDcl6g63uXlCrwznnh9gy_WmFkIT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PKMx3Xqy3aYkA50vVc5YZqXtNRm0TGfHpviBDNpaW-LKIs-BhnQZAu2w_kbIZEHOIwrL-3CHzg7kssedvuFbXRgmxi1HeYKHyOxyWVL6k4CLYQPQrUcsANBy7WCH7J0OLUpnm3vEKu56kZg2SIDqmHj8sYp7kZY1KHpRIPfuGfFlrUUPo8KxtHYt0Rg8B4B7veTb4QV3uzuM8hVo5e3IhHtf6LKcaWewY29efad6pf3h_zbKqQONramJCxGbSwttFnYi20lbwiJGIF6cBkbhorwn6RIJ76kANgFVbKlY_3Agq45kVdBX5XiPZ4RfwXDVb1B8WYIHuSzURlEiPA6Ieg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ozJ02TOqkNXcdh1sl6P6DSli0aLqIv_Xv6w02-jrKfSvH04cweTWT0AbX8JskvlxzlQuAXtj6NOwkTNReG_bPm_CsSKsJts0COQwmgyiG3pRTsTOlPXiApMzbKQKBodafgY_ShIo2DoM7L8leoBNf7Og7GF1DqFrR7JflZLhwpAWuegJKaCyW3aCX4UUpFIsLaNSp9jtixUZ7jVPi0OAG287HkUhqlh9AybeK16knjbx-5NZRIV9SUdl7DQ08tQ4IVHw5rP6jlo1JZbr462yPzICe9Xfcz8SSDfJM_DGkLI7p-XspZ4aMdsjenVuRPsdlOQckIriPlb4z5iCp9hAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vlrp36OqA6jiGVcFd02EX1teyovW9XKTQPiqqimMflM9ptq2wZltEHbf780rsGtP2qECBlABmHk0g_6K0LrZmrFUzdzO92y-rFCd_JD4RotTjRMmery35sjnt68ELrsyasSIJ17_tjRVjJ4iXl4780uvgP9zkRp4xd8S4iKOHhhDvc7nkXkuofGokNKxivR8NvVaGPD1iaj600MFAFNWJCGeozJqcUAfW3HcdFHUHuoNJvcmMacjBCM-dRGFmgCbPgAhYRZRJQRzN1b15Sk3r5Fk7pSxxr6Y3SE-AryWvL4GbSGxpYARDkBWnT6JXeBGIfI8Vwa3O83gemVRHp18vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=qqyOH0Gbtetf4KMpBxO4DzcQn1ONBSUuVzaGc7WtzFlAor4RxayVFzz3hpkjqO1Lb76LufrCveIwPgnFgci7UK-a7FipsDMvcSk8Eg4c7PCh9ylXlkT6Nf65dE5LuOR44ycLvFO7cHWc5FE0adAUKenOs6CK501F1OQt7bHVQEGMpVdSlslMnEvBtPiuBDFA-ccYukSu7cWQt1raOMlau9J4BwfkZIYWcXx_oqzbNQvz9fEhC23U2T2bWEfW51tDNR6WLlut34Vhf63FvvD2-R0pVuZHj2CVLItPWF6_7_7DxC_sj4UZ2gVVWS81oVLsPDhSmFurPpaJTk_MsDDktg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=qqyOH0Gbtetf4KMpBxO4DzcQn1ONBSUuVzaGc7WtzFlAor4RxayVFzz3hpkjqO1Lb76LufrCveIwPgnFgci7UK-a7FipsDMvcSk8Eg4c7PCh9ylXlkT6Nf65dE5LuOR44ycLvFO7cHWc5FE0adAUKenOs6CK501F1OQt7bHVQEGMpVdSlslMnEvBtPiuBDFA-ccYukSu7cWQt1raOMlau9J4BwfkZIYWcXx_oqzbNQvz9fEhC23U2T2bWEfW51tDNR6WLlut34Vhf63FvvD2-R0pVuZHj2CVLItPWF6_7_7DxC_sj4UZ2gVVWS81oVLsPDhSmFurPpaJTk_MsDDktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TbNqXhzEDzeVBHxrVdXW0gHV4sXqUXZua11U5aox6VYHoZgHYo42DiTtND7Wmg_uFS3bAyZF3BbHelFom0y-LU-ywt665aSj2SgwzoF4o4BHl-D_EszstBkxeelntMzuBukaBrZ4pwSkmcU_asMk7QD-ZT5w31cH3w_u2vz7Fw8BjSOWJc_hG4zlOBbNHmd411_XC4OqKd_S0x_GhjORjf1vvfJcneVmu1TvSnHJc--pwXROeq82dQPTEtfuIKv4Yas_Buy5brr7NEy6VwydwvyiTaFN5hcmDD7pbcn_S3Ofs99xY82yACB_OFXKHSeCWtjTxgye8xRcp4L74D39lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=PW6Gjrh__tIXGyqU3U3w3JoaK5ZhsAjE1HDXwGawlqWFny88nw1azvZbSwlX-1PRnJkkaQP0NbUIEaHmhg1ySoU9hBx3u3p-Crnu6-WyG5PyDlwFxNa3TImuyBci6n1zqC63xPU1MkUTb996H0r0qsZ8ihOpvxynI7EGX4AqgYE-JUHjP-bDmN5QXeDgY4Ge9aGgxZF9zqThQ-ixkT-HGAW2NLPjtAp71k2FLSLWkD8n_lp-juvvxNT4Rv2gT9UmcvBJUhmariJEU7glD6X2rUtKINv_idoC4QVznG1BawX_hW7Q5or1PRFYdEIAMpRMzVWNw3pt69bYh9Ivy6qkyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=PW6Gjrh__tIXGyqU3U3w3JoaK5ZhsAjE1HDXwGawlqWFny88nw1azvZbSwlX-1PRnJkkaQP0NbUIEaHmhg1ySoU9hBx3u3p-Crnu6-WyG5PyDlwFxNa3TImuyBci6n1zqC63xPU1MkUTb996H0r0qsZ8ihOpvxynI7EGX4AqgYE-JUHjP-bDmN5QXeDgY4Ge9aGgxZF9zqThQ-ixkT-HGAW2NLPjtAp71k2FLSLWkD8n_lp-juvvxNT4Rv2gT9UmcvBJUhmariJEU7glD6X2rUtKINv_idoC4QVznG1BawX_hW7Q5or1PRFYdEIAMpRMzVWNw3pt69bYh9Ivy6qkyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0OGJbujj7ryB5QZ3q3t5T4hDxreTJykGWR3kelBgT3w7TG_sapY7J5FbczHYFHYN4nZovsQUdZas013kgymC_hrpAy525VjipvhpB39M6I1-v03ha6OvK5riocfCZCq8BVl8FKIIzeZ6B05F8I5zYWoYJQMck7g9PkcQyH-LtuE06Maz1BE2f08FcIlO6KjW8JI-4_ZDyOyP5XqbQqNteDEBoo4FBlfqB4mXPEWZuFxqNv-lrN1kQq_R3j6iS1OD4GdCD604B69_mwmvtKprSOTdYO-ZqVxz3IWQJvVVw4jEDeV-ce0ToArKrHwDSRIzL3cYacTcGs3CjtSadXZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YbqpypbvSjKdXcIvPaUEd92tvUmpEDr16OwLTBOSnhj81qh4O0cSM0-zCfg-qceYAYuOMMWcqpRT4cIxfsF1OMyar1JXyoyW9SN2CB5qG_uppLfOupLXZ8_74Op7bNv-qsNjlFnpJsNzuGTA9H7Htv0bHqDkOincUyjE2wgoFUZ4GemxFLQ77w8QRbEPGJqUdEyyYEaZJXFjylWO3WN2mhZR9AJ3DLOgbRWwsowDFI3iV0atqhSxuQQZo7v6cuxquIfst_lvqU0IMQcFhLOjP68QpIM-wkM-a_JFKBrDzX_GdcOY9pZ70FLhtXJJUAZPmE3nhrQXP5QbWk0D6WV5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGHV1EzM352r3_D3Zz9MuyAhsNmN1M850lyCWWPUrUEuB5_C4i231_3QD5fTG9R5DcbUintBOGLp0_WXurSSmHo6dAJxb5ADOb9Dj29So4LCE0gUav8m__66Y2duBGHaEeLdM6jqhed3C2qU4egW4LoTRM4q5BynHIkQZ86cr7TTK7QUF8KgKDSzRuWh7rI60Jk5xff6A8wIovS31OMLTytk5a0HOliCCYhWKsPM-x18lMaWIfxx4MbCzSsTZwWsbuW4WR36b45pk9GNy4DC4eKmfCXUS2fznF5yI5uKl6fnUUXNy-HgaU_1azEVinh9BhoMyfZMxwe5bMGtPg-qYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
