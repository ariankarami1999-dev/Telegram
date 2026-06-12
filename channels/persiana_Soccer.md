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
<img src="https://cdn4.telesco.pe/file/sF2V53ozbzXl-taL4NuNsMvbPCuqRq4e8CHmZc1gn630fchu5wAyP6kpHjmyTL03rQdEIw7gXzuohdG8fPsDjLP9ytys8hBzI5eodnmLXChIlwongGojXctFNGAHRNWiXMH2qLXlU2sGudtY6xOKRHAC9TF1-08WYwd_hJXwTVIzV3-TqM4rhs162bL3u5NKg46c52s2rj_H9d-fXQ6Qhn-MqoYz9PP80pzVyxVIQP91NnXhE3m9tTIGEk8oCSTtCWYRNbrd-toI_nzhGrzWvh5Oggorovcbr1CMuUAU6UBR_ibrHRE3TMDvAMuvbZlm48YAAsZ6eVxds-WrfMPJ0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 247K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 22:28:47</div>
<hr>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVgxPAv5tVJkOhlZE468VOR4SF-SPMgT7vt_dR4OBouYqgKGgvsdLBX_Uotmp1EY9lvyQKnKQeggGdboDIzOUe4br8rZX6wuUPN3jZ-URMSSVjQwaOn8vBEDILLm3t8mm2qbc2Ce964atVYIKjE4Ca36zZ5yblot8IJdjRr3Vkw68jK5l-vM1JB3wxnYTku8E-nTKNu11Al_hpiYLiRQdbSf7kmv83pXPYuFNQwDg4qkMaQ43p4Td-uvteMOzFbCiPqE5n7aCzkc1fyVM5aMiyu4WBcumsQ9XfaBsio7rVaNto38nxTY9PatrX3ORfjkHlVQG-mBoB-Fj8tbiYbVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌‌اول‌ مسعود پزشکیان شب گذشته با سردار آزمون تماس گرفته و از اوخواسته‌ضمن عذرخواهی بابت استوری که دردوران‌جنگ‌از سران‌دولت امارات گذاشته بود به‌جمع‌شاگردان امیر قلعه‌نویی بازگردد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/persiana_Soccer/23302" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNqgMmXRqFL7pSIkWVgVsjtJR5pOCqjvEULw0R5NHO3A3de5n3frovK5_LWii17I4AFuU8sipxvqKvpM2hQoHA6ko-QjElr_Dm4VecUvtW4gzDV-ZPbsn6grw6ZmkQvduIZwSDw00J02alvByEswfzavBQ5gXXgGjLBnZH28sTZCbScHipxcT6EedrEe5SBfFc6fYW8E8UwKhUm_o0-T_7h6RWVkYF0dkov-21ukKMZ62BDliBoh_at-ghTS6ZpNTzGSr34DiAA-djPT8WFznUpjuPyaA22M9pcgZek_fxEJGMonpGSZHzhGR37F_QTzeaNQOBQ0XNKQzFmc-o_9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
|نشریه‌موندو:
دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/23301" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmDY6d-v3lkO1D8uQAywztmSAMtRZpmQvmy8Mbvf21b_TmnJwmE3uqxKXeWPE0FP87k4SZfb7V8cOaGKxR620guTuckpFsrr-yp-QQiffYsvNrb9bOErk2z4lElAVN_XIlSTi387uqubGAFzCwKO4_kGcPgYT8sBSVWwvdv6mCVZgaQ0_CaoPbxLQq9S9eGAeMb_dZnLTgh4kvuXYQLaZThPpZ9aUtElofl31i5IypDWzeAwo-fdfrp4HVF9JLoim9kXKtLhAy9e3r6ABRxcWU9iOKgUsnGWO2Zgk4f8_54kTFm8rRyfWY6JjbzGAeLr6ExkAwmnlxtGTfL2O2qYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا؛ مدیربرنامه کسری طاهری هم‌بامدیریت‌باشگاه پرسپولیس هم با باشگاه استقلال مذاکراتی داشته. رقم پیشنهادی باشگاه استقلال برای دستمزدخودِبازیکن‌بیشتر از رقم‌پیشنهادی پرسپولیس است و الان‌همه چی به‌خودِ بازیکن مربوط میشود که کدوم یکی از این دو باشگاه…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/23300" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیدار کریستیانو رونالدو بایک اینفلوئنسر که بشدت طرفدارشه؛ دختره زده زیر گریه رونالدو بهش میگه اشکات رو پاک کن عزیزم. تو خیلی خوشگلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/23299" target="_blank">📅 21:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjA1qL0Ntk_uVzwY5W5vnE4tgNGfncDUxzG4HJNuab_cZxx_rouj0oYJRDC4DYjT5pqkeFWgkv9_H0d7azNtJ_9PJLtz7LGexHJ9Gypai0U8JcOzjVJyv8BoarrEWPrCZiZvX6cCL4ALTKzPiN1wsPzg-e664wcxSRDcKWvbYyJvbE0JJM0obX4Jc9aWKmX4UbqZrOEQShq4nUSeFHwifpA9owbxUUNYwDNmcnBPElTBAGffpORPUKIwVuaiDYjriDzhvYl3VnTsffSTqvf8_FYSsGN65eKhlpOOWZH4qs-rO5Ck2ttIMOTVW3aHzj99as98LlFdbzrPbxQHGrhg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/23298" target="_blank">📅 21:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kz2aNl6B7zkEuGBQ2DcLVQy09Nt7AC-oDhgXoA-ASvnhAR2GBGt6xULDjNGmoPigv3qu0EP2afxSOaU4sdnIgJz-7_wqYGmaqdVbdVwKpFpAEnEx938SalljbP0RyJlTJdVdi-Nrs6gCfdV3U9MxVRX25hQY4H947_1U0TlAq5rQ5mTsSJixgsiNO_txstMC1VmePx0VqKadt8vvFGOPoh8g4rSELDx1LrWHRgAQjnPKu12qGRbYBxeR8CdyMGXvr7LwOWBKm-eAdAgUfTXfjx2cL_QLNtzmbW3QMIs9RZUG_qff_Ffk0mUZScA5kGgMeUxK2g2xY7XVw4OpPsFNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf186UZeTroH159ws62VF4IzpN4yiqz1f7jgGdVgxBFC7QmsRUMw36yqfPko2keXaep3PleGExBTFYuGMvx-MAI_ESG2rVXDU6bG93EePfIyR_DszXqtmyy41garAKTJxUHx7gz7Ll1re4ZwVzshdb2f1-bcCst_STN5p27ExqNaZjgbzkA5dVnWLTnA-qJd4JaThjJgdpB7f7lvveBQ2r8iP5boaaR6wmNkk0fxJg_5juQW7XYIXxm--Bbmefh82N3413T4TCXSX-Q6YvUtMKAqPsgjDT5g8NLLRBvpHO1KA72sFUHQicURVdjd2Tm-87ATgKD7yWoTagFHWaTOwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/23296" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
آکسیوس: دونالد ترامپ به نتانیاهو اطلاع داده که زمان پایان دادن به جنگ با ایران، فرا رسیده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/23295" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQvr_JHzJK9U_BqI-gnq7Ryxiwc0n-hJKKCp1znbROu_cNhOqITx7LpIB5RsmWVmNOljURBUlx7eqA-QXFKFMto2sEjZx8VRn4ReO7091gsWxT-mQ0N6YXKYG06VAyuAM5mQsFt_K5iPBJO7wxxRL5uzas7vw7kaRTUWgyRKfWomkJWhtd0F4qohSEI4FpbNluZXMc5Civokl2gmd5BtvKRGLEf5Xeqfjr20Tk5B8TUxjizoCme8YC178Pv9WJ2RWTjrfbWOYYn_NYEtL6jA0S_jofOjG1nZfxqUTUc1WuX-maO8gJJpLzBXx74gbAMD5J04Vi2L_kP5KqLLuXpUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23294" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23293">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپانیایی‌صحبت‌کردن‌جوادنکونام کاپیتان سابق تیم ملی با پائولو دیبالا ستاره تیم ملی آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/23293" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23292">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EayyDHbwUp2Ti0oyMgZahpe6zbfI5peFzWXGweiNAkbSNTDltVoYFh_21BGqPAwVdkzw6NzXqDDcwowATSFIjJ9R7h3iuk5AiPA7fCMA6upU5NrtO32_WSxyKr-t_UbdMZ5OdauyV40VIbBZ_yvehyBuzIiJK6dLl1rh-U9na2uLp3RgvErR-FkE53RasDiGeoK7FoMdX4yCZKJRf7Vu4Q6eI3tPSPCG17alYEp7-6qWFLCVxdY_yClHzWjBMbVDmO5Hn1lyDmgpKRVZamqNdACcSRkqiOqTUdgdhrL6P13Ksp-4rltdciEai_HxSB918HwhPW2EVY5vbZ3bP_j_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا برنان جانسون هافبک کریستال‌پالاس؛ با لیلی فیلیپسِ پورن‌استار که‌رکوردسکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/23292" target="_blank">📅 20:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23291">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5d5FmErc0ypnl0SNWSBppAKhEETLbTwT_fbH8q5RNrG0QlXmruQt5I0Zfivtoxg_TicbuEtivJkCetSxqIaQHQ27QsLi9voO4vZuTwPtp2by4VDHx87gxmCxuafVygwItQaBoFPS4DPnB0MGzrJZb5Jp3J4K0k_fOFXeWICRs8Lgs-t6VEW54sy1tah9C9Fnx4_3e4nKtez9R1XmLlhzUsuCSjsMsH60p4yRKV6x3VWjj_J1N4I9LP2ekx8JVIBEyZ-XHbrKmJKszlML4Q9N-6apsJwGhWX87RgzioQrLy6ihcFTvlQM342HAm-TFf-bSDMsS4yBDofbqiqaO4A1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌‌ بهونه اتهامات جدید توماس پارتی یادی‌ کنیم از‌ زمانی‌که اگردوربین‌‌لپتاپ‌نیمار روشن‌نبود، اون الان بخاطر پاپوش مدل‌برزیلی پشت‌میله‌های زندان بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/23291" target="_blank">📅 20:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23290">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLJ07fZMpjUqIa4BsUpcd8Sy7O-2vhV30kgm9Bn2x4QGBRIGNU8BcFKoGabC0Dxyp2a6y82YbUIXJ6aF7O1er5axMTZgjtsxZfpz69ZIkl5v63VJU2GS77VV_-FHnbI9dSu5L03NXrvzpaOF_n1oOeEaOKdmm1u43LEaXBYFzFam6V3f2m_NBOoME-gTcT5iUTAHEvS0I58MxpUcW9YkqMpp7ypgHJpNB0GEaCY4ZgEjG8WHpAoe2qWs7IqRC1fjlchDVIgRSj0ntmLDDMncQYLhS-1Gf86kZNLzpLvgZrXzaodnYhp7q59MRTtE9CSlqhmp1Sog_4ifd33pZJ5lAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/23290" target="_blank">📅 20:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23289">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJky9QgM8mtY1dn-aFQCQJ9cgChY0QY4CynLacVsCD_6DlFUI1Bkumr2jV86JbvMjgrvd9gbM8cEi8_t6AuPsJ-xmeqpS3klIxQXkDrboX6yQ1jSsJJvoROfrH9aq9VlY3g7cT-QJA9lmypgmt8bJId2-wF54ThkN-l8pvzsW6MoOfKNr6qHR0hozfCPJWjCQ8Dfwf37pVqO2A-KQ3tGqwmiseh8SjwN43axBPj1YH9LEzW9OSyYC0MO20ADd6gnaNL6gJq82HmWou_jnymgYksam22YR8lKNh1EEeC-byFdBixo3ZSVhBjJhJ_96gQIXp9RkVUSKscBCWYHp4fohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛شهریارمغانلو مهاجم‌ملی‌پوش اتحاد کلبا با اتمام قراردادش از این‌باشگاه جدا شد و بازیکن آزاد شد. شهریار فصل آینده به لیگ برتر برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/23289" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r06agJUP4QT64g63xhmysjV-5xe0VMYEZ6gIBT4ltVcMy-kQK-NlnlvPwkwk3ocQY9436bo2zTP4d4I9YGbJbZqGibWze5Hpwgn_qlVmk9eY820mattF1IGSx8pReZiM3DCxdSoVQ-_esCq5VKmEMUVbsZ_189bdk4PUdGSZxOfXWb33H7d50xd2LA0xo03-pRiTqTuJtooajnRy1f3crxbUGEcjghufmmLBAjRsidBxPooIv584WCp0k9k2cUHYjjSlESoMIP5Vrwnzsoae31WnYvPQdvT2H760cd0H5Yw3iQenMz7B024Zmq8_cLZGRBLfotHxFF4xj5wR4HlUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیرعامل‌تیم‌آلومینیوم‌اراک:طبق‌ صحبت‌هایی که انجام شده باشگاه استقلال ظرف یک هفته اینده مبلغ توافق‌شده رو به حساب‌ باشگاه ما واریز خواهد کرد و ما رضایت‌ نامه قطعی بهرام گودرزی و محمد خلیفه رو برای این باشگاه صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/23288" target="_blank">📅 20:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9VfSIJ6UlmXksjujY-991nZ_LBfbGTTLMTHSgRnK9Cu-a4iUyMXgaOhqien5Da9z98GeLxE7KQ5gzkbPF4se2HCLmsDXHeHZgqZzkTzIEtu3jTtNUsJi2Zts6BXFRPfE6do0pVgvFB66NxTpDsL5CS7oe1ihO8DyYpNf8sDYiMtfq8GRYcKOhy9YKDeVh6t4Z9cXKOqQawH7D4eXrj_M86eStKIi69vLlDnmg1dNinQgt2wMtlmO5sE4rZfPF-EXYNmzbUrbRYf3FhlTF1DHSczGX4nCSMluOzeOIjLPpg2zTXCR81Ul81xkaBqz-sXfIUUhMxaJue5HwrJFzA-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛دوباشگاه استقلال و پرسپولیس با ارسال نامه‌ای رسمی به باشگاه روبین‌کازان خواستار جذب کسری طاهری مهاجم 20 ساله این باشگاه شد. حالا دیگه بستگی بخود طاهری داره که کدوم یک از این دو باشگاه رو برای فصل اینده انتخاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/23287" target="_blank">📅 19:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23286">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbDWPtvk1nMrpfRlwrkJVn2LBP6BPLyckD5P2ubZNiVhjBYCKF_kwuAUUj8uMwFTtWznybOAMT8gcs-uaFmnoTEJsYSSR_26z5kn0mrMC-Iod1hxt7k5s2JUV2e_gCTwWFWQx52uFXdQKkBb2aM28YEz5ihFRgAJ6aO98A6b_VN9IEW4onb7MW9JH9RNWOaeHJUPysYyuSuxXnFXCPN-HDN4uyOj-MM572_tuGz3hnlnF9z-ERrjEEs80z-kgE_YzZyu1MPpaJs6BUw_1iyEy8-A5CU4mK3ufGA_qEwWjPlxxbsHOmXQmW1u1Lr6EgFbm_XtsWUg1r2NjUwuiFWxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23286" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23285">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23285" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23284">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
صحبت‌های‌جالب کریستیانو رونالدو اسطوره پرتعالی تاریخ فوتبال درخصوص جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23284" target="_blank">📅 19:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23283">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joHgx8ZAXmUIQgkjd2EWnM_rD9AzU3dXJJk7-C-K7JuXOXh6VOtPa1_8mKYTKzTNdoRLdA0oLClKRMCk39Lx7h1e_CwNc5X3CnW_rGu-rRrkgFU8qtIwIzLOKMzdOf0tXvPBg9CT-gsLkvzi-96_dCO_RO9urO_cJcmaWsQAVZjwVIwYhwxMgI_idYVL-EzGENTfV053tuPLBg1JQhmC1vTY5LaJySrQjHkGyUV2mNPs3CeHGw4HVgPHF0hI8m0hEgwu2kTrMQDPCKUhm7tv-4LCAI0VwNqH76_zWz7AVbk3IFzf9Oajl_N6h_ekFQzj6-Asiiln5NZFbFsT6Mkt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش ساعت جدیدی که امیر قلعه نویی خریده و در تمام شات‌هاش نشونش داد 136 میلیون تومنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23283" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=fI3e1AG8tYM-AU27MMqO20c7fCvOuxZmv_q6adpB7j9mTEe6FWF7zkSP_05jHOrWSyARqUeTbkrJllokLAHF-nmdYJFNaJM3RYSjELTZm2v5SyOCJDo2LfgPTl86jUV0WgNK9JZ0KZvqjLnTKLPBHDKcWEl1YIKtrbQorgDN5db6cRusJNR2D442eW2mA0ob1MuLU-ocKke9PRC4V8H4FJnxgHx8I4T0ja_7RP-OlwuU88aWZzpFJqHZAnqGQKttFMg5Xwt6RPP0vI_un83SMfxu-UIW20HE8e6S3qTi-ZfVSoWCttQvdTwoGXqVXv3HkgUL-wweEUm19nkayZLQKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=fI3e1AG8tYM-AU27MMqO20c7fCvOuxZmv_q6adpB7j9mTEe6FWF7zkSP_05jHOrWSyARqUeTbkrJllokLAHF-nmdYJFNaJM3RYSjELTZm2v5SyOCJDo2LfgPTl86jUV0WgNK9JZ0KZvqjLnTKLPBHDKcWEl1YIKtrbQorgDN5db6cRusJNR2D442eW2mA0ob1MuLU-ocKke9PRC4V8H4FJnxgHx8I4T0ja_7RP-OlwuU88aWZzpFJqHZAnqGQKttFMg5Xwt6RPP0vI_un83SMfxu-UIW20HE8e6S3qTi-ZfVSoWCttQvdTwoGXqVXv3HkgUL-wweEUm19nkayZLQKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ
: آتش‌بسی نقض نشده داریم به یه توافق فوق‌العاده دست‌پیدامیکنیم؛همون لحظه خاورمیانه. یکی‌از دلایل‌مهمی که اخبار جنگ رو پوشش نمیدیم همون صحبت‌های لحظه‌ایه. مغزمون به اندازه کافی سرویس شده دیگه لازم نیس صحبت های لحظه‌ ای ترامپ و جنگ رو پوشش‌بدیم. همینکه بتونیم اخبار مفید فوتبالی رو در اختیارتون بزاریم برای ما کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/23282" target="_blank">📅 18:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udslPFZC419yJYfpllK23VKvcK83O9n7vX0AM7AVoZri1MFSY-3qUtgBaObV6Sj28xS416w0dybNQFmfbI8jHiTZY0wQNZy-SGTHlUFqDe9uHLyMjzKxpQS35paUJsMB-Hmv4Gp-yI5G2US_yENM1k78gUcEeATW3TDRoTt8k-6Oa5NBsWFA-RVTOKSAstddflMpC1haqqe-KGz3vtcgJnS6JFP-mOC8QxmgEPXg3fHutBwXbKhpz9QHBXiagY2vmNt1gOCjMZt7yqqNKxLPAtgytv6wRzZ92slepwCCFRrgZTEFywZZcXHjexZkLxowStHr7wUoqmBPQt08xGvfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
اینجابودکه‌عادل مثل خیلیای دیگه شدیدا کراش زده بود رو دیبالا دیگه شروع کرد به تعریف و تمجید ازش؛ خنده های کاوه رضایی هم داشته باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23281" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ezRc0qPVMGr_MYU119zSXT1x3J3_9m57HxzSv8mWkGp4mB1jVkKQAiylo52MP7VQtO-cpQntiScWpaB_MtRhKlruIrhPQ-36RSuGxwEtqMgdn8K_7wuLUGwV6PVNEiZdcYYjnAvZV8ZBdbIJnDN_pVzr9Xzdp_g_KlZ1sb_RWMHt9UhukPvxplEn8_fdGXEdI8tTfxlqMYxM_ehrQoQWkBIIFE_KCcw8vEOFlAK_jYJOTE00UAAu2q57--9LEfa2ql18LrmDTJS5g0Zvoow3aM2p3APa2ZABAqc44xAysvb6nVFOTY-TxFbIl19kMeCcr-Ldwe5EERZ3uT7urFoPOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ezRc0qPVMGr_MYU119zSXT1x3J3_9m57HxzSv8mWkGp4mB1jVkKQAiylo52MP7VQtO-cpQntiScWpaB_MtRhKlruIrhPQ-36RSuGxwEtqMgdn8K_7wuLUGwV6PVNEiZdcYYjnAvZV8ZBdbIJnDN_pVzr9Xzdp_g_KlZ1sb_RWMHt9UhukPvxplEn8_fdGXEdI8tTfxlqMYxM_ehrQoQWkBIIFE_KCcw8vEOFlAK_jYJOTE00UAAu2q57--9LEfa2ql18LrmDTJS5g0Zvoow3aM2p3APa2ZABAqc44xAysvb6nVFOTY-TxFbIl19kMeCcr-Ldwe5EERZ3uT7urFoPOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23279" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=kZqh_qLoSdPmMCUQoF-2DE7ycvYca0urAUmQzYwL-y0D3aNeOxgJolgBUK0bm6vBWFnrcx6h1eJta778L9oC16cWliQx1fT-fvTM4YkUwTMPvKF7y2rcqx9bGpoItz0W63kpvfTnDj9vLi4NzKLIFN-tvZiBaexw77gxWkosAIgu-dRErgRpe7NDgYkNFbqS27wQuzveGRLkxsxNppxm7bgopRpxG9HvrmQNQoEe-CnPXR9gaWHvRqmG7E50C7_RzAFhq-9Db2ZKZLV5ciDLvQbtKjkEbQ7K3A_cLivdU8WYzUIq_IAC-mqt3jdYXGgK50x3L_mACfXtrrfWDgAIJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=kZqh_qLoSdPmMCUQoF-2DE7ycvYca0urAUmQzYwL-y0D3aNeOxgJolgBUK0bm6vBWFnrcx6h1eJta778L9oC16cWliQx1fT-fvTM4YkUwTMPvKF7y2rcqx9bGpoItz0W63kpvfTnDj9vLi4NzKLIFN-tvZiBaexw77gxWkosAIgu-dRErgRpe7NDgYkNFbqS27wQuzveGRLkxsxNppxm7bgopRpxG9HvrmQNQoEe-CnPXR9gaWHvRqmG7E50C7_RzAFhq-9Db2ZKZLV5ciDLvQbtKjkEbQ7K3A_cLivdU8WYzUIq_IAC-mqt3jdYXGgK50x3L_mACfXtrrfWDgAIJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اثر پروانه‌ای چیست؟
یک تغییر کوچک، جزیی و بظاهر بی‌اهمیت درشروع یک‌جریان، میتونه در طول زمان زنجیره‌ای از اتفاقات را رقم بزند که در نهایت به یک نتیجه‌ی غول‌ آسا، کاملاً متفاوت و غیر قابل‌ پیش‌ بینی ختم شود؛ درست مثل این ویدیو. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23278" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2HkpyfrML1aBF5Ras5LYOb_2AW59_xHIjUo8RMvEVQ_Y9S0wq7CVBRll1yHPxv8fvroXahT1jzKV-ak9BDKxIL8gUbjhDOdhvjIdamA2Xbg1lo31LmLNgDRtvO99RAUeTeLP1Fnro7ytm0VQSbMSsNvg2iZ2e2oKaLqwxEDZ_ZpGRlxl96MplYwN3Or8Jt9favRjI9KLuosqLEar42YASmefZA8pK6gwh-2mOoQ4zYS5Nap12hNwbHvQ5jUXXlGfJSnR4WjWv233TqFlhktTmYqqk9iNjMN-FpPhZDlzCUo-ES9oBB_K1kf9Sfqpf7gk_z7d0g3CpW3ztNVPnlcVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/23277" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRKxy5AxeMA3B57HKgNnmse6DpYUQnha5QUlpnUllmIrawKgF83_5l4W40MPKeOKB4VzDQJPeECyke8Pdzvs0-omn2_EexO4HlOvxUUaOl8suaxIm1bQi2ycCRmCneUT97pUo8mH4zr274Hvxnvw1inE0RTZNA6Lc2FwH2OkFaCwyZXPMmnETsimmX7Iz1gdds_s1pLtORODtCl6cSM0dr6Lm9PoSfgvY3RyBT01ATr8MIwUX-i0Xt-4E1FjQl-Km6-7HIiaZG7kqc18U0gIjYTe9wLdMhKLeQqiow3jDgXKhKf6eRwLcT349E4DnvRe5EewPJRS08D_tevnyGBEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23276" target="_blank">📅 17:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=Nch8nuybe15UbPc1LG3ff6y5J68vRo8vUyB1Hw-G-xXKb3wyG8tQaNkOdR2ZOlIF1YHVfWPCRHXTGgtcey8xhmvTPXIBnS0eoueSNuXuRLuIiLOHjzABmf3goJheIxpyqsIuWoEWGuTGH3i0D1wDFi4JEULngQYgdc5NjbZ5iUbAyyVcECbhkoS7E6exVwgKsHFKlUxJuvCYANTGBcUnYWBK_Cp4cakPxLzB9AiHDLQ1JkUnZjScKHYu8DyeKh2pjzCPxcwGOQ8FoHQBgvh0lVVVfG-5M-oM5slXXHMc6C9wM9mxQ7qyZFV4ngN4Ce-uCZguqLINauBdFBEcOhYGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=Nch8nuybe15UbPc1LG3ff6y5J68vRo8vUyB1Hw-G-xXKb3wyG8tQaNkOdR2ZOlIF1YHVfWPCRHXTGgtcey8xhmvTPXIBnS0eoueSNuXuRLuIiLOHjzABmf3goJheIxpyqsIuWoEWGuTGH3i0D1wDFi4JEULngQYgdc5NjbZ5iUbAyyVcECbhkoS7E6exVwgKsHFKlUxJuvCYANTGBcUnYWBK_Cp4cakPxLzB9AiHDLQ1JkUnZjScKHYu8DyeKh2pjzCPxcwGOQ8FoHQBgvh0lVVVfG-5M-oM5slXXHMc6C9wM9mxQ7qyZFV4ngN4Ce-uCZguqLINauBdFBEcOhYGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان قلعه‌نویی شب‌بازی با تیم‌ملی نیوزیلند؛ ژنرال ایران از تاکتیک‌های خاصی استفاده میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23275" target="_blank">📅 17:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnWKFrUKkjNPnrniZfNyWGNX5-mijc9w7okSqzQnwHfLtgl77oRlMUbkXGm0_PIFGR29L74PfHRC_2PBdXztLuMEk9ODZw9zhECiLhyCR1jow5NoFA78WXzn0nEx-AVcO--vSEQzw7jPWJ6s0F1Gci1sZTrWZ9yvPH5zpGowJMjd7nhN7UdErPn1tu9r4U-Oo_Z9Fv0-IkIpSqsY9Egd5TaeVFYEoLddnwrAECgu_e1E9o08BxcB5IALhF-LFLlFBVpaxdKxsQOMU5cDi7u_3b62dLrnuLK9X2Jm3lxGSIeV2SXpBbGpPF29sj9ol2NanXlEPC4LIU8OyiwHpTyVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23274" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=W3Bi4GUeGvZM297VojDmtqY6BSPGR9qcxM0QryvQC3HV00y8xbNLriWmnq6X_Lj34pPyKNrUiMhMIl7amlsVVm7xhW-QoKXNzssgvgl8m0mTIYQenhnE-s6bLm6VhFVLMS6wRaWLBGLdUJjjgEAzvUU3KnW4WvRqRGd55iXzfHzEppnIJBY7-06EbC2s7_eGGHnS3d1ZRyOi3e5bgPHEAhj2ZYsBP_dHFicsZXY_98l06HybyEhk_ZJJdUFA3GfAvLm-1H4KfxefcQhFeXt1MQDaEyjeiovf6l4DCxbdscYp4g9hKgM6sTCvObXcFVvNLK_-fDBdqNwo4mAJ6CZO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=W3Bi4GUeGvZM297VojDmtqY6BSPGR9qcxM0QryvQC3HV00y8xbNLriWmnq6X_Lj34pPyKNrUiMhMIl7amlsVVm7xhW-QoKXNzssgvgl8m0mTIYQenhnE-s6bLm6VhFVLMS6wRaWLBGLdUJjjgEAzvUU3KnW4WvRqRGd55iXzfHzEppnIJBY7-06EbC2s7_eGGHnS3d1ZRyOi3e5bgPHEAhj2ZYsBP_dHFicsZXY_98l06HybyEhk_ZJJdUFA3GfAvLm-1H4KfxefcQhFeXt1MQDaEyjeiovf6l4DCxbdscYp4g9hKgM6sTCvObXcFVvNLK_-fDBdqNwo4mAJ6CZO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23273" target="_blank">📅 17:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRCWQpX8swPcRA6b0Rk_aPao99_63RIpZUOQAZmeevY9i3cm_xX1sHApj8vBb_ReCgOeMYt6R4m_e9asYI4qJSItga2m4GQBBOZHoj5AGvzRVc-4VhyttRceTPUHZG2HvqDMpcBpV0y6WC7hd5ppaKw5g9m9Xv6DPhHagD3v3Hnsrn9o6lA__A_McnHUrXivtxn5kmnLLgtemKRWq5POFs6TVj5y0ouI2sJXGSqUhf6WtMXuCdnMFYU5zuC-fPDGT-kpoUoQWciHUOgXhzlf8Cr0GeW8JYBHjhJJeOzUDTXBkgAEgRLP6P2-PU-tUq6m_9IkQ4OGa00T6DaTG21tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23272" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23270">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1a4HIan_gDMgdX7WkaTGsNjaHSMG41x-rmRwvLZrGsWpqg8ETj1vVWsXMx4NWCcg4pIUNUk2xt7xVKYvjxY0m5iog1eO8oVmq6NbIn6GlNZgO5IgYaFoIL_r-GcG7d6GJ_LxO-pdH1gteV_QkcWeog0ZaASMwIKoDoZofdnaR32JqLVMJ4lRp3Y_TyHmNgLni19j4l4HU5aEPdodR9Qc0uEkiJlskN5uh8bhohm5M-GBMA1wDWRjcFQZujjd7UTvuYlm1RUh2tKeux-8LenCmL4IRlFWD1SWWj19uV2z3QPztjR7sUpSzZZYcyVOgMVuCr1fmg8IymG9rD87h0oxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITofklj1lr_Bslvyho7rRNePrQoljBRwq2qUkGluIpg5vwfSeLcMAg_qfXxYVnzw4bZXiEWBDHmfIbQnUsYQf9W-W9oFXiy8b8TDL599hRBFiNFDabr1N3jEFvyZ9vAkPM6ah2x0ubDZCToeO1bspqUV5Lb8R2uj0YePq1CNlC75xfC_L9p_9AffIY8VBsqpYFOU2tztRH98cYvlAz1MeY_mh5fD9ZqQbiq0oEIUGPQhi3VdIF1fEYgAf6krZmkKJ8fuOjrsrXSFrqik2ucoOCml-BCI0AS8zYhwRwaPzTcVDyri4DJZg7hQg9CKQsy-zvt5TX_bxo9jCO47Yqzs5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23270" target="_blank">📅 16:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=eXugSQKqTiGM2bP9o5FjzR7wfkLr30M_L0MV96mxCT7xL1wZuAfxB1CmjbqFsa8K-AQZpP5DxOc6FQ_4RWeGvz7iJeaer64cX8BsKPGk7qcag56BGFzJesYdRhmna1n8xR0P6WRFrqKBFCYpgxd0Yi53htwS_xNQwVmMpSLY2s8nyPC4NcarPTw4dL1GCcw6nMg4fZX4sg1LgkqGgHiMbkrIG--GCRDiBm8RVrU0bR7o4U7pMMI7HIHrqpU06fKsLyZbF0l8--DoS43G_B0bMRsGKQvx0ybZUQawX_FYrXUdKUM1kj3mZEftnyxG3Ra6dRua0_wQIfVIB_LWS0efHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=eXugSQKqTiGM2bP9o5FjzR7wfkLr30M_L0MV96mxCT7xL1wZuAfxB1CmjbqFsa8K-AQZpP5DxOc6FQ_4RWeGvz7iJeaer64cX8BsKPGk7qcag56BGFzJesYdRhmna1n8xR0P6WRFrqKBFCYpgxd0Yi53htwS_xNQwVmMpSLY2s8nyPC4NcarPTw4dL1GCcw6nMg4fZX4sg1LgkqGgHiMbkrIG--GCRDiBm8RVrU0bR7o4U7pMMI7HIHrqpU06fKsLyZbF0l8--DoS43G_B0bMRsGKQvx0ybZUQawX_FYrXUdKUM1kj3mZEftnyxG3Ra6dRua0_wQIfVIB_LWS0efHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم بهتره برادر بعد از این حرکتی که زد کلا از فوتبال خداحافظی کنه و پشت سرشم نگاه نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23269" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uziv-EEEJt6JT2xHd63Z7DzhHkqZIx8GgQUdWfNwh7_xR0TfkyDpkKy-sU3SGHN48d59OTo24zqsJVeeVv77JPdhzY-laahp6hj8EwFA5DI9giGo7U06GrPk1rZOADxDQKkRvaIQ_ByrOVYzhm8H567wFbwjPaKZPvF5udiIzZXCRsoLDXWQ46sYJENzyGM0wo8nlFNVNhCfS82S74pl2jXW0sNB2WHF3Qamz71bVLGjrRKbzen8CtETwpgpMRD2RTDnqWNAhInQZd_ZZ4_dAU7gyRcoB4dc_rUHEo2MTS13JtyQMEWuW1u-Mw81ve_pzJFZLDXc1VSKJ1VuV8FAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/23268" target="_blank">📅 15:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEghjjt1ULikenVQWTqcaoXd8vdelEB7cFtIRH9MG_o-RIvPBnQohhjg7Me3ajZiwYXXyzgDCxoo6hnxTmx2fyTtNlN7jRmW3CmpfnRxfl1yWJdQYNYaObQBAFk-yn4Q0c77Us_rER0iKjHp5OJ1JeOlReJEPHJo0UjyVnHZb6Ir4vVnCnS_i4PW5Cw6IORlMIBEv1AZXP7y_O5IQhzG-oS4CY9ckCxO1Jr_TqARNYqyGGvfm3FiAdacChnX66mWQghilpy80K4KLrMiNM5Ny0dkzafgw_TLOKoZrzdY_IWWkeVnHhoQA2S5AfsCmaBR8SfxxszhpC1rcWgmg9i5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛براساس‌رسانه‌های‌نزدیک‌به‌دولت ترتیب رفع فیلترشدن پلتفرم‌های‌ فضای‌مجازی به اینصورت: واتساپ، یوتیوب، توییتر، تلگرام و اینستاگرام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23267" target="_blank">📅 15:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=gPU35x6bacDSh_uvKAVLUEatyIrEo02VONdOp96L0BP0YEELOxgTh9x_UddnQdSbmGLLbtlFKXVZ88leO5Izyanb1DcLkwinM7HBmr3__dhimN3vEpWcm5m1QXbZsarb5vAaJeOUPSoABO6LKm1pzGNg30zrak7-SBUoE04cPClCYAO3GgpLlPq7lW0L5Ml_NkluiPWlvlnHYPl3lK2bKIhvqx6ZYlQUgyG38SAE2OLX06k_RukKrBNMLGqV3ZtYThuL8PZmPb07MQ997wV5bgUagSxjc3wvR4A5sUlrvliSwYb0bxe__805o5B4lUfMYaZAheiYGtY_PrKzPN5xuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=gPU35x6bacDSh_uvKAVLUEatyIrEo02VONdOp96L0BP0YEELOxgTh9x_UddnQdSbmGLLbtlFKXVZ88leO5Izyanb1DcLkwinM7HBmr3__dhimN3vEpWcm5m1QXbZsarb5vAaJeOUPSoABO6LKm1pzGNg30zrak7-SBUoE04cPClCYAO3GgpLlPq7lW0L5Ml_NkluiPWlvlnHYPl3lK2bKIhvqx6ZYlQUgyG38SAE2OLX06k_RukKrBNMLGqV3ZtYThuL8PZmPb07MQ997wV5bgUagSxjc3wvR4A5sUlrvliSwYb0bxe__805o5B4lUfMYaZAheiYGtY_PrKzPN5xuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درسال‌های‌اخیر؛
گولر، اندریک، دانز دامفریس و حالا هم برناردو سیلوا تا آستانه عقد قرارداد با بارسا پیش رفتند اما در نهایت سر از باشگاه رئال مادرید دراوردند و راهی سانتیاگو برنابئو شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23266" target="_blank">📅 15:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAsokkGht3PbJ1KEAO3xLVm5xVZuc3n7Y6f7AJAUwWWUSsrhp_cF8SI9FHTCVgKPTC5A_CxqPCN9-9MboI2po0pu9hwU3lRJlik-ujL15UF0F5jyufeADeIYGXK0IB_VCPQdoYttv-sE8h8dB5pZ7BWW8ufYkQfUkKoZYztXZwdt0ISH38NiYluucxQKFzwAA1s58Z3HGv6dkrQLp4tEIMn5gpZWq4SBTXp0qdL-e7ybEVgAgg0Tt9IF2WzjBhpk8boWiesiverOdZTO-g13Ft3PfiL3ClZ5k7iieSQE228WT_vvc81YRDokZ0KisMXjXikoiGgEepBcrfW1A6nHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23265" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=ArSyxhSDCZeJszVgrJhgbcLwGvmpzMX5uK6WAcc_1K-kjESRjUsnz1Z9F49k2B_FQsXO00D2lvfliRZ7C6T5VYctDAJozlUy0CT39qgmwuicMMvXbOqRls_ygcuHarpaMnSGh5KyH8bf6lPdeo6kR6EI-i-dWOmtKEwhvCYsyKbaSr1OKcUd1WI8HbnijKstL4UHsYgI2iCwCZpyBWxWqHyVwje4loavxjBHcYEleq0DzM1ZSxyeeAXvmjbCYtJLfEHDmXsyi1oGzKF6nj1-JtlC_MbPQ341ax_88vtAb63k-0AkQ-CsXsv-hpxw-TOHXF34sk9Jyadxk9m6QucvEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=ArSyxhSDCZeJszVgrJhgbcLwGvmpzMX5uK6WAcc_1K-kjESRjUsnz1Z9F49k2B_FQsXO00D2lvfliRZ7C6T5VYctDAJozlUy0CT39qgmwuicMMvXbOqRls_ygcuHarpaMnSGh5KyH8bf6lPdeo6kR6EI-i-dWOmtKEwhvCYsyKbaSr1OKcUd1WI8HbnijKstL4UHsYgI2iCwCZpyBWxWqHyVwje4loavxjBHcYEleq0DzM1ZSxyeeAXvmjbCYtJLfEHDmXsyi1oGzKF6nj1-JtlC_MbPQ341ax_88vtAb63k-0AkQ-CsXsv-hpxw-TOHXF34sk9Jyadxk9m6QucvEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌باحال‌از مسی‌ودریبل خاصش؛ همه میدونن‌میخواد چیکارکنه ولی بازم دریبل میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23264" target="_blank">📅 14:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otMSS85PcolDzgCwL2FiR5Cx2M9VA2s8_TC8tbV-VZroKUUFqmOyCzKO05otzWJQ5d6UZgdjKNx20eSYOV8hT78XumIe_f3L8M9vWz8E4n17PIMIV_Cb3OM7cipg8hbbT9Ay_RAGb4qAiVt29TRVYkNKDbF2vPOU3G-XF0ir6yy81AOlrVwcXmERwwFZAdJL2BAIOYgVYImffVzUHCI6w9dcvTmgF_D_efBJSXtFws64XFNvyzWu3MuH7qYO4vATuuBi5Re0tBISjhatu9xtwioquTw5aEB1v-AXmkvPNd3CrqX00LKQ8cs35nnkRdMEmwAgZ-TyLEzXWa9sXBVt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23262" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=etzC1XevbLQJ-na9E8Os7GLNTwWB_EOYEnc_HH7LHjLs87ooa60Jd0FyQQNCOWYiAlwVG1iJOIkj_-ZW1-FXsXIwqCw4JRvpibhWcg10gNJlNeye9vFVHttLt8mSQKEpEVoOPocQhwqqkK9cyX-cZgvsYqu1uiQlwxnl9blYo44Q37Sa083WSzB78KhWnAZ4iETA9JY1IQZGJn71ZuePi-wM0-PoPt2fLJKktCTIhmQWXpC-F0LGnQTcXnNk581n45hTBt1CYHcpu7ovhMRB6k4ddwZNUuZmM_4m5o3AYseGYy2ZWb_LmOzcVyKmexKQFY1cVUWCxii0sUUMNHLsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=etzC1XevbLQJ-na9E8Os7GLNTwWB_EOYEnc_HH7LHjLs87ooa60Jd0FyQQNCOWYiAlwVG1iJOIkj_-ZW1-FXsXIwqCw4JRvpibhWcg10gNJlNeye9vFVHttLt8mSQKEpEVoOPocQhwqqkK9cyX-cZgvsYqu1uiQlwxnl9blYo44Q37Sa083WSzB78KhWnAZ4iETA9JY1IQZGJn71ZuePi-wM0-PoPt2fLJKktCTIhmQWXpC-F0LGnQTcXnNk581n45hTBt1CYHcpu7ovhMRB6k4ddwZNUuZmM_4m5o3AYseGYy2ZWb_LmOzcVyKmexKQFY1cVUWCxii0sUUMNHLsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23261" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjnJpFt8rY3KMM8Vfr1c4-oRzHN0wxARMsPazaVAW2OVR8JOKKnZ9CyL9PrUsoOEh8H3F2tZdocuwuGN-U2aMQKctNnbqMnBsvdj-VgZgLtHkjiustJAD84DieKqRo0ejv8WClI57djRMHvuczgUWFdcVMt3fVvtAqN058DmWUdViOx0enyCdGMfKAjRWM9mC1a0kUUjcQql_Xqz5mhcitZcbkao9oVy2POFAlOrRdGQ_X3bivhxoq12i4ZBnfDZiOuBSAgx7fWaHwlwb1tA-dzsiEV0jePiRT3ZGwTeNUO-whbXsrRT2HtSgqEsplgnEAewF45KIjhIdPhJbS4Ikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دوستان‌عزیز لیست نقل و انتقالاتی باشگاه استقلال کاملاآماده‌کرده‌ایم و قرار شد امشب بزاریم که‌به‌احترام‌مدیربرنامه نزدیک به این باشگاه و طبق‌درخواستی‌که از ما داشتن فرداشب لیست کامل روبا جزئیات میزاریم. امشب باسه‌بازیکن مدنظر تیم جلسه داشتن که فردا…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23260" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7927d57219.mp4?token=HpYvolE5WZyG8a8wMLnQlBP1viS1LpX80PeZFXTka-afL8JZUMKjvaBRwkYfPGvMsU8ncz4O2nfjE4EkBHT6-UDgQb8vCBRltk_hxTgQsx1LJM0gIeaE48gkiFM7F0Rf3EIuzbR8NlA1e0OyNOhJoJKj2QZb3_wI38sYWfFRHyis2WEX7Nd8e5c8uTakmdfBqojzheJDznC1zdKO1h3uOuF1G1dKz_3OKtttbGFOgt6PDVzqCUqJjnICRUDdTtCeP1Dg9f1yoeKFV2-tiKPDig2wH3D6Eb-twUQ4iCywc8BmLjvpY-7osRgcDmv2KZVx_7le9tu4Cv9rw1jSRMgZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7927d57219.mp4?token=HpYvolE5WZyG8a8wMLnQlBP1viS1LpX80PeZFXTka-afL8JZUMKjvaBRwkYfPGvMsU8ncz4O2nfjE4EkBHT6-UDgQb8vCBRltk_hxTgQsx1LJM0gIeaE48gkiFM7F0Rf3EIuzbR8NlA1e0OyNOhJoJKj2QZb3_wI38sYWfFRHyis2WEX7Nd8e5c8uTakmdfBqojzheJDznC1zdKO1h3uOuF1G1dKz_3OKtttbGFOgt6PDVzqCUqJjnICRUDdTtCeP1Dg9f1yoeKFV2-tiKPDig2wH3D6Eb-twUQ4iCywc8BmLjvpY-7osRgcDmv2KZVx_7le9tu4Cv9rw1jSRMgZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23259" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRPkKrUt1daiT_VldpiTTaWgGld-YjkWhhKTIbsnldKAji6ExWq4Q5t0vEzrPt3EGEvJZ2ZI4i5GskAulzcfYKmMiN7wFC2PvAVA1v1JqQQK3kzLwD6-dfoczAFpx9J1k6tn5uslRIvhAK_C9ySi12PI1PmXlkwKJPfAMhZHJj4SQAt-ssgvciiarw3ANk1f9emnsrs-pSpCBO-rPhX5RnyGzWJOEhqu0W3yDVuXHJhUbdkuNMc1hCbf3D4yJY-uyoGIYMnuFlWvqzxWV7JFEo3wammlzsc_zPeF7wLWcDUsi0pv6qscleJjxiy_0x83H4b3Ea8vcIPe8369hLLMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avldMnzdfFOVqoMEE6_33For1eJIscMRZARHQahEKdrZlbpJ1faVDLXOEyPUnK8XZAblSd2LvRnS1l95syl1pIteMgia06hAdv0RWmWmdBMAMlJIdhic2ueOj8bPn-yW2p0-HdLorhjMF79eCM9zIRtQtI94IDTctRBrsvdY7Yp8QGnnBwDJb9uHgTAZ8BlmVFwLT3eAZy5VpviA87IcRFfLWH4M5CzvpOH4JFyfqR6eq7eGA7VNRsO1Ev-tfu5XEx8RpAfmKld_Z27v-x_HqWNM5tVmd9tviOR6SZuylAkeoH5GPKCzbyR9G82liB_YLUXTpikqBIr16gBqJ0YaeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به احتمال فراوان طی روز های آینده؛
پائولو مالدینی، لوئیز فیگو و رونالدو نازاریو نیزمهمون ویژه برنامه عادل خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23257" target="_blank">📅 13:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎙
استعداد ناب گزارشگری روببینید فقط؛
با این سنش چه صدااای خوبی داره چه قدرت بیانی داره. رفقامون تو شبکه پرشیانا اسپورت تو کانالن باهاش تماس بگیرند که گزارش بازیارو بهش بسپارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23256" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4ueYb-rjSchGzMSzErhpen9ClbFUbC_VNoouwFhEQsvJBiliS3-CCyvwqOhkv9IvW66yctTzhcuLQnn7WG63X0FlDmeD8jfLKdhDZb_L-49dw2zZqMi2d1xLUGY7cNZA9ngITBKaJJObM-gelFkjy0DvkjYbnHtLwCIUxR3Cu4ZvKRTvLfpFtl8ApkEtWSfoHYj6X5oAzAVGCCGB6cm6u_kbKvUApd07940lt-Oaj8eyuojpOyV9TNVVM2zfMUEV78Qar329lsubxaN1012jINK8aavgyRea5S8AT94CyNT5E2zkCCGXHGNNK3ew7y37MMle5h6BNCNdPNnCaxaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23255" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N87rOJcDp-EuuU3y1AR8KjTJf25R8TH7yysKbE34OqDlph9LZXLCmzqMGNgop4poIk4pB81pctBuANpEZWJaCxZeTP8lfypEyXT3YZbzXgaoEfkrGay-dv0hSrhxWmiWvmf_e41etzF1A08iO8beDTJobvclSIBUF8blcouIvbFMgyIR-nAu-pW5dlYgQLGgssPJpTUM1ndzN0ftICuxVmMXSmzrHCc_m7Q4scjx_e9tHdCgLYGNuawXBNdnZDWhpifdFE-0w8IBaPfYGPYoWzZUkqZe1rgrfCE-cQitvlc6930bZ65NZlw7WXsIrn51dtiJcwp9WFnNTauapOkPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23254" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srKB6EhCk4Yof3j3i2RIeX4daVDN_rTvg0DY2FD6oyFRDYd38Yugapyz_a-CeAOOXMIzi1TcFUGgu-FFf7o2B1XNc5GO9yZZhsHqW4zmAj_Qvu6dpQo31Ajl3mwpw2CN3a0H6Pd-8IqlYo8BUnVMz9gDO2pC6VWWgKOdAR56RIq1QzXS_Q_X82TSO0ZJyHlccY-6FPLEm-T87m9rXVvoBloyg_jR9Y9Mn-ESZxl9hq3m-nLI98o2v2Z_KYRGdnyAgF5GtZsl9BzvvCh7szr4hcsaqSIMxrs58wPWlahz1SmOUDqFhfIlEnj6APm4VkDUyYs08z4P9kZjSof3FAmhDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23253" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=JjCE9SOHqqNwKQsgWENWtOj519vGJ44-C8BRvdex_ZxGrQUF4Pz--_V7F9MUC-O5Z1m8tzBTmOjv1uC0iQGk2H_w7dgQEmdxxvNnX8vezNzVw3RI81pCah3mnkQ6Qg5SrqBvMdK2ULDNkzvtk6D_RowiTFxfS9T4E-A1iGOQT4UM3_dLEInSfRWRw-sSiQnWfIFKM9bQV1kHZpX_FsrqV2JeW9c9ynl7fdSyUpH9hr191xkVz9BRNhP8hh-PlsNHNbha2wqv5fWfasjCZnaaQL5OaI96x6zNrnoaZJKzWLN8O9Zf9QGPG30iN3CJ8DJqm6PN6B6X70XUGt_VFWAYKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=JjCE9SOHqqNwKQsgWENWtOj519vGJ44-C8BRvdex_ZxGrQUF4Pz--_V7F9MUC-O5Z1m8tzBTmOjv1uC0iQGk2H_w7dgQEmdxxvNnX8vezNzVw3RI81pCah3mnkQ6Qg5SrqBvMdK2ULDNkzvtk6D_RowiTFxfS9T4E-A1iGOQT4UM3_dLEInSfRWRw-sSiQnWfIFKM9bQV1kHZpX_FsrqV2JeW9c9ynl7fdSyUpH9hr191xkVz9BRNhP8hh-PlsNHNbha2wqv5fWfasjCZnaaQL5OaI96x6zNrnoaZJKzWLN8O9Zf9QGPG30iN3CJ8DJqm6PN6B6X70XUGt_VFWAYKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|
هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23252" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCWYXaBThtt7SpjVITGotZiS-zQR-zpdBALBS_4RIHOLEQukc-YPonwPl6ITOBdGLf34O_nZXIB3tM6y9ZblKpQ0EBCteQZ0pNyKZpmrRi8Mr24DxgYnKX5Yflw98Kw0FeTjF71LzrYk2yrXibolcoWZmxAIa973w471VRG-D9jSbWIY4d6mtoMEQghVt2FBMMw7v0QAhm-38eRZx5ZzjT6izTRdOzRwC0O46413oj5Ivx8-R2jMqnBrpGGOKtzDn7lnEqOvxlJR0RdmUhVFys-YdqM-PT1p8ETUtXWFqI_J8ANZQ1dsGPDxDw22B2w1QpCMZHHqEGatO7GC1LHgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
خوزه‌فلیکس‌دیاز: یوشکو گواردیول امروز در تماس بامدیران‌منچسترسیتی اعلام کرده که از باشگاه رئال مادرید آفر دریافت کرده و قصد داره بعد از جام جهانی به جمع شاگردان خوزه مورینیو اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23251" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLDHF4zDWephXEWDzFuEuLRnPGMscexOoJLu8H3VUnyhELo0wwJSAoiiiXhnPxVymrca7zfWjBt8GQNRN2wf5hy67xM8-ehnlYoan09T91um1onGmoIlPTjtZ8kx1wxYWig63PLNjgmE9nqnjOHfpyT5EjW3ItsYUSMq3vbTSpVBM2fZmx6l5aOUfZb397jfSzBQ9fzyfLolPe-mIF0q8_Da8sP3XqJ3cOONvPItT0q9LMOnQxrWd4UMLvm5KYG-YRu0s8xQWzcybUIhC4i6QPqF3T5fRUHGFEe_eLeKmX8zTG147yqVae6UGqnQnAJhTgC6PqGMIgkP1oXlFkxnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23250" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyxHI-ajUH3sGl32xF_-P1Hs1xrOdfk0x9g0eyKmWXeZ4nvuLrxuLLXUg-6StI514vl2e2Hul7m8xVRdJEqfpKSh_lyAX691xbJubBB0zpXghw-GZTUPUtjGISQwVGzfWpVPRmI2_YRS7omOtIWjV8hrttuDR68DRwD1kJzXSXIB-dgWX6AQfAe3prPn9ndx4HNG5Nb6C2vWil-W30XA5J-DgPkPY2TeG1XM3tFyXkwJxIyIEkCbU7NTdUKtC5bIWwKhqfCmFpEfb3eF7T60gLUJ0ZnIE1AbD-9NZT-xkJb3U6vH1-HPpWGuI3ensma19SHfdApNMiUPZxin0NZYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23249" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733942b449.mp4?token=YITyU1vVDYMejiGWbfC0PXMZX4ElKrD-Y-VrukzUAR9cKG9URvgQ8FRBS24nmo7wgrz4lJMUUqreY_P6M7TcJPS8NbNGfoWXbId-dc8BF_G4Eeh4UhMk4oNc4MmC8nxTFTrdW8Yx1nFBHnKOPi35m_keWxTfefxxNSJ2-A7P1XJqaXz0CEtu_8SFkPR4-kmYWpL8WZk3R-E28GvTn7-zQlsTjJBJ2XuoaUW5vW_p9uU4f-7ycvUw2jbN0bXZrXlrXcv0n7SYYteHI7-3hr4yNi0lkcFShk29O3mB1_NZVKkSo7TcltIH7dpmzGPRxfsapf5AjTH8NsKsfYYcRkv3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733942b449.mp4?token=YITyU1vVDYMejiGWbfC0PXMZX4ElKrD-Y-VrukzUAR9cKG9URvgQ8FRBS24nmo7wgrz4lJMUUqreY_P6M7TcJPS8NbNGfoWXbId-dc8BF_G4Eeh4UhMk4oNc4MmC8nxTFTrdW8Yx1nFBHnKOPi35m_keWxTfefxxNSJ2-A7P1XJqaXz0CEtu_8SFkPR4-kmYWpL8WZk3R-E28GvTn7-zQlsTjJBJ2XuoaUW5vW_p9uU4f-7ycvUw2jbN0bXZrXlrXcv0n7SYYteHI7-3hr4yNi0lkcFShk29O3mB1_NZVKkSo7TcltIH7dpmzGPRxfsapf5AjTH8NsKsfYYcRkv3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23248" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=ZGVdfO7D5WEIdurZj51bvrCnZ_Jmdg3yxLbLq5TrZ63bvut3rXmcDx5U_wACKa_4eAzhH0YiDoD9eIzC0y2rnzuf2QHGqVyNlQNQayHRLd8OGs93c98IH5drJpsXef4Cg_swUkRezS3P6SbGvVo2-rooBuPlkDPv42JNM2OO75YV-Kg30CS5oGYxDOss7NHPmg1SmFSk7l6Bh5TZdWBfymabceeyDHBaaQGDaysROp8Csrd6BMG6wwa3VegdmsbymthAt41b_8p-oyJ1Ew5UUnjD9URScmMwPs0qbvMQupyJ0pVP3YcHf1OCc3UKIimRZsnPqyCQQbk2PvZmpW15VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=ZGVdfO7D5WEIdurZj51bvrCnZ_Jmdg3yxLbLq5TrZ63bvut3rXmcDx5U_wACKa_4eAzhH0YiDoD9eIzC0y2rnzuf2QHGqVyNlQNQayHRLd8OGs93c98IH5drJpsXef4Cg_swUkRezS3P6SbGvVo2-rooBuPlkDPv42JNM2OO75YV-Kg30CS5oGYxDOss7NHPmg1SmFSk7l6Bh5TZdWBfymabceeyDHBaaQGDaysROp8Csrd6BMG6wwa3VegdmsbymthAt41b_8p-oyJ1Ew5UUnjD9URScmMwPs0qbvMQupyJ0pVP3YcHf1OCc3UKIimRZsnPqyCQQbk2PvZmpW15VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23247" target="_blank">📅 10:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=FY8wZZ9YMGHEsrPsKuQtJeTahzKcdPhSveOg2TNVHXQ_P_boLIc-878kxyx0QuziK-WTnfc61e6c7CZC0Kioq_Fn_z4-39MmjO_aTju-LCnxJh4kUnrgL7wVoz8BqzdU2KsifgQFo3IY10nwUoGNC5dA6A5LOE9UjUmrhQI34CPYh_SBkfKL0Ma6vbq-2JR3tZZv3O8ssxTKCxy5gR1UfBtX_NcWh6J2hM4hOuKBWwcRP5dXHxo-r9VU8nUmV7N2IOM6RiPsxKAg53A-d6nl8nWn_Xtv9MpGzzxbd7y1uI0A0MpK5XO-0y66x5dKL0Z_DPFvEwEuq69uvhSrva64bWXCzi_F-8S2V_i2cj5TXetlA5jkiri38F3TTZ-XwceH7dJkg_IjSRNIJNPBgDlhurkNb2-kFL8qBwsZnmpTzJtW86Ez52FueOHgndRmAHM-FuZIgWlGB_LDUoCel0_vzYlMeCwkwExICphexOTiCfc_-8haS5Qxgf1-e0lhItumn4CC474V0jabn9t23bXZ8skJNYp0MxVFRGPeyt6XyKW2OkYr6aqBuAo7j3DBr_cWg00VcvvIq40P80QVnwKPoo2jfGKhQYdXM_-XA7D-jPPfPnfJJCp58vtJ94WEqiXjFipY2ShO__e2gNZTOTVVeuar-XnrwVLpyrFDC3w7B8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=FY8wZZ9YMGHEsrPsKuQtJeTahzKcdPhSveOg2TNVHXQ_P_boLIc-878kxyx0QuziK-WTnfc61e6c7CZC0Kioq_Fn_z4-39MmjO_aTju-LCnxJh4kUnrgL7wVoz8BqzdU2KsifgQFo3IY10nwUoGNC5dA6A5LOE9UjUmrhQI34CPYh_SBkfKL0Ma6vbq-2JR3tZZv3O8ssxTKCxy5gR1UfBtX_NcWh6J2hM4hOuKBWwcRP5dXHxo-r9VU8nUmV7N2IOM6RiPsxKAg53A-d6nl8nWn_Xtv9MpGzzxbd7y1uI0A0MpK5XO-0y66x5dKL0Z_DPFvEwEuq69uvhSrva64bWXCzi_F-8S2V_i2cj5TXetlA5jkiri38F3TTZ-XwceH7dJkg_IjSRNIJNPBgDlhurkNb2-kFL8qBwsZnmpTzJtW86Ez52FueOHgndRmAHM-FuZIgWlGB_LDUoCel0_vzYlMeCwkwExICphexOTiCfc_-8haS5Qxgf1-e0lhItumn4CC474V0jabn9t23bXZ8skJNYp0MxVFRGPeyt6XyKW2OkYr6aqBuAo7j3DBr_cWg00VcvvIq40P80QVnwKPoo2jfGKhQYdXM_-XA7D-jPPfPnfJJCp58vtJ94WEqiXjFipY2ShO__e2gNZTOTVVeuar-XnrwVLpyrFDC3w7B8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه‌جالب‌ابوطالب‌حسینی‌باهوادار معروف و روشن دل باشگاه پرسپولیس که اون جمله معروف و تاریخی رو خطاب به علی پروین به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23246" target="_blank">📅 10:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQeLUnlWJJskEzZwgpx3zxYZuVckE-rVGoPko7bCdFz4Ya38ZK_639JPrUipG__d2Yiq76AKrUpqkFDQotTDMGTD2NRDD-p0-fETv4obIMLdunaohdCs3Wnj7VcxRVU9piLlHj6S2ML5LeAcs7CTWQ2M9ZVOyZiX_fEnZjimps09IoPiwfEY9HoDUY4sFo6AXBKA-I3b7GuGxz4JsaNguKaJnnMHnG9MwV501AuBUnWvpGQYFtfKqquXyrlSMTPTx_fRt62gChzSMbaoDD_6pJkFvdm8n-owKKtYYB6yO7ZdRsjXbMW6EsUaF1aRKYPwN3sS7O7DMgosKQ6c0IndVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23245" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23244">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5655edf133.mp4?token=uZ0ENF-VUcfGJgDv1AobPn_jm47ovw7uPEoi27s7SaJmJmfv86CY0-qmDuHOao01BVxn2LAZg_6kgkUAmmco5Cs6V22Og8qmeScDikuDNFlX5tjZHysNRP-Qs7-P6553WZdVuETGSOpsCMQAMY-2z66SGFCH7uUwzFfa_vkGF4ZmzzAR0JXjzAZSYcbWzGDKKWWjMTPwWiFi1vbAcw2Yb8u7zOZ3H7BZD6yekUyH1P2a-Pve_NFPSkAlTKx5_i9VDrgpOPpNscRCVH6nr7frQGueg6ggx7OFVcOG_-ss8UPhV-lsgu2N6Nczbw5DVOrmRmAbY7Irp0z8YFjMYtvqng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5655edf133.mp4?token=uZ0ENF-VUcfGJgDv1AobPn_jm47ovw7uPEoi27s7SaJmJmfv86CY0-qmDuHOao01BVxn2LAZg_6kgkUAmmco5Cs6V22Og8qmeScDikuDNFlX5tjZHysNRP-Qs7-P6553WZdVuETGSOpsCMQAMY-2z66SGFCH7uUwzFfa_vkGF4ZmzzAR0JXjzAZSYcbWzGDKKWWjMTPwWiFi1vbAcw2Yb8u7zOZ3H7BZD6yekUyH1P2a-Pve_NFPSkAlTKx5_i9VDrgpOPpNscRCVH6nr7frQGueg6ggx7OFVcOG_-ss8UPhV-lsgu2N6Nczbw5DVOrmRmAbY7Irp0z8YFjMYtvqng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زلاتان:
«مسی یا رونالدو؟ مسی بعد از بردن جام جهانی حجت رو تموم کرد.»مسی یا رونالدو؟ زلاتان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23244" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23243">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlyLGNulZz-H3E-a7-RwLrJQoUbwSfz1PX99Dx2iUlhuXiQBmgtsq3dBkoXNDyFGUB11-6vy74pc8w3ClpyuJ03cH2wa3RCc7UeSn4z7qBtkKuRaKWDOGVsVvAzBJy3Sj81eG9zcds4IrAMsaiW8gFwJGmeeC8DmQkUNuzQ5f4pStPTRh1am4YSFirCX2dVYi1OZxjgEoeK2dNVP7mH7VDsAYnfkRRtelO1Qi_Rd2SH6zn68juvMBc47MT_SgA9KeaYs5cdBXpmu2OH23i242o7trPYYSzad8DIZHrMgpOrXMMsgeSlVar_tmjNQEhIG_JUfuTIr9jNPyWKlLVxwZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23243" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23242">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=Bw7hjOnHwqfytc328YdHOSsPRPa7ROWkKvsYOS9OkiXYIF1TOfZrbyDvGn_Rni7rKlMmoxufW32njCTYmqxrfNDLi1Ls2B8VJ-RkQ5gLaZQooQ67vBWeKeXHXyMBw6Z5mBazl6dXRLD4SzqNgctjsjHbn81j18LiDSEm5ZDDoK4kqR3RkNz0GIl3nvztgvRwcKjYmXBXXb-afiII0aIkEYrdI1pAlzHQPRHvT2TcbuoQVdtRYUdfs_Je66UP1afW5IYKobxiUHh7W5WGfykp-ACZ0fc-HIwpTGcfAa5olKgvV-r9L5v_3kYtTqEWBUhmAkvptHZn_rO2GAr3oyFwfzUSbfEllNywiwcJcjwfgVMIuCdSGzKPcXdWgaSJc0MtVVeMRB7JPs07aYIqEqMASnBZUSr1tmLiUovPZz8ArJXZ3lCeK_LnAVDhto6sAAWyyMHZZxxWfCiuLh1s8bgpiRq38LdTPRsqptv3NkgK6l3B9O7_31nH8y0hPLNgx3Vz7xdmzoYAEuLPrWh01WVaumOOojinMHFAG0TcbVlawk4F2MZaT4W21UmYSCPre2Xs_D4zHVIsN2a2pUI4KwyiKB87M6f14NKL6O2fgQ_4GHNW-S1CmVCm7BPvgWW1nU-PjXB-GBDqIhXqet0R9DKEatasFKjbfA0iQDqwPQUOHu0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=Bw7hjOnHwqfytc328YdHOSsPRPa7ROWkKvsYOS9OkiXYIF1TOfZrbyDvGn_Rni7rKlMmoxufW32njCTYmqxrfNDLi1Ls2B8VJ-RkQ5gLaZQooQ67vBWeKeXHXyMBw6Z5mBazl6dXRLD4SzqNgctjsjHbn81j18LiDSEm5ZDDoK4kqR3RkNz0GIl3nvztgvRwcKjYmXBXXb-afiII0aIkEYrdI1pAlzHQPRHvT2TcbuoQVdtRYUdfs_Je66UP1afW5IYKobxiUHh7W5WGfykp-ACZ0fc-HIwpTGcfAa5olKgvV-r9L5v_3kYtTqEWBUhmAkvptHZn_rO2GAr3oyFwfzUSbfEllNywiwcJcjwfgVMIuCdSGzKPcXdWgaSJc0MtVVeMRB7JPs07aYIqEqMASnBZUSr1tmLiUovPZz8ArJXZ3lCeK_LnAVDhto6sAAWyyMHZZxxWfCiuLh1s8bgpiRq38LdTPRsqptv3NkgK6l3B9O7_31nH8y0hPLNgx3Vz7xdmzoYAEuLPrWh01WVaumOOojinMHFAG0TcbVlawk4F2MZaT4W21UmYSCPre2Xs_D4zHVIsN2a2pUI4KwyiKB87M6f14NKL6O2fgQ_4GHNW-S1CmVCm7BPvgWW1nU-PjXB-GBDqIhXqet0R9DKEatasFKjbfA0iQDqwPQUOHu0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌جالب‌از برخی‌بازی‌هایی‌که تیم‌های بزرگ تحقیر شدن و شکست سنگینی رو متحمل شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23242" target="_blank">📅 09:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23241">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=ThDSilrp1sClEcHJSGygSS-6gvF3suj53fIuVNNiH0Gk-45Wpx9tvLDn9XJ4XY_me0PhFd_Jr2ilP8Tdh1ohxMi2SsrlKwbqjNZiZIMhLGBmlIIfWyAHtRDkRQFetulnDy2Lfl2TBGuPXFhbKPe_qJyJN2MdsYxhlkISdLAaLcOA7lkaqmKOjObg_Zk7umInXhHCvz6YkJRcnKBL57_4nuk7SqxEOd9lCqibzc0p7HM0laxJaBuMC6PO_9ibdVz2wbjft-vj9ydLAz-rjwRYTQJ3HBO1S1UDEkccOnrywxbqCRVK-3JEixi2hqx3Cbeo-9xUGSRK2nOIsryB0CGBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=ThDSilrp1sClEcHJSGygSS-6gvF3suj53fIuVNNiH0Gk-45Wpx9tvLDn9XJ4XY_me0PhFd_Jr2ilP8Tdh1ohxMi2SsrlKwbqjNZiZIMhLGBmlIIfWyAHtRDkRQFetulnDy2Lfl2TBGuPXFhbKPe_qJyJN2MdsYxhlkISdLAaLcOA7lkaqmKOjObg_Zk7umInXhHCvz6YkJRcnKBL57_4nuk7SqxEOd9lCqibzc0p7HM0laxJaBuMC6PO_9ibdVz2wbjft-vj9ydLAz-rjwRYTQJ3HBO1S1UDEkccOnrywxbqCRVK-3JEixi2hqx3Cbeo-9xUGSRK2nOIsryB0CGBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مدعیان‌اصلی قهرمانی در رقابت‌های جام جهانی از نگاه کاوه رضایی و جواد نکونام؛ چقدر قدرت بیان کاوه خوبه. چقدر خوب و سنجیده حرف میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23241" target="_blank">📅 09:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qP22rSXI9Gd-0WfRvyXRejctAx2Y6XLk-V29rVatNO3RRqds1Gz4-niDYbzDWQoNp9P3wYh1oJMipS7kuy0EoHCVYr5xWPcVVGANpDo1LmVpqEJXZMb6KT1SVdEwzcE5CP4EHtGKSgeJ0wm5F0I4idgF4mZC0l7nETsW4YUK_BosxKR156PvehCFB6dVNlQpccf3TVA2UKM06ZVxs4iLMLUJ5Fpp77qm6f-_m2Eye9sif4XU83dOG3BxFGfl-OMdG3i-jj-7E9dHkfFTWg3c3jArBdzj9hN3avC6Cz200KXhxCsAQLgrd_yWkEBH7_FkwBZha3pLu-m6YYGRZbuclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: باشگاه مطالبات یاسر آسانی رو فراهم کرده و بزودی به او پرداخت خواهیم کرد. اجازه جدایی به همچین بازیکن‌‌ارزشمندی رونخواهیم‌داد. یاسر آسانی و منیر الحدادی فصل بعد نیز در تیم استقلال خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23240" target="_blank">📅 09:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=FxiO8LrxnWIj3tWNeGJZKaLs5-f6cvEVGQa_z4VFA6XFg7OmpYNwyYsr5A4d8zLMFJntGjrCaQL2x_aX8NXr-xsEg_AjdMkArD7hHYYLhESoupGBVIi-fvbZ5aiPi-5f4_CJfn4q5SShVjVE5dbFKAgct7znniPqsm3qineQP0scYVl0hviYsvkJFNMUshuQ1oPxSaKVuGZVjIURGeTzvxt2sVzioNgJSlvTcpW8hIuSnvl9m4_zCtlRl4g574pvu8so2XOE6LpY1xiWrMncVLOZZgutU7ZUP4iguUUQET1kKY3nafItquJfqSwwi7GDeeahmzjW61alJmvnIQoPOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=FxiO8LrxnWIj3tWNeGJZKaLs5-f6cvEVGQa_z4VFA6XFg7OmpYNwyYsr5A4d8zLMFJntGjrCaQL2x_aX8NXr-xsEg_AjdMkArD7hHYYLhESoupGBVIi-fvbZ5aiPi-5f4_CJfn4q5SShVjVE5dbFKAgct7znniPqsm3qineQP0scYVl0hviYsvkJFNMUshuQ1oPxSaKVuGZVjIURGeTzvxt2sVzioNgJSlvTcpW8hIuSnvl9m4_zCtlRl4g574pvu8so2XOE6LpY1xiWrMncVLOZZgutU7ZUP4iguUUQET1kKY3nafItquJfqSwwi7GDeeahmzjW61alJmvnIQoPOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هنگ کردن عادل از مصاحبه اخیر امیر قلعه نویی سرمربی ایران ازسخت‌تربودن جام جهانی 48 تیمی نسبت به 32 تیمی: واقعا نمیفهممش. یا من خنگم که نمیفهمم اون چی میگه یا قلعه نویی تعطیله و ندونسته که چی داره میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23238" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxRBLxYynzNYKj1XLenq7isPMluMx_l5nWBqrXjGCJ6jP5DP5Pk9ekNJcyxPslHN_Xbl7O8ovOn9VAgdohGxUbLLNVM51DYjoYyGI4Kazjz9XYYiGk3zaGMB94N6RGkXiV9P3BhNa6kQSX0DDO-bI1WI347lnbKlMqiXyrcdnpQXtFSkuAiUMTA6QQKH7MLcloiLnGyq0O8pIDY-skDeGju1SYN0ZEv0FaaE58a0qNRemKBvrtBIMdjOFl9f7HO0Lp8XmbkPvzlcBAQZIuJ5_lg040GZL58izp9A-DQ1a_yS1knACnnN1nQLrOzrBs7CtyOfKt_Vvw66FYvM6-O1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23237" target="_blank">📅 08:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23236" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgZXZh0IY_v-UdR6PhVkXVV0H_HOpoGqhg0dN1ipUfYhkhEVRMCqmAuc8dAbmuTLhcaOCqP9tfdz8cSmhKU42gnnoNLbSEZQWlwg_rX75UeiO3CWVyRg2hBWTtIVQt0aKHmqT4u6keRvER00dOhumGs3ZmWKdNfJi7AlZEvQJa7R_vvmdbSKBUKFyIzqckCwCHdvJSd8vD0uL1gewjPokmJna1pU92V4GozyyZWeUEbfRTcZ7VGi8mav5i3ykMslD7bP3Dw_zwh3jR9dyzVzYA0rFBwIqwUCKsTgl3fnxstYltKs2hEwn8b_zCbNBi5hdW8YHaShpeK06zAxXgA30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23235" target="_blank">📅 07:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbF4yPGyBpfaDC6iWFDxUOWowTChKtyVohALvZkVnqJfk6xyd1-Rf_qqDwYRfeUzep0NUudcvIIl-6DFsqiUcj8PGYRsOr229xAWYina86H0YVbJhC5wVsWTaEI-Liee2DmGA5jFZ6Yx8n1haHZRMPcT3Ppd0rXrE0xRDZusnvxXPX5_4JbCBwC8AhMAOPk02tHSwX5y0ajBo7Mk7EMQt-Ex3IwDmb8GNM1Swk1SXqhw9Y5Ae1JViqPUfhVXre8XS9uXObJloXjM7zTtha5ZZFxbY4aOv1tvSgcGQ7gKqwgEBgyUDtAE8rFij_oUCpUjFdmG8kxjyqAGHeNQFSIe7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23234" target="_blank">📅 07:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=pVXo0Pb7A4q6lk54jMlsuP-ZvJ_flmIbkPC2E3vAd0P7cV5PaTMyty25rdu0Wm23rXwSFJsv4g5gbF2mLUHDIGL-7J9eJNJBZs6nEJzjbWbKeTPtjSFnFF3fsbOunnIUzmxCHPLWvK8c70xrNy46AobvTcAxgy1cexka7dkqnbFC12DuDg5ZVFkE5xeEs2iha2xWgg-nhQoW7Aw2XvnQK_Co43cXnFD1XnmSeBjT1zg1tasmpJMeYlCg3eAklP8rURwSKbY3rB8PkreoIEuMT7G1CTWOL4BbEKaG4FGaXOF_fzBFirf7jGedVN-qbiEs9QV2A-4yM0Q336VR4QppXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=pVXo0Pb7A4q6lk54jMlsuP-ZvJ_flmIbkPC2E3vAd0P7cV5PaTMyty25rdu0Wm23rXwSFJsv4g5gbF2mLUHDIGL-7J9eJNJBZs6nEJzjbWbKeTPtjSFnFF3fsbOunnIUzmxCHPLWvK8c70xrNy46AobvTcAxgy1cexka7dkqnbFC12DuDg5ZVFkE5xeEs2iha2xWgg-nhQoW7Aw2XvnQK_Co43cXnFD1XnmSeBjT1zg1tasmpJMeYlCg3eAklP8rURwSKbY3rB8PkreoIEuMT7G1CTWOL4BbEKaG4FGaXOF_fzBFirf7jGedVN-qbiEs9QV2A-4yM0Q336VR4QppXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های والیبال؛ دومین شکست تلخ شاگردان روبرتو پیاتزا مقابل بلغارستانی‌ها
🏐
ایران
0️⃣
-
3️⃣
بلغارستان
🇧🇬
25|25|25
🇮🇷
23|19|21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23233" target="_blank">📅 01:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚽️
👤
ویدیوکامل قسمت‌اول ویژه برنامه عادل برای جام جهانی باحضور پائولو دیبالا، جواد نکونام و کاوه رضایی برای‌دوستانیکه‌نرسیدند کامل ببینن برنامه رو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23232" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=a1kWq10gL8-0MozUrJtgf0edlwRi22ehQfLKPCf8qqEChnHGfLMijoMVDmujiTTksUH1cUmOx_7YFUxT-nVIWN04vCCxTWuXEHp1CduUEoMyEMCB_I9pU8-KK27KR22-PlJiUBZ_x_-1IPzp8JPbSX8eUvZIQ5MbUCIXWED7JDqHf_3hNilR_ojPBaFEcFhHtNGicq1ommZFZEs0UJQmdQJU_CKavR-W60CxZYYY-CWe4MQuf4DcBkLUseCWjUtQmaGjvbV4d1hkPImpdSSILs2HxgNR_LbNn8MW0tCaQD8qPkhieIwGinMYq9ewiCYfcXcLJzKNwhRpKqh4Qqcacw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=a1kWq10gL8-0MozUrJtgf0edlwRi22ehQfLKPCf8qqEChnHGfLMijoMVDmujiTTksUH1cUmOx_7YFUxT-nVIWN04vCCxTWuXEHp1CduUEoMyEMCB_I9pU8-KK27KR22-PlJiUBZ_x_-1IPzp8JPbSX8eUvZIQ5MbUCIXWED7JDqHf_3hNilR_ojPBaFEcFhHtNGicq1ommZFZEs0UJQmdQJU_CKavR-W60CxZYYY-CWe4MQuf4DcBkLUseCWjUtQmaGjvbV4d1hkPImpdSSILs2HxgNR_LbNn8MW0tCaQD8qPkhieIwGinMYq9ewiCYfcXcLJzKNwhRpKqh4Qqcacw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل‌فردوسی‌پورخطاب به دیبالا: تو ۲۵ـ۳۰ سالی که کار رسانه می کنم تا الان با ادم خوشتیپ و خوش رویی مثل تو مصاحبه نکردم! خیلی خوشکلییی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23231" target="_blank">📅 01:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2aRU79qWGdisiqy4hzeHtcnvPLapDKzZSEjPQwa_CIsN0jT7wvZkB6Btrgrbc-YTsoI9JU2gDpWvC4PtVS_xdlCs3wdCaUH_qwREYtE2VgnkX6tZ4UBF4w75grnxSoojbgwAh8B-jxYeNxIUnXH1fhX8clVBeabPbP-OJGG6_eEGP8HXHU4ig4j0W1wgN7hhAkVeHkYTSiO13TaQyGvg4U3Tn3O2rgOmyRYMVGdcrisexvX6TK-2Umb7kkrnaUbYE6hUawArfZzqy7LunE2WYOkFVGAsS2yzVzwszgbx68BEwNfTA_qvaxHVyy4lWzv0yw4w3x-mT1BUsbwGS8n-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛اسپورت: تماس‌فوری‌خولیان آلوارز باسران‌تیم اتلتیکو: بندفسخ‌ قراردادم رو برای باشگاه بارسلونا فعال کنید. فصل بعد در اتلتیکو نمیمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23229" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-PO9Tg-OZZjZcWLr4op_RIHzU-9CEa0XVayEcW2qTq86rpNxuiCo3CwnLriWVRp7f86pG6Gth3o-ljhnJBjAhQ_DVogUP2ZBrVdMnvPN4xbPaASeXny4bNZ9THKZ15wLY0fP86VpKnQVxF20reRzgoM8d4Y9Tc18py3LIytoUm3hSFIppLNxAUO_-AHJunkDqRolJCCOLUn3jx-vYTo3TjbOkU7pz41_ww4U-fWlBzIAKVgXtIbspi19m2-feClbItZltcY54rlFz3A8S6V5A-4uBCT-jZaolUzDiaA3Wb30g05Qg16ps92gaNwh4zwHxzPo8D7LwftV-BHiVBEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23228" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bytzYqpaJfMo3vcEpHwre0HFPROmt63TmAeWND1jCTlLK-VODwuCRjCLXt27mqk7uUBFDHJeUFeCP-h_SbPzQ3m18NjuqfTcpjuCoSzV7iEZhjh2QkfJevOMMnhZehIczkA_Tmji-ig7Z3XzEa7xJymtmFGmROZwnl5xhukqOpAP1JMzTjERhsJY0_TXvsYSVnIAOIG2lloBNa-F_V31hqHtNjDboG7f6JB1or5Rm7cvuBgcsgntmf-6zMK6_KwmshoLMPlNWgGk8PwUP2nzVukUawB6ipRz5vzUocz2oIc4ETYmu-ou8aSnH5BMMJ7asdffG61VHAxfczTPg6j7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدارمهم ‌‌دیروز؛
استارت قوی مکزیکِ میزبان با غلبه بر آفریقای جنوبی در دیدار جنجالی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23227" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23225" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCCR7ww-wddGxPVZ2XRcZkZBtofq2wcLpR2qAn90ivTRC9z6WoUJpVSRVrmFRl9voSejSS4nYMCry6FewZ4bl4mEFgxssU383vwy6UP_2oZhXFlGeToPHJaRHq4zzNNae9daN4UwZ7hSLskmG6fTRfUPDcodQVXoRL4-h8z9J7TNlc9YNewaZBb8zhHK6hvGWw0gfTkTBgUGSS3_Uwe1NcqtLO6cXBykyLff13-4RXtdGwLyunj2y-3z64LfEUFv3Oo-BKKtZhl6gPEaAEdT4FuSyMTkZoJk5VcmH5VAgXaudzAfBQBbR9m_e1n2V1Z5HZlO-tRf5xPMNEkuLU_YKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ با وعلام رومانو؛ برناردو سیلوا ستاره سابق منچستر سیتی با عقد قراردادی تا سال 2028 رسما به رئال مادرید پیوست و شاگرد مورینیو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23224" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfsHV9wU90IWYH1i_K-VUcS9I207dMeb9rojWgC8lu5VKszg64KUOxQZ8-p_QPM8dTpZ6d93Ndfu7BBCz3HYz2UczAqY5mlHUa0B-7g4Y0RoTRTqyl1rI04x9vofKR6QvyZtQouxzFcNh06vyyLylDjzX_aPUT9j4GxNtfeqeGmDZdvDpd42gq5YIzPzE6Mu6Qga_PrkY1sfo2Fpvpf_tb96g_aoG60OEt6_UDxktORbaymGMnpScGNsZrU30BqvL4-pFUUkLx8anjgjJKzDRQJsdx4YrVsErjzROQraAHn9LII5i_nbRtK7rDhg8zLZFZ-6VuAqaQ9VzEtno4tyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIjVE5CLDeHzLJlKr2T74qXqBJ_lt_212sZKkjx4R6xa32xoFs7RahMcpkPUGuDNbtQ2QlkvhFqX0hDqxain6YcWilbdWQ8yQhBwuztFBmCx8JU0JeZdq3klgksz7tobeWsmuqm47bBDI-_mzpL6LdiLcdvfEK_3klSFbE3pQvOnwIaJovU65NnIJGAiTgv_LKhx6gij8JAR2-PpdFuyIihVKHicCmX3-9sGi92fhKLlJD4VtipIlEzQvpgoTXALwW59TSdeg9Ym_axe7lq-vLGe_7OIC1HDcggmEH7dBdJR7pjBwpuhfnz9sEedFApk8KyMrSeKcyzS-HiE7W7KqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23222" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT9eN4N33YSv3NT8cBpRUcAEuqBs4LLys9SZuynEAiXDLyT3BNIsWk6k4XO3BmM9i-NMswQdLDZGB6AYYlYjUt-drjKs6PIjx-Zzs9nd9hetjLaKls64Qb_e8Z4aTq1Ehygo2i2kbI7ciUKzxo2I5pZt4qhUyFhYVq70P9kVsN51xbgOyEYKlmcefnz0wbxi5VHbk97SDdW5c9vfMB3rVrAJh550tc7D5EqM3VnEvlgBWnVvCLwkOnCeRE4A4836HA0PdrBHe_mI986d-RKxc_n9Lp2p7y0kfP4YXQdNGR2eChlsHuD4UIK-dyVykw93Fby4wONZgTFFQFeF3Y3PvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حیف‌از این‌رالی‌دیدنی‌بازی‌بامداد ایران
🆚
برزیل؛ شاگردان روبرتو پیاتزا در نخستین گام لیگ ملت های والیبال بازی رو سه بر یک به برزیل واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23221" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq8SMvAs2t0WPBAO4neunU1e9Lbyr1Q9v3HpB0V_nXimH-bB7u0b_pUdw4_TcF8GjuHsEKND48e91eq12_EnRQuBZ9-x-z7tmdsmNoifEeCGqsEQTXNWpE7oDO-zr9qC_9G_tT756eZL4lM5U-dQh9XN4rcuz4RwS4i-lJZ09JMDUi4EzdPIAFBqWQk9C_pDAO08uqprCUHE5169OZuIeagY-X-UlfVe9gbuLpVUhCz4hemlnJF0GET6-rh6g7w42bEU_s9ZVFljEPfV9R8mILudFHm5HPEMMqVMmwQl7RPbSJ59Rakc4YD6b4kv6ow3esCdM4ykh-qPsnLHjLbWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مربی‌بدنسازباشگاه پرسپولیس ساعتی‌قبل به تهران رسید و از فردا در تمرینات سرخ پوشان شرکت خواهدکرد. اوسمار ویرا و کادرفنی‌اش نیز احتمال زیاد پنجشنبه وارد تهران خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23220" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQzbBhxHhqqf1ZjCDUxapOxFCGa0ByNmxBqze9tchGSx1_ONwCRdDARQaUJIiJn9yK0bn1JqGbum9QP6CKRPLXLVuas6I8CvDlVEv8D4F0PDC01e8qu7kasazMl4kdkVVfRRBfQGigO-v-fd6BabH15uWzxwJHQp0vv0E5FiHT_nypPAkUXvjd-Z9culcldFosZS4tvpahNtGYaJ7d9c_rAvta6revTZn9lXZ_khubu-9MVhrg-kAuUiNRzKnDydqipS1NIUDrQ4Z2n4dkOIgiGrerc5TRi0ssF2EhBnzU7O5_wB9qVNhi2M99NkPjFF6ExJohFBh8j7YE99SZ78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23219" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko_4uVFEIDl67SWWL4apSKYrQXrELfepAQQvRW9nKcXSzSxLEUfvLtoT96CdBCQSG7trj6CAg_C66uZV0Kkly3o0YSeAh85OhxPbyG4uRzgFluTVYE0Jp-8te_NK2jCn5KQdYXo7ZV11soyUqC-gx8fMYL6ltvhrztBWTSvLOB2fwAFzu-e3fr_j6Ei46bKc4GN83HwPYg7bQfQmNjVh1hep5PZEnIYAyIDkv62uZ17Py1p_HnBp3PFN49YblYswZUeOiph2jVs4tjzjwVk5yHjJj5EItevxni0rRMvOFFwhCH7Oj8ESX0WT9hsTrCy_G1QEsbLVqHZOQ_DS4QFAoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23218" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ik08dwB43mUl0hnQPKn9WicFGHNk9QQEE_XeTYTDsMeGN72aGTuH-XFktCOj-X36L7vwKuY822j1g5GApbZFu8ztkMw8QowSPiHUxahwwk54bcRZ2-wiFyrjX7EgW7SqWz-_9mfUnKnGfqylYz7K53CdsB94Mn2PnyCJRHNewPXvHVqmIu72Uz4RjXmCO_nPE312UioPPBS54Qo9qw_ocXrLd4WHfZZgcDEhnk5vap7vYcSSsf_lhL2rYqbRuX7YvNBTY4MNLdKue6Z3pHyN8LEdphyTcBznkFjUj2hIXsLjYLLy0FfHb8qRFhj_pr_UN4o7zqdMRXcpo-mij20ewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAPPqQXdOBzFzVBMWBYLBU2viMOPd9TCOMfcH4t6uU-xG-GsEJFJtNdczWwqU8rTxZyNUUOk0LVOtpGcBl64BRymC2bKI9WYfyUp4fkUJ9GyvUcTCrsTNLB_Td4t9dAijsFqfnaiMvTNQBsI3e3HofVnY8yvWw4XgWFU74bMqIrhj22KUhIbCtgVGNy36ztqmXS37jZ8Kyevs_Xiuni5ZUUqXNAT_J2jIo7_20AEdj-D55kGu4e0K4q-lUISbsyUQnHnnAbybHfDTBogmTeT2-q-R6YG1Z9HCuN2Wpl7a5nAvFD4b171j-jIenSVTFK_L_rrvN3IEpMBvPwL_G7r-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23216" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-eWiTdfKxjATzf3DD-_Hd1J8-xNQkCToKrZl1YJYwX15-3uMjrGyuXYb8Z20RCVe4NioBBfirOdtnJ1RIBNV4DuneDx2NZqVCiJrORDArhp_BPvrK2zw1K-Hi9xRocvZR5sJw1pb00AQRu_OzUYDHUFGBeXX0e37ngSWqLl4NtCd_Cf8RJos46u8wmw5jnxGjkgs1VbWTBziWASvACMbF3CXaaEdlxxHREetk-TRcsB3zageCuPqG7bfpxX163uwTAbzEaKp64Vzyz6myqDqI0NcvDpnQsZMwSJUt3Z1xyhuR9QSrCckN-0tcSkKw5jabCB2d1PBHXMWdQwvbsLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=ItLvzv6fbMHsTHZTmMC763jeToutpuD2CexbkHYcud9K3LcHIRMUy3-GpmCcml1rEYWNGo8u0NeIHHTQyfPxBqf58S2KdkrbkOXMsxroS8v3QfMy3JxfeZJwZEBCkIR3OUNN5QrD9_3srIQXUKNCzVVckO6aU0eMPhlXw7hosuJ-ZlyXc4csOmSfTtX0_qG-KHx8OIytCBJqtqsd5AziONUfLe7KbakwvZFcMe9YYw4TaG5hPLKgI7-9Ih6V0qpkqfMlvPiUw21ghVE6xz50CCsQsJQGX7r-__wyXmKgJmf9-V9ENIdVMgCL9PbyuKMPitY2m-yTISyGpPR0fPAC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=ItLvzv6fbMHsTHZTmMC763jeToutpuD2CexbkHYcud9K3LcHIRMUy3-GpmCcml1rEYWNGo8u0NeIHHTQyfPxBqf58S2KdkrbkOXMsxroS8v3QfMy3JxfeZJwZEBCkIR3OUNN5QrD9_3srIQXUKNCzVVckO6aU0eMPhlXw7hosuJ-ZlyXc4csOmSfTtX0_qG-KHx8OIytCBJqtqsd5AziONUfLe7KbakwvZFcMe9YYw4TaG5hPLKgI7-9Ih6V0qpkqfMlvPiUw21ghVE6xz50CCsQsJQGX7r-__wyXmKgJmf9-V9ENIdVMgCL9PbyuKMPitY2m-yTISyGpPR0fPAC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9bdQkeik6iqaJ24wVrewmPwFXcbvIYR1JQ5-b0hhSROImp6QKxuh48JtUAHlLY9Qb2PjFtt0_Av_nG_OmSxJaY_uhI-d0Q8IIOQXsvbt0hU3DbcFrxB1xtA6KtK3w3rm2cTQftvQgYgDUDaRjmlKeLsz_mRIQZWL0W2SsPtMHjlawh9alNRj85IKK20Dyixd34x9rroygs-WOToy_EHf56RkE71rTnP8OcqtygglgMEnkzUf11f09GIpmxq7dHz6Wywa6kEB8h9Yki1qvbTgLaqhoZtozplTx_Y8cJ09FHPpIQPodXDO93ZD9LKqGHi-DuAdD1ui2nnz76NylmH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇷
صحبت‌های جالب پائولو دیبالا ستاره تیم ملی آرژانتین در گفتگو با عادل؛ برگای جواد نکونام و کاوه رضایی از این مهمون برنامه عادل ریخت قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23212" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjECOPhk0AOFRovzAl6HqLHJnTIb5PZeE1CWR6kf08HROHHkHywcFpd6VmH1hA6dxAMBMqLKxDmYIJv_dQS8tv9bpoC8ySdx5UW3uTpZUqITffwy-vOT7MA433gfXg77yH6DmwQxoYzn6bo2AUaxPJ5lVx8RujffWWd6JSfbirBznZGSxztYyFBRcRmWSB4RiR0ffBx-3hwgvEqrCeTW47wtVrcgnIkUjrK2kGLwG4CIY_07m2QBxjHHA5sDjsK4aEmoSZ-e67P7abhrCVHTJAhm30psrJ9a3eZufVxrUvr47e8b50pRfzo_oKEdKo7_AlKYsO-RAdGD8HlKfV6yZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ باشگاه رئال‌مادرید تا ساعات آینده خبر عقد قرارداد سه ساله با ژوزه مورینیو رو منتشر خواهد کرد و رسما اعلام خواهدکرد که این سرمربی پرتغالی بار دیگر به جمع کهکشانی ها پیوسته است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23211" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAdF03rbP1luDh5MS4F1RVdrKAz49ndK_IA2lV5dYANOGSWYFd01_4nbAdrwLFouUlgYr5IlFFvoOwMBN-FDdkYv4lIaUkTng3ySVkvMxQrVIKbsvT6alQzyJxo1ocEcxnebPmwZKTCofd7Y0Je4klqiINEbbVOiOqAmGzup0BVThiGUGJa7vdq1gYH_JJ7Mm7WdOGJazHCcHnWtKUKAkSHg8JhJntMRwhcVbbDlgHXxc-cxfjFU1eWY6MN2wKZEJd_Xytjv5SjR4gvBn2fuZeFUCaYMOnxRytB7dKyvFXBQtVwYlfoXVvpzoCsheBKUDoeMsBwXxHlnuY4rEkQoxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23210" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=exXMGYYuUsdgon-J5scO_RHhHFhpzTi-vErLXMAYf-FetaLTbNjlCAXv9gB1_9VfN3s-PTDwoavMR4uPNGLhL0CPjqjpx_fA-qv51WONm4QTQkGJ0I4UnlJx_3D-egf1ysKqDOj_HqrqLntwMl1WUwb733Vy511X6a6uhR4m9x_9ywdmvwaU9oTn_7TBD5tRx_3iWIWB4QvyleaX7h3zgxCZW1MJXdrOt9EEOCfFTy-ehPYSX8NDTqKGh4M3Q8qm0aVUjo_TXrkf6DEdIxpU3apoNqZzBTf59UCEl4oAb_hKJTuy5EvPd4-Moap-off2c9F7a1bUDxKCMux59Dw0VLGLDHKQXULL9Pv_0Kp2l_yeVt3DY-F3kqYDQ0dN5Tg-ecX0KDrdT-mrcx4_rjPzeRKeyTxbh73fVKQHUT63Q6VLZMqXB5912DWrShnFB13LkJEb1nBJiwo2tKfVFm11TXsFKRAOxtsuKtRdIApyvn2jf_pCbOlgk134iZUyEgw87Nhf9BaClIAfF8yQC7NJL1k3wrtojeakaDR51DnfCTDjlt2foW6svMHbonGOmmBhxHMB-HD95lEjiyhOEhVfMLZp3nkczKex5-7r5O51QwnOPGrGOzSnavWXUCSRP55OmShjCdpsZXERPG3ooQc0lQJ7A1FPseusN_SR7a1uvCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=exXMGYYuUsdgon-J5scO_RHhHFhpzTi-vErLXMAYf-FetaLTbNjlCAXv9gB1_9VfN3s-PTDwoavMR4uPNGLhL0CPjqjpx_fA-qv51WONm4QTQkGJ0I4UnlJx_3D-egf1ysKqDOj_HqrqLntwMl1WUwb733Vy511X6a6uhR4m9x_9ywdmvwaU9oTn_7TBD5tRx_3iWIWB4QvyleaX7h3zgxCZW1MJXdrOt9EEOCfFTy-ehPYSX8NDTqKGh4M3Q8qm0aVUjo_TXrkf6DEdIxpU3apoNqZzBTf59UCEl4oAb_hKJTuy5EvPd4-Moap-off2c9F7a1bUDxKCMux59Dw0VLGLDHKQXULL9Pv_0Kp2l_yeVt3DY-F3kqYDQ0dN5Tg-ecX0KDrdT-mrcx4_rjPzeRKeyTxbh73fVKQHUT63Q6VLZMqXB5912DWrShnFB13LkJEb1nBJiwo2tKfVFm11TXsFKRAOxtsuKtRdIApyvn2jf_pCbOlgk134iZUyEgw87Nhf9BaClIAfF8yQC7NJL1k3wrtojeakaDR51DnfCTDjlt2foW6svMHbonGOmmBhxHMB-HD95lEjiyhOEhVfMLZp3nkczKex5-7r5O51QwnOPGrGOzSnavWXUCSRP55OmShjCdpsZXERPG3ooQc0lQJ7A1FPseusN_SR7a1uvCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23209" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709c123d60.mp4?token=mBmb1cFoIpEKELe0seMmp6ACVpd2vC7ccmEOkRrn9X2cST_JsJAeK4JRlS4borLydWy7bAycuU0Mq_UDkX5jfqRnmQ9ATouvWVUsIE9eqno6_FSkuighqnzEM0BUlX8gmv6pVHGe3SAKw9AlAf-FRaUdnPdBgeqtOVnpmpxzdD8n3k0cPcKosxbZhJK55iHaOuawTesQet_dkFTmN006qntIT-tbZVEsvMeAz13BazJf_QDN566lUIYWec4JaQVKKq-t4ISnN4evqW37k84QlvHflXx9N7MdX1-D0Z59GfykAraGNL18FvtdC5Qh_VsOVmMMI2NZSRnV9XbPhINxjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709c123d60.mp4?token=mBmb1cFoIpEKELe0seMmp6ACVpd2vC7ccmEOkRrn9X2cST_JsJAeK4JRlS4borLydWy7bAycuU0Mq_UDkX5jfqRnmQ9ATouvWVUsIE9eqno6_FSkuighqnzEM0BUlX8gmv6pVHGe3SAKw9AlAf-FRaUdnPdBgeqtOVnpmpxzdD8n3k0cPcKosxbZhJK55iHaOuawTesQet_dkFTmN006qntIT-tbZVEsvMeAz13BazJf_QDN566lUIYWec4JaQVKKq-t4ISnN4evqW37k84QlvHflXx9N7MdX1-D0Z59GfykAraGNL18FvtdC5Qh_VsOVmMMI2NZSRnV9XbPhINxjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور تو ویژه برنامه امشب پائولو دیبالا ستاره سابق‌تیم‌ملی آرژانتین و سابق یوونتوس رو بالا اورده و داره باهاش حرف میزنه؛ صداوسیما هم داره با خداداد عزیزی حرفای کارشناسانه میزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23208" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hk4KgwQIq8DGv3v4OTHbrTXUblS-69TIBz746BOOGsZnL95nmOqoG7Dc-_D4LIvFsADntFBTzKEd0dtvxf82xbZTigA_ELx4NdIseQY7NYPddFT0AEsl905otSO44LrcKj7QtPK6sD8w-68oS4n9ZH6czuuVZsdYhY0EvFLqyG8fxwrZyTnWvo1IL1nwr4MBKV7c4RAEmWqZgwsXPkqlX7lwtU_Psn3GK8oaBr1-3wjFu-1jEVA2AB9L7NinTDj-r4rtIKr3BsdmKv-b0lgdfyOO_pak2fV1SRdgNOOXxyksmgEY1UQb7I7eBJxquQ-HDh9Q0TkMoYr4VKi_XGCQAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23206" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArqXrQMmccXQDqsvmumyia5w0JA5tcRx4omjzzZJ1w6fkeSi2dEvM3N4gOLQFnIuo_SgW4tV6sf-O37bONcAGZOaS5oHGQDHI2XZTSny4oJWztsln7lrnTXe8NcNnIOUw8YtgqoKxNCUgmzZ7uItZfoqJPZvNcUWFF9oHFGJMRyUwOGmkj4wux_-TrhjOgi_c70Wm1jzd23DfHs6dUFMSTGSPqGpENt4gorgAObyf2N47daS8nggJSUg4zSEx0LYrEk2em0pXo5_7RkLjTwlyixlRom6Dd7Ms2bLV7ocp9ZxC7e-IU4lSkn-6WkrIoqv-ThH5Up_1n7HRm70SdSW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو: باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23205" target="_blank">📅 21:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULmVf3DRhe4EGV-8gZpOw6rP--JYNx4WAlWvOb1ueH62GWXE10Po_dDdtcexJ5a-tDJMemYf1U3kLVDsTNax_kSJnXAikin5MymmXieeoskSQFcbn-8Pg9iHB_E37wCkskIGG9a70nKzyHsfYpmmRNEewYYHMrPe2oPaLIVKl0Y_owYnkAfKD2JtHsx4sNpz91iEMknjV4MF9SWZvhXld8MzpcjGEVGMnP8E3SwZWjmZZBLuwv3fiHM4m_nFdMOVKc06UJUr3_ROFGqLnA2srEQPOvYlsg12KUl0QvlUJVtiFLzg_Y5gk2Hrj_aWPuKzZQfddMSj8mtqTEoiso2Dxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23204" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZDkWSw-3rK8qbzJVJvCqCPp-05MmS_wZxDLnGKzuDGvyAUQxmiMv2J9IQuolPbBwhHgQ5frhb8wezHwOUjJP51qASfSwsLO8aTiFC8mWeiAqjvAeHMi2JlSmZrV4mU6mm575SaG0bh4-lVRKdI3flmVMVotFZnBGZQgIRlhSZSDTRAdfAnnz5JuWTFXXfKU94XPNAXdvX-Byb6j4qIZPrl6blj8Y46PvRHW5nLqdchvYxBT4hrikayn3Q4WfzOyVAibn3EyNhSDRbfKC22KK6hlWqV-qkj_xQUUkoJYbY08FT96-OahnYWYGtl_F4CNpCP5rlcN60hjmFhwTtQ5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23203" target="_blank">📅 20:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dD-Q6e0tGClPCiwAhx_j9UjQrSrUffpaM5fKGMmkMuZ_Ij78OdHJWYimUXpWe865lHWydXTMWwxY9vnHEn9O4KjaFPJwa_c8gpjWoe7_xbBqx8QI8FTfbbKKVlbXBQWJHDWFikSeGMNZ8-LPuv2vp3IJnJNteih0xwAo_d9B1PzgM8mHuO7klbrBhshAIy4Bee0I77GcTMxfv7tVS3oSQ_yxQ-dOQNNj_NEubke5ph3Y71RPdHR77S7yXzO0vAE2j8jsKk30dwO2-ZkPPmFYqd_km-rGhO6X0ad1HjgANp9j6_67LNO-6lvfotk-yeZQvGZ4rNwglfRUp0ho1Wd7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23202" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4iZjHW2cDB8gOIQQ8qFmRmuBGLB2SYKhVV7qvlGdyUmge7vM-58T65iKtCyktgZtNR_pfv8mXB2G69RyfrJXRLW4xuDjP6-a-WijPu9IhKY8-8-j2vjyUPxgjll2voAFZDwpenplj5m6SUSBtsA5qDPvpxifmTd1dwxgkrYPAZXz957H_UJBqWUtJFG2CvmfCNeHS577czBKNd3Ac72k8rnUwTb7pkQv1-beb28FRMQwJpP8sCMxrVgR6ywiEuTlVaM4Uv5A-iHudj3LmkMtybnS5wCyagFBGns5oXrc7ObxWqNODmNEfi0xokHCMGo0d9Z9P2BWTZPIeG8t9XFjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو:
باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23201" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj364LHKWS3X0O_dUEeEvY3_0s8Cg_Wkmps45NODL2e0rAyHjBUK2BqPZe3eg_8cF3b9s5TkxNosL_bLAjJoH1O-kT_R33zbHMcMAwRJX8w70G-wdqJzmuH-rIPDHleS3DL1XQvj_HPGZ2FwRrLnv0qTfdGBeflen7j3XrcnpjhegKkXXjfXfH-jjzJ0JFTTiC8kzMzPynJawhIbL08Eah4fEXc8IX0W0ikFw76gyIUk4posZZc8_osH19Ra1CeKDeBAs8O-slxc1WZrpBkCc904N3ICmS6VOLpNSTFgo5HDwBgEfPh8i9GDgcE-GVJYzo9OEtv25VGwJpIctOg_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقا از طریق‌کانالای‌بالامیتونید مراسم افتتاحیه جام جهانی رو بدون سانسور ببینید. خودمونم سعی میکنیم در پایان مراسم ویدیو کاملش رو در کانال قراربدیم برای دوستانیکه نتونستن مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23200" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwm34Ey59-2pCg9AW1p3Xk_IO9xac89jlx_1XJ_cF6R6aUNTzESP3kDS5Gy1Zl57Rcs2O_Ir4n8Ta7ZIXhl1k__yodpRPTOImfLsOcyKjpp_YKK5xol385EP8yaxx-e-SPAqa0trgRqq1UI0f_F846JnX6wlyW7KJ9J2_M_svoSJ41Z_NwtqrZKBm7RnafgYSI5gxizIZaHrXWN6oacEiI-xIDw20utPSvkYuiytvDqULg5jgQqr9xAdagg4QobleVISBiqYamEUZjUTymsx0Vy7I-5BHb94M3kgvMZV5U2Dc0lr1L-xj781eTekNe33-wq6dDVbrcskxp7hDLoUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان: بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23199" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23198">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjdTcAHKTv9kkF0geTPe8X80H0hKA5fBoNEkHjEw9SRrdV4nYDAcsQ8RdEmJuiDelX9eocesWs2bl2ZPvaz3LN8sujsN2ceX1udwA3fWEqfEifBQdO-4O6LLoD0C_VtrFmhUmaC8bjGiY4j4cWgk0PpEiGikJJ3miKwIypaiTDGWrbmzZJn_nyKwYFWYpTFaG8193u4DTMje-YPcwd-hbYSRrYDMv2yEBkK_0_ShyFA0Ia2H795PI2rL3ep3AQufxf6ADul4AzfdTZoUPCxmMtAk7wzGf5zU-oHZAqRKslnTOsIi0rcp1I4kw0HM_fzg7XLUSJ4H6xq1Ch094Ac5bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23198" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23197">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAYRthOwZWStrIguAt5R-q-gkI_cDiBfN_K2QsJfDQk3FauqKuzjXQY7NZ0DOIEt7cGDibitWgGQUDUmEnlqCkyqnE4AYDEfy6nwhi9NS60iL39rtrDeH3pzEK_SSqoFPp83_TetQMOmKMWeL6bXSkGo1hTQMWUDxsXqo51rwOfS80C7jBH-qY4dhht2pd6EMHnVQd2iHEiTc5S2e_0KEfYkhUbZY4mcBuUlyTuaS6RBDyE7iTT7wAdEL1DJ-1dxOJeh7dh-AXnN6med2icOe5L72lOH2QxTe5zzsXGinifxwkr-WJvHmwS-JfAUnCiNAuXxY8zm_lkZQzCnBpP_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23197" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23196">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f4ZM65OYSvz56Z8pgvkquXtFP7sEqU6FKbs3tb_6d_k8X0FuYkUmEu-8tBKsNzTVDgmolJZeMWkIIm-5ufMwPEJje5J9FSJvsa1wKYf6IJ19i4XsZxXbWU8FCvShAVky4l-l-jjlXpNP8ZYe-Q-5pvpRzS0PTab3oY-K0rZNcAtzW9EYR9tAdxuuy5Xk4mOEXo2TYaPCfMaH5VjTeVNo6dEKJZv4JwWreCxo6mJWNpyWUuyzGivA9kyOxF4Ne0w6nJbgKkcFhqbv8p1_pXvuCCs3zxm-K2GDw4XaO0zjN2Gu5DqhLzWKDlhrylt6UaEfbyoTAfQpg2bxOL2jdsO68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌افتتاحیه‌رقابت‌های جام جهانی ۲۰۲۶
🔴
برنامه افتتاحیه در مکزیک
؛ پنج‌شنبه ۲۱ خرداد پیش از بازی مکزیک و آفریقای جنوبی؛ ساعت ۲۰:۳۰: آغاز مراسم افتتاحیه؛ساعت ۲۱:۴۰: گرم‌کردن تیم‌ها؛ ساعت۲۲:۳۰:آغاز بازی مکزیک-آفریقای جنوبی شکیرا، برنا، آلخاندرو فرناندز، بلیندا، دنی اوشن، جی بالوین.
🔴
برنامه‌افتتاحیه‌درکانادا
؛جمعه ۲۲ خرداد؛ پیش از بازی کانادا-بوسنی؛ساعت۲۱:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۲۲:۳۰:آغازبازی کانادا-بوسنی؛ آلنيس موریست، آلسیا کارا، الیانا، جسی ریز، مایکل بوبله، نورا فتحی، سانجوی، وگدریم و ویلیام پرینس
🔴
برنامه‌روزافتتاحیه‌در‌آمریکا؛بامدادشنبه۲۳ خرداد؛ پیش از بازی آمریکا-پاراگوئه؛ساعت ۳:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۴:۳۰: آغاز دیدار آمریکا و پاراگوئه؛ کیتی پری، فیوچر، آنیتا، لیسا، رما و تایلا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23196" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23194">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRJWvKvXIfUhUY7sYxMB3wNMFVN7-qwgM0_E8ItQI4ADuOH1yvmAkjVV3KqWPMOMOqJFBjYgrhQSa3ZoRdv9wVg3NQArmVyeUqa4sTwfh3f1T3wk5FNYSxAKV4mDVXRmS4MAd3K90fjAxbeCmno6iAKNUbmvnea98RpchaxWvxBfWuGJWjxUY0Sku3VvcIjIh1J_4NKPn0AyelbZCI2Xu8kbVdaPP-4QNfynN3VqMyvi-lcevOT8Y9gAfhhmmVXSGdlQPICgR6ZOODTWJMSznDGuB9APY2UPfdLXjip2QrrVi9TJzotembM0GePRVOM-brGgjOaG0wMIH5rnrSRs0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23194" target="_blank">📅 19:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQD3rNhTI5GtA4i5coQXTIv3bQf4yKuSwWRkU55QEXKGSwTyIpbSvEiYM3x1pgNghr-MvTjI2_o0tIIiPQRoNhhtiJn-FeH-8hIrGhAsx3UJvOZV9vCe0wIvM5Igg4gb-FDxQB26irYGK17d9RQon4Hm1vxcEMZFdRyR-udEfAtXb644e9SPMrw7qI_n6Iyz1LoFoqKCM9W3rXF-8zdPgCkLn5T6BN4Dxu05_HdThnfdSo4p9SxXUbZyYjgdVCFqt4COY9xxlYjNjj7BeOErO1Oo06Y56K8sf-FiRrq6uXAtyesJa-B3vapdnIZFixL3v3kvfzcMFiO4FeiqsBOcoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23193" target="_blank">📅 18:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=WML5WYowlEJJhsEfCMEktobC2E1uvzAj9sHb6Ib75iusG8ynFRnoZxGgaL4oMfMNhNfOrdeDcEZtXQ89A7MpmT9Xmo-iygWaUeJuyDHFXlS8xJkvLPX2_qmnzsNrVBKz6EDtumxiWeZjgeNvvJoBuVDoZBpfY3EVyGqvoWjtPzAdDakgNeu_cbd2yqu4YpCMd-zbY3sRC--ybZzHmlKHx2uwM3cKDdVSMsbakFJ3jT1dJzKTIm1T8vG5_gaGR7Jstllklu-nFZHXfjzEwP5P1ERUQrB4lLJJos9rD06V_GRaqQS_cA7uqihgw9NieU6QuLBVhCRVPTVcTapiGD0kPrMaWtf_Y_Q7WjcSE9YH0IyuspChySEBuThpMJLQami6rT4veOKchyQ5Ud_PJl5VBRzEE6E8SL9_b_uda9APvg6mTaKG8XpQVOWx6fTKZbGqBPtezPs7-hPyqGgx5rTHYIiPxEAFmGl0h_HUWJQ2lv_EcbA8UgiEcC9OJIEfryd0F0KbQI1YBdXolcRUpikj1_ZDUXyNKYvUJD-CULkE7xvjH2GhWatnpbdjrPpKHDQCECf2Ykhd1yv703XUwXIoBiHoRJ04MLbqy_o9gkEdyUyuSnhRKMLII0QOpaMptiudpX4J4Ne-5xKel9P7F1MkcedQoiNOV_FoICGqegfgFAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=WML5WYowlEJJhsEfCMEktobC2E1uvzAj9sHb6Ib75iusG8ynFRnoZxGgaL4oMfMNhNfOrdeDcEZtXQ89A7MpmT9Xmo-iygWaUeJuyDHFXlS8xJkvLPX2_qmnzsNrVBKz6EDtumxiWeZjgeNvvJoBuVDoZBpfY3EVyGqvoWjtPzAdDakgNeu_cbd2yqu4YpCMd-zbY3sRC--ybZzHmlKHx2uwM3cKDdVSMsbakFJ3jT1dJzKTIm1T8vG5_gaGR7Jstllklu-nFZHXfjzEwP5P1ERUQrB4lLJJos9rD06V_GRaqQS_cA7uqihgw9NieU6QuLBVhCRVPTVcTapiGD0kPrMaWtf_Y_Q7WjcSE9YH0IyuspChySEBuThpMJLQami6rT4veOKchyQ5Ud_PJl5VBRzEE6E8SL9_b_uda9APvg6mTaKG8XpQVOWx6fTKZbGqBPtezPs7-hPyqGgx5rTHYIiPxEAFmGl0h_HUWJQ2lv_EcbA8UgiEcC9OJIEfryd0F0KbQI1YBdXolcRUpikj1_ZDUXyNKYvUJD-CULkE7xvjH2GhWatnpbdjrPpKHDQCECf2Ykhd1yv703XUwXIoBiHoRJ04MLbqy_o9gkEdyUyuSnhRKMLII0QOpaMptiudpX4J4Ne-5xKel9P7F1MkcedQoiNOV_FoICGqegfgFAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23192" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fawyENoXo4Dbagf48tRo7AQpiY_lgdW5Deo3i3niv2gV8fiMGEb84hR1goUrChzW9peZ0GrXWxwwqsP_RwFx5w3A6ziYxYBT4w_0xuplpdbUafWEGZ3UjQ2rd7fRbFeVFmvjMmU0qiuCxjVmbIgfTHkeiHBRWVHRdzYDqQfbrxp7pKxe1yB2nB1-CHA_rjCjwKOAfIKhLQpfsblhnHhaLMW7F7EE9TCVGtM99GrQ8_STnbsMDnaZJBurhhQoUMkFOOdOZ55WFqPf60lR1mWmyYt8MYr3hdPVi5cDZ9duKoL4kpnv0UW5KW1lhC33VHKAKams4AD6WPBTqOaszovx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23191" target="_blank">📅 17:46 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
