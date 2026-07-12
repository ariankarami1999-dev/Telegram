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
<img src="https://cdn5.telesco.pe/file/ATROMVnxPMC5NtpmvHo4fvTSBY27R_jgdJyJxdRwHbjyGUIcdzJTyQS2d8yfyU5wdgM-ur0Ny5X4w9Oa_xzB79xZTE1umRa3Mezmo5wJo-9q-cLWkXr9pG8RtAAWtUVrnSDwye1D7tTFz0qS2LxQ6Q49d2AqYCNS0Lgn6vDGhje3vY6AsbnWTrMTvquWbMwCn5_XDQgleoZy1P04-3YTsFZZnJQkybScxHjrRLTju098meOPOQo7clwLBU5j9p-g5u7MLpr22ltQfydPUUcwvzjVWdgNMfOJOK9KCJE2DL2vii1G_dvBZ_WZHnV7Nf1jny7uP3lDrkokqL5QPMG0RQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 588K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 21:22:18</div>
<hr>

<div class="tg-post" id="msg-99853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMmrLamz2PKKDv8mE2pa7A5jpPGPh3tm90Bs6-k97q4lTEtdfBkvvlB4pFlNKe5nyncvf2Df4ewf9x1BGSFXYvavtoPHYEiP7cxV54ysR54h3_P-Ve1YZnUnwTUvqo8VAzDLGD-Gg7UpbgPWvRVdKR-YHTcXBeSjyFXh9pEyaffLJ142iK1YzFX_5-bT4jsw8fCB3VGK2Eh2_-T4nPeBONKIuklblStLpUTzhEUJERD6QY5Vp1tg9BQY4mrofrqQPeGwhsOAlYa-jDX9efB3tKKI_S70amZE0LPTksyDsrsXJW-eBUgQkMjps2t4cewT3X24Ar3pgTfhRj6ndv56JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوان لاپورتا مهمان ویژه بازی اسپانیا و فرانسه در دالاس خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/Futball180TV/99853" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99852">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWVoXIpD-fGti9Z96FWqtCeMaSEQiQP_4SKqgY_aOnQiYqfjgXKS9vWvA2oNKa19KOe7WxRYuUG1xkl2go_0NlD1cwIPk3OigstvMfgjGQpjdGOhv5o9Jc0XAAJ6ifSZPXbLPOJnwBCg1VCBdIJw-oq8N5XzVLevA_Iy08iFdyhqYO2JuYUS1-0nCjuoS-iNyOBaHsgtwEcNCnPI0MQe-5vrjydc3dIKrlu9b7d6ZyL3P_81MI8CjbZucyTt9R4SDnCqQLc8oTOIHL6e2nG6_OlOEBiErrgh_H4BrXDTB3L6XFmCUmmXoA8ClbQPwdcVZ0qKKf9Jn4zzmPGKGHipMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب احتمالی فرانسه مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/99852" target="_blank">📅 21:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99851">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSXcpr0bSEMt2DeWHMQJpHB7PbpuuKUnw4OeCGeOHg7do7qLCxu5bLuxX9u4joipo6pHgA4JDTQ0sD_jFDP6dykU_3kalky97zKRLZp_fKlMKGcnACeZ5lVyTMyKxDb7DzXprEQ3TrIHvTSEjArrrmTGWSEPIacYhHv1lPQDAXXktyslz0B0o9SF7Gdh7ijDTsD1NAe1LP8YMdkz9KOYC7f5PQ88_Md0C25KQSSYULvb6Ur27HM7-QvF-NyLi1nFRnfMEaXM4lxjMfZHCZLjOgoXYxTGOWsHJPqFq9nspeBvioKxFkCV6K57F2tE74IYdyQn1DrerCfVkSek70p-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بیشترین تعداد پیروزی کسب شده توسط بازیکنان در تاریخ جام جهانی:
1- اسطوره مسی، 22 پیروزی
🇦🇷
🤯
2- کلوزه، 17 پیروزی
🇩🇪
2- امباپه، 17 پیروزی
🇫🇷
3- کافو، 16 پیروزی
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/99851" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99850">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/Futball180TV/99850" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/99850" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99849">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qmMMW-BIAzvYKoEbJIM6RLJ6fZhgVPuDspHJHAjStKyoP5-s6VccQpOX-9LF_YOCjIUuD9L6lsociVY0H9sGOnJHPM8624BK3sQEm0KzdAt0Ov4Uw2ZQpkzVsyok8_qxTh6aabG0qQa4_WKUUXb5FQAbSP0bHuT5JUeaAps6rAm6NvyrA2NmyVxVkJrR6IBdrfdUK_5HvCApkk1SwPvOeiCQGYqG8OryWdf6m2sWupRnK6ZXqMgejwxlE3NUOLHpcsqQbVgA5W_397iSjlSZH_97_1gxKJAclpdIMIL42ntUZTspM2gP-5EAhBmd1HXry3f_4wd9Ns5AQ6qkm7Alhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎆
تورنومنت بزرگ
POpOK
Gamin
💥
فرصت ویژه برای علاقه‌مندان به بازی‌های کازینویی
🆒
📈
رقابت کن، امتیاز جمع کن و سهمت را از جوایز میلیادری بگیر
💰
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری همراه با انواع هدایای نقدی روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet1.space</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/99849" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99848">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi7tO_g9jJD9HoA8FX0Wlfi74BgtZV3Az_sEU2GmJJVDHuwrKLOmfG7W0oDfIi1HrDxS7CqJUag0Eff5Ptk3gvN1eUgeYRzkfm0iWlgA7hI8YrI_DisSScJg20i-wUaetdAyYDy6sL_yCF_nXTlwBHsUyrbjtcYm3OGUl1jSx3elj8SyvCREb_o5upatXlbrFkT-RtptJ6hsjSrp_5hsypPQtjOYtFiPp_dXK9gC_GXqQK8EqRZVbIr-r_fBEWkxyrqMin3aosYGAEVP3KRN6MIDd77rHX045w2IoQlbYw6ffYgCPne2ttMciDLHQXRrHEQe-ngNqDMN84zZkWy-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فودن و پسرش تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/99848" target="_blank">📅 20:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99847">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Smsne5kEjSHU1OnzpsPj0oewHV4fh4BUM1Z1DcfS4VBbIEAXrlgQfPQjBJijLRAsROLJEPtTYNdV0jiyfHRD0t7mISIOV_sYd6de4Dm0-93XEHDZWPVMlx4ahdY0yt8fITUrll_CybBAxAhyAM_Zn0w_J_FdqWd8eXZixtfLaWTILCgNp_xV_b6p5mDX_1c2b-CBRwcQqQ22iz1fop0IEJiNAyFZvrdek9rYR7JdiuV0UMJjLAxC3CJbRX9FumlDRf6CwVG9q0fckLcOBujJuDc1TvoVtBaGj2ImYV4aKIsyvqgA5VdxFecshlpdTXk00vFrgCFOIhc3JnQvxalPHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6429d99ef1.mp4?token=Smsne5kEjSHU1OnzpsPj0oewHV4fh4BUM1Z1DcfS4VBbIEAXrlgQfPQjBJijLRAsROLJEPtTYNdV0jiyfHRD0t7mISIOV_sYd6de4Dm0-93XEHDZWPVMlx4ahdY0yt8fITUrll_CybBAxAhyAM_Zn0w_J_FdqWd8eXZixtfLaWTILCgNp_xV_b6p5mDX_1c2b-CBRwcQqQ22iz1fop0IEJiNAyFZvrdek9rYR7JdiuV0UMJjLAxC3CJbRX9FumlDRf6CwVG9q0fckLcOBujJuDc1TvoVtBaGj2ImYV4aKIsyvqgA5VdxFecshlpdTXk00vFrgCFOIhc3JnQvxalPHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نروژی‌های دیوانه بعد از حذف جلو انگلیس
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/99847" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99846">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMG87x2zPW-od7fdtCCX6p7DDocWCL-ciPj0wv6F-4adI5E1Af8-W14MJN1FlPh849khu1svCCLu_updmHLwhSxgOrUurtBEN1gY5L9_xNt6WnIQu9Onwdx8LshlN1JXtLWAJOlvItFoSaDnzS-M1Rkdpi7ypi-ddJgu-F-4JTGXHQU60qqyvw15yY9Ox9OH_7c-sIWXDn9ok8gIqDcTIBqxoY5LBH0Pc3QpKlOJuwNm6AUTE0gkEUzYHvywZuhcnJATOI_ixkqmijvyFbd3yD0QwP4UXb5HpNYvBwOZtpK921CEFCGRlv86bhsEFrhvD-1MdgHABBSmWhOWoZICTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
یک تیر و سه نشان، فرصتی متفاوت برای سپرده گذاران؛
از اعتبار یک میلیارد ریالی تا قرعه کشی هزاران جایزه در جشنواره حساب های قرض الحسنه بانک کشاورزی
🔻
جشنواره بزرگ قرعه کشی حساب های قرض الحسنه پس انداز بانک کشاورزی با هزاران جایزه ارزنده و امکان دریافت اعتبار خرید کالا تا سقف یک میلیارد ریال، تا پایان تیرماه ادامه دارد.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/99846" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99844">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJdXX5KNZBxHDQeaAUHCthstJbwtFC3CNB-ODvHm_T3tZzNMWr6Xlu5OngQYnvl_rrz8YdZnMn8Ni-00ma9xOcg3dweJuzDK317zHQG5wAgFVeUwBXUcfVGS0C93Xae32QniCr5OxApgBTGuHaNbmI6CqJ4AfmW3mpZZo9SPM_3Fib6MbkHM8HHKbhtQtjYVtZh4FZl45_rE3dNLAzz7q6-_IJuP6Dpbby05mDIKG1-yeRME8ZA7FeUOh9eg0BLABllm_OOHsX3UK0Aj9ibbco2CuhmY_651t3_reA6BvK14PuFPWKLx3yKDL1iJjYUnrB9F0eaOfaHhdDb66lD4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
چهار تیم برتر جام‌جهانی در ادوار مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/99844" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99843">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
فرماندار قشم از اصابت ۱۰ تا ۱۱ پرتابه به قشم در عصر امروز خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/99843" target="_blank">📅 19:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99842">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=kcR9g0AriRm83SIC4dvRACQsf7HLMSw-p1mQ4ZjXElEObvem6rVCqVPetzZB7wTQlOnn2WoV_cTN1iREmu2jgAC7JOKsHeFwXsecdXU7CVMJETx3Nbc6U-4pqU4s8ugMiaw0FTILS2F6LNqgsGsz0Ze3AfiJj0ZnnlUlYN0sTQtEjLsNUMtZBa90Ii_mC23epY4T06GberJ0a_lub6brviCDNrFSof7YZ5MaUbirPZIErIN63xpjfvsgW828lznx3mGI1ZebaAdFi5tEYWiR0yahN5rUgrPfI4PrloZXaELNGU-ORbO-w3rbWnmYTkWkrRkbUGSFe9nZKU05F6gU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984b701bc8.mp4?token=kcR9g0AriRm83SIC4dvRACQsf7HLMSw-p1mQ4ZjXElEObvem6rVCqVPetzZB7wTQlOnn2WoV_cTN1iREmu2jgAC7JOKsHeFwXsecdXU7CVMJETx3Nbc6U-4pqU4s8ugMiaw0FTILS2F6LNqgsGsz0Ze3AfiJj0ZnnlUlYN0sTQtEjLsNUMtZBa90Ii_mC23epY4T06GberJ0a_lub6brviCDNrFSof7YZ5MaUbirPZIErIN63xpjfvsgW828lznx3mGI1ZebaAdFi5tEYWiR0yahN5rUgrPfI4PrloZXaELNGU-ORbO-w3rbWnmYTkWkrRkbUGSFe9nZKU05F6gU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به حملات آمریکا به جنوب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99842" target="_blank">📅 19:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99841">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
رسانه های عربی: ایران با موشک های کروز درحال حمله ی گسترده به ناوهای آمریکایی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/99841" target="_blank">📅 19:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99840">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99840" target="_blank">📅 19:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99839">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=EXHjrgvvejzLG22rdVireIrV2NLGwoDQkXY11h7g3JUz41ePy1siB2ZFX5DV7WocIC8pQRS54bLPbi0CWvwg7otVBb-qEMljR0YEW4CqCZq5dBa96uXPo_9l0eKrpA8NgegqwbSs9KEwCzQ6Y863wz-x1WOpcv_lOkTI_kmdcEdA1E-5Q2nWUDVYKOJdfurbAsUYdp4M6pdEIg2obQ8JqjB2kcWogUc9bKDlcpHDlCkPhqC1CCn_ga069BporDJur4ZAD4U-GzAFaAUV7Iwadch40Ed8DAo3Fiu_8zveObN0dE63iv4VStVoRrnv3cYaJ2Hrk0lXMdvuJYaOr9uDbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d63368dc.mp4?token=EXHjrgvvejzLG22rdVireIrV2NLGwoDQkXY11h7g3JUz41ePy1siB2ZFX5DV7WocIC8pQRS54bLPbi0CWvwg7otVBb-qEMljR0YEW4CqCZq5dBa96uXPo_9l0eKrpA8NgegqwbSs9KEwCzQ6Y863wz-x1WOpcv_lOkTI_kmdcEdA1E-5Q2nWUDVYKOJdfurbAsUYdp4M6pdEIg2obQ8JqjB2kcWogUc9bKDlcpHDlCkPhqC1CCn_ga069BporDJur4ZAD4U-GzAFaAUV7Iwadch40Ed8DAo3Fiu_8zveObN0dE63iv4VStVoRrnv3cYaJ2Hrk0lXMdvuJYaOr9uDbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
وضعیت پشم ریزون پایگاه آمریکا در کویت پس از حملات دقایقی قبل سپاه پاسداران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99839" target="_blank">📅 19:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99837">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kDgd_YIf1K7mCcl-xh0WzPIFF_MO1Y9G9g1oeURBsOQ5A32eZlCdCasVsuankQMZLsizUxvEflImlCp1uhudnKRgPOnbiLTJ5PW3giIC9Dfy1eSRHgiiOnvEte2Wp9jhDX7x8kdc-qlgW1AXlqHR4gLQNPizBoZudAH-Dwu5iJutSijo7t3yuGmuveAFWSMuDCCq0GqSdVCm37fZK6ta3FhkA54I1dkefh3dQe-zLH8RzuhdIIV_5iWHW0TemwLgWXIOZJamQkhhjEtHMs3FSFGG5_du0heNXS5nFBb_4rbaPWOesSI8n_uccH97leVmvbtNcJlgRdd0SbpdWf3GrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4L_KTH9oC9oDSFGcu0lVk6wgVW780GbzJZVkLxjvkMQWtHK_pGd7TbhA7e7lq_tNg4a68pJfPbnCM3-ici563LntTis-2FjH9TVEnYaj3yqtOv9iAbsaf5yNDl1FQYSd60ICDHWJhl1Olybf4twhjD7L-5f8wQtKDPuaKysG3X882G25XeYVhGiLiP4K-hf6_Uj7fZkpiww2MqVqcc8ctnusk0X_0cjPsbGBE-o3ZYeTHEws4PwjM-bmi_a_F-y1ZDJnlQEy2TzSmaJfOvgMRmUyb0er1XG0SqSyOZeySAhWgcRiGmNutM3UwPO0216pa43e17ULufSQCVx59l32g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه افتخارات تیم های حاضر تو مرحله نیمه نهایی جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99837" target="_blank">📅 19:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99836">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSM94t7xz58fefGrJ9Fa6QQlTzSXlEIvjjJn6qNXjXN8N-72Vz47AKzWSF1zVwNBjwY1rKQGE6kQJnwlfXDPjaTZcUn2BWYRy4XAxJMsEOCphSDBCPjzw-bhhGDXU-P-mbXmNSFnByxMpLyUVzB3_xzEKMzbkWvldUeCdi2JFGsVygQ7HTsXrU3PXvWdPz7gxOCr40521e61lZwArR2aO-Z9YFr-NKEy9m_J_eQ2t2wsLRCsAMN-iC2V8KFb8OgYX5_rwu1UPfx8O_crUgskepcikB3eNtsf5lwI43Dan_mRejdsKHuqCBDrzF2Sdyu5KI8lIcKr2rzPeS9YntcSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
متئو مورتو:
بارسلونا و اتلتیکو به زودی مذاکرات جدیدی در رابطه با آلوارز انجام خواهند داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99836" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99835">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-0OGNYD7_vpkx09Ac9MK3re5T1LZ_dvU4yC3ztvz8X_yCBId7fKugTSY6jLtI1jkSFYYg5WvQ_zzxFiXN7VJVv_KPZ1MHaiFYDGUOGFI9hef-8RFDK7IGHmQjXHtyNCaqZuMzu90D33KOhPt0UWARBlsMt6pXvjGcNTiBVj_cn35nfprAYB2ncQ_o3162M9QF45UDsjLq3FX6yxKVHosvlQqLyn5ZiCpDo-qItHTkYtOQoPUNMreT2bTagPmlrBu1a8lYIWu8hLzngIvunlavnR6ImZ9ybqK1GjA9O6w0g9qZM13d0teG4ksXJsqQZIk8pX_WkRPRK9BmRkUyVESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
🆚
🇪🇸
🏅
تکرار فینال دوره قبل یا شگفتی در راه هست؟
🔥
🏆
اسپانیا و فرانسه از یک سمت و آرژانتین و انگلستان از سوی دیگری برای رسیدن به افتخار حضور در فینال جام جهانی ۲۰۲۶ با هم مبارزه میکنند.
👀
⚡️
آیا این بار هم یاران مسی و امباپه در فینال بهم میرسند یا مسیر فینال متفاوت خواهد بود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/99835" target="_blank">📅 19:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99834">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc23jCOBrQiOVHTycyTkOwd7LpeH10K5zBAW3b7BKmn03mor7Nt_KE2l4aL6O6B1nxIK_1v9rDIRBky03vf90serXLjKcNJY5kxvm-2G7fxJI44Hr41ssP3UDDzWufoJkG3vh9OiAc-_cTgezYRQUMaFZquIVfoOz6dZ9Ldp9Er8D10urHd__CDDgb7KN4nmkl58txE03NxY15IeEDrmWjak6IZ5IkqC0F9KVkQpBnsukeDqfHsSIBcXf2k6KgBjJg8rZwhJUHmmzk1pDE3krOVzzwTYvKDqUD5NTQHi2awL6jloH0PBhi9qbeaeql0p-iNAjGOQRcnpuNykXEVRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فوق العاده رودری:
لمس توپ: 712 بار
مجموع پاس ها: 638
پاس های صحیح: 597
پاس های موفق در یک سوم حمله: 170‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/99834" target="_blank">📅 18:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99833">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04227938e0.mp4?token=cBwvO_XaIRak6Ech87ppriqTzjmFneBI7efFK0ui2ktmGIxKkfyc8-kxIvpadtXddWfQ-vV_UxqbXZWYIuHHfdJU8GGYOcHGBcl5kLDO7f1oGBFWVBgKnvcrXm_XaSw55RszEo8k5kMbJDt48JXYYbu83arvaYmO7TM2BX4qeD6frkGBeFadWHsjQY0AIKoolUqZ-X5_jsvjSZsI1N9lYoVeISYBtCF5AtCWDFe5JP840xCB2EzR0xgeJqxrGcNvReEKZawYwuIcQtCbwPQFRZptexyP4ZlvkcZ2mjBTq6bvclHEoR3vz_opR_dBWHx4c2z2NX5LEXglHLVFYlBFyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04227938e0.mp4?token=cBwvO_XaIRak6Ech87ppriqTzjmFneBI7efFK0ui2ktmGIxKkfyc8-kxIvpadtXddWfQ-vV_UxqbXZWYIuHHfdJU8GGYOcHGBcl5kLDO7f1oGBFWVBgKnvcrXm_XaSw55RszEo8k5kMbJDt48JXYYbu83arvaYmO7TM2BX4qeD6frkGBeFadWHsjQY0AIKoolUqZ-X5_jsvjSZsI1N9lYoVeISYBtCF5AtCWDFe5JP840xCB2EzR0xgeJqxrGcNvReEKZawYwuIcQtCbwPQFRZptexyP4ZlvkcZ2mjBTq6bvclHEoR3vz_opR_dBWHx4c2z2NX5LEXglHLVFYlBFyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
ژاپن این‌شکلی داره فوتسال خودش رو گسترش میده؛ واقعا همه‌جوره باید حسرت بخوریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/99833" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99832">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=dsfSHUOLv6A8FVsY-bOtekNIAliLp_-pFD82pNY_bifIreqyno6V2Z9MF6USPJxObr31H_8vTS_jvm0nadN8HK-_RVC8F7Wkk0xHIQ-OTxolMkwF9igHqGFkjlO7APoMvZOEI10c2giHksSjRv8mV3CTVYFXSFw2IcKJ4heZnxNo7AnaipeWZoZwXFWEJxAvQb-F57FN-FrdGNc3JKOKl4uUKOyZuuiTbEk4THB5fMlqQR1blp294z0zbnzUyqS0_AugYXmwt058CddfkWWu86GIAy-KYzXfAUhmrCuPvYgbi7TkXTQU8NqWWwp-sqTuEpyW-wddkLSSZi08YIGBKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54e8db96a.mp4?token=dsfSHUOLv6A8FVsY-bOtekNIAliLp_-pFD82pNY_bifIreqyno6V2Z9MF6USPJxObr31H_8vTS_jvm0nadN8HK-_RVC8F7Wkk0xHIQ-OTxolMkwF9igHqGFkjlO7APoMvZOEI10c2giHksSjRv8mV3CTVYFXSFw2IcKJ4heZnxNo7AnaipeWZoZwXFWEJxAvQb-F57FN-FrdGNc3JKOKl4uUKOyZuuiTbEk4THB5fMlqQR1blp294z0zbnzUyqS0_AugYXmwt058CddfkWWu86GIAy-KYzXfAUhmrCuPvYgbi7TkXTQU8NqWWwp-sqTuEpyW-wddkLSSZi08YIGBKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ماجرای تل سر یامال و عبارت EGO YAMAL
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99832" target="_blank">📅 18:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99831">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSpjUb6Ze_XbA6EcVCJRS7VAizI_XvEPD9BHcX58R-HMl9Wu4DgQC9zBuP2ZAuL0tAugHkOy1ey2NLHzOHDqfZ2ZSXWr-rSUkuF3tOgF__92Vhkgpte3OLJVtMbrLgQIfky_DhhRg7Slx2pChstnDNzVhDV_uxLq6bqJYjjB7fAsG29cf1s9wv84T8Uc8tiF3WWBcw3s3ZlcJiPtYwlY2-vTlodRbNloDTb21luD0BzEO5fMGIuGt7s_HtD-DEbpGbBskdBjGICDnhJLEaWWABqJjpqbjlfP5VKcvJpl6yTqletFIgs3rkFUXlx1OaYwpzryec_otIN86o69HZqwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇸🇦
اسپورت: الهلال عربستان اعلام کرده که هیچ قصدی برای جذب رافینیا نداره و این بازیکن جزو گزینه‌های تیمش نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99831" target="_blank">📅 18:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99830">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=NOrByOyv3q_mvvfKLhpyXMqqS4AcHMqoZGk_CNrqjrW1K4MbA8rj5PhoZaTqi5fOyELG9AAm-pebNfYMXxeSiusgETWM9sfInxcvJn0J5XSkJe6_AqhCi9QUeK9zYNxS1SLwK43cbUxKC5rq9U0Q9_7WDS_G-6etCma-pcf3K72xWHCigl7_JfTFdO8ToltGsJZWbexkIuxmIw42Xd7ae5FOP6J_zSNNKpRkifPu-vA3GB9NCac9QtMeW3r9yW306yaQRPHQIBG4aGb4vwINULcF0ZHSDpK94fkyZ7egbsyPea0KQS3E4tAM7miAqdB0AJ9PWzs60aiPFY3D98CJcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48ece8c0f.mp4?token=NOrByOyv3q_mvvfKLhpyXMqqS4AcHMqoZGk_CNrqjrW1K4MbA8rj5PhoZaTqi5fOyELG9AAm-pebNfYMXxeSiusgETWM9sfInxcvJn0J5XSkJe6_AqhCi9QUeK9zYNxS1SLwK43cbUxKC5rq9U0Q9_7WDS_G-6etCma-pcf3K72xWHCigl7_JfTFdO8ToltGsJZWbexkIuxmIw42Xd7ae5FOP6J_zSNNKpRkifPu-vA3GB9NCac9QtMeW3r9yW306yaQRPHQIBG4aGb4vwINULcF0ZHSDpK94fkyZ7egbsyPea0KQS3E4tAM7miAqdB0AJ9PWzs60aiPFY3D98CJcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇳🇴
هالند تو این صحنه خودشو خیلی کنترل کرد که کون سورلوث نذاره. احمق اگه پاس میداد شاید گل میزدن شاید صعود میکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99830" target="_blank">📅 18:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99829">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=rkXwB1esBJsXnzv6mw8VhbgrP7tjvpeqgfsG4McJyMQKSU-8iEVpedmDp3Be0EuV2emGANdFOhKwk2XAknBNPED6_QhQyrDJKB2jzq6xEYf_uppZJCLAvuZyBUOYRMB5pktXdWP34mw0O_Nd72WUdKGmTg9RVffBWWoElwzP9Y6OR1ed9B3ouBBEetLIdQx5dC_ckSq-CIJIG8SAJapDII7xhTmyg2wSPwaLYHKDFIBmdQ-YKSHveSKBjvEVgJOaeiW_IOxHBCqS61sOoUnYx-5i369KQCAB_oyYGQRIf55O8RnOrQJbdCfH6fufg4bOsYTR8DDvkF1TLfdra60OPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e3eb539b.mp4?token=rkXwB1esBJsXnzv6mw8VhbgrP7tjvpeqgfsG4McJyMQKSU-8iEVpedmDp3Be0EuV2emGANdFOhKwk2XAknBNPED6_QhQyrDJKB2jzq6xEYf_uppZJCLAvuZyBUOYRMB5pktXdWP34mw0O_Nd72WUdKGmTg9RVffBWWoElwzP9Y6OR1ed9B3ouBBEetLIdQx5dC_ckSq-CIJIG8SAJapDII7xhTmyg2wSPwaLYHKDFIBmdQ-YKSHveSKBjvEVgJOaeiW_IOxHBCqS61sOoUnYx-5i369KQCAB_oyYGQRIf55O8RnOrQJbdCfH6fufg4bOsYTR8DDvkF1TLfdra60OPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
نیمار بعد حذف از جام‌جهانی دوباره رفت سراغ عشق و حال و کار همیشگی خودش ینی پوکر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/99829" target="_blank">📅 17:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99828">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=atN5cPUp0zLt5mpkZdmCAl7w3_7Z84oImpymMzKv-C7QtdO4ytCdF3A8A2xmgaV2635OOXAwVv5wvWLTIkQ6MhUa93PvFaP41bth3Hb3bwD_kvXTMNUIl-TiT3yOlycmWhU4Cclv1OvW6X8NMzch4a2Qeny1eOtbgmSpe9HbaSn_aOzLpDU9qZ-dq1eXN7bvTgHLfb3K3bxbuX5OBdkJA7zpsfUOpS_CwNq47IIbEP08eMIVFdyYgDlbofCYrphpumKy5sThMhAEvRUR_7rZvSJdOfH2WUDBy-XIue0zlPbY1BBs64Yxj6l4g-N-l7g585wQNxlbnDGOFxxVqmueYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4744b6de28.mp4?token=atN5cPUp0zLt5mpkZdmCAl7w3_7Z84oImpymMzKv-C7QtdO4ytCdF3A8A2xmgaV2635OOXAwVv5wvWLTIkQ6MhUa93PvFaP41bth3Hb3bwD_kvXTMNUIl-TiT3yOlycmWhU4Cclv1OvW6X8NMzch4a2Qeny1eOtbgmSpe9HbaSn_aOzLpDU9qZ-dq1eXN7bvTgHLfb3K3bxbuX5OBdkJA7zpsfUOpS_CwNq47IIbEP08eMIVFdyYgDlbofCYrphpumKy5sThMhAEvRUR_7rZvSJdOfH2WUDBy-XIue0zlPbY1BBs64Yxj6l4g-N-l7g585wQNxlbnDGOFxxVqmueYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو رشید آوردن تو ویژه برنامه جام‌جهانی غافل از اینکه دوباره برامون حماسه آفرید
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99828" target="_blank">📅 17:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99827">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=TFd7RXOQ73_wLBem1U4p37eMrfEi9m1LXGrQnJEbCe-9G1vyvB5AZ_0cOEPZZ-NSfr3XfhNd_eINss1aPBnH9KENrZSy7QpNxdfYOnuhdT2tN9qLPhF8yxDK45vZVfRwO3yxs-8eM87CXAbfru8T6nnrF_QVYd7JalBOWDQ3im7J3dsrmXRYp7y-hTAUxnrFd9oXsQaVjQLE7IBcyxbTVYYN-OlF2jh0Oyk5joYsOPUV3y-Z-go_JDx3TjoT0yzLQYpxcgsybIJppv9JmQWnyp-czhFd6USfoQ20PdZz2PWmyXS-tIU2zrIQDE5STxaajBwKaOPdfmOv5ovqFocNYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cad474a63.mp4?token=TFd7RXOQ73_wLBem1U4p37eMrfEi9m1LXGrQnJEbCe-9G1vyvB5AZ_0cOEPZZ-NSfr3XfhNd_eINss1aPBnH9KENrZSy7QpNxdfYOnuhdT2tN9qLPhF8yxDK45vZVfRwO3yxs-8eM87CXAbfru8T6nnrF_QVYd7JalBOWDQ3im7J3dsrmXRYp7y-hTAUxnrFd9oXsQaVjQLE7IBcyxbTVYYN-OlF2jh0Oyk5joYsOPUV3y-Z-go_JDx3TjoT0yzLQYpxcgsybIJppv9JmQWnyp-czhFd6USfoQ20PdZz2PWmyXS-tIU2zrIQDE5STxaajBwKaOPdfmOv5ovqFocNYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
صحبت‌های جالب سیروس میمنت بازیگر سینما نسبت به اتفاقات تیم‌قلعه‌نویی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99827" target="_blank">📅 17:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99826">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFdOw3GN_7_PE4-eiiT46kp65Lyv1tlfvrH-WuFvhd15uFOuYn-4oLs99NXGlsAuV5UshyvG2hSpe4V8-KLfwjv0Dd5hXLwR3jsh_69p8GomBvLMtgwTbLjWoOE5Gxf_wcDzb_6Jtqr1IWujh2pYWpKXA8c1be5TbitIQ2I38BbbL3WKgcZLWYwhVi015UjaZWOgvh8hRgjKV6IJHpR7NWWbG8xjYvho0dwPcDBV4AyjxwKKFMH585MQHT2Qfdm8batqXidZsStJqIACU0YmpCghsaoZMkTopBgGzEo-duy_-9j9S6Bhj9tR27mG1rftmkQRdqD1IMqiOb7VHXqTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
ترکیب منتخب مرحله یک چهارم نهایی جام جهانی براساس نمرات سایت هواسکورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99826" target="_blank">📅 16:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99825">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
ویدیو فیفا و انتشار تصاویر ثبت‌شده از دوربین علیرضا فغانی در حین‌بازی انگلیس و مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99825" target="_blank">📅 16:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99824">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=eoVTukBsknyTthfbmHorzvcfieLSY-iCLQJwXkn316_5LXeBOva50PBw5KLyM_3qD5q8Kd_bQkNpDmO2viNCnYpOfzIJ_RTDn5mgMn6Rvg40AtGX1u_Q27IbQ17PK53qrqjUlvJngZcgxDZV-hfDptfp1vBlwsB-9_90gtawAxkLD-fkLtJyMNdsgdpgbmVLSZdFzLGlVG55SRHWT7AQ8iwjjWOoWUz22qCl4DOV-fAVH5feFP2Zw6fr9BsheZHavwuZQHxuh5xnZICHq0qkwFkYrb4VOpPyzLGyNac-4CzmLLlnboDhi05HmXJ81SJomqSZRk2RFy5Au2hR1i2otA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e7ba265f.mp4?token=eoVTukBsknyTthfbmHorzvcfieLSY-iCLQJwXkn316_5LXeBOva50PBw5KLyM_3qD5q8Kd_bQkNpDmO2viNCnYpOfzIJ_RTDn5mgMn6Rvg40AtGX1u_Q27IbQ17PK53qrqjUlvJngZcgxDZV-hfDptfp1vBlwsB-9_90gtawAxkLD-fkLtJyMNdsgdpgbmVLSZdFzLGlVG55SRHWT7AQ8iwjjWOoWUz22qCl4DOV-fAVH5feFP2Zw6fr9BsheZHavwuZQHxuh5xnZICHq0qkwFkYrb4VOpPyzLGyNac-4CzmLLlnboDhi05HmXJ81SJomqSZRk2RFy5Au2hR1i2otA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👀
عاشقانه‌های حسین‌ماهینی و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99824" target="_blank">📅 16:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99823">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=GOHcn4OVw3VM-Gd9t55HDnSy7NNGgn8vJ3mofVBwNaojooXbuFRlwd06CSD5EEFkhMr8dM4Nzqv6BuMdxgBBzdfJxTNliD1cAkU4nqsnx9DvyBamKkpoYjKi5bV1CeawkWB0IZEjlc0qPnXRBaxK5z3SwNf4kzKJ9SxWkOYl2k6-zj1XI1mWxgK_sZeYXr-JA4VdH6yOfzW4zNh2oVVrTikAbtwZR7CVCqvAEo1XfNqYkzH6WqpK6UgJBe1WGze-CJNCL1boIutkUyh1_7GM32fNwvUyjlXeRgg4Nlj2c5nBsZvti8DqrpSSx8N__Eum2noIJYMf1s8M4TMjb3n1gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affcde1f8c.mp4?token=GOHcn4OVw3VM-Gd9t55HDnSy7NNGgn8vJ3mofVBwNaojooXbuFRlwd06CSD5EEFkhMr8dM4Nzqv6BuMdxgBBzdfJxTNliD1cAkU4nqsnx9DvyBamKkpoYjKi5bV1CeawkWB0IZEjlc0qPnXRBaxK5z3SwNf4kzKJ9SxWkOYl2k6-zj1XI1mWxgK_sZeYXr-JA4VdH6yOfzW4zNh2oVVrTikAbtwZR7CVCqvAEo1XfNqYkzH6WqpK6UgJBe1WGze-CJNCL1boIutkUyh1_7GM32fNwvUyjlXeRgg4Nlj2c5nBsZvti8DqrpSSx8N__Eum2noIJYMf1s8M4TMjb3n1gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
واکنش دیوید بکهام به گل دیدنی بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99823" target="_blank">📅 16:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99822">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=n61LwevsqWeyCpoxpg2h0bc9WSCMEgmfd-f4mv8-CPKXb5kXlfWsSUFAm98RlW5WQ2EKfYGHsBkC8uEjCNrouvsrmFLqUC6Ze__wo-J71VsPvSE174SwvxU4KizoltSYqbBtu3m7N0x_licCMKV9Q3-WVQti3yG-f4OveY3c_VeWZXFH2lLuk0PpV3SsgUHK4HPCMhufqk4fXblpUKoxDHAU1BdOqUylYc28RIwPEAz9U06z8NBUmBnJQOpAp9HGoqUmeip1usIKXylh7awF5n7HqFgZYuS7zr_4FSI1fU2OhkBqkIaZ1pil8QDZdytOjA2KoKGYJB1xYT8LSxSakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3eeeaa3f.mp4?token=n61LwevsqWeyCpoxpg2h0bc9WSCMEgmfd-f4mv8-CPKXb5kXlfWsSUFAm98RlW5WQ2EKfYGHsBkC8uEjCNrouvsrmFLqUC6Ze__wo-J71VsPvSE174SwvxU4KizoltSYqbBtu3m7N0x_licCMKV9Q3-WVQti3yG-f4OveY3c_VeWZXFH2lLuk0PpV3SsgUHK4HPCMhufqk4fXblpUKoxDHAU1BdOqUylYc28RIwPEAz9U06z8NBUmBnJQOpAp9HGoqUmeip1usIKXylh7awF5n7HqFgZYuS7zr_4FSI1fU2OhkBqkIaZ1pil8QDZdytOjA2KoKGYJB1xYT8LSxSakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عیش‌و‌نوش محمدصلاح در کشور مصر بعد حذف شدن مقابل آرژانتین در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99822" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDi_0JQGS79_z2FiGdqQ_phmaccs0IF4nS_98vpGBBJDpZ9r33ReIvZr0eGXVKRt6x-FqM5WrC9m5259jW_hIqhKkgr_Oa6rkurU5Uh4R55qcUksQSGfUPxVFAbhdg9L27ujenG7WU9ADKGR3Ny0_GGhv3EN-wzor9HwXhqb8zxQgWiaBu7domZEUuyPh34_PS1yDSsmX-GAPISiGj5MhTcYN3ueQTZdYvacFD4qoguFwrlR8NRtxsPSMYWJyHqZdOVXhK5SeF25ZB_gORs5cNJ_epMf3zYmpHdR-uGv72PwXlLbzNcENVAB3m02tYBORwUeiu7pHFthhvzvfgGXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJoqnVx_5jImmAN-aMNMsDpcENshYtppQE_195ssOEDU4x1lg-i8DrHdMVY8X4YUHSkpyEr1qoDWAmblUllblCRjwl5MVLO9D34LxU2k06z_sq2MT8uaLUGT9Vkofu8ZeXW9B6bJoG_3ww_3LdI5_pgRfH2iF07rg-O1aPjFIEjyu51s__xX5-oYFnESz4GpPGwrsQfLAJtJFf5ulWY7t_AKInkpvjtCf4m0H-OhzAbhtTUkwW0sDrpffy-LPA7vBAtaP2tjPz0xy5M5NqFbGWpQAZv2l1N-PWXuvKWpBL0Kt4eYTIgXVg2ar93ePugb5acq_sAFVaQcecNsoSNzrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtV3xZJvbMvcmnQjAM6s470-fYJ9DInPelOTd6haOflfZa1KzZ5_xCKakqh3lAnR2-82p2E_MFGrJ12PdDaTOWQgrp8RkDuzGMK2vniq8Q6-Df-Hr7yDWRkyKPihNwhJKq0YNex5-WUfWgZKnVvO2XmTnkzAqe3FluPk51TEec4LLCyLljEwt6FbJivDswibKb4mu3-Ct2p4dT5jU0rYuaIxEdDVylOQRhH2DGZKm2tBWqO8mhffs8DvGJgeTnyM76e3ciUe6lsR4y4smFySSz8HO4KFnAvF2GX73drx9zl0btadkLZz12HYg2r5CHdkA_FMm3XfmXCujvnIYe7yyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJ3TMRGBVQMC_BtMF1bvtXU2RE2kYfsqc9rYDtsmComik4oXrj-jJnKFwN7ve-T0OTgGzMXchXklQI1JApf-C_J5UvoJvhNmA7Za5H4ebwMV5sU95a4vCeoOR6OVxnAF_oB3dVahwz4WhXC66ZQqVIi9-46booNAk-GzTUiZgoK_8_J4b31WtkE-TtGzpwNcEineHx69FZn6rwPbxIiGp1D2eUK8gcEruXxeZz3DbA__x5urs_c6p6C5uqWf4vPwIOtfgRBiBNwoJbgoTL85ZIOschshdrNyglLy7Ycp2qsNAh6kzYHgFzqIbPlET5StTqnMS_368ChQj7e4F4JqnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
استادیوم‌هایی که میزبان ۴ بازی باقی‌مانده جام جهانی ۲۰۲۶ خواهند بود:
🏟
• استادیوم AT&T [
🇫🇷
🇪🇸
]
🏟
• استادیوم مرسدس بنز [
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
]
🏟
• استادیوم هارد راک [بازی رده‌بندی].
🏟
• استادیوم مت‌لایف [فینال جام جهانی].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99818" target="_blank">📅 15:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99817">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgEoahr21yMnRcBKhweHlkLqgcm1WAC_DlhP8mMvOJRuWvlExrmSTJweZo0i3NLfay-1Q3qwYlxVQyi_5ouD_d820bopJNSAv1u4s5KGeQ31wRlZ7taau1QLchikGjj5aMGIt0tTyQEtJ_swduI6D-cfxwW9l84_BmA-Y9ZcZVxCdboCCTvBWCL4bKGs4ygLUsIIDiYul8KiZKaQqP4VPlsyhD68aFMtwAqNtOUlT-aVWRKDbgSi-EEvNJt-9VhtTyo8oxPqgcxGNzwpSXMRPuQXjw07MIQ_HQh3yZ8SE9sBMyILLUibfdEITuRQWJXTVzxdB_s7I38j12gSNe_8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد تیم ملی انگلیس در آخرین تورنمنت‌های رسمی و بزرگ:
🏆
جام جهانی 2018 — نیمه‌نهایی
🏆
یورو 2020 — فینال
🇶🇦
جام جهانی 2022 — یک‌چهارم نهایی
🏆
یورو 2024 — فینال
🏆
جام جهانی 2026 — نیمه‌نهایی
🤔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/99817" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99816">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=kqALw6-0FO0Bt8BBMzNi-OkZmKTjvGDfiR3BvtC9_R4LADR8YzK-s6IRcj6uU6TK8ipP9jZaHSby2yg2aNQCz3D04O84JkTRbhuzXvDj84PmfH0mfyZ9QArCjO_qEWSm5Rc76rsbZbq0jLNn6gXLqQE5HRDUekDL-StEKOcaJYhj1s0n9Luuwner2HuePHtrO8kaleE7uUGixJcaLbFhI4pe_yArxuCp4sviiBiRBWUSyxBk7NOIEOdQdG5FgI4aBoSxEt6lGJy4Fkr3A7TtHp6uliA0F3IG3ttN6ScqgjFys4aUF_tkUzbMvoWp9x9LykfEDwHKZ9EF_U1qTbTepyAmZj4nnWhzQPWpJalsR26cfPPuGnFPBp1j0tGQL5NWqwLRkYypE3dN82qX-xO7ilDaBFy-HsVk1KuXdgoC7xUQumn3l2zQv5XFaNR_yz9kk02QKFC6siY4jiimS-x0hM48dKHYbv6SHNt0SOEWMT9e2TbORkwZ917rjrh-MpET2ga_4149zd5l_OwzsfYKM_2G2oZYwUh3vwvXfe5eUrSvIuN0Ar-9qWw3Rq4di_r_-C4lhUaQ-KzObfCpQ6lpZWb79VEFeuS7NOnBJifgWAVSamPCr9aW8ATvzOwVqQFqyaqb9Xsyx2vLSWkhaXDyiLo5mhQo6ofPJVUcmP52tmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c41a3c293c.mp4?token=kqALw6-0FO0Bt8BBMzNi-OkZmKTjvGDfiR3BvtC9_R4LADR8YzK-s6IRcj6uU6TK8ipP9jZaHSby2yg2aNQCz3D04O84JkTRbhuzXvDj84PmfH0mfyZ9QArCjO_qEWSm5Rc76rsbZbq0jLNn6gXLqQE5HRDUekDL-StEKOcaJYhj1s0n9Luuwner2HuePHtrO8kaleE7uUGixJcaLbFhI4pe_yArxuCp4sviiBiRBWUSyxBk7NOIEOdQdG5FgI4aBoSxEt6lGJy4Fkr3A7TtHp6uliA0F3IG3ttN6ScqgjFys4aUF_tkUzbMvoWp9x9LykfEDwHKZ9EF_U1qTbTepyAmZj4nnWhzQPWpJalsR26cfPPuGnFPBp1j0tGQL5NWqwLRkYypE3dN82qX-xO7ilDaBFy-HsVk1KuXdgoC7xUQumn3l2zQv5XFaNR_yz9kk02QKFC6siY4jiimS-x0hM48dKHYbv6SHNt0SOEWMT9e2TbORkwZ917rjrh-MpET2ga_4149zd5l_OwzsfYKM_2G2oZYwUh3vwvXfe5eUrSvIuN0Ar-9qWw3Rq4di_r_-C4lhUaQ-KzObfCpQ6lpZWb79VEFeuS7NOnBJifgWAVSamPCr9aW8ATvzOwVqQFqyaqb9Xsyx2vLSWkhaXDyiLo5mhQo6ofPJVUcmP52tmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خوش‌شانسی یک‌آرایشگر در حاشیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99816" target="_blank">📅 15:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99815">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=jH_sZxAUsTHUmlRF56YMeXne34xvYR-mzjuorhht6rTUaI2v5EkF_9cRy-MGM7O0ytTjqbVBGrUV7uSMFZJs795IV1Mb4JdUcorWD9Y2dkJiYXQ9HIwUCq3_HDMBdrirtJk4zc-1Ep_UkvkSiI6wpCyfVcX5anoaOa9lUP3oqriIWWogSIv0FRF7Kh9RHDbZHCP_D_z9a0u2aGwbNvA8c54rnQoDgUaw8iFFrUVD9MN9Gu-58CTEXN6zUv6cKsA926KACVn-zGp5hGnqn_PqLTL90bSS6eeEoZ6v5bQ-4mxzJcTGc8GR24ETtOdWJwmiN5H2HhkbkSRtlsAY_L1jiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c1f00871.mp4?token=jH_sZxAUsTHUmlRF56YMeXne34xvYR-mzjuorhht6rTUaI2v5EkF_9cRy-MGM7O0ytTjqbVBGrUV7uSMFZJs795IV1Mb4JdUcorWD9Y2dkJiYXQ9HIwUCq3_HDMBdrirtJk4zc-1Ep_UkvkSiI6wpCyfVcX5anoaOa9lUP3oqriIWWogSIv0FRF7Kh9RHDbZHCP_D_z9a0u2aGwbNvA8c54rnQoDgUaw8iFFrUVD9MN9Gu-58CTEXN6zUv6cKsA926KACVn-zGp5hGnqn_PqLTL90bSS6eeEoZ6v5bQ-4mxzJcTGc8GR24ETtOdWJwmiN5H2HhkbkSRtlsAY_L1jiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حذف نروژ از جام جهانی به دستِ جود بلینگام.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🦁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/99815" target="_blank">📅 14:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99814">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpYBYO4VVUnOJsj5sKabYxcn4TFBW3TlbgqQdSrgFT1zkRkVNDkjCCoQJ_qOf3JxuXrOvOhthHtAIPz8p_vS6ybdWA0qObxlivMW43km9kWhXPp9aLuRnfL6TtbC46-0tZkskPjBBvhGT55bmcJfolYsg02W94GFCag7ayEWy91B3cQm0lcY3uuuJ7cz00CJ31eXGLOYn-KMOW3tsy8qBUWy8qHUKCj5VY5K7uVRGGOrbQvSaiCKo-ySLU7zgfpI0EkTVXtShMB353CHNXNVlMByu-Drrv_ncJWdm8hNXYXwQvHSB68WWVlQQuPfljqgwFjgIPW2HHfx9dfvub5RmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از حواشی زیبای بازی انگلیس و نروژ
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99814" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99813">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=a9hhWWQWYsq1REAi-mcJDdKA-McSyoy6ut6fWQURfMACR7vKX4W4AIn8olN6QHHkUbLwrhTBtnHvTrmLjpVT-MWR2dzJvFui4dq-FO6nt0YuvN_anKWvG_NDvH263xxY88VU_1VAYmqoMqfAf-mAKtwaJW67GQrSQIDhwy8MTvfpGHXOn7AyZbF7n1KsmIP9c9R_gm6snGyOCpr3WNPivB2P84Qm4e4Tu_oy9Fy-bsfiqRGeiv7mLXwQTXLrFqg8pTDuIvpY_YTj34fU-jLVlgZ9t0hmrjYURoTV8eoGBNJEAPLXKrmPkPXUUZnlqpMpcDjg6pjSMcOpPCyREdiUXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3480a720.mp4?token=a9hhWWQWYsq1REAi-mcJDdKA-McSyoy6ut6fWQURfMACR7vKX4W4AIn8olN6QHHkUbLwrhTBtnHvTrmLjpVT-MWR2dzJvFui4dq-FO6nt0YuvN_anKWvG_NDvH263xxY88VU_1VAYmqoMqfAf-mAKtwaJW67GQrSQIDhwy8MTvfpGHXOn7AyZbF7n1KsmIP9c9R_gm6snGyOCpr3WNPivB2P84Qm4e4Tu_oy9Fy-bsfiqRGeiv7mLXwQTXLrFqg8pTDuIvpY_YTj34fU-jLVlgZ9t0hmrjYURoTV8eoGBNJEAPLXKrmPkPXUUZnlqpMpcDjg6pjSMcOpPCyREdiUXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
کنایه عادل فردوسی‌پور به عادی جلوه دادن شهید شدن مردم هرمزگان توسط صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99813" target="_blank">📅 14:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99812">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🙂
اگه جام جهانی توی ایران برگزار میشد
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99812" target="_blank">📅 14:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99811">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=armBEa9MG8f89eDSzsTSe2O1uRvS2e-k1aZbB6pVyhcAsgC_7HKJnCtOKdqSrQXFDGUXTUdPvnqJxRSEf3SiNBdAfhelY3CszQjZOTa_oBB1xH1iuNV5dK9CxlX5nohLyUBivpgKNbJLu4GXit9gpflPrVwY6uO_hnLLiQ7ZngtYGshF_u_xAP1-Tb0ZbnX83DMNatTnQte_GtebAYQTqcHp3HTslA-Vxvy9NZAYPoqG0FD8R8bsemoT8bD9y_HuBZQx4orTgQ__NMBmfzozEkH9jh3x6S3vbtk7lBAX9u5LPlKTOlKkvDogBr-XSRhz7dP-V1avnIQcDpBV5XduFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2495db55b9.mp4?token=armBEa9MG8f89eDSzsTSe2O1uRvS2e-k1aZbB6pVyhcAsgC_7HKJnCtOKdqSrQXFDGUXTUdPvnqJxRSEf3SiNBdAfhelY3CszQjZOTa_oBB1xH1iuNV5dK9CxlX5nohLyUBivpgKNbJLu4GXit9gpflPrVwY6uO_hnLLiQ7ZngtYGshF_u_xAP1-Tb0ZbnX83DMNatTnQte_GtebAYQTqcHp3HTslA-Vxvy9NZAYPoqG0FD8R8bsemoT8bD9y_HuBZQx4orTgQ__NMBmfzozEkH9jh3x6S3vbtk7lBAX9u5LPlKTOlKkvDogBr-XSRhz7dP-V1avnIQcDpBV5XduFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇫🇷
حمید محمدی: اینکه کادرفنی فرانسه بعد از این نتایج درخشان و رسیدن به نیمه نهایی جام جهانی بگویند بس است و این سکان را به افرادی دیگر بدهیم بسیار آموزنده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99811" target="_blank">📅 13:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99810">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=uyouTozlEr4kUZ-tVs0zhinuT7kot33yMEynDQMlY9NT2gN8YcB5mheJx3-2T5YbIcVimeLB3GKbcvpI8YOkGEFuMTd0v5J1sKQE6E8jgToauJGGXlyrJhoTaM-ddtPagR_jBxpkUt2D6WLTEAYPPYhwRKgNkqM3fqyuWa-To19mSJ-puZA3uS6pzHq_-U5_gC6zTDlt-UujPGGRdYkkl7-uUhwws-TkjJF25ZGXUItNzH5VT4TIusqvrlBm898lTGPcjqQEafd6yorXWYB-6Qw6tF9vlZDmtPHEq7Vo3gLsSFdZdAHYlpCpgHecDtF09MFyKm6mhirt6Evkjxvq2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8bf3f6a7.mp4?token=uyouTozlEr4kUZ-tVs0zhinuT7kot33yMEynDQMlY9NT2gN8YcB5mheJx3-2T5YbIcVimeLB3GKbcvpI8YOkGEFuMTd0v5J1sKQE6E8jgToauJGGXlyrJhoTaM-ddtPagR_jBxpkUt2D6WLTEAYPPYhwRKgNkqM3fqyuWa-To19mSJ-puZA3uS6pzHq_-U5_gC6zTDlt-UujPGGRdYkkl7-uUhwws-TkjJF25ZGXUItNzH5VT4TIusqvrlBm898lTGPcjqQEafd6yorXWYB-6Qw6tF9vlZDmtPHEq7Vo3gLsSFdZdAHYlpCpgHecDtF09MFyKm6mhirt6Evkjxvq2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تکثیر ارلینگ‌هالند در سطح بین‌المللی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99810" target="_blank">📅 13:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99809">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5445db9621.mp4?token=GBY13G4VY2YWPZqakkkoiOw7-7tdU7GFWDsmgyaOYPxMOX3P-skj4nJakOMDL3dHACSABcsIHqdzhgJeXdmIKqybzuYd8XPSUiB2cPbTHa0cWfuPwefjIYhDXNjuR3m7lhxIF4T4IWB-UGDQjZ2-Z_6ohz5Wckfv8QCMlihmxTzbumr7xfbbc-FDSzy1MKAXW60cbrM-CgWKrb0aGV3wL2hX6HvfQjC8JThHV--Pzu6dKZ-rjx1b7ob-0S_K0jqg23uJ-Q_ytNiHixVe6-LJ-usa0k-HwJIGgYJnljfezupDmJlkBBbyOa3BdHP3btZs1ohyLTf_gw_rCng_XswLvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5445db9621.mp4?token=GBY13G4VY2YWPZqakkkoiOw7-7tdU7GFWDsmgyaOYPxMOX3P-skj4nJakOMDL3dHACSABcsIHqdzhgJeXdmIKqybzuYd8XPSUiB2cPbTHa0cWfuPwefjIYhDXNjuR3m7lhxIF4T4IWB-UGDQjZ2-Z_6ohz5Wckfv8QCMlihmxTzbumr7xfbbc-FDSzy1MKAXW60cbrM-CgWKrb0aGV3wL2hX6HvfQjC8JThHV--Pzu6dKZ-rjx1b7ob-0S_K0jqg23uJ-Q_ytNiHixVe6-LJ-usa0k-HwJIGgYJnljfezupDmJlkBBbyOa3BdHP3btZs1ohyLTf_gw_rCng_XswLvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
راز جلیقه‌های هوشمند بازیکنان در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99809" target="_blank">📅 13:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99808">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmkrcCbbNXMOs892CHpxvyNqxDRKLf_FPo_fonItp4YKudYtByDBCBjsfK9y02tXevONwvNRx8kPx1IDxqTeTDlg6XXiemtOoGzii6TT0E8DOk2DvMVjxJKsoZ4BAYmo6DT7n7UKUmoDXgiA6q9hCeD8zDAF9r8h_U1AqghKwWjhBSjML_mhA41M6AFSWu0VUzQDDtlBxc3HS_gUp3KVXz_RuboDKM14v65XrxIYl777KifBzHQREBJXqpjw2s0rRdSv6EZ6D7surnpbLisRc8Q7qCyqVVQo9g7-wi7IskxTiYgSKuSF5zZik6X30grqtJDTUp1pUsuSZot-p_cwaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
• درصد احتمال صعود تیم‌های راه یافته به فینال جام جهانی (بر اساس مدل‌های پیش‌بینی):
🇫🇷
فرانسه
- 58%
🇪🇸
اسپانیا
- 42%
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
- 51%
🇦🇷
آرژانتین
- 49%
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99808" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99807">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/99807" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">❌
با هر 1 میلیون شارژ ،
🅰️
🅰️
🅰️
هزارتومان شارژ اضافی بگیر
🅰️
بدون‌قیدو‌شرط
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی بدون فیلتر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/99807" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99806">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj4KqbuiNuf9ZItCXkTcNL-DCjUgvZzmTJnUYTWtO2sXL9zrNoVFThkrKbJi7iQeuOtG2uXB19HbUzvNzFx3iahdnB9SpuvTVAvxvYs9KbuUBHLje4bg4Qme5R1mV1lr18Y8AiMW3SDW6CHVM3FMbjBgKAzCfvo4mH1Z8GXpgTAS4uqwZ4zTpf9roc6SIVzc-QTRy9snmmEC0d8Wiz-GEy1j_UQRsZjknxDplZDh63r8rr2UaEZ9ABvaMVrzKFPReEB7qdix5iZVk_orov48F9Q9uITeB4Z0-yhLNbuz-qxde6_RivKkGzgQijIGXW8imwxIRIvqwaYiVkH_hZZixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تنها سایتی که ریسک شرطبندی
🅰️
🅰️
🅰️
آورده پایین#بت_اینجا هست،بخاطر اینکه :
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی میده
+
🤩
🤩
🅰️
کش بک بابت هر باخت
🏅
بهترین فرصت سرمایه گذاری و چند برابر کردن سرمایه :
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r21
@betinjabet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99806" target="_blank">📅 12:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99805">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22252f139a.mp4?token=rQ5RiQagauYvqKcZMKOkOm0J8mzxWXvmkFnTgenBMlFx2--vSbVg15ikHdl_d8huSfw-L2cEDNmAGtbT-Qb8oHfiH-p9nJY2pyoorJy76c0j-xUeHX1MXzjuzvEJ-HHVqj73Addppo-Dvtz9ozxMhg9fV8u6mu4fYCUjxJbo7fZRnQPBYEayq4OCYw6k0f7Ueq-s5FTciH6OAw_Z_t46yWLUa4WUukXqFRp1RJSWu6wxLOg57G5uVoR_FCmMsprEnFXaX9HRmxuprdW3uZqJlowa5cPd4OelruQqcNWNw4CU6pVsz2ZJHcGfghyAoAlEBP3TqRsVK58Ofdh2HfJNYQH0fck4-TPX8WB9iNI5WM0_xd1at1ZLVEzQW3AGWYjyNwaCbTYVNPbr4HGWv3IC9r1hmghxuAV-oz3nIvHV1VIWVXa6jfQpJbq2vxs6fxwpEfuMwYtjmr4gmikKY5N4NqF-3T3bUWt1cy4hFskoF3hKB1kzC3TClGC8EvYCM05NNtIMJpADL_O9LLi7hEBT7YTNQmKwyjWtAMPdmaWL8_3y1vWXJUfFLI4Zb5WTISGf9NxgaA2jv4dzFjQRdkZliOCTRUYkGnWeyTztEitRHews0T-kqfj5cZs3Zj2eao7hZ_zoEszHzWi1YDxUtkDdhDxunI5H8FOGVTCcF6UsZrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22252f139a.mp4?token=rQ5RiQagauYvqKcZMKOkOm0J8mzxWXvmkFnTgenBMlFx2--vSbVg15ikHdl_d8huSfw-L2cEDNmAGtbT-Qb8oHfiH-p9nJY2pyoorJy76c0j-xUeHX1MXzjuzvEJ-HHVqj73Addppo-Dvtz9ozxMhg9fV8u6mu4fYCUjxJbo7fZRnQPBYEayq4OCYw6k0f7Ueq-s5FTciH6OAw_Z_t46yWLUa4WUukXqFRp1RJSWu6wxLOg57G5uVoR_FCmMsprEnFXaX9HRmxuprdW3uZqJlowa5cPd4OelruQqcNWNw4CU6pVsz2ZJHcGfghyAoAlEBP3TqRsVK58Ofdh2HfJNYQH0fck4-TPX8WB9iNI5WM0_xd1at1ZLVEzQW3AGWYjyNwaCbTYVNPbr4HGWv3IC9r1hmghxuAV-oz3nIvHV1VIWVXa6jfQpJbq2vxs6fxwpEfuMwYtjmr4gmikKY5N4NqF-3T3bUWt1cy4hFskoF3hKB1kzC3TClGC8EvYCM05NNtIMJpADL_O9LLi7hEBT7YTNQmKwyjWtAMPdmaWL8_3y1vWXJUfFLI4Zb5WTISGf9NxgaA2jv4dzFjQRdkZliOCTRUYkGnWeyTztEitRHews0T-kqfj5cZs3Zj2eao7hZ_zoEszHzWi1YDxUtkDdhDxunI5H8FOGVTCcF6UsZrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انشالله برادر عزیز آقای عباس‌قانع با اون صدای گوشخراش خودش گزارشگر فینال جام‌جهانی نباشه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99805" target="_blank">📅 12:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99804">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=CeBs8ukr6uTKV_mZMhsrrR5n57FPXQ94X28C1DUelQHs__a9WLvY2CaKrCX1aMutth9EkL6Z6pi5unPzcZEfpSaJj0M6WXUax8yHMg3BDLAfHbUs9niI47Z2KpRmTTmiJ7jGDO5Lgh7mbfZ4CTvk8ohK7zlczMX1vkn38uhoq-gGTuBLNKVD33w-hFR3a0qWvZlv96fOCepAPUwwpGUwg0Lnl5CyTBOKraudwsjZfOIIXZkIn9oaZlAx0R72n2ZovDu8HU6vY3H8NMFZacrHJ4-P5gnihZRcsvpmGwAkM27iL79Hc9QNPtJX5ZoLLMG6Yh6YlNdm-wD3dkR3k2aOPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d299a804.mp4?token=CeBs8ukr6uTKV_mZMhsrrR5n57FPXQ94X28C1DUelQHs__a9WLvY2CaKrCX1aMutth9EkL6Z6pi5unPzcZEfpSaJj0M6WXUax8yHMg3BDLAfHbUs9niI47Z2KpRmTTmiJ7jGDO5Lgh7mbfZ4CTvk8ohK7zlczMX1vkn38uhoq-gGTuBLNKVD33w-hFR3a0qWvZlv96fOCepAPUwwpGUwg0Lnl5CyTBOKraudwsjZfOIIXZkIn9oaZlAx0R72n2ZovDu8HU6vY3H8NMFZacrHJ4-P5gnihZRcsvpmGwAkM27iL79Hc9QNPtJX5ZoLLMG6Yh6YlNdm-wD3dkR3k2aOPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😔
جوری که پیمان حدادی مدیرعامل پرسپولیس دیشب از حقوق ۲۰۰ میلیونی صحبت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99804" target="_blank">📅 12:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99801">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVYekhFSuv7Hl65DABuxoi0zpRdcyUhAZbIZz6ajOG9pyAp5sTUELJq_SgLxtiyae2Uc2qfF1GcdqUgXkpk_w1gj-y-65OcGsOc3jD-j8D9FVr9HXoq9fso0d-PuKCi80Jnn2vRqE9S-qRN6vOTG8-WL-5WKW8i-5y4UrFE-GNtVCz_VcpOPKDDX9pAUSw2bMu6_2AMpF1waHokm-I9ok3bNO7yqgPpG5inxB7Cs3763tLnYZoGrmc8SnGr0DK95V38P57bq-0pIgafUbchI9TNXzOeQraZFJQ4sVruqJrED2hXsuI-pssvE-J08xTwuLXD_wCHOKzsGe3kuX7_a-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C90rjujxiCj75R1GlyzATS0KC5G3xkfC-vILYame-RBy7dSNzSxeOzZ4jSONz9rq9YVuPIWBgAZQGLByEdKthZ0crsRsBAlq5VGvnUFBDQxZNuTxE7RIOWvxTxEN9LInMXF69qDx9ePwlvNPGPujGyuJyghgCVscwPqanMpcvhUOwJUfhGnVfHOwBG54QyHIOQ44YSHzsZnDVxuory3sT9PJ6tXVXyweIBTAG49a-3ihV8EwYKy_6Sd--4H_67kdjhI3xCUVOU_zARIvXkT2HdBbtC-_mLg2iwXzpm_P9n6AsdbTcheKsbyUfri1sd835VnLsjDNs6RXAn9IRxhlFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLWDF_nXzdrNIsSg-BgSzFkseOe_ZCiWOXu5aCkQjKqracv9vYXVQItvlQCMP9n40T8XJ77v7lN75Zh-_voXX-mAs4T4OXkoPdZq-tcD6MrLXyW24yKZeSYN07vhGpv5-qDTeXzDBc2YgKvsjCIaPRvzawW_EO86NSr8MUhRudM5h3lEBeLBOCCyudTtF04twCuGQN20u2EhD2XOGv5VZ92pR1SOsDHQ8ezcBAV6ccqV1aPEkchDLqr7pAt3Qv6THBuio7LhbAMGlW6du2RO3srxSYk2UdCc8mstA1NJCofNQN9F0bgIYCG3QAB8ZLagKfDayoLw4cDSjEB5RK_2Cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوس‌دختر بلینگهام در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99801" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99800">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007eae865e.mp4?token=WYeB55lIrCqXv-uDPH1dyK6eUQNDzf32E5Ed0SrwL1gKHLE1v1qXhmTGT7T5b47NMXLXfJf-Y3ymYYUEHGdDLdfJuRgopvYNo8JMvgL6qJNt6IkeBtzWwMahjHnyXbcGDA9TUBk1aRtrwt1t_mamNE5zTrUf_Svr574CKx4OvQoZN9yToz_-2lVd6UiYz_3KAuMG_R9wSjbxS3rHkFwqkeEeFOffzVsA2qLaKIh-uk6evQEE5zhjFgZmUFjl3Nc5hcH27OAGf8KUW3TIyKfKsWVAaB9wO9ZwpZscz10_5s0SkEC-t0uQ8WeK67SakdD6-_ahEG8qOsiIHtfGfnctKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007eae865e.mp4?token=WYeB55lIrCqXv-uDPH1dyK6eUQNDzf32E5Ed0SrwL1gKHLE1v1qXhmTGT7T5b47NMXLXfJf-Y3ymYYUEHGdDLdfJuRgopvYNo8JMvgL6qJNt6IkeBtzWwMahjHnyXbcGDA9TUBk1aRtrwt1t_mamNE5zTrUf_Svr574CKx4OvQoZN9yToz_-2lVd6UiYz_3KAuMG_R9wSjbxS3rHkFwqkeEeFOffzVsA2qLaKIh-uk6evQEE5zhjFgZmUFjl3Nc5hcH27OAGf8KUW3TIyKfKsWVAaB9wO9ZwpZscz10_5s0SkEC-t0uQ8WeK67SakdD6-_ahEG8qOsiIHtfGfnctKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
مود طرفداران آرژانتین در روزهای اخیر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99800" target="_blank">📅 11:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99796">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXX0Z8I46-5GUnDGZcp2DPeVH7zXg6PmFxvmz90-JcQ7bxM5h4xj4OoIZeXkWiiogEwg3YNfvulo04peldKwLfOxtPzxp7U6MqyuzWUQA1Yw_SsDfKOdmSQFhBXKPKsVUU3RqKM8MZudUBkMxgwJu29JP2YGJcOj8_CW7w9BuyDEl8J54Uvx6CvTo2HIuwbc0XMePqHR3n3zWsLC1SJyXuWNbDT5Iwqd3CwDhwWcZ8oBHn0AQSJxnsdZ7gSTvaGt8Vpyn1irphLgwTDUH7GwizDOHJjxfftwF3yoIsferV7o4nHj1BNWWnQpG13lTeL4HL0jfD_nRwSEmni22K270w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hdepc5GgDhMXTQU19qh4JtWIH-q0CVtsPxdP-KOoMH7dFEc-mEy7EBiA0ZaZrpbFUtwFcCIb5zJIkVNI8kXVCo4cwrXaT21VWmun-DnDxjh-c8o2WUYUA1MtwTz68Vns3yhgs8QjA4s9C1dv9DEabDZoyt5fZU-gtQbHNu70vEdNlaRNwLGK2o442fEsVgV9jRA2HHfQTcKpyUppwcWptoecYtfaYFd79ZK8xp3HawnG6vIIgM8Dr7cJAnKhcgX_UoYHqH7xDiCew5TkbRQrhWjIXUOLcM6g3th4KAa8tbaBcdSTp5rTcIc9Ag5QK0EGBdiqCQVjnl5AzNVicBkg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFVjOqkdSVVxh3Si4WZB75a0pdhZkWOuT5dozPH1khU05M2_cXkKGvV0lWF_c0vF4RGyBBFSjN9KHhuRBvsGpV-E2HYCz1zjU3-O-fwDqglGfFtbJklMZ5UEZUaf65I3JJ1oisQ0s412fXP3U7f2DzNDIuy-55wVnwGnNOTfowcAz-JSkVDahvSGbwrEAy0TeiOMzh2ipCU4a980Y6VBLw7zuXjNe8WeXLIh2e4UI4QFj9xAcpjsx0r-2JDarnZkflzYjofAvthQw2iP1_EStTHVcDoF6FpYlDX3sSrU8AUsCwVw0gKhxFbHiDByz17FDBDXwJaBr2zvZEUMqKfTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IPOSodF3355N1-AyK_8cPgW8-GVhpAH0GDreoRK0Amn94xUt8BaZn5xb95zDLK-T2shMfq9eOlzmD48F6sdRkzKLfOWtDLgnEVzAiJU4nLT41GlybjnuTxEVonfoDtckFwo4rOA0g-22RRaFpruBH6_amvcg6LvsqHQYfhpyo9DmzedAdLSplsg-I3-9Vc2H24302l6PIRcX_-dDHtT1GMfJgRmqLqg311jMX1dUG7MELJJjrAq_Gmjz3ZZENCwDS_L8AIEz1_C4clercDPYOWp9vme9H7DZyNAi43TP4uu0LH3kJGqm5KNVrTW_Noc2Mnh7t1CUhXOiYUFwG7gsAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇦🇷
خانواده لیونل‌مسی در بازی با سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99796" target="_blank">📅 11:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99795">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aaab4e8ef.mp4?token=i-Ur3SWoALiK_imXTCvxlQMCEGvBRTUmha3KtR1O2KC3asuZXGN2o2es5qMKKGNDp7qxmE7CnfmZmMlhZQHPxBwiPAcPt2MiEpubKotTb5303MqSt5CdlOwa8h9aeQJn5ANrKhULeYUL3yPWKPGuhG5YVLZC_1nbKL6_6_OEA-t_WjOuZf3gOfVN0KYg4iV4nBy7cN442ztGGvcWPW1TtOF4WWL80RupNY5dbWrOnIso1FOBy00WfYczo_qWhz9-2mcPc4iFBMNG_K5Wj2e0ihgi7cAL4oeQyoNAbST5j8Ajp84BYnJ8jAxjCb-8H7TCqUUsGVWzwAUwqFU-Tonr0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aaab4e8ef.mp4?token=i-Ur3SWoALiK_imXTCvxlQMCEGvBRTUmha3KtR1O2KC3asuZXGN2o2es5qMKKGNDp7qxmE7CnfmZmMlhZQHPxBwiPAcPt2MiEpubKotTb5303MqSt5CdlOwa8h9aeQJn5ANrKhULeYUL3yPWKPGuhG5YVLZC_1nbKL6_6_OEA-t_WjOuZf3gOfVN0KYg4iV4nBy7cN442ztGGvcWPW1TtOF4WWL80RupNY5dbWrOnIso1FOBy00WfYczo_qWhz9-2mcPc4iFBMNG_K5Wj2e0ihgi7cAL4oeQyoNAbST5j8Ajp84BYnJ8jAxjCb-8H7TCqUUsGVWzwAUwqFU-Tonr0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
روایت حمید مطهری سرمربی فولاد از بازی در آوردن علی‌نعمتی تازه به دوران رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99795" target="_blank">📅 11:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99791">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5BdXJKQqFXGep4fH9sffnvZGAQn9O4uxDYeigtGnUgRyLZyfM4mGjIgHJ_lb5L-K1m8CAbbGePUMxK1_eqSbpJuRFv2ZEE6yie6ghs4RvMq_ILeu-rq0aB1YInu9xrIk7gJtL6kTOhFZAadS3ayCI1BxoXjBJJtQV8gNeqAEU8jppVoKl9LD-gsnuHDVOYG1xhCaIm5lsA9zFqAUJgONgUB8k8bJII3msP20HmU69jsk3oxNSNqUtukcHYUjHQKiWaUGE5tug7h2EfwQHYn2-bLCFn_HI_U58KE9P-BLkLRRagZsb_YcygJFP6lAIbVGjBSLqwl4M-bL_HmWxJ8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQafz9CIjMBihYMLh4nd20Cf2VptQQQAL1BX2mFuD8DJupgraS66IeXwhYj6WoEsE5kUMwuPtWo7oGKorVHt3xeZ_gCOZAG8TtiFZGzZ1cTbXZp_edQFnjHmbqtQUjDtOKs_6h446IRy41iAlCoc-I82_Kv8ZAlRqHESWSRXw2C-ZgQWGM_Rdlc7LgSnma8keurqE9xkpEDXOtepvZTX7qazkiql0xJjmSizwLrenJOTbtFjugRBL2MRrUAZjsqbhF7YO-LQ_YGQZKNdnhuTjZIaPQedE30ZJ0uClAkyn66HqwRAUCFECXsF2k9Fj6rlkA-1tZjuUhHs3NCOyYGDDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
فیفا شروع کرده به فروش چمن های جام جهانی 2026 با قیمت 450 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/99791" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnQ1HapZxWj_jXIYr3llnXe_jha9cdlNMr9NEXKJsOApDT_L-eEczLF1ejl32FywV5R6aQhe058QmQc1Ym0QCV3JGyGKGXr-VGrsB-aTsV6oJrcmonZ5mzz7us7t2-HRr3WGFdmkLvUy0FWiU7vELu-rCSHKuV3PJC9McYzR8zfb40zQ3jV73D6MzjZlWY7OW4X0EE_OXBWYAjM0kWp6pngaIZiXpACWGgUPTKFwQ68_g5VMoZm4NyYR2umzQ6qsLWprmydiw-XrJ2BWSUoToz7hpvTphO_kndKI9Y3C8vy5SJUOgJCpqneErsR3sdgV684L9UvmrKdZEt3E6cFf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">� بعضی‌ها فقط پیش‌بینی می‌کنن…
بعضی‌ها از همون پیش‌بینی‌ها درآمد هم کسب می‌کنن!
داخل
@betegram_bot
می‌تونی شرط‌های برنده رو ببینی، از بقیه ایده بگیری، شرط خودت رو بفروشی، امتیاز جمع کنی و جایزه‌هایی مثل VPN، گیفت‌کارت، Steam، PlayStation و کارت‌های مجازی Visa و MasterCard بگیری.
⏳
هر مسابقه‌ای که از دست بدی، شاید فرصت بعدی درآمدت باشه.
👇
@betegram_bot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99790" target="_blank">📅 11:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99789">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=PgREgyw_NxJY76pOSZZESRzqmJW3bdUowmKQW0rc4BQBppyToFYWpCYJ1GTYDPI_CpuGno9DCmbamzbybCSCY1hOmAmfBsPYk6MoySvUwCKxUU_WZh5_NuQBVUFPpx9KMc9OlmzXIOfd6f_TCDmETtw5gobwqMfJZ1AMgqOHgnv1oqy6mlt1eO5oF6yvgalBeQ-uVc54rLVuc22qryQwIYmfj6sPgEcZgA5bYy9wbYREolgUKaVuAvbegvOtvk236fDUFkYxrhYiYA5K1ICJtJeQR4WgZM-Nz419g1VbeO0aVbRhvIPQPXSck8lfHyDWZ3wbWCwy6lx9AvzWuiG4KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e4fb76e4.mp4?token=PgREgyw_NxJY76pOSZZESRzqmJW3bdUowmKQW0rc4BQBppyToFYWpCYJ1GTYDPI_CpuGno9DCmbamzbybCSCY1hOmAmfBsPYk6MoySvUwCKxUU_WZh5_NuQBVUFPpx9KMc9OlmzXIOfd6f_TCDmETtw5gobwqMfJZ1AMgqOHgnv1oqy6mlt1eO5oF6yvgalBeQ-uVc54rLVuc22qryQwIYmfj6sPgEcZgA5bYy9wbYREolgUKaVuAvbegvOtvk236fDUFkYxrhYiYA5K1ICJtJeQR4WgZM-Nz419g1VbeO0aVbRhvIPQPXSck8lfHyDWZ3wbWCwy6lx9AvzWuiG4KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
لحظه اعلام خبر درگذشت گراهام توسط صداوسیما و تیتر: به درک واصل شدن گراهام رو به ملت ایران شادباش اعلام می‌کنیم
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99789" target="_blank">📅 11:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99788">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=kkvrAPyCYmp3f6A3_9xWrXs7aqjwZHh15tlt1YvvAB-heYbuk8w4hgxIz9K9HU3ODV7yc2SaDLSw9lT-nGMoOLJzQZUy3ZhnqW6Vola-1FxZzg6QXp90Uw2YhI4ND2a7dl3gweZu521nErLP9lIShQbaEITvjWJuNC1N6NklLyf_XrvkKLhCIpc0kQpfQDif1CsCp1gJIXB0flw0fHQsy3-WBo8IUA316dBdT-2Boxz9MjttWs-ptE2F_sZq9joV3sEhXS0xqGfIrGgQrTA0GsfEDYaKbMZCCijvB62yTN_vLTPFfHErnTIZ1yg-nSEahXN1gMT3XQUMnHLk8PlWjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f1adb911.mp4?token=kkvrAPyCYmp3f6A3_9xWrXs7aqjwZHh15tlt1YvvAB-heYbuk8w4hgxIz9K9HU3ODV7yc2SaDLSw9lT-nGMoOLJzQZUy3ZhnqW6Vola-1FxZzg6QXp90Uw2YhI4ND2a7dl3gweZu521nErLP9lIShQbaEITvjWJuNC1N6NklLyf_XrvkKLhCIpc0kQpfQDif1CsCp1gJIXB0flw0fHQsy3-WBo8IUA316dBdT-2Boxz9MjttWs-ptE2F_sZq9joV3sEhXS0xqGfIrGgQrTA0GsfEDYaKbMZCCijvB62yTN_vLTPFfHErnTIZ1yg-nSEahXN1gMT3XQUMnHLk8PlWjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیرمهدی ژوله: به پژمان جمشیدی با تاکید خیلی زیاد گفتم به تیم پاس نرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99788" target="_blank">📅 11:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99787">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=BgYBQdExaGgF-zT61CEfVPiw8NXWqWv8OHC_GZEEXor2vIEfUviwUqeKLHxSKOPl1GRGjGurm7e5obAvAc-S-TJhX7h7JRQ9JisUH5kZdqa2tYOavL90NHqJLgZkV1mzt0jN21RhnuXj5HAXhguKnvTNxJ2WNPkXJBkP9gQzMnfdK3fuz6O7lr16MDCVfQU_0oQoqGlU2ZCChiih1gY7qH0j45a2IpI9x-6wlfsp1-E1xmLibKaLL2LyqS8OmyL8oaQK3U3tXElqTBdeOhk1YlU9AP8vnCrpzh3WNtFnFACBs6iFuA8CMOOTXwBvdX6AnKx3pv10ZOZhQU111W8nuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e66e95548.mp4?token=BgYBQdExaGgF-zT61CEfVPiw8NXWqWv8OHC_GZEEXor2vIEfUviwUqeKLHxSKOPl1GRGjGurm7e5obAvAc-S-TJhX7h7JRQ9JisUH5kZdqa2tYOavL90NHqJLgZkV1mzt0jN21RhnuXj5HAXhguKnvTNxJ2WNPkXJBkP9gQzMnfdK3fuz6O7lr16MDCVfQU_0oQoqGlU2ZCChiih1gY7qH0j45a2IpI9x-6wlfsp1-E1xmLibKaLL2LyqS8OmyL8oaQK3U3tXElqTBdeOhk1YlU9AP8vnCrpzh3WNtFnFACBs6iFuA8CMOOTXwBvdX6AnKx3pv10ZOZhQU111W8nuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
میکل‌مرینو فرشته نجات تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99787" target="_blank">📅 10:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99786">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=QIgypOu8EopJ0xFCIJ6YcUdONCBFnbfMeWxMbriuXB2vgrwtTmHRNknGPIPoSdv7LPK9wpwWBOtbEnnSlwXiE-KniETUUCuNag0UXPb3cszeXepeB2NC8qE-riEeA2vU6Hvcr6MGG0UT2mjBU-ZAk69K4dyWHceToGU1-vkCvSuCQyucgMrpCHn3gKGHep1Ngb5LAsF7UY1-qab3VIvGr38IQSvG-n9kTyTw8p3Q57UegUB3b07-17_u1QZ1JFD38RuBCjdeAxLBWgp4CdNsnoNFnJcGok81U1P00MjuwXYpJ8cbhcd3JIhd_qKK0agcYFxRl6KxX9z3aefHXK1q9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e18c3ee23c.mp4?token=QIgypOu8EopJ0xFCIJ6YcUdONCBFnbfMeWxMbriuXB2vgrwtTmHRNknGPIPoSdv7LPK9wpwWBOtbEnnSlwXiE-KniETUUCuNag0UXPb3cszeXepeB2NC8qE-riEeA2vU6Hvcr6MGG0UT2mjBU-ZAk69K4dyWHceToGU1-vkCvSuCQyucgMrpCHn3gKGHep1Ngb5LAsF7UY1-qab3VIvGr38IQSvG-n9kTyTw8p3Q57UegUB3b07-17_u1QZ1JFD38RuBCjdeAxLBWgp4CdNsnoNFnJcGok81U1P00MjuwXYpJ8cbhcd3JIhd_qKK0agcYFxRl6KxX9z3aefHXK1q9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
جوری که جام‌جهانی قراره به پایان برسه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99786" target="_blank">📅 10:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99784">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dg9VKKLPATwEn1zmyI-eMVZue-cynrZyOSsM5bW97wIX0wT__rOU8hO4TRf3IyQtUm7SUe_xE7Ghvn4BaAEeXFHHFditp2JY1SZgEijJ6suMfr9Gky3NelLKXzmBoPGx9YnvLLKPGdeVI3ggLABuu90YJqTiIhV2DNI1VFPkqPQLrhAUP-CmuZ62vtLOlrKSCvejRMhv__VK3uliKHyKR9lbP1DdLVX1chwsaoQ8-tQkgyF1utDLwrrr9ZSdsC9j-_Jxj3TKBAi5kV4tZdOLLeFAkpkH4NOane0n8jaZnMn-9LGw0SoWk39DKPZtG3r27b5mAIC-ReaNK127baf_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulEqZo3ODmo7nbSfda2xlqp0Iv79atwd62zoYpEKVkVSioMj-YoxTV2_KmaHgB8wE5u3OAsBHdfymAt7R6FblteSWRGdoEfd0rmWUxmNp8G9lY8sMx2C6lzmf1kPz5an9mS73G0xDhtyKIUr4_00hVkdpRfmtCXrF8yKXCy8jd3BkCDB0te0qoMC-X4-Ejwg_RJKb6dEhsUQmNMSUUxDU0bOBZzYxBjuIgqlJEUHLQThHltYBhpCaBuB92B_L0GAcTpqmuplGBEsBVO-8JH3D_4yE1LCrBEZ0EWd1yL1Hv-cKvKWkNJM3Et6FXpqeBApDAo64MWKh6meVqXS7MEwgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چقدر به دروازه نزدیک‌تر بازی میکنه مهارنشدنی‌تر میشه. انگار بیشتر یه مهاجمه با قابلیت‌های یه هافبک نه برعکس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99784" target="_blank">📅 10:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99783">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=CZ-0i-blSRaZUNhnHgTZItzQTKvnaF16skMkZnmZ8yp6RcqRhtvjQgV6K2nOnRz_32CAwqaRoH5sia5Ke_--bxOYe-Wtzog5tiFDEpa7tT3btlajjbjer5TepZUV_49IsWlUN3L7eC5aVn194KklA-H4h60GG_PgZ4dmbIOhlbidn262kqyiudADqGeIqTMjZukarqsrtfvJc1kWl4SrBVv8EULxmb93DG-O031C6rrNRTvMUIbFeKBP4lVxooSdZDvp0sEnnPpuaT9v-7sP7JGOsowG7v1dlkdq5dBlkyhtucHVQb4ndaM6a-EteqB3eW-jD_ZFebAkPwJmqi3_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f570ead6a7.mp4?token=CZ-0i-blSRaZUNhnHgTZItzQTKvnaF16skMkZnmZ8yp6RcqRhtvjQgV6K2nOnRz_32CAwqaRoH5sia5Ke_--bxOYe-Wtzog5tiFDEpa7tT3btlajjbjer5TepZUV_49IsWlUN3L7eC5aVn194KklA-H4h60GG_PgZ4dmbIOhlbidn262kqyiudADqGeIqTMjZukarqsrtfvJc1kWl4SrBVv8EULxmb93DG-O031C6rrNRTvMUIbFeKBP4lVxooSdZDvp0sEnnPpuaT9v-7sP7JGOsowG7v1dlkdq5dBlkyhtucHVQb4ndaM6a-EteqB3eW-jD_ZFebAkPwJmqi3_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو هند اینقدر حوصله‌شون سر میره دست به همچین کارای کسشر و احمقانه‌ای میزنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99783" target="_blank">📅 10:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99782">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUK6SLFNlz8bBvcp8SyORv0YD1e6p1BptCct6Hx1y5hFqn2hb0i0WoTZJJl20ZoWqBJiwy9DQZAmJO7kt3I3sl9DS1IMIg3Joi_fLY7V1A8NyW-0BQtRo3TYPtUZDubY3N_6KXdBmqebs5JI_JvkTsReumhOkYZUtgaw-MIwtqo5Dz8EZRUel6YPIZkPCW2uwGjfZ8-2mzQYCw7dXEMKEBRtoldIkulXWBijIQUdqH-r5A0KlsjopkrejYX068uHoNiGTBu9MfLvVUy-FyB9eDqOw5H8T92niNfEsGiV4SpO82eNvjY50JFtcu-NTM_271y2GiPW50Vc6KY9OaXkhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیندسی گراهام سناتور جمهوری خواه و از حامیان ترامپ بر اثر بیماری درگذشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99782" target="_blank">📅 09:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99781">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=MuNX3ySVfFG5r5VfQK8WDGd9WTQIXyDiL-uYVnzxb2SE5aKJHuKNzz0sHkagEFPckbatv5z7RkP3HHJ1BR_lusiFXfd9j-ZApKLGItF7MxwfpDCRLQP5-g8-mkHV3wjW4VrVsTPw0e-91M0GC8gz3SNkxvF2XzJXrsByAbjL7MxWTRAweSGtZlQ8rb0trbAnNWlRLEhwO2CY8rOdBht3MFqstn2rn9DXvyHhtaBtPutTXhRfr22KD1kq9wsIihrEuYIiZSIn0qBd4hrFMtDqiVL8C1X0BYD5j2rf5dbRkZt_PbZm3e9UC41DKXRXQAp6AREcW-caKn9CwLwNXUE3aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cccb9946.mp4?token=MuNX3ySVfFG5r5VfQK8WDGd9WTQIXyDiL-uYVnzxb2SE5aKJHuKNzz0sHkagEFPckbatv5z7RkP3HHJ1BR_lusiFXfd9j-ZApKLGItF7MxwfpDCRLQP5-g8-mkHV3wjW4VrVsTPw0e-91M0GC8gz3SNkxvF2XzJXrsByAbjL7MxWTRAweSGtZlQ8rb0trbAnNWlRLEhwO2CY8rOdBht3MFqstn2rn9DXvyHhtaBtPutTXhRfr22KD1kq9wsIihrEuYIiZSIn0qBd4hrFMtDqiVL8C1X0BYD5j2rf5dbRkZt_PbZm3e9UC41DKXRXQAp6AREcW-caKn9CwLwNXUE3aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
صحنه زیبا در حاشیه بازی نروژ و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99781" target="_blank">📅 09:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99780">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=iu09V4LnCM-6_JAy2pX2AXmSgnMkAyR0d-Dqx62RMdJ5cvT6rPieI_bShj_i0BFNxS6oiQlIfM2lsC9QfFO5nw1w6f5R4L9f2TqNdcktTxs1pzPbbsexvpRv55T59GGCcK5kd2CmcaVnPvdYiIiMVu0HAXIR-smRluJRfcBfNPCC5r4kj0-ROgGL_Y1j202wJrhHbgyFfl_1o16sIZCs3ij6BO3XB6N4P6doQs4DdP7MQFyKM3UrP_aJ3swPuHVkGQTkNKb8WROPlbz5Kq-LTNwgOXrtffxG6whipaJy-UmiLDMQqXEwYfHlHUcDauiG7KAfIONA1rUgRR9lSqSwuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5675db48a.mp4?token=iu09V4LnCM-6_JAy2pX2AXmSgnMkAyR0d-Dqx62RMdJ5cvT6rPieI_bShj_i0BFNxS6oiQlIfM2lsC9QfFO5nw1w6f5R4L9f2TqNdcktTxs1pzPbbsexvpRv55T59GGCcK5kd2CmcaVnPvdYiIiMVu0HAXIR-smRluJRfcBfNPCC5r4kj0-ROgGL_Y1j202wJrhHbgyFfl_1o16sIZCs3ij6BO3XB6N4P6doQs4DdP7MQFyKM3UrP_aJ3swPuHVkGQTkNKb8WROPlbz5Kq-LTNwgOXrtffxG6whipaJy-UmiLDMQqXEwYfHlHUcDauiG7KAfIONA1rUgRR9lSqSwuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
واکنش تند فیروز کریمی به عملکرد بازیکنان نروژ!
فیروز کریمی با انتقاد از تصمیم عجیب این بازیکن گفت:
«اگر دسته سه تهران هم بود، پاس می‌داد!»
😅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99780" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99779">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhV3PcdchCS7tpvcv0IgPAZi1YpLiYKFGvfFrdUpZNZjBj5e1bcQOHjK826XvmZKZyfu2KcKGZSpvFC-TuVwybio6uDbz6LaTBfznJ_wckAWFCy8yWGwrlqQVKyIVUQy6IWS24Z1pKkxM5uqgA69bUA7Z_XddKcsvRdjg6fV38Z_sS3hPr_PNxM-vZz2xN6zgx6I4KjOU6Xei4jsFnqL7o3_gYz_R1TJNqrRWjgR2p-8vv4zrbsB5r_uq_oiH3Wfd8h5ZWqSBSPH6MjN1uKsSUSS2Mo_yPVy28BcvHo_pG5fYKvwVFkGoi6Tm2YslJtUUmlhqOifBnZzl8YWMW2Bug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک امروز 1 میلیون دلار رو کانر بت زده بود، که تو 30 ثانیه اول باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99779" target="_blank">📅 09:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99778">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=b7wQBQf7_JkaHsMvI9mQ2e-yVHG2HErJ9IdMRcjo6NVBg5yW3GtKDTpUTnp3yEI-jE2qvZNdhz8pfnoGAKbARESSHZSFpU8SLlEWVrg6y9p3rfQUvO5_2j6fKOByG-tQPTlp9HvvjRZeRbijZN1DAFRfXipIBBtETN29mJysTwZyfDLeI8y8bu8XVJphNvcy8JjtRy9EiowalybcY2mtdkpXzXd-irYpbDrT-AffHrAPhpwTGe6fX1zJhdZw32LNGGaPxETB00lMNmyiPCyJuegSmAUB4ppU9dHNS-DBbSUYY1SVklKS8qhCboe7QKZjRUd-4GjqWhw8y38aDGqycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9322a318fc.mp4?token=b7wQBQf7_JkaHsMvI9mQ2e-yVHG2HErJ9IdMRcjo6NVBg5yW3GtKDTpUTnp3yEI-jE2qvZNdhz8pfnoGAKbARESSHZSFpU8SLlEWVrg6y9p3rfQUvO5_2j6fKOByG-tQPTlp9HvvjRZeRbijZN1DAFRfXipIBBtETN29mJysTwZyfDLeI8y8bu8XVJphNvcy8JjtRy9EiowalybcY2mtdkpXzXd-irYpbDrT-AffHrAPhpwTGe6fX1zJhdZw32LNGGaPxETB00lMNmyiPCyJuegSmAUB4ppU9dHNS-DBbSUYY1SVklKS8qhCboe7QKZjRUd-4GjqWhw8y38aDGqycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس در نیمه نهایی به آرژانتین رسید!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🥶
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99778" target="_blank">📅 09:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99777">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=T5P5wpCYyye7APizEhnY4FkLx1F-WnJMbqFlWv-Ho4AFN3UvahF_81VVtmbpNE2xez3Mv5xh_SCILCRl5jqjRmOq-ON3L6QsfNHXkfYGBXUsjHt04u8MkkIkD0K851z5uZ1adc-QmKmj9sGVHx8Wa2jNGugwSccF_gv61GABlbp4sodzqzFE8QPwU_05PW68SmLvd4y_0NZ6rsR4FRyXZib3DZsBhR9_uto6LNIfVo9_4fE6vUtRAFFeDh8C3-O4Rq0PpkIcKK5LcZY9gIoj0dNefJ0dCvFAPaX4i-wrANrdEgvmasf18tcLI8ESVxirKnLJ7IXkQXtIkB4bHGxNjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2c616406.mp4?token=T5P5wpCYyye7APizEhnY4FkLx1F-WnJMbqFlWv-Ho4AFN3UvahF_81VVtmbpNE2xez3Mv5xh_SCILCRl5jqjRmOq-ON3L6QsfNHXkfYGBXUsjHt04u8MkkIkD0K851z5uZ1adc-QmKmj9sGVHx8Wa2jNGugwSccF_gv61GABlbp4sodzqzFE8QPwU_05PW68SmLvd4y_0NZ6rsR4FRyXZib3DZsBhR9_uto6LNIfVo9_4fE6vUtRAFFeDh8C3-O4Rq0PpkIcKK5LcZY9gIoj0dNefJ0dCvFAPaX4i-wrANrdEgvmasf18tcLI8ESVxirKnLJ7IXkQXtIkB4bHGxNjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😆
😆
😆
مکالمه پاره‌کننده دیشب هومن افاضلی و خداداد عزیزی. کپشن اصل داستانه⁩
من از شجاع پرسیدم!⁩ شجاع بهم گفت! گفت که بدنامون خسته بوده! خواب بوده
😂
⁩⁩ ولی هومن
💀
⁩⁩⁩ بعد همون شجاع
😂
😂
⁩ گفت غضلاتم همه گرفته، عضله رو ولشن!!!⁩پاهاش اینجوریه دیدی که
👐🏽
😂
، اگه پاش اینطوری بود
🦵🏻
آفساید نمیشد ما الان بالا بودیم
😂
😂
⁩⁩⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/99777" target="_blank">📅 08:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2w_muJKyB60H5mDdF4f0WHZtUirDhfzMGTInEYyOgfeiQ7vlyqmazqv6UKdfW69-AfX7-Nts8GXu_9pHSVMbfwAhpg1t4oZDy0vlVODUc6iLuMbU6ZHFaRw-I9JIW5gy_MCgRJAMnrInjIIpUIW--V-vipYkya1TjPeyLJL44Li9pOz9NYj1ySXGtU6Mrn9MQXDW_uT4iQHM0IfKefWg8oWNClpLBNzbAIOYc0BlSlm-3CiIDH-2jMHiRxbg5aPwZekr3ZcWYSYVGP1FpGZyBYKTvAvmcny9kei7IalWfhgiXpTHGxdF4GKZ12O1Tfv9Tas69UBtRVX8PU5-wyPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی اولین بازیکن تاریخ شد که 15 بازی در دور حذفی جام جهانی انجام داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99776" target="_blank">📅 08:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99775">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg-WOzMGQTksIhTaOiCI2AdytehGp2hAJ05XfR_AhR7BWNiMawH3nZobBG54qgaOOCrn4mkpepLaM5SvqJCCPGL4Wk77Ss8rDQrfazG9y5LP1iYhicffexEmqQMsTcwWpksWJ2xpadlOXqF7mvWl_jBwGbIFomnbsKYtNR89n4VWXQMNeNA-43kRdAXJBt1y1Csnjl8fKxJTsUFCvoJvlU-PLcMkKJzk9T46v9K6utlBnSXvi3pdLWXLS3gzsllfcPoW-5z_N0nKIBuncbisyU2biUTcSKFFdXABFLllddcjDeins4kXQMHP7dCs3wgnUjmqtIUJnqFDOpjfo1GzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🎙
🇦🇷
خولیان آلوارز: مثل یک ارتش پشت‌سر رهبر خود لیونل‌مسی هستیم و هرکاری برای قهرمان شدن مجدد وی در جام‌جهانی خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99775" target="_blank">📅 07:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99774">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlWP0ZmDPGqh2xv_FhzvxnfFOOpqUjT-0eF6AbWbl_Db9jc0ZZwu0l6oLpbDQv0v35PQ-ghjwFHGmPSAJj2Es9MgT_wEE8FBh8NVIJnM1-TuvYRoBJfVuxCxjRQP7LZTbJo8o_JfxAtoKUVxep6HCJdkrshoVNQo_5zuwxLdRhqUZBwuJUcLdca8WdObHqzH_8CAVit0jXmFA8WRrUTajIFk0jqyrHQmnafQQk6P96y2llt1OG9JG70_ZWaGZda5gRcURo6guqdeStcAYv9cagmv2KWzrcpQppGxKmc2eZM-yDvR7Q6yh6JayNbXsrgs9S98temRlTgEB74JLz_Kzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تیم‌هایی که در طول تاریخ بیشترین تعداد به نیمه‌نهایی جام جهانی رسیده‌اند:
‏12 بار —
🇩🇪
آلمان
‏8 بار —
🇧🇷
برزیل
‏8 بار —
🇫🇷
فرانسه
‏7 بار —
🇮🇹
ایتالیا
‏6 بار —
🇦🇷
آرژانتین
‏4 بار —
🇺🇾
اروگوئه
‏4 بار —
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99774" target="_blank">📅 07:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99773">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQwQEvPWjOR9kVL_CE9hIZgTrn-4770ZFXXX3llg_EoHNoQ9zWyExs33J4Xt1oWY0uKIw85KAHyJaw0j27ORgwaNsRi-X4uWVSZltxsBUD93Sg1t5C8amaLZGpvcfTSA8Eh46vyyvhyqxkL3Wkm4427M4X2uac5CNMYQHF_UB7IveYOBQEqW8Wkei52Q7yoDUtN_3UIMD05si2LFg8j34tg38jH8Z-zUQyHts3Snczgd4LE43t1Q_CI0fThd3n6Ai8L5u7EpAPuLb5u50QSvIhFl3y_B0oeaasleVEOqTRxDnf6AWeqkapsdbJQ2EJpBqh2yHX7nmIoFnLgWx1yhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇦🇷
خولیان آلوارز رکورد مارادونا با ۵ گل در مراحل حذفی جام‌جهانی رو شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99773" target="_blank">📅 07:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99772">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgoiCt-Sl_SpCnxCYe4adX8CLTGyvxkT7Lfcn2Rs4zHEoYvixGD91Bpu2Sk306ogEh7gXpHVVXCY3y_cirkzgERAY-qdAYjmk-ECVfEVVQXwNQ2369NyASyNpg_xo7XkdlAcVv0gEkNetKaUOy9jwWlbRcL7OWwmo_r1mUKjVghyCcog5c_awPQskcG3STs6Dv6ozeZPT45urUTV32oCqO6ZYBaaU1zQyGaAxeTeoBiHJBh8KiYQzvgde7BTKaJlmAEkgeMHMA1FMtqx8YVX9L2j5cmXeXBlOFTem0i1M1sbcZH65L4KtrAukqR1cUnxeqLSCf2PXs2QnUgXpnttPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی آرژانتین نخستین تیمی در تاریخ جام جهانی شد که بدون مصاف با ده تیم برتر رنکینگ فیفا به نیمه‌نهایی صعود کرده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99772" target="_blank">📅 07:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99771">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kC2qx8urKm1fGC9gbkdQMfP75gErl4jPUq6qvEYmrPd7Q1GreZ5NA8t_YAmrYB2EHJnZrGDLbCBQHQZ5dq2gdEiXr73T3kthI-iUfWvqTJHWxH0w3pyfMxc9UbA_lA0ut-1zWonjG4Yyp90rKR274SzjH2utMGLYDXlQGMu5Ae0tkf3ImgJCqr7YQSTWbuRNdWGy202oGgQB-EWJzWcIYathxQILYcZHqQhaupSMJ_fw9yNhV3WjR3Ihf5qo5fZszPhW_IrMyin22GOqsVfcQFnki59PlZruqFk7Vvxvffz2KCCtx_vvciGKY9fITapHUKg1nhTEYHZRQSPBWbn3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🌎
| برای اولین بار در تاریخ جام جهانی، چهار تیم برتر رنکینگ فیفا در مرحله نیمه‌نهایی با یکدیگر رقابت خواهند کرد:
🇫🇷
- فرانسه (رتبه ۱).
🇦🇷
- آرژانتین (رتبه ۲).
🇪🇸
- اسپانیا (رتبه ۳).
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس (رتبه ۴).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/99771" target="_blank">📅 07:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99770">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=L9K3uG4ar9tOS28e5w3sKD_aMOc3yJvX1-c1G3b6-PHiFR_ADSMsXVUY6i4AusiRSphwpeKSb7Rw2fF9U-5ED49mv03Pw2s9q0Ebp7oGaWt7AKdnP7pGKegnvB4gTYM4lt33WbsxIWGt4Cbs_GqtCOztA4jqGcQ2EFu6HzJmsY5AVUZU7smkhKIcYAacigniRPu1J8PqDedJ9XTXf_bC_rcsczqIbu6tIY10KgCL8413KcTnr4d-H31PDCDmWDg4gFN2uumtPALb7XN0EoOiZiMwyN0g9HzKwHbOBGCBAoVQn1GRdQjt4etUlGl0PsEEhYxCf9CZj4zyM3VXgl1VgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b30f5ad6.mp4?token=L9K3uG4ar9tOS28e5w3sKD_aMOc3yJvX1-c1G3b6-PHiFR_ADSMsXVUY6i4AusiRSphwpeKSb7Rw2fF9U-5ED49mv03Pw2s9q0Ebp7oGaWt7AKdnP7pGKegnvB4gTYM4lt33WbsxIWGt4Cbs_GqtCOztA4jqGcQ2EFu6HzJmsY5AVUZU7smkhKIcYAacigniRPu1J8PqDedJ9XTXf_bC_rcsczqIbu6tIY10KgCL8413KcTnr4d-H31PDCDmWDg4gFN2uumtPALb7XN0EoOiZiMwyN0g9HzKwHbOBGCBAoVQn1GRdQjt4etUlGl0PsEEhYxCf9CZj4zyM3VXgl1VgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی عجب کیری خورد تو این جام جهانی اسپید طفلک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99770" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99769">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIRtY84LkLR5G0zE9pc5wtAkACmPhp2-fV13mHZDfRO00PCfqW5T9LlZLKCgeTenGaDZpKqSU4AjELw-WtQrKjinpaaeqoGuvX0Yk9GLa4k_Y5wjFddoNTJ6c_YosB3VR2R6ddS53j5RllDfgUwlDWywxsF5YeairJK2W_yOWhSqtMwu8ASHvOw4sRuvTKx6cxmN-yjXUreE13Y3yLpa2F69bzz9FoJAE5ZjXIW5Amqi9Wi6LlwRnhrFpSB6gVvLFB4E_1Pdga5cLVg_93-tFDZWUOc5LYQCHNXxR1fCbHfSnEdNtzwiMkERPnwV46CDCprYyFcFd5PSx-W4tYzCtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🥶
🥶
قهرمان رو با ریکشن نشون بدید
🔥
فرانسه
❤️
آرژانتین
👍
اسپانیا
🤯
انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99769" target="_blank">📅 07:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99768">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99768" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99767">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n45HngQpMSghUg1dkIgoHoNtsmM8AX_Uedsdw5cAzDEGml-CqFeKyW7-TYddeJhIj2HjdltJ7N3ADvemuZtFSeA02PBh9Wp-YxShasqZZCaSoZfLJOwGbjfBBvhUCNYeFM7LlO9Mc4NyAczc6VPl1e8Kz6fxpF9ff2LyNwp8Pw-SJcVvrn5O2Jctt3LNu19ts4umzxWwApOiNzpHrHAnZY-Rn0QVbQ4cTmKfaYwnNVfJfTM_418moqlaVQmlZwl8bHJyU_NJ1eZlAy1CNU6JpGT9RuveEVQbYJGQK-aE790kc57Sx42mcIam8jWYFpkS1HnJCj01KmM6ujAvHQdhFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
برای سومین‌بار پس از دوره ۱۹۷۰ و ۱۹۹۰، هر چهار تیم حاضر در مرحله نیمه‌نهایی جام‌جهانی سابقه قهرمانی در این مسابقات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99767" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99766">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWg6_cy8EaxRAxLN4EFS8EMx3a1Ft2FkHEpT0JCro-BguG9uPdDm81ACJNo2PTlyeD7D8a1RsJ7KcFHMU5Io9U32IfKD2gX1XCSWhfCCP7CUKPRcZcHelWLOR50wmeHUbltkc3rSuT_KaeXwzYJZnApB3g_FV8jmPlLTdlVnk4f7si8nIFkKYsxwIXZ8yy7HBk57ndB-x-7biRFUdic622gFFVL-bkE3X0dDVGObn81hBHgQG03LzV5IMQQftNWX6bYC3CIDWPUW40tFkX0B2Q7f-JrTUPeZ0JpLH46FocWMo-S09rL_oDagRKLxfbKzZqPyiAhaKSWzEcdC0-S1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسو ببین یا خداااا
🥶
🥶
🥶
🐍
🐍
🐍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99766" target="_blank">📅 07:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99765">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DVtHcDOYuseZN_jph6F4vidFVhG9_gMS1SUpz9Vihmyc5bwbFkq9Mjq15997PCYUvGM63l26EYuWFKv9OWJgj8cBw-COHVqUwBjbCw3QIQWUXr8ktrEXcz6FHu6etNOrf6LvHAY88cSCxpXWW4YcldxVx6ncHKdZQCTu6xEjOkWqm8uBdleh1aHnHdRBjQtBrvJHhF9M9B5E_1AVXV3ayipZgNsBpmFaylBwxdDKPLnJa4WjPo7gI5pDsTUfrHZGNSMa8Ldub4kN9pG4vlk_tfhcZ3SpBY-TO2JqDodrXqQVbk0tE0kKN6P9Yz-OqBWpelRYa7GsdeS8HHzU-hg3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
لیونل مسی برای اولین بار در دوران فوتبالش، مقابل تیم ملی انگلیس قرار خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99765" target="_blank">📅 07:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99764">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-AkJjOpHCfoTqU-E1IQX17md1vISXVjZRKgIJ2r19hQch5QP6Av0QA7LUTcb7Ly9x0oSqhvTgR-k2_HX3Ek5aYch97PLXMirlvIfUwiOG_84YuPX0R2CHpt0yJJyh5Opwx-R9_2WB_iMPdMxuOp5G-j4MxUWX-2zbf9-szejLyKtzL-m2kjglN2AtIzHl5e0QQMfqpInoX0M0ralU17clzQj7YRfShct3Y9a668EqZ7oMHh5QHH1Ny5PcYxUrafH2w_7y8EYSm3OauL_3QVyANXjEcyWxvy7PpOf4Yho-XvJHkB-QNBoL5ZRNVOmqcMV85tvpHhlCwCdU3lo2LMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
سوپرگل تماشایی خولیان آلوارز مقابل سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99764" target="_blank">📅 07:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99763">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRCEZIZ8xRdLPJAQL-9tDtawNPELZwjZj2WrIPEn9USa4nd96Wha1pbW0CQMvyOI-tkoEaoa49_Rf6MBm2r5nf0zF8Hb5cZGdc_bKzcd8hNwtI5J8sI3Tz5xomsdHkmJe9L9g8LjMwtPA43r_0a_gXsIVqNdUdWnW8pre-rtPpmh-Oa0xpYFjqod-SnkNFVBwWQ55olp2ZQ2aVf9lUrzlsuwPIjFlU5hrYf7CrkxsE7opmwNkAXwhBJps-v054hlMCRn9jizdDz5RYYEdyGRxla3yeH87NgzemZg_DUv4CkQZIItQDNH2xhzqSQQ5-yArZSlHfzLsSTHaUZt6a1MwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99763" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99760">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUl3OY-XL5fJHVnjdiDWf1JCk7NIHCkjBBXZuIJw9gu3pDxuJ_ot0HxE1cDPk6FeT9KW7ou_1L1_OhvqHllM93v5YnXPSy4B9bpcdOZMfPF33ZnnSz0HTC5ESdxcbt-k-8-kUrbC_rgp2VY-2u9a_0F__SxidiVxwPVdMAHHwRcdsmBVvT1TOF2E8yHN3aUERDmA2VE5XwGu3cQdQ_Ndm6szE00ked_ZGZDBkUKxZP8fzaMsIeDc5eEo3BDZP2tbcZDShaV4Ja3Pudr4Q3L2XsZP3c4kBsOZvFvePROd1L3kaOq10X4GhOnjrxMvUiqzlNFvUsrlrcWe2lDvh6993A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99760" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99759">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnj7_gPZHxQqRnaTsOaSfcFxp1AjeHnNC5ZU0qisvxz_DUiyCADwCvN3BZD03cfBkCJlcIZC0dZ_B3UFSJ8mmrHDGn2016S-Bmo0Afpy9t1qKMk1BXxfJ4NJSPzG0ETatgQrJmtBPB2dGosWs4lNtWzYVMhm6PSJk7ZbLe0fcYw9q26Chh3YNcRJU4RvjPU17Uit8wsfiI5jEcdGpAk2ILbqktRweNZIuyZezdLeiQBjB3D_aM5MEKzI6efzcfjqWeD-b3QcbLFCrHwRgtLjDg1cih0fgc6O48HXNZOyxnO5hLBVVIVFPD1IAjuCSehiPWh5D76awaBgSa_fRUMQrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔥
🏆
تیم‌ملی آرژانتین با برد مقابل سوئیس حریف انگلستان در نیمه‌نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99759" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99758">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNP87N5N9POE_s1zowhc8GnyMynAcmKvjLHoWatj6CCYVonxcoA7Vxf_Rnf0xc4I_4PPUhd0ud4EPGjRNM1lIbeLuCdjytq2RS0z7rhkIsbiBHvqvym8rjCjoCh2tyLNqsUQTybxfG5QMujQWD5wVRwXno9iMlL3NDlcl-vVV0nvfQHHE1lzqEXGNGBSAtaNOZOL-DMINOF4wr8aIuB6l7RMAiYPbDKjlegccb8ygYjYx91-9QlzW6I_3mjP0MyfIS8mbMIOjXaCp5uO5aqvp9qj93hdAyAwcr2fB8tl4X4AxS1D-9OSrGUgfHGcDQ5_zzCPb0lCxOUBfkUGFBKLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|جام‌جهانی برای کشور آرژانتین به نیمه‌نهایی رسید؛ تقابل با سوئیس هم به ۱۲۰ دقیقه رفت. پسران اسکالونی با نهایت تزلزل مقابل سه‌شیرهای وحشی قرار می‌گیرند
🇦🇷
آرژانتین
😆
-
😃
سوئیس
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99758" target="_blank">📅 07:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99757">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مارتینززززززززز</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99757" target="_blank">📅 07:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99756">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لائوتاروووووووووووو</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99756" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99755">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">و تمامممممممممم</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99755" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99754">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلگلگگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99754" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دقیقه 118</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/99753" target="_blank">📅 07:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99752">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud3b-bIzMlsHQD5Zujw-EDEvK4Yj-zg-ti5uJbb76PSyd5bzdYBjNy8jw_PIDoSZ15q0PP6AYPbqBo8VXkyZ4qDpDhax7l_fyBUrUaTcmQhL7xxhYbbdT7TF8Z5bdaFCPi0u2gsAV9IxVKgj-ZBGPtPrkFldEQrJTvmqB0xt5CS1FFZ8UWUmJBjym9OF0N_4uOrF7Rhkew2lnu5WTYg7YPUkl3tXHMxh7IcMzgAo4jDKJoQ8R-MsMiH0L0H0jDSwb4DrWlY315e4mhcRdnyIJjr_SomRmDnxPrA8xAVA4vU0dR5ngHPFCF0DiRXUA_YG7z_AhjfjdzDVfmObmo1cFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلوارز توپ رو فرستاد جایی که غم نباشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99752" target="_blank">📅 07:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99751">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKQpAOLlOeovLAJ_e0N-gkNySqEWLUldCTSlz2fadl7nVxXdGjCWlsF092MhA95NST84QB-6U3aPsEmOWo6iGpMzMaqTB6IlwSjhI16YPGs9mxtVEpvZu1Yptmzc9Z5udYXZglL9FQA6rO0pSV92O4tOLKCWc0ysm4WK-yQvsRKnobFdhn8RC1STAt8UgJybseNeuinW_FZ8d7BHVlBg5lO1V8DVHmSTOuBiWPc-Qxdkv-YtJaYFn_2V3-GyIMrnh5G314LPIMLsn1KMHMJ4fjgmKOBD63RqdFsD0KSPRdDfbTL6W1NrdfMtV72gibFvG5GRjNBT4oDdzdZYnrzitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب جوی
عجب جنونی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99751" target="_blank">📅 07:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99750">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🔥
سوپرگل تماشایی خولیان آلوارز مقابل سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99750" target="_blank">📅 07:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99749">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آلوارز از اول جام جهانی نزد نزد
چه موقعی زد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99749" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99748">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آلواااااارززززززز</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99748" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99746">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خولیاااااااان</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99746" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99745">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مگه میشه مگه داریم</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99745" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99744">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آرژاااااااانیتنی</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99744" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99743">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگلگاگلگلگلگاگاگاگ دودووووم</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99743" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99742">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پشماممممممم</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99742" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99741">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یا خداااااااا</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99741" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99740">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/99740" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99739">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلگلگاگگلگلگلگاگگاگا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99739" target="_blank">📅 07:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99738">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسکالونی با این تاکتیکت ریدی برادر من</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99738" target="_blank">📅 07:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99737">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نیمه اول وقتای اضافیم تموم شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99737" target="_blank">📅 06:52 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
