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
<img src="https://cdn4.telesco.pe/file/Y-xPyG9rqL-hC0ltMCK3SbjmOcov35wdwwLIGE56FNxTCMFRxit_kNmZQ9-u5Ht2NEIys3Sk1mSUf-vDwkJJjxky031IVgP-h2lI2kcgvdbuYRAmWrCa1JohOOlyhaRBRo6iZtoMkwCuKhzItLGA0qVho-mbSgbUNnfJrlw9_rCIx70YVBAl-JJGIrOIdvDEVdLi-COfKHMxYCaFsRAtCzKscN3RG5LL8p_0OgsCIkU5LUQOrMQ0JcX5ECnbu5bLzrjV7tuieXqg5vY84JkXGGpGcfKLWq5aGKYIsu6ZwftNiXjEmU9NpzjsKS2MBuq3nMJJHPpIRhKGeYqXmtSNrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 178K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 20:43:08</div>
<hr>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=d34cmd1hk-O-BOEjOTjXxYPhI6mLN29sCVT5vqbC6d750isSVHbtkfNUB_x2lmvvERgcUl7i3D0kXGR4y670Y0UC6aDFtsyl1V8Ietz6wwBwSD3WrtRBZuZYFy72_8mrpzXzdeVhYuFDHAqVMU0-SN6odCMIN-O0gWf9woAQ0SJ9TKI_piVMayYDCehDaVbMod0GPKjgEwsaaEcyu2d_uF5mELUQbAIdmFxmc1fYPIAAYUPKL6M7Zb4kVO3syU3FAQlvEAjem7VuVNrA0bhRNmqqusuGUBVcX2EGObWA-6Zg05RLpEdsoAmW_1EsyFVXf5jnaBCyXk5_HB5b51EQ6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a2c0be9f.mp4?token=d34cmd1hk-O-BOEjOTjXxYPhI6mLN29sCVT5vqbC6d750isSVHbtkfNUB_x2lmvvERgcUl7i3D0kXGR4y670Y0UC6aDFtsyl1V8Ietz6wwBwSD3WrtRBZuZYFy72_8mrpzXzdeVhYuFDHAqVMU0-SN6odCMIN-O0gWf9woAQ0SJ9TKI_piVMayYDCehDaVbMod0GPKjgEwsaaEcyu2d_uF5mELUQbAIdmFxmc1fYPIAAYUPKL6M7Zb4kVO3syU3FAQlvEAjem7VuVNrA0bhRNmqqusuGUBVcX2EGObWA-6Zg05RLpEdsoAmW_1EsyFVXf5jnaBCyXk5_HB5b51EQ6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازهواداران‌بانو تیم‌های حاضر در رقابت های جام جهانی 2026؛ شما طرفدار کدوم تیمید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/22558" target="_blank">📅 20:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvwsuaLh08N7N6TR8SS4-ziCpQyS1LYS3ggjHH1kA0lVtbZjoJlphFDLH26yeOR-j-o7Pqr3Pkj9TXFRM5uyrdXr2G3L7QD4QpKvfuiS80ugtYRH4utjOqQP3VjUVTomT2_WErhhewQEoN0_yPNdcQvsJmUezIzAQfWdOMWGzmxK8XeJ8wasS8vISmNIQZlBcLtdX85LfOAU3MoVV3OxXnz2_W5j-RF90JZaJrARVXpvi_dfwo_2UN9B9xWzsCUaTOETRQd9XrtsccSocuCVo8eVIZ8plkUqOHlkGyiHu1LVw7IVfN21a7xz_GYrREhtuYAfZYV3gZzWD6o1oH8Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ مسعودپزشکیان دقایقی‌قبل به دلیل تسلط کامل‌فرماندهان‌سپاه ازسمت‌خود استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22557" target="_blank">📅 20:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF6DP41XbeLiNYMtzQ6PacKfsYZ5PFiwUwpIddW136Dwz5jiOYmhpyBnFeyGV_aTPzatL8bCw9Zg5gx_ENs_Sj_Nt0PG3bnrffzPpphahF_g5yUcTDq8dkRozUstSxaOhENk0QKuG6amYKLyi29xldXsyCdBQatuqpuK9VEQNM26XKypEwncvYVFqWJkLnserbkoam1Pp8syBEZ2lUezY1dVhgtu6WpiK_yfXaXhBlHxTx60MZbTM08-xCFMxi6vgHnRAkh_1Z4F_T1BK52ajae2FPZq9RRm6qKRNswmnhx2LP_bybZpz51K2YSQY2P5FwKqUGzB-qwntcxjt5H4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بااعلام‌کنفدراسیون فوتبال آسیا؛ مجوز حرفه ای باشگاه سپاهان برای حضور در سطح دوم رقابت های لیگ‌ قهرمانان‌ آسیا صادر نشد و فدراسیون موظفه که یک باشگاه لیگ برتری دیگر رو به AFC معرفی کند.
🔴
درصورتیکه که فدراسیون باشگاه پرسپولیس رو به AFC معرفی کند. اونوقت سرخ…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22556" target="_blank">📅 19:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjHuHFy82UmObqOkyjKT_dcRfJRZJYdq8dMqJ_DsyYWC64hkgwK-tVt_4wvBTlIEmmKT4V_jRZsNjuSCRpnMzP5_Lpc8L56317gDPYnkZugYKysUFTtrMsmIUXHY7oVQFhfCYukwN2WpmqbDsqBbdXPCPJn1vu1L3PQNsfNN8tRAW4wPWJVzkT8kKd-9R7dIc0pdEUodd9FDPYKxqcfgKbidgiTksI61AiNrU-YpdUkeeT-oNUs-wIHVyTJy6SlMdqfQkjS56-zpStfRSf_9Ezs3VvoTdJwzKDJe5CesR0D6OXmVgZJr8rRK3ISramNiR0DC3qommzYgFTgV7ReGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22555" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_5VZ6qkaMgd1s2E7kv8kFbLG_KUUp23sN59dmDwwPSWQCVNmBq_XhR562VWCmV12GxNCMwSsCJf8S4ktkflIC6jp65t5-oL4E9X2MlPdhNfJ3e5P3ylyQngasJqDsM12fWp01UpjJp69IgUgyzIbwAUR40dnaLfHIC7VdCSJJLnqvNWSFAY2vjlojDKJgadM1rbtv0EL9cpbUm11zWEB58rDQ8Day79r34m1ciEytC_koBO36f0uHcgC8odti-rhqOJAcTw3CjEOPioBy48A9cboAGtZr_mjJDIVKUy_eUMEw9Zgz2X3E4a6cKS-7VmoZXAX2B6Tr1DCF5JdkR1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCtwGVF6iZk_e0FI1LxFTJvKIgkmssBnuDSI6GQnNiVWXS-DayzQAepsG1kC50LEPl3yhUpBkIvc00yMURyyl8rELHsUGNMI94WCe5nE-8Riqq6FLbQ3xh9OPVv_2bErEu0fIt8JreGbySkThNZojZq59um0n096-T5GWMgHGbIANDJ6SEf1oQiokB3fWmc1t7foahiavgdEiRJeN_QJmTiB_O8eoT-1QW1EIRw4iOEiLEMrV4P3nuXZno9C1wcPO3VmhUNH9pOlKtJPLn5n7E1_lixCJQa6U7LfsgvdrEu2eYI3GrfI_kZlzvCuMwDcAbZN5n-m3110e-I7Tzj_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/av17zHrAdgxtnYsUQhTuIp_6V1zhmwoIxqQJXUHSep5S20BNo11fNcUNevGWHmFCAaFLK8YBU-f4rc6ZnpsWIOJColw6Ur3JNloMj7ml_uXYu-XMqfsolGjgyE3Ijo64w6NTp17xH3JH4D9Mv0hqLhptOcqI_R3u-2142CC90ljH7pYZuEu7sORWkRCJ7bOhe0PAzAfk_6KJ1ECXoPbkoSDpw5yLBveVsYkyGOuzQrOIvyiAKpV1e-hrrzUCE21cB_lyzOfhLcSUJqHv1YIHxJo9XlaSHqqRmfNB0S8kP-Sz14-MFGao29U7SIM_lusk0f2hZ5NHTqWNhYuCYVYklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aASV4Er8gMiudfXMGhfNvCHb5fibyB2lnCia5RK3lrxUL_JgJeFTon4-0m-qMOfYYc6EYGBwx9Q3r-fuI0MgVjR85cix-4DVj-OF2LjojqP1nVsbGUVsA2FS5h_74GQQi_Qp58VGlNxqMqw8bzcqGtAOd98ja0Xf--4fjQ5dMkIQc12jz8qSOoiFohraVUVWeI386tgBiD5rXMCdydvBFQ52tpM7ODOfLjIt6W4bIFA_dl-CvXz9hKeNI9MCEfXYSW0rSJpAqH32HFzcYPIqXfZuTNjAt9Tp_7_ge0XOkDJEKh8b-zrHAbN7_IlwFCzUQE5QeU0vz7i_KHRNm1adag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdSsmIeSqMVM9-5L217aEULWxs3MgOPz8Swsvrf-VbydfJnHCx-oHA5vRyu82AqhWOG7T9Zi9ljLb9yrFYHFlSZQwqCrtRaBhKkqNTWZCi-v1t4XPGKbAyaf5KMCCoQvvtOjWzWNkzd_iJddqKgWhT-j1Uip47C1xqDRpFMFFdKNEIQBb-WPiShO3Ub4r5SnOwkAVUBwZIo2dpB4AuUr88Sf1yWsWtWwMkqZ5MIHK06hOoRL3n9SmgureJe7_wrW8oK-rEQqYaUq-a--_f3yfa2JVHgJvsqDw96m1UW3WXxwwjkSvDnGw8I2bfkJj9EYCRDxIDg4zKoNUoAIYZ2_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=df9ar1NOkmtz_Bxxpd5cleNS336Wy-xHlnDPREr_cNkTbFhcFtoltj078ZSBMBZOS1ckjP8eX6yfbi4ymRNf03DSF_zKs5tcy3719GwzLwODt3-Vlg_0P4dQbAjHxpv3brdPeITkD3VWbjjI5JuhKI4ybYd3os1kmrw4iw9vibpl82pA9MtrAwFJ5Lg-h3PF7oAnqF08Ii8DG4Ild-dvv78Lx9V_NjDvwA_xSEROv83d_5FN8fDfaOwLweNjLkAXCHHfI6Edvm0ONrbHlJAbzccjDYFtWPK8h2OZ50z4Gr_NMvp6w7umjrR4IQ8I-g-fboXe5iHPJ8PaUGZR95OtRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa9a136cd.mp4?token=df9ar1NOkmtz_Bxxpd5cleNS336Wy-xHlnDPREr_cNkTbFhcFtoltj078ZSBMBZOS1ckjP8eX6yfbi4ymRNf03DSF_zKs5tcy3719GwzLwODt3-Vlg_0P4dQbAjHxpv3brdPeITkD3VWbjjI5JuhKI4ybYd3os1kmrw4iw9vibpl82pA9MtrAwFJ5Lg-h3PF7oAnqF08Ii8DG4Ild-dvv78Lx9V_NjDvwA_xSEROv83d_5FN8fDfaOwLweNjLkAXCHHfI6Edvm0ONrbHlJAbzccjDYFtWPK8h2OZ50z4Gr_NMvp6w7umjrR4IQ8I-g-fboXe5iHPJ8PaUGZR95OtRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
آماده‌ترین و بهترین‌خط هافبک حال حاضر در جام جهانی؛ بنظرتون پرتغال میتونی امسال قهرمان بشه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt8RxDaWbZM85ruxIzXeO-0n2CNT4EdFJdTwLsL2T4FWxVKGYikixGoQiXOVLKuLeUVenhTVmcOoayEVw5J_59Qqd-useBIti6t1Kk8VRkpPmo1qXoMpFuVH9qXfQ8bA3Ika9btqG7bDrtWrw4HueLix7mTCuvrYdjxNsT019POzcTQRiXM6uy3vCakhis97656xFjdtu9yRwPSEWBv5Q0J8BJLfWUe6LViL8izYWOhgVmr4VCuex8FFpzfLchcPyG0aGIxiXhNH1P2sqCbv4-71iAkrjQ4Ww-qpb8hS6R9xX59jmmSwiWtXC-XG26ZOdMKKpKt5iQ22lNgGZyqeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYSs65hm-hwRxImADxJMdjfddOnsAn70FK9YNDyHJrJTBpzczsxGgVrOgGsoKWFRfp3snWRXtvr1E-hBR4zthtzNLoKAwlfJ5aMbVz2FQnk5dF_XVbHjqfjkg3FZr7IriAvKBcwTUtNPKV7MixiG_J9sJhLCKLD3pyHButsevD9723UpXrYb9-zMhoR2AasGCjHo-GgzHlp4nsMaaMmrSL83mlv1PmVe0DZ_CFNPTNfEvyonH5N9Y8zDd80ZY4LNdTT4KEevpwbBQlUn4FW1Wfg9Iew9iWRMyWCXxV1y8lv6C58ULj2SKkU_-ijD1PF6PS2Bzfp0KgviOVJa2CaxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22543">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfLYbIhvXJce8vMT7Acs4jT83uiDCN0CzCc94O2gksd2usKL_VEeL62Df0jjp0ROYvO9hp66uC2Y_kJwd1Zs5XTBdJSlEHZNxRn82XKGhIdt5AC7QgNNReT2mr2t66neD90gZNEnawn6DQgAdodq77AHvpxSkIvJ4PShi0SPfDAD5_UXhL-6H_HgctDlNWFVXNxIyLeRfTQSOTXWqhV0CCSmsGtZG3XswDm0salxvvQ009R_vLmeGazfgqIrnQ6gxYz_64c8FWN_p9Xfl-mBwRh6BYwR22Y41FTKbziEuyUqIZlT5pjSK3IFWgSNhn6t96vvLX8DNj2_CQd5mYtj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💩
⚠️
دیگه
#فریب
بونوس‌های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت 500 هزار تومان‌اعتباربی‌قیدو شرط بگیر
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g10
📱
@winro_io</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22543" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy6yb2X9ce5yWzmgMFYM0QWUJayv_LqYMBGJpdU_pO6o3TBXvikdb9uZlxczGuXY74bNAkk9VUVBT38MW6eDfnMuFdllPxgFEzUIvIfZe0sQWiemrAgiz-SV_v_Q4OY14Ak1th2H3CyXKlN22l9_MGMmpi5CToOQr7mYR5hltxIHQGM-of1ePkAPabcFjH7JduNjEV0uu77zpISuXM37J8jKhElwNM8aKA_yaXHHts98eO-mQt7mGOfF2iAA0-vG2jXHG-p26R-LnIW2sr7-p5iEEdkHQrLembmxORu13QUtM95iHlUuhs7ViJb5awsqgCZIvXwuWn3FsI95RMWrGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XazcIfe1qQRWTdGfPTA15FMyHZox3NKLDh2rlZd5GdaueZ-RwwvzODQJrQVgpm75si3A1hPVk-ZJ5bQY03hQb8ZCkg6mqlp-rNwFMkHiejXuAUe6AvAyZp1JCtXbhjB5pqRzxGzbtvzB7NznyKeSwB0Rs63NwOxCg5yZuk6pK11yz_xUoFfteY8kQYsIB8pGawynPNUiKoEEPRUFJKpLMvpDTbpP6fO5Y0BJpeSDrak3bOTiFimDlRU7-KnFUndTNf2ubGonlzl3V7_5eloIqdCFrdtgUfMsgHTnnrjmnb7LY0wSlz-BJWlp6ZxD9Z8EAF3KPl-9nMWPFgJjq2AXX_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11672147cd.mp4?token=LTBKQXe5dE7hz57lowOU-s4Qq-E6QrvZsYA9dcPOWN-OZgyIangu14OHo-Gj_D6DOlJuTbCyiRaUptfSVn6dhW2nqAYnMiqQUwN0x_WeqIk7BtlwxUX4GJwyktJMXhXX-j9KHAg56-5tcoszaOG9RK2pTlegawZ5o2H_BTP3HTS3kQu5RVRGXlmN3ZbfMrMCtTUl_UOyLyiDvXz3h91jH_hLfeWx9G_xB-kLvbH7Ef8eM64W4D-cttnod1xgvS2MXMl6HpvQEqNmCLMhivttQCCMrwUhJSKvfXAuPA4dhVpYCqkzZAYjg8D0cGvrxCfOMZ-_K59tvQOFLS5DXBz9XazcIfe1qQRWTdGfPTA15FMyHZox3NKLDh2rlZd5GdaueZ-RwwvzODQJrQVgpm75si3A1hPVk-ZJ5bQY03hQb8ZCkg6mqlp-rNwFMkHiejXuAUe6AvAyZp1JCtXbhjB5pqRzxGzbtvzB7NznyKeSwB0Rs63NwOxCg5yZuk6pK11yz_xUoFfteY8kQYsIB8pGawynPNUiKoEEPRUFJKpLMvpDTbpP6fO5Y0BJpeSDrak3bOTiFimDlRU7-KnFUndTNf2ubGonlzl3V7_5eloIqdCFrdtgUfMsgHTnnrjmnb7LY0wSlz-BJWlp6ZxD9Z8EAF3KPl-9nMWPFgJjq2AXX_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=hRX8qmB-R8bvBnocsjvW2usOhVdS0tCIYK7O5u-5rDvwKEEM3CmGoiqnuqhvucILO1ZDwWPFLWtYc710-NPbhUGHXw2LCSWcnagxf-zamRscfj9mfLxZg7R6tBvBHGlsTy4xtmGfcaHZKjyoZYh8ouI0DZF_pa340bprW26rOQmnknNip5ZigWuZ96Bwe2tLxk8HvubJTj5nqP_fuMdN9u-PXe943aeC3FcrJSMB5_VdNn-oXyCmUzBHYxfoGACcEVfcIjp6DI8fHsyhkMmCGtd-NuxmIrEuLu49Pzu0YWaQsUNx0k3z7cp7mI9NUjwIEiDXPm1AUjiqBFjSeexAqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0b950725.mp4?token=hRX8qmB-R8bvBnocsjvW2usOhVdS0tCIYK7O5u-5rDvwKEEM3CmGoiqnuqhvucILO1ZDwWPFLWtYc710-NPbhUGHXw2LCSWcnagxf-zamRscfj9mfLxZg7R6tBvBHGlsTy4xtmGfcaHZKjyoZYh8ouI0DZF_pa340bprW26rOQmnknNip5ZigWuZ96Bwe2tLxk8HvubJTj5nqP_fuMdN9u-PXe943aeC3FcrJSMB5_VdNn-oXyCmUzBHYxfoGACcEVfcIjp6DI8fHsyhkMmCGtd-NuxmIrEuLu49Pzu0YWaQsUNx0k3z7cp7mI9NUjwIEiDXPm1AUjiqBFjSeexAqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
پاریسن‌ژرمن بعدِ قهرمانی در لیگ قهرمانان اروپا فصل ۲۰۲۵/۲۰۲۶ توانست‌درآمدی‌نزدیک‌به ۱۵۰ میلیون یورو از محل جوایز نقدی این رقابت‌ها کسب کند.
🔵
نکته‌قابل توجه اینه طی دو فصل اخیر، مجموع درآمد این باشگاه از UCL به حدود ۳۰۰ میلیون یورو رسیده؛ رقمی که بدون در نظر گرفتن درآمدهای روز مسابقه و فروش بلیت محاسبه شده و صرفاً مربوط به جوایز و سهم‌های مالی یوفا است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4b71efa6.mp4?token=LECsO_Grg1fi7fpwJPuoTCiynjTCUDVYPm5Trx_zkrtOG9RwxjiqPwI0QOGOAvaBxDabHlw0fsdNzZmtzdbXD_emiW8HMKDNyAf-18wyBdo5a1nOzc86BO7Ew8hVLYHFS6_BZIZHLTckn6oRamK5A0mKF4Z3Zg9M-j0boxngm5IevpZ512D3vTrsE78XWJpHCUpXag79MAE1IsiB0CEjC3xJ16U6wu8lt-jVsnVrCLyy_NKVvAnqzUVUiPgyMZBPHSfltjshlMj_PQ3vIJZ0n7gmsReS-XkstfgrgfBsKkiuaD3HgRCJ43jjcTZgdfQVvzfLGLr706Ief3SIWBngaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ایشون هم یه مدل اسپانیایی هستن که دیشب روقهرمانیPSGمبلغ 3 میلیون‌دلار شرط بسته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOuOzLee1NBfy67A1oMawMQRh3iW8Dx7uuUU8LqkB_IA8QOHx9woJuhkKp6wz8-bROaYgPzt9pNEtLlRxSCD3tEzv5sFEJ_t66MMAHDEobMI_x9OspQNOLd29TIkkVzDhudH6GfYmuMx-zZAmDt-oskDlAkiH4_ctBk-zb7tF2K0NUpjDHm_8hu-CPOPsbwX45q-dKuq1_Jrm30RZqYhRlVeFXtjDt9oFwB4tRFYYH46xNOIN9XP1391RHbZrCMPf0inu5wyCQoi_7mRCxHesvIYKf_FAh1IkUDWh8y_UqZ1dO91MxwvcY91RVApK3aTS6ogCgN0se8nk-_XMVquKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObWD0I5mcTanFCJ-jaYDX6gD5ig7mv9GKZFzpZa8IIBeDhPV9_VYG9zTLXTzXG4SqP9BCACrk_6ZOCFdkFqYW9pey4TULioW92Zt52_4IgnJAMGACLiZamNE_BeORgJARHmtC6VlJTAxqvAxSvWCz2gT_ORnaMn_GcK46YDaZhOMifIqSykJ_mW-sSgybFl9U6_yR1iBBfJ3HtWiZqKLhAVqbi_Ok9T3JpM9LuXY703DfMXCgalWH2NuXugy6N8oZVRUUqx5t6Jh2jY3k3yewj2FrbMof10ddqONIjMFufRyeohRN8hJzcSvKBrpFaM8hz4QyXTDKncWn2Whr6o2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYcdx_kxaEKeDpaH7q_Zcp1csFxWNq48Rqq1cZfOUSjeUyp_7blrD0GP387ORH5KUTRYicbvN4rnJEDX27MXxBLxdv2337b5x__U06vEYqpHAZeJdzpm_avycgkIDaj5gAqwP8MiBk7RmtHLOHwB0K30k1I6aB10qodnn-fNKEdpIJYZAgzMH__JxPeMr4NRnV085U7nJqQ-IgnMvFjZnPYuXZ3BTLF_YvdEVlUM5FvgqxrNst3HFxjI4drlsneNtClvFcmq5MX7ZSk44zxoA7n4dJ5OPmvRMDXx6GYpLOysuUOeCDIoIeHc2UAjFeotqxh_kIxlLS-Td_64JjdHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDi2flK1XL1MM7KsI9U3xss0RLuqgv-eJU5ARfUCmQcKE6nfA-hpjjxXy0B17lZXBIedkUSVtvt2nQDX1m9WBhir9CFaizKfadcm9CrlVZE4FPCDirbowMEDs9vm3AzBRzdho8kLYMAwgdFUHbOsIza8ZrNxIDxoiw4tn-ou3Czir4g7zmIDRsIfQnmVrFkloGrekrbLrQSgov8Q-7-3w89A1GWnd_msBFnZTOyf7NmjCz0bbi9D6IfRGjPusjP-gAqHklrw33x904-F2Nl_9qxUL-_fszZsuJeuxkqHbR-ZHa2yNM1eGVGkYa5Y9StjF71e9Yx3iDctl1bixjTQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpaAFIjeWZ9C4_sepgoHdkChTBrCrvpY1sqtv42eIRRKlrPQQwEfZYzEn6TkHpOI_xfjzBq-Ewbyv9fXdBNEWeqR1ZV-uqPRBp6DQzbwMDer3JWW8HUrop5GJoXamsnQXGW0UWEBJL9MvtArH8AkCHr0gu4ZksiUxyERZQjPVNv4Sauw1yocWBstkXNf7wyx-OHFSUrvvs6E1CsmgJfnZ8A4JfvB4MjqxfTV0zyRNUGn-5gDOemQegc3sdCnkRXbT-La3Gxwte7AwPwQIc9AQRJAMttP9JZGh2ne6vjPTo21qxcgHrHAycSm0bqqoOvqGpHCpiY4k9yFtAtia4-l-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE0zrF6QdwtrRbTinAhWqWcnrCua-4Oda1Ub1d9880pYUDgoQ8ijR9JG71K1bDKGC1DsxkP09Ocx-piZMzCZYBBF8XxAlQA4QIBNelOh4vF9SGciFNxi8L42tSLxGWYpDQo-FvJwJpWhEsx9hhaZMyvLy2brkJbWW_eSExXfk9Gi0tq_VJFu2js7It3zC-1ymaMZKNimGdCBOH7QmkYpjKjnaTTO8SeII6bd3srmRSFf7SgbMw2k1OyyFGaDzEHlMSIKfJjRaflMja81c0BGbs94GQ0Kuc2RDmN8_2A1j1OpZ22aqeXiHDvDV8rpehB3cDKw8JnLwkBfLHbju70ouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt4fS0aNTu4n9t1FaBcZnhHDzUi9t6wt1mXIxQzbjZIqukN0jN7tGyXE8ZzFfVNdc3DMkRekdQaZz4RQ44Du2K6Vqm2xeY6QcI5xh9-oUNY6EBLgJ699IZY44QS5Okk6sZnVd3qUL44TNE43r2aIkqlzugXYtd9ZysI3Rc-DCvKxjK7JN9kezxoxOKFg3AaKqtn-e5tQwbKUbiu936nnBLKQ9zG_V9A0nW_CNuiX0HAk_QdftA31JA4px_L-hSLB96gP3xAeqL_exC6lCbjBm0Zcg3Fv-tBZdtd6RegPR6S8xIlQDOaQ8x_kmwXnni-OlQFyH3xWCTlvaDfuG3TeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaXKoPz53ZbF4WlmVF9O9Fnt23b6JBA-q5BUAm9Rdw0B2DY0MUrapH2UWbBqFJaCZmODwXWNbt8pLHagnBbXr8F9iQzshIEbyxX3bFlq2xt51URNyKETeFbjLOVqbp4arys1WLOrHzBvijVEOgwH1fRky-SFAkVVe7p9QzcxRUgVYG5QIwrZz_e3ifmWVR5HQ7MTj4fQKBy_vBXzuOEFNaWwidQ74fsjeXZ_bmYns8HH0SfCvRQPvPDhK6Ei511FchIE81QHZ2uq9lY8tYeWNOHX17Pcc9-1o8Z4XgQwP0JcR40SCfUpw4UKz57bpTPKfNlKY-H9lKnxbxWzU_J1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460d6cadb7.mp4?token=TF3Fn7zwAh2YeFM0ZS0r1R-jcxAjxO576r3sFotzfqZz6LACz8d86G2e3FSndp1BkIZ2xih64JF49g4bS4D2qg9jyBZvq1GpUNeDNrwIJZEdJAiD55-a0K-inUgS7riugHOcdIaHua-0il7XZcMjbXM9rgWUAirdKzBhOZwz-ZKCbolyS9_sKKJnNeNAbn3gYGdOIPVbBGcoVm9lfvT3xFHLoP7FRlFEOdp586mVQnT6dXgCORzWjdnVh7fg8jX5D_b_4jR6imTRTcfgKQ3ZtZDTTHsEiX5r3v0t9k3ex4EvjvpWwSCL8_5wC0arTbGWRX4qywvBIWfaZP6LDjJPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بااعتماد به نفس کامل به کراشت گفتی بیاد ورزشگاه بازیتو ببینه که تحت تاثیر قرارش بدی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twXSBUkLwHEerxnqFilwM3ItsZEEu1PE5GgrOl-4FAU8SeAaxbfL2so2RdHHUYGsGy5zMeSlra9vQOGOoVx-g8UpqoRcaSQ1LQMIY2MVb-b3SmHs0Ysbxrsrh9-MMc6aJf-iYf2Y7wa_ihlq05osTi9c5ry3iurjf_a1jLqFBF6l08lB72J_GBXIGmSq-WoBh3TQBWaF-wzyZng7bXmNjmxmmkcRxIwZXwLXtr9TyWK0r-iszb9P2Dhd6w9o5OGazpGup-EhKsrnU16pbXSAeud7O-mD8XTL13hwKEdVv--rzUoNADcliRSO0MVlgyJ0OzG5niq63M44ddalU76a7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55166b2d48.mp4?token=eAnf6VgxqYKer5nnoAuPulp97gRj5j9HFnj0fMruWxLcNRFVWinr5i5B4qx9wKk-vVIltvld_eGqXYw-H8lbjk8I_5Xr-PfML5IBFDc9rKxuK1cG9LklEZuNlqJlPvea71UXRNogbvE2YE__BH9Zhz2qnCZAxN7eU-xBs8kcqGYPER1ZC2QojKB-dXbF5TXVt9swDlH3xF4D-DQfHCxoer3V2V7lBZPqjh9JPfjgXaYYLdGLATxDD5o4aUqLAu70GHtEOr865ITTAWQZQJG-kg7W1ojRkb7wnmDAJTLLE1LHjhSc1Ga1VKLm7HcoSPmTxJPSUVYMWGhsQIb2iwRM8whRYRBdnQ1KzhgztgfM0uGHYA13EuTNVG7ze7uzlheq7kD-tb62kEStb5yTh_NDEhyRcL60GEko_n-kn0k9XOpQ6d3fBczgkcxH-8I6EeoWoIteIAE3D26P-VUmOVqF8lmEgmckyy3ysmgOpb6-0zJQTc7rw2PEU1-Bk1-vrNPzPut3jR8SaBpCc-SUXv6tLV7D3hkRz36l2RKRLtUF7eYiwKvfFWTuRIpdmF9e10Z91JxaUwTcCoj9gCrd7NIcS8Ho1XCGBzUraWl1E6UodSr5Kzc90F_ov5xXVlt3OqhH7cMaPoHD_p5zPcUET_VPboxusY8P2E_BORfcgMhYydI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لحظه پنالتی آخر آرسنال و قهرمانی پاری سن ژرمن در فینال لیگ قهرمانان با گزارش جذاب فرشاد محمدی مرام که یکی‌از آرسنالی‌های دو آتیشه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b2ba8656.mp4?token=ZiV8r8Zvx-D9mO-BnW1ROUU7vTSXDJsuKN6M_IxxNqg0FbC92VZVEbF8MhwAuhTH3Ihc7wZODruDqxQyeTpCQfhEVdKoIyz1ICHWnKpErsCkCcwRWub_ni4VIIpec0QU02W2ZAh7RfgRQLLnc9i3cARw1207qAhsqZSTXkxknpdSQSSHJ63k2BGTrSg4sbn6nlSD6lc_Oi-Sr0JhYcuScBxkrTXkHrDKj-tdMqQ_rs0uiHlNhQ1V3aSlqug5VNAPJCMCWd1k-Nnogdxx6yMu71d9fSzDvgHHjOpVOTxNuMz7zl7YrQeAcfLL-cQeISKLi802-B-np_4psRnZYidQzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
واکنش عجیب ایوان تونی بازیکن تیم الاهلی به قیچی برگردون کریس رونالدو ستاره النصر
😳
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlR-izVaYPfLOz03BZFNOMdGXgQMVYM2MlcIpkM2wjSWT6NHtqBqd6ioLZaAjy7B7h5TEPC18QUKTMiRBP2MHuNbLmt_QxDXQoDIn9elChQ-npEpkLCLWIts_bD7-A03x5vVmKQmX3Dj13UzwMMcJ8ABTEJAfUjb7MTdXsfHVZH2rzbwAfl3oyNj08AHce0vXlZ0opkxrEaks2QWskAb_eZvzNnj0zXzhp5LoIi5MbwQkFGNs0MTXz49Mp6OnwIjnkN7zH-oAZJonBO5-GrVpY9yCcbp6qhUHAqABIU6XbxJTCB_F-RDwDAY91izJ19_HgtU59bd4e6c_1ZgVydeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1346d9dda7.mp4?token=fMhGrIc12t8cGl9I76IbF822rhnpeSwjR4iS1yAs3Gu2WYVGX5zD55_KMmdeIhFK0T8CCNF9JfuWvgk2kaA5G7aGtkv5CHiayqKhFNN7CaMG-Jyq3sOerNxR71LuVwhkLzJCDsgc6F0Lpo2BghlsCE_OjIvc-h5F5CbbPHvBzMXw9yfJPrGPSiioezMoiqvXiicAtsAQoVLmDxwDs4jVz5y7mvz0E1XZR4iGcmrMaX1Mal1-JkrviHAwpIzRw8M_nuGuwyUZbNN3u5SJRp9Rol5vYs_Kqxe-GwEIhxqpZx7xh3MtJBDzeIWJu74YehuTdOnM93SWSWVtEFPUy_FCNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژوزه مورینیو سرمربی‌ سابق چلسی:
ابراموویچ مالک چلسی به من‌گفت‌که برای مهاجم کی رو در نظر داری؟ منم بهش گفتم دیدیه دروگبا؛ گفت اون کیه؟ کجاست؟ گفتم شما فقط پول بده و حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c743e5df08.mp4?token=qLctV_nQN5iOde_2fpasSzmwPCuVQrTcqcTZIDKySIXi680NsiKGZsagPwQpicEbmlscGOjWR4zovUfG84Jhssqm6M1f3JHk9AndU4b49zagq9EdYdJkd0AP4m7MAXols3kxCtWUXr-Hmu2U5MDCq4Wr8rKQjT3PlSKSSknetkbdYp-Y_z02Zc6A7ArxWunff1BdEfX6-bgECvkz4kylM6vjXSzs1oELLQHQQEQpuZfG85gU1YqlhhHQJW1XDHbWVnH-nsexbPVgqgSQ3Rv_jkCNI9rznb-vQ1aWPkl3FXgoURPcEMtN3dwgkdgIFUQwoYtbduxiQAFEFqYVVyyoKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یجوری هم متعجب شد از اخراج شدنش که فکر کردم یه خطای ساده انجام داده!!! دِ اخه مرد حسابی زمین فوتبال رو با رینگ بوکس اشتباه گرفتی
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baebe6400d.mp4?token=KyRlNC9MlB7n1P1g3gVOu713wsYXAKdFg4fEUCV8JK4gWy_rPE8LfOKR_5VqIRpCamNqcmnfrCaQpcDNf-CiAuJVBrJNi7COimhkiJw8cDLpxLQfZ3lidecwg_S7JkxSRh52sHw0lgROeW3Z7pzsXdbykEXnnoQFeA2WGRoDGgHMWEXz8z8CcNw4o489zXQ_QO5FlygBoyFGtOuoI-gPj7DJBsy4tujSYdVshJp7XM4WOWBZAw7zuQQQq-JmqTREvRZYKfVVyZRZ-VG7I-fKvLWDkpeGYyrYfXMpEFKQBlpK4IdyFcwAMK0JjGgfqvUbvc0omGs9OOdqaT1b3GgCyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویتینیا: اونا تا میتونستن وقت تلفی کردن، اما در همچین بازی‌هایی بایدصبورباشی؛
ویتینیا علاوه برکسب‌جایزه بهترین بازیکن فینال یه‌آمار فوق‌العاده هم ثبت کرد؛ هافبک پرتغالی، در فینال لیگ قهرمانان اروپا مقابل آرسنال باثبت ۱۴۱ پاس صحیح، با رکورد تاریخی ژاوی درسال ۲۰۱۱ مقابل‌منچستریونایتد برای بیشترین تعداد پاس‌صحیح دریک‌بازی فینال از زمان شروع ثبت‌دقیق‌داده‌ها درفصل ۲۰۰۳/۰۴ برابری کرد؛ او همچنین باثبت مجموع ۱,۵۸۹ پاس صحیح در این فصل‌از رقابت‌ها و تعداد پاس‌های‌بالای ۱۰۰ در ۹ بازی مختلف، به‌تنها بازیکنی در کنار ژاوی تبدیل شد که به چنین دستاورد بی‌نظیری دست یافته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOJv9pBZD9sn5KPGjoB8XxocNU6fhGHDePicUkeWhCy5-BAmTpc2l3vmVeP9gl3gDVOCK1nNgZfrbX43bp5pDzjswMfcdZAEf6U3HONdVQSQHhNNvRoPMqNjKQyhIQGsGUg4TWw8kDbfuTKopLY3axyAcE6Q6PMD5cSMrkxOqiluhZYPNXG2PBnKMr9aa3OndnvOXxPF3wOgh6M6U5JF5GFVeaZHU3wT7qu_0sQ_M4nXv19aUGN5MA8TJfp_j3V9orRTXbNJHcvlA2xXwYmND0bj_iJF5uMRJyRPnWejq5urwPxoCsXPkHvBsMHBmsmSbGLLSPA66DpsTyqR5TuO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
🎉
کافی‌فقط‌عضوبشی‌تا
#وینروبهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r10
📱
@winro_io</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22518" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSr3i4a88R3odeglq7J6gaDvHX64MeK8nmNhbmXZY-nUI-OaVCNM84sHK4rnPgnex8uC10kNI30i89T3ehQbOTvA1jYEgq0C1DPjLoPE92ZUn1kmwqc1v-9Za8asDSlQk9GUactM-PosXd2aIKQVpTD4a93KnWmFiI-b4K4JBGjjyUo8yUH5ZJ9lZtycUiBkyrxNz20bZPacgfFXpXucpnqPsA7Zj-txRxx01ip9fD-PrHDtK2zlVdDwtDX-l_7aeQSjZ7IgMOTjfVtncZbAbMoGa36tYxbzMrfLZbxPcQnY_6wnExVAI28E9KQq3EfkKshvHvDcYylCqW8czr9wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22517" target="_blank">📅 09:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRGtYcYX-xgxwUSkQzt0fUhQYexxA14oAYzBzPX4rZ2q665QVLeqfJxAADY0xkvlnHboXagmqMAfan7YjPefXQ9IQhptxq69PC6oyTX2ZFIOQJAlzNW0gkSqWggjy2aiO20KSmK1ehJzru2nT25MsSWkHGoa2WReu_nh51Zvp2sG-QBKvBVYvPfheH5AJx__7S9i25qGGFe9bOGgm5ZG9gXVH27iq-UTUrohH4IVH_RfGmghItZTqy53RIbW5KPI9EHHwpJPnwMhHpII21yDjSZaCVW6uUOkhqwl9XClNuCwjjTZeJVskaEQWLlOJ0JiMA70D4PqMS7_KhrWp55e9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22516" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNMgVMRIBOuuv2oonpJR_rI7ibJgXSvto7ZWH_TO15xYV-KPkC_iSkCOCOOobo1av0tG0Tvl_btwp1_5ok4mrpj_XnUqfYCVLiWYQI3P5twTxTdHxbAtS5YEmL6PbgZ_bL0Vd1b3HZYXGcB2PEKy39KI-VLiGoQnqAJsVyH9OsHXju8no0K3CEdAFzOTJWamhu8K63I6cUhl2WZ0iqQvdV9jq1TBDM-VtiCv5yv4dhLRd_dtj5TTvgJr11G99BUadBDItcH1KYwbi-mZrrGyF3tLo77HJL5xHeHzJCD-glamtCop8nJHeaJxwsRQLv5p-UFCZhR7tII6djM1EQ5Qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا ستاره سابق باشگاه منچسترسیتی؛علاوه‌بر بارسا از اتلتیکومادرید نیز آفر دریافت کرده که اعلام کرده اولویتش عقد قرارداد و پیوستن به‌باشگاه بارسلونا است. این انتقال بزودی و به شکل رسمی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22515" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aulmGRz6tDQ-5vyd2wUfdbsGu2GzdAmH2GrleuMJFABplvHyZmdnuDdLEdl8oFGjHBURyZyi_NsyYEOzQu69bfhiQU9TnHGo9zaoTZrwXUyWJ1iOlbT_1OH2V-Nc-nmJmf4JOmJbTKoX08eKfO034ucf6VS3kN0I43wv4wCa6odyfvpUzsj23K0jx7rXzfPRz5YwTvGA_ph1lGmEMAVzEoEMGMx3Lv11I3QUDl3chCECzNc07V05qsw_dKIaX6yCwGvXDmqeeLdgCc3Qn9ESxrF0-x2nVoPitSVFyQnqXac_af3oTnhU-p6YgSjHmwlAKLUT1lwrHHZW5oOOJKdjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoNTgkR4dcHMXioKaQcLD6M5seqsVa9NTv-i79SVQxLA6ti25liLshU1uk4ccfT13msuf_f7ZXNYwGFT10yJG9IjHzlgAMXM-N75eU7DTZ08Iz_jx294HiFfNHXNFjMpVijf2bBDe5682i99AmWmjRjHaNl5LBPuNj5l2OQWByMRFE4CU084QMCTOvOsq0XOpKLkehm1ibqHjCzDnZQ-Fat4C_JQMhGv9A3x3k9PDsnnaBVl82QoCZWocnDX2rnzGkJPgPZomT6rdozuXS7zgHydJ7uLlCU2RmaEGOekqmdQNEcOLmdbbvvh9HjvXORLVsy5fCvnFne_x1-JtEA_GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXjcD6bZRTo0KatSJrLD6F3t6oZ9Hv065CH0JtU6O_660pmcJUhLBMCCEGUye-aldBESsz20RtlHYLDQ4m99MZlcclhzbshgAXFBsNWsKNZEWGvcBoWyOSXfGjrohi6KfKeQvtdFPbhR8hzGMKQqADYDlWkSFiLgR5nSB88mO66-t0DQWF8vtGoQezeC8WCgYb02b90_m1b2mbESj1AQTtyunxh_8inGZ2kdAOWRqC3-YCpIc_anHO1B5ZJXx89mpsRY1DYJUCMAv3CUHizXJ9vJcjn7bGI4W_bL5ahD_4CsCnm85ssoXa8yo47-xcvdKv5zk2W4M47mCHQZa3OcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXFTVfBxlZuj9eoMN0d0f2WXLngCW5Lh4iBY34qblzsjzqT4-9Xs8JmIi3miCmpXBbnT5v42Bwms-TzOrsnT9xHawD_lxiWI2TPK1riQ3bqsndiJ6-YJ4MlPpaZiJF7OZrTW9B5g_0tAgKln_YvPAznHmaqsQbAuaZYsGCdzfl1ZJwZDkzTUIOd9z2LpspFfaJEFeeecJX4lD5OjHOuzm9uxrChbJm1Val8ShaM9HYngjkSXv4J671JaZwXYaMq-u9iY3lmxBDhgee-BVsfqt5mGMJZv0gyjt7svqKi8l6u82IZjO8kPl026qAhd66rthZAUsFstr6uXu_r5qyFnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
کافیه‌فقط‌عضو‌بشی‌تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست. پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a9
📱
@winro_io</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22510" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt1bSjJ8RUaie_NuoeqVKUEQmll713ITtsljaSMaLBpu7QgpDv5DZgnNVLT8SFC3DcxQpD9kGuwd7pjoWNDFLIaZP4ISUQfr5jKAmOHyKlStud7RkFSjy7PpQG8RYz5mnUwED8a9ifB-PTC2uxtwpQS0BRizjjT19TkOnrHlno7HbGy6-_TSwYFZZes_rbTxdM6RBMEt8ak5Aue2yrwIUNNubtvN5nrNg2IsKOuwaIQwy58ev1Bv37gFerHumK5tmrOjG8MmNb14sH5zrj4WzvNjMhXxewE9XzLSvekvH274PwY60GhG0uAtPeFow6vtp9D87pFyvSDD8Eo9Yi7mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXCd4xbvjB2xJGzXjwnBLaBn__r1B2fL1ZMYJ-lsB-kN7dZNcJxMGEvF2KeYEDA7i90zPpM9g4Vrg4Tmu4RFa6JPgQztNknBb6SaopPqSKJ1kgJ7sAJ81LKmEomimcpvF1UEwaqD5DNOy1l84_R1TPcCvrNwBI__pM2fs2B20N1mI_4Rn0PaIe1nJsG-YevLy-thNwrMulTQNXig7f11SLepIfKxjZCOeMOUr6b5VBtc9fdtz7QEFP96yXDqHsWZH3L9DWRzKD7c9wOmvlbOqCgJPkqZ_dOX3zvDBhqGORBGKKS41WoYgDU6XjszmBwHJ2n6gn2bdkJ36TI3Ny1pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2be4rvZaaoqjW8deEFnvmBwGCHQ2PdVvXScCsFcqN4IRA7UaRilEyjRZPOI7lWdCbXNfeUgwyg3z5dqGXTWExL2-305raPyknUocVUShzFMpeceNadgyQDCI7Yqdx404NqqUiqBLf4DjsyMWBxOvF5mKvfkpTsrWWuS2c2fCjKvbdK2T2MDlR5MWNKpXIARPkbKu1p1ewf4JtaXf5ck1wIn86Fm0EKVS5BIxGD-1r7hNdv0Siai2U11gC4-zGXIQj__YvdQ4wQD06WEi2Caw9BqQ-K7cCmaY3XFaVEQkqXNFMbIEhaxn5TO9rqNKc3aJBMIc5JZdZn2vQSBVkuc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-bqJoQZkO9IoaMq-t-gmiaxpbyuG_y-wYQv5ipDAC6kqPoHKpH1Xak692hzSm_54TtHSBAxObBGJ5IzBBK-1ZNMxGwheLaTOIb61dY3p9CuPrW9pcJeNjrjfi10hb-n31znnNk5l354RSHUqhFDRN1W5mfo0j6TzMgt8eLEWr4U0zrFGK3RuD3hf7ylfOeegq2pYYsgqzPxxWTp6MreQEpabmGwZ8_xW_yXtF9-UV-7BDnNRuq_v1GvWe7HQ1aEJI14-o_xsMuzV_556fJZ-yWdxZYZ22bMZ-BkWc-ovE7Mfu40-e3szxDKYERZ_MUrnAlgX9Yu55usNsREW46BnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=o_hR16aP4uWzQQ09y8HZ1TN5XraGHn_1y9VvshBLIh7qIFhyKQ46fB6AMbB7jZ3xfqcFTEDdFaqMkCjsdmVCybLt_0Y7qq1oydBpJNfAKWe9PQa3tXZmz90JeYnS5PaX6OrvOsI-umL9DPDDgzOsOAMXIYmwh_7NhQNfjSPAflXw0hcAyc3AOp0Q1yGPWomtzTkNFq2eIc_G4dkiS_9IfBsHMcL0JfzxxwuhD6_0oq8X7slgyUualjcKMNJH0wsT8BP42tf9Mwc4x55gjp2o4Vd3qrY1Ue2nq9JE4ymdlLC3A33jxazpYPVhPrqiILQUP47FBS-C2xFppAteWvzL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=o_hR16aP4uWzQQ09y8HZ1TN5XraGHn_1y9VvshBLIh7qIFhyKQ46fB6AMbB7jZ3xfqcFTEDdFaqMkCjsdmVCybLt_0Y7qq1oydBpJNfAKWe9PQa3tXZmz90JeYnS5PaX6OrvOsI-umL9DPDDgzOsOAMXIYmwh_7NhQNfjSPAflXw0hcAyc3AOp0Q1yGPWomtzTkNFq2eIc_G4dkiS_9IfBsHMcL0JfzxxwuhD6_0oq8X7slgyUualjcKMNJH0wsT8BP42tf9Mwc4x55gjp2o4Vd3qrY1Ue2nq9JE4ymdlLC3A33jxazpYPVhPrqiILQUP47FBS-C2xFppAteWvzL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=lfw_ECTWvsrWiFYrsmLJc0pxXaXtDesEwxsHUTWPOXtnpbmLZ0EX9wKZEkPBWwW4-9zMRkeWEJx2v_BAYHIIDb3cpBkvWPbbWg833DxzvhA1sj8V_PX-YXsLb2AZUNab8Dgj6o5_yjQgW2IGdBfK1CcFF8D_gVLPaTohEh8EzpMazr7nZn-EqmA3ILAy3ecawf_Kf2p6g7PB3xdB9K27A0sCP2bmYvCI1QohleMt9pL_KarOsNajJ6uX_Hj0cqoaRmrteNKY-lkYRvcpeuOON7fmNmIgoVBQ4HbpFw7pjzstwU0GEWaLub-VVViH7NxRrFP3AW_ipvwXyvDs5Z2P6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=lfw_ECTWvsrWiFYrsmLJc0pxXaXtDesEwxsHUTWPOXtnpbmLZ0EX9wKZEkPBWwW4-9zMRkeWEJx2v_BAYHIIDb3cpBkvWPbbWg833DxzvhA1sj8V_PX-YXsLb2AZUNab8Dgj6o5_yjQgW2IGdBfK1CcFF8D_gVLPaTohEh8EzpMazr7nZn-EqmA3ILAy3ecawf_Kf2p6g7PB3xdB9K27A0sCP2bmYvCI1QohleMt9pL_KarOsNajJ6uX_Hj0cqoaRmrteNKY-lkYRvcpeuOON7fmNmIgoVBQ4HbpFw7pjzstwU0GEWaLub-VVViH7NxRrFP3AW_ipvwXyvDs5Z2P6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVqUl8-pm1K0ZmfQEVRFM9HTiAwRj-K1kiUMIZWF7Prw7ketzkEJXWdXvXN-k-rnEwFnPZxdSqVSNpmoNZ9xGxm6GhTEtcaCsdR-2H670xMoX5QzLn7C9Xt50zBMGpKQ9CToCF-2ugmvNsSLN9k1XcEMKpSw-j753ue8456GBpKkJWplT2O1hE7gr14xHst8WjYR_IZnA9O56WsSRuu_OXfVP34pVer3SPnhvNPp1Q0PkL6wPk48FKZ7IyOxasXH_5OA0DMNRulT3yFsOEgdq4YmlyVZZc610BfFOhMtPoYY-illU_AkF8OiqDLKhR9QpENuRdP7Mw4f_KzPWQ0Xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d915ebc4d.mp4?token=O_h3BIez4CzGzhX_XdSdBU_Bu7ET9hJ4AfwIhn6KKAPuJTcKwi2mDtGkA_evsf0AGA7Z2yF9cLCN1f8jZSVoZA3ywIy6OwIoCrBRK6h5AyZ20dgWbkKtU1PE85cqtpmyDqyUcWXhXOrke-7vQjKK9iJH54x1oZakaOSNNf6UjNjhnVW7y-lUmFqDMVJh-FiRj7pzl_VNEPqknwRgRHwMX4GDSJe6S5bROOWaaDH1PCegHmUnxZ76OfcQzH4qGceAObMXwCtE0I5up5O_QPrZmtNA4y-fDE4rUSfP8cyRDhSVrX5BlpORX4gLhQce0Ynzc-ksrA6Gf9ABR8dujBG7JWue82sMGdFxVniEmcy3wId7tiGbSDWVhikpQ3V6nET68lUpT9xFTvYBKxPmVhD3ncYdHH_a3tGtz4qtu1xxyYAmyJydXmKLgX_Nx1KbO3GEmCb4PRa-6fxnalAkQmN11GGs-aTjOQ6qcdELKArfXGNroig_4zv22pYriyPJhUyXm7-l8toIIxaKJg9DQZGeQ6bhbBuQA252rEWj_UCiNigmri1jeq2VFl5tpKLv42Jy_3Z7pjaSJ6Oxmg3NK7cE3aBbGvLPyraTSddfCDMgMXajgRaD7D45yCAl5QjnwVTFkkWz8C84peW5GFznyI2WGkEAlcfi1HZqIlbiWKY8Yvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=AmK-YuSJExVzs_pengBcrBiKe4cPYemvkHeRFnDAvgGe_p836Ifuyr4GOSh_ev-iHVTFdIwrxQALOOwJEDeKd8jlYU-23BJZ-QOLk2Rl1sk66kWVgNEaf_66v-mZ9WCakGakZah3C7dxHOGDrNXMP15xdfLQLYJQ3vwYBFPYN00jEIcweqsaDt82lHL2fxbD9ThV6gKOSV7_2JniHIms5ZXTFnnStokcxijYR-mJ7bS4XVT89mAGzkbyZN-zyQFOD1KVKlngbQU98z2BKcayCrMYGd8s-lnsNvsRm_N5_KawvGc6CjMwpzjfH6moPgh0XZgvd-d3ApsLU63RtQgP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=AmK-YuSJExVzs_pengBcrBiKe4cPYemvkHeRFnDAvgGe_p836Ifuyr4GOSh_ev-iHVTFdIwrxQALOOwJEDeKd8jlYU-23BJZ-QOLk2Rl1sk66kWVgNEaf_66v-mZ9WCakGakZah3C7dxHOGDrNXMP15xdfLQLYJQ3vwYBFPYN00jEIcweqsaDt82lHL2fxbD9ThV6gKOSV7_2JniHIms5ZXTFnnStokcxijYR-mJ7bS4XVT89mAGzkbyZN-zyQFOD1KVKlngbQU98z2BKcayCrMYGd8s-lnsNvsRm_N5_KawvGc6CjMwpzjfH6moPgh0XZgvd-d3ApsLU63RtQgP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw0Xn0Dnl8T4C-4Hajg7BRrYPJ7FhJdG-EHgBBtgxyeFUhzua79tnlCCSLEMKcxY_8z---QsdF8zAtbx_ZxydaxKwBrtnr0gqn6pl3onTjGDAJiWz7TanUrVQ4DFex_T7O54UZqebejz3q6RCz7SGQCTHETIz-oVx5u1d3Zsm3cVRqr7xPDPgQwYRVbKf3zlgFUDG7dP6WcwmSrTO0lqdPjpIJRCwe8dOpNdcjume1gRlghmiU2BW-1JaVxt8tLliWoq_ot-dbNyMitrEx_9BonVRf9ta70eSlOEP-8BQPIKUx20YXLVQswXBhy6Og5q7p-6PFVU6QS8CQdGTpnLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c46R93KJ1KuIHx0rHROguWv4Nm5TVO2od1hT5Sc-L8I-DydwTNUrUSsz2AGlvTkgdTx2Bj4KIgGu8w1M-lt8XqBliwmUoTavfOP9jJLe2NHzNKcFLoXLEuxO49pHnp9pdBDcQDI_lHyZm7uLTW_frUtfUbTGw3gJiWUv6301f5pY-yx1ED5wqdwhKY_w10hqd8OJnbdVg5C3jQuzb3a52lW6OIf-AXWN9WLF0ZoHw0tJtEHWXwxZ5_FtEw8IPzEcanQdyNu01f098lbl1uOOOY8Xbrb60aKKW2jSqdHrLS54DM8x77wJeNI_1phCpzvW_-no0AhmK2QV-6eikojppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازی مهیج و دیدنی امشب دوتیم ارسنال
🆚
پاری سن ژرمن بوقت‌های اضافی کشیده شد. آمارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22498" target="_blank">📅 22:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdH8Iyv9r_U6TKc9KqqsMo3j9q2zrGfbJUKeT9vlCF8mWS51EAN3MgZZgjECd87piFFfOfpF2BNSXcpnpiBqajEoOBZ1ZqDDA3sN0N9H4EROSrT6Rquh4QczC62uhNodfhifVdxqf-meazYcJp41LuQETYNDJYO0CIzi73sFWtUltQO91IaGmMNUbX4jEyp2x0UWX5NGKZoa60_nTU61kNXs3eBoZc-mlQ8dLOMPKnSXCqbWDACz7Rv0lMR1QXB3IIW0vQgX9cJ_txHgt9vIQxGfrhyHDZx9z60ruLdd-a6r76u6CM8LQ-W8RPIJjdLCS9wTs_3D17GCxDaCwt-SrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa9tiZo92EPRil9zMTyUrfpJIuf5BsTWMFnm2Z78rfXDjECmovtBLZe6Vllz2WVALWqoo730GseFEfjrFK-36P7ZRcBtL4pEytBGVmKKOnovaW1sJgQl8iIVfYSvCOYRTBKo_hGxvsKiMiJ0n9L03cZMhyLmbW3eBB5YK9hfGW80XvZUg7dE1ld2mDCgZGIm8ezBCT9wvfoq8B_Y8YDhKMX7d16_nd3awaIccvAlKGk0LpaWrL0J1_3oxWpqDcNphOtLPIyJSQM_qZDRQTVisvPXtZOOtTSytzGE7cefWwAAml8HMRlqMcOc4lo8toQ3hNFo1RmKer4f_Gk-E1elUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O96aoxv3S9af4fkRxQ0boK1gm1pA-t9gCTL18oiVnB22MbMYvPaYW8ZpuLge80kvsmNfWo1NG5D6fA2xWkSGKrtDEsrfvtNo_fzCbZrCopjRKZUMF4P5PivPEbv8RSDqtEUzZifjLsCD7T7k8zUi6KgZRTuIq20wp4mU0kP46dE2fef4WPF67pbW0P8Sibo9vElgrywAJTC_fRqiqUJz2j6ew5NtqBPWpuyslmuUgxXL5P0-s5PRkJvUCS0B_ameA011_UwBKcDFnP0k5XVkROEReD8hf3hBmjPabkyG-mVq3okO4jJTd30_dA7xumsGIEPIJGt0XaiXaPmvfu-TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiHKVRgm4glFsBA8wObkXQOHdD57leuEvsr88Gt3UeyNGdJ2p3bLuCU7wDTenOrMNSrM_u-h823JHuWFj4ea6E7DaePqu_ALLId5_waPu7vHzmBoJIwtMqCc9z4TaaAqb2bCNVldUXxKX29zARiyjH0oL7hSDGnxuhhIp-r7mh_QI8KyGoSqCBdw_Fx035q4ZrAQIQUxhar5JNm3UCliHjtuaNX7wE9pGYPev_aCT4nHdQwNwI7kPWUd1QBA3iaDZjq2fplxs1GUwgASGy17pe2hMjn35iyoj3IbJAEq4KRYR3Q8srVvJe3rukOqDYD0KcznT976LMHsqckU36I9yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO_c1WEAjsj70kOtuOgtgvAbbqs9iN9l7C7zFvfLQECKBCYgw2i054HEK_8m0SLkY_S0jXaITzf4yW6VHXrN-JUbP4k8ihyj4ZOAmtcRLzVFhoCrQpmRGnYVw8i5bNThNQ1HjsofItXJV0R7QoF6rPqqA5ByBwmA4LgrodKDQoHV8pO3kw4lFx5bQJnj6qd2uUx9v6q7RMNmDYmm8TxUvUxVAnLkhL-XkVQ6nhE2DSFi_hyrMC3fV_DfY2V2QlqQuy2PBT6VN347pC7mGdIwEorkGPTa73OfOTmHe07c8CN1WCMgIqxBPRNk0QLZOMO6trmxCHcO1TxfsMxOn-wp7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=XjJ0XaF2BvSKCl1EPWpUyi0XqQ8iV8wmW36PQ_46qyLPHAs8WG83TIXjN4qV-pOGzhYBCOlEMCbJ7ZS892l7Re_cXBwMiOL4wLKnLkA_wH5xoFscEkvG54FCw3KIKcklZsIe-CJn8knwBLPOB7FLdMiyADMpqzEVNfYoadmWQF_41ZpUJfWR_0k6pk8Vvphn4-voHLLl5yEN6qwculPzmllju3Qg6Ir2UG7PxS3mqRPU_c5uBggIOpa_1e016oDTAHWXF9CqwiBKyzEPAmR3xO0Q6GxpY11N413jUyTa5I3Z69ceTgn1ZnyIJE_HLbGSAL7dXjJvB-xLObZLPvTkcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=XjJ0XaF2BvSKCl1EPWpUyi0XqQ8iV8wmW36PQ_46qyLPHAs8WG83TIXjN4qV-pOGzhYBCOlEMCbJ7ZS892l7Re_cXBwMiOL4wLKnLkA_wH5xoFscEkvG54FCw3KIKcklZsIe-CJn8knwBLPOB7FLdMiyADMpqzEVNfYoadmWQF_41ZpUJfWR_0k6pk8Vvphn4-voHLLl5yEN6qwculPzmllju3Qg6Ir2UG7PxS3mqRPU_c5uBggIOpa_1e016oDTAHWXF9CqwiBKyzEPAmR3xO0Q6GxpY11N413jUyTa5I3Z69ceTgn1ZnyIJE_HLbGSAL7dXjJvB-xLObZLPvTkcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF5z5TIACHNEYK3OBnH-ntwQPEEtMDO68S7RW9Iy9Se-osuXBXet5LDQoQ8xdkoW1JxuHC6Cb8f0ixsRnR7QkvU-t_RBIopE0luPLEOTwTBvxIPf2jz3juLYhIRQZ5NUWjdsypEpacPhb-sD8B7BCHTCkQ2yC3uEZp1qdgIbVz9r2Iw41kdopoCkepODWyOzeLp8YqligPcwN5fxX63vUUFXpFfKF3vJ6hQibhDCTmSP6Zs6wfGJoVttTTjitX8QRtJtPtatdGM0Iv-re2OGXaFSaIOcaZsP_X8Z6ZYRUFvFcUqtYYOAfEBGI9kBJeysPeeCXVdKAGuz8rZonWsqag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xf2W2AnG1yOYPh_WFwQynTjXSM0vvDPED_cyOngTtb6sKEC3vsbWUni-93tMoNLVPLvJ5qNKLZ4qemau5f5nIRCvVX_9G8gdj_5tBEI8RQ30T2d7c0-xhbPcju_F424TIh9ECYq0PdPJ2InIrSM5B4Unfe7vBdK67pw5HctdmJhZTsh4ftQtnGpVtUYBuqZGdW1fdif7ApqODxHaY79SMqi7CeOZcBKMw9DdFBTZ8BbNmXO6iwIUdMDTRUzY8OVeZUzOywnosutEXdfJKGx8ZQTqfiT_2MySJDN4SWirttL8l-YZrY4QFBl-znRSJoe1R89IpCA0gRF7kGnk2eVjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyBkQ32551oW72Oo8FrFJKMZSmgDYBkS7M4BwFy-kfmfrKEHOc1Vxx8Oqbm3rY0y5IyYmGItfWEpyrXVUHnEe4wkeLtx3JyORpQexdNaOOyPgyctVN0SzRH0XaILLXvu6hu8KMm1ZVJWji8UqCKgBET3X1BH7aazgNvBmw4b73McrNNJf0pgpU37V2ohAVE-pvV_hJ2EdBL0xsCek7nlFUMeKXnh73crDxXd2qpt4U19SMjBq2YR4vmNSupCCYW242wc5gYwZxCyC8McmAzVtbwBZNh2xT8-C2ny2RSebY3Ll07Ij4jcQMoOT8SJeyY2JyStSJc1NlcBwG82zCQFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXrVZLVd6SckaWlbiVOfXLdaiTPRrDHBRphkKN9qPRZV06BNMPEeslvksp8C0B1tYWvhwQzAM-IJdRvDb2bWwW-Nm6zzElNdK0dDU__t6rmnbQ0sRi_ME2PeNgZz59GgJev1gr-4OcwEW2F4VWGD_XCz8hlj57ZU375ajHoYXdVVY5D6hj1i9N9AC42LJyjbZq6mv9-O0zEoa_whOFAyWv-ujJpDocqXNz7vxieYGteHV9-hxWNBky77I3CRkMqZRmtuJ-UbHoYHJ0xZVri-nAaP2MSf6Eg8KjnVAgS150WqU1-z3S7So9eI5m0UpcN29XEluKjNo7GOi8NxEdSUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVHhuCLbZYJMPLtQfJBdp2y0b3cawfarSJIZJur33QG5laEJ9mySRBv9cEFAIdCJEaxm7E98GJTs088Cd6Gg1IAAvgxKJX4ETgVsJGrGFbvq6gCf0QM1kkAy63yNp1--7flhLH83ec-Ie7yblgI_iLCqI3lEgrYloLiMYsngVmFLHyzT-yDUxlx4ySb0mA0uLviHewdyl6f0DcTBwm1kpc0EjxwPVCq28h5s80VLIAhSr7axUrCveFXR3Zbun77qeaBvMpGWN4oXFdcuX_RE8tgqdYyucdciYrUe0gn2QdYUEiMcXJ0B1wDmk3m3Ii-fk1K-z2orQrNpnVdAlYhL_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
شماتیک‌‌ترکیب‌دوتیم‌پاریسن‌ژرمن و آرسنال؛ ساعت ۱۹:۳۰ با گزارش عادل‌فردوسی‌پور ببینید‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22486" target="_blank">📅 18:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3jnmB53aOwaF2KkxT1LTVadsQrlqyQNt_kBZ4W_pcV6v7xpgtZxuXLdyagp8-hVYLTCmw2ZdCSIsVqsY2FrRrizTCCQgxoGZiwougW3yCT5TlZBM0hQJvrd_Yo41NnUkgBwdvVg3mHLseIwolYFbff9Yn7UtgC3hkWZV5DDdl8ZutOKeBP7UPTXlm-ibwUXHn2PHGublnWILQucUtgD34Rdt6JB5f3xDIqtZ1uGC_qEHDRsmfIAHWqKfYUaFY6D8KVTqaLmKB7t7UewMne8HUNpL_S3aJ9CkJxCSeoTJkSJn1kO05mXyTXMuIh_GATPNyjXKpQPQyQyqKq8fX6ZhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL1t5dmFAveOMeRh7wB3d3RD1xn6dbyQnqocKPrysTH9p_cFYfkLSuulc9VwQxh1IWLYA_1UW4zWLEIhTv_8D8ZYS8DG0NuqZH4jCV-2ttMlFmSn4B9JkFqOXbI5K3OPdaqeTFwx0_WbMy1OBJtiOoclnlDNTdxhPv2OqXu28V9RP25NpYkwVPC3dIC2WP7yIt0IRYf2kOQ60UfFSfANI_UZ8Jm5PvzHWIYIGHinIn0NzhVrIM5vDK_nhyxvqkGPZNNrP1H1CoBAP0VMVHwpgumsMS-KH-0vZgZx0uhDBLayJV-rmkJX7-6AibpFNdiRsyMEf9e5HgB5AYqL_cpFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU3I4Rr4kRZgvfMGIOeBuORCUp6095tMHHJoIiqHn8rt404FWkfw8Jq_pvGAWWqqw1xOrLBXms3M2EHB35wVZIRcoGUFPsQ-POb7EcuQfFPuorSHFzw_FAstcnAMxyyGRWFTj8EA3uFqi_QUeq8g4pM9F-U3vRI9iAcmRag_n0wdpWJA3yLuwypdQ30EPzVnG5fdab-9THMzU-A6zL_BeOj3QsCn_H_l3Zqebm05G8LWjGXWFRHY7hAaeCr3l6nPNmvwDEN516xgmztLi-19U1SizR2fNveoiwl6aL1oT_T6Vv_w_hyNsu5HrKxvoJGPvbpcLY_SWPqgW6rtPpcMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aparat Sport [3.6.2].apk</div>
  <div class="tg-doc-extra">8.2 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/22481" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
#مهم
؛ رفقای گل این اپ آپارات اسپرته که تموم بازی های مهم روجلوتراز صداوسیما و با کیفیت فوق العاده و با گزارش فارسی پخش میکنههه. یه قسمتی هم داره میزنی رو صفحه میتونی هم زمان هم بازی رو ببینی هم تو تلگرام و اینستا آنلاین باشی. خودمم ساعت 8 نوبت دندون پزشکی دارم از طریق همین برنامه نگاه میکنم. عادل خان‌هم گزارشگر بازیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22481" target="_blank">📅 17:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22480">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmmBiRVpM3FB19W3Yi2AGxKCLp2cqjBVgqxayDDSYBe7w21MrAKScy4Crqt2j4njbA3TDkvBxzggouDaN5eepYbU_OFb2qHRndZDYG_W3lM2BTaR6ZrRJ4ihuP5Q0cKHAW4XFRqn_TFHRQl9raJPqcVHjo5vRZSoR_m1s_zl1Ua4HmwTK1NL6DZqizzAbkIPMI6fuG4CbLbWFyTAKu9BMkg1yZPHGK-TCdS1r2xU37go4Hbdsyu5JIx5Sr_Ynh3quAJInaFAcsCWoMiUhfbt1EzaA4uqIRN6onb5zT5U2YgOxCiZCB2jX2YYsXYZZfLH6jOm7MCYonInxyAUQsb-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=tA5sTK7s-ADx7SGrdMrU2mTjRkNj4t2JYIibR2IzUW3oUf-yacOMZb8Xu-15D7gSWxDcp9YZzIgMfGXolu9VAK8C3WoGrnlkgOgn3if954ffIp_f0fJgZB_H-QE26wtrHiL1lMoQwjHxdVmUNz-IYH5UXvEBtQnwO4hQ46mE95qKZ8er2su2AGTlpT3IjfzUp2dcrnRCVLpY1qw5AD4wnlypM1uL50Mf5YBTnfeFikf5EWIYf2LGfh6pchk9LuRaIZyIL9mkhZycbAVeq7ZM4LlvWkHddybQJ_YfYaBrbEk7MjryQk9h3dVsLPChH1Y36i0LQGNqisCAKrNynMJXWWl__c2Ugbp8eJ6Tqca9Jzsgb_Y0QeBQbCGaRnu6YXXyLkfH69ojvWenDgLMJa44_BLPXmsRWBHncKqkOktcs9RslbtuXuen1w6DO6w2Qao_-8hOWoY2J-zUsVIdtUSQ93cTAlJvo-hq_NSNlb0t85KFncnhqi9o-iaNPmeCYyhz05ccFK0MsIt-3v-PRdfJAaLMJ1lhMQ_shDN_X9hmaRo2M8_2gQKOftxFBStp6uKNMPMRrox_h5qIijwZh7tiP-SICiCwb0hzipAq99Pr3-eMue2tKuePxvSc29NXz1nfJUVyJmIs7TJJmfEmBp0XSOB8kux3_3NZC3O59CanHls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=tA5sTK7s-ADx7SGrdMrU2mTjRkNj4t2JYIibR2IzUW3oUf-yacOMZb8Xu-15D7gSWxDcp9YZzIgMfGXolu9VAK8C3WoGrnlkgOgn3if954ffIp_f0fJgZB_H-QE26wtrHiL1lMoQwjHxdVmUNz-IYH5UXvEBtQnwO4hQ46mE95qKZ8er2su2AGTlpT3IjfzUp2dcrnRCVLpY1qw5AD4wnlypM1uL50Mf5YBTnfeFikf5EWIYf2LGfh6pchk9LuRaIZyIL9mkhZycbAVeq7ZM4LlvWkHddybQJ_YfYaBrbEk7MjryQk9h3dVsLPChH1Y36i0LQGNqisCAKrNynMJXWWl__c2Ugbp8eJ6Tqca9Jzsgb_Y0QeBQbCGaRnu6YXXyLkfH69ojvWenDgLMJa44_BLPXmsRWBHncKqkOktcs9RslbtuXuen1w6DO6w2Qao_-8hOWoY2J-zUsVIdtUSQ93cTAlJvo-hq_NSNlb0t85KFncnhqi9o-iaNPmeCYyhz05ccFK0MsIt-3v-PRdfJAaLMJ1lhMQ_shDN_X9hmaRo2M8_2gQKOftxFBStp6uKNMPMRrox_h5qIijwZh7tiP-SICiCwb0hzipAq99Pr3-eMue2tKuePxvSc29NXz1nfJUVyJmIs7TJJmfEmBp0XSOB8kux3_3NZC3O59CanHls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edfW6FjSxK3JBRan5-PS6Mb4rlIE7BvFb6f2Ae8Y1J_blYlYY9DHMHqvhul-7bvt0xJ5XfnfUy_-OfoZZLvooBKYQg0WdEHt_ADZWap9b46D6smKl8LGqzN_HbmNDRaSoaGxz03-PmYC2g1uZuYGsFm9WIIorxWgACElfB9X5OBb2Y03H7FEUbGCySSXWD0JVpIVwx9Thva-8eIm0jyN0uxtCQ-x4klfN117XqKhp5PXMZaZd5F74F3AIImCleS_tctaUpKAMRHWnfmCZ9uudmwFp2CfQ0rFTKHnH4_A2Ha1gcaHo-uBRPbtIU5_DpVCZAieVxByAPjAe2SaxV7AXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6IUY38YzycRfU-I3p3jbqWvo6naL2DFoQJNZjmIoIsL4rcQCV2rKUg3G3Du4XLnV9HP2WS0NLOQqhnIFnmv2Hr6VNoZDjkMerz714Vh1vRTDRjVp63hG__KQvA8QSyljlfP0e9B2exqXW35F9qMBYFnCWfxmzXUZOc_kctLUu7ADnX8R-1JlHFCVvSBP2QjdiJbxGU_4mCIi3YCgpCjVA97OfXuIi4LbjNn4bHTnKG5twRWJVRILQrUeSAJTapPabftUpDbrNGBeqqebe8Fje2gRWjFVSgW9PPDNNcitAMPLq-1Mya_1rXg7nknmto8Hx276nHeVaJIbe5I_QGcXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری‌ و خبرنگار بازی حساس امشب دوتیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22477" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsnFaurgnny4I3X8R0YX_Ix2VlY7nLGEp2t1aYNlxSNQZB6NQ-NYUaPEtJNW1lEtd8EEYSyTOvxAuUVk6f0gQjhLkdL6OUcQg5y9Dsdd7yHADqd7dzwFYz_ue6mhckUylEBdhTBhBIipcs0WImvWR-okFIw0I0GUhx5cAR1NcT0rW0E3PC8LfLaF4S5IIYDJOYO8jozjcPFT6k9XvVvEk7Z5zDJMApeVgpFNEDMwU2SR8EgZ-Ca6RqCKApctvijhV4769I0TSvrPEUSOgxuhLndz8s03X97ueeTB6fPyBJ7Y5U3ODoiNuHnSsSCPDFn0ROwT4dB2VcFzRLUpVevM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=j3yeNhzu7alWLH18JbTGATRGaTgWHsMaqQOj5uE-j-j7dVrxo2_basMKepWVkk9CWCbNywvVwgKamIsvT7MJ5zj4cW4FwVOZjAj0yQEfTHxfi65nF5l2iODO1WdU_DBYbCkoK1OR5kG_LhYbKG8FInLc3dvLFnMi43Deh1fb3xsyctZxaxbsgl2bbZn-6tw8KfSb3y2ZUkWUesvokIV37RR3F1VNQrbqlqy7Q2mBu3bXOUXQypOVcZv90qbGF_j6bpbdbZXj4ujEFh-1Q2S_-oVFlCkeM_9oWAtoB0hs_-0Yi20tvlgKiXkCg97X1Hx_wAzReq_P8wH5bwHWKHRBlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=j3yeNhzu7alWLH18JbTGATRGaTgWHsMaqQOj5uE-j-j7dVrxo2_basMKepWVkk9CWCbNywvVwgKamIsvT7MJ5zj4cW4FwVOZjAj0yQEfTHxfi65nF5l2iODO1WdU_DBYbCkoK1OR5kG_LhYbKG8FInLc3dvLFnMi43Deh1fb3xsyctZxaxbsgl2bbZn-6tw8KfSb3y2ZUkWUesvokIV37RR3F1VNQrbqlqy7Q2mBu3bXOUXQypOVcZv90qbGF_j6bpbdbZXj4ujEFh-1Q2S_-oVFlCkeM_9oWAtoB0hs_-0Yi20tvlgKiXkCg97X1Hx_wAzReq_P8wH5bwHWKHRBlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP5UvWLYX71W8cd_BkdH406HdtjyiRkubOmAwKYyq7cpObOKbaRiRj0kbROZP43vTDnBvRpcY519lcVgglY2zeUDwiuNke7taoxcJlIHO9PICRVt-xDFw62jiJiwidQazYxAjqq-WUc8NwzR-1Mvy8QIlTbKRPwkMekTwnkfrJlFaAQE97Z4pJKDSr4Fm9ZDnEk3GMAEpjsCNkRijObrOd4PJ1QClhP-6nJBFs1HKTRZfqjpdW7DQOz5XdSZ9669wOmLxYT1IxqKmrC4HzoGZi6smrxATzLfuN3JPPfiqtAZOKDrocC6sULpWW0uMqgrAkPQzSBbwjqRGmGlqNlsrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIYMOYSBW9_AxkPpi67Se1alobuoBDNFT3JdHhVl7MG7lXbT9xrd1rS_n7-Doy2JWzyrZGUpyAbbX8KfzcxlN_G0UxQjo2KpAjLZsanYSN5e0Lv-llAopEOfR-p05SCUDEY8UqBzjfcxQ_4X3B2vSx2lM6gmfCjY7nQCndOxKufFbuV3RgJytinZOb7ApkbprMmopu84t4Z3KKh1w0IBpmREa3qE1nGu05fcTdWpWKzT6KkGJkKTeTfByOL9woibsXw7ILZgykdza4g8zw4bPGb5WXvsTyfMajEwxGH5EDglZ8PDEX9OeaKHD6m59d4yPof8ha-YCY_P_eigVBkNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKBTW_9YIUIEH6fSS_-bIdANcj4xC8AIQ7Q5rBKo_u3FnZtUnjQybW-3pTK8FvYj3KoQJpqO_XqYvVlbgSVasuWpLVCwYwvgq17jEmrOXweatAVjZskQ8hqq2zS5m6-IY7XzJTs7VVmZlHx_7vmz1CsSgmC6OYgitAmkwac162RCWzH-NOOCEU3Xf9-Sa9g0tbmEskJA_jEoF9wvHRRi24N7P0B4Gt6lzgbnoGryo50hPPlJeHPkqtjkAJEdtaJZny8IfzvFxIdtVfDbdh73WholBCWfnLgQnMBVn9SGcFa1CzHbZ-q0LYLUt-lHpNQth7wqCjqerY-tNh8-zz_G1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNLtpYp4jBk64OtasOopKCyv7_fhJT-IjjlR6hDHxC7suSoCVRS0XxlD22YmYWQYSah6BJ-GjSVGDqIVKvrD7scQM7v24uIjBJWtLqTHmF0jdGbeRoh-upRHjh0YVls4eeu-af0cA5J70tr4eE6mO3QLR8zh_kD0hvLQB6sy4rR4ReMRZ3c5PsZ9aJ2EqoctxnJU6QY8zS6kU9WJn3NyJ-PTJlQFa5IdKYCcvMpjmNbw83qsq_DNy5giSI-rHNoipzCmERattPfgMcxYcQh829pLwMIXTq04fmtIq6FQhICSHDJufdlElT-Zg0VAauOnJTrXIOLn4ys_aoWawK9A5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0gk_JHNsKliIpU5M85-TE-0bzwFgeDyp5JPY5II4M8mBf389Z0tohxxVUenkcCKTEvKVbKiR69LfnfZYGWMdHupZHWw78E4AM3BmbMQ7Vji_J6PuABzV3FcNzyHO42D7qlx84uQgKW3qlbTHh6ifKNygBeTFMCPwXntTsFBoTBnPkatIzV3FjhtOh6A9FKtW9QzYWEbM1UwmmNcVy_27S9bO16kwKNGnjy1dXXQ_L99ZdwE0URwYtPADvTb8JyCu34E2sI4n5BRpbS8m0DWvAt95WYS6DSxMfX9O6hY1v_2S1tOYVR1jqwV5o4tlYDxTf7nzJB1yiWa87iZVSeJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4y5SskTC5EZUPsDMjLc2MvRFAIb9NjAhTA7JBwItxCPkOFtn9SMkicLyvscM2Rw7jhJrMYHwgFXlk_gSJzNZaVR_iYLPpuN-lg2c_bSAAsXWJVB3rrqXKhT2T4RACidPilAqlfuZ123WRXouQkFcgbNTIShAHnLj9k8LYe5SBs35ENAEC0ulItrDtdGG0O_2b9JukmoHJfUkuxVV8V_zDTxumlhirqTnR5aOgQrLlaTyR7MMStKXW3xiaGWVjUFVtDclcMrwYCkmKL-mATUkgYTix9hdbdenNcjBX2JURVrKtHUbVS9gjuYoYcud_yzSQQyuMryvXv2T9-ls7LKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZnimMhAGFNGp--GJ21Ce1-JySyHYg1npOLT7-fARRrM2zCyzIi-JJq3hEYStyT-tajOMLuV7L1AXIwcdY0PPBXAd6oLfQ6jDIxIa6OpILn93x0bqkqDNlC_T2qEx5ZdQMccLljt3K3Li6gNieAfg4y8Rkj9eY8Z-IMsSVqtFMpH4bXad1ZxaLzlXf-PRWJkbDR9gYNQ2-ok7ZpYQrdiW3tB4HTALa7Ie1pRGeqd6OQ1kh76gEEazsDntmEnFN1nduDgRMgOjSic_Lp5CSMdR3chtXvqCVrLgVihaE1ckNbnO32kN1v79aJBRmW75n8XnfnWA2_v_mHMxeXoXfvydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4hGr98hOXi7Vz8UsykVVrx3AV_E1g9w-efnjuhHY_aXLOtqJneSQGbEzJo__5qZd_2IzjY4XQbp_oOLhKXOKYOss7YDoFZXf3UZk37_-vNdMHaMon958wWt8A0XYsdcgsJtVAE0vQeedEJWCp7fExE32nSEZGRr7TsvpZYf4H9k3XmrSZ-qDpcXhxxLFrBD_yhFUHpIRUH9repOikgCNHgdlUSwgI0RWV_lqskr4PM8F8QBKQS17S_awYrDd1KFYKG7DkjlZQD5Co_HIn-SMKpeKExmDVbeLeqmn8BPEyRDuVykgnIFik8eE3snIuPQSn1AXiVg0-kwvyqCsCAwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj2brMkJ7ZkLtmHdSqretzcv2qym4UshOBXekHDdoWzV1cLd0UBI95ceihikkRqTeXrOlwEKTsJjkmV1HVVnhGhKXgsKMGR0n7fFSwZpahHhS2-EmFK0R13iA-phjHVmWmx1sgAaPi5BLlI3T2dWJ3FSK_MBSKNmEI_j3153fq-TYE5GOQmlQ5VZn_6sWmTw2LQiK-fXK8HcUDmPca1y3y0Le9ujHT66UyNOl_kg2BaCLddJuBAR_a4fNqbwVyKpx7uCeYAbHs5hSwnfP0bpcv2Dbd_rWk6y_pMsTsB8Qwpn8xq2HbRO8RO4cjxLtowCVGtvDc9WQ9Ys39LwEvwQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY-srLjWIrV9BW2wDiQUCtKFt2oAmrNC1TbsrKdONO1zef8WAcmtD_Nf0Bv7vHk_h_-JX_9qRTDMQqgFZ6liDkvAy2c1qRjKK2SOOUSwdrMGkaci772IwbClYkPGO0uY9LxvzymqR4_HEcg72tIKDJ9ZFxoKhV80AvebA92wYp63ox6b3qJHoZgdmMU0aH3KJs4ZBAQF7_yBwK47Itvm1ISPjVT38bfEPtoA0VXBMAtyH-m_nBa2K3j1pUgI2w6dV7Dnw_SGqPPu_DZRNBIuBie44pGO7KvrV_rAcK4IiT7X9P9ePcH-eAX-gp4wl06AjI3jIb5RuP2UJYEtGsq2Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrFXMTGX4bowt9fzEKfyRkRlQxp7fQ1B1zFRU64_Dw6xxX7ZAltWZBu3vzfd8ov7mcyhwvKSu9awHIhijE_AScwP9P0b4BUv_f_ZT7wnebhRN5ws237yBjaxqLlXlUp80vCgF8WdL4PEVFqkCUKzbY2kOPOx2fI_NxZyxJVPBYxhQABNA0eGgb8PnPXecRLBfdLsDqSW5tW_LeHGLodMNTf6MjipIdMrLlikL4beVsDQumbsBugYvGPpBMPeL7ubd3yuRhAmj60J99rouLDB5QXIbztYmuhRH05S4YGmuaRNYtosslt-Nq94KSNjKL6ufZcn101psHsrcjpeMyde6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8PU9Ub1IkyCQPwdQE-i-wcO4LKuR6wivPmSwtEWcZPzEGZpJ0dzPQhuTU07nykJ1LK7eSSOWDTRCOV3BGDMnrwXMOiON5Ml2kJnZ5r-mXzt-sp1zrgWjtWNVVpSqrVEU1WMF-bJMn-bTrlBlEWO0WnDNzZPw2WqcMgpv6Bz_JCNSmTcNkMj7e6ZA2xLM-dGiBUYm8KcDaapPz8BuGImfIIy_bMvX2jYsD2TZ2K6POw6BFuXAzdzJghCb6SngGmq7TfHLIKwOh-1td9dB4y5hrZOFxq4KLrUJc-i9zpOzrFuMSfEoxOeMR3hr3_rGvdrqVttwR24oETP9YYytk2o6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsi6r0P-_Qgn-6JEoZhuNRvjk1aGo_QafrkMe0aitwiEQyJ3XgQwaqQL0VRTuLT--F3vDXbHlGnYUJTk-c-6jYOU1EuNvRAwxyyUylOs6VdTQsIRJPoq1bXnCTgnWKVeHgmsGAUbeqdXaIMfIkUWjuQpep3p-WUVowS2ZeDFkd2k7P86t7bxWkZWur6DgywnPY5hYp_sY2FKGej6N98wQa1K2oJel1BbsQdYsZZqhj27PD7gJWFGuSjAR4-4bzbPDTa8AdoaeRAL0R99nJfTrnvzRMu7CAVVicEEiH122O6qOllUWbOIFNQUkfO-fHvfwONLsRYCyf3RdtCK8B48Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKfqNDdHfwHm6xgy6ptfDskr5B_x2YTWtgdnx4UKepbk5R7KEkmf2P-J9PrPXfOcIUb1pfiLQ0Msc6xmfwG4HBFN-gIrS6eZzLke7e91EtnCAaPHwOnFwKjh_cgbsEk2HFn_yW2dr6fvuTzRRYam1pnzRpRyukpVLpVtbI4gmt6Qgf9f6lhRMm9Zy5dcU176N24NQH1l4Q5tbCcsffQOBk8zK4uuy1oe8kgFdY0BYBpJ80aMzTOeDns3cam-nyceCVaNyOkiiq9bq5Caum2oEETla_AyhSl4cJa75ig1mPkkSN64M5fciY5BKYf87-lZA7ItXm1Ee8vyWwRbT8886g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atHFtqNyEwnmpFlW3869zMxwywQMOgiIadfD35y7fPQTZNj3wJNzydZS5HL3_badnv-T7R13abfbI78-rnbbf-KIwo5C3LzcdUtYh5eXEOn3KWowHkRiX9MChjTA2ROZX5wt8yeoWo0Soyk9WNb3l3RVB4tGcA4GVazmPjnNrK24KXCpLnKq8cKoIgsDhqsdzunzaRDQFJWacLdz_O1rwptLDliaqcYp10yJdh5UQiX09WBSjGuvLu1fLG3VTAZaENBhv215I5EabCz_lRqxab7sYdjBbt0ZxB6YkqceFD4VnZf8wAP3RvwBLy5K2Qcxh_LL4HTYM5lLPziHgvpPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=XiP9ixOHoOx8Xvg6Muz26qCcM3HhSu_KhIGoYK4gxlR3V9bJwtb0CgMg_Y4thnwHccCewS7cEahOaMalESgedBbZKMVYqyDqXrb3N8S89HHY_z59BtHy18T2Wu8Ik6BUUyUz4s_vc2lCrjPm9aZuz8Mgm-vCSObW8YqEgVTUjKoWC79JOHp8rFZhynXj9xFtWuh1gCRF0tA_UC7anM1dCg6dwr_K8KRRuiSREnRUjwJM1ibq_AswPf7D-v4hpJIoZmfer5nTxGGbXcusk_q_z7cYCc_-BAVJ3--0pFdJ5oEfbmfbSmOzkVfmipq_CEzqImyn1mIrdAE__j9ejoA6SmG4-Jgi8a26BeiLc2wrR_gLVNYCTiWJnvlenq5yz-tdo7eoSYTygbfaNKWYLknMh3MBe_TVSxHFBCux4Lh_IrEs-11RjkBqt2Alx65OI75DN7T-zplbnpZs8sC7fkYk4pUPKy5EfixSPrV9L1USrWquLRCYFYjsLjSO-H2Nd2_CglZpBsxo51A-Ks5RAOgB-wiuB__5gjoDfDVec1PL_4NWf0S_xrJdWHpkwxRp1EueT_Ek9CUxvjqRGUE40uFbh1iXn-Wcnw1J8UvWn-KOfBXLLtCV2uhu_Yu6jDAC4Vub7W-ve4WyytHI0PIpPwQ1TZA7bS6O9MU5S70EcMVXOsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=XiP9ixOHoOx8Xvg6Muz26qCcM3HhSu_KhIGoYK4gxlR3V9bJwtb0CgMg_Y4thnwHccCewS7cEahOaMalESgedBbZKMVYqyDqXrb3N8S89HHY_z59BtHy18T2Wu8Ik6BUUyUz4s_vc2lCrjPm9aZuz8Mgm-vCSObW8YqEgVTUjKoWC79JOHp8rFZhynXj9xFtWuh1gCRF0tA_UC7anM1dCg6dwr_K8KRRuiSREnRUjwJM1ibq_AswPf7D-v4hpJIoZmfer5nTxGGbXcusk_q_z7cYCc_-BAVJ3--0pFdJ5oEfbmfbSmOzkVfmipq_CEzqImyn1mIrdAE__j9ejoA6SmG4-Jgi8a26BeiLc2wrR_gLVNYCTiWJnvlenq5yz-tdo7eoSYTygbfaNKWYLknMh3MBe_TVSxHFBCux4Lh_IrEs-11RjkBqt2Alx65OI75DN7T-zplbnpZs8sC7fkYk4pUPKy5EfixSPrV9L1USrWquLRCYFYjsLjSO-H2Nd2_CglZpBsxo51A-Ks5RAOgB-wiuB__5gjoDfDVec1PL_4NWf0S_xrJdWHpkwxRp1EueT_Ek9CUxvjqRGUE40uFbh1iXn-Wcnw1J8UvWn-KOfBXLLtCV2uhu_Yu6jDAC4Vub7W-ve4WyytHI0PIpPwQ1TZA7bS6O9MU5S70EcMVXOsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grgByho5xOki43vxD4HpF9Hp6ArIQpYCXAx_R8d98kVEKULglklOOWOnupYVokHQIVS1YzP_bDJpQlllmmLPtJNPh6ndCZQyl9styquEmpjJkQhSmZ3Ff4z6tEAi7o3PzFFw1cXps9fSJ2Rmnt2uvVFQge8ydFZd4jWeYNKZ2xFGWX0F3ncXIvSh0tcTzRCI2y78q_XHuPoiPsPvEbx1zz7vORqmLVfVUcERWJ2hMsQzA9L9MSJ-rolrJwXDqQkpjVa2ZIiF5khGqrAB6WXU03hHev70V31Lh3WrKubHJWjoRSIZHEyJX2oYiK1Uj7azyCzl8_20b91AiiRYR9stwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFFxnEHYv1mLdUCfWdu4azP2e-Won38ucI4KrpKvV9lQL4ilP34ptCF59TybOl9JX5sUVLjyZHkcSHuR8Cc7C3ZtRiForW2Iq1g4bXqoVxcVceVhXVwyh3HSGvSKuiqUhOuhyLb3ZxBfJNz5sL2weujUIOraWcpK-KM4_MI0c39dafy9EHT1RYZkNCHzyDHtoqqKevWxLu1idOfIbuPNYeNAimtOAEpaGdbAcXSAIUvWYPqodZr0qJ9aT8hbbA3gDUFG5_LKjvl3TYSXOgBBQREOTTNjOhv7vUIXB1WNI1gpkU2BoJSfmb_lRZ7Yk2WSEYLPgABKWIGhWbB8vsu_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myq3Lw2sOmtWcBc2aY4vlwn9MTZ1tbbiCS4QjAFMz6WQw41UIqsat1rZmy4RaLRCvp_uesFuQXGZN9AlINcaimpT08v4K1u1wY42mfjlLQygMmejFqtnU7yBfJrs1NkJ5dFJN3necBoap3XgWv32WHu130iS-Jvm4VrxpoDGISUBmI-UIxMWkSDW0K6d6sXgW6ROvLw9NZmQkjZiO9Xccv6DEBNhwbRFhf6g-JjNa6lGDUaKwiRbqNWZ6SfI1JIphmxzN5feshJy8BivB_jKcDvHSyWq2nVDtDKoDF7kzd8b7VMLhy3PT04gWbxo8UyhW95sYScs-cwpavvzCnxung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=ijLq2hgQ4CkoHbB6FCwYoWLjUitDCy-2VaD68FMRE1k0y8lgWFge82e8VfNGdbmGxmmCzRG6rgsYEVjMG1NHXhhnAYLsGL8I-AjepwLjey3_a_K29gzz6ikZh1252XKhfA0jzk4GMCjjaW0FaGKf42sDJ_DZLPkczLgNParu9OOfyc6fgD5gAxe1u-xou1f7FugUQJw11tRaCIlJXRqcQXSOREoYOD9vJ6pE0vzYyvbjxC5WTZV-EfHkBnhcYNJyUsXeJBMabFZ9RROJR58cwmcG49X5U_uqOqflwDsFOL5sjmj135gy8e33_og_zM3nHH8Ms4P9vFtQkxrQ8UvkmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=ijLq2hgQ4CkoHbB6FCwYoWLjUitDCy-2VaD68FMRE1k0y8lgWFge82e8VfNGdbmGxmmCzRG6rgsYEVjMG1NHXhhnAYLsGL8I-AjepwLjey3_a_K29gzz6ikZh1252XKhfA0jzk4GMCjjaW0FaGKf42sDJ_DZLPkczLgNParu9OOfyc6fgD5gAxe1u-xou1f7FugUQJw11tRaCIlJXRqcQXSOREoYOD9vJ6pE0vzYyvbjxC5WTZV-EfHkBnhcYNJyUsXeJBMabFZ9RROJR58cwmcG49X5U_uqOqflwDsFOL5sjmj135gy8e33_og_zM3nHH8Ms4P9vFtQkxrQ8UvkmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=P_LaXxBtffH6dFIrXNTCXs3KaqM03QWBRQmuQxEAoghfyrV1D8FAJfohhwZzoIXBxULwPHqz0M_-zK4yLBQqBCKWibVPzrYn7IEHcYr4OCM25XK5mLHgynUmYrUHwKGho8JZxUMJ30XHEFV8Ac4AdzKMkA3EdYHuGUzOoMPKbsIH8s_OBdCyASNesuhUeSeh1IAAc7B-l3QENoe1vcDv_SMWp0bh67glEKg1elaise2BRTrY6HsBaCoYMGzi2LueetxMFVZf4f8y9TgYy2yb8eexTcFzInT3G7AtHniUuiXT83Jaiml82gAs0uQ0F1t4yFMuYjYolmDE5iPJq3Kbar-lpMtOB8bm6uWisTt_Nz9jKT-iOVqP8K-zO1uSMJrmMnLyWgLTfjDlUNCoMz2FUXT-F42t-uM6i-iNAG-NK3g8pfCsVfBoUh0Iy1q0jXgpRHJT8oQep-8t3xmQxsQCIMSL8ZN4r8hgU0qVoOfc2wKKKjD80it3VRCNEYZ-JXVfSitqH2HJYvo_UBexlss2e9BK5aJ-q1sUAtGvYH8fNWzxtI2X_YBfzgKIvLKK7O3Sezm4dkuFZC9wuDXRkG8aWp2bQwSIO3QxHEA_xb5qHwuXJBjl_i9v-aA8QJiXx35Jtm9_NRaksFsWHIgKwKiE1j5l-c7WqfbkF9U7TTuQeGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=P_LaXxBtffH6dFIrXNTCXs3KaqM03QWBRQmuQxEAoghfyrV1D8FAJfohhwZzoIXBxULwPHqz0M_-zK4yLBQqBCKWibVPzrYn7IEHcYr4OCM25XK5mLHgynUmYrUHwKGho8JZxUMJ30XHEFV8Ac4AdzKMkA3EdYHuGUzOoMPKbsIH8s_OBdCyASNesuhUeSeh1IAAc7B-l3QENoe1vcDv_SMWp0bh67glEKg1elaise2BRTrY6HsBaCoYMGzi2LueetxMFVZf4f8y9TgYy2yb8eexTcFzInT3G7AtHniUuiXT83Jaiml82gAs0uQ0F1t4yFMuYjYolmDE5iPJq3Kbar-lpMtOB8bm6uWisTt_Nz9jKT-iOVqP8K-zO1uSMJrmMnLyWgLTfjDlUNCoMz2FUXT-F42t-uM6i-iNAG-NK3g8pfCsVfBoUh0Iy1q0jXgpRHJT8oQep-8t3xmQxsQCIMSL8ZN4r8hgU0qVoOfc2wKKKjD80it3VRCNEYZ-JXVfSitqH2HJYvo_UBexlss2e9BK5aJ-q1sUAtGvYH8fNWzxtI2X_YBfzgKIvLKK7O3Sezm4dkuFZC9wuDXRkG8aWp2bQwSIO3QxHEA_xb5qHwuXJBjl_i9v-aA8QJiXx35Jtm9_NRaksFsWHIgKwKiE1j5l-c7WqfbkF9U7TTuQeGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=VlbDwIjO2YuZNTFQRaFJwMGxenoUCKPIOQbPjAsTXZ8wCKjxNmpQ5Q1fyVznRAz6aSffXd-A5hKE7-Vr49ZpZOha_qljCZ4RPDyQBUz5WO7wMR1ScsNOJ68nZNnT2dUezFfCfBBmfqTffAHBF5DzlV6o_KIHQMS2J7tvFA-OcqneLR0o3xNkufbMuO9NWlbAj_fmUiLTu07LxoKTJUw8IaKYKaUYhjk40vNImFD5DkRqiZLITkHJurdosmFtEYd6pYO9egTMD-Lb0HUfecLYOqWQstIRoxjOKKFBRHIkdC9ZGUWC9Prkp0aO1FMHsKYBZ91yz2Xnx0SPsVfVHTTt7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=VlbDwIjO2YuZNTFQRaFJwMGxenoUCKPIOQbPjAsTXZ8wCKjxNmpQ5Q1fyVznRAz6aSffXd-A5hKE7-Vr49ZpZOha_qljCZ4RPDyQBUz5WO7wMR1ScsNOJ68nZNnT2dUezFfCfBBmfqTffAHBF5DzlV6o_KIHQMS2J7tvFA-OcqneLR0o3xNkufbMuO9NWlbAj_fmUiLTu07LxoKTJUw8IaKYKaUYhjk40vNImFD5DkRqiZLITkHJurdosmFtEYd6pYO9egTMD-Lb0HUfecLYOqWQstIRoxjOKKFBRHIkdC9ZGUWC9Prkp0aO1FMHsKYBZ91yz2Xnx0SPsVfVHTTt7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17964484.mp4?token=cV0m-Es008FWeMR6kjexNEg7wDcduUEeH-a90mdHVsEThEpVbIJkxv5BQSi-fZD0O8rcv8oltQRaeiarTeBb5qegxwQyxpvtndei0nNu5Zytfl92WzIBIjx9fg0k8AGAvDghAbYvLfW5lZqEJ_x07pgScpnJuvktZLJk_mTFFMty5GB7EhN4R0lG7eHTHJ53lgZh2QYrX3J_LSn5GnHDR6SemKHtywXrXR7BqSKoUgCIVVwUQlsYzI1qpDWh2xQZvBOdEspqFdZ4MYT9NoKh7lShcGte_EL6R6ZM2Kq7MLGmC71AYDbWxMXrDkonzjSvMdFIBdCgRCI4HNMYSg0biQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17964484.mp4?token=cV0m-Es008FWeMR6kjexNEg7wDcduUEeH-a90mdHVsEThEpVbIJkxv5BQSi-fZD0O8rcv8oltQRaeiarTeBb5qegxwQyxpvtndei0nNu5Zytfl92WzIBIjx9fg0k8AGAvDghAbYvLfW5lZqEJ_x07pgScpnJuvktZLJk_mTFFMty5GB7EhN4R0lG7eHTHJ53lgZh2QYrX3J_LSn5GnHDR6SemKHtywXrXR7BqSKoUgCIVVwUQlsYzI1qpDWh2xQZvBOdEspqFdZ4MYT9NoKh7lShcGte_EL6R6ZM2Kq7MLGmC71AYDbWxMXrDkonzjSvMdFIBdCgRCI4HNMYSg0biQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
وضعیت خوان لاپورتا مدیرعامل باشگاه بارسلونا در روزهای اخیر بعد از پیدا کردن نفت زیر نیوکمپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ7ABlWQPMp0nfI4-IzdeK1_AW4GFsbwsrLhs-krWhlAGMCn-fdv5cKuWUlUj_lQKfQNzpJq0tPCO1ObRZiao91198yub5ukNEx1yZB0jbwe-UTOT0rY3JsqzOc1_76r6VfP_N8ueTdqvIy0u5j61_RBqbVddmgmavPm0SRvysOWgdR7zISHQfbHWWzQs2fAGrRldIrCud0VEA_lKRhE9-S2atbCm7CZ4qFu9CUj0MyheZ0aD2u92rxF7EpEQYeMvWqZvSolboX5ut0Zqb_r5GI_LkjnfTYEdvPV2oMJKDmmXIjTOv9LBJi-TA9NdEk50VlOXqLq1EMt8Z9ceO3knA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RahtCulhXpTNeK4nIK82ZhRS_RMkK629DxOWAE4b2xabIe0JSmxSYBh_ioMZBuUHYDmU9wyVpGvhSe4igeXH8PZutFXFlXRqwsrKKj5sYA4swuKoyq_4kHbt1QU68QzvZypdFhDrxQ60b2GnJWvolktq_cHxaEI1bLxtToRQ5JKJbt4VZI-C43a4YpUq-91c2CpNX60BqKkwP8-E2JTYHttLk01aFv1hqem9KtYSL1Q7vLPZG72Bj2_Z4J18k6SL3KzSU06ed0UYpkcD-Hbl2omk6wClERgsCT83ks4F70EljZ_7orYkaL2LtfRQy4RVK6h6pophI6R2ZpgiM1loTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr_cJ2TdEgQJMcwsfTyoPnpz45nhm_b77iJan4046Wb4BZmbZzh2udEm8N4u70rrMFLIYotna4b5g3Z7-bXhl0I-Z9Uh41YB8zKzk3u8lUjSSzjDyJUF5QR-AafitnMPRMc-5Q5-ZeuSmFBMf3TR6VCSiDQkugLiCb5l2Ow3kd33JO8EYjJfsqWOs1WjixBP_8DVYMOLpO0mRkvd2ucg_GxiOMxwwQW6FtqnB20J7v9iW60lPpheIm8vjcrjjF6-nwTzg7NQaC8ux2AZI2rK7bLVX1B4XeeRZnzq4oUKwPgXg3ryUluYxz4NX-2_O6M8iOaSOUTLOHI3ejhHDDiS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
