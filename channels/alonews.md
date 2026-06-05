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
<img src="https://cdn4.telesco.pe/file/J5JFblfJNQ0YddQag41ngFPQkhZvh2zSv_kGiAH0vfEVFePHuXB8CzSGsoUWq1K4o3DPntHCy4ak969KYBLI5w0fW5qIz6KgeXTpNzkjXRIGpSQBIkyNnlqNPmu264xizUyvl-oyzyXMOMHAZIYEIPoouNlRQ5O1xdVXVbsYlHAkZ6o756hDQpH9xHeZTuIbeHRP613B53TITNdDQJ-F-CGfbSQd3e6fk0Xqxi11-QUKazIxm-djYhopthDO8ECfOefsjT4wQA9shx3ZwVnEzKUP0S1r66WZ2oV_LwcE4BS5AkByp29x4t_uU0R_DbmQhxLHyN1kHh1lmAgq0R_lJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 968K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 17:57:44</div>
<hr>

<div class="tg-post" id="msg-125329">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ردیابی دریایی کپلر : چهار نفتکش با پرچم ایران دوشنبه از تنگه هرمز عبور کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/125329" target="_blank">📅 17:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125328">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بازگشت به بازرسی از سایت های هسته ای ایران، شرطی غیرقابل چشم پوشی پیش از هر توافقی است
🔴
مدیرکل آژانس بین المللی انرژی اتمی به الجزیره: بیش از ۸ ماه است که نتوانسته ایم موجودی اعلام شده ایران از اورانیوم را راستی آزمایی کنیم.
🔴
فرض ما بر این است که مواد هسته ای ایران هنوز در همان مکانهایی هستند که در زمان آغاز حملات بودند و تهران نیز این موضوع را تأیید کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/alonews/125328" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125327">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
گروسی: ایران و آمریکا نسبتاً به توافق نزدیک هستند؛ البته این را بیشتر در ارتباط با موضوع هسته‌ای می‌گویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/125327" target="_blank">📅 17:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125326">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6eefcf54.mp4?token=ZCENZPxDSMwPHTYbKAtMVvq_l1P-tQWMmgqom2PsDIZ8Hr_raGLL799GtpYfl_asXZRzC78B41FM9K8J_x2nNSIkfFRIIFVpN2n7XWvvzibalQX8TH5uosv4mYkInorV8511aF9R-H2_oV9s2YH5WLYIKiDhmAtR0bK2HeSe-xZbbXxzpa_SlU9zYYILTGr1dz113y1uKm8Hk-7LnpEbCufm7xNLMFZ4n8kjeee6Z7dIfRu_rQm1CLJPClaql_tqGuuQYr7lJ-NCg87AD4K58_3J_B1LA6Ccbq0gboewpX97riT3QdPbC9YS7CgTaUhyu2vKtnyDF9UI0nRQGmThTrhMXhk_quYn6VVPDJPLs30CMdZDW-lw69B8i1oiG5psK8tv1mpTTxusQ185UNpOn_ZIrKN72iU-b4gfyogzCkuugWJpfo21eJKr4d9MAYte9CUbz6BPfq2Bf69nGTNDiI3b5t2fbqvFZJ-C1BBSykDrchjjho4rX_bPtCKIBsJ0c3ZfCrNvGWItnEejbraG3geH0_gzTcF33Oh_Guyh_0qqVrsG6QzOTUXlFbp5kcFNMYgPwZpo28XSIBVWRU7EWz1kjE36-uUuJJgG5iMp0h62fcb4xkvIw-eVttEgAcV6n-qMK7UlrXoTErHy7B4NSUsB5jL9WLOONHpKJSR7-zY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6eefcf54.mp4?token=ZCENZPxDSMwPHTYbKAtMVvq_l1P-tQWMmgqom2PsDIZ8Hr_raGLL799GtpYfl_asXZRzC78B41FM9K8J_x2nNSIkfFRIIFVpN2n7XWvvzibalQX8TH5uosv4mYkInorV8511aF9R-H2_oV9s2YH5WLYIKiDhmAtR0bK2HeSe-xZbbXxzpa_SlU9zYYILTGr1dz113y1uKm8Hk-7LnpEbCufm7xNLMFZ4n8kjeee6Z7dIfRu_rQm1CLJPClaql_tqGuuQYr7lJ-NCg87AD4K58_3J_B1LA6Ccbq0gboewpX97riT3QdPbC9YS7CgTaUhyu2vKtnyDF9UI0nRQGmThTrhMXhk_quYn6VVPDJPLs30CMdZDW-lw69B8i1oiG5psK8tv1mpTTxusQ185UNpOn_ZIrKN72iU-b4gfyogzCkuugWJpfo21eJKr4d9MAYte9CUbz6BPfq2Bf69nGTNDiI3b5t2fbqvFZJ-C1BBSykDrchjjho4rX_bPtCKIBsJ0c3ZfCrNvGWItnEejbraG3geH0_gzTcF33Oh_Guyh_0qqVrsG6QzOTUXlFbp5kcFNMYgPwZpo28XSIBVWRU7EWz1kjE36-uUuJJgG5iMp0h62fcb4xkvIw-eVttEgAcV6n-qMK7UlrXoTErHy7B4NSUsB5jL9WLOONHpKJSR7-zY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان عون خطاب به ایران و حزب‌الله:
این کشور شما نیست؛ کشور ماست. این وظیفه ماست. دخالت در کشور ما وظیفه شما نیست.
🔴
مردم ما کشته می‌شوند؛ خانه‌های ما ویران می‌شوند. ایران لبنان را به عنوان اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کند. این غیرقابل قبول است.
🔴
حزب‌الله باید بفهمد که راه دیگری جز نشستن و گفتگو وجود ندارد. هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده نیست، جز از طریق مذاکره و دیپلماسی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125326" target="_blank">📅 17:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125325">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
جمالیان؛ نماینده مجلس:
کشت خشخاش در ایران خیلی زیاده شده. حتی جاهایی که قبلا برنج میکاشتن؛ به جاش دارن خشخاش میکارن. اینطوری همه تریاکی میشن. یکی یه کاری کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/125325" target="_blank">📅 17:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125324">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ZqvSI0rPJ8yqgAgXMve4aaJcaibm92Qdl_pU4S5dG_cC9a8ukpuC2YriVanzx0FesJao8YJf_SYobqiTamqGivIZzvKGFi35X4nnFPYnuCjzEufoUTuQrIVJPvqZdNN2jVZ4jevmLGSg3nGqKkguVpeXRc2dEpv1T29KrC1slV6NBm0QqU1JiIC6qlE9ok-SoS9MEtDEnsmToMMpXq1zPl9qDUQWn4CLTRL0Z6GXAq_Zm1CX9vqLhLUxwLg725boLNM4dgVAh1reTvRh5gxsdnpQ4T1XDcv6OS0bftfQom1XKUqcTezBCL1oX9ilGfMb9WPeovHMfaMhheaC0hUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وخامت حال میرحسین موسوی تکذیب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125324" target="_blank">📅 17:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125323">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=S9TPP3rSR2soWWb3zXgwxmqga6rrvaPi5SFEY6HtVCpYCG41PtjUPzBCha7uPI5byQm_ym1e36InZYc4IjpsNzbuHsnCEPoSovB2scGO5ajBUAYzX4G7LNCA0nD3kwCNZiqnMWBJ0ZmVE6IexV1FzP5i3Mwj_AKxOjcDC8Fmo6ABEi4H0U82Xoh1HS9N-s9J0X0LEDgvtfmKwvdP75oYZOI1rNW_bP0pzWloJxuC_2vjYj5E4-N0wCnQGV_RNwa6Y8cpZgotr-1M73wYRmnwOg59U5YP6LWdwNC4JQ4zp718bMw36uThKGj0mUtaXNnkaM90Cd8EB9rrXUhw7ReMVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d6cf55df.mp4?token=S9TPP3rSR2soWWb3zXgwxmqga6rrvaPi5SFEY6HtVCpYCG41PtjUPzBCha7uPI5byQm_ym1e36InZYc4IjpsNzbuHsnCEPoSovB2scGO5ajBUAYzX4G7LNCA0nD3kwCNZiqnMWBJ0ZmVE6IexV1FzP5i3Mwj_AKxOjcDC8Fmo6ABEi4H0U82Xoh1HS9N-s9J0X0LEDgvtfmKwvdP75oYZOI1rNW_bP0pzWloJxuC_2vjYj5E4-N0wCnQGV_RNwa6Y8cpZgotr-1M73wYRmnwOg59U5YP6LWdwNC4JQ4zp718bMw36uThKGj0mUtaXNnkaM90Cd8EB9rrXUhw7ReMVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهروند کفن‌پوش(گنده گوز) اصفهانی خطاب به مسئولان: من رو با همین لباس ببرین توی دولت قول میدم همه مشکلات رو حل میکنم؛ تورم، گرونی، همه رو حل می‌کنم
🔴
از پزشکیان هم میخوام حمایتم کنه مگه خودش نگفت هر کی میتونه مشکلاتو حل کنه بیاد؟ تو رو خدا اجازه بدین من بیام.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125323" target="_blank">📅 17:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125322">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPhzby0e1f-x8hMd3WKtnqFApgLs0YRJyHnH7UjrDt-Dwnh080zPi3rGLen5_m4IIkq3jVMoP15l1M4dxvyAsgecUjSuKjplPig7GuKBdlIe9sVRSwkhvE82VCDe35jeKYhir0Jcw2fkQaE2gWsFHr-58r5Bsu6zBv3Smc9_jPq0jE9fau9ffz_fb9MXJfUuihmHlOg6oAII5J5pJdko9C_Gs9LZarUaHuC9v0G4ot8kPFgYylBWC45L0GLeH_f8RlTJe0TVIXOqa6_hzy3lX3jgcQZvnEOctkOkeImOXFVHc-ei_5MpiQN3bKZPbfiBK4xEGZBhlTXdt9SYoI1d7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان:
خاک میخورم اما خاک نمیفروشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125322" target="_blank">📅 16:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125321">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipl12B0QLXrbkZlmZC8P4O6PXtR8aB3OffCgJSRmj-ujRJBdshcdnAZ1-nWe4XtHhSzRea9BaeGJqHN2ACbygJF14ikjm9Yl5p6ckZDMRmF_tZ1ENcinSVuETl9UeLtqejIbd-x8fVx_zCHkNsBKDUY4qsNwVig3yVg53yOi6IW7UWDd_xLo7KLiQso3gQ4JfX8Mkm4QKWuhk2CS6ie5Y-mZ77Kj7EmSfHRZnHon-5jat1IzMHNW0ALosc7kW5xtkZMzhwT-ub4dbxkLk7zXJ2Lc-MJVNnqaeoF08TFUaodYkJ98_42-bNGLTqvOkqXMn0790nqbWlirApv8Sh-HDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125321" target="_blank">📅 16:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125320">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJLLUTy2sin-c3J9LuAcr9GIzChUlbaezkH2p_z_N0BlWZ45o-c4h9QMTCB4KIw4EkXQPCcywBLk4yFGRYnwJktySC5jQDjhgaIXxw9I-6Ro7lMtkp7LaGoYiSNRCaLv-772SOSWH1IAH6Wf591V9nbet0ekb19tOdPbY4-wyxkkdPRpKPRApsrkexE37D4QqDxooU4OJAZTt4r4SeH8K_ZGOBnTtlO9TEPiYBXf0g3FVrUQcM7f7z6L0mKUzDz7AX2eZAv1GJKfk7UtudNIf70Fitq2oJ2mWByufNmlJff_bjCitpjLc2W6WBvemO1SxlucopWFzdHhd47fPWN72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
نیروهای ایرانی به کشتی‌های جنگی نیروی دریایی آمریکا حمله نکردند و به آنها شلیک نکردند.
🔴
انجام چنین کاری نقض آشکار آتش‌بس خواهد بود. نیروهای آمریکایی همچنان آزادانه در آب‌های منطقه‌ای فعالیت می‌کنند و در عین حال محاصره جاری علیه ایران را به طور کامل اجرا می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125320" target="_blank">📅 16:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گروسی به الجزیره: ما بیش از ۸ ماه است که نتوانسته‌ایم ذخایر اورانیوم اعلام شده ایران را تأیید کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125319" target="_blank">📅 16:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125318">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ماجرای پرواز جنگنده‌ها در ارتفاع پایین بر فراز اصفهان چه بود؟
🔴
دقایقی قبل پرواز چند فروند جنگنده در ارتفاع نسبتاً پایین بر فراز برخی مناطق شهر اصفهان مشاهده شد که صدای آن نیز توسط شهروندان شنیده شد.
🔴
پیگیری‌های خبرنگار مهر نشان می دهد، این جنگنده‌ها متعلق به نیروهای مسلح کشورمان بوده و پرواز آنها در چارچوب مأموریت‌های عملیاتی یا تمرینی انجام شده است.
🔴
گزارش‌ها حاکی است این پروازها در ادامه فعالیت‌های معمول دفاعی و امنیتی صورت گرفته و جای نگرانی برای شهروندان وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125318" target="_blank">📅 16:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125315">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94dfcf4fac.mp4?token=F0RCTXDrpOKYcNuBbKo1a7_uNrygWddsxujU7qjX0PD4qxnaGpbXNmg-75gQIZ30yiQCCnXB1NcnLjnvWLbTJpY04xT6MB848uTc-vpWLBq6HZ6quV7ypVFEOV6TVZWtRIgmysakIghcqlxnvvqnTRu1dFuBARDGJYLMhq-rVQsnUhhHL0YO2et310nNxkcUXndlS90L-HBqurREFHnoDPq_5daiFfBeKDWLIxRCqhr5SqOZWFNjocvzg4vEz2u4yssZi3t3wZkILfUVXlsVg0o0LoiEvGsccLyKQthZUUlpG0TQVqiPF7N3Dt_QMGi_Y_KclBjz5_KP7Vv77DrATg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94dfcf4fac.mp4?token=F0RCTXDrpOKYcNuBbKo1a7_uNrygWddsxujU7qjX0PD4qxnaGpbXNmg-75gQIZ30yiQCCnXB1NcnLjnvWLbTJpY04xT6MB848uTc-vpWLBq6HZ6quV7ypVFEOV6TVZWtRIgmysakIghcqlxnvvqnTRu1dFuBARDGJYLMhq-rVQsnUhhHL0YO2et310nNxkcUXndlS90L-HBqurREFHnoDPq_5daiFfBeKDWLIxRCqhr5SqOZWFNjocvzg4vEz2u4yssZi3t3wZkILfUVXlsVg0o0LoiEvGsccLyKQthZUUlpG0TQVqiPF7N3Dt_QMGi_Y_KclBjz5_KP7Vv77DrATg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی امروز نیز به حملات هوایی در سراسر جنوب لبنان ادامه داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125315" target="_blank">📅 16:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125314">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7JlToKX7E1SjMKCsgjCguoF0XCkhS8itGSeq3CFqhExsbe-pa1qdAVoXpX1Ph47U-acD_Qf6qV5q-wnxxfp1P2-LV-7eDYYy1PQig7h_n7bUZDTMsUUyGj1AU7v6gsVWbSG8PGB51ER3IY0Yl29BPVYzK--G0djp_O63rd_b0c_mOOUQLR9PDTzby7Qw6RxBoFuyPaZbR54FciDHmDTvSS4qmAzh-HoR7DMJkyByi50i5gE4KiYWCuxxTiHi5m-k5A0b6xiwfBEr_OOYhub5en2iyiAfthzghrkN9agymZvIBBo6i3iggt50PbHM_v_MlhPExY7-f1_PVbuJeTMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور لبنان :
- سپاه پاسداران ایران باید بفهمه که لبنان کشور ماست، نه کشور اونا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/125314" target="_blank">📅 16:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125313">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=PP4V24z0IG-fpCZiFJXdWIU5AICa4wxBeWRPApOoiW2z42uKMjUrpa6csHx5gqeei5APMgdlWKLTNKA_Nc72Yj4Y9ixGnRNe45VRbUI7uiGfepDmTCVqftnhvrVfj7cFvOq_ooFZ_RNOMTaqKObWJFTNQr1YhZ9ZuRKQT-vWWq-KnmHi6pklvMcLvZJSYdz-VRXL1GHjzl9Lz5zyf64x6CCSAF2qIrgmc4ofWQ4cJ1lHcUH6yANfCAQmcMRPaEGLTQr3C3JgTusdsrvnnKR9V_SecPLwjJ0BMmYe9kk7K9NPcrlOFdCiSh9fweo-F7zhaTFX9cUOWerW6p9MCduaIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5990d5144.mp4?token=PP4V24z0IG-fpCZiFJXdWIU5AICa4wxBeWRPApOoiW2z42uKMjUrpa6csHx5gqeei5APMgdlWKLTNKA_Nc72Yj4Y9ixGnRNe45VRbUI7uiGfepDmTCVqftnhvrVfj7cFvOq_ooFZ_RNOMTaqKObWJFTNQr1YhZ9ZuRKQT-vWWq-KnmHi6pklvMcLvZJSYdz-VRXL1GHjzl9Lz5zyf64x6CCSAF2qIrgmc4ofWQ4cJ1lHcUH6yANfCAQmcMRPaEGLTQr3C3JgTusdsrvnnKR9V_SecPLwjJ0BMmYe9kk7K9NPcrlOFdCiSh9fweo-F7zhaTFX9cUOWerW6p9MCduaIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ثابتی: قالیباف تو مذاکرات اختیارات تام نداره و پیشنهاد پزشکیان بوده. تو مذاکرات اسلام‌آباد اشتباهاتی خلاف خط قرمز رهبری شکل گرفته که باعث شده هیئت تذکر بگیرن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125313" target="_blank">📅 16:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125312">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان به سی‌ان‌ان : به نعیم قاسم میگم، مردم لبنان، مردم تو نیستن
🔴
ایران کمکمون نمی‌کنه
🔴
سپاه پاسداران ایران باید بفهمه که لبنان کشور ماست، نه کشور اون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/125312" target="_blank">📅 16:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125311">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت امور خارجه آلمان هشدار سفر برای بحرین و کویت صادر کرد و از شهروندان آلمان خواست که به این کشورها سفر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125311" target="_blank">📅 16:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125310">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccd93e861.mp4?token=aJ4ORk9P9fAM8X_tPms58h0XZfJoGX45-VytpN7wWINx_hlNCFhb0WcG6cnabt7C0Xib8p9a2G4zMsGfBTQvBK4awpB1ARJpRAcBPO3Xn5hYhsJrUp98ZlGYNlAF85jzVWELTZFjN7KdUr0SG-JtA2n-xt2aRBMQEmyH76nyQ516Mef-_jh5vTYCcJDX2di4leNbzVMqquVIFpIiSERtZxl0LZ1cA8FksskkoYe4jbZ44XyokgS0xyhzhgDAAX1jMfOesKafYrOTXKQwrK6Yy1Lii8ZoAEpWxIHK_3yoybF8Qs54G2DwSZu7o8Pq-ViL-2HUCudSa4No2xwuT-qXpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccd93e861.mp4?token=aJ4ORk9P9fAM8X_tPms58h0XZfJoGX45-VytpN7wWINx_hlNCFhb0WcG6cnabt7C0Xib8p9a2G4zMsGfBTQvBK4awpB1ARJpRAcBPO3Xn5hYhsJrUp98ZlGYNlAF85jzVWELTZFjN7KdUr0SG-JtA2n-xt2aRBMQEmyH76nyQ516Mef-_jh5vTYCcJDX2di4leNbzVMqquVIFpIiSERtZxl0LZ1cA8FksskkoYe4jbZ44XyokgS0xyhzhgDAAX1jMfOesKafYrOTXKQwrK6Yy1Lii8ZoAEpWxIHK_3yoybF8Qs54G2DwSZu7o8Pq-ViL-2HUCudSa4No2xwuT-qXpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاینده‌رود اصفهان پس از سال‌ها احیا شد
🔴
گزارش‌ها حاکیست که پس از خشک‌سالی‌های طولانی، جریان آب در زاینده‌رود اصفهان دوباره برقرار شده و رودخانه احیا شده است.
این احیا باعث بهبود شرایط زیست‌محیطی، کشاورزی و فضای شهری در مسیر رودخانه شده و مردم محلی خوشحالی خود را از بازگشت آب نشان داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125310" target="_blank">📅 16:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125309">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4AtYgGTb_ZptNLZT0vTbgJwgju8ttQ3fMB4N7ER1pKYpASjPIT7od72FfDQBcZX5GPVVR9a55W42rzBXqhRAV8bQko4QUg_WZfJEC26ga1-7YrvFrGy8fkWUYZApfNncQSQypKoVFsWy02_Osf-xsM8pc6IN8wYjkUKhuDCpv2CGeYJlt9z2ZaHOllThThru2OQ7qFlT3AxHn2IzyT01-F-lHHcoP4QJOtUITog2N2ttZsPJsCJqkTsAyuKQZ1o6yzTQ8ifapBjsTNfnFloWGVeRY4Csa_3mxio_I36EnsnoNKjostF5WI51EVFhrNPtNABSQNG5B0v2-JCvsqftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور لبنان : به نعیم قاسم میگم، مردم لبنان، مردم تو نیستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125309" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125308">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enTPmz-XEcVpE2yMVN3dKIklJPy98vAud6i32DAfxxPv9HnL8SCDlmLxmrZuH0p11bATogYulwC5f2dKS5KcxFak1NhKMjsmW_tCCqVD9rzkJ2P7QBq06LtF3gG1QIoHMoyhgU0H-1LbUl2SwJdxwB7bZCu3hYxOlo01TdHzQ_SX8kQf8G1hOHLVjrYRSTw7rXWo5gVe4TlyHQueTo9l4Cc8bZFoD6coML6GhTaA2a4twT716pPHh5u4fbntMCEwrDwIAlnknJsFHWDUYWwl7OAxVR1v8MPOZ4w9CrqxZIZJqBR4vaYNjCmI__eeu6iLhBb35DYkpYdtNa004p5j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
شهریار مغانلو:
آماده‌ایم که هر سه تا بازی جام‌جهانی رو ببریم و به عنوان تیم اول صعود کنیم
@AloSport</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125308" target="_blank">📅 16:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125307">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3962d58e87.mp4?token=lWI-y9vwmEhiGzNbCrpd2Ux_lMs6zIi_FFnYjWYzm3Yg9UqqIUUt4E-BO2p9Dp9__woFBgelbftCwjZu2Dvb82DGKcWZtxa6QwAHBwuEc8r5Val3D4Zbhb2AzIDmC6a7toz2d9gZtjy5XGsjvdddA3kzHhCNtl_Phhfa9fADFKieclmfKks_CM4uQoknVNhDBerAcam-gOC97nIUw01ygKpoECOO_vZS6PGyTgb2xqQCYY4nxbrmM6GHLsr3oWj6GecjHXzERvwdoZzLDr6xJk_xflatjcPsrH7GI-OdCJTJX5bcTsK-cwRazxivk9-nLCBZ8BzGG6vfeb-dH5EXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3962d58e87.mp4?token=lWI-y9vwmEhiGzNbCrpd2Ux_lMs6zIi_FFnYjWYzm3Yg9UqqIUUt4E-BO2p9Dp9__woFBgelbftCwjZu2Dvb82DGKcWZtxa6QwAHBwuEc8r5Val3D4Zbhb2AzIDmC6a7toz2d9gZtjy5XGsjvdddA3kzHhCNtl_Phhfa9fADFKieclmfKks_CM4uQoknVNhDBerAcam-gOC97nIUw01ygKpoECOO_vZS6PGyTgb2xqQCYY4nxbrmM6GHLsr3oWj6GecjHXzERvwdoZzLDr6xJk_xflatjcPsrH7GI-OdCJTJX5bcTsK-cwRazxivk9-nLCBZ8BzGG6vfeb-dH5EXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
آخرین پیام جاویدنام امیر عباس رضابخش ۱۸ ساله، قبل از کشته شدنش در همان شب:
🔴
«داداش، اگر برنگشتیم... عقب نکش. عقب‌نشینی نکن. ما برای این کشور خواهیم جنگید.»
🔴
او همان شب جانش را برای ایران فدا کرد. یک شیر واقعی، قهرمانی که هرگز برنگشت.
🤔
عرزشی حرام زاده، غیرت یعنی امیر عباس رضابخش نه تویی که اسلحه به سمت مردمت گرفتی و ادعای عدالت علی داری.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125307" target="_blank">📅 16:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125306">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / وزارت امور خارجه آلمان هشدار سفر برای بحرین و کویت صادر کرد و از شهروندان آلمان خواست که به این کشورها سفر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/125306" target="_blank">📅 16:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125305">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کیر استارمر: ارزیابی اطلاعاتی ما و ارزیابی کشورهای دیگر عضو ناتو این است که ممکن است روسیه در سال ۲۰۳۰ به ناتو حمله کند.
🔴
اغراق نیست اگر بگویم ما در خطرناک‌ترین و بی‌ثبات‌ترین دوران زندگی من و زندگی شما قرار داریم.
🔴
اولین وظیفه من، وظیفه‌ای که بالاتر از همه چیز است، حفظ امنیت کشورمان و حفظ امنیت مردم ماست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125305" target="_blank">📅 16:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125304">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
نیروی دریایی ایران اعلام کرد که ناوشکن‌های USS Truxtun (DDG-103) و USS Mason (DDG-87) تلاش کردند بدون مجوز ایران وارد خلیج فارس شوند و با شلیک موشک‌های ضد کشتی مواجه شدند که آنها را مجبور به بازگشت به سمت دریای عمان کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125304" target="_blank">📅 16:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125303">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30e85199ee.mp4?token=b7ZRhAprPjpfWhIgQDlXD8FBCrDVAjCE8rEiSfiuWVZ7g8Twjp--I2Z6PrMP4OgctU5apW2ZRBWUxTCjeSz8gW_WKs_rsRZfzjP7UV8LMEKkQlV7lLADVkMoBfpmU-LU4MwzOK4N1XGCwN4zPB-qImYwRwgPtGKynBYem3Rpm6bJMM3T_o1u6H7zsPTw6hStyHM2S5XmKs6VgtuJ9An80CvuravyNMuPg807OqzAxBIiCvdsx8MeQ6gYZUQGtfskIoXpwSkuOoBpSuQlJkz2cZGOIkase-sCtBz3JtcJ8rQBjJVE3FW8qls5uGyeKMNseQTTkLKKgCWjTL97dyD0Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30e85199ee.mp4?token=b7ZRhAprPjpfWhIgQDlXD8FBCrDVAjCE8rEiSfiuWVZ7g8Twjp--I2Z6PrMP4OgctU5apW2ZRBWUxTCjeSz8gW_WKs_rsRZfzjP7UV8LMEKkQlV7lLADVkMoBfpmU-LU4MwzOK4N1XGCwN4zPB-qImYwRwgPtGKynBYem3Rpm6bJMM3T_o1u6H7zsPTw6hStyHM2S5XmKs6VgtuJ9An80CvuravyNMuPg807OqzAxBIiCvdsx8MeQ6gYZUQGtfskIoXpwSkuOoBpSuQlJkz2cZGOIkase-sCtBz3JtcJ8rQBjJVE3FW8qls5uGyeKMNseQTTkLKKgCWjTL97dyD0Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدر اعظم آلمان مرتس: اگر در ۱۳ سال گذشته هیچ عضو جدیدی نپذیرفته‌ایم، این نشان‌دهنده شکست‌هایی از سوی اتحادیه اروپا نیز هست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125303" target="_blank">📅 16:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125302">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrM1OVm26_5_-C6dFLmfg06rkJ2iPmlpGP1a1pDfgMWjnTOkWeyWMCjlPHUFubCYmGE2wI2qAkfYZ-olOPeXROtGyvJYqaPjR_4EDmMB58ktg0kqKa1mQUWEuTBp54rkWgkZ257jqiU6wgaiIPcGBG7GBsIhIUKdKEx-f4l83IpNcHPQqEwfbwJwM31WmfMMk-aF_jJAUflRNPXxBsYGWTgBtrzqxiAW7pdxnquH-hZXeBnIaXomQCatgwmr6Z_hE-an5LUyLFNmpIxJt7rqoMXjBWBbkybo2sUZyEF8m1JRNGgKhi5iW7ncO58Non_v3P9T2iAUey662BFXY4QRWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پست هانتر بایدن را منتشر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125302" target="_blank">📅 16:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F5GTLA4l56mAcSCI54vMwBFKr1LfMC5ZYPuNkg_orZwAAHy0zYpL3ruMJpYdrnksxHA5Netj8XGU8W-g0VUvhQnvM1uz2FxFRB1B9750CHipy4CxXXBB4DkoAkg99iItXWpumrJdNK-riC7uFq_SxcRNwIzxl_JqfMKFPmy4LPuMme-KYm5dsbY37l4B3n2QR0mCqguU3K1sHOYB5clJ76SMV3e6L7BpmKZnNb244DfJyBiyzLOXjm10hZWtzUU26wU6PMNJXA3XtP0xESzQUo3La6SUkIhAqFA1QEfoLTYvZyytprrtEbL73-tPFadoovInjPVbfc4eCiFJ8Jfxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q_dyp3jQK0qAuj1fEj0RJagVNyBkyOnFx983Iw8FLz-jkyqfy8-hXfhave9EnNIOoD914QBjah6jjNGG9rp-0voCZ9vZAw-N_hGgdgqH3v59pKyXEuckL8ygdsd3SPiiN-3qMsNke7b6_-WADnPtQJrIcDNY6B_D5EBcBeYJsbaXq4nek0pe45FhdBAeDfkWTUe1eCXm0CbabGWNfJojkKMIgnLz6dlxdfJL_3iyLABwQ8uMYVcV7Wxz9gVPf0yPv7JJs6r6rob0E_htzdm8fwnMXuN7YaUajunpOQFNfqo_Fv6P5dxfNAYaI6_2HvSFTEfkmD9s_yUhy7Hw3qacFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GObNM9GorqcC8cHTbvLpR-V21-gn_dc7PbVuRtSBSqJY3unrhm0ytEmDIMcDmngPcTIwAXlqrbpDH0RQ_nr-ioSvmF-OkTZ3aiJqm1heCBWTpQqChRwByzr1M53iKM2SO2fFXgzd3ntcfZN7xtBT9GVcFCD-Z0MIds1WSGYvC-rq1P7rwBzr5MA_C_fdFb2Ao_qPxKRwL4-In4QiDi8E09kECUAGUP29zIqeOHmQz4Y-OPqKCMMMjwSTi5g9MioedlCFYwgz5asxvzdlqpw9mM7qAYbaSbfbPpILp13X-J8X3TbSfSXrOORGDPV_nq-TFoNCRdH5evceZzP-XvYTNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
🔴
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
🔴
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
🔴
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125298" target="_blank">📅 15:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سنتکام : کشتی مرتبط با ایران MT Davina رو تو دریا نگه داشتیم و رفت داخلش برای بازرسی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125297" target="_blank">📅 15:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l02ksV__Q_krvkBCWN4X_NSZnlhQvZPZzhRNEL3T9HiRCjdOPkJuQrpCSizdpB_owl4qdPM_tGFF37JSzq-FXNcNXXinEZ-Rq5ZAel2QOtcaloQieD_ZtTA6buTn5Fl_O0O3WPM6i5p0F0L8sIo5cLpYRt0b9sTPK6IOUP0RIQV66kBPhteZp03AjsxMZ2hohmj8Nf6BLGEFyieBdU2EKEZRwnRmO_HGZ54DOsoT2SNt9yncWEb-m6KJNce_DDwJlJUTpNerSdUJoY9YUxZ9Ip-OPOYo5rYU-97kwnUgxs0fGrjXRoigewrFVtXBm_4KqlQWO9JXjlJClvwkzqBR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125296" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125293">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALrtG2bsJf-4ObxKuJAGA2syc0tHurLBKj5C3T34bbkG_LFjn8m41KMUtOYsvVxOwYqjUgYH3rX7mdZmJzGRSGtv_9uzx2QiviwzZqjsVYoFQLx-evkrpji9JNBE7Ilo__VSqCWFYt8gxuFeEvOnlZ7WssUlH9pZRkr1e9Ow11VUbhSJxJ3xkJ708BVS8WH_OOsl9weGEPGqPCUd0zCdZhdH1feFaDF8miY_aTnKUldZHubAkO1HKKKHm-9YuHLVbpdBtBWwYXra8uLtJL3WGSfHiBWj27kJo06T0rIfibcY1g7RWOQPwkqsyewzVphggZi_KRtilDU-kXAX0AgvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVopM4-T2TaMAjBsDICnQlh-EA5K3Xb6xqi39oLOXggxxRCI1AflAeQwtCifncjvEwC_QfeuKk_j1KeRZmWffbTBkAMTx4yq48mG4qfRUKcBMyVtisDez8vi1EN0pV04-NpXwZr_IPATZ7NsHsgkNAm4mEzOh-oHlpgANJQ16h_1G0_QlyVFdSJep47ffvovNJRkSKZdz1xizQI1L3xV3NoJ0lbKfAt76X6hAINgeoEgNKoE0SeSSGYX02pGABmxzQ2maw8OI7dMs_nQyjGjkgSp-TqYnMpUjjA0wPqKKDnusTQTbLeT3MTnWM1d7Ynsacfavy6OdnZ80I06SGCQ7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fcf02896.mp4?token=hrc_E1kwttaAC0EJ6QbCDypCnD-g_eAXaSGVEd-Mg3e26Y12E4-8YflE0LiN9NtA_hVuJ1dhlB9L-6V2x3HfzsxsncqGzA37Doy8_xEH0v3dynRxfh4f2GcJ-BzLIGiYKybOl2TJ1I4Oz-WTciTEne_MW1ZkV8zV11PjklZd9K-LgU2dXWcLuXPZY7OBNLDRX8WJpmTt9Ckq4F_lOredYVHZCjYK2tdRs0zIcMh8veUgG0MbUelMp0rhWZVNVzfeOGLfuzFNNQKJaWNHzRgVRMxHwvMXif-Z0pYnH3knJ2gopNCcxq0-VmSK-X5CjQYJyYPRm5CreyyuI98BnvF4IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fcf02896.mp4?token=hrc_E1kwttaAC0EJ6QbCDypCnD-g_eAXaSGVEd-Mg3e26Y12E4-8YflE0LiN9NtA_hVuJ1dhlB9L-6V2x3HfzsxsncqGzA37Doy8_xEH0v3dynRxfh4f2GcJ-BzLIGiYKybOl2TJ1I4Oz-WTciTEne_MW1ZkV8zV11PjklZd9K-LgU2dXWcLuXPZY7OBNLDRX8WJpmTt9Ckq4F_lOredYVHZCjYK2tdRs0zIcMh8veUgG0MbUelMp0rhWZVNVzfeOGLfuzFNNQKJaWNHzRgVRMxHwvMXif-Z0pYnH3knJ2gopNCcxq0-VmSK-X5CjQYJyYPRm5CreyyuI98BnvF4IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ‌های هوایی به منطقه جبل الصافي جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125293" target="_blank">📅 15:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125292">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
منابع العربیه: دو شرکت وابسته به سپاه پاسداران قراردادهای برق با شرکت‌های عراقی امضا کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125292" target="_blank">📅 15:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125291">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
بر اساس نظرسنجی‌های معتبر آمریکایی حمایت افکار عمومی آمریکا از پایان جنگ و حرکت به‌سوی توافق، از ۴۹٪ پیش از جنگ به ۶۸٪ در آستانه توافق رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125291" target="_blank">📅 15:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125290">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
خبرگزاری فارس به نقل از یک منبع در هیئت مذاکره‌کننده: ما در این مرحله به مسائل مربوط به پرونده هسته‌ای نمی‌پردازیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125290" target="_blank">📅 15:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125289">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
فارس به نقل از منبع آگاه ایرانی:
ادعای موافقت ایران با انتقال ذخایر اورانیوم به کشور ثالث، صحت ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125289" target="_blank">📅 15:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125288">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ادعای العربیه: جناح‌های سیاسی عراق در طول جنگ ۱۲ روزه بیش از ۱ میلیارد دلار به ایران قاچاق کردند.
🔴
ادعای‌ الحدث: جناح‌ها و چهره‌های سیاسی عراق در جریان سفرهای اخیر قاآنی، مستقیماً به او پول نقد پرداخت کرده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125288" target="_blank">📅 15:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125287">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b3ef70b59.mp4?token=jr-dxn2YOwE8ueFwCdM-S4Rdua_v7t77IXkToa8693j7QWWPOIOO03jP3mrK5mT9xcSgFyvQ4z5lYKV4g_SoIV426UtBCdbHBqMJq3PPBHos2nzedYGEzHZGd3ECOT2ig_-embyqEV6JuhY_2Ye6dmyqazCw3M_iKktIUAdl6EgJqS6pCvV2AVZGrL04CLd0wVNiVYrKrFpjnvnn_S_R8FPs-0bhpKyFdtasImVcWUT4XrX3rk-MKRRRPoS0jNtMswyHyGPLLeKrrgl_HoBSxnJCIKRuD0V4LCmm54y0-hNZvOWkn9xUajGq2mWT5XONlQo95DVYrnLTtGY634_sDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b3ef70b59.mp4?token=jr-dxn2YOwE8ueFwCdM-S4Rdua_v7t77IXkToa8693j7QWWPOIOO03jP3mrK5mT9xcSgFyvQ4z5lYKV4g_SoIV426UtBCdbHBqMJq3PPBHos2nzedYGEzHZGd3ECOT2ig_-embyqEV6JuhY_2Ye6dmyqazCw3M_iKktIUAdl6EgJqS6pCvV2AVZGrL04CLd0wVNiVYrKrFpjnvnn_S_R8FPs-0bhpKyFdtasImVcWUT4XrX3rk-MKRRRPoS0jNtMswyHyGPLLeKrrgl_HoBSxnJCIKRuD0V4LCmm54y0-hNZvOWkn9xUajGq2mWT5XONlQo95DVYrnLTtGY634_sDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/نیروی دریایی ارتش از شلیک موشک های اخطار به سمت دو ناوشکن آمریکایی در دریای عمان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125287" target="_blank">📅 15:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125286">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
حمله اسرائیل به المجادل، منطقه صیدا، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125286" target="_blank">📅 15:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125285">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
گروسی: از سرگیری فعالیت‌های ما در ایران برای ارزیابی فنی دقیق وضعیت ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125285" target="_blank">📅 15:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125284">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی:
در حال حاضر در مذاکرات جاری بین ایران و آمریکا مشارکتی نداریم، اما می‌دانیم که آنها به دستیابی به توافق نزدیک شده‌اند.
🔴
راه‌حل بحران ایران و آمریکا باید دیپلماتیک باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125284" target="_blank">📅 15:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125283">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سازمان ملل: در صورت ادامه بسته ماندن تنگه هرمز، ۴۵ میلیون نفر ممکن است با ناامنی حاد غذایی روبه‌رو شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125283" target="_blank">📅 15:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125282">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کلاس‌های دانشگاه شریف حضوری شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125282" target="_blank">📅 14:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125281">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نبیه‌بری ، رئیس پارلمان لبنان: آتش‌بس باید کامل و بدون شرط باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125281" target="_blank">📅 14:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125280">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecn7a6zqcMxv6UYpcdVlIQzs1FSGcxPbUfE7RqyWBKKUm9-iuDCTW7fDl3WZZPFCyN3oye55Vt6xvPE-VtVhkeBeddCGf8ADEHFQGrpNf6CPBSP9DKoVKf6nNNnA85Qc72IiRd7806wQLTW4L99lNrCU4iaDt5zRP3vI-6tjD676UAOvUhKECNZX8zZNZ8OedBJVCJaH312VYzKsbnX_2aWTKOj_YyBRlNCfY8zjbtlzCsdd1RNRr81q_3SVmG2El03D2NDGUim2PeU_fKwSfvHTbKiHj3w7w34uVnXiV5vBTy-TIQDPJaY9gx_GWVZd8qisNokF_GVEkagMELtKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تا دیروز، تقریباً ۶۳ تانکر نیروی هوایی ایالات متحده (KC-135Rs و KC-46As) در فرودگاه بن گوریون اسرائیل مشاهده شدند
🔴
هواپیماهای نظامی ایالات متحده بیش از نیمی از جایگاه‌های پارکینگ فرودگاه را اشغال کرده‌اند و عملیات تجاری در فرودگاه اصلی غیرنظامی اسرائیل را مختل کرده‌اند
🔴
با وجود گزارش خبری قبلی که ادعا می‌کرد نیروی هوایی ایالات متحده بیشتر هواپیماهای نظامی را از فرودگاه بن گوریون خارج خواهد کرد، چنین اتفاقی نیفتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125280" target="_blank">📅 14:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125279">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObSrG6FvIHbNlWMtMftosjnLhbOCEBphb2pA_F2bMYMfBAz-5pFw-8Tnl2eM06usdjdVsYS0pR8QW_iZpL7jSPJ08XCK4n2PxYitgUz0apBJLsjLK-8EwheAO2bSDej9DJf0VrVOMZOncuBC0DbBVGwAPwy1NNvgcCx7LJeBppTlI3Y_tLgU4Aw8cWy_leemaNsSqAhj_hGULs9CyQcCFe7c1T6DlzmagIiDg7bVJElsg8YzaVMj47K2DNsJeNzD2e9OZPayUXrtgTcCM4zWPR9h19slK0peiSJC6_bvvDU5JzH9hvCmZUmwjpXA0v6fAU9ARqoA2OVQaYWmhzzNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125279" target="_blank">📅 14:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125278">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
العربیه: اختلاف اساسی در مذاکرات، آزادسازی دارایی‌های بلوکه‌شده ایران است.
🔴
روش و سازوکار آزادسازی دارایی‌های بلوکه‌شده ایران، یک شکاف (اختلاف نظر) در مذاکرات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125278" target="_blank">📅 14:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125277">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کرملین: احتمال دیدار پوتین و ترامپ در تابستان ۵۰-۵۰ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125277" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125276">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnt6sGSk7LyHAfT01hcLp0M4mJRHgRAqMK5UGtQfI1MX3sJGMFAUBkciem5iLmnxfxVK4pRut80GQUfSd3FLacYs-M0JyLAR46A11lOX9iA-k_iCUrQ-4sDyBDOE1majjGY1NbXCIKGKqOLAXKV-uFan55xM6sizPDD-zP6b7Q8hpyD0s1oUEnV-DyJujnjtRcYddqLIi-wPFoEqtMXC2vPJASPtX4vzoZJwcU7NoIxbALHYClK2O6d2zyXCUU4-H-32cj6wy771LsHAoIorPHM9It3gw5n4wgt0QdBi3ewXWf6-PdeSSzq2ni8joAoJn9jGNKLKdo19i0I_wJ__EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهر سکسقیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/125276" target="_blank">📅 14:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125275">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
جمالیان، عضو کمیسیون بهداشت مجلس: میزان کشت خشخاش در استان‌های ایران بسیار بالا رفته!
🔴
در استانی که قبلا برنج می‌کاشتند، امروز به کاشت خشخاش روی آوردند.
🔴
با توجه به اینکه این محصولات خالص‌تر هستند، قطعاً شدت اعتیاد را افزایش می‌دهند.
🔴
خشخاش‌هایی که [غیر قانونی] کاشته می‌شوند، جزو کشفیات است و به کارخانه‌های داروسازی تحویل داده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/125275" target="_blank">📅 14:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125274">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت خارجه جمهوری آذربایجان اعلام کرد: در حمله پهپادی شب گذشته به دو کشتی باری خارجی که ۲۵ شهروند آذربایجانی داشتند، پنج نفر کشته و سه نفر مجروح شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/125274" target="_blank">📅 14:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125273">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
العربیه: ایالات متحده همچنان با درخواست ایران برای آزادسازی دارایی‌های بلوکه‌شده مخالفت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125273" target="_blank">📅 13:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125272">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ماکرون، رئیس جمهور فرانسه : جنگ اسرائیل و لبنان هرچه سریع‌تر باید تموم شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125272" target="_blank">📅 13:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125271">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125271" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125270">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=HHpP4GVX1DZ3jyZyRk01zttcAkAWje7qtc-geiPPSRgZIFPkbPdbTcxtd2q7hk3TVJXdgMhDGZmUSu-qOndeIZqkGDhpVKBLILh8LXvDZT6ub8vZYZqyYOfc40L8wZigTC7cXc0dnOHJB_SnKrBpNWm3-jALxfdIyCmKVvsNC97VfOcYauuw8PimL5khgI3HiWzNG6NM-uIe-CaHU0q45K-WlWmiebOQXUdPVLjZ6FQd9a_bFSX-aPHQJ49wkWPOhzQk0PfPEP4dYSeN7ITQgij2kSUJHO5AAUE4tf_A_RYYjBd7CMFNNIZOLL7NyOSEk1UESLKP-ja5fQfGJJQ5Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c893a4439a.mp4?token=HHpP4GVX1DZ3jyZyRk01zttcAkAWje7qtc-geiPPSRgZIFPkbPdbTcxtd2q7hk3TVJXdgMhDGZmUSu-qOndeIZqkGDhpVKBLILh8LXvDZT6ub8vZYZqyYOfc40L8wZigTC7cXc0dnOHJB_SnKrBpNWm3-jALxfdIyCmKVvsNC97VfOcYauuw8PimL5khgI3HiWzNG6NM-uIe-CaHU0q45K-WlWmiebOQXUdPVLjZ6FQd9a_bFSX-aPHQJ49wkWPOhzQk0PfPEP4dYSeN7ITQgij2kSUJHO5AAUE4tf_A_RYYjBd7CMFNNIZOLL7NyOSEk1UESLKP-ja5fQfGJJQ5Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیرحسین ثابتی، نماینده مجلس: آمریکا بعد از جام جهانی سنگین‌تر به ایران حمله خواهد کرد و ایران را تبدیل به غزه دوم خواهند کرد.
🔴
باید پیش‌دستانه پتروشیمی‌ها و زیرساخت‌های منطقه را بزنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125270" target="_blank">📅 13:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125269">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681a291c50.mp4?token=Bspp7tOM-Y7R3P33TKKc--Yb12_xxoECQH_mxcV2nIi0FOGcwokMXQ-3R4Y7bRVnGMVb7Wz7oqeIzyXGo4QANWKy6wLA-kifkmodtzyGoEyTknBIUh_PiwXgUlhqWWzU09qimPtyG5lYXSBtczIFqpyknTiEmncXlI9a0QmYW2MjSlv6nSg_OvRsDpb72GYRaB_xXu2hW0DiFjkTHNvzHLaOW4ZHEmDHU0DrYgLdxdtN7iUOinQXC2lBkp1EoQ6zpQLHk2RtYjH3HChB3shmJnLueQZuSk41xKIsmHgX-R8NxvlXjq-sT097Wm60kA_jlJIREx4foD2bMU7KoE8IDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681a291c50.mp4?token=Bspp7tOM-Y7R3P33TKKc--Yb12_xxoECQH_mxcV2nIi0FOGcwokMXQ-3R4Y7bRVnGMVb7Wz7oqeIzyXGo4QANWKy6wLA-kifkmodtzyGoEyTknBIUh_PiwXgUlhqWWzU09qimPtyG5lYXSBtczIFqpyknTiEmncXlI9a0QmYW2MjSlv6nSg_OvRsDpb72GYRaB_xXu2hW0DiFjkTHNvzHLaOW4ZHEmDHU0DrYgLdxdtN7iUOinQXC2lBkp1EoQ6zpQLHk2RtYjH3HChB3shmJnLueQZuSk41xKIsmHgX-R8NxvlXjq-sT097Wm60kA_jlJIREx4foD2bMU7KoE8IDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ آمریکا، پیت هگست برای شرکت تو مراسم، رسید به پاریس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125269" target="_blank">📅 13:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125267">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gjvj_YWcPEwC2C6N3wY6IlBOhHbhl_d3DExO-WbUaa6FOCQl_uT3o219TYDjaWxZnpz25fXcJCiDFvVcnBgulMR0Z4fsp_AMsrwF-9EJUzaC0dCYvblyNpFZo1ThXS7EK_tLIi-PnB4x2kDJUQsuyRGMfdBIuO3xLO41YlxkIPOJ_Nq49iUDE03-CB6ylYX7zm82hUhOzCYJm4NaUnlSCapHnqsP1vdeOiKFKIvMxp6EfSqF42z15dmFj2KsothnVIuswbIIj08ckjJVFKOx0JXUz4ea5UHlaVngq3MREspEaUkcyyi79AVnDcH_V3xjdXWl4Z-lb-vJpnUDMalJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJFL9zaTmPT8A6e4n-eAc58hw9f_izrGQDBfPq049I-hYeTEMjzFnNvrv2WeJMPWzKphyoPtIWhxs5LL1pg-1ZJP71mfjg-i3gCJxTOwqNeWZNacJK5hjC_T3mr-GkSx46dzVf0ewJlR5lYmU-p9EQf3yU3gDtChjgTeqimn0kdRch_IFSzwAQzfYUT-ZCGmMeDlY3Lyi9zSc3vMWe7dGac56_Ivc-G_RhAWx8DIIaOQl8vKW2WWAQZeJfNIA6sy7-PzY8fCfHgjYGEd5Sd2gKR3de4dwFakLjvNpT5sVyM56ZDlv25F3IW5xpBvg0d9F-t7YNHXYqWhR7Vdkjz2IA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سنگین‌ترین موج تورمی در تمام تاریخ ایران!
🔴
۱. نمودار اول: تورم نقطه‌ای و متوسط سالانه
🔴
این نمودار روند تورم نقطه‌ای و تورم متوسط سالانه را از سال ۱۳۸۹ تا ۱۴۰۴ نشان می‌دهد. الان تورم نقطه‌ای روندی صعودی را آغاز کرده و از تورم متوسط سالانه پیشی گرفته. این اتفاق معمولاً نشانه آغاز یک موج جدید تورمی است؛ موجی که انتظار می‌رود در ماه‌های آینده اثر خود را با شدت بیشتری در اقتصاد و زندگی مردم نشان دهد.
🔴
۲. نمودار دوم: تورم انباشته ۸ ساله
نمودار دوم که بر اساس داده‌های بانک مرکزی تهیه شده، تصویری عمیق‌تر و هشداردهنده‌تر از وضعیت اقتصاد ارائه می‌دهد. این نمودار نشان می‌دهد که در ۸ سال گذشته، تورم انباشته با شتابی بی‌سابقه افزایش یافته و از ۲۰۰۰ درصد عبور کرده است.
🔴
بازه ۱۳۲۴ تا ۱۳۹۷: تورم انباشته در محدوده‌ای نسبتاً کنترل‌شده و نوسانی قرار داشت.
بازه ۱۳۹۷ تا ۱۴۰۵: روند تورم انباشته وارد یک مسیر عمودی و انفجاری شده است؛ مسیری که نتیجه آن، کاهش شدید و تاریخی قدرت خرید مردم بوده است.
🔴
به زبان ساده، این یعنی قدرت خرید پول ملی نسبت به ۸ سال پیش، بیش از ۲۰ برابر تضعیف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/125267" target="_blank">📅 13:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125266">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-EYriCkA9gWkbN6MlUY6Sv2LRC5aVIaECqkEF79z-dfXs9-ylmI4FAET7gCWx6iFIDha08_60PUYncqSduWTL0-EqhiKi1tgOC6e5z_55TDxQC3HqELwEGxMZy5-PWpn0XMy5I_NakTQz1YWEYpmYcvMQKgwdqk5iF2VyEztl0tsmMnDo_zZrxyGpFwbBmsHbdVLHs7EPSd88FLf-dQMjrGIUu3Y6QgvijtvjjDXXKgvvBjLwTE34pB4kjCIN18ZiY1KWAtqEUsFFWPP5NRKBMcWvgqbgsqaw7FkR9ptxf262DlHUc9pFqgzbbYi1V4qXYechDbpZh7TxturgN5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار یک پهپاد دریایی «مرتبط با جنگ اوکراین» در بندر رومانی
🔴
به گزارش رسانه‌های محلی، یک پهپاد دریایی مرتبط با جنگ اوکراین صبح روز جمعه در بندر کنستانتا، از مهم‌ترین شهرهای بندری رومانی منفجر شد.
🔴
وزارت دفاع ملی رومانی در بیانیه‌ای اعلام کرد این پهپاد حدود ساعت ۱۰:۳۰ صبح منفجر شده و «احتمالاً از نوع پهپادهایی بوده که در جنگ اوکراین مورد استفاده قرار می‌گیرند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125266" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125265">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3719112f5.mp4?token=Zivzj6QyX2TQ5UK27XkO04yfXRkGEXMuK7ptBauzmCcCCeS09k7wRKayKT_idgO98xMHFakGQAW0sgbXaYGRjpt51Mt2bD0q73uELuEKGiA5UQ8bxjR1mVf__J0GgBhCPg0DWk5hkOmxQ7Rqp8wtbjMcQrfDeuQz6IA3tO6vdIeVvo1Ny-3aBLxzGff4GfRPRc_u-PydaZXajzSMppxflhwCKsB6wZN_HHoyRgNaHPwYj1qT_3iFirx-OKQ866-z7_K8EuER7rnvU9X8VY-FanrGkciW3sjhNRw-mqugwvOdxh4TUzh908LyPbWZKrMX9GjclehXXqBGi4RgDKph-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3719112f5.mp4?token=Zivzj6QyX2TQ5UK27XkO04yfXRkGEXMuK7ptBauzmCcCCeS09k7wRKayKT_idgO98xMHFakGQAW0sgbXaYGRjpt51Mt2bD0q73uELuEKGiA5UQ8bxjR1mVf__J0GgBhCPg0DWk5hkOmxQ7Rqp8wtbjMcQrfDeuQz6IA3tO6vdIeVvo1Ny-3aBLxzGff4GfRPRc_u-PydaZXajzSMppxflhwCKsB6wZN_HHoyRgNaHPwYj1qT_3iFirx-OKQ866-z7_K8EuER7rnvU9X8VY-FanrGkciW3sjhNRw-mqugwvOdxh4TUzh908LyPbWZKrMX9GjclehXXqBGi4RgDKph-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زاینده‌رود زیبا به اصفهان بازگشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125265" target="_blank">📅 13:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125264">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سفیر ایران در مسکو تاکید کرد که ایران با دولت عمان برای مدیریت تنگه هرمز در حال مذاکره است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125264" target="_blank">📅 13:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125263">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7d920c97.mp4?token=uBhFGM9tBPMi8mRfnAGFbw6D_PiDZN11cm8_U4AzPdNhYbFsNbCH8XO0olT0uK1GltGvD9R000ddUrGBaUIHRoGS47B_bm1UyLEbgKxjsnC4_9wxVRW4xfiqaBHTHW5twBt5CNsnYXgqjGNkco29IgnFblBA7p5Qm7DH2adAsByAbYgDXcTZjN1dmYCbsQB-2CSwVhSOifmv5-2ENNaOs20oMeW3vFSwEIu-sQIYWsIPHl3kf_TXUgtlnZW9jyZbr5J45aQ3ojw-ixywm326F3pFH9i4QG7iXy-V72rxSS8gi0lvl5cZt_D4JWAfYC3kSvVH3s1E3BJYxAPaO6bhEwE3GlvSK2LXvSwG4esbNnApuBEdMHfdXs0Og8n1MeWIYyMeTb1gmyFOArAxQOO-QgtBYWSbcwfKy6KoUZU0MRaYYjuM0AvTQMdMdlgITZjrBHYhhRrmeiLvPipLH1zxEp769Q00YV9cc-T_K97LaU-60AccPqb9PJUJ8EJHFmF1cKZ3x57P-E_fHw15KCHtZGAM8PC2M2Qs4lKUFvwY7O4eNe-PrNqHBAMriR846yseFuzkZF5CKAgKWQeaLDtzvSHdE3U7c_C8Dc68fnmfibVbULLzkpwX0nZH5mAEh-wIJCjZVhmibB89bbxH-NDhwT9sRuJd_9G-rgLZrszOnPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7d920c97.mp4?token=uBhFGM9tBPMi8mRfnAGFbw6D_PiDZN11cm8_U4AzPdNhYbFsNbCH8XO0olT0uK1GltGvD9R000ddUrGBaUIHRoGS47B_bm1UyLEbgKxjsnC4_9wxVRW4xfiqaBHTHW5twBt5CNsnYXgqjGNkco29IgnFblBA7p5Qm7DH2adAsByAbYgDXcTZjN1dmYCbsQB-2CSwVhSOifmv5-2ENNaOs20oMeW3vFSwEIu-sQIYWsIPHl3kf_TXUgtlnZW9jyZbr5J45aQ3ojw-ixywm326F3pFH9i4QG7iXy-V72rxSS8gi0lvl5cZt_D4JWAfYC3kSvVH3s1E3BJYxAPaO6bhEwE3GlvSK2LXvSwG4esbNnApuBEdMHfdXs0Og8n1MeWIYyMeTb1gmyFOArAxQOO-QgtBYWSbcwfKy6KoUZU0MRaYYjuM0AvTQMdMdlgITZjrBHYhhRrmeiLvPipLH1zxEp769Q00YV9cc-T_K97LaU-60AccPqb9PJUJ8EJHFmF1cKZ3x57P-E_fHw15KCHtZGAM8PC2M2Qs4lKUFvwY7O4eNe-PrNqHBAMriR846yseFuzkZF5CKAgKWQeaLDtzvSHdE3U7c_C8Dc68fnmfibVbULLzkpwX0nZH5mAEh-wIJCjZVhmibB89bbxH-NDhwT9sRuJd_9G-rgLZrszOnPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس: جنگ ایران در بودجه پنتاگون نبود, حالا ارتش آمریکا به مشکل سوخت و مهمات خورده است
🔴
جنگ ایران در بودجه پنتاگون پیش‌بینی نشده بود و حالا وزارت دفاع آمریکا با فشار جدی در بخش سوخت، مهمات و ساعات آموزشی نیروها روبه‌رو شده است.
🔴
دریادار کادل، فرمانده عملیات نیروی دریایی آمریکا، در کنگره هشدار داده است:
«نگرانم که از بازه زمانی جولای مجبور شوم درباره نحوه آماده‌سازی و تولید نیروی عملیاتی تصمیم‌گیری کنم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125263" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125262">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر خارجه روسیه: ترویج گفت‌و‌گو میان پادشاهی‌های عرب و ایران را مهم می‌دانیم
🔴
ترامپ گفته بود که «ایران را به عنوان یک تمدن نابود خواهیم کرد»؛ این یک بلند پروازی گستاخانه و هدفی دست نیافتنی است
🔴
آمریکا به وضوح می‌داند که در موقعیت ناخوشایندی قرار دارد و نمی‌داند چگونه از آن خارج شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125262" target="_blank">📅 13:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125261">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرنگار العربیه: آمریکا همچنان درخواست ایران برای آزادسازی دارایی‌های مسدود شده‌اش را رد می‌کند‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125261" target="_blank">📅 13:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125260">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf655e55b0.mp4?token=p0Hg3zO2J31A5HklFLbg1oWGEuMnkBKJXW5SnXvfG5rvjwOuUL0ic2_N9twmwe4-XJgeb8-EHJLyH_790qmrPm_jja9Ehhi8Pvtxh884jUFOurWsbSURzPHQtyL7jfTAtMjTMRyym1l9xH3qK2LjfUK22pW1DFUzQGc5nfS07CcobUbhPihEU4viTD8RoPSJTCM65FFD0POy0fKQFsKuNuk2d8u5YngxLbV2M6dKXGqCE4K1d4XouAZnBk1ZxbOUbROQStey27RXo9qyVgVkWGvEwwCdMO5vJ8xRSA2_nQFWftv2vL20Tjgr-0uWa7OnaH4wTLYZ06Rj7A5Mu7D2bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf655e55b0.mp4?token=p0Hg3zO2J31A5HklFLbg1oWGEuMnkBKJXW5SnXvfG5rvjwOuUL0ic2_N9twmwe4-XJgeb8-EHJLyH_790qmrPm_jja9Ehhi8Pvtxh884jUFOurWsbSURzPHQtyL7jfTAtMjTMRyym1l9xH3qK2LjfUK22pW1DFUzQGc5nfS07CcobUbhPihEU4viTD8RoPSJTCM65FFD0POy0fKQFsKuNuk2d8u5YngxLbV2M6dKXGqCE4K1d4XouAZnBk1ZxbOUbROQStey27RXo9qyVgVkWGvEwwCdMO5vJ8xRSA2_nQFWftv2vL20Tjgr-0uWa7OnaH4wTLYZ06Rj7A5Mu7D2bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جاوید نام ‎سعید تروند ۳۳ ساله اهل ایلام شامگاه پنجشنبه ۱۸ دی در آبادان با شلیک مستقیم گلوله جنگی حرام زاده ها کشته شد.
🔴
او متاهل و دارای فرزندی ۳ ساله بنام آریامهر بود.
🔴
اینجا پدر سعید تروند با فرزند جانفدایش بدرود میگوید.
🤔
عرزشی حرام زاده ، پدر مادرتون باید مورد بررسی قرار بگیره که چه حرومی به خوردتون دادن که اسلحه به سمت مردمتون گرفتین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125260" target="_blank">📅 13:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125259">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مرکز ملی فضای مجازی: بر اساس بررسی‌های فنی و ارزیابی‌های عملیاتی انجام‌شده، قطع اینترنت در هفته‌های اخیر، تأثیر معناداری بر خنثی‌سازی حملات سایبری پیشرفته نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125259" target="_blank">📅 13:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c84ebce81d.mp4?token=quF0nH_--fGXWPEsE1SYx65O3q3vGa-IqtAATvNca4qt7onLFHyzUtiK3BqJdO3hXe8zHgc1-88ZhFCRNQpO167rtEPFIJooJN9Vzc61ukhaOPJ_A8GMCOrPMQD8KIbTosxfVbRie2J3cEY2XDTRIqtnLviJWyi4-lBFR5q_MRudmcxb-RtOiZ-pe0-GKD0xojZGzEo_mNtWWDiGJB--m92WhxaNwbllEJN95sP0Vz7772_4KnbTW7D1SQwnY6jCgsk1KcadJo5nkiywKSehBwWGOnUiW92x7Q3ntoWn_jtzcKKar8VaW1QqTp0jwUdnwueOC9qXUi_InxTQjkFtdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c84ebce81d.mp4?token=quF0nH_--fGXWPEsE1SYx65O3q3vGa-IqtAATvNca4qt7onLFHyzUtiK3BqJdO3hXe8zHgc1-88ZhFCRNQpO167rtEPFIJooJN9Vzc61ukhaOPJ_A8GMCOrPMQD8KIbTosxfVbRie2J3cEY2XDTRIqtnLviJWyi4-lBFR5q_MRudmcxb-RtOiZ-pe0-GKD0xojZGzEo_mNtWWDiGJB--m92WhxaNwbllEJN95sP0Vz7772_4KnbTW7D1SQwnY6jCgsk1KcadJo5nkiywKSehBwWGOnUiW92x7Q3ntoWn_jtzcKKar8VaW1QqTp0jwUdnwueOC9qXUi_InxTQjkFtdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد از هشدار ارتش اسرائیل برای تخلیه، مردم جنوب لبنان، و اطراف نبطیه، شروع به ترک منطقه کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125257" target="_blank">📅 13:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOdo9qymQwxWoOsO3zYO3O39UnxbgYzqTUBFE2p0RA2NIJcol0ahntqpRFJN8GmutSgUD4wEInHfYodI1OVnbJiQVBb610qMFaqeKlra9hbsHBLIcZ1OK9F7Dc2KPmnW2vTkNYhzNcp_zE006Ldr5TdnNU1hn2CcX4wiy4AsI-qlunMJYNptv5C_mgHw-Y8kOsKWpyBmTnHgqsR85Rm8PRwEMNy-ItD8SnC5sT309yk8y16BLANBTprowO5G9DdbscHXFhtPMOBqzuR8BPeQN3GMBKD1TPeYLjSMC7vquRbMiXo89LCewf4bpvYbEckoZIAPyLnG4wyXLE-lSSwlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125256" target="_blank">📅 13:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asZsbjUC-Ra_yTNP7Ekgwudj08jmnY_j-r9KNtWXBAZGRzqO2AuerxXsBvDSz6jCf0Nbjpea8nhkrhajvbeIsGiw6iakynT87Cuz7ePmfLf9GiCrUd7Vr_xg64dClmvOIYYDr0jYUSAh6T3OWGKtLJA-7eGrsZ8ZsL7TOhvxMnPF6nmxJtfLkWsuBqySU0cJvTRi1ivJN8jtnQBLcl6vKeWNsivIf3hiNxfOU7RRX-PyWM7o5nqHaZfU0Jn79uwb3KqIQ59K6zEIoYEhfB9D-kAXXDbB3gKuSjUJPMxZWBZNEc4McSSmCB6s9-rHYlDg3ItsYZcrTx1sHW0Dpg2KGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه دیتاسنتر ایران با فنلاند
🔴
سمت چپ: دیتاسنتر ایران.
🔴
سمت راست: دیتاسنتر فنلاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125255" target="_blank">📅 13:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_1s-p_5gONSGHaY_BEIZYHUdEW2PMN7k1RBXLo7B1oijTFivz51hdWZ1tTO8U_tbgmyvKicosJ_FicywTLUKcMfYu_5puPkZwhFf99EA80q6ESCw-_9TWR8FsdyfxnoNf3fkzcEUHx1fizXo6eG_ukYO0ghmd_A8p9EQQK2vW8CQ3I005PWGJT63uWEgNbHkD4P5UYvNU6Q5wo3-V6rOH6_Nbm7YP4wbbvtYiVciFA2WINfphDP03txngbezf6T9f5EJarl60Ju7dRX_XESUqvq6Hvcw65huTAlKFEYqXyEb0uLZnouqpa9x6MDZSFcInEAEU312SLIjo9Fysht1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنا با ۵۲ رأی موافق در برابر ۴۷ رأی مخالف، لایحه ۶۹.۵ میلیارد دلاری برای تأمین بودجه اداره مهاجرت و گمرک آمریکا (ICE) و گشت مرزی تا پایان دوره ریاست جمهوری ترامپ را تصویب کرد.
🔴
سناتور لیزا مورکوفسکی (جمهوری‌خواه از آلاسکا) تنها جمهوری‌خواهی بود که به این بسته رأی منفی داد و هیچ دموکراتی به آن رأی مثبت نداد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125254" target="_blank">📅 12:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125253">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea310363a4.mp4?token=FoG432RzKFmvT-LYqKYErtlHjJC3DMQwJMQ1eI92vaQ8KmllXCIrUg__8IAvfO6lZHg_5uU5UXb766rAMp8TZ0ZRySnyo16YIm_25CfgKyjwqf1Fsg3YyrJ92glTnsVXKq1Y6cgcVBZPJftAW0_ryI-ISWtrupiJ8jy5FSW0ufDuBdt0x77QGfZVTFjp-oQVOb4vh8N49v1MVBjGN1O5oN9cI4k05CKnWWPZJYXsHHPFyCm2ESh4ikGmJie2Lq2ycanmqpNncukAbErE6qomnHywqj2dGcwdEJORiAxazqnmPipk3aigO-ODeNlpSFcoHFNK3OGFcdKMUk6x8p0iXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea310363a4.mp4?token=FoG432RzKFmvT-LYqKYErtlHjJC3DMQwJMQ1eI92vaQ8KmllXCIrUg__8IAvfO6lZHg_5uU5UXb766rAMp8TZ0ZRySnyo16YIm_25CfgKyjwqf1Fsg3YyrJ92glTnsVXKq1Y6cgcVBZPJftAW0_ryI-ISWtrupiJ8jy5FSW0ufDuBdt0x77QGfZVTFjp-oQVOb4vh8N49v1MVBjGN1O5oN9cI4k05CKnWWPZJYXsHHPFyCm2ESh4ikGmJie2Lq2ycanmqpNncukAbErE6qomnHywqj2dGcwdEJORiAxazqnmPipk3aigO-ODeNlpSFcoHFNK3OGFcdKMUk6x8p0iXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جایگزین برنامه 90 بزودی با نام حکمت‌های فوتبالی روی آنتن زنده میرود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125253" target="_blank">📅 12:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125252">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwzeLI2M_nFl8y2-3BzTJpu7g6Yp88XzxGZ7saRKn_U4vKoJncOXqadVRKZqclbgcV1xfDzwWZd4GCDXmk_Ccw5sACbusUPBmWJ1qhWo4Ao0JwNV0YRBRO1JPuW6k4fPoXds2PspmRqJxW58iNVTYeph5ALxf3jR1S0fLMaXrSsVuMdBvhtnSFDz_i7BRQT4OIZ4q9N4I7mSarXVBADVfwS-98jPx9JI_-JhsDGT5BgrjAoqdZASj7DSZj4_V-yhc5AYpapM0yPlUkdtIe1MXy5Mo6_0u_j74gMcXxJyfUWRz-FBcCmB8ayFAXug1tHsv3BLE18nBkOZPD6inI223w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجموعه ای از حملات هوایی اسرائیل شهر عنقون در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125252" target="_blank">📅 12:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125251">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa9d58916.mp4?token=keAjNT5EAtbjGCzqR68o7xZiS_4A5pLBtZ92WZurIdaDzNoMfQHreeFeoz6m5hYS8m_i04Nsm25GG1zVZKidlj1lVs1OJnzvsAauB51D7k45ZwZdy7_KjiJU6Bkacb-b5Yk6i2Hw77d5XkJa_WXCLrFXa4XcU7jTUjieM8vispoQ739oJPqRLMCAFDmtR0spypB3GsOoxZ4ngN6lqU-pvTxd3X3pYHsaIMmUCi-NkuIBV9uheqj56PO3i4FOq9ZXFAiAegAvVOPMsSOGlqZhEg8fwa1hQtXir_fnRbEsQUdPsQF3n2pStVv-2j-iG6um0mtb0maH9fWJqO5krnyuZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa9d58916.mp4?token=keAjNT5EAtbjGCzqR68o7xZiS_4A5pLBtZ92WZurIdaDzNoMfQHreeFeoz6m5hYS8m_i04Nsm25GG1zVZKidlj1lVs1OJnzvsAauB51D7k45ZwZdy7_KjiJU6Bkacb-b5Yk6i2Hw77d5XkJa_WXCLrFXa4XcU7jTUjieM8vispoQ739oJPqRLMCAFDmtR0spypB3GsOoxZ4ngN6lqU-pvTxd3X3pYHsaIMmUCi-NkuIBV9uheqj56PO3i4FOq9ZXFAiAegAvVOPMsSOGlqZhEg8fwa1hQtXir_fnRbEsQUdPsQF3n2pStVv-2j-iG6um0mtb0maH9fWJqO5krnyuZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم خشمگین آلبانی در حال برداشتن فنس‌های حفاظتی در جزیره آلبانی که توسط دختر و داماد ترامپ خریداری شده، هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125251" target="_blank">📅 12:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125250">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
حملات هوایی گسترده در جنوب لبنان در حال وقوع است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125250" target="_blank">📅 12:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125248">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/175f9b173e.mp4?token=E_gvC73UkDDPpwg6HkXF9OPp2rARMfVld0O8a7zw6_A1ILmi_yqntGR-vt2RBFGZE-Oxl2P-n6lh6LmbDEawaBdD838kUIInrbaeJYKtp9m7fU_Aoon9YEjVve9rdyuijPymk9a92by9Sv9oh6SxIqLOjFI0jWmkn_GrN0Wb-FtzXLy8D4R-OkDdq2ji6JdB7cKOz5BTGfPMMp3izxU7SUBs5tLr0sUCnrF5Cm3eWdT4FUwPxvbvVSU_MUtggW3-Xn9rq7VeA6qSzqnd6R6ZOAQilF_rVZAZJrerZDyvHyARY98pkGfLxyaachcogpnC_b2qimr427WMCXmy2w7Sxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/175f9b173e.mp4?token=E_gvC73UkDDPpwg6HkXF9OPp2rARMfVld0O8a7zw6_A1ILmi_yqntGR-vt2RBFGZE-Oxl2P-n6lh6LmbDEawaBdD838kUIInrbaeJYKtp9m7fU_Aoon9YEjVve9rdyuijPymk9a92by9Sv9oh6SxIqLOjFI0jWmkn_GrN0Wb-FtzXLy8D4R-OkDdq2ji6JdB7cKOz5BTGfPMMp3izxU7SUBs5tLr0sUCnrF5Cm3eWdT4FUwPxvbvVSU_MUtggW3-Xn9rq7VeA6qSzqnd6R6ZOAQilF_rVZAZJrerZDyvHyARY98pkGfLxyaachcogpnC_b2qimr427WMCXmy2w7Sxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرگئی لاوروف، وزیر امور خارجه روسیه:  عملیات‌های آمریکا در ونزوئلا و ایران هر دو مربوط به بازارهای انرژی جهان است.
🔴
در مقطعی، آمریکایی‌ها حتی پیشنهاد دادند که تنگه هرمز به صورت ۵۰-۵۰ توسط آنها و ایران کنترل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125248" target="_blank">📅 12:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125247">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a7eb67c92.mp4?token=bX4ueCH2yEsMW2F_Jeay6tzrM216wJkteHpxCOoSnXyRu-lvU8UTU4c0ljeZKjNYv1rkDbCavkX4WlhtHsz0UldRYEMJpF_HevGmCh-5T2jT8FF19nanuVnnartd_CehB_LuS2S0bdRmhfjf5uz1YQgqxz_S-368lGlNJzrb7VwLzV17SU9oXQGl3l2yWKk0fl_g89d4RWeVRsnH_YRpJYtiYGPHwXl89-dSq-BIqf_43P7113vMr6p5egiG-itviWb9hZWG01vwf7MWp-Mbj5b5xpOY0NEmj-J5mJytqQ7oD-2xH8JI8yQPXKquMb2ndWXU-NOs5qLbUhzotza_rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a7eb67c92.mp4?token=bX4ueCH2yEsMW2F_Jeay6tzrM216wJkteHpxCOoSnXyRu-lvU8UTU4c0ljeZKjNYv1rkDbCavkX4WlhtHsz0UldRYEMJpF_HevGmCh-5T2jT8FF19nanuVnnartd_CehB_LuS2S0bdRmhfjf5uz1YQgqxz_S-368lGlNJzrb7VwLzV17SU9oXQGl3l2yWKk0fl_g89d4RWeVRsnH_YRpJYtiYGPHwXl89-dSq-BIqf_43P7113vMr6p5egiG-itviWb9hZWG01vwf7MWp-Mbj5b5xpOY0NEmj-J5mJytqQ7oD-2xH8JI8yQPXKquMb2ndWXU-NOs5qLbUhzotza_rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از یک زن ایرانی در مکه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125247" target="_blank">📅 12:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-XlmG_hm91p6i--bXw6GyTl5GuSY1MoVSzxeQObbyCRKnIkyWFhA4_5kt98cmeQt0y97RcYqOVu7tuwStLPhpBy5YA4CWevABbeq_3Y7LQr9ZhK87J8zoFxrnrfpJYlOij22f1cQLQcl0Sz_jhTcvbKm7zElQyvxlJCULB2U0QJ3bFjVCVYjDE2zor1VBCZewZMZMRY7VHYh572enGktuHJk0V_t9CsX7OV6hZQszMncTpFYw88plknPEvDtvDtT71bwppW9S-QW3XatrYt5hh9u4bhyilFfL3Xul7KpTbqi2nYYm_ss9uF7CtiOdxwESRWnjCmVR9eWirBKfjM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس تیمی نروژی‌ها پیش از جام جهانی به سبک وایکینگ‌ها
@AloSport</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125246" target="_blank">📅 12:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125244">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
مصاحبه با یک خانم بی حجاب: چرا تو این شبها تیپ های مثل شما کمتر بیرون میان؟
+خرشون از پل گذشته و میان به ما میگن پرچم دستتونه شالم بزنید و تذکر میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125244" target="_blank">📅 12:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125243">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
دیمیتری پسکوف: برنامه‌ای برای دیدار پوتین و ترامپ تو آینده نزدیک وجود نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125243" target="_blank">📅 12:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125242">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سازمان ملل متحد از اسرائیل خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت ملی این کشور احترام بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125242" target="_blank">📅 12:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125241">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
شی جین پینگ رئیس جمهور چین، در روزهای 18 و 19 خرداد به کره شمالی سفر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125241" target="_blank">📅 12:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125240">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
العربیه:وزیر کشور پاکستان برای دومین بار در عرض ۲۴ ساعت با همتای ایرانی خود در بیشکک دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125240" target="_blank">📅 12:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125239">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
خبرنگار : نظرت درباره اتهام نسل‌کشی از سوی وزیر خارجه ایران به آمریکا و اسرائیل چیه؟
🔴
روبیو : ایرانی‌ها خودشون استاد نسل‌کشی‌ان؛ هزاران نفر رو کشتن
🔴
هر مشکلی که تو خاورمیانه می‌بینید، یه ردپایی از ایران توش هست
🔴
حزب‌الله؟ ایران، شبه‌نظامیان شیعه تو عراق؟ ایران، حماس؟ ایران، حوثی‌ها؟ ایران، اسد تو سوریه؟ ایران
🔴
به هر طرف نگاه کنی، از نظر اون پشت همه این ماجراها ایران قرار داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125239" target="_blank">📅 12:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125238">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ebd4642f.mp4?token=UTbPJZqmu2eUDAjDVfqYqoFURquSTFPSkXvw9s3f49bwUuAZP33Qf2FrIVkzS59pX8K33729NtrQt4T34Z_3qI2adkcb6kJsEGB5c64fAUrh4TTMZOaH9jrk8PnuvMTAWTNHuV-Gin_cy8Vbpw-sV-vd5ROfMV22XrE9IMaTdUOHWfy6HVCU8P0yJd3kM6IdQWDxFjSHS7oRCRR9Ydsb9hnbOCZGcdsPCkzp1WuXhbUXZTLY0wS_hUeQPakqovJayeMwJFFc2reig1b7UdZBy3cQUsTkmeyKHrT7xKvZ58pAYUn_8roefTVuJnVohYYdQFWLgzgoddkJKK8EX93ubQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ebd4642f.mp4?token=UTbPJZqmu2eUDAjDVfqYqoFURquSTFPSkXvw9s3f49bwUuAZP33Qf2FrIVkzS59pX8K33729NtrQt4T34Z_3qI2adkcb6kJsEGB5c64fAUrh4TTMZOaH9jrk8PnuvMTAWTNHuV-Gin_cy8Vbpw-sV-vd5ROfMV22XrE9IMaTdUOHWfy6HVCU8P0yJd3kM6IdQWDxFjSHS7oRCRR9Ydsb9hnbOCZGcdsPCkzp1WuXhbUXZTLY0wS_hUeQPakqovJayeMwJFFc2reig1b7UdZBy3cQUsTkmeyKHrT7xKvZ58pAYUn_8roefTVuJnVohYYdQFWLgzgoddkJKK8EX93ubQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حرص و ولعی که حرام زاده های حکومتی در کشتن مردم داشتند در هیچ نیروی خارجی که در صد سال اخیر به ایران حمله کرده دیده نشده.
🤔
حرام زاده عرزشی، هرکسی حرام زاده های محله خودشو میشناسه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125238" target="_blank">📅 12:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125237">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ارتش اسرائیل در پیامی برای ۶ شهر و روستای دیگر شامل الصرفند، تفاحتا، البابليه، قعقعية الصنوبر، المروانيه و السكسكيه هشدار تخلیه صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125237" target="_blank">📅 12:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125236">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNRv1g6pEb1mI6fdufm2yoKJjZb_nSa1so6y1xh-IU-q2UvhBQZ32sMFnx1pibP0TZm2FzeCPW_Po15t5brx0_JfcPTYQA83pIxT0wl9-o0lZfgOpJb5SkLy_E8rpbUok-ljPhjIH0JFuQyLt1rwklkNnRplksSydhg-E4fPMyCTBOOcz26NBS7lQ3AmgCXeQR-Unl_BZxZ4sVxzy-kmO4wYezQWM3qi6XqeTDyZ51kry14D0Hf75cRCvqxfPoQmWoqlWrdT7-FFv-Y4xd2QrmD33o1eJ3BJEXG3jZPRLJWFkjQvr3qSeIuDkyZdZffeOvICshhgEsGhPBtO4CdGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه خبری المیادین از حمله پهپادی اسرائیل به شهرک‌های «تول»، «حبوش» و «تبنین» در جنوب لبنان خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125236" target="_blank">📅 12:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125235">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDDouLEqSfyi572cbjenrng4QF8z-RpfY7qoW8v1X9ixsobt0gn7OVXEupohuwzV2JXhBO_SibnnIb20PP5ZRnOZgNwIAr1kmGxThaZvdETSucdv-TM6VFV8lDiYEqLwhg_OCcSaBQjObtsXUrBZ9tVpAPt2TUJai-_JpHhCcJkZNBSp5859Kj98c1RfPNM8FjT9ecLL34dtfZnDp21F4W9AlQWwb7FCJCEomV3D68mVq6xg9qfqKYotPog_MfNAqg7XQWIZOsPdlbzJFS7ZEGntX6BYFHlj4Doh4yETGrsFcL9PO4F1JH4Uz4NQ_ypmtJiUQ_Qm3TlaKOC7KBZIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل: یک فرمانده واحد مهندسی حزب‌الله را ترور کردیم
🔴
رسانه‌های لبنانی از ترور حاج آدم عبد الحلیم حرب، از فرماندهان یگان مرکزی نبطیه حزب‌الله خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125235" target="_blank">📅 12:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125234">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78399abc8d.mp4?token=imnZPKDsSxUaLCtt-x8IS3gV3YVjZoGhk-y6yyQWx-gGRCLPfVfZqXv7XU9chDk6fLH8hIIvcP3nUNW5MRhaXWLLrq33EAjPg-of-_PFHFemgoobwCYOSbQjOHtFLyuHzbTwvkWcaYeagFHfKJrCIpsi0VukUOWSkHm-8zdQyu3bShW7Bml4a20Qb9N5P4xkdFWZPSwvhVeV_An6tGdJ-DEMSmb5LWAWZZSNlMYB0I7RnsbSbw9Vh33NeNxm_lmXdN4u-R4Ydz9Tw9o7h30bosqwmBPQ-hO1jE5V-j32-VMVa5xUpLUbphVdJAeK5Icis5Z0XWFm_5dTEnB4MXhMQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78399abc8d.mp4?token=imnZPKDsSxUaLCtt-x8IS3gV3YVjZoGhk-y6yyQWx-gGRCLPfVfZqXv7XU9chDk6fLH8hIIvcP3nUNW5MRhaXWLLrq33EAjPg-of-_PFHFemgoobwCYOSbQjOHtFLyuHzbTwvkWcaYeagFHfKJrCIpsi0VukUOWSkHm-8zdQyu3bShW7Bml4a20Qb9N5P4xkdFWZPSwvhVeV_An6tGdJ-DEMSmb5LWAWZZSNlMYB0I7RnsbSbw9Vh33NeNxm_lmXdN4u-R4Ydz9Tw9o7h30bosqwmBPQ-hO1jE5V-j32-VMVa5xUpLUbphVdJAeK5Icis5Z0XWFm_5dTEnB4MXhMQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از ساعتی بعد از آنکه دختر ترامپ از تصمیمش برای ساخت یک جزیره در آلبانی خبر داد این کشور بهم ریخته است
🔴
مردم شعار میدهند کشور را  به اسرائیل نمی‌فروشیم. اینکه مردم اروپا داماد ترامپ را هم معادل اسرائیل می‌ دانند پدیده جدیدی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/125234" target="_blank">📅 12:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125233">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
بلومبرگ: قیمت قراردادهای آتی استاندارد گاز طبیعی در اروپا از روز جمعه گذشته تاکنون ۷ درصد افزایش یافته است.
🔴
قیمت قراردادهای آتی گاز در روز پنجشنبه به بالاترین سطح خود در ۴ ماه گذشته رسید، همزمان با کاهش بیش از حد انتظار ذخایر داخلی گاز.
🔴
نرخ پرشدگی تأسیسات ذخیره‌سازی گاز طبیعی در اروپا کمی بیش از ۴۱ درصد است که نگرانی‌های اروپایی‌ها را افزایش داده است.
🔴
در صورت ادامه بسته شدن تنگه هرمز، رقابت با آسیا بر سر محموله‌های حمل‌شده از طریق دریا ممکن است در تابستان امسال تشدید شود.
🔴
قیمت گاز طبیعی اروپا در مسیر ثبت رشد هفتگی قرار دارد، زیرا همچنان توافقی میان آمریکا و ایران حاصل نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125233" target="_blank">📅 11:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125232">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سخنگوی سفارت آذربایجان در ایالات متحده در بیانیه‌ای به سی‌ان‌ان گفت: «ما ادعاهای بی‌اساس مبنی بر استفاده از خاک آذربایجان برای عملیات علیه کشورهای ثالث را قاطعانه رد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125232" target="_blank">📅 11:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125231">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سفرا و نمایندگان دائم، ایران، چین و روسیه در نشستی مشترک با رافائل گروسی، مدیرکل آژانس اتمی، موضوعات مربوط به موارد مطرح در نشست بعدی شورای حکام آژانس بین‌المللی انرژی اتمی را مورد بحث و بررسی قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125231" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125230">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7e8e2790.mp4?token=HPmHGiBNZ9caHsqvIa37w1CNyElnBOC0er15zWsieUUVsDyhPaRQKCbIYDfRdacf_aAAMIYetioXbl_drzXX2hxnBhbEWCl6mBmhEIiUVXnQbK5n7AKsB2iihws1LCCn0wbEmsxMsWf8ciEDv5dPkFtRXk7r4eILNDPt8AzfLH5LV--IHf0fgQgYXzePaSk2KHUXio9PSoz5kxT5qfUZ2ru_jQRcEt6m_nFBscu63xx4jtVq7WzPj1wG31TVlclgviFiXo-lrc-oZM7GZQv3GhWQbOBoABy5a2quWCcLUScZSqce2mO6_iLusSkjsjdXFjMnvBgXIg8aHVc0cp5nnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7e8e2790.mp4?token=HPmHGiBNZ9caHsqvIa37w1CNyElnBOC0er15zWsieUUVsDyhPaRQKCbIYDfRdacf_aAAMIYetioXbl_drzXX2hxnBhbEWCl6mBmhEIiUVXnQbK5n7AKsB2iihws1LCCn0wbEmsxMsWf8ciEDv5dPkFtRXk7r4eILNDPt8AzfLH5LV--IHf0fgQgYXzePaSk2KHUXio9PSoz5kxT5qfUZ2ru_jQRcEt6m_nFBscu63xx4jtVq7WzPj1wG31TVlclgviFiXo-lrc-oZM7GZQv3GhWQbOBoABy5a2quWCcLUScZSqce2mO6_iLusSkjsjdXFjMnvBgXIg8aHVc0cp5nnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی مطهرنیا، تحلیلگر: در آستانه ابرتورم هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125230" target="_blank">📅 11:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125229">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بلومبرگ: مذاکرات ایران و آمریکا همچنان بدون پیشرفت مونده و در حالت توقفه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/125229" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125228">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=YSxBEPrI1kfjODPGJypo6XebTRUVn9v_Hc87AjYQhFE6tjCCVzpikP6kZ1aEZ1-r3VFtXUc7FN6y6JfZk2Pl06qU2j77HtsaQoJ0_q1cNzqWhQMaNlnBqCJWuxpXqAg67PeoQ5YqeywLZkt4uQ6ehK7kb_9jWhu57FRBntZoF9Pp8Zv7yVdFNyl-ptlzQzSYm4lag15SmlqBlVt_rWFnaSoONKGUwljlZFFyUdmSiIEnrnOeIOozPBdoOco8WLyoyyrjdSEpldpQAAesAWhE2P6HsKad2NvLFPV9flaEvuLmOOnBXXD_pGyIJ6e43CDqa-0bF3WUQQpfyaQhcwP3bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=YSxBEPrI1kfjODPGJypo6XebTRUVn9v_Hc87AjYQhFE6tjCCVzpikP6kZ1aEZ1-r3VFtXUc7FN6y6JfZk2Pl06qU2j77HtsaQoJ0_q1cNzqWhQMaNlnBqCJWuxpXqAg67PeoQ5YqeywLZkt4uQ6ehK7kb_9jWhu57FRBntZoF9Pp8Zv7yVdFNyl-ptlzQzSYm4lag15SmlqBlVt_rWFnaSoONKGUwljlZFFyUdmSiIEnrnOeIOozPBdoOco8WLyoyyrjdSEpldpQAAesAWhE2P6HsKad2NvLFPV9flaEvuLmOOnBXXD_pGyIJ6e43CDqa-0bF3WUQQpfyaQhcwP3bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیک‌ها همه بالا
🍷
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125228" target="_blank">📅 11:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125227" target="_blank">📅 11:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125226">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTKtM8bg3REZ07QEZrfjOLi-JcX04XkFUYWdXS2CtgCAOVdW_UOyNujkRnAQsr-AmLZuXSjh4TUXVK_f--Uxn_gm1v3ytOeW704usRrOIbwr_VKtVUVp038KP7O2HTCq0e-3ZWuUdzo_7k8NbzjXYO-JkCVgtH0Qcjqur2DNQ074QRazprz_H9pIQQhBb6b6gEJO8a4rqmmowefUuPeneU4XQGFDfGujpow55OnUu4JG7CibqVfpEQfA7qoaFEKLM3BC0Mi7aw3jJDeFb9479CqQXYbJt_xOXnElhA6VxGDCNGJ6cSg__HB-QWlFQ1jwM7hHA-fvwvKBPtmdIa7NPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آذربایجان چهارمین کشوری است که گزارش شده اجازه داده نیروهای اسرائیلی علیه ایران در قلمرو آن فعالیت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125226" target="_blank">📅 11:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125225">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هر گیگ فقط 2هزار تومن
😳
😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/125225" target="_blank">📅 11:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125224">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3s8KR6HNBW7unXwOtioDK6WUs3xgDEwfvrIvGkrltLEWkaC9l7L_D9kyjnsorLqLym9UsXYuYG50IRmamspQ_TqY8cju13dQGPSzero-ZbJsbRdOEqBb8LKHJG3CuqvliFdllMFz_vTbTc7NyoU5lbG9lIBzLmBhVyIy1ZpgDWCtEkXT76zx6AqNVOkkuZ4Gn9hyuh3gFWTZAF1vjHVvVmXXZYXEVfp_kDBYaDaaH6B_kBImr2i4QWgx6QTZyPa4S0TvE1zokq3PSab9X7ApZR776ElaOSkZ20vn8yS5QiLfhPdRXz74YjXs3EZWaUatzpyPQNVjUPuWutxyYewvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط 2هزار تومن
😳
😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t
با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه ، سریع اقدام کنید که دیگه قرار نیست هزینه زیاد بابت وی پی ان بدید
👇
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/125224" target="_blank">📅 11:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125223">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583002539d.mp4?token=dE9X5sXDpqihvbKUIW1mCbRCaDBelSmg8zvGj9tHfJ1tYrNoB0B7w6sFm6InYRxuM4DfHXF_XhfeQ61o8oFcVNDTiT69BK2XKADzijHRv-s-vKGuNdWqtQTnP8w7DUBTDDD0gV32l08U1VfckHpL5QNwYw9QKgzi28E_aD4XaE2JXmvPxBqBhpYq71_66RQFMPplR3hy-hB-__u4DPOefId-f-fOS4uxjNcwHGjNXxJ4JkzbRwmYyEnjPND-bpy8SrLvpoIFmUN3zxtH82FVeTDY4pyCyeipDKI01fANR551JGgnLe9rsHS1Y_OQ5L5-a8OO-saTjMa1UxIQqrd3w3aOwyPzA9TkAd9IrciH-80nAt7S_oKcuqdvLk3Fpa8L2vXaP9n_6VHop4XdAxXZBkMOIFMZ0VTu_opzvFv1L5jjO_bS_vGT7dIe5-1GGA5wPfeaMI70mfavHf151oZ-cCZxn2dCXFnuWG43f9tvAq_XKOdiRdOM1TnQDtrpP4R6LQJR9_5SOc3qrv2f9nB3xlDVJ0MyEfn0UQ0jrsvQB718T3Nmtu5300ZSGlaUZeLq9-ct4bhVTQOI5et_V1-Vn9q17D0NFnXCX-wL72eMPi4nrX64xCve8oqQkg7lW47CvunxitP0Lf3g_k60MPlmxeF_vNSMzZVodIPOysnL8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583002539d.mp4?token=dE9X5sXDpqihvbKUIW1mCbRCaDBelSmg8zvGj9tHfJ1tYrNoB0B7w6sFm6InYRxuM4DfHXF_XhfeQ61o8oFcVNDTiT69BK2XKADzijHRv-s-vKGuNdWqtQTnP8w7DUBTDDD0gV32l08U1VfckHpL5QNwYw9QKgzi28E_aD4XaE2JXmvPxBqBhpYq71_66RQFMPplR3hy-hB-__u4DPOefId-f-fOS4uxjNcwHGjNXxJ4JkzbRwmYyEnjPND-bpy8SrLvpoIFmUN3zxtH82FVeTDY4pyCyeipDKI01fANR551JGgnLe9rsHS1Y_OQ5L5-a8OO-saTjMa1UxIQqrd3w3aOwyPzA9TkAd9IrciH-80nAt7S_oKcuqdvLk3Fpa8L2vXaP9n_6VHop4XdAxXZBkMOIFMZ0VTu_opzvFv1L5jjO_bS_vGT7dIe5-1GGA5wPfeaMI70mfavHf151oZ-cCZxn2dCXFnuWG43f9tvAq_XKOdiRdOM1TnQDtrpP4R6LQJR9_5SOc3qrv2f9nB3xlDVJ0MyEfn0UQ0jrsvQB718T3Nmtu5300ZSGlaUZeLq9-ct4bhVTQOI5et_V1-Vn9q17D0NFnXCX-wL72eMPi4nrX64xCve8oqQkg7lW47CvunxitP0Lf3g_k60MPlmxeF_vNSMzZVodIPOysnL8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره خروج اورانیوم از ایران: ایران مثل ونزوئلا نیست که چند دقیقه بمانیم، بعد خارج شویم و آنها برایمان دست تکان بدهند.
🔴
در ایران باید یک تا دو هفته می‌ماندیم، به تجهیزات عظیم نیاز داشتیم و آنجا یک منطقه جنگی واقعی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/125223" target="_blank">📅 11:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125222">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHc-AmPBdtPrB_4obTS0WgY2lLkua1fJIOY9g6MlBeuQKmtR6rxaDqhMRgFujfVXbi6u4_UCZfegCRkG9Az0IAePYnKalEbA8JlpR0xrnPCbvjwk_Xr05VWT7genOEmQ0ctMF8K0MA4sHPKopVSiLmy2pl_do4RcCBFU2XMQZj5qJJ5WtwoWlb4Pg4Kh_JYpzQmgeEP_bp1L9SVzCInFlSIWHYIlJr50WhExX7BvpqPZXVeZfMH062GZUlALjGBb2EJPa-Z95Lby7meAiPMDIg3Vdkb4fEzRzBYBn1kWDmtpcbMx61MHCfONIsOgUmc6sX9yujwm-ZTSaWWL-RNxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نظرسنجی جدید ماریو نشان داد که ۶۲٪ از اسرائیلی‌ها با «اجازه دادن به ترامپ برای تعیین عملیات نظامی» اسرائیل مخالف هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/125222" target="_blank">📅 11:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125221">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رئیس پلیس راهور تهران بزرگ: تردد اسکوتر‌های ایستاده و نشسته بدون پلاک در خیابان‌ها و معابر به جز بوستان‌ها و مسیر‌های ویژه ممنوع است.
🔴
هنوز سازوکار قانونی برای ثبت تخلف یا اعمال قانون برای اسکوتر‌ها وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125221" target="_blank">📅 10:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125220">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سازمان ملل متحد از اسرائیل خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت ملی این کشور احترام بگذارد.
🔴
سازمان ملل از حزب‌الله خواست به تصمیمات حاکمیتی دولت مرکزی بیروت پایبند باشد، به حاکمیت کشور احترام بگذارد و روند انحصار سلاح در دست دولت را بپذیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125220" target="_blank">📅 10:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125219">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
العربیه: وزیر کشور پاکستان برای دومین بار در عرض ۲۴ ساعت با همتای ایرانی خود در بیشکک دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/125219" target="_blank">📅 10:48 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
