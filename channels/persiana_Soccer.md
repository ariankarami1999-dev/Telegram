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
<img src="https://cdn4.telesco.pe/file/BuIeljnvCH4Dy_OvHVaKkCoDYWF8q11ZPScvC-zfUvJTqlsv_gMava8bts3q_3ET_PYXygpT28Vrf7fFAyCMwi4vA-MnZWgQ8ZGtb0JWO32SFy-dkGpZUd5pYQ9esOWO12esdIqFud7RukC8159nidbUMSJ87X2O1xxOp-VPEDUB0_D6i1aNd2nOPnMNt8RmgqSiTkbkw-Wf0xx6mFpFUPF23gfV5eqlf_rJiKHNVEhJVUhG-fYlMpxSfo-BC1eB-dflg0TZ5NaZYg1OnU9c9UlkzsW_zaxNpqAesrbXac_j8DTocUQumjei0UWjapwh3QePS4EnAA4yVgewUDMv5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 329K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 15:42:41</div>
<hr>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_W8yB-nC-ncJ9Ayc0lAgAPo8He8yAM87Ja7vh56nM0CYm84WJ2XuSQOag8rWMxeUtn_Re8tGvxhGguQ8pmCBYdbcdvkAgRzGIpPDWxlhQnzYbSmQ_HkM9oHhxnMxnf96c0GEOiRJDMEk1jcBugjjQ2fqJOPoz0bzZayrcOPylULMrRsVFizsxKLv-M79NeRzzMX7nE0GNfTX3yTqd4WWJ6ve5RieiAU8gpIkvvFsz9QWZeJtOBQfpLhPdzRTsgItcfJZaqj3wOww4e7KFCyRqPuP1LsbqVNCL-BzBjssc829Ektd-XCC8t2mN5pJdHy2MFnOorpBeFwAq32we8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK9XigW6u7bmYUaRSRtZkf4AYCPHHry4yXA8l0Biio8jQg9LvqEoVVvs6aWOXs_rbGATYuyt7ow4P2kkoiTToLoBVb5H9G8vHymstArzw_XxGo0SWx7dPB4hYCtZhlEZc_iGmz5KSwcCBmzT3bTYmJPouboNzrkjNO8yVyi9IyZ9TpEEx0PH6BiuBYIuDm6WWNAuBsrpoJZhY0V14G4JR6kbhTdXyxPRB4cuSUP8syPYQ_I6zqqfGytb05D4zOxNiRc7Jq9WH_mWjk3CxyTEdqo4YTddkQ1X6T6K72MVX3FxY9mGpClS7bge4hNN0rToe0I0dfok8JR7GE_rGRee-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWUMmcdQy4gbPFnoppVQ4Ql4XXZMb7hDBi2U_u2_Z9TJTuipybnErQIabFUzwCr2cQ8kTjf2UgYd63X2VNFfp5kZgt-3xvXHQOz9VqMEW7emBERC8kkTObEvwp99zS-t19JIpY-WMDB8-KImyG3cckplJbCq8TOzbssuLCYm9PH2tLcBYGI1h888u_xL09yC7RGRq0LuPJaFDpuuYTbZbKgVWveV0Tw5mthm0YOoTvYn-Ui3rgQtKPHQyhQ1tRonEkYiF2ae-Xm7Uz8Zj8Cm4yopaop6UmwU-vZ-JVTUkqkAu2rWWiOVRXmrv_6WoJouegXzneU5YwyRAsp-q94Jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWyH6B9zVohG0e--Nz6QHMlv_4qU53J15KKfKYRs17AHRlhxbIXFB7DNZwyE-vxgELN6lFWOKcQtzMBZQm3BgDk2Fv9Dhi8PXlxpC46Wj8e7UWU6e4lumbdgEfGT5N1o-LZ8t5ztR73ycKE6eghuyADHtiGSLOOUL0JXrvsIOPCA6YzrFoiNp1-esuAUPByyIDbP2RMTLZs0L-gQzMshK5PpopjgU4z397ZG8ibaPGRKIod4688Axt8BV_J0VS--21kdCwd3l9lhS7oLolac0xF6EGG1bDObpXFNGsZBnFWEG5354iKaqrvnXk7AGMJOvx9ZM9WT97V3aKZvuwqdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=KUGAJNybchwRKF8SREptRQ_IeAwFWXdW_MrbfKOoOLLlThUCaMukpBic2LxD8ndSEAMjqyS2Kr0rrsLhD2yAXYNARhfhnwy4v5ybbH9MMN1h-A-qRRq5962iQGmim32BBbmuuAwwxuIkPr3Gu0AfFgL_2sDkw27W46D4WJUvFluq9ddPTEqFc6zX38UzHHJPik07R8u4cL51nKmGIcgJ3-byw_QWYkeLF5xTSinUiuO-wu_aGoPlvuY8jc7XmzmRVhTfKiG7pozbJiRTOhP-8Iame6hGC1bkCcgzUpB078fnLQNOiwLmKz8e26cIez2ifrelITlSaFZHsHpYuExQFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=KUGAJNybchwRKF8SREptRQ_IeAwFWXdW_MrbfKOoOLLlThUCaMukpBic2LxD8ndSEAMjqyS2Kr0rrsLhD2yAXYNARhfhnwy4v5ybbH9MMN1h-A-qRRq5962iQGmim32BBbmuuAwwxuIkPr3Gu0AfFgL_2sDkw27W46D4WJUvFluq9ddPTEqFc6zX38UzHHJPik07R8u4cL51nKmGIcgJ3-byw_QWYkeLF5xTSinUiuO-wu_aGoPlvuY8jc7XmzmRVhTfKiG7pozbJiRTOhP-8Iame6hGC1bkCcgzUpB078fnLQNOiwLmKz8e26cIez2ifrelITlSaFZHsHpYuExQFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=lTC8VHE1YrT4YVHKbDIigdgxFyGoG2UeyWlDysASaC-hqXIzf_fA8YyDu11c0RVhAt1YQL05Il86x_bN9ZqGwSHWlDt-ZppUlHfPvZSZV-Yb1W5VpMAHbFqJZg4Qbg-MIR1Cc3AKDg2PiIaQFBu9VlnKxi9YHC7GNuocxphh18VZPsoGzdMFrkyfEks9K5Cuu_zSybmnrPioW7zEpnvCFfpkVWVPLl-rGeGczXXXbCboVT7LMcqYL01nkc8SeGxEaZ7Uew9zbCrwmXBwbtAEmnVnSSA9edCehY253fgy85ZpNJrb_-xuwZwOw_vIbINbvgTNZQlVntBQBGPIILY-oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=lTC8VHE1YrT4YVHKbDIigdgxFyGoG2UeyWlDysASaC-hqXIzf_fA8YyDu11c0RVhAt1YQL05Il86x_bN9ZqGwSHWlDt-ZppUlHfPvZSZV-Yb1W5VpMAHbFqJZg4Qbg-MIR1Cc3AKDg2PiIaQFBu9VlnKxi9YHC7GNuocxphh18VZPsoGzdMFrkyfEks9K5Cuu_zSybmnrPioW7zEpnvCFfpkVWVPLl-rGeGczXXXbCboVT7LMcqYL01nkc8SeGxEaZ7Uew9zbCrwmXBwbtAEmnVnSSA9edCehY253fgy85ZpNJrb_-xuwZwOw_vIbINbvgTNZQlVntBQBGPIILY-oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Totb5PsJf9-iP-KmJaTmhK7Q5RW-sadKdTrZ_bYkYRygzGaq2TrsQ-jUoJIZVjLVO9w-0IXBidml_vmW5wm95nYRIiJXHJtRXKzGbvQz7MxWYtk2HJoeI13zCSLWBapRrgS29wkJrLY9gEkr_vgSCv7wlI2ov-8QSSDkChnWYjEZKRJycD4zd2DQMwcIoS0QkNEq1bwmOzHoBCW51gVex3DmHO0jVmSpmVIr3qWqgfEQVCeUUq-fEhe7uy5fAr8gkBmzq4RlXWpbJjE1--qVx8xZN-VMjg0m2HuI973j20XJjvbChm-xkX4LF6EvUNVnAA9hM0bdQtHkjL_3Z-EKcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agm7aCLOs4hyv_Unh2Harf2pQJ5zxdkBAvPO6O17xN6xuyp0ujhyGrb1DkDptV78s-1l-t5RFii0LUivhfidP2LjBnUDK0O9gaSfPgvRH2TlTsSLIURN1CwV9zuNpmMt_U_PujdCD1LNqYvZqL-gPk91-LppNI2ToqH9GKEY-1R8abt-0A3wlQJgzfOYs1VR38Cx8AsG9Q_qsEB0gZLHME8NMhKvcZ6kq18zkcXhLGpU3gapIRaO-udGmNXSnby7u6WxHjMQDvpvrShMHX2WE5ZhTRVl3BZpB9XcSYnQlmUPmGHNuxlbj1ox4_dCxewYDy_wzIN0kQqyXhdCIGSCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKcfWuNwHLAHqVZ47YcUI4Vxmpx_zQg6RyIhT6_p8K2rmoxUwwiX3zexleU60UZ4jD7ZJknNJTHYp39KvLT9Evqfbq6rTBkTDI2hJhUKvl7t5vyUOtdss54aESIWQ2Xa9r6QpgGOgWiW3IGQjw5Vedw80hcKTyMdjY-ZP84VlAhYx1VdcozhF8KEVmKl_v-DWoxo-78kuHa5_J6V_SBFM0lg-cx-DCmpYcFkG1y4Ih-76ptvpo3MVP2GvvDClW8cImprCkCuLbKqfeBfwgdLJxv19Duo4tK4TvaKIzAPZyiR8g9Yzp7QsYkhJ-OXbxCCkIgzzSNi23QNrYR1tHodsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWk-JyTIUlQxXyDBmZGpuQP0ibDa9Kaa411AynCp1qol6I7tm3V6QvZe6DaFdi2XyFdnFSc-FNvuhFKxvsEryr7LOQixd9-LNjQQsjO4bg5QqbEq10kBPdzPEPVKkv4V-3afGEbJvyPCW-a1rkiii2HwlmYwWbO7XjRZr64MGrcmw2ylW6KNYrscdcHIOJkbFJjvyOrhj-LLwgc42enmCxnsvOw5ArEZp9DpzJeWJoca1XReK2PmOubPXNtsdv-DtpaGLO9fU8LZ6BpANNFEtAjYmYORHOy3Cr6M_jXx1pvL9OKojyiB2ArGTX3ENij0XD9WjcP8y-8ZvXV6MXhXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MujZELIeh3QyKn1l9i-ELVu9tFAI9t3D1AH5DaxfavFAET9nrXf1e7PM5GgLDII_Ba4COEJAS5u2I_mh1tw-xVLcu0WjnR_wnYLsGNEz60Luz0foh5bCc_kryE_pS3nEb0-QPl7WZZpibuXHvy7NoPtVdSuqosWYDa8ohcX-JCyGYmbNZmC96WF9vqbPXnjdw2mkvL36GlDi62PbS4tisCdTh_0G7w7St74ntYvFIQP3_-ymhPrakSDAPJFhgzSmDJJJgTmWhR8ceueqEocgjBYbCSjxrb6OyYZjY6_tvbN4gxeQ3hAKUowWEHvOoz2yWWMhQxzXA1pUZnZLGG_MQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چرااین‌روزهاسایت
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالات
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24517" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=ldD9XWXMhRr8L5KwFokC2iLtQb8DfrrHOnhfeLuqptzZrO5qyT2uKa0gUHFYasm50FWPSrsdMsJhUslrsFDEAFUUS3vTX9AaNUgb9wwG4QhD3CjaOTwwUdBxjXU0ycqTK4rQF5f5ThRgCmeB6e1dE-fScHQdTBb3KLoKonF9dEZJ9YRfcDR6CDVgq64a2RDzzJ3cWNkja1YPQzuFyKmr-_aTDjAl_lmYSJj9JTvbYi5cR490DmXD38jk7_2NQaupwIT2tHi29YWtTNJalcL5kxDuaAqgHUaVh93p8Al7c2xhKkE_rIGoLTVpdBJuClhmLy-VnYaEmeqUxa1KElVB2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=ldD9XWXMhRr8L5KwFokC2iLtQb8DfrrHOnhfeLuqptzZrO5qyT2uKa0gUHFYasm50FWPSrsdMsJhUslrsFDEAFUUS3vTX9AaNUgb9wwG4QhD3CjaOTwwUdBxjXU0ycqTK4rQF5f5ThRgCmeB6e1dE-fScHQdTBb3KLoKonF9dEZJ9YRfcDR6CDVgq64a2RDzzJ3cWNkja1YPQzuFyKmr-_aTDjAl_lmYSJj9JTvbYi5cR490DmXD38jk7_2NQaupwIT2tHi29YWtTNJalcL5kxDuaAqgHUaVh93p8Al7c2xhKkE_rIGoLTVpdBJuClhmLy-VnYaEmeqUxa1KElVB2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=TwiZbEaT2gpGxZ-gyqVAJNTVDy6RGy_nvzhAGV6Eukd6gt-UnR5m8RAnQ4a9qevNbixp1xaHjrwNsULA400mua7A_iU9ypXVC0jrlPDVKvahjFtkRcfBBwq2jiOAxN5A2QKEJfSlELb1Japl5DGiB0U_OOBuugZK6NlDwSEsMOkRPoQ5VEidjq9klzykgImbHjsVIGaLZC0ZzmWZCNYp3yNPS0M_4I54HSMrw2bV2J9AygMNq73ilwvIdVBS_Y9OYikSnGFHN51eoNVIoHeEWqVt-DmOgbPplwDN8ZPo8Hf6VK8wGWonZwYx3dBj3k1SxbqfHcSxp9B-7KK05W-JCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=TwiZbEaT2gpGxZ-gyqVAJNTVDy6RGy_nvzhAGV6Eukd6gt-UnR5m8RAnQ4a9qevNbixp1xaHjrwNsULA400mua7A_iU9ypXVC0jrlPDVKvahjFtkRcfBBwq2jiOAxN5A2QKEJfSlELb1Japl5DGiB0U_OOBuugZK6NlDwSEsMOkRPoQ5VEidjq9klzykgImbHjsVIGaLZC0ZzmWZCNYp3yNPS0M_4I54HSMrw2bV2J9AygMNq73ilwvIdVBS_Y9OYikSnGFHN51eoNVIoHeEWqVt-DmOgbPplwDN8ZPo8Hf6VK8wGWonZwYx3dBj3k1SxbqfHcSxp9B-7KK05W-JCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGGBcXi5X7yyd3IlAwv3086ykBfSnASgslDYJXhkqyRmUD5yFURU_L7Hj0YmoPfnkSkYN4eTenICZHSU7u_355ptBICvGuson4hpnDevdQFJghMJ6zAgkby3Ni0K1MEmFnpN_dOUzdznL7Ou99_DdpFFbp5YNhQN2rJAYwOhwJDa4G0oO5BU7gL4cZF3mfiXSSkKhUonnVV94qMimVVBZ9VVZDOjUIkipvUFirHHeRGQEmRFDa1eYVUNI_0jHRlkE7gtKS8UnMErzJtMr9C5vMOmJfRornOuj-csmJ5vht7jElAz-UAJXMwzokK3HhluC7Homi_qQuRF27YlxBfU3I7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGGBcXi5X7yyd3IlAwv3086ykBfSnASgslDYJXhkqyRmUD5yFURU_L7Hj0YmoPfnkSkYN4eTenICZHSU7u_355ptBICvGuson4hpnDevdQFJghMJ6zAgkby3Ni0K1MEmFnpN_dOUzdznL7Ou99_DdpFFbp5YNhQN2rJAYwOhwJDa4G0oO5BU7gL4cZF3mfiXSSkKhUonnVV94qMimVVBZ9VVZDOjUIkipvUFirHHeRGQEmRFDa1eYVUNI_0jHRlkE7gtKS8UnMErzJtMr9C5vMOmJfRornOuj-csmJ5vht7jElAz-UAJXMwzokK3HhluC7Homi_qQuRF27YlxBfU3I7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6vN91C-85w7bzQkn-U2bIcjCQtcv5YWJhMIPwhNRm8_fc4napLndzJOG2U0ZNod4gbiDxNUW_jKtejhoplpkqbXePty-082TiC7k_Ilx_YNQkdqII62C1MoNc-JPtTQ-ZVlwgG2iVKSGXdv7JjgVWHBTboD7t7VgujUyfio_mEeg94Zz49fxGt6sElts5J3hmWWHBIBqv5YVf6tDamlMakdnkBYDz01HuA9ESQPCkRU-2JQN4o6OrlAxWxQ0Zcz84Sfnj6BNLfxEwBp119TI2vJ434EirpX7YOw4kgc2WvnsPC_ntUKdLSjGz-KH7dBZr7ahOWCaid087_YhgvoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiGIGqMtXdQmoh5_bgF2RXLoUkOWR35jptQtAIY8js7OxUmkOcKRSy3p7WmZUPLCmdq9RpU5BZZjJg5hfkhsYQ90AKNSTn_S7oKf4h6pVDlNKGpVd1N904VDF0-ioxiWmDeQLJIo6M1_hQWmUHk4Jk87JeR1Ipi5toohnpCDD1v0WYwlz4A1Ykb1w6_VwysihRX6DTeT7ysb8G_YHz-3L3AXPMXvNjYMv6h1Rq5g0LF4t5FxT-_6TKfsysLl4lWTfDxjxcZ2_mZfeF3W2Fd0pZdCx6Hw_lphysdj1jnj9o9BpyA2Jism5BqByLYXQlfxqfcj8s1QzjRzYe8zX_-llQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSakpMmwbcgQBPezyAfvcxJ0_xZ6BNBDr-pR4HdzrDIEZYTo-xw9ld_DjQX9gMg7ii1uAXzxFxKS_c0E-otPVwTBOS7iVWJpiTwTYVJX_ztMj4bphlUfdOQ34dagyzOaxZwLe2Gu6_JFIBCJ1zfFekjumIoVp9mwkkcRni7Xa_pAYsM2M2aABvRijVoLQwg4oidg4tQuh3HfPrztooEinwmKrGPOnZAgZW2W7Vh0fq0CP90weHBKR0untxQBRdIrDsOw1qe9Kr4x7kfDfFTITIEJnaNeET3kZhos3HMpCT6cGSA_9RCxwZkKj8TXR7mAtDTZNghJWAtb1z6bpWeVLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNLHyKq5OlxSr3xlMKXn_ej7iy0Bei20O78IbDa9TkjD5byY8pZU31I0oi_5TXNSmOa4FYfWcBZePUtwfPrRjlK3s3Z5yB2lR9SaLuOBuaqoiph2dL25IvdY9R7yMAbuKgtZwrvUdFCo-5EK6mnAt712moc369uWsBTSQco04C_uZQ-iLwy67Zt_4kLgSjVca_zRuKZAMzFfDKk1brzP-XDgcYt3P36eJZairYEZB9j7j3iIZc-3UCub8LxQgbsoq6L2JO_46Qj98lmSdo8Krdb6xAYXlW8VbCBfGYRqXz0kT-vGEqlYL_5-ZCXBcfxp6gzM9U4ES3nAqZAH2iCGfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=emhG4lPBRQPzmtvd42Ca6-xlL92SSmA1O7OcEsnWKRMpVOdV9PJMIOXBOcrbvjV5DzZfuENkibDOzkX97caBpUJjAlQ6SG7Yuu0Z-COdfDgfPb-ZgNCbQK3olfti8nxrIN-oW33Ffj54YuJVErF6B5qfna-QtvQVJsdXxc07D1cK4-M25MfFlGuMFyAPRWD182UWn5Aw8OQQCR38miKk5pEq89zz0e8rIz8VAIXW0aykjo16X8SSvlqYhl6FEeHlONb_zz2r_LtVcLAiYedWH7NAjEfTMNt0FfkQmQAz6i85eh1_M9RdaoKUcSvxbhQwTgSzUZCCyufXiORRheYckwp052WA_L9EZt57zWvjsxFGQMvm3HhWtpaeVMOdNkU6JOGsSNq-c5gkcThYhKr7DZ5K1kNeH9c8D_g2Rf03XkEpTdwjF_ziyx5e5ZYI0nhphu-BpWL9qokIdO_-S98PRV8DhQgL0kHtZ0P1C6YfOoo9p7ozG-f_GTLHkvPJ3gg2MlkF7bUeLOKQusP26AD-xwRjMHWP4bokHOc7ArIPdVzVj9i9GNuAuAsoR5-eHARcTbzzz9VrfzlzO9gkifdsWK7RL-AuMwbkaslWT1dbrSjZprUPAutc3sAMH9OgoVqNvJnY5APf6YV7BfCr9_l3ACWUJc79VLUOPS775sx0luU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=emhG4lPBRQPzmtvd42Ca6-xlL92SSmA1O7OcEsnWKRMpVOdV9PJMIOXBOcrbvjV5DzZfuENkibDOzkX97caBpUJjAlQ6SG7Yuu0Z-COdfDgfPb-ZgNCbQK3olfti8nxrIN-oW33Ffj54YuJVErF6B5qfna-QtvQVJsdXxc07D1cK4-M25MfFlGuMFyAPRWD182UWn5Aw8OQQCR38miKk5pEq89zz0e8rIz8VAIXW0aykjo16X8SSvlqYhl6FEeHlONb_zz2r_LtVcLAiYedWH7NAjEfTMNt0FfkQmQAz6i85eh1_M9RdaoKUcSvxbhQwTgSzUZCCyufXiORRheYckwp052WA_L9EZt57zWvjsxFGQMvm3HhWtpaeVMOdNkU6JOGsSNq-c5gkcThYhKr7DZ5K1kNeH9c8D_g2Rf03XkEpTdwjF_ziyx5e5ZYI0nhphu-BpWL9qokIdO_-S98PRV8DhQgL0kHtZ0P1C6YfOoo9p7ozG-f_GTLHkvPJ3gg2MlkF7bUeLOKQusP26AD-xwRjMHWP4bokHOc7ArIPdVzVj9i9GNuAuAsoR5-eHARcTbzzz9VrfzlzO9gkifdsWK7RL-AuMwbkaslWT1dbrSjZprUPAutc3sAMH9OgoVqNvJnY5APf6YV7BfCr9_l3ACWUJc79VLUOPS775sx0luU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZuoN_Y_gB5TtGkJwryQLtf1YanT8sKeIqGNtaDTxO2Z4wFPPSvd-nN6ezwOv8CiYYXBVXAcnxHbS4vyM4GGN_kLu9iAlvMLD0MMsyFARMugFp9qA79aYIN4vbGf782PXF51IjTecSjr89lZCP28ckMR_JKsmdTLtdjIP6IX3_LrWNVwtfZiVODre9Zu5XQ9eqTGO309TQpPNKKZX72MUzQ-jFQd47Zt6p8QEufy57J15fbWOs2XuSKveXHOyVFIJJoa1DD3DDazRZe8UDVNcwK4VeVsNj4iBsLbK3CcD0DlG2rLhyGUpyFAz7OYuiQtw-Kf4yZ1DRd-FRRY-BxoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=gzPiUcNb3xaqimyGOgTutkhcxz5kZDBuxrv-jr2OnFXzMrTd0HEl03aBRUTvT4hOhTBMXpx4fSgBcD9LLvJy9LHVoLWwCaNrYBm2N50aeThwgT58gamT5Hj2xiz557A27u1uoqTEjKBNz1GOw_JzEQ6l-u9UE4qCNE0mN_cth7bEHnU_BNX89wuIEIA_VjMIJNV85U2-gES5VvBreWU6bF5QjDEJWhPRI1mc6s0jUs4DiSB4CnGM1iSLdDIXOuUWV9hP2rKglgB-cecGW2cBLpPcZqxkDo_iuVqNSApKrrI3xSL-ZjsgzawxkRNrxBtvaH_48MIobGI0-cEwa0Xrim94TWi5OZucaxtZC7KEvhhZRzf9vr32uwUD5IC67zD4DMedR9CabVTsXlT2pXK5sSxBXUpuq-FBjy_sGc_azNZeTZzEmF5nByPVjpYeDLdEXn4O9UfHE949whqepovSUfxgQkdSzdgZWsLnua-K2Mi2OBc4f0XJYDQByxFFKXCzVsIDN1StCrkuo36OvY3p-Oec2cjvvZai4aB6bCcrf__Jlxl7eUKxZ_2RxDub7Sv_mfSV0SSKsef6Aez50qxCFGFVZWXFaxpix9EBYcmvzZdeUyhPB7hYblVtvgRt5dEdYkNLX5H9fWHtoLsr7cM5iIr9NNHN2elk426HxKy9L6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=gzPiUcNb3xaqimyGOgTutkhcxz5kZDBuxrv-jr2OnFXzMrTd0HEl03aBRUTvT4hOhTBMXpx4fSgBcD9LLvJy9LHVoLWwCaNrYBm2N50aeThwgT58gamT5Hj2xiz557A27u1uoqTEjKBNz1GOw_JzEQ6l-u9UE4qCNE0mN_cth7bEHnU_BNX89wuIEIA_VjMIJNV85U2-gES5VvBreWU6bF5QjDEJWhPRI1mc6s0jUs4DiSB4CnGM1iSLdDIXOuUWV9hP2rKglgB-cecGW2cBLpPcZqxkDo_iuVqNSApKrrI3xSL-ZjsgzawxkRNrxBtvaH_48MIobGI0-cEwa0Xrim94TWi5OZucaxtZC7KEvhhZRzf9vr32uwUD5IC67zD4DMedR9CabVTsXlT2pXK5sSxBXUpuq-FBjy_sGc_azNZeTZzEmF5nByPVjpYeDLdEXn4O9UfHE949whqepovSUfxgQkdSzdgZWsLnua-K2Mi2OBc4f0XJYDQByxFFKXCzVsIDN1StCrkuo36OvY3p-Oec2cjvvZai4aB6bCcrf__Jlxl7eUKxZ_2RxDub7Sv_mfSV0SSKsef6Aez50qxCFGFVZWXFaxpix9EBYcmvzZdeUyhPB7hYblVtvgRt5dEdYkNLX5H9fWHtoLsr7cM5iIr9NNHN2elk426HxKy9L6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdmPWM9uFJ__9J30Oa2kw_pCR-PEgmV6shUdNFqR-RLjbHTblYeE6PB5xkCngwL96Noz-H6vZiBMxt8wxf7TN-SDWlqd08U9M0noKlC01ZcNytBClng9eWNmM937bPb3iHWmAyxYlsxvMywbi2OMDidH6tpmTIPmPmpIg95n0pzVF5a-8T7mJkH8xTnoquGnpQ7_DZqchLnED1qxGHPbdSB5uqdyodtxS0o2526mcWUlfvjGe3mS9TEyOOHSp5mbXPGM06ICC0VazcF8kdJasczzGT_Vc9MoDyOB2SNO1B6V6yl3VU7jM4mRIQtwd-gAoWUtiQX-fItv-aw7UQliyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tw3VwlzfZhN7FUHvE44N8UEZUbzCa-3cQt3cTOZ8lg7tKTRWCDELe2bBZiqjAsfPOqqwD-Bx2ck8Y2NdM9o3mkyb-ElZTfjtJzl7gczedIHjatboeCeYrDQPstgqSMEzRu9T9EsOwh9Drb9Yd6QGeGOp_AdbqrRKi2VN71q3Q187gywansQopmr9W7AetZrQGKOU9a_MIBk9BMfZBolttKCRCaptO98Kr8jOGK4yQPHxfb2eVwN8taaT5hYch_1j8fy8F6KNDPC3gSXKyxMjF5E1t7mcm9wNaVHdbvRDSPd7gUjS8ly2MPbM1-wsjCecc94UbPdLgUKsty0MhwTp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8AaRKaXStQYQrMSM8ryq_MIKYU9Wfvqokhlpo2eAHIk7aLmTqrICb8_S6a5_rDbhsGhA7nyoFU-l6VlbE8-PokO2BkwEfTHHSRXvW4irqL9D-O3N88AOTwBEESGGLzm2o0j12VKiEcPuf2n2HhugBloq0EEVB25E4VEnja4ZaSWBJAEjlruHngLR8SWVPqaFKWl7ej1gkIQ7CnEW_kti5jf4vTE7tZO6OdnRWJBXtfDgau8NwkCUzySVVsxcoNpfHSqsqcLn67ZFj1jXEuXmRUKJEVn4fmWNf2CTsxnGh_W0IIamWelGqDiNSf8Siqmf2wqnv7FyrcZwkXDwtbtVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAB3m2eMwVvfY37YTCBo1Y7YrZMLVnKrBTsTucqLelaybx9TlroH0FUc4W969yxYclpC1Yg1nHeFAEBY7yF96tkgMnw4nZ8A4CqTYHFPjRZloaqvn85urPq6itcCOrqxqY_xJcaBcnHWMOsU2FQHhEpOQQnmNVZnI6PW9YV9ibEHnwfKC9TZ6AvMUZpVnBGYc4dI3BU5A1Bx8gfSjpeqbyvfFO2ecChj9yVV1nikxe6cfqwnwcL9-NMLJPjDYeCvLGGgbLCr-XKrx3ucWQgSvt8rWRA4LLGfkasnyDnxNNoc9c1V2hNaoY5MDGgcApFl1YMXZSyZ3GOq-PjNKUjKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MICQGT3au-65iBuBv6JS9FOh-8L1xQ32uMgTDy3ISKkdwkQnDK2dz_xGqYKqg71RFg-KM3honCKlCbHTYQYWBM2h2sFmiTM0Il_q077AZJ4bzLzS-NzpJ-qcyXaKX9p6sy-zbGZTfMsQev45a1b5IkRROl5EFHgLA5YMBPtZs41qSoWMVg3D-YJzJp6VOoYU0TGD_qmLLsfC5AM3x4mfjDWAvdHX2VMwTRQgyiNfWCS9HKGHdBuVZm0X7Kgg-sEJP-dtHjLW2uZD7wai3fKPLceT-C6uBSvjcW17gjRZURQ7Lcgc9Ihb-k28fiyAMfVvHgNOtee0w5HiO5LR-w09KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PERhzFCEdqF3hvMK2ms_zAmuOtI3hUYFefY-ruvKtEabgxPv5MZnIsPiME0JzmLdSBzxK_DMNNknGsfqjP7JFpvAhbgeu4PcC-lvUpkKMi755mATLZmZDWcXOKVC2gTk76z9Hxan22j_BE6-GdupVkbBizTktFU4OX1QHxznHtgNV3DIB_hR6EkSDfs71GnB_mgfEKYgnAwBwhdXft8XaG5nmxFiGJX9U4zNvf3BXYSoWXvyROMUcLw6fHshdkoaaQmhZg0UpfVmTODMyMkm927VWdhto22E-_qcAyouT-C2xG4cmm-GRrN3MbpSNThub8p70hscQ4ryq8gEELVuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbUZTsSA-xwyTBW5r_kzNNlbN8IndZab6krLMCGWK5LMQsuUeJHp6ePRS6kuWBNE3zHoCHumKw9S1r1UTid1hr8959QKz7sz45zmBo0PVAQdpnUxgoVs616jmfC8pFsCAddz5ph9JKQt8H13SNdQCkoCMnAMw60LLc2racqRti256i2GjOtUTQw5iAGlXOAqoivbZip1LcG_AOYlcv1gzogtuVe0uil3arUDGgecBPYfBc7LDLnxAcu0wadFErT7Ben-nCnd7OhTYsGspsHS43besqPm4-4BTVrYLsaDNHzRtADLkqZXCzYYuaUMJGlh-HJJgOCKWCWMnNzdU7nBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=eMJLIVINyReQr50L3L0jHORkecAnBmPnLdYr3ghJ8dnDg51bKOoWCmAgas7uX7N1oRplrO4lCjdc7Z9o9F5CAbQEdvZRWMOR1c_NJJnMEMEEYYObc5UCDP9QglnXNhREKlRzuO-2_v1f0dV4Vo5sPL7nFJGLNdj66I34Mx7IddWlWUJogihzEDWShJuDij5Mazp9a5VQieycW_11b8XLOwkNjMFqAkZNcb6k7WzkmemH3qPMyOe8DDqCxAM8SCRFkhezPdKZlCQE0oqL9kFhF__CThkWqWzHOh8m2VM7fN7U5RmQ_fnMFh3sKLOAuurpu2mydah5ple6lCUHOnQa9rOCLdzNrPRD6p_CxVt5tQqywFpWmvgo-GqJC_zd-P_k2iM5oTlEB69Xu2q8RzvZw_yKcpvZVotgCM_-JIlxj-dRvm68E55XMCBQJ4gGlsrxuNx2P3GxgbEqnchodC1geyYyggfWOjJZSVKg09BWsp9g6ip4ACL5Bi8m9Gl89aT96oDWfAUYoEKg19O92b_Mh1jEwMSnNeknRiLbg5Z1E_Rii-2wvRmCkuD_skbQtrSJCDikv2-E0FjEVcSA7oZiNpUiXWHJkz3BbePmE10LepZcoGfUlCdkzTGtHFPDa8Hw0VO5l9DdCd8_Y8v4QkYRzpnmuAXEztv9rnXkpfgXIJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=eMJLIVINyReQr50L3L0jHORkecAnBmPnLdYr3ghJ8dnDg51bKOoWCmAgas7uX7N1oRplrO4lCjdc7Z9o9F5CAbQEdvZRWMOR1c_NJJnMEMEEYYObc5UCDP9QglnXNhREKlRzuO-2_v1f0dV4Vo5sPL7nFJGLNdj66I34Mx7IddWlWUJogihzEDWShJuDij5Mazp9a5VQieycW_11b8XLOwkNjMFqAkZNcb6k7WzkmemH3qPMyOe8DDqCxAM8SCRFkhezPdKZlCQE0oqL9kFhF__CThkWqWzHOh8m2VM7fN7U5RmQ_fnMFh3sKLOAuurpu2mydah5ple6lCUHOnQa9rOCLdzNrPRD6p_CxVt5tQqywFpWmvgo-GqJC_zd-P_k2iM5oTlEB69Xu2q8RzvZw_yKcpvZVotgCM_-JIlxj-dRvm68E55XMCBQJ4gGlsrxuNx2P3GxgbEqnchodC1geyYyggfWOjJZSVKg09BWsp9g6ip4ACL5Bi8m9Gl89aT96oDWfAUYoEKg19O92b_Mh1jEwMSnNeknRiLbg5Z1E_Rii-2wvRmCkuD_skbQtrSJCDikv2-E0FjEVcSA7oZiNpUiXWHJkz3BbePmE10LepZcoGfUlCdkzTGtHFPDa8Hw0VO5l9DdCd8_Y8v4QkYRzpnmuAXEztv9rnXkpfgXIJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvlMMaF85ZHziXw-8fDCpNIMc-IMAbmxgG8u4sEqIr5amd1FApW3whT50WZtgnPl3JlfWpxqgtz_jViOVD846AxmrqF9OlL08YaK4u5wLdElszEY0eywXgF-Zd6XOxsNxTFxpfuHkkmOvUn4PFDjWzj97GZQtyXkVknfCepJSx0g6D_rmCdINyXqnFNySB8cSusgDaJCSl3xBMRgXJAUHi0LfcZPndfahEuFUHkSuncr0-irjDKzUzsc4n98JvlQPAmwYudvuQfIh0Y96Z7WqwQtB8WdAaFVo_ax4cghC2Hwr9Z9rcdX0yJzrVhaNU2YOKDWW_mATFhuPrwr2OwpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph3kfWWYJJJfm1nupLz4jSGKyKG8w8V4xSyPayWKfb7VI-IP4qRHhMO5pMgHAQIxXO737vw9Y4ZRHoDgjTfPqEth44hj8gyEVdH6pKRQwREqbLcCGgcoyuhv5QriwLYypt-AV_pDUs4rV_mNmoQOtIs7Vf9Vrd9HQNbTH6y8zDgVKEpMEn4TN8QDZgkOUZO86q6AplK0WJZBuKZ_hmYHJSZaFZeWredCVcCYrXKKXO3OW4TTCvkNGm3QM4RXs4w7oekZf9RttI772pwmTz_fktpWfj-1ruBjWaY6VXXijbIpFOfqcTj7dMptJyvHqfAYDHIgLdIdlqXhdl-fY17JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXarFJVbkXbN9BeL860Api_SD0ZHh4GR9mZj1GwclZj-8BMwv1AF1PiR3W919ODJAF0LXbGhFnT7nMSATr0NmQYSk3FWCi5gsiXRrvNGd25E6FPfx0FA-wvZDL4pgIHL4PNoTuS3Yp4NvJvDjc8V4ukYh9Dgx1AJg21pnhjF2H4pZv3Yt2BJcIzd_Tde6-Fw6sujwmwvfe_jyElWifkn5-ZTaBil7Ne97KP9XUhY6jWUWQcyBBzYRbV8yLN8KqZfFAsjGE9WpGGkJh4qGBlaKBVLeomX5OjfczjUt06TAQHiLOTuWkY4kBJxdV3UM7Nfs00hLQZIVF_9pMrMT_YKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=iQV70yEndW4e-dkCmtvrUOMmf9O47XMM4Z4to_XDF_Vf3qOT2DvDpHemhBnjczxdWew2_ImS9CCe8ttyrGd6aRFialahgydIBhhOIdVD21G6fbCbKyZhTVPiCMXAZtx7IRb1Es7_MY6w_zUvWwrVbIxAUZqYUAem1CcRfYFqhtf5ZCcPxyZ0CKdn3mMhEFm6YKe-Jo1L5e1JZcOBG0THKHmO9rFonTBijqAymyooHq6ulJdUPudRmxfO6O1mzjmnmfwLJ5AhcHYSU-Hh5LRGNUFh3OW-iScynFgxlA-d_azDgyyf7o3Ks3Cp2gkVzbzHMYGsEJ5S6mSPa0gbs6p4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=iQV70yEndW4e-dkCmtvrUOMmf9O47XMM4Z4to_XDF_Vf3qOT2DvDpHemhBnjczxdWew2_ImS9CCe8ttyrGd6aRFialahgydIBhhOIdVD21G6fbCbKyZhTVPiCMXAZtx7IRb1Es7_MY6w_zUvWwrVbIxAUZqYUAem1CcRfYFqhtf5ZCcPxyZ0CKdn3mMhEFm6YKe-Jo1L5e1JZcOBG0THKHmO9rFonTBijqAymyooHq6ulJdUPudRmxfO6O1mzjmnmfwLJ5AhcHYSU-Hh5LRGNUFh3OW-iScynFgxlA-d_azDgyyf7o3Ks3Cp2gkVzbzHMYGsEJ5S6mSPa0gbs6p4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqm8au3GIxkIjSMngrc2cDKlVdCAuXzdIl_yqvqdnqZkOj66CHCL4PFsBHz1ChiXvU2c4TXBU6Uk8Vyfb4AAmLKbQn53iMtcKN_pmMFfVmjEsjIguPeRhjKV-ToyTQUVk8QrPslXwCmdr7El_EWrT4IwDZG6KASM9HH--Qg2PvI4aJX3587ceipnrxL_bzbd8skArV87sid3vBsubpSAA10Rhj9pTqW0l79h9ckVOPjkHPt6SLMKyPPqlijjfUwUySPi1wq35f2tl7uMAfMxIBwZrbY5zMpT61-pADqANfsv4_dKw7AayYgVD_LclrTJONGHoQv4hIiwLREWMFWq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbGNyJcSGDVbLikY3KkR9W6Tyk2MmJiHG2p1vLeXuLNgdgd6-xUOsJMJhACoFw0rS7z3794_-2W70PJ3iQKspMY_uX2bcUU3yLvX0OFCVJX6wqtnk3vnDpl1qdIt59kjxLt785KbRIJ8foO_bD3kMdzHYuxvd_ry-7mWNrtDO0CrB22lRNIdnjKpQNS0t99Is7KS2xTVkuEPeQwcuGpsjGdgSKqcTZPHd9RuqzZuVGLvATgFsMlHrszo5mlDa1Rm7cxOp1jPguGpqrEJcQGiQUnlXGfBjPE8PXio6qEUS5pTl6mRTVi6QC7vv7uNBaGoFrtMKKvbRpw6c4gR__SUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erfhG5p7n5zVZ6w84GuJS_JZk1Kh-I3BSsjxU8tvTv_5cH8v8dWgJnUOW7F5eJZu5BCSitqEunZg9vJpsA7w8_o9D6vcC0MDvcDBLtMq0jiGwCHe0pUuqdcN3CoWxN2zQjak7cPcJSGw4YGjCr_l3wGifcAjA3d4Kjt4xvZVhoePV63ZeaTKDN-CB9AR8oWmPpox8xyI3jIwZ8g5pmggTI2fz8YQ98PFGeL77GJONGkGIXrBl5RFV8iItYw04ymx2nvzlMnC3V6EWIvjNzSne2hOuC7Fyrw5TYQY_8ILZLZbsaCRiwyQbdDAS6yM8pCMB79Xy_zYigAjjEb5osqguA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq5bEDYrw468VjfchIFb5wCOXQCBlKaMoKUTvTExF1vS9MLjXHPn1WLGDmYk2oHGPeGU_-7_apqKj35A-5ma2mbJGT9EAZWmR9BTwwFe5EH07Xgm6PLfGmstT-iusii5O6hUq6-iWpXHLPBPcGj95Rl2phBoxhQEQr7osn01ne2Pxuvmh26sk2_hCc-Zn9j3_8q2wZmsfhH4bab5QgLnTkT75sO09fZRkwd5pk4oTIarBugnJ5QwS-D-ntzxyNi6CxqKt-nutbrViVcijJSCe1b4rZisIIAncwnzi9sSpoQpopueQfTco5aJ-jmF_hhoo7vQHgtWef9y3HQYb3tgBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXIWoJkhBV4IQ0lT0V3f9wuutuqQzsq2eO1ZsV3XIYfap_qfEYeyRmw78197grQVsh28GZsSFFd_iPf1mvTv6E8IaWcKJv-3TyG92okXa84XLHXXQHkMsXd-QsMCc2ue5Yp-mD46mMUkvbaQbngOh2biBZ5opJb_Oe3n1i0zt6MQbFXNXZCxl_D3KU3Kvm1fGGURpeRf9pJg10jlDmIcXac9_lhPgr63ccko2VSp58HfMHFZvcHaN6x9h_dntu_mNzX2oG1Gj67ZhdRn8CAW4zlKtNDzW8ga0Wgl7Qnao0JcIUjBzDht84ZsghyiaQgoSiGZn8EDmReg0hD3ruIAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAZMGfP9E9B_UCUPigGIE2DHCbTfQBDwggm9yeynI0Qr3dCBPqGykA1uaCBh4DDb4OLcgy9NG0K-exzvHsWnOpGoEdHBU4MZr-H60ya_e0cKTYz7mKwawjJIEbVK9xte-8C4_eqLRBPh3svgaRHPjAzgnhOglx89l_Bp4t8QepzeB02-UsyrHrDgBXf7CRPuhjfOwdtlvcTfwFidrEocfCj8of47332fbtY6vrpYuy53NFzgASJwJdHI-AJkhwZPLNlzUjG4Nw04pDk60C-HX4rbkFX4-No0rLv6GeVnptE3sCxrgM9c-nZgc9Di6PDTAVJBVvDytfWIu7SWqXboeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qg9u8Pfp0IxIaRiUtTG8eKjJ4bq6WIeVMg8FdYM7Ihqiz373gik9yPDkRIrPUwKygZvXPZVZnE4-0kP-0TqxPVHYXd2vw85rQdE0KzUFVuhW_FyxDEJ_yrjk5faipDZ7rvW_qeho1zL-7T0e_HvkPouJ-NL8crtHj2r-3q7OkeacoROFIBEXsZ82ET8lcLBXbmTZc37R25hHWkuZ8bQVvjOd57ekkJqjiY55KcXz_WnUwvD2bfvHkm1dDZaHobBl6hm-x1wQb2hhlg3Zp_LpO1Ljyvul3pdDAr0sygh7dz_h4H4j__5Yzxgy-iAOi9GmdmX1DKuWkfSemXDSpkdI3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkARrsNIlxVDyjWQPHcrbj7c5GMfqF5zYHHwLBAe65OjEA0HJ1-VEuMxsteGk6lmKnxXukrgLt-z3kNyTuwkC0wETh8bnwEX9OIIsOLO21HCbgwMt4rgqZjUp7h1HJWo_n3uRa1b2nSjQs-YxcwB3950sz-rU25OQNzckn8xJjqiy8oW8ySrJPXgA7FgBuA80g1i7uOfDbCBfbLdFlhB1QKjuCoI3gR7-1pdt-2rqF4yeQKepfwVct1JWy_gQfIYjC9UETBF28PV1Yc6WxerUgyuTREBJ1-lIz4qnKf4w20Hw5q8tjpNP0vgepdH74Ln8_YEvdUjNifhA1LcxKPxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=bctyPS6IO_hGX3oC3KloAKObb22r8SBrxnu94luGhJv3UU1z15o-b250k-KO-_49VOCU2M6U0xK4msHjhET_PIKKOcwwMRIfNL8kgEh1-f-QfXxL5fP72MIU7Yj83GOpR6fek0URR4NkvzYmq7be9c0h0Mc9n1SDIVnRkQsIkQ6IU7sucPqRX2_-y2YyJtjIO7l8rEGFtEYWm4AwmsqsujQ5id-fsCBNXmBkDBawlQhKJf1s4h13tLIDe0F7LClfAmjDnEUlFqO4eQKSru_zAsf2fjD5qaU8RVf4xhAwtOa_JXFYi_-hqBKeBwlKtZa_ZI7kX-ODAl45AepDwJ4IoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=bctyPS6IO_hGX3oC3KloAKObb22r8SBrxnu94luGhJv3UU1z15o-b250k-KO-_49VOCU2M6U0xK4msHjhET_PIKKOcwwMRIfNL8kgEh1-f-QfXxL5fP72MIU7Yj83GOpR6fek0URR4NkvzYmq7be9c0h0Mc9n1SDIVnRkQsIkQ6IU7sucPqRX2_-y2YyJtjIO7l8rEGFtEYWm4AwmsqsujQ5id-fsCBNXmBkDBawlQhKJf1s4h13tLIDe0F7LClfAmjDnEUlFqO4eQKSru_zAsf2fjD5qaU8RVf4xhAwtOa_JXFYi_-hqBKeBwlKtZa_ZI7kX-ODAl45AepDwJ4IoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doZbNQ35h0QSbPcXoeBwZMRHHz-sPR3lgYs64ubSoabEAkDHY1fpvy1CmEolNz5XtU2nll_y4oHAgYwRApoLDJd9EZQJuT9ed1AtmcpkxkbpxZ7YPq8ScV1yGvM1xUzQ0nmVI78zNdzd4EX2kxhJyAbyeKpwVGEWPwAYDiZceItDdFjq67I3uz7EuKcmDliaqzM5rfbxsB6kugDauXTfgNt9M7JIlQuv0em-mihGQhtuxQiqr97QQh1RkjRk5VyVAGpYuDr0J2JR9UQHBmSCtPYpR_KhjRh65l-cxpGnULTKunMhGjBrrAej3JGYCqUoYqYe4gjqFH85oF5bgHJ1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBiU1Lba-6h5Y7iPxwPdjaEU5v8zVTLO-PuH8SeofpTiip8XrKmBj3fNuGN50oMSU3vYeKPYJBCEAqDo3euzIo0GSfFAtIY-VdQocrMLCMdv9p258vg1xNJv70AJup7iPNNq8Hz9PMTkqe9i_uJYiIt8pWXZw4ZfIt0c3oeHMRYDkgFNuNMeY8hgKfeFoAhFroZWGh4j-D2VhzqE2K0pnpOxGnwnQMOX1rjCBTIiRl-pS0pfnEuITXPs63EWHZO2TasOvLEjDP1TyBndGz5rvnMjob315UdgLbISmkWq9ZuFrmLJZgXCSsqHR8wAJsxiEbIj8jUdO04usny5DNXS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoXz2j-LB0_9OOZJ8z4qLl4geHRluE6n_C_Lbr_wpFwmoZcBxr_weDxlwc85s-370zitI1zF9gGOLRnvyMbY_UCk0Nl1-qQ3i-82dCbnwbw3DwLF24yQPm0nusAPO50W0dqWXtPHBbnXmZkFN7epGtTOOMYFyw6tMRoXFYiXXKHYEFAlfG3bpm2H5Jj69EVM09lYIoOb5nzz1b_1f17V9gI30MfjJJahQeNxJFenRDvLva-dpqjS6VltLzi7JRC-60qh1JPjzW-JaX-eBOTgM9sNrIYrvAmYIb4K3yYqSaWUvYlyI-2vXfnkF6AAMhBvzKP5MVHc0nfx34qdt0Q-1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbSPpb5sh_zUDq1MEShj2xDmpOsTaXVD4gkACJ_B7PQMiPzIs0NQYL7YKCNDokP0d_-4Q0C8ldOHV4qpOXwf_-1uxfZXlUK_9sxrfNvJeSRlbqVEfTiOFAKczioSnuOzAYbjaQYzPel_RQTT62bvvfeSNVAGwWNgOvHMEiUDu7gZnta3ifWp8pAiALK8qp2nVpGO7IVaHPacy6yZHqy60vKxE0GebBtvkuLCBRXJo2Pvg6caXsowhKezfMKT-SDxRZXPyh69iAaWwg5baLlNIoARjnF2qYd1aFIBZcJQNAOCCn36_Po2wNQVaOhOseElXp3-IgSnE7mkDHV3xRY80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=E1iwFJCEwJawFMrtvHfHovzXKDG_SJSjVF_jTv04q7beVoaVWKTRWEtzwWXDi7z6j_fti-FSdrF0vpYXCpaNRRUVFToqrmaRcZjBH8kNJExN_CYussILbqNVZvF5wxkEqyuNgzXRpcZnHtw68U9jhJv9yVpJBi8NtTddvrgaP_wJ9ije4CabxfDWzbgRwn98rmvACLF4bli6b3ZbfLyIxWwM0iDf5WtQjjkoX1ui8rLeZakSooHGaMf_mz6hCL2xh4QUw2Q5WNEmoiPRsbiHinTaaaHHmSn-aGWXOtgvZP2gD1VLs3-IvpYV6dea1lTYQtemlASdcY7FpxCS_oqUtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=E1iwFJCEwJawFMrtvHfHovzXKDG_SJSjVF_jTv04q7beVoaVWKTRWEtzwWXDi7z6j_fti-FSdrF0vpYXCpaNRRUVFToqrmaRcZjBH8kNJExN_CYussILbqNVZvF5wxkEqyuNgzXRpcZnHtw68U9jhJv9yVpJBi8NtTddvrgaP_wJ9ije4CabxfDWzbgRwn98rmvACLF4bli6b3ZbfLyIxWwM0iDf5WtQjjkoX1ui8rLeZakSooHGaMf_mz6hCL2xh4QUw2Q5WNEmoiPRsbiHinTaaaHHmSn-aGWXOtgvZP2gD1VLs3-IvpYV6dea1lTYQtemlASdcY7FpxCS_oqUtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy9smcKgkMzTmou7clQqlnDqXUbgRsjlMRutx_r0tOtGsA1bpHsWxVvS7Mvp939OTFOoVQWcTkx6KbpyQj-ygvgIkEkAjBuEjz8OOkp7LvAExrmwXcKFgEqubmKBp0BXuUdbQUZf9YsL39ejjPe3kewlQ-bddNsVqxf5Db_IHteo4sJcxJ-vpiNF8162HZ7Mo1rXPdLrQmBi9NVE3iK31gQsErFoUnjdni4mYqWaFxkFS1UQk5CoAnaMmUrRR51fKiQ25jYF7EsMUKsXimcdUOHmI7obXn3L4wrqEWxpMxjTVflbdc7rFUCJL3-k5x06a6RL3Od5mUyb42ntYHLURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS7ORcRiIfNdDpc8G9Tsidq2-PfD_5_VcshSDckKIgyW68F2IJ1E5qDfF231jrKwuIWFZMh3IISDx8joQXvkznqhx0cU4Bb3pEMANFdC6yajYHx1h88PMtSH0UevQdMo4O6_aW51vodLNdZBE41s_QLPn77JtU_SknnNKkEgRJA0zeqEWZgwVlMEpGIbsgWnNy3jzBHbQzakB3jP7B8chb763SEPcLQ_c-VCK3qCTPSzunLRpxYbjUio6DUMp_y1xrBt4F0aSc19u2dY7NA6zylfSeLy3iKGoUWgXuvVS8tS6Ms73NU44lr3N59JNWiEvj89D6DzP9OMBuC-vSyriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkcHnYn5--ipJJfEDyz30Th2s8Tb8rL-yJB_NGHuTtzsLBP5tyu6XNj9uI32YdW4TRo5PPIrs9FdirMym15r6ymMNjSAMa5kcOmIK-mRu5pYPAqb2fmJT-wRqX0bJlgUEGq4dUm93n4IsEonASFoLu2f2aZBXoaPuNRHGLVGgIpDKxKxZZwjuqOhOaanns_Rk4AnOGNTrtRyE5aYdXluXfMuiyRaS7PKTwUwraQB72x0XvE0C1_D9qwhY4yywSQuMmIJdp6lVtn-_fhz4MSTeVaq7Z9Kdbx6j_V2SZ_bfbPP5zHUWEwz9mGZVcYjO8AOhsK3pIFYRGIVOMWUQ7_lHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SN-BdyVl61jYL9X1OgYnpVFJif_NScmeCD6CzyLeLWgKGTEKqeskbu2fyo0vYUkzimzSRlCwdJeTRKBQuriGasl1Ltw4gPbabHDUl0R7vBUs0-pViurFwK5M5U4fFVCbnjLrzHdSEm5shcSbAbPBMPPy4i-c_5IMCq3V_IrwzUscXJp5CQU_rJHBPqvvo_-prCB0mFnvg8a8tvykNtMVA-3jkLMWtkItfOmVnZk-TPGiZl9AIrZfAyvDFVc5ECrEzLLpEuNMsaZAARGucSDy-xCD0-JzxMmz7JVhxI4N0AXkAMAPyseJ9cBF7kvJPxsA5yklatXCHbCShTpwJWBu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0Css2EXpKf-ID-eHT03KsjQLg2416vqU0PynJUgCckMcir5OlFixkIsGTz52E69tgsIatRRTlWSe_IUzH3WPbk_cOpcHRIvDyHiIPRz2FEcy-LoI9XL2nLkSBmzi4WLdvgnfVUBNlefCdMnFLG4_SiqVBb9Dx11JKS9T9W4nrUT6RRVDaFmBRA0PPgWgZ97kjgorkYEXl3mxy9CF2WTR5tZhZcdv4On6OwEkfiBxGJcxUDThEtD8GPiy0GV2BqLJFMD0HpzxFDiOlT5d2MK4N6P1Uh8_hpSPXArfItAjKPC6zBts5kHVt1T0WlQC6Cif8bbuiebPFWDLQgxbJpJTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7XaQqEOwmhnpwOGXtxLXSiNjK8gsWuxId_1EJ54lFkWwsJQct9rsgt41jvFfF0CN2EUnGgSyGfBtYmaayC1VTFSb40MQkO2QN7Il2p6-GjOPOKyDBIwdiYPoE6N4UaaKf-klTxGf43zcCVFiQS5HqX7YWjX2E74nKzUnmKDAA_AjOt4OAVRX2pktPiyQiE4ddaZ049-yNxWsv-admXMKkc7O5c8qQ_rfAOb-Cu4dUvcadUP0r-4ktpyBeYwGskXQAyzuoKT36N6fU5UIDKy0OFpD9EgOUUx_ep3qqvgo2niRcxtAIneUEwmTtsaeammuxY95BVH8IbGsTWWnlGuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvlFqLdfvCRZSS0Q9YRh4sfbt9225wbIdy_iWMkpCYk5eNyOnMwhsxQjWkjxNl3BY2cUr15CrK6Vyels0AwODXAnoy9HcKjxnhrVc67fJvSnbirU6IbHtg2dBoXDS88HEq4s0nTQk78tu6OpMjMR_SFzOfzwpnIwnmEDPeBn-xxvuv3So-G1UdOmtkYugkk_sNCzLlz1rSPlKT5q2P8VUOSjSsqxk0mX5MmRs7g_rGOmGk_pLUmj4ngH_cKaiFACxN-2R_VrCOKIhLGGDh-GqCdsAi45Iwd-qLBz1EYnmxU0jq5Mb0lgROtLv2pUxeyd_mpM3tjwDtnArIqJYbFP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKYnFFxcn-J3DuLj4pNZIivECSp8BqjPdfehHueL38Q4kyNtYxe0puw7bxpJEQKz0vkgNU9lV1di91sxX7pyJEB4aK0ez9CezomQkLB-rQYDwnTnMy0ob6SlV5KcAdB1QfVo7yszMoadyDTJCsMGK2i9UXheUeWPbb711pSRVLkBRDMhqHnZaFKbDqbWx7HMfoIpGZn0sWMf65vC7fhRYny3pYz7gCVWSscLnWuQYQ1UQIiYZ5mPBMjnlNMzHF_pMhrThJ_vgDxJFGoOF9HGmgSf3dALoZsfs-MgzwV7fv79MpBt5a7DI3pk5dW_K4Gqej4umg22m5FplLwWdKtHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=QZFsNJKp_WBnvP4lqxN-ZghFFNHbpK09ob7jBXUf1yo0itFL4YZea4cKpMyRpmEs2LCWxlWGcpXKrsArCDz5SRz_tyxIeboPTsIoZJUooB1SmJxVOR7CXSoZiqvKEyGhMQIvjfyWD1AIKySFTqeT6_aaYOWqM8UihBs6mI6Q0oBNMATtYfV79NKZq5ywZejLIf7F9VT53i1UPHBFim4xaSIG_vfOL-8JukASPT_xdonqt_yY2eQFL-CDBP_lFa1bmAN6GQQpSGVoJO9bvtk2lUWCT7XOs7S4sIf6mKUR0EAUrfvQWhBFvQLz-bTLNu1bXGr6Q5q8Dyehyfrg45JgAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=QZFsNJKp_WBnvP4lqxN-ZghFFNHbpK09ob7jBXUf1yo0itFL4YZea4cKpMyRpmEs2LCWxlWGcpXKrsArCDz5SRz_tyxIeboPTsIoZJUooB1SmJxVOR7CXSoZiqvKEyGhMQIvjfyWD1AIKySFTqeT6_aaYOWqM8UihBs6mI6Q0oBNMATtYfV79NKZq5ywZejLIf7F9VT53i1UPHBFim4xaSIG_vfOL-8JukASPT_xdonqt_yY2eQFL-CDBP_lFa1bmAN6GQQpSGVoJO9bvtk2lUWCT7XOs7S4sIf6mKUR0EAUrfvQWhBFvQLz-bTLNu1bXGr6Q5q8Dyehyfrg45JgAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=CsXd6oR4tOccCC9W3epgIYFnG2U-VnGCV-j8FcILVQT3r06F0VNk2ZaHcTlcAJfwomo45rbFRHwZqB02hnrZToSdlEC8BZHT9M0FWaoSv_IkX_GSnPIYejQryPWJJCXIGLLpG0mgMePRYKUI87QZhxeFxTwxs_JOqKD0XaoJOZ3kPSyO9jlKQcXBani-jfOBVRy2McdpABkmrntnP4T1ZUq7_Y6XrJRkLdsAw4A7zCGarQCgcY0jnS9QCx5nsCld9fiQHOITA2kr0AXQDfH-_ylgr-AGphfQNsZlNVyexLsI4DgSyJsKK-jV_P9S-9x4WV_SxRTpixroBCz7zMhEpHv-kXUZ7YGLZb9UwJ3IszegYGwcqB5pqXZgB5UX3GGWc0COqydTCitQRlYc593hrl2K0_aiT-4vvdSaUMHaimCn900rIBcNoV5Pfn9tEH3NHt8iFMx9iqOtC_GaV2fONIIWj1-ZqlGB9tzDRcw2RrAJMfQyhgg-USnPFVI9skC_lUi3ZtjFvVmGAkBva0-KHfmyZpClIkuB-7rqoj3EGzaIo5iVgOzPWs1m4CJr0dpSWAO0HHT-07LzmbuwDAgMFrGZI8g8CWgoiRVK380hG76DRj4NaDIHD5zVZIHaPUyq2o0h5LZ98mPRDzGXzMElWuwajulR2Mbw_ftEg9IDxls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=CsXd6oR4tOccCC9W3epgIYFnG2U-VnGCV-j8FcILVQT3r06F0VNk2ZaHcTlcAJfwomo45rbFRHwZqB02hnrZToSdlEC8BZHT9M0FWaoSv_IkX_GSnPIYejQryPWJJCXIGLLpG0mgMePRYKUI87QZhxeFxTwxs_JOqKD0XaoJOZ3kPSyO9jlKQcXBani-jfOBVRy2McdpABkmrntnP4T1ZUq7_Y6XrJRkLdsAw4A7zCGarQCgcY0jnS9QCx5nsCld9fiQHOITA2kr0AXQDfH-_ylgr-AGphfQNsZlNVyexLsI4DgSyJsKK-jV_P9S-9x4WV_SxRTpixroBCz7zMhEpHv-kXUZ7YGLZb9UwJ3IszegYGwcqB5pqXZgB5UX3GGWc0COqydTCitQRlYc593hrl2K0_aiT-4vvdSaUMHaimCn900rIBcNoV5Pfn9tEH3NHt8iFMx9iqOtC_GaV2fONIIWj1-ZqlGB9tzDRcw2RrAJMfQyhgg-USnPFVI9skC_lUi3ZtjFvVmGAkBva0-KHfmyZpClIkuB-7rqoj3EGzaIo5iVgOzPWs1m4CJr0dpSWAO0HHT-07LzmbuwDAgMFrGZI8g8CWgoiRVK380hG76DRj4NaDIHD5zVZIHaPUyq2o0h5LZ98mPRDzGXzMElWuwajulR2Mbw_ftEg9IDxls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=HdAZ6JL98ff1EQcA1_fL5vkXmNOxHBjNJqBG6fWFkhAhd3ktqVBmj8lgkjZPW6b7a-kNzCkhN3tjH3-Rh59R0KcT2Qn14m2nF6MQztg1VoKo7DpGmbJB7YS92v9Jwpx9Sun0_vofku3HnQ-wpbVL-eSua7JegurzZuAmg5bXdOuOGA6vx9tvkwEFvJW4wmuP9o9h-gf5Yr29VIfdyL4K3kpTzMnyKQRu6-wZ8KWXvRD4B99hkJdfHMY9mC65NL0CHYtPKqwqwxt7eRL6X-aDVnxzOL4ECsyXk9Os7UVMybx9cOT8C_6gHu9nryfhgCCteMRjPxcBqeCzLUWHUoTuhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=HdAZ6JL98ff1EQcA1_fL5vkXmNOxHBjNJqBG6fWFkhAhd3ktqVBmj8lgkjZPW6b7a-kNzCkhN3tjH3-Rh59R0KcT2Qn14m2nF6MQztg1VoKo7DpGmbJB7YS92v9Jwpx9Sun0_vofku3HnQ-wpbVL-eSua7JegurzZuAmg5bXdOuOGA6vx9tvkwEFvJW4wmuP9o9h-gf5Yr29VIfdyL4K3kpTzMnyKQRu6-wZ8KWXvRD4B99hkJdfHMY9mC65NL0CHYtPKqwqwxt7eRL6X-aDVnxzOL4ECsyXk9Os7UVMybx9cOT8C_6gHu9nryfhgCCteMRjPxcBqeCzLUWHUoTuhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOJyia7E_wxyDmLAA9nGc_KlqxvhJUopO-du9cTQQlO2B3Je6_KGudpo2vUCvAW-p8dy7gOdDlNJ3Onaw25NClFgyC6VEr6uYsIimpEJ-GRSR_I24FpUpW7uDYdGzJgZm7orvdkTcPIxtxqzSrhAgFVUOYJ32dhikQ_F1YCvi9GQsf_soSbuszJ_2UeLQV6bYHdRxlFPpGdbwJFUq2lzIAt3ZIgZbpEJ0wVgLQFgLmWZgqgpXdK3gtI6BWrjzVTojNXDp-KKg4FhIcoCfEQJ3MI88ubMeCn5jLfKJ0s1lPz_aNWkp_qVrROoJkIEPYineZxTqumu7oWDqjVX8650yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjnajWSdrezULNP_HUcce7u00m-Moe77p5fk3yjl3P5S_AS-YK0Kkf7RIGhtl-enmr-kxKZMdgP_DefhGQUn7DqentUnB_5hTsn5JVniSlRAvaRnAGj6HOR8dw6c-FIQqkkIZ_4OqX-cXzn06mGDU7ebXuHHptMdd_aWAFfpxg-hNxDDdoMnuDj0FdYmjxUqVD-LHMxGkYfoOL_ylXeeaoMH520ZCt78E9AXj-MDwmN1FNAxrr0a29_uY3LysmENFonxLAUrCHmoO0_NpJwzSF5nwxpPOEcBkmKRgifMjC1Y732fbRVzdUMRdZ-BaTv1-M9bKm5RKVQu4Xo9O5Grkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=c-NL_4jfu71vBpKpXYz4SJrJzqhkdBYcvu0RT3Ern4oNvum7uYp8UAheSNO7IRqrDuSl3bX5fxh0Ao-osuI65FWWfJWi66jiB2SjbiIkIM6QS8aoCTvtXq4YUGmD8T6I3tMcJQ-mNH0NWvnY27RwJeOp_TChcQ0guBeb9DDmBJuzdfudNQuMF8su2u4QyHKFXBaZ_Lr8i1CUcAK70kg7T5r3_QXWiUXtljZxc7rGQjQL1TxRayAMva4biRgYoSvfZLmSCvffreQc7cqZhBvwbXyVYSkGnSX8r7V6JqPEBqwLurIqHqjVCJtQs3WhNzVW2QnlgHx1CMNP46tGrvdKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=c-NL_4jfu71vBpKpXYz4SJrJzqhkdBYcvu0RT3Ern4oNvum7uYp8UAheSNO7IRqrDuSl3bX5fxh0Ao-osuI65FWWfJWi66jiB2SjbiIkIM6QS8aoCTvtXq4YUGmD8T6I3tMcJQ-mNH0NWvnY27RwJeOp_TChcQ0guBeb9DDmBJuzdfudNQuMF8su2u4QyHKFXBaZ_Lr8i1CUcAK70kg7T5r3_QXWiUXtljZxc7rGQjQL1TxRayAMva4biRgYoSvfZLmSCvffreQc7cqZhBvwbXyVYSkGnSX8r7V6JqPEBqwLurIqHqjVCJtQs3WhNzVW2QnlgHx1CMNP46tGrvdKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trKOKLDQOT6UaL4vl3xgie3QlR-u0vCEmt_ytIvz0ab1fHHUF0KzamACPRelia1uvt-X569nfiyTHnqai_jUaBGRQclRGfuenYIk4B8ZCGi115LW6MOicSI3vK60JSBwiwm1mt1QMs5XU0hoC5ZUMlpzb9GizHEXiigG3bdVemUy0pSELiQnggjUomOWN5o9yZpydaTO4orOCryFtv1iYAM2tGkmBGBYOJAfhf6FH8uC1TqYYbUnn30THsToTDjsFtvSjE_T_akglAa0eVI-2c1-A-BDLI6yo7zJ9wrSoVRA1qJMBe4tFNOhL5DcawG-hRhgNTQjzF-3inx28uMV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8oRs4boX7vRDnvTbnBPjfH3JGrIQlUif4wwrAgsufF8MCQjEi8CDHDVmQDUs3tKf7UE--dZErJDIiwZRnQRLvnuiCaL-GlanZKsqHb5EUU7-qtrRu55xTmES5gmBW0qrT5JtUo8RHnj6MSqDgOwcvxPTctSTbY-Ata638Nr3Bq8sTWNH2qbEdMbGOSNnkhF3I0iFygYRNiV5y4tGPgU9GaRqvxSPm_m_PHW4Q47uwP_NrF7q_-Z1Qs5CRX4qNJTklkyJZX4xsQOu9MWE-5Pu3oMDRkdfoiYCryodZp30FV_AQBmAv5VOIcXphfWiFZAgWoIxlNDPFeDPMXtXnCYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIP9DGb6L4TIEyZQgAkUbGlk4DkacCuE0bylWxF1fWa1yCuxwPrEkGgTFO_FliW39dem-9pKA46ok9cQ5Ah_7ttfqxdd9ZHZlK_TC4JF0Ir-JnpW5oaQ0WKDuMAhkkTiAT0gUl-l7M_War5PhIjtmzf3YKeXUa45yipJr6xgdANknG_-QxRlw4Jw3KPeiJoLyH7hLn9_23y3jVfCYOMb1KIaCFZo7GnO7-e5sYV_UgPGLAMhK3St0EJKEu3ibjwvy-poGZGeJFARNnaFUA95MKOxq7G_5Hu1cyQQUMD4wzLVhDQc4byygLxPGn0TxFTrQK3sysluRmI0gqNfOZc4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSYHR9m44Nz2Clw8FaPF77fcvSTGo0OXWR_NgRXzNLEf_9XqqO6mp_1MUYFKmoX_tRxpURw96RFrwVNdDLkxVEBu1WNt9tiVaTBjj0qhuUkiZEKI6HrNniUxB88_HjnKf80lTWG_YPLdfdpXnsiwREZ2ODt4V39pWCDBxb_PHIxaanGpf7Ci6r7xWF104UmqT2PCq-RYin2cxpDfcNFsa1GsGSyHGpq468D04xE8JqJo7QIwQNlPv-II2jV40ZgedehHLIxRitNtowO6hYIcWLZN1jNQ1kZ4rpvW7cvbMDybYlCgRC3XRzWkwNSvq_A6zWDNrcW56GEpkpr0Q-Oz5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8vkofKJ-V84FRK5RXxixtXEmxaXh8g1hoAlm0c0T8reI34U6El-3HgTyp-Nhx26ugrTSO7iAkQIYYRwBKdzuWuTbJgn6GjMyih8Ep0MZppbwDCZV0rmK466iAxLonuHu0UJ4BRGhPe3AA7Oi-BRbfJnXCX23cm3p13XgDGc3nH91SZk6__5DthX7fVTklVI1eTyO6qNvmiw4yK5ROjHKm_cqg9_xYgRYhJp3_uuQAOz2rgQJEZiOfeh02THPgmRoJpBMzKLARJPmCPuJ8rShz1SuSJVpHLvOmx-dnLDUfuvZc-02NKSIt2jTDVvs2Rxjr8ZQ8TOevbZKfVNY5FOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEmPNs8R_g0AjFyGjMiuU5uotWG42JVgUUbnb9sbP_ccXgO9kH3-_CkuDTfpC4qLeOLnqk-xRhZFfLLSPCx2kR6howYzuC9q5Tu6i2Kk_MMOodMrpfGHLHVHvk8DMxzlmNZWbVzLEjvSgfagQISk6D2MlX5uGlIBjLa8AMWHvUBXNvFMRpHN7i7x_lD1ynVbebmdl2qIlldICklAehTlKcBEMg9nDZPE9ob-DiuwuBIO1tXb4Z1pgxpnGi6uoGjcBp-WyaRvCv8zUyroK9zecyPPDrJC5r4JqLjY9sBx8D8b9T5YTmhcg5j3JeIh4aAtxacS5-npQ4Kcil_QHHgB6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HsDi4ldn2fLRvWHMjn_KLds_nwOSLgu3NOm36rFT1JEcPRmiGwiyY_bCU7R4uTRWWeftToBJO_wABHXzVjrhZdATuq4Sg1jhH-PzsfHpzRFtMhTRe5pHhNTWurvA_JU3SL8kRlyic7Uv8-Ht_3tYs0HexJ3jRU5iE3nuIjCqUp0kESTafsm65bLwSOetqh2NN6mEZQpf0q_IZj6dXR9UqMNplTIV9vyp86uFWFBECgZJE1fYE-zx7G5c1WNox7-_z19AY8shr6GsJlEVmTWn6R8NHYQ2js2IqASXRFVjRkbo1OV6u2UAs2aRLmCIEWCCQjkHLIgEkVRtoTV9xZ5NGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf-oQhj7sa5mFWJqaLfj6h2Mp1t0uuk95H5-7FkSQveMVY1qtg3OUSF_LzY8N8AZsiGaaJzmOJHc1sOpa8QVYALR4QUiCepjuorSNh5ozqDeLhbjS7cAL0gtL9Ft_cKW_1EPZRltw170KQjio6rGz288jSpjo38FRgb-rfuyKBaneMe7-Y8zSZPzhclFG9TOKQt3nv5rX4umqrW3U-CabuSkMgC94IUDJpdoT6DpH-xg55swZBoifLOBEr6g3Dxm-lu4zBM_YrBMalydRl6mpciJyugl6e1y2b8uX7wLXfhIRdLSYTZgo1yViyxj3zVb_TClfHRc7xo9TQ4p2KOBgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfJEuz9OunuBcpEdPQyQF9dqOB8nZisxpjpzf5ENhxoWB_hBRk69Zh7pOx0waw0ATOOCzANKTGSoIKQmH3baLYlBZoHhMrbcRgPTuoT3BMF_WumW-hbbHm8SxnRGGlFquaZqxwLe0cjdBsJrRizG616fXlQViz7GD8vaKaZKMaTBna55b8VYUoIeW7eH_VuqxT4XfWP821qdnw7pVBSzBzVs0wdlEbthotUXqwCAkwvKJ29vp8Rha47Nw9JrzxIeKSHhtuFdKw7RlW4ZrWZOW9YgL9K9WZA0SmSS4Us6wkvfQcDGthRTqzhJ0v_12CrWhoaC64BQHVBhuxM6lzHeJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=RqIPmoJUSYcWkCGjUPV4lQe8lFxEJhaFoYW2by8PBUqJkwrrpWA6goZgwcqSATfZDX4y9S2TluGfGEgChF55AfAAKceR8IZCPnxc70ulA81OqsLQlUlpX8qfzGBht_33eypqM6ssqhouS-LGn__XOmKs0eBL8nGrQBrXGrfW98PqKbZMsA_Ug_qMgZIwwjD2Zc1T94iMCvEiv_gT3e9FWD8S19cY7tVfFnpheHSsIPIFwob_GcaCYjQp-oHO9V40-f_1I9pXH2cIgslUVkoG052TJjGFpxAanyNILJtR6-KgmVhdpUckKwEsEmq97S7NrvVRxd2GfbwtXBm1FglfdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=RqIPmoJUSYcWkCGjUPV4lQe8lFxEJhaFoYW2by8PBUqJkwrrpWA6goZgwcqSATfZDX4y9S2TluGfGEgChF55AfAAKceR8IZCPnxc70ulA81OqsLQlUlpX8qfzGBht_33eypqM6ssqhouS-LGn__XOmKs0eBL8nGrQBrXGrfW98PqKbZMsA_Ug_qMgZIwwjD2Zc1T94iMCvEiv_gT3e9FWD8S19cY7tVfFnpheHSsIPIFwob_GcaCYjQp-oHO9V40-f_1I9pXH2cIgslUVkoG052TJjGFpxAanyNILJtR6-KgmVhdpUckKwEsEmq97S7NrvVRxd2GfbwtXBm1FglfdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=mCfkPvMJgcOvW0OMgs0V6RsWa6T0Ci3ARvqvw1wMGGtJujTw6zrcmwaOOBXsTrtIpLiPbO6Q7sXPrRsxIuqW9tXbQSfviMaUdH0NC4XdvyXk-hz1bA5uhkFb8gIu72YALODh8I-6WSFs23C1jehAyRq2Y1wj-1x9CV8L0g9evnp6qB2qfh8XRGyxcYN_p7hE_og9C_fBqixFpsYeRSKgRJcezlKlAdA0ccdmHq__RFSKub-C9wnrqzwiB8rKaDSmX0rKrjxPu3ZtD24Jm0dRST3lF9FQFh8m94dhanvsha6BL08bEgmTx-lzM-o_mfGpn3reoMpyClxKKPvYkadCHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=mCfkPvMJgcOvW0OMgs0V6RsWa6T0Ci3ARvqvw1wMGGtJujTw6zrcmwaOOBXsTrtIpLiPbO6Q7sXPrRsxIuqW9tXbQSfviMaUdH0NC4XdvyXk-hz1bA5uhkFb8gIu72YALODh8I-6WSFs23C1jehAyRq2Y1wj-1x9CV8L0g9evnp6qB2qfh8XRGyxcYN_p7hE_og9C_fBqixFpsYeRSKgRJcezlKlAdA0ccdmHq__RFSKub-C9wnrqzwiB8rKaDSmX0rKrjxPu3ZtD24Jm0dRST3lF9FQFh8m94dhanvsha6BL08bEgmTx-lzM-o_mfGpn3reoMpyClxKKPvYkadCHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQec5_Ylajgu9BREuSf6ajzL5R45hZ0mA0EavcTfmb8iYLXAkMYtFBPOXFomAtJGm_K5L6m3DeIR2lysOht7TScAe9p6rJrhrTQ-CL8wzEfnohE3FPLEeSoKwabCOpvVKyPtyTO5czN-3Iv-z4b9h8bgv_aW-IPShA3iFjMzdmX8o3yXKiBBF9_-8klck3AbNv5cP7brNFe8b30yPphPM4TWuFyl3ijYbI4wzCGQb7oEz7RwXQpdx9baXOSVVZtCmsRCkgBBaX8sJYrDdi5mwVYs35BnEeCn6sFHpuqgch8qZJywGhRDO5zRYeoPkGyL-xLUzpYPJSriJ4eWfOBoVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr9dxk8X7bczGiUtTpdKuhwE7Z4m_r9ly8gGCK0LTgcFJIDEObTLLf49XlCWvVqZLNrSdTnCjxRhz880RqEY0mUZwLV5J-KeCs88_AWITMsESw_vioStA13wlBuxqsjoXhpAuZ_KassfO9WTe0C7PuprlIQo5bjatt50JZsSppdnz-l_-b_aoI1A4AGG_JuePgoxYwVV7g2lWJkEaHTpdzAym4gxzYABrOspOIQTqmdWtZ2rmtVWvzXkdxlMiMGICOQTXi4jVJid0XxZ6vJd1ieemdKaUG1fHv_2NwNTykOk9Ars8q7DdmOZ9HHiFoq4VrrcdO1xknPjx3sJqsmP0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=iK71pBGQJneARskBv04SXCo66PYAz7GOADuL8sjb6r0Z_0xfhRM6jbQcohchKDEbBoVtecBLLmuk88aYRkjw-jRZ0bwpXqECHRD54MtNZqNeYPbUXFH2opwdKHPQzwZHOnVWQVaJahtrrkwU35llngOTKN_GZ_wq5Xd5G3O2v2EzQq7eZuhnr_RIs52wPg5h6lIL-MgQ2BeeueEJwHW1k7t1GiuCvdsLs-A-yK-Xv8cFWrPrVQnjs_CpTFU4FHkJwryb70MMQQYSfoCrBy7riCZrh8uuaZQsnfMmpn4CTmNwn5A_cdbVVWU7A0ceEtTKb8UccvV6773bcUwPs8pE3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=iK71pBGQJneARskBv04SXCo66PYAz7GOADuL8sjb6r0Z_0xfhRM6jbQcohchKDEbBoVtecBLLmuk88aYRkjw-jRZ0bwpXqECHRD54MtNZqNeYPbUXFH2opwdKHPQzwZHOnVWQVaJahtrrkwU35llngOTKN_GZ_wq5Xd5G3O2v2EzQq7eZuhnr_RIs52wPg5h6lIL-MgQ2BeeueEJwHW1k7t1GiuCvdsLs-A-yK-Xv8cFWrPrVQnjs_CpTFU4FHkJwryb70MMQQYSfoCrBy7riCZrh8uuaZQsnfMmpn4CTmNwn5A_cdbVVWU7A0ceEtTKb8UccvV6773bcUwPs8pE3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=AIne3Bmdx_VAFw1Ro3YU9mm5QTrc5dzKWhwwLkCopD9EMqeJTarhf1FgBdcC6AVUAAh4deN1cOBaMQtLhmsDLXLMYZFOGO_hvvrkFhnJEo7IW_xYI4vfCzRPrrzhFtMs08koZ7IjKHVmksK-wesQ_buH8HBvBHk4D9pGL6zETCpaYf5ALkfSTdSpa3e5ZBNJsEPuaPp0kWDEwn_Q0QUg7VuivxSCyLeilF6qhk5Q3MHolrEPrliJqtAqmDaM4MYxj8-e9JPO-2hy1Rv_H81xwAi7bwI3a_RQ_7EA8KZg85MH-RBEXhfhqOjRAdXqqMjXg4sRPvlr54jrG4uUk7DuLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=AIne3Bmdx_VAFw1Ro3YU9mm5QTrc5dzKWhwwLkCopD9EMqeJTarhf1FgBdcC6AVUAAh4deN1cOBaMQtLhmsDLXLMYZFOGO_hvvrkFhnJEo7IW_xYI4vfCzRPrrzhFtMs08koZ7IjKHVmksK-wesQ_buH8HBvBHk4D9pGL6zETCpaYf5ALkfSTdSpa3e5ZBNJsEPuaPp0kWDEwn_Q0QUg7VuivxSCyLeilF6qhk5Q3MHolrEPrliJqtAqmDaM4MYxj8-e9JPO-2hy1Rv_H81xwAi7bwI3a_RQ_7EA8KZg85MH-RBEXhfhqOjRAdXqqMjXg4sRPvlr54jrG4uUk7DuLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPon4jOJ9ShFcKlgL6ZC_YJBIoVmVgH5oEK-IdLX_9pA33Djnh5CiKE57NrK-EN6uMhkGJP8DRyjlPG_mcVetqIlG5a9xMmHdWmSp3uq6Fd2_gGOwPQvlOCByq4b3HaoOE3-FdwR-1VXpxLP0IUc9BsfwPiSK8W-VA_ECJjd1lKSF-FNOI7l64cFup6MCAymK18wgJqI60r_0NaadXxxTr_4JhsVchnuwtXboOhV_HXqe2jn09kQtD5LEV-MwSdCFK9-XYR3RP_NynerApPfR2Pv7ULWIqlWaXLQMZSLxQw5F0-r1mPTGbLyPSRVuzlH_1H39-02TZD80XeeYzT2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFDkO0hn99yv7RlwVJ3YmCaYSJuIBZbRocGZBThhD8_4V18Tb_7M10jcR4v7XsixoSXcedKPS9U8xX2RpCGCfo1_edgTk_MGK-gIHXpS9tZ6WZLkQ0jCVsea96Xrcqb26AENQjuMLxrWB2OMHqg38I4x9sMbzoMBFbikNRtGlU2HJjCK0oDSIvGL1p-Ls2q-MK-Zp6MwrXEoYzgY3qxd80z-X3Gu0izTlcZJ9LcVBmujY3f1Kg6oiQNwfbSQyFXxcnSSZ2_zARdeQAv7h1mF61qbjS0nSOpbH66LdJrQia_iKjvaShbvvjfk4Ak4K0l3o4EfuXa2PtEZjeiYMulf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNNvvd_T5gNjznEwJANxssibMfJJR-MEgp1nqqG-V7xC-T_U3m70ExSGIJI_nhd2X3v4AUafmEigYVQ3XR6Igpwa_XDY9EeJKTRWD_3EWPR6bH_qHL4g-hN0isE6iUY2XQ8Fql3XgAYYHsIVSz8HivmdbaOy9fbYpjjLsLeBPTEgMEqRJGmUDHa4onNXKJJhTuZvE8PvC8VqKG3WWQ-UacijUxO4W0nke7sk2P7Q6NgEHwb-3t3uzxQK821m-7HtOxJCuFJj_LfLA7f7IC7Jf8ymOPu9HIYiUErhwJ3Ya_WS4erJmc_95j2AwbpJ1XIbHCN8oCLgTbCyfW1ce-U_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smP7aoepT_K6gzFSVL3FWb6lPsxcEJs-O5h_6mBzruY-0bNsZqVqmxZpZc5xpEvPVFGkHvQm1XhibwbJgPELpXXZhrlRoR8M_gaRpIG95cHBWKC0N6OKSo50H8Ib1JYLEYPrYhjGtwpu7OkP4HWw2wylO55m7wNY4EleDtBh5gq5Jb26Me9jf2qP_nchzrE_uPVw4WIr_DD4vklVfnfgaH9AmAcvwObdtgpepxCe579WCSLAs0rzUcQ1UKXpDwvP_EaaWDOtBUTd9n5jPRnvS0Q_13h8XD4ngY2QnFALVxif6AFSOTUmELXlIeODZ8Temb6Vm_XPC3efTkMi9OaC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6p2a1Sn8mKxxy3rUUVgXIepjMlcz4t4KrYHRhGufOv3i41WfP3Pdjnt7C4F-V6_zJShXzSzGxcfNbtr-41X-bxAmaKRyNiegNRdW_VJ3CpsV-4cHtfWZ75fKRIZtKeeLBjmz9U16nK6tuBCdEj4sJ1-IlhpV42tGE85vQj3OaFX5QRJ-63GNW-UnYjIDzCCABA73V5J94bwky9TnpMGgrJT0jNsB-npiewlBt3mcL-bWMXE0tL0EOcpTA70oHzAzMgLRO2dEFDi2E-NgvGLW-p9_ZxXW5OHH9yBjjU_uGB3zPrgnsXmPrPNt1htV3QwmCb1WBWCUjho4S71yWSGbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYbS7XMrbmoGeGA1PsEq3UE3nPf3H5E4SdMEfLJ50Qy-RcNlGe_DM99MJsW85u87_nUIY7pdmcHWqr_Z16QD7ivW_2p3nsZVCF3gk6M5QgKrdqS43gSVDpdaz3f5CeRSRPXLX0YHWsHPzUhYwelVFjSu2YD1dVFKRxpzuDXZGUYeHubDP-MmxSwPc5AeJa7_1mQGEYtW7-V6ok_Go9mO_nGQKvGg35fMkxYBE2K7c7KFHZRn9E8foNdOqev1NDh4cWzcShwP3O5sYWU5TSugk4ZVejTFHGBRfvJNcE0a8DeL5RcOP5hAb4BlgvbqT-Y4AulPFHIKp0S5anluvBhUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWyGr6B8Vcj7PHP3lS1-8WqCJJTHDVEKibrCRowKwZiDkNiHrNj0n1d2Rh40zmxTOsdQj2YWP0augwWLvuc2FIgiM7_nObYHemiUxiKMl_3lnC5ZHXums7vi4tnl3PRW4k6Owg_5Ap2u9wRu8VDFIAiZ6PztvaSdPPfLHbdU8fDo0cNVBHg3AV48S_W9VSQshEDVUU6QHWNFgLChT1DbmTB1ft590J-eg3btIoueXVgLCZFSBzbe7fwCXdGagwYpakbUIXqd5sAJjO2HIO4QL-fCszoIKk5vmSEuUXlE6RN7ieJjJBZPtd8uEepyJY--UMPq1sa_8xlMx_v9eF1GhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fkMOQ7D2C1yqZ75Yqv6tTwu6oJFJcJYZY1UPiDjgmUtUP8wHGHfjOOdhqZbLzbFzFFDGfKEaMCQmMFcqpz-mntT5OpMeKdXtU1F6iWEori8bb6raninEpB0mAQ2HI2eal-vgAaY23pHrH0tFgKTV393XdBO5EeWKflvYc8Cc_JO0HKG9KJwGcvyqBXKmYT1tGbQtFMr23i4GHjNC2Ta7jIG-6z1SvJJYA94XRNHoOdt4ZQmzliXGOENFiUDNNF2r90IhPVnitYoNJ7Yk66R7S0QgmT6g3XwRV0E51lAzUvHd1J6rRIsRks1oT-MPNMgKsuemP0u4n0txbaz8X-ibeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2YcwnYQgLlGrf0aCBq-_PI6jGJIHCYlIDZvI8BzDSZ9nZFhlhbKAXu7_sMwnB4CNGgvDc1E4pUy7dfX5N5-TsUhh40r5e_9oLbdSd9AJ-6qSIOR3043zr7Mq7GVvRpCMURyWX5PkObcaTgRrIshxpHqHPwDll3cSbvJ7Err0P6WE3bqWJRTYeDthVwSX8cj_SbHtg7C5wVrb5__2xAsxOXEpN_oeu5hFlM5yXDXTRLdVeBe81Bf_Fy3janDeOt5nDIaJOy7D7LXYl5IPCZczVN6Hw39sjsCEDNUydUGtDhbL0ClkxsOpmq5KNITb76U0eOENug1OQd_cZm9xSY23g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz7cmzNA11-TB9ADNpHUZd7-M3doCirmlakz6dpBreAczOJgG8Jjwfmgc4Xj-o6i1OX83OPblrpMV1jKgsddy6733ux95RgDyesuIO0zTubaS-unrhe4-w0ZcLSqVh3eXMqGXlKLqaCGGtF814tujwii40KWIRJ1D_vgW7CG3QeuufXZXwd7-ZBq9rqCTcWIGuCuWdeecTGEogOo4lYEjVP_peu1TiPEDZGU3ZHiG-slXTXByrWlgRbF2DmM1moIL7XYVe5AX2zG3z5D_JPLa_zcnkDkz1Lf3JoXdhmD7xUroCYXBhpix_hLbDcQRPcGO6D2GjAtoZmmr7fYeZAveQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6IciVQu9BOrulTVIfWqNA6hBA0TKLwM_HjNoqtN9ljdWj1Y_631pkdMoxsqcCFYQ4AMFoOUj7EHEKUT65hvN9ia8RJ50CGN7feJ9XAaifL_KjTQ5B32sx19zzQpDFP5kihHyBxJBKwOIyTJhD8iJ0eKdpaktu6CWnZhqwXV-Pd8NAz-r_DYYaZ6bEQG3tkoj7oAWILDdwb5eTRX8wqkw4d1UZ87O84Yj07jtdBAB02ZaBlmkrLKQJjo1d8Z110yQAocHIGD8oI4K_GcnB9VLbHS3h7NlfgfCYYddbeeHZCSY2cnx6q6P49aORtQKxgC7rnwRb6Qa1PkBCFD4v_aEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=bhnGMIbwIqI7fHFWUtLYtkVRqfoz1Fd32aY7UzOvEZ8IARoRYTabetdNBDgHk708a5TIIlam-dWXAYqNeTjFACwTHdYSZacSM1hGKOijkGpDbFPH-CrdcJ83noVCytBmS6iswCSGzbPsli5lvipNIbxsMGW1JwRC2oLAkZBUh1tGNip_zRRc6OcVmTcErGJWo_lTEholayJvF_JwntCMSnSCYtGbc0hoqAq7Ft1VqoQzCsVRR0KkX_9wtaniTHYultM0qVpbJN8v5Ue3dBruHv-T-SCzDz9fizAqfaY7kfpNBROsYr_3oSHTuAT1mDBQjf9N685ObTbRIIqlJXlwBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=bhnGMIbwIqI7fHFWUtLYtkVRqfoz1Fd32aY7UzOvEZ8IARoRYTabetdNBDgHk708a5TIIlam-dWXAYqNeTjFACwTHdYSZacSM1hGKOijkGpDbFPH-CrdcJ83noVCytBmS6iswCSGzbPsli5lvipNIbxsMGW1JwRC2oLAkZBUh1tGNip_zRRc6OcVmTcErGJWo_lTEholayJvF_JwntCMSnSCYtGbc0hoqAq7Ft1VqoQzCsVRR0KkX_9wtaniTHYultM0qVpbJN8v5Ue3dBruHv-T-SCzDz9fizAqfaY7kfpNBROsYr_3oSHTuAT1mDBQjf9N685ObTbRIIqlJXlwBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqSutt2QeLeITKxMAJ8FA1zfwTRxwKHcCZcX5ipJfqYDJvRzIPjVgr1xNm_54wWk7h391kiQxfqU0wU69rT_Q_GgREFxsAXAhgTDNYq1gKsY78GlM0_nVf4NTvqgroOTDI_2zDb2q97VNbWvNXplTk7CLQKZSjWLCkXm1YeXaEWOC43QZ0ZE50h3wzaYbBl9fpDoTwkaTf0IP0URnKc7_muZiz1x_OlRbvMVPedL73foG3YTBrMbA9t58lUm8yPso2TXQoX4kwT9BlLPOmYf-qVeG7CGDcOWPpldn-maBLQNq83A--ZokyFHXwrFiJNGztIGVzKQfI8YQt6oEYfGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=dVlBQNdA8QxYoiKaZ-LZL5DjQSg07jjJag-ZVGxEuSDuDy1_izHKYPl_1b2lkokHpFUUWp4qCBBNM3nF-a9mmXwr6WK1dRTvDU5b1iH7D-DnmnXc-5BnHmNg86fIukkRyJb3OrkDLECS0pLeXQ7Oy7g8qVuNT_Jr9o69IGFEFtw4qnC9q0J-otbIkltYp_KrX4w507oWL4lC7ej5JyOwNE8t82Lq1jvcz-Y-NMai8xQIjJHaHAM4eM98UKDBpd2rihqw_UEDoXe8t4MzWuUhyE348-p--kyyOHaSnVYTz--TMQl1ZJqrGXiTbJUuWQ2EgX0Y5RYyy1YP-z8xMbYSaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=dVlBQNdA8QxYoiKaZ-LZL5DjQSg07jjJag-ZVGxEuSDuDy1_izHKYPl_1b2lkokHpFUUWp4qCBBNM3nF-a9mmXwr6WK1dRTvDU5b1iH7D-DnmnXc-5BnHmNg86fIukkRyJb3OrkDLECS0pLeXQ7Oy7g8qVuNT_Jr9o69IGFEFtw4qnC9q0J-otbIkltYp_KrX4w507oWL4lC7ej5JyOwNE8t82Lq1jvcz-Y-NMai8xQIjJHaHAM4eM98UKDBpd2rihqw_UEDoXe8t4MzWuUhyE348-p--kyyOHaSnVYTz--TMQl1ZJqrGXiTbJUuWQ2EgX0Y5RYyy1YP-z8xMbYSaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI3ZKtmvLBZXYf6wtgVBJnDkkueAbMfR0AYaBHIcvtuu_xwpz9yGEJlgiJD2GQTIy5B2QyvIBkbKd8x5iJ1GkbRnhPVhbcU95PpYW-juouCbv3njQjHE9BrSaZ2z57CG6r6316NTJ0tFEPSYvjm2v15WIdKOeFUSIka_L4JvCQU5A9BVOOzk-IHm3AM0K0-z8e6OqNxmxKSLsIGL_I6tmIVsUpghKd0KPImC4tFhbU_w2cqLhWBWKmF2Bq5OeGI-FpOcvLOuwYKRe1LuKyrs07eQA9GucRZOGJpmNN8Cdja62KGn_eHlfZVVm_IY2Py37D2CuHn5apiOqmOdGW6fdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qasXjOuTkdlPD9KngYTGI3WU_Hbge3YHanP-1xwdq-ITidgwWUjXn1VayvQCKdd8kHZFX_dRMRH8-mcs23udAkwvvV3XR38-GUczAk1n28a2GfqGwoQY7D7JbZeh5r_6SzrU7ci6lX3t1uBYfB7X52yeudwphJ5qF88QlQY3AXXR4wy_8soizYmEYb53YUIpOMnx3CUbIwUPSd1OP_e0RWjkRI7yYZSJDP9o2B-z0WFLIYV6KihKvXTtNWq2dt7RYxyXwW96iG04fHVfBAoGcJ83f5JNWLwTgukwqCGEfIN8vThHTVVBdms8qYXBwGMhGyUyhmwlZJOm9mpdH3QgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn6Kk5EBzVJ_XI34Swnm3Qxb7C8HRJA4x6g5uzpSrcF3g6a1BU-fQifmt07PbsQDnlGn_i9wLQQpfGCf582RW25UgCaWVk5zl4KC8kwBk6ONVT4Abp1dtxtPj2K6ryAidbAy8pTPo0hW8k0B0MdpfATFOGb1zHWZfkAOZUvhSP14KUAkK27WWQDEscInrgIfTStUts22WWjquG4lTEhh_XxXCJFAH9qJbpObxG7nRyiZ9sCQvjKp9dw_qPftq37ETG_SLMgA-wdhskHk3vJdBCKgyVMFfz1t5yUBPWvpEOqBlqVL_9RAQb4v9EfkDZwEXc5LRDS8B0ChFxju4y8Q3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slTyaXPj028zoPx63Liksq7WO5gAfbzGF7jNvouxatrZeIB3PCpa4QVKXqR_ZFWj3cCue2UHo4pyGQn68OqyIZVeA7gQmBvq2rfRWGt6osNwB7p8tvKZW5uut882KvBtuxTydDoKZ4QEK3e_fSYQ8pJ04q8_muD-nAXxGHiOGj02OPJKEIyCctp7Yq_mN230m3YkHZ2Z0xbmgDaTz4DR1IcsfMdYMNZNShCaN-7WNEF2FkPrfEU1dLFhz7nJ6amACc5YVlIfBxpNGLnqXzmCtAxSJq0e_V2r0evK7OZhsiXtR0IKGWJuQ0dKVH5ORwGudLOC2BCu--YipnFhozYakg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
