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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 19:30:02</div>
<hr>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_5VZ6qkaMgd1s2E7kv8kFbLG_KUUp23sN59dmDwwPSWQCVNmBq_XhR562VWCmV12GxNCMwSsCJf8S4ktkflIC6jp65t5-oL4E9X2MlPdhNfJ3e5P3ylyQngasJqDsM12fWp01UpjJp69IgUgyzIbwAUR40dnaLfHIC7VdCSJJLnqvNWSFAY2vjlojDKJgadM1rbtv0EL9cpbUm11zWEB58rDQ8Day79r34m1ciEytC_koBO36f0uHcgC8odti-rhqOJAcTw3CjEOPioBy48A9cboAGtZr_mjJDIVKUy_eUMEw9Zgz2X3E4a6cKS-7VmoZXAX2B6Tr1DCF5JdkR1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|موندو:برناردو سیلوا پرتغالی تصمیم نهایی‌اش را برای‌پیوستن به بارسا گرفته و به هانسی فلیک برای‌عقدقرارداد دو ساله با آبی اناری‌ها قول داده. انتظار میره بزودی رونمایی انجام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/persiana_Soccer/22553" target="_blank">📅 19:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCtwGVF6iZk_e0FI1LxFTJvKIgkmssBnuDSI6GQnNiVWXS-DayzQAepsG1kC50LEPl3yhUpBkIvc00yMURyyl8rELHsUGNMI94WCe5nE-8Riqq6FLbQ3xh9OPVv_2bErEu0fIt8JreGbySkThNZojZq59um0n096-T5GWMgHGbIANDJ6SEf1oQiokB3fWmc1t7foahiavgdEiRJeN_QJmTiB_O8eoT-1QW1EIRw4iOEiLEMrV4P3nuXZno9C1wcPO3VmhUNH9pOlKtJPLn5n7E1_lixCJQa6U7LfsgvdrEu2eYI3GrfI_kZlzvCuMwDcAbZN5n-m3110e-I7Tzj_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛مدیران‌پرسپولیس به فدراسیون فوتبال اعلام کرده اند درصورتیکه این باشگاه فصل اینده در سطح دوم‌رقابت‌های‌لیگ قهرمانان‌آسیا حضور داشته باشد موافقت خود را با قهرمانی این فصل استقلال اعلام خواهند کرد. پیش‌تر تنها باشگاهی که مخالف قهرمانی استقلال در این…</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/persiana_Soccer/22552" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/av17zHrAdgxtnYsUQhTuIp_6V1zhmwoIxqQJXUHSep5S20BNo11fNcUNevGWHmFCAaFLK8YBU-f4rc6ZnpsWIOJColw6Ur3JNloMj7ml_uXYu-XMqfsolGjgyE3Ijo64w6NTp17xH3JH4D9Mv0hqLhptOcqI_R3u-2142CC90ljH7pYZuEu7sORWkRCJ7bOhe0PAzAfk_6KJ1ECXoPbkoSDpw5yLBveVsYkyGOuzQrOIvyiAKpV1e-hrrzUCE21cB_lyzOfhLcSUJqHv1YIHxJo9XlaSHqqRmfNB0S8kP-Sz14-MFGao29U7SIM_lusk0f2hZ5NHTqWNhYuCYVYklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aASV4Er8gMiudfXMGhfNvCHb5fibyB2lnCia5RK3lrxUL_JgJeFTon4-0m-qMOfYYc6EYGBwx9Q3r-fuI0MgVjR85cix-4DVj-OF2LjojqP1nVsbGUVsA2FS5h_74GQQi_Qp58VGlNxqMqw8bzcqGtAOd98ja0Xf--4fjQ5dMkIQc12jz8qSOoiFohraVUVWeI386tgBiD5rXMCdydvBFQ52tpM7ODOfLjIt6W4bIFA_dl-CvXz9hKeNI9MCEfXYSW0rSJpAqH32HFzcYPIqXfZuTNjAt9Tp_7_ge0XOkDJEKh8b-zrHAbN7_IlwFCzUQE5QeU0vz7i_KHRNm1adag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👤
رقص‌تماشایی خوزه مورایس بعداز قهرمانی الشارجه درسوپرکاپ امارات؛ برگای بازیکنان ریخته. انصافا دانش‌سرمربیگری‌رو داره فقط تو ایران خیلی زود قضاوت‌ها شروع شد. حتی یه جام هم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22550" target="_blank">📅 18:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdSsmIeSqMVM9-5L217aEULWxs3MgOPz8Swsvrf-VbydfJnHCx-oHA5vRyu82AqhWOG7T9Zi9ljLb9yrFYHFlSZQwqCrtRaBhKkqNTWZCi-v1t4XPGKbAyaf5KMCCoQvvtOjWzWNkzd_iJddqKgWhT-j1Uip47C1xqDRpFMFFdKNEIQBb-WPiShO3Ub4r5SnOwkAVUBwZIo2dpB4AuUr88Sf1yWsWtWwMkqZ5MIHK06hOoRL3n9SmgureJe7_wrW8oK-rEQqYaUq-a--_f3yfa2JVHgJvsqDw96m1UW3WXxwwjkSvDnGw8I2bfkJj9EYCRDxIDg4zKoNUoAIYZ2_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛
مالکان باشگاه پرسپولیس از عملکرد مدیریت سرخپوشان در فصل گذشته‌رضایت‌کافی ندارند و ممکن است بزودی اولویت‌نهایی و آخرین فرصت‌رو به حدادی مدیرعامل فعلی‌این‌تیم بدهند و درصورت‌ادامه عملکرد ضعیفش او رو از مدیرعاملی باشگاه پرسپولیس کنار بگذارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/22547" target="_blank">📅 18:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22546" target="_blank">📅 17:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt8RxDaWbZM85ruxIzXeO-0n2CNT4EdFJdTwLsL2T4FWxVKGYikixGoQiXOVLKuLeUVenhTVmcOoayEVw5J_59Qqd-useBIti6t1Kk8VRkpPmo1qXoMpFuVH9qXfQ8bA3Ika9btqG7bDrtWrw4HueLix7mTCuvrYdjxNsT019POzcTQRiXM6uy3vCakhis97656xFjdtu9yRwPSEWBv5Q0J8BJLfWUe6LViL8izYWOhgVmr4VCuex8FFpzfLchcPyG0aGIxiXhNH1P2sqCbv4-71iAkrjQ4Ww-qpb8hS6R9xX59jmmSwiWtXC-XG26ZOdMKKpKt5iQ22lNgGZyqeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی جالب از جمع‌آوری سریع و پشم‌ ریزون صحنه کنسرت فینال دیشب در کمتر از دو دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/22545" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYSs65hm-hwRxImADxJMdjfddOnsAn70FK9YNDyHJrJTBpzczsxGgVrOgGsoKWFRfp3snWRXtvr1E-hBR4zthtzNLoKAwlfJ5aMbVz2FQnk5dF_XVbHjqfjkg3FZr7IriAvKBcwTUtNPKV7MixiG_J9sJhLCKLD3pyHButsevD9723UpXrYb9-zMhoR2AasGCjHo-GgzHlp4nsMaaMmrSL83mlv1PmVe0DZ_CFNPTNfEvyonH5N9Y8zDd80ZY4LNdTT4KEevpwbBQlUn4FW1Wfg9Iew9iWRMyWCXxV1y8lv6C58ULj2SKkU_-ijD1PF6PS2Bzfp0KgviOVJa2CaxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/22544" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22543">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/22543" target="_blank">📅 17:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22542">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy6yb2X9ce5yWzmgMFYM0QWUJayv_LqYMBGJpdU_pO6o3TBXvikdb9uZlxczGuXY74bNAkk9VUVBT38MW6eDfnMuFdllPxgFEzUIvIfZe0sQWiemrAgiz-SV_v_Q4OY14Ak1th2H3CyXKlN22l9_MGMmpi5CToOQr7mYR5hltxIHQGM-of1ePkAPabcFjH7JduNjEV0uu77zpISuXM37J8jKhElwNM8aKA_yaXHHts98eO-mQt7mGOfF2iAA0-vG2jXHG-p26R-LnIW2sr7-p5iEEdkHQrLembmxORu13QUtM95iHlUuhs7ViJb5awsqgCZIvXwuWn3FsI95RMWrGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/22542" target="_blank">📅 17:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22541">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22541" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22540">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/22540" target="_blank">📅 16:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22539">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22539" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22538">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
برترین گل‌های فصل سوبوسلای در لیورپول؛ دومینیک سوبوسلای مجاری از باشگاه میلان نیز آفر رسمی دریافت کرده و احتمال این انتقال بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22538" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22537">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOuOzLee1NBfy67A1oMawMQRh3iW8Dx7uuUU8LqkB_IA8QOHx9woJuhkKp6wz8-bROaYgPzt9pNEtLlRxSCD3tEzv5sFEJ_t66MMAHDEobMI_x9OspQNOLd29TIkkVzDhudH6GfYmuMx-zZAmDt-oskDlAkiH4_ctBk-zb7tF2K0NUpjDHm_8hu-CPOPsbwX45q-dKuq1_Jrm30RZqYhRlVeFXtjDt9oFwB4tRFYYH46xNOIN9XP1391RHbZrCMPf0inu5wyCQoi_7mRCxHesvIYKf_FAh1IkUDWh8y_UqZ1dO91MxwvcY91RVApK3aTS6ogCgN0se8nk-_XMVquKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یه احتمال فوق‌العاده جذاب؛ اگه پرتغال و آرژانتین در گروه‌ های خود بعنوان صدرنشین صعود کنند و درمراحل حذف بالا بیان در یک چهارم نهایی بهم میخورند و یک جنگ تمام عیار بین یاران کریس رونالدو - لیونل مسی خواهیم‌دید. تقابلی تاریخی که شاید اخرین تقابل این دو…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/22537" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22536">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObWD0I5mcTanFCJ-jaYDX6gD5ig7mv9GKZFzpZa8IIBeDhPV9_VYG9zTLXTzXG4SqP9BCACrk_6ZOCFdkFqYW9pey4TULioW92Zt52_4IgnJAMGACLiZamNE_BeORgJARHmtC6VlJTAxqvAxSvWCz2gT_ORnaMn_GcK46YDaZhOMifIqSykJ_mW-sSgybFl9U6_yR1iBBfJ3HtWiZqKLhAVqbi_Ok9T3JpM9LuXY703DfMXCgalWH2NuXugy6N8oZVRUUqx5t6Jh2jY3k3yewj2FrbMof10ddqONIjMFufRyeohRN8hJzcSvKBrpFaM8hz4QyXTDKncWn2Whr6o2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/22536" target="_blank">📅 15:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22535">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYcdx_kxaEKeDpaH7q_Zcp1csFxWNq48Rqq1cZfOUSjeUyp_7blrD0GP387ORH5KUTRYicbvN4rnJEDX27MXxBLxdv2337b5x__U06vEYqpHAZeJdzpm_avycgkIDaj5gAqwP8MiBk7RmtHLOHwB0K30k1I6aB10qodnn-fNKEdpIJYZAgzMH__JxPeMr4NRnV085U7nJqQ-IgnMvFjZnPYuXZ3BTLF_YvdEVlUM5FvgqxrNst3HFxjI4drlsneNtClvFcmq5MX7ZSk44zxoA7n4dJ5OPmvRMDXx6GYpLOysuUOeCDIoIeHc2UAjFeotqxh_kIxlLS-Td_64JjdHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکیپ فرانسه: باشگاه رئال مادرید مذاکرات اولیه‌خود را بانماینده مایکل اولیسه وینگر راست فرانسوی بایرن مونیخ آغاز کرده. سران رئال میخوان اولیسه رو در این تابستون جذب کنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/22535" target="_blank">📅 14:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22534">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDi2flK1XL1MM7KsI9U3xss0RLuqgv-eJU5ARfUCmQcKE6nfA-hpjjxXy0B17lZXBIedkUSVtvt2nQDX1m9WBhir9CFaizKfadcm9CrlVZE4FPCDirbowMEDs9vm3AzBRzdho8kLYMAwgdFUHbOsIza8ZrNxIDxoiw4tn-ou3Czir4g7zmIDRsIfQnmVrFkloGrekrbLrQSgov8Q-7-3w89A1GWnd_msBFnZTOyf7NmjCz0bbi9D6IfRGjPusjP-gAqHklrw33x904-F2Nl_9qxUL-_fszZsuJeuxkqHbR-ZHa2yNM1eGVGkYa5Y9StjF71e9Yx3iDctl1bixjTQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22534" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22533">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇫🇷
عاشقانه‌های‌بازیکنان‌باشگاه پاری‌سن‌ژرمن با زن و بچه هاشون بعد فینال شب گذشته و قهرمانی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22533" target="_blank">📅 13:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22532">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpaAFIjeWZ9C4_sepgoHdkChTBrCrvpY1sqtv42eIRRKlrPQQwEfZYzEn6TkHpOI_xfjzBq-Ewbyv9fXdBNEWeqR1ZV-uqPRBp6DQzbwMDer3JWW8HUrop5GJoXamsnQXGW0UWEBJL9MvtArH8AkCHr0gu4ZksiUxyERZQjPVNv4Sauw1yocWBstkXNf7wyx-OHFSUrvvs6E1CsmgJfnZ8A4JfvB4MjqxfTV0zyRNUGn-5gDOemQegc3sdCnkRXbT-La3Gxwte7AwPwQIc9AQRJAMttP9JZGh2ne6vjPTo21qxcgHrHAycSm0bqqoOvqGpHCpiY4k9yFtAtia4-l-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرنوشت عجیب امباپه در UCL: سه فصل آفر رئال مادرید رو رد کرد همون سه فصل رئال قهرمان چمپیونزلیگ شد. بعدش این دو فصله که اومده رئال مادرید که PSG تیمش سابق داره پیاپی قهرمان این رقابت‌ها میشه. دمبله هم تو قهرمانی دبل کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22532" target="_blank">📅 13:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22531">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">▶️
تعدادی از آیکونیک‌ترین و فوق‌العاده‌ترین گل‌های والی که قبلش هم توپ رد با سینه کنترل کردن.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22531" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22530">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPm6i7XpbuLruXA9KLV6XcDJXgvAwzzIFNkPgHBQF08fYni6aT3fKF2T6JXBNEI7ghE1rFRcR1i4xkKf2gQ9UoZ1bCLL4kqG9PqdjVdWrrRJ6cgNTIn_hvoTyUT9tRwIA2ZW63oWtR8Lv4I5s1c10xxMLpOGp158zNxlyX5StVkSD1kY57t_xA-0en4gWqWeBY9P9A5e5k-dtcK1jBwxBtJfMbKnVoggnWmBG0w0m2lryylajVv-cPgWfFV7pooF5irSYDYDFqMdU-_DenZHnzNGSWOeGcBqwYeZU38uZxF7n1QQPKH1ZbQfPa21doJ9N4OBER2cj7IbxFySzZYIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇵🇹
#نقل‌وانتقالات|رافائل لیائو به شکل رسمی اعلام‌کرد که‌دراین‌تابستون‌رسما از میلان جدا خواهد شد. مقصد بعدی ستاره تیم ملی پرتغالی یکی از تیم های لیگ برتر انگلیسه. منچستریونایتد اولویت اوله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22530" target="_blank">📅 13:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22529">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt4fS0aNTu4n9t1FaBcZnhHDzUi9t6wt1mXIxQzbjZIqukN0jN7tGyXE8ZzFfVNdc3DMkRekdQaZz4RQ44Du2K6Vqm2xeY6QcI5xh9-oUNY6EBLgJ699IZY44QS5Okk6sZnVd3qUL44TNE43r2aIkqlzugXYtd9ZysI3Rc-DCvKxjK7JN9kezxoxOKFg3AaKqtn-e5tQwbKUbiu936nnBLKQ9zG_V9A0nW_CNuiX0HAk_QdftA31JA4px_L-hSLB96gP3xAeqL_exC6lCbjBm0Zcg3Fv-tBZdtd6RegPR6S8xIlQDOaQ8x_kmwXnni-OlQFyH3xWCTlvaDfuG3TeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22529" target="_blank">📅 12:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22528">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaXKoPz53ZbF4WlmVF9O9Fnt23b6JBA-q5BUAm9Rdw0B2DY0MUrapH2UWbBqFJaCZmODwXWNbt8pLHagnBbXr8F9iQzshIEbyxX3bFlq2xt51URNyKETeFbjLOVqbp4arys1WLOrHzBvijVEOgwH1fRky-SFAkVVe7p9QzcxRUgVYG5QIwrZz_e3ifmWVR5HQ7MTj4fQKBy_vBXzuOEFNaWwidQ74fsjeXZ_bmYns8HH0SfCvRQPvPDhK6Ei511FchIE81QHZ2uq9lY8tYeWNOHX17Pcc9-1o8Z4XgQwP0JcR40SCfUpw4UKz57bpTPKfNlKY-H9lKnxbxWzU_J1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخرین‌اخبار منتشر شده؛ باشگاه بارسا طی ساعات آینده پیشنهاد برگ ریزون 135 میلیون یورو برای جذب خولیان آلوارز به اتلتیکو ارائه خواهد کرد و این بار این باشگاه با این آفر موافقت خواهد کرد و این انتقال رسما انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/22528" target="_blank">📅 12:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22527">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22527" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22526">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twXSBUkLwHEerxnqFilwM3ItsZEEu1PE5GgrOl-4FAU8SeAaxbfL2so2RdHHUYGsGy5zMeSlra9vQOGOoVx-g8UpqoRcaSQ1LQMIY2MVb-b3SmHs0Ysbxrsrh9-MMc6aJf-iYf2Y7wa_ihlq05osTi9c5ry3iurjf_a1jLqFBF6l08lB72J_GBXIGmSq-WoBh3TQBWaF-wzyZng7bXmNjmxmmkcRxIwZXwLXtr9TyWK0r-iszb9P2Dhd6w9o5OGazpGup-EhKsrnU16pbXSAeud7O-mD8XTL13hwKEdVv--rzUoNADcliRSO0MVlgyJ0OzG5niq63M44ddalU76a7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/22526" target="_blank">📅 12:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22525" target="_blank">📅 11:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22524" target="_blank">📅 11:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlR-izVaYPfLOz03BZFNOMdGXgQMVYM2MlcIpkM2wjSWT6NHtqBqd6ioLZaAjy7B7h5TEPC18QUKTMiRBP2MHuNbLmt_QxDXQoDIn9elChQ-npEpkLCLWIts_bD7-A03x5vVmKQmX3Dj13UzwMMcJ8ABTEJAfUjb7MTdXsfHVZH2rzbwAfl3oyNj08AHce0vXlZ0opkxrEaks2QWskAb_eZvzNnj0zXzhp5LoIi5MbwQkFGNs0MTXz49Mp6OnwIjnkN7zH-oAZJonBO5-GrVpY9yCcbp6qhUHAqABIU6XbxJTCB_F-RDwDAY91izJ19_HgtU59bd4e6c_1ZgVydeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ مدیر برنامه های الهیار صیادمنش مهاجم24ساله سابق تیم فنرباغچه و هال‌سیتی درگفتگویی‌کوتاه بارسانه پرشیانا اعلام کرد اولویت این بازیکن برای فصل آینده حضور در فوتبال اروپاست اما اگر تصمیم‌به‌بازگشت به لیگ برتر داشته باشد اولویت او باشگاه…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22523" target="_blank">📅 10:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22522" target="_blank">📅 10:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22521" target="_blank">📅 10:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b417aa36e.mp4?token=qorvY22czpWThaLJuvmllWxFK9h-5NGwmTkJkpurThh0CPd-7FK95q3Ba7cCGUWNRTrQweu1bwRW4U42uLyKe869kGqGuVf3pJgGUdsosrYZY6op5Rq2UXbnuSXx6z7FGtNQnKnSV2rRpmaLC5mO-dOpL5EJsJvmOKQyWsmdYD-3ylJ0PQMrm9dWisZ_XXqXmRruTuzT_3fpS3QNIa1IkMXs6yEtRYQfUyoA_ESSS2ySB-ZHfImOE2TD9bEB_BYjcMoBHDIEWQ92P1P7HIGHVj8bjTT69QQnDCvVftOCFwZVXiTcsUZdvE5zd5tHKklohBbmnyHSR4xQJwLuk7uzXE3wEePplCz9GbRdmiKTXXG2t3h-zFVwF6dnXxuV-ZJg47o4TglgUUT2xsAVXmpWta8f0Zyb_9LxP-H8IysRvt4k-dOr5O9HgGuKDW_pns7YSay5jHPofb6X0fTZ7ktAZMhmz6XMeqGTo1EycB3epVgfSMaOEwvZw4TuM1HQ-usO7hHLzzm4M3fmK8UHYTIIyjA80zp-o3PSMkzntGDpcQ9-kBtXck9a0bWrmIYZoRz7Z3pKQeugvbqGS6Og2CaUdYNMo704rfrtiuDF0OGQYJc9LXq_hxGrswkfG_lw2wO2AcAwpEqg6LCrS9WYSxuW2WLmqTfDTF-EKp3JGgoLIro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کدبیس سه‌شبکه‌جذاب ماهواره‌ یاهست که بعد بالااومدن نیاز به‌واردکردن‌کدبیس دارند. اولش دکمه F1 میزنید بعدپشت‌بندش‌سه تا 3 بعدش یه صفحه میاد که باید کدبیس رو وارد کنی:  کدبیس شبکه جام جهانی HD:  BISS:2585AB552585CD77  کدبیس شبکه ورزش تاجیک HD: BISS:03A01BBE20C16D4E…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22520" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22519" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22518" target="_blank">📅 10:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSr3i4a88R3odeglq7J6gaDvHX64MeK8nmNhbmXZY-nUI-OaVCNM84sHK4rnPgnex8uC10kNI30i89T3ehQbOTvA1jYEgq0C1DPjLoPE92ZUn1kmwqc1v-9Za8asDSlQk9GUactM-PosXd2aIKQVpTD4a93KnWmFiI-b4K4JBGjjyUo8yUH5ZJ9lZtycUiBkyrxNz20bZPacgfFXpXucpnqPsA7Zj-txRxx01ip9fD-PrHDtK2zlVdDwtDX-l_7aeQSjZ7IgMOTjfVtncZbAbMoGa36tYxbzMrfLZbxPcQnY_6wnExVAI28E9KQq3EfkKshvHvDcYylCqW8czr9wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22517" target="_blank">📅 09:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRGtYcYX-xgxwUSkQzt0fUhQYexxA14oAYzBzPX4rZ2q665QVLeqfJxAADY0xkvlnHboXagmqMAfan7YjPefXQ9IQhptxq69PC6oyTX2ZFIOQJAlzNW0gkSqWggjy2aiO20KSmK1ehJzru2nT25MsSWkHGoa2WReu_nh51Zvp2sG-QBKvBVYvPfheH5AJx__7S9i25qGGFe9bOGgm5ZG9gXVH27iq-UTUrohH4IVH_RfGmghItZTqy53RIbW5KPI9EHHwpJPnwMhHpII21yDjSZaCVW6uUOkhqwl9XClNuCwjjTZeJVskaEQWLlOJ0JiMA70D4PqMS7_KhrWp55e9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|گاتزتا:سران‌باشگاه منچستر یونایتد مذاکرات‌رسمی‌خود رابرای جذب رافائل لیائو ستاره پرتغالی‌آث‌میلان‌آغاز کرده‌اند و قصد دارند این بازیکن روبعداز جام جهانی 2026 به خدمت بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22516" target="_blank">📅 09:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNMgVMRIBOuuv2oonpJR_rI7ibJgXSvto7ZWH_TO15xYV-KPkC_iSkCOCOOobo1av0tG0Tvl_btwp1_5ok4mrpj_XnUqfYCVLiWYQI3P5twTxTdHxbAtS5YEmL6PbgZ_bL0Vd1b3HZYXGcB2PEKy39KI-VLiGoQnqAJsVyH9OsHXju8no0K3CEdAFzOTJWamhu8K63I6cUhl2WZ0iqQvdV9jq1TBDM-VtiCv5yv4dhLRd_dtj5TTvgJr11G99BUadBDItcH1KYwbi-mZrrGyF3tLo77HJL5xHeHzJCD-glamtCop8nJHeaJxwsRQLv5p-UFCZhR7tII6djM1EQ5Qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا ستاره سابق باشگاه منچسترسیتی؛علاوه‌بر بارسا از اتلتیکومادرید نیز آفر دریافت کرده که اعلام کرده اولویتش عقد قرارداد و پیوستن به‌باشگاه بارسلونا است. این انتقال بزودی و به شکل رسمی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22515" target="_blank">📅 09:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aulmGRz6tDQ-5vyd2wUfdbsGu2GzdAmH2GrleuMJFABplvHyZmdnuDdLEdl8oFGjHBURyZyi_NsyYEOzQu69bfhiQU9TnHGo9zaoTZrwXUyWJ1iOlbT_1OH2V-Nc-nmJmf4JOmJbTKoX08eKfO034ucf6VS3kN0I43wv4wCa6odyfvpUzsj23K0jx7rXzfPRz5YwTvGA_ph1lGmEMAVzEoEMGMx3Lv11I3QUDl3chCECzNc07V05qsw_dKIaX6yCwGvXDmqeeLdgCc3Qn9ESxrF0-x2nVoPitSVFyQnqXac_af3oTnhU-p6YgSjHmwlAKLUT1lwrHHZW5oOOJKdjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
مدیربرنامه‌‌های دراگان اسکوچیچ سرمربی سابق‌تراکتور: به‌باشگاه‌تراکتور قول دادیم که امسال اسکوچیچ راهی تیمی از ایران نشود اما اسکوچیچ از ابتدای فصل آینده با یکی از سه باشگاه سپاهان، پرسپولیس یا استقلال قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22514" target="_blank">📅 00:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3mErtgvfzMSL0PqA49tmjNhD72oHRuMLV1hg08yJ2LZGlbDNL-JCtWCFgjCHRs9a2ZjKz04utYkH0r-f2rmZAVLnNbXC2dsBcFim58mevpAHWGSi1HEDobrcqoH2ZOFC3UmGIgogoKj1PF8vrh85MCRxVH4nPpLI5vUDHBqbE6RUfOtarBlQc4z8vNLOdiN3QrB1ixFP2fR5C8BdnAgRJsYiJpTwZw7qlZ0MiIuCBkajbsoG9_NCDMxSnHrQBd_CHNkGABh98jT8EFyFfUIU0KNCcVFk26AdoGYE7g2alTnHdYEWVzO3g9Fxbyu4-tOCWeRZG7ydzEgnXdk9JlSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌بازی‌های‌مهم‌‌امروز؛
آغاز مسابقات دوستانه ملی پیش از آغاز رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22512" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJm-cTZYycEcTIbfp90RapBSPaFRbD9NGu_ZIanE7yUKgsMRFzgIZfdMBoah4o5xNOtsstOAi-qkK-F8tY3HiYgp1vEqTKg9ru1lov6-_bZEQ0Q7c-E9vkwfd19aXqShBY9VF12ytR__fVHm9FbzMho4aT_5jakeP-H9lh-3PSp2UMXbOlLMqiPdcwOB_2vU5PSfQDw-2wPTcHY8s331qAByZKBX9qyQoz1BgEL2nagwyzaYORzhXstaJAFzoUstPOs8UcY3tB4H9GdCb32w5AQGXN1d4JYjUjVG1hmDVevVvJdqtklr7RC5TJpRhtPnzgpEVjqqa7PLFDRy-UZxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهادیدارمهم‌دیروز؛
دومین قهرمانی پیاپی شاگردان انریکه در UCL با شکست توپچی‌های لندن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22511" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opNzkJm_reRBq03VhD4Z_sftbTtdCdetrSNz7jGhIrW62xi0DlqYDiKO0kqcvZ-hIm5crqzvq5K6VB6M_ytKnLVjOzbP410dV3IpBKj7TzF3NcZEeeyZFZ72aWihq3Yc8tMDV95NQ6-ID-0g9_sre2PLZGoUOt91cMiaKG5ZdVZLqceOXLqdCWnG3tFzkAWFqq3W6bP7JJo50iLboG9K5Wdj_Hv8dJd5HodgaWYuqCHWDzgzKD98uTjfYwNg3wuTKIEtwdKuRDScf99KA2MHeThDSvuGSdZmZwhdafJYu8RbbJ11iqrIqivYw27p5boiZjdly3Ikdyc3e-0Wp4p_rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22510" target="_blank">📅 00:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt1bSjJ8RUaie_NuoeqVKUEQmll713ITtsljaSMaLBpu7QgpDv5DZgnNVLT8SFC3DcxQpD9kGuwd7pjoWNDFLIaZP4ISUQfr5jKAmOHyKlStud7RkFSjy7PpQG8RYz5mnUwED8a9ifB-PTC2uxtwpQS0BRizjjT19TkOnrHlno7HbGy6-_TSwYFZZes_rbTxdM6RBMEt8ak5Aue2yrwIUNNubtvN5nrNg2IsKOuwaIQwy58ev1Bv37gFerHumK5tmrOjG8MmNb14sH5zrj4WzvNjMhXxewE9XzLSvekvH274PwY60GhG0uAtPeFow6vtp9D87pFyvSDD8Eo9Yi7mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های دوران سرمربیگری هانسی فلیک‌ و ژوزه مورینیو سرمربیان فصل‌آینده بارسلونا
🆚
رئال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22509" target="_blank">📅 00:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXCd4xbvjB2xJGzXjwnBLaBn__r1B2fL1ZMYJ-lsB-kN7dZNcJxMGEvF2KeYEDA7i90zPpM9g4Vrg4Tmu4RFa6JPgQztNknBb6SaopPqSKJ1kgJ7sAJ81LKmEomimcpvF1UEwaqD5DNOy1l84_R1TPcCvrNwBI__pM2fs2B20N1mI_4Rn0PaIe1nJsG-YevLy-thNwrMulTQNXig7f11SLepIfKxjZCOeMOUr6b5VBtc9fdtz7QEFP96yXDqHsWZH3L9DWRzKD7c9wOmvlbOqCgJPkqZ_dOX3zvDBhqGORBGKKS41WoYgDU6XjszmBwHJ2n6gn2bdkJ36TI3Ny1pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22508" target="_blank">📅 00:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ-Uhy74D3sfVZ6PzygzaWklcrjW5Z6WxqhWI5QAAmPA0SAg3cOrQNmVPnXshhJRT-IOOV9QNd7C4rkQrVRMRgzf_SWevumYq-gx3ybUaaT2nPy7twJeEWR2eGEQwyVYVBgZIXsdph4gTWTMhzotSIW4195Sjc2aksyl2wPLgU6OBfb6_qGk9egJCgb7GOVRskNsSo6UDPKT-49-6tKyNms-uHEUw2CMPZuEdchysdu_c2JjSBepeSL8r09TyC3aMcuXVhRWGHiIC6WhWdursgynoN4KFvnkGsimw3J9fBlftB71GLqr5nVCmxFOs4A4J_y0OwKzGWwH9KXtcUS59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
تمامی قهرمانان ادوار مختلف رقابت های لیگ قهرمانان اروپا؛ رئالی‌ها همچنان‌بااختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22507" target="_blank">📅 23:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMhH7AKb4YvsTp-gDxFVmjm6d2-7qW934cz032BpOu45fepeQur4bysZF7NwqK5lkvhofHyMenbgMkDdSWI2KyJ1PU7JrDiKcMYsE4B3zlXJqn1DKArQ6Xm-09GLMhhbZtbnTxbxg6E-DMiL-3-8l8Th9XgrSs4UEtogbhcBxESgsA2eMLTXIgEUbDaahj7LpHu94aZ_kjrKKcQYvbUYpBqj175tqX1Dd0bZ9xI5Vc5Brj0l2caM69gU7G6E3TkKybOur9YqwsW68887Je3TY7pVmvtAltYsbWiExbupF_gSZ7fjDnk-Scn-Fy88RPgHjTyUOq-IeN054pV-3vOtdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌ضربات‌پنالتی دیدار حساس امشب دو تیم آرسنال
🆚
پاری‌سن ژرمن در فینال چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22506" target="_blank">📅 23:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d5a3b7a3.mp4?token=ZHdDdsFPzFIJ6uL-Udg5ZdzMwzjcgl-cK2VAgn8ez61gjWAXi3br3eguMHUvA5nuLfTmWt8GJSL5i9Ha-NhOtLTu4LAmxlMPUpSHMPkLGBal1OVw_u563CinAecVRa3S807nnSDncNzgeu9JJAirKMGVrldwKGL2o2pcjToVujxubUXPe6x4x4KAV_GudcsJeq2TBfjRvehTpRlOriN7aeIYCDlikwDQL9PWLLKPJ9AFjQob0MXfJ7a-74aRtOEKvrJ-FjIsta00Ws0aaX4wdvpLky0mbFmUHWTYmGzhXbnhpe666In9LxGui_RbstBsLZcJAcaIJf-knjmLwE1L4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اینم‌نسخه‌اصلی صحبت‌های امشب عادل فردوسی پور برای دوستانی که قصد استوری کردنش رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22505" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=H17sHIaekiYDQYZJYnwyJw0XGhiVEu90eJbDOpVvP16ET5qV42qkz4F8ueAPY38ERVJH20JeQgJvABnmsfHSoRGEPFGhgtMXxJ4S8FgPytezGudnrNAgx-2fwGQFARBm68cCbGcSFp72Y1pBPlC5sqj1OHqmbCQJn4K8SX-143VHMUFmq-vUpr1Id8fJ3c2-KP02xg8qXzdCYYWKv9fpa7n-5gmImPG5TAQmj8uZHKCEar0alp93qciwWHC4IBtakO_FaPKZgmgIP_AF74eEDqvwaIwK6Xr1OQJZNjeZtaa9a4FE7mpT1yP8ejTulnPQ2cLmrAeilSoeObPDGlwgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a1e84d8c.mp4?token=H17sHIaekiYDQYZJYnwyJw0XGhiVEu90eJbDOpVvP16ET5qV42qkz4F8ueAPY38ERVJH20JeQgJvABnmsfHSoRGEPFGhgtMXxJ4S8FgPytezGudnrNAgx-2fwGQFARBm68cCbGcSFp72Y1pBPlC5sqj1OHqmbCQJn4K8SX-143VHMUFmq-vUpr1Id8fJ3c2-KP02xg8qXzdCYYWKv9fpa7n-5gmImPG5TAQmj8uZHKCEar0alp93qciwWHC4IBtakO_FaPKZgmgIP_AF74eEDqvwaIwK6Xr1OQJZNjeZtaa9a4FE7mpT1yP8ejTulnPQ2cLmrAeilSoeObPDGlwgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
صحبت‌‌های فوق العاده ارزشمند و گران‌ بهای عادل خان فردوسی‌پور درشروع‌مسابقه امشب فینال چمپیونزلیگ و تسلیت به خانواده‌های داغدار دی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22504" target="_blank">📅 23:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVqUl8-pm1K0ZmfQEVRFM9HTiAwRj-K1kiUMIZWF7Prw7ketzkEJXWdXvXN-k-rnEwFnPZxdSqVSNpmoNZ9xGxm6GhTEtcaCsdR-2H670xMoX5QzLn7C9Xt50zBMGpKQ9CToCF-2ugmvNsSLN9k1XcEMKpSw-j753ue8456GBpKkJWplT2O1hE7gr14xHst8WjYR_IZnA9O56WsSRuu_OXfVP34pVer3SPnhvNPp1Q0PkL6wPk48FKZ7IyOxasXH_5OA0DMNRulT3yFsOEgdq4YmlyVZZc610BfFOhMtPoYY-illU_AkF8OiqDLKhR9QpENuRdP7Mw4f_KzPWQ0Xsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22503" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22502" target="_blank">📅 22:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50097d1448.mp4?token=lGNM6E1X3NJLmwAOAcyC6TU-uuDcfX7FvX6UZjwJEd0VzqDsr3N56aBzkuruZZg7yND7L-ZEkTaYtlCFYC8riLXPXbLJfMKj-mKcnTIV6HFeOLZk_W_9RYi5645tM3ZMN6iPZj-FDXMjMAUapvvXJkHQVZD76PfH-MK305rjSCVnC9gFSIA3zqzsj528RMjw7JF1F3AKITTkxTspQByq3wpTxMAU6RkE7cyLwb8vJLHgjuOjly_4mxX5w8EyLcGWZj7Kb_tstH0NmQ1V9vJ65IJiGiw2f5O4xNFvOreiwzSyZTiaMyinzzrSZhc0AKlt7-Fnd_FOHee_aYXIWYrtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لحظه حک شدن نام باشگاه پاری‌ سن‌ ژرمن روی جام قهرمانی فصل 26-2025 لیگ قهرمانان اروپا؛ این دومین قهرمانی UCL در تاریخ PSG بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22501" target="_blank">📅 22:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhQeOU9pq0yJXgU9_FJeqx-2ZvbjHb9xeKLSpOHdoPg7n9ymgL0pPbNvfE3CLootEWJ7bXGR6VtGzgKXKNKaGmvWEzSChQZj4Qz6c4smrufkULGHBTkZlobRUvtx81Q3DzxTXXyhzf7ImGRxGTHfCBYP6mu9-IxKk6G7m0x71VxiaCru3fUNi6vOiRe3hd-CfqtuR3TJZFmKqepY_iPtKdQs44HglIBVyaykDF5kGSrFqaETNV6x-tch3OI7WPIwv6Jn51QNnhXDyhL_zO6qJIrT6q7J4wPVdeuYE1VHyG2JBc4dmhdN-CVQjVm_CcZ4ocpgwu0llFyyYM8N6vIoWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار فینال‌لیگ‌قهرمانان‌اروپا مابین تیم‌های پاری‌ سن‌ ژرمن و آرسنال پس از تساوی یک-یک در اوقات قانونی و اضافه، به ضربات پنالتی کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22500" target="_blank">📅 22:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgqxalB68Es8dsVEO7AvKFtzxoa6wkRtZz0-cJxir3b8RmUlHoFTrNtm4dnlBCyeiYCGEE6uoPrtDWx9Co2QlkrpV3oJ8Xg6PNPHGW47vB5pJeNDgZ4pZzoXz4UuvVt3OBBVYAK9Lw10T3lSZlFlJ2vrYsnJArP34UFzyTPPLSmdT3JS5GkarJHJhpQIGKKtSzPEmLtCDajWzjKlDPE31b6k5p1WfEtYNQYwasXGQyNV94USd8DxjezumxZKJ5xFxdgvg6hxCpFgV2KIyZ3KFr4r9YE_aK3urSE2pO1cJ86L_04v8ZpP3SB3ZPu9_Dw8XtOPlcMT_RlEMICzKrEBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات|سران باشگاه منچستریونایتد به درخواست مایکل کریک سرمربی جوان خود با ارائه پیشنهادی 100 میلیون یورویی بدنبال جذب فرمین لوپز ستاره اسپانیایی باشگاه بارسلوناست.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22497" target="_blank">📅 22:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKuZT08MogQ5Jo_e57mTqNirLQXOlFmut-3QbrH-LC-tYrVUi2IpLyrjSxEIFfLe1xqp7rlM2vZMOYo1enOuZ722qf-7nfPnrK02mKKadJZwXgy3VlLftVv2yDH5ZQ4sqtAe5cAy-mh9nSawDx5y8noZnSsijeaxMuiuEkSgcrnHmbC9Gd8YKYpKPtqADEUJvKNzCNCXdmy1J3wPWR0i08rThDv3sTf_mKnkNF6T3sblWZokvSySLJK3CmzYcXflMRt96fa6UjLCj64kh4vjpBVK5culkmcyGVWX0fGRo4vPA6G3FhQaY6toaf6dva9hiGGeiXYCtf_oLW7jUiX4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22496" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O96aoxv3S9af4fkRxQ0boK1gm1pA-t9gCTL18oiVnB22MbMYvPaYW8ZpuLge80kvsmNfWo1NG5D6fA2xWkSGKrtDEsrfvtNo_fzCbZrCopjRKZUMF4P5PivPEbv8RSDqtEUzZifjLsCD7T7k8zUi6KgZRTuIq20wp4mU0kP46dE2fef4WPF67pbW0P8Sibo9vElgrywAJTC_fRqiqUJz2j6ew5NtqBPWpuyslmuUgxXL5P0-s5PRkJvUCS0B_ameA011_UwBKcDFnP0k5XVkROEReD8hf3hBmjPabkyG-mVq3okO4jJTd30_dA7xumsGIEPIJGt0XaiXaPmvfu-TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تنها 45 دقیقه تا قهرمانی تاریخی آرسنال میکل آرتتا درلیگ‌قهرمانان‌اروپا و کسب دومین جام ارزش مند و شیرین فصل؛ جای عارف خیلی خالیه.
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22495" target="_blank">📅 21:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEx-2LLmFFd_btN2nkiwPEX375rOZy6yb-pAiuHVV1Bopm2X4nLrhwW-Z2I7QqJNcQlUOHI1qxt_osQ0GXF9fIgAD7zRaP-bqSaqHFQWKRUl0EHteEgh8RzK0nIF95Onlays6PrnXG2GRPzmWAPLUm8LhIEZAdZ0p-mIS61tF73glc_FA2rqNcHieE9V2I1wZiXGOW18sm7cvuFArEINNxM1yu_4ezNfYQo3XKs-vz-uFybfQdrqfVc8CDbgN9GV0HGlmIUfuR6rHXSNLZpGUZUYov2fULj_fHlvCjnsZprxabdzTXDPimbNiPNlWIE-W_-ZkbEpJCxcSTvZ1beb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس پیشنهاد مالی بسیار بالایی رو بمدت‌سه‌فصل به آریا یوسفی داده و احتمال قبول‌کردن‌این‌آفر فوق العاده از سوی این بازیکن ملی‌پوش‌بسیارزیاد است. سالانه 80 میلیارد تومان پایه دستمزد + 20 میلیارد تومان آپشن.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22494" target="_blank">📅 20:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYeq9LV6gEt_rNP8D93kora1aSvIgsPp6EfeyL32TQ7zNb1pzMQXGkVUHseOzoFKZBJrGxaBCko35tzBvKnJH9DVZA60ZViS0e3pPAxakh1COzs9hskCka_tYHn99st1GMCVR3YfONgIE-SSMWbdSgSGVf2_KQvSntNzDT2ZYwexY4FKBN_QZHHVA44i84Yc8PO_FLL2wAQ-LQlqNUm1pXVk1vEzJoJ3pKBPLWN8pc4OPXeIHDsWNBLNZX_StT0h7nMmDPtgA-ICpENGH9LwbhtKKyEpgCVjS5Y1OmZAYDVXlgkHwUK3G1f7mhKsr8BX-MnKggR3W9lTK81TX2mypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
علاوه بر دریک؛ این‌مدل‌انگلیسی طرفدار آرسنال اعلام کرد روی قهرمانی‌این‌تیم درلیگ قهرمانان اروپا دربازی امشب با PSG پنج میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22493" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=PqkzVdUQLOzczJ3OJkEl4x9xnZIOm6hGznyTv7e7qLg7YrJUsdExOPCV9vjlZZG72oTg7U-G-A1V467RaVH1hCSuSTSoubju5pI-uorxgu7l8czc0E7QZP_NYAn7zuBONpsO1iAXZfOaHOA21NpkxFmaC6lVMj3UX1a3xE0_6cJrkGx-0jvQL53Plc80UDclJcA_EVdSSVcGdsthtQSfxrZDiQE-o0VV44AKShWSBqGJCXSi9Gc_0X2kXVivQ9Y0fO8UmXJxbDhChZB4Z0OXb5xI3DMJoBH4_t37pVK6hFoXPGlQjvOPwTlFOLktIeZwcPiVx84SIm14jupr5rrqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a443979ea7.mp4?token=PqkzVdUQLOzczJ3OJkEl4x9xnZIOm6hGznyTv7e7qLg7YrJUsdExOPCV9vjlZZG72oTg7U-G-A1V467RaVH1hCSuSTSoubju5pI-uorxgu7l8czc0E7QZP_NYAn7zuBONpsO1iAXZfOaHOA21NpkxFmaC6lVMj3UX1a3xE0_6cJrkGx-0jvQL53Plc80UDclJcA_EVdSSVcGdsthtQSfxrZDiQE-o0VV44AKShWSBqGJCXSi9Gc_0X2kXVivQ9Y0fO8UmXJxbDhChZB4Z0OXb5xI3DMJoBH4_t37pVK6hFoXPGlQjvOPwTlFOLktIeZwcPiVx84SIm14jupr5rrqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دریک رپر معروف کانادایی یک میلیون دلار روی قهرمانی آرسنال تو چمپیونزلیگ شرط‌بندی کرده.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22492" target="_blank">📅 19:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aF5z5TIACHNEYK3OBnH-ntwQPEEtMDO68S7RW9Iy9Se-osuXBXet5LDQoQ8xdkoW1JxuHC6Cb8f0ixsRnR7QkvU-t_RBIopE0luPLEOTwTBvxIPf2jz3juLYhIRQZ5NUWjdsypEpacPhb-sD8B7BCHTCkQ2yC3uEZp1qdgIbVz9r2Iw41kdopoCkepODWyOzeLp8YqligPcwN5fxX63vUUFXpFfKF3vJ6hQibhDCTmSP6Zs6wfGJoVttTTjitX8QRtJtPtatdGM0Iv-re2OGXaFSaIOcaZsP_X8Z6ZYRUFvFcUqtYYOAfEBGI9kBJeysPeeCXVdKAGuz8rZonWsqag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22491" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2qMaNCNnmD84eCODEZXhF2EK9G8nIOh5wdrxVwZXYWr_A4VYxvBMPewsJJIDP2SY4Scuy88MAmZ8cX0IjaqTANKnJmzpgWaHufv5V8boGh-0KV-M2q-od9z94XSYL7-cVbbvkh-xoqQOwGkShgc-SfpxvMY_Ta0kPwlkuvmnkbGw9JoYZNYArzxrNpILSEe5OUANYBKlS5CeA8pGtzCELvJKpSfpDRHKcUIZhLv4ypi6Csx2V2Vx7Bf2uvRi5huERKl3fQ5-LuTca_xOy0LjLfA3nmdTLzjM8Wl-x_O_TvFGnFtc3gS4YwAjHytrd05XgS2tj0DH_XPP1mD1Zve_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22490" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSseGim6TJb0mxVKoYV-_oF61hJ4-bwX001vLwIl23n7H7_Lg7ZnyfQ3K_YeE3d5abLrT3mL2L3i3V8j9r8kA5NZexvt_6_ZWAzjNQ-1WkI9JhdqrPsNtoE-I_etyGD1_dXFb5giNwNtfxsMvTIQW3t2iMc1lKRLO8BEF3sXUecVCtqA8a9VGuQbFV18rNRaVWsiL-G6KZVdXzMAzIa5rwZUgit4Wa_-7FvKp0sOYruOh2N81UXbDVCHouQ2jwJdpzBlADPDFHf8WARAJxGR_MceULYRqvhnBrWFbyy96Jrty6F2yZ-E9RfcXQSL9u059gMIZ5fRTPwOA-AR_E6H_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای گذشته نیز خبر دادیم؛ آریا یوسفی و محمدامین حزباوی دوستاره جوان تیم سپاهان مدنظر اوسمار ویرا برزیلی قرار گرفته است. آریا یوسفی علاوه بر باشگاه پرسپولیس از یک باشگاه اماراتی اماراتی نیز آفر رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22488" target="_blank">📅 18:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sb32r2bvxONTXDpMnPl8dF8sqFXmVSCHn6BaVNMJ_hDKrTfCaTzUsGCU0Q5rkxiBVPC58ai9k24joLM7fNn4tZ6579TZgpDaEaTjWPeoJN8aXFn8W4e-9XR7hC7A-C6lh7bW9Iymlhj-OKt0JYHxE-JxwTPGufMiu6mEzeoWLz3_t2KVcCbDkeL8Y3PDpWxgT6wBIRt_CPdN_vP1ltYAwLT0Ov9b-x142qSyA95Ma4QQT6hjMRZqjraaKWJpBBekS7jZW9ur-V1B-r6OPfXUJE1J_BGVJifrchPyFHCmbgKfk16-tSwTPwPKTZ56gZ1eoWgUW2VWe3hrUpDgd0Qihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22485" target="_blank">📅 17:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB7RmxnVxQ_nI1DHWQGinfk7Com9Zqy6Ub7CDtgTVbrBWjY8E_CO7tSD_g5V5wlizrQTuwUkzMiSAHFHQetdliqpraIVao4vjtEO2KPIsvCdmnJKySbmtIN2ID2Oz1_uTjXmZEBL0rdWysHbXyJqno-P5NV77vTvxUadJ3XpIpvLB-2C1nzd5ARxi9OGeLIDuObGMfB_vn7UMoty7zRq8OA-y1rJQXCvfsJldKLqnblR7C-BtdQtldGnVj6iP5dTv6DYQYtl3uHUBvBxmom1UhQZoFkETXmsx7xD3ZaTeABZR3te3C8J1tp_QAgjsVHgeANEausjJ8DikSvt1pUapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22483" target="_blank">📅 17:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU3I4Rr4kRZgvfMGIOeBuORCUp6095tMHHJoIiqHn8rt404FWkfw8Jq_pvGAWWqqw1xOrLBXms3M2EHB35wVZIRcoGUFPsQ-POb7EcuQfFPuorSHFzw_FAstcnAMxyyGRWFTj8EA3uFqi_QUeq8g4pM9F-U3vRI9iAcmRag_n0wdpWJA3yLuwypdQ30EPzVnG5fdab-9THMzU-A6zL_BeOj3QsCn_H_l3Zqebm05G8LWjGXWFRHY7hAaeCr3l6nPNmvwDEN516xgmztLi-19U1SizR2fNveoiwl6aL1oT_T6Vv_w_hyNsu5HrKxvoJGPvbpcLY_SWPqgW6rtPpcMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22482" target="_blank">📅 17:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmmBiRVpM3FB19W3Yi2AGxKCLp2cqjBVgqxayDDSYBe7w21MrAKScy4Crqt2j4njbA3TDkvBxzggouDaN5eepYbU_OFb2qHRndZDYG_W3lM2BTaR6ZrRJ4ihuP5Q0cKHAW4XFRqn_TFHRQl9raJPqcVHjo5vRZSoR_m1s_zl1Ua4HmwTK1NL6DZqizzAbkIPMI6fuG4CbLbWFyTAKu9BMkg1yZPHGK-TCdS1r2xU37go4Hbdsyu5JIx5Sr_Ynh3quAJInaFAcsCWoMiUhfbt1EzaA4uqIRN6onb5zT5U2YgOxCiZCB2jX2YYsXYZZfLH6jOm7MCYonInxyAUQsb-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22480" target="_blank">📅 17:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=KpnvidahzcWHD1A6xBtkYIZ4x-j2eZ6wi4sraHflEuJmtyHhl7O96p2xc83e7EvcuyNNIW082x72_GK8tU7hXwSV_L898ySIJPOKykIXdu45q7OMEHVRWeik8cutDrBEm7ww0YcBCY88l5n1BAezMSbtc5nYl6wxpddGqFGSa6AlQMYiB9pOco0wsxwdHDbDv8zXOR9bKsGrX3cD4wp-MLIV1abOvEdwiuAoPYU1bkAeqJ3KFBPSuWKLGaDv1AKfgI0NWPSXW_SQ-OQEySJCqcq_mr2qag0yFOp6jE0AU_8tRhyU0-7eUMc9oTXBjxCZYOUEqhJQJWGg57rBwiyBRzM3Erpefoz5lwfjXU3Qmepa-dnwtnAySCFBlAlMfhAgFmIvFnBtiTk7xnKNlrXBqoj_gMRd0N4jAZjiBOXnM2FRtYwRqaECgjTv7PJOPDhfWIQY8yfnGlUFUEtSxf7nFzO5DztU4UQr7OhhlG8X39x-c000p9fZOo-JNjgar1dDYrNdYcsEjBHeVv8m-WrdN_nuEejW-aAJwYQhuRO3cr0GPsN8gLOcWQSqBHkfADFT_5p04tBejDF8E5RLICuHE3udp6dvhdBrXMKheRIzOOQ4fQ7KuULXNtryGovHlVmCp7wW1TzESZkneBM2azxqgqpJNrgcw2mbkt7hxI9fK5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf37364cd.mp4?token=KpnvidahzcWHD1A6xBtkYIZ4x-j2eZ6wi4sraHflEuJmtyHhl7O96p2xc83e7EvcuyNNIW082x72_GK8tU7hXwSV_L898ySIJPOKykIXdu45q7OMEHVRWeik8cutDrBEm7ww0YcBCY88l5n1BAezMSbtc5nYl6wxpddGqFGSa6AlQMYiB9pOco0wsxwdHDbDv8zXOR9bKsGrX3cD4wp-MLIV1abOvEdwiuAoPYU1bkAeqJ3KFBPSuWKLGaDv1AKfgI0NWPSXW_SQ-OQEySJCqcq_mr2qag0yFOp6jE0AU_8tRhyU0-7eUMc9oTXBjxCZYOUEqhJQJWGg57rBwiyBRzM3Erpefoz5lwfjXU3Qmepa-dnwtnAySCFBlAlMfhAgFmIvFnBtiTk7xnKNlrXBqoj_gMRd0N4jAZjiBOXnM2FRtYwRqaECgjTv7PJOPDhfWIQY8yfnGlUFUEtSxf7nFzO5DztU4UQr7OhhlG8X39x-c000p9fZOo-JNjgar1dDYrNdYcsEjBHeVv8m-WrdN_nuEejW-aAJwYQhuRO3cr0GPsN8gLOcWQSqBHkfADFT_5p04tBejDF8E5RLICuHE3udp6dvhdBrXMKheRIzOOQ4fQ7KuULXNtryGovHlVmCp7wW1TzESZkneBM2azxqgqpJNrgcw2mbkt7hxI9fK5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این میم دیکتاتور داره هر روز سمی تر و سمی تر میشه؛ تاثیر کیلیان امباپه روی هم تیمی‌هاش
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22479" target="_blank">📅 16:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXUz0QlKQDEIAHJMDp6THQllwn43klh6Ivem1QNRxm5KXv3x69NzX-7OUemWrBchThpXj5rH2HiqaqbysK6Nw-fwBzGm6UjDNJmF7jpNqmDzdXNV-EHcYxyYIEkUUzwYEE9FiqLmkZMgT6HtfrZzhK1_ND-d13Mxtg44-xLGHyKJmRIXKNuLobOOvSPCC72uQCry_qyGPZMow995BqLI8NXXEZM0mLdEfaVWYvHDCd0p3SUoCyu-T_CeBXzNOe4I4A8hGSz6tv27OYLJ5jaYZZ4WCtJeE6ssGhKcPgA-GgoQWpaimx1MldD-ZTW77qdeEdNLByeXG2q94YYxg9Abnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYpL99Q8iMJsQSuZ3XxsyAxseeDEuiLG7y-rJ04qubB4HSpJlg-0zGD5R4r0x9FFp9hPlZ2Irl18DWKUQ2ZejFexcyHGAleKh4wKRhjWaO3hODVN-96Bz_BSzHEYY1bGDopk7xJN_q6_yqPQeQASPrVNQQtuma5vyLs1Xok5ifqIU05awJ9K5w9VnyRPgFXYMf-9PEMdMIgevBho-q-VwX8ZSsV_VGTz8AyeuNenccEvYyjDxkXHHfmzk7XgVSyq8tOxcsd_jJVZjpKib-RgyZWu0u4ZYx4NNBm2by8GJGGSi1v4_alEu5Mf8Jtfvfar_ChZRaZZYmdyMEOTSWTMmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsnFaurgnny4I3X8R0YX_Ix2VlY7nLGEp2t1aYNlxSNQZB6NQ-NYUaPEtJNW1lEtd8EEYSyTOvxAuUVk6f0gQjhLkdL6OUcQg5y9Dsdd7yHADqd7dzwFYz_ue6mhckUylEBdhTBhBIipcs0WImvWR-okFIw0I0GUhx5cAR1NcT0rW0E3PC8LfLaF4S5IIYDJOYO8jozjcPFT6k9XvVvEk7Z5zDJMApeVgpFNEDMwU2SR8EgZ-Ca6RqCKApctvijhV4769I0TSvrPEUSOgxuhLndz8s03X97ueeTB6fPyBJ7Y5U3ODoiNuHnSsSCPDFn0ROwT4dB2VcFzRLUpVevM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22476" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=pPA-dscu6ndnmcIifXmvIYFU9zO_b3jmBVz6c0nGi-g2_W6etbfn_QSZEjHtRLRLXD4ujCGoKt1gD_ubqzh4nMs9TL0CLzW9tWSXG8TMzOoPxZXZV4YEokbbmfsC4AXA-vicpFIuqJXEU4CPo2r6yDhy9QxFk3DDWdZeqoDNen-2iSgWmiLdfV_r9b_vfExogjVrIjhqit1Ylt2x4tHUGP_JAWc2AE_xb3treOrJZbV5E0_7g5Gyvlk7TwIn80ajo0KArGo-sYLY0bzeE8vX1Z8XS8BpwnfoAQ64Z0pXmGwKdNOyNY845DpX8_hyNfZPEUetuAbfL4ddl6D5kgImcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d18fefc27.mp4?token=pPA-dscu6ndnmcIifXmvIYFU9zO_b3jmBVz6c0nGi-g2_W6etbfn_QSZEjHtRLRLXD4ujCGoKt1gD_ubqzh4nMs9TL0CLzW9tWSXG8TMzOoPxZXZV4YEokbbmfsC4AXA-vicpFIuqJXEU4CPo2r6yDhy9QxFk3DDWdZeqoDNen-2iSgWmiLdfV_r9b_vfExogjVrIjhqit1Ylt2x4tHUGP_JAWc2AE_xb3treOrJZbV5E0_7g5Gyvlk7TwIn80ajo0KArGo-sYLY0bzeE8vX1Z8XS8BpwnfoAQ64Z0pXmGwKdNOyNY845DpX8_hyNfZPEUetuAbfL4ddl6D5kgImcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مورینیو در اولین بازیش روی نیمکت رئال مادرید وقتی دفاع کردن ترنت الکساندر آرنولد رو میبینه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22475" target="_blank">📅 16:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGOOAqjM4mGMhsuEHTme67qmiqFnQo9um3UQ4EZW2oLiUUskGpH92-JMS63d-0kxq6KXCretZ1DUWhmer4__7rGMtL40xLpGlUakiS2BRlGZRgsb2gG6O5QrqPE_aRaVvHRO4fUkLd4VwTe6w2fUscpqKpS084PAchc6Hz0zh-24JZnamQuAwcXzzADfYpH6FdA4Na5-VlAsz-qqry2WCA5rNS7fwuv0lTlQWu8oySc86RsP9VvlUesZgJ2uQ8NozCUahHI-DyHJPAhlqMAH7LJE4mY5FKqsrdHhYZmSJHWj13PtddmhvwB8OKFn4wG8vIZ4ZaDALP5VLRZiLAkiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|ژابی‌آلونسو سرمربی جدید تیم‌چلسی خواستارجذب آردا گولر شده است هرچند رئال‌مادرید این بازیکن راغیرقابل فروش اعلام کرده مگر اینکه رقمی بسیار نجومی پرداخت شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22474" target="_blank">📅 16:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIYMOYSBW9_AxkPpi67Se1alobuoBDNFT3JdHhVl7MG7lXbT9xrd1rS_n7-Doy2JWzyrZGUpyAbbX8KfzcxlN_G0UxQjo2KpAjLZsanYSN5e0Lv-llAopEOfR-p05SCUDEY8UqBzjfcxQ_4X3B2vSx2lM6gmfCjY7nQCndOxKufFbuV3RgJytinZOb7ApkbprMmopu84t4Z3KKh1w0IBpmREa3qE1nGu05fcTdWpWKzT6KkGJkKTeTfByOL9woibsXw7ILZgykdza4g8zw4bPGb5WXvsTyfMajEwxGH5EDglZ8PDEX9OeaKHD6m59d4yPof8ha-YCY_P_eigVBkNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکردفوق‌العاده‌داوید رایا ستاره آرسنال در این‌فصل لیگ‌قهرمانان‌اروپا؛ رایا درصورت کلین‌شیت در بازی امشب، رکورددار در تاریخ اروپا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22473" target="_blank">📅 15:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZappyPAYxsmCL55W2W_yTKUjCpA1rK9ab0-O283qlfZPp-GBwfdiauEESQERcBaMRLPtSndGUyhh6FIHp91MTguifaQEP3jI25eqjHN39wK1bpHhN62SzdhRmQkvJh7eyObxY79T8xgpz0Iry2Ym4fLXY3JfsIUQlR7ZVo__a0IaBgIEdo5_2AsN5EA57H2VbTr1pdLo5JHPMWyQ6e3lo_ftHRDyZt2F3jefhpKmwXCsLobBVAuBxB8mcZZHjuLtaVG__jFjExRZP-0G2nDfOLg_WkSyq7HwU5FUusTOxyZwQ0QgMxHIDTTRe3u2yRdThcM8dZjPkNNNg6DgR3aWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه بعدی اتلتیکو: هیر وی گو؛ برای پیشنهاد دوم به مشکل برخوردیم، بلیط کنسرت فردا تمام شده، بنابراین پیشنهاد قبلی را با ۶ بلیط برای کنسرت یکشنبه بهبود می‌دهیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22472" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNLtpYp4jBk64OtasOopKCyv7_fhJT-IjjlR6hDHxC7suSoCVRS0XxlD22YmYWQYSah6BJ-GjSVGDqIVKvrD7scQM7v24uIjBJWtLqTHmF0jdGbeRoh-upRHjh0YVls4eeu-af0cA5J70tr4eE6mO3QLR8zh_kD0hvLQB6sy4rR4ReMRZ3c5PsZ9aJ2EqoctxnJU6QY8zS6kU9WJn3NyJ-PTJlQFa5IdKYCcvMpjmNbw83qsq_DNy5giSI-rHNoipzCmERattPfgMcxYcQh829pLwMIXTq04fmtIq6FQhICSHDJufdlElT-Zg0VAauOnJTrXIOLn4ys_aoWawK9A5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22471" target="_blank">📅 15:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzb2ZfOGPNGomN-3ofOL4tAdW-R2uxChLGZoVpbSSZ6Ns7HXoXzhjzN_9DWLzRSaOTJuEHQKZO8flgY78KaBCB46aGjQcCJf2phLkLpRockKCV2GjGDcoJDN9j6zsZp_oVuEPJwkcouX_FbMYqd1dMIckKv-FSflpRwdBYDcV9RGPjUgEY9bE1FjwQb6jktAFAIxF7v-tour9Ki1q0Eor4ryFgoGRYfI4EGo-zj3iYyzvSI2AKuMT7bgurEGwKcwEUDkUP69R97gfhWBAcg6glMJooQCuooUMm0DEfPggYx7TiKryNfEjw4-gMcj-QE2puYhuYLqJ4tv1wLLEAlQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از یک فصل اسفناک؛ آرن اسلات هلندی از هدایت باشگاه لیورپول اخراج شد. اسلات سال اولش فوق العاده بود و قهرمانی لیگ جزیره رو هم از مشت پپ گواردیولا دراورد اما فصل دوم ناکام مطلق بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22470" target="_blank">📅 14:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2YxYqA4KKsb7vSFoqYjVy-wA380dvJHbvqatIneKVavQqnRjoZn8BhVXOgMW_bahcXhAYdpCHKwCj6zV-XCLNvH16XT6hQkqtC3_4e0SLc5qdpFdR75XPNxnpHOLGX1HWRJ_psrPFuyP4C8WgV-WVS4KC3ji2-7ERYKj9enJ1CQD-L9yR5JwBx0zCU7WZ4CGJlaHOhIx5y5FEeU0gKff7romWP0TFed2BXeXTsf_IE1DqJe_-pfgskQ_Xg8BIkv83oBKoPERGQpseJV0Nz9QxKE8soAz8oMxobhIgG7h4EvkG40k5qry6n7TOkXL-0nLepDVYliy1ip0TTW9L8xzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
#فکت
؛ کریم‌ بنزما یکی از بهترین مهاجمان یک دهه‌اخیر درکل دوران فوتبالی‌اش تنها یک دوره درجام‌ جهانی برای فرانسوی‌ها حضور داشته است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22469" target="_blank">📅 14:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP1KRDhL_8VVrwMJXwp0v2f36xnoIuJj7ECEVaChH-cj8JLpaEI5o-LvO4umJi_e4MPvCGnnj75iP5Gj1Qk2xK26u8YaqWu2qb6mVzLZ08M7nQmIZbYs0cMtl-azov3mBwnolW-5rhgi_OLKg_CMy-tP2GdhIVlULd5KdDU-2ji0MdIPIW5eVGkTkrLK6AkvVF6pZFcqXMxCVVao6jnlqw-IGA-p3k0riBcazcI0Z9MFIcqHZd9OVM--5_14Vu27D7JStVzF6mvVkUKktV14ncGh4ANmf-h7-sMpBwCA3lAQnMLyCQxoMhlj0fvyIa4HVkeL-ud7uWEEVO746NrzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
پیش‌بینی ژاوی سرمربی‌سابق بارسا از نتیجه فینال امشب: PSG بانتیجه 3 بر 1 آرسنال رو میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22468" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKGGxgM0Vqy9xj6CTutxKsT0SVaMjNF_EGHGxoAy7k5Wf-r3j2hO8egEIO9u0rOnKI6-ymPrnZ-FPF9O7gLWGjBw2CPWBvNP5NfdZxGHPNb-9Y7zVlZZWsOllqqhYJVjHo6Ku3BcSV_vPtustyg-7AEsV_rmIOOS-EOqd61iIsBOty8NgaZi4JW6ypKCurYBUNFM-iBrKuVyCGgGS_Sh13VlGbWZev_E4c76IcdKdHcNi1tgW1wF6MpSyEiJQEtGYdFyWhq8oCKQaCSFrgquF2IRxawSbU3cWh4_GD-41VjavE3woJ4Um2es1cUIvVf8GXukcuWo7t_uS-e_lwrdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باتوجه‌به‌‌مصدومیت‌های‌پیاپی در فصل قبل؛
احتمال‌اینکه امید عالیشاه درلیست مازاد اوسمار ویرا قرار بگیره و ازجمع سرخپوشان جداشه خیلی زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22467" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLI5EOYvx5r3tWXK19HbtbbdTTXhjR5EvfjAfo_ntAIStaNIY-pDKD9P-5ciatOf1cF0KjMbWiexj_mCCCCplQ2R2cWEPY5tOSkykG9po5usOT9SwM4ghqZ-nJBnVZUU2YzskM5I_GdH2QloBPn6tfITeyEXLRpKgnEuCHYbhxzC-97Xo32nZ26ZKm20Ek80e4WNHPtCEARoKCt8mgiStIkSF84NrGNGgz346rgP1sDduTHKRRNV1_3vftZ06_T-BWzgYcjY_6_wFxSL460nSFloeL04hGHHx7qLcCw00PsTuibmpzl4RpxHQiiJpZE9gRpCIA-K77i3UfeK0mA9kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
ژول‌کونده مدافع میانی تیم بارسا با پلی استیشن یکش رفته اردوی تیم ملی فرانسه برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22466" target="_blank">📅 14:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHmRM4slBNGscWl9mYHxD4MxVss-2H3UCo0UxXB7NHDmJgyGU8xd3HPHfR4gCwAwRRQ6_zkhE14_-WFuZUXqOZRyRYaL_KsBYumM6co7lQ8-X-L6N_a6yfCErWU1pzof2mcENm8rmmOHzXwyFxJ5H_hY6x75S7JVX937AGpYgKyRvhQjGjtRhg69DoFEB4AwGuWqwEHpzn2giAU8HOoc15LCiM19fFHjmzB6wAQ7wHitba2iabYIN3aOmrgde53I7QSn5MQnI2iLATxkrqp8zsFUhcZZAY-lJrueZKZOkXs4DPvGRrnquMGwe-y0wXly7-jjIyyDzO2C__bMAv54Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ علی رغم تلاش علی تاجرنیا برای گرفتن مجوز رسمی فعالیت فرهاد مجیدی در لیگ برتر؛ اسطوره باشگاه استقلال به مدیریت این تیم‌اعلام‌کرده علاقه ای به بازگشت به ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22465" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrFXMTGX4bowt9fzEKfyRkRlQxp7fQ1B1zFRU64_Dw6xxX7ZAltWZBu3vzfd8ov7mcyhwvKSu9awHIhijE_AScwP9P0b4BUv_f_ZT7wnebhRN5ws237yBjaxqLlXlUp80vCgF8WdL4PEVFqkCUKzbY2kOPOx2fI_NxZyxJVPBYxhQABNA0eGgb8PnPXecRLBfdLsDqSW5tW_LeHGLodMNTf6MjipIdMrLlikL4beVsDQumbsBugYvGPpBMPeL7ubd3yuRhAmj60J99rouLDB5QXIbztYmuhRH05S4YGmuaRNYtosslt-Nq94KSNjKL6ufZcn101psHsrcjpeMyde6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ استن کرونکه مالک آرسنال در صورت قهرمانی این تیم تو چمپیونز لیگ قول داده به هر بازیکن آرسنال یه رولز-رویس فانتوم هدیه بده.
💰
این‌جایزه بین 530 تا 580 هزار دلار ارزش داره.
💵
ناصر خلافم قول داده درصورت قهرمانی پاریس به هر بازیکن این تیم یک میلیون پوند…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22464" target="_blank">📅 13:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8PU9Ub1IkyCQPwdQE-i-wcO4LKuR6wivPmSwtEWcZPzEGZpJ0dzPQhuTU07nykJ1LK7eSSOWDTRCOV3BGDMnrwXMOiON5Ml2kJnZ5r-mXzt-sp1zrgWjtWNVVpSqrVEU1WMF-bJMn-bTrlBlEWO0WnDNzZPw2WqcMgpv6Bz_JCNSmTcNkMj7e6ZA2xLM-dGiBUYm8KcDaapPz8BuGImfIIy_bMvX2jYsD2TZ2K6POw6BFuXAzdzJghCb6SngGmq7TfHLIKwOh-1td9dB4y5hrZOFxq4KLrUJc-i9zpOzrFuMSfEoxOeMR3hr3_rGvdrqVttwR24oETP9YYytk2o6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ علی علیپور مهاجم 30 ساله پرسپولیس بزودی با حضور در ساختمان این باشگاه قرار داد خود را به مدت دو فصل تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22463" target="_blank">📅 13:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Inkeh18lTb1qDRIU0Wj-M-UaAPwd_y9Bt9IAOT6i5vuWOdY8iwwqtVgphJ0Tr5YgUZE1zLcTnygBla2sHAVGroABEAdydf0vY5hTF_OD044EKrlcU6UvIeR68vViZqRzXixmECkgW_BN9ty8BvtT7UrCzTcun9za2_6R82saTd0ZqwcBzHw3GitPouc7migGaByAk_7vjaCPsRC4XCN6lelHUz8nNDZYESHkz70Fj4vfCOrgm2eceNcm-dv4qfXc3sSAKnEoTIGFWRm6BvwipWOTnoDT1hl3zh9vLZV5WiNNMIWsvGw2-5hOtaaugPcJowvDvaO8xjqKZ2BirEebpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22462" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKfqNDdHfwHm6xgy6ptfDskr5B_x2YTWtgdnx4UKepbk5R7KEkmf2P-J9PrPXfOcIUb1pfiLQ0Msc6xmfwG4HBFN-gIrS6eZzLke7e91EtnCAaPHwOnFwKjh_cgbsEk2HFn_yW2dr6fvuTzRRYam1pnzRpRyukpVLpVtbI4gmt6Qgf9f6lhRMm9Zy5dcU176N24NQH1l4Q5tbCcsffQOBk8zK4uuy1oe8kgFdY0BYBpJ80aMzTOeDns3cam-nyceCVaNyOkiiq9bq5Caum2oEETla_AyhSl4cJa75ig1mPkkSN64M5fciY5BKYf87-lZA7ItXm1Ee8vyWwRbT8886g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ رسانه‌‌های‌اماراتی: علی‌رغم علاقه شدید فرهادمجیدی‌به‌استقلال و هواداران این باشگاه اما اسطوره آبی‌ها به دلیل حکومت جمهوری اسلامی قید بازگشت‌به‌تیم‌رو زد. مجیدی زمانی به این تیم باز خواهدگشت که دیگراین‌حکومت وجود نداشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22461" target="_blank">📅 12:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atHFtqNyEwnmpFlW3869zMxwywQMOgiIadfD35y7fPQTZNj3wJNzydZS5HL3_badnv-T7R13abfbI78-rnbbf-KIwo5C3LzcdUtYh5eXEOn3KWowHkRiX9MChjTA2ROZX5wt8yeoWo0Soyk9WNb3l3RVB4tGcA4GVazmPjnNrK24KXCpLnKq8cKoIgsDhqsdzunzaRDQFJWacLdz_O1rwptLDliaqcYp10yJdh5UQiX09WBSjGuvLu1fLG3VTAZaENBhv215I5EabCz_lRqxab7sYdjBbt0ZxB6YkqceFD4VnZf8wAP3RvwBLy5K2Qcxh_LL4HTYM5lLPziHgvpPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب کهکشانی و پرستاره بارسلونا هانسی فلیک در فصل‌اینده رقابت‌ها برای‌فتح UCL؛ به این ترکیب به احتمال فراوان برناردو سیلوا و کوکوریا مدافع چپ اسپانیایی باشگاه چلسی رو نیز اضافه کنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22460" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5359012d10.mp4?token=qr_qEXFRQHaeO15LAKzPvSW1_3-gj8V8ULY9R-DFICk7V8YhhPIn0ljtjPSqvhAph4DDiWhjhQnODDEXQj4zhRN9gRDVGkfqUxE7aUFEJH-FnkJDF9ZrgUqRIAH0kjZYVnJDjQuSGkBsX_NxW1XcJ4xQJGjb2u6ZPnVIhEa89tjGnsw2WJRl3Ce41gG7RkPLvCiZ1ed-PWgZXabQ5VxVCpfwkoZphCV5GNLLTg-ltkq089aVx4GF6XgaWttIK7op4_rTyayqHJbc-2P8ek20-3d03_BQTRP4NKoRnoiIAXbJ20Vq2RYKf-UN7LMq4aZRVwBlEw1POf6nXQD9Xiop4ppjFpgmm8GCI7ppalT4TNGtBupnF88huBjp91qjnFDHjWoicPe6Hr1Fpjj16lxpWTZnlPRDh-yLu6g7RLsismgRtwR39iDwcVxeHvzaLlK0IFDNBFHs66jiMBUh3U2jjVJy45XxAs2Zs9Mg1w7lpXS56GMW5cmo93XfWb4WDEgHGFGsnARoPv4bL7Sdx-FNEbM75IcIMvGBtvXbVl587XFE1JleP3_V6iwKuyO9WARptTdkBcHcqLgmjQIuLr2sMfV2Ri-Pb7-nI1rQHYBen948y30c-mXAi8uQwAEu78OQBWD8HcZBn40DW0iyszAG4mEi3zmKYQDuyVuSe7s2k3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5359012d10.mp4?token=qr_qEXFRQHaeO15LAKzPvSW1_3-gj8V8ULY9R-DFICk7V8YhhPIn0ljtjPSqvhAph4DDiWhjhQnODDEXQj4zhRN9gRDVGkfqUxE7aUFEJH-FnkJDF9ZrgUqRIAH0kjZYVnJDjQuSGkBsX_NxW1XcJ4xQJGjb2u6ZPnVIhEa89tjGnsw2WJRl3Ce41gG7RkPLvCiZ1ed-PWgZXabQ5VxVCpfwkoZphCV5GNLLTg-ltkq089aVx4GF6XgaWttIK7op4_rTyayqHJbc-2P8ek20-3d03_BQTRP4NKoRnoiIAXbJ20Vq2RYKf-UN7LMq4aZRVwBlEw1POf6nXQD9Xiop4ppjFpgmm8GCI7ppalT4TNGtBupnF88huBjp91qjnFDHjWoicPe6Hr1Fpjj16lxpWTZnlPRDh-yLu6g7RLsismgRtwR39iDwcVxeHvzaLlK0IFDNBFHs66jiMBUh3U2jjVJy45XxAs2Zs9Mg1w7lpXS56GMW5cmo93XfWb4WDEgHGFGsnARoPv4bL7Sdx-FNEbM75IcIMvGBtvXbVl587XFE1JleP3_V6iwKuyO9WARptTdkBcHcqLgmjQIuLr2sMfV2Ri-Pb7-nI1rQHYBen948y30c-mXAi8uQwAEu78OQBWD8HcZBn40DW0iyszAG4mEi3zmKYQDuyVuSe7s2k3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پنج‌ موزیک رسمی‌جام‌جهانی دوره‌‌های اخیر؛ تنها دوازده روز تا شروع داغ رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22459" target="_blank">📅 11:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnfNEupiaVvRZcaBMh6A5bcnMqjBy2PifnASlAHlDkY-dYMDeCEuXIM_aQ3sAmuM7DRT5QWqqR5eiHKWUYTWFNirsTBzY-t2c_QaaJnppOMJysNnUiztIR3ukwfFRMpV4NF3rsmCUfbAk76v6FfHs7JYVl7LqU04gkf7e5OlDOqMl2i0Lsn-TPNUX6C-tXITWZXupYsK4aaMfXOX_nx7fcZQ_o8d9c43RVK9195KsTjmHktDKGEtvv5aRtNF1BH-MN2BKK0hT-V9wJcNTivV7CAkzwyaxSLeOnjz_6Hai6z3OGCTuOEAKykwILIxDkWXcD-KMJPVFjKTOrNTJcKJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/22458" target="_blank">📅 10:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyPyau_N12XjPUbXmFetOTPCVAsWBSWZXzEdQfNxcLDlwuVI5qw6JV40INgcUN3RgjS72Z4FcFMtUEMCY0Qml_U3zvCC-qt8Q-i8PQRNk1NbzwYWMtG6YKo9RuTgWdhXlWE45pkXfVx_yfohF5u71pqMqGPktpIoAcJa776psc2WxZuhXY5kh0aUtcCROraqrB8lavoTffLaum4tdiFGmXWCftvuGj_O_rspGJtfcEkIi6UtNr1upvpLFwp-E68KqfR-N3hzD57CbDVAnJuWT3VXHG9rZBX0a-WqTgip-ndlzFgQrumHbGm19dFfRj6uOjBgiRwfFL328hQNmZeBcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
به‌مناسبت فینال امشب و حساس، مروری بر فهرست پرافتخارترین سرمربیان تاریخ لیگ‌قهرمانان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22457" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUT5HDksavI0NM65pz4QrH60uDoERWJBxYjBWoBIEkDC4IYgePdvwFK9IkDpRW6fOrVkppQtLXH6pDV0FGa7ict5Jy0_m_NQLdhHe4WJ7BWei_rnO3VwDssRIR9W5eUjnJ3B-T6BhnlJzefEeBxrwf9yTtlQYb3F3pptvpd9uyHn1Gml1KZ1KXzng61GP7lkPg_n5xY2aqrfa5g7sfjkz0g8xdTdL149DwqiZpO943Or9tHbwvFs5sWoNVXFfltJjsSNUfPjxz04gpBtBvDZ0REQlGhGVk13SWAxOTs7aD3b08Y6-YAQ5r82RE6YDSqjWWMhQhKH6_rxZZuK2jbCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22456" target="_blank">📅 10:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=W9dsEtFJLp0XjEUGO1WDK9gwEQnMXYEy_LY4vG0T8ckWuug1o3q28SPlq5eVQx6l0q3KdKAvDHcOCBXJfqblI8XlDOjwHMd46wC6zwlUKjqBdewgORblx1zx77mhKn034TrY2ZeN2cR8A8Jopcv5kI6buTD1J0n8wEXg1dMv2Q5uUz2hOlcAiY1X6PAu19BsnQeY_aP-zrSstOKRfC44d1JXO03ERNGPXJn5OFihGIh-88pngAH7RLbGRgCWIBMmW_X2axEBtlVWuT76ZoC6z0uXA3czN4D-NAqUeVuk473ZHHFWrAkEb3FI_pPVZA4d12biBc10Jcxh0N6Jvwk1tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d629612bbf.mp4?token=W9dsEtFJLp0XjEUGO1WDK9gwEQnMXYEy_LY4vG0T8ckWuug1o3q28SPlq5eVQx6l0q3KdKAvDHcOCBXJfqblI8XlDOjwHMd46wC6zwlUKjqBdewgORblx1zx77mhKn034TrY2ZeN2cR8A8Jopcv5kI6buTD1J0n8wEXg1dMv2Q5uUz2hOlcAiY1X6PAu19BsnQeY_aP-zrSstOKRfC44d1JXO03ERNGPXJn5OFihGIh-88pngAH7RLbGRgCWIBMmW_X2axEBtlVWuT76ZoC6z0uXA3czN4D-NAqUeVuk473ZHHFWrAkEb3FI_pPVZA4d12biBc10Jcxh0N6Jvwk1tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پدری به‌همراه فران تورس و دوست‌دخترش رفتن شهربازی، اونوقت پدری نشسته کنار فران؛ فقط قیافه پدری که متوجه‌شد شب‌قراره تو پارک بخوابه
😂
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22454" target="_blank">📅 09:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeWNrWMuQD4eKEvvrFaJ7CHPswqWebc3m1120j58qeAJDlbSkIG7Sq-PB9F4_Qs3vutrj_b1Cm7xRORRnzUKBLKJ51yxsIsZEam4tHEnmGLgO8rqQcZh5LsomucG26AOophqnu2CeLEyA6a-SRtFkZskzXqJzvvtFauoeecD8QMy1QDaYlOFcLglV__UU55bJDpSK-1Ra-gMa9twMDokGegRKtOg2N_kjHuGtRruf4irlo-JFE9y_nbEukW26lUZ_uibSbNUYCfA1IJiKreYWI3IqVFtrMRzwFxg2_pkRQkYxUbxJw5NhxpEbAJo5VziSNjmA2c2mb8qTp9VgfRGpPLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c867b80a08.mp4?token=R7zKmr3QKS4tMhzjhzMCkQK5BAb-9O0FiznKzlaS1v44F3dex97_TjbjiJIVPF4rZr9rNC_UnUksY16TFfaYGMaU5hXCrm-9L5yaAs4TraDJ_sjrVyTYzeBX2I8qk3vlMxedDYwsoDbawTXXrbI7WYisMvQafYNxWJ0KLvh8ipn0ld0PkfI33CkG1FMl5Ln5eikEOuoCFYdglGzDx8z-2gZCjUBvy1akTVxh6Bw5WHjLQbTDLv4tTXdOUpWwfG4FjcsQGLfm6u5cCSILLkRHtIGiTnGofd4Cne991Or07lCPZL2iP8b-Y0eaT1SmgBnG0WIdE3ikt7QytZHSqmKbeWNrWMuQD4eKEvvrFaJ7CHPswqWebc3m1120j58qeAJDlbSkIG7Sq-PB9F4_Qs3vutrj_b1Cm7xRORRnzUKBLKJ51yxsIsZEam4tHEnmGLgO8rqQcZh5LsomucG26AOophqnu2CeLEyA6a-SRtFkZskzXqJzvvtFauoeecD8QMy1QDaYlOFcLglV__UU55bJDpSK-1Ra-gMa9twMDokGegRKtOg2N_kjHuGtRruf4irlo-JFE9y_nbEukW26lUZ_uibSbNUYCfA1IJiKreYWI3IqVFtrMRzwFxg2_pkRQkYxUbxJw5NhxpEbAJo5VziSNjmA2c2mb8qTp9VgfRGpPLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موشک‌های‌گرانیت‌ژاکا بازیکن ۳۳ ساله سوئیسی سابق باشگاه‌های بایر لورکوزن و توپچی‌های لندن.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22453" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=UuLfHCHunTwR0Q5Zg7GnRibEn1AL6_WZ785A4JOD8DJhH7DTu32PHeK6LYd0mI4lWPgMi3v4G1fZXDIYx1j0gNqg1UPCCovgF-jPGbwjepJyH86f4go3fwVNgv-7uMc9-e3wB9KxKZ0Q1r7gUY4ncz5m7jC7rMy7pxkMSJfiMS3sITyhGkWrwDxpBh7gZWnLTARKSIF8IoJGpA9zVcEWhL6--SjwIitgB1L_FI1zkJPfNWEljovNtPX32YEK68KAM1ERCXx6daVjCxQ2J1s_1kVxBWNfseHjzSvbvLTWjJuJWeI8xpVonnXTbE3jzIeD8gPRzbyBz4rX8eqm_Fwo4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/928b5d2877.mp4?token=UuLfHCHunTwR0Q5Zg7GnRibEn1AL6_WZ785A4JOD8DJhH7DTu32PHeK6LYd0mI4lWPgMi3v4G1fZXDIYx1j0gNqg1UPCCovgF-jPGbwjepJyH86f4go3fwVNgv-7uMc9-e3wB9KxKZ0Q1r7gUY4ncz5m7jC7rMy7pxkMSJfiMS3sITyhGkWrwDxpBh7gZWnLTARKSIF8IoJGpA9zVcEWhL6--SjwIitgB1L_FI1zkJPfNWEljovNtPX32YEK68KAM1ERCXx6daVjCxQ2J1s_1kVxBWNfseHjzSvbvLTWjJuJWeI8xpVonnXTbE3jzIeD8gPRzbyBz4rX8eqm_Fwo4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
لوئیز انریکه‌سرمربی‌تیم PSG
: میکل آرتتا گفته قطعا آرسنال قهرمان چمپیونزلیگ میشه؟ اینا همش حرفای هیجانیه امشب‌میبینیم کی قهرمان میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22452" target="_blank">📅 09:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22451" target="_blank">📅 09:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRU-koYTSrQ6tR81qlCmwitsyzbByrVMPBzIbHj0t0ntIvinMUJuHaN991MjiqNmKCrZO3Ld7uLYtuzJMtnhgKg0TOSR2TE1nQ4eGvU18l3D84SIWj6ttUkKP9P1BdiDJo2zPP-73Cs9F8Q-edEbBV5qMpqJJe6UOwpmRQ0Z_Q3OlNFaZq-dHrRBRnxaaqxs0nV76fKIBU1Mywi-NtKBP03-Ln09jw7_Xc3rp81wP9KP0f9jFN1MxHZ0oiqpG1TIXewMespw0y-FIAI_i0PDYSH-JLvqECjtpVrDgoYtZ3z4QundYva7V31LPU3wn-2k-4qK6f8mE1HN5QzcnBqyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22450" target="_blank">📅 01:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwufLTvVwgvkJOPhXj97Kqt8PS08HzhBDpM8nrxxcRlDJFSldspUGD6jVrVvGSqzrYLHziHpENxJQHHKgnUOQvtchuo2GKSqqos0ZmqXDe_rjeqNcOfl2WjzTQKucgyOA-8VpZDhseNoOBQ6PVShKXk0bVQg_vQPffgKR6NBLQ3oQ44F5z8BYo1YfZT3bzpT7rwW_gvHQA3uUaZ7g4h688WezR9YkLNz0WIWIYrnOh2OQEHLNXRT3PBlrhqkNqxeolIK5DHSma8f7H_JO_pQkNkcMwT07tLK83Tw7KPLmo0M903K5NnTg5TwsclbIawH7TQVkIzOM1bVrg4Yx6rRLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها بازی مهم امروز؛
پایان فصل باشگاهی 2025/26 با فینال حساس لیگ قهرمانان اروپا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22448" target="_blank">📅 01:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrhPbB5ghYGy2-SJLCoU6ZqxK0HIz6Kr6qsRemkONW4StutLAf2OOblW2vxaVTCNpRtzHyivcsLtHZjEfSBra_4q3nPMRooLQcgcnA4ZbPR9zOlT6GqLZVtzX4U1P7xl-VFiyi0uN0JIYOXzET2bQzS3vEOsvIEVMu_kf8Kh4izYd5U-QLyxgSw8_6fNBiosZ_ZOLZxpdrolNK8STrPpO_MZM1zqYS7SPj0W2FAg38ClS5ZfSNg75IK5Hevadm3WPTYaCbpHkdKbdJVbCpByXNd0esQKRoKHPhCl0X6xOoDkN4cbi3vxC0nU_tjy_8OhtYb-R0rL8bzWgpTAAmePRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل دیدارهای دیروز؛
برد تیم‌های آسیایی در فاصله کمتر از دو هفته مانده به جام جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22447" target="_blank">📅 01:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9FqtZFbaEBI9htszqcTxfrXPjzRgo26GVTskbIsr4fbP8R1dTn6gCLauCPoNQt0SQ_UvQAWoKJWKCu8yMpvusuE3BzLr48N3MMEP4hKm6ehWQ4ik1MBGbhgdWpTmpnYbwRgE0KU-Mm0zr9_ZGtBMl2X9Hm_35QLfUnayASGvi02HK3VlLvYfz6DpUT_lFWHiit9udjHWBzWot_k9g_PEQH7NjiYZPovNgr4_adVN2xXNUOYvR1hbVI1yVvlusP55mR0pLs9E2pjuMpioZv_utAEQjyY6R6TIclorZx0n-2qlGrFSnyCyanuuhymOEsv1BGgLyyTjhcXQn2g8dQ-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فواید پیاده روی رو ببینید؛
گشاد بازی رو کنار بزارید؛ فقط یه‌ساعت پیاده روی عادی میتونه بیشتر ازاون چیزیکه فکرش رو میکنی بدنت رو تغییر بده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22446" target="_blank">📅 01:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEM958fL9Lq-LfWs4wAn_Wvd46r_oz2hUUOvAoFhRr9xNrfBZvVhgWERtWBvqSFnlGmn4uGdaEtpQMoTva55_Xo-yHvu6Bgwz1EWiuP4MOOEY0_kp1L_CXfayfaKyNn4iDAMhZ3T4836aGRn3Fw-kSeOnCJh0mfJVfueG_01tcuK3Y7s9e0C4cAqA4UI7d0aNrtw_QOouxE599ErIWIZPNIOxB8pSCwrCpHAShCTPUbDi7c807wc6VorCTw28Gl4zDPWLpe2chZTTKi4T-M3jlbRoooXZQScUqIHdATANHehKZEwsPI5vSRmcnxUAt47cIluTHc8JdbV5hyy8ujEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌فوق‌العاده‌حساس‌وتماشایی فرداشب آرسنال - پاری‌سن ژرمن رو در آپارات اسپرت ببینید. عادل خان هم بازی رو گزارش میکنه. از صداوسیما هم یکی دو دیقه جلو تره. کلا سعی کنید هیچی از این سازمان مزخرف نبینید. لینکشو فرداشب براتون میزارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22445" target="_blank">📅 01:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YULn02M-QetsmLolq0JMG7eskvJ50cl3zdCuKlGswpcaj2POOjEuZHiWyFDD3XX0agLC2uMu0I1gTVH69vf3Ny6lSqwPnRPb4OckdevJFQwzfj0KFnsSVzQyPcGBueMqGcM87UWVhHvVpIddBXejVuQyeVZcN4L6BYdMU4q4UdxVJPtUiu3dFQ79YCKo0ARBJoD-iWlKB1QS_xzc27KoCtoC78pnlXDTxcSrXZx6aWmc5F-keGepLvRvRGUDdBM4C0Tx8v95hvBzqQYz5VB2GX0iO5K7mx5c0WmDoGJMf1ud0Z_JmKql4OxfdEEHxsnRDRKBQpeQmx8V-BqSCbIXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو: آنتونیو رودیگر مدافع میانی رئال مادرید قرار داد خود را یک‌فصل دیگر با این تیم تمدید کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22443" target="_blank">📅 00:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOV6gMK57iOyKXYASUM_nEDwkqr58a_y0hGYfqxuxFhwth3WvtTGyHCHW32Ca5yy7ekmAxRjBErwDq9Q4ylqKNkW0vhID01c2xEyxmXoAEjuN3FmGoW4f5Ae7OQRXrCu0KEHXDTH0sH_yvm8MmbJBW6m1gT0wyORFmNifpZyZ-Teb2qbESiW572WYHeShIwMY7z3gGYRiVV4X90YJ6wYTyhWCH4sqodGAIhhQ0HlllUu-dNTJ-egLxDbc7NnfKDIfOBcBUoq5jBmcjKibe2ZFD6A02MCs_FZBgkE9hPKzwj63vwr6zHiQkfitnWDhUtsoiZMr06vCbKzlwxU-39Z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hka8gcwhAzQ2zTtkVVPERKr1iP2mHvDf4Fo5G0__yDh5oBS2hhz9aa-5ARZoA0sPAWITydpId9c2_9KyFWgAQyO3dlYedNUnnSSqHYqY4c3Bur9MlG_ngXu7WT8DlSH_BXRdttiU2Rme4SSqEvLU8RMezsrag4-A8HADw7SdTuzraojKyvvhdNX4Uppq8ZQFvotWwd0MWlV9h-aDpyhzqncjZ3mwuPC6B_9_oPv5BMUSfvoMM9gsRmVa-5Dm9cWy9pFlpqcd_oaPYRomiYS34bLemwJaxOlw2cfu42FcD0KJR1L3LN23uu6Wij_EM0Wx9KWPIzTxUJQ9-r5hHs1HlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22441" target="_blank">📅 00:38 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
