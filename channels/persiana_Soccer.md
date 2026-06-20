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
<img src="https://cdn4.telesco.pe/file/VKu9A8sneObxPkHUzJ-kWjwrk8uFxltL1gYWfVlv8Hvfat8EetXMgHu6rq_d30OMSeNsDFjDKeHcREfoh0Oo6xmw2_SA1-tpNauuoN_QwbZRGWiuzA4524T8fbMgNGA2IPk8w7i8Jr2M4vuzSnVooLR519ErL1hc6AJamMqL5Bk6ZP1ArED64DotO2v1KY5FcmBx6XXRzNbhp_t-tPs1CbwGs8-M6lxPY7N8XYK-5-aUTnO71njNNqangil5CNRdupWDles2wBRuCN7f5M1p_kqkYSK15unpYqYse01P5iHd8MfHDleXSChci2VT7UAe4S_Ng9W5HG02EtDeMxwSTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 310K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 00:17:24</div>
<hr>

<div class="tg-post" id="msg-23941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=UNDi_GBMplV9dyBr-p_bt6sCgtkZlJjFvfIAHDxBvQYcho3oKwmtCWSCzWqKtX0saCYh2QjhmYqG7whDASPewjsKApMIRTilGvWi02791kHJX37dgh66wx6Kby8bWu7X-zhX1xDvlft2tcwYaUGWWLq_2RC7oKgnYlq6qa7oBdJpLcGRbnFQGsAkpwedZP_ZFluzci-p0LZmHA93Hcmp9tHxlrRWqnhpmmiUWAUS2EW2jfsDxWge_H8VHUXRAgMRloiFMdXvnzGXapwh_5d2Nt4D1RWjE4NmUEaIx6M1e3ghNSBNgo6mWGbIBn3vtCe47QH98kL7RR1DNEF2yLIMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6c4ff321.mp4?token=UNDi_GBMplV9dyBr-p_bt6sCgtkZlJjFvfIAHDxBvQYcho3oKwmtCWSCzWqKtX0saCYh2QjhmYqG7whDASPewjsKApMIRTilGvWi02791kHJX37dgh66wx6Kby8bWu7X-zhX1xDvlft2tcwYaUGWWLq_2RC7oKgnYlq6qa7oBdJpLcGRbnFQGsAkpwedZP_ZFluzci-p0LZmHA93Hcmp9tHxlrRWqnhpmmiUWAUS2EW2jfsDxWge_H8VHUXRAgMRloiFMdXvnzGXapwh_5d2Nt4D1RWjE4NmUEaIx6M1e3ghNSBNgo6mWGbIBn3vtCe47QH98kL7RR1DNEF2yLIMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از دست‌کارای‌ جواد خیابانی فشار افتاده میگه حضرت عباسی این کارها چیه میکنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/23941" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri6vFnpNu4_Ei3KqePUHrInt8QXboAaUqaCcv37LuBXCXpCqkRWw1U2xYKiabLwIx-M_vUOCknMznBB6UXMS5KkdIsv8tQS1di3qwr0zEirazZWZL16ZXmMZJMROG6xIJ9ZYLLLlcb7hnZhekk3G6chmx-Q_rNjadugqLZquOVVbfAimA059w52E2rnjYSy07ppAIwmBFFIXkCIeGi3fO4K6fAmL2_NlRJZ-Pd_vPuk2M36cPg74079kSyYg8DkrJ082CLUOTosziC2B-3pJdTcXx71I-WERfx7lbyjbe_xHmQ_4RynxIENmU2CAsCnzFEfb8T1i4K_6QrECuAgL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی‌که در جام جهانی ۲۰۲۶ امتیاز کامل ۱۰.۰ را کسب کرده‌اند: لیونل مسی مقابل الجزایر؛ جاناتان دیوید مقابل قطر؛ کودی جاکپو مقابل سوئد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/23940" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elYpDGijupc-8COT4yf8BMzeC_LULD6dJuKSVV21mFUt3_vOC5yz1qZdymI1LK1Z9kU2QNSB3hl7vbq1kLk0WaxLyBxQ5qINGJR_ulqffILUDyVISHQk34JNDnWIe9HRHKOjJGePhwiwY7DZgyVKVdCLr8fqtrE7n7W7xer3gUalzGpH-k1iqVmewcsiHU3JbgKj1fe2bIj2vQiKjGyrb7Ga9QER0dxS_oYs9ffY_9ky5boNgf-S0vJ1LslvqZg0_YPPd2OfZJ0vQ_qGmneDts5BorJDWKPl2KV-7uzEWx-av6CYSiE_4a7ToTwISR2dKoGN7tnAssx2f7OOg4dVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/23939" target="_blank">📅 23:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4tRzUYeTUdDBCvcJ0CbvReN1axuMGOc52xbx-zo8qrn1tafIbuDu-eTAV7Cis-F8v2lG_7d8e5gFtjgBUDOcjJuG1GcMdQAUklpxUOPTF1f6aMzbnSDEGtTH-3CzixUYvkmrwPxs0CpyPR-jqfQogD-KwJ-B_ohAH95bfYfMcSCuNfYLtv0J_r0GmtUWAtfjo-_41f45Mv5PJ4lRSVQDs6Dfbm3Wv0ilclDG6sGi_YjYvYqU8TzZpVP7bhvge1v6l9HB5dJgzrxCxiOJQtsrJ77uTZH3s7jlFCywUUnCoqUKYJ5BzpGcEnYdx1xgmaPAXo2Pdddpnmh3MGXDkSG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/23938" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23937">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W04Jj6WpUScXU3IfrdrKtv5pUiy5nT_IJ1yr3nEWLUBWRUG1Rns4QYuV4QLS1NvKpanTDmJjjwBgZ8z6_4IYj3xu0fuyyahKWkWTpnxtKmWo3osMiwx_nu9a0hKOImMTyFVi58dcpYSg6fTmL-RaKHEiyhtYds74KIrBpJznBOHoW2aKoR3WFDak2oAetT_I33QUIecKDo3gek7Iyc_N0t42tF-q0Q1kQE8smSr_7OIIJviy3_3sxbGQVc_cSfPhIB1Aj25SQcZhG_UEShB5utZDPmry3C04C6YuS3_eqnfO3Lp-iCXL0IsvKyb1i_KTCS3_qqKZjBnE6qFbR1Wd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پیمان حدادی مدیرعامل باشگاه پرسپولیس برای انجام مذاکرات نهایی و عقد قرارداد با دراگان اسکوچیچ  راهی ترکیه شده. به احتمال 99 درصد اسکوچیچ سرمربی فصل پیش‌رو سرخ‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23937" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23936">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e541eb115f.mp4?token=kNl8VyPU7FVjGngmcW-wtA40dSCAiVhLdUg9uzJyN6W7KPeDMqwyK4zX7rrep1ITz1gYFcuf22bkZLFcp2Y94-ZHwAfyRs35O2_bEQjadUNjRaSUWyMdni9_fCbfVK7-GkLkQJHvvDaR318rDyJYE_gRoFwUSdO-oMMWB7BDWrmcYUN7OhZpRDMhleHt49KLX3fN_8ghx0_q3YWseViDyorN6DTydx2pUwJWF2KIlcsleOYwoV80K5ivJrHvEtVoNdUsYrKNjN1SasFVfpt7a3GFgQnDSO0aJXGzjoZtuApsWkybCpLxHCs8rvH__ZTmvA2b8Nchoopr06m40jqd65LfOGvTs2p7QwMfTdrt3UYE0q4bK3ALtIa5BZT_nvBZF7v8wrs6CFv4gv1cDZqPeRP7XJedwKgLJdMjGDMaq6MXxi6z_bbw1QJ-V9nVy_DuLgIK3rTdJbRkRvi8GK79EGFwbSXmRPV7beYeB6BrpeVvBxW6NZS8PfS_cNoGnTz4Qswb7PPYpFhFHVhusFl2rvW_A6DVb22hNKnmIxINb2YIjdL_En38kOD_pegNqTvImobkeuN4kPn2rOUy31kba8RlGI8fuA-q2GK55aMl4wq7YNg5JJDZhQsdX-1qIGPl266-_hEbho1E4DC9sIfXwZQpdwOpYqX02ha-Ev9YVis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های فیروز کریمی سرمربی سابق پاس و آبی‌ها درباره‌ اون‌ویدیو معروفی‌که ازش بیرون اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/23936" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23935">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXir4Tdg84lYWO-8hVC528Q3DoVrOTNo3_tIHFgHLDCP0UkOBft6VklnuqzflM5BrTjvjNGImd9E1S5sQL7vz1aLYbxh3_ouo2NtXG2X1UZOKkH4hHhmSVMhO9HgAGkHcqfx_ik2J-uQzrcBcrddN5QSdxGBmSGdP2eDkTTcKvovDYyfRjC9Pj_viNEFO3fc7PiCRvZXsmOFM1Ym4-WicJDSr7WFKpgNF93ZTp2vMjEQzexMpZl8KIZK788elAs76vMPMrZP_8ipONI_N5OBlJJq7MW_W4801pzfHhS51n_-X44oGO0Tx00Eh9SAO4mSdkBG9Sx02M_wiBsP0lnAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/23935" target="_blank">📅 23:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23934">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
هفته‌دوم جام‌جهانی 2026؛ پیروزی ارزشمند و پرگل لاله‌های‌نارنجی مقابل یاران گیوکرش در سوئد.
🇳🇱
هلند
5️⃣
-
1️⃣
سوئد
🇸🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/23934" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23933">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJAftfsek8qyM61wD4YEVG_0traQYCQ46Qo_1A3qZfV7Q6W1vNoxtjUmeMt60Cz5G1zouR5RE5vh1NDv4Y5oi5ht8aPGY4mIaQpAh-QWpS_LIY79qYztvm1xAOfi0_hvYuDqhvAsZcrbljbXLQRknfUdWKItaBehmUQIwsjjyvSrASBIlCFC0dWDseEnX5KTtP0FMkUT1iQIEKM6OxbncQXOZNuLB9CNjS1PZtkZ2Q-i56YcGt3D22TGPVshLErauHA68kURCHGyiyMVq1Ur9U98veCWK92XUEgfyaRa7TdA1dsIp1MCLzucvxGpjUCz4AG3I1iCH2ytcRJnt3tDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/23933" target="_blank">📅 22:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23931">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ad4RxPTvFipaYEvPZrQBkbnFQIwJxPyB9SRipN1iJz_T4iuroQCxW0xhEh6SjcKfoc0l9FCTGLEracaaoce9rAfaCn3pYk6SRoPQwIYSCtZswfDO_C8KOIfd10xh8szGLivCM1uPmLc5fF00-RTc0JWbz69dGUZ-GR8W_OIh7gY3QM5dh9ff7hywnYfCU5FMEt37ZEQdKjWawhfnTpzT4hkb7GiLsEzvZp1sXItKwk7pc-NnrFZ49lvdQO4ShkAowtxHnJ5YuZOR4TXSGazS_EAOKbFpDFK-OzYSKGKDktLxnLjulapXp6orzw_NiYwKJ9gJzdF4g1nrrj6N3ehAjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fR1cHDxyRN5vojxhZxQ4HKSha4k3A5OJMZ6lbj9X0nvClup96LAZYz9sDc4rkf-EWwXiAnRhttbeyljNMIHHb-3fg152wP5WAw0HAls9vEKZ-hX0hUFg9Ke600bKzUkaQPPJ1O1KV8MpVmct_WbOhkj5FBvWLfoFQ50cWJh97tr-kYzcGf70D2_3b06s4aEZOE72513R04Bq_gpiwBbNk8MNGKb27PNBReS4TwOOHKOMd0NjlIVhckOlY7iwM93cBVzJu7rBLg_zg-iYGUQ9dS_bdYy9GFrlnAS2lmCkp5HGt0NDObyUcBHm0kSnN4OFZ5fJexRHOcvNrbS3hPtlIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026
؛ شماتیک ترکیب دو تیم آلمان
🆚
ساحل عاج؛ ساعت 23:30 از شبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/23931" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23930">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKWJGzB8F_Llkta3fIVYsEMWG5iodbDW7gnn4-dqN6su_CkqG0TZNpYn6pyzbC8Tm4ktcwJD4Y3B88qcs-N-Xv7a-KOdB6iU6F2QzLSa-D-bjkfqYMubk-zOCA-o-NZn6ASGnz_NfZL7gfq9l0MsktZERyTVZkOWp7g2aaT5pXTHsi_63EBN2So97ud4DYihbr8dAhMv_3EhL2K611_Y3SJXa8pZIorQ7ZrMXR-IiGcsQUDzgjZumLzQhFuDbuDWEW9NZoqSzUHZygVtXf4JvXw3P34Nw08bC4TE_8zAqa2J_3Zt1RiT7TXYFBxXc0sTfWXqzuRk-zl3wf_ogCGotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/23930" target="_blank">📅 22:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23929">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3537466720.mp4?token=RwMlJW529uUSV29n_UE3rtfKE9xvstd_bCDQw2js3Iu15TlJhPB5Ut98hl9FIugkTU6iZt6k9T-XEfoSomKku1nozq2gbFxx8cCbcGLhTjPtThE_iE6wI020Gu_VqHMSnH-sgq5RIfRqL2z7nI3T06lyqzQgbNOY_dTMDfYMKC2cT0pfNiOnX64VIBxfrh0nTveEwpotfknzVyEeE5bDjeiS42py2Fok0yXZlLutS20Vaf73Sda_oBpVPCc5vHJoYSeLXzjnkMxFaOrORdl_PVw07DrC-qDv3unQrfhgHXApaxnpdADJx8w1x3v4KiNE1Z7PG4urn7RQhWXB_ZrvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3537466720.mp4?token=RwMlJW529uUSV29n_UE3rtfKE9xvstd_bCDQw2js3Iu15TlJhPB5Ut98hl9FIugkTU6iZt6k9T-XEfoSomKku1nozq2gbFxx8cCbcGLhTjPtThE_iE6wI020Gu_VqHMSnH-sgq5RIfRqL2z7nI3T06lyqzQgbNOY_dTMDfYMKC2cT0pfNiOnX64VIBxfrh0nTveEwpotfknzVyEeE5bDjeiS42py2Fok0yXZlLutS20Vaf73Sda_oBpVPCc5vHJoYSeLXzjnkMxFaOrORdl_PVw07DrC-qDv3unQrfhgHXApaxnpdADJx8w1x3v4KiNE1Z7PG4urn7RQhWXB_ZrvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سعید دقیقی امشب‌ مهمون‌برنامه عادل بود بنده خدا داشت‌راجب‌برادراش‌میگفت‌عادل برگشته میگه خودتم سفید مفیدی؛ عالی بود ببینید
😂
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/23929" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23928">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/463a3196cd.mp4?token=KlLnSxhFuI0nXmmUCnlF2jdGcBmG99UthOkaGQ6GcK6SZA7vcEOMmHas0lUxDNMp1-C9xUa3d5196oBZthJQ26JOsKAiD3V0WVHL5j0Sw3gqAjpq0VGwK69EIXhi1MqHirPEvyXDs74fHT7aLCz9qUmEWGXGPDgqjrdwyQIP343Sa14YQfuZBLMGyDmLeZhbBRfe9ZiPQWOLxjo9Zz1eMXs9jrEGVFec-IAodUONJYlzyhJyuD22V_9wLMsbh-ZJXWrS_4O6nZPlbOI8UALhhyh1ZcO2Z93MPq4xELCu-WRdI7PMa9Vy2xhjP7WVtjbh-N2H9ekK3DJTSWLPDrLf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش از گفتگو دیشب عادل و اوسمار ویرا تامل برانگیزه؛ زندگی‌سخت و تلخ اوسمار در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/23928" target="_blank">📅 21:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23927">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇳🇴
هوادارای‌نروژ وتشویق‌وایکینگی‌شون‌کف آمریکا؛ چه عشق و حالی‌میکنن، چه تابستونی رو میگذرونن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/23927" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23926">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh5qfau8cfehzgHe2oaFZo--wdq2UZZsH2nGUYHd8jetvCyjgh8QR5L7iQ9znCnqVi7CyTliwO2DHMR1grYzon3tP85fUaa7rLe-cdLUhkdmVOMUdkURr8gUQkeNHu8D40mT7cYzywHZknAyfCC_bNmjflz6Z7_yzHjBG4Xd3W5nhNQDeINXpYxpGG-839mfcFlGJrdthFYtfG3DhWTLCJcyQ4u0yxhMT3T7j7mhscCslgtM8rrvpYer4o036Dqvq9Lo5a3-DlkgaaDJjs1TKjRaZuMpl__l6J31ucZpreZHIJjdQHv8q4oH3wsc7hDny0S84a2AAkfaMgMxupnJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛دقایقی‌قبل با یکی ازمسئولان‌باشگاه‌پرسپولیس ارتباط گرفتیم که ایشان اعلام‌ کرد بزودی قرارداد اوسمار ویرا با باشگاه فسخ خواهد شد و او فصل بعد درپرسپولیس نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/23926" target="_blank">📅 21:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23925">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwavZm3Xtqk8Rn37bM7I5G-6Zi5fESNHB8k1dDUYKoh0PRU2btbserOeojxLff59mG95pPV-N00jPUeGZW9zX10Gqmlp791w-7wSjD3t6Vpc80ojHfDpJX2VdRGc9bOPchrQ3APybJlrQ59uRKuzsg1b_sS5Blh3vn2up797M11pBpn0FdRucYhYwkCxXszHG67ZGNylkZS65CAEPDW-sqL0CMzYFVSQot31KxZCVWyBuJIae_2X6vtkt8FJ2KjTcbI5ui48IvxoeqeKuz1utxYRyn11yIxp1THKEU2YjnCW9c4EkVo_prlPUFvg5qJSgF60zJ9R0f5dxLETyjRITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇹🇷
تیم‌ملی فوتبال ترکیه با ترکیب 300 میلیون یورویی و لژیونرای مطرح بادوباخت بدون گل مقابل استرالیا و پاراگوئه از جام جهانی 2026 حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23925" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23924">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
محمدجواد حسین‌نژاد ستاره سابق سپاهان: من خیلی میتونستم به‌تیم‌ملی کمک کنم و خیلی ناراحتم که در جام جهانی حضور ندارم.از لیگ ایران پیشنهاد دارم و احتمالا برای فصل پیش رو برگردم ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23924" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23923">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1Qq5b2cAIlS3Fm3xsoUxrK-FLlJnr17ns5J7csDipGP3boV3Pfy8vSqoG29E2jKy8gY0xHTV3GAH2C06Pw7F5k8ZE_0KrkzUB-guQBoQHI52isrQf8XmAaUaZhKeNs-fMkENFE-4cyKvUaodAOJm8ba_cwJi_esfBjDZk2VzxK2QjkmzgS02ghXNVIJmzNHJUyrO6voM9nJ58Ip5FJKcw3Hcd459r06jhzTy1JQ2chfeLvrp7cA_28d6c-zdZzPwUjuR2psy5UXsuDYZ8EnJ7ouldD8rRpj0fFvxfFuTB73HtIzleCuPFTU7wuy1lBRdILd3hApuFSpvJsN5D6Dxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23923" target="_blank">📅 20:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gX9SHj23mJRUZLTZeojjx9OFQf5cNDMUBRsGe5X9H2uKbHqYahmHytoUCXUgOkqWSoxEH7zRTmv7DTORJqzR42EUnb04D8hySOiidIBB3CV_Hm7lgMPWebtKkkPbhyEKPt-2Nz_mlBfCNAbjyxfFL1NiVO3PNqRJbjO8nm0oBqqC65qWHpS_VmZ81aBjmpEl_AjHZ49r-ALpPx5frSkAZz9mviV_xnMnOnDJYPzMFx9Ya_KKW-lvkjd7iB0C79suDU4RIQxERRhNdafZ4TWB9YJ1CndwGSBHIqZ4sVxq3tCcjncW5mOYWrB1r35zOo26mJqzffDY5Ge_ipegs7FTuto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gX9SHj23mJRUZLTZeojjx9OFQf5cNDMUBRsGe5X9H2uKbHqYahmHytoUCXUgOkqWSoxEH7zRTmv7DTORJqzR42EUnb04D8hySOiidIBB3CV_Hm7lgMPWebtKkkPbhyEKPt-2Nz_mlBfCNAbjyxfFL1NiVO3PNqRJbjO8nm0oBqqC65qWHpS_VmZ81aBjmpEl_AjHZ49r-ALpPx5frSkAZz9mviV_xnMnOnDJYPzMFx9Ya_KKW-lvkjd7iB0C79suDU4RIQxERRhNdafZ4TWB9YJ1CndwGSBHIqZ4sVxq3tCcjncW5mOYWrB1r35zOo26mJqzffDY5Ge_ipegs7FTuto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
‏یسری‌از آمریکایی‌هاازهمچین‌جایی‌شاهد گل دوم تیمشون مقابل استرالیا درهفته‌دوم‌جام جهانی بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23922" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUopnUl1RvUT3_oKEzlaxwLG35tbLU_crEB8LIZg9zFeNz7HHjJQ1ke-MjS2Cb644-qUz4gn9j0vqvJDi7GTb2uKNQbDMk0mrnunzbnkpxc7uXPSD20LzXftk5E2TXejIFdVD8zz7Kxh99qPL_DWcUXWkiWXqh_k3jHeZv6KyV_M-x_A404Rmtu47POz5FDtndghou7NW2kj7Bds4OULzIYln8NL0o_UVv1X6Yo7JbCYP9jeM8pdPX6mYhxMA-g0abSWQyU6T5e_nABb20twh9g9k6PtxZjEpNMun-iF5qCuxrTcI3uJHa_YAwcxtzjbUOTXmN8wQl5b0egLJudRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟢
طبق شنیده‌های رسانه پرشیانا؛
سید مهدی رحمتی در روزهای اخیر مذاکراتی با مدیران باشگاه پیکان و ذوب آهن داشته و احتمال اینکه با یکی از این‌دو باشگاه قرارداد امضا کنه بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23921" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr_0fC5TXdCEZEvb_dJXn-HxMrjz1SFJNQiKc7uULzUSE90wLSqVI0IJjhc8Fg25hltLkOWpED_euaSC1azAkpef0JaToNvQKvJdMEwiFSdpbfCibccO24ZqNN2niDsvJHJTNjgK0X0eA-6kgRSImW9nxF9X65M98Juv7LSGSqD0uyo55TMt7SECvUKu0Mv2Bya-ugXZbvfBKe5OjwORyLSWq2s9JCL2s9MiLCyygF-w8EQvUeMfMQ3Y9FZ3NKIvWuurS_9OYFh0y5EEx7yzRGXbXmp1gSDHJL0RXnenhGwzOZA9l1FxPQg5Ks1SlCrqfcDHSFqoQ7u4xvSu9Cp2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHO-KiOm5DwLnzQsY2x-8UGlEGZppSa_idpueb4OFkn8_Yp2mm2v69pX9W0hZK5MaIJdShBMI5d_QgmAG4MCAVzpverge31n4BbZo6_GVPySJ4J3NeD5U2rLhNh78eySkrF-7eOsHdnD195fG77pKEq7e4H5COR687o0bNDuQOg6Lxk4MUtdPm0381KfGaUX776YcnEMicXyPr5GXgJ43nHJuCIqFarYAxLRy3lnDg2SotpOxY2GrTHwKXCGctjWTluay7_VCDAyJck82ULWtVwZtPGhPS59LE5Z0ZJIGLOu2-ggs4HeOb4fHHNaVM6z-aNlm0y0I6Ni2lYVXLAR_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23919" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413165ef88.mp4?token=fhNyB-KgMUYobCvtlzBtUU6G3jWCX_SEvFLsGuVNKYLLbd_Fj9WDs78FwNX0Qa5rcqPDFZJQEzZjy7KimsDcNt4vu_MEr_SWikvztScbwNJ3Vf4cbi_0paq6SxhJxejH-0dGa_AxqP9GsYOwoZD_cjRJXZlLUPF-iYRPmHwsH1Txa-EifK_hyrjq92JhwI4BAKatkXtG6hVH8DBk6wrZ5LbEJJDCv0m2A47F8syvwcT5CBKvmljjzDLqvp7RqNriX3lEvQZXRj3xfrI8JxsZcjuT6IgHqaOC1OEhy1a-DWRpjzGZU9HvTT9dxCnZ81zfCcufFvddU9EMTExxHV0kQqE7TQPwIIx-wq3HoDnYwPxb0GyuBKeEZ3zM1z1ZtXEfRfVivTDeBcZpa2H5LrYijRC0wZD83ITCnJbrczgHFST-j9KrqVf26lBSYihWgN33ZMK2w-eIejcRdn2UUlhNwFZkxHx1xyrGXp7QImNjHxn92KB7v2oO23MO9KKLocZ_YQK4SMUbZi0wqlH451TsWg3R8MYeZWU5-HWHwpwpB48Ygb2b00Pr3qXqqeU5dQ9hG5WJ3-6bwgxMl8pENPOBfwvG0WaDSL_jULKA6hf2SBfNYEBfzXs5V1UB0N1hWuaeG7F0PgrzfO4yxAEFJcmwaICS8MQCHVFdyqrM-hokZP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413165ef88.mp4?token=fhNyB-KgMUYobCvtlzBtUU6G3jWCX_SEvFLsGuVNKYLLbd_Fj9WDs78FwNX0Qa5rcqPDFZJQEzZjy7KimsDcNt4vu_MEr_SWikvztScbwNJ3Vf4cbi_0paq6SxhJxejH-0dGa_AxqP9GsYOwoZD_cjRJXZlLUPF-iYRPmHwsH1Txa-EifK_hyrjq92JhwI4BAKatkXtG6hVH8DBk6wrZ5LbEJJDCv0m2A47F8syvwcT5CBKvmljjzDLqvp7RqNriX3lEvQZXRj3xfrI8JxsZcjuT6IgHqaOC1OEhy1a-DWRpjzGZU9HvTT9dxCnZ81zfCcufFvddU9EMTExxHV0kQqE7TQPwIIx-wq3HoDnYwPxb0GyuBKeEZ3zM1z1ZtXEfRfVivTDeBcZpa2H5LrYijRC0wZD83ITCnJbrczgHFST-j9KrqVf26lBSYihWgN33ZMK2w-eIejcRdn2UUlhNwFZkxHx1xyrGXp7QImNjHxn92KB7v2oO23MO9KKLocZ_YQK4SMUbZi0wqlH451TsWg3R8MYeZWU5-HWHwpwpB48Ygb2b00Pr3qXqqeU5dQ9hG5WJ3-6bwgxMl8pENPOBfwvG0WaDSL_jULKA6hf2SBfNYEBfzXs5V1UB0N1hWuaeG7F0PgrzfO4yxAEFJcmwaICS8MQCHVFdyqrM-hokZP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی کنیم از این صحبت‌های علی دایی عزیز اسطوره مردم ایران درباره رونالدو اسطوره جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23918" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23917">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7b4hWZxC2w3fSqL147NDxVy3SlY6LwqV4GwzrhQVn0dK2k5XZUk6vpIDiEMBV-hk_Cwu4HNvvhFYg1LdKJwQ0hkSjU2j3yDXgTXTgY4gCXA-Ra9eKGPxD917Vgyiap6nYdMDYZVKy0fzL-fvctDwsOSIfgAjOm_dNg4e4JJD372Sp7zkiB4xtlX1ua-RiDxwnda12kU0jr6amd0_LpBYv2lOXSWjNjC_adD4Ls6i8knXc9OZxQWCUEGuWK9DEnLhRk7PbGMofklWPjjH90db6KRlk6TZvxMx_AszHkJzgfGFoeO7Jw7e2XYeOsZ70YV9EkY-KlCtBXkx_mdUr2ycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیاز جمع‌کنید و برای‌سهمی‌از جایزه بزرگ ۲.۵
#میلیارد
تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود eg30:
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23917" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQzpxksQS0H64lv1hJnvbkfaoEnYeJmKU8A9LpTdU0P9c5els1mKpow7VXrdbOJiqHeaAgfpWw8D7qBenzwSS5Osr-eBrR-0w5wIYrGaElj5h9xHwFYs43qxWPYqS9S3lNPS6paR0nnVv_wG9WnZCXV3X5JXBk4tHssyBmsa3-dKBrZHo_j7WNP0TCoUAuICPElOu88ulXgKJSTC81m-0-F5r1c0OuEHgrRglU2fXKnd7klZNAA1ooAOl3b8qqfgZE4aFvERu7_VeIPGzWvKIY6IyqLyh3PXTQx9eSFRHEiIoURA5H-ptKRNy8rnMdBm_DjKLzQx-sRl6303uW4DXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک: تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23916" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQnjuLbspeIMTdQG5d1QWiqVPPuw5SxPVEeWU4nk_g6qI8P0v-jp752Pi23LZDg-98oUxBD4CzpNnQR1sk0OWO_9cmvuZ7bzLef6ORbC0aih0eE33GrYEe1hdIIFESVxAiTPJIKH2zzH7Ls7UO72KkPrs2F0IE6vbXDxP7_b8j0h1pvT-PwBt4mYNWLvXYLU6mcagb0CfOF1BIt-HRLZIcrnQcTcrubMng-6lRXXeJGrsKmCgwULmoxHgBgWWxe2NJ_E7nCfPovg0Z8arTaafCiKAvscIYmlBDTtCpG-ziZF3rXgpglB3KT75jXcuiC-hSIJ0liT5qrBJuNzTup75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
‼️
سایت‌اپتابراساس۱۰۰۰۰شبیه‌سازی‌نتیجه‌بازی ایران - بلژیک را پیش‌بینی‌کرده که درآن شانس برد شاگردان قلعه نویی ۱۵.۱ درصد است.  در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23915" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=u_JlP75LTtaTqPAzFdRSgWvVjhJYxO1vFyXGqzqDOGHrIwHvx7HnhxtEDUC91HkIeFwx1vNN1orb6oLDNwiLFq-dkAU4KyGSsC_IY-aXkKa2v1E30Zbcx4dPMsYqsAa8dVIg2GOZ1qBgvAqq-2BQCfTOu5r24ptNAS7j1ypbcXozupEOyJ7dtpJLozHJ9wUf3201-bmN7VfpKY9vV84E-mOxDWJ2FtCFZ-5pbBh_lqZv6s1uch9kuxRp2Gfx3S8KWQwOA7zJGMz8YQ6zuILrPADZaQxGlsIV43KrbAGOnpHWmemho5j551BqyC0N4tb3LMzfANgM44ZnAChG8SG4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=u_JlP75LTtaTqPAzFdRSgWvVjhJYxO1vFyXGqzqDOGHrIwHvx7HnhxtEDUC91HkIeFwx1vNN1orb6oLDNwiLFq-dkAU4KyGSsC_IY-aXkKa2v1E30Zbcx4dPMsYqsAa8dVIg2GOZ1qBgvAqq-2BQCfTOu5r24ptNAS7j1ypbcXozupEOyJ7dtpJLozHJ9wUf3201-bmN7VfpKY9vV84E-mOxDWJ2FtCFZ-5pbBh_lqZv6s1uch9kuxRp2Gfx3S8KWQwOA7zJGMz8YQ6zuILrPADZaQxGlsIV43KrbAGOnpHWmemho5j551BqyC0N4tb3LMzfANgM44ZnAChG8SG4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخراج‌المیرون‌ بخاطرتوهین به ترک‌ها:
آلمیرون بازیکن پاراگوئه به‌دلیل توهین‌قومی به بازیکن ترکیه اخراج شد! تو قانون‌ جدید اگر دست‌جلوی‌دهان بیاد و مشکل پیش‌بیاد بازیکن اخراج خواهد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23913" target="_blank">📅 16:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=cYL0vGmonC4xJ3_W1LPEON54YbkZ3sxntXMb1cpcfTJV-cOAZh-_I7-mACEZU_wqLv6jQ4pbU2isiALtN8NWSyA2W3grlNn9H3FkEUagzl4wVPKTQHe-omcmwjK2PywS9waDTsA9OdbL7gqZW-SfyIrIFI0zDYuUPS_wbXgswXKJqTE_9NbKliIS7Vbcmkshkc8JZZNFwvudX4oGpSqnUrAYVu0y6-LfTamnxBzCe8EsR2WjeApmjUq0hVku-x30EGr2j5CJ4RBagWn6_gRwiGjDseQq8iX5gj0kmD7OR9QOpMKcWtXMOWDkB0CvlPedO6cR6IFwQ_Qg1hFgU1FYqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=cYL0vGmonC4xJ3_W1LPEON54YbkZ3sxntXMb1cpcfTJV-cOAZh-_I7-mACEZU_wqLv6jQ4pbU2isiALtN8NWSyA2W3grlNn9H3FkEUagzl4wVPKTQHe-omcmwjK2PywS9waDTsA9OdbL7gqZW-SfyIrIFI0zDYuUPS_wbXgswXKJqTE_9NbKliIS7Vbcmkshkc8JZZNFwvudX4oGpSqnUrAYVu0y6-LfTamnxBzCe8EsR2WjeApmjUq0hVku-x30EGr2j5CJ4RBagWn6_gRwiGjDseQq8iX5gj0kmD7OR9QOpMKcWtXMOWDkB0CvlPedO6cR6IFwQ_Qg1hFgU1FYqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گرفتگی یهویی عضلات پای عادل در ویژه برنامه پریشب جام جهانی؛ سه تایی غش کردند از خنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23912" target="_blank">📅 16:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsV_DEs6mJATN-XRnGnkUj-qTWd9mxfv4D-RZz6Dl5UolhoORP83GNR4xCK7DKr6XFOA7OQNR14MaqEaPLeaYe0Wnvxb5ms67TZlWI4eBY0xpVmiRB8YESq9MIyLwI1nhmqGt3NqbC2sX6eMlx3wBgD4xbKU14gXPcwqzkHiiQsZ5v0nKzs5w9WkqpqhHs3MgSsYbAgIu1G52mD9eyNzbXAIERS_OYCtweqV6XEk4TuKqPJ-yghVYn_alNv9lZdnBLpz1hrPlf3rxasmFkuj_iuAJ4Kt7ngAB2ITSXNeAnUKR4wLyyTizub13QmkT8HAeSQSUky2pkvb3X7NbbwsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23911" target="_blank">📅 15:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLxa4iEGD08MZPvyIW98AKsA7bAO9NScgtjuTb6WK4XWV6I42vrCzw9hpmb8b35Upy8OWCoCfUv23fLj2oRboLtq6NdgRWi1YB5AxWrEU2mGTcgYp6WVtKlLLaqXKUnXOtVjKdBQ2EfG3TqT1ryMt1JtMV48IyUJtiIQhvyuMLsBFz6lWHUe_AHwtI3OmnYIIo4XVJyQGoNDD41a0ocz0kKQ38qpJDJe60leLKjHuOEJREXVjAOdDVTmiZgnRijO1bMmLYI5_SvVV45rwo1g05KIw5BxVuX6vswsetcrlTlzpWQv_rHtrKEFQK5CeF8U1vkGv2-zELPzD93qW_stIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23910" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=AFavA2eFhHTqiZsWd8Iqy8Nzkdx3QDy2Syn9UNgnC45AMA04aW_w1eRRGp7si-HPTPiQAlPe_oP2e9EwzM4y6fb9lHYZn7wmGaM3RTc7nCNIvw9EGPsDpQ5mZLD-Vaa2_g7MJhHfWJKSkN7Nqsgp3M2X-2Lu1HSJ9dt1rOLYvYjWM6-vPQcE3Hu3mdZ4sK0cmMrVKiD58KYmFRs8BPHajyIMriVvdwYslLGJMv8gI4qV4ot0jm5SIME9wC4pkz03TBg3E9_iLjvTw9VzmMS2n3x2vGVhARhCUSsTtLWm_o0zG2fZ5-F7uTbbjGGfpSErzlRF4d--WuDj0d6bOngoRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=AFavA2eFhHTqiZsWd8Iqy8Nzkdx3QDy2Syn9UNgnC45AMA04aW_w1eRRGp7si-HPTPiQAlPe_oP2e9EwzM4y6fb9lHYZn7wmGaM3RTc7nCNIvw9EGPsDpQ5mZLD-Vaa2_g7MJhHfWJKSkN7Nqsgp3M2X-2Lu1HSJ9dt1rOLYvYjWM6-vPQcE3Hu3mdZ4sK0cmMrVKiD58KYmFRs8BPHajyIMriVvdwYslLGJMv8gI4qV4ot0jm5SIME9wC4pkz03TBg3E9_iLjvTw9VzmMS2n3x2vGVhARhCUSsTtLWm_o0zG2fZ5-F7uTbbjGGfpSErzlRF4d--WuDj0d6bOngoRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ لحظه ماچ کردن خبرنگار کره‌ای توسط یه‌خبرنگارمکزیکی؛ حالا خبرنگاره اگه ایرانی میبود تا از خانومه لب نمیگرفت ول نمیکرد! این خجالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23908" target="_blank">📅 15:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYZHF2v5D_k8QlClRyfCy2dyx_2Gx_xeQnbBrDW6Pnp4WqAe9SW0UlpOrbahwrKknMsjYclaII7c-54wv6kAy6CmCZuYl4V2JwMncPkVds59LqmaxWohRbwiLtVkjn0wOlxa8shh2NajY9P0Qy9oH9yqQSJ7dAUwH9D4fiIN8BjozlnrAJRfSpXRtj4WfU3c29YY5avPiGL8k08H66rk0yWr_hDikSFz4zsDXymyGHcB_fi2Ij4mljuk70jJjvv7JwdGBzSQ7Pe-cZfQQnGDhNu6uyL73daHsemwDkaE9M54xWeQmp8uLHLNMH-aJ5PuAAmJ3uLdl9aUNji-ssTyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23907" target="_blank">📅 15:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkHypx4JSvY3Hthpy4QbOPSSndWJWv7PLjbujmmufyX5QP8Ie-EooIJuqFpO7l4PHWgdU-gzVUTbu_zcxaqSoOh9MCMmHI5HeD-ZAEJRmz7O6yXCYK06DQovS1rBxqLVPgDoX3ruKMRXNEiyTAALRBvCUdx2r42DhmWs6j7vO06JhhDjLK7dIFUQaKDB37lMPj9RH4Xs8eXAP9M_qGq9Zmdf6sY5pywasG5flGdUXnN5qaAcBo0zNAIsEYxzXEfSCMCodYVpk6jVl6MEOA7dKaH1WSS4BPnEgyKHE_PvjzqKirVCQe8wINRYXO9ss4lfPWb3WCislip_MIngKPzj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23906" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl--t_ujsnkzdg2QumfNs6wFJDwLZ_I5wT8BNfzmIwHWwCLEUYlUBNw8OFJHY9de6d0Al0I5zEa5VqcnKVDioUfqaQ34_wDpeDsQEiEGUusk76Gju4Kd5MHbwXIj4HJADN6eb68ym_te_7xlxE8f4cVHx64s1J0QGG2SbQkhBovouPe8-558bcaMQJvo5v1UnNil2zKKgpUsinvdaRaxhKWKPAK3VQ9zF_E2uVMDBijUtfA7EdQEeP0EzxIfhOvpdFypdf5gIqCszWQqhh-wRjeH61z8eaxrTLbadk3f9h8qhjLxDIWbNc-XanspDymYpSCb0Ae0TxQgYemiAZq0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاسمیرو ستاره‌خط‌هافبک تیم‌ملی برزیل و سابق رئال‌مادرید و منچستریونایتد برای‌عقد قرار دادی دو ساله با باشگاه اینترمیامی به توافق نهایی رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23905" target="_blank">📅 15:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4fNl0pwje9QdvmgVRKDF4bSfCM4RUkKF9SoKj2ki-zzhh230vjNL8Cce5uBSFEev5l5YtQRoFgXjD2hjA8muMb7wxvLRWDx6tvPX4fUz7AvHDKZ9F_O-jdyjLy-dVpnZMs2k-uqfKvFCXuiykZwMOZXfoefwcbXndlCuQWN0gCr9LLicwuq2WnyAZh3YOAIKmFTc3BVBrorNTrdap0E7o5LgGbDYoqyyd1Ta6KsMWu9HbggvsWw1NWKSOjWurq3qrPiT0p3DhWVmCqYtc_0ibxysl7nje9-NDeHKyEDkat-Nacc8TGP7DZaG3eA61_F5cBjgGyNT9rpbvM0h1MixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویژه برنامه پیمان یوسفی برای جام جهانی بدلیل این که علی فتح الله زاده به میثاقی مجری سبکه سه تیکه انداخت متوقف شد و به او اعلام شده که دیگر حق ادامه تولید این برنامه رو نداره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23904" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=PJMvRNc6vBBqRXKCmxPmPgwQMtM4r8-hVw4DjANmC9a19GPThwOo28fXbtM-flAfPhIm7v_ukx9h8ufHfc5UZ7u2ahizdArJy8jRB4S072CMzSbXJkqSlnj5w9fWUugHNG5pC2NPFlHzo5z2joU0ig_8X2HR7_3LBcm4q5aOW_-hsdNzjm1HRpkGeVZcmoTWfSXFBp98fP94_EJFyyTSxDWuAW_NQycV-52nR6hHztZ__ZbRqupThniDRIvCbBoP2d79d9vL6Hf3PdAYK_Qb5_JovK7ieTspisS4PZDar3qBrSE_yGZuYRzi0dESS_NoocN3t7NPL0Mno88ibxPr9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=PJMvRNc6vBBqRXKCmxPmPgwQMtM4r8-hVw4DjANmC9a19GPThwOo28fXbtM-flAfPhIm7v_ukx9h8ufHfc5UZ7u2ahizdArJy8jRB4S072CMzSbXJkqSlnj5w9fWUugHNG5pC2NPFlHzo5z2joU0ig_8X2HR7_3LBcm4q5aOW_-hsdNzjm1HRpkGeVZcmoTWfSXFBp98fP94_EJFyyTSxDWuAW_NQycV-52nR6hHztZ__ZbRqupThniDRIvCbBoP2d79d9vL6Hf3PdAYK_Qb5_JovK7ieTspisS4PZDar3qBrSE_yGZuYRzi0dESS_NoocN3t7NPL0Mno88ibxPr9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور:
یه زمانی من و محرم خیلی بدمون ازهم میومد ولی الان من خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23903" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpSMPc5bqTLdb2BNvjXb8kn6nr7PxEX5A89vx03lPQE2AnXOpQxpwyEgw31jgs4n8owUdXXyNSzZCrmUR9pGNKkLvs76ES-vLZiNqZstCPemHCAI8-oDM2lFzSOlvD0BP78ui-dlecXNV15XuBdO9O_u3MxBPaYuY1mh7kL3ijG7cNIhjxKjtUAC_B54YfV0kPAgH8b1Yb_sN8ofRFhRoiCjKUBoBX2bPw11E3DVhd-tRPqUdkdTLYt0FMH8Wy7zbhkbRuK0eyu--hK43nMJ5v5zQvfb5kX7uxNv_TN8F9mnS5WVJ640wtww-Jr1KtzEfMOWOMT1h2T-0ltufCA7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23902" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzm1WrQrfP6RHpoGERwekZwgpHukWj-ZjhkHObUIchQiGh0m6ZOglCS2gZtvJymthRoKujHmjxVjzWljJg0Pggk4GoWgPIru-vlVGrJRQx48qT6mngYqWhAIP60hBKXRdjsZn1IdNa5PkJbSaYFgfSe7LZOETZ2rtTMfffsdOVbb8biz8z04GhuluOOsJB_EQ53ygBrsRDuiV9qP5cfj_dJrQUy3zNYck5zFtTjb46dcbZQKLY40R8UlPjim18wDrk877ovR_CRmlIobB8rQcG8e6Yp8CoVwW9S9OjyD-5ARFYvx_urBGm44NLcDLdXrPBon1NV3nVNJdvbZUHJ9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
عملکردشاهکار ارلینگ‌هالند در لیگ‌ها و تورنمنت‌ هایی که تا امروز بازی کرده: 279 بازی و 260 گل!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23901" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJPLDV1JdQJHZhfogcFaf2poSGYglFcpkj4SdoQBsGYZOCw17Qh16vTPwbFV4p2wRitULCINt5cEZcD91DwC5xJiQGBb1aKAdA79tJA84WoXObVtRqXhjGcI1SpXsvx_MSWFO0TyC8UKjxyQVNyrnloX8dHMdkCbRV094sV_MWdRIYKiHLfbzV_I0WNnLocVLZN-UJ0w3qXa7eHiV2_FKibDDJ8pEUwkrj36p80R60pTlW3yrbM9aKwbhZ_zOOR639mk9EOoaxxPy0tMaTMxXRG7XvrqbVWtr92kqEIxHuMKjR5qon3hZ3q0IiOjp2URcvq81WEOPQfxS7YYLQ_ZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuabUtGAQk117PZ94MGcVua33YwJLdY_ENPs8biQt2JLZx4OYoq7nDzsHAP9hzyBxRZubxd4jAskKOD1TeidEVu5iue9AUqkLg6CPl4nzGO5zpBApiw5SrBU_x-eIW9b8keB79ZsJbBKRfp9DslGCHsuL4gOx27fOT-5kG_xChUrmwPVepPc_UwjjWRLXDyVFyscxS-SpnXZX6TsKQXfjRxZzqBnuJ1_OUplyE7umMNwtXyWo1gnCqO4i7NuGR_qWxlEoandwHKLnaHz9GUBeIuzdrlKmXUZ6RcOrDeL0IPi9yQdQX31gnz_EpSUxOdFRJeM3ngVxSack8b6KccjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=fxVA4AzG6CVVOUiIm6pr_Xde_-ZJKkJY5CP1eSAbwnxqxb3aze9PbnZPS_7vI2siDfwA_jGgMZp5X7nAdsVWj_xHij5XLt6_Z_pAFlD8lDGzq519ek4jl23qK5z5Fses7WpynyMzQSPFVJMbcHoQhUlfaQXJjy6FPi19POU6MFi528UEtKBfFDXbqRZXB0FNz-YO4wyhQktP8hRzr7AMfei2kSJBZgh9OB33nKdYhH3-i43LX42WvrbLsY9UpK936WEoRVufHQuWljdrmqw1bzGZGIJjvPOgSDOfELDAeMVFHEJEkilW5ybnijxI1UGWdyzXWdT0SE5Su7ou_ENC6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=fxVA4AzG6CVVOUiIm6pr_Xde_-ZJKkJY5CP1eSAbwnxqxb3aze9PbnZPS_7vI2siDfwA_jGgMZp5X7nAdsVWj_xHij5XLt6_Z_pAFlD8lDGzq519ek4jl23qK5z5Fses7WpynyMzQSPFVJMbcHoQhUlfaQXJjy6FPi19POU6MFi528UEtKBfFDXbqRZXB0FNz-YO4wyhQktP8hRzr7AMfei2kSJBZgh9OB33nKdYhH3-i43LX42WvrbLsY9UpK936WEoRVufHQuWljdrmqw1bzGZGIJjvPOgSDOfELDAeMVFHEJEkilW5ybnijxI1UGWdyzXWdT0SE5Su7ou_ENC6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=kc7DfVVeEAKVhzLOb1md41q617Udlw6EFpDv0050K9pX9jSAUHjKmegSEJH5LGCZEpj2fYl35IsT3jjJ1BoMWtYKeLhiswie6Oz0vfQdRT2KdWvAbAm6JrbTYoP_-5xfAwJ9yPWgBSnV8Ykm01sG9W5EuSw2EcEmFGBXVVtjjd3-LDF_Gg33fcztdRojmMWkwnKYugbZ0O4sM5KtMs57XyPtrWEcy4ZSiCgOY3C5fSILfwD8vncu7Q2_EFqx4auoVRs9J6I-hy3nokN0OU9NjFD3qXUSC6I1SPN57gLT6Cc9rhjgWnXPivkPFKn6WCUs3rK9FDGWYZN6DHjcxBEyoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=kc7DfVVeEAKVhzLOb1md41q617Udlw6EFpDv0050K9pX9jSAUHjKmegSEJH5LGCZEpj2fYl35IsT3jjJ1BoMWtYKeLhiswie6Oz0vfQdRT2KdWvAbAm6JrbTYoP_-5xfAwJ9yPWgBSnV8Ykm01sG9W5EuSw2EcEmFGBXVVtjjd3-LDF_Gg33fcztdRojmMWkwnKYugbZ0O4sM5KtMs57XyPtrWEcy4ZSiCgOY3C5fSILfwD8vncu7Q2_EFqx4auoVRs9J6I-hy3nokN0OU9NjFD3qXUSC6I1SPN57gLT6Cc9rhjgWnXPivkPFKn6WCUs3rK9FDGWYZN6DHjcxBEyoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی مهمون ویژه برنامه جام جهانی یه لحظه از دست جواد خیابانی عصبی شد پا شد زد تو سر خودش و نشست گفت من استعفا میدم.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc9m9S2Z_jI_BS9LJCpbqfWmEf7rCWgY-xC90NN3lg-FE9_GmrNz7qCKgUsfXfhPtxNnWlTu571bPBgHmz72hDKn8VrWyZcdp7xUY1ZHipt8PGIYeWswvZ-TPP9wlcLY3lwUky2ufshyXp-Dr63usIEmDg9a3GqUdzvOVDQMvHoQbE-1elZFOZPPW1GYaECAJJ9m7sIHXJcOhiOXpApEXkKg7SHeLz7-VP_LHMPjJiSjcfVma-8iNXkFvhb5dj_ZM2ItOYsy-5p6LwI1dkZUeuic1h0LzAKLnGi-ngwpVtVsF1jj9EtvGlNep6oVUZn886kXhZX_p7Ml6ZoDrOOlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb8-FOp4UhJ7gmKTwKDvGUdxqHwFRl95y9jRA3lpeFg3M-ksnjLxbAoWQlGFmiDQmQleAkbGEDCPyFLQHqFNJfGawalQ9FUDUwKn8C1DG8Kv0XWcIvPUae_mdqsfQwMuAWtHKELc4l-XJvKCosr7l6utLPzGcXvvyawkgWuULJgRYb3O5MlAgrnLK7TNEzk83m5uKGNVG_bm68Q_bXgPyuV0nkV9kKbPQXxb8mIkdNmiGU-7Gj74Y3TwWTdleCgvqDdqThu6opT2cAeq0DZEUpKNRyFgzl2wU9Kcfbmgb5gPQtVz3Nq5pJ6oQxxUiWZ5n8g65mcZjoXetJFqPKTeVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td3mXa_lEZXAiSPRnxVIlNMZrhxd_yHjMVT-mqGeFFcFc3y2rDRvE8c2oibZArCqTYsLS7oLl4K0ay_h7Pg2V24UxULz3SB_l5CFu8FZxwQK_lFxhq3iGsUysVHGpK1mPBiWbDfEPTbT1Yl3Ugx5P0WXQ4uUuYOCz2omPC2Y1XpXcrkRZh4EtKVgEjVW_S7BdDZGyP6Yhh5ZA-Aj8hNRqIDC62f-V4__67P0ykFookL76rca9Ldtegyua6IeSXmPEg9LxBqlRGT8NCW_mqhF7NUiclw4Y-XhiumqUQ8w1xuLZbIi4IS9xHFjgX1bVDiCFjRQoViYctIWnGi34T5eX0nE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td3mXa_lEZXAiSPRnxVIlNMZrhxd_yHjMVT-mqGeFFcFc3y2rDRvE8c2oibZArCqTYsLS7oLl4K0ay_h7Pg2V24UxULz3SB_l5CFu8FZxwQK_lFxhq3iGsUysVHGpK1mPBiWbDfEPTbT1Yl3Ugx5P0WXQ4uUuYOCz2omPC2Y1XpXcrkRZh4EtKVgEjVW_S7BdDZGyP6Yhh5ZA-Aj8hNRqIDC62f-V4__67P0ykFookL76rca9Ldtegyua6IeSXmPEg9LxBqlRGT8NCW_mqhF7NUiclw4Y-XhiumqUQ8w1xuLZbIi4IS9xHFjgX1bVDiCFjRQoViYctIWnGi34T5eX0nE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلچینی از صحبت‌های جواد خیابانی در گفتگو با امیر حسین قیاسی؛ مجری برنامه هنگ کرد قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqqLu7js0EJl-TcfT3kiPyzemML-50DAw9YFS56JCeF5EBQ-s-KCCKg2LRWR6PkaA7Y93FT42Ppqjtv2GN4nSTqkHxuTwCigPxd4Q_PIj3S8zYnMkgW12HWbBJel7ePFMbuK_QyKb3PMa_2RDNvW7EqrtA33XfWYpYNBe44EjPTSUdBWZK_SBMp1WeCN8Q2V_yenstMIXIMuAlfPT4SnJv0sS_qfneNz8PHVeGrriKtDINYFu6VYNLgC5luw_v3YSz92DWQRg-Bgrj_UnLamc4gPemK2i37TQ0RItkUWhvXBILbrzYktC1bhA7fYNiGiK38EpFtXk_kQKuFK9o3QOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICMSwf9RhVWGtUiYlrZIXIEKusIU8GpmHQBVxvdHkQYPT1z03qSFkHPomhzC7zGVPWIORtuC__IyM6VRoDosD2px9TYkxoan5ZiFIj8xsUQrXyJJE4KQ9_7CFoh9SaHhW6uN-_eMZzdvPc2vPutUKD6EHlVFXbLNz9AMku2ArstAEw4ckCplJmeZk8sXkIZpi5lDmd_96TRhS65LVS4PZ3km30w9eN5ZQzw7c4LaUAyvkOadELs5yzg3gg2OxLTOEAMStvBOKNIX0xlWtrQZfhS3ri1jf2wFE98bzkVLU2sqSb6eA9LmqwWA98NqeSezaBp-C8PLjRhwstejPi1S-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی پرشیانا؛ دراگان اسکوچیچ ظرف 72 ساااعت آینده به تهران خواهد آمد تا مذاکرات نهایی رو حضوری با مدیران باشگاه پرسپولیس داشته باشد. هیچ چیزی قطعی نشده. اوسمار 50 درصدشانس داره. اسکوم 50 درصد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23892" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=PXp6KEfAN6jxtlSmq8xOHb3G9gbc4owIeScNz6xpnZz1norsBXgpBBJEz7-_tAtRQTtD7arWqSNkmhGUikSUlqTTntTMpNy32qzNPg6PwHrMgkJQDtw8TOZvFQxJfgwj5LWYa2HIeA074CWFwX4iDyMQmUj9eUkmJ18RhJY75IrKMihOwxrKT6ynxPQtOqHFXeBAARKt-bZ7lmga34Wx9HDi2rGyduvm_Kzn6PIfFrqFXOOZwwHQGH8ptlt5LTsYXXRJ07spFhOUeNcyeoOy4f0zOS8iQZTTMjl3s8d-Zp95T6p0-XhEDVo1qQF5EwpKhA5hBsd1-qRuKAlVGZU9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=PXp6KEfAN6jxtlSmq8xOHb3G9gbc4owIeScNz6xpnZz1norsBXgpBBJEz7-_tAtRQTtD7arWqSNkmhGUikSUlqTTntTMpNy32qzNPg6PwHrMgkJQDtw8TOZvFQxJfgwj5LWYa2HIeA074CWFwX4iDyMQmUj9eUkmJ18RhJY75IrKMihOwxrKT6ynxPQtOqHFXeBAARKt-bZ7lmga34Wx9HDi2rGyduvm_Kzn6PIfFrqFXOOZwwHQGH8ptlt5LTsYXXRJ07spFhOUeNcyeoOy4f0zOS8iQZTTMjl3s8d-Zp95T6p0-XhEDVo1qQF5EwpKhA5hBsd1-qRuKAlVGZU9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5yap5SlvkosuRFiyD6vNBh18naYVg5lWxcuyMe2a-YMYgczFCtuDaK6oTOHRtdIukV09lwtW6YHocFrKj1zMojnDV-WjM-CuT1OK-Hfv7Efkg0LSR__RLRf_KZuT3k0cb278gslSZjpmnabN-1UDEpHRpjJR1G-aYhrnlphkkYEj5nZGyThtUVT5iSy-iFbKIkBLp5IIrIASc9zEASLXdE1AIlrF7S4Te8eb65uAf5XW2RopqzfxCNLS120b9dDlOd5dDzclmGCLDdQwx_YUVrrj9rR9dCNhp4ejX3NiEDFn2mdO27Q5C2h8ghspZsP8_nKK1yjNLxSG6OjlsEHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تماس‌تلفنی امیرحسین‌قیاسی با «سردار آزمون» وسط برنامه بفرماییدجام: من ایـرانی الاصل هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGraSaI-9Fcst90tlBJaTvqEfl5EUyvhzphcvR1QKQCDH6Xqg-FYM68BnMbEK-zhY93x2Qg4xFJFmNNzsY7vahoOzKZryibyY2XLTmMnNAiyPuRVTZEx9Z0_Ij7BSd61f_seH4IOXneExisd0G7ub4F3P4Po3tzNSquZflsGwT0qv9mZ9zxgHUkR18rbLWwmQJvbaNVA3KJ6MSbsoFgc63jnSSUPoqWCpQwt1Aphj8L_BuDur_TFND6k-ADSQktoO2zxPWbY7lZ1kugckFdKMZZrewlXrgFvgP8oNJTm9XTdwHa13DJV6dqpCh_gpN9Git5yhQanyAoK1LX1BA47jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=quBC_UIEFjCV7mQv_e0TDyKQ5c1DhNaotp1_BvuYKydVioQzl1WdLrhHTUTHXIjQjI2ZMIlsLsyPxMgzEZQ3NiURRsi4U3WVJeh5-ZYgnMJEYk2BNzpiSoQqf4U88GquDMoA8Xli_uDHR8nUjeBzHh9YpYBvRmhJDUQmyVShEHBRSW-i1dEscrYgFc-zZRtLepZEWMN_2vFyah68laNG8Dott0umxKJ0E5cJxg2dORtFDC27YB2oE694js2FASpQTzhHcT_qBM2zUQWWabbVNKixWaaJ3xJ6R4-dK4fiqvEPN0pZD7kTZ95imtABuwhW4XEWpeTME6h9nrkOgiD_Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=quBC_UIEFjCV7mQv_e0TDyKQ5c1DhNaotp1_BvuYKydVioQzl1WdLrhHTUTHXIjQjI2ZMIlsLsyPxMgzEZQ3NiURRsi4U3WVJeh5-ZYgnMJEYk2BNzpiSoQqf4U88GquDMoA8Xli_uDHR8nUjeBzHh9YpYBvRmhJDUQmyVShEHBRSW-i1dEscrYgFc-zZRtLepZEWMN_2vFyah68laNG8Dott0umxKJ0E5cJxg2dORtFDC27YB2oE694js2FASpQTzhHcT_qBM2zUQWWabbVNKixWaaJ3xJ6R4-dK4fiqvEPN0pZD7kTZ95imtABuwhW4XEWpeTME6h9nrkOgiD_Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a2dzzCxr6Ps9pQ_BF78KI0XYhTbBu1Dk38tCFidLBVsE2uTCNVnFCdBeg2ieppdB-5gru3jzKi0sW-3G43QWVWFpeVBgSmp6XZha-mFbktrTiP1lyA-Ulx9mQpC-8EUQJlx3s5m_RHEuW5VTuoSMWakPBDLmjJOKRHNj4wJHclcEJVh58eslrMcPLlIzLIbd9QkNJad1PtseL1cx87prngTvCHTrQ9PjweE6fWO67gXPEd-DJlwGlksdAGl5oUxaWIFrxAPG4CFqthKnO3xsOTNniHnkZPRUaN48HaGA5UlkO6rWQd3Ud3SOvNUsBH879qrAfthCHd7EamX9fPdiSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
بدلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🌐
MelBet1.net
🌐
MelBet1.net</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23886" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHac8rwTBW2ka1nofTblZy8EogrzSGV_JT2TgbjkcFH2_1iWa3rfgZ4KtYKcqHlqM588yAuDuzwY594vL4jdGw2DffaVe7ftdSVRMZoyco9qF5CQMDTjkxlOAncM1Y-5aGLMXe_HPCVHA3xCYbv1CLAWrSLqMfm5sk0Oi6_WlLweRXVIwEZTH9-Ghp6jbgMLiJpkN8l37iOCfD7Akc694DCOjQkBhi09KgNnGHADzb4RnsarwKBBa4yZRgfNlacY-uu9SVxp1NmlKrdeLVd18cXD7ZZlZSN2dBTJP8St1DxJAsiWF4TqAdmk6DmMemhSBNUVatWdNJRm8cKmoHYqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=WMFUCkQ9BXv8okdYptrvUN-CBLCfajZKVtlCjreeHinkoK-6wMHL2oXeVeViPMV_OwmA1-fXH-GXJbxDC0KpHNhhOr_HPGyW06y4oFEMIMs3ms9cUeR2N9Xi-EeFmhBpZfr59jXxZzxIf4DiUQZIxmsV-vv5CnOv5kOrWg5RKPYJj_YmAV0tRRL6x0zpgcsskO-6qa7dbFqhvzgUWFeF-Mr5GAbx6m2YY3P_7qDLXwn2Af_qSE1ApsYyKgHlFp-i0MBiJ07IZKSHkBcJsCUyEr46fbZ0tAnzpdRqRTTHFcrHi8jLORFORtu5wAAODq5r5uHKSieKOH8Hrg3OP753Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=WMFUCkQ9BXv8okdYptrvUN-CBLCfajZKVtlCjreeHinkoK-6wMHL2oXeVeViPMV_OwmA1-fXH-GXJbxDC0KpHNhhOr_HPGyW06y4oFEMIMs3ms9cUeR2N9Xi-EeFmhBpZfr59jXxZzxIf4DiUQZIxmsV-vv5CnOv5kOrWg5RKPYJj_YmAV0tRRL6x0zpgcsskO-6qa7dbFqhvzgUWFeF-Mr5GAbx6m2YY3P_7qDLXwn2Af_qSE1ApsYyKgHlFp-i0MBiJ07IZKSHkBcJsCUyEr46fbZ0tAnzpdRqRTTHFcrHi8jLORFORtu5wAAODq5r5uHKSieKOH8Hrg3OP753Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1o2MdAckpYJjCdJ5L53D99SIKUYUx3tYOJxeYDKiAgfAZdu7VBJkX7fdD4qNrIXBXyKZEEdEih26boc3Tva8HAmT3CQh1FjxGp45BsT9IvqrwJbRDSA6WlrRuZC1WblpVlTzHpTnAAzr9i8xq41-liGAXDKDbK61XMf2SzqaAVi02ZNQv64pFiBXk8OiUPNQ4hcWSk1iELgPZYJl_CQXlyA7iNt0-xgL_L4MaLoiMSt0IHc6Tf3GFjMLM7DVnpivSaTSAqaB6fngkiatc6svIU1_InE3FtjjogJQxBEJg-3VWGWQ9q3EBZxJijWQ1hj91uFPrgnvloUsNb8Xpg3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUGPbd6oqt2VdnYq7xvUCccHVwe9-ODyfKFdigOSFgW0YKUIY9y9I1Gzx16XfNleobbEhFRRrVFQv1tkgram4iwmPAwK2_irPU7MYUOj6dLeuj4cZTGcp1Gm0-MWPDqvOA3VJaY8CS534ePsHhD4i0IO6g8AQbXLgU8VRgBHdZYU4QTanXSWYjYpJnLXjo4ZSQpm22woPoOUu2iptLUchS_fcPfChlHTucbqxZMHcsX3U8Ix336WQKO5mriQ1CcnsqgBRJM9xtDhp4VPEYnWJA1qcMddJlpnKW6jzOjHy2RmXso2MVYfIxtFgECJcprQnaGfTeDSSEg4bzlByZJS8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6lOmu_sZDiaL1kDs1hCSTMLGxgGWByNpsgMFEg0_175221q6ztMYH9TS13p_evPDIbbBr5KQtwL7DH59f8Hr6ntRgP_NurfITpCsztGOfD-sqp9btnJI2gm9IL-vF51Z-85b_ritK1yi1lIZGWvZ0kZvC84dg9qrytdtkEqMRRV-XYU0xskaTCN92j6-D2IcDvr9ARWMVlgjmzMgjo-UN3Em1GGNYx5vIpDfbyVWtt0W2fSWEF_nsRhRGmV7h5BEKXzTJxPuoVtGWrvfkKFsfPcBVG2EYlX-jW1a90lBlGo2KH4ERHnkVAtgBnvstetDZZpv5T5pNXwq8Mgql3nKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23879" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23878">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu-ds9iLQ-1L4T9i5a9PTVr-fqZ9narnEyzAq8DmjEy7VhSbE1p2VY1oH1W9f3jp7km2e1_SUE1F1ofOotCheE9zeT_8QHIygRnmouL2YOHG0EDNW0oIY4SjW3xKThvhkTRedd35rW2zKLVgrS3OvGEKmv_UotdShQ5bnKRZtuq5GFrrX_U0xi0Nquy_Cp8y9i_S1vU8nU0ItJd28rz8sLP2BI9zxDP5xWhBqVifLIgIoQmXU05S7eQB9yFVK0kBja7qQEXRopO3IFiv-O5SHPMUw262LS9hmXDY7M7l1VE3o6ciHyyO7mUVDAwkcoNOUfzf4uv_x7vCjJHcw_Ykgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23878" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOkuLkMa8djLHtL0TKobt53Ho2_fR8ZJwuvjJexqFVFTzExUBMHMRX83grAkU8s3CC1rBi_U9aAqvBiuSRnAbd8E7GWa8XlgRgAg2Nkw3BsmYr5vTgLMvepIPBWCmTa9eN40BTEg8YaXYNcKrZMBeVxoB--Ve1wprk91gPbdC3vy94Z1jc5nnbInb9wFz3cTystWc_RnQkBVgrms04ArXkuBhJJUBi6sFjt-fjmcUsvFZV9RT4BLrgx2Ws4i6UEddBbiUJROmQk2x20ojsJc9essx1tDC4HI40REjDsD4eDvqclf7lR42AGYaP-wcU2bos3DPdqGOCGLQ_dhoCzHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9jDfP71myRn48f2DOoPDOp4S04T_A0iAUQaOIHEJNwBVXhAZWDqzslo_8kNYaUdbHoD0mWJI6hSTCg24T9HygN1QaogcQcY8FdtIlWoGFxEx0NjlZTGVV7uB8Pnv_K7232BApVIT8GToQG5e_ogGBb_lPQ6gq8R9CpsHhtjQ76p5vcclkBXe6PtNUqCBJ5nw_peSqLCvCry6oBaORurAWsflrEhGZ_ZaARfMow2VsbAShnDi0A6OVcNfWF0yFWt01DM84JNwbG897UhZzE35suWmevbL0lxOwBmji8ID6f2DX8t45JoxXejgHKqHsxOggrpGzuA2YqQvhFjJx4NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6o-C2klJxbdCIFGUpWZ70OJiNF3NY79V4aUMLR-p_2_ev0dP4Ry9YMk_4cSfN194PsEqcqaqnPUkwgTN1ihJivqsahy_D-QINCyL_Y-o8C3XsO4BgJFMYgdU9uxKDBNjQuhZovxCHhrxq8Q7MZcB9TEOonZzG0CllIHX1RpnqIaRtCyFccPjBZR14zw68qbRjv0Tdk9hCCxuBHkUdEDsZ07awmoHAqDQtJanUbLjFDU_if49udiuGjcI33mGXTjZNvOnj548GbveCxPIbnI41XpRz9bBt73lXcYumYhaqVvzGV7MJo05d-dUfPtsvljdF0xx57Sy9Fy4k1N51sKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzH9FS_UzLiNvWD4PT2eO7FfjzD7PJcF083qc7RPS2lAtwZvSJvscoo4gwRdAV3OqhIO7XC2a-BC8WBZiBiDlqgBK_DwX8QvSTyy5y55ic74eQTmxnarpH6Ui-ruH4G5752FbhxUbQ47GOIqRnNvmaeF4WPhOqFVrTJE2qwOatD4D4qKd60yP563TMwvwXHLa8Bx6OLNk1JrnRq9KhODzbHRkiigwON_MplvPQ15SOW9qN-4oFjKElkikuGCRXAIw4aQ53en8y3Wmu4tvNFMXydhUbtOdyDLQxxeD7vUcLvsyVKmruHMHFtC6H7No7Q7-DhUxQjF-L5pxJvgdvijWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-8RCjHGxwF66srjQZ2edIZ81Z_wpEO5-20olJFKctuGD0iEDN0pcw1EUbsdAnSMtbLKfHMoNYqtuLyJyFm33FANMQJe6nIvZmgWoMx932x5u0i_tDzTT9MZRyB3rJnSxWj7fd0XBiE0to_mj7TXryeDTcOgNRtGBaa7wtttEGOinq5WlWVq_klsYIZ7iNAKlAO_tJ3CRHsAKxhNdCYIuefK8w94a6N3XBtO7jbden8QucXA6FAXxy-iS0V49Y3SngzRvX3Py34l-def3GYLQirWzOS0ynYSswJoelSspc884FRbl2etTPbdOnyQjlC-xQrz1UixBqOMrFIbl7P_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚽️
ویدیوکامل‌ویژه‌برنامه‌امشب‌عادل‌برای جام جهانی 2026 با حضور اوسمار ویرا سرمربی پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23868" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWe_Ym4xUaO-NEz6FcBPrcBnViC-3W5h6d2dDi5TR8KmPHuIhjabWu_CGRTqivtC5PqtqUgWrlfJwK8XTe4yirUbQKOs8kHasA_sZJkeD_7Tw4WLDCw5Gn5mcNW-rsgCXy2MPBAVfDVJUc07VObSbwxWDmNISVcQHkIGvkGmXHWHK0Q_xSy0FZt4yLN9F69VWumJpv1gfo0GfbmjMmoLYvyT9zRTYSETAcNfPOgMA6l0yLIHwI9JVYfXGcBcuyHG-UmBnQsK3t2xY5Wj19FfYCEmim4iIvIwqyW-i2o0uWhPy5AgC3xPADBc8V8hx_-4M42BZs7Wq8YBFWGamXppAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛پیروخبر اخیررسانه پرشیانا؛ حالا خبر رسیده که‌مدیریت‌باشگاه‌استقلال برای عقد قرار دادی‌ چهارساله‌با پوریا شهرآبادی مهاجم 20 ساله گل گهر به توافق‌کامل و نهایی رسیده و درصورت توافق بامدیران تیم گل گهر این انتقال انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23867" target="_blank">📅 00:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23866" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm8A7--wRgND4xTZZVvSTDqCbFCv20-wxr2Cc1EaDoFXmbRfI2ze9TyFU3XEHG6NIi3PhUJy2AXwc2yUr4EufxI28HB5zUbbZ2S0_cRLf9sHlhcPL8lIytKats4iDgeZbsd20yVIV1Egwaw0BjBrVeUD4ZvtX_pL77fckLGvWeyZR2nZWF3gMSCc1gzXGeP9PJY-l8c9M1Of1owPKu1b9ibmYjIriQeALbfDCN_G5HmbWaCzmMbOEdIudE0XIujlbTB1mYc39i6hD6MF5RJ86qD8Igs5D50Znl69unjjwCjYXQ_pQpg672_piwUyf-g38UWY0XCRTtA85362XYQvBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026
؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23865" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXPfmK1mPMhs2MxDUQIZTSedJsNPJrexK0PW8lCjzCRobYFbZTaR3U219niXzwX2CXM7RQevnXosslZrC0Zuqey_WarFDHhtZ_xjXjyjTub3Hzq8wqCAq5JRVhVs0cDRP3Tlhh02hwGdD-QvvkBfzMmS04vhzSqUVAOrZyV_I31P9qw__pMKkcq6NE7SApN4VeRc3Yn88g1DdKLaOwYMYMkZS5DMasqrVmSf8aEaUbuCXTzh4PZW3peXbbpo7liQjiq9zlJrF3dXBpTOFa77746UsGyQC3ZyLI01PkDxtYmU_81tCpD41ECfaetJn6jqiSsQioN7uYGrMbI2xNvPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران باشگاه اتحادکلبا امارات اعلام کرده که اماده است که رضایت نامه محمد مهدی محبی وینگر 26 ساله خود را با دریافت 1.2 میلیون یورو صادر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23864" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVxVl79ptSUr9BmfIbPY8seqpnv632_b-lS3Em7UrhfCZVoZ7R2ZAAE6Ou1DkJBfUPnsNZm-Rz5O8om84oCW3d04zsm2LxzFKfSotYEHMz4Fhh0bq0ZZ2PBO7YuWhM5KGvbQYFcvVvBkAwepuy8QSD4brm6yfblgbP9HHoXpH2V5dy2-3yM56suQtfdaHw3CZmiQ0MPHPETmCwLdEOq92oqlfCQT8GF2uBX-PcEsDdpzDbmZTGlvaJdGPjaWW9usy0NirjaI-DQvR5F8i_hZtsLlSM4FTcxsjPAciMpW65CdGMX2XcG-NntHwggK8aIGrrRCGGpQCJZ3ytFCw1KIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام رضایت پرسپولیس، چادرملو و گل‌گهر؛ برگزاری تورنمنت 3 جانبه برای سهمیه آسیایی قطعی شد! و جزییات آن از سوی فدراسیون اعلام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23863" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9UFCNdtL9vMzFntYtxhFwIaXgC9BAO22jFaYTBFSoSqYkMk5iZNCLeurHITWhpF8D0viTK7j98osbEXH3lZTv2N_j-kcUHLeaYtZ5ga6bzoW-S1cEoZBHIojTXpdJ9Xmep8yojNuIDbBRelLA5O-Q5UVM_alwAnWpG7GMsduzc86NDOm-rTZMK7gK6J6OdIvAjADoB3oENsL_DizoOG8a3-9liYxjtP8fb626SHeAVQvpWttrTpcZovy1zaqDpAwNlKl0nSBYDBPRJK6mYpEXtjFi96FU4uj29fdHUINu6IiFX1OTwjlagTqF7WvUuaOHJMJDthke4-waNW9LrRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران‌دوباشگاه‌چادرملو و گل‌گهر سیرجان امروز به فدراسیون فوتبال اعلام کرده که در هییچ تورنمنت سه گانه‌ای برای تعیین‌تیم راه یافته به سطح دوم لیگ قهرمانان آسیا شرکت نخواهیم‌کرد. مدیرعامل گل‌گهر گفته حق مسلم باشگاه ماست که راهی آسیا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23862" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T07SpsFQD5OY8u7_kqKyXPBR3j9-p4GldAlFVXyDYFuupnYH-0NX85jmmkuuz-9Jc83vySqiRzF0HbmXCB_Psvs_R7xygQKeUO0WLdrHcJryMQv6Bf4YDc4hyqbacpH4fV-2NhB0skAbnr4ZfIYMJRt-_aqr2CTTg1QFDFAddxlmVPE5-_zlyXuyjZLSA7mo5x_k6_3T79NKOo6e4bnb0jPJq5fdIpF8erMc-3gZ7VdLAcAd9WWvGRy3dT_1hmytfgcFQIHN4hZwHz7bjAsi2-YSn5BZAcaPZmyaGnwje8eRp_11C2e0f7zqu3O6FR8uHF7oNNZEQx50TzycXiJSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23861" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyX7xO5Wzm_wSBpnqYMlE6cO7g6U5mGC06dBbUBAZ1ID8bh7DXXbin8XWwseZGUdvfmSelPfnx3pDXAo_zfMV7IE5m5XCZ3dEhUD2rkwALOKrNA3cBKHU6LLcr-s4NLPZTgbHvwAWJl9MPUwp5Xo4Y33IyUTBkcYhTxf2AvMHEzVH7FikXDhZ_DuleSUeISvnbdBZrfBb363S4VRVzW6warKVa7iE9cY4URzxnDLyz_YQTmrWiU7_dA5XT7WZn1ipvHLljAPd0uf4JztFCVGsqoZeXgybqXsIoGpSGMjX6UKrZKbW8WqCDZRVWsZUiL2suGR06NyP0mfGzZB-GqqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23860" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5d7_QP5UqhoMACT-nd6oj5s4vtzGG6ZBlvQ-fuOXzJ6RvKRY-AGGlutqThV5nKIIHQqy9JKAfNbExwxtcF9Oc_fAzYG7QWXzRt7MegZI5ZGlypIXgS61FmCquuhlQl0bg3vHfesnK7pMfQzgESPQj6vVcLtC58BMOzKG8r2fbNMagVkKsQ5cCJfKEEHLD9kYXTYg3IqunjWbrnXGV0KEvyKqRf36l4C8bZctDrbrt9uZgYtgLw6cxiZnjwAYWaDMInRgzL-OEmx6zCG-y2-HqBqbiyAGSDxUJaQ1vnktagPa9Wit-B63NSyjfInltbRtzQhyspMA4UAzKybZ5pGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23859" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AODnqGeWR-ROs-1XIh16sEPU3QKzqoL4ZIq9W_9zAH3mRBaeDf3mlgXBdqjmmajbCKHh5T2mQpbmjibhfvzMk40joFplBNUDbGPpIRaRG9xaGdn73aG-ZK3Wl5xf69wwFBu0Mw54dQbCXddTcjrchHlzon1pq82H53Gbqt7z44VwPVFoP3of1327y-gAC8vQ1gsaFnusmuB65MWUPNyFVlgmMbAw91Hjd-2UHfGiRq0TsOOmMGLvcz6wigJtqe38ab2Qk32a5lNYns2dhiIsctDXbpmX3Q2VB8_VBH5f4Sour-g5ohqB7V1huqyAPEXqpdj36L9m8LytxHju6TV_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23858" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz58XkoFiHilqcfw_Nttn6YrMMiToiEPiSrYJKz_jrO7eTHLHtv0tSxwob6JpFIb21RVCxTTRUsPBjQsG8C2xb0gdERQManxuO9J3f0Q8iHN8s3cdUsuj5ddltqaW6h8s5XIkeAkOFki8gvStrqDJK3nAB7kPAg7Voj--9uMRzHzoCVMmcjsn5R3GcYn0hTTaJXEZ9zeq8ZPDk_9FSPNggt9Fvqtf2mjxkbFBaO5BVYgdeB_P5MrZOp_83pxjk_axPk1zukisIu4zB2lnhV3q4e3kxjJY3ddBMB721JGCyDTYiTR54d-9ohptVwmrt-HQAt2K-dotRMR1SoB8UkqOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران بانک‌شهر معتقدن که پرسپولیس در فصل جدید باتاکتیک‌های‌اوسمار ویرا بجایی نمیرسه و قصد داره توافقی باویرا فسخ‌کنن و سرمربی سابق تراکتور رو به جمع سرخپوشان پایتخت بیاورند. باشگاه بخواد قرارداد اوسمار رو یک‌طرفه‌فسخ‌کنه باید 1.5 میلیون دلار به او پرداخت…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23857" target="_blank">📅 22:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc74mLoeTXZnHNOX8axleEYMkbjmqiiHz1N4P0rN42coiRLHPAryS6MPihRjFHej433l3DOcpK6ZFuagU-SDLTmJuUdFmSXIrI71HKCSsCMo0tEvZEkZ858c5FINQA4A06-9IxG8SH6zik1M6B6mO3zjlf9YR8O9vrrQup6_pLg82pJD8zvUmzk9I6bBasb-wUwKgYazI0kaQB0zIQgO5e32ccxcV5hE76AlJ6SDDl6D-K_H4l2mCf_nAC-MUwFnLm95phgVAwoxPAo_ng7TJhktrMmSzvFI96yxWrD79aZsXVH3I-VZLMz68cUY3EEgftV27dfLKsIlCUqFTap57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23856" target="_blank">📅 21:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oK0gCHxyHKDsPRwD2QtuXtru0ZyDPWchkjjFqBk-XIczhpBWUiy95QTS8K-7MAdJRamWmWWY_1tdGWok_LNUu40T4GiKLd5YcQVDCM04YUDz9TtQ1wAG-UXjl5v0Ogx5zL_R9XBrglxztcJqKY4rQgRKFATA9gq0nmwnuN1rD2Y2H7m_QIaAhEYZgipN0YJf9_3yhQQ7qWPEJ0jjNr45up6t2pW4x6_udBAPkofyoSa55EzSNUQCk_jW1O-G4WPJ9LQML7hFrOyqRHogINgDATgjn8UEb88I9K26YYvbVES6r1LGvd69_rfg0GooTkNxR04qyD4e89DunjU13yr9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I43Iu9E3lSvVEaiMjio-nBlEVumJDxJL6IgaWu5Euu6V17XdNpVbPS4ItaAME8ZcnvOwgLioC82V4kW8xIqNhyBvEQEd6mjUCdVujHXclkBBTPPpI3rb-XAN6BeHR18Fxpfc2inklk-eqa74Gb8yJA8KJ2qrw6mA_OWZofcc4kgoDGQfjZxH81LyWablFatpc0CMZG_YZw5TTJXLEzuhJEv0eUWWbDomyUDesXnqhF_mm6xIaYqNpQOi0u0dVh-LXS1kKRcNN2StoYFhlzj_A1gT4YLIElajUgElnqn9_K8l4WhRl28_qPsirPXNS8mMTA-0O69Udl4hnTf8WwkTDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd-CaE0t8zzFADaNsmJJrbg-BLcdNb4jpSQHYipibkcS6dDxTpAaOissMBb06Nv9PxKvO7fbW9mkRr_yxYVcGwujZ-dnlSmnjliwe5tnzZnc-BcWm_zK3HgSgF_0FPo94LWaPXzxwV5aufyIZGfm8lkEKXotYY7KLo0FASEK-jch3R-BmuKffucYtVmFLcVvVkUGydyesvPjsotBdKVyYtTcoddy6z4YFHe5yOH4gU3NIwzF887JriXsRUmSj9JNqUF1c_okmtHl7IdXhXuzUolKO2GXrIE5KJL3jgKQRUJTw1zzfUFfz6jfjj78nVUCJkSZljlOP1xHmRAtKa10iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awupJxyFK9XUmcde0rnirCBgVvpem0dNHYUM-y4_UYtQO-2RB9W8ta_LWY9IwAtaWLlhOITFwFe6B7HyAWlrUR6OVDYsUXkB6O1d9Td_nof7QfkQxLG99NLfeESFhiiBN2o2ZIzW6YgQpEKb-3hCryi-GL-kkEXjbPPiyZajOMBDcSfsA0uFtm7FEQP1IyiZgaZvgTbefOCZnNPUjeZkdinf1EBV5yGssdQ6FsCk-cs_i_znOZC0I-kvlVr-xNIujy0qUz7VZ4ctVKPmvKMvRFYOYVq1XBegwQTzIDQLPghX5oabK_01dl7j4rCHvM2o79A3tkHTHMMaT9J7Vu2X7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=eaAcXuwKrGN5QYzSyWNgq2pSebr7_gpZK096QZGDOu86WcjQWeabYdaITEdwXHEwgAfO7BxSCyw0Pg60elj9ic431cPzYoPTGpi2TCoW1hd0ErHKat48OjaFcpKjjBIB9pVMPI3mb1_OGdw2RrYIlC1ITlPsrGVfsNFMRXiLAubLOgYDcipR825NiZ9gpAyjJSy_kieqpy8L_oxvl8DUj2sOAOh4jI85KqIo4QXAVQgduyG3ntgPkz_IXGfCa3h9HKHi9V1tYxOqCi4m7Fy4Uigr_xrl7Mcn5m52s3G4_9TA5Xtrf0_Tw_1n9fr9bwi88DKfKHl_wWsJtOvWXrxPkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=eaAcXuwKrGN5QYzSyWNgq2pSebr7_gpZK096QZGDOu86WcjQWeabYdaITEdwXHEwgAfO7BxSCyw0Pg60elj9ic431cPzYoPTGpi2TCoW1hd0ErHKat48OjaFcpKjjBIB9pVMPI3mb1_OGdw2RrYIlC1ITlPsrGVfsNFMRXiLAubLOgYDcipR825NiZ9gpAyjJSy_kieqpy8L_oxvl8DUj2sOAOh4jI85KqIo4QXAVQgduyG3ntgPkz_IXGfCa3h9HKHi9V1tYxOqCi4m7Fy4Uigr_xrl7Mcn5m52s3G4_9TA5Xtrf0_Tw_1n9fr9bwi88DKfKHl_wWsJtOvWXrxPkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVYII7UyUelv3iafpHB2GaIql81Sj5OyYtmyKG-mI9e_pVVVXGHLGFL3CtnIC_GbbeQHde-k-FPEsHxONyii6kJDeGoJyNNH6Q63AusycQtTEPWqFFjwFQLyUVe4luq_yBTKYSuAaC6ZKFPrVdurpyqts2omO3XLHah4xu_MjobsxJlLJLBv04b5oz5cus5cW6CMuWIQvPW5TUHtxHo4B1_rRpIvp-cM7NONmM86lPTLseATrXGpagrqOtSkOWrDFlI8mmm8UrZGT-qyzZStp6RhHIgnGXcFHkzbYY-fpW3pbU3xrgmj3CehH79frgSzhZyIUTaYcubKuIUTkWWQwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrx9vVOFOVIRAE9K8UB3gaD2iwGlHF-1vFesdQ5z92Y6zdRExfHPbJtLh9OG1NDwsdqO6MU450rkWA-zf0BnjmF9LawYhN39awW8L9kDSJFDki8-l3I725H-dS-5uLx6sPnhAq6u5YVZuEdJGQaSWnKst26-6e3VGL3EA5L1bURmn2K8ViQgp7vBzodiuAOBpjrBiLPzWG4RQI6CGJnRUt0j6ggp6ByAM8nPTgK6n7uU_BUrzrRfTaAxjKy1k1i3mRc-RwaLXKN_EJKEtbn5V5l51R5a7IkyHb6fZk5gJGFlTFbn1YpjTEPhifSn36jCd6E4ZDhchcjdjgwP36QlLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY6AO_HtfEhc3Cm3JWV6pXb-UyKC_4TVxQow1Cos5q46csqI6-Mvk_ijOan9BnkeeieB4aWOLmlBdhby5mLvKeGXBZNnqjLR3rQLuQgSY_rLLv9jedPIjTBVe4lZrG9eOk5ZYBWgXxQBy2dZt0B3FgR_1RDohFpjfXyv7VRpbNCsQe6Jpf8aez_Gmte3oGmM1Rx5s03ayTaV9olasw91SrFDc6zRkNeu6NeANW4F3W6hMOdOmtWpELuJP91D79wEm5bNExkNlf6iiLHxPG5yEdtRpFDZAOFoi6v2OXokPWa3odp4gXnKGxRg2JWuSsuP7d7MJabsyfhtOIHc8zmO-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePQdGYdV4221B2dvfouEghz4usD3P3XFNgSqkpGN3n7ckIf9MnaFMGQ4VScXbLI7ay_F-rUzqo9lkQ-9q41bkk-esS9Xg5Gl2ZX5-wRJ6VnSoTARZ31XK7cXsU6seX5qXfZByOOdRncgjjb-rGRcoVLXGuygByFluvkci8jf2ABTtoiIqlyNLKHgfduu1XtoPAinniNa1boIrAYncUpx5KmPGri1YfJ43PorRLu16AsuZyfq4xiCFzUkq9ks1fOYzoA_qUWKVDq4gihFnolF556fIubGoM-IEuxZbuvJ-gS4i6o6L0Q9iBxm9iSqJi737l1mRrhGP91uz2EZab0kIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfauBoCdITozTTTy-ANXz7E_PiXKJUQmf5J7d2659C-4O5nBiA0ia7838Ve2Da43PU7Fu2fgWGUrzsA1M7IYbG7gbDtpWSzRbaC1B1cQcgJnm8M2V6lTxefrFIErZGFEQfHrN-bS4jPJVBCiitZX75rEgmKRWpYBUe2ykkF8f_sczzeS7D5YPxYffzjAbBxwVQNh6WrMGEhUsFryuKIAzrVT7TrtKn5eUnzy65_tEEgeLeAv4m0Z_0MFkm-ybal49SAiScngb00Qjs0EEW8A-kxiLUyvEHLj8IYmROut10YwkXhQLYbVHwJ7z8tLrc3B1XVS5hyHnwesyfo3JA51eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-SaMMFovblndpjjig-JYNXFBIWG72PGhdcO9Dq6bsQJut_0XEFB-37ObdZcJres9CRAafbF2cWqnwE39tpMssQF8SyLRR_G1XdT6KpotziRhgKWGYPcQmwZVgk9H0daeZd6HJ7k9fC8DyRY0xMS4iVnr7u_adaSvLAt492LiywaM_pECyKbApGzb7qqwj82ATp7epIyVEA9zFw4RPsWevzqR6G3hbzvHIjYYhCDCIfnpkI3jEux8jJh7QfNvGgus3lJE0cABj26opdI01Ur6_eHdeAJmMfBvTX1kN5AbUcy4lropG0jl9YgilveBQ2nasSA5zPfjLw2VQuS9K784Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ باشگاه تراکتور تبریز پیشنهادی دو ساله به ارزش 90 میلیارد تومان به شهریار معانلو مهاجم ملی پوش سابق اتحاد کلبا امارات داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23844" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-gKJmxwPvWKljT-g1oC2Teel5pKuByowIHcmDofRJ2XWUJcDfx4qBM5aUmEiql_gCbrP1Xo5_jK-Yk7DjOcQygjBAvVCJn8eWO9ApAmf9afpYAFIspTfHeqDVjmHBRXV2V_BKqFq82mBB6A0I-1E8bgNpOGTvxZbAIPg9-4IH7oLCnAt1AcSR1r6NtTyFiOXgXa9GzLvnyR04yWIxv_W_6JAcb-YjxNvdEBjrQ0uCXWhHWyJcx4ZQK4JW_23M7Ixb345ep4_p8G9PISjBI9i6z_0X6DKBYr0_wKen1Sca2npzuky97E-eQyCYafMxqQ0sXlZRZBanvd-NE1PxTjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23843" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9PRomaSFn55QDwwW9QF4pkcDzdWzDdqBgneKPrtDfEZnrqIXBGDBB24EbxIv4G7dP8NFp9qFkdYTuZiZ2sMZP_pPXdogPIcsSfmF_dxItmlfsFPPwOAqjZJEUDMxUfWqAsDDw4FuOnpPoopv2fAAhl1-KZfdeIAe48ubGqT8cGOCdXDBgXH6nmp8egNyTWvvdL6V7kKEf0FL1-xx6-DAPMWC6EisyeyWjNu6-WBruBjkbG0rvHOKRCcBq0OUMeESA-gK-WPRrrN_LCDHFE5hI1OjY2kw8R-eLWOMzvEjTLeEwea_zRAb0dyW-VTf7v85UJaFhYxk6hLy4sc2XewwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شش تا از سنگین‌ترین باخت تیم‌های آسیایی در تاریخ رقابت های جام جهانی؛ کره در صدر جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23841" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPyz0MOA8oCv9GrtbFQHU6umSm7uaJcycQ8kuJmzfr82TXI-VNl9AtdKnkNvsXhW3jyh0PFWHj6yksSGebeaT3OuG-S1jsm9-dQW9tTlKeJi-wPHsu7g6DllrZgHXMX5czkj055e3Iq5oWOKDAWihIyzSaDNyxIW524iRDS_2ZG3E870EhRW2Dq3GlHo7_ZlTQXQLCAfJ1t5PlG03enWMXThxzUBD9-cNH3CTJLmrqQNYGH2ANIZRbeCBoxZe3R6YsiTsfuVJPHhu28qRN2XE6IAecVG49gcYZrMIE4x7qngoloOR21w8ymjQDS7za0JZst7n0WUMX9MH8oRfV317w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
لیونل مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23840" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr2psXpyCdpnJo_FR7MVWaADlfvEHQ_2p3GcxMRpgoVUVv-FMFxqg--ZPdd42tJHE0tOw4Tvi7iJjaRqxu5PA80bUmVg2_94C4YxCzdY2UTXHH0hZkCrMPkcEEap9SMBux0cW5Wkz5MxlpdmxgjPgX1NWFwc5_R_AyaLI1_CZPpnbTea2u1_g3mZslubV0bZFNoBFiqQg06wY6NWeYD-ludDgc9hMnWv8xnhf4ZYPOFuMUfsu8B8NRXsJ6Q-Y8jT4Qp772FlawZatKpAS-QD7nhrZ_NYv0MQuDl2t8cfusNF1fkTk7uqo6uGKLk_YPHH0nLvFqrtfm-RsAwDAeyFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات
؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23839" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=AZqVwSLBqZuwWkX-tJx3dH0AGWob9XnuG_rhO_vyX8Ie0LV8KgvLZZwhY1rj69zlJevcDSKH5PhMEpvuWxp_g_PHczuPPwA1Ce6SI1iWVp_gwpiXiLySBkIUi1cunkMJJ_cvyKGB_POIYE5-n5-U_phkNwgA8vI2RpklHfiJ_acCmLuzTfYjrvrGEduIMuxaZyzKtqrMwip-EgXJjZL1TO4TATrqNLZMuPD2XphfZZiAFpcH6id4HguQyYYS6JpZ4GwUPi1RJQYJXqfmzRgpJSsJZkth_4C_heIFO2zM9kmwE-Xnrz45NDEqfUj96KH4SIAbBPdMIV7kf6em8u0wqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=AZqVwSLBqZuwWkX-tJx3dH0AGWob9XnuG_rhO_vyX8Ie0LV8KgvLZZwhY1rj69zlJevcDSKH5PhMEpvuWxp_g_PHczuPPwA1Ce6SI1iWVp_gwpiXiLySBkIUi1cunkMJJ_cvyKGB_POIYE5-n5-U_phkNwgA8vI2RpklHfiJ_acCmLuzTfYjrvrGEduIMuxaZyzKtqrMwip-EgXJjZL1TO4TATrqNLZMuPD2XphfZZiAFpcH6id4HguQyYYS6JpZ4GwUPi1RJQYJXqfmzRgpJSsJZkth_4C_heIFO2zM9kmwE-Xnrz45NDEqfUj96KH4SIAbBPdMIV7kf6em8u0wqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23838" target="_blank">📅 17:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
اگه‌ایران‌میزبان جام جهانی می‌شد...مگه اینکه با تصاویر ساخته‌شده‌توسط Ai بتونیم همچین چیزایی ببینیم وگرنه که تا حداقل ۲۰ ۳۰ سال دیگه هم قفله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23837" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4A6yNOJGQXO5WnTMVGh5iqD9Cgnlk6CDdAEYvS7CWg8HYl9YHCouSVHkY4aPuMTeB-iZ01-ZwH3-nbZHgpvBUNp_nQbGz6HUa-c2i36gC22zkf1IOJN-VSdSHlO6Lcxgibb4_0u5uvI3PgrBK62EbNTLS_uYDatnW6MAytF0rB9e1G6uQmDuXxR9PXzGBdDxIhnesbPHzG032rW9wWduAso5-agBw0oZ3ng6sff1QVy9gGDpJm38KRfsJQRwU4vfY22JBNbpQWS3uXLuEGBPUH5GK-hTK7pvIoCyY664khj5LwROUpq6guExi1ClbQuA1W2mpEwa7J-DrqkFBHAiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E80Ipztm1B1dX0rnxC9fru7Z4RFkpOp8S_Vp4_blS3Ry1RxW4a0bO9KIyjpd9TA97Ao_13BjXus_unlQOBiFjzHvaLNhavh5N5cyoiGW1KppmJ2oy1sSOtuZfZZpdLjHdLliMgf-J5usdzywoMRtBI8TdqMNRsogFocs0p15AZbISFje1ES_6o_MXF39YcjeGU20bTYNHe_rzGzCfnrWMiDM05yncbltFwdSLvTJMxgT-BzL6L_eZygsXpz5viVmMOnimvHBNphdfGjJ6IPcYvr_emeVSxWlNj2TnKb9tOMERvyerkCA4qxZrxh0b6EICNMG2Cy4_MkhgEZnL8kzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=tla7mdhNy0rWegBXZ24zIWAvy2eayucmmCrpHq1vkzj6niH5SRupEGS22jvEDw-iLh0HSLKRGTphn6-7T_1dCrR6yLHU0ndVJBeTGfubGOJkKs1Ebr8Ew-GqnV7uzRfgPsfJUe9QF07eUeZLmlu_slvmj32dtso3qStA_IDaONAs84_hIwbUZkNOmGbP87w_MANQJyPm7i8nKDD-z3dqYvTjjgGCv8lV0JwC0Mm0N_SRBKGD5BZv12HNeNIFbnnvgpnpCjNwYzojpvDj5UlGieIemYziSOqU1kX5wmS9GaTEUW_0cTyJKIxqZxyoZv7KgMsHrMMrHrtw1OBEOBZ7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=tla7mdhNy0rWegBXZ24zIWAvy2eayucmmCrpHq1vkzj6niH5SRupEGS22jvEDw-iLh0HSLKRGTphn6-7T_1dCrR6yLHU0ndVJBeTGfubGOJkKs1Ebr8Ew-GqnV7uzRfgPsfJUe9QF07eUeZLmlu_slvmj32dtso3qStA_IDaONAs84_hIwbUZkNOmGbP87w_MANQJyPm7i8nKDD-z3dqYvTjjgGCv8lV0JwC0Mm0N_SRBKGD5BZv12HNeNIFbnnvgpnpCjNwYzojpvDj5UlGieIemYziSOqU1kX5wmS9GaTEUW_0cTyJKIxqZxyoZv7KgMsHrMMrHrtw1OBEOBZ7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhKfxe-CYuvRI3SsczhhPZCGS8H9zo03qyUS26pNzjOeND7U4O64U3TKuYjBt-5uQ0i9y-MoyflZrxpltAljo3tw7H9fGDxWfDRS8V9es8HL67qYRDJPojG82hfasBeDqmav7zvfS4O6_h2ibOZyNeJoB_akqq8-Nt9swMUPoT-72AUZzVzRWSfNpckani42BUGcG_IUW--Rd8I8aOvSAX1EMpAPi41zsTzwjSBHSQb57Zu8iPZrKhGPa3T3SVliy7UXYrAYw3bp463auTTtKBIAyE1_dTdJlSscVALxlIbZT_VLfF2nZpL0ROFqegTTwVAuOBSGCWZvVTmSt4_0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hddkfq3Z2jbxO-vyr3UUUqmcTwZhEwBucL9Ln5534w9hDI8hfKQWS6B1ShD_kKnlx5fRTv7iLvAqgXHPVBLBYwpW13nsbU5Zzq0ZB_uE3E1XfZ91EwYPsgbV3YQkcDj6eZwswYSXZxQ2gV9WxozAWBKPPFmtRSCkgq5fLux-jMduzLp3O-egh1OTSA0h-tm_g43TjYZiwXabF1JLM1ON7ASBVG4N9P8d2kHNe0w9PUdSFJxEdslT33ka2I5PYk7C8YUw-ruhK_oxU2gef-3YlU8nv-jaRbTFJAW8RLjGbJpRB0TrEvjChk0QMODjvQcxrhuSQlnw79eQiYA0_cTmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=KTMRAz4y3zda0jgWWbBmV1wkJO0jupbdF_2m5Tep2lsWUtubuz-z29o-vP49BCjMM0NWrYqr7V7y7GZPK_fytlfcDlaEgpj90H_oBJaRQYbY0HR5il-hizkIPpvmOlJpYv7vZ_dYdCTmsU29e7XeoSHfwLiVwI9kZXBJArh8pDkX1eANy-ZMBsnsJUynrHwUredvghlYjm8ocaKQbS7KSEjQ1u3mkOGzm8ERvgfbXBRU6nE-NeZH9a41TwfmGS4QfmwDQjyxVq-grhC8SuvWduAUnmnlypWlg_mjIRYPWEPB14Q_WSCq0zZm5L_X8dyN-1SjmLf15fhjmTKwcQVbybtQXL_RBh59VuiwEBFGSO3aUupAg_s0mrDG7iN78dEAT0DD18jpf5wuU2NZMTVfzaREcHJqC8LdlB4-VfFh14DaKBByW2TvzCyJDTwMyMNsATwR3t1hfXyUFNZP8MQTT_6IChknGgOgcRTyzJjOFVRrNKDiBR2CH_fBsITYcGXOH4VhyI2_VIcIVgXbheVGJ9wmRW3NCgFMPcvavHVRyf6Wk0h2t8I5RrdSS7s4k5wty0Cmp8IBIquRpO74kqS1XVQH3meqU_4xt_jpZY2wwzc7O_fnlzOh4L9OIxvq3cez1CStWQDRjjd-hN2njTGQz3TgeyaCc4NW1h0tG3zPpg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=KTMRAz4y3zda0jgWWbBmV1wkJO0jupbdF_2m5Tep2lsWUtubuz-z29o-vP49BCjMM0NWrYqr7V7y7GZPK_fytlfcDlaEgpj90H_oBJaRQYbY0HR5il-hizkIPpvmOlJpYv7vZ_dYdCTmsU29e7XeoSHfwLiVwI9kZXBJArh8pDkX1eANy-ZMBsnsJUynrHwUredvghlYjm8ocaKQbS7KSEjQ1u3mkOGzm8ERvgfbXBRU6nE-NeZH9a41TwfmGS4QfmwDQjyxVq-grhC8SuvWduAUnmnlypWlg_mjIRYPWEPB14Q_WSCq0zZm5L_X8dyN-1SjmLf15fhjmTKwcQVbybtQXL_RBh59VuiwEBFGSO3aUupAg_s0mrDG7iN78dEAT0DD18jpf5wuU2NZMTVfzaREcHJqC8LdlB4-VfFh14DaKBByW2TvzCyJDTwMyMNsATwR3t1hfXyUFNZP8MQTT_6IChknGgOgcRTyzJjOFVRrNKDiBR2CH_fBsITYcGXOH4VhyI2_VIcIVgXbheVGJ9wmRW3NCgFMPcvavHVRyf6Wk0h2t8I5RrdSS7s4k5wty0Cmp8IBIquRpO74kqS1XVQH3meqU_4xt_jpZY2wwzc7O_fnlzOh4L9OIxvq3cez1CStWQDRjjd-hN2njTGQz3TgeyaCc4NW1h0tG3zPpg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
