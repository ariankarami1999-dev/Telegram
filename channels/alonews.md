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
<img src="https://cdn4.telesco.pe/file/SAD2gRopAA04krslXDmRC2q2P7Njjv-B7xhn9_Gt6r8BhppH_VbnYRRMURnUWrxBzHbOlUE9Z6IX_N4VHIF8BP-ZsOh5njNZ3FlsBsjghsswC3RI_WUO4KkVYarF7-MGjx_flhitWnbeDx6993UlNojhYgh5AohVmw4EJxKlo8T8pgn2_8N2npGnIbLUhJ09IhK7vjertztabP1W7_bfYnAhl2_HoZeY2Qt7qf_Ro8hwjbQsKcmYcPn6f03dlKMn6l2EXP_3LyfbScqEWhjTtgb9csW8q3uN9JL7eB4WdwKRdmkPk7L8lU6gR9VgKf_KS9czwOEDyZHRxhnblaMHvA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 928K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 00:35:10</div>
<hr>

<div class="tg-post" id="msg-130980">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❤️
حداد عادل: محمدرضا شاه هم مثل پدرش عوضی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/130980" target="_blank">📅 00:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130979">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngG9tRf_7bUJ4QwFHp4htz3fxEZrvbVqy45K_7djZcv5iXCjFr8pWc_IHNWoWNCfZ2fQ71gEfIrnfjuXkOc0I4xAaoSBlXc_VL6DecpCLxE8JWgazAleYwh1SCFUsmBYzNLqKVjh2lhqNgVlfst5WchUhVw2CCEaFxhC02RMtDnYl5vt-kFnmfV7VjDILc44a7D8uNQq6snL9uwZCL0ZRqX2YCN0cNYLM7YQ0n19PC8zp3_zajCMR4Zimiqdtfi5qSNOyXjS3NHwIcEojXRTs6V8Le3YSzTum3WCI-U2MJsqxVYayf7wXTHqqyMzib9J4M35CqXdml2tKTh2FiI0kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
محمدرضا شاه هم مثل پدرش عوضی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/130979" target="_blank">📅 00:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130978">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwGWXSQk6jHt8MZwrotXMnX1GvmYXdg-qG1TvHOLxoxZLbVr4alNskSlkdHAVbl3has66FrBlqynRTLJlRy_ZDYhSJHH2EnSPGm2yvk6r5DdrDoNXO7UPWcEmsfIUELySgFycb-zE4WfjOT0jQBXY_pCYek4cnfB1jQKSejbdLGohktFJsmvUmm_zLwxzbJDDBJy0xxMSVueNt9er7xlsPMztuACOBBnYLwfW2pnyhkiw6F6ujkowrNL9C-RpdEY26R_BA3osC5YnlY5hxPF2JuNQadxeWQs5NFv-MXe6yRoZIFeuoROE7JHlei1UwzSOKOLVu2zBgRP5Lyn56Antg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه ایالات متحده، با سدام حفتر، معاون فرمانده ارتش ملی لیبی دیدار کرد تا درباره تلاش‌ها برای یکپارچه‌سازی نظامی لیبی و پیشبرد شرایط برای صلح پایدار گفتگو کنند.
🔴
ایالات متحده اعلام کرد که به همکاری با رهبران لیبی و شرکای بین‌المللی برای حمایت از لیبی‌ای صلح‌آمیزتر، متحدتر و شکوفاتر ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130978" target="_blank">📅 00:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130977">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شبکه خبری فرانس ۲۴: ایران روز دوشنبه اعلام کرد که نخستین دیدار خود را با عمان درباره مدیریت تنگه هرمز از زمان امضای تفاهم نامه برای پایان دادن به جنگ با آمریکا برگزار کرده است.
🔴
آمریکا در تلاش است قوانین قدیمی عبور و مرور در تنگه هرمز را برقرار کند، در حالی که ایران به وضوح اعلام کرده که قوانین جدیدی در کار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/130977" target="_blank">📅 23:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130976">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری/وزیر دفاع اسرائیل: آغاز جنگ مجدد با ایران ممکن است در عرض 2 روز آینده و با شلیک موشک از ایران به سمت ما رخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/130976" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130975">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
روایت الشرق نیوز از متن کامل پیوست امنیتی توافق لبنان و اسرائیل: ارتش لبنان متعهد می‌شود اقدامات عملیاتی لازم را برای خلع سلاح حزب‌الله و تمام گروه‌های مسلح غیردولتی انجام دهد
🔴
تأیید پاکسازی از سوی یک نهاد ثالث مورد توافق طرفین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/130975" target="_blank">📅 23:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130974">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرنگار نیوزنیشن در ایکس نوشت: یک دیپلمات آگاه از مذاکرات به من می‌گوید که فردا (سه‌شنبه)، استیو ویتکاف و جرد کوشنر، در دوحه با نخست‌وزیر قطر و دیگر مقامات دیدار خواهند کرد تا در مورد مذاکرات با ایران گفت‌وگو کنند
🔴
وی در این باره افزود: روز بعد (چهارشنبه)، تیم‌های فنی از ایالات متحده و ایران به‌طور جداگانه با میانجیگران قطری و پاکستانی دیدار خواهند کرد.
🔴
پیش از این کاخ سفید مدعی شده بود که مذاکرات ایران و آمریکا این هفته در سطح بالا در قطر برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/130974" target="_blank">📅 23:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130973">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
موافقت عمان با اخذ هزینه خدمات دریایی
🔴
وزیرخارجه عمان تفاوت میان عوارض عبور و خدمات دریایی، زیست‌محیطی و مالی را توضیح داد که می‌توانند به‌طور داوطلبانه با کشورها و شرکت‌های ذی‌نفع مورد بحث قرار گیرند.
🔴
او افزود که برخی خدمات ممکن است شامل افزایش ایمنی ناوبری، حفاظت از آب‌ها در برابر آلودگی و ارتقای آمادگی برای مقابله با حوادث یا شرایط اضطراری باشد.
🔴
وی به امکان بهره‌گیری از الگوهای موجود مانند تنگهٔ مالاکا و سنگاپور اشاره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130973" target="_blank">📅 23:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130972">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ: ما تا حد زیادی با عقل سلیم حکومت می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/130972" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130971">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d045164058.mp4?token=aAUPs5hb9NTH-F_BI5B7Yp48QddbGT7wr_bCLGbpuuuzXD1mt-7125g15YmhfkUnDppYUBXhQGXi0ppLz3YKPhYjMwVIGRDn5bwJDhXWYhF3yCa44dDoebikKmt-36SwkOUZ4O4EBPWokIzpgjmnvIRWIElTTudBYytQ21nG9KWlAW3wLyCiO5YCvOgSeQum2IL7vVgySmS-Rb_xopUWLpWTjTsh-ln4mpOns9XqwX9e1z4xAbyoent8gf0RVjloVnwmcGH-YxlrfbPMe1Hvibd3dgmdCXDBXDc6CKlVI6j72W8lApt3SIysox9xPGtLjFwGU5jjOVCG8ajU_47RmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d045164058.mp4?token=aAUPs5hb9NTH-F_BI5B7Yp48QddbGT7wr_bCLGbpuuuzXD1mt-7125g15YmhfkUnDppYUBXhQGXi0ppLz3YKPhYjMwVIGRDn5bwJDhXWYhF3yCa44dDoebikKmt-36SwkOUZ4O4EBPWokIzpgjmnvIRWIElTTudBYytQ21nG9KWlAW3wLyCiO5YCvOgSeQum2IL7vVgySmS-Rb_xopUWLpWTjTsh-ln4mpOns9XqwX9e1z4xAbyoent8gf0RVjloVnwmcGH-YxlrfbPMe1Hvibd3dgmdCXDBXDc6CKlVI6j72W8lApt3SIysox9xPGtLjFwGU5jjOVCG8ajU_47RmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من قیمت داروها را ۲۰۰–۳۰۰–۴۰۰٪ کاهش می‌دهم. هیچ‌کس حتی درباره‌اش صحبت نمی‌کند.
🔴
دموکرات‌ها با این مخالفند. اگر آن‌ها به قدرت برسند، قیمت داروها ۳۰۰–۴۰۰–۵۰۰٪ افزایش خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/130971" target="_blank">📅 23:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130970">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8fc62c34.mp4?token=gPmI-2KWUjb0fGMIZ_ppeF_Zu9Eb29TBZZAUf0s5301mk45dH3Lmrx6QqXUzjZzUSToMiczbGDX2u5CzMWGS6vk55C4AvxPKqR25lG02JFdQ8y0gst88aNxl2mXPiCwwjUhStPkyug8x80oCUB3HnV8t7XgHGv7wvVdd9zCRiTEi6Kw9DpQfnBhgq9v8qZnxJwD-R6ejoxeCX32z4Dq_NTJlEgpTfSRJXLSUYWYYnf2k1RbIlDSglv3xal_lPg7xmiVWPeL63eM4p51kEldloGAZcTXHt7UmEToAsLt7brTCmphLERr2SDLoI1U1fQ7-1QM-2NOeSGXXiXuagu6ZpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8fc62c34.mp4?token=gPmI-2KWUjb0fGMIZ_ppeF_Zu9Eb29TBZZAUf0s5301mk45dH3Lmrx6QqXUzjZzUSToMiczbGDX2u5CzMWGS6vk55C4AvxPKqR25lG02JFdQ8y0gst88aNxl2mXPiCwwjUhStPkyug8x80oCUB3HnV8t7XgHGv7wvVdd9zCRiTEi6Kw9DpQfnBhgq9v8qZnxJwD-R6ejoxeCX32z4Dq_NTJlEgpTfSRJXLSUYWYYnf2k1RbIlDSglv3xal_lPg7xmiVWPeL63eM4p51kEldloGAZcTXHt7UmEToAsLt7brTCmphLERr2SDLoI1U1fQ7-1QM-2NOeSGXXiXuagu6ZpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در میدان نظامی پیروزیم. می‌توانم بگویم تقریباً در میدان نظامی پیروز شده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/130970" target="_blank">📅 23:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130969">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262fb7eb01.mp4?token=WGAaIYw2BZ9FjJe1tWvIj14uDHL00vJ_maqrrqub8OqUdgqMrwJzJoHXjwPAaiwfbYe6M9u1raVZya9W_m523n3F6I1zSjpol9FK5DTtbzaKWuj9m4wWDmUmMl_qD1UzKa5DcJqdGCLLzYrh4y_mF8-ZBNALt80LFKz5uPidUNwame9blpaMap3B5MRCmBpWSi8Am-y4NuBF3swrWgYMXxnrjqp6GoFSNH-7b9cCAWIEcIjRj06GqkT3FRgKNx7QPWNnnXrF8vak6I7-mVA4a2-_Z2YMlllH10TWOYevhA9SRnra6OIRSWvvkt6BTDAnjo3YbATvgKzxUUtJ9iNryJk5Q8DqBDSLSqmFqpf7oM_Dp60JQu1eWxb2OzmUlTfYWN0yy8gPlOhx8DTJoqkS4zazcgFVUiqQs70tKM9LH2kLk5kA9PdvFYZAlv5uhhzIYBtcT4wJtShpvAMNwC_TzN6phhYsc76t4KKQr7T1sIzw2lbYQ3XZoNPOVIVH3jeUWeO6gP-lt2unVQ6p99YkfN2z_TIheVGMBKk0YvxyubH1dzd7BFNgDziHQZPADLb5cCiHjHRyDpjkwoOaa_wLtNEKqvNsWr6HJiU872dEJMWTV6XO5isEWi0IjmLOazSRtMo2xRJEr5G2DzRRxPgPHZMXP7BcC_BHFRjjHOFg1DE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262fb7eb01.mp4?token=WGAaIYw2BZ9FjJe1tWvIj14uDHL00vJ_maqrrqub8OqUdgqMrwJzJoHXjwPAaiwfbYe6M9u1raVZya9W_m523n3F6I1zSjpol9FK5DTtbzaKWuj9m4wWDmUmMl_qD1UzKa5DcJqdGCLLzYrh4y_mF8-ZBNALt80LFKz5uPidUNwame9blpaMap3B5MRCmBpWSi8Am-y4NuBF3swrWgYMXxnrjqp6GoFSNH-7b9cCAWIEcIjRj06GqkT3FRgKNx7QPWNnnXrF8vak6I7-mVA4a2-_Z2YMlllH10TWOYevhA9SRnra6OIRSWvvkt6BTDAnjo3YbATvgKzxUUtJ9iNryJk5Q8DqBDSLSqmFqpf7oM_Dp60JQu1eWxb2OzmUlTfYWN0yy8gPlOhx8DTJoqkS4zazcgFVUiqQs70tKM9LH2kLk5kA9PdvFYZAlv5uhhzIYBtcT4wJtShpvAMNwC_TzN6phhYsc76t4KKQr7T1sIzw2lbYQ3XZoNPOVIVH3jeUWeO6gP-lt2unVQ6p99YkfN2z_TIheVGMBKk0YvxyubH1dzd7BFNgDziHQZPADLb5cCiHjHRyDpjkwoOaa_wLtNEKqvNsWr6HJiU872dEJMWTV6XO5isEWi0IjmLOazSRtMo2xRJEr5G2DzRRxPgPHZMXP7BcC_BHFRjjHOFg1DE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کمونیسم: این سوسیالیسم نیست؛ واقعاً کمونیسم است. آنها از عبارت «دموکرات اجتماعی» استفاده می‌کنند چون زیبا به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
🔴
فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ما است، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، یازده سپتامبر و حمله پرل هاربر می‌شود.
🔴
فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ما است. مردم وقتی این را می‌گویم لبخند می‌زنند، اما افراد باهوش خواهند گفت: «می‌دانی، احتمالاً حق با اوست.»
🔴
در واقع این معرفی کمونیسم به ایالات متحده آمریکا است. هرگز چیزی به این خطرناکی نبوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/130969" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130968">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681f6a849a.mp4?token=b-kYqIKw3ND0ZsKffHhWSZNXKCIfD0QBOJf2G9jtXQvthSLermQrGF5_K80XRWmniJw_dhl_U0Pe0h5WLhxZJau5igiIYAmbu0dIF6Lsa3qrHV7ptN3XlbdD0s7RjXEvU_c9-FUpQ-DFENJY-QpZt0qNjIOqKLsoEL1XIX1kxC9Psg_IZOv7PUQtQ4krNxj5GEwcxgpItdDMHp6nUqBd9tNdRQY6B6GVUyaR1x9oPzci4NDAyR9PWzFlp9X206APmZtftvJB31eVDwlWGbbRRSFnTBmVjFQ0ieqD9xhdc6qi-SiS3t02aezWiztfCrFDKuSXy_KcVUJC44ZeB1d5Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681f6a849a.mp4?token=b-kYqIKw3ND0ZsKffHhWSZNXKCIfD0QBOJf2G9jtXQvthSLermQrGF5_K80XRWmniJw_dhl_U0Pe0h5WLhxZJau5igiIYAmbu0dIF6Lsa3qrHV7ptN3XlbdD0s7RjXEvU_c9-FUpQ-DFENJY-QpZt0qNjIOqKLsoEL1XIX1kxC9Psg_IZOv7PUQtQ4krNxj5GEwcxgpItdDMHp6nUqBd9tNdRQY6B6GVUyaR1x9oPzci4NDAyR9PWzFlp9X206APmZtftvJB31eVDwlWGbbRRSFnTBmVjFQ0ieqD9xhdc6qi-SiS3t02aezWiztfCrFDKuSXy_KcVUJC44ZeB1d5Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: آنها مردم را به خاطر تعمیر ماشینشان دستگیر می‌کردند.
🔴
این حتی باورکردنی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130968" target="_blank">📅 23:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130967">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ : قیمت نفت خیلی کاهش پیدا کرده، ببینید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/130967" target="_blank">📅 23:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130966">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca333bc10.mp4?token=O-nTjJzJhNN42-4x11fTcQBHpBf161wvOxLvMfIRjUAJ3iIQcZBpHV5yC8ptQ5n5oVsi6DNurJQmo9Rq3goV1Jv0gMqM498B2r4bdcVz8lCgnIeXmo0rl2B3S6EP0dtsZmv3PDfylakbCHwKZA7Lnh_6yLTvnx7g3AccYZzyyMft9C7RJucsHjEYiZ60i3_LSAXES8RgTt8vjC7JFvd7ngaLfxIsHtNAQ2bBM_LUKNf9f37GEhdYN0ZiscHlfmJuNZsF_6y1rZyghyNxDx-r4webRR-_Hgt2gZiF35sxVBB4zSOiA5iLhxCd3bHPLvFcHXlllo3Y9ctbWynLvydA8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca333bc10.mp4?token=O-nTjJzJhNN42-4x11fTcQBHpBf161wvOxLvMfIRjUAJ3iIQcZBpHV5yC8ptQ5n5oVsi6DNurJQmo9Rq3goV1Jv0gMqM498B2r4bdcVz8lCgnIeXmo0rl2B3S6EP0dtsZmv3PDfylakbCHwKZA7Lnh_6yLTvnx7g3AccYZzyyMft9C7RJucsHjEYiZ60i3_LSAXES8RgTt8vjC7JFvd7ngaLfxIsHtNAQ2bBM_LUKNf9f37GEhdYN0ZiscHlfmJuNZsF_6y1rZyghyNxDx-r4webRR-_Hgt2gZiF35sxVBB4zSOiA5iLhxCd3bHPLvFcHXlllo3Y9ctbWynLvydA8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: نشست دوحه برگزار خواهد شد؛ شاید مهم باشد، شاید هم نباشد
🔴
خواهیم فهمید
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/130966" target="_blank">📅 23:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130965">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش ها از آغاز دور جدید حملات هوایی در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130965" target="_blank">📅 22:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130964">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7ybxJMdgmA6iB0ZOVNw6VD8jhDyc7AHrO5-rzzJx25Ym9AvRyta3ygIXCPZYWH9-XojnxW5lON7NXlVFcM-2VaNLynDjxJuEgbxBT5yoI-w2LUnoTQ4fa3mnPtJrNZgK7O-naOVRWL9B0Ukk0hpifbHWkrgIrsKPN1MiRaGFTQ-xG0jofaFeEl9x2V88rnxpn74MkC6Ckmcl3dEGt-IdzhLTQIFmGBp5mQ2sHPBYTzqbZd0ZQxRq0O2V9n3Tw6wcvVbvgMd_UOHOhm73n4hMkv1gucE7ZInj3SVfRFaZer5QmEJRT5AM7Y8xQvumgGir3q-fUu4fq9yoysAUvt_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاضل میبدی : جنگ‌طلبان اگر عاشق شهادتند، راهی بیروت یا غزه شوند/ رفراندوم بگذارید تا ببینید مردم چه می خواهند، مذاکره و صلح یا شعار مرگ و جنگ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/130964" target="_blank">📅 22:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130963">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8EQKejbyEgz38ZIl0AdPBA_iGe-C9IRYTNWncsc9Xybrh93vaEzdw9E_hdPDqyGrBl-3BL9nbucCmCHQ40rhwIRvbGa4xw16lL7ZfdyppGD_Q2X4VjSNlswvCOGpriaXuJe3birSPwV_03aYC1VD_XcQX9itV-QRUOPdUqnM0FbhJmOZuw0p6OeSeZvUmXU6r-5Z5laFBEmMZzMJPwt7F_pS9o_xE6aBLdK4Gx1qHrIT3fHG2PSy8JEazwlTPUKJHj1LqM6grgDdNLBEM7PrzpO7VREUStTwvgR1Lscni7BPOR_ut6ko3N413gtVtUxbWZXpGLedi_P0fHVzCfQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ادعای اینکه من با تهدید به استعفا موجب تغییر تصمیمات نهادهای عالی کشور شده باشم، صحت ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/130963" target="_blank">📅 22:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130962">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAWdy0sia1DrDchASvlIuXNay6SprrrgAleTgmFTshkujqKEPxH9sFOVScqMmksBLiZ-2Pn9vBkvl8lyzBNSfaYILaLKrHLIDibCDOjWptXa6uTiR7P99zLKVakugsv_3rshCa0J4ircngxkVc0B7KSPdfWn4YYpAu8LkFU-amjxnTkVW6hXK9HNv2snSQ-WhcvmsNPdHhUm3AHqTLfTsmgN36tjtLUpoh03q4IqXSrGLZeXoX6zQBUWhhidoNdjT9-NhqT97EZG0UNEKsxOK7t2NbTqef6hVntDhH2yTV5ZIX1q4TP5VbazOuhMfzKXHbK5Fc0HyUn_LZk9gdBROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
رضا شاه یه آدم بی دین، فاسد، عوضی بود و وقتی مرد کل ایران خوشحال شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/130962" target="_blank">📅 22:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130961">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات های زیر :
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/130961" target="_blank">📅 22:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130960">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/130960" target="_blank">📅 22:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130959">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
جیک سالیوان، مشاور سابق امنیت ملی آمریکا: کشورهای منطقه دنبال توافق اختصاصی با ایران بر سر تنگهٔ هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/130959" target="_blank">📅 22:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130958">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزارت امور خارجه ایران اعلام کرد: ما خواستار دریافت هزینه خدمات در تنگه هرمز هستیم و این موضوع را با سلطنت عمان مورد بحث و گفت‌وگو قرار داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130958" target="_blank">📅 22:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130957">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
حجت میرزایی، اقتصاددان: نمی‌گویم ۲۰ سال اما حداقل ۱۰ سال زمان می‌برد تا پس از لغو تحریم‌ها به دوره اقتصادی سیدمحمد خاتمی برگردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130957" target="_blank">📅 22:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130956">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=h9bOwFF06NYoOsbSDoAcAnzGnWoHVjuImwMeKBGmJg1yFAjEaECtaLQJ2ahXVsmIevhOOyWsZ9DEIUAPuhfWg1fW6THL-6MZ-_sFlLbWbE72q5oZIau2e3XTFZLYlnYMoWTvKU7OwxefT8HMbimPIDajnWV30ED3pbt7D7qq7XbNCrwquiQ_RZzLaT0_8CbRwdmjcbr1EBca5DXZ_tAT59hmTvlrRa_Kao-7tF274j1JR5zczztFb4whPFp81rCqC7WOplXdcHQeBtFnpUQkyYogeFs9THylnK3cMsTzq9V3_69yYRlF6WQ74ehT_N8BfbngIIxsG_yDcDpi6PhX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=h9bOwFF06NYoOsbSDoAcAnzGnWoHVjuImwMeKBGmJg1yFAjEaECtaLQJ2ahXVsmIevhOOyWsZ9DEIUAPuhfWg1fW6THL-6MZ-_sFlLbWbE72q5oZIau2e3XTFZLYlnYMoWTvKU7OwxefT8HMbimPIDajnWV30ED3pbt7D7qq7XbNCrwquiQ_RZzLaT0_8CbRwdmjcbr1EBca5DXZ_tAT59hmTvlrRa_Kao-7tF274j1JR5zczztFb4whPFp81rCqC7WOplXdcHQeBtFnpUQkyYogeFs9THylnK3cMsTzq9V3_69yYRlF6WQ74ehT_N8BfbngIIxsG_yDcDpi6PhX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس تلویزیون: جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130956" target="_blank">📅 21:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130955">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
آنتونیو گوترش، دبیرکل سازمان ملل متحد: تروریسم در حال تحول است — فناوری‌های نوظهور از جمله هوش مصنوعی، پلتفرم‌های دیجیتال و سلاح‌های بدون سرنشین را مورد سوءاستفاده قرار می‌دهد. هیچ کشوری نمی‌تواند به تنهایی به آن پاسخ دهد.
🔴
ما باید پیشگیری، همکاری و تعهد خود به حقوق بشر را تقویت کنیم تا جهانی امن‌تر بسازیم که در آن مردم بدون ترس زندگی کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130955" target="_blank">📅 21:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130954">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjGqpeSBcUv30ea0ddMSioScTpLix7Kmu1pSgq1HzZMp13tlC6ebaM0SZplFu-ZUM0sgSZkz7vkwQ36iokGa6yU5R68cd4Jl5VEKZz6btto6VnVk3nb2sHz4e-ZQZluigzUWtOhYlPd5n7Ttf1_uZtN-c1ncToU9iwsAwkpbpNEl6T6--cZ5vraOMFhzPTHERb_Pt__fkxFNTLdRfZSt3vig2Krf3_yF7KkNodZ0xRr2Doq_E5m4pwlwqeVQhvwTRFzFbaiEp_WSX-w3NHQbeqqKmrnZzSiLfXKc0aIr09tjwPZcSxbcQuKVl90ko3j1IYo6k477rLRE9tKaAmvGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: آمریکا اگه توافق میخواد باید ترامپ رو تحویل ما بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130954" target="_blank">📅 21:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130953">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=r8yzPsJbVYzdSYvbaoLnO3v64m41y3lGOvjM97-8eQW9-nnatsPa7ox7_auCOt3V8HQf_jGw2zgazMyBwZFv-dEnh1QEVTx5fF1HMkypQz5q2F7G2viwAHKcsY-mdY3zA3nvi6ewiPtH37ylVcMLZwHpx9mxeeOF8ESA-iQNinBbg79iE-gkGc9A-Mj-M5PogghCCRm-3Uw8e1pz8vIIFW49yqJPpfXQUwEh8MpBsBlImoAZv1CWDCSP3_u33ZOIilo3JP6sQPQkZ2ISvAOG8x-BPGURAabqAhwDhOW4OvOUTzYPLmZGvKtUFnVeIREB5frEdFPZdk9jVjQ7OO3rDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=r8yzPsJbVYzdSYvbaoLnO3v64m41y3lGOvjM97-8eQW9-nnatsPa7ox7_auCOt3V8HQf_jGw2zgazMyBwZFv-dEnh1QEVTx5fF1HMkypQz5q2F7G2viwAHKcsY-mdY3zA3nvi6ewiPtH37ylVcMLZwHpx9mxeeOF8ESA-iQNinBbg79iE-gkGc9A-Mj-M5PogghCCRm-3Uw8e1pz8vIIFW49yqJPpfXQUwEh8MpBsBlImoAZv1CWDCSP3_u33ZOIilo3JP6sQPQkZ2ISvAOG8x-BPGURAabqAhwDhOW4OvOUTzYPLmZGvKtUFnVeIREB5frEdFPZdk9jVjQ7OO3rDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا مذاکرات هسته‌ای با آمریکا آغاز شده؟!
آجورلو، عضو رسانه‌ای تیم مذاکره‌کننده:
تا الان هیچ مذاکرۀ هسته‌ای با آمریکا انجام نشده و تا عملی‌شدن شروط ایران هم مذاکره‌ای دربارۀ موضوعات هسته‌ای انجام نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130953" target="_blank">📅 21:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130951">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس:
محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه،
در یک سانحه رانندگی ساعاتی پیش درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130951" target="_blank">📅 21:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130950" target="_blank">📅 21:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130949">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: هنوز وارد مرحلۀ مذاکره برای توافق نهایی نشده‌ایم
🔴
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آن‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130949" target="_blank">📅 20:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130948">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=NFxzZFgARXStIHcb5SXBIPVgNNehQ0DWA2JueSJqqXlUI8N4osKHdnru8llNYvMVXytroMI7gkE_aAao-iKv29sclo-kp8ziGe4ihUDLXDFb6NTl2jbhj6HLjg94c6C8t841u6JkJC0H8VSAR-wLgt0cJYWuVdcWWPBrfmfCWq8y5p-wVeT1TcMmc_blLgfSRFtB4JLClG1veMxlWV0ljFnnNv1H39reIaahrUfra5GFIDgQeLphuNqij6BPr0_wcATZRerQJj7lQcMXTP9S8mnWzOMsel99GvTMTkyCLY09-njjqJw7wV_zDpBzhgpAq5Bxi2VmuXZE1lMJ1-MNOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=NFxzZFgARXStIHcb5SXBIPVgNNehQ0DWA2JueSJqqXlUI8N4osKHdnru8llNYvMVXytroMI7gkE_aAao-iKv29sclo-kp8ziGe4ihUDLXDFb6NTl2jbhj6HLjg94c6C8t841u6JkJC0H8VSAR-wLgt0cJYWuVdcWWPBrfmfCWq8y5p-wVeT1TcMmc_blLgfSRFtB4JLClG1veMxlWV0ljFnnNv1H39reIaahrUfra5GFIDgQeLphuNqij6BPr0_wcATZRerQJj7lQcMXTP9S8mnWzOMsel99GvTMTkyCLY09-njjqJw7wV_zDpBzhgpAq5Bxi2VmuXZE1lMJ1-MNOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات حق استاد محمود سریع‌القلم، مشاور سابق روحانی:دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
🔴
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
🔴
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130948" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130947">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJTVeSfDzEIThxlBMJ1V_u78JeI8VzJojRubYo6PFX_7-KokiDRf1SOdXU1OtEbACqPGpQKwYPpQb4bXFQXkDOKsezNJaY8UjGK4xGbWtlOdIFnoxqqa0MXu5NIRA2kssbKCZci0rHtqL1V0lJ7ol9DJJDUyLFpAG4uNuu3tGirWtzGr1M-ikf1OxPEcJCsgRkl1R3_R2curc6aXqim-p9CvlNwV94nXoH7dJp_3yWpEpXNxVBvO_jn7snKoRNdcXWVrdUE9ekHueA0DO3QVV9r7nzfyClWWLGNWY6AUKog_kaBaC0PDKwzVX-cbuLH98mTEpT2WZ9WmWxo0UWUs_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ژاپن موشک هایپرسونیک «تایپ ۲۵» را برای حملات دوربرد عملیاتی کرد
🔴
نیروهای دفاع زمینی ژاپن نخستین یگان مجهز به موشک هایپرسونیک «تایپ ۲۵» (HVGP) را عملیاتی کرده‌اند؛ سامانه‌ای که با هدف تقویت توان بازدارندگی و اجرای حملات دوربرد علیه اهداف دریایی و زمینی توسعه یافته است.
🔴
این موشک از فناوری Boost-Glide بهره می‌برد؛ به این معنا که ابتدا توسط یک بوستر راکتی به ارتفاع بالا و سرعت بسیار زیاد می‌رسد، سپس سرجنگی گلایدکننده آن با سرعت هایپرسونیک و در مسیر مانورپذیر به سمت هدف حرکت می‌کند؛ قابلیتی که رهگیری آن را برای سامانه‌های پدافندی دشوارتر می‌کند.
🔴
«تایپ ۲۵» به سامانه هدایت ترکیبی، ناوبری اینرسی و ماهواره‌ای مجهز است و برای هدف قرار دادن شناورهای سطحی و اهداف زمینی با دقت بالا طراحی شده است. ژاپن همچنین در حال توسعه نسخه‌های پیشرفته‌تر این موشک با بردی بین ۲ تا ۳ هزار کیلومتر و سرجنگی ارتقایافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130947" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130946">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd900cb7d1.mp4?token=Pooik50Y6iBXae71om9vWk4lpQw0-NRMK-4WplUf0KjCIMlpsKK69lIqMNspzm1AEhSOI598lFoM7g-Vq0VQKWN8hlKc9wMJdC0wc1-0pvYf8sBMne3L8eNMAxRFbmn7jJJ3yJV6tqYpUYxouDrkeXtmeATgz6-gaetr3XpihjWhe-Bk0GHVqWzogJVDlCm-PZA0NHftX8qfJlJ_BoKxOzpgc_x3uIeBFSXXrisx-t6FbiHkPzPe_AYNqcWJDxYwnP40oLNofw8lPxAk6TyX368a7lO34iS6N1nekO027ReWvWOMmJukYdCfYBvBcfM3pqJYbSgpZUS9HDjXqYNGMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd900cb7d1.mp4?token=Pooik50Y6iBXae71om9vWk4lpQw0-NRMK-4WplUf0KjCIMlpsKK69lIqMNspzm1AEhSOI598lFoM7g-Vq0VQKWN8hlKc9wMJdC0wc1-0pvYf8sBMne3L8eNMAxRFbmn7jJJ3yJV6tqYpUYxouDrkeXtmeATgz6-gaetr3XpihjWhe-Bk0GHVqWzogJVDlCm-PZA0NHftX8qfJlJ_BoKxOzpgc_x3uIeBFSXXrisx-t6FbiHkPzPe_AYNqcWJDxYwnP40oLNofw8lPxAk6TyX368a7lO34iS6N1nekO027ReWvWOMmJukYdCfYBvBcfM3pqJYbSgpZUS9HDjXqYNGMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: آزادی گروگان‌ها بدون پذیرش شروط حماس و خروج از غزه ممکن شد. فشار نظامی، فشار دیپلماتیک و حمایت آمریکا عامل این نتیجه بوده و اگر اسرائیل با خواسته‌های حماس موافقت می‌کرد، رهبران این گروه و دیگر گروه‌های هم‌پیمان همچنان در قدرت باقی می‌ماندند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130946" target="_blank">📅 20:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pANbjAFKV6dUmntHnNoMTXL85loK3ZNLddiFmM-ipUWDaxptRTu8bMloznRL-KpCECSDGCToDuHLRiUIJtbp6VhPnno3D_rMhsGaVemSQKXl9G7kat-iQlLZjWPKjzpdl4sXQt8zsYRl9d_cb1mEoWYQ4o4g3jq4k2M90PNREi_PyW8VVwAvIj66_H12dn3F5-Elk5Kx4Chs1b6il7NNrZx5IX2Wt6DcqF8oh2uc0GZNvJ7whs-8WMo1K3OmOuYnBvVPVSGlulpDotX7lcaiOdxuQgmwsYtbwuM2ts6sE6R0tMLxSB_dxekNOSruv6dqxFGuS43A3sigWxB8e3NaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: ماکرون گفته در مین زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری میکند. طبق یادداشت تفاهم اسلام آباد، مین زدایی صرفا توسط ایران انجام میشود و نه هیچ کشور دیگری، اصولا اجازه چنین کاری را هم نمیدهیم.
🔴
شرایط حساس و پیچیده است. توصیه اکید میکنیم فرانسه آنرا با تحریکاتش پیچیده تر نکند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130945" target="_blank">📅 20:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ایران اعلام کرد که برخلاف ادعاهای مقام‌های آمریکایی، هیچ برنامه‌ای برای برگزاری مذاکرات مستقیم با ایالات متحده در این هفته وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130944" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130943">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی دولت عراق اعلام کرد:
دولت به کلیه گروه‌های مسلح در این کشور تا ۳۰ سپتامبر سال جاری،‌ هشتم مهرماه آینده، فرصت داده تا سلاح‌های خود را تحویل دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130943" target="_blank">📅 20:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130942">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsE9nGwaQ8V6hrFFQ9TOH_mmbt-zhfwa02xym-y5MagdRZdJQ9M5E7RtHaREe3MLAODXDMgYT8xYRhzMtn8SnqmV4i6pw77YEmh2JQGTpxCGsljbIzDjae4yP3E_uZqkVQy7AXZSmn8KwY98k-kDc3BmtJ5vkl8USdg3jOCFcIOqEyrvOVsnBvVDQRDg6z1r7W1fuMdSHVFHMV0y0Hp6mxIqeRvfgm4UsyjnGABN7qfNMVWE0A9FJkGlBt3GUcoIB56_Fuphkd9-i208eN3zhSlfwkrsFByVJ6XsORiQdCT2mBfFxlftK_h_5n82UlTWSrrt2u0Gf0fqZ31bdsCp9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عالی ایالات متحده روز دوشنبه با صدور حکمی، اخراج روسای نهادهای مستقل توسط «دونالد ترامپ» رئیس‌جمهور آمریکا را آسان‌تر کرد؛ تصمیمی که توازن قدرت را از کنگره به سوی ترامپ تغییر می‌دهد و می‌تواند نحوه فعالیت بیش از دوازده نهاد فدرال را بازتعریف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130942" target="_blank">📅 20:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130941">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8041c64fe8.mp4?token=tThsbdsGid4qgVcQIyCAxmNPtwLUb-eul-5uI0pv-Lm5OdLRZZ5ryiH5U5idVext9sVkh6MGa-M4iByCH4mGaDm_V8jiLLmOHCjwe1sXLWr4IqQJ-lCnVIhzMVpwvvjDTH8xO8mXLq3onC4B7gsUB5A-zSiER3arbEYoViBInQrchCaTWv2mhGjO_TWt7SrGgt1vv__FQ4w5v9W3WnIc0vjcfGea59FPgd7DLhqVxTcNSLml-NpMzHsFZtQMC9-6ik_d1VuF17FW49dqa2lH5dtAwkpUN5sKuS-GIRN7_4ldpWrK4N60T3jtf3X3HgGzhTIdESayjzU4Fm4OJ1Vrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8041c64fe8.mp4?token=tThsbdsGid4qgVcQIyCAxmNPtwLUb-eul-5uI0pv-Lm5OdLRZZ5ryiH5U5idVext9sVkh6MGa-M4iByCH4mGaDm_V8jiLLmOHCjwe1sXLWr4IqQJ-lCnVIhzMVpwvvjDTH8xO8mXLq3onC4B7gsUB5A-zSiER3arbEYoViBInQrchCaTWv2mhGjO_TWt7SrGgt1vv__FQ4w5v9W3WnIc0vjcfGea59FPgd7DLhqVxTcNSLml-NpMzHsFZtQMC9-6ik_d1VuF17FW49dqa2lH5dtAwkpUN5sKuS-GIRN7_4ldpWrK4N60T3jtf3X3HgGzhTIdESayjzU4Fm4OJ1Vrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقبال مکرون (رئیس جمهوری فرانسه) از سلطان عمان در کاخ الیزه پاریس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130941" target="_blank">📅 20:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130940">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3dcc1c10.mp4?token=HGBKCRxJ94blGuZ8S-DVDvbnujiWlKrPM8CgkwNPkGEObiumFhmNJukKf6Gb1wwafHAQBajQbS9SzXMIWPM8pP2x-95Z8_sEky_LjvOw_caAVo5COzTQFoL55F3MDIb7IqOcJTyKY0wVZogaGkpYPqEKCXfMjqITLTs5fghOL2aSH65D7YsJp53_qwtXYY_HRPWZf7sZc_7lG57yfbjQoUsam6BH9lPn9rkSq3tzy97UF1IfTq04bLJvC_VZOYrE8GF0mLprF-qmcsT34Y9yC1rCDFROtQUST5_zqEW11bOE2hIBXb_3ZlcJf4aAIhAn_cXo_ECEpH2USmez3wirkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3dcc1c10.mp4?token=HGBKCRxJ94blGuZ8S-DVDvbnujiWlKrPM8CgkwNPkGEObiumFhmNJukKf6Gb1wwafHAQBajQbS9SzXMIWPM8pP2x-95Z8_sEky_LjvOw_caAVo5COzTQFoL55F3MDIb7IqOcJTyKY0wVZogaGkpYPqEKCXfMjqITLTs5fghOL2aSH65D7YsJp53_qwtXYY_HRPWZf7sZc_7lG57yfbjQoUsam6BH9lPn9rkSq3tzy97UF1IfTq04bLJvC_VZOYrE8GF0mLprF-qmcsT34Y9yC1rCDFROtQUST5_zqEW11bOE2hIBXb_3ZlcJf4aAIhAn_cXo_ECEpH2USmez3wirkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروژه تانک ساخته‌شده توسط دانشجویان طالب دانشکده مهندسی در افغانستان: نصب دوربین مداربسته روی تانک کنترلی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130940" target="_blank">📅 20:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130939">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نیویورک پست، به نقل از یک مقام آمریکایی: ما به ایران روشن کرده‌ایم که تا زمانی که در موضوع هسته‌ای پیشرفتی حاصل نشود، دارایی‌های مسدود شده‌اش را آزاد نخواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130939" target="_blank">📅 20:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130938">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: اگر ایران به اسرائیل حمله کند یا ترامپ مذاکرات را بی نتیجه قلمداد کند، جنگ با ایران دوباره شعله ور خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130938" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130937">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
والتز، نماینده آمریکا تو سازمان ملل :
۱۱۵ کشتی که حامل ۲۵۰۰ دریانورد هستن از تنگه هرمز خارج شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130937" target="_blank">📅 20:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130936">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7J1fT_nAhnewIHgM9J8Jpsca-_XRpmJGY4M0HRQ3NjY2DwlPt5P4hQLgjNVQL9oBoJjgk4rNBHMBaoTKHa575TLLpqJPI3PV_9sVfOECx5MqWlgFigHbaxgPplW7oTaJHN3LvI4g6Aj_9mlIz0V6WOyNgRLFeL9Z4-nWXmfZ6qgr8CNQuQdcH1w0etba-Dx8TEwbOuv1RXwcpS2du2uXJBKzuN8zgR4S4JsM11Kme5O6JWKxO38QkqdeqoiaiSQ2sw-insnWG259WB25N2hrc50Dw1QFZ8bgx_QSDkOF5LMjzoApPWbyZfTn58k3WWCjsarvjHdLqnwikvRiaGX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
دادخواست کوک، که مربوط به صلاحیت او برای نشستن در هیئت مدیره فدرال رزرو بود، به طور صرفاً رویه‌ای توسط دیوان عالی بازگردانده شد، ما فوراً اقدام مناسب را انجام خواهیم داد تا اطمینان حاصل کنیم که کسی که مرتکب تخلف شده است، تصمیمات حیاتی مربوط به رفاه ایالات متحده آمریکا را اتخاذ نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130936" target="_blank">📅 20:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130935">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
پزشکیان: برخی تحلیل‌های صدا و سیما با سیاست دولت منطبق نیست و انتظارات بیجا ایجاد می‌کند و منجر به نارضایتی مردم می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130935" target="_blank">📅 20:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130934">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سفارت ایران در قطر: مقدمات مذاکرات با آمریکا در دوحه هنوز آغاز نشده است
🔴
ما تاکنون هیچ اطلاعات رسمی در این مورد دریافت نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130934" target="_blank">📅 19:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130933">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6iP1hIHIgKEilW-rPUT2-lsLFgRKtSB1LrmHsQmJfi5xJ6Us87xbq4tPWswehSVr_kwjrm0Zs3g5P7E7s1t8-pEqXjvjti_gynLn8egn39Nb3rEZrvxK4H7YVOFOfIKx-6e1HLb7EoxknQhEfkvfpBcHF17-alDYkLoVIliwn9SQxAwTCA9gqglr3ijdynu--f6pjLTNTFpmXGOV9Jhjh8fI_9yrFsLn5kN81c8_ce2Oz-3XcmjvFqbvcV0Zg1OldtAxQeyCaLT1hXCHIBezxHrd0cDc0RqHOSLsnumlWSA2umlgxJ_4yWjTixZ03pJTQekkPpOXGgRR2k8T_ie0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره امتناع دیوان عالی از بررسی درخواست تجدیدنظر او در پرونده افترا علیه ای. جین کارول:
به طور شگفت‌آوری، دیوان عالی از «بررسی» پرونده جعلی که توسط زنی که هرگز او را ملاقات نکرده‌ام علیه من مطرح شده بود، خودداری کرد (عکس چند دهه پیش از یک سلبریتی، ایستاده کنار همسرش، حساب نمی‌شود!).
🔴
من به مبارزه علیه این پرونده تسلیحاتی و حقوقی علیه خودم، از جمله ادعای مضحک افترا، با تمام قدرت و توانم ادامه خواهم داد.
🔴
این پرونده در واقع علیه ایالات متحده آمریکا و همه ارزش‌های آن است و هرگز نباید اجازه داده شود برای رئیس‌جمهور یا نامزد دیگری اتفاق بیفتد!
🔴
ایالت نیویورک قانونی را برای مدت کوتاهی، که به چند دهه پیش بازمی‌گردد، ایجاد کرد تا به ناحق مرا «گیر بیندازد». این قانون به طور خاص طراحی شده بود و این بی‌عدالتی نباید باقی بماند! از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130933" target="_blank">📅 19:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130932">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cr76_XP1uGtUgjXOOAoKO9CFVtOSZ3tEiF17-s_tX-5qlC97cS0BzQqiMAWSJZE-3LE7EPHGO5kwY7T4y8LuWZMbFuNOx7tpHcYxQz3IGbOcHEELI7-QAPfR8EfjMAE9xdfNVMvYA8-IjSL2ETyPz9v8vYNcyREQr6duQ5RENisMxqJRaN_lQTfr-1gQvODEcSjc4IRU5ddE0X7rItpJke3rUI9RnvXMlgf6fA9UrtSZF2EN5WcnNsgkpVEfZgL6iB8Vup8RR1grB2wRKsoBSTU4gO93thXiYHMwkb94rhmFOzcwuNoGGEwM2N-5apu2E_5FKoTyspupPagva1n0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
با توجه به خسارت عظیمی که امروز در دیوان عالی کشور در مورد حقوق رأی‌دهندگان وارد شد و این واقعیت که رأی‌های «مردم» اجازه دارند مدت‌ها پس از پایان انتخابات شمرده شوند، تصویب قانون نجات آمریکا از همیشه مهم‌تر است، که عبارت است از:
🔴
1. همه رأی‌دهندگان باید کارت شناسایی عکس‌دار ارائه دهند (شناسایی!).
🔴
2. همه رأی‌دهندگان باید مدرک شهروندی ارائه دهند.
🔴
3. هیچ رأی پستی پذیرفته نمی‌شود (به جز در موارد بیماری، ناتوانی، اعزام نظامی یا سفر!).
🔴
هیچ بهانه‌ای برای یک سیاستمدار یا غیر آن برای مخالفت با سه الزام فوق وجود ندارد. تنها یک دلیل برای مخالفت وجود دارد — تقلب! مجلس نمایندگان این قانون حیاتی را سه بار تصویب کرده است. به نظر می‌رسد سنای ایالات متحده قادر به انجام این کار نیست. در زمانی که یک جنبش کمونیستی قدرتمند در کشور ما در جریان است، که خطرناک‌تر از جنگ جهانی اول، جنگ جهانی دوم، پرل هاربر یا یازدهم سپتامبر است، همه دموکرات‌ها و پنج سناتور جمهوری‌خواه ما، لیزا مورکوفسکی، سوزان کالینز، تام تیلیس، بیل کسیدی و میچ مک‌کانل باید به نجات کشور ما رأی دهند. دیگر هیچ بهانه‌ای پذیرفتنی نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130932" target="_blank">📅 19:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130931">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر خارجه آمریکا و فرستاده کاخ سفید در منطقه قرار است کنگره را در جریان تفاهم‌نامه میان واشنگتن و تهران قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/130931" target="_blank">📅 19:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130928">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROtpKj-ajTKvd9ay4jepeMEeSNe-R0_KBmZDEQuegifBknGIIMJp4NcxKO0SGQIQ5ko6dJLJ3Aw95gNEFt_jDfx_S_72IiCBB-jFeiwMFi6iUnLiLYDsKpXBl1ktmKig2rTUU0pgqPTpmZgBrLazwzLd_pshG462pVIZaSDC2Au0l3EKPWQnKgEfvxZm0Gqeteo4Dlj3PAfbO72qM9BAbtGG-18lpglgPm-KEOqrj1PobCYn3vw854a2XHPwbqEgalnGKqR8DnNNn8iiNSMmTK8ia2nZZ9osWlDgun16fYcJGuFAvkU9KiIR5f8oNaDM1YINkhcvmvf1SPaAfxT06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_umhogsfXPlTFR463AKZCCJnUGBYH_WPHXtjWuINjJxQOycBGJtClZ7WEhgVnLE9d0bJwKSPkLBM9fIVxq7tNHFaCyqdu6YUEC7l_kkj0CoV7hj2MqjUqqbfv_OTORw8rZXfN8uATepW_ae0jb52DZS0uiA8MdhHxGaBs0I067sjw5e2pR8-0SpvU0Nsg9HRv6JygGh9Q24JqhlPehcjmKDx_dRoqFCJjZCSXKzHXiX3L9uuqxtlUuIOymEQ2eBMDtPGG9WBLbcHpBMAbOuD04pOZ_QmaQme9WZo0ZeFFpd-7STSCgAj2E7INB0s-JIPXzeHNoH4Dy7OJxPS5clAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dO4ZIpwUcyG-WCtNIH8f5USJYdH2sXpEgTr5VDssK-j65_h1aTYJQCvbzZoVMz8VDs4UcyYB5rJULn3Or6L5L0DO-ftD_fBx6oqZOyxTHIHyhS615xXy2Unef24GA3dgj1-ogrFufPwzXR3Vu4XlRqhxL8f_gkCQan2xg8lmTmnYlLzGFhRMSO2eNTA3kbfO2kth0mg6N0U1c23R5w2e_FN9Ci2WVQelK8c1-vTIJaBIliQITf1HDSRANFDwBwXHfnOspBFI7eKxEVEjd_s2AYc81KB5_hS01tGp3wLhiIpARrsX7YfTB-3mnJN_lRqFsMhrC263U4FbeNXsLnkzjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از اجتماع تعدادی از قبایل یمنی در صنعا، در پاسخ به فراخوان عبدالملک بدرالدین الحوثی برای بسیج عمومی با هدف پایان دادن به محاصره یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130928" target="_blank">📅 19:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_4xnI3H7rkDAYB_XQ3b5orOTyIlpf8P6M8L0aYX2b4FYWLenN9TmNE3KP23-68sV-bJk1SugK4eFjHHOTTxeYu8r57Vo_5My-Bss-LgCI2m0yJtx3U1M_28fY7MKoQI4V6WAb_lVw_cImXGzia0OxyZnC9RRiTECPzPmIKRV77ALA0bWXH_3NSdgdAZRX42DLbT0CQEx2khgeAyVCY8tfcBMahV8jABDRyPCbVworq6cMw4O3_58L2y9Wjhfhh7GQh_eB-wmr9bHjNUahnlsvZz-8m2IHonrWDQlZqC6kv2-sDHCQoKrpQUVSdgU01U0YxMjNJ03pCQLFos6tg_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داغ‌ترین شهرهای جهان در ۲۴ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130927" target="_blank">📅 19:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130924">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاطلاع‌رسانی | لگ‌لس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqePbPTSA0-rzkvKzeJ6hIVREo_8TMGhr-QQWfyWnwWOk9U3l6mBj7GoMcVYDo-5lu9ydr0jbAezzMXyIpHj8kvquaqueawmzOgU6Gttnntj7m9qeD8JSwQXUgiqOKW6_VCA4tZjjUwFmErmE8PqgI69XuxY1pZ0OTDZVdDm5nfmzp13WFY3QBw7IFBLXbj5fU29WV09x5Um5_WtQYRVy0ozFs7dFQWD3KhjLT1C2gK_nmlM_mMCkYIfzAPRvtTr4JsuPeF6J6hn4_8vZ0YJuw1vDCARbXxwUbFEw-D-b0V3M4b2crl7GZVlQrnjQ0dVu3XPICDdWGAP2ZYp9ezmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
لگ‌لس٬ سرویس هوشمند
کاهش پینگ
مناسب برای پیسی و موبایل
کاهش پینگ و جیتر روی همه بازی‌های موبایل و پیسی
با ۳ سرور قدرتمند اروپا٬آلمان و خلیج فارس
مخصوص بازی‌های آنلاین
پروتوکل قدرتمند وایرگارد٬ بدون قطعی و تضمینی
برای دریافت تست رایگان کلیک کنید
👇
@LagLessBot
@LagLessBot
@LagLessBot
@LagLessBot</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130924" target="_blank">📅 19:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130923">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqFNZvL4XWkJiti0rmJjK-wUOhyDetPdb1wnhVgyvMIgyAHq196OzxxOf-cM9oDB97ZbWCnvdU5XUjKzTxzZIVkw0UzkyhrrWv2yLYpbOnPLlTKtjaVTMEDeQkDvENyqe9ev1C4mdBfynvN_N2eGtKMEFd-1OGNQayf0ombXW0JgAqT1zzvIt6tG_uIj8W8jVreR6CjT5OftGzVEsD9JcG4xL6cmDTowpHP0-Dq75Q0BzQwbjOtuOWj8FlSjnENr_ZgDfvoPOS1rbE5QRhiXg9p1nZtI2nNhqZoi2H79nflHJAR1jwxavhx8jZfde4i0VdonsTrJxu_HcIjLShX-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع خبری از وقوع یک انفجار در اطراف منطقه دیر میماس در جنوب لبنان خبر دادند.
🔴
تاکنون جزئیات بیشتری درباره خسارات یا اهداف این انفجار منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130923" target="_blank">📅 19:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130922">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سنتکام:
بیش از ۵۰ هزار نیروی آمریکایی در حال حاضر در خاورمیانه و در حالت آماده باش هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130922" target="_blank">📅 19:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130921">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlAvpDMShpN2mk4DmLlRT3UCaVOVKFrg4ak0230v7p_kjtfyAqcroF0NgOE11NYchPnvtipu9vJ1l3smo0MtNyny6p6KMCtDLOsHm2TJxkKLNjGTPDvFsyRTD6Um9HbqK6sF8zCoun7nXOTuLeodJPPdskXl8ZbLth4eQ0DkZddTgw1q95r1NCeEs4kQbZ97SyKZkvdFO0ZMF1ziyDJxDWpGCq0tMnJ5-tKcf2Af5hewOX1wUSMv6ppmaorFpCWh6VlDtqhfmHPYCl5Vm4RqulNlKAzGrLQ2QpX3YavLE-WBlyK35iXWsK2Cau-WteE9IPd_Czj9KvqU521LkBeLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خراتیان،کارشناس حکومتی: ساز و کار انحلال سپاه در برخی محافل درون نظام مطرح شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130921" target="_blank">📅 19:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130920">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
یک مقام کاخ سفید: روبیو و ویتکاف تلفنی کنگره را از توافق پایان جنگ با ایران مطلع خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130920" target="_blank">📅 18:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130919">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سیمایی وزیر علوم : نام رهبر انقلاب آیت الله خامنه ای ، در کنار کوروش کبیر برای تاریخ ایران خواهد درخشید،چون مثل کوروش کبیر تسلیم نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130919" target="_blank">📅 18:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130918">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کاتز، وزیر جنگ اسرائیل: ما چندین هدف آماده در داخل ایران داریم اما اکنون اقدامی نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130918" target="_blank">📅 18:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130917">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxK8hbNsMwfLUCQVQaq_e-baHlPaOOO3nqeFHAHxK4r23QN0VmBrahCQKThENCGVe-l_21y8-ZAecn_JJxZdZR3HSpKRhevrQs83m6F_yV8AGD_iTvdq5D8mkRrWlSxR_uYNIs16gOeeayYvrkCbxQlAMPXIcrYwekUdJHgQ2kBGWOgYV2HJKaNFVShUyUEoBNvDu2HAV5uCzzdWX_iwSpJY1j6TyEFjJdhBvtR8rNmx9OYuaJWWkcBeKkhsjHrzVgk9mH9D-b977MNe3VBw9nM6Rvf229i59dNUe1ApMwCS23HfiEL5lK1AwUTpUA_4yd_NX5aQfMoY5nmpHq75EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه قطر: حملات اسرائیل به لبنان قابل قبول نیست/ بندهای توافق اسلام آباد باید اجرایی شود/ ایران همسایه ماست و می خواهیم شکوفا باشد
🔴
"شیخ محمد بن عبدالرحمن آل ثانی"، وزیر امور خارجه قطر در گفتگویی با شبکه الجزیره ضمن انتقاد شدید از رفتارهای جنگ طلبانه اسرائیل علیه منطقه به ویژه لبنان، خواستار اجرایی شدن بندهای یادداشت تفاهم اسلام آباد بین ایران و آمریکا و صلح و ثبات در منطقه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130917" target="_blank">📅 18:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130916">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bxra78p51o-s60d5Fsc8_ApFi0x_8Vq1C_dSQcfEl1LJVvJejW8PtintjkNtu5Hk8weeuln2-Rhy8O_hhVhL_Z0onUwGXccGp4mM6tJOH_0JUwYAetejoV2Waf78cDlSjc0atR3M7_Oex6uISxuwzoJrDQQHoJW2bvJcIR9LMJVYZIYjg-aGixK9F17MKPMPfjoGRK5BmL7gatAfMMXr8t-HvzUcKYTb3v4H-qeFBn3Rgti5Zhq2y1bLMDippCu9FmIkahyB4JBO0Bmfc5YnVbCHaa3QZgvosHgcMigTHJfp9fhw-az_72H_Ej24IJhS45D-hAtOwGOSEasPt6TF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماسه‌سازی تاج بعد از صعود نکردن در جام ۴۸ تیمی:
🔴
نه تنها در هیچ مسابقه‌ای شکست نخوردیم بلکه به میزبان جام جهانی هم باخت ندادیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130916" target="_blank">📅 18:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130915">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
طبق برخی اخبار گویا به هر بازیکن تیم ملی فوتبال قراره ۲۰میلیارد پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130915" target="_blank">📅 18:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130914">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeP4f3Gzf5xmVDemhA162y9SnrgCuupdixQG87ixt1Kcmfh9W2GUYbJ4QrkhQ6RPvZfOU-uxZC24u6d5-rzD7dWNXfI6CamumLEJg0DhtUoXvtQ2r6ZiaR2W6gMCLYYzc2ta6n8yNUpjm0jFLAlSHLHfV9xYnSDoXs-7YqkN9XushIPDQMbzWNjSYEnl7wlEqL197gPaeQrKCswLWx9ao103-izVK8r2aoYrqjvLjomVPwvvB6FD1eOh0eBeBMVOproHSpkxPfEhzdWlIMw7ghSnsyBfIOeV6dulxI0GcbsSuiHi1VbYbiNCQMJ7wyZeGxeMJIj1MsVz5IBoQXJRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از 1500 سال تاریخ درحال تکرار شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130914" target="_blank">📅 18:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130913">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB4sF7yFDP4O6H308mei4v9iQMJiCgTYrftcU7J6MykiVP7HnKee-9xWYXYrHTVceYRIpivBWXjObdiTraGzdGU_S0zMqz2a9-QD_KQ_SEntctUqm5mYmtYBdcbV2bowjS0LUQLP3gN3B0sXZ9CvT1i7HjZ_LaO940lOatP9lChzxNK7uzvp74_-v0Up8uBcw0GAjEXzjHgpzwxYVNxLmjKC3rgRSaddF7d4zArp-0FpdDJZH_NCQ0Y4GI7ob7KGENGQqc5OwZQxj63ntyRn7TiJaEoT0gPK9M0JvW6i3_jR2n0te1GrdQDmDJdZtBuchTXb1s2gS6VKofQ7H1zEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار فرمانده سنتکام با رئیس‌جمهور لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130913" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26cc6d01b.mp4?token=fHlI_iGKBY6JkGHqtWFbWD4HLmAZH1QH8G-JP7g6m6zGC_658Ko0rhGWW3iVD1fYb0s0nhye8aNWjYTQ389GGuYpypLgzIBBFh39yIkrYR_SxNEay1KnGvK4HhcQLv3oZ7ZPZj7n9Mlm2ZRjxS2xhlEWK-WhO-8R-mo2V2QRiXCQq6SVZPslUlC2fTHfb_FN4JsDEtjfBeIPgQzLjclq-OHEtdSLIxVxqODyRUOO514We_y1TCXdlKuQaCBwv1NJVfHzxIyQ6l_yCPeD239JLxm8PZ_VVB8kc3DCo8FfjqpGKjeSNCPW6kGqlOkNsqeN-twdISKdBarjG2nSc5eYCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26cc6d01b.mp4?token=fHlI_iGKBY6JkGHqtWFbWD4HLmAZH1QH8G-JP7g6m6zGC_658Ko0rhGWW3iVD1fYb0s0nhye8aNWjYTQ389GGuYpypLgzIBBFh39yIkrYR_SxNEay1KnGvK4HhcQLv3oZ7ZPZj7n9Mlm2ZRjxS2xhlEWK-WhO-8R-mo2V2QRiXCQq6SVZPslUlC2fTHfb_FN4JsDEtjfBeIPgQzLjclq-OHEtdSLIxVxqODyRUOO514We_y1TCXdlKuQaCBwv1NJVfHzxIyQ6l_yCPeD239JLxm8PZ_VVB8kc3DCo8FfjqpGKjeSNCPW6kGqlOkNsqeN-twdISKdBarjG2nSc5eYCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله خوارج با شعار مرگ بر سازشگر به عراقچی در کربلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130912" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130911">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دولت عراق تا پایان شهریور به مقاومت عراق مهلت داده است تا سلاح خود را تحویل دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130911" target="_blank">📅 17:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130910">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
غریب‌آبادی، ادعای ترامپ درباره جلسات فنی برنامه‌ریزی‌شده آمریکا در این هفته را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130910" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130906">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2NeCWbeWerSiUtEYKjKYyxukoJDIPaHQBIQdzu9nYdSeeDhBwBlWFXN6N7AgbxIiZzVEtqsOnUBuaig7jlIEq0ZFZdeVzMWIzDO7iybP8zgITAit1prNPb0gq4dULd-8fMqh9C7t0G7V5QDSVk6N6j9Z0XX_292f-cx0in9wEfDvUQlEYFt9u-NXA6piAOAGtD97mPcEsA08my38-fOoOHVaF3yDpUaRuHSg7pC21LGLzZCBUWpD_zHwnKM9Fp0Wh0iizuQQlB2wN6G7FiFfCU7o6pcBvYYv2zpq27fqsgBaVKC9UFzUsZdWp51Hk35RqIavsl6zfK4LQBnFdjnSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e76a3148.mp4?token=U3YBVPlHfPchfJecVSxa1c-iXTDWZoR7IV53YZ-yRqEKkisund8mzWG1oyzuqqp3-E_Sl0_JUI3ubUeG4XzFdPMbRTz0U1loNce1j0DNSf8FC6yaurH8i7aIFOBpmWiWDtShq3H75I18MwoE-PZfHGwO_PQeBIyIzp2k2FnXfCi0T201EWq3ce31YcVc3YwUYCFkoyDtf8q3Y4viz3izaw4ARBk4_QWf9U-OhpGQ2_GMqlHd5nCpK1kNHuxTnPgW_Nl6950InrCFamPYHyBrfjxgGMhkmthBxmbONV0Wra36jBtq3_sPojHbBUSvbmdor_Ow00nadu-IGSuYvmLlig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e76a3148.mp4?token=U3YBVPlHfPchfJecVSxa1c-iXTDWZoR7IV53YZ-yRqEKkisund8mzWG1oyzuqqp3-E_Sl0_JUI3ubUeG4XzFdPMbRTz0U1loNce1j0DNSf8FC6yaurH8i7aIFOBpmWiWDtShq3H75I18MwoE-PZfHGwO_PQeBIyIzp2k2FnXfCi0T201EWq3ce31YcVc3YwUYCFkoyDtf8q3Y4viz3izaw4ARBk4_QWf9U-OhpGQ2_GMqlHd5nCpK1kNHuxTnPgW_Nl6950InrCFamPYHyBrfjxgGMhkmthBxmbONV0Wra36jBtq3_sPojHbBUSvbmdor_Ow00nadu-IGSuYvmLlig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پس از ورود دکتر عراقچی به خاک عراق، از دیروز تاحالا تو این کشور داره کودتا میشه
🔴
بنا به دستور الزیدی، نخست‌وزیر عراق، عملیاتی برای بازداشت تعدادی از مقام‌ها و چهره‌های سیاسی این کشور که متهم به فساد بودن صادر شده.
این عملیات با کمک نیروهای ویژه عراق و سرویس مبارزه با تروریسم (CTS)، خودروهای زرهی، تانک، سلاح‌های سبک و سنگین انجام شده.
تا الان 47 نفر تو این عملیات دستگیر شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130906" target="_blank">📅 17:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130905">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPSnGfEFXRHBkoBe9IIWg8VH7NgqLsE9AY932GdlmJEps_bWOr7gcL3zGhg-ZKQU3N8bvrQoylseLHB5lMdi31YcNHtzOiU2SrcelFMPXY6T_wwFx0UEtLP0j9d502Dn5YmqvXLJmrmJtTbWkq5DDTcuav5Xq61DMlLe74GYh6XFXfXT2JZxJfgtHRWxoikaqtK9-CfVJs2g0NxyX4nYKSdHiEeCeFkXc0elozWhYQ0qTe50G7JU5MpAuHLYXs31c0dw8b7Dt4fRdvwDv0deXp0U5OWz6OK-0wSxzORtYa_FEt4nQntKUO5kdrcMNBG-aNUEMlk5BwTzxvTFlQ2daw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده سنتکام، دریادار براد کوپر، برای دیدار با فرمانده ارتش لبنان، رودولف هیکل، به بیروت رسید — هدف اعلام‌شده، نظارت بر آغاز اجرای فاز آزمایشی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130905" target="_blank">📅 17:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130904">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کاخ سفید: کوشنر و ویتکاف به دوحه می‌روند
🔴
سخنگوی کاخ سفید اعلام کرد که فرستادگان آمریکا به منطقه و مذاکره کنندگان آمریکایی، قرار است برای رایزنی با مقامات ایرانی راهی دوحه شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130904" target="_blank">📅 17:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130903">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری / ترامپ: ایران درخواست جلسه داده است. این جلسه فردا در دوحه برگزار خواهد شد!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130903" target="_blank">📅 17:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130902">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سپاه : انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130902" target="_blank">📅 17:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130900">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyakWpzqya0NsYhDj9n8QpS0Dm4Oa-g2pNX-Iqc9-snliP7gXGIA_WczWBIRyNZVQzrg7BnVWDyu5AjKjkBQ7mZOP8FCCGcCjrAmfu81ZscW0Grl1zo393K71C_ewKEx2aOq30aIruVd1DNM38Qlulo-hjXwOu0iRbsRACbucArW8zqIM-IY4yQhMQs5rGsfVwtxgzvN4NcGM7C801NYFeMSo8b1urcvndZoXdsfRf6esgv5daa0UudTka30l-d8xhvSmDhzsq_htfWplcLjLxUbDBYp_JZLDw2LdPg9T2Z7yCaUc8DCp5iiLvljY1A4XsmXKOYS00e1JsHUmwcRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bOg2bAugkvNkdKe4RS-aZ_q_UGWd47rHqRw7xqzRZnFSPt9JopTV43tFVEOftcDjtcfdGeJ7I_6ai8dGetpxHfYYKMixCAJyCgb3jkZwkv1444TgBhDuryTRpLj2Z_sOhNmeiDEGGugutoy9PKApv3K80OWNsyDURck4zVs9mhcqgNJqmNZQRdBQB8ar7ghUgb98UnRD32IYx83dtXFPM_hPsEaF8CaUmEtxHLeXrnbtHpdp6lLSCaSgJuYD-pEHLxmBGHMmeVQo7_G_W_cKkj_PvoxukhzIKTJoSgYSEEG6Bg1kkRiYJWP4ZT2mUK2W_ofVANeDyGkYfTcN6aWnRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور سوریه، احمد الشعارا، با وزیر امور خارجه عراق، فؤاد حسین، در دمشق دیدار کرد تا درباره روابط دوجانبه و راه‌های گسترش همکاری در چندین بخش کلیدی گفتگو کنند.
🔴
دو طرف همچنین تحولات منطقه‌ای و بین‌المللی را بررسی کردند و بر ضرورت هماهنگی نزدیک‌تر در مواجهه با چالش‌های مشترک تأکید کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130900" target="_blank">📅 16:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
هشدار نیروی دریایی سپاه به شناورها: تنها مسیر عبور از تنگه هرمز، جنوب جزیره لارک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130899" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-0UaGqmC82f4Sb90stsLIM6lEDDhmqcsSyb46pzru-XfH_KySMSXabDg6ixfd8gXU1cp56NhKqS0Zw3iMVUdob4iWJIgT0-pBYxqPqZo3drhW_BKgPbDx82PiKqkgiUztC7aZLgSpRc7yNo3WRIP-fcDfB5GjpfYzTtM7XnrdSluXhDS6b2q3pFZ932W3YqvJdw0DdaDNg2SHBRao6mEclk-z0ddxSAtV0-ylAT-QO5t526saw2_NKxc1Ltch882ze4uihHbj620q0vwNsj0746OzjExWIa6oo6ucx68Z15-abFtYw-RQl6K1oPQXs31aN9LQLJK5mNj-vY-oLNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: کودتا در راه است؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130898" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130897">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0oWYsq6N_Y1QC2VgRE_5ayklCTakl_ysHZtOhyNMIVPXAXdOoRWUJSbyM4zl3CjC1UQI6dZhUF-yj89WVziUwe3wwlnuVXIxh1jzH7Dg9OlhPArLld0t05J6Gy5qief2tE30fWjfSR0vYxdGZcQKTo3bBr4ss5ELv27i03k9rDA9rqMKQj83BFvM8EVO0C_qtnK5vw92Xf08t8h2RdestRbK5Idpzdsq8_wZ4c9XLFmLFUkuQAbYJtl9h35NkdKcVuvgPRnXavsTUYeNN4cmzgiEzODR8VyPxLaTNSkpdNHvchxow4XlopdVGGTAMDAZXRUHK2Ep_lVN22F5yd49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی از کارشناسان صداسیما : تورم تو امریکا داره بیداد میکنه و کمر مردم رو شکونده، مسئولاشون بی عرضه ان
تورم امریکا تو 1 سال : 4.2%
تورم ایران تو خرداد ماه : 89%
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130897" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر کشاورزی آمریکا: محصولات ما آماده ارسال به ایران هستند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/130896" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
دلارهای کشف شده از منزل حسین منیسِ!
🔴
ذات سیاست مدارهای اسلامی شیعه انگار دزدیه
🤔
به عکس های دیوار توجه کنید، برا اینه کشورهای منطقه دارن جون میدن تا جمهوری اسلامی سقوط نکنه. ولی میکنه.</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130895" target="_blank">📅 16:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل و شین بت اعلام کردند که اسماعیل مصری، رئیس امنیت نظامی حماس در گردان رفح، در حمله‌ای اسرائیلی در نوار غزه در روز سه‌شنبه کشته شده است.
🔴
طبق اعلام ارتش اسرائیل، مصری یک شخصیت ارشد در گردان رفح بود که مسئول هماهنگی فعالیت‌های امنیتی و ضدجاسوسی این واحد، تلاش برای بازسازی توانمندی‌های امنیت نظامی حماس و پیشبرد تلاش‌ها برای «آسیب رساندن به آزادی عمل نیروهای دفاعی اسرائیل» در غزه بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130894" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130892">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLMIvElTibwJeqv6fPt4IJ8nHU-rTs-bLF3inYViAOjL9uVlXLWCHtkhHUSHhFlfW8aZi3vfmrUZxsVOXQQI2AH0TjOcZFiAJiLyPPSXpfynLqkcWlGFWYMAcS6nzk8Osar-TNU2RyzcDqLxOSYSLqH9nXM8kWtYjC0yeYFN-LeaU6u2YnBTNctNh2csllaC9Ztk-mt1LocDYaK6jazMrLtTQh8Xux3kRM_0nA4HAd7mt5jBOHx3oXShz-n38kD61F0ugMOny1p8FWqCXiVKkD6ipZvJmr-jpc1wQgBgy8yrZj2OLRwvq59sTf6nsNZVLl4gpJ4T-EbooPP2ged7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5_hOb0RaZAovmHeOstvf3NGfthSQaIPT3eYYRXItLSTnWzTXqkmKaQWxLCjReQ1FlkDxe8zvDYTK1eNdWzoIHe8ekVOfmBwqoK-zYaLFnEIWcxhlq1SI-2Ynak8zwGKQyYmNMI9BngxaQ9RiqxtQCWXc8WxSzhur4xBb7_kAnmw8OusUQQ5xv2jvRFUk9muFBZbWFa3ad3mF22quPt7L7Rg5nVAcLC-ASfpYbKc9RcxDk5dFcv59qPJ-4-dKD0S9K3Jls7Oi7OSRcP3fY4W86IZPF68QJTPlnYKS8HTiaGfyja1liaiUNqEjAbSD_XAYBFqwVpZSxPQ0XfH14F1Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک تانکر ال‌ان‌جی روسی مجهز به توپ‌های دوربرد نصب‌شده برای محافظت در برابر پهپادها و تلاش‌های احتمالی برای سوار شدن شده است، گزارش تایمز.
🔴
تصاویر مارشال واسیلوسکی، یک کشتی کلیدی تامین ال‌ان‌جی به کالینینگراد، دو سلاح ثابت نصب‌شده روی پل را نشان می‌دهد که برد تخمینی آن حدود ۱ کیلومتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130892" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130890">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PaFSlRAdO-9rk0gfSIqW1bZK-D-gLs2dxrYufOkzrKEbCrdNh9Co34gINV7uMRt6QC6EhEDdUcl7Gbn_6WK5a7Iy44Bo4Z_6oWMpC0TY8poclsGfvgv_TBShj88YiFHyI6ZX77olCemMkwH1xEEnU0ACsQ4xZDASZVk0wDks-7a5ct0w6SLz4g_4VaceOSpH184URqZyXUXxsEdPbwHQLS7j-TaU6aFpvVSdQJyltCDD28wU2nB41oi_0ihDgwcWJEyr22j7Y_z4k-EktEJBYKwVlVjefkVcu806r7aDj3TvPacDuI-DotL91cE87mDZJFxDD9LO1TLzGLa7nmbTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gU4CCHCu3cRUSqOLumtfxCxMQoKPAVzafQ6knz8u0e5Z4Hutsmxglgz_03G6caeIwpYoGd853rOiulf6rfIr70Dnpl2TQJV44tDtl42eoIygwOwyASO_ITBibUt-LlkNasQgX1QE7pOh-vswd7GAiQxwyed7GPBSTZ0AlqeXSJQuvfVU2JLMbre51-oqxJE-Dr8vNDlwp55RL7bYRchEEIVV6q-V6pR1DSULNuJjN54E99wx2vq1a7izAQ8wGxVAoFf_sQh8f67vomsiX95uEG1BTgFgVwKM2FCrNGuJy-frwq9T5F7dVoxhiq4G0egW3TgRbAEbXMwLROnDo22G1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی آمریکا به یک ریل پرتاب موشک S-200 (SA-5) ایرانی به همراه موشک متصل به آن
🔴
سامانه S-200 یک سیستم دفاع هوایی ساخت روسیه است که در دهه 1990 به ایران تحویل داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130890" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130889">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزارت خارجه عمان: کمیتهٔ مشترک عمانی–ایرانی در مسقط، نخستین نشست خود را دربارهٔ تنگهٔ هرمز برگزار کرد
🔴
دو طرف دربارهٔ راه‌های تقویت هماهنگی در زمینهٔ مسائل مرتبط با تنگهٔ هرمز و همچنین تأکید بر پایبندی خود به حقوق بین‌الملل گفت‌وگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130889" target="_blank">📅 16:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130888">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWiWkJcIcpveFobYaCphonAO1YQWSbhxpGLenuChLhFWoXtKfsHMj2WAruvJUWDoNxIVAMASH5-7aE_I-Bm1ZZD1UoNlxpCbF7vjBip61QgCoWgv3NLPRoQaHSK7xf1E115z69afR2fu68el_hyGuV9LnD7DNKo1zywdvMorKWoeC0TberYwbGehRy-VPtj9GcujOAqBO3QkAumO_Sls-eXG5M1h09CMvqlKY9gUdbdROb2RiwuR3G27C1HLvxCKxKNVGcUoQwyqG8N4-MqYEvWNevarse2ys47Eiv-jfyG1tVbokmqCuShz_WyQ6CVKMDyGrOIAznC_HHGQwaPEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اینکه خودمون بریم تحویل بگیریم باید پول بدیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130888" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dn6JHfhNwRUO7-04gkzkSC-SW_i4TOhLM0FiMHxGrMs2YPTZ2W_sMqOlSvYaBSluZBehWQ3gqT2gacjErYh-AlwuAmQRaTTw_jJtYZolQwqJQbkVQewmipGGU1C_9zITDLseweMIWPVIEcVk3mc9qEWJ8eUiXqQxf1E1y0-teWHElFbQVk5ItsSS5V9xIOqsmnS1R116tKU7BJcWgrQB45k1iozGJU9wG_gn5M3Titu8IKZ3P133z_pJfrcxVz6o1Vu1Cv9ADEbRd-3eOqIRxCIsr546D6hpUgG-Nj4L7RYrrfhbDk_Xij6rSlvYQWyJQoF6ASbGl_T3b43ThriJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7CbKCc2AB6cbbnFJ34H4741ITqxlHy15BdjMiztOnY6rgtLyjzc5s2x255SoOYIrgtObkIp6qBWVN-aXfc4o_aj8tX3Oj2ds-v7I8nYNJJ2Fu4vg3sprZCCqPpIa-yDdkOZ439ZtBNzrOkv_00_0i3xh-HjV9ClnyUy0Xesd4cndYEedm6BSx4WPKkp-hgGd6vVHYek3KifCip5Ri4qtLboHIdy79CI8UlgLhT0gmBCyhhoMpaW-rOgSpIONN2WvlPXqMv3F9jbC_11xZa1PbMmnb8b97fJ_7DXN5XSr2FKqEELsl366yqU9dSIC50mA-c1CWAb-tf1ovRIeYpkgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
دلارهای کشف شده از منزل حسین منیسِ!
🔴
ذات سیاست مدارهای اسلامی شیعه انگار دزدیه
🤔
به عکس های دیوار توجه کنید، برا اینه کشورهای منطقه دارن جون میدن تا جمهوری اسلامی سقوط نکنه. ولی میکنه.</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130886" target="_blank">📅 16:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
لاپید، نخست وزیر سابق اسرائیل :  نتانیاهو دیگه تو اسرائیل نمی‌تونه دولت تشکیل بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130885" target="_blank">📅 16:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
دقایقی پیش فرمانده سنتکام وارد لبنان، بیروت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130884" target="_blank">📅 16:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130883">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ed4036e.mp4?token=VgVOZz7EieqwWEeGQWBoxVc_D1R8_LSC-Dum_McTTW33l7Lwx1MEFIiMTjsm3_wwPdrGuEdKjhEFK84Tf3_hZcunxImh8Hp8McrCVJQA7HA6mskRAyHydmWm9hVQ4shbknYSknTegCSdAXyDK3y-PFZE651ZmKT8PGTpH7X0uUq6SESZoeqkQYxHiUM4Tlh-_PRevv7egcTgz-feosH-iLSMoD4Atq7slfTBUEWR7r6CNQ5f-ZVB5zJXKZkeu5ToZQWWKLuUeQCSa0m883h6ath-jmLiQ3QkgH9YJ3NhYtM7ye5p7qJ_ffeC9iY1u_9hfgQnp_30CpXL-7ae2avdxlZYYOg0RSE6u5mo5TEAvfOEqNv4tO-wNp5hw0ceuH1CFVGvmZaQ42JFPGGYCkKw6pMvCMoGNtfxiw0aPx_6BxgL7M8PcLV5M-Xmlbq7WH5q--QszdRUg-3Vj9SJH2G0_KqgnpVS-qFaSZRM608jyIiwx748UO6Wu8umIpN4t55oxPLsBZA4foDaQcn3OgSney9_naNFYzn2Npn-mp5Akapme1RiJ-bfNIdLypVhNsnc-Kdm4jYYEdzcv8Yqtj7Op6AbMdSxqfFuWj1nAqWqyby2W9bjrN3UOd7L6LdAeBJrGbLFCv8W9WPZfEzx7qE5xTvluncWnPzBBDNjH6MRSKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ed4036e.mp4?token=VgVOZz7EieqwWEeGQWBoxVc_D1R8_LSC-Dum_McTTW33l7Lwx1MEFIiMTjsm3_wwPdrGuEdKjhEFK84Tf3_hZcunxImh8Hp8McrCVJQA7HA6mskRAyHydmWm9hVQ4shbknYSknTegCSdAXyDK3y-PFZE651ZmKT8PGTpH7X0uUq6SESZoeqkQYxHiUM4Tlh-_PRevv7egcTgz-feosH-iLSMoD4Atq7slfTBUEWR7r6CNQ5f-ZVB5zJXKZkeu5ToZQWWKLuUeQCSa0m883h6ath-jmLiQ3QkgH9YJ3NhYtM7ye5p7qJ_ffeC9iY1u_9hfgQnp_30CpXL-7ae2avdxlZYYOg0RSE6u5mo5TEAvfOEqNv4tO-wNp5hw0ceuH1CFVGvmZaQ42JFPGGYCkKw6pMvCMoGNtfxiw0aPx_6BxgL7M8PcLV5M-Xmlbq7WH5q--QszdRUg-3Vj9SJH2G0_KqgnpVS-qFaSZRM608jyIiwx748UO6Wu8umIpN4t55oxPLsBZA4foDaQcn3OgSney9_naNFYzn2Npn-mp5Akapme1RiJ-bfNIdLypVhNsnc-Kdm4jYYEdzcv8Yqtj7Op6AbMdSxqfFuWj1nAqWqyby2W9bjrN3UOd7L6LdAeBJrGbLFCv8W9WPZfEzx7qE5xTvluncWnPzBBDNjH6MRSKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید: بسیاری از آمریکایی‌ها نگران هستند که حزب دموکرات تا چه حد به سمت چپ می‌رود.
🔴
شما این نامزدها را می‌بینید—این حزب دموکرت پدربزرگ شما نیست. این‌ها کمونیست هستند. رئیس‌جمهور حق دارد آن‌ها را این‌گونه بنامد.
🔴
آن‌ها می‌خواهند پلیس را منحل کنند و می‌خواهند مالکیت خصوصی را منحل کنند.
🔴
این‌ها ایده‌های مارکسیستی رادیکالی هستند که در تاریخ جهان هرگز کارساز نبوده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130883" target="_blank">📅 16:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130882">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
منبع ارشد ایرانی گفت که دوحه و تهران در مراحل پایانی توافق بر سر جزئیات فنی برای آزادسازی اولین 6 میلیارد دلار از دارایی‌های مسدودشده هستند که به گفته وی در دو مرحله پرداخت خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130882" target="_blank">📅 16:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130881">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMy84U6WxjHx1q113Y1rVxg2zxFpE9rX2UX0i0PzPzqEETBw5REfqnXKwPdr8YOqfSD07rHRg0fWanJG1yBTOo-DfpZn_JeX1S7mpUeKyw9XrkWKeJ97ZGheT2Znu_2m_SmXhwUZmZuJDkl5WcvEFy4kE2LxsmHez1iFRfEY9SPuayukoxO8XEFUhRAztZl0PFvq1tLTrOrSvCuvxX-L_ADcCecSCfPgEVAPGxg8k1s2xJbN6OFvcIU3bxH3Ni9kdPkDaC4Xm1yN49-mSFX7o4iyqqFlQn9odfBSzMSx0jimo4rmxlNjhgij5ISGXzbe1y-LN1Mvc1ajHweGTEQUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن ازغدی: ایران باید با کوبا و کلمبیا که آمریکا آنها را تهدید کرده ائتلاف ایجاد کند و علیه ناوهای آمریکا عملیات کند مثلاً با قایق‌های کوچک آنجا عملیات انتحاری کنند یا در آبهای اطراف آنها مین پخش کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130881" target="_blank">📅 16:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130880">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فاکس نیوز به نقل از کاخ سفید: گفت‌وگوهای فنی با ایران در حاشیهٔ گفت‌وگوهای سطح‌بالا برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130880" target="_blank">📅 16:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130879">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
عراقچی عراق را ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130879" target="_blank">📅 16:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130878">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
رویترز: توافق بر سر آزادسازی ۶میلیارد دلار از دارایی ایران در مراحل پایانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130878" target="_blank">📅 15:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130877">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f6c51391.mp4?token=QA1NeZo7sv9DCvCJkVxsz-2Udf-m20-DCeAm7rrVRb0_KsVDnQlx2LxrJT5hIjoG2r965-YJwJ3ZuqJoPlx4p7cTdX1lx2J9sCu5LFchDJ4UXONsj1ieb9WWiFIEIppAtYJC6jZNAYpPQ8LYKLmoFlPk9cq_oYA-hEEWPsBspg3tzOVBv-AiO7d1wIQT7m7obI3MduEBu6wqPWNWBeMjtcHcxTe7nFdWdLmyMAlKF7p6kBLI8owmR4o7W6NXQvWA-ljwaTiv30ZLTBwhggaCQOoM_3x1luf9cUv-Cd4ewC1ylLbZkcebq6yn3bSrLwNCajy-HUsui45O2VKSH65ftw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f6c51391.mp4?token=QA1NeZo7sv9DCvCJkVxsz-2Udf-m20-DCeAm7rrVRb0_KsVDnQlx2LxrJT5hIjoG2r965-YJwJ3ZuqJoPlx4p7cTdX1lx2J9sCu5LFchDJ4UXONsj1ieb9WWiFIEIppAtYJC6jZNAYpPQ8LYKLmoFlPk9cq_oYA-hEEWPsBspg3tzOVBv-AiO7d1wIQT7m7obI3MduEBu6wqPWNWBeMjtcHcxTe7nFdWdLmyMAlKF7p6kBLI8owmR4o7W6NXQvWA-ljwaTiv30ZLTBwhggaCQOoM_3x1luf9cUv-Cd4ewC1ylLbZkcebq6yn3bSrLwNCajy-HUsui45O2VKSH65ftw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید درباره ایران: ما به تعهدات خود در آتش‌بس پایبندیم.
🔴
حملاتی به کشتی‌های تجاری صورت گرفت و ما پاسخ دادیم.
🔴
خشونت با خشونت پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130877" target="_blank">📅 15:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130876">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869b87835f.mp4?token=BT_i-N_GLOt1jgCjCQVRGqqXbg3QE01KyeIrcxry1yGnqDJQID_YTsN1iWl55fcl0QAhA6XXGHIMziiT4RVhsa-oWZkEsT0Qs9G5SQevtq16bMR_iZHGpL8ELbLYzwXBLfcw_tMbTrD5d3lT4ROKQh2sNUEXXWK6hkoAAQ0h_2MOLnGeqtnxOjVlIWCRN3arTir3XPX3gY0ko2Ptzq60Vn6cOpMV-Amn8ClJ_WL-gj2SvB0PPLtpiKeM5oKk2IiiFX9tFhqpo569ryGIIC21oQjz6Sd2ZxK-we8sJBpLLwlguNrMpPpZ8pks3E-YNW4wpuUUeqhYSvtugxF_E674Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869b87835f.mp4?token=BT_i-N_GLOt1jgCjCQVRGqqXbg3QE01KyeIrcxry1yGnqDJQID_YTsN1iWl55fcl0QAhA6XXGHIMziiT4RVhsa-oWZkEsT0Qs9G5SQevtq16bMR_iZHGpL8ELbLYzwXBLfcw_tMbTrD5d3lT4ROKQh2sNUEXXWK6hkoAAQ0h_2MOLnGeqtnxOjVlIWCRN3arTir3XPX3gY0ko2Ptzq60Vn6cOpMV-Amn8ClJ_WL-gj2SvB0PPLtpiKeM5oKk2IiiFX9tFhqpo569ryGIIC21oQjz6Sd2ZxK-we8sJBpLLwlguNrMpPpZ8pks3E-YNW4wpuUUeqhYSvtugxF_E674Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاخ سفید: ایران درخواست جلسه‌ای در این هفته داده است.
🔴
ویتکاف و کوشنر برای جلسات سطح بالا به دوحه پرواز خواهند کرد.
🔴
در حاشیه این مذاکرات سطح بالا، مذاکرات فنی نیز برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130876" target="_blank">📅 15:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130875">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
‏این تنها بخش کوچکی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراق است.
🔴
‏اگر روزی خانه برخی مسئولان جمهوری اسلامی هم به همین شکل بازرسی شود، چه چیزهایی پیدا خواهد شد؟!
🔴
امروز در عراق بیش از ۱۲۰ نفر به اتهام فساد بازداشت شدند...
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130875" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سرکنسولگری ایران در دبی: نخستین پرواز تهران به دبی پس از جنگ در فرودگاه دبی امروز به زمین نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130874" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UQet0lktnyX2C-TgatSu0lG3kCUO9Z-k3cc0fBTV2vbV8rrnCbFQnsmnEXGub3oK4liYDomx0AQoEXaYOir_NRC-IJMttOmAV6wyyYd0YMQDerSEuPhno3dy5atFp1G05qu38msoseQROhgF7jziOrR0UUcjxmLphrFEANG8-1hFFJY-Y-8PZmJ3QaipXl_siL7G8YvyP_Tb6ouJeaBIDTZvOIJhDkvdyzK5Jv-S_f6WcMTVTOkBwr2ghRwswuH-IoCywAZIKiSw4ncVs0JMABInuyY2VXNhGiFuW-rs30B30L0qTbmyFwmSLcwq6KBQPneIrncdIXqEAYcyQaIxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر برزیل برای بازی امروز مقابل ژاپن
عمو و مادر سوباسا
@AloSport</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130873" target="_blank">📅 15:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0906a59cec.mp4?token=WIjfCIXpHMyTgN2vb1CCnr2CmD4QsSwQMgsgky36GPfIdpkc0G24ILqfR7QNIirpITEZ6FVF0n2wWTpMOrBDwUyYODKtQ5cyVm-Q8d_wPX44al37VCxKwGhDA2_tzGxHiArouTNC0AqM-Rte_tKS0c54pAUL-X8zwuCp3pGErIbcqEbX4ex8N1fa8Qse-AQifaotvQVPZJzMYlukqFwnLbcnPIhYtxZtwYrfEzTn0xeWSbTAhfeARGXhhOd8pMlGr0V1HBld5OLg517USFMVwN-JjxEWcCtapBghrrgR4c2TJ2Gxt1M16htHyysJTlpPpSI6DGt-tmc8eYklXEu20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0906a59cec.mp4?token=WIjfCIXpHMyTgN2vb1CCnr2CmD4QsSwQMgsgky36GPfIdpkc0G24ILqfR7QNIirpITEZ6FVF0n2wWTpMOrBDwUyYODKtQ5cyVm-Q8d_wPX44al37VCxKwGhDA2_tzGxHiArouTNC0AqM-Rte_tKS0c54pAUL-X8zwuCp3pGErIbcqEbX4ex8N1fa8Qse-AQifaotvQVPZJzMYlukqFwnLbcnPIhYtxZtwYrfEzTn0xeWSbTAhfeARGXhhOd8pMlGr0V1HBld5OLg517USFMVwN-JjxEWcCtapBghrrgR4c2TJ2Gxt1M16htHyysJTlpPpSI6DGt-tmc8eYklXEu20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اقدام عجیب تلویزیون کره جنوبی در اعتراض به حذف از جام جهانی
🔴
شبکه KBS کره جنوبی، پس از حذف کشورشان از مرحله گروهی جام جهانی ۲۰۲۶، تصویر هونگ میونگ‌بو، سرمربی تیم ملی را به‌صورت تار (محو) پخش کرد.
🔴
این اقدام معمولاً برای پنهان کردن هویت مجرمان استفاده می‌شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130872" target="_blank">📅 15:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پلیس آلمان: پنج نفر در پی تیراندازی در شهر شتاده در شمال آلمان کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130871" target="_blank">📅 15:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ: تهران هرگز سلاح هسته‌ای نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/130870" target="_blank">📅 15:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d4a95a20.mp4?token=NR41TH36EMYVwT31EYhJ0IR0ugPz5tRvIBG4gvWow1asFbTckrdrigCrUmInwXWW19hDmZ-1C8Fv-NliUkPC7hWlnxPu1_S_uJmilKNFuWkQsLZCJYCF4slNpGLGC9xzdop8LqUGQ9lU1UmIoA_ITubUAKr6Q2MQAIXDWDvHaEyku4hg07hjaeb7gLjScDU02U5brZiUPjus8b-flbpUNexHEr12kr7HrhT_sbWE7osXeuciTQh3C-RlBSc6q96QVYOqKeZCs4TU1z_zDGTzxksI9Iab4b46mPRmDPSMSajCBKUHTv3hulOteH-sGtw0k3CmDZDwm-27ZidnhnoDmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d4a95a20.mp4?token=NR41TH36EMYVwT31EYhJ0IR0ugPz5tRvIBG4gvWow1asFbTckrdrigCrUmInwXWW19hDmZ-1C8Fv-NliUkPC7hWlnxPu1_S_uJmilKNFuWkQsLZCJYCF4slNpGLGC9xzdop8LqUGQ9lU1UmIoA_ITubUAKr6Q2MQAIXDWDvHaEyku4hg07hjaeb7gLjScDU02U5brZiUPjus8b-flbpUNexHEr12kr7HrhT_sbWE7osXeuciTQh3C-RlBSc6q96QVYOqKeZCs4TU1z_zDGTzxksI9Iab4b46mPRmDPSMSajCBKUHTv3hulOteH-sGtw0k3CmDZDwm-27ZidnhnoDmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زنگنه : فرق این تفاهم‌نامه با برجام اینه که تو برجام امتیازهایی دادیم که پس گرفتنشون راحت نبود، اما تو این توافق هر وقت بخوایم، می‌تونیم بریم به همون شرایط قبل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130869" target="_blank">📅 15:18 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
