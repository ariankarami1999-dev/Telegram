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
<img src="https://cdn4.telesco.pe/file/ONWm_RBiQtHKKk4qpirnmPYnSDcPFu7acWTLAJ-_JCScXByFAjIZZjfKsKSQuUAFsPhFObPTrGNIVvUVArI2ninB2Jr-CEj5ejdOCkpirJUwvTPo5TAb67guXSPSWh_-Hge2T2DQNkYAY2-pt-7alXRP0K4fgsaD-j_wS7yCYqeptJmfMh8ZlR0CaXJjgd2oWqx0tg16n-ZaH4ZnYOKegg2olLM4oQhzro4kRT_N4A0Rwkzh-rLJ-UTuFumakpUhe7Kk786Vb_4iu8xYrYF-aaGtlFwOBQe3cG6IxJNaCRbhR-Nso_ERh_P8eXLoOEX2Yxf8Z9ShZg-a0dG7E5k7Ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 315K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 18:45:45</div>
<hr>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8GrtOrmmygCDvXfbFSknnmOjzHcmCo3piyQoo5D4l4gr1-ZZQ6owHGtKj5uSfywAnm18D3D_P-nF1t7rqESbOm6AToq_6tTD_vKbaZBbjEXzFD5Vmv7hpUziNJpGESI5-yykAGXtg2gGh5RTkPNNmyE3klVLiY7EL0lhAuJ0ga7Ih8zK_m6lOkJSKFvt99X7yssdtZMiYc9m48i0zi8nDM6tl8tuk68TU3TtHGW_N-llVuROJHiAM09F5L1J1s-yT1Vztw8kYi19KUgJWhk4rF20a5bCXxHsaKYr11_1cFQg-1KNhnb8D5bWaxaMeBol-wze3PjivZs1UAj9FGlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpj57wUDhukG5myY9N-7mFR6CI9M7r0pqypDGFArMTQDZ_f3wNGOCNS8tfs1KYSI40WjLSsZvNk0rYRdyIqcBfBhxI8xkKgr4WNbqEE8mjIFzq3pqbfR9wuo_9mENU19oOWJTU69u86oCLZ_XxiJRGUknNMzDaM3L6p8CPGGnzRo4FX20fdMDXM06SWwCB1nquiTYNzHwckmy7eH5zSZerJCGeR9c9Hu_o0WbKOvgVKEXMYBOyL5P9-SEhXd3ORNlQYRhlUMb9ZH3i7JrdWpUc6eXLKVjxRjvZDzLMF15PeGFBaU9i4GDAtO74nst5vkmuTOCXKge_EmaOL4MFjEqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoXiUonUqq7Tw5x7Qv4NHCJ5b9AvXv-G5y0t6snTZKxJp40Gw2fC9Yf2w6Wu_ldSbJsIcxyzhGznTXvEEd94RPVF3e6L3m_kVKNawF16pLJgZmkT8f-Nyh4bWapXP9BXxgk8mmnjkQspzDYk0tNdL0V4q1cdr42Q7yoEjjdgeV9A9uuFSXsmZFlYePi6NpC7QFFavY5ttvvlwnJO2J8_TRKhhVbhdmq7aBjzToliKoTGxD0wQiHUszDFb0TD2DRvg2utn55PZb5d2cWqYI-KtV5BOWDkaD-adAgQvmBqD1BD5DmfIULtUJcra5f4OzSACL1PH1Yn0vIW-jdDuSD2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
باشگاه چلسی: انزو فرناندز بارها اعلام کرده که قصد داره بعد از جام جهانی به رئال مارید بره. ما مشکلی برای این انتقال نداریم. با باشگاه رئال مادرید به توافق برسیم بند فسخ انزو رو فعال میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/24221" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbZpHEBQ8Lj4YNuGvBLWQda8JoOwjnigYObl4VPA7vZ76G9viBF467gAwFsXKfezTDGA_lzDYPFG77dcjcFHWV7Y0mM29tMN2Nd2Y0Rx3wuArSV7eBmcWBMCnbkvw_LjL4qMPMLNljes8_2kLhxBv2lLVy4Hm_xMKg-h7Jw9Jx6kopRnePXOCkT-rcckiY9fITQWnoGS8i_MXpXBOnKy2swl2jNi1DwvguAL8a99IsMgy65wp8BY6OK3ZffUR5YNdGLxO6qi2g6h7juOKBGWTSyzdesn4ZHspwcvlPFZhhLX14PTLaQpaDiFuaOJFe56RnU63iCw8HPDEfBfK3JGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/24220" target="_blank">📅 17:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZAsBT8e8tKq7xca5aLd4R_k4YOU18nd4rusKnqHN3INSt9tZIqvksWkLKSIw47KUD8rg0r1LgymgmjBra-6Nx5mct8qyhOJqmV27atl8Yl2R_8-zQygLUl9SXwKnuXDEsOT9jDYjp3_jq_TyBn1TlKlwvcmjgQTOWQTLk--aU0LB-zZGTwy2OgnkHnMqiUQrvAlrTMh0djV1EaJu3n0omISefrsnI8DWuSxws3MWmBuM_2j1DQZJVn_-1G750axnb-84xbttWOb5Vpkyn7cYhnoxdm1EXmo9Q2rNTpsFgNYoOoIYjZvK615-csjHUEHjv2qRhkzrKUHqfV8KMubSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/24219" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0kWPW5LJKzNWzi0gjx0MitJQvu-dQ5DRPjKXJLnu0FZ3htpQlO8gYGODfe58Cs7q6Gz8aPpFxjMqo0VKXyLNLYfRdocG77zcZnR-wiIjKfXKSvTES_eoRq93bw57dQ8LORFGKtUt4jfo_lIlLET9zgJGZ8HwVVPwPcyDy4INY0Lc-6yJO8i_jRSmaO_WLk4OZqS_bixaBL6GUjWkPAajaa6wWUaDHt_FZI06G3cgeV-s_8Z-RfUc8n5ENG72_hSrUI4GGJfHJ5BIVAQVKmxtq1-m7peYNsM15Z6GcbHVJZxkbV1yxUwPHvpa861ySIsr22HDeI0Fr7bGYOwxUtM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
علیرضا فغانی اسطوره‌داوری‌فوتبال ایران به عنوان داور بازی جذاب کلمبیا و پرتغال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/24218" target="_blank">📅 17:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgCAQ-wPtJxCvjn1_lgeQWMr7i5tEV3iCENyORXAXR4ZRo4hldWltUa2iPV7Nh7EKcavYRdb2yKZOGNTW2bhGqgdhAEBCra7K8uwK4cBSUVdmTem1CXUbv5i8xPoYK2xPQUUYCyj4cCtWlNCYLRpjvmgUiT4iOpaBPpgfNjVPMTsI_6tkOpNk8UR19ARunP6eLBchposmQ1-QVkIj56nMcq0cFCmtKzqrDaQsVlboRmsRq1GdrSIHXtB5hOZrizyd5S1KGxbdzlQofELPd9FffcqmdDWdtv9Ebnqx2qXCMb42b8hC03aORW1hBynF6bDcJea2u6qtH1sDA7l3MGCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/24217" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbI1WHaTqhYNt2Dm8bsuy_fBi_gx9G9vxCGirUbXTzzzDq_ozpSrfCw69VTMiNzy8MQHBeIvgvCzSg17nxQEeN5vUID5dGSYFLga5JPsJLDGKp3YY8ph8_i65z-OwEZ9z70yXrS26rtW6unBFfHxj6rX2S8vVIPvkiKkxqiHawlXdLtiqzXNhf1grPouuDolNs14JRCpWjBseUEwLq6NIQOFCBwK5QJYb0GFQggX9aO5TJgPVrnSoy3lYq7hTTEMA1_9NSngKny-BFB0J7kggVeqQpia14dlV7u_Kk6AEl9cbwredlLSDn9YZPyEflRyZnOQ731MD1UJXzaIyaeNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_FV4DWPlzNX5NY0K1OankD44Cr88eC6QsDlZEbtx0IVTFo5kpTNVV1OnuJa_Hb_JcmDPzXCjk9GqFxhFjdlB-AwPMysYmbsi8RKCDCahEB1s7dom84UJ0SIjUk3-IifYpLCI-upmM7redMDrBJWR3gjk-hS29fhhXjrneW3Z6eTLO8tMxYOpfk2jH1Znq3BeAT14UKQ97q0YvZjTBUjmT1r0VxGFbiV-OMurI0TWrCAUWe4bZ-Q9vVVxZEQg0iPJVy0zq1T4jPTCgUvjhZrMDDIwADxER_1c8otaTV90tpHFuGvN7mlVcwYVUGC6nxMGJktyQ4ZBrBPAiu8DpkTuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24215" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Rde3rlYL8mbxvrOX2hjWFnnvgcJ0ckcJ-F4YEhbtDYC3m-EWK2ZRsRS8R0qglV3pRHKZ-1mqfz_1z0-vGQcnSzerHdRHhVWD9GfwhI2PsLzTXZ-JhzUC6LjSRAnaI-5sxY4QBr0W7c9413-a6jGeX1d3Ljo6UP50c4-idhR9scbjmGIBAb6kT-_Bk6e-nW5q4ejwmfA0Hfu8aUj5Le1h8RoLappy6iHOJw5L0G5aeq-miEZPFtqxXwZh6A7gsiLaNf_PcVnpCJGB4ke9-MNSrYfa8RMqQRFzsfEAJwXYAPkz2KNaqWgxJ0AL8ZLh-z3OEHYSD2FK1k4TcYOlARuQ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79050b237.mp4?token=Rde3rlYL8mbxvrOX2hjWFnnvgcJ0ckcJ-F4YEhbtDYC3m-EWK2ZRsRS8R0qglV3pRHKZ-1mqfz_1z0-vGQcnSzerHdRHhVWD9GfwhI2PsLzTXZ-JhzUC6LjSRAnaI-5sxY4QBr0W7c9413-a6jGeX1d3Ljo6UP50c4-idhR9scbjmGIBAb6kT-_Bk6e-nW5q4ejwmfA0Hfu8aUj5Le1h8RoLappy6iHOJw5L0G5aeq-miEZPFtqxXwZh6A7gsiLaNf_PcVnpCJGB4ke9-MNSrYfa8RMqQRFzsfEAJwXYAPkz2KNaqWgxJ0AL8ZLh-z3OEHYSD2FK1k4TcYOlARuQ_4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی از تمرینات لیونل مسی 39 ساله
؛ نکته جالب ویدیواینه که تو هر بخش آقای رودریگو دی‌پائول فقط چند قدم با لئو فاصله داره.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24214" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFXCZFagW1CX8tl2caZiJhgUQyx2tubYEauQvyVFrtmvyT32w7I5Z_CIX83nh3gN3yVQha1nnXy1575CcyOmtlcfYvJ1UyzuhLlh3CiY6IHYlpuuIFULz3N4BLW8LQ34Vump_6xUZi2DaCwzrMhv1cAJbdp-Cj-jMuUbhCA7igSdJOQiDn8zN5-K2Xdxg9IRfaF6SAlqrHpXX0bFs9Kiwv7eJG9HaFwDw19a45hYfWz3Q-tULUDoERIkeYAR_hHMaFa8AnlINBWk8Bteu2MOQzBuJ0aamt_xXubL6orx8nA_hiIPd_G9t6LNHcv8uz89d3hiWBS2W1vMbFvzBp9FEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbk0q_hkmFCfA8IgnjreQYfK3BgXyaCwMF_aDqUC2-mLF4i6P3vcfpwL8lDDQOrGKiCesOs3iunfWSc0X0Uhh3tRRueW70X_Rkygf6J3mLI0SIUCbfCM_aQiHVS7uTVMk_dC4OAV1pQ6Wa9IKPWXRy89zSAy1VB1wR-fMQ0f5lGkNZcvDifePoYm-zisCoSJYSP5AiIW4OPL7PmoGhUxMivAzK3FQFIAn0AJtJxt7gqOS-gMOSkLwWJJ0SUoDf5sP2EwiBshZ5vWWvHS6bw_DJdphipB0LPTBYo6Y11qKovPd9qKebjYhfNxBEDO37zlOwqUknor1o51wCjiXb2QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHU7uzk-fxyo5Vvgs3i8LxYllApVw-tYQ8jGt_G5tGLySlZb9FB73pX96Vyo-sqQ1wn_c28HKoDjXx9cQ752gHB4i0pUjyMaql3i7_s8TtPs_mmSs9vMKtepq0QsglpP3rpAdPn0ofpWVOmBzivOMr2QlOfxK9ys5LipWuaDm8tWLfUd0EIbNLQzOb4LKGZ1Qdn94v1VllCp_vDmjUrbBeS_lE4DMXl2SYNwVbkXI9d03kRnpln1FyXJOFI_uLerHMqLcbUxHkDIzycHliKwzqkSprdy7Ux9tNd9Q2s0cx7IeGeWsO-bWfuWj8k8PI_jA70GxfaiDlwEWC5MPlZIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lytJdKwgSjdJU75Ee25-f1hBH7I0b4MnVXi164j7KjyahmSIsbLSOyiSU_nSnXOtE9auyNjEZzNeFayt-sEL-OAQHTYfOLbKJ_O0j8n02Mab4Ct_7B9UdlnTyhUbwKI9JeDMYwMzy1zNNenxAt-TDwG-3ACGFXraF8Fl3G4rfPviq2BydtHrrsps3eB6i29mQ18_FZhLkGknVxxa2x8tRtpJLUwnZUkKQalMcl5rUNCZlNuwNUMHzO7zH8Suf8weCq61zCCqbIG1QGdZlREoWJQGAoU3pMTEbLLS3iYqHjMmzdfbKsczy0rj7MMV2VFPxaHy4VcKN9ueDtwzviaPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tar-3hgazk4MAXgVwojBvrQWwK4zwg5lihl88AnsZufcixVICfL1TS8k74uUhnbvOjiXs-CmNDmd4tu8yzL-MPHCykrf7HjcV6XAlZQKxE2zpHKVTgR64N20cA5Lf01eGvgkM86qBe46kOKA7cTi314LwScJ49D41dmPixDQxt8HLj7nYp4TUKEqxhTER0CflXq91-wg7lg863sSRFfli-Qh5Qemr0oLTU-asrY_AFW0n9d-UEJhcNtkgv1K1Efb_baw2cisd9QDlLpJOTrbL7FIAHvMjr4ztZHVR3L-BSxgYUIUmDPz7mTRo5_jX_MolNBdjyJWb6ECYmb7kTEgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaWIC8mMFejXVCeUwppaBYuaktDMHtTkvy5kJUizoLuiExGmyzvQFFGnnxyule7LJymhTRh20D1G5YloAlmw79wPpAsXO_gUbxXaGJIJe4GBuJ_ejNw-spTbY975O8ftFGfHZxD88JUdmq7cFd2uP9vHDC4sexAaalxqiFN1kr9DKlvHpwBsCYSygnX2dwhfNAFYfpKGi8ieboF53K0NqDdP9PGEeeSg2mgUHyBcqnVr1A-LA-JdQTq_z0rFFBiKIb304-kOPfM8flfxgtDnp_6v_LJU_svlYZADDghodxyVmgseoSz0kW5GRJ0P6DydCspY4XAyf-lgDDkV49hqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=TM7j1AExwdL2oQikYUTVojkA-eN1MSpEzsnh849S-YcB5QMrVOKtPvcw0ycu06VJsPvNFsowZiA1FthtgEJzJklf9bnswS62dT9LyhJmFgf9PJCxbcv7etXrcdeEccrPy_IrkdAmFNQhzwC3r324s4-xUSBZQV6HFHycPWk70YcCy3BFboa_LJPisVf6pd0m5reoUTF1AhWHd7OWsq8JRldGOsIyBxMaBFhz5LINWO88yENMNQA279nGCFRgqTd2esoZq2YtsTaxhx66JimJkdhMSiGTtZU0WABbSHtPuaPqhgDJ_ntyy-23EESZ7CnrumiKZUUQNp2VmB_FzHURSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=TM7j1AExwdL2oQikYUTVojkA-eN1MSpEzsnh849S-YcB5QMrVOKtPvcw0ycu06VJsPvNFsowZiA1FthtgEJzJklf9bnswS62dT9LyhJmFgf9PJCxbcv7etXrcdeEccrPy_IrkdAmFNQhzwC3r324s4-xUSBZQV6HFHycPWk70YcCy3BFboa_LJPisVf6pd0m5reoUTF1AhWHd7OWsq8JRldGOsIyBxMaBFhz5LINWO88yENMNQA279nGCFRgqTd2esoZq2YtsTaxhx66JimJkdhMSiGTtZU0WABbSHtPuaPqhgDJ_ntyy-23EESZ7CnrumiKZUUQNp2VmB_FzHURSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=ScnH9FmonGSly1NFpD8OPr9hd7Sm_SRSGDclrT9oya4BiLUHSAYhVMm0gUaf8qVnr47MTB7VYwsYwS9S_f_GsTQwgBDaYERsnAvO6ouXfRBj53wUyOjgO9nrakSM_HyG6a2M3dlr_DgN0UmRDKpEzq6qprGSJnAXdIRR5_f5oJQ_T_N97j-jAY9q6l0PW32F0vn90mN4eG48RFsmvg5JLBLnTOivJUShXY-y5JQea3jDdKA3KTV4DQntnyPLeq-qN43Ms8HxSXjnQRBMfsYYhLSODbGCD292LW4Q5LB2scfe70miLIZYY_KggfOjiYtEGsvTcZSiGe1ttZzKTisFpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=ScnH9FmonGSly1NFpD8OPr9hd7Sm_SRSGDclrT9oya4BiLUHSAYhVMm0gUaf8qVnr47MTB7VYwsYwS9S_f_GsTQwgBDaYERsnAvO6ouXfRBj53wUyOjgO9nrakSM_HyG6a2M3dlr_DgN0UmRDKpEzq6qprGSJnAXdIRR5_f5oJQ_T_N97j-jAY9q6l0PW32F0vn90mN4eG48RFsmvg5JLBLnTOivJUShXY-y5JQea3jDdKA3KTV4DQntnyPLeq-qN43Ms8HxSXjnQRBMfsYYhLSODbGCD292LW4Q5LB2scfe70miLIZYY_KggfOjiYtEGsvTcZSiGe1ttZzKTisFpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن
🔴
مستقیم به قلب دروازه ی دشمن میرن
🔴
ترابی دریبل زنه، نعمتی هم حامیشه!!!!
🔴
مثل هایپرسونیک از لای دفاع رد میشه
🔴
یه طرف میلاد و از یه طرفم جهانبخش
🔴
پهپاد شاهینو رو دروازه ها میکنن پخش
🔴
حاج صفی، حردانی و یوسفی مثل شیرن
🔴
توپای علیپور از پاتریوت هم درمیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4_E_XJmvGGnQaEBTCFHcNIj_Olw7DB_t_DkjAp0EyRZEZmkFNQrnn_Am4ETwaYIV_5yE50pmLdMElxTgjOmOw1PAT37o4Xojz2b-fVOEgf1dc_LP8_LUxUxsgm-sjwKf_s8-xdYoFA2QPHhyp4xvbR_3yfLM9AjJP5WmKQorW6RTeYUEBrj8XlWt6ApJ08r-iiQjBm6muq0ZTB0CrG-qfHzQcLqe8vyr3UuPo4LyCcrWUEvM3wAUUi2apl818X_e7xORJ-8OiRouHTljlCIa_9GzygycxyGyM8jsFlx04wEOgLEgDZifLm72F3MsEVKEGauBNOgYPyrupZ9kxH_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn8HVGbXprb6iz_jFb6ElXXyrz32umzbMaL1t8KzxWge21mWQ8N3WeKys6QtwdGEP_kjoEQhaLqxFlKCzSG7-nKpkb5C6ngiYwxEhM7d0Ld3dMCA7FjnXvcTfvusuJWUwMU09-LtyBTTwhEzqr8AC_iQwHfsMkH5obZT6lrZ5qJadXpg0t2OthbM7Ds5WthP97SKmcd68CIqKdFdClfI70FTdfrt46BOF-XzuGRbfc9jVXtnAAPeRE6GNrb0QtdSG-SLg15yq1Yd1Lmr5npeqfgHhOdO1ow8SAqq0tuvSUGDhchaAZpSgSDxoQO2QY4iGky13aCkPo8LrIvBdgDF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZHUqv069rTkrqIomXc1-6XG0izO7JtK6_c3_GAFu1yJ9bRheaR9fpM1K6VK-lEekHo9Ibz98N3Qm9zUOwnDV8yWTvVfH_w7O76VJKrTK1uECrTBjkRflxpuiZFzS8IEuDfZ5ZtjnT3LvKJClsbgnFpWvyen25RQkSQSWpDdXwaTakvquZ6ALtS2Q9bhGd7eUj36IcGZuIDUiYBP__3U_lNirqUQMe-XsZwy-45-8-6CfGiX4URslL_MbQRNgTjnR4S-nBCSZmdHDpMxXZJv3alDggXbWaoXJws6FTHrdUvEkADRRolCrI8LhFPuhf5u6Wp9oCptBaQAZSTVV3ACoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBGflQFANh9WP0Y8q_98wvkNTt0BAWqiPRKyvoSc5HhKXO-rcXS8V50zBTrIhmGjb4RM8ufJOqkF2fnCj--HgraXyseFzlZNd9irGLIH7Z67NXaaNdGOTrmPLKVcQomqsG5-kXKJlg46Y7pvnpH0fPhh4Otqp9q-cLVXQsLkheeDwBwtG23o-GEZqLyAgKWUPYM58GKPdzYjLgO27Q2yUtrTKqdDjg3WezSYUuxhrwatIm-AOmMNG4sT3oSW2gkV3K6WcUJh5VsJRHvB6vMaK7uWg55IFRQc1Qn8YSvH8s1zB4mX0APtA0UzgOmgOOYhnqvU98fP8LsO3SvTjUpSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=OQpINFtm7Il9SwGyzs5LgJT7qfbsoT-zT_iOGgsAXplecbxiyeoL-spQa_gvsO-Wc9qps9gP-5f3PEhQeHi6U63vHIHEr8V4dzFNr_cddaupNsa8jECxgAfAMU9ntt_8VW_jk-nYhAj0Dc7Vwrbb3cKKAZ9rYpEfZNIPaHoKdGaMB-KmPbk3A37jwNUsstDTd-JyWlDakWzJBytRmpjxe7B4tchMHXwlImXDLTne7l7HhbhOjDKj7ZUa04rmW2oG9U_PzaaSSNoD9L9BRHiGu5etcZeybOFtwbpA5rpwPR98I65GvIzXXjlDAKZiP5Yg7fwl4e6NpoQlErd9JbIcYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=OQpINFtm7Il9SwGyzs5LgJT7qfbsoT-zT_iOGgsAXplecbxiyeoL-spQa_gvsO-Wc9qps9gP-5f3PEhQeHi6U63vHIHEr8V4dzFNr_cddaupNsa8jECxgAfAMU9ntt_8VW_jk-nYhAj0Dc7Vwrbb3cKKAZ9rYpEfZNIPaHoKdGaMB-KmPbk3A37jwNUsstDTd-JyWlDakWzJBytRmpjxe7B4tchMHXwlImXDLTne7l7HhbhOjDKj7ZUa04rmW2oG9U_PzaaSSNoD9L9BRHiGu5etcZeybOFtwbpA5rpwPR98I65GvIzXXjlDAKZiP5Yg7fwl4e6NpoQlErd9JbIcYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSTZJiDycVWlwVAbc8qEbtPcoOpSyva0MPzNnJGQ-ev9yHFMeBdN-82LbsJt6IYGzonFIal_FzX7DLBMsSpOnkiC8nJKC94EDzIZjfR2izebOwcvY-Rgpt2YZaNmIKKEZgl3diOiEarr-s5PUoCLvgU1eO5UVObCODH0Cnqsq5SSIUAe08w_OYme2HdaXSRhFqKLmjj6nkVPT6tChfWvuzyxSVc6-4z8wlvo6EepBzydheyPij48tIw7DaU9RX3zJDeUhED89VdGtKUOIJ5h4WVg9TkEKZcZrgiepLO1MtrynoCi2aFNMUVOHIudbC8bmJYqy-AH6VeQ98DNVd-zuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=RJy3HA6QitwFacTqeFI3W2k9gARBJ7IWcrYJOCbE6x8AplApIRM0wveER8pTrZeRPx86J8LVmz_1l2vEtexp-jS_FSu7pIfOkF6qDueT9RFvC4lP2-VoXFpFiDFyy06H0Gug4J0BtQrF3GU6vGIiyaqYKIZ8buFCzR4iOWFTcoSygEs5BMbgepdCRVoSsqHfMbmsJbbrfb7zBwwZ7v7q_buHuAwV2MfXxpWdIB2j9JKqXT-0fMisZ1gtSgloOYw4JxcADIwUhVjP6iKmfjjdmfqNv_kdrU_AMjqyg4Lly6XODqTjt1b9r7vaHAq971DDt4ZkLWDHW1cAjEglETd1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=RJy3HA6QitwFacTqeFI3W2k9gARBJ7IWcrYJOCbE6x8AplApIRM0wveER8pTrZeRPx86J8LVmz_1l2vEtexp-jS_FSu7pIfOkF6qDueT9RFvC4lP2-VoXFpFiDFyy06H0Gug4J0BtQrF3GU6vGIiyaqYKIZ8buFCzR4iOWFTcoSygEs5BMbgepdCRVoSsqHfMbmsJbbrfb7zBwwZ7v7q_buHuAwV2MfXxpWdIB2j9JKqXT-0fMisZ1gtSgloOYw4JxcADIwUhVjP6iKmfjjdmfqNv_kdrU_AMjqyg4Lly6XODqTjt1b9r7vaHAq971DDt4ZkLWDHW1cAjEglETd1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4-b7Ne7e4dL8Jv26CeJmKI_yfdwLkyRyKTUhYB0xITJF3NDG-S6rOl9Kex9INVm7o8BDuvAVmWVtGZa0PK6K2QxKYARKAOcognN1NPKpzG6s10AvOOUYjceLMgYf4t7FMQMEK8BAITpFXjNpfx_niO3awI7yB5dNJ5nOPty5NvzmLIPOtiygUlkP9AB5WG3mlhSFiqxx25Fm6Htl0yKNgafWvsb9oOqVFHDspFCxiXFpwqIOuQqxKfNK_6ODHlQYZ9AR5VwxPj3ePBvtqNLAGfwhx02U1QA_dXSd_FFioQ0flcLAejJl2sQMmtZB9-t69IIqhB3dTQsGzx4kvWdlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=eUqOo_5dpGFLM4pMGs5tDXonJbYzlVMdNXtrTMY6aN5UGb0FV_GoDCzJNqADSF72utZ5QNRGcs4pnQ53ksIJpdDgWBj7REr9WyFjwlh1wq-BBNT2DEjcNJya2rJwaXz9CCW7Gd_FvQyoIbC2C1uK7R_R3eNgHPuk0kbOa5mx0vLNIQ1EbjJ7N7mXZVX_Rg49-bEPfJ5f3eel6Y-isKYUS4-RGxYjriEe48Q-YwKh-HGErwURozXTfcotNwwHyecSG4w0icQXLcVN5ZMBLhNZJ8kPG5iJh1TlwRm_Z8ENI4YfM0AxmR86b4k0k422cQl9ytY7px7zl9pFSw12JiPYvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=eUqOo_5dpGFLM4pMGs5tDXonJbYzlVMdNXtrTMY6aN5UGb0FV_GoDCzJNqADSF72utZ5QNRGcs4pnQ53ksIJpdDgWBj7REr9WyFjwlh1wq-BBNT2DEjcNJya2rJwaXz9CCW7Gd_FvQyoIbC2C1uK7R_R3eNgHPuk0kbOa5mx0vLNIQ1EbjJ7N7mXZVX_Rg49-bEPfJ5f3eel6Y-isKYUS4-RGxYjriEe48Q-YwKh-HGErwURozXTfcotNwwHyecSG4w0icQXLcVN5ZMBLhNZJ8kPG5iJh1TlwRm_Z8ENI4YfM0AxmR86b4k0k422cQl9ytY7px7zl9pFSw12JiPYvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yllf0_JiGgQZ1NPViuA0DarAd0uWwe6FJZpKvukPCW99e9H45YcprXJ9EKwTaMeUm8iGU3iy914UOYPUJsfYGVZ0OqcRfoG3s-ymKn3wvm7_OmCQ6CXAAvcRL0Uw46YOe-ceg1SomnGt_C7mftcul88T7DF3jz6peQdvv41ssWdHvftSoOZxhD95vWaCoMCRIL4l68PJrB1KKlG4352VtwAgbswAs9IhveO9zvl2mzU4S7OSBRe7HuZnUjSHrTGIXLH43mqV68lGAnqnYEXq2D7Axw-uhm0MB6omZJxZ3vkjRBVZX-gIKbXW6pNnfHmDWtFf0OpE3FrCH64CJgUVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=EQElHnmk6sF1LpEDz_IPyKejG9BnU1VRjZi_Mr012ywCdrooSL_W8nlSCYEnCD17suLcrZsi3Dq2qWx3Nt03omu-k7Xpz_CeUFaUSuOdTB4gWYd0XmPDWUez-lkYJI9OT_fljKx1pX65zZY3tyRhrHjH1s9a9TXhFa2efqIhnvPXmLuOZZfTxQL7JF0CWmXJMyy_t66vlVSmyUjAeRyge-u_CG_l9pZ1Xg5KYVEJuOVDzbqtnFE418KYm14pj45rSA9rksYU8aDicKgvBh_FHXeuGSzFvHB_hrcBYvBRXCGVV9bsVPbSIAQa7G744LOpKCqM8i30iN8vrLjcAQuQhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=EQElHnmk6sF1LpEDz_IPyKejG9BnU1VRjZi_Mr012ywCdrooSL_W8nlSCYEnCD17suLcrZsi3Dq2qWx3Nt03omu-k7Xpz_CeUFaUSuOdTB4gWYd0XmPDWUez-lkYJI9OT_fljKx1pX65zZY3tyRhrHjH1s9a9TXhFa2efqIhnvPXmLuOZZfTxQL7JF0CWmXJMyy_t66vlVSmyUjAeRyge-u_CG_l9pZ1Xg5KYVEJuOVDzbqtnFE418KYm14pj45rSA9rksYU8aDicKgvBh_FHXeuGSzFvHB_hrcBYvBRXCGVV9bsVPbSIAQa7G744LOpKCqM8i30iN8vrLjcAQuQhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=q8dkxR_bgZ4Ao6Tra_6Nk7UPZmmNJY0Xos2EosmsXsIhOwjQI-zO-cVw0YOWS25rxpeRaazCuT8_L4fUluoog4miIxiV2o0IGRMuYz3j79UUtzGiq9PWrKOJVTP2yybZa58j2HePfXqXaGkHw3lSAy5Sk9KESSTyh_BgbE2HrWXpCp1GvP_CewhoQbNar8YdwA2DDen4lGjsgT7olylAx9EzGySGJfVZFAvMHXpJ3DdUasS7stowIKT-EjH94yzRp5o7bh6Id3YYhqD64GaYqGcf4DAXsiqQE6x7J5I050RfLzoDL0ynkIttSZ-mX3DdLTIr2aPUpmB-uQtdIHXgSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=q8dkxR_bgZ4Ao6Tra_6Nk7UPZmmNJY0Xos2EosmsXsIhOwjQI-zO-cVw0YOWS25rxpeRaazCuT8_L4fUluoog4miIxiV2o0IGRMuYz3j79UUtzGiq9PWrKOJVTP2yybZa58j2HePfXqXaGkHw3lSAy5Sk9KESSTyh_BgbE2HrWXpCp1GvP_CewhoQbNar8YdwA2DDen4lGjsgT7olylAx9EzGySGJfVZFAvMHXpJ3DdUasS7stowIKT-EjH94yzRp5o7bh6Id3YYhqD64GaYqGcf4DAXsiqQE6x7J5I050RfLzoDL0ynkIttSZ-mX3DdLTIr2aPUpmB-uQtdIHXgSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0NmFOZiSrydV7hTohSSuddsry02JUQ_oaIeUMGZRSVTEZ_Y2e0IKiLYs5Ket6IDCM_MLW4Oy3D8MMOZ5k68JRxUPfThDzQHWqsBgiLRxRkVOonPqhnY15kJmZkDTu4AEicnhAJKDqULGeDah0vzB5iz0u0P1a0ySEiHfV-FFK8r5vRb1oEAvsQr0F_eVpn8Ska8_PQElFGGrsJ62WmpIOuO3PzkJGmyNtaiyP2YIdY3cxo2D4bKoyZYeTOG7WU5sOd5CaxQv172gpXG8jZieCmrcKbtAxWj53dJ1vbhM6pcVP_v97va8kDXfercOewdSbxkv41vlV90dsA_xPn8pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKAon3g-DHrvamiSd3ef6VOaMGBE7RzYb2-sf8WRk-VBaPulf1lAfLXESQ7ChdM_u9tjrkG7r17BCAMXO4c3rJN5BGHWbGSqAdEmy_qtd0mLKn5pqLnfzdE-d3l3FuE5b_tZUuJTM4I-gONwpqXhQX2gGDWGk7SWvs4t-8nBKLYgKPgsvvq9cbY-nO7m5EBlLOfnnHjYqlXv1cneQRfvh-BJJ2DSNVjwtDWtnI4jA7tZ5xaElbqOHQ0G4aR7cQyA25Ides6lnoFB_DSz3ob8ADPLebSzVvNwX8uU89SPNAok1AaIa5vAAgdySDqw6VkNXe3dHvEYMwgqeQ1EPbxiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیگه بازنده مطلق نباش
🅰️
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
💵
با بت اینجا همیشه به سمت سود حرکت کن
🔼
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r3
@betinjabet</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/24190" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4qhH_c9isDA3S3sC5KYn48NN3H3UxM8mC9UUbm2cXSrfcHM5nwURyvTlGupv88LCROYI2OWBNVFGpnyLU3R8uO0xnPWmW0OsvLaJeUa2tvkNRzu56yF1tETbF_gq9p1ZpUwGP1vV7XvWaw3hbPrqGwr4n8abzK6rcUXuFVxIQ4PyFfjFgrwF92LqcaFTbP4RTrQDbTMtQfWCOWYD0-k5Ov0FPxY20xIZM2oZ2xPstj1RZXIy1OzfrlJpvuegP4xJIrG5fJZt2-TkOjVOU9Ooqr8EeqioMd0TTrYzDTepSXUfdWr8EdOLFlNTCtKIcFm-PpbiM7-80GTk4rqIKt_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3HPLn_hpqwuL3Itwr10TvM98oMXDCQHx6IRBDykTFP6w8ubFGWajNtwxkWmv8JbWVHM46MdtK0KwyKmQuWVI60PdzEyAwF3aPQhH0BpybXe8QXk2AOEp-TqsE6wNJqLMZT-5gLGktQqVhrJe7irLgPDDtE1RgCOOjlDT-JoULJwsUB5ch00h6UjzskKMiiV3vraCQexGj8oetinPh0g_UtioK_uvJtm81yeQp4J3Z0-00M_-p0Tni_tRcXUqGV2LnqZxu-HYjw2zAFP6ivJVooLgFT5-v8CZmJpus3ZEYiU5QGOJS7ph5fZ_XDN29rsaTi3MZRyvqeTFZAQycMqJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWHGJ7PvamBRkR3wwO_tSP9ptfgzuI3DrkvRuOufGTzbNK7DMp3a-23cwz1NnBGp5uEe7ZC5nU_MXe-EnrZlhSgEdkDIp797y-WWh0lqjGH5qYiZIEAF3tIMcWFQtCRgv-K2jOQ3xl8d53DmFZtvBuPsXlfDF0taJPEM5R2ORE65kkpf7Ov_FWHpJ0A_5Su3_XK120QXiKFFfpNEeapLrd1C_gUj6YnXCUwqRi2VXpN0eurCNdpvWtxTeu_DNRwdQEdjEwYWG5DQfpQPBRb5LOOSPLyv4qW6oQlfEzVW7UM-usjBMk1KL-KgGM34S7_CtoM_yefzFA6sjpGqJSwI3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4zW9PfV-jYteoMF5BfNaeCnemWoIl7u2JeshVUCTARLMyEqMOTd1LQDshipSdIYifq8GbR0IrCXTHb12NNjufvxPFUt9B331JTTge4F5L9f_T-cqwdqZNoVjBdfbdkRdJ5zUus3QoVPpziblNw9XvpXIzH9TlQLJy1OxwBHw6lF8e9RO4kTdscWRX2yAyFcT2UX5797N38LBBnlY-maNoh7iAgfqaxzCp3cyrN7GNAGHB9V80PIV0pk0oq9wDazVTttKLhjAPP196W7PFK-D0GwLG2dHRIp0TC3E_yE1eZKs8I6MMNHoBbJey8NqG9P7EdWv-9eDYlbFFpkCVL3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcFvjUT2oRZrsqY1iafh2ZImMaqrN2hqN-ngP5-WCDDNaU1E4BX4x8Xk6xXe2nBr3_MFQU1iHJDnD9Vvd55N30c4JP_yl8U5LsYXtvUHYYrXcwPMjMzDo_p57JcK7odOva45d9Tl_gp9YyjorVr0R7WPemF9tx-8q1B71JqVIbo-Iv8Fcz3AAx_kJFFa9d2XNTPf9i6C2JmUk9r7941GxJwvTnAzAhL1IJH6fiHjfIK6aOzmnAHBNl3K0ztYWCwNlWusAj6npY2byX-ktV_Mkw5eWQ0-eJK1GLaBLU97FjVrb2KozTxVruQM9lXE_Q8a17KdKnxuhTZDu6saYAJH7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbolZ361MBH1b6DAzRLA5rF9iLpFa3c9X68FNypdzJ2eiFlueQGJGHwIVj_oqb41QtzO9yQ-DBfGjUZjXtdyjezYDOPIfafxmUTIrUZZX9CYJ5roqlU9vCixZQLtSxWGnuvh_wDsnRC3yjpO9Dy3reqWF870t4UAxtQ25v7-gd8Hblyv1j58gwqKesdKf4bZeK9OMQJfzp03ntrJol2NZMT21eT7nqMzAHXuq8M2O8wjRguCppf8Dk1Kk-XU4S2VHYtUllw3i3NBDp2CSamSm8f6kFGHb69YG5wzzWqySq8clfft5TgudoWoPRctESoLL9k0h4iQ3BQ44Puj0zcjIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_DXFhZ_L2vAzRl5Zx_fqgWS8UfzC8srqCKbVZMW1s5xdJyFXg-J7IoGZEaywcYRaJPZjEutlxOAnyhU01RCsvRtvMzRY-fR5MV4xP6N2kRb4LaLbwyfOwLTDEhmJHU2cEGNgE7RNEEyR15yx84aBQNGr25nY8J2Juhv3Wgq6yChBcY6xUhhW0QUnQxc5wKfTp79ULYNbLm9ylM2sS_MBd4gum-ah_3Yl044rme5XyIzb--JLK3CnAJlptIWNpwnC9GMAjNOtrbR326L9ScJqkwTGwcfqLVWaEC32CeV5Xf_t0ked7OL-TboZ7tVmDSRp8cIu8f-krSqFPI4NCQUBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etCsxrVPtEoxZp05Ov_WSfru_XPKRdgW5uDfHMNu1ulZ_Jz4PCPzOgL9VV3mDGStjuYYXqQxKc9m219kdoGJayEGrKoV4KyOI7dAqBNdRjxkILXTs_fxC5Yprjg-hCveb2_6B3cX9B24Hm_-2yczrFhvYAslo3DAESndGA96IsgnyhnCwu5WgdsO5wK_sUy5N3kii2TGGhedJHA2Hp6MSm3JsZ1ia8FPf0YivXeAeIyKaOL6-k5Q5l_VdTW0ae3ZpnbFqPB3nXZAAIsAGE903g_0jLqb2d-7x7qssHA8AVRDk3HKx23vhOuMjUDYhHM0m7KRp4PJNaU3vYj8oJIFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbXXZ4faOHPaUbt-O8d9HJrjg1Rex7dQyD0ppySOj4IhcvT63IsOCgixixJlTUaHchCwEaTKJRV5s3G4Cub7tSCeffrDPqoYp6-Pmn-9QUadUfRU_niH7g4u8NThys_y8U8nimi0k0E8fMUBthgdj5iTbiy-LCwrMH0Vd9KFmc4I06xOez75TxrTcx1ysStQUcJ5QPHqOzJLzIX9mZ0_-y1jF-wkJ6UJaxyQXyV9leSfKaZcm8kRnKhv4z1s7oCqsPssP7HGQy-LOVY48SRYUlwXmrhCouZN9BbhSGmApAjunfClaJO5YJMqjABFv68XKtaal80wgTsYH8S2cvdCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQ5s3Ee7FlT1QS2ynixlefLBnGrh29avHmcY74zhONaIi8qFncoF7Q3LNl9ptYY06pEgwrdFEOclbYJI0NP7rpKm3WgiP66D-VPxPpxMEmMJinwgsw3XMinHgBOWgM5wFmu25Hx0sqhdagfZA1o74TLH4R0iTGpasD96wbjc2M3vyASokzVBczpLCcYZFK2exaI-Ajr__jFPAQ-EEO1tOxEJq3rSw8aMHYrU0FCqIP_GvjeoP0T-JUFLcOjkfGvMBgGKAqqhjWoWODPezN6WrRdQYl92dxU_AABwk403n9iFlVicoqbTH4GuIEkRdLkpJ6Xf9bZnpGmENNE4zYiEPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQbtP70EMDMGDEBPPRMYBP5t9qsUs1fSYcRT3IGPBHHU7BfraAqXxIDwA4b8GyNXoN4ZAgeBxqFrFHDF7ImQKRKixjn1T-W1h83EhDbCoDcXsnF6nB4i3kqYWxFyMchA9wddPWO469pQP7VkPtHAhfIIKPAKZmcT9oO62ch1FlO6-dUQ37jdtGzHlgEFIx69fKr_36hiP8yU1kZVRTvcmxUGdPgTS0PVvkuG7WfpMmCKOk42cmrIUtxNgkomtaMxPRYfb1MuW0YQ7ELXeqD7oZMN-I5GloAGXs5kPa-5Ca1gQ1l4cGdBZESYuCFSEN1bCsCbU4lvAhcYNIsG8a8NPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=YdtuwokwjEuBX5q9QCUP84bhlZz8LCXhLe4lY8LDHHettcNYtSBSdh4qTjDahnenmk-AvBNj5xNK4Rhu6grMPQiNvhtsW5vhxCOIpPrM_P0OoteIUSXitck5cucG9-419ncxy4_zcr4SANo8tYbd9lQVY_CYSWQP2TxW3bYjorFKxZpLKgCOVLQTdlxQarg_sy5D0riqEkfrtiVTgPkm2h69QVk9tEG3HILZG5w-4hTGBwtTWbCRnHIy7uVeHlk3suJ6pYNyvYpMRppJPj4OAn0qHcqoP_QuOklvODKJeNFUxef1nfequZKPY-ZG0_Z-XzLaG5TTQ-VZoygc2xWENw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=YdtuwokwjEuBX5q9QCUP84bhlZz8LCXhLe4lY8LDHHettcNYtSBSdh4qTjDahnenmk-AvBNj5xNK4Rhu6grMPQiNvhtsW5vhxCOIpPrM_P0OoteIUSXitck5cucG9-419ncxy4_zcr4SANo8tYbd9lQVY_CYSWQP2TxW3bYjorFKxZpLKgCOVLQTdlxQarg_sy5D0riqEkfrtiVTgPkm2h69QVk9tEG3HILZG5w-4hTGBwtTWbCRnHIy7uVeHlk3suJ6pYNyvYpMRppJPj4OAn0qHcqoP_QuOklvODKJeNFUxef1nfequZKPY-ZG0_Z-XzLaG5TTQ-VZoygc2xWENw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VExjrpScyXxsch_Ys7pqdUJe4od6LrpompRPbFrW_I7yIto_qEN5YwhmtNW37WANKRDxklXC16SqJelPrL1aTSQD0LKefL9c6EcVA48_PsMCR-dTQ_fBMqCAUxYSlSah0c4zM5gw_XszNT497bqJvTyI5n3UO8k5TlsmbS6QsFQZsyQ-_G0A9tF3UUXiVpLx_j4xBQOAan8pumVkDR2AMbyXxiuwNZmJhz_5or5gDleaffMmDLX2RafLRzY0CoChN6DJQoTJS5t9wH6_HjCE-tfA-bwzS-vcLvhHOmtlwHWYUrkZnQkOcYpr7K8MIZuO6yCLjt8FFFJu_LE54RXmDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=AV04Lej3zAMel2PJ7B5mEoLsLUuO57R6dkW0pERpGDy9LeOzJaxZRBCcsQS6vRPWW_HBmg0Mtu6r1gMw95qjgeAMOWT-uMjaMeqoHCsnINRz9z__-9zd1KxK2aN15p5Ax_JtthGzVa92ACmEcVXI16TeJSMwNmGqNdJg3hwV-5cEHStyNPlSjGFquCONtidgCzNfj1T1OxzoKzJEeWXTl1xVDcuqK5X2-grbQjsts8fkijzE6CFMrAkvovbN8bJD-wwmGmBc2ZRH5xv9coS2RFfyEnrccStzpvI2l27VL8IeRIFCpNclhYSYAV1mYzx8ntew7Wtz1P2mLQgAl9yzzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=AV04Lej3zAMel2PJ7B5mEoLsLUuO57R6dkW0pERpGDy9LeOzJaxZRBCcsQS6vRPWW_HBmg0Mtu6r1gMw95qjgeAMOWT-uMjaMeqoHCsnINRz9z__-9zd1KxK2aN15p5Ax_JtthGzVa92ACmEcVXI16TeJSMwNmGqNdJg3hwV-5cEHStyNPlSjGFquCONtidgCzNfj1T1OxzoKzJEeWXTl1xVDcuqK5X2-grbQjsts8fkijzE6CFMrAkvovbN8bJD-wwmGmBc2ZRH5xv9coS2RFfyEnrccStzpvI2l27VL8IeRIFCpNclhYSYAV1mYzx8ntew7Wtz1P2mLQgAl9yzzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhubivvHPD8d7KQ3zSXw1FtJouXneyAgvbfPw8wXYLzn2oWD283CBbKJXPgk-sc5EIvgrR_O2dnMv57W_CbJUqnka9nbDhT4-4MNMsvLleplj_0GUin9A1s7y60ZaYiso203MwpZrRchXDr4rnX9e8tnkpSlX3GQqchi5PKF7OOWwz7rJJ-x-pKzNaSXBMxHI-vqoC14c3lEM5nx0IpE74OmUSj-MrxgNdlr18CLuWtZRGonxEn6sLJkrVnqZW7auXyvC41Gy7YxhTDmUzr9-X-Leta3qTF26gbQIsDX6fwbdbIgY8VpZ3I7iHOEdXNuu9AaX6AGXSNpqS38kba5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=Z3UONfqtC_lbqQs3_H4DU-zinoJl07PZy2i-tDNWmqjTNyQGHglkvR5IEJ9rSoVpn0dtjJ3hR465OclzQIqSlCwqmjtSNSeD_8HDHH2Ko3s7ZQGEsD-WZYrl3Qamb5EoC2yBDNSFdGUEaM5FEjEHacBuuOcnPw-l8KCFFMdaR_o0UzzMk0Z18YIDC4d1dJEUh4raqlYrvzg3Sw0PML5tsX1_Md0OaYPUlAIdVUCVeMyvMhtTj4MWGyaRO0Cx8OkKMrGohV32kCaDMycm4frjB25ZGH-E14Dl1qezvNY-AqOK5UUTy3WTWhl8pYYeYi1B2omYpmjPnSSEIEPMnB_C7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=Z3UONfqtC_lbqQs3_H4DU-zinoJl07PZy2i-tDNWmqjTNyQGHglkvR5IEJ9rSoVpn0dtjJ3hR465OclzQIqSlCwqmjtSNSeD_8HDHH2Ko3s7ZQGEsD-WZYrl3Qamb5EoC2yBDNSFdGUEaM5FEjEHacBuuOcnPw-l8KCFFMdaR_o0UzzMk0Z18YIDC4d1dJEUh4raqlYrvzg3Sw0PML5tsX1_Md0OaYPUlAIdVUCVeMyvMhtTj4MWGyaRO0Cx8OkKMrGohV32kCaDMycm4frjB25ZGH-E14Dl1qezvNY-AqOK5UUTy3WTWhl8pYYeYi1B2omYpmjPnSSEIEPMnB_C7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlMIOJlw_iShtuWZ79GtAT_N28fkQm0ROkVh92OISlfVGBSXHWZtQc-8ZzOjL20RgyRrOYDqrP3xeNOyHZC0gHpsiEDbpF5-gxF3E0V1QaH-WtMv4WjqNXExmBgjSb1_hgGx4ffQbzO_22VmknPdouRL-CfE2zNmG6luI2O8jfakT_EQVMzpA9et5BLj4a-c79IoAyyubf3vfZzj4nk6c67cRlsr3RcrVs8hz3EoPWuQq3fJKxv_uUZQJEMxC9JjEz3k0HyCFftHFQovmSooFLetAOSlduYn2zOaFE0YSbPdDQtLxUUfUbSJLOhTLAJh3tgUOJZJ0c06uAEYOErTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvka6f4DXFDcRzmC1Z20-6O1WDmcJt6CoobaMnEvz8cSLTXWJJRnzQFcuHcnjzycJbDOBaDP7A7FtE2juz1xB0ZTE7TbmY2AXg0UQjPlvYJBRkPMMhVp9aHnYm-lukdIvk0Mp-dVFEVlA3P9pMMY5VccTgb2VYIpZ0uR-fbbTaIR3qRI7TF8tbqq2fri3doyueNQzAsgAjxmIHlqhwoWjM1na9ixCaORzW_egEm7XAqgIx-NplkKnnM7rA0KmdpOuogd0zSLDWGbBRoCoRl_0MMyfDKLrB9K2MLQkzZZfuvt4p5JXi9AGmqixmiB01ccIGMo_RiVDFoqwnskdp9Xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=k86NUmQM1pCnjRfaVppeeNqcpDq83uNEIDgx8ndz3rEImNCUqeZaQrrjdVscZQ-KbluSOnj6Fq03ZGZfM4XhgpFslPzKnHef7w18AWXrYBnpskzJ88wa3VfwwxkUFGGH9WxSL5BykJnZYxsEbsy8EPxuWiqRAzqcyIBCVoNZU_Zqv1q9aPEt_3K9TSdaSvH_RbGjvMvk8Kwd_HlBEaWUFlXXYmu_aboBMjgUe0lKgAhiBqEYImRZVMwneWdup6aEPMC01syUuJLSRd0224lVn0gWCk21THee4XN2gX15yrkXr2CDf7Ciaju5F3330yd9LB8x9GE4NMWt8QnfVFIacA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=k86NUmQM1pCnjRfaVppeeNqcpDq83uNEIDgx8ndz3rEImNCUqeZaQrrjdVscZQ-KbluSOnj6Fq03ZGZfM4XhgpFslPzKnHef7w18AWXrYBnpskzJ88wa3VfwwxkUFGGH9WxSL5BykJnZYxsEbsy8EPxuWiqRAzqcyIBCVoNZU_Zqv1q9aPEt_3K9TSdaSvH_RbGjvMvk8Kwd_HlBEaWUFlXXYmu_aboBMjgUe0lKgAhiBqEYImRZVMwneWdup6aEPMC01syUuJLSRd0224lVn0gWCk21THee4XN2gX15yrkXr2CDf7Ciaju5F3330yd9LB8x9GE4NMWt8QnfVFIacA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCC9IsH43aovl3hKkIkO6Di6eQe-OwqPjTp-iiSuwp4ILU5otaokPyVvSUKqUJ96-Mz2LmVy8eTT9EE9RhtWM2pbaiJsrvsuYU33TBGYg4ZoodLPpOytGO4D0wsVxDsNszvH9mQ_ZDwFIKZwzd2qyFF9hsAag9Xot0ZU_9QE4qBa2yAF6S6I-gBv2MxlENo7pSDXaiVPowj_pec4LBJMbSWiqjdiVuR9fFNs1o8RsK4Y5mQIIhN-Ua1W9CNZ9PmiPmQKyEmWYWiGRrosIZQwR21SgIuHrNzVosBO6MkgqaIXLH3y7scOy09XxAts04IXeMIrsswHa9kPO7HjOwWx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=kMvYeoACreEBMoMX5tKnjPoLiS8YEUJnJFyjQSw4KgT5CiElyHp7ETsZ6Yzqo7Tr4vPXk94Y9cV3YwRwnx23q557ZymQeUKxPAyLFJslG5CuKBQpE7_-4fZtrKcXwwF4EzBiZYH5PMhC5HmaNAPCEG53sRPEqIh2pI4qWX1VZnnw0FJARCYphOgtosrMQ-gMKd7yXwA0tVjKgIpHY6mhNfeQGqXx4-QxPAickmy0HdcXGntnGz6MGWgfM3jdS6Tw5i9fEkTY377xTk9VVypc60yjUrRLiD-tUWphQjBS27gvFat9wkr4HYsLj5WX-9KIwtE6kKgIgP4yX7FVRQDxvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=kMvYeoACreEBMoMX5tKnjPoLiS8YEUJnJFyjQSw4KgT5CiElyHp7ETsZ6Yzqo7Tr4vPXk94Y9cV3YwRwnx23q557ZymQeUKxPAyLFJslG5CuKBQpE7_-4fZtrKcXwwF4EzBiZYH5PMhC5HmaNAPCEG53sRPEqIh2pI4qWX1VZnnw0FJARCYphOgtosrMQ-gMKd7yXwA0tVjKgIpHY6mhNfeQGqXx4-QxPAickmy0HdcXGntnGz6MGWgfM3jdS6Tw5i9fEkTY377xTk9VVypc60yjUrRLiD-tUWphQjBS27gvFat9wkr4HYsLj5WX-9KIwtE6kKgIgP4yX7FVRQDxvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4DDaN1wdOiA-Kiu4GQv6nJ4d8OuowsIpduPgmvIpfXf7uUa8sJpf_Y0QWzBtnP2xgYZKHOUg8hmIAyF1X0SeWlbBXRCFwx1CKAX_RSDOtOZW0ifo-FhM3pdzGG_9MWCGmoDYp4COb5qfwPScUMk5_b6aqQeJ2EwfJf67nmuxg3BmVbNBtYByQclupNqx2toz9ZjWBTc-XuV5yknVcQhjlUAhGvXfTLTG6603wwdaX8adjmcdSK--YTDmWWgluBueobrGVyfosxsfmsqX5MCohSFgk2jPfCVzydkJWNGiAcphmunmvJbbmIv7YEG0FsKW8bj435H0zOjfFUCJCs6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n82cztz6hIYoNbzKUug6-XTMBOh5HhTj3aRgvhKYUzaXizHy4PsIIStO3zdbqO52rKhGR2RmvmivyMAYQI7pbQLx6nSCqsD-b-ZQuK-JOvhuZvA02iSgX503o5EDPOJO2AJ78DcNLVvHUu1z9nE1ZRvQ1Z-uwrbLpL8HQgmfR33etUU-4kW1lhIPdzpfEF2m88SvhCV1m19IjQyfWgJEPRLfD0T5r9Hgi-tDpudkFZk9EVjJJn8zZ02foouR2g3PgVcU3S2Wos8s82J_-w1EjIclMKZZhXBjY6kryDG-dPXVGllERllja0IviBcuDs6B6kosuPbNr0d2IZ9bGK4kyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0VMIjUbsLIOIQZpE-Ei-MJLIrwHUCeRp5vmfP_IHyQrSbPEJq-FhzjaY168Z092iTI_GxCqbgWDWTrZxijvSDBltCak_6t7z0JA6geJFjCpNBk-_lGAEkOteWgEYvi7VZyGL0S6ylWzONaPJmVd8X_2Smc2DRjwO22xGj0_bztHD3i85Q3pC0M9mI-S4WQCJy3qs4ELfeD4JojJSxbRhlNF1Xqux-A_YswfUuH10EhD8YU-7tR29inuBzwikA_YG8hyGKL3BhVzORv71zFxGBB8kBEcIrSH9LZeJEN75-BapEcW9dObju5KCXsyz2fzBVC2UbPJL5nveR63kNJ-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0vTT38nWE3HS_vwa2AGrKhwScKtKAHD0hfZdP4-TPFt64kw4_PSjNXcWGLonWgeLO_Yw1QmEjaBypRqNQbO-I7iBDk4uqus-6BeCh8jQ-Y9yMIuIyC6HqZhH3Dfn8ob6GF6mYsOWzKTSQChTmkZjucujFe-Iqnd-IQlxkzYijx3NH-j1Sm0ZUxsUJZ5ZUhJwuNWkALCOQpD4_1moXBdNrG-Ov0Sz_hhTxO_w2kDQJF1tGDVPzuKp4T_sKjraV0VNOvS3ic7tIw4_p9bCxozJYawDlTyyP34M6uOzzB2L9Bu0Mpin-T2pMAomCo3-b2DWMGHZFdruJjI5_r_LEi7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLvMtv0XJfT7qGVAUToqrGnyIwJFEqEHmXWSVgi3xNbyPWxYCt9JBynRXYpf2By669aiuPC2czcYX_YclOQ1nvNDNzDWq8V7ViHLyN68cw0Y4cr_UlT7JieMmYvz8dOE2mh_qJsX51De5OErmU-KIw0TAaMh7aaqKaQi4W6LlWpGNKk3WsRQVF4XLHvxQQ0HzaVzplpISLigIofP5S2_QJ4REJy5QmNoJu5i2kYbVkKr0iRk5dFd0HZFjeTwLvQ4ydnm5yIkgML6TEkBHymNvJ4m49hCC5VNz5o1iNJYMBSxfHOOgZLs34SDr33Izk6PfKxTDitjgWWdxWxe2C9s_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3ymBIq3ldW4-Day_2T7d0ZmlKYcYfDHutY-hLDSRXwc3rvGkcAd5OdaZaron5XDWZDAfU-Ywi9x9DpkZjGIqIscpMHjGeGfNDwf2C0_J9HCqqzHi9PKgdFi2kHMupAFlrlQmDykA9emBUmdgZ13WHkelQDjcmdT-gT_btAU7W3dEqqpsopk3TrQIseiDjzxtuelItW3IUm3EKJCy7apr0pPEGi0gNHDiHaCpeOehAn8trTcRtZqVxtYk0_kpCLzC_s7rFs1jwtXAeQ5vPF82Rzzo4GiC1fJZRRHE_8uinLbWTptg3pEOoBvZNwbhxc_iN8P8iEq2An_Kf-51muL4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJ6WVpmsWOWlDrHyR6QU-IY4o33zbuU9jLjxrotdQqV47l-ot4qr_ndixvSCZNpp4_FS2u2HqVpXeVVYXAWxhIy1NDc17Qx-0QEXKDV9zjf31fMniFFS4ON3M9uaSWVec9zy9y6n4ruDbL5Avi7rqUFKUF3xsdoMYDYKZIi_EK5BnyvjUMnrsCB2xFI6Noslq4rtUkcJ1E0sNtsl5KC0MKHnfhF3oHKtZLu_bmH5NxdMArPsbQE75V7ICAfUEhmlZbi-Q8ETb_EW710x5n-QSsk-90E1Tq6eQGzaL9wkBUh9H1GcDalPHGo4j6ml3nkt5I7hcGjqQVnb2-6a2unFfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPaEgbEUMKWJasFJDscOcCLKqBW13iL2Tybgp6ixaI1Nqond6D42cLT-GkWeFItUqEXnQetFpluee_1McgEYuGRGcCi4b1PiK-jV4M8xaW6fETtfZk_j0MfRYI5heMiRhvrMFyMYxgHPXcQTQA7HeEOOpKAb2F9JyJRcOvpliikb07iVKc3gs_5zbQC_KIfsGTANzfw_zXYJPlD6o1Gvve5TZaa_isk7iLDxzcnK5tJ9Vc0I3XlLla539ovz1m6Ry3Kdnpd5IvPmi-h_Ttu5KzgGY1JJham3gAIzQW9FP2rUziNfKfMdxY-h04TKy89Qt1H1jC5tFSdGymN3Qm7Hjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=nPUAM2BSECzvCvrozkCs8RWHdhui6iCBd2m6Ww1s3rEH1ndOY5NdL02Tv-t4R3LT-2OobFLx4gpSxzUKfyy0_4QKxipsW12Q7Nsx5LmhAsQBoExxDk1QEbk6Ma1QnbvBDTO1cmzzhzFpKu0Y5MJgR4-8VTwV8nH6eksCV88OOZQJ-2tF9SrLA6V6TMv5WxH442zqn_ZbIEFmncn6ey9KY4_BmU3tUAcYgA0aDhPjtDh4KHJydym9PyV0bsfZ8En1PraniCja1YxHgPrZCY7AqYLHFKGPjnGBvXI4xen48gg_aspc_WksrvkS92hq7VEzI1WE_2HDttxnm-MYM3I_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=nPUAM2BSECzvCvrozkCs8RWHdhui6iCBd2m6Ww1s3rEH1ndOY5NdL02Tv-t4R3LT-2OobFLx4gpSxzUKfyy0_4QKxipsW12Q7Nsx5LmhAsQBoExxDk1QEbk6Ma1QnbvBDTO1cmzzhzFpKu0Y5MJgR4-8VTwV8nH6eksCV88OOZQJ-2tF9SrLA6V6TMv5WxH442zqn_ZbIEFmncn6ey9KY4_BmU3tUAcYgA0aDhPjtDh4KHJydym9PyV0bsfZ8En1PraniCja1YxHgPrZCY7AqYLHFKGPjnGBvXI4xen48gg_aspc_WksrvkS92hq7VEzI1WE_2HDttxnm-MYM3I_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-mFc55tcI1x41yjHu0ePCv8OSHJ-FiPCHQkc4Ujh8HzNwpAJnWDpvaxmsitz6a9W-xgfOsv3BSKYnIPAMNl4BZ6cEzssCyqjj6F0AqgtOxZb3_U_T8EicsQPS2YGmxNkd6WxT5rzY5qhveSLCkh5Ge3ab9IWnopb4SkV6lkRc2gOds13YKKB0FWknFTWZx9h8BX4ZkqZXH5rFtdRaxSf2rnLG0Ja_XwYiFMtI7t9L9ubSpYK3WE7t-zQ2C3I-RLQldYGbmjH8X7CEwhmWF0B9ok3k642oB_IYboGsMP8qkKeM_sK8jqrCpWJOy-0aTI2WstmUpBbh_gdE_6WVsnJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=K1UfLX5OeWE5Hthx2aGp6mRBlgqS9EjVhJiMlUBtdeveR6Uo4YYnFJshP9zxDY9a2-bY9eME--0AVwMTPKs1q11zzvAcjZkCtHOGvBjGge4uVx3wDfKCH17BqsikWH8xDf1s5P_Nawv-Q2ix2E9kLHCk6KJLrx4u9we2XB613yFZWLMT1GgWL75SdL3XB3z4GwBAqM9FhBN2qOsV2757th79214_ZDg36m-GD1s3SCjV7nsmeYkHAkpLMXcGGKcBgyUjSYHc0aVAapHwgxyHvn1CnY4IbZVEx-Zmtu_k8FoYyjLfgmgVee9t8yepGKeQGHFWlrdw-T2qJ4_Fa7LQww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=K1UfLX5OeWE5Hthx2aGp6mRBlgqS9EjVhJiMlUBtdeveR6Uo4YYnFJshP9zxDY9a2-bY9eME--0AVwMTPKs1q11zzvAcjZkCtHOGvBjGge4uVx3wDfKCH17BqsikWH8xDf1s5P_Nawv-Q2ix2E9kLHCk6KJLrx4u9we2XB613yFZWLMT1GgWL75SdL3XB3z4GwBAqM9FhBN2qOsV2757th79214_ZDg36m-GD1s3SCjV7nsmeYkHAkpLMXcGGKcBgyUjSYHc0aVAapHwgxyHvn1CnY4IbZVEx-Zmtu_k8FoYyjLfgmgVee9t8yepGKeQGHFWlrdw-T2qJ4_Fa7LQww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=mQTfgtwmeBBMxroQIPIHd87YeyezIZFRlFbblxUsXRAs8YFXIpBT4GjdynMdQosAN8tXnuuvRRbjHQdLOqLWt_G3yP5EwAEB1Vw7Ii6zBCee7_f5HDA4sRb_FkUESn5Ss81O9KiKX13ZmZBua6XmK-Idzwp44lTSCzFIaUQPqiCw7eSZmg_kQO0ghoquspS3dSokSgnOrLaGzj5Er1_vsYXzGyl8uNNk3AhuQMpV8SleJxe2f5KsuI_k1ybvtcGhhZoqfOIehJlt0mOcfgXd-xno7B1mWtze5hooVsizydDpjZ2ZIOS6Yh-tgtQz8Ew0XeKsS3CUwKEuhtUV0IEx8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=mQTfgtwmeBBMxroQIPIHd87YeyezIZFRlFbblxUsXRAs8YFXIpBT4GjdynMdQosAN8tXnuuvRRbjHQdLOqLWt_G3yP5EwAEB1Vw7Ii6zBCee7_f5HDA4sRb_FkUESn5Ss81O9KiKX13ZmZBua6XmK-Idzwp44lTSCzFIaUQPqiCw7eSZmg_kQO0ghoquspS3dSokSgnOrLaGzj5Er1_vsYXzGyl8uNNk3AhuQMpV8SleJxe2f5KsuI_k1ybvtcGhhZoqfOIehJlt0mOcfgXd-xno7B1mWtze5hooVsizydDpjZ2ZIOS6Yh-tgtQz8Ew0XeKsS3CUwKEuhtUV0IEx8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=jS-GdYfaFKyMWOsWuzfK013QnJytE1oVolIV0G6UlqtfUOHWvgPvZKnNT9znk72FoaMrQgy5FIHS74bP6EUhaIOaJvSEoNmVDNsPMMfFdV2oy0dkAXgJFvc3MqavGce_qAnQ2z5xW7ETOF95_AcErcXVGhBULsnnRWveWtr6k7Ud4F65PP8kO2LydCaRCYpRgA06xMfMay_PQrDOK2eoMlGVhSbdCnXmmULNYAH_Xy8hWP775J_NOv3DwVJwj8bVw-_-oXOG86XbSa3l25xXPdL4VM_hvJgwlcUem-qdzGNF0ZrgWFtuqVs7tuNzTmlVJMb8QF6RfSsfX-TnL4v2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=jS-GdYfaFKyMWOsWuzfK013QnJytE1oVolIV0G6UlqtfUOHWvgPvZKnNT9znk72FoaMrQgy5FIHS74bP6EUhaIOaJvSEoNmVDNsPMMfFdV2oy0dkAXgJFvc3MqavGce_qAnQ2z5xW7ETOF95_AcErcXVGhBULsnnRWveWtr6k7Ud4F65PP8kO2LydCaRCYpRgA06xMfMay_PQrDOK2eoMlGVhSbdCnXmmULNYAH_Xy8hWP775J_NOv3DwVJwj8bVw-_-oXOG86XbSa3l25xXPdL4VM_hvJgwlcUem-qdzGNF0ZrgWFtuqVs7tuNzTmlVJMb8QF6RfSsfX-TnL4v2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAtyQ0ukLnlMAyX-6kZp9GmUOLh0DgJFl7iRQ7rfT-pFcWGCHl4lmHzfRLCMr9KdBuApjDreKJLofzidHL9i6dM-usmwlSkLdBYjzvZbesIW5EZjHAQSeu15BzPjw97ole6NphxXlxY37wuj3AUjQ7ciaRuDlLa02H3AsfV-mO98lfKCaGJ_LeBLnvq9m68T-Sbp94Yj83p1TGd2pk6TvaKrlc4YUNJjFiUMsVAFOWl3QslnyPwI-_NAdhjx9cBwDtVFkWcfQKu6xBuK5QYdRQu_y68wSyMoLgecC2MmD11WjmwrVEPfboCuqkw6gIiUFaMxacnjy1KTY39aqKhTVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC9-cfLTQS-jWMhqY-CCGpkkgPFOQlHRlNftfqlC61-D510XYU3zMBZvqDDrXXNK79jLrivs2bfFVbcykYBvPE3fuRjDwUK5hWLn0w59hzZ2QXcX1jF2Ovf02lGbiKWp9yg0LRESoAE51MH-Fv38VyCn-D7ukXVrMYDNTNjd5e74uhQ05OZAlHCi_OCJxy0wEvoog-IqdxItcUXgIoLwt-z4ZqFwrlBHkyovVT7xH-ZJ57ZY7UWAjq2YLeo--158oknbIwrPuzZofkS-h1QS4Iq5U3VnsE0FYuG9uprjGGF0Ovl_yyTgWyhCeiU7tVl2eXgF1bEs6mV6pE3x_xZtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsOty5jz-v8FpmT-eJC2frW25ZojHefpE-R0UKZoYBuHLGNk4y8nmtxISzW7zE-gNxiUzorMSnTlgeW6bV67ZAmxaV4NjWZ0Hgt60ZH0suVPrezO0djj7yn6is-8XUFqWvp53LKccY1LRJX-40WFi17tbcc5rN8QeGmfsFajVRKMzQSE7rDuDJjOtYUYC9ZDr6N-m7Uz75d85jAVf0W0-7J7J27IX6eSzzq9P2Jap592iKIfMyKw3fOYfNguuRDjOOiGc45VCgJ_vQYZUo5vES8ePpeK9a-bGX4RT_ghEz8ZBDWjNwC8DV3d8tw0yHDGSn0hN3qZRO4wqxdmoGX7zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5T5-pJKT8d5mKuCrFIs3HCuK93Hz2w2j6ViDTFFzMLrSWevBAyT5G6cJmRNG0RAByjifHycfo-oU7AMEH7MKiVcoYXFf3QqJ3IMScgOKHm7ANqKk9zbb9Z-e2Iru7yJ-Lfffqr7FYlcmihjO7UFliI2Axvgirvicsqy7uOv5Osfgps1EwmUeX0ACerxxJsxB_SujOYmwlxF_KhbancXHV6UTl7rHU4gQptchzOcbrDTaU8DZDuKr7lVMsmyy1XMx_opwj3SyJiS-AlaUaFL2T5VDkgF1-KEsFPlALMQ7eg7fhvlfvp8m1YzASnDvCpl59-fq5AfaTJ_IZpj_lS5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/px-kjZZZTEueODWy-CqqRFh26CB0t6k27mAOnFSpSwz2fKK3V2iRkKAe1xEVIUvPT8iOYyOrHOMpOYFzTXiadbGpiskbZMen_F6TbuDCLVVHgoOew7HJNwHYRbu0UVReqz9XRGteM-OJlw9DQ6lma9ISa0jRYluLsrDVacy6PFJ48qXe2oqJhS1jVQuTIFSNDAMFYf9Ojdi0ax8mbG-oW43CTnd9g1Dkk74gsQMlyqaDdyrZzkjz7pVEf5ALJGjV3ZKn0h5aVfh8FTMGpEV8cpE6YrwCN_DcTlBwp7FaCHiC6Qivr-3fgAqe5YVOyxyWv2ddgIBdtYBk08oDkac0oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGkkHv-P42EKf_-1utHJg-o1UoqtytOqDW33YaaRIxXBO4TFvHhhv5D755Eoo9-_7z4pJK0OaYcRHK1uPQec2zm3xTbPFBM_jqeGOHEdn3N91Dlv_tX2pCW9kHB7-zK6OS3LCSnCAQjl40HurHl-S_z_kEPrJ1LH7XJOSCOMf7Bvx8QUUOMp8B6cRXrC7JVTvCNcU7olncussAzACuDaF2jTgr79-M7Wg89msbIn0L607wiMC_H6eopQi1O-6z6MGVtuoSx3McvupIh4mU5cZ0-V5RSmhsXcPHJfpKDftM2-XfFypTIjM2D716DsTb_N8g0fJRHSAmv6Hud6S9tPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=i5cel8OjPpHpaIezrs3ZV6a67xWufU0faOaQWgS53SBjMYwJAuiLNQqb7EFqDEMXu3Zc8QxCo8ctGIAA1nTKGfFWR6Ph9aVnYjZ0u7Qbrwz0ZPZ4uyJ_sr5cIihsLodbv1gOLmWf0M3tjV6Mwpruu3h7vOPwRtWZ7N60VKBE9uvIhHs4Ga6WviDwq3rTnDIl_em3ungeB6Y8y9QzEg-7G-rAqtfGOGAEM0GLiOY4KGNLDe4yPVUO6U8ZtcOMAXecQubyGRGF5ZXofFgzkvzTq03CYM-ca6Kxp3xTUbKuN9U4G59G92Vw55q_lOJ3XVZP6Rbw5Q0EYgCui5MdJmSDmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=i5cel8OjPpHpaIezrs3ZV6a67xWufU0faOaQWgS53SBjMYwJAuiLNQqb7EFqDEMXu3Zc8QxCo8ctGIAA1nTKGfFWR6Ph9aVnYjZ0u7Qbrwz0ZPZ4uyJ_sr5cIihsLodbv1gOLmWf0M3tjV6Mwpruu3h7vOPwRtWZ7N60VKBE9uvIhHs4Ga6WviDwq3rTnDIl_em3ungeB6Y8y9QzEg-7G-rAqtfGOGAEM0GLiOY4KGNLDe4yPVUO6U8ZtcOMAXecQubyGRGF5ZXofFgzkvzTq03CYM-ca6Kxp3xTUbKuN9U4G59G92Vw55q_lOJ3XVZP6Rbw5Q0EYgCui5MdJmSDmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kraCWNGTZoLDdu9-jD42o1kI-gYZSDJ8IKFqC1dBQ2mSDSNsOMbrSvRatSN9tJCME0SVushUTRUX-YXSPc7Q1Eo_sUN0oQ2HlxYbqae98PrCAWlx4DkZfMLHm7Xb9G2bU5Gjcq6hYgRIZWZdvhdCcb5Yxfr3li_6UFFkXwpDqqBIsYgwKb88tmhtY5CWltaJ0W4MV_qpvHsjWtv1oPo3KMkwSoRwB5asb3aa-BtNcVVR-_30YDhTkh5PkhpNnZ2vyXFQZ0f7LqwTJiTxTly73llK4BqJh5nLaPuETTdzdDdnODnWPrzPQsX1qSCkm5HieufbCQfmJ-xNUklF_AldVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH93_vx9_QpwSO9cv7r4Brqj-mJfh9Bjks-4vdwNPI9Ydz0LRmyjygsgsLHanLAgxcSe5GFpkwcSlayu0XAYZpCIBBFLud3Zqtx784pkPGNVMqw7Qqzg253AU2XrLtDcMpNJDlKCbXK9OdQwwln0KhwOH3A-HvL4KQ6EqXf_iWv2ifhxpqUtoETkdzWzMQ8K5NXD1E_yX9KeU3cTq2oyR8htKYqBVM74kuFRppZt5MVRMs5CVAAbjbJCWlNtCZBZ6SDPSpn5nzkmmms-3rpYGD9aJyymaoyQ6yHm1o9r9cHlED2cyYzHyh10VFfTsr9WnNtB-jB9h0AFgWyDZ5al7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8K8wF3LyGJQKN2uTQH-jEWa7jDVJxOHYXb_y18CZ7nMKs_KMgpvoL2hFh9HD8RReFvo46hOEGfcukODcNQ3WbXdVEH8jjaXdEJ8MNXS405fkIPkDQt-FlGG3R2lUcZbxLkG4eHjEx5i0X8IvwXZdTAnVEy6Y24kKBZqX4ZS2Q_HAP9SXxZz_1z00F8yLZSxQQYs8OicxFyFbHO27xncRCkkZPkJ0fAiNPjxVlJh1l_ctCnMICf1N1E0LlhyeRgOAV0NYx6T3tgBInJjUZs9aR2YjwEOzKE-vHEFI79aZqlU33m2uX3p-IXjjBhQmhgBpu1ry0HAoeUV1uORxzPXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRC8aCyG6uwQZgxBZ1i1jlvUSwdjzC-7zn8lCFsLO1SYF0rZUz6T62-If3r-1AcmZgeQOuTLLw_oKPqLvFW1bymxy0ILFlbpKQEKCKoGp9r_OrTHt6gMGj4e73y7CYWvHBTP6tVoIjgyTy7IOa8DFN68xq8EBUm6hvghPrXmUob2C9SJ-2ooFxD6xhvmXwyFQ6ClOjly52lq7eie0tFjpAXMxfSd3BHc0FjzNi25EH9mzUV10nEw1RAyQi5ovhouH1EXuX-Gv0Kt0ASLEt5oeB6yDcpIc8wgmUdBDfaFE_rUB2qf4p9rKI2ogKjkAt_MvhryiJEXFL9RC38dH4yL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvekQcQNcpnt3B0iMu2K0bq4UH-r7wySawekwVg3uwRaKPIHR9-vMuc6NyQlZqFDEZNo-uP0He24Pi4GTJHo7jt2A6Y_rK-OzKPIJ0hTpOIS66veTv0l9vgvRKbbnBNdYqLw7BMNHWl8D9q3D1PCKvc1y3wD1Dl3CHPZWg8WsvqcIKcpsgXK2tjBRW0XnQNFb8rGcAoOkad6u0ZAIoknc8psRHbHer0eMnxcBBrEzLceR1pFn10f3dH72NoiEYmL0HCeoosWynbtvUXYofyQm9IeOgnyVhguKNwp9uZbPxURbrFxeybs4LE-rWoMPalnLSc_vCBfQ8_ilxGtHQH1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDUKE0_zGTFLVf-st8H7LQawSME0v40Kycw2qF_19-e_0dVQUdWqNhjKV-eLklg2IMZVt_REewSHcOlbUj1TUhYSRk6jyMVDUAqWApiG8_bVDKr783f8lqeSyx2fC3UoQRqYV6erJljyLUmwmk8yPwHjaYxs8Du8Y6w954csGp9qUltycOrT-gtLaPDxr50wThY6VbrLbUbp0SZZXpV4FH21PNPabWBaUIeCrJ7JQRNRuaMahJ0aZNFY6T7JubD41Xs0UNIJJsatlbhp37PiFePJmSMc0Wju63ib8uanvpFwQlP-C_a1rNYX91133bzz_684VNwu310zkkPBro9K3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=UBoIDbjXxnDJ6kug6OxqrclgANNSMIY3rvIbc0bYyyFYSJJrHNT2FiMa30euWYKbN_eAW1HpsZ-tAIjjerSpbIo6rjmfsPnBSIKS8vOgUWOjMXPK8Uk4ayIPioev6y_982947os2k-1omWaWd3nQ-xcgq7In0P6uSZaC0XAA4rLfS1ZUGmN9b4O6Wn-vGy-IrXTt9HzMkyVE66HtC0PsWLxLFqiDPylOXnID5Wz_Cd7a5GgAuAdhOfUenx92kNkvIvctkJYNgmsyKYSN1_E4ma_nOYh8Ef4emn78RXpho65_m9cMZPKUKol6xRq0c6AX4VNg1DydLBJHFNQfSDP04g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=UBoIDbjXxnDJ6kug6OxqrclgANNSMIY3rvIbc0bYyyFYSJJrHNT2FiMa30euWYKbN_eAW1HpsZ-tAIjjerSpbIo6rjmfsPnBSIKS8vOgUWOjMXPK8Uk4ayIPioev6y_982947os2k-1omWaWd3nQ-xcgq7In0P6uSZaC0XAA4rLfS1ZUGmN9b4O6Wn-vGy-IrXTt9HzMkyVE66HtC0PsWLxLFqiDPylOXnID5Wz_Cd7a5GgAuAdhOfUenx92kNkvIvctkJYNgmsyKYSN1_E4ma_nOYh8Ef4emn78RXpho65_m9cMZPKUKol6xRq0c6AX4VNg1DydLBJHFNQfSDP04g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUJIiZwetcKImBhm-_u6f-Cp1727IinZJRvPkXuJueyVc7XAuqJKe8kdTrZ1wuRgulRSu_aMV0ro-VzOvmc4F5sMy3-ZAMdN7N2WBkKOU1B3iqcc0wb5yrWEHw4kgvnPcn5klvyVilLGXA2qWr_sIthrjhXSfrNy-JYaDBP_7JHYVLA7yGlMlgfNeEWXETOGy0v025g0dEqHxPc2QbAIx9U7zyfsYtZ5iLtVEkLklHgQBDHE8rIDKOpG1cYHB4THGoE1ezl3Gs-rFYhrW_Mdfum5w9bLdAUBniEm_rMj2PgwMbZKrazMGisWmsp_BdGgXVfkJsfw5eqvMRS6M6LWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc015dYBzOzigdeQPt756XealWlgYR914Q07BB4tN8O2dDveFmsNC2bcjnrTQqJegApxWwJebb3ITX7V0CT4VhfnQ16my3fviek9_7HVDkUCdraZZggnCkUoXBRNCbpOvtZAXI-9teZkPVzhvkT21kuHyNkJdbPGdiMOSlGiFhNmeb0k5HfFDFdMR6McTg0Koz0Gg81okvncmJE7nAYN_PDBQxLTjkI2ws95QqU9FEAVNr1gP7Zsp1swXgnFjClS9-M_Nt8UtDkV0kFqfFTYNP1m22uFnn9mNBnV6vUgXm7J5VeQffNSvVCgJrh3lUjEeIg8NHSNjQYYMMtJ489Fpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI0nsff5cI5_kIkaoiIwXcZ3HhJHA2yG1XGnSJ_oYr29Y2q_uSW1NOG7Hh2AByacN7ZErVZoCxwSjsqeYES3eH2gR_d5eYK3KSkh7agumrMYZ8rP93KtrmCigSspsu_UJ01SjM-3x-y2a8mQ69ftzxb-Le_qzXEVGOvO-Of5Ph2MLGtDypHRlh7IIkPQJEbi3fbhDaAZf4uDWAKPFpiolb4IB6o9wpilWbOEa2DM8Am30Tp6c3ye8i4eiZuuYwJZNTH19EX8xcp8WFI2clz9HDSLS8T8D7XSNsNQ6XYYOWfG4wx4uj3gr6kcrFOe37JvGjzt8jlPdOwpF_ooz2-Ksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=pSFyPtx3VRcNOthtIkrF_mk9HwWqV3drvEvS6WtboOR5t3sF7BpfWmgkaZhGaHt4O-pPyDWdOWo4eEHYUgPgsp_wrqWf1iFucvl7zsTbxtov8qJ7GdqzW18UZD_KnUT_V0ALx5HWfhZp-l5ag0te-elO__DRamG-SeO3Q3i660hi6CRRZlmTMwkE8eFh0EGeIHsvTHmUoo4ODgjN0eo7_qfKiX8xqWeTDeGNgewMaBxn-hmBrJ6PdlrMACjoHWYhaEjSD1itGDIZkX9uVJeuPNCmv2xEwA0l1LHOnNSy1AL_ud-u2qd0idR3s5eImYnf4gylSHkvijnHTj2BBIkNXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=pSFyPtx3VRcNOthtIkrF_mk9HwWqV3drvEvS6WtboOR5t3sF7BpfWmgkaZhGaHt4O-pPyDWdOWo4eEHYUgPgsp_wrqWf1iFucvl7zsTbxtov8qJ7GdqzW18UZD_KnUT_V0ALx5HWfhZp-l5ag0te-elO__DRamG-SeO3Q3i660hi6CRRZlmTMwkE8eFh0EGeIHsvTHmUoo4ODgjN0eo7_qfKiX8xqWeTDeGNgewMaBxn-hmBrJ6PdlrMACjoHWYhaEjSD1itGDIZkX9uVJeuPNCmv2xEwA0l1LHOnNSy1AL_ud-u2qd0idR3s5eImYnf4gylSHkvijnHTj2BBIkNXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSKleX8q38X1V068JBkS48EVBMYUtGZHulC-j3FA2wOXUkqQ8cUB0il68ihnifg93ArXFK_tS8B096aJRPieZvFlt7XTXAnpDegl9pE9mjaCET8K7iwSTlNYVUmsgeuNacFa44xKjBiAVcOQ-vnJCbIwMtaUKlYraP8hMPH6SyirezyB1RTmC38j_1R6hbVDWLAgLNenpRH5jZfjxnjdUCVPjliNu1sAFHyr1YfmKPux7Y3YEnQyJjvu7tpDWFV5Bq6eR1e_ekl9rP6Pi6g6EanHewrfC5s13QGAKKrckRYEzDrQ5UWGEI5viYaEJBhzQloVMIrukXLY40m3vkhtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6lbYjfESf5QApT1ZTajZki7wPXA6-Bqzgrt6khG62stdd9Azm5Ix02VV4MbIZYz2WHgQHYIupuV8BY919WLrAqcJsp2cPQQ_RO7HsGkdHt7xy4-ijGkWVjiPZQcMriLyXpTMCPVf7TtGfKThPWlohEqFj76U0OVneR7xEbAiPsbur58-q1kiTsjz-F0i5QsLlB0lHjVLE1eDvum4F_gPKrQzjsFD_auu9pr3Y_4L351idKkvfBExRdCSVyyiXSCqkI_MOf1WWxLXrAKhz4GDg--sOl4jBAwmNGp-RVVkLK818dcjQgs2oavAcj2VGrgAKyO3wrzAY3DFvfVGoU4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjoSYBtb1sJy8E-Z_DRy2gDeCJytDAKe2_sx3gOvbEhThtfSOAuWFQk0dAc5sfIlOZ6D9HsyN0p_UzSSiGGpdJx6XruuHQ3nZ3_mW6jYD-BVBFu-5QLuTb3a2W72KS7XsLFhHoHbJ7TOlbFuTWZXIB_TwZ_f7EX05Bu0VNNFDiAcA6N6UZOS3aNy1f8Pfgebj7GWmDsJzF7KCdv-5snWQPwOblHedoRYRB12pnWiG9H463XAAZIrOgYbTf_gnERE4APJTz_elX7LeyxMG4twMJV1j4kcpydzbLat1x3RUiALqRdOaQ7b_zc5jEdvKP6cjhZQOVr77mt6GSCxvBmVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHsmWxGL0qxMx-W4aujBz0yB4saFTGBkYeC7HHPT4F13elQbtXsBQMb_me3mVyLSJ6PHu8HH-FPAXgkQ0lJr0Gg6QVCU2ZoKdOeu2yE9F1AWZfiP-WlBG3fWuBbutf2az-GL6JB_znMiP-K_aMmQ6Kdg4ty7xOu7XCCRgEAMmXe80Prr9Rv6w_7qQuCmCfolW_6wt3fMoPJnO9AsVrpKXGL2EOh7CiebQTW5Dmh6TaXY6m9l9OWGEpHp2P6vzy9bAY1eUULr48y8awqj5dS8M9jG5OXqX2w6lURpj_2O6gZqYSrUtTTWXL1QRoAWQwLpuNIySTe9kzNNIiVBg5j1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24123" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5eAkRS2MEumekG12XaZVKpwJpBLnZbEtC0urMq4Ucl4_smq2ibMBMPH2Rv592ufXSDJao2p6hFxqBD7sRyh1tIpawJJhrVxs3C_FNRIOx_tzpd1AUDgHvBC3iCbhhyjhy9JZru3jvY04KfOJ7--J89rasm19mRlpm8hSfCT7wAOshqStaLg2hLHThNkk3SK217BqOBYuy6YnMgFzA6X99MuxDvZ7Icm8aTL7FKTxfBIvTgAtslfSI-v9gQdO019nYZ2x-_kvXDO8R-JJ9y9O8_pntfV5nbSqyzw62VyI1dX6TA5S0iLYNWT-xRwxCbkrAd4aptHjPQ4Piosoy2YYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سه گلزن برتر رقابت‌های جام جهانی 2026؛ ارلینگ‌هالند هم بانروژی‌ها داره غوغا میکنه. دو بازی چهار گل‌زده. اگه هالند درتیم بهتری حضور داشت که اسکوادش بهترمیبود و هردوره درجام‌جهانی حضور میداشت قطعا الان هالند رکورد کلوزه رو زده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24122" target="_blank">📅 11:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DC9n-6j7-QFeO1_Zl3LPtEEavgUcuJRtH8AGAUkj9h4pWCUqyfXtglm0f1XJDI5Xi5iIrKEuh32Wrs4tpw9yqXnebWahCgtWPGM9fQQ0qxCyTtep81BOI5eIy76lF5jFzCNbEUy3Q2cJCP9nZ01kDGLDahF3AjYQXPjiXeODVmLssoqbfrX3K7frVfxU1IKqEVrYU-k4y9q8ckQDl49kxrMsIvH0xPuZj4EZEPO1sG_UnhfY8AFslKQVQ48G4MCOs2uULzUIkKRqfVREoTzN8EPFrHBuXXM8R-urHs7yuXet7HBg0wsvLMldr5Tt3_uP6N9QzE5-GSjta9VL8J-TMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24121" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=n8uB0G-2dEQOPoZU8iDis7hdqrKI1iB74qeti0uVlhEBW0HpU689x_IcRt7AZxW5RtNbfZHwSPETRgLktCluv2XsuKbkIqDEsTjO74q5XiJO4tYH_O-myE62fiYU8gGZsCmEI8VlvUNxwknpEVZ84HbQ0qowLnWQgQfA-w5ey4WH-oUHUT2zWgUWb-svW7iGyPFNyoziXpFnKvhELYFQTZuQTqq3XKn3dEoDGPf7ei_LZQ3qTYfiSPMmflO4bvsgzu1caUkiqmEOOZH8l5lNLGNDy-hSHN7PPI2g5O377-hbUOSSAgmjJgDvlyoic26Hllzr3a-EIcgPN7GUeMSaUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=n8uB0G-2dEQOPoZU8iDis7hdqrKI1iB74qeti0uVlhEBW0HpU689x_IcRt7AZxW5RtNbfZHwSPETRgLktCluv2XsuKbkIqDEsTjO74q5XiJO4tYH_O-myE62fiYU8gGZsCmEI8VlvUNxwknpEVZ84HbQ0qowLnWQgQfA-w5ey4WH-oUHUT2zWgUWb-svW7iGyPFNyoziXpFnKvhELYFQTZuQTqq3XKn3dEoDGPf7ei_LZQ3qTYfiSPMmflO4bvsgzu1caUkiqmEOOZH8l5lNLGNDy-hSHN7PPI2g5O377-hbUOSSAgmjJgDvlyoic26Hllzr3a-EIcgPN7GUeMSaUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌اونور آب واقعا عجیبن، از دخترای کشور خودمون بدترن؛بدجور روبازیکنای ایران کراش زدند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24120" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2qgn_61BnB71WqyPv7_35QAeUo1a62RYrlombwJAU0GQxDjFWhju4H4dmNH6HGN0iFIZj0ZaRRYoZnxkOv7TjdXo5j8OX510SBF9y8JVg2yWF5CPobfmHgnVDU3OJ_l_pF5HFyeG195Gjgi1rqOc0-aTH3S6l2B12ursz-esuj_ovsjv24-kgnTx0Vb59mKp8_n3PzTcnrNQMgYNccuD2OzbrK_4giw3kxGFB53oNamI22iA96bvXOvHI_xN_ogH_EUebwojw-KMGSac3R6_Iqwc-d9CzMx4xHVl5NUWZD-rRlmFIUexo91ZOWOz2xyfKXjmO4fG3mfy-vn11O2qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛پرسپولیس 5 تیر بمصاف چادرملو میره و برنده اون بازی روز 9 تیر با گل‌گهر مسابقه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24118" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8UFlE6R0EhvxQrt7X4u20C2dYQ3RK5TELVBunJb10QIHXK0jy7bIvYRmMeP6EvrYD2Ck24kLkIvZjTQheVhtqaplx6xOp0CSXpsCNr-Xzpyc4OOfoHCSXPgcqOF-L8jZaYTbTWZbqS1GXe694LW3Cvz5SFc2hXOI2mCmW-hFkQ7QP6ayBLDgUuGUYC1HiMdvA7n-49HfTujns6xqv5uXFWJFkYcA10mNSRVykTVC7bAxh3ARmkFJKhxrJNEWGz19DhACCs4jOL0xQHiNZnVwHfDp72fBuFoXAFM3GkdM8d1UBhjoKUjsdlGj817ONvsncc-X0Bdn-q_KRMmLzy0yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24117" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEmcTKrVNo99glmouMyreqDNvQ9kEma9Io_oLFXtB2fLi7f5fRQcm_Eo1bJ4H-x3b42NsJdIpojh3-vi3Uxg4HByWwx8F9EHgBSUBPJhozGxPmK3yQZ_dcJZJ9s2IqNTDq7JSxcFpdoqrS7t7CE6pvMNhnIkJUkBSY-h8BaOMRRlUxYfcLjKu-JM5ocgwtSJ08MX2G3leaEqs69inpe4Y7RjtnIRTK8tRatlIm0M4CEtp7T6kROPOO5H7DoTmoXEgFPkwArvnha0PrGem3Zk7gLq7iEfVaxi7gkQFH2LBTdqtFPwa1ko8DeBFfJKu8qPJKvv-9_RBewq0hthTRKbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24116" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=QnHhNgfMUtPk7sgKYwU4pekA6YdhWdKjCpUpXbcUmpfL7QKZotlhbAaFfANi9S0A_mmzTWICeAeAgcA3wBUBcwCXyQh3iTZds9n-GkaHNnuU-6PenxQlvJOpnmOPBWmMk5S5D-ZiJaPe-AE-DfrAiDkgCM-Dnl4qcyKth8NtiDWd7JC1MxWZ8wQRxE4XvG1I6tfPI_Qj8rWTON8z7Su44fXc4X42G7MdAcvRdbdbG6jewe9bJsrAlml6X4IIBatDRKo1_1-6qc_vk-B0IwOEAi141tVdDuU2AOK4FA32AJUvdsESx88WIKi1tYJH4qJgfq_DOCf0NFihvro0AiXUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=QnHhNgfMUtPk7sgKYwU4pekA6YdhWdKjCpUpXbcUmpfL7QKZotlhbAaFfANi9S0A_mmzTWICeAeAgcA3wBUBcwCXyQh3iTZds9n-GkaHNnuU-6PenxQlvJOpnmOPBWmMk5S5D-ZiJaPe-AE-DfrAiDkgCM-Dnl4qcyKth8NtiDWd7JC1MxWZ8wQRxE4XvG1I6tfPI_Qj8rWTON8z7Su44fXc4X42G7MdAcvRdbdbG6jewe9bJsrAlml6X4IIBatDRKo1_1-6qc_vk-B0IwOEAi141tVdDuU2AOK4FA32AJUvdsESx88WIKi1tYJH4qJgfq_DOCf0NFihvro0AiXUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24115" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=YO9q6V0YUsWTZlNuOiP1zF7jc26SPN2dnSXRzRroYNIxHQDzcCSsm3K9TTwXR-Dup7FyBjI5b62O8rQP_AKRsZUmWvqaNuk6Q8k8UvSicxXP6vfjoImQWcie6nurfoLpWcn2D4kqzFNgPqNHgFq6dbYiRbOl9ZkXK6bsvsZmhY1-unDM5h0i0bJ76jwvnwTecNbWk74cmS_fKx3rdz0bbkastGd-lViiH3QMQDUb9CtMc8ufkmbtqgPIvq6r23FeLjOiLB_tuesI1fxYY2yHEGeR71PZmFO0WDNMaYanwPXLrOFqDXpIFYRi54XRydecDjlFDQy_8G7Zdbkvo4kQYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=YO9q6V0YUsWTZlNuOiP1zF7jc26SPN2dnSXRzRroYNIxHQDzcCSsm3K9TTwXR-Dup7FyBjI5b62O8rQP_AKRsZUmWvqaNuk6Q8k8UvSicxXP6vfjoImQWcie6nurfoLpWcn2D4kqzFNgPqNHgFq6dbYiRbOl9ZkXK6bsvsZmhY1-unDM5h0i0bJ76jwvnwTecNbWk74cmS_fKx3rdz0bbkastGd-lViiH3QMQDUb9CtMc8ufkmbtqgPIvq6r23FeLjOiLB_tuesI1fxYY2yHEGeR71PZmFO0WDNMaYanwPXLrOFqDXpIFYRi54XRydecDjlFDQy_8G7Zdbkvo4kQYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
عادل دیشب باز هم اللهیار صیادمنش مهاجم ایرانی لخ پوزنان لهستان رو به ویژه برنامه اش برای جام جهانی دعودت باز کرد هم به لهجه‌ای گیر داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24113" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8rd-lye53oq2IFmo1bpw3B2VhR027N2PHrSj7hpESJ_wMGcLyb4VIEn2XyAYVY0BE5ZQNfZzUlbi5J7hlmYdM75GQp0lG1rDbhBFfrgvGDFgLz4Ll8KCaITlh52_Y9AA0UDC8hmsrUmNtrCOw9jJnJ41NRU7fL3z_9vUc0C-6uhVlBzTuOHOP-Dv_tRNlm8AxmN3gqWwHQ1ekdR29Bd35EFsA8HDKI_I7gkxXi1lEfhZPJFPldS3OM_JW2NFEn8S_xaWQTXZqPa-zmMc7MzfpOX-8erBSArVSfu7HFs0vN6F1pJfCyI_05txd5pq_BffGexIqMbzogosSX4fODw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24112" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTSWzN7TR8_SXd-yJNUNMdFrs9MiQwvibjoMQrEhAbzd_0PtBjhG7VbTTEQGMu0kZjOnCMFinhjAlc02qYjjMXzT5nh5k7TVjfZuhrtGWKeq7QD1X0Xtawd5Gy-L6vFvt5GxexyJs1IBCj9AJMO7_JNwmpYa1XqHVQeYVFPBOnYwexEc2bPYqJR5C609I8KlYqpLT0UE6aOwbCthjUerZQq8eoqfLe3pw_sdkszlJvtfSUj3VlHUkCI5UfER8FzE51Yfq4Gk3Jvo3qydRlu5-JzUaaQNdRLbwU5Poxc5NYbDm_ipiBOHaPaQUihhNNaKPHxUTg4Oos-ooDgwNRtmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24111" target="_blank">📅 09:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6r_t2WLCBuxaOKI091ZAKs1HM2N3E-EMrR5Dq1a-3VZuLudbaoLLQuzr91AGEoDGdwS2eqBLf1kCdm-kTr-hB4HZ-gqhGw3qrrKZPwGA6BxEbl5rrAAe6C2z_19kMaOzSMKvtSdeDZ2J-joKwH9VwGh0VqAHz-vLdO6KZfUtJas6D2Qj3GK8om0YFc32nZHLCihL7p9s7DhZUaFKH-Bze9bR3dP9siSLPNFmFevI3PoyrJOYM5lay-gfHv-iYsT6kRGJj9lg1w2yx0Ur7zqZjAtWBY-cPeFHkN3rMyhogDTaWck2XmGw8v1XucXvNIwPvBpHHwg8eNdNp-73ggylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌برترین‌گلزنان‌تاریح‌رقابت‌های جام جهانی بعد از هتریک لیونل مسی و دبل کیلیان امباپه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24110" target="_blank">📅 06:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24109" target="_blank">📅 06:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3lgCp4GEN5A_kBJ3EsOs3lsf8gF4lDlfBPazx3dRIXyredyCG_GAGeeqdP2syDqX-exRHHt9Hx-EfghpKrCPS-IO1CfXs_oqVQ9H2XJXrBV8x5Phw7xkeWwgj-9LkUVl8-SYVNMBRPeHP3yPf3IDTartlWCISA94eehi6jCDsJ9ts3K-4MbcFJYotCSbAZy5whSrU5VXq0dVbv3D4RkxxloFdvSoDyhYypkwVl3Yo_HI1EMsnsX4VveqFgcgf-SbsUIUQxAc8k99AMEn8dFIptTF_3m2CZDdzJmmrYDwc102HvQJD9BSNnkIHXHsKMcgHEvnXO1S3ICPx_WvYOAqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24108" target="_blank">📅 04:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دو تیم عراق
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24107" target="_blank">📅 04:30 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
