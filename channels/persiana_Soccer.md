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
<img src="https://cdn4.telesco.pe/file/jCc3YSp78ZdyqfgEwgwUqx3oysH0qgR4aqjTXuxjv9rC_VvuMzlbkvWOG964vD6lBWkWZ_fEoADPwcj9ke883BDTfjYYHVT9VQWGWUyF6wYfRJ9M9BIHkwVyEkkUCH3O-_4UWsfmgB8_N8132nxEw0llXMc-8fBmvt_NMYcSLUL8rA_1x1UnZC2NLZETScQJ_gC4G9bdLdwW7nB4BR4za8uWd9TSYGCvDGBeTcrW7iCGvdaA4pkdJYQRnPjaY4n66_acKQO69OWRaT5M-MlMJRGL7nbOgoSYU4feJ9lK_3mrMDpIS2EAWCGKOy0Pj1QooCk-aYb5WKHtRnH_FdMMDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 603K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 20:45:13</div>
<hr>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_ku-_dxBuhLq5DvlllfNNeARH_2Ar_-CLfZnL97Cg5GZlRiL_fE7-m-yuVe_q6c6_5lT_9N2yx8x8WfYJCfRI4MF18scL3qu67wLKoRQ_W0cNvbfwsS7cJel7NjdeGKQb9ihTEQCIZxuXByTsaup5gjqfoDyW32DzAaPv1vFiqNlm0HhwFp7FHzrBI_ZCwWFKeozFXAcCSCeJeShGgODFA7jmXUNSILioBD3pCMr6JBPls63JBseMMzSVnI6F4pzm_jf14_EJpjne_7-l3X-CFMwX_S85VgSwXqk9yZZPaJIXdX0oa_MfgpcleydbNh4NHmP2L1oSIaP_QJTYY-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUvVEWFuLH8InWb6Nk7Dg2xLyqqBDz--E3jYsLff1HfDtilUdne6QfG6u2eNe0MvIYnVN0AsCOPDUQuPH_U31Tov8EZCbRRBA4nZ_jwI5d6B1y7y5AV4vST_HDNPatzTR_iya-cOlOEe1Y4tORUZKTLuZ1wDff8ck7cQu7QVY4A3jehfCVw0BjmUsQZaMCWImyXaLEQK_vCLdQqX9cQ0M9Va-jjKxENYws5day0rtGEAFzrtXsckq2FxaocMJG6ln52_qoEFiL-CIHTPxpjxItmVi8fiLjgh1WE9KyHlfeYWK6KQ3-Va7VBtU3w0hGS9FGopSPI9rlltqzmyrZUGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae0WFtqXEQH8ATlgGVZTyYg8kRXyVg5paG46yY98OBTM_EHUq8RILux8Ax5YlEqKzAREJjMeOYeUgjt4JL0A8FaTL462X3DxGSksW9TZvvJQlwdbkLyV1gvld7TLVqM699tSWDhXqcVXqty95LN4id0wfbaNknecUBqutuC92IvCpWq5IeGENJjR5-fG9vSijPhkrqA9bAe7KDyDvrJ4ECwfHYFD7mqp6zS7vK49eBav7jJ28AH54WK0fgGEsS5zIuTZqeCIgIVUnh2oXg2DT9Nl8cGXCgBFq8VT-YW_a137x5FxQDCk4bluc3SxLw1SvpTy61QN_PArXO_TsGXiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqNNqJ-WfZt15tf3MARfJENv6BbL7ToEJ-0b37mMfJBDjH4bnOf2gYa2v6mOZSevLf4M583BbdyGd2OMDRWETnh3AApbMX21txyUGVnRDR4E_TR8lO_nbqlb8UlEGYWpovF77s-QKLmDItgPKsG-gIaS1t_BNwTmXpuZLniZVN7p_SanQEmrh0QERglaWtsntvA5zQZH2KHZMUn42n0OQiz-Ny9L6MmLNF1Xa7IScHd5SiJtOQYj4iysrsTER6_CTGH9-UBWXb6FmZssVT32SDwsnO0yWvLC5W8HxqJNQA2fKPmvm9d1nVAvTVm-dny8o5-qVMxWHKz6IGp7S-4aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2xnGxvkg2RWH4DocOJQ2TgifWu9ZTGlwfMPKX0MLVx6vQEYgP69OheG01D0Dd_0sDRNLY5qPIZ8gC_oIS7Z50SIT0Cs6k-P6cav9QsDtGFZ5SZ4YvEfF4L30yn37EhbgOeSlmaOl6_nlmwVLUrK_0IhCR4KnK24AC0F7Dwss4Tmp_BX7sf8Yrg3me1XSpLetb6zIzeX_srO0NaaHaITEleCKZXHBjx-LFBr-invMlxcoaEq_lYB1O1hDjwWIGRaBW5jjtUp_976JBwB47tpwyPuVZQKCgkMsIW1aXef983ApEuY_VxqWGmjrjKhCzhhlxEBtxuc7ome1zsLbV9Xog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHpDm9Vh3l7igt7JojxSRt1jGy_GiyotKYxuoxmljyEpsvDHyqosun_fDlJ2OzkEqEndEHVFcWcoxgMbuE7ZzM-oCRYV12LcFuq8DtlQRy6kDSyJqieVlUKRUOPpPwODu6gbnDPBxlqC4bQjwsNDqOYjGyALxBM43u0OKbYd9yOQW4ZTj8SEHJr6AFqGWiEUwniZpdYxQns_yOIkUuZVz2gUyoOQ7YlwwlCWuie1H0MM2m2Ozad6E3hROtY0uXRsVjkUNQZ6LgwTEFSLBc63yHEPumS7hkZEKhF1mW2vIZaii_nQpS3V3f8EPS5H8cj7n45TGpWp0J2wBAXKU-GPIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc8CAtxEjgo1r2AVbxYEAfLgTPe9EMnl87sBBbFck7YhS0YI67j2bFqjhayrWvsdGrcMAsWiLYc9plw3G4L-cO2lXvk0aX_DckHEs1mKHC4ZzgM3aMKvlsIJYYdPg2LvatvOp720filq50knsRcoCS9p5wSTNjUJhtFTJnGDEVmeY7OTehQGDNoFEEutH0I3osjI-_gtwpaXps6qLoW63w76o_ISwuT2CIcTbi7QEUk4CCoaVv1LE5QLlog8AeyAz2d_8s5AG_qgVUeORi0hInXAInheVYBef5W4OEKGM4MiE4TTpeVmOA2sYZOMksLukaQi77f3Vx9Vvz9obulV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBQS1zVIj1VWgHvShiywc1gnpg-mvBDsF0pmSNneq1z3vNHOaQ6e90sORi90xWQRw1CGjYpLhsA2JYM9PNI67ZcOYApee5aR0wc4lKVQYC73gYIuex7fm2SM2W4Ey2KAxl7LfWD7FMWM3-mZhEitTrpuwbwALdkEIu5siLnjSvo8lfgKDqLEV_3GB4h86i3EeGt2JMixryIJq1V_8Z83FRQv93s_lfMABNAN-36cZ2yjk3G4cWoLgTMprtXEOhTio_UCvo-EtT8tlmL7G1cghFKgHUFAR0n1uxrbwiyplXLA_G8xg20n12MfBK9khi6vG0E0v_GSRSX5pAXfJ5FRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=ZF8BxrZo2qEdU1cKGq_e0KKpL6X7G8-Qk72OjfHw_rA7LsDAxnwSTlWQi68PEpy_ihfISlyyawlITK4sj9IvZ1axIa29RWeFE397_RVlsTKHT70x-MV_DDxi0krcbweMvhiFjPgK2GPoTWF_AENno1FTWGklpdHDL3aaBLLYVDvzcks5hILolf_kLx8TIsM4DzQfPF0piztcx9PceOKZbcfv1mEGt6I40o5VNyEaUf7Y8uPEg_Am3734Koaw4czcglzAWnsXcyQFjNPk-FRBFXka9h2vY7OnMYyIiGJtSK2FWvHX8p-ASTSw_797ugwo1VgH6vwpp9ce9O4u0dX3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=ZF8BxrZo2qEdU1cKGq_e0KKpL6X7G8-Qk72OjfHw_rA7LsDAxnwSTlWQi68PEpy_ihfISlyyawlITK4sj9IvZ1axIa29RWeFE397_RVlsTKHT70x-MV_DDxi0krcbweMvhiFjPgK2GPoTWF_AENno1FTWGklpdHDL3aaBLLYVDvzcks5hILolf_kLx8TIsM4DzQfPF0piztcx9PceOKZbcfv1mEGt6I40o5VNyEaUf7Y8uPEg_Am3734Koaw4czcglzAWnsXcyQFjNPk-FRBFXka9h2vY7OnMYyIiGJtSK2FWvHX8p-ASTSw_797ugwo1VgH6vwpp9ce9O4u0dX3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=toH9Bi8IN8zciw8Ru-kxLEfPKBB_V6EDi-PyXIhkG0MFhoQwt70aeUZTwimh7vpKtYr3KvAhgoqzMqRvcxAhOWMEE9GrM4s-GUaIgEmwD8kFwdN__9TIVYbcrvYSaU6K0XW90wtw8LrWB5Qa8O4Cdre7qgFqal74jdyrnLNoyLqHoEV5iHIFTLyMjvud4Bx9K-ZezGcqSXgTli9FEXuG3vPZpbX8HcpXlkpoZpNXk1jGnronxVIhxMHGeR2NMW7GCZ0_wXSZCZIsSs1SbM2som4NSGpJpCpo0Eac_d9XBi_J57js-fI7TTXGe9QHtdFc-7CG46CbXso50xNB6gRTX47G9pWWNXqL6TakbVXHx-eG0-_4dDozziqbiO-FqjwAQS-8BeReeFr2ESa_gpADlw7nBLUVbwPP_IaFBhq2ctVVmFsc0xeKAllPkjprJ0aKKiw_zcj88iUQVVARvPZk6jPa7LRiLfV6YXCqFbxDOFNYfIC5xqk9qmF2gEAM6FDy2rMDWIBgS1Km2b6BBbquByECbmu7RfxvxrLzJtsfbX0K-DetB0UBECgox01jpXquBj3Kc13I8qnNbkgMzvx-RB1iE4gtt3IA8TYFiRg1kuQtPFdB5udRXpOq5Fhdc8m2bII7kgAdJcMSpz9DVXwA8ms3YvYMM71e5KpjqAVGSHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=toH9Bi8IN8zciw8Ru-kxLEfPKBB_V6EDi-PyXIhkG0MFhoQwt70aeUZTwimh7vpKtYr3KvAhgoqzMqRvcxAhOWMEE9GrM4s-GUaIgEmwD8kFwdN__9TIVYbcrvYSaU6K0XW90wtw8LrWB5Qa8O4Cdre7qgFqal74jdyrnLNoyLqHoEV5iHIFTLyMjvud4Bx9K-ZezGcqSXgTli9FEXuG3vPZpbX8HcpXlkpoZpNXk1jGnronxVIhxMHGeR2NMW7GCZ0_wXSZCZIsSs1SbM2som4NSGpJpCpo0Eac_d9XBi_J57js-fI7TTXGe9QHtdFc-7CG46CbXso50xNB6gRTX47G9pWWNXqL6TakbVXHx-eG0-_4dDozziqbiO-FqjwAQS-8BeReeFr2ESa_gpADlw7nBLUVbwPP_IaFBhq2ctVVmFsc0xeKAllPkjprJ0aKKiw_zcj88iUQVVARvPZk6jPa7LRiLfV6YXCqFbxDOFNYfIC5xqk9qmF2gEAM6FDy2rMDWIBgS1Km2b6BBbquByECbmu7RfxvxrLzJtsfbX0K-DetB0UBECgox01jpXquBj3Kc13I8qnNbkgMzvx-RB1iE4gtt3IA8TYFiRg1kuQtPFdB5udRXpOq5Fhdc8m2bII7kgAdJcMSpz9DVXwA8ms3YvYMM71e5KpjqAVGSHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26625">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF4IFcE0RDf5RVkJtVqrXVLV_vAkeZGJhd0GqtR90uqERC-2IjX_Av2ae7DNQBPp4vAgr8DRN5gHXELHvZf3KPcShZbKupQKc3y3tum7dbTcROLc8eKh90MmiFgSiJXiWoxqaRNb4eV0F2XkQtqXpj8PuooVx-1STJW4B0do6VEGvIORP-0Igcm6z-xoSFMh06pBfJF7G43sJ2xUdPvGXhDKIvt20GNRpcVfQIVyftEii7_wDQyUaLDegqVuCCNjYnu1F212TbGGjj4p3L77_M7YbqfvXLIUz_mx3_6z5mml5S4naK3ORcqE9KZKgf-6mssr1uK-b6baWvJiXyYSrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/26625" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWy_O59b_3K9xV7109V9nRTheDXV9d5KeH02TKceh_B4BnCpom5TUtHxPxAqy0YnSqD2wnmwOXTGIOLf9KDFAnU71MMk06yJcBsa4IiH1_RRi8RNlbtWmIGBWNUAW_nK5VQfsL9QbMOF2iqBgc-08_vayzme-k_sMWAkAOiCXb7AcV-0qVVf5C_HjGKElDTOMU9V_Gb0kE7COLB3bltpfR6vnc8ud0KdhjJ7G1x-befsfiTbJfB5pQTvjFzAI9UI4OZEoPVRLMR4rttMFg9srShB_OCOrPMf9HE4zwNzBcas1kWwQABV3390fU-7c2EDT7e3quUzqaAkiQcCev5Jow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRktDD5v9578o5e4KqpvG1zqb0WESRzLEkRO1z7gjaFrjiYMftqDONLhKwSLYvJepNTqNRSDP2x0iVYwB86_-P90lt3Ksj_p3qUABkAC0qOoFrVK8gtFY9LBN1LbdHgffPFcs4udCpDIWtm7e5XUEQ0K7f4Hum3VF1jH2BoBAkmDIUFrMgG7JCiYBFRbUA-2iHPMgx6Goe8qWxllL5SLxufSlf7NDLizaZfUxxwO50uO2Gep8KJ49QjnfGd7WbHH8JZLd0K3jLLLroAqG1IE14zKlpgQEYX9zwJSVqoWVtpVtbzXGnon-Jqj60RyrE5-T9rR3lPROp3wF0Sk3u5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag9Zo2borfYRA5NtMqaRY9rWREmp4xKuuF8hcEOdPrsB5Y_6aIr80R1n8jrvRFdWoyUKMfvmF43edJpk0JThM2SdbUtgiAyPiKY93ZgSbTUQBiuDpKbzIPshtCDRA4kPwMEGmJmHr2VUugEM7qpp1fdbxMOrwhy7Zykcx-lSeaHd0SKoUuhOLecgF_CCTNThylW3n8Ycos95saHy2JAlGz9syCAOHlyTsVlCC__Bes77Ea8xVVMqyEoKVrtqI5H5Z3izD2jI5j55wKPsLt9XxiqpVQCtFX1XZ_IinG2uQ9bFu6sK2ZJbnqVQbGuxcLrYVaEiyZjk_m4ZReWImThoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAPTjzae1IcCUl3Nj17IXKk25bvtUCb4w9MgUlleUSfk4Rin6cq_d7gR_yXKXHgWythCPL8xWaSbV9nSbnrIusQ2a05_0Rq0rJ4zXCcCd9gg1w03Vzwu93-W4Ehim1yg6AxCKqiDCpFnLpVZMvlGMwHzvvXh3v9Vx5O2CBCLjz16QobdcXLKjxcaQSI2QLTz_H_wS87qtBhphULIxtR6Ha8KuD3jDjLYHfuI6wYlqZ-fKTXoCYdGophxXJSkvww1YIdNBFrdM8_QJvbfjk_HbubaduTyCs_zNJZrbTF6kwmaDQ1k5Cs-ufvAUYjDDRS5bX3EajiakJhfO7EVifQNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=BgZS6jp4js50OrhJCXA5EfT4adUqi6LyhGbErTm_raRMZeJmdTBZRZ3GZGb7dheG0fGsUNeOTIEuG2QPsPVXFDVM87rqU5tDxzpwlLWJMbZW3oa71XqHtGaEZ1io_ZjTb5eyGPO4Skp0vUQRIOYjiq8vUoCgDjXd1vls4UyGx_NP-G8zA_P0NavF71xmzIKW9yrhZ_RlePuqTxI45YNJKx30QCCDedrfx_fd-KYFNeCz5RiTNG5E0rvYCcErvwcZkg7KDp3TifJbzsK599-_g4U0MGV09gypKQOnjszPN5xDe_gS4swdWb4RV8yZz7nTfkfWcytyZ7kvN0OFko69WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=BgZS6jp4js50OrhJCXA5EfT4adUqi6LyhGbErTm_raRMZeJmdTBZRZ3GZGb7dheG0fGsUNeOTIEuG2QPsPVXFDVM87rqU5tDxzpwlLWJMbZW3oa71XqHtGaEZ1io_ZjTb5eyGPO4Skp0vUQRIOYjiq8vUoCgDjXd1vls4UyGx_NP-G8zA_P0NavF71xmzIKW9yrhZ_RlePuqTxI45YNJKx30QCCDedrfx_fd-KYFNeCz5RiTNG5E0rvYCcErvwcZkg7KDp3TifJbzsK599-_g4U0MGV09gypKQOnjszPN5xDe_gS4swdWb4RV8yZz7nTfkfWcytyZ7kvN0OFko69WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1o0hkAGDlKcjGAjm4TJQcHCS9hR92cbuCECoJOJf1t7vhO8DnCh2Jm1CJap7ZLihllT3Jqdz_8kKtD-jcOo4my1pCjeUASuV7KpFALFnOE0h3f3n5BvecH6haxmv21yZtiI0qpaz8NIW2S0PXWgn6GEwkvepLobI2K-Su--upDXZalSn8OWSO2c4NlMLh2WKWRpwULNT7aZtZcnrhg1gjYG0wGq7DZZX86hKxDTDLEbfImZB5JfTOx9KIHnwaoXGy5eVu4hkF0lknYl8-2I5AQdYDqMx5BDSCMVcLOhdJP167qM35MJFS6liSET2PMrU0feRDBMXhk-ld_dvS6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HevWY4EdI9t1ofsfo5QwqlGIKpVyMQ4jZAKpcy7z1ZyV96jqo9bMPYl4SF1vPp3ca0KUSRYrXnxaWvNUvRAEHY46UYeqYpcr66FGPQ7NreeIlzEC8IQ97ZoREafENzoUQ97DKmbGCWVFN35fb9CsyVEEvSW3jjDHMW9NeC6-CI1IMDsGAXFn6GjVBBPZlXpnLCF54G4vBBfu2Z4CwVl-fAhN60eHuNeE-z7jc5Ztx1WzHMTrR75Y8CP7zTIzvaeA7gGVF_qtCfNqXhNBhh4_f98bmwD1WkNbYhTAjqDjVmKVgH_TeOO4URwUCtAFWN-L5mocBV9k03LG2TNvYQTlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6KoovFOQEwCzSzAtGqxkUhlvPADPxmeQ9Wa7tWo-Hi4arAJJr9nuwsC4z9kwTY7_Hy1w2uyD9UtJMnoaNPaNK6DWOT3pIQbsMbAjDOQLJMTo7r5-TevWZjHFqI-fDzoZ-P5r6YeiiXe3x_ofVULOCo4_l0a8AQvwyd9r44PC0170xU7m1TzR_0YIPC2-vgp3pCtWpPMWSDv6CL6KLO_mMgTNjMRJy6FdNATVQyyQ9A5jhRn3q4bEjC_Dj5m7y3iSmIqnIxlJlhFa6l8ftHZrq3oY5e9uhsUQRMcjHE_MzBonw82TMx0vtIm9hUm_5jPJZeuvPaxOWi0iUzQZFGfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m47grzWkPYPft66UbBbhMSNMu5BLZ-z25hGx12uk-9P5h6BIjb32GeU7btvBwkVG8lArgKPjlt2tYFAtkUbFF82Nt9a2yylzN43hyl4Zm5f50boy-1wFLY29KVia1G_zWjSW4aDDuGrnOYxaj14D6cUhFo_AkIzbxDY1r2c4942uQJgNKoZfW6p64whlrYB3HYZFIz3y-R1gzqbkaeXHS6WRdGi9LIORVEF83Pe07O57JnuoGZ_FTXVdJkPXdgvkmh0qVJ21ggd1WSobJggBxZP0kR7II1sxu3enGKvxcuKlRYj2sdTENINwR2u3L-2CA_JzTPw-Qxi3Hn0O28aEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3C65bpnQDvO2-8yghxpTZiAJLu2-JFtuWIncY4a3B87lJUl4c5ZUbiqnpOq35XpSy37Lz9Pr_Bh-3VnOD93DEBPzGMbevNDqdu0caUaQKpfRanzaXHQ0sqh-xaN7tn9cUzvjNjYTQy1tplEn-2wt0o_4X0wWB9YZmeQV9j1B_ibdft97IVuZUhsxT-BtdowNlp0--9ctfO2Yv8Tsc0u7WjKoTaUaLtqMxD7e4fORtPkGelBA2P5Z-wfKQnDYlcCqCCcja9i-7OehE2nuzFCahrYMxymRLN2zvWU0sUGzGFokBM9ALyJEA412tR7rHFYsDw3xkw8vkxy2aD2dWgzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6C032dX3A0m8V2t0N0P5ar5YJwkR8pjwYMXH3TADPq_KmuDWKYwWZbEwJK3zhSPGdahwJyTMMAQd5aNFgVfzcj9Ylo9HnvwnEWwdVaUSNap2JHE-UfkSIJGeHZXr-JhYsLLWc-0n6EvJCtovFnFvCWeUap78RWfZy18qChEnACEZjn8Ddi8YucRutN-E_HkJT-hs2oieGV2tZW0PocFqpQ8UTxpByaMJxyj3LRMpk4T79Si32aZmuRlpdLzP8jkm2i7rOff-A4lPQdGUrd45ojN2wYkyZiQPL3ryrmVHrP5HNNKOQo2we3IHazlaug2nQbLPY1Aa79lTkbHuHwTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr5EDdSDYeyp5EC80AZoqMCsmjVwNcgPvkt6QH4tKi7By1FSpTsE9PyfDUOPQKWZbX0hyXewYhYD57W5Y4rXPyEjTULY3uKg-gc2PkXijHjTq8GWMxEqfEvjYHMggxP1QDSBY3K0rn9U9Yo5jDm4NxUZGMl0-JCaX0soN5hYE0FZiZ64MB9vA6LajzFedplyJbdGmHfTbv-J0Qt0PW5EzoCcH9RuknE7D04q8eq7_X0MeD_3ukShVVE7JNW6zzSQvS84hIk8Nbjn5POEm1JeTP_ElpsLanKFmW0tJubh6uJGMdTTnQlFF5O9XGdCJOp0ZQSac0Lx730oJtUm4F_-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7ORqeEggHrIJXkj-0TWGRl23g_CKcjx2nXuFHA0v_4e01Q3racpbrxaEEkjhOuG-sOUk9VzbmvEXPWvVall66JRKZc8Zzx_bqRxMlfSOudZZp3mIqHK1e5bgG9RLuaR67LQ47n7vPIUeA12MYmdYZhMdJruB6xjscaoGd2N02KkyBVGmXyFwXrsymnJupJwm9zMLI02_LaII_j-fF-0EF3GdX8ucrD49wXdENZ5aTXNvYYxWEtaqnx5hbncKtOQmx_G2ptEpXJrFF5TrO8NkwbhSgpcCiKZefhqyUl9PznojkmN8R0hiJPc0syrqZg-j7TB8miz0mDm3OC_p9VfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcJWwgR8EJolmuAlDRWREtAk3BK_mRhyUTzMTgFdkThE9_gKngU43qBHMKrj-0zyjyWd6ftCLlJX3aHWIVHf5-DbVAC4YzZThgDpu2yQI_psHXQjlRd6CmpwEC8HFfZvvuCmCqCskBGFniyUvTTtjpAcugJPyZXpR9X9azl7wzuAa8s0qdtA7voy-ch7huM-Oalwi7KoNgmB60rp9rmu1pGik4N6bK_PiyK5TPYIQF3CkxnfNf9D5ExrYgeL8icWF_rxhbeagDchPrnQw5l44iLvTjQnY6vXFHenPVRyqao0ca8Ug9jXx4O-ORdoIUjuOtB-Nk9kB7rHhYJc-grItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=k6KpkebIVSnwAeeQdgwaUZCoki6GSJ1a-KZbaSUJfhcwOr1vv1mYBo6eH8WTP_EQLRPAZVbcvYOWZwBix10lVpWwnP1fCtUeKxmg7xsvY2-4W26HqyT2Dc2yIffHnecAZm05h2-1zfzV3eW8JQ3n2Af-HSJlebmWuH_zb6lyG2u0dO6qqy2fBait2k28F7X2-jeLoK-3ZBzvfxJoUOXm0fLXQSIrI82d8omyMyaiOwyV5hMJ79Ns6zTdx1LEWCK02Tetfz3yYUohBxWje0rtfIYXMRe7oxHozdR9N9FI-U5s1TDMn0mP-RFAUpvNerzvlit7bpy3fkY9jW5o2Brr4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=k6KpkebIVSnwAeeQdgwaUZCoki6GSJ1a-KZbaSUJfhcwOr1vv1mYBo6eH8WTP_EQLRPAZVbcvYOWZwBix10lVpWwnP1fCtUeKxmg7xsvY2-4W26HqyT2Dc2yIffHnecAZm05h2-1zfzV3eW8JQ3n2Af-HSJlebmWuH_zb6lyG2u0dO6qqy2fBait2k28F7X2-jeLoK-3ZBzvfxJoUOXm0fLXQSIrI82d8omyMyaiOwyV5hMJ79Ns6zTdx1LEWCK02Tetfz3yYUohBxWje0rtfIYXMRe7oxHozdR9N9FI-U5s1TDMn0mP-RFAUpvNerzvlit7bpy3fkY9jW5o2Brr4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esrgE2-IfiZhg-XvHPQbyBqfbQwRVrffh6PgP2k1eOekn6D770b8jtRzxZW_VUZsxMHuhEMCw3lxq3PNQXlonDYyesfzeAdJhk-rjyTTmC7le5adBDqubVRfDU35f90SRX6cBGEOY2WWb6boWlao3LhN009AXh-XfmB4PbhcwdnCDEasUQSEPA2szCLcgJxgnIjVN2NLKOT3vNfbPXLHz0gUmB_XzhwIMao7BOGy9jjd5gf7nO51PBH_gEEDoR9nVgEsEt4nC6wa-PS6pvvbFhDpvTpkGQHAdCst4Q5XW26wtuPs0WadTjpqBb8L1ij4LdCbLDjVsbHkYijJv2OOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwkTNWfCjXt2ccv_AAkJUhF963HyogEzS-Gh6aKoPtc8b9S_19SoBa7xgYGFFItBk5qXMzGbMH3xJnZhB73VV4Q4s6qoRwijYqtt-HRy91W-023jliBCu7XS1bVcUedWexKYeqQRZ9RZKz8r1emLX-7fbQi7gfV0_SUC7Ad_JKDfhqVnXOcZ8Q00qcpNbI-k7vvw5B4J6t1jjlCDpH3eFp_Kh-U5dUcbhfALsIXO-YGGCFOhbnZlfvFou2N1_TTuUnGqd6KGD1IxVrmVet-YTNrmiBFH4QzkKaqu_VGv5GuiQ-oWF0M1RoASRcyljtYfRM47w6PTp2TPL9qalO_03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmG6wYVxSR2htEfFgNP8cxVYLAcAaj4yu-JuG0qrQe4xdTAhzPMgGh7MNCyFGRM9A4NR8pJeuVKKTKV2RTksdX9vcY6JJKcen6g-XKwCCO5e-G97pSfRye_c_NBgDBv2-E_Bw4pccOBuvo5v-mbEwID6UGcMe0t6--PjyhYSIonhQbk_TZftVKVHpDPEj5ySlmywj2-BqHKYy_L1dJ02a-awNEpvRAWe1wy71EyxUcBo2GbWgVA20eVxub4Re33MazgFTql4q374IEANa149TMKcykwgLMufk9mECoonhdfoJ6bdNCpV0Kxh3l88F3RIXJd9ehSRP-SnYXIZRz_9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4u3hrE-OMlRXPWZSYScVWsgO07VkLeZ6UpKUau2NVDZIXNKo8Jtvij8kjmciRnj0UWwSzSGORgxaKT6e2s8bV2rhX_tr_FtvgvOEXyJA0ZIIwF9P8eIc94LdCxyglIOpftjrz2Um9srG0a87Hppc2Sr2inYFf-ftwOwFTRpegVcZRqIQOe-CBC6pUSVe2kdQJkUG-Mw2AFLLd5hv5oyBuW_IDLsXDNxVCWcKnNWdgri3DcUTOaSI6SRRuAluCJoRanshxAjU6Il1qYSAq8kNpa-IwLGD3TEk6yHd4kowW1a9aSpKBXOl3gORO8SqQsWmmS6mXt9xu4ajVzSN5ULvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op0_QB1M1MW-jYAnNwRtWFdZ3NrVU8vtd8-Hv4Yx2utANCNjlS8_bNVwcL_5cSpItwPYMsCwUAwpbLFPekN1zRWciQbz2IEwYK2sVO71Vz5IFurcN14njASgGipfqNOmRGLkbUYK06jT2JA-3B7WQh1OVQM21uNFXtIpc9WxItkCz67Hp-S5HdkjVeq-6M9Hl7Qb6oMkmi9bOhjapIcQyKG9JZ4TSRPzns_REIG6LaFoP_BfYyd7nhJ1I7S-mVmyFoBKNOnn85DnCNZPmXKaMOPQghwPvsfkXogtNokjJSnCecTAq7r9_4Qj6Eaov8IeRd_V7o0gIti9AQwvqz7UnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=AWR_JtvEP6iJiQwlGjxapojcyjVSUGQYK2CssDkQx72pLMIjC79GAEk-I1jKqItawZfJhe0JyMmNOiexP6Ww_By4oGrKVAHk23JcdvT9ezpRt2XLprvUw2IwmDDgRjRLxnaA0qKWcIvLynTB47zcFw3oTiVhLHdqDcfl8HoZeQgdsi0vSQZjopoSc0yc540i3azeViCO2IH-vmecxvJFN4xnOJ7ltq18WImRPgESIaPXzair3K6dgwStgVhUAEQSZQ8pJcVrldtlUtzwFBgMSJhoA8ZvDy96pzq7Ilbrj-lsmpHseQVLv-QOo_y7HUUnHYmoYurrXn5vXpUOFGTa3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=AWR_JtvEP6iJiQwlGjxapojcyjVSUGQYK2CssDkQx72pLMIjC79GAEk-I1jKqItawZfJhe0JyMmNOiexP6Ww_By4oGrKVAHk23JcdvT9ezpRt2XLprvUw2IwmDDgRjRLxnaA0qKWcIvLynTB47zcFw3oTiVhLHdqDcfl8HoZeQgdsi0vSQZjopoSc0yc540i3azeViCO2IH-vmecxvJFN4xnOJ7ltq18WImRPgESIaPXzair3K6dgwStgVhUAEQSZQ8pJcVrldtlUtzwFBgMSJhoA8ZvDy96pzq7Ilbrj-lsmpHseQVLv-QOo_y7HUUnHYmoYurrXn5vXpUOFGTa3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhL7amLJ1lvI_1mzGBDcvHwVF-L_CigGowdnKXA2iB8k7-yj8NK8OB5bgsS7gjfFvZy1eTSXg1l0blAw7k1zftrQd47_QzB4t_DoyCL-snH5APMxFxdBoaF_zr0kZnMwYO7W2hHnQyijlEqQkVEe4xaYBS9a6H6i58x7lZRvgKhOQ23J1K9r3PU_IK3wny8aJMpkohlHg0QJsLBiDlELwH2pBGqHgvx3qQT3XrSL_ZYgXPY9EVtuEASKpKzGvkIhjbXkKSRc2-qGk_EPxvk5e4YctDfkRXpZK3iLixqzoXrAx5367j_mzAerNj8NdKJWR3dQijGybrYc9PDXsJG16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfWbxd5Jpjy4cXY3Jl5rEc8siEmeYnwGLWL4GdbophzwNVtCKUybhhGv963IhhtiE5oTWm8Jmt6aMAu_xxGsjQH9dx6JTAEel4sLgJWKjn9tKprL1mAHyvS0Fy-YWkfgj6AYHChAg8XV-6ADaBeOa4Dg9ddNVa9I2wLY2MA8hje-4GBjiZPM58oT24KxQ8EOXXm-cm7aHTOD-XdEBeO58ns3DoJjw7_D5QdsxU9KteRHC_5TeVSsFWc2Mmn-Z9SmKDZc3nyAdtY_6Ydqv3EFhVPPSy_fv2qoM1xd9B2N-7XPje6vfGfnCSqtDjoQpabFrpfauU6Eppmet-aVooh9nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1jfor7dh7YiENEq4GfCZbtvIjv8EHFH8EWCX57uWHDigRD7pJBHiY2guy7EvO95cY5HqAp4mm5btL1Z-cyOrSDN52jQK_8m3Gao_P2K7w_eK2YJEZjaC00ITOcGbW2wXFoydVx3vfyQgsuj8XclO9GCFzsylmuagZelBWBp8liFOErz_Kxt3rkeqcnC2I7cnkrtUjdYGMjrxRVk3UG_0TkJaAnF3d7tStApQWtHAiEhWxqTti3U1e2gcQwaUXJUJU0I2CiNLapzNIwsn4D4CpWZQfUHkAD1YUOibyA9Wuhn8cctnmqDCtiD2rJnCmOix7d_ITt9Y7J6m16dUvZkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLJq2QsWI-7ASYu3QAifBVtfc_W6gc1ArF4C6trmOtYIGjSvxmBqBE0sUFGmqPfJXT9RJZaFX2WsoYoQmN0zPrHvQnwcssGSnBPYYhGcp_4526uUt3WxYWXac1KjQNXZxzEn6ifBksc5wN4Ky7OtExEo7uhhVZ-AfcjCLomnz8q1hJ76Pv8DY1bRnoSojqtrfk7h2G5ZekoU8oZzdT5bbyFo-TO6mdq10GFyQBbba2kQaZka_NGIbRU5lwuupihCa5eIYf_oS2Om-6M3qA4YyeY37T8rtoVP_GHhUNqpw5dIykugeh3BU6JT-j_NmmHCkBhA7S8SyB7KLk9hAHjrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26598">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLXHisLts73Dc6cMQnrOpMqb6yUQ1Y16A8NHWfmx3b6g4kziikAlE8mzYNTtck721SGuZjFndLb3GWemhD9OTiEWpILJ2WtT2YYMdNWamc91cq-wFmY_7YYVJZ426kf2cfs5-XI1F3NcbtIJF9wF5SZ7caYCf72LCn2K_4TK2phh24tGNAvkgJsYOmIZeaBkG0feFafYysK_cZ0fu4Np_cCl9chMcDJwL-zjaGgZNp10u6MwCjAkjj9Hb4niwioeEfUNUPUz2z0hwuyZEuELHGt-j0LQblgSWDGb_6BRQK9qzjJTAt7SPJXee_-0fGmkINaq06RytG6_rC2CvuVzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26598" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE4c4mrzs_9Z2tUD32ogxI5Oe_F9sRVks_63tYzjXparFi531hBA7f_EelRyRBpD-G3CWNdTJ_Kko5NgLOBaOoMgneiL5wRQt2l_fqwDXZ8lRZF6hAPcOLDgBRRQSQNRUOhS2xmL8B7pJ_y4jHsI2tw_7Du3TiRPgF_JgXU5bZqt6ICmfNFJHvqJp4iaEMMy0aeVjdgEhhSyy0-yJb7Dy-w6feeR8D5TYY_AgRRqJ2OuQQvCr2fjtGNI3S_tZkKOx9oYuLyK7mhx6HcxfkWOTQ__35z4gHZnuhoyp5-kF9xCEPlHtNBTRLjbVV1GJ75j-mpauBiu2aL1PqylGE_rYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=WH2Y8TC87HDJ1B3-Z2jxLbwGG_eRuqPc07AlIVNtAQXliYfBzweYVm2AUXUzMfi0tecMvIiamSjwrrrjU7Rl8vTVqqi2gAIEpw589ukyQBc6jETRIFTWveLDlPrjMnm8p61pODxEjvfhItlgPM8q7QSBzoNaD93CmfuvnIwb8jaQK_5_aFrpCDszS1xqwik_XPKdta4sVG1elTjfTFPlQdzJSPhawIr-aPyZUMc2c2_Ih1vl4nKC_7fAsb9TS0V6-wv-TB3F9bZhp3BSGvzU_pQCCkUke557t1UQCIBDWRm9RJ9KKYr8L6wgvbrsMDbgQzdpHIvA3ssolSeCrFwzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=WH2Y8TC87HDJ1B3-Z2jxLbwGG_eRuqPc07AlIVNtAQXliYfBzweYVm2AUXUzMfi0tecMvIiamSjwrrrjU7Rl8vTVqqi2gAIEpw589ukyQBc6jETRIFTWveLDlPrjMnm8p61pODxEjvfhItlgPM8q7QSBzoNaD93CmfuvnIwb8jaQK_5_aFrpCDszS1xqwik_XPKdta4sVG1elTjfTFPlQdzJSPhawIr-aPyZUMc2c2_Ih1vl4nKC_7fAsb9TS0V6-wv-TB3F9bZhp3BSGvzU_pQCCkUke557t1UQCIBDWRm9RJ9KKYr8L6wgvbrsMDbgQzdpHIvA3ssolSeCrFwzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpUlVK1JRkThEzdcLmr0fZVBxaxria-bNQPo8Pp9ekwYWvrlfTRWj5FyObImCcXOxSsGFFzbjib4knerWEdzpByRzhLnpljVfWvw8bTkiP6v0D2Trg0ReChfdbMxzkexsRtW5TaytH6D1DBxXzRTdDeZwP9ijCVi-EjSmvsza9BDPR3leChiPNKLgih2mQB2JXq4uTyLA4xVECkwxfW7xB5TlD7oTMUXgntW2VJGsM8wKrOr2cBurL1dNPvr_5SJMRJyMPTDyywq_vDf7ZKZBh4dhKKlOamu1_kqHeXONk4JpsJTBLmjRMhkE59uKVfwUZ9BaD7a4RJ8PF3zDja8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnioDMJ0BKwRhcy1BcPpXcL36xk-CLtlaB9ASFN0PwFYLNoIm36UUfzEwUaSPEy3S-awUITpqPkRhoY_p_0MulUzV-X6bHYziAVNpvlcjLd6OAlSK3MyUH_4v_OGRp_owGKkxN7fxb1k8UR3EYkpcJQ7T_CnjneeCSyZgq9S_f3VfxKCEZl0rQoypftiKiTBjXMQ-sSvz8cV7GkJo-243qZesP9CehYRzdwBnxB6OGhyQgIEluOG5J3WhJ3Q7ym2jehKcNPRBZLWUejVMjfLAfyRiYG6oMtIj8NUmJCd2CKNqkNpq-MVVmjFuozC5SOx27k_mMc5LwhRJ1lAaP0PpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFIr-_G1HKjyHabJnlc4DKmVb06eTyXGsb6RTH0roASYCxH_SI1fbwWAyMyDd5qKg4iMtu0_urEKcDTt8TCqewOuD1_3KfOsv-KmoP_kOXiNMwCAs7XIfoS3f3qJ3Pgz4ZOl_jTS-lmA12b523qHYcYNHSnoaMgeijF3hVKGVaBzO6MwjpbjEybn2F-ttwP99PivuRF7-ype91qU35lEDux7UjC6cvYXu684Wa3_rlfpq42LYPDHselWA8Sod-ydjfBYAKVyt_bMMGvrjaHnLkWXOPm_SroBmKKApo8CIgWCGSa075CiQlG-ihiK3rZXYqbO1i9-CoDDjMT0CICx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1iq7ZqXr56n-qfjvdzgTEZOB9HxjwXJpNAtcNml_fcyxOF19zCF2BCdHLDXPQZhN7P7hJ23D6PEPoS9vMcvDJQHeqVO9lw3GUgMR4B6X4v706aE4e65G4cM-Kgqq-xFGSjCBDLoDCDH9B8QnLod08SiotgHd2qfT4N_LuhumCgtw384-JfLWgE6DF5jzpaRdDxrxeYvi0n_sQNCBPpF_gLKG4jTrDU6r2av1LV4QyfPbLpyUbNehfYv_V4PbRuULptwZ5qZqLGJdzmGfsEB4vzyokSlswpaPqnHdRaqSHNfInl51yGwySS2B5iKdGlTqF93iL6B9YjAfl6VXd6SDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzpcm25TcyX9OPb8ecdDfo1CJuJw7vvOJO_Ol4HcfNfkfUedm1y3giRkRgVcgZYBcROiaay1rxyzGYnD9B9XFzo3GfmHOFS4P5IrG5QVIiJYCrdtVSwdZuO27exEgxMn94m3O4ar1SpU_AIVQj55TYt-Av2NQVwTMZUZtSj9Si1WtQw_V7PvXJPq69tfVyLPnpnGtX55y7XQ0f4g6ELoJ9XRO4bLjnyK-Sq3omTKKPvdC2EfuQcnUp5es0XLvMcr7xWsKRn8aH7XxgUbiq2n0qDKGcfklVFdrBfBSpGfhBYPCPCrqmk-FUuUwimoAcpo7k_MxzqseUYtAEHOSV7Tpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmuFB4BooXYbvGLbw9BQzKcm2iZ3r_qFP0pkrnl3MegM5ksxwOfVLc7p07c3ie1GvqQj_77j1p9SFXGOggBtzSN2hfJDQwLssUfae-Pgh7xoL51winH4ih8y0DIp1OYgbEy4Soc_DPw-zwYtQ3sVV8h8OQH0Zt-e_NZ7l011ZALT7wgJ8PAv38Kxc7_WGAimNH_ie7XdqwVbFAnqtiYxQVbcQi6uKcGRy4y-f4HIP5wZZctLm0pqPFxVhy4kAOO-DbxfyEvF_5inDm-R_P0leykaooZN-axk0hTciL8NCrmA9p6LcK2sHYBbwcX1bKC-MDS-FP7Tf5S59wDM7mgVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USRAEFdqvvx8sMY5fmFq2njZr1Bcw8I1buWbJor6znqyxRkFMGNsF_nooyueqUSpYYSH38cMnQ-0TXP0dgJTOPpchU9K3rpsWyekUvJvDeoE6mzne-UFNVCD9LCQESX4ORD7Cn2Il30RM7NNQkCKqBObLPZ9Flg9HJssgZ3HUhsYCNs_O6eMQUFxplSiQs-uPOkTnhqaMNUQR-BF8sRE1TaEezx81TU-QizLUs3qcAQBEqfTEthB-E5o3a60ODP_fdmSTF5VrueO9cmPjyl4XxB4w0VGrDk7rAhhI36oU4YP1GSVeXzv4mrEfGWzfu_tX8vwQ1hnYB9d_PDdTsUxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=uG5UXbK4IxWN_2CGIArFxYKCcElcn3qOEcWCFE_sa__AHxXs6YV6RDlrgVKQNaDFpx2m6qFQutQrVbwmoacCCDAblejv8uGebwiH9rJcz-rli3Wnqs0GAZ-UV0ktbiCQbKLOy1WlPsyPw6JECczGKnOqZnuJ8HpO9AYP_bI6GRm1ArYPSHGwsXcilBOYb0peMtD_9SHcYNtnbj-77I_dPQid6faOGQJ1oz8tvZ78ptt-arkxoTh-7wsrxKcuJBlVePl1zxd5YhrwdOUqTGEll8TywL541TRNJPC9XWOtKX6jw6KVH8xUqL0kumbavW0rAvWrpUVIioH6d_ZhHUAvBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=uG5UXbK4IxWN_2CGIArFxYKCcElcn3qOEcWCFE_sa__AHxXs6YV6RDlrgVKQNaDFpx2m6qFQutQrVbwmoacCCDAblejv8uGebwiH9rJcz-rli3Wnqs0GAZ-UV0ktbiCQbKLOy1WlPsyPw6JECczGKnOqZnuJ8HpO9AYP_bI6GRm1ArYPSHGwsXcilBOYb0peMtD_9SHcYNtnbj-77I_dPQid6faOGQJ1oz8tvZ78ptt-arkxoTh-7wsrxKcuJBlVePl1zxd5YhrwdOUqTGEll8TywL541TRNJPC9XWOtKX6jw6KVH8xUqL0kumbavW0rAvWrpUVIioH6d_ZhHUAvBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7oAllsL8QTcaMBsLxtKrphmzMrHRynWNyLn8t4OI-IwUq32Yed08LhAP9iQJJnK59gUOPY6v6NA447x0bx91WR6XcoIqxXNWt-ML-U0Dw3vKCXLcbDawx9Im0nF6gCFRPmd7aru0RYGyKCq-LugdI8PvvcaBzRrY4rChYC-j0sTMWoGOJ_Kwa8lyhuvJRh4JlnZBlnDsD89qFvUaOzFNZgwBThbEwmB2rXMlkKrKj_D8ax2sgd1FUZQMU3CCXnEsTEgrWkO2-rvAX1oH38phodjtlka-7qU8XSgaUe9ROwcGxqbOhIhjZN59Dbecv_wn9nsYmQwEAFPInopdDe9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-aMjpN35VOTfTnVAXcAu4Mwy0dljrEjT_DrwJAzI4MQ1J4dLzJsm3ZE1N1onj29iZBKBtsmD8-ogSHYUUCgo_3O3e5x6rtYXGSalZEqAIVI01TMi_avOvU0m_R4yOS-anwyCi4BdPEtS-f5jALuBAeT3tASdQ2lBY33FB5h0wKSVPjKtNyhDaNVeH5t-6W06UYzs41ctBQc0QlBu1j0fJ1WxsyCCVd-XH4xgDQaRpiG0J2hk4cfdUbxvgci5ksVC4L2CpVZvMx6CTj10IkNXQQgH_wed__gB2TnfNuKxUYokQ-UeYms6f2rV7kqATLI5BDnjfJnQk-ZDhrpEi3MLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAN1V9DEx1bxm_p4lxw6L5gbwEmHDRTiHTsiyHftzZOXgqIrR14c5Tmwfd-zjhyuQAC92mh4ppchPmQ9X3_t9-WFkcJcxPksPR5hs5S7NO8fCseU87x6BPiw4OtneD-dVamdhYIm8R0rZuSAmUDe7atv2EYV9pbBGdz40ud0Nx_gwRmCdP1lF86GuLaR79cboFVF0aKXwO8UruQWNKE-mFb2y0_yO-L5mjrAWEw9FPY4oytanuzeo8vNix_i2J43VO91krmF_YKRFvfvq7roB06g3LOmjpYhXon7dZEFj3S2i49fi7wxgCRbJyo6R7yDPfx7wcZRaNgZSzyy_YPmpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBatBncM4z5Ha6id25h9uml9Js09MuDVd0B1xSiTAaa3vwc_4govjkGYjS6rX6Hrn8dAXFM-vE8R4eBgkYfhr6zvTUiX7JbzOq2gqP7oO90a908MCdWD7lYZt6Vagu1CwLVXzpHsADyla0Bmphov_97_pbSXGzZsjnN8nRc5DxMebwj0-RS5VMrbvJMVzilMYpa_J-XqbuT48EFJX_AHHWVRUOuVG11Lz9LyYvgmTB5OvBzR5UWhr_Kg-iciXWo1Kd0YOr0S5TzXvDS4gUVLcMB16209heeKn4VbJXa8q-xF_FTCPuL2dXRXr_uACLPir8xm36wxi4klMKbBBzLtIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXNTx1ufjD4sknClmx2sx9xt1NQ70lmZTN2nheQo75-eNXArSpiwpZm4OZ4zPnAfj0k4jxNNhgzMLNpGgQBH6VeYZ0KkTt_kp6PoKUUJUraVz2LayhkjsDmni76oEXopAfm8cN675mxe56O3dROGfXa6ErVzH5-CjHiNgkgnjRHoVVDHV4GJJOvShwk0M8g-whOcLWky5BTzjDVXaz_SqTdkQxNsbQMkTIhID3beRfO-L5DrjB2xpPKrMUNbt7VmLhdLfBnNWJlQ0WuDBtJ11wD6VucxBigt-cIY8r0akCXP7m8yd2DU0Ahz4KE-FJG922KoC0wA6VlrT7gubHHqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfpG40VCkE7aGQhW6j83U98Spri46JtzU52kFOYKHrEfy6jh5-J_K4tklB9xO0o1-9Ma6kyvLwzEaM6w2Wlk_DASnNYLaFQA6f2Jb0rB6TcdgmrVipwbaYpLAnFwdos3ONf1ABIdTKhMM12S3UmMKY9es6J9WCHZjohT7f5IdB7WltPkhZyFhC5zjCBcQPodnirgNRGfKMmG254txmR-bzYiKnXIZC8FxkRO6TsDr2Gak_83ud7Hkm3qNDTsBlcBGwcQbZoyXn_OLlWlXsw-PiP8z9v8ewcz-05eh0IvKcp311x0DRueSA5YGFxjDsXGJqtQ3jWCd7OOrc9rDm_p9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOoYWJxCEzVixDvFnGpUjm7LWYQP-tFNnnie6_HgpSIAdXYBpZQ7Z_LH3S1c0cA4WuIalDLpq5J6uXrqVyQAtu1gDRgTFaHn72-xFJHAaLlYPL4oAOGpnGkTXwhSJ_8dGVdWa0j1rbs5f6rz1-lCZimYPw3djQWm9o7magOMvMS5m3ENKAqZb4zfBJbzObIrarIAWkbrMK5Y4arSY5S3B_it3_QtELVNQ5cH2Q5rThVmvVhwvquU98PMW4quluPVgd9S0XdkNRmyW-GjE-Z8c7_O4sUjVo8Tr_Vh01Cj4sG6cPUro9M0Y8FstNPWlAT4LEadA7OoeBH-JEEBrwzUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpNZunTGIY8nQA1Vf00pKk_kYHsAQLVxtktwqfpOC84TLAjORDEFV1CJC6SkhiR0ah_W1_UAocTQB0_EAhyamV6bYd4WwUaML6s6Q_ybSiDdoaECsvUKXhs9EdFRRjGw4Dbpf7H7HRoly0YCvy0ghuHA1_wy7sev271FWIUlNto9rI_iUEIPikCL1viA76rC9fPIb794O6u6asY_AgUHaQKn0WRdtdRS9dbkXMg7u0Gp0DR2HLz2gKgQ8kbhEw2lem2lnpBTUUUJopIClmubTN0dA89m1OokN8OdbuWi0RY5SndqJ-B9dvlwQR9B2spPGitHfRG15X5gGjUmLvqdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edVA5rO1qJjEidBB4Iy5gIgA7Xwye0mB2TpTIuvScRPnmMIZUAx2JUxzkxW2hLb6U6sjJucRFBgcO4i80iRqmS9zaLetIgDUbBHqIlyNfb-942BjXc4QGOLdCXodlVzm9LpGO6yVCcQylxS-JbSrSJDZGXJddWoGxu63YHfsb68diuXkisvX3m7C06fwDzVKlAMJQYUfy4VW0fz6x0aYdbA-WKdyDQ8HXWNGU2hLEjOrxA0MRszsOt1_YGXFGxdtaHEJZghjUAjVhmv5xVSF5ruK67A39Q15XcoEgk7W_iLQZJWB-gV50eXzdwVuFe9_6UEIQ_UrT70DuxDLtc2KoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=oHIfSI0b5Q3OrsdpnZYGgNwMxFQ1DXoKEzqBWX2qm522OIxfMa68HOMXt4CWHncqTjCrjCCv5aB91rfG5-TR6U6-hLGTyiWombrVCKeZQqcsX0lWIlyVdU9LWE_DAMeeKv2Hz75xP4-RPKMTLm5yU16n7XV9x-gGa2c_B1TgjDIRPwdd0H4pCrCKg5mh59V1acYsw23GxKqKajcIyjZ7JQLbdCpmtKMtgkAip8FAksxEiDicu9HIyxS2As1_G_Tnd1QZYVQC2KU5WtFVgsdjYX2SAxNHwSiveER1z9w_Ep2UdfU2lNxKBUoiwtlXx8pfHLok3wjqe7r_kbs5OqXvFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=oHIfSI0b5Q3OrsdpnZYGgNwMxFQ1DXoKEzqBWX2qm522OIxfMa68HOMXt4CWHncqTjCrjCCv5aB91rfG5-TR6U6-hLGTyiWombrVCKeZQqcsX0lWIlyVdU9LWE_DAMeeKv2Hz75xP4-RPKMTLm5yU16n7XV9x-gGa2c_B1TgjDIRPwdd0H4pCrCKg5mh59V1acYsw23GxKqKajcIyjZ7JQLbdCpmtKMtgkAip8FAksxEiDicu9HIyxS2As1_G_Tnd1QZYVQC2KU5WtFVgsdjYX2SAxNHwSiveER1z9w_Ep2UdfU2lNxKBUoiwtlXx8pfHLok3wjqe7r_kbs5OqXvFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO_cxGY5mbrnjkAdugPaAEl2BGoXe2EZfpGRP-IuRYtICaElie05UsfxGHCykFFJZLkL-hPmixwG8iySqYqrESQV3GA_vnB1dAO0wIdaq0SdN6ZHWmrn9u2c4C-Xp1u7SWYk5hrCsBNDrg_h6Hj5YffEddx3c080629Hxw1mVKujpst4lJtFqAgVY2xjVO8C7kQo0fnb-S43KDBijROE4kmLiYEOdW7BQCRKV0kiOsZsbDK_R78sIHr8uu4SK6vCVPdXmoVfffTDognBnV6zuhBvEZc80XcDsol6q25JiJQA694RSa0cZB3Wnsk3wohXbCodmmOtiSpUBp_oePuxvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-gFOPiD9Efc3P2JUZ-CzbtxF2Lo-FxWFK9yL3GC98HumLXXWhGhfqI_gmnGYeWUy9AjUGTKYFQt6Ps3OsE577auXIVl6KFNAM1X3hihxQo110xiC2mgXVk29I30bZy7jPrkVOz98n2kjU936ZHtIaGcqg4ON3oBI6qVt6_TGlRjobaprIpnk1RdpLDnNlJkN4u632e_MmX8OdutcHG70UUjQn8dJlR5uW9FF_RcYbhkjdvZts0hXBkpZttRpafCVWg0smc9LDAZjiAAlQgH09kLFKL59GxLAWi0t2QFXYHoSe5sFFF2UdbbPTPI4KpzMX8LVY5eVyV9p9D4OCCTwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTndy8M6U-eJiecdNjwXvgrfK0F3x4d1giP1Ff8dqjzMG_--pqWaAxjs5a1uxRMw_lAZAzLJQg9EMMAIJi_6-cIHES1xw9CkS-i5lVZPKM7perSVz0nwPVWdswv-_U1-2n7pbqOcDCgDw729I0m55_Y8r6lvHU8x21uuBzoPOjfXUUDXm09bpvFduaHq589VFp9hTF7jMN3bXo3RUgW10LA5u5zxDD9J00vXcu_Cf56r92G3BK-jVFgcsURGomF98XJD-nTfhnDmS18SN1ki6Iu81iD34xLOcIQB_gHZJFrO8lq7hqc9bZTh-Q2Cj4hMbAWdyHlvwQ7W482zhncpdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG4qtCLbGlL7SlEC1GYhzNr0BEGgsy4TE41xprQi5W8GNvXNAADKiVBMQTpKuraIQVYoWrBSQHVZWIjHHMGX4lyaXgZYG7GtHTj1q-afOnR-NEleAMFS5s4t6NSZ12KcO6-HaI--DaDOBHcXifENWGQz93P90-u3UMsrhqgVewGAaLIi1ANGPZZKicq0y5-j4RfMsOYseo9JlgXu4O5N0SWTdSv5avrpWtHYwn-mt37biS8hrGvo5eoIgvidOD8yWBC8Z2YX7DPfleDou6qkwQN3hdjYyJkZv3g2fm5szLBsdZz0vCKHepZDRi3KAtyf9RWrP3KsuWD_yPceeXM-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYIUWZxXfbP8tBH6uBObQpukwfF5dTsmZfvSdihPYtm-OrkBI47zVhxL0gtSE-1uyn0eYccxMWMuuP7r0hue9Jnsi-0W_RViwElL3MtLxpzorgn5sOD5qIKPMVgSt65MWaaa1XAJgMES6keZBmOsJACa6nL6Hhi29jcD3jrXWeVsn3I3OAcnASHd7Z8fjt0FNH4uKPebGlikqaWCbnRGmAiS51PI8EhBFvXbLG30iN4oN3RsyQPcJjULuxUnENuw1sU8b_FHBG2z4twhR74UOJlU5qc6FD4GSJWSmnoJArRPyKejsbm-BIC7trTzr9NHYP0jfLxMVxEEsTJZaaXHsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av2-y2OGzmOtx5Mw5fAOBkrojxYbfls5e9wUWKYzFLqFCVdt95dVaMcq8uT4wmRLJpifLFdjHCbF2xpk_tor_DXT19IGXeGHu9ryhYGsFNYMIizo1f7WXV1A97L70cKXbVNTjZfIisFfyWCc1gtxX_0Q-CTmZ7Ra-P4L3Oq38fq7cje9M94RgTiqT-1mA546I4ThtoMIjV1ork013BliD8rtx4RCN49QkVqb_Z5RI0q1nqGAS-S8HMulvD3xTKysixx9ItzKKKHXceW2OP0XyyAZFNKxtS2UlwucG8cxvvZjiQoNw_yY3cL2XOFHdRd8Bz8DpUYePWP2p4PmG8yQkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh9wcq3BWKiI18y6FEjh_2BQUUUAk-Gn61UoWkqMAgLkp2SRcEQL4uLEguGnviE3GAlEOd3MLoquNQgXBNmXNm8m7zZZDDcJpi_glMGmvICD6zeewZyTHeEGMJgh8E0iqTfMtYa-BEj8m7Guqp5l7NqJbZD17CtUfZTeilHsWuBTrQuTzZgHxYL-JgaD0X7ZREvZyM3JwreDrpVPD6FBDSzhKipx_ApibALnE_PVCWTgYnznzMLlKj6kMVsEBfivLjw16_gGxG0RaPpgaYMoydHs8PWGtugjv50I9jUKngcjWSiGENIXzSftVtl0CZb2U-OYPXOrpKnkzAhWhMOPTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arrkT01Zzb-56L1210Vt8uS5Y7N92EoChB9qxuURVVit15Xpjb6_OHHRGJ0JOlVUVLOBWwOpm2ehJL2MLkDk64ssY1hqa3yebdhrEQcXTLNjQsLz8oMKveaiwmpSqbzdJ2UrZ97DcY_Vq5JwsOaaUUR7d1M4kIUlTBx_IBXWkwq0HyBN91EfLOjFiuG_wpv1TaL74TEtoOS0tZV_CvDMVxL4ODNp3y5lp4i-vs9lEdldpK6XKceu1VapElflFK5OWcPBfybcGFzfKa-OwQ7Rl01TpE0dI36hnK5fVkBMvPBxMOLE9bmhjZ02whzQ6zDLQa752mswoNE_cHtFXcCj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsg8LZIRIIRM89Nbkym1m_UyRkBpWpa6KlDIYbmDWJ6d_ZzMbVCi6WjevgX24VZZX9iPvEypkgzRb4m0LZOF7lGsbyYMKDfxTyrYpfMGVTOJfm-H62SbrTWSyh7Vum7EIUVOdHuVcjSA2II1iwwu1rSM12k4r-NRFMMJ1rk7d8smj2A47QJDQV9cFWsJ4LTplEWbyyjppPYYheOIyub5WXIb-r07D5vDUDFSgEqPyuLXTuBa07rGPtHHw3ifaTbgB2mB8CT83gWlGLVcHHc72ZoZVO46fSb_UH2n9shGYo3utvwyLgIEhlVPdJuSHj7nUo0Ca_mvkoRqGsJDR97kJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGXFpIx0u_bwttvpdzD2jtq2vfuncn9pXhHtt0H-oI2mWOhMQsLia6baAEF4B3MXE5bqgSbMzWmZwqkm1lXVAmU3aHOO5KhI8AJa0iza-yHN7ndZiRrkdwYozkxlW5lnocMHu9Jx5SAV-arlndmeMfxi9UYgUU07QF9rkkMf5j_PBViE3zaa6pmY5yKaa364djDvGFYHlt8GWjfq71IH0fMj-1y7Ql8V1IQKYvnNxpz83c6c7wwrnMcPL49ekuWX2gZxaGmpFKPkwKbuNu5pV50YZfTl1s70rE8mcIUQTfLj0A-vaGRFe6LweVaGC_t4xOzQxg6InzSM1bcvYm3k4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=dXyH9Fe_x9Qsubnc6wHIPJwAnLjt_9GVDzLP0Xtj68dF07mTUi-yjb9BPwTUmZFrTpmWoOi-yy-Gth-c9bPamaYxOwyXQ6Rt3pWBl2RJ5CDPEP9nwP1rERO8cjvFJNS5B-MDDxb_FaRJXab-clj07Sn9qNVZ0_hNwlb5wpUArgEwH9F7FHcSiR2AvyUsXfhlA7Xqx0Bcj3itGpGDAAaVUx5MHZfWY8Pu8mEOn8yWx6Hq6Y35tkQCcMbQpNm4VyzjUKtvXo_ooX9369R0qMHUsBWY_21xI9W9Q6j2-TOl_Vyo-fG_b15eqOhTLa4aomJj8GKIS3R4_Tnxq22lbgsv9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=dXyH9Fe_x9Qsubnc6wHIPJwAnLjt_9GVDzLP0Xtj68dF07mTUi-yjb9BPwTUmZFrTpmWoOi-yy-Gth-c9bPamaYxOwyXQ6Rt3pWBl2RJ5CDPEP9nwP1rERO8cjvFJNS5B-MDDxb_FaRJXab-clj07Sn9qNVZ0_hNwlb5wpUArgEwH9F7FHcSiR2AvyUsXfhlA7Xqx0Bcj3itGpGDAAaVUx5MHZfWY8Pu8mEOn8yWx6Hq6Y35tkQCcMbQpNm4VyzjUKtvXo_ooX9369R0qMHUsBWY_21xI9W9Q6j2-TOl_Vyo-fG_b15eqOhTLa4aomJj8GKIS3R4_Tnxq22lbgsv9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_0cl0VYrjrX0tP0OxeAMviQDLcrEphtvPdUYGyQXvgoNSXyMm75ViytEn94JsdYfQx6A3YCUruVLZcchEgYwkczGTGzeQURSf07YzWoYCNP2skGpC2FhpQ1-SYFoy2QloCIUaCTyko-uHeIEXLMPygVhagKB0CdvQuSoTu0W32Bm8jHeEE0CKCUhGvYsbtAQkmHLh0OejabBg6ll1cJ_ik_Bli7To2nzj4i9CejxhNofoVfvlhHo27r64qYZ1lUq8e05QIKhDff3XuhF3D8ypkR28mi0UwR4ZwK4y1J3AnTlX8XpZna3l04ghmjkRXtRDIOe97kTF5IcH8vr9VGaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=tF3aPa8KEzWEW1VUKXorR33meJXZmvqBrhQBYQl43EP01GrIiZ36FBm6lU4YgyKK8EwYKaHRSf14EBh68MXkNroUTVHjDWwi_TXQ8qAEQWx2WvzkJSPYsqE0WnWNE9lYfi0W9uN-5cjjyR5lZY6cYADSJq1PKLuwKlxz9qFApYU1fuR0IczXCdbdg9zVB9oWMa2V_qGarglPEZ02F8VzlrO2jCyPwZ-xoM6R-u-mRvPIlkKOGmlSead4Z1InpmDptQxDvB1-HKPKvuQowJpnK_lw7TihOnEmc9Uz_7jb6nnjm-tRIsHLTCdZtvQaLAZa8COqjssEwsk_H3Yle7LUjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=tF3aPa8KEzWEW1VUKXorR33meJXZmvqBrhQBYQl43EP01GrIiZ36FBm6lU4YgyKK8EwYKaHRSf14EBh68MXkNroUTVHjDWwi_TXQ8qAEQWx2WvzkJSPYsqE0WnWNE9lYfi0W9uN-5cjjyR5lZY6cYADSJq1PKLuwKlxz9qFApYU1fuR0IczXCdbdg9zVB9oWMa2V_qGarglPEZ02F8VzlrO2jCyPwZ-xoM6R-u-mRvPIlkKOGmlSead4Z1InpmDptQxDvB1-HKPKvuQowJpnK_lw7TihOnEmc9Uz_7jb6nnjm-tRIsHLTCdZtvQaLAZa8COqjssEwsk_H3Yle7LUjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSACT5f3RfYknf-kZgBYjzECofxjMh4DweXQStYcvr2mjRTgnbK3IzOgXMgEvfz_D4sJrY-mmChG3YKoksgE5pDnmggBY5JONJG46xOKr_mJNIohgvhtkmu1NMYppIayKM6d-ZiMCxVxwVLWlaysUSnu1W2wZYmtJsp_tXTHe_srpLwtY5JLsKzw_-VuWBSLlmRh2DSMqP56cYxWJlo784kOPuxUTAt_5W1L4WXUZzhTzV5YDD6T_XQG9_arv7IOmdR7ZiActxzAdJXWqsQ9T2C_N97CLJb10_myQ7bLGtJrF_n060eF23ZbsFdtSeuCxTY7S5pDRpFE8tSy7dc-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRct8KQWzs1sq5rWPoNnWMEHgqATpCRsv1kGr3_j4uN4l31X7L1Cf_pMojs9a71F6bsyj3vGui4-SU-Uj9FMvS3Mhk7c-bKr6qLFnRcCfsK923TEHqoW5GXX8jhHNVB7SAQsoD7FuuBTVrn_Qsm1rSokUK_sv714HWEDqiF0Yzh1hKJCMdbxAHYevMkuRYBk5nlgtSrxn8l_c5-qsO6o83SploEPVqZC03p7mQdIuhrYUTkGP_KVnOu13nvlxauuA4tcOqGY16TsUCbTfyfuqd4XlgzPVhZIx9gfFDlzXJQV5_j3m8HF0KMezs9PSmlAzNlnl6LuLRpMC2PKew54sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfuouenNewDvXRIq44vw5S3o1vqdagu2XQKmp4lqeuTQCcA6x2iuavn9-b911W6PZnAl6oozEm2xfDTF6pgi-dOmHyqEei3h2jE8OIjcnQAOLukfX_VGgLc8BtYyikaJTBVb6WCpVn0Q1f-pscALVI4S2o93M1zxQ8iws-sLjslJ8VslvdjL5JDvl1qPuz1pZQjOzXDb-TKSW26PDP5L7AJXd4FaG33Mjz40jDQw3dr9rLs9JK7R-WQzfg2Mtuxn6A-5JucLi958BZC2c8gKKFfDdtDChKU9c_56WcxKEZZQlT1lWDVC4bh30cSe5F__UIieR93oRpzJJJBefKNKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdPmkwTu--O1WYOC_8xvZruj3XIiv6o_SnRz-0uiOvUaELGD7lhLC4RsYlnYftW_PQaeN3tb2kX1854lYIhkKmb6g5x0vfSltqZPhrj0XGNpWc7WNWUpwuotwgvW9lsufRah8K8hoO_6JfHj7qWkN22Qj0QwBu2yjSj_geSTJePru9Pp7WREQnD8SKPm2gXgR4ukFAz6-n3cvh30O7Y4zTqGj4ZmeyN1-HwUj41LnIPLt532y9x52MZvmKqLyU2yTGJLHuqbaFjPXs7RV-jzCw_qJdr9xKf71sDXvl_VaMi8dxeEOOQ-OwS5mlviQUOtnAuvboJi2T_5il1vQ1PSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1enRNqJs4Tqhp6f16Y0n0eikXlW6_IS46nI34nVWiuWbOXqhWVaM7y7gFGQpbzSdWXc2cgQI7A-yMsRy1e6nZEXIFe1jAxOP4_1tcIWZLTRrSHOB4oMG8HWmIwF2UdDxqHHqcFLCWe9wfVekRuHmyw29z8u_J4xe_vNG-H-SudBn5rltvNKSpapPa06-zzlmFQniaVWKSCOtT13gzaMdaFchgMl_nENrNo05n0TWk3BRnWmAbA5mPcYs3dLsbW13BN9ka6awPsly-_K6X-dO8VeGcZO4Z9Uj3Rnu5mqSnmsgtBrFy_a_FxIdfQfktcSAbwhR1k0iXpOJsbSGqDXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir2OodVokLsaDm2Tv2tjzXgBcSckEbucdzHS3x8WETJJfqtc2hwdonPkuvXTw5Ag9kesF2ULTDp5rKTa3uKZ20aZW3ba6n8vHcbohhC9FEkzUWQ8khNynBZdeYpLBVzTJNiLRNkdQVLiebxjmKKUmVwlZOSKotTrcguOBe2touXKgUj4fnsNCxGRcHMOpX5mCuaaD6DADb-k5yA8ncE1aN1uQB641CCrNVzCYpmEftfPHUuSzquHxh9SL5AQSJ0n3ehndUG8b_xh9MEnTCnbhN75lvA3iiyW8sW4nRxJm77zb8OQP6k3qTZtrRq-XpDy1fZr3sLjwtwAmZ4LUZtnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=LGPYLmxODVAmhR4vihY8BrHcsiq-RS7lMKQ3qSS_ZYVf_W1nBDS2tHsC_9NTkf3mXpSkHs2NDkYefwPHEOTZgIvFYxRt1vrO3hF7Z4-BoBHt-QCFZ-HFC3YWsONMqOPWdBn9X4w-3ZBrvtanjbFD9XP4VM2SI8OEO9-kc6g7-AEnfKfiOaT9OlcEpFqirp_7MZeDPF6_PXMzjA46AfhQokxJx8gscXXruToSssr9YgIqldJmbvwlIK9tUcOcUxvbInctUTY2NC7EUD5x5UWeY7y2Jks104WJAAfOD8nUnlceO4Fbnj7BNslsCP-Mom6rCzEp_277rUnoXKNJFx0vWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=LGPYLmxODVAmhR4vihY8BrHcsiq-RS7lMKQ3qSS_ZYVf_W1nBDS2tHsC_9NTkf3mXpSkHs2NDkYefwPHEOTZgIvFYxRt1vrO3hF7Z4-BoBHt-QCFZ-HFC3YWsONMqOPWdBn9X4w-3ZBrvtanjbFD9XP4VM2SI8OEO9-kc6g7-AEnfKfiOaT9OlcEpFqirp_7MZeDPF6_PXMzjA46AfhQokxJx8gscXXruToSssr9YgIqldJmbvwlIK9tUcOcUxvbInctUTY2NC7EUD5x5UWeY7y2Jks104WJAAfOD8nUnlceO4Fbnj7BNslsCP-Mom6rCzEp_277rUnoXKNJFx0vWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=Cf0NmljikseBAYAERdWx_7VJ9dmHFvhQjOMyM3vcm0TuXsuMtDkF2Acigv5kke392ZMEGGdGLgx_NIzQ3INaoW2esK2fgJ2E_KXm1DI0FqDSr9Vtjog7CHquyWLxdUthgbAhbVoyuOZEOWEkuu0JiCUHDe5o6OCU2y0pgaC97ggRTZqJAduynoisa5F9QEE4sSIdJRxHnSIs1BIzAqfyBs9GaUF52JYHcDLzQjqC5p3HeVqDZs-_e9v6rp3FCHEp7POsHYGobyly_Q1GK-oFGLst1yViEwoM43G50vH5AMZ7VKm_fVuD4L67tBQAlCG6TOC5weFx1gqXP2jwTXn8bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=Cf0NmljikseBAYAERdWx_7VJ9dmHFvhQjOMyM3vcm0TuXsuMtDkF2Acigv5kke392ZMEGGdGLgx_NIzQ3INaoW2esK2fgJ2E_KXm1DI0FqDSr9Vtjog7CHquyWLxdUthgbAhbVoyuOZEOWEkuu0JiCUHDe5o6OCU2y0pgaC97ggRTZqJAduynoisa5F9QEE4sSIdJRxHnSIs1BIzAqfyBs9GaUF52JYHcDLzQjqC5p3HeVqDZs-_e9v6rp3FCHEp7POsHYGobyly_Q1GK-oFGLst1yViEwoM43G50vH5AMZ7VKm_fVuD4L67tBQAlCG6TOC5weFx1gqXP2jwTXn8bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRfpXspnGXkNy4dWM57d-_OMFsaTCZMlscuFX5k_Z99sfaoL4U-Ua4qW5grz3R1xIDHkgFciLEPJAh5ykHkMTNZheStvpGlaYDs5gCkqg-C78sohdQeuwwoyYyCBU1cklYCWG1wYWzM7Jx2gC9bNdateShXPn4gLmNWGgHUGcmE_5p_YZ_iY2mVig-UeLM1qUK_MW-fmu7bZkbjGwNqhJQ-P9UiZzDoCiUNk95VlfM8b6knAsITHeCclmAdNeZuRCS8vPI89Wl3E6FsKI0QrtoiDhbBq1K-kTcuTebVp-Occ8dQyDJ3iBo9p8rGYYNcDEywiw55IYGVuhhUVQFPh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=kv6JY5MeMjfykytQbNpBg_KwoO-T4Be5m7fAnEs7CC-azlJfU6MyoMCDcCCQLGWfCWvIVN-8EoVARU_tdIJz32t-jljAcg4Bw6uqCKeEt6hIOf6ujHnSZkf0Z5AWIjpp24uT9HlNTQ7dQOPxxPmVdwFfjKTF7RxVG72DlVXv83WZBLX_UXANeD4zfR8mPYH_rvDbVd0EFmxlT_dUDO5miHYfFAfleAoXwyC1HT4UWHbcJjn5PtqdlDxXLvqlKhG-_j1dzII04gTevsXbo1z4bq-9_-cK5N0j-YXdEZsNrup_evrL835zRtFn1662fvO_hz7tpt2ZIN2hIr2pk_BbkzIHGc5Xph6HWlTg-_ZQSgPLX55yaPcNfGOStpfKGuK7Lj2fnffdR2AYYB3mJoT0s1QnRRsZhug361ibBS7loQe04wESRxif4SxvHa0vW5wNPsMAu2TWE54IBzcbLFts4Nac6ppy6puuenEd8ZFZ7zwcrMv1roN_TmJ6yV773-G6cAYiIIZUY4DsfH5xTkyN9wy5PsTM377i_XASpv1Edi6JbPdiQ-ZsjeuC6-a1kU4BwiipBW4ggHD4r-odi20dOlREjV2f0LUGbW5e5gqgEnN0pI0Xsi8zi8RDAqncJDiMc7NWj66uqG4ImJQaObfTB-6zSgJ241ayaxc3Q-ehluE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=kv6JY5MeMjfykytQbNpBg_KwoO-T4Be5m7fAnEs7CC-azlJfU6MyoMCDcCCQLGWfCWvIVN-8EoVARU_tdIJz32t-jljAcg4Bw6uqCKeEt6hIOf6ujHnSZkf0Z5AWIjpp24uT9HlNTQ7dQOPxxPmVdwFfjKTF7RxVG72DlVXv83WZBLX_UXANeD4zfR8mPYH_rvDbVd0EFmxlT_dUDO5miHYfFAfleAoXwyC1HT4UWHbcJjn5PtqdlDxXLvqlKhG-_j1dzII04gTevsXbo1z4bq-9_-cK5N0j-YXdEZsNrup_evrL835zRtFn1662fvO_hz7tpt2ZIN2hIr2pk_BbkzIHGc5Xph6HWlTg-_ZQSgPLX55yaPcNfGOStpfKGuK7Lj2fnffdR2AYYB3mJoT0s1QnRRsZhug361ibBS7loQe04wESRxif4SxvHa0vW5wNPsMAu2TWE54IBzcbLFts4Nac6ppy6puuenEd8ZFZ7zwcrMv1roN_TmJ6yV773-G6cAYiIIZUY4DsfH5xTkyN9wy5PsTM377i_XASpv1Edi6JbPdiQ-ZsjeuC6-a1kU4BwiipBW4ggHD4r-odi20dOlREjV2f0LUGbW5e5gqgEnN0pI0Xsi8zi8RDAqncJDiMc7NWj66uqG4ImJQaObfTB-6zSgJ241ayaxc3Q-ehluE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnDAA-T0gJ3i7zWEpTEC4Ur6tk2-_n-5uqzejS6QGUiW5valDBZu7zphC2HuGjBhAlUw1Q-HB4n8wbu8qSPsW_D0bTvq13OXA1URv6DRcu-J8X8BuFzeSRFly_44QfgNjhtzPx81kGkHcEv9jbJstMgIhbeqbXy-RXA1dKUXJXzRgHL8tgL4kRHzRHspXtG6-vt6fSrqjEsmWadRIgGP5lE2zTf_B8eqR0l9mtbmPE_zyBUwql5OTlt2IuhFU10yMC-8YYXohS4978GHs_XhUTH0I9lIzJp7HckEyxmzEnuE-sJVuBkve_j0dwFJCSqDn2JUyCF6Fd_Z7hbFNPDQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLenFsPMgd5ioydpZWZFxoUukx6eoznxpW9qSZ425H_YXzjaPCdes-ajFiKeYjxZTCfg5K8fN1aZ9dxfh4z0HzrQ66h_D_AcjKm67J-Ego9WsS_t5iGbpvOdmIQh6duHndLVs7Pu1EEL6e2fGuk659bwWO-LWBDz-_rdXUTdLQvh0E8h1PKaQdU2VSikezelGkh-ITFXLAx5HApboujkfxgjmO8LplEnNVl37edVx-Q8MUrFoyNfVhll1keB7BI_dwqm7y_1EKN5_m67OOfFxIpexYXFnzT3YZGc2T4--mTMzeoe4o1DqOKLrtzHcV53q0G-RJWspRSnZb_zKp2oVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBtfa1xSXKu3aYPQPex6U6SqB9R76JeThw92TW-mPK-jvAnQ83V5cm10RcJfoY9MvtvXz1-uUpr-I_JyDzo2PMpLKs8xibo4ZQXa9oM83CIfIHAOipfWq5I8ArGM-sWZTmbk3QGoMTqI8x7JFhdo_Du-g4DAqSusBwJZHLDsL0Q4pj9sBVhHY2cJJQEfjGQQa0D9hCF-a-zNo6IAR4fNtl4EpYAWjEKuXaK_gpSwZfU2UAJF0n7dA2-DYMlXiopwQjGUt9Kj_KFaI-AcFhaNoFljIUlyFMNT5qWT-sVGZD7UGDOOT5GfsgM5pZ91fhBv-YjhOHffc1qzF30kyTY95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=HXhCtOH8IvvllpplpsGCRumtq-NfSlx8cWQ9OBJXguZVVbM_HIqkEBUGs33bYWifKaJoO75chG5k6sVB1sTcmt7gxo40z9xjUBtyCnPlSMnc4J8S2ofl53UHG5R2xipZBHMaTNo5PH_S_3ZPptUuyruZFxw1aEKR1h-7L7kEa-AX3LCv2KcKf-fpizE53mJtDEeFuJA2Jr8eDJHsALzhkfrbe-gNBzwPGEYfDmZ7X9gyWV7stRTkSUDTaigypURsACXbG9cUWCRrHW5ylQ0LWmNASs0Vu2qz9SDGwHoQfF0BLRj1U1tA9-QKkHhi9yxFXADjPahyqnb7JZPxHylJbQuw1C-NTa77USKh7du3grkoQTUKFh1ET5pIfu5ojcXj6aXE2TB6ZVKKaoXWTRO0A7XGiq-jcww-qO-FbKtgKHFvSo2gHogbhPOr3p30nQuCwcLI00CI51odADv1YCk9QSYU7r4ZK1LZ_sD675noyIT-F5q5f5oY80fhvccBgrDWBr911z4ahOyn7iTW36IhugtBS_34Rihi6CQX84EhhY6SNbZbMGbglj6DchOZJHQqByK4oEYm0b9gU80dGFMUlOda8jxGZWz_CRv_ZEvzH01Qs8BXyS0hHYhqxdsf3F34K21mNWEtFGLyj3YCUB4ol1obH2fycbQU-pyqT8XVrMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=HXhCtOH8IvvllpplpsGCRumtq-NfSlx8cWQ9OBJXguZVVbM_HIqkEBUGs33bYWifKaJoO75chG5k6sVB1sTcmt7gxo40z9xjUBtyCnPlSMnc4J8S2ofl53UHG5R2xipZBHMaTNo5PH_S_3ZPptUuyruZFxw1aEKR1h-7L7kEa-AX3LCv2KcKf-fpizE53mJtDEeFuJA2Jr8eDJHsALzhkfrbe-gNBzwPGEYfDmZ7X9gyWV7stRTkSUDTaigypURsACXbG9cUWCRrHW5ylQ0LWmNASs0Vu2qz9SDGwHoQfF0BLRj1U1tA9-QKkHhi9yxFXADjPahyqnb7JZPxHylJbQuw1C-NTa77USKh7du3grkoQTUKFh1ET5pIfu5ojcXj6aXE2TB6ZVKKaoXWTRO0A7XGiq-jcww-qO-FbKtgKHFvSo2gHogbhPOr3p30nQuCwcLI00CI51odADv1YCk9QSYU7r4ZK1LZ_sD675noyIT-F5q5f5oY80fhvccBgrDWBr911z4ahOyn7iTW36IhugtBS_34Rihi6CQX84EhhY6SNbZbMGbglj6DchOZJHQqByK4oEYm0b9gU80dGFMUlOda8jxGZWz_CRv_ZEvzH01Qs8BXyS0hHYhqxdsf3F34K21mNWEtFGLyj3YCUB4ol1obH2fycbQU-pyqT8XVrMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwDcIJ0ERz2cunhVleziv8ut1cO9rVk-xS_sLH_uD5t6hLkPlQa132f6Yvil7tOb0jXOKLx_UmkQn10DdVGDfbbPmo-kCPzSzwTNqMfppRUBZtJLcjLWdSLGfICy6pTD9MwVnAjY0ftTTIulYvUUyiMsd31SQSCkbYADgqag3DgiqhtU0hsn75dNypkxCjGT8x9hVXr0xmLl0azgsyX8lNjDopoKNHVzXdESCTbMPSe7nFwG8zYauHz7Ffhp9GvBFjnQlPQWLypMoKlv8ODAVrAR_Gyx75EDCGsHxhZck15sCHbT_k7XvgAzEWN5v9G_8tCYSHX1dI9eEDYp4XRrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZgn-TWELA69TsQw5yvaXdSJmx4vp5PMYtXyVn9bgLCjNsk_iswCamOwePJe6uI3fPfSJ6Yv8hafQqRGy_Tl_yeyPMjBjyu4sC8NycTu8BjcNZ3bInWdJ01-jWhBf4Vf2sHvaOYy0UB0ikeV1-CrRSoEMgWDCJD27A67msI1QJj4Nrnwynwb3W1jgjT05HnpPY6DWeUE4GaYGbWq7k9SgHhbG_5Bhy9iP9a7XaugloxNxpwEJ5K55vDCI1SOFvzcW14VQj2y_KDAk99pI5kubxo9lF5_ffAKHMo991zFXFXmbh_mXn6EmNu-i8bkqPGzI0N_v0J-lfTcTfrzLw85xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUMRaJLJrSqvk9hlF5TLRjlWG0X5kzjmOIqNyHFRYNseo-zxMh8gyo6iKaezMtYzWWL41XFvPoGa1p7mjcravN9hIyEYbQ7BoELtj5p4KW4Y1z7QML_wgOPtogKsB_yohYDn3XYSl-vDZXILZeJ-ACq-vxQTEqx0zvBvF9O3OGkWon9tHJnX617p2zmoNeF77NXda1YDnTfwnn6CYqlNmAzs82x9Gx9N4eBuwupF3V-GEIXU59s0z7zaFtf4OoOUdTCoApIQDQHwhx_Uw-xINsyVXIAeYeukWis2m7M-ghoVgpoGiPD9WLDm8uvvp4b3Yi2HFi2d_HAX1LURBzZ-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrLjUlE3M6zff9XRFdpTUnQ2LVaue84lZ0pfY6Mlm8W4OWv5rBSQ3w4EpMICYlxf2DkCYfytJ8mbHzTPTQlOK8kADOROvZRN1E6R_nYCx0C64jjX54jzCenqU5xWNML08yezIIsunoZXmxG4AQsBReCY0nQbGGdgF1wAQEh4ldhJVt9f3ZOhsQnoxjGtSXwU5WJPGvKyc8_SHUSKu7FlgAiqh2QO1BefZpHk1M2bLWOkl1opvJbDbE0adI2dgvwZCVFa_QYwV4sZuRBEoLXhiF1kPAVXE6jhmQHBDA5VGXaAtYtmw2RBIXn1zO_yyKREnxrT6ZXrQUIamEz239oKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iejnRlBOZRhJ7fNUDO6EPdvn1m7MxLrTH8w5KRCN-Qv4qI0fi_EK0wQ0gjtZN7A6lp6ZrZ6WqLEqSPi8sdb34Sk7QJTuOS3G63wuMEBgfqaHCsic4iVSRdetmEnt3o4ogpYlbe9vF63EQGa3pSNUqWtVKMOfvECDIy6xoHTuIG4LY0tVGwb-FG6CACrS-JP1rmeK8fWQATZRG0wj860Qrkk_-lxv08fP9d4_LdxeqwX-SFEs9rrWijrFS2wNEDASUdKs1RY-D6JGf89zJu_TXyN0dtEv6XhK9Sa3n5TRVLurDUL94pCnvSF1H9vVczGHgOZO7g815zMlHV3Sibjfiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=UscnbuSqlYrUom7t0J05G8N7H7tHJJSE7WRdEXiroWQk1DbJW9MrU-Odre_KNT5HGV0OPqCHGokmJ7xNtoPYPqnhTse3L40V9RiM-xBYdIYkyiQdKkQCXOAEmnPvr2pMcP0ucrJ53MlAu-U0yGrnrqHdZIEq_YDFFTh9K5ldJOtr9f3k3LSH6mawUrTJ3RFNBLJIVgRF-ID59noEZbmKCGOWKcXlZrlwmADuXM0UOXyBGXmwIS7Gryi0o3I9AnAjQyMGsF1lEOiAysBaYnkSk6nfJF5qD1WMJNjim2CSYZ-978yFoxSQ5gVL86n0TPZqujSlUvVCLqpO3p1AvGbPEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=UscnbuSqlYrUom7t0J05G8N7H7tHJJSE7WRdEXiroWQk1DbJW9MrU-Odre_KNT5HGV0OPqCHGokmJ7xNtoPYPqnhTse3L40V9RiM-xBYdIYkyiQdKkQCXOAEmnPvr2pMcP0ucrJ53MlAu-U0yGrnrqHdZIEq_YDFFTh9K5ldJOtr9f3k3LSH6mawUrTJ3RFNBLJIVgRF-ID59noEZbmKCGOWKcXlZrlwmADuXM0UOXyBGXmwIS7Gryi0o3I9AnAjQyMGsF1lEOiAysBaYnkSk6nfJF5qD1WMJNjim2CSYZ-978yFoxSQ5gVL86n0TPZqujSlUvVCLqpO3p1AvGbPEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-YRP6UFxkjSHmakCOK5HmMWV-xSgk-EFZOXWyxgoeQNFZTX7ZAQqSx3cRErO5CYcu9hAFU35sLSHYy5bGLbiZ-0Lj-u88ytzEj7lG1GK0zxDNW7Em8uYgsQ8gwodizuTlIvP0NxD_HqNPqp3xlVt_ZPRj43uJEGYxfybzNOomH6Nkub-C2SVzdNqR-9cYm5lS13cMltqJJgy-8AlRsBWn48_mT0Gh3sCUY0p6ZkI3mMa3avqSvppA-Zh8xzqIkDHk533MRhPNV6LpztROMEmzMc5Ja-dLcVC_EY0io5fq4C__XEncI7sS_uNy4C7evX7VEgV9Vyum-8iqSbkPHKYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONSk98JQqJUbxHW5ZgeXL2RM5Mbzg1Y_ZF5zcspBQLuQzpmRb6NA6FJRK8d5ZTNEYYuabWPfmcnDReQH4MJVNxoBuIrCnc5Pd2P0ZUxiKuzy3x-Sza3nJVocEmjXBQ-L_V-x0W4iK9tldfMR5SEQhp9eIAGzxkEwsTfvp3kM6kgRbBKFPlFSmHiNACLnFGHkUnMaHPQif8n4BvT-jLOxXljfbJ0C7W6XIDfaNqYfTMSxgDv7J75JEBXYUcuvbvcBuih3K1wykN_itX-9HnlTyQElILVGmM8MD9rcuDIJasOCf_kJ8_BE6fwMZJK_BvUlnrcm3PxnFZDobBg0C1vo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-ZuSd9bc8tBmKhwkjSKbwmEkm0kqHR1kKpkK_oFtCuv19epabVufh0l5KduJ9lg0VqC-2DLxg_ybnozhGELpaXaE2if46WGtiHmyoAKdlVFjU_FU6x39sFJgQG9HY2vkKxIawv5yxRVEWEH4znCmcFjB6rAZCRuef_csi0yhGSdsOELqu7cy8c2Aqlwg-TLHvu6e73P5EhLlPFv15LNboRYo2Pk-EmxL7VowFvzT4BRQv2U5w59O8UWDvvqSh6UFksxlg_mDepOudzp59_kuMMclNxavN7Q1FoUBot7YiDEeJHNZn-H13y5nfQZy8iUVYlpk9iuoqAWSpyb0buFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trZ_Rqt9j8aFZqdhzZBhd8Tt_LPJGWvRIfLtTEc-NmLLGMU4wQPRh7SKtgl5DT_EiDkSfWptfubkhOA-bvMsAl8QrGAsrbJ8k9mD-EimwcQpIpWsaJZdR9V81udltjGFkLI_UUu-6nTUv8jKEBBq1N_nm2BkKI1umyG7qiftvn0i_Q2vEmAlB1KWb3otKbXJUBDMKxGMhhOlE8-EAV0BEwSzZwdgxa6Ha-ZAnTCNq3lnxRhj3hK-DfSlFQ4zh0-kYRqGRIc6EoIrZWXNu0RLsb7XbbgVlfSeTxXfmSopSfSZ7pUbSktLDvYiAa58bw2GW-V9Gc139IRRzNbMio8fkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjpRHmajCb9SQdMxNTl627RxJI1vO6hIRTWPy4AXee2-XHlIcy6h4HVnfgB1GXcGS2AF7xNAK6SVELh_YausyDKeYvs3yJ-KNwj8_za_wQg0eMjxrpC2hkFxGp3gx_BYbTLX3c2JetndsCmuwJnVcEfpoeX6rSMqyETqh9FzcGBj6e5Wiz29OffO2gaX_wudk54GCpzUjRLkVUSx7QuN0_DqIA_co-zoW85i408vlm5rp30b3WU_y3U4CfqIEwzshtwtQ4utXD3cRpiFZ1rCjiAONaPA987W9SZ-bR-avB8ysL0X58uc15q8UOSESY6m1hJfi-viIzvGLITOnZ9_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=QwjyBeEJVBaWMnEmYM9SFIG7zJ-GapfI40tyaosItx-hNLU1SWzQttlqFDZX1jH20jV72UQFFWyCtuZBl3mv7DdiTPVdN4HzKLP8FkrgOM4KvrFkoUQWP0jqE5IwEaRNNKMuxUEFBKqN8ItKaNmlhkU6jOYHrv6mmdipb9GEawsOj9CYtiesOPUaB-Py3WZgVFuhV6m_dqolYnzFw9pWWkiPhOlhYN82aq-RmvWrZLJODfImAD91Ai8rgs43IJPDX9el1BGoXpNFj8WCCvhrCkeBSh7tXXFvXHIxcJvzQZIx4AyWwG-d1AK_qv38XguN05m3pPRX-torhVAG_GQO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=QwjyBeEJVBaWMnEmYM9SFIG7zJ-GapfI40tyaosItx-hNLU1SWzQttlqFDZX1jH20jV72UQFFWyCtuZBl3mv7DdiTPVdN4HzKLP8FkrgOM4KvrFkoUQWP0jqE5IwEaRNNKMuxUEFBKqN8ItKaNmlhkU6jOYHrv6mmdipb9GEawsOj9CYtiesOPUaB-Py3WZgVFuhV6m_dqolYnzFw9pWWkiPhOlhYN82aq-RmvWrZLJODfImAD91Ai8rgs43IJPDX9el1BGoXpNFj8WCCvhrCkeBSh7tXXFvXHIxcJvzQZIx4AyWwG-d1AK_qv38XguN05m3pPRX-torhVAG_GQO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOCHixyHU2QFbtw3LJ9D6gpyf1DSt_xJ4nB8wQFLf4BEs8bgpr9Sflp9pH02yzEnFVvw_cOlvA91NJADPIxvJdhjeclhca1NmIsVzfkm6T0-IV4_6kR7FVtd_KD_WJe5dwqJutEybvdT5-dvqlOO3IGEEIE7Ti_rg_aXYiUpnJebxQ7Hlbl6Nod9qU96a13q42tUA_bWr-mq4zhuBjZ06A4MogJm_EEHCvphVuloRB83sLeuoqq2kB7Obaa16JR4uJ_Ey2Aj1j4zzUu5pcgxcstNCeoVaAUOOSbaC6WjgeHxKfAArjV5mlqhfV5a6Y9a91-TnizelWdPyLiU38CNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQlbmxA10q1GI_bfe0O-Ih6QeUO06DIXQey4VdTQrlD2Q72auXjEo7DDZjdQwWMbAU4QsvLTdv4HjranMulHuLRrvqbDHa49-lgRChMF9ETp5kvz6GJDGHw5L0g7kKEP98JEufWpdVvcNi7lcRjiVIRglaMB8RUq_9ndX1FQRXPOIaYfJ31FGJFhhjHCMxQ16DYQ43WBCdTlsXYP3wRb7fxcqLSE1hbPcVhQd6-daiOHDFX5p15RUXe27fJrg_9Sbx4Y-_z054G0Xa71cSjeBRKn8SVwFuGFmVmKjXx8X43xd5Ujfevwe7Gay2SZ5b-4tjRFDXdl7a4kiPU_HXI6pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrGUSd0Vp11vVdfps3TOPaRNVIg7BU7n5Ztg-Lf3Xb5y1OLMJJuUnKddu_l9Mzd0nRu0wwkxaRdiJPCznsTwbYT6UN1lWFDOrofqA88QMv52wPA4LT66b5IyI-KzxKj67mTriEM8g8UQOU1_srsMneH_2p9diIwBO8ugn_NRQZqIC26AzPUv89iVR5BxbzKscrKhkBooMTJ4JOfcl8-bpdLhwH7Bc8Vjum1EEdFVOA82C-ha-zPS17nd3Jkm3vNYZlSCKqd3KVZevXh2X3uj_zspyBDsICA-R6Ij_eUj3twKHl8xdU4I9gm4mQTDd8Ph40DaPZwLUSuHUi7-bFtw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCvTYs5UjBv2kU8_r3JggArT870F-lU60jjFLgZc7bBqZ2v_ktAzUh-M8DxHYi2prnq24-OOnscYcH9HKg7rNPrCLEePg-9MC39pAFsXel6o9BJuwQ96SHAVo5__wQXznr1hj44vKXc431_g_TQxLRc1GeHQURZF6HmH4N3aoCQWRkWS-kdrBTvEw9Bad3iJ65-04OGseijqa3yhpDEKCpmlnQLOpsBEBKyJ07grIEojbdh5n1Ab2avuq8q2hdDJbirJCJ5wCHS7E850UeijpNTabZBE5ZleBFaPGTBOug4gFzMROSL8wgLQ-6lyn7FenVHf-5u1fvSEctqXcZ_nIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
