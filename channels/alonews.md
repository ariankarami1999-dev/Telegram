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
<img src="https://cdn4.telesco.pe/file/KeFNhqeTxV4U7KRpuCe5uyTrpfgEjEM5hakugEWK2nadMCT2YLemJ3hf9eN2wc9T0G-xCiihO9YvH1cJGhtf_6M8u7rJv3X-ROTMBGJAwVsbGA4wvyv2-hrdi8Vhn9V4uaTbxYze6QwxhWxjobqqmn5hdNl4ZusHCB_QNJNVCjKdUAKj8O0PlnbW17Jiopof-N7Q8ihu0CTbyQZrrBRHPx_mc-x1HYt-0tSCpnWUVlHJnscEynbsYa02qzbf9WxBbSMV3yZFyZzIUrGdG3_P_1av0OxS5-94NjCdr6Rd4dXZ0yfveZC9BAxDqtPfhaiiAyZQqmIAKYRFYQ3FQXwkfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 972K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 08:32:28</div>
<hr>

<div class="tg-post" id="msg-140863">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9012d16498.mp4?token=LL8-PJ1rprKIYHs_Z4QDK-ihjSnuQUO9sXA2yxRzgrUwj0ghOCvYeFO5Dy-FZsuvRUBPBqkbNuZjMICdB_FtHY_jKV8-RjR4YRD2LcHZRzxBog3-1vyyw6N8KSjOixJsXJIDDWKfiF8ncbgJpn2GIMt5gGM5hab2FGvx4J1VTBj4LrzBnTAbPRnF6ofQnEuXEFyi0rukqEFHhnpyk0MvxIQSV8Xwb3g9MaLwZGjQj3pGYZKYWTHX-riNzHS56Wn9Jlao2quV7cwQeJxY7BB3W3CoLxPWTUI1ArqFnD3w_3Ct0Fbez9YXwWAjh0-cpv2AQshvLY_SGb2pddwXnOZ-aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9012d16498.mp4?token=LL8-PJ1rprKIYHs_Z4QDK-ihjSnuQUO9sXA2yxRzgrUwj0ghOCvYeFO5Dy-FZsuvRUBPBqkbNuZjMICdB_FtHY_jKV8-RjR4YRD2LcHZRzxBog3-1vyyw6N8KSjOixJsXJIDDWKfiF8ncbgJpn2GIMt5gGM5hab2FGvx4J1VTBj4LrzBnTAbPRnF6ofQnEuXEFyi0rukqEFHhnpyk0MvxIQSV8Xwb3g9MaLwZGjQj3pGYZKYWTHX-riNzHS56Wn9Jlao2quV7cwQeJxY7BB3W3CoLxPWTUI1ArqFnD3w_3Ct0Fbez9YXwWAjh0-cpv2AQshvLY_SGb2pddwXnOZ-aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
جشن امشب مردم ترکیه بخاطر توافق مکه:
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/140863" target="_blank">📅 07:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140862">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feeb36b6ca.mp4?token=A3TIqQNGcozlWcSz5OAEmdyrvLaHGvivkd19klKdTxz2atuw-SstebpPsYnKKDjAanWAMzWxTFF_CfgI_ajhLLXtb-7vbVO3myp5JhZcLinxuvdKbjeGaQY4PEotZjOH5k8hYg7HuJB2D3g2WRGJYUGpAkSrIK1rXNhl95t3bs7fV681uVAr3dTHernbMQf4Z_au128ETQz8i06uFOXEfBaZwrSMLkdEkYusDrJvMJ_3sej3KgTFxtf77VEABml30D2kyUedd_7tJDRQSZwiKmOb1S5RV0xHLe66Kn9vs-69ULdXRC_30YZoPk5hLdN1LvrPVudYTSz0zK23S3JDIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feeb36b6ca.mp4?token=A3TIqQNGcozlWcSz5OAEmdyrvLaHGvivkd19klKdTxz2atuw-SstebpPsYnKKDjAanWAMzWxTFF_CfgI_ajhLLXtb-7vbVO3myp5JhZcLinxuvdKbjeGaQY4PEotZjOH5k8hYg7HuJB2D3g2WRGJYUGpAkSrIK1rXNhl95t3bs7fV681uVAr3dTHernbMQf4Z_au128ETQz8i06uFOXEfBaZwrSMLkdEkYusDrJvMJ_3sej3KgTFxtf77VEABml30D2kyUedd_7tJDRQSZwiKmOb1S5RV0xHLe66Kn9vs-69ULdXRC_30YZoPk5hLdN1LvrPVudYTSz0zK23S3JDIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طالبان کاملا جدی برده داری جنسی زنان رو قانونی اعلام کرد، از این به بعد مرد ها میتونن مثل کالا زن هارو بخرن و مثل برده جنسی ازشون استفاده کنن
این در حالیه که حضور زنان در مدارس و تحصیل همچنان ممنوعه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/140862" target="_blank">📅 07:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140861">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">💢
💢
🔥
🔥
💢
قیمت طلا و دلار فردا سه شنبه ریزشیه
👇
سایت رسمی اتحادیه طلا و جواهرات goldonliveeeee@   لحظه ای قیمت میزنه  منبع دقیق قیمت لحظه ای طلا و تتر
😀
☝️</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140861" target="_blank">📅 01:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140860">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">💢
💢
🔥
🔥
💢
قیمت طلا و دلار فردا سه شنبه ریزشیه
👇
سایت رسمی اتحادیه طلا و جواهرات
goldonliveeeee@
لحظه ای قیمت میزنه
منبع دقیق قیمت لحظه ای طلا و تتر
😀
☝️</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/140860" target="_blank">📅 01:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140859">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwjqNstYTeXd_CFqERGQ2MUQRyQtzZZkLsLLWh0ie-C4C84JVEpa92qLxVvARnN_Ya8SCOyuQF-IucrXo_B5-lAqOfylol9KQYGcOSAdM5LJXyQZvT9ws9hSlsw6-bPS78x6q45UvEPhADrHvcVDlRipEI-CUoL_PGHh5S8K74Q-vulS4qzpSEgWqsh09lqu01zwJ78_Y06xqwKHgrNyGLJPK9fbjuIkCNKMXvsj60GBaZ7MFJFcn_vdrP-XGEu5mWyYBVgPMsUJFezbTETB2La5aWpX87xMpyIsVQX8DWjENzAMROwJ5xQgjDmWx5dtsHrjvOEdQuL7PprrMSJG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی مسیر ۵۵ فروند کشتی تجاری را تغییر داده‌اند، ۲ فروند را غیرفعال کرده‌اند و به ۲ فروند دیگر صعود کرده‌اند تا از رعایت مقررات مربوط به تحریم بنادر ایران اطمینان حاصل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/140859" target="_blank">📅 01:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140858">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
فوری/ بلومبرگ:
توافق درباره تنگه هرمز اکنون دور از دسترس است؛ ایران با مذاکرات مستقیم با آمریکا مخالفت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140858" target="_blank">📅 01:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کیهان: اردوغان و شهباز شریف مثل روباه مکار و گربه نره بن سلمان را سرکیسه کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/140857" target="_blank">📅 01:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd2301599.mp4?token=IDVRJ71VJ8w5vCuNvuZXhfHcLpcgdwROwSyu0irFGzZwZTGqTH9jtR4TUQOGnIrCPQd05ywQxx_YaCt3loT5V4WqraB99xbmKaTICXfwNnpe-gnWVKvq8qIlc7TW3uICF7DCOZL9EVfNKW2hesKWUEJlEKFfUJzkykDPV2bY-vKoTqLZMWkgjPblx_7zzpP8j3U0XtdESpdnqUy1yGfxC4lqOBILdox6hpQ9a2dcAFGZ_7EUQ5mtbxGCkUW-wnnAo9Pp7nj_29ZiXfTZxpYUiRWszqpTqRr9DyTR1j9AXy4hRV7PiXq828elDj4Y65YcI5ceCO75ogUYAZONmbnvCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd2301599.mp4?token=IDVRJ71VJ8w5vCuNvuZXhfHcLpcgdwROwSyu0irFGzZwZTGqTH9jtR4TUQOGnIrCPQd05ywQxx_YaCt3loT5V4WqraB99xbmKaTICXfwNnpe-gnWVKvq8qIlc7TW3uICF7DCOZL9EVfNKW2hesKWUEJlEKFfUJzkykDPV2bY-vKoTqLZMWkgjPblx_7zzpP8j3U0XtdESpdnqUy1yGfxC4lqOBILdox6hpQ9a2dcAFGZ_7EUQ5mtbxGCkUW-wnnAo9Pp7nj_29ZiXfTZxpYUiRWszqpTqRr9DyTR1j9AXy4hRV7PiXq828elDj4Y65YcI5ceCO75ogUYAZONmbnvCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه پهپاد رو تو جنوب کشور زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/140856" target="_blank">📅 01:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efvjJmrr5e9W8xv3cKuak8De7ykH_zaatduV00rQhlPGfMv65FyKzR-YZCe8QhdA20lVmahAL2r2A6TBOu0aG5LbnCwdkBv3RHGwv08CxA8M2X15ouD2O8xpN27goeFsKH9slloDJbRNpPC_hqMUwcTwMgbOufnQUrmZhb2HNuWIJxYRVQC5nmO7V371t0raif7eboK3kFH4MJKx4fk0VjxwWuF-RqNqAitVBAzqYB8gY_l-KSMFajPSC00-NzzNg4fs8HhEcvPjCWCDX9bNM90S419xT4KB_ybkomvuwdTfxG_3dxVkFN9hZfsLdlPkfTiTA8TvNyO_qyFCSgDCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میثاقی: علی دایی در حد فوتبال اسطوره هست و الا تو سیاست و روش زندگی کاراش خیلی چیپ بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140855" target="_blank">📅 01:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU_BhTmmXvi3Ox-KSgGilveyrpwGrnm3R722BT5q_uFmomap5Z1rKWzYrda7ysp6zQIYCQqR58HRXahiuHmoUPB9cayU2vIX8htzO-YCXiZEBxR56xxWaNmmflDDu7sTTNidpnxREQsUIgQIvYjYb-NpuqBe7x3aF3R1UBvfCbHqW-AmwLRaIX_RgkL4bUnOFDMLl5LTy1kUwYONx3Ghrl_fUHYij_TR5HUjdMbW3JzTEtBmyKVmsVeNxCO7uD_ReJqDntUk51zHWCevEInOeK_G04zXXgftmEYk5xJw3aGFBlhulCexBe-XQwb-REKUbtVXiKSTqvR2O5V8tVI4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه نفتکش تو نزدیکی عمان هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/140854" target="_blank">📅 00:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">💢
این وسط فیلم مسیح علینژاد و دوس پسر سیاه پوستش منتشر شده که.........
💢
مشاهده ویدیو</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/140853" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140852">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGt83eBx34yDhn8gxiOhzYMeNEPE4su1q9ukxtnuhRWzeWYZIojk9MpKBN3GvTNkd90KgJXe_2mFTWSLObP-txxwqStHfzwKYmtv9Y5pfrW7Ly-XxzpYcl92tz_Go3_mbUweWE4soeJxxt1R3AcgkLtfDhegUwT4RVq1Egrus0TgeCi0o3DR1QTO24X9TcQx0cfonraFBkF2maG2FV0Wo_8iQLJ_RqVZT1onBjYBO8HCnaRAB3fxzLgMZ5F3u51rHrVZ7QkMHac4EJeqP8j_EQsJ2YfoCc3-vBC2HvC08uYQG2TicItRp0ym1KI4GB8DjbQThjJD0ogtcjr9fRTUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ترامپ: 51 سال رفتار نامناسب ایران!
🔴
جالب اینکه چندسال آخر شاه رو هم رفتار نامناسب میدونه!!! و فرضیه اینکه غربی‌ها تو رژیم‌ چنج دخیل بودن رو قوی میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/140852" target="_blank">📅 00:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140851">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaa90a135.mp4?token=aXDVbbqnhSyUq8nQIr7IuXut6axh1tqsDsIEBnogv01GmT3IVlgUle_0_M04zyxUNGfGAnWQMZY2S7VfRueCRUF5BLTzDUSc-82Tx0zeG-KFUFj8-o4YRQFDGiRM0MaWI-0-ZeB8qkMvq8TzfL5zkPj7ivNhvMaHfDINeX0HSuPrA7LgmRVscp_RdVBcmiyGzXwwyiR_UQsrBTbgHMhZf4XpGRWqaPRyqH4MGSyWUChDw3InpHpJ_UOteQx2ap-Omp6XJcxgl8ufEQo27Cws7ZASeKYrcq9uLquaW0_Oue3BSHGtuXTyU94qSOVY2XHPbbC_uPwMaeDhn-VtzOwcmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaa90a135.mp4?token=aXDVbbqnhSyUq8nQIr7IuXut6axh1tqsDsIEBnogv01GmT3IVlgUle_0_M04zyxUNGfGAnWQMZY2S7VfRueCRUF5BLTzDUSc-82Tx0zeG-KFUFj8-o4YRQFDGiRM0MaWI-0-ZeB8qkMvq8TzfL5zkPj7ivNhvMaHfDINeX0HSuPrA7LgmRVscp_RdVBcmiyGzXwwyiR_UQsrBTbgHMhZf4XpGRWqaPRyqH4MGSyWUChDw3InpHpJ_UOteQx2ap-Omp6XJcxgl8ufEQo27Cws7ZASeKYrcq9uLquaW0_Oue3BSHGtuXTyU94qSOVY2XHPbbC_uPwMaeDhn-VtzOwcmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این زن چادری اومده اینطوری انتقام خون «رجب زاده» رو میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/140851" target="_blank">📅 00:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140850">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pCHPVC4xnHlpv4AYQjQMTundqKjo7rqA038YV8yw6KwkEhpGezxIiXJh-d1Ug49_H7FxgfyuZJshnr5-WfgrUVBVEoDfjSvdOSEX1Yyg3u_n9BLhS1srFCVN42Z0BY-DmPFNXG79kPChRLkXmfDn7xvpHd47jEwrngUt6qY9TH--4taLmP-KfOsesBBCMonoy3kyDSe_60l5cnMxMbaTmoCSWtIu5JGi71S3rjNZ79NHNnedrrBJxbAJtjjf668PHgvWp9N4w8wVRAasuIG6YCNeMW4HLOqEfJ5mDz3wulUCGW-ymDrHDmf0cgtOuzuWpOZCF0nf_VP6QqoTELSlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/140850" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140846">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHB2HrL_Yte4v5MfiH8M7Mc7NUiRjPs6w3j-m2IButlYoF9V-ptn4NuBIsTR-Q2_39oNjzqu53VYFYajiA_5soS4koqrCmBnYUGWYgXJXg9RB5__70cIrhRGK3xGLsSg91bNvcQu3qsEjPkTholautTy2276Ft3iMXydseRjoUYBS-KFG3qpVoFM1ejujKJDgpjIgz_W9QcnxVPx0qHPKRKu0JVYzqq66JTtubGsNK9ZTYEW6r0WxZpjA2l2yqjJugUAPiAAo3dFbiZYbJO9ZFqnpbh_FoOxAyzNN32nANUpwmF-Z-JGloCqt2EOyFEkymuOg4AUaQEZknJtHRbIDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_mG3SGiZnDwvJFnyAqlXwKtI052oh7ywMxp0yulsh-9-riWn1VbI__IjHzsYngN4gLmf0Oa8v1ZHbYQ_C4BIUpV0CcvR8g14dOeK_V61zyI3VXJt1DiOiTy85A0xJcqx2OOk162yGhVOI-GiGvJ7biwEiYi9H4WDK2_1EX4p_ADtSTNU4m9yp5KNIBNKqXoX-Bex9KuAdP4pDbXmB6GkZUKlN3_bIecJI7no5ZLsAgNRDg5xkEjuG2i6rtvNNheFQhHggtXasoIjXfeg9TwBK4eOjBSCiYmiFhW1E16TNGuHS2A9B1vYoguv7axHKi5akKK66Pi0S4Zwqj66Uf1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-Wza_coCWAUIpjHtQEeaFn_EIqIpoDma7sgLFFfNBPJ8NbrczPdbnAODMbd_mTafIZEsolEVY3GvTMdwSRMsSlDczTaz342qkz55wivcB3_ShUdOJRJLKO8exVlO1YISsEwnEfBYVQf_EnPvqYK2jcnqpLE_JrkIwNr6jwrU9p_TimWtHMMT6b4SuYTnLAN2v-pkAoRKTW_gnW8BQZgClwpq-YFxlReeF_-VvvxqwtcIofUoRZt_TAAg65Muyw2_jixxSTkFa8ERLcFvFNsnNAmqbQ5CieVi-JOLeksH2PJkx7GMMjy1ZIc93Rp2u2E4ch8kKF7L2PRLpWSFpemTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یگان‌های پدافند هوایی ارمنستان با استفاده از پدافند هوایی مجید ساخت ایران که اخیراً خریداری شده و سامانه موشکی هندی رزمایش آموزشی برگزار کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/140846" target="_blank">📅 00:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140845">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
👈
اعتراض شدید کارشناس هواشناسی: هواشناسی جای ترسوندن مردم برای بیشتر دیده‌شدن نیست
‏
🔴
ماجرای ال‌نینو را جدی نگیرید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/140845" target="_blank">📅 00:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140844">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f191ecf5.mp4?token=dPFt4VxL1YEVdbNT_EpxtAQWEIJHPQy9U_sZp3uDDqcQ1GlfIrOgmjH1NgB2GqZiHbDeJq8im5DEU34lrhloXEL42wCXGVSLQ0L8dRcvGca_pFr1VCNMa_2KSOT3RRxQlDsC-rmJE3BAqjUbZHoswEeryC_H9B-zccG-Lt3bRbVWN832ymTqR4i5rPSr2bx6_kdZpBYwjnQ48w8zS3QYb8-GZPgSUHPMz8EZUak9-SAjkLpaaGKkpbGqWN5zh_Afr-oT2ZzBhbyv_VPFupJUBLBipS4UJlARJPjD6pKWN0ayUlPn1OYaMGakdDQffukbDqbSGhhkqlA1cjZsWQ0zEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f191ecf5.mp4?token=dPFt4VxL1YEVdbNT_EpxtAQWEIJHPQy9U_sZp3uDDqcQ1GlfIrOgmjH1NgB2GqZiHbDeJq8im5DEU34lrhloXEL42wCXGVSLQ0L8dRcvGca_pFr1VCNMa_2KSOT3RRxQlDsC-rmJE3BAqjUbZHoswEeryC_H9B-zccG-Lt3bRbVWN832ymTqR4i5rPSr2bx6_kdZpBYwjnQ48w8zS3QYb8-GZPgSUHPMz8EZUak9-SAjkLpaaGKkpbGqWN5zh_Afr-oT2ZzBhbyv_VPFupJUBLBipS4UJlARJPjD6pKWN0ayUlPn1OYaMGakdDQffukbDqbSGhhkqlA1cjZsWQ0zEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی گسترده در ایالت بریتیش کلمبیا در غرب کانادا
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/140844" target="_blank">📅 23:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140843">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlcbuJQw1xqc29u_vSqZpRc8ZvPn9vgUwConYExEzb7nsnNtctX8z1xu4xmEMI-xp6MqDQD_7dWc7JEDtRVsxhpi4T2_gshznNE67MRswWRwJOZxEXEl5aPfhVcUHFbeC61s0O3jAJGSQUsNqszhSSh1tuI-pREoUtEqThHfSLJfbEdLVwl0Hn8rTWuSFZaAXV5F2THE1527zQKTvHCGtJTx-PxkmjMAhxHbK0Cbh3LEkRz5LAE9jx8XXKtP5ts3CjYy2HbisCFRIzSHOt0Bq5e44nYkyDD2QInx-RvpNWA9jGdOjGE0ItLWpREIQAHBeLzkN-PPmBZqf9IZnwpaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان 730 تیر موشک PAC-3MSE به همراه برخی ملزومات ( فاقد رادار کنترل آتش، پنل فرماندهی یا پرتابگرهای اضافه) به قیمت 9 میلیارد دلار خریده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/140843" target="_blank">📅 23:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140842">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4403cc9061.mp4?token=boh8-i1Kso-Howy0YxA7qaYfttpSBC-_vzZYQ1ypFWdKGVSY03X2zIRVq7yjRVyowpcSWGZO26VnuPFi8d-Yvz15zf2A8rjh_HQNUPXugRWLKv6mFWOl1Ex0tsmSSjqHIpACmBerigw9M6wXahd7kE-96HHbiu2vM6oI17FRyypwlw8CHXhCRhQsMZejLJBf76qb23p5C8QSgTiBBh4aMIZUs7O5V_s8zn_3hOEo8O7AJpqVnT7xBDwDQ-cwiQC-i7MsBzAj7pizstQwn4XbL5ahyZUxK6QRnnynaVDfPo-4aCEpj8IAPUpI8Ppc9UrarE8pD_s0xJpcSRh2DClDgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4403cc9061.mp4?token=boh8-i1Kso-Howy0YxA7qaYfttpSBC-_vzZYQ1ypFWdKGVSY03X2zIRVq7yjRVyowpcSWGZO26VnuPFi8d-Yvz15zf2A8rjh_HQNUPXugRWLKv6mFWOl1Ex0tsmSSjqHIpACmBerigw9M6wXahd7kE-96HHbiu2vM6oI17FRyypwlw8CHXhCRhQsMZejLJBf76qb23p5C8QSgTiBBh4aMIZUs7O5V_s8zn_3hOEo8O7AJpqVnT7xBDwDQ-cwiQC-i7MsBzAj7pizstQwn4XbL5ahyZUxK6QRnnynaVDfPo-4aCEpj8IAPUpI8Ppc9UrarE8pD_s0xJpcSRh2DClDgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: [مذاکره کنندگان] در حال گفت‌وگو هستند تا انشاالله مسیر را پیش ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140842" target="_blank">📅 23:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140841">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
زاکانی، شهردار تهران: با اصل مذاکره مخالف نیستم، اما مذاکره باید با شرط و شروط باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/140841" target="_blank">📅 23:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140840">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔥
🔥
⭕️
قیمت طلا و دلار فردا سه شنبه ریزشیه
👇
سایت رسمی اتحادیه طلا و جواهرات
goldonliveeeee@
لحظه ای قیمت میزنه
منبع دقیق قیمت لحظه ای طلا و تتر
🚨
☝️</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/140840" target="_blank">📅 23:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140839">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIkjy8qXQIPoQgroxKNH32uS4X7NJSnq51uFSp0GYwcXfi8geTfPXarTgjNG2E7PezYrt1iuowf-ZxlPWQZIXODd7swXulpdBEiC4gbuZOr5ie-H9NIEYU0Qx_xxdJpyV2Au77BpGs6CpwUaCHfDL-7lXowbLHwuIiVlOssFXXdIu2bFK-HvxweG8hWWddZuIEmO_KG3fsPszay265q06LbhVREcHKOJXhFIoHzD4_n-4nXhCaCjvOgEf5vdq1L9NmuX-zwB1Lgro-rGHdw1LrwWWAqR_e6OZsQL3b2opceRRNRXO5C3ptkq7lsy5k66CyfRzvOlc54aA4gdnbQSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: افرادی که در چند سال اخیر _خصوصا پس از ماجرای ۷ اکتبر_ مهمان جلسات خصوصیِ «فیلد مارشال محسن رضایی» بوده‌اند، شهادت می دهند که تمام اتفاقات بُهت‌آور این روزها را «محسن رضایی» به‌ دقت پیش‌بینی کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/140839" target="_blank">📅 23:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1xMpgDLSQ7KKQPcu9Li4VKzyegkefNMLPvOik4vxTU3H6XuIt6B2vNY7tWznLENGgCJHDjKk_dVa4Q60WCKLl21OZbrYhagpNWnP-kk2XmVgl5Bkjg2Pt8ygW55wmemvcr-Fb98Xo0YWDLWcEdqSSnarOHyBFMeBTvgbO4TCi0e9e98BbZ7VhNWiQNSMfGfY_WriNeTaMumgTq2TvcOWsDuIhys1Gg6qK15zUDlDOpr2pMM9UfdwOJpGWCM35-wsyisAQDdCQSJJgqtu2QLzx6LrCz9B7LmUrhgTSYr_X2l7aPeQZx4g1mB-XQLVi6Yzfeq_JW4SXEgqyvNOsicpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
این شخص پادشاه تایلنده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/140838" target="_blank">📅 23:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140834">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oX405NlPcohPWo4msbrhdnIWyuq8cI2G81TFvxUnbBPIQ1vquZXeb1yWrIYHV1Js_Vhvews-X0kAzmu2LEStSuQtwF-XWKG8F_RA-Z136bc9df0h6B5K1Qwl3h3gb317zMItOXCMYMTr3ZsLa0g4HcnZP92TIRx1xsz-Ar2_HmYMRgU5MkQLSM9vyKodpIDFFtx4jV9sjhHUU26ONXpikLxTomsJ8EvwgS02ImyfExn5bjOJ14UaniWMuXNJ1HpqAXNO9g2hsO4CXa2qayvpi2wVGc_6_x--0sBUvBj7qE7e-6RkDc3hvYzuBTnxYcP0Eke-f6_YQouCEBJg8i6YAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGyCBPuf2Rpoz7xoXlka0NoIBOw5t7mFZQTnuUwuCqVfpcehAoRa0WgqWFpo0EeQMr5pqPpePqujdCjO-HwePezvdyWRQ723fENBDUbmoIX7qIUrqNRiAdd_6NqvpBnOhRbtqmMzWHPXlNhKbvhTS2EvIRr2OfTHANG8O8SyGfKCnZic6xU7ayUMVCACHvetjMiEwyG8Wx12j82myHy_ZKBKcaIgWG4QMJ7tkVpDtBGUQbHGvfsxrV8v1_qz5ug1RvmqQXu-U24qCfJTNDexuf7m46Ix25fnaFvoWdGZ1WQ1SS0jP7rqelUBACMOS8p7MSaKWJkDEQvJ3DBXQ06BhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uU4_ryuwSpSCy9By0wsE83rT9QOVjmI7LeDxgv-OiYFYSBPanorSsTioUnpcu5-TW0LnUX66-LURhzZCym20A2GtDvZd-MUA4OaV9w7tD_fjoCsF2xpctiysh9cS5IRi0xAJdWKRSBCWp4KILxQ0Ad6pih9e7Kay2UhwQsZ8wbIeOaXjjiroB4tRhnR2w3ZkRGwAd-c1PLSE6wiEGTouZcJIeR8GYeuigaMwKhvhPikOnuHqoT6MkzPix0yR7niH0Dp8Ee1QStEC9GqjPsP1zzLwfT0NotDO6Bonk2pKLmnpRvHeLX8xzO1ULNSuQapOFJgrwCcAyMjPXhRaQxMktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9kNFJXlxh8S1JVQhBOU7aqTHnEwiMd4GlDwS33gV0hA-Qv4G8rfuzMjqV41Gso3FAV8aEMpBJeaSZ_8HUEEg5wLByHAvLnRBwz6hi0j9GN1WBczS-N_vNQ8Y18mN5DF8U2VV9PNMZUo3x2cZNoDDgakLs-hXhHQpAP7JIWSx1lDHHauQpLyNofRPXJUQZnfNdM-JaYTriumRt128EG5AWxmNezlY7Mi1ldm-acf8srn2xTHz7CiGf1dBmknm7mKbstCFdaVp1L7LCM_D0fCacc1fif2Ixm7OH1-kGZ-PLhkpngbICqAJSjlwd3KlhF5yQctq7FS0BpZNcuwWJxrTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شمار زیادی موشک و پهپاد به سمت تجمع‌های نیروهای دشمن سعودی و انبارهای سلاح‌های آن‌ها در المخا شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140834" target="_blank">📅 23:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140833">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWq-YiDFFyQoC91YjPdatPsjM2k4uGT3fqxNBKwPBX82eEUj2CBhHgkR--sCMooZgLeCMk06yywozyYl8GpH3qFeK1YO7uc6uo6VjTitu6s9-a-QADRTLDIsHzUAkvEx2csp5sULxiRzlLZsOOU2A2K2nZzeMsadG8ZQkUCmxU4uBYF6IxcpV8iNMAoowjokN0Pq9ukhjzfRsC44wVF_IRWTfG9UiTBvRJYxTcwUaxDqwzOYswK95y_lDx2NDnL9hv2fDhxWG78nWRy4RMCT3WVoPlqUcLHYiRvT8YEBEpVKM0g10v5PcU1jJ8RbRD5BdtXJvfmtFV9h-6_KWtcJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر یک سازندگی: مردم می‌خواهند زندگی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/140833" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140832">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12032b204c.mp4?token=MgornPoRFqIbYL29Vl7Rofy3Y2lz9CF4tK3gmoyB2MjwNvg7MbPUVNWM6ZLkzn9HzpBc7wwRpLR35uB1P1TsgEofDti-AqjDSBEXj89_6hMzKDcmnQs8pUujmCVggdYEOZMlj39zQP0juBQPmQT47IuPsq54TDOiMfXw87aNWkoSpO9gtRHRx9ZPdFTp1rnKctHKnTPeImRZOiLAxF0CaTRxGBjqCJZ1f7tWIqkD-dDsqV3hnWcp1ADTYI66WHBIhbMulB3yStH-qTx9c66xVjXYJu3joA4vm8pGw3eMnNYFCj4O3mTo4McNhvAvKHY0uBO6xp14-T-DJNFF0l6HZrkNILD3B-fRKHr8gCkasTszDaDJaCxBcYZi88XheaOsT-57fSJHvP9sW_iaL2b6tLUgYpCBfBf2bdV_ekKs0TIN4oCVLRF1Addvy9M6c_hgMGwXPJipQeckoy3e8oRkz_GxYv1sP70h7jRIEVz5Q-KSzeOsQu4GcL1posp68t5Z9AWtNwj_m1kNgMSX1iGtq5e90cjY4dDVVsE5ZSyhwy4MgHq3502dF1mZDoGQqbOyumSk_hITz8BPwlK9Fx6tsMqMvG1xqYUgBNJ0PLhubWq-J8yGIjZXPgZyUfLSOS4FYsYEy1kiTDR6OPslYK_1deCjNmeL9424Rj9gaOaCjGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12032b204c.mp4?token=MgornPoRFqIbYL29Vl7Rofy3Y2lz9CF4tK3gmoyB2MjwNvg7MbPUVNWM6ZLkzn9HzpBc7wwRpLR35uB1P1TsgEofDti-AqjDSBEXj89_6hMzKDcmnQs8pUujmCVggdYEOZMlj39zQP0juBQPmQT47IuPsq54TDOiMfXw87aNWkoSpO9gtRHRx9ZPdFTp1rnKctHKnTPeImRZOiLAxF0CaTRxGBjqCJZ1f7tWIqkD-dDsqV3hnWcp1ADTYI66WHBIhbMulB3yStH-qTx9c66xVjXYJu3joA4vm8pGw3eMnNYFCj4O3mTo4McNhvAvKHY0uBO6xp14-T-DJNFF0l6HZrkNILD3B-fRKHr8gCkasTszDaDJaCxBcYZi88XheaOsT-57fSJHvP9sW_iaL2b6tLUgYpCBfBf2bdV_ekKs0TIN4oCVLRF1Addvy9M6c_hgMGwXPJipQeckoy3e8oRkz_GxYv1sP70h7jRIEVz5Q-KSzeOsQu4GcL1posp68t5Z9AWtNwj_m1kNgMSX1iGtq5e90cjY4dDVVsE5ZSyhwy4MgHq3502dF1mZDoGQqbOyumSk_hITz8BPwlK9Fx6tsMqMvG1xqYUgBNJ0PLhubWq-J8yGIjZXPgZyUfLSOS4FYsYEy1kiTDR6OPslYK_1deCjNmeL9424Rj9gaOaCjGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش اطلاع‌رسانی جنگی یمن، تصاویری از شلیک تعدادی از موشک‌های بالستیک و پهپادها منتشر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/140832" target="_blank">📅 23:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140831">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/140831" target="_blank">📅 23:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140830">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
میتشل باراک، دستیار سابق نتانیاهو:
مخالفت علنی نخست‌وزیر اسرائیل با طرح غزه به انتخابات اکتبر مرتبط است
🔴
او این مخالفت را در جلسه کابینه و در میان «دولت بسیار راست‌گرای خود» اعلام کرد؛ موضوعی که نشان می‌دهد این اقدام بیشتر با هدف جلب پایگاه سیاسی داخلی او صورت گرفته تا مخالفت با واشنگتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/140830" target="_blank">📅 23:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140829">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wr2qp8adDDXsvv9pEK3t4k3gSho8HiRs02Ppek1b_GjX0lGOeeyliqgIKil7Zz4zsdo6RCOj_xvchkQ9SOfDzCMPJ3r2ngEvCwDJImNjwTUiIvaqfRxZTJMv7-sMDpq6W-iUWJBZdd9oWH4kp3a8pu5dLqSJNf5Go4BDRcNuErzBJlVOr-vJ7zufFVcZRp6XS5wYrVLSbjk-RtigqNw9BEb_GHAfrMhmPmv2zpFs9s_vUScwL7N_uyQOM1c5kQQLLZj3-4-N_4bA3uB8TN8sGFuh8IIzRFiYdFvKTMCf8cV05zE-p1hGo0CxNymxTuzg3DZGGTaWOqkx0Nwm1qXQEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس برخلاف نتانیاهو و رسانه های اسرائیلی که گفته بودند احمد وحیدی گفته در حال توسعه سلاح هسته‌ای هستیم، هرگونه تایید توسعه سلاح هسته‌ای توسط احمد وحیدی را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/140829" target="_blank">📅 22:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140828">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0662ccaa16.mp4?token=snfQqXfrT8v9ZRCWBL9JGEv9VZR8Tu9E2kiW3gqGHV8c_zhY14EH8MVq6mwhOnp9fsY-IAYynPR3D25cw_BY-Vp0peLlVILgjdN0qjrhv5_JoFMCkbh9gQc9a12at_n-D7x7LZB7fagTAlgJ-MaIDyXxbA5ZeoY_sIqRIQ6EYBGYSZlwDA_9Q9oBIHssG_KGlKhDJvQRSMKJ-PPayTcHGQOxIKY8zZzZKWc7nXlqVPNn02WzjabGTVay1pJgJ3ZxlFWkUmXavl7Gbahj9Y_F69uhasl2Tbkf6Q-MIUnRtStkxQyhAGw6ELWqqU-XGQAj5qk4_ggz_GMoAOtk1DyFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0662ccaa16.mp4?token=snfQqXfrT8v9ZRCWBL9JGEv9VZR8Tu9E2kiW3gqGHV8c_zhY14EH8MVq6mwhOnp9fsY-IAYynPR3D25cw_BY-Vp0peLlVILgjdN0qjrhv5_JoFMCkbh9gQc9a12at_n-D7x7LZB7fagTAlgJ-MaIDyXxbA5ZeoY_sIqRIQ6EYBGYSZlwDA_9Q9oBIHssG_KGlKhDJvQRSMKJ-PPayTcHGQOxIKY8zZzZKWc7nXlqVPNn02WzjabGTVay1pJgJ3ZxlFWkUmXavl7Gbahj9Y_F69uhasl2Tbkf6Q-MIUnRtStkxQyhAGw6ELWqqU-XGQAj5qk4_ggz_GMoAOtk1DyFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جشن امشب مردم پاکستان در اسلام آباد بخاطر توافق مکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/140828" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KceBQQRGZfwCED3m5T2-HZgNyhFb9G1n7_9kThmadye7UAcJL6afP7eTab262CGL4EyWMaOUi0B-FL4kHiWMUHtpZGP60_4E5czUAB8iMbPT6Yb7pxE9kWbMcFlezrYWVhWG6a9LWbQF5DDZVml3xSoF71Bzm80sa5-k2NZ-0a-6W0uLyoPlFunCP0FF9L9v5CTH5WUEyFvWTn80Ebh7Q6H3UBaBRvM8jugHYEIIn42wC_LwyrbJqJMcv7FXDe_ZhlqzUDNEgSMQpm4XbugPQfCWsuXusrfuDtL4ER7qkG7oouMD44fs9LaduH-Qk7GG5OA0DTpP2xHlkg3VlprGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vka4oR7TzGE_uyB7OMO4AAny02rmKvW1Fr4U_4cH_Wu6lUsyqrQuRuKv5uomxvuoWGK2Tkv4iUv3GRZv6LJWBOrM4K5bAUYbAJDviEEGy5JbTlrVoh7euOEvW2NJ9ojuxf8oNM5hmcqxwlET-UOTzOi_jmQYrFuQvcPg8rPtc4C-NCBGsX2jfFraST9K2DUIFRIGMNbTSZFUvi8KthkSbOWJwI0uJIg-dwgoQOHjbs8Zn4yTFE9TeqB9oIjJjlfn5pXOv74IzxR0XPhTA4N-1GG01T45zEd13aPe7QfnHDFKhVrh_XhzzVAe-b1afJ_GdFvs2j1vPFrKFLcoxcNHBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2qMr3MiSuC6wEheMCXQSyDzA5JEmGjgbmgsD-D2x5aHt7FRfEoUqKJnJxAX7TKTOYG3oXFoY84gjVpc0PS61sTMR5GYmR41mLOcpsA5dmOlslMDKJSlKkb-m1h-P0P14r3-Gw9gcGBVU5YHMEokS0WMCfSbLSpQfa4cCwNI0V59snYTq2i9Th6qzvSq6hlABhtAjxuWu8TLlqwNqQJYAFS0o48h3ZUncZAce7tT3eUulHW55kZ3wHeXVo5U3RkVxN2lE11qoiTgoYJ7MOWoN9mdgcrS8gi7irCtxpdEfwb3xjQrisMfwF8vQLKeU7hJo0zsWMto7hhBzOYnz-nGgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انتشار تصویر تلخ لیونل مسی در مراسم سوگواری و درگذشت پدرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140825" target="_blank">📅 22:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
اوکراین دیروز یه تانک روسی رو منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/140824" target="_blank">📅 22:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140823">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtc8kE6rUpRDC5jODZB8hD-eWFEIcO5uSVv7wT3rDobX6X381BBPB30b7quDDn7Y9iWUKRL0v-o_BATDmfwr2afL-cNcmAMiQc2bIoi_W2d2fC-BKK1hsS8RDOzLu5quenkpW1XuE61c3orTfZKUkcdL_rIMXpzXfxP0h5CyDvX-w-XinQDOhmr4Tkmmm56lAoAOxHR5Gd3DcowgLTeD5RnVD9f9ZwHQwv_cXf27kzhS46XAestcYKKdBEg5GZVfvE6cH2Zh2_1qRDHF7YJ1tNk5ZnnuJw3cfZKDTMthYzGzM-QoRH_rGbap-Vg31Jyg1LeuW4ydrGbtG846LrlrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه مراسم تعزیه، امروز تو ساختمون وزارت خارجه با حضور عراقچی انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/140823" target="_blank">📅 22:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140822">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a610735f5e.mp4?token=Y_mwSXHJs1BHUighBsgP1EEWKyRmu6jmnZaWdFCx3l2gr9eAozkzT1LjQ3f9hmM2Y1onLLxQcAjBgaig9F1QKKK7WUZr9ImLbp5MQWFH-lzN4pzE0vUB7cJxJVF7klY2qT0xZmaQqLTcPjU-DEoux1zn347lJvutjjX1ZmQAYvR6xrQMMT4uOu-3GNDogQrYkuOA_LDYXAbFESxqh9_uuGRT09p5R2kOxPCHXbJsv983WOzL1twKOyb80fAH9Aft_octXoFi5DUVyHZUAtyooNdijSfEbl3_LAYGlP8ean2yXDSuAkAFqGCCX2n8jUJHe-70w9jIxgE1scyaV5QejA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a610735f5e.mp4?token=Y_mwSXHJs1BHUighBsgP1EEWKyRmu6jmnZaWdFCx3l2gr9eAozkzT1LjQ3f9hmM2Y1onLLxQcAjBgaig9F1QKKK7WUZr9ImLbp5MQWFH-lzN4pzE0vUB7cJxJVF7klY2qT0xZmaQqLTcPjU-DEoux1zn347lJvutjjX1ZmQAYvR6xrQMMT4uOu-3GNDogQrYkuOA_LDYXAbFESxqh9_uuGRT09p5R2kOxPCHXbJsv983WOzL1twKOyb80fAH9Aft_octXoFi5DUVyHZUAtyooNdijSfEbl3_LAYGlP8ean2yXDSuAkAFqGCCX2n8jUJHe-70w9jIxgE1scyaV5QejA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌ها امروز به پرواز درآمده‌اند زیرا چندین هواپیمای عمومی وارد فضای هوایی محدود موقت نزدیک باشگاه گلف ترامپ در نیوجرسی شدند.
🔴
تمام هواپیماها به‌طور ایمن به بیرون هدایت شدند
🔴
این رهگیری‌ها زمانی که محدودیت‌های پروازی موقت در اطراف رئیس‌جمهور فعال هستند، روتین است
🔴
هیچ نشانه‌ای از نیت خصمانه وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/140822" target="_blank">📅 22:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140821">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=jX2E2FGtf4sAdjlzEaxsLUD6V2CFuHWn8l3yLqBBzzfGIpsKjQpCu7_cuU3btY4LuOhs5Cm7cqZBH7z7g8yKSCCYCML5drvkyjLaJPJjDpqxeP-o-TnO_pGlQh_v6kprbSbCsq3ee3R1YUbPZbQg9NA1Ypqy_SwtOj0UbiLZmiRgmn65FRgp8bkbJWfdLeQGRqO1TfnQ_rVriQmkx2vWB4Lm_zhJSEWFgolL9kjjI7kqrAZbc03U-B-u_6zg_R71dYeZb-lrpOhfJgstKwJ-BYbQlzIbGq8nabvX5Tauf5Hhz9rwp_rq_QdISKUwU8rz3dwCUNMJ_uu4A2hfGat157FdBBOs7MV1OGZPt0c8sxZlE7XtsK2IIrR4IR6FdME9v7oXWDM9U5RI17iRG_roe2tByPIVUvzmwCycl1yQmk6rm1mM17mOL2qLsihvMROa2Q9t7BRTAS1dQzMgJeHePnDJ3VAXrtgqnF0zRHkouTS16PiyWUgLcE2DBQEJkoIUjARiloNyi6ylVJPYaAx-Sw2r031IWR_GdhjanjlKYqgjhjSRJYHNOJgbQfWZJZAZupTpNkkXkngkNHbFEbK-eQVpZMFuWwVtbUEzjwaPgLvN2Fi5vqPXVuL5nAB5McNh4ZleQ1RMsO3BW_UdoNC6TzE8Bw1OZqdaRIzOImV7Y6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=jX2E2FGtf4sAdjlzEaxsLUD6V2CFuHWn8l3yLqBBzzfGIpsKjQpCu7_cuU3btY4LuOhs5Cm7cqZBH7z7g8yKSCCYCML5drvkyjLaJPJjDpqxeP-o-TnO_pGlQh_v6kprbSbCsq3ee3R1YUbPZbQg9NA1Ypqy_SwtOj0UbiLZmiRgmn65FRgp8bkbJWfdLeQGRqO1TfnQ_rVriQmkx2vWB4Lm_zhJSEWFgolL9kjjI7kqrAZbc03U-B-u_6zg_R71dYeZb-lrpOhfJgstKwJ-BYbQlzIbGq8nabvX5Tauf5Hhz9rwp_rq_QdISKUwU8rz3dwCUNMJ_uu4A2hfGat157FdBBOs7MV1OGZPt0c8sxZlE7XtsK2IIrR4IR6FdME9v7oXWDM9U5RI17iRG_roe2tByPIVUvzmwCycl1yQmk6rm1mM17mOL2qLsihvMROa2Q9t7BRTAS1dQzMgJeHePnDJ3VAXrtgqnF0zRHkouTS16PiyWUgLcE2DBQEJkoIUjARiloNyi6ylVJPYaAx-Sw2r031IWR_GdhjanjlKYqgjhjSRJYHNOJgbQfWZJZAZupTpNkkXkngkNHbFEbK-eQVpZMFuWwVtbUEzjwaPgLvN2Fi5vqPXVuL5nAB5McNh4ZleQ1RMsO3BW_UdoNC6TzE8Bw1OZqdaRIzOImV7Y6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌بیشرمانه و فحاشی مجری عن صداوسیما به سلطان علی دایی
@AloSport</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140821" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140820">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: ایالات متحده می‌خواهد اسرائیل به نبرد در سه جبهه فعال پایان دهد. این پیامی است که ژنرال برد کوپر، فرمانده ستاد مرکزی ایالات متحده، که آخر هفته از اسرائیل بازدید کرد، منتقل کرد. در مورد ایران، ارتش اسرائیل به آمریکایی‌ها اطلاع می‌دهد که اگر…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/140820" target="_blank">📅 22:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کنار تریدت بیا داخل ربات جایزه هم برنده شو‌
!
🏅
🔍
فکر می‌کنی نسبت به بقیه
زودتر می‌فهمی
بازار کجا میره؟
💥
پس وارد میدان واقعی شو
؛ جایی که فقط دقت پیش‌بینی حسابه، نه حرف و حدیث.
🔝
در ربات Preward قیمت نمادهای مهم
رو پیش‌بینی می‌کنی؛
💸
BTC
🌟
Gold
🛢
Crude Oil
🇪🇺
Eurusd
5️⃣
S&p
💵
هرچی دقیق‌تر باشی
، بالاتر می‌ری در جدول رده‌بندی و
جایزه دلاری می‌گیری
.
🛡
نه سرمایه‌ای درگیره
، نه معامله واقعی با ریسک حساب...
⚡️
فقط قدرت تحلیل تو تعیین می‌کنه چند نفر از بقیه جلوترن.
🏆
رقابت
هفتگی
برای کسایی که سریع می‌درخشن
🏆
رقابت
ماهانه
برای کسایی که با صبر و استراتژی جلو می‌رن.
💯
اگر مطمئنی تحلیلت خوبه و نتیجه میده
همین الان شروع کن و اسمت رو بین بهترین‌ها ثبت کن.
🪽
@Preward_trade_Bot
📱
@Preward_trade
#ربات
#جایزه_دلاری
#فارکس
#کریپتو
#ترید
#پیش_بینی</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/140819" target="_blank">📅 22:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140818">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کوین هاست، رئیس شورای اقتصادی ملی کاخ سفید، به نیوزمکس گفته قیمت بنزین در آمریکا همچنان «بالاتر از چیزی است که می‌خواهیم»
🔴
او تأکید کرده تا زمانی که بحران خلیج فارس حل نشود، نمی‌توان انتظار کاهش چشمگیر قیمت سوخت را داشت
🔴
فشار بحران منطقه حالا مستقیماً به پمپ‌ بنزین‌های آمریکا رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/140818" target="_blank">📅 22:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140817">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / گزارش‌ها از وقوع «حادثه امنیتی» در نزدیکی باشگاه گلف ترامپ در نیوجرسی
🔴
فرماندهی دفاع هوافضای آمریکای شمالی اعلام کرد جنگنده‌های این واحد، دو فروند هواپیما را که به حریم هوایی ممنوعه در نزدیکی باشگاه گلف دونالد ترامپ در بیدمینستر ایالت نیوجرسی وارد شده بودند، رهگیری کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140817" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140816">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: ایالات متحده می‌خواهد اسرائیل به نبرد در سه جبهه فعال پایان دهد. این پیامی است که ژنرال برد کوپر، فرمانده ستاد مرکزی ایالات متحده، که آخر هفته از اسرائیل بازدید کرد، منتقل کرد. در مورد ایران، ارتش اسرائیل به آمریکایی‌ها اطلاع می‌دهد که اگر اطلاعات نشان دهد که جمهوری اسلامی به تلاش بی‌وقفه خود برای دستیابی به سلاح‌های هسته‌ای و ارتقاء سیستم موشک‌های بالستیک خود ادامه می‌دهد، اسرائیل گزینه مداخله در ایران را برای خود محفوظ می‌دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/140816" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140815">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqImNXBjaONpoGz95iUKAvVRyV-5AD_Me_DMg0VYzQB5MdMA3hrgaBNmDuwvGDZmIAqQRI-x0XeXkxTBno3AUA0sPEW30gKK5tVpEXPk9R-fx_fWjQWhl1FqFirzJufn8k287Nrug1ScA4Ax-fI9GG8m3UMBacp-T6egLkh8YTOvSb5GvSjrBXtIr_titdyjzdGg2ZzOecIPXOYkPFggw0-TrFTA5qG22DVcTeitF-BJ4xp53wyhvEHgTfzXd2H191Bfz8IbBuS6O8G1APveGLhshbC1YaIE7PdV3RDhli8eSnEmul4JWVdNaRzmNGbrCz8bM6gk5GiSGYqx-PmnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
رییس کمیسیون امنیت ملی مجلس خبر داد/قانون کنترل تنگه هرمز در کمیسیون مجلس تصویب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/140815" target="_blank">📅 22:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140814">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnSoDjBvleUXFr5vTfceKH_jx1RsfKzlsrMyutljfo3fHDPQ9LFJiGKP2BO7PFrR4peBvwQy_BFRdnE8ro6Ed-ktr2U6rTS-3sG6St-OQvBYFgartBQlDYyNx2DrJPfyeeC-kX2HcoxxtmtJy8kKrsqAcCXGdHQujzmTi1B9vKQpeh2ipMAvzRpNxWFaYeX2g1cg73LHPzmO756J6UEr5bTutnWt0fI5VHgO4EE2cS4K62wNkYNB-9IEWIeIo9sNtT7Razz4FQAjrMlTAUVGC4waygFpgckwLfjL6NTqC7SO_oyrqkgzAqr5L1aCKneCxY4ro2Jii0PENIRxIgYNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید: هیچ رویایی زیادی بزرگ نیست، هیچ چالشی زیادی بزرگ نیست. هیچ چیز وجود نداره که برای آینده‌مان بخوایم و فراتر از دسترسی ما باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/140814" target="_blank">📅 22:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140813">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
حمله مرگبار به یک پایگاه ارتش در مالی؛ ۱۰ نظامی کشته شدند
🔴
بر اثر حمله‌ به یک پایگاه ارتش مالی در شهر «سان» در مرکز این کشور، ۱۰ نظامی کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/140813" target="_blank">📅 21:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140812">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMIQWaHiM6WfpqYo-Tsn7-PY5WHl6e6yW-h2T4Pxx-ZSE34-ROFBi-IGswaRUF7U9RyRWzMipN6HdXMVYcW7LOY2vIp0yDhC9rEvOVAjJfdUq55atJ1LTKkRbOeH0DuwyBNzF7LeOJB-1eonFZxdUsgsZq6IfuOhqDvnXRwa5vOlP_aRKqTMHNGH_Qfbx-gGaOqfejArdnkcQxIaWF_EQ1oqOK1tSPpetV82NR5GLtfajyjpVglzO4x27823NQPdLvRxZAjpO7KcD-x2lUbpvHFdOGQXdg5GrkycddvRIa0DpiTNyicAYlhDmujpMmdjsK2YKM1WOu5bQOpSOSSO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شانس برنده شدن انتخابات ریاست جمهوری آمریکا ۲۰۲۸، از نگاه کاربران کالشی:احتمال جی دی ونس بیش تر از همه هست
🔴
بعد از اون مارکو روبیو که به کم ترین
احتمال در چهار ماه اخیر رسیده
و در رتبه سوم گوین نیوسام، فرماندار دموکرات کالیفرنیا قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/140812" target="_blank">📅 21:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140811">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMpCTZKSvs77XLhdvuIWR_GRlBWti8d5z4oKDQDVUdBRCPRtxQhNs5CnKZOU9AB-D3OYabhA4sDY3DntZ0ru7No4WlPbCH0wDkp-3wZfI5MbhsLuj-WgZuCU87qG9Hk2Ruvi1z2QHIwubqbvL_MRHmL_5h0gdsh9ZJmM9Q0YY18RuybjnPldMtkXQ25C65UX2LX7PX7HhktFxLjnz9FTbBYAldi4-gJm6LnaxOMRMnUxHKB_L1RSPpWIeCfttd52FEnlVATnFKh6PHIk3jzJh7Jj8ByV29EzJ5hyKeUd791zQOcnOYvTWVREFXBKznqEsPHekfEtE6tNYIlvc1i2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با حکم پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/140811" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140810">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080f1da3b7.mp4?token=lfiJ2XMvM1atP3d0GREp-SM4K5jMYwhr8SIOiTzKlTEUYKd281RHiGUOQR3Spqos8t40ij9l8I711hP9Gb9Ykw1cdgEitqPayYU9IKo0aoAiQWPNvNXijhwKv4jOILcXOJUQFdjWpXekRGP-aJ3SpQn4fnSuMIeAHlb5UY0iCTKM4KcALXFHGo_oz7QQvMeKZtuUWs8jUxt7XFmbvuuJFxamnE1DKi1tDASqQJOBRxsyi9FLHjMWZ_VC7u0DtTeVz8XrORgphxgM3j6SY2Yd6Fh_cRciGch2sQRTbetrYi1aPuM1MU-_WFEGjYVgQ2hnW2hFiJbJznP_mvZMIZCOpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080f1da3b7.mp4?token=lfiJ2XMvM1atP3d0GREp-SM4K5jMYwhr8SIOiTzKlTEUYKd281RHiGUOQR3Spqos8t40ij9l8I711hP9Gb9Ykw1cdgEitqPayYU9IKo0aoAiQWPNvNXijhwKv4jOILcXOJUQFdjWpXekRGP-aJ3SpQn4fnSuMIeAHlb5UY0iCTKM4KcALXFHGo_oz7QQvMeKZtuUWs8jUxt7XFmbvuuJFxamnE1DKi1tDASqQJOBRxsyi9FLHjMWZ_VC7u0DtTeVz8XrORgphxgM3j6SY2Yd6Fh_cRciGch2sQRTbetrYi1aPuM1MU-_WFEGjYVgQ2hnW2hFiJbJznP_mvZMIZCOpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو شهر فوجیساوا ژاپن مردم اعتراضاتی بخاطر ساخت اولین مسجد تو این شهر انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/140810" target="_blank">📅 21:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140809">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHwenvgZQiSNHo0fIo0-22fZ_HRSBaeheTaKgZhwLvU3G__SgOUxmRBIk3ApHFd9VtIH1OJNs1JPxloWLtkxJtpkrzp5rSmUE7L1V_735olPQeGZwXs2zNeVecpKfz3aUfW1PnzR5b0WYe04g0hxAe49nBnrdWpfT5moasbukg8YTuyAUFmFC9Hov8EgrAbXZlJCOTjQmoRgt7-iQNBsKS5B9pDrnxxbphV1_ZU7Su7f74mqicbJCRNHVjVqNVO6nQl5yUNT-W-ySveFJHAB9j6-VKxgI95aBTD1gwihJdqnSn7QkNSSkmJm3SxX2qH9Coki20q5_gxl0zuVSD1cyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ پستی از هیلاری کلینتون که طرح او برای غزه را تحسین می‌کند، بازنشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/140809" target="_blank">📅 21:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140808">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
الجزیره: رد توافق غزه می‌تواند برای نتانیاهو یک بازی بسیار خطرناک باشد؛ ترامپ دوست ندارد در صحنه جهانی به او بی‌احترامی شود
🔴
ترامپ کنترل کاملی بر حزب جمهوری‌خواه دارد؛ بنابراین اگر او تصمیم بگیرد این موضوع را به مسئله‌ای سیاسی تبدیل کند و بگوید زمان جدایی از اسرائیل فرا رسیده، احتمالاً بسیاری از جمهوری‌خواهان از او پیروی خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/140808" target="_blank">📅 21:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140807">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اکسیوس: میانجی‌های قطری و پاکستانی اطمینان داشتند که این توافق روز
چهارشنبه
اعلام خواهد شد، اما از آن زمان، چشم‌انداز دستیابی به توافق کمرنگ‌تر به نظر می‌رسد
🔴
یک مقام آمریکایی مدعی شد که حدود ۸ میلیون بشکه نفت هر شب از خلیج فارس از مسیر کریدور جنوبی تنگه هرمز و با هماهنگی ارتش آمریکا خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/140807" target="_blank">📅 20:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آکسیوس به نقل از ترامپ نوشت :  داریم با ایران بی‌سروصدا و آروم پیش میریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140805" target="_blank">📅 20:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYAq77CJGWq7nJNBj0JU4-iqnxbNR_9dFexeDG8cU4f7E8F0nixltKRh1CERs5gyJ0PpMoJQUCVdBBbxJKzuuhoCr2ym7WSO0LOPot3PQmCqvmKpIChA6RLX_l5-f-1d3KQSX0cTNKc0BtCl82Htnq_Ea2CnZLom70hynLGVcIypCE9cwrvKrLHXzimo8WdY5KWBzEmGlBb_HVEJbdQFOHMcAxwPqly4oht8WeGv8U7D0kQebmDVdci078cIyQIVM6RhQ8PP_6w5D8bI5POcbAku-_EG53Ow_Fgt8c29Gcgw3f83UnUi-W6Hh75rqgiaXixX6scRYkPxzE3-Cwlh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید مجتبی خامنه‌ای، محسن رضایی را به عنوان نماینده خود در شورای عالی امنیت ملی منصوب کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/140804" target="_blank">📅 20:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
آکسیوس به نقل از ترامپ نوشت :
داریم با ایران بی‌سروصدا و آروم پیش میریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/140803" target="_blank">📅 20:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / ترامپ به کانال 12 اسرائیل: تصمیم گرفتیم تنش هارو کاهش بدیم با ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/140802" target="_blank">📅 20:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پزشکیان: باوجود پیچیدگی دیپلماسی پس‌از جنگ، ارتباط مطلوبی با کشورهای منطقه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140801" target="_blank">📅 20:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbb58dad63.mp4?token=kaaeBbvfuhjxB63NFyPHYUW7MYw2pDSGU6YMbMWp9GsywpzwOnpgOV39xofoGkUbiO9lhjAnizXrW_ubJ7pXZM6V_YKHRlSr7vWzycWIETAEZXny8qd0b-KjBs7W7pYqRE4O3JvbzYZOpIipmR1Qs-Zo6yLhKOnDyUNjZBWoX4hp4vFa0BJWKwb0bq7QGI4wXLnRaQheaLHXT0-8Qi7YZnYn7cDI3v5HtRnJjboWHjco3GkrFtpqDjsd6dNzv_r6q1Q45t3hU3m0DxbUGY21C3qRJiuQnUUY_22kLUUHJhR1hdjd3HqPF32p9FMY4DgSrkR8CUGK346lXml5UMzGUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbb58dad63.mp4?token=kaaeBbvfuhjxB63NFyPHYUW7MYw2pDSGU6YMbMWp9GsywpzwOnpgOV39xofoGkUbiO9lhjAnizXrW_ubJ7pXZM6V_YKHRlSr7vWzycWIETAEZXny8qd0b-KjBs7W7pYqRE4O3JvbzYZOpIipmR1Qs-Zo6yLhKOnDyUNjZBWoX4hp4vFa0BJWKwb0bq7QGI4wXLnRaQheaLHXT0-8Qi7YZnYn7cDI3v5HtRnJjboWHjco3GkrFtpqDjsd6dNzv_r6q1Q45t3hU3m0DxbUGY21C3qRJiuQnUUY_22kLUUHJhR1hdjd3HqPF32p9FMY4DgSrkR8CUGK346lXml5UMzGUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی دریایی آمریکا، یه قایق که حامل مقدار زیادی کوکائین بود، توقیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/140800" target="_blank">📅 20:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
الجزیره: تهران منتظر قول آمریکا برای رفع محاصره بنادر و تعلیق تحریم‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/140799" target="_blank">📅 20:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کان نیوز مدعی شده ایران برای بازگشایی تنگه هرمز شروطی از جمله رفع تحریم‌ها، خروج نیروهای آمریکایی از منطقه و پرداخت غرامت تعیین کرده است.
🔴
هم‌زمان، امارات ایران را به حمله به کشتی‌ های خود متهم کرده؛ ادعایی که در کنار شروط تهران، نگرانی‌ها درباره به بن‌بست رسیدن مذاکرات را افزایش داده است.
🔴
حالا بازگشایی هرمز بیش از آنکه یک توافق فنی باشد، به مجموعه‌ای از مطالبات سیاسی و امنیتی گره خورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/140798" target="_blank">📅 20:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31a5d6e71f.mp4?token=gde_5ALiV2yA9UL0tiyi8h1qVldVqyLa6kB5AQHxB6aU0CtR4WK60JuRQNyK2qy65_yrXcD_m0XFzQHWD1OMmtWZgbsq0Y02EA9Xu065nI-Rbx5kyWsJZKn6b6bCHkGlfExa_EppzxwH7P9mfwgPZjAyyPYUni4Lm8lexSPjw3gLWcpJwWkmLoP6cQEEjI6NoG4s_pHMPmBWxGwcMm_BoWSTd11rd8BAWlFiEqR8xe0rUhh4CXc1x14wBW529Lr3aE3rTXmrqclXLkb4tDFybzmIG7AZx1MN74aVbSh3H1s7nkJsS5JVy6k1FKh-aFNGBBw49Avstg5XB4NFmn1Cuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31a5d6e71f.mp4?token=gde_5ALiV2yA9UL0tiyi8h1qVldVqyLa6kB5AQHxB6aU0CtR4WK60JuRQNyK2qy65_yrXcD_m0XFzQHWD1OMmtWZgbsq0Y02EA9Xu065nI-Rbx5kyWsJZKn6b6bCHkGlfExa_EppzxwH7P9mfwgPZjAyyPYUni4Lm8lexSPjw3gLWcpJwWkmLoP6cQEEjI6NoG4s_pHMPmBWxGwcMm_BoWSTd11rd8BAWlFiEqR8xe0rUhh4CXc1x14wBW529Lr3aE3rTXmrqclXLkb4tDFybzmIG7AZx1MN74aVbSh3H1s7nkJsS5JVy6k1FKh-aFNGBBw49Avstg5XB4NFmn1Cuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: افغانستان و پاکستان نگذاشتند تروریست‌ها و تجزیه‌طلبان از خاکشان وارد ایران شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/140797" target="_blank">📅 20:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بمباران توپخانه‌ای ارتش اسرائیل، شهر المنصوری در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140796" target="_blank">📅 19:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سلطان عمان در قطر؛ هرمز روی میز رایزنی‌های دوحه
🔴
هیثم بن طارق، سلطان عمان، در سفر رسمی به قطر با شیخ تمیم بن حمد آل ثانی دیدار و درباره روابط دوجانبه و گسترش همکاری‌های دو کشور گفت‌وگو کرد.
🔴
بر اساس اعلام دولت قطر، وضعیت تنگه هرمز نیز از محورهای مذاکرات دو طرف بوده است؛ موضوعی که در میانه تحولات مرتبط با ایران، نقش میانجی‌گرانه مسقط و دوحه را پررنگ‌تر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/140795" target="_blank">📅 19:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بانک «جی‌پی‌مورگان چِیس» آمریکا پیش‌بینی می‌کند که قیمت طلا تا سه‌ماهه چهارم سال جاری میلادی به پنج هزار دلار در هر اونس خواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/140794" target="_blank">📅 19:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نیروهای دولت یمن تحت حمایت عربستان، تحرکات و تجمعات حوثی‌ها را در چندین جبهه در غرب، شمال غرب و شرق شهر تعز هدف حمله توپخانه‌ای قرار دادند.
🔴
این حملات شامل مناطق طبع المدارجات در شمال غرب تعز، جبهه‌های حمیر و العقروض، و منطقه المحرور بود. همچنین گزارش‌هایی از حرکت نیروهای کمکی حوثی‌ها به سمت جبهه شرقی شهر رصد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/140793" target="_blank">📅 19:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140792">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
لبنان حضور در مذاکرات رم را به نتیجه رایزنی‌های دیپلماتیک مشروط کرد
🔴
یک مقام لبنانی به شبکه سعودی الحدث گفت بیروت در حال بررسی دقیق مشارکت خود در دور بعدی مذاکرات رم است و تا مشخص شدن نتیجه تماس‌های دیپلماتیک جاری، تصمیم نهایی را به تعویق خواهد انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/140792" target="_blank">📅 19:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140791">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNAlzm6H_PvvzuCuzigODuLZuThjH2k2Ns7ND4VszjDcS3gdOn_wK1Pu-0CxIqNQXcVelxX9mpcjO8OimnFOZ7vcL4-CGL7Zpizb3UIv0mBVZdwiwT8B9bEluzNsugll0MI2i4bMtP7oTexw2Q9ivLpqPxwtqQ7gxnzUqGbiEjEIah9ol_Wz71ltoVX06XuT4ku_hiqfl4jfwxvJU4xic6oKAVSvf4Ur6S8zUmiOVHSVn2srtT0cmAbVxt08Gx4vXelEvn6-Ib5zxj9rZtayiGUBs5nkLRdGVyDNdtRoUmCFJ2C0G5ewdzb6oWVQEeDo1AVM7efsc5H5B05VnCnOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایوان به سرعت در حال گسترش استفاده از پهپادها و قایق های بدون سرنشین برای آماده شدن برای تهاجم احتمالی چین است و به شدت از درس های اوکراین استفاده می کند.
🔴
استراتژی آن ایجاد یک "چشم انداز جهنمی" در اطراف تایوان با استفاده از تعداد زیادی پهپاد، موشک و توپخانه برای مکان یابی و حمله به نیروهای مهاجم چینی است که یک حمله آبی خاکی را بسیار پرهزینه می کند.
🔴
چالش این است که تایوان هنوز باید سازمان نظامی، آموزش و دکترین خود را تغییر دهد تا به طور مؤثر ازدحام پهپادها را به کار گیرد و از جنگ الکترونیک چین جان سالم به در ببرد.
🔴
منبع: نیویورک تایمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/140791" target="_blank">📅 19:19 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140790">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CElPje8IPoLSt0VSWjZjUflhf8QW8CQp4bRbuPDbphOxqC57j6A8A5VE8YPPNctEyVMdDxxSG8vUc2pt662Cu3GGZOYZUp_2gRrSeaFX9fxw6ptm5aPYrUsnAStegKYFpP3ODxS4xhXXeVfd8zPKmNM80iQmjnlGOqriw8jYMb_t0dmky9H8TqG8OXOFzz_I6KakMMW8WkgppCpzo8KV0P9XFOIJQULGOrvLon752N_Y11v-A8oHM0D9ZBh-oMgzKqK0ZIJo_5JFN7mcd7xBSlzLw9EejXOuR2NrBGNMqNg2gqGPQoFKVQiWvaAqpWNM0DauxbEXJPCYT9pZEN-oTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: جت های جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در آسمان خاورمیانه گشت زنی می کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/140790" target="_blank">📅 19:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140789">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ed1e486.mp4?token=FXNvlpu5iIh-37WciYMMWpzGcf4_jHo9S562iIHRKWOZ3O2lGmdN2phc3AWLo4MPD1x4dIJpVxCHgAv8L9UI4NcjMEVs6qnjBCAz9cLj917rWScNt4BAt6v-LtjnBd9-2Hm1lg-TTzI1O-zrappC5RJ3nODL5Pi9GH0FyTsPMX_ogTFRv6WUtWJZ_O8I-T4SdM3XNE1o7D6E5qulaLVMLnKIB5bDIWsT97VYfpN8PSUUVeDii_-rZjBbJpncIVzI-f-5vHt8ybgoDiZWHzRFTfZaqmnpnXFdj8f6UJHt76ffJR9JaKSY_X702c4YHSIjhzlzVWuXQ8EYqwMk909P1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ed1e486.mp4?token=FXNvlpu5iIh-37WciYMMWpzGcf4_jHo9S562iIHRKWOZ3O2lGmdN2phc3AWLo4MPD1x4dIJpVxCHgAv8L9UI4NcjMEVs6qnjBCAz9cLj917rWScNt4BAt6v-LtjnBd9-2Hm1lg-TTzI1O-zrappC5RJ3nODL5Pi9GH0FyTsPMX_ogTFRv6WUtWJZ_O8I-T4SdM3XNE1o7D6E5qulaLVMLnKIB5bDIWsT97VYfpN8PSUUVeDii_-rZjBbJpncIVzI-f-5vHt8ybgoDiZWHzRFTfZaqmnpnXFdj8f6UJHt76ffJR9JaKSY_X702c4YHSIjhzlzVWuXQ8EYqwMk909P1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بت هندیا که نارگیل رو براشون نصف میکنه، و البته نصفش رو هم خودش برمیداره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140789" target="_blank">📅 19:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140788">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
اتحادیه بنکداران مواد غذایی تهران: برنج موسوم به «آمریکایی» به‌صورت قاچاق و از مسیر عراق وارد کشور می‌شود و فروش آن ممنوع است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/140788" target="_blank">📅 19:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140787">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
یمن: عربستان اینترنت را قطع کرد تا فیلمی از نتیجه حملات منتشر نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/140787" target="_blank">📅 19:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140786">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d976e17c50.mp4?token=kJXHwSfaHRcLQUx2N2_iVF_R8UayzoKu3_rb6MIxjrR2mzsSVJtSsA3_4426TJB6GahTuM5tokHh7EIMmRxM47TBcyPqT_loP4BvBpLx9eRA8J5U7x0a8B6rantfauCNO-un2ezNMNC0ei8HhcvpktNbK0qvbr1UeukiT2lTtMwgNMEf3Sy8dJ4Q5kC1LVGEXStvh09H1GGnHBDTM8oz2XlheF9-MXPrAh1DLhmx1rSsbslhTu2vYmGmY5ZPA1w_bWsyDYFhTUL-O8o4Ic0RqEqICQaJxptIXF2RjYFW-W-9JkIrklNl7zn2b9Urwkc6eSCK3uQBenZc7BIb1n81HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d976e17c50.mp4?token=kJXHwSfaHRcLQUx2N2_iVF_R8UayzoKu3_rb6MIxjrR2mzsSVJtSsA3_4426TJB6GahTuM5tokHh7EIMmRxM47TBcyPqT_loP4BvBpLx9eRA8J5U7x0a8B6rantfauCNO-un2ezNMNC0ei8HhcvpktNbK0qvbr1UeukiT2lTtMwgNMEf3Sy8dJ4Q5kC1LVGEXStvh09H1GGnHBDTM8oz2XlheF9-MXPrAh1DLhmx1rSsbslhTu2vYmGmY5ZPA1w_bWsyDYFhTUL-O8o4Ic0RqEqICQaJxptIXF2RjYFW-W-9JkIrklNl7zn2b9Urwkc6eSCK3uQBenZc7BIb1n81HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز جنگنده‌های ناشناس در آسمان استان ذی‌قار در جنوب عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/140786" target="_blank">📅 18:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140785">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نیروهای مسلح روسیه در ماه جولای 195 موشک بالستیک به سمت اوکراین شلیک کردند. بر اساس کانال های نظارتی، تنها 29 نفر رهگیری شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/140785" target="_blank">📅 18:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140784">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزارت کشور اعلام کرد رجب زاده شهید نیست و ماجرا شخصی(سر داف) بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/140784" target="_blank">📅 18:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140783">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏
👈
دادسرای جنایی: جنازه حمیدرضا رجب‌زاده اطراف تهران کشف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/140783" target="_blank">📅 18:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140782">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رئیس اتاق تعاون: خبر خوشی که برای مردم دارم اینه که تا اخر مرداد سود سهام عدالت میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/140782" target="_blank">📅 18:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140781">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c72250bd7.mp4?token=snZ46Y83H48sZlKRN26NceC_0SBeK3kG01BSCI14T7v7YQ6BnN8o2vexVnJ_CekcUCTRLoWV4WkVpev6_YAS6vU5DI-1TA5f9FqL_Gr3nTcde4s8fwqvJVTNME9zg40Gm8KyAbK_5rA0MQFR9UctEtHu9KKbnMG0EMXPKuDyPkUwIhZj5pNVU6-kWaq_A4VacUF9SMt_TH3DBwouskNdDZJ4N50Dm3wHEnT4IIcdbXPYR2PUn1g-qEmm6Faxj0Pn4-woKx-WhPInKrCL1eTU5QmRVobYecxlqdtc2_PQ95m7ckEuJuOgsRGgQ2RJZEE72pNaDlv8IT0sB-rbbtAlYCxzzFxgHZpSGNSJvFg1jcF4M-MNHJrkFCotSKTrPBcZB9fM1cKG48bpjgzPXncNOW-eEqnlU86oGeyIu3RmqdFiX4QG3x6TPoZ9Q3mLW1xYt6tsiwGDDIvjcUcrHrC0I4KZvQ99-NlIxQNw05lUAsENbJJjR2lQ1B17xh6ZmWFM_CqhTWrlX7rfQUz33kZSxG2Qy2-J4t_2GL0tBT-2HKiOG56Nsiq1VLiMa-adIAoq-EmwlkVmQYqEmAToAz8wJIOs_zv0MRlcKAxSSNd05ojhqS5ZESpbf2mMHGwjI8jHaR2ej2YZSD7aN27VICWPxmq_DIH1VKyvPCeZ0DdGoFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c72250bd7.mp4?token=snZ46Y83H48sZlKRN26NceC_0SBeK3kG01BSCI14T7v7YQ6BnN8o2vexVnJ_CekcUCTRLoWV4WkVpev6_YAS6vU5DI-1TA5f9FqL_Gr3nTcde4s8fwqvJVTNME9zg40Gm8KyAbK_5rA0MQFR9UctEtHu9KKbnMG0EMXPKuDyPkUwIhZj5pNVU6-kWaq_A4VacUF9SMt_TH3DBwouskNdDZJ4N50Dm3wHEnT4IIcdbXPYR2PUn1g-qEmm6Faxj0Pn4-woKx-WhPInKrCL1eTU5QmRVobYecxlqdtc2_PQ95m7ckEuJuOgsRGgQ2RJZEE72pNaDlv8IT0sB-rbbtAlYCxzzFxgHZpSGNSJvFg1jcF4M-MNHJrkFCotSKTrPBcZB9fM1cKG48bpjgzPXncNOW-eEqnlU86oGeyIu3RmqdFiX4QG3x6TPoZ9Q3mLW1xYt6tsiwGDDIvjcUcrHrC0I4KZvQ99-NlIxQNw05lUAsENbJJjR2lQ1B17xh6ZmWFM_CqhTWrlX7rfQUz33kZSxG2Qy2-J4t_2GL0tBT-2HKiOG56Nsiq1VLiMa-adIAoq-EmwlkVmQYqEmAToAz8wJIOs_zv0MRlcKAxSSNd05ojhqS5ZESpbf2mMHGwjI8jHaR2ej2YZSD7aN27VICWPxmq_DIH1VKyvPCeZ0DdGoFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور دیاسپورای اسرائیل، چیکلی:
اتحادیه مکه یک تحول بسیار خطرناک و نگران‌کننده است
🔴
عربستان سعودی اساساً روی دیوار نشسته بود. آن‌ها قبلاً یک توافق دفاعی با پاکستان داشتند، اما به محض اینکه با ترکیه که در تقابل مستقیم با ما هستند و این تقابل می‌تواند به ابعادی با پیامدهای بسیار جدی هم در مدیترانه و هم در جبهه سوریه منجر شود، بپیوندند، این تحولی بسیار، بسیار بد برای ما، برای اسرائیل است
🔴
این موضوع نیاز دارد که اتحاد خود را با یونان و قبرس، امارات متحده عربی و سومالی‌لند عمیق‌تر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/140781" target="_blank">📅 18:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140780">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq266KtrCujlKdvseh6WNFxZE97Uubn1BGheWx9kYMYcfoqjt94dv04nFHAVJXN53l2OFwcmcKLbjheNkc9U5o7rJ-euiEDVPDTohJ_C4G9vBeZ0NBgXkdapXwfQEtEaET5Hnr_FrX-n-7W1K-5UahOS4u4HbF5oxigBDM68vN88nCgQENX4RXFS0qU1JK1gOKJo4RJe1VX2J0UaYFvUhlF7e4NsPqd7q48fZAGCTGbLW_fICqIo9yGiJxDaDKedYealh0QWs31BGHOkuiRc8AWDJdykqoORfc_iIRob5gBJFkoU7qzz2HZJaeg4j3T5T0U5T_vYtCES62sgf7vG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر ۲۳ سال پیش روزنامه کیهان
🔴
از اون موقع تا الان منتظر انتقام بزرگ هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/140780" target="_blank">📅 18:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140779">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ریانووستی : انصارالله یمن به هزاران ریز پرنده FPV فیبر نوری مجهز شده است تا از آن ها بر علیه مواضع نظامیان نیروی های تحت حمایت عربستان سعودی استفاده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/140779" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140778">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrNuAtQBefUNe933-191NGxPKiHRwSpYFnYk5wbwPUIJN6DVBT1VgazFuDCice4iesWBY7v0aJ_EuId2M6mR-2zdTsz2kgVePxvcnUw8ndzXYwRftpE_pTJiZt6r5wtNvmKoTWDmwI7L5IboOTAWtZXFoFtVNWNoEhZV7r7pbSZ-NiylN6PPrny6E8cI3DkGuLhPTAHoZhG-Cdgo2sTStdObiaRqfqLKCQ5a_7NILNiRwd-NzvH9iYTINlxkX9eltQCb6LPM6brSmuU3vZWMfN4LKxRyZyOyuU9VmuqQ7w9MfQSsyNkZcoB_UCRy4pumw7JULgUIqF2sCkFEoc7Hmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
دادسرای جنایی: جنازه حمیدرضا رجب‌زاده اطراف تهران کشف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140778" target="_blank">📅 18:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140777">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پاپ لئو بار دیگر خواستار پایان جنگ اوکراین شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/140777" target="_blank">📅 18:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140776">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEfKfbq4p1XuSg_5NrNYVdMl6lGLJ8T8ZrWuTCGfZ0JvS-0DhuQZmCnFTljBSKHVuGT6LeWuxTEN2d_atk0eMLSsu24MYMeiBlD4IlBE13IViyt7RiRmxMbmoopT3rwQXAAs3G9eGre-GHWG9oUZiPccT7Lt6WrPPr11j6X5OsS9rkJBkogxElMgLjHD2o0nGiVaSsPDhsUh9tCSFLkBluhQ_B1xUGd-dqSopiDpIi5tgKjVSS5oHSvFA0Gs5Qm9hz-7IPhqRkojhBiZq-QbPrDRaDixMahUT7dzy4o1l3xtHsJWWTtZCN9ZIIgK_9tPn6pAUlFWDPGCZhsen5riiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره : مارکو روبیو، وزیر خارجه آمریکا، ترامپ را «رئیس‌جمهور صلح» توصیف کرد و از نقش او در پایان دادن به مناقشه میان ارمنستان و جمهوری آذربایجان تمجید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140776" target="_blank">📅 18:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140775">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10edf0d4dc.mp4?token=t_cE1Bf8SLyS_fYGSEvIX72kgLicFK13EjLFsPFzC817BTEwq0iXG-PkZwliDXz5EXrxLqqi6GRrSOzC5WVtNDCUMuqObdy4XIV-B94OiK6SKqUb1SihTbSn_y-AtpQv7FUNlWfNJ3NMbZtg3dOBUkyAoeDNPc0Jas22-8I_Q4gu7zv2qZD6EPFFNVm0wq4tG13X0Qz6qhqPBUOVQtl6yBvAWqMCUMaZMZ7jPCLUaaBqMLTHyU5UNKg778PgMRMLdJCBiatWm3yumioukSOWpYOtRIAOSgNpNgBkvyaaredY6dBsyA69E_Kq7E2mUMz65btNzMLfKAyPENOaL2HAVjfBKhiZGAS1v0vx-xfMLMgrZrVJdl-5FHPGlxUiz_teo8iVtLzXgMUI0V67tHPr9Z_6lzeaYhKk5ZD34ItCLmAEGmQYaljd7AkOV51wRLRsKHGsGCXnQ_EmZi9T3OpGFWFUBFXxcBy1q9Wn4BSH9oYVnm4472STzKGbphWzDHlXOITAdQe09qvcN0TcOJ7jynp_zH6dszToaUiumOQSxwAQOnEbKbX450RiUgVTrM88_7ZKucW1-hj7zJmkEjJKfplOCm9IZJQ87lUq4IgPVrOSjW-EliMbm9G5Q_s5EbucrRbQ8F-V7CgoXVQ21J-KHKmwyxIN6AX0CsogE_y7K8c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10edf0d4dc.mp4?token=t_cE1Bf8SLyS_fYGSEvIX72kgLicFK13EjLFsPFzC817BTEwq0iXG-PkZwliDXz5EXrxLqqi6GRrSOzC5WVtNDCUMuqObdy4XIV-B94OiK6SKqUb1SihTbSn_y-AtpQv7FUNlWfNJ3NMbZtg3dOBUkyAoeDNPc0Jas22-8I_Q4gu7zv2qZD6EPFFNVm0wq4tG13X0Qz6qhqPBUOVQtl6yBvAWqMCUMaZMZ7jPCLUaaBqMLTHyU5UNKg778PgMRMLdJCBiatWm3yumioukSOWpYOtRIAOSgNpNgBkvyaaredY6dBsyA69E_Kq7E2mUMz65btNzMLfKAyPENOaL2HAVjfBKhiZGAS1v0vx-xfMLMgrZrVJdl-5FHPGlxUiz_teo8iVtLzXgMUI0V67tHPr9Z_6lzeaYhKk5ZD34ItCLmAEGmQYaljd7AkOV51wRLRsKHGsGCXnQ_EmZi9T3OpGFWFUBFXxcBy1q9Wn4BSH9oYVnm4472STzKGbphWzDHlXOITAdQe09qvcN0TcOJ7jynp_zH6dszToaUiumOQSxwAQOnEbKbX450RiUgVTrM88_7ZKucW1-hj7zJmkEjJKfplOCm9IZJQ87lUq4IgPVrOSjW-EliMbm9G5Q_s5EbucrRbQ8F-V7CgoXVQ21J-KHKmwyxIN6AX0CsogE_y7K8c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدل ال‌سیّد در پاسخ به عکس ترامپ در شبکه اجتماعی «تروث» از او و همسرش با این کپشن «دو آمریکا بسیار متفاوت»: بله، او حق دارد. آمریکایی که در آن حاکمان شما دو نفر هستند که از یکدیگر خوششان نمی‌آید اما برای کسب میلیاردها دلار از شما با هم متحد شده‌اند.
🔴
یا دو نفری که واقعاً یکدیگر را دوست دارند، با هم پنکیک خورده‌اند و می‌خواهند برای ساختن آمریکایی که بتوانند در آن خانواده‌ای تشکیل دهند و بدانند که آن خانواده چیزهای خوب را خواهد داشت، با هم متحد شوند.
🔴
من و سارا از یکدیگر خوشمان می‌آید. نمی‌دانم در مورد بانوی اول و رئیس‌جمهور چه باشد، اما از آنچه شنیده‌ام، راهی پرچالش است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/140775" target="_blank">📅 18:22 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140774">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
به گزارش بلومبرگ، دیوان عالی آمریکا با مشکل کاهش اعتماد عمومی مواجه شده و حملات دونالد ترامپ به این نهاد، این وضعیت را تشدید کرده است.
🔴
این گزارش به افزایش نگرانی‌ها درباره جایگاه و اعتبار دیوان عالی در فضای سیاسی آمریکا اشاره می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/140774" target="_blank">📅 18:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140773">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnuR6XOnUTArQ0D0zMHqHeOaZN7MvWRdXib_hNoj4sRusO7Q0NGrnI7dk5BWMSYTa6asUheb5Bl04MBB5CEOP10PP3nObSMFzHyX-sp68Jc7YEtGKhakJ24aWjmH4Xo6MzyjkoX4U_D3i0-zAn1JC4tRNV50OgoF4LfB4946GwIw1IDB00IG5OUIhJCUv07JKO2Kmz2sEC85Tq1v1itslE_DEW1yd4vIIw00QoFUjdByVOs-HpvSooTCp6szX8Svz6wK_C2kV5iOQrPJonCOcCYw3ngaYuFx_4SlUAFZE2y9M-KOojHfTGRLWukLJyRZjD3Z8WPEPRKaGcfqrGW_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر خلاف اخبار ضد و نقیض، سعید جلیلی از شورای عالی امنیت ملی کنار گذاشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140773" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140772">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7yPDacwKA0r9GDJnhJqvCy0Hqsijyh_UbPKy6UOfg3yZjzRh7SJYZoOFE_oPjrYjKX06rBf6v-Q80QdoA_rgmlUQHDGxdEam85vIPtomS6NF1mMGNNXmBLMtqyxk8DrBNzJonR3Mn4nKMepYX1eo2XuimowIIM64VUVgV3o6IfCSqMAW3xIPSVz2AKpa5QUtlzbu5XCH8-6EHavxQ39AGS2_OsXZa4vqPDcWzkYYiT89sUh3WIV5wpKaRdnQ6x2wbBqliI3xKAdzXq3VOIn_R_2N_aiPntz-6rl7CgHmngnljnPKOhIfEzjpYr38vx73w2jlxHQE2A3U74PElvN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید
ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/140772" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140771">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
حماس: به اجرای مرحله دوم توافق آتش‌بس متعهد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/140771" target="_blank">📅 18:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140770">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کمیسیون امنیت ملی با اکثریت آرا لایحه‌ای را در مورد تأمین امنیت تنگه هرمز تصویب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/140770" target="_blank">📅 17:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140769">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رئیس مجمع تشخیص مصلحت نظام:
به هیچ قیمتی از موضع خود درباره تنگه هرمز عقب نشینی نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/140769" target="_blank">📅 17:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140768">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c731bac8ad.mp4?token=JmDganwdirhk5z27a_7sMbqGorXIO0pbJ9njAZTl4QgyBulmP6IApoxNB6PoXoO-rA8EzQc_FnnvEu9z9XvmWNnseq_Px5lRKM2Vo-kiLiOr0TzAUmvTlH5OhYrPzgrhB0ix6KEpT1RGG7lkApNjc9MuGNBXHFTWrYeGuLIuWP7ObNQzG_vCxwwzmzpxwp6e8DhIJM-ocz7DPBifPIY-oXMLWQiuY426ph2mn_Gfv5_IVEAy5Vz8F5Quq_-mGxxsnd2JFmAEW3Xp17AJployeHVd_K2SuZkTX5mjx5-8ozyrPYd3SUkCD8aiZFj94amNnpRz_IEjkYNpZCIQ2XAwnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c731bac8ad.mp4?token=JmDganwdirhk5z27a_7sMbqGorXIO0pbJ9njAZTl4QgyBulmP6IApoxNB6PoXoO-rA8EzQc_FnnvEu9z9XvmWNnseq_Px5lRKM2Vo-kiLiOr0TzAUmvTlH5OhYrPzgrhB0ix6KEpT1RGG7lkApNjc9MuGNBXHFTWrYeGuLIuWP7ObNQzG_vCxwwzmzpxwp6e8DhIJM-ocz7DPBifPIY-oXMLWQiuY426ph2mn_Gfv5_IVEAy5Vz8F5Quq_-mGxxsnd2JFmAEW3Xp17AJployeHVd_K2SuZkTX5mjx5-8ozyrPYd3SUkCD8aiZFj94amNnpRz_IEjkYNpZCIQ2XAwnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
طوفان سهمگین دلفین به چین رسید
‏
🔴
تلویزیون مرکزی چین از وقوع طوفان سهمگین «دلفین» در استان «چجیانگ» خبر داد.
‏
🔴
حادثه‌ای که با وزش بادهای شدید همراه بوده و وضعیت اضطراری ایجاد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/140768" target="_blank">📅 17:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140767">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c067f64333.mp4?token=JwKM4KImDTx3lNZU6hFYmja-N2N9G3uNs4GCMEgvFoqNaptxQuhd2ED1DuheXNMGwrEoSi9EVXTe8bBSkKzoE39VPpdpRbfh9ZExoT41T2d0Twp5iMy2j7rZ6nLt4KngCq4PSyJR2KPTVTQNg8mWa_7rkCMJYYRXoa8S37SUyK8CMN_LXkzRqYaxDUy3PUKlxVm4iXLCsrUKF3g_rhqA6gKumTMq9HVBQknCsDx_HoO5cnnKI__Nb88aA5dElSIEHBDSTvrbqN2bmgsHRgd6CElU9aXsnPdD5a7CxJjranI1T_nsCcy_t5s038dd3tYpZN3FOrYJ_fylZ7YWOXJ-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c067f64333.mp4?token=JwKM4KImDTx3lNZU6hFYmja-N2N9G3uNs4GCMEgvFoqNaptxQuhd2ED1DuheXNMGwrEoSi9EVXTe8bBSkKzoE39VPpdpRbfh9ZExoT41T2d0Twp5iMy2j7rZ6nLt4KngCq4PSyJR2KPTVTQNg8mWa_7rkCMJYYRXoa8S37SUyK8CMN_LXkzRqYaxDUy3PUKlxVm4iXLCsrUKF3g_rhqA6gKumTMq9HVBQknCsDx_HoO5cnnKI__Nb88aA5dElSIEHBDSTvrbqN2bmgsHRgd6CElU9aXsnPdD5a7CxJjranI1T_nsCcy_t5s038dd3tYpZN3FOrYJ_fylZ7YWOXJ-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خانعلی زاده: در جهان پس از ۲۰۰۸ اساسا تحریم اصلا معنایی ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/140767" target="_blank">📅 17:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140766">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/880188eb1c.mp4?token=jvgKO3is08D8Io0JbC7bKTeR310W1obw-5MT1lVYqQr9NWixmIJYvxxplOuTbCi6jR0FcymzBDhJN7E84wmLvLt8LwyHYBsbrNYa-Qb4pxN2kCMFi3ceJI7EWWRoLKlnlkINT3yF_MUOoh7fzQN-9XVEI141CbeO11XKrDEHmIMGIwZ0C8ejismFEMsyyc8CkHvgrb4wlGd-EHc0RR3Swj4jHLgg9cEN0L0_vVY-Vxfyi1j6rfgn5d-VYAqteq3p3PzUnJXiuZDWOdJHCVGTL2swD3WpmBwpCyor7FsMSy-rJ6RVHZPRutUihE8-seNWnplqoNiGSy09TJNMYIHHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/880188eb1c.mp4?token=jvgKO3is08D8Io0JbC7bKTeR310W1obw-5MT1lVYqQr9NWixmIJYvxxplOuTbCi6jR0FcymzBDhJN7E84wmLvLt8LwyHYBsbrNYa-Qb4pxN2kCMFi3ceJI7EWWRoLKlnlkINT3yF_MUOoh7fzQN-9XVEI141CbeO11XKrDEHmIMGIwZ0C8ejismFEMsyyc8CkHvgrb4wlGd-EHc0RR3Swj4jHLgg9cEN0L0_vVY-Vxfyi1j6rfgn5d-VYAqteq3p3PzUnJXiuZDWOdJHCVGTL2swD3WpmBwpCyor7FsMSy-rJ6RVHZPRutUihE8-seNWnplqoNiGSy09TJNMYIHHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند پهپاد آمریکایی از نوع MQ-9 که از پایگاه هوایی چابلی در جیبوتی به پرواز درآمده بود، سقوط کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/140766" target="_blank">📅 17:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزارت خارجه اسرائیل:
در تابستان ۲۰۲۷؛ ایرانی ها میتونن از خود ایران برای سفر تابستونی بیان اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/140765" target="_blank">📅 17:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad7777df6.mp4?token=gglIJ1A2UdYAttWyFW6F0OzJZF8I0ur9yl57o7Qu82KBJLMOpEHuQ1KwSdz_zK62C6Otd52R8AAyC4OIHWMpkO9j5Bq5Q5g8XuBHSPrL3aBggyBjlcRHDgPy7rzlh1NVQC2ZPQrWXA84xbtcm8oG0CmhmbENALmzyrkZuQVtCC4-8u2Aug4q56vTqbk8A_qC85-uImbQw7BBrJjbuWLHqriqsspslSk3Xgow4jjW_9BKvz3so2nWKB2Flieof1JNUhB5XPOPDl4o757XPuLXvvzSYo36wYppCcxHKn2jzLKPKQ-Zl8JmCPbc28-T4KrdDd9cZYXPHNZMVz4XVNW08w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad7777df6.mp4?token=gglIJ1A2UdYAttWyFW6F0OzJZF8I0ur9yl57o7Qu82KBJLMOpEHuQ1KwSdz_zK62C6Otd52R8AAyC4OIHWMpkO9j5Bq5Q5g8XuBHSPrL3aBggyBjlcRHDgPy7rzlh1NVQC2ZPQrWXA84xbtcm8oG0CmhmbENALmzyrkZuQVtCC4-8u2Aug4q56vTqbk8A_qC85-uImbQw7BBrJjbuWLHqriqsspslSk3Xgow4jjW_9BKvz3so2nWKB2Flieof1JNUhB5XPOPDl4o757XPuLXvvzSYo36wYppCcxHKn2jzLKPKQ-Zl8JmCPbc28-T4KrdDd9cZYXPHNZMVz4XVNW08w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در جنگل‌های بهشهر؛ هیرکانی دوباره می‌سوزد
!
‌
🔴
شعله‌های آتش بار دیگر بخشی از عرصه‌های جنگلی مازندران را درگیر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/140764" target="_blank">📅 17:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPQw6zTgMZSOzFfjONlMlpoShN54Xr625GgTPztNceUUCwhW0y9UkTsZfpZgnYtwcbBM25BYaAWs8mpStbxy1UX05YhNzl8tr0B0hzYXei6IxDoq0KByla81TRLauGuIPJiSBF63ajP0_zj5ZO784e0Sx2yeRFfTDjrzh22Yli3wAnVXe5Ycl4gPj7gIAlpl0aBNicRBoCzeXZ8pxyVdR1Tyqv8boXkVp6Yt9_Gh1kWTBH9OJ1zbDqLvmLgcazID6ZBnkOpXD74Q4npd4ljKjBq4lDCkThvT8CS_OkHXZWxSko8Z36XA5Iil6-FPjRSd0x8MZCKBKgeVtBzeANDuLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به وال‌استریت ژورنال:
🔴
به تمام اهداف نظامی خود در ایران دست یافته‌ایم، اما گزینه ازسرگیری جنگ همچنان روی میز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140763" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4a83f3cc.mp4?token=hj0MktF_2S6Q0nAmmCnxrtJIZo2-a4KVC8o4e1UYMUrkGpL_FFw6GiE50zQNpFQkoqmXgioElLds4VUyntIolKUpUlsQdGH5razq6ehP2OlxRWCXV9HsbZD8b4F7cP-wai5N21lN0UOE1EWSfHiLnBi3hhRI2yuPnKIEH676hO9FNEle06zkbXr2vDyaq98ksZYV8UMtg_nDeVXMCuT84lNwXY98bkSx8zT0MQBM3HRtqgSC_xiztWaMeZ2KH3ttyHFC3b5lxNnScVHxPSlpC7__t_DDLKRN45Xl3e7UDIi7SJDldfwAP3RuwNNt5cEYBy0FR4gIHWrNxGKuysl8fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4a83f3cc.mp4?token=hj0MktF_2S6Q0nAmmCnxrtJIZo2-a4KVC8o4e1UYMUrkGpL_FFw6GiE50zQNpFQkoqmXgioElLds4VUyntIolKUpUlsQdGH5razq6ehP2OlxRWCXV9HsbZD8b4F7cP-wai5N21lN0UOE1EWSfHiLnBi3hhRI2yuPnKIEH676hO9FNEle06zkbXr2vDyaq98ksZYV8UMtg_nDeVXMCuT84lNwXY98bkSx8zT0MQBM3HRtqgSC_xiztWaMeZ2KH3ttyHFC3b5lxNnScVHxPSlpC7__t_DDLKRN45Xl3e7UDIi7SJDldfwAP3RuwNNt5cEYBy0FR4gIHWrNxGKuysl8fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: قرار بود اینترنت دیگه باز‌ نشه و همینطوری بسته بمونه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/140762" target="_blank">📅 16:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ در پی خاتمه جنگ با ایران است
وال استریت ژوزنال:
‏
🔴
دونالد ترامپ به مشاوران ارشد خود گفته است که ممکن است تمایل داشته باشد بدون آنکه توافق هسته‌ای حاصل شود، به جنگ با ایران پایان دهد.
‏
🔴
این تصمیم مشروط بر این است که تنگه هرمز به طور کامل بازگشایی شود.
‏
🔴
طبق ادعای این رسانه آمریکایی، ترامپ معتقد است که برنامه هسته‌ای ایران به قدری آسیب دیده که نمی‌تواند به شکل قابل‌توجهی بازیابی شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/140761" target="_blank">📅 16:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e03e0d9e77.mp4?token=evun4-8t8n9aoC45iL6oRQs-QuxI8-Ev2EonkvwkeRP-B0ZMPouY7D8s4fEu0qGuKTpuSwScoWJN7hyMJ99ThmvErsX6ekEqcFyL_IDFVg4_4ffqZB3l1rMN7upXjYQ7FJEMgtywno1agK6WAmAfQmzVfGOrFNXix5YwZzv0AHhSTqd8NNI_f9UlYBKY3qKi38XdrRZhl_u-hvAS0zRFS6sMpJOLPv9hPfyhbFqagBDJL1nI-VM46MSBAY64oXaNSVIEGv-5SMxA81Eq0thwSbbK1yvt0mjcCHbYFM_kRAPujQoegKQG0TEsLGZqFx4qjLpSRhwZXa3fWb3J-IWoC6cTXqd9KqhpK54uHDoRh_6_8ksbSGgw8_cy01Ag9A8DvCrXHIetKLR0E9LJexT6RBq3rOqU-sV9tK0xStaEOiOkysoljYD4yrtmp_HbINTfPFuH9kXdAZx8Z9Ty6GFy_yOkehIHuybPFW6iyepbD6LktnJzrpnP2D8H7JOqx38RmWv025QvQQ7VGlw8daCHYtgUzcYYOfb2D_xKCIZXDjxuwIzYckBzjCCwTuaolfbyUj5rvlDn53yu1rEGY2xOEDL7gq1pzKrCZj7iifMlGvcz1x5c7vB4PQ_jU5xx6wIdNBkEnSCf9IlBAzrprnvLm-8oiVP3rTq73nqVnTqXoe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e03e0d9e77.mp4?token=evun4-8t8n9aoC45iL6oRQs-QuxI8-Ev2EonkvwkeRP-B0ZMPouY7D8s4fEu0qGuKTpuSwScoWJN7hyMJ99ThmvErsX6ekEqcFyL_IDFVg4_4ffqZB3l1rMN7upXjYQ7FJEMgtywno1agK6WAmAfQmzVfGOrFNXix5YwZzv0AHhSTqd8NNI_f9UlYBKY3qKi38XdrRZhl_u-hvAS0zRFS6sMpJOLPv9hPfyhbFqagBDJL1nI-VM46MSBAY64oXaNSVIEGv-5SMxA81Eq0thwSbbK1yvt0mjcCHbYFM_kRAPujQoegKQG0TEsLGZqFx4qjLpSRhwZXa3fWb3J-IWoC6cTXqd9KqhpK54uHDoRh_6_8ksbSGgw8_cy01Ag9A8DvCrXHIetKLR0E9LJexT6RBq3rOqU-sV9tK0xStaEOiOkysoljYD4yrtmp_HbINTfPFuH9kXdAZx8Z9Ty6GFy_yOkehIHuybPFW6iyepbD6LktnJzrpnP2D8H7JOqx38RmWv025QvQQ7VGlw8daCHYtgUzcYYOfb2D_xKCIZXDjxuwIzYckBzjCCwTuaolfbyUj5rvlDn53yu1rEGY2xOEDL7gq1pzKrCZj7iifMlGvcz1x5c7vB4PQ_jU5xx6wIdNBkEnSCf9IlBAzrprnvLm-8oiVP3rTq73nqVnTqXoe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمد جواد لاریجانی: باید به زور هم که شده غرامت بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140760" target="_blank">📅 16:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏
👈
الجزیره به نقل از جی‌دی‌ونس: آمریکا به توافقی درمورد تنگه هرمز نزدیک شده است که ممکن است در روزهای آینده منعقد شود
‏
🔴
نورالدین بوزیان، خبرنگار شبکه الجزیره در واشنگتن، به نقل از جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گزارش داد که ایالات متحده به توافقی دربارهٔ تنگه هرمز نزدیک شده است که ممکن است در روزهای آینده منعقد شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/140759" target="_blank">📅 16:13 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی صنعت برق: خاموشی‌ها تا دو هفته آینده به حداقل می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/140758" target="_blank">📅 16:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140756">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PGEY4mHQ73llDdd7KbhBy0SfAMvK3BceePNYGO9fNWQHPPerC0juBu7OHkg71EqqZ4Dz9alI90x1c285JmedYQDpvGgPnH5I-CbS5aTOPlURLHqCerHZpqMJUYc_MzBmmPVlCE-IzGzex-hhKzsgu_ZrIKlXCjolKbFXLHsSbqxVc6d9KIIsF8zfx6XoXTDibSErmLNv6ftSxEQcjxPCREB46ajyiGCMFFdPKA5S7lp90WJTrLjfKrlbzL0YY0joqOAREf1_UiQfowh2QoKaYEQRA0l4xIWklqdE1WE_lhbwzGHOqSbwLv8QMJzKmcbgzBQ0UYk4ZRYukFDlWHdxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XUjHSbyre33sljKjLwXZK_RSLzVpmuAR30KTUuiTSWXA4tObCdom7Ft4NCx_YDMGn14uXLMhUopLRRX4u9DtVVInQG455wQycx1fosxjcUKPTXTLb4sI5subD9LBFveu6CTEZcq4dYcxd_j-Iw3wICaen-4NC08nW3LAaDVrCFSVQvR1XdD7dAoRd7kSjx9uiRIaDB7sdgKlndRhXlezZS40jnfzRzIHcVz267E2OQDOQdfmgL3gtG66TbA0_7P9VEGUp5Su2KyIU0D_xy8T90cY0PYA6muS5jwgTAJ4Vti00Yy0OHQPijAhykuDqZJNOTKWM6ObqjP3gfCXtmKCYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت خارجه اسرائیل نقشه‌ای در ایکس منتشر کرد که ادعا می‌کرد داده‌هایی درباره سوءتغذیه حاد کودکان زیر پنج سال را نشان می‌دهد، اما این نقشه حاوی چندین نادرستی جغرافیایی بود، از جمله نشان دادن بخش بزرگی از جنوب لبنان به عنوان سرزمین اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/140756" target="_blank">📅 15:44 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140755">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAZoKIU_gzt3KPBM15TeQTxXq-N_bVnDpK_XBIOk5VcW87nTZcO7dyEaKQYc0dN3jxeYrnQMIMk-7Ea4dTBBvOPaogIGU5lyU4rA1TVBpzPnTWboICHq-qM6Tp1wqR86YGqJShvKfTp4rU--MtnzlCW3Fpyct3mtjJpWypEIIAC4-UKnyOQ2dafaykK4rdjCmVunfL8V0g7_MGpGX_dasA-rCIrs6ZF-cSEjwx5ODuQTYA8ZQK-GonMSIXGX1BHEhGpnEQ1SyMoziDeQkYLaKlwBzABINgJVlSGsZIhYfEDhnZ7iuio7VUn2MyhUhlCLv8kwXrUp49RLZCWJV7mMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خطرناکترین سلاح دنیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/140755" target="_blank">📅 15:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140754">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اولین شهید راه دختر
💢
🔴
دختر متهم: من با حمیدرضا رجب زاده در فضای مجازی آشنا شدم، اون مرتب به من تذکر حجاب میداد و می‌گفت درباره مسائل سیاسی حرف نزن.  ‏
🔴
منم رفتم به دوست پسرم گفتم، او هم گفت تو این مداح را به یه بهونه‌ای بکش یک جای خلوت، تا هم او را به قتل…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/140754" target="_blank">📅 15:35 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
