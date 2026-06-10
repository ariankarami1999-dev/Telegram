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
<img src="https://cdn4.telesco.pe/file/S7F72QmCcMignJQwYJ957PtKh_B6xkSLNPTi-Xtw1sxwipbJDiawWGBOtKlnalxhjy-WbOgjouz1wX326XOknVklEk58MQA0CmmYz7XVfM0Hs3OSV3gk458Bh5olzdiwb3p71Hp61iwJxufpbM_gJ6e33-Bvh37hOawS4kcFRmajkPWRKjsRqDcZn7MmBE8dAIr-XyKm5YvKIjJUilx4UWrk3uYVPGFr546HVnd7n_yfuXi3VVxckwL-a53UqftUG_so_VqP0ZQN5EtLjLDMkLfjFPqT0t9K2dtrZknaC9qqlEBVSOyWvj4SJ_0pL2ic7bj0_VgFSKSB8Jz48wskqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 196K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 14:36:43</div>
<hr>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4HyyG3mghZSaFcp7GeRB_4Dum4_Jir2AXdbChNnOiujTMmabl5jUOJacmAicUch2-nej-hxqXuficrqiTfcNdsKTj7-K3AaA6Azhf6siXfuVY9Z7Prhi2AwOUgRsWjCombRaBj9Z1cP_pFdP9a2jsDb9Xx2VkKaBEgt3mrchVY2lwRwHZT6_Kkhue4LCe8wS8AJQsM7yyCBIy_COEychUKIxmYehu-87GwAZQuelvoOeUO2KJGKQm43_lQrtVTo_4EtrpQGbjIBM6MdRJPpWvb-PFJpTL-wXzM4mF4-qU-dPCRhtw_shtHnD1dw12Kud5YFS4cRd0rmap6-LS0Gsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn-AThZy_ITnM7ywhTQ06AXefEu2BYKM5-_Ixs-3FlECkxkCZOp9MHnv6MUHqrDfcJ9q7msv3eP5ueFeyoxSS307H-lxucjr2ZAt0WfqPQAG8bLRf5bfmDZU2j1aIemCvX7w2Uc8y0cVyhJDIEzElK_CK1LX66FNK_Su5iMjUpuGkpZze7IKA5Ks1i8Bit8-zIUPFnweQkd5WB1qgtsGisR9ku1bzc0nDAdXt20M3jh1n6DXbA4gpkmjpZmO4tdU3a0gtBA0cdsKoe9HA4Ud7v9RZKNy47jjDI1HFdyVLVE10q1i2FxPmaLRlo8Wfsdmi9Ezkcc6NM_jSBEPBwXSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=FWvQPRbaGrRwrlH5hy2vPMtC0dOA0i4QB0gIcnDQjNXDISspbnJYGEnZ-TSo32kvvPNQkvhu7VKlUz0q-L2Z3vWRDb5GzgqDRy7_hVoVthR3AGaUuFVYRizPtUKNUCZvXfRzcqUB6QiyLWSs0itw7UwZ_GpUjaG_VMaSYUU6_u9t3W4qrOxWnxQl7ANNfarEgaqWlSsX5az9__wKjNHdGHSYfVmTurEOKWrmjXNeWM2u7KKhFAXy8bczG1KWq7X9Pw5_XklVBIiynyhUg-jFK6D2gN7p87j3Zt6ppgcIQju99eWwvJwYH7SR_-SxPsOCxp4v8o64S-89wJ5AOMvC14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=FWvQPRbaGrRwrlH5hy2vPMtC0dOA0i4QB0gIcnDQjNXDISspbnJYGEnZ-TSo32kvvPNQkvhu7VKlUz0q-L2Z3vWRDb5GzgqDRy7_hVoVthR3AGaUuFVYRizPtUKNUCZvXfRzcqUB6QiyLWSs0itw7UwZ_GpUjaG_VMaSYUU6_u9t3W4qrOxWnxQl7ANNfarEgaqWlSsX5az9__wKjNHdGHSYfVmTurEOKWrmjXNeWM2u7KKhFAXy8bczG1KWq7X9Pw5_XklVBIiynyhUg-jFK6D2gN7p87j3Zt6ppgcIQju99eWwvJwYH7SR_-SxPsOCxp4v8o64S-89wJ5AOMvC14WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWqIaJoibJZpydx-wY4dnG6DOxJDY3Kh8OTsCgDodyPFDmIK4Fmz_ipcrWnAper9HXd_3taphRIGO922E35odezWxAZcfELV8VXL1pHkvGQD7q4Jw2G_OWYxtEyb2nPRcGqfgixr-i4HsTcEHEybWgCzhR4NJsB4QS9_GxfDSLPs0qdsVGhIjAWnaumZBce_iw_SaRBnhgKCijXMoElm1QtiE5btg3tU7n6KRfdh1-cjjqa-1ruIzDBk_Ko3kwD_sS4gweX1nlkW6QyogZgliA0uY19uQDqZk2Y6B8Cb8sU2I9cIY1JXKnX2KSyTl3OeUaUQrTfpXuu_jaISh48tuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVNmRPlt_bPTFQT8D5uurEueZs--AILFuA5qA3p3aSC-9FoMFvn5oWYWvX5wLlZ3oF6fRN9dOUlnHjsHwZvcoRK_xau8QS4JTTSvZ4wcVTcEib0MN5GajQopmcFKBbOzEfKWmYP0GHNhRiiVSuvbelWouqgd0VGuHZwnQt1Ojbj3AoiYjTv1-ad11gQGr6Bms1SkZ8If_dE9U5n6vdB4aI7GhsEKamNF15h4l75NEVfrP_FyptenKYZyT5WDtkfHg1JrkdmKG946lM6eRlCZhglyWty171HP-34t8qXpp1GXKE7xPKTsL1-qb89_kQhuOYeUEOFbK6qvfp01sz-RDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/23111" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=DdjEM1MNbsu_i0jgQ8f-9MYnQcB9DqM-b8QSH0E2Rlf0qah4uylPh3HEP2DqNoUBfDbx2oTf9foRxV39O077kMAlBv8V4UkEKsJKeyvgcfrI_NmbxjQxduIJ6idl9Dj1obS4-PL7T9uzJcDYvjZJ1cj7NxTqDuR2YG9dZfnlO8fowVpHJYLDxNR6uR7phaO0-PJwnjyiOs7npCJzG6OqXLpx6gPOTgE-AaNZDAlSzVXxLMyeK5HTbcOwoAHkiYxYDVWic2D_LESFNMiKbI_H_bZyXcGbN4Yzgrf_ahnotOuKFYvkgf1Ukw8LJChyQOA-epKDp3CdDuObyWo_ir0r5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=DdjEM1MNbsu_i0jgQ8f-9MYnQcB9DqM-b8QSH0E2Rlf0qah4uylPh3HEP2DqNoUBfDbx2oTf9foRxV39O077kMAlBv8V4UkEKsJKeyvgcfrI_NmbxjQxduIJ6idl9Dj1obS4-PL7T9uzJcDYvjZJ1cj7NxTqDuR2YG9dZfnlO8fowVpHJYLDxNR6uR7phaO0-PJwnjyiOs7npCJzG6OqXLpx6gPOTgE-AaNZDAlSzVXxLMyeK5HTbcOwoAHkiYxYDVWic2D_LESFNMiKbI_H_bZyXcGbN4Yzgrf_ahnotOuKFYvkgf1Ukw8LJChyQOA-epKDp3CdDuObyWo_ir0r5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌قلعه‌نویی‌وقتی میبینه باید مقابل دوکو،دیبروین،صلاح و مرموش کلین‌شیت کنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/23110" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwY37agm-nxNNHque8yc5Gs4MEQC68Ozo7dQLa1pZZqErHc70iwFQ7FuhffCtavCoeXxUItsGPHOQ7LJnR8pyQ-ozSQUW_z7JsPR_tGlD_OLUTU0cP70KAQuX3L0Zl75dwhiBL1LUfkbdKkDOHkdVYoKZf8s8vQW9A_mIGOAGP1vKn9KB7zlJHzZ68GSc2hxn8l-I_Wwqr9yx7bkZjtBV6kgO0-Q4E3gW9_7rZblO02NyjoYzRzBpeOv8h4QoLSmw74sCfCU0A0U7ToEm77TuvbC7KjpABsGUUM04svlmp2FRV7QRsYv9VTXwq5zCgbkcTrSFeLpv7W1esGEUCjBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
دیمارتزیو: باشگاه رئال‌مادریدمذاکرات خود رابا باشگاه آرسنال برای‌جذب ریکاردو کالافیوری آغاز کرده. کالافیوری خودش برای عقد قرار دادی 5 ساله با کهکشانی ها با پرز به توافق نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/23109" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23108">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMgoqCFQmv_z1wKMw2NLYNHiNEgg-xRQVVKP6gB3vv_qmiiLwg25PgX9JT4lEE--dqLToDtk1Q_cDtownqvIUmUWpr5gxDMahwET3VtRN4bC7yXvgJCHcI7lYvQxpy6rEqWZcVE6aT17c0ooaKYRWRytsya9RXhLirz-hL3QCYG5HfWYtvc5VtWjE5-SSv9WsaIztfEPtQsOcK8lQDkiVO2AAeZVk_FGaWvG2vC8Y_hgvOsj5RW3TckU7WEJEcizdX7LBW4ov0ynRBa82Aeo9-hLesGxgJcjwV991kfpVxxiLxZcGpBgRHP45vYaRkX-LamAFSzMIWKN2l36F3vFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/23108" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuFUJZXqyes2hn_XQbatDwqpfFGI3w4b4yWR0DB_gs3KbAnRSFymmUOH4wpzRtTNf6qLG_W6l71f8sl1TlzMgOJPlgFx6RReEKZDMp10o6kZAaM9EYGuCy5TsgQVAW8M0tfkONVRScuSdkzhUPpd0Xe2NRzVOi9JIx7b07fSzion_ohsEFzXO4VOWvwuMF4DvXLsdfwkNvgrkGG-LtiFDTHjUE7YE1zH2lCcNIzgh4SGat33Ow_-q1cL0mD228mnotLG3GYnLy9eDZbRY8lIGDaQiOImNpPaWvXcq_dvpWMAXEp6-jdWruPWwtth_S-b21G1GDhqPkPpcOjnK39Fog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/23106" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1m7Su288cjAzILDNHR-W_3GfGdkx20aRBWCvdcnN7agFUcl7e4PQ6ZF7GlPJZgXRHTMF0dmPyE6HUjjbHW4T6kk_eIy2YzgJP6gXaGNSlt3yGPL8P0tWtGu4rT-6M7JU1YN3e7BxFOyIVatiTXYTqQZDx8ZsP8nQV3-iiOv_foXQa6R4uOWybAk9yPLY_7yoM6AbyHe8J9NJ7xdgHHuqacLpKaXJl3t2PDFK_zJxZwQOT1qNOAQIn4rDW0YIprPXsjiDbQ7kliSXL-Hzn_DwvEvzc1p7ippkgq6Them866gojAkR-4hYohJwtytzYukWlgFgUeoJ4rutiXUGVxHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/23105" target="_blank">📅 12:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gi0swB3TUr3riUyQjNNisMUTnHMC-58DZ65_C31RXAQhu81yyYuP7BUzgP_OwFoEKUXaji-tgyK8SaNtbE6lB6qzCwGt-kS3G7UXLnhcipToh87AL1VShu5wD280iHkILHYYXgMYZ-N2S9VCDnPcEJuNaoBMW_cGpavJ_RUocyobpzdcJIPw04f4iaUbfnM20hGiwOqr8sT1xdfLTZG5okQ2aK-m8iyT-2jIP9B6FxsNad4fzFoaYcMLQtzVE-sE61xg9GsFonWUpPAXVX4Hj0NtzRgkhdYdA8msKbh0ebX-l4DeULoPbP5iAWwUEYtfYJSrTsWbQRo96JbvWp3Wgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RB3G3JlJRYOQk0GzGY_F4Xj407jbXkDZ0Ki1OpkqjvEbtkl0irvl07-aIc5osakDJGG0_yCu65Voa3qByt8ks3qmyc19cfAuR1yhxyeQcgxDeD6IxFpclP-6cG8eMAvX7OtzzBzstXG6yK8l6lfKFQpJZBt1J4XDLLjl1MZoT7p8b2kF2Z4P3OK53sSADuMTeTxCs-ON13LbhfofiwBb42k6DpNDfagG_Ff6iJnJicPVgmsAn5Hfy8jJC3RANFot3Ztpl2DNzB8Ev_AxKQbx1Z8rHhQKNLKDFE_AxV0BYfpoUTHaIBlQ8JFnRo7L01I0SdFWDQgyyp-XJ8Z48XI9rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/23103" target="_blank">📅 11:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgm6S3dwVrxq0Iv_gJmV-6bpUMoD37ee8S_bLcf6Pr66GxK6Xe4sam-LuKr5nEjaq2Wbz0q1LQnwHNJ2JbCgP0ZQll7Ouoqle9mvouJcJ1K89XEuAUuYwIwqSqWxudLe1SY3nS8A0K8Y1kL9nvSuQwJIKJtAYyVfidmW5jr4xz-yh_dFTRWZnPB_mQDvNQdaCOzInwUsP5f8jbQrSgWtPvA-Qwdb7I1GvsIx4Z24wRPzwZ1FrN3zdlA9CTYY0NhPhsWQYUZ4ZAHZfhpQeGGu_B7AW6Plb_B2s2j2ph6wNX8-Gt2CQg1sMOVMmaHgPH9wCLgI9O1qXMaFQ5hsj62ZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آب پاک ناصر الخلیفی مالک تیم پاری سن ژرمن روی‌دست‌مشتریان‌ویتینیا و ژائو نوس: این‌دو ستاره رو به هیچ باشگاهی با هیچ رقمی نخواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/23102" target="_blank">📅 10:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHrqAePgVYUIwz4sN0O6r908xzPNpcRGE4mNUcfNqO97WuNKPY1kRINNJuja8K8moyWVLaOTCxtD_ABTMehnG05SARHNF7lLRBLK8cRk1khskTzUFpvXtUPTGscpCf8o8byjPPpS_t-QMnaVqV6mEZmhH3uloPZoC19ZfqQurgeasLmQUCarDnAwQeHkTP4-xQwZ7hmtt8y0seIOt8RSXuN33vvK14CMHbB5hW49xyyVUz6IM-1Kx4KXU4KTcbKIRPFer0N4qWBbKBVN8tG8W8Vo2de8GEWYns_DylxkUZSrWvEdEpmhyRS5naPDhR7Wha2oVDns9rPDZSI-IqWJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل گرا مدافع‌تیم‌پرسپولیس با دریافت چهارمین کارت زرد خود، دیدار مقابل ذوب‌آهن را از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/23101" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=bYRaBCr6-i7PoEepHAp95bdi_-rWC4xe6gBobb65RJhrjHW1v_cz_P_uxNa4SQOnfbHI8KFA1HXmW01XZauBaCSEDsvpdfiVTYtRaKWeCjHzcCv26C8kl_wAnLsIvT3w2pvCcSgV--M2B4nzfORpuUxO4kv7pWe9oNsQG2c0cXpdUGBFaAborq_JrrAgDH5lW0Ego20XK7Luh6GK0Cc3rC31-A70rW8QRMm2ACU8YiKdeb8odTszOsECh58s5fkJL8aV_YoQQWH59QfuXG3feEqGstLO3dwu_A8Dwu2zWOVHT544_aMwsu1yXqpM5sBjyhCAHbMgawidJywLyy_JSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=bYRaBCr6-i7PoEepHAp95bdi_-rWC4xe6gBobb65RJhrjHW1v_cz_P_uxNa4SQOnfbHI8KFA1HXmW01XZauBaCSEDsvpdfiVTYtRaKWeCjHzcCv26C8kl_wAnLsIvT3w2pvCcSgV--M2B4nzfORpuUxO4kv7pWe9oNsQG2c0cXpdUGBFaAborq_JrrAgDH5lW0Ego20XK7Luh6GK0Cc3rC31-A70rW8QRMm2ACU8YiKdeb8odTszOsECh58s5fkJL8aV_YoQQWH59QfuXG3feEqGstLO3dwu_A8Dwu2zWOVHT544_aMwsu1yXqpM5sBjyhCAHbMgawidJywLyy_JSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
درجام‌جهانی 2018، آلمان، مدافع عنوان قهرمانی داشت درآستانه حذف قرارمیگرفت و در حالی که 10 نفره بودن کروس دردقیقه 95 این شاهکارو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/23100" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇧🇷
👤
به‌مناسبت‌بازگشت نیمار به تیم ملی برزیل؛
ویدیویی ببینید از شاهکار‌های دیدنی او در سلسائو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/23099" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeHZZsyPEmUtUTfFjAoJp5VBeOVbfotiLxbDsCW0OvHPHMBFqISgY1Z_aqmvsYR9Xr8Bveq7GqfwLP-fQJxgY9jdj3E4QM8RpeHpEtFrlJB8QGef4vZUlBhUTZDc-i7M8VVpF1stdCkb0poYoYZAn5v1StIPM-zUjrM_nI0skchJDoP3wBC9p08aBjASGOco8m01CrDwGtaER3irj97pSuEAiWOW4uv_KAcCLHpO6Rt_rKVlVEQ0uGNMnEYIDgI_ObTDPDtHuvRnt6U-5tQ2fNYzvXGQjpc0eoWbGACDp8wxXie4sviYwTF2JaVmDXAUB06vYJXnB49J_kAemntS8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی جوایز تیم‌ های ملی در رقابت‌‌ های جام جهانی 2026؛ قهرمان 50 میلیون دلار میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23098" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kaja2h9isXmDyyu5UtbBbRKXhEJAjCzPUAMDFy6nbAe8Y2rbfIbEwyKxkM9TTLwv9H206MHXkctcaXff325ByE2r6GANLmhynEhSUgxxNY6_zHjV3YMlNEsVQb6ZKVlVfPUSJ9uM4qkHDv2Ml5JE2VaYh3v0oJ4mWBTka3qhcH9RUO6d9Zyr4blriFi-lxHNv8Yg7Y0Dv2UOMguHmbA84ylYCWBcAyN3Gs9aOJO1sWQ3C9azFSitsUu0GsRLPRUPRUA7DOLpcqA-LKHn0W6EaTUkvYIYZfmBZ1oCTb1CDkeHTn9pMNFF8Jlz1NZwQULzG2gTifvGO2HneqAZiEnBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان:
بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23097" target="_blank">📅 09:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=JE7pqzMyZy-6tZZoRCSGi5UMENG_1sePkofZ1Za0GMz0cPvK4mMWcEDOqjYf3jvd27rJJvLQ_COqt6kPjq8kwHzT21gLk4wgFMh73PgKnWVcNIsmj_lfJkMermiOIDGdqKn3BVpCQM_1exYFOWS6fN3gLyxkQ5fN_3uedn-n881ZtngdjqK7Usx-UMplxRjFiHlhILFcE-wr-n5tHcSepK-cJhf3ItDSucOSUzSxVlJovHllg_zNfV-pK_AfbNfDJQlYX0XWW85ahOHDlcUpzh-yR-8JytN384IW6WhdtWbjxoRtaXSNecCnaiulRwBY4uF2cW2kYyFyDmfKL7d2TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=JE7pqzMyZy-6tZZoRCSGi5UMENG_1sePkofZ1Za0GMz0cPvK4mMWcEDOqjYf3jvd27rJJvLQ_COqt6kPjq8kwHzT21gLk4wgFMh73PgKnWVcNIsmj_lfJkMermiOIDGdqKn3BVpCQM_1exYFOWS6fN3gLyxkQ5fN_3uedn-n881ZtngdjqK7Usx-UMplxRjFiHlhILFcE-wr-n5tHcSepK-cJhf3ItDSucOSUzSxVlJovHllg_zNfV-pK_AfbNfDJQlYX0XWW85ahOHDlcUpzh-yR-8JytN384IW6WhdtWbjxoRtaXSNecCnaiulRwBY4uF2cW2kYyFyDmfKL7d2TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/23096" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=lalrzfrNTtIlUTpPKXY5RF2eBtgauJCSULPXSid7goDuoNStlmBZ4plC4oWdjThhDZXt6gRcaCUBjg1ceY8APk-gng3ph3HleB9UkcANr5NcCEAkUWcUWz4pPVOahGBanXJedGngwrexfEXuecgl7U_eaPDZCNasjrX6H-tfi9pLC2YANxMro72jVx6-24N5j6V4KZTClPbxu0-TxTzIq0d4xQFEmtmfOS-auzOvIn3_m8QqJsVV-i6bxckZqxpaCfJ3-JX5rJqt4nP5YOjmhHThGPo1Pbbpj0kMXJrH7uTbXoXQA1NeCChf8G-XAs_GHorFJyj0W6kczWSY7woTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=lalrzfrNTtIlUTpPKXY5RF2eBtgauJCSULPXSid7goDuoNStlmBZ4plC4oWdjThhDZXt6gRcaCUBjg1ceY8APk-gng3ph3HleB9UkcANr5NcCEAkUWcUWz4pPVOahGBanXJedGngwrexfEXuecgl7U_eaPDZCNasjrX6H-tfi9pLC2YANxMro72jVx6-24N5j6V4KZTClPbxu0-TxTzIq0d4xQFEmtmfOS-auzOvIn3_m8QqJsVV-i6bxckZqxpaCfJ3-JX5rJqt4nP5YOjmhHThGPo1Pbbpj0kMXJrH7uTbXoXQA1NeCChf8G-XAs_GHorFJyj0W6kczWSY7woTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANE26Jvjlji47TEnt24oP7NKGc4OJpokUeBujT-_NtmB37TsLA4xki6XNgOB_4FO6PU6C4l3SPbxXlUUdOHUejN_cXN3JEOp9Yc8GQWcm6fw8SgCLhKgrDO-Ey2KkZPbovuWJ6veguacRrvjnCNljSWEsKZ6KP7cEaRAP4BeRJqiw7SEzshcqhXwMUHAV4Y3Y4Q9zxLndxoG4cR8w-W2y2WkABC1RkZqeXCsbmfTonnCMVOTiLYzgNEOtHZtDvvLono2pL0daM-WDNseQuRmirwWX8WJoL-qG2nFt2kUE5mHEZhNzZbmJIAPMygkRqeKSkyeuoKOEjxtQe70teRTUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doe6HpzWEAmBSP9CwHU5QfPf6ThasTg597v4qfLe1S6TTzTqtxravLTib2eTO9czTm2Ah1UvFnPOy0mpiK-AUf05suGVrmKgm0DdSLxdcbD08YpFl2I7AxV5PrRShH7IdshaEONBsN2UPhPMr2ipUbP-9FZ62T2STibAwVFLsVf6rEaFRjwwtRYizxzw2gPg29tIu65fwunauEEr-RoaMfTNMLBJc0wDalZmx8fiHoKcct8xitwZsya_BmV5ZJUMmuBu2gDy40-L9jdB_uA9dLBUGbIy76tqVu-C5TCiIN6n2UoZgHeJRkd7fcLUhxHAgCnSYlCu3d2-QLWIkTfKXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=HA4d4fv7K-1azLzlgghx3fgS9uZ81sy0dnRWZKbPPBZursahM6Lm1gu65vEsGRQ8KGY5Q5zu_bVnZ5xhK_6AFRtThtnUq8N8fkMKX1ifQZkVB8YNoq983MzZPAhpO84WjNARuv7Msk9NmnRqYwMCZW39yYO6ILpvHy29xxK6jZDAdhTDRCFOtEYsn4nt2lKX9NJJMZyW_uAI9eVcxgX0LAKrpn_x-62nVWnT0IwEwzv9Ywd_JeHoGw-T0TtVLf-mcSlCI9HymZmmgcutsk1P6EICJloTbP6nzeP_hVq0pt0Mue27b8D64EqA2C61sAUMK5tFYtjc6Z0CbeRD4qUZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcUtERQv1AgZCIzvtSRW2ZINcSj2t_Z_gK9XVuiPf-OvQ_fPehHUcOkAgo0CFTVP-MJt3uymcTJZiZQqf9-x6Ro1hijnvbIfJjRDyqUMD9S4kY9aWbZWxz_yOZaIZWz-XYs22R1Pv6CX_L443FWL84FCGSFXTBAPyX29EaVw4PncBvrzvED7SzIhjnTD5-WdykvYQdV4IW1_cEf2bW-1u4w-SZbtKQfh3VBaKZlsu7Q-Whux8QOeSIMa4OOslJeVu2OmK_ZAD0Qyf4_LydKec_dPenNuin_ZnvI1p6Fh0QRCHStuRIvMKO3arFA9UgaobWOuJ5F9FwwFqjAf2f4tVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bz4a1_mlJug_vAXN64iUKagOWQDlox8OgPY37iTjBLGm75T9WWabPC594McxfjtVriZYy0rzLOER8_VAUQeMaGRsLUzSGWt4qASPe1-dggs0cPF_UcGfpp936FVh6jtJP6lbsU1OicTaOQDWrCeItb0s0eVdY5oRQeGG0XW7ygGGYUMZeCO8uK_00l0hXs3kSyltx_OBjgbm2ZDpYc2x7nVVKSOQmc4twtcrN-QMjN4akG6WwTUhOV1FaQ34C5VLHALau4e6WcpcoI0Y4MiByV_NvQd1eBZM7Q8xxAWp08ICett3eHZlY4vilNggMLzG87oeup5NmZQ3_ltm4Vjytw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfeD03qy1tcb-6wbXOcoz_OBjZmtacSKMqVRxY8QDwNIZpNFMpyRAKWWAQQ6eG3khOREu0301xJUSMo00ZVYSd-zAh3l4JDEl8Dbwu6lPsgOeoRLWAGJK61KTbmTVUbUNiT5t3Dh3-kb8iiSidlpQSYhfkVTqZMJSO17Ez8s3xu5PsOH5ZuT-cxHnIPPPqAYkE_oplROqjZd20FGecKFGmtRf8-G6TV_v9p1tkrm7q4-_Pc6hjcldlXEBXVmJDQ7DvsbT7wfUsIQzwbBydy6Nu7_gF9z66W1oPD0ffKteTg5bzF_n9ymcby_YvvP4BzZ0xjoh2mvLxo2e1o4aQacyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=n7p3CH5ib-APxWqDkHb5SNkxDiFChDRFwsUXIn4OnG1WxclA94ZYA6HXy0qYTAU77QWf39coUhAguK8d9IQJ-EeXLQ3_8c1CY2h0HtIHvkN_GDBjd59FAYEzZR8CNNtgi60_70Dv4dEP45PSjYF38A7leHkKyK1N6ogFpKusTj-NkjmketPcErozg7fXXj6iHC5l8RKqY_TEz6sd1tXK-GSsgKBnMp4FS9gbKCAq_Bq8qwUFTKRoe1ALGxUxEU1SMD9QAAMg0Fb-u0pfYDoAUAF104pKxcqgV1yuZXbdu6iSJRCeJCm168sRWcg4JASiKIZASAmagn5CiK8_izVGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=n7p3CH5ib-APxWqDkHb5SNkxDiFChDRFwsUXIn4OnG1WxclA94ZYA6HXy0qYTAU77QWf39coUhAguK8d9IQJ-EeXLQ3_8c1CY2h0HtIHvkN_GDBjd59FAYEzZR8CNNtgi60_70Dv4dEP45PSjYF38A7leHkKyK1N6ogFpKusTj-NkjmketPcErozg7fXXj6iHC5l8RKqY_TEz6sd1tXK-GSsgKBnMp4FS9gbKCAq_Bq8qwUFTKRoe1ALGxUxEU1SMD9QAAMg0Fb-u0pfYDoAUAF104pKxcqgV1yuZXbdu6iSJRCeJCm168sRWcg4JASiKIZASAmagn5CiK8_izVGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23086">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XevjfzmXyK09z3O4UBkLV9jw-ZNxGbk3TExdXVHm_aodB90AF3aWc4D_DKmpbim6t43QDQzslRmN8zRrmZbdYHqPr_OTbQk4EuibAub0zwyEco5fNR8U_uc-RriCcAeKTL34L6k2rXv3hw2wSKeK5rXKoFUl8xU8d7WQEueSC_Aeb9G2bjWAQsLrHRZYSP5dkf8ADBwD5UaawiAX_P8BLUVyigZcQkFLpqBYeKGB_Oe6ey1PkBf20xVy-L2mFIV9ygJ8OQK55bm-xn_UrWRKNqGcLSvKvLNaCHKeoT3qAfRfE6KlItz0KJX3qEqNC0FbyzeI9Y8YPqWVIXYvFI6AlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23086" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4CmPKkCYd1EIodInutxIk7_QSzFT_GjyZRWFluSl4Bqc_lXaAq8Zk1w-ENeYirS8g8piNQ5pktsLqmIKUcF510RzwY0pN7GtntIonCagxAeO09G3wHbT2xMNQ2iTpQyVVljuRFuqb_IsMvd3GHCF2G6pm2kxNdZdNGwQFTF_YzBSVanB78C6Zew1fWQV14w0JWBi8GEJxVx-YeOHGLJmMNUqSoZdXNuRGn3bwWtP-ykjsz1zLJDNKfcrspNTwT_2aCf_FLydFvmeQVjcztEyAhaWrFao1Ta7cgj0_KPXC93TO1uu0Yx0djSz_Y8-S9GEt5RUTTMkeM5NwGQ5xpLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m84KOmFAZll9W9oPfFSok7x24ob16TLN10dakY8CyH2KQKKQPVt4nf1RTa1TBLd2uJjeRbbS0z9gZbfEHOJ_7KIiJAAY_c3er1qmt5DrZD__2M8XF0jNC7fnd8M0lNh7Z3-2oQA9Sxf08krPiIMUUG4y2xo12oDWxv4bHw1OBtRqN8jp9kN6KlrOpeGWns4o6lswjH32MiXfCUwQGwE24OJSUJlOMinnWz17x5VKZ_835VhLP4F-kqPtJ_vebZEzfbnW_tXsIxsL6HtzADy0_iEI2JS9AJfnY5dvRd_s9tBt8FgChQYkWKkpXMARhaNjaEPWrQFrucAsa5ZxNzvUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8NnlobTVtP38jBfCiSwojBEw-tg1KADprRcAnZB_MpR7uReafHbHjOU4-c_-kICrGdsaX9BxjbBeigLPvwXFAcQe4W9POOMjiqfz9jca7tIPsxNEARntfmzmrcnvA-RT4qAkxVSpd_xauUmGHZY1ykUWFnT1g-ZQ7JFiENr39LAXY6QSMfA7mhi46uzM5FxowoQ_stF_gvHUm4qWd6bjfxl8ulbSAmZIv1NX5D5Pwt37xqlFnzaCe6qZCxAcUB-ZVADx_9hTDddtrP1cHek7tOPatS4_2Mm1MSP0buo-T3m62MQln76exJPZRD8IYuKD7Wih5zFMRl2RNx1JsoDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAh6RKnCrrvLOXBQtQCnK3XQGOUrrUB-J87LqMU5nFW75xi01zPojgY2bIp1I0h2aoVwRcLiGtbxq7z22Jj3CRvN94jJGudylfwAY2fx0GSHFddiLSBMskCM26RBp6hCTn1yNnZE_nbEn9kBeYstZuI89VjZG42sX8uFmfEYM10EmG5PZluaKXY6CnF2aWOvFRMz0zZjdmo-uHuqS-0M4eo8RDvROq8Amr-8Lf-_kMbNn9LF-HS7Hn0TWW8e1Rwh71H2eB5QdTEa7syRi5DO_MZNQf4Mg356d2JpPoUlGXNaM2eOPODDD-pZityUhRl8j06BQ0ylBAP2vJGAKeEjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye3atitMNV0WY-XZq5shaSOjS8QA5HoLqWlKs7gOOI91xY-ULMo-Wuiydu0v_3oasepdc-vm1o1Ttj-Gprw9MtfpRFzYlWEmrjh3OfAVL1KR0CeqCwGRyQIrcCeA-XJ8IYD7gVn9GWqeRKd8OVaVJIYCuSIHezrO2yDS3ThGO_vXg7ZFVKOF6auuz-YLK8eRvcYqi4qkjsm9VmXBV-8V6sagoim3JFmI5BxCMmAWwccJYMM7zzIumi27o2L4nkxZH0PNbw2iiLxtLAL7SWNq-7NoWOdqmZvkn2Rqv5whDHPbfUedNN4n0kbeFG9C8u3G6g2xeR3rThFnbI8iow0o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Plqo5dYzzZn7C0XERP1tJjpRAE7fNuxvzIrzLkeqba4ol3peoN5tshFzSu65oL_qATS6q0ki2Ftjp727Geelz7XaqpIsGk6ML4K-Ux4mmikM-gI4T9eZkpUPiY8ebcumEJKTwraT5wP1kh9Tb5qRYjUp1cYYTWYx1AMIR4qxI3y-F8EMcDQBQQ23oImcDsIEF0TDFZttlcHcssZ-1R5SlU4rL7ZnN5oRwvY-NSXKaNgSYJ_oXnKLzr_MnQo-y7oeZhH-wd0VrmGOl-O3ZJf9hQJXAPrIecKJn66s18YlywcyddLFwBgdOPg5QoPse2gYjkpzii1REqGnqvC2_dtMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLjS6iW5XOmFxeKOiR4Qr_MJ3N7LeMaeOwzTDWBhIcJ2SaEgPEWCFDvKgjJ2g2nu2sVnhMTEk3UGFDHlc-9no-y2zfAV9SfIkJXNCl8B57GIO8kT-jkXHNm-tWjcq0Yw0zSDTIlSV_ZOlf0giTgtKSW6IXmPCJOo9TP2rX_H3dUOzlFA7aGW8R0kLIjwupvDZJ7Hibaaz-nFqrruIFUvHeBdBA8PVf-9deBdkb2KejT_iAseyo0kV8CyAAZnazpOxYin8FSWRTSXCQcLVDIE8l3VqfgErbKmZxiJ-7e_IkaBSXkY9OjjTOLcLEtoM135itOWypxSGO-CN3sUl6eF9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO843QxLpW9tiA2D_1aYkZQSz-6q--JIEMb9MuEYsEcD88nPOgh_egqKgwltuFc5u3eSpr_64VKHjTcm1L0h5ujTQKa5nRUAnV5A8PZ3DJtvu3UuPTHGhO1yo85y0dhAbklw0ElDDL4QMJo4zO-Z2OfH_oyM4nza-bSB08hV_EnhB2qHQZ_NE3mMtuQPITBMjS2SXTFfrN7FFuvlk94vvTbsFGF0laofJOTJ6yWyMqhRoKWj2D_JJUEB9Ng0aWoVLvVZrHkc3ZAZg3YyO5m4qgJBha916xzyl-4aQocxFK_iiDqtyVndLJZEqc8rO6xErWwyYNGgZpGTklWf92WqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER3FZL4ywMZE5rFgqrSGpx9UzGaiZhYSf2QEO4wG0u9x5YLaNGSNTdG5ImyJottFklcDg97tP9FIqDpu1nqzUOhNWRcrSVl_AvatwpeV0AqNUvJMOsYOOH8MKt3IroItqIstSk78PPTHeH2z8z9BgYaSfwLYIX8m--cSdxnvyb7WlzUggk9qSgwqv1-Wrg2PWE81q00lq16E-09H7x7ucSzLaewe24CWjKSU5fYAzLXI_96TQ7EVz9iL1WdLkxC-B6HFUKTyNThq2HmzYhXdGW4I9hAO3vY7b_OK_rZGfNcMQbU-6XH46yBdkeJtbZEJFW_wmbcxudXIVf5Pf22l7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUXHXJennlwGp3PUUgx0uPtspOTR0zFxEoAoO1SyzDGDjS-7so32S50sYr_gr_Ct3wtIbEG5_1fHtrjYqn6qefPn9aQnxzasVsqGHqiw9ym2hyPAycB8ur25QfY9IaQgIJtFIGpe6R-t2NFr-gvkRvl6w_ZH4oHYEKuijfvgjl0r6XuMQdNlGZJ007XAbASiHr2EzF07x1AslMoT00UeFRLiBnKoWU_wRcHHCSRcephSHAH10rFrQgYb1nTsXijJO-8BedlqLLoAMI0a5rYjGjRZzavUfJbzeiS0ZW6qMYIp-q_JQwZ_B9t1J7Wbt0zKFJRTof5LMffTGfXdFrkuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAdZGmKire8HXQYUqgfjTNTsy4OXXxZKkKL2HjBuoywfYDXiUFBZnpxXzJhCwzBXgWFhNWr5venFSpinDQdNXmJxiLZQMjSrOTSIFYGcwnyVntyWcupoKFziboS72B6KwBWpgYpakn4LT819wTq5jpOvoR8FneF7AevmeLZivIx_CybHZaGkB8XSvanie9-77QG3nMEczBK8CJR6ZlIuaimIds2h_v5PsMRpQLkDt4kDvu3R0OqbHHAd5ppROymfsL-Da_Q5TukKm0tEOKM7_2NXi0l0Hc8AGRqZWrAYyC5WL0YO2ddgNocc3ITxXi7Bqjmtl9F0S9hmTQDuoh2p_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbtQpMFb69pQY29TrKXa38ea68p0KD_Aq0eKWTwUetTrvZOIsyLYcvNVHOV_hPUqQiVnIt_CsG2qYZC9AntLbg6I7QI1qKjU-amS7jO9olLmhUwLQvQMqGgOqoU3wMGJIheqw6BQToMO10l4CzszTxnDuNTWlgK3Zl5oXZ946WWqNDiLyjad77-EX6rTyCrJRyEQRUPBqS2ycbYHZPJDBmeO37oaxF8krvnc8jeEMaXzcO4IuElJscABbFj0lOLiA4xLGmsKA9-02cZO3wemZS5i5f6HXSDjOo7kNR7x5TxqDHuhFQyWqT4DUqu9z-qo5XxY9POsldj3XuBsRaLpwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZejtzpaI82aaI1L3M4xYLVuLelSrmSjbIFqzyo7kmr5SMXITBCuamZccrapxWXeAxVjB1HtMgkbjm0K83xHaenG8jaDRZsOc-WHd-NA_8ITGUrJtx4yIuOUq_DmvoFj1fgl3Zxvtm9iAkgVg8STLvERcqY2wAbgXwJOax1EVdhROOlwkOHZMVinLdD8BfL-7HxShlxZkxsrLJRA2FWT2QiolbcFg7NHy5VEVPu02gHIwSiV9KYymPsejDrhqiGUjPvFWY8IVeBfg3uFF4q6RfOzK4HjdQqaP25I26QhNQu9_pBBiHfGnwFmRa7xJ_EWIPifnrpB-I1hgQFAwDZUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=psf6Pmx-bWHNrPV0sgSZ4-jGbRqV638OXJrHkfzR2RxDJJ2zcKyhY4DBFD0lB7hWDKLH-KHaVop8gu5CE8z0D7ns3gdEPbsvsqUtTbDOt10Bnr06wTJbzOIGa-ilmNVXrLCb-Jvg7AhZmKdb5hoFoT9wobT_j8BPNeT5BcyY__JUqTQXe_aeQeS96zrNjZWEkC7kA72jk2fvl_kW1Yl0T8k7MeaX2Zfo3stBC46MIlJoCaimrgYpYuYUbeNj7GupHhkxvuZEBkQl_yZDcedGBiwldd7ullCzvhmvA30nZOYr746SAXBe7rHrpImmW9K-9l2c6KxJ2CLAfSV89cW0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJhnBDPI5iIM6C5gm2rD-56UlQDdJazck37kZ0RqTrfnYlU_zCkG_6SkqwNRexll87dcUsmhz2tx7N7jqLQDgKyO9HMmm3Ew7fw-uKkhVcyYuhSEk0iisP3k1wxtMRZPiZz39JnSKi-NyNeB0ocThvxyQUng08q4j871VXJEDOBnpqsVGd2gkLVALslCAw2mebAmuC9Mprrwu-e62VAw11ig1wl13vNFOCd8PtMkM5KWAqolSMS5SH-2Ek8XDMYLsi6krvTGIFYkSCq9jq47c-bffgSQNkjKutKKTWCqH1BnnZA3-jI-1aOwduVbt8go9QhVAzmDeW574Y4UnemP8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NXqAl42yoLBK80Q-OdoGd1zuheAsu2yE5NE5Fnk5cUiioEx5_5dMH3l1SW-9IYeq-zMd-XWtAsLqQfT3bA0m-KeeReawGLj_My6sX51V63ctDoiw1F1bBpqNOWUBtvNh8Q5y0WmTswNzjmuAK6c3PrH7VjrwYjt7xbV_v6sHtZ4iGodVCauqUjcxBklRgglJu3FGFuZ-1Aqd52Artyl_tj-t67QRymBND8Bm87e0y-5eEq1IkQYvGi2WVy9rpZBqDvnSbl5z3OBG0qUhLpvNRN4vXkTgBIWzYcIbEqLerg5l_-tvXZTbFdjE514rV0vpPri99t519RRInyXIIWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUpPcmgf9sxhx4C2q1xqYlGfzsohmO4roNTOku2X_UjcHcV98Q2QwaLs8_B0ZfrtK3AB2tKPV0hF514ySnVeuVFmWvnhDTwi1QoO5gAfbOvgZAvX-f2sGdj9pu3GZy3jF8W6o4faI6D7a8EZeIJZrmqaHYF0SsKkGhYZuCLUZlUgCHJIurWIOaXzZN5mFygP4Y-QKjuOcvNcvnzP5lhRikHTkSndB1UfEFlR4vdhatxoripJniLFQQ6-dyZ5t9pc61Q-cqP_Kngi7T_3mzldFMj0xTcIeopnX8eZUgdG6rTdkIPeln17IvTMKmx1pYcdud38FTLgKSz2YMxHqsG_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsF4ta2b8NiaVBaZC-7TS6WPMJR-E6kII_i4vCxRfpCj2CNJGt_8e15oEDLwgugjhZhqnWgRVw-beNAy90b9lD2-Oj_vCRE07wyV5lG1W-WEgJqu9n7cFZyo15zgJsKMwGIB8xjR8BMMk15BBQyOlLwX62SIWe2TJ00lQYiWFPmxt2coRQuwVrMTC3BL4jrqRixxAdFv5GWT2D6rMr9PIbKbYyQkzLwxLFGNRno2alOJWKjWBVX7bxx3b0uXZ1jO3enIr61cOApZV6qpnB4AsQfNXqgqiHwPsyQlD6oWQTvIQuUkhLz3KHEoIY32iM9_xrIaO9L7jezTQnVgEe84ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyF-7Z2LvhwUKK-Nny-1LCkegydzNKrJDJcUjpclvw4FTdsm94KkIyiizIrN-L462RBPeScC-pOmk2eQS3_gMsaZe15Xw_Foi8NVrUyi5xsa_Qj4PRLqmNKi-qkIng8icRbuQDqEtRo6kQCoctPzfG_4h8O0khe1pfxQN55mXxRtszOP_b-e86naHZsSafGBz4KyF3yGjOoZ9RZjukVvO40sbGg25BYbpTJMwIX7jaZMvij-1VTxCzz_dYmOrnLElhrKlFVymSYS4xv4lH7Yxis9wqGk_9X8w3b2dAB7LmrXXyDESnGFhnDZ_M9HODRzUgtCsPisD7m94_DDFGzTvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp74hPxsVbXsmDwIUx9pm7UbUrNYaROSdmDMIHFFqqL3jREpwkoVF5mfi61Mh9GKR_uMiLsK7-Jww4lWToJBDdtCzsfAajt1d6VtMdj9HAXZMSi_rOvvBIaic3H7AOAkVgiDHuFcwiH9BR18LiDjDdTqhjupVLRNRciavus97q35CQ0Vyu2q54uJFIbXa3pgEFRWz_BmT5ms_7DoHBDkgpDvyaB8p-uwa5evW9KN8XvnQVqdBEUQrY8PKYomv0JhuJDI2C34iTjqKww8sSYsYluepBpkD8WxclWsI0nVhNu_LOjhGPTK3KxDm_8H3CCS-0MbPsLqluO_JUqAkA8BBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTWHWs0hptYdxNwH2yF3Sgn_PdYQObFWrw4Km_815OnKCUMOWqyPbBG3OsGb8Clx69_SK_D2cGjYQonKW46BExemizFDwj732piKn8a_p-KNQPH94V1TDIaN8V-0hBiLrKHgauRMJyLZn9z85bD3oYSx6rnJL18aQq1loE9XOhE6nnBx86AUmSk_dz3LVQz9Qvt9L6MSSzWkm5UXGAFO8uWGNrVlAGi5RJskndudBW_wXVeZCe3OpP0_KFD-Sv8x8ZuyjpfgImndsFgT27j0HuZqlhmOa7xPVwriDFOVg5RZUX5IkMNzifnoyORCuX1IKr0NzFXs2UEuRd0ma5SYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=YXQMvT36xYwCS-MfkgVE7NywzAG1LlrDUGIaJU_pIkCNc8VjSzffjJTnvDPM9r22dQVG7rprcM9h42R5zLLeVgb7lHxRywqwyEV7KFhr1CrmgiveHYvhjNoLUz7mQku0aPzCjnBBM7jnxj5R_kUlS41yhXJ4c2HM1KexEnUvCjQBYZGqT1JRJNNcf2kB0q_9e37nF32-NGHxNPnBHn4wZJ57f0YEl3ZQ2PV-MK-qe3FXAJQvRTrg0ZDDRlqV8KV8Yxwej-zB3agM25gWvCxrquM4Nes65hlCH3hNDWSel2eZ8R6Yh_-9FEOSpx_j-TDUtaj5CsDLna259zHBj6cLDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=YXQMvT36xYwCS-MfkgVE7NywzAG1LlrDUGIaJU_pIkCNc8VjSzffjJTnvDPM9r22dQVG7rprcM9h42R5zLLeVgb7lHxRywqwyEV7KFhr1CrmgiveHYvhjNoLUz7mQku0aPzCjnBBM7jnxj5R_kUlS41yhXJ4c2HM1KexEnUvCjQBYZGqT1JRJNNcf2kB0q_9e37nF32-NGHxNPnBHn4wZJ57f0YEl3ZQ2PV-MK-qe3FXAJQvRTrg0ZDDRlqV8KV8Yxwej-zB3agM25gWvCxrquM4Nes65hlCH3hNDWSel2eZ8R6Yh_-9FEOSpx_j-TDUtaj5CsDLna259zHBj6cLDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_I2VuhL83ZJB5LciwOxv6VmMyto7F1p7Wln8dZX0b1o8hnwYW50ZVOe5vxOtfacUKO2UodwlWobPOkntdfgNlG9P5HB2dIJEG0j3RXFw4fPygVwKGoV16NSApiAkKO2YLGD7saHic_2bYOo8zMoQbUAf8_u3SjD1j_UMpHBJe-lIZ5O6DmiRwp5lk9OqG7F9tw8sJ9Z2XhlT9BW7znfhalcRcjysMKOBTyK4NWP7cDzRrfyeym-U4Wm73W23hgn0b7OT9WfLlB-85k6tSNjPigXBsSxOV9MXLHFnZgwCWlBWJ_Mv9snXMciHYZEOVgJvRcVLJnNlv9_isDmSK_WLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-rCjhbE14Wf-3MftN0inCCbV8JdsfMnx0RlUjwOnY0yBdlIUcJoc77besrwEqQzmaBoqk0Z51UJ5gLZsYpvTQSmKLZzsDB4tHJDnx5P7ZcZRNKb6Eu2BPGpUz3e223PY1YP1lSoX-dLy_dd7XROEJ7UdLH02ysDAqAL6YnfsQn-steD3Rkq-GrJPTeO6OF1drX_tzLSbRxxFJuB2oD7XXtF7lDmkhPsfldBZAMmQ3syEEYDaSo10a6bWHc2j4kagtOyldpXT3-2wjN0GMwDAZadp3X_ETeuT3zUQJo7MIPg1BgNw7qISQBNA_lebBbMv_jKmCHzxB2Yhy674bSt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYuriZaOrGO81Us0O3t3A3L8-wAr3V0MNhZ4VFh7kp5UP4KmkoaSpzDkE5fpelga41IiN7ZmoKIZYDaQYaBJCDpenOIZyY4RGTBT3y8ZWefQ1D3KNHwf2pl9CWs0MyQvVHL-b7qwp144xweLuhDSPRsjBqQ_Oprr7a9mYbrTllI7-AK8MIRqRdfbDzXQCdnheKP7W9MhuAwiWi9dG8NodR1nZNFoubU3UJ84n-FjfEO9HlHwJqbhsg7WZqyi2G50y8Ce5PiEhar0K-glNFRuwsttmuoNb43FQn7olxtFwprV14cbTobAH5eUTwlkWIztoey_YA7aYh3Z1D9OLPPDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYrajnCPnIm4W9BaYf_j75yD1Y7x7uVfljqWS80B9xKi1XTmebUPRQgxGK8q2xSB5fhc5HcgK3bL6VbxZE9F06eya0oEWQRj56WkEhuZALsA2NptWj0oZYJBUTTHsFnc0a_clMincfe_i4cl9pOgeDi4IxRMnMPLsKnOfZsIBA5TybDwOlv_upqs_YXBl5Zoeis2jOlgUfAVJ3TZucGQ5KMr6DxdOrltg7fRx1csoPucqCif32ALLlPR2Qvpa35Q16rNqgl3vcJNmNZLt4GkLDmvO4C0vfYw3YVrdVNS1aew7G9qaXJk_I4tLUlQWSqy_DF8Scv05YFGINMXRvkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDKEXbwrP73nV1zpDd7UsaS1Oi2IuvU88z2fxotFTvLkpDwOKbXfTlqKn0fRfyZpYDLrqiKAMw_KY9MPPTH_jGavv8MzzK6WkqkJLqQGESjLBafdLmuskMtc5PomsB9p3qlMj7tItRRsLleMwHuY8WI69HFGFjHMPUG_YOXSGjY188-OyGVihvczrC-MUGhhXz9FSGruiWCP7BoNyoRsuE3vNNbL1Y93ZSm5pMZrDM8C-4XiObgfBgRHE-7Bi7p02OrMkJjitD280tvHaLhlRSxBKxiZVaVYqmpJ-nG3Y0wfltCHyum4tODknNdvB01AoWbVkYNyiuNephljiLWnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVt4e-We8f5fJOsYq3ZVzQzi8staSJpS_BMoXe5ke4W40oOnPwPcLJmcUIexi5I6gHx78VA2xUtwiCm5cCbRpDKM0FhEH9crTOSrB6GOeLd8k47kIuO_kI5nsaGK3uvQ74hV3hszZI0GzQcpZo1wJDzCNb9B-EA5G9jplJTKOi6NhirjOPG4V0FwCRYXLA71a2TcCIR8gv3xmhSQM7_EtaC7Ez5w2OpQlDu-yLNFAD3XaqOTwDa0nBwSzYrr7d2zdEmuxJudRHTE9u8qnRVDhgi_NKgj30R-QHkSeJYF09ji6yUV77wi-i8a9l00gruaSMU_D3gJjJUolKhDZIGeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chRA3eV1EqHEvYKZN2gizqIvqZWQE9w7ymg91wYBnao9lW1NHgm354aVmoPUNg4jl_kewPpSse6js6VxdSp4b5kAdtcl3nwIwklWAmHen_sE1gESM6N4DX-Cd6aZiuTaxdWi1EyTCYmhxdIR565AS183qj2eUE14XcDl_XY-M04GvnHmItmiAvivG97v71BcdaMtJFWX63iGSEe9Lpn4ql819up5PO8RbJTN9RYFBFWzMFhV1z4anmJOJpOAYY0MiyU-lFAUrhkoi7XqzhANLyxDltNeDG0ir2fzftw68nnVwOYerM01C7iUatus8j3xY2KY6kk67w4pQwOYiC_sWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=TvkBpV7wUFSuhu7Oy8rcfcsqChlraGQ3BslqSu1yXtX0JAtH-EgwcdnyHvAnmrr1JAHCXQ3WG8ZLzSM1M43m4y6kRhto1f1O1L-2gxHgaCW3lA79IbPA0j96MRAREkC4OrcgGS-TCweFk4qHAqhq-hXCy3Y0B0VUrcEOEV_Ps-4B8-bM_8tfJ-6hi3jnM0g5NeTZajGq8z58JB1lutnm8ung_j4ebR5-9NvoozlpGhE4bI9umJf15pEo9nr-jIV2UWg5wnSNP2cLHuGaqVrgq7F0d70JGd9xB9w8m6GcyKgm20kHRzN0H1gunQmt5HR0v4i_uhKReTy-y-0KgQvQoRYIpT9HrEYseNrN75r72CqTcoVK5AnYYfibhPLH5jnKe-JaY0CMjLunJTBoOOruF7VZpiq6p2eof4VcN7OC4ihrwQ5nvpP88hsffi2iR-bucRO4TPa6mXV3QL4-mYNnwzNMa562xgvsfUR3JGRkS5ikIMldumG4ZGKctT-tfGzcZ70iiSMGQtENVa-sp8oVr88065wDvszvVZbiCFrgbvctz9Wkm2bZFZQXOXArUKbiahB9ouq5-sFRMn4Ao-n61ywVds6IATh4cRKZBzjXmoXAO9hzOI1YGsoxiLC4eaE41hLJca8w1BHYJHuISoS_jT8PMmTsKR7ZYYFrx9sRzIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=TvkBpV7wUFSuhu7Oy8rcfcsqChlraGQ3BslqSu1yXtX0JAtH-EgwcdnyHvAnmrr1JAHCXQ3WG8ZLzSM1M43m4y6kRhto1f1O1L-2gxHgaCW3lA79IbPA0j96MRAREkC4OrcgGS-TCweFk4qHAqhq-hXCy3Y0B0VUrcEOEV_Ps-4B8-bM_8tfJ-6hi3jnM0g5NeTZajGq8z58JB1lutnm8ung_j4ebR5-9NvoozlpGhE4bI9umJf15pEo9nr-jIV2UWg5wnSNP2cLHuGaqVrgq7F0d70JGd9xB9w8m6GcyKgm20kHRzN0H1gunQmt5HR0v4i_uhKReTy-y-0KgQvQoRYIpT9HrEYseNrN75r72CqTcoVK5AnYYfibhPLH5jnKe-JaY0CMjLunJTBoOOruF7VZpiq6p2eof4VcN7OC4ihrwQ5nvpP88hsffi2iR-bucRO4TPa6mXV3QL4-mYNnwzNMa562xgvsfUR3JGRkS5ikIMldumG4ZGKctT-tfGzcZ70iiSMGQtENVa-sp8oVr88065wDvszvVZbiCFrgbvctz9Wkm2bZFZQXOXArUKbiahB9ouq5-sFRMn4Ao-n61ywVds6IATh4cRKZBzjXmoXAO9hzOI1YGsoxiLC4eaE41hLJca8w1BHYJHuISoS_jT8PMmTsKR7ZYYFrx9sRzIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZOVJbZp10YASy-ya6oQmI6nggd3iPLraipGh7iPnz46rv2FLYhZswZYk5d7BflsVKoNtHjdhlGAyNHLmAfybEUGrlzKuE-MflHPh4Fx5fJkMnzpyr93r43WjocNPMq36YMnuqI76cFZ8SCcnu2vjCmv6CysAGkg_28RlqKWraMVYgzpBGHGeZRxLLXO3yYq3Xto8ZCB2xQLulfnbh1ReaGQwxMoe6qkazXjFmuiduU7xkxot4mpy9GDCMbfABIAA8_3DOIodSWu7xiklqw6aYUEabHXRztPR0dHrCTBsHogJW0umakG5F7b5IVIjv-euWNI170A1P6eMpwwa3kNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=VMA020DkLDExPOXYuqSjH9wjugdk_j8H7qcEqc0RIPur4KFFnHVuNyUnvLKd-t1Pr8zYHfyZGblatPc-AN4D0vm0809YUygk70U6Cwb9umAUAxndtnwel2xVVzBm8Eu8acimiGL1iQCnTcX4EMHSa5Zt2mV-VQ28Owdd3N8C00KCG7IOujVhf_iOc073b7cPHrefyPzUalHFHlbhfwAQd1fUkXTfLHKZECrr0clasnZWQBWCkk631ZZ_3ARd2vo7gE92J69IJoFpjgySRQ6eAnn4I2mCEx6XQWJLHJYtZoGaNw_1r7dHlIM1b5HFFoLUScFFEokUBZNKian4TpR0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=VMA020DkLDExPOXYuqSjH9wjugdk_j8H7qcEqc0RIPur4KFFnHVuNyUnvLKd-t1Pr8zYHfyZGblatPc-AN4D0vm0809YUygk70U6Cwb9umAUAxndtnwel2xVVzBm8Eu8acimiGL1iQCnTcX4EMHSa5Zt2mV-VQ28Owdd3N8C00KCG7IOujVhf_iOc073b7cPHrefyPzUalHFHlbhfwAQd1fUkXTfLHKZECrr0clasnZWQBWCkk631ZZ_3ARd2vo7gE92J69IJoFpjgySRQ6eAnn4I2mCEx6XQWJLHJYtZoGaNw_1r7dHlIM1b5HFFoLUScFFEokUBZNKian4TpR0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC1zQa59ePLvuGc4_F9MQnpWgGmSq2Sv7Wdv6nj5CwovRbT3gepsE4FDF4JQ9Spy9TLQaNa7kFhe-iSr0udrejSNIiPIrUdEOqhlLHalN0uEsejlDzeXdVaV0XZeLdL7-vHbNFFyWV1s6nUjg7PQH2URJRujZx8ZSAvgWt_J6gCaCfutC8RzERg6XijHgRmQVr1YQYCEKHWxmyjXFkMfHXUiY6J6ZIFTx4_NECKl1fGpnfnWgmunLzUrC7OFzm8pQ06Smfms33m9nLMWgbVzK-y9xbq_OgYby45Re2CKjGidmP3mab8ZzdU9jtw-7QGgHewVBtRF19R0htmJjqlUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr_C6RIsmtzdNySy48NR4-IrQBR64dq53ASA4bJc532lQEh09HHT8TVA2sRXw-a3EKAyerYfgwkBodsnbqLzoj6erkjFLpTBcEwVyfa_V-UurWauC0-_zkFIkkqpWj2_AqX1J9N5e18qt8TOq-veL93IPqUtmw4OK_ivCrxwdh5QJd60Ay3Kqvp8O6R9AzAE5wB9BG7SGPqFidm-OSoKwWhG-dTYhO-n47QxL6jMp-GqUAP6AkScBQTr_sn6wNcg4Ism86UkGU2q0wB64uypBkLMyJGetY-ejwpLc_Cv43Uvjna0odcOX7I9f29EngnACp5gSQL_ygcuoDmzJAOwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5TMlKcfJADPf2DAG9ANhDi01_A9CZL3qUeUBZsHdbNlg6txUstbx6SS4uHqaSgTEiGf14WmtAeY-6oBZ6Vp1NUfpLuUmW6UrNgYonS_b3jW2I-eJn4re80NCRnF8oLfevIXXALjRe6Do-Y04JwwEq3cM2COeIPm7P2mm3ijZYXKBGBCwWnLg0_j6oX4UOkO7RKstzN18QQUCVwvfSFXE0LKSlrJXO9s2bSr0_7jhzvxifsVSfI34uwoqIxJZJ3eKuPtJST3xKVlF3_gqxL8junS1NcHJVaudglDEPUm5RLbCnb_zzqYSfD9dvsN02HbXD553SGtwnFhvoWw1bBdrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9hLLkq2lhgPwzQJFEyFlUIrGJXk1n_Dzql4hd_2JztWFsIuqSAcj6RpDRtCBRm-LJFRr9YtAItdI7IHY2x8ofR3_MF_44BANW7dJMj5IWScL_dqL16OYaPjrXEN7MC92_0DcqqBh0ISvTdhqiitaO-2lvi04sb1naV_z7fgFU4QP4rVXhn1EfLl9MsOOeee-NX2tFsZGoWLgDMYHmTvb2VfwsgnJqyWqzMsuRpZFGv0Aibmu1C37_xUIDt6ymNu6Eax86rjqIuqosuue7Li6czSBy_DEATMX_wgg_B0j2UeA6E_fPUalJjqq6cmbjq1svSY6GRn0LdJYYE0S2Hnfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=TQDxZ5DAha0JvxQFd9x5YsfwJBsNT3x4kTUFlUskUbEBGjuoy52PWr2lFx40AvWmJ05XFIrHsbq4DRYDSp7IKepPFw92YqX7Z8tdViO1xCebMjJ4EEI4d95FD8Pp2rVhfBUPCuZfFgyG2icfBA4NllpLEHTuzRr0mDd1RhlpYJodp1H0YiZ38GVBYx5QGejaTJb6FyMXHelZvcNSu7INLglrBcKQ49fJlL6Y1ALMevcJIkBffegSmimDsC49Hc5UqLJZrkvk6WgUXUB4N-4skWqjZonHoS-IrP7QCd5sc__6f7svju1CKcTjeTJKaWxmDNTWa2bTrxO8wzrEe-FfZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=TQDxZ5DAha0JvxQFd9x5YsfwJBsNT3x4kTUFlUskUbEBGjuoy52PWr2lFx40AvWmJ05XFIrHsbq4DRYDSp7IKepPFw92YqX7Z8tdViO1xCebMjJ4EEI4d95FD8Pp2rVhfBUPCuZfFgyG2icfBA4NllpLEHTuzRr0mDd1RhlpYJodp1H0YiZ38GVBYx5QGejaTJb6FyMXHelZvcNSu7INLglrBcKQ49fJlL6Y1ALMevcJIkBffegSmimDsC49Hc5UqLJZrkvk6WgUXUB4N-4skWqjZonHoS-IrP7QCd5sc__6f7svju1CKcTjeTJKaWxmDNTWa2bTrxO8wzrEe-FfZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YziWkR-qlE3qrbiUva9bMGcd0lEoWiNnUH1maNJosSGXJjMgCJeIchHwLDq6PuUKKbFokeYzVUVqtWz3CnUL2V8OymC2UTWOT_1qe4RjAm_zkxRYBHGiz7XJt2dypM22uF2Xa47_A5y5W_xnpx_C3IQ2G-epdmNT6Z4_mwZrcqfvCgRSTA0TmCnZYloQM4RGoBKBDxgqZDVbQmaewsLGLboMTCy4rBjmA1-JroT45BrnMxpDgpjk0kHuvGJAcM4bFoZAFtvyhffmC58ovJHNNUSwXkWc0XoPsWvZch9_5f4tkhc4MGu4akIc6lpL-zDKwVbDZzGY3fNXkNxHzeGS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpL9aXPPHFkCdc_JBg5_ZmR80AQaEGeuM-87Ubm6GL4aenmQFABY756c6el9g0RzNJ28nZUr3io0obJhcuIEpPf0c7E-KMC2J17aATI4YGwZ5zP0y9pvhslJc1E19VsRDCpznr8dwpIAExPouDzBo6p91Ov3rcDDBDQvx-Wz7A5CO1nkCPUWWscQl2PkO74aYLSUGbgqeN7SRsTEnIjid7qpM5k7TCO-Fv00oJwYdZ9-RVEGHQqUmD0RJnS6_caLx8a9mDe1dsskYdWMc6muWgz1Tr7wQWSEgD000rF41qxcCNeStKD-O9thl129M88ltlJRpwU6eLg8qWnsxNtRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG_rn8D_31gGlocPhNPDp8FP1Yu4PWdeMN0ztphbj6XVSw4I-cpheD_Gz0KFS3m7XDXgcaLayq0UT0ymTsqIGwE4eapeRtn6RtQBNP8BiFYP5gEGh_SlhHBoKNlAYMBC0ktfyXWGN3Qm_sw_k110l5uSHxIGwVBn2EVdjCr36ZfB_2Op1nwsRCWa-FjP3myfhX52I8ssRAjRWKW8cS1FYCDxDlnNV_gDo8RP-DKEKiSTa08u5EMPk2ssMdW3Wm2y92Nr_-f-l3SxyVnmaGIJiX6XO72QeTJOqj2UPQottdYuxMIt415PbM6uTmU4MBy9dXWGIvsaT-nW-9YfhONdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPb_P2zt0UxmuW7d9MteIYLVrcmVVOmcz3djodGRNPMN-FkzM8eSvccfRbC9SQ_vBFFOus33eh7AyFSwtCNV54_V4OKIalvcq5mpIkdwxzIOAP0rK7o4_Ul-XGdbeervWAWexPIntAIyetsNML7AFgI2_nMQoUmI-SyVYgEEOUP7z7luxCXiBwZyU79BCXshMmEWOREjV2lmhqOCke-9fhw818W0vZXOlESMF_g_xqnY9c-w2VvphDzy67QI5SRzHROq7p7BjpKpzDMMxA5cAZfy-S_eJ5pJDH53UA2P-uscrOsHid5E7lWs8sJ9FId2s6MavcHZveWs2I4ZHiOi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7Sjbt4Mr3NBu6zHeDVWfIgbDcTiWPQYqfpdzq8Jb53ONrXuwiQFCNnR0ePC9zS43kTCuYIAISG-AKeg08R8soTkBK6U8g7kZsxtpm7paglVmdOGulL4XdOFPJASm1Od1tajxvF4vsX8yEb2wRoTSxVu3GTNJrk98X9oMCZlRD-pYthXWeYJ3LT2q4zzfCdKAoSsgDkv0inNXglkkZLlX_dobbLlequoOB6ETIX3PwM9m6qA-HUTU4PYQpYv4eVAqNvtswAg7UJeYJ8esa266ZW33LMMJp1RUT20jzGmEnptNGbInFB8oQhqlfNUJ2TqkjfmiXRMHKP0RdjEQdd6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=IWxO9p5WNSTERmRYn2o4MEwhC5D-1JR5pfWx25V8I2cN-m0pG2LUVp7Iy7tOWX1B5BqKs3i3GCP4357IOruNNn9sH1myd16bg_6vLde0Jf3czW4BmlzkCK7S_CPi9iU-1inM9Sh_omq6nwjt_btPca7Bz2PrgRlCKCkxi0XojwJ1sHG5dI49sqrbCuaQQeuP6tYVLGEovuEhVjwIrIaBA3rtKv3TznZhk920WHIX8WwzJ5YDErTqY38scCGadsI8wYqp4g-s8MR2flf8hydCDNXFNxLSVOLe2iJ15zZ0F5QyvZlVYjX6WscwesHnu3Be7fG-YtHS_-7VOnk3ENdn0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=IWxO9p5WNSTERmRYn2o4MEwhC5D-1JR5pfWx25V8I2cN-m0pG2LUVp7Iy7tOWX1B5BqKs3i3GCP4357IOruNNn9sH1myd16bg_6vLde0Jf3czW4BmlzkCK7S_CPi9iU-1inM9Sh_omq6nwjt_btPca7Bz2PrgRlCKCkxi0XojwJ1sHG5dI49sqrbCuaQQeuP6tYVLGEovuEhVjwIrIaBA3rtKv3TznZhk920WHIX8WwzJ5YDErTqY38scCGadsI8wYqp4g-s8MR2flf8hydCDNXFNxLSVOLe2iJ15zZ0F5QyvZlVYjX6WscwesHnu3Be7fG-YtHS_-7VOnk3ENdn0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv978ygJpZO6bKzmryTiGc-2r2MLFHCDJjBroJ4dGNYVeZNUXiSaJCd0jzIBNyIOVEipJTMddVglvjRzbJvF1j_lBbbfJrclxctfnElX4dK56YwmEM93dKyG5wyiHgPyxfKD_zX_5BWCFhmvmhMDdHztF670pb3MLsuYWVJWVUAa0q_tvKHTWrZR8qp3PgnUaEeRRr1jKGkTVm4xTM-qx0ijnP7WKjcH_jXuqNkKRMYP8aJPYtxBmVbIqg1YHox08EqClurvWCCzFEqww57skGydVgJpcVIXIt37W9UqdcooIf1qxrsU1685eZ22FI8BbeIjk-6hPdbULRdifI46dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsCtQiEiF_ry-WbfiUR71IulztYay7cNtDXDB8PTWC3fAGYtXlR8UoiHq76-8dDqxWL4Iq4aEGhf3yrXrs3HqE-Yr5qFOSPXhimZqP6I57l-Zn9xHj-2CMXvbTsExZ1pWqb0d6GKQubaCor9_jY1L6VML6TQPDwlays-0mbEwVXypmYQndLUO32L-79fOLUASkdSsjznkHlDdzMQ-rFGqw5OlnJn2eAvOGsPVE8fdAiUUYQAqyWOqCGIChINpz64DbInpRR_ucmPBvoSWdb4LTfTTLWo8TEttb09ypaJNfR1XIkonBLoxe9QfcueYMdO9pZ3MTDy3owTDKFI2Evv7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEPcimaBQu-Pwy3CXf_zh6TItp3iGOGb9whWPuylztKyKdHNoEgdV4W-mnIFATmNmWGYgsfn6QD10FAa6W6V_DXAOItbAdRWVJDRoWIJNB0b11p9z5h27bq4jOIAXbANE6noQExrpCqJw3hLrNASkendooYQvevojY2oprkA1iwQNakiNexeug-dQzY4v-OCfoPzUds0bu-3oV78W5hhihq25xpR7c3PZgBsprC0MN0vhblFovZinDb7QkskbZnkHFSnMcR1tEy7xmbAiRloVueAusppg9X7CV49n44-H4s64_qB5pFQOkhusOPWtlQsTl_-0ovq3N1dqRz0P9ms6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUvmqcrpJz-uzVijN32QJJWyNkGNucD0CtDthCS2zomse55druPjTxEbcgINdeuzcDOj0XVrabYk4TwB_ReWovqvc036B5wQoYam0C-9PybMazJmen5kabmmCuNKNGbibOHaPei1ONtuOm4V2s-efj4VywEyrQrlIMBgWu0KRTwHy1FVc0cV1Kz9UAgZN-Oy8uwpukqOYY5do6689Hq8J0wJFxOrZAWEFbs4sO89vUYSyxInxbM8MtbpifkoUZJ2-Rljqr-lzKPSpa1b5F2GwK6p343pGfM6-r5L1zijj-yiwIvsxSy5H4IkcnVJ3bna5xlG0jiEkgZ4RlMGe_AdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a12NxUG3ZG_MM-pf5cpOc93Ria3YSyjyxpRiWMePlND68u_shfi24AaqTwd0_2TXnCtx7Pk6HiK1OWWyk7sd6-nwQmJbC-r2UrJ3wbrzXd7j9kPhARnBd9L-YsK_hmHQj58qLpgJBH-MTvJ9NFQ2q5BFKLQ-7ZId4G7Zouy_HsfgSCamjnmUM2Y9yFitLGpWam7Z7ujQUpB6SG95vOr3jFkuNYvQc1_cPs66t6hZkGfrsvHpzwjw7plNfC88OLrPRRjwn8TZG71bD9BadzTcD5LcnhPxGxRk3TkpNrsUzKL7GVcLTqeznJn_MynXS3YtqOd6aTnyVHbsOnQxYl7G3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjEMDi3ncohNMXps01mFdgJEJ_A9YPXPmsX2v-AjfjZw5FUEf4kfzykiCWbt4zcUwr3a8moPmk1aX_NCohFSrWNvjOY2Kl_qcbAtXcNZx7-5k5OGghsEPwKlsVYO4vsdFMCit7E7PeHEalFNnVq-y9j4pDXTsb5qUKvGuBaqDkA13myh-4HB5BVhqkNnNF16Djgxknaq1-Gx4WrY_XAQ9ySeb65HnAbOQA0FOn7qbBWjSn0w3ZR1FSTApYAiNlOcLyluJhUF_sa-2EGKBH9buJ4Df-8jdxGRauZNw8R_AnRM6FEbliP3joCGsU21SdcyPUvjZaJK1jIv-UFTD429mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgfcduT4iymIr0yCnRYeUKGper7V3yXXy1RiuUH3jYupzKSBXZdNl_myUGVNN5SKbvOouqoKlhI3kwEoEm-jvYltHwKS8PdNC2ctP5LzCPPIDqYZY5ux7irB7QPyQP4SckxRgm8roSDgfa7C0Pis9esrzk3n8O1CLGeNquI0-QWLC0ZG7q19Vcu9ny-7tPYbGqRKv_LkPZhKjKecToV1xPZwZc-1Fs42vpfT9EiEw9aVGU_5-3M2HdYbdKpSN_v4cVHdJ5I30gyBZSL68DlSxvaDxGot9K8DLKQBJ6hFLMxfL_7oICKaAYyvIyelLbpYozdguREGB5fTbtcavK92WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq3er5tDjUUsUwFWr9qBJx8wCd1p_Wyc-s8T6G3hJ4hKzWVqC-07nsh1vxpdpuBNj1MnUQIzDgNJeT_DS0Nus-_4f8DS8pZQZVUkfaeb_Rnk5j944JD_GJFcNAzDxvrwr2VneCmHQuby0WnD0vpa4-WYq7Pv7KKZO6j8Rj20ZGDc9VitI-7gDtBBJcKSUaf7zh4wSpygr2osHF39cnK9kpBc1HOhfqrPUA-nz8yTFiKjCbrnDKjFeevFU8YKZn3-ZOlgzbT3inVfc370YymJKICAy4tUQVe9r6_P09ibfP0wo-cpnmdl65rjQJChqQ3tJdjOOOJEOOksnXEy7GExZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=EQQgA6hJHiax9Y6NK_9UOnpX7gz7njwk7Lje4ovyIU_yXqARKOqxqEDFuxxtiz9uA8EBFA3aAN-FaIOSoi8-RYHAnwKbxhLlbcTj_c2Ai8Lxj8S-uosjgUZim3l0mz30Gyq3CwncAkWIQTyMszq1aVokGqoEXUqsA1QzgQD66Hs3uBhlvc7rbOsizoOcPBhycn1K5kfUfUtZNyBJVqPySdak4IS35JNVucYYQncTp9Zc78IeDhpLvqr8y6BDAFjkRXZmGo9uUhFwoOuwpCkiTPyjhJafEy5IlAgY165nTgfTIVvplOx5qyD3LRSxaYXi27zAWHgc4JRtsEdIi0bEMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=EQQgA6hJHiax9Y6NK_9UOnpX7gz7njwk7Lje4ovyIU_yXqARKOqxqEDFuxxtiz9uA8EBFA3aAN-FaIOSoi8-RYHAnwKbxhLlbcTj_c2Ai8Lxj8S-uosjgUZim3l0mz30Gyq3CwncAkWIQTyMszq1aVokGqoEXUqsA1QzgQD66Hs3uBhlvc7rbOsizoOcPBhycn1K5kfUfUtZNyBJVqPySdak4IS35JNVucYYQncTp9Zc78IeDhpLvqr8y6BDAFjkRXZmGo9uUhFwoOuwpCkiTPyjhJafEy5IlAgY165nTgfTIVvplOx5qyD3LRSxaYXi27zAWHgc4JRtsEdIi0bEMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUzIQrlIzWmpdUFzC_ZWMztkFRX6Prni1rFWeGCZK8Vj9bZ2t-6ZIogH7Yy5NKESfeUwAg1cRiVv3t55AKDdQT5ErWEvO0xb9QWFdtsCBA38cfj9CodQugoDL-0Bvi0WSzrDdFY69fYOqavjyXU8KHnKOsS9jJc7f3__pHOgs4XY3u5tVb2CIGFQVKS_4UwetM1r8gwZ8OwzB90tolu6DLLFmYdA6U5UDh_TRldFhoQFLG1OkZW-SZ3mgW2OM-DOO8_HHrMsPTyHki9PR2_PUWbcdTdyccRvSabZOKrINtTe0hpcOMz4yKnZPdZ9HJu1n7TbjQarq5RCklLkLQ3hQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=TRYNuMmxjDuoaLZHXXI-NDvWtTKbBj4J_Eh7vwJ99dsbRN93tJIbfd7ciuX8jZyAXOKszdnslpuGGVE0OovBaUvai21SeuKrsV1J5x1iemU34y4XgGHeZtPQYgu43nSKUHk3IZ72pmUXmOP-tm1UMGU-EX9pmQWzjf3wqaHcnn62D2bNCeFO8mTLKzgx5Xq1OoMw9HoCNO2N9wAknCcYlJWVdHDl8dbkUm_Vi9f26i_M1S1M-HaoYiis56LnVyUUKzQUIxoVtKaoFQqp5eqtR7RrYi9vz2Fq871cZxR34o2Q7kKcYT9vi1x7O0kr9NIm3wHx3rir0BmIE_c1z7IJhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=TRYNuMmxjDuoaLZHXXI-NDvWtTKbBj4J_Eh7vwJ99dsbRN93tJIbfd7ciuX8jZyAXOKszdnslpuGGVE0OovBaUvai21SeuKrsV1J5x1iemU34y4XgGHeZtPQYgu43nSKUHk3IZ72pmUXmOP-tm1UMGU-EX9pmQWzjf3wqaHcnn62D2bNCeFO8mTLKzgx5Xq1OoMw9HoCNO2N9wAknCcYlJWVdHDl8dbkUm_Vi9f26i_M1S1M-HaoYiis56LnVyUUKzQUIxoVtKaoFQqp5eqtR7RrYi9vz2Fq871cZxR34o2Q7kKcYT9vi1x7O0kr9NIm3wHx3rir0BmIE_c1z7IJhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=bJle20GBK7BPj2ZkVrhL2-B4uuVbT0dzWVDWUvJr9GztwJWJ5dJeFTXzGtZHnFjfy7DKY1mtoOX0LTxeL83mm0JMlVag_LdG8qqFdtdgSdq1KKNYmjolUuab-VfdAzXw8gejEsOib4EESnVE3fYU2TjPwmeIigeE8vbTX3UdrhxQw5rddFt13BIFHdN-HxqE02Esd1z6cZ9ETS_lriIC6mCOUOW__qLGLEQESAmHENt2A-ZpRYM1iczYQ6Md1qKfuNq3Y71Wgi0Eu7aLQChjlM5dwDM77fqbswfGjH0-UXBiqr7_0MpPqc8N3NbUWPfm7kwsdUoStjDmY-wQ9EQ_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=bJle20GBK7BPj2ZkVrhL2-B4uuVbT0dzWVDWUvJr9GztwJWJ5dJeFTXzGtZHnFjfy7DKY1mtoOX0LTxeL83mm0JMlVag_LdG8qqFdtdgSdq1KKNYmjolUuab-VfdAzXw8gejEsOib4EESnVE3fYU2TjPwmeIigeE8vbTX3UdrhxQw5rddFt13BIFHdN-HxqE02Esd1z6cZ9ETS_lriIC6mCOUOW__qLGLEQESAmHENt2A-ZpRYM1iczYQ6Md1qKfuNq3Y71Wgi0Eu7aLQChjlM5dwDM77fqbswfGjH0-UXBiqr7_0MpPqc8N3NbUWPfm7kwsdUoStjDmY-wQ9EQ_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=MHSpkZd0UdnGnRK8o3GmAB9iR7W9RG004eSjUmkAciCdWm1TLCY_WPIwaPI6vmyeQUUf1oo6WeIgtaB7ravcIHiEjLKMzSz0TYQ0T7WpSHafT6ZlxMbzfuAf4TuTyBm9ePEKIFiInAUioJFbsm1Y74SMp9kpAvoEfi9hyrakLrewsqba_s3Kkzsgv8pkIgl0d9iRz79gWeato_ynlf4opm5F7YP9YGx7zLaT8dEBdXwoyjYYByUXrLcH1MXBSL5pSpYELRKQ4vuaADnjw8Q5d0Py7mgc89nErB6hjKEZb8EcXr7ghS2QTgvc7-VrOhCCG7Hk49PNDoBlORg-x3I1ogFhYPiNk563f1te8zfjhGXc_tiufh-SJdlF7VQMkjOZCTKs-pwBXI1SZlvHbUkbT1Q7rlkiNZLLx76uy5esa9Kgv_EwUFMUtMCdoEcdfsJihhfDdR32LcFN2zaKfzPG5frdJHZMC_dtVYvCnidMm5BZFRQp0cPoVPlLIC5GhyVEVvsm2gr4cXYF1ZQsJa80cn4dNgcNEA-woBvZiSnHffVs9XqFbXsfKaUnGXF92T4dP_tnuZv8NEk9fxmc4MlF0PXIItsdMp3WexkfKrDtNHGPIc-P6P5QSrfnEWI9G1jJ_0BDe9F8fv5j030vt7b4DQIwc9WkQCQ6ifReLjyn8hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=MHSpkZd0UdnGnRK8o3GmAB9iR7W9RG004eSjUmkAciCdWm1TLCY_WPIwaPI6vmyeQUUf1oo6WeIgtaB7ravcIHiEjLKMzSz0TYQ0T7WpSHafT6ZlxMbzfuAf4TuTyBm9ePEKIFiInAUioJFbsm1Y74SMp9kpAvoEfi9hyrakLrewsqba_s3Kkzsgv8pkIgl0d9iRz79gWeato_ynlf4opm5F7YP9YGx7zLaT8dEBdXwoyjYYByUXrLcH1MXBSL5pSpYELRKQ4vuaADnjw8Q5d0Py7mgc89nErB6hjKEZb8EcXr7ghS2QTgvc7-VrOhCCG7Hk49PNDoBlORg-x3I1ogFhYPiNk563f1te8zfjhGXc_tiufh-SJdlF7VQMkjOZCTKs-pwBXI1SZlvHbUkbT1Q7rlkiNZLLx76uy5esa9Kgv_EwUFMUtMCdoEcdfsJihhfDdR32LcFN2zaKfzPG5frdJHZMC_dtVYvCnidMm5BZFRQp0cPoVPlLIC5GhyVEVvsm2gr4cXYF1ZQsJa80cn4dNgcNEA-woBvZiSnHffVs9XqFbXsfKaUnGXF92T4dP_tnuZv8NEk9fxmc4MlF0PXIItsdMp3WexkfKrDtNHGPIc-P6P5QSrfnEWI9G1jJ_0BDe9F8fv5j030vt7b4DQIwc9WkQCQ6ifReLjyn8hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFNwYMHttdCmZMqRZOzLvEgM-DaVNAjbmsJnGL7u8de-kC6pT2YF_Csof3xwvgyAgFCIOdbsHbqv6Kc33sBJaIO6AQKish7P1omN2tQm6mG3RTLtbxxpQg8SmyRSJjhVpuxU723QNChFHz0759nl5OEBKEzcAUVGOXm9fAbbxUaIYQPO2ztkPMLqba7J8QcyYbxfoPbuRpxfln0S6L1HUxNwoDb4FGsJ5XIUpvFVDCAB4sUviWfj6AGnNqun232fnACRWZ6-ZmzAT59ie-U7BbytvTI3mSSBQ1aHRtkYZR1ERPpLuXNOpmMdPc1wbm86mcnDD-NCKIXlNMtiVJVMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXWkHHAongMcUJNpq0bxOs22REezm2iQZ0Jky-u0ulFngKBg8iInzmye_nVySGfIvj4H0pAzOa8QL6tvId4V9CWMBxEftAxLn5JMlqCQQ7iMmkT80x0SxE0xzpbAjBQJ2z37bF5xN1JImpcxbT2i4BmDhFNh6Jz3sUFG19MA0xBv9sSPK_HLahZe2lZL0nubeGB1ePLu-7-k0LF65QwOj14xD00J0ci8cwFT745kkzJ969_cW_BOhue2utzN0ZsPf-RArYOh0mYcu_uPutkFZZaM3PUKHmlcvOuuKq4QGm4o4aqha6s7ksivKJx2_LO4qZlBQWs55gxeaJch7QXylw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZWYM0Ou0g-4C2eu6dEW0ORJwtuouZrKfmDQounS04DvdxdGGF2CTlUDJsr88MLfP3Gnpa_f053CabsarRpRUmOMp1lCr_ZbBX7SjfBD0q5b4IQ1K3GOzlxu7-Vz139SjumqdoH1yDd070ZLLGvu_0OrYM3QSZum_57_CYbgbqHaKP-NzUUJ13FDcxB5j1G9TReRfoU8wwarEUklJ0R_gJqLX860K2w5EUJUpdsEOI-kwmikFgQ82daF0QoS-taHqY5cyfaQY7-kU7_LnhBEMv9YPWVKJzdzf5lxnhvFom3cy0F0Q1P9mV4KYXWWN_Agp9ZbMbrlgvzsT1Jk4XMNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=XAYL22WzHryQgDKW1iUjoon18gbXe3drRQ7TfKcNk-bK87aPikqSbmRBCpLrGe1ts33seL6tzmrR_hzfqykkmEAUPh-uSxOIkU_u0UdtqzxLsrJRKhwE7bxy-Wed2knynTbqbRYG02eb3Kxes1eOg0xFo9m2usbRqwxHUBR_tskL7LGGZricwifU3dkmoXRy0HH_oxOTaOpHTfubNty0qBfJSO2PA4f0RmunztRJZOG4oy6OCCGDQaOZu-8yuyRKPY3cnihAPD-ZxRU98BsSevQZEMzxW5OL6u-6iRpeAL0lQBJgWjGzeJtD60QPNAf4l89wa4emUslbnXmKvKiRpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=XAYL22WzHryQgDKW1iUjoon18gbXe3drRQ7TfKcNk-bK87aPikqSbmRBCpLrGe1ts33seL6tzmrR_hzfqykkmEAUPh-uSxOIkU_u0UdtqzxLsrJRKhwE7bxy-Wed2knynTbqbRYG02eb3Kxes1eOg0xFo9m2usbRqwxHUBR_tskL7LGGZricwifU3dkmoXRy0HH_oxOTaOpHTfubNty0qBfJSO2PA4f0RmunztRJZOG4oy6OCCGDQaOZu-8yuyRKPY3cnihAPD-ZxRU98BsSevQZEMzxW5OL6u-6iRpeAL0lQBJgWjGzeJtD60QPNAf4l89wa4emUslbnXmKvKiRpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXP4B_ntEYTfUJCnysHUgc-hKgxEZhGiH_VIj-0vqK_nlVuEP9hDlhntGt11vPfC6O8jr0Mna6Lj-_fSjJE_fTBH8gUDtqYyOxH8_PxjHOIMO1txrsM76FDQncUEkFjHwhEmxWzEMVQw7w6sMnsO_DaVWj9XHF2aWfk2T_wvT8IQG8YNl_mFNvc442vb1odebb3m5lrRCuK2tiarw4SidyCZ2OP2ZKIjtHIe_089t9d4xuG3oEUMUTGvY1gXV3SMLNf6p97c2M_m-nIa9Dbd82SpD0YUsdMWEwDWrot9bTyZSLV6wLLAvVGvGwk3R1I17F5g4C-e0lThKfloiTygYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX2b4d0AHLPgTU9wQdsQ9wBhoXqjDA7QSkiNbBRZxga0VxwGYd2ISiVFvVbhtZU4JU4QWCvQQSOuqKZkYthfg2RaK3uH79w7IhJ2kFQjipPebKW8FFolIemyxlSrgaNDt_YazqXJ-UkAGRSrJiTMNdSSnGjYKn6NbTU1K5X8TMVD7HmxrvqleR6kU-GkWyas1wQrjMx5Z7Lt7EinX-IXCC2V69xjkE5AQE34mz3t7cndOabdOKIcu2GwMK5VSBtczjcSyrKavsII29zNkpRKWiER5sIN2yPepzN8056RzGfWz6PetUtbtUuO2bqQLTBqOSv88mzJp-NoFeP0E0jIjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osSNSsD2-TKGoAcf295PpiHzzpw8WJmaqOAiE2ssGEkTg4QFiOnComlajNz-igQJKt843fCS-9Xn3eYlSS20raKSxnrVNX_r5N0zlFOTBFVI5hMDacdYmyirjMoHKEFw22GGs4NTg2G8o_JDJKWznpSNOphi-2LmwaBweIXySt1KNpYKkFSa7KqN6QElPkPyqroueKCGOw0BeERfTVwYhxEV9kxU7w2yF-m6XdEHrMOT8N-tOt14oTwUrtYysQz541xSAvmeB67lwNo7Hk72fg0pJli7iPOe0wWlVTPhoxQxZmDRqWeE9v-2FQCsSe5go11aO1f2QdXPomf62HZLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW9HN9uGzTMSkSQoTYWqs6k-r8SRszMap4kmxPVxlkQ_MK2lE8UjdMzzTXD9_UZ73MJdTXprcHibRHZYc0yGnoDs-LfjclIXTvadZ7wk-JW7Vpqj91p3NCss3elVNYULviirXX-6v_7MAzgN4ZziAj6PeA-gpNw7KuWBUv647a1dN12Wady2WP4J0s4RiS7bkdNXRoWqXLEXf8ePspqByq2csnfPaCqP8a-Ap-vtFFT1QA7mUVe3TDu2ke84vH7WSLIIIuAwVPbSCvRY0gTKda3aPJOljFJuA60WjobMLSFxBKoie2XHHovHePSOSl03xFA2iUxcTH6fpmXW5IWijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Babv3FiJA6HCuVZ_7kPJbpG8gk9wtHQIOtRd8NSk1FbfcPv4t4G5DRAkLjVOU3jgyLY3xmX5-NDTGK_cZUUDjDFuBkKB9oyxt33bdA3bVNA1KKMnYCrIkRzzGnNKGVSS-_R4sq2JVba11zvqeII2-sukJHVe_nH8mZlA2YLviNVuHGmSHa4jUozX1Zln1rhYO2xHIVRCWWes5HiQhrEt3_8AHp-NJri61aNebN7YGLo5dMOzANY-YdN2NDthLHhK15CSwtzTa0oi1dXJd9nXL6-Xw4kYyXtCKDS1KVvQQnS0zp6ZHoGwvg00kbixJyAC3QqLQqN8JMtTxqOwJX3ALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=WMJKT1R4u1_YI5BDkMQgXi9Nyc3MXh6iVFO2qPPU9QDyNJQfKyWn3vj4p5r5bqMreNeaznLbxXRDFBpV-ikL3YkuXOyfhuIGNI-p_WdEOJ_v_A4J3Ei6kNaaaaCF3S-tU-LRFd58U0Sd8gqxr7rd1y0Jwelt0mq4Vte6psxgzUTkn3DxMtP_lAYtnYPyu4An8Kcu7mRbVB1rB9IzvUSfjIC1TjhHRzMHxJoSWN6kAfHF_DgqmS9gdoGnx3K3Wk-IWdQ7mOFQ2A3vfyjYavJFhM5u4fRGCNDgXL3ys7Xv8Hc53Ckd2vp4NgqhkCoO9aWnY7yE9uPf2QkeZe2zQAO21w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=WMJKT1R4u1_YI5BDkMQgXi9Nyc3MXh6iVFO2qPPU9QDyNJQfKyWn3vj4p5r5bqMreNeaznLbxXRDFBpV-ikL3YkuXOyfhuIGNI-p_WdEOJ_v_A4J3Ei6kNaaaaCF3S-tU-LRFd58U0Sd8gqxr7rd1y0Jwelt0mq4Vte6psxgzUTkn3DxMtP_lAYtnYPyu4An8Kcu7mRbVB1rB9IzvUSfjIC1TjhHRzMHxJoSWN6kAfHF_DgqmS9gdoGnx3K3Wk-IWdQ7mOFQ2A3vfyjYavJFhM5u4fRGCNDgXL3ys7Xv8Hc53Ckd2vp4NgqhkCoO9aWnY7yE9uPf2QkeZe2zQAO21w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riN-ZeH-vwbUtwTVvIK4P-Vb_UKpXSUzzSxyjNl51vEUWiman_mOuXJ1O5_A7-djS-GbGpnzw6maLSJ1-I0qJBQcUhSuVQUW_hsj1sZnU_LuFvcZLpqmhuJh5dXuxxG7i-4nB0dmZFD-yYrcZSf3lCc8k7kNBVzTSLfgZGOb4Q5QnJ01NLWqSBdwI7NP0ufQUMGcy07VGL5QkK9lHLY_cAeXuNqi44hvpn3JShHBS56NsuIyIK65QvqvaQMDuRybWRIMUM74LDcub56T5ENg5xDDfRmogAQP34JjNUTaKY0Hr-Hf9Qwr03ztGBYk2-Kix_EDX-IAaFF1zPOwaKlLQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rws0nj6R9Kobaut4IMIiNYQ7Rll1cZoGF2fxH7aiMoRSAJhOqAkBMVU8CaPDgwrGGqabiSciBqHqhRBkD5Nb6jYn9Gg7sGyxKUZRBNacVg6585B0ME8oySJGkI41jL5jFZFE_SINS8HQ0Wt-_KXa909qBoWXQBVLsdw3ZRyHpiC7fj-UVjI7qCTV7J94eTkqafutBIVz4VJ8KjLQMdgqnu7IhRDt1k-97Oj7Nfz8dRE-Rv0g5a8d7tZJP_B9GK1uBubKuZ7EPcI9Fs6nIoHuQY17fQphpYmjWrlQzHMe90yZNIa_x5VPimGsX8tpZxMMctPE5H8xLRDUfbKxLSANQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=NS_MmtJqVLnVE1Zl03MiSNTS-rI0SbBiDPUN_WhlPD1KjTXYEJFJJL3p-aSgrbSaWvP26YI8yeldoIrugACJ-Qv5hAkua4VY6fwLlcOhdeAV7NopSRtmC-O5977OiB7dYl-BDNXCvynd80yuLxGxJMaAFUn90vJyfUnfM3HhKDFWSUc-A09wtkXiGJu0uX7oKVz6gf6KOnH0cE5uWwlZg91oI1byLJWbuFnb_pigbRZdkqnhbhbtq56Ny9vTZGLcaYTzc05G7xUDH4jui8vtY1dRB49jIRLkBtgQqM-0yDDeQ6XDtMGYE1fGybldVLYuFo_HdZGSTUFBgl62xzwCBk57VAqXEQT4QikNeqOlDhMd1rzoL-ewPUc17HzHZnpypcsAQW0KdZjfPy69GW12mQ935kd8dsBzfIo76QeMKs0T5ci-984JRtS8KtoVfocV8wofmzg5RKmG1OKPyC5uQtlmG0Noafm3i0fKHGpgDzhaeB7lXODVEZ_Z3zb0o8EC936ASWZb1ZubkHbbZVh_ZOqXF7-rRiotguQrtuP_X2-FWj23abi-Ew5wKuYh_ZkdTdP3QeKPMK5z1BKBsUFbpklmDPC9zHAtw7klv-noigVGkLF3BvBLyUzPr1fIiuX2bcHqxLbLj-OyI5EpjhznQK_bjlM1GXFhFKXtolkCIBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=NS_MmtJqVLnVE1Zl03MiSNTS-rI0SbBiDPUN_WhlPD1KjTXYEJFJJL3p-aSgrbSaWvP26YI8yeldoIrugACJ-Qv5hAkua4VY6fwLlcOhdeAV7NopSRtmC-O5977OiB7dYl-BDNXCvynd80yuLxGxJMaAFUn90vJyfUnfM3HhKDFWSUc-A09wtkXiGJu0uX7oKVz6gf6KOnH0cE5uWwlZg91oI1byLJWbuFnb_pigbRZdkqnhbhbtq56Ny9vTZGLcaYTzc05G7xUDH4jui8vtY1dRB49jIRLkBtgQqM-0yDDeQ6XDtMGYE1fGybldVLYuFo_HdZGSTUFBgl62xzwCBk57VAqXEQT4QikNeqOlDhMd1rzoL-ewPUc17HzHZnpypcsAQW0KdZjfPy69GW12mQ935kd8dsBzfIo76QeMKs0T5ci-984JRtS8KtoVfocV8wofmzg5RKmG1OKPyC5uQtlmG0Noafm3i0fKHGpgDzhaeB7lXODVEZ_Z3zb0o8EC936ASWZb1ZubkHbbZVh_ZOqXF7-rRiotguQrtuP_X2-FWj23abi-Ew5wKuYh_ZkdTdP3QeKPMK5z1BKBsUFbpklmDPC9zHAtw7klv-noigVGkLF3BvBLyUzPr1fIiuX2bcHqxLbLj-OyI5EpjhznQK_bjlM1GXFhFKXtolkCIBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0I50cM3LVf_WDQk35nJVil6za7zwHIIVQ46maiQyWVLbS6SwFBckHkWDyPuBIH7obgQkKEj7M7swdK8zw9aQZcqjBPD8muVS80qf0DE8A-MUGuhQO1sBhx21ZQg7XsxqpAUgH034S7zTVr51ZveSH7jYO8KpXMXqravlf-0chbhRajmhZZINHLlHkG3JbHPrgoilL5KRWRSIpw2W11Z4QQKrTNnl-k1t17Ba5iOuEGinqYjT_V_qPWOoSsBoVFWi0VGvkdQOSXNhup4rAWwgY_UGEcvuQt4UJqOkStYxUyPDfDVFShnO1HKsaaX-ExwsTAQCJ6g6ZwoyqLdqNWEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHyMJbAin_2qjSonQhszM37rMKU-L77QD7nI6tJ_iQv6dSJgClW5EIReLkQNXelif2-eO1rGCNcCm4SzaS5g99H32hIAxcUkeSpEY_65qii6o3Ti95oEhxxCkzYHeqbTEYKqdOjDY17iSywCcG4xhHHsTsI7Vw4phxI9UmHfaUTBkqMoJ0Mn2GfQlAzngES_7ZywuDkMfgO_qX2_yo3qXJVag6RWoHgqDkOmN41SuJnYIKBVSZTHNuGQS_G-mB5JKiFywzo_poR6x1wa0E4gdHLmmR7gmQAfLt_DtnLMYRkUGBiLLHlgloAcHwoRsu_msy9FGNqXhut12XqgTiiOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=GtGxXCWC_nBDKbyB0PjmSVta3aNPgkXqXboWvwEAaYkpH2LVFCv6mqn0N7BrklwStSVI9o3U54wieKthVYfQlT-etCpjIMswX_rsdRmTXqWev1GFlHOvfDh0f-3C2xK3boE6bWgneE5_FLUBLpL2VmgCFQ0aX0arMQsdQxglUMYnJPKQAJu73O6YBpKvfyrao0p2f1Ux4keI_VX3UKYymurpQqSdkwrIiwtfznDoUgOH7apJZLWqWA3LJcVsmK2gD7L9WyQD_ZTbFIPARlzMg2R_JesJ4riGo9Z6bnCX8YgDR0HgQHh2VId1Bt-Yzs_3iavF4VT-0GlOhwML17ohXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=GtGxXCWC_nBDKbyB0PjmSVta3aNPgkXqXboWvwEAaYkpH2LVFCv6mqn0N7BrklwStSVI9o3U54wieKthVYfQlT-etCpjIMswX_rsdRmTXqWev1GFlHOvfDh0f-3C2xK3boE6bWgneE5_FLUBLpL2VmgCFQ0aX0arMQsdQxglUMYnJPKQAJu73O6YBpKvfyrao0p2f1Ux4keI_VX3UKYymurpQqSdkwrIiwtfznDoUgOH7apJZLWqWA3LJcVsmK2gD7L9WyQD_ZTbFIPARlzMg2R_JesJ4riGo9Z6bnCX8YgDR0HgQHh2VId1Bt-Yzs_3iavF4VT-0GlOhwML17ohXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzLzMT34n1TGDMoRORXiWvS0qlvJLNIWLze9-GhmjUB9AkGKUeo9bJQL0UHFW9IQCtziHFPWjeY-lkqsJGPHDUWyK9URppBTw6oVj-cNivWVW04oPO_8xZ_WLY74Hgnnlh_kmbPqz8yv8qWq3v_21zgHagUQSqekEKwbzVMgGxtF_KjJJtSLPSmEXgC2_enMnM2PaNIoDO2686G4_5lKf4l7lc6vJQTYE-oIb6wTbEwmUabc_OSv04G1LSDy5UYnIrmyqedTf7utk-U3Wj3xJqJtyU1MbQrHJ_iMaxXR0c63Wp0-gZ061xj8AAq_TF_AbLpmBngHJThE5VlFM7vyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi7hh44U0utzg1I5mlfATCOMUzlxW0foL2buqMq_3O9IkvpWhwAOIiNWOLWpZ4ydWdz_ss3FM_JsZP7XVa8ECV6GoJNbwFC0xeSE3r8QWboE2-rIOZIAZ2BzjZEOlDqzlWko6HG_IpM86C5zyW393itW6mgZtJ18cJ9BQLe1HqInn0-ctGq6TlNF2WqWrzGYo7SlS_RsRP9t3yp8YW3mratUHVlC9QofE6gM-DlSlG4mtDCdOhgjptwPr1SpN4no59_mrR-3S-3Le7nsmEJ--0DOxaR2a4FbBEaKZBD2Q4VccsMuz0e-iEC7OAQkc7qtsabeK7txkB9H5h03-_N7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=dnJh9rak3HuTZQltJEg5CN8cU_rPvIPFzRzHbVX1nowAjzQe4AFBbTIORKS1XrltZuUakHelvZaqWJk2_teOWhrEmC-5LrP8DNXkYePHAULs0qMXfxSgKLfQ8VprhpSsaYrLyJVUSr6HbjEqP2XhuLaqtC9R9ikboFQofbLlNP4shysCeBFqbACgUX0bfpYLrcjM-Mi0ye01TXBPo7LdzqJMB4LYGW9ZepYwRUgWTQDTDE1ct57UBID6XGzKwRVi6WwceL00_JaaDYOuDy5nMThTY7Cb96M_IUv29X91zCHHP_QiB_o0ooctxlzjB35zl7GuZwnw7iWwDpZFV0esQ2Bm8MDpHKWJC3SkDLAS3ULEa6M3XY88l-u78Od6lgLyrwR1SlnFLwPGdknulIck87_e3j3-QVViCWoky7Otrg-QuFESDkdAIuCXdOWorzAxJuF321YttqKEnVEOyri7nvsRsSyaOhzwCSJmSYowGKN9aYi9Bl429obwXlLoXdoolL8y6clVPqIsPaXOX7uyo1DLhYOPGou55MlqiykeOk1pIycosEsJ0r6KAvzK_9LL_3jf14cNHJEE8m73zoaupxdQDabWHKjW7AL6dhTJVK9Qvvy4RnlLIzwsDNLK5BelOsEGDD-65SXg94xyGPh_zDfvl1_tmYJXjSzxgCdDPLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=dnJh9rak3HuTZQltJEg5CN8cU_rPvIPFzRzHbVX1nowAjzQe4AFBbTIORKS1XrltZuUakHelvZaqWJk2_teOWhrEmC-5LrP8DNXkYePHAULs0qMXfxSgKLfQ8VprhpSsaYrLyJVUSr6HbjEqP2XhuLaqtC9R9ikboFQofbLlNP4shysCeBFqbACgUX0bfpYLrcjM-Mi0ye01TXBPo7LdzqJMB4LYGW9ZepYwRUgWTQDTDE1ct57UBID6XGzKwRVi6WwceL00_JaaDYOuDy5nMThTY7Cb96M_IUv29X91zCHHP_QiB_o0ooctxlzjB35zl7GuZwnw7iWwDpZFV0esQ2Bm8MDpHKWJC3SkDLAS3ULEa6M3XY88l-u78Od6lgLyrwR1SlnFLwPGdknulIck87_e3j3-QVViCWoky7Otrg-QuFESDkdAIuCXdOWorzAxJuF321YttqKEnVEOyri7nvsRsSyaOhzwCSJmSYowGKN9aYi9Bl429obwXlLoXdoolL8y6clVPqIsPaXOX7uyo1DLhYOPGou55MlqiykeOk1pIycosEsJ0r6KAvzK_9LL_3jf14cNHJEE8m73zoaupxdQDabWHKjW7AL6dhTJVK9Qvvy4RnlLIzwsDNLK5BelOsEGDD-65SXg94xyGPh_zDfvl1_tmYJXjSzxgCdDPLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=AIBeFwOfKht1u3GeXQiUI0zV2C7d0IfUf7vIdXxQ0Sqx2u6HRc8hTE8mOXBju2O5liq9ATDtwXZJT4vOzo5nqO00mwehiwoZzCokWFgxonmq68jAysaKw3qCULoCcuyPVdwmKwRoK0adLIlcyUv3m2OTvRNX0VyT5p8qQC-QN24j10OraPWOREsHx66zpDkqCSoB88y9EXkQb3bhTdsblxMvFL1lYIGM2JSjCZSswNXoqcrUCTyMAgWGnWFxWlOAWfIRX_QZWt5XbhwFxILZO_cfUzMgz7O3QyatYrDkSGx1XoVij_rhrgnJtW6HpNg4bMLn5JIM6XtoZ95ng-GGLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=AIBeFwOfKht1u3GeXQiUI0zV2C7d0IfUf7vIdXxQ0Sqx2u6HRc8hTE8mOXBju2O5liq9ATDtwXZJT4vOzo5nqO00mwehiwoZzCokWFgxonmq68jAysaKw3qCULoCcuyPVdwmKwRoK0adLIlcyUv3m2OTvRNX0VyT5p8qQC-QN24j10OraPWOREsHx66zpDkqCSoB88y9EXkQb3bhTdsblxMvFL1lYIGM2JSjCZSswNXoqcrUCTyMAgWGnWFxWlOAWfIRX_QZWt5XbhwFxILZO_cfUzMgz7O3QyatYrDkSGx1XoVij_rhrgnJtW6HpNg4bMLn5JIM6XtoZ95ng-GGLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
