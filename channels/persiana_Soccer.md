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
<p>@persiana_Soccer • 👥 634K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 03:22:42</div>
<hr>

<div class="tg-post" id="msg-28557">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxGm45GIUZTR_m2vJba4-oJdk-pKmPKIrEeYjTfHVrLaYcEw2ao5oSmft5s1BhgQ-iRJQSNBTeTM-rxpT6Qd85Zx-OUr_8HCdzHwoHNs8QDkQ_5UgYMtfrh6J6e4QP62ChzG6J5u3xSsggfTMSBI77q8BKR2sptylT-VFg8R-yFrZmM97g6AuqoyA1VSr3LMNbklQRbSuUQ9sqggi0IZQCHZChl1_Mi4628SMFFcBzgFn7JJu6aM5WCblp6_bFuB4UQjSS-6uSOAZaBRgg3fk-T1bK-U-5KeW4pZiin5LtfU_AWyHC5Y8iXqrwSE5u5MszGqf--Y9FRmTSQn9fAwiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
دوئل‌جذاب‌تیم‌های هانسی فلیک و ادین‌ترزیچ این‌بار درلالیگاواستادیوم نیوکمپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/persiana_Soccer/28557" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28556">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8xHG5_0n4gfgfMDFD6qw-8WVbisqoPxKvXkkpweYz17f1d2AyoPKiybLJfHCaWGOL0KTRAEIJqFGnT65Bqw0ogZ1x19t5FvFVIWnFqwabFU7We0fCZiQl1qBwsRujvI7_rtjrGPsQF2ESNvRjCbnr7tYBb_UkgGY0dBUbGjLr3YZjg292xsKf1xStiZXWfjXSm57T9IAjbmwpSxr4Zhza2N2OsFLKaeA8YnEAeJJasnT7BYZqwnWImOr6Gn3sNKcWvobny7inLsqBpulOT4ObpHRP-63eMmXpPG_N5dXbyUt69JMro6l02JdNjWRLEdQJep13u-PO4Py0BPHFmonQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
از برد رئالی‌ها با هتریک امباپه تا صعود یاران کارتال به دور گروهی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/persiana_Soccer/28556" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28555">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=PmhWYhgquqIrp8tANnHWF27qhT0j5iAHFjJAvUKNBAmP2kWmZt77JesCpMkFSf28YtjSVuqPJcAKC9m6AtA_uq7XKrRJhrUsiW2zSB3rD8Ax3PrCEenDo7bqflAx-oTXaM35AUr9snmtZsV5-C_AWTxbHXgXJqIYqngzLB3dmG3t2e32icHzhZJD_WtJaukUkwV-6KLYHH0vhGIBqjEqTR5EsF8FwJZTL6zUN3Ee-Blg8ScD1dIBTDQztQBtVpPhsyoHESwGBwQTRzh0duRuf14iXRICOfwLhJfUVOUQXlM0e4NqD6Bxy0RbLaY7T8MgriL19IvTurqulTT1F7padA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=PmhWYhgquqIrp8tANnHWF27qhT0j5iAHFjJAvUKNBAmP2kWmZt77JesCpMkFSf28YtjSVuqPJcAKC9m6AtA_uq7XKrRJhrUsiW2zSB3rD8Ax3PrCEenDo7bqflAx-oTXaM35AUr9snmtZsV5-C_AWTxbHXgXJqIYqngzLB3dmG3t2e32icHzhZJD_WtJaukUkwV-6KLYHH0vhGIBqjEqTR5EsF8FwJZTL6zUN3Ee-Blg8ScD1dIBTDQztQBtVpPhsyoHESwGBwQTRzh0duRuf14iXRICOfwLhJfUVOUQXlM0e4NqD6Bxy0RbLaY7T8MgriL19IvTurqulTT1F7padA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#هشدار
؛این‌ویدیوکوتاه‌از صحبت‌های مهم دکتر علی کرمی مدیرآزمایشگاه‌کنترل کیفیت مواد غذایی ببینید درباره مصرف آب معدنی برگاتون میریزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/28555" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28554">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-U-Yt6kjYIa4y7KdpkTAlfV9zlPznzSO59Xo4n3R635xr2wvUqywj-dcsfmTUrS_uuxTINAxh0hgpJopHeoD73eBtToZNeMd91pDEBg0jP1MeyR0o07PxIawMj3i0TKQgfzhxbZnG3P3p7Mc0KLpAOwP18JTSFh3xIM5T0g871tBrpRJmCXIhOxe_KiFqQ8e3lo0DhQZY7dBAWnFLTg36Belnv4f6VaxVsDhx4HuNuCwgPZxveOgGFk4x1jgdvmtbxpC95f6CX6wYQMW8SfQjJxpfkURBg_jNRvUzae3kBxXujrrHRMRGpu0j996J1lEnhADsFZZeAKHmKclHg6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/28554" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28553">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRbytw2Olw_BNqneKOubPqLA-7WWHhg2H_sTkHX5TN66hlZIACiqlerA9irDRCoitiu4KQ4dOHGOlHnW_bMnEvYPxWSe8oBw6umyiJ5NuIJpHE-DBledKFuMAYsvwltwBJ1e-VGGt7cLDIXty1DI6BCIl52JPeI42oXDb39Y9-9nydGuf3bIj_KWJsOil5RC309LsSz0zpYQUC48Clo8Bc_qZRJ1U6EGgA7ifz9fC_1HL9FNHmlfRow4Oo1Tn8sH9Tk8WagGCUVleHeCwld_a9QtBBgYi0P2uAeSy6JqsQQbGyoxXEytVPWfWr9pTpTDMCEjyxph1uD0ISPYrR84wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/28553" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jv_9RwEs85xcIJW-eszZ3vCgXKhqe93oGuZt7j7KR5ityX045LINtTfeozWI1aln_61Li5UmJlrrhhJJiSy4ctBUydI0CyeyxSMjQby5QVH7_Xq5Qe07pSRXCBsKlRSjeuW38cs-6V5d9kOEO2W1LcfjuQum8rj84TF9_1JDpSXYzOSnPSl1rF79bzgh-zIrNOocHj8XGMdPSv-Sa76Y8X4nYDfPoHAOkJNVj8MrQW0UhV_OEPr2aYfmkw14lNlXFAni7E-SbhN22JWMdsgJafiRxgTRyvYqXYq2XgkHNilGLfR1B184cdHY61bCSTin6M0cn50VTe2nS_o6EHq15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربات هوش مصنوعی فوتبال
🤖
ربات دستیار هوش مصنوعی و آنالیز مسابقات و پیشبینی بازی‌ها بر پایه AI
🔥
ویژگی های کلیدی
1- 10+ سایت‌شرطبندی بزرگ، از بازارهای آسیایی و اروپایی‌راپوشش‌میدهد. هشدارهای زمان واقعی برای تحرکات مشکوک بازار. کاهش ضریب، حرکات خط و قفل بازار را دنبال می کند.
💠
لینک عضویت کانال راهنما ربات:
https://t.me/+86B34ioXJtUwODg6
https://t.me/+86B34ioXJtUwODg6</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/28552" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28551">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV8RiPszEr3egG0PLerxJA4xNwlGZjcAMcXisPQSRTFAKe0HTy4WXsQ6ZVj0LF7W072Hy81NOKsLa7VkvqNyr6IGk4P4MkwZlF-ic8P57oiiVqzdvj0EADhOb_f0CWPS0raGrrsYQBo-axWY3eT0fzW8Iy5IzLvCXCTCDOLD9AXAYVniRp1JWHauB5ejCXBH4t7E6wN1hNi-H5-MnctRrPl6oDW-tCGD4NfRpktr7GMl9u3vVIFuVifS24-zyUEnr7S1QFMGzbzIdP4WT8LAeh4VAxGe0NG-8Et8PKwygWHJ8Zc9pMpIuzAXbJJw31lGroyJ2l2YKag03SMQ7Weeyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/28551" target="_blank">📅 01:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnYzWgb6l1NRgayCqeJGvshUbF8B2jF5jrNHHFgkSMU1hPKW0yD8VWUr2udMKcpCiVXqRQtzD93x0Jb4_ae-t7yGvEOSEONtyl1gyxITahYnHi1okJgQnQakMD4IDd8A3Iq8lNnACqoysQtHOKWW0AkyX7lquI1DR9JgFgg1GCsoaxtzuVQ-NiZQBtcpanzu4dDgJDN7f5i_NK_5Iaz0skY_XNkfi-l7yo-oXb3FRP5JdloHyZVuOlvu8eNG0VGnAMfsbExyR20C7K-6ZS6WtAHaiHaKY7IwlUHzJ9h8r4ahK1P2UKtPw0mjpTJI3YckoQ0Q8CmwL0-ynbKv68S9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شاگردان مورینیو در هفته دوم لالیگا با درخشش وهتریک امباپه چهار بر یک از سد سوسیداد گذشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/28550" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrvg8L-FW5vMMTkaCGGiullXU4TnyUMIdU6V4_2Cef_mgUkiMQ1mVxnx1muh-gxmj0dvX7rvSdxplB8jdLDEvvrBAqxpnIxR4PiuRF4g7kgTOFgtozqNJoaWw-4hsGrd8d5jKg2yY6aAo_f6GXL4s_s6g8--n1BtdYE_OkEln72K1N-n7cBCjDr2cMvkUY1Kb9YE4SdvHw-quk6YJKxqxEvzwqa0tfielkkBZ6OBkD3bLY58JdgkLoxxqU8yizqKRig9-5Yd73GNTY7cKpM9cpymDRe0HvXVT7g7z9B1T7wdpXcbLdSCTOhd3XVtsEKurW-XTIpTni5BFnEiGQMC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/28549" target="_blank">📅 00:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5bCA4nYjza_caPMVHVylEF_wPejJQOsFJ0yqC5KD8oR_weaoqdBttQJIhxBtfzNmM0OlzoZVgkH3TH8PvzTvaDmvmNMuPWJYQiF8PhmcqajZ6LqbIMjTfzYzAL-cnDAmn96E9K5nO3tSd-jOQwd5xSBrB-SeCkBoCMm02X_WipCOYJz41hvXzQDiiT1vmfBKmIL9k7qEZ3QUKpwXTM4n4d7UsqJ4s8hPCbFAeqQ9a7wv-UpOJw0CvLfXg2hNEbcQTAq5XNvkJY96yJk9WKQNLcMwNA0Hx8excura_e2mtH5e5SSrwTEGcRpXDPzqSPsXyQfaEpbbai6zBFZB3Vr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/28548" target="_blank">📅 00:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28547">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
ویدیویی‌دیگرازجشن‌فارغ‌التحصیلی دانجشویان رشته علوم ورزشی این بار دانشگاه آزاد تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/28547" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28546">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9LxRFTr4m4r7rUKMbhBKuWYbWtNVQxFo8EUNJ2YYBAnYvDaJE9MTD5TKFEj9DPvSpqzcvgyWn0LeBgEip1oZHxuPMNJ3Xkb4xSf5_LbTk7PNm4xWmqoK3QpVkkjkFV3WRz2hfysYtPoty1YXg6LMdwzBqnvC6jymMEpotBk572Idx_WrdiF7NrviGkpjpzyRy_4TBjpSyC-7a2k0VfCrHhrVVZuP3Eo4-pTfglnVpIQ5g8-CetvsJ5VkBsm9OukTtbslEL4cQ0RmdxmUiS6CcwPG-TRPMmAEf4oTDXMadUTIHiuird6E4-aNW-NCpT0Rl8XveSHpVOYreEEMBS6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌هفته‌چهارم رقابت های لیگ برتر؛ شش دیدار روز جمعه برگزار میشه، سه دیدار شنبه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/28546" target="_blank">📅 23:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP-mJs06mM00Die-srGcuRdMSil056W9BSW1X8n4XJP5tkSLBbiAxvvcnkioXvzgUsYOPTE04WROMHZDD5h37CgVIHxEA8i0fCuFGzm2XWGlmkL0atne7qeeaNlmqMv7ZmNvX5Ob8uGMhVAwH8smQLHuL_bl6mAjLLXuaqcf_YnO-7AGNV5LxY-XrDrBIjwasZxx1E8xgAXK292PIPaXMofJCwbDLv5BdgotcydY3BbX6F9x-7Fs9gl_7v_rCHzxRtwSIOwYRYh1yyquZ52jMgjhiJsGxhI8UrBVOB9m0Tt0M7KVhgdfcr9awlziB27f0Jzc7EZJFbdVs5iKybd27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌پیگیری‌های‌پرشیانا؛‌پاسخ‌فیفا به درخواست باشگاه استقلال برای‌جذب 3 بازیکن آزاد بعد از بسته شدن پنجره نقل و انتقالات تابستانی لیگ برتر منفی بوده و پنجره ابی‌ها درنیم‌فصل رسما بازخواهدشد و این باشگاه مجوز جذب بازیکنان مدنظرش رو داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/28545" target="_blank">📅 23:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🗓
#تقویم
؛ 3 سال پیش درچنین‌روزی؛ لیونل مسی تو اولین بازیش درلیگ MLS این گلو به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/28544" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myg-FReLAecaJmrpUn8EkyzppJxul4exOAS7QCZhmLP0qPWPj6BA9MfClfAN77gtqu-jVgSb2WASH-V6IxbXtpJ1VM5AdHmJQbab2JX5IKx_6YeLCx5So6VoQ3eo6NUHMOIc8qRpVmcIkVK7_Kv7p-o3VlxdwCS4ld63oEmHnWwoYY9mQmUVUlEDOIDTTt1H53sgmV1sytLyEgfNIkNlyfogbonpzPpLLS8AyQDMfS7aFt4U1F3U31t4dEvN_ZUgMRugGXHRauPVukxs6Kn37bQCpwcCSI6UulfeVcRRy0QVF1PDW9UtSp3W4q-flcrHBuQalNb55et-kEch6OyPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/28543" target="_blank">📅 22:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28542">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=gJCxRs739SZlH7xtOyjH-fhVBAlGHF4_TFTjLYQUz0hINCrKYCzFkDSHAnvsiQntEB5M1eDhx4icNzBTp1QVvYX25vECzjYy4g3Q4fjSWi0Xqlc--LVcA-zq_lNVDTKRgpk4f1jfevpTxd6cNXXfxQLVvbXNNTejIGGRHl8n4MkEv7WS30DkPAH4x4FvirZVpCcylgcDfix7aFjyfu9WXJoj_cgI4ev3QkyL4uQBtrKBuASI5htwaDZGwGB-L3xNlM7SGIXkgwrUaTg2hc7-lnxXb_pS117UXUQJsMcTILL0ByW40mPH5yNJMCkOhNtBJFH5g6Z-fNO_2ja3r-9ttQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=gJCxRs739SZlH7xtOyjH-fhVBAlGHF4_TFTjLYQUz0hINCrKYCzFkDSHAnvsiQntEB5M1eDhx4icNzBTp1QVvYX25vECzjYy4g3Q4fjSWi0Xqlc--LVcA-zq_lNVDTKRgpk4f1jfevpTxd6cNXXfxQLVvbXNNTejIGGRHl8n4MkEv7WS30DkPAH4x4FvirZVpCcylgcDfix7aFjyfu9WXJoj_cgI4ev3QkyL4uQBtrKBuASI5htwaDZGwGB-L3xNlM7SGIXkgwrUaTg2hc7-lnxXb_pS117UXUQJsMcTILL0ByW40mPH5yNJMCkOhNtBJFH5g6Z-fNO_2ja3r-9ttQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانهTRTاسپورت: بعد از جذب لوکاکو، باشگاه فنرباغچه‌بدرخواست اسماعیل کارتال سرمربی ترکیه ای خود خواستارجذب رافائل لیائو شده و قصد داره با آفر سنگین او رو از منچستریونایتد هایجک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/28542" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28541">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmRYA1eH35MvMx3mh-8NwOQGkuWmJXNEV8cZjyf2St4Y5KBPf3xNE20GN5tIUqqcV3mPldJ-ZltZvzGBegHgHrIehywDAZKhMdp3Oz9Vss51d3X8ZELjsN3UwXr1YGdYbBOBHI71_sm1khfOqmqWAAgU8k5liLGf75QqMzltTLoCEjwHstcIWD5Yip954mKt3sJFsVhL_p1qj1oSEkUVyjFxj0Gr8cTfDT7CWmZovGIqvOoUyvYcPqthQrZIPm56U5vDv_VR7XSVV0961AoMbsJpv_a-WR1wmgoN9kZTvMcQOOIvwanCybzF7mOT4Pvbu2RAv8i-9tRutWEi9z0UNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
آستون‌ویلا با پرداخت 65 میلیون یورو به چلسی نیکولاس جکسون ستاره‌سنگالی این‌تیم رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/28541" target="_blank">📅 21:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28540">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUV4cRuZb0yKpjHXQFYkfLTnKtqkgUspZPGUasg2TSPlhZfml-gPE4WYCW45Z2Bcqu4rRxIbAzHClqYhs49EfcdTyXMLDhbNB_y26mS4q_3LBCNxGzxZmgJpxn06ZYORhVJdbXV_41kHQqf3GEYkTAJHGGTobK7HOx05kpblgY8HBps4KVxczKRGiEu8wOj7RHZ5ZLlt15iM66_Ij3XMgVeCsDXkp7H5OWE5m0d86gr3Z22lEBwkpkcu6TjxTB5DkAIhFavMFYqDZtLlrXRFYyq4AC5w5pQWnZoVbqseqwZqU2tsACkZJx1e0L8K1vt34s5xVIq8e2kFIm7dL7fHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28540" target="_blank">📅 21:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28539">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l02FQgFFRp58fPQamp_-gzxzkDV_1AMtqikpMYSMUe5fE2xewN6OZyTJj3emkxEa3ROK4NX2K923wPX4yHk6kZVdLeiokP1ntYeHEXY13g6H_YgZJeZvS61IC5dPgwhRfaAKXFfFJAXE8BHcu7gonoW5RGSsetocQ7VhdAmCngYSdFlw8-m7ZOtP85YBZCEtMDwFtjFqe9li5FlO-kRU9lmLppcJ7WvB47-Kdmtf8qMGdtHb8KAerZPex04JU4JIE1QTnXXTVRgvm5bnVm8a0uT68LNnBBTTBTuDxO5PkhJ7Go5D6HPW4CJGgfe2HOyTZ1ZZJPMDCycSvRU118P4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مقایسه‌قیمت‌دیروز و امروز پلی‌استشن 5، آیفون 17 پرومکس و سامسونگ S26 اولترا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28539" target="_blank">📅 20:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28538">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmSVsPABr6lPpmg0zm_1Wz1eV8z4jkF0PDfrQReCn0zZs-NOj9h5yKiP9gRmcJCDaNryMTLT_QT5igYl1QjZyZJ5zir1Z1ZK3OYYUGvuSRcKweSIQSq8zOQuBNDpUG9xfrJFspRd8QuJ-pc1sJoD5XtwpKsywuURDxwDBJa2ZTxHYR2vAPetdM1_7dgbxv9HVfpuQsM9hFudVop7Iu3MBTdt-l6RfzAO1EwEpyNtNRUFje2ePDbREbA5oTj0H2OHqpKEHO35QP3cgJ0x-FT29UFun0CIpvF7g8Nn4w4yML52NdPo-cEPTvqndRx8Ae8PODwQKb_qN_-Shn_9GoVQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28538" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28537">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28537" target="_blank">📅 20:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28536">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28536" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28535">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_aOKQRqVglyn6qnaNtDI3BHsVFmNpcudbDpXt-NuYJYMcZ8WoLS7H09vuJMoWFAZU7PMtUrv2zaC0pwYszLAWNYMrhLQ97AaBkFW-smLvXQ7eOtKICdI7mb1y7ZXe0TUGy6hPSnKy3sW7MN4bih4dUNM_dGsQETIpUMlzYtG5c1MKDimJ6mx6zay-LIjA7elcZPYFZ-RvhmPkO8ZDF7A3oJGZmKZYS6EcpHYQwBR3msNR97LW7U8SIIde_3-dfcFqyRs85N7vXxB2llkjscCKCBdNgSgNY4KYhezf5ftcCtNGsFGzgFuvd3BDlGLP4a_GxaeXpDFzzY5HG-I56xxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ هکتور فورت ستاره جوان بارسلونا در آستانه عقد قراردادی چهار با دورتموند قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28535" target="_blank">📅 19:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28534">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28534" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28533">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4qqFdrJFsCao6fUG-Lfu0OTBtT-8f7Z-rhFuoDzUOMylIn3xxx50rGTmwcRet8jpFOTSvytx3dnuWNuE6Z2K74XYfHYzuFOCsCb3toh7Jsd7tC4MBLmVxuedo8y8f4o5Ba048nqyJLgAwZk8mG5pGYOwjdOeod6fNUUQPZZN9gU4gOuefU0iSox-4Z0FvmwdjrFI2yh0fmLFtbYCI3AG7f7pnymq1SGnT_fqqv-PaPcTa3nDH9tcWsmbDThBiIRRIcqWJEbnUNpj9FXCBJ5LnTcVXmBvhBaOr_MxfcEfzmLw97ympH4CPCeOI6HzEyQkKi4ENDN1uYlQAO-dlL3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عمق اسکواد بایرن‌مونیخ در‌فصل‌جدید رقابت‌ها؛ این فصل آخرین فصل حضور نویر خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28533" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28532">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28532" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28531">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/28531" target="_blank">📅 17:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28530">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7ABhuDYJDP1yAUhOcwFYZhbnXdFwX-GBP8oVT-imkZs_34P04gS0rHEYAHpC7l8XaO3Frer5z0X0wafH3bsdePt8pZcVlzBBo5DXYbmtTMDPiz4R3vXfoz57yWxnu17aqTIyE50JqUcbfxoQKX9M69SYEfemqeyTUVFBi5vVntSdTDFaAtiI67uMTy7qpWig0OnKV5FZlt-D9k9cjFe2h_a0X_8cvOTiyhhJw4PqlgDvHk5T7ChMdXs369enfL1X_p5NIhmp7JOb-EJyvirMtVRdYeD_8QWvqmNNhhYomCZieVndqXw6FpmZ9IpmJwMqAyLPMLCORnqelegQmi88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28530" target="_blank">📅 17:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28529">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28529" target="_blank">📅 16:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28528">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQngA9d8Hcnoc-fzENA_LtcDxjs2EPfpCAhTJEcuqUcpeHRjquKj3UiosdzuKCc9xNTupvBFnedQDTRpRiqccuPGgUndXL6qHaL3mA-k806mhI3DPIKaXz11PWBNq4_57Pdls9ueSkFLUFPyLREajAElEoKE41eugLTx_ujdF5OnWEdHBlBY8mrmzOSBVoYlyq86e_OC0rW1DrDhiqyCmQuvpA1ICJXFftgdHvL8qhFCKDuSQqMVL2QMXQA-bVfkUmEjYHKNeL0ABtkoBMbAUp2Dux_emB_LqA1v8yZ_earYBERZWaljYlpOM0WxgtqXHSHlFNFwuG7Y9rQt4dKhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌روزپیش‌گفتیم‌باشگاه‌خیبر قصد داره که ابوذر صفر زاده مدافع‌چپ‌جدید این‌تیم‌رو به شکل معاوضه با حسین ابرقویی‌به‌پرسپولیس بده که همون رسانه‌ای که خیلی‌ادعاش‌میشه که از همه چی باشگاه خبر داره تکذیب کرد و گفت اصلامدنظر مهدی تارتار نیست الان زده تارتار گفته…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28528" target="_blank">📅 16:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28527">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWibeUhgeDsjs_N9EZH8BRvHxt8K45RS0tGRoyxWJ4Fsd6e_keoW32V6P6bn_gE4rvJQ934A2ncI1a6t8b6s5cjaOFhXCRr_YmyGhf50yekiyrzmhpVxAN2UCeacsb8_knc3XYGXstfavbqjyEedPJ7M8u_xsgcAF3sf9Ckwbv_MpmBWnXE_WGYWSJBVJAAQ5OsTbjlM5OrXqKR3T-irfuzxvJ1HwpKCNp--z3FmHr9GkuurmfKE6SNZbfJ1H7mg3O2LrD3vaCv-lHEVx2ONCYCZqMIiisHM8M3jvBJyUAlFuYHktkxxk3SE6gFerqcDJVdILd3nlgeCWL3usLnmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28527" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28526">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhtl2nOFMkMnGtRB66siXdc8zamk7Cl0H-qO7A_KqJb-nPicql0CB7wWFe-TuoiD6jB0hC_DpLfMVNkK6vD6xxC-vRFcpgqhiiHQwIq4R7rg0WUItajx1p7H0jvz4dmUSEB9vhNUMwIB3iLf7ZgXIfoY-y5JdjkKIFKpX9drZM3FwEe15cyJp4DTJzqVLCWhvUQQ-0uPdQJOuEvuC5NQUL37G2yOf94LJ-hYbkHQiZucvOYbEJBSjKsiQF1uUP88p37wnhfGCF7hEEd_eUySbLNI2ReWUFMPQ1GDODQLDqvpg_y26pmfCgRDCtyFNRH-rZ6RezP6UtItSy2wflGq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل شده. زنده باد مادرید!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28526" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28525">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDMSZhXqv4csaECS0RGzk0-kVgIozwKIJnoKxU6hrKYRdWLvZ3Xv6bwJ_tXUfOxQi6gJblV9DRqI93TNnY_eKFQBgYoejANdy8Z9FC1UBjE5tzQOsZ0k7a4wmfqYA1zbSKT_I49sEL-xK-HveRevS9WFwmb4Tc45yeNazm00VsEoTvpN--Ym6IaDZy_LQibNy5hl3buPJZvowdz3nnAmfmwK3DWANqwZFLQrsHgBs9NIbepgQMNfT4mtgz0zUx_xJM5y4qtlho2m69HeVtN2JhPtky8J-Mj8yRPefL100TTEbUmYt2plvvRRplsotXLZlqewOTwhXzQfNjuCNUalZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛نیمار اندرز مدافع‌راست‌سابق لگانس که اخیرا با قراردادی 5 ساله‌به‌استقلال پیوست بعد از توافق بین دو تیم باقراردادی قرضی شس ماه به اس. خوزستان پیوست و نیم‌فصل به‌جمع‌آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28525" target="_blank">📅 15:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28524">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28524" target="_blank">📅 15:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUpdZTADbNCgdb6qvd3TD0Xwu9oawFYpA9cHZGYlMQYJsaOacqLYzcEbE2DbWd3TEXGJs6SPdscS8YW9a5iown4eV6WguVhCLqI2P6t2-aaXDKw6qN9LGx5JBlKhKkb7VNdrLagE4GCalbtR15j0SXldrOXcWUK3mAfufrrJQ7x8Cl5t2M5ehThnn-wPaT8swl0kZycG7Q-sJgRrVoj15GCIhw6aR5SchDiXmrb0m9Mk3fML5Yx3K0S53TgjhX7nsGqwV1M5WPfo2yzmtsYR3MHw1IGXu9aiPUOUnvbvtNqKB7bMqRBtQqGAbU9hYAruKu_oiPskYukUJzy9Sj66Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaHkp0q2ZpwPPIurcgvOvTUc8bEKS20fDwBBxv5HdYiA3vAgDQvX22duREQYIgzCCfL6EvXK52sonYgGRkj2KEqsvTjil5oIsKV_gv7perGKfnXVlnXpyziELnQNqS6bItXr7fbK2KprnXrL867RTYF4uv0FlFtotUEIyAJbErUkmqUlmBc_4fYRlIoREtWXkoRzBCt_yXvmQvEx1REZu21BFTQsfwTKb-e-o7k3aLGddYlDjUBAysbswGev1Pw_owzc5U1jBsVEXvQAd4nOEak2nPcW9PDiB8CP8lb8s0ZkzDB165RuMjsjOPhspGPo37gTnmRzYJMFU1OfFZCFkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28522" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28521">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOzANpcasWpaDtG07eMpwY0QQbiXkczGsNXXCEY2aHAK5rwYWyQr_BsuQYo0SGqCXS6onmPSkK-dYdktXSr_NXUSAGOaO5x8oAd9Td-Vc_mlDQ3DffjOqBUXU0WYfWz27gp8LlZuxkxcEY5FVkFkEfz8ayyqTLwATEAuVIdxAwXQEevXlgxfuknFc9QdqMMe24KoV9NdvbyjcT_if_pLA1e9DrxSYW7XBDkrhINM68yNRDVADflos6KdRAgmpRSOdLvu8H5VnK95GIX4xDzXUjh7roo6jReBzY0Lqn1punff7sw7j0_vdqktt6DV2Dj4LPFWAnWbFBsSupoq5bRfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحاشیه‌دیدارهای‌این‌هفته لیگ‌عراق؛
یه بازیکن عراقی بعدگلزنی‌واسه‌تیمش لباسشو در آورد و دویید سمت جایگاه تماشاگرا تاباهاشون خوشحالی کنه ولی هیچ تماشاگری تو جایگاه نبود، بعدشم که برگشت به زمین‌گلش ردشد و بخاطر درآوردن لباسش کارت زرد دوم هم گرفت و از زمین مسابقه هم اخراج شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28521" target="_blank">📅 14:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28520">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8oTVhY6uLsn-HVeLuHRZA61VbUTC_4I02wYP4LE8S2TqXZ-o0rNeGBDED_cI6MfIzQn7xgBmSVVDFppze2WxYI_m_bGM6WPAhEVavnBZSEK6EZIghHwN8MxlXbCsCfT6MV2Q59ir1Hw2uL-0DkcWVgnKYbcdT01IBQ37j_THUrbEHCxIyc3QNIXR5L5UxKvrNJAzOvkgB6h_gZJKOnIbdBCTvfZbFYxzHAWLQ1OKN83Kz_MJdK7OiG2kOY6wyVmvZyov8FwCfSYpc2GQyUvnsvPfLU3tuw10QxiT7fALM4JP7qAkvvFdGtwvdYmTwbn9o8u0Z1YoGIA2Y2uajkqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان ستاره 36 ساله‌فولاد از هواداران این تیم خواست که دربازی روز جمعه مقابل استقلال کل ورزشگاه فولادآرنا روپر کنند و از مدیریت باشگاه فولاد نیز خواست که بلیط فروشی رو رایگان کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28520" target="_blank">📅 14:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28519">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTqvw8m0_mpT1dSX8YNQM2lTFAy6GEHHI_f3qmyB1oJxPFpyygW0-LS_QfvmmRYeDKjCxvuYuIwrETtR71gsqMERgeoTKb-UndQVUgxAu8iQBw4U3TJn45_zmxkNaSMeHeGRijCYHjB1DZFvnOW55MKmE9GitdmUoC-FHxNsFLbNjSKbOUqLd50-WKCd7JE4Ti2WR2Xss64IW_4OeA6fKw1zmBIYbu2eUcE3aAox6pfusyDvWLdQLZ8FCkh2UC9rmk_LF1pFqcJbAx5PokLFuK5WLrK44wWeBuAaiGYBHzOAXZfQrUIftAkMqWCKGhDDFrTQJQjH0kN2XDoXfr20Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دولت دو کشور آمریکا و امارات براش ویزا صادر نکردند و مسابقات‌جهانی‌مستر المپیا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28519" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28518">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSiQ3rEwatCE1nGxHOzkYZYOvrvHjIulvArJvsreg9K24jjQUBElEICILBcx7UIXHsGQTFA79b0Si8APVvLLCG-KCrSAL6f9FcFSDo74Pu4I8Fkt8jszHGnymj5JvNj8HIiighmZNd9BbLE1v8ZodT1UJSLMsEKupIvG8Bnq1AZbDHRbWbCBXUM3SLk2pADSD6QeNeGxNg42U5dRjw_Xe0-d0IzrJhSvJeGdM-SkGaiuTC9sE0tacFgVKik_JkPKRIlr2EZXgIrG7rLEl_H-0q3UuoQh5v-50TU0DZ9Y3hA69XPFth-VoZLIKtBsJTbg9_ePCxItjtWww9Bi0syUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28518" target="_blank">📅 14:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28516">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28516" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28515">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLv0ZJL05F6gxH5HV1Cj1JGbBNB7zoRZ7lSPQejQ84vnyOqfkrn9WdlaKZTdvJxpci74qRSjHo47KTTZw0KpXwhiLWBz7C_D2J8hChAq7MbwpvfjNjew7PoVULNuHO01ikirx2GvGga2DKOGIXTn2HzdU3fDIHLiS7zMEfiVvjZNqInY7DE-1fiC3ISDvuJpgy0PdE70cik5r7FfLlheSyhJatZ5Uu8stIeZY95nwqqKC5XuxHTCyV6C9fwMraVGTvkfcZdRjG2CAegXWg_TPZZ8aiUmvNzZX3pxe7wsEmXE3aPxmYdGuLdcI_KmpU8agQJgOQLGOyphrGHeB4zpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
النصر دیروز درهفته‌سوم لیگ عربستان درحالی تونست سه امتیاز شییرین این دیدار رو بگیره که از دقیقه 12 بازی10 نفره‌شد و دو هیچ‌از حریف عقب بود اما در نهایت با درخشش مانع سه بر دو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28515" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o29H2HI29GgM0P7rfBiOaSCSZ4_eu59mklRMzmV7VZUSuO-a9fzeRXxe65rKM6GHGXu_adx-8sjeoHe5MhVMTNgeRBdtx3ue4AEcnIBquktDbwt_ytu76x-uwbZuXar7MwL2xgMwAbunrH-CYRFBbWYloRjGInZoYAPq4921QVUH0dGelkXkj5Ii7xlNkB3D85fHjVOdobCLGPIrdKwIxyrtCQxIlsfynCiCzwkBfh50o2v-0IGFDSfIW-NjzOHbQ46e9Useo_KZyOQFh9uAMiboLfQQus_JeMi9YPrD-8upjMZSa4xsMX-s7jSjQG40FnO_CtDuyRcLiPuqBsGe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28511" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi1tFuY05nnL_I9PHGOeP4dUSjMPAesYpnwCKAtA-277gnP8kSi9RduFdmlOYUgMrDDHEdTzGRgpYgQGzD6r7JOwZddRZfcV0AjXU1taA8-8Ev_nth4xLiPT5EggeKeRhOBz0s0kjx8zAC941KXL7HRKxkxs95aPs8z28xFKwa7YKr1SKme0HS5q7imcsD2JPVkWm1-be6V5xnkjC7b3d0lG6WAooy2n4LS3sU7Ttv0q19NVB3Or8C23TwkgY_7NM9bPbuiaAG9X7gGhEVesWGBXzdzC1fywbDl63iwHsmEfJHnmMdFJ647OpgYfYcl8XOBZd5CWPJlxmi1TMaVLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28510" target="_blank">📅 12:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBU5TEn6Qe80cAEkVyF7HdfldDIh7Nsms7dcdE852TI3UGUO0EsIrgttevzKOsqnibo2HlRRtHoghDNEsHtqHVVDpCxoscYF7oipaOIcK7Bvdx1aJG7uKNdijtnPAPTksvLbRmNb8mpGNnHbEWwHK1-dX5Ye5REfMkofXHiWK-ywxYSvJxF9246np2CUMRK7sT0lEkcbou38qAl1am4Buik8-QcqcoCrKXQ9DRsy9epmdAltJa3D48bO1_Y9X6P7xTGSc_wZJ57At-s7RsD0610T088d88eEped56uKJWkQAJeP6AmwYNL5wGjMQCZhy3UJiOZuH-7F665XA1qJcGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28509" target="_blank">📅 12:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGz-JuqRUVxWXWN3lSfgxxEU7ZNHo03YmTqlxUaH47Bbipgaj9FB7VFzcIR6GY71tGHUxaqXla4eStS4BL-GQ3gI6ZVLe5k-EcVMp1Vy67dvs02aE-ZiiJF5X28kdWhVMYwkHGfWCD_RdX00rtZwrfz3MsiM7XGbNlVthCGQIpRJfv1gt_5qCT-DV5RdVhG6Bu0eUBybFEqcqtwUhAE-GuBJ_4RwlThTuiD6pJPtVZjEsHOFFjY5cyAXt3IzrMocjPUsWLC4U-rObtRalxGToPX10D32tySsYIguVZ3wLL1z3C65OiPTWi1AgjA8H5Rypt7xUzvPxEfVW2-v_EcLIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار کوپه:
آدمای داخل باشگاه میگن که تو خیلی ریلکس و آروم هستی. مورینیو: عه؟ پس تو یه منبع داخل باشگاه داری. خوب شد که بهم گفتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28508" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28507">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28507" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-mMkNxyse1oouyD1PaOxJUJd24-ZBtlrE9WsQZ9dqpxehn7fVjq3ccDhkpos0LIQhHxS5NttOSFPfN5VehmxycDPJrry95dlyLCWD9-vrPvdDgOXO1YRQsWvp-M2M4ErCV77HeU6BedSElSLVD82-GAeUlokNe_HjEc_Uwf7nrcU_9VRcPRW85zsigOfEyIRkobW9MjSrXoxbJnTbBgEwTExjpKFo1jgYOO-x_9wCcilb_wTsD9_3IrzON-BTbIb8zFSuSFd_MRmSyQXDxZhr5jpT65R32nR94BjE-npNrd75MksGX30lLxurqEVFKItNJYdvJSrd2AbVfovPKYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28506" target="_blank">📅 10:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLNrgkQoDF5bQ34XVVWZnQUhl_uUFyn7tPwSQ-CK6iFvYs_NJGmiDTJ3i3SopwXofHOj38X1xWngmXSiyAQdfYItKXa7X28_N2CkwFCiey4Zbrg3TWj0vsdHYr_AOvYRgem4oljCEJlgwGo-Bi_9knlJIyYSAt8PIK7b6cCp3-mnt4CU-ZMR30Sd82faIC0AO9iRy-UYeJ3lmVFXgRdG9vbus8mMKeSapYoYGObA18V5iH0lP1VbGdv964xs47xbVSB1BtFEMt81CDhPZQ8IK8WZTKyT_Ug7-TMo_wGulnu7R8ReHGYTBLxZ-_2TPZKExdwEjwwN-ABvK59cTVPCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فکت؛درصورت‌پیروزی‌استقلال دربازی روز جمعه مقابل فولاد در اهواز؛ سهراب بختیاری زاده به تنهاسرمربی‌تاریخ‌استقلال تبدیل خواهد شد که فصل جدید لیگ برتر رو با چهار پیروزی پیاپی آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28505" target="_blank">📅 10:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtibm8SaIU1fMMxiYWx1fLP9gVkIj6D_xIitu8KRdsSMBnCilgwpcE3DtWPjcOdgCx2fKId0dxFR14wm0XW9e9GIT_r7yRR8k1CrhTHFJMcd285mM7yHKFYkozvOlx0rPqzi9eNtXpWw5sUwXkFeJ5Bnz76xxcJ1hFbbVKOuyTqsUwmMltQW46OywG2CQyrlf3L5ldy_GGXw34Rh_kDJG_a_ftyAxrBjTVVHoLDEulfgbZPExwONIE4X79mvdBqFp1VCXco0OMv3HrUzMw_k4pkStnT2sEZHbAvVzRadpoqyKCdw2FUFUoZIpCmnp4mj6u96zA9WndPW_nRU7gByQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌چهارم رقابت‌های لیگ برتر که روزهای جمعه و شنبه پیش برگزار میشوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28504" target="_blank">📅 09:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK9qoLumiXGP5QdW0mvQwrc5ySwaobZBdFdsmpc7a1AKsNtOUE3eiGYHqgq8pC1B4-MHTsAd2zTBStRqY0K9JX13PPYztX8umopQdAqlBnj9LZCOGyPpBKDl3olFpWS1CuKMdgKBUMjX-o_OboeAvCXSlVynU2m7_vEsRf6mOGBml6m1LQp3kA51kQMbWX7iEbbrJg5espz_gV35hLDsRsS9tH5JYEgMNHC6dqchJ8TemDNMmr-Yqn710ov-KNh6pW5Pnnym_nq-kdw12ixtwdR3D4fGtZE9vjB0m4ckleKrCtk7ctgaxxiINKLnbSMwiTPCSSRmUIdrYxt0KeROBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوانگی‌مطلق‌درسوپرلیگ‌بلژیک؛
رویال آنتورپ با نتیجه ۴-۱ مقابل خنک شکست خورده بود و تنها ۱۰ دقیقه تا پایان بازی باقی مانده بود، اما در اتفاقی باورنکردنی‌توانست‌بازی را برگرداند و به تساوی ۴-۴ برسد. سه گل در تنها هشت دقیقه برای‌رقم‌زدن یکی از باورنکردنی‌ترین بازگشت‌های‌فوتبال درفصل جدید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28503" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0UDle85qkdy9mCmvztQSVtuUgGKqmvlZdjJC6NlT1f7ZBfZMa8H2kRaFqovGpshuKXwiqRcCrRbkRBqjD-tj2Wlh7xyuDjRgu8RXJZIGUncLkC76Z_0OVGNtoVwGl5bXlrN_kk3CZZ25QzBky8-m9D_wg1zuVWgbnTsAsLPgj_rrCJVPQQwtmOG4zGlxLKx8JLOAOqBOfitwRaLTiC1K2UZk0ARCTdPeCbmLzQw-D4pqUrEbR48ZCwFg47IMlr0zFboK5UDTBON3W18S9aKg72TJHVX7nG8iue74ouhHvEI9DwMXm1VeJRZ8vCXz1mDix_Al04uaIpLXBWpiDj9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت‌تیم‌های‌حاضر درلیگ‌برتر فصل 1405/06
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28502" target="_blank">📅 09:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwTGlDUntWDXXype3Vsi7LegZwhKcg2RdOdT9j4TKxw6fwKQv4hK25dv1PIZ4IL1UghPAd8ZdyYwZ-xsg37v4mkUbODL3DSOudBVkiyxnuAHWi9kCiLrqrTKGOsLktZ8CHnZLm1Wo7MLLM4zTGSdLfocQtQ9OpvEPlofGRILZz87ASijhCkPsWwXxXKDgC7Pc9H44syY33aBBmf3PhzNJ490sm0dFNm83eTyqif4COVTmzU304ZzM9NCE8q-WcZcoqN5GkxWwAQRZuHSXf2S1dxOFUbWPVJzlwJezlzZUk3NtlpVlH2aoD2bCYtikeTnSz93z28E-5Cge-WFPtZNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
مارکو رویس در گفتگو با رسانه‌های آمریکایی اعلام کرده به احتمال زیاد در پایان قراردادش "خرداد ماه" از باشگاه لس‌آنجلس‌گلگسی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28501" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guSToIvWrfiJijz5OC1VCzdmP5DAnFhGHIPhspSuwx3MI1A9Ac0IRnptpgsRE-4Qklt30ABW8Luhu7SY1baPuDoGIYI6CDDpLuOgAk11HYCcXRZ447REc2dGi_lxGPYYD8D8ok1Xzu14rWTxPz6sRMQSh93dWLe6HBnV60B_NgHV2LA-2eRwOywmBLheRbz9IQCu1w2vdqNk_yiAT6xJ-hRgfvbh5wtzpvmBUoqfyTUxj9dejoZPtJBKPc224wCtuybis_7Bx-BmxzjTEGPwETZTYypd5QPWdTBiFO8YpJ4XjGhMvkmIDaBcrSScWmsD0g5Np-X-lVXwtNBFMjnF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
دومین آزمون مورینیو با نبرد کهکشانی‌ها برابر سوسیداد در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28500" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn4Cz7pCANg76ayc2R5JnC-hExskle0aHzH7cbU89hZtJUMojie3BlZ0mwySPbfFksDZ43bOjZMVb0q5eQURHNgfJdWIPgr2uI75VO-Obsv5-3z6uDXsdA0sdYy0Jc-M2Y3tyuUQv8omB67orfvfORpEPtpSr0I1uHoT-s1XyxTXhLabubbhCj5kDowB6QkYdZFlhjZX_kUcm2KR2iLn8K1mdDq8HX2Hww0kp7juu_ZGYKU1-D7svfMR1XRyuTGZTns-7FMRZgX2MVyoI2Y9QkyB_I_mn1DyCDi8lJd1xRtuGm2ifFmZJBMONrxiw_v0tZ3XEQYYUhQgae8QvSx62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
بازگشت‌دراماتیک شاگردان پوستکوگلو با درخشش ژائو فلیکس و سادیو مانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28499" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28497">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAwl_AEL3mzmy7A69V4Jl0IDWUNux1Qi_CbESZL-R2yQLV-4gdGrU5eDR7j5_me7LtX991fNBTMJdbRf_3aqwW3WDufOp1D8haCYP2iiFX5r-xozvvtxh5d611GOHNgyBq0ph3s7xU8-HWINkJou9Fz01aZzTJwC6WOSIn7uej64niWBtTxdbjYKlZBJejRgFhb2R9if0dL9XTPQC_1in-rO6SEf0wdTcWzrB1tJaG1gJSIMHU7yesY4CRM3hvjnOukYvKEgOWGVO5CV590ddZllYOrxmWNotPNFtD7tFnVFbnvYgAFCMzvufQTXfLwvLa4b0Gbf9xqFEsufLihGHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛ باشگاه آستون ویلان پیشنهاد 45 میلیون یورویی الهلال برای‌جذب اولی واتکینز ستاره خط حمله این تیم روکرده و قصد داره با 70 میلیون یورو این بازیکن رو به عربستانی‌ها بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28497" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28496">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=K3aNulprvfCvvK2Ug9g8QIqeupvgYJVwf1dbn5Kaz-5sA1qUwN1Wpb362q1HK7DTOtYsdIDGQvDXg2HL1PugmynTKKY6d7IQU14tHlptEufEYBwzFKaZtXQ2EtDB_k33YCYXpa-SBJzaJNIIVF9GtuhMGheuOv8b89WsVbZcGSzh2NbisiGHcyQ3w78jaNU3hmR6hlFyuT_14ew2prrUUihYc07WqqtpMAKglNpyNIrhaFSGU7XnIiANUSG5pMvMyzOQ-JJduz0OVB4jY7wkH9cfgDMc3BXHNxhZ46bSZueill6mmLNGQxvwxwF1NX8lPxqYsxdNmlKsPwF5H-8P7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=K3aNulprvfCvvK2Ug9g8QIqeupvgYJVwf1dbn5Kaz-5sA1qUwN1Wpb362q1HK7DTOtYsdIDGQvDXg2HL1PugmynTKKY6d7IQU14tHlptEufEYBwzFKaZtXQ2EtDB_k33YCYXpa-SBJzaJNIIVF9GtuhMGheuOv8b89WsVbZcGSzh2NbisiGHcyQ3w78jaNU3hmR6hlFyuT_14ew2prrUUihYc07WqqtpMAKglNpyNIrhaFSGU7XnIiANUSG5pMvMyzOQ-JJduz0OVB4jY7wkH9cfgDMc3BXHNxhZ46bSZueill6mmLNGQxvwxwF1NX8lPxqYsxdNmlKsPwF5H-8P7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28496" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28495">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=g3eh9-Ik0NJ1Jcgw3XSnSZAik4a0mRO2QE2tjal-oDEE77-UnHDuXsAApDK2bUAnkovH6EupwmtEyLPpcNMBjz3VX5W_n3kLaGGNWdMfJcOoS0kpbEXo_f3mYgrnMk8haophsQ55S-4v3VlvyEgqORvdKsT40E1RDRGci0tatKs6xPgMVn2mDUN97Qh8RjUmSkQ5N5gn769u7HebIVc6s0yIj-_Eqcuv3HIy0FtAJJ-XyAsC_8cIPIuK1klY6I96wYFwsqPtimK7Yhf4fRxtuxnLRmtMbTYhIrUyn4eaNBUgulOysSWwtrD24Io14pu3ZJikK6wLgqTXGCrqpBQrqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=g3eh9-Ik0NJ1Jcgw3XSnSZAik4a0mRO2QE2tjal-oDEE77-UnHDuXsAApDK2bUAnkovH6EupwmtEyLPpcNMBjz3VX5W_n3kLaGGNWdMfJcOoS0kpbEXo_f3mYgrnMk8haophsQ55S-4v3VlvyEgqORvdKsT40E1RDRGci0tatKs6xPgMVn2mDUN97Qh8RjUmSkQ5N5gn769u7HebIVc6s0yIj-_Eqcuv3HIy0FtAJJ-XyAsC_8cIPIuK1klY6I96wYFwsqPtimK7Yhf4fRxtuxnLRmtMbTYhIrUyn4eaNBUgulOysSWwtrD24Io14pu3ZJikK6wLgqTXGCrqpBQrqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال «مرد سه‌هزار چهره» به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28495" target="_blank">📅 00:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28494">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFtFjuDq29NP4WqNM7SWS4MPvHNN0OIFzSSQHZu1K3k2bDKWPYYMgEKCnxD7B3J7S8XBZGEoTyDieGgsFQMRm-mFPT0aCIBOc9tADBTLWjKb0nDeFMICiyeH6TssVTjBx0SGnRhggeFO77QF6bV2vh0X2zQz1XZhwQ3SAHTjUfLUEqDxzXIAuT-FFRIybBNgup-9ZHOs-ct2_px0J-G92E4j37orjush4Kjmz9Q_Rt0S2qHk-s4lNvRnBPCxVB0S8ZU2Cqz67baQRvf9xgtp2tyxEtTp7VcNP7B84ShWNvnJm6aKkkSsw9nJ-Ow8foFZEaUbJXbR26U1pk8F_QJZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28494" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28492">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORQuiQEhMuDYJCVpjPDw5TbcRpbcJ7Z8GvWL-K1c5jv86bW04hLNuptaG4Kz4wQrtVNP-g3ePqwaEJ-7EnxcnguYOHwxBVV_hvBp8Yn4zZa_VWAQ1XATPmigZIhSblAXibBCkanArsW_rtfNRr4bT7ghF6jmWXyZPqjR7JA-oLVCsr7mLkRp-ZMOhhi_UjAYnUKuOqlc0SShZqEi1Trv9Nyc-30j2OzyYNFjbQQW_VU6uM2FDBPuJKntGtKhEZ7SlIWED7C-JkBay5xdXgR3yELmFz9Mk0dvJrYgPQjz7hcaNw2b0DIx8cU7hzF6mDT5o71yaVhfW_buLt3Aa3aBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGEeWsuC4M7fICcU00QoSkDox6rFGkAv5HNQF9iVAgJEkOkFMY-8llTj-a5xIMveugSQNJyHlQrTFjYIDcqgakaUOpj9k4cgvNPVbsRFeVC0YdIvz80xjirmLsZ9jREmT9fIi6unaF7h7SPBxIL_pKviL0zsWW16YZPKbDIQ_PLnTAwlyrtPgTfnIn6MtB3AkG0j2cRq9DQ0Z_NzE1yyNasq3VBd1UjVdY9dkaiYiAsi_U5Li0SfAPxR-qoXBB1QJ5KLyvVoUBVsY0iDLAJdYrICeSpxxAgZV9NXvlBpfOokdaHuTA4Ie38dnh7ZNS9rTqJj8I9kxS36d3g8XCpzNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28492" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28491">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1hYQodo5rM-4W5lHxuMq-yW9Pa8Pc6wOjVu1ZdXb0G_Xb3-IRYEG8QNicmfcA1ZirsPHJjWzY8YQLDFtQFspVDAn1jaVWr6twCheZ9yvfrv8JmEckTZeV-bqEV_h9EEhdLphl6pW_KpsiVIOrD3zNf5NSuwu0r5jcqb-IAAUXcebD8b9Hzio5P0XbWC-Lj8ioqy102wSeHtQGZ8cpRe-6wY_ZBwrBCAdLWV7fnR-_xQdxNRMHlIyO8l4szFr51_FOtq_cbaCDMZ7SfkfrkrBHRuluSOITLByKrGpVzBFFToQT8RidA5DBZ7VGaqBDRIs6RN3fpSH9dRQAgDXc6BVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مصدومیت اوستون اورونوف از ناحیه‌قدیمی همسترینگ بوده که بارها در این ناحیه مصدوم شده. فردا از او MRI گرفته خواهد شد و میزان دوری از او از میادین مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28491" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28490">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28490" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28489" target="_blank">📅 23:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4elalfaGQcanB09lkM6OfuAVJU8fPcQ3H2oFzY6ZpUw39ZJzqyGg1HB6Pk-iTaK00ZBegqg4x0hvVoEsMIjFA2nORKBCS2chbARLYkZrrZIUR0eS-Zhbd2JLRkvTLGjSXwB1lSCi2tT70m9eXXi5Uln3VzKWcB0QNwP1PqqXCYhQmOMT43AwQVZoe9p4XJkGm8zoS6IuBRVmoS71MYqWFQkwTRxXxdKB-NDWtGQKCM6lZ7Du4j-s9cfw54a9fz_jM3o38PV2m_ta6JP6a6tvezc02tfnvn4Qy8n0RcTA2rBIV-6Nm4BW6VjHAs9awbamCo_eY7puBDLGT4j1pr8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
برونو فرناندز ستاره پرتغالی منچستریونایتد بعنوان‌بهترین‌بازیکن‌فصل گذشته لیگ جزیره انتخاب شد و جایزه ارزشمند خود را نیز دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28488" target="_blank">📅 23:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCxOTr-J6QlxS6EwjUoAoKdiJJ7bvfwTHuCQ9CZLU41sSBxLbCX6v1-e4kAWO-y9taqnRdJ3Mr0qtpZCp6hKjMNH3JkVMLy-LhMZFZmN6drT4IdGrd3VrJ2sI6-bKqfgxM4NULJsH1-i-ckuJtDbutJDfOlhAWivvDJ3SmxtAZHFTMZSD9A2Gg5xJFDAN518GNwGbIi7S6wDEMIF19tUCnWqJsO1q4aUzl34cLB1UIAfzTEoSk1T0PRi_-cqDecBgYe4mub8OXGdtbjr5CCewWDfl6UdknJKPQC4RCWxLpbC0FZhHbGd3lA4wgrHhWYEfLiIvGAkagJl7ni7V5xNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ترکیب‌تیم‌منتخب فوق‌ستاره‌هایی که فوتبالشون رو ازباشگاه‌پرتغالی‌اسپورتینگ لیسبون آغاز کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28487" target="_blank">📅 22:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28486">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28486" target="_blank">📅 22:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIdJA2AGPIUXweqnL64V_WJqgHGoeM5Dvcq9PF8bt074XakIquB37ovBW5OeWOJnIcHkGwhD3hYSC5qr_dr2if0EwW8J2PiYkVhZBYzmyZs6HFcf9vrOcvYDLgNN-KrrWjOIRSGhvA9DEIQ3gr8Im4-6MN4lkTq2ByCUV7XRWQeE1MRCvHFjjfwvItyqYv2LSs08Lt1H9tls9hEXp9n-PP_WipiMfg-A_mOxjZHQCi00eUDJJEhwYeABFOYJ_JDoSid66hRgH1o2jjZGmXp6MNzipDRtk_3QgSpzQSVgl0W2w_zw4JoZYINNyvZ3vBOhgCWI54r3xFbpJ4AQEgBIvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ انزو فرناندز ستاره25ساله باشگاه چلسی در یکقدمی پیوستن به منچسترسیتی فاصله داره. آلونسو گفته دل انزو باموندن درچلسی نیست پس بفروشید و 140 میلیون‌یورو درآمدزایی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28485" target="_blank">📅 21:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boe6Mj7ihBv3S0WPxY_orL8YWapKbGS-qXKGK9k37gM416Hm_gT8-qS7BndmDHawtspFe_UFlGKV2pCGEaHhme8KzR-4lCcL3WYHs1VJtV-9FhzPRHUu3aChMrgOxezHfu-Zf-5F6GHV14p-44O7kADZZ0ifFfq2LlbkzJC5E0CA7iuuhEM5-pUueUecyEzRDD124mDfypospJGr865WfAtvdvKd4aBV88mIOZsMkmAde484MOtXqlIBE1chHiLv0kqWavC_F3RkdmbbtAscQQgZBCjf348BOpmquFSgP9Qbpm0Wlk1uhnrnW1qc3WZuYIeESFRILTZig5fk6IeZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌میلان باموافقت‌روبن‌آموریم؛
کریستوفر انکونکو ستاره‌فرانسوی‌خود رو با قراردادی قرضی تا پایان‌فصل به لایپزیگ‌آلمان داد. انکونکو از ستاره‌های فصل‌گذشته روسونری بود که روبن‌آموریم نخواست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28484" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGA0QBXMXgsMPc2MYQENsqqhlYQsTmz4cRCEkA_blHG9v2VOdyU-zbWgyXMREfWMKnmtCeZmc7zw-IHZrf5fj-f9iy9r8ZoWjCG_8MJ8SaGe6SiFqqsdd8qoJCpzedMCgLZIjTEONt7GY4kyNig1aOao0mE4VJ5sUfMigiIdxVgboQqfC-CMSJcg5RlMm4yjVkx__kIczwQ3n-mbeKxIQvg0nhaHraJRv1574qZlU3bJTRNvv2bmjDUIShfB8D_7BYTpofGECA8qXSt-Zcq8ezOHxkVIRXYVBbq7m7fKmACaL-aoG6tmpk0Sh9iMyYYQKElRplnD4eOBoItS56z34g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28483" target="_blank">📅 21:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nvj3L_7ixxmFBRR-hApLenosCg7G1Kv6IBHqV9n8ABAYg_dKGsL8ePlcJg4jlsyqous3TWcsYrm3iKY_gZsNFnhYnIXgiIXk0nWpZ8qwKrp6ZHBt3b8WiuBFNyFmtF1eTzwXM1uIz0eDoO07onQHEEz7S9HY3Cls_Lv_MxmVqmJKTc43oT2wHp1ueJtVHpJ_4XsfSnHTTgOamydJJDwuvHPYt0vlQoEOf6GakrjiuIHnetMSnv09EOVspCjLsuNgJi79HrBg4FdpmSPT1dLg-zpoeYq4GQrT1e8rpKrv20MFy_ckuHhKsLkOnx1Z3AvuuXmQvfEXk31FDU5xszLdzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛
با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28482" target="_blank">📅 20:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBCm4I2ivNLVj6NovLj1pqC7daOWwRmZPM5ZXfhcN4z72aTbFvYtoojE5XL7q8P8cA3ZSH4Qsze4WBSQwOsoHsK1ddb6cKCWpjFnzpXY8yRaha3s9joASbBK2t4HM58ZYIMoBPhkI-O6UWoirqkqhTTex-Co6JMCG-dZA-0_SX4RIlyihb3CUs3wsqqhX7flwEpNenSt_lYbCtBXbd8Ze2stX9eDRkrltpYOrUbRo-65SjryrqaU5WH0HbmWHHUmxeRhAYh7R8EtrUWUqnOWmh4vsoLRI6CYFQyOkAxc1vSVwiU3NuSe923M0mdT_gCGIdohVVCwbVOqd1eCEquMQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28481" target="_blank">📅 20:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28479">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQ7hEYuOPtWzP9kk1RGus6t3aVF8ysVFJ0tRZPbgIDwuePbBmb6tPhmD0NTn7PmvfGO_JQkDq4Ti4yEsvYQA7NAKAyfxijQ2j_Jw_FgcplZRt9yykgP_E0e7gAemezXWfJ8LblT8gIHahWVS-zpKZ7EC3tY5HFNgsreH5jnRrfEBc1DJxmSq-8IMmjOHh_6q4LylrEy22xTdinUB54dfszKuLq5byYS7uddBrQcMLKwrGH7io7v314YJ2FThTjylwPhDgwPCWt1FSkmnaCFcZnO1Afkcpr8s3dL3nUgnf_lJIBwm_WvTTVcH5KQZiBIrvQS6wAAYpBOOm-EkWbkhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUvGZ3X9tHKR1xisE_HkbJXiVJ-GsCEh5jHIst3Apl6AWhYT4M0Zmhq4HDxiLcfyvBRKzBulg7bo4oZ0WdXx9O7p1UiDFsD06JLSZN7mqm3y-wf0vUMi8aqEKlwSwXUSpMSa8YauKDPWjhlrPL-RJgiZHqa08PDNcf22GmxP7lnEdZGeBM9XhlrUVdDNEKDQ9rI8AWhtPTizAggm1OnmsIBkj6If8DKN8MPmweQ29klcM9WNpAZjRpsRWtNJSkkbNxtUZlC6DGi-loLZGM5lrMiDRHspDilJ6-K5KA4Wi-_5L8o6C8owiryAnJI_iXfjf8bvIH_0xfndwJbkZhJu7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28479" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28478">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYDtgabeiQV9QJneMAt92FMbQFMG8vFUMzEbbktuKjo7wQLqBxJ_EdpbmeIMrOoeIbch9E6UwlyzEfECzn-blxRd9nbE6U30eTcj_uekI_Q4QS9VaTYrDvpES6STTLxz4TNO9m79Hm1YbholLGY2xxwWfTki4UyB0Ru0T3H-ahH-PVR1c5G2_9zBw-zbJBNiI-g3tVSO46FQznQl7b-MTJWlEufVcL2SjwMqC3opFqcWxMDhgLjss88Uh2PbvVYsZavtYJk4Hsjgas9mMXo63ulLSs9deU7kQs3DzUptGT-F8OrkCzaOGNIYVQh7CvNxdMcNOxPnBtrQVdUHEjmYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ هفت روز تا پایان نقل و انتقالات باقی مانده و هنوزسرنوشت بازیکنانی مثل بارکولا، آلوارز، انزو، مینته، امبایه، گاکپو و پست مهاجم نوک برای بارسلونا و وینگر برای لیورپول مشخص نشده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28478" target="_blank">📅 19:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4Z3ayJYh0ffgKxUMpx1yJjmG23WNTVBvtju2aEDR-NcIGIUEG2Ti40hKdEM4OQwsHvhqvC6rZKBtuz2b1Sa8Ou0CJgCiurB1dIoTT2jmnPZbIk6y2WcIfnbhZQCBtKVmjav-shZQ9DiYiEsUdlMGqwib1MrUMJHh8LNSICSAR8j7VLUJss4vefOcfjvHa8wm5nCX1PaJvKwiRvfq2Guru6XmsbpJjgIA-0z-6uZkyfQLqWc47RVS6kG9Eys6v2jouWTK7w1zRKJtKCNsNeGU48J-uVW4FfY1mDDr8iCC4X94UmRH1Cw8vR8FZ6RKFCVNgrN4W8GC7BQ0txaxYfHzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28477" target="_blank">📅 19:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0h2kGnuZxp-m23DrKnE6FaXGWooNa39-HOwAouCkYJz13BaFLVmMXzNXfcP_N1NmySGvUS9N1fV5unoQ2NM6q1akdNz9-XVoIp_k4B-fXLlbRnBKGOjNleGBMUJRwA_4sKTIwIM8poEaFePoQr7gSMxN4GGqlNlBkUpJbFbYGMqgdUlnpuwhOi8tTtSLa4g8qH5DfCLYi7nDTTKLDXsBfXV-NAbyLfrFyFECFbPVFn3trc_zOrCEtDfrAnsjlZnWU6d9S5L0q8qFpi0rWPZi_sctMsYLDXgIlgextrNTcD7s_B6BYnbKTwmOuJHlS6LP5dPmv9bRwMJPhSHbldfig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28476" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
قیمت‌موادخوراکی‌درتنها 5 سال‌اخیر رو مقایسه میکنی آدم‌کرک‌وپرش‌میریزه. کسی ندونه فکر میکنه 50 سال‌گذشته و این‌قیمتا تغییرکرده. قیمت خودرو هم که بماند همین امروز روهرماشینی 50 رفت بالا.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28475" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbtxJNW2e10ySis32jZzHCggeyDQv3Q-wUHYvqMmT4aWGuexkWiwLM-vgDKCIPmySJrkT_ZxSNwZ2XRDTcxLfFa2cX0l2TvpnaXDq9WnuaaLO1e9L1MNLdzwrh0AVxN2Yv8Qz-XFB0uXDDeWu_GOubueVxuql_TSoDgbqcXFSylJ7iAP2OpTnTOOVwS9ZxzNcNPBSWZRRv_H0YQkU7yIic3z_LlZrtjnyFeKXKg35QC_TCkdbOcjjn31iDh6PdahIptjpTo67-oHjmQzzB1YBohTYs5GIQhGPCspw9XMpvYobU7GobdyxlZhBXd0GcCUi9DriwyNJrJV0kkHM-ZAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2017 در چنین روزی؛
بارسا باپرداخت 145M€ به بورسیا دورتموند عثمان دمبله ستاره جوان‌فرانسوی این‌باشگاه رو به خدمت گرفت.
عملکرد دمبله دربارسا
: 185 بازی، 40 گلزده، 6 پاس گل، 141 بازی رو به دلیل مصدومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28474" target="_blank">📅 17:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wpf3ZeJWzA-9jEH-qKZBk-5jIdViX-O_GcH7EkIZ2mptgTZ5tANBUHoaPH6z7C7NAclewz79skDJeupQNr4_z8TEJdzV5KjMJXJpDQVQHs3uQ1Nv6cAIlmBA2gHuaEqO8d3_FRYljj4kOd8g7I3WtAEGnVSOYtC-tV2tL9pKlMwdtU9cPvet71oTSs24Gx7bcidGadNq7Fk9Mtbg5EnttS_vZQrWP-hDXl005Thfbey5rB1YEBu9XgC9oMoreyPVkh4ac89vbOLbp-Ok_jKxhi1wMvPBrnazywXMj4uVo96kwYF6uwuWobTSUmAMky3_lYS0hnSkbop6LNefnBMrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28473" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecKRnXrJzU_iGD7TpgQPqiZLEY2rGrR6IuXpLxGT4alxuTg-xEb92KMNXeDWB3_Lkkkni3gbf00tozuU7CJWrkkMSi4NCBhSsGwKpx0Qm2U1hnYzmHLcR4IMKm69CMx1wzR1OipE3qRgaucaP7cyumjgJ2wPfZJk26iW6qHaHDNrWcTxtjOZEWmfH3I_LlDLOcbnPhwSIKUUrNwMOwfaD6-GgPpfSyK50-yhZiiEpC2wUHcvxDem1HR5dvDXSkqdlp7eP_3dTThAlW02KylZKt_95frmzxvhce1ItR9cnrOBunrdIrdb3QaHpIb5ajtNVudUGT-h8IoDW2VsY1fADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ترکیب‌احتمالی تیم‌اینترمیامی درفصل جاری درصورت پیوستن‌پل‌پوگبا و آنخل دیماریا به‌این تیم؛ دیویدبکهام‌مذاکرات‌خودرا بااین دوستاره‌فرانسوی و آرژانتینی‌آغازکرده تا درصورت توافق‌نهایی باهاشون قراردادی دو ساله تا سال 2028 امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28472" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28470">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Koa9UwQDWyV2zlv9Ot0zug-4XxSgHRl1z_gKO3c7UFrOdluq6ulesVFVyzn8TdGjSp0fYWJ3nLTOtsTtVsSYpB-MqTONYmofVMaMiRk5zq4ubr7zgD2ix7_JkIlAVuOCn8ZUdgmLO_pF1wH1PxEgYo21Focbk6lCr70B2nXm58tA4yfzawGVOkjxc7AYpbpvFHYxiWBnrufujcUHEBdPOO5L-RY7Gd3eKUfzTAhHo_XsFSbVMCd7cdkqHCJbwJ8o7vlAsWIrdWBkqIB9v2mDmvBqptLxfZZX_mxWDwy7uBIPYU-7J6xIkRES5sWhL39RDuBXW9nKdoC6JUTHGkirAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28470" target="_blank">📅 16:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28468">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=ed4JSZaadNZFt-Wo24ZAfwsr5ss2qVMMdDaP9NEwXfe6RSesDgbwX55Z1JmUdc_fR0kvXWAEqbFsZBDuF9um3qRSCpXHI6ujZ5NvVWZtelblrqN0SK5lKeVM2UJWrDnSdIgkg6CRRGscjGtDliUNoaely8dzBexoylxRewvyAWFL1yO5S-f34yTd__zlXClZhwDdNDpYUmKzIc2dP6uRihQqPNOsLqB5H2TQUxQxJD0g5bsuZvtH7c94CAxIEhy38U6Gej3qZLEva-mxvEmbef_U61DACWZ_7k7NcTzM3zaB7uFJ00uhPM_TYlCDIn5mIoOJnmqrdiu2K9ZtT-Tlaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=ed4JSZaadNZFt-Wo24ZAfwsr5ss2qVMMdDaP9NEwXfe6RSesDgbwX55Z1JmUdc_fR0kvXWAEqbFsZBDuF9um3qRSCpXHI6ujZ5NvVWZtelblrqN0SK5lKeVM2UJWrDnSdIgkg6CRRGscjGtDliUNoaely8dzBexoylxRewvyAWFL1yO5S-f34yTd__zlXClZhwDdNDpYUmKzIc2dP6uRihQqPNOsLqB5H2TQUxQxJD0g5bsuZvtH7c94CAxIEhy38U6Gej3qZLEva-mxvEmbef_U61DACWZ_7k7NcTzM3zaB7uFJ00uhPM_TYlCDIn5mIoOJnmqrdiu2K9ZtT-Tlaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28468" target="_blank">📅 16:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28467">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rokLwuEXuhsn91QScF9bTOoTLRh29kBNMPYM--y3oHP2Rg10Qr-W9CI0LlVKS7jZ6XVkIxkYCplJgEcPcX59kRpUTuMueTxPgk_c6NbM1RZFbTRd7mO1YEmJnL-J-7djvedBdvbhaWSZHduDYBiCw_HUVy1N40MGxO7EjbLnd3qDG9oaiiCYXxA1Rj2xLUKPF7suJrpkF7qRKoRTrpjNGxTw58b4mblM-BJ79znq0WcNXRakmnjYVjkIyQ3CruMin_iRceK7ybIKgB-KyNDienTedMHRjF2xyMRU_6JqlSzsJ78SqY8c_ZSP88MxWyJntU7xCut3m9LgjdUnXkmd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قانون 90 به 10 در دربی بالاخره اجرا خواهد شد؟! بااعلام‌رسمی‌سخنگوی‌سازمان لیگ، طبق قانون باتوجه به میزبانی‌استقلال در دربی 107ام 90 درصد ظرفیت ورزشگاه در اختیار هواداران این باشگاهه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28467" target="_blank">📅 16:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28466">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAnlQSH7AKlkTErST9JExecCOPXbooMMJjUP3A_rd85IpSR-nYA12FIqHNWlaKBf4wuzFUnW_fCKi5cDzXO5xWvB8WE9fdIwJG2uxkTBEJEW4ubaHNqIcukbbjWjlSHnkAU_5PL_OlIVy3gHmmPoBREPd5VCxc3NXbDQOj81ZF7dqynnoplCRqxXKGUWaba7U6_ZZIxMV66Zs0jdoeQBcI07d_xWTCUvANEjlBhHNRfTg-_aJG5HTiarzVCS3K0d7knVKuqzT28_BuRqm9smw5_g5_Yrg-g-YLLcbk9UAlvKzKw7BVv_BWNIVPu9ZEOqjdw5_T4q0FcXHnCnlCOu3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عارف‌غلامی مدافع‌میانی‌استقلال با قراردادی یه ساله به ارزش 8 میلیارد تومان به چادرملو پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28466" target="_blank">📅 14:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28465">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEUJ3rTQ0dz0WtBVot4Z9ya9JRdkAXoKAKHLsQK8qWiyzdLPcutkaaoGT8pcZL5coGu4mGydQ5t-0VhZF3-TKbCyegmxW4DYY6Bg0F6gBJXQd2w2UTJiY-yP6quDFa46i3RE3F4lidCFy3JG-7FBQedwoROEqMulO2GE_NRZotiXBz1gG71vi2IUdGrKbLprcnFe4liMp0hyKv0BD1qlnZV6eDwaweSfZmdesVWJByWu59Wp83Ue_AkfzcYsFpCOC1Aio7MwGafjcSMuh3IxUvA6SMUtzJSfN8_gM-IRnTdI36EZwPBebalMhaHQXbIPDI14KzqvmAH-AOymGcW6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28465" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP2J6JtxvVfKmqLgp4GD9dExcegUYbBIT4w98OSFLXc5PrCTJ1HXgu39dWPDHWu5rMMz9ak_EZnkbmsrMmU2xgzZT6Ti7UajL6XLaa_QyS0MC_vKzIK3dcWHLdoM0hKX78yd9L9edag4ub7oVoL2l5uQNK9ly1LYflioe7jOztcNFCLNBRzHihsfV7bZV1ENnMpA291xnzuNbSe0Y8iNrv5ofIzVEUfeJ0Tqa02iybM4hZvVJ3kmHoH_MYF_qe_Hg4PndJd-Ery_oCPoWrzDhhm2KcS1C6n-assP0ZlKCs9WOOR2-e_efgx5UrzvEDhc-YN6-33r7llTvrGeJCdwMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28464" target="_blank">📅 13:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP5XClXlCqjuLHzfTA2V1BcUhPjBOe3GYrIAnqnpbEoBathCQw0jwg5dB5gfi_CbT87dOm18xXsetu4jL1qi8WO2Z0VWuD115viz-7SMXGZjHFSw5qa83YlHENNBgd9HiMh76VfyjNIVyD4IoAMKIu5W2JfffnkIHgVnud7XAzLItJP7YGaysxLSeARv3vjdXSD71_pAMtxBcqV75QkeLrwQgtTADyAPsWqH107MWsQs78r7grj515CqkIvkskK6PWosJ91K5_i2QUIWVFOhwvdaWxUED3Qf6TlqITlnPjKhNnsUXbh_KxjNGYqwCnUB_ks5QhZUqoK45JUMEmRYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توورژن‌آمریکایی‌فصل‌جدید عشق ابدی یک دختر ایرانی رو دعوت کردن که همه پسرها عاشقش شدن؛ اینم رفت همشون رو به ترتیب بغل و بوس کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28463" target="_blank">📅 13:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28462">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=vVnJZV13e3wju3yE3E_sOihs0sLD85oZTkVg9gnd60x8Sac02ww0vfTRPp1Tgu5zK5ZXJk4D2Tz-upWxgbdPOLGrVFbRQpBv6iGRzdDWT-KH8OwPdTvfQ5znzdeclD4CQHZkjflKII2ySqVbXVh0Malob5ztKKDkIzmYsUhu8FAlJLPhJGeQge-7pGf-dn6P--v0o2tHrZbNhV6wJUYDXo0KuJLTDKIQxpPkSGf_MbD79glIQGZoApVYwRjWRvnnT_sL_S_luDwMXS3X6CKOKZXhKt4W5Br4_TZSBzP9HqvjybhMwfMLC-1HkbG-XDQ1Tfcj-3HN4dQECDuk3aTfAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=vVnJZV13e3wju3yE3E_sOihs0sLD85oZTkVg9gnd60x8Sac02ww0vfTRPp1Tgu5zK5ZXJk4D2Tz-upWxgbdPOLGrVFbRQpBv6iGRzdDWT-KH8OwPdTvfQ5znzdeclD4CQHZkjflKII2ySqVbXVh0Malob5ztKKDkIzmYsUhu8FAlJLPhJGeQge-7pGf-dn6P--v0o2tHrZbNhV6wJUYDXo0KuJLTDKIQxpPkSGf_MbD79glIQGZoApVYwRjWRvnnT_sL_S_luDwMXS3X6CKOKZXhKt4W5Br4_TZSBzP9HqvjybhMwfMLC-1HkbG-XDQ1Tfcj-3HN4dQECDuk3aTfAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28462" target="_blank">📅 13:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28461">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoTlYjAr2qRv4GEMzKIIx1pZ1ma56OWGVt9Peqj8eK1Smuv4odbtcccX3W3hSfLe97lJMwGJkGNgSByxmE49Fc_yhkLbBOTbeZfMJguOZuByLkwGTtrsrThv1FduMy0s8acSvw8nhaHhX_6DSti2bs4-Xg-F19Zd4WzoALsGWVIE5rGsvxaNC9_WkGwCKqiq59SdBzkFfJTgzwGV1rzTRLxtZgM3ubOkm6EZ3fYUIH-U_3SfS6JcUzO3Hw4ToZEVaUbA9V36dmW22kxhf_2KXjmJEibng7HgON-Egg2FDV38jkimk25J9reHol6GYIBE1oyNpx0mFqQsGSXzOkSsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28461" target="_blank">📅 13:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tTWOa3leJVtx0eb-GLp_uBlRu0_K9sUGdqn57B0eM8XVSPCQht013LM2SJ1VCe433ub8ZL1f5YQjd_sm8H1w1aMxMQjtsjVL0Yjm7dX7anGOAJDwXy-SVw6TmKYrECRkQl0hghKfrDHn5KpPgByljsMSAfccwTE3fphKQHU55Z7y6-Z74dmT7OVRev78AYTHGRDwBkyopqEJhabrmZm9xkwahtjzf-y50zsZ6Lg0o5TYvKSJEYvo-XZfDkYcYMHEvfsYP48fM6HmILB8pggaitms7bTQUb68xujb_bk_wKjeN_TWfIHKAujjqS3HnYK1cVdSKXnWx_k91x7bLmIAQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uf0rUupHaWtcJ29Kbv4ylZ8z_n4e-iH5ZrVitB-wj4AlGqZ3XB8-MSzqAfShGXZt7FOwmrYDsqDvuLhUSXyxGwfsUsjeGfylj-Q_S6z8lQqVe2jTsAYO9f00kfCgdH-qOYnjOMKD9m342HLCVvshzAxF8znvISzwlNdvjaufRBRlXTbVKJgG_Dk7afqlxHKHSnHnRKsCYlhTAqL-VXwmmHq4rSwXEawCQUvqlHWyE331PFV2KmauMHuof7-FRUjUWeR6BJSoiQwNLlBItw0LpkEMuthyix4NFxOS5tEKzbBeVP7-pxAxnZrUIFj3KqUdFpNyV6lr-CqEt6XruS8XaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
از مربیان آکادمی لاماسیا؛
که حسابی به بازیکنان این آکادمی رسیدگی میکنند تا ستاره هایی بزرگ به تیم بزرگسالان تحویل بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28459" target="_blank">📅 12:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28458">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=Em17mCWmXgjlql9TZwzwBPY1hC5pAmPdZfFUs11nLfz-QL3mL2Hq-8IXLUNDOfapT_UEOAlS8oiQeGhmrkHQBjc4nA-hA0fMcksAmVx7Zwq-kyE11fTPi4KjVCdSG6Z3I-ELclS4eVMBHOnOcTdqTgWVrXCh8D4r77ajbW_R1APWv-_ps3mPO1c3-4PjKTWvpGGEu2v7_cohpUYQsnAsJh29q__IAW8yXgfLIsCudYODAIm3h1YUxG8R03OUCQFS_WGOJMSDv_3t3w_RlNe6CwrrZI3P2Tyo1mOHS7VBgUT415e39ioiZWkWBdB4JuAD3ksDJDbaTRI10H9dS_g1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=Em17mCWmXgjlql9TZwzwBPY1hC5pAmPdZfFUs11nLfz-QL3mL2Hq-8IXLUNDOfapT_UEOAlS8oiQeGhmrkHQBjc4nA-hA0fMcksAmVx7Zwq-kyE11fTPi4KjVCdSG6Z3I-ELclS4eVMBHOnOcTdqTgWVrXCh8D4r77ajbW_R1APWv-_ps3mPO1c3-4PjKTWvpGGEu2v7_cohpUYQsnAsJh29q__IAW8yXgfLIsCudYODAIm3h1YUxG8R03OUCQFS_WGOJMSDv_3t3w_RlNe6CwrrZI3P2Tyo1mOHS7VBgUT415e39ioiZWkWBdB4JuAD3ksDJDbaTRI10H9dS_g1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال:
باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28458" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28457">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbCEqdsU1t1cPSAH7XOxPXrMI8SUsdpH_DgAWCaDOngza3oEJVz5utxancRkXtnE9Ip8LTjraSzmkPJMaInNj1BScZkGrlBP6BrMIi_L-u_5Vp2VCLhOhPESRlhQfdRJXzxMRE4m-qho9j8S5uRzrqW-Jl-BV3aB5C7HZYkgO39zEHhLRxB-AroSv294eHOiI9I5DZjw51KsJUf5C_6XafxUBJq09v__ttFGxIj24knQ9MCOD-iVjwVTJPA_yQqHoLTRgjApRtjIdf_uNap4cTxA9Q8p35Jpp1QfKEG_ea0X5biMmb5hvfuSFnu3rDsKUgItaVZRHlY5jz-l_bNhaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام خوزه فلیکس دیاز خبرنگار نزدیک به پرز؛
اوسکار ناسی مدافع میانی 21 ساله گرانادا با عقد قراردادی پنج ساله به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28457" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28456">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u56xzC9nPVk9dbbkVfOkcxfsjF6OX_DCdqbve0AAXLnDyp9qWgPiDWzes-x1uJdnngrgTjpsV2n5eMrUXfteP_3Tx9TqAyjFx8YQwId3vfMp-kl2qlJvsdE8p9yyQZhnmZ83VXAtG_Pz_167MewvocqcJH59h-_FpZsZY9vu27LuXp4y_StSdyEyjYs-Eg--7UPtibRuwFSi8DrE4f8EXEreIz1FFdHb3OafC9JcPRsfWIP02ZGrmWVXEo96oK5jj3dobWxAN7ZXT36Rgz0l3_61cxpr9FU4cKWjySYT5w4jxBvoujPPEUoINLGo_xTorj0BEshR5xQVEi50t9-QNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی‌از حرکات‌خفن‌و‌فوق‌العاده برای در آوردن سیکس پک‌های شکم درکناریک‌رژیم درست؛ تو‌ کانال دوم تمرینات‌بیشتری گذاشتیم اونجا هم جوین شید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28456" target="_blank">📅 11:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28455">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfRraMQntNGpA9vfHHFpvOye9XE4ZbgWKKXDe9gor_sw7nm0U4sn_SSIJh0voe7l_MpkgF7wSpIreMhN3-lWJt3UyuwiuX3vwQGkzUbCdMObeRrcF7YXsPvzk3WGdvo06bFYRqL8IWboPeYGOs7O7F-nTjbjBbb_rRJjn-KzGZAfkjlKA4MzJQbsvBUjqTKdYWWMp2wjOTDogIr-7UrZQ-EXeWP6Lqhn7tWrq3s-JqISFOyfOLz-2ttwrl7h1ZkcmFoWfh8DSK-jnXPc2F_RZFMuaP7EmJpfJ9jPEqCvySWyFH87vtpeNJgEIxcoJsKzo3K8XoY4OyqruZeykBPgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمیدرضاگرشاسبی‌مدیرعامل تیم فولاد: باشگاه استقلال یوسف مزرعه رو میخواست و مذاکراتی هم بین دو باشگاه انجام‌شد اما کوتاهی باشگاه تهرانی در پرداخت رضایت‌نامه و تاکید آقای حمید مطهری برای ماندن مزرعه باعث شد که این انتقال انجام نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28455" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28454">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBZgaVgdVX-Gq7sN4qXEGDI22khW8IMn6XrkIahK0xqzD6Aftw6b469cCfbqPO5I2l_ajNQoP1POX61KXnEmjQU635y2ruV2DCB_gg1jwxqMfcC90-Hz42QwyQHKLC2NtpAQgNj6XivmQuJmT0x5w9mWRyll1J5v_-yuGNnjaKTJr0lws_s3I7gLkIut7x_rJTWjFCTpXaFqOhCyaEuPFxUxYHtrp4IskS2qh1UFENleCIp69zU-Ce8V8iOCGDRwi_LhXMUFSqNjg-rtE-_9gRmjEBVEtlUjm1x3NIykD62XRcb0Vjvbtlxu0wammclCdxBlU4-Anue4hUJR7AXnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28454" target="_blank">📅 11:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28453">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwzRjtB7pXljfO0hDd1oOp5iIq5fAA6BT9w_mVC7tg640XCdBTTYTLn7jTfLKY_dra47icoFFfozYFNvXHIN6wcEtMigbXnhh-QOOOMVf9pUzeBIXwrGUuq_SfS6L2li94-XopdcdGANKZ7Rjt72r_Mf--O8ENCNtU4qhp-aZMrIF4BFiyJQDRJ4yJ-T4BDfZK1e4cWVZ2Eh_chsQVANe5T1_n9Zps89qnY49D6Rohc4K8CGSz1VoqawzKn7uaYMXEhnTQnEuG7M567BIx1idBkcV3WbCv-mnN9O01he8eXgQncV3dIOKETSGR6cua4hDWOglpkVa42xfAm7CqZOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛‌سران‌منچسترسیتی‌بیخیال انزو فرناندز ستاره آرژانتینی چلسی نشده‌اند و مقصد دارند به هر شکلی که شده او رو به خدمت بگیرند. انزو در بازی اخیر چلسی از سوی هواداران بشدت هو شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28453" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28452">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9I0vxdjvM5N-74wJ3d-A5Bq48dSqqtN1JNtujTsxGAl-iJJ3fZkIs5pi1eSUJtgIec5VT5H1MFh3F2VBFyQs7CbTvOQ9L-cC24ZUx139fvP0xyt3Rk0JklN4NnEdf0hZsPQqW_jXVNSzpzsxPudB-iQIVJ895waafxvyNnAPcjVdIRhEmNOkgBu6Pxh2NPoOAUNcspTb5rhUOyIjaOJ5I9__XjZhhVaJ-NFS7DfMPpSva52qpmPavlxcxD1JEqCBgVwfkRqR-3f8UswaAk1CzKO95zzfJyMo0_64mas1EmK3GrR2YOObeqSbmsKfQ_dvbL4I243ZOaeEwq125bvnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی‌تارتار سرمربی‌پرسپولیس گفته ترکیب تیم‌من تشکیل‌شده از بازیکنان 22 23 ساله. براساس امار رسانه‌ها میانگین سنی تیم پرسپولیس در بازی امروز مقابل تراکتورِ نکونام 28.5 بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28452" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28450">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr9mlV47e5j9Pl4qso3sm1s5Ht1mtSx4RzYRtZDuHnMJjbiC_r2b17x5RK7QhkhZpf_JJ8zvXAG-KPCIGudStAbI7NCQAyBxZUJTiq3fMv8cXW4LbDN4UMqQXZvfUsYRhj1ULN3SxRzlxXgr8-3dIXkUgoBOtD2R4Op8tn2NWSlYEr1IgMeScGoWMLcOx7BEG4TQ1klEQafA4TP_6DPmIOdn2l2I3faqPVxOWtJm7nYMAm0SGjho726HUy6uVBdLzQ8NMfCGT6aZDz77Wi9p2fwYm6Wry2X99fV1hgDJnb02i7kbsvPFTKFeVzizs6f5rW3egbAeufzonxBGQirq4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28450" target="_blank">📅 10:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28449">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=GObFkW5RIfVC70ACIAHXCTxtX1gUZMf8fYELuApwfAV8sVmF5lxsNSHGkZlepvuwfiuZxbI8KGW8UCfT5ZYZ1eNzgs6CsOqazJX8WWUehTXT3HVmxWw-ek-1SRBokGs1s_2ln82NYLv3Y9GVhcPY5A4kBJG4Grjf5qt3KTYPzbe-vmwDXQAbVQvm2pcFt9uIpp6vpmkL8wWTpWDRu8Kzt0Tqm5th4rYNYB0BNfO1Wfpeb7SpfTcG1CkutiMCOma_Ze_QZRxxctELg8_opsycdxhQUMHByQ35omR0Ep7a_w9IKL6pU1rMIl0Dg6ZzyhkiWrTyGLqsi-HWOWHsurIIJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=GObFkW5RIfVC70ACIAHXCTxtX1gUZMf8fYELuApwfAV8sVmF5lxsNSHGkZlepvuwfiuZxbI8KGW8UCfT5ZYZ1eNzgs6CsOqazJX8WWUehTXT3HVmxWw-ek-1SRBokGs1s_2ln82NYLv3Y9GVhcPY5A4kBJG4Grjf5qt3KTYPzbe-vmwDXQAbVQvm2pcFt9uIpp6vpmkL8wWTpWDRu8Kzt0Tqm5th4rYNYB0BNfO1Wfpeb7SpfTcG1CkutiMCOma_Ze_QZRxxctELg8_opsycdxhQUMHByQ35omR0Ep7a_w9IKL6pU1rMIl0Dg6ZzyhkiWrTyGLqsi-HWOWHsurIIJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
مجری‌شبکه پرشیانااسپورت:
جدا از شوخی سبک‌فوتبال استقلالِ سهراب‌بختیاری زاده یه شباهت هایی به‌سبک‌بازی منچسترسیتیِ پپ گواردیولا داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28449" target="_blank">📅 10:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28448">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTnaq4ZyreYo8FKvUUhOSHK0z64KfmToMQH5sk-YeRGMBeIYqEeHm_y5a8eh_U02DcSanKIMs8qr_2sVKzHKdyoQOr6nT_rUin4QJMx-3YFCrxJMFqS8fcfUzcCOlyqxGuMZnm2bReY45Rioxm9FabN7Y6xNPNZIL509GQGO4b7EyB0B7wPBxfUEBTZJLaUuacPJi-iCWYZw3Z356Rk21sjukhU7Wz_wetBLNBi_UYXDyu8CV3yaBnongLp8_YIr0RGjIgHH8jaUfqL1Q1XG-w91lknpqifXNiXy0KJ080mWNlAIZo6eCT-o8xCX-iEdaxHJsrkSrCxsvC5eLxoP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه سپاهان به‌نماینده محمد حسین صادقی وینگر جوان تیم پرسپولیس اعلام‌کرده درصورتی که بتواند رضایت‌نامه‌اش رو از باشگاه پرسمولیس دریافت کند حاضرند که قراردادی‌چهارساله با صادقی امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28448" target="_blank">📅 10:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LS1guyPJ-vi5tYaV9waOkH5uKkps2vzdYWtOLAvSyBKtwEA95ek4kpzJ7CC5_NwouCU_Gku7tGP_6huqzC-vbgRFjodShvtsCZ_mOqIonL6c8FpboNA9GE9WlFJ15cHvtOQ8KRmJzUDgOxO01eXEJ8dCOkAq7GWPF6u6rLjq1-yRmsBWVXurGlqNnN_zkvk4hCvZlbdzL4-WSjYQMeu51cui_R7R2NhScnQP8Weg38pPfqH2OcyaDsWZjCECmJ2Xa7Wh3rW1bQTfI6iNOwBCQr0QlgtW8UBrQxzDUYdKSbqcP_LW9UCrwur8pPYmHQueH7AYyfowA3jloTSSyEGxBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgeOcC4XK_1b-bjbjWm6pFZjW0qELxmydxBFI3UcBM5t0Uw1VYZ9SB-p39tffhx5nYIhaa1hLW02Mmyv7bh6PAxGZBg7RrS8_W-g3lKjjCf2-KGG6x2c_1nw9JRr6sJrj9ZGcl8peysrgfra5DjAEBG_C3W4qErYvEg9qZWLLhfXabinyir46S_qHWxEVWGOK9RmQAGJ66Sm0b5OdJAkTSxktjbCMHpQRAMZSHCUO6N5XCdtt-lT3w8GpNPXaa3T5nObJgLiHLn9ELtWL3Zo1FJdaObglwbzDXGqMthlOCApLxPaqTp_hfNHuakIGNY-IcoWU4Q_HsaaXBtwkevJGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
برنامه‌وزمان‌دقیق برگزاری دیدارهای تراکتور و استقلال در لیگ‌ نخبگان‌ آسیا؛ این پست رو یه جایی سیو کنید و برای دوستانتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28446" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrK4mFhxEoSK8JR5ps_Odv-c3Xw_AADWqkG8IRm2iz2uaAQkoHb_5Rnc3AW0nzCn9Vg_olqXoMGliHPhnp_f1Vp-Qo344MJrF0kV9DE8hoXPWgFhQdUNh2Lh9DBr0u4cUQjgPmNy6wa_LeFIJ9l73-3_jTUSnG2AKV28TnopqDO5HH-pKYrtdWWh31cOB7eCfebcAjFfzoeuK8JFKGMmo6ZJYl_DQBCAlI4zOSvT1ZmugGvPQhnZi-KYzqFVRnYG_kgxqRBBX1gxJWkF2H--jm8S_8rGAJDSvOiTG7lAmv2OH9S2jA_czenCXxYNjoOy6237wSZMO_nrPKC5frrcipAro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrK4mFhxEoSK8JR5ps_Odv-c3Xw_AADWqkG8IRm2iz2uaAQkoHb_5Rnc3AW0nzCn9Vg_olqXoMGliHPhnp_f1Vp-Qo344MJrF0kV9DE8hoXPWgFhQdUNh2Lh9DBr0u4cUQjgPmNy6wa_LeFIJ9l73-3_jTUSnG2AKV28TnopqDO5HH-pKYrtdWWh31cOB7eCfebcAjFfzoeuK8JFKGMmo6ZJYl_DQBCAlI4zOSvT1ZmugGvPQhnZi-KYzqFVRnYG_kgxqRBBX1gxJWkF2H--jm8S_8rGAJDSvOiTG7lAmv2OH9S2jA_czenCXxYNjoOy6237wSZMO_nrPKC5frrcipAro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
موقعیت صدرصدی که دیروز شهرآبادی در دقیقه 90+6 برابر تیم‌تراکتور خراب کرد اوستون اورونوف فصل‌گذشته دقیقا اون موقعیت رو تبدبل به گل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28445" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
