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
<img src="https://cdn4.telesco.pe/file/e19dkDtGMIMw7LG-ecBJi9Mb8KgmXUPVORAD5qLHQMF4YFbYjxDrC8RDTGxCyDuvfR05ja8K8GIZd7sReDvSLZH0EQCdgayvHUc8a0tmDxhpQpEOYmnrdaWGQehlxJ7eqEwdpwDpzilrlKl2bc2Iu-8xCWnUTyOSVr8YoXlcesB_oeeDOSmTl20l5SvIHZWpp_wSFFOFbS_PmRzAkv4iOTb-YRTCopBTSErPoWqKPN0W2lrHqW-9TrDIjYsdjOzN8EsVgJNkbzOsaLOQjXQCP2t4ozjHe7VzSOsf3_SRBpNjm4pBIasVk_tt0B8r1TbU3fbLsMcdiMLvH6G9dWm-Cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-20281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:  دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/SBoxxx/20281" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20279">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWyp71lCl3uvKu2U4b4rMZ_8JAmb__Z6SeUHvBpooiczxMqQ2nmT40ueJPpZSJKe_O_8sQ6_0vih_E9PigJmAy4RwlVOpTf_NRJhpRXVxbMZ1UqhKYHtoMbZ66xv1FAdXmoqfoj1ZhJs_mML_JTNh2PI8FNR4h15zUNZJ5Bsn-1Qr3c6MF7vFffAwm1ZmFTVxCtuEieigT4Smrp8j_z_yCqxBt7QMqahAE5Ia2bPYbSz5d20OlO-6587ebuu9QGARFI-TDZQpZbE2l2njgwAEC2DTi7XfESc0EBQn_E3Q6_v0AoTXf9_WZ1UqF3SYbVD9xV8sgxB80HV5BK-XG_FeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
دیگر انتظار خوش رفتاری از من نداشته باشید!</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SBoxxx/20279" target="_blank">📅 16:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20278">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-CgF_qCnC3mmqs-dbIm8tSaAS98YTDiWY7mK1eH7DmNyUdUzT6jGXTkRRTKkCK-YBVfBliwQ6zcSyh6OtvoBTVxHSGc4R8PRNVnm7JmtsN4G2Wc6S7at6sOhHWUqRZo60Hqmaq5NlA_sP36VYBybWTBIXBKXUXgG2vLDd-kYXmcYn8IY3Uoup6mJhLMgZHqLpMU6ijbGUJCAvxMkvl_tbIPDdMcqRwYIFm4_vRW8JZdX9j65ciScm5Y4sPzD0CsVVZrPn2i8QX9cISk2X1d6fZiQGixw9jH8WqU9O7hg1QW41boDXp_peRsSwtf-87cFtJlGvPJm-yMcsHp4uLL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس
:
آمریکا در نبرد تنگه هرمز، دست بالاتر را دارد.</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/20278" target="_blank">📅 14:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20277">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICivBsEnXaiu0N_8CpXgOcFG8GRLOr0Ra9mxsfCICYCxLDGsOtRXyXFXOA5pNZ78IXGiyEQhQIReVWonilCkHlpItTGqhM61FYdufVn8cq6DGc0b0RZA0VnbyEQoVG5lrUbtoEXeXwY6TopeUb2K1tBruyoiOBX4DcOfgxVYs41FebRvS1gbifGD4Pto0rr33v7VxPv6tMqCqopmzm4Fgrkajo8grQ9Ryarx2SzBHhPU9hrH2_dipxypTt3fzlrQUFCUE1SsOP983KLD-sDekK-qLjUPT9gydV1SN-T_bWRRcSNxdW110PdBKiYbpFL0vuxfvp6_gP0bKJ4AtBztNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/20277" target="_blank">📅 12:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20276">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pd0S7Rr3aV4FuQJppTZg0m4uIHnlo7n77VDXjRRlzcyv5tIE06a-J5Qenj-XPOuT9yriosgDu7dLbujc-O8zN-TfWymk_6tIYAJ18yZ5Un-j2z9KcDp1iaq9NkMVyOUb5BbY6L17qyZxBcy3KcPu5zHOQ_snkz8qS816dDETCg27AoXngrogpZPD01VxS1EItH-naq0r5HQ6SRbGf9oPIgBffYl0J-INBo10QJSMfhOyJfeGSO0lCPoe92IHLWKGbCDrJn8RqjcV5t5QFiMZkkk-Q9NQuvZLzjLiB_JU4T-PgBr2gLboFKiDJfrl54R5SzXus0kLYXVRfIbIrDanPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح نسبتاً بالایی است و با این وضعیت انتظار می رود طلا موفق به ثبت سقف جدید نشود.
به نظرم بالای 4630 فروش دارد.</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/20276" target="_blank">📅 12:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20275">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">این بار هم ۳۰۰ پیپ دیگر</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/20275" target="_blank">📅 10:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20274">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">عزیزی، رئیس کمیسیون امنیت ملی مجلس:
هیچ کشتی‌ای بدون اجازه نیروهای مسلح از تنگه هرمز عبور نمی‌کند</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SBoxxx/20274" target="_blank">📅 10:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20273">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به حومه دمشق</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/20273" target="_blank">📅 00:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20272">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یورش پلیس آمریکا به خانه پسر ایلهان عمر  ️روزنامه دیلی میل که این خبر را پوشش داده، نوشت که پلیس شهر مینیاپولیس واقع در ایالت مینه‌سوتا به «آلفا نیوز» گفته که سه‌شنبه حکم تفتیش خانه عدنان، پسر ایلهان عمر، اجرا شده و در جریان این بازرسی، اسلحه و مهمات از خانه…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20272" target="_blank">📅 00:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20270">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بد نیست بدانید ایلهان عمر یک نکبت اخوانی است که اساساً به صورت نیمه غیرقانونی در آمریکا شهروندی گرفته و اساساً زادگاهش سومالی است؛ یعنی کشوری که دقیق ترین تعریف «دولت فرومانده» Failed State را دارد.  عًمَر همچنین یکی از سگ های وفادار به اردوغان است.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20270" target="_blank">📅 00:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی:
اگر محاصره ادامه پیدا کند، صد درصد ما منافع اقتصادی آمریکا در منطقه را با موشک هدف قرار خواهیم داد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20269" target="_blank">📅 23:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20268">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20268" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پزشکیان
:
اگر وحدت و انسجام در کشور نبود، قطعاً ما خیلی جلوتر از این از هم پاشیده بودیم</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/20267" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiP8iu1nqaoGgrYlB1Z40qeV2zbqTKSZgLIumPX_8R9Fy95l1e27FvkPAkEb7hgzW4m3y-J_dMjb3smKSjmJSmLFIi9setQLetTpDLXHOwrdhaOO-PUs3Fj0y5c5r-STuI7BHQh42ZsgLXl6tzEjNCgF-TgusYE8_9M04DSCea4tuLHdopBHH3apPjBhRxQYZpwXVuoOmBEPa--H26TEP4-8mfv2J2Ag6l5qywTI5ssk1viF8yW8OLXxO-WDYovDP0QvtzOacDjas3HUa3sHvk0c-DRFTyNhnX8zrtuL9W_LdIuuq1VS5sXSAYfc8RC4itLbiTd1TJ8kxGVc4bOw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازگشت به تفاهمنامه مخالفت کرد!  کاخ سفید، درخواست بازگشت به مفاد یادداشت تفاهم ژوئن با ایران را  با مخالفت ترامپ رد کرده است، که این امر تلاش‌های دیپلماتیک این هفته برای از سرگیری مذاکرات را پیچیده‌تر کرده است.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20266" target="_blank">📅 22:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20265">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ:   کاری که ما در مورد ایران انجام می‌دهیم به این معنی نیست که جنبه نظامی را کنار گذاشته‌ایم   نمی‌خواهیم با ایران صحبت کنیم و به دنبال ملاقات با آنها نیستیم!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20265" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20264">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ:   احتمالاً بانک‌های چینی به فهرست تحریم‌هایی که علیه ایران اعمال شده، اضافه خواهند شد.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20264" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20263">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20263" target="_blank">📅 21:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20262">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20262" target="_blank">📅 20:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20261">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20261" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20260">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-bomYi-mNuENcMu030xr98mOCF2FbwnEJ6RNp4fLWnsq8oWDSqQtZtY61E3wR6bthPM-wDiUVY0bWSKVjK5o3c0rc8KrCRl08FqTKnW7clR94fDKxtJlWZjUZyGvUUn1xtd-VxO2tWhVEJaxqYwkKSp-qYDLN2ezyDTNvUANLy683Cb0vhFirNYMI4qiwsDSQU5IfYFZ8xEh1Rzieq6jjKl-NhKPJNm7Y044jR7z5rBCXImsJPJ4Ds_UgJyHUh7B8jVIgGFSUO2u22zkUjsVLceh0M65vkeVMc3TisKSmklil-6_crmgko7Qq6WXfQ-gVQ4nwyZi_Z5WQOb2_qQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بسیار مهم اینکه این اسوه تقوا و هنر نیز به کشور بازگشت و به همین دلیل قیمت تریاک در ۱ ساعت حدود ۴۰ درصد رشد کرد.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20260" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20259">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!  از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20259" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20258">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20258" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20257">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ایران می‌گوید با وجود محاصره آمریکا، همچنان به فروش نفت خود ادامه می‌دهد.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/20257" target="_blank">📅 19:38 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20256">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک دور از 4570 حدود ۳۰۰ پیپ داد  دور‌ بعدی احتمالا محدوده ها را ببیند</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20256" target="_blank">📅 18:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20255">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محدوده های خوب خرید طلا برای امروز  شاید به این محدوده ها نرسد لذا توصیه می شود به صورت پله ای زیر 4580 خرید بشود و در خود سطوح افزایش حجم داشته باشیم.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20255" target="_blank">📅 17:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20254">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حملات گسترده ارتش اسراییل به جنوب لبنان</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20254" target="_blank">📅 16:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20253">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سخنگوی کاخ سفید:
در حال حاضر هیچ مذاکره‌ای با ایران در جریان نیست</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20253" target="_blank">📅 16:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20252">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دقیقاً 20 روز از این داستان نمی گذرد و بحث حمله نظامی روسیه به انگلیس دارد قوت می گیرد!</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20252" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20251">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انگار یک دستمال سفید را دور اسکاچ سیمی بپیچید!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/20251" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20250">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.  این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20250" target="_blank">📅 13:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20249">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8Hfsh1BUt2FaXeuZocl6DMP3GoVtCjWK16_2n4FRgTWpXXUDClHvD4xk46gm_SbYRCOZU46bcm6tneMpKZaBtUJ16JI-AtPdLof0GTvg9ujtpEVh00a0UX-ETteJTMyGFXGIX58InGQAkR4jM05gFnh3cZu89cwhxyegRM5-3KsXUCh5Rpv17f1NqmHUo6S7jEeXIGRC2nM_8efpSt4N2wjZvIpfFmXUaI_Gcl6OmgUXjCWh5oV4NdJMirw4F3ovJmhJRIVe_BUWTipYJjZxxy25ZaQ65VjdLyH8E7S_6pDINT32mNrEJlokzzF_NIgN2ls_HRgjfK-BvKFqpSQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالد شیخ محمد، که به دست داشتن در حملات یازده سپتامبر متهم است، قرار است در تاریخ ۵ ژوئن ۲۰۲۸ در پایگاه گوانتانامو به همراه سه نفر دیگر که همدست او تلقی می‌شوند، محاکمه شود.
این تروریست که در سال ۲۰۰۳ در پاکستان دستگیر شد، از سال ۲۰۰۶ در گوانتانامو نگهداری می‌شود.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20249" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20248">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K37SRQmy4UheGS7D_QbckeKZTTclPB5cVk0Prnd3-PRqPKHVhS2owMjNn_4g-lvL06SKrrUMdnqX_aiwAXzQifSglBKHTs6Y2TP3B9H4pdBz6_A-Qln7ZzDrirtUs3AudLxGuL1kfa4I5batYt5f_muRJ6LNnWb-Fiwa57My34WVW2Lt1qXWos8p0iGuWFEm902Tn2-HJx-RFyBykVR2UFrk0cRx3HUw_k1p_nkitoUxmNBqKwDcIfjbSobXJLiyih_ucSih7rRsZr7SFpUYQnpUy1VlY3bKZ8o0aHv19mgFEkXyLGktrmza9bhidliPZQHwERLKsC9x9gR4Q45JwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.  خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20248" target="_blank">📅 13:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20247">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1XWfh3xjpmdtX2Qh91gvq87kp9IiW57Ac8aerIz6clwoJmmAN7yzl9qTrweMBuE5g40vCg-3JqNqt4XvrUWXyv8mWjB19y57VL8U6sSsCe7Xw2VyUf8EnlNFdSeTrn2Rman3YdkVSfCQkrGpI_d8rvYIn5uwVytSnu3BUB5H41q2qeeDf1sPMgC6GgWQg3xkHc155SEv2byP-KRcNzK5zJb44DBnhg50Ridb_SJyRbfw5mqhzaX7YpQeaBca93ZXoGFKT706dFnm2cKThk8-j3H0_pR3eiFUyC58Kz4v-p_IiXg2AENy3DUn2M2H48qqr771j0TCnhnCsRD619s5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز شاخص ریسک ژئوپولیتیک در سطح نسبتاً پایینی قرار داد و پیش بینی می شود طلا یک کف سازی انجام داده و رشد خوبی پس از آن داشته باشد.
خرید در حمایت ها شدیداً توصیه می شود.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20247" target="_blank">📅 11:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20245">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_dLne4RJIZL1N_0-Ymx1rvQEP4MHMxpDMSIof2iYPK22hJ3fW0djIsFRPQUYxShxWQXtpI27PdUVzL_9gJiciAQS3Gk2ljFDtn6B3sYRwZukkG0x6B-LKtx2UuHHpm5VNQSUwz8PX4vxZhlwB8VKsL8Ql_eZIvFdoXtFolcggv9GLDacYMnT3RTDDWvRc9Mok3Pmyra3NGGalm0e5Tk44I_RtHsCXXrYOI3nsRLxBLztDsiMA7YaBqfLou4AI733WFnCd-BVN9yORLcVfEMw0-YXsyITq6hbMD1gyYAkAclyOhbQOGitb-UjbSl9q4VldSy6fwmZOsCYDdaLy_lwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MD9IgyCLRHNTEcbll5taqszaLUPC0q6hxh1hlVxowRItMkrFeDIovcgvxfxvqCukO6aC9lRioWAUqvLyT7ymjHA5ENMnSzEbbSLEbub2cj2qtCk4tDaLhIbZa1kD4tmdR_SeevdX6xps_1uUqHpLuZYgRfVM2NAMTPiUJbExO7ps9YJVUJFIskYEKNX3khXZkDHDCeRTtpZ1_8rWMuxIGkGJqwl78uvs_BzPhwTImYhpxCbOT8nZbTb1LjuZWaG-JsJ02PIDEAxvJAiV3gdz5w6949G4YKZlO3KF44uTfSLRl_gdH6LMzNpky1JdcfucT6ug-aNMgh6AU1Q1p7e3sw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/20245" target="_blank">📅 11:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20244">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=BU-4h7RukTcehEIF1lVZu1vnabjSrEYXqYYUyb-7Zp7scorZfWPCJCjFE2jvJfYwkgvY7-7ANxq-5hDvsIuWbaw_wlXWHLI8CQ9AJqgkUqnplF2F7Z9cgNosqhHwOA0ncKxZHM-yuDIFcMUGCHEGwswfu3I33NFvbP0p_scloudla-9yxNO4V_QCOsR3IQrDJNuJGQn1RIcVJH0sCsm7D7KjaabTuJlCUFK0NzpSyjxpNZ0GGk65AFrDiFr4pM9-o_J64ZiYaGvJoVq41pvUgqhfS-HKpKw6juhiPBn9arz8fjJR6eKS1nE-ngiXj6k7c2BX3RlvA1slip91Ux022Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f65ff1052.mp4?token=BU-4h7RukTcehEIF1lVZu1vnabjSrEYXqYYUyb-7Zp7scorZfWPCJCjFE2jvJfYwkgvY7-7ANxq-5hDvsIuWbaw_wlXWHLI8CQ9AJqgkUqnplF2F7Z9cgNosqhHwOA0ncKxZHM-yuDIFcMUGCHEGwswfu3I33NFvbP0p_scloudla-9yxNO4V_QCOsR3IQrDJNuJGQn1RIcVJH0sCsm7D7KjaabTuJlCUFK0NzpSyjxpNZ0GGk65AFrDiFr4pM9-o_J64ZiYaGvJoVq41pvUgqhfS-HKpKw6juhiPBn9arz8fjJR6eKS1nE-ngiXj6k7c2BX3RlvA1slip91Ux022Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیخود نیست صنعا را پاریس خواهرمیانه می نامند!
ناموسا این ویدیو را ببینید! پلیس های ریقوی یمنی دارند مردمی را که هر کدامشان یک کلاشنیکوف بر دوش دارند «بازرسی» می‌کنند!
به خود تفنگ شان هم‌ کاری ندارند و اصلا مشخص نیست هدف بازرسی چیست؟!
شاید فقط دنبال بمب می‌گردند چون میدانند اگر فرد مسلحی بخواهد با این جماعت درگیر بشود که ظرف ۱۰ ثانیه به گوشت چرخ کرده تبدیل خواهدشد</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20244" target="_blank">📅 00:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20243">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20243" target="_blank">📅 22:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20242">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به نظر می‌رسد داریم به لحظات ملکوتی وطی دبر حافظه تاریخی با علی آقا کریمی نزدیک می شویم!</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20242" target="_blank">📅 22:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20241">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قالیباف:   رابطهٔ راهبردی ایران و چین به اجازه هیچکس نیازی ندارد</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20241" target="_blank">📅 22:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20240">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFYMEtD9NYhurmmj8xgOEJPpU-a_LVzFJngnYIFa2yYKPYHXObS3NLpjs0Ejl3doewftvdmDWPoOhThNpXm6VGB_J2d-k0lGpWLpiF2cwUxqKgnIOrr8HEwdEEIj-F2D49VX_0Hqaa2rk8kpXUiYiyfa4bfQJMN3Mw1vSMmZdJ5K1XZUzyvLFl-XbqOVrE9H8HaUVzbMbpo6SkXJKujpJhq7V_2ttuHUt_wsvxuXsb_D6vDBhIu9M4IfylCR914CZmkpH-gTJSguIdCPomFCNHWCR5rwFxLYySUZiPoRGsXkvFWp9P6F1pf0HPl4k1alPDIU6PSBlthRuwfNX70vUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفتگو با الجزیره گفته که برای گفتگو با ایران شتابی ندارد!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20240" target="_blank">📅 21:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20239">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در دنیای فاینانس میگویند همه تخم مرغ هایتان را در یک سبد نگذارید!  به عبارت منابع درآمدی و دارایی تان را گونه گون سازی کنید (Diversification ) تا اگر یک منبع تهدید شد، منابع دیگری باشد که جایگزین بشوند.  حالا حکایت ما را ببینید که در سال‌های اخیر چطور به چین…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20239" target="_blank">📅 21:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20238" target="_blank">📅 21:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20237">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک نفتکش هندی هنگام عبور از تنگه هرمز توقیف شد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20237" target="_blank">📅 21:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20236">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWRtxz5Ps4hL_ALxouYmJJjH_l0YJtGRu90AIteAWDg1Hx4y3U2p8Qiz1Y128-_MvHjF265gF_kDEjrd52F-9F96TUW2bcrinqNVxa3F6cys_TqaQZTJY1EBeOSGQIUkoeHMTGqkXivm4rgiSmGflfPnGsMYA-L1e2HwXpaVHY8qRTCla7xM6TRAJcSOHif4aw1UOSIpBQOrP8qamZG_FdOnm27xn_UVdF7Ie6sz9_r_Bd6i-mHst0eKCPAfKjo9AzX8t0XItAcMYVLk8dWp8mcgf5Mnvv65jpDvqQv-DTRtbyK6YCwkrvFNT-si-cHfGUYbZFWdCJ14S-QOTVyzrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواننده Secret Box از 18 ماه پیش می داند که چین
«تا جایی که می تواند از اقتصاد و حاکمیت ایران حمایت خواهدکرد»
و البته از
خطر و ریسک این All-in کردن به اتکای چینی ها
هم آگاه است و متوجه است که به محض اینکه آمریکا یک امتیاز اساسی به چین بدهد، ر
وسیه و ایران هر دو
در موقعیت بشدت ضعیفی قرار خواهندگرفت.
اقدامات احتمالی ایران و پیآمدهای آنها را هم دقیقاً
1 سال پیش در یک نشست لایو اینستاگرامی
مطرح کرده بودیم که اغلبشان تا کنون محقق شده اند.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20236" target="_blank">📅 19:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20235">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خلاصه مقاله آسوشیتدپرس که دقیقاً تاییدی بر دیدگاه ارائه شده است:   ضعف اصلی استراتژی جدید تحریم‌های آمریکا علیه ایران، نه خود ایران، بلکه چین است.  واشنگتن می‌تواند شرکت‌های ایرانی، شبکه‌های کشتیرانی، واسطه‌های مالی، شرکت‌های هنگ‌کنگی و حتی برخی شرکت‌های چینی…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20235" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20234">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk76vDlAtwmDC7iJjWnMJdqf8xE-80FGTckOoKoEm5pjSBCfLlwhPf6QUTQXvI-f2cCqULXXZs_fcucK59M0Cyx5cEvYLsSncPAbC-vmgEeth4jT3F14w08ky7OBepMnRAUV_S2-ahPM368lIpSKG0HJvYbfWcssSBH5fY1ZiBF-_qVZNsqG8Dou93okF9pgaEM4HeAvjXxlrjdKiEq8AVckqsoIvQF3331BD2_CB-xRffjUVsoPAq0WNhw6kvZDmMiSCZFP_dbN0OTr5cQzQ-8CrMi90uvRAx--gO4TUdQ6dpUVqXNG8kSyzvCin8sXvmVjkNowh990Jc6rGbr7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20234" target="_blank">📅 19:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20233">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=i04nQ068XKcuccj1slpwHj7ZP2oO5taCYQ9wTHTL5fu2Uuk6RezS57RFP0Hg8hbfg9oR_Vrt5eLUR4h94uJQnOdC_3Xv9JtTYznWU4PYT1fm0dIbyx8s_bvbJyqr2egBSYS0neAZerIPX8_WPjJkmg8E7YP5p2KCHI5pt9u_Wlxe1H3bsqu4aG37_cheW4l_-Ex9VfD6QlKJPsxz6YzlqMnhj9n9lbhPVe2L39rvyt8ZvOfVYsq1qF9s4jFA3edwDmLa2bL6Lmc_Kt9N6PzpJOP5fnvflxxnRvSIpb4cnEAWrUNwEBw07j7WmFTe5bQoA1SXsamTzQworhh_Rp_dzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c39d5bd85c.mp4?token=i04nQ068XKcuccj1slpwHj7ZP2oO5taCYQ9wTHTL5fu2Uuk6RezS57RFP0Hg8hbfg9oR_Vrt5eLUR4h94uJQnOdC_3Xv9JtTYznWU4PYT1fm0dIbyx8s_bvbJyqr2egBSYS0neAZerIPX8_WPjJkmg8E7YP5p2KCHI5pt9u_Wlxe1H3bsqu4aG37_cheW4l_-Ex9VfD6QlKJPsxz6YzlqMnhj9n9lbhPVe2L39rvyt8ZvOfVYsq1qF9s4jFA3edwDmLa2bL6Lmc_Kt9N6PzpJOP5fnvflxxnRvSIpb4cnEAWrUNwEBw07j7WmFTe5bQoA1SXsamTzQworhh_Rp_dzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی:   مذاکرات مثل خوردن گوشت الاغ مرده در بیابان است!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20233" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20232">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نگاهی به فیلم «رشته ها»!   امروز، ۶ اوت، سالروز بمباران اتمی هیروشیماست؛ روزی که در سال ۱۹۴۵ برای نخستین‌بار در تاریخ، یک سلاح هسته‌ای علیه یک شهر به کار گرفته شد و جهان وارد عصر جدیدی شد که در آن یک بحران نظامی می‌تواند، در صورت خروج از کنترل، به تهدیدی برای…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20232" target="_blank">📅 18:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20231">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: می‌خواهم ضربه اقتصادی نهایی را به ایران وارد کنم
ترامپ لحظاتی پیش مدعی شد: آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20231" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20230">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-poll">
<h4>📊 اسرائیل تحت هدایت کدام دکترین و چند بار به تاسیسات هسته ای کشورهای منطقه حمله کرده است؟</h4>
<ul>
<li>✓ دکترین مونرو — 2 بار</li>
<li>✓ دکترین بگین — 3 بار</li>
<li>✓ دکترین بن گوریون — 4 بار</li>
<li>✓ دکترین شمعون — 2 بار</li>
</ul>
</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20230" target="_blank">📅 15:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20229">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ناصر نوسان کف دلار را در 195000 بست.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20229" target="_blank">📅 13:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20228">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20228" target="_blank">📅 12:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20227">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20227" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20226">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA60GyWOQS2rNgjZ951NSVjAKucd4EggMfGRJ68h2P1PtDh0Lld3G00QPpV83dj2iKn6TBGEwyfuJefsMbQqxfFOy-4caBXwq8n4NqrbUy-A69DXojnAyZAk69lsl-6q-NPJgUDNwT7NqTOP6n8qYUll88TiqXPn5TowDBuPf7B5-52zyLUqTm9MUx_ZrpspYarxqNRSPF4M6ETEPlx89slLm3y8mDZLYyidDPhOJLY7kGGxlSvLbb-UQ2R65jx20gBESg4bbUiAg9aVXWohtn1A17BraQm9_z4jOYDdCk3IzKDU1-yVa7sXAObh53MDU3pTujTZZZnAbpzV19gGgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش
تا زمانی که بتوانم پادکست های GeoMarkets را دوباره از سربگیرم، این جدول هر روز ارائه خواهدشد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20226" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20225">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVza-2QG8xohtHMbg0SYHZn-EpHJSZf2BevkxcYYkiT3CygCqeGicYDE0yMAN2VXDvvQCHtXwG-_YeG8nxI4EPsqxebQYsVRbmjihDLPbR_kNGmBRxdnIn7TGBXViT8ou3L0sAeaqBr9N6AOhgV1-8p9qT2zgJgYtuQhAXkKjsxNCAArqPxkGUWERbUIPv7c89Trc12pSVJMl1Cygiw6r-3hGe9d_2PuHnrcTD7y1n49Xgvum7mt5OfAb7cxcpi1-Q4W1igWJXHNYbznbbAvgJTcl5Yc-qH80Ow-Kb7lsDo4gFEnQeA0G6xG2HjMWV49SypJOEcM9CR3j2eisWRcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتصال ریلی ایران و چین   پس از آغاز نخستین محاصره بنادر ایران در ۱۳ آوریل، حمل‌ونقل ریلی کالا از شی‌آن چین به تهران افزایش یافته و تعداد قطارهای باری این مسیر از حدود یک قطار در هفته به یک قطار در هر سه تا چهار روز رسیده است.  این مسیر ریلی پیش از آغاز بحران…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20225" target="_blank">📅 12:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20223">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8DdS-jcb_TgfrNRNjjCcIsV2MswrNmcIlrv339uZWcOBNwJlVkrceu4gVIHkGynUC_1kLf6neFKDKCDFVNkbeci7roE_WpeB7W5Vjsy5yXzueBT_LHchXyDJIAPGEVgZA_uST6MhLVy1wt5UhwFxHZhkh420H4I4Nlo4S3id6Yl76aABv2DtaO73Dcu3i8FK4YlnjPRqTlmXf7zMZdoC610hptNuQ7_z9ns9WLlDfZG1UlBAAWkR8kCg-fC8L0rnyL1zjBMiIv38Al9i7Q73MTjhhTXziseBXlSnp0ZsmPFuaoOPJUEvRF9ItHUWo7uSpgdHRC2yoOos2FV2oY3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnYbPsOFj2_ADgnv8HFcWz5rtnUmrqDSresITub_gmUH01yTGjuRLm6H5jHlMv1fj7zaB7wHCbBUVYObIT5kvBCT_97HbM2Wokq54LNFxo9qQMt1GpMaZUaViXK7qb9ZLaSAyvET1OWxJsCYDaNrSS0m9_FSX5-O6PVmkqbU85JUKz8rUUc9F6FmmpS_BJcMfYogJPYSSif3jh4M3dhQyRxJ4lB2Q6RJDmt6wvNdj9xsOf3TpD_fOTJHQZEnmdmppRmvr3lRtdf9kRyujOXDGZVlu-A2VHKBOn0hGgYqTV-0uJzlDm28Uunv2mucye98IZzgEyfSx2tLe37gucZv1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.  طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.  دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/20223" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20222">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laMVmZgT2Q5a9fJQzUojoPWO6xecMU-2nX9KZHwj0rMrLxAyVbfH2XW6aey15V4vBBO2_lCRPqQbZ9ih3olM0dhWlJUVDPwgxoRKhCYJBoudSLootaQHpb2wHmT9XsJ1LZqRxSTMIjqtLY4nQUVnpJzFSmilk11EWxoX314i_xENgOJybQ5zbnBGqQKSxD4ClNbOtfMOdy0zBYZL0T5Am05wZKUGP8azs_0HodOXflZmUWa2wTxdGvuqWy0UOW8Kb2JkcYaepi8yYz8znQetbAaX3DJGvK9KkBGsfkIvCg9IwpW4X8ObE7bdcwZfGOOdQWcR3aUa9_qUoifHEo7RYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم در سطح بالایی است و فشار فروش روی دارایی های ریسکی و احتمالاً طلا پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/20222" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20221">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عاصم منیر به تهران آمد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20221" target="_blank">📅 11:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20220">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ1iHxmmp8bNeHG2WKotgwo0qrHEV_IUdCg1BXBhM_cTFLJfud8mX1VTAYFPSZYrgD4xDIGPn7LrDV6zn8rtabLAgguFd0ts8MeR9eq-0NUpwxNsDESt7A_PdnAEop9Esvi50yqQFEdsYrTuIFeBc8mjQIgMfv9Y-3jTTU8_l3EgWql1oBXOhkh2g1AOQDOqEHFI6i4v6PefFeh1MtHumVczHPE44RH6EYxeAcqD8dIhgHMCK_lb06bc9J8tt5nNyZ3vCyx_KyqJY1mvQ8Hg2pjK_iU1eHr7nvu4StdoDi7dIDHlExTgIrfldUP7dKHnSpCtUU0MMm-8HoPBnQm99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه NBC:
حملات موشکی و پهپادی ایران خسارات بی‌سابقه‌ای به تأسیسات ایالات متحده در خاورمیانه وارد کرده است که از هر آنچه ایالات متحده پیش از این با آن مواجه بوده فراتر می‌رود
- میزان این خسارات از هرگونه تلفات قبلی ایالات متحده در تمام درگیری‌های گذشته فراتر می‌رود.
- بازسازی زیرساخت‌ها طبق منابع خبری، میلیاردها دلار هزینه برای واشنگتن در پی خواهد داشت.
- این حملات نه تنها به تأسیسات اطلاعاتی، بلکه به سیستم‌های رادار، تجهیزات نظارتی و پایگاه‌های نظامی ایالات متحده در عراق و سایر کشورها نیز هدف قرار گرفتند.
- این خسارات سؤالاتی درباره توانایی پنتاگون و وزارت خارجه در ارائه حفاظت کافی برای تأسیسات خود برانگیخته است. کنگره از همین حالا بحث‌هایی را درباره تأمین مالی بازسازی تأسیسات آسیب‌دیده و تخصیص مجدد منابع اطلاعاتی با توجه به افزایش تهدید از سوی ایران آغاز کرده است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20220" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20219">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3f69Nd8DHjAiZDMZGmPgoBmzVTNHdz0dAcvzFqda2nTU23Ij9r9cJ-9LPSiAzsh4GDphZFQEoq3EofgKGquT8DPGWF45V14YkiSzoe3spZSM5WiuUAiJYxDYbDiu0h70G1kzJ4pzDDCHTNfJ41elIkZPdH_tSu_nJkK2is8BQdqoJ1B1opRI5CDUqmlnjxrCm8iV1_Jpu_V1uMjKxxqBfbSoXbPti_Gf8jjOvSaLGSiYD3oZesWnKPMtc8PNXmheOvPNWWcdmI_EyM8Zupvoa_3wPzxPUo6pjUTngSSvSze-5ZVzP9P-AfPUWmaWtZbIE9ldiuUPTyUH7FIQAZprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
روز شلوغ انتقال نفت در دریای عمان
🔹
کپلر: در دریای عمان دست‌کم ۱۵ عملیات انتقال کشتی‌به‌کشتی در حال انجام است.
🔹
حجم نفت خام درگیر این عملیات حدود ۲۵ میلیون بشکه و مقداری فرآورده نفتی است.
🔹
نکته مهم اینکه منشأ این محموله‌ها تقریباً از تمام کشورهای نفت‌خیز منطقه به‌جز ایران است.
@khate_energy</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/20219" target="_blank">📅 09:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20218">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ می‌گوید توافق هسته‌ای با عربستان سعودی تنها در صورتی پیش خواهد رفت که ریاض به توافق‌های ابراهیمی بپیوندد و اسرائیل را به رسمیت بشناسد</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20218" target="_blank">📅 02:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20217">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=iG2-V49hlkVKQu9yJ1iCObc6MqznJggBQqyfOGKrm7lT2GYFmQR4gkbYGfAEf12ywRZWJmeweCzv1ousQOVjCqZK-v44feCf2eA9oXbwQmLylMmkCaMzcTwxKKT0Cv824ygVzCP6nFSpFflU-0sm-QR1_GLMhyk_0Dcgb6lm9RZwNTpqlo1dzH36mY1TSLXM2n7nGkAPKRGRS-3jQK_rWoizjddxO_qQxH3jAD-Y5NL9K7ftXKoGisg2IjbA5N8zlViIFMZAqpbAj3-8zp8RWhISjnzvsD_uG1Jq3FOtOfrz8fSceqaQkpoPI6GCfcy-8cT3HU2d1H0dZOlVgFxs4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c56a73bd.mp4?token=iG2-V49hlkVKQu9yJ1iCObc6MqznJggBQqyfOGKrm7lT2GYFmQR4gkbYGfAEf12ywRZWJmeweCzv1ousQOVjCqZK-v44feCf2eA9oXbwQmLylMmkCaMzcTwxKKT0Cv824ygVzCP6nFSpFflU-0sm-QR1_GLMhyk_0Dcgb6lm9RZwNTpqlo1dzH36mY1TSLXM2n7nGkAPKRGRS-3jQK_rWoizjddxO_qQxH3jAD-Y5NL9K7ftXKoGisg2IjbA5N8zlViIFMZAqpbAj3-8zp8RWhISjnzvsD_uG1Jq3FOtOfrz8fSceqaQkpoPI6GCfcy-8cT3HU2d1H0dZOlVgFxs4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20217" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20216">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خیلی overbought است</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/20216" target="_blank">📅 01:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20215">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:  پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20215" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20214">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=HvSrbOdoeSHzkn6ji3d-MOIF-V6VUGjopM8lvdjMSD_DQskMZOdGfT_fEzxX-unQihgkGumnlfNOwm8wVuPuIGL65OFwBtDUVKryPYf-K7DYwVoCm9C80bHhUKObsGHbUdI_26aoF5LndSJT0ms_3Uaa9bq6Ezxq2J9YJe0XIt4v5KB-wiJPavMKA0X9B_Y0EGU4xEINHAJuq8lAlpGyY8NZwI-chsVjzK-_eMNCE91j39wY8pNDRLmRVZ_onDP_jLzX0uCi5nZhiZmNXrEiQgFXOFYCKEtRWfEAFdfjXaMXEYMB_etdEvK7_m2s74s97UE3_XmDB-3criKlbozXsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affe27b93.mp4?token=HvSrbOdoeSHzkn6ji3d-MOIF-V6VUGjopM8lvdjMSD_DQskMZOdGfT_fEzxX-unQihgkGumnlfNOwm8wVuPuIGL65OFwBtDUVKryPYf-K7DYwVoCm9C80bHhUKObsGHbUdI_26aoF5LndSJT0ms_3Uaa9bq6Ezxq2J9YJe0XIt4v5KB-wiJPavMKA0X9B_Y0EGU4xEINHAJuq8lAlpGyY8NZwI-chsVjzK-_eMNCE91j39wY8pNDRLmRVZ_onDP_jLzX0uCi5nZhiZmNXrEiQgFXOFYCKEtRWfEAFdfjXaMXEYMB_etdEvK7_m2s74s97UE3_XmDB-3criKlbozXsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از همراهان کانال این را فرستاده و گفته:
پایین کانالتون شاهد خروج سفیانی هستیم
😁
سبحان الله راست میگوید این شیُ عجاب دیگر کیست؟!</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20214" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20213">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20213" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20212">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20212" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اقتصاد_ایران_ممکن_است_از_دوره_ریاست‌جمهوری_ترامپ_جان_سالم_به_در.pdf</div>
  <div class="tg-doc-extra">299.1 KB</div>
</div>
<a href="https://t.me/SBoxxx/20210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20210" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ونس:   کنجکاوم بدانم قالیباف چقدر در درک زبان انگلیسی خوب است</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20209" target="_blank">📅 00:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20208">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLHunHJ0Yw8AFjmBFXJ6bJmzxXtCDVyxpQJqEyNVJBJvjjlPQxX-RtWI_tRdcGvrk4v5Jm5XNo2B5kjCfaDGs7bANokQPPIFBAP6EU9CsIS2EKpFMkwB1xxUnuh61cGYIiyix0WsuKovj9D0LvABbe3XOITRaJRxzt5GjnSIjeh-AclmQBN_BPB421BScg7f4_TjmQzPQT0pR92mdS3cy0J4jyYT44MOsTDGJ7lqcCBJaLsLlWZNwy60c-Ol7SArSlJHvw-bmANcimSDRvfRBdXJrkk0Yt6pTS_Ej9CbI28U1GP7oz9MS3D0JpaTNfNdcnUOu7_MkKA2SjySIobDAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف در تمسخر اسکات بسنت</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/20208" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20207">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">باید بگویم خیلی خوشحالم که عمانی هم نیستم!
از یک طرف ترامپ می گوید آنها را بمباران خواهدکرد از یک طرف دیگر ایران می گوید که باید مسیر جنوبی را ببندد که البته خودش هم می گوید بدون نیاز به مجوز عمانی ها هم این کار را خودش کرده!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20207" target="_blank">📅 00:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20206">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">غریب‌آبادی: در تفاهم جدید عمان می‌پذیرد مسیر جنوبی را کاملا ببندد
البته درحال حاضر هم نیروهای مسلح ما اجازه عبور از مسیر جنوبی را نمی‌دهند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20206" target="_blank">📅 00:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20205">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کاظم خان امشب اساسی رو بای نفت است</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20205" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20204">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20204" target="_blank">📅 00:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20203">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">با این وضعیت می‌شود فهمید چرا ناگهانی تصمیم به دوبل کردن قیمت بنزین گرفته اند.  وقتی عرضه سقوط کند، کاهش تقاضا با جهش قیمت یک گزینه است.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20203" target="_blank">📅 00:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20202">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXqg9EW19C5eqJq5qIFpSgLawpheqGz1wXooBtiR1dY9ywfXvY_2U7Xs_yulUS8vl_RNXDCduLm4lKQHsN-RKTWVEImCzC8hKucOjr1elHxE19U2g8VrBSEUyFmqMC3TC3YnqljT4a_nokAF2rwykEA_ROFlWT2an2BjhXvUfi_b4iRA-BTbEYyD7_Bjn0FCmE85HW5sAb0ntrZ5i6N0d35QFytCxiN1N7cSSFoe0j5mP4X-djhVFhgovrYHXihTjauOC0w6sOGlhkd8Ogd2QWWRfpzo8mFhXTQWIl8h6nGseR0Bh1p8sY5zJKE--tmuNsnq8dCxrd2phjN_uNlUDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#Gasoline
— D
قیمت بنزین به نظر چنین مسیری داشته باشد.
کاملاً حرکت نزولی اصلاحی به نظر می رسد و تریگر آغاز چنین حرکتی می تواند زدن تاسیسات نفتی منطقه توسط سپاه باشد.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/20202" target="_blank">📅 21:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20201">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdmjLdXVVrhHmbcA1P5JM1jdyCMSbyKwTHPLF7VYdKxjziqU2yFaMwVmsT3A2ovgF29q4PfmUp9bbN9BPwLOJEDkj2x3nHXDsFvi_RhNie5oa14q7ywy_NvFY9757ys3fjhW0F5zNkoPTfl4kMbxjneku5GvLqwLDlIjIGKEPiVFshnR_-YNme32PrmlKvdnMd9KlhLPMQuoqYSRhfSrdbXU7qwKoHn7p1VZMire9qg5miyM4bKiai8ctMtgmmVoPRZ5BsNp7r9ykbmuhXIvLvEE5oDtr5JlaNG7Rzpe3Zlr-EKWR8CPbSWnfC3v_-ZrBZoNrhbNW2VNJqO-E2vUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اسکات بسنت وزیر خزانه داری آمریکا
رهبری ایران در حال اعتراف به شکست اقتصادی است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20201" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20200">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر جنگ اسرائیل: از سوریه خارج نمی‌شویم
کاتز: تا زمانی که تهدیدها علیه ما به قوت خود باقی باشد، ما از جبل الشیخ یا منطقه امنیتی در سوریه خارج نخواهیم شد.
ترکیه در تلاش است در سوریه مستقر شود و ما به همین دلیل وارد عمل شدیم؛ زیرا منافع امنیتی اسرائیل در معرض تهدید بود.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20200" target="_blank">📅 19:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20199">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ایران و عمان گفتند که پروژه‌ی مین‌روبی در تنگه هرمز را بحث کرده‌اند</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20199" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20198">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyqzU-ShGOhRdbYrAHSkh-xJuJGEz2JvSNZWlGzxVPRuosGxR6g6wHtKVEVrKiwmSS-d3ZmOpxuMUjlbixUHDwxzSAypPrZ3oDoTgDAedr_FCKDtBPVrJStnqSeBGo6sTaoDqPLx8QNeCaJ-fGMyyDHa0hzen79zTP6x-jMsybv1cR7mcP4fkakZBdljCA-vA1s7hZXuMx1T0ybKSkH6rg5XFzfPyY7rzKSEvCNB_q3HQO0iQxFVZjO-UtBi6BFhTy-4tI9QMr4UZV5zmrFnw7Rf2buUoe7IDU7hk3IcnQlikyVUnzXBzxVXQ8DPl6J2mxtim2v2CxzOaxzzxGxqEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تمام مین‌های دریایی که سپاه پیش‌تر در نقاط مختلف تنگه هرمز قرار داده بود منهدم و یا جمع‌آوری شدند.
همچنین وضعیت تنگه هرمز به صورت وجب به وجب تحت رصد ماهواره‌ای (نیروی فضایی ایالات متحده) قرار دارد و هر اقدامی در جهت مین‌گذاری مجدد با پاسخ ارتش این کشور مواجه خواهد شد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20198" target="_blank">📅 18:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20197">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Veeb3j1WsZRFpepljXA3Rj4OKS0QLBMAOcLEc5tNwRFhZS7fvEBKTumJG9DEshbleoPbIVeGuFr1PkZw6cz4iPJIbmDOlycjplmF9VNkKXNcDYnVoR596ya-XPDw4mMHixQZX3MlX0EZDrR0AbwZmjEJAJgmFJwJAw0uakIL8J626aNh-kgMk9pvbBC4uHbrI3tzpxpsEeMIgLvaHcgZGjJE0UQhhJCFLzXU4QQK970RBxHUOzHUGhPd15IYTG4nVoilLd7wleB70o79iIkT_V2jZnAcgOpWgPu3641XrRc2v_uyVT_8j2l3UpFDFOYnnKKIPHOr_NPc2zSiB0kAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عن این مفنگی را درآوردید!  ولش کنید دیگر بگذارید بمیرد.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20197" target="_blank">📅 17:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20196">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRKxqs-NTpLNRe4e9y7RZuNtzmv41ePYcRsVZzVS0IrUlhnGHMfWcDu5FbV3QVvGA6eTZfyHsrbSp5wwjiXXXyaLP2GGFbRvR8z-QA-aXBti5JFZAf4JMW_zhYBBpkVyogHNliswr4FSSBqK9c_M9xjaHeaU_cVxIX-nRtbIoDngXjc8vl0Mt3ULwtA56-2iRwFjSCR4ulYG5YakanR42qzVTWfVRq1kAr1o4vNRCLJUP1MoT5ZNrWRgnOdot2nXaP8L5WnJ5aJswpZrcIKuTbx1IVJBV2EDxurLQkTARlfs-0YFBsR_W7epjd02LuXwGLVdeNmF0M8Jna-1A84LpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
«جمهوری اسلامی ایران که در حال فروپاشی است، بخش‌های بزرگی از نیروهای نظامی خود را حقوق نمی‌دهد و هم‌زمان، در سطحی بی‌سابقه اقدام به کشتن معترضان می‌کند؛ حتی افرادی که در حال اعتراض نیستند.
این یک بحران انسانی با ابعادی بی‌سابقه است و باید همین حالا متوقف شود.</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20196" target="_blank">📅 15:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20195">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لحظه ای که روسیه ضد اوکراین سلاح هسته ای استفاده کند، آمریکا هم ایران را با هسته ای خواهدزد.  شاید هم اول آمریکا بزند.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20195" target="_blank">📅 14:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20194">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حالا اگر تصویر میکنید که یک فروند ناصر همتی میتواند جلوی این روند ژئوپولیتیکی را بگیرد که ولی خب.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20194" target="_blank">📅 13:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20193">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبلومبرگ فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw0dIN6PcD7zzcF5XEzxiL_WTVCMyEWiMxkd-EXdQifvbQwNqWUmTtyDYMr6_hqL15Yoi14Oj-bS2Drp32a2O5YxLwPPWWhK8Mv71SBz4CsZJUWyHILwLtiK4bz4svsh7TPML3LcVEwGrdNpeNaehfAy-rO19e5dzPKY_DJL-8AbaF3-gPMevLHLmn2-w9ZA80sXC21DW2ImNbRycSg-VqO78oxZZTImE-6F_IPfsDI5QG-fyVxnJnjXu_5_fVnFmoxBN41sV5ZJrOQ60OSh2Li5NOXfEluEGfyfHSrSboEhNtKLrMwB1m8yssTLbTGWFyhIRTRXyQqim2cgE6p4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای همتی از زمان دلار ۳٠ تومانی تا امروز که دلار ۲٠٠ تومان را پشت سر گذاشت به آینده اقتصاد خوش‌بین است
☑️
@persiannbloomberg
بلومبرگ فارسی
✔️</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20193" target="_blank">📅 13:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20192">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIvZ18q4LtXUjtRkwoWwiEixRKjrrKNgu3Z0If3W-LY7-tosnupwcfy0bIHkCT5B41e7LxY9j0OzqNs4BSHj0N-DZjV1VT4Y0nQy73SUEFX8hN3_bEkyXd80BWb0HOR5ELBvlgqTU4IvNT2r6ac_8m__KkTKVMEDSq5Yv8r2BXONckz-4nQjWnmLjfol0tvUptivrbPT6fhhefIB1WgVkKdLD2wdYPInVaDbLnPDImfTmepCmRovKDf7nkXT1Es3epGErgz4tfI0Cea679CVay70IGfAWWf9dz2JGQxZcgM9LLpI7BG8snAdD-wbGpEYMrvTSJPctAJSVXE8OOV6Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادغام شبکه خبر و اینترنشنال</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/20192" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20191">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چرند.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20191" target="_blank">📅 12:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20190">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:   آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20190" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20189">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک منبع مطلع در خبرگزاری العربیه:
آمریکا پیشنهاد کرده است که در ازای باز شدن تنگه هرمز و توقف حملات توسط عوامل، محاصره را متوقف کرده و تحریم‌ها را رفع کند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20189" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20188">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVSA_nvh8INCZl8BUQoOXD0sppf5oo14Ood4Z1fzwWO1xZjokCPOqrPGIJtbN3vISEOrQwffU0uf4juyq3SkZLNYv2JAysHzdMPyvoCWSi1da4uNNUORIEw9jPA3qzAkewh5vGZEdHe32iMebKi-VkMabhg2WauRKd0gSTnYn5H192X65vNQMgP3YrmTZlbicrUtI9VujYyfo0R2353bZqsxJOHJY6Zxg4_mOw4EQxD5tWxqSdTp66y0Q0MGo0VP8DBJGc6uNjmXaLdf-cLdUiYh1LWS1iiGcxKD0ueRHeoD90bOo-L23FORSLf7gdcdCEFJuFtL-0g_wGavr0b0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز هم بسیار بالاست و پیش بینی می شود شاخص نزدک افت داشته باشد.
طلا هم با این وضعیت قاعدتاً امروز باید به افت خود ادامه بدهد.
دقت کنید که سقف دیشب عملاً جعلی بود و بعد از ثبت آن حدود 800 پیپ افت داشت.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20188" target="_blank">📅 11:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20187">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2PokbD8qqxMN8fHCJvVnWcGQs8plxEHqNiE27dOVqcTw6CTeHHBwHn3viqcFLjp1TW3EDt8Tp1q3TsfeSY5iX4DyruNbIk5RDBrQjPMkXRMgvWDngtqbf7NbC6Ia1GYyfoIq5h8XC2DKsbWsEf7t5sGr_VpkCnruDwP0BDDwtVrbSZr_jbDry03oiuJWAysvWbwUMk_6TyrHDOKORZ3zdu-NcwkJ-_s9lh7m20AEdAsyV4V-DksuaTGvxF8po1aBqB-0W_P2pelwVKb1q-jNlQiPAYBlJ2jmxWrftU8f5LTuhrDDFdpp_XiNfoUstMm4fW5pHW0tI8GPvUhrM4CLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج 2 نفت دارد تمام می شود.  موج اصلاحی دلار به ریال هم قاعدتاً باید آغاز بشود با تارگت 240 به بالا.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/20187" target="_blank">📅 10:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20186">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmqtN_m6NMdbUOicS-79H_pyxq0EbTMC7XIjyfLC0Ei9oPaQTPobvGZlW0lYx3eiaGz7Jvxe_vHnrLAJj73wsH9fI84p7ptnydIZ1j_6ghLpCKvyGhxxSCoFZm7eNgclsXS3H6suvnYHM_ytYOz9YhTlPPivO3IMkAjwhkWRfwxVemmRhxs04F7S0GKvJcQXKxR3CB32U54XtECLIBcO5Smh9dyLgvXU25I2JWcmwRBkbPbEXHt8hSOGDy4DGNauyqGyZaPOXX8woNfaY4t0BiAi5OHkJdbh5aMrfhxjFGQDYFlM72oYZoB_DQl66aUpV62VyAYAMVUdm6pDQaA7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بسته جدید بسنت سروصدایش بیشتر از تاثیرش خواهدبود.  چین اگر بخواهد — که به نظرم می خواهد — به هر قمیتی از سقوط کامل اقتصاد ایران جلو میگیرد و همه ابزارهایش را هم دارد که اینجا اشاره کردم.  کالاهای موردنیاز ایران را کماکان تا جای امکان صادر می کند و پولی…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20186" target="_blank">📅 03:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20185">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibr_OpE7Kv3TfQJ6fyxQQi5xnB02Y9TVScpfhQqV4FTyn8YGeuDIeOrIbHbVKJJx_7pywgmq6MgE6IomMEi7Bx_MzU7hsWHJm1pySzDi0VJnr-XIuzW1Blb9jP9iPMbpfesuji6O6ked2Mxz7AEpvG_SrbGtJyyLPLyUIMSuvRZ0W2zrfQYAjYdvLKaAbSbs9lh-Dw3YVIV5_AQCN2DzMysAAD_7mflHe-GMCOWQsumfIH4zIdIAWdyO9kokXL4vVr3nTGLaNdlkYlTDM0azKd3mGlpOnFr1z3dDSJbczFwXtP6_bAlf4Iez2XbVk2fQOOuT0GcQm0yfaLlaTFqa5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار بالایی قرار دارد.  دقت کنید که با آغاز برنامه بازخرید اوراق قرضه بلندمدت خزانه داری آمریکا، یک عامل جدید وارد محاسبات شده که در این شاخص هنوز آن را دخیل نکرده ایم که روی طلا موثر است.   ولی با این حال، پیش…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20185" target="_blank">📅 03:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20184">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فرمانده انتظامی کل کشور در ساری:  جنگ سوم هنوز تمام نشده لذا باید با آمادگی کامل در برابر دشمن، غافگیر نشویم، چرا که خیلی از غافلگیری‌ها نتیجه غفلت بوده و دشمن از ما دست برنداشته و جایی از ما دست بر می دارد که ما دست برتر داشته باشیم.   دشمن به‌دنبال ایجاد…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20184" target="_blank">📅 01:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20183">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تحلیل عوامل سیاسی چرایی شتاب شدید رالی اخیر دلار</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20183" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20182">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=VmKLcxhp0QZsqPgvghXwPrVxC-8GqyQWzS-3xVPNC5w7m4evOJuOf3-n2yehxV3QeU3uguA7Dooy5zv0ZBdjr_WJW7fmio7FhHfV2UYCLTlrIQgvt1sJ42EupYLbkG5qFqzoyhNAB6uprwJWLzZR9g1g8D_qyk8jlWml8VBePqw0eUUcf_jN8yDfEY5QGvxhE5I8dJS6OwrR332aWYeOujiafrlzJD1yNTZ3459euyLPWjcPCOoBh3FnEaDuW8g8uCiuD70xDmDIAJVOTe_0qPr3_Sy-fb14cB-OlBj4612zVlh4_jnCCWsvsFkcDE2byVWjTNGhG5hAvpFYs5UmRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313a4a00f6.mp4?token=VmKLcxhp0QZsqPgvghXwPrVxC-8GqyQWzS-3xVPNC5w7m4evOJuOf3-n2yehxV3QeU3uguA7Dooy5zv0ZBdjr_WJW7fmio7FhHfV2UYCLTlrIQgvt1sJ42EupYLbkG5qFqzoyhNAB6uprwJWLzZR9g1g8D_qyk8jlWml8VBePqw0eUUcf_jN8yDfEY5QGvxhE5I8dJS6OwrR332aWYeOujiafrlzJD1yNTZ3459euyLPWjcPCOoBh3FnEaDuW8g8uCiuD70xDmDIAJVOTe_0qPr3_Sy-fb14cB-OlBj4612zVlh4_jnCCWsvsFkcDE2byVWjTNGhG5hAvpFYs5UmRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های امشب محسن رضایی دیگر قطعی کرد که جمهوری اسلامی به دنبال زدن چاه ها و تاسیسات نفتی منطقه و نیز خط لوله های جایگزینی است که از سوی عرب ها و ترک ها دارد ساخته می شود.  منتظر نفت 130 دلاری باشید.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20182" target="_blank">📅 01:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20181">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کری خوانی وزیر خزانه داری آمریکا برای عبدالناصر همتی:   به زودی دلار 300 هزار تومانی تحویلت می دهم</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20181" target="_blank">📅 01:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20180">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc_ASv5AqbAwEr_JMag1xO2cwxwR6Tv2PyQnd1DsUTS6Ua0SQrZ8M22JDqONfNb5QtBiMHcpjeGsKD8ydMAgWgXUtGVXloL2QPsEi1nuCi-3b3UbAbP4hipHno3b92w8en7mmlc5xsc7N7RM27Gyf43U3tep1O2_VgZmzhoNUgOEIgMGBGshBCNi4j3b6OV7oyEnIk2kliKKyV7rko7-656ziHB-pKkz52TLzXHk5ANcyriCPDWb0Q6Mmz2JrXXHmcTww0AsZYYyOlPH6QzNEwKreKtJF87giozdJc5Z3G7gpXQT1rl6wss7Cy8tB8uc08e9OFxt6GBtIgFyKfR6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر نفت خام آمریکا به سطحی پایین رسیده است که از دهه ۱۹۷۰ شاهد آن نبوده‌ایم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20180" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20179">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20179" target="_blank">📅 23:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20178">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ6q-AkBUx4I0y3F2V_ZNGL06eWie8OxsHmAp6afm2KGCLcJAKGOQ5nHbGvjwiboN8L2O85yOyBDYsUxi58uwM-p4EJtvJ5-VRAn2v3d783_j_huzgSFnHb_D6vw0fNjNYKKQJd_REPtVFsRhZnDP_uuySbjKXo8J5pUJOdDtzAvmUePcScNdKNdQ3ZkpQue-uUXbI1qkvLYWAl-P3U0DliDpv3zA0QLfwugV0IK-fj2IjwHkvyq3GrvQiT-uuKKcLTLHff01vX76dzo8ulab5VS_UF8AtZKITi8LnbJBNewdbRL9yPKepATOehvkFWTR1qWRuUAanjROaUSvUmK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده:  «امروز، وزارت خزانه‌داری ایالات متحده عملیات طرد اقتصادی، یک کمپین بی‌سابقه علیه جمهوری اسلامی ایران را آغاز کرده است.  ما در حال آغاز یک حمله اقتصادی علیه ارتباطات مالی ایران در سراسر جهان هستیم. هدف ما قطع هرگونه…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SBoxxx/20178" target="_blank">📅 23:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20177">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">— اسکات بسنت، وزیر خزانه‌داری ایالات متحده، درباره‌ی چین:  «ما می‌خواهیم امروز اینجا روشن کنیم که هیچ‌کس فراتر از دسترس تحریم‌های ایالات متحده نیست.  اگر آن‌ها تسهیل‌گر معاملات باشند و بخشی از اکوسیستمی باشند که نفت ایران را به پول و سرکوب تبدیل می‌کند، هدف…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20177" target="_blank">📅 21:57 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
