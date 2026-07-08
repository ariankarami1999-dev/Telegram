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
<img src="https://cdn4.telesco.pe/file/Z78h1wQn5tDrchqtg4Yz0Bkx-wMdPgIuOTETZtTWt11oMJ0Kufl9pM7lg3uGAxuswBPeWK6vFvVNZmQQQ9V7DM2omv_27kdRwiraMHI2scF1WFLxZjakyrdxiboz5fDOlexAF7dDp_m7R0vAaIw3y_fQAJk_Hpw9SWH1p40huxq6HMBtrBmYCisBZ-II7FCBpdMnacDA3AKnt55Nubbw4QLC3FkI33fiP9raoVOVZszdC2pV1nPcYKW9DJKZERnyGG5tWyl5g-_6tdOxsD7uXfjLIf0QrDIEQWlmZEevWAQx-56cVjgymZRJELk_A3tQUJiB_NUHCHhkx_HFxUfocA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 422K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 11:13:54</div>
<hr>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwkMYG5uWb3yXqLq2ZWSBOZL5pz9Wd0jDNsHRKOhXuzyuGo5kwIieryGyYn81MU4tz8_sta3vfScxSN_RmsCPLq6f6zF6dSizLrvwNuWnBIUEyc2CdTyQD4mgeKa0VoHB0lw_Ou2PFzNL3Dvde8-FGXHtDdiVzhfH9oZ1jTI7xfuWFR79hPBZoTC3GBubNzyeUlKdj9oRfwb9rr4CfTmQozIh-t4UZwUbrZscszEeF2pPLCgLb1cnjiJZEyMHfN540iDmDHXjOJxwCmHFrlR5Ixleen4LEvzg6qIma4RDDCb5Buh23ycqKLWKuUa9rtD0oO0ZcS-9GgoywjASx5YPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAMCtsOKFAneuywziLtQw_-YL8SmVMUt-Igh74AdVUkVxALgncYEn8p-v20wJzCQahy97rWisjAbmzOf9csNUqxT3r91BVqxv2LejNGNiUJV5Frfp1g9is69nbfNUnxuXifNorud9vHeEzuWLxc2MAycntr5Bv1XXzHZTXg1RZpJegxFA15ep63iGKA7DVLqr5mAwZMoEGB6LLCvfcJUBKGEqzh_mDAfEgYFv4tpqx1aataQtDkKLE9Sn42_ZHWRtIMQ3K_fEaa8-o9iPCWYYYPi9EHpmtdgqlCZG7tl8nYzbMp7bGnwiknaDvNzm5Ip35v9HraCpNGYlOV0VGMLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYROZbdDK_NxMC2HyUbQvOf_qT3p13ltJTvVyE_a7yLuE0urp9TFh-t2R1hfBxLiOOhoZoCXKDUB2_53yNAdodTb6GyLbssibuxMozQboLN6APB3FNbB2USyBftbFoxeSFfjcuc3E0VYP_oI9MeAaEKTdagFUfzEOQmeY58DJGYzTAzIz4IyIYT1aAJVCpS1ZsB5lYPCh2z-KyG8uxgHfoMKqRqlj-x1a1LB8kd_iJcUE8DedeEWt45xzdLB1jJxq_NPjOWxK8GXJIFjbPnDJn0BlCgOlNrU1QcCE6ufqMGzVwHwol_Ti0F-4F6cY3K0OmMJukmGkR9W8MGbzCBzog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGgaRuVbRi6f0hNF49iILqfBBmbHFbJGO8DBNrP6YEe_2Mln_KAAEcKh26egBlQPS1QGw6Ykw2gTUI-5quIH_Yup81i0uyEEHZyuQj46LsP6m4nZhMs5Yqpus0mmAURu620W7-GaoFKdizNcQXYFPV2rJiKmQCZ-R9J6RGtn5l6hwXPWRpbXycqMd7DYrWxhPFPjcCLGlrguUhAUIEB1KbCf9Zbq9QAHHhZoQSVLcGfFpu5pU_3uWGLa_dbXzcJLuuFKR0TuAQnyRbnT3O03JSiIoF3UhOliWzn0J7q4L0VuB6vzzE1AkQ7t-Xar974lymqCIXUCgVhe7bBypVZyMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=axqS-ADnNxhav6IAehisNgBTo4DxyqTmOjPfOpqCT3IXPg0BssEnqqdcdz2DkHFbv5eeYj1caFEld5x7-tv94vtwvSTQZAOGXBspaP5GjPgDc9E9XEyOaGH7NI2r31CPtsWyvdQEkFvPU3ZvnTjg3883GvrdZ-0wt2IVsNyNQlzM2l64BDlYBi2S1V3WvfEwmZsy39eV4rOFXHnL5W7HqPgOj810FKAnbzcp_K1X4Xj9aVUmKo5WtmQLx1E0_BjBg3iOsZS5zajEBNPTzQXpkkqQ29Y2stAAYosmbWmdk0MOD3LmDMIgfVJEX5mp6G55TaMEmbLfL4FdjKdxz-eikg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=axqS-ADnNxhav6IAehisNgBTo4DxyqTmOjPfOpqCT3IXPg0BssEnqqdcdz2DkHFbv5eeYj1caFEld5x7-tv94vtwvSTQZAOGXBspaP5GjPgDc9E9XEyOaGH7NI2r31CPtsWyvdQEkFvPU3ZvnTjg3883GvrdZ-0wt2IVsNyNQlzM2l64BDlYBi2S1V3WvfEwmZsy39eV4rOFXHnL5W7HqPgOj810FKAnbzcp_K1X4Xj9aVUmKo5WtmQLx1E0_BjBg3iOsZS5zajEBNPTzQXpkkqQ29Y2stAAYosmbWmdk0MOD3LmDMIgfVJEX5mp6G55TaMEmbLfL4FdjKdxz-eikg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=WxAkFusHBrF9pE3Pg6IGhnPbJNkb7kiizwovFazQGB18JgATtsNqWzEFIKrGys8G1ZfmMCrI440AuQoVCNo5cajMff3OBdEm0OsCaBuiWj5wtXFZxih_5iGzFvSWZC1ZS8PdteK5YacYha8Lg8dYSNqKhhlSARAHCl5CIboepXed83a7ldDSiNd_SSPdx2gVOQzIxeX2srDswhO_Or72pB3kdukQPwCDTkfu0nw4HS9jRs2Aka_oeqrN5dUcNDbHAplXDJb6xGwZ-kyiNI4mks2qWDx2-LT62tWmSUngXlhcxgQkUKR3Q6ZVuHVUKxN-g34m17OlBbt-RrOJHkk8yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=WxAkFusHBrF9pE3Pg6IGhnPbJNkb7kiizwovFazQGB18JgATtsNqWzEFIKrGys8G1ZfmMCrI440AuQoVCNo5cajMff3OBdEm0OsCaBuiWj5wtXFZxih_5iGzFvSWZC1ZS8PdteK5YacYha8Lg8dYSNqKhhlSARAHCl5CIboepXed83a7ldDSiNd_SSPdx2gVOQzIxeX2srDswhO_Or72pB3kdukQPwCDTkfu0nw4HS9jRs2Aka_oeqrN5dUcNDbHAplXDJb6xGwZ-kyiNI4mks2qWDx2-LT62tWmSUngXlhcxgQkUKR3Q6ZVuHVUKxN-g34m17OlBbt-RrOJHkk8yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjMYdaezMOmA7S1kV8SQmfmy9o9Yt7kPco8f7bNgw-i5hq7CMV5hNLZD4mUcrBBymUylFt1BQeTjVKQd-17s-oZviY-gmFMVGVM1ziDprzTy_WSvfdWVKqtzDeY9OyUVK2ZhqnXxQaTCV9zBIGrXigWrWn0pUFWbJgP15YWeRjj-UmZW7AHGAv2eyRpqnhmeQf0TgBk7dLqvjhb5HcAyCbS2nVZQvwnPOe2FCicQogqav9dD9XnGegCAzhcK0gDxp9t2HXDNGAmlNGw-RukVpZRczhcoLJ-WCvFYevezMA1ObNPT1V57QxAY5kyC7Tu2sQ5I3ZyXcmS177d6ffZSMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_YCvpSJO7psqko0jc87T4B-kgA7FDZ-Bu5QRngCa43alzva7RNcp8RlheTGAD9zK8Wi8IBUyKW_pbyizPgavZsv3KU0SFmBZqyxYBnjqu7d_T8adjOaXGkRzT3VYs5U14v36h-GJ6NMkeC-vR2w-b4aAw9Mry9YxMChzdOjefT8nhrTjihY_qR6hpN0FpQK__x7q8wP8E-w2aipMCwhzbzdzjyO93xKJwsAT3rAWpjnxw9egBtoustmwQ7XcJeDk2Ambwzey0VruakL1ATbH1uC9SlRaaYic1maVseuGtHCuFOtkiX-nj3DlvGlpSCG2z9w0qPfb-tFXCCgGTBnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=kW_JlHVP64hbYAPTGzLuo_gchOAaDfSIz2y6IRWDzjnyrWMIAMeZmEQLjHOr0ruHWu2GjoqDlje_QrZBW2Up1MOqgQSjHJO_TEUCICP1Z8LHs3hw465XVIF7PHHM-oUVeYr2Yu-cm1ygLsIIImJWn_CAGUFU0MNXVA5Bafs1xC3E0jwd879RPbgvpleI_FZ10bvgnaMhEWPkzzYz2x6A9wvY59lJtCNfw4w-JyrUQWtXpoOmmcZktN2bMdhDFByPB-UzBMWxUp1-j6w-MK4XkdoEzFqXOE6G8E1U4hCr9fCDHDdtxUwjLqM1wPg_mtqz9XgLpGQdulKKe5yw6RXmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=kW_JlHVP64hbYAPTGzLuo_gchOAaDfSIz2y6IRWDzjnyrWMIAMeZmEQLjHOr0ruHWu2GjoqDlje_QrZBW2Up1MOqgQSjHJO_TEUCICP1Z8LHs3hw465XVIF7PHHM-oUVeYr2Yu-cm1ygLsIIImJWn_CAGUFU0MNXVA5Bafs1xC3E0jwd879RPbgvpleI_FZ10bvgnaMhEWPkzzYz2x6A9wvY59lJtCNfw4w-JyrUQWtXpoOmmcZktN2bMdhDFByPB-UzBMWxUp1-j6w-MK4XkdoEzFqXOE6G8E1U4hCr9fCDHDdtxUwjLqM1wPg_mtqz9XgLpGQdulKKe5yw6RXmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk_NIDdoaCiuxuUvVA6yPdnC65rpVBrA4sXkJg8k8u9t22Yz30CFx32Q4Uk1eS43p1ugY8e_1bSitRUxGyNXispfedPFD6AeSjz9ZA5C22DGiXZSCPcLx6StP87sbdcCidESzil672JO_waScvrz_gsgrspD7OArzGUTfzksOAkPTTqZ7-QyhWcbe0aR0bFHN4FSxepAOT54hlz43K-ghgmAQStESC76q09Yvph1S1c_AQUp5M50HCrYa_XL4sUt2wKwc6uSq4YqfLodFoP6lC6ghxEyBjRq89XQ_GFqxCV_pdwFghRbsQVkhsGiLdvf0VIIf1c03mhEqan8MXx_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU1uswUELUJkxt2JVXs3dEvCKxnaTzR9QhTZfrI4gIXwtPMN5y2_Sk5zTJioi8c-GcZP-0veotoHwJwZBtnN_y4rdE76JIj347eERATu-xvVSYvgewJ2hq88i8D9_sBXhvkTUAw7WOcBZ_ZMyF1mKe_T6TgJoqOpIjnDEkijKrsm6P1BR_ODc9IlMfFN--40l5wcj7QcKRXk3w-8nAQvpGP-Ky6qvtTm29crg4rrwKVWk8YSNl7MwzMy1-LAQk7uMP8RbFXdFOyi6qMXpTK8WHC-XZr8bptfMRAfVp03Q8dWIujMB8xVRAqd_WIGgN1FrGWNjSBGuJ3hQ73LQJyQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lutGogflxoDdJpAfyNdOUlv1FwATUMUEOM502Q3OPp-Ds-C90-TdXg-bvo4up33B_nbKR__gPTrDdTsKSDx_v3X4HsP605_rjG_d-l_Jx0ODpclxvjKQkzt7m9USCot8jMOKQEaVv5-HQuzFkSas4S0OfK2s9CZVbT_F6h-azhvgmcwPAUQBQJI8Ztk_Jwfm2NXzV_CmrJFYI34ruaFweR3lIOk8gFQMslFyjV2u1B3HwHcc5xh9v0PG97d6pOZCg8J45ydvmNqvHjdk1SlMWYMbH-ByhSO94yo9rRn_QU48vzdXVqZ-A9Sx1Ao0wCbujsTacCgGlJ1PjZW4VSIqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCG9v5fdWmLM0vY6qUfv-TRON_7EhKOnP1tmKnQE0scQP6-PPQ4RtDqTxmsxRtbh-MQP_7xfrp3iIBQsuIVBNWS5rPgqNvrnnHLrG87AxcBWq0zRA1pisBOoilbEZIKhhv_JsLZafV77j4tPx52CP2DdPj45l46EHCot0L2VA-c_-gXFAJygq3OilwL-FuX8nP_pdtSFRMqgXJ1kLlq89mCVT95_hULnh7zJP-Cff1ZxkGJSdYlvpxMF-ZQowwDfkONSr7wqyB1WCep1l140MGxiWp8iQeM9eoVgDVkS3akzkK5zCGFSBNG5Le1LElsXgjM5S-qFyiTGAjJGmJhvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNKgtdNihLT1mWdloNuBY9I3JTvudWyMSdDMsIyLhhcYUagBfYsu_ilZihVTvvSADPZ03BqpfLJkr6_LlJLw526yWE05E11-uDYyieeWqvgxE7nAw27ccNetAJMR4s6eEO1ZGVNlb7PQmgdFiK9uyD_9t2PI8EAAtlxLfL-HEhfNc8snCnmlAT93ffMo5PFRc9jQQAtn266jphqg1NJcVtk2SuH8OXYGJCMXGLSUOCHMtLbBoBVLeHVn0Ylst2oaptzyukrQXFrK-fhVpiLH73n1TxGO-AlWZLIV6BW6cSduArmDi_YvF2RmKqGSVNnV9tH_z5p-G5Vm2PBmUTP0cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
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
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25177" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBSaCDvVU_dZ1bbQs9RPPwEQZ0vQM-TOLJH_R1hTjX2Fyeohjrfv2Cm0L1GVI6OBpGZ3CP9F021aeBDS49VT21RSWGg6zM1ky5Vs6SxNbDlWIeaLNTVST84XWaDaZPXnVgFLVqZxt4n-avolVwVhtfTgA36G-a88JBGNyCn2JBBNvgExuz8W7t390iLuklae5Dm8MfEWJ_BOM6saRqLPDRG4YrbSDUzMYjmfa4CHA1iJaJ-L2YAB4P0s8QY3LN3MLAGbwJIamgf_06Xx_NqGHZQuxztINeVkqmmp4A3-Gx2G_Jh2Uf6OrjA_hOGo44s21vrpKcarZ8BAW4cdv4ZNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu6nBctNXkuVfC7PRwhvv3V__Tmk51WTuWxPupeDBxAGrIRfgj0Rhn8ZUxSDu12sB4U9vdC4MkUrzzMjxtt1S8qJJ95aqsq8qisKlHMgTaQIp1m4UqhU9plt6Nu2MxVy3aSPLf2akV6ucatFW4jJS8Viudfxs29N-0jd0cwezse7r4RgxKBFLK3QSDwVX1xSRPo4grqSPLFtRrI-7uclioa8EF_JH7itOqFSShye_xQUDagqJZt1UpN5_imI_yfGTUbYY4bQ8HgMGw1t7usQZo6BRkxw5-2ns11C5r471nSbRyS-CWGQh0DH41tJEpfp4hXkcF1GG_0QXp0f3LZezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdSogmpwQvoPWoF__nmzXljdB4AmDKV4QQg7w6Ij0Q2gv5ErTFhsbKyAsyCaACuHUw7iPQxOr-AvFI71_-elpqNDyUk_0gAUz281-VzMYm4INcSHllTXufA1jHrNvlTKmP-EJmp38wpWc3jn-N5Rj5Q_YAk7F6DmGm-VJZF9D_WBshHv0_wTs_MPt8t6CWfP2IzGAV9LqAhCzguQOlhAUkXwL3zMbQn6oZam2wT7Na2np8s9wycNIL1J-vKcQ4H5FnazwLbVWRMU5W3GKWjGPHysQdI-xseMk9qDakxqoPHcCgK36JwlfR9-LCsyTGq71Iw7AZXgUpFIvqAxwmtUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXoACGSJ4KA2dHO3RvYT-LdbKJiPfZbvAgBpir1Fa1ObuTtVRtMorRwJh1Gdgfr-jRQfm0jsOivDSI_aKGvTqGlvX0dvJ5hIqZ09c79BxA1VHZ4G6OapT9dutu3l1R_Nel1uK1DsVxPhj5c9DCguCKQiZgqi-3Eqb1pEh9-nQsXKAl1ABcYeB_nX8jdQEMkGWRrSssTGBij4-3lSfxYCOjGMIPZry0cITmk2fbqGtftKA_wIAsgWfI4a6EjBIIYpV12ih-crZF-krSaeuMpn46ulhnjw7vpNqJ8mgpxSYv2r8hf6wgJE5yQngYzMbSFFBibIPY2iSsWwUyKmrWOlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl5Bc0tUmuT-_bLjOpNx7rscgVe-ubT1-pEwVMIdfk5KAMz34fmXJVk5OdX1y3eXK_MsVJVkxjWM-npvD3kahWkIt6w7HUx2PfO6GHJ32Aq2d3daiS2znH-LNgzY347QO1hmhw1zw0PdEFU1IVWltOZ0W700jKf5U6QO0U1hLR8m2U5g_AL4uPAp9nC0UH2jcaM2LFvgXPfmDKa11hYk_3pJN3iUsl5w9cGSYabKoOJRVB1mvDfTfKvPtijnwzBMsCtm2LL4ajzAhitoXg8xZ37k3UPETlesrkYgCvfx3FJ_6RwdaWgIOskzhoXDfC7bWW_9iM-JHyQUr8mqZeYPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl2qsNJMBs8emrfkYcGMhJ9wrHiqMbZx3icni5rp3jNyGpQ5hH6kAIffqwGfv28Y2gjWrwxwHUzUbvSt5iJdg8_w0zAAV29Dnd5Wg-d0cByGTNocieR8zHntDksgf-t1mdbKbrbIYV8qqYhaNthKaVXeP3vgdZOoNflJ2jtRCcEOB-GIEYL90vucCLvflcWYdHEEKyxvmcbrueInzzlFra_5W_6v-iKhojGpXH1H7hbuU_IQVjqXwE6I1KWZxfAmeu-sPQOsf6FEXhadp8y16FeuU0ZzVSnMWN0gHEKy5phXctzZGzYwAOuKFU1zVIucty2mzaa6GMqUc_rmx71G2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0uMJDpNcrN5UrvSH0vtkH56DQgz8woy06T0b0S6aR4tyMJV6SX2p_lfSGKTt3KHK9rw4PA9DiS7XXb3ucQDP5ss7I6HiECuz0Rar-S0dkdMU-vezyUei29eCh-V6pcb1hFfPtnpveJ4trm952Cs0ABwPVgBdTXLGbb4xb09cQzVDi9_kv6XpFVjJyBufkGBzgh13g0qxRw8-_52ToVx6_G3lt1DtVPefRSa02hN6kubA2aAoLsyYeotfZB45oUP24xznDYwDrFZ39rYiqFotDnEUWSGZI1hxtl8P5UaIkF5VHt4eCdgBgR-QiSX9mRunddpU_EYRBuAD0-hz17WMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZGZ64jq6wTdRMfItnMveCJO0vhXo-n1FqBteDytEKd9R0cRJL_0V90h3sqNv1CWdHl6c6vOQ48sghVe7_2tuITDvkmoMMjxMIvctHLqhwwFSIVCntQVBXfso3cQSKRQumF7f-iZ6jyDAzb8rsh3qOtuI4SytIx3MG7ggLI3H42UZ_JgODgbUyxYFueC8rJ_yariBWMv1N6-xxrAIGvyYzRIZNRaR3ds1dGmft9HLCCMdUkCvMjAI_Us1rekNuXs-u7VFUqsuwE-uNXTwY4ToyWt4uD4vUlCZVtu7NVJCfHXqPiyTqFHnBrtmPMJvb2O9sNg2_4L-4vYKrb9dCQP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EevuH8qBf3x2t_6cCO5UJ5AgG2CtfBzYhNfRuvteBF7b2Bv5QMik29hYBA_AfI83-RA8nNmBlxc1iookMdgfHFTR9EOIVG9r1skijaLRyxiDXbkm0Pw3yT_0g-cf7tmsO-SP9HN8KnTcKme9aR1IKQPQ6rdqRSqYBCI2aYOIy1e_o8zKcpYOAqU18lRqXPqrLPmlnSS8FpuYjEtNOwxbwLgY2o-QyBGxEBS8lKPYkmw523lMywQicJuMhP0jSVProFzAhYn42aeIF58TnBQw0Lu7IiBBcVTRF-Qgd1yLlyB0JTXY0QKF5hclqI-tkBT7NyVOX-wFberEX6JSjorZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go77RYcIgWCvVZQ_TS4jOvg-3dAn1p5AZScdfeHMenKVPRIKGaYGTeaHUWygGvb4LrK_4fxwzfrHAlBox-vaj04jkF_tRZgV4I8iGygtD7amBn16snv5Nc-C9bInY2VBM4MkLL1onKtx0ZZBQFxnbGF9iDFifzK24a-8r4mE0y4KT96gDOqXjBBTBa6k9CGKzi45a7UmoWrS3JdpNU_h8iba5j2T8V0Jw5KJHsA60Z8ys8_IaJV4BTomJOEr7J9LqBYIwR_aX5XNLafFfBXLFJDCmaU-5lJseFgN7DxdhUWvIZbqSxxaPRq4euXp2F1ySjgpebtwxMtmnTeD3PDqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC1NpzQ9xcOd3oqyqkVrk0nS6oxIxq1ujzusRj85PxSy3WR4Oi1FFrVsm34jLbYEOvtcNgT68aTwM6yQRle_8wId6Gs0uopMQJhK_R9PqKsoxjjtYf_YovZe79CVZrevQLIL5uphGlguKgoAIfP3fG6v3EF85sufAmjrN_BKevmL_oxQj5_YcU_bIFOqwCInIXp98fsEbnnYWh2xjggWqtArchZBoHBkqPpqxMVLbunrtEe7gbmKv6PpQeFO3ZZ9GCvAdycHHFyxoBbE3AZnHQv72DRBg_XDIJt9gOret04fEjv-Sc7s5NpPUKl6z6OGKnhiDvejbzN1D_FKIL_mrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpKMI0q0JREo2s3xFOuuCcRZolMw35U4TdJfdnadNDa-IPbJ0l2W8lv8yV3-PQUV-YWmw1ttOI3Tg_8p0YpU2O7syZy4XTL1TjVlOuekxYMwNxh2IS4tMRI5tR90lW6utgYCqAYOJQPCsrxv2AUnGjQkJqnQC_iOxT3d04zgkD5xHHWXbWGoOW5R2anMpQecO66GMbFWN8wg_Y_93e-Oac7Djq377gY8JAcRXosYOiM-65okbBS_qj59pVhqj_MC-8m3kAKgs4082_nua53qP-y_6duf4DSiZg3N6DvR_QxfEH6lzxzLTIBorL1Vm9nQo9PClrreeYktrqSV2RMebAn0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpKMI0q0JREo2s3xFOuuCcRZolMw35U4TdJfdnadNDa-IPbJ0l2W8lv8yV3-PQUV-YWmw1ttOI3Tg_8p0YpU2O7syZy4XTL1TjVlOuekxYMwNxh2IS4tMRI5tR90lW6utgYCqAYOJQPCsrxv2AUnGjQkJqnQC_iOxT3d04zgkD5xHHWXbWGoOW5R2anMpQecO66GMbFWN8wg_Y_93e-Oac7Djq377gY8JAcRXosYOiM-65okbBS_qj59pVhqj_MC-8m3kAKgs4082_nua53qP-y_6duf4DSiZg3N6DvR_QxfEH6lzxzLTIBorL1Vm9nQo9PClrreeYktrqSV2RMebAn0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8U2Y-KrSENCC55PdfTo8RyIvgNWDzUgjuxsn-j0wNr49BWVdDgU_hxjh4GVo1vF8oOrZ5qNWyhY_QamwyYQNsPbgOc1rkyYitGQCFwlLKku3x1pwFrSLys5YMRH--J5dnO7antUxCyZo01IciltjQNzV8gwKO_epjlNCNB51zn54AbSs4ebTw39Ani6ExzrgquWdJWZey13m9yJ-1Cj1PAkXkcI8735NWScXZa70YvQUI92Z9mhO8FunlMdjOcsRTmnH0dHi14mqHIiJ5nVB7A4wqUdvoAV_LerJSM1ef4-CxcQwkJBmPJHQZ6nAAw-IvUgCViuaGp9leo-2_Nl7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STFmCz7pNbnGDiEJhjCT9iAF_5pER56-dnbNrT-rrNLMxSoK6ecq3wbq-6mT-uqoMbiRd7ShX7rzrC1Af1Fg2z-P9SSqsXU9yam7rXJJVHQc6rFzY4MMwW9zgFJFczQ2xHLNNnjQpEEWHbMe5WnerbcgkNGQ2ylaLq7_hwSD0QE7tLb0WPW3xrWdnMFz2Tzij_haG7X7i0X7dDlSmPA1nVUvsAL8-Lsam6LhGvBnSTUHOQOEklGEvRvg8xIPdKVh86pNoxWwiU-0dBha8GBtOYqLdzcVWmjQLo5Ys-ZKEuJLptpAqNG7xjBprUCavYas0RyIrBETty5aJeNzQESxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_VP6qvdKRGe4Vyj6TMf0853jNgm3eG5X9eTIXr7OzdooQ5oNGEfrCnpIe5pGoh-VVdieJWxzz0qcKKauXE7-CxYkwgGVUDFKIGYut64F5MPeb0eR8a_rp9Woq22OhyvOtjzr5ccQ5ULSuUCz5BR_BnZyx8aJ4mea91AMTvD3uiqPbQKFOxa4O95Uw8cuR-uLquaIZ3CRSMsMZvEiyQmaZKte6g49FiRn_doJ9gpGW3GUXVwUJLE-rfu8jDEVxZwKExVrTvxSp4W0KwLePVF5y7pKJdyd2-OeadShmZyK9glnXVyviBaygFX-EMzWWm-9mRg6OjOhmaTtVUVFWR9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=fhAgnM3y0M3hHLOb_Izy3lPVqpD2TzVHgwAZeStRWzCd_wF8ZzjOBWzQG8vGjK2LUq-JYLaWmj-gRKBYOGP_nAQbLbYCmgg3hhxboFNpzVyLf3GN9X6A8Z-RBGsAqFJaksEQGaGE02dNIjsXeO-_1ch1tUBsXiuz7J4j6Sy0XUp4tgBZoBhGitavpBDfqMoEunbT6XGjtw4nqoWyjdrFi6B1foSEVRCMhkVehYu4O7GTXXHFok0CU3I9Shlu7tVkwWKlUIY_YBz6mnIGAYNDZDR23u2R-71LVjLQBZA51tFyA1Vg8EPkPSBXaKR5QDZAE9XtQJj4FIz6L_c2Wr15OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=fhAgnM3y0M3hHLOb_Izy3lPVqpD2TzVHgwAZeStRWzCd_wF8ZzjOBWzQG8vGjK2LUq-JYLaWmj-gRKBYOGP_nAQbLbYCmgg3hhxboFNpzVyLf3GN9X6A8Z-RBGsAqFJaksEQGaGE02dNIjsXeO-_1ch1tUBsXiuz7J4j6Sy0XUp4tgBZoBhGitavpBDfqMoEunbT6XGjtw4nqoWyjdrFi6B1foSEVRCMhkVehYu4O7GTXXHFok0CU3I9Shlu7tVkwWKlUIY_YBz6mnIGAYNDZDR23u2R-71LVjLQBZA51tFyA1Vg8EPkPSBXaKR5QDZAE9XtQJj4FIz6L_c2Wr15OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=n8sIbpUCn3jtLOt3OtBGhNlPHjG0NYn-KInqdzut6wEaEnHdYejTDflY6c4l0qPr9TyBfdYFs1myMgjM_GZKsbuCo9fcVGby3svLND-a-5QfblcPPp2SCc3kk2Uzw9SoQF0_SQCFx8noas_Nf5VjrY7LfBzy_8Nl_vVTSTztxwHgwVfsdpSaR9FIpE9NJmp4vRGCaXF0W-vUeYYtEMGPtJCSZjB9RVKlpClz3JPjnFCyPL-rkqtAw5IVJKBIOP-AL6g0XwT7VJBMcd2lNixK1i0eE_xPOwnCiP3JZsBMAKzwwzm1zdoXs5ldCgnoYLvab2OtAmla5Si0qC6Se7cWkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=n8sIbpUCn3jtLOt3OtBGhNlPHjG0NYn-KInqdzut6wEaEnHdYejTDflY6c4l0qPr9TyBfdYFs1myMgjM_GZKsbuCo9fcVGby3svLND-a-5QfblcPPp2SCc3kk2Uzw9SoQF0_SQCFx8noas_Nf5VjrY7LfBzy_8Nl_vVTSTztxwHgwVfsdpSaR9FIpE9NJmp4vRGCaXF0W-vUeYYtEMGPtJCSZjB9RVKlpClz3JPjnFCyPL-rkqtAw5IVJKBIOP-AL6g0XwT7VJBMcd2lNixK1i0eE_xPOwnCiP3JZsBMAKzwwzm1zdoXs5ldCgnoYLvab2OtAmla5Si0qC6Se7cWkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MY3_90FU9mOm9iDN0FIzcBoCTsrV1OfNlwrlEWURAh_lOR6Xk0Ls1ueIZJGIyukp9eoSL74wTqwEjh8sQvgMnaWFdiLE828c8TSEeMtbRVJGcoJyAcYE4mjmMkuxRW0cNLy6W9uZ0Ku1rnVz9hUQ71o8E-4popooYCtTNg8XsLNsZl5WW9wWS0x9If3Rz932Q7yb8TENCeqofGBstvrtqgvBABO7_uPhZDREIMou4wrBkhKD06UvbNistPRxgTV-1T8SWZBwKFb4Q3hSYV7JsKlLb1nDiN2q79GTtGDo-TZmfHiQcidBN6sip5IaHFi6Icp6xuWUWbdlKcUBawgrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHmDHsqxYYnQNoLxWBANDr9YRT5vFj4C2oODH8_dGHU_X-CUfsH27rQ-uGA0s4OW5chejiQCFMJUWVxFN1HeSks8osFfVd1Hoei5B-GTy61U3hxzA87ACCFHG8GYDOVyNB1WFIhP0Bc5k5ourU-Tkik7-Fjgt1duLoQkUu_C7vn0ZOApvt4vG3fdSPQS2lQ_U4u-PmVwGX1fcSmhVl3iROeYqsgMlGYSjfdqTAW7kAg2e5HHi7c4xorMVCpAfZyjFSfxnC7QTVnJmn_dVYNT2-QCz-9FRYeQBN3du_HHZDzE1rnOIEzGk9MHZriLGlNZAEuouAjDLyvehrAacn5FTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF35nb50tG694_iF6y8ilBW-6jHloKIi10fRnmnkAc2kGP4Oxgnsqh12QFZ-H7hSp4A6ZF_fMxCsJb9JJPTTOzPwttl1FaJaNRm0-O-uk34rBwVC9-9U8WLknVzd8xF0DLq6MIFlYSfhXDqV5tcY6keGU49RA7M5EfU2YJgBBwhDig_WmUnvo--dHk5JlbpBblhsLOI4um9RZn4pMldksvzTE1wehp6KFeeQbTcJ57T7wOWlKX0b1BKO2tcjyGaV4FvcxuUH2lzXVAyWU9g0c5LT8zgxSMcZG9GHklRCPWY0bbAfb3-4mYJz8gcZEw_HsFazGU5Jl5TvX_FO3OWo-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZh_nmN2laAnubj3bGK-O724ZbtgLw6MF-dnsshuFT_ijSZrpBMoUhT-snBAUcTDVqZU7pv5ZDijE7ZTd8ukIHB-KUQzegE6xKQ7pVZjJSUhqxw7hXZFbV6eX_wVF7YutTDpJZONTAsNfVlh9LXQdPhNEJsNgJCO7SJPe5w-MJ_vgJYyLp7g-T2V6ipCedbuxhoEEZwEqbbfImNvS750OVzHMyMztbXmefdPAsJ0pWLIldSZdyxRAx0fIF8U4pII0A0EMdqSd-a5nG0xuDVuwl1tpzETRY1u_o80-r2KWoqkNoxozlBVh3s3DvZIK7s-7NMVIIlJBNprM-7rLryB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkwTWeQmTbs2lmv6P-P9qTrUaMDNQW9A4aFlT1lYrHkCYudj13LIoApo1cJUqZtszClQCxeIGy85i5Nn-qeQOCSzNYdhjXJGIBaiSoUf27g5APiIt2myjS-c1Bn-3wTYW8nVH1pjul1gT9t_jVg650Q5gralNG3GnBJwbDs1lIsYn89IzD8rdkkEsjfmpkEEjZyubvNBeRb3JWHJAOBz2ag9U4te9x-e1Hdm4fuAZNufNfpqpX3DOudhyR6Xlvuuzj9_8vrgQc4Tv0q4OeqLUYFjo6ylBjEa8-2iRxM1hl-DMN0u_7lkrrdt9PCTVr9McnUC1vSSNt0b7ZzijQlfPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEZlKhFvzflT7rmdN4IJDXAxmcbiAAeM-C6cUOUbfajBlq_-SV2FtdN7LPrZRI9Ypb2W3dQc9sPA_ehK_2PrBrfR7OXaaGaMeJEtFtAJnJ-2tQlTlOYV52WOxPmXMQOKXzEJda2B9ZvQMAyljYfGroCoqUioCHbgevGOAz1Y-nOkkwUMaroYAkA5LSyPji5dw4-t9B_REqqQbZKKIhWS8n33jhNpHtWZ3R2Sn_lD-VlJhvNKvxSA3TwgZGJja3kJ7gwk975Cc5r_ENnpthb0pROwHE5YPGlSFfQT9RanCt8rvWzjFe3G-HqHFAYFQmVkAoA8PiIzXy4fYN5a9koEEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPKmGi1lhdr_5SMvk7u7WmkX1sfXBynsRBfabppX5epiSb9qmQWkXKoAVvj9OtyJ8wG70QRyCDNkYLjJoOK7SzFkS1soLSXKsDM-dobuqhHeakuoiP3KBfse1SXFYp8vxGfYDRojW3iy0bvI8P58xYo-N-zOUXh1VouEQi70GvnIn-nWTBdN_ZXKRVuz5J3KRKJHiph5J3VpbjA62G-Pbw-ZaYboG_ZBhhlYw94m-gHjIpayDIzyh2Wjng06_9qrqRy6m-DLAO1LjhD6C0cahjIvh1nJdBgn6RtHBlhpWK3DEKAMm8BXWVPg5AEtS-hendGOXSiq7gopkNn-x4fzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRworAe-hg-0pneauFazu9vp1fKdR5VvwuMN-jenKf9sKvn93047KjitoPZed87AWQQkcfcCJ9qOZEtivxgojUp0BoohmRDhKPETtu3wUFDBucZgnMt1R9QYUCXW4nVT6-IQb2uU6Gkcob_S6ot-NCG_Pu-9E2NHsbribhueXhyQDnDuPTDmX5pBILyEUBV9csNKSz2Kfl93cQXTSAelBOWOrhQQyYCFiuc2PqA7KsQbCL32qTzefbzwhjn_7gNotktMJ0j_cznzkIpkXUkaOIyJ2wQrlu1OLl19yCDDDpqlwtTYhsCb9F0unQsbcRXcIEU_GddFNnEgnpm_EATT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALF0pO4SYCvsj0v87NLjyZt6UcTwrFkMkqWdrrFgWA37Qn_MKCR9i9u0mHiSR4DM-vgdam4_Qdjx9rb1B1nvVVFm_KPtPVs27ddExeJ8AKc1xZDO_NY2gdUPVofFRcEFOE8r-rwdyTU-L8vTF8bHM321Ijxkq0OabaClvwyir6qN7F7TcMUqcRjKTh6Dft47lIXIYQ5jvI6EDPF3ONzPIe3db_E99XUJSd4O6FY5iWaXrWs-QhbSJq1_xehxB6UzKE7fj4EM856UjRt8BtWhQ1qUMn7hEWWexJ7eLAqh4-k_XIgsg4DbeS5Aibb0Zq1dv4_jixChXct4vXQxxxLbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBVUGFvZF3sdwgKU7Jaurt9a6xMtxhzryVUpXncXO_O5VKg6kzS3EcVVWVZoiVAr_ifK433020FnVKfQ2DTbcASMpLoG1VdIVisNbk6eRhyv2lhED1CrKGMGMsTMNn4p4nZsVHuN4pYxmQbfoL7uvoQ2etEQxln5c5MvuKNGISR49EuYZHRcJIamciTUiLOKAdjiPzZPhhIGYADKXGXrdqgMStAJ1cgB0vI8JrZ5KlXLU9DmmnFE-kRsIXiAg3JZi3ugKORdbBA21o4tvhHg8kEQrDDLbnbmgXlpDkuHxiZ_f91yymvV_okPyFZE5sZ3b8WsZgQHy_YCHaq2uVAKGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhTj32iDDhfjlR9gJ0F1WChKyRgMclMDfeunJZREkl7QcikoDfBuNyOGw-EVtV5NID53ClohWDygfnOTAURUYDAXRDAfr94O2Y8YLmRUNIDTA6q4K2sKOTrar8Lnmlg0QL4S2Hk5x6NnRMyec7kSgiKiGs1DQvX1IpNDMyV7yRn4lSEYMShic1Gk7_J62qGIGZBx_X5BPM-nzHA784-jn1coOo9ToW6638CQ5mgj4n5VuJxMgb0DEeTFwbFLArEIfREyEkZo_M8ANMZE2lmfBsrjIP4kzi1YfxcqVv39m-0Q7xClkM5lDz6d0U2cou72H0Jt3-kx6YwZtJBkUQJfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY144qEmrl30xTJq5XrM_RYM3jqGEZAdElfVIyv0GXMA82qZ1zqjrFwoT99-a8u2Y_BqIlC0nlVnEZF_bWYmn57P4vfSF9ogb0b_P3pzzhZUMbzmLXQWZRyyxgbx9EfFOQKKAnPeHuDQw29Jcw9irGknLMVVJptMYAJxM1FxjXM1O59RyD7E4RwMJFN8EHqP1YoSIiCmLqGxZ6MIIEcb9A0v-DJzWUj_0J2We4oM1X6tw4_1wVCdcxahWa12kQIk0WsAJ77MMfuhXbPqKpdaHsdPHW_R_gu3jqXMMeaDD4Pb2-nRB46D_CaLqnVlQK4VGD3cLrqzjo8W06tNsob3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZF5Xt-RFWlzZ3gTxpM7ylIE3eoXYew9fUbTlIGdvScMspjQz94V1c2CMkwjsvajvtbc4YwbjYzN-rXKHd3b9AtK2II70IFVjLvM3guUcO3IQLH_VKWzUfV1H16y1Blp9CqCrxyFb-pUDtWZyyGLlhtfuCyDlgY9yjJYObkNmn3sidCOlm8rSqMI-gTyCB6gefWhqoZpvHoOmciN7m9pCfHVUrWdr_x-J4__XzUPOUR2MO1XP-zutIa8gLjj5JBGKYotn6HZBa6iZYIxHV-XRBvoHjwUjR-_eo_lm-B3BQrlUJytDoGlND6nFn_6c6IZya7KbYtrHjVSgM7Fz8ryUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaX2cRGE7lFSTwGkyn9aq96XQH6uxWWq-BP0snZjIAg9MT6cTyUSQN5R_kYCPh3VOxyon8Xp5Ve3CXRlDIg6Eum0V8zBGQQ7DCdrFkkFXB0O9NoelToX_vzJTz8Z974fGOlRXe1T1cuLR2_fFzFk_4Oe24jXVTIOMbA4SoqeQtENRL3W-NIn1A9TVpN4tbh4M3YzhE78PIQ7TwToXHI_yJ4G2vXebVnffY6EHuiiEZn-AWQYwYIntCs8NXOqOkjF586TbCuQjVkVth6ii82NigXKeql9G2ZwHlGJropJZgA74gdyDil8frQEvBk0LYy-oF92innMtrm2aSzAS4BBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cImh8t_lHvrLUM9eZ6ofg9jbKCacP1-wsx60u9T2mOXh5GZvi7FR_omKAtQhz_ahuWPhyk6F7-AOfWGR6Z6AEdVOfgFB0rlubzMN6IZl0_WtrutyDwTfnvaHKZyZebV2Ep9RWIwvLAL0d2dxv7Qpk2U4iHyTeX75WXKtuDI4hctlPXm0GDQ5O8AOo4T2uuImCHy8zebKkpOUN35ChjyOKTcpUOmxCv5BYGMIxjOKkz7PB1ZCVeTf73UzEg8MpdCv6dglgBcKwSo7TguNAcYySdt0u_P2yF-IA_IxoWlNtuUHwbwAsFO3R5sVEnUEXR_2UeF0_XPWBxYQ0Jmbh-hmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOgZX5pAfyjn9QreTWGQCptXAvUjfWvVG7op_4XHjb7zLsl4Sn8LLSJjSrnIxzOkHhjIsbVv6gOlpPQzOuISa9UalOPaMnMRwkSnWxaUlm1RInhWsXVebDwOqtGnW3RQUGpdHF6KFydOZEuf99B2UNJ7wK_IlzXmKfRAvhVAljgLDhJgPzU-vmAt9Jr6ZHsF2RiIDkfJs9ZfNZHck5E0pZnkBqq3zb_XBmOJ3uIRKdiTfr97uThzaw2kEoY2faQAb19p_Ri8t77B6-DFFfM-42vGNPEZ6zfJqwVNwO9RZwmdMsbflseqTAv24r9LjAtH-hvLeQFpPworkF3VY9FjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C94LTbCevpz-posREnUKWYVec0v6XAFOwlV8VcM9hF2VdCi8EvKxpt3RSPsX2sdqPHeNi8SnVN1QWJ31_V_ZTZ7EP_yTt4RJfyEwrdHvmH45_2AVrvjEyXQqxyh-DHZT1AOMi-jrw7YAxi3WxcuACL-VhuWDyjknjDFeXE3FWL8LughbanP1ZdsQypS20wyOHuGGh3ftNVKs6ZY2qPy4eadwxLUIjFfZRtjtnFzHsoCo6GdFM0hVdoAUz2-K81vh1ptJIY0KuZYUlI7qfqR1baz9Ph_1oCT_pTPMVXqpXStuSbe95QlPIlP4o1kEGX9J4Qso0Sn2rlMg7DlXgfFYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/poVkH9zrFrYhzqDWQeJMymMhlrMz4NaTHOC9JhvLULvcS0DYifNVTgrn0QwwxOvSsuPdeNmQ9NoGsJK5eix0wKG_mbQsx5rOnh-w8IM3RuB0mqApNdIZLnhU2c0B1ts1zR8lwNaw7xT8hner5Xk5Q43vyjG_pYK_kJmV2tjtvKOlhNx2EuIRDh27toL51HIz2fmYxlHReQM3hRCq225hcoxIaWUnPhezROmhc8A81LYGQJ2__flp4wurbt9oGIfz-EorNOh4WP0EIQQBI1zkKaziNoGxSiSnWfl0h_hWhn0UtFkBo9L1E7zd7iznrj0qrXa7LdsQdYUZOc33rmBLzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbsXaHKcOrTEdBF_DLjXtNW0JywEtCOYj93xdnXKKsBwflljEDpepeVrzC_oUWo4rTP_vBYAULi7QtLW8XaJFXzp4wSsdsHrFEv43-Rf9bG50O61czyJpVoUL49wS8HfRmHOZRkZhNIypZog9z6mdTfSAALEfP2prSZoZw2AmnkNH4KVDlsAp60bpR5JTh5LFJtThtUBQTryXx5RJVHUxLNkhTLcRuMByhPHvlBomQT38n-SN6iaYg2u56RC8WgGE9IO9aviai1OajsLOKdgIOS6Yxs_BELlW865iT71V0BWXuGMQJzNNuvf8rmtC_zAQZyYZPBURRvTbSsWJ0u9XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBMy4rEZdJBJVFYrNgTi1B5pfNP8ht1lkikezadQ6OtQClnFdQAKWVJHF3F8G-HOyFwlS2sNIMczRHnGQ0nV-nqDl1p-wyygMxUdPxOA3Wtd8rmSGRJQN8ZhVDtut2ByFb5D6DAidPo5jeoefPhpKOV_w9fHhFoTcDCK2cpo8Bb6uqqs_TQcsh6I05HhwxjDjX4QE2E3OhPYWZqGzqysrWZzj1sK8GZq6xW9ZwRqOUMLyOrdgSJD-Ks3VWXFORG4V6aw3TRHfIaugmh2NsERRHunNJhSI8xpFhLHHojt8Kiz9hIqiZlboIrJtD2rHujG_zidNWTA1CegjAtMzRBTBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bx_0uJCCNKgqysNKsxLpfCH0ltxtXZmTtJT-hpscDiM7nOg8C431vi23BzV9LWGLNGEoEgwbZ5dsPZpHk9-aGIsrZ44vzPmV1P_QkBP7qqD00a6fy4HqVse3hggbXp5MayW9kf-RQezNAIEJSZsNpdfQcsrOkeUmui_n3MEJCLXA31z_OdYFKJcyODjI3AXS24huBHf8TW09_wZgHJM5nVkf9Xg6Wyonm42dyZzAs4JOTOM6bFyagU4tl371RkVcEXrkc-JWLgVWxQPUVi_3r1-X8FcubQy7mMapmAUs5sYY0o7h0a4asXfBRiurUPo-8SUPB2NhVN7sCf4QHkgllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=pgLL5UDpbfX27tpq-ddFtceMOWofuY1ticgMwTvgFhr7GegCQBQl68pXJaaupKKoAwdKR5oBG-8gy9fyJX2DEoGdhO_mmDaRB0UC0HZbFdQu0bEIUuoDz-ex_4d6Ys1e9Gy846my1FLsBUpxCmM6AldbVYwUlK7DBPejeGvaHRfZQ6ONcn_eby17kpjb5O85l0Fl_1HFr6isuGg8u-DJtJuLbjyUwLtwl1VGW1sd4vsQMWNB3p3gk_MTL64ulTv_XNRUNXdrnNaSYfjwZ7gcEKR9t895_g0FlPid94QaIF1vOT1lV8qyONf49YSmcl3bnrwDstxX81QkbA53CXmK0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=pgLL5UDpbfX27tpq-ddFtceMOWofuY1ticgMwTvgFhr7GegCQBQl68pXJaaupKKoAwdKR5oBG-8gy9fyJX2DEoGdhO_mmDaRB0UC0HZbFdQu0bEIUuoDz-ex_4d6Ys1e9Gy846my1FLsBUpxCmM6AldbVYwUlK7DBPejeGvaHRfZQ6ONcn_eby17kpjb5O85l0Fl_1HFr6isuGg8u-DJtJuLbjyUwLtwl1VGW1sd4vsQMWNB3p3gk_MTL64ulTv_XNRUNXdrnNaSYfjwZ7gcEKR9t895_g0FlPid94QaIF1vOT1lV8qyONf49YSmcl3bnrwDstxX81QkbA53CXmK0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuaacXXTl3AqKaIJYEWBihQJ-glLEbkDTDqO9B5XaHrzf7Abyell-n46xUK92pzTjxxtRqfR-n5pstw1-KTZvDHwYZVDgLtGH86XpLkxxoYoV6TAZpBRGAh87tYK2b1NRBDENAH_lz65ZWhPIy1OJUcF8t6HDCzLSbb2jVoXKdcYgtUn_LDAW4BXMdK6c1JcswaFHUcuoKdcuG8qfB96pb47teS4K1qunlFt9kZaojZA5kmkCW9WFCbhGUy10fn_r3FED2Sn63zouRseDX1-5p2ojF33fhd00zlWLjfZhUMH3W-CFT5OBoyyDI1vI66P-GpMy8PfeAiK3H2Pmuca4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA-0go3yHpovpAU9JPKhwV2HdOmAij6pQZV2MHHEX7MNPnzM5R8FEUXENi2Xcv0fj34R4-s3Tzkotd3eQjoSqDW2p20EGk0x3qovQGmbvceo1mSP5YepBS-yFU1jW26b_TY5un7AS20cRb-PAgjLdo2l3voumM-XmcDZVTdYymaarDc57LAbYqST1omBu82TbvKW7HJ53rJ7WQVF4w_FVUhLfEfxBxeAAoMwTV8odjEllodnUJvbgiPFA9HmQCn5iogJ3AFIBsDx8RzkF6-CkeFry3O89FNAIsIuByJ4Q93zBIbJapPz0LH2MGZCpvjiOONlVED2HkAKzZXUWLUpsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJMCvkzt-bsP_cypJV-xOJ2x3To1gGoj9CikoO_cZw8ioFVONsSYCemKIVLNGiCtvxb6xVm6KyA1HmX-0Uf8A0gk1O7DurDN62GTNzhaF57uF7lXv4jwdofrFLbEMkl6pHlg471t4mNZas1mLfS9rhJ57Sen3YlOhHdAeFjAGjtKGrBF-DHy4iSFSO9YMXKmDiR55eBHHa9Esgqy2SR5T9JNE9LLjparDpoISuLIN9EF54i6_2ifUFTQCMyuMRG21EIo-Ge1JLL6hOCHLq0jiXMuX_IYqWOHUh6wf_7fMZfJ25HJgVYKki3MM3psYHTaiJISbp59eqCs_0Evw0Kr0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9FQ2NFbcTk0-qOa8tjbGSrFzEoypEZX2VuXAe16R-D7JDbuLRL-M2nxJ2EtC6BMt9yka8d7LECvjfavZCbdqO0e1BOoZ-iLgAT7O4-SxW3NuY_rXv9QRF6CkLIYJF27w7-04eyYbHqtByXNOOmBY3GwDYCKSxKxSLQp4zMoHu4fO9bTTCG1BWuQcjxmC_Bi_v7mGw4ANFZSPL-sCeY8Fh1mctJSgxBo3_xv4R5xnFpQUSaSYrs2laJfACW9y-05f-2tEkL_v2yTCynEvkVl-bbggzwJn7D2DNlw41LYA8ooVw3nNJDI7_ACn3S3ajnGhgXk0AhNM5BmCBBaLPsRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZjP4smg0KHIIgIA5JuZ86Sm5ZOY6PnrersxqctG_N6_claCIVTOWrk3G_z1XojEJSUGjUz8sXtbmkKasW6Kb0JarcZjpVgBaueeIIe_FAPOr4aaMO6N7bC7G-TcWPzF3l2_6-KYPSiWCiEgFJzYvW0k8nlnaT0YMOXsGJQ_WmvD0j0mtIR785N7upQKeynRhuK4gac8FIJRuT5KKolz3v_0QdZFTH19kCP0XJ5iHcK6l8pZO3IzxrPPcrqYUkCih_MAZ6mQVARqRiyFImSbEFGzhHoPn8oC7lZOcI-a-ubyR737ecu-pawnc8kF6IRlbcMIhSJBOgVbpsMf7qJShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twWXdya3YrQuW87K4SP4rH17gNrpBSeG6g4O99gG8foe6KhG3tL20zZoafeFcjhfV26016fdnBCi5JMtMrV_-ARpdXUZkVJ_jwPCMKVNT42RTjqfMWw5oNTJScrvx3OchUOGN-gT_iVDuallxuxuN5XMcAqiivy4K8a7AE2irAffKO9o2GyVOWUge0qXrIzR-SWPljPHs1v3VMqd187FeEtMsfujgsBY81LMqTJdarcOmraED5B5dHuIDDbnAPfa-JdPQwtmes4eLzp4JXf4xdy-uMOjFfBOdoWMY0zdQaFPYC2_fkvslCQhy-C7AisO8fnUFEEKquzxXqh8n6mquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njttqlTppyaGkIwZ5CFS3j4TvBxrBwgCDyKTT51jVmSQLa2fNAItnbJApBnwdFVeXyFs2dDEpD4Ep9cWERasyUW-SAU53YN2TEjzDBq6SvdKXY1YM9yOjcKiXnfYSuAU3d2a4XB5S6K5APen1k-xh036hVZF8hynRhqW3aiqtjLL3VokVL_VYMRr1wuve04rtwEhZ708ReKknVbXbNYaqXc8-HAI6CKYRZXD2ES-kiaavODR9ubwjmEhJI0FFgm-KgILxGVrCFzjyaPKJ2L2qcPus-PC-YD7Mx8mgFQBrcNwAtf-kSw97Fxls52_eyanRoWTTbESk4pNWlbRUO6MXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUwuoGL0Es7dBWU5jN0q2P5h3wkaI9FPDbNWWgV2h9dzpYZlJAbrqNqVP3BKAN76GeH8ueAfA8pE2vrPMWV9I02IIfDN353jSzvxtHZh_h9tE9Uto2C_IQlxwr4fRiY7yX2Fy7uARL_GkL63VZCG4AUuze2TFMm18D0DHgJ77j1-G-LDJUL5o9FKBHE3AmE0RVtR6y8vu1QxOtHg896XpAYk9ApUarPVZXCT-YkYlev18HabmA0fBqMuySsvkqCvyRidoe-iwkbcTzOofKxzXBt3ZluckRMXnQxWddUB_egs0y6WIC-_Dz7nC14cytsCWB0MSquyNQpWCopZd3nELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=gnRlNXLMgve8Rg_f1QOg1uYMZWN28tLLnAH9e6sQurG9R4EQ7Ul41-CTq3HDrahO0puSkUXRyYKuD-qEu13v5j5Nq5J_HA8feJSM1sqW1qBhmagJSkz2tC2hI8beuEJxc_bNdDGu6GKrNKfrlMNPabeEF3QEj0ArCML4cdphVwgowSpI5iSGJwvtg5InT86rhVUNvO1RuRK2IF05zxdIaGkS0tBI5Dkd8LDBNN__uBGEcBJAy0yOrPKKOo0dw3F2tM6MDhSvj31c0naRZwBbtwrazYJVeHM_x0ygU9zuHgKsVAPNvedaPTtIafsgS4TpjrPklcfhtHhxTo9N_S1reQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=gnRlNXLMgve8Rg_f1QOg1uYMZWN28tLLnAH9e6sQurG9R4EQ7Ul41-CTq3HDrahO0puSkUXRyYKuD-qEu13v5j5Nq5J_HA8feJSM1sqW1qBhmagJSkz2tC2hI8beuEJxc_bNdDGu6GKrNKfrlMNPabeEF3QEj0ArCML4cdphVwgowSpI5iSGJwvtg5InT86rhVUNvO1RuRK2IF05zxdIaGkS0tBI5Dkd8LDBNN__uBGEcBJAy0yOrPKKOo0dw3F2tM6MDhSvj31c0naRZwBbtwrazYJVeHM_x0ygU9zuHgKsVAPNvedaPTtIafsgS4TpjrPklcfhtHhxTo9N_S1reQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3Qyw7bazIRGUWm88NOuODX6vFYbqq_OuPhLpc9Ve-d3HGtT5qK5QTYUgbwa3uob2CkJ0Xhjmkm-QBQQY4WAY2ROVH_6tqdWWux9Zjis3-b2eXO926y4cqPQScGbwe0x4UX9jAtyMvVEhQ8MwtvGwUi9ZhqQZqG2bOEQYsBWDhU5xVNafQQ9MlRHM9fUX9cW4fUMCNXFSpBNRoW_h6bxSUKLEto3LAzQixqRdd8ZnhIs3ru686UJwK8oV3OGmmxJdueLL16ZkZSIOVD6D3uaDvpTNr0-On-1hRxFYVE73bZYv2cj54iFbC_UxpH66qNL_J1NW7DBSOUDkWQzCgA6bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=E7p2KuG2t0odniVvaVM0T03JotINLWXfSxHdITej73tGGBsQA1GHTj_pcSpfHoH5_3Yh0toDMGvC1QE14EIlK9h5w27NYP3iRBvFJPrBMZepshztGW4D9ISwqrnbjkNjyYcgOQ0Mll-0WAqMDg8WIfdkyxe4sTOHWhbIVHq6a0bubTXTNRRwq77Eq7lhvwbAIMwpMd41JQsZ7RnUSd-k6Mka20BUX807mtMrMrruoup6xB51PX2wzL-St88FxUK7ZcrEg3Zp7ZjXzji5uEtKMlVzCYoFXMpZvwsGHPTQ8rZw13iV6jJ9XL9QNvwArm4Vvv1fLMymjoXE24SKR5eY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=E7p2KuG2t0odniVvaVM0T03JotINLWXfSxHdITej73tGGBsQA1GHTj_pcSpfHoH5_3Yh0toDMGvC1QE14EIlK9h5w27NYP3iRBvFJPrBMZepshztGW4D9ISwqrnbjkNjyYcgOQ0Mll-0WAqMDg8WIfdkyxe4sTOHWhbIVHq6a0bubTXTNRRwq77Eq7lhvwbAIMwpMd41JQsZ7RnUSd-k6Mka20BUX807mtMrMrruoup6xB51PX2wzL-St88FxUK7ZcrEg3Zp7ZjXzji5uEtKMlVzCYoFXMpZvwsGHPTQ8rZw13iV6jJ9XL9QNvwArm4Vvv1fLMymjoXE24SKR5eY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=tXavkR98OD81QSKL2cwlp7Zgsi_O_kLaU6q0Nu7IdDTUu_lyG88mapIeaAYysLmcd4CLLTB4xmIFz5vlrSNT9VnFoerbfMdpjr4pzdhCkCZ480QKbEX7i56jr1047BPz-n8aONNkpFfquQlbV5LszwRygJ55MzXq_PFng_NQJTlQeKnxbNtycDYLNsq4RwfIX5-6fteBq6gp1iLXuoNgea2LoawYDTgbGdwufHLJpH23-iCau_X1fOAPiDw4lcRt-iNfjrQe-bj-gOCG42nXBo6NcXcOmHntZhEmCpFKmNZvnYmpMVT52Jfk-eyjkpiQeZqArSu0AYlcgQbRqS1w44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=tXavkR98OD81QSKL2cwlp7Zgsi_O_kLaU6q0Nu7IdDTUu_lyG88mapIeaAYysLmcd4CLLTB4xmIFz5vlrSNT9VnFoerbfMdpjr4pzdhCkCZ480QKbEX7i56jr1047BPz-n8aONNkpFfquQlbV5LszwRygJ55MzXq_PFng_NQJTlQeKnxbNtycDYLNsq4RwfIX5-6fteBq6gp1iLXuoNgea2LoawYDTgbGdwufHLJpH23-iCau_X1fOAPiDw4lcRt-iNfjrQe-bj-gOCG42nXBo6NcXcOmHntZhEmCpFKmNZvnYmpMVT52Jfk-eyjkpiQeZqArSu0AYlcgQbRqS1w44i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=tpMqyLQDpeS1uplliuH1DHIkGsqOIeJfwH3pTMEDn8iqmmBXqekFl7JeANj5lSxa81Mwzdjt6pdYFnJtbk9LxH-TcXHi6AQI1qL02vTLzVlxEqft14qtz393RBsJ7BWfTsN_ki3_iwZImR3DhDhKHQrACpgevyygNsbsfJJtWqSAWKd8ysgPCiygQyi9sR1FPbsdd8iN8Yr0GUGsq1OdO6ehKu_nV4SYhlUs7IfqIbxcgBc07VAJF77Q8-YdZ4h7NUm4OlkbMMoW34L0GJ26rp5NCIUCgOuvMP-jupDhN5xdNgx1V8I_iN447GLwWFez1ZbRsUG_YWKHHaSEJBX_Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=tpMqyLQDpeS1uplliuH1DHIkGsqOIeJfwH3pTMEDn8iqmmBXqekFl7JeANj5lSxa81Mwzdjt6pdYFnJtbk9LxH-TcXHi6AQI1qL02vTLzVlxEqft14qtz393RBsJ7BWfTsN_ki3_iwZImR3DhDhKHQrACpgevyygNsbsfJJtWqSAWKd8ysgPCiygQyi9sR1FPbsdd8iN8Yr0GUGsq1OdO6ehKu_nV4SYhlUs7IfqIbxcgBc07VAJF77Q8-YdZ4h7NUm4OlkbMMoW34L0GJ26rp5NCIUCgOuvMP-jupDhN5xdNgx1V8I_iN447GLwWFez1ZbRsUG_YWKHHaSEJBX_Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJVZ9kM5vKzQwoaChH3vBJetuWFT1p58h8orY3V9KDsmM-ixvkZqy87GFtAbRuBgc_XsTrIsfbHBq_CP53MTiug_UelaRDosUVZn83PwTNV2hD1jnAOYH7IFDh4W9tBahbY-rq415yjkRLi-MnHPEvRuiowEf3j9mOx5Gqa7uUYmFXPjlbOfopbpD1rwsG1MMInIPXktQxdzIHQvIE_6eEddkTIGJxi9dm7493HcI5m8QBjCIO49x3tWiB-_5ROdhzVv_TG5jt0L9nkwZeaz-nAgUwv1c3B2g3R2B0t5UqTDoiBoXw3yBheKdD68PbLbEjtkRNUYDIiSXW_OvuCFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXsFWNplA4on7U_w7d5RNQkIC72bmjv4YhEUhRZFatsmZSFe4o1Kt2eoRIXniA57Lhx-DiKDKXJWIokzxvNBEom_BVvkqCRMeHRMBOn8cTzM1Yx2lrmqRSn5eAIgJ9RyzpxkCxrhW5KiDdR745W2Ln2pR3h-KKxPaRX5Zjgyn7fsyBM_o32-IAxIiEAlao-lXUKVsBIN1MpAbPN7HxXGF_rN2mqvpKfYJPMv4t8_X00QEqp32jfLtwgcnn8b_4XS27aG-0mei5oC-uZkktFSWOvgBsT95BIeYlo9u8e4S0-CeO6GPEuvPLZM4MUY0Db3nDIgzq9-7KvzZ7kxO2pmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMrPC27nsQsHL2gMjKZGiFTRkxj3z7_9Ry7kuOCvyPm2fOLcRuoxWGmJA2l5MvIF_dRQPZ13nOzX4ae5O_m5sgf0hWBqRRRrqit_S9uSQMRBHgBy1A4MSd_D45K-s68fTO3hwfGXvYMOmk2W9RKSTIUcWq5uurphhpWMMTvPKWEYP5hwSrWshlf9W_WjioCxtO0m-Lt1g8h_YeCfIzFtaEV_y-KgjtJsuDOf1ljVJWr6fV8gyTOewcSYDf0SGEHX_xIht03a_eidBzw1SkuBpqcUjJ6AvuWJRKMaXebUahosKQK1zDzwarS7OKN0_nqNjt2VhcpVesXTFQkMDh6IMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHXfFTLVSQAxYRXWm_T_ihVM4BntIYfQ8afixlLcODpiMGDBs7hMxlkEEmUPrvBJAmhwsITNzLQumuUOTpHqv25gNXbbGXBzr0SHPeTInLpJp6BQp-vW61u8zmU-TIZ6WHGruZ1t_6N_xsM5ZkzzMoxjhjDomwPiF9z_aF2TPZSPLXHz0dO_PW2sKFF056HMVzXJi_bmVXawiKd3kueDIF4fdkrRDKoG1cvd0DZ1k2huIJDN8-IRRPWfE4Wh3N-vI1VGlBJsaidAIOKobNZMi_PL2_JKJDCeHeIcW1Tkl8oTEzpzPjQcu6TVrMoHlvOKlqe-G9LSVcaAhTeIUI3UkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=r_mtmhaGBd6rtot38tbB_xiz7VnX3iKBHrgmdToVchp8PeggR3VZzempP8_oIDaca0w6MdIu54wMPJPi4DJ17LvmfGhWK7HOA0vWDmN2LYJxj1M2nYaoHyEVOQN9vGFUz7axJNLb23UsTX6ppr5zEQyFHoKpArgzVXfNuSypaFL0NqS5TYjJcgAI37VWwACvjjWIZza0xU710vtRomae27tuOKl-5vTFa4XClB7RcG-qyE9viTr17wsiDloAoQRltvX3QIwFDZkR655CV1yrwHd9DEIvJjzLWQ2S8zb8R3C5ISePNZROdLvKyBrtbP1itOw2q1Fs3Ncs4MdK2APIqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=r_mtmhaGBd6rtot38tbB_xiz7VnX3iKBHrgmdToVchp8PeggR3VZzempP8_oIDaca0w6MdIu54wMPJPi4DJ17LvmfGhWK7HOA0vWDmN2LYJxj1M2nYaoHyEVOQN9vGFUz7axJNLb23UsTX6ppr5zEQyFHoKpArgzVXfNuSypaFL0NqS5TYjJcgAI37VWwACvjjWIZza0xU710vtRomae27tuOKl-5vTFa4XClB7RcG-qyE9viTr17wsiDloAoQRltvX3QIwFDZkR655CV1yrwHd9DEIvJjzLWQ2S8zb8R3C5ISePNZROdLvKyBrtbP1itOw2q1Fs3Ncs4MdK2APIqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4y_Bwo4pIPEj1W6LnrTvVpHIGEXs8Y5Gt8faaQrgTSMkFPtjzTBsGQe8pvT1WN4zL0Uqw1OJZn92NwN-j73epl1Jqb4JFTVOA8m_Wuj_JJ5Q3bgCv7OKrBkugd5Z2mfKdEI0mHXZElfvYk4kPdFIYy1R05K5D40xt1IJp_NCEyr07G_HvvxEns73CyZVETnvoZJbjcYKfCUwPle5wp2AAjbbyNKz_4umYXwSwKuzR8LZti4jTsJqUpP-QqiQmbV8qxrD7E_Ty_BXi0kOFJMtjOp00qF9VJi32EGwpmUg8ZD6wk6NqqiGzs-P4E9Ve4YwiwbXl5GI5qjUtds4BaJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzJH9iQ9vA8a0HeNma8ElMnYq7XNkxakuYrN038OcsS97SfhsC6wPlLptTnNF5iy96ufa9B6N3lImorn5Vah-x2cCGFZh7CTHvPGjowi2NtL8L1Tpfa5N1XYCB8Py_m5oOulhou_iqQygvxd-uNg7gX5wJ_zAB6Ywa8qn1Am0Fb52va4cJBTtOKPd7_EDDtu_LXmuds42L9F1LAEt5g6pEd6-4xxZpKShWRuVyQaAKyI2Uur9QKuflvWAp8OIo8zXz6iJSJer6sL8e2fxF7gca35zHj9czHetDUBtUuWbtjlBkOxkByhGgZNZlpwpvsRfpIUCGgzMCZm7HRQ2fqwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQrQYhvd0Cl4qCw-sf5nCKl3c4W9q0YLN0JupXFggI6U0CWHOUSTl5A-OfKKwcTDsLn0d9q7jtvfUYSdVebrXaxIKF9jX9bfAorhbnWpFky83iJ5CGrx6oGvwlAY4j_1N1VVto4QcOvEq7BPWNzOEitlfQ1cLALOcsyba2aw5Rghmtiq5nwzONYfITKTvq8vEjG7CscrwVS2EZlEDwFOw0Y7o_otu5zFTwc1P1IbqF40ZdjY78XexMISQiQHpp5UnHIcI1-GkZ4f7h8nDZw0PEyi3AmiGir373vsurR8Hj9Me_V8kdQjNvV8IKhwvxau6d40NVQaChzXLe_Wj7k7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw4XfxTjW9ocGvWZgHD-KJZEGoz8KUCS2XtXBs59Hdntuhg0WpfDs3Iu8fVaIaNnudCR_wjvjC9WRHxdWQCXbshdjLQa9gLoI_Vh1dw1a_fk382wfmUU6IHDE-rR9ZruoaEXSur2yIdgMmKQeTU-QqB3zD41wzaxF_tViCBxXd-WddKjyNRpeRtHfXXUJ-3r4Kl5KN3Y3enQc28BGtGbiY4a1yZ7A4xU99nQgR8WkAXfmdAr7tNzJvbF7s8YUj7-AhYLxFSLltvq0t8BkuuxT5t1KkHqzstdsbE5ifInKLuv2owvFEJCsEsjKs-t8DGrAK2aCWtU_BavgsV14-0JTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxLGbgQWrSxJ_rYeIpXiKzz7kKDKnOIMGrl_g-YzbcLNaodjS1EYr45KenQiOY-lgaJui2cf1Liw4bnxyP3SiU_5D0lVcWmw5NkLR_ecinXn0Uq7f6xlRdV1uEImFLUW2QyVsBNWnGUdmXzg1tISF36z8psVy4eTXgc-0JJ5UZzshnY4BrUyJGXFp7u_GbB2Zb0dHS2n8CNpNkMRDaQej4Wv5p5aU7UbGkU5FLt7rwaxRGM3t-wxeWqIs0sVpOiDiiJ_41plhxfMIPVqR4b5PdD8aeSgSd0AoFkF9qWVSopxmAGuRWMbNtTR0uGIr9FDjqMjx6pWHlN5HOFmsZ5ofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLF07va0Q4XoUOZ51puXZHduMM5y51bro36p_jVhZL3WA4-hdcS-rcdD8B8cMsbytjoJiiHguR6JtM87rADNnzHhdxDQmcGZJbm0PgID9rUGMcP3GdwN0-2ho-qgnuMzYKE3Cwtz_ZrjWgUk7NsxLVRJX4IQ6FmPHN0IYbNHdjjvxS4wVVAtI3SN4yuzyRo7Mm7xYtV8H_mrUmawDYcN4IlNi5ExszpyvL5DI4nWr9sSrYVnriCzJYXcUCzS0edcWxdGVjNELhO4e7VZWkGpN6WtKoo2BFo9xl2IdioiC6lU-nDsQubsuc77yaYPZCLQVY4jO72O5FlGZa4XhQhGog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=ib3pWEuVKDMtEoA_sSN0VRogsSzDM_8p9tCHkCDNxbcXFfhbY2JZLvz8pCLLlaZPm5l2GvTNWi2gYEF0moWS_qkZAo0DvYMnYqkZ-1k2lO12YgAagTPAOl1SIuofu13kXQWRHtjB7okAPXUOlad6aeco213m5DgaF0AUwfhlhknp4dCHlLgfR3Ww6UQpA-pnGGmK3Ia9e6jwNe6zwz584ogZlkONC2LzDQW7uuEZw8anS3cfE23mGM73bkOafHZmqTENX_xuiiwVp_xrZ0mmTjvYwniukduWmhHesgfd1wWPEXqGi6cc7nm3Yst71bCr6TacVIHWtoay9Jmji8FwlJCH604IvfBaWvjxg5PmE6mUzxFQO3kz22H1GNmlN7IYuhl5f9lOErxYeUYth3LRPQXWN7u11Eaxw-ev7bVMEhCxJKhPG1_aNGuUxzLLxa2gaK3TIksp5gLd8Ebboyi2acQbslehG2jt1ShAPlfBEQS-bShYB1IxyN2j2NW0X9_Y-JtUc8Zf_-Xnog-GC1AML6kpGnLQ5bFGJSrKKN37S9FpP39cW--WWZjg56Lql3kBYIp41_2W2qyG7bQPeiOgWfn6_FiyWc8ldrmhQdyq_DBspbEh5Ms9Wr6PtStX5HchczbFJXWPRaFG_NPgBjdRpCXmk8MacKIIaeIsNmi6PXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=ib3pWEuVKDMtEoA_sSN0VRogsSzDM_8p9tCHkCDNxbcXFfhbY2JZLvz8pCLLlaZPm5l2GvTNWi2gYEF0moWS_qkZAo0DvYMnYqkZ-1k2lO12YgAagTPAOl1SIuofu13kXQWRHtjB7okAPXUOlad6aeco213m5DgaF0AUwfhlhknp4dCHlLgfR3Ww6UQpA-pnGGmK3Ia9e6jwNe6zwz584ogZlkONC2LzDQW7uuEZw8anS3cfE23mGM73bkOafHZmqTENX_xuiiwVp_xrZ0mmTjvYwniukduWmhHesgfd1wWPEXqGi6cc7nm3Yst71bCr6TacVIHWtoay9Jmji8FwlJCH604IvfBaWvjxg5PmE6mUzxFQO3kz22H1GNmlN7IYuhl5f9lOErxYeUYth3LRPQXWN7u11Eaxw-ev7bVMEhCxJKhPG1_aNGuUxzLLxa2gaK3TIksp5gLd8Ebboyi2acQbslehG2jt1ShAPlfBEQS-bShYB1IxyN2j2NW0X9_Y-JtUc8Zf_-Xnog-GC1AML6kpGnLQ5bFGJSrKKN37S9FpP39cW--WWZjg56Lql3kBYIp41_2W2qyG7bQPeiOgWfn6_FiyWc8ldrmhQdyq_DBspbEh5Ms9Wr6PtStX5HchczbFJXWPRaFG_NPgBjdRpCXmk8MacKIIaeIsNmi6PXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=Op1oppRDzIhC3JGrQIVuM14247a8h1-RPAzioRlxr1D8ypOKDY5AO14EN9ljFpHLwc6nQI2eS_djRfLOM9QtnRVdgD6fnFbx6Kx_tsPEzEWfEvxcYcV1HDo02P0MbkRCm9TQrtcMhaOCtUIyHgkaRxMf4yIzYGwHRxXx20y3DJJzquC9zCCiEj_SUtroftW22h9e4Q4hefNW4cHPt-iNuVqZCCQvrPFwiClSWzTFEUUfiAljJCZyN6K7hYv8BgIGa-59hz_MgcwZcl2P2u54gGLHEXTRJWbdk3bllmSQNHQMGTN1tfRD4nvWpJJaLNKoBy46-VgpKHama3L7slCX2TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=Op1oppRDzIhC3JGrQIVuM14247a8h1-RPAzioRlxr1D8ypOKDY5AO14EN9ljFpHLwc6nQI2eS_djRfLOM9QtnRVdgD6fnFbx6Kx_tsPEzEWfEvxcYcV1HDo02P0MbkRCm9TQrtcMhaOCtUIyHgkaRxMf4yIzYGwHRxXx20y3DJJzquC9zCCiEj_SUtroftW22h9e4Q4hefNW4cHPt-iNuVqZCCQvrPFwiClSWzTFEUUfiAljJCZyN6K7hYv8BgIGa-59hz_MgcwZcl2P2u54gGLHEXTRJWbdk3bllmSQNHQMGTN1tfRD4nvWpJJaLNKoBy46-VgpKHama3L7slCX2TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxU38oZzLs9bTcnlw9ps66K_YQDBPsg3Xc7qtxt3w9QJawTbxjiFFH1NTrQZgtd02AqikKUTBQmslVAKDzknZI1u__CDnrRjUVQhTpqY4miMpJlrLJw5xbhlfKooSRqs3RLKmOFRoAe9uM_tsrgY424rbJm4VznzV-Ka-6jhO3Qxtng_JeCebO45v-Nv7xL4momi0RkaOQ5Qx3ne0KT7HQtih-bVeVzxbBC4cpj_VxW2VXi_M7GmuKUu7Untm9c8ZW74oIiAeEsoQHLMNRZS2mImuBCxeyT4rtvjfY918SShJvxMHB_9RXuiQJvXTP4riiN0Sg6pmJppA_u5DZgggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQB9HpRCj77s6RpXHmKneOII0gqFgSwp0mJOEWCHKnzCE_XfJsrKEKuvnn0bFJlbfnxScC0vRU7ernPUw716M1UUZ_FwJcl_9ZqqE7y7SZzvv978aSAY0NgN4g4KdNzrPQy2Ti76wDfC15ldMRN7KKrA12ixy-TZfcSQLFtbJLYQADAF8O3W3pUrRdw0nPYQtLi-2XprSHJhrCBUvMU_d2WrduPmJzi272YJeaGGBf3j9QWBR_ZuKym2tlmm2Wp64srmKguKRU6nEF5TCh0RtF-GnaFcdTbd9kqja6vZ8R1RNd2sE6C_EMPfNRsx0aKqkKjU13dAZSCQg6UHlOMEyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3eePoPZP9Eq7rQkmfKBoEavImBsizzRH4gS-c-JphcjKDMrM1bt2IWDR_Z1rEKoNyJHZ59tG1bUwjh31fVJLqtzPd_RCHny3XZYZlkBOqHiGh8dkwDoupr3Sy0L-j4KqMUOjEmKhU1in4-DSLW-d8ItgIdW3HvtofdJ5aYVJbhkr7uS4s2Qr_quBlSlvPW6G4EePhxmNIlacbCRxtnaSs7nPdAeKj79X5uGn2sw4RHs5TiG54VCj_RcSbH8_xHm0jZjPHSUZ91p2MGY978YURLKjge3OhRyebZJq9PbQ0D6QWiInjrF6n-c3iIOQbYlqrJ7b0fLus-2p_MAKwQptA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC8QkEm6eUnrQEc2xkhcWzKczxuh4qc0Q3sBuBaFlvSMyHdfPpNHkxSkZJeu21kEF05EwSVgHIeDtp1tiQHNYcr7Mcnj7zK00lq9HgbIGAwQxk1Cd5upmqE747WCIUEiSKNkWf7-5_UnmBO0ww4RaUk6pR0dGYuQPkCg3fFSTTsmXFdYCgsBqMyb6c5OvsIyUMl0UAhYx2vVwsrp8SsVNEXX3DZfJK3f8seVhWv_2gMvJLtndkG-Ufc1UCUI7HZwdrNRRzp8LJXyLhZs8JpPOKaYrHzi0MBWD6xxdMZq3qjzJm2BnQCWh3glHAwSO-zYwMVAVkSyAKA4wNHgA0Bsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRkBzCeBCI6epSVMpxMFya6S_gVyFlk1ukLQP3UVCVJdpmxz1cjs3Y9S2MCbtUwdjc7Dxlbcf0unGhyzYtltF-qpBLsCSa7nLiGptWjY5t7_BrU1_SN_1SCqE8bYVL5a9G9-KxoLQvC5DUCKR4ElAXKWqEh1jcO6im3rl1TRSGFYdkO9IvrkQqg9lGGGOMcoIHvE9_uV7F3BUGVoJS0NJwrBSArnO7Yvphjck5XXNGcyh1Y25wb4gL4Ebr26mXWBE8kKPzoHoXUUk506tCVS2OD4EI0gy2qovb1tQVyfPnf_LE6i4gM6mupNvOtmaB5irBNsJlkT23iHpxvMRuKP9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV_U8hzy_YQ_4_oTLybXZTkYA85pKfWtCySeL9cKSFNzjsfnStWyBjD922mpGbJb5tOgAXC5hc3Fivjx-5wn8oX55KndA-ehYZXUgga23Gfzl40Mqiw76PXeTYkK-NwZNJNpH0LRjkfQDa0QFlqTeQlSH7kz3-DRpZfWJyYfi5agE4czdTxC_9-nf2FwcuUpxxc9zU7VbY69ixMJR9t0u2CNT3AY4ablq53Z68wKOTqznKltjXiCq1GSeOymfkKAU2Cx7R0Hd94mx-wwjKNWyvFKlP7iwoYl1LxN2JDdo5jzjvQ7OHfGArO26-smqSI-psld2x0G-o_Jq8YLC6iagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An8cvVVzyjAl3faitkMutOuqfs15Of7rDABdWVtMLMaQJxjJJ-JtixccpSO2kkkKlmGO7mSdaxW3Q1mfIPcg_4LMZjC0oZ-oMIt9c1HSs6DkFwOKgYq93s5Vzm7aTry-XILYFQo5alGEHin_Rotn1Run6xjwkvrwA8_mdA0yazxalD3la1MIMYS_BJ7u9KujAeXM_nBbIJMeQZ1gCxHOyuA7EH9C7J0NM7P54cDdNgk0pLQRYg2cbr2d76tdXruGk0j4bZ6eltmoPPtRLWDHchPn4fgpGdiq1mQXVOqdpwARcWI418t9QBqTLmxZKmbIxkz1H9tJAtU__SOqbV0Fhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMWdNm8XvHOMcrmkYcKIagABPKkSYS8gmLIjdNzzi0yThojZs5kRDddd0JFWTxLcSsOZQ9wIWwDmk3YSxvXBuPj4hA8SjUU4Q0VBPNk-RGClWKhpXqT9VnNUZEAGbkWyM-utUwsTWSgShZgJYhK5IgPlOm43vug0Q07ciLW9TilLo41IdEoZM4n6E7AntD5uW7S9MFr3U5R8W0NvOeQXUbyoCzqxW3jyXI3JjsssrsGELxkjvt9kmjVz1WDEYzJH6sOEHt-YlQqdKz5X7_gO3v2SYRn_vpctDJW61U1brkNfUJ8AI--QXfJK49YhlYVboB_rWipE0rQQOV-81MEfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa9c8nADhCTki6y06_Gj_PzPd98B_v884Fa3VAD0LDRI1QSXu_FSyOkjRuJCBQQCY__5VydAyd5Md_wI2UypvKcn2cz7IW4oVN7wg9HD6TfnR2ZrNnfWIibNXvFNIAu9t5uCgNvR3JG1U9_Upu5cKM51bXiy34Rmy9t159aIfQLKccHf3iAaL-SLWaSzEXcYkexOKDC93LASyG0vVozBhwJsVsVtPaUzMDlhNhwGYuKEqsDVLTCKrXQNFuRRpqhoFOrjjHlL7lEt7Nwnr_jBvvTi7CdtfTYsliZbM6EmPMQYdCRsrb4xiXz2ODRQecfUvzOg9GNuuUPDr8ZDKmezyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVPnM0hMqtrOd18fqER9TYdq-ceQU4_C42pxlGdmlaIeBkrvxHqKi9zXwaP1N4Rl0mG6slSAPtssC6KlgFrGnIsIt4vir6TJEMYF4-sYUtUEA2yRfalcvjaxhN5sGKWcPN8-HOc8mCarmye96bc48uC8Rw6Wj5jXu2mESveX5n-H0SxChDdzO_SklYJDDo9_dUOrdCs7Amo-HNk0-guGOcHgn0GdogFXxiSmiHJnq8Ili3Gb3_mQRtnR4bZ6R-KhG4_vyDbCWOhueN_D9UmVffdaauSc2tCPiXC783gtX46hs6MY4pNTrMjRDZ9dyO-9ppfrC_TyxeTWnnOMCyPigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE71urF17zQu8tldC2s87o2YgzfudHQqmQP1eh2E8Bt-9C-cIkZVm5RX1o39MW4aZZyVS2XkAqVOxbCfzfEGRiRkMHLMqqiLSbnSglTVT0m68PTCn_cPVSOgc9IaQFvB0v73u_PV9VUzzqVqDL6PqWtKiB8qeXdfWxwTalWWzWbzzFA8BkLUYgxKMvKZ2h0qU5J9ymRKjiKXj2euKDB1iXJKQL5QmiizvdvB53mbb39WkWmqrFToTANTTaNPS6mImE3ZOy3fsWTa5L3AzAunHgAOanxc8CpNfKmZ2VGZ7Pa3oxeus93aDp9Y6L2btIdM0f7Ut_T3-4aUE3t_zhYcmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3Q-meAs7sI7-tp6_Z4P3YKzjSJxWnI-NsurRqYa_Cwfu_pGpi2bxLAMF3hxR1x2Ba1znF506YCoedZsn-qSwZQu7D2jXs-jaHkWhBoN-97R6s9FGsiDRH6MEE-l_I6HwiZIDFgP2ywEIARb63oHy13cL4k0iAG5hnPDmhHOvZqvGPsljxnwKyw9mJ8E6-Ynf6CQC7ZBZq5a-bknNcCH5OtRWPHUOCut3P3a-fUrZbwphX22J_zOnopXxtXsiW5JN5m02DV9uQuFVZZzTkL3or4HNJuf9a2yYDPeFkl1VgJ5LANU3YbNLxSsrRsvY_GvRJCBm4GnTyl2_qJ9uJ0f8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NO9Ju0S99rXk8XrrIx8UFwfnHSwAJdUnkFByduUx96fOx-qFSpBXiMBwt9yauVs--SdwFRo-x-UddLEjsU52BEUCi2PeZiaQO_gYZzIOXSg9mzzObkAtWyDdHMrCdxPdIkIyzwBHZEqikQ-k1a4XGDEQWbhzsksQ5wZQfJRSu5P-Nlx_qMhb0Jb17PfF04mNjvxXXoWs0rhLLIzLlaM9fc4K-t7iKAkiuLkotq93D6JLx3PG1xTylDR6Whb3vNsDdIQBnk_Hw7N8TiPD4x77yM4Ygs8jvT0loJhFVqAXN_9TZYWmteqwKRX1yVzSC_nvNFRePvy_HQIEVFy0HgIMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKVdehUdkHtQggBjEiGezDclWalzlhuuJ-ZNnb0b2qpLYu6ZW-Vremm9Kc1v3iD5khc2auqLvHTFdKCsjeHtR-qtcC1tXadEfDRTMcXqN6qIZ5Xb73I_aqlwCstnITu1slhyvLUC7ojV4NFhm4tLqlPx9kRRYvGMtDCSHtLSeJNiSP0Ba1ITdeSUHX0K46xAqw85J_f9SbTzVDQm8cC4QXRFwkLRjzt4NOndOe0uZ3ruSF4bE27VWstF8x4FveVwVBbLKyS9D13bP6yX1mnK0sfE0CjnagixxoQWJv7r-BZYv3_Id0AmIJBKOYXisWb3JIrjO-NRJ39M0g3DICVNDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPAWm-s3AsOk5NpAt5P5VyUIDELa5oY7ucWCchxnmbiArjYwY39pRQfuwkE_xY_IPCLDpv3qeiDZdTMzZJJV6Ydj3_Vx4fBtLl6-BrTUzeEf66Zp8UPmHEx7SkRwSfUQYlGWuLBkDS3jaf8JxaOyTbghepXTPVOOrAsNvWvey6ZjFyfq_RXP4yxSiEBL3O19fyPJRdMwDva4D6KjqCp3J4YzY_zcLPyvnuJLgTNmPu2s2_Vo9Bf7wCXylpIjy_w_l2Mu7THhylnuyFe4VVMW9Cgfm9lzm5fQ6Wsp1a8JwFmuSqBr_o-rtTOjFDGNAQh4-Y1fYrLCzxg5MmXgISCENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkM0oPoc0TeQKuOXDEv3bnJOqmAuI3X5Oj7e4PSUa4OnHElJdFYpy9Jgd0A6AwSBsV5kjOkmZaB75c5jbo1u7AehJLVRccC-oRbB1suGXio8e2cmt3ta5BT-34ZMs5JZ5RUTiKmTF_dYNq7gJJMXVFwpv2OGWLuXoNuX3KnS9_E2M99Urnywbv2jdUj1htKsdSarl4ofmFCP_SHcUemu_JMHVL73VQY5YIGoWcUgjYoDjXwLIpymDIWHxP8v1aE-3hILHfBIk2v8dqYKIJh_GuN9WlYzlZLmNEN5VhSo2MeYTmvY4dYl3-zj7h1IH9SULaXeVTbMPL9p0OMHgOOfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_Gox4A5rUdN01QelYT2PUDbFJCXtazFgBkaDGQWNl6fcTUyHrLY35yWkQVouezA6MEuT6XhHIVmy29cf1_Nlfye7IVsKpjl7Qg99oVKpJuDy8FX-tSknUGeR_8V7br17omdFrUoKuoeyGEgTS4gpj136uYtK5olmp6ILVxoi7t9qaxah6BXgSKXWNhOmfQk76zeE-kaSTnwsABTgyWF8AMcOkgFj06K3ePvrh_pp9bl11H3gkx1WIEb5TyjzwNYxgtH5ZmsHqC0bHmhUZEMzXinqHKhUaPM5wVbFaKlyGxjNPuAnqdwZboocUcGx3VgkYKPBfU5qcf8RhBZcJVuVomsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_Gox4A5rUdN01QelYT2PUDbFJCXtazFgBkaDGQWNl6fcTUyHrLY35yWkQVouezA6MEuT6XhHIVmy29cf1_Nlfye7IVsKpjl7Qg99oVKpJuDy8FX-tSknUGeR_8V7br17omdFrUoKuoeyGEgTS4gpj136uYtK5olmp6ILVxoi7t9qaxah6BXgSKXWNhOmfQk76zeE-kaSTnwsABTgyWF8AMcOkgFj06K3ePvrh_pp9bl11H3gkx1WIEb5TyjzwNYxgtH5ZmsHqC0bHmhUZEMzXinqHKhUaPM5wVbFaKlyGxjNPuAnqdwZboocUcGx3VgkYKPBfU5qcf8RhBZcJVuVomsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuMdiGGnws29sP2GKertLciy4MtQo4o_Q6o-i8yj6ZJQWtKVXtaZDsf0JeMAD9XOKbom2afi0ATNB8Yt34eaFwmVEqLEeTLjyrV7br5lFkhxfHfZHpG5P369MgMtVP55_TVuex9HvMU6aE3eUiV_xTtCWiI-2WsstYvu9i0nKhf3QyMi3tfsdHYU8JurS51ybWwg7QtitTPAmliofndTdMKjwNDZSKRkoeohu_SORr2D6WVeSbn4TRgaWQbvlRDh9KAzZZKTvkvzxB3l3wL4Agz0Rq1jj198GY8P0PZtbdGfTvlf86Lvd68TmdJkWNfEfxoWGuPMYIOV_bmwbk7pPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMxlvwPK4mJfsjK0KPbmsoOJStlI28nY70eTT-7zL2RgwFNOn7HR6ETMgd1bv35xfALbRqnf0vTbyqnK7mC4z-vrPPKdpNvXKuajvcKX4LgFuTycadi-ltDXFS7wvVP5Wfu66UW9h2IvvYPi35puipFXyJoFuEagKl-mQ_SeSTHWn9mCmYKdDppumGNRJIqOcIfK407FWoJ-C3_VFRQmf4DoKh-PhUI-EXkV8nmM65K5E-E63lTqQiMe7boOwJ-wQj7uopExjA1MbtcAgojpsHkgsRFLJiGaBsL6zcOv2mueREIw2i9kMaxdfJO6yV6Hk943RFIsuIPW6Ohb-uLPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKugr3lmYElwC-6crqeEUypw6SYBr2YqY9N8xII6Wq53NibmMz4ukn_zNRGL6U_6iIMapr8C-xOG7WcLiJ-zgaEl5UdWdzhzPmXyRd_z70eurSkcQs0TgDMLYtI2XvsBpcJo-x2j04qBzVJacu5Hbojb2Jq6cifDujOC_xL5kcd1E4B4gDmZ7ALSLVaepizi8nyTDZXVS5zf5DhVU8_PE32SZt6P43PeOii9L3FOGKZZzPikQ2VVl0SAEydQJfflVro0ulZQJ515nNEUTGSx2oYq3RvdPE3B-TTW8yTOlzX9CK8TAqQSEYzB0Q9d5Qt9RNelDnH4N15MD-tNKAyzSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzzq9kaRZYqPWCJxChlPx4egLWRvZU44Gdr5K3iB8JVVXW6IOuEYDohrCvdU3DXqao-GPS7s-QyyFtwltGpDO5EYGwtvdWcCX13b6GXXYZztIauFn44LeSARAvSTw9LPCHq-DKacEfhrYK3rxZt7Gjgp_UCSZ7wbhSgeNGl8-CcFEwR4uJ_efSYiASV_yjEFbjFDCHc1hsFINcF-FgSo8H3sCxqw7ZXxUwRYUdISluBbHjJBbCoivMVuhdNlNxNiy4TR78uyANx3SO2L-e4wRC2zGIFjeJObNVVFzWcbJTl6LEGtDICkWnkd8dLSkmQAJOxDhXb5VhmyDC7IpCWN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si_IWOgjc5T9r-oK1cGQ268OC6Chj0Z71Bm1nv8wibjcUC7vF0YGalToRQCFX8deyKB302ANDj_hj9dycR3pWy2D1JbIDwhtwrap9wXmeCRKCGBeYttDFmcscgGki9F3K98MMpgHWw5fbjuCjRppL7p_wz-rHbjfwkGHc1xIkblVX98QjsDllt2ldaHb383-djA_EuA1bcdft2uaKrHPmZLrl-XuAHtrrVZHDzfOQFqIj2mZwgP-BAjmuzx0sNnCPoF2pMB8kr-FaPMD_fFXnwSVFqclOZTOgAqRuwvN3C9CTMWU2XfwXSxz3zktnuFjUFJuV2q6FfoX6solUDtvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSaXZSEj6wC3aCzX1_8Ufp88l-dXApiWWc2MCoBdRyWXg6P_Ogh6jAUw5MyS7ZZ3Y8bqOUNvZlDV7MwfdLi097buviyxEEZOv9MIbq5zOqeIsUX-s_GIE_Z0o38G2ULhBY2iEw4_qLkKZiDPr2QdKO8HzLpSVJm80ztzwBa7xGkgWPp_JMhi5QCWeG05N-g2aRJ7pxPBye2E3-niRMIg8ZMA_0IHesSPqKTFNSRaZgBckkuTK9NP76mvMiVC04nCSdWpkNJBPhpf2vRSN1J3JFY8rE5PbRgyKuWPmA9oCIoAPuvgzElL8hTu6BIEXUUbS4FJyR5kMoI5ysIZiVFZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQyYv1buHye1peXbKKxsscETPeSTeEFuVxgW2YkFv3-snpl0soOQsfmQ_xaXPJ_ShlpshUG67Bs0X26ukBC3n3udSoQ5yi3940myKZafMUJ2P7E3_7mw94wh7ESDSlWCEUn_IE5vDapSXZBWHR5ufOOojk2hOD-8YYJlHTtYk5QgIpBmdig9RF_lsySHV0tdJqkVbUdBrwvuV2Q1xLBYdKmaTBXPlagTlmPOX4LGqumvE_pwz4yBMd-GlOH7m_3_-RzNdBYgoV3SC6YsufzCbX2AcGYNuQh0qqkiyNaqm8275zVYhqZhLCs3B3m-jEzdUrrB3eD9yOwm4-1qF4Rlbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
