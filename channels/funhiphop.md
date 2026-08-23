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
<img src="https://cdn4.telesco.pe/file/tsKX1Fz1vz-gmkTtZfI2T-tYh2q7aimCKZDxUqe0pruKpOO-4cXUrDiTqqRhg8_bZd0psRICI14iEa7DfJkjLyE2mkOCv3Y7wPFQUJ-EIdMHYrCfYXkI0ZyaY1pHexbaGiGS0lkcfPF4bLj0W_OJGIFblpjUkhRpcYNNa4pfemz60FxcpFinP3RRM_9EnrheS9nW8hoVphmGSeQUavuVRyktP6MS--66RtsxtvpiGL3E_vDgKPRPWEX7dAO82rbwZ3SfTSpgoEjNtB45lTI2_KOLHMMI8086tMoyyLxgPm5-bTVboQYIBCogpNxIe3evifzXiSPBceEcXJszfI94pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 19:13:37</div>
<hr>

<div class="tg-post" id="msg-82494">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a34a3c950.mp4?token=MQh8GWyYenk8rTVJSgq225QrPQwQWsoNyONLL0dorp3LKZwq80iz2nK1OZBMlNl8Wy3iNwePpp8zk0yYowiV-j0dL4wBplJVjXRcWNbNjGwq-ytZEMsiMLtVvcw6l6wgkyzLYhfaKJdj2iHEc7URVlujEGsZz3xJPL1RGBXILpk9c7spahEVCd-XUb6mHx-1ydjqge7nggrmUBgRMkIfd3sX_BIhJowfan_sA1bsjqeIVeiVkFnHDgrnr2HHL0ujCOTSnP8dUnUIe2loD4ptaIj190hgYcrjM4VMSRiWYrkxmsfhwbSQj0z0qWI_dXIIVQtimVAmgwFXOLvlO81ekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a34a3c950.mp4?token=MQh8GWyYenk8rTVJSgq225QrPQwQWsoNyONLL0dorp3LKZwq80iz2nK1OZBMlNl8Wy3iNwePpp8zk0yYowiV-j0dL4wBplJVjXRcWNbNjGwq-ytZEMsiMLtVvcw6l6wgkyzLYhfaKJdj2iHEc7URVlujEGsZz3xJPL1RGBXILpk9c7spahEVCd-XUb6mHx-1ydjqge7nggrmUBgRMkIfd3sX_BIhJowfan_sA1bsjqeIVeiVkFnHDgrnr2HHL0ujCOTSnP8dUnUIe2loD4ptaIj190hgYcrjM4VMSRiWYrkxmsfhwbSQj0z0qWI_dXIIVQtimVAmgwFXOLvlO81ekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آفرین ایرانی باز افتخار آفریدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/82494" target="_blank">📅 19:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82493">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOmPJSAdz0gSOYctqKgXWUxZv0SVrFAMntKvefHs-tj-sTUjmDd-OXaI_PlAXLPRbdh1BUN1IPyTWeQb0e5Qh6cc0N5MoJ_5xWakc1MjA5dG1wbXMfx8Mi8YcwMNmLNaXSVKuZr1KX2iUqyBFa1vfjGsZiRnRdBkfhVtPKtwe_6zIAeWJt8Bn8A-sgcrOHpHnhiNSwnnYvArttMlf1qRxFa8OwQ67EfWdhpsAqEKT0cOv-3_uVFozVnxTNCvgf44mKUF4gbsEVg7W8dlgrMgHd9o4tTCb_IhB98tMYRL_twZuLdyFSP4bUPWkd203WSj7WzKPlnFGPcSmr6Cnmex_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
الچه
🇪🇸
-
🇪🇸
بارسلونا
🏆
لالیگا اسپانیا
🇪🇸
🕔
یکشنبه ساعت ۲۳:۰۰
🏟
ورزشگاه مانوئل مارتینز والرو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
الچه
:
۳ برد، ۶ تساوی و ۱ شکست در ۱۰ بازی اخیر.
✅
بارسلونا
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر الچه: ۲.۴ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر بارسلونا: ۳.۲ گل در هر بازی.
🧠
بازی آگاهانه، نشانه حرفه‌ای‌بودن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g1
💻
@BetForward</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/funhiphop/82493" target="_blank">📅 19:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82492">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c451060b.mp4?token=Owwr_-3sGrwDuw6Cxi0HBJPr_SV98TQgchwQA1QlXHr3mucal233QNPI0_fU-FyjvqX0FXnQnkDkcNBqrZrS3aPWRZgoi3nmfbUt0DpVntwWu7An7tffsTHHwxba3KNso1UxTcWoFjploFq18_AmcOQuHcixYJctMQd7edFLgnv7oWze6Zp-DeRXWPMUXU4cO9Qk5hvslyFbQd9bauKOmM97IdgsUPqvGORWsA9vEvOTh5W_h1cxgUjgAx16mjou_zZMctfDVNC0nK7z4OZsv7yYjSmOgqZ0wljUVgxrc7mYV1qCmt4KBAqBfr7uYEfeEmDhyJFAUr38V1shgvAy_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c451060b.mp4?token=Owwr_-3sGrwDuw6Cxi0HBJPr_SV98TQgchwQA1QlXHr3mucal233QNPI0_fU-FyjvqX0FXnQnkDkcNBqrZrS3aPWRZgoi3nmfbUt0DpVntwWu7An7tffsTHHwxba3KNso1UxTcWoFjploFq18_AmcOQuHcixYJctMQd7edFLgnv7oWze6Zp-DeRXWPMUXU4cO9Qk5hvslyFbQd9bauKOmM97IdgsUPqvGORWsA9vEvOTh5W_h1cxgUjgAx16mjou_zZMctfDVNC0nK7z4OZsv7yYjSmOgqZ0wljUVgxrc7mYV1qCmt4KBAqBfr7uYEfeEmDhyJFAUr38V1shgvAy_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/82492" target="_blank">📅 18:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82491">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خداروشکر جلیلی نیومد که دلار بشه ۲۰۰ تومن</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/funhiphop/82491" target="_blank">📅 15:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82490">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان به نظرتون اسکرین شات دلار ۲۰۰ هزار تومنی و ایموجی قلب سیاه شکسته رو با آهنگای محسن چاووشی ادیت بزنم استوری کنم بهتره یا آهنگای استاد محسن نامجو بهتر می‌تونه ناراحت و نگران بودنمو نشون بده؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/82490" target="_blank">📅 14:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82489">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خب بگم دلتون برا همین 200 تومن هم تنگ میشه یا زوده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/82489" target="_blank">📅 14:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82488">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ویلسون ناموسا چرا به همه چیز هایی که تو مملکت اتفاق میوفته با ۶ ماه تاخیر واکنش نشون میدی</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/82488" target="_blank">📅 14:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82487">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW_VBG4eapG1X8u_zg_pxOa_qMAGD9Xd9TtCY4J90otEjpC7mFNh1xvBimXZZ2JvQIZOnolsMPsoS6f9j9uaUobiKKw8f7kv4rcTVamduGep_HGZXdAsHaiHUAgCI2eKdsaKSpeEIhueJ5D7rQtj_ahwMYCyNHIC0aW_fLGs39G6M8NDTXpXaoOMKABcN4-5y5FcuYGuOkziCHEXnaqkPZRp7dt3C3wrJfwhP8wrXOJKu_LJmjr319elqtFEzRLtJoVfQ93lSRbVms9ICYLdVkPMvH4ndVSFigU2OTifwwmdnwhPIA-y9MjqAC_8Rt7Dbmo-PpK3XD9C56VH_woPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار 200k شد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82487" target="_blank">📅 14:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82486">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دلار 200k شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/82486" target="_blank">📅 14:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gn1UIGPLcehTLJ-DY2hyY6jVsOiXQHnPFZd3WqO-wjw07gEiP4hpPULhtd8BU7nKoJjA0CUz7FiiOSqD0svWYVPg6CJrGMOV-ma0LLTR-B8qnGW4cF3iMJE4QvfluQgMpl_6OQhqGOilzp3AL-sKAa2ZPWHah6QDqP_Ekhe8VVI-hAAil7BGkNY-t44uaTzbv25VYX2fqQMJv7fQMdtRTf1y3P3fOyYJ92sD3aJKVutp3gbptR147jNXD68RPa0a7p4r4JB1R5Yg5EKswJ86--rVJCZtCc6q1Hs0d3VfchUZPpFZ1A3D8WWAp3iF-lHQYh7RuucsU8uxhe90stlPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoJBmOvfZ3TP1KnxBsUsusMitWMFhov5ba1pKQTtz8vMvHzK_ImZeYI9_x_Yx63AKHG06BkcHNIOVtzxLWyKE3Jkx939BhguY4DFCo-yxiA_XM9zwmzhmZ43FTndUDjrN4gR2J9fPhrxD8HwaN5WrSMPZNZ6u5jkTrJ7_IQiTxtzgRgVyXc40AN11KuCQZ6KoX1a8D8uObotK_ThwKl3nk4k4ABAbgXYoH-sY6lgwqKRHTKvnxola85ETkXCUQHEUw8V3j-ljok7fL-iIVWB2f-yMXEQz4rIhh2fBmpLHUN3DU-FD7QKU0l4FUQxeA8UZkikJkq-7C9qXh0fx0dtOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هالند کصخل موهاشو کوتاه کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82484" target="_blank">📅 13:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRi1aop3AQaEmb1_Pnsl51CabNVvByHbhafr3CgvvuiIZn-I5gFNm_Loyy2NZoi7_jMzzyWTGr82qvKvuqqOaUiKNRqdA159Fl-Xj9E0N4tPWDAwqlGImy9x0uk2RsP3DgfXQ3sFFq1mxsKP5KSAOYSs6dZ1ZMuSBg2irOSCnyF3e4-qL3o4vAP9DfgJWNh8GziH6DNEdHQate643s_R-AlKZuh6FDkjV1LNly_2p4uxZ4twF9jJ9KiEEWhd2KAHqKoAtNf_BKCSv0Ho6YFnb0bAhhdLdWcjBXCbscT4eKrRBSYMzBYcyFc4nTTDZJGAOWX0AVSyWl5S5b8Tv6Znfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا ارومیه رو چطوری ربط بدیم به عربستان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82483" target="_blank">📅 12:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df1ed91c9.mp4?token=p0PIRdF9XrHPzgRUaBUuTQDHuONoN0SMsCA_51oLdqfSqtQJ7xRNvxao1Ox9hcnNrAg8p92r3afGkCZhLTKFyzOnEQ2muspP3oGnsiUtWuvpcBva8ZoEbPxJueefrwn6GRnKVQZ1ql6k7N0buWKzTKjhcxzscGsC72uOkODrFgXbous6IYuLygOXTRsmnXfzqjBH50oBf7Uxnzv7v_Dv1qOJbJGCHNWu8zgLUp0SROg6bk_CDsGorzcP3e5WFHHmb6YJ_ARs8s4B5YEKCPbh8DaBM66qKSfagcz2mYpOBEn48gV325qbEeqdspS2jIbYJZnQhgI8oCeHowmhFhY4ZyM1BjNytaY1bEpJ0pgjz454ZbUFtsSNXqDGIDq6Ti7eymSgWX-t5NQI8wkM8tucVGOmdpOCqDjQO8rfztTPiCJ3et-0qNikX8-j6RadNyWYgQadw-6cGaHtmVvptcxRvfW-8bjwiGcQF3ql5wH8DoX4BjQ4EGPkCQw2yoJSEZ5VqckDQDOYstxFKkdZCtbyBPK9D7v9fQDhnlNJTxGxyX8NzZd3fAZo5lwa9JCADKl8yAON5e4OcZjpdEEIONhSdk4xg-qB5Vmts4AXGY5J6exv0Kf8W8pXMAEHlwWpnyF1pK3UN9Z6_2ijhQD8cPjZQpN-3YLSkKp5of4r46P3wTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df1ed91c9.mp4?token=p0PIRdF9XrHPzgRUaBUuTQDHuONoN0SMsCA_51oLdqfSqtQJ7xRNvxao1Ox9hcnNrAg8p92r3afGkCZhLTKFyzOnEQ2muspP3oGnsiUtWuvpcBva8ZoEbPxJueefrwn6GRnKVQZ1ql6k7N0buWKzTKjhcxzscGsC72uOkODrFgXbous6IYuLygOXTRsmnXfzqjBH50oBf7Uxnzv7v_Dv1qOJbJGCHNWu8zgLUp0SROg6bk_CDsGorzcP3e5WFHHmb6YJ_ARs8s4B5YEKCPbh8DaBM66qKSfagcz2mYpOBEn48gV325qbEeqdspS2jIbYJZnQhgI8oCeHowmhFhY4ZyM1BjNytaY1bEpJ0pgjz454ZbUFtsSNXqDGIDq6Ti7eymSgWX-t5NQI8wkM8tucVGOmdpOCqDjQO8rfztTPiCJ3et-0qNikX8-j6RadNyWYgQadw-6cGaHtmVvptcxRvfW-8bjwiGcQF3ql5wH8DoX4BjQ4EGPkCQw2yoJSEZ5VqckDQDOYstxFKkdZCtbyBPK9D7v9fQDhnlNJTxGxyX8NzZd3fAZo5lwa9JCADKl8yAON5e4OcZjpdEEIONhSdk4xg-qB5Vmts4AXGY5J6exv0Kf8W8pXMAEHlwWpnyF1pK3UN9Z6_2ijhQD8cPjZQpN-3YLSkKp5of4r46P3wTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو تظاهرات با چادر تو ساحل دریای مازندران برای اعتراض به بی‌حجابی هایی که در سواحل رخ میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/82482" target="_blank">📅 11:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a208381aa.mp4?token=E04CkJTOlL3cjNFxopTdPvscoh9diQZzk7kMfrzt73ymttRb1dI6UIU0MNBsHxe6ekhjisqVftohLr9EW1XKN4UpaegQwiqQa37FcbffbH-pvBMfM4Jm3px4RFsjwyOnBO8h5AASK7BKM3q_iMSquypjz_CbbV5E2KAsKY9nLoXVxOMfLfcPIF0fSRD0OTHa0uT9cTmlPRKdmn74HmHWSOoxPNhGkGCqY6hDtoBcmYL-343ArcKUWYGdNum4P5sVJ3Xw4s4csEWUW9Uwk__uCiKLLJB5dQsWvk1zTy7gwL64LBsmx8-8e1CPiqx15e72rcdwythhqDSYe_Ajj3EdIIB9tU6QhMqurYDD2GCEkPFhDfFQ227ZB_aQfO6CrdOFj1JKnICaByn0xHozZ8leceqBK3Q-5YAWUvCyCrVj6zOr1nTESLDKRSaei8L1JF_L-tLumaHR1unaxfxQqatokKRDqsscEsoBBVbrIU5f3V_1lgncU6fsPVX3aafO3b2PQs2w6UrgR0yFGlc0ZqOKwzgnVPZX2Pk-6pZbQ4OFkFnqhuiBQS8GJ81n8HhagMH0Meiic3IzJJhNeOF_p6qDXAFEJiEiLdweK2PacZydA5MUSYdSwFx4EfZi6yDQzcrqolNmArOhIfVBlmvMUsDYQFBlm6WjRiu_5bF8swYFDAo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a208381aa.mp4?token=E04CkJTOlL3cjNFxopTdPvscoh9diQZzk7kMfrzt73ymttRb1dI6UIU0MNBsHxe6ekhjisqVftohLr9EW1XKN4UpaegQwiqQa37FcbffbH-pvBMfM4Jm3px4RFsjwyOnBO8h5AASK7BKM3q_iMSquypjz_CbbV5E2KAsKY9nLoXVxOMfLfcPIF0fSRD0OTHa0uT9cTmlPRKdmn74HmHWSOoxPNhGkGCqY6hDtoBcmYL-343ArcKUWYGdNum4P5sVJ3Xw4s4csEWUW9Uwk__uCiKLLJB5dQsWvk1zTy7gwL64LBsmx8-8e1CPiqx15e72rcdwythhqDSYe_Ajj3EdIIB9tU6QhMqurYDD2GCEkPFhDfFQ227ZB_aQfO6CrdOFj1JKnICaByn0xHozZ8leceqBK3Q-5YAWUvCyCrVj6zOr1nTESLDKRSaei8L1JF_L-tLumaHR1unaxfxQqatokKRDqsscEsoBBVbrIU5f3V_1lgncU6fsPVX3aafO3b2PQs2w6UrgR0yFGlc0ZqOKwzgnVPZX2Pk-6pZbQ4OFkFnqhuiBQS8GJ81n8HhagMH0Meiic3IzJJhNeOF_p6qDXAFEJiEiLdweK2PacZydA5MUSYdSwFx4EfZi6yDQzcrqolNmArOhIfVBlmvMUsDYQFBlm6WjRiu_5bF8swYFDAo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خانواده تبریزی تو استانبول عروسی فوق لاکچری گرفتن
یه پولی‌هم جلوی اندی انداختن پاشده از لس آنجلس اومده استانبول براشون بخونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82481" target="_blank">📅 10:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfb4Od7ksUDk0Wl1KgbXiF-rJdS_n0jNRN7Wc61xJjkSanx5W_h1nXrvc2dQYL0jwetDkf9KXgAkO-GHn2nApdfwP2TZTvFhYC6sv2IOPhLsSheh5VRx8VB4hp730vyqdzwxFfphlVtBiiUbzXZ-DCFoTUerevtEnS223KUsBe2El2auxPaD_UYlUsKc6IJLw6i5NcDObbUbiBQn1NkdvWq9YnTnA4LAewsImzAqm4vmv4TNgK2BWOqzs4HrSzgPqPIGD5kJNtoysORgKl06nPLgBjnHPoUWAmvzNmlkel76FLiFa0t4zNQxbj-mXLNYdkcqBgWVbrcxaBb7KVJ5vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
الچه
🇪🇸
-
🇪🇸
بارسلونا
🏆
لالیگا اسپانیا
🇪🇸
🕔
یکشنبه ساعت ۲۳:۰۰
🏟
ورزشگاه مانوئل مارتینز والرو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
الچه
:
۳ برد، ۶ تساوی و ۱ شکست در ۱۰ بازی اخیر.
✅
بارسلونا
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر الچه: ۲.۴ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر بارسلونا: ۳.۲ گل در هر بازی.
🧠
بازی آگاهانه، نشانه حرفه‌ای‌بودن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r1
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82480" target="_blank">📅 10:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صبح بخیر
ترامپ: تنگه هرمز دیگه جزعی از کشور امریکاست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/82479" target="_blank">📅 09:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-BE_Hr5y6GPtv-L7WmLHwgh6Q1JP73nTObnfDKDPtywkl40SACxwMu_uBLXuugncTXZScdkrjndFVBYeKiwp8negik3K7dX7KZqEHc4RSd4dDUSUWp0QKiWE_2uHP_YWmMqxgZfnK8kIWff7fgttxhu0ynhx25YPlsH1duLZLRVR1Gu1Ty9tF8_AUBrgacxzOxH_M5oph7K5AR5S2WL2iDKBrfwwHzncOQSGbhVaju78jKXZSy221yD_p0_crtb1F3yNyQ33b2fPV5FYF10iCkE0b3RFl6SJQEZC4DO6bmhiSUI4-8PRGvb5n3EHcv4kyhmLIUaB5GjRmdfz1GZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82478" target="_blank">📅 01:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کوروش چقد خشن شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82477" target="_blank">📅 01:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مورینیو یه خسرو حیدری و حنیف عمران زاده نیاز داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82476" target="_blank">📅 00:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان که با کد تخفیف ( bakei ) میتونید تا 20 درصد تخفیف بگیرید
🔖
جهت خرید و مشاهده محصولات: @HyperPing_VPNBOT</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82475" target="_blank">📅 00:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓔𝓻𝓯𝓪𝓷.</strong></div>
<div class="tg-text">میخواد یه ورژن ۲ بسازه باگای اولیو رفع کنه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82474" target="_blank">📅 00:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پدر آرات داره بچه جدید میسازه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82473" target="_blank">📅 00:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBTvSNN4HFTSyhOqfoKld1YKT9puZYT4KILYpMpGCTDpC29WlBMkSzyuj0UuX_8OnfxAoqNdyAQOcIdeDwpVfpom3vEvB2OkBR6LLFpTi_YOul-3YZ5F3nENQio652qTFlXRvCTZSRfQwHuQvTGC3mYLzr96bFTIyLi0cNkumrqq8gf5vWkF7F3PRSXSEEmqcgjHMor8Q9Rlvg9h0Zg1NqLXOnEXHwWFI6Jmfq4Eq1azcq_9j4vdhpR51BhyxFd3-O9AqHVhHJa_S5rFtds2Fd1yJ0uih9TLplL1PLLTMJOtriPI8sFR0jeLnf8KQZ41Q0xvBENYk8LfdWz9SametA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر آرات داره بچه جدید میسازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82472" target="_blank">📅 23:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کیه این؟</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82471" target="_blank">📅 23:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txNCDVNKUZ87_FR24z7iacSla-QM6JDAVT4bOi2p3Jn0cyGAvhOE1EoBYQkQ__oRaN-zONLc-7Z-ivMwROubAc0xQnHAnZrq1gpwUqdF2pa6V8xxxxMIpugfq2cDhnmr5bld5sMaejlIs5XTTf9jHTFdBk-SNIQKUeSMuqcs42gv71yoH83t0hYE5S8T3HkIaVwZ3_gnrsP22baXglGIWpe5ehCNyBO_Nr6EMAVaX5cphOeO7OROp1g91xFBZ7d5qtWpUsDPDBfh0dhBZROHjuhbBVmZW0_xRMyabsiUNl_GUocgUcd9S9EYINh7W1GUUgy1MasR1fyfAX3r5BqYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه برا خودت ارزش قائلی از تلگرام دور بمون دادا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82470" target="_blank">📅 22:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان که با کد تخفیف (
bakei
) میتونید تا 20 درصد تخفیف بگیرید
🔖
جهت خرید و مشاهده محصولات:
@HyperPing_VPNBOT</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82469" target="_blank">📅 21:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82468">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdjFnmJdKMd_aHU4mJYwaGicZbhfIf8S63favHHZPpfh1d6DtKRQdZU6x9wrOpZGr9seIfoUhJmQ-CMd4_GEf-FLhbBr1MxA0PtcdsRlmJpVvalBSMiqwU89q6GpVvWy82DDJGBl8w2JEmswHLH-HfFa4PoDJnCeo-bg9Ddt24TiGT_OxgP-JFFZ0FspHh3qC1aQ6IdHOqkOiVeHSG5UI492uk7y60hC2SGMNgvxS9J_tpan7tuSdUzD7Fy0rApXB_KXUARZcqFHq0XPhjaSx_r-dgAY6ru2MZ83LgdJjQHqfRouKNHR2TMmTCKrEScCYVx3hAlRFKvTBKlkV_kVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاتنهام چقد پلشته، با اینهمه خرج بازم گوهی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82468" target="_blank">📅 21:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82467">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82467" target="_blank">📅 20:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82466" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPj3M0FypASU5Q2ir9lz6_iXvY-YqM3oSb5BOnyUUn5BV_Ua830bPQ1xg9cdOrV0hXVlaQWqb273GDNVPYwQGkRzBxCtb7tXmDYH0NrPhGXJpKEIhEyZ9y_OkS-WpUpAxBM7VZlNzKuE1GEfekWAjxy8XjMlSVxaRtiFvRK2lp90DqQS3yN9SUe8hlmT7Va4Uo62QmH-tr4Ons9QDMLtbwKjsUYwHDDr25sT_XrHvKdQl5bxcjSdxkr7ef6gOfu18WS76wRhA9zyPdD9pKQpKjdUmaLNCGjPKdMU3FxX4azE2HujGgj6r0lxZh0HP8gCHePgEKjuBI_94-cgvrIV9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و TM Bax به اسم Shh! منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82465" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82464">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533cf854d8.mp4?token=XandRmKg0U4CpUeTc4_n14PS7LUaP8FHW0eYlt46WHem89WXLnFTGQ3n65YuLHtQg8_LfCSA0-Kbyon4ZNZ0o40zIOSII76zTDuZblSDZ24oCCMdBmYua7hfi6f4kEl0jgLGimmf34KyRKhpGyBH4IQIf4R_3X9Rx60-MAkRmG5y1Rutye-40IKs7J8quxJQWh64EGCYMDg3TYQxAv0XtdZnpyWxsUO_az-6cxLvUGWBRZ9Stk8SUMfRBlmM9jSyMsfFk4QCupC-Vqjq6ZVzal10_0MRZOkx69DMKGSP59l7vqRD5dRNBMg6idTod3Ysjo2-Y6kxnKRmGTrFH-y2tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533cf854d8.mp4?token=XandRmKg0U4CpUeTc4_n14PS7LUaP8FHW0eYlt46WHem89WXLnFTGQ3n65YuLHtQg8_LfCSA0-Kbyon4ZNZ0o40zIOSII76zTDuZblSDZ24oCCMdBmYua7hfi6f4kEl0jgLGimmf34KyRKhpGyBH4IQIf4R_3X9Rx60-MAkRmG5y1Rutye-40IKs7J8quxJQWh64EGCYMDg3TYQxAv0XtdZnpyWxsUO_az-6cxLvUGWBRZ9Stk8SUMfRBlmM9jSyMsfFk4QCupC-Vqjq6ZVzal10_0MRZOkx69DMKGSP59l7vqRD5dRNBMg6idTod3Ysjo2-Y6kxnKRmGTrFH-y2tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرمال ترین حرکت پسرا تو جمع
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82464" target="_blank">📅 19:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82463">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMFM_e-M6hC-pXGJnxeC4OfNCrwLsxbHNk3zp2RcXi7TE5t6T8ZkOjcsvqztTYD-jyg9n2BcRvG35ssbgyWHkMnFQ_7Afx2TArx0CQVuM38RLjQvGfz5bd5ryAKI9BTMuDepjwIV3rM_d1wX_QF2uH5clucQlNpV6QfcovmlNN1Ls_VDZeWCnpY-vPmyza3rG4U2zn43uqAw2Ul0oz1PXMxQa3HIwj9JUmS16fLnLCKYs-0MrNE3VZYIc6VIZMjoS1h5RuESyh9MbmDN5-4Ob9tguS78MhHGWRW7v8Y74t5o1UwoE9C5f8-5v7Xto8JU4ipWxBFrD1NvUuowTClpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضرم برا گیر کردن سوزن حافظه‌ی تاریخی رو رضا پیشرو، دو تا کلیه‌هام رو بدم تا قبل از مرگ بهترین محتواهای تاریخ بشریت رو تجربه کرده باشم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82463" target="_blank">📅 19:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82462">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtClhI6GMj_t4r9066zWEDcJrFprwPzmLPIZLa8iB-6ytXao1ErW2xTl9H_5FixGruVKOhsujKalzqUe8FbTXxYC9dhHFY_jjFUmDkiksUJGmbPKUgMpyK4C_-BIpwouUTk-a1Xe3HEeJoaHXGPGSdumdVW1rA149eaTYViG98oUAj9ovYgjzXRHvJF70xQD3u9zi4WvPSgSX8UZHPvfmnhV5hlE2TZqxNz7HqcXOwhdm-c5Wk_fYDa0m2mOez6XCtlnHAshWMKt-VfT2H1429jEt-jrSc7I2kkwDZWTbOPRb4sUlVjzuRCWTFmnrpJ6MDHtitWQJRLkFBzPuBkQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به رضا پهلوی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82462" target="_blank">📅 18:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82460">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b179e0b7b7.mp4?token=ZGyq6va3OiQ9mjZPqNeF8OG3VKMXncXVfz9jbS_KDO3VVe-bXCSzcv65CHIL6uzqNLYFeEA_wFJjuk77uD3xOGmuzdeYP9_Ko1lsJUfBr03OMTbXTmw7-nXZkn7EyRN-AmZpIBCRCN-LVgS6zJhFMmlOb2w9Ba3QWUChf_Nd2gBGeicpvNmyZFVf4RG5vlhMXxbr_D7CTeK0NUaT68ivKVRkoe8ybP9j5gf0jkGjTj6v1z_W_uCUSjjUxelbVlazctmxHFoDAJVC2wKA2p0g_eDLW6nWMcs7ISi_KfQXuug2I5Q7XWm7n0_8DMnQ9b2d7QO7VGnXdhqSRJ--HOSHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b179e0b7b7.mp4?token=ZGyq6va3OiQ9mjZPqNeF8OG3VKMXncXVfz9jbS_KDO3VVe-bXCSzcv65CHIL6uzqNLYFeEA_wFJjuk77uD3xOGmuzdeYP9_Ko1lsJUfBr03OMTbXTmw7-nXZkn7EyRN-AmZpIBCRCN-LVgS6zJhFMmlOb2w9Ba3QWUChf_Nd2gBGeicpvNmyZFVf4RG5vlhMXxbr_D7CTeK0NUaT68ivKVRkoe8ybP9j5gf0jkGjTj6v1z_W_uCUSjjUxelbVlazctmxHFoDAJVC2wKA2p0g_eDLW6nWMcs7ISi_KfQXuug2I5Q7XWm7n0_8DMnQ9b2d7QO7VGnXdhqSRJ--HOSHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وطندار عربستانی اولین موزیک رسمی خودشو منتشر کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82460" target="_blank">📅 16:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82459">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHbFoTAnfhYCriM2h2Woj1wINo1aHrq3lRTrMHBPTmhiAVlaDrlwTWD82MYbYw-7EAq_pSgqpssnu1X7fFnq02ZeChCUGjIbUlznlNAw1OzlX8KR3-0Pph2I3_SfjTaWURUUpXAlOeD38QctW4yQYhmOi92kc_pQc2MF2g29GcyrMbTYF51dS3CIlXonFB9yy7JQ79dQWz_6FnieWxRfLOJ2KDKdFisYCwB3i_WTg_DBQHI8EWixUw-csrcxEj2_sYTDNZa2VL_V5MrdIce0ckhDyqaPVYK7LMf1kGyRVd0T_UMic-EJM-k6Iek4FcNkI8hf69DcYxL2p1XW8Wwf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدسامتینگشاه:
تو چند وقت اخیر کشورهای همسایه از ما خواهش و التماس کردن که باهاشون قرارداد دفاعی و نظامی ببندیم؛
چون براشون مثل روز روشن شده که وعده محافظت‌ها و قدرت آمریکا دروغی بیش نیست جوری که حتی اسرائیل رو هم تو خطر نابودی کامل انداختن؛
پس فقط یه قدرت مستقل و مقتدر مثل ما می‌تونه از صلح و کشورهای منطقه به صورت واقعی محافظت کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82459" target="_blank">📅 15:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82458">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxvX0uhysuvob7BdRSKUqsSdw38-ztFvrZfd8X9cgeRwPBs9rkqEnmd3zRDfH1R70hGtrSTuvEcVC8w0qOlIp3E4D_ukoM4E1uepw0a6ZeLYKTCk3Dcrb9KYcG-wdmh9ii8z2kw0TIa8ScdaDCOL_JDsN_JjSqKLYcCWZ8XFLf7A6ls41wnHOQHcxtVhBmhO9tJ9HCa2OPCjywDHHIqNIZ-_0CkVSZs6b6MhfD9rHdpU7p3DQierguJ7Sm2aLmGv_az42vjbYovuwPMKL4SCUxVw3Ex44FVUgJVhySAftQdAsRhKKRu7xtT7YaXStTQI0Viw5bW8qe_582f3or4UYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این دالگ شامپانزه رو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82458" target="_blank">📅 15:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82457">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b87bf64f9.mp4?token=GiLagBnDmUL5A9ev8WFZSAIl3QH27sUye7mElbYdCf32jA-ou0kHFHRvcAVD7e6XlCh16GX-Hk7R7JXslqM5wpDP_EoAyiX1zoPv-nWLOLi3XW1ra_1jGHOwZbV8RIJDcgnqP1KSQiO_u0LNApBYmjuSpipH1Ms8fLs76f3VSIWZ1X48moJuy-td1WR7yqmS8Q7mg1aqoXJxAaXqQn0QWnqxWsnmNzm77TJDYXuE096AOqaA9A5CS9z3lpsNCaUDNX4NomGl0HvZEzJEENaVQ7e3gLUIahamOcq4byThLKH4LW8_G5UCQWoIJnrqWFMdSk71O_bLuHnMuLJNoZ2sLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b87bf64f9.mp4?token=GiLagBnDmUL5A9ev8WFZSAIl3QH27sUye7mElbYdCf32jA-ou0kHFHRvcAVD7e6XlCh16GX-Hk7R7JXslqM5wpDP_EoAyiX1zoPv-nWLOLi3XW1ra_1jGHOwZbV8RIJDcgnqP1KSQiO_u0LNApBYmjuSpipH1Ms8fLs76f3VSIWZ1X48moJuy-td1WR7yqmS8Q7mg1aqoXJxAaXqQn0QWnqxWsnmNzm77TJDYXuE096AOqaA9A5CS9z3lpsNCaUDNX4NomGl0HvZEzJEENaVQ7e3gLUIahamOcq4byThLKH4LW8_G5UCQWoIJnrqWFMdSk71O_bLuHnMuLJNoZ2sLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هندی‌ها به کامیون‌هایی که گمان می‌کنند حامل گوشت گاو است  ده‌ها راننده کامیون تاکنون جان باخته‌اند  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82457" target="_blank">📅 15:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82456">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0YvEi9I8F4QepKvvsf0mf31FFJAoH2g-CpHqnqfVe1RZqN3IavflhJtVkaZe4sXGJUbuOXuN-j4cj01FlU0crCbDurOZKJODI-7VdAknkIuhZAxZkPwGm-cyk7f6oIjFDNS2aW-PGSx1DzqZGaKuUOxSK0Nyna8sEFSwDXaDxvgcCq_7AjaZWeFIiF43_peVY5z3spJoVLlj1m0v73FGbjIZFN3awPGIn8qvmdmXaMSMlDPaM1Mq2q0O_YstFh7XLuVH7ZA4vSm3ULaQ-vdzp-X7fdJ9sEasMtQajY7zSogMJHMB18mUmq8puTu6zkR3pJzat_JukXT7Mdex4AO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم بعد از موفقیت ژانر «پشمام داریوش تبهکار بالاخره ترک کرد چقدر خوب شده»، الان وقتشه با ژانر ««پشمام رها وانتونز بالاخره غذا خورد چقدر خوب شده» چنلای رپی رو به دوران اوجشون برگردونیم.
#MFGA
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82456" target="_blank">📅 14:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82455">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQZTTZGqF_SUQKNicg8Owu_Df8ZqMDicilb_xs54m2AXbMzJ0xG-wluLy46mcd03Ynbt1dU7P3zgy3I6GDHpeyRIm_rGaKURdZOZ8NGnwggZjyYW38nAxQ280rrPSNOYaQDvJqtDUwMERNJGUip0N4VHqduwN2yInepUQKy_7t2UBmtCs-jzKlnhqmI1CIjpZdl_B_jE8v89df_X77ZCVqcIkjRw0IBrrzlkN37kAQkRoZPNqLM7sWQ6pXttfrZK2EVMIQVV2xcNkSIvbwQ1HtTCiCBj42EQiekFhBrZJrLh4ABU2z5xticjsHnmmLWBopDxJKXFvz_j0TfGcLHteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مرحله‌ای از رپفارسی هستیم که خود رپرای مملکت به یه همچین فلاکتی افتادن بعد یه سریا جدی زیر کامنتای این چنل درخواست محتوای ۱۰۰ درصد رپی دارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82455" target="_blank">📅 14:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82454">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFyPjA1BNEoiLVVBfXv_FYNtKP_e0CDQ6c-8wYz-IFPY3aaUFtgzRlK_7KYEXfv96iT8sXQDZN2q-ki4q4gQmoq9xsHuYmHm3foNgDZ1nhO-joppuYaXAvDS-I9gltrT69BKFDvt9OF9yfGVcQ3JBt5dh5D9XBPqOXxdxEdQTbr_p9pRT1bc8KIQM0e3dTwhJQROZNjCTxUb7g-B6WhBG0HMlyrSm2fl0iMQt1QMeSuUx7oGrBSdHP2uhEfGDEVbU6tT_06gv1qxotb2R9o51TDVXKLqDwKCziOqFvXJW4ErqkPNmTs0Px67a2011-m51waHWCx6af97nK-O1GJJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خو کصخلا چون عقایدش کیریه دلیل نمیشه هنر طرفم زیر سوال ببرید که.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82454" target="_blank">📅 12:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82453">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اسطوره تاکتیک های ناشناخته ژنرال محسن گواردیولا: با ادامه محاصره دریایی، ممکن است از پیمان منع سلاح های هسته‌ای خارج شویم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82453" target="_blank">📅 12:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82451">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTNaN-JZZ4XxZupJplujrBLi3cLA4qk2X1Hse51qxyy87Tq-satPYXKWgibRAjqWoWyWFug8jsAdilbh18Ox0eSnWBG2q7CjigvFXI4vmXBGRMz5FfoGscz9Ri2SvlGiooWxYXngf75FF4iOYjEGI3WYFT4zALjLKTZ9Wrg6yrqyWDyvX5auviIhdH0CLNiC38lWv3RbzNyiK9_llmQh5kjGfkpuJaXcm6ZweKUoZszb-KOuBRP_O9bGSgAorjepLVi_tterIU_k98tl8ckuvKka8uzPCaE5a81xXqSNy71F94Q25yAxUfR5j8DJIQ8vEc7tu_wUovPZWrF2yCZ4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a203398b.mp4?token=HrWyImfmtj4Jnq0fi2etV7vDzuOF_2HcFnWqP1SM4xQx-uHwl0DNDT8o_d9zhritxXhw-n2TADfy9JyEWBsIrLWiUhsR4oCQjesKJJdXZPURm6PypbOm-qxcqsbdxCEXhmAI411pjYhj3IN10hWw5Lta_aJEFoVgNQ2Xpn_TTR3tKuJKd8uOJ2qfIZhK7k6BjymQxrpKMhX1DpnW7UkpkLWeCjvUg8o47rOGdSdVS-JcpeeDG15xukGfE0al02c6HRezHYgs8hecTimrxv9Ibn0aQCA5x-8fO_mC7jFHt6p7t9QbJtu5WnjW1By4CV1-Mh-qglEB7MfAsGVZip-nEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a203398b.mp4?token=HrWyImfmtj4Jnq0fi2etV7vDzuOF_2HcFnWqP1SM4xQx-uHwl0DNDT8o_d9zhritxXhw-n2TADfy9JyEWBsIrLWiUhsR4oCQjesKJJdXZPURm6PypbOm-qxcqsbdxCEXhmAI411pjYhj3IN10hWw5Lta_aJEFoVgNQ2Xpn_TTR3tKuJKd8uOJ2qfIZhK7k6BjymQxrpKMhX1DpnW7UkpkLWeCjvUg8o47rOGdSdVS-JcpeeDG15xukGfE0al02c6HRezHYgs8hecTimrxv9Ibn0aQCA5x-8fO_mC7jFHt6p7t9QbJtu5WnjW1By4CV1-Mh-qglEB7MfAsGVZip-nEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مینا نامداری با حجاب رفته تو یه برنامه داخلی و مصاحبه کرده
تو یه قسمتشم داره میگه پوتک بهم پول داد که آلبومشو هایپ کنم، اینم واکنش پوتک به این حرفاشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82451" target="_blank">📅 11:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82450">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f612890d7.mp4?token=kxOvUuPLwBeET1s-HcGvwxfLNJmOQYwf1TEUncXwml9lV7cai2neqskEgq6v2TRjTn0aur6ebv1wyvxrdP1IaHmCtR6b9QHVkf_yfUVl6izjOWvt87XLDH6SfiOx3KjWOZIf_UZC7J77X48zx7pzT5Xa6U1hPj9E8NQMpK4XnE6JBsh17l1SwcdxMbFyqfwpBWt290nFbT6_v9KHkcx9QbwId36JiJ86rS1XnRAyjhBrR2TkGoax9jf8CVwiEInyIpw4yCziUojauA13w1r9MXOGcGssssQ9C-Fjfc9ctDbVEZy6jTthOUz-sma2NcLN91uoS4a6czroCARfbMoEqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f612890d7.mp4?token=kxOvUuPLwBeET1s-HcGvwxfLNJmOQYwf1TEUncXwml9lV7cai2neqskEgq6v2TRjTn0aur6ebv1wyvxrdP1IaHmCtR6b9QHVkf_yfUVl6izjOWvt87XLDH6SfiOx3KjWOZIf_UZC7J77X48zx7pzT5Xa6U1hPj9E8NQMpK4XnE6JBsh17l1SwcdxMbFyqfwpBWt290nFbT6_v9KHkcx9QbwId36JiJ86rS1XnRAyjhBrR2TkGoax9jf8CVwiEInyIpw4yCziUojauA13w1r9MXOGcGssssQ9C-Fjfc9ctDbVEZy6jTthOUz-sma2NcLN91uoS4a6czroCARfbMoEqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی اتوبان بابایی تهران، یه پسر داشت با پژو پارس لایی میکشید، که این شکلی بگا رفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82450" target="_blank">📅 11:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82449">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bde28cd1.mp4?token=Hei7TRjC1lHZHGuZD_GZ3bqRNCr-xQVMXBthZjAF-eDay9ax72usfZx5NJQaAqcAE9Mqon1l86o2I6-DG10bEDBpUHrfUpXUN3qxmivXErfMFD2ZD0rUG0WNbWzNNatz_JdtRC-DOWoHwD6JTDn9nuHwypF9DcfX4jZIQRVOG52gPRPLCZLIMFXwG3cb09xzm00DL3qwbQ_XNslTHsXU6pNdh-SYK88_8CXwe8oAq7NEKaGifTnqJdodG1TVctM6orwPs55JodMuo8f6K9DvA8ngdx_RJPRJh5oMFrO4ydmedKQnI6PlPegqrKSQoGh_1NeNptl-E7mhHaexOxU_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bde28cd1.mp4?token=Hei7TRjC1lHZHGuZD_GZ3bqRNCr-xQVMXBthZjAF-eDay9ax72usfZx5NJQaAqcAE9Mqon1l86o2I6-DG10bEDBpUHrfUpXUN3qxmivXErfMFD2ZD0rUG0WNbWzNNatz_JdtRC-DOWoHwD6JTDn9nuHwypF9DcfX4jZIQRVOG52gPRPLCZLIMFXwG3cb09xzm00DL3qwbQ_XNslTHsXU6pNdh-SYK88_8CXwe8oAq7NEKaGifTnqJdodG1TVctM6orwPs55JodMuo8f6K9DvA8ngdx_RJPRJh5oMFrO4ydmedKQnI6PlPegqrKSQoGh_1NeNptl-E7mhHaexOxU_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هندی‌ها به کامیون‌هایی که گمان می‌کنند حامل گوشت گاو است
ده‌ها راننده کامیون تاکنون جان باخته‌اند
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82449" target="_blank">📅 10:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82447">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2eddcce9.mp4?token=M6_cUIFJD_JjaN-_ieaxUbUdBqelB1DtyQmBxuwkytajpo7KpwcJ2Ct8HVWN3YziAgbU7lJEQpJk1rj8kLYVaBubyaYqeR3rHehOM9eDJ7md67zo9zJZdhMMCClQwNF5SKn19KbxDGxJabSqeuLqpOjbj84s7JxVrM7tMvPXzxEhoRcbxT9PctudABIhLpx_LP6h1CQ3DL0C1P-UHk26Jr9VL7Q7dcU9psE3fwsPfuvXU3CTiwOl5gpwzuD80gzOPnRxieLlcq_YTMCPwkbuzFr-0D1D7axI1e6uVIk9eympQG-bgTOmM4AfKz4rg8FeHn7lf7oGRTIAE7WADocp8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2eddcce9.mp4?token=M6_cUIFJD_JjaN-_ieaxUbUdBqelB1DtyQmBxuwkytajpo7KpwcJ2Ct8HVWN3YziAgbU7lJEQpJk1rj8kLYVaBubyaYqeR3rHehOM9eDJ7md67zo9zJZdhMMCClQwNF5SKn19KbxDGxJabSqeuLqpOjbj84s7JxVrM7tMvPXzxEhoRcbxT9PctudABIhLpx_LP6h1CQ3DL0C1P-UHk26Jr9VL7Q7dcU9psE3fwsPfuvXU3CTiwOl5gpwzuD80gzOPnRxieLlcq_YTMCPwkbuzFr-0D1D7axI1e6uVIk9eympQG-bgTOmM4AfKz4rg8FeHn7lf7oGRTIAE7WADocp8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوید محمدزاده داره تمرین میکنه اعزام شه فلسطین.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82447" target="_blank">📅 10:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82446">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این کصشرایی که عرشیاس و چارتا پاپ خون شبیه‌ به اون میخونن رو میبینم به رپفارسی امیدوار میشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82446" target="_blank">📅 01:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82445">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAKs2zZQqbdIQ2AEHBpLqYYEOkvRFNonsc_T_WZQOPzb_Mbx3AKrk7BXJ2PfJpEM0X8oILL3ofFSgbNJ_RTo1rhyhu8HYsHi-zpTtHuW28GPZZfRlqtSCxrkE5ALDtwfh0rGoBV8ObKCftY44SdYKgXpBy7esiN6EAFZS5v-tDEa3dMDG4jdkctXHNHDRAkJPVLcg59d3ZJVJA3giTGm7-0rfPK0WpYjLdBOwuI2HnuTagTZSYasF2jeU-9BE6t9y4YFMS0qPgbquc4GzHWVli3KPni5l-8ALbZ9EXf4-4jYJtdJCEgqsVM-SMK51m4GdHsJ0zT_j267p26yVW3lCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دوتا بدبخت رو نیمکت آرسنال تلف شدن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82445" target="_blank">📅 23:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از ترند امشب جا نمونیم
صدای انفجار در امیرآباد، تهران
احتمالاً فعالیت پدافند هوایی
مرکز تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82444" target="_blank">📅 23:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82443">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTojcePHzX17bdtrGfu1Fo3c6hOeWNP7dbkuFEYa7UAPiwXH9xfe0s0pU0tBcClL7ajeNOoPZZAY80ixZGUXITzj19CfG2O6bB5kFv-80of-muLxPshn9pALtTrqmO8polETJCGyT_JfIHFHGThrJZlS0kD8Kt4PilDqKU2XVbqr44YyUPT-GeExwQV33oofwikicxl-LbqnUHOjzMsqYKngmCulolDye60CLj9bMAs_W2HIqGF_ymTWJkQqDy6mkUMvkBBbVKzlN7uyEWDIh_d9GTTv37ev5_6fnifDojv1O-8iUf-wvTUDimBpx7V1GXkIOth57lhX1J1MPpc7wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زور نزن مشتی جام جهانی تموم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82443" target="_blank">📅 22:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82442">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEyagZKJ00G8sMzHwfHaMM87KXvrHXiOuHA78KDRciM_jfk8qaNrvIsAWvRyhvyQIcuT8IdnPfvawV_2wjsf6UFqErBp329nCVEwevdd8-no4Hv_3XBDQsYc7aODmrDZO7FamwN_Cvs_dDt-1CSHfVPMOQdmBLQwwpwgwxPopNIerIbOxpXg_uLE56hU-mD0mFW1-y-hpDUbkSLiLN0uPHHY0WCmah0MDrUSMSLCRX-OJH7bX9XQJMCjLrStOQkFEi_b_MnbaSXIBWJbuBzK1mxLVtyYWD1gxJMZPgbyooPtJZbJEzz0XDArHBgQZB9r4ehvO4bH0tk-8jrfCCXnIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخی، قانون اجازه نمیده کلاغ نگه داری؟
🥺
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82442" target="_blank">📅 22:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN1iPdWJezWhH09DsqLNQsj7rMMF_0TLSmrPqlT_gRmjSb6Mgped8F2cR-oxBdzfMVAvefmoKz16MOogu_mZaqPUH57VeeaGHVGjnBMYiFdmccnqH-UXTVcHJkGBudVexftdKzwvDv3eWfSSW0mGl4FOSQK_ILUAa9G-MSBcFr6nwXbO2241LnpLSBhgkHoqgNEqPw0Gvl_5MUqNUlxXhdwcvvyI_ksw34qrl3FSelg8UsmGqa-1eUySHGTngkDPRnblo2P63jDtIA-NG-7xi8qolfAWBHECm9wlnluBZwPRkf7wKFYmp0CkuRTm8iDfLcHw1Z4-6z-Jm0iYf7V57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82441" target="_blank">📅 21:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82440">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej4QP5SNPscEXlumLHHpa4p8TO3QwYL2xT9KCbLQ0DyJVBuRViubM-BVjXXzZLD0T2pN_UpMmsGjEaVXHN5zSa8uz2BHOzu33WXXzfHgTcuexEKhMDfTJLRbsTsSLz8O7FM2c4iOO6Z5eDytbbir-ighIOVSGivn6vAPi2vkh0u5mQh8l2Qj80UUWIswfk5_rh2BGn5qvUsEq6NhCKnbCwYbz1Feog1Uw29lqhVLvkLZviDz7UwABQZruE3Bopd203x5G7VSjIw4VX1Nz00uLk5kSMrWFGd0GgV2VfJbund_c4xbpOpE0W623vyarIoafInbytHEkSqndAkWmPMXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی این همه واسه پوری کیر گوزیدی که تهش با مجهول کار کنی، دسخووووش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82440" target="_blank">📅 21:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82439">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مثل اینکه یه تیم خلاق و با تجربه یه چیزی شبیه پورتال و مارکت ساخته که میتونید ازش گیفت nft با پرداخت ریالی بخرین استارز و پرمیوم هم داره
ایدیش
@premium_grams_bot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82439" target="_blank">📅 20:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82438">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ایده ی فیت پیشرو با سارن رو کی داد اولین نفر پیداش کنید واسم</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82438" target="_blank">📅 20:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82437">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9p83fELd8gmcrzfbBc8y51JPEp4orA6aWjZdUC7P4-RSXqfiPbUIiD5b97M12ZyDM0DLkDPAf6DlJNo-psDnVaPi6-XzZoWacxJyMDYIUs_3WgN5JYqC3DX-GCyHWHd639TLDQ0g0_3oEGVN4yadSd16CmCRjMIiVslpfYLfQAaNuSAaeSiivym89TgmzuNRbTVmNsvPRkphT48VxXAGE0hwFGZtyptMjWbjo5fvg6evCflp0MyF0TYA8GEllWG1yWAHq0qa-AngPDK8HKux2pEeqvn5kfcywwAJJ57dIZJdqpV_4CYFo2Esj9rxEVRffEjjzPOZdqakDs25AAf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید این دو تا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82437" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82436">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قالیباف:
ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی و رشد اقتصادی نداشته باشیم، دوام نمی‌آوریم
امنیت و اقتصاد لازم و ملزوم یکدیگر هستند؛ اگر امنیت را برقرار کنیم و تداومش را با اقتصاد پیش نبریم پایدار نخواهد بود
ما به عنوان یک رزمنده، بیش از آنهایی که حرف از صلح می‌زنند، قدر صلح را می‌دانیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82436" target="_blank">📅 19:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82434">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkToVCmWKgLoVtWlfKKgjZRaj0njhraC7p2JDNOSmsUwbn7OIvMpIdhBLIxPj0IKPrhXEedRh3sd75ZQeXP-bSmBjB03V9AesnBdrqY6bx3pqrsuBfufXQUoavpcyMUj4UcWLG8qpTUwjfu8g2-nurVOtKkyOo60ry3gCyf7tRn7PaBLe-gpPOkd8jEF3Fq2vGMpl1OW9-VaGkdjdIQ01Wo5tshDkbSZgLSRYryRhsc5LYQIDqpv964u-N4g8Ss7Kbz4e8SnK713bws767etN3NQq2-7_tnJYBo1U3p-cDRveADB2ItS0H4pgz390PtyoUknEdum-OJVeUArksgkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82434" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82433">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یکی راکستار رو هک کرده و داره تهدیدشون میکنه که یه ویدیو میدم بالا تا مرحله آخر بازی اسپویل شه
تا الان هم چندتا ویدیو از بازی بیرون داده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82433" target="_blank">📅 17:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0f2i7B_RIwEZ7ErPTUHJNuLAtc4Xcx1kC93LJZZMq6Xk7O5hiiRYl9Rd0s9C8qz5_geACbMf8ca8qxUpQFuj56pRq24yNn0pgZmywBJAy21CpuLa1Ge9eZbkfXFFD2VQ94QozrJjvbItootO47WUrt-po35QQyyiW_d6knBb-AO4EYoRgSvMo-U7GMUp49rYrNPmEwF0nviqtNEFLpHvZetxydbbnv3wFf3Le_G1swvxlLX6TPSi5PCWfeiA-ZnYdTzsEqwJYpL5vnPZzb31jxOxS1WHTeydd0sQgXHBH1ZzWIyAuHqTHA82mpHa9i_O3pXgmzhAFNIvWQgYJcH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRYOdZHz_7RDOxXsCzbnvKhtehfETXCbno0bX906C1P0h54xfkwQEzbYp4x85tRTYpYrdhl_DLpp8T1D7GdNxFt3s0KImvV-9G9Dwu5ceLF2bN66YTsW3RAVBoG6XtrGh0-cqnII_QLGhUzgR6ugrjgsuy2Gz3vne60r3hOHPURcJf40CtKfTb4bFNjBOQIg4EWkthikvkvim6EjEDFA9jBzkHGnspf1bhVnvtViiGPOedTll7dV4PWza-fHjW8bqEnNi65005TloJhMFDAxSuiDJI-9tvNRoWZX98FQzIlRcfQZaHK_fS0Sobe5omcYBG89KHb-gR6H82pMd5F8TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز عقاب نیروهوایی ایران، امیرسرتیپ مصطفی روستایی در گذشت
وی خلبان F-14 و F-4 بود و در جنگ موفق شد ۵ جنگنده بعثی را ساقط کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82431" target="_blank">📅 17:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82429">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_w_uD0QQ3l6rwOpLJL62UtRNAPJqXbPF8I7vIcp_Tef1ZtP6Ypt8mGM_euJHGFqwWO8YFATYdLiQmpxfrfBdztlEIcHHTBv-mtYD--F_0edaefTWRIctpLJC_AurDNEynpw_fPm7vcGfCWvA1tnlV6W-L8Ak4OwYBg98UfgNELs18zIaeOUbS27CepTXeyRGMXoAgPh-NnlI6Miyp9B-V5EDjw07YGNSeOCLbgvdSYzTsiHhvh1ISQAf_jlf8unNjpG7cS-9bj6empmz9NL8KwjVGvIF-ia8dcn5kBZO85KNnwFf5x4inu8sU3ys641ndEWRjX3LqRtvbhFlsG89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالا مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82429" target="_blank">📅 17:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82428">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82428" target="_blank">📅 17:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82427">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b51c8c227.mp4?token=D-ncq3L-Tzey0bo0E6-eB3hTTUZzxpi3AF_NH9Y2SwwZPe_NZyn5eJV2gBjIn4ZkCwpIEheC238I8GoC3Hz9RUY3_0nXZ0dJbh447tDLwB5EemSLIKfZwlwbKyzMqB5jp-meJkta79RskKvlpQlkW3vDnVB99SyMWB1PmPolSaMgxhd8b_lnppZvd-NqDP13lDhcQef4KjTYGlqVsJnf4zRJrQLY2dmoPVL2gvlMFIWGNENtqxfaFL_ei1hWORdMivp4BWAwN0ZukLe2ilBloiCS3yv5SMKPJXH8Q1z9fGWNIwR2htQxUbovI9OQ3VlvGuhBZINaAb3f_v-F0jCdxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b51c8c227.mp4?token=D-ncq3L-Tzey0bo0E6-eB3hTTUZzxpi3AF_NH9Y2SwwZPe_NZyn5eJV2gBjIn4ZkCwpIEheC238I8GoC3Hz9RUY3_0nXZ0dJbh447tDLwB5EemSLIKfZwlwbKyzMqB5jp-meJkta79RskKvlpQlkW3vDnVB99SyMWB1PmPolSaMgxhd8b_lnppZvd-NqDP13lDhcQef4KjTYGlqVsJnf4zRJrQLY2dmoPVL2gvlMFIWGNENtqxfaFL_ei1hWORdMivp4BWAwN0ZukLe2ilBloiCS3yv5SMKPJXH8Q1z9fGWNIwR2htQxUbovI9OQ3VlvGuhBZINaAb3f_v-F0jCdxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشبختانه خبر رسید که عبدلله امروز یکم ریده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82427" target="_blank">📅 16:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
دسخوووووش
باشگاه خبرنگاران جوان: مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین تولیدی این پالایشگاه رو تأیید کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82426" target="_blank">📅 16:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZimTC6de2FLgnvT_7jm5mY1hBOF4J7Jma-5QI8YJ9Nq2vXEiQLyUl4Dm23PdeY3FEbcQ6ACpQ78dL0qd-EDsWy4mN9AZWRzOA8ItfpFZVq1oipK7FAVSJfWoG4NHuR9F1rktrRGzoleAIe5pQOlhfO-8HL_9SJpUmHCjDHyP43I6XmJlXiqlgHZLUyluqSTS3_c7KvOgbIHJqH62Gl3t2eXj9FEMSnKmd_O0zJpszX6a0Mh0Aoz-rY7cS7OYiMr6al7cwBjqrMGLnOIKqB2djSHiQoDVElm0FqR4tV8EAI3ON9xItFVrqLmvVwPYhrfGjEj9i1ckfZlLk9EdE8h2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کدوم رپر میشه ربطش داد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82425" target="_blank">📅 15:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پزشکیان : جنگ باید در یه زمانی بلاخره به پایان برسه، بهتره امروز که در قدرت و عزت هستیم و تمام دنیا باور دارن که ما توی این جنگ پیروز شدیم و آمریکا در دنیا منفوره، به جنگ پایان بدیم
پ.ن:
😭
😭
😭
😭
😭
😭
😭
😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82424" target="_blank">📅 15:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7wsBV1ZEr1re6Q4DDeUhXqO81-CySLF87poVzv9pMAt791_DMS3_NNhUrB9WH0aHbzwpzSlDgzRkpjhbqWSlLPB7dKG_FWIPSZ3D5r8K1LvYfVoeMQVlKPhwYbFGsDDx8pL12qaafIMX903ftLFk-xNpX6HQvwq_-KA2OlVHuH6gG3FM_Byeza96kpsQeCKJoDtMZq636ibfGGMio_8y5OawN4XaLKaPIB_KIkWzK85IcGcf--MXmaP4G60ZRXnHYZXFV8shw1Steo--uuWxN2lJY5LwQIRTTF_9ZcYgw3KhnKGWmj30YTwWPYfV3B-D0MseGkIhv5navyEgUDlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82423" target="_blank">📅 14:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کنکورو چطور دادید؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82422" target="_blank">📅 14:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR2B9HQ0XhUtUxsYOq1gTO-hwrclLl3G-uRrSL0vxFmVRPR-tz7LbtEjuJTgOUYkZvIihTJoBfurM0eVqkwywGg6Qbwy7fbkRQpmjSX0DlvAPdmQTYx0DXeqYmPmNG4VKiBJ_xUR7LaUXGnGaQq0Pdi65pw8mN-QbqYggyNCOPTM7mCcQQUKEU7QPtiPC2kINtw2nbRgmeC8yQh9fUDgs0DpudmhkbvRECWFfInFK9naSEBxYz1icasIWAHz5qh_YtjD_puafnG09ixyJ1aXjjVw_kxCWjeSjERGH5btDiYeHT2JTBi2PzC5Mc4-KVLaDtIGFnUu_juzfdqpaRcEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پیشرو و سارن به نام Mirrors منتشر شد(لیک)
Download
(حمایت)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82421" target="_blank">📅 13:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC8d81qeArBb6oiuBCGdC76hmJeTHXdnhGnS3O3dKKQm_VHDsgWAaFeDhn__Xd9RxsIaxk44WPU5JddlceGPkNPi9gW9lhzTYnzfz4cTMYsKT-8jFI8J1P38zxQhqgzKsr4AIwE0ROTDfKq5vn5LzRd__Qko-g7cQ6c-FpEGWeYWfDLX_kxiAZK2xE7gV22Q54FaZNcN3BA3HKWDO0stmx0Bsyoq-y8Z7L6Yh4lkwOqUV0U3yhBFe-nN-UgOlAoKMQqL1Bn270gNHscQzP7hyVCj6CV5vvpG7sh9xVfuWdwQw5uHW8Jw5HtpJSZZ4fgWukT767IDmeI9RV5p1GdlrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من تست کردم مثل یویو کش اومد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82420" target="_blank">📅 13:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">عربستان اینترنت یکی از استان‌های یمن رو قطع کرده
حالا تسنیم اومده نوشته اقدام ضد انسانی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82419" target="_blank">📅 12:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=TSqxsBJpMPwoQQIOoK4Uik59610lB32HjbQUsh3hdw1BxqOo_J-V4uRSqJw6oC3-mtNlQT4pzE50O9K5BmQQySR7qT9ufY2-LrpbwxZ_G8U_5gKkKxD98JCOrAYng2wdijuEDEZHAVmGjAa51XaanvaKiEfjCDJ-TyhNMXMNKtRgCfYkugx-l7-4HhDnqdAhYu8wWahf1tGg4mjVlGfwzklPFP5yq7Y27R-rkxTnmAu-iKCdPcmXdfgr-pwgMXUINqVD21VAEYSG0Lfi0Yp2QNKCXtKshuDgiSeftTUR0vKYmE-LV4vs6KW5u_Ko6mptx4LC5epL_GBaLlz0Vi4kGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee66c3b75.mp4?token=TSqxsBJpMPwoQQIOoK4Uik59610lB32HjbQUsh3hdw1BxqOo_J-V4uRSqJw6oC3-mtNlQT4pzE50O9K5BmQQySR7qT9ufY2-LrpbwxZ_G8U_5gKkKxD98JCOrAYng2wdijuEDEZHAVmGjAa51XaanvaKiEfjCDJ-TyhNMXMNKtRgCfYkugx-l7-4HhDnqdAhYu8wWahf1tGg4mjVlGfwzklPFP5yq7Y27R-rkxTnmAu-iKCdPcmXdfgr-pwgMXUINqVD21VAEYSG0Lfi0Yp2QNKCXtKshuDgiSeftTUR0vKYmE-LV4vs6KW5u_Ko6mptx4LC5epL_GBaLlz0Vi4kGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسره با دوست دخترش قهر کرده، دوست دخترش هم برای اینکه از دلش در بیاره براش بنز خریده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82418" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فنای پیشرو جان جدتون دست از سر این سامان ویلسون بردارید، از وقتی یادم میاد هی داره تو چنلش میگه فنای پیشرو بیکارن علافن بدبختن هی به من زنگ میزنن مزاحم میشن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82417" target="_blank">📅 11:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f89bbbdd.mp4?token=Z7AWGZ3QWSmJICUmTSKmrfaBd5H8hNDoCRqMey2d2i4LnUL7FYfh2xE1YwQIGgy1FxzKqy-kjsbi4H0iIdrwAkOEP8BApb2jKPSFOZv-I9Er8wEAe9lYRPfBf3e6kzuZMF31qDl5j5CiKd4414xnMlQa0hqc2yynRCePIa3_h6Ah2DA5XQJ1s3MTTFgRIStoza99693o2BZBg49j8DGozS1vxSb1mt0EBZEoddp5G3VkjlfmymsEIWOoV50ccatCYV4FgqzpSvGs5DyENPFBA3CPid2Ubo0BBV_Iye77yFu2MsxC_aIhcHNDnkuZ4cHsSv48XL-7pgRJWr7-qh29kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f89bbbdd.mp4?token=Z7AWGZ3QWSmJICUmTSKmrfaBd5H8hNDoCRqMey2d2i4LnUL7FYfh2xE1YwQIGgy1FxzKqy-kjsbi4H0iIdrwAkOEP8BApb2jKPSFOZv-I9Er8wEAe9lYRPfBf3e6kzuZMF31qDl5j5CiKd4414xnMlQa0hqc2yynRCePIa3_h6Ah2DA5XQJ1s3MTTFgRIStoza99693o2BZBg49j8DGozS1vxSb1mt0EBZEoddp5G3VkjlfmymsEIWOoV50ccatCYV4FgqzpSvGs5DyENPFBA3CPid2Ubo0BBV_Iye77yFu2MsxC_aIhcHNDnkuZ4cHsSv48XL-7pgRJWr7-qh29kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخت و پز
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82416" target="_blank">📅 10:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0g-ttSrAM7OIF67RbpDK_XkKJ-20kaX2CCcNgTCnkBd-8A9teD-IQAQxGQbi3oYfDQaHPNqEwL39K578pgCYEZM06cqE0MiJVI_ezWzfAGupHJb6lt6zEWfYXfQNDM-nEYBpZnYu-d5CB5rKehCkrKXD42GlrGZxBD1u6zv4vOU6e0y06PJanlBJg5aB-D-WjETZx4gwkzgRhncHGbiuXgYUj18C2wGaKuJOkcw2iMBlO5iuwv2rd5Iclv-hpUaS9ZVXWiPqI44F-txk_lEG0GmicydcFRE0rkTiD6Lt1A527OW8t91kBI93b6-fusaHb5_egyap2wnaMPXijPdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید آرتا و سمی لو به نام Azizam منتشر شد
🟢
Spotify
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82415" target="_blank">📅 10:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82413">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d570e6ef4.mp4?token=EMzyMWrAKFNxYKYoxN2u6XV7t4dKO1S-dHwJ0LXMv3N1W0sNwZ9CYuLOEpmuoX30b2dURnKz3Z6sI_nOm962yvJj_zAC7y3SeFnBnSP_88D-EGnR21bFt7JhynUzsfMcAoempvx_o3oBeTj-z1fwzLWmJ6kbomGkSTq3WgIktDJ6rMiTMemZaaMBc5rC_DuVYUdYdIP9f9V7gwmcRP7rJIOsrIuw7Dm0wQwbrwMtsV11XGMnGdHIEriHaR2JPzAA-sfTARaukn6hYKCEC-ABxAVmThVl2by-Ki5NdywE0oD2AFJ7W4Pbrlf7r5F5-Pdnrm1jIu3CT57XTih8pvkhcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d570e6ef4.mp4?token=EMzyMWrAKFNxYKYoxN2u6XV7t4dKO1S-dHwJ0LXMv3N1W0sNwZ9CYuLOEpmuoX30b2dURnKz3Z6sI_nOm962yvJj_zAC7y3SeFnBnSP_88D-EGnR21bFt7JhynUzsfMcAoempvx_o3oBeTj-z1fwzLWmJ6kbomGkSTq3WgIktDJ6rMiTMemZaaMBc5rC_DuVYUdYdIP9f9V7gwmcRP7rJIOsrIuw7Dm0wQwbrwMtsV11XGMnGdHIEriHaR2JPzAA-sfTARaukn6hYKCEC-ABxAVmThVl2by-Ki5NdywE0oD2AFJ7W4Pbrlf7r5F5-Pdnrm1jIu3CT57XTih8pvkhcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این لحظه به بعد کیرم تو استقلال، ملوان عشق.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82413" target="_blank">📅 09:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82412">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCkP0IjC2uMw38V7guwqc06YfP46Hu7WI_9JOGGQZIg0XnGAt9E1RL4z9KmoCAaVP76FSvFv3HwgeRvB9Pp765j3MMjE3vHi0rSLlIz96GgYKLAkWzfVPy1jSsB9UfzC8Ulnqx0Zdqyax0wmWOOCRj_zSUolHuvSczHpeTjQPEue8E_R2vFR5O4fmjMxaVFfZ4GUE5D9JtgOo3X9L0-MOSNaHWgIfw5_kqyUM9plrM1X75dLo0N4fdr-rqRabHQ6Et2ZhigkhnmfchXmtNx2Y10gjpC-sfj1hRCsXEpGFDOBdmJipLHIGMWWT9_FaTJi0ucQiHwI90u_pmu5SET1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارسا یکم بی ادب بود ولی بیس حرفش درست بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82412" target="_blank">📅 09:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82411">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atvzqkFlIuLcv6CsNOrQdkFpyBM0gH_FISkd-QO9iHHrBycPCQzktGLWNrdh2GrR4_fGkL1K4q73FLQ_L-5K6zUASeZcUd_gZP7wCGLYTOdBbJpTTfl_17BQqo5GvrGgYi3x3hooWQRgSpyJBCugUhchWyCHcSB9EaxcgSSf8CdK8aN97_ZQso0JjBhtLc-mFGwWB_tCJ5EF7NyTlw0hPMyhRC46PfnpBrSxOi56kPz7ID0jVhHPBMEmHWV7aoWVVrefGURsnTxyP3joqejGaBttAcmSmGv3wwcK7hMTnLdjg1QAZtbR4hSbpECT5x8gj0aXgrlelDUOidTHNwLKUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
💙
با این وضعیت تورم و گرونی دیگه سخت میشه کیت استقلال خرید
ولی این ربات هر هفته کلی کیت استقلال هدیه میده
👇
☑️
@F00TiBot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82411" target="_blank">📅 00:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFOEOLaTc6MzQu5-OQlitQsEgefCKJA6xi5rqnvWgC1qCmr-mJ_IWFZ93TErz4OEITBLAaHB3sXwbJS8k8IdVvFR_MKTk9htXnfLJT2Sm5wWhMDVgHu3qtu1C8Ko2ckgG9HE1TtPWPxfyLhs1lpK6czCLmkPPqXlM_XtJcpzde_PCzY4K4nA_y1bLiZVPX7AKwaetNiL62JArmezAR8qlKtaNBdIjeWj3TxRj9ujhjUN9mJscB8oKYQ0zHfnd0wcxqo4c-GvGv3WWh_8RVOaoY1mw3jsU7rFRPkW7aNh4KQETbpWmzRg5yUs-ml6wulUBwIk_Wg50tXD-92ATW2P5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82410" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb91ca0a56.mp4?token=M8xxBJc495dCd68dKdcE5q1-vpNohnkr16ZBcsBlssaTKS6x-DwpJoIFZTN48BdUgdxpBZ6LCRWzl585YCs-U_HZD6dhJtvNjtMi2W62W3Bp61rf2KP6J7klNdHiH7j4zVP7zNqLKASTKlT2VOMSmx_s2QV78R07XXdikIdAShPFCVSIw-sOVMNrnbc6eguQzj4QveH6M9E17nEn86RiQfhQlv-wLhjwSgTSL9N4RnJWsZ521gkreeIHW1U0yUZ-Xxkk4BP1yJAAqeqjUbaJPFYi0NQZQrP12aGzGF7pdY5IuXjSFJOCuEIKkw8qLtmVrhUKJ8dtfVA8QJcrIIgNog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb91ca0a56.mp4?token=M8xxBJc495dCd68dKdcE5q1-vpNohnkr16ZBcsBlssaTKS6x-DwpJoIFZTN48BdUgdxpBZ6LCRWzl585YCs-U_HZD6dhJtvNjtMi2W62W3Bp61rf2KP6J7klNdHiH7j4zVP7zNqLKASTKlT2VOMSmx_s2QV78R07XXdikIdAShPFCVSIw-sOVMNrnbc6eguQzj4QveH6M9E17nEn86RiQfhQlv-wLhjwSgTSL9N4RnJWsZ521gkreeIHW1U0yUZ-Xxkk4BP1yJAAqeqjUbaJPFYi0NQZQrP12aGzGF7pdY5IuXjSFJOCuEIKkw8qLtmVrhUKJ8dtfVA8QJcrIIgNog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینو میخواستی بشنوی کصکش؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82409" target="_blank">📅 23:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82408">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNHBxxCLuVjD6klDQfPvOLmxDs2p4p61tsBSNC-9DJqa0FItFihg7S70GDmYS79rgDEgAoFtFhHzghs-LAbGIxKeLVR_WSzSt15g3T2ewL9LE80ag1HFWQHJWYmkZl6y60yn8Qutth4T6arUKNYBq_RtZkogWuENse8apEhBqp8BSLBd8FVWUn0yowjOTE6mqA7JZBrSFeMDb1vcOsEuilAiXzDpmFYftERQhK5cPMLxe0awDqGcOSRmv3SkS5YOBzJyODVbVk1Yr7mIwrmPAVB6vZJKXi-uc3fbiyTzI0bumrRFjHO9oZ5NUdBBcnXxWkCPdU4v4MVW5YBQC6zddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا برای عبدالله دعا کنید  @FuunHipHop | TemSah</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82408" target="_blank">📅 23:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82407">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پسر ایران فوق العادس
غریب آبادی، معاون وزیرخارجه:
آمریکا اسم شکست بعدیش رو «جنگ اقتصادی» گذاشته‌
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82407" target="_blank">📅 22:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82406">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b263aec1c3.mp4?token=LHREmXCtej7eN3IvzAh0G649Kc192hWyyuqGuIw_C_-EMmLvb-ZC0ITVP82foCfLC-VS7uRSMjDpAonlu0Tt9nRCDDO2PIW2dgOYHP3bjoIR1ca4RQIKSIk3PXClLH3EvSeTd3DtRHMHjfsv9L_EYiET6z7LiBhOdjmu8L8WJmu5dH4jAkVD6HCPCE71EKWTQq-2bQIeRARbj7_-orP5-elmQ0Wx7hvzqsEa2mYGf3wUOt6yyEHuyr_JAB8TdLu730M9twYMxztFtPs9TzdjyvEjTYIR-dCdxWSMjehByWOPr1yELmJT14mGcvCExssqrQ8VlxtfvZfvaXLFlqVplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b263aec1c3.mp4?token=LHREmXCtej7eN3IvzAh0G649Kc192hWyyuqGuIw_C_-EMmLvb-ZC0ITVP82foCfLC-VS7uRSMjDpAonlu0Tt9nRCDDO2PIW2dgOYHP3bjoIR1ca4RQIKSIk3PXClLH3EvSeTd3DtRHMHjfsv9L_EYiET6z7LiBhOdjmu8L8WJmu5dH4jAkVD6HCPCE71EKWTQq-2bQIeRARbj7_-orP5-elmQ0Wx7hvzqsEa2mYGf3wUOt6yyEHuyr_JAB8TdLu730M9twYMxztFtPs9TzdjyvEjTYIR-dCdxWSMjehByWOPr1yELmJT14mGcvCExssqrQ8VlxtfvZfvaXLFlqVplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید با خودتون بگید این کسشر چیه ولی این اثر هنری با ۲۰۰ دلار بودجه ساخته شده و تو بازار چین ۴ میلیون دلار فروخته
پ.ن: ممبرا نجاتمون دادن محتوا فرستادن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82406" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82405">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">محتوا با تایتل "عاقبت اعتباد" میخواید برید اجرای جدید علی گرامیو ببینید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82405" target="_blank">📅 21:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82404">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آبگوشت</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82404" target="_blank">📅 20:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82403">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آبگوشت</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82403" target="_blank">📅 20:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82402">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH47MzDbYKWYG7weiBEgz-_3BUWHjiK2rJck903tBw8keCoCsY6G1XbB1W6Z6B-XIZNK7ZGLt8qbsxCbgA_bFGQqx-lFEnFohk2cU7V9oOg54-1mniw33_cxzD5Ac5NbtUeA08nJVtb7KYzIxpYf0wS3UhrAhKz54uXTMGDpjWBdv52a30bG8Tl9MvZ7bnIeTp7mg5prORMUukij0IlmIBhsSl097SLaLfO4hMfwY8TbKsjVkaWhzna85UwM56xMYGMVZAZwCmuGCEzocaCVJiCoTW5GPsEBK2UgqP2vEnJdyLaviIHiAhef_JBFZxAepbCygSC8WYGF_Wrkew590g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود ببخشید یادم رفت وجود داری
موزیک جدید ویناک به نام باور کن منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82402" target="_blank">📅 20:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82401">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بسنت، وزیر خزانه داری آمریکا:
ما قرار است سخت‌ترین تحریم‌ها را در تاریخ اعمال کنیم، و من به شما می‌گویم، این کارساز خواهد بود.
این روش قبلاً در ونزوئلا زمانی که ما محاصره اقتصادی را اعمال کردیم، موثر بود. در حال حاضر در کوبا نیز در حال کار است، و در ایران نیز موثر خواهد بود، و ما این رژیم را سرنگون خواهیم کرد.
وزارت خارجه ایران:
اعلام تحریم‌های جدید علیه ایران از سوی آمریکا، اقدامی پیشاپیش شکست خورده است که نتیجه‌ای جز تکرار ناکامی‌های گذشته نخواهد داشت.
با در نظر داشتن تجارب ۷ دهه مقاومت همه جانبه، از همه ظرفیت‌ها برای دفع شرارت دشمن بهره می‌گیریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82401" target="_blank">📅 20:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82400">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زندگی پر از آزمونای بزرگ تر و مهم تر از کنکوره، فداسرتون که خراب کردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82400" target="_blank">📅 18:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82399">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVgOltE4OHe9Kf47y9X-NZMCkZ0X4pq_2TyIYZ9VUEyJfDFpevEEG5REY9rXpSmDMpwXcZ33fr-N95mXcXWFwSeNGQN1-m-BnN0kSvvxiqR4B4-jztm0qj83-7PBxOCnSMJNFGCV79VTUdAI3_Xfcm3uuAIeSEeqFZ0fDZZPD3R5EBYWFcCy6OZ7hmEao2jLKxan3JnNDUx0-4N6l5X4KfP1tVBM7HsE2SeD2StI9uDQg2IQjBrZUFQ0WDoaqv3zYSFXF_qZMH2D5eIgKc53wLuOuvpLbcCV4lVyP1_bmCfIgb1eyb2vG89eXGyuk8w09H-pppM1NhlFmeHK62LeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابامیخواستیم اقامت و حقوق پایه چند هزار دلاری رو ول کنیم بیایم واس ماهی ۲۰ تومن کار کنیما
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82399" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82398">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DS4RG7CqQzfSc-TbOoDYd53cvvbhzJu1QbpysWOe93oNOaaMD1gfPPq9Vmq5sEOzL53S1UriULtqj960MicwrNxR_UuoCDxAorbmn1WFfzXSTR47VrYsswDaoymDII2r4drqeVzooaUtmTvlZYbv3RFxcRojQu5g--TsvUAkKIzrF-2kwomyfmpnfpVgS8QuQsKQ0I4SwAcbUGfODUn00WlLZMGh8njv1hIXEYA2ymXlCM-rxn0JuA2YLMjx89qeNjzGKlC0xsOzRAuGSdYp0mIKo_zUTxxfdauW2o_RKWZhi79DK_VW9oQOiDLkg0TpFUkyWKQ1adutgFBrGRwsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا شما راحت باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82398" target="_blank">📅 17:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82397">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ویلسون چرا مست میکنه فاز رگنار میگیره
😂
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82397" target="_blank">📅 17:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82395">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b61995a79.mp4?token=ER5gTA1C4bumzzd1qgVdSAX17w788DfWUS6ZXLdS3Enh-KNGr1FB4lHP8S79pz7tLXrnb_dNJ8zXZvGQ0XYJPUuDTmTsdE3t2oAyc4NRJ5J8OA_6Dvp8LjFQLPYWiCDQOEfdk5f0Pa9hFX78NNzacJPM-TI_wcEge4HKwzmXywchXWm-q2T30d1xsNjIdIXOUGy_JNWFWPP2GearLcS4vpwyGzUxfDP5rtnXt8cIr17lRDBZshAw_kzaT7A5LGTqHHAf7acYujVg9xoJ82j1usNinuSW_jW4INE4mZ5ePLreE6_4nfEjzpP1M8duYyx2zBoSJ1KCbYDpTU7p_CCsOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b61995a79.mp4?token=ER5gTA1C4bumzzd1qgVdSAX17w788DfWUS6ZXLdS3Enh-KNGr1FB4lHP8S79pz7tLXrnb_dNJ8zXZvGQ0XYJPUuDTmTsdE3t2oAyc4NRJ5J8OA_6Dvp8LjFQLPYWiCDQOEfdk5f0Pa9hFX78NNzacJPM-TI_wcEge4HKwzmXywchXWm-q2T30d1xsNjIdIXOUGy_JNWFWPP2GearLcS4vpwyGzUxfDP5rtnXt8cIr17lRDBZshAw_kzaT7A5LGTqHHAf7acYujVg9xoJ82j1usNinuSW_jW4INE4mZ5ePLreE6_4nfEjzpP1M8duYyx2zBoSJ1KCbYDpTU7p_CCsOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند روزیه یه بچه گربه تو اینستا به نام عبدلله یبوست گرفته، تا عبدلله خوب نشه منم نمیرینم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82395" target="_blank">📅 16:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82393">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دلو دیگه نخون لطفا، برگرد همون دوتا۲ ات رو بازی کن(
منم دارم میرم مچ بعدیو فایند کنم
)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82393" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82392">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ8860JDsS7M0FYRJMFTjehYPhqIJYAabosDh9-9pPVp7H4i7_SiyZysln9uzUKz_XVAC9rTMGQWeKN15b-wxLp2Zu1GUAySwK9i0YfhD7LZdZTJFrvQMQ97lWgemyuP_ihy5QGoly06GaymW6cVf4aIapAGrQj38-1TziozSc52nJk6FuvKJ8aHvVHCPVdPIA9QD9kLRJjyie1G3Mg6JGlclFmXtYmIXUs3q-BKlm15gojj4vJhRyTmC97NG57jmu5bmBfXfQeR5CPW1JIzT0CWxIhIv82hkbEMDLn4_BMKGwuNyiKpx8iHe0sWrJPc2OSG9wJxKMVXDLdqiYcTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دونالد، ترکوندی دونالد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82392" target="_blank">📅 15:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82391">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چند روزیه یه بچه گربه تو اینستا به نام عبدلله یبوست گرفته، تا عبدلله خوب نشه منم نمیرینم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82391" target="_blank">📅 15:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82390">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وزیر خارجه مصر تاکید کرد که به هیچ کشوری، فارغ از اینکه کدام کشور باشد نمی‌توان اجازه داد مانع دریانوری شود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82390" target="_blank">📅 15:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82389">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بچه های کنکوری بیاید بگید ببینم تو کدوم پادگان قبول میشید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82389" target="_blank">📅 14:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82388">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP-ZLb0ijIRLZ8Rs17VM9aNJ2ui6rwq2rc6IIkIrB7fK1Dll_yyRiWjS2Liw4YSmG8oTYxSSKiAIqre6Ab3FpFOWG_oMi8O1A5VUrPbEG2uTDedaTYCNw2mgnRlXRNyQOCxgg5T0LqSEhRGlXreFcxh8p9KGkgh_6YkVWjAWIpkuK11yo1gZebBilIpQl5w4EC9V52WWO7L_AbLrjNscbZvA4GiEkIJl5LpXF__QAYByCY7bBELcRgjmbZuop6fnqk94UI6Fi4g0DJ6vkhFDObp_DSdkkYY3JC7cpZkXzpYOKCjW_XTiud_K2p4khIUx712PJPAnsBlC3OyHQGUw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار رو به جلو اگه جواب میداد دیگه کسی قد کاگانو مسخره نمیکرد اردلان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82388" target="_blank">📅 14:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82387">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=eItAVK3vsAuwvMT-66ntX5GsDXy_iK0vYKTUxOch-zWBpg3o1ctmCvJfC46rbScAJKNlYocnSizCoJZ47JrPFJapUaj6xBgZ7DJUmZa_Ni-59iQtlyD6kC3bbChoaFUy35MUpj43clVcRGs-zqNRm3P0cqRUCHSvTWCXM5EDPp6gAyIJH-S-hdmVTN1kVEIEfAAPb3CRXKQLscH435qMyw-gltD9fjkeVOfmvi1wH4KcXSa-H9f2Bb6KbaBvbv_lC5eL-YW2l7PiRM57iMEqJam_7jciMUuQBfNOGxmPhqcyzql9x1kSXfIY6NH3afTgxK24jTG5-iXx2mOJdXLAPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b2647e03.mp4?token=eItAVK3vsAuwvMT-66ntX5GsDXy_iK0vYKTUxOch-zWBpg3o1ctmCvJfC46rbScAJKNlYocnSizCoJZ47JrPFJapUaj6xBgZ7DJUmZa_Ni-59iQtlyD6kC3bbChoaFUy35MUpj43clVcRGs-zqNRm3P0cqRUCHSvTWCXM5EDPp6gAyIJH-S-hdmVTN1kVEIEfAAPb3CRXKQLscH435qMyw-gltD9fjkeVOfmvi1wH4KcXSa-H9f2Bb6KbaBvbv_lC5eL-YW2l7PiRM57iMEqJam_7jciMUuQBfNOGxmPhqcyzql9x1kSXfIY6NH3afTgxK24jTG5-iXx2mOJdXLAPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازه میفهمم احمدشاه اون زمان چرا این حرفو زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82387" target="_blank">📅 14:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82386">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جواب کنکوراتون کی میاد، کد واسه شارژ ایرانسل لازم دارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82386" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82385">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTqaCu4B4c_ug6eML9ouw0SkArGouahvrN2uy8SP4X6sd0LBtuwHUDukBhSCH6YpR07Q0xQQL0aZmLqCx_tooUeMDW6VxwcJpZGVnk1u024cnpyf3a9_2N6754m71zaEAsK7vd9lx_Kvh8H55J9vGnWL6GfApTmNPiUoqgu196EiDZcQsHQTMbJe_zEbwNCexEC68zOgOh9nUw9G7PlvKhV2SNR1q_rLBtX6mFxe0wjOWZGL9LQ4J1kXP_TV4k81WLnUzIgKwRohmxUxvTwQEu_IsOL91e5G8vMLQuguFyRBfNHkpL8CKF9yLdbL42xlHSxG1kQLWjILhJvTSDHTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی ایرانی هعی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82385" target="_blank">📅 13:59 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
