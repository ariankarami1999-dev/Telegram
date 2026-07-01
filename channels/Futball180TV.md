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
<img src="https://cdn5.telesco.pe/file/UFXmewFz6qrOO05Si9vO9AO3mISN0q_I0dmegawcwKTzy9aAvSWmv5q3vjGfA_LLgIC2zWexCbKYs5FuPSTigErLQMe8oRqSulMXqJ_elp58EN-cPU5syjIh2zre6QfLWAwcBSQdyWHddcsOIGJcekg4YKT_LWaWSOGRW87HbuLJJLLUJIKft0Yq0n7uhl0UNIMhcvbvJt2YSYXXFzlWq7lzP_XcChLJfE6ZYz81Eq0la7TI2-0_OLH9r5QPtAoss23lJ2zKyA14MhqnxOD77R1zHi4wNROZ5ATH1Qw583JRGwYZz0-HnBxg5sShLqwg7JWNh_fUJLFyj20wh3jj5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 663K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 01:43:18</div>
<hr>

<div class="tg-post" id="msg-97496">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بازی رفت وقت اضافه</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/97496" target="_blank">📅 01:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97495">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e236b4c020.mp4?token=B5t6ZpXh9z5l4fR3R8TL6XR7gP65LXuBk7u5jGTH60sc5qk2mLDUdRUSBp6eCuFDnz2_tV_MmIaZRd4hlk0_cuiEE2bAFW_YoFFKtupIO9fa7DzIUYwoz-j9qWF-JwLNRZ2r_TC-TC45_wsVmeXzn3OSRmYJGKRG3JzpXK_FF8avNKylPgnI8y6Km40INxfj8lOyBnmUJHytGLY_h-NEA6roKDyTZsZ4_WrPz6OH20UCs2-PXC2cQJNErZqGp2BRgqctQBeXsWbk2oWGKAxXk4WhpxwKFN-K-ItY6SaYRO1qPVoEHYMJrX1FVpBOb4CHk741PsPy_PUgW-tjyfcWTSgXX9gJQoh450-cWpvvogpUEarWZuLuE8w-2G4A8deveubcNnM6NRVmp8NjfKa0PYbpXYV3SMGPjjeVg8PajqTztIIqIyVhw077ATBcf1c2PmD1OmOjkMUVlQU_EmOSxmU654d8vf9YyOAh57c6twAcDIXVWeir9nN5e32D6_nIsI4zGMZfWwO_ilAHTHxOPRmyL1Db7KVor0NaLUHFTFcODdmMBiHSIB7XEiTcFe1XoB4vNsVJ0Rvg_RMmGguUhn-TD98jyb-BrOHoUpwl_VhW3N-mirSBfdqxR-G4EKiLcUOR87lEO3fCq6LjWvT40vyuVp5JX_vSvsLmexM2sG4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e236b4c020.mp4?token=B5t6ZpXh9z5l4fR3R8TL6XR7gP65LXuBk7u5jGTH60sc5qk2mLDUdRUSBp6eCuFDnz2_tV_MmIaZRd4hlk0_cuiEE2bAFW_YoFFKtupIO9fa7DzIUYwoz-j9qWF-JwLNRZ2r_TC-TC45_wsVmeXzn3OSRmYJGKRG3JzpXK_FF8avNKylPgnI8y6Km40INxfj8lOyBnmUJHytGLY_h-NEA6roKDyTZsZ4_WrPz6OH20UCs2-PXC2cQJNErZqGp2BRgqctQBeXsWbk2oWGKAxXk4WhpxwKFN-K-ItY6SaYRO1qPVoEHYMJrX1FVpBOb4CHk741PsPy_PUgW-tjyfcWTSgXX9gJQoh450-cWpvvogpUEarWZuLuE8w-2G4A8deveubcNnM6NRVmp8NjfKa0PYbpXYV3SMGPjjeVg8PajqTztIIqIyVhw077ATBcf1c2PmD1OmOjkMUVlQU_EmOSxmU654d8vf9YyOAh57c6twAcDIXVWeir9nN5e32D6_nIsI4zGMZfWwO_ilAHTHxOPRmyL1Db7KVor0NaLUHFTFcODdmMBiHSIB7XEiTcFe1XoB4vNsVJ0Rvg_RMmGguUhn-TD98jyb-BrOHoUpwl_VhW3N-mirSBfdqxR-G4EKiLcUOR87lEO3fCq6LjWvT40vyuVp5JX_vSvsLmexM2sG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل‌تساوی بلژیک به سنگال توسط تیلمانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/97495" target="_blank">📅 01:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97494">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هفت دقیقه وقت اضافههههه</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/97494" target="_blank">📅 01:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97493">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو  تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/97493" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97492">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تروسارددددددد پاس گلللل داد
😂
😐</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97492" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97491">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کاپیتان تیلمانسسسسسسسس</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97491" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97490">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اللللللللههههههه
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97490" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97489">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مساووووووی شدددددددد</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97489" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97488">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یا خدااااااااا</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97488" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97487">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گلگللگلگلگگگلگلگلگلگللگلگلگلگلگالگلگل</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97487" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97486">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">لگلگللگلگلگگلگل</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97486" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97485">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0dcdf5a8a.mp4?token=JMcebbkfdElwGohqEDNIOlv9NU4L6sKv4ARGO6K9tNCLAYpAyue0kWQ18lhOehrvgehL_sQjp0wpyRcPFBbN5uM55I5zVhM_nOhHPW1r6-2N4r0k4u2v-6TzaN93TK8Uph54uBgsZwUPyzi6CPyqifYOYh30kqoDlybd5yes8ZL7QaxXqROfPhDDoGfXmEOkHvXBK8UcabomsPDxjjTi5IKrjBq-1l3bvR0Ubv013RXZaKwBA_cjVeHKpKTLT5C0pfQ-UpsCKV38_13VgXyPyZ1cXlHGgdvgGnc0UuUP6VqJ_xbcYJvg1DylzMFsHmw_JzZ9ODXeoa2fkCnxs7ZZTyeU5FPSQ0c_n5ryCRNV4k5zySkJDZ4o3T5pwhALKQP27NMt_mgXHdDTeTA_fBZp8BeNDyz6X6uqW2GslOq9LRHxPRR0SnA5F54g6QqEYzS-N5IAqGWoaqHzrHXCKpAPxUt9jPEpYjsobMIdyV0xp98IG7gJ1gA_ne3kQMv3NRpRIzNgZ2waG_O_7yztWN9DHnawopCyI0YZM31-6zUshzhg1WhYHiu-g5r7DQ_Sars4y51jEak2_VEgngl6dC3MuK3tOokVqfPO5hoXW7u3dFkJ9YMNhMKtIdc4AuOm7aSSOQFFASnEnaFjMhU0n3in2yVYhFm1TMkd_z2kR0ywSvo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0dcdf5a8a.mp4?token=JMcebbkfdElwGohqEDNIOlv9NU4L6sKv4ARGO6K9tNCLAYpAyue0kWQ18lhOehrvgehL_sQjp0wpyRcPFBbN5uM55I5zVhM_nOhHPW1r6-2N4r0k4u2v-6TzaN93TK8Uph54uBgsZwUPyzi6CPyqifYOYh30kqoDlybd5yes8ZL7QaxXqROfPhDDoGfXmEOkHvXBK8UcabomsPDxjjTi5IKrjBq-1l3bvR0Ubv013RXZaKwBA_cjVeHKpKTLT5C0pfQ-UpsCKV38_13VgXyPyZ1cXlHGgdvgGnc0UuUP6VqJ_xbcYJvg1DylzMFsHmw_JzZ9ODXeoa2fkCnxs7ZZTyeU5FPSQ0c_n5ryCRNV4k5zySkJDZ4o3T5pwhALKQP27NMt_mgXHdDTeTA_fBZp8BeNDyz6X6uqW2GslOq9LRHxPRR0SnA5F54g6QqEYzS-N5IAqGWoaqHzrHXCKpAPxUt9jPEpYjsobMIdyV0xp98IG7gJ1gA_ne3kQMv3NRpRIzNgZ2waG_O_7yztWN9DHnawopCyI0YZM31-6zUshzhg1WhYHiu-g5r7DQ_Sars4y51jEak2_VEgngl6dC3MuK3tOokVqfPO5hoXW7u3dFkJ9YMNhMKtIdc4AuOm7aSSOQFFASnEnaFjMhU0n3in2yVYhFm1TMkd_z2kR0ywSvo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل‌اول بلژیک به سنگال توسط روملو لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97485" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97484">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وقت زیادی برای بلژیکی‌ها نمونده</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/97484" target="_blank">📅 01:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97483">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">لوکاکوووووو</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/97483" target="_blank">📅 01:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97482">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلژیککککک یکی زدددددد</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/97482" target="_blank">📅 01:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97481">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گلگلگللگلگل</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/97481" target="_blank">📅 01:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97480">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
‼️
نیویورک تایمز: یه شهروند ایرانی - آمریکایی با تهیه لایحه‌ای علیه فیفا از طرف 90 میلیون ایرانی از ترامپ و اینفانتینو شکایت کرده و خواستار پرداخت یک میلیارد دلار غرامت به ایران بابت حذف از جام‌جهانی شده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/97480" target="_blank">📅 01:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97479">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو  تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/97479" target="_blank">📅 01:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97478">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyXsp-Hk-VG-ccWMwn3dz4C7KkzLCbqmm1SJdKduC691JJ6aYibvdsMRobcf6wjfEQ--a7pSBwCkFyaYpdyo8W3maNNvaI7CFkiXU22htmGHrzavsW_rvYvSgTwMi5uDrwrxhAV2pzd9AX1IMZ6RXsLLA3XAI9wLTB2EQLbcHsuKWPdRcRkVHuDsz42SVTRKPIhFaJJPX1Lreb4ldqevDfVdQHa6utqoXgXsf2Ki965xAf38vQ3lPFcYwKibilBisn0CeV8myDgVW90bgl3BkPbq6PUvvKswpDotAbIy4sjz8seVznRmq2VyazQYpKsnHRk6uX05cAxzycVtJgDWvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اوه اوه اینجارو
تروسارد و تیلمانس نزدیک بود وسط زمین کون هم بذارن که لوکاکو و بقیه جداشون کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/97478" target="_blank">📅 01:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97477">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52150cb58.mp4?token=KCdYixTKXuVupUM9IteYH7MclHsOtf55QINprVXRAlGoyEB45BNJotU8PwhD-tzEiEAygpF1mvoCb3ZFJoAIcsufdBLUs7alnZLlzsbns2UtC0SC7bSzRr1juDb-yNzwBbVh-Vl5cTnjLGb8UBVzpTtS62bS7I7vd0rpA5pm6wx8B1AGTgrl7H9ST4JK6vYI_oYS0__7LyNW0vX_xpBFDooIrcAzuVmYp4EMYCotbGJ9IjYs7HuC1cjJiyaVSOU-ep48B7ZxS0GRbqRcVYBIxMZgbdL6B_dzu8FueRBnWq55da8mnQlPvB1X_xhWABR6wuzOBfb9Zv0pVE822oHc3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52150cb58.mp4?token=KCdYixTKXuVupUM9IteYH7MclHsOtf55QINprVXRAlGoyEB45BNJotU8PwhD-tzEiEAygpF1mvoCb3ZFJoAIcsufdBLUs7alnZLlzsbns2UtC0SC7bSzRr1juDb-yNzwBbVh-Vl5cTnjLGb8UBVzpTtS62bS7I7vd0rpA5pm6wx8B1AGTgrl7H9ST4JK6vYI_oYS0__7LyNW0vX_xpBFDooIrcAzuVmYp4EMYCotbGJ9IjYs7HuC1cjJiyaVSOU-ep48B7ZxS0GRbqRcVYBIxMZgbdL6B_dzu8FueRBnWq55da8mnQlPvB1X_xhWABR6wuzOBfb9Zv0pVE822oHc3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇻🇪
آسمون ونزوئلا چرا اینجوری شده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97477" target="_blank">📅 01:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97476">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به بلژیک توسط سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97476" target="_blank">📅 00:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97475">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به بلژیک توسط سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97475" target="_blank">📅 00:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97474">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به بلژیک توسط سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97474" target="_blank">📅 00:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97473">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
اسماعیلااااااا ساااااااارررررررر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97473" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97472">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سنگال دومیوووووو زدددددد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97472" target="_blank">📅 00:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97471">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلگلگلگلگلگلگا</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/97471" target="_blank">📅 00:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97470">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">لوکاکو بین نیمه وارد زمین شده تا نتیجه رو تغییر بده</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97470" target="_blank">📅 00:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97469">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ut2sn2TPhmfwjXjvn4Ww7b3vHHqO_fNfQrIb_vPpoJiQGM8BBnf6i_wEQimXzWUy2pymqUHLPrcJwYd97Hgi5rRoXVDu3rknpq_slpt31T6Uji6-NefLH6DzkMJkTePCwxmGn3MfW5tquPFqtKS7vnf_a7A8D-HdxNqJ7CVZa88dgs0IPfHuCyIVmIY3_L8UoTZmw4BzQZG_xdSEdHok4tDoxevjxFqSUoJw_CecZYWzQoVSwh07-oStqPSPwK4ufFJBw9j2qRlM-dE4V1XAtVg8hTvZDCdqw29k3vvCJPjXyMYCKA65ZZq6YgfLwoDM4sdbq-IxFbNf1qy_UXmYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مارتینز:
فردا جام جهانی واقعی برای ما آغاز میشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/97469" target="_blank">📅 00:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97468">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3VR_k6Rx3iO6BsUsrJcfJpT5xf7ZL9pOAcWJLZECJnhqHNWJ45Pvl22NPifmIC9VkIzPsxilwML7pCNcsvQyZuk8Ix8ciOB_rYe7237xw_GTG13V1JvMLfruQui1RDr-RnLHsQBttMJr1PfqKf1_6zilruLNGz3Ywa6HToXwPE7npHTdW_6HhaHZqnRCBaKgGJwgyMANOZ2U4Rruz29M-dUtFS7eKs7xEqhxHiC162pGVWvTM8eXGQjn4jlo8vyUR9xg0XsMfxVufK4YJE7xiRqBLUNQ3d0G5FEhet9x4SGBFRYfLKUojMCMfaZ2XBCULd4JCZOv7QC2cYuavGPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
متئو مورتو:
الساندرو باستونی به یکی از گزینه‌های اولویت‌دار رئال مادرید برای تقویت خط دفاع تبدیل شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97468" target="_blank">📅 00:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97465">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bopFgr9pGbgtu6Qh6HEI3pLzBPa_s-U7_Fj2FXI53cQEt5JYxtWVe2nYMqwWZtoBpEzB-bDwrcdytp5yWJlt1UboZqH77mfU1i9scQH8pnnHiiNh8bkg5tQrmvYuBoPdviqgBR2FbFcVZ_z5ZWVgXpnjNf-4mMkSGHUKaMmd08lOkH_iBQJnJeXAjTP2UbwM_erENZUri7puHAj6EimvdLiSNBmj0a_lDVxeNH58OUVgs-0uVx6Vk8AYPYeWP33IAX9zvtdz1sOsmPIueRjaETHIauqwAU5d-owFVzfsnvRAENFKUwkWfb8VCaAqyyxCrymh9mirjQd3UPw7gkpaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ci4mbYO3UMrgCvgjJeB-sD5QnF0xeYB5mmD6OP04oK2g61TaJ0L13V1rSQnxbn_PmRG-9quPfaj6iMqtWmprmD5wirbvr0h8YTVM-qrq0MTGO5lIpo5fVCzZKkU1jZ2gY8fMWo7La2s0EsA07TcrM6iPHkvTYysfcf8FmZa6ADNvtKcYStQnoVkIH4m4UQr9oN4-l3dyyptPp2RXuxshhLxvqCFFmXsBTbYR0I39OVr_KHFMWdaa8Nl7TmbXxVkUnCvp8Un2PH1FPISVSvmvrEbo1EsQkEAcoy4QPwp9IgKVdHIyuljfoX-0R_04kyCxgVDWSal77Qt8Cin4K9E9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8DJ5OO6HuERq_0ad-0y0QRPef_7bBXqqBfw9z5N5AvBHRcRMVdiNJqJzWAa_K3z_GFxravXC8RWUsgPoJxUt33vVMzbitfYcL00cWYPlXql9R4VepY6mkPIJd5oerN5pfzU9HQihIfhJpQnWssvy-KmhKz9T1CiARzFvyoL2gPUAi5NZbiJH90175VzNR6B_0lHrGjh3B7uIyluBmJRn9a18QR-mSBJw-aeFtmGWHFs6t3Rztrxtksxyxk6JohQTJrDjnYR3Vsif7HBwnZqzO4FMvR1DuHM4UBIn9ua-u8siTzEqSCNyMR-x4AoeNRgZKJD5ovzYlK8kHvsx88THA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جیمی جامپ های بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97465" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97464">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR4LS9hKb6u0BfOcrgDrFW22jiJQiEJ0-zID10Bg7GjtyjCMfAri0ekikYdccsolTaUFFGd7ec9YQIKkh57ALtPBXultufXceDYL5RKg7HZnwzAzbkGFT3pvEBk3aoHeTVIabtPo64aNVRQRKOHa6X3JOnRFJ0hh55h8DAQI9bu17bRE-gagc3QgbhdPO5OZrYmo1eb9kz21EPHuphYbvwCwlGqSW5ONySnyN3qshH1TQJ_h3YOPqOIpqxXUJsvHM3BDdvIt2gF0ZjDIRecox9TG5fheaHuJVd_aedIZkLpQBcmCa3ESD9YiHqKGsuhdSTo3NShExLJki4GjYaemMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری متئو مورتو: بعد پیوستن تونالی به تاتنهام، کاماوینگا هدف منچسترسیتی شده و احتمالا مذاکرات بزودی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97464" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97463">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
متئو مورتو: بعد پیوستن تونالی به تاتنهام، کاماوینگا هدف منچسترسیتی شده و احتمالا مذاکرات بزودی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97463" target="_blank">📅 00:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97462">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گل اول سنگال به بلژیک توسط دیارا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97462" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97461">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چه کصشریه این بلژیک دیگه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97461" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97460">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گللللل سنگال زددد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97460" target="_blank">📅 23:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97459">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFSdOixjcETLAGGnBHNdyWxQI_AGotsMozT5vniJYpK5pSVZpObQnJpJpG0vQpKRg2AF6CaTBoStmf66XCnaAH-IgxCgSGBP06-FPMUMVwWUhVPLx9FJqtLmcHuOFxMdIFIF8ijkQZ2EpE5bzPKsLv7CU1F0j3XdN_zt6NtPiPoXZK3jtS_uLb9vs746zBIz8ud-H3ig6YkT9g6b2iKlq7kdaoeVsVjzZJ7zTrsB3yl03RymS_8DJjy5MtrmJpr6EibMC3bE72lxx080g1WLxiii7Zjqp52QVQ3K_atxpLLteatHAcXaaGTc19EPGV7leLFIdhBxBKAsohdRq6M_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از شروع فوق‌العاده امباپه تو جام جهانی، هوادارای رئال یه طومار با عنوان «کیلیان، ما رو ببخش» ساختن که بیش از ۱۱ هزار نفرم امضاش کردن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97459" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97458">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a16ec06f22.mp4?token=lABwlCKkcIDxgA7-Tlv37AXWZM8E8WCc7jKzsZMDaz5ru0XNBHJQeiRtr5ipSXBUaX7j1R-sDP2VFy2F5zl2LjChdB8ePvgaMcYPh9HfYDHUKqSb04KQpgfzQg0xjqOtPmxs53ADUUmGlupjR3CfrI2MDgg8vqMTLSt3ZhpZ30Kpg9pX30NUF-1Hjr2FmB8N2DN2U4wxQwJzRzDtB9-vMW0gJLjwE_bOdwVWMfnB2w6cVysQwOXCOuqt2RVzMgJfYJWEnV1qJPgVPd6IHXBaQDV8nNmgQ2RX-e3r_33gEK-cvnMHvs3cMwt4UDlDqEypMws6fyjccPfhVp5k42kjx5mDh_tW9YVoJiItl13ojJdd5j6VcikcWBDGA7hrrYw_QWk00EdU1zCzP2fUrRYwb1mwzpufg9nI0prKovqFAnvibaIdYxX0bA1T2vswMl_E6KodBVBnTxR6ZpmETD-qLIq3-l2o3pyt3btXD9EjsDye6fi4e0JDrGB9Z_NVcIqLXtHpR3vz_fWMtuERU9nzbJiFfnzwarcjibmQ4qkDO0o9b4ahS1Kug_IHyR_biZdI5YN70PTr8bpnfrSlq8AVg4Rdb_jgJpdqdyuZUUdTtq9cZVD9njA5LNlqK-lDnACyXAifqarorIedprYPGLPL2EllH1QsC5ndtEKCv7dC_M0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a16ec06f22.mp4?token=lABwlCKkcIDxgA7-Tlv37AXWZM8E8WCc7jKzsZMDaz5ru0XNBHJQeiRtr5ipSXBUaX7j1R-sDP2VFy2F5zl2LjChdB8ePvgaMcYPh9HfYDHUKqSb04KQpgfzQg0xjqOtPmxs53ADUUmGlupjR3CfrI2MDgg8vqMTLSt3ZhpZ30Kpg9pX30NUF-1Hjr2FmB8N2DN2U4wxQwJzRzDtB9-vMW0gJLjwE_bOdwVWMfnB2w6cVysQwOXCOuqt2RVzMgJfYJWEnV1qJPgVPd6IHXBaQDV8nNmgQ2RX-e3r_33gEK-cvnMHvs3cMwt4UDlDqEypMws6fyjccPfhVp5k42kjx5mDh_tW9YVoJiItl13ojJdd5j6VcikcWBDGA7hrrYw_QWk00EdU1zCzP2fUrRYwb1mwzpufg9nI0prKovqFAnvibaIdYxX0bA1T2vswMl_E6KodBVBnTxR6ZpmETD-qLIq3-l2o3pyt3btXD9EjsDye6fi4e0JDrGB9Z_NVcIqLXtHpR3vz_fWMtuERU9nzbJiFfnzwarcjibmQ4qkDO0o9b4ahS1Kug_IHyR_biZdI5YN70PTr8bpnfrSlq8AVg4Rdb_jgJpdqdyuZUUdTtq9cZVD9njA5LNlqK-lDnACyXAifqarorIedprYPGLPL2EllH1QsC5ndtEKCv7dC_M0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
اخباری سرمربی چادرملو: هر انتخابی غیر از چادرملو برای آسیا، حتما همراه با مفسده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97458" target="_blank">📅 23:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97457">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبتهای عجیب ممبینی دبیرکل فدراسیون فوتبال: در حال مکاتبه هستیم تا AFC برنده تورنمنت سه جانبه را به عنوان نماینده ایران قبول کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97457" target="_blank">📅 23:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97456">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمله شدید بابایی، مدیرعامل چادرملو به ارکان فدراسیون فوتبال: اگر گل‌گهر به آسیا برود، حق مردم یزد ضایع می‌شود. حضور 40-50 روزه ممبینی کنار تیم ملی چه فایده‌ای داشت؟‌ اگر یک آرایشگر کنار تیم بود در آراستگی بازیکنان نقش داشت؛ او مگر شومن است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97456" target="_blank">📅 23:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97455">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
فدراسیون فوتبال پنج‌ستاره ایران ظاهرا حدود یکماه قبل اسم تیم گل‌گهر رو به عنوان نماینده آسیا داده و این تورنمنت سهمیه که برگزار شده فقط برای ساکت کردن پرسپولیس بوده و فکر میکردن قرار نیست براشون دردسر بشه اما حالا با قهرمانی چادرملو توش موندن که ببینن چیکار کنن و AFC قبول نکرده گل‌گهر رو حذف کنه و چادرملو جایگزین بشه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97455" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97454">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شروع بازی حساس بلژیک - سنگال
🔥
🔥</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97454" target="_blank">📅 23:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97453">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzU-SInwI8nLhzFpX_338KCg-vI0LHVzteyOuCPkErB4kBXxGXbw0Md227DelH0ZgFlJiY_GkzD1xGcy3_kelh4XAQ218s08mRnRAomMqO4DF6O70_JSEfKr8NLh0PDgsGzY0B2aQ1WDbUJ_wlXwHGZUDAFHeX7D13EYNqwRz0tMK8GKXWkZnywAQWl2xQo4txKbo3vxxXQi8OT9zNpWQiBw2kMp-tW1WgoMnGqgmHS9hc37gh0fiWOwiWSzntv6G5qlGnCxZiW65SWTLSj6i23xgkp4iuiyMLH25bYLxeCgF6nSa7msySd6NAD3mSv_n4as2rAvQDTXfc-ZzBc2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ لکیپ فرانسه: میسون گرونوود انگلیسی هدف اتلتیکومادرید قرار گرفته و مذاکره نهایی با این بازیکن برای جانشینی احتمالی خولیان آلوارز آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97453" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97452">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmtiF4_rCp7SV4KWbZfCHhherKEnBD1s7Z8uVkiD4op13CWOKsEmuGsa2Ord7JJs9atbV3LYvaehCHeanRSd_vns0JmX9nEyb7QwZYblCY_qm_aBSCMmtfaWoxfMSQEa8Hsj1fwjqw_pjRWytecqnmZouj0n4Vi_2f09wRckjhBvB2KM3bsaiuYm5NMSOpwfIppGaSWuCwOXItNofCGKsXhWboAgeEkr0KaFKd4bAC3ZVJp3dhs6FTvcRNGZIQx1FUbCcaxx9MFdgAc3rCIC9Ule0DK3twalEKl5rkbN9qU9Pq1_nueCAxFuSFx4369txcK-LZwNdD2FS7Sg8MGkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
توخل درباره هری کین و امباپه
و مسی و ستارگان بزرگی که گل می‌زنند
: آنها همه مثل کوسه‌ها هستند... بوی خون را حس می‌کنند، سپس حمله می‌کنند و گل می‌زنند. آنها جلوی دروازه قاتل هستند.»
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97452" target="_blank">📅 23:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97451">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fee1b4fa7.mp4?token=barbeL7DTjRmlXyR-71T7aAgAorbTCOWH7kkqA-suIYjwcoP3UPszSIG6Ir5zN2gr2JvDroEmnHj5XC_OpwRRG9SB9tWMxhrPqvhsax4YdIkMkA44Bo_hatIEY_ddP52TyfyZIxEzljp_j8i_o35YDSTgpRzhHDmc3U_wV-09N9_DiJITUjHcI9P4hSaoPxX9G7m32mka8w_WY4j4QyouecAWYlCqRRsQ64RhbCg93UIHFIx93aexCjRirN31wl_wNgf8PvQEu6n_bDBvBij3djA3hrxIdv3wNFKwbnMc4YU-tuZ0gBZUq0s9wmUqHmXAW61dVF_a07C57TQ0r9leg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fee1b4fa7.mp4?token=barbeL7DTjRmlXyR-71T7aAgAorbTCOWH7kkqA-suIYjwcoP3UPszSIG6Ir5zN2gr2JvDroEmnHj5XC_OpwRRG9SB9tWMxhrPqvhsax4YdIkMkA44Bo_hatIEY_ddP52TyfyZIxEzljp_j8i_o35YDSTgpRzhHDmc3U_wV-09N9_DiJITUjHcI9P4hSaoPxX9G7m32mka8w_WY4j4QyouecAWYlCqRRsQ64RhbCg93UIHFIx93aexCjRirN31wl_wNgf8PvQEu6n_bDBvBij3djA3hrxIdv3wNFKwbnMc4YU-tuZ0gBZUq0s9wmUqHmXAW61dVF_a07C57TQ0r9leg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
Senegal vs Belgium l
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97451" target="_blank">📅 23:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97450">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc4ce63b.mp4?token=hLEq4lUTPITProcruJmC4MFA-jXL0h4qmUxKgvpUZcZ-Iy2raVOZtk2-VHb9pRhrKF2zilAGJSoHIyoc-YgmIMTB7f5FCc5m3i8xy1ujSIUa5FO7W5oLW_2eaYB7IDMCgaBIzXa-qoWYeLoJbP1HOUGWky1nfV4oim7nt4U3oq04OQokjuuttah65tLVO7H8eBygxmk2W_-X6vg0dtPorTqKT6yjD80ix-FGg4HSQykiN-7KO8Edtg112XbEoMnLce7U-U9IybvXaVB3UMLMt6vwu1nBStFXX45HUc6tpqepitVDu0YxaVxTUOII_aanE_7YmUyXHXnZvj3lK-rJJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc4ce63b.mp4?token=hLEq4lUTPITProcruJmC4MFA-jXL0h4qmUxKgvpUZcZ-Iy2raVOZtk2-VHb9pRhrKF2zilAGJSoHIyoc-YgmIMTB7f5FCc5m3i8xy1ujSIUa5FO7W5oLW_2eaYB7IDMCgaBIzXa-qoWYeLoJbP1HOUGWky1nfV4oim7nt4U3oq04OQokjuuttah65tLVO7H8eBygxmk2W_-X6vg0dtPorTqKT6yjD80ix-FGg4HSQykiN-7KO8Edtg112XbEoMnLce7U-U9IybvXaVB3UMLMt6vwu1nBStFXX45HUc6tpqepitVDu0YxaVxTUOII_aanE_7YmUyXHXnZvj3lK-rJJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارلینگ هالند 26 سالشه
‏هری کین 32 سالشه
‏کیلیان امباپه قراره 28 ساله بشه
‏لیونل مسی در 25 سالگی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97450" target="_blank">📅 22:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97449">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxdmcfPo1qRYeRGaebOJX_FEm20SFNK_zsqKWG-VW2Inp7dlKB7-Z9SkX-PShSGcKlqPs_9lVpurg_UI5QPXxZJN7Vg2GD2fF9RLIZ2LfTufIBYPrlMpmUIq2m0QrTMIyfyNeXOn5yDgfgnyCX9GO75MlWxYweNCIR7nqJ-gejHSBDLDQjk2KmVey-KY7xZx81oV2zfVsjBsHwcrJgxXHtAUkrrOlymBDeiAlNOYPBD8nVmtcMK_DKuBjeBGaeo1l4jFnxZAJ-n63OKaU_C-2F_RJsqhQX95jTEi--JG_fJ6kK6bgisO_2PzTB_RmtrCX4fa58JBBqdNEpPpTbByEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانک کسیه رسما از الاهلی عربستان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97449" target="_blank">📅 22:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97448">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNlN7KR1hT65z1F4XIb6lpqUKwl-ZSzZKNkGqntUMhJX0JYl-972Ze46TJVSiBYH5QLKAEphpJWFtz4pEJCQlOKIMgYcR0MXc4wdHt2K-P-6Va9yctOBzk75founnHg0sbWLaOtUGOpd-mOoVI4ByJ_WgMBh-4XjxNB3HXvUzRND5kXbT5UbCJRSB_fYf7TSOHIOxthU3WDRAWrZEbyq_J1o8Sf7R9Rhusgrt5fTGESpGt5HRitp6e98J9mHDtibxxYrjXSts-ulxiSG0cF-U_PP1IeI114NQtiCuW_wHDI8oLjioAESezqPY-9R6IrqYyvfVebNRWRpv-3pTAn_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
خط هافبک تاتنهام برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97448" target="_blank">📅 22:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97447">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇩🇪
#فووووووری؛ قرارداد ناگلمزمن با آلمان بزودی توافقی فسخ خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97447" target="_blank">📅 22:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97445">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KHcLAZIABikBDTSVHRF5fePgFYfglLqd1TjSEs88EM8xM2lIwnJVUyJ3WRHlDqaBvZmvME89-nogAWeNvAJwLB9yDKijDiY3W70bgTraHwKHfpBTbtShDGfrcsiCTsU0Fm4RDaHcJk6vBw2U0KPcdEp870Li7mGf5d8bcvJ30QgAjqd-71w-8Glt8J2FVVOxxUbZ2pQG1gJ4doVxRxvfnhvdqWLxhXMD2eAU6XTrALuUxTfDfMvEhY_-vOVPArnPXm858dH4rKIpnkR0TEOlFzGUYn_gVOAvhbICMpt6-Vczz9GA1UWDivcFK-R8mQnH3iO7AH7plaxZVvOBpMik5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V4qyVfu5V2Ji_2TTIlThUAVz7V6xvW-8_rZ2PQpUt-Kz7vCvGK7oGJoC-_BFcrhA-ZoQBixAj813xBfJ2B8UrY2pFlgUZ-NrNb4mN3cGs8MxrERyN4XlE0dwpambVsiHNWEIJ8C8p4nUoIfZxmFlzemeCtbugGBojdpxs4o9VujS18X3jONeM2H2vJarqKJJBY0og1XaoIaUAlghUtktSKF4ojMBqb4hN4boZhsatPx8VqjYvhlyq-gmOhvzJRiBQsla-i4nqI60U9gkoJ07RvVrSDTCXIYOO5Z5Hs-WoGnSzjcWg2roWY3V_o1h55frWkr5SVOhmJ14xqLIFY1t6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
🇧🇪
🇸🇳
ترکیب بلژیک و سنگال؛ 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/97445" target="_blank">📅 22:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97444">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT0KV_0dI9tetyrvTYC0X-C8B3a18WKs3NCSfGOk-MRWYutkeySyly0PyN6VLMsci5_qMjr0D5-cdYBPw6eWTZ4fWfal1ibLDdv6zMRgye9MR2f6hJAcNymRAZqfslpQOYMs9tnAkqxH9eXeH-pPYck8ZkxFD0SEMprFca8mjivvjqUbMIyHL2ADNvOF6RDvhvHdrJJsfZDCWEosy42c-I-LNJgGEXUEDf1J19kB9ObEWWXT6cpHmvYNnICpx2daT3drk0X9hbDrl7pzGZ50VNCATknX3ppnkxCmTFVqxQps32ZH4XWp7AbDcbcNX640FMfvdX7XWqD0kp8SGMve3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فووووووری
؛ قرارداد ناگلمزمن با آلمان بزودی توافقی فسخ خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97444" target="_blank">📅 22:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97443">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddt7qnrIC9tLO-Q-V_BG1kC-5-ybfj5Vf4vhNlI2AFreTzVGEp3tSrFsVfJCEDRQRdM3ibAIV8rfXNesOjgEoBhG-FaBvzvIxLTDwCN3luJiZBz1-6Cv25o5GZGksWCWy0PM2Rmy0LZSLn1hSIZ8S-sxBLWt74RpLQ4LWciqvOu8TL6rYAsVCn6gguFIg88oOCXAMrWoe1fliPZaeNlf7aU-7tNXaJCrmAMYLvSCx-ZpIR4jL2o_iCNeLq6oJUdTPDJOFRTTWQRA94CGhC9i2L23RPbXaABpNlATWiuBvMPt9Az6wxhAyc-fdUCa9YcW6UKVuxwcSzUESZ86dKmKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
گزارش Bild آلمان درباره وضعیت مایکل اولیسه برای بایرن مونیخ کمی نگران‌کننده شده است.
- شایعاتی درباره این بازیکن فرانسوی وجود دارد که گفته می‌شود نزدیکانش معتقدند او می‌داند که می‌تواند با بایرن مونیخ قهرمان لیگ شود، اما او این کار را قبلاً انجام داده و اکنون جام داخلی را هم دارد.
- اما قهرمانی در لیگ قهرمانان اروپا شاید کمی سخت‌تر با بایرن مونیخ باشد.
- شایعاتی وجود دارد که او می‌خواهد به باشگاه دیگری برود و رئال مادرید باشگاهی است که باید به پیوستن به آن رویا داشته باشد. اولیسه زیاد صحبت نمی‌کند، بنابراین نمی‌توان صحت این شایعات را تأیید کرد.
- با این حال، گفته می‌شود کسانی که درباره او صحبت می‌کنند بسیار به او نزدیک هستند. این ممکن است برای بایرن مشکل‌ساز شود، زیرا همه می‌دانند بازیکنان ناراضی بازیکنان خوبی نیستند. انتظار ندارم این بازیکن ملی‌پوش فرانسوی در آینده نزدیک قرارداد جدیدی با بایرن امضا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97443" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97442">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97442" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97441">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDRXknPG4Zsgdav7Ebh34sGTRFZ52biN-7wDpnCRwazTx1aPLwCzxzeX7NwziU4jfDpXziwK36DLtjVR3pxfqj5W1a313badhYO374LhmNOX0dHILViZ4ZGlj5GA4J_QLP_hdWh9VowX5Bsu3fHQTckezi1EG5SqB2KrYtqBeQDDFBT8zyFz4KMOG4QizKSGpQv86JPyeM4L7EAhMW3-3hc8Ydwlebysz2Cv9CUjfb_ukL-rb2W2f3DKaLQ4f3qa1p6tyOfltCpHOGZ7-a6912rM0QOeUvWjtQCfdabIpgH3YAkhA0KssnvFuRd5PPkgREZuSzGE3t7R9KpXNBh53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
برترین گلزنان تاریخ تیم ملی انگلیس در مراحل حذفی جام جهانی:
⚽️
۶ گل — گری لینکر
⚽️
۵ گل — هری کین
🆕
🔥
⚽️
۴ گل — جف هرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97441" target="_blank">📅 22:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97440">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su_DTFhGhQJZCAeRjPxv9CjrAGhTuWiTKKutK3xUDwjAjfLUyITxZgTeMSKHJdvVEbAzWLiIzf51xtJ3MnwXk_gp6HQcwe9HKCttQy_FLhxSQyoPyo1oOyDIeWjqze4bIWJrLUsu1JnkLpJtw7tEjrj1NigVbVnMHDf71TLlNeulWnzVKGBbeqkMrNi6-L8RIhI4i-XEZj1HH17zySxQgApuAv8FodkGA8-i9IXstPvkDnUCUR53tWUK2NQHPBknzHzuOnbX-Nm0cO6kmTqBHnI6HSyQOvHswXxhSd1EU8yvTF65Q5Q0LigjSlk_FYnS_1dlJTYRszfWgtqQnwVoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97440" target="_blank">📅 22:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97439">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv7YespFt7KXboy_WBKS1h7fYf3GvhE8MI-KSLN6HO-i8RXhhGxEUqGLBi5pGqBtbashEpnD9yy_DAx4MnzlnWUgMUkHbM8DBm5lmsbeZagfVZMoKo-07JJpdcxJhk7qFt3EmU86XP7__dWmh_QDGFgLXK79eJ5agpwAFrtvOEop7ugRtm_mG89aXanq8-wacVJlMgZak6EtbuPKtTTbs8DfLHBzueTH2xUjjS4fKsLOX_qD5sr9rcIyJyM6U5ikkmZchnoByvyZuRXF5HrdKxnHrMF-rxRWouRvk_rWgcZpRINb7U3kVJ7S9DfeZ3jhj2Kj7UHXdqpSZCgGMU7vdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیکتاتور هری‌کین
❌
کاپیتان هری‌کین
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97439" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97438">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5s2TGI1U_SM80m2t-noP3W7vuvT_PjCYhxfZq64DlqbB9escx5yyHDrpE9LD_Ren_IDhDUAsIAXXEgs8hKUVdcdGGo2OMUxFk5JiAk1e1tkMPmlHWpp2Myr0S-eBuq8L0gfRT0buLb_HAoY_oM91TMnS_FHHo7T-OoESeD6-FN92FNM2P7bwi-mZ_gekFM7jTpqQ9MdDYSRZcCGrF8z1x3P8MeGZ8LaVbh94ni5Czg3aYHSrF63BXRiIZIH2NgQdtHMDpdMbEDlKYrEnaS6vG8OpDPytb9AFAD5U-b2sXYg8KBAHAt-BD5wgaCKKhBNtSlTEy158CECiwLiWxH7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
🎙
اشلی کول:
هری
کین بهترین مهاجم در تاریخ فوتبال انگلیس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97438" target="_blank">📅 22:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97437">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5-Af8vimrR260e2C6AW5FIPYUwGWoiBsWPTOGWxtv78VYicT56L5ukonbFL_QZ5roSvFhDjph80FHy7wmdFIQa0zlX_8D7uZ3goqzHCfiwjLshsaqbnFUIVTGs-8QKNHBZcpqd0w-sDeCv23inadzAsMQ7pJVzqvKzBan-G9un9Arai402e8GIrgC5xC7GoFxTlW3KZzdrMQXV6Ftoly5_sWNUsM77CIO3wnNwSUCRs245RWuymSqahMuZkk2Hi-5ZNM9_tCPes_Tq62KGHZiSOYv4QbCFJzvUMyPRY17VvDhvAv0pORLhoGg1eUdgV5a5r9J-rRY1luw9FObWgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار مرحله حذفی جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97437" target="_blank">📅 21:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97436">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brhKWbBkCeaH5EWw-M5M7i3HODrSJbW5YxC3A5T3yQx4Irc2-m6TbcYCvP358zSnU3F-ocKopV1OWik9z67ftFdw5kP1x2gfkLx7YILGf5Ra54Sat9iME3qLnJYWOL28Gr5ZynLRXosW9DP1eyA4SrBzLy_wR3q0bp34A_NVuo5NtrmJal58yLjfHWt8WYYzloof_FhrWs9Pk2_DJb1KRfqUm0Vt9irhOOcqzi4CHTmFb1MLeh5uWcbUcoGm2qiNv-XTv5TsKY1tgikrqTyWFN1ht9QWpAElSV1iWW0t7gpHp74ZRNSpji2Vd4hDaiLIeTURYX6fM3PPISQynXaWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار هری کین در جام جهانی ها:
15 بازی
13 گل
3 پاس گل
بهترین گلزن تاریخ انگلیس در جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97436" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97435">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEo4d4BM2RYRDp744hmkWuTck_4v554VTfO6RobjTbv7Q9EuwGRaNeN8pFptNNsGMqSwtOiikOCJxiibUQCu8a7BskUAY-kbKdNJ_eLIpZk7AsMpgxiOIu34rkBbIze-R80884WcDXUqgkbRMBH7F3mMHm4Zkj4NXVQh72s8HSPVtMLItwj1DRdD3aYZDA2SWB-0aufgMUSmxCafsau_oAKYVjuKlOVoM3YnlcZC7FJKBdL4hvaHmyJOSkb8BU_IEQkqr2GC997JZli-83ClEuPCgdmA1Z7OXNAkanxTuDZWZB5eSoFZ26QSlWCXZccWQR9ltNCamtTXYYfEGwhHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚽️
جدول بهترین گلزنان جام که شاهزاده هری هم وارد رقابت با بقیه ستاره‌ها شده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97435" target="_blank">📅 21:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97433">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yeww7JOOemsI498xVMiubgaa6tDpvncV3oFP2OQ2dzkDRyP0OwNaBNp6HOZYhtqaIdKaFVNeVYlkC5WC7H3njUmWHzKTd-y-WFGcm_s2Bk4BP66Y0fBoe6NNehcmeAf2aV-xmOQUC06mDhH4KVrqj4CHRclDDRKFNXIS1UvxHqoFRhXHBgrtQXRYTa79uHuUUshqG3a8qaEpJMbcS2oVvwGI_9MxiOvoL_ViKqJu6jgFyn8pMUhZJLi1ETp6kRI3cAhFCuD-0gY_DIhYR1KtxiKzuokPOcArBfFhWllsqES5GhYG7OmsIARti87mJQawDhwSnBF38IjOQe_QSLrclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFnSvTX9_PE5wQCAZd6znltTYhVAqM_FVbjHOcmdqQQ_0n2ZVFALNicozQr-mzWFftiSPrfLTnK8km2VmZMRd9YqYEB7X_L_A81gehMW3mVSeByJ9kkC8esL__0DW3whyOHBHJIU_8VNIEyyXwruxde8uMfTRqEi_vw_xVvTxswi4KiNAV2Pdz6ib7mhIFzQMtdGVsOzMHT952ralCbWj5XGz5w1wk8xAIekovHjGIMJsyvveEpzhYmsm2HZSALHjES9zOPmXMhi2lybuSIdSGVsYd7fwJupwq93dOKQxYzZttWbYgAet5RavgDsS99m51xzrWk0Sre7KFMw44PRPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🆚
🇧🇦
🗓️
۱۱ تیر
⏰
۰۳:۳۰
آمریکا
🆚
بوسنی و هرزگوین
📌
میزبان در مسیر صعود یا فرصت طلایی بوسنی؟
آمریکا با حمایت هوادارانش برای ادامه مسیر وارد میدان می‌شود، اما بوسنی به دنبال غافلگیری است.
👀
⚡️
آمریکا میزبان صعود می‌کند یا بوسنی معادلات را تغییر می‌دهد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97433" target="_blank">📅 21:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97431">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw5sk_A_8GrcIi5KhyLHGpq076d6cG1VDcOmhjdcBeJpy4ySKNv2D8ILkmL_A3-LFhDdUnAlIO8wvEamZxkhUz2sD19MQW-25eeaRiN2Vywg6AnqKRBvkJLVHhtiwFSymmb2q7-BN1sAhM5bq5IfWkRwbsgFAku9iwkPY4c56Sl3AmAoBgzN2UHgB_2WrBs-8ES3ieyfoOQQET8bkqJ65nMZIrYBBphg7VJv-cyKJuP-i98pTI9UYuS_VxT2-y7Qtj6_Xp-RCKGHRoeF3RCmMPfOKtxmFLNboCiV0PzmA2otNY_DtgF6o7_dzLyDuDe9trqD4gdUFs66ZCEyUX9u5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاپیتان هری کین پس از پیروزی:
‏
🔺
امروز جشن میگیریم اما تمرکزمان روی فردای پیش رو است.
🔥
🏴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97431" target="_blank">📅 21:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-ArUew_jh1p5pK-yYR1iulFTTPUBdzCe0eXEPckPbu88ZrglUuIC4z3FDIjLyJ3gA_CsW3Z0rU4MSIxnusfO6KWY2wQ7aP7_poXswew-GaSs3VO2FHNWSH06gYW0lupKxrg0EzBq02vZX-WgqtQxLVMPyKbpr5xLcayq63QutKWmXOh0zdh-DCLPloTdotBrlpZG71G0nC_yHdlIxOAmXKqb0YKcrmtLtnkpOXr8h04E7kTEHlSbiGzrfOsxRwXeq3l43s37SpWyxnruSeOEIdRRheoBL794b3AinHviN5NKk1g66KynJxUmxHjyv0kMdXaCffLnsXAnG_9QxH8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴
آنتونی گوردون اولین بازیکنیه که به عنوان بازیکن ذخیره در یک بازی حذفی در کل تاریخ جام جهانی دو پاس گل داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97430" target="_blank">📅 21:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btEc2_hG684xFtV8mczCDzLAaldyK4PvJh63mGZhw2yc6vQ7p4r5SsoKHuAyUXutTaUQhiS37zSaNbPg8TIy7FWwzAgp6k7GkXMGkprAdxWawwUBEWg0tOWai6QU9QlkzJoRQnye2NvEn3UzqK5wPi8hWB4UksvM0DrYlORVb5l6WSouuVQUVy8lKInVB4mZcd3_XBxKJeSrE08uMWWcESbpxzJjVwU6oEfMmYOMtIxFy8u78mNPfPP9FdHAFbvpDomXXAKfIXaInY54AYDz429cThBvJWiknUMgXQ1akQDo6KoWNGcqmdO2pdMEQRvnSHsaUSvIH6X0Y64Lp6ZBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان هرگز در یک بازی حذفی جام جهانی مقابل هیچ تیم آفریقایی شکست نخورده است:
◉ انگلستان ۳-۲ کامرون (۱۹۹۰)
◉ انگلستان ۳-۰ سنگال (۲۰۲۲)
◉ انگلستان ۲-۱ جمهوری دموکراتیک کنگو (۲۰۲۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97429" target="_blank">📅 21:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHwZgMVClLUvISUp1hN341ay084x9tX5kr6dTkk7TKrYQJ7SMcfzzM0YipLZ4jagkuL8c8M40_-KGKzc8_9hvd4PxU7YiyiEq1BNm90-PPIp8tGuMG8zBRz4uy7X9JcPWCBrSeeQHLA6LGtUlm23qq1JxW1JnKc6x6RG6ZwO59V7b2Ilw8t0DnASt8OQ994qD2VM0p2ixa28g6BVx_xlTaQmfaPg-lQZorMXI_F97JC3y_DHugtdxG_C3IZcuUrVWsUUckIqEE1kRrSTBYDv-k2a8gLGFvWKLB5LSWfEFzvGIk5I8aAiSDaARoxkiFC9EiUccyECh1uBX1W0-7Zu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤖
هری کین رکورد خود را به عنوان بهترین گلزن تاریخ تیم ملی انگلستان در جام جهانی بهبود بخشید (۱۳ گل)!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97428" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97427">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9FSenmsAtUASLFe2st2BIXFVb-dY2202rRUZm-e5eQ2VyFWNeCUnXovdC-V6UZkojE-LA-cHBT2NEb70YfdXZdgVj5vBekr-nuEvxJiAFbRMyeTwXkM034BeEigO9x-2b2sLTa9hRE8Y7_NPXVI8BqtiIuZ0N1EVfMSGxF_AUubWHMaAE0utIz0XfLdj6GSNZ-e7_5xCThy9lj7kHRpbtvwbt3tjvIjM9z5jLMtLy27xgzEONOXQ1HAIXhsea_Oz-oFoy95bNpWBAWwgpksv0S5Mh9ZcQpRhw2pV7wGK66OsykTa4NYrI_xWUdbH8P8lFb8gZkKlf7nObyA_KIDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
مکزیک
🇲🇽
🗓
دوشنبه
۱۵ تیر ساعت
03:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97427" target="_blank">📅 21:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97426">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp6k9fmDt27CeTeZstNFK5tnbQdEMSvdxcLdFmdesLPjXqr5hqon8sEeZXmq_oUj8GwlV7ZgzKh62jUR-gVmGWclkX4O7idkjIY-aoytN4Y-9hmaAIzgXiuhtCAeOEvG5CXxHQBI60epuVTZDn3-p5fJixAAugrpmNCvytONThq6TOigqjiQ-8csN0gl5gcXC4pXIqMiUysCi90aJEJGHzBJ3sFPePTJMM8Am40aJm78EaoVoURR1i0v4iQFdGrE9M4dtqQofIez1jmkDMdn7qYi2NSoXadWd2Yrs4PT-dPNGmp2lc54LV6Wx46W6efQD_d0EydA2VJncgDPD7_SNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ انگلیس
😀
-
😃
کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97426" target="_blank">📅 21:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97425">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxyPuefDw8bUTcPU83lVWo0PBMEjDrXEk_mMfMEgxWAThwEWuUgY8KN76PGCqG7avq5ObIpw9X_M7ForzjxkjDwXdLPJzw3pvV12Iftka5G4Gexkrt-pCBbwJVP8_eNuIUHCf-KqXIE3mNSDfRslbbu5x9qR9cUCwavsDgfXYOwODGGF5XL5P3lQiK6QxUXnY9MtRlf03C8Z3RwF_1RwAuyzdl_rRUFmkY8Slf6k_1fxgQwoqCZlfNOYlrNj4SbckDqO91tn6P4qJ63cTQdgmo9ugm-stloF5W7b706DfCn2YJ79nQHiEQR49d7lV9fLzWvPqHg6vBDURGshuoqJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوردون بازیکن جدید بارسا امشب دو تا پاس گل داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97425" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97424">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97424" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97423">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exnSfqvCw4JBthE6JkwFjvW1-IHzK5biuA8jCnt_qSvLwoXFU8U3Dp-gi3vz5nitzTBw6rKTkC-3JMyDg6Z6NN9eHLBbpzZkAPF6CbUdQrD_cMf4PTo5C31TZMTZXRu8ksgZ7CVd-_M9kUq5Gbb6Mf-bnOWbERtTDFCbQG0c4ws0a2yPpfms53ehC2LBdozARmBntUpX90Ln8mSJkOn20uZBIPuyMySYpOe145T4QdWNVW852xCsosOp2E3Vt_oAZUrMAZCOCHSmuoNho1MST6GTBUh0_sALTsAuLqpANAziClybbRbROwuoSsAide_CYnY8M66R3DTiAhmvXtgF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97423" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97422">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97422" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97421">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5faa5495c9.mp4?token=O-4t6A6oPBi5QW6cD4BC1tpzdPPV3d3gonNPr1_BTrFQwyg1UeOEty6Qprd7IT2wU6JfSp5T-YMP7vheBVGfBwSdeuvUokNVqX_e9J5iga-RzwES8aKGMYkyHvFB76TRH20uf8eZA_FgCm_cz1JI_9wLDifBUV06pqHKZ-zQSUmVNaxWNw5pbf67OXXq8AkicwqpoAd003yKIPdpcFOoTpJq0TT3Nl8B8Q34Xn-IZzpksezu2MIS0Ow0WvCfMl9644mPlSh3tsw_W92WUMePMsM3ENGsi-h1kehKjWu9vyF8r5i50MxmPW3IuO98SbPhVXSlrobwxHiwyGlpd5an53HyV3t2l9m-QSewiauIrRE7ZlADhgHlZI2AlkNmlA9fT_l23H4tV22eTa9Ye-nC8WZJzjdssqBNJC5jurb22bceVQvo-R7NeiwXXoK83HjfGH2TRPCQXbB5XVEOdbei0_klJpo76WBN8EEnPCXTsjPEVVLAnJ_bhJYl93fid3aTCz8F1VXwVnAz6C4EUy2bwa-rUvjw3K1E20Vev57_L1Jh71ce5nUkiAHhflwxdVaEdPljAaW98XDjpr5_nM1PnsOsdyNVAC9PxJ9AK_G0e6SIw4xBWlWCv_299wj9qQt96Qb9gNiOvufOX90tFWtTCY6lE3JJu3mpQK2wLmXq1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5faa5495c9.mp4?token=O-4t6A6oPBi5QW6cD4BC1tpzdPPV3d3gonNPr1_BTrFQwyg1UeOEty6Qprd7IT2wU6JfSp5T-YMP7vheBVGfBwSdeuvUokNVqX_e9J5iga-RzwES8aKGMYkyHvFB76TRH20uf8eZA_FgCm_cz1JI_9wLDifBUV06pqHKZ-zQSUmVNaxWNw5pbf67OXXq8AkicwqpoAd003yKIPdpcFOoTpJq0TT3Nl8B8Q34Xn-IZzpksezu2MIS0Ow0WvCfMl9644mPlSh3tsw_W92WUMePMsM3ENGsi-h1kehKjWu9vyF8r5i50MxmPW3IuO98SbPhVXSlrobwxHiwyGlpd5an53HyV3t2l9m-QSewiauIrRE7ZlADhgHlZI2AlkNmlA9fT_l23H4tV22eTa9Ye-nC8WZJzjdssqBNJC5jurb22bceVQvo-R7NeiwXXoK83HjfGH2TRPCQXbB5XVEOdbei0_klJpo76WBN8EEnPCXTsjPEVVLAnJ_bhJYl93fid3aTCz8F1VXwVnAz6C4EUy2bwa-rUvjw3K1E20Vev57_L1Jh71ce5nUkiAHhflwxdVaEdPljAaW98XDjpr5_nM1PnsOsdyNVAC9PxJ9AK_G0e6SIw4xBWlWCv_299wj9qQt96Qb9gNiOvufOX90tFWtTCY6lE3JJu3mpQK2wLmXq1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به کنگو توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97421" target="_blank">📅 21:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97420">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/97420" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97419">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوممممممم انگلیسسسسسس</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97419" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97418">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هررررری کینننننن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97418" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97417">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گلگلگگلگلگل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97417" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97416">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5851711fa4.mp4?token=S6tPMqUsV1bPnxQBxUHmMHG0iD11P0U3qP7a4syYzBZSGT1hyNfqQKe7L8lMHz8VKOMPMcxL-Om5fdfFV4bXaFXJI1YjzXv9p9PRctcCZQk1tvxXiVSXjIg8XfeLJSZJhKbKvDkKOCEcnRAJFe6p-YxiWCZY9E4JflXGIaTlW9UT8jVsj1VsCcJ3wFY09FpN6b4rHrmGNwLJAFpxrvIi79BLtfJuotuG5C7GHl0JoiURcHYhsiBl1eH-uxT140iGi7zjVNIq9YFfkPNPhypKiHjzZfaIu1BrJJFeVfUW8MpqNI1S0DXOch-n25mq1Qizzj01vV8F3Eed1B7-VEDDCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5851711fa4.mp4?token=S6tPMqUsV1bPnxQBxUHmMHG0iD11P0U3qP7a4syYzBZSGT1hyNfqQKe7L8lMHz8VKOMPMcxL-Om5fdfFV4bXaFXJI1YjzXv9p9PRctcCZQk1tvxXiVSXjIg8XfeLJSZJhKbKvDkKOCEcnRAJFe6p-YxiWCZY9E4JflXGIaTlW9UT8jVsj1VsCcJ3wFY09FpN6b4rHrmGNwLJAFpxrvIi79BLtfJuotuG5C7GHl0JoiURcHYhsiBl1eH-uxT140iGi7zjVNIq9YFfkPNPhypKiHjzZfaIu1BrJJFeVfUW8MpqNI1S0DXOch-n25mq1Qizzj01vV8F3Eed1B7-VEDDCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول انگلیس به کنگو توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97416" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97415">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شاهزاده هری کیننننن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97415" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97414">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انگلیسسسسس</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97414" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97413">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97413" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97412">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYzcinkafQy2Pbxtcdnt3NbkeGAQpDJ_GCUjzIzIsDiun7GtXRie03y727Jia3zr0lOZwZi68rKOrJid3YroeFolY4YoSxjuEbZUOmjldBohtMZHcBPpD-Uk_NyUyOlq-aT-aX66LuJpj86n_TVh8vkqIMLnld8zqr5CpeEryCHT-lqmsgsW8nE7NjFVMQBhb83HcHgYlzDBK3Tw362O6bKEhPuJXxAQ227VJydknIor091SfK90WNww3MKNLX8Ed74dv__D6GkA1ayzKtS_18DSBaElbz5w9LKq2v5L2v3DPAgq_MBA8yfCOPtO3FkYrITJ0K8t8v88jIyiQmA7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇩
گل‌اول کنگو به انگلیس در دقیقه ۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97412" target="_blank">📅 21:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97411">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انگلیس فعلا نتونسته کاری بکنهه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97411" target="_blank">📅 21:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97410">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97410" target="_blank">📅 20:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97409">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMhGL_6efkf5dEju_txDJx28bXmpr8GXr1dB3ad8DL02FIgwfdIIIcLIy8R4k7yOobRZe8CL18ooY-0vYKO6S7WTvKjKf8mUon50eAn_y5kxl868R4_duMEgqhy7BqJAbCZJLyWiSPRuM3EtoPuLQ2qZrEo6BesY7BNGL3W22PZ4Aw0D9TBK_YxBBTIuFQfQkLHgimEkWbEzfN0JWgBLYcsdS5S9WrDSgFV4EYwOn_3qNNMvWpVbKYgd02qoDrSiaZqTdvO1f8ftGB0qaMOl2tsLqsQeOM4ObFnfEhzP7xGL8Fvlw-QevYE5WmZLW7lD7dgZu9BpSeJiS2evaFY-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقطه ای که گلر کنگو باهاش سیو کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97409" target="_blank">📅 20:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97408">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممم مصاحبه فیروز کریمیو:
😆
😆
😆
😆
فیروز کریمی روی آنتن زنده: قلعه نویی ۵ سانت و ۱۰ سانت را تحمل کرد، دیگه ۳۰ سانت را کجایش بگذارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97408" target="_blank">📅 20:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97407">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🏆
پایان نیمه‌اول با برتری یک‌گله کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/97407" target="_blank">📅 20:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97406">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلرررررر کنگووووو بازم گرفتتتتتت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97406" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97405">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97405" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97404">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=ElkP_vigc4qBJhdBaC7EgIZjEpyoa3VBYVEicUC4XKydIcLgMrAj5vEWqEaqm8wo_-ulLPwl4Vw1TlV5KYuOwgI67SKtTsD4TwB-9qQ2PojxYxjdhBlBzxMLQ7iWwA05jREzJtHql9Ne9N8acwnWaB1XaWxXq4x2bFeYB2js3UxJ2yD4e8pQHGzN7FIvBqT9zFiG6m5pcKoenpwc9CaJS4iAiTeZHj5QFm4Mm6rEaDsL4WhAVtdEQmBI2e10zc9S62oRMaNiCKl3ehbynyD74O2W7KbGnku0ES4t7JeuDJp2dXa72pNV7At8N22eTuVFhcuN1pyrfBE7r89mCS5i8A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=ElkP_vigc4qBJhdBaC7EgIZjEpyoa3VBYVEicUC4XKydIcLgMrAj5vEWqEaqm8wo_-ulLPwl4Vw1TlV5KYuOwgI67SKtTsD4TwB-9qQ2PojxYxjdhBlBzxMLQ7iWwA05jREzJtHql9Ne9N8acwnWaB1XaWxXq4x2bFeYB2js3UxJ2yD4e8pQHGzN7FIvBqT9zFiG6m5pcKoenpwc9CaJS4iAiTeZHj5QFm4Mm6rEaDsL4WhAVtdEQmBI2e10zc9S62oRMaNiCKl3ehbynyD74O2W7KbGnku0ES4t7JeuDJp2dXa72pNV7At8N22eTuVFhcuN1pyrfBE7r89mCS5i8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممم مصاحبه فیروز کریمیو
:
😆
😆
😆
😆
فیروز کریمی روی آنتن زنده: قلعه نویی ۵ سانت و ۱۰ سانت را تحمل کرد، دیگه ۳۰ سانت را کجایش بگذارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97404" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97403">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلرررررر کنگووووو چی گرفتتتتتتت</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97403" target="_blank">📅 20:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97402">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">چی گلگلگلگگلگلگلگل نشددددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97402" target="_blank">📅 20:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97401" target="_blank">📅 20:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97400">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رشفووووورد ریددددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97400" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97399">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq7KeNoyXb4RrT0sImzHFenrH3IoIUH1Z5rpRXpEizNEHBYVTWvxikDFO9zAI3uxGQLNf4ijSS5hRvIpeGdhlMt92ztKKpO6Xl09hkc4qsXhq7vCZsVlaX4VGJY3AogD_8t8yTco-MWxHI3cJ6HOiHCt-NpPOg5higdC0RM7vC9Pkb6YjmuDSrI1pyo_fLsQxklOlPp9u4SYx91N8DqS2-XMWv3yKDGi3gQtfFqK0h3CO4v7eKd5GglVgr76zsJbTu4-KD1n6C4zUQR1mcmG_m5pJHx9FULVFGvTj25_kksC-mq26_dd_uisRpUfdGhVHnk1SIM6VyCH_yDLYL_tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
👍
بوووووود یا نبوووووود
👎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97399" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97398">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نگرفتتتتتت</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97398" target="_blank">📅 20:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97397">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خیلی مشکوکهههههه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97397" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97396">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">داور تمارض هری‌کین گرفتتتت</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/97396" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97395">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پنالتی نشددددد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97395" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97394">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انگلیس داره گاییده میشههههه
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97394" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97393">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کنگوووووو زدد تیررررررر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97393" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97392">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پشماممممممم</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97392" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
