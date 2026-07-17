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
<img src="https://cdn4.telesco.pe/file/TsHtSeINuSNnBx8tegBWfWK5_PwlLgkeap7aLRPX0k8-f8LTVDZuiCFHffd_kK2reAGRcsRHyU-FxJ9hFyBltcin3p6gwmU3BiKRXtZ8mPFjvslGkk6T8xmDU-grweQNlHc1bJBimdntzBzMkoARG0qOCe6coBuktnPGhEQ0eyV7bR0_nAsaYlecMOCvf0tqJ0m17h4kQ31aj8vn_Zp_LJiQfxxXOWiRTmhcwhE2yIHgRpzYX9_peQ6lvJzUPz8JHY_3f06D73_OS-S3fUVdJVA_okdz6xebKEugyi-AXbl-T4c-Jv8bbdRFktpuNzPTzwodfGE6KqE3XcY1zQ2sww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 15:32:33</div>
<hr>

<div class="tg-post" id="msg-135048">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
آی‌۲۴نیوز: طی حملات دیشب آمریکا، هفت پل و ایستگاه قطار در ایران موردهدف قرار گرفتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/135048" target="_blank">📅 15:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135047">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD5LK6UvJWG-SaH8tL-f_pUd9Hkw613C5YgsPSq0KQ0Pq7CksxxNiOUhHh7T3pk4FfqJzM_xeCzk0O3BIlWp0pH44HWjWajqF18P-w0tZ7hXHuvSOoCyr3xeAiy3yNmZ8Djm3EvfD0okU1jzLvGq9xJFNILpv7f6uUMP8duEMtvCSEOYgLkmFJnKzj5dNKu_u9qZ5LfcKLWy9cEqURl60TGmel6fdfrxXwaO6tIKKoq0fdqkMoUu-AMt_coRTcf3snz9yS6iVZnlT3i7HWYQ0IZjvaTkfa0ZybzOaNOEaHmzzQlGdv-Vn1IueQISB5rqIRYxEkxyyNLGxZ0A_ig-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: باید بریم پایگاه آمریکا تو کویت رو تصرف کنیم بعد تجهیزاتشون رو به غنیمت بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/135047" target="_blank">📅 15:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135046">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUEKJ7HYAVExQ2WPcCocqMWmsRn2-csfR3XdxGtU_J0yxoyLDlSQR5rCs430tpOWpUobg4EPfPWsRGcNQF0KNclVNbwmpJGeHN38Mg_YwZRMW_b8gPq31d-hy2RxnrrdJiA7OVbXcQpN9M89-7j4BKEC9cXx1jVYTpvpfx7G6HWIL0XYMPUmYKmvaKp5FM4KZELnBsOrJnNwQjcLw9-efPTibeatRpx4NUFcOaMhYBPv5scVxpJnCZwSMdi8CvvF2VA2nyN_BiSUkGQBaVEgPBm_m5iBVkM9QNsJTGZKoVHfdaptndEC0jtrfpyRoa7b_k-NVhA-WxBtAAU9h5fR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در بندرعباس مردم قایق‌هایشان را جلوی در خانه پارک کردند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135046" target="_blank">📅 15:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135045">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">صداوسیما: ارتش آمریکا برج مراقبت ترافیک دریایی را در سواحل مکران به کلی تخریب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135045" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135044">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZd0wwJ43NPHVIAyPZRrbL4Q-iAnwHjFU9DoEeNoM4WYQrQQeyVOPWud1HEwXBT4htGQfdgY3qbmhRv6dVuGWijJ2H1hCvdqRnWXxgtRXmxxkWrQLf-2w5BnCjass68F1KFzimVu5RyozoaLNAgO8RbcH87-ZqK9T8sH6nqw0jxEEFHdfeSIrEB_fkfIK9UQIEQdyW_kBVcurPj4pLynqdoe82X3k9KspEYWcBLJLekvCNU0IVnc1RaB5UYbBEJLBYagTroyUOgMH6ZwFHb-UpAfEDCWu5qW4ksDsFMaMMmlcaoZS8duXe0WcbgxxHvehmOghHXzTgou5HrfeBLE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست‌های عجیب در پلتفرم ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/135044" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135043">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
دولت انگلیس:
از این پس هرکس در انگلیس از سپاه پاسداران حمایت یا به آن کمک کند، ممکن است با ۱۴ سال زندان روبرو شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/135043" target="_blank">📅 15:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBPlYNPyTYKdEzyhpygobV4n7oe85TzkjX7NqSIEDLywJ1eMdLnxb8oNC63fauEYQi_CILJguC9JYUB4ui21d8AA-T04vqMccxAXnC5xpA4TLtS6LCo-d_J--B-cg0vR7wAe5ElY4738_jEHrrrPR__5CKFnW9YaaVY79tHy-HSZdOUi_Yo-4c5Hzhayylzw2tflYzPxUVd7293p2UpiaERg7Pjx852NAcBRB2iP_eJayioLjO66YGj4nyVxHvfJ2sF273XS-VwNbZsIDulaXI0-T-2yRlDKNmybJ_YkO75OGM10hWPqyfXeaWNGjKsJifQHJ5ET5DpwC2y0aPF9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی عجیب در تجمعک‌های شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/135042" target="_blank">📅 14:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135041">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9aa080b85.mp4?token=MB8bEogJ3lYMCdj7kyXzf3wpBL0uVyuAf-sPB4zdI01XcQFn1-mbLWiJB5WqqmITjjMxE4pqB272fmKlMRMlYM0wbiZfdYL2MhMmWQis8ZwaNody4OJIU8Ib7DVHb8hsxLVLhtLYiIQNDt3ZEO88il0kBNPx-hQqD4KLH2TW50yCO6hBZ-9MwvLa3kPNwM7P2vsd5ZjBXNe5zR9FP1UFNHm0wPXh5_E1P92cAZkdfX82qVDAwbzNuxmIboKUms7WVClSEMhCwMqx0FUoHLE46lriIx_pYlnaS4vsQTPGPkNZrUBccCc83WmVjV-ufnbG6hPBuUBOnd3uqww-NHm8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9aa080b85.mp4?token=MB8bEogJ3lYMCdj7kyXzf3wpBL0uVyuAf-sPB4zdI01XcQFn1-mbLWiJB5WqqmITjjMxE4pqB272fmKlMRMlYM0wbiZfdYL2MhMmWQis8ZwaNody4OJIU8Ib7DVHb8hsxLVLhtLYiIQNDt3ZEO88il0kBNPx-hQqD4KLH2TW50yCO6hBZ-9MwvLa3kPNwM7P2vsd5ZjBXNe5zR9FP1UFNHm0wPXh5_E1P92cAZkdfX82qVDAwbzNuxmIboKUms7WVClSEMhCwMqx0FUoHLE46lriIx_pYlnaS4vsQTPGPkNZrUBccCc83WmVjV-ufnbG6hPBuUBOnd3uqww-NHm8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار تو تجمعات شبانه : جنوب لبنان و جنوب ایران اسوه ( الگو ) رزم همه‌ی دلیران
🔴
عملا دارن افتخار میکنن که ایران رو به غزه و لبنان تبدیل کردن!!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135041" target="_blank">📅 14:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135040">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZqb2jIEB61EpPdnjkmbsSV-Wl7_vGgLVjLL1gbKSX-Xd7MLEvP6pUqvBt0tQt6Gsr0JFB-G-aGexgfVllMCIJ1MGY9pXC4w3Z2_CdJyvcQFHamYyjcr3VdiG6r89vIKJ-ke_Fual-s5nI-0I6KGKbiGNJlJ1rpGuT2Z6-MH5lnqCxcW51o1arNcbwjhaKBrFlsH5TAkx_niW5VD8L9y5QASgMWOYLFVozc3Iv864G27xsNVF3ntAWMVi8J8AZo1-b07J10mUEHuTsYoQgg9s90K9RKszYemtcCMNOgTXIFj_998ZeTL2mrvrkTj_d6uuwGK59uwlSCxfhIYEi1UJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپ جام جهانی رسید نیویورک
@AloSport</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135040" target="_blank">📅 14:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135039">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkn5flYtEE8Smy4Ay5gLAm6CXzcDuh4wjILUHlXIeLBg-1uUGW2Tx7WW_AothoH5H8-d-cX5Spy3wR5vIuFbijwH_4zrb4GhtEU29NjE9zYksJjuviuQ6y43FaQKxGNmP5zR61Lh53N3XMOVm55cl7PIGy9Mnyftf2x77UKnszmbcSn5v6bsaAT7xMgsaOzXxll2rU6GhsrZKjZsygOatEbmqfjrooP8TizHPxkOZNVCxwYyfjn9qMp71rVugAlj0kdTK6aohIun9aWUv-Lr2MNZqR-M1_NqTR-sgBuUdxCf2OjUonL7lLKFzxW_afxDDK3mP19yjuR_c9rwYSKH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی از یک حادثه شامل یک کشتی تجاری و نیروهای نظامی در فاصله تقریبی ۱۰۰ مایل دریایی شرق دوقم، عمان، دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/135039" target="_blank">📅 14:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135038">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=Hztwv2p6-O4Je_EwTzpg6jhjiDNN8n5Qk_iDL04vqiYT44cEwslZvNkxLJSTFzT9VpgZHHauOOkWmiGwamP17v18eHzXAr-5q7H9G3kLPEB5Qj0erQYG-VFQxfthoCeqwlyivWpoSZT20elRcFsFdNB7b_-VwroOsfYeDGG7FxqwZj6q_Tijk7zrb4t2NiugazIIzolpbxtQ0yUmuipIvCMhH1Y9t6170dZOLPq3hIB2ZTznxjEmPYO4KiSImKX82OLcZKr7oil4dsaGXnzvnrhcrzOt6VwzQ5qJWfFMvXsItoeUgo4Ac3ifP4_B8gOUsWOTsjUVkFRD8h7a1iQ8JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=Hztwv2p6-O4Je_EwTzpg6jhjiDNN8n5Qk_iDL04vqiYT44cEwslZvNkxLJSTFzT9VpgZHHauOOkWmiGwamP17v18eHzXAr-5q7H9G3kLPEB5Qj0erQYG-VFQxfthoCeqwlyivWpoSZT20elRcFsFdNB7b_-VwroOsfYeDGG7FxqwZj6q_Tijk7zrb4t2NiugazIIzolpbxtQ0yUmuipIvCMhH1Y9t6170dZOLPq3hIB2ZTznxjEmPYO4KiSImKX82OLcZKr7oil4dsaGXnzvnrhcrzOt6VwzQ5qJWfFMvXsItoeUgo4Ac3ifP4_B8gOUsWOTsjUVkFRD8h7a1iQ8JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی جدید از پل کهورستان شهرستان خمیر که طی حملات دیشب منهدم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135038" target="_blank">📅 14:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135037">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/135037" target="_blank">📅 14:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135035">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=f2E0GB_gS18AbZoLy_IBDtFcG_pfSavo6qUIqhdkuiCYHRz5q9BwAUpceGTMtjFzWdGiv348uDOd1w9aOYwnG3zmIs6TFUuF0tfwtYQO521Tl5_GvbfMx4tw8i6LE6joNyVjdwzopl8Oud9bsvRR_fSSAW1u7WpaeSSO5Xfc_4ce507VJnAYtWdCGeg89WAcT22O_g8mZpU3lMFzoFfbz2vTgRdvodbS8UGIAfB834YoHfYaI0B1Q8UT6FxmCPpH2w0ltC58EOLsRe9w16bOcEAkUzshFk2XmRGmb0I-LWUivturCh6ukJAks-w2JuC5RM7uXJ61Fh0v3GBYpw1QUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=f2E0GB_gS18AbZoLy_IBDtFcG_pfSavo6qUIqhdkuiCYHRz5q9BwAUpceGTMtjFzWdGiv348uDOd1w9aOYwnG3zmIs6TFUuF0tfwtYQO521Tl5_GvbfMx4tw8i6LE6joNyVjdwzopl8Oud9bsvRR_fSSAW1u7WpaeSSO5Xfc_4ce507VJnAYtWdCGeg89WAcT22O_g8mZpU3lMFzoFfbz2vTgRdvodbS8UGIAfB834YoHfYaI0B1Q8UT6FxmCPpH2w0ltC58EOLsRe9w16bOcEAkUzshFk2XmRGmb0I-LWUivturCh6ukJAks-w2JuC5RM7uXJ61Fh0v3GBYpw1QUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی، تحلیلگر اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن
🔴
الان هم اگه سپاه تو تنگه هرمز حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور مارو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/135035" target="_blank">📅 14:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135034">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvwRkM-rawA0cJG59hLMFveyE9ftclITBpbWib4flgd_aGXq3jmwyXB3HmymOzCagWliAhokFTbQs2plmitZVpuQ4VxgcgS9xGoLYaiZHcd3kTkQQabUpXz9M9CsQeGW0TkgZJKgntM-QAAT6hHpqucF2lI-KLIUaHhJF4WJJiVWZp_7wjYepEzBd548pPUcS9sy8reqXISH_469Cjs6mNNj8hQOfJX-WhZrza1e2_fKxcssQ9r1gYPlgpwHgy8-KtZtxvbUuu-NaBEIEfVMdzjS6tLnXMQzJg10ZKFHCdsv-c-gAY0__1MuNo7yjDG4C_HsRXMCN5wGJZNRavYC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل هم در حال تخریب شدید زیرساخت‌های حزب‌الله تو جنوب لبنانه. (زوطر شرقی - غربی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/135034" target="_blank">📅 14:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135033">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/135033" target="_blank">📅 14:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135032">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lja31KU_fr_egVxKyeuhwGOp0RjPPAv4hEsM2l97301tLQ9_A22n-MhDymTOLMJKbbtVNFrNg7T-2fJPyeX03ZKbZHkGUqYCytXC_RrcfWP1QvSpiumHtFS9ZhmMdfSjbAcge-NQGZ-rxyYQ0RMP-MsYZ7SkeTJWhlyexXI65JEuVgP9Pfzfix49z_OeruaLhyXGN-6uJyTumCK-i-_vnuRN0sL83ieeQGUwph9EClZjVN5EvFiOaU23fX5H41ES6u9f4amWLYUNI3LNQDves0wuFA0OkoAMM9gbHKyG00NrnfOakywfySE5k6qaQN9w-lxT8rFcAqU1RKVQav-3ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+اونجا رو می‌بینی آقای رنگو؟
اونا می‌خواستن برن فلسطین رو آزاد کنن، اما حالا از ترس حمله آمریکا حتی وجودشو ندارن برن جنوب کشور خودشون
اونا خیلی حرام زاده ان آقای رنگو.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/135032" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135031">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f391b5f3bb.mp4?token=FsVgheO6YRcUhtAYQw-SiHwUiC86ZqIM1M6i0cBi5xdk6msojzJ3XofNqIGu_LF-pmUJF70R3W1tHc6MYtaDMzSTgvis4BNXnP5qzQZfBQCJw5hSN6n-peSfSX8aALW0qDYMZkqr1UBLI6xF5F8cCtAtqs13YsDe2R1oJeoq1xoy1QFTcqdPzXbQtHHCGTP93fMepajqT2NJzQ_g2wxQPXoB3IJQfGMGg7_lUCHxGMeiL1kKKYCCo6YJWF5FZUyzNCjbOjvdxm5rb8kXj9awqEapNLJLUjA3naoQdglrmcjJ9eJDQYxuiXUkHegc7cYrAzBePIJGNEWAqxq3aWkA1TkCl8DC6wukl9HrXQ6EV-LIqZb1OGXFJz0IYzUoUXUCRTFLK3qUqLdZfbYb7CklexehRs3sRGicNn4fgBrnaois3RHaeVYSYgPo3Ql0MzGkSPKe_aWl0iYVftLOsWkGT-ZlnukFMPbPuMMuin6UcFvrpqQPun_6jzj_1XnDJqnEH9ch7L0YQsXTdsPfEJh43eHCtYfY4ER7MjUz-uh7Bji1ppSY3tVqAeOQKyFn7AojUhwkoH5OIdmZDlGBub6Uj1S1tQZR8H1WFG55LIluUuDSJ8tAIougsD_Qa1yr5ExZVfx4tqBOoqquPnkNgo1yhKDVOQOBB4maZBQUmIDV5Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f391b5f3bb.mp4?token=FsVgheO6YRcUhtAYQw-SiHwUiC86ZqIM1M6i0cBi5xdk6msojzJ3XofNqIGu_LF-pmUJF70R3W1tHc6MYtaDMzSTgvis4BNXnP5qzQZfBQCJw5hSN6n-peSfSX8aALW0qDYMZkqr1UBLI6xF5F8cCtAtqs13YsDe2R1oJeoq1xoy1QFTcqdPzXbQtHHCGTP93fMepajqT2NJzQ_g2wxQPXoB3IJQfGMGg7_lUCHxGMeiL1kKKYCCo6YJWF5FZUyzNCjbOjvdxm5rb8kXj9awqEapNLJLUjA3naoQdglrmcjJ9eJDQYxuiXUkHegc7cYrAzBePIJGNEWAqxq3aWkA1TkCl8DC6wukl9HrXQ6EV-LIqZb1OGXFJz0IYzUoUXUCRTFLK3qUqLdZfbYb7CklexehRs3sRGicNn4fgBrnaois3RHaeVYSYgPo3Ql0MzGkSPKe_aWl0iYVftLOsWkGT-ZlnukFMPbPuMMuin6UcFvrpqQPun_6jzj_1XnDJqnEH9ch7L0YQsXTdsPfEJh43eHCtYfY4ER7MjUz-uh7Bji1ppSY3tVqAeOQKyFn7AojUhwkoH5OIdmZDlGBub6Uj1S1tQZR8H1WFG55LIluUuDSJ8tAIougsD_Qa1yr5ExZVfx4tqBOoqquPnkNgo1yhKDVOQOBB4maZBQUmIDV5Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آخرین وضعیت پل‌ها و مسیرهای مواصلاتی هرمزگان پس از حملات آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/135031" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135030">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
هم اکنون یک اسکادران بزرگ از جنگنده‌های F-16 آمریکایی با استفاده از چهار هواپیمای تانکر سوخت، در حال حرکت به سمت خاورمیانه می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135030" target="_blank">📅 14:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135029">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فرماندار ایرانشهر: در حال حاضر، عملیات بازسازی خرابی‌های ناشی از حملات آمریکا در حال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/135029" target="_blank">📅 14:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135028">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF-0gTEUbr5b5K1_EMsN3AsO8g0ABN-4JKTTCNUpwe0YJO9gv8E03RkvyLYY-GIBJ8v2K5fNnmMtg12WK1JeuuyM5VnWmL1sqlyPqNgcgHbAy8xrLWHZywW3MZYV209DtJ0WbeSVY4ql4Sb_O8A9MlFfwgaCLO-qhrHpYGnUakNKRPStHM6p_d3O1q6PT1BiP1rB4mbKkuKIUhhNa1mXNN8w9YYPYXzfneWDpUQTB62D_aRaM7sCdkp86ChZJzjvppoT_cr6QAf4F8amnLgvw3gl01QLVoY2MN191up6yvstPK9g5NmJNm6zmQ41uOTJFTli-1lVA0KOAci9YFfxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت کامنت‌های پویش جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135028" target="_blank">📅 14:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135027">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سایت داده‌های کشتیرانی کپلر:
ترافیک کشتی‌ها از تنگه هرمز دیروز به تنها ۸ کشتی کاهش یافت که پایین‌ترین میزان در ۳ هفته اخیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/135027" target="_blank">📅 14:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135026">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHYREC3ytBPPtBFyrLaeipdy_LGutk-5N12asJOJe0Ms6nbuHiJdiiiBjONaFer8rezvUEMvwd7EzaIGC3Ugpc2juQMU4-6YjC0Y_cLWaRLgTM6kAk4-SLqpJN_ziBj6TuqDdj2rJi3JCHNWReaMuj1tl-ucDxpQfCrQ1GHKkobDATFyKnZkvvgKFC1Ia7H5VOvmc1GmqIECjE5A8V-ALMMh5IXaEzzHX6G-XoBcYdt3xBl-0oWSI8Y3TGoxvzsyiau4TZ6YTDLYCCKjWUFCfZwXe3mwBNKqoolY5ycQe-6ktlTd1ASQku8bOQ-FQuWjjpiqLhObtYsTK_a1RuC50w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135026" target="_blank">📅 14:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135025">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ce491105e.mp4?token=O2rTjnUtwqCajwfa28OrKfBMZTEwvlADKe0yysypV9Crh1JGM8xvid47yhi_aKTQ2XLz7rWRgEy0Ph9AwmC75vkmbDovwQC65ZZLYbmKZ1YmrIZa7kkq0Fj5XG-XNcTCTYiy_AiAVwCayVLpCEbeP6Lo3KhBYMdz5ut8ut36YIQG9kZFUcDBHHAc1jS3tuwErgvbkRfUxF81X9wonybbPCq3jXJGAs9OUANG4GZcDYpD5pjaKmbTfIyxT2h9WNeMUTT1emAEKRMebsSHQlBMed7Oba4ZfR8Sw6Yyc1Swrr0TMLAuyj622wzgTwv-0V3YcBjLDrfWXKdtknGq4y9OMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ce491105e.mp4?token=O2rTjnUtwqCajwfa28OrKfBMZTEwvlADKe0yysypV9Crh1JGM8xvid47yhi_aKTQ2XLz7rWRgEy0Ph9AwmC75vkmbDovwQC65ZZLYbmKZ1YmrIZa7kkq0Fj5XG-XNcTCTYiy_AiAVwCayVLpCEbeP6Lo3KhBYMdz5ut8ut36YIQG9kZFUcDBHHAc1jS3tuwErgvbkRfUxF81X9wonybbPCq3jXJGAs9OUANG4GZcDYpD5pjaKmbTfIyxT2h9WNeMUTT1emAEKRMebsSHQlBMed7Oba4ZfR8Sw6Yyc1Swrr0TMLAuyj622wzgTwv-0V3YcBjLDrfWXKdtknGq4y9OMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدخشان از دست طالبان لغزید
🔴
گروه تازه‌ تاسیس مخالف طالبان موسوم به سپاهیان میهن صبح امروز موفق شد برای مدت کوتاهی کنترل شهرستان یفتل در استان بدخشان افغانستان را از دست طالبان خارج کند
🔴
این گروه همچنین مدعی شده پیش از آغاز ضدحمله طالبان، بخشی از تجهیزات نظامی مستقر در منطقه را به غنیمت گرفته است
🔴
اگرچه طالبان در ادامه با اجرای عملیات متقابل، کنترل منطقه را دوباره به دست آورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135025" target="_blank">📅 14:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135023">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9pBK0O-nr2F8dwqlVl78DEdf9QStVD_I_rjf5mX3wn9NgWU9QjoeMdI1HC3FgJv2Kg8O1ZZ1SJFq5biV6MHbRbLH1C9MZ6jtGMUIal6rdpDZB0ET-rR2jWSYyY4q3sODLKhnUJYeEPEDWpKmSIVFqZMZJQvNlh4687UKCNXLryn2_W_H8tGMHHj8WiulP-r6bVRwnpTv-mzneujqW6LP3fYZwsCE4_7FavjzkAjSS_DoFvmcH2WPK5NzcmWeq3kvqhH7CS3Ti8gWX3fcyFIH1an4PS5wT90QcsHStl5ZVbZ1eYydKTzq4WI7l_LuMetfjNCr3Xo221JOmJbjSqkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر دوباره همه را غافلگیر کرد؛ بازار در تب‌وتاب افزایش قیمت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135023" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135022">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRsrTGfQVNTLhI4zCrv8QkaN6PqcN8oa-1G_dJ0bTKRXKnIfsd1fzlyJVk64BEHJJwq2V2llLqbxnsBZBG-AVh10K-3qlYvAreHuQrxBRzlavqBKwUgz2BIA8uhh-PqNtttGlLWHxjRrwnpHXvyViKLaidtBFfTrREPsDkjaS1ewpM5PwmkLsdhOSS54J5nj2E8Zu_kPbEp704LFCBRlqGU4IeD7otmN3tJVx7aHymALAQIQm2El3aHd_dFYEpbll_mzeOceie04beWrwDK-ok4JkWtlAe6F-BJiQP0jjg6VHQmsJKcab84FPGSsDB_pnk_beUgY42-rqHWmajG7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱۰ فروند ترابری نظامی C-17A به خاورمیانه اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135022" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135021">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
توانیر: همه روزی ۱ ساعت کولرو خاموش کنن تا به جنوب کمک بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135021" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135020">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی آمریکا علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/135020" target="_blank">📅 13:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135019">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سفارت آمریکا در عراق سطح هشدار سفر به این کشور را به بالاترین درجه افزایش داد و از شهروندان آمریکایی خواست به عراق سفر نکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/135019" target="_blank">📅 13:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135018">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ در سخنرانی دیشب خود که در ساعات پربیننده انجام شد، به‌ندرت به درگیری با ایران اشاره کرد
🔴
رئیس‌جمهور دونالد ترامپ در شرایط جنگی به دنبال یک سخنرانی نادر در ساعات پربیننده بود تا مستقیماً با مردم آمریکا سخن بگوید، اما او از این فرصت استفاده نکرد تا به‌وضوح چشم‌انداز خود را برای مسیر پیش‌روی درگیری با ایران - که در روزهای اخیر تشدید شده - ترسیم کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/135018" target="_blank">📅 13:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135017">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
دلار هم اکنون 188,250
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135017" target="_blank">📅 13:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135016">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFfjEPBx4jbrTSnn6ES6ptA7D_qfM_sgzh2Uvlx2VvTy_tQJqiPcFzqqJ44yUmy10nDiBZrBw-Td4LOoNI1SfNGYyTTiqlJcLRj-_lyWAosDW_eBgpkFKyrTIf_09wYH6sgZOhiMy01Z_ylIwf_IDUu6I90XJoyyzB3C_NaSQft680s_ojsPVH9pJSbfSvf1MVt4LXPv-yoYAdlkyEFjo6TCx09rcyKNFcepGhAPkEe-AKgqCCzSoGu3KXXYvH92tcXWC2kXsnaWVnusf5jfU9q1iIBvesjORtafxbUAP9rPDgWYN2abIFCFmt0Pjm2fArqip5jxBmQ5EAwk3uQLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در همین حال، ارتش اسرائیل به تضعیف زیرساخت‌های حزب‌الله ادامه می‌دهد و گزارش‌ها حاکی از تخریب گسترده در شهر زوطر الشرقیه در جنوب لبنان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135016" target="_blank">📅 13:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135015">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد.
🔴
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135015" target="_blank">📅 13:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135014">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع امنیتی دریایی گزارش داد: افراد مسلح به نفتکش حامل محصولات شیمیایی «آسانا» در خلیج عدن در سواحل یمن حمله کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/135014" target="_blank">📅 13:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135013">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل : موج بعدی حملات آمریکا قراره خیلی شدیدتر باشه و‌ احتمالا تهران و بقیه شهر هارو هم بزنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135013" target="_blank">📅 12:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کویت: یکی از نیروگاه‌های تولید برق و آب‌شیرین‌کن مورد حمله قرار گرفت که به تأسیسات آن خسارت وارد شد.
🔴
در پی حملهٔ به یکی از نیروگاه‌ها، تعداد زیادی از واحدهای تولید برق آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/135012" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
آمریکا: حملات ایران به کشورهای حوزه خلیج فارس هیچ تاثیر عملیاتی بر نیروهای آمریکایی نداشته است
🔴
سخنگوی سرفرماندهی مرکزی ایالات متحده، سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/135011" target="_blank">📅 12:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135010">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b9f44987.mp4?token=PHxaWnj5EgXQPArpuxVh4xIFWz3oRu_sAnfT40Q1Pc2sdzAKOUwDZdew1iUym-mOHkdGyc2yT9kX0JI71ySWPZobAt3_E7eRn4UzBWiK922C6I0JJwXkTvnRkNXub2He-odbe40-tAWWRTjIr_-6eqEEHuMQBFr0BM7oHB6enL-vF0NCODUCcJiKVGIBqfXOAorZTliPFJTtyRON_ePDexwGf-X5sHR7OQ9GTchU1o9MtGFNIbwGk773_AXHMYkUvVQvHgjg768BJr4vW8ecUiN_gV80VgZW8wVKR1Zm86T2purSbfBndvYWnrsaU4Xc0t9kSTMB1H_GrwtNI1EErR5_5M_kpf47en-IpHs4OhEvqyr9kWQKnQWrVkwx9_Vrsqna9pHlEpxP9sBljaOtc1gs_SYjedXNDG_tkFfoViFeemwtMZYAaFfGnPAJ22o7oa_fY1IkRdbNOdfOR3VEvcSf5EG9eTz6mOpZK_S-l0g-OS80dxepBVQuX-ygjYxpvmFjbYUBBgfWvMiUEUWXOJ1AnQXgmsOUeKD7fdySL86oO2TAwWmSqScUvyQtyIWvvsbXiNapNEcdJx2UXLADQOJuAdpyzDGSPeUkgL2pVlJHKK3T0SRvQnVFOgI3pi64lfs_qHEl6pxVA4Gl4Geh7agXgThtiDuecIDET9JFVxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b9f44987.mp4?token=PHxaWnj5EgXQPArpuxVh4xIFWz3oRu_sAnfT40Q1Pc2sdzAKOUwDZdew1iUym-mOHkdGyc2yT9kX0JI71ySWPZobAt3_E7eRn4UzBWiK922C6I0JJwXkTvnRkNXub2He-odbe40-tAWWRTjIr_-6eqEEHuMQBFr0BM7oHB6enL-vF0NCODUCcJiKVGIBqfXOAorZTliPFJTtyRON_ePDexwGf-X5sHR7OQ9GTchU1o9MtGFNIbwGk773_AXHMYkUvVQvHgjg768BJr4vW8ecUiN_gV80VgZW8wVKR1Zm86T2purSbfBndvYWnrsaU4Xc0t9kSTMB1H_GrwtNI1EErR5_5M_kpf47en-IpHs4OhEvqyr9kWQKnQWrVkwx9_Vrsqna9pHlEpxP9sBljaOtc1gs_SYjedXNDG_tkFfoViFeemwtMZYAaFfGnPAJ22o7oa_fY1IkRdbNOdfOR3VEvcSf5EG9eTz6mOpZK_S-l0g-OS80dxepBVQuX-ygjYxpvmFjbYUBBgfWvMiUEUWXOJ1AnQXgmsOUeKD7fdySL86oO2TAwWmSqScUvyQtyIWvvsbXiNapNEcdJx2UXLADQOJuAdpyzDGSPeUkgL2pVlJHKK3T0SRvQnVFOgI3pi64lfs_qHEl6pxVA4Gl4Geh7agXgThtiDuecIDET9JFVxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لغو پرتاب استارشیپ؛ نقص فنی موتورها پرتاب اسپیس ایکس را متوقف کرد
🔴
شرکت اسپیس ایکس دومین پرتاب آزمایشی راکت ارتقایافته استارشیپ V3 را به دلیل روشن‌نشدن چهار موتور رپتور در فرایند احتراق به‌طور ناگهانی متوقف کرد. ایلان ماسک اعلام کرده است که سیستم خودکار لغو پرتاب به‌موقع عمل کرده و تیم فنی باید دو موتور را تعویض کند. پرتاب بعدی این موشک غول‌پیکر زودتر از هفته آینده انجام نخواهد شد.
🔴
این حادثه درست در زمانی رخ داد که اسپیس ایکس پس از بزرگ‌ترین عرضه اولیه تاریخ، فشار زیادی را در بازار بورس تحمل می‌کند. به دنبال این لغو پرتاب، ارزش سهام شرکت بیش از ۴ درصد افت کرد و به زیر قیمت عرضه اولیه (۱۳۵ دلار) رسید. این مأموریت قرار بود ماهواره‌های نسل جدید استارلینک را برای راه‌اندازی پروژه دیتاسنترهای مداری به فضا ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/135010" target="_blank">📅 12:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135009">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otUNFHIq-Czsj7HRzFllij3-Uuwq_A5Uh-BUKu_hBT6JbH-OwEJZ1yPikFnI4inuE_LXUZ-n7rTf8dzAAO2EMPwjH_y8Dt5UjHZ3JOS36eWjHeyKusjf5glV_jZ-5jPqJbhuPon43DHE2UnJ2iiAQj2uS5lRr_txQ8umi-rO4yaaOYA8GQ_sbEoHs5owi7b7ff5f21G2WhSCluKVs8wtBspJmrz0OXXujPv1ihLTB67iZW7y68D4hgjWoEKW4OulaUNzx0YHegJWRRpoVrhambaS-Gy4Jw4IXDSr_B8KUrg1Zn3KlOBPTdRUwvnMzAgXKuEQZvA5vAhP-OI7oxMA9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا اعلام کرد برای اولین بار در جام جهانی، علاوه بر جام؛ انگشتر قهرمانی هم به تیم قهرمان
تعلق میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/135009" target="_blank">📅 12:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135008">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / ترامپ: هفته آینده خاورمیانه تغییر خواهد کرد و همه باید برای آن آماده باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/135008" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135005">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N11mXOvQQGXXOgvoqqmybRqUKOr6G1_0aeCgPM7Bxwdw7ufgOicUkYOiz24gQaVZjCHYlod7WtUBF1Pq0rlfS7S-9kXRND57eFIWRvNNen8boZFrQgsfQXRa5Q0Q9OQB4tTeh7io-Jr88nH5fzGqtXK8ueyPFreSjAyLZ0twQXumoLB9WFSJdJqOOUSWGnDkmy4ASSzRQrWaE_Lt4B414lD7ub1aNk1Jh-OvaFPQ5oMoKbZspFokECBC1EXEXi1-tdsyR49MAyFbdlQa2BklMhQtYp8oQGJCBWoO9z4zM7_n3oKEvjj2NafLpu0Yu6ZfDTE4wstNx737QhW5rtm02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دست کم ده ترابری از پایگاه‌های آمریکا در آلمان، یک پرواز اطلاعاتی از خاک ایتالیا و یک سوخت‌رسان و یک ترابری از آمریکا به سمت خاورمیانه در حال حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/135005" target="_blank">📅 11:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135004">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/135004" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135001">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۲ درصد کاهش، به ۳۹۸۸ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/135001" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135000">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFTsyCF-4RjihZFp5G5ox4iJvq6lCZpGjtclfuEdHP2SjFZ1012QsofxjxRjEMajeBehXTGFygnOc8mnUGdUsWIcQogWdUSg_U03mbDIVeKB0fKlykQphWyf4U1ax6GsGf_QQCjaBQDu9F6KYr5_8o7KxBixIawvBIdmAyj0iucauFSuDimgnCB089BGoOVdqpf0vinYMbQdbOlfe9zSTH8OTmHIDJG5jCk0pgZVsUDXO6blaNEghnivf6KPS9AZI12xWwUsTSxtDn83Ub9I0iM1A5DVZwDqWEmKecQ6WKdVI3fQgwd2wKu1-wNCcCebrXZO-3s29pLEne5zLAlLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا صدور گواهی امنیتی SSL را برای خبرگزاری فارس مسدود کرد که این موضوع باعث میشه اخبار این خبرگزاری به مرور از گوگل پاک شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135000" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134999">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سپاه: چندین جنگنده و سوخت‌رسان آمریکا را با حملات خود منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/134999" target="_blank">📅 11:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134997">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ec9980c.mp4?token=CgCbj37yBSYhsgzGvatqWGRU9UDXNDC6GUHgqCGTNan61PGp9Bn40m1F0NcTHPRBuqVPNuXVj9MUNOph-9r8MNimECQ-271zWh0UKtSmRyFVovLo41HJULzt1R-HRyDdDiMw3WimZtXLhROyXJaK_slP8WO93LZMFcG7838fG1A3r1uuyU-YqLKGDe1jV3Y7ccH9tdC0T0utJrSjNsuDvrmKNBpiBS4BCbkNepdFSipe6RLshflkhOBq2m4aZQ1oXrdku6UMhCvVUxrnPkw0fOrXS9YETv8TCntcgjDjmz9G7zTnwk_IrhUFlnGYDTjpfBSLUxJv1QSSjZ5q4TtR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : شبکه‌های تلویزیونی که این سخنرانی من را پخش نمی‌کنند، باید مجوزهایشان باطل شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134997" target="_blank">📅 11:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رئیس پلیس راه مازندران: جاده هراز به صورت موقت برای اجرای چند عملیات عمرانی ‌۲۹ و ۳۰ تیرماه جاری مسدود می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134996" target="_blank">📅 11:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134995">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وال استریت ژورنال: اختلاف میان محافل تصمیم‌گیرنده در ایران گسترش یافت
🔴
‏ گروهی به دنبال تشدید تقابل با آمریکا و کنترل تنگه هرمز هستند و گروهی با در نظر گرفتن محاصره دریایی و تشدید جنگ نگران وخامت اقتصادی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/134995" target="_blank">📅 11:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134994">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اسرائیل در مورد نقشه ترور به ترامپ چه گفته بود؟
🔴
اکسیوس نوشت: در جریان سفر ترامپ به آنکارا، تل‌آویو به واشنگتن هشدار داد که یک مقام ایرانی درباره تلاش برای ترور رئیس‌جمهور آمریکا در زمانی که او در ترکیه حضور داشت، صحبت کرده است.
🔴
این اطلاعات باعث افزایش تدابیر امنیتی شد. از جمله این اقدامات، جابه‌جایی ترامپ را یک هواپیمای قدیمی‌تر «ایرفورس وان» (هواپیمای ریاست‌جمهوری آمریکا) بود.
🔴
با این حال، مقام‌های آمریکایی گفتند این اطلاعات بر اساس یک منبع واحد و تاییدنشده بوده و جنبه برنامه عملیاتی واقعی نداشته است.
🔴
بر اساس اطلاعات اسرائیل یک مقام ایرانی در گفت‌وگو با همکارانش گفته‌بود که ایران باید تلاش کند رئیس‌جمهور آمریکا را زمانی که در آنکارا حضور دارد، ترور کند.
🔴
نیروهای امنیتی ترکیه نیز این ادعا را بررسی و اعلام کردند هیچ طرح مشخصی برای ترور ترامپ در آنکارا پیدا نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134994" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134993">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
نظامیان اسرائیلی با ورود به روستاهای «معریه» و «عابدین» در درعا، مسیرهای مسدود را بازگشایی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134993" target="_blank">📅 10:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134992">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: چین به اطلاعات ۲۲۰ میلیون پرونده رأی‌دهندگان آمریکایی دست پیدا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/134992" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134991">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن جانشان را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134991" target="_blank">📅 10:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134990">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
جنگنده‌های آمریکایی صبح امروز، برای سومین بار برج مراقبت دریایی چابهار را با سه موشک هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134990" target="_blank">📅 10:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134989">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/134989" target="_blank">📅 10:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134988">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
آکسیوس: مقامات کاخ سفید از گزارش‌های اسرائیل مبنی بر اینکه ترامپ قرار است روز دوشنبه با نتانیاهو دیدار کند، متعجب شدند، زیرا در واقع هیچ جلسه‌ای برنامه‌ریزی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/134988" target="_blank">📅 10:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134987">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75dbcaec2b.mp4?token=Przbx_mG6VkZlWvEzCp9XCgMXme7XzWFYwaTjhcWwHkevJycxwLlXG3iP2kLR_tsWwD8_10LJkroa-r1Z-MzMN-iq0FsWFnL7Z_34m_FGQs5-XyS9xa4vnE10q_PpCLZlsaD5Ap56oKzJ6Xl1rbAKbZfUcXCL8aj9z9T6ORC5dkyH_AK5XMn0xMxyoNGrnKsdetOd5eLJY2FE-R14UpQzrZ9eb9aPwN1E0fcrziNiPY1rADEE-KOHA8yUkwdnIEcTT_JblC0kRWE7k3XIhzaSIH-3j_X5Gaf4EyLMRzZzDCwvV4Ui1QPgFqjxN6R9u7_uhIVrGv_ja4-jPzZ_eQdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75dbcaec2b.mp4?token=Przbx_mG6VkZlWvEzCp9XCgMXme7XzWFYwaTjhcWwHkevJycxwLlXG3iP2kLR_tsWwD8_10LJkroa-r1Z-MzMN-iq0FsWFnL7Z_34m_FGQs5-XyS9xa4vnE10q_PpCLZlsaD5Ap56oKzJ6Xl1rbAKbZfUcXCL8aj9z9T6ORC5dkyH_AK5XMn0xMxyoNGrnKsdetOd5eLJY2FE-R14UpQzrZ9eb9aPwN1E0fcrziNiPY1rADEE-KOHA8yUkwdnIEcTT_JblC0kRWE7k3XIhzaSIH-3j_X5Gaf4EyLMRzZzDCwvV4Ui1QPgFqjxN6R9u7_uhIVrGv_ja4-jPzZ_eQdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهگیری یک موشک بالستیک توسط پدافند قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/134987" target="_blank">📅 10:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134986">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAMpExEY4Kg7hG3PMwOI1LXOC4aXuo7D3DcpsqhAxkh419O1vDujqUDtt-DShIcM91DPw_w3WJAbMbGCzf9PFJT9nra6g2zACohj93gdlfXsmorTG3u2P9nu-AsSK6sGxI1Y8uukEFwWhZ7UZnriKqB2SNFkkSIY8LGV7_zUfavIVoMY12Qx79oAQVHHgLYglieGrQ4sJu4S4DZ_f8J8ghKewkb6_SmWuiN-y75DjuD48chtrlLmmmS2-JzvkS2LoXHx-qc1uS2VFblsZxgeyatKKxQF61d3HtuKn9g5g1EqxHTrLA68OpmXJWxmPJtCNwimxRgFKcNE_a0BkFnDVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش رئیس کمیسیون امنیت ملی مجلس به حملات به جنوب کشور:روزگارتان را سیاه می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134986" target="_blank">📅 10:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134985">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY12AjdKxrqXbpWM-qKC_tJooi0Glepan7Gje6JvDk5bL6PC5SuVxdPo65Oe2Z59Jfxqg0_RO-anq-4UH9aRbLwSVgJq2GWQmmwmzfB6w0J_nOzAfsoiN2BwusVJ3xtXzGJKS8e8NoF34jeRTIcV4dHqH9MNTFGxbLlispZKEKlFPNu3KJen6ni4RtHIEqmMIR1sgcy-1-o-XhGr2znO4CoJnpL9oaMFQx_q1pHdeg_TvREOeUHq_eR0J7yYsvteUEkPY189v-Ch4o6GlprnMsH0P9631c3H0-GRF6RpWHVS6ret55KIOchlaRe1tdnadCM1X2T6B7nrPg78SiBSmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارش داد که یک نفتکش در ۱۳ مایل دریایی جنوب شرقی لیما، عمان، مورد اصابت یک موشک ضد کشتی قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134985" target="_blank">📅 10:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134984">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / برخی منابع عربی: پالایشگاه‌های نفت در بحرین مورد حملۀ پهپادی قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134984" target="_blank">📅 10:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSiO6Tmwb4BIbmcTdMwsBhNflnK9dZiFSz1_8mOUWy6pvRUFm2fQQlJ-3h3NZnINNTqav5e_TT7WfOCfP5__qzQHax9ntJAhb4OSe8nUb8f52K4il0JqBll182ef7xTzQaZX6sQLPKk5d_Hd69TQKTfn6uy1UhK8GFEB8SMF8UX7Y9GIfFpwdl4TbBgHX1BxtjlTqM8t65lfITyjOa32-c6ts2uPCiCeX0ECXsAgwhUKzDjNnGjX30zfvcZJ-SxTf6DSMK8QXb82Xa1-jdTqnsYBwmVJL8Md6k2xwDgwgG0DU--VvrBDEVKXL63tThFkKj-SIulqgXS2yrOnrozNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a4635a48.mp4?token=oO8-fDu5_d8v-3l53QOeI0ozm4_AGHak-UllQiVNCoN_rxLR0-M0y0dGQKPNoov3qhHD1kFphAK2ZFYOLAzEcbGFVJdrRZY5_TTiAtefxUKEzwVKitLE7MVDmeGIM-uBfpI4Yv3vdXS_Rlmb-N53RpNxqGUQ8uuvsXBQm86ytWaLQYmJGmV509aPulG0kD6faEAEehaemZS8PQ7f_qFOlCcrQffui-gIbhYQdYm1zdKk8LNhwtJtvNDCTIrDTdFS3eHxYLyih1YD7S-XZSNU6-jw6vn_FFlqPijcrZDsA-i0mrSZI_snG2-pTUnLt57ngBDOA_eS49qWocgRj4RzIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a4635a48.mp4?token=oO8-fDu5_d8v-3l53QOeI0ozm4_AGHak-UllQiVNCoN_rxLR0-M0y0dGQKPNoov3qhHD1kFphAK2ZFYOLAzEcbGFVJdrRZY5_TTiAtefxUKEzwVKitLE7MVDmeGIM-uBfpI4Yv3vdXS_Rlmb-N53RpNxqGUQ8uuvsXBQm86ytWaLQYmJGmV509aPulG0kD6faEAEehaemZS8PQ7f_qFOlCcrQffui-gIbhYQdYm1zdKk8LNhwtJtvNDCTIrDTdFS3eHxYLyih1YD7S-XZSNU6-jw6vn_FFlqPijcrZDsA-i0mrSZI_snG2-pTUnLt57ngBDOA_eS49qWocgRj4RzIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام: «تفنگداران دریایی ایالات متحده از واحد یازدهم اعزامی دریایی، در ۱۶ ژوئیه، در خلیج عمان، عملیات بازرسی و تأیید ورود به کشتی M/T Wen Yao را انجام می‌دهند.
🔴
تا به امروز، نیروهای آمریکایی ۳ کشتی تجاری را که سعی در عبور از محاصره داشتند، تغییر مسیر داده‌اند، ۱ کشتی را که رعایت نکرده بود، غیرفعال کرده‌اند و ۱ کشتی را نیز برای اطمینان از رعایت کامل محاصره دریایی مداوم ایالات متحده علیه ایران، سوار کشتی کرده‌اند.
🔴
تنگه هرمز و آب‌های اطراف آن، به جز کشتی‌هایی که سعی در نقض محاصره دیوار فولادی آمریکا دارند، همچنان آزاد و باز هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134980" target="_blank">📅 10:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کنست رأی به انحلال خود داد؛ اسرائیل به سمت انتخابات زودهنگام می‌رود
🔴
پارلمان اسرائیل با تصویب نهایی طرح انحلال خود، به فعالیت دوره کنونی پایان داد و مسیر برگزاری انتخابات زودهنگام را هموار کرد. انتظار می‌رود زمان انتخابات جدید در روزهای آینده مشخص شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134979" target="_blank">📅 09:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سنتکام: مسیر سه کشتی تجاری را که قصد حرکت به سوی ایران را داشتند، تغییر دادیم. یکی از کشتی‌ها که از دستورات نیروهای آمریکایی تبعیت نکرد از کار انداخته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/134978" target="_blank">📅 09:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFD5yRMkvkAUcUaP9irlE8RcN6YwLv7cpfk9fgeyiGry0UiEttwig-OMBdbxiC_8mczLxeLlX8_ghUY1a4oXcU_9zavmRQ5RX6yT8yg7yEA-f1E02PKYJUGoQopywkhzV57UHLBlSUN-hKUiO4BtgFvsxHU-8MXtdFCsNXeclU6UPhT1ZLO-1-F_HjBK1d2_FFufof0DeTdBBFScfV_UaxYEIVS9OvBDlwlY70JXM1pxZk3WB5yVlSxrBt1Q7NzE6_HRmQspjdxPXI23vfW9UaB28zPOh7TA30z2LHeQbpZa9wN9ikR4Q78aB3frLzUePoGI9jT6Z9U3IRUwL9U5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که سه انبار در منطقه نظامی زاید در نزدیک ابوظبی امارات، در نتیجه حملات موشکی-پهپادی سپاه پاسداران در تاریخ 13 جولای (22 تیرماه)، نابود شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/134977" target="_blank">📅 09:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ1KQv98nzB2WwxRwFP67tDiYVmLfqOcJK18XJG1qdEqTw29DIdC86bUBaJYmhC8EHor5_SzPAGplJlRrSO7Q8eluZnRUnf63BJyT36AoPy6-I0htBb3k46dkWtHz-1Xi10AN4EWlY3gd9hW6ZRV1ojiNH4BzOnZgfYAxPrttBNeJXgLbi_ZR434SeJ2JEdzXwPz3dwJtyMcuetfFEOayIFwCBjw3E-pxa2p5rD8qZLFBI2N4QaLe442s2f5ts9hQx4mHtQgau4-1KoEZAtpnFUIBA0szLpoDKmfEboMpXxxejrSvc8xa8J2JJFPkuKlUmS--ffsyeulWwI9Bg3W4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردن اعلام کرد سه موشک ایرانی شلیک‌شده به سوی این کشور را رهگیری و سرنگون کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/134976" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134975">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
الجزیره: قیمت نفت با تشدید حملات آمریکا و ایران افزایش یافت
🔴
قیمت معاملات آتی نفت برنت به میزان ۱٫۰۵ دلار یا حدود ۱٫۲۵ درصد افزایش یافت و به ۸۵٫۲۸ دلار در هر بشکه رسید و قیمت معاملات آتی نفت خام وست تگزاس اینترمیدیت (WTI) آمریکا نیز ۱٫۰۳ دلار یا ۱٫۳ درصد افزایش یافت و به ۷۹٫۹۸ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134975" target="_blank">📅 09:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134974">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551b40e9d2.mp4?token=i7aYBHjh6GzmIxfyhfK0Dj9qQ_2mgzQIClW378xvpritgYLLVXwW_XdzRoQAWkbtAfsgYbr24gz103IItw0VJMndzJjb92S2g3XJbn3KLRpMJYbUf-kcANGDgoUHGjgjOUqva6Aw1dN-0hPKifEL5les1uA9FDjU-iOnAbeb_QDVHlX8ePOr2JY5gKdPUv_HhjmwOX8aEcy4bJgPpqlzSRC4XhyIp5nsjNySUjnM4nl13oAjcxSWJSB6ljrUtZnosEkBU-3o-XsbxF7_HGPbXRMX8J_9lECYU0SPY6W7yj636u5_MIbLnRdeG9vBxSHhGsWZSvN-GDBSxm_Ltg9kmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551b40e9d2.mp4?token=i7aYBHjh6GzmIxfyhfK0Dj9qQ_2mgzQIClW378xvpritgYLLVXwW_XdzRoQAWkbtAfsgYbr24gz103IItw0VJMndzJjb92S2g3XJbn3KLRpMJYbUf-kcANGDgoUHGjgjOUqva6Aw1dN-0hPKifEL5les1uA9FDjU-iOnAbeb_QDVHlX8ePOr2JY5gKdPUv_HhjmwOX8aEcy4bJgPpqlzSRC4XhyIp5nsjNySUjnM4nl13oAjcxSWJSB6ljrUtZnosEkBU-3o-XsbxF7_HGPbXRMX8J_9lECYU0SPY6W7yj636u5_MIbLnRdeG9vBxSHhGsWZSvN-GDBSxm_Ltg9kmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملات موشکی ایران به پایگاه‌های آمریکایی در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/134974" target="_blank">📅 09:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134973">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPsRbdD5toprI5GrBP3uXL7ak4BAJkv3ZhyaGUMMo_Yd7ZXPCatvdC2f6dlrQRpW5tbLvNJHeBDbjPUg77w7WTAsfFPaJkf9GYw5a3NSyAglPMXDcJBBBCWGf513W5PqtisvFb9Y08Xmv1bpPAwuPidzzuOHd2mqBh_ePVoU5-OtHBGQU9X4NQNSVnA3vCiBDembTYQrOBJmfPN33u5_CVpfoqaZ38bIn4fF4PRLN3xmh1W21XIkw99gkVZvafQpUYvEGVHAs0ZBLNIAjNdXnSaJJlaSURa6_E--ogV7XoIMcDQ7J1NOB2od241mA95DMrkh0i1lsbJGYEdZgBbRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134973" target="_blank">📅 09:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134972">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سپاه: رادار کنترل دریایی در صخره‌های سلامه و رادار کنترل هوایی آمریکا مستقر در منطقه غنم عمان منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/134972" target="_blank">📅 09:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134971">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام بار دیگر افزایش یافت و قیمت نفت خام برنت به ۸۵ دلار به ازای هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134971" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134970">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پکن: چین و پاکستان خواستار آتش‌بس و از سرگیری مذاکرات بین آمریکا و ایران شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134970" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134969">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
مقام آمریکایی به وال استریت ژورنال:
حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134969" target="_blank">📅 09:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134968">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=s8u660rjdJBthM1xrVUcF7BZRGxvNxCfkPK2Caxaly6pzBRehYH0S3YJ56-L_GxvlNt2VfC6KnG2VHd4ruq8bsoRgk30jJ-ZlGtG1RtDAygZyy4ULMKjb2S1sr9ao3Uqq91mmnc9SY8BfapWHtA9yZlAhFkAhz9XsZQH2hH2exriT5ofuj4JMEM5rSHTl3OlvjCOpiPetyMg9TuPw-fBZ1KbO2j_a3EFG1jpY2c5F7OQ77du84aD6hawK1aqDeBmGFp3ydx-NQTS9BR-hfsFS1FXij4hBzVh1gmqgrYhR6J9ti0EcJc6p_95bOOU4QKLB4RxSloIq4F9PSgOsDeSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca4c68898d.mp4?token=s8u660rjdJBthM1xrVUcF7BZRGxvNxCfkPK2Caxaly6pzBRehYH0S3YJ56-L_GxvlNt2VfC6KnG2VHd4ruq8bsoRgk30jJ-ZlGtG1RtDAygZyy4ULMKjb2S1sr9ao3Uqq91mmnc9SY8BfapWHtA9yZlAhFkAhz9XsZQH2hH2exriT5ofuj4JMEM5rSHTl3OlvjCOpiPetyMg9TuPw-fBZ1KbO2j_a3EFG1jpY2c5F7OQ77du84aD6hawK1aqDeBmGFp3ydx-NQTS9BR-hfsFS1FXij4hBzVh1gmqgrYhR6J9ti0EcJc6p_95bOOU4QKLB4RxSloIq4F9PSgOsDeSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت پل کهورستان در محور بندرعباس شیراز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/134968" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134967">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIiRert8UMl28JHX2vUXy89EOf67cie6s97oeH3cgimVxV8_KtOU4JOvKbNos53DQ63eD8tciWYb4pecx9fI84rsbhkg4w8Tgqpe7yOx_QkAocNiUA5KtkR-6Ze1YeGbA_bSI3-HnZRewKoURl9cLa4ijhZ77JD4eDT8k7LRAu6sj38fCGgSFuY3EGUQUGOy6CSzwMOaHNe6NLZR-ZjEfItSTWd6HqqHGt-q-vO6LXxQ5RNRpFppob3nYPkmAbrKS6bf_6_BtSTy6mpcjYcnghfzXlFpaUTb5RsSNnfcM2hJDMaQD8yIDr9fkQjXXkTIDJitZXYRLq96-W2vLhR7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستون دود در
نزدیکی فرودگاه اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/134967" target="_blank">📅 09:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134966">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913d736794.mp4?token=fpvYsQB7YBcPkH1UctlSQ0HcNkpKVyTBWzrRvT-hKg2Wg4hyaJ8pNQF0ANyJ5OwCFs7hGbDtcfsM1uqEjYs4AqcaeQWFCoozqo1ZvcC6JILb70pt0Q0SY3MjOjJk0ai9uxga0A8fAqXFmTK5-75suVn7fhC5jKPI2QvDvZVe9yTww9QPsIPRLyAjMTt4vjeCbMp1XHAOyP9ROFsqZSDusd5RO5zIA-WneRnEjKVfeT93rSZ7QxAQaZitpnoml99yHNxXVP-UgBexHx4LZ8VLcDIjjFlyaIwqRiteIj7l-Dh1HhSsR1QSNkQRTxPVyByAvgw-v35KR4Gt6B9V89IuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913d736794.mp4?token=fpvYsQB7YBcPkH1UctlSQ0HcNkpKVyTBWzrRvT-hKg2Wg4hyaJ8pNQF0ANyJ5OwCFs7hGbDtcfsM1uqEjYs4AqcaeQWFCoozqo1ZvcC6JILb70pt0Q0SY3MjOjJk0ai9uxga0A8fAqXFmTK5-75suVn7fhC5jKPI2QvDvZVe9yTww9QPsIPRLyAjMTt4vjeCbMp1XHAOyP9ROFsqZSDusd5RO5zIA-WneRnEjKVfeT93rSZ7QxAQaZitpnoml99yHNxXVP-UgBexHx4LZ8VLcDIjjFlyaIwqRiteIj7l-Dh1HhSsR1QSNkQRTxPVyByAvgw-v35KR4Gt6B9V89IuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ستون دود برخاسته از مقر گروه‌های تجزیه‌طلب در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/134966" target="_blank">📅 09:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134965">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
فارس: آمریکا دیشب ۵ پل را هدف قرار داد!
🔴
پلگریوه؛  مسیر بندرعباس، خمیر، لار
🔴
پل بعد از روستای لاتیدان (کلمتلی)؛  مسیر برگشت بندرعباس، خمیر، لار
🔴
دو پل مسیر کهورستان، لار
🔴
پل نیمه‌کاره؛  مرکز بندر خمیر، کشار، بندرعباس
🔴
پل روستای مارو شهرستان خمیر
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134965" target="_blank">📅 09:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134964">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vaktg3MFHk5hlT2WQOqg1zynrvvQWmdpz3ZdJhGB7xClziJtQAxtYxMyT2nfeUQN5pRTsbNgg38IWMgw4IyM1wOobvNwyUGef-ZuPP8Svvk_Gi6kg483kYXRtqCaZ7QZyIgsQQx8zKBz8Jnhc5T5EqbMUqY-XP1LX0Bg71NsjvYWhbhb6iI0UoZOwKVryLCd9DNQaO9TVmZqP0Fn47LiTB2_CuA22GACw3u8YmhCBLK2DMVjBw-dpzvirLLHgeOQ4oFwHsT_9raAjjGhYrGla1_TP-fpLmqUImg7DUWBQYdgZsoRTCHjDtDgB3dAywAIOLuh-OpuVjS3rSriGcx0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهباد آمریکایی روی آسمان چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/alonews/134964" target="_blank">📅 05:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134963">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ در پایان سخنرانیش: ما قویترین ارتش جهان رو داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/134963" target="_blank">📅 04:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134962">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/134962" target="_blank">📅 04:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134961">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c26581b61.mp4?token=GvNjNxesN4uikOqXOPGQfI7WREv9LjKyAsPEPuZ1pdTYwLkNQYbRArUmsU0leT5zWvxjGNyveHRIEAIPnZEPBC1H4q6RrPYJqg7iYGwObaijPF3PFgdww5JNIrfh27uvFxtynFNXn4MIWMZWGcEOmgacvhWKwBzRgNG4cEVVObJxIVgp_tuD03DfEyHV7f4BSoPUuE_zlhBsM154frlrvjyLWK4TgvDf69NKjy0wTjIHq1CUdhKeQubEgPHw6u22Q_haFzsp79puQ9072D9hT1LmkbpMKqcrlHr98HZgTvZpkw4vBkMv_NObm5U6xaopDjxZY85-hfiWSilgqhQvSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c26581b61.mp4?token=GvNjNxesN4uikOqXOPGQfI7WREv9LjKyAsPEPuZ1pdTYwLkNQYbRArUmsU0leT5zWvxjGNyveHRIEAIPnZEPBC1H4q6RrPYJqg7iYGwObaijPF3PFgdww5JNIrfh27uvFxtynFNXn4MIWMZWGcEOmgacvhWKwBzRgNG4cEVVObJxIVgp_tuD03DfEyHV7f4BSoPUuE_zlhBsM154frlrvjyLWK4TgvDf69NKjy0wTjIHq1CUdhKeQubEgPHw6u22Q_haFzsp79puQ9072D9hT1LmkbpMKqcrlHr98HZgTvZpkw4vBkMv_NObm5U6xaopDjxZY85-hfiWSilgqhQvSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور آمریکا، دونالد ترامپ
: ما در ونزوئلا پیروز شدیم، کشوری که اکنون با ما همکاری می‌کند تا میلیون‌ها بشکه نفت تولید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/134961" target="_blank">📅 04:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134960">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4ce05c84.mp4?token=kB9JaB-UDyk1c2DrCQ_FSLqPUfMaqfBJtaNoec1ctSdQm1pChxLj08dkdIt5dFS72YnB2gFBSXciUBH3_M7GSvwW01dWUzUT9K8ud9MO36G9AdvA-S53IgMXcKD5Ei1O_AL3tWy3lGmNVwYB-d9rtHgtrAeh38k-Z7_Tzge1bVGM7yRjmx9Skvrw4YHTkS5buzjP9s-KTeEgL4VYYFqjE_rP55427cERtWqTuqqJWxy6nORjWv3CfPzSFrZAauha3PcV5jEwflCwm_gbEPijVltNELTpUNXmHxGBa9gf_JEKMT0ZERGmK9zeYrB5yie0WhLDfmBtXIe3cLksn63FSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4ce05c84.mp4?token=kB9JaB-UDyk1c2DrCQ_FSLqPUfMaqfBJtaNoec1ctSdQm1pChxLj08dkdIt5dFS72YnB2gFBSXciUBH3_M7GSvwW01dWUzUT9K8ud9MO36G9AdvA-S53IgMXcKD5Ei1O_AL3tWy3lGmNVwYB-d9rtHgtrAeh38k-Z7_Tzge1bVGM7yRjmx9Skvrw4YHTkS5buzjP9s-KTeEgL4VYYFqjE_rP55427cERtWqTuqqJWxy6nORjWv3CfPzSFrZAauha3PcV5jEwflCwm_gbEPijVltNELTpUNXmHxGBa9gf_JEKMT0ZERGmK9zeYrB5yie0WhLDfmBtXIe3cLksn63FSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: چین به اطلاعات ۲۲۰ میلیون پرونده رأی‌دهندگان آمریکایی دست پیدا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/134960" target="_blank">📅 04:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134959">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ:
اگه من تو انتخابات رای نیارم یعنی تقلبی در سیستم شکل گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/134959" target="_blank">📅 04:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134958">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37596bf02.mp4?token=ey1EttK-fmlwz6NcaSLO-AFJi-F6RSEuMtqt5a0sx_qdRBmmUT-XQMePVETTSRiuvgVCjJBNTKJofmbKr-E4d0gbjClkln91LfsUn8sg4mCuDEx6VazyZ81Qk9cpASWUQPyxPPIr_EsmiChkHG4B7ewQk4ynrc20xK5wtM0ynBx-eKRshptgxj1l_LCqPHw_98yWBxTPW-1Wbu1IM3DVvblyw1XKGXaWPK26d1w_urIt-32TXfRXQpsH3sr_0nqYh7meTewCr3G96TBewlYi0a0VCDYMoiIf7ZoeckSQeNAojDZXMzxUJVwdUciecx5GQHbvsnKtd-rlKLlyljMgNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37596bf02.mp4?token=ey1EttK-fmlwz6NcaSLO-AFJi-F6RSEuMtqt5a0sx_qdRBmmUT-XQMePVETTSRiuvgVCjJBNTKJofmbKr-E4d0gbjClkln91LfsUn8sg4mCuDEx6VazyZ81Qk9cpASWUQPyxPPIr_EsmiChkHG4B7ewQk4ynrc20xK5wtM0ynBx-eKRshptgxj1l_LCqPHw_98yWBxTPW-1Wbu1IM3DVvblyw1XKGXaWPK26d1w_urIt-32TXfRXQpsH3sr_0nqYh7meTewCr3G96TBewlYi0a0VCDYMoiIf7ZoeckSQeNAojDZXMzxUJVwdUciecx5GQHbvsnKtd-rlKLlyljMgNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ
: اعلام می‌کنم که از همین لحظه، اسناد اطلاعاتی مهمی که آسیب‌پذیری‌های تکان‌دهنده‌ای در زیرساخت‌های انتخاباتی آمریکا را نشان می‌دهند، از حالت محرمانه خارج شده و منتشر خواهند شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/134958" target="_blank">📅 04:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134957">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38775e5358.mp4?token=Tbolz2Xq0ajjOx9Vfd6YBUG_wTwMqe_tVSzVKn4atbmA3s-U7hDtilb3dyONkmKQWvDWEnee6giXazb626fikGJSPhDQr1c-8cGzVLILCviTxqIsTZEqjZ8G9p_yB3_S0ZkpJykkJ2wTcrPBKH-24AMKKufZArEPMb0-qQp4Y76bi-1kjOm8aoqjBgWeOJTqV5lUzr9in7bk2ipIMJTQDJrXPRmYPHaJ01Nb8R6DcQNveMCaRPmIzCmeOp52kjOpOTV1gNWBXqMW2ADFbGOidRWR0n2N6FTbQ_f81-B2ypAJLEzBwOlw-9eSEBoq4SYsH7bd4eMeEERu1aMWGoswOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38775e5358.mp4?token=Tbolz2Xq0ajjOx9Vfd6YBUG_wTwMqe_tVSzVKn4atbmA3s-U7hDtilb3dyONkmKQWvDWEnee6giXazb626fikGJSPhDQr1c-8cGzVLILCviTxqIsTZEqjZ8G9p_yB3_S0ZkpJykkJ2wTcrPBKH-24AMKKufZArEPMb0-qQp4Y76bi-1kjOm8aoqjBgWeOJTqV5lUzr9in7bk2ipIMJTQDJrXPRmYPHaJ01Nb8R6DcQNveMCaRPmIzCmeOp52kjOpOTV1gNWBXqMW2ADFbGOidRWR0n2N6FTbQ_f81-B2ypAJLEzBwOlw-9eSEBoq4SYsH7bd4eMeEERu1aMWGoswOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/134957" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134956">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857d55ae03.mp4?token=KAFrgTNdxpQK8Axmz29DwrcZqbRQKiXCdfXjne60hQk8VI94ligb_bFHhzS-Tl9JFo1gi_hiVlDik7UusqETOS09WnqwYXLFUVHCOkoT75coabrJJ6AwwzrVDE4mHUd7FzPrIJ_lSdud74aouOg6Q1fR4xpLEChKbHotJASvdeIvCcDChyUlFVcORnBRPZQZwCY_sL7Z1XKSbgoaUzp1Eb1Gagkfk8Im8rWx7bEkGjPXoE3sbhX5BcTiqQRsDMTMhH_o4ahsGBRRoMzTsYoCZjSVROiGjA19G80kcmSei4OXx_wbJVqpIxV3uwVK3vQYONGsHMhcNAsfn6vdaa1bWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857d55ae03.mp4?token=KAFrgTNdxpQK8Axmz29DwrcZqbRQKiXCdfXjne60hQk8VI94ligb_bFHhzS-Tl9JFo1gi_hiVlDik7UusqETOS09WnqwYXLFUVHCOkoT75coabrJJ6AwwzrVDE4mHUd7FzPrIJ_lSdud74aouOg6Q1fR4xpLEChKbHotJASvdeIvCcDChyUlFVcORnBRPZQZwCY_sL7Z1XKSbgoaUzp1Eb1Gagkfk8Im8rWx7bEkGjPXoE3sbhX5BcTiqQRsDMTMhH_o4ahsGBRRoMzTsYoCZjSVROiGjA19G80kcmSei4OXx_wbJVqpIxV3uwVK3vQYONGsHMhcNAsfn6vdaa1bWoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: قیمت داروها بین 70 تا 80 تا 90 درصد کاهش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/134956" target="_blank">📅 04:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134955">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ :قبلاً همه دنیا به آمریکا می‌خندیدن، اما دیگه اون دوران تموم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/134955" target="_blank">📅 04:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134954">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
گویا دالامان که نزدیک آنتالیا هست پرواز معراج داره، این پرواز رو یه آژانس هواپیمایی ایرانی چارتر می کنه هر هفته که مسافرش رو از آنتالیا برگردونه ربطی به مذاکره و ... نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/134954" target="_blank">📅 04:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134953">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
برگردید عراقچی نیست توش</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/134953" target="_blank">📅 04:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134952">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
هواپیمای عراقچی رو آسمون ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/134952" target="_blank">📅 04:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134951">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
انفجار ها در پایگاه آمریکایی العدیده قطر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/134951" target="_blank">📅 04:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134950">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRud54AT9BAbNxfF_hA7rUNS1RqONG2dDblO8uv8cp6ZydDANEb3lTpuR676DBe5-_hhyv5WI6iqNRYc2JZnTtjxxbmvNr874Nr4-eHUYqXY-R7Pgo24YCrAAnJ1E1DusmgMyleBexw9hQq2uhmEcyqRZCcwPjwZ15udCI0WrIiice201502yTO_7gm30UknILhw85W5bNxYoG5BZFAkAcSBWkE1RKpCFSWpPFFuvu389xNkdYvkZsVrKerU-BhWOpev3XcIo2L_f2Pxj7F8pbfKMQ8efr9ZYuncXXhM_-qL5_wG2VxY5E3AXF8a8kTMl-iBk4Wb-bHb22cHmmsqXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت شدید پدافند در بحرین هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/134950" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134949">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmI06Kc6xENZEJiAPh8T9QSPwfHpTTUh31lJc020ZDTuF1fx-jVB51dzm04dLAwFpmDG8MkYew0oGERelzH71q-KF3dIg5MVrSvSWs-yLKqtlcRP1LDUByMmpZyoL7nSLbsD2i5c1EhrD-vuVeZH2Ni7mgQ6CZdjk2NK87ELatJiY8wFI5a7PeUTY_hDNNRmfXpydBFjzDplo7LIERAMFYiUnVH2MKySB033kP2A2jozcJx6YCFc8po7DgCvFB_NOpfzJCJXE9J5tX4gnJJaSKSokZNC439at1AleNNnPXF6fxfHRdmBPGQSOTh4YQVoo2MHnpeBdFncQaVe3k-fnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان قطر بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/134949" target="_blank">📅 04:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134948">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
حمله موشکی به العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134948" target="_blank">📅 04:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134947">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ویدیو تخریب پل ملک فهد که درحال پخشه متعلق به یک پل در روسیه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/134947" target="_blank">📅 04:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d99c3c0b64.mp4?token=JQxU75zpPJM24VK48Y9lMW8cXKTmKE3PnHuCxX6ezk8jaNPjtQZvKR3rWDPNrP-c1Kyh6g8xJWa2W2sHKT5gFV42OQpZmHUPTXeO3lqBzqz9dd6XqRmwCyIFwv6RC9BWgIyg1OU4bgW92nnWryLJEtMTlyNqazSB5-0VQE_vOBHCRIPMEtJGcjAk8nwzrCQkXE1N5tGHoFV8tiiPvAhzhqbz8eL8HibGwKGR9ibeRHhjs70u-TFiGBLyu53tryMzF_Hm5J7qDBVrHLk83OuAMcg8PzBeXQPg6wmpcGQSVLUFwyfM8zUxW8wePzwh4M2hOuGwK3zv_MgXK1Reyi6z5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d99c3c0b64.mp4?token=JQxU75zpPJM24VK48Y9lMW8cXKTmKE3PnHuCxX6ezk8jaNPjtQZvKR3rWDPNrP-c1Kyh6g8xJWa2W2sHKT5gFV42OQpZmHUPTXeO3lqBzqz9dd6XqRmwCyIFwv6RC9BWgIyg1OU4bgW92nnWryLJEtMTlyNqazSB5-0VQE_vOBHCRIPMEtJGcjAk8nwzrCQkXE1N5tGHoFV8tiiPvAhzhqbz8eL8HibGwKGR9ibeRHhjs70u-TFiGBLyu53tryMzF_Hm5J7qDBVrHLk83OuAMcg8PzBeXQPg6wmpcGQSVLUFwyfM8zUxW8wePzwh4M2hOuGwK3zv_MgXK1Reyi6z5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک های ایرانی در آسمان قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/134945" target="_blank">📅 04:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت کشور قطر:
سطح تهدیدات امنیتی بالاست و از همه شهروندان تقاضا می‌شود که در خانه‌ها و مکان‌های امن بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/134944" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
انفجار در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134943" target="_blank">📅 04:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
برخی منابع: اعزام گسترده نیروهای امنیتی عربستان به مسیر پل ارتباطی عربستان و بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/alonews/134942" target="_blank">📅 03:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
چندین انفجار جدید در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134940" target="_blank">📅 03:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18319f2842.mp4?token=pw2dbduhgWLihhMZH86Q5Ihml_xO32XxHjJbJKBfki5Ank7L3cnBO0zCOX9HvE6QtKuuRAsf-7pk6W_96cFmdOcoCa2wr-ERSAkwFT4vJORDC2JiKXCZRi6EZBOUZpEV3hcZ_h0JbBam1Xr4rZ1vB0rbgdM3G77R8eCrOb4INP1yQ1IPhXmbzBek42flFZEAkQlgIuZjQ0d-RWXTyktQwpazc4yhgVoBoeqTcPwxb5oYlgxec1D-7SgNwwfeuruw8e5jqBbA19ssmayIbAotI4qNNdZ8DlTRr9Cr-n_DpQdzgCpOvbaVrN64Y0hiUyqGiXxGLfenIpxKkrmzV6206g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18319f2842.mp4?token=pw2dbduhgWLihhMZH86Q5Ihml_xO32XxHjJbJKBfki5Ank7L3cnBO0zCOX9HvE6QtKuuRAsf-7pk6W_96cFmdOcoCa2wr-ERSAkwFT4vJORDC2JiKXCZRi6EZBOUZpEV3hcZ_h0JbBam1Xr4rZ1vB0rbgdM3G77R8eCrOb4INP1yQ1IPhXmbzBek42flFZEAkQlgIuZjQ0d-RWXTyktQwpazc4yhgVoBoeqTcPwxb5oYlgxec1D-7SgNwwfeuruw8e5jqBbA19ssmayIbAotI4qNNdZ8DlTRr9Cr-n_DpQdzgCpOvbaVrN64Y0hiUyqGiXxGLfenIpxKkrmzV6206g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش خبرنگار تسنیم از پل بندرعباس به لار
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134939" target="_blank">📅 03:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIdmE-o-385n9h-z5HrUFtbArUM9gcGAKmA-NXsc5u2KrMQ3t8QbLYiiNCxivFUVfUt3fY_fLUsfyoQ1NQ-LDFv167DR0irymRdE45fHcYjN1pRk55fE9UmCY3voGyc1D-4KQQpXEacPTz7LHgqfONED9BVzSCFmbkz336PrqnOsly0U3pqxEKBAYITVB2g60T67gpAGonndCNvcmHRUHvOj85UDT4FgrRz4ewvwLFrQYOhclIFGgCa0ScLcjrE2nrwujO7_V6dC2YD41Q1Z_VNli8EKaQSMuZzxavsjS8wuO76W1Og2T0eePFsx9PY7u0riAqPsT9sLB2ddglHgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
شاید به تهران حمله اتمی بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134938" target="_blank">📅 03:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
مقام آمریکایی به وال استریت ژورنال:
حملات آمریکا به پل‌های ایران با هدف قطع مسیرهای تأمین و پشتیبانی به سمت بندرعباس انجام شد؛ جایی که ایران یک پایگاه دریایی دارد و از آن برای حمله به کشتی‌ها در تنگه هرمز استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/134937" target="_blank">📅 03:41 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
