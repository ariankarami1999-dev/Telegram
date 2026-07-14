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
<img src="https://cdn5.telesco.pe/file/vbDUPXRmE4AEGMmclH3iI-z3NYy4UU8ToIOq0ntwZy7gCrB49NE9oF1HjSe0ChxWbaFi_Jn4gVQIO4R8SebIFVFYv358Gpk66OD1FNyAsbLFTXQZlmMclvZQGKMRKbCUvpIPb8OXYwOldAZ-w_1eXE9vx3hmASntZOYCgOLSlEaZSc20v8aoFpTSEzvL7GhdevVxzhkk2rWrjwoQCOXuxz5XTGqpLNrDuNZGV_-Ra54ydJ_UZiZDUsDKEntIlYCtis_Y4-W8opPPnYzNAPmcPZZWLK-TjfyCbDHr6Dwtwibio0t45JVYgJy6w0ClQMG7QLy34yKTzkJbcPPp7-cwEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 578K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 00:04:59</div>
<hr>

<div class="tg-post" id="msg-100160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اولیسه امشب جوری بازی کرد که بایرن‌مونیخ اسمشو بزنه دیوار مهربانی</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/100160" target="_blank">📅 00:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اولیسه و دینیه رفتن تئو و چرکی اومدن</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/100159" target="_blank">📅 00:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زیدان هم بیاری این بازیو نمیبری اقای دشاااااان
🤣
🤣
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/100158" target="_blank">📅 00:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">لوکاس دینیه نمره ۵.۶ رو تا الان گرفته</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/100157" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dcwa7CJyJzXPtNAqfKNO3OVNtpW2M1Bcx2Fj2KZrKNU9ijshxBov4oR3X7JhtZWcEndhDSTlCOaKNsjW7KFaAJzjxwExsTFAdtMoT6bifdisO5n5V3uE8Qs9F6xKB1b4qkA4lmSL0ZYOjBF3b_nrB0pPy1vVE1EOx-P7cCh2csUHJ5qG7zlm9RN6y2-vEZosXIQ7ojrYoGckIXgDMh3JEnBI2iFk1x5M97dvjrksBRn5Nbq_MVq5ZHcKPZ2a6EeZl9hAxY0i5XPR1arM_aBXV6OfMY4Jnb2qHbMIVNLiFnxB1m6pyGMoh6LQA221ip2aIsdOaWwDBobIpNzIcvFCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🥶
🥶
🥶
تو ۱۹ سالگی ترکووووووووووند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/100156" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100155">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">امباپهههه داشت میزدددد</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/100155" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100154">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/100154" target="_blank">📅 23:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100153">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرانسه این بازی خروس نبوده مرغ بوده</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/100153" target="_blank">📅 23:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100152">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گلللل سوم ولی افساید</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/100152" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100151">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c10bc62198.mp4?token=f-lwMKMH4wl-mOx2tEjPehJf8_WzwEEwAvzD8zGWZK0NQkMR1edXL5t0oAL9pXnc26zrSDNELJ6E_g7-U-zWqOJSCka6oCogciH1vQQ3dy-BLv9DNNypwYaWYy2K5EWBdJHFon6MgIm0CGjdYQ7YqWLQzeN4L9zOIyJQY1sAtj1yC-Rcagg1Mz10H2zvW64hHk-X0-LGbZszyq4gkeyOW5div3oe7GzmKNPhSyFp556BNf4T16LDaNZD8D_F-esIFdzquuNSUrNlydRlNwyFVdq_cbkWEo4qs8FlZlBMa9LV-v_X6BHmYI0BfB72xFfFDullHxniKzK3fFAUdZi9Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c10bc62198.mp4?token=f-lwMKMH4wl-mOx2tEjPehJf8_WzwEEwAvzD8zGWZK0NQkMR1edXL5t0oAL9pXnc26zrSDNELJ6E_g7-U-zWqOJSCka6oCogciH1vQQ3dy-BLv9DNNypwYaWYy2K5EWBdJHFon6MgIm0CGjdYQ7YqWLQzeN4L9zOIyJQY1sAtj1yC-Rcagg1Mz10H2zvW64hHk-X0-LGbZszyq4gkeyOW5div3oe7GzmKNPhSyFp556BNf4T16LDaNZD8D_F-esIFdzquuNSUrNlydRlNwyFVdq_cbkWEo4qs8FlZlBMa9LV-v_X6BHmYI0BfB72xFfFDullHxniKzK3fFAUdZi9Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/100151" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100150">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
خوب این‌ پاراگوئه نیستتتت عزیزاننممممم</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/100150" target="_blank">📅 23:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100149">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پدرو پوووووورووووو</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/100149" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100148">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فرانسنسنسنسنسنسسهههه نگایدیدیدیدیدیدیدمممممم</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/100148" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100147">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چه گلییییی چه کار ترکیبی اییییی</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/100147" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100146">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اسپانیااااااااااا</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/100146" target="_blank">📅 23:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100145">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلللللللللللل دومممم</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/100145" target="_blank">📅 23:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100144">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">داور قشنگ با فرانسه مهربون بوده</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/100144" target="_blank">📅 23:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100143">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آغاز نیمه‌دوم بازی فرانسه و اسپانیا</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/100143" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100142">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ربیو رفت بیرون و کونیه اومد</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/100142" target="_blank">📅 23:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100141">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9XyjXFg_y-04G5-n938kAqPVjQ02UXoho2o013fmXwF1oL4Z06e4DRjCNsrrfhlBi7DDIcDUCGdGndiZV1H_H91H_-YtzLyH2yyYS7RQe-3kdDBUI_BG1Zhk_1r3H3Hv-9lOgD3GbdQasrjaj6yOxHpJNmSOgUWCe9WodIWmMR_2WTzV5cx3DIUNyHLSBBvkt5v98D9EzSJ_GRiy8hV01FiflBHlVb_OCMIhP9dn7Il0XIrm6D_XsiAx-jEYmvhOz_RxQJX6OauHFoIX8N8PEYTJvFsfiUqi4_dV_AN5QuLyCuq9G-4DMtCta7VyMEEUN4zbuKfq_P1hD39Azy76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آمار نیمه‌اول بازی اسپانیا و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/100141" target="_blank">📅 23:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100140">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فرانسه نیمه‌دوم بازیو برمیگردونه؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/100140" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100139">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOYtd88NHJS8MesGd3skJ9GjEThjK8Bh7JXJSINIU6QlSltatN-PYH9JDDB6NqdGdi8pL-Z6qvRdAjlaQl3ZEpzGmt7H6NqJHeSK6a4DILrrDz5XS1AAQB6GoVgVcyjCsDpK7d0lY4mBQaOJhgmVehmOKcMZLBXblQ04Roc2glj4xSprGYWtI9c6xb4zZ0_f3_ChXB1w__D9zXFu-qKekDsi0jD64LGNf17OZxicrAkxTAtpd2vn5zzVVn5j8nOxgmW79AbH1oaVJ-C6eo1U31n4NTpQOKT6tgEhMGpGrx9LHNx348Y3kqKK9pY9Q42-QEJiGCVSuBq-NZDkYeZUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه نیمه‌دوم بازیو برمیگردونه؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/100139" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100138">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gxH_vOvkdhE7_tknhAhy8OJkDg0obqxphPJzjP4ak1LDxLj8JVxwj2U2pcV1fhC_PAZUf_IzILIoygqM10ny5v5ptA5CQbS8U7BDLWN81KqlaLRKLv3RXMZBU-WCH_3P7pl9GK5qu8AofWHoO7FUUJ7XwnKBpbbbQ1njV4w1vcwuhj_vUYfzflr8MJkupBS8SmcePCVWeGUc2P55AJtnws23bWSZ2S_2mOPvAbleeSho405isl9CjbpAhPXp1-tJMin1n2J_jedEcL5tult-m7JroU557sWrmMuMKRfD08HkDZMxRfEKaPRCKsDggXO2C8K7_jRQ98k7nXRzmFep6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
اولمو امشب تو نقش مسی داره خط هافبک فرانسه رو میگاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/100138" target="_blank">📅 23:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100137">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoBKJ7RHokp7iNXLJQVklA0FH4nEPDm6S7ZfP7yOY9fpSFWHvpzUmQFq4wWJaExTkUj96jgBZhtoEHNDz1gn7AbIVdJyEh76Fh-E-i3UzM0hlKmx_dn_ZN_MKoxg49FLH2qSCVtXrzYSifWN53zxyzMykLA9v2kyaAjNVYmZGdHBZ6DO1G1hjo7reQ1ksPQ8rGdkzwL511GRypwblv5nsBmkUIAgAoJgpT47aKFZtfxwM_BeXT7jpcY_MJL0h8Agb6tM4m2dqmk3rTWMbPswC7YsIbdc1drKVnRzvorianHNcEStarKyeKAqKoXv4MYvCj_NE6A697CMNaLJ7Zkmlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آمار نیمه‌اول بازی اسپانیا و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/100137" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100136">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9ENgZ1Mwc7gHBEyJjONQHET5IrRZUQHFL1iLM3tbywXZoFxggFyRtoMVk5TN3Oy-sPo0jsxiXCf34vXTzf6SpZuRCIJteRP0d7WOSoxNuXSzXDgkE_0P-SPUiTR0zlVogjI7kQyGpRvjaB4NdFfBcadF8RexcD3iBdxf_PtKeUk396YR1ALI_RAKZyjCYXCPNb07DvT357amhFd8Gyi7CmchCUfDcc19EupZdNV4OcbNKp8QIIBdLcsHZwg6SvJkuL55IVJxp4vFSl7IvEV4ozdV6A5qeMd5Inf4VROFLHIyCfYxrSHKEuGDoPjHCT_VkqamDejENQXgE_ir_ftXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
برای اولین بار در جام جهانی 2026، فرانسه در نتیجه بازی عقب افتاده.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/100136" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100135">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f951af3a7c.mp4?token=Ye5yv-oVI2P1TqBbzbY7KgNDEf4IxddS0p2dJOxFqh2TliuiEVJL4T_Ypw7qDHc_iWqwSceSZWCyNgsnLJLFH10F40odXxuUj3BEFAO6XdBN9ije538pEz2aVp95kOLoujnsiE4K97zUT0NzeYP4jCi4cky2saUEGWVM7an0CFXlASIZtZSSAPRNOkvwBbrZYYRoxzj7BwuDeXsCFdrmmqxEqVRbSVbp52l0Ro2IKC_9vRwo3aOCT-enAMvdwWQRVFBzjW49c4BMNRFsEAEtoJvEsE6lYh2D12xYetyiccCOZiF8YIX8sHTx-kdcHCz-GBBa7PYZ0_A-gPP1-ioQZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f951af3a7c.mp4?token=Ye5yv-oVI2P1TqBbzbY7KgNDEf4IxddS0p2dJOxFqh2TliuiEVJL4T_Ypw7qDHc_iWqwSceSZWCyNgsnLJLFH10F40odXxuUj3BEFAO6XdBN9ije538pEz2aVp95kOLoujnsiE4K97zUT0NzeYP4jCi4cky2saUEGWVM7an0CFXlASIZtZSSAPRNOkvwBbrZYYRoxzj7BwuDeXsCFdrmmqxEqVRbSVbp52l0Ro2IKC_9vRwo3aOCT-enAMvdwWQRVFBzjW49c4BMNRFsEAEtoJvEsE6lYh2D12xYetyiccCOZiF8YIX8sHTx-kdcHCz-GBBa7PYZ0_A-gPP1-ioQZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت اسپانیا تو بازی امشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/100135" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100133">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
پایان نیمه اول؛ اسپانیا 1 فرانسه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/100133" target="_blank">📅 23:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100132">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100132" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100131">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اولیسه خیلی بد بوده این نیمه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100131" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100130">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">داور گل کشیده؟؟</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100130" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100129">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خطای خووووش جا برای فرانسه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100129" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100128">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خطای خووووش جا برای فرانسه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100128" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100127">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چه حرکتی زد سیمون</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100127" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100126">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-lUnNS8JkUH72wH9RwXONEoGUQAtXFpo7yHr9if9L_4hUSI5lkvtLgtfTixk6T8-yH2NWk6zCN2OAfQO_nHsGSEul9q55KuhU0z17DPFIl20Q6RX0mUtEMqPkkIzSEGp8ZEGDIEMSdVnE2FGyStdzTlB9WgxerHxhBBT3t_mxOztNq8hbxuffZ93BHUzsuHYIyzQPvAsMMOzFRFmIYAMZwxhOyjcUmtxLMEr-kB2D5QDTF1OykOknYG_p2Wttvms2au8bgupy5uHMQ4BhtLk4UAGnZGxtTOfwQWc7v8A6pIKTRO2d6qfxHVXLamfgd00Vpvc_PY50JCgAUU1wB6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
🥶
🥶
🫣</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100126" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100125">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">امباپه همچنان تو آفسایده</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/100125" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100124">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امباپه همچنان تو آفسایده</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100124" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100123">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M47c7NTVwfO_6shz1JdWvFOMMCnEfiCxQGv_3PaPJfP3Ad2sgRK92VoIpr73KOGTNjQuRbNjHxJzIuZTkpaDZDGe-byK1dWR2aDbnlizuyN4PKYhZ0BMje6UsGAr5sh0pdWr1puazAGEKopFHSP3S8fx5EXt-pRnTD2hJzJgvG2BlTtrjIoKZxeR_i7h_Y73hKaOugcWNxiuRo1HWWy_Mra_4KXBij0rVrXaQpQlL1-gFcPFHWjSey3SI9rL4q4TvyUITYSSCOGe95zOj7FyNTBVa5tGrMG1D5AaauEtBABs7Rqd39PlSK3r1S-wU_HQg0jKjovpz6mGGlhrc9JKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری نیمار از وضعیتش:
دختر داشته باشی و وضعیت خونت دیکتاتوری نباشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100123" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100122">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/767e8b3586.mp4?token=BoytFgM8eO0TEEiHEs4NttmvKGVuxPrdhSUWho9rvxuG4uT5_DwQhcxpGn1W9FYWp-Ih93QtNOLh-3SIwz0xWjEyIdnyRR1UkBUPkVJ4Ph5cSLG5fqgPNphZbbk3W7-Aspj0ONyn1eVk2EzICqKvo7maNyUc1Q-GbfgGPmrCJrxV2FMfD_zUUOzOMUH3KAU-gveGz0GlTUTBy2SB0UvNOSxzXJZ0pKf1HuBrbNS5W3ZmZo9mXLpoL7V4PYsXYPxjhNUDcBmE5WUVdI34noA_C1wXOjSamJzvsR82uI90XDTlxtQQMc80-9lWjIXVBHjwItbsp8LZtuoh6ccOCeJktT8WYMAUD6VKQB8KrsBZsdzp-NJWP1_bFo-gqVH-od27jrqaYn1AspX20W-iJRz3ZY_9L2oQB5hyfl_6tHgfKb1PmUVhyFwBShZe6a2ogkMcIWWhs8UmCx4cyxa41ZsRctBt3p-WBGcTlOypVhDm198_8RHO0qqHobW57l-b4AzlHaMpiVY1OcYhh6o3qUdxbGvl0_YzHv_NP4RDU3aEzIyeb88L4s6vBJ1eO36Blq4HRkHS46eGofGaMIMcWD16fpD6Z-qdCFjqiPLg7JGGD7NiTCe4oYZEEtEwztQV2u039ZaAu3ySUiGv5PL6cdxd4Sfe3sr3tjLsT1PgTsW3vPk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/767e8b3586.mp4?token=BoytFgM8eO0TEEiHEs4NttmvKGVuxPrdhSUWho9rvxuG4uT5_DwQhcxpGn1W9FYWp-Ih93QtNOLh-3SIwz0xWjEyIdnyRR1UkBUPkVJ4Ph5cSLG5fqgPNphZbbk3W7-Aspj0ONyn1eVk2EzICqKvo7maNyUc1Q-GbfgGPmrCJrxV2FMfD_zUUOzOMUH3KAU-gveGz0GlTUTBy2SB0UvNOSxzXJZ0pKf1HuBrbNS5W3ZmZo9mXLpoL7V4PYsXYPxjhNUDcBmE5WUVdI34noA_C1wXOjSamJzvsR82uI90XDTlxtQQMc80-9lWjIXVBHjwItbsp8LZtuoh6ccOCeJktT8WYMAUD6VKQB8KrsBZsdzp-NJWP1_bFo-gqVH-od27jrqaYn1AspX20W-iJRz3ZY_9L2oQB5hyfl_6tHgfKb1PmUVhyFwBShZe6a2ogkMcIWWhs8UmCx4cyxa41ZsRctBt3p-WBGcTlOypVhDm198_8RHO0qqHobW57l-b4AzlHaMpiVY1OcYhh6o3qUdxbGvl0_YzHv_NP4RDU3aEzIyeb88L4s6vBJ1eO36Blq4HRkHS46eGofGaMIMcWD16fpD6Z-qdCFjqiPLg7JGGD7NiTCe4oYZEEtEwztQV2u039ZaAu3ySUiGv5PL6cdxd4Sfe3sr3tjLsT1PgTsW3vPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
نجات دروازه فوق‌العاده اوپامکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/100122" target="_blank">📅 23:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100121">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فرانسه پر اشتباهه</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/100121" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100120">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسپانیا داشت دومیووووو میزد</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/100120" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100119">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">واااااااای</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/100119" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100118">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فرانسه نزدیککککک بود بزنهههه</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/100118" target="_blank">📅 23:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100117">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100117" target="_blank">📅 23:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100116">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
چون پاش نشکست و فلج نشد و هنوز زندست پس خطا نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100116" target="_blank">📅 23:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100115">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سالیبا مصدوم شد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/100115" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100114">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27954ba1f7.mp4?token=FuvW3559lh3fuGol8Ipz2Hu6E67frEwaKNDk2STCdCWaOdIHLi876s5kbGfcUnVQkf5kIZvbn1zYXj5WRQz3Trf5bf-RCX7pdQe3GeS9zD7CDHPB58IRGLuOmiBYQ3FEsEe2zD_EDDvEHJSBJo9gllOtr_gGzgpOW_EODexOKih5RdhRxIdeG3cSKh6QLueSz7S2pe96IW8OKPDErcQzMzxJYMyfUZLkFxi0DiXqXdmljnib5p_4Q_PmmV6zsTVZ-zDkfrllFI-qnWnHJu6INFCWDYmwkTc0FkY7PatDWZ-waWN3JPATrc3R8IKDeDC383SyP-2PlLGTerkg5qZMv7wsX5xhuv9HL-83LyOO9ZFacqjN4yvnKAgov-PANhgSGOORTAv6C8If-KIam5iBi8GWeFKqQDUbSMCe1NnypRQ97avcxFtzZn2mOCHB_VxlFBXDrjO2II8AxWorAMRGE5AIZ1kQkgzGKejHZkBdO5-NMQRI-6SLjVXGXutvux4dNLe92Sxvra_LYecbIURgFDy_E6ZeJe1To4-gFLeSHvLjrhsiQ8AUMK74eoZWRFyTliILVO4Utt7lCZjtQLwqDknoBJAP9LSYQUvZalYgrsEATRnUtymLYujnnpRelykCpghZpEGNcGF8iEcfFPS-II0gHfL5d8eBbKiXBN8ffS8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27954ba1f7.mp4?token=FuvW3559lh3fuGol8Ipz2Hu6E67frEwaKNDk2STCdCWaOdIHLi876s5kbGfcUnVQkf5kIZvbn1zYXj5WRQz3Trf5bf-RCX7pdQe3GeS9zD7CDHPB58IRGLuOmiBYQ3FEsEe2zD_EDDvEHJSBJo9gllOtr_gGzgpOW_EODexOKih5RdhRxIdeG3cSKh6QLueSz7S2pe96IW8OKPDErcQzMzxJYMyfUZLkFxi0DiXqXdmljnib5p_4Q_PmmV6zsTVZ-zDkfrllFI-qnWnHJu6INFCWDYmwkTc0FkY7PatDWZ-waWN3JPATrc3R8IKDeDC383SyP-2PlLGTerkg5qZMv7wsX5xhuv9HL-83LyOO9ZFacqjN4yvnKAgov-PANhgSGOORTAv6C8If-KIam5iBi8GWeFKqQDUbSMCe1NnypRQ97avcxFtzZn2mOCHB_VxlFBXDrjO2II8AxWorAMRGE5AIZ1kQkgzGKejHZkBdO5-NMQRI-6SLjVXGXutvux4dNLe92Sxvra_LYecbIURgFDy_E6ZeJe1To4-gFLeSHvLjrhsiQ8AUMK74eoZWRFyTliILVO4Utt7lCZjtQLwqDknoBJAP9LSYQUvZalYgrsEATRnUtymLYujnnpRelykCpghZpEGNcGF8iEcfFPS-II0gHfL5d8eBbKiXBN8ffS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به فرانسه اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/100114" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100113">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگلگلگلگلگللگگللللللللللللل</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/100113" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100112">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/100112" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100111">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسپانییییییا اولیییییییی</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/100111" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100110">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گللللللللللللللللل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100110" target="_blank">📅 22:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100109">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خدایا این دیگه گل بشه خدااااا</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100109" target="_blank">📅 22:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100108">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اویارزابال پشت توپ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/100108" target="_blank">📅 22:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100107">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پنالتییییییی اسپانیا</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/100107" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100106">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH157ActwLAIF1yjwTTLi1FIJXwXwvvMA_OsMY3i0h-iuKSr8L6QVlY5piP3sd6Q4M8-MvJFa6ebY1LXq5_PbPfmTyisAnR8uoaJXZyS_LLrnv7T0HW_slO0Nqv-byt8sxb2QyE7nidmCMRrCvP24kWDuI1bQUohqGQkC7__j3J8TjN141uVxGEF5_ZkMJL3guMfKGxxCj8ECAjn6PLJXlRR6MV0_mgyIoK9VLiS05QFAM_ea0gpKEpTOqaVT8E0Snvcvd9SkSw3B7Jjr3dPWUy2fqzXa1c0_cDpLZ7l2Zkf0btOXy9ZvniWsdJJ43UBXL5bd5z7s7ZTWzJZEPQBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی کارت زرد هم به اولیسه نداد !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/100106" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100105">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqypxXFiTGMTHn7QHSK8spy_SAlkAL6xO1grhT1QQftBEVCeIie2HTUP7wy0WonGQr6ZrTD5t93x2IrDSF7P_w8ZnRKysKkQfpx6rZVsv5zrP624hpeqjazpiuZC1bBk5oVUfwtirk3zDGkXLxB8d66NixS_GyqOslH9vf6ne78dH8A3puB-erO1RmEPFJlF0qha9WpQIrXoZxh6H-c7UC3snZ0LqCGfrPitaDb51JnqrIZ5F8spLa-R8f1n387QXPd5uvne6JsPHPADfIk5HuHtqLb2rSPChGUKNMfeDp44Uxomj1OXqsZ7fltyko6ehd3q90M2DNgAF8rqAzXFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی کارت زرد هم به اولیسه نداد !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100105" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100104">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
لحظاتی پیش صدای چند انفجار در اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/100104" target="_blank">📅 22:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100103">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خطای خوش جا اسپانیااا ربیوت هم زرد گرفت</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100103" target="_blank">📅 22:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100102">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خطای خوش جا اسپانیااا
ربیوت هم زرد گرفت</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100102" target="_blank">📅 22:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100101">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بریییم سراغ بازی جذاب و فوق هیجانی اسپانیا و فرانسه
🔥</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100101" target="_blank">📅 22:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100099">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci4pC1Z-9JRRTGaeYsnnz5T6gm1978PrKwIDgpirmK3flNw3yqBz5THLUOJvYqwm2VBn5EapQbRPgaDfaUTrLLjoh6UPTAkPxLCT1U6F2jMLnRF_TYZYKb-jFtO22A1ccI7QG90alGIzJTyh1wACHbotNs8DdMkFfs1rtUGUI8Flb-L-RP8aBY2UogJYQJITwhZfaQwQd71JhLQPNnzSLieypTFZr3QElbE5kJdDqTdSqvmuPXfMSQyftOHZb1zGpNvRSK6RUCtYHUsWqleapDmkXcQ3kxDmVCLUk0S6D_y_QIcTEbcKDQKKr7bcIJL2c6bitE64bJiZJoPpDTbGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقاتونم همه هستن که
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100099" target="_blank">📅 22:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100098">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izw5z0TolDkXM33WMfFV8k1EqhKX8eES4cCfLR1UXAHRzgzjOUzVgMECksE3KcvUDxlG2jX65_Sb4pb9BhuDCHNkUyKYaSyqbUzbperK8nFcYoCbgPTZNp1nsCuiAza3eVCiZ3Z84bTiWJ5E7n-mdxuA5dNb-wGcuNAhQEbSqjnh-M12wZeuLWzj5K1ZjqyiwxD4CLxdlB-2g2wubhlK-GSczzk5saNFRfvmI1REtw0VI8MQmTA9yMFgj5d36xxxEPdfp0aSwFwk52W3kXna-hAxJ98BqnAVl9FgalHEEi0zyvYx9g_uuRVv3HEqOMefh3RxdymbK7nExkAi7hAnZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گری نویل:
بین تیم‌هایی که توی جام جهانی باقی موندن، اسپانیا تنها تیمیه که بیشترین شانس رو برای شکست دادن فرانسه داره. فرانسه بهترین تیم این تورنمنت بوده، اما اسپانیا سبک بازی‌ای داره که می‌تونه هر تیمی رو شکست بده. من هنوز فکر میکنم فرانسه قهرمان میشه، اما اگه یه تیم بتونه جلوشون رو بگیره، همین اسپانیاییه که داریم می‌بینیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/100098" target="_blank">📅 22:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100097">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reKDKD2x9A7YsTl4vFkezxTr612fPVZS7OVrXBHpUzKgdqY0PqNBcise7jBfkStfaZGsbCVJyEHAbqtqZ4FzIy2vJWrq8bYxdjZrHeDKsff_AClMY6Wuit3T7l_NwZ3UdJqCJ8XSW8nkA3MaKkDMCrvhYLpm0CzJqfp79kFxKnr5hUGzoA1vGv-BF9-p7tmlyWyeoutFrvLom9m2_z6A1rV25sfu3uZEGr4OhtB7hKqyuQp9q-miOAPHYDWDggqcYrLwWWJcZb5G8yq3Nao9Nv3eWRgWBTTONaXJSp3GOqaQyx_T_GW4TgTIBDsuh7atFk5qWVR8PFU-1-kS2Erfpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو: کریستین رومرو از تاتنهام جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/100097" target="_blank">📅 22:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100096">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnJHVJFFzcrcSCyl4db3YEJWDozOdSpjh71Pxj58mLgKfdk4pIM094aX2q649fUTrilyqxLR8PruFLcgcKvuEfb_JM6jrNEDiHdPsxatk0Y721O5MdtToPU0QLuaQIhwQligQP66w4W4BruSZfsCS7qgzZAuYtPMZR_OFO43FwXU1qgEvmVKP6Jnm6UCl5yUyCGYZ0fvLwUBEPo-VB5R_8n4Hijusp0ZqkwaG3_vOw6yEd9pUxqdqrY-lxELSNHbzz64yQd0ZBZiuYmwMEMvuQq2Zrs4Ts5Yzo_-R7mMgWAnFp9P7NWgcGj3CTqvo5-6S8OefgEofAJ72p1FtDyfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
افزایش مجدد قیمت طلا
📊
قیمت طلا
با حدود ۲ درصد افزایش، بار دیگر به محدوده ۱۸ میلیون تومان نزدیک شد.
👇
در شرایط پرنوسان بازار، اپلیکیشن میلی پیشنهاد می‌کند:
۱.  به‌جای خرید یا فروش یک جای طلا،
معاملات خود را به‌صورت پله‌ای و در بازه‌های زمانی یا قیمتی مختلف
انجام دهید. این روش می‌تواند ریسک تصمیم‌گیری در نوسانات شدید بازار را کاهش دهد.
۲.
قیمت طلا
را در مرجعی رصد کنید که
نرخ آن بر پایه معاملات واقعی
روز بازار تعیین می‌شود و امکان خرید یا فروش فوری را در لحظه تصمیم‌گیری فراهم می‌کند.
📌
کد ویژه
خرید
اول
برای مخاطبان این کانال در میلی:
gheimat</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/100096" target="_blank">📅 22:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100095">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ca1OPXkzUwwouLooMnUm6Jr6qF6ZWxRVv8GA6C50ZbBHSJHghlhwIC4lcQp1sCp7rLbPesVAHQRMkd-B3Z-KC6rcYnH2hw5gk1wnJBuN3NkkFuS6R_Ghraw5-d7GIegAt92k8naGgQ86TqvXHYXjsXQuQtzcQKJlbO_6N4Un0ARTjunAyJbodC8kAU__hNN2y4JyLQvqT7oQslq5K4DPXn5UAfx4J_A39_YnHVIQ684366wPWyd39LFxVWi3v8ch0TMEXxIrqpUgvyPJR6maHjZYRtEVlUTytzCnSG4txz-Q2WAQMgvKaVs_O_B5PQeFbNgY7ZogLwiBTuFzALzzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یامال هم تو ورزشگاهه
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/100095" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100094">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QERFw9K9FI_V_WMdz_qUOYZ0vchjFfaVZhfM8U6OToCsEiP6Qke446c_X-f7r9Sr_C_6jyS9LsrHXoswtv0q13SUBFzIluicj1CxiALJkJOEOqpWAvva2PMzdQVlXcmXzJarIvdwKcLHebR7mg9o80WS4qz-lwi3Ybn4wXeuXiW8jaFCVQClj5WEjAog1nlfFuwqIaOYVeW4-uFzrpnRVRxZRjCDkgflLlrpsG_uKH73mI1zncnLCC8shxNWVis1lAQvbvQ3DkVMsiKq9GL2pDn4Ovg4I4AvErs4KVfmnRlTkQv3TSOWvmeyScreMHVFnaGmpZga911jxYSOWemjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
کریستین رومرو از تاتنهام جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/100094" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100093">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKI3cvsLQv1EltPCPmcVgrXLPYU0PERuKK1n0Xxn59INDHN42CzoWd-xn4FowswoN-GWkVK7Jrp_KOJKD8AG3k3MhKpbdB_1bsVNMFAc2c_yVTKUzPOySUz5shGBqbGOQ8jAMtJmpA8H8Ty5uK0dHXXD5xLw0xH4bk-CkoF3fjR20R3tpdUo7ZvLK55tlz459mckyncdaf31FADgXX0l5Gz51nUl_xfCIOwaTTaTWCymxJEllhc_YqXKQn3OrekYVi4uVG-XxpyMZ90l7HCQwmzGHlUPjI4cKndFNNKq9nDB-sKaUk0-f9Rol5zJzwZA8X3o2E_sR6v1IE0jRRYclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیکری‌ که یامال با خودش آورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/100093" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZMGq8xfee5SOE1LGnGhfdaUaKzLWY-Dx61Qd7pSMLY6rPzV1zXccsQPM3z7wAnHLgcloNw1Sn9MsbVQ_K-urWnU2RF1jTtVLRCmFzV42R_xQN2FZMt6n__dHLAVhUdPgac2DyhOpGanFJjL-nN3PURhD8GtbbbjQWpfd7YLZc-7mpO67zJmbAOE-6NgHT-I-BKxyrxs3eGQXg7uAeCxtuCdHXPYAH30_cFqyKC2xQEK1mSP7OT_t0DAQR5UVNc5PzxlxKAo-GW4AdPwvHVa-K4VbWhCZJR_Zyra1-K-p5gF_CfIyVZ-ONpxOaqy6DGh4_5vPg1CT-QKAYKK8viuOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛ کیلیان امباپه تاکنون در نیمه‌نهایی جام‌جهانی گلزنی نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/100091" target="_blank">📅 21:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdf9b5534.mp4?token=UbDFqCCyg1XC0YlUJiIMfzhjk6e7ytG0-NWvZdUI6TdILSpxFHJXV2iUGsFtU1c2D6rDmk1wPdwSkE5tzTeKt_AHmRDrDWk48j7mVPWe3HDs3PfVHb_pCRNzI8KKQiQxLhpNu8CuNFm6GJp-kOsdU9Lp5Cz-8JtyNVzdm7xv17WGulXrMa2fv3suZCpp2MazwaO30xLQhyrXdhmzjNSBc0RFQ_tbBzbMtr5z6jVRJxK5eThM9sVet38BZOKEUsJ1uesk_cgp7RCjCsgpJgSDOYXC2m4Wzo80dSOZ1OE6kjGUGMO2RBBXQje7FglSgB462lV2Zgc20pwAnQpnNXJSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdf9b5534.mp4?token=UbDFqCCyg1XC0YlUJiIMfzhjk6e7ytG0-NWvZdUI6TdILSpxFHJXV2iUGsFtU1c2D6rDmk1wPdwSkE5tzTeKt_AHmRDrDWk48j7mVPWe3HDs3PfVHb_pCRNzI8KKQiQxLhpNu8CuNFm6GJp-kOsdU9Lp5Cz-8JtyNVzdm7xv17WGulXrMa2fv3suZCpp2MazwaO30xLQhyrXdhmzjNSBc0RFQ_tbBzbMtr5z6jVRJxK5eThM9sVet38BZOKEUsJ1uesk_cgp7RCjCsgpJgSDOYXC2m4Wzo80dSOZ1OE6kjGUGMO2RBBXQje7FglSgB462lV2Zgc20pwAnQpnNXJSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
‼️
ابوالفضل جلالی بازیکن پرسپولیس: وقتی در استقلال بودم رسانه پرسپولیس را کم و پیش دنبال می کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/100090" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100089">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d875642e.mp4?token=AgJ3c0KyrH0GGCLBXMTEkX1fMR_bB_XeCFJgqnjZE24gb7b4BOfUo1iu4_v9dN3CG40xzEisXZKSgJOw8XlZf1ty5F2iNOGdSHW6CBJqwxmZpHq-qLjRrhBAHrI4Wby7CIR1TytAQVQDObZi-wx_Vgic6S8SwKfb-sz2ru6cYcQzr2CTKHMx8HtqAgfBv5D4VyGxD9TJc55FGdDGoGhkuzpky6kntx4pXH4aNr5zEuiMORno7a0uzxAHMBfmBrVm-F4ReMJps2powXOYh3fO0m64Dt0xC4zcOs6dDS2kOZoD4WRQtki9FQCxbYFm0tbPboQXh0oKH7PNpWQOupBICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d875642e.mp4?token=AgJ3c0KyrH0GGCLBXMTEkX1fMR_bB_XeCFJgqnjZE24gb7b4BOfUo1iu4_v9dN3CG40xzEisXZKSgJOw8XlZf1ty5F2iNOGdSHW6CBJqwxmZpHq-qLjRrhBAHrI4Wby7CIR1TytAQVQDObZi-wx_Vgic6S8SwKfb-sz2ru6cYcQzr2CTKHMx8HtqAgfBv5D4VyGxD9TJc55FGdDGoGhkuzpky6kntx4pXH4aNr5zEuiMORno7a0uzxAHMBfmBrVm-F4ReMJps2powXOYh3fO0m64Dt0xC4zcOs6dDS2kOZoD4WRQtki9FQCxbYFm0tbPboQXh0oKH7PNpWQOupBICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وریا غفوری: استقلال را باید قهرمان اعلام کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/100089" target="_blank">📅 21:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100088">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAelzuNctlBh_agPCftSS2iN-KP8SxqQEkFmaYogEiSbhoW_CfMW6HRbCeIqh9_9s0p7d-uHJ3WHYYBQajrjxCMBS1oped8y8GCdd11WARkT59aorrW6YCXl6SN492DrOEerz5cUCPCVbrQfWkhuE-Wu-aKDMq9KxiyeLX0V0PRAIA9BW5cwvq70XMF9a8DaTnwapscybvS0QF7BagNECWUerr5kqywRWR1Ozyq9Z-FU3KTaS44NNajMFWFnCxGRQuuOEBx8Gfh_dCZW7dLp34-DDGj5cJirNlDpvj-H7mQv9O3YtOxVyzKiVBnrn5eNm-rjMuReyD2mqnDXnNbhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
پیراهن ستاره رئال‌مادرید در رختکن فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100088" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100087">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35230c72d.mp4?token=gwkn4ZKBMCATR3ielgx_cUt0c4QuKe2TevIZOtoLv7mKrZF7Aivu1bRDgNyQB7p-4k9UZ-UqYuV9RD76iTLK3kwK6eOAWqXKlN1TH5-bzUg7iOR-iF-IKchMJ1f_rfxQ4V-Gr9MxgYNw9a_eZplgchBAKNYYBYOvlKsk0U_4_deHPjGk5SIGhQUC1IC7Hq-qdI-hDvpAS2f67pgbBYCtW15CjBSozVZBceTmrY7eUDI8zAHHhQCp4KA9SmystpdcI2a7YQWuUhRuw7c8MRv9rxhL9SRXQ4yDkbyV5z8ONQCAprNGjR2aDoCr8E5S91vUVnrEab6svwKN2sIIWmDCHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35230c72d.mp4?token=gwkn4ZKBMCATR3ielgx_cUt0c4QuKe2TevIZOtoLv7mKrZF7Aivu1bRDgNyQB7p-4k9UZ-UqYuV9RD76iTLK3kwK6eOAWqXKlN1TH5-bzUg7iOR-iF-IKchMJ1f_rfxQ4V-Gr9MxgYNw9a_eZplgchBAKNYYBYOvlKsk0U_4_deHPjGk5SIGhQUC1IC7Hq-qdI-hDvpAS2f67pgbBYCtW15CjBSozVZBceTmrY7eUDI8zAHHhQCp4KA9SmystpdcI2a7YQWuUhRuw7c8MRv9rxhL9SRXQ4yDkbyV5z8ONQCAprNGjR2aDoCr8E5S91vUVnrEab6svwKN2sIIWmDCHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
یک تیر و سه نشان!!
🎁
با شرکت در
جشنواره حساب های قرض الحسنه بانک کشاورزی
با یک تیر، سه نشان بزنید.
🎯
مشارکت در کار خیر
🎯
شرکت در قرعه کشی و بهره‌مندی از جوایز ارزنده
🎯
دریافت اعتبار خرید تا سقف یک میلیارد ریال
🔻
افتتاح‌ حساب قرض‌ الحسنه از طریق
اپلیکیشن‌باران
و شعب بانک کشاورزی
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100087" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100086">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC0aPdYxmUW2ZTYLbc1n52w4VLi7f-NqAObTJsrKiy1jL40prvA1AtrAsY_7tuQGOz027LKPbR0omFHxToEkt7wzXURFKvYfZ8n0pf-x8DfvhfzleO-__doD4CyFTMZU8-QRmYyGeIFibEicPyMBf1YqUFVRKMZ-c3WuJtzHVa-ISmwKAohv1oJVcVaSMKX5PqXqATtpb4268YlSm36lVDK66AvOFJJ7Ko3MWM9bUutRyPwRSl-5iCGaoeKgxWg3YaS5KEJue_Rlp4mlPFhynybAFjtyxkiJAsCd6j48B0vWD2A-TWwym-N_7rwtqLyyI2FaIz8C-aeHsYr78HaBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسلونا اولین تیم تاریخ جام جهانی شد که 10 بازیکنش در نیمه نهایی جام جهانی حضور دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100086" target="_blank">📅 21:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100085">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QstOVUoNRgBuUycwrVST0n_SQwuWHysNL9IkkOrxp6XtO_Z7ZtTE8MJfUmldbq8uuugHieJdugZhzwH-qt6MijN5N18qLdqVF56ts687sqJ8iC9zJH9LA5o7FKMRcwkacEu3G5IHn2tGtciT6BUqTx2SC3F-dAIcQKd-pyfcnxDNgk2e-Ng6eZXVvAefSKL-ZPO7I0uWRxrdcQVd4_oUMnPdHKxxfR2eEzBBM0aFK-i5YS4nQQciE5ytfM0kyZL377REnj5nzB0-XejNUiksQC4t8XA4wbxkri0DIknQRzoYde-cx73RT_YV_B1lwZeCx_xUnVkDNM5ot0kfMaD4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا در حاشیه بازی امروز به تماشاگران اعلام کرده که بلیت فینال جام‌جهانی همچنان در دسترسه و هرکسی میخواد میتونه خریداری کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/100085" target="_blank">📅 21:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100084">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXLFKU7LkU9d_Nv4UHTIDZpMT31p1tEFt6bJpkZ6AUcqI7ojUCy8atY_BiPcoNPLXzNE4OasstTzeV8e4eixowKClgvGMaipJPhS6Q54z9UcO44MjEaz2ih0KqPGUotXQeibZztpHHf3aPCtXmXCji66uws_T_lc52UGz8ohYVcGGhxSrxVzGPRGCaoHaAA4bsoNdhSBb86197wr1L5KKEUrf9WbMkRtGsIK2ep1YCDvZrQBSi_lf72N5x1mL2TWWJaw6i1SnOgJOusX3GpHPe91lUpIk5zUWejDuQ7rqx_MaYybomVgIgn05iK5WfuFKsi3DlteObMS0NSuRqPqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100084" target="_blank">📅 21:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100083">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZTiCzCgFMs7DdkR76W5anxcXU8L3i2oNVSxCgdcV22f1ZYLJjyFbRXIUPqg8fEUm21ojiUHC904LCGt5v3VZSZPsA-9hyNt3DgvZq559OuE5ZynOjVjuh1VPQTWGFyK9iPlmamnD-h5MZ_u2xdbyXi1iFJj6xG0ns25gb7jbl7Bi1r_-JX8w6DuMMILaSGi7QhaQJNNZL1kkTBap4uxpljW687qxSMEs5Q1tmo1s5C_DfaAz8wHEJ_YoxdWOEeKDsi1tS_ycXRPfsx6Db-KQ2-dRDZ_D3dHOYH4tWesYw4tkefL1WTEJhNoCpoh5CwLyXAjuylSa4i3R6O2YDga5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
#رسمی
|
تیلمانس هافبک بلژیکی استون ویلا به منچستر یونایتد پیوست.
💰
مبلغ قرارداد: 35 میلیون پوند و تا سال 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100083" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100082">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇫🇷
ترکیببببب تیم ملی فرانسه مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100082" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100081">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCiSLIj1fAKC1XDuSNhUiAd3-J31M9gWVq9I4Gjravv9cK18nYrnrrsUKXOqX19ValUs-qg71qbhiNZrNbXOFOUwthja-hbs0JCfJYpaUtXSaNprzxUHFUDC3wokUg1xAeTX2yo6sUNEaZLuZr90uFo5vE7uYvlLNmOv2v5zSJwgFdxU7Wutn8NfNwIOSwGaHE-12gk8m1RP8CA2-Tc3Gq2epG_7CuMeaFPu82XuoDnVpZKv3fL25475BtXnN-HtJwP78aA5TA-ynaiEAUzPOfavlCdi1Wcza5xvjIdlcTBLuiRuFFbnoZk7y4-W9poUgml8hJxOOiuAxwGNzOoqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی تیم ملی اسپانیا برای بازی با فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/100081" target="_blank">📅 20:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100080">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF-VnezVsd0Q-ABSwQFpLfkI3TSND9PnYLofDYGgMhbwtURRhRsWu5MIZ2pM9srTPrxxqvsjvo_UeoG9EJ5nQcqORVNoak-nVyfViHRVxWjAwfJDCda-mbDgK1snpAH2ypryshQJ5RP06Ik3xmYfQkkQu3daaibPk5C3FuyLh0ggd77-bygLCIFmAeDpfdOb4Bk7DkxuYRwDkzupXeMHkDfFIWyK5_YaMIqUcuc8XDhQ7IdLzAf4tAWvSIttHvQGUHoHmbMZUsvW1hvhY5OJYoVkUit7E6Mcq6WBUoXaYInURyOU5-udnhs_xS3gnBnpUUeB-IOupWy5ReIzqxL-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی تیم ملی اسپانیا برای بازی با فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100080" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1J6DWgGjSJz6K0kTc_0-nFLlJZ4lcj55OkQWImsQv5cqOCx-g9fX76ZyN9W6P-o3byTuAbmLxi16QyN3DKD6lZDOzYe2C5_mHP0wihz1flVvuXfERxhg0sho1NQKXCUAL-pTsDvsMulT2GSA5bLr4BZZ0C6kIpiHt_-TnMQIFrGr33r4DQSPRD-ljYl4pdiwyYw509bE-t1UQcx1uoJQrCj5B-PR5MLhNXJL8ElG9tVGOiOpWXrFMCDt49c5khBsan0W57Ii-2-pQAdt8UQJXPBKVFIfhXz6s8rFcg7TSx-iufrH2ihjuKmMdO2Xsh93vhmfGrlPU1xZzGQubBpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی تیم ملی اسپانیا برای بازی با فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100079" target="_blank">📅 20:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSjmYcrCjXOmEUeOrAOK7JOKmWvXT5LCvo3HTXZhHyZct66H1aLVYlxxeUEpr9hueJ_KezFboe6RCIkvqG9VMkOl1zMmVn479T4IJ8UtPiFaVIJ0LfZxqTFVgqa-s-ZFM6w_S0qFVW0yXy1AiUASaCVPH1Lrqk0rJJZ4XUBaOWd2i96RNShgzejyr5qfXID1oo-bVgDXFLNA0-2tbeMUyr03B1hvZcXxA5S3TeYBZd4nRYeKutrDgZypSJhNxRara-xnP825Gj5Cv1JlMKrNNWc7D2fXIR8USzbBfFeby7xVGMx1FmMpdTWcHdPWP1Ls4bVo6z2B6VwtqocGF5P8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/100078" target="_blank">📅 20:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100076">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Axruy9oYBv02HA9Z8liztEMepWD75HQhZT1QPaNvkhzEeXPWkkaGn-foV9jk54xyDS460Ss_JJ9FVe1P-yPMnIz041mhGDDyS7WyL4VWuEPrCBGXL07Ic5PbI7VcwUsPDLtqb-8j78QOwOf0_zoORC_2wISCxHg-lRFIjCDmKFL_eoWWvbvdZ7O4gPsOuOtujqJ351H2uSrSc701mwuIuVkVDo0iyt6cK5WXrHsXU_0TIVZ9m2iUsqGcR8W2c1o6EQ2e2bWIAsZ5p2SPN6Ol85lj7P2XpMjkRMonvzbRgur9fSw9KGOqL4i_oUCqg_Y29jHNqLmy8GOqkWDGio_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا در نیمه‌نهایی مسابقات بزرگ، هیچ بازی‌ای را تا به حال نباخته است:
‏
✅
برنده نیمه‌نهایی یورو ۱۹۶۴
‏
✅
برنده نیمه‌نهایی یورو ۱۹۸۴
‏
✅
برنده نیمه‌نهایی المپیک ۱۹۹۲
‏
✅
برنده نیمه‌نهایی المپیک ۲۰۰۰
‏
✅
برنده نیمه‌نهایی یورو ۲۰۰۸
‏
✅
برنده نیمه‌نهایی جام جهانی ۲۰۱۰
‏
✅
برنده نیمه‌نهایی یورو ۲۰۱۲
‏
➖
تساوی و حذف در ضربات پنالتی، "یورو ۲۰۲۰"
‏
✅
برنده نیمه‌نهایی یورو ۲۰۲۴
‏
✅
برنده نیمه‌نهایی المپیک پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100076" target="_blank">📅 20:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100074">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Km5Yf8oRS3UKFA_jzQAt98VZSx-nGnyiLaXRYLMJ5YYU-eDyXsB-8aO1AqWGI8WZNevON386mwTstvHX0eNaV2qNtx56vATQ_BIa0PiS75lASthGPE5lwJSQh8mcn6d1vTy8-9aEjx2tev3nv47citI7mT-TFqpwh5L27ba-zOTj5y3osrqqyinWSi3slwLjnzdPuyh7OFgmebVG4Ctgkttjp5wFg-auqM0FixuVdk8F8NSMni7sRN6ih8i6qh8i_nQUpcdVKm6zAmu8NRCMD2l311aOJ7jGjg2Q4d9QJnPvEHklMyQb2cWR2T9530VgOC0u-PoQ2YYQz4qy91nX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwUObnvLFI3DxbVBgfSLMseE9Kx3gZyqLpD9lWEuECPXDfphfT6CPN_VEHb8RcYCTzHxaHQzQx1Wfto7Jxz4JA-K-ZbJN2RSMvVgZCaNhNdRr14HvpZkGHw18YhOXx34tgJdYfY8RRHyWfFqZe3GbttLPW-r-ftgvJtpUp6bo2M7LbSYT1QkBXZ6HLlKwe5Ei4WCb9HUwS-3ZvS2zT6KLTsuR9ItacyQGU5DANTt5WXzD18bhhNe9EJJqLaMOMxSSgUrnBBhxIYmiKlMuF9VrA80MnfmwrXYSvuFNoNJs3NZKosHsOFAqcMi2zkwKolvQJ_lX4wb2nHawWOqi8O_Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🔥
کری‌خونی‌های لامین‌یامال شروع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100074" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100073">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR3gWiqqAUdqmqGOg_w_kLDQBiSgNOg8oGHsuVs8CzR7nSDmT-PSIGb_NXKJQrR1bwroboCKAGIGvDwT1wDto-H2YccGz6SFIpzY66zYx-8vYJoxLb-x_gM_v1uk6-2toi4s5MtNoc9KeJcsj83W-qo4SDNpGE_lbdKSztzn-0dyahLhdmb9E3SbwSH1ks4ismGUlV7M4N8LO9OwBjtlXvmfHQM9qMRBOROVFGizHEROkNVc_ypwTw6rG-Y2e4Sj9eWoIGuIwIAkxeMM6O_nkWw81dbmiIMzBSimrhsnu2Z29E2WgCvcSKnzdzZX5E6PUbRbEgI_vnMXl80uxmxewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتلتیکومادرید در تماس با فران‌تورس از این بازیکن درخواست کرده که فصل‌آینده قراردادش را تمدید نکند و به صورت رایگان راهی مادرید شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100073" target="_blank">📅 19:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100072">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzkIMxxFAfPKNU_gzxx6BtGv1ZX0SPoTXOPJ8o-BO92bS9mNLgkm7wKoFnaTYimycpMW-IrUhq5KzSNYV0oo0Of_WxSLVz-sgEMXKnJRZWikjCXkd9mD8fgHqw19NqNs802r2yNfjUMv9PSQ7XB0vzSOud0eIfQwGOarIX-R0g5dFFZQEhUAEqaQsy_tKj1pR-S-Zct10Cp2znng_dqErvvtxpLEvKDdqn-oo6ySEFhkrDV9zQ_akJ_UrE7G4HpTrE-IS1TDOKqMzF4Rr1HzeREuUj1hhoomCC1J4rAKhdteYSioSoI-5QsJmx7Cl8s6PYjrct2qaFoZjibmNu7YWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
هفته بعدی تاجرنیا مصاحبه میکنه که زن یاسر آسانی مخالف برگشتش به ایران بوده و ما تمام تلاش خودمون رو کردیم
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100072" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100071">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
🇫🇷
🇪🇸
آخرین تقابل فرانسه و اسپانیا در لیگ‌ ملت‌های اروپا که با نتیجه پرگل به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100071" target="_blank">📅 19:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100070">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7893735fc4.mp4?token=c9z5JIJ9g6qfpJR4jUNc31LnEACx_SFvBAKizEJnMNpD9DvZRH39YCdlYT0nikOiXuWZd6lIb9qxOBVxY_Esx0up9Ph0YjHFBiv50xZ9TDZfhOqppS4WvnKGYC6CeyxTYeYnsmHp_bNyZjlXgCjmSAjoDlSQTPOOkHdXt-JhDCggaDR6cfocayEuhZNAse2WGDpZmvAv-lzCcKta06DeHmm9ynqAFj4VsBnrJnTgxDZQtUQOho96x64tVm3nsiu-nDE9T83Xc1k75sH4EHOGIa_hjYE23XNpCu86n3Zxe-koKwaA-SA9JGOiads_dkKW1xKqPR4DTu-PcKHHtVyw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7893735fc4.mp4?token=c9z5JIJ9g6qfpJR4jUNc31LnEACx_SFvBAKizEJnMNpD9DvZRH39YCdlYT0nikOiXuWZd6lIb9qxOBVxY_Esx0up9Ph0YjHFBiv50xZ9TDZfhOqppS4WvnKGYC6CeyxTYeYnsmHp_bNyZjlXgCjmSAjoDlSQTPOOkHdXt-JhDCggaDR6cfocayEuhZNAse2WGDpZmvAv-lzCcKta06DeHmm9ynqAFj4VsBnrJnTgxDZQtUQOho96x64tVm3nsiu-nDE9T83Xc1k75sH4EHOGIa_hjYE23XNpCu86n3Zxe-koKwaA-SA9JGOiads_dkKW1xKqPR4DTu-PcKHHtVyw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇪🇸
مروری بر نیمه‌نهایی یورو ۲۰۲۴ و سوپرگل فوق‌العاده لامین‌یامال مقابل تیم‌ملی فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100070" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100069">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uaEKMetx7CJnJlyiUsTl9YDhs16Rwnd3Fai83QxXzvOYyYbccdid_xn8vOM_rh_HgeWCwxFzdEY7hG68AkLStjM5KA4SRWD3A3KWnhg6qbQQ47CqnIXQW6e_1uiNdmjJUSaCeEORjs9DjJLcJ6pnzyByREi4LVi_8sWHSJwecJdsgn6X4oRayXEyEkjJ3uK7Zow-L4tkqF1nDb-DJYfFLYqEZYLRyjoP0Jm0UrtLIPk8-cwcDCEqgEiSu0ZQZYcWExQy1hw4LlD-U9oyYuyZe-oZh8GyuQ7_GnwZwnTYNIK1fCsqxCMRoFfzxeBcnFNCUTdQZsFtC5C4DwpG-e2r_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🚨
فیفا از هنرمندان حاضر در مراسم اختتامیه فینال جام‌جهانی پرده برداشت. این هنرمندان عبارتند از: تام کروز، جنیفر هدسون، لورا باوسینی، نیکول شرزینگر، آی شو اسپید و روبی ویلیامز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100069" target="_blank">📅 18:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100068">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789a70c949.mp4?token=XC9v2QaVND4jG2rSGnrW_MsHkmOiW7Kqa9cUJOPegN7WI0NJfHYGGWJxL9psqe3vgQ1OyEUo5YS-G6GDIjwv4XmIfDH0qDVwNTTbZ1sGtU6KuciAJGCk6CNX9_vH_mFtOGAl9NQxz2j0JmpWK-OS9NJxRzq-j9mL3zz6TrenLMAmCrbQGqMLicPUsdnGvnwbVQy3okEAqQjIyHyHtOTC3UapFLZxT3s6F0i70UYZ5CFuhDEXJS9krw_ui1bjb08iOTsRKOxzt9688jh5-lvKNcxNmf8h2scyCRv1ZzbAE1PZcr68534bLToThTcBQu9gmhTPPNxjkHqkgLHjRXKvPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789a70c949.mp4?token=XC9v2QaVND4jG2rSGnrW_MsHkmOiW7Kqa9cUJOPegN7WI0NJfHYGGWJxL9psqe3vgQ1OyEUo5YS-G6GDIjwv4XmIfDH0qDVwNTTbZ1sGtU6KuciAJGCk6CNX9_vH_mFtOGAl9NQxz2j0JmpWK-OS9NJxRzq-j9mL3zz6TrenLMAmCrbQGqMLicPUsdnGvnwbVQy3okEAqQjIyHyHtOTC3UapFLZxT3s6F0i70UYZ5CFuhDEXJS9krw_ui1bjb08iOTsRKOxzt9688jh5-lvKNcxNmf8h2scyCRv1ZzbAE1PZcr68534bLToThTcBQu9gmhTPPNxjkHqkgLHjRXKvPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
⏳
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100068" target="_blank">📅 18:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100067">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c97b0625.mp4?token=L-fN4c41sJUiypP8_754egw5MucDbqxU5NKLwdNIrv2a8zP9sn7uuu4tnY_ApoEd9G4ge8__txG9BpyiuetAc914wfHeYY5d2OynggZhElakQFREOdIOyl7JRRoNvEB7e2ZCItk0G0ab40TpJunrf7rreeeitZhOeozhty0tinIYGcITn0A5BYYGgH0ETKBdko_QSPfJPvZcf-_bYY2-gX0PLd-tJAbhkAgV10450SrXk-q4W01FmA_eV0cEWJAlm--dCinUOyJ4u_FnPX9S2_nV3NiL5T6NxgqOkeDrvQeo_RQsKIajGrfLAHv-SJSxAaUJWtPiwl6I_YcaPFnl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c97b0625.mp4?token=L-fN4c41sJUiypP8_754egw5MucDbqxU5NKLwdNIrv2a8zP9sn7uuu4tnY_ApoEd9G4ge8__txG9BpyiuetAc914wfHeYY5d2OynggZhElakQFREOdIOyl7JRRoNvEB7e2ZCItk0G0ab40TpJunrf7rreeeitZhOeozhty0tinIYGcITn0A5BYYGgH0ETKBdko_QSPfJPvZcf-_bYY2-gX0PLd-tJAbhkAgV10450SrXk-q4W01FmA_eV0cEWJAlm--dCinUOyJ4u_FnPX9S2_nV3NiL5T6NxgqOkeDrvQeo_RQsKIajGrfLAHv-SJSxAaUJWtPiwl6I_YcaPFnl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
نبرد حساس امشب میان فرانسه و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100067" target="_blank">📅 18:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100066">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWieucLQUljovNC8Py4zpQuCWlY8f8V9Av9Ioo1-w8rgAg4M0jCmT9cwVZ0f7CdVp5btHbW4rK8GF8eSMgAhpbCJmcw7rVJsjiD3vLsVMh161XYYTjWUR0kwXWZF0efDfV6_ytbQewSagRVYOz-JIclfpwvSS3InVlP5N-TwRdaFGymcZGbFO87rcvAUmEowJJzsAfPnY3VgrWkY1-JE5TH4BVx-qtQN3qvPdX1mn36DJ5fE1-H04iECtRsAQ_Llf_yK_-d_KSORhgVQWmeSxpRPvBaE0KWVME7UfN6wGmWAp2mnKYN4l-hSMu4XMM3gsbiDi8MgWMuhWqsssxekLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
فرزند کریستیانو رونالدو واجد شرایط انتخاب یکی از کشورهای زیر برای بازی‌های ملی‌است:
🇵🇹
پرتغال – به دلیل ملیت پدرش
🇺🇸
ایالات متحده آمریکا – به دلیل تولد در آنجا
🇪🇸
اسپانیا – به دلیل زندگی کردن در آنجا به مدت سه سال قبل از رسیدن به سن 10 سالگی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس – به دلیل زندگی کردن در آنجا به مدت بیش از 5 سال
🇨🇻
کیپ ورد – به دلیل ریشه خانوادگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100066" target="_blank">📅 17:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100065">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔥
🇪🇸
بازگشت بارسلونا به تمرینات برای فصل‌جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100065" target="_blank">📅 17:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100064">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffb38d84e.mp4?token=d8VByNPGrW9tmueCitSYReJicsMQ1dcVp4UKyxI-tg3tMGSk7bNo-ftAcy49syRwo5J5Lf8-t63rSUCPDZLe39uH4bgL1tYQh5rMRzx0X3RkCZjWb85VanUHn6MXe7Kz5fnKwQGsKrxW9rSfCG7chuf8asiwfDp9kiev1NeoX5rjEimMjEsQQhF8ok7c_qTtcqIYBrobz0jRoBYWmHaNpblb10w_5blsCeE3ARxHC9kh19njLjuf-8KNtmjqwkpjUHmxnevMmvMFNc9tAarEF9SIxYa2J915yskaNXTc8hzEK1iZbTVXym4gqZ8OIjrVuRRkGPxbjHJkBl5Qd6oLOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffb38d84e.mp4?token=d8VByNPGrW9tmueCitSYReJicsMQ1dcVp4UKyxI-tg3tMGSk7bNo-ftAcy49syRwo5J5Lf8-t63rSUCPDZLe39uH4bgL1tYQh5rMRzx0X3RkCZjWb85VanUHn6MXe7Kz5fnKwQGsKrxW9rSfCG7chuf8asiwfDp9kiev1NeoX5rjEimMjEsQQhF8ok7c_qTtcqIYBrobz0jRoBYWmHaNpblb10w_5blsCeE3ARxHC9kh19njLjuf-8KNtmjqwkpjUHmxnevMmvMFNc9tAarEF9SIxYa2J915yskaNXTc8hzEK1iZbTVXym4gqZ8OIjrVuRRkGPxbjHJkBl5Qd6oLOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇳🇴
اسکورت و استقبال از کاروان تیم‌ملی نروژ توسط جنگنده‌های این کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100064" target="_blank">📅 17:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100063">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMv2GqZ9An3W6OTBujKd_Yy0x4qMOmtXleCUQdCfKIvE-8mbZAEkMLHuzHmkdxkAqhQdNitjyEfmvjLzBZgY2QU-ENolV9eh5jn-RilB5UAYhql2MqGAylrcmFtbZ9Jbq1R-o7MguBa-GNvxuyte8ALbEe9YTtDreG93hLpbjCrAdibVGm_a4ccKn6J93iAwk7USjmhDK9Pd0oYYSe4rApQcXfkTZfOscP8EyiLZCgF_QzXFKiJP4czSeOuIBCOno4eKxB7wWxSM549ilUfk-q-JxrxL32LNqcojbSBonWjXisXPYAd3qxWur6Ab2q1mxWIAz-YcQNCYVxEADdm1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
#فوووووری از متئو مورتو: فرنکی‌دی‌یونگ هافبک هلندی بارسلونا دچار مصدومیت شده و حدود ۴ ماه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100063" target="_blank">📅 17:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100062">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f23f251977.mp4?token=NgZNLlp8UA5AflCs3w6PMMlnEN9nCiVPuwluKRwZGdgVwLt4nslOrL-c7gniMc_X4I6dU8QUim6tzvVQe6xdtxtDV5EDyTuP_ikdtlE49qelWaMrrsNSnEBpFeHPX30yw8_JPJ1Bf4_TvsrKebwnjrZhnLzM5NgdUkGkhOzexIU6_VNjUJ725l7mYIQn9dIkoxiLT_CzSW2LXU8m7PAXp3Vzg7vRkYdJfwyE1X7c36w-fAIKMhHCyDIj5mY_kD-0hMMcHmbAIwFYOuVn9kI6ILYWMxIGqhGtWgqo2Td_RHFgSK8tzmGK9N-fKZW4jDArGUdSskjiMvG72nz8XuLG2yLfzp7VA9VgRZIzHQFBKqAj0Ta3s1xr-gWKbtSIWCAdbk4jkXPA_gws9LmZ9P1zy6wAmL8ASPdBRuqlcofgSdnkG_z0C4ij3JaUIoGU-Cf7lGdDA2hgpTvEAtVz-k_rGfNCDsTDXyflaQFvKO772bav9EpXjSJw9ABsHaD8pltohxMRVZsThTKJTKqoux6HpVCFeFEjvxzgd5Fn2PDZIqXSUUI4hRQIUBgk4j5IjL3-_QxUvLh_gvQ-S8HfDYzRNz9v9FeUEXJgG1Zz4LTM6HyuNE99_HDdUXuZ8UX_A5V6uKznJV-pSRX9h46YKcT3oOAPt4r0lWuDrvexDqkK2hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f23f251977.mp4?token=NgZNLlp8UA5AflCs3w6PMMlnEN9nCiVPuwluKRwZGdgVwLt4nslOrL-c7gniMc_X4I6dU8QUim6tzvVQe6xdtxtDV5EDyTuP_ikdtlE49qelWaMrrsNSnEBpFeHPX30yw8_JPJ1Bf4_TvsrKebwnjrZhnLzM5NgdUkGkhOzexIU6_VNjUJ725l7mYIQn9dIkoxiLT_CzSW2LXU8m7PAXp3Vzg7vRkYdJfwyE1X7c36w-fAIKMhHCyDIj5mY_kD-0hMMcHmbAIwFYOuVn9kI6ILYWMxIGqhGtWgqo2Td_RHFgSK8tzmGK9N-fKZW4jDArGUdSskjiMvG72nz8XuLG2yLfzp7VA9VgRZIzHQFBKqAj0Ta3s1xr-gWKbtSIWCAdbk4jkXPA_gws9LmZ9P1zy6wAmL8ASPdBRuqlcofgSdnkG_z0C4ij3JaUIoGU-Cf7lGdDA2hgpTvEAtVz-k_rGfNCDsTDXyflaQFvKO772bav9EpXjSJw9ABsHaD8pltohxMRVZsThTKJTKqoux6HpVCFeFEjvxzgd5Fn2PDZIqXSUUI4hRQIUBgk4j5IjL3-_QxUvLh_gvQ-S8HfDYzRNz9v9FeUEXJgG1Zz4LTM6HyuNE99_HDdUXuZ8UX_A5V6uKznJV-pSRX9h46YKcT3oOAPt4r0lWuDrvexDqkK2hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تنها چند ساعت تا تقابل خونین اسپانیا و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100062" target="_blank">📅 17:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100061">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1C0NET5S5Q3dWjqxT_HrPBEiU9If2-Ilp9g733TbSqjDOV1jcJHHfqaedNPPuvu_lDkV5kjgBjAffy_-bRGkJNgGxPtosEFDS95MFTcDYaMRWmr500Cs7bBRmj95no2rYiLF7j9ZMZOW-ZXQ1Unf2hzUOk-zkE4nQNiB_kdxXi-GMR3cWJGFelzjuL4OPLl6SDShFKMHsUbGhvWu8fCPsWXQNrjd-kw5pdBvq6R3FVjw3nyarEmdhALlDfD0YcCMp2I0-xefTMdW9Z1LSH4_niWc9iOTw3A1XU8Pnh9VyzTOddTpQZ6qnnnQFGacNFDMppJ7jncnpbkbejt9rKHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
#فوووووری
از متئو مورتو: فرنکی‌دی‌یونگ هافبک هلندی بارسلونا دچار مصدومیت شده و حدود ۴ ماه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100061" target="_blank">📅 16:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84de7847.mp4?token=I4LACbA82hzN9531-0vYHMf5vy1MYsM1DiFGqDKpMa9Q5vIFrqLNYXbqBoFCHabcnx9hu9d5LPFM9_JqZOd_oHXSG1lu21iLmOMjkCZ0MkU7jJ3la98rZhjXh0SP38JoGroHD9aR_SYnLacQ9pHnZpPeScWQrfbRiTV6geC3KEt8iH63276JS3-9OmMWDm5jgAUR8FZR-G9whPbxmNneC2SafdZOzaCq7Fv0pCSoDwaUz7YpUn06opoJuhrHgUGnvl5sQ3T8F-Y5-_jg7UHXAOJ29sno7nhI_nFGe_EvPQY-vatPPwuY8u3lcLdbgIVv3FF-WtE_7Tmzih9QnsZsyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84de7847.mp4?token=I4LACbA82hzN9531-0vYHMf5vy1MYsM1DiFGqDKpMa9Q5vIFrqLNYXbqBoFCHabcnx9hu9d5LPFM9_JqZOd_oHXSG1lu21iLmOMjkCZ0MkU7jJ3la98rZhjXh0SP38JoGroHD9aR_SYnLacQ9pHnZpPeScWQrfbRiTV6geC3KEt8iH63276JS3-9OmMWDm5jgAUR8FZR-G9whPbxmNneC2SafdZOzaCq7Fv0pCSoDwaUz7YpUn06opoJuhrHgUGnvl5sQ3T8F-Y5-_jg7UHXAOJ29sno7nhI_nFGe_EvPQY-vatPPwuY8u3lcLdbgIVv3FF-WtE_7Tmzih9QnsZsyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارو زدن 150 هزار نفری نروژی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100060" target="_blank">📅 16:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100059">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417c844b52.mp4?token=VmWg4_HmShsXb3h2ZJuhzeiPGmhv6kQ-SjI342RQqImGwvvcJvrZnEFa2R1u7uU7QLtgtaNMm5LQnVfXkh94xN6en6lmTQiYNHxnFyNduE9P1Dbr-ulhJVoiPcvzApGDVIPpjoJXL-IAUm6LMN51K1HwABFElrp8WpDiItueiPmAfUDNmm71txdyldruBsyaIhG_FEv4DsY6ZIs07Mn3m3-ChMdclQrWCiK6SHCcazEM4KFDypIuIHtL9gGfgwUJSlIau0otJWQA7Ww_oTXuMF6qOLyZRQq5ABSxLrEXSJutZSlAENCL3noppGni95FHb1LymgODNo--y2Hym3f39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417c844b52.mp4?token=VmWg4_HmShsXb3h2ZJuhzeiPGmhv6kQ-SjI342RQqImGwvvcJvrZnEFa2R1u7uU7QLtgtaNMm5LQnVfXkh94xN6en6lmTQiYNHxnFyNduE9P1Dbr-ulhJVoiPcvzApGDVIPpjoJXL-IAUm6LMN51K1HwABFElrp8WpDiItueiPmAfUDNmm71txdyldruBsyaIhG_FEv4DsY6ZIs07Mn3m3-ChMdclQrWCiK6SHCcazEM4KFDypIuIHtL9gGfgwUJSlIau0otJWQA7Ww_oTXuMF6qOLyZRQq5ABSxLrEXSJutZSlAENCL3noppGni95FHb1LymgODNo--y2Hym3f39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله‌روا و ابوطالب آبروی قیاسی رو بردن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100059" target="_blank">📅 16:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100058">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_AEa1crOK9KUYpzSAL9nJdi2XGOfDCcACnogwq9WAKQg1DksH-OCY4jd-sJ8wrkn3ErI63SCQm4o9QSoitHWBcyYKoJRCKWTlMaXDo4WGsa7iKHunxSBQDUgsgiB9ZvfirfsPIZuQtYh4kk0oW3QfyF3Hm9KeyE4Up0Lagm0cflrRVnnmtaAgsWcXOKpe4AGtDx6puMlmo4NMqRL3N6aYr3pXJnEc7ZT4Ag6MArKxIwK_MWGm8w8YupAOYtn_u3ZySj0XTG7whLjwOQpVvzQSNPZEv764V4BecUIKgA6HWabs9Pnroh-r7lvllqAJDrLP5bXSUhe7UsLJKHj50bFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100058" target="_blank">📅 16:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100057">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx2D5Fxnmf0ltr0Ej_FDFEGTdF3cBxD5KjK3tSIwb9JUg0UKgqDOCmoEdbK-d-V8bqhJkgo123FX905r1Ajy71U1V5aDETEX2821CF62mtanWPe7qgdhkfEIu2wHqvHj1vzp5pihzjrext6YlNmg4PQc5DKgvCZV5vj8a3cu5f9qX2xFEKaF7SyQOb26HI9ZewVRhV-qTMoINu97UfbW-XYR-MGfxRyV0cMhaIHWrNsIKVluz9qom2hb_WmK4nvnqpD6m_qy9HNyuARrk2Lzj46A0PFV43-xXKlVWR3k0p-8J_iQzI1Bpr90CreBFcjcmRJxVE5X3SF3OXEWSIHaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دیوید اورنشتین:
لیورپول به شدت به بارکولا علاقه‌منده، پاریس میخواد اونو نگه داره، اما این یک گزینه واقع‌بینانه است. تنها دو سال از قراردادش باقی مونده، و اون به طور منظم بازی نمیکنه و فیکس نیست، در حالی که او میخواد اینطور باشه. بارکولا در صورت  وجود فرصت مناسب، از انتقال استقبال میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100057" target="_blank">📅 16:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100055">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b8b38999a.mp4?token=qdG_M67fqxzyk7nO0ZEH9JU1zsQyj740kS-USS2cjtitiopXVnlxnSGiz2MwTTxFbFgJhEMPyKE5QvhJ_tYFvEbom8vIm6FtUImOznp0Yxz2o8PFGHoGLTuusQzM0lotNiDVFDw_QTAVkZfrJZwyi6r_iz8QWTLekUqpwPksuz5mAzuRlpgqSVF1w-ZNBTbQibc1YzR3YmzAWEQ-BGzYWIGPt_KbPNoi-seDib1ydygnHwgrwR_1Eg7gK_n_YkbWaF2Qtda_TG-dzhXFFjCQ9k9t4odeQtHNBpmKFL5uDa8TGJgXwNg3I8ZYpjrpP76ers2QijeyVyz3xO8nmxQTurBCEHp8mqxOo7t1jO-POEL-EO4_MBZHmcoiH7peOXQa_MQbn__XRcmc187AFH1Pw8DI-WpRdfHUZzT4dWQW1FeRKEObrL9o6o3RE0XtvVt5adDMBPUeNcLJdKSZFNSmXi71MPoqYD8NX6ZKux-i3nkKyX3Gw-idusWwfUG8ne46lC02d5voPpe3NLMWezXLptqGkidwWsVsuNO47tiRPXpXbv34gIV-sqL0pQxbsW3rCKOK50F0YF7uILoeJOzu9NzD3Q29MFi1oqqRCueF2KZAgg3mpGJ-rym-hUHu7IEgiWY2gkjK2XOoNFXhCtgrQlA-A9Vn78mrmQKGyNLdDM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b8b38999a.mp4?token=qdG_M67fqxzyk7nO0ZEH9JU1zsQyj740kS-USS2cjtitiopXVnlxnSGiz2MwTTxFbFgJhEMPyKE5QvhJ_tYFvEbom8vIm6FtUImOznp0Yxz2o8PFGHoGLTuusQzM0lotNiDVFDw_QTAVkZfrJZwyi6r_iz8QWTLekUqpwPksuz5mAzuRlpgqSVF1w-ZNBTbQibc1YzR3YmzAWEQ-BGzYWIGPt_KbPNoi-seDib1ydygnHwgrwR_1Eg7gK_n_YkbWaF2Qtda_TG-dzhXFFjCQ9k9t4odeQtHNBpmKFL5uDa8TGJgXwNg3I8ZYpjrpP76ers2QijeyVyz3xO8nmxQTurBCEHp8mqxOo7t1jO-POEL-EO4_MBZHmcoiH7peOXQa_MQbn__XRcmc187AFH1Pw8DI-WpRdfHUZzT4dWQW1FeRKEObrL9o6o3RE0XtvVt5adDMBPUeNcLJdKSZFNSmXi71MPoqYD8NX6ZKux-i3nkKyX3Gw-idusWwfUG8ne46lC02d5voPpe3NLMWezXLptqGkidwWsVsuNO47tiRPXpXbv34gIV-sqL0pQxbsW3rCKOK50F0YF7uILoeJOzu9NzD3Q29MFi1oqqRCueF2KZAgg3mpGJ-rym-hUHu7IEgiWY2gkjK2XOoNFXhCtgrQlA-A9Vn78mrmQKGyNLdDM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محدودیت‌های عجیب هاجر دباغ ستاره فوتبال بانوان کشور برای انجام یک‌تمرین ساده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100055" target="_blank">📅 16:20 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
