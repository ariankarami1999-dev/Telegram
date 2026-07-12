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
<img src="https://cdn4.telesco.pe/file/UVE4kDOR6uh7OvvoDUfGIXEaULS_ae5vGc8mSAzYrelbWk1gt4_Lc4dK_Rr_yDCzocEo25LoQyOLjVAyU1R35VACJl6sb49IaOqOPRmvPtjufM001mHfI4nK3wWTiflKjiaoGUNTZ-sVu5ACHdu2zJGmuB0w6Du8iZLx7Pr79RTH5lxF9y6BMNvDQIio6Fok9ztIyK4CygvczkAORQVu7jQ-vToGBQcbPCuJdLrFFkeXGu98o74J3R-RNXoTaAuEulT9JcrkIomqPTiVADI7p5KjSJstfgF9lzQNvi4Ain8vB2HrVO7Yd-hS5UOXTyr8aqVynL-fiCHC5jrWiE0Zsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 431K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 11:09:31</div>
<hr>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjs5bxTjsfcFshbPqq9BCg5u6eOW6GOx-hsPflui3N39Zlh9UbNwsktDzrbecJmsJ9OBIT_ROIhdjkz7DDOSDu4jxaA2U8XiQVUNXBqU07bASFXexGfeOVvywAn2ArCEqd18YDN30IwQ2TIxQ1aw3Fr2JxQiuml0_IJetemYwBWnU6psXQLBpOssK_IxE79Nz1pPu4aWmwnC2q9__geMP1JmfXCvGmHQUfGbCnCRG8rG8VH1wW-F80j-EhkXG70nifxoN4edUFdpcteEz6WoW-esrc90iN68vlAJM9Q_Vh90hl5tH7Vc4HWw5ltb3_c_luSiVVzoCG4Bh7XZ_7WHYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/25503" target="_blank">📅 11:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a0f9a7afc.mp4?token=JK3WHqBfwYN4gj_TR7N7vm2a_Kw9qpeWi62HkJlilACXSsn5p78PAB8RYrjlDsFZcNrnL2fsmHOsFe98sOBygHSylDU-moR7X38ZsBkqH283aXbGGmVinMAf0mB1qZEgf51Hyp1brcEh72MIqQJB04mZh_y4XwJ72I6sTS4u7BeX6YUqDaq7nXnrw91AhpMNARA2F4WOdQG5dkHZxPFGwH_w2sI8XjtEwixucCn4FQV7i-HWAzsDp_fuyfOCShKRKXpNBCrsngGSYcuDaOh-1QN-JppYEI29lSgZg2Te8ZrKldacnMhc0uhaqLYmSq36G8c3fi5sd22J-1bF7z-0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
نروژفراموش‌نشدنی‌ترین‌تیم‌جام‌جهانی۲۰۲۶ بود. جسارت‌وجنگندگی‌کم‌نظیری‌داشتن و شدیدا دل‌همه فوتبال‌ دوستان رو بردن. به قول یه بنده‌ خدایی اگه ایتالیا مدل گتوزو تو اون گروه اول میشد جای اینا میومد احتمالا این مراحل رو به چشم نمیدید. من خودم بشدت فن ایتالیام ولی خب مدل اسپالتی و گتوزو افتضاح بود ولی مانچینی درستش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/persiana_Soccer/25502" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsc7_WqgsnCTNwdAUYGxmBWY55pE1AomIYjgbVSmBqOrhDNC8uk5h46_QChUy4PrYuyqt2kH3JwWXS2TVV47Qe3wDAGEB3m3Cg3m2Eo_4qxKQln6yzIFmh2wlaVQ2xkPvfDw9NfUtbbGiuLL5yCzkHmOni0AGEC34lmqhSLf2aqymrHOtpehmjIuH_eEQt57q9Q105p2CzoYJYo4wSdJvjZX6Qg8Q-SjJ28_4u6P_hGjAXJ9PddkFHTxXXMzIQ2E_SZMgrCGJqBUQWQiHDklkCn8haW_35EOzSksdTf0BSPwmDlW8fUWBOgEc98rTRjXnafxG2FcF6yzGdISelWPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4928773d8.mp4?token=Giiw11oOwBugb-O7_1HAixbwjxkxMRpLIcNhwlBYN6bgqIyt9hy30gJ3n46aGMQUtmE7Tumz4vxYqIFFRw-Eea_E72NHRZiv-vP3ZAqaoYC_nnu8c25ahhpekVbhD-g83Km-NMcZrMa6nUEfQuv0s170KRX_MUberzWXErFU5j9zYWp_bbyq_s5_aqzOUlIr0D2FkbYAG6O47kKzxWmzPelzumoq14gsYLpK3kEy4b4tROKRBoO5FvVHHxtZ1ccY34nbrSWivgcnK8IKuHJp-u6sVfO2ijFS0roYCy3BmLIBRTLBi6agBsQIIGfhtcddcFT9ZBaoRGszSf6oC9nrcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/persiana_Soccer/25500" target="_blank">📅 10:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1HiyRluZ4h5anybNnolz0FOwTte-vkFoFRBKmZD7OIJvSibUTsPrtUFCoYCLjfc5IvmFFWzu4Y4pfBP11veo7DpxwdxjxCh4vuqvzv9zix6EY1Zy0-k-zfQlujErOticqYAAYahrDBZLwd0oY7iDv02Etj4S7UCXf7vpa4NFD4FNYsyKgew-OyLkl7EzVbYuJ09KPKqC5Te72Gi1jK-asMwMPJCS86SXO2qFv9f5V2XwnlIKT2HXFrowIlzSQATJJtqYSxPw4JhtBjab-7wpS0yhAgQJhl1ioQ8ctC9VAkXDr4M7tWPFavF_k5zzYu02C32riK7eIbR9R45oVayRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/25499" target="_blank">📅 10:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAqn_FqBQkc8pASUX7A3Gya4EGqekPhx8T-2MFQu3Z7oJO-xkCMZUyFAxFsNzYvGQZHvEO0msBXhvAejcejpXwpeheMUWhu8rtiArmOei0B2-FqOe9Ycgq6N-npig5HVWG3cLuFSlqJ9eQjTI0LORLyDgxLgxKkoARRmnAXAwuJcCX_14fPp7leoW1pWsOE8y7n1ukbYzMJztuVZ7mPtWnPw6hwVfBWHvLkLeRWu30hnuOQ8Jp_Osol1YJOWqcqBAXHuILUrCLaDjN7m_tgRmS4myUuLoBeWNb2wJ-kvU_Fg3JifLs6c6E8yFZKXpZ9YFUMlLORwBaof2TiocILW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ جلسه مدیران دوتیم‌پرسپولیس‌ونساجی‌دقایقی‌قبل به اتمام رسید؛ نساجی‌رقم‌رضایت‌نامه رو550 هزار دلار اعلام کرده که حدادی‌امروز درجلسه‌به مدیرعامل‌باشگاه نساجی گفته تا400 هزار دلار حاضر است به باشگاه نساجی پرداخت کنه. قرار شده که ایری…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/25498" target="_blank">📅 10:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=Jfp8QO_FYyNUIA6g3BRbLf1ZhOlYPnKGM_VvctUXKCHzb-AHcAzsFkobU55jfdYREWZgZZZP3urR8LAAsjFGt5orkRjLm4EyfYbbJ7HBRy2j4yqwOPyLryGlk8tVGJzZpMChXcqvOC_u8q_PzZZyoz9GFY2bBdhiTvkluMq-6jiQBgWQRUmhplvlN22yJey6o75EgGif_r0z-Yb8cmlPdS5er-Nu6ISmAIrjKD077ysTpuY6vgLifJ-uNMKBFjwDnI5ALPdJbQQeJ0QSrCVWKhRrMHKLZQ6VgnH0L_Z3Y7gZ5xr0ErTTzpXqH5zA4y3zC1n4ACGXZTNhDApUidTh7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda5f52119.mp4?token=Jfp8QO_FYyNUIA6g3BRbLf1ZhOlYPnKGM_VvctUXKCHzb-AHcAzsFkobU55jfdYREWZgZZZP3urR8LAAsjFGt5orkRjLm4EyfYbbJ7HBRy2j4yqwOPyLryGlk8tVGJzZpMChXcqvOC_u8q_PzZZyoz9GFY2bBdhiTvkluMq-6jiQBgWQRUmhplvlN22yJey6o75EgGif_r0z-Yb8cmlPdS5er-Nu6ISmAIrjKD077ysTpuY6vgLifJ-uNMKBFjwDnI5ALPdJbQQeJ0QSrCVWKhRrMHKLZQ6VgnH0L_Z3Y7gZ5xr0ErTTzpXqH5zA4y3zC1n4ACGXZTNhDApUidTh7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس‌جونیور ستاره‌برزیلی رئال مادرید امروز 26 ساله شد. او تا کنون موفق به زدن 128 گل برای کهکشانی‌ها شده و همچنین برای تمدید قرارداد بااین تیم با فلورنتینو پرز به توافق کامل رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/25497" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ0fFUEwtXThD_Bv9YSbe00ozW1FlX2VHDBEO0xAlk0YHKOG_TlOMgaZrt8Mm1A2pEDNdl2sYV689lDIRRTS5aRAPEsWLziZoOFWZ6dbY1hY43PnIwD5zvT5C0aM-mXo7Dr4-jjbHu4l-P8zbOGICd6Vlco1U0ArtFktsDAWLB7LBX5MzQcNBPhVVr-vHI613p2cijbpRmSTgu5sPUJPCG9nFVkoZD6xYc6Bga3mCijBULOh52KmjUCNYy6zGWnGBdPOrD_jLvSgFg1qAgb2XSQgT3yLggiy8ATWePHnXEZ0LBC41YEJt0bhHcbACwUo3LDF8TsnuvGCQszfqzCuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
5️⃣
میلیون‌ریال‌فری بت ویژه ی فینال ویمبلدون
🎲
بدون ریسک در وینرو پیشبینی کنید و از تماشای تنیس لذت ببرید
🎁
🎾
فینال تنیس ویمبلدون
🎾
🎾
زوروف
🇩🇪
✖️
🇮🇹
سینر
⏰
امروز ساعت 18:40
🚨
ورزشگاه سنتر کورت
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
بابیش‌از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/25496" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=KgXG4BM7cQfr2otAxhJT2U7jJSwZf6qFvKaUr4UoOBKMiWjqbYkERwtX0pb3pwrzh53TieTbOA0jNvDzwGrUssjxayiwwinoj1KTA7td6c2zWzPcQWmfisSFtP7tCLW__YY1Lu9zYM3WdAJWCFXRRlubC0-jLU6DQp7PvYozvSFDBfk513J2KoEkYiyKA0Jmqunrq9etJQUUtrNLTo8qR8YqVeFXGCIPfn13B1C7LNsSDNxIrHGUWxxJ_XYw_p6MPPmFFyucOwv6mBFjDfEoxBq6CI-A933ir0x9DgfhQJg3EVWQxRKJzAIQ-LcyulBlBnZN1FCtRUIljDcx0u7XEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63b6abc08.mp4?token=KgXG4BM7cQfr2otAxhJT2U7jJSwZf6qFvKaUr4UoOBKMiWjqbYkERwtX0pb3pwrzh53TieTbOA0jNvDzwGrUssjxayiwwinoj1KTA7td6c2zWzPcQWmfisSFtP7tCLW__YY1Lu9zYM3WdAJWCFXRRlubC0-jLU6DQp7PvYozvSFDBfk513J2KoEkYiyKA0Jmqunrq9etJQUUtrNLTo8qR8YqVeFXGCIPfn13B1C7LNsSDNxIrHGUWxxJ_XYw_p6MPPmFFyucOwv6mBFjDfEoxBq6CI-A933ir0x9DgfhQJg3EVWQxRKJzAIQ-LcyulBlBnZN1FCtRUIljDcx0u7XEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/25495" target="_blank">📅 09:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHzX5qbytv8r7vor81kh7ev0yq2p8HD6K-375Wpu37JYyMKFGulSz29efNMArGHk3athr0tOj65QJF3wdIaXgTnOdb7Zz6S1jNu3DKQrGoea5avRQmu37XF0sE4zjhJOwMrlcji5k7Q7ExHrxcHFD0NCCSZYwdrftEcZlewNchIEy7YXTXHZPbCqgqDmuEnVJQyMFRXTli50QMF42X8Wscg8g81oq-8UgaqlRADRZMTDAdRt3Ah411QluJrAt0xm5GfSfpsxjyfJ4ITQx9CJJ-BL9uaHDY-cir8fHQzl0BYwJqbQnuQ41AcjjU41WsI5tvrArFaQG0iu29G0S5vgdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/25494" target="_blank">📅 09:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjkYM5kNqZ8OfF1LA0-dxlE35i6stmGFjVQNP8G1XR4NQEE3-x0FaIb8xTMfRnyCTfWxSUdL1LCC0z6V0rn-KPrN0AEVobb9ryCuVjavuuYd2c3W9M1q4D7csxaK8nWPy300mNYcSlBwZ070tw1wCZJqxEUk780Ac5TzbF-UMecUHvF6qJXZfP6iyA8RYJHyu9a4PhmOUgNmVoMJBD-T59WnUaqV3eXIKd_T9YwAjZOnZnTSvLA_FsKMeNRbLoRCII-39a1GnqVgyAJmUoh9NfMw3Re4I7u7J63qwL2jAhgAX87CbsOVRL_RZedaJIAjdzjfnkwy5CnftfCx3KgE6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا
؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/25493" target="_blank">📅 09:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_j_kptCKXSiPEEGiIf5YYdSrSnqmgR13RFH5h2gyLTCXUV78C28v1erYj1vvq-QEQ_JOGqj71vgSZ7B28jtDsAEwE5p50TZIT5J7fqpxVCIs7MPH4mepvn56wgGWIYMQXIC5iowtfn97kND4YJ26ETiKY58IKJZ3jxUM0JRxRw8rwHyWcSzArpVb4WMC1qIoC4RADcgo_MPj6jqYaQVxE87OeVryBs4ShzDOLhTLEhSdBsgRS4hiG9-eioKecf29_fPp26uMQIK06jMnjJA2o5FbDdMViyYD-8Un_LAAitP0YaS_EkG34ycfbGDV7EsgbOVH0Z-gKvbUQVkCiqiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1-RgkumQMhyONcM4YamG7DcL5gQbQjD5kcV35QWp3m6MuAi5FkonpYilB6f9mxlN14ZDW9RRqf7XQu5ewJ1XLnZksHPTkrPCXYAzyr_DE3XMQlVQ49LmjJEPkS9ISADPb_tcS_XA5xIxEkcC5hv0GtmpXEvsN5Q0zn2pjgupG9nf8SeLTItCI9ajovyKGepjwZLM0StTleW-Ce-bCCtEjulnEL9mBssQxt63BiK3LriP-egxYbr5HHkS68-QH7ZzoCNJWYdvBdZtNW2rMkD_DXH1ZIrAERL6dYZoAmX1dNLmfGZh9hrgSxFjXAmmyNoN0qZXZmPR4WHnh_DiB88jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iipIDfJor0R5Jk99q0-b8TRx6xpnuPY8G5BIO9_qDTsJpS-XtMaRJFJy-sfaYgxh0DkZTixX8-aqlARPMIR-ZDe4GWWoX3C-HaAhYfAC6N4-1X_RP6Ob5G9rjrPx0WuMRUVDn7RMRcSIvtEwjo5mHWjqLaNk2ya-Ci944aceD3B-K4227NqOc0jKqYJFImBq_61FLlSUMQGl_SjzR-LvghBsDC8uyUGADvVmLVYJzCMGcfaABWjmAmkDCrsV10o1rRQ_Y3jyeixiklcIHqa0hgLTIHAJ5I4-qiX4B_uB0hECISF1NbexT1lbxNAM94SLBkzWMpIGZagBx5hkIdvFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQMZ3R5UQaH0wfKfqi4f16GdHEIb28jVFdJQJ7vhmDkvhnktN1VFHWpmgfEiQmuydj7fay2FSg2jvhH8cjCCWx1CXETtG8TyXOaoQ-IqaJO0xKPGT2B8WIi07yyYxpii0zyLlmWJp044nguWa6_PS_YaRWKqp6P_FufrI4xJ8OMNcQSbSFxXQnhvmXPGRaJLQQjsqFfHl6-KOrVVt5rsG8dn_FSqcDaDVsgo2T7CcZRH0P2_Y2ca1HX_YWSsGr3kjhvQzcPjFaRrqeQD2oRE4fts0vpXfydsZipupD_DbJfXuA4HHcKvA1Sx5CSIhYqDCK3_-Rgyt6-nUf3D2tXkAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv8eXNPDwZnyd9cVwcWY3iMaKXOrqiAPfa6ugB42c81GX_8riL8UTr2LW-euuIWnLM81BDiwa23dbCKu3PjvB1q6DD2iZ3ilSMzNLtY9qammof2DlS-K0SyC23RTRADgo0r0AivI69ihrJ2qFPwj00mwLmIPETX8fa1ybHzgvgVWA_FUH_Nej-RqBEBS4nZxY6Uh6jGTpdv5Y-zHczY2mRJFGGzFQL_ih_wv9iG-QtD5hnIuTUs41JnnbSHMqEbUnCXRiEYP1ToX-G77NT5EeRmX7Fr975WJnwNtAFuZUlqbWY_2e5LCT0v_tMBSvX2n83F5oy1OI0Y2zmebSIa0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcR6_mOgBqhmIbQicjw1J6gb8yD6_gpOstgH-R4PTvYY094kvb2PiMrh3Qi1zbLUxFF_E-Fssrk8PBC7fxZ3FkLy77teYRYIW8LIM_q60vhVTy49_2k29bnuwdd8ni7frxYV-iRCNrpPjT-nX9wu3192X21NnoNZdnvCcj6ikypz49azy7tTr-q7amkCDdnMrGgHL7O7k-nyz4aaLnlbq2tkmAQ-Hmjh5HJjBg0DMGckJEOu8i8BYCHFUAYso0zmt_pLmClII-bTOVePh19316-rzJciX35d8v4eyKAR_IG_mvfBgPBHUqejUqpsTLM_stajbh3VXbCxaXRa1HicCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=v4FSpkFmIDmJloFBBWI-DfWb1b4OiycuwJJNzWI1SH0DawPexdcXNQzapOxIl_GqwqHKGHrsbvjKu6wmdOqZe08iup7inWYfkYB7VK7ETRjV-DAhnhR6F0MExt_Jusv3ZJzvCJLpQ9Iut-vZ5ayCDjmfkmd-QuWVY_ZmWhtv1xBibAWuYpaFjmcO8lF20JI1f0_7QekNHS83pKmtHO4uHl_3QDnE0mznWs5-2JktOBoYoyDo2XiPn7T9zMZumao6BXcYv-u7tijRrdKtbPdfWMobFp6vAW2VCLE1-BY_MivBG8Oh_Es8yeLS_52z-huAUIVv78zrSqPvYoyNwVbRFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=v4FSpkFmIDmJloFBBWI-DfWb1b4OiycuwJJNzWI1SH0DawPexdcXNQzapOxIl_GqwqHKGHrsbvjKu6wmdOqZe08iup7inWYfkYB7VK7ETRjV-DAhnhR6F0MExt_Jusv3ZJzvCJLpQ9Iut-vZ5ayCDjmfkmd-QuWVY_ZmWhtv1xBibAWuYpaFjmcO8lF20JI1f0_7QekNHS83pKmtHO4uHl_3QDnE0mznWs5-2JktOBoYoyDo2XiPn7T9zMZumao6BXcYv-u7tijRrdKtbPdfWMobFp6vAW2VCLE1-BY_MivBG8Oh_Es8yeLS_52z-huAUIVv78zrSqPvYoyNwVbRFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSw_7ia6wdoDUhipFnvN1dGrNxu1MOJYnOfG97df1_-fYciq-KKpVtSMirLWANvpzGLmQvOhGHVd0bu05FAlEUh8lhsl4qgUlGF5QdvJzRT8OS59y6yhrFP0ryKKyLAssKBiTKF0EuGtTYaNEXsLpv5zmog6e1po9sFH5RFNCQjTNGI8PkTuRVAaGBHLl51P-MavYLrdpuxvesetdpyOd_JkhfioT863cuVGsYebf0Nzn_y2f5c-igV0mDlbEJkl4df5si5zmokNoT7d3SS7tHR3P4udBcGVtH1bX7dfliFe2DTz2fe-5bWocjm-yJSA4QMuAGcSCoVdGJWEcmg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyau-GVGPPYT5zwCd9GpQN-Wzq1AWT-pJ7f2Ypt7xqSOT8-S6nUunn_N6MgipbR_2vv0Qjdl9v-0YcZujCyglkrQIiPr7uRhtYNyY7z3Z0a-BKe00msi1svcqQjGtV1y7c42GZSENiEJsv2AX36Fgdd6K82bx956Vuk_VU9jhjRZJlz2jUmOtwwWIukMgiiJ_YIRDpECbPzbnM1WTEzhKqc5PgdKmf9lddXHATxVLhIuELYoCAp5PGsHQPv0wgbV1K3MTfFYct-0zDu0gjggDEj8nq8i6NMKIFFGVbjToAJC4IQYvlEK3p9JKh7xfUxaet36rCiuiChyY7fzPZ4zRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTMYrb5y2vmy0VPc7GxHXFkC0s5uBUENqAMif7uLEME7gkQFcYOXQ25d-gec5rfFZFhOsvTmT4FyY9S3fhZGxN38cIlfb4nyLKzD-EQbub8dPMt83z569JGoTTz96EwNJ7ypcJrhBB9ZDYScypyw1NIvfSU6AZ83W7-6yKaEd8UdkMcOCzW4mjDx-yIDF9OpXgY2fNDpvT4OFMGGU_SauANIi8bXlxAdsbexvmYWbPGSLuy4BE2DCy1ZcJU60xdL1wHxIvtoxeiirVwEeYtj01jS4Ni5NcWxaQL3K1bLvrkquYMrDjNpQ2vzMb8bliM-K-pT87wAZsAwyikUHzr5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvgjxT3aZR030Mx6fJoAKp3iz5PIP7jedz26VjyBWINBGEiIREO4nOfzSmgBv9iD2n7FJhrIly-ZhitD3Un0KuPVIK-NKIemucz6yXSELLStqNwSENsALnlIPIHmBvj0N7fjEGW9niuTaz7sKsuROcmm8Ifvf-5z1jZl0JLnijVESFsM4wufGXdTV1l-kMLapqvqHZ1cneybmCZWsRrlI4W86bC25C0EpSueVFKT9junY18tbm5XnIyk5Qkcbf06BnYOxTbX97prXCr54idCEDCb0Fj8VVo5eSmurwaEZqA6BZPzeuY-QutJXYs__8En2IHbLVFYJ3FrMFjXsspfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQk1jGRnlsm-gNW9PUUQakEjOhdFUIDNISjrJgL8jAwC3qmAcKs0188ZnDJ2mlx6OZaLXLxHkijDna7YjW-4AJ2fEWQT69tVgeTIR_uw0OLXzMnACRDgxFCl9zGTPyIhz7JeBoT0ZnUGf3Yf4E-XLK30foKKFAhzfn_ux-cgkf9PxszqtU6yX9gOLrk6UFbwRa3lDUZndDY6vn9I7IdtCaMWM9IgnZIABAAH_B_CB1lsFKX2LGAkAliegH_ajBQTgFUeciQ4zgof2xn1i7iJOuywAG2brDovnr1bIsLBHtZy3dvFjOBovvIvDStxr9z4-ZhNIB39x7UfBonfsMvJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ieh8r97hnYKrRgz43i9Hdz5hraqt66RPjK1T3fnXugxntPCAc23WDWj2gik2G9-DumbFrHbxeK0Ex82SyZMp4RKD__Qbifavwnv7UfBtuwXcjxTEFjXsgxcV9OL3nCVJD36ttENDBRQJsmSERyjij0Eq8ZsEd3Le7Q6zXHO2Ie2A2oZZsXtAfhwgwnlJXKXYB_M0XZf5xVtRikjiya84Q6hyo0AAI9kBqzigvcFUJuEcXgFCT9wGOkwtgE3fQtUQ_G5KRmRQdW-JqCF15KnejFiTHkQEHsPRS6PVNP3SMpA79lBi-IL2bUm8pHSEwxRADlMA3Yk5zQD1w234AAmwBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZiwdDkVBa6hFMh2GkrWND4wi05SNV0YPALq9sAPRHOup6drqcKykqh23yGLwCz_RFKZNtXyi96cxEcnY4DZ6tpfwPGLy4BpOsxqa-d6X9fRHPy2J0rwGRgP_zxiytS98ofeWcW8Y2IoNMb8cKuz6P3_aJ_7I5T1GYumTY4YcFleg-WZKQRQXkSHuxM2USxw0R9diZf7N1Ia4joGmDXPhqJA9_QVrUDpRUAmQmHF5LsyoRMnzcF8_Oh_j9UAG_RDTP_hPVqwVoHJhHHZphw7lFRYE8SfxFq0c3hVhzW95Pr-R3GWynrnaVHklo6-rNZ2iN5qPg59g4ozQ3PUsnPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSFibhxK1DfNTy7oeZWx_t7esT9G4V3UFHNiXApyuOXyTulG91Ud1E_kTk7_UgfLKK-mgn4QsMuDrd4iXEmzCl4tmXj2N0rISBwND2FQhCvRiAIYS1cBTX3DypU5rgxFguswNkzBVuujx7JazysQXtTeryGWEMLiYkE_iGhm-UvfHhg33_pHRHuH9OF6NkPLXY5bVL-PbRKbhPz15QhYcvn0-n4r5dZEncVzbBIN-TIm5jgBwTiZLK4f-bRRmrj78qxchAkFaGaTMW5AdN4CLv3FMM4MswYV1f0nuaBRG3eVNB0RQ0U2PBvUAJnXdwBJf-K2PKPn8icVoQ-3wvn_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rac2itQruu8G_Bdos62hFBt1F3iFHTr5kCYFF2CB8AePqed3EOmnYKJ2UjnPqqkKLN7XIJsESFIZG8BGmu1tlsiwnfc0JCsaqTjlo3UL9CgPVONj7YrbDp1mjNn0XUtRLBHTKGOnetahF1hw1la7gBPXY72bGoG6EguMPX49Gq1hF-7WiAWO2cAdbZvkA5hLRs6-u5dYG-F5B3AYwiQvNoLKSCzigUHauq3Kmd7__RJvPjw4N15bA1xWQISDdG8Pi3Mm6z-igTjy6gY3m-m43Vs-vZ7uTN5a_XCWucWCx-iJofeHeb_GbB91Tea5vJ6CV89ix6N_Q4zKXBjiDsbWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=A8RBY0wgcwYZZtSb52extsIBF2kq5bUBjaTEFMv9yspE39YQNs69NcuxzSvjhCRcTjlnowHmvDlFEbjqUgqLk_A4EaSgraSBArY_mJe_ClPZIyg8QuMRqbp5gHxJhk6QvOaIP3MSzumP9Jl2HCzEEcDMfLYzxcKQGGQaDh_myx2zhRMqXbY1iVsm_va-aKCU01iyX773z_4FSkzQF4inQv45t6S-C2ihIbj6qymuUEgjya8DFvarxZTYxisjtS1_Q-1jzTqCnwS4TB9SIPNrRBECGIgEkUfZydX0s5xSUrUQLu-BB_ZlZSBgL4A-1YNCj24hQTdcCzVcJzkjYbMypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=A8RBY0wgcwYZZtSb52extsIBF2kq5bUBjaTEFMv9yspE39YQNs69NcuxzSvjhCRcTjlnowHmvDlFEbjqUgqLk_A4EaSgraSBArY_mJe_ClPZIyg8QuMRqbp5gHxJhk6QvOaIP3MSzumP9Jl2HCzEEcDMfLYzxcKQGGQaDh_myx2zhRMqXbY1iVsm_va-aKCU01iyX773z_4FSkzQF4inQv45t6S-C2ihIbj6qymuUEgjya8DFvarxZTYxisjtS1_Q-1jzTqCnwS4TB9SIPNrRBECGIgEkUfZydX0s5xSUrUQLu-BB_ZlZSBgL4A-1YNCj24hQTdcCzVcJzkjYbMypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDOUBhMRhEQiEUYEuw3-AtBwcH-K_96V551TXnipRJf6NurUO6V66VvoS1xu3fTIaQpYy0buPauNZjqmcrqtgBKX8QcUMlvZZ2yiXYnXZh5BgzEC-3o2GrooZJe9Cak9uYidk2vNX4Kn6Kus_VADk1Dh6PScuhkgiQZrNLrnqC5ZU2V0Z5XBw0bKA59VsJjZ-K7mitq1NHGJE5LIz2909ENWz0D_AFR_eZA43Xg7lAt_5gy4k6e3sTv7WOwSTOLIEIVxaut8__GedmSnxal4JOwkRNDSwipcbfumoCreT-eE8X0mkfO3Z7F-XP0A75miRIvKlnNiTcXUpGocE9cd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=hoqKhNRnr5jRd2YXs9sLSAFoBym3tntowWt1L2lq12mfyNiw2gtecC9jG2PjPn44ZIkz0OopYP2qkOIcj545OtuKKHzGtgKKxWil52gHD8MPtNtgzFbkEYD3kKV-mlcgVKbncNlB1XoQzmv0BtUCX_5h4W5FnrJ5EYeu4x_DWlvIXwF0PWtF6ZCa5t7fq8A5U0QmnvZzD-Tv-xlRxrpHI-rJKtySPk40NgytFy9KfkampXSww_QeLOOd-DLP0BzoxNhh1Zs4mMJMGJo9vhkgoj7GuNeBtn-ivAwqz4iyFu_de2jD4b8FGLtA_WEBvfFipaXPioiOBxjhwlPuml8vYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=hoqKhNRnr5jRd2YXs9sLSAFoBym3tntowWt1L2lq12mfyNiw2gtecC9jG2PjPn44ZIkz0OopYP2qkOIcj545OtuKKHzGtgKKxWil52gHD8MPtNtgzFbkEYD3kKV-mlcgVKbncNlB1XoQzmv0BtUCX_5h4W5FnrJ5EYeu4x_DWlvIXwF0PWtF6ZCa5t7fq8A5U0QmnvZzD-Tv-xlRxrpHI-rJKtySPk40NgytFy9KfkampXSww_QeLOOd-DLP0BzoxNhh1Zs4mMJMGJo9vhkgoj7GuNeBtn-ivAwqz4iyFu_de2jD4b8FGLtA_WEBvfFipaXPioiOBxjhwlPuml8vYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-JYUcIuKDJfVXWbFazZnz17PIjiEqAniaxzAL90xLpL5glTUpEgdAsjhFs3zAgOuslfEU5n-ZKrknIHhMvjVOe_C2dVdtlA76IjYKT-oJlXQmQyxW6yrp9oj1ypQvEgSlvhHZFB3BvxL-n83k7YVGXLO9jfSJCAfi-TxmY3yMr8814tIoI4HWg2jyfPkyXajpelYa2tpcWP18iGFahlrTfuW9gn0lqy6Hc7NwjwDyN5uk_RyxmmJNgMPloL4V0AYzx2hXh1gqHnl1YPGudyGmdGMGEwLYkxbBCY3i136vyJ_JiWq3Bnuf1WTSGzYTxDBoZzB40lcSVyjx8rJ5R66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2t8uD1vQ1slxmhdwC1fgc_Xsgl9g_sCOajMhTDSrXAIifv1ySE6UhPA6MvX5gk-LiZ8b1Ry1LSu-wEqrvmTz-9iB4YRmVFu2LjwBUcDCxQj19qkcuJcLQvvkL0QSsHcYPcwXXI9PaYaU7kMkpLeov_k0HHJgvNb7mG51GUhWWAHhXnzA2JvU6wfN0NE99K29-S7P5hnySNC7H4RaLrCKnF4WEsvkthDMqfw7vq68So3aQKvsDVmJiTv-Vl0u7Y2D89yUlExtod9YFNy2wYijMjYHC4QLR5-4AVIEVSZnfuq5iwqIl49hWM6XQXY66-3zFXpPt8VO06pBCok6YN0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANBa7EeCRsefV7EZbpE4Rv52QMS0_9YIk_DVMM5w6CWbiatwTGZZr5EM4KcBdtS6k97ThcQj4mlKcZnisnVsVmCccKRYTsG8GCv_vyUyImZBeaLcsJflWk3mwn3mB4ctWCe8Z31fMmH0D3ZaG1_-V96x_wbmMNefExGOSYsnH4c-f5tT-GYdaZtyQJdhGGJB_I7AA1SLPWeZfDd5-qlNXY9s9AOUCEQD91xskZyMl11iOJ5oVHVT5xQ_uhOu3u4hkJbYSp-btjPhUAvnAolj4TZUwZsFuJzxUKuP70c3HiF-92QjpZKpGmwhW1kF1Luk7qPdXID4avpA2MiOMzRuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=u4lIIGTLzqqrL1IOQh-eixEqc_v_ntx_w5mazleo-HaqCQY6kJLh_LcZi1aaaCZnJyJbDWXElxfziKeO8q9f9CoafSel1P2BezDdI2Oz-Wwn-2zGXWH84tLBPgACXj0wkC5CCvNHcncGlqxhFJlNv7ummxbOJEwAsgTHtuj8YnqAoO-LPZE_eeq5-pauOT7SOM9w9ackdvHHpdIFQ4RPmLEtQWVN-y_GtqeF4QKyEDKiuA-B3HNoEk5H83iUGREpwqHbSrqiPQ2To4nWkhz9Z5okuqsPbgBJlfktN02O2uZYPvN2_jYUMROHNybTaILaXJnyzG35Axw008yaUfLIlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=u4lIIGTLzqqrL1IOQh-eixEqc_v_ntx_w5mazleo-HaqCQY6kJLh_LcZi1aaaCZnJyJbDWXElxfziKeO8q9f9CoafSel1P2BezDdI2Oz-Wwn-2zGXWH84tLBPgACXj0wkC5CCvNHcncGlqxhFJlNv7ummxbOJEwAsgTHtuj8YnqAoO-LPZE_eeq5-pauOT7SOM9w9ackdvHHpdIFQ4RPmLEtQWVN-y_GtqeF4QKyEDKiuA-B3HNoEk5H83iUGREpwqHbSrqiPQ2To4nWkhz9Z5okuqsPbgBJlfktN02O2uZYPvN2_jYUMROHNybTaILaXJnyzG35Axw008yaUfLIlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3FdtNyarYvNaim0QAkpa-Bi5YXq_6ZW3OpnKTJgBoXdKMPjX0Wrx1orowB6815RmOR5L-b-bHLJlOZaHIBx9DTkDqZ5qijdCz_mUSlShV1SKS9urdpOAJmP8MMMW8hkOeE_AboDkskEXrdQwoP2JD2pYcgqsrK7dd0ME7RAr74LC4l3bIxDsfS1TXcGHudGcK0zs6BgK78sR36F1m1q7vPcw7mhHUlA0W8VB-L3CRlDsWl7PcBXJ87TgsvAVMKs_zCtQsadEwFEfyrZhi7bP-M-FKABmIAvPPGkA_VYyW3X8rTF44S7etekIT4vhljzGeX7BKlebgiex2w91xV4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGXpwxgYdxX_3hzYSzNxsZFtGWDbsKJcjENlUEmowV-J8ysRbMOfjgxPpEsSsKcNPWeBGdIcf_IhpKenhOqzLxqAQdgc-aWG5AsJG716aPRyGrWihs1IpkeSXHI2KWjMP4ynDL7cBwOv8fJP-iIKRohD3df3R-IaDfDeFTA5LxImGNqv2igdlqJDtBz1g7I6p9xBRsbn7x74slKlduSmwcyrOLe5WiMx__uQIy8Otpq8PlcnW_BWZtioRVjw-YTX_LwKw8tSR3JzkhPE-L59-vUdWhIVp4bqi_x0MoJWexAwntvnfw14N-OFHaPTjHEk5Kw8psQzHFMpMX-4H3GfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdZ9kQ30pDHBAYFzyOexNTzbuECi1twaaT14FtjdpO4nDE2sAQ0D5Og4tjiY0HcP7FEFHBhSP3tnb6AeEehXHld4djS6PWHbnOeN-4B8e9lh8BMpTvjYhmoVfye3K0huhRwyH1AZjMG-9mhpYFT3Kfn3RXTiwPSBfvsEnIAPFMoUJ3rjuQ7lL7kms5fiZSTr8DCJx1uxmxB7NGf-LyPCZ7i9vXuBXCx6KPGE1yMdS2rFrBwAKwaknuefuvIWxGYrK-3m4SDcMF9SHxH1vDZ1THHsiXWyLdfJj_JcIFoRYLenjA9hx2pHM9A8HQg9kVMbGMwc6uZnFTyuLqxietvbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pao0bPsyACtrfgTRjpWUsZXrnTHoq9Po0Pf3q8iJX2XqGIF4qj4l2lQd-PYXXkd-FTCFfYXNlbyLa-7_1Qhyptn08_AN9GsrDP67-OBbPVX616v69lsPInrFvsU50FpTpzUWNqVuTmshAD-UkdWiPUGWUyw2SozCEqkC5Gwm2s_ePtVseenLxd5sc7bTmWCF-ug2TLvJpLZPihm0bptYP6TZmltw3gpAX2XJfjOEYM9GVGMDQ8PNy8Hgrmkcb-7dEXs0e_-K-yZogFL-ReW8hTYaRaBYwrlIffZ4rIYNmZbP2burOhu5ciKstxIHi-qpNLxXzK6iDmisGlGvhc9cUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-8FqmoPM5Zj8mWxFADbB9hS3vMxXSTvtUUjkvz9xUokECsBA3atf1QpAc7_Ya5qL47yttp6-_F1LDPs3HqWbWgF7WwaPRrK8feFtpN2JWUnlodoK0lw09YxF1r_usBswvYePI1UaJIloe07uwYD3L5h8B_oxocY80JCSp3T5uGI7KDoHwSx8pfEk7k2Pp0Ml1qTApwjUlNjlEYUnQl0W9ddGKdtIsowDCyzAxs-uJRrN2ASvuO7FdSVAHY560AYV7jd9l2Gt5ioZV7W5vnWnKf2ZDMSG_qEXNFLHYKWhZ75PVSWmH3mwZf8pevyMmhPSAVMiAiW6EuF2o3I7S6rtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPM4O4Y9Q_xJn6JP-hAkR2R2q9ilpAGJxdNmip3m92FbQne68_yhR3Tk9eeSnugechgbquvbrHSQo8Qn0cgZsyXi_gbsnpvv5t4O6VJ3bDeA1msApUw_29KICDxYz4g0z9WWjJNrmHHGoQm_qW0whRxLt_YJWxt0tC5sg932-1YTHbHi1SnAwRcVjLKKuNIg-ngaA5gwxigryTJHcHkSLYTsK66UcEs4Jp7PkqUvIP79SBi3eVihrJ9wib8YKiObEeFsaNlTQCwgjM3sj4tZZE_DnVYhueCaNCUaSC6-CqmLwZras0131ROZUF1N59KxtpKjrEdS977MI8DZfQMnvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApV1xAxSdRt9SIfLLBZ13pRJiCZ9aD8ZX8JF_zF86QuuwxB8fqp1EwgqF6LM27rFNmNib61Bde-mosFuEIR5eXZR4N8O7xIytKTFMwM2mSu_NiSGiPyFlGbW88qPAkrYGaetoiUh-m6JJLki_XDw3_K45Fdws0-amcDNNDRUGvLeG5LOd-VeQqGHt9Q-OI0_74YNoslOwPYLjjTh7vT1nCihHvkmiIlomB5Ewtqzzme2XeYXWNxGmsMhHfowF7zFGUcu-xZsmjOlw8q3xQu5kO0NlqZBgNsl6rxmXB_llHOptNWeeRQ5Fh8y6XBVt1Y7MwyXgpp1fVPlTJIg0Pn1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwD4hLSAdYO_B8l3SpSQOuraIpZiCN6DTaAOtjp7k7z7_j5kgJJgaaUCVgZ0h_z2Wrlqe8HHJCulvtKnQmHR9ZabhpUkfKuTRwRdq1nnTNyN9XMsUR8im5H0GLYJk74n3vakdTSGnPFHTSL8NU7aRl1n0Wk8-1V4AL-79uLkGTVP3Zb4hBqYTjLBdysheY69_xBIzwoPm6Vm6JAN0_aHZgRLb4qX-R_wgE0cM0gY2k2kF7spuBNvxFW9hwbzUnuuaUouGzDUUJpjKW1Yf6UwZx7FRz_3iNhabaVME1-xppaVHC4SnxniSXjKBg2ADs3Q5RuCJAUEkYOgxc5nQUfKbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=RAg54XXD3AgOKS8HEFcS9AwnnebCHfRg6H7Hf4XtOkbXdOy1Zl8zZdBKoHtkSIHUBiD8UWdEedXmEBF3IPiHIkSCf06qGMu3XwXrLWnA4PPPbsx3tN89VtKzDVY1LpBplNyLM2V4SNCbOY2cv7kA2ht5C9h7zcRJJggtUK0YzMl7q-L5FlYVdxp1DYR2XsvU1zUebxKzC5s-IKFiBSlGVD3HxSBcg_ZMWvt1Np9YbzfS0GnriILRo262xAe4N__7B8aCUi35F_RZQu_h1wZlPkj4vt-ai-JYJ1kO4iUz5YgyAroadhsbfjtw6dpBuFxWYwMXwATykTENol2fb-7_eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=RAg54XXD3AgOKS8HEFcS9AwnnebCHfRg6H7Hf4XtOkbXdOy1Zl8zZdBKoHtkSIHUBiD8UWdEedXmEBF3IPiHIkSCf06qGMu3XwXrLWnA4PPPbsx3tN89VtKzDVY1LpBplNyLM2V4SNCbOY2cv7kA2ht5C9h7zcRJJggtUK0YzMl7q-L5FlYVdxp1DYR2XsvU1zUebxKzC5s-IKFiBSlGVD3HxSBcg_ZMWvt1Np9YbzfS0GnriILRo262xAe4N__7B8aCUi35F_RZQu_h1wZlPkj4vt-ai-JYJ1kO4iUz5YgyAroadhsbfjtw6dpBuFxWYwMXwATykTENol2fb-7_eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtyKbS52SQgrE7UqNg1hRemuCXG5dDtHd7Tp2T0yXSsofpRj8cXQ8OMg0YJGdRFUp5__2fwSz603NCBgcp9HoRnJ5xoGuc8_99aKhiXHAdVv6juXgzoPPFvQBSGPvhpzGxTEUokAEIAlQPg89mUcMQPb0hUlw1vbKYk3NjIL99Hp559vYxbmGtuHnKIcOzE6gB3fVMPOGBVDWkbWKxRKYiXF87rUpt5m_gnRz8nVsvL_B4mlEoS2IrdyqXfIHGnKUvm02VX2nWoY-bBcjdarjJo4HKQGE9nl63e9nQvMruh2-IpOx5kGIj-NBDcypc0PzL8K2TV8bh1qrkCPPQjgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5h91ST3pc43bTWcKDJsgLS27kmTi9wbngZMRpE6P7u_72KfrVY7WjsfJL_CKGop4KmnIP6d3LGMNxUI3tsQZESmWnD5KnRXITCfRjq0Md_0IXHMRvMo3TSmA_8C86DmjZDALWsiybAUavRpWFe3NV2gMBy31Pzfdlw5sHq9k5Pvopg21FV2lfkJdi5Ao42BZjkS5Nb770_uvsID7b0o3fVXpw-SnoTIxKsii65d1gAYKLrNRM438chn9XzfnSfWYJ2tSgAoYD8JR9AtSNpHeCDmFeQ3KdRN5a-zD7r6okrajGx2F5CnuYYXRktgXH6v4r3jwx9AluWfbyWyHa4Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAEKMR-cY2AAFNyqdmItnlDw7W2WAMOuu191TTAg79ZHyVauj-l9K7DOVcWUZKcs9CFj65cUSPASbXCetBPDd4Bc1x2bnFLspj5LtZTT0GvJ-4i9ryp02IQVmE3hFi6Eo_J0MNLUTAg4QzMsiyUGmCZL8mfLIWAdBTnVYxOMlNl_NXDZwYJFcLs3Lr8QSvvoNn17Aynh35RlGXfRWGjU9Sxryjt0Lia8NTf3pZIBYl79cM8Kk0Te3T11VThVKge29lTpcgTSXHkbPcl01-DBTMVP4cXgW9XNf1hg5wWkF4OyZLICpWo1ZbypQupsF8NDaU5vFxTB5B_e9tqmthWqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHpOO5C7H83tHV4xCO3puQ7o4pFBeKBNUw4FiK0PUva-fcrqTqdSOASciWOUa0i6hpM6QhAICmTI8wx82lZ0_rSzq22F-d75yKiihK_V_hYaWjT-h-Ifn2WPsku-reuLd0OsSJwygoyuZg1Co53UokDn8yN118eGj3NEK7Q_8cn0xmHtP16Qms5DB5FRbuMoGjNna6VdHzc61vO-thBqYoZTVIdzLy6m2-xfZVjmr9mp_i0PD8I5Ey12KSlsWQALvGCSONBqzWG11-e2dQAk2MBhjmrPm1XtAu9MhRjKjHIDVNQkIAk2kT4zx2A-7gAriLw3LXtPxIzqCwMp588inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AH5xzw0SpzV0R6Sp0hHxiv1pv9VIM6BgaSBAzFQ71U8S984-lbclsXjqqQkRW2tE9K6PLYtWE6TL6Uhx8UR8B4j_FJJ8YLKM3gHB0WatMIwjssrfOW1xoxd5v0OIHThP0qD-82w6PfPa3MwecEsmlLEvTxgkDJYvbrSXGay5Q94EEKwOBScx2qaJhjJ1cjsbPVRiJWpDoqcZhoNjW4nfWbZ8txAuctI7SQwb6byU_lKn9qvR3yZgX7xpZEEOlc74fAVc4gRW3GitrfhsiBl3_fpzQs2ZCok2UIYyGPFl1F6r3Mp_mauFPY3XIuV1A2PjPk7bgcDW3v82-3ZFj84cYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOItZ8VNtR9-cyqZjhwjf6RW_hN5Pw3DPWmgMykZLaoyrLgCOJhWsP39dY6b2tEQobJxoJiAFrlcsO4nxm5MBUJe5Xy5D3v-WZQ7IX_UDiB4_T0rpEbZMZSsu_E30_GaZV23OlOVpHacSiOVkAsBzgkkbZVt7dlG0VnE_QJqQTe5cBT_lGtqZBBQUNjM_xodm94SiXtEzwB2DrNfOjIG-hppu06zit7X-TlO6m_b-1nFXO5FuFRay3fXhTXnSAXrIFsCTN-SHKwmFhUE6q7CeOC-0O3SzM2nFWnsc7Ie4Dq39Tsu4_zjhDpL9O051fdPK-2K7Fq0CYs6VwFk6CBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfG5Tn8A1zxsfTPYGFC8OEY9oD-cHHA3CEy_PjUhAu2YpicUSgKJoUuD7qXo-s1GqPL3h1lfaa651_vnO77RGehCZ5Cp_235Rz_Kd5nFjsYNQHudIUm-ORkL6S7HmJQ4LOA8JRRynp2UpcWOR_7FVhk14n9w7MfbH28pNWtnze-YmkFwpk-YDMjtPEdVBecwvXY30flS4XxieekaBFqhlzhgMBoU1Zlc6MolAkZ9dLjTrcyzEfu25bPoHzXKlSUYS9fLUa4wQshBzJSJR6GY2sHlNLyXGXOon2sNa2PoXIt_n_7734GNKsQ3fidgu7p8nABwnNV05C9ExJqyp2168Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vmu49SkWX6vMOJcu6ubwCXTJXSdzYYxNzIkkO5wyo1R88mvfQAWRLiYlXzkyDafcitMBVCtoFwH3AO0ELZZjpYQc7TP6hB9xFm8azDHy5pmtudZppUI3jLvqYvSjXYpIUcMElVjzpJzhIUj8suQiLG4vL4Km7FibSVpNFuAOoQjzzv_6gUhUs9Yamp5BHjZDDauGt2niBVZW-fM-HjbLQ_CsA9slYdcecf158xHoECZFw4OW72ufEt1iQH0JQgClzB0SHNzidHDpw6Rs9jA4RjAULKKWPCHQ2pPg42tXbaCuu9eN0BnLC-UXsQyyMnXdxeCbnjzvRL2-gQhG_BV7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR5T9C36LUYAuYM6UYPa-gKeuSFVoRsgD-SOYZZgNuGleJH168XpYuNnJh5Lg3mXGX4jmcuvZiktNGlrBDErMcqISrBDzUOMwXHC-a95qg69UiwsuAzg940n_6V_sFkTxpPUFmFnW4jpTzQNMHxlIVpBDkcXkT5Rkj2oMLKtjzCw9Hh8efXUtw6P3TRemyAgTlD7mqfqLLcQHuzO9OqNNWOrdtq5qdyLceyI_70ywxW9Rh5Ss3_wrvVWRNG6Ve6h_HfBDYQhEmiJ6Ai301mE-T6NmQ_TrHgoFiuH59lNznbL-zww2easNkz-FmVW20lRCrkZGtqjRztaLdcc2-0BVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMeLPJ9h5kDbwFeSovf05_w6OzYmKs20Jq3H-A17AMvyCtUBWeXZHwSMgZrxu7U6akZUKp3gS0_hTLgbVhR1TpF5QDFMnBQmpzs0aEks8mOnW_UPFl5_UDOyTe5G-L_BICJD9N7am6svdljY09hpFJWoxSfH2XJ20BOj7N99p6jBKqt2qYKH-SZHk65sRvTRMOy6TWaR6Cm56FJp7tM_LjwjmWfqIta3EnF4PpzT9DCzhFQF3NFhMMvtIFAC6MPN-iIZSkwnQ6W5iZtkC7Ac-Kt9vGQOuIf9doJSoIt-ByiXgyL-ufIT-RlQJEvLb9j_ax52hrlMzzqIuVzBDjxzSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keo7ZAGUeHtv3ZwiyQjY2Zv9883fsNOSkXJcq5DOvz_3nOzlJudFVWFsX76hMcJXyizpDt850d_5auYVaEi2iisQZ5Ve6vSn-AjyAndapuvXY5lTUFrJdFT7PgwYBHSw2Kat-CwalBkEPp2tTVU9Pgk4t7SYrO23Xgi7RZvxKB0vNDCp2Q9y6Sb8oPioHCcqVLbenIHSZT1j3EC1xsbfmcM2Jb9EBIp46W4meXzOnPxFcMPCb1nwmrN_J8klY0Ou_SJV2CJvPiFWlZsYWNpGFL-jR8uQ9BDH3GfjXVF8Xlw-9DflSAvMrpNeERJXTOEp9FQZ8-G7O5lAek3FpkZRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smIbyGPvqrAXQwzJyvCYV6msHsgbWtIRUrtrfmfe8MU14yRV1C3HPtDPYPUKJOj8guia6OhRknDIhW0v6MMzzty774abdezVleafMWlR2q9F8EWAF-HQY_jMl3eMpa64DEJED-Rw5aMhn93lv6cll-MqZRQrqjD56wU2nrzZAAf93DR7pO-YPhXBE8c0J0oLJmPxtrS_cpOawaJ5VKOSoFKycXrK4d6kT58yBnMndHp_NymfnDSC09maNNPZPHrHtJbmA9IDMEN5g7ylnJePSPZiUjr0W3SvptaBESgoSEmKbrPNXEAOZ1vbIJKNHB1YmNA02z-uY6i037SenITp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3nynYLbFOUF4BRQJh_E2PCiB-xkL-74Aojy5Ihmh-Ipp_HpKzr2mKM0CC3NC7-5ew8ypcw6gmWClSXhDB-2jitsoKqRMmm6vbiy0G2qMq3YPgjKQiyK8nh0W5-Pwp9nAErc6Eoh4Yy6hMNm3Pc_rU-q6gdbaxEZwqL0zFmoHVa1HDL2OChCTtg55rDz5fztIjzf67JG8wyQebz5JKnUMLY2w1-xezpNBrDcjmtwRvFZZAxGv0qP-Zr7Od8xl1-feIHq1TeRpxarHwi1dqu-QoS9quj2nXRhdfEd2xSVvAmlwlqyFwrVZ0dsH7cJfsvlbcPULMYpVnkDJDuJRZ1tjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIzS8RY5W2dDcMoofhi8TyRUA4W1QPEpPQx6Tun1FUnbhdLnBVTbj5xL-ZL8e-ElkoXUuh-ykHC2ejNeoUuvIBqyLcYhFXQ5Kk7Sl7m9Qx2Rz4kRi3e7aBJ2__wweVVdk8OyX8yKAxCVEFay2zhfccJ3ppMGs3ChKcVuj8sSAXUy_RTgSXt1_RdCqIngCwj5V10F3NjHaswwh_fyf2jCRxAbYQqmxBwKfyFrLnLowtHIHNrUy90vmmR7SOqYtKvoOL3ZWZTEX54Ucmd9CqxCepDBhauvwsn6DTl4LSX94rKT2NYvlNWgfLY0EnU01bT023DawabRVjB1W9wbHxmX8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBsLIkBp96F_tl0uzGOquSudgZAcm2m0VGyXDjewXqFoIJOHU2TtHFXt8CkcExWQZlvov6XoAqwo90pl5q0GCAODDZG9ULnkX6LQs3OYSAqjgEqsazXWI0q9uoo6-1vANYg0HJ3BMnWiIuDGIHckeqgbSAhlC5xGxrp38z0Vw3q1jct-za9MR_RCP6iE3i5adl5v2D12J8hJ97VvG7ZBJkcIHUkH2bE_ElJ9fx2hj8zgXtS7CFC7IhHFNsyKcj_cwtBmEpDaktbQDwWeJDrWSDE89_xrE_C4NiPKQ-i5UVjph3AtK60rM7GUGXgMBruEunw_viVBJVHaE3EmWtKEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WixnoiLjXsr1Ee537fMjBnFn2A2c620KnM9V5bkNh89QKkqQsU0Z7iB2Y3SANDyTt8JvZonb1Hl4C_9yOfPOBRIRk7Gpu6dBO7dBqVko9YEMA9eHWuKW3I5KxmbwUmqTC4BtDt4rHf4Q3M6A_MvhQIXl4L82K9FsEfyTbc8ruHM3TE27KhkBtRgsY6p_MpK9kntQNEGjC3bGdeu2htZvQq8gj5hQSwU1ZPwuhMXT_w08N_m4HwFrfGl5nwENo0-nVl9v8MHSQ9TKbuHh1IAQqd4T827f59NZyITJPP0YnPJsIY_uG7XDKq_5itOC453cDDzjsaVPiReuAD3tAjj1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzGkNs2sMjGT17U1osXQ8v7HYgHYaVptT5753VSmOkJJLRnY4un9beTJSY0Op0-gsWWROSyPuM8-jsrr1jU0MUJI4mkX028XMHfKoquiRtmgcUU75g2kYhJ93mxQWQfQc1YzGe0mRJg4m6ELvrrEUeTSB_RkvcCqa09WHvgYBJJ8T3oHVwhQjWRLH_uBZi0EetcK1C5e3dPAW8ay_xM1cIsfwgBXyUq9NXX535kSampLBBOZ0MhLpqwVh5K0m2J7PwVgwpvy_QUCnC8C6fign2gjIRSknP0mPI9jDnNgeUyzCMx2BIMU5ebH-4DP0NJEQRrcqwIvWYR1pIjYIM1p-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCUpUXf-puHRuXUN9AmWn3El7V8uFcKqU2cj_k4p4xHFJxjdUnMGlWsoMMEUR6X09c8TSOLdx9Et1YBvuCoeDHFNzNTN5UuqNk7kaakLofJ6j4F3NcBZFGbp6u8TRtfny84r2XNFY6Vn7J9kYq5UT8iZBzUbr55sgjCj5EH0c7W_l_EvHzfXOBT9e-EG5CvoqpTCs8cTth0-xSs40AcHEbaBWvxUO7_3TOlDR1pXZEkLc8GwRMj1NVr18U5jh5avJ5ECenDvb8M9e9xZm03jAtRET5LdBNrAsPcCoxrqUFLj-r1nk4N-ejYZkgLwpravw9bodINHKdtQ9ASKqYlhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWpTWIeGafsopY63sebkIKZKsBqzDVwHj9hqs-kZYJ0VFaik9Q9uqbVZkPv90Txfzu2s6QzSI2HkQad05oA23JbFIcaX0AsWNGvkdHX0jmdoGg4u9jX9b6UDK4sIzRE-rJ8Jfxtfj2KJ3W5qoXhLY9hcs8Ue5aHic645PDtoc-Yhv-O-n_p4bQFlASA8sSB5IRggB9JC2wtzrZ1h42zIWldCiuuu6Ty2sa_8Ne5K274OrcTwsgC9jot4DVBjI7zKGKGlPJgy83tvVvwac9u4Cdb6k3WMBjdXEwZXgX1CxXwVi3zVuukYAt_C0wjulH7-CaF93NiALnr2bw4ZFygwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH-oZtpmnr24ipfgICfzv-CXLcwg7t4rhg4acKLiBo5mxQqPe_Wcyj6gJEfxsT_WxU5BfLCRvTeVx4oxFOhnr0eRIR3L41BJbhfYkOTvOZ8ThBWfcFxE3qy5vRLaS8LAYYN6aCVctXoFukR8RLoZx9SXSrVkqDdx3k6B-LT6Ow4LN6YdWurI136GmtX7LOuGa3RKqPgFqS1D8ga1YVah6_kskcyZ78pcI6UWB3gwLex-e-3a76smKu1ZInTaHNvvKSmFxhFhFpIaLYp5lnmtrsWNIJHMbfJkGR1hieHhYsPWTjBDdwKy-p0YFaubKhehPc1oojaM_-QnZdURApSbTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=S2Bqgljxt3qCDuAp84U_Slc68CL77vq_grwjEaSs01PWxjL7eE-K8w0o1eU269HZnyGflzwyKYxpi13kZ0A0_wx3V5TWXKAGk8fjbeRcpLkOdAd0UTLvjmxiULgfJr5vu_UPJdAPrR7eaJp741ldC6eP_G6HLR6XXKrDernGotih2KDrj76YpFWrc_MPgN-FlBOKunZo4nNvXQk_mCUTehExNjWSDs061RnWuZzBr2cgL0Dzz2mI6DhimVkdt7JiVox2HzoBRaf8P-1BfttV2NWLXH0j9Z8bm0gElOL-7vNaK2y3LLKXqNmIv92FGo_h0DJtA3h5ZJr2olVB48GlEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=S2Bqgljxt3qCDuAp84U_Slc68CL77vq_grwjEaSs01PWxjL7eE-K8w0o1eU269HZnyGflzwyKYxpi13kZ0A0_wx3V5TWXKAGk8fjbeRcpLkOdAd0UTLvjmxiULgfJr5vu_UPJdAPrR7eaJp741ldC6eP_G6HLR6XXKrDernGotih2KDrj76YpFWrc_MPgN-FlBOKunZo4nNvXQk_mCUTehExNjWSDs061RnWuZzBr2cgL0Dzz2mI6DhimVkdt7JiVox2HzoBRaf8P-1BfttV2NWLXH0j9Z8bm0gElOL-7vNaK2y3LLKXqNmIv92FGo_h0DJtA3h5ZJr2olVB48GlEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0wQowUCs25_9Yuk-1v8vVxBWifYNFBuMNtymMCzaVr56sCCfe9XLx-GKPf9bXiO-pRNdNVhQkKe4-ycGLd9HHMBsKrU7UCA06XzLoq7hI3muN8r9IMjPizK1lDD442SoT8d7HIOVqRbhy7xpJZ546XkhWWK8F2VkaMas848fAe3kX7Fvb2rX2qtynN8bhvAi6JXE-WnLP_6lq0UADtecjx3KfIy09YmYLRWoIoQlST4wagBTVR5lSxir81JHz7QQBCmgkMU7nF4EtX_f1YX8MTOxGKjZkfnD_i4e8TeqUwxfOIxGosQ5c0xOv90ah42dV3WiU2EFOSt6LECNSwzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI1JMsqVPm0IxBPg8RQEEO8Pahpvhc-h3zclR2fM3WVRv2dAuFHZeJz8jF7UEk1cmE681OYzOd9Qh7JRcBTVO5AZnNtitUb8no-Y9vTxB7HFfWe5JX3Otv5x_ny3AjxJY6eUVktnD_34f3TcJhxyIVDNAEc6nr07H9Z7hdueKq0joQ3nLSrbiS94cWq6uHQe5txptjKDGfZthKP1irdEINN--NAxpVsYjqexIUhPs1vt8cbRx54wtz6lj7BxvhIUttN6vyJ4UmQkrPuiDi_J51ACCqNvgwJNMwoBoP8hFCnhVUv7RAJ6U6ZsQNdmy-wTA6Y0rEmSOzaZHF5mFnXkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY2RXgiKWlx5o5cXw3rmK8Vp5652OwEutAf6MZip0vnyvLCTuaxMjEPcQTTJp68Z3pZD0modO4QUIec79kD5-3GFXi1vyszgEOKmy6IStqMXhsbMxGuAZnrFK3iuV70_S0le_XDC7_EV6CgSf1wPLX3dU8J7mfJeZ4L3H8gRoCU5oEvB6HuQKZgk0VzzSqrKYxSma0MXknIg428WNWHWBDoVkkdWywQr2Tu-4pCPb9iXMzFd0o5aM4D_vLkreT7hETz7IBXK7i92l5bVUZnz_n7U2QYaxMA-2atzzPinEO-xXh_dcjQ5v3XnSK7EFjJEGDCPV9wQu2RDSujwAHPkLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dvg7Uu-aTw5lZ3JkHHHl6-wrqZp2Wd48a0cC7l96F25X3mrM4vPRzJoLjl9hCqj6O_Z9nTRlRMMtWQezWT4p3qTxzHGsL5P3x_wqlAH5Wx0VnuhLMbGFMxqG3xqt00IxMRz-UwtR2bn0HV33LWEhR-vjYpTWxJk2jotOOibprRfnQDor4fZxQTZnKa6rdRdyhwlS7Yrx06gNwtZHdqYUf5xP1sVnFwWAoKTg3OdjVchemiN4tZivSd_D29aB-z0I_WN7V9Yd0wa_8TyfOA8fk37r8kZbkhvTbqSrDMOI_ULKMXspD5UFEH1x1wcu1Owy3e2bYYf0IQMY6CJLOopWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPDmS_M1XF6ZAJqP-GnGWkuEoMkJWLvmL-RdVyaOfwTUcchWtJUFJA6OaHQlY0l2rUmfkZMm2LvuH55Ky6CP9hum7c3Es3CiqdyQtetzqZRB8SeaXA8EHzfNUIxzVEjeuUB3-9P43E_PzKRBw_0kiBisCBym5F2uUBGA9BkingzoZOsP-vcykon4-G10jZrKmJ0RF0S_nSujYO5kq9SOj6zd3c4zTjnBR2eWYfqvctsrbxz1_eirKBhPjUIkva6Dqs581X5_6Adu3rh0h6bu5TT-Tk6HUn7NFBCrFbO0Hx6BNCUYsUyChpeOaeRx0WJYhM3jUScHOvBLn7iJeXcdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHLcqoFmt5krZ_y_JGh7-zThbvxpoHP0gfiqmAcbRZYUzXR-acNvyxB3UIX4tJA_J9QIiSgcp41TOtP-jIO4lS1VBNdVwMgyJYFOtpO0PAWm1_Y8JLDVxA0vZ8WB49SnFiOQb-Cw1KXPT8lU8L2BO7h1pqBnHhv_Jj9xN1A2RWnFPC68TjktEePzSJqo3YBJH4DwzQfm7y2DDY2K0DtdHQ-l5IZ17mFLL100QhEjQls6C-vb0pcK3HMpaQthJHyRlmLHPHyUdx3tarlK87Ox2j4gxK2F6xtqJKZjBRYgWc9lTfIH89vub6Nr2wdR9bFUVuXP__n2MeqKIr05MBzZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8dxLq6_EVyNc6D4c6VwYx9VyBirCW2KKnH6pF6DyhaQdyG80UsoSoiDnbA6hCKpRh-OgCTc3aJcsXV6mMdW4nschH3J1WCVSISIe5st8Ol_5IfwWn0tyJBg9rgoH4nnz9FN5aRrNZmCb95fMjP0SvNZ3ahVslRJ66iY4bAPeBfiu-vY3Z5ORwPbUrNTPBYaM8T_uE3kDiN1ak4Jhtte59hcmQmjOcbpqYd3kqYAPWsUgkmKA0Qwh8I3FfgBto4wwCGaWrV_w0udZBSjJpeE1YyNzcH9RpCpRbqXl1-ESMZhDVSMB67vtNnSKmFcxhMeelUp258nM3gavFEX-neovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=o0ccDWCQ7eCyECc2XJ0rYk-40YapUuLmNq0Dx5nMmzkG5QDDMWQWbZkA-eYFsB3JvUGjRLnbrB3JZATlDpX6qicqorf_QvvLzyYLiPLQUqD3lwNALLjCbk2lXO3F36d1xJw8sgqZjq5El7HACXBZdiiPk1i_nAKdZZ1FtgHMemmjlvEPnDekjwli4-AtMpho1ixGuTUxZ3kBRH5Y_SYQIJwCWD7OERcdamVEx9S7WwJc83yq_Zmc51f9oOt4rXgtrfFXZygEYeYn2Hg3C-3a04hCpLEy0FUG_sKUqgVyDiRpeksFpnQqnierRTZrnEPozKCNP42qhSA55gjbcAvfRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=o0ccDWCQ7eCyECc2XJ0rYk-40YapUuLmNq0Dx5nMmzkG5QDDMWQWbZkA-eYFsB3JvUGjRLnbrB3JZATlDpX6qicqorf_QvvLzyYLiPLQUqD3lwNALLjCbk2lXO3F36d1xJw8sgqZjq5El7HACXBZdiiPk1i_nAKdZZ1FtgHMemmjlvEPnDekjwli4-AtMpho1ixGuTUxZ3kBRH5Y_SYQIJwCWD7OERcdamVEx9S7WwJc83yq_Zmc51f9oOt4rXgtrfFXZygEYeYn2Hg3C-3a04hCpLEy0FUG_sKUqgVyDiRpeksFpnQqnierRTZrnEPozKCNP42qhSA55gjbcAvfRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6kDQwgp14HhXAk9JCrIkX77ZsJ_IQe87Gb8YK65izlipH9Br6Fd9Z0V5fB2ZLE0iDNCXC-BXPeOjAZABlEacmSiuZ_InN_xRaj7kXY4QayoGJFenzWZL8QUBQlgLmp32xC5FD68HPljhv6PaWT7VnVtN01S3kvKex5lk8uy5Plj23TPavyxAE8xD9rihumaiKDrvHtQoz4X60oiIZfNLcUq-FRG3Blrc0e2YDVglQ_jZxpo1HAoJfT7s8R4KTitbznKhIX2sLz0XmVu4wsvbOs79fzueisKMSFQ_BlUdonCxCDAZx5mhORy9yYZBCxfcLcE6zp4fgPYlmAT6QOOUjPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6kDQwgp14HhXAk9JCrIkX77ZsJ_IQe87Gb8YK65izlipH9Br6Fd9Z0V5fB2ZLE0iDNCXC-BXPeOjAZABlEacmSiuZ_InN_xRaj7kXY4QayoGJFenzWZL8QUBQlgLmp32xC5FD68HPljhv6PaWT7VnVtN01S3kvKex5lk8uy5Plj23TPavyxAE8xD9rihumaiKDrvHtQoz4X60oiIZfNLcUq-FRG3Blrc0e2YDVglQ_jZxpo1HAoJfT7s8R4KTitbznKhIX2sLz0XmVu4wsvbOs79fzueisKMSFQ_BlUdonCxCDAZx5mhORy9yYZBCxfcLcE6zp4fgPYlmAT6QOOUjPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGX59ZV9VuC96aBvpuVlB6IyDdpxz498P6Yq5BVrw-hsFisnly1m2tzzD5EUT8pAKchKoOxao8RJjM24CUbvesJrnzV_udDRpXPEtQSOCRIbbyduOfelduDq0KsNvoSnGKVqAkR--XTMaklmseoPFFPBHLaycWWovbfMmmKb-W44Kxl8Ao6_Y2vwXmMDhizmcEkKn9A7mU10VMIXAZ9uyskoN_LdoiahQaFQ38E7ZtCUd4Sog1qg4yadM0W5emwpELSdc9DI10bAI7iRYH8pyjfVHVVIYFQN2P1KVacMPhhv0QVckzLXjWKJ1W5aehmBb0G3pjn1Gm0V98SdmP1Htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dV5neY2JIFuqeU63x3t-jFxkcCwR54g-MaGdrg87gdMAQ0T6SKDornBBWlbi1VUCVMt7TnVoGBxwgTvauv28SFztBsfDh3aeN7q2DQEYh3cPUWxtnsAGxsZ1wrOjGdbxLN8Xg1WqueH8hTH7GaAbHkzppgYh1NJuDvgZ7I_AdGBVvXzSXTRQA3nLsRZ5GE8EhIV08Tib8LCX6ZlYgWdVs3V5qT_bK1PX4pz4ifZL3ad8E9jiAtxQgh-Er0XvCzU1w7o7g-CdyzjeETSRzmn8VLIdqUSqVMGIbb1raqbhOVUqKnSLlu1PdlIZnOK3tZZW_WYyNp0y2OGCPy1XQ6TaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=bps7PqKKt9bCz1iPLRMzhgeq28czY8zQ5fL3Qc_UMG4NkQm-Xcz4Th16t3NeTwqMCpTY8tm5aU-yNlnqHPo9B4iSr8cdBKV8OxwjceHG99eoSJjXoXZE9VJEnhCDEtftbQZPtW0vRwK6nVWLTfYBgPnRhAg94BhiWGVez3vZD6-9L_V5wjRGStds-gYUfx1gGeSe9UEynxKt15-hI8Oia_UEl5MU8XlMB5w-Viyx6yj8zxOmswXK4XoxIrb2vz-bPlRwLqmZDq-y4EIPppw_kRDNJKbr7spVD7AsxvO4LmVX7n6m3KmSxnDfNMa4VBz__yGOFu4Nc4HgSD8fjgTHoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=bps7PqKKt9bCz1iPLRMzhgeq28czY8zQ5fL3Qc_UMG4NkQm-Xcz4Th16t3NeTwqMCpTY8tm5aU-yNlnqHPo9B4iSr8cdBKV8OxwjceHG99eoSJjXoXZE9VJEnhCDEtftbQZPtW0vRwK6nVWLTfYBgPnRhAg94BhiWGVez3vZD6-9L_V5wjRGStds-gYUfx1gGeSe9UEynxKt15-hI8Oia_UEl5MU8XlMB5w-Viyx6yj8zxOmswXK4XoxIrb2vz-bPlRwLqmZDq-y4EIPppw_kRDNJKbr7spVD7AsxvO4LmVX7n6m3KmSxnDfNMa4VBz__yGOFu4Nc4HgSD8fjgTHoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eL0rM4KYlxFtV0eMtfArnzINU9a3E4AFBMGXeb_IQlAgEQmW762XN8vjyt-OOcpkEdfItxMC3q6YXTllT5f69AgErTbXoccdTDeQAcMfkQpl61TzqGDrGhWq0WM8HylkQYfp4V33GT8eCp5KLTMDE78_lUZkq2ti6tSrfUDQFi7o2mpe08e7rTHwaJ79fMTvSIUGMh-e_ONUWt74CtkX1D4AbQIPTtBV34mOhg_ZWyGmqiKjmy450EbrmWqGvDoaaGX3Xs7jUBJ2oPp15CGkkSpVRM-HLqUVD05Kz2sCVfa8KRaxKl7wHr2GlkE2PAvDK72c_YFmB3m_876F0Oseyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDvkO-wZG5AUQPpEywbtILiwvpE9deSoIr_NEiB6mkus6hv8GZaeSbwk56Lp7jhfypJGU_IBQxgV7OuMpjLvvdhdDZjtRlbvuUlcHdvwuw5x06MCAkqhsUC8_La8j9Ea6nTRvQf5WrEPaJtmnu7uT2-tyP60DGhg-yWcN-3W6u5vi6MD9YHFUyZKjwvJJ1O5sSrEAKNWt8pQzVZFbemAF64JUzrqlOukCfyZosHK3JgEhqYTO7-n5l2N4GLZ7vB4KHJ6jAuF8zIISI6gtlV82ch9BS4cWGKtlWeuSbslTuivlQ8tOZeFPbqdauXApXmp718UbUxLDQ90v1RRnGL-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=ecShp6QsL5aYqvxaOAdxPhgQrcX310bB4x8FfKcik9HXIEiP57gSnFx__4mZG_tCWEK1eo1VpPGgkRrnnAwCOUY86FXb9O2nkBmAUIsEGVvDuti7gXdJ6OES9qojmU7sXS7p11FCQVUVh8Jgd_RIC4U2dnIdtuXjNZi5tXkKzyCmC22cLACzBVAp23YOvf7KrswT7lf2AX3aK9LzcpnztJaV3lCkSTV6B75bDmxSBhdVs7ZnFRRj7zch9RtFxEogD71vPExD9pab4f9HQWPHDT-oqsqarglnHSyi8sog1mDG91afi8iJgtw8o99AwEB91kNcZEW-A8dq0xtp4_Zl6K7kV6fZ5eggPjqCOZzpaxvbOy6Egw6Tov4geu5aV8nMIbaa6f6mHhn0zIr2s4EKnvGtAnGT5AV4JwQ9402K9_xZ1Guknnq5EPbflVT7drM4Foq1s2VcI5wY0vWNstmyq03mzm3qBlXmYAFbjhkrn-XGT6jrpVA63hYoxurjGpPVGoS-BtW_CmvJ9434-hVFYr5B2IiYN9UmED9QRVl4Az2ARP0Qaf5O-JcFj9m79-ZgKbXQlol5LHHz2DPr0aIUJOuvMrY7mqufQ68qvmHWIxC5KZb_UlBc_kw_ozufviQCFUXELKMYBldfEXd3Vf6o5eW4wDTi8ATSnS6PfPWil54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=ecShp6QsL5aYqvxaOAdxPhgQrcX310bB4x8FfKcik9HXIEiP57gSnFx__4mZG_tCWEK1eo1VpPGgkRrnnAwCOUY86FXb9O2nkBmAUIsEGVvDuti7gXdJ6OES9qojmU7sXS7p11FCQVUVh8Jgd_RIC4U2dnIdtuXjNZi5tXkKzyCmC22cLACzBVAp23YOvf7KrswT7lf2AX3aK9LzcpnztJaV3lCkSTV6B75bDmxSBhdVs7ZnFRRj7zch9RtFxEogD71vPExD9pab4f9HQWPHDT-oqsqarglnHSyi8sog1mDG91afi8iJgtw8o99AwEB91kNcZEW-A8dq0xtp4_Zl6K7kV6fZ5eggPjqCOZzpaxvbOy6Egw6Tov4geu5aV8nMIbaa6f6mHhn0zIr2s4EKnvGtAnGT5AV4JwQ9402K9_xZ1Guknnq5EPbflVT7drM4Foq1s2VcI5wY0vWNstmyq03mzm3qBlXmYAFbjhkrn-XGT6jrpVA63hYoxurjGpPVGoS-BtW_CmvJ9434-hVFYr5B2IiYN9UmED9QRVl4Az2ARP0Qaf5O-JcFj9m79-ZgKbXQlol5LHHz2DPr0aIUJOuvMrY7mqufQ68qvmHWIxC5KZb_UlBc_kw_ozufviQCFUXELKMYBldfEXd3Vf6o5eW4wDTi8ATSnS6PfPWil54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncZ3qkWMP0RG6u-tpFbS8qka0vj59TWo3dIyoqMJE1iTrN7ilFIjwBSnnRdfoGojBl-a9eHPb5exKba4J7snWIVZCqvMWelYRtUuhm6Vx8F6tRp_hqEe3IHeV3Yg4WT1goqR1ZfKUh5tFmLLop2YbqbfkErs8ECrGwb8X12pNePE_Ps_-SU140Wa2ePqmxaHVjbpn3KhhqkWuDkKmRptAjwfvr6kNJuLkNFIO733l4_wmMVDVTgg6Rrv0uv6bcxcUUqCMuOCnENyzoh15X1imlK8xvTpwxFr_NR2RcE92n113kDprYZrZg2CmL3ixQWPH4bBcBNYdWTtgpbtzM7OzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXuyTJLPzYfjYw_sTKCTCHcBWShBPGVmzi8lwqRNXhaGjuvuCGOJnKw4SCS9jL_GLqojSO6nkL-Msj_wTfyE9xOqOoUQcB2kOc0ZOPNNo9EL-hq3o8-nITU3rmHf4I6qWL4smHw_-CiWbCST1ViV8BXpuGiqwx2nrEv6Mgx_ZHKhqI3UOOFT4pncRmVsZXLzN3QuaYQqyV3o2E1lzFuugALMDFX1zTdNLlwYBCBphAoicbHbtAnwDkNQvVOMdo3SNUzcm31hQSZDpwn1EaGgjVIwzSeIEOWmoRMTTjKtLrtDSMVX3dYiZZsHFLPHuzq-jGyTRqZlDDhKzlU1L3HSjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY6IJTbA2NOEqu_OTvNqB4mKGtsvY1tVvCtmIizgAWjNXNCPrJrudp3EX6Wlgh7f_sPD3qzj0isahPyPFcNRClprn-WYr_W8wgpE8zKRZ1qo176Yx3uUTtNGpsvs7_E0CSqEn9XNg6weO6v3WX-hALYiThWhVU9babfcnLbggX2xpckpAaID0km60B2cx0i5s2BySvT6r872BHnHYvH7wOxna-89AcFsTvTc-xlthI7rlbgoirWkTXRIF-GhQ059JCLKkBw7QdoMOyYMSKs4BNZ27zr5wOojNHreHGYFl4Wi8M61SwkQXx8_SnghVTBl6oC0Eb6Bkw-T1mIlKXRe-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=X6bRtK4n-k4x0qVqpw2oia2T2suWd3W37sfetSoFcTUziB4WL2MnPxO-pZrnCq3DG9CRstpN3BIMxzdImVRfbfcOWaD7IEjIZGe2V8_aIL8XbT0-dTCr0wnKNSOxvY8yBb69pQtNtbWXJDLNJ8E1YyMoCmWqYb-yugl7PB___72r4nH3eXBMrZdTLJiBDo10-GKehvP4bHZBixaffIrUDzeBBEpllteUI7_pST0ZcUxKloG0IHrNT1frfx_G04Xoy7QKatvXP6ShzefwnK_SqDfMVtwTB-g4AdRWbcy_ll3T_6B0v8lL5Oe9d4tAuOsjM0_eQFihP0NHIpuCnGdDqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=X6bRtK4n-k4x0qVqpw2oia2T2suWd3W37sfetSoFcTUziB4WL2MnPxO-pZrnCq3DG9CRstpN3BIMxzdImVRfbfcOWaD7IEjIZGe2V8_aIL8XbT0-dTCr0wnKNSOxvY8yBb69pQtNtbWXJDLNJ8E1YyMoCmWqYb-yugl7PB___72r4nH3eXBMrZdTLJiBDo10-GKehvP4bHZBixaffIrUDzeBBEpllteUI7_pST0ZcUxKloG0IHrNT1frfx_G04Xoy7QKatvXP6ShzefwnK_SqDfMVtwTB-g4AdRWbcy_ll3T_6B0v8lL5Oe9d4tAuOsjM0_eQFihP0NHIpuCnGdDqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=uwz5FJUzlGQMfbX2JYQmgusxdLRefSFkEcWYLuPe7Oa8qVBYaks2T5JR1dky-c7sTZlHX8PZl6mLHUkLBEvGapbYJFSLGodqTK0kuvOVaNK1qg6RsIeeBtYNHLJ5eaVZfkakxbl8IbIUlwo5Ie0o5hqmUBE6dNHsCjBUaLcyf3xpUJvI78jqBbm8yAol72_kPoqJBfevQCzjFxNjomc21mFuigV8bFQbb63N3y7ipTMprPhy3D54uYpN_1-W2gulbjOMJuH7sLaE97fXLN7hwpdC_8CsS_y-vbHEHf05sxqXh_ucYnpu2n_QvrcukBuSWPpPR9bDEVrEeUfqdT3Avw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=uwz5FJUzlGQMfbX2JYQmgusxdLRefSFkEcWYLuPe7Oa8qVBYaks2T5JR1dky-c7sTZlHX8PZl6mLHUkLBEvGapbYJFSLGodqTK0kuvOVaNK1qg6RsIeeBtYNHLJ5eaVZfkakxbl8IbIUlwo5Ie0o5hqmUBE6dNHsCjBUaLcyf3xpUJvI78jqBbm8yAol72_kPoqJBfevQCzjFxNjomc21mFuigV8bFQbb63N3y7ipTMprPhy3D54uYpN_1-W2gulbjOMJuH7sLaE97fXLN7hwpdC_8CsS_y-vbHEHf05sxqXh_ucYnpu2n_QvrcukBuSWPpPR9bDEVrEeUfqdT3Avw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbS934_Aczkjli72ng8qTH3iy2f-HKubkB3lvOaMn0VgCRtCmby6wpMptL88TFy4MM6UEnKLcmeF0n8Ugzl6JhmnTlOUoZP0IdFN9CxANcjnuwzMTiOk79wAj2xOgIKaCjUnCnyKvR17FjAN89DHgZ-EkFV1Xzqz_RTPCS2Wtxp5ndvgYMkvQ52-WvvSaU2nvAN7e0hs0pxjse9JPMKgOO29zFMr6oTRzap4b1UQzgIAAAyWX7kJp6q8RUg7kzk_Btu6I0LUswVKP6KuAYVE-rUtuUkrmvmsh-564sHp_YTTdw5jNFZVbSR05RTP0Ndye0x5WicsjVYxcpdvTvte_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC-c6Myy-LTrmUIncwTGDTtNTQyRdA2CsvaxASiOgNTutccRTYLoLZ6LyZGtsaaJ_mWqXAHoe3B0uxLArPWy2gFkHX9mpSawQXAC18ZVMoRUEjq65D5Lbvz8vdmQ9utvC4C63mUmzUIRee9sRmkWkLx464it_I2RE89iT3R69UH5hPLsXMX-Llc7hJbxF3uJVNX3_U-WD3K3e62OrRJi5lfpZ3FiRdaoJzyEXqrDyCicabyO9sLxr1UZgYo9cZSzfdufWc_Hgi2kdNJy3ZxkxGfsKrDdGcz6_pk4mAe41S46wlvWDmDtYBxsrAB65DoIIK0C9o2wJP9LRpbhmQuSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=q0mSFllOhbSX-SJVjLr-LyBGWq6FWDqEOhUA-nLC9t2aMY-rsuxCbu4j2z83buRpwKQCz6_Uz8KmfEPn99w41P50As6iqPvVuekBMbMfsA-qKJhIm6WymCFGWwD7rUm9lhCq3xjiNP3jj9rFW1U-Wj3b22JOi5FADYwcjaQut5rpnaU8YqKnQjsz_t8OTsWb8PHBDT291d1ThOLi_0l0Cc9eqglFWiK3Z51Og6IbydUjU7nnS4pjslF7nJw966m6tPaW3FrX_-D2BS1wvcgmMtZmZ0779kGSAo22MoynW4XIWPASP07twhDEC9KA47CLWwyzgnzf5BD3wTXGVgR8nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=q0mSFllOhbSX-SJVjLr-LyBGWq6FWDqEOhUA-nLC9t2aMY-rsuxCbu4j2z83buRpwKQCz6_Uz8KmfEPn99w41P50As6iqPvVuekBMbMfsA-qKJhIm6WymCFGWwD7rUm9lhCq3xjiNP3jj9rFW1U-Wj3b22JOi5FADYwcjaQut5rpnaU8YqKnQjsz_t8OTsWb8PHBDT291d1ThOLi_0l0Cc9eqglFWiK3Z51Og6IbydUjU7nnS4pjslF7nJw966m6tPaW3FrX_-D2BS1wvcgmMtZmZ0779kGSAo22MoynW4XIWPASP07twhDEC9KA47CLWwyzgnzf5BD3wTXGVgR8nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpei7suogb4Lp-7JJs0hVC__5WmYjJSnbTDhx_8kc1HOOKmMf-rqAsMza1CPPvrPz0PN3yzzeJFHol4EyWSsmmJVGfXgNDvzfqP-scNQ6XIt1eEzUG6n1byKnttO3kb79wfIKxoLXPgHFK_6W7-VuhGmFy6YqRx6JwKwu9J3NjAAfVSWs5MO5g7AqeEAffNGOET1TzR56DBslDe64gji9NShyPiULducGTcFYIQ1xAE7zwSBCpToRzwdKUuo5X01XBKaFWMK_8k2hWHHGfm6_ASPe1RvtmpTGTYCSx1gCgwQj3Ta9RhcZSpKk88tNu7FbD7oSRvrrO5u5j27jsQK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsxiA_vHr0tpYKlaor2UQRzK_5-RnVhu7_qnCxr4VVspGxyaqzc_HGY-ASu2JOeH6vFgCqh_JvO2Qoh-MoKlcNW6OXlDZ_pBXjRSws-OAWxBnOQRvt5bjPhcR9xYmjGPR-2ZRGM2FUBLZQPxagib1VpyCBY7p9qr8W_vZBgVRyI2WsEAUk62dBa9mcvEcHY6l5kn4boEsJ4gvkQDQ4xSynjINdLbgSgzimXgdsYRTqKW2-8R1VyErqDwkRQg7on-U0wQMDtcX3sTexEYdjQWr28ofGSVqbskyHgRWNpBp9UqvBJc-c1iJZrGE6nGqJDgD7XHGffRUYJ3FNbvHC5f2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDDMdig6-bBZEM1hm9N0gx794_Sc_aoa2shGC5Vmm_SAJquCOFxuwrm3jUv2rjFqbCo4GGrMYb87k7vqRDkHqhZ5PIAsqb3Fr_tzlB8-GThaChMk3MlmZ069FeyvljCh8ECgVFlsQSc73dcuh7qJgWe8RrL5R3_A33qaKJOQBgeyZZzyjOTXcWCGG_uTy4MoeaETSTZBoIonMilsEsdM_GUx_Q4ik5uCoMhKBt9Go_7R1SMWQ56k6ocHDmpZD1y-m890aXY3wQKgBRs6QqwinGT0AgnD9D3-ZG4cjNrMrrJeQqH4k6HFJ0PA8btUJaXvjro16IxNHML_kADy1rhL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm8IPrJHdYeTu0y6ndi06GGGe2OB6MhWdHuopF5onVEsnPfhjogJszPbMq1PyuPJhAcTwHLr7Q3V9lOWBblxFysJTwSPEvrg0RBbRle_UTZ3lAqZz38eFuLq0H6luyi7OS3jAs4bH__huBzQmLk3zINrBnNccLfRS6y9RfB0GCjV9a6cixQXD2OXXsddN16RAIXeaDlvN6zFB54KUdEENpeWybQjzFBHtoO4QZAY9RhtuDdnUpcCkozSdZ-d-kBUJQEMKL7ph_2-Ss5YOTydaUPVBOuFrZG1u7ftnftw-06ezGOhX_WzVfNfU_JjOcdNgKNvoNCDuoeaAPpaMkGe0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J008Hmc1ObGjZZjWbYnqWuokeGQxO6V7NEW8V0WZsHiAgHk7UZveBIWxXNGJS3O_PvAkRy51AK9-be1P5KlxeUAYtcGNjhMll9MwWFAGmL3m90IbNhmKoKFfniH1-e-UdsUtmzWI8XcjR7kVJ9V632N7s9AsRBNPMEYTs5LcziU2UfyMbao47ps3mg6nyL54n_xnPUhmnTDUqC87sqhLfDVD7vvUS2Zgg55wCAJQBtCAd7B1dma2N-vqER6vqojOwJIQkvAQFN2DL0KwLmTHrCK4BgX5NZXo5sbtP7lvT3oOro6jk-NK9lOGewD1Jog_A4FBCoVz-0x7GTxpNi9alA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC7ebvC52ZcVDC1rrwiveJQioNUb1kdcJUKLlDFaiuMHxdZtfXs9NcFVm6mRjNz-SaZmtfKoIAkCMNLzptxgIHHmZfyvdguU51b8bdaftgUL3yTYuJ5K7V_E4xHx021NIq-zgcRk0F-yxdK5rPjKIQ55kVVCgmy_OFwoQAPCeIb54vfbYZqPVRnIvmAD-d7HUHmlhk2m97q6k7cQResqqlgZPiZVJspE_jIM6pcRi8HlV4o_rTrQ2hxEIFjca21Jx8EC5UDLQlBGxTjJ5YanZnonaGRIp1sg8kIdC6ebc9g2uyOJ28nI8dext613PS09C2cyvdfw7J0O4ztwZdglqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZpnE0UMptYEe9TKy2sVDBp7uorLqLYNmavpzpsSNnNYzAjM5do8XgYwRitO2ujawbSM5o80L8GGV8ZO_5m9Bnvtm3QPfJt2iNLcWVhTSYR1lBrfSy4Yjzvvslbnh2CljyOW-JUaVBQV8ABz0kF2PhLE3u2zNREegKGfYR4apC0nD5GY0DRNN9feY0TQpaed0uRjesLqtuoAxVsF3WHia-jqyB8UNI_kVTHm2ctCOIsQ8vSV47KumvufUSSRjXWx8dbdcDJnH_4oR9mSXnVq8Tvdlg2wjykMviXclZOWqmdxwln2GGhl8Ceyszd2e-flxY6CflkPCdcOfJC9kXG7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYxJlyoSsNOjcC5LdBE5C25rrb-JAX4YDjZL3h3RFXiq-LqIZGQC6OjORW5vt-0HNj9CNUyThp6WtSAxoi0lYkdozxuGRmH6DI2f5fieyp_L3zM0i4X5lrt9EWwRX9ax3ATAkrCQQYCor0P4882WjSPN0AoACHIOxg9va02imDbW0UpqBc2b9W4ft8buDUxdkRFc-WXUhca3WujPFfbTsn3R-CSimLEBft-MPoDAcGdwsKT2VAZpsD8SiFCLqhVaejY30PuZCOdNWNvG3CibgSrgp_jvD9uXu7GnfJnkJRuC1F6xxOROGyeD3biztClFprsdICAkW3Q0z4mnvJOpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKaov-sUUZoUCBAHckTvHOZVEt7T-fiIBsbsDXSlpzkL4f25QxRDsrJfz51LmynL0bW1Ag9ZWJ3i1uAtM_Lh7pnQ8NYSPqkDL8HllhIN2BbRNWQcndnnAu95YZ0cdxoFW3hDzVbTWcp6AQXmFPtSoIE6V5N7TX3heFqkJtFjRcTUtU6yIt3BawiVd9VjITYXOhN98vWkSats0iJknq7RQ_Otb5mYQS_I9ntzJ4G8ezcOS_afJ3YF2zEtUmk6o4DNXlYXYdaFQ6SYt1Jo63E9J8GLTYC1vq8tLmTSol3YAExK6VA-o8Z8PRGA763qyPnrqtRc_pV59-Fl28cfYuLu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmk1Co-16RvXdVmx0FwWm6cMqXCAeQ0yJbcuufuMQBvOcumyCzfbjbjRPQJq690jx0axlXr82UVOrnik33ID00_qhZtMnmIesytyYcDqkjSAZQaqSuI3Lsu_SubJmY930AhtOo9uLAt0MpinsTO1TWisUwU_8RJe6d46A-hT586n_fWIYg7ySTdgCdzBjKwgrh_QuQonkNZHES7ktiDXGvf2BLpIkhlcQp95KKATJtIvuexEegr6zRZjHLkphNXl0t6WWMbYLxuMIUYrH5qWzHysFHrFncGn5balqqlxs6jr_WwEwcF7u7nDcn3He0VpsDBIbwQLaF3r9eYZtwcnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6jy_Jc1jv8UuXkOr8AIDN9L4C4wmJpiS1n7W2jPcwNwzYDdMayCzNesIg4wT7jPCVwXxdcpZkl7CcSQ1uVjPCviS-AN0ElAoKS5LikFC92M4DHhwRRsWcLXH33qQk_qjkC_MjQ22E_3AvpmED7jeG3zTaN-qOlg8AtDA9N7Cu8yiXlbrQLbY9eeusU_yCy2Mu21LTqcEbnNzZgEDQXM7LCAEKEB7stBp647sgu5lX898r0UzUGAXDO9Eqp-62hJjCURJmgwObfd6medEm1dldxm8IMFWSKN4vnotjp1u1bldNIStHO9xeaoXMJg9G9HVuVQimcuGH3Qowfvr2DRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfpIxl8t6SvvsYEV3aqEmnXxeKBY6lC3PNGRUYhzdXB5Laquo_sF069nlLzdGhzRZvI_3kQhrJlRKa68TcK5zqCBZJInJS5Y-XKkbG2KER0MiOo6qoQm10fP1OaeeSdkke8UcIkcAsKrpMhFvN2mEwOK7JDfgINZ8tWQjHMNFybfNiBaW3uWEfyRfQsMEBhTcuWbPP72QbRgLDAtZmIGEAcavhXHu3CRZr8mi9-_O31lKFFkyuAd2m_e88B88BbVee9H_8MPf7UyR5Jhhy-LGRkpZQG54hLlTWjJcSUhhQ_iWRKoywOTt5fFrG9o3KC1di_IecW9LsIgJ0k7ayuJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QrUULrFQDyb_OsBq-LLwEmHKl4zzPQuuVhpOVgE5nebvhARIm_S_YmJj__jUIH2PvZfBDCLdb-sDDraIHCCxjicNYvfaiJbekM6uXmOAqIjklBEmo423QsPitW0AGOFccr8AizhlxHHY9fePUhwDNuCDe8KMjZAt-q88pHcvanNQbiMhtsnbZSGRUJ8GIHQfdPCL1cfUR--nyHj-5xXZjKn8heXSdYG_oykapTe8yT6GErRZ3xQ-p4TmMdepcwYc6SR0GpTG7rFl1QWXZpYD13kYITynkgAGcCodMzj3HxUo5PaPOFP2hmRGGb96X21DmIgecb_gT6iZAxFhOeaEEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pd_PLstdjTHcv_P2zrKs1519cvAaIQs2piethynh_SDLBzoTU_2CrTniYC8Ow-HcRTlefG8_qHW9f8uGKyhZMXem3Vaw-HPSvUgeEF76ylxa-4nRnNFq7FJYUx7d5BOtPc8uvBf-G4DD2gZfYCb4SLR34XsW9TzBjFPscZjlO4aY_G0n57gLRmdqICI4tCxJ4JDlNVyhwqjmxh9UCepS6wsWasoXCf7kAkXWZeRL-rE6i7a3XhOmuIfMzB8ggOJH-7BjnVje7RzJsArMm42q1YaFLCaimwfacIjmwPJkQwRSifxODwzEAwF34zD75bx_WgI69UfUt-aH6_E1Cs786Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcaSCRO6GYKLXNFtSgSm9-rSB2emzk5_GaTL8SA3Sw0xnh479MU-5GXGV5Gvrycw0c-KJ2eiC6yA3_YeB5X51s-nnFiVqrRY_5YRszQn7_jFxjhxdrJJMGbFfp3lR2PC5FeM6v2ksXIK8ItQJjJzgc9VhcKJ_6_pFad4QWcVVDxl8-BZbSrQfxyrThdLx5aNOa7atjgC3icMDTggcm-RseeL4HH2x_inGG2tLfv7iOD8vALPxR5o7lql8PMOxPwat90qkLIrOspLALpI4nKi2EKmrAFWtirXvTbhbj-wxvtpc65a07IDS24dNs-EcsUFjmGy03lhIwv4NruvCdItgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
