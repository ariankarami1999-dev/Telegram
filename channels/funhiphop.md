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
<img src="https://cdn4.telesco.pe/file/uuBqIuCxj1taWsOKRqAlOXySBDTZSHa5asfVSOb1MZvYJmFIIF6TMIcQ3VhTCT7K820JdqFDX357GBPj-LFoMJVUzJWADmpelEiQiQsXYqzc_gMDghfD2W5hLrHWJeW7LRLm1mFyASELXafxfL_QazeWxyZTqGUo6FXlFJNd4edd2AVJBS8F9gLzhIYfhyrzLaK1R8v9GtNmaXKK6axZsk21uzr9JSg2yXjijhApTgdJOMpeUscxw_oMI41N9YsYJ8GE1ePQ89x1VUqusD-IiDiv9aOW25AfF4iAyYTnq0oxWMUo1ILyk9XulKzObgXnjerJmYzDSjBf2P60QnrYmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 18:08:14</div>
<hr>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8k3B03QqqFtgIuReTj6heX9bsKzpyWkqjTZLZuJXD-P0lJTti7fzkB0jjwv_27I0q3K5mcu8PeTcK-acs1uAOHbDNA8vgIoZHkK39RGtCbcHftH-sKOaQFJDv6Q7njPXhZojxdQd2K49ncXqsM3xbCywHNtRf0oOW_8JKZSyMHsHVI9gSKRILWbUwns5LmUOBtWbeTn0A2jUZTylJ5X40cW11A4Vjf6HjV7FYwpFTlRGVavcgOCDndgW-NH0GjF_pB2aFIgiDM6BWLjE0fAM1a8kp2KyZwzf1E3Cax1jiQjmVwuQey97Q56ubm5dnR3FDQbYsFeDlWTuHE3aOEIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نتونن تیم ژنرال رو متوقف کنن حریف احتمالی تو دور بعدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/funhiphop/78285" target="_blank">📅 17:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLKglPph_Frox4bUTgYoK2VPwXwOM_AQ4gVLoQ_pbKqo2HnvacDw_y1TEcNl5qmPO0TcaPc3mZWP28b6BEjJjh2EQ8ytbxR_-56VSk1N1rVLMG3itwmdlsEy3ywATlLnd8fdflYpT3c-aYpEzsY5hdp7XNkTjgZpejmI7pR0Q1G3Pq2UNQ-0fp_FBCEivSiaugNa1xlGMTyMztyyyNiv82Kx9sDLzr84Yj2guz3RfAaSNxVVhm03_CQdYcrQ-QETieFPBTYujjIkRkoMfLvlua84nawC8wqzzruD0abI9Hdv1jUD3CGYcK-MhvrX7b1ZEBmJOEh9ODk9_6PibTzudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی تیم های سوم جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/funhiphop/78284" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/funhiphop/78283" target="_blank">📅 17:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ546SPYDOnPVAcGrMpIvSWB9jVjjFjh_mZ3y8YQMQDJP8xsZ-erETJdoiLRN2oKFmw6XCIIoubWu5_TYYq8Gk3gA_Ki05KlJNgiwj5vsrL6DHOgt4lE1IXtt-1bMOE-MgzpY1d9Pe3-icxjcl7dSY6tN6JFS69WZwgiWE7A0V7ESAcmF3G9uJMX_ISxqjGmoz2jV-YQqdpa9XBxYtdJx37p3C_cRlm7I_TedAMDZ7l_iddj1hAsZpyCDyoATIzT9iPj-BY9PJ2Abm8NOex7kCiPzTlEBBbQ4ninwedZs5vOCMV9MweHUBMaazvglvIiyMU3sYBQnZUBp5chdF48nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم بالاخره افتخار همبازی شدن با بهترین بازیکن تاریخ نصیبش شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/funhiphop/78282" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سخنگوی وزارت کشور: کسایی که به مراسم تشییع پیکر خامنه‌ای بیان، به صورت رایگان تحت پوشش بیمه قرار میگیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/78281" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/78280" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/funhiphop/78279" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دولت عراق مجوز استفاده از استارلینک و صادر کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/78278" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rhe04G0qF0TAV3GymFjeMjTkKkSOgTDhY_THmQWPPh-x_DL3KrX5Lyvv5_hTIIJXOV0wikAAcFBF3rLu-IJwiWi_8l2HHCsX3WVgNUNbJYNHejtZHPEcrwU9bxiz4aQgr9CfH-iWK0v62LuEOzMnghxTEnUdVVb2HVJmj7Cf4D6aCczGqVQ7_JPVfgxA-jNzZxRN660YaIadnp2c4E3lEIUTi0rGD0wUREQtGR9QqNTlmfvczpEBsRGg6WLj_GE1j3JkDAJE79BLQXh76yymU_umRuNPRmvSrg9km0lSIVO7Kr1F7KneIE1zVGbEuCWS8_LjuwL5fsT_iVuCwFBFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدینیو و طرفدار گمنامش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/78277" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv9niYtcIAT0CelmNIgBEtmUoVp3zMSGCJfyqa0GITBLe7vxnJw3VUCLKpOnKP4rAMazQptCVrB2NrTniD5hECfZYsNKawPEMeN8AuGOntdy-wK81D5_UqJicOgm87qWtkeDYzrTO235SAfDSN34mze_ehMJwgoymkEr2WoYX-wXRJ2WNzqJZ5WHSukVQc-s7YX5gez0TmHaQOi6nFi-miaBM7nMY3rwWdAUW98yHPwCXynsDMAa-uI37OH8WFBl_BMZiBWxVqgDxO9lb4rzybbxdIIza-eurt1Iy7ytYYuMuHfEmm1Fu-TspEmiDUPfkM4buVSOS2b2pv8k7RZKjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باهوشا جواب بدید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/78276" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تو جنوب لبنان داره نسل کشی و زمین سوخته سازی انجام میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78275" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIVOT-iQ9vo3vqbAO0Gw2DHHnS6FzcmmdbMLJdOtbJrObZHMmTMXxa3SYk7iL3opw3EjUHVf-JhRh7aebY9wz5FbQAOfntGv3zOmalKoJAcl1Y6tlmTizte0KnRx9s-RQN_5ohPC3NyFhj-WOC13yuo6_mSQ4WAW9j3pOis598suLSUktxq_FZBh278H0df6XrsRQ04zoPK8HZ-5bQ8FsAZ2vvPaC9GscUegFFA4QCZmyWsHTYpUen9AE62N7UuwEgzlIBq-4CDaOevaFQrdvNGNj-13BJKYnAy6-2mfsEj2UeV9U71ZBYtLnFJEyg4x9LnZb3JpO_skkvTJ3YuXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخواید اعتراض هم بکنید لااقل یه متنی بنویسید که با عقل جور در بیاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78274" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4X4rVzSepZ2dBxExb05esSqrKW333rk0dwBMOdQKv5rUw3fR-BgiXQNWxliwiSG_JD67hCZYDxwI7J1Gfj1xnjurT4ZDODs5Td_3iuvawCfGz0WUIrwrBKUnxE_9OHekuMdlZ_CpKyIVIjE2__a3HpbdDTaUN24fO6ZfEsrAM0NHv5Y7n6H0-NGKIR4vDnClr0aBccWqpStaNDFwIRYkD9UpU6p1v92kj4ZmJldPt7Q6qRsf8Z-pE1VUjbuAi8r0pPI93XrNlysiHKTMyH3fVHfoJX9gbMAEdNT-YQjt5uuYZlS8sycGfjQl4RARuhayG39VV7AmTteuGDleuXVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیک‌تاکی ها هم کم کم دارن آدم میشن
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78273" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78272" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWr8lWHltcBk-Sdi_0ZKqoM9jyOSY6C7zQLmmQV3fYCPe80p4q7ChKQylFY_u1UWctjFsEx3KyFni4RY2xELslYIK-5HUJUFzvv6fEgailUynemUbSvCy1Q7jmKwK-eSkLprRpgQ7PZomrPQngHgWSU5ggf9kfcYUhg0Y0m4RTqHPKKuciJlsKZUSB0XhjzxAPMMpBH4P5FKsYbbymVszkQGYZ3QsN85EdK5NBii0hZKZIY5t0uvNUKlAVpzrI96FUlyszrk8cTnStkomcBaKEuuHywSEFkH-WfLqsCfQoPPfrOkJKE6jR7qFoQ71qCfCFyL9BvqNjp8twnV5MoYoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78271" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نمیدونم چرا بازیکنا برزیل نزدیک ۳۰ که میشن با هر بدنی تبدیل به شیشه میشن، من دوسال پیش اون بدن رافینیا رو میدیدم میگفتم این اصلا مصدوم نمیشه، حالا ماهی یبار مصدومه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78269" target="_blank">📅 11:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کشور جنایتکار آمریکا گل اول رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78264" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بازی استرالیا و رقیبش هم داره شروع میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78263" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw0wUlfXKOk7jMHp3peWLhZP1Qh1JJ4LrUfiPmNymeEEwvh8Oc4nmV3ggGiMrWxCpqINKErWhuFLbocRyePSbwpNMlOea8iWdDONWwp2H4N2xSAkudHNvnRXZAkpc4bycRIgXbYCYcuhw5SLUsaVp-C5aWkEldDDtYTXZSTrtR0mdY9iRcaRAa736q0kUgKZ9LHzRGb_Yug5rAzFnxpvzKiHacj-d7XcN6NsXsVILnC1_0loX0rqV87xpy87FzUwaQIFLls-Cpmp9-49JBE9g-YEQdOTjMBciwDyq1tgZXW7Dklp1oRxwekLJRECf82WSlpM85mVkNwDvYFpJbntnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین رونالدوی موجود در جام جهانی 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oidmaOkvlye9kLxiXFnPOIPekaEaDj8pOAbiUZdJoPocVJdd40rLzSJ4FaNvSpDwQ5yJfv0Zys2exD_U0LgIzNcx4McfCulnV1auVIkBNaki8XuH8K8eJp9BPMkoOae1_EDz3O7vW8onLyyN0ZykMEwqAxNVJ6YCZeJGO-FHGbZNSx3Ntbs0fodtM4ceUsI71kfMJ6UChoKiabWJ3uFWsfOvFdbuBdSGeS46Ktp3lnmpExqodw_4oyyYJaURA0xIe8qe2vS5Tk1pZNtRQCcfz5ifva5hiHhcC92nC-qVgxKaq0wTeLEsddb9tQaAf5qNUM7_QLfEULTJ5cBgCIOcBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید کون میداد تا بهش 10 بدید؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فنای رونالدو به پیج کل بازیکنا تیم ملی پرتغال حمله کردن دارن فحش میدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78260" target="_blank">📅 20:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Offc9nsst3g5qbCEokUWAW0ETT0YgruT3k2eYp8oxpSik3p2k_rpxz4hAEOXD_3ooysol2GEX-m181QxWx0aKGv3Xdd26N8ZrU7tZ5la-iNt-WUj-awZ4tXTJzi056OI3GBlHtDMDLhhBbRtqKw5J0gWlRt7j0JdTBpXkHsh1JWgQTnI52ymFJAWDacf0RU8eshNDH0h__0k_plrQNDKDBSr-5N6_vhY6FowMXEi5y8Z--NrwZf8pikl8T7vPjMYioOQCF751c2NXFPTWHP8I7PqNhsoiPT_hLSxb0lbqM_VqLG-8-Y7qnD6YcYnJIrSFXyWt2N6KvgMoI7cCG9vuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شایع ترک داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78258" target="_blank">📅 19:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUTfOvnFkTLPywQmGDSUf1pVaM1u3zGQkjuB7PFMMDQAGB9o6VkHwnJ5ujZAWAIAAMvf3-kOfW7UE3nvAIQlCJAdKMw23bE14nfSrGGYXjAL_NSll8012SxYvEA02NwiOQ-JVZCPh_21FgEEFHpr-fkWHrmW4tK9G_ub9JnVllNI3rvuQDgAJ6oBETYa57DSLulxQ1JBrtbM6WPCz9CeXc6li-3uBkixPljNOOJ9MBPOa3gR-cY_CgI6Q8OBSN-2GRWFLprLQyS5xjkW1sdx8hfehwwJUeD1Pm7Sy_nTYRaiuJ0cSC2xD0r3PpTixH9GB7FtWS265BQGNDffe1__cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنیف عمران‌زاده: یه شب تو باغ با برادر خانمم مست کردیم تصمیم گرفتم از فوتبال خداحافظی کنم، به خانومم گفتم یه پیام تو پیجم منتشر کنه که من خداحافظی کردم از فوتبال، فردا صبح بیدار شدم از تصمیمی که گرفتم پشیمون شدم ولی رفتم تو گوشی یهو دیدم همه واسم پیام گذاشتن داداش تو ادامه مسیر زندگیت موفق باشی، منم دیگه مجبور شدم از فوتبال خداحافظی کنم با اینکه دلم نمیخواست این کار رو کنم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78256" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLYX5NF7UuOMhaMZWCivNMtt0yOZYEy0QYFUhC1YLpoXgSNkHoWSIF5tFBidecXCz1S8kidYcFaVN5QPpVqGgwe9NLPhkO-T6uq9ZaZ6mvaCTfAZ4J3VALNJARq0sGp7sZWev48_pob0mLSvKMfRPXZ2SuzZG5Nhj-3b0nqsSpD_1yAW9UvXggv_zAQpsy-RiuhOuEFlbIIk7GfcvoH7hKS5LCb7TuJuSevBdwmPLguyrIbQMI_vzMf1NqNqkiBYcZJHYEXbOWuRhljr2OWn6WkZWe0JCHGN80V-7DVrjiaJSQgAG6GD-l7m4V1SaqJP-xyksSpP2cvZp1LW3wsCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78255" target="_blank">📅 17:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLRFzFTcVpxI6vdNjf2zmN7DSHuWOm7-h48uJLeaftEUwpwS9qSl9vrl2q38h4HBV2lhvUJuokT4xrIl16p2jSNZAKdr5Hrg3kpaF5rJg_yRiJwNxN4KSQ65A4mcHn9fTtj3MxyPdrgb0jefNYEuUeTmU5lzbLUHYMGmVruRjAgJrZypPSFJJ1zC4LpVyxzkEGopaVOUyXzPVvXaZbzI9xe08TmP3BC7Fe6sO1gnDgFgAx_25HRdlXrhA0JuEng9WF6KwP_1-CqAdnbbPO8XoWGd16zdpeQ2u0BgUOCDwqDcvytTt2DQSGIkESXrhm7MhMxeTw0a6QafTqTME6_0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78254" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78253">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جام جهانی ۲۰۲۶ با بری بت شیرینه
🔥</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78253" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78252">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎁
🌳
جام جهانی با سوپرایزهای بری بت
🌳
🎁
⭐️
تورنمنت 1،000،000،000 تومانی
⭐️
✨
شارژ اضافه
0️⃣
1️⃣
🔣
برای واریز کریپتویی
💰
🏆
5️⃣
🔣
کش بک روزانه ورزشی
🏆
📱
همین حالا در بری بت ثبت نام کنید تا بهترین‌ها را تجربه کنید
✅
G29
🅰
🔴
ورود به سایت
👇
🔴
https://gfyweuuchsa.shop/fa/affiliates/?btag=914641_l303106
☑️
کانال رسمی ما در تلگرام
👇
☑️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78252" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWry_ynMVPjrPcqTYVitfzPcg4z7UXtLK2Cy1dr8DXwnxl6KmYvIxODVtzjzMTOkeQDMP0cLsEYp4ibtrkfgHCC6xdp7_DXWJWj97qNSWh_OaRFMt4E2GDeUu6qLa_tiN4ByRE8gbIvwgokJwrcNcMey8zcw-5ErGffR77gXWjFCPt2-MxXqGIUpmIYol89hAFtYW2m-TU6G_d6WTjng7ELKu4mCeYiHhYKGtJ-Vp9uVzNCfzju6MDTvnBI4a0LqOv7T9OjbALqW82EvjEuyIj67SUi3zwYSh3SmNoXZXAdyR6_zEEXvIVwpfqfBAGz3s2VO7mq5zqLyOoJGoa2rRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژوتا یالا از قبر بیا بیرون پاس بده دیگه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78251" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rysKxa1OjS2WKcsrROaYQX63F4hz9v_aNsuoDJ8kXo0wsu-n2tC_8UtlE3cYZ88WY_O_-C2XgHvKhJl5cyq3N2R3HfFH9BdNKcFB-eBxf3jvwpNOvuav-T34odlqaJ8Vc6fLqkjzDymaBp8U9iC0hLXpMtZyK6VZLRWNDNtZ1APJ52kDglxVJsN4ava_BhHPAo2eK7SddsX3abSEVM7DFVhD4YzndAKAYVSwP020mTkd2YpjcyyfEKnrx1AvlhiFsvtbBxDBMmhrkoEA6cK_Gf4gX_xtFvDa3ZSSFszh-ewzmmowN-OArmJaUiai3h6Vq-TvB75sy6XcMEm_RQPE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78250" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMjr5eLvA8oxXBhgIf8IFJkq84511DFYB3XFZh77bpOAucH_e-D5jnNHBBJtpzWaAgnX92ZeLinFLuSMZTgG_KaBb-piPH21GEJJEtTb72BpVsBXwRoIn7UVKCNN93uxVToc10pwadHwc7hwOP9aOELb2GMHwZeu444wVYQTPRctDBusO8TaAmx_m1ImEVVq56wsmm5ElSzMWpWRfU6dj_069wl6-IVGNQCK3_24LXUGd8M_83cny_RqVm159KWGnYet_z2K3lNFyjniMOVA0fEyB7ie0Nt3dqwAlw5LCtUnb-GiXib-8uCI2LjiSOhJRKyDJwMCgUV4ZftbYoC8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به لغو دیدار فردا و کنسل شدن مذاکرات:
«ما از روی استیصال به دنبال دیدار نبودیم؛ این ایران بود که چنین درخواستی داشت. آن‌ها تمام شده‌اند!
ما همان مهلت ۶۰ روزه را تا آخر اجرا می‌کنیم.
هیچ پولی هم دریافت نمی‌کنند؛ حتی یک سنت!»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78248" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_syuxnLHhPD1Xjy6YtFmFwF3XlZp1ky0vGdgBzAX0QkEPMqyjt07QyqRvcF-XTk1MqBH0eiB5v8MTRSI2afbGQWtjQ1s57FxA9R95sPm6_D7_govIbGVHbuh85LneTL_J1TshqaK8-fBKyg42HlAhLw4n3gFfvPSnwhanpOsqCm3fjgk3FUIV7ZODN8AhVAZ8u76YhYIpXJ60PUF9fWSkDby55c9grOQ3fjyAW3SACwEsZkH-6ZgLrSU22Oe8E88v6041VQ1rP-_O3JjLasmH1N_wvFNkLHlrGTOPdQzGhOnu2uJAO9gFE6cbQlGUtKtSPDZuhPhDsiC6ZHQwsl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بهزاد لیتو به نام "Late night drive" منتشر شد
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78247" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78246" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ میاد خایه مالی میکنه و میگه اسرائیل باید حملاتش به لبنان رو متوقف کنه وگرنه باهاشون برخورد میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78245" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78244" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مادر اشکان لئو رو گاییدن الان تو کماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78242" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYmrMk5IXVgpw4EOrwxwfGr7Lfm_9j5H2WRT8SX4SPiaVzO9yKK7O4d_JOvN221SF9heL5hef05fh7PAJNsU1xZB1I0WS_HjdqcPZz8naGg1jxR2VNl-VD7qmr90Ku_vzvyH82P91e6fbJXE1GyFxCJ2y907EaHpy1W9H2RVL9ilB4gFO0C6r9KqvrcLBnF6Gt2SZlKKvBhqpDj5YjJZoA1Doe5PpwRVtd2TJl4CGkxz3ssZNKaVurXj8OO_Rr-BZeG6CMArchWxK5HG_IyflZWutIm-R-SrIcI01RVrwML7ZIbexUsrmcbkJk9s7FffldNHRr0w1xWkl5vbvhyb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم ترین دغدغه این روزام اینه که بدونم این یارو پایین تنه چی میپوشه میاد جلو دوربین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78241" target="_blank">📅 12:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جنوب لبنان چرا منهدم نمیشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78240" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vdvrx5dg7U4EL8jRX0gbzR2n1j6-6ApO8naYzj5wh0iZZAuEbT0_2swQQ8F6evWhMPUewxFWYAXt9HCToZgw24Rd_Dk7UX9LM4CfEUXCJZiFAPBG9hotUY13-E3MSjKQprCaaG4gROvG-K3env87Ct6X6_8sxtWMPOwDdbjEI-f7Y7F4ypYbaBytTmz6kjjAK_hcWTY1ChboJz1AhkZdwx7SgjQlYS9Cl3mkMNem4sqO3BzJS_9NPIk_PAIvA95kcPCnN6M8Nlw5jMxTd29udOGEuEsIMVxj8NVEtDDk5gwsufe8VmoMKbB8HfS0XyNrGP8SqD_ZuRBnl9wdbrvBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبلنا که ترک پوریو میذاشتم آرشیو تو کمتر از ۲۴ ساعت بالای ۲۰۰۰ تا فوروارد میشد، امارش تقریبا یک سوم شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78239" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAOIgFacAPXzg85YbDyA5cmBBfSTKsjGI3NcMUmUNOhzkiogyNo9GZOyYCcGBTadyFPj5-Ts3tpmSykqbSgOWfERrpReS6M3lTuUJFytkNgHb5c3NJv9GYL_zeSK7Tri4TS0YSky4ybwWeoZhGUCDN39p0meylT5SXoLduZ1v24oDZ5MnEviNiR3i6NnSUKUt_nPr6cljUUZcLSTXsezvWX0H__qxSC_e7vWzyh7uh8jKrCEy23DUQQV_izV4Hf_A3f7L3lATY-YCR-FdR9-qpLZArwh2eOLpgtx2FdkU6XVffkjhi-wp29h1qE4IZivS783Otk7UwtQDeOHDTy7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای مادرجنده
💔
آقای مادرجنده چقد فید شدی آقای مادرجنده
💔
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78238" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78237" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78237" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbYaS1MJFp8wxxgUyF5bikyviHsgKqMqIX6pP0M1eOB7NJfb6u2_cS2HwarnBwohSFOxcWzc5s6CfsqwMsvjKCRcbQWZbMMl_IlSbAzkxVo19NJ5dLETu09G-Qa9JgjQZm0275QFKDHGAHH_L-LAlAqjHfTYRd2XpQkMEiP49Zwfo2uHdhaAxqZ1HLY7h_w6xSdtYpW3hIM1iRBZoNyHOeZg8c_tC8xOjAaQdzMT8AlOX17RXuaybcHbmIpL7viufghuseTfjuVeaeZctQBcL-zJ5Vj9NnwZhEXYPhN5PRfe5ktiCTomf2InTdmJd-2DFjP0tudSwoP9GqXCtrSoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r29
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78236" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سوییس کنسل شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78235" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ولی سکانس به درک واصل شدن حرمله >>>>
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78234" target="_blank">📅 02:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستان کسی از ساعت دقیق پخش مختارنامه خبر داره؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78233" target="_blank">📅 02:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78230" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اون سازمان دریانوردی که اسمش یادم نیس: تنگه هرمز گشاد شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78229" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تروخدا وضعیتو المیادین: هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78228" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تروخدا وضعیتو
المیادین:
هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78227" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شجاع خلیلزاده به عنوان مادرکسه ترین موجود هفته اول جام جهانی انتخاب شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78226" target="_blank">📅 23:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIn20Ba7bDwWHx1wylsQD5trdX7gVK7zI72yYdjg6q194jyXO8QetR3t_GDwHDUFjd3_XgLjF537dzZoH06DGpkZtswJjvVvBc5rHdSCHG4nBj9PsPwNd0g4K84Os3Cxh_F5vAlH7JFBsVvSZjW4RTjF4H-PaZ5XwS_LHiyM5CiqI_3lwdzLMCNqoLvOvLZ8yVm0O2zio-mvArkxZKBTKnTQi3ScT_QGtlhbtFpj1eavbgJipyvd_73tspSL_OyBmpzA-qyVkzsVn6jZP34c_9JWk0Q9jHRTooI74dkmhKugmTK4fswhO8Kj3mvNDoqGSVbJZOKti4KtCzEX6_pfyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام چه داره پیشرفت میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78225" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78224" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWeera news | ویرا نیوز</strong></div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78223" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDO3k9EERpKeN_Fc0VYs1yU-qqMUkwlxPrLY-2eYTrkVYU4gKPIan6xrfLd2OUbrog8d5yVVSqLAHclOn9j12x3aaPmnTN45CnCtZaIFW7bC5USiDd5nX1kNj_JklFzl35ydYLnAscKBsjJaGx9ZJML_hhJdJTExSo3_ZATrbT4WKFyb9xiFYhAOL-LQVxcwv3dyoY9DgHYEmpHgBeMW5UcvHaq6iwif1Yjh0plu7WjBeQy8ejsxbiUA2gLtXxxBNDoJuUkLYsC4CFpYKA64kY-sjEEOMwgz-cFVPc2cAVrFeuP9KgS0rrsdONk-4ThA92bofJ_AyC0ULboFgw4xqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون ۱۰ نسل قبل یارو نسل کشی کردن یعنی این دختره خوشگل نیست؟ خار منطق
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78222" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب حل شد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78221" target="_blank">📅 21:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شما جنبه افغانستان ندارید، بزار یچی دیگه بزارم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78220" target="_blank">📅 21:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پوری کیرم دهنت کاش خایمال نبودی</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78219" target="_blank">📅 21:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تنها کسی که میتونه برینه وسط مذاکرات تندرو های داخلی ایرانن، تحلیلای مرادویسی من‌باب نتانیاهو همه کاره اس رو جدی نگیرید، نتانیاهو خیلی وقته قدرتش تو لابی کردن در آمریکا از دست داده و توهم اینکه آمریکا سگِ اسرائیله هم از تفکرات رائفی پور طوره
ونس امشب یه حرف حقی زد، نتانیاهو بدون ترامپ و آمریکا(عملا یعنی بدون جمهوری خواه ها) هیچه.
تا فردا صبحم لبنانو بزنن هیچ آتش بسی نقض نمیشه، ولی تندرو ها تنها کسایی هستن که میتونن کیر کنن تو توافق بین ایران و آمریکا
اینکه مجتبی خامنه ای امشب همه چیو ریخت رو پزشکیان اگه نتونن جو رو کنترل کنن میتونه استارت یه درگیری داخلی بین موافقان و مخالفان مذاکره باشه
تنکس فور یور اتنشن تو دیس متر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78218" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=Lyw2AJxfe94gsi1mq9peu3YLkU3bKDVUmevbHd0kVd8XIAN8au4zDViNeeaIHuddqD7z-NFl8oTNmN5fIDqRyziSIdv_3kOPxm877GjeHxerSWofzM_R6JqOmPREWsxttTCphSmhozhHv3_LA2lvi16IHl1Tzum73yvkG-PDW9exyHeSFk6N8nK9mg_cgd4LLe0cunrwH1q7P0yF7mN1s-KXT46FmXAvd548pzSypT5k3pW9dzd5koKt-6YCnUbKehOX_42tqxJZ6hb1fcmDXeQsW1j1-zGuOyYWanuvHinbdO6WYKczyE9i6HbohqKaYRbwwx_IoDDJrV9XHlaj3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=Lyw2AJxfe94gsi1mq9peu3YLkU3bKDVUmevbHd0kVd8XIAN8au4zDViNeeaIHuddqD7z-NFl8oTNmN5fIDqRyziSIdv_3kOPxm877GjeHxerSWofzM_R6JqOmPREWsxttTCphSmhozhHv3_LA2lvi16IHl1Tzum73yvkG-PDW9exyHeSFk6N8nK9mg_cgd4LLe0cunrwH1q7P0yF7mN1s-KXT46FmXAvd548pzSypT5k3pW9dzd5koKt-6YCnUbKehOX_42tqxJZ6hb1fcmDXeQsW1j1-zGuOyYWanuvHinbdO6WYKczyE9i6HbohqKaYRbwwx_IoDDJrV9XHlaj3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6JfnvYPQS3_a0SD0l3I3t-Ye3yEkcPZI-xRCiwXiRirPfdsQfoBbraio2zMOdX-YmOK1RD0u4dXB119wSdvVJic28OJ_f6_BZFrde-eqq-ahiaWK7xsH6xQCaVsvgKof4SuZbjBkqoZZ2pmnbsSKZG7rU6zdbRz6LaCXbdNU2mhJLZbrMy52iQkfJ7nuvnE2xx6LChM_6RX6Ve54w7URFtN7X7Pz_T8_oqjTG84g1klXZx_v7Cvo0hWK0-XDAm871mgp95m_siGbPTp6HJ4UfxdHGD1Vio1hq1SzsrhdQZvZnBh6PMNIeWh1NJw7SLczCmGa8K2ikYDIxxx9q6W8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78212">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQtO6mGSp1XPtO5wOkUqboG6tKFcCSioHLExjGMGqTe324zggJ8ahWLHsHcL3hg8tRAftPumlQrJpzM4FIFNSuHG1lg0Eeg4hPt-EvqVlPUrDucXbXU8_ystvBWB88MgK6eT_MC3qznm4nZVLHz2qRozDLiGR_EUETzD4kx5l4fqCcJBSfA29PC48Rfk0wh36ciWLbHY6tFt7sftBs3y5K4vU2h1BGWLqwRrjLUvUTKrwZ7-wuW3_fSpDgNC4mG5JHVdHd8wNYobV6NUMM3EiZkBqxCsd0QlsFLpxG95sAEEBffQvSuw5ExqbFpFbe3VOrHp3t9BzBeQZNizXiBTXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری عماد قویدل برای پوری
@FunHipHop
| Behi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78212" target="_blank">📅 19:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXe-CEJSSKBiaN5fbmMmvzuiJQSDO2rcsMG_0IERPIRf5M-sGSYTmoDW5pOOcSReFeyf5IlHLZi14QPVqTuBM4uY-z1GNNCj3zgM2te-0Esbuz31zFnjFWFVPN0q7Y0jpd4uA5oPLH62_QJaQ7LiwXcYbXHRk7im6N0ZcQ631hHxid5Pane3lRzH8Gw6vi1cZwbVIDQIVVCwWHUb0eaGfCKAuGNEivk7g66FiuPNBbtL-gIFWFQAADQKlX5idQiStmpusmHVJMybIFAwID7mPIUwloTJ9tDiB-iNNE42pbAhDkOPWpohlNafhYIQPoaVZ5VNelfQOYsZPLP6QrIDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 کامیون ایموجی خنده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78211" target="_blank">📅 19:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78210" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78209">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-A_ggeHnofg2_wAi_7gDR8WFZtQam9Cdnnt3GsU_-wDMxcMSraE-X1Db-pnkSxIwcaQ1rA2Ew0nWT3sFqLR6mZ7edGgRsWHfBygEBJCXPWwM2O5RHxmsrUxeJdiPCKW06ln_9GccFx7Q3U6Z7ffhyexH0wrp6eeJxT5JGb7l-PoRLtNaI9WjM4anPbcYViO8nESIJtuPBKuiSr1dr7s2SV5Ejp6wwK4Ws8h5BIPMSELCidIpx4A4V_GhaCRaKVooSXL6e0AUNtNkNn0y-4T2aX57-9gkQswNJWWhtMF7UuO4cagPxdl_nhyb569Ub96fS3XWvxBPVZP1rPdZibayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم منتخب هفته اول جام جهانی 2026
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78209" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Htt9DBtr3ibLjhrpa_vM8VWjsBvCzjBg1OSw3Y6okL_hX8Ak2-tBoB5lFL_er_wdwZuYOhDyMrHKoAcxJDwhIXgsTPoCihX9K-Y0b2_6SH5yvmdXcrhTLouMCC_pa-y0ONRfnpNr75ESWF8o9_tbQuxBx0DDbBf1fmsfCa8UcZfLSTSb7U9URPkiP9BCvcPxBAlvlJixjuS3HaogCs9PRjqIQkckMqy9LEkUS6alHSlBtknbneXTHQGxdItUHNkG_KrKegi8mY_R7SvCIOcxY2qmWMCpH5l9uon5SV05QTomefYbpmY5q2Bza3kFsZSVH4emZarAjiTcIl8XpPCzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ساله ترجیح دادم پول سیگار
بشه غذا واسه حیوونای تو خیابون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78208" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78207" target="_blank">📅 18:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVWaE8Xi1Nv98LvvgxZyLCHfIv49pYFnJHXRsNg_GEd0DTe7X6cQBducNQ-zMb5P8proWJ7aB5JHHDHggf039zcYFFZ7e9wNhXFvvUs__xYqPAi3bDLDL5LPhXOolO96i_UKmNqco3hQd0ZoEw-ZAcbPi00yv-h-obHbzrbr_7pyucA-wLVLtIsF3vobshCsEDVWBJ2I8EslpUy8k36s7znjH20QAjeyCyiKHw60JeY7pjEEiwOVvxnY30I5Q7dbITNRlmSZyeggKjrGXwOGNhUwNGH0Xyy6vATrUAu9Kkr4iWofHkGTN9U36oYqpuqMDZx2eAH8vmkqkoHaVeL2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب جام‌جهانی
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78206" target="_blank">📅 18:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt1Pn1Sgx6Ikv4358KhfJGBK-P9MlGttvP08z9HceZ8LXeNccvNHuItjRSjg6mpI1bu2b5TkinVlQWMrHkx4J8QmOF2RMOrehIWqvZfobAA16O1z3wwU4moyubR1pu-HLJ63jNy8yk05WmxrDvwsDLRyU80HnPk41DYkOyRPeZhd_m4XiYf7zl_bB-Y0FS_9rR9hSM4E1rTpS2oem5xpyW6WVujXQYH5rY28Jdqgm4opeAmspLVmdAeqbBw97PriIRWW8LhYJvXUXrnrEXUhg5MLSvCOo50NNSgFdcoUT3yrDsM2mekTdFD2Ax35WlKdwHyeRzqS31kRQoUP-jn0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djJ8YdNQJGJuGGYCiMMdem_ZRUhJZYwQKGDR63hL_azwcgUoLQdwPCtsQyAgo_fCsU1xL_c9GQdUrAiVtP3_XXjtpXOg43PmMpmBtjb6u3S5BVvOOrt4Hdq2zVc5k3Y6qcdaoV4KEDblz78S8kBnNaI7dw-K8UKOOx2qNJijJAsrMBCa6kE9B9lwwAtQLeTGlTuQ8hu777BdlANzOKf1AfDk9ALi0k14qy7aOUf9QIqkZIN5Crl2dZzP-1oSAr4ZcEz39AF7IcSFb1dl8sSegJPapIoowDlzL7XV6DBiDPJGsSs6r9E8UDem5imEy_RTPJms3bCVikesV46lTe2ffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLgfguWM7FW8vXXbVTLhk40-FfVsKs6b1BYchVvpAXLn_npj4sB03whDYqtC_dNkFG1pR426aRXWC7Y5rzm47Knb5e53pE1XHEa4mznXh56QRYWLaQsWkUx8fq3-bqAshMHjqt3PTIwgh5gSIIMLid1RkjFKUYKFrr9zSYGp2PAsCx9jXoM6zrt-Yrkw7M0POJr66BzER3DC3gzO3OyLj98cbdAcsjbz9JIYA2htcMy4EeWmkgnuavFTPv2n9EWDBzmL-u8qW9Zh0Mzo0AduApifOvAO6lz3jsjRJKROENkoFbi-grH1_39mlMqQJ7A9tCJOrbTNrnUH_o6Ht0dM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdQbLlBBKZBhtReaRlqTQ7zL8CRCSveDUpPiPIjvnIc_QPLx1peN9nLHJJhUYdRYnPyNP9cO2-Pp_stazDiRJ45rpWnj9SvVKO32L1yX462JhaUiXpyCMcOJgZUo5ddV7mg_Z7J7AdHKVT6IdojVIG-ESPvDp8--QAE5MviJprU4DarJ-cJMAddFxB882rvHWZN4UBEI1pHlwMV9apySGD0J-BRILeds40J0Kv_BbBcnsxxg2ggSzrzfuXG_5yyz-ifmtNpoHLimkMHckxuAv4Eb5DuUhUY2tAm4xtvG8qFTkrp2FDRYoFbEKGkBGCJQeDYkIu0YOBRZJrFvPrusbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzICCLVLWg0aZ4BfzbLo33zIrS1RbSBhAo4CR0KP1mBlrPY2Gqtk9BSqSJFUlOt2GcKn0TlDb6s4c996IcyMrzRVTjaoAkFc9KDXjVotzuoX0W6Cdd5w8qyd2odyc69EsnaFDEI_klh8YyavdYu36iKORMZ7KoquX8zHl2BigS9dUO-6656TB_gvG4fe2N4ls0qQmdHZjlcGVusWRMvXfTmUedWkwv4Z-qCk3KbI9mvyaDzktBH7u3arDsALEJxEn4owHKYZvH0TBAYW2F-rbJ0wzbo7mY1Mssr5sUrqSnKMsTIbuKHmbqWL943owe2Ao3Ig1ToJ_NMAQzMpGtxMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سنت خجالت بکش کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78195" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پوری میخوام برم بیرون، سریع تر ترکو ریلیز کن یکم بخندم برم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78194" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromuıǝssoɥ pɐɯɯɐɥoW</strong></div>
<div class="tg-text">مهدی واقعا افغانیه؟ آگه آره که کیرم دهن صاحب کانال که یه سگ افغان و ادمین کرده</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78193" target="_blank">📅 15:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ef661660.mp4?token=Rb1zDMaSaIV6L93wTqUvALIgJTcT5mqYI2xx0ro6D4E-ELD788uU_3Ne83uWRowJreeHQpyiX9-374s-q3nRjf8nzWUdEarxsOlwOCtD6Dez1Cv14TokyDx7g8eYOBO-CrtubfWFG7AZdDuP01vhEERTp8eJrNqGIFtoLG-Xzm2nQZSyVt5fTXso8XAjSCnsO8CEo-2RDl7KPKc8lRkSu_pPBf0KdWpKKiCtyozBNpIbJLK4-PFrKXNlnRZ2Pw1p-PzizVipcGyiXCuI7Ppuww0w8WkalY10B6cbr26JDFcNYCO3NcuXmt2vfCAyyCZJR_et9y-Uwyy3vfep_pRxkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ef661660.mp4?token=Rb1zDMaSaIV6L93wTqUvALIgJTcT5mqYI2xx0ro6D4E-ELD788uU_3Ne83uWRowJreeHQpyiX9-374s-q3nRjf8nzWUdEarxsOlwOCtD6Dez1Cv14TokyDx7g8eYOBO-CrtubfWFG7AZdDuP01vhEERTp8eJrNqGIFtoLG-Xzm2nQZSyVt5fTXso8XAjSCnsO8CEo-2RDl7KPKc8lRkSu_pPBf0KdWpKKiCtyozBNpIbJLK4-PFrKXNlnRZ2Pw1p-PzizVipcGyiXCuI7Ppuww0w8WkalY10B6cbr26JDFcNYCO3NcuXmt2vfCAyyCZJR_et9y-Uwyy3vfep_pRxkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچ یک کانادا و حومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78192" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">راستی محرمه، پرچم عوض شد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78191" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انقد همه پرچم گذاشتن جلو اسمشون منم تصمیم گرفتم بزارم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78190" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duSZgaY2w6jvtB0iIMIoETZWXHvQqWowTeKy1NeYgSGLQmiLj20qN5qN5BYOfljEQeD2olSZIVvU3LBrMzLU6YOCLr-dKU6xF_nC05v9n497aDc290Vy-vboOvIfMF29CkfGZoG4i1sKc4bZ2pqqqd6ghO306X5I4Ng877WPt0iBRzrsvGoUoEKJm62kjVz8vHR9fogG0Cj2Y018yNZj64j4F421SgFwYjhwLjzvLTFipIulIaLhJr7wLXhR6kiSSZ13wrkAsaLawKIJ0ukJikWfL-QEgucRPkvYXTcOZSISlPmctzR3RW128yhbfSO3dGEklffmdmOeFltIw-epew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت اوردم براتون که توش میتونید خودتونو درحالت امضای توافق با آمریکا قرار بدید
پرامپتش:
A tight close-up mirror selfie, black and white, grainy backstage aesthetic.
Subject 1 (Foreground): A young man with messy, sweaty wavy hair. He is wearing a tight superhero suit with a web texture. His face has realistic battle-damage makeup (cuts, dirt, bruises) and he looks exhausted but calm.
Subject 2 (Right): A girl leaning her chin heavily on the man's shoulder, snuggling in very close. She is holding a small retro silver camera directly to her eye, covering half her face, smiling.
The lighting is harsh and direct (flash photography style), creating strong shadows. The background is cluttered with a hanging white t-shirt and messy towels. High noise, raw, candid snapshot.
‌
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78189" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78186" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78185" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0w_l2eUTuxwi70p4E4FF0gxL0zKABPBbDkEmQ9A_EHiDi0_Ok_IAMarcdFwrXzUuAGDcHUMt4GUAETCsN6reJJ0hEkyJ4wF5yHoqpuSDyQlrzVxAaAmgPSodKz-ZlND_VvaRBK3FEk6Iyyg_QPXUhbGOyHcAZEkPeGN0Tux_HmAs7tXe6I7mPEJ5haSLcYiiroxAXDUB595aUs0Kc5d-wfXjoYNJhUHU8NzXVevsRGVzwsELVudo4AAqdnWiMfmgbORqJH_a1kT3k3XPhGVR51UtTAstrO4hF0AM2AzK-X1igwkDcbQfiGK8jC_f9qqE3NkXxOg_jcBHTTYdMOk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78184" target="_blank">📅 13:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب دیگه توافق هم امضا شد و مانعی برای سخنرانی مقام معظم رهبری در ملا عام وجود ندارد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78182" target="_blank">📅 13:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78181" target="_blank">📅 12:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBo_NLNWbj-YUPgZ3SWB53saeK0BsCUaq-jKZ7wGtnhldWW_Lns8MA22iIJQ9AAXhSqOgtTvsof6HIN5aTPqe4i2oy-PgYQdERcbWHjg39VyOCMApEnVvnkBMgpIM-E-_xdkPNbaBrx-G6ou--Hc5P-R6KvdCAiiY9f9kkQAarsiseryF0rTw_wjkOVG1bki9LvilFy_af5FncWGZpHsnEa1YAWowknN-AxuOsYOdTVWwRRbv-gLBlqNXXxJG4e_zCSqTBsyrM_WvKRBGIE8TgLBdsbvEXvu22YzzZ2KCcamPeij4kwjfU-Auz-jStTX6GuUvO1wst4RZzHUmYusQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78180" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عرفان چطوری میتونی انقد کصشر باشی داداش</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78179" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آرتا:‌ کصه بشینه نمیره عین جمهوری اسلامی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78178" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78177">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78177" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78176" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
