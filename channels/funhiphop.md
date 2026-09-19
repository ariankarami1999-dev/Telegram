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
<img src="https://cdn4.telesco.pe/file/QxE7PqKZKjyiuUKDsB4UU3hb_5-eUPSE4uIDIp4tcpRBQPhxzuXXz1Sm4hwxSc-r8ayUNxxLj-L_m8lFXOy_oqFgxHD1Bknso36ZTGCHGpi3dVe9h-xkJX3EIOXLDJkLpqXh4m2cWo9aTsvmRXNkJk0QjX1EC2oTfapCYrM_IGbX3AWdrD0Cv_38kkQ9db_-cF-J3ErP5CLseHGrodofHqMgKwDH-76tI3NuNzPbd-pcInOC49p4jEXGQvIsFi3uXFtbX7SaX8B4sYDTu2F1OP4KvINlWJV266QCz0MS0mPmN_s_2PKRWO9Fwh0eWLv75n0OBZsFqlZwObtCAkYPxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 251K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 21:48:15</div>
<hr>

<div class="tg-post" id="msg-83777">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کوروش وانتونز با استناد به
یک کامنت
،
دیس‌ترک خود
را پر پانچ‌ترین دیس‌ترک رپ‌فارسی نامید و به فدایی فحاشی رکیک کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/funhiphop/83777" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83776">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243abf4097.mp4?token=I6HGrFy20O_3JFhTyiInybZ3VsRYqXrlg0m5HZqgb2U4uhsrYoKYC5RiA6PBqvHwBJubVfY2QCg68r2lf5MfGeTAsxM7hNv_9D-uzLeUlgs3kveCtbA3-AVMAKT0APLWksNXtAWVrsOaEZHOFG3bYXeuOYuDkdDFMeSszRueiI0mcNDMFT-v-B11mcsC-jZBcAaHslRkGb27NLt-WKnIIXuNS6khKKe5T0TlbMYqHke5NExcxDMhwQ18jR0OgpGR8MhwKngCK3z5LHxZ4INacQ-692SZHB5tHBQjIKgTUaVpAPQzXJ-McGCxZYCRC5Y9_M6aMBncmu8oF0iW6DGtzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243abf4097.mp4?token=I6HGrFy20O_3JFhTyiInybZ3VsRYqXrlg0m5HZqgb2U4uhsrYoKYC5RiA6PBqvHwBJubVfY2QCg68r2lf5MfGeTAsxM7hNv_9D-uzLeUlgs3kveCtbA3-AVMAKT0APLWksNXtAWVrsOaEZHOFG3bYXeuOYuDkdDFMeSszRueiI0mcNDMFT-v-B11mcsC-jZBcAaHslRkGb27NLt-WKnIIXuNS6khKKe5T0TlbMYqHke5NExcxDMhwQ18jR0OgpGR8MhwKngCK3z5LHxZ4INacQ-692SZHB5tHBQjIKgTUaVpAPQzXJ-McGCxZYCRC5Y9_M6aMBncmu8oF0iW6DGtzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیانو اینجوری تهدید کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/funhiphop/83776" target="_blank">📅 20:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83775">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سهام شله با کون خورد زمین
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/83775" target="_blank">📅 18:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83774">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">برایتون یکی فرو کرد به ارسنال   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/83774" target="_blank">📅 18:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83773">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">برایتون یکی فرو کرد به ارسنال
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/83773" target="_blank">📅 18:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83772">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOs4zILyYDLEjDGmJtmEVgvuPuVLwljqDvo0Z2DaIkbfLjiYE3pyH9K3lpvywIO78aydrKRo-aYiI70pZwp8d9APZtVQTobDdCn-s-TkQUYHZVYwdB1SI5aLBGsIOZd8wIlJX8Zng_mD8GeRXY0BYJm0l1zT5b3XxhbN0GJgyZzVu3_WDMg7kTRaOOYrX6HYG8erPGjZOtcjqqJNnC-kHODaJE8BF4QLEQDg1JoMZa-J7Kjw28lbq0IBxk1TAc5V1rtrWxqD0Olwod0Pxd5Dmo8dO3gD7JsoA3bTFhpBGam2mVtMc0aMuELYaBFSKouHOXalBf5TNBxpyQjzqMmEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حافظه_تاریخی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83772" target="_blank">📅 17:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تاتنهام بالاخره گل زد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83771" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تاتنهام بالاخره گل زد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/83770" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHfA6_5GdcBwq8ZDrh4-LGQjMbRnzpdTnQm-4P3PrQuf-ryywtEwJ6EjAY_z8UCpafwRtPQcatpGiXESxPePcp2r-PYlNAaKK0L25vLJiuiL7bzSNd2syLUd5_cZUAe01Zu76vicI9UkEZ19g-ne-LM7deqpFoBsomBBbjoRmKh5wJjZ3PHDjAnRf6lqp9ygfcl7-i9usXBRsKyG8hbszB6-_3d6PZPR8r13rMiaEiq28Od7xv8NzdsRwxe7EWSaOWqTSugNkeX4scn311ICirCihuNHAMQ_0uydsTSfC7tHMfSELVQUioCHu8fkQqKLJufjRzJ_OPYPQcXA8i6Zyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83769" target="_blank">📅 16:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPCI9nyExxsrQtaa4A8eLaC6IHumbVDowHSg8t8xcL5tr5CQYTZ-t_nKBMQP2At1snDUynSSDHQeV5Bz0dr8XTv7SMfgNhfV_ayt5fX8w27WoyeZ5Gxirotzc3WOhhhK9cYvP4US3mVoT1JNfDU5CYFEkGAF89UQ0AZjKkh1p44CXW3lXCqoSttNUzaZ_YhHPlVyuXsiXMeayURBMst3LE2Dnom7U5PkOmyL6OdWA_4HVFh51gwV51gKU8rNE8fV_ecWD7xxqzNn0tG22JrBQA4yr7E9K1r1Q9GcgtLD20-n9wE1-L-Sa1RNIuQtmCVWPUz_cNZx5dfrA-wF_g8hIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83768" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6_OUpjr-BJNBRIEC1cblO1-8f9yr1KWgO4jYkbB9ENl3LNMtANebltl5A081XfL_VzuNM7c7SoFMun0CsgkQOPKpYysPNWAXsmhJCVQHMuNJNdQcl_C5A4RggaLT8QHI3DaB9AJlenjZMBM8NjNwFczEb0vNRrWy3XGvntLWE0S5cK87G2C_fN4dwchzp27NPsz2aW-02MHeGAHqzVpJempLB8nai2TKEgNWw28dq4Fq7Arey3DK8C8sm_TviHNhe7LAkdenNiorX5LNMsZuCHi43N25yAr3EgtPhBOH8bnNe769rSe5j82-eawT_kLcafDT8E6lVRDZbNnMZP6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر قذافی که 7 ماه پیش آخرین امید مردم لیبی بود و مردم لیبی خواستار برگشتنش بودن و داشت با رسانه ها اوکی میشد تو سن 53 سالگی ترور شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83767" target="_blank">📅 14:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">به قول امیر پارسا و ناگهان کص ننه چلسی</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83766" target="_blank">📅 14:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خروج رسمی امریکا از شورای حقوق بشر سازمان ملل.
آمریکا اعلام کرد عضویت و مشارکت خود در شورای حقوق بشر سازمان ملل را پایان داده است. وزارت خارجه این کشور شورای حقوق بشر را به ترویج ادبیات ضد آمریکایی و مماشات با رژیم های متهم به سرکوب مردم متهم کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83765" target="_blank">📅 13:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amzSkqjWkERT6Z417cHOORX_43GK1ufMAs-M5RYIfBrH-QeBhiHJZmDyn1D_g_roOc-ny9URwn4hSGIBJRWid3sgUo1xOMMG7TmwoywlK41EcB0n_0yG5q75FbyH_87COZehrxm5aYfxWznw14LECYZTks4ubzIAUG3CFaRvO7cCqscJh0juBTeoDPdp8JwjRia0wXm-RD8iXoWZHz4eGuAeCt0Tu9hGS4iocUtJkMygsElnEmNS372tdQcfW0W6vQ6IHO8gcW7GONXGlC4n7EexAlSk_qF9wjBEZiY4zSYFtEA71rKFRe9rkaCir10vhOoHkOMCnTxJ8Js4qszXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسدالله مادرت گاییدس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83764" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ff3a5a22.mp4?token=taEf8B2RCMRGLle8wCu18Zh6esDIfBZD1UOyBvZwevkbKe8ji9uVbRigHpwu5d64HbCbWTM9yYJGCPFgNnKL_5VmLyglgEStiiSbVCFjXV8GpY_kHzWoqA7hRP4lENWHBJPMHTG0K2M-eGNyZSdn6DfXE4p5J6yPWynlcXOnjeBwEkRYVu879A-n_FRsrREmNHzSSucfwvbHYsxevSc-SCyHM2IXLrCbxLaN25hl1ufdZnLUtpCnl0G1qZfxcvlq62huUZISWsPIKlHqxvi2q05reNZjezKfvhY_glEKBytQbS4S0FPNVj0d_nZ_doEgLslW4NkRMvBZdcW-Hq5CeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ff3a5a22.mp4?token=taEf8B2RCMRGLle8wCu18Zh6esDIfBZD1UOyBvZwevkbKe8ji9uVbRigHpwu5d64HbCbWTM9yYJGCPFgNnKL_5VmLyglgEStiiSbVCFjXV8GpY_kHzWoqA7hRP4lENWHBJPMHTG0K2M-eGNyZSdn6DfXE4p5J6yPWynlcXOnjeBwEkRYVu879A-n_FRsrREmNHzSSucfwvbHYsxevSc-SCyHM2IXLrCbxLaN25hl1ufdZnLUtpCnl0G1qZfxcvlq62huUZISWsPIKlHqxvi2q05reNZjezKfvhY_glEKBytQbS4S0FPNVj0d_nZ_doEgLslW4NkRMvBZdcW-Hq5CeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مصدومیت خوان گارسیا فلیک داره رافینیا رو تو پست گلر تست می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83763" target="_blank">📅 11:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7124a1535.mp4?token=XRqy1Nw7c9f-fpb48JWF6f4GkKwlmX6aDd1-ntg9QWagDcFyt0vibBDAm_nAh0JeJdP8SV9p6721zBs5uVYfq7GKjxPu3xbqg7AvePoo3xczfuMgZoRRBIzfdhieA1nRI2jD4XKnGAYVC0inZMHSD7nic6wP-nlKhY1PJIwioeu9a0l20sawicBVZv4dbs6HETdKs9F-bSBdvy26YuNBAWTo3T2FZU8Ak3SP-mYxNenbZP6XQSrj-n1P_6q-zAG3N-0-7e1ykloaJ-gG2E8H31JuHfo8F9BqdzTJGuQIiU5P-Man0CcaLcUwoWIMHFixpnyjbPee_hr5jInjGhL_aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7124a1535.mp4?token=XRqy1Nw7c9f-fpb48JWF6f4GkKwlmX6aDd1-ntg9QWagDcFyt0vibBDAm_nAh0JeJdP8SV9p6721zBs5uVYfq7GKjxPu3xbqg7AvePoo3xczfuMgZoRRBIzfdhieA1nRI2jD4XKnGAYVC0inZMHSD7nic6wP-nlKhY1PJIwioeu9a0l20sawicBVZv4dbs6HETdKs9F-bSBdvy26YuNBAWTo3T2FZU8Ak3SP-mYxNenbZP6XQSrj-n1P_6q-zAG3N-0-7e1ykloaJ-gG2E8H31JuHfo8F9BqdzTJGuQIiU5P-Man0CcaLcUwoWIMHFixpnyjbPee_hr5jInjGhL_aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اشکان شادکامی میتونست باعث بشه این کصشر قابل گوش دادن بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83762" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss3JJz19_s_EuhBQ0YPLz0QxvtlObRHvn5-i8jHsLDvvM0QfmFAvFrsOWfdSslXA7lYxfqNiU9bt6fmZvay_JG45TL8nDYPFVyW1bQ1gHVhdY5dp-8vJf3glCTMJ7Bn0GRViNrQKfBWPMdQBAb5Hq33AIy0NDwyn8MpQ3lDFbrP_MnVoNbBFe2Gw3n3llow9Eb_tfVTY_msUkAbWv7ged1ACECCBrBSN6fZhl4riUzwIITwrn-gjapIeUydfOyB0pg2exqxKtLArd9qgyAS2eCEciRi7w0cPZTFMagfvVMbmbKS_oz2xS7MQV03FYGK1EwFMFTYYejxyEVS2TIDsDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس شیر ایرانی رو بعنوان "بازیگر معروف هالیوودی" معرفی کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83761" target="_blank">📅 10:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4_So9p5PRSD9RSV9dFc_6ezsPTlDq3nwzYDTjt5pD5WVScYgOaBzE30YXruYdFdDR5LII1FBzmFuXaZIXeCH2dCgxsYWs96uZImWZVdoSWtP_Impyf1t33yoceZKg7ATpxAk7p3bWWoU61t-OM2tXWcMn3BV7XWDpfJ_rMiZCxmHOwWm44qm0VIfHAF__9NjVXRNgGa65fOcr0zrZWGvbcSfXUMv1ZgYMSBVMiQn3eGa7iATfTUzca-StaJNLJBiIXDltdHAeKoOHCTHA4XpMRu_NSw3SNG2gR1kAsDtFq-M78FkBjsiF5ndvPK6yrxq_I9TmW6ZHQpySDH0n2Jvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
سویا - بارسلونا
⏰
ساعت ۲۲:۳۰
🌎
📲
اتلتیک بیلبائو - دپورتیوو الاوس
😀
ساعت ۱۷:۴۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R28
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83760" target="_blank">📅 10:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">افزایش قیمت بنزینم نتونست صفای پمپ بنزینا رو کمتر کنه، کونمون پارس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83759" target="_blank">📅 09:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این امیرمحمد کصکشو با تیر بزنید خیلی نرینه به مارکت موسیقی ترکیه، با همون بلوک۳ و سمی جنک و اینا جمع بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83758" target="_blank">📅 09:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مصدومیت اجازه میداد میزوگی اصلا نمیذاشت همچین سوالی تو فضای مجازی ردوبدل بشه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83757" target="_blank">📅 08:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c6f49b83.mp4?token=Z1R9FsNa3HFk6AhCaL0S2VUNRKE5jixIcyccdhdSqJBbKcUD5dHKJc8ipD0A8gf2b8yw8DV60UiF2QpwDHnTcuZju1lK0Mj2bZ3UAdUmMoxRT8bG9yMiJdhATFUOHsYY2RRYpw-tVoBesF72HnQFE6BfglOnueBIuyCUcOkAs0kXuUPYBnWcr_7tHUplS15U4_HuPChark9UhjJFuSFgjl1FBbKKW6r8cFnvX5MhhnT2bfVnRmAQC7T2korYJshocXHL7RieTHwZ1ZJXwIjYFfP-ojZe6P2NrT_so1zrP4KH1IN2eXrkMbAcdve05OZFTEq4WdNwAa2rHL2oHqtWSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c6f49b83.mp4?token=Z1R9FsNa3HFk6AhCaL0S2VUNRKE5jixIcyccdhdSqJBbKcUD5dHKJc8ipD0A8gf2b8yw8DV60UiF2QpwDHnTcuZju1lK0Mj2bZ3UAdUmMoxRT8bG9yMiJdhATFUOHsYY2RRYpw-tVoBesF72HnQFE6BfglOnueBIuyCUcOkAs0kXuUPYBnWcr_7tHUplS15U4_HuPChark9UhjJFuSFgjl1FBbKKW6r8cFnvX5MhhnT2bfVnRmAQC7T2korYJshocXHL7RieTHwZ1ZJXwIjYFfP-ojZe6P2NrT_so1zrP4KH1IN2eXrkMbAcdve05OZFTEq4WdNwAa2rHL2oHqtWSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت اجازه میداد میزوگی اصلا نمیذاشت همچین سوالی تو فضای مجازی ردوبدل بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83756" target="_blank">📅 08:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4FEamary1lnB03UQvCsYTGL7L4wLymFK_TUIblUASkO-EOaTTtgCOx5BIy9-6gPhc7GpHrZjfESsS48qIJAKz98FoudDPFoiTiFpij_ONQ_64m5Uk2ygfDes9dfKj9H0VM2X8QA0gkA8VGjMFWmIQVfKqQWEtYqEM4QmlUocoeIFAk8a0fuMPsNR6aLIqLeJEIR625DuOgZl0sImvUDrN68OX5m7HyZkn01Oqxb_f5dtJ5ng0VfVKwUv3vaOz-b-9VI1qcOqI4aGXmE2wIVKPHn-KxsxlsGHSdu7nuDJ6pRgeOcjJpDxaftSK4XduuQmgAIcYRpc3xNNQiizqmAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرفان کیر تو دهنت الان اونی که باید این گلو میداد تو میبودی نه سیجل.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83755" target="_blank">📅 07:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1PRcFKJxxrcfE39jS5VrQpWnLpbPBKKabBeXBNbQ26QB_KKsJEOYIyTz6y4TH2LSQlIFj0BmNo__3MNaIlfj3k_t3Y8odj62WtHy-IODADnLC1U25T94cTCEiN8J7S1NxhLCMRb-3pHUWAhu0KxVepj-Q9zMMBBX1nH12GwF93nbPNw2WQ3P6aqIyhuAga7pZrZBuDQkjWaROenoHnrr-mFYUmKofdANu6sw9Czk7Jg-0o7QEBNuR7RxAIyXcpytmjglFLdobqcy-jKLg4I1Eu_R7JZfhcP6tCvZVaZ0LXdZd8C9gLeI4ZHqNhZnAS1N6s7Xh_UNHcbUWV8SYaGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83754" target="_blank">📅 02:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دیگه کم کم آخرین باری که یه نسل چهاری سوپر هیت دادو یادم نمیاد(اگه کصشرایی که با پول پخش کردن ترند میکننو سوپر هیت حساب نکنیم)</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83753" target="_blank">📅 02:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بهداد اقبالی زنتو گاییدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83752" target="_blank">📅 00:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL2lkd3HoUNfFUW1ne0K81aybXnVAS30w4CdAV5LOwUuWDsgarRli8wWEcoiCCBrYg7yx9QYosLZ1JF3HqRQPcrphIK1fdbxhNiEya0cJ6ZWXniP3x1sReR3QGV6ovMuw3XPHuO1ljcBXiej1aA36DkR13vSJgKhgWA1SZgBQn_OxfILIWhbPXZ6FUpfT1NrWm2-f7xEA1yEtBrt2REaFQO0Nrm6XYuz3RcAF5V8j0z4HiSaIDp49VgBjEYVe4_NrVBpxTXDITiCFFnrlzT8LRvaur7iIh4Q8qr2AamiLUPwtCqdBragWUvBznCJMRQX-FUjyVVzLny6JC-86I6QBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/83747" target="_blank">📅 22:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83745">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83745" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83744">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8926315b1c.mp4?token=SDWtOtD8fdRFVRGDPjtIc8rbeYvD-3aZRWvSzVudvMwNNFSejpY8ltzmO6bPuaaps1TMZgwrzgEDLfnqKv816zBPhZBcrDyzln2AZek8LE58dtjDMcN9ltHf7bgK2yZhxc1aNHVUSUx773ZIPNKa705sKqjL4CsVLx3KmlITNCWk3iplVuTAoD0ijVguvaWELlrckP6wreuAfSOZTN823yDJAH8CJ9qL4JJMj1YTe4fPSKTEEINSzlfsCX5rEDX2onduriRFZQw8TIB0caEoiaFCSHlF4AfZm7uEO1f2DFs_uXZeNOyw-8VWp1ti0-wQ_FFqL9irnqLA4ZQt_YSJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8926315b1c.mp4?token=SDWtOtD8fdRFVRGDPjtIc8rbeYvD-3aZRWvSzVudvMwNNFSejpY8ltzmO6bPuaaps1TMZgwrzgEDLfnqKv816zBPhZBcrDyzln2AZek8LE58dtjDMcN9ltHf7bgK2yZhxc1aNHVUSUx773ZIPNKa705sKqjL4CsVLx3KmlITNCWk3iplVuTAoD0ijVguvaWELlrckP6wreuAfSOZTN823yDJAH8CJ9qL4JJMj1YTe4fPSKTEEINSzlfsCX5rEDX2onduriRFZQw8TIB0caEoiaFCSHlF4AfZm7uEO1f2DFs_uXZeNOyw-8VWp1ti0-wQ_FFqL9irnqLA4ZQt_YSJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83744" target="_blank">📅 22:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVlsqeEx_tG0tsUonRKRWa0xZSkgUQy9KfIDJ29poT6lGj2XEkndyeDJ5ShucJkeEv1M9pz2hqYpfeN3Xb-nx2DqG1-GvGurqgfM5MBRyf_-HzzY9vhu3H9Z-256zvL0XVg8e-nHOH-YKCuHIDxlGj5Dd-nzsVm4wP4U-meAvoWCLS4iaegKyP4ewj5t9doY3y4S6fZklYAyK4bCCfcncNxgieLDjw6_wINrfrjfS-7hwUIUjBL7yCjh2XZmxA9kgrFR3mHrWouhe6gz4VFkd1m-Ykoj76UxGtSdkoLXHQ7a6RY9oixdYFbWuTDpvArHPnejp9W9AKUy7cUhtCaPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب وقتشه که پنتاگونو بمبارون کنید  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83743" target="_blank">📅 22:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83742">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پوتک به ده تا رپر دیس داد دیشب
کی جوابشو داد؟ ایمانمون، تنها کسی که پوتک بهش هیچی نگفته بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83742" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83724">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شیر ایرانی که کون میداد فیلمشو میگرفت توبه کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83724" target="_blank">📅 21:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83723">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4397dc1e0c.mp4?token=SYpBSRqo33XTrQyFwZgbKi4NaUk0K-LfNG_JZStUirJ98El_U-YfLMeDkSy4S4_B2rtwNFM2IyKHvyUTw1-8pWQGAlEirU64soLc2hu9EnP4Ggqcv6Wk4ROJ1_n5M1Vi_0u4ixz2mGfF8mW5wOquUjFKvHMW86ZeHQ0FEdq8untvR1St64OYTAusRdpOIc3CJs0w54fkwOTFNNE56tx1WNVHTuTb1mdM1vR7ZOdOJQidGkPYVz2ierCN8u4LhUFk_0TeU-bRmYBy4LJTPT46zUxderbWQ34BNto5eHap_O36_7nggH7YdmENS3You5hLAH-SQL5U8BDC0GUaoGHUOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4397dc1e0c.mp4?token=SYpBSRqo33XTrQyFwZgbKi4NaUk0K-LfNG_JZStUirJ98El_U-YfLMeDkSy4S4_B2rtwNFM2IyKHvyUTw1-8pWQGAlEirU64soLc2hu9EnP4Ggqcv6Wk4ROJ1_n5M1Vi_0u4ixz2mGfF8mW5wOquUjFKvHMW86ZeHQ0FEdq8untvR1St64OYTAusRdpOIc3CJs0w54fkwOTFNNE56tx1WNVHTuTb1mdM1vR7ZOdOJQidGkPYVz2ierCN8u4LhUFk_0TeU-bRmYBy4LJTPT46zUxderbWQ34BNto5eHap_O36_7nggH7YdmENS3You5hLAH-SQL5U8BDC0GUaoGHUOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی که کون میداد فیلمشو میگرفت توبه کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83723" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83721">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1443105ba1.mp4?token=qnSx0oqtFqH7Z2ndfJpf1N1Oo3h5mdX0DgvjQvAAHC_giCMNBtkH-sKy9QHzBAKkmBOmpYfPEnpCYxZKryLRhcqD3LNMtrX2Sc4GSGr-sjsQztGXzwIngo7o78vNUEeeARFxJAg8YYFzDZs9Pp9ys9jrj1PZnxvSo4MP_y3et9431B14uWgIRR9Oo5iRqvWMsO0io7qwUgu21PiNNtMM0vX_XyvQBwAs6suBAtmPIpAGxZa4GZj3I5qtK8GDcyglozNGc9ppLQHcmftEXUc4lHqLsAEjy91NkRg_vTKKoddAlKbHahv3F3jvE-G8yJOxsfxRYNFSzpr4u_ms7sHeUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1443105ba1.mp4?token=qnSx0oqtFqH7Z2ndfJpf1N1Oo3h5mdX0DgvjQvAAHC_giCMNBtkH-sKy9QHzBAKkmBOmpYfPEnpCYxZKryLRhcqD3LNMtrX2Sc4GSGr-sjsQztGXzwIngo7o78vNUEeeARFxJAg8YYFzDZs9Pp9ys9jrj1PZnxvSo4MP_y3et9431B14uWgIRR9Oo5iRqvWMsO0io7qwUgu21PiNNtMM0vX_XyvQBwAs6suBAtmPIpAGxZa4GZj3I5qtK8GDcyglozNGc9ppLQHcmftEXUc4lHqLsAEjy91NkRg_vTKKoddAlKbHahv3F3jvE-G8yJOxsfxRYNFSzpr4u_ms7sHeUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی که کون میداد فیلمشو میگرفت توبه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83721" target="_blank">📅 21:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83720">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7a3000ee.mp4?token=M8tqFxLqIy7tPEX3zu2EPmqApWn-GatjGgA6XfVzfuq09wlZWnKLwb3dV9dnRk_3e2ARLdI_t7sI4bQAwTBhawXYWSWMpnhnGU8oSqa2_bL4xcvMgXaab6JM1uVXEHHInfm9rCUfcQD7YQJcKuX3exBR_2dND1E5LrDqJWe8UoGwUPejHHEt6aJvg-JBwz_PvWtutUnhg7pdVR1qPpwUxL-J8f704wG6iTWDrv7wt-BTZwJnhKfSWuPqhfp9WSNDhe3frwbhlby6-QkEib9fMsfcEg2MDSYqI-koRNGjjQmKZYD_laBQ_b4TZRNR6--dvhiEFuJjKuCom7LtKUDHZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7a3000ee.mp4?token=M8tqFxLqIy7tPEX3zu2EPmqApWn-GatjGgA6XfVzfuq09wlZWnKLwb3dV9dnRk_3e2ARLdI_t7sI4bQAwTBhawXYWSWMpnhnGU8oSqa2_bL4xcvMgXaab6JM1uVXEHHInfm9rCUfcQD7YQJcKuX3exBR_2dND1E5LrDqJWe8UoGwUPejHHEt6aJvg-JBwz_PvWtutUnhg7pdVR1qPpwUxL-J8f704wG6iTWDrv7wt-BTZwJnhKfSWuPqhfp9WSNDhe3frwbhlby6-QkEib9fMsfcEg2MDSYqI-koRNGjjQmKZYD_laBQ_b4TZRNR6--dvhiEFuJjKuCom7LtKUDHZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوروش هم فهمید که تولد ریری از همه‌ی این بچه بازیا مهم تره و همه‌چیز رو ول کرد تا بره تو اون یکی چنلش به ریری تبریک تولد بگه. تیم رسانه بین‌المللی و مردمی فان‌هیپ‌هاپ هم به نوبه و وسع خود، این رویداد استثنایی و تولد ریری را به خودش، فن‌هایش و تمام مردم جهان…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83720" target="_blank">📅 21:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83719">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b843e8143c.mp4?token=NPI_otD2pTlko2vFkMdLEkGrUzrpT2d7h4edNCqhiXuFbeVUQ5OaBv0MKyUdnShwEuV1pw5L-J4wjwY182xDSIdj6FmpqT3nDxjl0PrKo4M5gb5MY8EhmiyePIuiXmOte1NFtydXlkd4qOaorLZOJYsqUve1i92O_NfV5MURHSF7bWNDzmHpl5R_rRtTQM49C3iYTo7CX0eaw3_kedTw96znEPh2yUNFd45sy_sEboesVk62PRx3wDR5D8xYFRm6A-fneiCdhsjKfZes_TEGg9A1epVdo2oqrf9PxvGxmOjxl65McZZbkXqGByJmEBtDXHDLiYma2CWk-pmaKm1hxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b843e8143c.mp4?token=NPI_otD2pTlko2vFkMdLEkGrUzrpT2d7h4edNCqhiXuFbeVUQ5OaBv0MKyUdnShwEuV1pw5L-J4wjwY182xDSIdj6FmpqT3nDxjl0PrKo4M5gb5MY8EhmiyePIuiXmOte1NFtydXlkd4qOaorLZOJYsqUve1i92O_NfV5MURHSF7bWNDzmHpl5R_rRtTQM49C3iYTo7CX0eaw3_kedTw96znEPh2yUNFd45sy_sEboesVk62PRx3wDR5D8xYFRm6A-fneiCdhsjKfZes_TEGg9A1epVdo2oqrf9PxvGxmOjxl65McZZbkXqGByJmEBtDXHDLiYma2CWk-pmaKm1hxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوریا علاقه‌ی شدیدی به ایفای نقش باتم در رابطه جنسی BDSM با هرزگان دارد.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83719" target="_blank">📅 20:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83718">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آرتا داداش ۲۳ سانت دیگه دودول نیست دسته بیله، دودول برا همون ۳ سانته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83718" target="_blank">📅 20:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83717">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ: ممکن است به سمت جنگی تمام‌عیار با ایران پیش برویم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83717" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83716">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام "بدفاز" منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83716" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83715">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMKuceiQgUAnEBZ2tUdFzSznxOmumZRwYAb6NAaO9kaybMhq6efdjBJJHjVy6f3f8eU9kA8NHMIsrBHULmX8UcklyqT_Pk1okpXRBPcTiyHPIOW5rIEcaGHp_3X0ela8lFWV0a6Q0nuhN_QQa27jU1n4M1ZYrUwwBRs7CaGfIrkn_-QT2-gq89OQLxfh8f-S4IA0MRl5_hieHO7HjyWFxuuKs_tVcBnHLcCnVyYA3oR0TlIe_ZhuhOo2np759XtG0I1KdXVSNIzTRvwrI-9pvBcC_mnnZVHBWWGowYb1AbV5lC6sjAGHeibrMGTzy44hvps-CvBNvMTOmDvXhjyhfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام "بدفاز" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83715" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83714">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سال ۹۰ یه آلبوم سولو داد واقعا خفن بود</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83714" target="_blank">📅 19:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83713">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تیکه‌ی سنگین علیرضا جی‌جی به محمود ویناک
😐
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83713" target="_blank">📅 19:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83712">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP7WDOXCygrIDusBW2Pa7KWQvkg4PX4Ufeup2tFRWGa8ozJAQNjkk-Z6QejPL9FPhFyIwT3v3w8RV3uZUbmf6nC7IMrTMHd2-8d4MhHTONDtOHBAAyMPHW4PTH_9l9e8JFs_Bhfv6kG1Uy5ZsvJhv6ckyXqC1Xx7p8OciR1Mzi-8UHkDClyJ4FqAGfxv5JUnLCR7lOf-BoIqvL44h_myydCBky78jcpr9PapjHfbKOoj3TTV5uQfqNNlQf2wM1Hq1sWoY8CDcAgdASES4dyv3CI00TpW9EFf-SsVnfqPCadg1iRKwXgBPdFnlSoUlxIq8KQYEYlUmOyyol0ZGWJweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیکه‌ی سنگین علیرضا جی‌جی به محمود ویناک
😐
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83712" target="_blank">📅 19:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83711">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3xrPdJfqov9nj5l7Cj5zls7nk8WGI5q_p8bK4HU1YbRSL8F1CuCNgkJubLwoZZTO-uAiXyCtdyC5M9Q9w3PNaWcraCIU21IdkbnRTNgibrkvcMFd1irZXzDASEF_B1d-aD40tb9XXT9vxC9dp4paV0SxapU_KKvzwK3p3vNpCfeLbhmkxrLYNrF6-lnmvbd_Pmkvu7jIi8u789PqpDxGWc7Vp6pdw5o_kJdHF6NlLKFOpYzd_kXbuq5vdi9jEgvNsBes7V617lNTK5Y2j4ZNoj6Nl4-AMc4q267lNxpIZWmtw9gbobkkwb3rfhG7gaZr2f5oHMS7E0G4w-CkcG1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست جمعی روانی شدید پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83711" target="_blank">📅 19:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83710">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مصاحبه ها یامال یجوریه که بیشتر از خودش برا امباپه میماله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83710" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fv9zEgvPehsVzh9v5D88_x48xsDGVQmF4_FcZmqiXO1c2kyk4fd2dUu-pCtKyXEluSkvQfOY2Fy6OAY_iwlueMQPcjDZ3VT27Xm7GMecUPccolCf5WadLlxAukXWm9drFfg1Ucw4QtHt6JNO-6c_fxAgsDe8PRetq8-VbQDchQQRNFsOw4bsgCyCVhgF7AOnhzL02W8Fxa2LfIVR7VDl9Tv7yAwC7kBENZfVTTZ0PeS3am8jKUeT4RxSj8gGoKnGHSzfYL2PSIgIXpWN-Tw5QItyupbk3qmCFZcKrsiYcoFNPi1L1NsxuFmw135sPuoQ-kvi3lkRXx0YvL3l40WDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااین اوبنه ای رفته تو رابطه؟</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83708" target="_blank">📅 18:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83707">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN3-Hxj3rJZVNCq2-YzOmVSIujvUQwfw3ScaXEB6fLj7oOpjVPiB78ej_Pf5blFaomZBbECUQqNDM9dRE0BS6RfBeKTACaxVe6-sJEEphxcWhU6oXGuy9xDw6YOmNBhoZpHET4Zl_WER9uHBCYcgkW-WdG0i_WvJ-GzBrUZd1VvOEToOhCbGP2ihAauC2WixDZRQFTMKWg31W2AB3m4VBxoFITkhJnY3Pv_uKUioHe4VDyMQUSGSxWnIkzLe00h8dWtUPL3LgmFJ6e3ENb3ObHR66SkKQ5ivq6UY_LsekfJb_EjGwiKTYaJBJpJNDXWi8HQTIIRDFIIaQ8kWc6nN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر پوتک همین دیروز با اسباب بازیاش بازی میکرد پوتک ویدیو میذاشت ازش، کی انقد بزرگ شد که بره تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83707" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83706">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9LO1bOWY2W5msPbo1DbvKFpmTWb06b6mOGcHhi6AwwcnThVfilCGexqeuwHyQ74oLgeOOFhdTYvIVy6ZAr8fUZ7FWbzBkxi8ISCdF_korjdnuUPXt4TlW2UAJNC9UK8Zw_lncnQ9vItgsFalUzgufSic20HaBKno7jLtFzyDuv1CtQEkIKhXNvnOry-3lhqyCW6bTyxozyHoVuQ8SCuzq8vfm767bEh7dls9MlNBQsp2MJ2Jg1TyKHd4fL0_P1P8JSFJ10_p89tgFQttHUyM5eG7P3epWdx5BcGsUlobp6mxJLUCUK9jo6JCsXLLwB9UwHLRdTI1bFzqnAvyWIPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
27g
🅰
🛒
ورود به سایت
👇
✅
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83706" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دلو به منم پول بده تعریف کنم از ترکت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83705" target="_blank">📅 18:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83704">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_a45z-rjJLdLaqv_qCAovzml_WyvjOqLZ0N6X940sm5AHCIWO2EiBu-CSkbuoLjVYa0Y1-aSC3AhVsQ4cwx1VL6P6ejfKFrdoJ7ygzh_nx4hOcbiTeY25WpNULM8-qm1DxxJ_rj-_XB7kGZwUhfRxzebP5pRBBncFbBf-BmburYqUK21HP0Hq-hevzoUttxbbaPsSlU_V9j4vrs9SJlnVtx3YeZbA2h3ZlUwe-_1GPhCIy369UEPr8-J0Z2d26xIgSGa9wWu3CWHvLHY9mMobHG2CGB6doEMOqLU0dARNuQL6IZttIVjHl7ISSFytNZBPs2XHqmY02Sn4lYtLKUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام DUH! ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83704" target="_blank">📅 18:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83701">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f38y4SnesOypgLZDqBlyQfa5CJ1fiz9Ub3kKWQwvJXOrusp3TsQ0vxhKFipEddwFNX7Vt7dYi1VFX2zQKRW8l9l0DC-rM1ZclRdNoM10WyH4GgpWXxOsHpALhHxeZDt3KQEQLoDsVvhq3Vqnf6OLrgAj50j_0uX3tD9x3QdVCAkosr7yRNJ1nz_D1A-bOkN_BLYISWkYVM7tJEJ8Dzmtf77N5LzUeWJT01Y_3FMDDI-L_zwb7CutCJwLSaF8mGQgjlqyBKg-lnc7FJ8_lV1RDxixSvbiLeD9Y0uAQywlZiyJXTVAVljMRYKnvv3nYf37oICvWo2DBk6wmF4xUhrgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا انگار داره آینده ای که نیمار پسش زد رو زندگی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83701" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83700">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترک جدید امین تیجی به نام "قلبم نی" منتشر شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83700" target="_blank">📅 17:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83699">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3l2yXvM2ckcgaTxF2jWxsrhwtIZUmqSjfyH_NLYfLtozCWN_0uU_6MLSyEQEsV7ZMrLubDC8Mnm_z-krN9TIMcd3CKrF0iz7w53_TCHFZUFCOU6RvrVTfUXKWty5jLPDw9illP69f5rCJ4xryuACEeTLkQX_HK7kUBA2JPgOxUqdRTgJ8eiNoj5_1Nr337-OJQ4HzGzR5kTuRsCF76hQywE647YK6DV0HCi5Lp6xdUOfg7OQ-43R7Pg4EXaldjf8eYJmx0Wz5QLB3_aVwXv0Cad8FCymAhhd3hP5hdmC051hz4_skbLQcGwQ-tDQUDzE9WnxIM_AuQQfAKSH1pQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید امین تیجی به نام "قلبم نی" منتشر شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83699" target="_blank">📅 17:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83698">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfupi_LkuNoMixiAqOAaCXu1c0VxjIjQ9LT--cZKGOPKTw5mBp7jxi_zz7TLjBaCeefw1EJebB39o-wLQxoHrG_-9Y2_MNbHN4uXb1WHxtB28wdFoJBpFLzo5m7orxHJIg5M918gV4DF_NmdLVX5AEtQFsjVzO5zI3IydHZ5Hjx35cs54r9gIMhHdhoMm0A5JfLJKg7w-UplLR0t59x8OdFQaMgCxvBblC-yr-G8RMT6FJC2mdd5hFlC3qbF3pAuSBlw7X42EVFPbXTLxc4mzy4SR3nwKnSQIf47xYUzs8mvr_uL3Nma8FswwmLphjukTwxkIiupancKUOQ_mEOXKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر خونده پوتک: واقعا خنده داره که شما احمقا متوجه نیستید با این کاراتون باعث میشید پیج من بیشتر دیده بشه و فالور بگیرم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83698" target="_blank">📅 17:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83697">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HORy6naDXKmf7Akg6TElndCPD14bNS-L5Sys-3FiQz1brDlarauc1bYWcLZtW_wowKwN_RXzR2cGDU0JNtSxNaDCs_n7hcY9P727oR-K9BlRwXsSNJX3KqlgjKf28D7Cft-iUZrzX07W8AmLEPltHZHd1OnIo9Oq_966cXy4xkwnBh2DZCM3CatYoMhxbiBv51HT_gV2zvY9ILNGt3aGJjZKtfdJetJv2lCn34woUKpSOLOn4zR8o7QhpMoBUBxXE3UMOBCYbrYMqYprrmPkBU6qjTjEWtHaSW-fKltCDDnQliYQv9KMeCIOrDl3-J1TU8kMn6TvPewG4b7XvTKiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلان ماسک: «یا باید ویدیوگیم بازی کنید یا احمق بمانید؛ فقط همین دو انتخاب را دارید.» این اظهارنظر در واکنش به پژوهشی روی ۹۲۳ نفر مطرح شد که نشان می‌دهد گیمرها در عملکردهای شناختی، مشابه افراد حدود ۱۳.۷ سال جوان‌تر عمل می‌کنند. این مطالعه همچنین ارتباط بازی منظم با عملکرد بهتر حافظه، استدلال و سرعت پردازش اطلاعات را نشان داده، اما ثابت نمی‌کند که بازی‌کردن مستقیماً باعث جوان‌تر شدن مغز می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83697" target="_blank">📅 16:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83695">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bas9c-XJWLWxWQPgFGXegDXrNhpKt1oG8xRvGKLmjvIkyg-RLcGIniPFbaSnQh4CLPE-8qGJ_xsVe0qyxyEJnxGhMCiIWGyKz-_dVXc_C5dMzU1MeqKe9WZz2pwHG2zeJIYClA9Aw3T5VieVJ3QUtwXheXpiL_mslz-0agniOEkt12Oi4GlHJvyQteh5JBEeYdIBJpbU4T0QLkZmt_LWw7-1ZXvJaWG1bLL5e0V0MQZCcUeOojc5facXrjGeYJ0VGe6-vZq3OL2NbNcNQhrR3aYgo_bRN3AC0ElDfncamCmO3dCo7dIlbGUFnmJ3H35ajjMI_yb9aIbmuNYvKfB1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5f4b92ce.mp4?token=ltuohiyZ0wBqSGCbfcpfM_HwfScEqzCr9N23_E-QHx0_eOReq6wcSQNGWesQUt52uWKhsqaPmnVIlyeDTYvz8ipi-wi6meh06FlndFwDTkWDO30BRYYytaFOEkYQ98_HjwlGoiy3gM8nna1BDYAaevJFtEFIz1I40MLuNJwwGUdtv0zOtNAuRgkJDzcPZHo7xU9MDNIU24SXVoe8hsp2tsY33bQ-_-H6usHieQH6dJfyQp5_UMW3mVIir9_4K_gMT2PtYLhHiVEm8-pHqkFskKDaWjH4TKAlTqZOHFXUEU63PcXItUH-ilhMuVq6k--G3iSyVEBHuB0PpiIUFUPNyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5f4b92ce.mp4?token=ltuohiyZ0wBqSGCbfcpfM_HwfScEqzCr9N23_E-QHx0_eOReq6wcSQNGWesQUt52uWKhsqaPmnVIlyeDTYvz8ipi-wi6meh06FlndFwDTkWDO30BRYYytaFOEkYQ98_HjwlGoiy3gM8nna1BDYAaevJFtEFIz1I40MLuNJwwGUdtv0zOtNAuRgkJDzcPZHo7xU9MDNIU24SXVoe8hsp2tsY33bQ-_-H6usHieQH6dJfyQp5_UMW3mVIir9_4K_gMT2PtYLhHiVEm8-pHqkFskKDaWjH4TKAlTqZOHFXUEU63PcXItUH-ilhMuVq6k--G3iSyVEBHuB0PpiIUFUPNyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بازی FC27 وقتی پک جمال موسیالا رو بازکنی، تو انیمیشن ورودش غش میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83695" target="_blank">📅 16:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83694">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2b646200.mp4?token=BKrrPEXEzZ8ycbbUgbCuJn9jVCmKwsJEYjH7nw4qRl92KV7M0iOj9KTTH0_9ChFt10vi9xHmDLI8kpmoVOdIMBl434YBXR2RtAg8DvFIP5JC3IHgksNR6x7Dm-Hg2T66K9brrEmXfV6mUSCQfzdoTgvq4Nx7PByDH2GX7skScPymjy0XODLPhFKMGBDBZowJCgkMezXKTw5Ea81wel-nZd8rPwFpIwiVfolZ4-pOU6Z87FlfYnqehhCw8Bm2HNMhiRf_BL6juJ3StubABYF1W8VtHIv0-SVKXqDxqlHIvKlzqQLprHS2hlCTEczCh5lWqXefSehO68VjnEGx2J8QQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2b646200.mp4?token=BKrrPEXEzZ8ycbbUgbCuJn9jVCmKwsJEYjH7nw4qRl92KV7M0iOj9KTTH0_9ChFt10vi9xHmDLI8kpmoVOdIMBl434YBXR2RtAg8DvFIP5JC3IHgksNR6x7Dm-Hg2T66K9brrEmXfV6mUSCQfzdoTgvq4Nx7PByDH2GX7skScPymjy0XODLPhFKMGBDBZowJCgkMezXKTw5Ea81wel-nZd8rPwFpIwiVfolZ4-pOU6Z87FlfYnqehhCw8Bm2HNMhiRf_BL6juJ3StubABYF1W8VtHIv0-SVKXqDxqlHIvKlzqQLprHS2hlCTEczCh5lWqXefSehO68VjnEGx2J8QQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من به خدا آدم خوبیم نمی‌دونم چرا خدا این محتواها رو می‌ذاره تو اکسپلور من.
راستی تا یادم نرفته بگم آرتا هم گفت امروز دستش بنده، ولی فردا یه دیس‌بک خیلی خفن به پوریا پوتک می‌ده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83694" target="_blank">📅 16:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83693">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKd6fkM1OQPzHD44JkZsXGOesgnHxOue6LEqdHotwrG3SLJc445tdUxYY5YTvj53TIxGYfFvb8mt4nw3EgNCm87gQutl22OkAkY1CQ8k2Aku8fO4fGLOS6dmnKI5ywDZAG4QfI4cYJX8WTrIsboHAtqovdJLRoPXdEY2lK6wP1if3KS6pdnUPHPehHI_Ler2XFqBqnPWZrRehHaZUf8fbs2GagYAztdrhoz6Ur1TvPSh6_5OCCn-5ux2MjjyUYKtpXCdb_4FR5jxYYPMJjGP3ZvRVwUESYyO5f4_R3lC3G53aGKqkE_WqqXk_3cBJkTOmnAEAG4d4P8gDT6HxyzoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب وقتشه که پنتاگونو بمبارون کنید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83693" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83692">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14cd46867.mp4?token=r9zED7Bc8ehm3egarOmQGCsFkoWI6xrDodivLTXFzHZmd6E2qopzkd9U6px5H7ZVoVUUo9LjGyQQJDO8WJNdZOoCFpqjjlQluMEbKoveD1BSEUeaFd7E_7aMfonO5e7eG-p-AnTGZC7XE5ZbjtlH2b7n71Q2a7aVWD5miom-cvKaGSYldt1vszQuBCMwJbLnDBGFgSu7ye8EdP-VHxonr1y4ip0sDPfj5ZPl1oiVEY0RW8cnGylZrbzz6tulfrC_EdJq_cAurczug7E7tNAA40_k4KVznfBC_gDrI7DTwak8X4v-LzYs1xj2qlL6qg8Ro6d9LsbScGFczvcfZc8zLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14cd46867.mp4?token=r9zED7Bc8ehm3egarOmQGCsFkoWI6xrDodivLTXFzHZmd6E2qopzkd9U6px5H7ZVoVUUo9LjGyQQJDO8WJNdZOoCFpqjjlQluMEbKoveD1BSEUeaFd7E_7aMfonO5e7eG-p-AnTGZC7XE5ZbjtlH2b7n71Q2a7aVWD5miom-cvKaGSYldt1vszQuBCMwJbLnDBGFgSu7ye8EdP-VHxonr1y4ip0sDPfj5ZPl1oiVEY0RW8cnGylZrbzz6tulfrC_EdJq_cAurczug7E7tNAA40_k4KVznfBC_gDrI7DTwak8X4v-LzYs1xj2qlL6qg8Ro6d9LsbScGFczvcfZc8zLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین محمود شوماخر چقد‌ بخت زدس که از سجاد همیلتون اسکی میره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83692" target="_blank">📅 15:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83691">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">محمود کوتاه بیا ناموسا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83691" target="_blank">📅 14:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83689">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RTNXo9YFg_YeB9mJJ9xtRGPRApx9daE_pHnrGx_j7oLJ4VXRZcXNdlts9Fe4NAMGZSdrHqGr1WFGE5P98BN4JSLFfMmDrlheO8LdvKX0zELfJ42wpaH6RufkvDqcs5-fp7mpqmUbeI-TRtjvFNOQI3AmOKA1LvgzaGhWDwrzR1WpwxBxWWEhbe0pS00wBpPaCSa51kyKwAETEGVaXrsvaP7F8dEUuPSzsXrv5oOgrwM_YElF55jaESrcnfEpLLEq22buRN2pwuBE3Pf1jfA0j85VG4HGOIgslhnJJr6zWC-X8BZmSCf9zCder4Y7-YVOm6x-w-xFDaWojn5TMsINtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3Z8iaHChlESi1gyyg5uM34GaLzQjao2ISmpVQI6AeYvgRUH5Ngt408zTKylhH9_CsHkbLZnmN3CKE3_U5FrukElvp7xYpBmOCqLE0kJSU1U4pV1B5GOp5F2ojIWYAeSFXlnOjIV0YSqeztDhHbRdUPcSCHg-ABNseGKNhslMKG-PT1ulrRicNWu-s1XT1HIFFEp9UEnT2hi03cc7S7Ebzptvd4Ov5DcwghOyDi7csV44YnZY7ZLSvX9xxkSWPRlJbPdfq1Wlporijdtus9tjykt5LaEQC1iBitdp7Sjpzoow3j6wia8Ld8w1vtsLDOCIBxi0J6aRdrfwquxmTBZCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یعنی من باور کنم آرتا کیرش از گوریل بزرگ تره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83689" target="_blank">📅 14:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83688">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اسپانیول - الچه
⏰
ساعت ۲۲:۳۰
🌎
📲
برنتفورد - چلسی
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83688" target="_blank">📅 14:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83687">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o076X5qXqtixF9tEPcELjFWhzvFXx1AH1u3mBybd-77lLcIoZw3afyYfKrBWnO5N_R0JNEgwbzjFqTcZjisc4X-K308gHYIUcrLKg3CFG6WJxEWhafiGPCPdMGWaBm8bywief-aq-egU9u-7zXx3mWbCagtFr0mhGyjWeSvRkyooK5Tmzmi85d-OHRoBGOvJhZg2mJPfBFpZ8MWRVrf2JHPkIx2tJK9UpUEjXgOj6nGJT5T1SB2k1j6AC4hwFkG7A_tKSUSl6WQCMmyFcOzkp79zabVvaOGj-xk6E5Pa8rib4D3QWLsZbMUp8bqLVW-4kvoUJUHpGxJOx8C-XYtI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اسپانیول - الچه
⏰
ساعت ۲۲:۳۰
🌎
📲
برنتفورد - چلسی
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R27
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83687" target="_blank">📅 14:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83686">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHWls-irsOb4Owygftig9bOa6s7SctTHZFZ7iIGLyV7b_OmMgDCk2YGuZLhE7SbIwwQkgMb--6NCFtNTSC61ukKWWX-MBun0O_wknUVA5sSn-ha_bTaPkNx42gzMbkGV4VXgukHXNzV5ob0Mn_wbjxWF2fDCU4VUp3puCA791y-BFOGeITSheJ_itSKq5sermtMXlgSfdU1mukx2grkDqDfi3V2OMRNhtaQAJAa69njV0WHaw5oH-RyWJQDbA_BdTwZkCHMGVLxJImmmCYK2NToku0fOwZRDPNjaQVpEhi5dkNAuRTGP82ehLdC0KXKQBtUpZ6G49Iim4TITWK2kRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور سیاسی مجتبی خامنه‌ای:
اگه ترامپ و نتانیاهو از قدرت کنار برن تنگه هرمز رو باز می‌کنیم.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83686" target="_blank">📅 13:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945ef1ce48.mp4?token=YVAscUsA81ITZyVg-VVHRrZFA2mVnhkKXvLOLeOb_QkQaOBXwT3OVsnrSQp_Nd050lVrH9TrQYrWenCY7aVo57OvdPTTjmNZzSB73anIYS8lbh27QTLRZbPM2cxrYWzymhM8Zst6QKWr0rPsDSQhkC6zIAL4ZbMlei8ZhjrptJ2AQP6DhOk-N1ocuZtZnLoo-YbbUNmm5m9_bIAm0CP-pYGVC2B9K9HIoUAPUo1_pRJEgshuTjitFezpVlL8p2lc3UzEBdPReXA85pEaegeCTwR2kRLP0UPqysj4iwjerIRwC5Nv8ZRd1vzxgy3-r5sXjmFWsnAvw-A9vShCph3boQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945ef1ce48.mp4?token=YVAscUsA81ITZyVg-VVHRrZFA2mVnhkKXvLOLeOb_QkQaOBXwT3OVsnrSQp_Nd050lVrH9TrQYrWenCY7aVo57OvdPTTjmNZzSB73anIYS8lbh27QTLRZbPM2cxrYWzymhM8Zst6QKWr0rPsDSQhkC6zIAL4ZbMlei8ZhjrptJ2AQP6DhOk-N1ocuZtZnLoo-YbbUNmm5m9_bIAm0CP-pYGVC2B9K9HIoUAPUo1_pRJEgshuTjitFezpVlL8p2lc3UzEBdPReXA85pEaegeCTwR2kRLP0UPqysj4iwjerIRwC5Nv8ZRd1vzxgy3-r5sXjmFWsnAvw-A9vShCph3boQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین دوتا از اسطوره‌های موزیک فارسی برا کنسرت‌های جدیدشون.
کدومشون بهتر بود؟
🔥
👌
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83684" target="_blank">📅 13:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83683">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uug8NgMFAN3r1flRBWqP176LbuI28p-eVDJ5gbrz92BXeChMYIgERAnA5MGL_Opf6F-LAoswJV8tfAvo9elb8gTgFMeS4DyCUcIWBRTN0Kf1rSgGPBEKHiePaEyiVFh1AJpSHT86IaIZSzwndam2h9zO6niTN-oq-teHY0AK6kWrUex7aBBpecdBiCql7ohs-Ye4geOFyb3yTz9aoa9S1IJvjcmXJlm4qXgJ84wVpRj57fozSLl6Diuw4sungd-qHd_Sxi7YWUcvXCRjxKzbFjNgJzVLPBd9TBFM3jBzWtSd-epTKt8TBd3n9YgTN5uErJ-lnPJO9X12AO2ILcmFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Yeat
📋
Title:
COCOON
🛑
Featured: Drake
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83683" target="_blank">📅 10:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83682">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JY65zdOY0WNUt1EBGeznCEyIkVSDaoJtvIpHhOUDOLsPF0xDQ84OTbdbq4R0f9dAza7da91CuQ0HmDHelvaHrRZmi5Z7z_YJFX_qBIkJSsGQcDEtfz6AXyLXRwsm9EuEMo5czjmgvJY4YpHDHewUtaJmQcRjeSpBqE0KFSZYouWYb7bQus7sO8Hs76PKkJXnYAXbdwrFeDLSKp7rUzUzYYjsf7bbF-Xpxfd64UKg9DZxGTo29HQJ2MDCL0_t2A6l3cmMXzZZQbmMW_ZpOueAddi2bxc5cdmxneYHO_lignL6g50MArxlM_2AkEjsAvDsMWWS4yacsixTYmlXNct9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته آینده قراره به هیئت از ایران بره تو سازمان ملل تو یه نشست سالانه کنار هیئت کشورهای دیگه سخنرانی کنه.
آمریکا هم به چند نفر از مقامات بلند پایه که می‌خواستن برن ویزا نداده و الان هم آمریکا گفته که هیچ‌کس از این هیئت حق نداره از هتل خارج شه برا خودش آزادانه تو آمریکا خرید انجام بده!
معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران تحت سرکوب وحشیانه، کمبود آب و برق و افزایش شدید قیمت‌ها رنج می‌برند، مقامات رژیم قصد دارند به خرید و تفریح در نیویورک بپردازند. این اتفاق تحت نظارت ما نخواهد افتاد.
ما اجازه نخواهیم داد که مقامات رژیم ایران از مجمع عمومی سازمان ملل برای انجام خریدهای لوکس با هزینه رنج مردم ایران سوء استفاده کنند، در حالی که این رژیم ثروت ایران را به حمایت از عوامل تروریستی خود اختصاص می‌دهد.
ایالات متحده به ممنوعیت خرید اعضای ارشد مأموریت ایران در سازمان ملل، مقامات بازدیدکننده و خانواده‌هایشان از فروشگاه‌های عمده‌فروشی یا کالاهای لوکس در این کشور ادامه خواهد داد.
به فروشندگان منطقه نیویورک: هوشیار باشید و در این تخلفات سهیم نشوید.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83682" target="_blank">📅 08:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83681">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odjReZbAmz72hLt4RzDeINeOW4NdhSgu7sX76im8rkeFy_v57PRW-uKfKvfIGa49dwi4tXP2JdWHqxHh41cMbX0YguiO5t9d0lzok8YATX7PI1zKQDc1yqz7n5k5o9koyXN83fNw8mG-YN6dVm47ynZ0HlzxXmvekk4cu8e-mpvFRTuT9vwTaw2JlkYa7dyAHIfJxeV7vR-EVDT682D4XWE2f4d4k0SML0LHp0VDYvC-K2npGuzQNsHrFpeJ-KcYiHXrQQhcPRwwr67w6UupZMDq3YCXV3_SCeP1-zhi3O0QuhjyNcj_kdWA6hQ4q4WrEYKHB0xnW9SPXcExXbsEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام عزیزان صبح زیباتون بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83681" target="_blank">📅 07:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83679">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6UDmPzXdmqXUnH2JtcI2RiNfpHNbNOVELTk8gwzE1bvZiQteo79JgkC7KCecfe0OAUg5eZnnRw8R0t3no__wG9NjG_ddnHf760PczUl2tkWxcaV4ab-zTFUWHo9M8fojH01c08B9b5TyOtw1uNhcT6PNA0TUBDDjEfMfCWGOXsgFtr5Lnm-esT317iGX1Fp0pm2F8H0p38uQZu7mOdFHAqctunycjXNcv7Wb9C2QJMAnnE2LxNmJkg2jlaXBHzNw3529yhOudl9KFT20TbJyOh3JQW_wYkkPPHGeXLpuomcnh1bacLxDY8C4RaZrdX_OL4w5_vTjqIZbpSrSDbC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش اینجوریه که بعد از ۵ ساعت بحث می‌گه نه آخه می‌دونی از چی حرصم می‌گیره؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83679" target="_blank">📅 05:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83678">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvSrPVNfO1ekEy6lsZ8lLLgoiIU-ljq_nHllomr0Wv-RZY03sVwqJa2ck6NcZ4hbrovt4sGeUu11gP4cV5TzzInGSkUUhD5nt34fBm6cjNgd7WLVMVE6bBA-elkRHluhNzdzbPEAiFRwb6Sv5Emm3L35vKDvieZZ00Ypli2UOd2QC_TYe77K30ADI_GDl_pINI5ZadFWQ15VbeU4zG4I46pvgaBVR2LpibPfNuQIxM19T7jOwbO0f7vxqYjqTW3x6IHTKXXsgKz_1o_GHp1M1OxsDpGOHkMTdJxeC1LskJ3inJkDGXCGRRHJpNTjR3uWmcyDm7B5Txur36bu15xKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش هم فهمید که تولد ریری از همه‌ی این بچه بازیا مهم تره و همه‌چیز رو ول کرد تا بره تو اون یکی چنلش به ریری تبریک تولد بگه.
تیم رسانه بین‌المللی و مردمی فان‌هیپ‌هاپ هم به نوبه و وسع خود، این رویداد استثنایی و تولد ریری را به خودش، فن‌هایش و تمام مردم جهان تبریک و تهنیت عرض می‌کند به امید موفقیت‌های بسیار بزرگ و روز افزون در پناه حق استوار و مانا باشید.
🌹
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83678" target="_blank">📅 04:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83677">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بعد از اون فاجعه اسکم استارلینکا، فقط چنین معجزه‌ی دور از ذهن و عجیب غریبی از طرف دوتا از بزرگ‌ترین رپرای مارکت (کوروش و آرتا) می‌تونست یکم محبوبیت پوتک خدا زده رو دوباره بالا بیاره که خب نمی‌دونم چرا ولی انجامش دادن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83677" target="_blank">📅 04:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83676">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVlOwMvH6Ht34yeUCi5uwEsT7RLJWRofrOIi1cRpCzAGIWToR0PKJkg7WqgDkqYpakV5Q-3vz-51sbJNBYso-cQ70rObNQh3diDCpNDmeJe5zfr_y3wKuaoavqsY5wL_GKY_-KxR8n6NQdeFxi1gEdBPAwV8xkWvMQw08Kk7cx31abYkqxFLxqQXd3p1_xayQ0OGtrhdlPL9E_NU3qf1d7sm0cjFSetOIeOBOFSYIpFpI04xRnVnXToq9CqXDzc-FZKRlkAjUhgOlTwvIStmxaDT6A14DVVp8v4vG0KkUYtMhfTwH00Dl9iEZ96vaEIyD3P4_ulXYy9k2v8hVuFOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک در جواب این همه ویس و ادعاهای مطرح شده، فقط این عکسو از آمار یوتیوبش گذاشت چنلش
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83676" target="_blank">📅 04:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83675">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfVSYFfuqW-wefKDPSc0BaUNFw3ruQcGP2PV4kXI5rY-esiv9f9GqsWzM0VUlGJDHTCKBw1Go_A9XmlpBuuVnQrWmUhMUfOxRBCngWjIWJAtlI191HrSdfScOe1uDMaqM_Vpd2X5Gp6thCkhryB-XR7IkBrhyRqpu9ZdaU85CcOIREcuVPPzhaCuKjcGhcbLyZG2wOTT0zIanS3zIr8oe4J68thG3QcQz7oQDCEh2zEEBiR_Nm71iT96xeWiXqPcl4NyswS4CN9G1Fhiy78nV-VAC9GVtbPu9eT9lqZooaWDOAJKQzzKzCRS5g8q0NJO0gGOuCETOy7Cv7QWtOc8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو فکر کنم هر کلمه رو یک پانچ در نظر میگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83675" target="_blank">📅 04:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83674">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">داستان ادعایی کوروش وانتونز از نحوه تولد دختر و پسر پوتک
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83674" target="_blank">📅 04:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389c5e1170.mp4?token=QytTdvZE5QDYidOzZSbKtaLK9XT6qWSQsjY6B25K72lDf3pSqAuBKFnrn1vI-wqWs-zpT7Py2Z65MQdGWw4k8Bd3A8HR6zEgEi3fhgdpJpQG6po2FJDzrYOMx8rcES751n2OP9ImTomscSiq8c7udi0BD7K5wZotlSpY0y9wscP-vD8Neht0RlLO-onRRQuzUZapLWliBenabj3YXc0RTjxtWlIjWqk4XEl8WyGukAa47dAcE3wqX3f70g94AInJ1H4hCJNucgqsIQJl-5m6IUJvpXmckvjSxpiZYySOjgASeeaGBjTep8pYTLMPBnNnFnIH_VmRWQe2d_CSwzkjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389c5e1170.mp4?token=QytTdvZE5QDYidOzZSbKtaLK9XT6qWSQsjY6B25K72lDf3pSqAuBKFnrn1vI-wqWs-zpT7Py2Z65MQdGWw4k8Bd3A8HR6zEgEi3fhgdpJpQG6po2FJDzrYOMx8rcES751n2OP9ImTomscSiq8c7udi0BD7K5wZotlSpY0y9wscP-vD8Neht0RlLO-onRRQuzUZapLWliBenabj3YXc0RTjxtWlIjWqk4XEl8WyGukAa47dAcE3wqX3f70g94AInJ1H4hCJNucgqsIQJl-5m6IUJvpXmckvjSxpiZYySOjgASeeaGBjTep8pYTLMPBnNnFnIH_VmRWQe2d_CSwzkjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند عدد از افشاگری‌های کوروش درمورد پوریا در این موسیقی: منیجر پوریا وصل است. پوریا با اکس منیجرش لب گرفته است. حق فیت حصین رحمتی ۵۰ هزار دلار است اما پوریا این پول را نداشته است. پوریا موادهای مخدرش را زیر تخت ریچ (پسرش) جاساز کرده است. پوریا به عمد همسر…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83673" target="_blank">📅 04:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83672">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=v1K0jFlGJBCAR299XTwAVBTVaYTRz_HlSMO4OsqAMhKTF9s58c8YExGTVTarv4IPZyTQvTLlOxfIkzBqlWaVuBolWq3xicQRRDUH8dCrUOw-_dRq7s2imn2Bp9BfeYP8ZuPAKdKKAATMd5FlKFJnHTJFcQFL9MMGsWhKBDsNDKdq36H07GR98CLHFn7k59t-E_p7NsKIgxCyVHXDlvDlgapm1ftUYXyduiyq14jBhSoa4NDmiVwTDSnfj702NXCzGpkaFAP2-rwf3NWfPA3FMQoonTi2S7uBfgydDD_4KyoVUGoYf1MXJT96TPXLFA6xf7RogzzL8vsEOWlmhoARXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=v1K0jFlGJBCAR299XTwAVBTVaYTRz_HlSMO4OsqAMhKTF9s58c8YExGTVTarv4IPZyTQvTLlOxfIkzBqlWaVuBolWq3xicQRRDUH8dCrUOw-_dRq7s2imn2Bp9BfeYP8ZuPAKdKKAATMd5FlKFJnHTJFcQFL9MMGsWhKBDsNDKdq36H07GR98CLHFn7k59t-E_p7NsKIgxCyVHXDlvDlgapm1ftUYXyduiyq14jBhSoa4NDmiVwTDSnfj702NXCzGpkaFAP2-rwf3NWfPA3FMQoonTi2S7uBfgydDD_4KyoVUGoYf1MXJT96TPXLFA6xf7RogzzL8vsEOWlmhoARXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب شب خنده داری شده پسر مدعیان حامی حقوق زنان و زن زندگی آزادی دارن زنو بچه همو تو یه درگیری رپی میگان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83672" target="_blank">📅 03:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83671">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کوروش چرا به این اشاره نمیکنی که پوتک نسل دویی‌عه و اصلا نسل سه‌ای نیست و چون تو خودش ندید با فدایی و سورنا رقابت کنه خودشو شاهِ نسل سه جا زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83671" target="_blank">📅 03:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83670">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کوروش وانتونز ادعا کرد زن پوریا پوتک سابقا رقصنده میله یا استریپر بوده و در ادامه برای دفاع از اعمال خود این حرف‌ها را زد:
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83670" target="_blank">📅 03:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83669">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1OiRgMjjqEGxr67bjUFvQFAmV6ukTKcorWZBFL4Pw0w7AJr-E9JRWAWKSE0DfvgRS1EasYF37B4Zl2ueHK0chtix0Vje3kIY1rsl0auFoqxmDT3CJqmWde5bL2es36lM1oFQkYikaO3sTuyzLa79bON2jo1BWfcX0O18GaNUS3dGxzA1NZJEva6HOGdmscp9dkCeXUCvz8ptn8FJ5txz3aJGwaM_a8W_mlK2kTUb0H05BYveq1rSSU4g6DDgN-IWtxEa9nby_4ZLq0J0DryLRviE5rjl48zGcENvOprjLWlUPorKKqiDiDepM8p_6fwWBjICLIHPtN8E7sR90F73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا باباش ارتاس جون ناموست برو بخواب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83669" target="_blank">📅 03:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83668">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کوروش وانتونز ادعا می‌کند پوریا در کلاب‌ها به همسر خود دراگ می‌دهد تا کنترل خود را از دست دهد و پوریا بتواند به برقراری رابطه با سایر زن‌ها بپردازد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83668" target="_blank">📅 03:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83667">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaJpIEuXguHLUTXbd0_Zkm3LON19Bw8gprvGrUUPDPJoyzPgFDLugJP-BYmXdlyk5fcBTZl4W44Xt_PJTtTH0H-tRDHfwb0Sen5j0ZLhHzr9U8377x3QYmIUeRezXRPjB0KcrvrB8h1lziq0DL65plsRQb0xuBRhAasYeCSXHb_y2S06uF_XKuz16cXY643Vor19-TJLTVdCVoVXL4jd0atqELorYvCSQhIivu5265N2cYzUyPi5OrIdGRvShoblsVg6hw06YcGSRyeR5qngBTqPQpgqHODvwGyWpf-FpNlWDZGlhYpLYzEAfn4CwvBsuhVhBde2ate5SlptgeRhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش وانتونز ادعا می‌کند پوریا در کلاب‌ها به همسر خود دراگ می‌دهد تا کنترل خود را از دست دهد و پوریا بتواند به برقراری رابطه با سایر زن‌ها بپردازد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83667" target="_blank">📅 03:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83666">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گنده لات یک مدرسه رو نگاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83666" target="_blank">📅 03:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83664">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mR3_PPU-eacxDYrIyoqWxdkDSv1F3WytZOzKOOCsqhBIShBDdsNWv2Tn0RGyxjn25Bg_iriQ2mw8ZJEi3Q0efmTJzkaPGuPpvb8JU1ZFYZI7vDbZRDLJgJjFjBZqL0I57WnRArynCa7XaWbfIb3NTjmLPMgBQ7vBGcgt8AxE_tJu1tQ_fm1hO5HbsxzuU6vtWtQp-1RvLEXQK78Lf48SQYFfM8DjiFI-_Kr6Ez7wM_EPD2vj6goPpLuYa30MF5sQ52w6P_Hc6QFC5XgCvrU5NmdGklrSk--6aTg_U_bwiZMADGQLsz7QIsZJ3mwOvHNdh40Hu2NAGtR4cJfcqV-PnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saqZqkhmu5Vw6eU2SKvMbt0DZ62DP7M-6IM47-z_OxgrhBawgOcSp0HLXzNvMiXEEoBNIvp76TcFinqKJ2UqpF4m6RnKgXcaYpo9euZn62BLMPulamuRFc0Tnbmb_qoomC_WWikgMRbRsFyqrrW3lohZzH7zAi7b7ojQqAAiabhTABJTH4ncA8QapTMdklCQzF3ufWKRTlEoxNwQeqF-_XvyxDwEZLaJWgIegf3r1zGYTHZOdP5yEqNE9PsWrLJovSjj-puMK1Zx39UruQoouGcdHx4W1-p3TPfD5KJbyOABQB1cdpEIin2N-a5_qJS-_SoIEDsVCRntelrLyDmEGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوروش واقعا رد داده
رفته با گوگل ترنسلیت یه طومار فحش به اوکراینی ترجمه کرده به دایرکت پیج دختر پوتک فرستاده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83664" target="_blank">📅 03:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83663">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حالا خوبه دیس پوتک ضعیف بود که این دو تا اینجوری ولکن نیستن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83663" target="_blank">📅 03:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83662">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITxfgGkSTXQ6Pj6OCQ0j8joogENnWKTArqzWoAHcs-GHECQlCunHLfzf3_n95jIlxUYV58a5kQ8Z9C5w2XFwXQoMOcRmvPa4v3metX57z93zHGYsGucy55i1fw51qSQGY2K2l90hbf7GyWZFI_DYGtbcR3IkyVEVzaLoaZCrZ_iGWG2-Qlr5xi0_NhfNg34e9ZNW7e8tf7TdxS_uA7YoR5e4aVXacnKqaklp18SqX5CMEsvw5duMl8uOdcuMTZOdW2OwCwePj4o8vmR7sGWGGjLdARKDONuUOL_mrH5xrBG5G_s9_Sgz3vaz5DZgyOABPgsHjyBLTo1pPxFGnVWw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان من چیزی به ذهنم نرسید راجبش بگم شما خودتون نظر بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83662" target="_blank">📅 03:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83661">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نه دیگه نشد داری زیاده روی می‌کنی.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83661" target="_blank">📅 03:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83660">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جدی یکی از خنده دار ترین بیف ها(بعد از بیف شایان رگ و آدرویت) بیف پوتک و وانتونزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83660" target="_blank">📅 03:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83657">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">میگم چرا همش بگ میپوشه، تو شلوار های عادی جا نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83657" target="_blank">📅 02:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83656">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArta</strong></div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83656" target="_blank">📅 02:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83655">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83655" target="_blank">📅 02:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83653">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کوروش: من مثل توی مادرجنده نیستم ناموسی بدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83653" target="_blank">📅 01:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83652">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تو همون دوران وعده وعید های پوتک، کوروش هم موزیک سیاسی میخوند میفروخت به رادیو جوان
خلاصه کون هردو گوهیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83652" target="_blank">📅 01:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83651">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">استارلینکا رفت تو کون کوروش
مگه وظیفه یارو بوده بده</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83651" target="_blank">📅 01:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83650">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کوروش: استارلینکا سابات چیشد
پوتک: مادرت جندس دافت جندس به دوس دخترت خیانت کردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83650" target="_blank">📅 01:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83649">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کوروش جان قصد دخالت ندارما ولی این که اوایل ریلیز ترک لایک رو بیشتر از ویو نشون میده باگ یوتوبه که وقتی اتفاق میفته که حجم زیادی آدم هجوم میارن برا گوش دادن اون موزیک یا دیدن اون ویدیو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83649" target="_blank">📅 01:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83648">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHA-DEhsdMhWl2H8TFgo4-w5gs36_xBz662WasAJBpeuc330Lxhh0ar0BQTlLr_rPwRjA5eVESz0H-wQP4kNk7F_GloSSN6hCpVU_tYPdHNPxvdPDWVLZ2PkvOJflPH719bpPbqrBLzVvobnovNjQlfC1WafzCLgxPwn-dGTBXbM61Mgs4fRShhtrssEfc6I3upiE48OSTxWCVliO5zACCVm7hOYcaojAral01uhXt3h09RBvXlHtnBbdWZeq_ZzS7MzrpMLfepZtykEFibxIFor_gMYvU3rhRRsk1GxlrEhhUdoXukdkuyxqDlLHV8KB-ixLf1zjPBDv5fSBgf6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83648" target="_blank">📅 01:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83647">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آقا کوروش یک گنده لاتا مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83647" target="_blank">📅 01:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83646">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83646" target="_blank">📅 01:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83645">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خب دیگه بسه خیلی حال داد حالا وقتشه طبق عادت بگیم از بیف ملتفت با تعداد کثیری از خواننده ها رسیدیم به بیفِ کیا؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83645" target="_blank">📅 00:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83644">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SblycIWORvHkyc6hLYamHP0iyW-Ka5MAkwHQbCJqKuztrEBEVRlLJWK_bFxBEF5UKPeVjOyfEneIVLBm-unUpSeUFZ2wuoPMNv5T9wh1U5VKUeVRL7weCImrmeZWUEDaLWJY1fJaXeSxok_5wQHYaCrTqwLfkMdBI7ur9li78LJy3apH68SXXXulMQmIqhnViCAXs9CFAuH4ZVqTZAWj315jK1_1YztXBTFSOYg0auDTdg-J0GUh6q7-voDr73zYnboOO5O3SvGlPcV1FGpwizCeMXseb6LncLJYQ7swhRfr0xN6VO1Z8HBvOCeST41er68T1Tc50q0cAafidlKxOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش زودتر از ما گوش داد ترکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83644" target="_blank">📅 00:54 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
