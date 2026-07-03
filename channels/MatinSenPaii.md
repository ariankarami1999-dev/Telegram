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
<img src="https://cdn1.telesco.pe/file/lwIhpx_Qq84wqkLCAuCEwELylCjN1_wt05uzkK6Cq6MZrkdHYBfl1WOnn8FJKWNNicaB8kUCzKIjNZ_3Wp5siTwE0vcjjEb-GDOk9vFwEQv8V0D5msiUOnpFvrhPQj_FngaszSao-Yb5Gkt6QCY3PFXe_XLxTDvQHsO5VQ_srwA3K3kPJyZtJc2IwDFr7quz9ot89yCu85LCfEB5951DqmWgXM87ve77dPViUnjrmxAE8HCNTX2zxdarHnU02GWDB57tJoA_Q5OjZe_EJW5QbbxJNE-taFLP5r5rgMMyyqPdz9ZWk3iR_yvZVffDxwYuLS87gFzj8uhwzfJ-onwlWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 19:49:21</div>
<hr>

<div class="tg-post" id="msg-4206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=Hu_y1fIsH1Nvt9QDWz-ylo5TzyGaLofeCsdmy98EpBYLAlerTBEDq1PRiUII-T96t8sdo1d3hi-2a1uh4ORLvO_X19OEAtJsAWr__X25q5_PzDVacECvLqwzsSIfRibKMAEiM6Ivis3xbCflcsAQa81Br_c2SBtYwky3PseIy3JZl0fI5cnjw__bzpkQ22bbzFPrKurG3G68I6bS0WtctRoSwN4exo_cn-bbYTo6-opVLjbeRNKSZ2T0CH7gfJI7y_WSJPfArLy7zktqARm854PqvSaHwcUIhRVmD4cAONcXjqdtbQkPjsNep1VuPd7PZ2hCS4xMO0srqmqKcb8CBIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=Hu_y1fIsH1Nvt9QDWz-ylo5TzyGaLofeCsdmy98EpBYLAlerTBEDq1PRiUII-T96t8sdo1d3hi-2a1uh4ORLvO_X19OEAtJsAWr__X25q5_PzDVacECvLqwzsSIfRibKMAEiM6Ivis3xbCflcsAQa81Br_c2SBtYwky3PseIy3JZl0fI5cnjw__bzpkQ22bbzFPrKurG3G68I6bS0WtctRoSwN4exo_cn-bbYTo6-opVLjbeRNKSZ2T0CH7gfJI7y_WSJPfArLy7zktqARm854PqvSaHwcUIhRVmD4cAONcXjqdtbQkPjsNep1VuPd7PZ2hCS4xMO0srqmqKcb8CBIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی نهایت آدرس ایمیل با یک دامنه روی کلودفلر:
https://youtu.be/Z069VNFAgAc</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/MatinSenPaii/4206" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/MatinSenPaii/4205" target="_blank">📅 19:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OiJQ8HhrQ5aFDuIhM5olM8yDR_H_taRnKrMGacGujtvHLPohgRHqTuQU3Ww3FML6HbCtOeczqEe8Gb_QGtsgbBZ7F9xhrfQAYo3q8DKXYvWnHBhoeM9HEz2VKu-qT7pNQ0NuiuHPlwX5pfUXCGU_LhQxRiQkW5KRH39ehN05dwS8uJUqCwzmBNRMknjHtKQRPGVtiK7KP3FQxFtbQlH502jhnf8D6kS12uWmVEmkzw3L-tLiu6nZK9WVf1bbt6cbh_pYiHLc27B8R_y8YZ-xprCsakE4rcPeyA_UyLK0tR_q5CsCcNrIsvRqQEqsji0L3zzxRfvib-dFV4zlBLbrKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب دوستان GLM 5.2 اومد روی Nvidia
وقت استفاده‌ست
👋</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/MatinSenPaii/4204" target="_blank">📅 17:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4202">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iqw0TBdPXQvmZAmkPALG5vimqcyiUHMrOXmhhqjpQzd0YHubMvKnoJhCLHTfBIKF_nzcWZLPER2AGU1-0kL2-6MXqqnfCv7P9pQT9voxclp0nqnGonsObwblk16ypcDbsd0Nms2FlAWRnJvj8wW1RT8Cf-P3zRFih-vygNYLoKw-A11-Md98ZQ6vHuudUfOOo4otBlyfDfRAL8jG4CZZUVnqEHCsRUHpVwWjkFyum8Pj1rgQXb064VNMn0aaCwqEDnTcQ-XdECtNemdIqhdN9KQ9TK3ysnHUcVyWckUN0bqWSLDf9VzfIZrHwFzQ4-q2VWQbBp_mY1hp8w01UVesbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DLsSegsPTbC8Bojqtfgf4t3YIcpGVYDRqwC8LzHvVYgyXYKyEHO-j-hARHZ_KrE6wVbhpnBohXO72O0r-WiCKdyKnu-pb3djhiW8FZMoVre02AA_YowUvH6Ow1rUUgK0pMmQwzTTUNDbzHcNsIXpitn0QKm2-a185E7zn_Uyoibj6yJQBaGybQedKTILTNgqT7ie5vYepEEVXNUgzUM3kteHi9d4tBaqlqjIhuaFsBIkKc85DPiBbDIWO3iMoT0ewItEHU3h1uDDnrUdOeATMn19ZXS30AjIfbMNj71LYaug0pHJlrhLlF-rpThZkHsFBG-vZ32ETYTlYEiBRR-oxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چیز بامزه‌ای نوشت اما پر باگ. دیشب GLM 5.2 برام دومی رو نوشته بود که کار می‌کرد همینو الان با sonnet-5 هم تست میکنم</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/MatinSenPaii/4202" target="_blank">📅 17:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4200">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SuSYZLB6Oxmg0LobMyAzLPZBsdB2j1u54WPVal9MjNszB4E0xnnEnDhG39oWP10wqXVjp8VJCbu7GVccc9WkIxEKYYDbeaNeHBXaaLzc4uoP9N-ULWmePaA_G9762wAKsKNITNM91lAIzQmhax8zSj6Jw5e2_PxQ81Ok1zfVmO8jGwVz4wgZqf67zFj9myUQWUosAuFyqV25hs5rss5iGZNYUwdDIgP8V983rRDGlGW1nB0oBMkf4Tj_F_FgIG6Kg5Ntf4Q7vWuqho0TDUf2rYsmMNhixQj1-kDMU4rmAygkGsXU-jJPSJvlyJKSYWwJ-lxwnMoZji20J0aaAOahnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DNceRWvuJRHhFmfjy4FEanndH-BTnsyavBLcPtjYfrasomaW9mG68qso-xVMbrwTiASJxhSHQ80njIKVwxXvrXE5vly-mTtA8iNuNmD6pvrS1b67BSL0A5Wwo7XKcy6hYzvTT2Zf6LTu580bQ6oc6icnoGvdWMQoyp4NOvmx0jDOV5ocFWKO6VR26_I4feK1GiHGXIRU_e9ZtTVjS7gRRHyCEWxfIO8wiyZcuB0pdkn30dYn3feStZT3VgvKKqFLNCw95B9z8O6u-v-F7Zrb6RTHGrKTZlmrl_aVbR2z5RBC4dQtMPtjMzWS749EBFe_YSPFINId6qHKB0qraz5Mnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بریم ببینم با یه تسک گنگ و غلط غلوط چیکار میکنه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/MatinSenPaii/4200" target="_blank">📅 16:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4199">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CiyE49epzOecvSHEyJuzUtcR-zTGQP4vRB5jfbgX-h8XWFTyBq345bPHNB1h2dgjbRIbXM9WxpV5FmKKfdomayTf3IlTkMV6_y7AwZGZH9fpmIlipSplBRfdrbVEtNi8LDZZQUAA7mD2L-2dNaR6LQoJcVNT5eZbfFde_WzAC73dbZ78HbRiGNj6aue5mijZrYUKNMHsXaX5_fSIdOmzsAfP2fE71j-VKwEaEfWn0Ec8dg_J10lvqhbqw_fdZc8MBx4bmWfziaEnpmT7AxJJGX3UZIAh-TxmIthQQeIQ2yU6OKO-t2eleSZ4QmHLD3xnahJLXZStSn0Fh-zzxrnV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با chat.qwen.ai نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/4199" target="_blank">📅 16:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4198">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHGJdFjS2lmyIPT8Fd-havPO3RpZJdFGK4IkWFyVCCegWdHKc-2h5uWxpl6ImLHb7m2YOQEPFxyO9uaJNYLAN74BNydW9nQp6Jo4HRcdMCRQhEAGoM_esHH8ssS51N3Zb55aaY5Fh2mY90qliYx1bXJd-_MeELERYQ_3KmCYjrvgb8mvB6fIgyjDC4gFlqOvYNrPIz7WvaFLJiKuvClCk06k3z9cnDuXPlj4X6MDIxAyfLWCYlk6Wy19J7mOruMYyrqFq5AcQ_YnBygevx9N3mrf_d6OUfhFigVoxA-f3dsGA8j3mvoeQqsFFWer4_Rv0l8b05WT0fobIB_2X79vFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثلا هیچ فعالیت روزمره ی معمولی غیر تخصصی و تاحدی تخصصی ای نیست که با
chat.qwen.ai
نتونی انجامش بدی و نیاز به خرید اشتراک chatgpt یا claude یا gemini داشته باشی. البته دارم تواضع به خرج میدم و میگم که qwen صرفا از پس کارای معمولی برمیاد! برای سرویسی که میتونه پروژه بسازه، مموری زیاد داره، عکس میسازه، فیلم میسازه، ریزنینگ قوی داره و برای هر سوالت یه لشکر ایجنت بسیج میکنه استفاده از واژه غیرتخصصی تحقیرآمیزه.
✍️
بوکانت</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/4198" target="_blank">📅 16:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4197">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">توی مدلهای چینی طبق تجربه‌ای که روی هرمس داشتم، MiniMax m3 خیلی بهتر از Kimi 2.6 کار کرد واسم روی api انویدیا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/4197" target="_blank">📅 16:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4196">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">به قول یکی از بچه‌ها هر روز جوری با Claude کار می‌کنم که انگار روز آخرمه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/4196" target="_blank">📅 14:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4195">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4195" target="_blank">📅 13:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AAuvbUzKVoboKbndrSK0XuBv7NrLwlJY-UfyEPxpfkGKzBBENdDUtQgm4psoknhPRUwpB1qoQZ72bdIqRiDofTyQsrLCBMcR_I5rJTKn2iVQxOywTOHgsqqG5uUIyZFSxGOKz6F5duLMoIAOa4b_WZrcP6lfi-uf3TAmXvNwu9FrsqbNrjjnU6zW3hjSk73ZLbvykJpZqgYqz9yZK7GsaH1mqb2-WBjW6MEXdImcPbRztwssHYpU2cYUxc71XZv2YqydojBfe9hbPVoMe5GF4yCbQJ1FCIs9HQQs-8THJXRrDvHDI6Sd7GTU7JfOlHneiUw0VQIi5j4XZq0IMC6ZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LU2EBOEZp_J5ecJQqHOgOPsZjO4U1dGKfSXy7HBqkBW9eBEdsE94BhPd1Jo_CdhsQnTFMA6ZaqkUp-fiAdqSbe5J-1O7PR3akxAkqn8wvoYVEViGgibbakcsOehUJlpt0RtT9j9el-JMg-9LZj304ij-fkEzTqFLhJoQn3NBZfaexkE37cpLFpG94jAQTcSML11n36gq-CO_J0MJge01QxuutbNCYBYRLNz7m5ObPFeEK9nGQomS_-RigLx-r--ikdUWHMQHQ1jmyKxbgbg5hpzCFprTsTzBO9Nl9z2zuvXAd7173JP64XLNNkirbGF3qRKEa0xlG5E1dwzH7spsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLGXet_wKHnVTkTOi3UegxLMeVPqEDJoBGAEhM6I1FqK6iQLFjwRypGcpBnmgI7odhFESSs1cpscu4SLDRmsm9jHYTsN9zBymSX1t-Q1Xox7zUuaZlssprzq0ER9uy4Gs84P5FhxX4dYJKpby2nyRq-QOv4vTF2mc_5_-QY4q18c9ipYGbgqaF6OQOWILxvyOWgVGbeL5mZay13dybtTy7uG703l9SwNp2EASsH0wzUePRvQITB_0GpW8QxiQi5NPPobSRZxc9-KOina92pUkrgim3GP8VEs072tL5ipqWY9H4rthBhonsyl2cacyXOclRWmqJeKuFYVWd95QwPelA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
DoH
HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده از endpointهای DoH، کش نتایج قبلی، fallback و حالت اضطراری، اتصال کاربر را پایدارتر و قابل‌اعتمادتر نگه دارد.
لینک دانلود برنامه:
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy/releases/latest
لینک پروژه
👇
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SSHLBBJahB51SxqcP7pGx82beG5Y9auksXId2Xaep2BlqfvtXI241bn4gQRppPeel1WzWPxQNNaZGl0n9wVPcPdOYRYFR7eComVUO4IviDfNmdhtWTakyopl3uYx0U-2xIiZLfmrtL7TUOtNkCwTrTeXiQmCYnm4oK1DC4Wq-_YbFmODTbG4KoihRwakiyxlARM__94VyQliXaH7B29uA-rvSi6jxkqrFb0lluqBjIPlKnjmMz6-Xgt7cf8Qq4q3_EjDm-N_RO2fHGuIxE_2VmHW1BbgebmQHm35AEWQcYywYzGHRhaec3gzfB0jDJRgMvuTVNit6RnYy5EW4ZAugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqg6IUZt-FLlyO6x0ySj5l_6wW34ehwbYWpQyiCdAT3GVjcZoYRAzDTpIeaIYVBdeef5-zCyMrOXP1s4Mj7S-Elj-9v6QjEOWVb4pUGbpAmC5BdnnbAmlsbCK3PMvl8PI0UUN2Fhfm88f4Kbanvcdb8uqQBMdkwr_xz6cduGww9tPvUnRToCsEev-FojcsCX19TflElyL7b-NLUnewjwtKORpPVCdNol3R0-EUu5XK_6DkDDALyBk7fSnDkbzm-aW8keo48J1IEW2_hQ9FYWVjZ6P8e2nR5ECQ_LE5v_9NquWKbu0aPcBSE50-e2zWnX2nU7LXI8sF-ru_mlSb9cJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X7xTmv-nPLyrv9XSppzmDQ8YuWqVZYK5IrZldDFj7qu0ZJGxnO8ZZ9BCI5WRJ-s0bEnYE03WZphiQysCoXQNP4vZ9NJf6nrcaG97keo2r0XhUH17GhXfg3TFir4V4Fs-tRHsRpwjYQnzALHwXzqOjMl8ZW6YOWSduBvmwc1ZweEhRjUg6W0JHKW33T_55XNBFlAYoAJtMEf8mSfY86yQCJFnXZ-_ufmrKd9a4VaHPtuEcT5kuvsbE4DT1ildOk-YaGlGEdKLJcCr0kb7vECK2npdsEc1bjRxdEjKm9SJu7W4yKbtOcEOkI8WeGTxyZYyZqdh7clFtQHz3wlPsdN5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">886 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4178" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات نصب Hermes روی سیستم‌عامل‌های مختلف و سرور
سایت YottaSrc:
https://yottasrc.com/
سایت Netlen:
https://www.netlen.com.tr/
سایت Senko:
https://senko.digital/</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ps9DcufzHobz32OVYdA2a2F6gpAz6z2rCFbGklUJH2WXOETv2XLWEYuDxi2sRdTHssoflS6GKN78hkINHEqxneMHz5kXsxFIa7xGv7Rf11o8WF7PCv9jZGqFzkPUVia2_5DxWMs0S7_c2NdUW9SxWsk3pvJRifokwwUsXYLA7kSDwYeRletp2P5LCrdcRAo1tqpJnZQy4DJsiLvz7BPzTyD9bW753epZ9IJuNFjpUroJudUoeD1RVI04OAAnv-Gw8LounmrU5hueyucs59I4ioLBu6Sf7uN6ydRsxewfLCgx3UGRRtZP2NQkNtnMaLGyZMouj2JPRbX96juw6atcqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو:
00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟
04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس)
13:47 نصب و راه‌ اندازی روی سرور لینوکسی
16:46 نصب 9Router روی سرور لینوکسی
18:10 استفاده از API و مدلهای رایگان قدرتمند Nvidia
21:20 دور زدن محدودیت دسترسی به API ها با Worker کلودفلر
22:40 استفاده از Endpoint 9Router بر روی لینوکس و ساخت Combo
24:31 اتصال Hermes به اکانت تلگرام( و واتس اپ و دیسکورد و...)
26:35 نوشتن یه کرون جاب کوچولو که هر 5 دقیقه قیمت بیت کوین رو بفرسته و تحلیل کنه
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LtmDxuMnUgIGLe0jkacqE2nsoiaj9jeIb7DgK2cWOJ1KpctyIsRXHhc3nSktw_ksJ2OjPzOhvWJzjgx7VboddZYQLj6Iq5Xqmnbiy5WVUBo2a_0oLDgU2CcdlxBR8pTJnJWvvet0xkmY_wt8doGc3yKwA2dBV9XciRG_sk2mkW9XEg_NlrxLAD6SM9VjOYc0pAA6Np8GWbbP_t_IBP5GO6CtjBjOCYOcYCe3xHqGM5gqKJHJ4wu_5f92rm8Z3nDXzpbDnCyANiu5dG15bCDNGcs86NuopWRUSvoh3GFpQcdzwDa1WCrsOU_weTK2ZZc0_dXfSG9FNpmIBVSHPAZ2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5LyPaOiNw_csD8sH4NuPJtu9a2AHA9kTmwpjhoDKGQvpIUCaKOAVhOpsB5vm6ZQnSHjLEX4bCDJfyBF07mHUgcU_P9jyW8_QpkUkZkZ4gVxNsXKLf7uQOSqIg4rPwHeDaOjPSiabsDAXTs9M7yi7viVG4BiecfVSxRFarX4iLJoCCbMApS99ooGwnb8X_JRyha0w-YDb0xwS9NymLvud1C5AD04R3DJ95GOgYQCsmjbdGIZIEdGZPftT-Hh9oUw6KTRS9mWgU7PxWlggIQcAXhktY55gNHp0qUI8Ocins6HTtL_XwjSYE60Cbk_GiUQFdIzrtCTouqMVP9DLMWnrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RXDafVaShxCRUfvG-Jw6Yf4fD4jCs5AtHmFNHx5ptvSReRQINacJvy0OYoYUMuCx1TjG02iCgdJWy1ndQbUOkMKM2UlwJDkTLkO_GxBp8P9hgp9HF6_OWcQIRc60Cypp_6nucwi8GaKiM8gMMQMAMgaZPJlRRglrdBHroYkGoMBPKeXIocehMEIequ6sGCqEpLikAEMqPCmcXeRsxO8xKjTOe_vExoFtROGs9-tz8ApNHDDuv6RiEiOcI16JTCrPBL1xO0F_LKHd6q_raQEJM71g-3VXdoCzjPTfMd2M5m0LBS9KHbsMKjd3Tk4nMZXA3F1ILJOnkh5bVqmcv4Y4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGPRiXxjjNp9ZTUVIpgV_pP4_MstyN7cTUp0Ds4oJ0W3WZLRPeAlv6pv0F7DR_9AFdj1lpgcVajNWrQo83-Mu2D3CgxZ8G17lweIMFOPz1Y1R-k2yf_NrCKJrx7BwdmgirFM5GZ1S75c-4ri-59lSI_QyUXBqXm5KExmKRTR8wMAZcQUTGysIwV4bn6DiHBFeSecqz2BP2G0m5rz2bUY61eQ49l_r1M7GVUYYUQ63ZyapT2seI4FkGbPLnuqyv9k-eMA7Ww-0l_mIQ34KpG7FNst0x5lJgCnXekgYbYMDrqA8w2NvhJnGw6PhdupETvTkrmcmM_y-dtPpaEDDQZRbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BC5lMFdJj2mEXigWAvaIMKxaGTjMLgoghGG2a68WDZhvEclN4PKZIHkwNZ9GnPRCgBJXwlHPO2M48nlkTYlCNguB7DAmmFPrbahwAtax9xLhU5fz_AC5lDsJw3jXirXFB3ZzAKgXLEZ1DoDAeLFPpOF7qkHun6JTUK4TBk9nhuqflLWStpZzn-oilZaml96jIFkFkzps8KePaNEASwLSxTV7eA00PYcJPVhlAIrFZDa14NzUpuj4q1uDYHDY1YApkCm4LALcSlZXYhna-GtDTbiUcXt6Gh_Kn93jpDMviamDWu4caYHOX85UUOTbeCOaYRDhZJR0Tm9117mITzg9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IB1O4qIYOtn1cl4bLcEb3sIPjjZPAPkSR41eD3iVzpwUPmEjhG5Po-MiUaIuFGzFmn7c8ngLu-3Lz2gtkwUqrF5iIyseVcWIYDHt-D1lKSDsh_uzKR4UVXVu0PvTC7Ov12ijfeln51ASfW8T-l9tlIksCqAgmiNXYM-ybqeuXPPPAowI6_B5UCJtamko0A3hnK8IQWW7vkrVWvkhrPwv3Rjvdgh4-1QO4d-Io7ve3AugNH35njxAa4XEC-iljRPhhDVebd6Re4dYx4BobpLd8gJpR9I6JsIqP9AS1l2UP6fSQTkGZYrwGDDKSaMGFO0W0WzLUKhQLXKmPehkUy1_Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bp140yJn8K4Tl5L1yXF87NoAi45CTd6lU34V6Yh5aWavM36OpX5yhWk1GXeKAlS318L8oCo0EBshiNc_FUw7APxyYm8DPZpwp5TfdvLVZWl-PDWy98wV4-LWRsRzmewfEymN7zhxpPUcBIQJPNFIVoPVQSCeY9BA8WrDEzYMEKDlF6T1Pe56KfwoROgSMalrM0TcM9MQG-bJhbhlpb-qELBwOWfcfRNSX3eAVRKRkUAiDi0u487xdl1ZwIRxkTiyTumhhGVNy0lLSCqVrXE5VwO7WUUIGOYT_4m6wST4UCh7iMBvRuMEmBBaItyefMGSJN2akNTvWFy6jVONGbciLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QGLyJZPKYKZvP_kuJR2DVnA87enjJSwV4GDN3rRpL6bLBVkITEatrzIBL1zrXWAmN-7UqgGPa1msqgXwO9DaJc__u6e3GbJQ2RoPa7VLs2cP5AaYNPTwOs2_EeiQkFRwCmhelPIUI4jRDCo8h6e_obb2jRF8kpPhzppoeuxEEofRqCX4vXNonoxceBxJdE4L-r4NDH3pk73LWxWJpQSI17GKuXe8fhMn0L4P3SIJesxHVOlz6Mm16a0vcRaYWAjjAZxin9PpLoSluZKg2LCV1WQ0GTIE0TtesnFQYHKjKT0frPkz34I7llslI9HzyQ3FSraqi5y2N1E7jAfN6_iuGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ulmxRfqkFhWV45FLLeVOfNfM4rWewQGlD8gZaJZdfqW0AQZqXbqVWNnWg1md6Bsa-NW9UWlYQPPesu-RsPW0ztaw8j-UAZ0LexhywrmaldY8wEVw_wKTKQvy7Fe2lA9IJ5lcCIN_lsrGosDAYhasgahvO5-CwtvujZRl-Cqve-0yMNZ-Sr88exMw1-S516SVodqnsglMyu488QmOwPm3cKvpf2Sn4CUdHQI-_NROnhesiqkzQ6sQHn1rGySCVSDRxaVoBtYElqQr70OUo_Rx1NK-yh8z2RLrpn0EazsFAuyd_qWDEH5kUYhS8Y6krPSNxrpVQcyNDYeo30r-F3xYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=rNGo1sp44U1aU5ANNqUZcPC7GFd_O1mD4MO1Dtoz2Rqn9evBTuNtxkTPO8XSckwIu7vhmU9zPW1IF1Oeqdvi4E9QJ2ztEpU4RM3UJDNZfFRnZhwkurnOt4rW3ijdRC_u_kBLeEUXxvPoCO5TzRRKn9lCERNpYdwwvwrFNOeqaRkmH-Rpj617j2hsuB4twnGdX76S5hPz_cfWjEuqdsNaFNwDwhyTeJ2wUODI1Pixjx-CYZ_ebJE8j4L308-4OzxROD25nHLyD__GfAqURwUP_9B8fYc8plD9hiFQI-omuuL50lU70zAtL9KOOhyuo2d3ibj95hI40jL2CPVo7Ah0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=rNGo1sp44U1aU5ANNqUZcPC7GFd_O1mD4MO1Dtoz2Rqn9evBTuNtxkTPO8XSckwIu7vhmU9zPW1IF1Oeqdvi4E9QJ2ztEpU4RM3UJDNZfFRnZhwkurnOt4rW3ijdRC_u_kBLeEUXxvPoCO5TzRRKn9lCERNpYdwwvwrFNOeqaRkmH-Rpj617j2hsuB4twnGdX76S5hPz_cfWjEuqdsNaFNwDwhyTeJ2wUODI1Pixjx-CYZ_ebJE8j4L308-4OzxROD25nHLyD__GfAqURwUP_9B8fYc8plD9hiFQI-omuuL50lU70zAtL9KOOhyuo2d3ibj95hI40jL2CPVo7Ah0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Anthropic از Claude Science رونمایی کرده که به صورت اختصاصی برای مراحل مختلف کارهای پژوهشی و علمی طراحی شده.
توی این نسخه محقق‌ها می‌تونن کدهایی که مدل می‌نویسه (Artifacts) رو به طور دقیق ردیابی کنن، محیط‌های اجرای کد رو بر اساس نیازشون همون‌جا بسازن، و جالب‌تر از همه، بیشتر از ۶۰ تا دیتابیس معتبر علمی رو مستقیم به کلود متصل کنن تا تحلیل‌ها روی داده‌های واقعیِ علمی انجام بشه. این نسخه فعلا تو حالت بتا در دسترسه.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9603918fce.mp4?token=RKQruIy1dBQ2OW9woasPt4Yd2YOb98NUk51KS4l_QhCvcOklFtSErXtrqzlpfL4HpTLEThfcIaxDtNzWv_pdI2WwC69ar6lnXWnvNY_7eKcoIyYHBNq2ej8paM4xlwb1kQUyW9xkBv_2pn-czErkMH_V5lCUAEJbLU1oEuVTIoZG0izyTir2WTibAfNsyWTGlZ8TXjLYH8XUH612KM6uYlHRY9_SC7_-ItrshBMmmnyXz9ePb7rOL8e5DfCnsyGA0rOAyg5HlZSI-vrfL6GBSXmxtfgHL0PL7v_cg0kixp-vCRHGtEvjttkHgLWjxlKnliyJIy3QwbfH0wUpmn38qw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9603918fce.mp4?token=RKQruIy1dBQ2OW9woasPt4Yd2YOb98NUk51KS4l_QhCvcOklFtSErXtrqzlpfL4HpTLEThfcIaxDtNzWv_pdI2WwC69ar6lnXWnvNY_7eKcoIyYHBNq2ej8paM4xlwb1kQUyW9xkBv_2pn-czErkMH_V5lCUAEJbLU1oEuVTIoZG0izyTir2WTibAfNsyWTGlZ8TXjLYH8XUH612KM6uYlHRY9_SC7_-ItrshBMmmnyXz9ePb7rOL8e5DfCnsyGA0rOAyg5HlZSI-vrfL6GBSXmxtfgHL0PL7v_cg0kixp-vCRHGtEvjttkHgLWjxlKnliyJIy3QwbfH0wUpmn38qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه جدید Hermes Agent سرعت خوندن صفحات وب رو ۶۰ برابر بیشتر و هزینه مصرف توکن رو ۴۹ برابر کمتر کرده.
تیم توسعه‌دهنده‌اش، Nous Research،  با حذف پردازش‌های میانی کاری کردن که دیتای تمیز مستقیماً از بک‌اند به ایجنت برسه. همچنین برای صفحات طولانی و سنگین، داکیومنت‌ها اول روی سیستم کاربر ذخیره میشن و ایجنت به صورت صفحه‌بندی‌شده و فقط در صورت نیاز اطلاعات رو می‌خونه.
این تغییر یعنی کیفیت تحلیل و پردازش هیچ افتی نمی‌کنه، اما زمان و هزینه‌ای که بابتش صرف میشه به شکل چشم‌گیری کاهش پیدا کرده. و یکی از نقاط ضعفش یعنی مصرف زیاد توکن رو پوشش میده!
کم کم تیم Hermes داره یکی یکی مشکلات محصولش رو برطرف می‌کنه و امیدوارم همین شکلی جلو بره
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lZyStOvbXSCHvlOpOotJTDE3jV9TxvXNLRLOTSfX1uapY0D6k0wGsy9sGqsAi1XUbOGdqVN6Q24e1XVQOSw542ukuo8QmJlnHCIodZIxEfRHC0cXZDmBDwmNkZ47TOLBYwsNPBtz0Rny1CRJqEugWoJE5pExLZE02NHFgs3d1teX6tiQ3NJuDuWUAtf022hGIuIrwW3lstI7Yv1bp7FQJRxNKvGlF5MRijQr-Hd9CDkA8pAW5CE3veNT8UoQhEHgV3ScJ-eceACKBcAEjqtRGTgZKj8xBDxkRmnO_iP31UtrUQ05iVM-xbgP75iZzTYFxHjYvEhIlunWLKTZosae8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6aVAlAB0lWfqcWU1wAveR3C5NPARVqA0pcUQMZ6l5SsGg18wZbDfTrq-ES-_1fP7jgp0mNKCtayaRCGoNWW8HZuYw_BZFnefk_LbkI_CniTam1XqAj2IT7RuXlczsc3Av8M5f-GrpahsgUz5NMxZDckT5D9GC3zVIYgKevf2PVu6YEuHHlDZ91eun0eJLrAPuxgSDks-mw6DeMQR9ntg9wCxyfZvd9hqBWOStJY46klxAjdhRYwwzrWn6jzUG-7JCQqXVTGyX7iVlid7AwNa5TWIVWDUlDyDNyp0FFrQ_ZRTtNmSfJWG9gKpdh_sQFf5X8xgtJMjxvDchSMGGnFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HbQemXVhrlO9WAPjQFFgz-LhfnbsXIqV7BzyQPGlE4XwOlosYFY_JEEN4ZHf4FFrXKhI8Q0lvYbrgW-xXRovFDlv67__YJWHDvdD_DMYd84ManEbAYJ-aG-vf0Dd6we5R_tWQvQhhZSVPxOQXSRQigidBJGBbcdpIxltmPy3Uo-yXmsNqe9lCb3LEK4zHWXRJO9UxscguKxi5qL282QQRQQSJTL_qr32tpL2Idf26OLeRD-0HwKSoioz55CWlaPF0UX8eyUS_BnM9OWpa0pJ9kcPg6A2tmhy27z-gbd_m5jHf9afvbCpBnmwTQbaGhOKwAm96W7ugoCYcc217mMebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!
این ویدیو دقیقاً به شما یاد میده که:
✅
چطور کاراکترهای ثابت و باکیفیت طراحی کنید.
✅
چطور با استفاده از AI سناریو و موزیک مخصوص کودک بسازید.
✅
چطور انیمیشن‌ها رو با صدای کاراکترها لیپ‌سینک (همگام‌سازی لب) کنید.
اگر به دنبال یک بیزینس مدل جدید و پولساز در حوزه هوش مصنوعی هستید، این آموزش گام‌به‌گام رو از دست ندید.
ویدیو با حجم 300 مگابایت اپلود شده , از طریق نسخه دسکتاپ تلگرام میتونید با حجم کمتر دانلود کنید.
〰️
〰️
〰️
〰️
〰️
〰️
در صورتی که مایل بودید میتونید از لینک زیر دونیت کنیدتا قسمت های بعدی و موضوعات بیشتری پوشش داده شود.
🌎
donate.isega.ro
〰️
〰️
〰️
〰️
〰️
〰️
📽
زیرنویس فارسی
🌐
ترجمه این ویدیو با وب‌سایت
isega.ro
انجام شده — حتماً سر بزن!
📌
برای دیدن قسمت‌های بعدی کانال رو دنبال کن:
📺
🌐
@AiSegaro
🚀
هر روز یک قدم نزدیک‌تر به آینده‌ای هوشمند!
📤
بازنشر آزاد با</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ShmUWcmELXb5O8mKENrbJ0i0XkgvXhd4bfF1HvgSW1Ysj-p7LwopVpHoxjuAgGT9BRsG25yPYMS8tuh9wujqXfXCKN9KF82ouORew42YYr_rKZyPpdTh0syJESJlVEk_8iWABixB6ufU3w-KmC5O46LAHmkhSlI9tusoleuFM3-eOUEJ46MLLOGY0iOJsPajE7PGqGawBLQ7OhLSREWRzZopTzza3AQ22GkPy79Yky4C_JNA24ykq7ESRNVl6AKQWejUTT78Ksn_nR9FZd7_Zupzn6yUbNpsYq1T4JziHo7zpjB4NBxMSkDdjqhnM5sJm53v2GIKkzhyIz4b3Wi7ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qxIiGVAXZu53kPkJ4dC3OMyqR0F_AiJpzF_XPsumw0Io8cAc_6RXE7N7fjgBUDgn_PY-uThDTmevHdfamZniX0s8g_YzghzonfbDtRAS6Uz4ekFB_Eet5uzaPfbGY23_usUbGsCYjk0dy8HctdMoQiV06dv6Juz4EylheLhTGUIdTppEmnxNSAuI0E7OjQbMEDet0AhjsXS8neb36BVCdWt9as_SAqw-SGGsnbAZIjVZyBr70vqiLbHKm6iMT5QuUIhVjhXJhtbNkoYsASLY0AzjmXW5jyMu7dRmeqjbLfucpm8I3h3LQre-5S-6LZ0EvBtGsf6z59RlHwPQCRMwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G2WCXiMdUtIC0x2JXAukJBNM5u6wLcJOWAHaEXEgrC9ATRBDueLYxK85phBn8nOtPIosolSOXbT3jJacJ6aYq1c8UcnIlFgLup80QRjj9rNIxeS9XxE0-qwUC1P3Y7EqqBf5MVYL3Xfd8OPHrPequP-UP5HJUvIB4zDOvxdiwM-KLGWQLUadPfJlPEG8XCUpSivs3eHXI4faY_seQ-jBkCaCwr_AObp7X0XexhJ_B_vSyAbKxuq0uDD-FJuVI-cUWGHWKgd11zl_rDjCx8vv_bqB9hu39nkxFGs5nWGpevzCNIlZ2odXSL2gwfpNLNvdanjXcEpLGtGyiOB5G0lUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AIHBCSlOjHNfMHsY7GjwMK0ZZ43v2-qhUUwd65tuU3H6bgeUWwO0SvLQ7XZYqJJs5mJjiMQyCbOWShXUBXfxvOxYWdCJzJe9zLWzVqE27jIVzE2eX1H99FGEfISBu8dgd8X2VC-EhgY4dtY7gKZ9-Eddw-IMtV1LJ0v7W5TlRZz56-tRtMCtdYhxepLuVTVUzJWEWYmuv0N0tvfLjvVLTm8HvF_j6qEmzByS0KYnpiK5VCLNbPizrIqlgS3qEJKEEzhXbv30r80MNl-Qmge2idJZY6aJ3zwTgJKOUKtLMrjOykXhoJcqjscGA1Hz_wvG0xSdWVr-w7qBM7P7f2309Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g-a_mXB5g1e15IiEHHSoIVAokciPUFcgXlvIAd_ZThSGnPm6bnIakxlp95Sr2hkGDR0sYZOOR5dW7fH5WzHkaC60PxqipVs6Q2CRVKnB5yI5QSWb1uJwQIfQe0SIY05nMiAI4svap5HZwLgoUi7oxoxYdkhSzB1PVAlktjF47Bkh3pKt_cuIyddjDbALHB-BZCSIW0jUXpodEOztjuYhjwM3fGKKoMcJX_vui5RfXfcqJD-cYv8-i4RVihYtDLOk9pXAYqW-gELU2IDF24ZNhDKEsZdZCW0ca7MPQQF1jwNEmgGM7od2gFdeSXxLC4aJ6ZpnMZigf6AEJbYS3L460Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMQpRCdUCSh6NrgwenBnmBjZt7Bb6JocM_qCriVbr_SDkz72iamRRx25YjA43BpH9X_UWkGMB2zmDwDDz83HAK5QRumf_g2MTaIp4xVMANdtzrDYTuxkcRKoDo37eDeyNF9zF10aZ442eVlSCrdKOcwNDP36u5zpB7qMyV86Yd4WtJjCxuXlHHmvOGxNBsI0Q0Q2WULWBQw37gquoXb0TxWMow8V-cjF6gmxA_uUfNO8IEXQ1mtza0qd7XrgnIjuLe3FRQ-BvhCTQk6kRHNnmdJXUmS8GCncrDfF7R95ZDVVG3CG4I3lwhsbMXIOu7STqr38elrcVwIjNowyObnVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=YArEGhrfcu5iAh8Bd6CJyKiAmONvsPl4cKm6hPsQNQx3FzNCnlpbqmRpy0dToBvpvVMbu2paG5N-E5b6jEHoFbQWw48PEzydDAnhGXXwNNJwOsc2WYn8Wf0gPN44p8q9hgeHOp8lEzM5UXzvQt8lpC96zxwIYIwmqRypIAQIsFO1Ss_lR2DHH4yl_e1uTQmI9UEh2Pv6Bot_TD6bkhX63QkvdqDJWLxCQ6v9xdGO4g22UsdDakUkJ4LUwb50q8nlnZWtYSY4ichgHAKEjXvMsjIqbCu1Vtc0NgT4wtU06Vt3SKpyqWg6ydzGi1K_AEuW15Xq82luJ8MpHZoHQJnd8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=YArEGhrfcu5iAh8Bd6CJyKiAmONvsPl4cKm6hPsQNQx3FzNCnlpbqmRpy0dToBvpvVMbu2paG5N-E5b6jEHoFbQWw48PEzydDAnhGXXwNNJwOsc2WYn8Wf0gPN44p8q9hgeHOp8lEzM5UXzvQt8lpC96zxwIYIwmqRypIAQIsFO1Ss_lR2DHH4yl_e1uTQmI9UEh2Pv6Bot_TD6bkhX63QkvdqDJWLxCQ6v9xdGO4g22UsdDakUkJ4LUwb50q8nlnZWtYSY4ichgHAKEjXvMsjIqbCu1Vtc0NgT4wtU06Vt3SKpyqWg6ydzGi1K_AEuW15Xq82luJ8MpHZoHQJnd8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SMxMEJn2p5eaObEGed5Regw9DjoC3YpfFsUrA1yuRKrUiMOBZG2jr5ftBTPj41RlMrffkxxIbDLvDXnpDu4VKAUAU9XTyRhl2K7pkThUtd4iYfkTwsvIHCfSHCoJphW-wGM45_kgj2LAnZTdE24dugE5Xgy0f8ks5as3-CUNTlbMXEs3N5JBGbdgUIh71zJiVpvJeFz6-hmJfmyMXsKOQAD1GNqNoYALAxPkdAFwgf1dsQhFDAI_aqY9jUYkPT4GnbtcqygDRcow9vX1FGlH5NFzyBD1p2XpTzGPqTYe9F9IldECBHjpss0hcVdG7iX4LQGHXFZ6f42gmHF95nWEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router:
https://9router.com/
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم
2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم
3- کلی API رایگان وصل می‌کنیم بهش
3.5- اگر تیک آبی توییتر داریم، به راحتی از گروک 4 و اگر جمنای پرو داریم، از AntiGravity استفاده می‌کنیم
4- از امکانات 9Router مثل Combo استفاده می‌کنیم و چندین هوش مصنوعی رو توی یه مدل فرضی کنار هم میاریم
5- به ChatBox و افزونه Cline وصلش می‌کنیم که هم بتونیم عادی چت کنیم، هم بتونیم کد بزنیم باهاش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگان و ساده‌ست و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZAzhzGq1UmBNnxyd95uXQk0V52cFTEUrkMH8RoAwL8ZG6KT-9OjtDy21Iq8wKAp4HMkZz3Vt7HtrNgSDNoFM1FelD9odGIM7d-fMKMOrGUgXjldL1T1vm0UyLe3X2yfhEYKqpVJx43u8TpzZkdNtD3QCPVrb27XWQitaJ2mzAqLdD1XuK-1Ao0xaAlrwqNs_h6dpoAcTOXw_TLIC-mcrTyeUw0dJNiAjEQGpkHyelJv2yce28q38mijt_M8MQ4iLzd6V_2nVcURxlqmJ3veC4UwVn9gRzFndkOR2QEBQt2HdUBaCsOWPgv0iX6_um7BYbSbKSgspvUe_reJQSY2xHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4112">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vO-42ke-Cii_w6ZrdoC2wJ4g82kXz6rpfV_6ra9tucU30NSvI-rXgypEhlxkjyB7brkQEVd42w0AZI69CcLievecMaGfcNEl0V6HGmomJCkfoII2nIzwPNvabr-lCtywVur0cC3Hj_Ac0gXPSrI3IwW5vV45xw8wLhDCEnOCTfUl4OvXRZ2TbLKacrZqZDmgRuD2GOp9N346RgaWtDh9DNFpDK-az-wSCvdflijAI1wMgkgHhTI7RkGizc-h-qvEe-cPeEI1JXDOr8XDnSKna8B-88GxiZYN1r27rHD2l2cSqa1Ow9Qq3YSZLAq6qtAlC_LXWKaQIQaAmOz2-biMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r8UwslJboJTPw1kEJJ9Qu-v0ZFoGls0tVyf_bb1_9D-p5yUv7CKhiHTWVGrrPKeUg-oBB-0P6BfvuMVzT_5lJeRpPKfifLJ62wltJHxbGH2ZKmZfBc9b--Nq1-TlDlZ91qL5EgFa9yRi6p5ndhGWdQTlvVl8nv88TZr0CFiqb_PqJCq-fDz7GDhuscbGAbcLX1W0_2EMRp4CLmbzB6IaXfYuqp9FbXKDwgtmu55r7U-7lEjFW2Hkdw7IJtdoiqJcN9ufXkzb4Q1jiMlY201YoAgxCfhbCqSJt-kteusde8eaukJpZPjmRp89cnFq11gQUeu4adHqFfHLYUc2xeMTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/je4HW2ZEhBfrfUijxx4ope0zSybiWXJs6kcFVeEGbrwcndYpUxxLt9iU4A3ZWMSUDh0C0O0q4PdYgTITta-KNW84bNrl3ZsXrqTcmQQRGAsjMmylP9fr53qbbloLbOwsNSEs9K-mwlOMAwQplIXwlb8n5SsieQ_6BflewYM3M_hIowm9JPJcwCKrDMhp0TwiFkVEFsh2vu1Voow7LlKTAKiiNZKDSmZnoLoFqaWPIa8xv9L0snim446dKfDWr2bqsI3a9t225dZuha2uaYf8kONE1LsT9ytiC8B6SS0mNDKiRvT5rqAP1cxWcDEA0XmvcKZvGHOeWKqlW3BrJlMfOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی واقعا داره پول میده به یوتوب که ایرانیا رو به دین مسیحیت دعوت کنه
این تیکه هم از یه فیلم بود. دوبله فارسی
😂
😂
وبسایتشون هم بامزه بود
https://daneh.online/four-spiritual-laws/</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4112" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4110">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k_pYwZE3Q_OluVQMlljHIb8_7BlZeLZSAEup39d7b5g1-5fPZiSBawI1TUz6uT3oamoeAiRdnl1Eg4q5Yydp1ZC57td5JNtMg0WBH_EmOHqRNofKpIzmpRfmlrx9qsf9D4_KOBkkvFyy2MWOW-eUJ29QnaKD2ETyNSo8z1UIBnPdR52H9JsIOoYHnY9Ldd8PGsfLZGZMztThko34bCK5zBAs0-ex0Nxsn0XzhkXSkqwguGlzgpMnLEjuGmywBpKVvfrJsaabJXuUkU_GAGtt_3TFa4fukhShxtbGEJ02itXlic-vx2DkUzRLrVGsp_lSTbttbB9TfKO9nkS4gQk0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t4DIOOK493MQe1PT9VCr_nXDsvngsIAflq7rD9GvE-EzOEu6G5Yr0yDKY5j-QzCbc0WYmar73UZlDdL3uyR8-Oq9xmgjb7Gp2pmgReS8bM0T5vGeSb8rDaKS4hBCWBrBFrW9cCLHQCdRtpMldAYhetuV77HKqGVZ3zeHM8mGiU3oL9cWDL7Mv0aUw8evhpKTe2ZKv0SC6c4Z93jtPFfKF-tIQiiIaxQImIVFSCzl1P89Bk8W-WmpXwSt23vdUa2697RPaUHqWJnfWeerqLZILJbAOMEQ3e2v5zgyxYl9U87nv5D451808bYlgo0S3Mh0thfgqZw21vXDGAFT12YNMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:)) همه‌ی اینا برای یه تسک ساده. بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو 10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4110" target="_blank">📅 04:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4108">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ddDd11XtiXgldRWJNOtkk9ga-yHarc5Kez2HHedhLiZZy9G-9gBgwXJvdQexwaXjZFLEOO2RfdVsIChudyccZIs_guy3KCh2aq_IEmPjHks9grlPha69PWEC3KKSTxYWcjDMtqvp4-sXQI4zjrtStpTxh0rnt1pmjE3_t0A_xe9YtV8kmrbvRuI45RtwEtZ2RRB_VOksNEDiXUqbNJ8opmdKAePdaCWRcXRyrffY7IwyNjCJOyh9W3qphtcwjeBdF_qKwZjLOAB3tsm9bg897wcd-b8ZQTDTYYtGg7WI6y-JzZgGwkifdJZFaKR8zdyRGsLJVI4PCQIM1dF7YtPfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bcxHaZfmT04M_3zOF0ZSUHbPOtb0vAmj_mP8dPhFc-xXYaP57LrRxqevkzwe7n_DWIGAPd2dn3QR3Pg-Da4pi9BqCfh19IWDgXFTiewwtTd7456AmIrmzbYcVFn1Fdj1quhARowBbzIgLJDWVre_7_yKoJJ3J4ngbucalbbbD0IfDT8BfrfpeSbtLJAWoRI-Rr3i2jd567D7ua6T4ZsA8HQ3vimOGHqmWRlga6vNkBkV1iVJv9F3xUCeYIoHd6tgJbDYO53YKX2seUFyhGAbcAUGxD2CEPHKiDNsu7IDdV9de9vPj4MVut4KdPNphhAk3CCRZPegubplNJbe-Kdo8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:))
همه‌ی اینا برای یه تسک ساده.
بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو
10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی اسپویل طبیعتا)</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4108" target="_blank">📅 04:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4096">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j25gnN45XWLX7Yi_2Bd5XqGLovSlyrwdEf4Y0mA4iIq90WcFbOVo7mMwtZimWad__mR6qC35aroFdgmc2JoOe3-z3-M_lXao1clGWDs_nHCskQCFSfhSydVFvWEbkxak2lPX9iumpBNOrTBt9OF54b3xW4wzcLlXB4iuTS-zWY8G9FWyM7xlv5rCe-Ahop5ozPH0ysrHY_FuhQZXe8DV9FUOnaQQDcnDBX3vxulrbOs7ZigPdJTCvSp5kdRyBKMY3copxtD9sxLOTI7rVoc9nHtDttps3bg4bazlJkoej3YrLPyNG-dvcknhgIpOSyFfZ2jPexTgbA0_ODQJ8bIwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CVhrMfYhSAW6tnZ88VKM9TzkWqkRkfYxbI3ein_1Pp4jQNHG3KEm-ujX5oQ4Rfrf6_THzo6jwoiofwduAPEtYHyUdvqZeDAyw7J5tVf0XK7d7lV8J2CucX3bpzmKhu5CaJysExhxzC1BjdV9JjuxY7XM_Gj8lJws5_mkd43t1TtLIWFBPU71hTF0WSzavchjalnWR3Xe2xx36FUbVTIpKEBdnM0T5pxQkXKuS9qr9ZKqBN3MDCvOF8BGJZuj5gT8KKXKbiYIxFVDykSN52PKvSHCUx-Gldhqh_Nz0VkgW5SxCU9u8wfEbzG5YTWBVxhX00t2zZmFt4UKD6UBZ9Lipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lpFWzkmCtcC5PinGCWxj1VyqZblQHH8tOUTJ2VrM704EZxNZK_scmDGkcX159Hr1NY_yLQZuv0NPS7_Fq696MTzy8izNZ9A3gZH062PmTEwh37cmsBt38uhx29_I8cYqS_gaj6awZHujQS1mtr4jyUyWCFqTz-wVr1tC1eNI45BAS5c6kdQjMLb2J5-_Y362alaqh2GtjDlrwVDGlLfTEpCthgrLWTHkUA5deX4QC9wDn9TA1zsWcJ88786sbbiOVpaMkgdeBJRu-bltPLwdUtzg5SONwamowT7spbWQzziIluAcqWr9ky7j_JEeNMG2NyBfzLbb06Uo_fDqC2mG3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eOB2RDz2z_EsGs5-g4eMXJglFUuXjFRVG-pbmy8f2QW99uPbWwWLV2sIrRso6RWWsqvVZgzlvCmfUdKSgk8KTm6rJZFJr-8w9OQ4IO6Svpca-ol8LMG9JV3KDL8u26narXPuthO4LvA8_RmZQkRpFtS37SIxo506YwHFw9hNo4MtHDJTaRzRx0hva-svQQCsIsyJk-vgBeiKgmk2HsY5N0TyMIug4MAW6ZRoqlaFHmPbZZXVxHrazxG_5v44aLfHq0uELzFXseJoX0TG_eaSEKI-5XWd25jdlUO5rkvPox90oFMEvAs_oprdi0K7UbHl4bwzNuhPyiSvtY5sIpUSmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R3HIyI9IAab6fZidN3X5xWrxkUxShXSmJqXuNBLqS8lMQI7Cqp-kORFxNKUHghV_2AgEXMAKFWjWKo5X78jxUMQz7L4pYPsbXTC6LbNuNYsSDfD8Q1Anza4Zq2opFMYjl9YqCKPpr4zn9wmaE5KtN_dYm026YV5QselbnDrOu98_uSxgfBFbtFhmE0j8aYH8BIrMaJLJCnYiY4K9urkfOQuBka_16QAy9Tv9xELq3OatIr21Ze1-HIhucEi87D4XLJ__mDAPIimkOMH-hkTsb16p1voZdoq_imQ8llrf-xIj43JEDwB_RBLJCzcP2GdX8h880Bi5xoHiEuPY-MWg4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4096" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4095">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-poll">
<h4>📊 بچه‌ها آیا نیازه من یه ویدئوی کوچولو بگیرم واسه‌ی طرز استفاده از همه‌ی این ‌apiها؟</h4>
<ul>
<li>✓ آره. بلد نیستم👍</li>
<li>✓ نه نیازی نیست. بلدم👎</li>
<li>✓ رهگذرم. دیدن نتایج👋</li>
</ul>
</div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.   خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم  در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4095" target="_blank">📅 15:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4093">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k1gnBVN4iD7tuOfMS1SuCnVMaoD6-jlxMWvXA-xpARqGrk7ppe5lqzK9H9Zo6fcc1vAi2d0huQs1LGdSzumuF20x5Pcciegfa_ddpmcQ5eoLYnkVCuTh151IEpttJF6JHHiYveNggWSmvRe_MHQoC-vIJI4VJUrVQ081yGDmUMm720u4jRuSDNM_3yJ_pLecZINI_47MOz0yknUvanjKuUSvVKFqAzPoBrxtN2sSZnQbFG5O4sC7eM5Pz4puC_5e2pN2ffteVB7DWesSN7ljF9uVodjWZqiOsZOhToQkZVaEPSMYza9e13I1SIGhGzaO4e-NZimqnSvt6slPbCUG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ULppBtnZLQmOdTmQXiAX0g5w_wrBMr7uteJM_nju3ijzGdf9aNVY-Q3ZT9n46M8fO782U1HA91Kyg9a6QmOmnB1lXLtJBFtkrTjl6hiSgScOdZ1y351pLQELZ_E2bqQYYaqdYP8KnZ545OPOkCRP8ZDHLx-O9J1uokoNW9MmDY6ocz2fZOpldXj_0YVb3l9W41jJoLQQ2qPkUo03xgVvQzVk-6SC-_8ymj5fzZiTdaj0JZ4vb2gjsMDas513thAf9EQTuQHHBwEW94Raj7ZyQdsQGEU7FytR13IOO9JlTzUulfvaNYc-IfFmpDpVhQwNex8L47PlBxCZcNOz8fQh9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اونوقت واسه بوفه خوابگاه ما تو یه روز 30 نفر کارت به کارت میکردن حسابش مسدود میشد به خاطر تعداد تراکنش</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4093" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4092">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c7DhHbzM3nljS_7_mdY4_UCZeA8U0c_OTsLbV-44tajfN8RVtOY24jBEtFZp-5ZkplR6H5d6L7ggUVC4qK7rcWFMRfiUjeKSMbC0Q2WuYiLPF658RbJiWUMBNs65DIHpqNAYRT-BWZqcERCpEW11fteuczC7mnjCeN1aG1u_sN7tdWYZgm7I55IH2F-NM4nLUOAFWdZDzcfQbGFe0BMx2xQd-p4WV1R2aVGh5i37UIXOP9bJMavcz2p19M4uRVLmmuCzIFcp-AvK8dErU98J1TzAaKSk_E7nK7-2TROybP8CIdZhRERt9ZC-jI2Wv4-lNu9JIkSvq33uJEzrf1Yu4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.
خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم
در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و یه رفرنس خوبی درست بشه
این لینکش، big pickle هم برام درستش کرد دستش درد نکنه:
https://ez-ai-access.yazdan.me/
✍️
Yazdan Fathali</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4092" target="_blank">📅 14:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4091">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر api رایگان پیدا کردیم که حالا نمیدونیم باهاش چیکار کنیم
😂
چندتا نکته:
1- اصلا از api های رایگان روی پروژه‌های خصوصی یا حساستون استفاده نکنید
2- هیچ اطلاعات حساسی بهش ندید
3- توی env پروژه‌تون، api key یا... نذارید مخصوصا api پولی کلاد یا gpt یا چیزی
4- حواستون باشه که به جز شرکت‌های معتبر(مثل خود شیائومی که mimo رو رایگان میده یه مدت)، به هیچکدوم از بقیه‌ی سایت‌هایی که api رایگان میدن اعتبار و اعتمادی نیست</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4091" target="_blank">📅 14:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4090">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oFoZZEAkG3LcI9_GV7DVpV_9gwV0I-nrBZdy7EcVwK10NTXycNHymULmYwpZEkluW_hXKqHWoe6AoMwTq9jMjO7zvgjthxcQpADTeaV_2m9skz0-WIQF1htZ1Kzj1q6fw9CyHHce5D_HE_mk31IRS9YkhkNTy0BToEgBSfBhPAjcP2GRMZklt7D6UeCgoOdviLOhoDQbjq6ELrLihALLIeTRE7ytwvOFPsN7INcoQ1huNNdzJb5sHKqeaXu5Rvcaqa9NPhS6XfRTDdgk-SIt4OxfT55n1bxFeF4H7ey3yK_tKEMhkwO-q0MmfLmi7d8e-SGRSLFjE9uv9qqz50bV-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت بامزه پیدا کردم تمام اخبار جهان رو با ai رصد میکنه. اوپن سورس هم هستش
خبرای ایران و آمریکا رو هم می‌زنه درجا وقتی موشک میزنن و اینها
این پروژه‌اش:
https://github.com/koala73/worldmonitor
اینم سایتش:
https://worldmonitor.app/</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/4090" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4089">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4089" target="_blank">📅 11:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ftn_Y-jmIyVXTn_Y3vJsQX3f3YhzI9tt7FNar_5iQYxJbQhI-LtSIf2K9V9iIL5RjkjaJFJV1sI97UABBEyQcKSY5tjeSRzNzAG3SghGDSc7q2i9rVBPda7f9F9-K_sbYyztUYMSSCWEMrnM7veT4OiHlul6JpCcjhsx81AHFPq6uWfRgif0kX8SliyyjPN0mzeY-ieczcdhvnjymkkRpVnDtK-uInow9ka6dK2WF6jkqAgyHVLYQG58M3lEnm24YD-q7URz13tcxZWDo0QFG6Wwcpe9gSMeOJ3SxfKjaF5Sm7w0gFlDnwa9jitrOt8fWoOVpr0krnDklHKULuartw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم علت بن شدن دسته‌ای اکانت‌ها، چیز دیگه‌ای باشه. نه فارسی حرف زدن یا ایران و... .
به نظرم مشکل یا کارتی که باهاش پرداخت شده هست(که شاید کارت‌هایی که batch payment داشتن رو تشخیص داده و اکانت‌ها رو بن کرده)
یا اینکه علت دیگه‌ای داره. چون خود خارجی‌ها هم باهاش درگیرن توی ساب‌ردیت‌ها</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4088" target="_blank">📅 10:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4087">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیشرفت ai واقعا گاهی اوقات ترسناک به نظر می‌رسه، اما من به شخصه باور دارم که نه جای متخصصینِ واقعی رو قراره بگیره، نه قراره اتفاق بدی برای زندگیمون بیفته(به جز افزایش قیمت رم
🤣
)
در کل، نباید نسبت بهش گارد گرفت. نباید هم نسبت بهش پذیرای 100 درصد بود که "آره ai خداست هرچی بگه درسته"
مخصوصا توی برنامه‌نویسی خیلی خیلی جنگ و دعوا هست و می‌بینم که کسایی که به خودشون میگن وایب کدر و کسایی که به خودشون نمی‌گن وایب کدر، هر روز توی سر و کله‌ی همدیگه می‌زنن. که خب صحبت طولانی‌ایه؛ اما
نه اونی که می‌گه نباید از ai زیاد استفاده بشه اشتباه می‌کنه
نه اونی که می‌گه کلا همه چیز رو باید سپرد دست ai
چون این دوتا دارن راجب دوتا شرایط و چیز کاملا متفاوت صحبت می‌کنن. و این وسط یه سری سؤتفاهم‌های بزرگی پیش اومده و هر دو دسته پیش همدیگه منفور شدن.
به نظرم با گذشت زمان، خودش درست میشه
بازار، خودشو پیش می‌بره و پیدا می‌کنه
و در نهایت، کار هر دو دسته هم مشخص میشه.
الان همگی توی قطار پیشرفت ai هستیم و صدای همدیگه رو نمی‌شنویم:) بهتره صبر کنیم ببینیم کجا می‌ایسته، یا لااقل سرعتش کمی کمتر می‌شه، اون زمان میشه بحث و استدلال کرد دقیق</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/4087" target="_blank">📅 01:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4085">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یادش به خیر یه زمانی مد شده بود می‌گفتن Prompt Engineering کنید قبل از اینکه با ai حرف بزنید و یه سریا دوره برگزار کردن کلی فروختن</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4085" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4084">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c2M91AXR3p1UaLaAhmnHAHYBl5O_zpT5CBPbtoIGuQGPy11aaXy6niK4nktUbWQlqpPnZG5w8kWHXOEWliyLgByyEGQ8JS26yPY1ufyDFjNH4OGzWPyqgPwsvzYzhDCEABY84jW5KB-28sAhq2PwBqKpGEr3PTAkcKEvY253fbIwwcMmjLu_sKcaSHHDcaLmv_6z9qjw6XKPo4jsle3lXsJBSu1ofPoGYAy4Lk5Rdd0RAIj2DqMJ9ZdoBalffCoLh6-c8KW-CRX-GujYlU8zlhXB2sU1wSvioO0qFfgEEV0uWjCAF8JaMnKXO27Lwhbr9txyCrj9qGuzbWrrYKgzHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید اعتراف کنم وقتایی که حوصله‌ام نمیشه یه ویدئوی یوتوب رو ببینم یا وقت ندارم، میدم
جمنای
واسم خلاصه‌اش کنه
👌
attention span در حال غرق شدن</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/4084" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qrigr230gLxbY1nTvc1Bl3e7AdXK3g8UnRQuOyJYGraG8cxZn9a8KVOS7NHAY0R0nJeNYs-ZefcTym_VHNyU3-J-TxlPWJ-qKYdFCXX55j5RWNrTB_bf-NNidOpD2UPJ8i-0N7kK_AH0DjWUESAZglMW6LSkJxqioLjjJUE0FJA4FM9s36xiixtkNgcMHL8d0UaK9-7Ry3qQEBlimq4iXYkHatpHZx3ED6UHxlBKjXVyXEunVP1Nr-emeb5xkk_v9gE5KVXeaF_Ubnihocuy0eIs3vrmT0zoqeUs3uUAHIp4_bxfg9_o-nH5D4FCqr4IOZC7ORv0W2Vro8x6fqdiqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tNxWSOS70L2-JGteQWEmOpl6zmVMezyxPHpFbbsapMnolYSvmQtHhwbrBd19Q3qUmACPWzLgPX3AfkA02iPsHwW61CyWeX4qWMd5bH3adpA_JVVN-JMv3Tc439KEsE0UFlWvYXnDVfoPeIPsc_Qf_2B3b7ked2JThlmFRvjbJ_MEC28l5qVt5kRmn8y6oiYI3bHwmNoPyCT0qYm6OBP8Ad4KTk4pK9kewUG1WQgK85bsznSS716W7EB6tdUKomsmwBup0eI_kl3B7y_SadyK3WZ5cMvT3JXrFBTZUrzUL1ZOCEk5JmYt_tF4c7iWhboSdxwDdlL74Und8XXGfOOrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d3Apfre6KSLlTs5im3v0Edue7MlKMpEAUFPED6FlTeiO1dDuttDYnfMdXW87ceFpmwK7cttbXxmV-w8ijIe7_jQsfCWOcjdNkmIEHSNFdY71ODNZwVE_jAweBKJdghLo0ZoVVLMbnnn4Tl2gkE8p-MT_iVk6B_0zQcrp2jDHgR7qK2nRuFtH4r7xq-C5X2evHPk1a3wX5Xl66brMMu7CqB3NwB6GhaEzFaA2LM_bQer87kxUtl_XlmTUHG_Ukd3lZK9NyWaw9PadLUHwcOdvajh1xQ31vjSGwZDoLCztvQPt_Eomlf_jdJFX6XHplkJQLQVjPR2Rd2V3e9vYG9SFDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
