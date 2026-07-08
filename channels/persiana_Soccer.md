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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjMYdaezMOmA7S1kV8SQmfmy9o9Yt7kPco8f7bNgw-i5hq7CMV5hNLZD4mUcrBBymUylFt1BQeTjVKQd-17s-oZviY-gmFMVGVM1ziDprzTy_WSvfdWVKqtzDeY9OyUVK2ZhqnXxQaTCV9zBIGrXigWrWn0pUFWbJgP15YWeRjj-UmZW7AHGAv2eyRpqnhmeQf0TgBk7dLqvjhb5HcAyCbS2nVZQvwnPOe2FCicQogqav9dD9XnGegCAzhcK0gDxp9t2HXDNGAmlNGw-RukVpZRczhcoLJ-WCvFYevezMA1ObNPT1V57QxAY5kyC7Tu2sQ5I3ZyXcmS177d6ffZSMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_YCvpSJO7psqko0jc87T4B-kgA7FDZ-Bu5QRngCa43alzva7RNcp8RlheTGAD9zK8Wi8IBUyKW_pbyizPgavZsv3KU0SFmBZqyxYBnjqu7d_T8adjOaXGkRzT3VYs5U14v36h-GJ6NMkeC-vR2w-b4aAw9Mry9YxMChzdOjefT8nhrTjihY_qR6hpN0FpQK__x7q8wP8E-w2aipMCwhzbzdzjyO93xKJwsAT3rAWpjnxw9egBtoustmwQ7XcJeDk2Ambwzey0VruakL1ATbH1uC9SlRaaYic1maVseuGtHCuFOtkiX-nj3DlvGlpSCG2z9w0qPfb-tFXCCgGTBnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk_NIDdoaCiuxuUvVA6yPdnC65rpVBrA4sXkJg8k8u9t22Yz30CFx32Q4Uk1eS43p1ugY8e_1bSitRUxGyNXispfedPFD6AeSjz9ZA5C22DGiXZSCPcLx6StP87sbdcCidESzil672JO_waScvrz_gsgrspD7OArzGUTfzksOAkPTTqZ7-QyhWcbe0aR0bFHN4FSxepAOT54hlz43K-ghgmAQStESC76q09Yvph1S1c_AQUp5M50HCrYa_XL4sUt2wKwc6uSq4YqfLodFoP6lC6ghxEyBjRq89XQ_GFqxCV_pdwFghRbsQVkhsGiLdvf0VIIf1c03mhEqan8MXx_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fU1uswUELUJkxt2JVXs3dEvCKxnaTzR9QhTZfrI4gIXwtPMN5y2_Sk5zTJioi8c-GcZP-0veotoHwJwZBtnN_y4rdE76JIj347eERATu-xvVSYvgewJ2hq88i8D9_sBXhvkTUAw7WOcBZ_ZMyF1mKe_T6TgJoqOpIjnDEkijKrsm6P1BR_ODc9IlMfFN--40l5wcj7QcKRXk3w-8nAQvpGP-Ky6qvtTm29crg4rrwKVWk8YSNl7MwzMy1-LAQk7uMP8RbFXdFOyi6qMXpTK8WHC-XZr8bptfMRAfVp03Q8dWIujMB8xVRAqd_WIGgN1FrGWNjSBGuJ3hQ73LQJyQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lutGogflxoDdJpAfyNdOUlv1FwATUMUEOM502Q3OPp-Ds-C90-TdXg-bvo4up33B_nbKR__gPTrDdTsKSDx_v3X4HsP605_rjG_d-l_Jx0ODpclxvjKQkzt7m9USCot8jMOKQEaVv5-HQuzFkSas4S0OfK2s9CZVbT_F6h-azhvgmcwPAUQBQJI8Ztk_Jwfm2NXzV_CmrJFYI34ruaFweR3lIOk8gFQMslFyjV2u1B3HwHcc5xh9v0PG97d6pOZCg8J45ydvmNqvHjdk1SlMWYMbH-ByhSO94yo9rRn_QU48vzdXVqZ-A9Sx1Ao0wCbujsTacCgGlJ1PjZW4VSIqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCG9v5fdWmLM0vY6qUfv-TRON_7EhKOnP1tmKnQE0scQP6-PPQ4RtDqTxmsxRtbh-MQP_7xfrp3iIBQsuIVBNWS5rPgqNvrnnHLrG87AxcBWq0zRA1pisBOoilbEZIKhhv_JsLZafV77j4tPx52CP2DdPj45l46EHCot0L2VA-c_-gXFAJygq3OilwL-FuX8nP_pdtSFRMqgXJ1kLlq89mCVT95_hULnh7zJP-Cff1ZxkGJSdYlvpxMF-ZQowwDfkONSr7wqyB1WCep1l140MGxiWp8iQeM9eoVgDVkS3akzkK5zCGFSBNG5Le1LElsXgjM5S-qFyiTGAjJGmJhvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25177" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBSaCDvVU_dZ1bbQs9RPPwEQZ0vQM-TOLJH_R1hTjX2Fyeohjrfv2Cm0L1GVI6OBpGZ3CP9F021aeBDS49VT21RSWGg6zM1ky5Vs6SxNbDlWIeaLNTVST84XWaDaZPXnVgFLVqZxt4n-avolVwVhtfTgA36G-a88JBGNyCn2JBBNvgExuz8W7t390iLuklae5Dm8MfEWJ_BOM6saRqLPDRG4YrbSDUzMYjmfa4CHA1iJaJ-L2YAB4P0s8QY3LN3MLAGbwJIamgf_06Xx_NqGHZQuxztINeVkqmmp4A3-Gx2G_Jh2Uf6OrjA_hOGo44s21vrpKcarZ8BAW4cdv4ZNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu6nBctNXkuVfC7PRwhvv3V__Tmk51WTuWxPupeDBxAGrIRfgj0Rhn8ZUxSDu12sB4U9vdC4MkUrzzMjxtt1S8qJJ95aqsq8qisKlHMgTaQIp1m4UqhU9plt6Nu2MxVy3aSPLf2akV6ucatFW4jJS8Viudfxs29N-0jd0cwezse7r4RgxKBFLK3QSDwVX1xSRPo4grqSPLFtRrI-7uclioa8EF_JH7itOqFSShye_xQUDagqJZt1UpN5_imI_yfGTUbYY4bQ8HgMGw1t7usQZo6BRkxw5-2ns11C5r471nSbRyS-CWGQh0DH41tJEpfp4hXkcF1GG_0QXp0f3LZezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdSogmpwQvoPWoF__nmzXljdB4AmDKV4QQg7w6Ij0Q2gv5ErTFhsbKyAsyCaACuHUw7iPQxOr-AvFI71_-elpqNDyUk_0gAUz281-VzMYm4INcSHllTXufA1jHrNvlTKmP-EJmp38wpWc3jn-N5Rj5Q_YAk7F6DmGm-VJZF9D_WBshHv0_wTs_MPt8t6CWfP2IzGAV9LqAhCzguQOlhAUkXwL3zMbQn6oZam2wT7Na2np8s9wycNIL1J-vKcQ4H5FnazwLbVWRMU5W3GKWjGPHysQdI-xseMk9qDakxqoPHcCgK36JwlfR9-LCsyTGq71Iw7AZXgUpFIvqAxwmtUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXoACGSJ4KA2dHO3RvYT-LdbKJiPfZbvAgBpir1Fa1ObuTtVRtMorRwJh1Gdgfr-jRQfm0jsOivDSI_aKGvTqGlvX0dvJ5hIqZ09c79BxA1VHZ4G6OapT9dutu3l1R_Nel1uK1DsVxPhj5c9DCguCKQiZgqi-3Eqb1pEh9-nQsXKAl1ABcYeB_nX8jdQEMkGWRrSssTGBij4-3lSfxYCOjGMIPZry0cITmk2fbqGtftKA_wIAsgWfI4a6EjBIIYpV12ih-crZF-krSaeuMpn46ulhnjw7vpNqJ8mgpxSYv2r8hf6wgJE5yQngYzMbSFFBibIPY2iSsWwUyKmrWOlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl5Bc0tUmuT-_bLjOpNx7rscgVe-ubT1-pEwVMIdfk5KAMz34fmXJVk5OdX1y3eXK_MsVJVkxjWM-npvD3kahWkIt6w7HUx2PfO6GHJ32Aq2d3daiS2znH-LNgzY347QO1hmhw1zw0PdEFU1IVWltOZ0W700jKf5U6QO0U1hLR8m2U5g_AL4uPAp9nC0UH2jcaM2LFvgXPfmDKa11hYk_3pJN3iUsl5w9cGSYabKoOJRVB1mvDfTfKvPtijnwzBMsCtm2LL4ajzAhitoXg8xZ37k3UPETlesrkYgCvfx3FJ_6RwdaWgIOskzhoXDfC7bWW_9iM-JHyQUr8mqZeYPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl2qsNJMBs8emrfkYcGMhJ9wrHiqMbZx3icni5rp3jNyGpQ5hH6kAIffqwGfv28Y2gjWrwxwHUzUbvSt5iJdg8_w0zAAV29Dnd5Wg-d0cByGTNocieR8zHntDksgf-t1mdbKbrbIYV8qqYhaNthKaVXeP3vgdZOoNflJ2jtRCcEOB-GIEYL90vucCLvflcWYdHEEKyxvmcbrueInzzlFra_5W_6v-iKhojGpXH1H7hbuU_IQVjqXwE6I1KWZxfAmeu-sPQOsf6FEXhadp8y16FeuU0ZzVSnMWN0gHEKy5phXctzZGzYwAOuKFU1zVIucty2mzaa6GMqUc_rmx71G2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0uMJDpNcrN5UrvSH0vtkH56DQgz8woy06T0b0S6aR4tyMJV6SX2p_lfSGKTt3KHK9rw4PA9DiS7XXb3ucQDP5ss7I6HiECuz0Rar-S0dkdMU-vezyUei29eCh-V6pcb1hFfPtnpveJ4trm952Cs0ABwPVgBdTXLGbb4xb09cQzVDi9_kv6XpFVjJyBufkGBzgh13g0qxRw8-_52ToVx6_G3lt1DtVPefRSa02hN6kubA2aAoLsyYeotfZB45oUP24xznDYwDrFZ39rYiqFotDnEUWSGZI1hxtl8P5UaIkF5VHt4eCdgBgR-QiSX9mRunddpU_EYRBuAD0-hz17WMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZGZ64jq6wTdRMfItnMveCJO0vhXo-n1FqBteDytEKd9R0cRJL_0V90h3sqNv1CWdHl6c6vOQ48sghVe7_2tuITDvkmoMMjxMIvctHLqhwwFSIVCntQVBXfso3cQSKRQumF7f-iZ6jyDAzb8rsh3qOtuI4SytIx3MG7ggLI3H42UZ_JgODgbUyxYFueC8rJ_yariBWMv1N6-xxrAIGvyYzRIZNRaR3ds1dGmft9HLCCMdUkCvMjAI_Us1rekNuXs-u7VFUqsuwE-uNXTwY4ToyWt4uD4vUlCZVtu7NVJCfHXqPiyTqFHnBrtmPMJvb2O9sNg2_4L-4vYKrb9dCQP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EevuH8qBf3x2t_6cCO5UJ5AgG2CtfBzYhNfRuvteBF7b2Bv5QMik29hYBA_AfI83-RA8nNmBlxc1iookMdgfHFTR9EOIVG9r1skijaLRyxiDXbkm0Pw3yT_0g-cf7tmsO-SP9HN8KnTcKme9aR1IKQPQ6rdqRSqYBCI2aYOIy1e_o8zKcpYOAqU18lRqXPqrLPmlnSS8FpuYjEtNOwxbwLgY2o-QyBGxEBS8lKPYkmw523lMywQicJuMhP0jSVProFzAhYn42aeIF58TnBQw0Lu7IiBBcVTRF-Qgd1yLlyB0JTXY0QKF5hclqI-tkBT7NyVOX-wFberEX6JSjorZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ7TlaiiKyG2ckC_ZgcD4Aek-109X4wCBjEJEF9O7rAx3omoYxAnfBhcNBzjVhtH-NEbeCVSkGqWK2X9dbc6a29riYqe0-WLSfGbBSjf4IXoIS1wwVwvtmJP-yYiKGWzdPCAxGj-vnwoV1uiqsBf7jmirvkVCpBGAU4xS8NnKqWZHdr9Wb0_Pp-Y4uRwWiOWT2iqfYXMmd56wW-ez8FRPDNeUN4KsIQtXdoxEhN9a7S2vN2FL2-jG62K_Qj0UaFSWTYNItzTDlBxpnV9P6nm7k5CTxf9RRPzrmiZxz3jdhqswmya96Y2GIL0HYaAU9bpI-S99MYY877wNz0nrSQytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB-y4QwN3W3inBpLygUDncdWTiZNk-Fst2AHCE6rUdOsQi5iWOV9xwuUOG8IUxylolOAjOCA3wbqgCH7j1QtCD5PR8jduoVhyrJz1YKPiGiqr1fUU-MzIZRWwT17bLdtCX9a6_zh93MyNUUEb1EppAZr2J_zVfFf_1c0bEBK8H-rVKLJ_URK2eiZ6FPFegUdRjUDyVcC25rMQ7up5zgwmlDcm5Xzch440oaEq91fjNexs75BO_I7bTUR4Y4gXkANolvRGN40-VpbiwYWO4bWLk4FKbqHwvtEsfV0hgtqe19rqqBcIW-jJKGh9LdN0QIAOREIodAMhIvPsmOsog3Trg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4Ev-k_8vbU7LiKp9wr_8ebitIdfU6I_deA4o-Z6VKac5Smdeqk__VfImGD7Xd0y9jdE5deLfA67tBR2IdzFDBNlFIBksvj3PoCPeYKgnhNW7wRyjzv6sHNbJLNOJxxbSmgoVBy0QApZOWl1GyuK5ZViVy2VQt6TV5826duNZLjONQPRTwvu3-jYg4y_2TVeQjZss8YF26nLCoAq3OGWn_kRnGVnc1WWOvYvWeUtnHddWU_r0cjKnaB53DeV9_1KfLZSSZYqWwSl2DYWBc9Ih2ewRvP5KmVABgR6viR7G3MzltYWLbbvqxCwjqwNRsk7f41sKGBS9H_95XNTZiVhsT3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4Ev-k_8vbU7LiKp9wr_8ebitIdfU6I_deA4o-Z6VKac5Smdeqk__VfImGD7Xd0y9jdE5deLfA67tBR2IdzFDBNlFIBksvj3PoCPeYKgnhNW7wRyjzv6sHNbJLNOJxxbSmgoVBy0QApZOWl1GyuK5ZViVy2VQt6TV5826duNZLjONQPRTwvu3-jYg4y_2TVeQjZss8YF26nLCoAq3OGWn_kRnGVnc1WWOvYvWeUtnHddWU_r0cjKnaB53DeV9_1KfLZSSZYqWwSl2DYWBc9Ih2ewRvP5KmVABgR6viR7G3MzltYWLbbvqxCwjqwNRsk7f41sKGBS9H_95XNTZiVhsT3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyDeGUTAgeSvXlsqqP1762C7XozoPjbg79NUcS9eAzdgBehXp27BAxNlZ07ha_J_o0ToooSvGrmp6f4_v8FmkkXo6YcWoIGHoA0EfpwP7eq_dvEC-WJ9S6XtHV50FbBv-LKc1fF5b2heiSgu8xitZ4rmsgyK1ku8XPAR4bkReEIn84TPGbWjhZPpvx-Q3hYn_lMRp2lWEkJwZ-OYnWgqDnXCaz-dz_hgpLVnxn6qf0_Baethe3jcwDEDrZ34vlQXj_0DBM5D6ifb-UzRGt5YedV7Fr_Qj5l50By57SD0nF0BseSbhE_at0RkXQtZLDISFitTqmYBzdD4mAjn5IMCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnBMyirs-eJR9rAec7KbmUtMjj5t-4TaXBGecmAd8S3aQdYENueQuTNF-TENTrsDoSnoKpMohFdmGL227Naf4zFHDrPtoPD4ckKaXueSINVl41EO_d0QTSwPz1mccI4YE_OTjHYHVxa-nvmz-yv3uBejeks5mEKKdj1osrp8vtgYNtmwhSnGQubBdLcFfgAgXBVPN3nXmOcH4_oQlxynbGSPJJOK7gzQryGv2OOzjlTb8AdV9a8NFsOB3lfUL8jB27-JPKZk6xhzDSufOjuvYIG12FZXzS54XA5K00bns_h3cJhhNx0NQ84nntwZ-M8FS5crw3LLRxKPJFtH_ukCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl8xIxNC0Lkx4rcE6oSu-QJ5LLI_AfT3qYmfX3ek38cRjmw7rZGmPdSSrF4w7XTASGnjPXtoWA0oYaUjrZ3FyfIGKHQGSZkxUHoDTZpkRIpGfFDR_gM5ABo3U0x6P4EXHNPENAxPl5jksZz3V_C2aJEoat2LgaOdzbc0Tl9opMK5no7zS-32dSBY_eG_tY_jeqxrTk6Rev345FHxJfA0GgI4wxBv5iBL6fGsRHq86Rsj5xcuRZ50olCQ6LywRvh6R5rIz24RdF5V3YHNlRGQIPfPIAQQSi8WR2chVxfWXRTSRsHPkshaebTg79rgyqH6QQJ9IerTe7EV7RWsXUq5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=ZGtWPrTp5-YeGhmEpFGUzXyAmIJQ8uOLtnmkhV3bOsishEPP_95Cr8gatcZTk-OUJA_wjc733EBkGlLMuAY8C6MWgbZXRLcF5_tUXKLQkMzxdIzt2rszii2VgiERqXm6UPuwkxTwcx97jsKvErp3UcfPtZAoQ2FtW9UC9pmXknBw4zE6m_cAX-8mPH2AxOTF1GZV3wziPvDRxcD8bu8Un8qzwJw8SzS-gXH-oDIJmedui-CEAHWPBKsUtNw_zRwZgsF85hMMR50nH6nwLF8s6MwqjyJV5pnzDyDgrNVWgpmbT_sUdD-1DYi2ry4r7GI-DoQGg1kuNgq0i-UrECiP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=ZGtWPrTp5-YeGhmEpFGUzXyAmIJQ8uOLtnmkhV3bOsishEPP_95Cr8gatcZTk-OUJA_wjc733EBkGlLMuAY8C6MWgbZXRLcF5_tUXKLQkMzxdIzt2rszii2VgiERqXm6UPuwkxTwcx97jsKvErp3UcfPtZAoQ2FtW9UC9pmXknBw4zE6m_cAX-8mPH2AxOTF1GZV3wziPvDRxcD8bu8Un8qzwJw8SzS-gXH-oDIJmedui-CEAHWPBKsUtNw_zRwZgsF85hMMR50nH6nwLF8s6MwqjyJV5pnzDyDgrNVWgpmbT_sUdD-1DYi2ry4r7GI-DoQGg1kuNgq0i-UrECiP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=nfPYHGEsIPDbY0yDhY6aWozDhoCkUHzmkDtWEGabCrO0OMQI1tHxaUM2DAu4UOSTSkze4jk8o0yhVzcvR2XHrDBGdodhv-u0yRc1ld0VUO0EtTMOC0de9aisMp7nxDERwq-oaVB7dU9LYnWtM6ua8pMaL3_n6jgjODkCCKwrys2bBx0x3YK4FngCdsrPX7d73MXM__AfXUP3zLl0AApWCjpAwyNwDLRBS-I0L3Va3Cm60iNJbIndadFBFzXGV51JqPz-GNwUxD5-IBEOrA8cc8V0D_AhPtbQWpmBvpPbze7Uhru3lch9L49jgFwoWQ-IAJDo26kH5IFZQrOCZrpZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=nfPYHGEsIPDbY0yDhY6aWozDhoCkUHzmkDtWEGabCrO0OMQI1tHxaUM2DAu4UOSTSkze4jk8o0yhVzcvR2XHrDBGdodhv-u0yRc1ld0VUO0EtTMOC0de9aisMp7nxDERwq-oaVB7dU9LYnWtM6ua8pMaL3_n6jgjODkCCKwrys2bBx0x3YK4FngCdsrPX7d73MXM__AfXUP3zLl0AApWCjpAwyNwDLRBS-I0L3Va3Cm60iNJbIndadFBFzXGV51JqPz-GNwUxD5-IBEOrA8cc8V0D_AhPtbQWpmBvpPbze7Uhru3lch9L49jgFwoWQ-IAJDo26kH5IFZQrOCZrpZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5loZ70G-xM_A9SqhA2H1OeTDXJBMSDTuKZzd6kI4uQC_PHEu5FT8mVQJADKRFbimzfWn5oVCDCxQhSfpdIkrJKKXyT_UoXKQr_G7ajth424F2kVKm62wde5ruO1DsMiHKRvNWGPOq9g7ENCsaVcYv7inL50G5a40L95k80nRm5lJswdyzRqkePuXgMyXLydz5wO5hHzSwYn9E0PQPR34Rdu-TllFUxOfGxj8_IdMDBbT0v6w46mwyNPr0AD1nygJQn30iNNrZaDDtUc6-bPlmdxoHedgZyOgbkLPFIpIw7_I1OWosYkAsT0FBwit8Ah_c5SNpzbrZr7VD9ikO6V1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ci2eRtTDgwz7OeCC45fuXPSNc99vpNUQXfUSivEYHMENorscxIGw5ya3YY_xEBQQSQQoI_22_mRKq3OSozJWJCPIj3jzOM4d5o-GA7gTFFv5WOmmleFWOYREHjBEp2_sE1w98EGfhXU8_gh7oypDq8wG58GA_PkjUDEc4VxtKYJM9QtDlrStu7Xs1wcxLgfp6ralCGlv6x8-Kayp3s5PipZHBq3EpIHTKhpmOYZz4kid-QtsYaIFfxndkkc89hgtqgMUZPCgmbOT6fsTPxrscfA3z-MenCAJbUQyXZrPcBaQ1ALplBS30yQyLjWfuna_3y8RlYnL5QFHOUJwLDeifA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWMJjmWZ81wNp4-z16n86RmAfbDKMsVTlIpJg3nGKmZWzniW6noasm9cblYDdjfe8CWkWSX6fgGM2gZCCBhaPWRF1ZPV3olnyYQ5OJOX0zRi0z8I_M9S_LhqFApNtZV1IYUx4GKUNsqNChhgVEnMVImMryw-olRX8UbwNIq7Ppzz723ZjiLa25COi85YAhM88vG_x8QngDu4rOrhjk-WKB-Er6SwLad5fCpFOpYk9Kre5f3hIF8_PabxLfSq0Mg9BdHR4qCNDxnD7LRcAWe9490h8Zsf2_6nC6q1f_GrEm2l3FxNH4sJQWxP7-zTXM5cMhkZH-By9gLssSOOVoNVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6llFZw3zUjIeNr8UWLqwyOF2pFtxvWq6aFhfaatReuGhMOrA1kRwdsDv5YC1b_iPc4eJy5rEu4vdqJt9vGwfCl8od4zJL1OlK53_1sDPFPd3CliR7l28sPIe3IBYR9_6K7R-e7Vdk2ka71GVLpejMLJFk2B6XG0rW1Tymht7bN8XY-vWEbAR2PXZ0bWmIx6e52MB0h05BBofSNF3Vs_68YNa7NZ4Y4t0p6YQhqVv34sY1DFsFE2Jwd3B16psYTvYHktlN9LPLPKr3fV9vGNkFFR1910NxJhdJ9oYV6S_Lt20xswAj7ZIS8h2UtN95wlaz0M1Zrt7VqOQAmwra4o0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVINSLVCnHlNkyS10b-Dyax2lbwdmq1uZIu4bXFJsY4lx45lk2tck7HGjQHwY-5j1D4Ka5gaSzKE-veizqLPtWKFewo26JASwzkBX1gBQ21xeXq5SjLssFka1Suld38gwTUJasq4H0yYN4UMqrNQHBncuTRmmOo2QEZMjjAHHyeRHJ28v3jlaTyWH4k6qdBVedgej3yGd7pn4yzwyFZHSoKFzMHx2c_m2l7J564V_fuMWszyDLebZnKH974mI08idhnN2CG18ukCWdqvJ9iJDNy3QiQc9u5b-JYqNLngAdhLM2slgwBjOZ7gbdQCZZ8l8-ZG7pUYWf8NIQA-_By9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fem9yK052MkTHKyfxCwtbng8brItZgt7KxhYe-J3TV68wE6D9Izjuy9zFUsl-N8fs2-E5f5V398LVrPdtcRMqrUCgC1haLHGv5jmOUy6EwbnQB_SaTakG9tPbaklxe05EZifo1mtBhB1supsaK3Fe3Pk9HXRO2hIuxGSeq4jMBwTIIQfs8iqOF4IQFO_eDOBmu0IFiof7p6orUvT4pef0vWNZbd2sQCycpNGgwdezZKwq8V9etwDBpwFFcC9hU1dhskLwIFB2zP0OYQVtQi3hxVO8oZDD3Jqm5ZOzVrwRbhd4DWBHkzRoViHOwNKjsSakD0_8FUovC3a6Y0z-qnDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Njp67P2i1Jrf2p0c7Yx-CmGlkVprkbPe9WsALC8-rtL0Jy4JBxU34pwdTX3GOV_Maphg29_i8-hcWuqpWBsEbudwr5sq2msu_A7v3GTB1IedvOIlppEPto_jbaqPwwFzT3vUNzmLv98CEeEiDlTPCwSKYu7tImRC1br5bk16jB-LXi5w6cGvKRgffE7XBpGyKAj-e_3_pWVtAVvTFmx3utd7zLTKc-7wyME5gMJdvxWY5xUfXDCQKffWt38pSKx7h38PgoacOapFuUEMjZjfgUA9gowjhgDw93YFUFRnU69AKwSnspnS67vk6dsj1odnnP7p4ikRwNjEcdXwOp9LDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1npkiGSwXr6iELeGPdK4EnxhE5-o6FvfpDHVmyNd-ArSsox8WYlzT7UNLhwSm4N_n-znKQs7AtgNgWK089VyF0SLuyD1BhTp6a0DfZxsmQEkbYeMShbT63YeFjqcBsOsIKqfN5AAnXEqamcWPuuuqk5HbBJ4JfNmWIONQls-prN_zuHxuVzqkwqPJCSgbpTA_uRIEynl57yxFyyZwtMd0_W2pHHkSpsEGr-DwkkwIFe7nt9HKGdTu4WhQpXE9HIKGDr6bCSvaD-3Y3NXJ_KvnHpmCW33X7Jy-nSAyJtLWHe-SE4y8ttfSlC73PVz6pmYQEEKHDQBq5QP6p4zLbvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBlhzS0cH6rbQqheMfPe1L9y1ledzOa1Y_8L25ndGAv_QH98F3_xknOgcJmLGsVCXTg4hA6oACO-TL6Nm3_2GM5A9bzXyA3Z2GhAO03yQLw-bQ-g9g8xCd5yp_PHYK_Z4OQsFp0SkbHic4mFb-Kc-FsGz8Xm5ZwUuNw8X0qZUOW3eLKnK3kmRaIUdZdV2K9HzjR6tXhooDE1ZLZqaHl1ImAoQv144tsIkFIbsJ1oz61VYpYQxAaDzfrHxWQOWDA-JVmsK1GrqX-mEsKcuKt0cj8njWZAUDbZ3qaS17NKsIJKDQXlD-eh3DLMUvaz5g-wrDXJw4nEWPFFOKrvs5GhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKc5rp0BkK_8C8de44PzHxdDTfV5PQXzyFdWY7NuSiKs5mhmCcQyv0EVEH4_iM0t8Qjh04S1slMMVxw6Xvs-Rx4mYZpDycGOni7S4X8yTeb9JQALVxgUSYJxPcj8Hj6tI2JC7lHK-yMz3IjPHr_sjOIq84DrPt6tl8Ipteqzb5mLNBby_SPajr-i_LbHW7xC1k3DLZJuxCWWXuJ-ba286Y-oAbGHbuxEuQScmYxAtUc_TSmUeCbiNEzFML2pfseC0qLe-deJ0RAPjYGo9TQJBozSNrljd3zl4w7ipGOB03EDSd_OYNzWAyZEQqQzahUGkhwEOp4KM3RWVfeh5F5C1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNLKs_hA9V_72NYVe2r5_Fb71cNMTWa4-SKuqfxOgsYDQB8v645g2KnTpsjBCfxGu3PeFqvz2q9ONJvsvEIYvftKH5_6vhRjIOAI7zpkjpCDx4DVMKeAAQdAIlCzqfCW9mFRYS6D7sfRLYFRj4m21zNDPuo7nbcMnuBJ3rOFBjD_sAsEjybFsd__GT4pnZCcCw3UgH8dEQyj22CkmlZlERxbzK0bewYLfEp7R4tJs-L-qGp4bD9g5JtHv-5w887T5QyfoXZCF2ZD7yZy-v7hY6opw8ozsfgkkFr8w0jQqQ0C1lmGJbe0a5DbjZw8ZCOreRHtr4_fXUmo4yQDnoNkSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYjQaExiMouKcnC-zEKvFnUGSGF5VAsdq65j6Mri0nznG2YB_QbrXer39atmlM0pZ3nMCrSs_8sKV-OuqT2j_RKFbesssJhCyJlptaV5rMrJZZDhar_cy3gsTysxOa0Qe5i2uEFM1FWpRwgkvEVIrGh_cbe0-3hLonHQXfSJCSHonWe6ehW3XtE0g_zEmNTxkWdZRlMVlhVVapBwXGh-KQKZm0wkbxsDvvyrFqTY0sEb3zJDKPN8nzQy24IPBI734QSMPh-rH-lpkVSgbWwm3kcya1YeFuQmxh9CgRm9VVKUOK0j3DXFMS5QZCZDlKGkwSemW2xq1yoCZedrln4BIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brntzDjJyZJtRxCaps1eEQQNMKZkoF1COAwJAPR9e6a6DDFwqVsuQjJlAhO-KoomFYHuglqw-UVXzSqQ6s5qAbp8ci_S1hv1HB6h1qyw1yJ_n0SSyXIXmmovjKicWi00-pZA79_W_XN3zj7usnth11xn3m3EaQ8LdNuzUGUaJxvkwEJCGkPGjwSHIPjlnCiwZ_jvq1F8QWi6sWDLDmjKHwlqIeqiO4vIu8A7e4f_ztKlLTpqeifufFrgDqpBqWxCCewuYZsxP3Gcev1N0XbIXLlthcjSuG9ByrU-RJZ5b5xyEBFbtNN9f4JcbpgfngEarl1r9axiDwXFIimQZPKgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-e9OI2ijtG98DnQsISW7pJUyK42OET3zOJn_RuQ9zhoVvIPzYpfUMX2RjGe1m8ZlZMati7khMc0bhLPgafF0vsD4iSDrgINU33mOYGHezlOZorb6obsiqm9Y_VoCQA2JIJ1oyOHM06oqRu_3_fLsuDKZnAaYtcMBysThqK5J6-rKIX0EP3KTzrw_FnZS2EYCgP1-75Tdbk9Pvje74-G6rHk9tv3y6D9_xAuvRdK-k5yg1QRt-mxXAsH8q5rOpcvZ6BlEWBi030wuWPbZtduyX4mrMjFxPGTqlb-Z19Dl78mGPQRhLAVHOaJZUaEei0OlHhGixtvq1qt18RR5KjVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cImh8t_lHvrLUM9eZ6ofg9jbKCacP1-wsx60u9T2mOXh5GZvi7FR_omKAtQhz_ahuWPhyk6F7-AOfWGR6Z6AEdVOfgFB0rlubzMN6IZl0_WtrutyDwTfnvaHKZyZebV2Ep9RWIwvLAL0d2dxv7Qpk2U4iHyTeX75WXKtuDI4hctlPXm0GDQ5O8AOo4T2uuImCHy8zebKkpOUN35ChjyOKTcpUOmxCv5BYGMIxjOKkz7PB1ZCVeTf73UzEg8MpdCv6dglgBcKwSo7TguNAcYySdt0u_P2yF-IA_IxoWlNtuUHwbwAsFO3R5sVEnUEXR_2UeF0_XPWBxYQ0Jmbh-hmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpbdcKr8hrmbnHmU2wC-xL4gVBh0GAiGv3tfxYJRfl6brH49ZEQYHAi47f2RQjUycOSLBkjXKlUJyUtPsP0GC4DVc9-UNjSyig3j6FPU5paz4WiyxXLYaSuhmU7o06UXojxUwI5yXEMvLb84K1XpivyyF-lsvacVLyNZnqNsM2B2soe_BJDbgvHr8Yx0Dj9tCTZUG9oYtwb6ksaTLT17GbO7OwOkdmmgiNSuZjEehECW3ToNVmMHhidsDSRR3Dcoal9EmAXujUBJzziyweri-apAQBAMaGSBFfyjS_RZHYFs7yQSW1fWyX-brqMtr4GMMBw6bOmXjEggCWCO-uaDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB-BnIn-s_1xGzAw7eo9i0gJuwasEBi41ksakUHutfce-LDTogvcSI-O0k_tSoPUWUeIDS8qadQaBPxLkn5jwejy_7xWPiyEdldpt5Xk2IXYiJUMtf11BqKsT_chGdH8m8BqsCgONReWI3QLh_6_SfFN8wv3OIRDnmMsUYfx7VdzARJ9qkW5HYCsgl7hexR-F2PjrSqEuo3I9TtxlWfV_q-peT7clLhJhuzlyRVKKE0HDs5Crgk0aSOArKK9E8dYt_Y7EsgS-3LwaMA4u6YXujQHE7mO282bNDz2VSLGPQivCiwV5SLGN0JkyvXIIaX1gRCT8IfCCZUP0pYj_2hQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IF8VQO2sp1CZq8QDw0Mn0jWjOYfXQfAe7uO6NgBocsvbmPp0U_hz35EJKH6ZG0stTJdyzMFj3Tnv9kN_f4df0qjuhufA08DRbcXnlMPTActSqdMq_YU2yym4pwe6GxNHce2Er1kTlVMcgsucb255dW1Bi8dGN8oU11N_vsbA0qzltK1mCOWeT9sM4-7Bg3PUIZ67F0Eqq2yXZkundh7Y4sLTKaozZl4qBRDo31efxLOXIauU7GD6wdAgw_vX1qTMUHfvS2TXY3PkJuZk1KbW53TGmBpy5uUCOUmoxxI_hP916GWCgcRcS2rKheDCuvyDWjJvTe9qAGCcV26986Q-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuPOsPr-8uD22nCqOkUobfGA1Vz12wbuMj6mItTU5ykRJ1EIwhS_ma88KQtF-I5p0Pay9bdy-nz2uz4-J7ocmWxrPDftmz-H66p3zdanZ2B4KrBAwaGemHJQjguLdOP9sTAeU6tiBb5ch1GOLc9M_kay3RIT9kVKFpmTsrhpmDRQiKqXmIhKrfetLU0kv9a5yi_Gmk6aXYt3wkVuGzPdjx0K2zlpeBmi3sQdKdWdgooE5ZAfJRcoW3wIAb_ilTeLe90b0E_OQnDuci37vjXgFvq8Ahi1zWwimnboH4jNXIUuCcUhQr6eBojoyEWXKltxT_59JRjZHeS94PR2KCXhbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Vun95Hs0muNKUyGXvnFiVclXLPlZu1uILcnxrPOA3VZHIZqfYi7VKQ1S0OzxYczdvA5L-XH-lebUBE0Mmly50ATe-Ev9ZeBoFzgPVGYoEOIbXN0vxKuLvZqlNK4sWoG4LGJszOULL9sdFDN1Bd3ywFT7EY23Z2mSwxlLILQOYlUt9irUMhdEt1707UdCzjabBmdHl9lU2MbGYNhUr35FtXcIBqxTqYQ8ILYYd3PCugvislDEPrKif1Lvc5aMSq0u2IxZQq_4e3B1gTBUmXJ0fUW0wXuBs1xAormfIGx_6HexnH8ZpVtteU_y3ZQFaOwx-NqEcIhyDDxKyBFK1TIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPBX1xEJQ59JZiUR0IjAejEvAEI0z_8vzQQ4dZJAdf40O0N-lICfUDUGcIUdLIFCjhWbgg3Na9fhJPtjBZo2-yvEvaf0fa6yFIVl3HxHLJl4WuTCgwPkheTHCdULY_qZD3Y5aQG8-7MzRb6dC8Cmu1H1aRDrHE5A3iEumMOLQ6m9ArjvnAlt5P8Q-_nh06hW03PxVtlTnF0hVFmoroEonEJY9BQmEmBl3bYLCBu96RtXWm0R3sZwFwZdfPR0C9pswqIPuVKwIhbO-7bRpmSyMH85djX9CrBn98_PLufS17KfEX3y8KC64EForKGWYPbtMvLyoD9AkQcs2kHhV9p-dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=L2OiSRv3xEEcFoIuvAIMepTcFPg48Hvj9uG-PaJC701iAHpWVdpQwQJoX6pPr_74F9JVR4MgiHKodw8A_WngjwY78jsxAjFwSS0ll3DZQQqBWfr7iOjhXcSO1jS1xD9fOY1-asHjeZ7FoTs4eF1L5mqPU6unoVuz-7g3Io4PkWwPjmUyroqmSc6xD0ldbVYg_w1CUjepgeFeVGhgSoF77o6mP4DmiGMd3-TAm5CMHeFXLBIQEs-HE4sdN7JBBPPBEG6Tno8MBaFDa_zMNb0N2o3JfjyCwwvxp3dcCm6yjzLTtsGebb2iVwL0_aK4Me__JLPhlRhezTe0bTpcibvYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=L2OiSRv3xEEcFoIuvAIMepTcFPg48Hvj9uG-PaJC701iAHpWVdpQwQJoX6pPr_74F9JVR4MgiHKodw8A_WngjwY78jsxAjFwSS0ll3DZQQqBWfr7iOjhXcSO1jS1xD9fOY1-asHjeZ7FoTs4eF1L5mqPU6unoVuz-7g3Io4PkWwPjmUyroqmSc6xD0ldbVYg_w1CUjepgeFeVGhgSoF77o6mP4DmiGMd3-TAm5CMHeFXLBIQEs-HE4sdN7JBBPPBEG6Tno8MBaFDa_zMNb0N2o3JfjyCwwvxp3dcCm6yjzLTtsGebb2iVwL0_aK4Me__JLPhlRhezTe0bTpcibvYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHyx-UQwO-kI05cRM5YqLTFi3km13vRpCFU9YTlZaq8gTLbDdzxySwwijttGYY71E32_rvXKYE7zXEyPCiEsMT2zIHrAxxO7w1zAp_4sJhYlJ9OnvLBNRTQuRvjPBpq3loRlxwYXMFR1VXeCYxy_TLPeJiGbRmwKGVoMLLdDMcdxnPcwhyD4E3uvGXix7UM_lWl47MBy5qoimoJzQ79uRRKnxcpZzGwiKlpEPLA1FzqOctlFVexYI9TpNqvgvyGWtO0d3oYNr_0IpyiAr9EBcZ5LXfxqHoxPZChkTU6MEYhnBgVtyBm2BKmd6Z94bHi1iKqwlwtiZGnssf3MEaW_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEIM9wzLfgZtuoZyFq_TctEm-mQe1bqoqH2vuM96yJiQAlGMp5QPSTvptsQQFd5ql1qL2wM-mfZURc8Yi900z2xcNozk0l_M8gfX272PMTUVtGnYWPaONVDlukUyM0iXHu9s9RYtzpAE-w2oJ6syVFRlL9VO9_yDC5kT7hBzgD2kX28kthc8su8ujImqX10IS73BmJturGKX1bUxT-dU1i35rbxOE9Uzia63AEB4_f4DTfC1F5FU0f_RjrhwxxAXhU5RcWLxuPl16DK3nF3Ve8tWAFT1sgDsaKBU4Um5gQm79KyIZfNNC2jJyT1it-TeU0UfLFWDY72w0tmDVKgwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYc23uccF12V43H0_0jOweb-6mDlaMDu831THNOI3HPS5IkcR4a1kgoiO45TGXZH1N5k874xj0yKGJmD8vXFDlDjkMxf_MS0fcIlOfRyPpS6zowZOItjGj2EEycuB83asiuugit4_FvdPJJgcuerR6XTSnFxch8HuqnuLnN-1G_3STMF-EQni-4joN4HE24yD-wkgkzirf2xeCbSfnSvZGCEkvrrWetFP0zUAIdlJXHm7Xl39dWyd8dcUowETNfqCPE7fVRiwStF4ZM7FGXySGNuLJGll02V2Vk2sUOuBzobn8Y_-7yVhewJNkxn1SI_74vhMquC9C1TsnlxcHbU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYp5fwRjP8chE-kWRPn11kio4SF5jRB4iE4OVmvZEHgTFjbq9DzttjKiKOjhFcQq6M-Y203lnIOAkuKVz_nuVGQDACO8hPjZpaTS8zY878wn3iXmesy-OXE4aix5XE668eRDrj9W0qw5h7qt0wjC9QgKpwx41V5HpQvd2plzljmzs2wk_9oTpoC2KltO-GdTuUBN_iLBS-5jQtI57-gcOpteNoMb6MgPw9l-VmARgc1oe_KjYfHoY7AQ5MQBX4Xxhdz3acz78p_QjPAkPa0dcpx3h63iKaDtG44D54D3ZufwYVLxl4_WjXrxclztKetnsiAIfPiP3VXyUdqh9m7nRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS8amzV6NVMH8oVwVD_FL6hXx-79hER8l021ue31diFrxhhcsnCybn3-vO92IU4cRQHTyTTQcoYcSyxXuX8braOTih0-b7z5_aLTb_pUkP_InbmsAOxFPPrYwRfnxfaCm6lN7HZIhRzqiWwEZTp8da6D5MudGvXROQHjkbRplOC3xdcTLiCTFJihSyAfp4cTGtANE4Y-iMpz5zfjMmUv4XY8TX5b3Qci6pQUFzxclebItkw4crSam8HM4yhU0pMYYujpUTkqOKZm7t4hwBe3nPICrVUyTZXJxx5rmMD_pENX3YwK9VDVP6-A3Z4nMSovbgKyi3s_ngvc7jDVCESdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY5HT6FSoBQHQizqpLjzDONwoaKoBEQaQXJcxY3wVn8QMSSvyH1ObmRuaJ8TTaSC2PtZSTiScrdzZupCPvrZmwQzcUoBwmCQ3RSG5S4sdGDE41CYlwUjFgZ67AR1RmVjtdtU7LTQReNyawzgS9h3-i28ffxgfwGUMmCtpI9JoZxgRkv7CuvRNm1X0kqJMR5mgGQ6lQXw9CeBFLkGH6J_uL8DjV8tvsN53byxLcSQYZgBof5MhqT00NcLAZVJNYyh0Sk-MRiJpXWzy-WaLIM8yhxzota3U64SNQlvE_obTqAF6opo2I9RkYsprHHElpct2szo23xgua9M92Oajm7qAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6_2TT3wN6GvpOZN_Rdq32jwmpobyH7Dy5bF4a7gxA80yTlpIHMlZ1ly7wNO8MQXK7x4rUZkTfkuuJ3mwCnBidkzRnOCmGJwEJg1G5vGWfkGOTtYSFZ6ZerW-dkcbyefow3ozBwbzIEVP2QP3vZ-MYR4jNho6T9UZ0Mn21G6j-d1abxIbRXmExfzvrua-W6G1xbo4H8eXoxbwrH1fT7vKNRo4isZQdB2DRGqmJl7CBMs9mhjHcnugV_7M96YRDHo7xTKDswCxuvk_fQCHDjmRfvA_Pj5v6pKB5Rf9K4rWVilskhrVMJTdyziXBxjop2hXUKYh5IaJ4jSwP_IS155Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glLiba5bIE5jNru7YE8l5b0tAbGuu2PeRB6wxKf0s0MAXzjUai8Hnv8A_5YFWHmBiq_NGeZ5ahd7Hi62zSuSiPNhuf--PGY3J_lhbDpGnrtzUm_YIlUo12ZTBGZJ6818yXh9ojbh0Q3mnU4nuCEmgpOuAAwUV1YmysMlv_dRfDYDgH58QyFanYfI9-rsF9lxZuaw2y39HgMOJV3tfEkucRf99NhxJSek_NHd7jt1dGqCKaYdu7fFHp_IqTaZTMrajQ0pZ3W8K7T7DF1CoZqr1fKTZYfovpD6SwEtqVQTfJ7_uy3cNAXZ4D35ozJP09I4ZMcV9iNxBZBfrgIW7TA7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=eezFbQM1uDZ5PW0PzbBZ7dIDEHFZArFoMTTYVkT65FLT_vFHPOrtAqvdge-3wOimWH26-DozNNyo5WMmc-EjSOAmt1js0q3jNjzqMetN_9wGcRLAU0NcG_74dLiX0ar3D7u-tWFeLFI-Lzwr9HA1sWYRxIv3g1F2bPdD4Xzk_NmwkLi7H3VJ0-7kc0DyGm_zSOJC4H2fSaZSqrqTXNSpvA5t09lWJZFAq2p8Hxu8ZPmisAxRa8exJm1is_eJ_DtpChM71oTqH2yqRUHnKQUSrZ-LbBifq2ND4zMyxCWZ-R1Uexdq1kocZ96VQDUNagH0Loc4YN1JH6vQI-sIu47Ovg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=eezFbQM1uDZ5PW0PzbBZ7dIDEHFZArFoMTTYVkT65FLT_vFHPOrtAqvdge-3wOimWH26-DozNNyo5WMmc-EjSOAmt1js0q3jNjzqMetN_9wGcRLAU0NcG_74dLiX0ar3D7u-tWFeLFI-Lzwr9HA1sWYRxIv3g1F2bPdD4Xzk_NmwkLi7H3VJ0-7kc0DyGm_zSOJC4H2fSaZSqrqTXNSpvA5t09lWJZFAq2p8Hxu8ZPmisAxRa8exJm1is_eJ_DtpChM71oTqH2yqRUHnKQUSrZ-LbBifq2ND4zMyxCWZ-R1Uexdq1kocZ96VQDUNagH0Loc4YN1JH6vQI-sIu47Ovg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzPKBZ4MzrnxYLicOql5WSo6WzXhKoR9vXTrF3bfsMtIh0ghG7CZHi3QY2L9Wki-lzoCU5azF7x5TWGkoXxlGf0SQNKTJbRxezN8C_VllNfDfm6BE-NmU1uatyVsxFxhtY8EzTn-Gj98GRi_3kWw1iHBTrob8nJsnrzpgGLEvgcSThBrKeVawa8XAVrLxiCQqu3bFFiiTWVB_OgKuEGfBRUSHp_jfUDVqEgRjckToZRH4WH7xGB5s5U4I6OaOTmTSqhzR56Qtpm8jmdPp_sXQ3KDacJyMawyRprXb4EzihONon6RKVPG7bnthtgA3s62HdV8qntbLi8sQJilhDt9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=ooeaWwijlNG0-iNHj7Tlj0184pPpo8grahSlyKus7U8_i2wmxbpSrh0PulUKOuRArcQh7dFC-MqOV0V0xZcTsCuVtNnCEQQi6n7jM1LjDcMR7wwabY70N-iCQ17dNTpACuZGxOICHN8evb3LPM0YPRMqO1Q6Zj-0CJ_kZ2v2kil4otI58KMjfHxGTqZbxkuQ3TmDgiljy17opNEqOC0-sCz5g8WuQkReuElxG3ojuHnamGRmZT1-C4jwxSLRhTR_LlefW8S_abOUAb-vEYU4TcLdfLQtvuZAmT-B2shjqtTON7Vi_Vh8isJxkL87sG7-pDz85JbwiYs3tRhhedQSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=ooeaWwijlNG0-iNHj7Tlj0184pPpo8grahSlyKus7U8_i2wmxbpSrh0PulUKOuRArcQh7dFC-MqOV0V0xZcTsCuVtNnCEQQi6n7jM1LjDcMR7wwabY70N-iCQ17dNTpACuZGxOICHN8evb3LPM0YPRMqO1Q6Zj-0CJ_kZ2v2kil4otI58KMjfHxGTqZbxkuQ3TmDgiljy17opNEqOC0-sCz5g8WuQkReuElxG3ojuHnamGRmZT1-C4jwxSLRhTR_LlefW8S_abOUAb-vEYU4TcLdfLQtvuZAmT-B2shjqtTON7Vi_Vh8isJxkL87sG7-pDz85JbwiYs3tRhhedQSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=uf73noIvBqpRbENinBpoXCr1paMHi7fadUR48VTLU-h3oZx8ltJxSc0MILtyvmxin8-PqV6QP8LUljqrGd-qWFrF8Gkx3LctW90CyJIMQvKzJ3hT978zOgfjNNJAWzf7IdjooCS-ho25TdPEa8sp2afRTHsIRtroWuT0PhsRUUXwrGIrnPQJjW8ew9xbSzrZLdxVArU2HUSf2EqTlNNzuCFmfvw75DpVaXbdV4RaZBSg4RW4D0jlLJO_MdB8Xo8e_6_SVXEobUE6D6AaPwK-JfEzjPz9Z5u-qEfagvPDjwS9nSddkbilMw-h0q7olzOSYkea5BOO9-GJ8iyTQncSpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=uf73noIvBqpRbENinBpoXCr1paMHi7fadUR48VTLU-h3oZx8ltJxSc0MILtyvmxin8-PqV6QP8LUljqrGd-qWFrF8Gkx3LctW90CyJIMQvKzJ3hT978zOgfjNNJAWzf7IdjooCS-ho25TdPEa8sp2afRTHsIRtroWuT0PhsRUUXwrGIrnPQJjW8ew9xbSzrZLdxVArU2HUSf2EqTlNNzuCFmfvw75DpVaXbdV4RaZBSg4RW4D0jlLJO_MdB8Xo8e_6_SVXEobUE6D6AaPwK-JfEzjPz9Z5u-qEfagvPDjwS9nSddkbilMw-h0q7olzOSYkea5BOO9-GJ8iyTQncSpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=YnJEbYNGcaOLX0co-P_BnEazsoXaUCntBlLSEkG1zCEWfNQrD1WL-m0SXEArvyuJVV871KiMGLI-zA1BpQl5rKuPT9j4EK8fPRmKozhx5c_rfgXF9Rg7uclp4lyOCUArlhBTSlzmIdq9-CPinHUU-fV8YJL0sm1GQdfKd8dcWX4kq-hBKUxl5ILlC45_oDFVsf64eoy7Gx_O3gN2ffM6s_DUOEhBToW3-c5cbSQPQ64w44Gac05Hr0EOqbix3shCT83zkcuRXpwSX9CM8wmIBM8QUy2JOfiZStVpduFA90T2p-H6fdJW2j3yWP6QbEOAiSCZ6jIa4XjqHot-EChqtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=YnJEbYNGcaOLX0co-P_BnEazsoXaUCntBlLSEkG1zCEWfNQrD1WL-m0SXEArvyuJVV871KiMGLI-zA1BpQl5rKuPT9j4EK8fPRmKozhx5c_rfgXF9Rg7uclp4lyOCUArlhBTSlzmIdq9-CPinHUU-fV8YJL0sm1GQdfKd8dcWX4kq-hBKUxl5ILlC45_oDFVsf64eoy7Gx_O3gN2ffM6s_DUOEhBToW3-c5cbSQPQ64w44Gac05Hr0EOqbix3shCT83zkcuRXpwSX9CM8wmIBM8QUy2JOfiZStVpduFA90T2p-H6fdJW2j3yWP6QbEOAiSCZ6jIa4XjqHot-EChqtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYHcTBVHpCH1R8Yp-dB6gJaF5V1rCq8WgMwdBi6pkUTxeiHUVs1sy9ySLpzHH2QacCMF8_i8xSohEbkg7vDqt5bfYBnr_xBijLlGmo9TUlEww0HXsCZ5Lr1vkbrwrkp7JaZ0d4rMvb3yPmHioAR8lONZLwKz2HYR_6wtqchE2jueuinKoKRB3IGYYpi7iBEJTopX92RoImAZZfgyfjWQlxGgmXyeuJKdDnZfYm-EsmUEV4ZqCMujeMzGwFK-1Vkde18DL5_3LuOTYpWOJhapogZ15hTU0-pLcZsRI3EqgRX-D3Or5DnBaJgRRzkl5vYDuUgE821J6FbnuA3xEv8ZMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw17njbKK03FZ6Mz1Jge0r0HR93gFrhw4IH5so1-sI1flwWiixqbBJf7_NzykUHJoMFeQe6h6ltYSEzikbxbeiZLzAcUEKnj_1Bj6-ckCC_a4ezNpgTRG69LURV_d3-C5nVzzkElDnOkARzml268L5a5EFMV_qK3QBT_LH1Z1M68xLnzXlLWNFXiE6C4Ku3-hG1e3vd4I5pAKSGdbKdTzqyk5dNwTjYJodIlxlwF2aYgLv0xWMTpqvyPuZr0EbgjGg-9kwoFp2qruDDdsTWC9Jo96KuDxXn9wbqtsIQCXegT_GEcy9r7FZTrGnUyQB2qet6tu4dKSebpvxc2Vpq7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMrPC27nsQsHL2gMjKZGiFTRkxj3z7_9Ry7kuOCvyPm2fOLcRuoxWGmJA2l5MvIF_dRQPZ13nOzX4ae5O_m5sgf0hWBqRRRrqit_S9uSQMRBHgBy1A4MSd_D45K-s68fTO3hwfGXvYMOmk2W9RKSTIUcWq5uurphhpWMMTvPKWEYP5hwSrWshlf9W_WjioCxtO0m-Lt1g8h_YeCfIzFtaEV_y-KgjtJsuDOf1ljVJWr6fV8gyTOewcSYDf0SGEHX_xIht03a_eidBzw1SkuBpqcUjJ6AvuWJRKMaXebUahosKQK1zDzwarS7OKN0_nqNjt2VhcpVesXTFQkMDh6IMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXKSZaY_s12TYHtG-1K61hz1oZa0T_pSuHAeqwq5wMB_Du2jYuq4IEfsw5CEHKMf2qU45r4bh-QEa2IkrPO6P2582mLwy0nz8iPYE894a27YoVTeP2da2HBJ2ovehVx5-bx-KAckzntlPBF_7OQIl3VYmC1C_NhWt-rJWj74jo2x0Sf3NVhUfBEjjFOa2kkdgm6Np8ljOb46_P39N1mX8OXvqmzo2wr5oebm2meqwjLYpytpOy1334VKHugPmQooZUwMqOWVZ5lLs-627IiXR4dz4mTGQVJZzWx3BJNMMbaL8kvqt9-2kMjjvm7EYa74P7u5qdW-zIucOeB_8zlUzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=IkHSmC-YZb5ujkz4R9rfobmEuJfUVCNF8wqME3n0gsxsExjfmTe4Skm51YKOD75jgOV7-CnT9maVLpSwNo-ZCGuWMIkDNOSKp1PTfwUOw09wUMyGzE-9l8YZmgilskxWOuCYCkBrZYbnzWt2mRDUv3UaWUA7hVz2VMsJnbOo9aF8dPq-YQ7XrukLRRdd7v4zvIymY9Wbcv-5WXp39PNZVEXu554cQ3d3yOpOle4oejBoiQgOlitAGT38HSesta_mL8Mf_QixbN_U6c7i7M3hXBPmPNL9huWKAZd0cUNH5cHVELwcjK4QlHgji357PL80RfThx851Ndb6NeKYVFOoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=IkHSmC-YZb5ujkz4R9rfobmEuJfUVCNF8wqME3n0gsxsExjfmTe4Skm51YKOD75jgOV7-CnT9maVLpSwNo-ZCGuWMIkDNOSKp1PTfwUOw09wUMyGzE-9l8YZmgilskxWOuCYCkBrZYbnzWt2mRDUv3UaWUA7hVz2VMsJnbOo9aF8dPq-YQ7XrukLRRdd7v4zvIymY9Wbcv-5WXp39PNZVEXu554cQ3d3yOpOle4oejBoiQgOlitAGT38HSesta_mL8Mf_QixbN_U6c7i7M3hXBPmPNL9huWKAZd0cUNH5cHVELwcjK4QlHgji357PL80RfThx851Ndb6NeKYVFOoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCBs93O3lmxRcAkxN2-YvsrHxiu5K00sQXh83kaZnjljYO7y_NvzhCzV7EcYfq3-4zVdkg3CW6q7rjv_qraz-zFRLaKYaHee6q4ZfV9sL9h7kwOu2oL25Vw6ZsRDK42cA5xrFurshbefEygKroxcBc0ay6Hsk1ugEoYFOv3KQg3X_VSCdUw8BnXUrpTMDb0RGaF89XqtPATu9KBLEksV-Y2UALXPyDTslmKQhqdUqjPRr204Ify4LrTbVRFvWkcXOB4SoK-ygqz6jxlFQxx_dC656-YB_YN5VVBJobq8hfCHt0PGUgc6osxtAMt7pRXFHY9UPYA1wBDKHrjbQtmArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nENNMeXr5FtaUn6ascNegk8ql4QNvBZcQarzJiQXICpFfly95cXUJfWGnJypZgOmjvvL3BSblb3rCKaBZiYQv_bFIXwrxZ9Qh--Kv7kf04HVynErg8ynicnBTVkUKflC_22TPD8FVcnzzbMNHzzpm2wtv6bd-bvQN21JH27spGcVhH_HVHDsv3FHBlGnIX89v7Q_iVdF-J3YYRVXA1IP7XjCQq2WIqk0yjPie2_uQN0dbavyqW7E0Fp4yLx0Vhzq6msHbrq48ge-P-eucGcXjKbEEtj7wYgX0WI17Y-kPnxWDtyuq-7Ya7STKDVBsXVC075PSWHTWvwBTRzt_ujaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJWz2eDeDYg05ywxWu20-a6b9HvXlerqwz2C5xT8cvpPRMa6LIiiSC4tvVEvvgFYauMX5J1oTTAYk6VfAkBXv6-P2akrJrhjJpuxmkQdwdXWe62GxDaKsZQePoRgAcs8oTIAo-RYxkaHGGHY3YY_Tq1NJQuRdyKAxyDbA8MK8uoVI035fc4P7Vx313TTSenEC7wZ9LGL64egbiPoC0Dzoht1iD-aT7DyjyzN31CN0r9a5nxV5h_CHz6lvkIx2DRHUQkJ1MWODzimCS9tq8NQdQvfoHRjKUh63jc3hbMzyvRkSQ4a9pjUN2GUSHQcj9aZ9tR0RD3ujJOU5UlTq8SLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph3NGIW-AHylkwhUm6PXOf2b0rGNGLEqoiNB28Qg0I1ZUNnNzFNixKYlNuO-L0IL7_OhR9Yz0olmOjSuzDTTC41CIemu-ljbhL5sOmTx3-I9q6E4jwXwHKAX50MxKhEs8agplRB2zsRRSrcYy7xlrFvlDC_LB5ktExpIqdp1z0ebowRDJDs8oRzPdDIY7dpLVM1waLSsW1OO9FehOVhA9tWm4wvS0v93nEnVL5tB_FupB5bIIfeeoLqK0RIGmX_Ka4Vn9yV5_q-bN2LQVCUirPdbt_cgaiIt-lq734WmewX_DPAGCSblDLXvAZNnPdy23lzwWXvgPQsV4PK86h8sTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2Xgxl_bkZCX9ruDXSGoHACTjNznIfck_v3QHRC_T_fEPCW78MMcExP0RWkZjxD-m_2CRdjbghtNVr21S6CI11JkznGUIAtbnKqp3VqYmr0blZ3ROaKsPnu-KaKJ2_UhW2-uZV3Pi8yWljM612FN2-TeL-D2G8-okbk9t0Y2lIcQR2cwxZ6F6df33UZIg3QXe_0hX0ngvzkjafTYd-Go-YghQwqBw0AHMyEQ17JjrpBAg9o-00kgLLNhcrhhiZb0UX2-BWPH1YZFuK-Zns6Y9lzB_EwgPPBwMzc7WLsjyloBGPuZbkV5Dh3Lmonfkp1LbQ5tynF8tsvU8Ns3EXkcIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrvTP4-hGlPCMOSAzk-NzWlSl33zeXSWxS1i4M6S44BgU5mLrQ2O2jQJla65nnxXY23Lk6f6Ogwp2ykbdhyHIgj3fh4zJmnj06TLXfVwRi4PqTtY7cPUk3YiYD2n0tvEcKIeaWLs-QXn8OGZMYZmz9rnyK2tALCxgye0oLvLS768ekhKGJ7HbvIlRyPOfVLIRudd_QYUPWgK0E_d3Qi_vdO4x7atah5y1n0FfTXIqsctKjVg1EuJlD1jRL0IBeG8dJFDgZuMnlA45XNg9hdAEh8mKhdXHL8Qy6XoEApYS1KMSr5P4l-oUJoqC6G67zvucYrcNBUabCFiDnTdYvkdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=deZHt22D7B7nwEfAMMsltdM-pCOsEq7q0UUlzyRh6xpdeao1cTYbd4NCxPaVoyLOGW8UwXiZMYpgclOnmBzA3F3t1gcvYEYDTW1td0qr1Gm-BmmaboROromE0Say9HjFdV4JRP0Z-4UjGo6KTO5AYMMeTCLg85EdPOj0XBv1H46es7koqk_IB11hrIVTiGxGYrP78Qz7WODgoVGUklNOZJi4RdE5ke8394mrhZnoDHZ8ek50zYiWV61BkYKHyQrpjD1jtmurvjPJbU1uvRCA8HagKVGpwNCuxE_2f8q7qcp57c0j_QJ0Inx_RaaM31YC1F7-VmyupjdWq9WvQGnVoWBFUH1Zu56LtHcDEGiftFyfNHJPQNTczCbzbw0W8PO-ptt4gf1scfly9eP3QENMSIOeZ-GuQ-AfBhObUAZgBgFfsmBzXLTymQoSXCJz0d5P9ArIQ1tGBXb_JlJ2JjH3NJ7-uIS0Vr-UbizFhpfEgQbRJ1eyClrdZwUDTtcqSwfsky_O304dBX8bd6BMnGAKpHtBq-Nz85i36teeM5OEb1dtXwCt7ONMolilddtf7uEKhYv0HO9KFGhkaf79d7e1RD81tggkFaCa97jnrEloIQvuMq7vHY9VaSsboEYdAkiEiMXGUdkV9OOuyfHJyrTbjJWbQ_xnD68h4O48VWEVEok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=deZHt22D7B7nwEfAMMsltdM-pCOsEq7q0UUlzyRh6xpdeao1cTYbd4NCxPaVoyLOGW8UwXiZMYpgclOnmBzA3F3t1gcvYEYDTW1td0qr1Gm-BmmaboROromE0Say9HjFdV4JRP0Z-4UjGo6KTO5AYMMeTCLg85EdPOj0XBv1H46es7koqk_IB11hrIVTiGxGYrP78Qz7WODgoVGUklNOZJi4RdE5ke8394mrhZnoDHZ8ek50zYiWV61BkYKHyQrpjD1jtmurvjPJbU1uvRCA8HagKVGpwNCuxE_2f8q7qcp57c0j_QJ0Inx_RaaM31YC1F7-VmyupjdWq9WvQGnVoWBFUH1Zu56LtHcDEGiftFyfNHJPQNTczCbzbw0W8PO-ptt4gf1scfly9eP3QENMSIOeZ-GuQ-AfBhObUAZgBgFfsmBzXLTymQoSXCJz0d5P9ArIQ1tGBXb_JlJ2JjH3NJ7-uIS0Vr-UbizFhpfEgQbRJ1eyClrdZwUDTtcqSwfsky_O304dBX8bd6BMnGAKpHtBq-Nz85i36teeM5OEb1dtXwCt7ONMolilddtf7uEKhYv0HO9KFGhkaf79d7e1RD81tggkFaCa97jnrEloIQvuMq7vHY9VaSsboEYdAkiEiMXGUdkV9OOuyfHJyrTbjJWbQ_xnD68h4O48VWEVEok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=GiqaEPAQvpIqlzLmcXbc-pISmWYUvcodP9n52lbA0yC9IcBGgAb28uWehno-QaLjBt32nPKplVQeFzAWNNdn6ouY7VwPPulqeabT1vTxtG9RcxpSRpA49gIRS1jvNXEwYwlEFe3if5SvqCWZQC-9gThtLc7H_u3xlGr_G7SSqRf6HymNqlZHNW05DRrtvZzGCzLI2VHCotwuo_tKMrBKPGFmY1OgHefWdd-rTm56QYf5prwCq-wABon40coUhw-ghH2ZVZo9I0yp9VlleRpAh0YHBBkKazR85rX1LVMG9cfuS0QngGRu-Bv4avpsSP5yjq9vTmU_pmTC6Q-GKUPYjDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=GiqaEPAQvpIqlzLmcXbc-pISmWYUvcodP9n52lbA0yC9IcBGgAb28uWehno-QaLjBt32nPKplVQeFzAWNNdn6ouY7VwPPulqeabT1vTxtG9RcxpSRpA49gIRS1jvNXEwYwlEFe3if5SvqCWZQC-9gThtLc7H_u3xlGr_G7SSqRf6HymNqlZHNW05DRrtvZzGCzLI2VHCotwuo_tKMrBKPGFmY1OgHefWdd-rTm56QYf5prwCq-wABon40coUhw-ghH2ZVZo9I0yp9VlleRpAh0YHBBkKazR85rX1LVMG9cfuS0QngGRu-Bv4avpsSP5yjq9vTmU_pmTC6Q-GKUPYjDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl3z3jSKUqeGBv722NFIo2keZPxjlsy7uU10a_FDnnGkfdZPmUgZq8ILsGCbrtJk_qK5px3WSnYFEHNqMWYCPclf_x-MPe-PFXQGo_moxgJR_b2rJPsxoFt1iytYn-VPCQE6X1vpP7CsAz8LXqI3e1H2q-xcdDJMxhb0S9J7QjPkapRbjGSPx_l9GUv37khRboT_uY9JDXUFTQd_siz3kB3dVVZrkmsoh28uDYz-Mxh-LZhG0ux_vLLudzU9mezy1OsTMjVfyqn70otQdIM3gmyQ1QcNsDf4USE4v2AOYKLBjiHTzU6o1gjGy5Vyn5ePGV3xT4lMqs6FxmF8wUeGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tESupggNwsXe-0ce-kpmhCXAOi1tkpGoGhLRN2dj6W_waZw0b3ZNTjxNyiDh1q2J45EIpRtn3-fcoVPexYWwNsJsrTMlfmYwITib6b9RDBxE4WPSLRlvo5j_OT3jax6er_RlJWHwOh0Lp3KOFvOOfOqv_pbuzJ4xa2I3Jf_RLR7g7CUzQTqbOcJEkh4r3ub_nxLKPBMUL5VlSu9sAn0t7EZTO7FmvVppai4wrBVK-MOM5I_b1D1U6Vfx28H-L9Q3QJmI6tuXl2xWya4DwWjDhlJszyXQ2O2ClMxpZc0nBfYOpljKKrqTVcZ_bn0TQe4EeOqz8AyCnqx9ctLLlGZZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm_fgtPfXp1wDGuSxQzIYfRllDCcx9r5HnE89DRrwHcDCvkD-rMF3XlwX4W5wQAx2jL0aH2KAIYGVY6X8qxCQoEZBqkDPRUXzmbythDTG6MT1XjCNINvN8-i14NMwAysUnn3VyyZRZ-qxAaO-1Joil9qmYTLgAyxJw0VpfCwaP7-gqqovZnWukGkACaWsQ3-IM73DPSMEMsF3zuX3muJ9riKXr_KhIeRSWsdKLPt5XyAaj_d5B3A7_SVCR3kCAkTCcfx0f_nR4lYzluehQ0azADc6hBbvAKX4bewqubP39E1aPzLy4P15qqKRm5rV6OQSwVFrCejLR90jNyIHnafJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3U3l66M7A1i-MdW7J7JVtNkA26aC8ByCCMvyQgZDcypAX_lzfOwawTGGMR_nO5YbIiYzvCVWch8PzgXuaVzfCfUPddf1628oYo-JtnCAK6cw7PRvh4xIHc4LvtxcS6-i8Xy85iiS2EgjeFrsqONoMGELHXPfwY0Q9SMN4s9UMVcxoE-b0fkDCZvpOPEvkEH8QVpE2cj3hXivCf7lHE_Vpea9L8E_I3sQxooDZKCRQFrEsHjpM4Hu2YkHG0IaTaPexW_ToEc8p9LwyYkw3IkDC05_-jAwhop9DUOKxQOLhywc5z7YzK_P1_GmCE8OQvDt4pH9Ego9e7MsL7RslJn3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmsYOIdwumHMAa75KaBhC43Wphl03TYOR6ddgyqeRpYcMdwHH90FX_jnHpnjFmzu-BXsee_1AtRBKbV7dq8qMUX4rRpLmfJMXytQkZi4ns9ts9yWDzI7G1wcO3sG_2zNmPVnPzGZWTJY0lYH9hNDNwGNfzCNVmQU5vnc69A0big3srseHU8hRVDwbPqJSVga-ibz-WM4IpgS4JpvXz1kcyz3CMr2cCkSMn1_H0TkNO-2mJYyHi9CMFst4q_BoWQnmmwmTIQS6llTfmgq9TpKPdenlXQpJuCQTMozWMSYQERUOympPYUHUpWsZbqCBuenbiYSwmcZBMPuzixu4VDR6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NICmUtKMw5JKOY4g1Loz9qyxtixlY7JFgEOV9dmJbkurkVbD1S4sttWIsU9P7kG8sNWYhHiDt3oDIQIO-7G_AZELzOXkDAySZyXiXgonHxzQ8uzrPXKl-7rDN4OV4xYeTdZIO7L9bViRtU_R72v_PkAMEEcozsFnScFIdIfx-C-LzPsbEVImcUG9qtMksfQfdGx-0TUcZT0psHj7M4m3Ut0nkSjuQP1WSx0qoKe2GpvmxcQrJ2ln_lkIjpN1FM80De953m6CCbMs8TxEec_j8Kh2bDGVY1KkvaZQL2SWVBriCMgqugZ3-AXiYs1ny5caJIvC5uavdfcECmebXt_G9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M16I6H2MwS8-VkQ61Lx4sjWe6U8q2UftwfyCEbNlJgStV4i74xI0RpuanI-SH0n4uLe1sH4fntj8jExZE0F7X-VbIYiOgzC6CBZEulGpDwsCTz71pM6xB-nNVQxrXvSJrHTdnvg0Ju6C5Gct9-n5qRW0_xiVrsTM4r-lrMKaI5ZllBKHA0YTN4tRAyIH91jTRCz63JcgOZGvGLHyO1WUoM05HOqnRhKBj_QF91weCD-IMwpdXGiq0-7M3_oXE9U2cKVoiXXGjJzMIE3gHmzoqMi5V2cQStEWSMOtTNV0eNIH3KgUe9FR7w2CcseZHVjcL2NHrsn5n7DI2iFYuFt3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZ270df41xaVXTJ0NAxj_wWl6vN3Uwk2EZ_Kh5tgpppYs9M5E3u1sXiJQkIXEpjTmLxzt4vrtVQE7vMBQfQITXVeoatyIYVFftRU03mk7D-2QG6D08iuI2y19dLoJLvKKRtYpWI1S1ZhaI7-0njseH4sUFA6mL3XIkUnvp9JQ5Ugspq2bLFN6Yb50T11m1q_1PSbY1LV7rWbZYbq2cKanvWXqy8H_VwQxllEQ9mVjrcJfCGUkM3OEVs5qnKjH4RmbVFNOZliFOJ82WvfcYLrFaVQrJm8QPZh8aNkWoWo7pHJB_XgLyzqV9MwHF5QSrtESbV2D-ztxTtNWw2cE_m6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR2bCbGyLJFMSbFuJFLpm7jiJano1O2Gm8N2BGrRWbLQ7BQiqv4ZXQRNFJYhYVTaut9uR2eeQOU9kJBScSXKXqBxfC2vBc86F4nWsqYzEFoPugEUAaM_AY-brS3j0r_rOkufOVMX-N_aFxImPXn2yAWr2DncVPkm8YdhjRntPtjB9pMYhcdaxtaORinxs3ZtBehQ_xmKvEv5aOvj4_cQd0ljETZkGriSr8IW-o_Qagq-l25Lh5tZKx37gdeG9ynklxXERz3ETvuFTcgKu5-kBPXEvd7nlHTHJZlcBf15juiu9HM9C2rYIkLwIoDve1WhciaFo5XPHf_3Ga0CVO04fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVTEFZzhfRYQlB4laICjqG0kQPEXisDFwxUEsJXFC6uph3VE7PX06dorA0dsiwg6MnES3trE55geRJ9wBRmoipATYdZT1tHP3r3V6wzgujAX1Hw5ZlnpIp91KcnJg1pKen5SfzFiKIGJVDVNUbAEBuaUOzCaf1t_WQlesBT3Dt8_xcFKz5FHeWLR-soqe3bEKS43sTz_u-ob-WYT_5FOgdtoPHETJ4eIQ2KCmUiIjvv7dysxGRRCj11wZ9QsEN6rL9rYjVxbptckCSn-ZtBLO_FEbjJsBg9yN26VluW9oleJfS9df2ZEl8jjaK_Kl6GFyiyIpamb-iaWcL8vqbpZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXRzfb1xAHqm7tzqhk-RjwhNd-p76c6UtFhiE8nW2RvOzIS7Ho8i0974t-rtWRp4gSbwuROABQqYFlGYud30kJPBB1xhyebS14miHdAyhX-5pjTTbal8WFsv2WZq23fXo54mpk3Ilc55FXLGu2FfqmoUOpiu2U5yCBofa9qLCdZhPHW57h_JHnw_ZcLNIwv7FdWlJwehTNckKXR3KdHt5iptD4I67ftp8MOwC941I18-MAqHB0SDKtObYAFA-C-7ND8l9vsKBqyK2JD7JEKG3QaRkxs0nM7lCGImDSdJWqHW5wTjjU7NyzlodIiVmpUYGZBLET8zGqfL0UtyIz18Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlledcEpBwBGqH0Ev3HhQ4p2LY0LeWEN7dxpO8zJvsVRHJhkPhn0WaqmMkefWUvu9IddaIwMH8GDNdMfP0-lv5vd84E_VaBSl3rnC6n8TaJNb1TJfhrbDb4cMit4vRa7Is3d7FFqYVVhatACO85Nt9cnzH8Y14NAvVd5ZZzYl5yV4zaqgdvFzlNBTqvSgZyOf-Me5laOIl9gKj4IgK4U_ODVvTBZtTz2ropO9r1cq8zeoeZfkAMUYBixW4CVOdxEfF9J8zf51pfhB7xVaKEYpzFYG-NT3timycnxis36kd6_KzI-VulIN_n8CHPBn3HlmVQVETy4gS6RqeS2HOnmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTrOWXQ7IxGItwFtup_wftUYKZ3RSv5Clutd6qXrN18-N6hNMG_d8STdy-HZPEF1Mn7w_xKRpaANUkxzMenApgtNHmY09Bht60xJic_GpqpLe5MXvmQSD0-pqVI_Uy2XI6ICm3YDXzS3U5e55Iyg2VMwQ9ZFWgX7B6v8vnyBcVNQALG97ZKSw33u_wCccLGkBoL8JbpDJ7aDPfNtAQPFVRMkzHh7py_TfgUHR7ojKUDlGKu5yoJ0_me0xLCf14rwj8i1n7TCAee_zwx6H-Qc6ItRaiS5UumNIrAQ34l_gY7_zbttb2ScbAGSD_yE5QjTxtaaeTfNVAw5Mp6WKoKabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUO1K1lKTpwReFZhUVZ9VR1UqOYdWKSRSwCqShZifaYSwG4yf8spTkIqRdaGVhe2n38IEqeISrz9yIfxdevtZpMaHPjdGeb9NTYOfgzYFj9XvUGF24lOf_4P6tXTl0YN0iY1E5lGWzH9ceOGYupAJq-swh2jyAmiMqbaYACNHXfxegO7VX0agZ70Pg_3DnejfDDasMNK5kFX9gCxvi_hWmxFRXPhd1iDNKC__EseRJNuHp_EbyAPNOrwnzBZjd7ypLY3-Ncs_OEDXCdWn3TSOB4z9WOp8_l8KXGaUB3eYbCCpFP9WQ4vvZyEhuxD4A24-jikC7yuQwNavrlRCBq7hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqL6ncOn7aW4f8AM03dUOmYK3Uxqd-STWeVOKY-dvOPuAzE5HrQ5CzybUGvH6nuEwqhf_RQ6ViPPwuPFhya39WftQWHH-uN_m7aCSYZa2MZp_mpHYFNsWBQ4xof5pzJ0EOLbKnPJpNRkFow9XSHXzS82sLCejJEsFiixOS4_7PQsnafcB80nlkM0dIV8y1ZPH5MIXw_gScD34AeH4nv-B3U7wmo_HTUgMuuvuKyrn30q7LsAsZMcSpcwxA4_gK8HcTQppiW4hn9aQzU-a_pbmVOBzyJp84X5ckYcXM6JEPWYA3I0R9JKnMJR4NJOvSdA7XMhPdQQNZV-SD7clHpMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1f5FBsSWvKVDJrA39RX2K4DUmMzM2NjycHw1qBlx5ghdd5YmM4n6nO75ytsSk05F8L3QMOZ05-w09RGJ8DnlAzIZYweo22n8oyMhVscQPTlesOfde5KiXdIZBR3G-aO0ZmCIBI0Wm2MK7oNqsCir_O3c7errmPl3kvPTzUGLzEvKVB_qf1vtd1_fb6FQ_1sdrXLbDsgG_VcZxYHSx6vno4AablYocUUBFZp8mHdyLjcoUvlcA6BT3U0dAQjNrrLXoibbXGM5YJ_niZxsp4pidwWnnb9u4S_SJyrwpheuSuGE6-l3KhGCvc07rZFX_k7RxRwwJ5oWsESBj-xdq4pOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=vRhjfM3N1wGXmYKY4PttYyvFno-CVyK1Igr3ey2nazt3VH6nMFmzEhhinbRAKjyaBmuJcwHbrIOcG8iNqZlepTxYWvrze_HcLbe8xxOpwO43wmEvJcTHsL34x15NivE0zfxZo6dwpdiTOQsm7hEd4wxVZR2Q3a0biwAQToyi0HRACjcn8-VDmerw287SokpFEUgkqkpd8fpMGkHAcK3qY8yj6xrowvlus9aswczOkCcNR84XCGkbOV-e11jAiJEQK5TSojdDbqw9tJ4N4XcoQDslsoJDh8ndIai6U2gNk24yzSNjOd7I4cFZMc0CCVKRsTWsDxD_mIpWjHwn9gXeDEQLuCF3mYD6rOjWBAKiTeg8_M5_wVWDSlrorZ7qRXEjtLgM0WWCG2uJRZ7rQRKL4Xy9T_OnJCuaUchDrCJn8wN8rjccInXzslNg_FDxT6K8J0xOEymC75jRrDIMHQFuyk3g8akdH4OVYF1i1XOpG0BjJ1VumqGmuyDm3gZJf45K7dlKQ66VaAPzGN4M4WmyT2Mp1CBG8DjrahBkfWFedQYyEAX8B619Q9Kccus6WQOfaWy_BukDXfhD4i_NyXGM-Uzuy2Umw-h5U2RMAP4NMZcL4CC_ju5kLv-sDmZSRKFrwFm0gKuhJxaS3D4KMb5iPurVdX34D8NPlI-YwgVVFZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=vRhjfM3N1wGXmYKY4PttYyvFno-CVyK1Igr3ey2nazt3VH6nMFmzEhhinbRAKjyaBmuJcwHbrIOcG8iNqZlepTxYWvrze_HcLbe8xxOpwO43wmEvJcTHsL34x15NivE0zfxZo6dwpdiTOQsm7hEd4wxVZR2Q3a0biwAQToyi0HRACjcn8-VDmerw287SokpFEUgkqkpd8fpMGkHAcK3qY8yj6xrowvlus9aswczOkCcNR84XCGkbOV-e11jAiJEQK5TSojdDbqw9tJ4N4XcoQDslsoJDh8ndIai6U2gNk24yzSNjOd7I4cFZMc0CCVKRsTWsDxD_mIpWjHwn9gXeDEQLuCF3mYD6rOjWBAKiTeg8_M5_wVWDSlrorZ7qRXEjtLgM0WWCG2uJRZ7rQRKL4Xy9T_OnJCuaUchDrCJn8wN8rjccInXzslNg_FDxT6K8J0xOEymC75jRrDIMHQFuyk3g8akdH4OVYF1i1XOpG0BjJ1VumqGmuyDm3gZJf45K7dlKQ66VaAPzGN4M4WmyT2Mp1CBG8DjrahBkfWFedQYyEAX8B619Q9Kccus6WQOfaWy_BukDXfhD4i_NyXGM-Uzuy2Umw-h5U2RMAP4NMZcL4CC_ju5kLv-sDmZSRKFrwFm0gKuhJxaS3D4KMb5iPurVdX34D8NPlI-YwgVVFZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBjYRxMLjChOBNmktRWI4_Ew9SDoVm-O7rg0gQ4Uy5lCnqLgTB-7fgxlSLrnFRC4fVr4_OHvlS7TCxUw30n8f7aztUR1K8ZfmVMJVza6D0u06SF__K7CFjQ1CwShuxFf0hwz0N9WATyi65EnLYKsYnuvcD9CCQfb2-2IuCDXuimdC1jlPeUaNQQ18K9XbhhIsWvUujfnBt2BiOfbKYdcqbNWTCX5S2PFBkrzbkFRAjZ2Kb6jcJvarLOEBN5Bv9aN6jFcP9uGo04Y5WazgcGIDEzxm7iteqSzY_sPcLv14xPHgMOvsJ8mq-58uJ2HYInN1QlYBJEqVLPxYHDMiK_9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_f7tckyD-odED8e59iRgOVEu4nlTQ6c6BK95jNFWLS6Nv_pTrELghEtoBmG_n3kvLdimy3BWzuDX-5YDH1Fdtf15nWOwj2uLjCm4loeBLZCWnJkwlmgluMzcwkNixN_AmNbqmxWJr204ygl0r-MB6phUaOR8KtoQydQ9GvzAP7bbYvfVsrYRgoRYRRjbEwgDv6LmOOyg_Fp2PwE-2X_aXL8r4OA0yLlBi0e7rflNdI9lqVhgWfiB9rt9oE5xd0R0EKtJCy0LQbgfGwcJspV9qpm2nUq1ffvp4KiFgmBzoa8o1fiy-j2FtDAEd5jqi8Skkohronffc83iPda8I43EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTHazJy-sGbVxdUNG0h71dZwQU2V4PSSDfgDuBmtsfIPoPE656-9z61kobSY4wf4O_P2JqSpMyT4xJOqgu5WITjYVkyNymzmMGWf6oj74Y1D0afu3F9ISMTk6__Tc8rEX7GA5RvLcIYruQ432ZRsQZ5tsNctKOdcP-ULhGPv7q-Xb03TYHx-2GtZ5JDl5BCPpHNfwCBajAr7yYMV35PN_8YLtwn74mKU1ihKRfcWUG6DeRjj1xk1R02vgSPl2eHbbMKMKn7D4Q35nV4XtlH4u0RzcSasX0HtEJCOk0ERX_GTO2IHPjCC5s18kPxkWfXgBbRptlIYqAttgRZCjouEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXOj7KZlSRMoTU1bu_iMfrs-kemB3cJkpeI5VaaU4OkLKumLjVHg6LqBOaC8emMXWQtuf8dlB5J9EUY7y9SD9OgrZ1bv_4WQ4QT5cltgynqts9sqJSg8MFaZZ3-G4lZhIoUIBDrqRQcsH4bFST3uP85wS0J3flYUksHDLHKZSbYW7tuvFuvjVQFGqdBvKvsC8Yg-mnF4y1n3_p_c_lMOYz5Pq-nyYDW3lr1KlLm_79ZiQHTa3gST5fMbVV3DfZN6pVm5Rs-Dhg3xfkrZRFCyJhHVr3CJEb3xDin7Ml0U09EL1-zPD4PR01rMXAedPSsVU6KnWMBFvZJ5IHh-uWSMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob161cD0EsJqdSvSLlkrByeN1lbhWLC5UKozClowoFxFTESnQjGCy1Ck6Q5rtmHs8tT424p0rJ_dYwzi9KI_JDErZdgAJoUa3Nguxv-kqSg394hD9FKQ09h_Ibs6e2-P3nPMyGqBoAs9714tyNBgnca5K6CsnyToO4tDa9FciN5woKfLTSvpBQFhYx3OB6VZNJwBAtD2UNEXLi02AmVrUMd1CmYlIfcx9IvXVRsvh7Z5iiP4mjr2WYveaJAYwFs9k2YRs03ZQAiC80fmjZQovIf8Ga3qJIhPn-lXwvqvFfRD43bpjBtIbvVH8AKjkg11pxnoEGTRHUBcApQyDUDFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2cjluTXRLkozH98L8mZp2mxK302c1oqtYCkOKP6pSBvjBcWHtfZLGUt_Y76JAy4r_QlkDxNoDf7nJ6A8ROT7Y6MsHGC5mjTbbgBqR8cma9n02fETKmdwnPvYgeVhRi8JLeqPOW-Ai7BAgECeHg4tInZRWGyJ-7aCNxs6LmacmxcTekf6nzrNclnrbPG8ZzWGNG5KSfWY2_gxxOyqg-uS_RwI0tkib33u1SeK2u58pu0ILOeU9YzPfVdtogSh9RFnAQ3_vLrgWrGTKmBI597h44AtOKy4mICPkT3Cf6a8u3N0tzcNScaIxT-Nrt_BKqLNFHFSmjdXfQKYUX0uH7rqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXzTz03NFejGAWo-STjcgfxqvgOPMQ7u5SO5CHYNS-TGN0SADLLtrjGzInzWri4DCxJzWkeYJSoZfAINoBFHgJ0MJ_aPgTeJu0bl4fKozpQq7BBFPT2Y0ValnAH8iVZ-Ce9WeOZNCi-g3iQJ9xqipYJF4BCaEOTxpvDSNzOXBzbXSeR3NYDh9uoCrVb4jLQZjn3v6_bOgN2i7yebLnKqe07jG63HWYpTUHWIpzJHIwPY8nyx0Rgi40nQyIQ7DhXokIG3919c0e-gfUFP8g2LfAnU62pitWC_z2qyzvTNAtH02WOQSnWbig9Gds5Ao9hJei6qTzv-Gj67dWHGAnr3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETxNFesuESKx1A28iPcVsCSRPbYqs7dP7xMDOOt8fxWJxbSHQrVPhtWhXnEp7Plk41GUKElW3i57ZhQgG2ZOCCb3kc8zzdH2CK0dp4CWsjtNC-JJd30xdelPEgVX_IxE9f4UJ2-xz4Lm3MT6iskYY81gkxSushsO4_2DtdZQdkZSgU-Y-QCOZXgTly9AtQZSuIX-48cmjDI3KUGdGvEqJEaWek728BsQwEdft2uw5arhUYRLEQ_G0HB-2xLH2gn_bo3ao6qbcrXS4jTVyIljg8MzdLd9-FllFCYXyOiQaY12Z_P3IeAZZi4RLs_6TyeANEysvzppUvkToXhxPs9XqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgmfd707WoZ_vcpFkXQRpDQYIZkcshfZHYbsWnpOYhRUiWpv4IXQJD8PaZzhpYf7qtgwUCBP4dLO_3TFvSP46EAS8sTLwLQLwMjaffkZZQ5MslrS_4jk3RmMoOPM9PFXqa0n2fzA0a1OhfBl54ODxn8QEJWY2gW_m8JKOOL-LpfMaIUWX5wHxex_63JvHQPO6tqwLe6Z75raT2T1ZJyHgMKad5ZPtmHChmMlmusfPlkBvg_cTgfGPw9_z74vMmEUXjrNyVQpnCAnu4hnJH4nNZLDyWPfnsKFPFZnrZFHOQgQ1GWHJrisXsf7_VkxoRqTRMbHloR0iPP8bHfJqtTXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-cw_MqNxmmFkBx6Y_sVVUKLKnI1ceBNNM-QJ5YZtowDaeXGdRyjZkDB0bnUQue52_USTjB-xQ91CKYXRMFNUEqpxD5cHAUvUKn7wg1O3O8qTmXn0sxvCM60sEQFj8ubPZVZVQEa7c_whrZN8edjaa4EsfLUBOLCzajJ-2YBbLx-ZZW7cjyO-_iYXJOgMgHRL5-45Iksfn6RPTua_5EkHCzi2vVg8rIOIkgHqzf7Bqp7qZKV1hLXUud2DGe1gRgZlOnnjA5Jwb5SX3LvGheEYRkqCYMff8h99PPKDlXdJqrMhWBUIpalhmKO5dTFKGuy0xm2gidAKOZtxyHSR8AxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYvSqPs4auUrApT3hOJZkVoruLDTNLl6Ss-aKym5AGjbEEG-q0fvm2X5__JNdTzja7a7PmuzCmIwPbxIoPEz5eMSGstKfGxF0Iicu8b6hx890Fbo-YVMPJLcn1UIvguxC7Yl8WqD_A-ZOpXWZJuhZ2AZP-vZtFlYGpRWXXeqqo6mqrqsfENsj8Z_24hJw12jT4mw7bqj9MuWHyD5Wyitpp6EqnLboNR7FgNzCGVe2Hd6FUiKspijhT4-CT-aA0vJF97Xg07YapfcTqRfJpZNxgg7hkPvnk9SJqhOnVI0HfVzUYNWbxCiOqef4bJevTsAp9-GIMyrTGLSF8l40YuDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
