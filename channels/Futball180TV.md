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
<img src="https://cdn5.telesco.pe/file/P2ymGHLTTkdP_Bi-MM9NL9MDiT5EHM2bwmhdYCkHi1VH-DXdnrojM9IKr4N0J9mcNRxNVkqCwxO77hn2X451mj735ZS9uA_FXYZhBDm2I3InKo6Kb4jOUk9lv-dfkV5FpqH0TftS6vJc-MSn1tDSjdFbm0_-h-DAgJpVwcUbzb7YYj0zs0XoNvabOt4qcDl9lHWVxsX2MLSvMuELz1iSQcgXGtbz2iDt-8Z4wr8OGKgmXlPEyAf71JbLyZjTjm5rMWB8Y2e6MQj-Yv7kS2ORvRcQyJJ4kAdl3c0q6NiwAD56Qj_-4OE5sbtyf0hbQZ4leu9V-Kv083BSrsmO3qqRog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 356K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 22:11:38</div>
<hr>

<div class="tg-post" id="msg-92121">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15e74f9b5.mp4?token=Z6qRgH2ycjnMoeLcKXROliBai2KAKJpvs0OZrT2E3TyTyrEmT2E51Km7Jo3Zb7pnsJZLUp_OLnrj34cIiGu_YiT4CcYALx96W3jy-_kYXXY-hxynisg4L8twoVtA2kUhtUcotph6rTZ4IE-3z1ENW5psgLcheVaSrObOXOXmBEXq1ftylgI3laVLjFzCJb8HSUtFv3bvX7Tqs277So3groZFLURql_mXKbLGANm2ZU_EXVeTwMMx-g7mwwryS3PHXEOzU5qfzhi5uXeTavzjut_YWzZQs1Tf0Q655Qc3fGK7AdpUl9NIYRM3SKc1otwkKQtpybplBpJZhrE3FoCRPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15e74f9b5.mp4?token=Z6qRgH2ycjnMoeLcKXROliBai2KAKJpvs0OZrT2E3TyTyrEmT2E51Km7Jo3Zb7pnsJZLUp_OLnrj34cIiGu_YiT4CcYALx96W3jy-_kYXXY-hxynisg4L8twoVtA2kUhtUcotph6rTZ4IE-3z1ENW5psgLcheVaSrObOXOXmBEXq1ftylgI3laVLjFzCJb8HSUtFv3bvX7Tqs277So3groZFLURql_mXKbLGANm2ZU_EXVeTwMMx-g7mwwryS3PHXEOzU5qfzhi5uXeTavzjut_YWzZQs1Tf0Q655Qc3fGK7AdpUl9NIYRM3SKc1otwkKQtpybplBpJZhrE3FoCRPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فردوسی‌پور و نکونام نشستن دور هم راجب خوشگلی دیبالا حرف میزنن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/92121" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92120">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
معرفی تیم ملی جمهوری اسلامی در مراسم افتتاحیه جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/92120" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92119">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4c66d54ee.mp4?token=bpBOa6fWUeVwSjtPech7LK6ms-R3mLJUNDKljDlJd067cIQnNZo1CC1tV6Q1PCRBwDrpiT9Bk6jb0xgkId9JpdQZC2DulaLyMG7G-6PHfiAGIaf1xB2PILPWqHs-rbyZXk7wa_YllOr4UOJfTuIgaLUrD33c76suPx0NrdxAKlh1dd3clrGHGlrOZpUcalU3IO8gAXVOqAqft65T9mM_epmHPaWb_n0o6tBxtDw5JST23e5UPjEJ79oviw81-1xclFWG8W8Rx6XjpS-b4KE1kZ34s9a_hw2elDzT-m1edp2KSvwDZ6xt27OeW1WWyg33YBjq75cMwgvnjk58939Svw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4c66d54ee.mp4?token=bpBOa6fWUeVwSjtPech7LK6ms-R3mLJUNDKljDlJd067cIQnNZo1CC1tV6Q1PCRBwDrpiT9Bk6jb0xgkId9JpdQZC2DulaLyMG7G-6PHfiAGIaf1xB2PILPWqHs-rbyZXk7wa_YllOr4UOJfTuIgaLUrD33c76suPx0NrdxAKlh1dd3clrGHGlrOZpUcalU3IO8gAXVOqAqft65T9mM_epmHPaWb_n0o6tBxtDw5JST23e5UPjEJ79oviw81-1xclFWG8W8Rx6XjpS-b4KE1kZ34s9a_hw2elDzT-m1edp2KSvwDZ6xt27OeW1WWyg33YBjq75cMwgvnjk58939Svw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لبوبو تو مراسم افتتاحیه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/92119" target="_blank">📅 22:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92118">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjGdXuNK5H-AFYHmN41UxcB5frHZOC2VDVl81UYOF_etwGxOWHUOigvAXUui4Bk-j0Zu_Chrr10yJqnhndpDhf0WCKVVc5vDAAQ6vCMaCACUuMWKaZce-FCXhcSvFzL236vRxqJ98z-FT7ehFZF34ZEg9k8PjAXw7buya5RevDbVe7K3vuxyyCPgDJbngo7K0XvVJd4DiW6QT_U9PXOovMGPhLCJHkuISlEODf9IKApbZWNKP9J0IaDeDRM-Hqi7Ep7MF6SsqQPChlvhJZo1YjQeVfY2a0UrJcveDIq_lKxRoO-e-3hKINyOixz_s-DHf20eqDBGxqaWJ8jfaQS_ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا 30,000 تتر جایزه ببر
🎁
💸
فقط با
پیش‌پینی
بازی‌های جام جهانی در
صرافی‌بیت‌پین
😍
بزن رو لینک و شروع کن</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/92118" target="_blank">📅 22:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92117">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIRMHXIgyGKhlFiZQuKnuUXyDH3aGEPLvCip3nbQ0ynQTdwoip14nzNoeCxOTA4Svz0BckypQ4-m29nHG67G8kFeZWITDDP3XVeExxpOdrbgiLL4E7RM1tmmB58j_b6eAel6At59xiNpMU_7ZslgkqkwdIbYb81as19-e-WX7wCZl-QxrowXrDpDWPge1xNkYD0EH_uv5RbVWnI-VVdJ3H_jz-iDYBhIgXcLSstnbk42Z0wmP4qU1pVRp6BuEfMMpoCviGPQYnNvt6Q6BZKlkI9C2mQrwLCgxN7Wvz4LIqs0R9OXL80PVM_KAF-_8f9P-OwkrIVxKPUh55AGApFQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیانو اینفانتینو:
بیایید واقع‌بین باشیم، بهترین کشوری که تاکنون میزبان جام جهانی بوده است، کشور قطر است.
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/92117" target="_blank">📅 22:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92116">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c616b3432.mp4?token=jexJbZ_-PRnhXfZib9JrRn7ydrNC6o5IjY4yhxYLA9_2x80SizHPinuKmsUe30AJGQb1qN3ZYzKPX0M71eANhXfB-DPR1kr7S_RL2U6_mQu3b2xJ-S5iQ6bD4j0huSbEIWRqACuj6Zf3j_poxlEH0cV3W5mA9Gh_Vi7WWvy2AO5-oTi2rSR0vw_XGpN0tx7Ojabi20bi3sVWSq3L4JXc1r2-suF9gxTU-8o9Z7eX_BAb4nHAs1gB0qwOugOq0FJqtzBBX10DvLhk2dG2kBNJ8jBQ7t3lWNwpT-ItRs8diTcc_hBhAUul1nIW-NJxqyuasdH0a7SM8BCx0cUJRoHxAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c616b3432.mp4?token=jexJbZ_-PRnhXfZib9JrRn7ydrNC6o5IjY4yhxYLA9_2x80SizHPinuKmsUe30AJGQb1qN3ZYzKPX0M71eANhXfB-DPR1kr7S_RL2U6_mQu3b2xJ-S5iQ6bD4j0huSbEIWRqACuj6Zf3j_poxlEH0cV3W5mA9Gh_Vi7WWvy2AO5-oTi2rSR0vw_XGpN0tx7Ojabi20bi3sVWSq3L4JXc1r2-suF9gxTU-8o9Z7eX_BAb4nHAs1gB0qwOugOq0FJqtzBBX10DvLhk2dG2kBNJ8jBQ7t3lWNwpT-ItRs8diTcc_hBhAUul1nIW-NJxqyuasdH0a7SM8BCx0cUJRoHxAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
🎙
نکونام:
🔵
سال دوم تیم من را خیلی اذیت کردند و نگذاشتند کار کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/92116" target="_blank">📅 21:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92115">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0d67b4e7.mp4?token=m8hqU88Tvq1VMD0Db-DIdrB48SdWA6S1LQC9EqDJDS1jsCd6XEn3KxTk3kxMcIrl7GKiQtS6_XWWn1FvJd86Kubzfe1nUHZvL5x4-iiQtDttS_Gb4At3u9pV1ZNP_FB2VXL5L_iLcOEtaz_KTYf18CQLuf5WEYvb59qxi_nuz9hVQ8b_dPbest0RI2rpVSKBYqY9N8Uj44T7x3d6KACEiS42r0JLJp5Oj4Qh_0Tv-W6OeUmhQOb7ZSib7R1ztRtZBTIoFNc1uOR_LH3Bm70_lCeEZswwd-0i1H1Gg8PfEQRqh1-fjSWjTE4AFlXvIDcnXd9RuedZnP3F2uzrlt0i5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0d67b4e7.mp4?token=m8hqU88Tvq1VMD0Db-DIdrB48SdWA6S1LQC9EqDJDS1jsCd6XEn3KxTk3kxMcIrl7GKiQtS6_XWWn1FvJd86Kubzfe1nUHZvL5x4-iiQtDttS_Gb4At3u9pV1ZNP_FB2VXL5L_iLcOEtaz_KTYf18CQLuf5WEYvb59qxi_nuz9hVQ8b_dPbest0RI2rpVSKBYqY9N8Uj44T7x3d6KACEiS42r0JLJp5Oj4Qh_0Tv-W6OeUmhQOb7ZSib7R1ztRtZBTIoFNc1uOR_LH3Bm70_lCeEZswwd-0i1H1Gg8PfEQRqh1-fjSWjTE4AFlXvIDcnXd9RuedZnP3F2uzrlt0i5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استادیوم پشم ریزون مرسدس بنز توی شهر آتلانتای آمریکا که قراره میزبان بازی های جام جهانی باشه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/92115" target="_blank">📅 21:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92114">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFIoFLs4DDlKMKb89rKAhaAVtLmeAA8YgBdSVS0g-ld-D_wpYSxcCCqzRV6jbJ5Ax7fl9sGTk3Vwww2jbUABxhXt9U0zPN4O_RiY25zGs_OLGLJmup9F0w2Esnq7BzMqPCkuevw3WpBNegpD8JmgntEJs9-9Pl1Ud52LIPRlDoJQpdRIAmea7YL2jywsLzITqBGOR4TBi-eMZY2Ye9i27r28XLb87YfFFqOadqIV_bT9ppx1jRAA9R2-hKqLY2L2DevF3vbC5mkNeOYbGxO7XtPYnzqx3Nd1Lvr-m_V-l3i21R6KlLZeJrKVaq3iDZ7emNgOH4rs1N85o-UachlTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
اجرای دقایقی‌پیش شکیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92114" target="_blank">📅 21:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92113">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz5AAPaJE2c0U3mwLAr1YYqLPxYAna6ynUEwkOjsy5cCXa7LdYH0bXclLddnM13HZp8GBbzpS46k0xj1l0puzpNopprJMUW64iHTUeuT9mFYvsc6PjH64IThT0TDbaXti3XqE9AZSrYyuO7HvHC6LdwRNceQxJ0Zpz75Xuz7jiMvpv8Qwb3_jIRpa383lOjM4yP9YS17IrY6f3ykIraMGvBu2Akq3Dc4iUnRXGqMXc92C8W5tgoV51dEChdPS-nEUUkOL4tE-QcZ9ZCT9iM_NlpHDK6RUkXRJK7GGyvGOHecj3qc8inkxw5hcBSMlPUyHMz_AphnfD8Rxh1WiUipUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی
و رسمی:
⚪️
آقای خاص رسما سرمربی رئال مادرید شد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92113" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
‼️
خبرنگار نیویورک پست:
ترامپ همین الان به من گفت که توافق با ایران کاملاً نهایی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92112" target="_blank">📅 21:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92111">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">من خودم زن رونالدوعم ولی الان واقعا دیگه بحث بحث وطنه باید از آرژانتین رونمایی کنم :   @sammfoott</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92111" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92110">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/093643fe1d.mp4?token=Mbhqof97rpe54c_I7p1jnLbh1cBTMi7iTvQ9ikZw8GHecMUcVNzrwUnVzbh7XeWzft8FbCGCwftuPlMJD3jsmXcZ7oobdMHpaDfRLR29_KEstnVbEfwFoF3rPIl7bphpqZdc9curD6XkqWXqVohjC7tTjRdppnXmt6btyHP0eS7dG1a7IAF9avoB3VnUoqPqCIGl5Toofa2KDugV3zEhkAVAn2uoOLfKX7GBhYeQAPnbSy-Y5qZ6PgSIZ4yfqA_d7a5SY1erd94b_1m0gQNG4hfWdgO9Y8wwuqXSzKPLS7V4NoTS_DlfsoRd8v8I5lxW5tZ9wZcamCEryMJyW4ulszbd6cEG2zEn0y6im1SbzG6tPK1uka2iEF2K65LJ9NJOynp1mmMX-BBsXzaaY8GWQ_S-0r5Va7cbVuyApRmsbGhP1vde4enXq2hdP_e1gbAL1fGp97m5U_LLLKS0GVd3JlzFCEgihwtlv-s9Cxgp77olF8IftXQqflEXAVpggUmsHGfMoZMRhtDMr4zt9U9DjvOzraO64NDxNTFhBqNsYM92jjIa97oAvr5Y2EVWXX6ZXeb4538u8ylpcMKvy_vwkcRTGzNT_yYatkO0voq9JLq0a9-FVz08VzttDJoNIoIrCm2_dhINnqee0Bg5IoiQVj3mQiLsRXoOpJLnJH_YCL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/093643fe1d.mp4?token=Mbhqof97rpe54c_I7p1jnLbh1cBTMi7iTvQ9ikZw8GHecMUcVNzrwUnVzbh7XeWzft8FbCGCwftuPlMJD3jsmXcZ7oobdMHpaDfRLR29_KEstnVbEfwFoF3rPIl7bphpqZdc9curD6XkqWXqVohjC7tTjRdppnXmt6btyHP0eS7dG1a7IAF9avoB3VnUoqPqCIGl5Toofa2KDugV3zEhkAVAn2uoOLfKX7GBhYeQAPnbSy-Y5qZ6PgSIZ4yfqA_d7a5SY1erd94b_1m0gQNG4hfWdgO9Y8wwuqXSzKPLS7V4NoTS_DlfsoRd8v8I5lxW5tZ9wZcamCEryMJyW4ulszbd6cEG2zEn0y6im1SbzG6tPK1uka2iEF2K65LJ9NJOynp1mmMX-BBsXzaaY8GWQ_S-0r5Va7cbVuyApRmsbGhP1vde4enXq2hdP_e1gbAL1fGp97m5U_LLLKS0GVd3JlzFCEgihwtlv-s9Cxgp77olF8IftXQqflEXAVpggUmsHGfMoZMRhtDMr4zt9U9DjvOzraO64NDxNTFhBqNsYM92jjIa97oAvr5Y2EVWXX6ZXeb4538u8ylpcMKvy_vwkcRTGzNT_yYatkO0voq9JLq0a9-FVz08VzttDJoNIoIrCm2_dhINnqee0Bg5IoiQVj3mQiLsRXoOpJLnJH_YCL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🏆
اجرای دقایقی‌پیش شکیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92110" target="_blank">📅 21:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
پایان مراسم اولیه افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/92109" target="_blank">📅 21:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92107">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sjb0BqkxlOCgu4bjuNRaSW97NREA7c3UhEO02czaRYPQ8j1CzfmhZAqxMBfHIO8WvY8xj0xSz-0lbZDJlw-64hdpql3mVjKEMlXO2T71I0yb--hhv1Jlgxka-kd2r66LvXVh3IbtHbE2hr70yyn6TnSmbfSsm7B1tJZDo3MDwlJvFzL7N0GQwtA74TikwiQUcBxmoP6bdyJxbYA4rcAMZ8B8eRSu2jrpzlKil-IpT6YlVwaNGREWO-rgw-YsJKxSV9bC12PYwquk1IhYR67GfmJ4ZK_We7dLQQfhb_wZbEpQfA4gzok6gY4U1SGKHGuiNMhiGCPF2-vaDMDg9GdCjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3H1qgT4B2V1hpHUh-3bt_Ooh8RTWbZBmHnq0rpoVpmA0wNMLbhTPW3X2mX3wH2pKCF5dUv-JXfEwk4feJC10kcWzamHsR3KuhbUZFfGi5pq3dFAPFC8x8JYyDc1spIDZDS5dISbv3i0id9aMht_w5PqlIQrtsVHnlPOuprt-Nb2SrA0pS23Vfv2xEvlNIz3CcoEsPZlUEf05xXxRYR41wCKZkJSMf_UXFVYwtbl8nF14v_g9iQnb4izoR-ZL2Bp0qWZk9VKI7q9VVqR6Q_hwicpmlU7N_J0K4bl-Uw0YUlfBlsUfMGeZsORcpO_mdIgjoBh8R10J7G9DWcyr4fBUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اجرای شکیرا تموم شددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92107" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92106">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports (بدون VPN) Bein Sports (بدون VPN)  لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92106" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92105">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جام جهانی 2026 | فوتبال 180
pinned «
🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports (بدون VPN) Bein Sports (بدون VPN)  لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV
»</div>
<div class="tg-footer"><a href="https://t.me/Futball180TV/92105" target="_blank">📅 21:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92104">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🏆
🏆
بزنید افتتاحیه ببینید
🔥
🔥
Persiana Sports
(بدون VPN)
Bein Sports
(بدون VPN)
لینک های m3u8 رو با برنامه های iptv player یا mx player - pot player - vlc پخش کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92104" target="_blank">📅 21:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92103">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8XLIRtwsfx-kylrMo2eNJOBNGzt7FHAkwjfeEu4BSaL1ZKTIFoZCvgAH6DwtfGeVplSBgQgXn2rBWhbC8Bgiq7ZSQyT-MYw4nErHKZyNKDXjruDSmQ42EiGqLaGBNsk09F5SP9HMU8KXArK8yxqEj8x53coh3NUP1nJbqvPTNme6s4Wzfz-vWxZaJq3f3gsGh_c0AjN4NpR4pC-tioGgRR9kjrFVpuUlxrdNr_m1x833UbaTpcNio1p7UkKy6fYBYzTn2ttqgZzETUUVCb5E5QuEUT3Pi2yvZBCK6dFg6upO_4yxVjKMiVU9aCA-igoPDsfkgUh92DgdFuiEmJR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عادل تو لایو فوتبال 360 دیبالا رو آورده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92103" target="_blank">📅 21:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92102">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خب مراسم افتتاحیه شروع شد.
بریم برا پوشش خبرا
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92102" target="_blank">📅 21:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92101">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElFOlSkt6m23_bcUCcqRDWy4PkBLLYCy38SD5JhU2G2L7LI3n8rXQh8H8loDt48KAMVGijYjXvCFhI8h0JaYwbGUfql70nk2McthsW7Wu0ZWvm968BuXMfK9VfeHlrC8g9ko0byuU0oS-1FbpvzVQ9z3-kJl-pfEUfAeHaNlp9qT-KE7C4aG2wxOE4uSUfKWGNmoj4L5JC974wXf5HNGzAd9JZ_Rp8M-7whiNj4qrzWNYNDp6PXjw4GfMg2qUaKbv8AjF1Fjlodu6TTQa8cShGgKaaqofQuIJklge96a76VhCoh3_T42y_SQS8QIQpg4GuIr6RU8qkJKrfFAmuvFvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇲🇽
هفته‌اول مرحله‌گروهی جام‌جهانی؛ ترکیب مکزیک مقابل آفریقای‌جنوبی؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92101" target="_blank">📅 21:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92100">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJwyTPRrCFIzRNHFDBhpXDezanz6mmJ68jl0xRYwllSjb9MRnQPR6FsVjdWqoJht-L2UGgyqYznDIqjm_9pUvZ-34Fc8MUC984lsH4Cb0XhT5F6RyMY_7trTkIkZx122URko6HOE5BbYkk8iz-_RyF_9iPgjvURKr0gaWNY-5nRIXficgQM8Vw5wM4L-zBuFdRW24-zywjDk0RQCe6AU6bJMiLrReVMGvipieYMdjQhzN3QDT4fLxuT63KZ4LYdGx0OAbpkKV5YiLXaxcgVP4dLjSVHfAdfVXdwvcCTnHHv7_T9S2kZEyTXpw7rUQZ6YLF4nfBRHaqEcf9jMi6bFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇺🇸
ترامپ:
🔴
با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران رسیده و مورد تایید قرار گرفته من حملات و بمباران برنامه ریزی شده عصر امروز علیه ایران را لغو کردم.
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/92100" target="_blank">📅 21:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92099">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
🔴
🔴
ترامپ :
🔻
ایالات متحده امشب حمله بسیار شدیدی به ایران انجام خواهد داد.
🔻
در مقطعی در آینده‌ای نه‌چندان دور، ما کنترل جزیره خارک و سایر زیرساخت‌های نفتی را به دست خواهیم گرفت و تسلط کامل بر بازارهای نفت و گاز آن‌ها پیدا می‌کنیم
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/92099" target="_blank">📅 21:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92098">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dy5PXb_46Lz-GCndGsHQYwfy49KdDD1WIy3PTu9F-uVOuuXVg73NttkfCmmLWpwqvTvH6UxUhEqwVuO12g27tl8INpUkjbuefd37fDh368we1SXxM_lm2DE48NdkG2I51EgoEkZK3LHq5RUK9xyX7Ba1QLBKJ4yRAPwRhpexpPzIr9hEeBNc0hEVrf8v0CjmAsgBDlM7ldRzMaMChsU4jAOSzC-bO0cv0jiofACQ3hvP2LqkXQJSWnYoUAK2fcAppESrvPru7-nXUFdUxTfSzU3MdSc8vai9mahCwpeV8gyjmI2iY6os_elmV3WGu9DoJZbLq9xT2KQCfv_4sFOsgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسل‌ها عوض میشن، ولی فوتبال ادامه داره..
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/92098" target="_blank">📅 21:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92097">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DriTF4yT1WiHFlz1MZJiJzfmHnOQqs5Nk8LU6catpgiJv8PvNSY0bAIgV1Fkc_zSWVKw7wnKS-MhH1d4bQRgHiYxeONwX8Dfttey8QPQL6eEc73-n7xDNrQ3UTOuepMg_qkcOAN9I6iwDZBzVgrnTOIea5eRID1emqo9_SQ2QS8WcXKjY0chLxUuvpOvaO5tbis1RCNzRp0w3hD8QJ2Hzq2ku5RIn41nb3kz2R5piRKZ28SdJfvU-6svL6ozX1cq0jBCN9U6BX4sX6XIGoMsORgXXfJLcRD7cGuKgaKEcevFbab34abNsLGc9J1N7l4uelMVEhMgf1m0qR5AOzmC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور لوئیس فیگو در ورزشگاه آزتکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92097" target="_blank">📅 20:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92096">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hslnBjVQpWHTsnxR4C3M7x4ChmDbiafEwTHWeFCgESdm6Fgq7VN1AeiS3X-08ujOG9LScNob0L4CIQ1MTogvtcmUNxxmSIRzG5ZZrHu_oG3TJhTx5sWGzO0Gx75ikFSLX6DDPMtXyQIIUgAVJbuFjEPr0L5Ll2kpCfLX814BXwscw2F19wFC6mtZz0Y8xcCUB01gAEIsxkPQsvXeeyCLANc3kZ_AQLIfB4rABwtD4w_Z3dFNEC-iSQe_AspWu1U-vNK1yQXJ54H6XixpxB27xH0BXbLkrRyZCrcItTrdEe7ZPWDUqkCF0d9e4YkOvTQsBfNqUvL6w4tV2oi01Mo9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🦁
🏆
تعداد بازیکنان هر تیم لیگ‌برتری در جام جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/92096" target="_blank">📅 20:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92095">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s87v_wA5auXykoU8xm8xo8eclEvmRbLyUC_OSKI4ryQTysAWW6koa6vs5XXFjc_COT_sWMgUGH9uv7KB1OmS-lbeRG1dmbldX8fA8qWOnoqHuU3v1z9eipUVdmGBgv77CqIYicJETzcmoj3BJCJpnpzjFhQB_2CTTyBmTQ99h2VhP6BPo1XrU-rYZbLLwV843N3Fh0kFtKuILWCmM7Hz8nSp_i0l4sy2dCTUe6WYlnMRh6bbGehmQfX_73nnmfV72XxreQ0980DWndCWhvTwEEMYtpOAmt6eaeTLyG9NNmM3BoG3rJjV5JGH6RyUpSvMblhph5Rkm0blClrvmeOmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
🏆
از آغاز جام جهانی، ۴۷۱ بازیکن قهرمان شده‌اند:
‏۴۵۰ بازیکن: یک جام برده‌اند
‏۲۰ بازیکن: دو جام برده‌اند
‏یک بازیکن: سه جام برده است [پله]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/92095" target="_blank">📅 20:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92094">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0pTNSwYK-246wCIt98Cj8rCEtMbrISXO2TnGDF8kc5hqOnWgeyd9ZZZy9Otj2wvcWp0kHp9QiPgs-o7AgE-yMr0_cZFk_DkaPA4Yx_GQAHpxi_C0wwKeJGsT5Xq247tcFY6HoWWIt3QM6C4HrbqBTacJnLrH3495Ky_oESXbKJsaIJ4HJdx-V0Zuzhd6kjwg8rCaXhQSYH6j3e27JUvnia1SbIUWlHIGqEaSz7VIEQhWLgbddQTcQnXAcLwlojoLMw79IquwO7nPkBo3UuzJRQqinZc2_8tHExOJjCtOZ0GLeVh4GEQk1e4FZLy6STFDRQPH9UFeVcqwMdKqXcnUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووری؛ رومانو: اگه بزودی با خبر: برناردو سیلوا با قراردادی دوساله به رئال‌مادرید پیوست روبه‌رو شدید، اصلا تعجب نکنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92094" target="_blank">📅 20:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92093">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0941184f.mp4?token=nnuVT3S0Z4r5PTzxThU1HOCsvWLBHtA0dNbj69mVHL8SxfZbbmH_8sOv8QobqX5EVGrz7XaJ0aYCGd8PGvvtLpzJPbLSo_-XfzHk1cVfFaIKT-H8jrydcUvvzimOL2bp8X7JsNSaAyuB-Cb_tnLb-oLIEgRgGhzPqLA0avDTIwo5ndcpzGsyKBgmXapK6thZWdbSUS3z0Faz92xqlGlqWcTKByLKWh8K5bHsj8Zirxb5ecUohQ3d4w_rACr-PIsowIOjRbHA-YJZvrocXK5CcYLHaMDHUvEiLnCWWlnyqFVAm6cxVpEEnSewpQO3joptdQIfq36q_Wv3dSxnBi9b-3N6L2rhF6HDuAEQfg_5_UbYgaNwfthV1a_1EUbpUzxKYB8BbXlAmKbRtbX8JRnuWJmWgL7sCPnoQUW9c0wIdaDdgznAwjege_7s6Y309-UqmZjXW1WWOq4DrLWL5mvUTC6v6S72lvEtyHEK0ZzJiVczNRgKjIlKWLGiREJOOG59FTNrQGUxRep-gCWj2SiQGQh8Xx29uk9KwvcOX_SPXNwcoTOzuZzLA1ORJg4zwhKGyjJSc4Iu42rCaJ6iiYUiqcIs2npJlnGFiNL_nbTfuZ16fRvKXqKgYTNadPW3rhKUwEwuoa7UCXU21DU3aTXFLGUBjAEeh-2sVStE_rPP0SM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0941184f.mp4?token=nnuVT3S0Z4r5PTzxThU1HOCsvWLBHtA0dNbj69mVHL8SxfZbbmH_8sOv8QobqX5EVGrz7XaJ0aYCGd8PGvvtLpzJPbLSo_-XfzHk1cVfFaIKT-H8jrydcUvvzimOL2bp8X7JsNSaAyuB-Cb_tnLb-oLIEgRgGhzPqLA0avDTIwo5ndcpzGsyKBgmXapK6thZWdbSUS3z0Faz92xqlGlqWcTKByLKWh8K5bHsj8Zirxb5ecUohQ3d4w_rACr-PIsowIOjRbHA-YJZvrocXK5CcYLHaMDHUvEiLnCWWlnyqFVAm6cxVpEEnSewpQO3joptdQIfq36q_Wv3dSxnBi9b-3N6L2rhF6HDuAEQfg_5_UbYgaNwfthV1a_1EUbpUzxKYB8BbXlAmKbRtbX8JRnuWJmWgL7sCPnoQUW9c0wIdaDdgznAwjege_7s6Y309-UqmZjXW1WWOq4DrLWL5mvUTC6v6S72lvEtyHEK0ZzJiVczNRgKjIlKWLGiREJOOG59FTNrQGUxRep-gCWj2SiQGQh8Xx29uk9KwvcOX_SPXNwcoTOzuZzLA1ORJg4zwhKGyjJSc4Iu42rCaJ6iiYUiqcIs2npJlnGFiNL_nbTfuZ16fRvKXqKgYTNadPW3rhKUwEwuoa7UCXU21DU3aTXFLGUBjAEeh-2sVStE_rPP0SM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇿🇦
تیم ملی آفریقای جنوبی اینجوری وارد استادیوم محل بازیشون شد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/92093" target="_blank">📅 20:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92092">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGmOHntLXjoelPjjzzb2O3jNYhGQWeLL7lEUdNv4wiLwhUrWOFqIgHL8ReAfMUT06awp1YPGozuiwF3QdZQXev0gUtYhBfKGXRqWFQfVVvvycdy4EPA7sBbP3CcGYdsL2JVEtPWbyjb0vVmophrU-dJZWVKrzwma14PBE_um0t3zH0aT1A03ks0QO45da4U4t7zhbMhIWiVACAEiO2NAkm9JmAatuuQGc2guJg78N2QpYnI9-xw6tvSL7uek38rzh94DLfvr3-uq8LP6XVApxvu3suNXHfdQWk7vO5poGUfTk76Pj49WxscORkLYQF2_iMntjJxLiSAKOZvuQ7QdKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
💥
🏆
روبرتو کارلوس: به لیونل‌مسی توصیه میکنم در جام‌جهانی 2030 حضور داشته باشه. مسی به‌خوبی از خودش مراقبت میکنه و اگه خودش بخواد امکان این اتفاق وجود داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92092" target="_blank">📅 20:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92091">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJCK1Lb9wk2fGtbdbiOxWhUdjIAuabBATsTDmb2ZpSVJIXRj0Myjyc-1GSGjZcs8XO7weYqhsJgial2WOWJ0lApL3PUg-13pZnxFY70czWNnps3tWM_PmT3CbcuMzoeCWXwnFDYv0sS3x7k3EsS282IJcEN0jaKPV47yys7-2akB9jz_Qx2uGzRjwbaSuNZ8yaXEttv1Na4f9bnOrLNYNJrXe1nmmwyY6W1WZUsEx1oByc0CnMYdO3WwnYAAlylqv5fOFiHKP-8fep5vao4_7ftpW0LPbAcvLAJ7Af0bk4yLEGKQ_dMEAj1bs6gwU8IsbbKDAYu2bK7rETiU9FC6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔥
خبر خوش برای طرفدارای میلان: یایسله این هفته با مدیرای میلان جلسه داره و احتمال اینکه سرمربی میلان بشه شدیدا زیاده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92091" target="_blank">📅 20:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92090">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی از رومانو:
⚪️
رئال مادرید رسما پیشنهاد خودشو برای جذب برناردو سیلوا ارسال کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/92090" target="_blank">📅 20:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92089">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCb7hkXB_NJbEu7naS5ucJpg2v7C4ZcBfcGZJx-n6JTeJaxUOjJIaE2bv18sgiyxbDW4mliC0o9926_a0PQl-gWMuWXhRqxepAhYEPxAQ6p4lfRv2t9zUZia8HKg6ux3oz2qMMaSXvKi0GVhBYOv7F5vyG0Qzeu6a8PR34mCua3xJGgngnM7mMIYkW4frqpsXH_fz9VuUWa3EtTB5ilwtBCSpxOMSvc7WiebSkEexJ0nQd5JApv2nTpR2LP5roRwQ-E0SLjk__nptJCJ5LBoPbCna9LPZatDsBrpFhjhgfAwiWCEq1Nr3PRzmIirQBVQKmgqzrDhGkVpuL8ZQjWjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی از رومانو:
⚪️
رئال مادرید رسما پیشنهاد خودشو برای جذب برناردو سیلوا ارسال کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/92089" target="_blank">📅 20:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92088">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی از رومانو:
⚪️
رئال مادرید رسما پیشنهاد خودشو برای جذب برناردو سیلوا ارسال کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/92088" target="_blank">📅 20:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92087">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7WIkARadZkfYOYxpwhM7b3ARWnOu_A4OxBIZq3KgnLClIsOJuQuDOF3-iak_XrWJf0S8Zw1qUdCoiKKCd9V6h85yNLoA16oA2cNdAxx23pdvxupPC0gQAyI5uISMic91tYcVNS24wMjMtUInNSN49JQ4l1LAwv4MuIwg3uCzVV5mPV-lM9yf_nimu4dlMdVKdFV6msdEgUL3JJj57Cr3H88Azh30JMU76LF9C3LR_C9-VppDlVtQgmfwsOAqSILreAFYOOAmJLD5BU7guwhpfcfkuU_POiJn94PrVscDgs_TcErwQNC5e3VxrkY_ooeaS2uGKetqK5cMSNgjFh1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوریییی
از رومانو:
⚪️
رئال مادرید رسما پیشنهاد خودشو برای جذب برناردو سیلوا ارسال کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92087" target="_blank">📅 20:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlOTGHRh7_0n_qaET28AqMvQNURrnV1eu8jo9KES8ujhM1cmfA32_LO9S58nhwhGA_zo7uT_QCPIbxazJa5vxj7x-h1Lxaxjmc80uwrCqKqoTlo1HYSmvdD3mZJFqH-BcUECMfTLG0OwTqC_uw7CEmyY3YEla5xyQiqLXVjaqqApaijDzVfRZSRgC53OY5lF-3tzOf_gF3ePMiheEcTTQuihOhit1Qq6xuSCEwnt-mGvdswZOjZ2BVLv8zirkEvwTeSPMSv2oLtmUEvbgU16aJUKLQYlFV4WPjwRYpIt5VsnvaE645gLEQy1OuFBAys4DqsbdZxdNi5rRs6Vp8yyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOBj8-r2_tvDng3PWwKaPaEP8mYMkF2IQ4YpLsRzqnprDhGHPQlHomVM3SHtQsgvSyUgizZbk81ML3oBeGAvYiLREpuogyfkQeHra2VilMHm6cVV8ONE-rVRX82rZsJikHW0Wz4LB93ryKRJnhl4Cslw5ADCA5-j9qqVcK25q8BP363WM4n3eCfs0IcgQQZJvSnet1xmPhPJusfOir5xOEHjypZP0-oasiECs4Qx_fvDfK0W2ZaAxQ4tZ0Hom5EGTXTJvVqbR4BxRcX2isQ9efFoN1vmcV2HCds5OIn1wKcJ1Z3e4PD3GjfRoGRNZ03GZM-EcLKY7br6DOiiTr7MVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0nvHWQzNus0ybwHJg84S9M5o7b0-_pKUQZcBIDDu26nuzPeuPsHKt0eUVam6LzCC5_9dfcidyQEAIW4hdMPofQDbWhF_gZJ_p6a8J5X9RrshjWUdPlfx3DMWDKoO-QM5BpWvXsFthVTDJWoLMeQggATSigEWP9OonLvZk2LYMhbXioAW_OVDYIkCNfp95Z4jqHrNn2SwC1gwKtyUsa_GdwQg0e0asHBWx4N0FInmcNKfL7kWtRTdJ9UQ3zI9U3ygorWeQ58TR8kfyC3o-mMvtxZmH3gc4WOW9wXW_3kUynYR8wqPDTzAHRmM01xyPoyxtNbl8VMLD4HzxoJaA0-wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وضعیت پشم‌ریزون خیابونای مکزیکککک
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92084" target="_blank">📅 20:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLd9HfiQ-dwHnQHU7l-vFKH0WNFYG4ErMMzGqcGJo9g-5eZ1NRLExKmb9aqvw6mBpg7OQFAFho06JbnlwSnNRX3UzOW224GxCcrf7Lg5CaELxSRqxqKTkunu3EyjLIvfRcIoOWn4rYolId-haD2Ve2eQxqQxXzEuzL56ZmWFGDj66gbYR8evsnJa8ic79A-zYm32EKX1VcofWPcOgn8A00z2scD4RhpW7bBAka2-lNSPUaFXE7VEZiKg1ICO6VJiijtAjh1Ch90Gihm3UIO16lD92YdYnAoTaitswmCJrqalRyT7qA9Ex-1q01arKOUhe8WrzSfWo2vdHXh5D9XJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6dada1cba.mp4?token=cTadGSj7WA5vqNWjrvbKdTR0TvrP9_j7AB_QNCLEq-omB71feaFNtwsokN58hd8PANGCVVidO5BOTzlQ8tL4KWmhOnPx5Qigy52bT5QsRnhax8wcnS9MBjvoTgMHuz2G74pfcVtrJVY6zZSzPQUZTWINJPGR3uwUd9WRum7glFDyrhhJOiHSqnYY6jV0xzb_IyaoPnsp2tEELh8NuLuow5KvJIlxHoYZ-GIyMe2ZaMHuXBhJko0PhuAi3mpV5v8Vuk3uR8MwvlCn6Z6qOmR_qa3NfKTlmNjT_w8grFS1P1R4VHt5GatxYRkpOOyZ8rOeVeI7Oqq7EItC-yoIA0uxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6dada1cba.mp4?token=cTadGSj7WA5vqNWjrvbKdTR0TvrP9_j7AB_QNCLEq-omB71feaFNtwsokN58hd8PANGCVVidO5BOTzlQ8tL4KWmhOnPx5Qigy52bT5QsRnhax8wcnS9MBjvoTgMHuz2G74pfcVtrJVY6zZSzPQUZTWINJPGR3uwUd9WRum7glFDyrhhJOiHSqnYY6jV0xzb_IyaoPnsp2tEELh8NuLuow5KvJIlxHoYZ-GIyMe2ZaMHuXBhJko0PhuAi3mpV5v8Vuk3uR8MwvlCn6Z6qOmR_qa3NfKTlmNjT_w8grFS1P1R4VHt5GatxYRkpOOyZ8rOeVeI7Oqq7EItC-yoIA0uxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشقتون لیسا خانوم هستن که قراره تو مراسم افتتاحیه قبل‌بازی آمریکا و پاراگوئه تو لس‌آنجلس، برنامه اجرا کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/92082" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92081">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc82e4c46b.mp4?token=pZjmPqjw7MAYQLrEfgyVVXBIQJbH0P9fZ9yHExuFgl5NP89ZvwdJV-FMR_RT24QmtS0dlhJwDnwly-F1DoXrGyjT_vygwyXpNq7yApVP0XMuqCeEzBVjU1yqfKUcI8-xLnBaL0MGN_S2CHY2dUupL9uIBZz0tJeQcScp7WKeVjVIwuZlgr9-gFHL4tWJwXZ9jB5BbppTG9JjrdhcH-giof7zMI4BWWK8aK8qgblA6DV9l4AF8uXSyCmiCWkjyjIs6Qa_uCvEwlQNyMcYGnIvayItTnvAp2QM-SU8nr4cM7lGDHs7H489RJnW-W6Zuzpz1WZAyNvkeC_LCweG6BO4jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc82e4c46b.mp4?token=pZjmPqjw7MAYQLrEfgyVVXBIQJbH0P9fZ9yHExuFgl5NP89ZvwdJV-FMR_RT24QmtS0dlhJwDnwly-F1DoXrGyjT_vygwyXpNq7yApVP0XMuqCeEzBVjU1yqfKUcI8-xLnBaL0MGN_S2CHY2dUupL9uIBZz0tJeQcScp7WKeVjVIwuZlgr9-gFHL4tWJwXZ9jB5BbppTG9JjrdhcH-giof7zMI4BWWK8aK8qgblA6DV9l4AF8uXSyCmiCWkjyjIs6Qa_uCvEwlQNyMcYGnIvayItTnvAp2QM-SU8nr4cM7lGDHs7H489RJnW-W6Zuzpz1WZAyNvkeC_LCweG6BO4jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت پشم‌ریزون خیابونای مکزیکککک
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/92081" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCYLLXwosMO5OZB8yAFo4iISk2oMz9iEu63_PsKFcLSPagXw1K3CMVh9vD7-VdWAotHViFhFrsUw7dL71oz1tvUVuk3S4EEmlz1KtZDBPsdHzmf9zMjPQuSR0MGcR_nmIx1OisYvOaZRbGtARpDuXkA_74deTVD7WTeS4a1ZOexP8higNuSy0S1MqxSwLZ-l9pr3DpQ-UxJR1wS2I0DbbwksIKdtdKd7kgFWVM0auroG_wPzQphCoSrW6lk1DOw4noXIR9Z4UV60CF6zjLWbhEjVrANcY7I_3AMll7SUQDAmZVQufdow5ZQBbjj1YO3iQseop48U1PQgP7RFh1XMWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇲🇽
یورگن‌کلوپ در ورزشگاه آزتکا مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/92080" target="_blank">📅 20:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🇺🇿
#فوووووری؛ ماشاریپوف بازیکن استقلال بدلیل مصدومیت جام‌جهانی رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/92079" target="_blank">📅 19:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffff5adfd.mp4?token=fNB4AWw1nlsF-zIBYDKXWzGUF-iDS_1AFSE-Qwy3-0j7PGA-zL7cUQ53dkiBLQ2YVHbVAhI0PLTmOgAo2OgRQlb2lVIbgZKmI6ybf7kpknZO1SAaFt_opgM8PvxMOZeHEP253rhJgQomK1xLZeJIqqdMSqy27EuPCcZ31qBHhUWhr2N_PwbxwLDSuz_cFndPS9PFKG4j5OXw1wEKaGKqEm1nEcHjCdxvjWS5_wclQJdacGWVuALVUm2xQHZQiZU7eUU4Pbb9hfkrQRD1THk6-xL4OaTt4YLFaL-7ub6bJU2_O-fpWPEw3KYL6HJMyEyce88QF6Q50MK5hLxFK6_Abg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffff5adfd.mp4?token=fNB4AWw1nlsF-zIBYDKXWzGUF-iDS_1AFSE-Qwy3-0j7PGA-zL7cUQ53dkiBLQ2YVHbVAhI0PLTmOgAo2OgRQlb2lVIbgZKmI6ybf7kpknZO1SAaFt_opgM8PvxMOZeHEP253rhJgQomK1xLZeJIqqdMSqy27EuPCcZ31qBHhUWhr2N_PwbxwLDSuz_cFndPS9PFKG4j5OXw1wEKaGKqEm1nEcHjCdxvjWS5_wclQJdacGWVuALVUm2xQHZQiZU7eUU4Pbb9hfkrQRD1THk6-xL4OaTt4YLFaL-7ub6bJU2_O-fpWPEw3KYL6HJMyEyce88QF6Q50MK5hLxFK6_Abg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🙂
🏆
شب‌های رویایی جام‌جهانی در اروپا و خاورمیانه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/92078" target="_blank">📅 19:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDG7IrA39lvS8rbfQE6dOvNZwlG319Ylhikh__pgWsQbZDB0Ts0RdxXg3i8EUIeEN39nJKwsJ-hPEkyvbQs-GMmp9up66Yj8GT3EGB8PL7kx7IRkofwdyaZ3mkhr1v1CubMGFKqo-X76MPbFCZJe0S7mHdD4bj8g-WfUXlZz1tsLP_SSemP0gZRh83hJc2ECec5jZUXmxJouJE7vKbWdsqyaxpkJN52hS2ttoEe_Xun3O08xMF_0wTXcg_IzgayIFGott1oiinydk5PC5Hlbb4uOix3xQAfItgFPYR54wK0QCSXhsm_6_3O3QinlCsgaEcCFzR0X4LR1WCrQrJdW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر تو دنیا داره ترند میشه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92077" target="_blank">📅 19:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qomJ0OqkFNpjUEW6Nxjccw8JWIB3nRxtiVYHmiqbssKjnWRUkft3WIuw4Y5fkc6hbpoh6i-NN7Qu9dK6qDFqjAE91_pMlj_yeT8EvgdAugcL5_DPdtI74DBavza7quIK7VYratab_5fzCLFP46gb8ldO-qJrmDmO2H3hT-jKFdLCKt2D7Mzu1SJG7cm3tkdDBq3lVghDhe2nfFvtZ1-qWHAg0nx58af5Cqb5RAWgjgyc7FOcFDfUKTWEyz6WRc8c3fm4pHKWnFXZ3WUDY04IlPajyk0bY2NENc9GpiEuDrtS0yvkjmcJ91prWZe2VmlpIe0KjPU7sL-LmeFHK9NOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🏆
ترکیب منتخب جام‌جهانی ۲۰۲۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/92076" target="_blank">📅 19:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92075">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPa-8b44RXzeAnjDfXt3dLXCk6VuVQgEoW8I-G5ajlXn60qW2z73QZhvrr0RkVmrvqDmtAuSMWv9xPyaEE-e5rutPzMZoUAtHVdw_hM-PRJvUvVTxjb6b50pbi-65_fPBuRgNlVI-xd-0gr2liRMYEzh8h1qGEBanGn44Tjns7XimvWalGtmCsDB8ROglGo2F7bgjBt1dktKIcRt2fB9AORz7c047j735s4fXwDb44rlXgHC0M6j31mmoD1vx49orMMX3e8a10TcHeBRttlCQi6eNz5g-5cE7A_p2LjBU95Xur9KqQtZ-8dQWOsnN4PweDrinXsBxiEhkGetGwBrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇲🇽
🏆
تیم ملی مکزیک بیشترین حضور را در بازی‌های افتتاحیه جام جهانی در تاریخ دارد، با ۸ بازی.
• اما نکته جالب این است که در این بازی‌ها هیچ پیروزی کسب نکرده است:
🤝
دو تساوی
❌
۶ شکست
• امشب در مقابل آفریقای جنوبی، تیم ملی مکزیک فرصت دارد این طلسم تاریخی را بشکند و اولین پیروزی خود را در بازی افتتاحیه جام جهانی به دست آورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/92075" target="_blank">📅 19:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92074">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uneSinmlQETMKVUA0jkzoXrJwBuFYFYP7cDRdA5Qo0QsZy9TO5DkPMCLlT21MyUxz8yg0G5kSceSqwn0CRsKP2607QeUYIPeIvZUr9PYt7X9Vx4jun7f4iR7WWxtMs2FqMmGz1g6U8oFbdbIDOdnd4AEdE6PBmkryAEPzZUCZKRNe0CfQVHLbYbtCaHOkQs4s_a6w5ia2AmlXsHivlV69zWtpFRuPcKZibLVPEtpQ-vvYdNSRXQWWh6dawheUDII-pr5DiQFnfLILVkdE6mjadfKYPYjW-TcFF7SaCMQj3NJFL0t4VPCUKQ_ZLcamyDoGvTjbyS34JzNwXsQrhcVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇲🇽
هفته‌اول مرحله‌گروهی جام‌جهانی؛ ترکیب مکزیک مقابل آفریقای‌جنوبی؛ ساعت
۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/92074" target="_blank">📅 19:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92070">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Co_6BzGH8aVT9mZkWU1_aTNsfsw_tsakt7zTSZckHaEb4fmmpZ2OTij0TVtrOlaFPtsT8OrFir5OXD_aopNi4uOJLObvbNafzjNar2o6P9o6Hc54WnQN93PExZDXRwkcXqHpyLCAgXkITXNTGaJ2O9JOAjWAcEnQXxJTL3SSknDhnJiCKvzu9mehS4OQEjBGxKDCXLaiZ9e1VJoxhxcEms73MPFLtKSUhPKmzqMamzQFToxRb8kh2U3YIN64b4D2w5XN7jdgiKilgUi9TmAEgQXjJs8Sx7aHKhKh_6A52vZ6zOSvpD4TjJlFM72Ml8zRWQ20jJ9T4iZaEpTXka5hyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tq5dPtEbNE5ZDKc0QRSvIKN85uvAWRoTGeuoXgTTmfMpgNlGV990Ok1e0GZcDFCQXckNj5NfCkZjh_31j33tgBaJSU6Wc-NWyK2Ab45ENBMz4MyMjgkR1yIEgbFPFmbTou4SR-4592kYs1gwTNgimZVRMn9WfEWM42wPnWhmtZQTGkfzFtdqiJRl1WhubkHIrZSXKNWGHTn606SUVsnAlFPRkInsSbwJc0er4VjZVPSSZoZehi6PDriYOapzaB4M-eaDtdx7nOilhPE4cQAXneLG4GgbdFsymXoHnHLjEw6rrYyNpVF6dECVcx1BlwMG-6uZfJVsdHWXT2TiPmQCRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O85sr2jZx5oT3GmrDt2csagPZ3jDiBl0DhsAY4QwDx3Nh_qbIbXguTggbbHwSlX6RpLisyCNhc0OtkOYhUBTxHJ6mpWl1vr-lARwM1joNdq8g2fyYRu1FapTaZruK4Cdf6bIRW6aCjeq8egQazwYZ5Py1H8Q6y6CVLHFRChQsLzU6cnvoAvIheVH1NPJgLeJUV4DGQ6WuUoi-CMpxVLtgsYEtYHa8afd8aN_d0-C14eAMMvSdktyoL7AuXU4aHpU3O1AJHGYzhcCiQ5DeTzjgKH4-d6sL_umPLtUmlVT09SRgY5vvLKYdZSIuFLIeMrWg0DxmkJQ6ftzbCzrWDpiCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FuMJWVJq5hZmmpiZBfr1QcpmjncVoDAxXJKIAi47ww3StjlWlRCq4a9p6_tR2-VUqdkFMrFox9YEwbtlJxxCXgtayuK7iAq4woojCfc69wNqrfejkhzwvlUrQcKTp2fcXLxPQ8aKQWJF3MmdA0s-A3C6lMkjRl_XRiVpM6SpZ0b8pbCyPy8OdOjOrhMvfS-i4Mg4K5lZObivkx2q_yhOAT61XJhsUD142GKP-nrsDRxt80OjBNIsN8qQ7cpz9s_QFbzx8LCH5glYDFgE5uzQl-LleJB_MBYZoUpLEyEpNPzF7_HSsdyz285i9DOAi9TBqVHRzhbAWgTkUa54EPnjFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇲🇽
🔥
تماشاگران مکزیکی ‌آماده جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/92070" target="_blank">📅 19:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92069">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnBE_82cETwQahl20FrdA-rjYLxFfIrZXFFY1ogs2ArlSM14TbdpV4IYTCQ5DN18F69p25Zx30XZH5SeoTssEA8GBdlUqjdqxRJD5o-NHdrB2fIaBMTvCBbb3L95vmhhJpmJIkCXv7rtOHIGn5FB4IHqNR_vtRLl8sisCXs56NJgGO12eaAY3yhROZZLD_5PxcYDGKPsRTTigMZyPv2k-G4Z9TZyhDzRhZKKfkaAGTq867o_4_xme9zl2DZZ9JW3Mnh9iWEnmMQGJYGr0FrulAfwDdXnflDhDQ1ymaDRXUjip6vA0NVzh4ApTrUI9o78KpsIP7BCdTncjqzwTSKlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
بر عکس آمریکا بنظرم مکزیک دقیقا روح فوتبال توش جریان داره!
هم میزبان پله بوده هم مارادونا و اصلا انگار گره خورده به جام جهانی
پ ن : عکس از افتتاحیه جام جهانی 1986
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/92069" target="_blank">📅 19:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92068">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjGKWaTE6MvsAu6eDVJcL_m2-pDVHjKB2KH6fBy3512koYwrc9iAxc6QloLxYj5v5P4zkiRqzhnCuK22U74u6KsCvomDtDOC3JoVHtAdIw_kVerEzJUyMbb31as5WNHLQFtS6oswmI-J6gz_Cy0kJ-J-rpzNLG37lam0Sd--mhE-2ZEM6ypD2VEumcXVtKSagdELWh1X4eRPX5h952FDpFcwwxpqWpt2Mc6KlXzMTusPZiGOh4ZgomIAEkR2z1oI1Phud5-bzSUD1zQDyxi2gT11gxNehZh1TARmbwki_K-TiTPar4WLSjF_B9vCwLSRiCI4vWbCG9A043qIZSmerw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">17 سال پیش تو چنین روزی، رونالدو به رئال مادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/92068" target="_blank">📅 18:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92067">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92067" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/92067" target="_blank">📅 18:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92066">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyAldP380a2KmthzkrQ207vt3fsrBJerv7kotWKICFuUDKCixTGW5FkoG7ZxSAvaq-vcbQmVLrluWzAVy5vFPv9PvHHa9Ua0-gd49uee0KP5bwq_-cg0x0AXbXKO-hwRClGt1NUrWXckIpdTjOJL5_YsIoiYA3s-MJswgKLMffKSCaQbKXlv0JfYNXbnyITVJ6OjJZf6naHcBiwUNodxNA2yBpegNtQB2H-3ShzavkwwoQWJMTcdD2Qq71wbMZ4GtHzdindf8KovBmGpn0E2RsORGHppXOfSXG2LwoDHOLcVjCBVPf65CcsoKeGzfs32s7UWo3K5Z8DpsQICm_kqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/92066" target="_blank">📅 18:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92065">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
🏆
💥
ده سوپرگل تماشایی در ادوار جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/92065" target="_blank">📅 18:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92064">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKVAu4i8nOige4PxC6erqlihT3i-E7ZFZfN3Mc7DrQoJ_ybUyIKbSDjMnHQ3Kj1Uhtg-wAPeYGX2GzjutVECl475f7BJ3ZzET9th_kLhKHHVelu7SLJ_hr9qqcu_eoMqWniUJN5ZUmBRHHxEn2yfhddFH07pJ0TPFZupxJsPB5KyQKowNf_0TsjLWConrwYh5tEhUHicad7iLmTmkwiot-0IT7Ce3ppmNSbuDFtrDFL-tO-zJ1kr8F3r-S1MeVpUtdLKFwu1g_jkZbs8Sz2XWeAL9tWB59UfKTCW1H1ShFezgjzA_Cj91ggHdW9gPiBt5AlDW9f-aNLPz5ggJhmO9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
ارزشمندترین بازیکنان جام جهانی ۲۰۲۶ با حضور یامال و هالند در صدر با ۲۰۰ میلیون یورو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92064" target="_blank">📅 18:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92063">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81506eae7c.mp4?token=v6S_weTY7y8ON2j9wY_ISWAMer3nxiD1QlsuwyxEUNv9Tv128ugRaUXV2e5tjm9n2CggLBEKjNAjtlLaURmnM4kxjCz0Q6oLGVbyFHPBn5jtp6nDisKHS7d58G81jIn6qeAEEJB51MdlezaWhsMRPIEkCio--ZXPZZwFr0sYgUTO5Xa5KG6dwMMMWufOjYrQ5_FXvIUGquCMJcAqtJ9gHJA4IQj2n7UxlvhhhFGnC8Yz0RC661V33vdz9Ypq8M6L9AOz-U7u1rTQA_T4RsED_UqtNVveVlC4CsLhzSwPhEPP3LLZ8HMnkK2kGN0Y3xpexmWn7oZIdegtW-ZVdFsiTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81506eae7c.mp4?token=v6S_weTY7y8ON2j9wY_ISWAMer3nxiD1QlsuwyxEUNv9Tv128ugRaUXV2e5tjm9n2CggLBEKjNAjtlLaURmnM4kxjCz0Q6oLGVbyFHPBn5jtp6nDisKHS7d58G81jIn6qeAEEJB51MdlezaWhsMRPIEkCio--ZXPZZwFr0sYgUTO5Xa5KG6dwMMMWufOjYrQ5_FXvIUGquCMJcAqtJ9gHJA4IQj2n7UxlvhhhFGnC8Yz0RC661V33vdz9Ypq8M6L9AOz-U7u1rTQA_T4RsED_UqtNVveVlC4CsLhzSwPhEPP3LLZ8HMnkK2kGN0Y3xpexmWn7oZIdegtW-ZVdFsiTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇲🇽
🇿🇦
جمعیت عظیم تماشاگران مکزیکی از دقایقی‌پیش و با باز شدن درهای استادیوم وارد محل برگزاری افتتاحیه شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/92063" target="_blank">📅 18:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92062">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIWWofzJ4KzyWqBz5J_I-cqZRyDy6xM1c9y4jNdpSbpzIxgKoSlk4UEae9tg0aMdO2GEgQy37pk3qlHIR-dVEBZu-shdQUlV-UOD6H3eZBg-wA-y1hUuQJIEJSNLJ0vZwqegLX3SWRtIqYcOOtlrsJ_GLcjl7rPsLCzUM6FqU96T5DJtTFMCTSR7dYWjCdgJg3-syAxhmva-q_lG4fbUO8knz3dR1pgamV-GkrU_3TGpzlsqX8-BwOv-J5MuLxjT-s7I1EkedOLJjP932K1-M1A792heGq5rN8xdL7n3eR5Z7uheBRdm4HlbGdjGFjA-9eV-DJLpTYEOmfcbqg76WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نخست وزیر مکزیک به دلیل ترس از هو شدن توسط هواداران در ورزشگاه آزتکا، در بازی افتتاحیه جام جهانی شرکت نخواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/92062" target="_blank">📅 18:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92061">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beMpvZRM0V9bUoFAoEUbeochWajNBttzgtJCVOjAcDNMvnH5C03okhAJBDJAnPRvaAwkzE1snJvSLIkqe-C5qhZbtNxWxRhsKgsAzXCP7HygSZe9lG8pzQuP6rQ9RSsbQYxX8_sK88FVtXk5sMHFNKdhTX2ceNtOYne0BPlPSkbj2XQlLUFMqpcTfjJon4JlXQj5uNyrKEzKDK0EEnqmsg66o8T_YxIBSa1UZ_w7d1pVQdzi4CRuuhzWaO3wydzEGZtQR_eN0fn8O3wpp23WZFFwuiD_0oLcMImlXp3EZ508pRb498WPc3_Cl4cALfra3SApDraxvuhV54sIBWVa6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آلوارو موراتا: "کریستیانو همیشه با من به شکلی استثنایی رفتار می‌کرد، یادم می‌آید وقتی برای خرید بیرون می‌رفتیم، با هدایایی مثل آیپد، تلفن‌های همراه و عطرها ما را غافلگیر می‌کرد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92061" target="_blank">📅 18:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92060">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c5dd1e48.mp4?token=MyGjXH8wWHBQ-DbNN165Ed9OezsEkBMHljf-wkEue4RJBRg7ItUnkc6RqNDGAVCuAdV7RyK87XiXdVR5w_Qs71XGHIJSzsFwdSxTANY3dy5891AQB_VocwkGR5XszZnm_GgLhFVcYdpAiBIEmurrVUPKyiRktMV8wpiXxOHBgjuhCKywKK3Yg1IHFjCf0Uo1I3sIVUCOkINNzd9eYKHSmw4NSrVuHcAkCmTYNoijG7gK6cQbWnL4A_YR-WhcPb5LGQ0wvXcCB6QeZ47Io7teNNzvfvYWJ0UmCPGiN9lRad2P9DReZxCmMIsZGyHQHA5MyJw6Phb_iwTQZ5IawveSRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c5dd1e48.mp4?token=MyGjXH8wWHBQ-DbNN165Ed9OezsEkBMHljf-wkEue4RJBRg7ItUnkc6RqNDGAVCuAdV7RyK87XiXdVR5w_Qs71XGHIJSzsFwdSxTANY3dy5891AQB_VocwkGR5XszZnm_GgLhFVcYdpAiBIEmurrVUPKyiRktMV8wpiXxOHBgjuhCKywKK3Yg1IHFjCf0Uo1I3sIVUCOkINNzd9eYKHSmw4NSrVuHcAkCmTYNoijG7gK6cQbWnL4A_YR-WhcPb5LGQ0wvXcCB6QeZ47Io7teNNzvfvYWJ0UmCPGiN9lRad2P9DReZxCmMIsZGyHQHA5MyJw6Phb_iwTQZ5IawveSRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی : این آبه ؟
مک آلیستر : نه احمق اون آب نیست بده من
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/92060" target="_blank">📅 17:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0db4c3221.mp4?token=nNBDfXDutfdoAQDDVXVjX0mRpXuyZrglgaw1hqitGSSIFzUEOypLq2KesKP8Ygoys4hp8GXDUgcA1lCmpA1FaCQThKvjc-j3uxowE01gyIB7hRwD0ETrMwmlQxZWPTCoym2_k6FYOWkBRsl4ujrje1yPdudIZ8aGcZn3f4jGXkcZQrsEAfc_LO9qc9JkJN2a76abcg1YTcbA7Pp_tE1k2ZKLx9l5XmOuH0euBnTxRzDXKBmdrMsgnbj0nF63WX8Y9-AiCNofnwU11quUp4dR6I6AWRMg9VAALJYA0mqNiWLjacEA-X-uYzqP-BFVFuw_J7eI-X4U_11l9YYE6-8qmL98Nn5T1Us91S8dDh4h6IT_fdGHI7YaeeRGbTNqg4t8wwKi5zHM6V8aiTbbvVPL00EEVEiL7E2UIaE8So-9lUK1L46rnoi7e5Xg6u_akF2JqzkxONrypXp9xxK1dGYKykOsGvE5_ltRxOsDHw3_-lB-KiFgszy4sQfelnomokbXZ9z_yjd374M3ljLj5EcEnNThdSBS8AEv-FiEtB-I_R-aTTDhWa039nX9SH3d_AJInzyaJt4oy-f7Mz3Ic-oxJwlgam-ueVBx4Ep3BSBO2VEqNDWOf2kPNBRMGCX636BJcW9HoVMRPewohJV2-xl9qn8kGfSshK4fJfprqAD_Vew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0db4c3221.mp4?token=nNBDfXDutfdoAQDDVXVjX0mRpXuyZrglgaw1hqitGSSIFzUEOypLq2KesKP8Ygoys4hp8GXDUgcA1lCmpA1FaCQThKvjc-j3uxowE01gyIB7hRwD0ETrMwmlQxZWPTCoym2_k6FYOWkBRsl4ujrje1yPdudIZ8aGcZn3f4jGXkcZQrsEAfc_LO9qc9JkJN2a76abcg1YTcbA7Pp_tE1k2ZKLx9l5XmOuH0euBnTxRzDXKBmdrMsgnbj0nF63WX8Y9-AiCNofnwU11quUp4dR6I6AWRMg9VAALJYA0mqNiWLjacEA-X-uYzqP-BFVFuw_J7eI-X4U_11l9YYE6-8qmL98Nn5T1Us91S8dDh4h6IT_fdGHI7YaeeRGbTNqg4t8wwKi5zHM6V8aiTbbvVPL00EEVEiL7E2UIaE8So-9lUK1L46rnoi7e5Xg6u_akF2JqzkxONrypXp9xxK1dGYKykOsGvE5_ltRxOsDHw3_-lB-KiFgszy4sQfelnomokbXZ9z_yjd374M3ljLj5EcEnNThdSBS8AEv-FiEtB-I_R-aTTDhWa039nX9SH3d_AJInzyaJt4oy-f7Mz3Ic-oxJwlgam-ueVBx4Ep3BSBO2VEqNDWOf2kPNBRMGCX636BJcW9HoVMRPewohJV2-xl9qn8kGfSshK4fJfprqAD_Vew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
صحبت‌های جالب مجتبی پوربخش راجب افتخار تاریخ داوری ایران‌ و‌ آسیا علیرضا فغانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/92059" target="_blank">📅 17:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهایپراستار ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5kedM18a701wYEe8pgnxx3aGkpsYXyKibqweWFayHSWU6CePE13pNiWnIthEGblwhuBPJVl0VCnCaIqsbfk4LQZXgHJw0KZ_RUkl4lxcfyxfqYykDLY_jnFNQIb2ex2AswrJmBHwtrZVVaySDjxZQwlMIgVhkwxXVjU3SRR7VOCJMPVcgkQ43eWuyA6szerjoSUyMHpzws_3pDvlR2mTMjLlVS3_EA8talRnjsXwt9TQh82_eljS_UZ3vJRKjPXar1q9Wp5FenWnvlr1J5c4Pt-Cl4tygoyb1PwiX-4hVHrC3PI3fM06DrVnr2dKT59fWnIhim648rjr-UqLOLohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی کن، پلی‌استیشن ببر!
🏆
قهرمان رو پیش‌بینی کن و هر روز بیا تو ربات تا یکی از جوایز رو تو ببری!
🤑
ورود به ربات پیش‌بینی:
🔃
@hyperstariranofficialbot
🔃
@hyperstariranofficialbot
🔃
@hyperstariranofficialbot
بازی امشب:
مکزیک
🇲🇽
- آفریقای جنوبی
🇿🇦
بازی‌های فردا:
کره جنوبی
🇰🇷
- جمهوری چک
🇨🇿
کانادا
🇨🇦
- بوسنی و هرزگوین
🇧🇦
کانال رسمی هایپراستار ایران:
🔤
@Hyperstarofficial</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/92058" target="_blank">📅 17:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خایه‌نیست که ماشالا. پیکنیکههههههه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/92057" target="_blank">📅 17:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFGjej0Wei7xq0p1mLucyISc9VtJvAbN_hjZZFtcmKajiqj5eMmNTJUobKm8SPWtkZ8q_LJfWxu5zjohab2G-S15PKoOY2kYFuv2Gg1UdNgJKEh4g-xB2wM5dDWbMx-a-UAPX7DxdfwArZhUFlHmsywVWgIhbbuV_W-BapIpjVypEP_3Mw0nIzkw-NXDdmmmz8EBVjk7ctclp4Rldnoa4qBjG6mzkUfMcKjSUtp_sie9uCNDLo5FgnAsRdeGsf4MyFMZVfG_y07r1D6Fnf1lOQpfbhqCG7ybpkOBuaRHB3XrCmqcu0PWlUvN44X-16xqHuAi6DgrLGM74-7zam2N_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏟
وضعیت ورزشگاه میزبان افتتاحیه جام‌جهانی چند ساعت قبل از مراسم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/92056" target="_blank">📅 17:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iKxkPhsguUfNYhaxStLYnf_NmHMQKTMlgBSnbKtoz-0t8ygf71Wq65uisPT4dCKVAmfivitFEE-IqB-nPqcCIpszNpa3G46jPsodHLwEGWdjyV81FDM6lWzP96fofdRUeQdN_UUbLjeMQCNqOXWo2V41rvSJkXQOOdhftwT4ITF4cwskq3Gnp_kEMimwmIF7ufOafN0ILCUMrajBGlUIhRxrvLfTIRfv3zI15lmOw0iAZOHPN00BA3gPuJ4OTAxVUJu_dsEf_2JzSxHHn-uPdAtWemyGz-9Wk8tzu0q0GjBA-ICV0rxc1hP4C0X6T_TRnZ0zyewDcF3AN-Q-A-LfUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ترکیب منتخب ستارگان جام‌جهانی که آخرین دوره حضور خود را سپری خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92055" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnmxnLtVCVF9l6sWUM8ucz_E485_njDBeqqSx6vIla5A7wE6r2CX6RsLFHby2ebiWt_DNv_TjR_nIq8DniLcknRzpxyRYknnkbhM5fmu8mZakjPou2jNzpT3YJ0wt-yRMyif9Gtc8cvmyueJQg-ZW3an9XC2mZik5K-6IW3LhXQF7jCuKBRKeNRaOEqyPql279_NJQEzmkVov8zZzVhbRCMP7xJR89CG0pSMGtET5kyGBurs7hbyofCOxXbfvJ7hOnTQIdEFT3JiQw1MoDYqF7pq26NgnWjY10rF3oExEHLBhcQJpmwz_GmZ4mM22zboKgf8rKRBsr0DGAhrAvfruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین پیش‌بینی بزرگ جام جهانی
همراه اولی‌ها جام را به چه کسی می‌دهند؟
🔹
همراه اول همزمان با آغاز لیگ پیش‌بینی جام جهانی در «همراه من» این فرصت را در اختیار کاربران قرار داده تا پیش از شروع مسابقات، قهرمان مورد نظر خود را انتخاب کنند و پیش‌بینی‌شان را با سایر فوتبال‌دوستان به اشتراک بگذارند.
🔹
در لیگ پیش‌بینی جام جهانی، کاربران علاوه بر پیش‌بینی نتایج مسابقات، می‌توانند تیم قهرمان را نیز انتخاب کنند و بر اساس عملکرد خود در طول مسابقات امتیاز بگیرند.
🔹
برای شرکت در این پیش‌بینی
اینجا
کلیک کنید.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/92054" target="_blank">📅 17:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32b927065.mp4?token=DXFEV6A-zuhyULK-xcOn91g3tJvG7kjo84-IbsWzjl3cxPGx2OaggAt4dA0QmTcKtn-w4ZGmOeWA6xE6BhI4NGux38qnpNqaMQTEMuQSzxhQYs1U8v09qSZuv7Tf8rKGjQQmJ6hKOjh8ju9xXxerqJTG0Js0thp_c-Qjr1GG_lqZUidiDqf9rfGPBv2cONC74qDzTW6NynlFeeKcp3JyYpGaqJv-Bg1ep6_LSI09QdzV7NfqQSfvFG1l86zSOI7E5QyU4p6eh8yCq-7mhu-L3iYOGjV8Sb15L991H4JeQ35jRl16dSUR5pxqE0KnWalK8LHBVvWdmwwcpKHZY_an3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32b927065.mp4?token=DXFEV6A-zuhyULK-xcOn91g3tJvG7kjo84-IbsWzjl3cxPGx2OaggAt4dA0QmTcKtn-w4ZGmOeWA6xE6BhI4NGux38qnpNqaMQTEMuQSzxhQYs1U8v09qSZuv7Tf8rKGjQQmJ6hKOjh8ju9xXxerqJTG0Js0thp_c-Qjr1GG_lqZUidiDqf9rfGPBv2cONC74qDzTW6NynlFeeKcp3JyYpGaqJv-Bg1ep6_LSI09QdzV7NfqQSfvFG1l86zSOI7E5QyU4p6eh8yCq-7mhu-L3iYOGjV8Sb15L991H4JeQ35jRl16dSUR5pxqE0KnWalK8LHBVvWdmwwcpKHZY_an3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
اجرای شکیرا دیروز‌ روی استیج با موزیک دای‌دای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/92053" target="_blank">📅 17:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: ایالات متحده از این پس «هر شب» به ایران حمله خواهد کرد، تا زمانی که به توافق برسد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92052" target="_blank">📅 16:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYZhFBe42qjAJ0Uns7NlKT-l9i4a65MiVHcyOlQvxu3_di0IdU7fTawPFAlHZV_U8S-Ny_T-tbLwWnBsyMuTqcaGOD5Z_bYXMlMOgIKk37vW1nNX7R3ddbyMTofWoL6iVck84GLkj6yZb590LAMsz-kzGDVTQtT9e5Mr4MuVS-lY6vhW7goR7BuYJDGOm0jteuajpQ7Q3Ma584gQYDMMCjWa2qSKjgRLzRnvG4UJROo1Lt9JG3PVKwzMOhSy3wECQzk6VkakQ8ivPjeocb7XIF3w8Ki56bnP8AqNBaKUwZqSZWiercTWRQkf1VnLX18YVZdfHka83v4hodEyFH2_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤝
🇫🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اتحادیه اروپا عمر ارتان سومالیایی را که از جام‌جهانی منع شده بود، به عنوان داور بازی سوپرکاپ اروپا بین پاری سن ژرمن و استون ویلا منصوب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/92051" target="_blank">📅 16:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1c02dd8f.mp4?token=fGEf93b_GZltKPOhjeshyFoVy-OMKJQRA_3KSSp1Xj_IAf8gGzrv_ryiaeCHRqnu7tbwUpCG2UkBGOikPN18xfSpGOQaax4pZ-x3ITth6q9eSSyQLS3SuZskrVOHq9oCYUhXSS2YKNbiL7GtwqOvGlfNX9ocA9JsqAyFSBE2tIvfp9iT3qJ18E5BaNpq32umPz1Nk06GorOqspocqS-_qCZWlyRs8gGlEKqsRd3c_F3OR7Bgwf2Wd0YHllNHvthayGhJ1-uCCzVYJonFoO58-AAKR2CJ_LFJS4gtIPXaunaxFq9PbGdvQtT-1h1mh4vIerOHjGdjKLUCYwA6Vdm_sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1c02dd8f.mp4?token=fGEf93b_GZltKPOhjeshyFoVy-OMKJQRA_3KSSp1Xj_IAf8gGzrv_ryiaeCHRqnu7tbwUpCG2UkBGOikPN18xfSpGOQaax4pZ-x3ITth6q9eSSyQLS3SuZskrVOHq9oCYUhXSS2YKNbiL7GtwqOvGlfNX9ocA9JsqAyFSBE2tIvfp9iT3qJ18E5BaNpq32umPz1Nk06GorOqspocqS-_qCZWlyRs8gGlEKqsRd3c_F3OR7Bgwf2Wd0YHllNHvthayGhJ1-uCCzVYJonFoO58-AAKR2CJ_LFJS4gtIPXaunaxFq9PbGdvQtT-1h1mh4vIerOHjGdjKLUCYwA6Vdm_sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من از این به بعد فن پاراگوئه هستم دلیلش هم به خودم مربوطه هرکی مشکل داره میتونه از ایران بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/92050" target="_blank">📅 16:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92049">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhKBR9C9TWbpEhxHF6aa30wF_xUYfu6U5S9okCHcMf3a_yOofMjkhV-JVrUBjw60SOZe62CvhK-m6gF-nkcpfsB62tJnt5lnOqNV9lXvHfbuP3x6PUWS99nSw7RG5qUv9Beyozzd-oBtuU-M7_dULMCV8O0JERgpb1qtbeiMNSxX6HHMeQcXYrTpbXdFuj8IFwbsbAC7PETs7VZKuU8GhPk8IM1D9WKieEbjYpMD-fOZ_8GWR_KrUROGz2JoKkJiCE__MJ7yDu9-HvuicwRsZEgeFIXwVBYlNYD21n_B7qlCfSCxyJyexxMpeeZx9RkF2CSAMTgD09YFxVoEWYDDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوزه فلیکس دیاز : برناردو سیلوا به شدت به پیوستن به رئال مادرید نزدیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/92049" target="_blank">📅 16:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92048">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c32ac0cc6.mp4?token=Dn-h5AAv5QUzd3-zBma4Gii-hfFiFGjVUCypQQE591o40UrAf3G_Xk-qIa3RKikjLxiQflHbQsMDwCuhgK8YINMrNsaZx80LGLjpcKH6kV1WT9FUop2htYthzq6g7xmDk_yF6DAXOzU_1_wCdol2vuVtUGvyaXbs8wJa-jdwxLGjKN155cqle7IBIxh1ST4k7K1eeaKELUmSt1mFc25NIxFFoskZRr2ZnbJZVocptJfd8z1M2ykssn9NnNBWhqnujmofPulqbIg6LYghrJ6D93LtE7e86vRZeDXB8NmcjUk8g7rNhwqwEcR3xiIet3du6E07ZUfjPvRUDinYi0xK-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c32ac0cc6.mp4?token=Dn-h5AAv5QUzd3-zBma4Gii-hfFiFGjVUCypQQE591o40UrAf3G_Xk-qIa3RKikjLxiQflHbQsMDwCuhgK8YINMrNsaZx80LGLjpcKH6kV1WT9FUop2htYthzq6g7xmDk_yF6DAXOzU_1_wCdol2vuVtUGvyaXbs8wJa-jdwxLGjKN155cqle7IBIxh1ST4k7K1eeaKELUmSt1mFc25NIxFFoskZRr2ZnbJZVocptJfd8z1M2ykssn9NnNBWhqnujmofPulqbIg6LYghrJ6D93LtE7e86vRZeDXB8NmcjUk8g7rNhwqwEcR3xiIet3du6E07ZUfjPvRUDinYi0xK-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇨🇭
🇶🇦
نمایش‌تمرینی کادر برگزاری بازی قطر و سوئیس در فاصله چند روز‌ مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92048" target="_blank">📅 16:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92047">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ: من ترجیح خودم اینه که پل‌ها و نیروگاه‌ها رو هدف قرار ندم چون مردم نمیتونن آب بنوشند و رنج می‌برن، من نمیخوام این کار رو کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/92047" target="_blank">📅 16:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به فاکس نیوز : ایران الان داره با ما مذاکره میکنه  ترجیح شخصی من اینه که جزیره خارک رو بگیریم. فقط مطمئن نیستم آمریکا آمادگی یا تمایلش رو داشته باشه که چنین کاری انجام بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/92046" target="_blank">📅 16:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5ubhACXr0TmUIwXIlxUUhEKz_aT5_5-7VRfFvPJlYu12bFIDJsBw-Z10AEzxfVnemDuXzKxlVSgQzx0MhcFeNI4WjkcI_Oqo8CW-Dw_fkGJP8iJibDqfvQuSdDrJn4PcEOi0ByVN87hhfppedOyvJHccyF5GWHzhnHYSp4_3PpF35jj9LVLe-CgPdwxY4VnKUo28pIq85zMFk7hAkrbs6T5HD9utJqttn3TlrUzy7E4yGEI_PTrA22wWIvX7OEw9mKC7_HPdlZICp7ba-tAePZ9P7fcxhI_xHQUTwzPt-hQIUfcLrrtxbbvBpfiDXC6y4swIB_QoJ5TqApFCOUZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ به فاکس نیوز : ایران الان داره با ما مذاکره میکنه
ترجیح شخصی من اینه که جزیره خارک رو بگیریم.
فقط مطمئن نیستم آمریکا آمادگی یا تمایلش رو داشته باشه که چنین کاری انجام بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/92045" target="_blank">📅 16:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92044">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787198f5a5.mp4?token=pE4vJxI81pMR_TRsl94okURH-L9fKZTC5gKnmhZHYyRBj112T7B5MLhWYB9b97a4Eq7FYUNXGCT_cGpfhfq4VCQaKrkEFvV_X3spkSMH9reunTVmIwFU0z2uVlSMUgWX-5sbGapKDi3J-t9wsTtTFMJr6lSNMuBnmbYp8Yv8IsIsSW2jAE77aGOWuorDM54Gmx6ZwP_1C63xIRGdB2-fRjAkoFNiW4ECQE7rd47Qw84odH9SpLMlEUFrij6A0BFYl6lQ8RtctoLCN6z1Q5FcAGwabfsAiv0dwjXjA_d-Qj9UyHEP14od9hlgAq6jAgY5iCqEJSgkHoQx1eJ06LWikw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787198f5a5.mp4?token=pE4vJxI81pMR_TRsl94okURH-L9fKZTC5gKnmhZHYyRBj112T7B5MLhWYB9b97a4Eq7FYUNXGCT_cGpfhfq4VCQaKrkEFvV_X3spkSMH9reunTVmIwFU0z2uVlSMUgWX-5sbGapKDi3J-t9wsTtTFMJr6lSNMuBnmbYp8Yv8IsIsSW2jAE77aGOWuorDM54Gmx6ZwP_1C63xIRGdB2-fRjAkoFNiW4ECQE7rd47Qw84odH9SpLMlEUFrij6A0BFYl6lQ8RtctoLCN6z1Q5FcAGwabfsAiv0dwjXjA_d-Qj9UyHEP14od9hlgAq6jAgY5iCqEJSgkHoQx1eJ06LWikw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
☔️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
وضعیت استادیوم بازی دیشب انگلیس و کاستاریکا تو کشور آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/92044" target="_blank">📅 16:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92043">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
🔴
🔴
ترامپ :
🔻
ایالات متحده امشب حمله بسیار شدیدی به ایران انجام خواهد داد.
🔻
در مقطعی در آینده‌ای نه‌چندان دور، ما کنترل جزیره خارک و سایر زیرساخت‌های نفتی را به دست خواهیم گرفت و تسلط کامل بر بازارهای نفت و گاز آن‌ها پیدا می‌کنیم
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/92043" target="_blank">📅 15:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92041">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU-Iz-4tFjSZBeZUkM0Ft65UAWyL6165sEcfVuh1gSVDQ7U6EdWQKjntz2axBgA443jqX5W-Bf1PisQ-ApgweupLSmVCkndjQN6KTfuHfC1g0ZTteB5Od6_FPNTP909Kuzi5lmAO8Qp_O1JeQ732i0ghCnBqlwpVcYN1rgzdZz9ryUeZBgaKAozOAR5DcFZIXFgPxzl9iTK86z3TwD_W1cnBPJSo6tnG2q1OlM8yTdjs5b038MtuGk1UZZfDKwaVJXFsLG6nuoko-Pd1CenBYV430kv2NCuj_uEj9nMaItUon6VUv_moWwZlVcQDseSug7WuqbKtB6CcKKL29dCXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوزه فلیکس دیاز : برناردو سیلوا به شدت به پیوستن به رئال مادرید نزدیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92041" target="_blank">📅 15:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92040">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f53efb98.mp4?token=sndVT_ko7_mTM3kl91kBmlXgwAwHodR0P8f3A33CFI6ev2RJ-xeFNLC7RZVBY7uKgc6mAt2RnNp8yhPu-gnDQo5Bi9kW7_BA12vzQ8kiXlYbiBMy-mOurZv1qy1QWmjc7ss9MbYT2DpOE4j7PhivrCg_oF3G7fEKFavoKNn3h97QhY4glp49TO6a-bmoumoYu3YcRKbCXIXIoI1L9fEWPwtz87D7okpUSj9pAUl4Gs4bsaanuorQ6u5FuFFp7KIiXtNkCklZ5wW4p3mOD7xanUnBVronVX6JVRdWM_GkDcG-5Z-BiubBHldiSFI9HDcpjLDgX-sXorCZtma-JzdMYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f53efb98.mp4?token=sndVT_ko7_mTM3kl91kBmlXgwAwHodR0P8f3A33CFI6ev2RJ-xeFNLC7RZVBY7uKgc6mAt2RnNp8yhPu-gnDQo5Bi9kW7_BA12vzQ8kiXlYbiBMy-mOurZv1qy1QWmjc7ss9MbYT2DpOE4j7PhivrCg_oF3G7fEKFavoKNn3h97QhY4glp49TO6a-bmoumoYu3YcRKbCXIXIoI1L9fEWPwtz87D7okpUSj9pAUl4Gs4bsaanuorQ6u5FuFFp7KIiXtNkCklZ5wW4p3mOD7xanUnBVronVX6JVRdWM_GkDcG-5Z-BiubBHldiSFI9HDcpjLDgX-sXorCZtma-JzdMYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
چالش‌دختران‌ایرانی با موزیک‌جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92040" target="_blank">📅 15:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92039">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb9ac9152.mp4?token=fM360FARjBpfpLgQFtg9LMeHdpPZoJWr_qHn1K74wfc7PF6NpyI591cNTfaLor0eDRB3DhdAu3Xrmvj1f0lBdfF3z3wypsqvPqHdPSuqK4vS0xnJM1-sZaBM0G_ViU6YKuOerWwyK7THLRhCs2zD5e_WnGuQJc_GaXGWvjdacwC87a9NFPjmutP90ACS4tMmQIs8E97tSeZvQ6hvuln4OPt7eTpPEb9v-YhAtyB8us77kH4fR61aIQuMkJpBTAxz84_soDArwemmIvGztWKyDncTa7LgtdoOAXROismHXVEKf2qUFQSI46jl1t7hdScF8sBOVWhTxNBs8_tzVOYRtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb9ac9152.mp4?token=fM360FARjBpfpLgQFtg9LMeHdpPZoJWr_qHn1K74wfc7PF6NpyI591cNTfaLor0eDRB3DhdAu3Xrmvj1f0lBdfF3z3wypsqvPqHdPSuqK4vS0xnJM1-sZaBM0G_ViU6YKuOerWwyK7THLRhCs2zD5e_WnGuQJc_GaXGWvjdacwC87a9NFPjmutP90ACS4tMmQIs8E97tSeZvQ6hvuln4OPt7eTpPEb9v-YhAtyB8us77kH4fR61aIQuMkJpBTAxz84_soDArwemmIvGztWKyDncTa7LgtdoOAXROismHXVEKf2qUFQSI46jl1t7hdScF8sBOVWhTxNBs8_tzVOYRtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
همچنان از بانوان ایرانی با موزیک‌جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/92039" target="_blank">📅 15:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92038">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAOUk_xvuUWC803wCVMmw-Y3WV0eiooZ-f7-XakqVZjvdB_Ei1MNyffdqj320gA4-qjk81VwOOUuJfHVm2yWiBYGWuGk1tS7FIIBAcNXDwv54BhV0UOl5szfAViDV-o2F_l24UQqiwqddd7urrtcFf-06rDEBdAevTeeocSveV02h0vZhIS_QAoyJdCT4PK1nz8zZXlvYhBAS8MGbUoXws9D582l1jCIoR-1vcJKUalmBZsN0u8XHSuFJeZmUnoQu7HqNIqcDijdy8E5k6R6_fy4Uwu_mJFazAqnXw3I3sa0TN6ydydLUprlNyODWXGtKHdkdaNH8q6o3PheT0LNdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم های منتخب جام جهانی ۲۰۲۶ با قوی‌ترین خط هافبک سه‌نفره
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/92038" target="_blank">📅 15:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92037">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Td2Vq3a6clHO2qQJThPDiesHHVpw2TrNOxt2x4Oc_mFTaDd7TsQnFdO7CJgXstC0mNEt8VRP7iCLnihgfrzQTZzSaf9xzqpmx5IhyUBKlJuPVfwm_LKJT0O4q3SMwuSUcFO98EwiLI83PKGrlLfhC-40wJhI1fuHZ-IX0nYgMqAF2OWGHUgXRohpgjWCZVkFzxtDpPfm_o7wVjCbDhg_kPA7ut7jT3Rf5HswsCpDpeYwtxuBf_fAi7r2CZjss6_yw1SOA_7j20cAGRXZsiOmsHFg7ozluAgBY2A-PaDeNzBITYYyfM9XCmXU5YPj_7eIoZFzRXKkAqUrZ_sYP0XyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر غم پشت اون لایکی‌ که شکیری کرده هست
هر جام جهانی میومد یه سوپر گل میزد می‌رفت چهار سال دیگه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/92037" target="_blank">📅 15:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92036">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✨
ورزشگاه خاطره‌انگیز آزتکا؛ محل افتتاحیه جام‌جهانی فوتبال بین‌مکزیک و آفریقای جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/92036" target="_blank">📅 15:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92035">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75f014414d.mp4?token=aMOmFr8BgcL3BpETOfOPPariqNa5DVetkrwWzHkwSFvmEtbgoC0utoirnsCphFwsppUlggFT-xb6HwZMGSix_gVRmWShStalpRDbH6gHtEWKz0E1Tp8we2JbXzZ6XLo4rUDH9Sv2tD5KVmZQVTtOmKoBTzTzLYZ-R4_WsZDJ5Fd85B0y-GCiXPD-KzCAm2YscB8sev9e_I_xeAnikIbn7n719Y_cGUHFhqKz1T3znrFsw8fHIqeJr_pVQspH7z7gRye28T2ARDc36qE1oJ1_ttxa6FOCDJYGn5CQYkPwnKKhFDqO057VF_vBjeda47ZJ8g5Wgf9jJmy6Sobu9Z2m0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75f014414d.mp4?token=aMOmFr8BgcL3BpETOfOPPariqNa5DVetkrwWzHkwSFvmEtbgoC0utoirnsCphFwsppUlggFT-xb6HwZMGSix_gVRmWShStalpRDbH6gHtEWKz0E1Tp8we2JbXzZ6XLo4rUDH9Sv2tD5KVmZQVTtOmKoBTzTzLYZ-R4_WsZDJ5Fd85B0y-GCiXPD-KzCAm2YscB8sev9e_I_xeAnikIbn7n719Y_cGUHFhqKz1T3znrFsw8fHIqeJr_pVQspH7z7gRye28T2ARDc36qE1oJ1_ttxa6FOCDJYGn5CQYkPwnKKhFDqO057VF_vBjeda47ZJ8g5Wgf9jJmy6Sobu9Z2m0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اونایی که جام جهانی ۲۰۱۰ بازیای اروگوئه رو میدیدن یادشونه فورلان تو نسخه پرایمش یه تنه کون همه تیما گذاشته بود، آخرم جایزه بهترین بازیکن اون جام جهانی رو گرفت
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/92035" target="_blank">📅 14:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92034">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDZKmeHScKqePK09h34Yitu3wKkNBhfZcEURgD7iEUFx7X8kmfWxBi-CWKZjzQHaTKlhuuVj96vXCDoSGoqfgGhfwoO640WUKBDtqS-E0ajIABwefglr37QZlJu5hE4QXz1EC13sawh18J6-N2Gg9pH8N3YlpgdGxlabvvtbbaE5lJUA-vPHayFPfjy-6cbNBr37TANslRiSNWKNgJ0bBUuSXyxrqOirjYCEb6F5zGAFeID5goMbDg7g4uKUPBeGW0cfZWkvLXG5_8bL1MT-ThJLZ2x4iViVwM_Gln3Vk4G5m4NUs660IR-uz_VFOOIcDCnEoHSTMU0fwyKo_4xP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نویر از جام جهانی 2010 تا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/92034" target="_blank">📅 14:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92033">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0LOqq5mVYYGAheyo9Sec1ImUD_ERTqNj_rAAu53M0xZI4WHP3VXVBmucgEiAEBP-MNrixA5Cjvc9gdfzVyl-qkDIP63bJTa_KBjjwjvsUAtpRTkXIl9hgmw6z8PlDsZO-Yl1nj5QSmtiCcYbPHZF1AX94HzZ8mnQwktYTjYL8OlKPmMSr39SbcYEzvH5aekUSXTth1n1CY405NU2ZYXns79hRs7_8OeFy8LvHmd8eaVuEwTVv-mTk1tUmDH5afeYxUuhTWa-VCFEYAyOGbmZW7PLtMiN9WcBomlTbN3QdwKdL4r6PW4PZXY6TVN1NShLXfx1jrJNtrF9JMvj7wSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس‌های اصلی قهرمانی جام جهانی ۲۰۲۶ براساس آمار اپتا تا این لحظه؛
اسپانیا شانس اول قهرمانیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/92033" target="_blank">📅 14:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92031">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdWVrE85iwLV5BIgdAJfZIWKY7CHT82l_DpXAB446aBcK0b42sulgYWIk1ieIqiA8MhtTe7eUWpe0W2iCDNOdcqnXijrIztAP6bEonHzoau4WzNP420SgruK7YzBiXPjzc_Vy5pSo6huJqX82OLPqcLIXHetD1t-CJ8YKJIrJ7RIdSaWv1pKclAp5v7NdU8rwn-uIQcHAfSE5ohGmUQmp2grXAIPQC_3VODbyUd3cc2fHjnTNj7IlPcRIHozAyN_2WqquOQHmULlcFmgyBY67hG9gaOOTdDvv04dxUczSEVC-gUnas_HC_Ok1CwsFuV5OgxB4lbBC69wpEnKowqVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtRDnSoeYPxaxi9JiuJZwsRXD5nc3P8zYuFTFxCxtxgF-gGinPY2PCqDfLWMrlldmAh1XFBlR_JnVgGtb89AD7MWXJPvREOIj2ezS31MZ6rW7-xbXHCW4f0nq2ffYYNQJhN07fCf_Zbquxwnojpo00Gh361kVvPvFl7ZPp6jSV4IJ8e2svRezo_F-qBeZSbN07UJn8khV4097KBRWnFOpNk6BWW-7r5mWG1YkczzbqCCi3pa3M59pgFD1Osjs6cWPaVfTmcdftmCub1WxTrnfRJT5kU3G-Q1sOKdwTnHHrpW2oOt34EHP1nIkcu31XKDDY46U3jZI-8eaHCfQ0ozww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکوردهایی که کیلیان امباپه در این جام جهانی به دنبال شکستن آن‌هاست:
🔹
اگر دو گل بزند با عبور از ژیرو با 57 گل بهترین گلزن تیم ملی فرانسه خواهد شد.
🔺
اگر دو گل بزند، بهترین گلزن فرانسه در تاریخ جام جهانی خواهد شد و رکورد فونتین با ۱۳ گل را خواهد شکست.
🔻
اگر پنج گل بزند، بهترین گلزن تاریخ جام جهانی خواهد شد و از کلوزه با ۱۶ گل پیشی خواهد گرفت.
🔸
اگر به فینال برسد و در آن گل بزند، اولین فوتبالیستی خواهد بود که در فینال‌های جام جهانی ۵ گل زده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92031" target="_blank">📅 14:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518369de4e.mp4?token=nJpNW2Wa6NvpLSlZ2VKF_Gokbe0aV1TAVSQHnHcxIRqXF6hURQCeCzQaPF6Nz_-spRVcyXpQp_0NpGeZDRfu3UAWj3t5caLkj93ixPFdNDib7i7EzATdEmTLerD7-SocqIiujdLNNuUV2EZfvlEEU_2i3FH4SDGdxpkfRN5vERIvGEeRiCox0sAcmgnm8WDFn0Er_VwT_7QZygbkEb0OWMOFX2Irsca3hRJLFdTdQlbA9C5HF5xu_53vNH0VgkapWYW9nlDNM5sZ1XuENg-c-bsm7UlDOstqzeFhrWYiXvQP50-qfDfzZWdop5TZJfAJG5TFW3UvaKh_9nhTuhXXtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518369de4e.mp4?token=nJpNW2Wa6NvpLSlZ2VKF_Gokbe0aV1TAVSQHnHcxIRqXF6hURQCeCzQaPF6Nz_-spRVcyXpQp_0NpGeZDRfu3UAWj3t5caLkj93ixPFdNDib7i7EzATdEmTLerD7-SocqIiujdLNNuUV2EZfvlEEU_2i3FH4SDGdxpkfRN5vERIvGEeRiCox0sAcmgnm8WDFn0Er_VwT_7QZygbkEb0OWMOFX2Irsca3hRJLFdTdQlbA9C5HF5xu_53vNH0VgkapWYW9nlDNM5sZ1XuENg-c-bsm7UlDOstqzeFhrWYiXvQP50-qfDfzZWdop5TZJfAJG5TFW3UvaKh_9nhTuhXXtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🏆
تمرینات شکیرا و تیمش برای اجرای مراسم در افتتاحیه امشب جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/92029" target="_blank">📅 14:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92027">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec269de90.mp4?token=KJAugX2mCLb9zP8KxK7toV4KCNoyniWRszpJc-NHlRgGPeCORoCho0MdF0HSFAbKwypvCIq5-FbWO6al1y4LJ2CY8Nb8izXpiGo-5hE7P8G0OQHJGlbo-SB8YkJn_GmHAgBrQVCJz23y0PLYU20Lq9wSf6gQqzE6qw7G85OppF8sORq_sgvesojPKW2GLAvn8TyAVuSUM8d7k7_CUxih_NjEwFOb2b_vCDILhzWMmiDEHKsrel6SdOTO8FvS5Tv4WbayXSecQ7UcoN0wLHLhM9-g3gc9tiT8YoEwf6NehxnPRb1p_42UjL90D6JtcJuseLHhInTP8-_0gT1lmoclWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec269de90.mp4?token=KJAugX2mCLb9zP8KxK7toV4KCNoyniWRszpJc-NHlRgGPeCORoCho0MdF0HSFAbKwypvCIq5-FbWO6al1y4LJ2CY8Nb8izXpiGo-5hE7P8G0OQHJGlbo-SB8YkJn_GmHAgBrQVCJz23y0PLYU20Lq9wSf6gQqzE6qw7G85OppF8sORq_sgvesojPKW2GLAvn8TyAVuSUM8d7k7_CUxih_NjEwFOb2b_vCDILhzWMmiDEHKsrel6SdOTO8FvS5Tv4WbayXSecQ7UcoN0wLHLhM9-g3gc9tiT8YoEwf6NehxnPRb1p_42UjL90D6JtcJuseLHhInTP8-_0gT1lmoclWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
ستاره‌های جام‌جهانی اگه زن‌بودن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92027" target="_blank">📅 14:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92026">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fc15b62c.mp4?token=j2Bg9k5xsnnFhpYadGDC3YmYboCu-IubHnOFYTnsnrRjKYgo-tD2Z_7OXnx3PUBbjwM__5UuBkPX_C3pA9w5F6GxXot_U-Gn4SEJz5xYl_MLOGSnvCf2sbGqvasoHSlQIFM9NU16kj9CUmB3FDPX9uyRifYsz4S2V-ShKrqDO6BrRsh4pzRO_S82uRM-ArCdlSbJnVqPkIA5pLCSKmXdAreDKqwG3wype8DFj1SdI4ogpoVbGufZywlS7jKLmSr_MsyIlbcCiDucyh_cwT1s8Qyzous9_xx6DcKRqF06__aovp_F3iLcv3vHrVo3x-IKdBSGQ1Wkva8x4ntSw5Gd_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fc15b62c.mp4?token=j2Bg9k5xsnnFhpYadGDC3YmYboCu-IubHnOFYTnsnrRjKYgo-tD2Z_7OXnx3PUBbjwM__5UuBkPX_C3pA9w5F6GxXot_U-Gn4SEJz5xYl_MLOGSnvCf2sbGqvasoHSlQIFM9NU16kj9CUmB3FDPX9uyRifYsz4S2V-ShKrqDO6BrRsh4pzRO_S82uRM-ArCdlSbJnVqPkIA5pLCSKmXdAreDKqwG3wype8DFj1SdI4ogpoVbGufZywlS7jKLmSr_MsyIlbcCiDucyh_cwT1s8Qyzous9_xx6DcKRqF06__aovp_F3iLcv3vHrVo3x-IKdBSGQ1Wkva8x4ntSw5Gd_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
🏆
🇲🇽
برگزاری تمرینی مراسم افتتاحیه جام‌جهانی در استادیوم آزتکا مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/92026" target="_blank">📅 14:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92025">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZ9eO7ztf99Xo5uUrc68ZcCUD4CaMR4mjGjcuocZbaLVLY4v-tBqpaZIp3vMAuXqc7KTX25zp5AJ_0-XMymjDt5HT8IuLUD2ZAp1dRht_3sIpgs83ftbmTVwFl6VQ5a2UAwOGXjeLjPoPxIIQFE9lBhNmibIvwAIIneBSitI0ZIfQ1vKwT9u87ozEZMItH3Xjc6o40_MJSNJWCauoAhJ0i3TQ-_Z0Z_cUOmUhhpXtWiNzy7prXyl0D-qtLggxSfiEnOwBJCNmLyPB6qtGcrIol2aBL7LoBE2PEy9Ju5h7nH1dydcavpFCdnQypOIg5j6mV7VhS9VCJTDJHJgfkSKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تابلو رسمی نتایج‌ بازی‌های جام‌جهانی که از تلویزیون نمایش داده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92025" target="_blank">📅 13:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92024">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4165d542ed.mp4?token=gep-0vsbjj92_s26SLeVzsiWKmT4DS2uD9V1KEx6oVccm_dFF-7XIPhd_A1uq15nvX3EhDkLZQJgsho_ylUroKlrSzwtF0_0Zwmw9gXp_svYqKJPb4LmSgpOImiYXg3bSW2InE1ExQ09GbAFKWaWH2p8Uub4GuwPjcHbo4rSTw_po1CM46ch6xuTAcc_MN9WC8gfapD1YQ2eyhd0dWXVxg9AJYFi0bPs11YrEtQynpB3UQGLDiksdGgpC9tXrC3R5n0p4ip479e0Q7L9YfoaW_Vz4ApmHaKNapKKK_GnoinwIkQ3ST8Q1BVQcglDNzQAPzk6FyuFHuc-De0Jdf2SGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4165d542ed.mp4?token=gep-0vsbjj92_s26SLeVzsiWKmT4DS2uD9V1KEx6oVccm_dFF-7XIPhd_A1uq15nvX3EhDkLZQJgsho_ylUroKlrSzwtF0_0Zwmw9gXp_svYqKJPb4LmSgpOImiYXg3bSW2InE1ExQ09GbAFKWaWH2p8Uub4GuwPjcHbo4rSTw_po1CM46ch6xuTAcc_MN9WC8gfapD1YQ2eyhd0dWXVxg9AJYFi0bPs11YrEtQynpB3UQGLDiksdGgpC9tXrC3R5n0p4ip479e0Q7L9YfoaW_Vz4ApmHaKNapKKK_GnoinwIkQ3ST8Q1BVQcglDNzQAPzk6FyuFHuc-De0Jdf2SGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇺🇸
واکنش بازیکنان‌ تیم‌ملی فوتبال آمریکا به کامبک باورنکردنی نیویورک‌نیکس مقابل سن‌آنتونیو در بازی دیشب فینال لیگ NBA!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92024" target="_blank">📅 13:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92022">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7053e2c082.mp4?token=WpC0MltLumg4eu1k7u04MnebppzscgYS5pKLSsMz5dN9Ff-tamob6JVUBZfjpLIMBMFw7fsg3pio5HuBC7fM4Vcvkfbtm0Zve3-GKO2RNsXYh4tHeujkJyj19Xgeh42qXoqnuSn20HTnE6V0oLuMJBWCFSOBAKDFyivaN3EQ8GxFgR0SFJVppc5msrL-CKQ50TEQL7dyrY2rWTk0DtTKmT9nAyq_RhdLJCKIsiK9QrFMNA68_Uw9q9UE2CuTPwUgUgOWair59Co2w_YTNCqLpAInCgOt2UD4SJ15OSRFlpNWp9qRvKV2uaGMFrgJK_asrvXjP0Qo7yMIstmsNyZBF53_MGFGAKReiODn1nUhNnUPFV9p4Pal8x9Eh7W2XFKzF9uqagawJWuXaEoJ2g0c_jNskDFUpSUmHTVHBjpLCWKRx8rIyySvwWPe0-tuT8Je8k3g6lTLB6abNDAhIFIvuqadVYv81XC8P1KrXYaiUPKC1bOyVLwdGI0GbBtOjE6vQNTy5f4TJmt9YH_x8NHmPff8Dl6JEgP5IIz4jS6wOXJU8uQDO38NnPTplBEvdzoU_FPePhmPjF_-P-p2wJTB1v1YwQtUmSHBILFAzw3Q4J_PrQl6FTQ3nlFxAeizABmqVEN1FNjYUXoZvV0yr3u7Wyaoi1lKPnMdVlRky9xB6lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7053e2c082.mp4?token=WpC0MltLumg4eu1k7u04MnebppzscgYS5pKLSsMz5dN9Ff-tamob6JVUBZfjpLIMBMFw7fsg3pio5HuBC7fM4Vcvkfbtm0Zve3-GKO2RNsXYh4tHeujkJyj19Xgeh42qXoqnuSn20HTnE6V0oLuMJBWCFSOBAKDFyivaN3EQ8GxFgR0SFJVppc5msrL-CKQ50TEQL7dyrY2rWTk0DtTKmT9nAyq_RhdLJCKIsiK9QrFMNA68_Uw9q9UE2CuTPwUgUgOWair59Co2w_YTNCqLpAInCgOt2UD4SJ15OSRFlpNWp9qRvKV2uaGMFrgJK_asrvXjP0Qo7yMIstmsNyZBF53_MGFGAKReiODn1nUhNnUPFV9p4Pal8x9Eh7W2XFKzF9uqagawJWuXaEoJ2g0c_jNskDFUpSUmHTVHBjpLCWKRx8rIyySvwWPe0-tuT8Je8k3g6lTLB6abNDAhIFIvuqadVYv81XC8P1KrXYaiUPKC1bOyVLwdGI0GbBtOjE6vQNTy5f4TJmt9YH_x8NHmPff8Dl6JEgP5IIz4jS6wOXJU8uQDO38NnPTplBEvdzoU_FPePhmPjF_-P-p2wJTB1v1YwQtUmSHBILFAzw3Q4J_PrQl6FTQ3nlFxAeizABmqVEN1FNjYUXoZvV0yr3u7Wyaoi1lKPnMdVlRky9xB6lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏆
توضیحات‌جالب و دیدنی محمدرضا فغانی در خصوص تکنولوژی توپ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/92022" target="_blank">📅 13:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92021">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n64-hMNgf-JUp6imbTsk95kyB8IqzBsuIesgi-VhdTuuFypbzgcqikvhfYV1guaK_gT8ijngO0yAKAC6ji-Sh523R-EG9i88i46Jka61tjJSfKCs-naA_9Tja216OIkIsd0NB9P0B9JomCZK-9aF-ffDrIpMNFpd1I5m6_vkTYiE7DgUosZya9dCipVwwRPZGunmWsbP3HCBNE_as3_r_w5xjGvdT7DFtqVGYzTL1FhWoqPbtubijby7iv8Q_8hBsmYh8FjqD_VgEdEth0YEO1U7bD4Fo78M5swAT-qny2V_pdotikmN6l5UdSHM3uSNUE02dd8WQu3UJuxxTi2DFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇭
فدراسیون فوتبال سوئیس از وجود مارهای سمی در کنار محل تمرین شکایت دارند.
‼️
اونا در ساعات گذشته به دنبال راه حلی در سریع‌ترین زمان ممکن هستن تا به محل دیگری منتقل شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/92021" target="_blank">📅 13:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92020">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_53cufKO9TEZ71oD9CWg8b752WJqJcLAsrUKjSNh1ZczEuuBeuZjTVMJJRwtJJ4QQ4Hfr3Pc7tUZAtxZaKlPkD8DJmgOK0Cfh0TyRLhsDW0RC6v8IvVoi5q02AIKAkrPhYcL1-u93FQKwMFLrL7xDd6qNKYj0Q5WCQXNme1T-ETu8mp7pVGbhFuaJlngCMrnAawMRqMqyqNmPVf3UrFnFFGIn3tOktahhditEGO5BZU61iT1JGNB-eqF3v38J-dYew9wgwPZXWV1Mk71Etfutset06IF1-2riFk7VahfGZGJQyWukxYP9rgMA1nlatoYIAsg-v27wQU0Iio37uEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇧🇷
رافینیا:
احساس می‌کنم در این جام جهانی نسبت به ۲۰۲۲ بسیار بالغ‌تر و کمتر تحت فشار هستم و میتونم عملکرد خیلی بهتری ارائه بدم.
به نظرم وینیسیوس جونیور اون بازیکنیه که میتونه گره بازی‌ها رو باز کنه و ستاره ششم رو برای برزیل بیاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/92020" target="_blank">📅 13:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICaj7ENNA5sueidZOlO3WKxehEctx0f54Ed_VOjWMjcNZfCXkQI3sWEyzvo0qX_SRfkTJcyxAQNIgTiHd9I7m2mOO-I-DE4YD3ky_KoFXQKw_c0pzFpXTsv7eQMpkpqlmWyM3xFeTnlB74uHN1B0F93O5qzGEeD31hGvyWNBY-rJYRyrXMs9x_DpbrmefEaMCqr5hh6IlTu-aYyR3Z44DuUjF3boMzn7h95h0qwXcXGYLfA9iIXwksioc1eC41hY-L3gCCR8GtiwKqlyQwNouD1nFpbIQ5cAOkOvgPeQgwtazOvXCiA7cNP-HCrf1GlR2pX-5EoFimAxJG9uQYDxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyEylk2rM3-ZV9fk_ll4VOH8xjblwQpASfkRR8z0ks7Wr44-GNVykeZl7r-XQnhooDklKTGZvf1UJqGPx5kuIZE8LzP1UVY40u_oq8UDaLfEYDICHLs-HuKfJdgcWpQ_U0QHvfvdCkgTta0zbppFxRPm_g66_CMrSgZSp9DhjUzRlYFdJc1-axO89oPzIlbSsp1S8E-br7DI6rZDbc86L2IEpAVGYGxibXY3i807V1lBX1Hq41dk1xfm_y72jUgVo4t4FzaVwgAYNGLMwHYSuIOQwpEsda7sChh1Aum-7BGmG4UUX40ah9nuaYzlB2yqNzo4dmO7x0jWHlh26PSllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oyQY1lMsG7jNA9nybKkmSyi9WqUsxYT_auPXOAk6w5nU9aSliIFQAWeE1c2BwcG0h6imfGrkM198vwABG3pY25KPi5CyQa2VfGdxorVWFFg_y6LSHw5pLBp-CjKG7FgVz4cl6dzXZnghATHzqTLfWP5qIvsww7hBhFebg7VG5Kt3lehjF9Sie6VofjlCKvKG3if7jGRtNRFzZEa3RRvPlKLlb3yA6M5N-siZDxqOJu1-OH3eqBVZzgK1sEPmS3zEuq48ziIwiTb-vr5USmpedixKlFXyEXzabEti9R0yww3S22Vah__eL5fVzBMmorOvJfopfZtpgkPqKZRG06qnKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شوخی‌شوخی با مسی هم شوخی؟
😂
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/92017" target="_blank">📅 13:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7862oLBIY2VqEjx1jbOGkol0czIr0ifzRNYJN-UYow0LJNzZmG9rv6YWQkCAtAG0hH0fBw2Aj6A4U9-K69Q9i4JdvgH7upvB0k2S4bec3-8VLr2GGDkgtJ2mNpbTHD_CarqmgR2yrQ_NnKDuDtjor4SNZ2HZnmaca2p5cel7d8Xgy8BUXeFEYamtLfy4npFc26HBXvCmDHulMaUy2L6Ms2ng6o2_OtMEter2w2aPBd3IqFpzJvK9u5ibdm6vDUY-QE226QJ6lhDGJ6LkmGxSBv5S_9qd2Yf0hLvQ566XKtc6eiMIU2IsjDEelMFElYfzDWLoaLoc9SU0fuwfU9bkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
👀
مسی یا رونالدو؟
🚨
🚨
🗣
زلاتان ابراهیموویچ:
- آیا این بحث هنوز ادامه دارد؟ در سال ۲۰۲۲، مسی در را به روی همه بست
🥶
❓
خبرنگار: یکی را انتخاب کن
🚨
🚨
زلاتان ابراهیموویچ: زلاتان
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92016" target="_blank">📅 13:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7WJ6qirBUrCMfF3MBxzXDgY57d7FRAYJEDUtyZO_vX7lHEpRVR2L9rAdSwfI8NaRJP2wFgTUKTGkfcv_knQac-ZokhTXx2GHTrj4M2PdcBquOsmYlisp6alrkTDRKY6ACvvbaX-RGGgmLgldqPFwQi2SolRiqI1sHvwYHNmGkLPrc8r-mYIKdghIounLn5QTXtiP9KQW-q2TY7q6tzfr5DuG2Xri-k4VkEukeTqSUBTuP3nM_Dgp2cia7YruTxafl1wsOy6UfGEUAy-RkmHn-MrlbKgyxPgsudI3NXPI8rcaw6VqdDXgzVD-9OzNxRB98rrfOH6MzX-tZZuGrYI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
شانس‌های‌اصلی کسب توپ‌طلا جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/92015" target="_blank">📅 13:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92013">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klJU278LxeQUqVXhcFYD2Z8w_Bo2f0CQ4C1Du-9xSSOt8FaQXBmt9fhNLHehpdPuIlOt4GsZ-RYUBH4brapzQrQCnVkwzBI0fDuU-8zeoPbv3CH7diiC6uGyQMhaJmMCVJE-jNzphI027Pd5T7qrWRrPSKxxBgjcx3prAjlnAm82BqNodT6mbed9QC0ozcnWj0RkCCxRgNtinG89QcStyj2DSQ40ns8qsJGaf6U_nDXb2BCCGAOGsjOTNkewx_C9l6UERA_rFPkv3cRIXrtLVyAMTpZmIUbCnPRwc0e30fc6xZJmUuqf8P9V8Nf7zGCiWtj1a1EnJi3CvD1Xu15KGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brvKGqnhdyxOkg8tnfbQ-vUgt5RmY_RHdRvjmfir5E8ibyw4XXj8CGih0dA007AZh9IyZvYYGtNXaax63PYOnu4lz90ZgDVyoVsYYQHnqe0Zf39Fnts41eXmkng_rFWDgalnC97uHifftqyUMgHoRbb6z8AwGCMzpA_TTXHC-fHIwfn7mcmZ66rReeXsHr8WdHTZ6ATVlJ5SOyMZoNDBdnXAkcCk6zaBn7hfFxdT7pHgNSRoyfbrKUbPdIgqFNcZRRcv7DH1wH1CjUSmzpLdmSox1C6XJysYhr9A5FEaKJI_iAwpvnrFu8sh9H0kIe0hisp3rQQdJmjIrNz56AAclg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏅
🏅
🏅
نظمی گریپشی مهاجم آلبانیایی روبین کازان به ۳ تیم استقلال پرسپولیس تراکتور پیشنهاد شد.
روبین کازان با این عملکرد نچندان خوب ۲ میلیون گفته میخوام
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92013" target="_blank">📅 13:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92012">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcC2F-kQKhfFTgDcKPRppZUyEByqLCrZ7hAkHzl8TjFzVO80bVKgCOe1ozTwTxqSLwMlKiUzZPe5j98Ccs0cCdq92xu5lxLpScZS8jnthgutl11ud6PL1Tx2G__hPsvx2ZUWf6sRiElfJZp-qGW5SkUEWCsB2gDoluavOkRe0ELj1QbN5AIo_eHQZ80s6zMGpSt5zAFSWd7vGmpmBuk_OS4VC0t3m2FAApaMz8EQKShTk8jmVkoccne3AlFp0TIEATJdSGooy5-haVc_9GqI-bC2GHYHAhPnCp4Nb7mY6MuhD7B3zJVKlW0s2-waOGeiGUyy1wm57JUHd-vi-GTC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی دوستانه بانوان برزیل و آمریکا:))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/92012" target="_blank">📅 13:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92011">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsGsYLe1CrZQR5M9sM5-tGCm41u4WXZ0IytwwpJ_rd7rWeeopWwxgrA25iIaiIxQalqEo8URqUCppt3EsSz3TY7PG4AjIjm5FjPsAi7sjYA4IM9J4sBw3sfv9tLMjRCHVOwfT90ZCHJqX-B5AfUZVgSrcNJKSRYFlpC87RG3pFlm9ZzErM56KVSQ2TiPp4ABXFUOeC52uSSBnoVrk5jJoUaiI7GCYixTR9K9POZA3m7ApU7aUpJTCm6DyDQIeABKboAn2Qsn4pXewwYf3kxaNG14eci_64CyXQiXitUVB4slxP-QSgQMMtbF-p9XhnH1ctnYS2vbHuWx8RoEbx2pAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌍
🇩🇪
🔥
تصویر‌رسمی‌تیم‌ملی‌آلمان‌برای‌جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/92011" target="_blank">📅 12:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92010">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🔵
تاجرنیا مدیرعامل استقلال: پول یاسر‌آسانی فراهم شده و تا اوایل هفته بهش میدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/92010" target="_blank">📅 12:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92009">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad367e9fd.mp4?token=saarVUvrQAgnuRGB3wSPfWHGBPFIYwqNq1wxvwtTQ-5on8-Wt4B8sSluq7AzNgwF8g3c3Y_zmlmrAhmKdv4ljW7AdTzeT0yY7ZFhhdhYTPTbjme18uzJ1uT6cU---a_WTxIj3aQioYu7_LjIpLOoTJ-HUwtMS-aDrr_Qt_Y10lb9Md-a_rTzUg5Vo7G3HaJKSjCpesa11-MsMDUj7j1MKNsI9d6yNGywE6B4iB7IFKkNvrOnl0D99i5VjPcxjjfyhHnVsBDcABT16hxVkPYtwr6vE5vJLbq9GRysWNTa9kqzaq4E8DDF0V0lmYlvz-pQKOxTNtbKyde5hKY7TkuDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad367e9fd.mp4?token=saarVUvrQAgnuRGB3wSPfWHGBPFIYwqNq1wxvwtTQ-5on8-Wt4B8sSluq7AzNgwF8g3c3Y_zmlmrAhmKdv4ljW7AdTzeT0yY7ZFhhdhYTPTbjme18uzJ1uT6cU---a_WTxIj3aQioYu7_LjIpLOoTJ-HUwtMS-aDrr_Qt_Y10lb9Md-a_rTzUg5Vo7G3HaJKSjCpesa11-MsMDUj7j1MKNsI9d6yNGywE6B4iB7IFKkNvrOnl0D99i5VjPcxjjfyhHnVsBDcABT16hxVkPYtwr6vE5vJLbq9GRysWNTa9kqzaq4E8DDF0V0lmYlvz-pQKOxTNtbKyde5hKY7TkuDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حق‌ترین ویدیو نسبت به تیم‌فوتبال ایران:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/92009" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92008">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">1xbet_ir.apk</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92008" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92007">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1️⃣
▪️
نسخه آپدیت شده اپلیکیشن وان ایکس
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!
• آدرس سایت 1xbet:
🌐
bitly.uk/connect1xbet
❗️
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92007" target="_blank">📅 12:47 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
