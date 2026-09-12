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
<img src="https://cdn4.telesco.pe/file/ptBShGFRi0UIXwwbdd_hUY48Ph30WOmpWBSHiu3f4jxbcQLMH4DlLtYZKbpejm1Sk-5I6ZqbtCQ23reWQwAl3NOdR642i3VnDTfYOVryr5PYP1E130DitS6x7PjZMdlou_ySGJ-2QYAa3AKJxy6OmhUvhBsrUzbufTk70umJ9uDf-zIop-HwsvOu6iFMQEFutmWHcHbHEZu5del1bl2DG8qcsWl5dQr0q0r0wgWK_2DEL0kbXPZaFYd0SaBwod5HC0laoOZxhbsVFD9nORZ-Z2xciPFvnZYUgF2uRtttjyk4ibjBhlep4Fc67pQNdVv2aL5jxDrxpgTshHx4aCMGLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 528K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 17:45:14</div>
<hr>

<div class="tg-post" id="msg-29606">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1Gbneqv_VbXrcwh9B4O0ax4MH628kR4JSOwRLyURks8FlcAFPfqIB4lKFd-cL9NElnQsk4e5wQKO7E1dhQTnGGnFg0RcQWIAfFwuSg_h84CTfiaSpy5_lIdOzuHKyYNHktMF_FEQ1XljwW3PmVYzzAq5zLBWIU8hh0UVtj8EFs8xgIHsdMYUf3PwyYU8WHX-9V7bzLxXrA8B-mBKm5JaWCznh5DUOY_CSybXHq3XkwnCD6E26rDxnJTFRN7loe2rilIB6hHqIqmPTNtGPGQkZ-rEHK0utd8g-lDq452Kpa3OW2k9ejEEHHP_-IgE6dqC2QklX-Y1Tm9LmBPcPOptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/persiana_Soccer/29606" target="_blank">📅 17:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29605">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQ_i44Cseb8uHwThRoWRXsGhBJdzIPcb9YxRNqUxNTybxGKvLVFoiNsCwxpKXzEFW7cTMkfdo6aws4irdLqYMYOWBKynwn_vdUwTAOLpWDbFqU9kLQzaJTpbs3x6y_EglLm3_lRBFYRhrpmPgPA0al8zfhk5gl3DfgJVPrsld1qXmKKiCpnZZvCfZZi_rfENsXailOKxjsif0Iegd6rpNzhKmBIqygPEeiJRGgXA-4ehJLNmtCMAp07ovTZJwp04G3zu0MASZCIjuSU85CHYpk3UloYfgFKZwFCdGNc3vpGMb3zV5ghFKe6sVrEEdtchhDKWAzoRwx5bJFoDKFlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
برگاتون بریزه؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مدیران باشگاه سپاهان امروز صبح به‌مدیریت تراکتور گفته برای صادرکردن رضایت نامه آرش رضاوند علاوه‌بر تومیسلاو اشترکالی 50 میلیارد تومان هم بایدپرداخت‌کنند تا رضاوند تراکتوری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/persiana_Soccer/29605" target="_blank">📅 17:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29604">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js4tgGy7pd_lyN7VIq1c5T7iAfqZVZB3wobrc1Yl7mI_83Ohw4Hov9-R1i_b42JTG1PYT5hois4W2EdFRCD7ZTLHsXZLMzkaPc4Shz2q9FSKjdmKXwKXMDsgU7xIqItiYQyNmw0NM7l5Qi5SlGLnQFMI-8hznqknzSfErYuld6DDBhkDaWK-IMeFTJuCA-vqAwCkiR_UtYcqgQKaSm8alIRiP-JVMkXNi28VwPljpGa5jv6kMq6l9VkR-dd6r0hBNnLF7oWcSSma_zvTPCnHLIDyPetHYUDzpL8ZVY7ZQiVcdaPTjnF8qt1g0ELjihv7UdSfyuA2yVcAcDqPYzvd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
با برطرف شدن موانع موجود، کاروان تیم فوتبال استقلال تاساعاتی‌دیگربرای دیدار فوق العاده حساس مقابل السد در لیگ نخبگان آسیا، به طور مستقیم از فرودگاه مهرآباد تهران عازم بصره خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/29604" target="_blank">📅 16:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD67VcC34oZYj3UvqMeiTr_DW7PRWQeVahl25Z2CMjMoa-weTwAvO_sgcIH8U-e8YYeoFCFr9oHUh5woTVsdLqtOW8RdZtv8l-vlMQLnH5EMRQICtgGRPeHFxFLPHPvXbwZWYgb0p0zxzkq7lVA8AmzZwKat88VFm0ki8zN-6Qo4cc9RwQfytsOcbO6d0bLnko4G92hKbfMBmbUNdY90qVUdMBBEIT4wCjZJn_uF1TddT3hl0fZrmIGMRVXv-xxRuvMxvLftMsQlch9JXCFl617NGwn2fAxaiu2PRaynsYU6xVEqr1Lox6fFV_6A2UdVyAbGzHM_kc14D5e1IOT16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه‌کامل‌ودقیق دو سری آیفون 17 پرومکس با آیفون 18 پرومکس که دیشب ازش رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/29603" target="_blank">📅 16:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=FDWrkKHd9-ht3VsmHeTFjGfAIUkyhsuGlFFr_EvpT9nmHIIw4xz82HRx-3QnHsQ6NZrOwrWlZ2ZCvBSKktG-4KpwBPtfSn_2xEZiAbQZx8Lu8NQyV0A5hNtk7fFLqlqX0yunh1vOf0LZYCQRxt36G0JB_INccYog_sXSKIUC88P1ezy-O6HC0xJ7Ed8yhW9nKh103BbL80x95TNZ_4NPnlCOOEWL412_Egj49ggJ29domeYx7nEc6H0ULOiDfqRKau9xBQ55nyeISMYckvO3YnXOzwiJcUxl7vF-4w1nZWt50pa1JH4dU-a_e7UMPrwpDjd3ylKHxTjayZqAHQ_ANA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=FDWrkKHd9-ht3VsmHeTFjGfAIUkyhsuGlFFr_EvpT9nmHIIw4xz82HRx-3QnHsQ6NZrOwrWlZ2ZCvBSKktG-4KpwBPtfSn_2xEZiAbQZx8Lu8NQyV0A5hNtk7fFLqlqX0yunh1vOf0LZYCQRxt36G0JB_INccYog_sXSKIUC88P1ezy-O6HC0xJ7Ed8yhW9nKh103BbL80x95TNZ_4NPnlCOOEWL412_Egj49ggJ29domeYx7nEc6H0ULOiDfqRKau9xBQ55nyeISMYckvO3YnXOzwiJcUxl7vF-4w1nZWt50pa1JH4dU-a_e7UMPrwpDjd3ylKHxTjayZqAHQ_ANA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیویی‌از اولین‌پنالتی تاریخ فوتبال که کلا 0.2 ثانیه توپ تو دروازه‌بود. دربازی این هفته لیگ MLS به این شکل که مشاهده میکنید بدون اینکه توپ به تور، تیرک یا دروازه‌بان برخوردی کنه گل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/29602" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLFnfI9zvMwdyRfrEfjBP3rv4OzJt9wio0tYdmFXzBuoZxwtMHf4pNnGpw7UYuO6X_eGRh3smIbHx6Y1HcFdDuUsFhum6ZztLWJM0iImm4O1ZQlCy92FZR7hT2ynsrs4bHAqvPbfls_9dNyJ67gIZupU3qYiUIS2_pofFqBWIXEQza3c1DubJxjNtBiaKg5pqqeohLGVsAY2ns0isFARcoHb3g69PLFIqBJMqhC_jomHyCxjdmrt1zg8OZznK2eX7V2boR2gbmGSLDkVxtRLoYDcWk1joDj9zmuJNUqPuHKRAZd7sYCf-wyeHnEZ0ACx4XjMlBaeWqVJDzPmopPeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/29601" target="_blank">📅 15:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2KAxxQgbk9MWZQTcR5223bi3kInzi_Ngl3LrcPengMZe-Y7KJDXo6tOHsH-mhgbXsJcMNEjewKBDVOchQ1-Tn5UNjGT6-jR8GtcLdzroM2WIGRxswDgfLvQS_r4xRRRxt06h5yQ_NCipoZ0unvXVxn1qU-vM6ew1arX-dFdCPoYm79d4shIBWLTk_yDoBD_H_7qjL_0EBIQS4KO-ltv5VBy6LCaybTLOjSpKYuV-3yk0Z_gEJkACLfZDrl3KgiCvT1ZdlrHSXY_0h54y9kDPJF7iyvME2UKV4y8qJj-9VKD_I7zSsrKNuIvEbtVMvhkPa_t5OXqv5XPPAc2em-WbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/29600" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epWHa-_4Q1w1w5YXSJCrrVqW60B7PVKvo7c3Argnj5ZRjsL_ef6Zsf6W9up1BBdHI0wEoOe9z38Zkd9ZyT08E8NwyBbVZX_VsH6PuVX5A17BEYexMcizellvzLsOsCgs-RSyNWIBguIb9uCzw-nlEeQTwKk5MbwGiYqa5yK0-87s64DDMBhZgKnPwgiGJsViumn2Wjv0j4Zp0vH0R7KNA5NyByO0qsMvv9M0K1d62VUlIqOgl0kET4dxWvF-Y60H9VhQp4i1bMEb3Ea3Lgnx-Sglv2jhB5Aq8t_ilLnC2opewq2NvVhJErzuCMlYzit7qHhbfIDSvL-ce8_bHN76WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/29599" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29597">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=tx_cpQBtTCV4RWYZZ3xKf9vT8Ar5As6FUKN5BGDCLfeIoyjUQ2ZbkU21HuzPTmo0mlfR6I_ZHGWUwOAPnxoLhpwttrcOpj5up7sknYjaFwi174fB6bFTdddji2X7585OrgLbCQcgIUmaAA9X9vECbvpABuUvfkZYuj2lngy2Cl9wJIuV6ceJKlJ9lCH-T39fU4v7wBxgYb5Akfx41lu-_Q2h73n9N2VbvHpNBS_CPMhJl-CDmJWb8F2DlKRy4Xp91TWu3lIumETxYVB0NcIAsnGKx3A7aP20XcvUUKk38qOmFiFYz-m_xNY_xt8mAky4VbGxGjG4tOqPc9OkADDeNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=tx_cpQBtTCV4RWYZZ3xKf9vT8Ar5As6FUKN5BGDCLfeIoyjUQ2ZbkU21HuzPTmo0mlfR6I_ZHGWUwOAPnxoLhpwttrcOpj5up7sknYjaFwi174fB6bFTdddji2X7585OrgLbCQcgIUmaAA9X9vECbvpABuUvfkZYuj2lngy2Cl9wJIuV6ceJKlJ9lCH-T39fU4v7wBxgYb5Akfx41lu-_Q2h73n9N2VbvHpNBS_CPMhJl-CDmJWb8F2DlKRy4Xp91TWu3lIumETxYVB0NcIAsnGKx3A7aP20XcvUUKk38qOmFiFYz-m_xNY_xt8mAky4VbGxGjG4tOqPc9OkADDeNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان پیاتزا بابرتری قاطع 3 بر 1 برابر استرالیا درنیمه‌نهایی جام ملت‌های آسیا به فینال این رقابت‌ها راه پیدا کرد و در فینال برای قهرمانی آسیا به مصاف برنده دیدار امروز ژاپن و کره جنوبی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/29597" target="_blank">📅 15:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29596">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T55o4m2VPEQNYrUvLzFFfVMaZTpaK1-8bvgJOpsTLprY5a1GiVYmeUP-eNJW_WnqAEAMVl0pi6V8djBrDY_bZKnuUhgwPAKPs8AE_1r_g1RmhCBW56BaVEkWRewaSTYh8keHu-AEdaSdtz39WAReCJ6WLFHrOvtTJSuESZD1wKOAEtDlqIYrH8a411hwu-zOK6ViGCcbRILOTwLVnTvV2ZItBDqgwTfJO4289jGsJkkYnfO61EglBY3u-6JwsXBYHr1M181twOmlP-Q1IQ_jwjmAWwN-2KTHIXdwotEdMAaWBWiY6RVIs4X6_2uX2TBtSh9EnhKPeEW2Se0bT66XUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاریوس دروازه‌بان سابق باشگاه لیورپول در کنار همسرش دیلتا لئوتا گزارشگر شبکه ایتالیایی DAZN
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29596" target="_blank">📅 14:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29595">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wslx7AzbYttC3dSRHXvfdcnJ3MEMxHIzgcMdyA0utFHPS_T4EiG6J_jRrFJTFoOANjjVADS_xiTJYq9aq3RLiZnvGK8ko2eygSY1to6foiFE2ziy-c5gMPxJ4GsVjrr_CjIyDO4t3FehOOgcOpVH2f0sT5evy3uTg-wwkaGMYZr_03K4sJIEsG3mMoLLpXfHgxym8GCaQJepO7_MMr87qhiWVi8szMqcM8mmfopJjMZEht7jZgEznPix0VMsm4YqWchCNGEQBxrqFSaZWqZGR_TE0iAkzzza3Zi8CpvmFzTll80Eq8X4GEhtB8nd3N6B0kGP4FdGEFSCCW3F7jsYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌ویدیواز اول تاآخرش‌سم بود از دست ندید؛  مهدی توتونچی تو برنامه‌شبکه‌ورزش نادر محمدی رو اورده بود رو آنتن زنده بهش میگه شنیدم میکل آرتتا دنبالته که تو روبرای آرسنال بگیره نادر هم کلا ویدیو کال رو قطع میکنه. بعد توتونچی میگه آخیش! پست ریپلای شده رو هم…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/29595" target="_blank">📅 14:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29594">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozhCqX3sUhxnPBG20FYBiYuZ1ebUdK6nIsSgseC378L3CyEmTkPyIF8I4Qw3LXO7X3Tfzn6jVig5CUL6KopqFx5_-kyE-CSlA0MPGabCYJJUY44xajgpXAJDXTseptzRZb3-eyc7TiSXG5bY1ezI7bG46YuYEr3uNjoaPeSWh0K1efYrne85YmAW21IOUvYizp6TZ-pE575zlE93601jRRyubL0Io5okIZDKPP1ipdqZWj6BuPtSGUPElJ12hfTDyGgC1CLJRNNd2xUuPZB8kQ3WN4KCnHpRWszyzqh6vNmaoRxELxpXOCDMH0tSY-eibsA1vv24sSJKl21huzPanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛ ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/29594" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29593">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ro9Ddol6i9_wtX_6TXdieVrYSOeb9TtIJzlCtE-IFc5Zcro2N_yvf9GV_0ti-8qCmOK71uApI1DsWaLl6xQZ5AE7u2t7xN1D1tNkLLbtdZYNUyt9yav0zecDe7L-LOa9ZI5-JrRBCmhJ-pDA8TiPDhZ0lCGQquloeNqUUwh8B-dC1IprmiAFreqL5rTwmUwHfgkjCogc3cdTzuitRdpU5dvQQarlvUscjAl2pOcivgx_3rK-cNCHH9lI0YCC88DAdFMvclSktvgVQTn7sGv4XWIZimn6n3jsRyHabI5c817gXBwb1rKXUZBDd7P_8BaLxcW8dVeLRU4auf2j9cLkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بااعلام‌پزشکان باشگاه تراکتور؛ پارگی رباط صلیبی مهدی ترابی تایید شد و این بازیکن 32 ساله رقابت‌های این فصل لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/29593" target="_blank">📅 13:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/29591" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29590">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp6OZ-673UuICAPbrKiuyvp0hG_bSkjFTjdhMLI31fiSaIo4A0s96EIEssjzu4gurk6tdupFWqmdzl4qP-g7VeXOoqAdAnrLmlTMriG65Y-pP-gioWzqtOCqegBRg1dSidHmL2QSDo1lreuwHcMTJOt3bcMD2nRYfKWIsOr_6L1Y7kPv-9pfLA4MfRv0D-ylDWNmmvRoZZ-mExYASIv1nx9ThFYUJmck5iIknqVEkmToaXe6Og75QbRDkfwmJ03iQk5e_WjeejgpkU8Z0y99InduU1JGn7zUKJNm_dZ3bQNQ_wJLfPerrBpfvlJJUcvyUOhPwHn8XjhTrvd8VNYYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان،…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/29590" target="_blank">📅 13:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29588">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU4LJ3XxWVKRQs4DMGlWNRyQp6kN3BWG_dWNcMb2mps3_1YBP18x7pD373IQvwW6S7F_FpNq2My1XyEkg9wYin3CiXgYSMqeOLadT7St55zT0n8yF1bgeYJL-SGwdttafK4RmX_qa9MRXGmKWYONroum6dGkW5A4kMEU1ocLV3Rf1i_eeZECce0Cq5Opv_2d6mb7i95VqgizRBogoBINMRJ0GvVRlS2VYCYbnpNTzr32wFUA_hH6eK9Wdvyy2dTxAbiedhzE_GW-5kXxSTjK7-rwbqa5nQajOl4iOH39S6nVemJRoO1sjyB3igBOL-YteXm_XAyyeTnB6g6XLMlmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
معیارهای رای‌دهی به توپ طلا؛ عملکرد فردی؛ نمایش بازیکن در طول فصل و لحظات مهم و تاثیر گذار؛ موفقیت‌های تیمی؛ جام‌هایی که تیم به دست آورده و میزان تاثیرگذاری بازیکن درکسب آنها؛ بازی جوانمردانه؛ رفتار،احترام‌وشخصیت‌بازیکن درزمین‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29588" target="_blank">📅 12:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29587">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLWaTYQ_temNHsVC0XaxGGsnLgqeRlf9cKkJtLE1mNZXPya7WuRbEcolxtpaHmB_cNH1tUCcao0KYKUFz03xF0rkDHjCn5qaLd7mIRKx4klZCPKmI13aHofTR0a6Y-gUKu6DvYss1Ymg1lu-fV9MdshVirNY_Hfi4_8A510kMX-GpViUrGUZ45xWTcj4dAsv9uVfCCCE2qLnGnwaJ8dSJFILjnr7-dqomYlgh4MznoC7rTXcGgvvCZenUzNLmqUx788HvmouO7e7GdikGqrIjO0u7sQVk7IMTZgNQ-rI9wWSq1WJupAweFxKApjuAAiJZ9Ksl3LoIRiV1rgsZC-loA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
برگاتون بریزه؛ امیر قلعه نویی سرمربی تیم ملی که تاپایان جام‌ملت‌های‌آسیا در تیم ملی موندنی شد درخواست دستمزد ماهیانه 15 میلیارد تومان از فدراسیون‌فوتبال داشته و شرطش برای موندن روی نیمکت تیم ملی در جام ملت‌های آسیا این بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29587" target="_blank">📅 12:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29586">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=CyGcEBUbhZ6VbY7GcAd4TQW8mHQMMcyBtvbccK5fsZFj9KGY3nz-oxEQKm_izEXJ_3xsVRhxDQM8LRQrwbxYPgXoLU_b7DHAZaWVTWQ67BAHlA5jYNoMaohQlZEQJjQfjJ_zvz6cXSAAo9TINBnm6wZcpXB8U3N8AK64LHvCmDMimnIkuXw9ffby7ATE7NI-LRU_zOSsdbc1Xj5ZAwNfHGrttoBpdDdeoh8EqL86TvfoLQs4aYRoFSWlEyzugANhOU6z3DFVJV4jqgsnJ_aYcJN0xZi4FAIQaHv0p1dq3EE0A5dpfBBnj83mfCCkLHnXIcAtYpTE6YzhB1NiyEO6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تقویم
؛26سال از این‌خوشحالی عجیب و غریب محسن رسولی ستاره 19 ساله سایپا گذشت که با یک حرکتش روی آنتن زنده شبکه سه فوتبالش نابود. بعد چقدر بازیش خوب بود این پسر. یه لحظه نتونست خودش رو کنترل کنه شورت ورزشی رو آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29586" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29585">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrQRO_gazYn-vkH540jSTgT6JiolnGh6d1q5XfJBQ4UuytgjskqsjkQwCOjzEY0KO4WA5zyv6E9Go2JgoO6tcPIeahH9yWyc_Y2xFSdYFjnM17h7TmamkbdYf8ij-VMCZkWK93VXMk_Vz_t6ipWLddw71uw8e4vJUcOaDWiXFYhxpAlMF-QPdUrhJF989DKGR6UZmtnjOkJ4ixZXYOELNX5NEUypOAN6T5x3f9bLjBnZ4kKUL-GcaGDgujMKsaSwZhvHZMqaZHGyq3IH8hOFVflk7Ci57VRAn7Y_YCPuYqiTO1ph-bc7QrhFgkq7ws_flvw7Jm6DNJ8sr0SzGayiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛ فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/29585" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29584">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkgeN6Tt0kVQbDGm2QjSgLP_63RwC7u26ce0yc72PzQwi5WeJwBcPOQQe91pA_tiJoLN94PlULhnUbJ2jh3x_zR_C-1hispNO_g8O2V32Dv7EcHZwHxFlGfrXQQBxivKLky8T9OxsAVNhH_L4JzTbkOi21X3M18sICKzzjxxa708Fi1eKLvd9FvqJtnXxUFTtTYhQa1NGkDk9y0xcNF9nYg1_D1QSid-ArhmLUF1nKGh3zICmrQVlKXFfjv68V-jpmBHfzeQZY0r6kT3yD8sUxNa8P3S9sblOLQaJI7i45tmgvHd7QMU73R9czvM2jdpvy0wy5YR2rZ9AVjQ6sdnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
باشگاه السد قطر حریف‌هفته‌اول استقلال اعلام کرد برای تمرکز رو لیگ ستارگان قطر و لیگ نخبگان آسیا از رقابت‌های جام حذفی قطر انصراف داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/29584" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29583">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsSaVroKEIw1IRiaUpfA_SwEFbYhdygIfoocuT6K37AMa_LdBbJvMxjhDop_utRGvGtA3LBFbwInRzU5xDhc_yAchr_C9ikjDwSVgicYik32hbhTnKVqDka4e7zC9OhwOkCC7jLiFhV8v0KOqooiWoOhWYtpezlkMQdYt2f0sFzHueFJdHJB9WgUK5-PCDEWv2_LJ3lKfIY-pKQ4umZnbpA6CuSihJvc-CBO_NvYF2j6D9G5q2pe5yw8BR7mrhcX_NZ2vHJWVAKJihXgXeV4HKkegsnt_p2xKm8KmJ9EXnQmkabuvkPzxuJsyIgNTHEX8eK26EPjOkbIqA8YJ3g2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
‼️
از تحلیل و آنالیز تا پیشبینی رایگان
از مسابقه و چالش  تا همفکری و گفتگو در مورد رقابت های ورزشی
❤️
🪂
هیجان ولذت پیشبینی در کنار بت بازهای باتجربه و تیم حرفه ای پین بت
❤️
🤝
همین حالا در کانال پین بت عضو شو تا در مسیر موفقیت کنار یک تیم آنالیز حرفه ای به سود و موفقیت برسی
❤️
🤩
آنالیز دقیق رقابت های ورزشی
👟
چالش های نقدی
📝
گروه همفکری
🧤
ارائه فرم های  رایگان روزانه
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6
🔗
https://t.me/+IxmGEx4ep9A0MzQ6</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29583" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29582">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
فرانکو ماستانتونو ستاره آرژانتینی رئال مادرید که مورینیو به پرز گفته بود اعتقادی به سبک بازیش نداره و قرضی اون رو به‌فیورنتینا دادند امشب برای تیمش درسری‌آ هتریک کرده و نمره خارق العاده 9.8 از سایت فوتموب دریافت کرده است. ماستانتونو در پایان فصل به جمع کهکشانی‌ها…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/29582" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29581">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ5ElgYlWErQ-FtbrSuG1Y2ktAzI2F3wLwTBM4wrAZ9SpkTIcKgyAapxCut6I1RDTfk0qzSA_JlQJnpiyxplO9Q-zQ_GtAEp89lmC9DDRYbqwR3RRU41QPFFsTMJO3oMTDhkCkNAUrPSVk059HKLSWOvWf6KzuckmGybYr0xDK9aALyCtmECw7uyjDDyWyNdPAqMUV0d8H6xXHbUQlQpMDE8djbvWYm5a8_rao9T3nDQt0VgJNfhuNL-DC1QWjs8KF6Jx_DVAcPTjOcbfkSZWgH-G8CukQQjOhpIixT8MA11eO02yhCbtvL_NOaInLCy2jgzLsz1GfC7U6L486sHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
47 سال‌پیش درچنین روزی؛
اریک آبیدال ستاره سابق بارسلونا به دنیااومد و با این تیم به دو قهرمانی ارزشمندچمپیونزلیگ رسید. آبیدال سال 2011 هم به بیماری صعب العلاج خود غلبه کرد و بزرگان بارسا در شب قهرمانی این‌تیم در UCL بازوبند رو به‌بازوی این بازیکن بستن و آبیدال جام قهرمانی رو بالای سر برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/29581" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29579">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af01699be1.mp4?token=nQ0mDapzBzeXpD4EiN6CBC2-n11NJ8GO49F8XXMAXyXU8ONRDz8EmcNwi0_RUvKcWqho0jeyT2fORD9yO6b1MzqngTjcAjEhhCqn66gLUWlYCcIIGrrXEOSKttXE3SwA2-Gu-aH2s-s8mCs0mSxmgnTB9VqjUD3gadbwErp2wZ6nR_Z4BzI8DJKqjLQx3uKxCBU_kfS7iCqFicSUriN9vXlX-Dmu08e-edqB6EdEvv09MBVQ6zz-P21g8GOXjJbHuvOHVDHbJHK_XSNSDF6es1SvG9ewxlBVgO63PiBkQQxFzio2KY5cpquBKfy7AGQGh_F6IF3A3urXhHsS1zZvn3PdStG8Fxdkt_mkaN8-FVeCUSXHAkxyUvYLQ5s8nTBqS9Ew6_d10MP7Ve2sW2KJnWK91P0fNSjQ9elZSSwjvikFSYghSsbc-j5IpSjad2Xjz0lrA0FMFIZ4K-Jjpb97eIGr6ogjKiwhX4IAdJUM5e8eey7Y6IywuqI6pz7EMl0RHVfXpRs0cWtIKehBn8xJrVfxakuWxC5fboOJJA1G-aXmhQRe9LbaRO-FCx-i92qQpx1jbGI82VTzHU6Feanh7v81u8ldaR8wBur5WX65ybe_V9YrLjSilZxYXsDWHya0Mq2iO1bWKwo5tuZbg9SGqd5pKiFoPShyUGoOg3mCvtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af01699be1.mp4?token=nQ0mDapzBzeXpD4EiN6CBC2-n11NJ8GO49F8XXMAXyXU8ONRDz8EmcNwi0_RUvKcWqho0jeyT2fORD9yO6b1MzqngTjcAjEhhCqn66gLUWlYCcIIGrrXEOSKttXE3SwA2-Gu-aH2s-s8mCs0mSxmgnTB9VqjUD3gadbwErp2wZ6nR_Z4BzI8DJKqjLQx3uKxCBU_kfS7iCqFicSUriN9vXlX-Dmu08e-edqB6EdEvv09MBVQ6zz-P21g8GOXjJbHuvOHVDHbJHK_XSNSDF6es1SvG9ewxlBVgO63PiBkQQxFzio2KY5cpquBKfy7AGQGh_F6IF3A3urXhHsS1zZvn3PdStG8Fxdkt_mkaN8-FVeCUSXHAkxyUvYLQ5s8nTBqS9Ew6_d10MP7Ve2sW2KJnWK91P0fNSjQ9elZSSwjvikFSYghSsbc-j5IpSjad2Xjz0lrA0FMFIZ4K-Jjpb97eIGr6ogjKiwhX4IAdJUM5e8eey7Y6IywuqI6pz7EMl0RHVfXpRs0cWtIKehBn8xJrVfxakuWxC5fboOJJA1G-aXmhQRe9LbaRO-FCx-i92qQpx1jbGI82VTzHU6Feanh7v81u8ldaR8wBur5WX65ybe_V9YrLjSilZxYXsDWHya0Mq2iO1bWKwo5tuZbg9SGqd5pKiFoPShyUGoOg3mCvtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما روز به روز داره خفن تر میشه! شبکه دو یه کارشناس اورده داره از خاطره قدیم میگه میگه کارتون میذاشتن زیر کونشون فیلم رو میدیدن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29579" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29578">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRzSBBelcyInq5OiG7OxLv9nwaA8XNWaIPxjGEpFcCpOVChQcJNjP9vUU9-bfUHS0UhSo7xLr-45jpU0Wsj8GjkiyZ19-qMe25TJCbkxiT_doqpJ7JzkfBruRMljDMwkCDY0YAQhgcD63dpuH1NJYMWYyYAU9n_CYgySN2sPlr8VXeplkuGFicSooKldAM-T7H3xTEi48ZDJEp5KzI721e27VgKiGBPf77xFXfxtCblKGpNCTGNgRJjINjcdKbYx6HuqMEulwCgvIbpK4yBQ_JRWDa0rodRyb4l0NDz6emPT_nsD-MLwToSsxazW_xbQlJKMr78Txf48XdnoUlKcSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29578" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29577">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJl-Yx-w2lPAd4Qgl05V_2JzeMgwBcQ8TE2rXT2v1-s5lecKuLWWi8G7ROOBNo4VoDqA8vow-1rhX6BMeqUlLuWJY4noqNO-lqJG904u0GEvSoHWL15k2N0o2wCs2KHaNOZB1rdvBTbTCfb3TUoQ6cBhSqaNUKeRJdzJhXgDIK2UtLhq2KfT8ozejbSZqdghUL_nfbrLlBJw7XNUp33Qnx680dGsh9JoCvQhoPVeE9kiI3FPWkqxrx5zmefADrAk6v6nkehw8oHiMgnG_UdKw7JPJHUOrPejNIzRvxhWVgJ5GYgfFA_sBU4nJtjIdm8oBQq6857LK2KoOM7iVUA1AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با این تیم غیر قانونی بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29577" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29576">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=TM7oyf3MnSBsQHpr6NyLdlEPC4jdW_W7RtR8EgoICjqwGjqZSqL3JAXFvtRsJgyqyO8keUGQyq7gReGb2EMBlKIIQ3bFt923CdnZt-xMFW73KJCTQUsAD0W6RPOAL8NtBHB-q1KfgLeypC7hfndbpqaxzrOGmAG1CX4k7R1gpzqmlYqxpP8VUvmSB9wtReTFnxlegMse8IA2eLj1b2EGADTTgBznYMb_LqCLIT-8o0g9GrUuq1zYHs-up52mAUiN3NeKh7rbJvgNiznMKm7WDBd1Jyn4vTZNWHvM6Tm9lREDyjfPNwtfAa9dFJZtxNLyioFcBCQnb4xbJNFyiArjgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29576" target="_blank">📅 09:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29575">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=pgVjYov30yeZ-xAbcTEy-rsF2OE2KauoKuODJhlQgzkQidx6s2di-VfBnJiNfjn_lihsinlbpHLZcecjZ8dS9eYGsNjetx_5KyqtVu-9Ws11-44gDxonHGIXBhDY90LiGAVZ5dPYhlLjt8u1uKxnh5SxM03ZL81AIgDdP9Q_koKYVmSZ2fO1Oemvba75VTOJlcTmH0iOrWd87D0ZfjndL1f3KyFNvyPacMzeLXpn8xeaNMrM6-TcOI80uBNNzo8lsxCC-HfGPkzV0Fa9kI97xqRSAHdTaLqxBXrxk010sQa_DXmi_iNuW-zCAR9wygvqsJYtcsmeQxc8vbYxZLT2bWvO7Ns8e301VlMuhRLtW-1msp1znn-noZ88vosOjDKzf2TsU-iN_U9A0IxHee2GUq-ElFGAuX_YUsuk2f6QOkdt1kPnrHemmx_fIU_d-9KxFUbKSPhYpZ8uGzazavuIvE0c11ZDP5l-X9MMraEnf5peTqACzpmMsyHSWrBBQ2rLxJU4P1ViQDjW9DC30OoRinYLn0IzFNbE6hiw_afShKA1osGWikvYVccU1NpoUf1l46fA1B2B7_e4lEEuH2sNJv-6U5geby1SBK2NgtarMFjanfYDajm7jvdosAdQYthSlA3xWTI09uElW1qBu8vqdzpBbYjI1xitsKBz5B5lVEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=pgVjYov30yeZ-xAbcTEy-rsF2OE2KauoKuODJhlQgzkQidx6s2di-VfBnJiNfjn_lihsinlbpHLZcecjZ8dS9eYGsNjetx_5KyqtVu-9Ws11-44gDxonHGIXBhDY90LiGAVZ5dPYhlLjt8u1uKxnh5SxM03ZL81AIgDdP9Q_koKYVmSZ2fO1Oemvba75VTOJlcTmH0iOrWd87D0ZfjndL1f3KyFNvyPacMzeLXpn8xeaNMrM6-TcOI80uBNNzo8lsxCC-HfGPkzV0Fa9kI97xqRSAHdTaLqxBXrxk010sQa_DXmi_iNuW-zCAR9wygvqsJYtcsmeQxc8vbYxZLT2bWvO7Ns8e301VlMuhRLtW-1msp1znn-noZ88vosOjDKzf2TsU-iN_U9A0IxHee2GUq-ElFGAuX_YUsuk2f6QOkdt1kPnrHemmx_fIU_d-9KxFUbKSPhYpZ8uGzazavuIvE0c11ZDP5l-X9MMraEnf5peTqACzpmMsyHSWrBBQ2rLxJU4P1ViQDjW9DC30OoRinYLn0IzFNbE6hiw_afShKA1osGWikvYVccU1NpoUf1l46fA1B2B7_e4lEEuH2sNJv-6U5geby1SBK2NgtarMFjanfYDajm7jvdosAdQYthSlA3xWTI09uElW1qBu8vqdzpBbYjI1xitsKBz5B5lVEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌خاطره‌انگیز و دیدنی از عملکرد گرت بیل در تقابل با بارسا در فینال کوپا دل‌ری فصل 2014
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29575" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29574">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
گئورگی گولسیانی مدافع میانی سابق پرسپولیس و سپاهان درسن 35 سالگی از دنیای فوتبال خدافظی کرد. او بزودی در لیگ برتر مربیگری میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/29574" target="_blank">📅 01:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29573">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1VOiknQEA0iflHCQruMkJjU7kwtvusuYSZwmMDCrGs3t8DwQ9rgoAUFHzwZ7P-AIG-XrkNrYO5KglMWPQpNGxdJMaiQKd8fyehy19IlFvCruyP23I4wcd9Wy18NdtP4PSlKABhgN5lUUGPKQg_-avtJ72lKn4PCBiimZ-2wDFiQorldF7GOBGRcQDEemh8tYJa9u7SLYja0rt141VtPUBx1O0Y6Ar3twKGilItFo84b_dLnlLPGU9rAqxB44W3RSTkaUbpEcSZznjZwEUZ9-QD-8gbL6zVEVTz2sOfXDJ_Y1kzf1pqCKRlY0DtA_KQXzoK_f2xTEIONAZ607OmLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/29573" target="_blank">📅 01:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5wwWzT_-ZnIOzluCdAMHWHHjt2GveAnyP8Gmlhl9KtuqvvLggYk2VjDzwGWO0j0B199AcD7zqXINie1XR7Plj7e8lpAy8OAfrBwqFFrR86XvPu56Aq2WUURt01PpV-PFQ61TDdH-hEokKuXSdIMjthPEL_iLfv2t84gEpwVSaFxdwUHE6UKMXGYeyt8MAocc2THq9D8tnF1zE5hpQfsIIqgEaxDn2ozhIlIZYabl_z4NFoh8fnE2WVY_0bNOxklzeFgMDGoKb0HWw0mGHGgfEsgCcKgkZ2IacAa7rPVw92ynf8N1f3E4Z9FiBJJpdrNSoMWYP7Jx4lcnr6W4v-ZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین گلزنان ایرانی در تمامی مسابقات در سال 2026؛ سعید عزت‌اللهی با دوازده گل زده در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29571" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29570">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJlLXXDdgsYXq3WLDOBDqJmmRMjblQjcLF8tgIsm-W3bw7cshcNLI8xHc_aA323VLWN7j1dzAnE49GBmBTV-4cCJk53RxWiiOCXSkclv2TKxaVjp0c1ZijRZ5Xhg1Ks93-bBncRKwZ6v95afAIiwzbQ5dnzdmszGIZqHbwW3h3X7pdyIRAVncFCL0648vBQmgij0PABwyWDV8hZeSCCAMT0YVUqimmJentIUYExu639TPNOXKSoCkupE1sBUB8uIIhkgd3dj1vWn1sEUPrNgvZcOCgVhOTC1JwfLS9R25lgSgAPHW_EPptqGzCPYnk8PifeM1Q088gyIU80kyJDW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری زاده و نکونام سرمربیان استقلال و تراکتور به شدت علاقمند به جذب شهاب زاهدی در نیم فصل هستند و حتی صحبت‌هایی باخودِ این بازیکن داشته اند و به احتمال زیاد زاهدی در نیم فصل به لیگ برتر بازخواهد گشت و راهی یکی از…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29570" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29568">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5UdUGFHq1NlZ5I8iiFZufH3CngdNoy4usS1pRs8Vj9WCb3xOqGUe5h-OgLyM_KAsu9e6Gci9qJMHXXCqyFgei3ygpWk6R8xDkDnmkn1cyvNAJSUaCBOAgC_Y3F7zJbMnaX3rU4FE6CW0-Avdw-EX2Jkp7aiei-0QawfEusGLxsQYJNztyKH0FiWnQqGxWMAL-EmGcj2f0pgfD2izXOhddA35sP28_fEhRgFCKcfm-yMg3hNoL2JYUbRhanAYCt7JFI0HjA53S23J7jYc9bPeByyIx4sh4lN9tK8wr1SGMAyqCSGINuEyxcWbmdFjHCQByAZo3V_pD9QuvS8SRbv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ فرانکو ماستانتونو وینگر آرژانتینی ۱۸ ساله رئال مادرید، با قراردادی قرضی بدون بند خرید دائمی به تیم فوتبال فیورنتینا ایتالیا پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/persiana_Soccer/29568" target="_blank">📅 00:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29567">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFauMRYdqDDLKZ5ahs6zfxg11sni3OjyNRd5nrGOPHhl9YiVsFOTQXMafANUTLEYf-X2kkYbNDISKskGkXZLixMScsytN3FX6zjPquQfsKvYLND_rs0Ggap0MeNchbqGz_EBynaGrCTjzxmK2qRLMT6kjbSgZPcfgG8cyacNfKP1bSgOBJE7WMqZ3iN_Xm25U1dI8bX60sho1R4AtxGvhwojCbMdF_3qZb3hh6mnTYyTXOgP67-caI2D5ZP2kngmlRb2Ti2PKbyAEPOsw1vqq9k6TBGbEQu559KpJf32ccp-e1yEiiW-8kSR1hAFkw6YtkykL3iYwiJH3W7XtGP4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/persiana_Soccer/29567" target="_blank">📅 00:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29566">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=vIf-4jUKP5L77flBDCN1g-cfDWnbmJQKMvu2JpgDYnX5BCUOHhvA1zHxtgEftbm-_ilSMzyiKGlrguG_U1x6BvdN_H9BDOWaR8gsXZukFw_3p0gjyL40L7jpvB3eJBHgABWrh0cFtJYgycJjsy2T4NjcPq44PciRZN1Oe7CMVJs5sX_3whqzqLpyjo-8aEIuzluPASu7ED86I4L2IZI0kUC6RedNHjs2jWb-93wrTxeuhdRupOVPefB4MZ4T64UmOt-1fpvZh-wB9UcJXkSRCasnwV74pnM1p9-3NOB3zguBAWFC6N48IAfNsflCO_LICU4N4JqcRHJJutXpIetsSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=vIf-4jUKP5L77flBDCN1g-cfDWnbmJQKMvu2JpgDYnX5BCUOHhvA1zHxtgEftbm-_ilSMzyiKGlrguG_U1x6BvdN_H9BDOWaR8gsXZukFw_3p0gjyL40L7jpvB3eJBHgABWrh0cFtJYgycJjsy2T4NjcPq44PciRZN1Oe7CMVJs5sX_3whqzqLpyjo-8aEIuzluPASu7ED86I4L2IZI0kUC6RedNHjs2jWb-93wrTxeuhdRupOVPefB4MZ4T64UmOt-1fpvZh-wB9UcJXkSRCasnwV74pnM1p9-3NOB3zguBAWFC6N48IAfNsflCO_LICU4N4JqcRHJJutXpIetsSoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌مهران‌مدیری‌به‌گرفتن وام‌های‌کلان در قسمت دوم جدید سریال جدیدش بنام «مرد سه‌هزارچهره»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/persiana_Soccer/29566" target="_blank">📅 00:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29565">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiNT8Cr1K9GVlWsfOhOLrs2vXSGcgb8FNjYPZEjbQD8AQveFuQiFNMDyxDLNP653p0780iB7hFuxOLAjZtmL1SNdxmppEnX1UhDyW5dWFRDNVpUGmymjfBgezyiN93N8Z7xQsn1e3ozscYMILeNHcCOQdPjJ-XfJ5B8kQ0Obpwzh_dt5sRGsQOizplG7CwpCWWIo4MFvPLMs-3rIKDHsMPeSnigiO7xePFVLnmT2Z4KgCM8qWYSsytdyu--tRvSDJXtNHZ4y1K12VRkXv5mKkABOCYpJDvnBIsI853zCYqupURVbmNmofeWvpEUvdaASmQHeXjjL4ZB9TuKnecU8AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/29565" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29564">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTKAGfJGw9WV4JOeiXnsfiweyeTvWgeO8AZ0FMURiABDrqigw_utstaEPqN2UjefvqZXS_Pf1rwGGyugQZR70VPjXE7YpiI7nLTsA-c1RUKUolitO4vyss9eDaAyLf6zxPM-9l4j1SraMhXWCgIMiVPruN0iMXek6iy6NetoXlsYycO0mkOqQebJcsXBoGvSjuWt3VZPSzyymZ94GmcmqAVoQdbEpWC4dODQbEo5htrz2oQSGq8fYyj0vx3eY4ZqIQvGw6VL_ZmNTFswMApDi6LOAhdPvm7gX-GIpIE17WDBXgaVJXfzCYYTwUWBKalsl0nP0RfG5Pn8kniVADGcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شکست شاگردان مورایس برابرالوحده‌وبرد اتحادکلبا با پاس‌گل سامان قدوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29564" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29563">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_QWutbpepxJyLbnOUchn24IbFeQlAIZlcjOYTS2eXTziS1b0km0CM68xOcr4eBzqPUUP3-Om7od_O07JmkQUQe_QZlEtNtmEZZVgyh1Ocj_vNDe-iVd38zTR8Xu2ZXH-i3VL7TvH0gS_72ZrxAeQDvUqrHjFSYmIJ9SKbCEj1EJ4g7ygFqn5RwIFUtp4EdEFutpJe0XnmMtgQ0nsbWw5ebeZjOrLaM5hixqGmtZmxe330w30DuHAekKrRVJUPFttriD0qqlyCRckbOZdnWidUZ88MB8n_TsrNS7rP01mLoQW8-_q5uI-cMNRJJ82FYZDP3zYE3ABTLqG8NVChIQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29563" target="_blank">📅 23:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29562">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr01sIpz4-WpdGr14Xklz25R-h8Ztv29kHBotvDEIduywbtPYHPqS7K-oWwOkDlGLr3YvPzmxqWRYVAAlXPHpIhsgkP52MYNlwhbYF4Dsmz-gcsdebnA_LBRukNY_VU3iDr0D_kM2A66aEEvgxYL0G55Kzp2bT6LCi4o3d1pSeak4g51g182Prk3mjGtnQ_ys8MFi4A2Y3Hg8xBLkA2iC0BRQRNLcENCvMAU19i3h4E_dXSVxDdQ8Gx38uVKKU2Pqzfhx8FEw-4ckO11Wtwx-3in2nenirmja9XaaoaL7bIsts5Pujt5Z2Kzv7xgVazgcTFvKtFYVjlzc2ruX5y1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رقم دقیق قراردادی که نظری جویباری و محمود رضا بابایی با فابیو کاریله امضا کردند 1.2 میلیون دلار بود که بعدش یکطرفه فسخ کردند. حالا 40 روز فرصت دارند که با این سرمربی برزیلی برای پرداخت یه مبلغی توافق‌کنند درغیراینصورت کاریله به‌فیفا شکایت میکنه...…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29562" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29561">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhFsVU6m5PbK6fAR-1TpYtLDA0O6faZKyxya6M36rPJjxlO_p1D0ZzCNQCMRoWMZyMOEm9njrAPITdhDPXvDSSBN-EEY-w7egHw44c2uBpFcBOvgfZO03xEoP6aDGq_uvEDBXauQ2Pl1MZaPqxmMEfDmt5gOj72TDTO00TumivWU9XtLilqEnYrzPo7K1qNCk0u7KYJYQNbzDrarfIRFixVnAN6-lLAWAjB0qN_6X3qxl7s-eowVhRFpukN89En87xu3MZX2aBEr5UhB6pZFo-w6srfLlS9lOFEhra8lUEYXbvIwuDtwXPetXD5vKfCIxqcr2NWSiGp3tyOl6F5Bnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29561" target="_blank">📅 23:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29560">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNslKD5psAmSz1BV-5X-zx3x3G8QtIg3wQ1BEZWYL-QguMFAVjLw0j4JTYmG8Mpd_5j4AZym70cbFhucpgFvUuzLYGzDy-dFVBe-0MbKC87LrmYkcy2pybehVXwIjCoPrBZ71_DBu7HBDWODLVhhu06vswJ5XPuwE--NzCLmykU-x5auMT3slqruLOnkiSINW4tnAQDPKgqsZrvCz_F5fMxP7cnYsm1WE1N6GJhdRBCD8I-CFYjGD9FcESrJtTCwflmu0BdHdPxsLkmkVa3GGohm1cNaLVnGm2FGPVjE1GZksYCow6XnJPglgxSN0kZM_oeJN6F4GJ91mAWEWm5oIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29560" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29559">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZtLxwkyA8L1Q7eWpzaFRCV1fqsOyakyZZg6F3eqHBgiGFn7P2FRJstjevhuHJ55m8UzjIkJ2SVq_sgWk4yeDbGUou5B0nOqWmlqC_a7DE3E3o698coEz7lS5-iHJMBpXjj92aaj9VhJ_nQTj9o2se5xjQgxUhycS8JW4PUJL9JyTHoVMCtnAT-U7FEFnAB442P0Ila1NO28KnL4AMAWyNejYpNFPZogGNei3LSOh2aqP_Cu7HInhl_jmLkg-n3At3Ac3St1rX0c6RZRrYaEKtZSQ5TJbJInZx_zoYJL3sbKfSQvhIg88lZEoJ4ako3NuW90ruyyR2Ze20J6nGLWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29559" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29558">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=G3L1BN1kSd17g0Vas2aQjrQQ7TS8w6GfJKUOnpH-uQcARPri8YtIXO1OSJvuR1cM6bvytidH4qibrjtEao8BJ8cyW2egqTu2T5_2ZWqq01lYgNC50l04wZ5Q_tgdmu6eqiGgtSMXdjsm0RzBXb0HqvFO8vQ3MFE4PUdKcAFN_TVmOh76Kby_T3faZOWcKp3kWGd1FC3eRdXSBMAHmxH8lxwIYe51EZXhazVuLMaEx8_WiidE25gJvET0A4c1DYCC26kcCsfUn4LE7jfOM8pKs_xbKXNezLdvGw89iWKQ00gx0wrpvk3kRXpmUQ91M0tGN3TLzY1NESZK14HnLag6kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=G3L1BN1kSd17g0Vas2aQjrQQ7TS8w6GfJKUOnpH-uQcARPri8YtIXO1OSJvuR1cM6bvytidH4qibrjtEao8BJ8cyW2egqTu2T5_2ZWqq01lYgNC50l04wZ5Q_tgdmu6eqiGgtSMXdjsm0RzBXb0HqvFO8vQ3MFE4PUdKcAFN_TVmOh76Kby_T3faZOWcKp3kWGd1FC3eRdXSBMAHmxH8lxwIYe51EZXhazVuLMaEx8_WiidE25gJvET0A4c1DYCC26kcCsfUn4LE7jfOM8pKs_xbKXNezLdvGw89iWKQ00gx0wrpvk3kRXpmUQ91M0tGN3TLzY1NESZK14HnLag6kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های‌انگیزشی‌رونالدو دررختکن النصر دربازی این هفته این تیم؛ نمایش یک کاپیتان واقعی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29558" target="_blank">📅 22:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29557">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMBP5IS5B-53duFQFYTCZfVhwvU1l4-nbaQd8VhrkwxxxBCR-zFcgzAnmVTceF-I2iOpv641LCHR17c4OmIT_1ZkVn-xMQtnfbvhm9ydrXtHRoW90JC-AdTrodrMBcCj-Qtxa3fTESnUZa9O7XDx7kWKde-y4qdRmCWi6gWIjquRCOl8oUXjswUfbfoWiQ-B-BLOosw8slwG-Fh2m-du6hsguv-6b2VvNk7BfzPNyLyZdz-g9Ykiepg6WuZQR5A2zUbgCDVdwK79kv6vnWHnDWETIGVmVAydQKq1QYexB2YJcB7_YVQQtf_D7U3po3mQj2uqB5TqfDN3cGyhAaHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29557" target="_blank">📅 22:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29556">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOibS_dwLo0JPUYaNsaJcq8_dBhVsUr8rbE9bTdZ3PlE0kPkrHMSpSa9rM7w9CflBGgjYVfsMDM9W4aXDpu-Kxp6yYgAncBi2cBc62PWA2PdkBjnsbkLfdklCQzxIpkQuWTeBUEEZ8w0NOYM2L9LNdNCVi0AHGMt058DlZss3jUaQ_wbDtnpnsq7B2yjGYT7PhdJ8FsUBaZJSPCPPpfis7jCw9dBOxSHN5zdT_EvE7ZbaUSR-GkbCjoX5Lt8nu8RPRV_y-fF5s1KYNib8oVO_BPMF59IRMp0e-nRZdPp5d2D1IcJn19Bq1wOCGgBQkqzfV5hXhuIPLoZV5anywUErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/29556" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29555">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpW9omjGKI-mFKZZM4EBkf8SbiFIseP6h1Bg5pcpu_CHQ352FaSy4CaxMuE0SYTzkwqo8AkObmteTIUcF5_RfMrl9-Yqe_ss8iNPIEQtU4qokVotLwrYc7iNH7PqkxwPMnU4JyNi7ZgQg0J-McOO-C0AvY1w4mQbus8uc7MikIUxVVa8l-Lc6bpZ_5orGBGnlIJTup1y4_Tsxn04VJZEF7HiEAUmC80u_91zm30XgLb7NZGihFT1jdkeJGrzEQk9Ca391FEtLfBx-weeqnQgzmeIHVJ_C6IVHs-0ua8beLq4VkilyLpfgmD45hwVnSvOLUft4A8vRAI_McrV-D3azw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/29555" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29554">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=c1Ug8p8h849xvTknusIF2GG8VJKK1_O15BWjQm-UgXhrUqx0DG73xJCZcElnRzEuGu2195T9T-_qXIMH5xsWr8l10UJCndNHjs0rqzv66aUdQGAJ8MvuZH6GDEQ1k6aQXHomJEHVzxfw-QiTwEkakc74kE0ipi0iu5lLetJ0WHcFb-g8Gcp8pbdnorlVztm3Ra_wZlB3LJeqI1rrsowL4NjGr0139Yp6r_qxY1LLjwfU8zxaG1gVLHbOdQWWVgLJFdK8gxTMewaNu4iYdR_41d-ZHJOlEq2CcA_h4ZaDxzNuTTYUAtssnkKdUCD6-SPIz7UJmrBGbFkEoYSq0lVF4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت‌مجدد مورینیو از وینی با یک ضرب المثل جالب: "تو فقط به درخت‌هایی سنگ پرت می‌کنی که میوه دارن. به درختی که هیچی بهت نمیده که سنگ نمیزنی. به درختی سنگ میزنی که پر از میوه‌ست."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29554" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=bzPkAtp3l9pI1H-KIj2lYC7eT2RDHiP81naKPwcBVUzfirryssEHmL1xcZSMBQ8l_4xB6XCByLtzUaxh_lzdaajePueiJZx_qHcYopCLtJKkcao7FOVJS51b1kLOAKq3b0jeaS8BTuIMm8QwlTQ4lqa15_8FD8Vk90mkptAPNnyXbyqPDPOzMrqj8QaD_513Ethpzl1xspOhaU26IpiZBgElWMzJuD2VRLhDYZz65Fybz2KMZyOoOzJyCucX0zJ9Q7bDYTbI3ILfOGP08l2RMWJHV99dUh-f9kYGl271cKKt9wTcSew0MbubTrwcgH-sd8LdvFwV9xvCqgoZVT1YWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=bzPkAtp3l9pI1H-KIj2lYC7eT2RDHiP81naKPwcBVUzfirryssEHmL1xcZSMBQ8l_4xB6XCByLtzUaxh_lzdaajePueiJZx_qHcYopCLtJKkcao7FOVJS51b1kLOAKq3b0jeaS8BTuIMm8QwlTQ4lqa15_8FD8Vk90mkptAPNnyXbyqPDPOzMrqj8QaD_513Ethpzl1xspOhaU26IpiZBgElWMzJuD2VRLhDYZz65Fybz2KMZyOoOzJyCucX0zJ9Q7bDYTbI3ILfOGP08l2RMWJHV99dUh-f9kYGl271cKKt9wTcSew0MbubTrwcgH-sd8LdvFwV9xvCqgoZVT1YWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29553" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29551">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6TJuf-Cx4kNW-_aVimvbMA9BqRii8a0HfnllPlqzA_achQpDPNTNyanW8Wf13dSKwGzSXUROL7T2uY0-OT8fwOqQvhwkB_Y8_0nZDty5Rmz8iY3FPQxYG6GkXuBXxBvLQ7GsVZYg19xcct1GBQZM7yXm9N78vNr2f0rWAulilDa2lQ-t9XKecE6Vm1YUgDTDD8izaipLJgJxzvDtX2EdzrrvDFH5nk5-gSP-eVaDBeCUWyJMMBqHPNMRd2wGE7oY_wuuEpAOLXpvgjq4Gup-qWVx9ggNDJVU2owibF4oXB6kef3mPJ3BjUTM833B0G4CXen-wWuXaaddg4R8Vu_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روشنک‌مسئول‌مسابقات‌لیگ‌برتر:
بعد از فیفادی و بازگشت تیم امید به ایران بین هفته هشتم و نهم بازی‌های معوقه هفته هفتم را برگزار خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29551" target="_blank">📅 20:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29550">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
کارشناسی داوری دیدار استقلال و پیکان و دیدار تراکتور و استقلال خوزستان با مارک کلاتنبرگ: بنظرم باید برای پیکان پنالتی اعلام میشد. هر دو گل تراکتور به درستی افساید گرفته شد و گل‌آبی‌ها هم سالم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29550" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29549">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4FXCy8Gfmqog2QaW3IKRzHRaGtWpkwMShyxDwLxUH6S1733BSjCSez4dohYW_ftAHPyHnHF-F0XAfq55Ufs94mLb4ZBNFOpCH_HXdy7UDjyuHpMYA8ha_R0L3stO-FOw5DV028_pR4XPpkmwV_ObW96sktefceh9M0dQA6c7GKIyzXzqW5VJpdmQSeedxb4Eo3RyuTCnlnzHiG2cQ6oARLP0Sb_kmjFtrpt5TXa1FdTMTyG4M8ECGngk-awZcLZopzwWLd7lnXv2E-rRIlpPdKWwyGiC9QUGuwRgYu2_a_BnFuTeTF48ZsJWMtoU2516Hg_pjC_sENb46zT-pRalg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نشریه‌فوربس‌گفته کریس رونالدو هر پستی که تو اینستاگرام میزاره3.3میلیون‌یورو که با پول خودمون میشه حدود  910 میلیارد تومان پول میگیره. در بین تمام کابران و سلبریتی‌ها اون بیشترین درآمد رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29549" target="_blank">📅 20:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29548">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSq3a5bEOrORfiNig4uWnvsazIPxg-o7OEpdHyi0zeXwQ9giqYrYVM0qQIwMF4LPOv-UE3wlcakjDwraYDELrTs8TWJfTudONzm8kDmM_3bCb57_MnG4zirDfsBdF7ccqiSbE-rm5clyMjGB6VzV28-5dJJJ6En3_QTUV4lDza0FCca_lTAFT3Ho-7SwjLnLj94BlP3CrSx0WfHGcU3TRcvhJGmbZ51jpP9fr35Z-ahvJQP4C4FmznNfmBlMXCg-z3WQw1pIwOPFP3FrnrVDb84yyiXoqlMmaWOTv3t4MYrJJSJbA8gMsiC8F2UMIkrOtsDoCZTogKuKvrCDwIzwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
#فوری؛ فابیو کاریله سرمربی برزیلی به فیفا نامه زده و اعلام کرده من پیش نویس قراردادی باشگاه استقلال رو امضا کرده‌ام و درخواست غرامت میلیون دلاری کرده! گویا پرونده استراماچونی دو به وسیله جویباری و محمود بابایی راه افتاده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29548" target="_blank">📅 20:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29547">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm8Q9W27Xht70PdGOEqMmlNCQ-W8kr47EWJ3q54EvLqvvI5mjuHaDEBV7-q0uw6Na3stnrmYlGECpRXg9Kz-jZqQaRZp_NauUPVHCtNHaEL3KDbQz6LYnjM0YrcCbUd4fAnM7KMTx716VDa35flln4bhytxYNfDFhp3JMTm8T31a_wvz_FxF-e0k83xn1I3_laMDd8_EBb0hP3_ue5A86dhBBzP4TWW_79KyCYLxgCAREwBmtTeYZ4P8zkZgFh05vUG9gPTpUOubMCu_Tlu89WgTwsgTCMi7aKxnspSuzQGjtWvFahlA_MxyZkIlwxVgJ4zfZuS6hCO8Xfa2TJf2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق‌ستاره 29 ساله بارسلونا با به ثمر رساندن شش گل و یک پاس گل در چهار مسابقه بعنوان بهترین‌ بازیکن‌ماه رقابتای لالیگا اننخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29547" target="_blank">📅 19:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29546">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdrZGVdJ7QvmFXdRoWyHIwzSSZhtuCDCpCNPso1L5fau9rGT7-BYkVBXMiCjRGhoC7G_5oAxsFTS2BKTEl3F3ni4sPpy4E_6mBjskv1MpUmq9AalitiMyqBbcP9g5YqPAapMJzK38WFZkr4uNVsH4BfgPaFtNee6yHPNyjG2HiJO1q0fy52ZmEXv2gHKvSYnvpDHBQMY8sq1KmoxfOqjWXUpRuYETj2Z5_hcDO6rG6Cq0ly5eiCnzCiIHLi_L3yJSqc6OQXsQ02QbekvRfMjeVSgfK6Uy1HpY3Ngl8sY8x5gUuvng2Ay_paTYRPt00E0uSmZyIZMiLUN82hgGcG4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
‼️
علی نظری جویباری مدیرعامل باشگاه استقلال: هیچ خطری باشگاه استقلال رو در پرونده کاریله تهدید نمیکنه، قراردادی که برای فابیو کاریله فرستادیم امضا نداشت و فقط سربرگ باشگاه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29546" target="_blank">📅 19:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29545">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgC3n5Zpd5g-4zbhx4KXC3TNOzLAyyjFe6p1Wn4BTStfFkgAGIIH3MIsruoPI6-6lZmgbt3iIk0yWktYWMv8Irmk5n1Iwp_w2WNJ9ebj2Sps9kr8hUU5gAk7ayNdfKSKZXwZTLEVo0hb5m6lTvJV22epEKi5qchQMQToqZWU7OVdOAFYoVMCYS094Vn4k8naugC1EZ_LLfQeNzn9e6w1ObZfD5GWPSjC3kR-jH8wzgzvklTL1dpJSH4OOaGzZx_PiWCmB51lvNSuEv0ZLiJCC8ONkWfw911B5Lj8iK_HOMmrAQ1ufrJ1aKl9rQwJRkfV27NhdtkG8BsmGjWdUN17ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
گئورگی گولسیانی مدافع گرجستانی سپاهان بزودی قرار دادش رو با طلایی‌پوشان فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29545" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29544">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1XQJr_g2ur8cZXbleG2PwodXCeXNIBW14eqNgBjLHnKUQ230CRW0sSnPH7SeFCmljrZQhyWhsxUi95xniRqhi1Az2kIBBOHwScyPrhZPp0mcuSdyW76tOYnEkRX079PfhwDPLB0jUWOAndiEgaQS78f0aGeiO8ceIWi8Y1AnRvayqX2SVDwvFyOdoS5CW1Amq6Jb1vl6E57_uk49--MT2ImFaf6ju3ucrYgdyPshLSD4qXuIeSWsdCa1GaXFryPcuN0PZnu2JYveVsz59Z2LX5sG4qJPBikkRH1GZFw1kiP8AiH5hm20nUu1H3-yx4sdb7dDBTn2A9pmLnwJx50JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN:سسک‌فابرگاس و میکل آرتتا دو گزینه‌نهایی‌فلورنتینو پرز برای‌فصل آینده رئال مادرید درصورت عدم قهرمانی در این فصل با مورینیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29544" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxcjMdHCybd0JMMB_CocShk0M20zcfGqNdOnvCrAPADNjQxO2aGEUZMtXHmXVP_LwA9Nqhl1b-aGSNXP8EpwjegfGVp5UuiVKbh_lPu7cL31V3BFAdKQxAeFeMBUkET3D4gnrYiCqr5xndiLi-zcsHInN8wEOAKUjoJ7pVEttEKXCkUeDVyqhqJC26CsxNWMZJdL4S31l131ssztlWdSD5q5ByJ_L-CUnRR8bj0_okYFlu4ipSasjd3EaMivuuOJgCIqcIq1BzMZI-bNKEZviOaydesJSvarRSo5PafJoFRsK-sNNAI_k-dY6UnZSQ6ra0rkZMJ-SZvL-3jzy1qkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت برگ ریزون؛ تیم فوتبال بایرن مونیخ  12 سال و 9 ماه‌ست که در مرحله گروهی دور رفت لیگ قهرمانان اروپا در خانه شکست نخورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29542" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ3reGvjkC6WMfh9f02cxKLPlQjmTn9sn3SAk2SKnqTXsVXDABYduF2aYtKF_396G9hLt9n7g7RChdv2f8TQzpyDOVVkEuDGSovh0PPK0eYQe6LFFbJ6azsm3-nJnw5NlDBcsMvournG-tVknakgUI7_LeAgawNwALDZf1a34Xxkt0i9vfO3ZOu7lyZCRYQZni6oMKD0vueEO8mPvsGYMK6wER77xaVChODKtxjz1gfjOHjV2ZntFFZi0EPziCNIdJsCROYurmOOVpTigwCxuDwC0P1tCB3uWJwB9aq68JHidcQV8MSCOqpRQt-lojTWV-d-FGRezadM21pOIqzeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#فکت؛ ازشروع‌فصل‌گذشته رقابت های لیگ قهرمانان اروپا تاکنون‌آرسنالِ‌مدل‌میکل آرتتا در وقت معمول "۹۰ دقیقه" متحمل شکست نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29541" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBNKSc6Hd6ZylpIbk4LDvAoiEC7psCAPk5Wl5jGRLDry1yLNcO0ImNTh9iHsQfOBkd1JHHRawC8uGhSgO3MXLaNnTjjzf1LZVbCZy_ZL8MMd5194lq41y7ROOlJ9f9H5xAL2MI9ckHQoFg1zgVbgkG9wlXNsxjizdHzffBVLUFWXcU0w4Xmgcyv596GbDzlqCfSl3vQaRGhLQJBGt4t6QK05Hq4zJrI2jVvYeeNdkpt8KquZxtoujWnSVeii3BLzEuKOjK-I7QArbYHONGK8rxyLFBKNF3gXcQVemLMOwCXizk6Aw2XDF5RSJKO2QkXHaPwopcE7-qHM48dzFY2qZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛
فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29540" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=eoGePuosD0eA0c_y8Z_5VmuMJu3iyatWe4dalTiGp_eRDlon-hyhS5cTR26Zc85sAm1cAIqOiiRWebEHbmPRahW5dGYWUEDFBIE9Gt1PblrNSqEm-YTlUu_p2ehAl1yzFlN_d17wXsuh-Yh_OKl4giNMhaHKjTpqxdDHH8wilhNVKSZfpw0ecOOzO8z7x6WVM0MwBiiuOZktYgXaFFi3sdiwMgJ5ZZfYGRuciMeUmjrS2FdMFxK5N5cf9PHKv_ablOffmKOuLtxXwID4e5aAFAGZNEKstNWoJyJ8yNdRj8XK9vjU50y_7JdPhTYJDCwfS6DeCeFJx2FJhtiEglO5tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=eoGePuosD0eA0c_y8Z_5VmuMJu3iyatWe4dalTiGp_eRDlon-hyhS5cTR26Zc85sAm1cAIqOiiRWebEHbmPRahW5dGYWUEDFBIE9Gt1PblrNSqEm-YTlUu_p2ehAl1yzFlN_d17wXsuh-Yh_OKl4giNMhaHKjTpqxdDHH8wilhNVKSZfpw0ecOOzO8z7x6WVM0MwBiiuOZktYgXaFFi3sdiwMgJ5ZZfYGRuciMeUmjrS2FdMFxK5N5cf9PHKv_ablOffmKOuLtxXwID4e5aAFAGZNEKstNWoJyJ8yNdRj8XK9vjU50y_7JdPhTYJDCwfS6DeCeFJx2FJhtiEglO5tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29539" target="_blank">📅 17:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjEABch0RjKBY1fOznFH6zj9OgtAPFj3UHdJUzHUmXcAAzcTzilF9J5ZAxrGL1wvXtixqjOyJai3H9tZ2f9VOlMXaDxwQB1nHyjH33aswVBP6iySPuUpkj_ubZAkMnUE3LCcCWCioSGSWrxKt91f0DRhKgrkGuiL9YGNGIeWtuzADOFEHdHxKSfHS-C8cvJBLASlT4F8KtkMYJmVDgwwyA6G--5P-Dx3WAzXrvWa_g3waRN7AQ-yTfugJDArZ4LwaOw4yUDKkuDblDssEVOe531var_mhg2jkVq5nVOUu_0uxpMusTvdfZIB0w39NYf_F8F8J02pxs6pDof3YHmpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌مهره‌های‌هجومی‌استقلال
🆚
پرسپولیس؛ تیم مهدی تارتار تاپایان هفته‌ششم لیگ‌برتر با دوازده گل هجومی‌ترین تیم لیگ بوده اما استقلال سهراب بختیاری‌ زاده هم عناصر هجومی خوبی دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29538" target="_blank">📅 17:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29537">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=uT93tjMu1kxCJuUo66gUvnRjPhkNRXDKC1Ow9bxVBOkLJWFfqthDAufC6SPIMQmva1oDOi628KcyE88jTd0kW_aAAvxuFeJ5eeDXpKpuiYqPff18F60PxXBG0wbt8P9Gm9KMQEBk5v_jykNz14joDnXZuo4CshY4SCmL_8_n0NAQxVPP9kIntennDUt-rYxRFpKrqTl9qsyvvbquoluvHkYUpxl-1z0FM99VZCKY1Zdg1aGmiERDQRtit-oEZOxCbZ30t5pnTl4RaI0tTleN8rDYmXPmJxz6aTBRJQOomARoiWW2KSZq9hpRjXD1wDjCyUK7BDBgUDjFv7Qdg1TSjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=uT93tjMu1kxCJuUo66gUvnRjPhkNRXDKC1Ow9bxVBOkLJWFfqthDAufC6SPIMQmva1oDOi628KcyE88jTd0kW_aAAvxuFeJ5eeDXpKpuiYqPff18F60PxXBG0wbt8P9Gm9KMQEBk5v_jykNz14joDnXZuo4CshY4SCmL_8_n0NAQxVPP9kIntennDUt-rYxRFpKrqTl9qsyvvbquoluvHkYUpxl-1z0FM99VZCKY1Zdg1aGmiERDQRtit-oEZOxCbZ30t5pnTl4RaI0tTleN8rDYmXPmJxz6aTBRJQOomARoiWW2KSZq9hpRjXD1wDjCyUK7BDBgUDjFv7Qdg1TSjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی دوباره شهاب زاهدی در بازی امروز جوهر داراتعظیم دررقابت‌های‌لیگ‌برتر مالزی؛ این نهمین گل زاهدی در تمام مسابقات برای این تیم مالزیایی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29537" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDX6A9kT1ZTYsNlFH4sLWUYDI04tUnrHq6-2Fy7uOyb3n-S2q4y7csSWqt8s735Sa1N00iJzmLPQyYWXwydDwbESvMIT6puTzRZPsSx9giwuBWByOMbFJeRozByO6vVnUAyA3w-0rvfIhUopU8UQx61KsdI2lY1dH0pfG3VITI80X0VyvSt8Yc-Dr5nFGMXF2iC-CEBE2-sGM31e84Uiin8jyBjd_8ofBECxmMxSXwPZsrjgS9-8mfh5Qy-FKfdukeyLadQvEHP4lS2AxpkaYqd3arL4fq-mvUxt8f9IsXYBjGzu3vhEF-th7FgGk0QzLCe-4goZDug6U9ILb1zlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29536" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_LmlrKaboNDnEvld0ZYOU39YYzUsxuzCWMXSCcKYeCqV9V5MRgGdTs4tou8RveKFMRuY72QXaj96lLX9ZHC7vUt7x03E9qT-V9qyXPZQHhNAxoAk7UCbALoWme7ycq3Bh3qvM-Ytn5W3AhHWpATwEBVx3KNW-2o0AOpLMCJ2F4FCPeTmiC-QBSk2uIhHAKKyBiXPNT8REMd4dgSJ5fSpG6RE1ycV3B0at53j-C8HtIGEan-n4ZzhYIZ_kuIpLRei2tDlII5k8CuOFH8j4aRR-1jYnYkFY_ickUCbzFJHQBdln8K2JiQDix18XfR-5pJmiWD0mwOpxSznysC7C4BkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کار انسان دوستانه یاسر آسانی با خرید یک خونه برای یکی از هواداران استقلال از زبان وریا غفوری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29535" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29534">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUsaMNDsQwvl7CXx2qC9-RbFimgtO61VO4k7APKzE-dpDymgXcFZIB-NVYhIgVzJXRuxbZsPtz2F1Fe0HxyxFR1R5tzh6-dfEM22cDir-o8KZe7pkOm0GTYyzjZc9lFp0F7tPzXoiJhECUDHHIlYfu_xrKBCxaAJT8CaEluiy8OyDL9On0nqnAHRuIUMemXqQt5nkoN15Qh6XWeUCvmpDYnVhj4NIy64dIiC0wTOKJV37ea6wNTNRrhW5VKYNhtdL_NbuL2FjW28R13b796rXCvoP4rj7uhXUPs7ih6GylxBpkyCrm9qq98OSnFyMFcQlw8n-lbxTRuwAdXiybu55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به گفته کارشناسان؛ علت اینکه فوتبال محبوب ترین ورزش‌جهانه‌اینه که شبیه‌ترین ورزش به زندگیه و دیشب یکی‌ دیگه از این اتفاقات افتاد. دیکتاتورها وقتی سقوط‌میکنن که خیال میکنن دراوج قدرتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29534" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29533">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdDKRqQ-5ZyAzizX4GxBdmDQA_oBtJ_WbOLEiOXqZSuSXwQ6aIUEebPNTrJlIDZCMzeeSd2zEXDVzSJGZcvz87axekrI_nv82PttnM9uEqDG9e2b757w4u0sVwWQtiTwdYbe1FAGeeA__AFtdYG9bBk7JVEY8XBUe-vn4WhTxOh3NKZOSxlqesL4d5iKA01H7k3ve7Z-GEuZQE9cG8zKNjdHxcRkYozoEFkl4I1qzjljbQNLIGsxKTCyllvDOUJj9oG2NDWU4CUUc2cT5QynS2MAqhA_64RkLxVIwx1NRU0iujENJMx8YOd25Nasx2TJdCq_fCmdhm1LJ6kN4e1g_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#تکمیلی؛ سران باشگاه بارسلونا به این نتیجه رسیده‌اند که میکل‌آرتتا سرمربی‌آرسنال مناسبت ترین گزینه جانشینی هانسی فلیک در سال‌های آینده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29533" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29532">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk5YAZge_H9NI8nU-2dn3ZvvcY9bpGIviI7K8TtO_x_Zbp6MXyZTvHdR69y7pN7_tDDjTt0yhSI556Ijs3gP7G_rx1jxW81BEApABGtr3RzuL_VCQqqefEmtyuWKdJgZibKVpLHC2QrWVoMEtkyZmanyr76L4lT6AUQ6pJz7Y7a_XcSVV5be_i-Jxc4HYn_0H0qOtnsfS0VJVsu32AOUKTUIyXeLuFXFjks0JB4arZwQ6DDwgdc-yEy8GRog_31InsqrI-X4UcxGlkNjh-aEFJrzCRGWVNaLW5yVld0OFkEGZyxO8DwH3BMB6pwo8WrgpVQDWH9Sy0-iKMQ7DyfyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29532" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29530">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHWQHhxNv7DN101o1WZ60Fetl2ZOT0L4sicYpLUT3vsnWsUOj5G_5JoChWD5UuIgg9hXBBHhPm-WfnpsyjQazimUngoBH5uGaISV6S6GdgGriC3qn7eEcdz8odpdvyknxgPqXyuqYYAH2RgcWGawSxU1zGBeY38ENcxNCZIvFXtik_4N2FsPNWYjWuhaPDGecb1RxvFn7MutrNuVXcCh6tp2SUbt5at5w94E7Nh0bIjAeXO_FgRyOOEQ-QCgznF6Yn1i2texcouyE-BuWrQYsu1-y9DPL3ZFOMynn_135iuJU5p49mMfD0QCzS9h_6agwaRoSr1yMog7FMlM9pMNRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29530" target="_blank">📅 15:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29529">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYAb8RBfnQ23eM5q-Kc_rjyWtiEm7On_hXzzGkJetNYqsXgh1GyYTg0AI-k7MrdvUoSKQ0E8HhBu2Ao93m-1yPQ-PrNblTGDf8kujmfMD4srTVx5_zUzJ7IIUqeg59rRUbGSgmqypfX4l_MFtPT8LBg-ojZ5aZ6ttVLMMW03u5lzpQCDddnXSk_yzu9rjBW34AYKusTtAS9vWYfWam1suOqHBF9Ky6BISXuDTMKZ85DTQEVTzLo3prWvgbakNGWpavF1yxnWIIywnbn2d__hvetxuhKTcVgSECI6Fne7jQROik2wyXrrM22vO_bj0ZuuPqNhwgnVsAHFDApPLa09OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29529" target="_blank">📅 15:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeEbn78DMLPFNeLJobI1ux-BkBh5rvug2n7UOzteQl8bpEJHXLNRCVqZfYHGfGzkrSNJFsDmS9dcZ5JMeyzbU0GLroB1EB52TUw_-gj4QYkv-dLNmRCbX-tmUrWrzqjcipVIxHn8zgGxP3TDaS59CWdAMEi-_pfiEDsKq490HzpTWzSLJcvw61XcWXP-nP8fOG6xUdlLiXjqNQ0x24A-JAaZe15kCyCv2QjeRo_7Zw8HqhZtBhXDGOmE7o_C3cUHhllWx_8nlenQU0c-yrsSX8q_MYcUQ0YGrEUfYJ7vPpcMDLtYFO_WEmsCWBgHqcgbzhrAsy8u556-idPr6_aT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29528" target="_blank">📅 15:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFB8_gZknn36kdQ6kiq3t7CLcHAUwzJ4WzrNshEiVNQftTePVfPvGxCtwyuaZ9VlD79EtOFEpyJwohZ7vetgDrYczRDlzy4XYiBQGso4VITXqRzd6wZj286TEEV_seEqwOAZ5xPYn7L7R1hBdCYPX7ko1NSndsyDETsecNjrxDC3k4917JjmSNwv6A_dhkRYmU_nMTtKkFRTUg_i3KDl08L-QKoRd7Fh6Y6L4tIS8PRFDzvYXvKCLiBq0Qrvg25d3wBuwgF2Ef2w3ibzAKVDFOiJQbPnxvywLBuotp9OzuUAJBASJiS0CBIGgBX_UnjG--fxVhB02dcBjfdglmhREg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛مهدی‌تارتار سر مربی پرسپولیس به کادر مدیریتی سرخ‌ها اعلام کرده درصورتی‌که محمد عمری تمایل به لژیونر شدن داشته باشه با جذب عباس کهریزی ستاره جوان و 20 ساله آلومینیوم مشکلی با جدایی عمری نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29527" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29525">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/io3dabi-KgPZlBVB8CUIpIbdiPpi36QLtyO5UxRN9MT8q3OynzpjMyyf5HSc0XPbL8eaj0G1xfbPgqskvQ_MWi2cA1q03a2jsXW1LRJGDMXdCAe0tD5vjs77kr88sHPxkycDAT3By0_hnsPRUFEYfgT4q7Zp-aulvpNTilbAtAVpE8goC_hIQ_OyWeoWgve8PV091K3nODKc84gXdmPX4BpXIAjFCNoqUKTroQtMsY9is2gY_Pob3ESjvqbz66m--0O5OkQHEVr_GTxAYDa2Pjr-uXaxGIfv_kliDkUEkdLIKmAg9ADlaX2pNUauFM0KEmA-eYN8h3s9IwLez1ijoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات؛ یاسر آسانی ستاره آلبانیایی استقلال مشکلی برای دیدار با السد نخواهد داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29525" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29524">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRmcj3NOY843mlk1bjga7OzCh5ZCj8oyvADsYeWKmW-9obfWxLZSjpYzy0t19_yfHCyTv6B7Fo7ZYY0e1I44XbPiPDvPpaQQBaNUM1gV5elnNjiCY73ws-lqYW9-zI2ZrtXIVnpVbfbKcGRezL2yKy0NYYDdmqUsv3xZnrJ7fFaUGdpeEDvImRUBsBvXLeV-zs3maiWEIdiE_ifpuBQ_g5KR1AS28UffywOPiUjTvsjn9OtuP9U-dp0fz_JtsDgdY92yegIzDOimcuXo6wBf01fAydg48zXbe40RRqBgI3c-edQLn-CgAtPqrFpoH-oSu9ZYS8cBIN3aJ1tGK01g-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئیس‌باشگاه‌فنرباغچه:بااستعفای‌اسماعیل کارتال مخالفت‌کردیم و اجازه‌جدایی به او نمیدیم. حین بازی دیشب یکی‌ازهواداران یه‌بطری میزنه توسر کارتال که باعث ناراحتی او میشه و بعدبازی‌میگه استعفا میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29524" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMaLXnTjKhC82KNpntMtwzT0BQjib58ZWVS-Bu17Ea4oCXlJqc04dOBDMynnoYWLCWD1qumyQdIdg4ueqmMB9WrC0jzMkfDe2w9BzNJvjopHm0JZbYYoDlkhur83sRFfv8Z-4j9TxVcvDVhR4b9xtTam81vLCYvuPr_Bx3c10DbDkWXroiiCpVbV5tq6jRwC_cVegonhh2XrSk7GpepHCbw06rwk_bbYMn7Cdo4yBIVuwTJA-pdb8VvVmPcGMk6zv7bCWZVq9xuIa7eRTJh9y5CkkK28ODLM1LFevpMCz623PfT7zZCsMfHcN-ah22ULHpj32aIP8qjJDRqM-M3rJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر رسمی باشگاه اتلتیکو ناسیونال کلمبیا برای خامس رودریگزخریدجدید این‌باشگاه. قرارداد خامس یکساله و به ارزش 1.4 میلیون دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29523" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29522">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1TWp2FbM-gfhY5JBJdHnf0uXVBdb8vuJhTnPvOxG7Jeg4bQTLV8qCM5tTK1lc48quncdiA9j8630RYANpaut94OGTuxTMdpyIXSqAHvWUak7r6_UKZcIwzMX-FH2m6P-0M5CayxXHeVoT3EBo8Q6MlG3odn625GYcaXwWV1F-cund9e1DqPEWdGXKO_N6QR_Y-tbCRiO50O4iExvWU48qaoRGapk1ZYmaphcTjjBW-LJQU7HHPou7-SpmZrQXm90m1ZRH0aYwvlWSDraM4BRpyBbUBSkBp6MCq2-QMj6mKgzL1X3X1P1hE8sDpdHY3vM2SpWnpVhiiVKRFgYLriaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29522" target="_blank">📅 13:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29520">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDxMe_fGC90eQmLFzteWAODemCx-V2x2l7gOrXxumBnRKhvhRDNtgPTkCPdQx8y4Jlm6RKeoEo2U_qZS_JI9R23uukA30muxJxoy5w7RAh3oYjPLILFkeIdCo8O7pasIc36FhKLmCSd5ZD3obzzdxZhuG5L12-voSCZtBmWxaBqHoSld9NI2CW2ZruH8XQCVMOSQdlHk13UU9mz4eNvKALPXifXKtCXWNZiN3BNVSkmfiUf4N6rUfYlamKiuXbS7QUcOUBpgpOvh3sLDZJRsojYzRcBTu551QmaOR1iB7xpYCFaD4-gHSbPsxwsIWKOvpA0jyq_w49s8bBoDcneSwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2jL8Ot4wCrJnMWmzIzhQiCQc-ASTxWgYVxTdvKa24SOtW6_NChDzUcYj73gy5q6aq5ez4H0F2Kq2WljOwoCPgYVk2CGJ-3zHcDUgsyEQBOx9WCp7zgh8PEb8J0EpNLXYdfYGLiQotxomtPDBgJ3mndpJiijRjZPdCJf1TjivpFJt_WBM0PHD3vnV728MbnpqGzGBPJfrw5fZ-tbCxMo_RxvQ8oNWbf_vrpatOiuXfkpYwGvXI4GS35v_aM0VfgkBVjrZEHrKITay7ZnUDtiTsDqut4FvVrav8x3hNGLmSZEka6mJZe1ZsQQG7kx70wLWH3G5kZX6JrdU3PGHGrc4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇺
دوخبرنگار شبکه TRT SPOR که پیش بینی کرده‌اند امسال بارسا قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29520" target="_blank">📅 13:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29519">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egS3UqfLu_1maIeFh-7kJ3uZk1JRu2omi-JyTR6YvyyN7h0fLeCkHMKmuHUXO9fWluM7G_4nHSpcx01DJtB6xjGXmypWrgr_4bqCu9_KvsH25GkLIbZFRD2S1BnqbFmK4DjjXlCWQ81npYMXeSxEac9lnd2nkC7va7NeyhRgzZmrvEbeiY2CStPhhyRoyfariLNtoErKcUTRDYAcKHom9fgiRFcLpMngRsmvS7-Tmfn_WseRTm_qxv4_flmETGVMvtoZxRe56WiEA2XZuYsuUpx13I1dXg1wS7xWGhq31_vYS8GK7KakQE7Y_23HQSR8hxae1O745yBnAV6PKy9naQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
🇨🇴
خامس رودریگز کلمبیایی باعقد قراردادی یک ساله رسما به اتلتیکوناسیونال کلمبیا پیوست. دستمزد یک‌فصل خامس رودریگز 1.4 میلیون دلار امضا شده. خامس دیروز درآستانه‌حضور درسری B ایتالیا بود که دستمزد باشگاه کلمبیایی بیشتربود و پاسخ مثبت داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29519" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvOW5bpvmEkG4HNlFNBZ0Ek0PE1VfGcZngTiZjk44AWhnRsfHWDpUCde1hZFcDTi73PcZa2A65VbKZaibizWeeNTmCV0qNNfutLadS0KRMbu4v54wKmxhi2D1EDsS564HKai66ck03nksB_9b6zPN-zI5lp0pBCDH4GYoE6TDuge58hLroKV9IH_e6GLbX-7NnEsufan2tfQrrgY0cBLkuOTrt6rd6Bqtx-yWYlyCS7EmAuU1F5wlhyvZ59pnWt_EjbC5wAS2Q3q_l9PUA5Z-TfADNt9tKnM6XBMrpy7Yfs8cwRBEgtZDPDwJNYA-w4_f9gxSn37oYU3QFP4smuLJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب استقلال و پیکان از نگاه نشریه متریکا؛ یاسر آسانی بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29518" target="_blank">📅 12:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29517">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
نجات دروازه‌ برگ ریزون آنتوان گریزمان در بازی این هفته تیم اورلاندو سیتی در لیگ MLS آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29517" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29516">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhVrGKv5nrqUEaQlteqicNQ67SU55FerYFnJOBfurSfwUJscouukVIRpzPMfKojZP53t4OBnYBTYlLIDGjE1ZeQu5ulEbQPauhJWzMVoWCwOwzaakuo1RNFDTaykful6phNPvcTwoxqXlKtQ_GaOGh0L--y3zwfU4WTp1f45xp2C0TaJXzusC3-87jShZhso08iFF4RRjyOTSWvMLAsesTokvHmqTPN7WCDOIWx3mL17m5hgnjMauBxqL38cJ1bFkF32c37vKYU0GijwWqvHVnSUAt-8-p_YmJN9aD56vJauACuW0s-r9RvJLOar-6s2xTwWZuad2IBwdrQ34S5fdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29516" target="_blank">📅 12:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29515">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-Tm2jg6CO2C1_VVSuMRwZvN91oBL5oimiYonLv6Xp0E7_vQPn3E3Zx07dXgAlvUBdaac3BmyqRY9ZcOw-DhhNzyCLrgvibXhHJV8thN6GcZsRTdTY6vCpsUOIfygNX-veFHGVEJJpZxtO9QHqgziWVrkXyhzn4OB6SwmATksKBYKml3i-nXK_z_1N0hLeC6U96ndJ74B8jIbycAm5GxCH7im-n5_pcBUqGFj6tIRfX9k2NftYcOyKwI2igb6mkqj3BDLLcIHbYNhKzCBqSGjFWqHG0HvVj3JdONFXzjjdnGSvrM7XxZD2c7dCzTQO56X31700bHt_U_BRdzkoWBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
🔴
#تکمیلی؛ باشگاه خیبر خرم اباد به دلیل حضور مسعود محبی در تیم‌ امید خواستار به تعویق‌ افتادن بازی‌این‌تیم باپرسپولیس شده بود که مدیران سازمان‌لیگ با این‌درخواست موافقت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29515" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29514">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
دو گل آفساید تراکتور در بازی امشب با استقلال خوزستان که طبق گفته کارشناسان گل اول به اشتباه مردود اعلام شد و در شرایط سالم گل شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29514" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29513">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbgbX-Jkxq6WOFG8mmb2LYOy0Q15My8B0bHTkAc2GjsjLqUdG_E5e_GvqrZqoU5VhWxs725oBJFamRIowLueE318S5-7KbzLT0IaISdxrDuP0pqPsQJ6iwfvC2bBWZ9wMcugeQqXy7D5F6UZfEaQwy0e_18Q3Twl7HDG4yzBfEnlImua7KsSIPS8zvUNUwgQg4H1oLP3TyRcF_rsVf8cygYoN1XQH9_R9hbAmRY9Xlf4Ovm5Hx4CNH8K740fjvts3okS8AVrBnTVbT11MHOIAq2Wbnfqho4KqbzMxZ505AdwTN6QMHBIaYhDPhLbPLhEoiP_2miEH1T16FByEbw8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره منچسترسیتی:
یه صحنه تو بازی ما با پورتو هست که روساریو داره باسن منو می‌گیره. دیدن عکسش قراره واقعا جالب باشه.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29513" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29512">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6spz7xnKWP9d4Iodlew9lEO4OoUF3ZLeAhAV9C4SjoS1mgbPlsNj3ZMNQ0IEqrDcijjBL9ztFTqkVG_Ny7ym3SLYwupUat49Fs7aXyZQIpJjMXI0E7o9_mz3V4jG4CMquY_l8JFOlQ7qReBatf1SulOmZ8WaiKtRThS3CGRBih7HFdcH0rETsezl8L1y5pXTs4a0NaDrdAK5RGVS7K8BmnfjiuUk-wK8tVG16_30lOOR-TE-4cq3CiMm66fxOp8avUp7kBbSP0jbTc9NXvxYFDilaSkYemcDrqRPhtNLY8WNCOtl5zNSCy1x8oZ2WMxwSkIG8kYO8Y6aYSaeSyyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دی‌پائول به لواندوفسکی در حاشیه دیدار بامداد امروز میامی و شیکاگو: تو دیگه کی هستی احمق؟! من‌دوتا کوپاآمریکا و یک جام‌جهانی بردم. تو چی؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29512" target="_blank">📅 10:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29511">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZxmlIaaeMss3HXX6xhQiOwHMgpLqZzm5L7g9zD7nAz18yNzxmDdTAO6obfYpRIWPXZwKAELZS1iBvGy4Ogkc3DC8UHWBvy7d1tWNT-c7zJOMeMnUfIdt8sH-UT0Bf_tcxfSYnHS4afkbBGBSLXYiXI6fWkDx0ipNO8Qqx1Z9ByEFTTnNWZSgRkmg2Z6RwzHhaQ9I22BWx7O-uCPnsm52C5s2sr4luNoUSA2L_6mE_aBj43V0rUWm6IiuZm0Frz1r-IQ7FYJK6hPJAO5JCaJb32CAhwiK1ODF3LTx6ugk07xo8HX8T7A_rHdcD7ObK3lz2nljQz1R-Kygg7yVY1CXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس:
اگر کریستیانو رونالدو سال 2018 رئال مادرید رو ترک‌نمیکرد ما پنج بار متوالی قهرمان لیگ‌قهرمانان‌میشدیم؛ لیونل مسی قابل احترامه ولی بنظرم رونالدو بهترین بازیکن تاریخ فوتبال دنیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29511" target="_blank">📅 10:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29509">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=AivEP5nWfHV99pu7g7xNmf3HOcoKyuKivtYpxFJgD9JzeNWU243XHXBuWlRYaIsWNtsCaZ4zRItNSv2_xj81NdlhLyK0lR9u8ecgP7zIRHXmrd71c1HcrUl9bdq-hQ0yAC9WOdcrihcaoxE28ulkf4hrHarB4PvbOOrSOEmTQogHCkTu6g1gFvavCtPD7EpeGCansLUgTGM8PK6R07unsPZwgnEKgSp0ibsUiwb8kr797dEN2rYBIvmVhX2Eeho9utaJLTtdGbJV1FrhWegI8uTTd_GlDuIwhpCR0-l6fszxdytHpagN0mcrF4Je7LBdP-4VJboktxeICUrbVB9-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad4501227.mp4?token=AivEP5nWfHV99pu7g7xNmf3HOcoKyuKivtYpxFJgD9JzeNWU243XHXBuWlRYaIsWNtsCaZ4zRItNSv2_xj81NdlhLyK0lR9u8ecgP7zIRHXmrd71c1HcrUl9bdq-hQ0yAC9WOdcrihcaoxE28ulkf4hrHarB4PvbOOrSOEmTQogHCkTu6g1gFvavCtPD7EpeGCansLUgTGM8PK6R07unsPZwgnEKgSp0ibsUiwb8kr797dEN2rYBIvmVhX2Eeho9utaJLTtdGbJV1FrhWegI8uTTd_GlDuIwhpCR0-l6fszxdytHpagN0mcrF4Je7LBdP-4VJboktxeICUrbVB9-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب سسک ‌فابرگاس سرمربی جوان و موفق کومو درباره بارسلونا مدل هانسی فلیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29509" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29508">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=YQo8Bq_B3-l68enYT6NK2-2QG4cZuP8A8RfHc5LgV9rE0tP44dCRkpAkbQihYGjcFlfQKMC883sYq6iU6EeeRg4qgCrtcU8Esbjggt2nJTyPXBEMcZ-e6aarDTbm9J6ElRAeoH5T-dhTHpvJw7e0VWQYpQy78QREN-FP3_Z1LsMWQpmncpQxgcWj8Zogdu7uy8FsNA2iuvxAUrjQ77sWWEHcBb5JXtOwIVJ-7f7JFzFmE-KOo9QGtfCqBaUnyl7Hr2AM--2ID_vSprRpbN1T4jusaDQr-NDXzBVDn9guO7oasVOX3KvdQyZOUXeuIUBTdrr4pcpmU15oexo70HjRVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5e1c9532.mp4?token=YQo8Bq_B3-l68enYT6NK2-2QG4cZuP8A8RfHc5LgV9rE0tP44dCRkpAkbQihYGjcFlfQKMC883sYq6iU6EeeRg4qgCrtcU8Esbjggt2nJTyPXBEMcZ-e6aarDTbm9J6ElRAeoH5T-dhTHpvJw7e0VWQYpQy78QREN-FP3_Z1LsMWQpmncpQxgcWj8Zogdu7uy8FsNA2iuvxAUrjQ77sWWEHcBb5JXtOwIVJ-7f7JFzFmE-KOo9QGtfCqBaUnyl7Hr2AM--2ID_vSprRpbN1T4jusaDQr-NDXzBVDn9guO7oasVOX3KvdQyZOUXeuIUBTdrr4pcpmU15oexo70HjRVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از واکنش دوسرمربی بزرگ دنیا پس از پایان رقابت‌های‌جام‌جهانی 2026؛ یکی نایب قهرمان جام شد و دیگری‌از آسون‌ترین‌گروه‌ممکن‌صعود نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29508" target="_blank">📅 10:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29506">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=EznClc8bOLSJpgx--JEGtVKITFzaSQ1mVkXIIOhV6HJMH_shP4sGKkgGOrd_MZb5TAkOzu9HqR0vSMYC332eILFse67vLgKzftVzbbr3Fgnp9tqe1NDOY9E_GEK_wVhM5-Xj5u5fw5UlpMOdqoEwj2km7GWQYodKqC-VuSEJRh0ieqjcw0nOfWoCGinm_tE6oiyJmZmhZPHMtWlAiKi-sbB6lUBR0LsaF3RO5JjS4_t5WO-P1HDU9N_anD-zrT57fuGkFylIxgfO0oss0JXjjhOH6ickKKu9ePGJeoyGLuOiQIRXelAbmKZFYGcVWYWeI5Nptg8W6lqa6kHTnYoElg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec53e2096.mp4?token=EznClc8bOLSJpgx--JEGtVKITFzaSQ1mVkXIIOhV6HJMH_shP4sGKkgGOrd_MZb5TAkOzu9HqR0vSMYC332eILFse67vLgKzftVzbbr3Fgnp9tqe1NDOY9E_GEK_wVhM5-Xj5u5fw5UlpMOdqoEwj2km7GWQYodKqC-VuSEJRh0ieqjcw0nOfWoCGinm_tE6oiyJmZmhZPHMtWlAiKi-sbB6lUBR0LsaF3RO5JjS4_t5WO-P1HDU9N_anD-zrT57fuGkFylIxgfO0oss0JXjjhOH6ickKKu9ePGJeoyGLuOiQIRXelAbmKZFYGcVWYWeI5Nptg8W6lqa6kHTnYoElg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرفان‌کرمی گزارشگر دیدار تراکتور
🆚
استقلال خوزستان: گل عارف رستمی به بیرو بسیار شبیه گل ده سال پیش کاوه رضایی به این دروازه بان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29506" target="_blank">📅 10:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29505">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59654769b7.mp4?token=e8AzL6ADqSwuGJn2J7w6e6iozVMxzrSc34bMSQKGUfmdjA4ypGaJ7IuYTFCQq4qn6Lr6Goso6yeGWMXLF9aYLSEV3taHiWXdQhYJnS10pcgUK3EjXmjUppuOrFblhB8XCKsX_VrhYrVR2i7e3DUpqELQOxe_TvWW4FPZJbRMWvgpMV-BPQHqDp3q21Lpke2cd7bDU7pcOwp0z1r2-NHSH0UO9SJ1Ys1XvwZqDcIr9b5eHxnVlILBJRqwAnaz2WeWEnQe6zaIuL9EAJHMI5Cqv_ZrVd5l7fa9ytpcqbmBdvIU8W_fDMvLeStKEwcE90WHR5TmnuQ-pZme79P92cdbkRxyQhRZQ5EJIn84_sfb_BCLvOUggp0TEUiFZ74W6le4yKSS3HreUM8Rm_ws_2nPyZ5ulP6l3VqzXTzRTxyH1VmT_1Nl_rEKdgNm3EkVEc6qSJZM_JubTkHQo3HX2MfiUpgMPNrQAFioBANsYRZNo9OzyK7zWUwOMcq0W8Cw-zBZ9bZce8kq7Qzi2iv6NxL-OOxHe0Z5XVkcfgLoEujMOu_LGb1qRFpTV9agSP9d1Tn-XcKlhDoDL0cQxbjQtwYs9hYIr6oBtqGqwsY1WDxA8xJJhmI4Ce6GQwETgnhAttYzekDMBtGDfWnSPdB4HyRWMUjrG1KMmu1xgrz9GjRMW18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59654769b7.mp4?token=e8AzL6ADqSwuGJn2J7w6e6iozVMxzrSc34bMSQKGUfmdjA4ypGaJ7IuYTFCQq4qn6Lr6Goso6yeGWMXLF9aYLSEV3taHiWXdQhYJnS10pcgUK3EjXmjUppuOrFblhB8XCKsX_VrhYrVR2i7e3DUpqELQOxe_TvWW4FPZJbRMWvgpMV-BPQHqDp3q21Lpke2cd7bDU7pcOwp0z1r2-NHSH0UO9SJ1Ys1XvwZqDcIr9b5eHxnVlILBJRqwAnaz2WeWEnQe6zaIuL9EAJHMI5Cqv_ZrVd5l7fa9ytpcqbmBdvIU8W_fDMvLeStKEwcE90WHR5TmnuQ-pZme79P92cdbkRxyQhRZQ5EJIn84_sfb_BCLvOUggp0TEUiFZ74W6le4yKSS3HreUM8Rm_ws_2nPyZ5ulP6l3VqzXTzRTxyH1VmT_1Nl_rEKdgNm3EkVEc6qSJZM_JubTkHQo3HX2MfiUpgMPNrQAFioBANsYRZNo9OzyK7zWUwOMcq0W8Cw-zBZ9bZce8kq7Qzi2iv6NxL-OOxHe0Z5XVkcfgLoEujMOu_LGb1qRFpTV9agSP9d1Tn-XcKlhDoDL0cQxbjQtwYs9hYIr6oBtqGqwsY1WDxA8xJJhmI4Ce6GQwETgnhAttYzekDMBtGDfWnSPdB4HyRWMUjrG1KMmu1xgrz9GjRMW18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29505" target="_blank">📅 09:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=VCw6k4VfsGr-9P396H9mCeQA7QVFDMqvP6_ClRbfywbcBwfHxsOjrPt4mgMiXuCXde3a3-jT-ej-zKAN-Tb53NdRtCNg1RaEa0-_vaG6xKHBiuKcOeAC4KQb4qtk5fH4UllZyIVG-O_5BEI8XzXCO8TNAOfjEnBEunEQBKngGjWyRGGxqS41IBGieBZsl-QibkJ9t-YLIFVFc8DAVtV6kB--d7Qn-Z3uiv-MHF6bt32vvnMjxIs_A9Ox8qW2CpcpcLXEZrJsrXkSPM7I1vrwjvv8Pl_2HEOFgoSqfIHmHFps0zVFbVqLFN0suNAWlC5KHwfwlMY-hwo-mH_bSZSWeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cea298e80.mp4?token=VCw6k4VfsGr-9P396H9mCeQA7QVFDMqvP6_ClRbfywbcBwfHxsOjrPt4mgMiXuCXde3a3-jT-ej-zKAN-Tb53NdRtCNg1RaEa0-_vaG6xKHBiuKcOeAC4KQb4qtk5fH4UllZyIVG-O_5BEI8XzXCO8TNAOfjEnBEunEQBKngGjWyRGGxqS41IBGieBZsl-QibkJ9t-YLIFVFc8DAVtV6kB--d7Qn-Z3uiv-MHF6bt32vvnMjxIs_A9Ox8qW2CpcpcLXEZrJsrXkSPM7I1vrwjvv8Pl_2HEOFgoSqfIHmHFps0zVFbVqLFN0suNAWlC5KHwfwlMY-hwo-mH_bSZSWeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لیگ برتر؛ کار بزرگ خوزستانی‌ها با بردن تیم جوادنکونام؛ تراکتور بالاخره در هفته هفتم تسلیم شد؛ نخستین شکست‌پرشورها در فصل جدید.
🔵
استقلال خوزستان
1️⃣
-
0️⃣
تراکتور تبریز
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29504" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95470742c3.mp4?token=eioWUhrPpUQ3dZX-cc3VSYyPuUWH1IGncUxGaOM3rGCkgIIdfxyiNC5H_EaehynI5YZkUqNvAlXP4l8K-b079NvHd6-i5AG5X6IyBSQb7zQPFhi85JhY0UtjnjzfplDNSNcNjM8-xmmMgkiIdddth3p9quwhYDxJMqzJnY6PKMnGG9Eq1uPa-1CXeTQ1x6nq_lZqlUxjwRrxK1NTjg0QzMgXLWfEsfd47npSfg4B1hU-cW5O-Vp0i9Zajed0LRlzqiqE0zn9pJ_bNqocZZZ7MamZLf2MgCxtczqubEkr6Ragdg6sW3h8OO1b9czfns55Ks301Fhj0_VZLYFHsW6GVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95470742c3.mp4?token=eioWUhrPpUQ3dZX-cc3VSYyPuUWH1IGncUxGaOM3rGCkgIIdfxyiNC5H_EaehynI5YZkUqNvAlXP4l8K-b079NvHd6-i5AG5X6IyBSQb7zQPFhi85JhY0UtjnjzfplDNSNcNjM8-xmmMgkiIdddth3p9quwhYDxJMqzJnY6PKMnGG9Eq1uPa-1CXeTQ1x6nq_lZqlUxjwRrxK1NTjg0QzMgXLWfEsfd47npSfg4B1hU-cW5O-Vp0i9Zajed0LRlzqiqE0zn9pJ_bNqocZZZ7MamZLf2MgCxtczqubEkr6Ragdg6sW3h8OO1b9czfns55Ks301Fhj0_VZLYFHsW6GVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇫🇷
درپایان‌بازی‌بایرن؛ خبرنگار از اولیسه میپرسه میگه حالت‌خوبه اولیسه میگه‌نمیدونم، خبرنگار میگه حست‌چیه دوگل خوشکل زدی؟ بازمیگه نمیدونم من همینجوری فقط شوت زدم توپه خودش رفت تو گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/29503" target="_blank">📅 09:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8vSI8hCrnVxk5Y6GooF86SIWl9R7NXdqKFTaoDc_a_RtHDQE9C0Grpr7VSphfG1NtfyhUdjxXY_6HHLQNAj98FW6wI3A0-TLF_UA0HVsFp86zhtD815FWgth84qAB9Mt2FlTG_JeI-Q3AAckD4g6dYbEop5iyNVTgghvmMv6VWLCqJ_bOPMHAo2zPf-6J1wEPaxnQSfhR3SzkWX0dL3HNaR8bRH94ybGY_hIE7eWf3xM81_6yxmEu5aVwKxgaPyhngfWD5vwijNaXBed1rivLT0IimDzkF7HWEaoeDIPxjqkFv2l38-JQXV9jHqYC0lw59u8BOBXLy_TSIzhMj5pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
بعدازتساوی‌مقابل آاس رم؛ اسماعیل کارتال از هدایت تیم فنرباغچه استعفا داد و اعلام کرد دیگر هیچوقت به این باشگاه باز نخواهد گشت. کارتال هر بازیکنیکه میخواست رومدیریت‌براش جذب کرد اما نتایج ضعیفی در همین ابتدای فصل کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/29502" target="_blank">📅 02:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29500">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=d-kk8ABOaLcJWhiCdkTJ03JwPpDpNUEQtuB8JfdR-agIW6z081P1ug2HJxmB2YMiVoO8FMb3RhY4Gml9ksAUKLM6KOQpnnqzuZrbwZ_gzMjRuoJfadWMOS_C-IXjLffYfjbRQsu9eNaz_fva8vsWPsEnrCJX1tsgXOAHjF-Bh_nYJ4ke7pjdscfjoajUNSx-lBh-xh4EgCHIItxgNO-yhrQSxbba5zFieIaod60ASxMEgPh-IWb474VmbCGj_JakGOduiS2Kqr8fz_2v6jgd6-lgIR9pqXY5CsQS63dqaNjF6PXpuwyMsaaEvKPkMAdGrMPvAs2yjnXJi9LaabKmRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a82a62e0d5.mp4?token=d-kk8ABOaLcJWhiCdkTJ03JwPpDpNUEQtuB8JfdR-agIW6z081P1ug2HJxmB2YMiVoO8FMb3RhY4Gml9ksAUKLM6KOQpnnqzuZrbwZ_gzMjRuoJfadWMOS_C-IXjLffYfjbRQsu9eNaz_fva8vsWPsEnrCJX1tsgXOAHjF-Bh_nYJ4ke7pjdscfjoajUNSx-lBh-xh4EgCHIItxgNO-yhrQSxbba5zFieIaod60ASxMEgPh-IWb474VmbCGj_JakGOduiS2Kqr8fz_2v6jgd6-lgIR9pqXY5CsQS63dqaNjF6PXpuwyMsaaEvKPkMAdGrMPvAs2yjnXJi9LaabKmRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گل‌های‌دیدنی‌بازی جذاب و یکطرفه امشب بایرن مونیخ
🆚
بودو گلیمت؛ حتما ببینید از دست ندین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/persiana_Soccer/29500" target="_blank">📅 01:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29499">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8b6esuERpWl6TJYvcA9f2pgiZrw0IHIrhfwsYrPwgY6_qwUUqJXzXrSGS6EGwRLAeR4-Iq2CL2E7wRhWo1-CIPvCjZjaAgnD07xrgcVPpvsNpafr9rVmcmd2-8fJ8zddyV6boNeFrTPF9H9iScUfYcurkT-qcXO9-RLFBid4ru4P48SFetrGNBcsvaKkr-nk0vuQKhT1e7C1S3k_kGJ0EYsgVJtp-2k-kRXaSjrCagmW1BW0qp2oXfGoBbJxLNe8lwuoDP1VdQ9Q7q_NtqsqgFrC54tfKgF64WdPrJ-QgtIANcY6vMMLl3LhcZ346Cuywe9xO--AFdLcsvDUmjwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/persiana_Soccer/29499" target="_blank">📅 01:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29498">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkh4stSNWLB2AXoz7MMEeyayalOp2gxSK7r5BstE2dyMgetfdqtKaAYg5Kk-pDCvgLlIyDHFMTLgb6eCJOXYpmm3HC54L0PDKSquD5fMkS6udsytqRHWCZLQPc9kdopJr6DLbqAx-Gyut4iqVxwCOgyEeS7P-ehB7GrQ8c976068jiCyapQ_PWD5mAoZv6CwayiyPZi2DAcGrEgaQgctkBjP4KnCBVHDBYNcuhMoSWE9TznKmNG0tY0v2njyHPC8BwAIwFid6NsvsHorqTt3CjFg_aLEWetDaVRD5YAJJpjABY5U-4fWJ3m01-DwqGFX4zcrIV9RfqEked6juSi-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/persiana_Soccer/29498" target="_blank">📅 01:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29497">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uulPNKk2E6AO9On1keGNBgmaBkv-_qyklDrRIpMQRuqesl-vCXot0FxUk2Wus04OymK3qashIgWtkOde7fgtxT-EO8MBTTcQSku7XIjRjo9yQ80AMqiY9wSGmil8LJbi5Ki8pGXm4wpQ1JujjSMrDWOy3fWLuyRSqqBEmWHpZrJQV4abyGG53S48iFbHjlkgkRDt_po__jEy0xJaC4uJxe8yb8pI7mv5-MXeSSUuTUGvegB5cqZ-TUGsi_6PehNCkeXvABJ6oFpqEEAGomZX1EHWWduZ4Zs0NHYwxZU-a3nYBKcKaz-Nh6Au1N0pggKOxRvdmSvwdqMBp1FqevAZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ مصاف یاران محمد قربانی با تیم ژوزه مورایس در هفته پنجم لیگ امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/29497" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29496">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UORGCp7D_mc9LMs_wsgZJr_IOvLh212XMOIeKpVHPu2swZ6moNCtk8V0gZVVXv8OPW2B8eLUNIoTx_-GyWV6cD8OSmD5s42oaLWDB14jnjZY01WKpULyRmvvEkZG6A_0qTQIOQab14tNrRwc3yFOU70uIrQkx3ebv4bESwUAosxL-jKfvqv5GjJR1FIEwZ5O0JarcEBEUTmtLX0sovTzn4L8f7uOLjC3w3qIoVSfqD93yyxKs02wWGo7NjrGLP02czkypQT1FNEhNZb3MRgASMgZCboEvNWO-c_oUvz1xXsyCez9_NeQTEJHu9lPEJ-4KdaVlotqK0Vs60bt8_HU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد آبی‌ها با تک‌گل آسانی تابرد قاطعانه‌بایرن‌مونیخ و من‌یونایتد درگام نخست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/29496" target="_blank">📅 01:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29494">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📊
نتایج‌کامل‌دیدارهای‌هفته‌اول لیگ قهرمانان اروپا دریک‌نگاه؛ برگاتون‌بریزه دراین 18 مسابقه 69 گل به ثمر رسیده‌شد که یکی از یکی خوشکل تر و خفن تر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/29494" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29493">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/29493" target="_blank">📅 00:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29492">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0EXIIsBZAO36-fmATFA7xL0wClizxv0dYdJxaraeA_lZ-U-GryvSWN_RoOn3BtsQ6Xb92zhaxVv3VJN-wZnh1KzNyPo8ZYTZBsKkyR8qP_0PsmS5ztszHV-z1MIQMHddbHk2-LazsjVOIAXmGl3NszOUru5aQ-YyJixKKvSBXR04sxjrLdiFsLpUq8dVkE8UgqfaQgdJvdRNNtfttbHmBQUckStnAQBo_69PgmVUwsi5Wj8cyUi3tduI3oTQHWuIvKfpIKtslRYNz9PZRy8bWUu-PA0kT6Obaz7lPHeoFH895gP2p7t7sjx0oqc5hFryJb0XLDNWqYIuggiTk7F1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتیجه‌دیدارهای شب‌سوم هفته نخست لیگ قهرمانان اروپا و جدول رده بندی رقابت‌ها؛ آتش بازی باواریایی‌ ها و شیاطین سرخ مقابل رقبای هم نام و نشان خود و پیروزی کومو؛ اولیسه باز هم درخشید و داغ فلورنتینو پرز رو تازه کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/29492" target="_blank">📅 00:38 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
