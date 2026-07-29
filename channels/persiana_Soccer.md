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
<img src="https://cdn4.telesco.pe/file/Z3Ch8Y_mxb-anIyJIR8PBMgI8u5-UGKPWkvQCO4lOV6FJjib6ZQRPAHMIcHj3V_iBPdm8-IpO5Iy_wl1WKkOt-qEjJNWPAtX-J1Yu-yz4WsfBDUK7iebyBfDN3KFs1jW8_7mOXGuAM-2Amx_K-aQO2NrZ8B8q5-Dfdjg7QGNsCOvvWF-NltI8nzsTCcUVATD9QYsCPVNlYoX1dtYkXejt75ldGGjW5Bnt-Z62iqvTQhz6ddS8Yc6OBN6NRgUeUe0J5Q_S8kCXKH-qXDOfpqvpHwuwDxKpJfZHfelfVUPxYXB2kibrO62yLtSdFHJmlVpM-aLou-uEkfevvKaeLT1CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 01:21:14</div>
<hr>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqXzCkLIMtXGKhY1O97RiCxHAooruwT1CcydwUKIGR7c4kzrrBavHDWbMtLLTzR2tzxQdWMZ0fWuHxP0y0pGK4coEfeeeO3F1aCMUvC-FIPU0-urBOZvPgulxdWVdxrv-hOSWdXYXEz2C_FoqTYBNn8dz5HVZuPH24nYC_WfPaa3XurURkApQHkOmC2a4efCI2NvJISFrd8anb1Mnx9VWdxYixmCeSrpPcfgHeVCgqmBiohzf2NF5xFxBhZSshqxXWWGYpIUntpXAqnzl1kT-xpGkIHn4BOEuhtryABfgPR7BPMWm6hrUQO7HQLFKMO4Xm-WswM-y4ZU7LvCDYmXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKLAlL-ExMUGqoAsMb5D-v1kRt4HxjhzSKljxcWCJZXjRFCBhlm2gqXHzfRlpwPVv6GohTe9mIG33ONT4D0gtlkaNQSs3EIn3ltzS58iQLY3vLb5oul18wZ9f2Bkh0KJ6Yv0OmOVV2raLhkcBhMFWjKuBQLarQsfQbeFTstkAqXsvk_BFv3Q-Y-Unhvl6LgBD5ikwuyXgBlPTs9nV1g_6LiJFaoM9xiOWpy2FPDr2dZvhfktSZrpmHtfaQ4UQ1NkvHlcAADss3my_qyyDIbNPUmHAFRxs8lEm3-DQDIZfgJcNY-ejKCmQR3AqMD0POElobLEcDL2zEM5E9cnso4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26790">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAl5Kmib6uheLTBuyPIoMfYKKg3GdJjXj2Ell-N30o58IV1RWNpKqcPELlCLVWfBQdbIRwNCqKfMByjtXq8qe2htt2gQR1gbqJDH7ZmYLy2KfW3EKFQwXE1yZN8DhVC4Iql0-ZOsi-90Kd1MB0yCdb3U2gnhD7ffp-ZGRzYdidYX3zUx-GVG-5pVa4ZvUD66Ti9GVhUk0dnWDE1B6ba3aJZ8ym8Bl6pg5UptKMOD1gyKW_CJbckqbQReR4jXj9SOOgq5_kJ4PssdWc5X2Sa4qWY2HTcNQIKtn4JyfPDsO4KnMxdrOV6Ay5u81kPGWQ7NeKxp2RyM7qrmDcbY-uV1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/26790" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4HoJ6m5_qruuKxpO3Lnp1nyXDdFHOqijscSsCV1Z3cIJ_cO8Wyy2AQs7WmN4CHgcdcuCmTJWOSE1kLEQ-mHse6bdEttgohjXYmEOQ7O36WRDcpraF-K7rA3BioLgd_7DeKZNdz5phiBR33Bfp7QMOGc2JUHhdQ9tDEveP5oiY9ZefyOSJXr5wKzYYf14f2z_qo3NDshZnBAbiyFGwb8sVdK-n9u2WQn551aQOIlmBflamwosMULxmbT_feZL6gI0LxEWHaG3fsVXL0809h9hlqv167D_eZI-J7lbcWkgjDXIrJwJJeaeJJVRRSDXZgAiPLDGNM5e1O_OA7Dg099Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wie6JgANgoom_Avx6vLpS7p1oZ3mO80-tZKsFuHPjHewAKJa-do4LufBgpbrbsA5sNkmONJiWSsUgXkoQpQfEH8G9ZyjZ1xgssGcHLKtp3mmIO7lfmVPDQWECpVCETddFxIiSaNokaZ3I5I0tc1PcCqyJ14MM0J1clnpcmbZjTIggne1rg5XmjugCNX0QchUVY6Ev2gaoZ6K0edn7y2K-g0QBX-dNfLX1ayOEq7ecrofYmwh_IcO62T5nOded7QoieaeBX6qrQh0XQcH-oLq5dQDXQFd37q3iG1jrBnJ8yidc3EVmZ6tDTkM_H5MwCXBmmdjgzwsHWs5RA7mJwYy5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GswMRoobA8GYonPTH4oHbCoe6yezwLNzbhfFqwXfX87e1xwTNJ9ZppJBVNez2v8kMCmuvOJ4hxfA8QLz7AeUS4HzY9baqZch7YGGHUuRtMlwojURWya-4ahPILku56Rqy-ch-Qza6jIZLE-xc9PvSxlNb6KlMBlynb2EiVXnkUEkj4lsNK7wwG7jeUCzijdfGuX7T0EwkyYa50dsCHstLSN7EyYRL70aUd4v4mIgOYihDxLr8bhpLwK9BhOeCv-OgJQaiGLTgOEbUa7ZgV8TY4VGAQYqVihgYYpxZIth1e-g1tM_a_360iqpjH1asF-S3MWIyQvFcuEI8BQ9btD0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJmTNGFdA9fpcR1jWhaSfqZnSfHboihMhmR6TcmxB01FPHTyIM7yD7Y85Fqx8e5yHYFaOSlGUWnBSrUy_OYA4adXdoBA0RIZGt3gIA1uXnfivcfW0ZEiuj6rO_D78p27JWtsNiAF0js-ELF8Kr8extCa8ITjwZcJ4Sd8W0XAB84UA2EqJFXxSKlYGH8toeoFJKCDGiNaeAVQmnSGMmlN87CcZz4aMKBsvH2rbdxtlN-XhZw3KAMSI7JHoyluBrV0jt5KJil9yZuzMhIitou46ApVk3nEvdTY_IdjZ6v3bSFj57q5kA7Arw06NNq6iUaWKCXWBBHqSFAx_UnSx2fPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOiSCF02LdkNe7XeUEA2OX8-fI_9HdyCUxMvf-adhWYKxDYDzOv4g0s396P_Dxp9k_CRDGIAbG_K_fIuLMx-ps3JxqU6wvEvpyHfFM2WoVOkYvYZ2qRfoU7WN9jz8EslTQHHxzE57sdn0INz9DwNEaa4EfMv2x7sAoD-UVsIJLeO1i8HDl4uE7XquBKi1JwJv0BrNXMLOnDF1zgtrb6rbtLuQnaMxO-Xf5x-WfBGqG5RCdnZgOGBriPBSpgZ_bAjBicY5g7e8roM71C4ymBaQPlNiDmEC-AVeuHF74x5K_tnyoaJR8ZVNAvqIZb5IXDU5vypKsZSQuyuCCOwYr_i0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOxe1LFexCbOHlVa46EMKe3whmsUYawgjtFT2tnZ0H5u_SsCUIIeyZ9DwdSgvwgLwq8ccuDkTwfpeY2igQyRYbTv2kH-zgQrQ-u6QdZEqUnPT0inNnZjBlgmirQACuZ72H2Xk47gOkABq6Ho-Eq1mmuGoNPIi_YCa-q4ZhCzil7fDmSzFx54TMFqLuAN3npiFgMkmGemJwczSKi7JW4dHAVOyt8eZzCsk4WhxhTDuXvuyy0W7l1XjkkliyKr3hkYXu2WINXuHCFeJO4Ax_7pJtH2RnlG6E4mImtbvXjIKdwAHisI9fgDGldCfToDMxtdDoLwcXuXsmuwSQvrrgVIgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbR00GFTRWAt3QXqCJhSjEOMiBNkyuRXHx8Z2Ay1ZnOxvWhgGyU5aZD-GaZRWbOBs0mPSVgcy0Tmo0L2yCRlGPIlmDbpsp6nMQW78gK0FiXMB1uOl7mJeXZk17jidD7YWS8Ipv7gEBt5JL5O0m6qWFZyxFR_h4-aYwfjU5kqj1PiXP83PMo-jDQL5USA02D3mppjKtaiwK138yO_oF-vphHPkO6G2FHuF4885zUGsKu_LEPm83Qghbz0nYi8KrXLtHkKKk-prhuKbLuxndDH9wft9m4ndydh-JhltHEEDdjvBmue-9WSF8CPrzwsjemRWAcR0feVPVPK6K1Cl-RcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi-4SOOeMmEtmquHY5lqGqFJlbqG1N1rotZbFboVSDgjt6Z5bf2gNPVqGp8RnU3hedYUElT3bmyRMwJi48ZY3rN4usDjUdYKJVW82se5slxSgOp8JcSsbBye8iTjMZuN2ES1rsuOiWmEFRqi1QmDG301W3sFhloiSe2vTbiBwhQgEzG-Dg0e7QiUfCUTo486xMSbDyJReodhhrjtcAmzHzQR0d4oqW2pC3dDTSMjfeGg-YC9UKkZxXuxdSNL_3iTv1OD6PEDf7vc095YYpF2XG-Gp-JJdMjpKX0a44XAyuDYpgkzFl-bmRduz6FR1P4fJCJR7waQXEF4zZbKjSBCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEYuUktl0rcezwmTOJfF0NLqzkxLfKLLd_hSwkb4PjxZTRB8i82cyjbr2svo5rqybgRHaNwJ37svPvTFZgBwPm3nm0EaZIz0Ct7Yi21Q44-yCcqGKqYp1bPi-3wXKyurxihNPNEwRfpXMnodYo_s2_6-yfUDtZh514MXlirbSx3JoA0pVjG-RiPiC-AxuqVgxNh-oSNsKo-mtEVZ22X-tqXd8vzbI9duW-sKltZ8O22K6_b4_2tdRfxSUpngxXznqbGvdTfUS_NdxKMb9x4dFSIqEhjqOD3ATU2qmwS8Sduy3GxeCCYnVc8EJtVtxVHuKwVD3S0wUbeNDiVT19DN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWzOFoFdeadkCYEQBbuiMg2C-4Y2fAMF8BP7SQhpyZ7N7tubH4A3kZ9TqHEer3Yi-evVfK8-6drIARVWAzsCHAtUJSbJK-d3iSqOPSNDhgFGV4-4k9m01bRfqtOZxmWwlxIvP7pbGgXoNM974OnSw-0rXx9bdmIamEI5n63gWc7Dax7YMMau7XH-kZiXE1CqixXbssB_J8OXuZVf9ZLgq_JvRZUxW5BGjfmogLA3xBouuoU9fUoTgHPHXoDlOY-6f26ZnUa1a_DRzAbBWcsV8mnwl0O8nbGBzaWKSXpyiqiENUfhR2VmzZtmPcu6q4F3w-kPoENWU4Wk6w01d9ch5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhPEm4GfwBGNvOgC-cWcee2XiRZQFIaM2k_VJDa0PUt0PPunEfG0hFY4vpBZj7_7EhUBatX4PlkWCpam4rs_HKtuhrBzlwR5cfVFgOzZVpnWSVgbJ77-SLJ-3iqjlAV2ayKmxz4DssVEtNEia2pICH_zyuNTkqxAqsiz_lHesyKv22u52mAVp0ZdpyQgS-CI9J1YVDtshL2rjKdhBnqHYg8jlwERe51peSj2FdeASlGi0zyyiLFvVFIQXRMvWXk1uAhKnGZQclikKoMiVGmm5SwyD-_kzVzyIX65TG4mat5CA2zUxCFGz-js7G9Bfx58q29yd43ZU17_ppkMbJ-DeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-_yEyu3UHNpDbgVpKGUoQNbTr3QiYDo7rQFYGgf0v8Ni-Gtr2LdEwH8Es9hs6LGMfySuZceKY3L355KeR3KG6dsdX2ixGk1Q9hUm-sUeuP3ttfdFn00U7mwvJCIT5ZnWuuXzEzxcI3btemFFsDFoNXVHewrMLsnHO3q0sC4qn8Nz4aPGN_vXXhGAI9ZZCnXT2wagPwA_ZHtC2T--jWA2xP2v35x60WCBF0iI3t31uWJO3XGiyrTfExVPtxSwc26qkeboB60sd-CS0qXlf2hNpwMEGNwjMIyJLgC_kQEQRBa6G1BA9dS8_TjKCMlc2tRsR52uDqXUrkq14zd_nMRxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujiVCUmRHR50pJ5Pz4_-iCo--g_U-Y7zqjcN0V0pTjkM9Mo3Mum_IrqnDDtv0YwMjwHJX6GrY9pB2DVRjcVttnFmO9dlf7Qm_YxgnKLL_Uk3LGdqc2c2D2fpzdl82-tWJYVV1R3q68VEvRfkFVjBTwIZ8mYjCUaV2cfkbUSn6wIkKDxOL-hr_AcvWa-yLGRbpYxw7I77Q6_nfwc8IyyKq-18YUOjDiLz2xPlsKs5k6dfzmJgiby7mrvGzozTHm672xbwfa6obaa5AziOxFzrOIlOL7YjDsM3K31vXbuEuy8GqakFIbN-7-s0ciEsaocJY-5GDHf4nPaoLe6F_rxvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPu0WBbdhEffOdbCexdbnOYSlHhwury2RBeKNjtMiO_-Ix6byhE5iQz9o9yhB--zgKGrGMB3tnIiNCENhpHweJAl9CpyqXliQNNEAXHr_agtNfm_3nbd3YJmFkXHbBhe4nD38JQTSKshCFIZF5Viyq2mJ1ecNZ7GQPuhS85_A3I6byQ7mjnJd2DLA9rzP8Rb3ZshuzKoa-pMUOGdnO4xpF9eSu4lj9FUPt8DqKylKB34oouhmLMgYryZqsj3ZN-uIP5DociTEjCnhPpTSRtTVPCZTkT4_EPa3cFE5mW2WTD0-LPXd2MRdOrKk3mS9LDIWgVdh9f8JEnCT0KBDljzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3lB2h8HXbW-gyZvzMR4nJhvaAI8g5kS1alWnvB0pDrgZrqTsA4wvBM_wbI8Cf_vlbtRmL_zgLfhq5eYJbxpSMOFzJkFJvuvsOcYvMxnTl0yP-DzD2ZETzIB_QDo9OCV_UCkfjTDo3VdJlzaCU417mFmoadZ47qTwLPTBRyItx4HcekWJWsVQLskL6WgGaIJ_1C2s_D2SYwmUHkDPfmKTh4wOxAZzsVO2rJLzBVbUkI0nD8yAl_JAF-VtYapq4q0koOaz5cdmewm6G4gje1azzTxHZN8lGFLLqrUzzYAtb1Q0dk9pTw2eVXjtvDbVO177E4_uhfQ-7vcHp0-a5wjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqpiTTot7-N2bcDHdN5ttwKoDvm4KTzNmDKYjQeF0iW2ZsMOjHkhC5ZzrY72bfeXByC88eLhiUdj_zt_DQhgEige8R-XUGA_FUhZ_GSnO_xKSWdXnWt2_Qwx_GuFSI2wBZpwaW09_YbldtLJahT6GbyPQmU69HrYiVBqeAppzzWYvWvQJILSH9mUn24ZJhFoup38ORIdTWhnLLzIfKiA9RwATk7Y7DT_aTC21K2Lx0738aopqh5JR5Kx0DyVYc-XaHap-04NCaZ6hiEX34RP8KYFnUcHdSgt2CNR0fvPNKRK43_az54nOI40PCrOUko2QxWld1GhJeMDOMN_E5-EZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=uWKPxEQq-bjGr4FjW9q23ajGh-Vp1rDp10NXHNCxgR86Y58acY7M6-N7ji-yxKsh_w7yhZsux0A9rbOU2BbA6HTHDRl6QIrCiCIqELltP0QdHqTZbssq7_gFY8H693oJL_Ums4iaO2kjCZA5xmaYVAhTka2djXQ8pidUuwaeRiD_9WLWJ-gdNfBQ2E0DYvkq8YL4cAbFmLbPqeHGiVcdQ-4-HYCr1f7kO0FyRGLO3KAUV-TnhkUBcnMBy2IDdB1E1f4zDODwT9-iljLAHh-8jEgV82_jXhkOXhS3FiJNNjlR-v-5ASjUYGrOim-TY3PQecC4aHZfrbWkzx6sf0zpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivmS-FwcCJlK4nqwkDJPQoxMhNsgIAxWfvWI2k5lOXVtXdxKYRkTLumpSH7rCKRC6tCX1hdasGVn0igtjjvjy6RBG4WtuVxD67Hoa-0PLeyYd6-qqE2bSlVzjIM1PQHTI213Z42E78uZB33Edu9V7eIyHT7O7RbTlqaB3KFx_vGp3tFO_BBeN3aLCiS7hN_CbSAq1o-ySH-bE-OoGDRo9LoJM8MlK-dUgqFQtv9t-alFRWOqe8LFd5kUpZJidsvHF8LVv06hGQ4hY8_CcdtCoUnM9xSZa7wqwjw5fhA4TuZNI-bldZuZ2D93utOzSeOyr4dWsJP4uThOwNLNngBfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzfLErNOGS93aEHwdLuh8L37TZF89CGc9X2vczmvaynGlioOhbM9M7LANcFaBnf3Mu_N2MNJzEsFa2GgsChda2-QQdWlQY6rucFc6xzt4nfdzrhe2jW2ocRg89qhxz8Jwz3Z2ij-cV3tjF10t2QqPLFqEmJ2oOxth784asJNHfPaydCPXVx35r4k7_HV8p_LpVxwUYvOgagfuVuWBrtMvk0GEl5tFGMU7Yphh6qe49j5ZByEb6JwW00TMcVNQVHmoHFsd58T6YV-5xdD0iVdbGjI-Em_4v4gmVbh6q3qID-u89KHrQQCw61J76RZ9xRyy5IVomCm5y_uIkHr2H_I5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnb6Gxx3JVum60zVFvTjqiq70crjRrpEsq3Zv6NRn3FB9fi-I7f7Yw3jO_aup56umclhWVzPXXLqRTkoi0TIM0EawQ5131dMMDXfSVNrUwuh7Eq9awIrVamygVPhERnMxcD2l0xgS2loSYmmVTrP7iDPVSX5uCvz1yHn13i5LKRLhbEYZcfuScgZwBzhtQBe_taeL72ItGICfHk754KeDPctyGSfthKFnEQatAJUx6Hp4IPNo52lxSg05pxSkiRT5oH9chLhq0jS0kKRjmhfgqXajnvt1kRsfNpqEMyGixxVwuHYCvTUc5vjr72vzjlx1Pc765hSWqO33rLckVoHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcTZxAP5Xh4wyHQjos2URJARMyfYvyKkIOROyxrSQX1OB5zQwGBsV_wguccngDpXeSKMtigf28a5olXwWRv_eX_dIjK_jvSM-xpDf63sWDfCLojiIUyUoXoc44SdYegq44_wQsT26tkEG_Cu0smLdlYKoakg23i3hqZRWNbmCl55Z6wabDtNeUYbPkZYKUDxlUu57Cto7gaaK6_SlVjnvmEiG44V-_8pphfgQez7XPUxeYnSMn-D1qyoZW9A77XfKg5zhhWbd9iTkwR2ZYaN4p2YIYBkuk17YgNfFZA-SX4U8Irr8QVZmFBwZQbuzKBvgmutI2AkutLzTwKdaHrqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26758">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnxBCZXOK1pnY2omkBJW5vH2ZeidUjsAhHLV8LBrgon3kLWvFhHzpXHdWYqxeKHX6KqJSUAPvOS7uXCNadoo6lO2Nwng6kG_9ui_68aeBLzLB6bw2-z4f1cL0ekkhxL7pwTOlidNsi1OhaDBAilsiNqigxpI7qBLAbNOqnM5bBJRt_9Obb7Kq5VqCImxz_cyO0va19Dd8-XzLunR9IE0cyPn-VInO6bYan1aQ9tMVGMcQ5RQRfq6yYR7UziUHZlWJiZQd4lo7OZWLMZ-7ttnJ9syTf1j9od5JNWySh-BW-56d3l4sMOl9l8A2jESSAb6FudZkDJmreaz0VAByOG-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26758" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOSmWYz-tLMVaZRiZIPHoVKdzOMPaYpWjhqm0HTbFABpTpT2dPpHieHeWId1blBq8lMUl35x4w0vJ7FvONi0K0ISzyyFN6XmpgouJ03poFpCjfbww_474ocyyNL3LVT9R4xaZxBWwyXMmoKY57MlgxB634TJ_o4rtPJnSQvq90VqM2T7jm7Ba63pgLCgjh_byreEd7CTO9P_MHSy5RBTX0nCqgDUPoYsZTw_5s_ojyQ80imj9Hx20Z3Q_eV-dEQKJvxKi3WB4B9hMS_zqEEuwOAb4ey5Y4M2zWsl2NM0ssmR3BEIAkr07D93B5i3w5ITatp1P8j71u-NlY8HSuzi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7YMMUfzTu2g5fvskE50DGJKUsnIOBmwpsTXxS0nmcPD7NR1wnTrZOFa5CQPp148I8Q4C-ruV6Dx9DsDso2z5btPmFoDq7rr3v_89AGgmOdHd5tMu55EBtHdNA2GBHBfhR36Da0ePwBzfo4u0NyT9eA8GZ32jgHo63rhYfWI_VsT10LprbEqtxbSZ0Dv0GmFpFueducmcixouerxJfMqdMXlsZNXtrJnyB7yZ_bOaBe5iTB5lIEmS6CcpEnBtDj3ryaJHxKAnbI1WebnYI8_yCpDfuNj-rfVLpl0ZMiYj3mESOszs-YTS6C5U6TbuqHZziwzm3jEpixopOnu9neuZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3WjxLUR8ANyWMrTsGW5sqhcwsbcCJ1veo3yYbk3zCyxcr3FxDOAaZvab1-jmqvW1CQW4iqHZQIbxY68u17pCZw5iSHOusdEmYISOG3qBkfNWDit0tomdkogszFN3bN-GvodSZ3uNZtVJ9K1JDMVBXRayIuvLMzszBQqyZL_N4MbrYo0_0p3iI6sdGMEJ-kbTJKUQG2F8Uo_AIE6hBOVnQo58v3lg11PR1ws45OuQ0_VR54EpnryV_vCQnF4N1tYw1trQNe8kx0JxeG4IrCZfKq3UmchZB9Eiu5wLREGBRC-8e80jv3_tcuRZPq8p1gBOED_N8fxOc7PYHUycst0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BneAuHU406W6H8LXHJ2fEXrO39dP-7yqVcCvr9NUiuSQ4rXIqyh8fpYAiB2YF6f-ndj8KITWKjG-_9tlbl8g2BLn8m-jI5La9YqKAYQwVZ3m2HBMvh_v-gEEO0pjoct30NWusRb69SkyeWLBvKgUMShrTwRfgMAyl373JS7KGcfGHKYoB8rYMxyuXDVA5KHUZjg0L34Rc0Mbnb1b5reGwxWYpKxgd64b6CIxU_nu5yKNbpI_8eHtN_CFhqdM8TM-ZhTCjH5m6osbpiijawifC05xhYlw_2slbhFoK3dXmPK2PUiG46UiqCZYNyFdXULmGgTbCEO42xJZe0vDM-Z07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Ho4vjv9vB3TjASE8vHv9YHgIXZ0F1yYCnb-mB-zGdW_pFPhfzeV9xrsEXa7X_Fo1nAeog_ErVFTIhr3tVk09J8L9_7yEekUFoWv1fWiKj8_4lNj3kIG-CpUl1U_o3UX8ai84iQqivOQMV1LRwxFTXvfqcRSgX1ePdvxTOdYQqlZWg8RWSrNGOXPTK3ketYIDjRa0j9TE23kjgRBZ1TdMwpw3cUCiQcNJEd1iXqut3vvaxOdqfG_ZywOgZHK8ewbk9Yb-LT5RIkKGXtbJxsOEfgQTkDrQIHfw_CpJjacfrSWEYMyjLNhe3tXNdNTRilhCA4OztcxFxZvvPmaxo6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aknC9ltuYi57cb0QG8CX0uhpd6aP_UTdz5baGB7YK2a7ahVgU2uQaPH0GzS0hxJ0U9zbefq12iu4tzgh1uDa8UfVm33c-Q17LodR4ayuBDkiDrytmeUbmGcdnPuk6__pnKdUQ2JiQ2wmZWHHCC0FnYcm9e_vp8a2SC83iK5lAleXYicUm7XbM-O2tqy4xJTQjFHZg8BVV3RqyqSv3Yac0z5pCbijr-voN75nqxgqPCusRwJwKt70S0x2GuUrnSN8xA6chACFqD4rZ2bHM84Or4hl874fSrN7LzTQXOoJNo8iw96R1k8xxNChBRC7OuxOtXaHTyT86BUg4XP5DpTGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx07aEeIkAoCI58EOHj85eZF7h8S8-yIj6rTUldIs0P8fjmI9bbieUryERUkZa5qwfwkLHM6UltnCBQ7cx6LgoUF-k1h1Ur5woSuXPWsOeRulNJpUZJwsjo5O1I-6SKMUj0ZM3wkNyezmOsAtGux3TUu6FM86b9HoNslBLRQKXdAYMKlkIAaEGF8jQfIB0E8ROgzfWeSUID_rW2I5rUOSfvDWzjww7FUYTuGWsOoNj1fK2-QJ50gg53qpMjk_o6tIkimLIWFBeEmHowO9S23d_5kQR3ITNe8rfnKbD4gwbS0_jdh7yAawly1x1izASmDdYyZVT-jO6-9UzrecgohVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BN8F_N73Z4fq0wfB7HlRucDm9MoR_m2ehFczdSUCCGLWW8QNcF3CxyqRdZo9MyeNlWT3GpVXncqa1VK5U4L98XxP5DRZmR_j6XvgdjkqqBgU0By0SyJgoQW_DiQN2X9XuD8SsD36fjNkOADfqrQT2sgA4FzkCdxr5d16Z0WpwRmPZcJFQfy9Mmf2Sv5IKLx2YMaZpqff1QU84mGaVg2HEOBbN-FupxIveWpoXobDSiDEGgBkP_wsRYfrCln1ijsdFikOz5Z89ZyxEG8ufN1pN5JzfLU7lB83qDUkLfL4xtIEQnNa-wz0gLM4j3fdiU5Ga3gfNMX4RLk0Wx5tgAKpqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhCjIDt9twmOcctLL8h_dAM6V2CSRtiKHkiyOqgogge_AUMu2hk7a40bRZjZ0kVovsZJSJwMcYBZKuXNslWuDKg6HCt-jPak7v7Fk2eKB4RcquPYvLMeHr1XfQT4ZVkipR0gfulb-gGu1gmHzTzHHyncXvOJhDqm06-UMZ9d547NWKKtu-gd9IXhTvY2Kg8l-pW0_XYAY4BoFwYaprSPiHS6dCx2k5fc9RI3e4qoELfArJvvadH3xIw-5Q5Sd3WRsmLVnsRRwOmKyH0OyXmM6VG0LrcMhlCsxVaHcouiNhP7yE9q7UH1v7loWnb6BOCZGO6ZcM5lMPes-GCoC-of6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ll5FOOVFb1ETFkTaIWJk8L2wCvSDLaxuXVXNsYxMdTmCzyf3dG_yhPNvrRj59aqwXlu_fJTw7FdffVf9pdaPQx_Jb5XH_BRLI58wSQV-9etQP1r2m7Tb9IuitdeB1_xLE-He3pFty7zeD-_tj9xdqFHrOP8FVRdt-7ghAbAD1fd1OJ-Cks9RKlayMTrpwN_mYUkQwkMVWzyM2tel4xRRPxuYlcwKQYo51QkLXzjnD6TsywXMIhIbI2jipGTH9iBbLxLDjTO0Xhc1C4GlLEXYyJWssPAZKjTwqd8VeXQsyXQiprDk4X-_5X8qTj8zcDIa3y1yXOE1dji2QVlGKvPurg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=ll5FOOVFb1ETFkTaIWJk8L2wCvSDLaxuXVXNsYxMdTmCzyf3dG_yhPNvrRj59aqwXlu_fJTw7FdffVf9pdaPQx_Jb5XH_BRLI58wSQV-9etQP1r2m7Tb9IuitdeB1_xLE-He3pFty7zeD-_tj9xdqFHrOP8FVRdt-7ghAbAD1fd1OJ-Cks9RKlayMTrpwN_mYUkQwkMVWzyM2tel4xRRPxuYlcwKQYo51QkLXzjnD6TsywXMIhIbI2jipGTH9iBbLxLDjTO0Xhc1C4GlLEXYyJWssPAZKjTwqd8VeXQsyXQiprDk4X-_5X8qTj8zcDIa3y1yXOE1dji2QVlGKvPurg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3BJGSWqYoutgI9r8-Otc4BI9IMj6rddID-Blw1cb6rj2ygSQJoxII5wxw2byz9mEzlhBwt1JSq8VvgBujvZ4lGi6UA8uQ0PwCx2EukAnL1ZyqJb0qWSoyNeFp-Y37jq2657BZsIP1odv5HjcyLXad67jjAkOMKxmFjiWG3BoZtlUx82Q4UjhQ8kcLQJ_tXXRh04V9RG358aiW5nRu2I3sjHLgogBS6gFh9k5F5LgHFhrmssZZSY8TyeXMNakeQrwmfvl5XTnmmz8nRovMoTgsKDVoGQt-NsNeLuXe3A9osWkTDMPG0JlBKg-0s5up_EZlM44-gmIB4DuQ45YRbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juPhyuGkucOn07p6S4xROgtIRoHs3_r1DiSgP_UXtPteZTFmT1YVbAYHl5TKSR5HlzlTj5Mwt4OXPKvtoOVWqKPbJJb8lijDiQdhKS5CMx7katpI17GxljxKrpqmWQtuIwpgAHJpUUTjbV0nrfrSilm1zGgnJky2Cl2K9DlN13sWUGya-1jPxeA_H-kpXKy63CKmboauthgCOiiR9muAqIn3wWaYbffgkXytxi6BQkFEvYmlMrIYxd1kxaM3le4dL-uTZG4zI-9s3X8m6maEy6MyBFB2dHZEV6y5sFDPaX-jC-q18HLdCXINyZw-HLo5hvoYCMeLE0ZMYCwqLsL5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYqlXyBNhFmdq_oJpiHJz-54EWUZE0fSnZMFg-mKoN4iljeIO-eV7oNIia7bNjkAdqakEJxX4KR-8IYodTtWGr-BPYmhgHAkG0PAPXFJcl-G4V6BSJ8zEniORWT4de15shGfuShCKsCfeleWaXHCIgbl-onpfgPBmme9L2Wvb6ebnmHStccZtn1s0wL9DJ9Pnwm-_nhR05XpnTGw7Bq5nqJ8_jMP7vZ27GL1zDU35FerZrgTBIN5yJwQIXDbA42LENGSW3XmxOEeEg3uO5s1k3Qrrh64EAKFz4RcEamoBUlfqnLz3ZmvxHflq9zBpIy7zecUsdDpiJctIvlLsG8-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gICxKefYIbtW0pQYauMQ1TkOhnm1jAP_--iO8r19NzHk1KOtyoXLYAQpmrNVqf03Vp-22p7Kifpy1MHmaawU3oX-DwxQSXpz8waz1bSzCUCjB08whVvZ6lcKWZgist5s_poD5fyI80slDqNaeK4WA5lokjuYQvcWBLF49IMUfk2dwO2LedQpI0q9Fao2SMV7D8tWToeQbBhFqly1QDMBcFsgpJpdRQILLoB7iOgAtzDZw7GPF5Kr2kcwZcdgA6HMko7leC13q6kelXplY4ST-S5D9OJuACFKVrdBovKKYVR9E9oLkhC2ZUh-N282dvkGK9mZiZNCCMDSGO3CnnSvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=blsV_WXyELhwBhwdYKmnsG8cjBbdF9VV4jsY2YZxBC9R3r7Eu5jbTlKF9g0peATt2cOZR7WUa17fcAu_TKyZtdXXdErBK_OTyW16QgEkEUdlAWTpPhjXqmpj7MebhyfsCLz517WRRqgE2QUGrzVcyvaPLc-5vTDwPg9nH1XShxM47heqGTWH3W3NHR508Esn4qE_gcYaX1ZTjLlAmOIG05ze8x2gulDuLdKkxXjMDxXrS4ZH0SpYJzGwL5mYnXm_w3YHDNgyy2DkOpkcAQPvM_pBUKTPHF76r3A8i5gaigY5tvcBpELGD27PFD1IeUca-Wi9yvOvKzoySGEFYcwdkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=blsV_WXyELhwBhwdYKmnsG8cjBbdF9VV4jsY2YZxBC9R3r7Eu5jbTlKF9g0peATt2cOZR7WUa17fcAu_TKyZtdXXdErBK_OTyW16QgEkEUdlAWTpPhjXqmpj7MebhyfsCLz517WRRqgE2QUGrzVcyvaPLc-5vTDwPg9nH1XShxM47heqGTWH3W3NHR508Esn4qE_gcYaX1ZTjLlAmOIG05ze8x2gulDuLdKkxXjMDxXrS4ZH0SpYJzGwL5mYnXm_w3YHDNgyy2DkOpkcAQPvM_pBUKTPHF76r3A8i5gaigY5tvcBpELGD27PFD1IeUca-Wi9yvOvKzoySGEFYcwdkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6A-dc0G77Z3YzAIYcFVjhnqAby_RIG-RHw5oRwORuxGNqwPbj_ZMyCVXbcYoaOMZTPGpgi1sTWTjdmYwWhyro7SP3TI1RBby6KqqOftd0NphP6MUAKLwPlkZElREAM56XJ1RVOLZW2FVZYE5wZlgE8r3_tCjmgACR6UgRHm4VRGvkwswJ5j-FeZcdeqEzHJEFS11v-moxwk-V3C8sNLlt_66-1zOw8l1pippMqPaoUdN94CLP3blS37Rzuovk0n3f2pYcnsugHqfuGAIzIeJci_6MfLoUGidUMK3PA7hhhw6EK4S192ax2kePGbv3TEY2IVW7whJkhO3zf5gHYLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfUmFK64sDuwksQnKD9yq91YOTK1X8Su5JWMSvIdCAFAmh4AXj0Tlj-BjCcoRkjNg3Ht11USFnqfhQrHK_nOouQT-UwOt1W9JqEuM4tVUn8BOPCkIO2Wn5ajrKnly_sMwdmblh-B6Kjdlz8Oj25YSSqSpKPwgHBSkUYM2m3y8udWxViL9Zh9ULf3Mhmqqr9GZUb7fkRO5lPqQpSsDD2KcIkLkWLFxgDBfRsuPBorZP_vD1hYtLZXwAtg77mPoWzazcK1sT2I2DN5W5IjGBku6w7KRCHpavVWimUrDWvXjpZXdYywBqy3Qp7lXpPZzJQTPau4mHF5LsMyMxOQwKmEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26735">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz_6_ZAldARu42Ax-BjdEl5eVEaHwSI--dEFoTYSguynULgFl44uIYEjfybGsWCpOF74uJLKRc95nUw8mKTf3gn1UxYQOSIRD5dfgjzVOKqcahNApCoZSq-7X75AJBQCL69qRua1HfNEnAZtP_y2TNYOKlbfReYIgNmRSAJDRABWpyVhDKu--8ixjbxsoVP03BP_RBK7gmmQ5g-G4XclAsUNVppm22ZMY6H13mNvU7IGGibud6zwNnitFcjCkoZ2RPlehqydngmrastMLVQSg0zRZK0Mmnj5zL51SWXfD8Zqj5JIPloha-lC_wNBywQxB79_EICCW75hXnBFCP3LGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
🔥
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26735" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oshNibq_rBML009NgHjFa1_9TeABco3rUOJy_doIm2aXx0qj37puZSbLq4z8Z7UGq5N3noQcegCdUt3OC5tH-oQWmtlwvIesNwpyJcn2UGjSmlexi2A5TNwJlxEtsQ9V9GMt6YGwehtxIbBx1TVKy4PBcalyvWdemOQ54iUSuxaASIMeQXrGk8ZTvO9N_zvyyPjW2-2nFso1hK0Eoj-lt6O5iTas2RmVjj4_hAhEhs5KeTh3HXZ4W9ZvxXW0Rf3pPSTAemVdyIRGlBSlOlwZMHKEgzJIE5cQXsKdqRcHdECY3noleiS9jCWxsEiN_Tse58PiuU-Ymz9RiY_X5lF6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=MFxSfbaVfyi_c7_RU3tkvTVUaO_UvuqXSV-iEwSyEqzyb1OwaVE9VGN6WyE4FPhtmLLuNeaG7i8wIlYt-WtWQEQh4rzTMm-VTuVICo3sJq9SBvPMH1sR8qrlHu_J6IgXApxH3rtfhAPWo0Tcono1zWqn9NIXDyO4UooyVpGglg__5Eo4z0Lriu7QGnrpAMR6xrSHLEcnJlcNs7vw68BStKwOXEAwXgUSwq_gRp3CXoOKjrMdREJB2FeMbaa3S0wP4YdQMoXxiMizvK2E9Kog2WkWVuM2IvGjSNbMjU278XVYKvnmwdg0L7zxlDxI2mv7Ly8dM1WeJxcEzStsZt4IIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=MFxSfbaVfyi_c7_RU3tkvTVUaO_UvuqXSV-iEwSyEqzyb1OwaVE9VGN6WyE4FPhtmLLuNeaG7i8wIlYt-WtWQEQh4rzTMm-VTuVICo3sJq9SBvPMH1sR8qrlHu_J6IgXApxH3rtfhAPWo0Tcono1zWqn9NIXDyO4UooyVpGglg__5Eo4z0Lriu7QGnrpAMR6xrSHLEcnJlcNs7vw68BStKwOXEAwXgUSwq_gRp3CXoOKjrMdREJB2FeMbaa3S0wP4YdQMoXxiMizvK2E9Kog2WkWVuM2IvGjSNbMjU278XVYKvnmwdg0L7zxlDxI2mv7Ly8dM1WeJxcEzStsZt4IIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=lXxQWEhV_wLZ5zmQo-KkKnENPa8axR9p0rKis888hOliG70Hd_1KHmlYnY52l7uI8qH78BmajbGkSTm01QeqQ1UIwbdebHbUkd2e6VxvRi-ZwRiLQHqoxa2ke4RnG9ipoJ_DU82L20GTHfbaaFtK51y0FmcNgbQFhQ69sC88-A-nVkBveof_TxEs7GR2iowtsmHZp1_akcQ5VJkm3Wc7Uz57iZr3FKxm6tFN_qDBbI8Hfu5XZptGbY_8-469uyxwYRoHqTPr2KxbhplFosA07a7rr0N_OJ8yOas6O166ZgLBwh4geGNFE9cLwRDI2dxr-YQUD-zWlGBs9fC5kBiapKT4kSHLZfVs0MXFNrLai_YQNtUJH6Y6LYX_JbKOX9_JfVUDORPrT9Z3eXevt0KdVf1u1GMbInwlyaEUkMkNPSVHftFRpxpPo_yq_uwr1hhwQWAHH9pv3xhgFcd-Xj1GOLcCXvld_DeRt397PiO1w1rBN8boSPP4FHI8A0JBchX6lDgrB5VSWZkq9NaplQIN39hW3-75n5yB1_V_A5ydaHiqVWrZtDri1WUgvYlJrTmLGeruH6BlRjO4QWHheOVzexqSISNo6KpwRjr72T4eKmmG3rTiXZkM8m0dxj8LhaYipGf9Oq3L8bhIAZ22oHA5xUkZjI6DAWcE6fzHr5YASRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=lXxQWEhV_wLZ5zmQo-KkKnENPa8axR9p0rKis888hOliG70Hd_1KHmlYnY52l7uI8qH78BmajbGkSTm01QeqQ1UIwbdebHbUkd2e6VxvRi-ZwRiLQHqoxa2ke4RnG9ipoJ_DU82L20GTHfbaaFtK51y0FmcNgbQFhQ69sC88-A-nVkBveof_TxEs7GR2iowtsmHZp1_akcQ5VJkm3Wc7Uz57iZr3FKxm6tFN_qDBbI8Hfu5XZptGbY_8-469uyxwYRoHqTPr2KxbhplFosA07a7rr0N_OJ8yOas6O166ZgLBwh4geGNFE9cLwRDI2dxr-YQUD-zWlGBs9fC5kBiapKT4kSHLZfVs0MXFNrLai_YQNtUJH6Y6LYX_JbKOX9_JfVUDORPrT9Z3eXevt0KdVf1u1GMbInwlyaEUkMkNPSVHftFRpxpPo_yq_uwr1hhwQWAHH9pv3xhgFcd-Xj1GOLcCXvld_DeRt397PiO1w1rBN8boSPP4FHI8A0JBchX6lDgrB5VSWZkq9NaplQIN39hW3-75n5yB1_V_A5ydaHiqVWrZtDri1WUgvYlJrTmLGeruH6BlRjO4QWHheOVzexqSISNo6KpwRjr72T4eKmmG3rTiXZkM8m0dxj8LhaYipGf9Oq3L8bhIAZ22oHA5xUkZjI6DAWcE6fzHr5YASRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1VCF0D89oZH9Z0rOs9aNXj0uSx9RBcWj6E0GiHdkJFyedFSrf3qEOOjT98ft75G9BuAhu0odyobfXKV-Ro17Q7Kh4VeK2hFqh6sh9ZHzSaLxog-PfeKEjkrHZjWTt0PYmRsiNc-sH4wscX-xIC0Ply3YevVEdjckyVXCD8Vq5E0Y2kF0CF3wfaFyeKxVJNjWXS5FNfwsV-U7Br8VVwxcTj5DBMzT6aAkTDuGH8HNWcuhtpOF_GDvgkkZOIQHPIGkz1KcTWOh4Wfj4ttiozt5tc5Zm7Hi_eTi1Io5NON1ckhBlXM7gnO31_Lu9FldBW68NZxIwrMTGEkl6dueMk3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNr20X_69vkukXoKQbYNRIE3gvcPZjmBNq9fWgbiZMTzHmSmphPzIupnx-CYgnMyRgJJfFlKZx-SIAl2QfY3MGoalXiAvGSv9xNX4EbuGFFwp2QbQV2ykS3yen4R_aEBd7E31frRtoimSuPcMVmQJOJYqWfkMxzFfClU-7iz17lc3Iy-AjtJLKMhu6lbAq42zt0L0tcpjtzU5KMga5RE4pCkCJJkeepm9HSjKxLJskVY-ac-KOCjnVtGQIa2klPFxGK_mf8H75RkGAuXdgLtk7Nloe1lAHyvFmJYugNhtuZN4dTaejkhvlcMrL_mFZ4hn--3vsa0E7uCM4mj0C8raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INqfrlHVSJbIKdn54d1Q_qggDxGIx6x4xC4Va0uRk_ux6sFLUmyRcgtThbde54DvAulXSyutySzthNB4OX9zbpUzBfhnOdRPzdGPznkuGUPejrDLprM9_fryEMlAVX7pLKLsv8hTDxwqZ7kEFj4EL_ycD-QVGqDSo5X5naITSe2ZOaUJA_82G4hXETcHqR-OBLs9zfuqbU60_mWBhgjIUn1t91jGcYR8HPNjy6o82aVtnwpV8R8bxM7O51rZNr8FiFRF-iZ02psTKc31x3dDbo2gU-BezQ-WTYCO4RZUGwi3PYUI30MLKm4esFLJc6R7Vb3zkn5Bq7LHPfOzBTRlqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6l1gHPeEkBLCpRrBqD2y-dIIl83Kvo6ygAkNBvTGHWxQhABr12kIPB1KQe1rOShqVSTDUR73-W0kUsq-hYvwY9gsoS58TjG91iG4HaqBeL6utRCnewAGDzj49dMuVqDNOPv2W72wzuI4eEPfFhuM71ya-SPuxtKtAsCmQG8mv4qZ2Nxr2PEo4oRlRSRI86OUmYyFTuuVChs55bjji5JsZYQz3_fz6JY0yjNHTyu2ub82YEqJ3TH_VcSl3dMIBZZtjQL0_rk6Xj50JmgahwaNLkj2R1pDL8s7HSdRhSoyhvjVX1PulWI7kSQb4rYVidbYCeudEo732qDz5FB0naaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vIEh9_g3y_F2CKrAn_2w5vk0VoTar9S6EChVidtWJDP0xJlXtc631YvpQ1bnFxzrukpwrBcAwxqxP8EFPtYX5OpzaPhne_uYSwIROmLY40K7BAp9E1yYGTCEWT4oyOJ_nW26IVFoanRhJZWjqpzjSZ4ZJwUfSBzGw29fqMu2g0Sg2zjBpbiSvGnOghHgw28hNvk6reC_bSmXebI4qQUKNnDCJbGLKBgOhX0Vb3LNgv0rudl3i8EJUlw576oxtUeKTS48SaUSuLnJ9QTsOyiBcuDXZW2A-pbXL97MLZpteoRfgWRCb7x58QXOWHfsCxbg8eP7_nf97OVPc-K6XEwrZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf6sV5ZjzncBGEuMMNfI7L0PANcIIbs9UREBINJKMvMzpA0b0omdKbVSod2eObIknBWjkDhCYP120inQUyDBEdsCQmPedfRPDEXd5K9lhA7GXaNaTi2-XBDuMYCbMBgXlAGm5PUc9QuKlaSrOe9jy3IHyfoGQwFH-6a4zKssSSlNz8KJUgmwvBB9pMPYFXzLiaeFYPMojQuavX9q9ED9nL7Jy00k7PIL-vmkJumqBQTFuSY5egoQy45g27tLEJJFbJUxVBbLOBN6oS6toh_qqc_rnbyQZxP_8m-w3RqvH1xK4Aj85vi_J8k5JVrVSspqTUQkVz5n0vvMsIQ10jrijQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC0wkt5A2y4cvVq1z3qhe5wviNQC80GWwS6PPFgzHQKXjKOoBPcg2GVC8despJQzcu9YbkW9pS9pZOkIQGNRucfIVLEjGudvwBCOOvMWGtMYBXq_DszrWWuLKgA7VCz-3EZRhjJJUtn99mDzfAAbR1aZNnLo6QoEUN4eHtz6Zq5vRcK7GButaip4mUbBrpQEq5-_EcPVwRBKXbr3QtS2KSWJR9ydPKVC4JfEOb3dDnnCwt7krFkpUu5JcaH9gAZtcmgcJNtCE3ONNeZC5ShjEYtCAGJVRSOQCtVC0Mc4gwZdpODSIOY-PkBxpgp_jrl8u0uGrOXY721zu3QN9fka1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=i_QLlW8QbUKsNCBOqpPWGuj7SnhhMh8-EnP9vve1-c0dqV9m5rw3MlRBRk3ApgaxkFqHQZhb3Ttv7Tefz0-AvXcS6VLo_KufvU6KUif3iKqDsJRl5XmDVd1WlY0yl9xaeCUwyzIgwXfdC308cF7ntCPAN_IUfBV-P6ggw1Q28GymDLfQGzK2FajkBs1EwzcMoSBEEfD6u7WLrE5IyV3H-SAxDm58iyM86Y-U7q3sJqQuw-r8o8FfSTxsXIuIZKxoAd92m9kA8-E7YW_94PxQ0HwEuxLN8wwHoqEt-TsMHR7EHzk1AKGtaNp1RhJG8Jnq3UQFcI-9cgxU3fUi7vPQKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=i_QLlW8QbUKsNCBOqpPWGuj7SnhhMh8-EnP9vve1-c0dqV9m5rw3MlRBRk3ApgaxkFqHQZhb3Ttv7Tefz0-AvXcS6VLo_KufvU6KUif3iKqDsJRl5XmDVd1WlY0yl9xaeCUwyzIgwXfdC308cF7ntCPAN_IUfBV-P6ggw1Q28GymDLfQGzK2FajkBs1EwzcMoSBEEfD6u7WLrE5IyV3H-SAxDm58iyM86Y-U7q3sJqQuw-r8o8FfSTxsXIuIZKxoAd92m9kA8-E7YW_94PxQ0HwEuxLN8wwHoqEt-TsMHR7EHzk1AKGtaNp1RhJG8Jnq3UQFcI-9cgxU3fUi7vPQKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WshmQ9t4ym1_Zry5UuzsT2wYc-CQriSC3zKHJtT6dK4_jYuMmy8kP3MLd9nCYPITYgqyVYS_NIEem4_wABrDXlH9HZAfAvGcv1Pdmr8VG3RE6SWNsRK6iMdIbIy0l8BZM6sP3JD5vmFJlUgbksthANVTySL7A4w8-AzT5UmU0HNE9yMZVeXxlUQY3CfhujjutHcNLXkiqbE_LOUTupSNPv1CRbDhT85dJ_3NBw7YpwWlOkhKlbyegqQtCug2giw2bUXREvwSVZzB8tlrRyuYS9Cogz4z40fopzw4PKD3H2la7P6cGwKq_5C_S-pLnNPprBPg3X5TF4a2Bt6MLbPkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT13g478ALrIYmRYRKikAvoaM1oGuRnNr7hlyBa42U5TZ3vM1b_BhHGrkWxVpPAQB2Y4L-z_PgAqrkoX2LrUAoM3xI1dJSWW9GVaaKTK9gTiVWiw_WPBeuPx59XtD4ri-eQYWB_57wzARo6s5yUmmfB8UcR1So0g5xZyJH-xXrMGCOob_N5UheVcgbzUEYUnwGY17JEbou6HoPhT04qYZwNhS1zVFQNbpejbBVXahsFR-SV7bLUV6pgybcM8CeUzJHFQgAnLQRrJAo9HC_5gXuhshuzYiyyrAMwkQYOgaeGH4Tj8328EBWlS3pN08kwGB93psGBRytY2acsKajLeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJvv93A4BD4Xr7FbrC36aSo_k3wQ97CVGi646C0RBcFiBq-D0KYfNmw-jgiGvHK1MFZXhSAOcMzF_kEn9XWvHWKqUPuIbJVW4hn2txRDrpVS8f2QmbtHwz8pW4vSoWm-AlcJOdGkRLWwSdmrax300hPqPO6EpDzbKNB25nWbZoid4ne7nD_931RoAJjCjqFGwd2geAx4fbDSkzw0MxD2nY1FEoo0WTv6ZpA-G-GUEXyJi6rKNJl9jB4-5tQ3Zs00n4hRkWEp1DDPt35sAcF8wDMgmEqDmaNBkQxst3JVdnvNJfAw5GjSFtlRy_fEH3urjsiBQhx_4KSt3Ii5BuLMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gy3bHGCI9keQ4al0I6ozwMoZq1pRhiz3Q375c8abXrQp3wkzKdGkOtBp6yw3udh9zrqIZNPjkNqtOcfOgqxJlcwgpx3_8yBF-NvNmuYsQXty51R9BjUFaVhfzyUzfh9FRae6BPwGq_-Fwr3zHGHAPnlPFMjr7dVC8uC6WksZwIQLrArw_3poTxdXHLOgPZuF2noCRsii0FKSTjAMGHyzCYgL1hBZYqFwCLg81YsIkTY3VEDMqQyuTICshD41lbMCVe_V9UzdyJj6DKm9PAjB9YMlamL5eKPO1T6oaqQGeRa-9T4byOHf0_YLpdJzLdO6N-B3jorD4p0tiEVoArzWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=vkHeLax6jsQ1WKMfEh5OpiHf_AywRQ1KI7E7qhUYHXNeFxi3mjYGcrOP5WPlkuZ0Mfp39GK3obxukX2AhjVr1WzbSIlKU9X3_K0nNo9foRaDq3B0B8hjiaAA3CqhP7wtwD0XQoygP-PdTTgYpQKpbKeeCZAO3bK-dH0sVqvjKj9sw9-hXJfzTfTpUbpcdBkgh7W9U_qjTFfCo0jOmGYQI_OTFrI0pzIqSP0RNVgeOlCl37d5XQHba6_F3s3hfbNzcZNNNaNP6sTZEIB_9voAVFPW9eRMhLNK7ja7OwJI2skvOZjoD7gPgTkpiz6b-iGG052NgEhjg4-xkW39dNlWJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=vkHeLax6jsQ1WKMfEh5OpiHf_AywRQ1KI7E7qhUYHXNeFxi3mjYGcrOP5WPlkuZ0Mfp39GK3obxukX2AhjVr1WzbSIlKU9X3_K0nNo9foRaDq3B0B8hjiaAA3CqhP7wtwD0XQoygP-PdTTgYpQKpbKeeCZAO3bK-dH0sVqvjKj9sw9-hXJfzTfTpUbpcdBkgh7W9U_qjTFfCo0jOmGYQI_OTFrI0pzIqSP0RNVgeOlCl37d5XQHba6_F3s3hfbNzcZNNNaNP6sTZEIB_9voAVFPW9eRMhLNK7ja7OwJI2skvOZjoD7gPgTkpiz6b-iGG052NgEhjg4-xkW39dNlWJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBUoOGxN6MROGv0BiEgSI1HPNDw8bCdk3lplW_hHHnRjBB8WYlPUAbVb___gJFs-meBKW4JYCoXepioYSOhC-8PUEgwzqSPnZOIwvN2eoUk_Ww19_f9rGxjSn9Z8c0bJfpdlXv4PgpiYHUhPnIzIZCfLSysw1ccXIUbD2Qk7X21ojVj6d1zPobWmxlOlruK8emCsmkmFc-9cgJDwN8FIddW-14F68yRmtWgWRZbOEa7ve4S2uQ6gjpfptKj5KI058u7y3pSFuXNwQWapUMLAHBVQHnoWAGWPPQ6sHWDL-LChQpHgxV3D22_KJbAvo-YDJ1lcCFK4hE9TtaDONOZ9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoqlxBffH4aSb6a6vYvHYDHfevpo-hBoAJlolmsoxHs5TcqrrRNe1RlvCTFLjyrmIjKmGWlqpTcLF5EWtcaSw6CD-iwOogkxJ504DKPs68AsVzl8ghXjZzca1SmHx6nM73YTnqiins4zfoycq8LHPa63yMb8Dco3gV68roJKIwgvTVZCTzbXsNdqDsEdMiExHqNTuxfW71AKP3SHYZ3nbT_rK4Pt5YAxyPvoUZS4ZrJjA8HVuH4jUhDT4WHNGKtRLS_hk_7LzTCNx7CEGIUlS_7xrVkv9Rog6jqSS6q6BuWai4MEFxV9Kn9LzWfcG1I7987fpLrq1ZmpODLsnJaY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGQ857McXdtgWVXOCb-ocpkneQ8z7bgyMNNXz7Fqi_bystOWtZQUQ2Sv7CR4s81hapz_30ndmOb3w8lfvZx4qgiRZilooolwaHb0u__yrVrePDspam8a1ez93xxwIDwv9t59QG2HmAMKG0g9wEravUkC9XUPuRgJacXMJsgJukXDmDW7Fv3UQf7wz3aZBsvGReF8QGYzoyXQSbIz1MV-ftIDo-Yo4KihfPg2PQvj7zkJUbPEfYwswc6mslqE7WO7uSxnjS8G_k5XjjEafD_H4bwlyY0cJehW-WRiU7UxQ8_VQtjwXRF-mF1ve-8ebjatlaoXK1eUt2Ivs_ZClzBi2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=IJoy_b-GEAUn6YT-0LNKF_qq-OSH9id94_TnUueoBpnlXZQofoj3fuSl4UGu0orbqazAfh5hvc4xrC9clLFdfrdy30tSJ3VQ81LIU5zay6mmqLYy51m_ACzZHvMzcnSmgQQNWcK_myKNTin-tWx7mc8RUfoutsKwGMl-yQeRbkVebVtR1Y_wouu2fTEEOI9sy5GP77S532JIsQbKtl2UFVnEXppA1eNBHx_Iqz4DSZ4HlfwVAep_q65Z7FWayDwdDmWSc6Y1wMZjrgfLgyg5B9C_fMK43Zu2N1XOiLD9o9YBDN1QUHT2HIQ6iM-PrVElHu3xZV6sCWzPY_5K8ueFdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=IJoy_b-GEAUn6YT-0LNKF_qq-OSH9id94_TnUueoBpnlXZQofoj3fuSl4UGu0orbqazAfh5hvc4xrC9clLFdfrdy30tSJ3VQ81LIU5zay6mmqLYy51m_ACzZHvMzcnSmgQQNWcK_myKNTin-tWx7mc8RUfoutsKwGMl-yQeRbkVebVtR1Y_wouu2fTEEOI9sy5GP77S532JIsQbKtl2UFVnEXppA1eNBHx_Iqz4DSZ4HlfwVAep_q65Z7FWayDwdDmWSc6Y1wMZjrgfLgyg5B9C_fMK43Zu2N1XOiLD9o9YBDN1QUHT2HIQ6iM-PrVElHu3xZV6sCWzPY_5K8ueFdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=v2rwsvGZWVNEJIzt9pdPg9Q7El_RKGlDrjx1oWTglKO-YNs-5euL49jQBVaDiUKC0XJYLiQ5MCFangHLvNp4hkBIYCbVaNX1xcS_uYXeKIqte9OQFBi_p6zofJSVr9prTHBOzKnSnqI4kcEW3nwig5J3aa0AIHLnKOqdyOQBXG6_FnLZANL0-eDSu3L6b76PMkLRS9ucb4UaJUxeqslwalHsVjTPsD35d7E-O4-ipuMJGTS5voNyHbwzLSgWv4FZyJqTIOfBA4OaJ_Z6OwRhTMlVwHCo-pzej48EEslbNmLKpi6cNNhz19p7S8mKK1bQPN-bjtJEgnxK6Kh2AlujcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=v2rwsvGZWVNEJIzt9pdPg9Q7El_RKGlDrjx1oWTglKO-YNs-5euL49jQBVaDiUKC0XJYLiQ5MCFangHLvNp4hkBIYCbVaNX1xcS_uYXeKIqte9OQFBi_p6zofJSVr9prTHBOzKnSnqI4kcEW3nwig5J3aa0AIHLnKOqdyOQBXG6_FnLZANL0-eDSu3L6b76PMkLRS9ucb4UaJUxeqslwalHsVjTPsD35d7E-O4-ipuMJGTS5voNyHbwzLSgWv4FZyJqTIOfBA4OaJ_Z6OwRhTMlVwHCo-pzej48EEslbNmLKpi6cNNhz19p7S8mKK1bQPN-bjtJEgnxK6Kh2AlujcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlN9gtojXzJLj1J87Gj7VHs_rtNRDjTQ__eWQFDOAQPJMEWPoV64kWgXFuIRFRiMY5SFyUJx7URRiCgsZ-AmEErYKxcDrpx9w1hnF_AS6LbBnDrqyUVN4xAQITifOseWAD8zU_drpepHaKIcVQJt3AvFeN9tpW-1m-EyyZ2fdet9f4iSjbXIQFhxZwQ37MlvJ8ga1aSNgOLnatW5fJBAXjn6RhBukWP8HnmTa9OMcudgTVUy9yXbVGxSrXUFJjqbe64gnPAfC6I-0yfBLsALOe_RolqBGRRfFeSNLualwbMcpNXL_Lr7WPFIzmykQSL8MyK1TYa55qZlWHoMnmkGUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8S27EGOAqI92XoKOO-qbbRq-4yzRpjVgmxrdmVC8Le5jcDx-swc4Ji_0vApr6eOiDivrPC8evPzpX05l7ijxn8RPVkJRb7rxsGUnZP_dgrCO6-IfzAmnCynHL1u9OO_b-SGEZkGLeRwilk-91fbssQ05jKIOToo4jqm6KMnF77joBqaDKrIUG-I0LmSxd46Ny7_iwtM3-lFYIGHzLQ2LVaU6kXhO6RHzGCFsimEkVJCxLn3pGQY4O_x5ruxroTJuJCajYUPhusSUnPK0JbY480GfpBHrwZIhaLizvNgqTKvB-S2zF_F_RWkN_Kgg5cF1lTW1U824XVyaacxSubGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=Zj_sTK-O8tVcN5BYcsJn1CbTlFxW8YMCpMJeQyNzspKdqWHr2zuhJbzfbTj44uszRpkF0jMoMKWD0-daQ5K1ZU9cdS7ITHf3ouiUDXTWrHkpc0USxATO3V4lDbDyS-8D3JAfq7KC2FjYgPK0J4K1a2PQFezeiwVKQ8b333qvlIunCdBL7OujcW7pEabS1h_AxMXIVTHgPB9FGTV8ym3XfkKrNvYn-yOhyNIdZVzpNtgm3gxAoQ3UppU2utcYkGmQzJX95LMEF1JMNIoB4OXJXu1tfJXR88HAYEy2qDVMpylXyn7O7UREfF6cZthc7vL4Gf29ykvidF6rEe-RQf5FyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=Zj_sTK-O8tVcN5BYcsJn1CbTlFxW8YMCpMJeQyNzspKdqWHr2zuhJbzfbTj44uszRpkF0jMoMKWD0-daQ5K1ZU9cdS7ITHf3ouiUDXTWrHkpc0USxATO3V4lDbDyS-8D3JAfq7KC2FjYgPK0J4K1a2PQFezeiwVKQ8b333qvlIunCdBL7OujcW7pEabS1h_AxMXIVTHgPB9FGTV8ym3XfkKrNvYn-yOhyNIdZVzpNtgm3gxAoQ3UppU2utcYkGmQzJX95LMEF1JMNIoB4OXJXu1tfJXR88HAYEy2qDVMpylXyn7O7UREfF6cZthc7vL4Gf29ykvidF6rEe-RQf5FyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNSMhJWEfcTJ1-LV_FePJmKEMwj1PYW9jHIku1SWsJMPCmozR_1E2VPD3Jvqt8mP38H9LjDL14CMwtDAUB8_1le3z3JcExpD3rfidmg0uEwYiL6RSfTaNocmJwr71zbQiu8fDAF6z6xdzXZ-UVpTenVQqlKceSI9k-EzHgkhoSL-hB4i8hYwz69hw-QeRr8M1-UBHIlKAOafAp-7CJOyOhZMGJWEALnd9KZ-4mO615CJcjpRQ9_nuizwrcXXnfAF38c1rdeCm2CS-rPPfo_vRInrvUQAdk2g7F5axLnU3BfUN54pHcFhYim-Al3vHUwprLfOsL1bBFhtN1k407VAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAX08YWLOIgipHotVvjyber0ZJ09bdIco1UIFOcamT0lnpco1Xmwl9i4Tsx2c7EQwz9aRNZ161gicHTYmWkDwUbTT_9g2ERkHZ7mfb94TAKsmRZTjTtJYR-DPR4ZBl7tOSgG9pU2CBcY_kGxg0Cc9j56RDah2ZJtgXMn_BNSWK4ggI9zS3gZH2jpKjYt3qUJMm-Y4mJJUMhk7kEe7TQiV88e5AL0mvtdxVOAp7ukFwptOWBGOjbPMe5TxRxFoMAJrkLpz4vH-D1iiacvuAdx7VQ9CeA2ItF_XngHSuODbikEmqYrsIFB1PH7NcaLcutkzaB2DBerfJfT7bsNZUVM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwAZRy7DNOJbVbl4vBu4V9OFrwfmN5rQakpMalADbqg-qBnOps9w6Ugpv9o6Cytkm9aCApQ2emTHl-xIFzeTIVfdBMGOjIinNhztUXIETCoxNUhl6IJvHlxz0KfZNqFtdKlm4_YgYgW7XCyqSM_npw4hYHy_2O3jeSCBvfUA6HQzKQdEI-H_-_uq-ThIz_7unl0W6ZR2j8RoWYfsujE70aaMasSrLEkCPFxmCiGK9IfAvKnpp4IMXH7JHF59Ce5bz27BJPr-wufEadjiwlRHcgf0k_m7v_s_5_We2VHtWF94YYpY76Fp0Z_6swzsa16SNZy86LmX1ZHu9_wlGz4ahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=GYnilr7qWIy1wAuHwr1cgokIPQbDWJNSb2ZoiG02ZujZFjefgBsqQr1CNEfsitGFGzvnCwZXlM4LZL_psmr4Q9iftIYnO6niG1e20aBvgTDGEg9kMP0QAcl1cb2j11y5ewQHzOFHo4-Rg-YAj8CfK5iqXEf8W6jVwNtSentJphbpnmP1AjQyFogpua5u3-5do7H6jnXbyQA7TmIqTYMyV5v9hU49XjNN6VHWW68OfUpmK2HTs2vkxAdCYV7bmffdyyqIZ6Zt1U_8CDkOhu3cVXe5-FHpCaXRRYAkxVsAU4WbBciNp8_ZjAtrgBuzjemST69f31Qqaklwmu28q0qsymfZPAPqZHklWO7tKzdaEy4qPI_uGRQLvNN59bIm-uLbOccbFIQJ9T8y0G2QEwu-RfsBZJmoJ5351AFezHlCb1wfIkiEeaPZ135PFvOdtLgQz88i_cq56ZXb4fXb2N3hb1fn46CdfrqZSxJBXyTWtz72xhVE26IbcFyCNJ1qcVj3DJ-rsoqaw0RvV2IvDk1MqVBLOhW8ER7w1pf-LaQlJArY_2noLwRXAJg_7I2cOZWfSj4c9-6kzl50lk_BNjyhFOKAhZTeNll6NcnGBs-j3MurqAML5GdCY16kyB9AzgSpnHBst5GrQhd-PCMLY6i8zDWqtWu39gCf7UPYvciFNcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=GYnilr7qWIy1wAuHwr1cgokIPQbDWJNSb2ZoiG02ZujZFjefgBsqQr1CNEfsitGFGzvnCwZXlM4LZL_psmr4Q9iftIYnO6niG1e20aBvgTDGEg9kMP0QAcl1cb2j11y5ewQHzOFHo4-Rg-YAj8CfK5iqXEf8W6jVwNtSentJphbpnmP1AjQyFogpua5u3-5do7H6jnXbyQA7TmIqTYMyV5v9hU49XjNN6VHWW68OfUpmK2HTs2vkxAdCYV7bmffdyyqIZ6Zt1U_8CDkOhu3cVXe5-FHpCaXRRYAkxVsAU4WbBciNp8_ZjAtrgBuzjemST69f31Qqaklwmu28q0qsymfZPAPqZHklWO7tKzdaEy4qPI_uGRQLvNN59bIm-uLbOccbFIQJ9T8y0G2QEwu-RfsBZJmoJ5351AFezHlCb1wfIkiEeaPZ135PFvOdtLgQz88i_cq56ZXb4fXb2N3hb1fn46CdfrqZSxJBXyTWtz72xhVE26IbcFyCNJ1qcVj3DJ-rsoqaw0RvV2IvDk1MqVBLOhW8ER7w1pf-LaQlJArY_2noLwRXAJg_7I2cOZWfSj4c9-6kzl50lk_BNjyhFOKAhZTeNll6NcnGBs-j3MurqAML5GdCY16kyB9AzgSpnHBst5GrQhd-PCMLY6i8zDWqtWu39gCf7UPYvciFNcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3FIFHATfmNVuoA1qDit1Pq9s5sp2p6GbtdMGHegLog1-fHMW8uokPRuDfXNO_qj0lHOHI_Ea6R4aDl59puVKZ0C7mREUZE0cy2W7y2Ba6DndFKVJvyf_lAv9FhM0Of9oDXGFJiLVOdyYFtf4BHwvuZtDJb0n2iPY5ns_NwtsqvwXGR7m0d2p3tEupUQ3hW6GN97daspQrL2ohT8fLfJSiVUCxF0rbjpPL7LIXvK8Vm8rLZDSPQMuCd7MVRb_I7XMTMoMpGsq8H_E25rpuYcUsq9NBhnFCJ3lrxeKQZ0NQF7mRciq6nHvBHp_48Wwc5B2L5MNBITUoPuURopBIZJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJNrZ9VpILLYZEYlLRi3blaH3jtVyFu1O5V7Bkut3gtEW8-zU90QiZSOwg2PM9dhjRZCDJz7KiqSVzeFwmgw2NnqAzQFYy1wZrKbpdBZxHBI7AhW6ohWw1NDi7KOg1SwKorgUVCxBeH3AgzoYdAZfSHUA90OqbUzqKxYUV4vxKflXsrXP5fGkuA5UWbFnWMvxC30djSB_Q4zte1sdpZxWh9TO6Rvkf66IL1_5m0-L5d_Rx7hqZfZ_FWP42Y13zNmWw4-HPvFJK0uqCWDDeREqEqXGvmzJjlSaa2-YvbbfO50OG9WXq7QLVXdIx-bATe3DycfpCmGipZdD22JnGbZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENys6hEIl5vAennPieTDTzGd2ZBuXtM91FJDZH43TYgIvolKj9Ovr5Oes1MEcngq7EeNZIHogIZEn8VNGr1BISMEB3wl8e3tBrJkv8aDR-BtwbQuQnQIgCO2YVIE7WEHYo33Is15aLwyYM-0hF2KZ7HLUeo2c6bcj7OfnmguOdzeDJ-5rqt0Y4w3FisxcwERvLF_ilgg76DzZwrl5NjstSXexzUBOy_npHLfNpncLo163TO9dEc0ytDMPEJiNmlmIPUPfACeFzmUS0QJviWFaRmRIaCkQrO6nSpoTQmg2Fbh4WnK5-PfocdQANf9qOwUhv_jHgITyUMVl6zbrhONyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STAX70EfEHCLoDhtR5qaj9eg6YTapgnxu39pygDGfkPuz_WnDYJzk1OOqTwVRNfiw1QVgiZnPj8JRq8i9N9qvcoHl4Mq22nfs9z8kcyE122iEXyQer05JbON5KfkiJSYKu0VyHgq_-iiC9JBJIR2YgQJXMVc0En2fbv0Fi1Bt7S69aqZWpMqn_N7hDoTf1CGsUFGK4Qv5qpwB8kLHBFY1Fq9RQWuIfQyMK-_VkRHZ-BClJFVK6AfqFiS4lAmp9NcNTT8eXxf0QVugZaPYN96p1J6H68bq-5po57aNbFl3mJstBbvGyu-At1A-pQBwapLogbjRJAEX2XzL0q_hNZ99A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icGqCL2xjPxGd39NXmVPqPD9I2QlXU-v8KM4BgOn44N5jMsr_ryvtAa47cOdG5wEsIlNcw1snrBER8PHx0tvcoZ3ySNbAWPlAL75jx1osBfYD2idtDv7HuTvJE2uo3v5Gwq9zhO3XlriZRA5_zRKsy2If-7AaIKqLbWK98xl1ODLXGlw1OAB25wQCkSCenXB9OcZQ2Wu3021yNzcT2T7E6QZ8vGOsfThW56yK7g6rxrYhGQWGMdPujb-tT-SdYNJZMgOSRmQU-qGKjnxwpDDIRxh3Qk96z5fY9xbwSGAgtP-v275H8_OdupE05jTno4-6BcTMolVupHHNf17OZCVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxzd25OVVQKb760jTQmQO3v2cGkb__n4LcB5UgRPrcwMsIBC5NsS-CBkg_h8dXhaZ2lmu_Icm47TQY1loeQV7qygfsReVsfpkdRPTZYBC4uOAcWNlGr1gOKOuK8JvfkModwkJmLaWeUqPc2ik42JfFCIdHsff7fBufmBpfNRFuakV2SgZ0H-McPGOa21em2O0EdCsbdMj08Ws2OuAry9iNBN9_uhfMA7lOiTxZS00BhT5XUMG0uwXdljYlI2nsY-9WL81lBchl6kKQuA2oqoNpLguPlPNzUoojYXm7E1arY0pJ03GtsaCMWiu_kr1JM2YKLmA2dKS2zcEMQViVk8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afp2MsalcfeNR0Csv16ZagRu4nUXbTCocJItBN2-AX6ezhDqSzAsqFzHVkKQMd9xNX3lyx6Hlkq-nQn3ZAKz9nmstavE6gLDaGW22YzzgtHx3GEZJtrvN-riwS9lcMQfKmqElz6E_hDytFP5r8BcCw-nKcaxudICrGFEg6FaRbCtqdSmixrr2rQERpRft5h00L2bTOCa4ZfyahPBUOqstzRLKOQgFOaZvbtP0ig1YyypihajZcqHJ9aa0Jh7OeOE55vPMRcnq3MQboOKb9A-2wO0-rMj4TAOop4AB9gHOjEkDCCw5zWOvAfrVRVWC0fT1pMSvISOheY_F7zIjDXO4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=cGd7FFTzqtlzDRdE5-8jgw43Up24X839dqVLzrorHrIC4S_6siuMmEx8lXXYZN7yURQ6xphT9RTqzavP80RvsMkr3goNLOb3wT2xsEPWSmqVkOV2z4Cv9bVPbk6mAEaMbhXx9FJQlOr0eZEcmSmLVOQ9H2q2I6mub2riOkkHXR0xdSSphyt47uVYFPHZcuxaZYBVba2ZvfTjyLpT0WbxV7IO3p-p5MohdPMtHF1BbicTklHiYVHvBC037oSRoDZXZiB1iTQ-eAVD0c8XVQdwL5jZk60KXYiXzkNsYZXp2S9SJYwWjdzQfY23FLEYjgHRRJt__eWFa8iZashCaD8qIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=cGd7FFTzqtlzDRdE5-8jgw43Up24X839dqVLzrorHrIC4S_6siuMmEx8lXXYZN7yURQ6xphT9RTqzavP80RvsMkr3goNLOb3wT2xsEPWSmqVkOV2z4Cv9bVPbk6mAEaMbhXx9FJQlOr0eZEcmSmLVOQ9H2q2I6mub2riOkkHXR0xdSSphyt47uVYFPHZcuxaZYBVba2ZvfTjyLpT0WbxV7IO3p-p5MohdPMtHF1BbicTklHiYVHvBC037oSRoDZXZiB1iTQ-eAVD0c8XVQdwL5jZk60KXYiXzkNsYZXp2S9SJYwWjdzQfY23FLEYjgHRRJt__eWFa8iZashCaD8qIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPJNoj8IDqFGgUJyeg6oWZhNvHcfF6GBiArkmuCoVUh8L_oT1BOc00GpQZwYrH-m-k2ujeOUWirIuJOPc8TzvA_Z_cqKhe3vclK4ETVrNixjpd3O1aUPR56dtm4xb0v0KJ8EziCqxgpCjvcZSrMa7N_Ibl9sJyy_xymhqED4WpkHsnnAV2MGVujMpnusUO3VKAUd5HtJB0nh8WIxRLjDIIoRotR7Q7Okb601Aaa8UNa1H8pO4wfn_eMkbv2VEVrm8w7lQ-h0S5Hmuqw984xhyu1l3m9lrS37gx4OmMMPHCHYM0BvAtd6uvYrSoIQKfBUBeyxtXlWKe6UeVfs5lE7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG0X4X2mHBl1DKJ_6G9fK9iPX-5qLcnY9giBIwytwVFYMRqrYvAFi1ZP3PsOz6nnqTqYKWoLTrupzQAPP7zeH77XyTgkjbo39PB5gswjUAmx2OIUQ5HptjUklL2fuMGiPAAXHDFgHBkzZihlha4bCMWhDAhF2MkMuBz5wPNHKrksC7mw-l4aCy5avGhY8ZaxxlPuVh36d9NCoUHAD84AgdcF7ZaJfxKYrwUOGJCX2t0C7IyUUqR2V3EbZlaVybHgdVxYob8VwXMIBSiIxnD-tJU_mrKDCqn-IfasOEvmhrm4NOgPW-jYfNg9IW8EOB0ub8rdFFE6AuL1iCEeczH-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMPWtrTiWzf5IxhBiAzh41DgJ5ofr15GPuMgQyOvwWI09t7u3iWb4ayoMOqeQnXGa-JswdmMMtkJtV7rcm9dS7Cz-Vcrx5HTbaNm4-mrHLKrFUKqBjD8EWlQojDvoZjZbhzkVzQUrmKtE6W7ToKxhJy5ey4204BMeTyV49MOnHYTReVXUg9tuO9upkGZ9pWC6lu-763XT1rgwc2xYDKST26Rn68KLzZvZSui15odnuwDyPALXZCdAmvxpnUXIr5GOqdOCsNgexZ2GdZlQQcH_uzAsGZoDhLTFotPS5pBArkpq1mpqxpqQJeVDwvK9dym5AeDyNlezRADCSJq47oGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=p8F6Ul29FO8Gcu-geGyQLBeEfu-EICPYTMRB6qL2RnMqqdFQzDzivE16gxoneCA2G8_ovA_N7jIyduXFjE99q5xRoxqKVd3eazQ6lWGsfcdPdQceaSDEp_ut01r7JQQxrQ8idBLC-PIQf-jEi9YP5gVAzYCr8l1jLEy8vLH5ZMGOllBKs3R8RUdoFb8UDr77Lbt5cO6u8yFMCRcZLKY4Tt32ubACEdUiU5zKdZgSSCeGQceDRTaybkSk-9xPx68r6V_0G202qTaK_80nz_Wm6S1I5I-Y_ywQStrzMEWzE5Wr13SgijYfM5egq1s5ThtVDFg1OXrdGo86EcI28iRxHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=p8F6Ul29FO8Gcu-geGyQLBeEfu-EICPYTMRB6qL2RnMqqdFQzDzivE16gxoneCA2G8_ovA_N7jIyduXFjE99q5xRoxqKVd3eazQ6lWGsfcdPdQceaSDEp_ut01r7JQQxrQ8idBLC-PIQf-jEi9YP5gVAzYCr8l1jLEy8vLH5ZMGOllBKs3R8RUdoFb8UDr77Lbt5cO6u8yFMCRcZLKY4Tt32ubACEdUiU5zKdZgSSCeGQceDRTaybkSk-9xPx68r6V_0G202qTaK_80nz_Wm6S1I5I-Y_ywQStrzMEWzE5Wr13SgijYfM5egq1s5ThtVDFg1OXrdGo86EcI28iRxHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unlGMPMPqVbWbaCDU3cBPiyQhgCYPk9iTkya-OYDFq1S0mw9Gn95hb6ManqgUQUGJKw4GfDGzUjwSRe5UOiRb7XYXYwcpVFlbv-bSzMIPvJhBsfsMLIJ7rmNbd-oRkmLTeMIiH8ezyK0P2T-5Cyyo4J1ozZ1XAI4WoIJcpZH9EKxAWSCQ2WFjl5mm5bMG_2gFSMZNfSHX7Vjfl4gCwZdg8g1lv8q31dKoRjL0zGXurBW0plsZpUMZMbzK30GLwYqPHu3ZAHAQuL79RuXv9JkUpehHVQgzYNELvA1EZEZF35AqUXjBPRr0Dg6Tczg9yyCrV79b90Xff1EhYk1VwKdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVLNY-VziI3R14eM3qrXZ5ROeu5AGvlZyxSffbFa7QEuzeNF5Q_TktgFk44Pc85GInleQOaTlkejNYiYd_6-eIga5dW5IjycQObIyxTEbVx9mC1oCNN24ktIT6eDONvR_-Cx9d3WwZ0E4u4HXT73lGedOrjqj5ZYAomY-BZQ95Qxpe0EEkrBYGdXG1tCZhSg0FW0xZKkf0L7vVFo4E1mKiTbSLobo_efAOfUi49Cwyabl1gQ8FGsvtAX3dJjQM4vjf5tuUA3_CZBlvdhMM7mQGXjUILnPsPsUMUb1YFX6skjdcvOQiylXCR_K86rGgDtHURswoGXJOQy4WsoE7yiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB6Y3zsdxjoD2UnT0X022ZbbzWz_jPmAH0-GfnqxgDP9xFf_BUeRuwuTcWevR5wE-2J8eVjfeI4tSXS6QfebEJpC2n1WWUpFgFA36Q_5QGycicaLRsJ-cVOb7ZG1k9Ny8a32y3vb0FinRJSP6_xy_EXlypxeq-kp-Dr_GWK8vj9AIgxpax6CXnWiksXkgIs9VLI7DbowZnb8bDndcgK9eyaXKIpJVCUpJH06Lmw5JPEaK1A8WCM5RRUHZ0_Afg12m7EklysaYj5FqLjKi_Ji7eMvh9TJQS13x6wxfxpZorXX8OJwEN-DTwkCOeS9R8HchETSs0xe-svcjHLXaSj1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vurVtzEZIU1Qqp5TMMhXC9egDoVGKkncJyvC2b8bVLzfPUUc2E0eqa8IkzYnMM07BLigyzEaUxBSjzgsz4Ztfx-ckkcIG4I17YS0a3uZ9Hs6ZI8Ws1YgFxdHUH7P_UJy2I6bVjB4o2NW2buKxQMstmoY0FB2zh603oPdMmHfVCPHMZIaPvxrusQlhGI1NtJvSXkA-_zDgrmsWzuHxKlpp9NHJb6bWKOfMdnmZIGtDOjqhNDBSyNGKhfhFZc3M4MyibGqZvALhT5VRLazRS1A2aDnjHnrXAqibRNdBdU2VDAub_DybNk47OZotceypksAnwcBz_lZ3nSBF7kup0J-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfGU6dHZuSWXFMdEK3rBiFHjgRmg7B1Rq6CvSxdBQ5Eog_ujTg86TuN1F1aYe0i4OTvcZz0dSwlmmFR8bZNEY2WU2chYnnxGPdD4MYCUqIZT7jWTFHUkNd5PyYwojJOd1EWAplJ0oK8sRXPtV5rpN8ezhmNmWtHZpUpJMzwPLHWiExbweA17uw1b17X31sTzzN8dE2esUSNH6oBMwZV0UQXQ29TrWZDN6pk9xiZHpj-oJIh0iU3_N7siO1kk1nUK_XX1jdMZgqWInx6q-sB6yAVDtGkh_aF6p_bTxzNFOvCn3B-v7o4dXuaWJuwDJGYMfWW012e3kjdHGrV1Pr8zEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW-X4TnRjBdZHLUaI9ZA83aHgkNIZU4TTBiiF5bIfV2LbG7ht6VweIAOunwWUj7iSf4VI21Mkp6lA0O3-QMOLwnbahx8Zenl12vHEiJpl8w7pymlLvBRnxwuJJ5b7JCQgeXd1NAYZbvVG0B6HcyRAr65O9Th7ylSBtI8zMcGU9gX9lxdUP9H8kagyYM3YDQah1ca2HwPko4h5gbEyuMS4qUZ_DWazRiYTLXx-bW3DR6oPBiBUH0VxMMpwJLqQKvFLQ0ALxvDWjeDmAxVgXev9ngyZrqAoq06Co-8t3lYZhnYw7lTfiZ9ICD0dhVXfUap8aCl3f8wUBi69zhHpwBU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLScKmAk46lIk6B_roWJjA6nO5Hcj2ePNrcxsde-2_9g7LtrHB6Go8wTJq1slMS7EzXNYFHodT7pIZGhbddCL4kJjxoTrwek-mTSV-T9_6OV07iuge80NmoJU13Bt_aH9Okv1qJ4uCeFvAcG-_2mHNWF1or54fSttyBLo_7EiEpDJeaUMKiKkBTPh0zF4eeRnA1YIr8t7ODnCHCMCQfNKXKpm2x6-HtHQiCS_89-m1hhN_AmdjRyNoVYuh48lUTwEin_8HRmMGOW4fhlxwn9Ra1csczfZcTw8IO_0dyahbaYTj4EWXFy_XttSeBYZeLQkmy9FryH_ihXwq6Z2Rr1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVWPZltkbvDOXhzC9Bj3oJfZjUB9iNaLxqDhpvKcnI3Qha1I9KEUAPpLB_ztn6liMoeLBEBtdMpQGTQQUruE-ZwwsnY7SKmwX-kn1VRXihkslamQw2wCz9mgGAnfd1g9v3ExWd8H5kQvGSJ6ZjYriAQUey2ctEUXZxwj5HCKoD_5CG_BlV7xPUfaXAS0YslbeBXzhHT-Z-mAcFf5aYkVkLNSsSgk0zK4ynLNtiPTxbprbdBWkYgYXqY3KBdzQ31ljX_kyqsUyRP8MpdkYcoEFKrsJSiw8e7MdS-JuX-NH-q473UYeo_QwQ4FGYfkwziwN9j--VyvoXTd7ZIJNWB4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5rdNNmU2YGFX0P1hr363bWapO6zvOzsdoN-p9MrOEQLeM5-xs_B2zeEJ-p687bAoTE-VwUkgcjMUsFWNFoJY0s-sqlXjytpsWhp06wEg8DrtGA_Y6gUvo739wLDFfBh9JVnqstBGE4hcVncOXMnH4ZbpMF6I4lXvnRn7xdFhnS0hww2mUcNN3dvDKd2II4rqt3u4MOxT3V0LODHIjHFchhbE4XOGf8dRqiNef2ljNNWIrDH4fvKFhH9_J7-rSRDShghcLhpboxwUOO5u4Ai7GpZCVAaw3z2W2991bPFKp15cJPidNoqLBpOuTkemrTHxr-2-zH6LWfEbULQBQfQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
