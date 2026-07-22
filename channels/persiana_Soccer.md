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
<img src="https://cdn4.telesco.pe/file/poSPcI5yPdJdgU3hrGWzQ8eNlNE3zapgCh-p1KY9EzWFshZrrmk6g8xv_jMz-lhmpSyZdgVhD96EHbQiIylh6-Bwd9mBM_kB3yOweKYxrHTPobLrvL_8U-ytcw3NjalGhISMqmKXBIqv1jTAiCzuTQkO_J1nsIYUqcpCwS_yLrudASTBEtKh1kC7fW68qXIpZshIMQLuPVh-glr5Bru6M-W0_R3wK2bckl5dJVscMkdk_HhOKeFxve6XW0VkbzPAViy-a_52UxoQOBpAMwnSqqC-b79L0UOn2o6CdmcpLuPMI9F5ffHC1egyLumEt46PMdoKSbNdP-qD50Dyt8KtQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 545K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 21:16:59</div>
<hr>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ0HJqAh26asGcJZtmV9ucW08X73JdSHIZIsMiOACeqjBtfQV0s6fr_sVNSQANf2Mk1vOODnrfZMLP2jxOmmEtWskNPpsJVvWozhYW3ZKfKHDnL_3bzo5Ug5518eP9jm8gF96GW41dvEuG3N43Z2tnFh3GvIM1cBSyXWq_7ffFmX70zpWs2CJpTsHDZ5yitJGCpv5En2h9m79XtnOQlDIT6SrmRrBjnLxmUDSB0fvwuL7qf7bEEF1VBdvOhReWUQFVwIEEh_vVOuExDfrc4YzciI9x7LC56AhMhvZ-bpF80T9U4udlUv28378PWCYiJCnUZ_bG_Q3LSaUDUm4SLf3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u52p_3XRjDB66XHHcd3eXrPxCsAO_1p7_ZKI7xv3NvEtdSASDAqkjsC2pBB6nxZGQ9ZdNh25WO7QCwSIxbBrp5w_o01kz8FZ5LZkEuwWwkDTBwnARJRRe2qq4JChcNFDjyUWW0s2M9TqyIJ9RNrQ-OltY8ZX2dsJkqEeG1h45SaBsRGm5NYXcMnCqixUPSbeQGYfR0SlVMoUO8XvDylSamyWOq6-xd7RXhxm9R_yL6VJGeFOnTSP0vOdU3AF550NsMKW3XakkuPy3XbJ3YU8KPWdC01soY9m7hCpz01EVX-oE18tA3yYA32CX6C2dbbC57EoQNRLpzyFtH5I6zVUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=jX6v9fGnE1w9T-mO-xMpLax8dq07_tmR_8h1klGe4f0qRRiF8Y2DIroN5zvpQMqN-C0LsOVcq4nuvPcB_SK78hwReO7JM6m2MbDaGdmNzLWyD-2alQzr0cjhrKFGN_0Nn--yKXAW81BqNe_bJP2KgCNODWnTJ5A1_Q2pfeWnN-v5K-8bq1ni8yveo8dA__zERCcrFR45VYtsr4yFKATW-LbXMO7Nm-mecZ-N4TvBHnpb88HTlJ23bfMLyioZZRqtmoPRIPpO25zJqyj5jcNCZaZnX_2rNn8ckp3SpophYT2EhtNOATrDUxKj8r51pjBFrChAsg9uJ9HorLQXB5iljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=adP7pPJc-vXZiBZiGtPskDGPfCxyNWMbFnwAU42R0sEd3B7bwc6jgOiqE4buP1JzmtKd6ly31njubTohgsYKxu4NvyLHwcgds1Yg1CUtt6B5g65g2WFH2fnR2R7tBeSjC2gY2pEKDnP867t0OkO7yqaivZsq704mqUAyI4e3E1nO2cyaJZhpjt20WHlw0FWBIzZBxdVSYG2wytazvRST4Qmn-sDqoVXf4wQSRIZFzlRFy67Fy6zwTNhtAzmSPExw5BgBHF-YSGXEUI1qlcWKK16EOjTOotqt6sKJHfPbY0RZIwTkvLY7nW0ER0Y3kEbDZYj-h2qyAMeBu3H5ybyqog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1W6pJlD1zYMdlHA3BL78qOA08yY2Qj4oJvjkI1JzjmxkZV_ceS2qvc8e45HlU097LMMMOBOjEzZsGITbF48vLHPNrDx6E9wfcmrUcQus2K5MiAU4RDsLMmC2ejZIpEnWD3ET2Nn8oP-20rNTSsOQ7MN7UQ9qsKB4TvD_OFFo6QSA34Mm7LqXNW1UYsRu6gHR4R-ZAjcoGUtRbdeSGgalJpwQXx-e0dUUMgf4ksUOshhc0DwW8Rj0BGpP1VIY-o6JX5l0LJ7b9FTQHIjTRoDOQWy07dPaPkL2x6DAp0QWU6BF-HE_XHQnPyWshqIPaZL3eK968xPfZdRjj8EQ_PPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDp-387yjF39QLIM8YF3Gk9ELwtzT4_4_6B-h8-qbngUZ2fBgrQE3DAGsVxHI6oXG-A06kAD5tUcoL68owOc2otqB5LCsW9SLqvFN05AzZRPlPjiV6QTj4jPE1rta93hrZI7sD7noXFOuBKA4VOIAF2OyPxwr4N9oYY67rqjUUM4wzh_OkRFlNy-a3UmkK6H3vdPJ1DPLuSTqv7_aESMFyRNpBWN7hgQdVpPhnzWmI16lJdDz7tGMiDjVEy02ncjes_-sceYyTGZW1on9h_Sr6YJ8TY2qkBTz_xsiMCfHU3xLzSan0jMac9vzYfgDGmPPOUVxTy_8dnUSt9tHvr5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoVDrE2BZcH5fTLEdGoGuK1NkMf5CSSYE0Dw_w67gE1WdzZVeLSMWiPWepAfSIr6CNUsiMDQf19i7cQ9_ObLEGnpO4rLK5NEq6DJS8msQAyAv7cia03V5xjEszX3nE_l2Re66vO1CRGxiTC5_GA6BStNBJGxQVR6vf7i03eceBhSTaTrlDqDXinMnCmXQZh-Y7hdpCLAP0EnnmOYjElwUc4ueWAAzu4dlI3LXNa0wm0eR0QjdWO7J8al8KvWFz_SqGd4m_P3q71RZE48-er-zY62_lHvFd8nrUTC5MYMToqBodijIsAqViacHLKbEpU9pwwJNRzCPPG8xJWADIdgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgPedxORJXwDG9JfYk7d-GB75b8JOe9BwA0JX-lw-t6gjp_eZ_tJQoGHDq3USBi79JzDBI5-MweLEonR7WJyAKyiDK3tDT_3_xE8E4_KG4jhpfJWeaFQ84eZJAtyWvNZUcdWyHohgipMlN1V59zxVgz70gYLEh4w7PODBjQGr00h63WJj1CtaE2ZtiEaUOEY6gbDE21tUCsi379ggO3V3f1pQavWAIykre7PXg21AoM60B5hEJ7E3enK5yfIsXcr8BEAYE_xepQGfm-xC4UKx35T8-diB0xY79ji4TrI2jPDeOi3mDhsUwxzPztXVxju4V7gK2therWAjFspnTF4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMXFxXOvcoWSARqD8t6JkM4YxYM5Yq2eBYz89Bc_Hk9iB-i-RWLeuKoOjjMwfyr4pRDyAyv_hSggP8hR_iLOuBSa2T-BNH4QYxI0PdEZjkopRGpDy5o_rbci4WtZlCIQyeag6CQ0vUfgS3UIYdc8vVvRuobF9G7p_WQEEd790-J5Xv4M-ePdKZuRRP06RyYVZ7-2_dH9zxIw72kL10vB4AyCAfoFZFc6Qz0zKmB1SkYHnjALd9sdKEH8pigHyW9r__jGhjJY4-1UVbxK2ZvYVDBDigGw2WrKADiWAaCaKaDl231lCZuaThNF_OCeRcJoLIXjt6QlrpFkM9voGkNA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_pV1ROFZ2gQ220_2ya6NYHWwuqYT5T_TXsplIjniRPDopBiewOyssEA2KRvfOYO_mhwAgB2bLFQbqSZO9rxC502So23jk97JUMiTrtY3Eocnsa-dR0vLtQEMOigVVVzEL7DpoAqSNIjqeSfZUi1pOXyGLo-yWCHVM-IwuIFcnitc2WzSaXOcHVKkh-aFh1YIIdMDj7NQ05X0yWFF1ghQUOfSCHFRrLOtZb_KwKF_K_4ogsCfxzXXLIAVPKtCvFR5dTfIMLQ5amcSZxqxnGLuh-Czu6ZdyJp4rCVD9U_dD7bHuAYA_0-c_9dMxsDOfMj1qlc8TTKDIUr37YXiC9xjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx9LXdV1H2SKcYt-WsvjNAOwgnaIVozCBFIZDSOHc918-g9sRfXsCnOG5eKpeXlJ8MP50OCpuoIGEy_IWXLcl_vh0NQxGLC0VR4192fLAZCKthgZPoVTTyPE6Y1oJOoRnGvs1gtE3tsNg4tEiR2w7aRGkFKQlOrFeHB2BcderLEnaWuQhUl8-XL98x-F2yOOXgfZ5aODfpTId2pCLcvoqxLHDIZ3tFIFEL1k2TL2UdggokekCH40vgkRd3JLOKN-xq-yqaYu9OwiKMLr3I4Zow88bhhOoAj_gGA6emrqZxWt8RpbiL1MRK83aE0DNCB7UTw2LxkJkWtzfL1vCu9aYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ1rHbkMoBOmHlPgc_lt-JrSLNZECPCIftHu18-DyybZ0uWGb1N-g5Jv2vp18Jj6UQXP38GRK5fYV8u-lNlHkgasyw9i408yUAiIfCsdBEsdLs55DCHZibxdbHiXNgnHfImeihYth5EEaUicAHIg5vyPSbAeIrfGPa_5GNTFEt6ZFuSBDRvf-gm2pZHrgNJQ1iFPb-GhBZ9lExNYklMjsY6eLIPwfuKtimzpnfRLcTU-AayGF9l4qHMc8dCIQXNRoceWGC9A4KkOzH9bkt5NWgcvZBvtMon2PYkRR0sJ_owJYZOzhNx6UE-CGx9rI3_-odELKJohzsLDqvfbYBfZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OemgJYU3j0XvuRE6JrISGeYLvj99pf8sOMMWJh7VFxxdw9Lf6dqQhL-1PtWv6LPqYdrvdDTOoiY1xCIf60V44PaTioIrLPCpD3KVQuUOvYBuwOUFofqjixsXX00w2nqGr0_BhPGNOu6OLoe5hqnvv2pfMclt3I19lj9InBP8fRM43v68SYEmvH7lKsOJCXm6596BeljD5sF9N5_98mYopXsEy4Bri5LoZpo7VQejrpPshZWqx9JydWOzPnArqg3URX_YXDzxt28l6NX1FVDoYOxstDPsfDb_x4ldALc-AhTHtV0UUvtIHl51WsWKoagLVEsh7fRyfvG1ovWOcp7wSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1Lx0u1mLBx76hVLN1jM0V0n-6U0J5H5JG2MzkKlGXwRxZZJM_5naeoJdNoLc2E83RoCteNBq38maEMxHoU0K1wNCoCJ9urYUo4dcBfch-OfzUUilPDU6t__cDTRLF8Q0N15dM7i5PDG6HDNm1adHKgtsQyfwp9lQLzrife77SVwTlJ9vaYYRJY7-BqyIlObuckenffcq-1xkfFxBe8Ons-YwUaWwGIRVx3QcIQAQDa8p2FKTuKurxFFx1AeOICQNIZU4RzJeh_oQ12XDNShGbYCM3IwvDul7pIQVVI-QwHKmh5qC-ylZqRx1G1ALTFL6GndfwWpI3qrJsUGQ2LbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUjuyaV4yXw6UFmpuUkZtGOEUB3prV_gqndkMXM5U3Pe-GzNC1eLJIrBWb9gbeWO7Oshvn5bLQBmldPDR5nB3csXniBvQhJkjq0jyhHQlwC9L1xcWnb9Hma0UR0yp18sOS67oOPqBhLJ3Fikeurx5FyuvM49cDN91dICgZ9fabcpv3wjFEg7BzAqvxRdcstV_ugzSUFo4NVP-jLKjF6rJak6mtaVj8tsV02qbziNTiD-1bMeqXv4zpLK_Viqk9BJeU-5nDKSgs9Bvs3kME-ZZbGeo207EsX1QtQnfGjNfdtOh6SrRI_GOAxIDcHEMaNzAUEp5-kDMVIKfMwUTKmEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwvOzMokkoLYNAotFP2S7_AZBkYVoZs1bDiDefzSnC9FwEiEt71aCSvEbrt0fmYM9RY8veF5kbm3NJkj8CqDKOYVPlHteuoDhrMzi2VVNWYIo92QLQ71dRd_7nQBoAyrZMIwg_RfIVB5pvmcyJTMhb5zN7shGS1XUR-cdf18pRABzmrc2RJd2AHdD2ynDwSqcghpsxvSlPHc810-hwm8IaqrIZN4ML8kubFtX3UqaseiIgkGlObpR0agkOUcgwSnnUgtW6VbrV-NH9du5twx53PqLkY481C0cjG1FU3lgLlhOEW-D0FJaFjxWMI5aU6pZVo60TL0jrmlvB_mlY1MIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvEr5QPWrew8lrEJpc95xgK-9DryBZmMVF0EIXwETBLudX5Oeztl3qTZlZcdl8jqYNQe2RVAsyVzS6DGPXQ5qD3jJF4OKaJDrKevZqlTDQyfSCeHD4eaMON_e-jsxq_wXvpPQe3TolTXp6u1LVrvvnGTAfa34bP13CsMo_4hReALLALTvfDm9Dl36AKtF5PlA-C5h52XBXnWM_4YoQhIm-r6x2x5f6LJAjl5AjrTzK4i86cykM9tW5fLByY4xMYQKPLI2nt3FaJuvbA6wBzWpyBaTtcoyaUX9auvrUjAxCj4n-v1Tbm-NUJBuY8jA0SKxZdkST-SB45IPzweVdk7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olteHfHhY6FAGPyNwYPVpjyNozzi1-b3pQhxs0CNhfKf95ngvEx7XDfWulWNJz9GPEYUDRZN9ogw-xZkhNCXIYVWOY2ckts0SlonmYlBoKa85ajFlEgbrspQ4bI6MYPpdLXxqTA2aSFnNoAjTRFhXaF1tAmOkdKyWesraXweIV5dhEDE-HwKgaROIDUYHtL2mCpmrlvzz2ehGJta0PVpuzePRfxBOe37fV_PZl1yVwYRM48NwuMlt75eBl1EqX6RQ8pcMj-QZrIADsPvWpL1k8If4tzRV5-atp_Ap-1Y73_Ie5h25ygNiGnXsUPOTplelVnJou-Sdz7afHBrr7nLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D0F2hCZWzazsyCu-F5KGXkjlmCkR6NOvd9fO8f-rQqTBLWqjYBnroHbqDbteYu0b_2gtmu7UIXHzW502-UBj9PhDehMa542M8rbaZNLbMa4_HLtZPheOCe6FWkeyYV6WdBY4CX71KRATXkths2jXAIMnMo_zj2FdToctS3FGQWaChQwBU_tuTKDysjcPsw-1WEbzwayt3xycCZG0_YWto0NQ_FVFw_vwg-1kEqvapi9KfDVb37lnqVDxOO5zPABggnZACAyq8Jhh7iBvCSZroWWGBBxJ6z5W7cgGo9DgqOVYx5k4lJbD7KgN6GIJQs8GZ7dUPH36eaBw-TnsZPHXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4PgX-FlcV-_-wihCwlTbrQ5IrHNrA6VsDg8HNH123FdXmhrffNXINdXKzwYEob-oBdk7w34p5xPySSfQzYirOjVMEoqJl-QXF7I2Zxam69wkX0kbmj984FlnMcSz2UJIaAUi3B9xIk1yij7JrmUunE95H1bcX5hwR5aI1xtFZ9tDB2f9A1sMeQh9QyfnDqGBMpjqJS3xPFVzTTxX7zrzEUQrJeVxEXWp_bJQhONbVaIBTlnaWz7EfeU5LaI5-K0_Bok8CZ8bnWwATtJ-Sxva8ecbfG-ps4hucPZk-zSG5oINd4m8H0Sg5nS5jM12lUyBnwo7zXX4v3SN0x6uN7nBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYIED3fY3wavwMaHP3UZLkjHBpfCaaDRswfwff2c4Yd0r-xbbxJZAOJ-LffKrSn7W0CQ8m21hWIo0JjSsW-bXKLhzaiwPz4wwCCO4FMOeyzxqZBdueWcq8EtClaRmZ2Iis9wVMFIrPHRpor-u6s8HGxwnHfkq24VCf-Uz5hhPt8FFl2UwFOZC2TsHmLJwG7134JIRfvcIK9S1ZQ0D-W0aKxSW1J2cjWXLCrJxUs8-_bg6Jy32R54cXSuVbgaPhK6e7IYZhT5hP9n_nwex_4tOQ6ISL-dPM4LEbnjH25d1iYAGRZgEflPi3vINDerBuEHVRaDgtR4JFzhMXkLpGrfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqFDAKniYAtGC5HhYFlo8SqWZFsdT8PvEpjD2w9sEf82o0hcc9zGXtFuZIASHO-69PRyvISzz9iyfwpkKqPboKkfTnADCZq-pTCzzW8oXZgQq69I5k1Gy2mZZX_c7781u0vlSXLzU5EzxWT79XEnd7CNxtfIXd2trElQXCB49TGphWw3eDFyh-uSLdC8MvHvRdAGOh17Kl0THrQ-veIwEqFE6aeNMaRJ5lZRIL3qfmFJ7wzDZ3yhdyS1S_TCl8eRevoUfTiAVEfolNW1FLljPyXQdBw2Ogy-WExtUmivEcleWDtTIiqJMDyfTMflU5_iNoPyxhbvyNFAbGtmSHItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmFyLCClfnA97WjL4SxLwCGT5BUfKUGYrV25O1L9gJQuQOxleuLbGUTX_Bil83lQa2BXPhxyfgrS93bogN2ZKiqSsds59-J4f0fysbS0RmRBusHa27og1P-_JsfKLXo7gAfXAty30AJFYs9-8L8IQaEO4-33kp7DWZhgbZsHUT6PWWt2ID2PWweEKPo55AIwDh5c1ussKgZ03grf20KnmVNd4hPFJVRgTGPDn--a8Th3IGUkVXgtPUpgUu8YUnwUgPgXAchdIGc6uid_iZsJFbkNkpQ6vReBWpsy2_1PwAC3s7Q1Sj0DRdFs3s-b7x1eHyKq7nfX17ytUdkFmoXI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT77gQuzeTLN56X5pdBpJw10ZzRu4kKByKWBiojAbBdIFLiOJMCSGeYki18JCAWreFgEMOhSavXNcEV9AvFuUgs7Ws1CUkLN2ufUBwmLs0wEoJKvdb6-C5gLUHAeWCc26zE5rA98aCxrGlOFf3Evs5G6LdP5nyt_6IFWHTX7gnrDe8X5mJZs-zRobzbPGPFGiCMKoFgyzwU72Am_S4V610AfeJaycvUPAsemL_QJF9LHv4FfeezVDk1bLydtPPp_c26wk8WUYYJ0p7BA3eLFJxFgl_Qtbj8a7KVQyT4_emDj2rJ31aaKAS4tUv1zuyV2_qIYviDxV-VDGtwWWVQuBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26286">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h41pbYvhb9e0DKRwl4nmkMylfjR-L_tw-Q_u1kgjrIAa-zqEKnIpLdrsXeEsv4NaKUUyLpzbZUnogyAG8nrPyUxHWEjTejJBgChTLoF26tDq62oMlN9rggeq-HnNLHq1xbsdgLGAQd1Uz23i0J0pCAAL_U8wmX0_ARuoNMvHyQv-DDyU8JrYXMyfBPprca8m0c1Jv8g3xWdzEWntvrDOMsWvDi4IA1_VnsilREud0LNmu96zrOoNtpPS4rzBz9zjVlBqEuVwK5VVzueshEg-U4zst7Zrdb99BALFund44B6QeO6SNd-fvUSw0ZCegQaC_xZxyRK5UiCPR07rRHVDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی
: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/26286" target="_blank">📅 13:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26285">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHSV551QYiaa7lNxeZyZHdoqMT5rVTZ2Mp_QqLo7WTBaFO3W3E1VFTfTT3j0P53qHoyERa1sirBfEfeYaYiB15LtHussL6SMdUEloOrh0KhkK8Thn14Bw-eGzIjDW1WbWK0BPNtSHB4eGsCjKSB0XyF-35NKkFlQy2X_ixysDWAN1KVjjWjRiLztEmR-2v5pJL4g-mnNWeUg6Dyrabb6dwT3qInXbxspQmbmhdYiTnFWj71lwwgRwRbHTru1IO3i_exbTlJBLDKBk47k8niROmoK0mvgDwG3brHc8CUnDotlSe0y86SCFbjuYT41KlrMKjmac5UjCvjabQJgq3tWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپید، یوتیوبر معروف که بشدت فن کریس رونالدو هست‌ شب‌گذشته حین اجرا در اختتامیه جام جهانی مقابل‌چشم‌ میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت و به شدت مورد استقبال ایرانی‌ ها قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26285" target="_blank">📅 12:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26284">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRvbMTLBdPZOTyaVhKM7EMzUwe3y2uxrJ9X0GpgK0cNVnne33bFE0W2Svq4UvTNlIkFlVTWweT-EJXXMjslRopUL6LygZlgI_3QWPVEabWeFEiIrcn9Vw6JvxR_NSiCySwAi2PFGVryc6fFa6FAVmD3eRYeSOEAQNsuNcThlDGCKuEEfVFmLK6IVeFxf8si_tSD-2LmlXlb8XZU_9d68IiQROcrqGoi3CxjAc9YNjE98CaOyr6DTjYLqpUVpSMBwlKKnEvJjxnGXLo7lEnJ9L3HNL62sZoMRsgCJvyShc04_oLnktrfaRIH2PJ0v9FWPDAvL9O1PIBrxj468XvFEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
با اعلام باشگاه منچستریونایتد آندری سانتوس هافبک برزیلی سابق چلسی با قراردادی پنج ساله تا 2031 به جمع شاگردان مایکل کریک ملحق شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26284" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26283">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfbTxnVOObZtKHadnNtxCtZtdBr67DUZynwZBbegv863QHo7DJRrN4GT1-KpPcUqcbcuP9iAFKUW5HdocjXct_GJouLM6IE11LJnpaqE1LCiCiubLYpF_z8KSWaJwr28LZxjsJyQAnnV3IThy2ELUUCroidbFVji9lFQUrTJmP5W72mnuVGxdtupRThGoZSSNkL7gmI1mlgGRH59_ZOxE1KtcWsXHmVvRzCAlDQIuCV4kGoVvA1NqdASSzwaUOszNx02vbsm4Z9Mgp-iWXAgKGEfiRVVF46hxfVMKkKb8eme1Khveo7yB6yYYw_so6mx7C5yhtDUrThh3OUWIO9LIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پوستر رسمی باشگاه چلسی برای مورگان راجرز فوق‌ستاره‌ انگلیسی‌جدیدخود؛ چلسی برای این انتقال 137 میلیون‌یورو به باشگاه آستون‌ویلا پرداخت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26283" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26282">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grPzqcVyce5MbcL6MKBQ736WntDNNSBCCHlGV4yXv-f6hY9aL9KUptZhGMzt8G1Pfc1clCX_i-89Hsc7T6fyZsvF1hINQT9AH_W0MOE4VI9vlSqndsQCAH0uN1eouRxmaGc5vHleMy7eNpSwdJh5AClTqbRTGEai1NgKnIGzaf3bJDS5V-zwaxbYwJzVVTs-wXq6ks3kXsstP23-W-vDJJdMXGXViybJWMkOT6dkhCWRTBgjCfOn6Fvcf-yRl2ApkEOZNMJL4ohDWF02auUlvzvFKKsD8MC9qU0XATooNq4ikSY7rY3U-fy7FDUWXeglXY-YhDVgkvAeQabvm2E2gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب‌کهکشانی‌وبرگ‌ریزون رئال مادرید در فصل جدید درصورت‌قطعی‌شدن حضور اولیسه و رودری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26282" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26281">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FueuJqDAvtTTLVmIuUP2sqMzu9BsTxqfH9b3vV0p2UFwih48yP6fdly-jBfFDRE5zUpO8BcBm5m7A_XtAfbXJPe2D2I9bAaAn7kF3BETpxqxBKxmKmr3lfgTeBtGQk01qEW6pCttXT9q1tDJZOOmb4S0gUEfM1KFFhuomVTax5JlgkPDOPSY2N3UdbS5SHrdL0_YIqArda-7nOE6VPMb-oeLXvn3MupFX8XwdFhCjFAk98AL00gQCl-EVq0XPzmYaHlViHaFkpgrk3-AaKYIBPIE-Za0GfNMN4QDyP2WO20IfOKlKuANLFI8SGKTzT5zQc0ZwRk_fSOr-vAAT1p9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ دیمارتزیو: مالدینی مدیرورزشی تیم ملی ایتالیا مامورشده‌‌که پپ‌گواردیولا رو راضی کنه باقراردادی چهار ساله سکان هدایت آتزوری رو قبول کنه. بایستی صبر کرد و دید پپ قبول میکنه یا خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26281" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26280">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxAjgqSl2SB1YeWhbuLTig2G-bw7zrV_xlUArawlnZ6fRv0SdEEHxp0A9z9q28hck0olb0ty8F4SyEHlh2t30blDhCu9uIZHWbC2qWugYc1zpuMlDLMKwVZZrs4ZwHuxrExRmYMhQ68PV-S164IVg-HrQyYxxUSP5IHVKA0BpI0nKdpMuIQfsHg4sTk6hp4xtkxJjH2lOm_RlTyMhITMXWrMfNeMya9nNToe04o1rnvOdSq81fF7EsZoevY920xS1RyS4Scuk5MT2D_RduxWbpPZ4V2cgh4ibuylMgES-D6N3a6ug1zAHR86NO-vNoPVf2dzjpg6nWtxhq7kjRIuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
1️⃣
میلیون تومان واریز كن
3️⃣
میلیون تومان تو وینرو شارژ شو
🔝
🎲
سوپر بونوس
🤩
🤩
🤩
درصدی وینرو
🎲
✅
مخصوص اولین واریز
✔️
🎲
برای اولین بار در ایران
🎰
متنوع ترین بونوس های را در وینرو تجربه کنید
🔊
با وینرو همیشه راهی برای برد پیدا میکنی
🎁
🚨
اطلاعات تکیملی بونوس
⚡️
✅
✍
️
ثبت نام آسان و سریع کلیک کنید
✅
🤩
🤩
🤩
کش‌بک هفتگی
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده
!
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
r31
📩
@winro_io</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/26280" target="_blank">📅 11:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26279">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct_sCUJoYKCSkrv7FheNNZqS-RNvF_O_ORHUpCZ9J1TkFd9KMbFXRsSJVfplWs6IIi0Qpl6ARsCITny2-CfJYSQdWYszNX5XdAFkfpE96sy81oyaKX4rxXexB5wuWYPeWnfV7F8rE3L_zuSW6gQZjBFUqWOt5uE785dHXlnWJoAB7uip1Hm0qNChrPM-RSvsm1-FShQNw3syvvpQeT7zTODI3GBY2XI9YaT5gMKGmToLejEz2yI6ogvzPItpupOHtZ77yi-I5UjWnOSTMN1pFOVvs_OWeBbvdtL378j8cr1DBNpkZiGgMdRwM8KDBGrdphF9RsOwHZOEHDVOrvC8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26279" target="_blank">📅 10:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26278">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc9hWvN41KNFguFZXBHX2zCwYwB_Vxrrxl8Q9TPtxrF9YZ_EcEsImlWPlCt2RwB1ezHWyEFXTXT441h0IsyWw1ghyVUSZUA1pgltBu0L1DtOqdfq--Wpp1CfbO14opymjWiZ3-IiXLlg_sq8kQPuejDxVEoVIXlKEc84bWUj9XUICNi4RayCh6SeaGxo48Wo9ggdWOzIGZ1DO10SMmnEHOrJCjoalzt0R15ND7jckh9P9_bKUNZkV_vDkjMhapXTg5dxMua3gEGwMPJUos_2Pg7cvZA3dtSNSwKYyp0oGAB-PU_HjhVswXEs06rpcBmTf7VhjRto3R_qgW1LnmkNaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26278" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26277">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2fwQEkDyLVzJCxMXqJVrgoXOr1JZN8wdH5eoVbmVExLp4vUnPZMUhjyFbPKDUp4aTqa9YJT7Mxwir8EzfuKU3R99VghS6DlkYsZcU5fwooaJB8E6o8G-aTGXUm4wyq_ICUTn2xDa1daRLFnJT9Ml6Aqm-69mfJC6QHjz6BufnqePkRLKhkUxrJ7FWtZ4A7ZDajKg9CuSRewC0m3CefYR2BAQhIcuv7mbmfgwd58BBuKbabkWXwTXIr7zW9uUlQ-NexarlQvsq6_GjfOwqA-7b4aBVTijjfMo-9idfdzl7JGxTIH-5n3Ko3PxAMet2EjTS7c1vMpPgfzE0y9OUAwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
شمارش معکوس برای بازگشت فوتبال باشگاهی اروپا آغاز شد؛ یک ماه تا آغاز رقابت‌های لیگ‌جزیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26277" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26276">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKwO7R2uEbyelP6p_iFbqZPOTheYL5Ln5osouHvObuD8PyPO9ybvA6rqdpR-gW8cL54gXfZkZn5KH_7GBCQyBJVsn1jMUtaDbVBIbiXQd5RnrC7pTg1LL--AUOOUo7WZbkGNHoIxxOusjofXxlGfwHZymj-ztHdJHBtG1LkraP6zYmmX0CxmDHOE6isyV3qo9L0cgstJM5G9YFhuEYbBRfMJkA7Yu13vuU-jRrgQ_5r0R6o_UpiMLuLgRHubavH_tfy9BnzwT_T8s8g7o9VMhTA2cuhzPwX37AbBLm7TTl96hTuHgnQWZULzN_IgYS9dR5d446On3eNcdohMbeQh1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26276" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26275">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScOyWttHrXssh489CemT9klkbMv5NBrlKwxIqCjfXmADmwKVTuwPEq92LYVDddba8O_SXMPL7CFSJZ8Vl-BXufWPfbDYLX2Bj5CTeLrXicprgSJazowOrn512oK9Lo8StgDhQv4KkXNJZPXtoLUF2egfxDD-onIp1D-llFPygWIAmM9lkZVc6UKkzd2VBfWR8TaQNB-kTCdPef04DXVpQ22nAd5D5o5xf9Bl4PnTzS-w4AlliaVyiHhyWY0rxECUhwpxa6-6zoqIOqtrrMBMZRJeGZJ5PC1MnA3_M7iAjNQkXpUmdnXZAH33DRqIjaOh6XzvAKTkdbluFNKaq08d0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26275" target="_blank">📅 09:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26273">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZVNy12ewHbhCUdaC1vp6SCeub9gkDCqyO8dxvnt-_DtLIPhRzALXi7wkfaqM9DIqwhW3JcKXAIPDCBt0svN3T-nJHG7fUSGWSHtx6Hhx1g0YN3cq-1p4PCpaFn9XGkAtS3HsZ90abq0vTz8OAzjbWEHMe7gOsN-I8NU5yB-N2eEwFBy2dg_td3dpdvb4oOjcwaqPXUNGsbsLLleqXfVliM5bYJ_PiGWcBeO1iwvKFLcecYgYd1x4OH0wGfWe-QEWzZ3oUQDYbQxnSc8r3mifBqNhx7kqFqbNS2fVY6trjj1n-p7X0kr2prMcXQrw1zVK-sA6ImsNSBjQ4qcR108XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26273" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26272">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=CAvNzNLVKtv5m0czf3dwjpglNRex3Pmtr5wxgbDLbjsagTZN6vtm9ON1oQ_H8rLEMHAr2WMubGu0iQO9bcD4f4xlBrlq2Md3zaipE88OFsm7lN1dAQoLlhQhPihfmgptCqMWDcu1HjagGOXxLdCi_GxVKDGwv2JFynHK46N0swr6Z2lNaPuCakHgucURcezcO4twW5Qt-r7tX3axXBSLT11zMk5zv4JMR8jp28gfX-Tyv7NQfn8cVnQPz_4RLbgbe8v1D6NCvQ8_0atSiXaaZvvsvHZbzqS1zD3n9LCadKx31JbarmsIHDrPJmb5A8F_bAovp5tGA5nOx7Z2UNAnzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/955b39f6d5.mp4?token=CAvNzNLVKtv5m0czf3dwjpglNRex3Pmtr5wxgbDLbjsagTZN6vtm9ON1oQ_H8rLEMHAr2WMubGu0iQO9bcD4f4xlBrlq2Md3zaipE88OFsm7lN1dAQoLlhQhPihfmgptCqMWDcu1HjagGOXxLdCi_GxVKDGwv2JFynHK46N0swr6Z2lNaPuCakHgucURcezcO4twW5Qt-r7tX3axXBSLT11zMk5zv4JMR8jp28gfX-Tyv7NQfn8cVnQPz_4RLbgbe8v1D6NCvQ8_0atSiXaaZvvsvHZbzqS1zD3n9LCadKx31JbarmsIHDrPJmb5A8F_bAovp5tGA5nOx7Z2UNAnzYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پاسخ معنادار و جالب جواد کاظمیان به ادعای «بدشانس‌‌ترین‌نسل‌تاریخ» توسط بازیکنان تیم ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26272" target="_blank">📅 09:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26271">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZLYPVuCsc3uCwoLqVGll0Va_CyfcGCSof4WqclGwHbsi_uJT_zpKjZPwewZ4i6GI9yIjrWTWndvQ2668gjMVB4yZ3au1OJnMfykbp3PpsDUkJ3KnF62k9g9CuxHK3WRTDRAy-0LCn-ASkjYvZLP4ZIUnQXedXUiIhdsSWpu_hLRIAz6wG0XN57T5segytFSgDC_3uzNJtqaJb1T3zS4kZBN0p6OCiKlnVkjfyX_T_MGwWYXdp6MJ_bK9C8nurYuy-SG_bpJMNYo-iqMHW3u4HFgAphGVahf46jzDV-brlU9Cq6J82B6ZDNMSa5V4jbQid0X7bibdwLUiFXHpnsLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال در روز های گذشته مذاکرات مثبتی‌روبا مهدی گودرزی ستاره‌ جوان خیبر خرم آباد داشته و حتی‌ توافقاتی‌نیز بانماینده‌او برای آبی پوش کردن این‌ستاره‌داشته و حالاتنها توافق باباشگاه خیبر خرم آباد مونده. درصورتیکه‌ برای‌گرفتن رضایت نامه با‌خرم آبادی‌…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26271" target="_blank">📅 08:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26270">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=pe7Yqk-x4bIIFz4csY8y53VRcjgAmRAOJfDLda5wZ1C6fNMliSZ5THEIMM-_doAUxE9DxLjkl5TTPEl7ocSdgkcB107OyZvXyZ8DBGxlV0FmaPxwSJ_aKYMoK6KEWl6L5e1zIw7f61ijrucG9nr42TE7To6bJ2DcrMwQDjlpdcKz2q4HiCBE2LrljoBu8X-KiRlOi8sCzaPmBsxW_MMZqy3dvlN0gMUrZD1qb3RpUgfiI0y5mIaDJTN3nOBC1Ceq1RHHraEofQqXoxB7AD3qQ0XUpkxvXME7rcFV8vJRART0ywAnVY4Di6tBJ1TYDAkLwcoCwCvPjIn85Opf6HbnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab82c054c.mp4?token=pe7Yqk-x4bIIFz4csY8y53VRcjgAmRAOJfDLda5wZ1C6fNMliSZ5THEIMM-_doAUxE9DxLjkl5TTPEl7ocSdgkcB107OyZvXyZ8DBGxlV0FmaPxwSJ_aKYMoK6KEWl6L5e1zIw7f61ijrucG9nr42TE7To6bJ2DcrMwQDjlpdcKz2q4HiCBE2LrljoBu8X-KiRlOi8sCzaPmBsxW_MMZqy3dvlN0gMUrZD1qb3RpUgfiI0y5mIaDJTN3nOBC1Ceq1RHHraEofQqXoxB7AD3qQ0XUpkxvXME7rcFV8vJRART0ywAnVY4Di6tBJ1TYDAkLwcoCwCvPjIn85Opf6HbnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26270" target="_blank">📅 08:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26269">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5wlPFNd6oXaMHrDlYTIsb-mY62t29f3j-YlqfLJjTOB-cHjCgTV_TbWCXInmEUwuKGaRvzDTPREzSXfURdadlnnkcemCSEbILl6HjDtK4Wqh7umDkp53K-DaMU0kev8kJX_UApsf-w6ZV0xD0gJ7PwjwI7Zsx-liZwKSMN-Wu3t63MVbI4pRdiC-Z7sU5LKZ0y6-MDeu6egLY7AZmFb1E23sSpDoXfA2f-onNmcZvVtPD1UQyF7peAg8VVFLaHpfdPuf5Q00SqBMUrrbQYpr7dDXJFo8TejNIMoNcXNT7_O_fX0omghTIVaI5Uxc3TBmnMj4_--rGmTF3BIb2uW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ رودری تموم‌پیشنهادات منچسترسیتی برای تمدیدقرارداد ردکرده و منتظر آفر رسمی باشگاه رئال مادریده تابلافاصله پاسخ مثبت‌بدهد. پرز بزودی آفر رسمی میده... قرار داد فعلی رودری تابستان سال 2027 رسما به‌پایان‌میرسه و سیتی میخواد اگه قرار دادش رو نمدید نکنه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26269" target="_blank">📅 08:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26268">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM-QI07_J__erHYrL6HUiVqK3t3h-imqWtfCX-rqIrUW0BO3LJ5wRquREuA3sGeS5bD1rA2gFT08CqWxFu99f5e27edAw2B6CmYsVxwfitkqjeMaOCxAq4nN1oGi6EfLy-lfLGP8rsnp93ftVroIrcsgcE6pPmxNkmEMKW5N24Vn5LLwLA-02JYtgpOAFjvs9tvWz5YvsqeX-cRQNKFsOdEKgg0g3qkzOF_spIIl9Og7cMwhF6XnXSX0b4Urn9ATt1Uo0EyKDt690Y1bLzYSzU3LpCgqYzVUgGxmMYJA0y9mDNGat6OLzoiXfORCoEV77eKSX14C-w62gaBfdp2HQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ به‌ احتمال‌فراوان بعداز رونمایی از محمد خلیفه؛ باشگاه‌استقلال از مهدی گودرزی نیز در صورت‌توافق‌نهایی رونمایی خواهدکرد. گودرزی فصل گذشته یکی از موثرترین بازیکنان خیبر خرم آباد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26268" target="_blank">📅 07:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26267">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41630a748.mp4?token=sgj_hfKU9DUGJQB3koSEXAwXb0iXPTDCVDwCjoxITcjzhwdeh5ssKzjlk7hRPl3WTGtbSc-843j5CSBEc_4yXjD2uQZ8z9AXp0pG5tLAckKn1iAGkUqxXMG_m6qbsoP3-ezSxEhNvdsLazNxThZgpQ6eoU_wpRe6CKQ_fXJpIpbpZ95rWL5mjVm9lSBxEtyENEFmWMA6hlMQVDlwdiHPzRNgSlhDT3iI3UahmQDvwUeJ5TlvbSmdkTLt6bTA9QAkzt2lyWKP2wMayTCjNnwSWAAgFtsaQYs-wsk2AaZO-KhkjyrOsLwpEmxkZPXWKuySChEsIBpn0enCjabU6LcRwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41630a748.mp4?token=sgj_hfKU9DUGJQB3koSEXAwXb0iXPTDCVDwCjoxITcjzhwdeh5ssKzjlk7hRPl3WTGtbSc-843j5CSBEc_4yXjD2uQZ8z9AXp0pG5tLAckKn1iAGkUqxXMG_m6qbsoP3-ezSxEhNvdsLazNxThZgpQ6eoU_wpRe6CKQ_fXJpIpbpZ95rWL5mjVm9lSBxEtyENEFmWMA6hlMQVDlwdiHPzRNgSlhDT3iI3UahmQDvwUeJ5TlvbSmdkTLt6bTA9QAkzt2lyWKP2wMayTCjNnwSWAAgFtsaQYs-wsk2AaZO-KhkjyrOsLwpEmxkZPXWKuySChEsIBpn0enCjabU6LcRwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های رضارشیدپور مجری‌سابق صداوسیما در حمایت از عادل‌فردوسی‌پور در پی حواشی اخیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26267" target="_blank">📅 07:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26265">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKTEYnfYTKLEAqg3KzR5I4_CBeGQotohlBt4hRQVko0bPMmasvpnsqXHj5uq8Oow5p0D99W_gKf8tmVjcqYdEEcaGevIo6v0MNkX0bGOV2S67Gj0Pq2dDL84VMOYdPyZMKeMppTn5f4gcQY2UOztqviZbZpXnEW6fla6jPvXFGeR0aPtHmd9wLxNkkRgfxt2HKGFpu3ihWvtgTvqQx3oslrKqYbl0vly3PvVj1gILXW3HAOU6gPOJMsFAjhTqdQRxRBsv0TPADZUBApidkVJrUjg2GOw0OekOlp1DMBol5uRYD3O1Wx-mtEca_BDFOM_aDt9MeL2b2Fbry-xSCiflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCvQ50ZdPs3rJrFlZXzLwf_Jpm7xmx0y_9z35IIkq2sVjC9HWsBRI2ZQ8vX9t81wuPF52-chFR5pY46bqvVTcsW1KLJu1g7-mA5YKdeh3crIsIqpY1AY6vPk90_lH4a2XAq3Swvl4_cMgJxFR4fH860nEIVhhF3FD4LtaqFjRAgM0OIKPHsD8Vimlib_cDN4B2SULcdAf9C3d5ZBolLMDRoHuMPmmAyYXid2pBd-1-TRkhGZio1TDp_oNI0Gkh746_cqEO3TQJjoaDpZS2yv9IMp4-Jp330os0p_hMh11J5iRga6W_QP3p7Jy_5er_7rmgPxqSAAi-pARL3pk3lGrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اگه بخوام یه آماری از لیگ ملت‌های والیبال بدم بهتون؛ ایران بابازی‌که امروزجلوی ترکیه 3 -1 باخت درمجموع بین 12 بازی 9 بار باخت و 3 بار بُرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26265" target="_blank">📅 01:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26264">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-Ew5uGkTu5s-PSwI00O4msN0e3tfHAyrWzvGX0BPm6XmoMu6b1GNiI3jKZoHTEonpVQlbdqAhUZKImw5J0IVa4HR8gEAJZQfPCkb42gzqizyvnIWWH-EomoHEzx2CmDmqO242KIGr83CFxi2SNRGasHDspnpAV19sL13nVtWzxVFH_fMqvrh1LfYD_whwgDWK7315qG6abUl6LUV0cGPLG2HctAGvdrUCraf6SaDSgXDRHPtU32-UWBvWygYgCnXEHSKuOZOz4Q3EHUs2ccxGGAfUXywow60tGU34ir5CnZaD9pGOMU8BZxvDj0oRPKZof7K6H7Vje8s9c5az6xcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رامون آلوارز: بعد از ابراز تمایل شدید رودری به پیوستن به رئال‌مادرید؛ حالا پرز هم بعد از مشورت با مورینیو علاقمند به جذب این ستاره 30 ساله شده و بزودی آفر رسمی خود را برای او ارسال خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26264" target="_blank">📅 01:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26263">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=ES_y0fd_jz1ULZnr2UPbpl4wpbl--GzG6PjUeAY3XyX3YAcT6ZOtUHDNZxPwdXFoqklhbTdc-xqBpp8Tww5fj7qrlLlIMu-sEUl_1SlYwTRG3-yhKRXoC9dT3RmrlDQRNHUHuWXdP22eLZ0qrE9PhMQWIFbJrq-aB-XmzA0YWXzzzJshtYEsNGU5_Va6TVjz17yGBFbRO5xE_h0g_kmMu3pXKy8D0E9FOCyzu5y4VoQbxJs2Fwfj32SemQQpF9Nhka9bXyeck5zqeKxe5dguGh_805kWxkZg7DXUisYQL_t8G_sQTetlY6IrZlT6EAXXE6uKBC9AJouT465xf1xbkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6052d2abc7.mp4?token=ES_y0fd_jz1ULZnr2UPbpl4wpbl--GzG6PjUeAY3XyX3YAcT6ZOtUHDNZxPwdXFoqklhbTdc-xqBpp8Tww5fj7qrlLlIMu-sEUl_1SlYwTRG3-yhKRXoC9dT3RmrlDQRNHUHuWXdP22eLZ0qrE9PhMQWIFbJrq-aB-XmzA0YWXzzzJshtYEsNGU5_Va6TVjz17yGBFbRO5xE_h0g_kmMu3pXKy8D0E9FOCyzu5y4VoQbxJs2Fwfj32SemQQpF9Nhka9bXyeck5zqeKxe5dguGh_805kWxkZg7DXUisYQL_t8G_sQTetlY6IrZlT6EAXXE6uKBC9AJouT465xf1xbkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26263" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26262">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=BzWCbRqlqBcLLH1h0AMxXCaFcXHO5Q4PTuBzee0aBumRjaMBiqmsb3j30wbMeR85TzmpDembSncvzNF2pj5VtanRSknOMzqlPPBuONWhqtBcUH5tmVuS9nLTUdrce2WzWiztPk997LRYwe4CP9QKE4lx_B60bGD4izbg57GVTliBTHe1Jk23-FMjgPtVat7KZOHd_eniKqXf4X_MnMG079qBXu6Vxunp64NN8IEbNJapltxEL4hrRgUVL1jpR6qqLd6uvsJINd4NQtpJpxjtHtQIEMjA7o7rEfKO9jqAoSGEDpINo3jRrsZiE222-tvOUWTiOUA8MOej23xpPh34Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea272dc59.mp4?token=BzWCbRqlqBcLLH1h0AMxXCaFcXHO5Q4PTuBzee0aBumRjaMBiqmsb3j30wbMeR85TzmpDembSncvzNF2pj5VtanRSknOMzqlPPBuONWhqtBcUH5tmVuS9nLTUdrce2WzWiztPk997LRYwe4CP9QKE4lx_B60bGD4izbg57GVTliBTHe1Jk23-FMjgPtVat7KZOHd_eniKqXf4X_MnMG079qBXu6Vxunp64NN8IEbNJapltxEL4hrRgUVL1jpR6qqLd6uvsJINd4NQtpJpxjtHtQIEMjA7o7rEfKO9jqAoSGEDpINo3jRrsZiE222-tvOUWTiOUA8MOej23xpPh34Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بجای مانده از مسابقه فینال جام جهانی؛
لحظه بلند شدن کاپ نمادین این رقابت‌ها در وسط زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26262" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnsMc5xwQ2zTNs8Lqr3anvq8KdQDEu_pYIhMyIkixdx00V0tCuy9n7J-zBBW3T4OOZQOYC3JB7xgLv5R_TLgksYvIFK2RLsjt89Ej3spVpY15fgO-m8m0gKl63-d_nNKDyrCJ-9ER8r4nPoLS6egpDKs5CybC_uydnqOkUoQOSM4hF5BGW6lth0BA83qNSKMFtPfOlNDd1ntehazTdg2fLz6ftz69jdBnvhvLnBguzLb3KkwiRrTsgpriSbhOfo9oRWxCLsg7DI1vm8YM1D-fzGydwiNhji01z3F53FxjJs9Rjcwc17HJhmkeOFcycL--U5g5PyjlUkJ886nOcfV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26260" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47a31e55.mp4?token=C0vUxMbBti-P-onlrnutorbQojywm8GGwyMOESCbv2f4azaqdKlfT_lh-EQQp6Kl1C-oNmnEq9Uyz0IU5zS1Lfe7Bi05DPt1HDZjFyC9WzLwMtNKU5TNyHET9aa39cVcvQJ3sqNdtvyDIIlvBqFDSxGyl44tEO9g5wbFfRp4sxNvbBq3eqNIjbdxL3j7RHIOU468YZdSpaX91S7_jxGUsR38q0dRxbv41QTJapA-Ky-eu6aKJVWD5y-s-yXIOzQq1LgreUzFcuFtLVcHAuyw6BVQ-SDcV4Rc_ZODFqb-mjI5NQUaZN4RJlpVbJdnhAG8hpyXW7GsPn_rVE3ln30Kjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26259" target="_blank">📅 00:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8Kj2UdV1MK14eUM_QwMorv3vi-UHBzJCfV2iqh9Lr1FfG32LLwmsbB9AHhMRUDiJNFGHoeP2Kfc4trwL-dSIRAhX_Pkc2wF3gh1L68T3rI7psKVAeTW8kWT-6vE9oOIoEge6DXnOMsV_vxbqRaWINdadvcrq30_PI8wu7l-B5hSJn2Ih_c92wQp5dvN2Tfoi8Wuk-Ek6pQgZeDyv9gn24Cj6LdD9Wr6d0t5s2n6fO_km2IzLphhvNJU10yEel9nJWWKCp3mKyEQ3-pdGysFlkb-GAeXZu1EOYJeY_YtG8cBj2WskoMpWaYglEsd0bx_l8kes74nRrCSEpcvKnZQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26258" target="_blank">📅 00:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26257">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxjQBOzVyOqJ5dVCBznf_Z0qUqUuG0JH7m3ZiXssyf3zmez6OWEynd6VGczs-TWC5rrwXqk-UI_3AhcZFPrDQ3kEkstFB_tTmJfUpAlcIVzTvfsWNYdR1SFndpoTWWSMFQdKkeNehuBScB1UEz5Q926x16JK4PzBtRskBH9f9kQJ_19IHaIdW_VsugyeSY1bppQAHV_ATM7uesUa2B6gHGsC9vRDTqAlZKOE7fmUTBgScuQJzOZS_zXR3sOtO-kNiWLI4qX9SzuX8cvsOlrATP83SBFRMVBFMI_xKU1LzY78el_EAAnANHwXM9yGIjuO6s4pHpPilJExfkLhr8F7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26257" target="_blank">📅 00:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26256">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJPIW0F38-whcPbIR7mrbFokbcAywKaXyC10bpWaft46L33OVsx7meNG4aahHtXgUYYo7fLsL5RuSOd97cfXjqpLAyE7Kal9XZhjI_saWWqTykEssUsmyVKSJGkQyTsmIKEVL1NU3EJEGxdH2AxJmoYAXXFer-XVljUGAV2yPSODzl-7rInOnHjS0DhSEDFReyVaTi6QLjDJq00jYCmCPTZes-konqab1lskm7uanZK5h5wh8uu81fpvmX9B3PsoyD1s9s2ohatr4zFBmoYQV1UMY9uzGGFRTWiimSU3hDl6i8simJgsgv3jwQWwB30DQeSGkJ6NUlJMOsqlUwqD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ محمد رضا آزادی که یک‌فصل‌دیگر با استقلال قرارداد داره برای جدایی‌‌ازتیم‌ خواستاردریافت 20 میلیاردتومان شده. آزادی درلیست‌‌خروج بختیاری‌زاده قرارگرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26256" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26255">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPWN9928nxTwdUqA21wN3_J7sI9QTW43AQthOhLLJGbjEGxx9Cjy9UFMXMuhO69OrRm5WvG059RIFghx4-8z-vVBa0p5YwGRqU30zXc0-sVuA5-4Jybx5j9MEyWnlkIfkswZZHiS6e9WAbs0nphkFCHZqXye1s-u6Zh0YMAby4zEOd3q5WG-MryjnxJoGYjQPVJY1R52q7ycr6rpIlfts-TKx8JLJ1pgHcaXIyhcEHVoEgWsH1AQckdxZQH_rboRQs-NqhXDjLIBwhGwcR-GUv_GDSIiwGTXzmIlFvOLGdfwsXceE4asqQmVmiEL7wtGb5xt5LsjUP65PPZTD82HnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه کاور EA FC27
؛ نوجوان و جوان ایرانی باید ۱۱۰ تا دلار ۱۹۰ هزار تومنی برای خرید این بازی خرج‌کنه. تازه‌اگه‌فقط بخواد آفلاین بازیش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26255" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26254">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUEUlzevl4iUXt5ubwwiZW8WUNdTpuCD6DE1VZzvqqtjGa-01K_V7XJGK6C-1zge0dkPLwNpbFfk0xzA5K5y4JEbctwUvTm1vBJx9fCnirz8MdLMYXXNLZe8TQ202r77634LaKKZo7YnqfcjT-LzRbYwM3hmq7IMnxLZp2zpvlTGXBlgj1FSwlmWVPRLLUDuU7miW8dmON2dYPbPVctpI_vfN03tQBWKpeCnn8reYlo_d_RxpI_3vT_ExmmcEdaSQYq3lJLAP_2Ggb4clbWb6pdw62PXYDIz_AUonz-FUh5lCyKr5j_wkjJTV64EpvFoogcyzZRc3oG5iiy95vGQCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26254" target="_blank">📅 23:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26252">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=AYCFcb7so2TlJCfEUz0GF9PHoszpWoA54FWk3VseNriNnih6ynciDSLpKsvrHyp4gF7IPnkvAJWbsBNJiD2YowtVX7w8Y_LcXpflXxVJXF1dwPJ1ARrotvJ4LSeydNcrL5vBkVD82sSe_Apr_0mdo1PebqWRslKNzAnStSV0zNGAUBEymNfHLgrvohgnpdQE_YOwPN_5Wwtj8farPTnUYWltbUOh4l46BVL6vqI0CYBU3Yxj3uOPRVYtBIh4v8fOzDnwKQ0CWAz-YrM2t3QuYwZhbzyrTDyKDeHdLRPCSY40njo3LbR1PQ2FjGiEm8YScYZU6bOk64eUUqgATRJsQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42bce1c0ee.mp4?token=AYCFcb7so2TlJCfEUz0GF9PHoszpWoA54FWk3VseNriNnih6ynciDSLpKsvrHyp4gF7IPnkvAJWbsBNJiD2YowtVX7w8Y_LcXpflXxVJXF1dwPJ1ARrotvJ4LSeydNcrL5vBkVD82sSe_Apr_0mdo1PebqWRslKNzAnStSV0zNGAUBEymNfHLgrvohgnpdQE_YOwPN_5Wwtj8farPTnUYWltbUOh4l46BVL6vqI0CYBU3Yxj3uOPRVYtBIh4v8fOzDnwKQ0CWAz-YrM2t3QuYwZhbzyrTDyKDeHdLRPCSY40njo3LbR1PQ2FjGiEm8YScYZU6bOk64eUUqgATRJsQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوجذاب ساخته‌شده از هوش مصنوعی؛ خوندن عو عو برای عمو ها این بار با حضور لئو مسی فوف ستاره آرژانتینی فوتبال جهان.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26252" target="_blank">📅 23:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26251">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=eeXCYa_9GlXfa2HAE409ZIpNslXvTwVJz50gpgRrKCl8rWtWnGqkRXuAuPuS0-Sk3PqLkv5IzmGs-jRUxKixcSvk1l2zg1x2cbJOszxMDAyI_eyxgUENCoPSlJKIJESF7IsIwpE2KQm5gbe-y-jFps2lTKHlTmnqtb9_m1YTchLakM5lQ_J4t2Y5GQxu9Vgc6JMgcOHrLHWhE5vXtOfiiIT_hj1UeI7uNOxqdGyq01ipboDitaEgORgMjTEZPlHylXSzJMEjxFqTBzEIbDoexotXJT3dyJYaEMWCbrCELCHGVEhdcy_IslZGgrAMC0DVG7GqWcUXfZHgPQxpFNvlJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b149394bb5.mp4?token=eeXCYa_9GlXfa2HAE409ZIpNslXvTwVJz50gpgRrKCl8rWtWnGqkRXuAuPuS0-Sk3PqLkv5IzmGs-jRUxKixcSvk1l2zg1x2cbJOszxMDAyI_eyxgUENCoPSlJKIJESF7IsIwpE2KQm5gbe-y-jFps2lTKHlTmnqtb9_m1YTchLakM5lQ_J4t2Y5GQxu9Vgc6JMgcOHrLHWhE5vXtOfiiIT_hj1UeI7uNOxqdGyq01ipboDitaEgORgMjTEZPlHylXSzJMEjxFqTBzEIbDoexotXJT3dyJYaEMWCbrCELCHGVEhdcy_IslZGgrAMC0DVG7GqWcUXfZHgPQxpFNvlJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو آخرین قسمت‌ویژه برنامه جام؛ خداداد عزیزی وسط عذرخواهی از خیابانی با خیابانی دعواش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26251" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFANXUm04LlT-gxEevZWZUiNSKk8nmkvjpsLBXDO60arp0lFJmyzI3REZqbZXJ44U8UGUrLYbopl8Bm2zpV-HlikqYg4xBGWZlVSv1Wzv26NifSOLMQ7qNwWxMb9ncLgTYaD_I6vo9WMen1S-wOmAzTQZ4bKfb-96KxjlUkx1AlTmrUBMU-zQ6enZRI6rAW8IXK0HhjGuMyg0qASWGrvj9jb8pwz3BW1A1TG2i9rsyfD5Pikp6dgxQF9bdKMrZH3ZY0BBTOUeZlIUxuV_jXC-_jIaLdN9dUgf7br65GzuQFUnPixsBp1RtlIxtAKmdsIXf0_0bBvI217Ag6bEj66SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ویدیو باشگاه استقلال که به استقبال رونمایی از محمد خلیفه گلر شماره یک جدید خود میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26250" target="_blank">📅 22:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=j-6f0Vu9LWdjCEQ6BxAYmimSen1MATCIT1hfZGrxRCdw34Sy6ZF46bl-QYvAL7-j2jNXglcr2I7p-u38tNzqy1N62Qo6APujEe1AyuD4VWr0-hqQoCXGWnj-Jlm33f8ACMwV6UHkA-Rbtsg0v_CGLpVy0I2FbIZ4WHyCHvVski5uaO1Rt8wC_o1ZCuK75RNMPx1RDhDvISS8ptwGJxTeX2c2hLWsOTqVAAw7xY5fSXIDsLTb1HVVMTANHphj04sUkKn5k0Gdi0jIxYVQ2UbVaHwDqPN3wjNjNQ5Lg_klGIkFZbE1p-6GSA03uPd4GpSbL7bz4TgkkDlB6XnTcQr0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1e4b083.mp4?token=j-6f0Vu9LWdjCEQ6BxAYmimSen1MATCIT1hfZGrxRCdw34Sy6ZF46bl-QYvAL7-j2jNXglcr2I7p-u38tNzqy1N62Qo6APujEe1AyuD4VWr0-hqQoCXGWnj-Jlm33f8ACMwV6UHkA-Rbtsg0v_CGLpVy0I2FbIZ4WHyCHvVski5uaO1Rt8wC_o1ZCuK75RNMPx1RDhDvISS8ptwGJxTeX2c2hLWsOTqVAAw7xY5fSXIDsLTb1HVVMTANHphj04sUkKn5k0Gdi0jIxYVQ2UbVaHwDqPN3wjNjNQ5Lg_klGIkFZbE1p-6GSA03uPd4GpSbL7bz4TgkkDlB6XnTcQr0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم!
آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا با وجود خطـ..ـر ابتلا، دو شیفت دوشیفت توی بیمارستان‌میموندکه‌انسان‌های بیشتری رو نجات بده.. «ایثار» رواون‌آتش‌نشانی کرد که برای نجات آدما وارد پلاسکوی درحال‌سوختن شد و دیگه هیچوقت برنگشت‌ آره برادر؛ نه تویی که ۱۴۰ میلیارد تومان فقط پاداش گرفتی. حرف نزنی نمیگن لاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26249" target="_blank">📅 22:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8899308b74.mp4?token=CNBUUrS2AHUR4ajPT-AN5JuPDPuuROucyZxMgN4_7twIMMp4iWkuEWThE1UPcSzZUKSvUUeNAx9Lp466gEccBnpUJgEajanH31oNo2-MBmgIwNwivPF2P75ch-rhBhE_YSEK40lrLRr3PqOmS9WvLOOV5QvibMDagqfLlFfKP9FkKE7hgdLoBPmEfz3hT4tf5lowvIEeMRepdFFru4bdeha8jXzzbJQyyYfKujl8vk7eBg--g5kpnJUwise7ncd4bx_l0fUexa1-_x43aF60AGlr4xnCRSFTuKOS2TII-M6sQkvHvQYVe9Y44sk1vJzvLFed-8oY8TnLV2CB2ZdbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8899308b74.mp4?token=CNBUUrS2AHUR4ajPT-AN5JuPDPuuROucyZxMgN4_7twIMMp4iWkuEWThE1UPcSzZUKSvUUeNAx9Lp466gEccBnpUJgEajanH31oNo2-MBmgIwNwivPF2P75ch-rhBhE_YSEK40lrLRr3PqOmS9WvLOOV5QvibMDagqfLlFfKP9FkKE7hgdLoBPmEfz3hT4tf5lowvIEeMRepdFFru4bdeha8jXzzbJQyyYfKujl8vk7eBg--g5kpnJUwise7ncd4bx_l0fUexa1-_x43aF60AGlr4xnCRSFTuKOS2TII-M6sQkvHvQYVe9Y44sk1vJzvLFed-8oY8TnLV2CB2ZdbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛ برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26248" target="_blank">📅 22:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26247">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq2nGF0m-YmkR41QU749L2Xc25VQQQ_gHCMGOvLoxgsOmcNhWFDl44jD-M9_MwsvbuOF_DN3PlfWqEJCKU9ymS5VV0XcVSPt2WoP6S9G-AdaSCzD_nBUwPeOGpbP3JcDjJCoRRQdM-nx9xZTymeUfguHR_iE0AWwkoJwGCVdIwtDOR1KTf82YcOtyERn1RFMcXw5RkoHDWCLh8qvFpEsHsd7h-rbGF_W7FeLrjXQRbyweezkb-upDMd7JxXeEZTGiYVWa5U1kJjPMNTdy9TPXeB_4P_9-a6UvRV7X6J0WZLe2wjjkgJB__YgG2JbYR_Gy5vDF7iS4hOGfubpN03ApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ویژه برنامه‌ های اینترنتی جام جهانی؛
برنامه عادل با اختلاف در صدر جدول پر ببینده‌ ترینا قرار گرفت. مردم‌خودشون‌انتخاب‌میکنند. با فیلتر کردن نه‌تنها چیزی درست نمیشه محبوبیت بیشتر میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26247" target="_blank">📅 21:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXZc9CK0Mf-2Dk4tuq9Yiu9ZWuB8oa1f8iJoTabX8UxZ_luf4yyoZpcwrvpTcEqI2sx7EMxnec6RWsf2K1-V5ilQQtubfmLC7TIrd0URcQT7WNr8vFZ-7Tkqm60YVuGJXSD7Gseq7az2q_Rmd-dZPSk2cne_TitnXNDTVsCA9Gay659SKrjBAFInAgFunKI37uAD5IXXJYJmcxQ_THjI1pdKbfBMw3ZpmCL9EphRG5MRz0ELkiTEu1kbJASgy0uhM_7CEmKU0-IdQYQn3yRdL5H4a9TCoQEakYAkeFRRbq4cxtl7KKYuPNuNfL2YboPZ3DA8gOBqVY2UD5e-um20QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متاسفانه توی همدان بعداز شکست لیونل مسی و آرژانتین توی فینال جام جهانی، یه پسر نوجوون نتونست طاقت دیدن اشکای لئو مسی رو بیاره و از شدت ناراحتی ایست قلبی کرد و درجا فوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26246" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JofWJjArqP1YDxuDcTAPGox2bpaABfG9Ka4ANM7so5G4RPaFZAu541oNV9y6Tj77mi0UgWJPrj0rpvjN9mySQcVlgxl8ZOKk3K4wHVaBPcY7V5opOsukl-cwcNawmVR7_n5G1ZN2wahG8a3pT0TAOAjLvvlpKnRvHRmhqGRg37WFo9_qspPIrGGxZbe1U_8-rcNszthK8tyDp68-u4X4RtSa4kyP8OlvT4bk8xdhypIqWWSshDuXKMoadxVLWyZmT0UbvI2qltWUKV0jXfpYbTtSuIaWSGbGYRL6jtpTbVd6k6CaJs5Emyja4un2Ay5naiu7X2a-12luXezbbW-5eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
نشریه گاتزتا در خبری فوری؛ لوکا مودریچ فوق ستاره 40 ساله‌کروات‌سابق رئال مادرید و آث میلان تصمیم به خداحافظی از دنیای فوتبال گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26245" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26244">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=Lc9MXcxI0kuyTr-seUEZen4cZuOWKHii2yvxAaoR5Sw0yvMlzAbXNU0mRkBrDKCuOdadsWmeilyDOuBwZlQCQetC-FDdL5Ac9FS_E_2wC8DWO35VZQI4Rb83OUXX_XpJyfJMr9DDbvR_NsacOF15gxBkm3KlUSIUxrs69pH4QJ6k8DBmSced2kGzk9ZGWRSsQHaIivnjm0VsfBznDg2ZHElzXFEbYrygw47O3z2SW3j_lc_vDOGQGPGj-mmmw7ISOpJ4kXr0tfF1NudmXCjH5iqy1SrBu2NP6NcjDB2GuOwJFG1jmGxofGhCKtrFOinBeAV2D6Btb5zTbN4zibu8HFNUKNlhOJ2S8kl-9Tw7UTTzWQV745QlY4h0RloI4of3A164Y0t25NItBRedJ7G6P1QIQfPgq86vuq8qgZZRgDxE2EEFS1DP6y8dwjh427XCcqMLFd-seDz2hSMARqD4fbpjD3PH4JJqTuzubMaB5qXhLjU58_CRd9exJmWyyLXzYKwKUxJwQOd6eJY5ssdT_vEaZOeFW3niMBqnaRtZ6BnljP7wcCk74Xhe273vyVeVHJLD4HuvsoaEwAk2K0xbeycncspEJ0pKQycWjkwwJ5SGFMxEbLUFSVU9Uf3qoYCZKohRevlp-fjVXY6emfmQwr4M21ngo1g2N0fqMJpUM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/512d886ac4.mp4?token=Lc9MXcxI0kuyTr-seUEZen4cZuOWKHii2yvxAaoR5Sw0yvMlzAbXNU0mRkBrDKCuOdadsWmeilyDOuBwZlQCQetC-FDdL5Ac9FS_E_2wC8DWO35VZQI4Rb83OUXX_XpJyfJMr9DDbvR_NsacOF15gxBkm3KlUSIUxrs69pH4QJ6k8DBmSced2kGzk9ZGWRSsQHaIivnjm0VsfBznDg2ZHElzXFEbYrygw47O3z2SW3j_lc_vDOGQGPGj-mmmw7ISOpJ4kXr0tfF1NudmXCjH5iqy1SrBu2NP6NcjDB2GuOwJFG1jmGxofGhCKtrFOinBeAV2D6Btb5zTbN4zibu8HFNUKNlhOJ2S8kl-9Tw7UTTzWQV745QlY4h0RloI4of3A164Y0t25NItBRedJ7G6P1QIQfPgq86vuq8qgZZRgDxE2EEFS1DP6y8dwjh427XCcqMLFd-seDz2hSMARqD4fbpjD3PH4JJqTuzubMaB5qXhLjU58_CRd9exJmWyyLXzYKwKUxJwQOd6eJY5ssdT_vEaZOeFW3niMBqnaRtZ6BnljP7wcCk74Xhe273vyVeVHJLD4HuvsoaEwAk2K0xbeycncspEJ0pKQycWjkwwJ5SGFMxEbLUFSVU9Uf3qoYCZKohRevlp-fjVXY6emfmQwr4M21ngo1g2N0fqMJpUM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26244" target="_blank">📅 20:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26243">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GINRtLBZtNAoswi8OQK6pTB6pi05ivX_wwHFlxLiW6-Ecay_Mreg5Mu1yINV7gF2JWegc0yyCS3oPXrD_r0MRRtHskItluKTG_-j03QZyPbJvdDhPmnMA1mbLSw2bODon5AKIFwHi8He0yQBA_tkl3E00vPRiUNr8q1p5OtZ01frhw2z8XC9f01Tg19Eg9EZiLkZ37N1IJKQl-KKyiJsfS0tqA_sGzhzieOxn2agnENlQHg-IbMkj0lKQ1fwOSfmj5YshYxy_btONLed3pw4a98syOwj1JmZZu20v9f3GbOTosUSDSu_jTRpheSN7ccF5AR3Uu7wjN7zTk_qyD6ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26243" target="_blank">📅 20:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHW8GGP38B_KS4_NtWIAGywr2Jdwbr3cD9CfeXsseRGvutYV2Ql2iTDybCKMfo9ncnRZoP5jcpwlBj338QCW81VosNsm90V1BMutnGQ7ffJlczXSr2PYguwntZh_WpSHnOzg7XzlKSLvk-nXBnSzNzEGrYu98goWCL0gJl8m56vN-fSbfRr_T5d835r78CHppBHXEwfaiktkead8g-U1iBHmI1el9ATrz1quQfIk3yMwI3j1dr0uKi4SrZxFrWefXveHpxzEdAodDICg5KUWtLClUZB_Jo2dmXDbnagcE_0YWlKER0roXXEt9Y3gL21G6nPjwKImaXprhyMD-k6SPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رامین رضاییان ستاره آبی‌ها ظرف امروز یا فردا راهی‌ساختمان‌باشگاه استقلال تا تکلیف نهایی‌اش مشخص شود. اختلاف مالی بین طرفین بر طرف شود رضاییان در استقلال ماندنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26242" target="_blank">📅 20:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26241">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW4l_y6MKk0QuJDpem6zIyq5qa24Nlr4H_rlso4iTLyMyODlsThj5E75nDCoIc-xuZcdWNZDtqta78OuGjKQHqd55mvcvNCO-xnnprMXzzhF_LMObj4AifEMyKwKC3rSaUIsYaG9hoK3EjOBpHTJX-7rK73dnLxkpLFBvSnmyM6lbE7NXBmjddVTdvMjLw4EzIgttGMyEJgHiD8-g6UX3EvOE6yhLvNfjz5cmjrxNTBwHQU7IvC9cixcQQDH5OSkU8o7x1rY0bLHIFj7Hn8HH5VqjiwegFA-sJcPsfXjLWZGIWtAsZuLthcKrZkyMW0NaO86zqS33gJjgCNYoTFbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26241" target="_blank">📅 19:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26240">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGdZwQXGJ67hlaSaQzG-O9dyiqu8DdZZinAB_wdktvBo0kt0tRHZmktcqh73cSH65qR4PBBgyM_6GlcfigmMD8_mZgQOP_fOyOi70sSZGB4hBVcQwO8jKDE62fpzwFoRAKhVaBM03VA0gTFnwi9v1F1M4qDMo396cGIgAobR2HQ8CcI3tMRmYxBnFk-bGVeDNQS806449sc0DDEHXzBOXC8VBOUc0jx9JzdqE1KB87eYsxKVcuqZW6WRD56yl2Nd8Yf_zRpg86Vow0crELyf8qYaQ2kolF_Lu_uE92Ne_6Vq64ieqQTDNAIqxIcEvSGr90SkNqtAdvO08DerMGznBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26240" target="_blank">📅 19:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26239">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehoCIYnEa1LSI_wtpIkbezcK3wTcEt4HB-yGzzQkUke-lFg6HU_xG49NYh9TtiQ7wb5fjRvNwy9ZikWLv8WyRqu2ApJd58VxZaSR15qqbd9mPhxJVaJsQ-7NYIMGgPrmRevORfxXyoZ4xVok5bvAkulaQgusVSOWq-5MQMz6GTSD09h-XPypMVWQxbx3_uYFtg5dMAIEwknBlBQmHzUGh4q8RQ1K_3G6AyLh32iFyPjD7uCtJLuDn6YkFg9lMHOMeKPCI8fr-sgw8wKGCojxI_9oGfTEAztQGpkQdAI63Pqz_2bfrpKBoMHcnJVX8Fh_iSZCZrgwHIY6d75bDsjIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تیم پرسپولیس امروز عصر در بازی دوستانه بادرخشش مهدی تیکدری 2 بر 0 از سد خیبر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26239" target="_blank">📅 19:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26238">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=gbHP-vHTpSPnF0n8y0jISvLIlIivmZMYtCuOnJ5iM01NCOURdlSQZzHVSh4kt9tEsGVAicQtbxanRYgJc33CyX9H4BqgLRxYWgeZ4IwePsU2yqmfkHl3wdA9zUqLEuOuGjvGrrQv8gEOUOb5lBL_hkmR5g2ozj-2FW5jY-ohpSkHnidAkFpwnq6hPb7Q1FDDn7rghmWwP-zvjBYmT2wWawxuMXVIvt1oaGKc8z-fnGuGVdy10PMh3_dCTRZy9xj5WUjwqGYjD8dKIuQguOo3t2ssMumjo_jMQo_-aiOQYRn_71QFOgQrH7LP0oF7FR7NX_ao_WRhNwYI3jOX5MOlfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe98fee7a.mp4?token=gbHP-vHTpSPnF0n8y0jISvLIlIivmZMYtCuOnJ5iM01NCOURdlSQZzHVSh4kt9tEsGVAicQtbxanRYgJc33CyX9H4BqgLRxYWgeZ4IwePsU2yqmfkHl3wdA9zUqLEuOuGjvGrrQv8gEOUOb5lBL_hkmR5g2ozj-2FW5jY-ohpSkHnidAkFpwnq6hPb7Q1FDDn7rghmWwP-zvjBYmT2wWawxuMXVIvt1oaGKc8z-fnGuGVdy10PMh3_dCTRZy9xj5WUjwqGYjD8dKIuQguOo3t2ssMumjo_jMQo_-aiOQYRn_71QFOgQrH7LP0oF7FR7NX_ao_WRhNwYI3jOX5MOlfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین: بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26238" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0SL6IA_p_zhOlViHTLGbKrl3fzIDegCmql7JwBz7OZ3WXc9fvr_WGwvcJEvws94Sln6X5bZCOkj5nz5gDZ7sdJ-CsIaeW3IR2CO_lTLlaymsbRBv_2oNT7tORIycUc5K-b_FbvMkJaYHZjZIJcQgRHkWfdiOZ9eUNgo4RvxJZPaKxvfJqy1vK1PnQ3FaRqdB4RqeaM4ZP4y9ALz-hfKXNBkF9JOtYBaSLLoecqhAVNofY3mp1R7fwpqA2farhFWo4JkUIixaOwJXUD9PXvWn8dSCUF_c3G1moy8sbE6OkWMf_bDk4Jf4K5BEUrVsVM6B4aHLnfp-yzGJeLyWmMWxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26237" target="_blank">📅 19:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26236">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFBWcNBKe0FFmmMo9a1fcTw9tGtcDdzCOeoVe-431xUnQlmoE-fnS02MHOygTIs2kWTVZIaXAnm6WMQGVSXrKqnx12rb2QblVAf85rlR4E3gWtXGEu9x5j8qM1B6I6tIzX4FKO0YgaTYQikkrUkc_UZoEj2bNsMMYaUBqGymj9-Li3eeUxHsd6FqVz7mTAhwiMH8Z9T3dQrLvJf8Qti7Juz7RXMWzQQihq-XzWfbnETizNvd0qf1KPQWH-rJqp2AOCUIVptHc6pwebAuYaosluH5aQXIAlmTtzdTNtE9upo-IWZEOf08DHZoqLy0QRBqZLR0uhj8RqwtLmSvk3kQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26236" target="_blank">📅 19:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26235">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBuYf2fUQLihL66TPpxcuboFkCeiz8htMpNNGsH8a3R3LKOrloC23IdS8ej2VKl0WF73VYamtsNpFg8a9Uouk1v1BjfFgrnohOByew5JscukSPCxwiob4spqnxvFB9rg3vPIbJ77ul5Kp6HkURcC2MOizfn4BpFo3BmbIf6iZtAFn9B4HRROlNXAdwPUZ8PXJMmF0s2iUwWx4ZTsxW3BWdM5bg5CJizFlQM3vwE42zieoEXS3GHwpRagybVSDBgd5uy61goKvldhnJ89HkdRrG667y_f3cJ-ugW2AFnZMEOpHjx4M3m8YSVtu8TLUjhltP1xL2Z9HOu4bonKSs3MqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه پرسپولیس دو هفته پیش با ارسال نامه ای خواستار جذب فرهان جعفری هافبک تهاجمی 20 ساله ملوان‌انزلی‌شد که‌درکانال گفتیم. باشگاه با خودِ جعفری به‌ توافق رسیده و توافق با ملوان باقی مانده که باتوجه به‌فشار بازیکن به باشگاه در روزهای آینده رضایت‌نامه این…</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26235" target="_blank">📅 19:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26234">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59137224b2.mp4?token=V-Ug7xxsNwn15baMg1SbVSt3NE8ynUwFdJPH_PPtLPIJbtDHzaDCagHubpe4P-8mW5WnnqggMOvAnm8mzPg4-_-L5fF2eWehRf24waSn5FS9LnfVCH6IRs786UCZ-PkLmxX_Fg0a1adneGXTW-4x6ZYaiwN9lKtlvtd3AYXpag3CpUo5rprgbZWmyt-u-I6pZfFoWgRzMlW8EZSb9AGoP_uItB7eeSf-nIU1RT1aHhpzeecrIiVxEvlduDy__2vVUIUyAOsSvDn10MGsMUObL8AB2Z8xz12V8GRgBtTqXOjmERwVGn-9xgSkPf1Lv_uk3E-OVbl1-M7HsTcOEgCyeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59137224b2.mp4?token=V-Ug7xxsNwn15baMg1SbVSt3NE8ynUwFdJPH_PPtLPIJbtDHzaDCagHubpe4P-8mW5WnnqggMOvAnm8mzPg4-_-L5fF2eWehRf24waSn5FS9LnfVCH6IRs786UCZ-PkLmxX_Fg0a1adneGXTW-4x6ZYaiwN9lKtlvtd3AYXpag3CpUo5rprgbZWmyt-u-I6pZfFoWgRzMlW8EZSb9AGoP_uItB7eeSf-nIU1RT1aHhpzeecrIiVxEvlduDy__2vVUIUyAOsSvDn10MGsMUObL8AB2Z8xz12V8GRgBtTqXOjmERwVGn-9xgSkPf1Lv_uk3E-OVbl1-M7HsTcOEgCyeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
راز ساده‌ داشتن بدن خوب در کنار ورزش کردن مستمر؛ به‌هیچ‌عنوان سمت آمپول زدن نرید تا دلتون بخوادعوارض‌‌داره. مستمرتمرینت روبکن تغذیت هم خوب باشه بدن خودش یواش یواش میاد بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26234" target="_blank">📅 18:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26232">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJTopbJcqwHJ-_rRrG8rj24avDb7pfqws9hkTF4pYC_K_AbSJPYAljgiwP1enGlNKrKNSVVRdonLtqlBs0yp72lW2eodw315urrxLO1KhNUuBozIXrXGTE0MTJp8Iu4BrmvKiPkfkups1vaV5TctSwMCc71-ylz4i80C0nFAV4-OIpHhYsNoWBfuhSpP7CvyRp_hgd8TXe6gpZ1ZGTooVMqbD6kz-ZvATx01wixa8SvR9qIa_tCwAH1zBz28EKredNJ9eg4BojQVcgxJe4banNnjgh-BjpA7qB3PYCYAWbTDIgoqDVa5B91_rBOo4Q-MkEZ02Xkbr-K1SIvKEAiIAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZouJOM5LbRQ24IxPO1niGz1cOk_1xXvv0kD57OG7T_cWHxnnoAHRpuHZq1S5SijA4RmjF0SiBkXaB5k6aFzzSMsYk5-Y3aMC-q_dog3fUzr4EWYUp0sV2VG0ulo-T-4ScDRBlOizUzVi3QvAM0oDYsXYTWqilyPbxF1E7_LoX3ahkVYz3C2vxEmEr5AY5ErtX6PP6W1Afb9e1YomMGBdXvanzI42Hn2ghbx8kAcMTI_Jlct3iLMe8qjvbq8H-iAPezH2EerfmFv-rZf8-VWqE-6kiwBHFvcg0rDf-Am3TcaqoRnUWom07tBJTPqtQ34V_S9dG2iz5P0gPztDu3IDlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
نیوفیس وینیسیوس‌جونیورستاره برزیلی رئال مادرید درکنار پارتنرش؛ بعد از ترزیق ژل زاویه فک و چونه‌ اش خیلی خوب شده، اون غبغب‌های زیر چونش برداشته شده. فقط این ریشی که گذاشته‌ قیافش‌رو تغییر داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26232" target="_blank">📅 18:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26231">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNvJ0NYmRnaFPrNz13BuOrPh5ZKsTouzBkD--dgVVFJcujVQh-Wj-IQn4zGn2FhsB2x_vcJzuO4kVDNGqPX7EkTtbA0KePPz9BRCDHztEWZiN6jW9P1kCa_qqFC857IBsx3bbN7X_FMiPWcDCHF5mHxPm0Fgg7lUWl2BGaIh-fLrfrDOg063SVVVabKZk0iYuHcD4rP1xFvWFDrsF5T9UZFgichEdsVNy4AqE5oVy8TwH3CCWhbypketeZaMk5T7AvIwSiLnrM93ZFCTSbbmTJbm6hgvKPwPo08oQJ2TMqv2Y3jjEnfmHTtwHo_0rT9d9B1z-G-1mFw3NXrSspsUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تایید شد؛ با دستور مسئولان هلدینگ خلیج فارس؛ علاوه بر مجتبی فریدونی، محمود رضا بابایی نیز از هیات مدیره باشگاه استقلال رفتنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26231" target="_blank">📅 18:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26230">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtPa3zxk_V7J29lsDFZSEKRSGdyVqMqGFVcqFMJXutKqMm00l_yRC8G6Tc1X8oni4KUHVyrD0fB5XAn5oE2fVznaZhOaxxxY15U5g1D1vy6M_6etuiogY80e0mBi4wy4yvN070LbNYQZlq7WzHAv5LwDoGKDnQtuMnzdrBexg9Tbk1swrcoXo2ymB0cgb1Angrw3To8faU-RIuW6LD3S8-O4kwZQhkWVfvt8euqtsLyGP79EONZP2vBqG8VcROnQUd7drcd0dbIZ7H2O43INx7t46FR1U0SVmUxsdlgWjrzXBEm3IIrzvEQ6xYe_B3G-XDYvtsAn_NkzB8usInzGXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلر شش دوره‌اخیر جام جهانی؛ بوفون، کاسیاس، نویر، تیبو کورتوا، مارتینز و اونای سیمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26230" target="_blank">📅 17:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoZcJv17rAuUEr7BCqpvEf2_bqVfHW0lj9xVq2FvpZSbGY6ASKBlRLYM8YtPJ4YrT2WHcuM3FZXkNzUL9Cg1OTDGJUZjc_CHJIdP5TQMGhcIW8XNXdpEDz7eBvayI7vNSB6J6VDxUyO8CGo1UBda9Xn4sOtSmNYtXRwLByDlm05e5KEb0EXxzzJb0CnyyCBqLyJ-Vhan97joMns4QR8IpaLbGUXSVk3eCqIQNx6p1fRzMeFEzwDa_fhFptPbkAL7sMItrfUvaExyAbOCOZ1HswfBOtL6vbdfeAhkxgn3FsBiyI9enyb-bLP8H5rjYZcaL7le8NE_4V_wHYba3PwyZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت رده‌بندی فیفا پس از جام جهانی؛ سقوط ایران و صعود اسپانیایی‌ها در رنکینگ بندی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26229" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26228">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=vbP25m8skvm3vyU7iRfZkM7nbMJRXHQmmkGm7stxABZSiuJabuH3iajWcciyJ8q2kxmkCY_rPulWMrYlWNSFa4x5U1RfsVbUUg_aWVxoqItOvhjD0iNIDdxiNcXwc8COkHGEUEQcgn2rXDopDM4cCCC4-LRssxtcfWt9BJZOxp5am1RT-wQ3eRbaAAgT9jEuAbT12koI8fULSdL0h9NoMfFOtU4NFHB9YwobvUwB_UbCTpYWJqMkZB1gQKW44JXjTDsTlsdWVCT9rxG2jCJjeUWBRduw1rNdpOI7DrQpO1zoNvO8RjuhkSooVFwOZoMYkbrTYllQQT_9QM96FYpEEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3639cfb2fe.mp4?token=vbP25m8skvm3vyU7iRfZkM7nbMJRXHQmmkGm7stxABZSiuJabuH3iajWcciyJ8q2kxmkCY_rPulWMrYlWNSFa4x5U1RfsVbUUg_aWVxoqItOvhjD0iNIDdxiNcXwc8COkHGEUEQcgn2rXDopDM4cCCC4-LRssxtcfWt9BJZOxp5am1RT-wQ3eRbaAAgT9jEuAbT12koI8fULSdL0h9NoMfFOtU4NFHB9YwobvUwB_UbCTpYWJqMkZB1gQKW44JXjTDsTlsdWVCT9rxG2jCJjeUWBRduw1rNdpOI7DrQpO1zoNvO8RjuhkSooVFwOZoMYkbrTYllQQT_9QM96FYpEEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بعضی‌صحنه‌هاگل‌نیستن امابه‌اندازه یه قهرمانی ارزش دارن. دفع‌توپ‌کوبارسی تو دقیقه ۱۲۰ از همون لحظه‌ها بود؛ جایی که با یه اشتباه می‌تونست گل به خودی بزنه یا پنالتی بده، اما با خونسردی کامل توپ رو بیرون کشید. این فقط دفاع نیست، یه اثر هنریه.
و یادمون نره؛ فقط ۱۹ سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26228" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26227">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=Z4qCsHNdWNhZbK1_FHUbDbKPG5J2so4ELXr2dQuC8ZkjhV2ZaQkOSprsrC0U-OK8Xav7QbbbnQV_G071UANxQKP4xBewAUFjQ0A4hixFgIrm-2YwDaxBYdmiwh6cewXpLydJfSmSLcYwbmqrua_6Ujn4yJ7tlTvxlYqE6HExo0h_50-sVf_au0ZGboEFtudelRRTA8eeytPF8E_bO5i_Vt_rtmAs8xchWqME9z1NZN7LYvc6VwO3NOuUWLzOHedZaR_Gs20kzYPrgkuBwTLuG1xOhtI9P_hY4Q6FJ6L_vtPqT-FEe1yTMeX05ZjWUsRI3uQZvtsVeW_0B22AoPRhlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec8c45572.mp4?token=Z4qCsHNdWNhZbK1_FHUbDbKPG5J2so4ELXr2dQuC8ZkjhV2ZaQkOSprsrC0U-OK8Xav7QbbbnQV_G071UANxQKP4xBewAUFjQ0A4hixFgIrm-2YwDaxBYdmiwh6cewXpLydJfSmSLcYwbmqrua_6Ujn4yJ7tlTvxlYqE6HExo0h_50-sVf_au0ZGboEFtudelRRTA8eeytPF8E_bO5i_Vt_rtmAs8xchWqME9z1NZN7LYvc6VwO3NOuUWLzOHedZaR_Gs20kzYPrgkuBwTLuG1xOhtI9P_hY4Q6FJ6L_vtPqT-FEe1yTMeX05ZjWUsRI3uQZvtsVeW_0B22AoPRhlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکات عجیب لامین یامال ستاره 19 ساله تیم اسپانیا درجشن‌قهرمانی‌شب‌گذشته؛ چرا یهو کشیدی پایین؟ یه‌درصدتوپ‌طلابگیری میخوای چیکار کنی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26227" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=BdagGm93HNwQuiKCkX7-j1zZ9RFbGNpB8r4rzzwPBm5f4MwmLTyBCvrEA_ufS8qU6xCnR-xqMDNdgqzaDEsXycxVx_fIRc1TQXYvDsKLIPLzCXS72mUgimeCR_WZoT6o54KGzICoONL-DMHLLQBtQv-54eAqnoHaUnEBKGb-KaCozQ0madugOQyqKj0sxH8PyMdyw9VJqjnURizOZlbUMmxROyNUgOtoNuHLAjUdDznSNpxLgOzpPh83DONdBXEV3sh4h7S631pMIkxCwee3bu_eg4deBjpxw7gUwryius4D0oj_2xPxn9OX16R7bPc2wspsGji-lvmVKXQmOwXCsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b008c54e.mp4?token=BdagGm93HNwQuiKCkX7-j1zZ9RFbGNpB8r4rzzwPBm5f4MwmLTyBCvrEA_ufS8qU6xCnR-xqMDNdgqzaDEsXycxVx_fIRc1TQXYvDsKLIPLzCXS72mUgimeCR_WZoT6o54KGzICoONL-DMHLLQBtQv-54eAqnoHaUnEBKGb-KaCozQ0madugOQyqKj0sxH8PyMdyw9VJqjnURizOZlbUMmxROyNUgOtoNuHLAjUdDznSNpxLgOzpPh83DONdBXEV3sh4h7S631pMIkxCwee3bu_eg4deBjpxw7gUwryius4D0oj_2xPxn9OX16R7bPc2wspsGji-lvmVKXQmOwXCsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛قرارداد محمد خلیفه دروازه‌بان 21 ساله جدید استقلال پنج‌ساله امضا شده است. باشگاه بزودی پوستر رونمایی از خلیفه رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26225" target="_blank">📅 17:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b782IDNO4y9-3rrA8onqonsopvu4EW5YM4gQagI4VVUpabpCSCU1fpiviIPKpMl9Q6HuByWPUjWb4aUfy5HUvmgsugNJQiRzNjddbYia1BkP0zwKMR4SeHN_jLvr21wj3qKa0AyVoWqaPF59fY0MhVIB-MXik2UePO1FIwcJSHneaQ7j-y7XTdGJS3ashBWO81kk-W5Mt-fmTLGMtSR6c-gY42VXWH51PGCODfAJ-6G7ugJRMwFP-Dlg6DABahavLgHBei61vUoO8ClujWlvbCa2TI0_uzFhOtmKkpK6s6RmIspI217NnlpWWtuPYxwzxC4l40mnQ-JkqnejhhsLHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
◽️
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مجتبی حسینی سرمربی سابق‌تیم آلومینیوم اراک که در روزهای گذشته مذاکرات مثبتی رو با مدیران فجر سپاسی داشت. امشب بعد از جدایی رضا عنایتی از نساجی مدیریت این تیم با او تماس گرفته و صحبت‌ های مفصلی رو با او داشته. حسینی…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26224" target="_blank">📅 16:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26222">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SjPC-8RLAretzIjfGD467XxUFmKZjJ4cOqmW6KKRfzItrjZ6tU02Ss6fI5PHewhHVVJAt9lMPpee8S-ZRkjcLRiqK6bnsr7-w0zbYsMMjkx--oW2qX4bLX9GD5KvYgROri_4sP1H_aKutDZkGMbXptFN0wz1fceycoQN-Kuk9iU2v48kZ2c-Y3XzepLwbe6Svqlhh19xGEwHLOA56gV2OLbxWDUrMwU5zHECS07Y60RQnauqcIBW58IUf_Sl3lAhWHyhRYA2leTCUy8PkORgEHty133jMe6DdWpeBWKR02rbP1-3t4xjQlrhBBeNOg54mvzGy7ucU35PvG-GMz9Y_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAmu0hOt4sNM0-94yXnKYSrmTHSWUgtidAANVeeoFvDYybO30SJVE_keOlOLbD0_qdffxoFpGUJVo3cask1vWPdkTVF_mgqgtIbZTTNLENRbOXbVqJioXjc5YwU2572n6rSiiOiYF38xNzqVqBvLIXiPLhU0DEL_WnZcqbLyHn3xGMuG9ZilaLy4TYb6KhX44WvQqYW17Kxxdf1u2CwKC7FDAUbLFSaalCkzvCtmAoi5JyjpZehCblj7_XLPRpN1afEH30CbXA1WleXdaWCLa1kKKLflWr4ICfjLBHiGKQ1iaxwk2s6dHx4EaSGilUnWdQL_PrOOLM8c1YgxUY0WQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
خواننده‌های جشن قهرمانی تیم ملی اسپانیا بعد از موفقیت در تورنمنت بزرگ و ارزشمند جام جهانی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26222" target="_blank">📅 16:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26221">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxA9coCtndck4HiAx0ViNwgtyDkNVKYqBfkUN6ntzU6zCCetg9Cf71XsvnYG56HMHt_3l11D5lk2wB7DiTdrrGLsP-pZofg7xti8AC2PZL4E0-Xiy6xTBiK5FN4XMaq2oBa6Nxy83vLx7kUdLVYh0q7UA9l3oUHiWhjrHoPtDI481msLw3lSTQ_wCmpcLrWvG14VNp9Un4IpDzgxFsoOGp3g-nAJnxDh9Vtvy2MDWTR-fL6J6oSpgfmVYm0L0C7deHd4g6yUxe8mWn3U1YxeDh4v2vn_KzJZJcr7uVFBxdlfQZHkCyQQU2ONqGyQ5cmnI3gKFDCcWYG5ol1c5FkSHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26221" target="_blank">📅 16:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26220">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9mZH7MY4ORf6Epd4d6T5Y7p1XFXId1SQShOOKN2p8lFgsIgoyTdg2m4p1A5M7C1LTqXUoFZ2I6WU4jJzYN1WjKjKrtEVJJykjnusonCe0rNFfF3EJet4pCc7Qi9tHljm9KptH5rk7B2HSCdkeWb4rzEvw1C3qDJ9ukiKrZKazDyQnuDnN5Z9J_UXqsJf8gZu1Yrnk-ogFA2ngNmMgCHk5k_gp3MAmiYduNtPoBeh4euzmvJ5rhBPT6rqFausppsQFWZ0kLMnQzzmYiX_5sZmlXFdnNsipmVUm16zwFAbM3wlefL3lMwO3JIUdZI7X-a1ePMZVoIp8FoiOXCAKdpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
درحالی که با قهرمانی اسپانیا هیچ گزینه قاطعی برای کسب توپ طلا دیده نمیشود ، فرانس فوتبال در آخرین‌آپدیت‌خود درماه آپریل "عملکرد فردی در تمام مسابقات بزرگ و مهم" را جزو ملاک‌های مهم انتخاب برنده توپ طلا در سال جاری اعلام کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26220" target="_blank">📅 16:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26219">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzKxg5ajzGIqXC7eetRXQE4WtgxlFzZD8IEgtaWtgoVUSqbKfrxZOBxsYKfmkJ6JVDWC4DdKFoVlAS1EuYC7lcpiz6MZOoP_EwLZFTI0GfDlBvmzZjftFOPQndKRrHGR7cPp4ab4kgrPoqoSRzG-Ao-kJh-orGUFgEBX_A6h5DoDmOX2SdwT3hyQ082I4a4pZSrl4N_GmGmEYRwMwfFxUQqnMZ31XZ1-GDhb6qFJYeEBWOeK82Ex0U7pE9EjJ4orpBecEVFKg180E1CZ45KwEbBsyOKzKXLcWBRwC48bOGP1Zry5dfZBEnb9to0wTzL8Ln40YoWptw7kUzWMj4-lrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت‌های‌جام‌جهانی 2026 با 655 میلیون دلار جایزه نقدی، گران‌ترین دوره درتاریخ‌فوتبال شد. 50 میلیون دلار از این جایزه روفقط اسپانیایی‌ها بردن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26219" target="_blank">📅 16:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26218">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6LY2tpExrxsC2x97NdV4WFUL_tis4eXTnc9ayaEYLLcwwFfbX12CLKhQeVDn0PMw2cEWPBkJUzmDxMIR8_snJ-oQbGyQLzTofCIdIk9JWmUgbwW0uWR02_E7--ce2E-eH1z7kabWkrHT_fHUcSEqX_v_pms3_d4fmuGhaSGcM_GfFOn9YWxFl8OW3pof8NgVkhgWIoxcp0cHjBR1O8yMawInjPOFHpYH__8Hn2yZgisb78-sNlZTUXaovlkTbniA6AAzLGcXNSFpe40wdOf3zvCQgnLhBZBWqBjsRYP-_MxH_IPvpFjYNEiwdpWOsJvwwAiMRbFELWj8D7-2eMO8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
محرم نوید کیا سرمربی سپاهان؛ علی کریمی هافبک 32 ساله طلایی‌پوشان زاینده‌رود رو در لیست مازاد این تیم قرار داد و کریمی به زودی با حضور در ساختمان باشگاه قراردادش رو فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26218" target="_blank">📅 15:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26214">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvEISXDtld7VrhagewdOMJqdhkKiPZcmu9Pz8CS8qe3VzAEFVmhZmT-SxiZGiWAZY3vfPyz7dZ-oZ__tQouQjGHXp7TvBVUTXOd6IIvrUCkmcLVGBhtwA0F-K2hmn5E9ZTOwWBw_TS9ft_2HSHKBNNrog4JM6jjSw9ls4Izo3rjwMuG94dV3q-30OBMWwzY6m2G_bebATa47h2r_GnwRM-I401OWQjQVGw4W5yRYQN5k6ImbeuUYAoMgbpFIViQsCa2OLLuT7YBl7FZ73wRIBT1naYoyJWNKCjUIihypio-n7kvcUMaoE5fr9qib52c0MzQYtyzWYwb0G29g3aGvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری؛ رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26214" target="_blank">📅 15:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26213">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L94vnWqZSEN9HwOfjvbOYw1QVMcTllomJwEYO6dAcywJIzjox8a70xr3BWvkTPTaAWGl5wx40yTkbmmzt6cttQJvKjexl6mcCLBZOuOmqF-vtwA184dmdB7n1_dBYxKnjL4d8W9T66e6hGRQi-YUnbT-uLKUsH3bHZEl_2RRhJeORs_4pjgT9djNT-6rQx8M3e2HK2UxP3tbA_Kc8akpmxXF0fsmar2J8_GZrWb1jg6xqzQTv2jcpbVJGWhpn69Z6xPgi43-teqIgaHXsCEIIM0P1Rz87bWcLnhdBtgSyy9JFsgG1-kQdFd_k5DUkre9KXBWW20Ij6GLJ6Clsnbz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26213" target="_blank">📅 15:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26212">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1Ygrvevp3WBcOF8H0RKy8cub3KnAgE3UUfS6fFouG08HmpXp6XQtA4QScqpDBGRfMMJd6cViFi9SAmAiBwVVmvKzQ0I9x9DlQWXBmpFcs3WVTlTM8u1SMnDNt50BUWbbhc3k0vLVlIe4oaEfgbyVgYwRKNWAwRFZZxCUgjlOnSL8BBlYSzWEKHNUDp1hmtYL4jOrhGKl_ahDBAO9EqYPYerzTUfB_8KiipoPVT456gqYSx9DrI-N5dMLyjPbKwn-VsuXF_gr_9GyUpVODKyGuVL2BEBGaBt10lpzMRreSjsrQXixfXdd8HTaRTZZ0w-fbwSJJJ8fP7a89tcC91huQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26212" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26211">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8Ifc8mZUuF1s760LO5ygTgYyD1zxtuIQZNSIC36IuhJqtQDgj1ehjSe8T8p_dWwNeWEOZrVi3gJpup7rwrXkqvl3CLl_a-d3SP8oUXTOQAdBKBk07OHKo5RWLbswqAfz_lwl57kaMRH17v5b-fJ2fikHO_GnbodpTYWGxHlAKmf4Ox_Kdq8ZzPkc03RHcNtmqV6oracdI79hRasWRa5txeIJTNJGw0J4bsKccFDZDKwxq4xaC3hocAj0jiStp9dAztMdR9yO_-7OuuewVDS57pJKSuGlmFr8M1Zr-0126obE5PBY7lUM_RQ18s0RWjy3LEOC9yQPzZM-Eiq3s_dLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26211" target="_blank">📅 14:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26210">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8XdgpSkD4KCx0qpcYvUKPRJM5ZeMbxk6aceFAj8K3PXfJGCKfSkSuWvX31gJAPe22tqVzNR-QxkKsSG7rdVKoOSGaw-yw3BOTug7vQbI-4aRoou-D6OeO2JW2KBJ-yMRgRN26_kBPwqyvhePq1mXSClxqhTlz0G-UJCQzrv0BI01oWYohZco29n9WXNqNSLqEN_9u1jKuJSL8-TznyCKIybFtq_-FdfuVoCmMi5q-Y2qS_TlWRegnKWxcXPul4OdYKA7RiPQ9VXN9AcDnrkGk1ABcCjpgZuIDl3mePOk9DtL_fvWrDcU5SkEhs9YZ64_ycBLVW9CL_WNWOVXpdJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26210" target="_blank">📅 13:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26209">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZ9y33wqXqplWsUKCjM1T5hgwdupp1O51ghLWdz7DRft_JesL2GF-l6tyr1ifdiktbWpnC2QVio5n29jx_1QTfFbp41CEkAKujD8MiloOfk--sSC6efuZcFMHHHEh8J54oPxGul85I_6XjI9bYFyA_uQGUDoo7_aZw3nx-tt-TSqq0LPGlpGTd6B-ZXc3mig6mhMQLzuj95B-nyEV8nSmJEkqavj1Gc79LPD4xy8F9h4FFxf7mEZ2cqhI0QR_RghmK-ICOSdqS07Sdc-7mxzNTUzWzoaoffR9Q7zSRZ1gsLblttbSSE4jfj8OjG8fVJf7oTwYejrTpQtEbwBdSeb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوری
؛
رودری فوق ستاره 30 ساله تیم ملی اسپانیا و باشگاه‌منچسترسیتی که بعنوان بهترین بازیکن جام جهانی 2026 انتخاب شد آمادگی خود را برای عقدقرارداد چهار ساله با رئال مادرید اعلام کرده و به نزدیکانش گفته پرز بخواد میاد رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26209" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26208">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O51_gd9rse3R4IOxQK8IVB9u_utrzZ1KT5BBtKY2C4ZvUPRIXW5eTSAAACEKM5D0BZ6QcxEaWPP0cdJXH3fHkrD2830Sj_WUvf-XiF72t4z182jhuoRknDQyH175Nli3wPUXBQdx5lMNwH7Ip5MIJ23sgFBYSdXpL_C9xVY6cG3n9cYJ-bCyDIw4UXF9VpDvCK_Pdv1X6IynYYDeuuWt3QL7rRcUjY2VydmGziYSSoYxZ9pYgqZawcc63viDygWKLrVQL8lLzUjvtJCi3zeunf2tahGLlsLwEjRtTwHGwusedtYmmXAxue2E8QFW-6B4FvZnapYYqC9qgmlGZNPlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 10 روز پیش پرشیانا
🔵
بهرام گودرزی مدافع‌چپ‌فصل‌قبل آلومینیوم اراک باعقد قراردادی پنج ساله رسما به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26208" target="_blank">📅 13:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26207">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIcYF9lPQCTP1RhgsBSLFa2Pog7QhlA_gzQv9pWztpSnKca_InDfDQ_4VbwylswOkTqZ7loy-5YICfO_KP_A_i94Ua0RH1AhFPnXDwwNb3MilLS6cLUiZTGpbZjLYqIOCwkmMHhsWZWWPBheYp2IJUAN2WsEKgeEf6SnIRx4_9Bs5szXKRx5jy_TsaSEIUYkyXF8f4PoqdzPu06YL_985dbRf4OVsNgS4eLCzbOolvtgPgNYM_64o6tNhrtxouEvL1L9hCTOTDw2suzdJ6wFJ2qWCzqr-RDmhJi8e5GjNCS33Y9Sk55UOT1fWzfyw7HcSOy6sVFXDGsgsaMXwAcbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26207" target="_blank">📅 13:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26206">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwfedzAVq9TgzGTlnl1Z4vbII9TvddhdFIZ2MEOEGQknqFw2GWwBFp-0Arxxp0Popz31NuFNH-bxYcLle4APrs4vWIx5TPS0cE9tVvMzYZ7fE70ILp4kzsm3stvbG6jJhZo-E5NBwYzcPrE6XAyDZxI33bjJtchyEZ7pD5gOZIZVYOLGy4zdZN7OSy1YTjhmKgk4hg4ud19VC9kcJEERSjmzsCOEWmpZRQT8BtpeNvMEyE9IsJ1kPmOIT3kNTCXvNCbMBWhbSn7nH9TW1ojRukPB_O5y6OuhHXdrD3i6br4w_gbWh23ej9gBhgWM-HIsI4R6WSy5ZzhY7R4JGzK2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26206" target="_blank">📅 12:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26205">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwxt4NaYv1ViskZtNJ7bK62MQJNdQGrax31dbhW7UNct6MvqWQN6EUKiEIkr0Ptx-DHwJaar0HgObcPitFSGESY8BfspPJfFRVYSvgEAB92LiYDtm6N0ebv2AAovNmOL8ITE146qMNURVZOC4ffMzDIDHbfkI5H5gP8fZe9MbqjWYmpBo7-Lffd4VAY7YtF0DqaZFQewUscOdO4TLqM4nTVH086YkRlYvQu7G2vRK5wT34xDo_DfTgASa4KKNXredQoh6UOkib-8uoSSBonmsMVqRwsAhUQKVcBRT3pcDHlynoIamOvwiKXGX9iVwQNPzXTuKqysE4yh-Qg7sPlVZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سیدبندی فصل جدید لیگ‌نخبگان آسیا اعلام شد که در آن استقلال در سید نخست و تراکتور در سید سوم قراردارند. هر تیم با ۲ تیم هرسبد بازی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26205" target="_blank">📅 12:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26204">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">▶️
هایلایتی‌ازعملکرد بهرام‌گودرزی مدافع‌چپ جدید تیم استقلال در فصل گذشته رقابت‌ های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26204" target="_blank">📅 11:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26203">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-U-JN2JqtAuJwHkLavgxEVycLvIL516RLGWjluEMVZt50SGrvzrSFoc5wA-mWGOCS5Xhtmzfa-nIioC62GbQSilpkq8aLlXfKxKm_SbQuyCQIH7g-HJ8OMQs9SBqxRRavO3OJicwhb4hkyXsYd7CsgyO8If2GQDgg2cyeXDqZqoFdyoT78fVZQVHzJ2r-IE5qZlueQ_ZgSoUvUDB26S_BjrTddckDh3qg-T1UvQhrObGew1eiopoqX2786rrTypvMUAsa06QWCSxY63jQGaSdJVKK0XJ4_3SVTVkOBEOVNxo8mQ-D8sBdc_y103zgSaSGQx1PHxDqsVF36bO69mUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26203" target="_blank">📅 11:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26202">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=nLXNfFnHfzpv0MSaI18FF8SIxDFGptD0dg5Ii0L1lqeIkNQYb5MNiH2BMcPMrqZdzWhonkRbWNhna7XobFjyPjbeiljaTvNA2v9lCsM2Is59OpDo9trYVK2JFWdSxU6qOFAj-sIxxQIFt_lvjJ_LEMCPpLLAY06ESIa0AKYUTuQZTeHgMNyKV-coDqZjKOXrNNqAYUOqL3enfXyuSMpvcN-yFB9-phyTEpsIkoz9-IKPCaqb0WikZhbHopuR1OWPcbpfM3Q07gDSwIfYeK9FoSoa4ew6ndTRnhFLk50_qsMMBsQIJgAwhVDBbnKCK6SVcDKSvoZuZUrFYqC9_qZVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cc5dfc32.mp4?token=nLXNfFnHfzpv0MSaI18FF8SIxDFGptD0dg5Ii0L1lqeIkNQYb5MNiH2BMcPMrqZdzWhonkRbWNhna7XobFjyPjbeiljaTvNA2v9lCsM2Is59OpDo9trYVK2JFWdSxU6qOFAj-sIxxQIFt_lvjJ_LEMCPpLLAY06ESIa0AKYUTuQZTeHgMNyKV-coDqZjKOXrNNqAYUOqL3enfXyuSMpvcN-yFB9-phyTEpsIkoz9-IKPCaqb0WikZhbHopuR1OWPcbpfM3Q07gDSwIfYeK9FoSoa4ew6ndTRnhFLk50_qsMMBsQIJgAwhVDBbnKCK6SVcDKSvoZuZUrFYqC9_qZVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور دربرنامه امشب رسما اعلام کردکه: سایت و اپلیکیشن پلتفرم 360 رو به خاطر صحبت های روز گذشته امیر قلعه نویی بسته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26202" target="_blank">📅 11:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26201">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe9lg7F58cBSUw1wBr8SVjMeR-ZWwyLfie3f_vvA-i6MLFZVDSSth4OdogrFGLBe63utGwe1oyKSJ1fz7g7dYsQT0ogbJBrG9d15Ntf5_uc2xTP3G5rMvtn5XadZb2hx5el0isl6yLMicuaw7ER2u4Txx2eSVKXN6KpuL1_wdCDXIz78AnEQEkleeBKFoZYAtw604vUrV_RS4_CnMqOyZcugxwW3u4_o4YLfN5wmS2EiqaYk4ng_dgDNYnuoVGMpTwhClywGxzlJDiTfjMcjOQ0szN4wZ8CltQsQ3AX56q1IBjBHwZjFyhnGdC9RMtPgjU9EDn7uYs5Ollr5DvBLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26201" target="_blank">📅 11:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26200">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gxet8852FectcmGPqImoyPgZE78qDq3LUo-qmQ-BCejbQC0DXqHuwuNzGc4HQVvhjEc_NWRCbwCbTZ2Vws-eJA5JWL7LPkjPvBwR0BxvrB30fYhxmANJXo-73hYsdTpnL3IaQmmsclv88Kpzv3mBeYhpYGeI2V25XHIVoKkduIjaxESM4n_MRbV2ra0-rSJiwp1IYbhmRkCXbcD9xWL0o3FwVtTkbqlTR_t1naAeym56udwPWF9WWGcAN5HBXpqpDiVvUiLlIts1I76m8BSknPZNz5zzeSi-n1yG5Ag-vLkquG0AGoNij6ZVtBoas-fMpjXPENOD0eYSu5A8kE9bMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
علی تاجرنیا باز هم تاکید کرد: انشالله تا آخر همین هفته پنجره باشگاه استقلال باز خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26200" target="_blank">📅 10:45 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
