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
<img src="https://cdn4.telesco.pe/file/lHjXCm15g_ZmsLKrDgTkaWYaGBNyXs7AkZgnlAReowFgaE8j5-_foP-Zb5nOI2M8kn4_jQT1y_AkoFHK9SSf2l64Sa7T3oa-4V6GjjKJjJ4VcWzteSxTYNwIPvHpJC7iDtf2d951up25tbnbxihuU4uMRS1w-Uhpx4GplZyCUnWuCqUeJ7tFHr21JtF4xh-hhkK6eTWSnJHhXrAJjO-L--4x_13_fsKz2-jRtqZfS6fQ_1DmF9fDEupHC229Ox7Qa3ZX_Z42Xvy_emzrjg-Ihgf3UbbJI9bDy-AmeqL0akYb9dV9hM3-CzNYlBhbSXqO5zTFlrIcNhMJt2NbZL5Rjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 225K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 20:15:04</div>
<hr>

<div class="tg-post" id="msg-65939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oujOM9tE_s8MDhmD8jfsEjObMj-8P8jPbFTs2igpms3I5Blh7dAtEEWJfBStFjgFcc8qGIaoqoJqZAGdIHItVLx2mJ8liJR3NPCjYuqf0aBYap7fJ5KjiPjcyyE_RoNo10YvZdz9tpr2XdK2syhE-zUmyjNPtR-hUz2FeirxXT_K_0pXzRIqQq1-uDKrHyRE1KltYLHnuqJVdI7vpkqiIt6li5a34MBKy99EAdpLpPSVEP61TLlmdrUCvIIVsnNXtbH5aqJay8F-83foW1eSUQxDj3EdxvQoONgz7rE-Yw4rOsqxpcUdgW8GyTYrlgRieiXCfqPOHzvJPB0X2J3leg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام:
ناوهای جنگی و دارایی های هوایی نیروی دریایی ایالات متحده همچنان به گشت زنی در آب های منطقه ای ادامه میدهند و محاصره علیه ایران را اجرا میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/news_hut/65939" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=gqrpGCYTwbHXr755tqNulWdTzXfMER1kiLuRhNZIMtazagw6oR6LmCuabAnL4TL2ZOsO1OWzELlGYXtdoAvg-qP0CUmsAVJ417kRcTBbvFdX9fiP31WRcDI4EZfHimUsRroU-3TqNTbg7ZjaIoXzq2a-m2wpuuRgERzOPdqHnOzDFysnjQ_FRvK833B9xEwYnanOlJyhkcwJyZq3Cnh2wALskWG6bfo0bxZnnssXlXXits7hQHzZT3Th8QkU8bDcYQlXhuUl1bJM-NAkwbkfD3WPALufCj_nRaN2Qy7YydbxvOeyUU2Q4MTnU8Ay1yrou_LdtEhgZldmle0P6PEemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3347ca6.mp4?token=gqrpGCYTwbHXr755tqNulWdTzXfMER1kiLuRhNZIMtazagw6oR6LmCuabAnL4TL2ZOsO1OWzELlGYXtdoAvg-qP0CUmsAVJ417kRcTBbvFdX9fiP31WRcDI4EZfHimUsRroU-3TqNTbg7ZjaIoXzq2a-m2wpuuRgERzOPdqHnOzDFysnjQ_FRvK833B9xEwYnanOlJyhkcwJyZq3Cnh2wALskWG6bfo0bxZnnssXlXXits7hQHzZT3Th8QkU8bDcYQlXhuUl1bJM-NAkwbkfD3WPALufCj_nRaN2Qy7YydbxvOeyUU2Q4MTnU8Ay1yrou_LdtEhgZldmle0P6PEemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی قبل از جنگ ۱۲ روزه و ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/news_hut/65937" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI7shHJDCXge3eFqBHAw44OP0CHP8nphkjI2PKoSedoascBW7ZhHr8EvD4Yzq7YAituchejgRoJ634xGGBBiGInIhvc4kia_W2sVBI703P0DNxpdHnMTpbK22n2sLGWGg6AQHk-XCrshLTUcM8CAp3HhE0fw52JSqmqdXtfQHSJkn4tKgubrYMqyeizY1UuTFfZrlb6FlKDvpSgAyyVzRrBiZ55lnXNjVQFJdzPIZbD27FutIJBDdO3G76Vx5S0EOim-DiC8P8kBGAIR8JXlKp25dS0SGYrK7EatSbJ6CGVfj_AgK63wzYz52Wzm6s6mykRRpADpeQR8UjE8W4Rihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: تفاهم‌نامه اسلام‌آباد هرگز تا این حد نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از گمانه‌زنی در مورد محتوای آن خودداری کنند  @News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/65936" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
جی‌دی ونس:
اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/65935" target="_blank">📅 18:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تا دیدن اعصاب ترامپ تخمی شده عراقچی یه توییت زد گفت رسانه ها چیزی در مورد جزئیات توافق نگید :)))) #hjAly‌</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/65934" target="_blank">📅 18:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/65933" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65931">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-1pIGIJo-rT8sJOFp4Hs7pI16xzSVXV00i5qQgHMBS8qkuLVd-HmcyXz9lEFLl2RIwDKr-h9afFyEgaypFGBuF7095kucPw-kCpBeEq4PRLyzXAyEhOxUKD5piuBmhe-b3RGwhKMqW2_44EBFMVs-C4M-LlhEFddUhSLivNVq2f-lDlptBwKF3DXrMjDmwG7Wu7b_aWib5hMsowFpPW_WGskF84G2dWNXhk78IBzVAfodIC9iU0q-JAsn31UAcne1_xcB9vzYYi8IQUbyVKlkUC4s5lt9rbsQxFvRQp65kB7_c_ca54xKdSumYGMMweqL16Fi96KguEG5A4fMLC3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbDGx58PySt2-kkDRnd6oN0W3HyF_K6McCWbFbudK64AmJTtemAAFzxD6tUH9KpSMdf4xwRDE6y9L-c-pdwPpUB2Xnhp_sBY1s9o2q83O5ZJ7dCUC_7PDDVfxaF-ND1GcSlYWASAbG-PffLro18t6b84nktT5lPr7OzgaWdMl-2_JO5VwOOZZPl8UaWggY4GkXnGF1T5HVSDhqTPJwkNLHZPgGrQtsR_9py5q2toaFrVTAUzdv0LAKnL8KyE38vvpg2Ede4C5liO0YzGbbxh1jVv-8OUo9z0MuFI8PKpRVbkwmz_IepVm2imL3OLPoYL_XcZehfwYGAjg0x88a-VbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برنامه امتحانات نهایی پایه های یازدهم و دوازدهم منتشر شد.
شروع امتحانات از ۱۳و۱۴تیر
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65931" target="_blank">📅 17:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bi54Q0r-40p4gf0L6DxE39m3AmKCFhHrXZDu7NpsZjPb8cxtYxelRxqdqqq48uWwtwrXz1jAcy8AHPTaPuQNzXnHQX9WMX7G_Q_pYBbBTWOYIhbKM3i3YmmCj63sA519O9ktyvQlVNDQqU5XhsnjQpQt3QihJhLgm8HRVixwkOADnnxGxz46MsXuzF4Pt6TQ-h1T4qKJNM3kgKTGjYC6QhFGctC5twKFg1UrBIb_2cdWK6wLCUtg6PJeHKMqu-ogTkrKiuV0VtSG8JU8MPzBgZi71UCnY7dGt_wxvZmvZ9wEGl1FpEHOO-3cRL9DQ9TKEe8_V-MvIYJEMREf5a9Wzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c65a1f96.mp4?token=bi54Q0r-40p4gf0L6DxE39m3AmKCFhHrXZDu7NpsZjPb8cxtYxelRxqdqqq48uWwtwrXz1jAcy8AHPTaPuQNzXnHQX9WMX7G_Q_pYBbBTWOYIhbKM3i3YmmCj63sA519O9ktyvQlVNDQqU5XhsnjQpQt3QihJhLgm8HRVixwkOADnnxGxz46MsXuzF4Pt6TQ-h1T4qKJNM3kgKTGjYC6QhFGctC5twKFg1UrBIb_2cdWK6wLCUtg6PJeHKMqu-ogTkrKiuV0VtSG8JU8MPzBgZi71UCnY7dGt_wxvZmvZ9wEGl1FpEHOO-3cRL9DQ9TKEe8_V-MvIYJEMREf5a9Wzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین طهلیل ویدیویی بنده از شرایط خاص منطقه برای عزیزایی که تو دایرکت درخواست داشتن
🙏
🙏
🙏
#hjAly‌</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/65930" target="_blank">📅 17:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65929">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=LCNmPyPZ68inCAezB_hgbPSsSn7ARWhMwrTr3Rtg9e6ywGJAdOFN1zKWY7hL6Bygte3ODEwz97kmJYSkjB3zWLe5qyr1kQ5kB_ovPBXUpiS8saGAgezLzfzN3v2uZEvU-Tf2PNL_hQRF5jfUPZ52kCCAf1Dfw_9nUXv4WXFts2D6h55cFihbyc7aC65O1RmZJc94nW1T5tc5ZXn0OHk72jyN2yLmHpDSlpZI1EKuaKmHKbFmkpOlAeiwNk6m4v0xXJ1cvbablB_BYS6ua65amahteEJK570WXp_nSBOgf2T5gDvepWhCtocV0x45VE3lTPVUOu5WXkMEtFGsv1d39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6007e01a82.mp4?token=LCNmPyPZ68inCAezB_hgbPSsSn7ARWhMwrTr3Rtg9e6ywGJAdOFN1zKWY7hL6Bygte3ODEwz97kmJYSkjB3zWLe5qyr1kQ5kB_ovPBXUpiS8saGAgezLzfzN3v2uZEvU-Tf2PNL_hQRF5jfUPZ52kCCAf1Dfw_9nUXv4WXFts2D6h55cFihbyc7aC65O1RmZJc94nW1T5tc5ZXn0OHk72jyN2yLmHpDSlpZI1EKuaKmHKbFmkpOlAeiwNk6m4v0xXJ1cvbablB_BYS6ua65amahteEJK570WXp_nSBOgf2T5gDvepWhCtocV0x45VE3lTPVUOu5WXkMEtFGsv1d39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه ای ۶سال قبل:
هیچ پیام مستقیمی برای ترامپ ندارم چون اون رو شایسته مبادله پیام هم نمیدونم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/65929" target="_blank">📅 17:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ:   شرایطی که ایران به رسانه‌های دروغگو فاش کرده است هیچ ارتباطی با شرایط توافق شده کتبی ندارد. آنچه گفتند، از جمله بیانیه ضعیف و تأسف‌بارشان درباره وجود توافق، هیچ ربطی به حقیقت ندارد. افرادی بسیار ناصادق در برخورد با آنها هستند. هیچ چیزی به نام…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65928" target="_blank">📅 17:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:  ۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/65927" target="_blank">📅 17:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65926">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPUQaMbxgIfFNeaQCNBA1phQ-6ZZHR5nebdEK9qeZ-CUTPSV9WFUMRDHtfSc1-Sp-hDd_AlKJiOspKPaay13jdbqqu6zl83qyrz01zBDAJwayBXxLmw_OywYSlMk4_k1y88t6KVELwzOC8Vtwmdzlvr_X9IQssDN00_olQvPwy0YEIc_je0BEkSWnl5uX_S5YG7OBabvyrR6loxX0X6dKwvqEySSxT1t4XfZFxojuF3GILxieTdleNsu2TKbz2Y6WYK2lfxii44_CaIW91lh4ye5OFMtwILNQw3Xc498xR0MpZW-cOb_-tEwFUg3HdqbtZ_9U9H6mNWdVtMwiGOaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلاکاردی عجیب در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65926" target="_blank">📅 17:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65925">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/br7tvQ6R8HY7LScsxsdWtPNlonE-TvKzngePYLa2lJOY-3FsaIKHRqa38vDGFKWIg9cTg5QextrRmC9GGyI1uiiad0Zxqoc_ir-LJi8FWhbm2f0sYVFx2FmnepJImpAFwjGi94smfs_k6j-Bflg4EiRHMKUGUqjNiUgOsnRQ65oIv9yxMBHicRjal7VjbjdGzxn_Jr8Y_mbUGZ_Xd-TiwQ8aVa4hrP9lL0kdcgE38s26-FVWT4qr4Gq4XhJS3fvNAu4TdreIEP74SMCGoU0n0o2AkI_mFWsELxg6h4KQjB0oiBpxcnVwNmHb0uUw0_35yNe25BmJT4SwoA0jMk4JLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
ترامپ در سال 2049:
ایرانی‌ها هر لحظه ممکن است توافقی را امضا کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65925" target="_blank">📅 17:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65924">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezuYn-HM2PbkVWHqUnzjZxk7jEuDpsAwAaERwMDs7NYjg_goYQ3Bj6tvlV6yhnVF4WpHKBQogGln1TQK10mAz6S26saVV8E3MzGv05kcCMzTiG7QwBFWyEdHh0UTAoUDY8dHe052InD7tZcswu0VQR9906o1p7MhRXEYRjdKPjYxT0DheyACGHH7BrivIvP3woCaGcm9mZhBn3Y08nzH8k3XBvLPwcTKYuCa-P_rNdjrDXJPgTTPIeRzE_RgvoGfjhOz2ysAFqGJgnLBZaWiAGVfQD7WHN9EtNXWJAiaBS_KL7kAg38M5kNvtOeEB3YoWRBiva6xmcP6e4nq66KB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
مرندی، عضو تیم مذاکره‌کننده: یکشنبه در ژنو اتفاقی نمی‌افتد
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65924" target="_blank">📅 16:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=K-VLISqeHv1QaM8UiHt73STCeyCmPy9iHh6XbUYuKhCzKVD1g2Iykc3bNNzMzwmwrrlqFwkfvtRQv5iT-n5eC22X1lFTzMcbr67Hh5nMt_2kPAaWp7oD7PuyRCM5JCvXy41bhlhFECin8QaH7EOt0cttjzCtOJaP_dhXQyoawyhY75hcnJ_uML0HpkXTq9NtXvaAYz30MwkK0KSuno1Lx5qBMOCgr40NXFSYeHntk9QlD2LOjSwW0FPZNkccYVgPKmm4KvJLwqiNO0uWu36Ek7MF7kF8bx93bSyUTHIuAL9y7Wvx99jjugiIVyETYi_0ZPhu1EW2PK5lf9F0I9TQGaRf1mINgkVgJqtJUK740A-4mcg_u0dnyAakJPjobD-YpMaEakOBGtBemFMs5rJg5CRwveuo33jXVWcEAuVveObLCK3wFntHiZ0qF5pYvchV6phNg08ozXqP6hvmwVjIu3rRf7Y7a8-OVMWSonlB_vUI2hvaz4HQ7nmCebaKfrNKjqct7Z1YP7B_xmvz8rSSjfVSMRjHNz0VedtiNRjA1pA7zHtEG9e8assjJQp8M22jTjLsZQvOpjZQSFVDWnrSduB-y0nrqYkI5jdWzpApHpxUUyNltr-ElgwtgnFI_nIZBnaL14MmP74_6zOfLNC_puoqjpARK_bKBOlad019k18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f5e54d8d.mp4?token=K-VLISqeHv1QaM8UiHt73STCeyCmPy9iHh6XbUYuKhCzKVD1g2Iykc3bNNzMzwmwrrlqFwkfvtRQv5iT-n5eC22X1lFTzMcbr67Hh5nMt_2kPAaWp7oD7PuyRCM5JCvXy41bhlhFECin8QaH7EOt0cttjzCtOJaP_dhXQyoawyhY75hcnJ_uML0HpkXTq9NtXvaAYz30MwkK0KSuno1Lx5qBMOCgr40NXFSYeHntk9QlD2LOjSwW0FPZNkccYVgPKmm4KvJLwqiNO0uWu36Ek7MF7kF8bx93bSyUTHIuAL9y7Wvx99jjugiIVyETYi_0ZPhu1EW2PK5lf9F0I9TQGaRf1mINgkVgJqtJUK740A-4mcg_u0dnyAakJPjobD-YpMaEakOBGtBemFMs5rJg5CRwveuo33jXVWcEAuVveObLCK3wFntHiZ0qF5pYvchV6phNg08ozXqP6hvmwVjIu3rRf7Y7a8-OVMWSonlB_vUI2hvaz4HQ7nmCebaKfrNKjqct7Z1YP7B_xmvz8rSSjfVSMRjHNz0VedtiNRjA1pA7zHtEG9e8assjJQp8M22jTjLsZQvOpjZQSFVDWnrSduB-y0nrqYkI5jdWzpApHpxUUyNltr-ElgwtgnFI_nIZBnaL14MmP74_6zOfLNC_puoqjpARK_bKBOlad019k18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هگست وزیر جنگ آمریکا امروز ۴۴تا پرس سینه زد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65923" target="_blank">📅 15:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
خاورمیانه در این مدت
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65922" target="_blank">📅 15:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65921">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
ایرنامتنی رو منتشر کرده و گفته تفاهم نامه پایان جنگ دربرگیرنده این مسائل و موضوعات است:
۱. موضوع هسته‌ای دست‌نخورده باقی می‌ماند
هیچ توافقی در مورد پرونده هسته‌ای در تفاهم‌نامه فعلی انجام نمی‌شود و ایران هیچ تعهد جدیدی نمی‌دهد. گفت‌وگوهای هسته‌ای در مهلت ۶۰ روزه پس از امضا انجام خواهد شد.
۲. تنگه هرمز؛ نه واگذاری، نه نقش آمریکا
ایران هیچ تعهدی در مورد واگذاری مدیریت تنگه هرمز نمی‌دهد. آینده اداره تنگه در چارچوب یک امر منطقه‌ای و از طریق گفت‌وگو و تصمیم گیری مشترک تهران با عمان حل و فصل می‌شود.
۳. پایان قاطع جنگ در تمام جبهه‌ها، از جمله لبنان
هدف اصلی تفاهم‌نامه، پایان جنگ در تمامی جبهه‌های منطقه است. آمریکا تعهد می‌دهد که اسرائیل را وادار به پایان جنگ در لبنان کند و عبارت «تمدید آتش‌بس» در متن جایی ندارد.
۴. آزادی دارایی‌های مسدودشده با ساز و کار مشخص
بخشی از دارایی‌های مسدودشده بلافاصله پس از امضا و بقیه به تدریج در طول مذاکرات آزاد خواهند شد. تهران تضمین‌های روشنی بر اساس ساز و کارهای مورد نظر خود دریافت کرده است.
۵. غرامت جنگ در دستور کار
خسارات وارده به ایران در تجاوز آمریکا و اسرائیل از جمله موارد مورد اشاره در تفاهم‌نامه است. ساز و کار اجرایی دریافت غرامت در مذاکرات ۶۰ روزه پس از امضا مورد توافق قرار خواهد گرفت.
۶. جزییات رفع تحریم‌های اولیه و ثانویه؛
موضوع مورد بحث در توافق نهایی
رفع تمامی تحریم‌های آمریکا و قطعنامه‌های بین‌المللی در مهلت ۶۰ روزه مذاکرات هسته‌ای بررسی می‌شود.
۷. سه موضوع و ۶۰ روز برای توافق نهایی
در مذاکرات ۶۰ روزه تنها سه موضوع بررسی می‌شود: استمرار برنامه صلح‌آمیز هسته‌ای، رفع تحریم‌های یکجانبه آمریکا، و ساز و کار جبران خسارات. هیچ موضوع دیگری در از جمله توانمندی موشکی ایران، دستور کار نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65921" target="_blank">📅 14:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
متن توافق پایان درگیری میان ایران و آمریکا تقریبا نهایی شده و منتظر تایید نهادهای مربوطه هستیم.
متن نهایی تا زمان پذیرش قطعی آن توسط دو طرف منتشر نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65920" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65918">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlTrQvFiRhhPGLpD0MGEtmSfFXKUr8nLBVm592SaHSSsY_ECfNsFKBRLPSw0vYlGvDHoR7HjMMRWPnCfiPzZBXMrsKzDWuN2gXGthb8Njm0VYLoec-1LlHjByZlHyXQBkYAygINSwamGBrI70G_UwKBCyW4erW-oNgiAPtd1yiibNroOJN2_5634ZdN7jaICRyeEvmuIBCdagOZ8mLDkUk17zPxFrC7U5ep-TPd3wuEU2oq60Xm7xSspF_tR8OQfF7TO5osSkh7XlsemRLR0Sf8_L7iICfWIJrQRY7gx4FMFQUt-ogupYgJIKSg97bTKCpeZNBt0h-GWDMm5Xbn1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXyQkHVJ_vv4xlZIE7mCJi1RAVid4dTRQFuK3NvFjNNDNo5Jqg108rZ1gup7J-g6QSf9GkRNtPb_WoQgIBk0KyBSndeUM9UOcCEvE-EvYC65UxKaPuwjMc17Z09-g1C1NjvVXrh_34G3tfZ7vJ7WYsBE4S-bPqz13wQIBFsNa7aAb4zQ6C1XWX2PByxFYGewcK5Szi_zv6I94XaCagB9NlWJVNgBUREX1cHCQWvaHBufNIXLvdLGQk4htJuJvIDglgjPBT_GrZIIrcZGYOPYdZtWJ12ZjGioScTl0eGF_xaa0W5C48b8ldq7KuXXrCAqb-ZV6hwm2H1-SxviDsgyMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تصویری که یک پرستوی نظام در تجمعات شبانه از خودش منتشر کرده درحالی که چاک سینش پیداست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65918" target="_blank">📅 14:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65917">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=GmS-gKmf_JafpKLmIeQL3HDEpa13qlBrVZuSHuPWh5u8BtqvqTr-HE7U2xjUglXj_5UvpgVNxjH2U3I0zPSFZF1NO8gairBIWzSG2M3s6UmXSdSfDjHmVoKa3lZdl19fqTfKxVw3WDonGlDNFnxNkf0mTDNiFsRHPpk7472f3XbHQIeEFrZw3eKrj6rWAiiop0HZvK-8CClDpibAUfts9v_cTsam06RX_AP3VaeQroRREtdIgClauhLqsMW6auwbhFquaC-SyuRqhFyUeqpvkCkfFtHbAZmWSFQAeh5UOuVfmV4cgAN6p4tOIeTcJzhWu7wKCapvdQ7hLxpT2aNl0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aed65f61d.mp4?token=GmS-gKmf_JafpKLmIeQL3HDEpa13qlBrVZuSHuPWh5u8BtqvqTr-HE7U2xjUglXj_5UvpgVNxjH2U3I0zPSFZF1NO8gairBIWzSG2M3s6UmXSdSfDjHmVoKa3lZdl19fqTfKxVw3WDonGlDNFnxNkf0mTDNiFsRHPpk7472f3XbHQIeEFrZw3eKrj6rWAiiop0HZvK-8CClDpibAUfts9v_cTsam06RX_AP3VaeQroRREtdIgClauhLqsMW6auwbhFquaC-SyuRqhFyUeqpvkCkfFtHbAZmWSFQAeh5UOuVfmV4cgAN6p4tOIeTcJzhWu7wKCapvdQ7hLxpT2aNl0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وزیر ارتباطات: بستن اینترنت امنیت نمی‌آورد. وقتی اینترنت قطع بود، وزیر اطلاعات، لاریجانی، رییس اطلاعات سپاه و بقیه ترور شدند. با بستن اینترنت، جوانان نخبه مهاجرت می‌کنند و این ضد امنیتی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65917" target="_blank">📅 13:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65916">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
ترامپ از زمان شروع جنگ ۳۹بار گفته با جمهوری اسلامی به توافق میرسه
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65916" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65915">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=gmEUSYh1Id2CYMkvQjd8xkRxZrXQy2bCXPa3gcYF3dQ6M4vNMmz_j8zHgk99ip3_UcrVsX2JAZu9AyRQRVOh9IP4svMixYbmd-EyX8W7ikGx-ahiGezaPUv9x0StBTNpzovw51MGtu3HTRSy4_hS10cWspENupaMfoM82LQiPgY_6K8ZDKioFjhAztjVTHUopzDKbOUYXYZPI5xA2jgnP9HhZ3Oq_b3EEShllxMYivkbFe65GuyvaAZ5svQYmRgcZu9OZXwHWyq98heLED-oZLO0UTrPaxdVdhKPU5_UJ_F2rn5jJc1raZ6YvwhevwjqTCWkpZhL1ojHiOdniXIRWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30551bbbff.mp4?token=gmEUSYh1Id2CYMkvQjd8xkRxZrXQy2bCXPa3gcYF3dQ6M4vNMmz_j8zHgk99ip3_UcrVsX2JAZu9AyRQRVOh9IP4svMixYbmd-EyX8W7ikGx-ahiGezaPUv9x0StBTNpzovw51MGtu3HTRSy4_hS10cWspENupaMfoM82LQiPgY_6K8ZDKioFjhAztjVTHUopzDKbOUYXYZPI5xA2jgnP9HhZ3Oq_b3EEShllxMYivkbFe65GuyvaAZ5svQYmRgcZu9OZXwHWyq98heLED-oZLO0UTrPaxdVdhKPU5_UJ_F2rn5jJc1raZ6YvwhevwjqTCWkpZhL1ojHiOdniXIRWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آتش بس در خاورمیانه:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65915" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65914">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65914" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65914" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65913">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Mh1IShvMz_S4Ag-WdztK-tuqfEX21jReeUcGqMt_tU0LJx-3ZckS3NHviB_VqCTk201JaxumAp8jK080kk53M8fIJnQFrOqUj0NcF09CmMlR-K_0VV2UtbtcKHAPrkE6vowL1XaXc8uNcvEH_wPNI0ulE_kQkdmGgeC_Rs5yLfSBzzT02jDTILERvZrYXuQDx5UQSKu-qzDAmyXawaTHbVZ9z-68E3qNXhU8RvsngUYS-GcI6oSaYCGcOHgPF_6wddoxCWbb1pGIt7Ps5kHZ8IsCKOtImrJwHLVB433kJ5L3d3W3QibfKfDZKMQDrE9eQR8ugvTBjtMXkUe4lGH6uhRiUAP-8DO_NMRwx8tbAuRTqmK7cy2cClIWfCAMvgf8N-59SAX6LL4Lnjs2M4kwNIxNn_8fkCL0yTOo5TMA6dbdegE7JvjvT8-yjML2tv6VjPuOuQl23TqIsB_Y9vvR9cJDAGRIEdl9z81J_Ynjm-TNf2YKTJoW9y3fM7Jgp64U_S0uUSdwBnmEetpb_o1_ybxuFhDiy7vwf6HF4FHY5cbcWnRnBLxUc4phn7KR9JowpOjFBEGfXJBA90SRLQsLV08kxHQWyYLwIuzQsM2dPLmz0C2K81dNJrUaUgpxLUZt5WGTgEbL-YEpujOydN2t45VXujkfkHqfpitY4tbWHeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=Mh1IShvMz_S4Ag-WdztK-tuqfEX21jReeUcGqMt_tU0LJx-3ZckS3NHviB_VqCTk201JaxumAp8jK080kk53M8fIJnQFrOqUj0NcF09CmMlR-K_0VV2UtbtcKHAPrkE6vowL1XaXc8uNcvEH_wPNI0ulE_kQkdmGgeC_Rs5yLfSBzzT02jDTILERvZrYXuQDx5UQSKu-qzDAmyXawaTHbVZ9z-68E3qNXhU8RvsngUYS-GcI6oSaYCGcOHgPF_6wddoxCWbb1pGIt7Ps5kHZ8IsCKOtImrJwHLVB433kJ5L3d3W3QibfKfDZKMQDrE9eQR8ugvTBjtMXkUe4lGH6uhRiUAP-8DO_NMRwx8tbAuRTqmK7cy2cClIWfCAMvgf8N-59SAX6LL4Lnjs2M4kwNIxNn_8fkCL0yTOo5TMA6dbdegE7JvjvT8-yjML2tv6VjPuOuQl23TqIsB_Y9vvR9cJDAGRIEdl9z81J_Ynjm-TNf2YKTJoW9y3fM7Jgp64U_S0uUSdwBnmEetpb_o1_ybxuFhDiy7vwf6HF4FHY5cbcWnRnBLxUc4phn7KR9JowpOjFBEGfXJBA90SRLQsLV08kxHQWyYLwIuzQsM2dPLmz0C2K81dNJrUaUgpxLUZt5WGTgEbL-YEpujOydN2t45VXujkfkHqfpitY4tbWHeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65913" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65912">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
کانال۱۲اسرائیل:
مذاکرات نهایی آمریکا و جمهوری اسلامی در مورد برنامه هسته ای و مسائل اقتصادی است و برنامه موشکی در آن جایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65912" target="_blank">📅 12:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65911">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
یه‌یارو بیکاری بلند شده تمام اسکناس‌های کشورای مختلف دنیا رو جمع کرده و باهاش ویدیو ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65911" target="_blank">📅 12:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
رهبران قطر،امارات و پاکستان کسانی بودند که مانع حمله دیروز ترامپ به ایران شدند.
سران این کشور ها به ترامپ وعده دادند که توافقی اولیه با جمهوری اسلامی دردسترس است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65910" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247426e69.mp4?token=rmj4r4wfGQWGRxJIgykI-vtQccwcDC2yDiHspPchOOQTM2QVjcEmmttJ0-BgXJcRallweN-77xM8RfJLlrCOdD4ATA-UPeZ9sJq3G-NaGND0yQrykr-Cy-U1pvMAi7drOk5DHPRa367EFLTL9G95EHyttRUpZ1zP-2S_lgS8kop6RbmCrAffy1G6TLHNgCwsl4A7keAdKzz9zWdSgQtz9gelxUzHBCftliNv6QRjsNZPdwQxOZjJ00OUu1WJzE25IFIjvnXJ9RD_WjkJNBsWXl9co2CKH-TelTQ29pIiYy7PDiccLTaGtmSo0bmfwnytFOs6RmvxP5qu7Xx8wLv4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247426e69.mp4?token=rmj4r4wfGQWGRxJIgykI-vtQccwcDC2yDiHspPchOOQTM2QVjcEmmttJ0-BgXJcRallweN-77xM8RfJLlrCOdD4ATA-UPeZ9sJq3G-NaGND0yQrykr-Cy-U1pvMAi7drOk5DHPRa367EFLTL9G95EHyttRUpZ1zP-2S_lgS8kop6RbmCrAffy1G6TLHNgCwsl4A7keAdKzz9zWdSgQtz9gelxUzHBCftliNv6QRjsNZPdwQxOZjJ00OUu1WJzE25IFIjvnXJ9RD_WjkJNBsWXl9co2CKH-TelTQ29pIiYy7PDiccLTaGtmSo0bmfwnytFOs6RmvxP5qu7Xx8wLv4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یکی از کشورهای آمریکایی پلیس به یه زن مشکوک میشه که ازش اسلحه بگیره. تهش طی تحقیقات زیاد متوجه میشن اسلحه رو تو واژن خودش مخفی کرده و با تهدید پلیس مجبور‌ به تحویل میشه
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65909" target="_blank">📅 11:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا منتشر شد. این تفاهم شامل تعهد آمریکا به رفع تحریم ها، خروج نیروهایش از اطراف ایران، رفع محاصره دریایی، بازگشایی تنگه هرمز، لغو تحریم های نفتی، و پول های بلوکه شده ایران است.  آمریکا موظف است طرح بازسازی اقتصاد ایران را ارائه دهد و در حالی مذاکره نهایی میان دو کشور باید در مسایل هسته ای و اقتصادی انجام شود، بدون بحث درباره برنامه موشکی ایران. این پیش‌نویس نیازمند نهایی شدن در نهادهای مربوطه است
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65908" target="_blank">📅 11:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65907">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک دیپلمات از یکی از کشورهای میانجی که بندهای متن فعلی را با من بررسی کرد، گفت که «ایالات متحده و ایران در مورد متن توافق به توافق رسیده‌اند»، اما اذعان کرد که هنوز تأیید نهایی لازم است. با این حال، هواپیماهای نیروی هوایی ایالات متحده دیشب با تجهیزاتی به مقصد اروپا به پرواز درآمدند تا برای احتمال سفر معاون رئیس جمهور ونس به مراسم امضای توافق در ژنو در روزهای آینده آماده شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65907" target="_blank">📅 10:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
⭕️
توافق قریب‌الوقوع جمهوری اسلامی و آمریکا بزودی در ژنو امضا خواهد شد و به‌نام توافق "اسلام‌آباد" نامگذاری می‌شود. طی این توافق یک آتش‌بس ۶۰ روزه که لبنان هم شامل شود، شکل گرفته و ایران می‌تواند با پول‌های بلوکه‌شده خود کالاهای بشردوستانه تهیه کند
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65906" target="_blank">📅 10:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=rl-i8GEU6dA5sYtVGslP-HcWt5NXegbGY9ezN4_SZN7T0FJW7_ezSppF5hSbQcYHNXYc093r60xzsyOF6EKERakKJ--myf7SX4Z-AEpMljVIGpwqxSCq-926yP3zc0t5-Y_lnFVSUMe1mAWZZxVCvazK3aNlIAK_OjBXUvL8bR4qlFVUJim1XkDSNPcuZVnTrf0qOhZy4HDkJBlgChY2o89TsBjwxUEzuMN1y2u-qP8FVaCnEA0TPCYFMCcAJaJztBwF1QNU_COJi_rmnH_Azc3bZiu4V4PYJ8vsCxjtUGrAm0NFbO4RdmomdB_f5BEVEveoUl7XH4bxhjMZ10Vn7n6kXdZirr9AD9usra1i4yesXHllt4GlKHpLSxeb-fJcnzyG7AuBjsbw1YyS2owSkx_OcqvucNLHrJGxwQcLeb9zCCsNnZZwQSEBvGcwSTP89wgWMMxx67o1gRhmoKhcfWEqTjF5mo8Ejouaf_s-hwysfeFk9p21tmqg7nQWcLvwT2tiL09PMFFT6Po8HsbE9qvN50WkftXldaV71BJ9wWAjDURswvtDZQaH_lKZDwzXyBvfRrDt9I0wQ7FehHLFbjcMffzug6YeR9wnkOct-9pFor2RFRso9VhdL-GWuHCK7b98wpKKcRL9M3Afc4aZXvFxJVz6ZllEnqO7koEsCjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/215d29fff2.mp4?token=rl-i8GEU6dA5sYtVGslP-HcWt5NXegbGY9ezN4_SZN7T0FJW7_ezSppF5hSbQcYHNXYc093r60xzsyOF6EKERakKJ--myf7SX4Z-AEpMljVIGpwqxSCq-926yP3zc0t5-Y_lnFVSUMe1mAWZZxVCvazK3aNlIAK_OjBXUvL8bR4qlFVUJim1XkDSNPcuZVnTrf0qOhZy4HDkJBlgChY2o89TsBjwxUEzuMN1y2u-qP8FVaCnEA0TPCYFMCcAJaJztBwF1QNU_COJi_rmnH_Azc3bZiu4V4PYJ8vsCxjtUGrAm0NFbO4RdmomdB_f5BEVEveoUl7XH4bxhjMZ10Vn7n6kXdZirr9AD9usra1i4yesXHllt4GlKHpLSxeb-fJcnzyG7AuBjsbw1YyS2owSkx_OcqvucNLHrJGxwQcLeb9zCCsNnZZwQSEBvGcwSTP89wgWMMxx67o1gRhmoKhcfWEqTjF5mo8Ejouaf_s-hwysfeFk9p21tmqg7nQWcLvwT2tiL09PMFFT6Po8HsbE9qvN50WkftXldaV71BJ9wWAjDURswvtDZQaH_lKZDwzXyBvfRrDt9I0wQ7FehHLFbjcMffzug6YeR9wnkOct-9pFor2RFRso9VhdL-GWuHCK7b98wpKKcRL9M3Afc4aZXvFxJVz6ZllEnqO7koEsCjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه خبر:
با صراحت میگویم بخش عمده ای از شروط ده‌گانه در توافق وجود ندارد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65905" target="_blank">📅 09:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=THUsU4TZFPotn9BY_n8DLxnd4xq4g5-_1mO-9Jlsfepa5CruIW6O_yzsTz89ylTc2GbkzUu7d1sOZuOPhhqRFNkk1UzT3m3zzW6BWQMbt1-i3JtIRhYQyIDFcVuIls1n0-7is2G63LhYUPe8dXG0xsAAYp80KTFSPJX0xxDAiwP3pAuO_MQ54eg7x2S35McyEbItheDOAh2AGkUvh9287OgFVG6MJZWPZksf2-mqr3vvRUDB50ndoColPzHMS5QRl8fcYmxWLkFCJCGQF2Ku5jhSNXXAH-FwXs_DVUzW1pNr5fYw0y3zOhRMGLWkRAhfIlDgWWbTrfzM3_eVl_WUPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6afe375b.mp4?token=THUsU4TZFPotn9BY_n8DLxnd4xq4g5-_1mO-9Jlsfepa5CruIW6O_yzsTz89ylTc2GbkzUu7d1sOZuOPhhqRFNkk1UzT3m3zzW6BWQMbt1-i3JtIRhYQyIDFcVuIls1n0-7is2G63LhYUPe8dXG0xsAAYp80KTFSPJX0xxDAiwP3pAuO_MQ54eg7x2S35McyEbItheDOAh2AGkUvh9287OgFVG6MJZWPZksf2-mqr3vvRUDB50ndoColPzHMS5QRl8fcYmxWLkFCJCGQF2Ku5jhSNXXAH-FwXs_DVUzW1pNr5fYw0y3zOhRMGLWkRAhfIlDgWWbTrfzM3_eVl_WUPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گفته شده ترامپ بعد دیدن این ویدیو تصمیم گرفته که توافق کنه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65904" target="_blank">📅 09:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhhsewN77S3JCMK5--mbQQEXD0bIjeiBHmxqQBGX2bPufWw3d84DiOX_REqNta-042XdEHUlOulmelLCJ_9-fvXTGkWrIV6-tNXYSkfcsvNbDUJzy8qQYmV5GK0xks8bofxbQBGEifxahwMpgTk4qDgO1fRH9R4mCx-NznpM32lwBqQyYPUxqLftiPOQe__awdugfIy8YVownQSKN0x7_N_DEKRjc2Cs5k3GL2Z9VO6SktMeD-HdZcOgjdZrN2s3RWaWzVTXrylRiwEuI2cTawdYDgqMQcOoyU9TF1KuCVUV7T8Zut9NfUHVvbu8Vx_0q7rNiBxQjSqPm-yBMeqbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین:
اگر همه این دولت‌ها با این توافق موافقت کرده‌اند، شگفت‌انگیز است که چگونه همه این دولت‌ها به این سرعت امضا کردند در حالی که ما اعلام می‌کردیم که در اسرع وقت بمباران خواهیم کرد.از آنجایی که این توافق انجام شده است، آیا می‌توانیم آن را ببینیم؟
در این توافق چه چیزی هست؟میتوانیم آن را ببینیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65903" target="_blank">📅 04:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ8AmelYGZd4b0EUH0FNnNjWv0nh3sVQs0bUz2AyQ7Cc8tBmkTAzhA8A9svfiNkBfki_LeJiyLQCv7pH9vg5ax7dcwejlGVxa6etJdT6F1IZ552jbhpTv50IRAD725VxuMB2gopY3N4cYnOpQDGNowFA8kOuDyMuvLAibB-xUiVdN3FA4u_gK7DH8B3SVRy1dfzSGtWbhc9rXXEbAzUBF2GtATk9oirXYzZKzMmUbjnYqjkYQ6YWcrVFC6gcWEWeehwyYthL64H4cpLMOUIECq2V0mjqp7AX8V_s9hpI17SekKWE2-BXaB0V6JX0GhTWsfoOSRoUVk7wtk08Je2nJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دقایقی پیش زلزله ۳/۱ ریشتر در پردیس تهران به‌ وقوع پیوست
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65902" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
رئیس‌جمهور ترامپ درباره ایران:
ما با ایران توافق کردیم. معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
مردم خیلی زود به خانه‌هایشان بازخواهند گشت. تقریباً همه چیز تکمیل شده است. ما هر آنچه می‌خواستیم را به دست آوردیم.
نکته مهم این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت. یعنی نه توسعه یافته و نه خریداری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65901" target="_blank">📅 03:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65899">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=JzsTdPtFU9Jq1sFZ6IxYRl2eRPIkB6QKqzr3he5MZ1F7iY78msgTWTinbvh6K9uDWQU4fQlYYBUaQ1TF15dVLrhn4OZ7iBVx1FTot4VhSBk1k78G_gBVni5bqythLSWDGxtAPDu0fUOu-pKrlnVdmA-ZiTGOCPE_rUhHn4LxHY7s3fKdAjpjEFH-n7pJMf1f9yqMVEJ2e2CAj0TufMl6w31tdSH41xocfwaPxOLNX6k0lX1JY_uQKI3yBCYQdlqPo6gx19yX0_uFIMhsdaGzrwiznuylJrE_1_Ag4KK2jjkOgFoJQWw-Q_LMUg1b1ZGRpuOagesgwh8PgP756lzZ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78687e07ef.mp4?token=JzsTdPtFU9Jq1sFZ6IxYRl2eRPIkB6QKqzr3he5MZ1F7iY78msgTWTinbvh6K9uDWQU4fQlYYBUaQ1TF15dVLrhn4OZ7iBVx1FTot4VhSBk1k78G_gBVni5bqythLSWDGxtAPDu0fUOu-pKrlnVdmA-ZiTGOCPE_rUhHn4LxHY7s3fKdAjpjEFH-n7pJMf1f9yqMVEJ2e2CAj0TufMl6w31tdSH41xocfwaPxOLNX6k0lX1JY_uQKI3yBCYQdlqPo6gx19yX0_uFIMhsdaGzrwiznuylJrE_1_Ag4KK2jjkOgFoJQWw-Q_LMUg1b1ZGRpuOagesgwh8PgP756lzZ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ درباره ایران:
امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود. این ۹۵٪ از موضوع بود و آنها این کار را به قدرتمندترین شکل ممکن انجام دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65899" target="_blank">📅 03:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65898">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65898" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65897">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KaFz4c_4si9iZVxGT7JafsY5om9ccGzjC_89NuMmXvDg9Dw6mY-sB5YE0j-IWjqIMcrtJWBFEA6F27AAliJtFDLvBg6poL8Cvu27NWmgywuF5XN4CWZbYgTtc_9Yk61XMAViknQZe9TICSE0MFHjG9CtIwBjK4pQe1FI7gfUrKeTT_XCWZcIIMLfvFSjAYluLLz0tkKauMM8rzrpLEkWtyOxfXTqh-mgeGWlq3lV7kMcn5ZYja6A9dSIZKyzvwIF9U5iMWZ71I-sVRQc3jUAWasASkoFM_6XeSlhedGc3NGES72uc-MA1I3ZH9H_u033KACgJzJERUUIXr2ivOSvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65897" target="_blank">📅 01:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65896">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
صداوسیما:
شنیده شدن صدای دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65896" target="_blank">📅 01:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65895">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gky1TJyWy5eq8yGp4pHLCf6OCNoEnl9CvMwb7UkhNhL0Q7hMZtztpuwRlLYGl_l72UTdjkXWX8UVHwikDxYWTKCvOj07S7TljdMTXDixQtjWRL1GKOtQPsxfLr5ftvEsj2aWKp7yKdFrwoBWvX5wqsjME-8_N-l0cVGjPhGIfFxI-Uxle-bT1AUd7f7cv0DMs2IpyDAI-W_aVeC9uiyrw2RkTSDxEg4V6cuI3kreCtnCcNnRxHLnEZylTRRRP0J-zNxLN1GgREmQq607yYTUxXHUL-U-MYY2SFl3tpJ60I5FB8zxZ6ULTRcodTJXpa5vnzOo-YObrb122VOheCY0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام کد اضطراری یک F35 در آسمان امارات
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65895" target="_blank">📅 01:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65894">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دیگه نمی‌زنن
😭
#hjAly‌</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65894" target="_blank">📅 01:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65893">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
فعالیت سوخت رسان های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65893" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65892">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
مهر:
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65892" target="_blank">📅 01:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65891">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
گزارش هایی تایید نشده از انفجار در گناوه
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65891" target="_blank">📅 01:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65890">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر :
منابع محلی در سیریک صدای انفجار شنیده اند اما هنوز علت این انفجار ها مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65890" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65889">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHdissTopG0utOckYk_B0-Vtgy5kL0pFTK0wTInAM2S7j5HtICjx8jKneN03y9yXA-0zMoVCNUzv8UddIOqGqjD15OhnxWp2ObkY-0FeWMuZhtgzRkyYr8Rod1Ydss5TYs687CWV8UoO4PlNQNm4IqeNP0yoGg-sQ1nOk66TeNNFMNncxKRYfkzwNXL9g0YSyZivk58ax9daIDXvgyKOOqgOkqy9WMphJ559y4fnHovBBULrv9PeKvtiKJp20CzYRFcSk6KRCy0sxLgvI4_BUcdoyRJjhoQaXRQaUxPPsu9HgEITVYrVlsobluNJ3AEepcbfD4g4LvR5gf_YLxRPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
تنها یک پست از ترامپ امروز 1.3 تریلیون دلار به ارزش بازار سهام ایالات متحده اضافه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65889" target="_blank">📅 00:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65888">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐌𝐈𝐑 𝐌𝐀𝐒𝐎𝐔𝐃</strong></div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65888" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65887">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما به نقل از سخنگوی وزارت خارجه:
قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد.
مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65887" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65886">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-ywlq1VuWzbRLie_5klLb2fB5lGAqHgeZj2q94Z3sehcLL1jYEylfY8r3cAg50UaI4Y1hNrawwmnIyNqBz2qeh4BKBrXNWxDHWR9ipmjRVbtQNa5IziHVfnIBFB-SLQ6dq592YFvkEdoDVPWL6LHFWKehXb3KF_xbCSZeMW4niszmHuAloqTYnZgtT7rR5TWMJIgfPFFo1_kuzXAg3gZUnA0-TR4aGTT9TUuYJl8TORYB6KY1ptbOw71Z6N5aM4ET7XhF0mSU3aWRDpwf17mggk-8zE-MRlH59acRe6DvBMbFAYbNdUO6UAIGFqqa_u-u7RC0037N3X-9tlKDmLtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:   رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد. اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65886" target="_blank">📅 23:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65885">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65885" target="_blank">📅 23:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65884">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
دفتر نتانیاهو:
رئیس جمهور ترامپ با نخست وزیر نتانیاهو در مورد نهایی شدن یادداشت تفاهم با ایران برای ورود به مذاکرات صحبت کرد.
اگرچه اسرائیل طرف این یادداشت تفاهم نیست،نخست وزیر از تعهد رئیس جمهور ترامپ برای اطمینان از اینکه توافق نهایی که در پایان مذاکرات شامل حذف مواد غنی شده،برچیدن زیرساخت‌های غنی سازی،محدودیت تولید و برد موشک و توقف حمایت ایران از گروه‌های تروریستی وابسته به آن در منطقه باشد، ابراز قدردانی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65884" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65883">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: بعد از توافق سریع محاصره رو بر می‌دارم
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65883" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65882">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
رهبر جمهوری اسلامی با امضای یک توافق موافقت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65882" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65881">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛ نورالدین الدغیر خبرنگار الجزیره در تهران:
دیگر همه چیز قطعی و تمام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65881" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65880">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65880" target="_blank">📅 23:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65879">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=ejDJ0a3zMXRy8fRQu_HMGfv-w6ebfh8C5YV6IT04LuWXOH-MWiWzc4D6Aw0b1TXcEDqkj3YnClDdpfGfgJbZTHnPZw6NpJQlFLfx616v7L-7oiGp6aQptKF_xYIuPXNoBeWcD6FRCgaBcGNowIrZTDXyovUOxyR_c7lLsxrlgq2Vz7igMwD_BmrgCu83cwemO_HESpgWPj3auQyNoK1SK4Zn3h3ilHT2fabFIkJ0oy0qLnrWb5mveRB9DqLfzFkCTLI2Hi6btazo4Hin-b0A_dfdsZvSAjfn4fkHeLDae8EXP544QFwEm_UmLAWzdgKb9WfZmZ7N4z-K1QJIJl5DFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ca9d87d.mp4?token=ejDJ0a3zMXRy8fRQu_HMGfv-w6ebfh8C5YV6IT04LuWXOH-MWiWzc4D6Aw0b1TXcEDqkj3YnClDdpfGfgJbZTHnPZw6NpJQlFLfx616v7L-7oiGp6aQptKF_xYIuPXNoBeWcD6FRCgaBcGNowIrZTDXyovUOxyR_c7lLsxrlgq2Vz7igMwD_BmrgCu83cwemO_HESpgWPj3auQyNoK1SK4Zn3h3ilHT2fabFIkJ0oy0qLnrWb5mveRB9DqLfzFkCTLI2Hi6btazo4Hin-b0A_dfdsZvSAjfn4fkHeLDae8EXP544QFwEm_UmLAWzdgKb9WfZmZ7N4z-K1QJIJl5DFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
🇮🇷
#فوووری
: ترامپ: به من اطلاع داده‌اند که رهبر ایران توافق صلح را تایید کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65879" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65878">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=tV8ONrSJbcRdtY9RVkuVIGpy2UM3OKswBsE9clNze1D2WAva3xuesMju8nUaaOP_8o6MhfxxiHohavovCQjjY41CGPceGEoJmc2DOWHhVvRHaMXmc3FawDK-2svXzCMVHe8UR1LXOLV2EZdN74GQiWjgxQ5IzOeahW10-fBjZfxbZaLRGXdRPt-OLtAAPPbNjkvE39_vYyCOXdin2ASqAR_6OjOoZQ6X5mfp8LXitOW4UGJX6ZvTqjpS4X1-20ADTPow_MuX9M1KGMQndUVG7iZmJKaURafjHz9czqLgWuAQMuDA7qtxsDzz3e8eenD459FoJeuCHUBzUXcrU6ze2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1ce54a8a4.mp4?token=tV8ONrSJbcRdtY9RVkuVIGpy2UM3OKswBsE9clNze1D2WAva3xuesMju8nUaaOP_8o6MhfxxiHohavovCQjjY41CGPceGEoJmc2DOWHhVvRHaMXmc3FawDK-2svXzCMVHe8UR1LXOLV2EZdN74GQiWjgxQ5IzOeahW10-fBjZfxbZaLRGXdRPt-OLtAAPPbNjkvE39_vYyCOXdin2ASqAR_6OjOoZQ6X5mfp8LXitOW4UGJX6ZvTqjpS4X1-20ADTPow_MuX9M1KGMQndUVG7iZmJKaURafjHz9czqLgWuAQMuDA7qtxsDzz3e8eenD459FoJeuCHUBzUXcrU6ze2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرِ واشنگتن #hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65878" target="_blank">📅 23:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65877">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
منابع شبکه العربیه: طبق توافق، آمریکا تحریم‌ها را کاهش می‌دهد و محاصره را برمی‌دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65877" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65876">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeD7O-8w8N31NIvvblvnVvYgzb5K_zT9LGSWFNaEXq1vDiAOF9ugY626k9Wu3PyjvU8TAskAiQ1N18byfFK3ePhhyCVsc2N2thZ3dOvfKFwC58LLRYyk1HWDr9a8EmreVsgnLUlknC5qecMgTpYhX3AFPhNlSFTufQCLbpMAVyq3HOj1pjIVpx1GdS3ZNh_eZli2Dg_TjoTH7mRfLi0WaA4xBS0mu9dkvvwCK6OcPc1NJSXVZHc4UFKXey2ZirUePlWkFJORp2804-oW6IQvuO1cxabn5jY4EnLbWIhBkBfCAhIxh_0LDGXp_8nsERxMclqgeIJ5CRGUOoZvlf1xXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیرِ واشنگتن
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65876" target="_blank">📅 23:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65875">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=tre8zgbon2Nsu6WF86LsbR2uFKTEc0bKC0wS15uURS-2RjTw1UTlc6hLQgYyPX1esRu8fcNQUwnn4EUfoWHxZePioG_3ywPMfvBSC_cLbLxxOylJAo7xAwji0W7KzzYsjlZmXuki8PguaAxrMUNskUauIwGMv_qllk3p3uN6LwthzQ4OaFq1LzJ5Wi8a4tqZta0FqbABdQlscClYO7HlhyU6j_rT8Oy-XulKO_AaLmcscC463zJFu6clEa6bxNpmXH4goksmojtJAPsUXDkiIClHV0YhavZaG6oETY7OvkZ_CGMB1YIWOdqoGXBHFlK_3_Rg0CB27nnDDvVFuHBYD39wtfOW5jgOXVVfL6ZI7cWbiE2jipZi6K70yeYA_Cu3A4KNrrAnXTbmB9sJq2EMP6IiwASLOoEUZ9s6XwbYMTKWqxzABjobhM2uHADObjd3o1Ju47BcVCcYzf8l0XwqBJu00Vzp7Jp2frgy9HfPzUP2sTmIDAJPCWFLlwhZP7mCEkIR_EZAAkLvG7GB4MjJS0GT0LON1HbJPw6QuejqscSsCo120Ilb-CxtFtE7Hhys6_vxDLuW4VhlVukNBL2BcNbUJZVpzieEsUiW1g6FlH-NMpBBmW3VmkUgE00f9UJJvV8MhFeHxctY4tPPKIbNrcy2tmIqNwYtGFyxmwQkkBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e445beba9.mp4?token=tre8zgbon2Nsu6WF86LsbR2uFKTEc0bKC0wS15uURS-2RjTw1UTlc6hLQgYyPX1esRu8fcNQUwnn4EUfoWHxZePioG_3ywPMfvBSC_cLbLxxOylJAo7xAwji0W7KzzYsjlZmXuki8PguaAxrMUNskUauIwGMv_qllk3p3uN6LwthzQ4OaFq1LzJ5Wi8a4tqZta0FqbABdQlscClYO7HlhyU6j_rT8Oy-XulKO_AaLmcscC463zJFu6clEa6bxNpmXH4goksmojtJAPsUXDkiIClHV0YhavZaG6oETY7OvkZ_CGMB1YIWOdqoGXBHFlK_3_Rg0CB27nnDDvVFuHBYD39wtfOW5jgOXVVfL6ZI7cWbiE2jipZi6K70yeYA_Cu3A4KNrrAnXTbmB9sJq2EMP6IiwASLOoEUZ9s6XwbYMTKWqxzABjobhM2uHADObjd3o1Ju47BcVCcYzf8l0XwqBJu00Vzp7Jp2frgy9HfPzUP2sTmIDAJPCWFLlwhZP7mCEkIR_EZAAkLvG7GB4MjJS0GT0LON1HbJPw6QuejqscSsCo120Ilb-CxtFtE7Hhys6_vxDLuW4VhlVukNBL2BcNbUJZVpzieEsUiW1g6FlH-NMpBBmW3VmkUgE00f9UJJvV8MhFeHxctY4tPPKIbNrcy2tmIqNwYtGFyxmwQkkBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره جمهوري اسلامي:
ما توافقی داریم که ایران هرگز سلاح هسته‌ای نخواهد داشت، که این کل هدفی بود که باید از آن عبور کنیم تا به این برسیم.
اما ما به زودی امضایی داریم و اسناد تقریباً در شکل نهایی هستند. بنابراین خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65875" target="_blank">📅 23:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65874">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
دونالد ترامپ: در مراسم امضای توافق حضور نخواهم داشت و جی‌دی‌ونس قرار است عازم اروپا شود  @News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65874" target="_blank">📅 23:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65873">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk3M1eo74WeX9MNGjv0D3GWo8lGf8H2OzAIe4ZG6M9vuCd0SLGplVATtqh79xlU8OO-NmVpEIwiW_cS6YKNUuoe37n6qYABui5_EbInU-dv7sXveIrM-KsmGtoMPY07CUHIyL3Y589fhkq4ypjz3j0jmWIIclF7gIu5-Jd651w_6lKHuF76aafhpXgjzDkbgE1YEF28_nuf5PUwCFZQ2MOoezWVIGntLTIKOjdjVBvrnbm9kHYFV1tbnJO-hUpss8hKg7jmvmlb1bct7B4Eu9C_CAPnYTOJ4pO-yrn3w0u4qdeVJiwtQLlfopWGdBKVHAeB_rgknbzZVTSLO38SHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره داش آخوند های حرومی تسلیم شدند هفته دیگه جشن آزادیه
🤡
🤡
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65873" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65872">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/65872" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65871">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ترامپ: توافق با ایران بزودی در اروپا امضا می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65871" target="_blank">📅 23:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65870">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
دفتر امیر قطر: تمامی کشورهای منطقه در خصوص تفاهم ایران و آمریکا رضایت دارند
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65870" target="_blank">📅 23:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65869">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmrGv7ODa_DZAxnEpMfMug5d1pEjGtS7lhRZSbJtITTf2sYkTGRJj8Wzc5nvI3kwW7yPyIZyj1TU9dKBUWE_YEDM4TUqePiCzPU-coPM8KSI_sCG56FQbtJ_wGcn2cXexhkreWgIVABj4Kyiy4vfLpoQ0LyrPC38cX5JmTCrgw05uuVnSRdd79DeGsBPBYyhHOfnrdTTIWsfsQpywi5AAFWTqDtGLe9gElwg_P-B7ldCCGrRAk0-8l-En_ZVC68zjxDhdSOWvQA9vl0I2fl5FYCYArTTN-McCJAGabyGtuzn-M1e4YbUSaOYsLRI7mbz9NEKrR2Ol7EyIehMNYl26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
صد درصد بیمه ویژه مرحله گروهی جام جهانی ۲۰۲۶
🔥
⏩
تا یکشنبه هفتم تیر ماه، روزانه با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های مرحله گروهی جام‌جهانی ۲۰۲۶، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد در هر روز از رقابت‌ها ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین:
🔗
bfrd.link/WCUP1
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
✅
دریافت سرورفیلترشکن اختصاصی
💻
@BetForward</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65869" target="_blank">📅 22:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65868">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
ادعای اکسیوس:
منابع ایرانی امروز به کشورهای منطقه اطلاع دادند که توافق «اصولی» در مورد یادداشت تفاهم حاصل شده است، اما تأیید رهبر انقلاب همچنان لازم است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65868" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65867">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
خبرگزاری حکومتی فارس:
‌ منبع آگاه: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده جمهوری اسلامی ایران به خبرنگار فارس گفت.
رئیس‌جمهور ایالات متحده ساعتی قبل در پیامی در شبکه اجتماعی تروث سوشال ادعا کرده بود که ایران در عالی‌ترین سطح با متنی برای یادداشت تفاهم اولیه موافقت کرده است.
وی دقایقی بعد در اظهاراتی مشابه خطاب به روزنامه آمریکایی نیویورک‌پست هم گفت که متن مزبور جمع‌بندی شده است.
ادعای ترامپ در حالی مطرح می‌شود که ایران و آمریکا بامداد پنجشنبه یکی از شدیدترین درگیری‌های خود را پس از اعلام آتش‌بس پشت سر گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65867" target="_blank">📅 21:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65866">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
آکسیوس:
به گفته سه منبع آگاه از مذاکرات، قطری‌ها و ایرانی‌ها روز چهارشنبه معتقد بودند که به متن مورد توافقی رسیده‌اند که آمریکا نیز آن را خواهد پذیرفت.
این منابع گفتند که اختلاف‌ها در سه موضوع کلیدی کاهش یافته است:
سازوکار آزادسازی دارایی‌های مسدود شده ایران - مهمترین مسئله برای ایرانی‌ها.
تمهیداتی برای بازگشایی تنگه هرمز در طول دوره آتش‌بس ۶۰ روزه.
چگونگی انجام مذاکرات بر سر برنامه هسته‌ای ایران در طول دوره آتش‌بس ۶۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65866" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65865">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: زمان و مکان امضای توافق بزودی اعلام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65865" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65863">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65863" target="_blank">📅 21:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65862">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(ммd)</strong></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65862" target="_blank">📅 21:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65860">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AAvMhYFGE3-d9l5-sK9k5hWFiQodedQRS34woGmyQJnmWLCwUcAy88Yn8Lz6Hu1LTSXD4PdqI15jsf0kphyJrgCgHIjKxC8YS0s-xQ0gkb89Lotk8TbP9gnjtIhnri7Rv-pAr7rKBSeYJIKIHHIzUOeyICrSpw5VUcVNHRv1QKi416_KTE8WSrLEHW9HHWqrKT2LiyYpyYENofqE3qFwl22Eqty4JOWc5HaVYV41YUHWkiD70TcTFN0zTXyV0nZIn8CiCmO8oc0wNfK65YgDxDDtwKVQkQoZKMxjgHpEQgDQpsE_ei5trxfokfMujPLFKa8NjoYRCIP3_kGxIgKUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QO_kQEHfxogRnil15MTw80tUJLzmYTqYSdfDPoDqRH2KXPerOw6faQZ0ywmzXBHw1aC0P_9byp2p97HLHb6qhOAiTXq7Iowc17T3VXP2XOpqTbYJWmDsCY_i8e5JySw99u53GVICMwxKqZAnYggC92Wk1ljiQ5vMld0yzl0zkRQPLeCGYRvMKqlNIpJcozgEKgxv_csEPJP2uEhYgV2LgYa1NSz6jdxS7IhIkb4EGS9KuMPW8ceYIbCGQJToN2cj4ckPONuLo-6DcSE-LtpYM9duOPn43eSVqgWCrnO5s-tTMknzxdJI6N4lvHH8MvchAt5XbfO7PN-p5LY8quHMEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
اجرای شکیرا در مراسم افتتاحیه جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65860" target="_blank">📅 21:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65859">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmXmqJynf1Y0eM6JGLYKcXoSKBN6VsyoczHicxCQXYjrhRfVv5a-uxLSHYd4TKDAAg28xZ3dZ6xchyDQnH8F5p52ZrS99Oil1FggULjKJImy6K3hKL70UtyXgo5629aPxNZILv0NLvD3i_DkziByUmKB7OfG6-rrf1MSDEbbFfF4u5flcohMruDlqskKRvePB3GJAKEWefbBt-hvdR069Toxh-azzt2EGleaFUSITci5KunDerPheA_Q9rH89FTxiElOvnV-LwOxGDK8o4VF8TZifdS0ckF4A_EmdfMsra8S82gfWkGlpb5LxHvQqjF1JraJtZc-2KAJ7dzQbRCpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت سپی هست داداشمون
که در تمام سه ماهِ جنگ vpn هات نیوز رو برای پوشش اخبار تامین کرد، هواشو داشته باشید و می‌تونید از داخل سایت بطور زنده افتتاحیه رو ببنید فقط کافیه یه ورد بزنید
🔴
لینک سایت
http://Chosefil.com
🔤
لینک کانال
@officialChosefil
#hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65859" target="_blank">📅 21:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65858">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ=حرومیِ کاکولدزاده #hjAly‌</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65858" target="_blank">📅 21:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65857">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ماشالااا تراااااامپ شیردل
😤
#hjAly‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65857" target="_blank">📅 21:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65856">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1P0M5YrysRISdCjwemCpV0cB3-2-WP2WOSrRB1t4Vlp2IJu7AHHXsNV80S4Hl4tF2zE15NZBVKR5sY4Q6a2Qp1u_KqNoFh_o95FCIIx4feDQ_upY5-298sPHYTbiVu7Y34K-yGG1k2Wui28PX-qdNCI0X66jIApYfrmSpPfcTfEfu_yPPc5ognhzaC4qUM9Ql9BdjlNhhSHyhGnlZ4N_mspVVRbJ6A2vDlWPB_h3ba4WogmqrK-yIMkj62bYm4J6v0EZp5SzDoJumXic7H65DmkBQsrbZaGcWQ6LPezMFlC9seZMpl5IyWcMU1AnCFVvtcy9E9_GxjVtgYA_lKWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
با توجه به اینکه مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایرانیان برده شده و تایید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی شده امشب علیه ایران را لغو کردم.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات فراوان، توسط تمام طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات متحده عربی، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران، تایید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل و با اثر باقی خواهد ماند
زمان و مکان امضا به زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65856" target="_blank">📅 21:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65855">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
#فورییی
؛ترامپ:
حملات و بمباران های برنامه ریزی شده عصر امروز علیه ایران را لغو کردم
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65855" target="_blank">📅 21:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65854">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
علی‌عبداللهی فرمانده قرارگاه مرکزی خاتم‌الانبیا: صادرات نفت و گاز یا برای همه خواهد بود یا هیچکس. ترامپ اگر خریت کند تمام منافع و منابع نفتی و انرژی منطقه را با دستور قاطع پودر می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65854" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65853">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=ZRjRkchEVaslN_TBPuWZNwbuVcDxWJzpjztDTF2hXqLEIq8B3jcVgWQFW6T61c_XHJDGlOqA1L1B9jdOK3W1xH--vZEbyCDiMoH8xA_G6u2cUNZ1WFK_U9srDDpqtLlMAeS4OOnAfNSHhAmNY7tDwcnjgMxUHFeynKDcgpVHHBpikKPNeSUj8qq9QA1JuriUoVi78F8qcEgEFBCdoygWp6uSfrSAMzZmr-q6fv7uy59DMd2BpGJitPWKJnKPdxUgnorO8QJ1aCuTV45DK6ihZ-24LB7rQ9g9M_o7TCCsh3xF-bUdpDZ3Pzqzg4CMkHndDt80puo6wEBxKzV8Gut72A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7e36d42b7.mp4?token=ZRjRkchEVaslN_TBPuWZNwbuVcDxWJzpjztDTF2hXqLEIq8B3jcVgWQFW6T61c_XHJDGlOqA1L1B9jdOK3W1xH--vZEbyCDiMoH8xA_G6u2cUNZ1WFK_U9srDDpqtLlMAeS4OOnAfNSHhAmNY7tDwcnjgMxUHFeynKDcgpVHHBpikKPNeSUj8qq9QA1JuriUoVi78F8qcEgEFBCdoygWp6uSfrSAMzZmr-q6fv7uy59DMd2BpGJitPWKJnKPdxUgnorO8QJ1aCuTV45DK6ihZ-24LB7rQ9g9M_o7TCCsh3xF-bUdpDZ3Pzqzg4CMkHndDt80puo6wEBxKzV8Gut72A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
تهدید وزیر خارکمبه علوم: اون دانشجویانی که پرچم پهلوی گرفتن تو دست و پرچم جمهوری اسلامیو اتیش زدن تحت تعقیبن قراره مجازات و اخراج بشن
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65853" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65852">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgondCb9_c90edEXQUS0574Kg6uZXgmn-fflSteDx3hv05Rxqh7t7_TLfOIRShuhY5xgQuKKERupZQvIUC0sPA4i7MasfEcIWYC0WAOUUMejDnZ-M4SASMXlz6Lijjpz0rz-7RWK6Pe3Q79Nz_zOBllulDatfgbOF_sX-Xa4sEGMu9sLNDqt5J0ARccrc5TU7Cr4DZm2JREB0Va7rgPt4dvAFRorojUR6s8-37Rj_gZTdO-4n7Yi-okgVRYDi4JdyPcOTV-yNfjWw4MeM8gGF64joGs_RTTFcRidmfndsOhXJ09MGZkSG63p7wEGojEFDEDaPOVKro--P4CN8MX41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قالیباف:
استراتژی‌های اشتباه و تصمیمات عجولانه، کل اوضاع را به سمت بدتر شدن تغییر می‌دهد، زیرساخت‌های انرژی و بازارها را منفجر می‌کند و باتلاقی بی‌پایان ایجاد می‌کند که سال‌ها در آن گیر خواهید کرد.
شما ایران متفاوتی را خواهید دید.
زارت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65852" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg-FyRUa9OBZa8jEAYGXXu-S2it9ckfk4vMFplydSVjLdWbV2kpYnbwLiSAXNkg6ibvHxhuO2IMPQGLk1em2zKQSZGJhZLosOu0K1GxFI2cDeE-gr_v80aR2P7Ol9iH7_pIPgvekSCDXF8P-lznvXzT6HOlxoZEm_A7kMMcV_cnMx9JvoX0Y7u9HS4WCXgFqTIUUftj0SforYpYPdYRN6a7CfZMoohaQhNuK6RDurjitHUNvlJYvNUtcCznur5KI-Csjak8bGu16Wg9CjUqT0SJd9xlEHxw54j9vvx9QBDl8v-EBEproKRfKWYGoqGQGoOAueiwi7Ll9mM85AnFJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
به‌روزرسانی عملیات در لبنان:
سربازان ارتش اسرائیل فعالیت‌های خود را برای دستیابی به کنترل عملیاتی و پاکسازی منطقه شمال رودخانه سلوکی در امتداد خط دفاعی مقدم به پایان رساندند.
منطقه رودخانه سلوکی توسط حزب‌الله به عنوان مکانی اصلی برای عملیات پهپادهای انفجاری و حملات غیرمستقیم علیه سربازان ارتش اسرائیل استفاده شده است.
این نیروها صدها سازه تروریستی را منهدم و بیش از ۵۰ تروریست را از بین بردند. علاوه بر این، چندین سلاح از جمله دستگاه‌های انفجاری، موشک‌های ضد تانک و موشک‌اندازهای ضد تانک کشف و ضبط شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65851" target="_blank">📅 19:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65850">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRG_KCFAlgJ0s6aft2dZJIHu61r31_nNaScwOt-DMhuEkutbzFMY6PCffL7Tk8G-FdUp6lpO99_sl_Ie0bYt0SJX59mlA0uzHOiIjucERddIYvg7mWVKgs8dAs0HuSSGxUjyFttMD5uNKqaECSvY1GCh3_tNchGEJCmVWlNdqltAQZiGoTUvTiEpY9RaKpmb2IOhHrzkQznlAq5VHYMa_hl0Axdm2zm--FaGYq1-QFsXzPrq8By-OgmTSvhLa1S7_QxXsX-z_UgQCzymc_TxxtOtBJ4uu4AHTkzcIh53mQo01DfREqNQq7MURWUfQSwa-6fq5cthaKUCrnJQWFcO4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پست جدید سنتکام:
تنگه هرمز همچنان برای عبور و مرور باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65850" target="_blank">📅 19:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65849">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
الحدث: ترکیه، مصر، پاکستان، عربستان سعودی و قطر قراره جلسه‌ای فوری برای جلوگیری از شعله‌ور شدن جنگ میان ایران و آمریکا و پیدا کردن راهی برای توافق بین این دو کشور، تشکیل بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65849" target="_blank">📅 19:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65848">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
جمعیت هلال‌احمر اعلام کرد که در پی خطرات احتمالی حملات امشب، در آمادگی سطح بالا و کامل قرار دارد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65848" target="_blank">📅 18:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65847">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVI6Qz-Dtgc4bM2-Ka0u2RSINlDLOXS0cfvtLKa8S-qoR5w8kumOxktF8oK2h2xeKncIGp0ASPshaQRF5jCybHZyKI0sAwVjTvz4pro4yCsuowGtTz6aPQwVgRr6Bqnx4u-B_xQawyY6_CPZi3jjwTg9PrGlrLQKygVo-3sXHmaVehVhdfUYII9iYU_Md2LCV27sW3eUQARcNKT-H0QkpgJRZ_eldIUiqb9PJQSXT_Ej9abxtCpVC3Cdvhhq7NNL6DUZnZaVZ8PBEHREvoprwYTD1yBFBs5zRpd5uIzxuNXn9__5ZGyA-fgl7bDL5JEjPuP0v1bMPhMsMlorcJG6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست جدید ترامپ در تروث سوشیال
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65847" target="_blank">📅 18:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65846">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/65846" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65846" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65845">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1WZ4AFsm1Gzxkd3ftQ8sQoFMydlj8Pb03aqHlUL6854FAxOGCIovaexTajRmYn1rrbzJCsq8R51amhNKjVHH9MojbTy68GSCQRbd8iO7n9QrOOdm1DsPRhML7epupkXfaMCxqpwd4G6_QiiAqGvtdsTrOD_Y8HOD_x1tbYh4BMzUgw5R8uc4a4BA3gbNi1ucF9qv_e2bmMJrMdHOhw_Jm_nWScPUOsCl449ABC-737DPxscUYa7JcquWKTxlLV_ezZPOwLV26pOwqvIT-jZkmo9OUa-Nc_EaWIuLrPxOZxjUGgdnY9jrOjeyYw_fbdiNmJXQzJb5X_5iWO8LkZayQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/65845" target="_blank">📅 18:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65844">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14bcfc7050.mp4?token=NCIih55tUWCz-EncUbR_xBz3ogWJHzEwJBpoQecNDiEddNEEbyBgHdLPW7Y1-lGJpjTmylDJylN7-b1ItFCZ0upUPRJcDcIvlxOyiZP2TcmHjKrGK8zD85vS6n1fGBgXyAi6sZkZSjAwBbUzcFE0lR8gXYK7e81QTGVN4Gz8lYK6Nj_6SM_1i3uaXZaFKYK-beSpgcE57X1K8GoQ0ZOQIMZ58jCspObptnFy6y1JhiiOGFJCoK8e5Dj40i8ygaWRRxGUvVRNUUtzjNlUr0_qJIAI0RYKylEpjzcrlO0HdkLJ3jYeKTYJWsRlqKPiSeKn1SnJHRfsTKVdFjtc0aNKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14bcfc7050.mp4?token=NCIih55tUWCz-EncUbR_xBz3ogWJHzEwJBpoQecNDiEddNEEbyBgHdLPW7Y1-lGJpjTmylDJylN7-b1ItFCZ0upUPRJcDcIvlxOyiZP2TcmHjKrGK8zD85vS6n1fGBgXyAi6sZkZSjAwBbUzcFE0lR8gXYK7e81QTGVN4Gz8lYK6Nj_6SM_1i3uaXZaFKYK-beSpgcE57X1K8GoQ0ZOQIMZ58jCspObptnFy6y1JhiiOGFJCoK8e5Dj40i8ygaWRRxGUvVRNUUtzjNlUr0_qJIAI0RYKylEpjzcrlO0HdkLJ3jYeKTYJWsRlqKPiSeKn1SnJHRfsTKVdFjtc0aNKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
'لحظه انفجار حمله حدود ۴ صبح به
پیشوا
در  تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65844" target="_blank">📅 18:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65843">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPEziXIxRaSh9wI2Tm9AGyU6_JRNiP51CfdmsCNftkoRp15fE_MJBqqXpnTJU4pYG4iPKyELlY0c1zmt3YEtIk97q5kymscYIP8ZIVKAMNjSE4JJ1TYMS3aoi9r0w0XefGEKqBVmY3EO1mnpkA89BJKS5KqzwjWhtf81ua-D0ub6JCMlUnpyyM30nOAPHLZxLtsG588dXVtFl6kn2VpwBUQrRk8_qsrKXdAkCiVVzfESkv4d1FI3GoCLyBk8PeAP2pDvJg7cFgl5gFdA4IhGZSy4AsHB7MNCJ3h83lN4_6YoAXy2KZZpT274UbA4owuSSR5EnshUx0z3tjTsZAjAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست جدید حساب کاخ سفید:
«رئیس جمهور ترامپ همه کارت ها را در دست دارد»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65843" target="_blank">📅 18:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65842">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
اسکات بسنت، وزیر خزانه داری آمریکا:
رژیم ایران در بازی مجموع صفر که در حال انجام آن است شکست خواهد خورد.
هر آسیبی که به متحدان ما در خلیج(فارس)وارد کند با وجوه استخراج شده از حساب های ایرانی جبران خواهد شد.
هر عوارضی که به مقامات تنگه خلیج(فارس)پرداخت شود با وجوه استخراج شده از حساب های آنها جبران خواهد شد.
هر حمله ای که ایران راه اندازی کند، تنها پیامد های مالی و اقتصادی را که با آن روبرو است عمیق تر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65842" target="_blank">📅 17:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65841">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCf-omDvTiAqeXt8o0GbjMsWwcfGXomm4qM0ST9beYLcffwFZeRknLdO-AG9ZohxuFdebOrfvqjBX4u1YRBXh3rNDpNG-jHt2_e35VPXBmWVn6Gd8GwQQYSObe6SSlwM6zZ4ldvaQVT-K5uAnoC4M5xUlhfu7G1N9y3DrD762d92BRiVcM8hElZMh_V3aHQJsBN48d2-SI2gQKJAUnnlepP2P0lghaZYQjOetEYB4QPAv6vkUlPlprEQYqBIXe18J9fis2GTTGDgJqzkHpNVaIEFPI3HDaBe77rz0n9nIGQJVp52EUGF7WG3-w0QQoqbFE9_ZJIG1Pvculr4mqpZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
ایالات متحده امشب به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمام اشکال دیگر دفاع آن، به همراه بخش عمده‌ای از توانایی تهاجمی‌اش، از بین رفته است!) ضربه بسیار سختی خواهد زد.
در مقطعی در آینده‌ای نه چندان دور، ما جزیره خارک و سایر نقاط زیرساخت نفتی را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آنها را به دست خواهیم گرفت، دقیقاً مانند کاری که با ونزوئلا انجام دادیم، که به طرز درخشانی هم برای ونزوئلا و هم برای ایالات متحده آمریکا نتیجه می‌دهد.
از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65841" target="_blank">📅 17:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65840">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ارسال سلاح از طریق کردها:
ما در واقع به آن‌ها سلاح فرستادیم و صادقانه بگویم از کردها بسیار ناامید شدیم. کردها ما را ناامید کردند.
من با این تصمیم مخالف بودم. می‌دانید، من می‌گفتم، «نه، باور ندارم که آن‌ها سلاح‌ها را تحویل دهند.
فکر می‌کنم آن‌ها سلاح‌ها را برای خود نگه داشتند. فکر می‌کنم این یک ننگ است. اما من این را به یاد خواهم سپرد، کردها. من این را به یاد خواهم سپرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65840" target="_blank">📅 17:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65839">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
جی دی ونس درباره نتانیاهو:
نتانیاهو کشوری را اداره می‌کند که به‌وضوح یک شریک بسیار نزدیک ایالات متحده است.
اما حتی وقتی ما شرکای نزدیک بوده‌ایم، گاهی اوقات منافع ما کاملاً همسو است و گاهی اوقات منافع ما ناهمسو است.
نتانیاهو به‌شدت منافع کشور خود را تأکید می‌کند. گاهی این بدان معناست که ما در یک صفحه هستیم و گاهی بدان معناست که نیستیم.
آن‌ها به‌عنوان یک شریک بزرگ در بسیاری از راه‌ها بوده‌اند، اما ما همچنین باید بر آنچه در بهترین منافع آمریکاست تمرکز کنیم. و جایی که این منافع منحرف می‌شود، متأسفانه برای اسرائیلی‌ها باید سمت مردم آمریکایی را انتخاب کنیم، که همیشه این کار را می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65839" target="_blank">📅 16:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromromo heidary</strong></div>
<div class="tg-text">اسپویل
فیلد مارشال عاصم منیر، پادشاهان عرب به ویژه محمد بن سلمان از من خواستند که به دیپلماسی فرصت بدم و ایرانیا هم از من خواستن تا فرصت نهایی رو بهشون بدم منم گفتم باشه و حملات امشب که قرار بود زیرساخت های ایران رو نابود کنه و جزایر ایران رو از روی نقشه محو کنه متوقف کردم
از توجه شما سپاس گذارم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65838" target="_blank">📅 16:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری از ترامپ: آمریکا امشب حمله بسیار سخت و شدیدی به ایران انجام خواهد داد. ما بزودی جزیره خارک و دیگر نقاط زیرساختی نفتی را تحت کنترل خواهیم گرفت و کنترل کامل بازارهای نفت و گاز آنها را در دست خواهیم گرفت، همان‌طور که با ونزوئلا انجام دادیم  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65837" target="_blank">📅 16:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1LHoKTZwvBFG8hKpIVl8b6ouDaH_0eXTgojUZ3SFe-P6H1BGZxF59StZ8Jk4ewaS9kuERDLoXpAFbMvJ98aEF1YcZ-o49-YOstCheYO78dOD8DZ9UW-1jXZ6uWBzDmFoncbQKDNDw-Uh0TUWMC-hEWUQ5gnm1mYLrMAjdPy7ZCQOIOetCHlnsyP5PwnAqGkW8zfluBPzhb3hEqP208qClxWJiCYVM8U_Gu1v0J0CiiK-fq-rTPjU-XPOpzSH24vopdZq5F-fGUrVHZwfmXj4SZwPikIsDz9I5xb74JjMuyertk_NEGNtBcvhFmIjD9UaJcXh777FVaKvOeK0e6nNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
از ترامپ: آمریکا امشب حمله بسیار سخت و شدیدی به ایران انجام خواهد داد. ما بزودی جزیره خارک و دیگر نقاط زیرساختی نفتی را تحت کنترل خواهیم گرفت و کنترل کامل بازارهای نفت و گاز آنها را در دست خواهیم گرفت، همان‌طور که با ونزوئلا انجام دادیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65836" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65835">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5x0yiieKggwuiJz9eV-2rs8POls13qrLdmRc97TywcDsAEYUkfCVTsJGl-lByYGOCtbQ9Zq4J4fqfOVSe0ph89alobR_WsPHppNLlgKLvL8waf0cEnGbhCn6ucpClsqIY4I7McA5jJIcGC3232ybG2mWhrJCNBhdB8dWuaNvrD8jY-FJgt8XOp8ot8zrTAm_l-DzSbTRjRIrqq4EpRfxnbn-d-71UAzWAhpfrotRLnn7V2R1GEt2AFZmgD2qOCxpAt4hVO7ka_prvxhl1TVGYdzAqLFmZJP45-9O9rFXciDoIdWV5UBhf2dRU_Z3JKKb1tdnIkql0IlcW8mU73fjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایران اینترنشنال:
‏
محسن رضایی، مشاور نظامی مجتبی خامنه‌ای، در شبکه ایکس نوشت: «رییس‌جمهوری از تعادل خارج‌شده آمریکا تصور می‌کند بمب‌ها می‌توانند او را از باتلاقی که خود ساخته نجات دهند، اما موشک‌های جمهوری اسلامی او را بیش از پیش در همان باتلاق فرو خواهند برد.»
او همچنین نوشت آمریکا در برابر انتخابی دشوار قرار دارد.
رضایی افزود: «واشینگتن باید میان پذیرش شروط جمهوری اسلامی و از دست دادن آخرین بقایای اعتبار خود در جهان، یکی را انتخاب کند.»
اظهارات رضایی در حالی مطرح شده است که مقام‌های جمهوری اسلامی بارها بر ادامه پاسخ به اقدامات نظامی آمریکا تاکید کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65835" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65834">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
فاکس نیوز:
«ما آنها را بمباران خواهیم کرد.»
هشدار صریح رئیس جمهور ترامپ به ایران در جریان تماس تلفنی با تری‌یینگست، معاون رئیس جمهور ونس و نمایندگان ویژه استیو ویتکاف و جورد کوشنر از اتاق وضعیت مطرح شد.
دولت معتقد است که ایران همچنان در میز مذاکره تعلل می‌کند، حتی در حالی که نیروهای آمریکایی اهرم نظامی گسترده‌ای را نشان می‌دهند.
پیام ترامپ: ایران حتی نمی‌تواند آسمان کشور خود را کنترل کند. ایالات متحده ۴۹ موشک تاماهاک شلیک کرد که طبق گزارش‌ها برخی از حملات به اهدافی در حدود ۴۰ مایلی خارج از تهران اصابت کردند، در حالی که جت‌های جنگنده مواضعی را در امتداد ساحل جنوب غربی ایران هدف قرار دادند.
در مرکز این بن‌بست، یک توافق پیشنهادی وجود دارد که تنگه هرمز را بازگشایی کرده و محدودیت‌هایی را بر برنامه هسته‌ای ایران اعمال می‌کند. اکنون سوال این است که آیا تهران قبل از تشدید بیشتر فشارها، به میز مذاکره می‌آید یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65834" target="_blank">📅 15:32 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
