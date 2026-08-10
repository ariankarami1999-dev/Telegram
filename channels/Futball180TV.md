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
<img src="https://cdn5.telesco.pe/file/ZEzTZQGvM9NxmsM2Qm5055YaR0sFNFYwMoiiUsJvzvmx5b_EBeMtBCyLRd9pd7a7QlhG-y3DWv5avILRclvKBuXpkYlfaHt_YIdDX_2hed_qDe_nOQqq9zjc8MmKn4fza_7sRwhgiBP-Oou3vHFvmK6QDjxn8349LS0k4bV38JQEei1uV1qGe2zWEv5_Cjbra9isfC7AgyXv_stE_O0gCjlZbqSMrt9dB-LR02Yl87mx3dGwP1WF_XA8sLB5Rc5zctH8JjI5p0t3Y8pH5jnYcO85Hantv_s4c34q6aRKYNNQSvxZazOU8b-WfxYFJxGSXZBnpajlgrKaCi4ATdwqQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 480K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 11:51:28</div>
<hr>

<div class="tg-post" id="msg-103235">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=Q4Dgs0uH7P-4q6tYyaH0zzyBMJH9gWl3k5x4oy2zROMrQufRxB8EHIsQNNkk2deyXla1PfDsF8zIbjGihlwIR6vTPWCs_fc3lwga9-6rUKYXjsWbZ0mpIUWTwfPoRrkTyFHKtqipQzWrduoLt-rZ9OwVCnOWYsFmMD-jti_LpKPm3C-13ImY-ad8TeXao61j_CaWj9DJMWIsUBAkbAZNrjkqm6TchZn-C6Zafu1AI1IXgyvcZUhs9_QymiFOvFj992pNE5uR2Z9AGr_iFRGEzcJuegONzGGokOT-3zEmBGFzTZHBQAS_4U5UVUHcAwqeedcoMZqpKIP4guXCWqy2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=Q4Dgs0uH7P-4q6tYyaH0zzyBMJH9gWl3k5x4oy2zROMrQufRxB8EHIsQNNkk2deyXla1PfDsF8zIbjGihlwIR6vTPWCs_fc3lwga9-6rUKYXjsWbZ0mpIUWTwfPoRrkTyFHKtqipQzWrduoLt-rZ9OwVCnOWYsFmMD-jti_LpKPm3C-13ImY-ad8TeXao61j_CaWj9DJMWIsUBAkbAZNrjkqm6TchZn-C6Zafu1AI1IXgyvcZUhs9_QymiFOvFj992pNE5uR2Z9AGr_iFRGEzcJuegONzGGokOT-3zEmBGFzTZHBQAS_4U5UVUHcAwqeedcoMZqpKIP4guXCWqy2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
🎙
داریوش: شجاعیان: شفر قبل دربی گفت اگر پنالتی شد فرشید بزند. رحمتی به منشا گفت بیرانوند تو را می‌شناسد و نذاشت پنالتی بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/Futball180TV/103235" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=lxJOR1wCjuypSQDzeYzWlQD4BEhpIbInpwx4vCPoNM_ZDjghl0VjORLyuAu2DNX-29EBIswNp9030xf9UxqEIICgNo6wP8YbfxVOjm73GuCMB6a6RRUz2OJHV9yiwgTWbWRzqbFWKFvp_I0JPRntNRoraTFf71w8XK2hZUxqnSt-dbHgzKF1ztRGIfuYVGrdc4oFTo5GP2uSEjkZUiTAgDM8o4x6hJ9dZbLJ2_CDngl-w59u5Yi2L2Kv0NoeUAS65HPcU-qSomRVgTmrtJd4mlSE8q3v31hiIEv_PFKXAnaEq-rctwRbo2jsn_HxTUWvCLPd_ekkulLwIdUpoEClYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=lxJOR1wCjuypSQDzeYzWlQD4BEhpIbInpwx4vCPoNM_ZDjghl0VjORLyuAu2DNX-29EBIswNp9030xf9UxqEIICgNo6wP8YbfxVOjm73GuCMB6a6RRUz2OJHV9yiwgTWbWRzqbFWKFvp_I0JPRntNRoraTFf71w8XK2hZUxqnSt-dbHgzKF1ztRGIfuYVGrdc4oFTo5GP2uSEjkZUiTAgDM8o4x6hJ9dZbLJ2_CDngl-w59u5Yi2L2Kv0NoeUAS65HPcU-qSomRVgTmrtJd4mlSE8q3v31hiIEv_PFKXAnaEq-rctwRbo2jsn_HxTUWvCLPd_ekkulLwIdUpoEClYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین‌بازی ضعیف دومفریس در‌ رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/Futball180TV/103234" target="_blank">📅 11:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103233">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7ItAT4X3scIY0vtTL5143FlnKR3muQrco1-1csXic5lbXbmERU9crH0x2H88538DeTHWbJa5JrObu65cCGePHqkanjK03F3T0Yg4vHw1Q3HK_bHlYBBzsa9uc4eCj9iBZ4ui6xc_Susaj72lOcECuQ5eD-bcuC657aaAW7GtJoomHlSGtqv9PbwhmNHxhH-JUk4plenCfIS_g-eg40RCZ6f6CLnRot7iPcWD1R9GAknEwbRNJWKWXjbh0qjgvu75OAQT5MaaB78xs-ftxijE_dJ8ELJwDta1maTDG0OqHQKvJLPmNsq3YaP0Q6_PDMWVaslv32H3bk8JR91VUkI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
5 سال پیش در چنین روزی؛ لیونل مسی اسطوره فوتبال در انتقالی پشم ریزون به PSG پیوست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/103233" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103232">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuSQIds7s9NDbJQ9bcUpyRikGuHyGd7CsiwD_SFbF2zUcitDLXj9pXW7EFnvUu9nXml3bxddmRMygU2DR0pSPOvhZACjGkS4ISxEIzGroG6vzi4NDQZ82ZCe52RfeXnFDO1ewM7viOrY3DVfN-60_Ovxreo6zBjlewc6Ujy2J6NHMr08Cbnqg74Ig1i7RYNtiIy7QvgAylVNLBlJrErN4EHaEoIg6enmPNic7TL0v8avS11x5IP19MBgiz14G8o0hKjg5LBdJ7wk6LQ4eIzHv97tGkuDZK1rxDZUxIzDFdrdXE_XpeCfXWI1IhUJ0_CKMvMjsbXswy3WgU8mDAuKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
😳
جرارد رومرو خبرنگار بارسایی امروز کسخل شده سر صبح داره دوربین‌های سطح شهر مادرید رو بررسی میکنه تا ببینه آلوارز کی رد میشه و کجا قراره بره
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/Futball180TV/103232" target="_blank">📅 10:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtY0n_BXsEm3MvxevMgJ3mp8-suYPSXzUGTpyfCds3aVZPb0IPSjw4KCScUUN5whgibriOiTI9qbWNBa8g870IuaQvWBpG0M2o0TuBLw08y-X9IfIak5YX5YyMtJlRBO8TVYMWhJzhXr2jLnQ4PyPHqry6fGhijEBl4bTM9gRARC-sAxCO9zqpP5BkhnN-p3zGZ5l8Gq9uzVXXl049xz1SdPsPimLZwQqZUKXbIDGpd0rXVQKd-Ub_CbpCXvA32HZDzbzt4NAA2a8zIPc1syFMAeG1_p4qKympiMxZg7OKvHQuH-yJyPBnAWsIDl9I9IUZQk3ux1ZFVQ8h5cOwziVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: ایوب‌بوعدی ستاره تیم‌ملی مراکش با منچسترسیتی به توافق شخصی رسیده و مذاکرات با باشگاه لیل‌ در جریانه. بوعدی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/Futball180TV/103231" target="_blank">📅 10:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=iBa6U1S9oWFnMhW3r5iCH8c32MlUcM1Kujj2kIR-hEv4lNYBPtwUj4Rcwo20wM_pUP0hQ7mPXwYGSk9axp7t3bdeza5Ub4n9B1KwX85tz4F_WPl5ShAWSM1MLjsZiRGm1ofe0NZt5pTx4JcgflK6MClvBjoS-IKhqQfo1jSwxv2IKgD49pHuuFitgKnwYXS93UnZ5feoapqiCQkCZCxXkgqu3KZiBLSxKwgyIpKnAImas9lfjQF2UXRKE-QSR3DD7bl3KAWVZ23JWnrJd3ARyB62Afsl_Fy0wLYVDrDHTnIP4v6EIeAi_N-ME3domRJFAYpcnvFRuG09a4_JSS4yebs5W9Q04WcyrsC9_3m9oyzzkc7bStLvJQaj9n07BYEekgIjsESSI4kXw00tahaf5sh1p_24rxnzvdNNAkqb0A-QWlMz-Lnf1qCeV1b_roR8rvbuihmiX3X9CCoKM1s_jdFdQN2uTOvzjNpF7WfuIHSAoXuoe2CaBmosBhNQAPXDrMXiPv8fbJx2_Cc_yaMyZcRLV0Oq1ugh-LRrF6orHnF8EpaTHYmtiwhcX71xtSsihZqC6Dv57iqiYtw-vU1cimDI1cEQhoOjqNFLgwIn1Bv4FVabtdxmgPcrgxcC1xRafyC8qjrORsyTGtu2TudAvDPwgywtXafcMcoycZbLPL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=iBa6U1S9oWFnMhW3r5iCH8c32MlUcM1Kujj2kIR-hEv4lNYBPtwUj4Rcwo20wM_pUP0hQ7mPXwYGSk9axp7t3bdeza5Ub4n9B1KwX85tz4F_WPl5ShAWSM1MLjsZiRGm1ofe0NZt5pTx4JcgflK6MClvBjoS-IKhqQfo1jSwxv2IKgD49pHuuFitgKnwYXS93UnZ5feoapqiCQkCZCxXkgqu3KZiBLSxKwgyIpKnAImas9lfjQF2UXRKE-QSR3DD7bl3KAWVZ23JWnrJd3ARyB62Afsl_Fy0wLYVDrDHTnIP4v6EIeAi_N-ME3domRJFAYpcnvFRuG09a4_JSS4yebs5W9Q04WcyrsC9_3m9oyzzkc7bStLvJQaj9n07BYEekgIjsESSI4kXw00tahaf5sh1p_24rxnzvdNNAkqb0A-QWlMz-Lnf1qCeV1b_roR8rvbuihmiX3X9CCoKM1s_jdFdQN2uTOvzjNpF7WfuIHSAoXuoe2CaBmosBhNQAPXDrMXiPv8fbJx2_Cc_yaMyZcRLV0Oq1ugh-LRrF6orHnF8EpaTHYmtiwhcX71xtSsihZqC6Dv57iqiYtw-vU1cimDI1cEQhoOjqNFLgwIn1Bv4FVabtdxmgPcrgxcC1xRafyC8qjrORsyTGtu2TudAvDPwgywtXafcMcoycZbLPL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🏟️
آخرین وضعیت استادیوم آزادی تهران
✅
قرار است به‌جای دروازه‌هایی که به‌ صورت ثابت در دل چمن نصب می‌شدند، از تیر دروازه‌های سوکتی استفاده شود تا در مواقع لازم ؛ امکان نصب، تعویض سریع یا جمع‌آوری آن‌ها فراهم باشد. عمق محل نصب سوکت‌ها، بسته به مدل ، معمولاً حدود ۴۰ تا ۵۰ سانتی‌متر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/103230" target="_blank">📅 10:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3E7Fx3MB35Ubim0LOVN2qzQ657VJORaiq2NL28S2mSZcB6xO_2-2eMTm33teP7iCcFtMwud5Qk_TMhRutXuU0ss0k60s_GrYFxEFrkdzhPcWPY7mQjjpV9tiytgySthTAUXFEA770FICvmihWhZVlaUhVDxLWH-z33214o-Giz20-LOcjSjCtxbYu79eWXkzstj-UidYaGiCjMPZQEpXn2DLElEhZiH2vTdy_ZfJ0K9rBzzBlaxiGRDzGbnwcp5fDtgInxEs3yWNd1zsyjpTGidhdgkuSyUS6CVChIIIBBI8AaT2UTaZRwix_APCneIM8gi33_2O-g3Uu5pVB7MFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
آرسنال برای فروش زوبیمندی خواستار دریافت رقم ۹۰ میلیون یورو شده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/Futball180TV/103229" target="_blank">📅 10:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=vhpzo2ugisCaitgO0mNS26O0p5KZprfFF0eFfClZilsHTAmJWeUjiGxg0j8Oed5-wjx08j4wZv66su__bISUC4OrLgEliPszL2LjSIhHxs-jofGcoCEMAVOn-dppm9dWTj1LDJs18wP_ITQnmAPinG4Kdt1rXJUwctjdkx9u0eztLm8lZOGByO-xFdBS187fRJXojG2PcmdfdTeB112NVe564HfRssZFtPNQPnQn_P6iRXWZYAZ1u2-s_mS_A-k9cXH8Hx24ybIOv5yWX8UPphJKWkHg52ti5S_ihjihrb_KVXAE272iDcp4OigIitx6Yxvve4XKSD6z4ZkuyBLHCWVzPuJg2UpWsO_ehGdfRnQJMXqD1Zwoo3IojMSNTZocS2MrSA7exO204xFr016bnSzRtwZM_XK3C8JOsrS7K2neku1fyDT3xpHRxzkb2WZH0WLupVdpl26Ky-pHEJ-_YgeGpYtFBX00KCeAIDdaSj_BvxRER6bpnsHkMtc1JCnJk9uRLa24loX8xUzGUTaDwFuwfUZNuKNOkmXmSLVKjTnDnxlARc6Le6uzvCR3gQ9CtkBo6kDQnEvZyICGE3mYSgPJFuOo-mOqpfuGV-RhJ0t8dQfXf43V1e4W0GLfd8wnKkIZdb_jEGensYqIB6PlFnK9X0G-K0rdi-fYhRk1Wso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=vhpzo2ugisCaitgO0mNS26O0p5KZprfFF0eFfClZilsHTAmJWeUjiGxg0j8Oed5-wjx08j4wZv66su__bISUC4OrLgEliPszL2LjSIhHxs-jofGcoCEMAVOn-dppm9dWTj1LDJs18wP_ITQnmAPinG4Kdt1rXJUwctjdkx9u0eztLm8lZOGByO-xFdBS187fRJXojG2PcmdfdTeB112NVe564HfRssZFtPNQPnQn_P6iRXWZYAZ1u2-s_mS_A-k9cXH8Hx24ybIOv5yWX8UPphJKWkHg52ti5S_ihjihrb_KVXAE272iDcp4OigIitx6Yxvve4XKSD6z4ZkuyBLHCWVzPuJg2UpWsO_ehGdfRnQJMXqD1Zwoo3IojMSNTZocS2MrSA7exO204xFr016bnSzRtwZM_XK3C8JOsrS7K2neku1fyDT3xpHRxzkb2WZH0WLupVdpl26Ky-pHEJ-_YgeGpYtFBX00KCeAIDdaSj_BvxRER6bpnsHkMtc1JCnJk9uRLa24loX8xUzGUTaDwFuwfUZNuKNOkmXmSLVKjTnDnxlARc6Le6uzvCR3gQ9CtkBo6kDQnEvZyICGE3mYSgPJFuOo-mOqpfuGV-RhJ0t8dQfXf43V1e4W0GLfd8wnKkIZdb_jEGensYqIB6PlFnK9X0G-K0rdi-fYhRk1Wso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
شلیک‌های سهمگین سوبوسلای ستاره لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/Futball180TV/103228" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103227">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103227" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/103227" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103226">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TEsoMX3TDRfib-PIhcpq58pgX30KPLKeuNeMv1BObFm-FNpulD3wFZiAIrUPkjY_YT0W4V-dHmyOpkp4ny086GZBXrdvFU6kwyTlvlvgDg97dskg_efNUYXKbSVcT84WoGoBfIWnmlt16ddihPL8KpiERlEnX6LEynZHLAMCP190YgpYGNQncrgR_RpsD_DYcw3Vb0rMuc0VqDceO5TfT-0jLFw_iDgwB-a2MsMQlYw8fGNPHzXnkVn7rNpf7uxy0o763UcTBCREmMWzRl39gK5n6LAsd1DVyR1HXUDvqouvPyeQvpI1bSD1wlofNumoci8tmqgsta8Yar6rbEANUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TEsoMX3TDRfib-PIhcpq58pgX30KPLKeuNeMv1BObFm-FNpulD3wFZiAIrUPkjY_YT0W4V-dHmyOpkp4ny086GZBXrdvFU6kwyTlvlvgDg97dskg_efNUYXKbSVcT84WoGoBfIWnmlt16ddihPL8KpiERlEnX6LEynZHLAMCP190YgpYGNQncrgR_RpsD_DYcw3Vb0rMuc0VqDceO5TfT-0jLFw_iDgwB-a2MsMQlYw8fGNPHzXnkVn7rNpf7uxy0o763UcTBCREmMWzRl39gK5n6LAsd1DVyR1HXUDvqouvPyeQvpI1bSD1wlofNumoci8tmqgsta8Yar6rbEANUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/103226" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103225">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqfkDrF8WRGwr4QQ5yxZWthF1Ftsf5pxZrxXIfZ1wVsYouR7mV9UpsF1PDyhzW17dKl5MZNgxcJsIv-EnB2Ica0fH9mWN135SJ0l1ccFwrf-wIFIpBgMTfsGOYOXl3KxmONYPfQDV05KXGUnhG3wa-8GDUgPxn-kubBFQ1HemsfN5agDEjRoGhplTh57edPdKjn4MOlgQjzycHpo6i1lRzL7bOkNBlW8usUSKqzSaL9kk-Y1lpMng4_kaWuUQkJbMfIAUixocUU_6I8Qi2fLxDlbKUJJAuby6LDyMo1WNA0AcLu6HJRGgZrIb5Q-0Bk5Y4AwtYrqgfjGyseo2Whcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
مقایسه آمار فرنکی‌دی‌یونگ و رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/103225" target="_blank">📅 09:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103224">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJIHAdALsxGa0XN7yYoyXOgN4gf3482RX4drsrHk0V36suknCXaF0sHRdldegRCfeBGaRJGVHBCyU4EbnlUK352L5fA4A0FDbF-iBOzV6j-G5gz7Qstju9AxOvLWz6Em-_PjhZwsUIlcdpkrEzLlkd8DPjuq9r7WEuOgYFD_qg6EzmCPSJn1m0Qh1slx9ogeVTxzguVLYDjxRxDI_pk_kb4LGM2NMkdezw9ebh4lVikRiDXuxrYtWzB4bZ4zIPSv0m1W0c8R4XXWgBEWlfRRJQPG-ERYh5GAnCrVLt_sxdgJ8XDH4oyimNczfxS0CM0C6Kr5rO3D6HRtJ5EDW_aEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط هجومی فصل‌آینده الکلاسیکو
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/103224" target="_blank">📅 09:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103223">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👀
🔥
برخی از گل‌های چیپ تاریخی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/103223" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103222">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsRerGv4jJNIx6hPFSKOQn1LjXqWqTJWHA40fFFJn3bSI--rdlNFkNlXVRaLtG5A8I99ZOOsTNR3riLpNoBzPxyEPQmI0ZHGKaFKBJ9sLGA7WYlmbm4-vBSX_BCSE_JgAAy_SLZc9oxt8aR7Hi29dBqpaXyi3dPbp0K3s17CwxWd6jxGT0uLmfosqhvFtBT3r_uS4Wgbtm8sT_GLWMmZwk_JaF6UMvjWC6h3-LwHg8H9s-xOjzpsrkocTHkNA7N6x-x7529_p1gcn6q0chdj0V7VWr-JAeePgpTUrtIa5DYOZ9xW8JiJERqd4P383qUtWaWMB2Rx-4ER11-JS48bPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇩🇪
نشریه‌تایمز انگلیس: هری‌کین بزودی قرارداد خود را با بایرن‌مونیخ تا ۲۰۲۹ تمدید میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/103222" target="_blank">📅 08:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103221">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-DufT3vobUjBpoPYXv--BtLkR111_4s6l_7sYjqHZHb2xFBQZTnxaRt1LBwKSVS4vc8UudAp1oP_pNaVMKCC-H-SZG6D56m-fpGN00YDaIW3Dp7JvCevRGKemlGf-ON_xnySu1vuolfW_Xvs6qLyF3tnXx4hCX2a0fGRHPnLOfWfGA1vHuwIwH675Q28acRlxZPVkkxkL3OogGNgcFSgwYbVCCP1Z7gvncY4gbd_8E_b9zI2mp-Tx9Tm-EhRq_qOmdYtbR9pnTekHvp5SjJwIGxKYMX4XJBtFLaZT4z0OSStbcR2TUHDG8oD2Hlm82qAV65Te6Bei96iIDljGO1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
#فوووووری
از رومانو: اندریک خواهان موندن در رئال‌مادرید شده. از طرفی استون‌ویلا و رم برای جذب این بازیکن اقدام کردن و مشخص نیست که رئال راضی به قرض دادن مجدد این بازیکن میشه یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103221" target="_blank">📅 01:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103220">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ5e6mY3QeFnU8bn75Vz1AOPXETzA0W4REzzX_NVRtiXnztIVE34zJW34hWQyBA551GY57B_ANfHACi2Q3EtzH7NfGtCTyeFsRpPRuDKxMIM5ZRyuZ_swns9VqRB1GBjeM5wMatoqslXTLTM4-i1t8jN2AO6ZKfKQzrv1QGezWuuZdCzKeiAJEzJQRcAaBwybFsfeJT5G5k1ljbRy-yFUp8lhpzI1-o_D3Tjx3sp_llT9UC195DVYcnZ-nGZK2LU4pGXGCXwJGu_9s_zQnXEesph8y_5vMbbKYudQZuVEAGJ2_sEXeJQ_4wt41Vc6t7tqH3kt89Se9OtNq13KWci-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: کونده مدافع تیم‌ملی فرانسه و بارسلونا از یک تیم در لیگ‌برتر انگلیس پیشنهاد خوبی دریافت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103220" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103219">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
👀
⚠️
حمله تُند و بی سابقه محمود فکری به عادل فردوسی پور: زورت برسه همه رو لِه می کنی! نرسه هم دستشون رو می بوسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103219" target="_blank">📅 01:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103218">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🎙
‼️
📰
علیرضا دبیر: شبکه به‌دردنخور، آدم‌کش، جاسوس و کثافتِ اینترنشنال! من محکم تا تهش هستم؛ مسئولین هم نترسن، بزنن، بترکوننشون، به مردم بشناسونن این کثافت‌ها رو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103218" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103217">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtwyVXo_S9jMSPHASo2jiFGOUPxJiqz9gPdHzKdulrynJKL3YRHe63zroFYeVKt5WvmGbD8G5pR0S6JWvrVEsReLFsKLWpHmfJ-DRwOc28c-UR5q1es78c4qOscHQd5gvk31zdFc6VcUfLU0cGJ_G1xErk6_LcORidtpMXJyhKcTiL42NEpl7dzgBoyvFtDUbCNPShYuKnH66EqfXxzgw6diws4EWZIXF5XyF1dHAG56mCGthfmRbPduJ1ENMOGTWKSUW7uNHes0TEMOtlTpbXamdUTdtFgwoeb4UogBW-VqhcIldgt84ZAlr-68prniPZDEfQ6sgsW9oGPJ6YjcOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇹
برنامه فصل‌آینده مسابقات کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103217" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103216">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103216" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103216" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103215">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=LrbGlzvisXQt3YO0TghEJpwc3hgEk4V43y3QOtCJEVwrp-JboaSffIUBtrONyfk6AmKUbVWJ2xC6Fwx4xV3_Phio8U8WGjhnCVrYPzRVHMP9FDo0-LpnvarloyIrY7dCHZYpXsDH-o-6LahkNvU2KWnfM4VKAm_xWl98ayEnHMmnFOLeRlORU6WxESKkB02YfMdBL6Tbz-imXBkQSAZA7vQsbXdBSSNFWn1mTB8LCynbcaxSi3yz-wSCLNnMtjT9rUJjZPFCpqUv59JNiYZAkX0MEVfTvPbrOhZ7ZT8cCEe5d3doIV849zcIMM56fSbKt7Sv-17Jj7hN_2eQmZpkAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=LrbGlzvisXQt3YO0TghEJpwc3hgEk4V43y3QOtCJEVwrp-JboaSffIUBtrONyfk6AmKUbVWJ2xC6Fwx4xV3_Phio8U8WGjhnCVrYPzRVHMP9FDo0-LpnvarloyIrY7dCHZYpXsDH-o-6LahkNvU2KWnfM4VKAm_xWl98ayEnHMmnFOLeRlORU6WxESKkB02YfMdBL6Tbz-imXBkQSAZA7vQsbXdBSSNFWn1mTB8LCynbcaxSi3yz-wSCLNnMtjT9rUJjZPFCpqUv59JNiYZAkX0MEVfTvPbrOhZ7ZT8cCEe5d3doIV849zcIMM56fSbKt7Sv-17Jj7hN_2eQmZpkAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103215" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
⭕️
🇮🇷
سپاه پاسداران یک کشتی در تنگه هرمز را با موشک هدف قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103213" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQWLkqz7EV_AuSkxfE7KA07srHfLPzUrIZNrTWAyof2pLxGvGN5-4DI1Dlf5YKcZZ4FcNiyyASY3KfGuQe_xHYXZpCnqpKrO20on_UeFwVnEQUkQkqdM68le5wvYSogTnaxzgEHK8J1nC6HmRi-TexdQCoVYNg0f1AZ2mQbuAwXM_FaR8MSawoFAHtNGFhbP441Hk3XhsN8oHF0pze5XEoPVPFAd2ubcxCBh2yVws39Pg6ZWo2QTRIW3N0kyyd3op1y9nBb0MRmFfUOhgxCOLQBVnQkMrHlAWAT6wWHZFP_yOog-VdwyM3mu0ogRC1U6f8P5uSpD-i7kqXHHmQu6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از گستون‌ایدول: کریستین رومرو مدافع آرژانتین به اتلتیکومادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103212" target="_blank">📅 00:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
گستون‌ایدول:
🔻
بارسلونا به خولیان قول داده بعد از صحبت او با مدیران تمام تلاششو می‌کنه و پیشنهاد مالی چشمگیری به اتلتیکو میدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103211" target="_blank">📅 00:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJfbmyBQL1VEDvB0RDB6_TzG_NNPjtiwc2z2tfO7I_n2pWC18_QTGLWBtlJBarDBxopMeIKtrcSZkk7bkjVfmA0Mut1FLdGKZ2iwWuH7T5VSH6mv6m_YrVUIN24FmWmPYoC6L2HPwUPPg0p0rPLstNRAdMhrha1YvlZlxTl9NqmMFJ38pMc_0RcGDfdV9nxFfl1xTvW3VUSWf22jDdTO_IkzNmdKBYuSG0A9eiLEqOs6RjqWlGPBu8sf4qizijGu2g1HG3Xu02clsHe_syyPffs2Z-G0DIF29c-LAcUYZEFm5vHYsrh6WCDvISuLwFrhxCA_o5sSPzHm1bbzLR4jsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
و
#رسمیییییی
: داروین نونیز با عقد قراردادی به ترابوزان‌اسپور پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103210" target="_blank">📅 00:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103209">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103209" target="_blank">📅 23:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103208">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103208" target="_blank">📅 23:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103207">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103207" target="_blank">📅 23:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103206">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffgL7QWJrRks1NcfbKoC6mHDzJn93kCAubPCIEBbttNT5q83w01mYct1WSbJwZhABsUG-4_60wraS7AEy3_JuiBAqgXRT8YciBuKOo0r6SprX5cwbtV2LgxnutcIaHfTWsqxFky2R6_IzQDKxrEAFDtYdUftXau2pLQLDr-FQTHXVxR67HjyamgWBdzX8A9FP5tI16TuAQWtLGWm4PVHT1IvMN4nvvfYYt-hXt3RP2ONRqKTBVZaibeiJFKiXLcIA1eOYa3_-CwDQnPFn-3dUq36nHq7RcgohdfnCb1HUkSdU4Lrgo-jyu_nxVrLGkM3eGxuM06-BK3BbFUFXDnf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103206" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103205">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImaqvA_tjidQvD14m0vPHgIGCM37ihyLRFYgpASQuN2CC2cDGFTDY35TC8CcAOPwuztoZHkAd2_AK5uHevOo8sAv7lBXjgw-ox14EHxHgNRd6_iqXKv3ffVn0UJ5m4CxTbuiuZVpMYGyjvYrixgKpl6Str1rN181wtQmNWmf8qoF9vaud97Lb1c5d3jhPsje36ByYKnmO-siYWoR9Aa3PkoIVd2N8TTo-0YHhl2DY6WT52jtBoDYXEOUG5IxNBPWWIq76AlqRrnJB3y5SdJ0_v-CLlM1iOVSWoa5xUYj5YyrmBk44HcOVUnfFwJbkEaXbeuSZq_C8Vz6_gtjYcCcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
باشگاه بارسلونا در اقدامی‌جالب نام رابرت لواندوفسکی رو‌ در لیست اساطیر تاریخ کاتالان‌ها قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103205" target="_blank">📅 23:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103204">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mABBr1vIea-hg318ogCBL0_BC-tWMjblBYjYKT_bfdBN4_DwaWwNCHERfz7vWtCKHCNU9AcdnAi3S6-kE5P0G6XT7nqVH1qdPuHot0vRDt38SEp6PNCq1tHNXMeXvPK77XtC-AEqW2GIZxU-FyrRSGGcDdaAjG56kB_muGBigIK24k6mjO2JpAGA3eCfDhpEwcb_mHcJ05QHvc2s057zhu4G24cIXk7BlR8sfr8KRRTVbZjErwl4HWyb0jYFdlpu6poV56Sa-HUlgvfGiLTmjTnd7-0aiXuqskLLgG-csHMkPjiZcbOo-U12CntuJqsDWvp06d-yMLXgOskdFu7NlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دفاع وسطای لیورپول در فصل 2026/27:
🇳🇱
ویرجیل فن دایک — قد 195 سانتی‌متر
🇫🇷
جرمی ژاکه — قد 188 سانتی‌متر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جو گومز — قد 188 سانتی‌متر
🇮🇹
جیوانی لئونی — قد 196 سانتی‌متر
🇺🇾
رونالد آرائوخو — قد 191 سانتی‌متر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103204" target="_blank">📅 23:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103203">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0zI79B5nl5xozx4cnbeDh2xzBsF0mX0ARyJBoaeg5o1J0OXoTvFztdeCVcPTEFqYFAcCd3dPDDojBrMTzaXYR_hetCuL3C2wSWw-Pv91ycOS4WKU-XlFabtUAXYxQ_ST_xX_4-rMQ5KWQ_flyaGtdjv73WPfBoJJdHzx6ssXUlypUgs02GzP9l8Hrlp1YNa6IQH-BvI1Jgmv4Hc7Wp3eCHn0bUOhkf0jhTS_dbxOKng5ikSKePZjeJQMS9LQg071jDM_cLrcU4HhgwF9AlLfM1-QwqplV08pBs-C154taqs0b6ma04k-2qwQ7GRULMrb4ErKA6UsjhnSxsN2L0ubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
پیشبینی هوش مصنوعی از جدول فصل بعد پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103203" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103202">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7-TPWmyDPZfqbJS5JYKqGlryeJJAEYC12C1NybTrBv6wv9btN2u0HYxvdv5hhTs4vWBR71yX31yeWi50cB4870YHAaRiGnBhgzhR6Lvx-HIkX8S8LJXRoUmNFivwUH0LccH1hMsaghuKKLXfiTkSgBethqnfOqPyTfZQofiNwhAqy098wJUGKKVtb6naq0JQHBnPCbziNWsUSXZ7HLJxtjJgDXFfW36vKlba8bjRe22doPP6yIOCM6BvL8IhK_oog72llwmAEFg8STSGzpUJcrdGe0nlmJcdoqgI0nmPvMdqlzMXekODjx8h88gVE6-WZWfW8RU2glyq3GHMLZl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103202" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103201">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_y6FbsRXxjyLpz-rHLoOD1PdWglJJnS1Ktbjw0ygdgSdNR1en6lvyT3q3Lwv08uzD_DiRbwzk3GnQ1sVmyKJuEIqs5JAkrLBSZdzxslqwjqVWR97eOAeuSIDpnwj9jMigMo0R3fzE-xw3PN95p2sl-tLJh99u2LTJ5f1rmc5FjZFH6E3QuwncxcmBp25HnS2H2ppKV5l_CxszqrfwFpexdrmPZd-AjUpmrb0DFhUoUozcU31Si7TLMzpFeJA6K_Io6UD4aLlXqSk2t3vgqqeYqxrYoJ8CdJyUJ_l3kBaDJ59RGQFHanG0F6xNxk1CFruFxwywaccMM7QxYaIcTfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103201" target="_blank">📅 22:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103200">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=vWRQJFYVIyUf_rEdfHS9Sr8WJJOlqIxf-fF0YCE2SVpIWflvujGNXdZdkMAmS7TTHnQ38ZtGewsvIQcSfY9S6z0JdbvG6mqoEAw9mEcXsCETKA-enOSc3Unfe9k9eMf2oMh0CdEi2XagINHOnYvT0T_CjHWQgMq8AlDGRzqGY8kwN7jMhPRRPYG5JlfvFQsy-VSgKKa4nBMqxv-QzYyO0c64mR8wbJ1vUYNrz19ul416n-hQSI6Z4CsrIJFE4jtCviBQAgord80M57thKU7zyQ0g_NROTM4YgKi_laJjWfmg1ch5MI61t1HF4vaA9qNxzGTB8JipswajD4NLArUjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=vWRQJFYVIyUf_rEdfHS9Sr8WJJOlqIxf-fF0YCE2SVpIWflvujGNXdZdkMAmS7TTHnQ38ZtGewsvIQcSfY9S6z0JdbvG6mqoEAw9mEcXsCETKA-enOSc3Unfe9k9eMf2oMh0CdEi2XagINHOnYvT0T_CjHWQgMq8AlDGRzqGY8kwN7jMhPRRPYG5JlfvFQsy-VSgKKa4nBMqxv-QzYyO0c64mR8wbJ1vUYNrz19ul416n-hQSI6Z4CsrIJFE4jtCviBQAgord80M57thKU7zyQ0g_NROTM4YgKi_laJjWfmg1ch5MI61t1HF4vaA9qNxzGTB8JipswajD4NLArUjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😳
😳
😂
😂
کوروش اژدهاکش بازیکن جوان پرسپولیس: می گویند اجداد ما اژدهاکش بوده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103200" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103199">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD4SZq1X7nNg7uK-Xe5MssTrZxZp2nk_-mjnFku5MuYnvR8ZXWissRvgoHKZ6POPUh5Lq0rnEGjM-ouA9eC-JNswUoA56iB8vdXsyNzN_YR5iWCqVaLCFJ6rgy_wCD-rnSsDBIgruNXnBPYwOTErDMl-C_MMsayrsHne9gWdaOdtWy7vKPh2b3wfLhIjzUCoJ9KI0X96NgKo532ppOmzdj9IeFCldNEb6_xQ58ZcW7y9SaMH8j7Mnm_T5FDzq8Ylmn_s7Dd-AShEQZUywEp9mgSN_5YcL15VHAbDjR1oehfLqJQ8fFvlGTk7jXQ_Hde75RRXOY8Ogxo_30kDzD85cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
‼️
درصد شانس قهرمانی در چمپیونزلیگ فصل بعد تو سایت های شرط بندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103199" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103196">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddhPEBKNoIgJKfgEmkmRq8UtZU5CM27aSYkaBETdq18N54h9vWcIUoTC24X11iVHVZ8JbZbdYiwEN5wiQkczdDo7R1-iSbAoYTZE41OMqLFnBO8Xa6k7SbncEiNIzm71E3VranoFCbMAUZg4FPW_3Bgqedfel-QMTmZBRU_91GTyjSd0JrgbvTKH_ocQOCNV5ISwFnkkQGbf7LUd4V0IlKBxIoqdruS16lx-YY7iFgDGVz3PIdOOGeREpdGKW5GYw847dDVlyzpH2zow9H4xgT0qGlms8ZuIslVqJzlny63KIILEdB4qC_DNpmuq6VvGAEMqCf_jqs92XoxrKe9fOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2O3JCe64MnBitMBtTXcNhwG0ff5wt8bwG-DR2sBZtcWmaLfr8dMlp57vOqa1XmfspOGgdd-GkaNrFFurGnpVRwhcbMx777wLLDxl5FD2T9XocPkQZVBjKQSkQrtAhjQGJKKToe0SKNE2k_JRqkxMbuyGo59idsH0mfN_v8UfvKwUzQqvVQ6uy2ev-LAn9vVFoRW-Fy-3Qj0sOIevirbkd8_DdmWnWKgoeN6CKSSd6RO5ZSQP2judBx6S6lNE8LxY_mqBaiGTAm1OOmUjyL5emdUf75691nATbJVAnBIQQ8Btpn7MWEfOBWJHiG2ixZXVl4cj2qgbfs3sLZ5vN7_5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=uPeh5vRsqyeZm9y_fb4k5R-1t0qcShRrcqmS3RgxhLKHKCMFy62NcKgcIh6fYAKmhJL-xiPjaT7uHbvuPTS1YqQZuD_XnFP8EYYB7Wu3EnjB3neadcHHnlw8NixAxDo32gsjFcCKjJfoz3jNjbzuHbikRJCNsjuaDK-5dwns8FqepghrSnEzanC0Je_AM2n_pJWa5Rfd3yB0hMUacxpg_ISgGC2L6jLphmihnXMyS5FGpxoESvaaeJl3coNn289HuoE_DmMVo7zJCiWDS8dPGS3Cgb7IvSL8GTM4SyjQ452xhERZcYRbtlNDFjyQJCDojX8apwUIeU877vWFCz0AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=uPeh5vRsqyeZm9y_fb4k5R-1t0qcShRrcqmS3RgxhLKHKCMFy62NcKgcIh6fYAKmhJL-xiPjaT7uHbvuPTS1YqQZuD_XnFP8EYYB7Wu3EnjB3neadcHHnlw8NixAxDo32gsjFcCKjJfoz3jNjbzuHbikRJCNsjuaDK-5dwns8FqepghrSnEzanC0Je_AM2n_pJWa5Rfd3yB0hMUacxpg_ISgGC2L6jLphmihnXMyS5FGpxoESvaaeJl3coNn289HuoE_DmMVo7zJCiWDS8dPGS3Cgb7IvSL8GTM4SyjQ452xhERZcYRbtlNDFjyQJCDojX8apwUIeU877vWFCz0AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان پیشنهاد میکنم حتما از ست‌های برند mimoa استفاده کنید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103196" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103195">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqr8okGDATIV3dIjyAo8imPsa_BPsiWprqshijNJnanmYUvPsUDl-YOKKXxfmHwB9eS0EBuVPLKQsdZLwmPWE2qb4QQnpdwJwmp9fV8iczPubZZRFaNsb2iD2ynphpqpY4X6aqcyAx7NHG6-cdbLnyyFHSIAh8Ge5QL7aEM3UeCsv-mDUuC1MjfEjVVMh_2-rnP4_8i2loUVUnL9VvlGngbqnJLu20aeUGPnzuJmT9x62AzqpHuZM1LIfOG40j6e0RkAp2OtHxcY3P8Jimqw1H9r4ubsT69pKAe5NQ9GZItrri1ezo46wtOf606Rk8jmT7lF-wVDm0ub_CfUEAMDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
🇹🇷
#فوووووری
از گری‌جیکوب: دو باشگاه گالاتاسرای و فنرباغچه ترکیه بدنبال جذب گابریل مارتینلی ستاره آرسنال هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103195" target="_blank">📅 21:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103194">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjQQ7rDUZ3QC3znHgPPFK9vpXwxjSmnSl-g8qhjvC-q6aUS6dKfVnLDMaTDNMykNkIcu8Rfdpn45Z5G8Z4NnU6HGTJBVqS_vYfHYpQ4-mZ075vuh3l9PcRB-D9xlbDM-jnBIX9ec1hXi1FpzqI4cdXadA39xcVrMjc8p4JhuN2V2kiVjbFZXH_gtXt3vRDBk4kM2PKP6NTYKNYCxP-0ghh5KgQx2vdkLTF4gw38WFKhBYRzejdOwfBdUA6KZyofwS1yd-qrKj5DgCpq1HHrB8MUffbQ1P75Io9zWUtHfANzzD9fJmtuvdrX0-0YesXxt9A8V027qGqJrrOI3UeGaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
باشگاه فولام‌انگلیس بدنبال ارائه پیشنهاد برای جذب هکتور فورت بازیکن بارسلونا است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103194" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103193">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfDctse4xeQkE-hovGGheMkWmjnyCrutgzmSvSf4-ewXWmfdshuwKZsciSs2uvpu_WjreBATMg7GwMIkUrZuzmtcdGWIQnNHpEh5tAxJnV7rEndjht3DLiORQrgYNvvzMZd-eKMsotI7-Q7-CqHFR3pxIxw3mdiaoPMUIdf3yK5rNFvQ7qxgzJfrJlJK2CbLUBfkacMUbpjGv4gU5uFUrjWf3eEEZAjhUJlcBuv1CnO0se30x6lnx75kDY9aeaB8DarzqYeSrWLH3SCEGIkqT_tADiLvlGlQYB_-3lB7bxAYkM5C9Tx9ZxDDMKvZg25DvxBN83ZuaQn-k_qF7Dvgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🇫🇷
🇪🇸
لپاریسین: مذاکرات بین پاری‌سن‌ژرمن و بارسلونا هنوز آغاز نشده، اما ارزش انتقال او کمتر از ۵۰ میلیون یورو برآورد میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103193" target="_blank">📅 20:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103192">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ6AUWioAofUF_sWFx2HY6cWXSz4tkAdrwANW-72c2dYRHiqsj7ck69v509PHpMYTSQhKQs5-km4WhCEQQeYiL-CU6zBtHgsmpcY7FQAfxOm4yHZW0HWQY2GNFb1XhQEkjjVMAZHbs5MgE0OHt8yUBe--APuZ0EzflIGnjNizQOTaTlMRky6W9fBGIUD-e2KXkjYmtau6CGXDKiryc24BXuOPD_NitosetSshJMbsg8XGmu6JuZ01A31Ml5BX3LsY8oc5YeTVNzEaIzXUFXUoy7jbv-eCAD7YGgNMNnBu64DhG8FAtYzbVu8bxG27BmmzO_E6kOn6f2zJ74-Rq8-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103192" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103191">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl3HsosAcFYH5gS5lXyIhfDNGnmaIi6S2tFfCX-yTFd1hKtEaiyQbQl5scuSiVhPUSfedTfx6v8c6Zvr_iSG0wa-gg40clkQSv1DV58YYkhwZ6Tk8tX5xgYhh2umPRHYsdB_nABxsL_O6hoKtpEPJbBZnpFK-lOMTGAVxO31n5HdSEecYgjjZ9-QXATy3PSVfeJsv0pFXJ0_ot_3iinQ_J7tA14qzwt3vXBwgy1RwtKHEk67s6kuLNj2dK9o5MLHfBeaxoK_0mYfit_lw49zsKvcjPudcFvDtnP4QvE0du6ohohuZUQrERWkFvOZeUWKS-0nUXk6HWsKAiSp39b86g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
✅
رونمایی‌رسمی پاری‌سن‌ژرمن از لوکاس‌دینیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/103191" target="_blank">📅 20:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103190">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJnbHt_gp9Mblj8ZFZd07S8ZR-5OQbQP0X90ZRoHc0Nw-A1J93Fswf4oW_xhOvIxZJefq_Mpuca84c4BEHIKGbszPG1w6YVeVC9WYpKH3DHo52fGh9gYDkns3yv74a6x_sJBN_z02IYCPOhuQ2ODTIu_x2cp3D3DNhjeN_itN-OVlj38F2V09CN2L5wfkk1GTe8x6bzcnh7MqP1Oa33tS-nhPGhdWOmWdvRAVVrUC5-7xApytzotz4Ws0cpZ58faBAqCxvp_fTqX_t45qWRUIjXruLnM6tTP9g4d5fQzy7P1akk7RdmFG7CwC0LXElcOPsNNvITkUOLjNUywLQgH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره لیونل‌مسی در مراسم خاکسپاری پدرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103190" target="_blank">📅 19:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103189">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=T6ZabDsBlrFnR1KdJ4XMVt_5R6q50SoN9jQNPUbr02vHaznrpDSfAZ2e17Z_KaV6fpxnuZiAtPcxMq6IAA_rlGyol7-UikphKo2SWucCC8r4ng8Np5WokrMBxzZygITgBnfJGgkZv6OgzDOvpkb1Nj8r9BZrXHMKUsH777v4nTs3L5U1Gfe3CnFvJ-oakF_PP0hZ5pvjFzu8u1WQr0SzLo9VbrSsUffNKAP1nF_RYalcGQT9oX4nMlYHSnmzB0C0vTeRXlTIWih7NOvjS3vbczXh8aL6TjNRzX31MMW8Xu8GjXR1V7_9CSdhEncP3oIYvCjrRbqHPbdi5-uwW-FmsYXP6zVA76UYq0zi3skjIoIAlSuBGQ0A701nQ-juYTIK1MEuA9cinKQp2Deio1fcTobIx2o1MaKopfojl4FVJ5jmHNyTNp1fdcpWvTFNFTFStQkwXq709VgfSxZIGfnGAjWpBzBxkjem7pfe29dziCeoFTXJ4Ia1C6QQZ_yfgTfeOcgoM0pxcblVtq-pFntEa6BFNlJNxr_RC5mVba3qN4xAnu8XgFHSlIyyxcy_WhPJpgw9-NngZQjbj54yXtJ26vpTfLqy88bEP3jHpTo2tGQLSzF451FSWBCSfygZXauoCdCHRQY4vlfzleMbnqyFnfxXrM207rFTGNlS4kK0LTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=T6ZabDsBlrFnR1KdJ4XMVt_5R6q50SoN9jQNPUbr02vHaznrpDSfAZ2e17Z_KaV6fpxnuZiAtPcxMq6IAA_rlGyol7-UikphKo2SWucCC8r4ng8Np5WokrMBxzZygITgBnfJGgkZv6OgzDOvpkb1Nj8r9BZrXHMKUsH777v4nTs3L5U1Gfe3CnFvJ-oakF_PP0hZ5pvjFzu8u1WQr0SzLo9VbrSsUffNKAP1nF_RYalcGQT9oX4nMlYHSnmzB0C0vTeRXlTIWih7NOvjS3vbczXh8aL6TjNRzX31MMW8Xu8GjXR1V7_9CSdhEncP3oIYvCjrRbqHPbdi5-uwW-FmsYXP6zVA76UYq0zi3skjIoIAlSuBGQ0A701nQ-juYTIK1MEuA9cinKQp2Deio1fcTobIx2o1MaKopfojl4FVJ5jmHNyTNp1fdcpWvTFNFTFStQkwXq709VgfSxZIGfnGAjWpBzBxkjem7pfe29dziCeoFTXJ4Ia1C6QQZ_yfgTfeOcgoM0pxcblVtq-pFntEa6BFNlJNxr_RC5mVba3qN4xAnu8XgFHSlIyyxcy_WhPJpgw9-NngZQjbj54yXtJ26vpTfLqy88bEP3jHpTo2tGQLSzF451FSWBCSfygZXauoCdCHRQY4vlfzleMbnqyFnfxXrM207rFTGNlS4kK0LTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
حمله‌بیشرمانه مجری صداوسیما به علی‌دایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103189" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103188">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFcQZhplobxvvPBEmMA8NtNaZdg1gBG-cRTrRMq1JC72HPoZV-quiZ2v0d_wJMgeBg2Tk9dEtIJWMprRu4rm-5ubrUaG040qE-KfYwjdQdMYI8sE0fQgRpW6ajIiT1HOFg0JN4u4drTXRnxyjwuV8pK23JNs5zQ4x0BMKPXyePE51Tf5FWruvxpahzEHraQ71aqUCEI7zPGHNVKQBsO0yNiV3Fhp5hX8qjIrZWq5seZpaVXmOE8XBrt9M-nCOMbTPKL8fAxkbGSOLZz2G2TrDz9xul6ynVltPIxytTc4Ryexbo9TdIQ7z83PYLuwb8Tr2HoDGRcqV_kLIs-ZwMNVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی، منتخب کرج را با نتیجه پرگل ۱۱ بر صفر شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103188" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103187">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiPXDTCBrGfVnQEjIOXs8OpbWwpoOpth2TijGKXvVCJh9dkOzP21O6SXQI_Q7pUcJuy7pMF9io5JTAKmxbLP0kP0c5dR_jzGP1lgCxTIIQSMvZKMSVVpFMuJRhMgeAchBA0RGzzSjDSuZaRFZ6_Kxk3a495ip1IwrwrwkgPqL37Gw6aGXppqmQp1CedbvpnxLCPxL23AXoBJ7U61NQwCcRizFw5QkyCx1sRgWiAJtDy0F3FTe4Gv48bLDUre3ekGwjaYJ75TIKorfs6Lo96PitNHAUNkMlSabCW7-1aK0NP7ISEOkNI22IEFsgnDr5jDTgfNld-7Vav9wA8qdokMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🎙
انزو مارسکا: رودری؟ فعلاً او روز چهارشنبه در منچستر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103187" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103186">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103186" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103185">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ovMbFwDuLwqZSARa-fIvumr1PnU9_DXvPhxSd7RSzutp0Q2NU-6_wMtQd_LsUfFZZz1u3G71OfSj7urY50R5QqgJ1ltXliy5EREjqnBPcOQuvzdLTMLOUxIRFCQW1kGJ98-vkkCgSBRLKkLFXbTkt7PHqurZPl-LmoLwTkeh8teNJ9NMfH5_L9XSDMvuNXk_uCPbudF9UnnoX-5Onflvib85PhvAmw6bDyqVYirvdP-aBa17VsgQriAtunvAmWJ9J3531o91QNHBD5pCaX54Mtc7WkgtzV76vxEgaViE4ZL925_0H7QgYAPDTVoi8NR0gq9HzeMGA8s7Vb__zF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103185" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103184">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=TxjmayINaHTdDrJuuzJkrDSXku8lJRV2uSGflYj15laKroCsmnoP0_-9O1lH4EgLzlROWBKGBQlhCtxo4ZSI78HDhYPhoPNkl-a6QzSvEv_yDOq1vMO2E9yd7h-srAArMTBbqNYJvhPHhw5LMRr9T-4UJsFj7NDKzmqLzY1oMflkSv_DmOQdYKFkjUhsrpeBBr6ATbuArS_IZ3UIQFktv6KYMhmimgXtG3agEZSJIT53OfeuRXMU_BXp_7WvsIosGYeB3bH5ghMto2gyOBoKRfHKxmdgI0qjHHz9sbCAOOHbK8azD1ZV3HisDIzfnAOrgZvGlU6v-scJO_xT7JbdobrjZqH7oVOjm7tdREGuHeekAwFW7bNnG5F6O1ptum83GZJEnlIjzKLRN9ziAPCDr1Wm5gXhyHH1cU4Zle5Z948IC_Ngsfd25iFlu_BQiu2kRbrGYlBYlmvkKuaRYMShCSUIGDbI1oXyXH7wq2gcsHB-IGlW65F3omZiasewyxuQr39hnmqVI2ZuQvutxNsy8RmGFQw1uJ1RjRknyuugTir1ooifdaOtXDCFn44vhK_uW4LMXuWGUTAqm7W_pg1wbN9jPtDlAQpi6L2n10EQ2iaIFWdyxjmf8Monur7QrbAReJBxiBm4q-IjvGaeYc_JUJMLEQD7w8L8SDwbbLZlNUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=TxjmayINaHTdDrJuuzJkrDSXku8lJRV2uSGflYj15laKroCsmnoP0_-9O1lH4EgLzlROWBKGBQlhCtxo4ZSI78HDhYPhoPNkl-a6QzSvEv_yDOq1vMO2E9yd7h-srAArMTBbqNYJvhPHhw5LMRr9T-4UJsFj7NDKzmqLzY1oMflkSv_DmOQdYKFkjUhsrpeBBr6ATbuArS_IZ3UIQFktv6KYMhmimgXtG3agEZSJIT53OfeuRXMU_BXp_7WvsIosGYeB3bH5ghMto2gyOBoKRfHKxmdgI0qjHHz9sbCAOOHbK8azD1ZV3HisDIzfnAOrgZvGlU6v-scJO_xT7JbdobrjZqH7oVOjm7tdREGuHeekAwFW7bNnG5F6O1ptum83GZJEnlIjzKLRN9ziAPCDr1Wm5gXhyHH1cU4Zle5Z948IC_Ngsfd25iFlu_BQiu2kRbrGYlBYlmvkKuaRYMShCSUIGDbI1oXyXH7wq2gcsHB-IGlW65F3omZiasewyxuQr39hnmqVI2ZuQvutxNsy8RmGFQw1uJ1RjRknyuugTir1ooifdaOtXDCFn44vhK_uW4LMXuWGUTAqm7W_pg1wbN9jPtDlAQpi6L2n10EQ2iaIFWdyxjmf8Monur7QrbAReJBxiBm4q-IjvGaeYc_JUJMLEQD7w8L8SDwbbLZlNUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
مراسم ترحیم پدر مسی اگه تو ایران بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103184" target="_blank">📅 19:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103183">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=mDFOQ7DWsQXQgUxVwe1fsA_FPQyAj8Ig90DRY_RNahuZdCYdzROPsG-e-67fDqWsXWogpfzeUQ50fFgwnGR5lN96QlEW45rqgv0TmqvXDcuZkdddMD_23MlwjYiM7vGrxtuWKrhgizLFFAGZuwZcK6xe1cnP4vqybync5o62J24rbg1H8QuElKztKFrKN8P4lVVhap2mkJgOgBj3ESPGh_01Y-uPPClxDIxNaHuC5Ps2N8L8ZwA3eJdzalABbP5zYVKei7qFYucuZNrglKNqufminkqo_Mp7KRtcKEVK5nc0MQ8dUCWHMqAvRIhp-wHpLCat4GiStTnU70q9-09k1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=mDFOQ7DWsQXQgUxVwe1fsA_FPQyAj8Ig90DRY_RNahuZdCYdzROPsG-e-67fDqWsXWogpfzeUQ50fFgwnGR5lN96QlEW45rqgv0TmqvXDcuZkdddMD_23MlwjYiM7vGrxtuWKrhgizLFFAGZuwZcK6xe1cnP4vqybync5o62J24rbg1H8QuElKztKFrKN8P4lVVhap2mkJgOgBj3ESPGh_01Y-uPPClxDIxNaHuC5Ps2N8L8ZwA3eJdzalABbP5zYVKei7qFYucuZNrglKNqufminkqo_Mp7KRtcKEVK5nc0MQ8dUCWHMqAvRIhp-wHpLCat4GiStTnU70q9-09k1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کارا چیه مرد حسابی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103183" target="_blank">📅 18:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103182">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
هایلایت بازی آرسنال 2-3 دورتمند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103182" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103181">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=ujsTcwZ7oQ59HfSEaqc6IKCmTIbxeIwwZec9oOrt2lVGOSTndgfK_0rcqC908ARukS5ncvXEDwqUloIfmanf-_46yxwRa03bh07ZI3B-hnnLo1E5pJycRYAxYaCH4hcUfxouNIduL9z0tvlzu22j0cdTqxJVbxSLLCXTdJf_1mCfDfNlVa6kPShegYe4P5Cdg3eUNsSo8Ggv5M4z1P2JJUK4cXSlozlsIERGMaBw1BbLzS-Qt_xVRo3S8PKvFiOad5ZpNs9uu1xRJG8Gv0Jxlq7v0Wys5_hmn5mae8pDMvTO__9OMb-DpaqywGu8QQLMYBhf3X4eEEUvzQg8lnhBow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=ujsTcwZ7oQ59HfSEaqc6IKCmTIbxeIwwZec9oOrt2lVGOSTndgfK_0rcqC908ARukS5ncvXEDwqUloIfmanf-_46yxwRa03bh07ZI3B-hnnLo1E5pJycRYAxYaCH4hcUfxouNIduL9z0tvlzu22j0cdTqxJVbxSLLCXTdJf_1mCfDfNlVa6kPShegYe4P5Cdg3eUNsSo8Ggv5M4z1P2JJUK4cXSlozlsIERGMaBw1BbLzS-Qt_xVRo3S8PKvFiOad5ZpNs9uu1xRJG8Gv0Jxlq7v0Wys5_hmn5mae8pDMvTO__9OMb-DpaqywGu8QQLMYBhf3X4eEEUvzQg8lnhBow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلبم گرفت حقیقتا
💘
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103181" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103180">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAx74HTPwcJl-3yH6CcZCuWydHlQDM7JK5bJjJ-nsdMxTD-h8bsYomsk4RxS9_JSZBaz8JE84ZGyYlqeifmoR9U-lWMBkzuoKAP4nhJdtZOK4RIFC08iYXbC8Ys3UimVPT1aUDyjM8f5CHoHmi1a1hY1ONRmeSekKr2w2k5pa9ePwhNCM7Qs770gA6E_C39SdYnBl9Edq92zg3WSIJ-aF6-ud92eVFVsp_LzNl4hjZd8FQ2csoyP96WR9rqSQjBSQGj3JAb7_QBR6iCozFGfucPpaVa9RMzt8qrc5ZOHdOxJ9PfApt6jiQ0I8UuTHstouqDMs3DLiNKh4iujXSLR9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🇪🇸
فابریزیو رومانو: پاری سن ژرمن زنگ زده بارسا و گفته با بازیکن تون به توافق رسیدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103180" target="_blank">📅 18:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103179">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=B9iMcPinbejwkcttJPv7SFqOUxjlwl9CRUl-FWwUmeYtJDN_-XMJVN3uoSJkDaPzhWA6pOHvvFrhiXOsCveB2YXaVn8KMahOLo8Gggl8JUgcBJlp8CtpaPMfonNwiJRtZOt8iua4ANVljdlq5iS_cf2N41hvRjrht8JCoAVIzmab7zGjhhSbLzfC9IWqn0bNCkfZ2eK32i1WHsbZl2OFm13BZjZQgklAghJISPK0COfhWcpNCbgbkpKUAXD_oKgr2x6GeTZy05zX7E7hFOuwCv7m5JZA5l0r6GPwfME1XpKVSVxoq3b4LPgj42hlRME30RbJjIZJTSLGuoNy50Mzig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=B9iMcPinbejwkcttJPv7SFqOUxjlwl9CRUl-FWwUmeYtJDN_-XMJVN3uoSJkDaPzhWA6pOHvvFrhiXOsCveB2YXaVn8KMahOLo8Gggl8JUgcBJlp8CtpaPMfonNwiJRtZOt8iua4ANVljdlq5iS_cf2N41hvRjrht8JCoAVIzmab7zGjhhSbLzfC9IWqn0bNCkfZ2eK32i1WHsbZl2OFm13BZjZQgklAghJISPK0COfhWcpNCbgbkpKUAXD_oKgr2x6GeTZy05zX7E7hFOuwCv7m5JZA5l0r6GPwfME1XpKVSVxoq3b4LPgj42hlRME30RbJjIZJTSLGuoNy50Mzig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ساندرو تونالی هنوز فصل شروع نشده حواشی خودشو آغاز کرده و تو بازی دیروز تاتنهام وسط بازی با بازیکن حریف به شکل عجیبی درگیر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103179" target="_blank">📅 18:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103177">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuiEMbwUFY34eHdqbE-IQgAy3kIqgqu74ZZB2wsZRXxP0-WPBZANu6x9hLzGlajbYd60uwUDXRtdI2wszDf2bb8KhCFK0Ztfj-xArtRQ8fWJL3os_V9qn_xVMeb0Feto7PH6x1P1yu4ydJhYwOJXYBJRpqO_AEMmlyojdIrAB5QkoIpaLkCP9BHMSHCF-GXnTpt0odb7wOXVWIim-QoSWErZhTXkaPbn_hXkatD0SgZw9swI6ULoDwOs0RoSvkS1V78mIB8a3QQMClkqy3LzEC2MGKDKT-iJlhHBxlmnqg5H1IwhYdDBPJioRm2RBxCS9GR6DIe9jDIpEP0UV1q9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC0x5rT54DEN-D4gevkT-BuBM7UxRhuArJQqmJKzmXtcKy8QXRtcoQ-X_ILAGxDATAPEX5P-Z7WozCOVz5bCrOrOpe_aPV67KYJaVyKk8A881YI1TeMqeSnFdq_vcgJeBwqktqerwXwDorqkSadBCCiGYrRgN_c5GR5SkBfxrIvJoCGP1iuf2KGfQfV9JrrNNPVS0ZNqHVTismMwSW_ImKQ2DRbgaAmRo6Pk-jDZP5AYyL6NQ7kttY8JbwmCe0VIuY_o8FVTlrz4nCQQ7BdJAg-F73CdTDX4WCfkJIFT4Dul8VbGGd1RgNHcxhH43iVS9WhGxFxEMBgOGlBXpGosdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔴
رونمایی از برونو گیمارش پیش از بازی آرسنال و دورتموند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103177" target="_blank">📅 17:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103176">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyvU6GuStavzjZlqNlT8LCxAPpKuk5eTWmWP7Nt6P6fmewbPYqxNUklURhc_f-vJVsDvXdYGek-G-pvmMgXLfX8yEnFLnO7liHiKIgiJQ9UJolzP6eKRuOhU2dZVJrdvWJv69AzzoawlqWOI0RLASLjVjleP75DhhANNMld7WcEeAwKXy5RCp5bT09E29PViYnnOjrBQyAUevO6fLu0CStcE7cOOU20lbcTVgJ_Viwidy8nCz4jhyAMSqxQ2KVZzWoSAgTFEwMVOdLkrTBkYClUDMI6ZNHKQZlouIqhYHGZ6uBMzevFvVwMnpb-sIN7qrQfadye1h9A8-BjLC-U4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
چلسی مقابل دارالتعظیم با پنالتی مساوی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103176" target="_blank">📅 17:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103175">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=HBzNAFGBqxyqyrTTokZb0DKR7Y030rDHiSOsnjXdolseLN_0-OpzSUT-3_S_11G2xmrf1-YHF9BskBvnmQ8KeZNVVuALuSp8nBj_LC5xpXOqsY0NHmHJ_Tb2VaHUWzhPdiKcleHIse-PkDNWiU-lwjMYhGp6epI6v4Hg9pwJpjDiFtf_G1VVUtuY6Dtb7eDl3aAZ-QiiEs-F-m0EsFsxaF8Jx-NdjVB3PzKWqiCQRU4H0V4QhggZG2sQbQh-JfgQESm-0BgMQL2acfiu_4XwqB4-A0XnaQAAptJzipzFRj9api1PgeWEcBgQHyD0kncSQhcZrZi_Grj2-4bfqj_B9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=HBzNAFGBqxyqyrTTokZb0DKR7Y030rDHiSOsnjXdolseLN_0-OpzSUT-3_S_11G2xmrf1-YHF9BskBvnmQ8KeZNVVuALuSp8nBj_LC5xpXOqsY0NHmHJ_Tb2VaHUWzhPdiKcleHIse-PkDNWiU-lwjMYhGp6epI6v4Hg9pwJpjDiFtf_G1VVUtuY6Dtb7eDl3aAZ-QiiEs-F-m0EsFsxaF8Jx-NdjVB3PzKWqiCQRU4H0V4QhggZG2sQbQh-JfgQESm-0BgMQL2acfiu_4XwqB4-A0XnaQAAptJzipzFRj9api1PgeWEcBgQHyD0kncSQhcZrZi_Grj2-4bfqj_B9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
😢
وسط مراسم معارفه نکونام برق تبریز رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103175" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKRbatB-o2F-01y1DBmc9iyBhhovw8hh13qW3GFjPdNEiGlnjEeSPzkUrn1zXLnkWSvfUNo0I2-Hmr4M6dqq2o_mGiQHathDC0M5TdEUIIKa9BJBHAdrf9rTg90naM7_T9R4sN9WN3TkExrS9AmJwgDPDqi_1CeRQwVSoSrJbvtejyppME2JyoLeN3PwNxN6ZXaRqg3ToJKEpmEqzXlQtz3X76x-kaDvg8OeixnBHhAA5xFXQ46nVGcb7ef9T5B1-z4yNH4Gc5MrIlpNYAsD2sI3-shMmPJOK5pRAcYDk9Mo6WF17EmAUPNszegQ5rXdhYWriPgWGacxsezf2SgtDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه دومینگوئز بازیکن 16 ساله اتلتیکو تو بازی دوستانه به سیتی گل زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103173" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#نوستالژی
؛چالش‌دیدنی‌پسرمارسلو مدافع سابق رئال مادرید در رختکن کهکشانی‌ها و ادامه داستان...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103172" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjHqXBDlf-9KkykGigTTVCGot1ZMEkLelYeFvd2gRQ6nhGP-L6cVOB5K8KPlwyBdZ3BolqJGFEDrudAJuRdv6Uk0L4uorC5eHFpk6tfrKZZQ8HoimSyKyXb-3y9St1i6XrOHz5tMhGtFgNS3iOHt1LH8jq4nVsMFMOjdzy90QBPLdWQk4Nh5GOzGy0KJPcEPTiqkqbdEY0w3FHfEzfIiv_xJH-ZTvaqLSMTz-wB_M2frz7CiImqFqzfg1VLg5qetwrz61RWkXIloVBXJUbLxHVYtF9R2L_RAAtT-TlljECJ3s1OF23LqTs1tjpwwz_rQwQiXkzjky-FGRkD352T2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
8 سال پیش در چنین روزی، تیبو کورتوا با قراردادی 6 ساله به مبلغ 40 میلیون یورو به رئال مادرید پیوست.
🎙
تیبو کورتوا: تا هرموقع رئال مادرید منو بخواد میمونم و قراردادمو تمدید میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103171" target="_blank">📅 16:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=glQDDZvpMcq2cKrwAnt5xEopeq7gzrPCBz9P6CPgQqBFpPKWzjN4Zt6rHJel6GhGS-rjNzqnIGH2D4MZb4T_GAQUmy20t8tKw7Yosv3U0viqwSyeiauBCl6gEb3gTA-1vGZUdA0ZLpmazs_E97Opdd-ZZNXx4jc4Op4qFcU6C9mGtD8X4FAvKdEvjzccvCjKUHJ4y5aT6t_sZMfN-dlyfWgMix1PmGqG5Vta31aahikr1a_I4H5CbyWw-_Ms0LFLk5Kj2ZxkyGZIMiBR2g5v3WIRYCXJDxeA-PnQi75BzU_wN1WP-V9L030kwwgJBUsJq4S8C8FEpjGfNC47c1DLBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=glQDDZvpMcq2cKrwAnt5xEopeq7gzrPCBz9P6CPgQqBFpPKWzjN4Zt6rHJel6GhGS-rjNzqnIGH2D4MZb4T_GAQUmy20t8tKw7Yosv3U0viqwSyeiauBCl6gEb3gTA-1vGZUdA0ZLpmazs_E97Opdd-ZZNXx4jc4Op4qFcU6C9mGtD8X4FAvKdEvjzccvCjKUHJ4y5aT6t_sZMfN-dlyfWgMix1PmGqG5Vta31aahikr1a_I4H5CbyWw-_Ms0LFLk5Kj2ZxkyGZIMiBR2g5v3WIRYCXJDxeA-PnQi75BzU_wN1WP-V9L030kwwgJBUsJq4S8C8FEpjGfNC47c1DLBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلای تاریخی کیانوش رستمی در المپیک ریو
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103170" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103168">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwWKkspHYUMlp7R5oqK6nYz-wEKkXO5ZTWt04Inb2Qfm5NRG8nJBK6cSTXF8q0KoLiLui7-YsA-m_79vxYumZjlVTTPKV0JH1xkRGy3rB0JeT7QWSiv_GbPtmtK-NZRdeGwWM-ibBr2R8g1gLWKlXhw60FF713Zy7-zNkDwIrrR7VJX-K5gk25FfNW5WVLWsbCbRTIJju29NAm4CzAAxJlw_e0Og2HnbWJYCmU6AWwRUT2po5EujAAcq07Qs6GIplq6ezCehZaZhD6lhA9seXp37O7JA3s7-oVKMAe_RpJKSyBS64VIJ2Hw8yXE3039TCkd4-eSsDvHguq1rX2NtBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NN3QANWX6Y4IZspuGMIg1Cqw2s6-swU0iiWnerdC1cX_gVfBFMaRb6-nNLmAEUo4ZICtdeIO-lSs0C1VIUO-xw0PyosihrsM8gwgZPyMy7k9v1EzaaT4Hn468D80Tp5YtXr78jLzTSZyf9Fp7pNlB1KpldqXqP9Zi3yTmrf8E7qbu9GG-0XHW1n4hcYWskVrCNTldWcjG55u4SlGEuA3j_T7WO2dO4zM0Z1p8ttQMNXQJw7VSkT193bRL37e9TCmU5OqqNCC1_VQiA9xZRezpqLobcvOu6_N-h--e9SogBWvS399c2jhlENIb5eNT1iIPjC2cs5QR0DzlFmHk3ApdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103168" target="_blank">📅 16:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103167">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=A_9JbV0lr0WPnVUpEBBFxN_ur0EUEFXYq1N_FCG8wa-GNJpP8WNPO4hSZmBHyuX1WDKFcxjHeYs6yXqxQOLvx_j_rvdhXl4z1b2jcsMF3gC_syUfnO-DOxxsBRw2fWgadRL9F3Q07UECRov7oBGg9ZmUpvvZ2qm1VXlXehyYKiBr0B_Q25ktu1Tr7930wycBmYK7ROdrLl4G3tLz2hfvdXpJA_gmQPrOF8ciXh29LmzdpP-oD4boJrzy1syfhD5jZ_p-ws7l11RUhKIgNWKQQMTi2SdFmmYSPgRQHOKVwhVa-E0AOLfaZlAnIykmJrh5NTPJhz4Gt4CYxRmardMV5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=A_9JbV0lr0WPnVUpEBBFxN_ur0EUEFXYq1N_FCG8wa-GNJpP8WNPO4hSZmBHyuX1WDKFcxjHeYs6yXqxQOLvx_j_rvdhXl4z1b2jcsMF3gC_syUfnO-DOxxsBRw2fWgadRL9F3Q07UECRov7oBGg9ZmUpvvZ2qm1VXlXehyYKiBr0B_Q25ktu1Tr7930wycBmYK7ROdrLl4G3tLz2hfvdXpJA_gmQPrOF8ciXh29LmzdpP-oD4boJrzy1syfhD5jZ_p-ws7l11RUhKIgNWKQQMTi2SdFmmYSPgRQHOKVwhVa-E0AOLfaZlAnIykmJrh5NTPJhz4Gt4CYxRmardMV5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کین اسطوره یونایتد: اینکه‌دنبال بازیکنی بدوی تا بخوای پیرهنت رو باهاش عوض کنی کار خوبی نیست. تا حالا نه دنبال کسی رفتم که باهاش پیرهن عوض کنم و نه از کسی درخواست عکس داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103167" target="_blank">📅 16:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103166">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXys3mWzH5nvhPPs9iYUiC6DhLZ3mvspd3PogvbupjfhU2sA4NxNAU9Ddh63g7CtInBOYcW54PtIyG0WJn7AkHUfAzgBX-eSg7enbM3GIMCg7LVJdlly8uJ_euKLO9MMb9BZQgEavqzkEAGJRib4-q3ePAYzFOUHWOc71DbKpzzYnsSWe5hW1PI0_gkBbwrpfRDmP8fo0pfMQqB-OGQSI31I4VVE98lq7QvC1v9iMFGvH64iZ5I060gCqYbjic1majWPPay03m_S56-mUrcLR-b7f0FpwCfoWeCkRRt4ZhvvvJnDnE2OQxITM0wfmJzhEPYDq4BkD5-PaPuEF5sagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چلسی از دارالتعظیم مالزی گل خورده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103166" target="_blank">📅 16:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103165">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5F4M3NX816YsdtHJz-G4mSRVJa4n1Vt1IA1l_hKS_T3eXle7rJsdMu9x1nFA8FHv5bcILfDRUbvhFEqgnONyNdoRhnyf8_f83FwHvA0NIuRizDNmo-o1O_YEBfs8YavvdE5jLnGAQcWBVtUYrE4wErCH8t_vFof03ZB828PShdarNIwLzShFyMqPrLoNlIMqOtNh_zaJNeTMKIsJBtl5Yi0Hy4y5ZY-JfKbepRLLfR2oo0-zO6Oarvlrkbu5CcEuzRjXhcOWkLre1-6OT6hrqYLaunFvbBI7c98orAc1WB4YfTx1KvLQLDDvcnuzOC35XCmk4uPMsqbop914JhonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عمق‌اسکواد تیم‌آرسنال در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103165" target="_blank">📅 15:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103164">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=k-BlPddl_RNs6Kf59G94MRAxgneh7NU35ipgMJTuZ8SjAsu45D67FsQSuCWnwRTh-8-u58zLUMYC27vKUR5BmcMQ70w_D9do6CqNodKrrUHBgnG3i3EC1GNieoLdonB0DjvjeMzkMENxcyTBbQEmWGEP37rePgLzrJS6Tv-KcHGFzduMyadH7mlAVX5yON7XJkNxZ2d4Q6Z0kmM7ccyK--803tUu8Rael7vaE0wkz093HdBVZqV5T937X0QXRoM8tlitGWNLurVRz2sJT5kb7cIMEVggkMY2ovVBNnLRnqOt8h3zNR7P2AyzGJgRlMQVthnKxhjeL3GzOqT_JH98MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=k-BlPddl_RNs6Kf59G94MRAxgneh7NU35ipgMJTuZ8SjAsu45D67FsQSuCWnwRTh-8-u58zLUMYC27vKUR5BmcMQ70w_D9do6CqNodKrrUHBgnG3i3EC1GNieoLdonB0DjvjeMzkMENxcyTBbQEmWGEP37rePgLzrJS6Tv-KcHGFzduMyadH7mlAVX5yON7XJkNxZ2d4Q6Z0kmM7ccyK--803tUu8Rael7vaE0wkz093HdBVZqV5T937X0QXRoM8tlitGWNLurVRz2sJT5kb7cIMEVggkMY2ovVBNnLRnqOt8h3zNR7P2AyzGJgRlMQVthnKxhjeL3GzOqT_JH98MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
کابوس شب و روز بارساییا در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103164" target="_blank">📅 15:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103163">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmRDtYPowlbrdvoGimkTm99fK88Cf5JTM--XbVhg7TdleMm_l0j0lN1Ej3WXMWHVRgD_60QxsellOENCvH8Iv4X1wfmNrrwfLWuZW5Z1sJ0JRrZB8SAxzo0m-6irumEYjMAZOLWLVlhVPu_VJAHl89dzLBTogOxYOBaDSvFwJrklekCK0nbz4XVGV1aENckTs3TBdyIHoOmGN-dcEXu2_XiY2FH_u7X4FsIi0-hg_Q05a0VFKD2wN6XJj6756_ycWTgyYm8f0cAI2a2lbcGOQ10Y_pYmK_qMjtCVSIPRD9Ox8OQ-LaRlpBqNhVcUbs_ABDfLk5hKTEqfqPAPVRaTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آرائوخو وارد انگلیس شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103163" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103162">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVYxjH-gejZ3pd4WaEb3VRtQG3Fg0UN9riU4mbCNuwPL_gEVfH4Cwq23DwnkQt_6YaSrRClqjjFjlSzzo8wJR8Sfr-zf86IOcLBzXoFNTRTEPFVY9EmQyNID8gJUqgDCtOE3pBPtIl739uLRCA4JbhEDNm8BEedUy8KPlw1GjOVmGrbj3goOfEHvCSShUsGuc5AsS2z0ZYlq2nYCQg7TeU0kX4MCXZxN5-E8HcYilK0vIlgrfidGUTW8B0_b-QcmmVQ9kYrmFLwmZnjrNMLgRkTCfcXcL1cy2OrlzL-SajmlZf5QUSKpC719OPEtFmRyrcwZi_XbP9AcQjIjnXu6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
هایجک‌های تاریخی بارسلونا از رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103162" target="_blank">📅 14:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103161">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=BRaAyuYnH2NsAAqwG34b_WX2YJtk8X7CCJkJ4ZI6UUMQhXuyIg7ocnEQakQcM1-mrw9_0o2aE34FjFqAwmGSB_W-x1jf7TWCNDGmt5A9GIUpXpzmZLQ42IFfqD-UzZDiR231uVU4-LMgINMzwDZFhHEtRAEam7Ymk62E0thmsx9Ep_eC0CxOCDLYi2T9L4XH_3WrPCNYrC-SnLf7RFH22oLOUodzGFwyDpG1vuJs4vZWlQhbwThRGV_uj983ohQz3mYZZMdYM87hCRZlqgqQZUpMUEyhSEskv1bSLwwHjB3XQQPRk3vyu487HliLFSHP4dj4nnT2fxobyYmYAZWfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=BRaAyuYnH2NsAAqwG34b_WX2YJtk8X7CCJkJ4ZI6UUMQhXuyIg7ocnEQakQcM1-mrw9_0o2aE34FjFqAwmGSB_W-x1jf7TWCNDGmt5A9GIUpXpzmZLQ42IFfqD-UzZDiR231uVU4-LMgINMzwDZFhHEtRAEam7Ymk62E0thmsx9Ep_eC0CxOCDLYi2T9L4XH_3WrPCNYrC-SnLf7RFH22oLOUodzGFwyDpG1vuJs4vZWlQhbwThRGV_uj983ohQz3mYZZMdYM87hCRZlqgqQZUpMUEyhSEskv1bSLwwHjB3XQQPRk3vyu487HliLFSHP4dj4nnT2fxobyYmYAZWfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
یه ویدیو کاربردی برای دوستانی که حین رانندگی قصد دارن ویدیو بگیرن و همزمان موزیک گوش بدن؛ بفرستید برای دوستان ماشین‌سوارتون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103161" target="_blank">📅 14:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_kfdgXQx-WE6JSRWB7RlXHWSu1NeCj2K52rq7U7qWLhz76lsGFX1c71zXDUdqSkZ3sYXu3LTHIlWYExt3rlazfc0s4DSTYdfGwQa9tv1igssYMJVuOGWWU7Ghi_qQFGs0YzioSOdt__VTCNE7htVTZ8xi87bs3pJUIKjD35DHLS05Yqbesw7lyds0DomYvZ8Tw3AIsURpHIGeqJR8qMOsziSKlzap-co-X9x9T4rz1NwV_HGiMOt5_mNFvmuuJHnxZ23SAd75LWwKJDLuo7wIHt399iPF5iHU_7pKq73q0BP_BFI6ZzuPw-vMFS8dOuxLcyXURJg-H02inVCx6B6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TuYxYB757tUjG0Xmy6G3cbGaNeWL76En0z_dcJtL_Zxlq96gSQtDsqYy9ArZ4PKn4Ygk0-gPqKBb-hwtFCizB794C_KrdzINzGaIXHs7E2fSOXDTYbpx5jD0sZ2HM6eaYVr5UEWwZkb7hZntLE54d844_C7b44mN7lFRsBeqHA07rxvaosWD8cgYKzwsePv50L9aKD_O5RHZUN1ujFqq05VHGM_KcnfWVb0lhUEgaxmBrHU8FczAvM77kTo_9iA2dxbFNXeGYvZVNAUbwvzPzSYydSQKfprTh-P-gIIAZw59_GR_IaYF_zl4VgTDyR7yJvp415jvp6yJ-j3etH6jmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
ترکیب منچستر سیتی
🆚
اتلتیکو مادرید در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103159" target="_blank">📅 14:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=PRvpw68tGZ0IIKJrwwf_qyd5TEmIyrXlnUxeak7Yc2utcp9I6-Kl1FtQSiDJ8mUKPOCIpy6BgZHjcRr6Eeg0VmyIjdaBOGlXAGEdfTBk3txW72jF-FcqwnOeJDWkx8wp4mbtzmPmUVpl2Tbzz3xevgdySQZSWnBd8z3sLXUiuKLU0Yll68OopTjRCdhcA8MIkmM1VoxTPpzmyQyxaroZRoEFmoPQoiA9Q4Z05yFx56_ys4Yw8ebMbTHw_b3w11sXWQaB9z5ZQSMkq8oOhlW7pHDCOdgAwNm2nDpmQMMZCQ8MWeF5K6zvBpBw8pmE3dLu8O46aXQ4flUcIB_CFn1gLnG-Imj22JPuEzbs7pbt6xvcXnh0FKPINVVRvv6QJN6sf1XX4QJygpWTV16ywaECNmhR2vspeGsA6Swh5mmTb5S_ezgeOmAs98lQ7wX2c87EnoeDHirf_35GWGScqnUrJCszB4vOsrp4pYaWobX4xWLmu22kdQkVAP5VD3h8Lo7W7ZRGabFVNcql8k2WdDP_GNAFawYpGKh-i1mhkeGxmYLScQBU-7H2HYdThinNpqbfm4EzbhnUvbVdNOJlcbvFjbaVBjn-PxPizWhgIJa194e5CuFt6txvij3yfnLb7dpM-LkFDEu035jxg8ni0V5wvYqsOWq0RDL4SJ8ICWvY-ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=PRvpw68tGZ0IIKJrwwf_qyd5TEmIyrXlnUxeak7Yc2utcp9I6-Kl1FtQSiDJ8mUKPOCIpy6BgZHjcRr6Eeg0VmyIjdaBOGlXAGEdfTBk3txW72jF-FcqwnOeJDWkx8wp4mbtzmPmUVpl2Tbzz3xevgdySQZSWnBd8z3sLXUiuKLU0Yll68OopTjRCdhcA8MIkmM1VoxTPpzmyQyxaroZRoEFmoPQoiA9Q4Z05yFx56_ys4Yw8ebMbTHw_b3w11sXWQaB9z5ZQSMkq8oOhlW7pHDCOdgAwNm2nDpmQMMZCQ8MWeF5K6zvBpBw8pmE3dLu8O46aXQ4flUcIB_CFn1gLnG-Imj22JPuEzbs7pbt6xvcXnh0FKPINVVRvv6QJN6sf1XX4QJygpWTV16ywaECNmhR2vspeGsA6Swh5mmTb5S_ezgeOmAs98lQ7wX2c87EnoeDHirf_35GWGScqnUrJCszB4vOsrp4pYaWobX4xWLmu22kdQkVAP5VD3h8Lo7W7ZRGabFVNcql8k2WdDP_GNAFawYpGKh-i1mhkeGxmYLScQBU-7H2HYdThinNpqbfm4EzbhnUvbVdNOJlcbvFjbaVBjn-PxPizWhgIJa194e5CuFt6txvij3yfnLb7dpM-LkFDEu035jxg8ni0V5wvYqsOWq0RDL4SJ8ICWvY-ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
⁉️
بهترین گل‌تاریخ فوتبال از نگاه امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103158" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103157">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4Oc_QBE2FXwHFvlvGPr0car8l-hLoL05yf6yY8DAHI9gq4RTNWLSOPhK8tOrt1Rh4jIvxyhpCqUJBiBhewP9rJlS5B-g5SudbMMknMnZhnAa4lx8RhDJiLcQVl512NIyy8YEhgQ0bRnOThU85JXWJVZcgGtDTXjb7M8pHHhYsCrPngNY-VAYXlZfdubFJky7CObc9CEVh2qUCiocbyzkX2-ozAXjA67PFGSiRnlF7onS_XM7_zFCbtuFX06KjdsksoQ6L9ZkVzBI6XiDrl9GdrphFRCULvHLgxBdozF3VDYk8Ju_84Aj5ozhJ0Nw7f47Y_0eSy_BfE6kpizG0LKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گستون ایدول (خبرنگار آرژانتینی) :
✅
علاقه بارسلونا به جولیان آلوارز همچنان ادامه داره.
❌
آلوارز تمایلی به ادامه حضور در اتلتیکو نداره و احتمالاً دوشنبه با سیمیونه صحبت خواهد کرد.
💸
بارسلونا آماده‌ست تا پیشنهاد خودش رو تا ۱۲۰ میلیون یورو بالا ببره.
⚠️
هنوز معتقدم شانس خوبی وجود داره که او در بارسلونا بازی کنه
📌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103157" target="_blank">📅 13:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103156">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=FRXjMbip07RcRlEOdPp4fRZecOLXYuqpM7gvI5nv6ETvIlvcKQVQZoWzYkvVntaCWCjgs4rRcIxg4WzF3o7xLyqdOxaMshL2AlMVKwhKuRpWvl_Iu-faxlBfQ358lh9cXjDGTUVwMtaJ8mTI4WqhaurSsM7csMeSABmtZtSXnW-ozVufmm6zF_NufJY5bqm509Jgi0ur1K_p7saTUjPq6u5fPdC2sIe1shd2IwLWQyzrIHG5_-j35n_FjWo9kN4RNC8i2ZB5vYMUF2shAPksVf-EtIlCf_lZaWWTatc_3iloW2Ur4_ssOwdZ4qEvodE6gxHTJBQkgo4c5mmTYNoRRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=FRXjMbip07RcRlEOdPp4fRZecOLXYuqpM7gvI5nv6ETvIlvcKQVQZoWzYkvVntaCWCjgs4rRcIxg4WzF3o7xLyqdOxaMshL2AlMVKwhKuRpWvl_Iu-faxlBfQ358lh9cXjDGTUVwMtaJ8mTI4WqhaurSsM7csMeSABmtZtSXnW-ozVufmm6zF_NufJY5bqm509Jgi0ur1K_p7saTUjPq6u5fPdC2sIe1shd2IwLWQyzrIHG5_-j35n_FjWo9kN4RNC8i2ZB5vYMUF2shAPksVf-EtIlCf_lZaWWTatc_3iloW2Ur4_ssOwdZ4qEvodE6gxHTJBQkgo4c5mmTYNoRRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تخریب یکی از ورزشگاه‌های اوکراین پس از حملات اخیر کشور روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103156" target="_blank">📅 13:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103155">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3i2XhziiZ59SnrW8wanlJLalk2cmVpc627fg8o3uDSfZ0YMbjM98Oc-Cs0JJqAovQoKSUDZp_IhXYe2SGg3JfAOmPa0lD5M2ZI8Mu43otZK02WrlnjQDRaT4J9FGiV7nWw95NmzpZJzGaPhNLqBozNM4gohgqKfm3Zkcbf04fm5QEnAoq5N3FiS9QqDLh0dYdnbRBA1wqLAsKeSfUfl0nHij_op3mr9Gh_zEeZaDiNsBLu6pC7Y_IZhTh7jb_tSilSZ92T5OBmRS7wupbAQIVKjuS5a3g0MaiT-8r6Bj-FsIuInK7YufgO93NoX2CUGT4_sanUTDU8uds_gI7lmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنیل‌مالدینی با عقد قراردادی به کالیاری پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103155" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103154">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHQ_s16-U3vUoGIDfF6xa-qxgO88AOyD0_sZYuWAmk3jzR7JvOMFsECx45wpmYKeEajNCqlwY2oOaFWO-cNsc6s9xHAqHcQdTwIkT_HDIUn0ar8iFUYDLEjqJBypsL0aVqmPZRExZN3AOD3AgsK9T_PdTQALrE3_Qhmh7Lx8bXrZsup7ScdMETgbSaqCBFtsKG1Oge870Zh9BShQ0IiMCYoFXlu_smCEo7G74_i5RuU9cj1r9xSCEOAucmLSNQpJbpiGfIJaOMbmknqsrHvZqZGpBZtV6idytgr7_7xOq-UfhLWdeg8td8-b9urgVG7bpR1_qBn0bAo8-zNaYXlpiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
😳
😳
ایران مهد عجایب! یه مرد در طول روز، زیادی به خانمش دستور میداده که براش چای بیاره!
بعد از یه مدت، زنش توی دوران پریودی میزنه به سیم آخر و وقتی مرده میخوابه، قوری رو میکنه توی
کونش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103154" target="_blank">📅 12:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103153">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeLR-_gVIas2fgGO8LuyQXUtY8_cnUvORn1VJ9P_j959sXq1gtVCdyMIfT9L_FcMusA-r_5-IoQ1WuOdk-cnIAcQTPPwSmudSqlxyEurglisHZXc4Gur1DpNILqLhL0fYsSn_uy5R38WypDxJyPDfh7ftr_36c-XhzVuUy7a_PuKG7TlEri2kS-jYt0sD9TeoqC5U4k4K7y1RjwgajxZTm1jUDNcQEhSlsSRGw_eLTjUHVAgPKHBeUgqNzP5zsIGst71ZME9V2f_8iXkJn2PMNfgWyAOGLZ_0PaaIxKXRqqHd1BsHpfmCSRL3Pgsdd3ObayAdCai7JpBeClg0wVodg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
روزنامه موندو دپورتیوو:
❌
🔻
اظهارات سیمئونه استراتژی بارسلونا را تغییر نمیده. هفته آینده برای مشخص شدن سرنوشت انتقال خولیان آلوارز تعیین‌کننده خواهد بود. اگر خولیان نتواند وضعیتش را حل کند، بارسلونا سراغ پلن B خواهد رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103153" target="_blank">📅 12:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103152">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh2afVGfSf-AXyCUqKXYd1TjRNCWhy-AgV1d2USqXZGMP91S5tiIUV16gLom6t5Zxl72s0XdLhubIabKOxkBe0MmXeHmBvp8yyw-UfP6cMMpZMfiJm6omnXT1RNuuYSDa36toKAe-CU1eLekbdCk394K2NPHRAsTLgSAvFzVE_e4hOSYZCsE_Z8Kyx7fFOTJj3piqM5ADGNYxSEYJOWnvGgpQsBxz4QSoRxYn940CKa_nDdGOa0I_AU0849iNbsPqBdyWSgCjDUr80VtO0EMTKQJQ1qJIhowmll_WCY_1tswXPM_RBdREouorNPkahpnjLqiIF4REfzGq9ktFdDw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
خنده‌های حجت‌کریمی و جواد‌نکونام بعد کودتا علیه محمد ربیعی در تبریز
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103152" target="_blank">📅 12:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103151">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDN_uOAXosVOygyo617Zxm3ScrM8ogGlGFQEyhaWWbwKPF8_v1VQWovxyLfkFZjonnqR-TpcsliTKb8WJDptnXmWPaHCUNAN0_NwK1knACpfW9ENdZ6Tq7jhZ5ugTDYfnEPexdOqC6ynRZ_TU0YgTANFb9OP3PVCsrwZZ9WPUlZQAG4hfiqdZPw3keqK_8mvCWLIU8XbcekJ26RN9hnlWVYe4ynGL2U5w9bdWST54ltJYeAOrWp1uX2Iezn27dBKIm_O8RGzzCL9W2KYQwdY6M4PGChtlTNIS-AjynDaR2gFCkDrZCFEUxPdGNQVLeYQ6Sap4y9_Qc6-qejQRuRH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۲ سال از بازی منچستریونایتد و رئال‌مادرید در آمریکا و حضور ۱۰۹.۳۱۸ نفری گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103151" target="_blank">📅 12:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103150">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/103150" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103150" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103149">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFmMtBqmdNdKvfeIvC_TBhtzfpphmjXa5G_3Nsa4MH2jo2_ff3pKjkRGmAgfjuPYF6ZzfSsIXJP_KzKgTGfVpNaVRntMVgbwRcHzT-mBZkIbSzoinf7h98MvEIP-Y1xGOEOOoojKls01JA-DsqPyuf8YexcFGxqAMRywzGaR-bY8gg0esuZhVwyvOc5u0lsR4iea5Alt6QIqueFYu3qWi9EDWhr3RG0UOYCAR9VDliFJXsETFXq5ObwCCWA_cL5q5ifcJUfijSsdKMU15Uq9YwB_Y5UmdACvLbwmEEYw0j7qxos2P5eL4oWRsAsPOPnYyi_2ktaQkQ64bFAmonWzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103149" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103148">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یکی از جذاب‌ترین دربی‌های سالیان اخیر منچستر و تقابل پپ‌گواردیولا و‌ مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103148" target="_blank">📅 11:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103147">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW8lsq-nOYhrLn3b2kGuWfNwFBNuhQGSOnIewjeZIoBKmDjELU4HC245sgsrXjT31DnDTdF4nkKJfVLmaaheoEj27zFz-4UG_gG9wDqzXtVH6WPdWy-SyB06bIG8Iu8zayP4dBVtTzZva4chovwWabYQO_so_NBOfIuqa-TcymwMp_9te2c7n3lJqfythugyqQHQfiBXEeX7CIMq8dBLKgrYWGsBbu_P81PKwAR2E8zf5g5Czym9RudX9zsVrVvqLYY5g8U2e8qhkqEAKbQdRionlJ2l82eL3y8uoA_08gtowo2AZaw6Fmgm7P_zHl4eTxs7dooUN3kIfo9NMA2Y3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
فده والورده:
من انتظار نداشتم مورینیو این‌طور باشه. او خیلی به ما نزدیکه. گاهی اوقات سخت‌‌گیره، اما فکر میکنم همین میتونه باعث پیشرفت ما بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103147" target="_blank">📅 11:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103146">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=gyoh1lMA_tc8VEMIfBDhS5wSFirVt47wPFTEYhQKHPZ2vtC0aiJ-X-r52xvfz02aej1BQrUVfjJee10rbvks_51LEzZVcWPsg8phYGKE1zEjib5Rt0u2wrg-RO0hEiA9QUv8dLT0iBdEHsBhCJCyhtpOnProp1b9q5BHUQR9sfpStmfO0HTxibHrmR391m0MgxYEbvdxvHJhPfCZ17-0Tm-yh4dy5zCuuHJeMzNXeDYQSrnXCKKC0oQCH08bdUMPdylEbxV5LQXeH03-Qb0aoXYzEZeuwA444IFtfmUqvgt_aIFlLgoRjSbU7hd2GNJfJRIV6eizIdYyZhdFTF1kvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=gyoh1lMA_tc8VEMIfBDhS5wSFirVt47wPFTEYhQKHPZ2vtC0aiJ-X-r52xvfz02aej1BQrUVfjJee10rbvks_51LEzZVcWPsg8phYGKE1zEjib5Rt0u2wrg-RO0hEiA9QUv8dLT0iBdEHsBhCJCyhtpOnProp1b9q5BHUQR9sfpStmfO0HTxibHrmR391m0MgxYEbvdxvHJhPfCZ17-0Tm-yh4dy5zCuuHJeMzNXeDYQSrnXCKKC0oQCH08bdUMPdylEbxV5LQXeH03-Qb0aoXYzEZeuwA444IFtfmUqvgt_aIFlLgoRjSbU7hd2GNJfJRIV6eizIdYyZhdFTF1kvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اَبَر قهرمانی وفادار به عشقش فوتبال
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103146" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103145">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=sFatZT6MAmAOkZEzz92S0wVGFIjc8E2urvezhyteztJC1KGlj9nZ2tDI3e2oPEwLNrUWMhavKRA_xSos2YeFpyGam72WW0WmqWSd1jg6Xr58bep7JJBqjJb4P-jz078rbO88spmrYB7xuGDcHOPLX6-k7iUsEt9KfVVqiRJTuVFY_P0GhCqP8C3dPuE1ksxPAimF7_bGBMzNIOxLMIdG_T2SMgpxiW-8Dp13-qu78k9wYeaSonTWwRdPQ18NrewjKBC8YMQfp6gt__siBlj6NatpxMzH27le6ssbfxzkHxJwOo7k2l9Mk3ulRz9WNJyOQHt4L_erkGu0N7xxUjbNyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=sFatZT6MAmAOkZEzz92S0wVGFIjc8E2urvezhyteztJC1KGlj9nZ2tDI3e2oPEwLNrUWMhavKRA_xSos2YeFpyGam72WW0WmqWSd1jg6Xr58bep7JJBqjJb4P-jz078rbO88spmrYB7xuGDcHOPLX6-k7iUsEt9KfVVqiRJTuVFY_P0GhCqP8C3dPuE1ksxPAimF7_bGBMzNIOxLMIdG_T2SMgpxiW-8Dp13-qu78k9wYeaSonTWwRdPQ18NrewjKBC8YMQfp6gt__siBlj6NatpxMzH27le6ssbfxzkHxJwOo7k2l9Mk3ulRz9WNJyOQHt4L_erkGu0N7xxUjbNyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
والیبالیست های بانو رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103145" target="_blank">📅 11:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkxPbEPVTewipDV8OGERIx9kjYX64KBtd1d1nwciq6-Fkk2kTaQTLNcAFNakcveqV40V-3w3SLDM48TY2xLQ8k_b9T3so6zXAjIG36lsYEyngqVHXB9t5m6DrNbNN2CzveuYGUm3cDgT0gBuaX2CNY6PkDIYDcZurf5TgJS8px3gclIWb61bFgwmCGTf55psR89krqCmeC11mqyT8Tj1vMVc9j_GzaxM-_eFc0Xzk3S9ZRonDi0pzgCegRTHmyiS5q8BDARWqfVzSBpylnKc2BqhbT9O5B2Kl7n3w_j6UtRcYBAiiMsDfZD_s_8fXPZttnVD2qe4Uyt0xJMY_t4bfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اینزاگی عشق میلانی‌ها امروز 53 ساله شد.
🔻
فلیپو اینزاگی انقدر تو دوران بازیش روی خط آفساید زندگی میکرد که عملاً آمار افسانه‌ای داره؛ تو کل دوران سری آ 300+ بازی انجام داده که اینزاگی دقیقاً 368 بار آفساید گرفت! از 125 گل رسمی اینزاگی در سری آ، خیلی‌ها معتقدند اگه VAR اون موقع بود، حداقل 30-40 تاش مردود می‌شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103144" target="_blank">📅 10:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8debb5a7.mp4?token=LrpQQwvkFQR3dawTxa4nfPDY5UA-iGVyEiXqDkv8o9qgmAuPUKYex9wtHO0EWR4bpIbxN2D4KAK0bPzqv6-bmUfNYxbCKSsgUYXRvcvM2-qzmUVg6FLKr_IIVOz8Fml1IqM_13d_xGTMTycXpCqyuW6KhCYS6U-EH4n2DEeOWLyz2KeJWiMR7ET74Os_g4h3YyWtQ8sf5vMb5FlZM9NO7dbVOgl662i_mioaXQCoSmAlBqDs89e9KLTfrdFiU9O8c0JOac6g7r-WEVjq5PQYrE1DMgGs545V0Iqqcjorw7jqT4KaExWSj9JIYukdUxBr_5E_7qftuCib84UsYsc7MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8debb5a7.mp4?token=LrpQQwvkFQR3dawTxa4nfPDY5UA-iGVyEiXqDkv8o9qgmAuPUKYex9wtHO0EWR4bpIbxN2D4KAK0bPzqv6-bmUfNYxbCKSsgUYXRvcvM2-qzmUVg6FLKr_IIVOz8Fml1IqM_13d_xGTMTycXpCqyuW6KhCYS6U-EH4n2DEeOWLyz2KeJWiMR7ET74Os_g4h3YyWtQ8sf5vMb5FlZM9NO7dbVOgl662i_mioaXQCoSmAlBqDs89e9KLTfrdFiU9O8c0JOac6g7r-WEVjq5PQYrE1DMgGs545V0Iqqcjorw7jqT4KaExWSj9JIYukdUxBr_5E_7qftuCib84UsYsc7MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شغل لذت بخشیه واقعا این فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103143" target="_blank">📅 10:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103142">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cccf30963.mp4?token=jrLQKwG94GW_k3_36-HLThAP0hRDtoSoQ8lWKFLhvLVvJT1p0Yq7qBB8Z5t8iO5W0kqWzdCp_a7y9g9rx0hGyGxn-g7ht5H3Gz8ybjBkOms4sEEcx9VsStwGuvpwNkP0ETW2PwqTNWtVfW6qRzYoFVgIWFx6aC_4zNjsU6VIC9c-rNuv_CtuWV7ZTaEBrArISExc06NaJz1nHOh5vSvl8Xs9jsUHSMA_ONtpMwsX7LVeukBQKjjk3uapvk8q_9TOU1Hu-DsHT8HGISoNAqnhHHB_X8sth0xL2t3lVL-QJRbd_3cl8gK-vc90LuYiehvgfIy9XGU7mHaX29YsCUMSh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cccf30963.mp4?token=jrLQKwG94GW_k3_36-HLThAP0hRDtoSoQ8lWKFLhvLVvJT1p0Yq7qBB8Z5t8iO5W0kqWzdCp_a7y9g9rx0hGyGxn-g7ht5H3Gz8ybjBkOms4sEEcx9VsStwGuvpwNkP0ETW2PwqTNWtVfW6qRzYoFVgIWFx6aC_4zNjsU6VIC9c-rNuv_CtuWV7ZTaEBrArISExc06NaJz1nHOh5vSvl8Xs9jsUHSMA_ONtpMwsX7LVeukBQKjjk3uapvk8q_9TOU1Hu-DsHT8HGISoNAqnhHHB_X8sth0xL2t3lVL-QJRbd_3cl8gK-vc90LuYiehvgfIy9XGU7mHaX29YsCUMSh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
هنر جذاب و تماشایی زین‌الدین زیدان در کنترل توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103142" target="_blank">📅 10:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103141">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_vvj3xtJEmoHOEiXkYfhVNW_NojHSRvUZgCO0al4kRO0gn3m3nLgMYWM7WacZ-i-bC0X8HwYhtTDGqj7o0gs-NG-K4K-P1mr4NxsSU_l21tr6OXf3b1Q8fpv6IMeOYBBHVGkjIAttc7BdQDoA10RBlu-Wps7B3fJ_Z0BAAmB-ISrBb1CytIeyIyIi_IS81vPb8yfoi_8sQ4GaDXGTbdajL8oT9x0KXmU4682nG1mB6SLBKQcvT08wcEM_6SjBvr7aGkwS29tmnRwUY-c6nilkk3iH82s8rdnyFI3NhxuXRCd4C4DJIz6gez0lt3dNrFpG2nbXBN8B7g7pUYlIm05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فابریزیو رومانو: رونالد آرائوخو امروز راهی مرسی‌ساید میشه تا تست‌های پزشکی خودشو با لیورپول انجام بده.
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103141" target="_blank">📅 10:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn3iY7zbfHulAWZlvsT80fR-n2uvdqxr5iLe82bLcWIcEPWSkxcTPJiQX9RCEbE6VYleDlmApBrJI4TiZdCVI8kuOvV08DzEXCjMWKbUl-1rbBNC961lojJ0Zunxih4wWrHwwKoPfkTQBrf-Tu7vn_Ac0Ro5opqBOiFhVYAw3gMHfpUoiTweX1hN3DlDqutF0zCdB4XiiRUFZeoI0ooFl4GpuViA_m2v7rW-OaB7s77oMbigBLWPfhL1TddNbZhx-JpbmnNIFkdYPAsO5JUgAF8QMVn3_eqL1KhkDJWbJWoeU2Hm2GMRW0bx2awyb64igWUNFuVb82ca6L_wv0WWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔴
آموریم با میلان هنوز تو بازی‌های پیش‌فصل هیچ بردی نداشته! حریف بعدی میلان منچستره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103140" target="_blank">📅 09:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103139">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رقص معروف لامین‌یامال سوژه عروسی‌ها شده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103139" target="_blank">📅 09:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103138">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHOHMKSE6iD6yz0f4zB2v02utv3VmjflRaaL7TJIpFZg_KY-1eYzNzsjYFkAwY-nZqBA-eD093Zvuk35rKDlQLEPJ3HscPUGqnlj0ds-W7y7vi1QYsfcao1hxhxZQx8Ia7Oqtx2O_3_o1_7_xFkXinbWFQVc8N0x7-Me96uxj_m57_ah58lfBkXR523KmZkwKpYaiwlFvS-uVA5PNIx_k6o54yredjKa32Rdd3fH33OsCw6yIgaoXbx_3M_PbqvHVJOVmV5dOy0A6aT8eTs7OF3Iz-foFefabbrAsu1womQ7DP8pCE4I6yKlhDZAJ3QCNyisfpzpx-RfDFZPUXEHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
#فوووووری
؛ جواد نکونام به عنوان سرمربی جدید تراکتور انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103138" target="_blank">📅 09:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103137">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR3OZ45RTN6ry0V31xjzRz9jPObINSF5h-gw_5EWbPHpJ4agtNDJx2Ai8sIe3Cj7uIn1un5kLtOXUdoJ4OABfySjf9i9gSm--L1_RM4nvFHLszS7V9g6CG0Nq3j-fZ0YD-kris7w2Put3YAWx-8OWaRSUQYkuOJoGgrpKSqZR2iMqCA9pGgwaatPihpLyiQMUms0L2p_3OZ-9UALUPeEyMltyNCEcuso8dqe1JXTfDni6VBtxpq3gopDtsd9HZH4KXSE_BIFgPfcVVZnnPSnAjvkovS-TK5Eu_yTkKzhIxEO9J-6JCoXbBS4d4XWCnz2v4IVF0mzK2OonXlJxWKElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💥
هرگز فراموش نکنید که لوئیس سوارز چگونه فصل ۲۰۱۵/۱۶ را با شگفت‌انگیزترین شکل به پایان رساند
🤯
🔥
⚽
⚽
⚽
⚽
🅰️
🅰️
🅰️
vs Deportivo de La Coruña
⚽
⚽
⚽
⚽
vs Sporting Gijon
⚽️
⚽
vs Real Betis
⚽
⚽
🅰️
vs Espanyol
⚽
⚽
⚽
vs Granada
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103137" target="_blank">📅 09:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103136">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730562ee98.mp4?token=eREPAKGsTQZDBW0LaSdAYuUflnkk74R5Xt585Ov5m6RbSnx-OXkwlNKRZKn00zQeYEDIoIkprHzyM7G-esxY-UhD5SI6vXfo0SfIVjfkYkDQUtZx40CyQtEP7fM_6Z1gksPF6t6flDGo2TXX-ACh13oMaea8nAApRd23kRiczWl2c3tO70IxhBikfvZaf7Kmb_vPCKp5PZcMNuxQpVe6Z9gpGivj8EkdgqXbvo2MdXNH2K2rvNMNOIxO34yLopINv-bG2JmLnq1zXWwEj_IsAC5I_0P2mpq6GwZeTyOxPJ_0VvlocD8bG47_DqxQMdM2lPi0kjNAonTlt7ikc7_fIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730562ee98.mp4?token=eREPAKGsTQZDBW0LaSdAYuUflnkk74R5Xt585Ov5m6RbSnx-OXkwlNKRZKn00zQeYEDIoIkprHzyM7G-esxY-UhD5SI6vXfo0SfIVjfkYkDQUtZx40CyQtEP7fM_6Z1gksPF6t6flDGo2TXX-ACh13oMaea8nAApRd23kRiczWl2c3tO70IxhBikfvZaf7Kmb_vPCKp5PZcMNuxQpVe6Z9gpGivj8EkdgqXbvo2MdXNH2K2rvNMNOIxO34yLopINv-bG2JmLnq1zXWwEj_IsAC5I_0P2mpq6GwZeTyOxPJ_0VvlocD8bG47_DqxQMdM2lPi0kjNAonTlt7ikc7_fIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوشاد عالمیان یه سبک زندگیه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103136" target="_blank">📅 09:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103135">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhFLwIHzo3z2F_R5IbAKBB2US2oIMpNphis8qalBPnD95MJpQwB2_uji9gWLks_6wsREde94FXUoYHbNkHTCiiqy9lCIbzYAfObHDbBdcCkv3AZMYRFnk36oRYR5mBd0UAkksO2QrKoqEIJaAvMZHC4I2Jj-HKhl5FhZ_5Yg_orD49uWLUp0hbE1Uku5p7Uaew9RCokB0rLOSzqKQ0KR4L1ieSEhgI9tHVsA71gHtCcarJIUY1xNGabrlhbSF0ZtEfn5STX3wSITnT-Vhl89oEo8wKoHOiRpKAD4AzOEEfDrOMmX_DDljsR4cJbAy1D8jxUU3oKYKY-fbIXBOwSfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهره مسی هنگام ورود به روزاریو
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/103135" target="_blank">📅 07:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103134">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ejjDEIUMdJyMyzKrdXVGOfctnkA8Ptj-uJ134SjJTuUOK0msjNYw1G6BCvZ8B3zj1khw-7C3U_I216HkOb903_ENj6BnYxjUYfhXAS-D9I-fu56TqER4WsuZG4bQVMf3_rjuCZWoP66GXzkpWhQw3Q9_IlJeZN7fQ_WJDgJL0L-4VlduV27epOO6qRLTGTKw60lOxtI00CLBpzjabc6snwJO1jSBiV2ZN_HO-l1fEz2RcmpOAKAWvX2wgoda1BMXn0LpVcsVp_VIZ2qgA5boQeZZycW9McpHI8XwB5m6ZYXPVdehMmk5Yvl5R8kAW-pCWVcm-BTWBhZ11OvbM7fIiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ejjDEIUMdJyMyzKrdXVGOfctnkA8Ptj-uJ134SjJTuUOK0msjNYw1G6BCvZ8B3zj1khw-7C3U_I216HkOb903_ENj6BnYxjUYfhXAS-D9I-fu56TqER4WsuZG4bQVMf3_rjuCZWoP66GXzkpWhQw3Q9_IlJeZN7fQ_WJDgJL0L-4VlduV27epOO6qRLTGTKw60lOxtI00CLBpzjabc6snwJO1jSBiV2ZN_HO-l1fEz2RcmpOAKAWvX2wgoda1BMXn0LpVcsVp_VIZ2qgA5boQeZZycW9McpHI8XwB5m6ZYXPVdehMmk5Yvl5R8kAW-pCWVcm-BTWBhZ11OvbM7fIiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رودریگو دی پائول، گل خودشو با پوشیدن پیراهن مسی جشن گرفت. لئو مسی به دلیل فوت پدرش، خورخه مسی، در این مسابقه حضور نداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/103134" target="_blank">📅 07:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103133">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfkBmBhifiatZ2RIKZju0I0D19l9CIGsgiYDpyR4FJB0OuKbp74jdtdtRRpSVzXByrZd5BIuQ41s6aJJCCAtr2MdKUEcimJjvtk0ALLPPGdkpZwiRPX2sDxbAxiSNkXqM-22f3U4GcAfSBy734BYElu98Gor5G-xRg9v0ndoSJgk8RxP11yFmAbsjoMiKFCoTjGdhpJqhCR4tKU3YpeNE9SzOOn_S-7Y54CbOS0Wz5C3tmhCgJ8UpQ4Q8kOjZWB2TvT-uh0V84NMqsf35n6ZJ5Jq54zlmj7HI3aYO3mxbq6tiHpG8u8C4h5-IHE8tUNkJOzQ4Y1T7rcEMQh5ivu4Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اینستاگرامی لامین‌یامال
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/103133" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103132">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=solEQaath5pfdYU1zm9pCz7Ai6cx52Plca7FAxeAfNnHdoG0DeIuOTHux5iIFEmELxZmAazEUJBMkQrJbusTdh-oBxExcCrm1FtXB3oa82v-YvwdkpfJ1R0poySI2OT4rq80Cuw1vgKhu4sK6i4Kn28oYEdsG56EGeB96K1-orhjlxxeQHcgtOHWhA67Vz4FoK-cdmPIl2wdBIJfEea2LSjTRQQRwGltN3-I10lyiuzRGNzVSFdEzpijW8rjoMWi0UrGMNFPZFBPkeh0N9ECANpbhou0Z82zrHXMy_LKX9-kakGr1S_8PjbaMru1uw8lrlUj-bDc2MIUSj7g25wHMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=solEQaath5pfdYU1zm9pCz7Ai6cx52Plca7FAxeAfNnHdoG0DeIuOTHux5iIFEmELxZmAazEUJBMkQrJbusTdh-oBxExcCrm1FtXB3oa82v-YvwdkpfJ1R0poySI2OT4rq80Cuw1vgKhu4sK6i4Kn28oYEdsG56EGeB96K1-orhjlxxeQHcgtOHWhA67Vz4FoK-cdmPIl2wdBIJfEea2LSjTRQQRwGltN3-I10lyiuzRGNzVSFdEzpijW8rjoMWi0UrGMNFPZFBPkeh0N9ECANpbhou0Z82zrHXMy_LKX9-kakGr1S_8PjbaMru1uw8lrlUj-bDc2MIUSj7g25wHMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه اصفهانی که قرار بوده برقشون ۵ عصر قطع بشه و نشده،‌ زنگ میزنه اداره برق یادآوری کنه که در ادامه این اتفاق فوق پاره‌کننده میفته
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/103132" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103131">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEk2ZXdEQcvCtkNReBCpa_nWgXxXIsUVUPmpUzWw2-M69Fxu5B76HmYNNt_YtIT9i835t6jWx_Cdyn9sDCHIhIs_OgwsTb6BV2mq0Dpq7vmIVA0HPTnpkCslAvAEF-_XkfIwGntJbggYSjWtdHQLsFz4Dm2BIbdFY-HoyEScDI9iFaw3YWnA1FbrxL1yGUbk885_LU2HHOMercxXLkcbiZ0p_Cn61GCH3Yvn1ss8E4rdGYEI3o5senswk_mZL7iDr5kUvnN5jkfiCLifhNSaa8mwuAN4jm00GKdFOGpNbDVZUezhnYNsNcg8KgdWSLU5hMEnHNasoIM1J-Fl7mYXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیو فیس و این حرفا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/103131" target="_blank">📅 00:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103130">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrru77Ipq0AZp4xlxs6-eau9jxVmftTDJj4jwHdMnamgLdSE8xFxFleA9jCeKZyZrLoiekvtNWnAGhotN9NWMsbYKsHU2LDkv4J_oN--1ZUJARoWpxlhwK_15GOOhaOFbPHIFaNgO6dIgPJfcqv6Wc1AnZIK_FWH-NZGWpC7TID5b1L62q_MuLSakoUMS8nyrCF0mFQzrr1YjY2l-tMMMPW-ROWyOaoLwltHa9mXOTZtUoi-VkT-9FkJZikyLz5p2h7ubJADde42u6dPaTGUsAoFNQ0dbDYSjNfrupBxNfhguPHEOyGIMU_6rqqjLb8Pib7S4AQyHYGMgkzDu6_6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
👀
فلیک‌حسابی کلش کیریه که اولین جام فصلشو از دست داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/103130" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103129">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=FLNGnyEhrY-KyTUz1Vot7rDIx4YQCq9B1bwGwSV39jisIo95BDVzglhoX-_IBxPaUmb-Jjb5FUgpDJZRBgV-crHYpgkzhl4hFupL53ETHwlqot9edCO_HYrJSPmbPqUkwNWk6i4dcRaP3Ghc4vlu5IG_4P3peMPF4Ii6Hnzu0QVtcCCtW2sUV6e-gq4bOINkVMrTuDC9wLeM6eRR3uQswe2VfWNWjyRguIxQeGHKK7nnsQkLORvjzqhZV2uBV0nW7R2x8iB2Ku8V1zZreKCRainQJ_rmx0nI9k_GMWTtOcAi6N3toAnuWJd7c6yRn7G7mVGB0CX8HrZ6nd7HtHTfAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=FLNGnyEhrY-KyTUz1Vot7rDIx4YQCq9B1bwGwSV39jisIo95BDVzglhoX-_IBxPaUmb-Jjb5FUgpDJZRBgV-crHYpgkzhl4hFupL53ETHwlqot9edCO_HYrJSPmbPqUkwNWk6i4dcRaP3Ghc4vlu5IG_4P3peMPF4Ii6Hnzu0QVtcCCtW2sUV6e-gq4bOINkVMrTuDC9wLeM6eRR3uQswe2VfWNWjyRguIxQeGHKK7nnsQkLORvjzqhZV2uBV0nW7R2x8iB2Ku8V1zZreKCRainQJ_rmx0nI9k_GMWTtOcAi6N3toAnuWJd7c6yRn7G7mVGB0CX8HrZ6nd7HtHTfAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
تک‌گل تیم اودینزه به بارسلونا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/103129" target="_blank">📅 00:36 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
