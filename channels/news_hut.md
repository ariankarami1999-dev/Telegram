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
<img src="https://cdn4.telesco.pe/file/Dg0WRgoEdKlhP7PkANmk30b2tUpDP2uTWXcP_2g0PQTAYNGRLZ7wxRcxfFbDvfL1GQKUek1aiZLQ5k0KGbIZEt6qHlKI7LMcIQBpHpQQc33iAykfZdNp_RbMrFsK8bDl7zaxL00WKL1Zn0DWsZKxfIjvq3uddGLuQu34st6Ht89nbr8_HRYSR5cexZ0ysWLKSXxR8XjqF62fPMobkncO3UbPIjStevrr2E3c6DJrarmNqfVPMC8dcQjjvWMK_3td4_rNaadVH5_rzqctO5bIz8PAoBqU9JvcSDfDoDk7VqjqIwvXIAxZpF60KdXmKKOCtk2bGMXo3qxiDWne47L4Wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-71950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=EkcGwG1jW3i-Z6rbPlQM5hrE9HN6PmXS_sfpHqtx0cYkB6qqO21AJv52WMgJv3cpuKEO7MXvc7IABRzsJikmmY5S9PyNe5YeLoirR6gzN_tSe5UoQ4p3MABIOyfFk_yct6uVNJg3Io3vGrS5HA7sveFnF_HIJkoRJ7X_ESE9i-YP-4JkFFuUeq3JCZEP8UEZ8MknUlBBofFES-07tTKA9dtvIerX_oUP4yRlH2PmDk9YnNhWf-RFvrb_636p8EzCL7Fy47U4yNU3zz5g7xSEVfPip7yvOo0O3doqVa1jD0iHj2bjCdnXXe_vcYuRY1Eq4D0rYwvlPGZ3P34zaaUulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=EkcGwG1jW3i-Z6rbPlQM5hrE9HN6PmXS_sfpHqtx0cYkB6qqO21AJv52WMgJv3cpuKEO7MXvc7IABRzsJikmmY5S9PyNe5YeLoirR6gzN_tSe5UoQ4p3MABIOyfFk_yct6uVNJg3Io3vGrS5HA7sveFnF_HIJkoRJ7X_ESE9i-YP-4JkFFuUeq3JCZEP8UEZ8MknUlBBofFES-07tTKA9dtvIerX_oUP4yRlH2PmDk9YnNhWf-RFvrb_636p8EzCL7Fy47U4yNU3zz5g7xSEVfPip7yvOo0O3doqVa1jD0iHj2bjCdnXXe_vcYuRY1Eq4D0rYwvlPGZ3P34zaaUulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برخی از مقامات ایرانی همچون موش‌ها پنهان شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/news_hut/71950" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ درباره ایران:  در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.  گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.  بهتر است درست رفتار کنند!  @News_Hut</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/news_hut/71949" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71948">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=SKolgHdKNnYmfvNhjk6ZRPP5OPPjZNTxhZopeuooi2EB81-cq2b_ezMUtl1i9oXiuZEKBOf_nGP7_eHWtPeo1uCQObm_CAs-j6VS0hn11NyYcArovr-wpnhEMmdMyzJDLF77aEjmoCXYfGaQAnpl6PFP-WvL1HosMFgn4Alk8S65PguTy8-HCPT6ER_UEvACLlM5FLHTr9TNqX9QHGiXfLV7I-FtQbBqAWWB7We1dCQJYl6WQF9FAPR2qPjd-HfnUEtNWNpOUBC339stOxpW887by4lsxmy721rraWimbotfcCEgfEuaioCxSooRb8BlJrtM7sWUrqDA9foxd7gD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=SKolgHdKNnYmfvNhjk6ZRPP5OPPjZNTxhZopeuooi2EB81-cq2b_ezMUtl1i9oXiuZEKBOf_nGP7_eHWtPeo1uCQObm_CAs-j6VS0hn11NyYcArovr-wpnhEMmdMyzJDLF77aEjmoCXYfGaQAnpl6PFP-WvL1HosMFgn4Alk8S65PguTy8-HCPT6ER_UEvACLlM5FLHTr9TNqX9QHGiXfLV7I-FtQbBqAWWB7We1dCQJYl6WQF9FAPR2qPjd-HfnUEtNWNpOUBC339stOxpW887by4lsxmy721rraWimbotfcCEgfEuaioCxSooRb8BlJrtM7sWUrqDA9foxd7gD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ:
ترامپ می‌گوید «احتمالاً» برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل آمادگی دارد
😂
پزشکیان هفته آینده در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/news_hut/71948" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71947">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=pITFxTs2aGCbyhCbLh9x3XovmVvNg7dKuiDQsKgsnKc1bpQllL2UR71IDcGt9Qdt7W9EotI8rtKbdKNHAnmCF_ap7SBeB0cvIfieJeDwdRntydKsz83sa-QowA4SwP_soGo-ILCingEJex6TVJUk-1Yvq6_Um96vomdKKg7J561UUkUcuWevrjvz813bss4YQznaOVT8g6dEO5zE_RhPytyjZVa7nE9AIoUxZi8ImgtN_5IL8690Ya13ceCVEMY7NpeV1ZNt7KEePDNI0intHN-ef-ALDhyazXrN6eWgkShKMrvRQTHTOLMru4991YF_vKGBhrhlRh6oPCYqJGFA-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=pITFxTs2aGCbyhCbLh9x3XovmVvNg7dKuiDQsKgsnKc1bpQllL2UR71IDcGt9Qdt7W9EotI8rtKbdKNHAnmCF_ap7SBeB0cvIfieJeDwdRntydKsz83sa-QowA4SwP_soGo-ILCingEJex6TVJUk-1Yvq6_Um96vomdKKg7J561UUkUcuWevrjvz813bss4YQznaOVT8g6dEO5zE_RhPytyjZVa7nE9AIoUxZi8ImgtN_5IL8690Ya13ceCVEMY7NpeV1ZNt7KEePDNI0intHN-ef-ALDhyazXrN6eWgkShKMrvRQTHTOLMru4991YF_vKGBhrhlRh6oPCYqJGFA-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.
گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.
بهتر است درست رفتار کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/news_hut/71947" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71946">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=qLwIUsvPymQIVqMeP77A6QHMzKO58kVdmdwVwAvEahWmLK8lnRmXrs2Iag0dRqMu4WL1ZCDTSDxo4djuK38M53Ng6tH57ZuviurvpHDX5NMHgSHeGh4me7y4h_USnboY1IEfPTfANKoY9xbSMxT-R91N_EUHC-AfeeG6SzG1Yl04RARp2pUzyTS00O1L4yCmODxYdrO45Ij6OHO9ViG2MkXymIUwi-GlY7imYhY4Bg44MXHzPKAR22mKJWs1jrklGN8TLcjMYSoxDZx5V01HFTn2jjFrtNXt3RAHt2mwClojxNug7oHH2wYvwfFQ86AerB5nGUpX1A5GOfmgGi5OJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=qLwIUsvPymQIVqMeP77A6QHMzKO58kVdmdwVwAvEahWmLK8lnRmXrs2Iag0dRqMu4WL1ZCDTSDxo4djuK38M53Ng6tH57ZuviurvpHDX5NMHgSHeGh4me7y4h_USnboY1IEfPTfANKoY9xbSMxT-R91N_EUHC-AfeeG6SzG1Yl04RARp2pUzyTS00O1L4yCmODxYdrO45Ij6OHO9ViG2MkXymIUwi-GlY7imYhY4Bg44MXHzPKAR22mKJWs1jrklGN8TLcjMYSoxDZx5V01HFTn2jjFrtNXt3RAHt2mwClojxNug7oHH2wYvwfFQ86AerB5nGUpX1A5GOfmgGi5OJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهراب قاسم‌خانی نویسنده سریال پاورچین :
تو سریال یه اصطلاحی بین مهران مدیری و سحر زکریا ( نقش زن و شوهر ) بود که درباره " کوه رفتن " به هم میگفتن؛
مثلا زکریا به مدیری میگفت بیا بریم کوه، یا میگفت تو اوایل ازدواجمون بیشتر میومدی کوه،
ولی اصلا موضوع کوه نبود و داشتن درباره رابطه‌شون صحبت میکردن.
بعد از 5,6 قسمت مسئولان صداوسیما متوجه شدن و دیگه اجازه ندادن این دیالوگ تو سریال رد و بدل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/news_hut/71946" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71945">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=vgyGv5E_b3phTBtrCHAhylLzJB3w2icZgiaCzMArL8bbrJM4n77TyXSpbSr9eWlJG3We3lvgwQFUQcA-vtIh52JYh9N2LDVM0J_Rm_zgvjKZFOGzifyxz0YdpbzTXWKie83APdtno11hvDE8xFoEkrxsw-VLyiddD2yQjVWGzn90F0s9n8E0_prPNdIPARZ1PXzK7RqLxzuu0FJvRu45i7-qD_WEF5sGpjGf0zfIRCUhfwtGHzSaciThbcHUH379AuQSnID56Dm-6UMB-6y7lvXyJSIMzIE9mAYh9nNRGBbc9Ip82wFqlibqPZvSAkY1icGj-mhzJyeG4s5C60H4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=vgyGv5E_b3phTBtrCHAhylLzJB3w2icZgiaCzMArL8bbrJM4n77TyXSpbSr9eWlJG3We3lvgwQFUQcA-vtIh52JYh9N2LDVM0J_Rm_zgvjKZFOGzifyxz0YdpbzTXWKie83APdtno11hvDE8xFoEkrxsw-VLyiddD2yQjVWGzn90F0s9n8E0_prPNdIPARZ1PXzK7RqLxzuu0FJvRu45i7-qD_WEF5sGpjGf0zfIRCUhfwtGHzSaciThbcHUH379AuQSnID56Dm-6UMB-6y7lvXyJSIMzIE9mAYh9nNRGBbc9Ip82wFqlibqPZvSAkY1icGj-mhzJyeG4s5C60H4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی :
100 میلیون بشکه نفت تو مملکت گم شده !
کسی که مسئول نظارت رو این موارد بود بهم گفته که 100 میلیون بشکه نفت رو نمیدونیم چی شده. نه تو دریا ریخته شده، نه امریکا تحریمش کرده و نه دزدای دریایی دزدیدنش.
به نیروی مسلح، قرارگاه فلان‌جا، نیروی انتظامی و ستاد کل چه ربطی داره که همشون دارن نفت میفروشن؟
اطلاعاتی نباید نفت بفروشه؛
اطلاعاتی سواد و فهمش رو نداره، درک نمیکنه. اطلاعاتی‌ای که 50 میلیون حقوق میگیره، میلیارد دلار، ترانزکشن، بیمه، حمل و نقل و این چیزها رو نمیفهمه.
@News_Hut</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/news_hut/71945" target="_blank">📅 16:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71944">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=ZCWXrDVBOtwqQtsLOGhvLNjF7PRW9993APlb7hJDlEOyGoC3KPCqEX_Rj1NMC9EC5mevckeQG0aERwJV7bUy9lUaql5eb4ZUg0nuHayQH5y8juoyhxFXag8jIks9UWmmTQliJ05gHjW3TfDpC_vn7GtJbI_LhvhFNZMHx2IuuhlY2xHu8daDgGusHNz4K30lohvmp7LmvrkE0luIuNe65qWIE-Z-Q3QPXKIHXGCUqVE9Q94BRigXAJSoML-FP402igLATrB5PiPGrSGIRi872Cn_-usu-aeNjZXDuFDYSnxlTdixNpEqm_XOdLsMJ0WsvJARzrHb1Kdflz0GH59Z_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=ZCWXrDVBOtwqQtsLOGhvLNjF7PRW9993APlb7hJDlEOyGoC3KPCqEX_Rj1NMC9EC5mevckeQG0aERwJV7bUy9lUaql5eb4ZUg0nuHayQH5y8juoyhxFXag8jIks9UWmmTQliJ05gHjW3TfDpC_vn7GtJbI_LhvhFNZMHx2IuuhlY2xHu8daDgGusHNz4K30lohvmp7LmvrkE0luIuNe65qWIE-Z-Q3QPXKIHXGCUqVE9Q94BRigXAJSoML-FP402igLATrB5PiPGrSGIRi872Cn_-usu-aeNjZXDuFDYSnxlTdixNpEqm_XOdLsMJ0WsvJARzrHb1Kdflz0GH59Z_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
@News_Hut</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/news_hut/71944" target="_blank">📅 16:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71941">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=LDCLqHK6YbTvv78GLfhl7khkWrX2mzMxIcu-Yf5DT5T22mr0Vc5OVBbbBqw-zf71vKxw5sHYFP39hdAu71sIXQytI3UK-mNMMdqWeo7Ywk2xgYjvf7IT-g1UnyyBb07wavDNnqdqhHCcp_AFxPQXSNfkOLAcqdUu-MXmCz4BeItMgn2rPveLMzmpuE9o4AumpY1zleu6Fnl5U-JwQ7BOd2kdexHHr8BPRvTNTdqn7jRNYNzX8k7411j970CCWgWx3nrfq8qx0_W8i9lI0awnyp26ldUq6qmiWDnkkas14wVvZ_6AGA0hQOigdF2oHn6wdLTvfMZ3BVhiQi1CbhQUUQMWlUfDvbdQOIAwbOdL8pe7sNXp72VF9W0TfVZrBTwu1U5sHHxLHkBnxM6qnxmc74scDsS_2M0iYFxsH_4_q9jIBQBRHCO-B_y8mlyUkJvDxEOrpGJBDn3IXrql1Kq_MTdZfAq750Cbm8NHlYV_thsb3pr49O59FlR9estBM2d1rev9z9kLwWYZQgzJfpgEKGRvqxFGSTmHSFV5xx1Gh6AmSCJ8Nc0TDa5ebbviRQI-9LJ85L6Ruggu07m_EUZVBvUeLeft3SILHlh7Q6o_A2RoLARh5ti24vWHEyqT0-rSHUdng0iNAbfRqvFoa5Ab9dxikQQin_mL_VD9cxkaaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=LDCLqHK6YbTvv78GLfhl7khkWrX2mzMxIcu-Yf5DT5T22mr0Vc5OVBbbBqw-zf71vKxw5sHYFP39hdAu71sIXQytI3UK-mNMMdqWeo7Ywk2xgYjvf7IT-g1UnyyBb07wavDNnqdqhHCcp_AFxPQXSNfkOLAcqdUu-MXmCz4BeItMgn2rPveLMzmpuE9o4AumpY1zleu6Fnl5U-JwQ7BOd2kdexHHr8BPRvTNTdqn7jRNYNzX8k7411j970CCWgWx3nrfq8qx0_W8i9lI0awnyp26ldUq6qmiWDnkkas14wVvZ_6AGA0hQOigdF2oHn6wdLTvfMZ3BVhiQi1CbhQUUQMWlUfDvbdQOIAwbOdL8pe7sNXp72VF9W0TfVZrBTwu1U5sHHxLHkBnxM6qnxmc74scDsS_2M0iYFxsH_4_q9jIBQBRHCO-B_y8mlyUkJvDxEOrpGJBDn3IXrql1Kq_MTdZfAq750Cbm8NHlYV_thsb3pr49O59FlR9estBM2d1rev9z9kLwWYZQgzJfpgEKGRvqxFGSTmHSFV5xx1Gh6AmSCJ8Nc0TDa5ebbviRQI-9LJ85L6Ruggu07m_EUZVBvUeLeft3SILHlh7Q6o_A2RoLARh5ti24vWHEyqT0-rSHUdng0iNAbfRqvFoa5Ab9dxikQQin_mL_VD9cxkaaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حمله گسترده پهپادی اوکراین به پالایشگاه کاپوتنیا در مسکو، روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/71941" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71940">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=JXYMiOm_hz9pYwvKfZWzrGv6TRstQd9h30iZh1zdr_a8BPV7KiDfCq3SmBNRiuVC3YHjpYY6QiWovXG6NtHgn6aE_f2kwh2ME5BgATT2gb6ExfmrTJuLFhJJXlxcYpG2irCO2ha6eq4-tAljRB1DTWbHN-InC3HC4IgfotTfH8HPA1NCuqaXc62pv7FOfejHJnA8CuehAz7m9srM56jXL0PgQCDqnVfAhHJDdQ7ij1U8g8qMqTo_un4VqwzpSTB41dZjyuhbBKhoqwsz9M28lZjKKQqLCymqwFHM-2rPKlrUK9m8_0dePuYOU-aJBRQ1glBdqOQTUaq4VDW_h0Et2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=JXYMiOm_hz9pYwvKfZWzrGv6TRstQd9h30iZh1zdr_a8BPV7KiDfCq3SmBNRiuVC3YHjpYY6QiWovXG6NtHgn6aE_f2kwh2ME5BgATT2gb6ExfmrTJuLFhJJXlxcYpG2irCO2ha6eq4-tAljRB1DTWbHN-InC3HC4IgfotTfH8HPA1NCuqaXc62pv7FOfejHJnA8CuehAz7m9srM56jXL0PgQCDqnVfAhHJDdQ7ij1U8g8qMqTo_un4VqwzpSTB41dZjyuhbBKhoqwsz9M28lZjKKQqLCymqwFHM-2rPKlrUK9m8_0dePuYOU-aJBRQ1glBdqOQTUaq4VDW_h0Et2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانگین آی‌کیو یمنی‌ها:
یه حوثی پین نارنجک رو کشید واسه اینکه نشون بده خدا باهاشه و نتیجه شد این.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/71940" target="_blank">📅 15:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71939">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">قرارگاه خاتم الانبیا:
هرگونه حمله به ایران، منجر به حملات «مداوم، مؤثر و دردناک» به تمامی پایگاه‌ها و منافع آمریکا در منطقه، «بدون هیچ‌گونه محدودیتی» خواهد شد.
کشورهای منطقه‌ای که با تجاوز آمریکا همراهی کنند، شریک این حمله محسوب شده و نباید انتظار خویشتن‌داری ایران را داشته باشند.
بر اساس اطلاعات دریافتی آمریکا با چراغ سبز متحدان منطقه‌ای خود و بر اساس هماهنگی‌های صورت‌گرفته در یک نشست اروپایی، در حال برنامه‌ریزی اقداماتی جدید علیه ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71939" target="_blank">📅 14:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71938">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=UR34cLh5fPhQzzifOsqwpXF8OVGuFIXaH2Q5fg18a6sfVDdPFYcrZnyLfq0FYQtOhatA6UN2I3K7z0UPexCKmd4svkwdYFIxCKljl5hfovPPQDGr9gbSIMEuj0fwS-GHaYkUyXvZ0dcUu05brnPRQEuJDXQrQhdmnYkyf7vvg9lL6-1fbSTG5v90xce2DqGQlMuPRCdkQPSGVWRE2nkp2EuwvOafrXK6VsGEBIIf3DVfAsfu2aotaih2MYoVyeHzYI3QeRyBEhlbgh73bYC7U4gdmGEDXIq7kuUOPSr0PthA-wVitkNlvmSi_o_aLP-Dn8PzdWI6deYCVvmFBCWZmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=UR34cLh5fPhQzzifOsqwpXF8OVGuFIXaH2Q5fg18a6sfVDdPFYcrZnyLfq0FYQtOhatA6UN2I3K7z0UPexCKmd4svkwdYFIxCKljl5hfovPPQDGr9gbSIMEuj0fwS-GHaYkUyXvZ0dcUu05brnPRQEuJDXQrQhdmnYkyf7vvg9lL6-1fbSTG5v90xce2DqGQlMuPRCdkQPSGVWRE2nkp2EuwvOafrXK6VsGEBIIf3DVfAsfu2aotaih2MYoVyeHzYI3QeRyBEhlbgh73bYC7U4gdmGEDXIq7kuUOPSr0PthA-wVitkNlvmSi_o_aLP-Dn8PzdWI6deYCVvmFBCWZmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجمه امینی، دانشجوی ۲۳ ساله و بازداشت شده در جریان انقلاب ملی در مشهد که او را محکوم به اعدام کرده‌اند، در تماسی تلفنی از زندان وکیل‌آباد مشهد از همه مردم خواست تا صدای او باشند.
درود به مردم عزیز ایران، حکم اعدام من صادر شده، لطفا صدای من باشین، من یه جوونم با کلی آرزو.
تروخدا فقط صدای منو نشنوین، اونو نشر بدین و صدای من باشین، من بی گناهم.
شاید این آخرین صدایی باشه که از من میشنوین چون شاید دیگه نتونم حرف بزنم، ولی تنها امیدم ایران آباد و آزاده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71938" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71937">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=q9EAhju6S9tgzvOZzpGBkpd47n7RkmfqzDFw2VG4TNDibteHpO6EqVveITLsfGpyYsxMBdAn2VzgR5IIBSzjlhWOB_L0WtRjfjJetK-znPbR6p9uiM1haKDmrkqNK6Xq5zXRjEfup2gwA-iPDsCZmEAwyNcgxmkHq0Q__iOYxBNq1DS_jOkbLe8s403ix5vURaxWEROVpi6MHdPgYY2KlppmUND0bPRpWslCDQhYVcEBTyHxdt1JtBikJdG7XIyaYpP-ProMRlUEsLt0W516ABtjiZbbI5LXH7KJtM-Ir8K21Tu6h-EIw05Wkj3fmbRfNucuotgR8FxKBw454OgF2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=q9EAhju6S9tgzvOZzpGBkpd47n7RkmfqzDFw2VG4TNDibteHpO6EqVveITLsfGpyYsxMBdAn2VzgR5IIBSzjlhWOB_L0WtRjfjJetK-znPbR6p9uiM1haKDmrkqNK6Xq5zXRjEfup2gwA-iPDsCZmEAwyNcgxmkHq0Q__iOYxBNq1DS_jOkbLe8s403ix5vURaxWEROVpi6MHdPgYY2KlppmUND0bPRpWslCDQhYVcEBTyHxdt1JtBikJdG7XIyaYpP-ProMRlUEsLt0W516ABtjiZbbI5LXH7KJtM-Ir8K21Tu6h-EIw05Wkj3fmbRfNucuotgR8FxKBw454OgF2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اسرائیلی‌ها تونل‌های خالی در لبنان را برای اهداف تبلیغاتی و نمایش انتخاباتی منفجر کردند. آن‌ها عکس و فیلم گرفتند و گفتند: «ببینید نتانیاهو چقدر قدرتمند است.»
همه این‌ها تبلیغات است و همگی به انتخابات مربوط می‌شود.
اما کار ما مبتنی بر اصول است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71937" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71936">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=HlZJhOgV2p3_azktj0Kg4RrMOSqPLaKOox8QrMzAPOq6BwZfkx3l1jFHAbGG2OHP7SIfBUJl4kHU2QEp75JFkbcG6nrTPITTSYW9l1KEoVXx_Qs_LUkurnYPhbMO352tKz4KQKGeJYWbz2Ms9T2Xoe2d8sZb6uj_daHs601lwE4LvTl4Su-TxKBZD_jQdVAJuwDVI_s6vK9aCi535JqWiDqnECuTithoQ6zd7KDYmNs26Mtr7G81Duocv8Yx6DQT26EnXoPCwTPJY2KDl1CUUCeOrN_aCJkKi7J_mR-QL5sv1OdmdQfkVcS_L17IUMRUhrHXvYwB6vvhabARQOj6Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=HlZJhOgV2p3_azktj0Kg4RrMOSqPLaKOox8QrMzAPOq6BwZfkx3l1jFHAbGG2OHP7SIfBUJl4kHU2QEp75JFkbcG6nrTPITTSYW9l1KEoVXx_Qs_LUkurnYPhbMO352tKz4KQKGeJYWbz2Ms9T2Xoe2d8sZb6uj_daHs601lwE4LvTl4Su-TxKBZD_jQdVAJuwDVI_s6vK9aCi535JqWiDqnECuTithoQ6zd7KDYmNs26Mtr7G81Duocv8Yx6DQT26EnXoPCwTPJY2KDl1CUUCeOrN_aCJkKi7J_mR-QL5sv1OdmdQfkVcS_L17IUMRUhrHXvYwB6vvhabARQOj6Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی:
پرسش من از مقامات عرب این است: اگر ایران مقاومت نمی‌کرد و ناچار به تسلیم می‌شد، آیا اسرائیل امروز به عربستان سعودی حمله نمی‌کرد؟ آیا اسرائیل تا دمشق پیشروی نمی‌کرد؟ آیا اسرائیل به عراق حمله نمی‌کرد؟
ما در اینجا شهید دادیم و از کشورهای عربی دفاع کردیم. اگر بینی آمریکا و اسرائیل را در اینجا، در ایران، به خاک نمی‌مالیدیم و اگر آن‌ها در ایران احساس پیروزی می‌کردند، دیگر کسی در منطقه باقی نمی‌ماند که بتواند در برابرشان بایستد.
اسرائیل به تمام کشورهای عربی حمله می‌کرد و آمریکا نیز از آن حمایت می‌نمود. ما مقاومت کردیم — بله، ما از کشور خودمان دفاع کردیم — اما دفاع ما به نفع کشورهای عربی نیز تمام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71936" target="_blank">📅 12:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71935">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=pEhlVpXSbVTg1JkVsyY3CVPLdwsuBiCLgFBt_aJIYyof397eaAkLdwZpSo30MWC6zBek83luRREwINUSAMfipOxbQe23CVRZYk2m8JNWZk70f-OhtdwbBQvTVfyvRnLnv0yUZDd3Et-sLmVg7DqzbU3qeU7vDmm-Oafljb44SdXJR1TVVlMCXfPQ70ENH0450KvbbgOhdORaI4II0MvhrVzxfCCyMEmCbs-D5qfGfz9Y_MU-xCLhDSWC0j69gnY6PxHqaHX9oMd0ZeyaXX-KoV_ICjTyEcQKCSSdiVCBoXZvaDgRGtzHpdo0n_VAA-_9hZkFBMmC37_cU6qC1ho7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=pEhlVpXSbVTg1JkVsyY3CVPLdwsuBiCLgFBt_aJIYyof397eaAkLdwZpSo30MWC6zBek83luRREwINUSAMfipOxbQe23CVRZYk2m8JNWZk70f-OhtdwbBQvTVfyvRnLnv0yUZDd3Et-sLmVg7DqzbU3qeU7vDmm-Oafljb44SdXJR1TVVlMCXfPQ70ENH0450KvbbgOhdORaI4II0MvhrVzxfCCyMEmCbs-D5qfGfz9Y_MU-xCLhDSWC0j69gnY6PxHqaHX9oMd0ZeyaXX-KoV_ICjTyEcQKCSSdiVCBoXZvaDgRGtzHpdo0n_VAA-_9hZkFBMmC37_cU6qC1ho7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقعیت، در مسیر فروپاشی قرار دارد. آمریکا طی ۱۰ سال آینده، دیگر آن کشوری نخواهد بود که امروز هست.
اما ما و کشورهای عربی باقی خواهیم ماند. ما خودمان باید وضعیت منطقه را سامان دهیم. ما باید امنیت خلیج فارس را برقرار کنیم، پیمانی برای همکاری اقتصادی شکل دهیم و در منطقه با یکدیگر دوست باشیم.
ما یک خانواده هستیم؛ خانواده خلیج فارس. ما هشت کشوریم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری داشته باشیم، در سرمایه‌گذاری‌های هم مشارکت کنیم و حتی به سمت ایجاد واحد پولی مشترک و بازار مشترک واحد حرکت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71935" target="_blank">📅 12:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71934">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpfzL9uNCLslYMrKQUVoTcQLFlqfpMPCAYjzoDEluYpkKjBvm-dHqvjtBg4jJxF1oE1HebEuvFN57cc8oac4ebvsi90iN5-Zjjz4bOHcAzsDxJo9-EwbjLRVc7hP-ZBWD8ubUUqA6AUN_xUejoVSfbz3VGqOXIJ5Nn5Q-F506LL8GCpFM65cYz5dmT6EyE2EYL8-BrxvroSgp6sQDJZNUF-RtSIAcQtVHOBh5uEadRGMk6ZvlQlKvCHsVPd5glG_vvAlMY5v-62KwDPsuUTK-sW9eJMRw3bpy5qFY9o0d46e1iDPHsYBkn2os3zp3hEbHBh7POV_DO4m1aig-yEHR82po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=ogBwV-JeMLJBrXXG_zwRwM05q4NElTc8sOYWmhfI2VFnKh2UTEgAh4KMnbxHyrjcFon7SsU9ohYjY5mOCLLR9fAbXvUt-M4Z1ObJlhgX6pVC8iilCtwRancluzuCHNgPoW2vlgempKeMuAZzCUA3wxAiNLPqr52qjHZMJa6nqefYvCDjLSCokoMllhIGKk8SEjLQgM6dOV9kV1EF-o4LVcrtf8T4QX55vMPaMLjdo11q_1FN6yHBscyF6hgRfdXjqVkiup8NFyIaO36uBrhiYbRedWjpN_XnxTMWs8zCBhisQ4iYlmlwQD5sD6ReflB80DwSGt5D27ycCwf5mqwpfzL9uNCLslYMrKQUVoTcQLFlqfpMPCAYjzoDEluYpkKjBvm-dHqvjtBg4jJxF1oE1HebEuvFN57cc8oac4ebvsi90iN5-Zjjz4bOHcAzsDxJo9-EwbjLRVc7hP-ZBWD8ubUUqA6AUN_xUejoVSfbz3VGqOXIJ5Nn5Q-F506LL8GCpFM65cYz5dmT6EyE2EYL8-BrxvroSgp6sQDJZNUF-RtSIAcQtVHOBh5uEadRGMk6ZvlQlKvCHsVPd5glG_vvAlMY5v-62KwDPsuUTK-sW9eJMRw3bpy5qFY9o0d46e1iDPHsYBkn2os3zp3hEbHBh7POV_DO4m1aig-yEHR82po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند. چرا وارد نمی‌شوند؟
در جنگ‌ها، این نیروهای زمینی هستند که همیشه حرف آخر را می‌زنند.
چرا لشکر‌های هوابرد نمی‌آیند؟ چرا نیروهای زمینی آمریکا وارد ایران نمی‌شوند؟ چرا فقط از آسمان بمباران می‌کنند و سپس می‌روند؟
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71934" target="_blank">📅 12:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71933">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=hkNHPXOlk3LPQQ59kG_mDXqmPcCNDV8CupP7VY8iYotVvilmUvbTSwCWd6e0kR-cFgMV-8VXAjCIToSJlHbzV6mgKOrcVdyTwTDbsLI44Vf6S97wuNz5pxaLeLOQ8rs1XWGelTUI8UE8RAVo3TnnbRqCXrZ4oRvL0_SuV_RrDlRXRaiUBUngxifBf7MVl2nyxVTNYpevgbQlFnzMYCs8QLHeVH6AdphNfIOV7Xo_r3aueRJcixfpWTFijTFqNq0X_hUW1FRsT5v5qvykLX6i3BJzHHkKFi4oOO6iFI4ybHmtt09O_6_KhiKTZm3Ez_y0DmOp-QglzYMBOFyDMyZ6BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=hkNHPXOlk3LPQQ59kG_mDXqmPcCNDV8CupP7VY8iYotVvilmUvbTSwCWd6e0kR-cFgMV-8VXAjCIToSJlHbzV6mgKOrcVdyTwTDbsLI44Vf6S97wuNz5pxaLeLOQ8rs1XWGelTUI8UE8RAVo3TnnbRqCXrZ4oRvL0_SuV_RrDlRXRaiUBUngxifBf7MVl2nyxVTNYpevgbQlFnzMYCs8QLHeVH6AdphNfIOV7Xo_r3aueRJcixfpWTFijTFqNq0X_hUW1FRsT5v5qvykLX6i3BJzHHkKFi4oOO6iFI4ybHmtt09O_6_KhiKTZm3Ez_y0DmOp-QglzYMBOFyDMyZ6BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر کجای این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم.
ما سرعت موشک‌های هایپرسونیک (مافوق صوت) خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
بنابراین، ما کاملاً آماده‌ایم. اگر آمریکا جنگی را آغاز کند، با نیرویی بیشتر و ضرباتی پرتعدادتر و دردناک‌تر با آن مقابله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71933" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71932">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71932" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71932" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71931">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pizIQmObhU7nYxqWlufZnyBZoA1TISjCXsMbbMEo-sUOYzJMiFB_K5zy1ydaIEcbHmu55WBNTWBbxOQmOxz1CkPhIYY1QAiDyYvydYEGAQKKcZ6XnXjLxi74Gl6F1iR3SJ0l5jEAq_hOJQSbcsElJ0MVk4Y-ePRiwSY-N7NRfBARqjbrMIDx_bQSkFWul8P8q4NoJxMpnbUbYY093_q5lUF9h7TbBgXteROVMbgQ0td0Wkvu9u8mjvuL55_U1JM3aUAx9f9dNsJLY5mC-gMDAEuuMr9TBIMl7dBMhlN68iN9t-qxTgHs_5CnWlqEjnRA7joBUt7IkK9Sh8BAoVWcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
رویارویی غول‌های مادرید!
🦖
نبرد هیجان انگیز رئال مادرید
🆚
اتلتیکو مادرید را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ رویارویی اخیر دو تیم:
رئال مادرید: ۳ برد، ۲ شکست و ۹ گل زده
اتلتیکو مادرید: ۲ برد، ۳ شکست و ۱۰ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71931" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71930">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=Cujnbmne1Qs_bq-J3uv-gkBM4QGnLNiYygnaCH5_AJNhE1MGfjDbypatFLqEF4kPN5bHWOJvzlNbYhXtv0k3fQWESbWi-wSU3tNWnW3DXUjiCz0VHQUh-juUvK1OP-33PkXte37f9Nv9KImnadoYHXfj1kc_FqrmjFbfgbuJ2ALEK1kYMtcOWmErRrJKxzhIvE3LFoGY841HfZLIRh_PvDNaX4w2iYGu_3tm4mUnZHMDIHqczVQ0_XH86FhDcWUsOz9pqeCLOvMk4h8w-IETNLPxUuotsQXOBh2l3R_gtiNgGPCOBKRWAtZg9aB1DDDZMeKvYXkTiOGQtmv8II5W3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=Cujnbmne1Qs_bq-J3uv-gkBM4QGnLNiYygnaCH5_AJNhE1MGfjDbypatFLqEF4kPN5bHWOJvzlNbYhXtv0k3fQWESbWi-wSU3tNWnW3DXUjiCz0VHQUh-juUvK1OP-33PkXte37f9Nv9KImnadoYHXfj1kc_FqrmjFbfgbuJ2ALEK1kYMtcOWmErRrJKxzhIvE3LFoGY841HfZLIRh_PvDNaX4w2iYGu_3tm4mUnZHMDIHqczVQ0_XH86FhDcWUsOz9pqeCLOvMk4h8w-IETNLPxUuotsQXOBh2l3R_gtiNgGPCOBKRWAtZg9aB1DDDZMeKvYXkTiOGQtmv8II5W3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیلی فلیپس پورن استار آمریکایی، موقع انجام کار‌ نیک راهی بیمارستان شد.
امروز در حین تلاش برای شکستن رکورد بیشترین تعداد سکس تو ۲۴ ساعت، دقایقی بعد از آغاز عملیات یکی از مردایی که باهاش رابطه داشت پاشید تو صورتش و بیناییش بشدت به مشکل خورد و راهی بیمارستان شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71930" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71929">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=BgCPM-1O4cn46pN8V_Ap8QlQut-MgpJQM_qWSEYyRo73A3kiJNCu1QBvpj1kyy6w6lv-wPhYXvgI-mA43Nj4VGG5OmBpNb7WjL33D4csT2HCLozMQZzhbykgaur4_klxFGLmWGneRkXVuO5XS7f1QgU0DFIXjfDBJ7H4PJHL6OMI5IvElMU_IvfZciKXWfIuk0bND0ow3fpYW7TgrjYbQEGV7vXj66JR7dZhgpJPHxId8rG9-_17IUNUxnpQ-X3O4t3D15XJEomH2LRBDU9k8VXoRlfiv7silti9ll9Hh8LFae8v9c3JGuf3Tt8EH3pbogCrVmuaC2tTwMVzVq2r4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=BgCPM-1O4cn46pN8V_Ap8QlQut-MgpJQM_qWSEYyRo73A3kiJNCu1QBvpj1kyy6w6lv-wPhYXvgI-mA43Nj4VGG5OmBpNb7WjL33D4csT2HCLozMQZzhbykgaur4_klxFGLmWGneRkXVuO5XS7f1QgU0DFIXjfDBJ7H4PJHL6OMI5IvElMU_IvfZciKXWfIuk0bND0ow3fpYW7TgrjYbQEGV7vXj66JR7dZhgpJPHxId8rG9-_17IUNUxnpQ-X3O4t3D15XJEomH2LRBDU9k8VXoRlfiv7silti9ll9Hh8LFae8v9c3JGuf3Tt8EH3pbogCrVmuaC2tTwMVzVq2r4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکراین شب گذشته یکی از بزرگترین حملات پهپادی خود را علیه مسکو انجام داد.
روسیه مدعی است که بیش از ۱۶۰۰ پهپاد، از جمله ۴۵۰ پهپادِ عازمِ مسکو، سرنگون شده‌اند.
این حملات به پالایشگاه نفت «کاپوتنیا» (بزرگترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر از ساکنان شد.
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71929" target="_blank">📅 11:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71926">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=X6Z38fa8agehO0QIrzojxQVNSw49Cw2fg4i3wC1jZXm4HyJqzPWOl7FZ4whYYjPxHVhtUvg17eZD3c4IQiXsKflkpsPrezyPyLoTt1xzjM5X0BYGyxR7oyvzKH-Hrv8FHiOvsJGC4cz-khbAhIXQmAHNuIqXdKdqDngSXNBbJlX9u4WOOWtyV__7-miMQDroh8qUkJiTuaRUhrd7r8KrlR2cJQ5t6Nyn9vQuYUrwjlLaa9H7ALw-Hba5fVY-oSoADbSnWXmsUfXm-AQiBKO_p5Eq-irpaqBF30A0bJ_x3alHjv6_heiVmazvPHZSAa-SGeZnUxftAhyoZ0r7tKN1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=X6Z38fa8agehO0QIrzojxQVNSw49Cw2fg4i3wC1jZXm4HyJqzPWOl7FZ4whYYjPxHVhtUvg17eZD3c4IQiXsKflkpsPrezyPyLoTt1xzjM5X0BYGyxR7oyvzKH-Hrv8FHiOvsJGC4cz-khbAhIXQmAHNuIqXdKdqDngSXNBbJlX9u4WOOWtyV__7-miMQDroh8qUkJiTuaRUhrd7r8KrlR2cJQ5t6Nyn9vQuYUrwjlLaa9H7ALw-Hba5fVY-oSoADbSnWXmsUfXm-AQiBKO_p5Eq-irpaqBF30A0bJ_x3alHjv6_heiVmazvPHZSAa-SGeZnUxftAhyoZ0r7tKN1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71926" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71925">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شاهزاده رضا پهلوی:
با توجه به شرایط جدید، تاکتیک‌ها و روش‌های اجرایی مخالفان جمهوری اسلامی تغییر کرده، اما هدف همچنان سرنگونی جمهوری اسلامی و دستیابی به ایرانی آزاد و آباد است.
«ما امروز با تجربه‌تر و مصمم‌تر از هر زمان دیگری هستیم. هدف ما مشخص است، سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد.»
ایشان گفتند: «چهار اصل کلیدی ما مشخص است:
حفظ تمامیت ارضی ایران
جدایی دین از حکومت
آزادی‌های فردی و برابری همه شهروندان در قانون
حق ملت در مشخص کردن شکل آینده حاکمیت ایران از طریق صندوق رای آزاد و منصفانه
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71925" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71924">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=j5I6Jk6ageTpaN180cHWMNoNRtGbhrKutgvjmCTcimrWtaMAAy4JPx5I2YCiEXQQt_bn1Xkc6ps8KIcwV94tdQRlPu-8Ygx1zcY6KHQmZhBlAIaN1FKYijcKI7fgQp7rFfx-35JeswSP2OSm2_KW4c8OyZCIOzSioxM8vu08j8AYkFT9b_xhGeBZTgTPESihpJTq-CE6l1KJesYxL6rIi-J6OVEWLdjppGgBUEEwl0vSIMnaiqMKyd7ZMdzIB1GtbS-EZK2InunHzgtWeTQT_nJHxiGQrIobtcbl33AeN3GDEb0-WOxRU_JrpD0DiRcgGfjEWE_-27sQqbc8LXLEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=j5I6Jk6ageTpaN180cHWMNoNRtGbhrKutgvjmCTcimrWtaMAAy4JPx5I2YCiEXQQt_bn1Xkc6ps8KIcwV94tdQRlPu-8Ygx1zcY6KHQmZhBlAIaN1FKYijcKI7fgQp7rFfx-35JeswSP2OSm2_KW4c8OyZCIOzSioxM8vu08j8AYkFT9b_xhGeBZTgTPESihpJTq-CE6l1KJesYxL6rIi-J6OVEWLdjppGgBUEEwl0vSIMnaiqMKyd7ZMdzIB1GtbS-EZK2InunHzgtWeTQT_nJHxiGQrIobtcbl33AeN3GDEb0-WOxRU_JrpD0DiRcgGfjEWE_-27sQqbc8LXLEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:مجتبی مفقود است و اگر هم زنده باشد در تاریکی زیرزمین جرأت آن را ندارد که حتی صدایی از خود منتشر کند :))
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71924" target="_blank">📅 09:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71923">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d403914707.mp4?token=k1UZwAOPtuRiJ1VrHnZbM6ADR0Ly280YcJMPIrDH0QLGnf4ADVXTLDl1ZpgQ9vsat1JiC7t8sMH8PnOwLpZyFbzJ8B2BdPHCWazTW1b6y2g92l3rOQ33tjLWgf0oT4N2MijPmX5NWQwxMktc4GYSul9t3NVf_VSugdNXTF_2MlGEYzBTyomLyoNnPubeYGxXc8c6sPuL8Rdu3ZrJIQMkXzate2C2yxJZa4ul4upTHxzOV6UsYS7a1v0IYeeDV7Xz_6489Wyfye1WLrfjnyj4sTP7R7bBSEfKARm3ZTDFy-LpZM0nJAck9WEyi7c6vCnYr36OIZu49OoXiXGhY2hkrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d403914707.mp4?token=k1UZwAOPtuRiJ1VrHnZbM6ADR0Ly280YcJMPIrDH0QLGnf4ADVXTLDl1ZpgQ9vsat1JiC7t8sMH8PnOwLpZyFbzJ8B2BdPHCWazTW1b6y2g92l3rOQ33tjLWgf0oT4N2MijPmX5NWQwxMktc4GYSul9t3NVf_VSugdNXTF_2MlGEYzBTyomLyoNnPubeYGxXc8c6sPuL8Rdu3ZrJIQMkXzate2C2yxJZa4ul4upTHxzOV6UsYS7a1v0IYeeDV7Xz_6489Wyfye1WLrfjnyj4sTP7R7bBSEfKARm3ZTDFy-LpZM0nJAck9WEyi7c6vCnYr36OIZu49OoXiXGhY2hkrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده‌ رضا پهلوی:
«امروز این (جاویدشاه) یک شعار است .
یک شعار پشتیبانی و من از صمیم قلب سپاس گزارم.
کاری بکنیم که اون روزی که صندوق رای در تهران برقرار شد تبدیل  به رای بشه , نه یک شعار .»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71923" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71922">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71922" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71921">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btyb_i51yzMI91wGGzc7CbxpCX8Zk5it3OmY2HKC4NlKx6SAgSWEKecJV97mkZiFIj7SmvW8a8dCPUJvLDKPZtbbcw-McPCoDMXnYtOsYY3Ea7MFBtKT8Jh4sCc-0E58x0K-7fEqrNTOiRtfNWLgV1kAm2XK6TuQeWw1oANbFbFpOpx1TLtz0t_An0NkbAL4Uu4dWSyHrpXscdCotwsVwJeLoHONwFZVrWGt3b_YHtJRYcUZSZZY4j0brBri3gWJhSpM9EzHlKpdU_H1xhV2MimqimBCXTFgBupHJpfNfZgCFlx9lClmA1JPSOhk0qXgaQ8Rjm4neabNUTlhqhG22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71921" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71920">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkgZ9RWaonZx2dGy_ks25dQ-S41q2j3q2vjuvB7P3YbtanupyvPRKUD8PYch7SOVtrkoASn5mEMa3a6pyycQqOxbpoRbmQf7Gwr47cmFXKC3zkEmynfJTwySlSYLE9yHdZuB9-5BcYRWmOFrduVgwLuC9FT4qfRUShTaRwaPag5SC2rAhpOevdvBSFOmc7AxSdAkux55hc9PgYxu9V7O1oIj7zP4QqNPtxa3YYvBVOUHFu4HGyQAr-WnIyXPs92kQsaldzwxb8_eM6qXH6yhWWD6h0Fok1D9Q6R1S0WgQLWPW60O06bIhlxyO8bdAA84BVJrnaANbUUH-llwHxcUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71920" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71919">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هشدار جدید آمریکا برای شهروندانش در خاورمیانه:
بر اساس آخرین اطلاعات منتشرشده، عربستان سعودی، بحرین، کویت و قطر در سطح «۳؛ تجدیدنظر در سفر» قرار دارند.
آمریکا در مورد عربستان نسبت به خطر حملات پهپادی و موشکی، درگیری مسلحانه و تهدیدهای تروریستی هشدار داده است.
در بحرین نیز آمریکا به تهدید حملات پهپادی و موشکی و اختلال در پروازهای تجاری اشاره کرده و سفر به این کشور را در سطح «تجدیدنظر در سفر» قرار داده است.
هشدار آمریکا درباره کویت نیز همچنان در سطح ۳ قرار دارد و از تهدید درگیری مسلحانه و حملات پهپادی و موشکی به‌عنوان عوامل اصلی این هشدار نام برده شده است.
در قطر نیز وزارت خارجه آمریکا نسبت به تهدید ناشی از درگیری مسلحانه، اختلال در پروازها و خطرات مرتبط با وضعیت امنیتی منطقه هشدار داده و از شهروندان خود خواسته برای احتمال تشدید شرایط آماده باشند.
در همین حال، لبنان در سطح بالاتری از هشدار قرار دارد و وزارت خارجه آمریکا از شهروندانش خواسته به لبنان سفر نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71919" target="_blank">📅 01:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71915">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vrIILlJJsk962DadXeg_b47rb9f9bbWftQNV9ufhpTFagK3m_S80_OvOz1bXHg3X1QFL7UakzUj10R8-2_ggz5kQGegxqeEeBOvNJSZTtgB8WKmt3EuM1H772BVULBYLKWXS6M_fhwfl2s61A63wnhNi2J5pA2fz7kxUAUjDc5JrLjwULaeVGbXqJFslpziPN2FCQNDZ4obre4Z_Od9IaInx2IJSJjhZzltZPSTAhyx81kGLHXiWFa6XV-RPMmuZnQivvoj1tJd80H0Hnpu8fApRhKnu9s5tXWyiJX45f_-Cq6Wd7HCsdnmKTSiepOg-qviDKSHY8fIRmztwScxm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Lqb8z38SkhdXEk6Oy2v7vINpJb4GUmO5t2hSmLIlXaXSW4vQiuhpczJhTVXkyKrH_N8IB-5voSr9TzlQhw5ziMmX-lYxTWqkR2lF6EKKVrmo7iOf-J7PLZbEhBIq_QpHslrtrYccgNxAkyBX5oHY_mS44yd9VrDvbcUwv8Dnu4AE9iqkXdA4rRP8M2uKcFwV3ozDOYswKRjC9AKgw6GyYvU7AIwyszI-XFQowCXgNW1Bb0zBwY1igXUvYCYJcVLwwMruJXoXVJajDXel-3r6OA2Pzhf9V4ZAEfretMaSex1iR5BnxQtoo0syNyj9gHGUXXBPTs4hfR7iteyFMKn_rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Lqb8z38SkhdXEk6Oy2v7vINpJb4GUmO5t2hSmLIlXaXSW4vQiuhpczJhTVXkyKrH_N8IB-5voSr9TzlQhw5ziMmX-lYxTWqkR2lF6EKKVrmo7iOf-J7PLZbEhBIq_QpHslrtrYccgNxAkyBX5oHY_mS44yd9VrDvbcUwv8Dnu4AE9iqkXdA4rRP8M2uKcFwV3ozDOYswKRjC9AKgw6GyYvU7AIwyszI-XFQowCXgNW1Bb0zBwY1igXUvYCYJcVLwwMruJXoXVJajDXel-3r6OA2Pzhf9V4ZAEfretMaSex1iR5BnxQtoo0syNyj9gHGUXXBPTs4hfR7iteyFMKn_rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم بزرگداشت کوروش بزرگ در تورنتو کانادا و استقبال فوق‌العاده مردم از ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71915" target="_blank">📅 01:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71914">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7zAwpgw9kSYdA2ya8azjYfaPZTF_583E7dLI5dxnPYq1AR82Zi1oI7OWQDvYOcpq6A-FjFRNf5HYCE5jjHfFyi5C_vdHWscWmNeV0_oxg6T6pqiS7FbRH-IIVt_6zpseSdJHPPX3hPvoA5sm73fyr6JjJDSNRhbDWUOIl1oY1z_YekzgkBJsdmi0iMeTTS3i59XnVaQRdgKqlJKIvd1MBAV4jMhm5Wya8HgWTA2EMe-y-GItSig77RXdQCUENHp3N1mrDjLH1TpEwMxvYg6B_kOF-3CHq0loLNr_p8lF0GtzecJ0LKxGd66eXE69ctgqZUpAopkeQGUATqiNL5A0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
ایران هفت شرط را برای آغاز هرگونه مذاکره به دولت آمریکا اعلام کرده است.
پیام تهران روشن و صریح است؛ اگر واشنگتن می‌خواهد از باتلاقی که خود برای خویش ایجاد کرده رهایی یابد و از گرفتارتر شدن در آن پرهیز کند، چاره‌ای جز پذیرش حقوق و شروط ایران ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71914" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71913">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=KKc38D4kaEQwNXws-eAmkNGdE7o6_kPDyh6kgQX097fH9FhBcfLWY3nl5NHo613Tx7jkBicb6_mAu8nRjj4CMRqVYVfNnMXLfmB4SN8mp__U6gAN4odk4vQLQWhMXg7bGxaJqnCjl_tHJukPHNDd6uNW3QSTYLbQxKm6zL_usCTDApKOIrzeypdttjxVSpVYrYqge8Yvqnmf9ZaUtIZNK9os1zueWAFAKkwGpdN1IMtkdx4SvczAdGxqbzQDfrCJTcxOAQeLZbqNPSCt9gKF0_p-pSCu6M4kdZllZqE9Hu8it4iErDirNVAhUAB0oDUx10_MbUKeAPka_ZXdJKNnl6YagLVweWkG_oK7oc6dgfsEu6ZB2qGy5FUudDa7teqzaQbitXhhhcsYnc-gJBdKsJ0xFbWbFN43prxBahkA2xwkBTusvxnO-ZR1g4ss5BHw9GsaISBwfi7HLT8BHTYJJjS3yME1dpR0OU-8wnys-921D8xOG5vZv6zCkAHApgmllue65v1x2munDJh5RureyO-mZxDPKTgK_k_J9nqU8u-ibNYfhJ1gvDZD7iG4l7Qp2sx81Xh2ZCXy1q5gZ3UHZdl07kJiIBJmQrrKwS90TVji4vKJZEIFN5Egy787pCVgCtUTJtA7gPe9yVGdmXaZVVqqnnrTuOvYaOVISp9BxNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=KKc38D4kaEQwNXws-eAmkNGdE7o6_kPDyh6kgQX097fH9FhBcfLWY3nl5NHo613Tx7jkBicb6_mAu8nRjj4CMRqVYVfNnMXLfmB4SN8mp__U6gAN4odk4vQLQWhMXg7bGxaJqnCjl_tHJukPHNDd6uNW3QSTYLbQxKm6zL_usCTDApKOIrzeypdttjxVSpVYrYqge8Yvqnmf9ZaUtIZNK9os1zueWAFAKkwGpdN1IMtkdx4SvczAdGxqbzQDfrCJTcxOAQeLZbqNPSCt9gKF0_p-pSCu6M4kdZllZqE9Hu8it4iErDirNVAhUAB0oDUx10_MbUKeAPka_ZXdJKNnl6YagLVweWkG_oK7oc6dgfsEu6ZB2qGy5FUudDa7teqzaQbitXhhhcsYnc-gJBdKsJ0xFbWbFN43prxBahkA2xwkBTusvxnO-ZR1g4ss5BHw9GsaISBwfi7HLT8BHTYJJjS3yME1dpR0OU-8wnys-921D8xOG5vZv6zCkAHApgmllue65v1x2munDJh5RureyO-mZxDPKTgK_k_J9nqU8u-ibNYfhJ1gvDZD7iG4l7Qp2sx81Xh2ZCXy1q5gZ3UHZdl07kJiIBJmQrrKwS90TVji4vKJZEIFN5Egy787pCVgCtUTJtA7gPe9yVGdmXaZVVqqnnrTuOvYaOVISp9BxNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن‌استار ایرانی ملقب به «شیر ایرانی» با شروع بسم الله و کشیدن علامت صلیب توبه کرد :
خدایا منو ببخش و از این آتیش جهنم دورم کن بعد این همه گناهی که کردم
بدترین انسان نیستم ولی بهترین انسان هم نیستم به همه میگم خوبی بکنن کارای مثبت بکنن
دنیا خرابه جنگ زیاده سختی زیاده اصلا سختی دنیا زیاد شده و سختی عمر اعصاب آدما رو خراب کرده
خدایا نه فقط من بلکه همه آدمای دنیا رو از آتیش جهنم دور کن
الله اکبر خدایا منو ببخش خدایا دنیا رو جای خوبی بکن خدایا جنگ ها رو تموم بکن
خدایا منو نجات بده نزدیک خودت بکن میخام آدم خوبی بشم خواهرام و برادرام هم میخام بهت نزدیک بشن الحمدلله
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71913" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71912">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkQNzfFvMwqde7wgijebXV8K0YQRPktke61pbKm8UW8E8Rvo5nB3do89vfoOouaJqhxYNeK-PNwHbhDFgjr9WIrcj96TMbZuV79rL2sFxfgLL4ox97FfsrGepOu8YjytkRNrBtSh_NI4l8eN5EnpW_rpCRy0UismxFa3RfBdeT05bvACZydyBfsdOIhg3eGowVhrK8dXXn2ceSFxVGYEbRM48hLHZeExx5iDxRmX0tM3TI-N0rng3Ehk2u9cxuJDbbzV9tj1j_3cN69vuXl32D34h2w9eq_nzaJEvRzuMTpkTCjaSq-rcvft_6BKAZm0bm-AilGWDU6FLGQMtNw1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد دیدن این عکس دستور حسینیه شدن کاخ سفید رو صادر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71912" target="_blank">📅 23:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71911">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz1W1SQw17TTQnJQElN4QFpi0YSrBmjsqBtsAWNZqszXRJLmGkx_2M5nryWuQpCrJSaSUiaGzMYhnmVGiuJb-BCRit05LLVIVcLQM35oirPJOwURli87a_pGXzf22sr7ULdlj2Jn01KzmBafcHKtesdG32Xl4A7Z5pClKVKoIxsoj8Ok9pvDGQaEwTxWNaT3rtokVmkAqjigfBXi7v8aDN5B4W1aY3YEFvAjmGLe2AZz9peI5q7bS9Hdc_5ulfiPnhw6I_-UrSS8Yg8PmdZDx1cT9ujHbYg7kmF-6LOk23LdUgLbuqA08Z8GAnEr0KHF1MLi033u0ywNsGlUxjoBAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه سی‌ان‌ان اعلام کرد که روز شنبه به دلیل ممنوعیت اعمال‌شده از سوی ترامپ، از ورود خبرنگارانش به محوطه کاخ سفید جلوگیری شده است؛ این شبکه اقدام مذکور را «تعرضی غیرقانونی» به حقوق خود ذیل متمم اول قانون اساسی توصیف کرد.
سی‌ان‌ان با تأکید بر اینکه «قاطعانه از تیم خود در کاخ سفید حمایت می‌کند»، اظهار داشت: «ما از انجام وظیفه خود در پاسخگو نگه داشتن دولت و سایر نهادهای عمومی، باز نخواهیم ایستاد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71911" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71910">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=UD09C-8qzeAqowCXKczc5eGJkf3X_QI0j-UvfdkUKvFA1sGqPGhdVJ-pA2deq3NbtZNBHZ2L7Pmer6rlVWUEjFdzB_9TcXOHg7Q6R7o2LGJdz6ykoILcDIwNn2RkCmGiR3Tu5oPvz_ijOjUNq36s1RavCWSN-i-_khz0_pIAP6m_fKzfkYzO_2rEgUX-GeZYPhoV_3ry7HxBjAb94037-rgoMd_fZwcGwVgXTR2RZev_QN8gPNe9qFWM6W4ZSh8c8QCci62bpzU_YNycQgRtWSkqD3G8VyPFpg9LaNQ-cIdLBAkhf6GRtvd5VENt7XLbghnKQZYUCS2sDzznJmRogTF_Treui-IH3PYv9kxLg8TQlj5pwv2J0O_relcymCmgzb3es1pw98Rt6nGbZ8okTFequOKhln4ugaohIULWDqPTioem37tt9JnkQH-Cd0ELK6ddIdWCfU2DZAWki-DcqgCxzBLXBYez66p3HMGoDh0Vbq8v7mjsztNz9J3YtxhoHLm3ZhtvQAyRVcx8ZW7UCjgdQmDExJfX-4hiGfUtGXIWelJKvpfr5BxxoBeUoHooV05SLOl2vCv43ZfUlbvL22qdOH43E9lF24DnSCvtVaND2-l3ALI-SgoVN5oMwj7CLE61XQN13Tp58ap4OTodmjv4Y0g_tP3rlK0yM-WdAis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=UD09C-8qzeAqowCXKczc5eGJkf3X_QI0j-UvfdkUKvFA1sGqPGhdVJ-pA2deq3NbtZNBHZ2L7Pmer6rlVWUEjFdzB_9TcXOHg7Q6R7o2LGJdz6ykoILcDIwNn2RkCmGiR3Tu5oPvz_ijOjUNq36s1RavCWSN-i-_khz0_pIAP6m_fKzfkYzO_2rEgUX-GeZYPhoV_3ry7HxBjAb94037-rgoMd_fZwcGwVgXTR2RZev_QN8gPNe9qFWM6W4ZSh8c8QCci62bpzU_YNycQgRtWSkqD3G8VyPFpg9LaNQ-cIdLBAkhf6GRtvd5VENt7XLbghnKQZYUCS2sDzznJmRogTF_Treui-IH3PYv9kxLg8TQlj5pwv2J0O_relcymCmgzb3es1pw98Rt6nGbZ8okTFequOKhln4ugaohIULWDqPTioem37tt9JnkQH-Cd0ELK6ddIdWCfU2DZAWki-DcqgCxzBLXBYez66p3HMGoDh0Vbq8v7mjsztNz9J3YtxhoHLm3ZhtvQAyRVcx8ZW7UCjgdQmDExJfX-4hiGfUtGXIWelJKvpfr5BxxoBeUoHooV05SLOl2vCv43ZfUlbvL22qdOH43E9lF24DnSCvtVaND2-l3ALI-SgoVN5oMwj7CLE61XQN13Tp58ap4OTodmjv4Y0g_tP3rlK0yM-WdAis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حامیان حکومت تو تجمعات شبانه شهر بابلِ استان مازندران داشتن دورهم «کلاغ پر» بازی میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71910" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71909">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGXN3NsXsR7hhN2LRshB8g1eHpIC2GJRJ8F17pmU3Alu0KDWPU-eTOWIQuUIFyi8nVJaK5ElV8TH9y1ytiR7BdXdX-FeAF-p6OJvRRUbXEe_gJatyib79h9MF6ux4Qpsx0dghdCK0chDn2pGPSSb2F0wwZQz7glUB9BeZtPYKHfbN6MbpkWATmRk8DSkhqX8qlMwiHVqqHvx7sULgzSzIAztYlYQel6f1vxhiPlYyH1CjQ31kD-W3oiQAYaVisRkX137pO_NeEWp4ikSMIHNoeVsE-IwDWKT82LaOzkHU-t69xx4u-m77yh8OP0GLFzflpBZXQQccQd2K8pwrM8Xmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:نام فعلی هوش مصنوعی چرته و از رأی‌دهندگان می‌پرسه که آیا نام «هوش مصنوعی» باید به «هوش برتر»، «هوش فوق‌العاده» یا «هوش متعالی» تغییر کنه یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71909" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71908">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=lqE90YOr6cbo9i2vTmdr5DWKEtVh38nUKI08S5RWb1IfD3ILnRyh84LzlCqkT-0TO403uVWeSLxKmEgoXMF8-gsolgQfxVELyMkO1DP_nDy2L7sVyGfwRcxoBMjuiJwiCaQi-5onh_J4_QNSMl-8GvyGTEl1yF0iGOjycErdSmstlt-Ke5X--SfOH6xxNJNlTifrZWXOcr9J_b_him0rbCXqlG79LYaEv4xaGd8bQcQKCQcdRkYsl9h-7DASMK6VCvCdxQTRNZOnFhkfqky7gdvnLrnZCatQunpBGqACGCe090yI3oKd5NkOdMoNuoQlw6arFgK8Qg8FlmprcmCdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=lqE90YOr6cbo9i2vTmdr5DWKEtVh38nUKI08S5RWb1IfD3ILnRyh84LzlCqkT-0TO403uVWeSLxKmEgoXMF8-gsolgQfxVELyMkO1DP_nDy2L7sVyGfwRcxoBMjuiJwiCaQi-5onh_J4_QNSMl-8GvyGTEl1yF0iGOjycErdSmstlt-Ke5X--SfOH6xxNJNlTifrZWXOcr9J_b_him0rbCXqlG79LYaEv4xaGd8bQcQKCQcdRkYsl9h-7DASMK6VCvCdxQTRNZOnFhkfqky7gdvnLrnZCatQunpBGqACGCe090yI3oKd5NkOdMoNuoQlw6arFgK8Qg8FlmprcmCdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست اکتان بنزین در عربستان …
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71908" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71907">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzONjUlKW5dUrqwBhZQ8USEH4E6NgWzSS_r7MnuRuiZMVbk9C8L6ffQMMMPXRjUifj7jHIXFTK6K0BGI-Dm8dWMBzc0ZIsAmvFApLkKdKvQaMSx1IUqcrGaMP31LmJ4Orb4LQtvivWjQoVKQY8rZAVCVpVZ-tK0NBM3xsRswmI0OUjAuTNFoFvceAKSrFw17FeXS48mZ10FJfEIgEoWp98VVUBUtGh_LMIZQUIIfD7kvMad8G37QdQBxlEbwXiRnQL3xQ_Hmu_9GXNM_Ub_5RBp5phhJnSRV33GW-yFlG2STeIRYLUHsPCVnNabSrkHvNEY-2ANT0LshCwNJo2VhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواشناسی: طبق پیش‌بینی‌های فصلی، بارش پاییز امسال در مجموع فراتر از نرمال خواهد بود؛ تمرکز بیشتر بارش‌ها نیز در غرب، جنوب‌غرب، دامنه‌های زاگرس و بخش‌هایی از البرز پیش‌بینی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71907" target="_blank">📅 19:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71906">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، در گفتگو با شبکه الجزیره اظهار داشت که دونالد ترامپ، رئیس‌جمهور آمریکا، در ارزیابی خود نسبت به ایران «دچار اشتباه محاسباتی» شده است؛ وی همچنین بنیامین نتانیاهو، نخست‌وزیر اسرائیل، را به تحریک برای آغاز جنگ متهم کرد.
رضایی با بیان اینکه تهران «برای یک جنگ قاطع» آمادگی دارد، هشدار داد که هرگونه حمله بیشتر، با پاسخ‌های شدیدتر علیه پایگاه‌ها و منافع آمریکا در سراسر منطقه مواجه خواهد شد.
وی خاطرنشان کرد که ایران نقاط ضعف ارتش آمریکا را می‌شناسد و برای مقابله با حملات هوایی این کشور آمادگی بهتری دارد؛ ضمن آنکه اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کرده است.
او همچنین افزود که ایران به این نتیجه رسیده است که پس از خروج آمریکا از یک تفاهم‌نامه، باید راهبرد خود را در قبال واشنگتن تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71906" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71905">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رضایی، دبیر شورای امنیت ملی:
رایزنی‌ها با میانجی‌های قطری و پاکستانی ادامه دارد و ما شرایط خود را برای مذاکره به آن‌ها اعلام کرده‌ایم.
ما با میانجی قطری در تماس هستیم؛ او شرایط ما را برای توقف جنگ به واشنگتن منتقل کرده است و ما منتظر پاسخ ترامپ به این شرایط هستیم.
شرایط ما عبارتند از: پایان دادن به جنگ در تمام جبهه‌ها، آزادسازی منابع مالی بلوکه‌شده و پایان دادن به محاصره دریایی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71905" target="_blank">📅 19:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71904">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmANSvseZgXSPmWiRw_jxIQgRIC8Ik3SXBdIta2yfqqqhqi-VcvhMgjZfRhvx8eW4qzfbkEgjG2o83rdLvutLRtTJm9Sh6iUWY67M4VwYsyEmYd8ER9topIw5lGPK_2vb_dEB5j7_Pbw1IULyfKoE8y-9HZG0GAEry3owslAGkxsswqSyTUA8ZwiWxb1_aGBdzYzGqJ21ucGwwlOzrjq2EhUD6dI9VhcuP2eOMMi6jkbf0421eXwmQJ2Z0Q-teWmgANiksOchDqR2SRBDDGdkf8vHM4fY0abk-G28rsUiR977kiqwiQLYAZC8OI9LRJlOj4-Cd8sT-2Lb82Wvg2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: اقدامات آمریکا و اسرائیل ممکن است ایران را به سمت خروج از «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) سوق دهد.
رضایی گفت که ایران هنوز تصمیمی برای خروج از این پیمان نگرفته و افزود که این تصمیم به اقدامات آتی واشنگتن بستگی خواهد داشت.
وی تأکید کرد که ایران همچنان به فتوای رهبر فقید انقلاب اسلامی مبنی بر ممنوعیت سلاح‌های هسته‌ای پایبند است و دکترین هسته‌ای خود را تغییر نداده، اما «نمی‌دانیم در آینده چه پیش خواهد آمد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71904" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71903">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=JrjY-RCfenySOpYKmaNcEkMVUXTqsbD4HE4J8c1FXy_qiXdUYCMO4f_BUreDqEAr0q5yF0YPH2Xve8B7ewsUCvCp_x7yITl5VMGQnYdLdVFcqkK4N8ih4o2lt6zZraZBJ6r8tqhWPComvMnsefyf8BdzCXpLOlyNtfnIrq4i4Hh4tE20CThrT6FUf8ZI5HVYAvT25NcgMzHFext6FZL0cg6VLK8JDlDauNpPf8sFuyEm_NN2ORHxc-3qt-b9KpAKRwFnZ9i1bckqBM5yRxj-8xHRq73FgFZGNvE8wsDoaNVS9EA5iiGETh4fagunllw2DEV3d8cm5Akn5b8SVL25Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=JrjY-RCfenySOpYKmaNcEkMVUXTqsbD4HE4J8c1FXy_qiXdUYCMO4f_BUreDqEAr0q5yF0YPH2Xve8B7ewsUCvCp_x7yITl5VMGQnYdLdVFcqkK4N8ih4o2lt6zZraZBJ6r8tqhWPComvMnsefyf8BdzCXpLOlyNtfnIrq4i4Hh4tE20CThrT6FUf8ZI5HVYAvT25NcgMzHFext6FZL0cg6VLK8JDlDauNpPf8sFuyEm_NN2ORHxc-3qt-b9KpAKRwFnZ9i1bckqBM5yRxj-8xHRq73FgFZGNvE8wsDoaNVS9EA5iiGETh4fagunllw2DEV3d8cm5Akn5b8SVL25Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: کنگره در چه مقطعی وارد عمل شده و به مسئله جنگ با ایران می‌پردازد؟
رئیس مجلس، جانسون: ببینید، دولت این وضعیت را یک جنگِ در جریان نمی‌داند؛ و واقعاً هم چنین نیست. آن‌ها در تلاش برای به سرانجام رساندن یک عملیات هستند — عملیات «خشم حماسی» (Epic Fury) که موفقیتی عظیم بود.
به گمانم در حال حاضر نیازی نیست دموکرات‌های لیبرالِ مارکسیست در کنگره بخواهند به فرمانده کل قوا دیکته کنند که با ارتش چه کار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71903" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71901">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=t1SKIfRf7_HOZ_Mn6vZDRxyjQvLRZqk6vrv3wTXQPevt6M7BqM8R8V5WZU-T3tqyFg8CqT9VY60PA-XJB5DoTidZzJ6OG3iqR49pgZdAhFn1f-Y48I5WFeCHGJlr7torfaDzKPp-EFFKxRgbAvSbWA8W-Qw4vD3SXUaZWZBFlWkLm0leW1ytzrNK8xaoLshEfrZJLNfLayBBFUm_zZs1Br_CJNfmr-H_uNgrFRc7eVtiRqSUvX3y7ugY3HBtUMVVldcImKCQHPsFH7r1QbWE0_8lJllloDuffbgQSLClLBTctCXaSEFDU5pzNkiZ_BCsthe9KzF_g-P3TAIt9KF3Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=t1SKIfRf7_HOZ_Mn6vZDRxyjQvLRZqk6vrv3wTXQPevt6M7BqM8R8V5WZU-T3tqyFg8CqT9VY60PA-XJB5DoTidZzJ6OG3iqR49pgZdAhFn1f-Y48I5WFeCHGJlr7torfaDzKPp-EFFKxRgbAvSbWA8W-Qw4vD3SXUaZWZBFlWkLm0leW1ytzrNK8xaoLshEfrZJLNfLayBBFUm_zZs1Br_CJNfmr-H_uNgrFRc7eVtiRqSUvX3y7ugY3HBtUMVVldcImKCQHPsFH7r1QbWE0_8lJllloDuffbgQSLClLBTctCXaSEFDU5pzNkiZ_BCsthe9KzF_g-P3TAIt9KF3Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی به تخریب خانه‌ها در «میس‌الجبل» و «المنصوری» در جنوب لبنان ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71901" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71900">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=d-f3YqwcVXFBHuuKbBIFIquGzIjOvrWncAd5eEXoQsQ7YLLTFMK0VzAhixF6H_6ORlMKk2Dh6E-XF_XSCZMtrc7A3eNdfewLx9r4qPEd1aCiIT-iGWn2JyL6pyLWrFEoPH2vBXMliYXQkhpuJ7055P2gNnxdAi3z1gj7a_BYHMQjmVi5vSu7Nw-Tp91bwcvKSp19BJ3D2hAuLQMFmuv3FAo8PlYbzR4r6WoK0TGze059PTircU8ItGn2Yw3a-JlOH0n6BAIWbcvZ35ZH58sSMK_AHLr6UHeQJz8VWWuKEFOKTLfCj77dShjWLzBm0O6-s8c9a-WwKQBW9V16-TaibQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=d-f3YqwcVXFBHuuKbBIFIquGzIjOvrWncAd5eEXoQsQ7YLLTFMK0VzAhixF6H_6ORlMKk2Dh6E-XF_XSCZMtrc7A3eNdfewLx9r4qPEd1aCiIT-iGWn2JyL6pyLWrFEoPH2vBXMliYXQkhpuJ7055P2gNnxdAi3z1gj7a_BYHMQjmVi5vSu7Nw-Tp91bwcvKSp19BJ3D2hAuLQMFmuv3FAo8PlYbzR4r6WoK0TGze059PTircU8ItGn2Yw3a-JlOH0n6BAIWbcvZ35ZH58sSMK_AHLr6UHeQJz8VWWuKEFOKTLfCj77dShjWLzBm0O6-s8c9a-WwKQBW9V16-TaibQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، در حال انجام تمرینات بدنی صبحگاهی با «سپاه دانشجویان افسری» دانشگاه تگزاس ای‌اندام (Texas A&M) است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71900" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71899">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام:
بیش از یک میلیارد بشکه نفت خام از سوی شرکای ما در خلیج فارس از طریق تنگه هرمز ارسال شده، در حالی که ایران به لطف محاصره آهنین ما، حتی یک بشکه هم صادر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71899" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71898">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71898" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71897">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lplEOma-Pf4arlUkrZ2fseGPGbTON7tq6ZceYy-im5fZ3nEPbmqQBfJgT65sLLhRQhZ9xrSyx2P4VEoPkAazGTOYfE9PQsH6J-lxT4IBoHnpqdglT1W8vy7fXx00TQlzgNZweLerHj3EGgvCv8rxGeHal-ZEuEkA3M8v0Boejzv_nsC_JsN3J41nZiJlDRGCQ8TRu1eDgwkbbbR2hpiQP_f5LBNEV-VG3vvdVwIOiPZlfmeD2kenskP_Dgz5FjTLwHPHxJM-pbg39RXrXupNkr8SRyR-Tz5oeyNWpekUkupxuhXgxGO4yF2lXi4w6TxqTQmKsGsJCpYVFq7Z4f5XUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71897" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71896">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=KCKMRyETMg27jvyhWyRuOgGL6o5epIk3mRbyyfxTC4W9tzbLzTSVgP_8W2He46VoBmLFb1GXA4bsxvNh1AqNRJDGv-5fDiqgpzCZTootOWiDFxa_82NdQCifYcyDfrZYk4Pq2Qfb1QWBGmLavz2ult9Mt1l8T-M7vbGUwxBqxvtdpv82l6imO80wbUFURSW_15Q5PReUuFGhExcLOEh_HU3CERkzn27E2RSnTJPNThhH1rkDIuTufmgrevLygi7MaeYXuc4IFIeeqBoHr7LmzPp3uNY6Iwd816n68SKPsDKyPkKoCkK5dZ27z0SChIJ3bqyUiKOlXnRD76JmztdclA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=KCKMRyETMg27jvyhWyRuOgGL6o5epIk3mRbyyfxTC4W9tzbLzTSVgP_8W2He46VoBmLFb1GXA4bsxvNh1AqNRJDGv-5fDiqgpzCZTootOWiDFxa_82NdQCifYcyDfrZYk4Pq2Qfb1QWBGmLavz2ult9Mt1l8T-M7vbGUwxBqxvtdpv82l6imO80wbUFURSW_15Q5PReUuFGhExcLOEh_HU3CERkzn27E2RSnTJPNThhH1rkDIuTufmgrevLygi7MaeYXuc4IFIeeqBoHr7LmzPp3uNY6Iwd816n68SKPsDKyPkKoCkK5dZ27z0SChIJ3bqyUiKOlXnRD76JmztdclA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه ده‌ها هزار نفری جانفداهای عراقی در حمایت از صدام حسین دو ماه قبل از سقوط رژیم عراق (۱۵ بهمن ۱۳۸۱)
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71896" target="_blank">📅 17:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71895">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=AoiqKjLBC3k3NIU8SMBTF9KeiK8gatI8CFdWhO7uDOPywzYBgg0sqqMQcHin73s6zkO1Eo4iuXYpSWCprPA_5VgsYFf__OgIHKEC5dth67EsRhpILf7e7ib2M0vAlwl9j3jfTxzGUSD77oERuEwNuIk3qGuUOJXZzBYOqPKvtDPu8oZ_Uxm3Ail9UzxdJp9X7lrDTPXDo4wfh6Oaz49Tl8-W5nSHaHKRKO4kShAe3g815-mTYorKyGlFl1CYV73yx0S104LQ9s0sDcPvyvnTx2DQH_jVyPLuGQGCpwe1IJcbin1nZbDdlTPQmB2RxshkT3XeihzIpKVVok20V5iB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=AoiqKjLBC3k3NIU8SMBTF9KeiK8gatI8CFdWhO7uDOPywzYBgg0sqqMQcHin73s6zkO1Eo4iuXYpSWCprPA_5VgsYFf__OgIHKEC5dth67EsRhpILf7e7ib2M0vAlwl9j3jfTxzGUSD77oERuEwNuIk3qGuUOJXZzBYOqPKvtDPu8oZ_Uxm3Ail9UzxdJp9X7lrDTPXDo4wfh6Oaz49Tl8-W5nSHaHKRKO4kShAe3g815-mTYorKyGlFl1CYV73yx0S104LQ9s0sDcPvyvnTx2DQH_jVyPLuGQGCpwe1IJcbin1nZbDdlTPQmB2RxshkT3XeihzIpKVVok20V5iB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند تو صداوسیما :
اگر یک
قو
با
لک لک
ازدواج کنه بچشون
«قلک»
می‌شه
اگر یه
دارکوب
با
بلدرچین
ازدواج کنه بچشون
«دارچین»
می‌شه
اگر یه
مارمولک
با
لاک پشت
ازدواج کنه، بچه‌دار نمی‌شن براشون دعا کنین
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71895" target="_blank">📅 17:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71894">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUoTkreYFwv5DVColQQi1ecfKxGa6vQbjDml48BpvfRW1a9z5tNrXlt2a0xJ8A7cL3gNc_KmgE4rqlbUHplXP6dq1rISvp8NEQBQ7lpkCxbyAcrdTCQnvgmXFe3nrp1SQc9UqM5SFJf-Z6oeEA4nba35ztLAf2oKsbdKcA1raxKjdrzsMxu1_A_rYz1PCFiOeRktlfkEv0hRPYJkcuraNYeyTXDdue18NP6FCYJpm-2_71s0BZ_J5uqpD8lRgNs60KUUc1K27l01y4f3IlZJigFKHXKeVe1dBkvI8N6-8RAqKS6ro3tDrnTr21TsSvwAbQTOL7qdYE6nd-GGzRbCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون روز جمعه ششمین مجموعه از اسناد مربوط به UAP/UFO (پدیده‌های هوایی ناشناس/اشیای پرنده ناشناس) را منتشر کرد که شامل ۷۱ پرونده مربوط به بازه زمانی ۱۹۵۲ تا ۲۰۲۵ است.
این مجموعه شامل ۵۵ فایل PDF، ۱۵ ویدیو و یک فایل صوتی است که ۶۴ مورد از این ۷۱ پرونده، حاوی بخش‌های سانسورشده (حذف‌شده) هستند.
در میان این اسناد، سوابقی از یک برنامه نظامی وجود دارد که پژوهش‌هایی را درباره موضوعات غیرمتعارف — از جمله پیشرانه‌های «وارپ» (warp drives)، کرم‌چاله‌ها و گزارش‌های مربوط به آسیب‌های وارده به پژوهشگران در پی برخوردهای احتمالی با وسایل پرنده ناشناس — سفارش داده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71894" target="_blank">📅 16:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71893">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=XdjJzn7qINaCy9TAPK65oOavPa46U19qz9T02MKMXlbgsUr81szGNR-d1gCExywIKvF2wygoXTzi6Hfwg173gFA6RSCeadreszzBhi24hrCb9rraBOdiVe-Qu974jErtx2Af7TTmMFkGdHMFXNOrXnpGXCieKq-Uo4gsPKnFOGrbv9HdcgcVW5_T4kbAbT5jsfTrtL-tSWSYL6ArYjisgI6IQ2XW6TcIBHr5r2tyNq1jB6RLWkKyeLO1aC45vdyFTy4WqTumLNLjnzj6x4bNEtKh8fA0ENqH6aMLdo24zOjxi81tMTrKj2QM6joJdK71w587M2RT8LhfAWPG1Ak4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=XdjJzn7qINaCy9TAPK65oOavPa46U19qz9T02MKMXlbgsUr81szGNR-d1gCExywIKvF2wygoXTzi6Hfwg173gFA6RSCeadreszzBhi24hrCb9rraBOdiVe-Qu974jErtx2Af7TTmMFkGdHMFXNOrXnpGXCieKq-Uo4gsPKnFOGrbv9HdcgcVW5_T4kbAbT5jsfTrtL-tSWSYL6ArYjisgI6IQ2XW6TcIBHr5r2tyNq1jB6RLWkKyeLO1aC45vdyFTy4WqTumLNLjnzj6x4bNEtKh8fA0ENqH6aMLdo24zOjxi81tMTrKj2QM6joJdK71w587M2RT8LhfAWPG1Ak4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71893" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71888">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aSikH6D6gePRiKpByQMEg8uMhMj98YheU5rZYshTxKSS6FCuspxcFLrJbYlPFQefSLK0N7E4X_AzAt5OWE3hygWnGvKTex1MB1gX1sJxmd-ixI8vtninY5JovnM0nW5SIRAghho0vV0iJonyGKM6oe2s92aQlHSCnLXAWda4JTRHrKmRewY6fNjMVTpbObW0lTwFdhq2X_c0ZsKkv28tuOlNbWhP-m86muTAPC1l8hZl-L1eaRs7hbpRUaZhet0GL9o1HovRynimrHT2NBPxa3Xid4LjYyb9W3Nintx_iX47XxEqSiR-6PsT_SggUb2hnAdq_IAo8O7o6lGuqk7ZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Af5Fz-SSKWI4V2FvlKNfuUdokWGya2f3yr7thOnoOEGo1Q5KAWyYjJbBJwBhi9xM66g9oxuUKeju53WsUr7JfeJDrE6ukRWqWp9JwCj2MsAkKPbdjGvbhptCl6jHDEBOkUYs1HHrzcZ8LkhM6G1XuybTBzFRDFj9hBwdR38OwBTPjxp_MxR6raFhJi7qS97908hol_dAgCqVl6aKrV9VPfk2P8TDJRKyBnKDT76ewik_MZC_zGBUFN26rF_dOSdBI51XioCmUA98quBh2OVBDYxUH3hLGuwb7sp3TDGM956-LbcywL1K8iZrg8bEr1ydGC4Zq_zOyfPHN_iMqhUl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jrXBgMkEQKrnml79xMtqNmMinoPqEBsVa5M8QNQeKZiiix9q5-INZO87Rwx8f-oRCOgOAL0TEylRGt1-p5OeJUpphhhfRVUEEuWVSLnsoHbNiZqC0_D3VGKsW--yGv5tJQQD2EWG8CngYzPs6IYgJWeXlSo6bA1rpc4KFsjDW2WehNBx9FFQFGGThMSwLpsA2kNZW3_YXqw5PvII9Byjn7abzJ2jop3E7FCtgHjVPWBcw2hdqEXnwl_m75WEQQWBvfu28FNy_zxlzQ0T49kWsuEqavmKy7xj82L_023O-g1r-YH_09dqzlrRDR1wcMiPUjTlQ1dHFg0U4dS2pz-GgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C93mDZUXTIdLxuOvBkgN96nNposhvHFdI6nyDyeMo9BBVIhEBM-txIdB_36Hrfw87eKllBmsntCOestm_NZB_2BxfoeCLBGQmyf-gFRy0G5Vnv2EYcqVx3H1pb36Vnv2fqQMTYP4scK2udo5S0yW-emLTLKxpgktnkvGCvLG4A_He43mavkydwS4R4-PwaUr-GM8Xgq3Ezi9sKOYYJ91xlLePs60DY6qbU3ptmsbOUsMPohm5tbLNQqEw0_mfNG6xkY0FPmVh5OWmsneMAkASjuvE1sRNQcV2xO0DcqrczHRD7aQYlmY6z8z2QSFr8HKjXegeXzc1aDW82vMXivDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RVvL-BGqhmkUEkd3mZI4fkCbgbsILTjFtqZPwbrXtx7vpGr8EwZlmfySKR-hDtQVqwHhkQp1nrn4Obm8Z-0FivojH4pUrJdqIlEUHK3hplkO1i9KOull3JVxyvYsy1MOEStGW6A4cNP5yzRiJ-hfvW2MtegcRQPzJkJQofDUDoXqYI5VF85dfkHWMQPrs-o9dA-gbJk4hHhXX4GTd-qaItixl7sfIj5m2v-HttzAHBWYYeE9P5LYZmP4LYxdMRZMKw0f_t4p_tuloAYjDrPNrq7pxNlb4CH69q6Bl6yT5sSbx6lmqDmF3UwgnKes9wKFsr4r3T_Y0F0iDN_-p84lqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه «میداس نیوز» (Meidas News) پنج عکس منتشر کرده است که پیامدهای حمله ایران به یک پایگاه آمریکایی در کویت را نشان می‌دهند.
در این گزارش نام دقیق پایگاه ذکر نشده، اما من آن را به عنوان «کمپ عارف‌جان» (Camp Arifjan) متعلق به ارتش ایالات متحده شناسایی کرده‌ام.
تصاویر حاکی از وارد آمدن خسارات سنگین به یک انبار، محوطه بالگردها، یک پناهگاه مستحکم (که برای اسکان نیروهای آمریکایی در شرایط حمله در نظر گرفته شده بود)، یک ساختمان چندطبقه و یک ساختمان پشتیبانی دیگر است که همگی در کمپ عریفجان واقع شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71888" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71885">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMaGTR300o2-iyOF08xRIBj3jgR0E-EDfsp6OQqOXXYPADXgn6VLDN1CMfJF2Q0m5CYkGd3Et6tpouZS1yetEipcQm5wPlbpveFLGYm9fv0QClMP1IG81Iq2PtFx5WngzYkYtHW9pl0WknskLZ2Kjhywz3Dfd3TuHS3hWhRhiabrOAYsiut2tKozq9HliaMPFL7frZ2_ht9j04cIucti7T5Xy_G5ly4UmZrqpzk_w6sHhViiwGqywdWaAL-9Z-rA1ba8WKi7lZABNShT1-SEPsZjURZZN-_3yevAT8Est3_pHjoRE28fAJADAY7u7-YUJ4Wv8aPJ9X6Zgkcwcioynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/poqr0MfEL03N8JIFkL_qg7JOx_O4AQBVwXanx8O2zeLhngiETGSTiBlZSsCyH9Dd1gL93RcgVxPbiwCNisLWGQdUDG-KuiLN0ghXjiHxUz9c-YdvpXoVGufopS02eyweQOy75_LyWKusa4cm6Vbj7erHh78WECOCQTSwn8YfDeX0eSnmgGrAyN-01-Wtfo9GxWD-miQ1AQVAnNYbjSSluZfv0OA8Krs0VpEmhBjqnsmZh7Y5aXzgwlEihZgDOTCDCSvZ-rkvNoWJnJw-sD7UJ-8cGifWPFrX3rQ8aJwV44JHxeK1BjHrHqXgeyoEKwwINWQEJCGfbLN1JOlIWI54aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aqpa0u8WGr0lAuSLyF7XM3d8Cn9rqaSdgCwmzof6htkGIzoOkj7E16n251u24iaHK4zwEEg7BQ6M4OleiLkPKCtdoP3Ig1mrXuNRZy1W8pscAVLub05M2hrzHXPO7xzNTK2G_ZLoVi4a3RUS2N39aAwpxumbSnchvS1U_1B0BfxHAefeAlEb_MqgkIQsRb1prTHDnDKkNVyD_KszUElCbJwo6vp_CkHlY9WXjxcZ88qRsC1elNEsmRPD0WD_jZJBx9DVfxAwT_j1jN5v-ZkLRF2kYNDbaog2kDrYknId7vZn3jrnLUDtPc54dq9eusQdF3cC2OFlT3MlGZ1Tn6GVRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71885" target="_blank">📅 14:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71884">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=TK7IqC7x3GdS6t9bDO3b25HeHwpyboVZONmwpJHOiStO01vKbUpfOjL0j3DETRzuG4wPjNIK7D5hqtnlpCZLmgvKj7zOr6sksi0y3mKxajeg3Z9_7wh6mE3_n40TJ5lJbIXrhCsqqrjdPjYf4wuU26Q4ZygXbJ0zMzkZdCR-HViZFYYZmd2t2pa_fZczxjuslegl_hxJfRDHFR-B9mkSkDgnNCfqnMKmtPRwb7Uh7Nx7bQyyqWoo8vxnf4PZfzFpFm9oajT5UAIGe3NGCJ0daM0GHsb4SVCZvD_OObV3AvvzGrRijFFey9ox9IyIu5CrXxLkhhC_j1o1bY6jpH88Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=TK7IqC7x3GdS6t9bDO3b25HeHwpyboVZONmwpJHOiStO01vKbUpfOjL0j3DETRzuG4wPjNIK7D5hqtnlpCZLmgvKj7zOr6sksi0y3mKxajeg3Z9_7wh6mE3_n40TJ5lJbIXrhCsqqrjdPjYf4wuU26Q4ZygXbJ0zMzkZdCR-HViZFYYZmd2t2pa_fZczxjuslegl_hxJfRDHFR-B9mkSkDgnNCfqnMKmtPRwb7Uh7Nx7bQyyqWoo8vxnf4PZfzFpFm9oajT5UAIGe3NGCJ0daM0GHsb4SVCZvD_OObV3AvvzGrRijFFey9ox9IyIu5CrXxLkhhC_j1o1bY6jpH88Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف سوال پرسیده: سخت‌ترین قسمت پسر بودن چیه؟
جوابا جالب و دردناک بود:
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71884" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e492d945.mp4?token=E3AAxk38GmmSpCSCILWFSyklevMpDtvbDA6xAI4oKMQkL5PBt0sgr0bNuK9e17RmAP4dFswrNYHEehJov6F0N9Vdvc0vkmeYfGA16--wJLlYI__hhFjgwg5RtequTcrEfOqwjpg4yM3NNpLWrH_2wnRiqW2dQ07BwojcAen5LnI-cSWfo0ZMGaB41l6VGdZRqnVFG0P33XGkKhZOv_51PjC4rppV-EjhMRXaQzrC5Nf6QFBX4sCWUIxZ-cZpjuiKcDll1FKL3Ay9EIwCsDyzarLAlBQnE4zgMMopAuG-3geMhwbA0pKYLlzsRBzrmPBS-AdKzicMyarpoKQQb9GWtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e492d945.mp4?token=E3AAxk38GmmSpCSCILWFSyklevMpDtvbDA6xAI4oKMQkL5PBt0sgr0bNuK9e17RmAP4dFswrNYHEehJov6F0N9Vdvc0vkmeYfGA16--wJLlYI__hhFjgwg5RtequTcrEfOqwjpg4yM3NNpLWrH_2wnRiqW2dQ07BwojcAen5LnI-cSWfo0ZMGaB41l6VGdZRqnVFG0P33XGkKhZOv_51PjC4rppV-EjhMRXaQzrC5Nf6QFBX4sCWUIxZ-cZpjuiKcDll1FKL3Ay9EIwCsDyzarLAlBQnE4zgMMopAuG-3geMhwbA0pKYLlzsRBzrmPBS-AdKzicMyarpoKQQb9GWtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای امنیتی پاکستان عملیاتی را علیه یک هسته تروریستی — که گفته می‌شود متشکل از شبه‌نظامیان «تی‌تی‌پی» (TTP) است — در منطقه «کوهات» واقع در استان خیبر پختونخوا آغاز کردند.
در پی حملات بمب‌گذاری روز گذشته علیه مسجد شهر، شبه‌نظامیان مسلح یک مقر پلیس را به تصرف خود درآوردند که منجر به درگیری‌ای ۲۰ ساعته شد.
نیروهای پاکستانی اکنون این مقر را به‌طور کامل پاکسازی کرده و تمامی شبه‌نظامیان را از پای درآورده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71880" target="_blank">📅 14:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=jWoaPQhp1RzMuHJGrUWMDd8qOZmF_W3xpJFKPHSK2U4IVYfhRQ-Q0KTNIH87q4bSpUZ04XbDEgn4x1x7nVrUthcy_BtaYwEgu_IYQeMoZfOtPkRAlcwD86juxnWhgAcGlgLkLZT1BRW1ocKXNFgWMdG-Of3CmwdDEOcIzO0O7xC8uwN7tB5MYfWbQXcithqsqv0Au_to3OpVQFGQNTy4mEv9DNGusEpLX6nePNlvdyVX87_jqcabvYhd22vyDfoTrjMEPgRw2vVEWzJwCOzAX-CYgE85-qJ8Q8WgofPk5k1jELuALK2YX73_BNQ0NUcEpirBxtfh9hYTjJ9RBDwBvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=jWoaPQhp1RzMuHJGrUWMDd8qOZmF_W3xpJFKPHSK2U4IVYfhRQ-Q0KTNIH87q4bSpUZ04XbDEgn4x1x7nVrUthcy_BtaYwEgu_IYQeMoZfOtPkRAlcwD86juxnWhgAcGlgLkLZT1BRW1ocKXNFgWMdG-Of3CmwdDEOcIzO0O7xC8uwN7tB5MYfWbQXcithqsqv0Au_to3OpVQFGQNTy4mEv9DNGusEpLX6nePNlvdyVX87_jqcabvYhd22vyDfoTrjMEPgRw2vVEWzJwCOzAX-CYgE85-qJ8Q8WgofPk5k1jELuALK2YX73_BNQ0NUcEpirBxtfh9hYTjJ9RBDwBvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبیله‌ای در جنگل‌های آمازون که با دنیای بیرون تماسی نداشته، از هوا فیلم‌برداری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71879" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=W16CqbaIeIvlK5HhI4Z9L5pMMtqlsTr3v9fCIXGkiYovnIhcMdTToOLQd7dvzgi_AAZwRTfEiFo-oEfE4wKV0HN032KvtS4gjxdZisXhfJm7GPJTtsieqI3IjHgPTyk4QmzD7Ju8ejjAZoNFtLLZqXxgQzURiW6Hf4dDRpdciU4j72RV0_Si3rRW73ZC6rNbb6nm2gkVfXXqz7HA_zmBguysQ0oLoojwxzMWZ1h_FR3vUG0qcgMQl-EqchSYdsqIs7ZblHsr99iW6DvDSTHqbupSb3F1KGLT4-0FklsM3eZdnRbxjn_Geg5MS48zgJrwhDKVyjf6TCHHHmKidbnkdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=W16CqbaIeIvlK5HhI4Z9L5pMMtqlsTr3v9fCIXGkiYovnIhcMdTToOLQd7dvzgi_AAZwRTfEiFo-oEfE4wKV0HN032KvtS4gjxdZisXhfJm7GPJTtsieqI3IjHgPTyk4QmzD7Ju8ejjAZoNFtLLZqXxgQzURiW6Hf4dDRpdciU4j72RV0_Si3rRW73ZC6rNbb6nm2gkVfXXqz7HA_zmBguysQ0oLoojwxzMWZ1h_FR3vUG0qcgMQl-EqchSYdsqIs7ZblHsr99iW6DvDSTHqbupSb3F1KGLT4-0FklsM3eZdnRbxjn_Geg5MS48zgJrwhDKVyjf6TCHHHmKidbnkdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیبی می‌نوازد:
«نصرالله کجاست؟ بعد از من تکرار کنید: حذف شد!»
جمعیت: «حذف شد!»
بیبی: «سنوار کجاست؟»
جمعیت: «حذف شد!»
بیبی: «هنیه کجاست؟»
جمعیت: «حذف شد!»
بیبی: «با خامنه‌ای چه کار کردیم؟»
جمعیت: «حذف شد!»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71878" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71877" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71877" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQQSQKxc7Yv6w6d5T2d59nc_t9-AxkcdSE454-_sDuKORfXcZH7VZ1xJz3QnSW8vfZ93_m-ELNlgPqwBhWpYO3PIuEZHSFQrr7c3hjs-7OgMWyvshjhb3L369r3EULXcorQwUc6IiVmxecTmhtGjrkdEUiYhl0eyOpUbHg5OorsHctwL7Th3iMEmLOS2hFbvtBtsqC2vr_GQBBNb4zeG1FvWDaI0uAVTEKM9jbU-Et0a6bMmfwTvlcK3FfiN96Lb6xYcMibquPeTuD8sM5qZ16LUGZFVvGWP7ENaDfB2Jv0XLwTjutP3tKYFkla5Q_rCkL44_Io-2X9czEvm6hPWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71876" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71875">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=h3JJcyS86q05AMnQxUea9StxXG6r-t4Dm8eiPOkHVH42NxpYweRRFrr7Tz6DSTRULRf_JZsR6hO9jbz9o-eB9IMP-zEQgxxWnxtGs_0ibNLVcK6k0KcTnb2r3k5QDDf3YJ0lOJQ4_TGfQK-CoYdP6pKEatDcq-8wCRcWNvPy1Dw-ZFgt2Xcx5qup00UxXG5Aukp74kEzFbu36bAGcAwr3qZ17MQtArMMuYKVUC5fjnl9jJ4vO3dK1pBCXugoYY5SIcO4k0xBfzKBoUbjlLfOn6GCpl591XiJjxp2w4dMU8_HbI6X7rLZ5zP2ys67VRfnuu65duZGxtTFVSbB-EUzjXpJ20f1mmLtrLBO73Sp9jlzBcBd-YQQteXnw-GkwWBdJhmSftYjpdHZUmkJs4fvSaKhqcGUKcTG_bBpioJ7unA6O4n34KwC3U8Xnz0I9Z8liCZSZOLckh2p0Zag5p5wmKMt6hWRvgNFwrQ19xY109JEwXxTZ-M6d8TfNb_nd7KUuJ7LxH152u7PoQrO1z3_9E3nzncMUt4WzsopdSZOMpraZwTCIfZYONWXjKJQTSKdCcuRqmtqlb0cK61X1UWtdo1qHzYBehHS0CCRgOsvArWA1Quk0ih_qzPb4O5ERHmyetoiGOI_u-pcvxo0qxwp4TEjzVUvT9uDcSFf_lsDDx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=h3JJcyS86q05AMnQxUea9StxXG6r-t4Dm8eiPOkHVH42NxpYweRRFrr7Tz6DSTRULRf_JZsR6hO9jbz9o-eB9IMP-zEQgxxWnxtGs_0ibNLVcK6k0KcTnb2r3k5QDDf3YJ0lOJQ4_TGfQK-CoYdP6pKEatDcq-8wCRcWNvPy1Dw-ZFgt2Xcx5qup00UxXG5Aukp74kEzFbu36bAGcAwr3qZ17MQtArMMuYKVUC5fjnl9jJ4vO3dK1pBCXugoYY5SIcO4k0xBfzKBoUbjlLfOn6GCpl591XiJjxp2w4dMU8_HbI6X7rLZ5zP2ys67VRfnuu65duZGxtTFVSbB-EUzjXpJ20f1mmLtrLBO73Sp9jlzBcBd-YQQteXnw-GkwWBdJhmSftYjpdHZUmkJs4fvSaKhqcGUKcTG_bBpioJ7unA6O4n34KwC3U8Xnz0I9Z8liCZSZOLckh2p0Zag5p5wmKMt6hWRvgNFwrQ19xY109JEwXxTZ-M6d8TfNb_nd7KUuJ7LxH152u7PoQrO1z3_9E3nzncMUt4WzsopdSZOMpraZwTCIfZYONWXjKJQTSKdCcuRqmtqlb0cK61X1UWtdo1qHzYBehHS0CCRgOsvArWA1Quk0ih_qzPb4O5ERHmyetoiGOI_u-pcvxo0qxwp4TEjzVUvT9uDcSFf_lsDDx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنری کیسینجر و توضیح سه مسیر تاریخی ایران:
دولت–ملت
امپراتوری
ایدئولوژی خمینی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71875" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71874">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=kF77RABmlmi9Hhg1c1sarRFVMnTRilpzEfrBacu2X53ysHI_gOvhk29wTc_7RtUqDSK61l2HeAU0_otf17oiv50GJDGY9My4FqhoyVHdcGd6e4ypF7wduygEuzQd4FymmaO83DcY9nvobkW1tyYQ7q4_t_tqis38vkzrxsOiKaQqYtK3LW91SBMULbM-w-nFld-EZRcMNx6n8lnK1ZQz9TBB8ZiaP8ma93nAPaRLCER402Tv09THOtfs1DJRZLFmOhZx7whwhGTAm1DQvsfWZkZCYHhkgxUQeqC1cCLPb2YVNuTcybk6SNSQozvzit-8AwoNZfDOLiHwbGtGVgMe6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=kF77RABmlmi9Hhg1c1sarRFVMnTRilpzEfrBacu2X53ysHI_gOvhk29wTc_7RtUqDSK61l2HeAU0_otf17oiv50GJDGY9My4FqhoyVHdcGd6e4ypF7wduygEuzQd4FymmaO83DcY9nvobkW1tyYQ7q4_t_tqis38vkzrxsOiKaQqYtK3LW91SBMULbM-w-nFld-EZRcMNx6n8lnK1ZQz9TBB8ZiaP8ma93nAPaRLCER402Tv09THOtfs1DJRZLFmOhZx7whwhGTAm1DQvsfWZkZCYHhkgxUQeqC1cCLPb2YVNuTcybk6SNSQozvzit-8AwoNZfDOLiHwbGtGVgMe6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تئاترهای مملکت این روزا تو وضعیت عجیبی قرار گرفتن؛ گویا شوخی های جنسی برای تئاتر ها آنلاک شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71874" target="_blank">📅 12:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71873">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=kFCf099fFytPohTvDb8ravTnRMtEkd-hdLBut31E-i5pBzDCoaoKoLuQ1Z9ToApvOISYPXx8m-aKnQtmpbVkMaW6wXPmzR8zo4S64nutuFIuhJLhSTo0WAXxfoYkBHGZQkD6lwDh2ZFZpEHnKzCsVDwzf-fsm7rIqKMX5HvRa77MCynmFT2-qLlCfdzS2vDj93VxknfyA9ped-Oul58wXoTHhN51PEVZTaAyPdUERo0eh85Hnv3s_8AAlkrrDpPOuL-tOM1ep353LHkWkaJU-29yILX01Y7jQr8QbMtmatdgmIIhFTXKNdBGrAfXVoFOSQrGa1sDyO9bPLuRj8p1iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=kFCf099fFytPohTvDb8ravTnRMtEkd-hdLBut31E-i5pBzDCoaoKoLuQ1Z9ToApvOISYPXx8m-aKnQtmpbVkMaW6wXPmzR8zo4S64nutuFIuhJLhSTo0WAXxfoYkBHGZQkD6lwDh2ZFZpEHnKzCsVDwzf-fsm7rIqKMX5HvRa77MCynmFT2-qLlCfdzS2vDj93VxknfyA9ped-Oul58wXoTHhN51PEVZTaAyPdUERo0eh85Hnv3s_8AAlkrrDpPOuL-tOM1ep353LHkWkaJU-29yILX01Y7jQr8QbMtmatdgmIIhFTXKNdBGrAfXVoFOSQrGa1sDyO9bPLuRj8p1iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه شغلی در کانادا هست به اسم آتش‌بان. طرف باید فصل تابستان رو در کابینی بالای کوه بگذرونه و هر وقت آتش‌سوزی جنگلی دید گزارش کنه. عمیقا حس میکنم من میتونم خیلی تو این شغل موفق باشم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71873" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71872">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=oiLPj6v6G5wOWt2hmxkUXe7qAvbh2_7SvY_3Vz0ZrKf5DCY1yc9hRGWKTV5W21xme85WUxMb9v8oD1yzmbqpWC6qLzE9hWqIKpvyp1B5irEc88DR-0vUFxX5Ek_MJZFKWr21gcvJy6CVif6IPDSubn5Q667F-zVHlKYVdvNxNRIi42OOsaQqMuXYIYzg2fKOtPAdhDSqhp-GVvTbpMuuWQrLyceXiobLRxFTTRsBeUOJs0ByVaHna9-FE7Um5vEF1ub7G_Qjt7PGCDZICqa_ZWv29wmSGMcTA0qzzgeRRPeQh7VFREnyo8E5y9ldJ8zj1A7dt3HS9ncsBIKW2heqZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=oiLPj6v6G5wOWt2hmxkUXe7qAvbh2_7SvY_3Vz0ZrKf5DCY1yc9hRGWKTV5W21xme85WUxMb9v8oD1yzmbqpWC6qLzE9hWqIKpvyp1B5irEc88DR-0vUFxX5Ek_MJZFKWr21gcvJy6CVif6IPDSubn5Q667F-zVHlKYVdvNxNRIi42OOsaQqMuXYIYzg2fKOtPAdhDSqhp-GVvTbpMuuWQrLyceXiobLRxFTTRsBeUOJs0ByVaHna9-FE7Um5vEF1ub7G_Qjt7PGCDZICqa_ZWv29wmSGMcTA0qzzgeRRPeQh7VFREnyo8E5y9ldJ8zj1A7dt3HS9ncsBIKW2heqZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور:
رهبر شهید به رئیسی گفتند چرا به امیر تتلو نزدیک‌تر نشدی
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71872" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71871">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=oChpORNNhX6mf1F9ppwb1rj6cAESOONoPftQNjfhA2ovrLNEBAW31ULVJPxHmVClLj_gh-MuBLm70He3pyF-BT_2Ahlz6dytimhg1zFCv6tY8I_XlBqP9c-Op07ciIzTuE9yvYB4dzjJCClO9USawup0qKKHlPAMheMLCs-PrjtQIjIR-yKWHiUUlTNjyce12QV2vA-kbMbHjWyDIlxR0ET3w8Bm5ioDkYYskYFdgg3CaAWFxbCDJ-3RxLtoAFXm-new8YO-okyDeO6q59BHg3418Vj1Pds5N2Qpqm7lVZGDCCtGh2OHZGtXTtB2h9dwrVD8X81Uxvo3coI-758y6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=oChpORNNhX6mf1F9ppwb1rj6cAESOONoPftQNjfhA2ovrLNEBAW31ULVJPxHmVClLj_gh-MuBLm70He3pyF-BT_2Ahlz6dytimhg1zFCv6tY8I_XlBqP9c-Op07ciIzTuE9yvYB4dzjJCClO9USawup0qKKHlPAMheMLCs-PrjtQIjIR-yKWHiUUlTNjyce12QV2vA-kbMbHjWyDIlxR0ET3w8Bm5ioDkYYskYFdgg3CaAWFxbCDJ-3RxLtoAFXm-new8YO-okyDeO6q59BHg3418Vj1Pds5N2Qpqm7lVZGDCCtGh2OHZGtXTtB2h9dwrVD8X81Uxvo3coI-758y6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن استار معروف ایرانی ملقب به «شیر ایرانی» با انتشار این ویدیو اعلام کرده که مسلمون شده و از خدا طلب بخشش کرده :
کاری به هیچی ندارم ، چرا وقتی میگه بسم‌الله ، با دستاش صلیب میکشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71871" target="_blank">📅 10:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71870">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=RERiqUXviF-rot3AbMRWQSyDysku-1vqYdHup9qtSk1cwjpwdxVGa1ZUV_oyk3YaOkG5o0TEED6x0rBrJOdccWwPyxOtImJmyjvrSphUmGTLiYiMYn_Hxk8uuJ7KQsQO5hJBdqcI8TXorRjw9E51tSMqHEsCkUFtgzyqU-oczF7KJwFQzrQ-WxTbwEPpRB8cPW-oh9xsaDlbF-3e-4gQ--DH8mzWfuc0VxozLzOD4EoWmI0uoheqc9racY79Rc72c4mjwDUAm09XEogpIL_-xEMzLGi2IZXMgHQikbCldXVZKks7DoqC2oczsQm39dC1tL3IY030Z4VmRvkzrQ6Eqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=RERiqUXviF-rot3AbMRWQSyDysku-1vqYdHup9qtSk1cwjpwdxVGa1ZUV_oyk3YaOkG5o0TEED6x0rBrJOdccWwPyxOtImJmyjvrSphUmGTLiYiMYn_Hxk8uuJ7KQsQO5hJBdqcI8TXorRjw9E51tSMqHEsCkUFtgzyqU-oczF7KJwFQzrQ-WxTbwEPpRB8cPW-oh9xsaDlbF-3e-4gQ--DH8mzWfuc0VxozLzOD4EoWmI0uoheqc9racY79Rc72c4mjwDUAm09XEogpIL_-xEMzLGi2IZXMgHQikbCldXVZKks7DoqC2oczsQm39dC1tL3IY030Z4VmRvkzrQ6Eqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اسلامشهر ی موتوری خیلی ریلکس و بدون پوشوندن صورتش میاد گوشی ی دختر جوونو به زور ازش میگیره و فرار میکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71870" target="_blank">📅 10:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=C82SbWD39m06N6os8VK6NxzCLeavpDci_9zZ1A1E6AHbPXpgC-1SpolgE1bdm3aLTIne2nYSNb622v7sp4c-bpGhotrGYTcry7rRhzzOfPJkNtGssK1n1ahpUPPhvUcJD2PLXefY69vbH2gL0ZUnPKvBLXjT30EIcZT280OlNDwDSUjKDAA-quQRi2nPb9Orb2YNK87joSBnVaHU4zh6n8yYgtZzLXABUp9aqRCOhFuhcT1rbR8X-sJt9b25fVavkFA96bZOHcvXEk8mHytFZFN4rAH2FLYhcprUrXRSanK_-dQtvy24F3p3pQVyBx7UvCRLxYPAmkYW_NfYkCkp9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=C82SbWD39m06N6os8VK6NxzCLeavpDci_9zZ1A1E6AHbPXpgC-1SpolgE1bdm3aLTIne2nYSNb622v7sp4c-bpGhotrGYTcry7rRhzzOfPJkNtGssK1n1ahpUPPhvUcJD2PLXefY69vbH2gL0ZUnPKvBLXjT30EIcZT280OlNDwDSUjKDAA-quQRi2nPb9Orb2YNK87joSBnVaHU4zh6n8yYgtZzLXABUp9aqRCOhFuhcT1rbR8X-sJt9b25fVavkFA96bZOHcvXEk8mHytFZFN4rAH2FLYhcprUrXRSanK_-dQtvy24F3p3pQVyBx7UvCRLxYPAmkYW_NfYkCkp9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی ایشون دختر نیست و یه فمبوی(پسر) ایرانیه که خیلیا روش کراش زدن و توی تله‌اش افتادن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71866" target="_blank">📅 09:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71865">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=JiI0R4okYhuWlxCv5mxCDvFMAJMX6Dft1_lG2-8cumUVSmA21meJXh-md66I3EKhbD8Pf4p0ZJgqBbOoFsDnMptNX3yH7oxIyG0fGBCL67Q51UP2fv8bwZIbFYg7BCaC43x-vTYsqjNg1xVwHpkHXkybewpV-JI9fXjO4rOADth4KQArje8a4xt_-snJ_mg2LwGGcJhm4MHoTANFa2GWux4dSr7HyxWEfrGIcKfIlmvSoATzeNKyRiABjpnCGV3TNnH0a_ISoiRdDBp1cTEkZhqV7fx4PmCZJz8emZrFkKXYFDJ9Fbyi1O4xU03hAyhpYZGrqvV6D4IICipN6gxaz0HNVjglTpLSnGLJn2_IhirNm8mZaHnlFC4iZWdkbOjKVPVEZazL2Bd27VWX7zZ6-4TQmP-DIY8ZOA-Hg5W-nM8WmI-xN5LcNcOtv4c4VB3hugDvpTK_YvFvCIAuhB8hfyd5EK-AxntKGQHEsOpUveD5U4fJBGdoHpcef9g9blvAOf9G-vcx61s_NohdaO6zfWF873FkWC1BYBhFEvTz2BKd8UwrictmiqgI3e-YxW792hhgwA2KzBkJc2gdhgsa_LjQKxxTtnQbJuJFJHCrWtSC-BtS2uCdZUVQ8HaT_v_qxY7C6EBznD5L_gc5S-u984PcLgXJbhGPDjM9_1NKcvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=JiI0R4okYhuWlxCv5mxCDvFMAJMX6Dft1_lG2-8cumUVSmA21meJXh-md66I3EKhbD8Pf4p0ZJgqBbOoFsDnMptNX3yH7oxIyG0fGBCL67Q51UP2fv8bwZIbFYg7BCaC43x-vTYsqjNg1xVwHpkHXkybewpV-JI9fXjO4rOADth4KQArje8a4xt_-snJ_mg2LwGGcJhm4MHoTANFa2GWux4dSr7HyxWEfrGIcKfIlmvSoATzeNKyRiABjpnCGV3TNnH0a_ISoiRdDBp1cTEkZhqV7fx4PmCZJz8emZrFkKXYFDJ9Fbyi1O4xU03hAyhpYZGrqvV6D4IICipN6gxaz0HNVjglTpLSnGLJn2_IhirNm8mZaHnlFC4iZWdkbOjKVPVEZazL2Bd27VWX7zZ6-4TQmP-DIY8ZOA-Hg5W-nM8WmI-xN5LcNcOtv4c4VB3hugDvpTK_YvFvCIAuhB8hfyd5EK-AxntKGQHEsOpUveD5U4fJBGdoHpcef9g9blvAOf9G-vcx61s_NohdaO6zfWF873FkWC1BYBhFEvTz2BKd8UwrictmiqgI3e-YxW792hhgwA2KzBkJc2gdhgsa_LjQKxxTtnQbJuJFJHCrWtSC-BtS2uCdZUVQ8HaT_v_qxY7C6EBznD5L_gc5S-u984PcLgXJbhGPDjM9_1NKcvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آیا خواهان جناح چپ هستید؟ (جمعیت: نه!)
آیا خواهان جناح راست هستید؟ (جمعیت: بله!)»
«آیا خواهان تشکیل کشور فلسطین هستید؟ (جمعیت: نه!)
آیا خواهان کشوری یهودی هستید؟ (جمعیت: بله!)»
«آیا می‌خواهید تسلیم شوید؟ (جمعیت: نه!)
آیا می‌خواهید بجنگید؟ (جمعیت: بله!)»
«این جوهره‌ی این انتخابات است: یا چپ، یا راست.»
ما در جناح راست هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71865" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71864">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🦖
اینجا فقط ضری ب‌ها نیستن که می‌درخشن...
🦖
چندتا Star آماده‌ست برای کسایی که توی قرعه‌کشی شرکت کردن. شاید قرعه به اسم تو بخوره؛ امتحان کردنش که هزینه‌ای نداره!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71864" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71863">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/news_hut/71863" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71862">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">#فوری؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.  این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71862" target="_blank">📅 01:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71861">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg7c_ynTWxfzysTiYVN8ut4j5revSTHeEZtZfQFJvaKIJ48XRpsB-foEoTWroaJlIzZh35FmpqetEU3fZEi7e0_y6p_pHJgLOMt6mS0_ZIN750FQ0ia7yCMhEZaCAq57bKwQhdvKs4_LCvrvUpzcpU2XiZGHVOS7Kb_MJEY_O0ThdjonBN4hAiyKbECdN9n-eBlMm7_9LPyrRYAG8Nv-ekUdmur-n9SNIEsIfeJAFEI12VehTufs3LhcUESnsjSMSRGwDRKVNk3jGq4Yx3Vqh7PPYRBUPGx3_zYcgkZqpJDwX_C2sVN4N0HdNdgwtkTNtKRR2arLlL-4OP8e1LNRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.
این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را تمدید می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71861" target="_blank">📅 01:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71860">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.  ترامپ این توافق را توافقی با «عمر…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71860" target="_blank">📅 01:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71859">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O57w9_z2eyBjALx1u5MfRQeGUH_IRVNirwzEDA-pDniOp4LQMTfUOHE4rF_Ug-s9qOLWaBMg_YVec62UDgIEeSAIC0JPFHYDMXuQJ6zQUVmjzgmJ5JaXUf1wefjyDrwQNteABKvZFTAuIrZabFPrgmVfztwWlHg7nZEbEQrxWPaQnSMvN5k-GMOaLFjwwaPnNqjbBqxwqCtLBn826vUUaNwN4KnNTSYCrJF9m7PiX3AhLh3ifancRw8MxHtXuPky-Lr1LYoLdd7KB9yrBWBlSC5r3tcCqmB7jpiZ3460t8myUWg4eRh0RtiIOraAfHEs__9Coe0H4SbwsUxjEcz4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.
ترامپ این توافق را توافقی با «عمر نامحدود» و «بدون تاریخ انقضا» توصیف کرد و اظهار داشت که ایالات متحده قادر خواهد بود اقداماتی را که برای دفاع از گرینلند و آمریکا ضروری می‌داند، انجام دهد.
وی همچنین تأکید کرد که هیچ‌یک از دشمنان ایالات متحده اجازه نخواهند داشت بدون تأیید آمریکا، در گرینلند حضور نظامی داشته باشند، پایگاهی دایر کنند یا سرمایه‌گذاری‌های حساسی انجام دهند.
او می‌گوید این توافق برای ایالات متحده «هیچ هزینه‌ای» در بر نخواهد داشت و واشنگتن بلافاصله روند گسترش حضور نظامی خود در گرینلند را آغاز کرده و در زمینه ساخت‌وساز و توسعه با مردم گرینلند همکاری خواهد کرد.
ترامپ این توافق را «تاریخی» و «تحقق یک رویا برای ایالات متحده» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71859" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71855">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1RkbYLbXHzaOSdYqWVEugRnRjzOp09li2kox01cgeWGz6KhXRu1CO8BuWFRefbRIwLNkIJKy5dLV62xQiRKaUMGg682ulv_Ms3lWI-DwTshtgK1de8nLT3I4OtiZVS2kSry2htV5KZd-4Pjy8z8riJY5bFadJC2aInurPV5Od-JeekofygltRai-poPW1-CCSZeOiE8Sit49t1YHrqjvC6bW0R1Vi1Hs2dCb18v1NWqrLbKGgVCqwIJcBBfMMyaNAaMcvWkBf_IoaOITme5NovE_F1C3ur5dvHHim8evLeOALrqnGAoDdQ8FkyYlwY0Zz-lh_35BAwrli0D-2siWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7u9tW9Z9jmSjD2TTAdxTYL3i10x395d2Ybq4M2zYfe_v3qknjsRczNXADRmz5zfHtgLYb3uReNSFStT1bGoYPeppqT3ZzKfbqanDeY6cjpVKVBgXavIkFzm1R3WVbrPkWWETb0cbY55QOxF_H8uNPWatP_J49Mfo6ILGNUki5SrSn4ZJT3kcA3GNFHKfgNU_pb6V9-kduyxkHh3a8pUnGyJhUzT1Yjsy-mLDQQT6b5dLUxUP94LeDX9_vgfWMmN0hOJqysmWG-yBuGCUS71SU1FNHHY0kbxSRp4Oq5vhwVWn6iFlMvnTeC68E51gpA4iCvfCkh8x-kSQZSbJv60jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_uGo_8ALSwFke3mwNHrEEfJqzPsiczAARLvkUtY45QnH7LZ4AkTPUvNXJk6FY_P8RVs5Eueg2q_8xlS3LuUnXlXFDu0S5AgSCGrdplkLZ7QYm38pXKexxXpRd0Z_3R50Yzvo3B-BAUeBVCe8twrVbWKsZzfyDSPk1WINxMAu02LYbN6pjwC_WXCt2LZkT8blP5Yza6XYzLog7UCGXIf-GBY5Pe7kCD5yJEqiQtVr79AehDhgAPbZ2VcaA-lC_tFw8pbJwzOHhW-y4tIBgeIh5DPAWi9ziSzbyPIc1s5UOsZkP0bvWRULkE74cKIfXSTo-HJ-dCO8SxK5CA4nJHL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbOACW4qBXJsTrYKvOSszlxg5EnjeZ12E-dAYYJnhTtXm0HW5tRJN9p9g7hyXQFzjI9apZrbtW75gv7qW7R8RfOIzhe1ZWqEXowXKWaKhKC8V6VdcMpk0As5XAkSkbgihdu6vmg8LJhdYYyOVX-tb5Ndz0keU7LQQRRvqkFgcaZOYOwgwP8hQ2jQYpSJLdTss5HPzeCHqo-Pr-TE785B6_6dscB44Mh0Zrd9FbI0wy5DwIXj_sLqipkpmFbucfCqymW9WJ5PRvhu7JPY-g--GsvKYUeOCk2x_bqnB32J599OEKqOXQ_8Zi2so0rzYPnG5aG7siT3faWSa_EWcVFiXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سنتکام:
تفنگداران دریایی ایالات متحده، وابسته به «یازدهمین یگان اعزامی تفنگداران دریایی» مستقر در ناو «یو‌اس‌اس باکسر» (LHD 4)، هم‌زمان با حرکت این کشتی در دریای عرب، به تمرین هنرهای رزمی می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71855" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71854">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=Rh6443mge847tHgfBE9RUgP7i47l1-qHmtN12dHJnwAQ9RPnNL0QiTIsE2s540lsQocRsCNMd5XflBzVeUFeRd6VTW4iOM_VdDwc4vJcsmQlTWtvf62d2XOodAMBcCZyh-zVsB9pHH87Z6MQqX6zp20b2_2Xj3lqAbMtrLhcRc1Z2mS2eoIhtm1lBSFLR3z-o_Cn0YVOgoSKsWoCv5fMXOSb-QBw_3T-gIfuaTCiEe-ZDb_3iBqH3byR4S2NzL8ONdJ5AUwBZrxoduwaJpXRDRGxyVPpx9S742DjUkChYYu7Wboevf1TAV5v_1ZlYwUEWqz6D28qoDyr6ODt4tZ6tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=Rh6443mge847tHgfBE9RUgP7i47l1-qHmtN12dHJnwAQ9RPnNL0QiTIsE2s540lsQocRsCNMd5XflBzVeUFeRd6VTW4iOM_VdDwc4vJcsmQlTWtvf62d2XOodAMBcCZyh-zVsB9pHH87Z6MQqX6zp20b2_2Xj3lqAbMtrLhcRc1Z2mS2eoIhtm1lBSFLR3z-o_Cn0YVOgoSKsWoCv5fMXOSb-QBw_3T-gIfuaTCiEe-ZDb_3iBqH3byR4S2NzL8ONdJ5AUwBZrxoduwaJpXRDRGxyVPpx9S742DjUkChYYu7Wboevf1TAV5v_1ZlYwUEWqz6D28qoDyr6ODt4tZ6tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
ترامپ: ممنون که این را به من گفتید.
خبرنگار: آیا سعی دارید با ارعاب، مانع از انجام وظیفه مطبوعات شوید؟
ترامپ: نه، نه، نه. من از مطبوعاتِ غیرصادقی مثل شما خوشم نمی‌آید. به نظرم شما افتضاح هستید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71854" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71851">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=vzesh_SkDCHcndfr3QixUwYE_LO2DpWRqPRmustZUU9xV_TSngYqqDwfTyvNn5t3aJR0N44ufN83YPUn6lPBlr0gKOQYttkWP5d4fMjQzw2-jG68N6kqc5w_tLTEJdZ5kWX9jkuWgZq-ERIIUqKdG4ELdFAEwuZ478o38lbFsJf9hM2o2urkhq2ds5C8TlWzAJ921KCozocMsIlI6MafMM76gf01l6c1RYovkNG1A6ZlkL4CriGXli8yJYei5pNYmnXujiB2dmAwqEQwjW5BGMwX0iqzXIeoMhg6K1Py1NiOWc6GIdArZuIKg0JA2-ag2onWdcei1IrNRkA2x_3V7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=vzesh_SkDCHcndfr3QixUwYE_LO2DpWRqPRmustZUU9xV_TSngYqqDwfTyvNn5t3aJR0N44ufN83YPUn6lPBlr0gKOQYttkWP5d4fMjQzw2-jG68N6kqc5w_tLTEJdZ5kWX9jkuWgZq-ERIIUqKdG4ELdFAEwuZ478o38lbFsJf9hM2o2urkhq2ds5C8TlWzAJ921KCozocMsIlI6MafMM76gf01l6c1RYovkNG1A6ZlkL4CriGXli8yJYei5pNYmnXujiB2dmAwqEQwjW5BGMwX0iqzXIeoMhg6K1Py1NiOWc6GIdArZuIKg0JA2-ag2onWdcei1IrNRkA2x_3V7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر قرار بود رأی‌گیری‌ای میان «کاهش قیمت بنزین» و «اجازه دادن به ایران برای دستیابی به سلاح هسته‌ای» برگزار شود، نتیجه آن یک پیروزی قاطع و چشمگیر می‌بود.
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71851" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71848">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuYdFP0dZSoi1mdActn6RLNKUqpIKOlwWvTBF9qrniuyEASVVLC7HjHYiMhgFbLYvigxzuCxwQm7_R2UV84Zi37UX0JXqC7mITX8DelNowxYdnO_GYm5CquNKJhMpEOBz7nUh3nJCqdPXtZFDf9XsCh8hitHwb6do7biJ8EDlzOx8VGSKB0ylX1woG_M_shrALBQI4dblHwyCF1bdA2y6G2UhTtMe1J-8cBlxhZINs5RKqLOlhMY5iO2X8E2ml2wyE0Vq03ZDSWV98Ralj0mndqGwWcHSwpccJQfGVhdf-1ivSxvP1knLt3y-x7l7b_xzZsdGj8PoU6a16IrWJTE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WEY3zV6oTjAQRRUwBMV1gYl3kULIJmE1n5HDcT9zrkhqe7_Ezfc-XpZx5XWbHh5cI1qTd1bY8vrF8ivwVNL7rFOzXrBaU4y973l5oJPa-eGAso-FsDfp-2c31Y7XcE88SjDI0ihSVkcM5TQz2-JQNo87J8jmKK0H5ceyL4PR8n8tuScM-STRpf0uMjIo3T8RZkDDiHC6b0Nu2LHBKA-p9-30kP8Ka7Mwpyu5aYoxZSAqT4kT_hk81d1MDtkQDql5Pha_KkfRXWFL3AFg537Nh31ZxZA56KI-FyHMrOTc5TkNU-p0-L30-_8dylYSRVJQs5mTqy0LdImXQZjbQx2Hpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtkbWEcvywIjfqBuSSAZ1v3fx_rjH2yaP6_ZT7nCqkWLUIMSkxheVTl2MAbUBJqnDKeyeZyTHuq5y5mr8LhMao7oLNldgBAUMitLka71TaSSgjGEl1-g_F2JZc2l7OxsKszhzM4YRYN1wCu6kxhcN7xuF4CuckkmIwhB2HP34NGxmQTCTtRnauyvxiI3J0oDIaPmpgLF6sicDiv-0uhPdcb-SLtCA7FD_Bj3fICoG2cZ0kV2yzMhFD1sb9CxnimPqBookkEBmLHyO2ZboFo4Zy0izg62tibmkxNEQg3MCh4VFrMdKa9PUsR24JrJecKP4GTsV_yM9HyNVuGNzI1LDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گردان های بانوان جانفدا تو همایش امروز:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71848" target="_blank">📅 23:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71847">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7102741190.mp4?token=NQMDr39Ly5SkrJs1iCrjZHy3uPnowS5C9-8wE6vM2QwDFMyGm320v0VeAo5dWsnbcUA7Vp24O7DgISvvW2c5uV7IDl27y1CP1ABN9GzpFqzoFNHUlvBktsBjhJD8ln4JMbNHQpgktpsvZEQmlNIG-DflH7DH1avCQv6sq8RFA4u-BJXOl5QGJpTYYpYSVENLqTMLclemhgnFggNWSDn-utHxhsD8tFDIRoWWYWYjTXbWntyZt6_5trSgqHNH_mWysRKW7pkeyv6kP7N0hUB0kP45aBdpfvol-LU7qlyBBANqbsWLLkgNtRAE9nqR1pcawdY9z1PQaVIW7FiJHsK2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7102741190.mp4?token=NQMDr39Ly5SkrJs1iCrjZHy3uPnowS5C9-8wE6vM2QwDFMyGm320v0VeAo5dWsnbcUA7Vp24O7DgISvvW2c5uV7IDl27y1CP1ABN9GzpFqzoFNHUlvBktsBjhJD8ln4JMbNHQpgktpsvZEQmlNIG-DflH7DH1avCQv6sq8RFA4u-BJXOl5QGJpTYYpYSVENLqTMLclemhgnFggNWSDn-utHxhsD8tFDIRoWWYWYjTXbWntyZt6_5trSgqHNH_mWysRKW7pkeyv6kP7N0hUB0kP45aBdpfvol-LU7qlyBBANqbsWLLkgNtRAE9nqR1pcawdY9z1PQaVIW7FiJHsK2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم تو بخش پذیرش یه مطب کار میکنه. حالا به یه بیماری برخورد کرده که یه فامیلی شاهکار داره و باید از بلندگو صداش کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71847" target="_blank">📅 23:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71846">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=NkN-Ent7665pqIEEEapQJ0HIzf9BUWidrZdtUlkKQvx7eiUKkZxchWToG5FHQH6rmhwQEe6tvMy_ZynO1WXW4y_KyKBzpyfjqm_T_rMgp1Tiojta4PDGUoyAn9dh7YL0_mbr282T6CzkjwXtd_YdvHifs3M4luAT7mIx8YdaPvWgbIwHr051VoC4qJCLePaAzu7Bn2X9WrdTWZiadiglue52NuWuT_dpXvK8JqAcUAb-Bx9ZKZCKoc_HMY6PrAgWnqaUzqFfxXlsK1LybaBb58Y8a9mYQeZnMa1Eq1YsByQFuCzgDMMJ3k6yftRXm8rVtPvGIKGzGo6ESuikAL2Llw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=NkN-Ent7665pqIEEEapQJ0HIzf9BUWidrZdtUlkKQvx7eiUKkZxchWToG5FHQH6rmhwQEe6tvMy_ZynO1WXW4y_KyKBzpyfjqm_T_rMgp1Tiojta4PDGUoyAn9dh7YL0_mbr282T6CzkjwXtd_YdvHifs3M4luAT7mIx8YdaPvWgbIwHr051VoC4qJCLePaAzu7Bn2X9WrdTWZiadiglue52NuWuT_dpXvK8JqAcUAb-Bx9ZKZCKoc_HMY6PrAgWnqaUzqFfxXlsK1LybaBb58Y8a9mYQeZnMa1Eq1YsByQFuCzgDMMJ3k6yftRXm8rVtPvGIKGzGo6ESuikAL2Llw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71846" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71845">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=MQEGG7tFQTDzfKvyMpMJtA6jkl0tI1XBWxJva79RuvBekTkTS6l3l5S34ltP4UfApoYqnuwsfXBaQCeIuevX3jSQdluvye2zQ_hbCs-Mbp3VfopA-6v_Am4tZKGrq6jVV6dN2f7vhxkpAg1KjKhoyKEF0H1-kD6D-gFpzd3U4-nZHa2T6QcblWs70xFmlBP7mQCZF94bC5M2EW5X5ncfpFdQZTbfgFWBWvsccfTSVPkT4OhSuP-FJWmzUDRYKCZUb_mlC8DE9VqUsEkq-th8ys_KItstLkVXjgzO1Gff1l00OowNelZdTxgZWqNfylXFFCpxonmI72MxfQAD6rXiYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=MQEGG7tFQTDzfKvyMpMJtA6jkl0tI1XBWxJva79RuvBekTkTS6l3l5S34ltP4UfApoYqnuwsfXBaQCeIuevX3jSQdluvye2zQ_hbCs-Mbp3VfopA-6v_Am4tZKGrq6jVV6dN2f7vhxkpAg1KjKhoyKEF0H1-kD6D-gFpzd3U4-nZHa2T6QcblWs70xFmlBP7mQCZF94bC5M2EW5X5ncfpFdQZTbfgFWBWvsccfTSVPkT4OhSuP-FJWmzUDRYKCZUb_mlC8DE9VqUsEkq-th8ys_KItstLkVXjgzO1Gff1l00OowNelZdTxgZWqNfylXFFCpxonmI72MxfQAD6rXiYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته شده بعد از انتشار این کلیپ، ترامپ از ترس ۳ روزه رفته تو اتاق درو بسته و فقط داره می‌خنده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71845" target="_blank">📅 21:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71844">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QA5zHceMkI1oaFpF0SjdmAZsnV8kltIhMIWPEvFApscu99Y0LcdMGD2JK_s4MYqgviH9xdDXYE3_PMGbCGJ7ZOgjiM2HAKbP5k8V5FFGacI3dsyfseXpGYE2E2f1oyUAnLFaP_eudbjXAJOKgpPlalC7FAkGAYP0AvwRm4H1vhz3e6y7dSbXlvzG-_pmL75TmzNaqIO4fRReyekqDoC5wVfuUDdWAyoqlMcPUJXfHxgA4-iwl5yQ7coTd1U9WdmfEHmahaxqqvkgvdUeMAkkXfzkDiL5i3YhG1jG2f2TEH1ezIaECjnq-iklVH8lRSXR9Fq6ut5kt0oAIabYzXDjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز September 18، روزِ عشق اوله
❤️
این روز بهانه‌ای برای یادآوری و زنده کردن خاطرات نخستین تجربه عاشقی در زندگی است.
به عشق اول و آخر زندگیت تبریک بگو و این پست رو بفرست براش
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71844" target="_blank">📅 21:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71843">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیروهای «ارتش ملی یمن» (تحت حمایت عربستان) تصاویری از انهدام ۹ دستگاه خودروی نظامی حوثی‌ها (انصارالله) با استفاده از موشک‌های ضدزره (ATGM) در جبهه غربی مأرب منتشر کردند و مدعی شدند که تمامی سرنشینان این خودروها کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71843" target="_blank">📅 20:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71842">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo5ZdRVwNNztYqh5cwqN49WpG7EattvfcGUBFJFP4UtQutPqyB9VVqcsQ34u5MWUshdkhgt8xKLG9kri5fJmWcDjFpqBSUKWJ49o2YyXxgG3eZJHg-OTb9bxhT5IMfImfo1UaK9E4jtTcbH7S-MDgpGC2o2IWc50X8cbipcuJ431iVJ6YgS4r8O-1aHm6aFRKexiIv4rzox-RTdIvwaC1yOJK3CZyy7JCtD_EOruXszrogC_XVPRj4-cBR67bc5t6m2dJ6YXU909M_Mks_Sa11Jg3-FAcWOm9Y6hFtB_QKroFnxxDsybmK5_vdE9hT9OL_vKmiRwueI-kPgN_tplWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پاسخ به پرسش شبکه «نیوزنیشن» درباره اظهارات اخیرش مبنی بر اینکه احتمال «نابودی» ایران را بررسی می‌کرده است، گفت: «باید دید چه پیش می‌آید.»
ترامپ اظهار داشت که ایران در حال حاضر خواهان توافق است و افزود: «اگر توافق، توافق درستی نباشد، حتی به آن فکر هم نمی‌کنم. اما در حال حاضر، آن‌ها می‌خواهند توافق کنند، چرا که در همه زمینه‌ها در حال باختن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71842" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71841">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ به «نیوزنیشن»: آمریکا با حوثی‌ها در حال گفتگو است.
حوثی‌ها نیز مایل به دستیابی به توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71841" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=lEsoViLfLVXvZM4OXkyku58DwQHAuDZIH2dHj5nyj_YtdZ5XA1IgPJfICeaPa9U3op-CY6y9xu2m7X6chHMci5JX9RmqRi7UEu0hiqITeP4azy3g1uZEwLCeqIy_MOzIOQcieu0Z-WqauQCE58HDmDTrpn9woZQjI1_wUUMVTaZXPaNEctz6C1GtN_QQLapfCk8YYvWvfYc-l9YK76Uzqy2JW3dNtt80jjcH3NfGUGrPT1_8qSY4Bu6Qod81L3-Au_zj_sSiiQrcSp4t98cIXOFzQ-7BvfyTGqvRsINFoHj1BkC_QKzycw_J5Z7L9O776V9nNCn33DaFR5A5nSjNyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=lEsoViLfLVXvZM4OXkyku58DwQHAuDZIH2dHj5nyj_YtdZ5XA1IgPJfICeaPa9U3op-CY6y9xu2m7X6chHMci5JX9RmqRi7UEu0hiqITeP4azy3g1uZEwLCeqIy_MOzIOQcieu0Z-WqauQCE58HDmDTrpn9woZQjI1_wUUMVTaZXPaNEctz6C1GtN_QQLapfCk8YYvWvfYc-l9YK76Uzqy2JW3dNtt80jjcH3NfGUGrPT1_8qSY4Bu6Qod81L3-Au_zj_sSiiQrcSp4t98cIXOFzQ-7BvfyTGqvRsINFoHj1BkC_QKzycw_J5Z7L9O776V9nNCn33DaFR5A5nSjNyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
ما انگلیسی‌ها رو از ایران خارج کردیم ولی الان کشور افتاده دست چندتا بچه اطلاعاتی!
تشکیل مافیای فروش نفت هم از دوره روحانی و توسط زنگنه (شیخ الوزرا و وزیر نفت سابق) شروع شد.
درحال حاضر چهارنفر دارن نفت ایران رو میفروشن [حسین شمخانی، روح‌الله رضوی (دامادِ سخنگوی جریان پایداری)، علی بایندریان و محمد‌هادی مومنین].
پسر شمخانی(حسین) تو این چند سال، بالای 30 میلیارد دلار یعنی چندین برابر ثروت ترامپ فقط نفت فروخته!!
این چهارتا فقط تو فروش اخیر نفت ایران، 1.5 میلیارد دلار پول به جیب زدن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71839" target="_blank">📅 19:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71838">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHAomgPEh5yQRd6UDUr3CWpYJGRZc9AAALbYGSny0mg7oHOj21xtqONGhPQ46HaIWY55DkGcLWWyD7IVaJfqgo1sTWD89TKdFFQNHWG4-3orTDnuhiag6zMeDT-vt36ooWGXrrmad4aGL3GcRT61PYdxSpvRq43T3QnXqsBn4ehDugW3Y_288klSYC3Sp1kCok9hepKMPVnLUPlNX1cAOV1Ya1cw0XwV19lDE8uMo8YDpt3Zt4cMgDhQWEn29eNb-MAKcMixNy7vjtEbuQskb_mXXILVfX-PP79En067Ja8J8MNjTV1GQ4Bpx6WebtbIU6HxYsGDIrLWZ-urLT_qnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب تلگرام در پلتفرم ایکس این تصویرو از ایلان‌ماسک منتشر کرده و نوشته:
ثروت کاذب:
🛩️
💰
🏎️
ثروت واقعی:ممه‌های ۸۵ ایلان ماسک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71838" target="_blank">📅 18:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71837">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=C-_8gJdJU1g1XPid3B9tTyJSad_mLUgcx6MmTOyoNWss5fc55PBbbvk_-ob7rwmzN1TN8xi5PhDJAn1qjkSuD-Ri-6LxdyBw0DXn1p2KcPAQa4yyksfY9MP6r_YNPpTFwC29tqvVJ6W4P9C_aagdrNiUg9csRNs8jmuzR4yTU_yiVS0Uwck5ucCzzSJUEfNYEl3ev1_DkOiqzCWDiyDVT9g8xEU5vj0XW9W3IUj5VWYB3egOUCxd1jkeee7bHvgAA9n0crJnysFJUjIdbi-lvPLAr6LXn4LhiGcmMVqNvOUB7TH1CZv9SJx6eglmUgJnSk68NL59FoWQKhX9-FSTaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=C-_8gJdJU1g1XPid3B9tTyJSad_mLUgcx6MmTOyoNWss5fc55PBbbvk_-ob7rwmzN1TN8xi5PhDJAn1qjkSuD-Ri-6LxdyBw0DXn1p2KcPAQa4yyksfY9MP6r_YNPpTFwC29tqvVJ6W4P9C_aagdrNiUg9csRNs8jmuzR4yTU_yiVS0Uwck5ucCzzSJUEfNYEl3ev1_DkOiqzCWDiyDVT9g8xEU5vj0XW9W3IUj5VWYB3egOUCxd1jkeee7bHvgAA9n0crJnysFJUjIdbi-lvPLAr6LXn4LhiGcmMVqNvOUB7TH1CZv9SJx6eglmUgJnSk68NL59FoWQKhX9-FSTaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا «قانون لیندزی او. گراهام برای تحریم روسیه و ایران (مصوب ۲۰۲۶)» را با ۲۶۲ رأی موافق در برابر ۱۵۹ رأی مخالف تصویب کرد و این مصوبه را برای امضا نزد رئیس‌جمهور ترامپ فرستاد.
این لایحه «ناوگان سایه» روسیه را هدف تحریم قرار می‌دهد، اعمال تعرفه‌هایی تا سقف ۱۰۰ درصد بر پنج خریدار بزرگ محصولات انرژی روسیه را مجاز می‌سازد و «قانون تحریم‌های ایران (مصوب ۱۹۹۶)» را تمدید می‌کند؛ این موارد در کنار سایر اقداماتی است که روسیه و ایران را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71837" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71836">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71836" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix_zkSYiL0C0hKbl5Eiq8v35ZHNxhssD9yFOkxaAtGuG9Uo8XUxbsD0ganZUUAWGKKAqiDmKmvu6d-z3nVdVlm2V6SZzKXerJLrqVmD0pLsMjnyKBeprz4OXjkcq0ABDsUDhfmSCZ8NilVnXx6XRdKxlDgo4ABP3plNgoqR_Xs9sfDXAzoihueY1wHjrAp4ivRpBU0fK9jo-0Fxx2-y7M8Ct11LISTwTpryA_QyS-DOJ3ew3Gkc9bGNNECzBU0UXahBhGQCQiIoB6e1RfmjSDtEdVKUBqIizvHH8eIOvmxjG0DMjxg4CQIdeTwidqcMscalUCanZColCKqvMdxO4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71835" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=THRCzrF38plF4gqmoe6YV4QuDlTPp3i8PgG7oGIiyjZuQGyK8Vx4RJpQdwJ2LTUxogcWjBPf97GoB7wL_zcUvEmlkbmtNOalvwcJM2zOFlp8sY72NgFSXUCDYhtz8ndnK06fwPQvbZmOR-Vgqrgm4Mv1j0tw3HIZlIx1kpQIAOxWPheF4D4tbLEr7l04Q7X66uk5nZzekxn5sheyyFFJicEeAEcCesP0UJzfR6sRZ48iGTgzmEtYM4KAvy2Rvjrk3d-2OuennnfuJ2vvc_92ulpe_ZuKpqMWUqL3ZZhDCwf9eXgrGnqb_hsRTZXnriLMuZi_9tPbuvljo-iRI59C5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=THRCzrF38plF4gqmoe6YV4QuDlTPp3i8PgG7oGIiyjZuQGyK8Vx4RJpQdwJ2LTUxogcWjBPf97GoB7wL_zcUvEmlkbmtNOalvwcJM2zOFlp8sY72NgFSXUCDYhtz8ndnK06fwPQvbZmOR-Vgqrgm4Mv1j0tw3HIZlIx1kpQIAOxWPheF4D4tbLEr7l04Q7X66uk5nZzekxn5sheyyFFJicEeAEcCesP0UJzfR6sRZ48iGTgzmEtYM4KAvy2Rvjrk3d-2OuennnfuJ2vvc_92ulpe_ZuKpqMWUqL3ZZhDCwf9eXgrGnqb_hsRTZXnriLMuZi_9tPbuvljo-iRI59C5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
این جانفدا‌ها چجوری میتونن به دولت کمک کنن؟
پزشکیان:
ما باید کاری بکنیم که چرخ کارخونه‌ها بچرخه. برای این کار باید مصرف گازمون رو کنترل کنیم، بنزین رو کنترل کنیم. با همون حمل و نقل عمومی بیاییم بالا تا بتونیم دشمن رو ناامید کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71834" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71830">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=nLwAqQo1ChNO-_bYKa8EFaCToV9b53t8FrvjWzseVPwxA3L3Fad1E4FS74AsmUWMrquSw6-BB4fBQlZtMvFlz_JEUFJyxJfwAeB9qGVcTfDbuFMar0B7vnMSYCD9SokV6RwWnBecCEgac-g_cs4KAtG_et4AKEVwnG6cBJto0iLhhgiHaVLz_yS4HkLSmGa1sl2V8b1uqIWG6qgS6fqiYgzEw8FQMeyzJ9aFZSMjnXS5TEMb8dum9_j4rZ_V3LRMmEEHuuyZiY3bLHsQtSgoE2par5c74YUANBWB3DoY2OvRslezGSbQshs4aHFMwwsVYnEkZ64XLd_DqG8N3HMMHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=nLwAqQo1ChNO-_bYKa8EFaCToV9b53t8FrvjWzseVPwxA3L3Fad1E4FS74AsmUWMrquSw6-BB4fBQlZtMvFlz_JEUFJyxJfwAeB9qGVcTfDbuFMar0B7vnMSYCD9SokV6RwWnBecCEgac-g_cs4KAtG_et4AKEVwnG6cBJto0iLhhgiHaVLz_yS4HkLSmGa1sl2V8b1uqIWG6qgS6fqiYgzEw8FQMeyzJ9aFZSMjnXS5TEMb8dum9_j4rZ_V3LRMmEEHuuyZiY3bLHsQtSgoE2par5c74YUANBWB3DoY2OvRslezGSbQshs4aHFMwwsVYnEkZ64XLd_DqG8N3HMMHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسجدی در شهر کوهات، واقع در ایالت خیبر پختونخوا پاکستان، هدف حمله یک بمب‌گذار انتحاری قرار گرفت که در پی آن بیش از ۱۰ نفر کشته و بیش از ۹ تن دیگر زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71830" target="_blank">📅 17:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71829">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دقایقی قبل صدای دو انفجار از سمت تنگه‌هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71829" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71827">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ارتش اسرائیل روز پنج‌شنبه اعلام کرد که نیروی دریایی اسرائیل و یونان دو هفته پیش یک رزمایش دریایی مشترک در دریای مدیترانه برگزار کردند.
این رزمایش با مشارکت دو ناو موشک‌انداز اسرائیلی و دو ناوچه یونانی انجام شد و بر تقویت هماهنگی عملیاتی میان نیروهای دریایی دو کشور تمرکز داشت.
شناورهای حاضر در این رزمایش، سناریوهای متعددی از جمله اجرای پروتکل‌های اضطراری و همچنین شناسایی و مقابله با تهدیدات دریایی را تمرین کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71827" target="_blank">📅 17:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71826">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=gUqxbFSdI_wVe7_MKl7ARAzk26QCUgEUxwftMym5zSmEuYhPfViEMfAS2Xeruc4pI2thGn5ZE9lC9D8admf0LH94jHNeBKS7NZCrzKRD-qzvjc3c_Qzk-jmkIZhsbTERZMM5WCFjxEY4lIYhkRlXqjA5kEqQDjQ83tdEKx_OPcA2MB7OmPnVxZ21l37JchsMApy8pOH0BlN1vxcT1KAzEHNmzufgv8kXfWvU20zHPc1oMC6dmeZVuyPkyzo36VeZ17monZBUuZZ5x4F--YQ68zQjwPKneq-fiCN17rewV21dy90tZ8NfnGh94zV-t3_J7KzyL6n1hwq_ElwkXUWXHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=gUqxbFSdI_wVe7_MKl7ARAzk26QCUgEUxwftMym5zSmEuYhPfViEMfAS2Xeruc4pI2thGn5ZE9lC9D8admf0LH94jHNeBKS7NZCrzKRD-qzvjc3c_Qzk-jmkIZhsbTERZMM5WCFjxEY4lIYhkRlXqjA5kEqQDjQ83tdEKx_OPcA2MB7OmPnVxZ21l37JchsMApy8pOH0BlN1vxcT1KAzEHNmzufgv8kXfWvU20zHPc1oMC6dmeZVuyPkyzo36VeZ17monZBUuZZ5x4F--YQ68zQjwPKneq-fiCN17rewV21dy90tZ8NfnGh94zV-t3_J7KzyL6n1hwq_ElwkXUWXHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند‌روز قبل حدود هزاران تریان که عمدتا سگ، گرگ، گربه، شغال و روباه بودن روبه روی پارلمان آلمان در شهر برلین تجمع کردن و خواستار به رسمیت شناختن حقوق جامعه تریان ها به عنوان شهروند عادی شدند
به آدم هایی که رفتارشون مثل گرگ، گربه، سگ و ... هست تریان می‌گن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71826" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71825">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=d-tx6t548okP1pwM6ixtAsUeJR-BJoZz_i-__7FyIWZOp5k8pEzaXYFL5tZtRP-ZOk306-sgND0neBy0GREXo3f0oMfhMh3NkkgzIoRUnAMTKI--8bKjCxiqccTx5Z3P0G35sYMPE2zs-cw1vaPjsLMO39d4yhINp0A-dYKrJI2r5N_Lxyf9QvlcR76i1UYci516UM-g0mA8cwAIh3kpdTli7vhojLMLEen5xpEwnWQN8qUqasc2gRxfY2_s_SBjQ5IyaqU-hfHw6IyNsClTQi_fH2zewQuODg2QzcDxLgsbXvZaSY5teahG8yW5_1sSRveT_mqqai1v1GkaUr8s-Y2--caC_ttQU-uYXHPiwj9CoxEzGSxqhqXNEdfQYuN_QSyqgVf2byU6yutLAO4UNnXVVNOYhOEebn56zEIBVX5iO0rc7KDOpyj_PidATq7kHFC81Tx-cOEfFYicCU4ze4EhUz3KEzvu60sr8ZtNPP37hvnpjNnjh1gD7WLGU0BwXDl61gwYaNEsbspjw7Ta3vFOUc8iQd3QH4BuEq831QGhLfP_gD2Z33td7RFvtqTnvYu0w74syJGFztC_sGtt6E7x0ZvBQVysVKS27cDDUKp_s8B88VK125dIiJNw2oPsK65BmNpATuHL4pueBBA7R_VTBGrX6_cXYZGrGBPYE7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=d-tx6t548okP1pwM6ixtAsUeJR-BJoZz_i-__7FyIWZOp5k8pEzaXYFL5tZtRP-ZOk306-sgND0neBy0GREXo3f0oMfhMh3NkkgzIoRUnAMTKI--8bKjCxiqccTx5Z3P0G35sYMPE2zs-cw1vaPjsLMO39d4yhINp0A-dYKrJI2r5N_Lxyf9QvlcR76i1UYci516UM-g0mA8cwAIh3kpdTli7vhojLMLEen5xpEwnWQN8qUqasc2gRxfY2_s_SBjQ5IyaqU-hfHw6IyNsClTQi_fH2zewQuODg2QzcDxLgsbXvZaSY5teahG8yW5_1sSRveT_mqqai1v1GkaUr8s-Y2--caC_ttQU-uYXHPiwj9CoxEzGSxqhqXNEdfQYuN_QSyqgVf2byU6yutLAO4UNnXVVNOYhOEebn56zEIBVX5iO0rc7KDOpyj_PidATq7kHFC81Tx-cOEfFYicCU4ze4EhUz3KEzvu60sr8ZtNPP37hvnpjNnjh1gD7WLGU0BwXDl61gwYaNEsbspjw7Ta3vFOUc8iQd3QH4BuEq831QGhLfP_gD2Z33td7RFvtqTnvYu0w74syJGFztC_sGtt6E7x0ZvBQVysVKS27cDDUKp_s8B88VK125dIiJNw2oPsK65BmNpATuHL4pueBBA7R_VTBGrX6_cXYZGrGBPYE7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه:
تنگه هرمز عملاً مسدود باقی مانده و هیچ توافقی برای بازگشایی آن وجود ندارد.
در واقع، وضعیت تردد نسبت به چند هفته پیش بدتر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71825" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71824">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=DzBkJ1MdlqM6WgW6Z7RhfKNb93sABoxwCamA2XVMl1kSoktuzPItY9Wis_qMSo0lAA6del7UyAArUXxK2cqI3eZ8KYnkzS3MwCXh_WPu4RjriSpP0FN5MOE0r0N8l-GQnt3netUCtoN5sHPeRW4Uk-eFCOWa9qckNdbaj7PG3CFbKx8E-54xkXuoOC3znITvWwcJzwfVkP0JC_sgR-2MmNEPioB-QXRD4frw0m_PerUuNpfchVNUr6VM3gsd4pz7t6HlY45JnaUpOCFWy_81azWZCjUd3sx6cEma5ih-iOvY94ETdERulTffBvp-nJhHegbXL-UeEb62QLBolpk_FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=DzBkJ1MdlqM6WgW6Z7RhfKNb93sABoxwCamA2XVMl1kSoktuzPItY9Wis_qMSo0lAA6del7UyAArUXxK2cqI3eZ8KYnkzS3MwCXh_WPu4RjriSpP0FN5MOE0r0N8l-GQnt3netUCtoN5sHPeRW4Uk-eFCOWa9qckNdbaj7PG3CFbKx8E-54xkXuoOC3znITvWwcJzwfVkP0JC_sgR-2MmNEPioB-QXRD4frw0m_PerUuNpfchVNUr6VM3gsd4pz7t6HlY45JnaUpOCFWy_81azWZCjUd3sx6cEma5ih-iOvY94ETdERulTffBvp-nJhHegbXL-UeEb62QLBolpk_FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین گورکا، مسئول ارشد مبارزه با تروریسم در کاخ سفید:
قیمت بنزین برایم اهمیتی ندارد، چرا که وقتی پیروز شویم — که به‌زودی هم خواهد بود — قیمت بنزین ارزان خواهد شد.
مسئله، انتخابات میان‌دوره‌ای نیست؛ مسئله، نابود کردن کسانی است که قصد کشتن آمریکایی‌ها را دارند.
اگر فکر می‌کنید این موضوع اهمیت کمتری نسبت به قیمت بنزین دارد، شما آمریکایی نیستید. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71824" target="_blank">📅 15:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71823">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=TbrKEkTSORC_5zd82sU2D5lzP2OZPAoeK7FY6Xg3MANMNAIjt_rKQqV-ObW5HLvavPW8Y9noBH0bohLXnfEcnOAxVL_w3u3T65M4SlAGaVzh38S6Ilg9gHZtnOBB82GZt6YVHcsT49-TQfZqHqvlAvqWKlxa08fJQF5Npkj1EnLZQZo6chTwn6a-WXk3ByN6vsJVE4Ql9Efuf6RbtIyW92xrmXLpu1farDUcpNwJpsGpsrmz3ffcedXwUwRGmucVFSel_69EQDUDnd5jHKZxTlQj5QsjtT4mi0eTtJ6WAU6Pt-W2tX7o2BqoU_1716AcM2fbooFYf_BHnb1l30xC0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=TbrKEkTSORC_5zd82sU2D5lzP2OZPAoeK7FY6Xg3MANMNAIjt_rKQqV-ObW5HLvavPW8Y9noBH0bohLXnfEcnOAxVL_w3u3T65M4SlAGaVzh38S6Ilg9gHZtnOBB82GZt6YVHcsT49-TQfZqHqvlAvqWKlxa08fJQF5Npkj1EnLZQZo6chTwn6a-WXk3ByN6vsJVE4Ql9Efuf6RbtIyW92xrmXLpu1farDUcpNwJpsGpsrmz3ffcedXwUwRGmucVFSel_69EQDUDnd5jHKZxTlQj5QsjtT4mi0eTtJ6WAU6Pt-W2tX7o2BqoU_1716AcM2fbooFYf_BHnb1l30xC0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه:
از مشمولان غایب تقاضا داریم بیان خدمت ، هر ارگانی خودشون دوست داشته باشن پذیرششون ‌میکنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71823" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71822">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=ZAjn8r79v7yNO-kxjn3LXryr8oS7bGa-K-DeeiUM2Hmez0gFJGb_QDh_b4WFMa_7jI-3KxEqFH0sm2Myp0uVJBDPviOtlRB7XcN8XFMU8FCLaO85dWfF8tFsqbRAhBDgaLsm4Nm6egCuADcBBGn73NkBiU0JKs4l7M7iB5JWUdtHuJL9arOvWxz4BgRP_0nappNFXkp3XVyVS45UbDyMmfLoGrIS9PWYiPiAZwa5SZyr_Ngu5u-lvUVubgNT7YG8cveauHEvAC0vBl4mov7CSvtq1lOaYhBppbSJAX9nlZiyh78VE3PwiVbQ3edvMSJ7rja9q9QN3LjRNfCypIdhpoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=ZAjn8r79v7yNO-kxjn3LXryr8oS7bGa-K-DeeiUM2Hmez0gFJGb_QDh_b4WFMa_7jI-3KxEqFH0sm2Myp0uVJBDPviOtlRB7XcN8XFMU8FCLaO85dWfF8tFsqbRAhBDgaLsm4Nm6egCuADcBBGn73NkBiU0JKs4l7M7iB5JWUdtHuJL9arOvWxz4BgRP_0nappNFXkp3XVyVS45UbDyMmfLoGrIS9PWYiPiAZwa5SZyr_Ngu5u-lvUVubgNT7YG8cveauHEvAC0vBl4mov7CSvtq1lOaYhBppbSJAX9nlZiyh78VE3PwiVbQ3edvMSJ7rja9q9QN3LjRNfCypIdhpoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرسه لاکچری؛ شهریه سالی ۳۰۰ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71822" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71819">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=e7b_yRxTGV0vzQ81rtXdkzgdg4yytSgy22DVV49oMvVzl1bSjxZxidEnUnhQfwb1UuyGMD26WnF85PBDzJ47P4d2rDBI1bPW86HBYCRjpC3b7tQAe3b7tVLW5qNI9TCMnzu0BVg5BF6eqeptKrCk3a7iu01OzcpXpwXbPhUy51zOz5vDG2J6tgpXTbx-daPer3LRjscKDFT0s5INj7RU7kj8mZwMyq0Fwev2vwLebvLwAqr5YphdHmROyv3zsQGewevxDYuzhJg3ZjKxNTN30s3P-7NSn_ZQKDrZffhfYq_wZrZIbJIEZVmOUZp_nJrQ-vG6nyj9pBTAt1dMLumZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=e7b_yRxTGV0vzQ81rtXdkzgdg4yytSgy22DVV49oMvVzl1bSjxZxidEnUnhQfwb1UuyGMD26WnF85PBDzJ47P4d2rDBI1bPW86HBYCRjpC3b7tQAe3b7tVLW5qNI9TCMnzu0BVg5BF6eqeptKrCk3a7iu01OzcpXpwXbPhUy51zOz5vDG2J6tgpXTbx-daPer3LRjscKDFT0s5INj7RU7kj8mZwMyq0Fwev2vwLebvLwAqr5YphdHmROyv3zsQGewevxDYuzhJg3ZjKxNTN30s3P-7NSn_ZQKDrZffhfYq_wZrZIbJIEZVmOUZp_nJrQ-vG6nyj9pBTAt1dMLumZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای فروشندگان نفت را لو داد!
از داماد سخنگوی پایداری‌ها تا خانواده شمخانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71819" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71817">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=jzc1dA1bFyAyFNE10qiI51-GtGRm8-v3dS5DBxcRgKqdGwLhnuhlV5keNWheoyTPNPS7svaC_JleUayI5SyICRaPOVSPjsW5B3DolHqtVECWgwF5uTujCt3KOKnJx0jM4dGS24wwAcfMWGRKdpM2VxftEewzwEDu9eazTjTOV9xHijXDFxppvCd0UW7SndCwaZkva8x8mhCMYS4bbheRy7UPpSWb3ljn4XoxrLyDdk97_LQvp7nf5m_ukA2eaJd14QXattTqvbP74xPM7mNrKQCyTsFjxkEGcKf0Y9vXotU6vZJ2y9UXmU1orq9WCW5Y3wNAv6O4vFNvB1JGftQdgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=jzc1dA1bFyAyFNE10qiI51-GtGRm8-v3dS5DBxcRgKqdGwLhnuhlV5keNWheoyTPNPS7svaC_JleUayI5SyICRaPOVSPjsW5B3DolHqtVECWgwF5uTujCt3KOKnJx0jM4dGS24wwAcfMWGRKdpM2VxftEewzwEDu9eazTjTOV9xHijXDFxppvCd0UW7SndCwaZkva8x8mhCMYS4bbheRy7UPpSWb3ljn4XoxrLyDdk97_LQvp7nf5m_ukA2eaJd14QXattTqvbP74xPM7mNrKQCyTsFjxkEGcKf0Y9vXotU6vZJ2y9UXmU1orq9WCW5Y3wNAv6O4vFNvB1JGftQdgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هزاران نفر در رژه «جانفدا» در تهران شرکت کردند و از میدان امام حسین تا میدان انقلاب راهپیمایی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71817" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71816">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=eluIWFSP9G4Mln1XMmu2Vnh8XBHJxUfWXsdwrPEmutV8_y8lemuk4TUmpWW3H6gvtEGRbpQRSZ9j6OKTjUYbwRhQ6i_U98r5Vxm4WP7PQrsJkhRxkgDrpSW9QuZ2zM2rxw85vhq5jtJ_LWpCFZDJSO9WVTWSPBApmcbgVjJU6qgWXw4saUqbXO7cHmDiCXqOPLDsYcjGXElH7ZQR-uts9vOP12JwYiZXJOMntc2M7KkRAl5vnSEo0hHp6QMtasffTTbI8L2mA3sKx2ucOfOSw55_rN2CTVpDUIKt-otGhaltTzGo_pU_UsS6R5JEXAAFHfli2dza-8jXnsqOwGkrHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=eluIWFSP9G4Mln1XMmu2Vnh8XBHJxUfWXsdwrPEmutV8_y8lemuk4TUmpWW3H6gvtEGRbpQRSZ9j6OKTjUYbwRhQ6i_U98r5Vxm4WP7PQrsJkhRxkgDrpSW9QuZ2zM2rxw85vhq5jtJ_LWpCFZDJSO9WVTWSPBApmcbgVjJU6qgWXw4saUqbXO7cHmDiCXqOPLDsYcjGXElH7ZQR-uts9vOP12JwYiZXJOMntc2M7KkRAl5vnSEo0hHp6QMtasffTTbI8L2mA3sKx2ucOfOSw55_rN2CTVpDUIKt-otGhaltTzGo_pU_UsS6R5JEXAAFHfli2dza-8jXnsqOwGkrHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین شوخی پسرا
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71816" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
