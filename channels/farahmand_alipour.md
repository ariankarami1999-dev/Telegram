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
<img src="https://cdn4.telesco.pe/file/UGrTOBhuWzgOww0wXNEREE5BjVRiLPYFKvrvgDLUziz46mHJSGeuuPqkaGPQ_oKyab-gueii-mR-MpVg9nudsQyMrhY2ccggKL1HVOUmt6we3D6ZKsym2BO4B-Oa8FBcTHNLxNM3vU-YX9r77PYHLJ_RUwd3x4Ee8o6rjJISRJay-zYpBjOfUkF8nJrti_78iHuSH3y6zaGf1xy6kfTYRhqrgcayfChYNJlCt2PgooL6PMl2yyxC0Ks-6SL4WZvPe8X1vMii7IB8FdBAbjiuJrXkgTCoN3YyeAfHvqiCwI1Yc-FFi9zgR2Pcvn7Q-uaunI5pVhWoa0xXVAvqxJZu_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 22:38:16</div>
<hr>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وحید اشتریان، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=UXWRm7lYHpYCw1qyAzHoH9RpGZg0HjFgdm8Q1kds-ms3j-nRfwtgDZXcfonmTD7g6owXxChLzeQwDUA59NS_vE-mxipovnL2q6pNqPjqjkTiFX6GLK0-OczdSTp8YLYn1dtMC_ZKH8KbE6tzQUkPhKP_Vs_i5dipAu5elZkl7_tl3sI8ixpk4IUz_FiowCHCC5ynH1vflJ1HToS-R8bDSfMXuBY_TxmRERE00Lq-_NipJVwv_H720p27mV8vqC0v17o6dDEUxD5wTkxtWFF0Ccna0UgMsYBSwss8KjxzJwSqqEcm8mlPeGFzeuQjS2Mvo7nCXanZ6JwtBlJCPC7h0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-CMETcUc6r3II7t4-ot8tUzi7rgzXrmB5n_IBtuOJi7h_gmadMcLHlPTxgBgb825hnhkGL1gqKBJdSY8m9MSR3bZwNQPbYUXSra5B17mlc3A2DO5_WxmQO6lukzYfK4yxIICB4GIZO3sikuyD1vIuO93_5Ik-kHl3pkOD14jqNyvjEMJIQdH0pw_FEdu7bmOuF5kYoSPaN2iFUp8OvFdaP86bEXN7Xj2gQQppxAhRTxtXJNahBHbQ8Rp0ozC3ClRbLhmNe8eNEKM4kZFjOWBZNPjSVUq1deOGeyWXq4v1t64Ft2ofTCh6ANPNZxTKEbcaIkzEDpbRFbnaw4-e2ktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfXv39ugSjEHvm5gEjzri-MRjsw55eFIY6fHEtU1o1sHSBmz0vrukcl8UyGAiY2rX-m1DJH9kBHqtDCmMflMXK5kdE5-HigEG6F_SY4RxOrJDpo6bZ45q2VhftAkY-PwTaO6Vp2h0LIVkUULM6Fb4y2nCJ4Rrp1Z0gXw4Jj6EELuIPCD-Tko0jpH_AmYheawOxt6g9O2WV5lMOw2hmDdiwWmLmNyI37SH3llvQkNDiIe4JijY8eBsJdefSgoxzXtTmrHL_nj_joClfuyDQJIPbGfZ6IaTAV7WDcQd5H2FlWSg7Q8C6ObD6hywuFXzpPTH7OeCekzdH-Cx58ectm2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbyTtCMPT-IgwUAZUZLTSBccqB8S8jZ5C3Bzwei1BUAsr6XToSaptBGg98dz-VlL3VaWnTj5c9PFVjRexJW6mX6r5vtxmAkiPS9H0r9F8kdVkK5gLfG0OR2m3xYPz5CXRvJ4EyjTfMApF_ogmSV1XTYYZu5vzAbx3Jy6urzbS2fqy2m3_q5kyHqNmBuTxWeRqk8LXIUgrlfV5aPk-3BPrKMb3KpnMBbYq-fDmO-pekDH1kp2DeDbjK2pUaqzIRl5FJgy9wcEbYMvcn2hJOWI8-hx5DhWUeyPs3KPkXCHCRce_ugtH6rMvH-GNwlSGVdWyar5WBJmnlj9YbsvYA3isw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=uaYyv8daaW-2OgmvzFIGpqMIDH_00-NHrDSTQKY2Fppf17qLRsy2c6LIMRh3XjQF0Owr3fkNGd1_Elg3CECjf03RS2rsyZDzFVOTFT3qW257LyolwldN1CVQLaNGEYLXnArSa4An2Ii6NGSTUXesjGFWqqN_NNO62GIdE6XwmbfKtSXgv5IeRQCYAr85Tbw4-ssA7ECrKufQwY5BUznEcy_vojx8r29O64NEN1uPA_xDRmuw-InNmb0rUDoz2xVlPy0g0bJjGLhVyhlIcXZkFitwZYIxWkN6nDMgstRzrtKaWQibj0rdlq_nyiItX2wC1GZWllU_Vy4y5ais39dN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=uaYyv8daaW-2OgmvzFIGpqMIDH_00-NHrDSTQKY2Fppf17qLRsy2c6LIMRh3XjQF0Owr3fkNGd1_Elg3CECjf03RS2rsyZDzFVOTFT3qW257LyolwldN1CVQLaNGEYLXnArSa4An2Ii6NGSTUXesjGFWqqN_NNO62GIdE6XwmbfKtSXgv5IeRQCYAr85Tbw4-ssA7ECrKufQwY5BUznEcy_vojx8r29O64NEN1uPA_xDRmuw-InNmb0rUDoz2xVlPy0g0bJjGLhVyhlIcXZkFitwZYIxWkN6nDMgstRzrtKaWQibj0rdlq_nyiItX2wC1GZWllU_Vy4y5ais39dN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs2PsAHxgsIzSuTUkxuvBA3rNX2fpAQhlOfIKqHxbNkSEHa-KTOHl3CAMNwEdwhU0e65CnJVeGpLCAaC2bL9u7wrFS5jjAWdc2UK1BvQ1SeQg_CqR54w6LCFCHvVhkre1okm3JV-7ld_Y3uIgsRmYhE650_eUuwS9uy0ypAavWPPQ9B2uDwVaHvneBezH-N3E9LothbhpAdNetPharzqmgQ9mXuZTM2ydOSi6ZkcTZ0pEYZSd_8ssCboVWp_3d39v4iFRwcvSVMJj7DRPrsDHWQUhAiY2FqGz4lAEo_c66Gabo04dy_aVVt0t9D_EfhGqGpSlX64Enjb299tJNcFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR-cqyRh_cCZkHhGS97QlBz2tGbpbRBqyJ8glo0FWImVX8Q4F91UZL5prrRymYW4VvzT6Kly_dDPfvg3ilax0KEo6xsPly5LNkIULqpLddIyZmFcSGP-lhx0wqjzkoyz81aeCYdjoXF7h7ZFJZ7eWZhRDqN7--QRWx08FuuGQj6QDHPXXziFcsFm2XQ9h3rwLc0dVnAHVjrzJdBHaH6TKtXyf5_f5B6JPw3HQcEy3UzdVgF46q3iN7UrCgkFgsP3uAOPrsB2QQcFITU8j_INMUBtLPMOYFwBa-D3N9NtJIBgjVWragIDIxzKLi_SGp8OAnf__ZD90DO1Da1ZPmq3Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r65_cUMVECRh1d_kX9m8b7VQ0FZmDfcKjK5LsxSJDbvxHVp5xnYLKbeowLxfnN1TP8Im_mqoLpJkqLYkiQVBqM3GLdgd4iJJ-NJDgn0ZsSdo2fsakhBlvVnfI862S-zi1kWLoGe-xCe0YhQLYdCoes_jWGYN8dvH3lV3PhVnD2d3-vmdFEVO1Qjg8eGhBmeew8YDn2JCZ2m88iTbZLu2zI87dlLKDFjSdfoB-B00V3poqMiinoXrZ9ej_lJaaMkHyCNpihs3nT_PfmFbiyHpxISRFAdpcxHFXmAdXp0ULkmpgwd_kG1eNBm2gu3ADaJW0KDnI9h3O4PyiZLz8k4Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCENO7HAwxe5xWLgQqaGtApjF5C5lSXuTD6BcEOBtv0jNtqL3ZFZD6gTn2NtmIlIeGqR2Tjycio2kLkyS7CnZtVu7sVt13hoMPRntN5l64tUiKCw9LtowPte8fEjjD6sin6S5nGgUYufdBb2bbXR2O-iFfO-1qBZ5v22Nc2AAhDFLjrY8-tOOPPbGKE0Ma3YVmOsvk9_K3UjsNOU14Q5AFPIkr6g0Xz1JU4iKHtU5W_Y4qCA1RUn6LONpIrY-wNOozCupy0cB0iV0bFjKaSX1T_OxvxSeWxjoSM4L8yTHfdFT1KlMkZinE6kOwbVjKJKoBc51OSxgcH5pLoaosCcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=QaS_ZJN2tWAeOBCj6avsuO-47reSTC883ZAPruBJYv0pa6VatWIk8ynqO7mxVtKSsxnlIHHG1bZBCguObqAym7isX6vxgPamCHy7d4L9CADmtEF30grBPB2goXDpvxrHPJbhFfE8RS1jG92rHiw-K844PZR8TdmoTuNnI3gfxYYVZSlazWA6h8NzvxDS5kldLaYPLEOkK-hM8s48ihU13YwECzUAyZ1j2DN7Oy3EV0Da_9kgk4m1Q3eZQBvV0q4mW7gcdpIZTxmkl1_qSXWk7sJlWzDV1h19AU_hleTHb8rFm8zqY14wjhRTi-MuUcgy3Wa7CG4i4sl_Fd5zAR-OMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNzC_EHdaJpPMhkbbDDzh3HcJR8r3Ue0SpkoS7_EvI8qJHoutX7yYxxrdVoz_278HGKLKh3JMer7dt8w6AYVrFLSE_kdBOhp-pXjxdqLxWaF3gCHNResanUTzKGP7JP3XTMzk0kombnH16nL9LH_MBKWKTP0xKCvBmUrtPSNWSv_w-hUALDeQmkktBM-zizbQSES-IDEu35zsvCgOEc2Q6njW5qkPyZ_dqMYU6ZHeVsxSsCrVqL1Rt8jgPNd_iBVe2lF7a_Kax_w6bSt8vSvGT4OvEeF5iC2Gztb7rpsIcol3hDOL35oO3vw_w6GJ5RxQsMzG0vEsk24KaBgCbNfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBZn9xG00ukVt-Zwp-SzpyrLM5t6WksgFugTcqmyzQXHQ9-1r-WjXLXhV3V9fcnRnYjLHY2RT7l4gW3SRTePhzDz9XudcS9L4csiBN3D6taPQvYXpTcYXVHh-f_hyzWunEDkBwIX7ZoQ9ooSFnueERu0Eu9-foE7oZ2_PvNGB43MavM80WV8GoBDqfWNK0ljZSrwF8K1kD0USDwVKH8pSMLnAjN-WNEwj3alHWfbf09-3kqYbfE-JpAu8JsDA_YC_j-Z4F8Fs5eszZkoO8HIuLMnF2tqgCN3R_J93U-YuOUuSCbyKUECz3u5CIN7g10jBP9OUE_ymbTPgnb9ZxaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZeYh9RPtt8JT0oV05Krm6lQKse0sDn_VbsiLgusg5UJq7DLfgfvaO5DDXBQlVhPXjlMKV1zwjh8f9sqoKU28GzsB43QIYDpxpTJ0e0g-KrtHHhGS4692cNY6hU0e4x2iwC2T8MP9Bc8nb4mtxanQfjCtlht9UuMqRv_ynJipik5D4GgMNpaoQP_Ctq3ZFL4DpjdQJXZKYEfWK81xvCSye8Fer2WIZME9s9zGIwVPkT0Y0zjQFfxA5IloeqiV33Wi0Crvmt31e3H3ROTSHrl8HBryESJBwAU6jJfnYAAmNkR0jIQUB4C3TzKXOW-UabBhSWAIMjUBi-s25V_fnufYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=huWxXYw9OPFUt6Id_4Ov3XoJAn4h282ddcXKjwp88aERGY1irvZiwKUNo8AeVnBJpUJaZs6xWH_V-1BPINez7UoVWXW5Uqjt3JtDSkVFhuBtrOgsuhHgGox-ckczAzYNC0h5cSUckIsx65jLzf7xauFUQGpESL0vuUo5hRM--OUaJyQWz_2-kBu_q0taWTXJ0-hb39cDuWnt9K_i0BCZr7WWS0rUmLo2XPOoWnL1IvdosQJEFamMKPuWQl_hlbBpW2v4Bv--W_n6YUWziE7HTKeSw3_mhH5AAWaxnu4JgQyg2X8xcsN2AUQUO1hW-O-XxhLJg6McVp6Ix3ORchE_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K6Zf2KpWDsTScUGf8J1m-heHOOKfO1AScVLqlmZ0qO99qhhHiXAUpbAYIlusTbwhAnVccgpmXxyCzCR3hCF4DHlTFAY9qjewju3Wvtl5qELMXXIyFBVXGbFV05qxU8U53lIyBgii5CzYZzgIR7i11aSs4Bh-mfSKQrQNzhrMtZ802eYlmt1vd_HoSlkRbF-CxXWhgH9kdtqn2kOlefSehGHENf2sqDCfgX21sYRjbdxE5W5M2n8FcdH_laMnz7aZX8NibCE4x8OOruS5zyFVEuX06bO1GBtCRzpT4b918Gy09wWH7VYVVo4pcfKnAUXVnkG7eTdm2s6HDmCTojLAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=K6Zf2KpWDsTScUGf8J1m-heHOOKfO1AScVLqlmZ0qO99qhhHiXAUpbAYIlusTbwhAnVccgpmXxyCzCR3hCF4DHlTFAY9qjewju3Wvtl5qELMXXIyFBVXGbFV05qxU8U53lIyBgii5CzYZzgIR7i11aSs4Bh-mfSKQrQNzhrMtZ802eYlmt1vd_HoSlkRbF-CxXWhgH9kdtqn2kOlefSehGHENf2sqDCfgX21sYRjbdxE5W5M2n8FcdH_laMnz7aZX8NibCE4x8OOruS5zyFVEuX06bO1GBtCRzpT4b918Gy09wWH7VYVVo4pcfKnAUXVnkG7eTdm2s6HDmCTojLAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IZyW1Tjmq5ZJQP3eHdCmajmYLVTOGlEvzYdRScYT5GYQaPep67WOuDeaDqQV7OxcGij2haTRCSeYTLFBCvLA9Bwn61cDersfXkLRmBSkwr1aSkDZk2j5a_EZAWiLvNCq7eOxe2BaiXnQKj3oFY-FT7TjukTWeb1iHbUAsPXKdQcW9C7GoOXP2n70xxdhRmNsYN7UI0on7YfQVOVEidP1KmvgsJliRbNgaLj9kZe-C9M7pKn52I7a1VgMZm_ueRg2SGQX8WqGHmCU2gwxedghNK9-YOohNyAsfa1mL6t2UuffPviS-nXtBMcZKydwASRnQrvQYuyyO-Kf8zQgvsQqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=IZyW1Tjmq5ZJQP3eHdCmajmYLVTOGlEvzYdRScYT5GYQaPep67WOuDeaDqQV7OxcGij2haTRCSeYTLFBCvLA9Bwn61cDersfXkLRmBSkwr1aSkDZk2j5a_EZAWiLvNCq7eOxe2BaiXnQKj3oFY-FT7TjukTWeb1iHbUAsPXKdQcW9C7GoOXP2n70xxdhRmNsYN7UI0on7YfQVOVEidP1KmvgsJliRbNgaLj9kZe-C9M7pKn52I7a1VgMZm_ueRg2SGQX8WqGHmCU2gwxedghNK9-YOohNyAsfa1mL6t2UuffPviS-nXtBMcZKydwASRnQrvQYuyyO-Kf8zQgvsQqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP12R7IrQ9SpHAjPJWzcSi2Z1Kqe88ADG2ug6tXVV_6S2E3R7YMSw7caK5cPBagACfbBrAvog5039vA2g3MyliZF_nlg-qdY-Leol4kT1dnTOVvBAXbhlazJZCtF42ohRvOmFIQNrG75QHFk0mCZoP96QsI7aHVCDwjuJbcMPO3GYv8evYY1zWm4bapfYwjNvgib8ci0-jn2tNKsoMWXs8Z4oa_b9L3h-KHqn85yyfh7HnQnfmh37wJRmJclzjxm1OiETqcH_rVNPhVW1AtCjrXnCaYmiavQsBwBqV3h79Poz8rv6Zlc_7YnezJqJF74hsDN6lV3ejDyJNt1PNbrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qC418qRcKw92-FaMy1vbJ0qmZJSGRxVhu0bb2Re6qWQl_hWad0LXt-JlkaUrRML10geWf2LGnNmpS5yuqwXHZjAlOBIcR7S6gVSxQ02ksbaqxU-iynHliyohGAxUNWLkuLY_kZmI5NsdCJZlEthWr2QXsHp1-X1h1Lc0wYVuBTpP2ukNVSTjJXsNSeaDIwAqhgXShwheitw5uTwGNBB0noM0DC_gjYiaTen13nF1n1jRsJCdV-UFivVphHKZsaAT8I4t3-fCcUZMqt7BywD6xOclIfMO-fskZPXxhOtTf8NyH0mtmpi1vxFLw4Aul076LNLRAcuBnOzmEtkCSpzKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9WsK6mM6FDYwL6c9T6XMyGLYW1hx947FmWK2ZsGZwbi_11ny8ndq2zz7s3eua1XEH0YJZgWtkGEGrWndCumhxM9fzuXFja6Z_d6eNCT85DG6tSUctSIKdD7PvYbEOW7UNMmsozbeyxEMy-DHzq_nkeerZxy_lFMpADRp1mADZW3c9JMaPL_l9vBb8VIt8VmUZXoKcjXzlYIWzEB3VTYDE3bJ_JzxLOEAOwTVNyf7dzudy9hBFXWyHRoJKE5hFCDrJD1E8Fh8-JvEeBFvXc3w2wJT2xA5q-4lY5bqQj0YHWIORD6VHS09HqMnUB4La3RtLV8_8CJYzTAm09Rsqu71w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cttoojcoSiYXx9MfuaFQILFNLqqy76kyxHxMuzkcCQdyEeiKSnFiEf63VoLPi7AVm7UrQ-PHcQUyQZMmp6INvsSBYfYTVUVUcHboJQOBo-9dHhc9jP182ETz0NUGY4avXbl2_8n_pPjntyCg82rj-PIBZMXsAxHFQB2WiIajzwJdybi-_1BVOt49o9CFlD_6R_j6vSvFn4HaFuSlxiGiVI2V6R5fXB2Xr3tyf3OzKeBtIUQ1K_lFzpLbs93Sa9BGA-WnCwUpvkw6z9D4n_EQcaqHWoue4OqV6dkCZZY646FcVfKTT0nbsQuoe1bdZ29STH-hxlh3eBEaYt6T7ygL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqqjVy40McybRWo99TVR7ExDiS7iiPIpVhzO1pzRqpPgrKe-ofiZtx3Sig7wAgjOK96jnVIcYuBQ6BOHENT17znKb4rv2Ilyvc2GoU57OOJa-yfaHTXbgWYCgrdZFIimIzMwJwjzG33fHK21e6otuUajkaEdKdTgzHiZ-R0GlLVTdPY0MrJq7Odtbqw4PjnIf4KFP_BxPKVMX1P_dENU5ktLjZaT6c0Gicr6cEGTsV9BqNnrDM-ZWjm3BvDTUs_ONwmis7BOOSYYPpQBAHKbo_lEjjs8BbZve_rn9Ts8ou8w207RLrJWjvhKask2LbnjW7fLDst4JaeYgh6cx6NKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_R_YRsyMrs12jxk8kITv7wj-7ODSZu2wMhxuF-PsPdHbH_6I80z_VzIU5F0DMnQzeVkHKksYkcM9nH2mOLGNOSZl8sz8yFCs1tT5Mqb6wHLUGZtfgSXfTMbWGxQonFOUJshL_omTbDLK5Ox5UouH5UpaRufwVE2R0yxnt52EJmaLeEtyRPJrXWOTRFLHdA6O02M06Mt367iZW1_mtkyXlgTEtoKyckcqhOrjBbtHw3FzCu_OCxvzulzqm--ix7XBWbTabozdAgmEz_f-IPKvkqT6hAepdgSDtXtW7N9e-Gdk7wk1FE_G9xP4QZ355Cxko3RGtbL0QgFX1gAbmUEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4oZkCkGASr6Sy2Qqh-Hlj3uXtFdXQ3M1EIWE17dxiiyVQVTKZ7rV7TFyrAaa29zKaUlzmJDVr2WtpqOk6WPp2fx55pk32-PobdO_1pkBNdsCEk0sPYGcAPgteog9N7YLDXkAMP9onH5nj0ssmbXwMK2rkN_oe0bRePRTBtVILDYwCepaCtl07azW-ueBoDZm44oQVI7JXVwU8_DBj531Dhx_S2eN1LUAvC3ov-kuZrPIUhKF1W_d65kE1oX-JbNzHDoFFTnPZ2BkK8JOBMjL-lTMGoxDDjy7WihMtSaNAg6X0FGJx5qJEiG09RP5HTTNi1krxjuXYWE09xWkquC6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfgJzCWDq66HFgaqdh9OVwNeHwqgVQt4pBIdM7ljrHrUSzORKyyPNT7Bt-6PsOhEtsr_61r0cSYyW6NorNavO-oBOpe-h6ZMrHSVnu6I0Yn79C1RJqWY7hl7gQpwbA1qtfKRS7nn4lDJibO2pt_gj3UqfdXf_Sqp1HZEASIwA7LhF6p9LIDRbQY4XFBo5DPhxQoWitaLyOYcxAiZ8Jxg5AZit_nuKQsMabL68h9NN1fpVWotcTt-mD8zPFvO-uGbOCmll4PY99SbMOrseLjqLF4vJ67a8TQ8Fze5ntX9WV1RcrzpftY7IghgA0-U5MyDsmEq8zL8MV2unh4H_LPuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObgEMBSQ3SY4C4wB4M39-2SHE8J8-AgzHNHMxlcL1KsRsoJe7wWLH9Sii-PXtF25tkZsjG5JuOm8AEhEC0YebhAW-9iHkXyXi8QDzMgock6RoXiYqBTNlKgY2MyF5kAUfj6eUt-DnADYLELHb3KsUaFCYztouVkQns9-l3wO7uOKfL_5FF99vlme02krJQEUL-6BJMqJGp9VM83lwNOHIYkn-J-z7O6JPWIgqPVpcso9ej8vGhPGIpOWKwHvGs01idrlyCnrw3QzoUY2L_2qpXT0f2FFvXyP7ZYho_1Lhi0P0ftERgtx8Y8r1cEbsL61WuUejRy42t_N9mJwwjP_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgy60DIFS2hyVX7AV4Q0rpf7FP0VQp-ZuqvII0FrcbGWmtyuGJ-0_XVubvsaERcjfztLQQ_czcUhb-zlSyfTE5YfwvUUiIILA_LfBhSIXspFGz8E2pgd609L7lSBD0Rilu44d6Q9ITumw4nuYMVmxEedxvtZV0v47iiqLwWt1boUgwcKd43kme-W6LNt_mXG_h2g8TiyZ98bpnT7oo5_zdru02V1XwSPGIyQmYAAvL7LJEqqN0epPiyagfFKhBAc0SQ2wcfYfqAKZcRSazedhJTGhivnVyPoo3Zw35mGo3hlps8HCn3PnG0VlbuLdMzT41_ExNCmF3QLo397CEhCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5E1Z5uvKIchk8_lfm4WDQdkqJ33i3Bi6ZGziXCik4y8xJWKpCB6lAHRUTsqf_fb5I6rRJ7fhIdkPxYyFI3_hIH3olTweP451FKs5eZeSxDLsfBq1eQvCksELbkefNsjqM8JcAR4ZCFUE9FAUprBjFutYYvC5upV2t3e_XoT2xcmunDQR00kop3GfxRQW0IcAevrayb3IczcRYcHsF8UN-_IBzAIsB3tLLEn7BTI7qOw79s8d-YI5jAfKLwlkYNqbSp6jpJeov3l-D6HDV5I04-TxT-0CHwfWI6oAPdqBUJJsbXONoQq_beVZtkW3bW91kVr7ZY85oOFSWTMwjCXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbbMCHOt6qyCK9rAvhXkL79ekEuXXxXHTEjY6_kqdAwY2vGf_AlWHlCfkCy0GioxeHWJZwqeFat9WNP9vELVpiC3QdwS86SE95YioeAxrPqoq94rfP_BVTNaQC3XeAPuR0SaMAitE0qg434_5T--vFcoR8dArS7MQa7td13OuDs-xB8gBCT-ccuwS_0tPWQ2l5FVQd6zdACX9fcWQ4PFICOH4_dKjSc8FBpBdcCU95djeORsYD7rP9lJgwRGWvrRg2CXeRYcjoqJoL2f3Z81_GlsZLy99sgpnyqHvD5JwXxULuJOJGdCHqC2B3-jZ9pX8o_V0zRPkFXBGW3-CbWdAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQEEMmfedZH2k_n7UoKLKeqT2eTBLh4GYRQkYRL-cQqY0p_ChD4TTFj71R9cUoZr7i6hJSQrGH1OSNC5agAwlGpGaHyhAcJ8CoCSaHMUwe9ipjfvn_CYpNN48DO76rb45Y68Jqsza0KQS7fPih_tYsX08hmW41Xkk6c-n6mOI6BbGaOuT3KOglq4FLxDVGQWQwogkP1iB86X_t5XXygvh1IkKvw8MjtvQ224Lxiwid2UnuZgN3LcQME0mS-bAE7IO8UVcQjU77rmDZl2HrqvTmhlhUSU2KBmxR04Git4dF1wNUHl-ZDuk41PyPa9ytBsSYabyGEuKf6Ko_JshU1PvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbtzPkS9Sqx7f-W9yUQHZWcFxr8luZ7Y2yMMTJor0Mo3SLzxBXLg-sDran_XEB9SWAxTKbfJmGbE5FnZLrT4DHZyVKXt3nbalBx5WNkxSs6u5G1flI5nOZgAetONHZFcDCzHTEy4jQPUCh1b2CI-zqfTanVRVtFyGISeLGLc8pNszrNrtYxDC2y8_qOhcbxRBW7cHWwpA-TnucbXOpicsjQp-pFwjbDavbCj6emKU_baj-7wSXaua_Z31y5E4StqOcr1u0zsNkOw7P93LBoGg4OEAhh-es3sXEX1wdXhRXd2M_KVCouXXW-SSpmtCByfV1mOsIOokVXZtyJbZcfBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلا درخواست یک توییت از ترامپ دادن</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5684" target="_blank">📅 21:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
برخلاف ادعای شبکه الجزیره ، هیئت جمهوری اسلامی محل مذاکرات رو ترک نکرده!
پس از آنکه ترامپ  مطلبی در تروث سوشال منتشر کرد و به سران جمهوری اسلامی گفت که باید دست از حمایت از گروه تروریستی حزب‌الله بردارند و گرنه شدیدا بمباران خواهید شد،
هئیت جمهوری اسلامی ناراحت شد و پاسخ داد و…. و شایعه شد که مذاکرات رو ترک کردن، ولی ترک نکردن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5683" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lg9F7ugYaxiGd4VaKJe1KqV2l6Di8Ru2lhInp5mXFmksHdlyBWKgB1zQ6nGYIkTNKrh8WAOcR4h6jexbzcf_70BVgYgPxslrIO1t9esuKFXhxiBeyQ25KHsHZtPW0OIWHzidvWA27t61HQJPbURgyC_SxStusfImgy-qf9kXpK1kJn4GH_pQ3YrOb6vehkfp5VmJs1gT-4zoGZRq5_24jXQJe4xT7HbtL4oFUlztU1d35Mp5ZQHU1D8Dk7fa27qMgoEAMW0x1CNANahQLhU0GWcskmzCrScqN7ZkW74nJpS3igEH-6ZvJu9fqtY83_XCCX53Lva5bH8igN2i5lBKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل امروز به جنوب لبنان رفت و دیداری با فرماندهان نیروهای اسرائیلی در جنوب لبنان داشت.
جنوب لبنان تا همین ۴ ماه پیش در کنترل نظامی اسرائیل نبود!
حزب‌الله برای انتقام خون خامنه‌ای ، دست به جنگ زد، ۴ هزار کشته داد، ۲۰٪ خاک لبنان را داد و حدود یک میلیون شیعه لبنانی، بیش از ۳ ماه است که آواره محلات مسیحی و سنی و… هستند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5682" target="_blank">📅 20:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=J_IQer5AV2LgJbzATUUxeYH56l6tuDYaxmejaoJL8-RI0Ix0_G58jVROwRf4LEHwmTOVue3rZYwZhVv_CxC72Fez1AQW06UImzWcgBJDPH2zxZ6TG6cGGJblsnka4urEndvLfishmPvH9Vn7I18w_3K-fep7jCIxj1vuuZKZORNrQRfLln78H0y1BfjI-jT9u1uBrEZWHdqehw8jDM9gUQY7rLfAa_jodCDx7ohZPGqpMUfUPDKc094nIgmAfaX824moU6Os50R4CJ8XpgC9XdDkXOZ-TyGkh5mos6Zh8ZZVlUy6ASHXHTExd1t389UVggTWog7_tIeYA_-PsnS-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca65ce2ecf.mp4?token=J_IQer5AV2LgJbzATUUxeYH56l6tuDYaxmejaoJL8-RI0Ix0_G58jVROwRf4LEHwmTOVue3rZYwZhVv_CxC72Fez1AQW06UImzWcgBJDPH2zxZ6TG6cGGJblsnka4urEndvLfishmPvH9Vn7I18w_3K-fep7jCIxj1vuuZKZORNrQRfLln78H0y1BfjI-jT9u1uBrEZWHdqehw8jDM9gUQY7rLfAa_jodCDx7ohZPGqpMUfUPDKc094nIgmAfaX824moU6Os50R4CJ8XpgC9XdDkXOZ-TyGkh5mos6Zh8ZZVlUy6ASHXHTExd1t389UVggTWog7_tIeYA_-PsnS-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین شب‌ها:
یک مراسم عزاداری در‌جمهوری اسلامی
و یک عروسی در غزه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5680" target="_blank">📅 20:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyoy_PPhK8Z4g8zcZ5dx-ONXVyb86-4Vf8SX0k1YLyKxH4f-0kFJeel8AZSeNv5DiiPmML6iSyWGuyw3h2BUE_a0b-4SL3Uf2Y7-ghIM8JeUJL6zriQu8rJ4aHssThap6jilramnLA9v8-mI-iJEpqoXmHvj8dYn3O3H1qODEtXGOwSlWZJlTK-_Q8_AUkH2nm3_BEGqGvGC0316m6Dsm4D1MYv5XrqmlWLE6Jj_VvTd11kf9nyA3YyUNLfA7PhbuwfBvVcsuSCo7UEMmMb26qRYbpewYxrNL7_NB1MT7YRFa0jYQ92zoX88N_Ax6xhTWK19xr_epp4s6u9KDlg79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=uVSVC3V6uUw8Ozf8dA7DWQOc1EdKGkwxQQW-3ZYUydcRtz9jLIZTO3EN4QPK8y5rLNbPRrPChaGamX78V1-me0L3qeUxS3Fz2kidF65R5cg0f7k3_wVvhKTcUfkTBXlgt5a5zqkWi9qTlUeptD5X5V_-sdocJ7E3CQCKd9WDUEQCuYjInjLzVj98jUluYP_uL6i_SqgmE8QNO7VkOI8ScN9f8H62mvuI4X5ozjEv9EKAC170O_q-WceRb5zc5_UgYR2uZ2RzQfQgs5hboHYTNB3sEZIMjrdIXd6keRCHDJVgcUcpr5n2svJE--RW7qZ_DHxa6V1UeQAylJbsQxIc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=uVSVC3V6uUw8Ozf8dA7DWQOc1EdKGkwxQQW-3ZYUydcRtz9jLIZTO3EN4QPK8y5rLNbPRrPChaGamX78V1-me0L3qeUxS3Fz2kidF65R5cg0f7k3_wVvhKTcUfkTBXlgt5a5zqkWi9qTlUeptD5X5V_-sdocJ7E3CQCKd9WDUEQCuYjInjLzVj98jUluYP_uL6i_SqgmE8QNO7VkOI8ScN9f8H62mvuI4X5ozjEv9EKAC170O_q-WceRb5zc5_UgYR2uZ2RzQfQgs5hboHYTNB3sEZIMjrdIXd6keRCHDJVgcUcpr5n2svJE--RW7qZ_DHxa6V1UeQAylJbsQxIc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=bGWqNfDs9S7K1w5rdnpoqWR6Z28nFYULEPn98xmvD6PgycXr557ye-EA01cqgzN1eTm6so-uXFBT1dT9D00Qk9HStZxGl6EPdclwic8la2tLPR47_HOiIcJOTEhYTqUOQLFpAHn9HGPiB2TpyHq0VGFhDTScXG11RqIRPmp0diilCw6pvJ1s1yB1jGSmOF1MkCsVWo2MdPDlqnozfmCE7nvc4iNvp5KoqTaFl8bHb5uuYi8tG66aa43-cKgjDv4o4SUc-64ZdvkZDMKq7_bZBQbWRu48XpGvI6UKra44_Qhl8qwHlQGhGi3m9yzjTBfaG3Fg44cahGqdzk3nFMgNoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=bGWqNfDs9S7K1w5rdnpoqWR6Z28nFYULEPn98xmvD6PgycXr557ye-EA01cqgzN1eTm6so-uXFBT1dT9D00Qk9HStZxGl6EPdclwic8la2tLPR47_HOiIcJOTEhYTqUOQLFpAHn9HGPiB2TpyHq0VGFhDTScXG11RqIRPmp0diilCw6pvJ1s1yB1jGSmOF1MkCsVWo2MdPDlqnozfmCE7nvc4iNvp5KoqTaFl8bHb5uuYi8tG66aa43-cKgjDv4o4SUc-64ZdvkZDMKq7_bZBQbWRu48XpGvI6UKra44_Qhl8qwHlQGhGi3m9yzjTBfaG3Fg44cahGqdzk3nFMgNoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOTpfHQ96STuCaEK-Q8T2cIx8tGJnUV0LbdOT6aoZcA57aVV1F3stpPCjsMO_XboOlceJaCwvnQ4R2XGrng0YVt0fQvHJr4er13Z9zqrJDRE3s9ISlIWeL7K7Nc0UohXDCWiuqZOQtTugL0wAAICQXt5JsG7EjrXNQ3DRvtbTWQqxwLOzWuz-o6WnuhzW24-HzGfe35qM55VL6os_lWyFC9qyzgHOqU-p1orgA5SdbXOu5NX_xXjqE_tuq6_BgDjKWMC4OPEAO8p1itail1gyF_CdEzjDySO8hDmYb0PG4hfxB1yV7NauwmLeeYg4AcvCf2okzASQc47q0ji5pnjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=gYBKZws58SuBEgdev2mTQgFehl4y-GTk6tdqcR7ZDN4bYc_c379RB-BYzdDATEWVyo3NddXhNyq2BBE7kGnVWa6ui3CIBGOglsiMQhG1P2vIOn51mlPzDVLBxH6igdmoqPTArFKzAJPpMYZzauNSoXIfpSTeZ2NbJ_NwSlbsTy7-Uo4mTMm6otwjC0DrndVEB5E4S7hmYhW8du3G2cPtk7UQF0MjNpS9V9MZk0Sgo4mqylioEI9ixH7bX7rmu9KKbLrwltjl4497J27J5qjP5v79wsJg0gFKv4AtSCteuhaELV-PG8vh9rICtqWGJNiO-nvLrJMZ7u_RQxf170Adew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=gYBKZws58SuBEgdev2mTQgFehl4y-GTk6tdqcR7ZDN4bYc_c379RB-BYzdDATEWVyo3NddXhNyq2BBE7kGnVWa6ui3CIBGOglsiMQhG1P2vIOn51mlPzDVLBxH6igdmoqPTArFKzAJPpMYZzauNSoXIfpSTeZ2NbJ_NwSlbsTy7-Uo4mTMm6otwjC0DrndVEB5E4S7hmYhW8du3G2cPtk7UQF0MjNpS9V9MZk0Sgo4mqylioEI9ixH7bX7rmu9KKbLrwltjl4497J27J5qjP5v79wsJg0gFKv4AtSCteuhaELV-PG8vh9rICtqWGJNiO-nvLrJMZ7u_RQxf170Adew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiuzpa9ORofo52Sn28Y6R-dG7IgWnx65a17YIkPFYGm7bMP7_YJjRpAJJ0w48vixYPaz-fJ8XTYLKBfBcvxc-e44i_Bfcw014b351p0j2N3jOcwa1_0w9qqD0554hvhG4c-8XI1oKZ6kf11sXSK0DbjOB1xNWPDX99n45PchF7mh7aLJX0kE_MVOc_MbnAOMTtgdUm0dhl-OlKUaVIENaCiPPCHRyNOsd5kf5oq6LxGKBe81caQj8Z8lVFY1eaoKW3Cxn6nsIdbI-23YvkzS9i2I12j5Dph3x9MeDS5ggy_nRRPjH98smgXzInqTb3_nemw9eclpEA71azkMTkUNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiFHYx3PjbXVo7C5R-JM2Suty6Bh3gYLZf83SRQilRMkXY2NhG15ZWls-S_UWAZ_XtVE-4DEP7IkYGheB4-C6sXz-MLXOqEhq4phu3O_2OPj18sw3VYZmwcHr77oflBE9prpkWA7HlvsqXa-hudhjiFPWHd1UywugSAxOS6pA-QWmMiA2_WJPyByJcIqxgb98gI5aUYmxn8kEhmrPocEcX0UW9kvIlheQ1o_T9SyVMzk2Mae350BED8OkRu-9PTKFp_0SBTpvwVlOjs63_yzUG3fhaNdXs6_HV5-f1MxtrvFlGrwzuSCnueMjRm2oDsp9zILGtHNL8c2ShLuAeNCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUuyvaZYW89tPaHQiDjz6WlI9EgYqNk4PxLCqkDheWDTCLeQCt8ExvXEWOwTUR2wz66XeCnTj-KEcjpH1AQ9wQ71FtpakrNaZyAOLSplMfJUlPZ8mGf7G3XtRAs8iXE12xNk-ssyz3_QhTVFiCdUrp3SFDDCMwaxF_IgZb0W4cjF2USrPYfaj8y7y9KYRnuoenkEVEA00t6Rl-WWbUtHvT-1B1kG_R55tHclPQYEMPCRGNN3lKyV9MFt3zxKgfBb-Ip30gx0atmVeo5IdaxnJFDZqUIEXBztYUU6chwb8tWDWfpZO4ks8rKLcCRRhZT756Wutoxi75Qe8yuvnIJlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6wJ3MVbVRtm6BF-pl5hsGM7ryiDbPx8VLbEdb5KKbJessvDsJPHvwDgF8WQAwv2sFESlWOo9W8-QmuYl38nkSDxg1k7067EwtowPjbO-Xxb9riaPIgtyvM7TXH-4sKFG97fU__hdpX3mAR1-x6GL8a79Kv6FCDbQQ6DkwxDxAuzCvxtO0diIAt7V9m12lLW-uvVqP6yTXgMV7_p7aheN02RnygUVoenRblm7uYYeN3oz2cO8Ifra4BckbmugqQ3WYH3kd95fT0R4e-DjnL_cT11cP0lboEr-AI61OWUvScbOVrFv4RV7r-fHouyr9FkwGTe49GcPsQgr6-vN0iD_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=GhfeZpXas98dfiAcNGuebJgJMP85FzF36iIJqQ7kwwnBtTCXs5C8Fit-QzeCgLo7NYGx0e_mfs3PVw-Zps72uJ22s_nwuLWZW4ZGEMY6GmO_dwNafwHUtN_8TH93-PB3b0pARCCvnmwOl3anyi5NAg1Q3E3P0yArAY05YxP4jd5F8fJc_p15cdhCSrmnY9rETRksZccQS94vhEQjKgir_0Xy59T1gezlOF09QoyfgoVqS7A5ycLRXXZMmsB8jZSySv864ac-RN-8uZrpZFcrDonsNCQpLhzAZA1sJSnctsNINEq3d6OcH5-xpLns-576xhbnz9Cex6n2dNDlAfsoOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=GhfeZpXas98dfiAcNGuebJgJMP85FzF36iIJqQ7kwwnBtTCXs5C8Fit-QzeCgLo7NYGx0e_mfs3PVw-Zps72uJ22s_nwuLWZW4ZGEMY6GmO_dwNafwHUtN_8TH93-PB3b0pARCCvnmwOl3anyi5NAg1Q3E3P0yArAY05YxP4jd5F8fJc_p15cdhCSrmnY9rETRksZccQS94vhEQjKgir_0Xy59T1gezlOF09QoyfgoVqS7A5ycLRXXZMmsB8jZSySv864ac-RN-8uZrpZFcrDonsNCQpLhzAZA1sJSnctsNINEq3d6OcH5-xpLns-576xhbnz9Cex6n2dNDlAfsoOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=SAd3lUdzB3qD-akEL0BXgqPYRpPcsqsVx_2VKublRAruMyp-eBPl3T1nYt_BnIwqZvmK06Y_JFujfVGLF2ef1BewCiqpzJuJyFz9rCEsKCnp4hZSa_lXZVPXPd0uLyPO_t3lpWdsl9V9IWqUI-RCXVYI1XmI6hNzsv8XcZrTOHUDGxY3thqdGZ_WHZdTaO-w-uwR8r-LcDRGEzs859Qo3W_CqL8WIIoD_YHdrhNNmnPQ8SUS7AFfKmvV6hQpWt82QL9CLiaOM296jR1U2kYQcLl81H72XffEo21VKZJuvuFtRMrl8Usp1RHNqCQn1GMfKlCS8cA44UmiAZ_lkE8eeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=SAd3lUdzB3qD-akEL0BXgqPYRpPcsqsVx_2VKublRAruMyp-eBPl3T1nYt_BnIwqZvmK06Y_JFujfVGLF2ef1BewCiqpzJuJyFz9rCEsKCnp4hZSa_lXZVPXPd0uLyPO_t3lpWdsl9V9IWqUI-RCXVYI1XmI6hNzsv8XcZrTOHUDGxY3thqdGZ_WHZdTaO-w-uwR8r-LcDRGEzs859Qo3W_CqL8WIIoD_YHdrhNNmnPQ8SUS7AFfKmvV6hQpWt82QL9CLiaOM296jR1U2kYQcLl81H72XffEo21VKZJuvuFtRMrl8Usp1RHNqCQn1GMfKlCS8cA44UmiAZ_lkE8eeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=f-_cr82h5j4VnJn5ite8Tt2j2EojfR4soXk0dHSJvX08aSgDFLCl_lyR6tt69b71tJe6GuiTxKJ6z-aWW8NyV0xkA-tP1WPOauzLYgN7wkMwRmbFLNbIzcMKgNbiR7wflV7c_6_VJoSIQ3GC8OdcseTi3iHqgOtFqQAc0cBvV0aEuCF0nn7A5Y00Mihnj4246WLdYdzNWnTd87rT8Ofu0m1K_fWWOnMXsL4PdNPUPUyuG8SREJufJe9NhzxMgyDOsinJEn3CLPWBUuQWxC_ZPTu6hMcWk4xkZMSu-qKYYweSTbPCs6U_buwevzlkWQJU1BA82yObWSgStNmT_r0Gyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=f-_cr82h5j4VnJn5ite8Tt2j2EojfR4soXk0dHSJvX08aSgDFLCl_lyR6tt69b71tJe6GuiTxKJ6z-aWW8NyV0xkA-tP1WPOauzLYgN7wkMwRmbFLNbIzcMKgNbiR7wflV7c_6_VJoSIQ3GC8OdcseTi3iHqgOtFqQAc0cBvV0aEuCF0nn7A5Y00Mihnj4246WLdYdzNWnTd87rT8Ofu0m1K_fWWOnMXsL4PdNPUPUyuG8SREJufJe9NhzxMgyDOsinJEn3CLPWBUuQWxC_ZPTu6hMcWk4xkZMSu-qKYYweSTbPCs6U_buwevzlkWQJU1BA82yObWSgStNmT_r0Gyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=dRiahI3JCoAwYJDeLe5G_pnSEkoYqFCCPb7vY_uBdCD3oCH0VeV0_7Q5VMbulopRnTJdMzL2BNANrQOynLN8OrQ8LezcZWzkoubkdKuEFF2iYZWmqGjP35B7jwwg1hceIjKm0G8ouVoAo4bDplwQJpcTGsu5DmHepB4n3h2XV37F__t4qhaxh3DLT35eguuTBN4cC3THTT499L91fiRPzN85irCQkQtDSJ8NmHe4LXq_58VK_AmL7_D90S9iYSBcYGyNTIjF6J_FLnbWJyDPGVJCKHwwAz29VfrOy6fxRldVdJyypCGLmNe9QGDc47trtq1OUbM9-F4kzn3ni_Y1DypyG3Czojl3zlFuTjfzR1eLsdGuOuvkFhLmsRcM5AWp4crRDYVVmEWtHTRZA2RvpqMQm8_aUPlrzwW-Y1V2iA94XIY0t02iu8ceXND-MYgBPC75UaN1IOXT58Xml7vXlaiT4Z6ZBddSDkmwwwkc0XrXAkHOaZCZlcMzz-m_jP5gv1IFyzJLe87Cf7_9fs8B_GlS9VsZMkGGeP-8Iuam48koJleC9YTGRFFIOBZCNvEFnWS1E2GMKP0cfIAJIyj8Ez3VlOaC8CF2eqJx7y2knBs-yqzTxM83CF3PRg3vDtSz4dktcfXJkLBrEfkWvY0U01VS4ciG0WI5quZ60BObJss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=dRiahI3JCoAwYJDeLe5G_pnSEkoYqFCCPb7vY_uBdCD3oCH0VeV0_7Q5VMbulopRnTJdMzL2BNANrQOynLN8OrQ8LezcZWzkoubkdKuEFF2iYZWmqGjP35B7jwwg1hceIjKm0G8ouVoAo4bDplwQJpcTGsu5DmHepB4n3h2XV37F__t4qhaxh3DLT35eguuTBN4cC3THTT499L91fiRPzN85irCQkQtDSJ8NmHe4LXq_58VK_AmL7_D90S9iYSBcYGyNTIjF6J_FLnbWJyDPGVJCKHwwAz29VfrOy6fxRldVdJyypCGLmNe9QGDc47trtq1OUbM9-F4kzn3ni_Y1DypyG3Czojl3zlFuTjfzR1eLsdGuOuvkFhLmsRcM5AWp4crRDYVVmEWtHTRZA2RvpqMQm8_aUPlrzwW-Y1V2iA94XIY0t02iu8ceXND-MYgBPC75UaN1IOXT58Xml7vXlaiT4Z6ZBddSDkmwwwkc0XrXAkHOaZCZlcMzz-m_jP5gv1IFyzJLe87Cf7_9fs8B_GlS9VsZMkGGeP-8Iuam48koJleC9YTGRFFIOBZCNvEFnWS1E2GMKP0cfIAJIyj8Ez3VlOaC8CF2eqJx7y2knBs-yqzTxM83CF3PRg3vDtSz4dktcfXJkLBrEfkWvY0U01VS4ciG0WI5quZ60BObJss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=AMyDxl3sN6M3qbVqzNavfH-Xe1saRcqp1JoxaujKONj946VetgMsiHZRT9b39vqQ3Eb26wzsM_UwfU1pV8F7F9dPvsAPWduFgMdXeFMPJobrzw4ND0VAfYaqHSg5EtXyOd3CopOr2HTFdP2MMVJPV8Q5eDRrV-wof60W8iYJTAfqJhCEwX8eLcfMb3xBpouTrXgJLY4yaOqwtXrY_9pZzhVxHG7nadJ7lkVwooongQbjCnbTIqKVheS6aSU5HiNGs9hoopHDr2YYcgFW_r2jfRTBz3d9CuZlzcUmJSehpdZrgO_rhtfHhR4S0-yyss-y9mBwY3IZn_1n1KDO4z-SFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=AMyDxl3sN6M3qbVqzNavfH-Xe1saRcqp1JoxaujKONj946VetgMsiHZRT9b39vqQ3Eb26wzsM_UwfU1pV8F7F9dPvsAPWduFgMdXeFMPJobrzw4ND0VAfYaqHSg5EtXyOd3CopOr2HTFdP2MMVJPV8Q5eDRrV-wof60W8iYJTAfqJhCEwX8eLcfMb3xBpouTrXgJLY4yaOqwtXrY_9pZzhVxHG7nadJ7lkVwooongQbjCnbTIqKVheS6aSU5HiNGs9hoopHDr2YYcgFW_r2jfRTBz3d9CuZlzcUmJSehpdZrgO_rhtfHhR4S0-yyss-y9mBwY3IZn_1n1KDO4z-SFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=t9HRO1Q5FuiLLE0ILzicEUGbztRbLc8joG4ydGSZDEjW5Y_Tf5DKrgj45NWVlgUNUNZLNjJFfiIoR6VY0KvAMnF9RdkGBiUToZ_JwVHHs7al97keSvYjypXm3p4aTKsdYbcpw6vyGsirwM2vI7rg1NGXqYNzfyn_H8XvWabirqGfiodbV1dmrRRGXbyUAOjT6ea42VCU2v_4Nd_WQz3ViU0XErr3bmMygFzyDeQVafMT2D4w-8D7LIL5Y2Q3Qe2V49WMxBlYpuZBmvb2yid-2NKvqJgwJNISrc8bC_Dyn8c81ptJ2vju9ksQ4visZ1zHsUj292fAOh2SV863xgmoAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=t9HRO1Q5FuiLLE0ILzicEUGbztRbLc8joG4ydGSZDEjW5Y_Tf5DKrgj45NWVlgUNUNZLNjJFfiIoR6VY0KvAMnF9RdkGBiUToZ_JwVHHs7al97keSvYjypXm3p4aTKsdYbcpw6vyGsirwM2vI7rg1NGXqYNzfyn_H8XvWabirqGfiodbV1dmrRRGXbyUAOjT6ea42VCU2v_4Nd_WQz3ViU0XErr3bmMygFzyDeQVafMT2D4w-8D7LIL5Y2Q3Qe2V49WMxBlYpuZBmvb2yid-2NKvqJgwJNISrc8bC_Dyn8c81ptJ2vju9ksQ4visZ1zHsUj292fAOh2SV863xgmoAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn4W64CDpuB95IcsQ0F0sVc78jXdhykrbHNRZlKIRNjniZ-b-mmDZdD0m9vNex8u9LVnJRulMrFI4FwEXwiiDRDzRpuHFzpy1cyNFMadM0MhNkQQXUKrBPl50gcjNl26zKgx27_lEG2RTtclKVmXgXPZEs7a4bC8LJUuiQpOUIfkVwWSM09To3Rm99gxJZuWL09ztnUbsBvatAI_uct-hbG8JemEyTYjb0bthIFZPITkvZIgY3YV_ymoSJ0vBbdEiqBPil_qN9bOz7DGF5Vm3p5mE1xODa61K_bBVMewt1GwlBK2UQhYv7kyN-AbyU9nneqnu4xFNyqCsGc9mxa5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=UAKISL4Oeo_OfKCCdI3bV6D66joZUFs6nk91dMHUHnh9CmAGFru7c650Aw_ZtcUcB6Rrjau1ZxUuIz4ZALA2HYDIzHZCMQlnLRSgDXsxBl7LUrRITXxqNLEuh3RIcX4XtM1HBq4buMQeYFdK8WM7Ip8Raw4LQi0QPdMzIFR-JRSV56HEfbrZ9E3gLiHveInmnkJqC4ZPAxxfvnSfQf5UaQJB_Ys2OVQ7QcvR9eb0qFgs8ugD6MYdUGLuZTJUbSnh11Lpwn2sKb50K93LGGWZSYA9GSXw1vvfi5gsx4dgkMiuLlwc_VskSaO6AtIWTlTzhJcNHwZM2mx56AJIRsafzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=UAKISL4Oeo_OfKCCdI3bV6D66joZUFs6nk91dMHUHnh9CmAGFru7c650Aw_ZtcUcB6Rrjau1ZxUuIz4ZALA2HYDIzHZCMQlnLRSgDXsxBl7LUrRITXxqNLEuh3RIcX4XtM1HBq4buMQeYFdK8WM7Ip8Raw4LQi0QPdMzIFR-JRSV56HEfbrZ9E3gLiHveInmnkJqC4ZPAxxfvnSfQf5UaQJB_Ys2OVQ7QcvR9eb0qFgs8ugD6MYdUGLuZTJUbSnh11Lpwn2sKb50K93LGGWZSYA9GSXw1vvfi5gsx4dgkMiuLlwc_VskSaO6AtIWTlTzhJcNHwZM2mx56AJIRsafzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJoPi6D4fQOsnoIjcMDIPAD0G9RWBBDLFoP4BBI6lw4Z3UMz9nY7v9j-ouzbgREjMmP-kwxKyzU-R3llM0WsiPc3C0WNXWsSrrV6yl3tUuS9ZenOEi0E54UPv2QfIZnEL9w5j6vH7qoLmj6wg3H36KC7KpbZZCs6aUaGcBRbD_s3B73Wf3B1doI0bSR-xOFayZG5q91LvtYbDRui6pbZCtsglWRvAUN6PmZDP06t4jWxkyaY5yyRFnHI_HjkbRM6U7fOzJ7SmBdFpxkdZ_If0T6f9QstFDIx7z-jHielscxIEFZ7iCZGtYdWo6bEoMENscLDbTRzv2OmVxu8JGAZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q__e_w-clayS1BrhGkjVZLrpj2FoqTpo9e32upa3abJqHMYcQRVkjCKIcChXequcXc7-Ogo3Dg7lG69FRoohXwJhqXmKB2TKcQY2EqPWsIzqLLWcKGjNHEs0B5T04FHMtYcvtArAZGD3wG5OxHIfXsSPZhrXMkvP4rh7npiXIQMAIAUM9LbUdf9Nzmg1VJv0aWU9DrGGdURNE9-PQwjWd5-tMZfPeYfhlhr2EaSO1pILfAf1fV-vpuKo8fhCbn0TACuNkmHDuFvmpJnxb1kA6sBdnJp82z7l89FIgHdoHdcYD6QJtSc_QXqsYAT1-jXMCXf6yleI5lL6Bm0uouLW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Ex3YkEWMj0fqXal3cseXH4yt5mSfQdAS3gu3T9NaFxBRbhjgq-LWgWDu7Hj1aFFFpFpUwISGAiUPeTVubKqaCtSIg38-XFA0ld2-B1QFe3Uk9Y7UoblF5ETAMZV-OqrEuiS_HteZIbVF2im_iWlYpFZo8JT4JZnuMK1BKEfShzMxRbA7gJTltsKvJ9ZeXq9fdnFQO_8puM-wWcIdzPxINkbTG2k9KDsQ8HSj8Thg50VDjMl45Q_CuN_d6PrFyCEJxt1DEPdeIK6bdM8gzek2hKn1JNGqFRFnoywkMmWwbP8qYr6vveZ3PEPeAzZQZUsz4gwpajChBxMU0Q9ldVz9yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=Ex3YkEWMj0fqXal3cseXH4yt5mSfQdAS3gu3T9NaFxBRbhjgq-LWgWDu7Hj1aFFFpFpUwISGAiUPeTVubKqaCtSIg38-XFA0ld2-B1QFe3Uk9Y7UoblF5ETAMZV-OqrEuiS_HteZIbVF2im_iWlYpFZo8JT4JZnuMK1BKEfShzMxRbA7gJTltsKvJ9ZeXq9fdnFQO_8puM-wWcIdzPxINkbTG2k9KDsQ8HSj8Thg50VDjMl45Q_CuN_d6PrFyCEJxt1DEPdeIK6bdM8gzek2hKn1JNGqFRFnoywkMmWwbP8qYr6vveZ3PEPeAzZQZUsz4gwpajChBxMU0Q9ldVz9yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=uzWc5fReIquAPrl4qg2tAR5H9OXEif-FSLqSbPousw_pewWupq0FxZk79YGfYTlADaBKrrikgcNRtEAAbbJfI2ZSUpzs-0lF8qj_hhy8WBeYK5b0njru3bTQQbTIT6W0e7p5dDHkO7OmxZ9fzsqPgQeiIebCa5V3RFX3qsTEHXZcGryjbDxG1_BJfAZXswrBFFmGp2CgqO-d4YIXQ7R6Os0vHiRRX9Pa4OvJDUNiNPoYcJmN2Mte_PLdoez7UtRDaaYi1epuQayVOS6pvShJeK0wllmBaUpiSdlndq0Qw-VFzOSF_mjj92YBXkzajAUb6hvmfrWLp_c3bN-6CACXjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=uzWc5fReIquAPrl4qg2tAR5H9OXEif-FSLqSbPousw_pewWupq0FxZk79YGfYTlADaBKrrikgcNRtEAAbbJfI2ZSUpzs-0lF8qj_hhy8WBeYK5b0njru3bTQQbTIT6W0e7p5dDHkO7OmxZ9fzsqPgQeiIebCa5V3RFX3qsTEHXZcGryjbDxG1_BJfAZXswrBFFmGp2CgqO-d4YIXQ7R6Os0vHiRRX9Pa4OvJDUNiNPoYcJmN2Mte_PLdoez7UtRDaaYi1epuQayVOS6pvShJeK0wllmBaUpiSdlndq0Qw-VFzOSF_mjj92YBXkzajAUb6hvmfrWLp_c3bN-6CACXjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=FzGrmKRrHycV6VpWs4E0gMl19qrHbxDapKgrI1bIt87reVZNCi8bLIMdMOUIX0iyh57NnERgqntSKpMA8jLDUbawjOKxEQjNEiIqP2gAKb0MQGBSOG1BnY489X2i05aKWyzgtmZesiMUYv3B4Qgcz7rSPGRqZZh0Ur8_M1b02bD4mwaYHf7U0dKRCEqt9gZR6WvZw3AYR1UqETHbF7UPH8nlsAxbXo9G81D75VRVe4haGLRPjVqwvdkQZ7jcYiUqAArvZSVjMEFCOc7dC862q7Er0QOsM1MRHxXW3oYosOGcEGvTOhAkcwRW_bchrGfh5F73y54TUKHbJJ0zLW7ZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=FzGrmKRrHycV6VpWs4E0gMl19qrHbxDapKgrI1bIt87reVZNCi8bLIMdMOUIX0iyh57NnERgqntSKpMA8jLDUbawjOKxEQjNEiIqP2gAKb0MQGBSOG1BnY489X2i05aKWyzgtmZesiMUYv3B4Qgcz7rSPGRqZZh0Ur8_M1b02bD4mwaYHf7U0dKRCEqt9gZR6WvZw3AYR1UqETHbF7UPH8nlsAxbXo9G81D75VRVe4haGLRPjVqwvdkQZ7jcYiUqAArvZSVjMEFCOc7dC862q7Er0QOsM1MRHxXW3oYosOGcEGvTOhAkcwRW_bchrGfh5F73y54TUKHbJJ0zLW7ZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9XGBoHbGEjP3D30RNOAziXwp-NdNROJPMdd-lPgviCEi-jNCnii_DYKSs6Z8tKkSi3a2f37_tDZxasjrn3tcW3TxgTuAN84OYgIRo0zu3YkwizRT22Ae6T4CfABrQWNlaq_fAt84TwEIPA2U6krNf4IVQ8Kqv9vcb0ZnePFz8f_JrzibOUuvQcasZtOpiUoEobt24Hb8uB-lNOcj6BROWId0Pvr782vftUol6fIEEShpO_9_H7z5zTdJuIyOLLJQ8l_dwopNFVdDM77t6GeGbHboDhhRtR1yyWhU1Aj_wcmNzFGRhLC5HmisCQqG6LKKE0cKXAJrZkWpjDt3Lum1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=oLLQCMBktG6i-5yr7DeTV3uvcF1ltaPiwsy6Te5YLz-eozThVh_TNsNecCqCumUdnmOr4_62XSk1Y8p860p-ycB6PbxJFamYK-UAQgbeKb5m8V7oZVPGRsLj53nxbaMZm-rpzyaFUkzGTu-WVokfWZh6TJQjGGSEOFwPY4HIw6y6yLwECYgOUTOJNu6zwwWLsn_i7os_JsL59mDf29r5ljEAUjFyVBlKGnk03JPfkcVXsqMAc3wNTDOrNNkeqoE1t29ILJKZo90JdYKD6CJISTNM8ipI2E1FApeD6va7mnd5QJR5dTJWEjG8_h-hUU24esQ3Jay_cHNjiPPCZh3l0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=oLLQCMBktG6i-5yr7DeTV3uvcF1ltaPiwsy6Te5YLz-eozThVh_TNsNecCqCumUdnmOr4_62XSk1Y8p860p-ycB6PbxJFamYK-UAQgbeKb5m8V7oZVPGRsLj53nxbaMZm-rpzyaFUkzGTu-WVokfWZh6TJQjGGSEOFwPY4HIw6y6yLwECYgOUTOJNu6zwwWLsn_i7os_JsL59mDf29r5ljEAUjFyVBlKGnk03JPfkcVXsqMAc3wNTDOrNNkeqoE1t29ILJKZo90JdYKD6CJISTNM8ipI2E1FApeD6va7mnd5QJR5dTJWEjG8_h-hUU24esQ3Jay_cHNjiPPCZh3l0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=EA5CkSkm1CoSx6TkW-i8_Xz5KAXTp_UhTu0b131OjqsENODoBSAIXWmk4Lm2ZuBpL-SPp98_LDjo_oBNOUeuCHsiue6Y7IFyNACaSGfa921MCSoTkZRTb2XY0Fmn-UuqlcPGLvd2WNJL3GBFx-LVzJqmttyTqX-6lNQeqmsoBhwpf-3YO49lAQ8INJu_48S2avWqJ_VrCx8fvA0Mv9Mr5CFuxPjwYZKu11LdeRBFLbwunfiRPMUxICHe3FKLxDJHAALDKRV6TlQXqZsSjYykGs6z065i4RyuRQPDweaH_iUJlSr7-2Wme7gwAvT6CLPhK0F4g1B30eBjRJLO6W1p7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=EA5CkSkm1CoSx6TkW-i8_Xz5KAXTp_UhTu0b131OjqsENODoBSAIXWmk4Lm2ZuBpL-SPp98_LDjo_oBNOUeuCHsiue6Y7IFyNACaSGfa921MCSoTkZRTb2XY0Fmn-UuqlcPGLvd2WNJL3GBFx-LVzJqmttyTqX-6lNQeqmsoBhwpf-3YO49lAQ8INJu_48S2avWqJ_VrCx8fvA0Mv9Mr5CFuxPjwYZKu11LdeRBFLbwunfiRPMUxICHe3FKLxDJHAALDKRV6TlQXqZsSjYykGs6z065i4RyuRQPDweaH_iUJlSr7-2Wme7gwAvT6CLPhK0F4g1B30eBjRJLO6W1p7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=bnsQQvSV08AxNZKvkezI35MRTKktsPfqJfEjdCRZEclgsA_9jYJ_GUBfEQ8dC54oifZsmTCGYm_RdZnr1mhKrg9elw5IhYIKlEGkqbK_A3nd-h8GPidzq96bzpU9kdrijjqZPSogFKDbhKpJmNTTNvCfr2XjwJArm3qKg_4tBY5LBED4ZsOaV2S-Vmoof6rK2TzlR3B0H668ZqT2J-x1LcvnXyb7OQoVljb3o7uqqqVWHA6ciHRUuWrJRagt16o8bKcnCUzxKOeJs4fBPOLKk-z1aizj4MBnSEjnmwSnZ_yZjGgCfqs3SpOBJWRvHMgvF4lXR6kXc2jocrJTbVz8tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=bnsQQvSV08AxNZKvkezI35MRTKktsPfqJfEjdCRZEclgsA_9jYJ_GUBfEQ8dC54oifZsmTCGYm_RdZnr1mhKrg9elw5IhYIKlEGkqbK_A3nd-h8GPidzq96bzpU9kdrijjqZPSogFKDbhKpJmNTTNvCfr2XjwJArm3qKg_4tBY5LBED4ZsOaV2S-Vmoof6rK2TzlR3B0H668ZqT2J-x1LcvnXyb7OQoVljb3o7uqqqVWHA6ciHRUuWrJRagt16o8bKcnCUzxKOeJs4fBPOLKk-z1aizj4MBnSEjnmwSnZ_yZjGgCfqs3SpOBJWRvHMgvF4lXR6kXc2jocrJTbVz8tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT6Zc7MKyPOWYA7lyZlxSnWLpec6tOiWVmysYNBsOkpZ1JNUBBW9GOSGALf--egTpR6Oj9fevu1hKlJQRv_jJDMErwxehQPmAloLJ6YaRR3HroBkNWSzHMLXR3AyQIXSxrSLpT5FZ_BHfZhMokg3hIU-mfJ83RAv6hSmzUD_s11ee60cYGKU3qzDFtyXY7jKN_tLKaMoacAcr9g9h6SCv6bY-PxxaszryPc89p0BClbr66BSJ0cditBxhYuKEhannwlPvPmhmsPvk-zwUzI7-0SoQj6K5nwlpEMUquAkh0MrY-dqz4f9YwhgLHHqYtabmtkO0ExvvgE5I6tFT5ZWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=H2-2v9Yvt6cyM5YVSX4PqJIk0H4Y2S11fpTubLUnxiAmyV-VDlKVjSwx2gxpWD1DFN8DFkAzfN3XAP6Hf-tUOdbAg-3VPX4EgRFNE7CPuEawAthzNyPgrfZCJwzrCc0w_EzVb4ZY7RIj5ehWedtK1dgEmnoaJZcBTgmkZuK0qeCyf6BbpdCITcGQElp6LulN1-EputQEBvYFNPIUtpkYKKKV9Gt-_qPC98gwFCfBuhhWNfZ0LBddHj81MPUO9ifGVlsiAd11krTLwflKsOFrrnprABslerHsIxopnkFdwpFRDcm0nvCOQg4xc8qMweXJjfroZvVn-LDv9wJOurG0sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=H2-2v9Yvt6cyM5YVSX4PqJIk0H4Y2S11fpTubLUnxiAmyV-VDlKVjSwx2gxpWD1DFN8DFkAzfN3XAP6Hf-tUOdbAg-3VPX4EgRFNE7CPuEawAthzNyPgrfZCJwzrCc0w_EzVb4ZY7RIj5ehWedtK1dgEmnoaJZcBTgmkZuK0qeCyf6BbpdCITcGQElp6LulN1-EputQEBvYFNPIUtpkYKKKV9Gt-_qPC98gwFCfBuhhWNfZ0LBddHj81MPUO9ifGVlsiAd11krTLwflKsOFrrnprABslerHsIxopnkFdwpFRDcm0nvCOQg4xc8qMweXJjfroZvVn-LDv9wJOurG0sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjEfFISMosyWyhQ7BhTTptLJod7SgJVwmHmpbyR4Y-iWaAfAM1xdH9uwMxcLkS9Pzl_7PzFE4X1Cs6sh3QDnFDzUNwkGGJGWE6X3fAehoWuSLgNSWhUuPamgjlzdIFjzgpoDAVbxPaddpsIhhMd-nErrRPplBwPqCjDsgfVSMWEI3erxW2oZlZ0QxGiXlippdesvcykLnM7GDpiCAw5xn8blu-icP8Gxe5zt0-YZsA-hsU6-cusMPlfe9h_9O8IQ_p-EPtReEw-GF7xkDXFjlVV_cIgUF5zWT5v5LPsZJskbCcUR90ouP0SxRNNZq9QnCn0eMpPMwhHXisJ7ztJKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=Jr82d9JD4TFhaUZmtXyE8F7ovg5vZszZF7Jej4zFwzyV2U-PugwE2wmJGjTJIKMLaNj2LMB3JOnXbnujwm2UaY86CiNRubAf5pgWvx_Xq1Igo4J8MR1zoJg01y_3aoS90oSMvPTkxOsgG5WUYNe1WG06rDFycdw8TW3nLeWkzzgZAB-ag-gO_pn7apSkqVgu4Ked8AzEx5ePrdX0juNzpE0YKRuQuifnNO5NsJq84mv4v5kzwyTE295eycYgGuDyJ_nK8eK9VxCcNDXPLvfd1ber8yLOSvMQkqKzzA0tDx5QzQt-idiJbUEXLeDoAeO9yG4I-uFX4W5DkSqGBjSrag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=Jr82d9JD4TFhaUZmtXyE8F7ovg5vZszZF7Jej4zFwzyV2U-PugwE2wmJGjTJIKMLaNj2LMB3JOnXbnujwm2UaY86CiNRubAf5pgWvx_Xq1Igo4J8MR1zoJg01y_3aoS90oSMvPTkxOsgG5WUYNe1WG06rDFycdw8TW3nLeWkzzgZAB-ag-gO_pn7apSkqVgu4Ked8AzEx5ePrdX0juNzpE0YKRuQuifnNO5NsJq84mv4v5kzwyTE295eycYgGuDyJ_nK8eK9VxCcNDXPLvfd1ber8yLOSvMQkqKzzA0tDx5QzQt-idiJbUEXLeDoAeO9yG4I-uFX4W5DkSqGBjSrag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OevM3PL7i4d09UPi5gOKucNv2lrSFeVy6ooNYeV6h4k9u9pGmJYnHbmVutuSIaQXCc3J4ikBJGcFUCxv7azF5-DSGudTKzNUC8-x44DVEWz3T_FcWX7z_k--4ft1pAwtX1BYAus_Ed3OA1oU6g27HbQzKQi7E6HdBRwczdT258eukxiD4wxpiFrd3y13NtQGl9BqBOcnmNXT-gXdOFntVpb6MDNC9Oo8pN_sAx37Lo2QfGvdSQVgdTpJ4Lo6022qwVUaunyvyD_Zl4AIVhlA0mudPsnuCqTia4WzChBknHVBpYHnCHR7CI2qMW_18a16OoQiTnvpotNwzlmfN-djrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=ItxfQAjK87Zadb7-rtlHvpeqpb7yBsQIfCQbs_nwi_9IkJ716BvyTFyk3beXvJfxxcgtcB1EDEuCySY4bK9SW4RohNVJkabXLJc6M3s3qCZTedeXOCGzA_stdE-VcIT_R-VW5DteMEd3gU86UzmnhRXD2G_Ah-h3mFGFkIgqbrTbtyEBTF5u6CDsFG7w3DHCKyaL93HHHKomurglNm1O6erg2JLfQYexI-6enPJMoCdLvlCgclxKErQddS8KmE9swjuIlugHBGFEh_QE2Se20KP0ZouncpXNrlMFaWT_o9Y0pPLMZfixdQiJcZmjcw_h0JG-7gzTfYSDMuGUCuvAUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=ItxfQAjK87Zadb7-rtlHvpeqpb7yBsQIfCQbs_nwi_9IkJ716BvyTFyk3beXvJfxxcgtcB1EDEuCySY4bK9SW4RohNVJkabXLJc6M3s3qCZTedeXOCGzA_stdE-VcIT_R-VW5DteMEd3gU86UzmnhRXD2G_Ah-h3mFGFkIgqbrTbtyEBTF5u6CDsFG7w3DHCKyaL93HHHKomurglNm1O6erg2JLfQYexI-6enPJMoCdLvlCgclxKErQddS8KmE9swjuIlugHBGFEh_QE2Se20KP0ZouncpXNrlMFaWT_o9Y0pPLMZfixdQiJcZmjcw_h0JG-7gzTfYSDMuGUCuvAUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/St2mLPnI7fCVbLm-HSpWF6hTKFQ6jvpJZOwfQtTqPT6O-Nne5rYrIDI6k04UvR0vJI1QoMvqaAJoBbl8f67Uhqi79PVn7puV66qFf9araTMbB6Qmp3m4FTZu7k5zFC39Ok-bt2trr59B1F5ePed2uOix9YRumWTpsxO6kMOwSor4Zs_ZiVRQxTp2fLBY8d6xb2TTN8WaUZWGm4StF_cgoERnu2Geg9zGG0O4-TLFJABZiOESwMRgqg7zXyxFLv_TfsfpNL3N-cO2Ecr52zof7M6voPM-Q5ljQ67VT65w50s9T_JyPhXKGIBmqW4g7DwIuWaZupWMO0L6QqKo4TXeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkSgw7anqEJnzRWneaOoWvvhFLqj4g9RcQRxHXhtxRF7ATujYAVfz7nlnZDx5rQvi0AuH1HKHlGBal0U9NmllJDqCsI6YgBsh1WqXPFegXaEN2f_0VSRutbNmTGsOLCGy4krljFM8zzACcoakXFSv4YJt1kybmB_tyJr5giPwvAumkVIsHOpjrxOQWbqOtgqvoXzsh6XiBFTtJ4XV_bj-wy41VlD6Os9jR2hP9dABGm8XiHug2S0U_lfseKb3qcHY5PHZTK075GiWvHXtEWuYw1PDunh4UBB7D68-OCe6Z6x7c6oem3_sc673u0xMqW78dojxb8YZq6_RqWnSVaEdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=HhByUGtRkM6B-alJET_aJU8r0kvbXwBzxmvX2kCSAQV68axxWGHjq22GviPBz3Ur9fPnd8qqNcDg04viEgFkZRaxv3yV6XarZtdOXEXE71A5Qul4FdCXPppw57sFg9-9XHGe4jTvmKpfT3Nf_nPGTWBtCEQg9RTQ_xTWo4MgM_cFXqu_-jfz0EmLWzfRCPzKwEJj5DtYjQXYnX77FAYqx-279Bvs-q1xahK2mrvsePQ7PoSPzhpVwYrVhwAQRtC_ElwPhOzu2XhjspeHyCtwkzxHGVuTHlG2NOnp3Oa-t491sb3ZylymRp1iqAH_TbIyMd-a5McSuZoEF2p5hxd8kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=HhByUGtRkM6B-alJET_aJU8r0kvbXwBzxmvX2kCSAQV68axxWGHjq22GviPBz3Ur9fPnd8qqNcDg04viEgFkZRaxv3yV6XarZtdOXEXE71A5Qul4FdCXPppw57sFg9-9XHGe4jTvmKpfT3Nf_nPGTWBtCEQg9RTQ_xTWo4MgM_cFXqu_-jfz0EmLWzfRCPzKwEJj5DtYjQXYnX77FAYqx-279Bvs-q1xahK2mrvsePQ7PoSPzhpVwYrVhwAQRtC_ElwPhOzu2XhjspeHyCtwkzxHGVuTHlG2NOnp3Oa-t491sb3ZylymRp1iqAH_TbIyMd-a5McSuZoEF2p5hxd8kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1Y0H6B2WkwA8GKKDVJnaJWPUKyhdXefdzspI37Hcj4RXn6KlMB3zBXzQl8-Ka80-eqrZrlsaPbIgw3wVSpi0m9rTiR1pd8hjeZMoB4tnZdZcjGC6Kz9pj0zuUndfQWDHzQ-zMuG1IZ6IbwVH7IpJCSaSDfx7-lvQWMKO2LGUl_LoBA2iartGzksA1QlZqsVf4Lp8xpUaazJfTO1tPpbilc8geUkZs7lQVr8e48VoLUhyQwsXhiA8jE_jvl3oahEAEbrEfwR4oTmf6ZDk4IFIdzo2npZVliuR7ABavbNt-2SnQIMDeWdFpo4EsAFdMu0d73BnVOH1WT0t7bl5s_CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm-HdSwuCVhNfwnLwp_Qb0k5EeoGIVpkuE9wc2mXSiR4Q8WEFQApzzSjZQGRzz8ihzJUv_1CE1oU97f20TTWEgn7XV-oX9KJAtx3sGO7H6udEu7H6J7P5nOzY1vVG5JFGN6xCtXIwO11OXjpiV4UMAlHW5B30Fcqkj3CmPoytcP8iIbZkbvNqL79Cw_xyKTts0NVLPqtwADwWwgwrPWRLXAwL89Kliv2YUSI0p7YiGy7GtYLejkptIrDwJ3tdl2sL6cl1BDB5Y2DtRAFrGs3ILss8f20riX0IbLn_fQy7pTym1f4p1vBx_unMWjJUrbbVWJkdVc2dyJxmUfgnG10Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4B4hJzUQbXo9NVDFT-LlIfZUE3jUqqUEVTkABjIvoZ7Lt4zgj5b0MHAIV5Y2wrzjrnDcxPyT-w80-dOfgXCgmLx6JJC6zEUCOjt2uMTmlPE4MMzwiCNtJh8kbgIbD_q-9W01GfJJW7J1YsajQhx5H4IqFKZ0_WfJWmfbUV2DLNCIosNvdQv3ho-b1M6NTCTnTX78gbTGQvMe8V5MvHAMJwQUOjUk3pDEof3Ge1VRHm83riFltdWvjv3JJmIfgL5_0ATP_JwzvAZENksPYR6cqNG4Hneuq6UzHUVPYt11bDV5iMCu5nYZGGSTIzs8Dxh1GuTtCf-ZoKKatoHZkZceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-hlNx3tZ0l0DH95ErsN_GCcf-U86zTpSYr-LZf92WmrE3F9UGb0FzuVfnzrLkc776_NMW6M_kNcI3ibAOhGTcraqjd0QlZVVFdKVbqxOsK9MkuH1nn5caXCQM8_kP8i_hSwQgZQwYdxLeLvbuY0swna3vR3GXO-_Rs9mon3UR8NZeHtsOcGyJHv0N_ZPL58X_GzcrZ_Ie0mYhH6BmFJRDR5hby7OVZWtJjCRasKYXz3SBuhirJkMiTYRQrkKM1ZZ6EERhpAnR0_oSgY935tS0tZ9-8mttRCr4d_8exgEo6EMZs1jA5kt2baHMtP3HH0hYI5U3TwmS3N1OoGN3lWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idb-x59Eu9Fm0UF8qRAyZPUGKlJRAWrvXNiBrX-wXhPIQavvL34IADYCCLJIs-F7pV2mOYYpXDhf-GFOjZt5AICEVxoGA0j0vZHPadZUsEMpkzQKrepy43-85chASSNN-_H-AnvZd_DMzsYcW4HLyYVHVq8SOgAEjKVAeuCuQfCOCiU68hNvwFiRI9QGGEG7FCcMSi4hh3SA1_YXVEemW0NH6-hVhtRUIHxwfvMXMojNTOvccgWg944a6a4KzVzsMvJgz2pZZLlm3uFxvlhd6SYWUIsORJZaFqL8qD9SNoJ-ft6kovKNkVJF3clLFyZxMA-g0I0azmHgvNVyrhISzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=cBaP2BXxoySBIWv0h3wMP6HIsYfsfWiXC2J6Tk6sqZ4Xb-niZ4qBhMDnx8FabCe4Z94eJcW7QL6WNJxmR5bZsaiy4d5LeCRNGUjIg_LXYqWnbblPH6DyrYX4uR9zoIlX2xPsvULxUhb3CrnSxH1VdnaxyPPGkvl3jNYOClU_N-Y0zdG-EufDYsJ8T9v4zHkpftTAP0M1-26HCIWC3Foz7AJhwQJVHVchgjppKhSAx1x0OfS0TdXZmaNpzZi8PK9mGdjCrdk3kA6RbSTw0PYkvxq7GeH1ti1GZHVOVS1kfDMz08wWD_ZKIPGAF1c3aBPExkAk7ljq0WbJkr9Yd2B95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=cBaP2BXxoySBIWv0h3wMP6HIsYfsfWiXC2J6Tk6sqZ4Xb-niZ4qBhMDnx8FabCe4Z94eJcW7QL6WNJxmR5bZsaiy4d5LeCRNGUjIg_LXYqWnbblPH6DyrYX4uR9zoIlX2xPsvULxUhb3CrnSxH1VdnaxyPPGkvl3jNYOClU_N-Y0zdG-EufDYsJ8T9v4zHkpftTAP0M1-26HCIWC3Foz7AJhwQJVHVchgjppKhSAx1x0OfS0TdXZmaNpzZi8PK9mGdjCrdk3kA6RbSTw0PYkvxq7GeH1ti1GZHVOVS1kfDMz08wWD_ZKIPGAF1c3aBPExkAk7ljq0WbJkr9Yd2B95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=eMtN6Llbk3dFUTIAonCrIsXOEzYcRJoyhLlOyxwzoPyJVNx4mEnD9dflEeCh7-HclrmNKYpCLN3DrwHpaCJrZHdg6V1QKScYpr5ZzqljYfS08W0_W2fy9VIKXEsW2Dvsr6PpIGJRZSVIVuDeepAn4XZKNpWTOMEGUFNwCyGS0HlKOKzJltVOhhVXX2kIEbwquE6IdoT_Lcm_RIkL6OcoA4mK13tvpyP5J-_n0CfgnGa6KaSujTC7kSpwkojt1YRnw5xacgN77ahIYVpmF5z73JMM8SqQrdxwYbYb1vaqIevHU4Vrr5qoPtmzKROw2EpxBbCCLHR1pEqbJh9Nwd45GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=eMtN6Llbk3dFUTIAonCrIsXOEzYcRJoyhLlOyxwzoPyJVNx4mEnD9dflEeCh7-HclrmNKYpCLN3DrwHpaCJrZHdg6V1QKScYpr5ZzqljYfS08W0_W2fy9VIKXEsW2Dvsr6PpIGJRZSVIVuDeepAn4XZKNpWTOMEGUFNwCyGS0HlKOKzJltVOhhVXX2kIEbwquE6IdoT_Lcm_RIkL6OcoA4mK13tvpyP5J-_n0CfgnGa6KaSujTC7kSpwkojt1YRnw5xacgN77ahIYVpmF5z73JMM8SqQrdxwYbYb1vaqIevHU4Vrr5qoPtmzKROw2EpxBbCCLHR1pEqbJh9Nwd45GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=KbgwtTF4GR0SQsHMyb5JN0qNSbd-n9t5698BK-cDkcbl8fsHID0zW7Zy_4gEtNygnyM4v220fXVzARUT72ZhuMDPZqsjb_B4qhOCTt5bjNGTgS04FXUUXDI9H8orxJ7jwD1v728UASqh3qNmKFRXxYRa1RhSQ3wmxp57mrYV1Afqf-ntwZX3XV86AgtZtQoIaUNt-YCRo747FzHckiy6x_VySX_nJIi3KpUfmDxz0pZzD9qp-FX1ziX1vURKXgi1DoM7I6CAJWsm9lL_ELqLAcJC00KaM_Aeqynqy-4Jl6rVURwOOU64zqHnBB1jsRTsTDLvhTcYSaYRzdsoGu00Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=KbgwtTF4GR0SQsHMyb5JN0qNSbd-n9t5698BK-cDkcbl8fsHID0zW7Zy_4gEtNygnyM4v220fXVzARUT72ZhuMDPZqsjb_B4qhOCTt5bjNGTgS04FXUUXDI9H8orxJ7jwD1v728UASqh3qNmKFRXxYRa1RhSQ3wmxp57mrYV1Afqf-ntwZX3XV86AgtZtQoIaUNt-YCRo747FzHckiy6x_VySX_nJIi3KpUfmDxz0pZzD9qp-FX1ziX1vURKXgi1DoM7I6CAJWsm9lL_ELqLAcJC00KaM_Aeqynqy-4Jl6rVURwOOU64zqHnBB1jsRTsTDLvhTcYSaYRzdsoGu00Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=RUvIaHoEaQQOhx4OZSDhRRVc7PDo6klDn6ZlHKKHdyuAd-nekbzQRQA0ROvxdQW36R9Iod73t7V-C7VrgHh__mrveV9i7cNPofhXJC0EL0o4QOO4F8AOkTsALEtFkeoQtQb5P3AbOhDTbcf1LlKGu4K9V6gZSuPbvYzm-R3LWpsHVvQ4GInDGBRE2bXnyftBNo-KZaP8V_gX08i82AXakLma25tq9kX61FuGg15-Y6VFxssp_QukNffProjCkLPS29R_Pu3hXWPZZIY_lTYx53pQcQZUKf0EAUWuuYmyP0KujwzKpU-xOFsWGY0WAdPvGz8Ptp1HEks9Qb9wNYOR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=RUvIaHoEaQQOhx4OZSDhRRVc7PDo6klDn6ZlHKKHdyuAd-nekbzQRQA0ROvxdQW36R9Iod73t7V-C7VrgHh__mrveV9i7cNPofhXJC0EL0o4QOO4F8AOkTsALEtFkeoQtQb5P3AbOhDTbcf1LlKGu4K9V6gZSuPbvYzm-R3LWpsHVvQ4GInDGBRE2bXnyftBNo-KZaP8V_gX08i82AXakLma25tq9kX61FuGg15-Y6VFxssp_QukNffProjCkLPS29R_Pu3hXWPZZIY_lTYx53pQcQZUKf0EAUWuuYmyP0KujwzKpU-xOFsWGY0WAdPvGz8Ptp1HEks9Qb9wNYOR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sH64D5DpnVLUsSTpuKCa_k9Jojq2pJpRetmZ06Uj0z5oHOIf-uKZ5Dd4r9QvQtgYF4ZgDRk28a48EA9ascRVIzyAFkahWr8N-zymPxs1KDqYNsddMvJz51bZbehKZjIQpvseSfTQD9HiJkgx4t4LzkD-UJmxNcN6kxLwuRB__pX_qqfFEi1VidfqAtw261FZGLW5LDLn7VI_MKd62kj9NgWa25ViWP93nH0P3oug-TZtr0y0ZJ4pCJDKtH9TbnCzZfoIfx6yupyT2FnZuRWklXr6TPipfYP-_ay8ykYRvy0XL6pNqxBZPANpot91Igxr-4e_ovow3W0a3STcSeozWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFYYhkQqszSoyN_uzN6XLvNaeI2-bbZT_kVd8ZhijFDecFFmYpv6R_Qx74YB9NiNZNcGlecGo10fzoE6cHa9octYgRvEj6DwhcZFVDwjP57CQz8oCJT6Kdlmx6NC1wncZHd9HF03L3aO_FUaN08KOG4gQ0k9gj0vd8QMezuqeDlOkyBF7kclPLI0ikaZBeJQYDkZKfKi0wloU5SNhe1ucVLww8ejpnqjFSohaOQyxqTHgY4s6f_22fBjZ7_f5rN355Z4zZM2GoB6Cd_7hY3B4pf9jrQvJvR-7Ixpl5IMgX4fD-JYbR37IeTmWVVxwuGyWqabUqNV7LliwbBkgSPcZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=IiBqtBlYktUyFT0z6oiNC78t2CEe3SIJ8BN0z7S66z5Rqd2Q-LeTT5SREKg8Ofb44Lqa7UVQYK9l22qwdQCtxgOgd_0NXrwG4mnpWp5NPKX7XTBuKIx8zeLvmIR_e7W4wat4OEMOSEOQXcExRXOjeRufSCw2j_kRPVBpwNv5rQZFT53xu2QtAYayov0fiDLjazKj8bQJIb1MGTtfpJ8uzfgmCZHgZLM53XgwU_ulbU9JaVCGEbcF5QIOspFTxqgqzodk6OSzRCFvDa1iP9MngmdWOVDF9GXzHOC7vKDa6GDxj9ZZG87eGcHB7x2V1_JskEZpXqufW2StUJ_FSO5MTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=IiBqtBlYktUyFT0z6oiNC78t2CEe3SIJ8BN0z7S66z5Rqd2Q-LeTT5SREKg8Ofb44Lqa7UVQYK9l22qwdQCtxgOgd_0NXrwG4mnpWp5NPKX7XTBuKIx8zeLvmIR_e7W4wat4OEMOSEOQXcExRXOjeRufSCw2j_kRPVBpwNv5rQZFT53xu2QtAYayov0fiDLjazKj8bQJIb1MGTtfpJ8uzfgmCZHgZLM53XgwU_ulbU9JaVCGEbcF5QIOspFTxqgqzodk6OSzRCFvDa1iP9MngmdWOVDF9GXzHOC7vKDa6GDxj9ZZG87eGcHB7x2V1_JskEZpXqufW2StUJ_FSO5MTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvrjyiSB-DCWuiEEfFjdniq3MSA9yjpfnve0NT6-9ONLD2kKQQpBuuG1IMmWSNgoJzqW8Ii0NXuUvfXAOOMYaf1mek-k5Edy2evAu_n_OJSx5kIM5AB0wBtvxQXIKljxRw_lGuawbG7tm9PpQk6AoJvDQKL44Poo-A72dFC1XaSuPxlcNw0lLmzKdBXUFgL6_ILTBeI4Z_-7vgv1bTHOwbvX2GLk5MfI0NR9Z0JlBIs8Vz44cPBGCc6S9t1In6PVqgVBXt1mSfdc677cV_dw841Ifzbg4bhIWoCtoePRnI6hgYumARHIQguLoPtX2vq5tGvmIL9IWXlNoL5KS6c3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=h5pbUF-D6h_fVJ40UWAO_x9FpnqR_aBz5xy0rxyLs2Cy6edVSDwPsrw9Zhl2nY59yybdMhkqd4NdOFdZb9TkL58pv9nZe8JJuqMMnF1MqKq-QswlUUiLmd_flTy3IQdIOV0P3ZaqZtNv4kAAoVGXtRU-IXhjwZ7AJqRZO7ClF9WEeE_9g6m5NcneDlgSe0mWPuG9u4c05HFatpbTGJwrJIpaiIgVhmdkgFXFnBJKV9xz0cFqz3FdG6gaUEP9kKp5X-SXNCWMRFBbeLLunP_3kHlagZVfC03o_q4IjRKid1Cb7YS3jU2m3u0-BDzPE8MPauqGJItP2Xg93ItxWA9elA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=h5pbUF-D6h_fVJ40UWAO_x9FpnqR_aBz5xy0rxyLs2Cy6edVSDwPsrw9Zhl2nY59yybdMhkqd4NdOFdZb9TkL58pv9nZe8JJuqMMnF1MqKq-QswlUUiLmd_flTy3IQdIOV0P3ZaqZtNv4kAAoVGXtRU-IXhjwZ7AJqRZO7ClF9WEeE_9g6m5NcneDlgSe0mWPuG9u4c05HFatpbTGJwrJIpaiIgVhmdkgFXFnBJKV9xz0cFqz3FdG6gaUEP9kKp5X-SXNCWMRFBbeLLunP_3kHlagZVfC03o_q4IjRKid1Cb7YS3jU2m3u0-BDzPE8MPauqGJItP2Xg93ItxWA9elA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh3ACbDf6370Pq-aMbXiZJkGv8lmq8gRM0Bs-70hUOb_9mOGdGk2wjVoo4Qzvz9cdPfjZZ6jK0Sa6qnSczQRcsCtXC_Dorh3CjuWd0yToR2p8ulkJA4dYIXaNcampiaoojoxpEsFyCiMN0wwCIVog25wOTOhBCqNtcEU-6oxiZwjfD6J6RVTAL6kUvZ3qe3gFE4Lo3QOpSLZ9HRjc-iKIm0wx9A7dMYOXtNs1ZJ52SzZI37cxNj8xDHwdrUpBbFR5KiuExrlDjRQG4PHEfNOfUbRcyyBYIhe9U5O7oD_vzxqvFXag8zT4Dgreuv68hnQQCvjoSjRcZ1U16A2BmcqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gehymbdneCowX9ARksyu--pKIjt2pIFy0XXLPfXMMNOr938ML-na4reC_8K5OK6CrER5KNJEhLLFEABvfurCv9CKNwQblEU_EIghEOkyJtaPNgW5hoziDQC_nmXBSpOWC-aNhHtooFum_S9gemDjeLApHSvgmcIOqGUaNsGHEeEmnbfxkAy3ySxp6SnbVRt1Ng4B7Mj45pk4nLfkrvxFLb8yqy-XLFwoKsMYAVSwekAMqQzv-IID_iJKQgXqElvSXuqBHozikwf-YrRENdOZ3WoZWoiEd0RvxqxmQxM2sX1LMbptXZFU8zVTTe5lY5kxutsGc9Xe0mxyT4jLJyND2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=O6BbgMG1kxYu0iMPO1afcvtgXjTlWAyEnk53EluqJHFaZ8H0e8TXTH6_lHsqEq03rOUQMWQFBadvX8JyTrlzrKbRV3i-4ycMjUzrEXgcbYmlFvyjQvbmbf-ecSinkHQuIYB7kypPr-pmD6PSRFMde930IRipEB0O2EqqCVqNSwEyFTMFhpv1d-aaGl1IS6irBBHjLV9lg8eLUmFuOYEcUMVmcQP3T1QrNbEtEtIys72kxCQWU-QnLGuzJAi3Ege9jVxUAGYdY0I1QYjQ-cU8VlIBjv25ztOuygAO8MzqaXcymnOVr3KtTi6FjrbRKRAkra8pUoo4lSlCj-r-dXBvLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=O6BbgMG1kxYu0iMPO1afcvtgXjTlWAyEnk53EluqJHFaZ8H0e8TXTH6_lHsqEq03rOUQMWQFBadvX8JyTrlzrKbRV3i-4ycMjUzrEXgcbYmlFvyjQvbmbf-ecSinkHQuIYB7kypPr-pmD6PSRFMde930IRipEB0O2EqqCVqNSwEyFTMFhpv1d-aaGl1IS6irBBHjLV9lg8eLUmFuOYEcUMVmcQP3T1QrNbEtEtIys72kxCQWU-QnLGuzJAi3Ege9jVxUAGYdY0I1QYjQ-cU8VlIBjv25ztOuygAO8MzqaXcymnOVr3KtTi6FjrbRKRAkra8pUoo4lSlCj-r-dXBvLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=rn6sl8F54MlICqQ1O8r8NKcgy2bvLaTjKZt0owXvniSNKAcJE6qU-WRqF5rBQu_ZcxCVKz02dy-QaqJ6Qc4KH-lw-hqDk7AA6D_rbhjQ9s6RuiKGgbSplHQCtjXjknnsPNxxTS_tu-eO6AIKA4mAKlQFuKgKhyj5qZWjvYkS_K-Ydk3GgtqPw7XwVmCqfx7w7-m0in4Dd_UmVdOonOU0SrF5LPVLLJaRari8tdr5ewYYFuIjyFUV-AaHNUkYPsGM2o6sXbe74eNIxSvINMQqsBEmKU8G40BfQwAPGbiM18rkcmdljwI6AWLD5CWB2JTqvW-CKVU_Qx4pneAvTnKasQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=rn6sl8F54MlICqQ1O8r8NKcgy2bvLaTjKZt0owXvniSNKAcJE6qU-WRqF5rBQu_ZcxCVKz02dy-QaqJ6Qc4KH-lw-hqDk7AA6D_rbhjQ9s6RuiKGgbSplHQCtjXjknnsPNxxTS_tu-eO6AIKA4mAKlQFuKgKhyj5qZWjvYkS_K-Ydk3GgtqPw7XwVmCqfx7w7-m0in4Dd_UmVdOonOU0SrF5LPVLLJaRari8tdr5ewYYFuIjyFUV-AaHNUkYPsGM2o6sXbe74eNIxSvINMQqsBEmKU8G40BfQwAPGbiM18rkcmdljwI6AWLD5CWB2JTqvW-CKVU_Qx4pneAvTnKasQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmuM2hww3A__MgLq8BiCCY0-1lMAF26eVMGJ9Yz89n2DgG2Ys1AgDMGfaiRUB8Ig3ok9ZEhBCkEjb3sOqLQw240XAhgiRodmT_FLe7AzCQyOTajTbIx05XURrhFgNhPR46MxFNGN0oTlbutB7BqYEF6zUunvyL351WfM1XoMMKBiWfLd5n6hUKk7ETxJ_8Yhh5lHsHyHSbVa-G5p8U7REdQWjEqYu7Zj-SHkBxBEpPgP9W2z34MjgVNs4cHalm66GjMXYPpgBOiKIybyyQXF3YKU1akpmXJdHeZhbySqCZ1xxxb9o3YApjFlKznzGldJGizaZQOp_2Ih_3wepKI5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoFzuZB86ThosGOPYnee7bnPtVPuMF-7hkVv0Ab_xUv0RadTkFtZwEq280qL6TfQR2BVejwYKqOUAYVV8P4G_HYA29sews6fIMtssUQh1Aa6qDzNceXIVpURyF0PAdCxTP6Gr1awpNQXkFm2hZy7VsTEg2titJ-7wL1DRgeNy6MuFOxnH-NbFhbsTE_hHEMMsRaNZN1hT_MsT_2cRUwr6Yd_lVUEYrAhIOYkiKVOt-bPwfvn-2D1LVBDFYV2DbvHc-GQxxkOhBydKOACfioKrnUzXuOdPpRCutmjRundMX6aeEVKaNAD9jnI9IuSn8KR-Y1kEG3nYouuzzYDKB0Trw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7V8yfy1NT3Rp5wzmiuZJ3A2qDNjpMeMAg2oxm-ywkI_Jy0x_5D_9KOMr2Q3SMotjzPFkxx2si8fGttwFboBPO158hiX_1nwoPPRdpyR954PvPx7HUffxaOHDQB-O2WQeU9aWpP9DrmzENCNKih5GJER_Bc7DShzfsZB_Wx5YJix4NpjCvxUM13oYFD0epodi7Y_r1MZnWZxjpmSCwiv0uEttMSlxHLTHEbNxs8kUsDKleH6vxIGFj-bL7QXXzqaPkrsWApYfA_Sosq0PEGKhhBAMlyReeZ1Htb2A0LY6IqDeq4iRs7zudBFaz0_SXwAZEeY2OvJxyiX3PqVRBNyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
