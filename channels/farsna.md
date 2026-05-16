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
<img src="https://cdn4.telesco.pe/file/OqEMc-0B_TqTU76iXe6lEFkpb9JMDhqk83F8EKJJ7lxvqFIAdr9Cq5NvMniWFNkpUlKgig61HnISHNpZpcArr9S62-FMGQGR3Z7o1hIc9twzrDgMU0Z6Xe3rCQCbcLyySCQU1Z5v3LDswpeSEG_Id46UkT0n8fVusbkHeGjExLcIc3XJfdHCkgyJaWRU2BwYPVKuqFyHrPNbiLhi5GM-cFUnvVuC7UztBBJjL7AjaC2yA9dNmHZuZqIP4kyyNYE1Z3Te66pM5GlzRWDC8TH5wlFgcFWvqqj4NXNSIpQpsPovNgNChDwN4OxHAXEMFMxmnKrGPBtMZUHwdo2fy5uIpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 15:13:52</div>
<hr>

<div class="tg-post" id="msg-435891">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17c3c0505.mp4?token=Wk_K3c9ruJz1tY6I7wV5euVcgpUvO2a95UlRMAXh8iieh08QMRK4XERRGkz9t-xYdi0dzOOwIFwTOcOBqafMF5GFcIfw8YjtOg8AJ8ah2Fw3WTddl6gNitek2ohLDCQQd0EDGqYxkAnVCfItbxLsNeszB62zP92aYMeyaYdBNgbOlKBnxFHupmED1ZUmFC1Devlbo-1lSbNTZ6_r0HtlrY2d0QteQsL5cTPBo0AnD6kzE9FugTtJpPbZRhpL8OQx5IcVOcn441unRRBEwvBDDcAMervdjtEh97C8pIniY34D9bDGjt85FyRQzcNTDEIeqEyssfeDOKV4FCVd8KVAcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17c3c0505.mp4?token=Wk_K3c9ruJz1tY6I7wV5euVcgpUvO2a95UlRMAXh8iieh08QMRK4XERRGkz9t-xYdi0dzOOwIFwTOcOBqafMF5GFcIfw8YjtOg8AJ8ah2Fw3WTddl6gNitek2ohLDCQQd0EDGqYxkAnVCfItbxLsNeszB62zP92aYMeyaYdBNgbOlKBnxFHupmED1ZUmFC1Devlbo-1lSbNTZ6_r0HtlrY2d0QteQsL5cTPBo0AnD6kzE9FugTtJpPbZRhpL8OQx5IcVOcn441unRRBEwvBDDcAMervdjtEh97C8pIniY34D9bDGjt85FyRQzcNTDEIeqEyssfeDOKV4FCVd8KVAcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور در دورهٔ اصلاحات: مدال افتخار موشکی‌شدن ایران را باید به سینهٔ رهبر شهید زد  @Farsna - Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/435891" target="_blank">📅 15:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435890">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIyymL9L8dfx4PdBZgArmR-AzwRqxBZoObn5CLsgXpAzfE5JKjbCQu7ziA6lqZUZavglIGSxutXwYad-2o2LY7ScGuxx9EZDeVz1DQJkbd49r1WueeOmNCcwi61iU2UdhrnHO6z3RbVvCkM-O0EJJP6OuBrqXY9Yz3xJniUBNTA7cHkURxtjbWxc09OkEGpI9lGgMQ2qVVVH584Suf2fPJ4Au-hPSp5gLKxIHSs15w-Vtw3VrEDXYmsGubIY5-MIJeLfqp3oOkHRnJ25ce0wj0mbsA6zKxgLyDMtoP9e5dRQiFQ-Z5AhF_nhEQnpjlOn1wPhoDiTjWLq2XyOmwAIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💠
جزئیات تسهیلات ویژه بانک صادرات ایران به کسب‌وکارهای آسیب‌دیده در جنگ رمضان
🔹
بانک صادرات ایران با هدف حمایت از تولید ملی و اشتغال کارگران، فرآیند پرداخت تسهیلات ویژه به کسب‌وکارها و بنگاه‌های اقتصادی آسیب‌دیده در جنگ رمضان را سرعت بخشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 642 · <a href="https://t.me/farsna/435890" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435889">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S66AEe88z8M89aai-FZE-FzhIFp95i52TXVXIp4YQqq_5s5ZSYwY5g1_zR4PfDqJ6CrIYcMQS1rWsidMg5zY4GnjDi3cwJt0KC-KII6LDozQ0b3VF6Ufw8QKO4GWsUop3iznnhd5F2RkeZybW55bqkPdalRqxvlRXbYKCAwoXYrjoNxjgTMsAUJV2UrrBdnP756b7qp-s57x7Pq07A5drOuxttxD6cEBizLwTPyhkQ9UZXpQbkfvjySJt3b68D_YAzLLy_d6oMjuIRX2ApLyNXnGSLsxoQC2m-Tn9BEBYaFlK5kHWhzFgVblhuLRtqwclxTyJ-DIe3vcf1pPV98zCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مس دوباره از ۱۴هزار دلار گذشت؛
🔰
بازار جهانی در تنگنای عرضه
🔻
قیمت جهانی مس در معاملات اخیر بیش از ۲درصد افزایش یافت و برای دومین‌بار در سال جاری از مرز ۱۴هزار دلار در هر تن عبور کرد؛ رخدادی که از نگاه تحلیلگران، نشانه‌ای روشن از فشرده‌تر شدن توازن بازار جهانی این فلز راهبردی است.
🔸
مس که اوایل سال جاری رکورد تاریخی ۱۴هزار و ۵۰۰ دلار در هر تن را ثبت کرده بود، اکنون از ابتدای سال حدود ۹.۳ درصد بازدهی داشته و بار دیگر به بالاترین سطح پایانی تاریخ نزدیک شده است.
🔸
تحلیلگران، جهش اخیر قیمت را حاصل هم‌زمانی ریسک‌های فزاینده در سمت عرضه و تقویت چشم‌انداز تقاضای بلندمدت می‌دانند.
ادامه خبر در مس‌پرس
👇
https://mespress.ir/x6QK
@mespress_ir</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/farsna/435889" target="_blank">📅 15:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435888">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/farsna/435888" target="_blank">📅 15:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435887">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c0659d89.mp4?token=pwiaWSzC88m3dxIsA8wDseujbwyJjWAWEtU1XFIyCkyR6BJBSN1rKWcz4KXAgLYB2UsFJLInAiVqGwvFsQQdURAFC6BoFUv5Vo6Ll-KZvkjLc5UVa-J0cLXBCuAhUL7RPl3hP0fJNnqnSKEQj0ijx97dny4E31j9QDCiAjsVF202o__TPxRfTsfA96VISyHJJgAWhocwr5lInVVtVtsMnc2Gt2hAJBsC2UMTrFwxofzZ9v12EHkNtRbNqXOdLo9QiJGBeVD3FrOyW-HmQAxt-Wo9BuX7wCichStDKyR5griAU2j4VVoDrElQvcurDaprB-8V_p4G5pE2BeBhgPZRFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c0659d89.mp4?token=pwiaWSzC88m3dxIsA8wDseujbwyJjWAWEtU1XFIyCkyR6BJBSN1rKWcz4KXAgLYB2UsFJLInAiVqGwvFsQQdURAFC6BoFUv5Vo6Ll-KZvkjLc5UVa-J0cLXBCuAhUL7RPl3hP0fJNnqnSKEQj0ijx97dny4E31j9QDCiAjsVF202o__TPxRfTsfA96VISyHJJgAWhocwr5lInVVtVtsMnc2Gt2hAJBsC2UMTrFwxofzZ9v12EHkNtRbNqXOdLo9QiJGBeVD3FrOyW-HmQAxt-Wo9BuX7wCichStDKyR5griAU2j4VVoDrElQvcurDaprB-8V_p4G5pE2BeBhgPZRFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف نفتکش متخلف در تنگه هرمز
🔹
محمولۀ ۴۵۰ هزار بشکه‌ای نفتکش متخلف به مخازن ساحلی استان هرمزگان بازگردانده شد.
@Farsna</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/farsna/435887" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435886">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31b828f779.mp4?token=rg-LuKHADfElrppUtSCc_TOxPRTbrG4qAqydZrHjN-VjQlLZUGlFdMjaN2rd7RrdQH7Q8dKThX3kqfGmjNB3YElY9COQr1YhZJWhhgG4cTdisomqwR2XZqP7008nbhjFS45HDn2o5cavw4q4eIvRg-YZGflneLlu_JZWRb6u4ceT8rRh-A-XsnjYuHuq8FrKMaP0XNw3lt13xw0W9SNB_oYHOnDpZKudr_j4eQt7DT_a6G3HuI76qM-UvbAc-ZqRiJ5HBfJZzB629CzwgVRI54KbCyn5Q-UZDioSCQb9GU17IwOqCCksl_xf3aYSrG91otpnK2leJbsV_5lauW0Hbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31b828f779.mp4?token=rg-LuKHADfElrppUtSCc_TOxPRTbrG4qAqydZrHjN-VjQlLZUGlFdMjaN2rd7RrdQH7Q8dKThX3kqfGmjNB3YElY9COQr1YhZJWhhgG4cTdisomqwR2XZqP7008nbhjFS45HDn2o5cavw4q4eIvRg-YZGflneLlu_JZWRb6u4ceT8rRh-A-XsnjYuHuq8FrKMaP0XNw3lt13xw0W9SNB_oYHOnDpZKudr_j4eQt7DT_a6G3HuI76qM-UvbAc-ZqRiJ5HBfJZzB629CzwgVRI54KbCyn5Q-UZDioSCQb9GU17IwOqCCksl_xf3aYSrG91otpnK2leJbsV_5lauW0Hbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین خبرها از تنگه هرمز
🔹
پس از گذشت کشتی‌هایی از کشورهای شرق آسیا و به‌ویژه چین، ژاپن و پاکستان امروز خبر آمد که اروپایی‌ها هم وارد مذاکره با نیروی دریایی سپاه شده‌اند.
🔹
نظم ایرانی در تنگه هرمز هم در مبادی ورودی از جنوب جزیره هرمز تا مبدا خروجی در جنوب جزیره لارک همچنان پابرجاست.
@Farsna</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/435886" target="_blank">📅 14:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABb9s_vTfuHu6R1yt2oY0H4iFAOeUimzjerK0JLQKr0Yxqnkq4wPeNVwA0sFkJOp7Jp4kc3cxaVxVhX7zNuBBCcyF9wznczkJXZu84ZLRtcs67iTuL9yviIlVN3BdilHssNrtENVBaj9HSsgr_0wP4BK1HBpjVuJxO33PT6TdkQC2npxcy_4TQgD3cnsGWqR_sVvY8kVdoeL1hKAqaE2o5Cv_M6d8hAG8ujWNpsOcHS8wtPgFDU4sHtUdHFG1_nYgsOUXjiv0GCxTmHTwhmMk3NMQ_lC4dPR_v98JVEgSq2EOhxxZJC04DgsRFxdCXYgF1TKxuRC47HqJJ-jt-LTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مشاور رهبر انقلاب: این خویشتنداری همیشگی نیست
🔹
ایران سال‌ها به چشم دوست و برادر به آنها نگاه کرد ولی آنها با پیش فروش استقلال خود، حتی خاک و خانه‌هایشان را در اختیار دشمنان فلسطین و ایران قرار دادند.
🔹
پاسخ جمهوری اسلامی به سنگرهای استیجاری سنتکام در جنگ اخیر تمام عیار نبود؛ اما قطعا این خویشتنداری همیشگی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/435885" target="_blank">📅 14:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQrUSVddRLvMzpm0h6WbeRR1xm5WqIGX4FzNrIGT2q4oTij7voAJh8PA1G25lweykGc9AVNVNGTeW51IRi45pyv5n7w3acpgcsw6T-hkqyM_-SY2699yJFWPq2M2BVaJcmWk4jJZ45CGfOucbHU0ldAnVu2ZoTg3NRuwatn1Y378PPO8-cQgH9yAoJbdQrhYq1dCiv8uoOtEJayDQHD8wVM0fppEWuB5okR2jMfEBKw6hKEtGfe_cm079M7wAK1V_ufWdQiMvOHVXTRYYLeeNhEU05U_lsmLGB7D3XaiIfrT61P4LTxqlbPrGfH9SDCuqu3VMskjQZMrIEkjIyi1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت‌ملی مجلس: فقط کشتی‌های طرف همکاری با ایران حق عبور از تنگهٔ هرمز دارند
🔹
ایران در چارچوب حق حاکمیت ملی و تضمین امنیت تجارت بین‌الملل، سازوکاری حرفه‌ای برای مدیریت ترافیک تنگهٔ هرمز در مسیر تعیین‌شده تهیه کرده که به‌زودی رونمایی می‌شود.
🔹
در این فرآیند، فقط کشتی‌های تجاری و طرف‌های همکاری با ایران از آن بهره‌مند خواهند شد. حقوق لازم در ازایِ خدمات تخصصی ارائه شده، با این سازوکار برای ایران اخذ می‌شود.
🔹
این مسیر کماکان برای عاملین پروژهٔ به اصطلاح آزادی بسته خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/435884" target="_blank">📅 14:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435877">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYVHWixb6PK2D5tj9GpGE6gLVVemjTfFl7CQKHCLL5FUcA35pU-GwmaQs6bY797Fc2VhYrWMPFiQi6aRqvB2K7eGwluNzACWpNFpaKTN2WXGYQ-w5x-zknZtxdHSjzno_pzJKNV2f1YP5Z6cFSi_5t5mEgTPeJRY3FnrEOtGAVSzmYECnLFBbpctL9Yd3XzTAvZg0W_8o6XmWT0VqXeAvQqmTAdrq5HCVZyrJWEDw25r5BJD2bds3Sb0YnYy6f0MYFzO1kJbVowDX60rmacZO233xsPQ-EWJ1Ea1nwtcerPwcyaaH-ja7QCHuYT01OMoR5TvocmiUlviJMOrluSGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVJSl79NZJS1Rl4GuQ5wzR6PJo_3bS5oZZbJZ2B02Rx7cM6NlND-7Nfn3RTSeTydWvJXP01-wwY-_oinZbVoGZsthhpcCcLUMcLG6Nnn2BnynZ7jB5Mar2hrZZKqk0ZacX4yJ_5377xUhI02UCaN-P8rEkepktg4V0FyxGeeAppjRNIz-1fviOj_B6lmbG0jvtlkf1g0w-fxy1PfyjJsaQkfdeiMoGmZfDt2bnu9aL9uE5xTxSlqX7o40-j1DP_qa5PsDXk6NK9HxzR8_LAShZzJOqre5PauqKz0Zc_hOeeF04Cly8IKBuIi97Whox8V3gm3zD3m5XBgZZoaAtQdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hLgjFIvO_wNvpB83bHJPC7TmzuvJBEhB7jkHK7kb3NMQo-bSDKovL_onj8BBIywZenkq6pZ-IFnlo0EXM9uSMRRSjUCRu6oqbBdXGLBgZjggEjDVTwlacBR7pcfrklztoXqlllQ5F5vQD4xAq1P2Sw3ZQp1y8I2UTX0-XAZNmHcERRyplnDfEVzHPslHBBStHXegVKZ2pUambJEpWi4Sq_p8NpMriS6eEOjIeMmTpIdshx9IF_bXqZwMvJgSsjsFACNLqqksdZpUMxPuDOEeL7ZI1A53x6Uhigqd52dLudPpDEGhz1PxiVQkmJEuz1FUIN8kfAWMDEHE8D-3elNRrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0JHpTciA4j2qVaKrENReT6g0EyR_TL8NQY_bTi1brIKwaTOgrQSxHq6Nz8TN1cg7tHsJjUfRMtW_yzEty6mMOf2A42a23v8RY7U7m5ZtNezaslUDX9S4bF1G4MmUzJs6Vd_O0QfGvBo9oaCzoqZrD7ls6aW1_livDgKVTmmSs7hFyA46Qwju-LLFbLvIYSzxraK9Sh8rjLwkkdHu47DoS2VFk7cpfRW83l4tabZ1Ht6JY100bWVg4c7ThrXSlf0t9wXqegbL0RecvuW3athMdcdv41U4mOqJN2N8aoP59I2XI_2GmumAeWj5M1aHC2cBDoo80qf4LlqKHycm6fGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNaCJjCYyl7_XaNZ7PCyGXx5Z-Noxtj5ZyrjDpFwb9QZJ18z7_rhcHFSCLRIohva-m8cNxUzCjjnuYwZmaLkQK1TwK0rn2NA69f6_LxypHUiY4XDSGqIpsfg9AaUG1rH7agl5e9mQmxpUDBCXzleI5CcKTfuA2zWIhAg_XU_GPXP6_8OnhDRdGEnHaiGSQ_Q0hXA9VanHrMVV5Qr4fpUh17aIwVVpjyZKbuj97M7R7fm_qxBH9eWHpec_2Q4ImQ3BybKY6BbjCcawSwcXbew38AMzOu9aUx-yqSl5nRPThwqpE6booH8pusQPoaoSflUwzeMqEz0qd-igarn02z4KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfQGAQJ1V4wz1WEcCi7JKyErbKDC3oznXk5m5SC0LrfVY1w-XRnMFTFfaf7g7Hx5ZmQBOjm1MNaqtNp4YqXCWu17A4zKJAZ-56dPaCndMhRffkatkgFZ7TOoxPlbahJBK3oM-jxqS2jqPTW1A0yi2HLMueckcPcPYGW7B3TsrSxEt41ySqN-plLfGSwZ-G2SD3HP8DMG5kBrYSwdGrdu3J21nSlAGc63AoPAYSItI_X9PRI1bLm7XzpHGSMGg7YzS8qbNbDKmkP7OO4fiS1qTWX7b7-RqiUuuCwlCJKo2NX4710ICMw-5PGvHg3JyfW8-pAWlsnkOuFQOPaPJ-h2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYkYr-NWO8Tf-rZWMupC67YypKPkIMIb6Zy74IitfFMVoaMc__-1MBjWBaQ3whqU0s6qSXmph5doyu39qhoRHfS7wSS5mi1hHP4G-6pVhVxEP_5KIsWfzYefuueKex7Sjxzr4nvR0WckJQXorrURtuaiSzeWO3cgbHo5xtBWNULF1HbjCabxbH9vbX6lz3OoT-V7J3n89oW0t_N14Cb-wLkquECM2R9n-kxgRw84q2stMdmpl4SXjY-IHYnDSy41LM4eys9GnIm8bY2zEZuExddKcVT5A_X_ilU3MolzyD414GZPbB7mfr1c-WAUgVwAidb0_ekhaTC-Ti9UprkdnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سیاه‌پوشی حرم امیرالمومنین(ع) در آستانهٔ شهادت حضرت جوادالائمه(ع)
@Farsna</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/farsna/435877" target="_blank">📅 14:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435876">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در شیراز
به‌مدت ۳ روز
🔹
روابط‌عمومی ارتش فارس: عملیات خنثی‌سازی ‌بمب‌های عمل‌نکرده از حملات اخیر در شهر شیراز از امروز تا ساعت ۱۴ به‌مدت ۳ روز انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/farsna/435876" target="_blank">📅 13:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435875">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdRcLurr78cVtVPZVj_l_dsHpIsy4W2LWzJxZkfJ_yHHc9f_Qj2gxOz7AcsGlmBld6ZYwA4tfQO7XCakWraSDbKJ1cgu1I6iRV0puFocv4Mm4E5Q7RTjDiCTfox_vtBBLB9MrnlaTiJFVR82UXSRVFPjwpzo8upIAFyaRXqWp0cRBDQMEBqzfwx5znT8Jp6v098giqj2B54TQpDTSZY2acLnig8A774iLEhpJmfAnGBslRxKnABlN_8yj8ryexZMczc444LeGTugtlhFONxR75lZ7TAekk9W1MV89jVZ1qMa0jmhZN6Ls57D39biEHmunrnOKh5BCWDYdPmRs5qWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌های بزرگ روسیه وارد همکاری مالی با ایران شدند
🔹
پیمان‌پاک، رئیس اسبق سازمان توسعهٔ تجارت ایران: برخی از بانک‌های بزرگ روسیه از جمله اسبربانک و وی‌تی‌بی‌بانک که هر یک دارای دارایی‌هایی در حدود ۴۰۰ تا ۵۰۰ میلیارد دلار هستند، با بانک مرکزی ایران و بانک‌های عامل کشور حساب‌های کارگزاری فعال ایجاد کرده‌اند.
🔹
این بانک‌ها از نظر حجم دارایی تقریباً ۲ برابر مجموع دارایی بانک‌های ایران منابع مالی در اختیار دارند و همین موضوع ظرفیت قابل‌توجهی برای توسعهٔ مبادلات مالی فراهم کرده است.
🔹
اتصال سامانهٔ مالی ایران «سپام» به شبکهٔ روسی SPFS باعث شده انتقال ارز تجار از چند ماه به حدود ۴۸ ساعت کاهش یابد و حجم مبادلات ارزی رشد شدیدی پیدا کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/435875" target="_blank">📅 13:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m72PdbE82vtuDTDAxaZgz2ifDzqqgnmL8cnCGAW-2JYa4w1uZDV_7cU-HG7azhuFSQinuzyGubTQ6CrhXRKQVlkTBY3h5Ew6zzauyZC3pqDufu3juZgOcLjndo9EwyOOw5CtFKeZeTxvGTbb_F9RzhtoSRpjCJMuRJF1hVt_qy1LOVrBlQxp_2drkB9yqB0TC_KG4eYiYBhzqBMHgGO1-D5fgzcLf9sgQjncH49J0ST4RPTUDjMOxNbgR0dk3g-zFBVaNBgjBPy84DKAcTQQ2pDqpNMT_NIcaWdTAu_3237E1uiaN-SDifck8ADkPFNE7qUNSt9lHcNPjU5Z5_tkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاتک ایران به محاصرهٔ آمریکا با مهرهٔ چینی
🔹
یک نفتکش غول‌پیکر چینی که از تنگهٔ هرمز عبور کرده بود، خارج از خط محاصرهٔ آمریکا رویت شد.
🔹
این نفتکش پیش از آغاز مذاکرات رئیس‌جمهور چین و ترامپ درحال عبور از مسیر تعیین‌شدهٔ ایران در تنگهٔ هرمز در کنار جزیرهٔ لارک دیده شده بود.
🔹
حالا پایش داده‌های ماهواره‌ای نشان می‌دهد که نفتکش «یوان هوا هو» از خط محاصرهٔ آمریکا رد شده و آخرین سیگنالی که ارسال کرده است به روز پنج‌شنبه بازمی‌گردد؛ یعنی زمانی‌که ترامپ در پکن حضور داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/435874" target="_blank">📅 13:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435873">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU7GznrVP4Ac3WkBY8cD5PbDAkpIPlHpusB1cYD5v2G041Cp7x45HEIaCujdbOmHLBTJwGd-Pil_6jIFSDzuu2bhzVMuSTSdY525iRnUCI1Zm1GC63_V6tOOX2G9gM2W7ggG1R9AgV6V_WQMUqVgtX8AKXq5GBhWxRRYTKWyh7lT-YVF-09JkK8hR4zEp0q9ii1A5PoFTRYkLRVd65BfLWyQ7McIWCbolYij7vHajgWmA5MVnoNMkhzizLUzB0rYqm-JJLySbe1kOmJFF2T1qOnjiJu7iQ0jvCGOG0G8SboHz4SkgDeGdmc-gHYopJmKEItmogDIyc_kYGrcXGybTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ، تجارت ایران و عمان را ۲.۵ برابر کرد
🔹
باجلان، فعال اقتصادی ایرانی ساکن عمان: حجم مبادلات تجاری ایران بعد از جنگ رشد بسیار زیادی پیدا کرد؛ به‌طوری که در این مدت از ۲ میلیارد دلار به ۵ میلیارد دلار رسیده است.
🔹
بعد از جنگ با حرکت خوبی که در بحث مدیریت تنگهٔ هرمز اتفاق افتاد، حجم بسیار سنگینی از کالاها از سراسر جهان وارد اسکلهٔ سلطان قابوس، بندر سویق و بندر صحار شد.
🔹
عمانی‌ها نسبت به ایرانی‌ها احترام بسیار زیادی قائل هستند و مفتیان عمان در زمان جنگ به‌نفع ایران اعلام جبهه کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/435873" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435872">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P583t9P1AHP4fkOeyfudQV8DnenTu_mSiQvyTaQ_XcQq_gDOxjmkxftOdOsYFVgYmd8809IsO86qsT-qGEoRk596qievSZA68Loji-CKhW1ruMy-QGQ1Fa3igqP-M81V8Bx4YFZkhGO4YTHtdTPHtivzb-ILMxHdQsao9P1Q56woyI4ym_FKD82nh3qgE0t3NlJ1tpLWRPvYR51X9zGwV9l88ZypSadpOLLWYBrMv8jK1CsgnkuZRAU-EexZZJpcmc1ZwW5ALKdA3WSQnILr962aId9l1XZVJqbXxNAQJDv5_aJq6PctHEkpWPFXFJJxajErCL3jIQ9zEs0hsnkR9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ ماموریت ویژۀ رئیس‌جمهور به معاون اول در سِمت جدید
🔹
پزشکیان نظر به ضرورت فوری استقرار حکمرانی یکپارچه، منسجم و کارآمد در فضای مجازی عارف را با حفظ سمت به‌عنوان رئیس ستاد ویژه ساماندهی و راهبری فضای مجازی کشور منصوب کرد.
🔹
رئیس‌جمهور همچنین «تدوین و اجرای…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/435872" target="_blank">📅 13:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435871">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2006914dc.mp4?token=tfBhvczb42ksOa-1het9-29dBraURBvKWWMIffDLqb8o0xo3nHONuTZiBpPGyTM30A6vukEVFh0NfRN2NtHKj4PzBpXQ_2x3Y7zX4GH9acYanUGXpGHt3_32LDuBfQTyDtU3k_20RZqGpnHeMuo4jZyqhBYUJ2eLncJKvOtqYnbn51SyKhPqujUTB4vdBs3QY1MgYGFlogLBjKFXmP9lEVfQpC-EHSgasTK64erGVF-xGUFtcSXJlwijiQn8hXTyiBFhLBGCHHDmzbMdJiIWt-E5aWvYuuizN4u4H10Oon9ccZbIdWQXijfW_J8LPiXgjl4w5dNau7s5XL8sieOavA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2006914dc.mp4?token=tfBhvczb42ksOa-1het9-29dBraURBvKWWMIffDLqb8o0xo3nHONuTZiBpPGyTM30A6vukEVFh0NfRN2NtHKj4PzBpXQ_2x3Y7zX4GH9acYanUGXpGHt3_32LDuBfQTyDtU3k_20RZqGpnHeMuo4jZyqhBYUJ2eLncJKvOtqYnbn51SyKhPqujUTB4vdBs3QY1MgYGFlogLBjKFXmP9lEVfQpC-EHSgasTK64erGVF-xGUFtcSXJlwijiQn8hXTyiBFhLBGCHHDmzbMdJiIWt-E5aWvYuuizN4u4H10Oon9ccZbIdWQXijfW_J8LPiXgjl4w5dNau7s5XL8sieOavA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجاهد: شهید حاجی‌زاده، دورۀ مدیریت شهید رئیسی را نقطه عطف پیشرفت‌های فضایی کشور می‌دانست
🔹
معاون پیگیری‌های ویژۀ دفتر دولت شهید رئیسی ادامه داد: گمان من این بود که اگر دولت شهید رئیسی ادامه پیدا می‌کرد، بسیاری از مشکلات کشور و مسائل ما حل می‌شد.  @Farsna…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/435871" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435870">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b62ce881c.mp4?token=uymyT4vkuPb8tbWkrT9JbsCG11qqWfxIUEo-8xjlJKI3dy3VM__MqJA7VgBDyTsRFiL6jnSMtLGqvm2KcR-u6g_mwmnmQkmcAcychvX3y6b26pYzhvcqUMsgbQ_UUMHYDSdqegaSvoO86wR4Ee97fY-7fj_McpKTCTFMfR7ku-4uZp8He_jWuv-5lnICu_LEqRoBuz_l7665X1kMtOOBJkHsleIHZ-vmf4Xm__3DcWQ_ZBpzlADPe4wULPV3ilV0tUr7n-Z4c1b8A2HLGTitMKG4oaQIQBdsCSoKUAKlVg0F9HFBJCVlOfY52joDK3d-xzqT8wcFGoX4FUcxndqGaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b62ce881c.mp4?token=uymyT4vkuPb8tbWkrT9JbsCG11qqWfxIUEo-8xjlJKI3dy3VM__MqJA7VgBDyTsRFiL6jnSMtLGqvm2KcR-u6g_mwmnmQkmcAcychvX3y6b26pYzhvcqUMsgbQ_UUMHYDSdqegaSvoO86wR4Ee97fY-7fj_McpKTCTFMfR7ku-4uZp8He_jWuv-5lnICu_LEqRoBuz_l7665X1kMtOOBJkHsleIHZ-vmf4Xm__3DcWQ_ZBpzlADPe4wULPV3ilV0tUr7n-Z4c1b8A2HLGTitMKG4oaQIQBdsCSoKUAKlVg0F9HFBJCVlOfY52joDK3d-xzqT8wcFGoX4FUcxndqGaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلجی: شهید رئیسی پنجشنبه و جمعه‌ها را نیز به روزهای پرخبر تبدیل کرد
🔹
رئیس شورای اطلاع‌رسانی دولت سیزدهم: رهبر شهید انقلاب دولت و شخصیت شهید رئیسی را با دوران پرافتخار امیرکبیر مقایسه کردند؛ این اتفاق بسیار مهمی است.   @Farsna - Link</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/435870" target="_blank">📅 12:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435869">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6f5b69a3.mp4?token=SQfwuv7lt46CFpnL2Yjt3mP6VPxtFq56xVO3N2-L9yqITT3CyPspuEHU_M4m5NbJJ-ka-KCXaZPbOTGRbEct3u6IQwglKaqgLVtT5pXT1WpnWDsxKWHjGXaS0Y0cF1y6qVN7zoMUhpKAcBVO0qoA9N1uLFrCYjLf9ExhGaShFaAT2v2yx45Haek-HFxe2Cb8qfFYFfzC7ry2uX9STZ-gRDh_cvHalzoij8nhcFYBBD3r1G11Ach_E2rlLKvJVpyC6PAxrnwXFs_KdWRPVku31-QolG_1yznN0K_NMf_5ag8DUhZfw3GWx9RKxTNBmhjrAb-zUwQzajnxrlJLvfJLmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6f5b69a3.mp4?token=SQfwuv7lt46CFpnL2Yjt3mP6VPxtFq56xVO3N2-L9yqITT3CyPspuEHU_M4m5NbJJ-ka-KCXaZPbOTGRbEct3u6IQwglKaqgLVtT5pXT1WpnWDsxKWHjGXaS0Y0cF1y6qVN7zoMUhpKAcBVO0qoA9N1uLFrCYjLf9ExhGaShFaAT2v2yx45Haek-HFxe2Cb8qfFYFfzC7ry2uX9STZ-gRDh_cvHalzoij8nhcFYBBD3r1G11Ach_E2rlLKvJVpyC6PAxrnwXFs_KdWRPVku31-QolG_1yznN0K_NMf_5ag8DUhZfw3GWx9RKxTNBmhjrAb-zUwQzajnxrlJLvfJLmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی: شهید رئیسی ایران قوی را در سایۀ اجرای عدالت اجتماعی تعریف کرده بودند
🔹
وزیر رفاه دولت سیزدهم: اولین دستوری که آیت‌الله رئیسی به من دادند موضوع کالابرگ بود. به من گفتتند به هر شکل ممکن باید این کار عملیاتی و اجرایی شود.   @Farsna</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/435869" target="_blank">📅 12:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435868">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ujns3dyK8VA-tob27L5J79v9Fj-gU0gCxOHkIATWYY8WSI9DtYKloNUUTuOBII8i_Tm3Fcy4SR20bFjprejtN0Z4_OferxILVk4Wsg9snfqHs1m1n6Oz25_bbR8appY0fAV5ETW-z7hG7Rh79oZlWT5qzFj_gL7kd3Bk0pjbPE8bLWg6EFcN2PaZB96DelHvKSXVssi27onGQvExjeKA1XZhhRzFiJ1RAIu_g3X7OBhpt4G2a4aIYKVys3IxL05nHYIy8N31jXz049kziZEV1AYeqnmUY49zsxlO1YyT3CKjMMwGDYJ-BhlhZedc0wopvm4smnV44NhMxNxJEr8Fug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز نمایشگاه مجازی کتاب از ساعت ۱۰ صبح
🔹
نمایشگاه مجازی کتاب تهران امروز از ساعت ۱۰ صبح در سامانهٔ book.icfi.ir آغازبه‌کار می‌کند.
🔹
نمایشگاه به مدت یک هفته برقرار است و کتاب‌ها در این دوره با ۲۵٪ تخفیف و ارسال رایگان فروخته خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/435868" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435867">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ad4ac91d.mp4?token=rxuPMX-qIHaPX4KyqHMqLPe-aFBfjbaOnCEfRXliM_ch9XiMJfhI7pE6TxYPKSLwAw6dwa_eE1qRAWDY_1EQxkScPlSqsTatV_uexVQ-ZBhRalHISLaIZ0mNg8QxAVCdpRIiPN7IHJmoTv3y7dk-N_Bi4YZGyC0nce2UvH8WWEopR8hmwEGeiY9yuskjMYtcINNvxkHnmB9Ezj8JHgQlWGcWh26IHNqgUHMU6mAZv_M11oY8fEUhhsE04Sbqh04LnXgbtL0eFjAHGVKeD6bVst2yIMp7Un1wEb8UDDc15rlxccATrwYTiUXbbkDMsundP1UJiLZnzM1T-lpdTeiC2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ad4ac91d.mp4?token=rxuPMX-qIHaPX4KyqHMqLPe-aFBfjbaOnCEfRXliM_ch9XiMJfhI7pE6TxYPKSLwAw6dwa_eE1qRAWDY_1EQxkScPlSqsTatV_uexVQ-ZBhRalHISLaIZ0mNg8QxAVCdpRIiPN7IHJmoTv3y7dk-N_Bi4YZGyC0nce2UvH8WWEopR8hmwEGeiY9yuskjMYtcINNvxkHnmB9Ezj8JHgQlWGcWh26IHNqgUHMU6mAZv_M11oY8fEUhhsE04Sbqh04LnXgbtL0eFjAHGVKeD6bVst2yIMp7Un1wEb8UDDc15rlxccATrwYTiUXbbkDMsundP1UJiLZnzM1T-lpdTeiC2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقاپور، مرد سال فوتسال آسیا: این دشمن در حد مردم ایران نیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/435867" target="_blank">📅 12:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435866">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ9PxW_kk8aomk0urUIBscIBUezVbvOTo4rHwf7CN50E3ML8XNwAjhBJRVXFV_x2YvZnc5Hn5VZSgPad9gsJ-GyrO3qUdxqCs-XAZKJi-9wUlRo-xXjyecNJW_oMoZI0kbQUIxOLgxiNqxQsgZEtA-nWHEZRqvcn0tgAYbhRIMaG7fvu5Iy2IVG3rlBTyieplIOOiCpaISbI0UlNPdQ8qqc2OR5Um5CsiJMOpx95bknV-Ta8ZD0BYBajaKg4MuSUT_toeJPCVAK-kDi7YpXotssI3TnuMcgSAHVWsZuYznI6M4MfGP1n-skJic1EPaoBP3MUaTbjwSFZMTXBTNKE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گندم به بازار سیاه رفت
!
🔹
رئیس بنیاد ملی گندم‌کاران: در حالی که وضعیت تولید گندم امسال بهتر از پارسال ارزیابی شده تا امروز یک میلیون و ۴۰۰ هزار تن از کشاورزان خریداری شده که نسبت به پارسال ۲۸۰ هزار تن کمتر خریداری شده.
🔹
کارشناس کشاورزی ابراهیم مرادزاده علاقه نداشتن کشاورزان برای فروش گندم به دولت را هشداری برای مصرف گندم در خوراک دام می‌داند.
🔹
اکنون قیمت هر کیلو ذرت دامی در بازار آزاد اگر پیدا شود ۶۰ هزار و قیمت گندم ۴۹ هزار است و مرغدار گندم ارزان را جایگزین ذرت گران به‌عنوان خوراک مرغ می‌کند.
🔹
رئیس بنیاد ملی گندم‌کاران می‌گوید دولت پس از ۴۵ روز هنوز ریالی به کشاروزی نداده و انگیزۀ آنها را برای فروش به دلال بیشتر و احتمال ورود گندم به چرخۀ خوراک دام و تهدید خودکفایی را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/435866" target="_blank">📅 12:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435865">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">توقیف اموال ۵۱ نفر از خائنین به کشور در یزد
🔹
اموال ۵۱ نفر از خائنین به وطن و افراد تاثیرگذار در شبکهٔ همکاران دشمن در راستای اجرای قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونسیتی علیه امنیت و منافع ملی در یزد توقیف شد.
🔹
این اموال شامل وجوه نقد بانکی، اموال منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی می‌شود که با دستور قضایی توقیف شده است و بررسی دقیق‌تر در مورد پرونده این افراد ادامه دارد.
🔹
از این تعداد، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر درحال‌حاضر در خارج از کشور به‌سر می‌برند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/435865" target="_blank">📅 12:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435863">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4385b6bb5c.mp4?token=Qqm0giCMeWv22_Ta54RsLokOY9x1k_HHlbA2qUIpXDLwUIAcWWT6JLlAcVmcj4zpFbwWqjCA9xnH4cYHWxzkdy3qsRuIS1eR1o7yqDKJm2-qGaCpuTE5SwNUDEggC0C-U8ea4L-yY-n7XpJ5MfGy2nIKdz9llgwsPbllJTJ3sD7ZNGjU1uaTEXaqlYMBbynno6DMJyZKR-dpteCMApqKx_9b9XRYeRdVYwc2cBxtDy4106agbK_N_P--5LCOs463rXNVkKx3WeebArHx1eLYVcku6fEXwF_zKNpZm6m3Lt9tWPehI2IZ2xeAAbOCpFziyOpUJ4zPCCFDkWwh2Evw7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4385b6bb5c.mp4?token=Qqm0giCMeWv22_Ta54RsLokOY9x1k_HHlbA2qUIpXDLwUIAcWWT6JLlAcVmcj4zpFbwWqjCA9xnH4cYHWxzkdy3qsRuIS1eR1o7yqDKJm2-qGaCpuTE5SwNUDEggC0C-U8ea4L-yY-n7XpJ5MfGy2nIKdz9llgwsPbllJTJ3sD7ZNGjU1uaTEXaqlYMBbynno6DMJyZKR-dpteCMApqKx_9b9XRYeRdVYwc2cBxtDy4106agbK_N_P--5LCOs463rXNVkKx3WeebArHx1eLYVcku6fEXwF_zKNpZm6m3Lt9tWPehI2IZ2xeAAbOCpFziyOpUJ4zPCCFDkWwh2Evw7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرتضوی: شهید رئیسی بر این باور بود که ایران باید قوی باشد
🔹
وزیر کار دولت سیزدهم: ایشان بر این باور بود آن ایران قویست که می‌تواند در بزنگاه‌ها نجات‌بخش محور مقاومت و ایران اسلامی باشد. @Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/435863" target="_blank">📅 11:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435862">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055e57e9b1.mp4?token=bm4WdK3cSqm5aOljX526D6Dr-NuE9oXhS3ymVilmed2DLLkz4FstygiwsfCqZHdKRAOF5tajY6y6ai5MKV1T7tpvzRpWp3USc6tfHUo9IT7AqM-4RjcC6rRONZnk2Bs0HvXNvRVcWxgshk5Ce0Bl8di_0pbQEh4MauoVTu7epPdmk2cQJXEhgz1FiR659J_065LfWKg8ei-ZxXMHneUSbx5iBJP2DyljZL01rPHU-ztuNlorfRrbmsYFPHyYe4KDdUhrHZHFmoKh6XjMsahlKusBeEdNePpkEm4U_GLt7nXnTBQB5j87cpJDQElE5lplC8AurClOridsnZFFzhi47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055e57e9b1.mp4?token=bm4WdK3cSqm5aOljX526D6Dr-NuE9oXhS3ymVilmed2DLLkz4FstygiwsfCqZHdKRAOF5tajY6y6ai5MKV1T7tpvzRpWp3USc6tfHUo9IT7AqM-4RjcC6rRONZnk2Bs0HvXNvRVcWxgshk5Ce0Bl8di_0pbQEh4MauoVTu7epPdmk2cQJXEhgz1FiR659J_065LfWKg8ei-ZxXMHneUSbx5iBJP2DyljZL01rPHU-ztuNlorfRrbmsYFPHyYe4KDdUhrHZHFmoKh6XjMsahlKusBeEdNePpkEm4U_GLt7nXnTBQB5j87cpJDQElE5lplC8AurClOridsnZFFzhi47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شلیک با اسلحه در برنامۀ زندۀ تلویزیون!
@Farsna</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/435862" target="_blank">📅 11:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435861">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d5637a2e6.mp4?token=gIoQIFIy58PZgR61rK7-_o_WS70jFNut72x0j9yYWK8ZXHaPSteWLfKLbwisgund3eiMnEtThzMxv2UkYn1kqZ8nu2IRBCa2valCjLWJHxDaKVcnbxsMUrboX8cq97nHJGHGEv2sIjDlHIRCEy4PvZ-_AC8z_g3wZT197xUKZS20keCw7He2RpcBNXURGI233LejAlPCMzffo8c0Vxs4-SFulHJIQdbJy3hm9bS4DsJXG5Xyx7tei3h2ahSzBq4stxeK3v7KTNIVjiEy7ATrd9bT5OQpirYcF7hAz7zBRsuw0xk9TDFbBsNmzGg26_6SK6CyrM8a_Q4d-JTG955GWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d5637a2e6.mp4?token=gIoQIFIy58PZgR61rK7-_o_WS70jFNut72x0j9yYWK8ZXHaPSteWLfKLbwisgund3eiMnEtThzMxv2UkYn1kqZ8nu2IRBCa2valCjLWJHxDaKVcnbxsMUrboX8cq97nHJGHGEv2sIjDlHIRCEy4PvZ-_AC8z_g3wZT197xUKZS20keCw7He2RpcBNXURGI233LejAlPCMzffo8c0Vxs4-SFulHJIQdbJy3hm9bS4DsJXG5Xyx7tei3h2ahSzBq4stxeK3v7KTNIVjiEy7ATrd9bT5OQpirYcF7hAz7zBRsuw0xk9TDFbBsNmzGg26_6SK6CyrM8a_Q4d-JTG955GWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشریح برنامه‌های دومین سالگرد شهادت آیت‌الله رئیسی  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/435861" target="_blank">📅 11:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435860">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99a5e9d49a.mp4?token=eQkpYABj_63d2VsCK3UhtwbPybDYDuRLW7dVyADh16rCg5w-nPNXxqy2MDtxaeLcYAT4K6E4GyeyLUiVV82HLk4AU88-ijmlcCIMaglg_4VClPBNwyiks9JpgKXT9AH3ZMwKVmVVzPI5lzFAD6eH4LHujjOXfod7V9sOS97jafTrgEj_5AzqHwmuCcfm9LM1v48IAntXNvUtmXx9OGZdvVBGiCg3KaUys9pHVlB2wQGJhlVx-QJjGytEZhruqqzsEV9KS9Af49Bz-TM3pu6IqogaPFE6jyOc9AfopQ0vnEosuN6Iljjp3WIOih-ayJz0K1dPVhS6T1XXAy5x_Z81GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99a5e9d49a.mp4?token=eQkpYABj_63d2VsCK3UhtwbPybDYDuRLW7dVyADh16rCg5w-nPNXxqy2MDtxaeLcYAT4K6E4GyeyLUiVV82HLk4AU88-ijmlcCIMaglg_4VClPBNwyiks9JpgKXT9AH3ZMwKVmVVzPI5lzFAD6eH4LHujjOXfod7V9sOS97jafTrgEj_5AzqHwmuCcfm9LM1v48IAntXNvUtmXx9OGZdvVBGiCg3KaUys9pHVlB2wQGJhlVx-QJjGytEZhruqqzsEV9KS9Af49Bz-TM3pu6IqogaPFE6jyOc9AfopQ0vnEosuN6Iljjp3WIOih-ayJz0K1dPVhS6T1XXAy5x_Z81GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
نشست خبری دومین سالگرد شهادت آیت‌الله رئیسی را در پخش زندهٔ فارس و آپارات ببینید  @Farsna</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/435860" target="_blank">📅 11:24 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435859">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaEncd2rswxlEF5GeBly6-uEC7_wKKe9mcUClH1wukM1bIqcSf8CJgJFd_HZTYTlUZhc43dzUMAZJYioC4nuEDahmIa1Cz8BOLHgrAE9Uo2bHDII8xYvNpk5k7lm9hQ6Kbi4YT-ElsEI8ZqSzWME23CvWoKdXg-marM4KOvWIFZbRciiV0GwI8LVdKayLbIjOl0Df82D7M-_411y2TQGf0kq43V6bA7vDqdXjTgokiAMnzJyx_y4bK5RaK9joKqitlxkhSqTdESbw01DnsoJVJqo_z2SHsH3TJi4WsUE8RA5uxlLzNWrwYm6pcmY1vTPFYHQeOm9hl22fW39MdzhnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
نشست خبری دومین سالگرد شهادت آیت‌الله رئیسی را در پخش زندهٔ
فارس
و
آپارات
ببینید
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/435859" target="_blank">📅 11:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435857">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آخرین وضعیت نحوۀ برگزاری امتحانات دورۀ متوسطۀ شهر تهران
🔹
آموزش‌وپرورش تهران از پیش‌بینی دو سناریو برای نحوۀ برگزاری امتحانات پایه‌های هفتم تا دهم خبر داد.
🔸
سناریوی نخست: در صورت تداوم شرایط فعلی، احتمالا امتحانات داخلی دانش‌آموزان پایه‌های هفتم، هشتم، نهم…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/435857" target="_blank">📅 11:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435856">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTIBhIdnt5sJsvMV-6VrH81eBTYagu5aUb6mXeMKVEhtqp0-PTF874W24hsQ2Qd5rAftklIBY7rPmApIJZPcIKVy6m8IUvHu7SEYGUw9Nu9bn9HXPdIukz7mpPeeuoYgI25dCYDQyY5BhJl_XXK_fBd13ym8mj0f9U00pu7lCnPBHZjBnvrNNjLLQnAEIiyXXPFdrrLNm9hHY3OJxtG7d9Kfx7Ke9_XEDFFsHhRDc4MiQW6obsKvF1I9CGW8K7JQP791XFtgx7vsaEUHMmFHpxR81Rf6W-CBI2M5vZATrU4gK4Tt0bvx2xvwriM6lXhyTHzR4h-BxYqcVRaUpqnXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود بیش از ۱۷ هزار زائر ایرانی به سرزمین وحی
🔹
رئیس سازمان حج و زیارت: تا پایان روز پنجشنبه ۱۷ اردیبهشت‌ماه، بیش از ۱۷ هزار و ۵۰۰ زائر ایرانی وارد عربستان سعودی شده‌اند و روند انتقال زائران از مدینه منوره به مکه مکرمه نیز به‌صورت منظم با قطار سریع‌السیر ادامه…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435856" target="_blank">📅 10:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435855">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ca9b32ea.mp4?token=dG3dF5OyYUwQeNKBeBE2BsMi9OVNIscDwwzZl0Vif4es3sg1dUxHqqIWHcCKv2owlhqLv9KEpK6RRzVtawX5KdOOxL_mTRkj_lGjlVwUQRIzy-scv6uEIxnvQ9XgNjcRIAetykRG0PYVYuZpyMYj7mtPWItd1slJp1JrRpNti-E0xReGjdCKf9wJN7_L37prONHEVfXhOYbxtEdvw6F9QQ6-EJvOJiiwhJrW60_9a39NSt9YrzAANd9A6r0IgakFC5ExZALXdxRA1wz6hqBhJs3dKfy0tvOk5mnnapKTYUhLRHu0k-EBkyulyS2sXwW-AZj24B_GlDpATnyktptOE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ca9b32ea.mp4?token=dG3dF5OyYUwQeNKBeBE2BsMi9OVNIscDwwzZl0Vif4es3sg1dUxHqqIWHcCKv2owlhqLv9KEpK6RRzVtawX5KdOOxL_mTRkj_lGjlVwUQRIzy-scv6uEIxnvQ9XgNjcRIAetykRG0PYVYuZpyMYj7mtPWItd1slJp1JrRpNti-E0xReGjdCKf9wJN7_L37prONHEVfXhOYbxtEdvw6F9QQ6-EJvOJiiwhJrW60_9a39NSt9YrzAANd9A6r0IgakFC5ExZALXdxRA1wz6hqBhJs3dKfy0tvOk5mnnapKTYUhLRHu0k-EBkyulyS2sXwW-AZj24B_GlDpATnyktptOE4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازخوانی سالگرد سفر اردیبهشتی رهبر شهید به مریوان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/435855" target="_blank">📅 10:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435854">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-EyqRNLJ6bD4EfB9t_uXUW3U8Aqjr4o9D6X2Gb_4rKcdi3e3xcv5VxCCo2ImuHFWXQDijaJwfloOhH3rluihLLFR4tMUT-dlYr5jqWjs0zr6B2-trfUi3nSQ4o6amNVI9fiIpj6HZkJUIart6NdKt4to2kx5dg8RQrGyfKU4AcZxV7u6F3MYHyLLVqn1sv0C4W1jPW7nU_QESHrvs1ABl5mFnX9oVrJhdyW5GZo7sL7cGy6e22V0QptcyS9V9k_TliZv_XN7LlzTXggEduxN7P5HEeIubp1S8jvhPA_sJZEV2zALf9C-7PwbwxUkSdxlEhIOGIt7RE42hwSolfISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌ رایگان‌بودن مترو و اتوبوس تا ۲۷ اردیبهشت تمدید شد
🔹
شهردار تهران: خدمات رایگان مترو و اتوبوس تا ۲۷ اردیبهشت تمدید شد و تصمیم‌گیری نهایی به‌زودی در شورای شهر انجام می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/farsna/435854" target="_blank">📅 10:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435852">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdee230e76.mp4?token=giD0BI7l8t0X27kdb12RUTAZW5jGcjz7IpUwNPadbCYGyD1PW0Vj_Y0r2LmxXfXk1iMS0O9DpFgueEzNNO82Fl_qXWg61Mf-Zv0Q_9_dwVWW1o4V3byv8BxjlUciX9c9vBLjPmQvCU83g2gdkRoHDNS-x0nfJlhtAkCzdy_L1xEbz6R7UGp7J9Sd7Ho8T-pNdloGq3T_UNxjYXesypAn5Ki1Fo1B1XcAuAvh0LFNUk0CsIBgMX5ASuveUG4TyZUCaxrGmWxB151ljSMuyPjtgXAfnKQooAMmDys5ld3HkvNJ5PgenxJ5fvZhtUTMxG6crtNw2l-div462ljk12ukzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdee230e76.mp4?token=giD0BI7l8t0X27kdb12RUTAZW5jGcjz7IpUwNPadbCYGyD1PW0Vj_Y0r2LmxXfXk1iMS0O9DpFgueEzNNO82Fl_qXWg61Mf-Zv0Q_9_dwVWW1o4V3byv8BxjlUciX9c9vBLjPmQvCU83g2gdkRoHDNS-x0nfJlhtAkCzdy_L1xEbz6R7UGp7J9Sd7Ho8T-pNdloGq3T_UNxjYXesypAn5Ki1Fo1B1XcAuAvh0LFNUk0CsIBgMX5ASuveUG4TyZUCaxrGmWxB151ljSMuyPjtgXAfnKQooAMmDys5ld3HkvNJ5PgenxJ5fvZhtUTMxG6crtNw2l-div462ljk12ukzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهلوی‌چی‌ها به خودی می‌زنند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/435852" target="_blank">📅 09:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435851">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فراخوان مشمولان متولد ۱۳۵۵ تا ۱۳۸۷ برای تعیین‌تکلیف سربازی
🔹
سازمان وظیفهٔ عمومی فراجا اعلام کرد: همهٔ مشمولان غایب و غیرغایب متولد سال‌های ۱۳۵۵تا ۱۳۸۷ باید خدمت وضعیت خدمتی خود را تعیین‌تکلیف کنند و مشمولانی که در مهلت تعیین‌شده وضعیت خود را مشخص نکنند، وارد غیبت می‌شوند و با محرومیت‌های اجتماعی مواجه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/435851" target="_blank">📅 09:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435850">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgyuB9av5mC0hPX9bZJOst-GRl0NOCaa7UPabTjlI6RLQ0iBAPkxuEAurLlx2fE3BAVQ3wV5VWbKFdCvpL1sKQu8BgBqFnA1Zw6fzjxTUUBGjTmhq5lSQQu4SNdsYmrcFDfKgbcB8pj5qNAOh9oFljGkG6K_FHyZTD8UsgYDQ8cSd1rHT3ZyTFHlPJkhVKm-mMcdA7EnubvR0ARbgoptVnm7Bz28QO_opcPKxIWUJj0Aer0U-c-XnGclMHLDu_J7lIj7NjBk5wVNx-zxKcKtI6mhAP7eiDl4G7fxr-6l3kE6QSH3_4QgsQSvxJVc_GS6pU7jI_h00EybCdglG2hV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رهبر کاتولیک‌های جهان: تهدیدها علیه ایران به‌هیچ‌وجه پذیرفتنی نیست
🔹
پاپ لئو: حمله به زیرساخت‌های غیرنظامی برخلاف قوانین بین‌المللی است. تهدیدها علیه ایران به‌هیچ‌وجه پذیرفتنی نیست.
🔹
مردم همواره به دنبال صلح باشند و نه خشونت؛ و جنگ را طرد کنند؛ به‌ویژه…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/farsna/435850" target="_blank">📅 09:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435849">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc2eb23cc.mp4?token=MF6sHy1LRolEjKnw955xvNFNs1NtGv_6PPceln7i1TU-zLeaacDxTSBgsWncgfQKkx6HGh5ijBOxIeiAhXiDXgKpxuLawtEdRudCAAwil8TffGaWE7bzcVgIiCkTDF3AHnq3MFBOGv29x5wtkQDS_UxZGp7lWv-z_gGasvdSSR7G5vil2M16EbONOFxU4psqXeMrLqzttvveggceeJkGgr41UJ04aF35anAzea5zW9Zm8z4vbNz9HVzrb4C9i1dDIhsF7RKoN28wF4zQF3chnaiYIGhsQ7nRgyEN9tFZOc7WryUZkRQ8jxz6vTQTNsYC7PAUw53ZICZycGCPvx_zFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc2eb23cc.mp4?token=MF6sHy1LRolEjKnw955xvNFNs1NtGv_6PPceln7i1TU-zLeaacDxTSBgsWncgfQKkx6HGh5ijBOxIeiAhXiDXgKpxuLawtEdRudCAAwil8TffGaWE7bzcVgIiCkTDF3AHnq3MFBOGv29x5wtkQDS_UxZGp7lWv-z_gGasvdSSR7G5vil2M16EbONOFxU4psqXeMrLqzttvveggceeJkGgr41UJ04aF35anAzea5zW9Zm8z4vbNz9HVzrb4C9i1dDIhsF7RKoN28wF4zQF3chnaiYIGhsQ7nRgyEN9tFZOc7WryUZkRQ8jxz6vTQTNsYC7PAUw53ZICZycGCPvx_zFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ خواننده سیاسیِ منفور به محسن چاووشیِ وطن‌پرست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/435849" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435848">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUV8bvEtH654Ig0YVzeQhMUzwNZyZfcICwCCBYGIFyaXZdntiI4BN4FEJvhdstqLNvCaDJt5vZjV8GeILgNBOSjOu2QwmynLKpJgtxa8ORH0o-jRHE240NA1dZxM5h0L_nNWXRRgz9uv0z6E1IjwRxTrBtwcJz2tco29g7KHtRwWlp5Qc15ZYgMGJoTfbr__Sit7SsVmLnxKwxTLIcoBiwpHgfdl471emenUJyXoEab9fcinlv6a0j66LHGqpcr4lmEKceo-vtWV95Tar-iPnWLomZCbmW_GMZCLNabJxOtdureY22CfqJYgV_yxWvIBxpzzFOsSFGBfupFqs5JeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مدعی کشتن مرد شماره ۲ داعش شد
🔹
رئیس‌جمهور آمریکا، بامداد امروز از کشته شدن فعال‌ترین تروریست جهان به نام «ابوبلال المینوکی»، نفر دوم داعش در سطح بین‌المللی، خبر داد.
🔹
ترامپ در پیام خود مدعی شد که این عملیات به فرمان مستقیم او و با مشارکت «نیروهای دلاور آمریکایی و نیروهای مسلح نیجریه» انجام شده است.
🔹
رئیس‌جمهور آمریکا در ادامه بار دیگر با تلاش برای پررنگ کردن نقش آمریکا در این عملیات نوشت که که المینوکی گمان می‌کرده می‌تواند در آفریقا پنهان شود، اما از وجود منابع اطلاعاتی آمریکا که تمام تحرکات او را زیر نظر داشتند، بی‌خبر بوده است. ترامپ در این باره نوشت: «نمی‌دانست که ما منابعی داریم که ما را در جریان کارهایش نگه می‌داشتند.»
🔹
ترامپ در پایان پیام خود از همکاری دولت نیجریه در این عملیات قدردانی کرد و نوشت: «از دولت نیجریه برای همکاری شما در این عملیات سپاسگزارم. خداوند آمریکا را حفظ کند!»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/435848" target="_blank">📅 09:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435847">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emRk2FVFekZ4mIG-Q9AFvi8gqbjlE23W5SQIePkYz-41lFfYc20f3d9DxfwdNhUCfPbqem4fV3htIH6wl-cJmtGH3N4nZmr5m67Sp9RMx-TE7EPgjN99QBPX-T4TZ2YPIOq3tzkB1xT2dCXOQFeb7B6JVgW1rofU6KqP3kb7AstLggMK1HeBaFT7s2EmoZq2ASlgBJbFc19WN6bH3qdOVL4ZasyV-Rgx_zQNSPln4y7YCNi6IN8nZ4zB5xXYM196c7v4D8kPOXFIvziAeGDRyaxM5827-yVsxOgb9oFYoyqT0zR0m6CLxdZsGc6Qo0Iw_G4-vFTtSjr83aI9iUq9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز نمایشگاه مجازی کتاب از ساعت ۱۰ صبح
🔹
نمایشگاه مجازی کتاب تهران امروز از ساعت ۱۰ صبح در سامانهٔ
book.icfi.ir
آغازبه‌کار می‌کند.
🔹
نمایشگاه به مدت یک هفته برقرار است و کتاب‌ها در این دوره با ۲۵٪ تخفیف و ارسال رایگان فروخته خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/farsna/435847" target="_blank">📅 08:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435846">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGUDoTZGzRhdvhe0YICb6AYsd91C4f7e6FKEhDNMdQL_3YH9ndxvd7hSSmpdsAV4oeIjvrTgyIHIWghigqk9ywGZQSItAHT9m15n2mO-1ZJVKOCDXeyJmS6EO5nDuyeU7AubzHZmmwamN3EibIs8iJiMWPk4jtwRV-GG5No_Cm5XCQ5UoCBFa7ybhX0ilR8iYxasO_S6g0FNXFECNPABJGVcumAKunuKFdV9MRY_zycXcaL438FAm9ZGT0cJb2ZLCgq4mR4V-eJbRcLt0QEtKoWD90zTAsAyTY7lUyysJdgNq_dJ8fz8DQqDBNFsyku78mrDvx31H07J6uzIGvVMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی، هدیۀ چینی‌ها را دور ریخت
🔹
خبرنگار نیویورک‌تایمز گزارش داد کلیۀ اعضای هیئت آمریکایی پیش از سوارشدن به هواپیما برای ترک چین، تک‌تک اقلامی را که چینی‌ها در اختیارشان گذاشته بودند، دور انداختند.
🔹
هدیه‌ها، نشان‌ها، سنجاق‌ها و اشیای یادبود همگی در همان محل درون یک سطل زباله ریخته شدند.
🔹
به‌گفتهٔ این خبرنگار، هیچ اقلامی با منشأ چینی اجازه ورود به هواپیما را نداشت.
🔹
این احتیاط‌ها تنها به زمان خروج محدود نمی‌شد؛ پیش از این نیز اعضای هیئت آمریکایی تمام وسایل الکترونیکی شخصی خود را پیش از سفر به چین در خانه گذاشته بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/435846" target="_blank">📅 08:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435845">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
تعطیلی ادارات و بانک‌های ایلام به‌دلیل گردوغبار
🔹
کارگروه اضطرار آلودگی هوای استان ایلام با توجه به تداوم گردوغبار و افزایش شاخص آلودگی، از تعطیلی تمامی دستگاه‌های اجرایی، ادارات و بانک‌های استان در روز شنبه ۲۶ اردیبهشت‌ماه خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/farsna/435845" target="_blank">📅 07:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435844">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بارش باران و رعدوبرق در ۱۴ استان
🔹
سازمان هواشناسی امروز شنبه برای تهران و ۱۳ استان واقع در نوار شمالی کشور بارش باران و رعدوبرق پیش‌بینی کرد.
🔹
در استان‌های آذربایجان شرقی، آذربایجان غربی، اردبیل، کردستان، کرمانشاه، لرستان، زنجان، قزوین، البرز، تهران، همدان، مرکزی، مازندران و گیلان در برخی ساعات بارندگی، رعدوبرق و در نقاط مستعد تگرگ پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/435844" target="_blank">📅 07:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435843">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNRTYGvz_IUnbkABTR1CqNWW_M3VstZbuwYYgvSA8-Qm7yxVpbP_1rx4iFc22NjOVI6oe75KdDJUQGTWtjmBsSNPL7DSPKm6dBsWsDkGgkkJMgJOAt7wRHlIazpPtJ7yqDQhELXnIM6MZobSgtx5yCrSdhmUwB236tiv3JchLQotMWJ4o6vF-a-puBbgyreTBqAe795i2e4JTqmcGf5voqW1x1FgFGr9tj9OKID2AxIz-ebSgHWXK8T8NJVQJYuEnKP5eSztgtPjlVmCgr-dc5t3l4MEE0m2ZKOJzmcR3erwcm2eYWNMQzqG3dnVOYoQlg6fTsABUcISjuBj_H6dsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام گمرک‌های عراق به‌روی ایران باز شد
🔹
بیش از یک ماه از محاصرۀ دریایی آمریکا می‌گذرد، تجارت ریلی ایران و چین سه برابر شده، پاکستان یک مسیر ترانزیتی جدید با ایران راه‌اندازی کرده و مجوز عبور کالاهای کشورهای ثالث از طریق خاک این کشور به مقصد ایران را می‌دهد.
🔹
حالا نخست‌وزیر عراق هم ادارۀ گمرک‌های مناطق شمالی، مرکزی، غربی، جنوبی، ادارۀ گمرک بار هوایی و گمرک فرودگاه بین‌المللی بغداد را موظف کرده تا حمل‌ونقل ترانزیت و بارگیری مجدد کالا‌ها با ایران را فعال کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/435843" target="_blank">📅 07:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435841">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMv2Aif85NoD_MOjxJgC461VVQAULvydVbG1gZWueLYs3rP0bywVK9Hslg0mSJyPAizPBstp8kk7HvW0dq1ijk2uxrveM95OCKmtl0d3K0EjTMNtA1n92eBWKFNaI27D16d1aCeoFuGZ_BycuFqTSzm_9bBoTKbbjqTbXi1qqNHYuQob-q2AKIHxvHKM9GoUX_Zv96szGrFwwHu65DirmX-NFlNopC6LcEl2Ud7tWQubbd_UhCipa_KvK7XQtRHQK4MR7BOabPxHkJqjFJjVK_hRw_EckIj_zrQ9tBfxmvLFmivWk4fx63exc9U9Y_DGozZ3diiRAc6Z4NE4q2U2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احضار غول‌های فناوری به سنا
🔹
مدیران عامل شرکت‌های بزرگ فناوری آمریکا از جمله متا، آلفابت، تیک‌تاک و اسنپ بار دیگر برای حضور در جلسه استماع سنای آمریکا درباره امنیت کودکان در فضای آنلاین احضار شدند.
🔹
این جلسه در شرایطی برگزار می‌شود که فشارها بر شرکت‌های فناوری در آمریکا به‌دلیل اتهام طراحی پلتفرم‌های اعتیادآور و آسیب‌زا برای نوجوانان افزایش یافته است. قانون‌گذاران آمریکایی طی ماه‌های اخیر بارها خواستار تصویب قوانین سخت‌گیرانه‌تر علیه شبکه‌های اجتماعی شده‌اند.
🔹
جلسه جدید سنا ادامه روندی است که از سال ۲۰۲۴ آغاز شد؛ زمانی که مدیران شبکه‌های اجتماعی برای پاسخ‌گویی درباره سوءاستفاده از کودکان و محتوای خطرناک به کنگره احضار شده بودند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/435841" target="_blank">📅 05:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435840">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
روایت سخنگوی دولت سیزدهم از عصبانیت شهید رئیسی برای عدم پاسخگویی به یک دانشجو
@Farsna
-
link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/435840" target="_blank">📅 05:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435839">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e91091688.mp4?token=fYCBPzatdaPl5O2M3iSvIdCz9Xtp30hAHm1Ep5gDU_iDs3FXo5OASViweC_ZOEvnnutUn7Zo6jgHEB7n71WyCitUTSMegv3sV6nV2UfttWZBVXxGTz8b1dz_lDRsUlqnez2fdQjs1SS5H5I637nR9wmoxxzZbasufOpXxyAXLnolHGc3RqrwivRJRJrUfng52MU9Abd1cm8uj6nxv4Fyin_iIIb7rBMKIS08stwFk3FgeBBxL7kEb--1x8RwtZxDqbIDKa1pCdeplkcF-bgLVFfpY5AQlVQlj8PhgEjOS0uBKVl3yOatuxDCKNC0ysTeZi5GSnfkWUVBmTyWiGK02w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e91091688.mp4?token=fYCBPzatdaPl5O2M3iSvIdCz9Xtp30hAHm1Ep5gDU_iDs3FXo5OASViweC_ZOEvnnutUn7Zo6jgHEB7n71WyCitUTSMegv3sV6nV2UfttWZBVXxGTz8b1dz_lDRsUlqnez2fdQjs1SS5H5I637nR9wmoxxzZbasufOpXxyAXLnolHGc3RqrwivRJRJrUfng52MU9Abd1cm8uj6nxv4Fyin_iIIb7rBMKIS08stwFk3FgeBBxL7kEb--1x8RwtZxDqbIDKa1pCdeplkcF-bgLVFfpY5AQlVQlj8PhgEjOS0uBKVl3yOatuxDCKNC0ysTeZi5GSnfkWUVBmTyWiGK02w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنگ‌تمام اردبیلی‌ها در شب هفتادوششم
@Farsna</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/435839" target="_blank">📅 04:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435838">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cdb5a18d.mp4?token=FpL0lHtec5GdNvFf4XfDrNlBCEM3ypfrDozwOs22GWy60gmsksavVgn8aqpvAWYNCCrIe52jWV0lVFD0s1arptTcUX6SLkT2bMD-_Sr_2bpbg2a2fS7xzM7YD9uAK6jCyx9d3IOneBZ-zCIUmcjTN_vm2IPJovM3cym_uX-H--wa99o_QSTdDb9jTIxrC6R7NmmloCkcy4cpAi5R2lLJkEw9tiuvCx_ilaFuy_PTpov4LWWggnDhD4Q7C7WhD94j_98jnhibo7GgZzmt3tqFfbihidGjPirD_hYuOQi57bimdcDhvB1E5iCfdHtg5WLtf3nLvzMHIlYiN_XaemgEuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cdb5a18d.mp4?token=FpL0lHtec5GdNvFf4XfDrNlBCEM3ypfrDozwOs22GWy60gmsksavVgn8aqpvAWYNCCrIe52jWV0lVFD0s1arptTcUX6SLkT2bMD-_Sr_2bpbg2a2fS7xzM7YD9uAK6jCyx9d3IOneBZ-zCIUmcjTN_vm2IPJovM3cym_uX-H--wa99o_QSTdDb9jTIxrC6R7NmmloCkcy4cpAi5R2lLJkEw9tiuvCx_ilaFuy_PTpov4LWWggnDhD4Q7C7WhD94j_98jnhibo7GgZzmt3tqFfbihidGjPirD_hYuOQi57bimdcDhvB1E5iCfdHtg5WLtf3nLvzMHIlYiN_XaemgEuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نسل زِدی‌های جهادی!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/435838" target="_blank">📅 04:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435837">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyAGcxUpPR8IPLb1_y707YpdNmd0GGlgMyQIbBZ4TahTsdQkKNqGzpDnBqrW9wjx4jaevi6P8PtBV0XB8uUZvjyUFmmRq4W1cSnXZG9kioB8W9avoW4ZNHCdyt6f8q1OOwjW3-4S4DlGjHmfArUgBzrYDWcEiJnll9sLtPjk4LqoKjQCIAVEIs8v5UjXgA25VG9KU3Va1Ki8m9pGmHBkTbdD-1nc2O-Qj4BfVb9lbbNmYKX_KVUSdc1ACRczZI8Ce-KKUaWIW6QxD_UCxN8fh1L3Hjfin1gruzOHrQQS_NigdKIfcSEMG0JHdnLd1gopjMif89Q840qZgxbhDNrtSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز بنزین هند را گران کرد
🔹
در پی جهش قیمت جهانی نفت و تشدید بحران انرژی ناشی از ناامنی در تنگۀ هرمز، هند برای نخستین‌بار طی چهار سال اخیر قیمت بنزین و گازوئیل را افزایش داد؛ اقدامی که از تشدید فشار اقتصادی بر سومین واردکنندۀ بزرگ نفت جهان حکایت دارد.
🔹
در همین حال، نخست‌وزیر هند طی روزهای اخیر به‌صورت بی‌سابقه از مردم خواسته مصرف سوخت را کاهش دهند، سفرهای غیرضروری را محدود کنند و استفاده از حمل‌ونقل عمومی را افزایش دهند.
🔹
رسانه‌های هندی این اقدامات را بخشی از برنامۀ اضطراری دولت برای مقابله با تبعات بحران انرژی توصیف کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/435837" target="_blank">📅 03:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435827">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTJ4F72Y2xYZuB2GrsbSOPGKXfCQD4TagWw3Ty5nFn1j68QB1q6ybL9qQi0vnfroXLNolb_m8Coe_2XRvx6X8ZTE_fSWnEQappmtjDEmPvRqE-Wt1zCUTnYjWA74A5e-xnG6o3zuVeMF72hnLc1l6Y6tikm3pGUpOq2GQ-Udf9nMKQTKDRUR0jdVeaKTiwOiH5ljoAfSL4KTa0DgcFQKrVqThrZwFccyEzLN3b9SJrdaB0yas1C1axe0nwcaVK-mPXI9T3dPnJhwR9yEuHEf4_NWeyq9ilQBxYQLOK7cRM33i7etVikzKJWR6UsvlFtpMz891vgR5e2ZGZ4L1NmqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vos-dMWxwm7Z4uIorNYfHaJPw3ZEHpKQiDpW6Ybwu1IuSt-EI8uP734-qeXQzQ9iynZUvoMbCNS9oYmGKueIWz3Gy1EGg91o-5g4xMuAgBWlNg7HoJ_ahG7KZo47eK_8uuBGOMet4lG8QXv-Rl8NJ9hNNtjlNT0q-AAMXQC7-TRhtTGiUsD4yIiqIVc8C7zs69qsWPSdSUjI8ZSqYEztdS2VZAGrkKUwU8WFDTlJua2wQyLQqRqTioyVJLffRM2oqBJKub2VIc7cs8MLW0msFB5NWbUknkPKBtUWUNkaaUh53hfdbPzROMhI_QefKNfj2awb1FlDQo8gYIxI_wxDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLor9dgaohtFnU1uddmlYdKAJx9OdQJbRqgxwkKshGjy5-bT3uDj9Di6C3WeaziIGm7OsOKMT94a8hIML2ac89vHEoZG9OevmhqaFA7Ln7FXv8BaDE-STjwd1DockyBciuUa8bBzlapEtA_kFMkzGeoGCVXF9TmN_Effs2JFyUNnV2wZr3dlGdENtQmzXwtWS_ZWDePfCJ4Quyvnq_ERF2PPlid3lyBARllXURdaJKGjN1aZNDkS1UGRs3ScZuB5kKgb7nzGkjGoKR3HgM2UiugbqGhC5FGsecB0jidTlABciDtBs_97U-AejyT1hk5JblxtyPhsHK5pzkEEgK-Q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hiYDUNifR4xPsvSobXkWLd67uJcrMBS91nbL4VtdFotHEcDwBTYl0hmoS_SKCXTV0ViNCmOiQDzVLj9VMONjdL0BaRehFVtTOBRWGFp3pRbSmJwEhu1DjLXlB-l5CQZw21jUedeDI79xX2qr2StqZmXTX-Ltvehw5prPpoDZIg69hf3Nty6gMNohLQNoG3IpK2bhgLz4C6SsGb1fBtkhwNfQoufSEALLKTzQYfGfZpjEX6PaIJfbw53cNaeRkiYjj1Wn7ZZ7QFkkeZ0ZP_39lgYE_jGEmmbXI-QzaDlPOYmkFeyB6iPedYO7-VzTJ00bzikLwp4Qy6tSXpHogEhOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avefFjs__jFGfZDXUSYm7UDKsbdqDa_zr00-4Z_56wk46WkommUdoDyZCtW-eMcHFzXD9zNbMt8l3e7UQl_b8J3BBMvB7Ce3tgWSQrmNqtP3Y1fK5r46fuh4qUw_uVGspE3i-NS9pByDVV_X6g_BDMMnnQoHF_g6MdqXx2GyUy59X8VMkW_I-72Ybs8SQQGHmdZbTFNux7JA65lWAJjOT5zJQk2EeEraPJnQjdH0qsP36jlY_FYQKZQ5mQ6g6dZRLP_ZPGufsOsEIJG-MhoKwt5IhcJIYw5oDzS6065hAoI5cSGLceZzzVSvFmVM67EhohyBizRmKfU-ptDDcVo41w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cECzrXsBHWPvLTCXiJYZyA1ha_QY57S7POLC8cLm_LY2o7OIKfzUajv4gT4l3rgO1-x7RCFrIY7u3hOEPSMBNFcJX_4XSNmvT4OMBznhR414ZcySXku13UaYKUOC3QJ5AkTOCXo_AFGFFdP3Vn-5qiQKnyLT2XJmBKtevgrasIvcWsVYDoKrTlDes6rUpVm6OA-L1OptTpOw250Ayl8w-YZmfkYZgMOUupeuN9TWkDrT0fvmAoHi_FUYfBHy9Cuj6pTaW2Y5KODgAhMpQ9xzc3QkfYVsx8H-ianmTWq6zNQGrs1lTY3fI7fD3qEMyO1CVBzEPZXtOup4st-msOw7nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oQhz555ID3L6rJINHcdMQ6Tc3SJtwVMSzojAkCLypK3GBkZ0siiGh-3D-cqHt8nBfYiJQp-N7pfZnSvUFltc5S6WNR458Eguv_yRmGpcBt4VoCARfMhkikow4RiS0hdrio1GJQ7OUAvLqcdRmrm6dfgsI5LuVUe2v_EMk3tzmKoZvsAHuK93q_g80TCSXusCW7JkKXKgMus_k4bwWHozVraoyd8_3sC7Lkn_8gczqf0ifKcVJyw4OuQJV2vVT5YtwKYc20wcUR_6J-xnC4NRhXCyV0M5ayINvO7KlMO69jRdqP62jDkxILcacoJdyFdMk_jBUpdvv9U5YJ6Tlw0iNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AySCZLkDZll8ZOG48FB7kx175VeRwWH7GylWi1_o9D96f9XC_yB7wlu2Avb3MwJ0eRlXIG4srHl5YWMVF5fyFIG9Dzw_F9RCFE_waZsQZeeOjcd0mY5jqi37-ukcTWZa3gaBA86AWiubypi-BBdMereuNF10_nRr8r7bKnbuVZCTNGpqcdOqsntVj-tvY1iokEk48uUyJ4ahFMlB-8iDAXYOe_heSS5nhUgyDyWAFRd7oQmHYOAVEhir70anA8tATu7E2rxrsjh5tu_20dYYpkFxiUzjK8btD-24GZ5DvQp0W9j25jBO97dRr3HweE9FqC4yQU2EBY-7WcL6OpEGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pk-eR_1P8DF_RqlubdkZmO_bg_669Ez1JKZbPhz0aE2wQGXstc-7VYc0huzs5MhqtCkWgznAL39RlxBQsQPN-pHkSeP-Yqa1BDDWRjvHCR_Ti-Prq-7PbxwSvLQILd4h5wyyrqFYic9U-DSm-EaGhdsjRH9K_1lzLtiYgDE_Wz7_BXciDwxg1uIdhNlV_0j3-_oM34mdLkjIN6GtTfM73Of1hUZXPfeZXoKwVZF0Z2NDSFy6Ola-yob4MFHrsjjf2X8p1VSeQ_wcgyyCsnNG4ECNAcdV5F1QgITPkrR1_8C_xUCODhs6S7-kUkaOmEHGRMF0mDfRJT8c2E_N4d2E9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ0ozhdzT20tilVDLaUg0suZ4Dd7I7vvEwwLk3nGvTqh-N4TEzDeWoCJTSIIBESF6dNtBgKGIWos_2EyEwsxDnWWfZ1eseMMl-cV69ELdnc7DShZ4TQefpHxBnCvihN1esVS1SHHq5ZrnDAKWhzn5OOWy2ywH03x_Ai6PbBoFukxWKKz1m-5IAUZ6ptpnsKsOBHlGiH1n2ntwb8e3NIL9UWdBMKFnSOJcXgumSzTzb7DsKYMboTXDJKVfr_twPcLipwFMq8BvqmGJzN2ypkJ9ZnwiqIOm8alh2CBEpdVOhcgfa-YWJeDKFy5t4YgGbX8jNWxIMnLJqi9rSvQzQHU0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن تکلیف دختران تهرانی در میدانِ دفاع ملی
🔹
جشن تشرف (تکلیف) دختران تهرانی در هفتادوششمین شب حماسه‌آفرینی در میدان جهاد برگزار شد.
عکاس:
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/435827" target="_blank">📅 03:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435826">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baab29a915.mp4?token=CMzv4r41SyGU6HQcuLiIwOX39R_0dg2665an2QcVPpLubxY07QCo4R17jkeScdW4uGzSx1O-0KDRg6oxYfHhi8oitG0rhEEQGDH8VCwRKaA0fhIhAC2zjlZgUjaunfUnnxk-Skq3BLNaVyKhNN-2jOm3q3GXHQzkVmUzKi1zsq7cra87BWVlEZ-CPMVFxu_oMXW0liQNLCAG56rUdGzPY8TkeHdtxCXZ8s-L2qKo61Rx6ec_MynbfSY7wdmCvSh_T57Wc3fAufL9j6y70-rb5WUh5nO1yOHxzVSu6GZaSHMDHztd3D1qNqzYFulMV4NECmTXqfnROizc_phkIH3Bbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baab29a915.mp4?token=CMzv4r41SyGU6HQcuLiIwOX39R_0dg2665an2QcVPpLubxY07QCo4R17jkeScdW4uGzSx1O-0KDRg6oxYfHhi8oitG0rhEEQGDH8VCwRKaA0fhIhAC2zjlZgUjaunfUnnxk-Skq3BLNaVyKhNN-2jOm3q3GXHQzkVmUzKi1zsq7cra87BWVlEZ-CPMVFxu_oMXW0liQNLCAG56rUdGzPY8TkeHdtxCXZ8s-L2qKo61Rx6ec_MynbfSY7wdmCvSh_T57Wc3fAufL9j6y70-rb5WUh5nO1yOHxzVSu6GZaSHMDHztd3D1qNqzYFulMV4NECmTXqfnROizc_phkIH3Bbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هفتادوششمین شب حماسه‌آفرینی قمی‌ها در میدان خیابان
@Farsna</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/435826" target="_blank">📅 02:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435825">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6Fu5Q5NJ0eY4ffM5ZL8QMh2Iwe7qM4FxhFcocYA--hPtqsy4wtzn9KeHDltNzhBLgc6CqhY7AmepT4BJMcQhUHy8XeX_TsmYuNALGbW9qKqbOyAj8yAjKt0-hieYwuLxvVv9AgMNGJnpjh_MtIQ8slfUNkngf5a8CIF7GVtiXCtjICVtsuLlJ9lwj9nsehB31ZjOv9rnXa5WjKbmSAZNnFYmMF0eHCK-XQJlLxhD4ihZMTKPZtaiq_VAael3FEi3ruJ0nGZ4ZQQ6SmYRGwMSujHXRNgTCu_sGJ3HT2yLhitXxDoMrREEuZhm8T__a1zZgf6ALaije2uU4Z7rj7qYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب‌نشینی ایلان ماسک مقابل انگلیس
🔹
شبکۀ اجتماعی ایکس متعلق به ایلان ماسک، با انگلیس به توافق رسیده تا نظارت بر محتوای نفرت‌پراکن و مرتبط با گروه‌های افراطی را افزایش دهد.
🔹
ایکس متعهد شده گزارش‌های مربوط به محتوای نفرت‌پراکن یا تروریستی را به‌طور میانگین ظرف ۲۴ ساعت بررسی کند و حداقل ۸۵ درصد محتوای گزارش‌شده را طی ۴۸ ساعت ارزیابی کند.
🔹
این اقدام در حالی انجام می‌شود که دولت انگلیس طی سال‌های اخیر قوانین سخت‌گیرانه‌تری برای کنترل محتوای آنلاین تصویب کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/435825" target="_blank">📅 02:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435824">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc9a447c75.mp4?token=EH-51Cg-VWABvf_EC3wWhhSa7hfOVoujDMkaNTOs3fF9yAI2OjO-PVGMbxN6wDJ90mdZZKxWEghVUV2M3eoYDLpDUGVLfy_E7XkW3Bq6L7NvWejYX90iywgwTXBHTXovQCEptS9Q-_7Vu1cViPObOLcQLigSMtGZm7XLWciJfUh3jZ9FmBIbS3d8NDnJBc6VRJGOjBnzQtVX2nKkKagBOOsnkn-CPt6Rj6dq5PpPBtiRTDEDSypKDtj-o8cibeMfgcfoa8jq35Iv9OYV5hqH5wR7SQzVKD7a_n79zYFgwPjum_B3Ftr1ysqgne9kOr1Wdt6syfaiAj_8LZhdQTKjbjL1sh6Xbtkxxcd4_PeGmGp3uAJUUvCao7xw_OS1y0kZRvwAYOf9Rw0TWlK5EVZQmXwGaaxwpzZjzR5TwYWltlcOtjCK9sbVU7fJNQtrCtXHxg8Ula_K-QbVBhXR2T3N3bjmQVCJvPyg_5HLLLxDSJ2Ecu5V0p1z3I5Z7h_C537twLmLNs-xaagS9YwepC4M6Elh5AZ_5xQ26htJy6WpKYdhcxRxeXE1rAg4WEGox_uZpuB0q8FE5sbZKDbvnWQkWn-H1liqhbhjGGHsCfp7Gn3XNZXre08hPr2jnapfwF1198gtINvq9vT2wnmTrKD1B3zAiiKLTFujtZy-CBF60qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc9a447c75.mp4?token=EH-51Cg-VWABvf_EC3wWhhSa7hfOVoujDMkaNTOs3fF9yAI2OjO-PVGMbxN6wDJ90mdZZKxWEghVUV2M3eoYDLpDUGVLfy_E7XkW3Bq6L7NvWejYX90iywgwTXBHTXovQCEptS9Q-_7Vu1cViPObOLcQLigSMtGZm7XLWciJfUh3jZ9FmBIbS3d8NDnJBc6VRJGOjBnzQtVX2nKkKagBOOsnkn-CPt6Rj6dq5PpPBtiRTDEDSypKDtj-o8cibeMfgcfoa8jq35Iv9OYV5hqH5wR7SQzVKD7a_n79zYFgwPjum_B3Ftr1ysqgne9kOr1Wdt6syfaiAj_8LZhdQTKjbjL1sh6Xbtkxxcd4_PeGmGp3uAJUUvCao7xw_OS1y0kZRvwAYOf9Rw0TWlK5EVZQmXwGaaxwpzZjzR5TwYWltlcOtjCK9sbVU7fJNQtrCtXHxg8Ula_K-QbVBhXR2T3N3bjmQVCJvPyg_5HLLLxDSJ2Ecu5V0p1z3I5Z7h_C537twLmLNs-xaagS9YwepC4M6Elh5AZ_5xQ26htJy6WpKYdhcxRxeXE1rAg4WEGox_uZpuB0q8FE5sbZKDbvnWQkWn-H1liqhbhjGGHsCfp7Gn3XNZXre08hPr2jnapfwF1198gtINvq9vT2wnmTrKD1B3zAiiKLTFujtZy-CBF60qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج هفتادوششم دفاع ملی در رفسنجان
@Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/435824" target="_blank">📅 02:23 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435823">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تداوم بازداشت ۴۱ عالم شیعی در زندان‌های بحرین
🔹
جمعیت وفاق ملی اسلامی بحرین: از زمان قطع ارتباط با ۴۱ عالم شیعی بازداشت‌شده بیش از ۷۲ ساعت می‌گذرد؛ امری که نشانگر ادامه جنگ سیستماتیک علیه شیعیان در بحرین است.
🔹
رژیم بحرین همچنین ۱۰ شهروند را در پرونده‌های…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/435823" target="_blank">📅 02:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435822">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPElXj-inazforfQcM0uyY67zYGSCJapYunhQqyl8R-JJfm9VPIZmmlJ8lJMDlNjIRqg3tkkjLH-O8pz5QUEhChtaaXP8uphmAU3oE5ry9whS-ga_8iDuHZGAHjZbO0kuqGVY3KEIUSAALcavtr6CVrcI16NkAU88JW235pSo216y7nAMEQX04x9FlwybrfTbEDxl6EkkqphjSPPPkeaiL1xYtqxWbSLrfmoV1tp6UqUB8Ivb5BIvytzaRrHJELYGHE85dCoikt7RhRU5KN7tSFmCfedO6x_3gtrPIeKs6N1TqAM-CYjuPTEStSHW4ZgTnrGGmHom-X28cubGb2Kxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین از قطعنامۀ پیشنهادی آمریکا و بحرین درباره تنگۀ هرمز انتقاد کرد
سفیر چین در سازمان ملل از پیش‌نویس قطعنامۀ پیشنهادی آمریکا و بحرین دربارۀ تنگۀ هرمز انتقاد و تاکید کرد که محتوا و زمان آن مناسب نیست و تصویب آن کمک‌کننده نخواهد بود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/435822" target="_blank">📅 01:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435821">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8920b53738.mp4?token=A9BojfFmUsLgn0LyxmbgVG35FzO_fnM65EzbVVbRH-4DMl4XWk-Gv2xVGC0MUaCQX8wXPrYL-IePDODx76pwJj_z5VCsTmjXcVEE3r1HsOGk85BksP62EZ8jOFEUrTADAz3UnVFJtEvkuYa_c_LQwVWQjzkH3FYiw08z6WNcNdScls0r5J2OzR5XqLzjJFS3VKg2ORDElMAICEz_9h0gFnWe_saAQmNeqfb3crnXohPoU1xXywWZQJjjuH8Y8sJAcb8FNVjl_sIHy0D3CuDHhpcQ1xHTp0lrewHIW250DMn94nOMaKwWoVi5YsIbjRjrgoj1qWuiZYQJpWTZ7pKKhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8920b53738.mp4?token=A9BojfFmUsLgn0LyxmbgVG35FzO_fnM65EzbVVbRH-4DMl4XWk-Gv2xVGC0MUaCQX8wXPrYL-IePDODx76pwJj_z5VCsTmjXcVEE3r1HsOGk85BksP62EZ8jOFEUrTADAz3UnVFJtEvkuYa_c_LQwVWQjzkH3FYiw08z6WNcNdScls0r5J2OzR5XqLzjJFS3VKg2ORDElMAICEz_9h0gFnWe_saAQmNeqfb3crnXohPoU1xXywWZQJjjuH8Y8sJAcb8FNVjl_sIHy0D3CuDHhpcQ1xHTp0lrewHIW250DMn94nOMaKwWoVi5YsIbjRjrgoj1qWuiZYQJpWTZ7pKKhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ایلام خیابان را به میدان اقتدار تبدیل کردند
@Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/435821" target="_blank">📅 01:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435820">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fin4UTIaEU-hanZG6pvix8IJhoPby7d4-f2Mogp4YzH6Nkzq396z3w_rMic8eDFSOn_ioExrWBobOdAqUGavGoOXE7KWfbZGKurvFSyljz1zDjCJyp3pGIVFt8H1GHWq7MfPZc7V_hecdq_vtP9mM_8tosIsjuhYw-UY-BCEUnIK2KZ9uNXbwXPsaGiA-3ZN0xcUZ_kJ9JbQ9uZqLjSJp41D7hv2xp1qQkNsi8fbdamEYzgiCITSswyGlG7hbuT2l0nAmsRibp04c4SWMxDS5MWNHOtZ4NOxIIXUnG1Pge2xsqjr2qiGeAKaSthAizSso5qSaY6mtHn2tvRWx1vH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته بودن تنگۀ هرمز برق کوبا را قطع کرد
🔹
صدها نفر از مردم کوبا با حضور در خیابان‌ها و روشن کردن آتش نسبت به قطعی گسترده و سراسری برق تجمع اعتراضی برپا کردند.
🔹
کمبود سوخت عامل اصلی قطعی برق در کوباست که به خاطر جنگ آمریکا و اسرائیل علیه ایران تشدید شده است.
🔹
وزیر انرژی کوبا می‌گوید، ذخایر سوختی که روسیه به این کشور اهدا کرده بود تمام شده است. وی آمریکا را به خاطر بسته ماندن تنگۀ هرمز سرزنش و تاکید کرد که قطع جریان نفت ضررهای زیادی به کوبا وارد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/435820" target="_blank">📅 01:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435819">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rktGFbw1C6weWAq3kvvV1Vbq0UwHPFMBoGwQf8f5wHvwd2_lHDTWxzAqiW9YbCFwAT8DYatzmX2tLz7c1H3hpzHM7rr2AYFHB2gBzYXTAxacpKqQtGlefOHPURGAWrobRivPvfiz-s8zyJk_mjzBvvCgNDQTLe_rqihrBHJo0jPWA4yvglBMgk91pxVFJdprXR_hyZhQwBvl86ZsjvAL9XHSfMXTHpUTuSyrrL9KdbRpB57P2RNaGJ3KcYsci75PYej7ec4dvtAzH3XuMB2wI7uRXQmARBeAsnQvYkG9dNSA2iLVR4_RY77peWtNbYOm4O8YVMWjrOElo7CBRxpzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز یک قرار تازه برای تعیین تکلیف امتحانات نهایی!
🔹
سخنگوی آموزش‌وپرورش روز گذشته اعلام کرد که «تا پایان تیرماه صبر می‌کنیم و اگر امکان برگزاری آزمون نهایی فراهم شود، انجام می‌دهیم». تاریخی که تاکنون چندین بار تغییر کرده است.
🔹
اولین‌بار سخنگوی آموزش‌وپرورش دو هفتۀ پیش در حاشیۀ نشست خبری‌اش زمان تعیین تکلیف امتحانات نهایی را نیمۀ مرداد ذکر کرد، اما سه روز پیش وزیر آموزش‌وپرورش، این تاریخ را نیمۀ تیرماه عنوان کرد و حالا سخنگو، پانزده روز به آن اضافه کرده است.
🔸
دانش‌آموزان می‌گویند که در این شرایط بلاتکلیف هستند اما مسئولان آموزش‌وپرورش به جای توضیح دربارۀ تغییر تاریخ‌ها، می‌گویند که دانش‌آموزان به جای نگرانی، درس‌هایشان را مطالعه کنند تا زمان امتحانات اطلاع‌رسانی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/435819" target="_blank">📅 01:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435818">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ff319359.mp4?token=XO1OducE_bBz9gme5wOqObEXiYnzaRGSXrtkE8hGteO_FGRcg5jNmrEwYja5MZ-2uT4ZpPPS4-72rgrLUkzTONnUT6IhiRcb9-YNJbOX_BXiT1lZccQLiEO0LThTfBgYnBs607PFKrkNUPn6JXwtd1I4opy7XwuMSjE-ZP81U_9nyW9CaoI9LIxJ55uGMM2AWO19jsHDMRdLyz_1V7XytHUjXZcX2bWlpa8RcBW0bGgJd26heozZ1LEzxE0_eCqYVCNAdN8DnTi0a4HQcKalpsC5DYQzf40c08cHxv6KADShZUPtiaWgryMA-a6sJeyqum9bwi52R2IQeQUV67UZfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ff319359.mp4?token=XO1OducE_bBz9gme5wOqObEXiYnzaRGSXrtkE8hGteO_FGRcg5jNmrEwYja5MZ-2uT4ZpPPS4-72rgrLUkzTONnUT6IhiRcb9-YNJbOX_BXiT1lZccQLiEO0LThTfBgYnBs607PFKrkNUPn6JXwtd1I4opy7XwuMSjE-ZP81U_9nyW9CaoI9LIxJ55uGMM2AWO19jsHDMRdLyz_1V7XytHUjXZcX2bWlpa8RcBW0bGgJd26heozZ1LEzxE0_eCqYVCNAdN8DnTi0a4HQcKalpsC5DYQzf40c08cHxv6KADShZUPtiaWgryMA-a6sJeyqum9bwi52R2IQeQUV67UZfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور خانم مجری شبکه سه با اسلحه روی آنتن زنده تلویزیون
@Farsna</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/435818" target="_blank">📅 00:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
پاکدشتی‌ها: حتی در سخت‌ترین شرایط به آمریکا اعتماد نمی‌کنیم
@Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/435816" target="_blank">📅 00:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435815">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhfe7XIzst-eMOjIxY0hz31czPyp3waMMazChk6Bomlr8ug5J0ELQEa1FBgTmRkO2Wylb8FhglMuXZ7B-atD55i0kJypl-u1XZYuGMx9RcKK-LabiVsjPh3j5Drj9DKJfXHAMQELaJxW45IGq0ubRQWnwtTZ8hnKsMwikbRECzYknyMl0L_XjGebHdO3DEd7TXtOQSxtT5vvskkCYN5SylruFN_Y1OGnQs-tnvmJa7nlJFukL89PuGRoXxKnXYosVveu47E8B-ScLUVaMMLDP0KAWiocsEbp4cd-rx9k3QJkh3SGRr7_XlNOJ0kNwJSKUGzR_AKaDXFJu5JTL1XUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش عراقچی به تبعات جنگ ایران بر اقتصاد امریکا
🔹
به آمریکایی‌ها گفته می‌شود که باید هزینه‌های سرسام‌آور جنگِ انتخابی علیه ایران را بپردازند.
🔹
فعلاً افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید.
🔹
درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.
🔹
همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است.
🔸
تمام این‌ها قابل اجتناب بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/435815" target="_blank">📅 00:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435814">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
حزب‌الله: با یک اسکادران پهپاد تهاجمی، تجمع خودروها و سربازان ارتش رژیم صهیونیستی را در نزدیکی شهر ناقوره هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/435814" target="_blank">📅 00:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pP4c-xSBttTIVk7AAVdmZYB2LQADwaSI2SxMK1XUyJXA68Jk6z0nTJi6HR7J50fhtpOez-jE4-d7bdasOTHV2MS673Rlnfx42dj_IVFbAlT2pa-iuUQ5k9e1STMuaN2taDuvgLzfA6JCg6tfSBQjjbmI5m3oBP5yrcf8AOnMDcRxCExNbPLVsDGNihAlgElWl2DOe_L8t317xNNmQ1w2CZxOcrH2pHC3q_8BKBFioF4WGuG_4lGWM7B3Xnd6gjHT4qkrytzyrCxsy9XDstdydaxCIjr-uI0E-QsQJjVRof4pSxNM_MBCEJfSTeiP-DLJcvecSq9F7ZfOONg1JgDMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiCRHke-4FVeZRsOdhaHVeIAeMhe4Ry63hYPITnhrqL9qYuF4yPvEV0vlM7LG_2ipJdY4PzhkQtvmIabtKs4wCYRP4T8tpRV5MvR7pmfeNg1EAdfIE7Xgr8_-Yy10ULaIoqnCCgA2jpKJSK2Dal02hQ1Yh3HcKwzEyjhQJRP-GEdl0iLIP7cRsnNKUl2aReMw_LMfuwS-rghvAcV70PKA3TmuUQDDl0_Lw5HN0ytKzXrN4d6bckW-kZArSL3N0dr9_ozYA--6rvKsdWvAeKlXPj0dBwJdrQV1PPizzVfOrF4La_br2iu700_D_kTvtsDtw2zIxmVmFAxT3Z_HSfJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b8IO1_BXExp4FVK7_a62PiSGvNZt48UmyBwW7-UDpy4W74oB9XFc8CAb7V-csjE1RL-w0L_tw1b1PDtss7dHhOBdngKelAFP3M4KdIXeEqlbCTrcfqbtni7VWgv5u_P9VVmvO-0n0TYpK0419LQazZ8mrC6efkKrjy9VQ34R68gSWbHcjXw15xEwzH-A99OR4ZBhlxnz_DXnxxlEUN75bd9fJ_W1fwn6UwpXvQaqoFrXzJIPT7gqeqaf6e4AubhTbLucJtPooM1gkqsFhRIBWk2_BadSzYtarVwBTDZznFFOpJ0H0Iba04JSa1PYgglTQwiDZrNdSrR59UB1ARZNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXte61syjCbwHBjGRGIs1K95dMXBTA57xhLoIoTPLT5d-bzwTDOG-dGiLCB7_lNob6Q6VUsMoAdFvUpM4BvK-oAHh7rupbPTDv3MN39xQPqJgkTUEbbC2TOuGpPRAdEhS8wSh_PdwJzvKOdV-9jsQxjU4cPuv7imYabPNvhPVPz7_VxI48P_D8Nvy0BixxhgC_9FQLYBxXQFdgKUNS3H2DDxYCG2E_npnfiYgdUcdJ_lUVBC4A74vI6tMboZk8HYolDoP0HIm1TiG3QN9r8OZ7WlstKV2jc64pIe3H4LpiFZQIdJds3uAp_FUXDDlkG_f4DdxNG9-rohbs0A3AbNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yp3Tge9Nbcdim6H7PiKzyUeUBuEm2tk2qbS8dcLxkI2hvX3E4xpU3pVA4OSEGlpZLg_ct5TA4Ihy3CNg50yZLBPqdZu4CWTvnjYzPQCXZ5M7kx4T_M_XXSzPbnn6YM4f46xi9gNW9rhGtwbNZOB3qZuWhRUKRf8o-8fG6Mfz0y-k4E1nWRkvOWLPZxSlyqXpXj9kwqegpj4OoZNqgiz4jJ_xv82GJ7PNMYR65ppIsIlahBy53bfG7_zuGbSgt1jd7a0USgmmSa0WH5sr2FbejSs-L9rZ3133i2hPyahGqmmpp1wlSRR6ElfHI-27_qTqz-lgRn5VO1E9qNzXsShF9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۲۶ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/435809" target="_blank">📅 00:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435799">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rm-8dzJnDu66yHEhyGUMmCmEp-2sqQHDFukHg-YneodEtm3qXnmUlBNO5yBaRrRMnTuOZHtVHfUfyF6GDzKvfaL_i8xKk2qc2-ATQETR3OvnX1E4bM9pPOobMNGosd3KyP4Qkdo9qXeyU794s13lRosTJLlaDXrKSa8HTz3_1mW_NEBlFY_vPgVNVagxX7vBG6TLfwFY9CKd0IS7CES_-Aor-RIhWhsCSY70DU_pLnJVzpTkW8ayXtSkhyohOt1vstyy-Z4jKhcs3gI-5O1lgdqMUXA8lIAXmuqi5yrYah1HsqDLbdTukaEKH75wO2Z1MpidvS2uJ3AzIInWTKXIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOJiim5OfguloUJYzsAq9Mxtgsj10SqqgR6sVMIqpoqsJTpmIB5Ip17h_KQMlUeiE-G8aqPVV8Q6pxiMKE6TkauQUE12NhUxf96as28AUGc1PoEdA3HYGEMicrH0wh5BL_QH7OiyzHrEBn4LnrLR_jRSQcW5Q3xMpL5o4zyulSPAJSXx5MbidHKpEM99PMaJ7_1LoKk7EzSrWZq9oj2eTLg25XKVKDnhmwJcW_kaGWoMnx1xlVCAV7XQRLMMfiXu7iwlDVRVzbvFjPg8w1ZBYqK0j-cGh_xKLI8ZXdpA3v-V3tft_4GvZ8Ngk6jZiAusOJxG4NjSxCkjrVWHomY9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cGli6Alkh69xnXZuPlSspmo9eh2cDiNwQYsNnoOiL-Z1d_hGTfWXZIQNimZemmEA6WgXu9r8HHDNVnEalDqX68t_gYz2a-Okxik5h4nQJoGHG_eawdmVqp5hAegm-mZBCm-78d8o7rdJYCv_EMuw93XWYEqMA6i0P_KDbKwPie5blIHnEOm1HZ1fPvplXHUDugnyHLsiBctNiwGwrwO3Zt77ZJ0Eivfk6IrxRB5HJ8_fxq50elyCrv9ypL6cKknadJ0V-yEmwsZ3kj97909Ypd7MO8LVsnZh5YloPAdvpm_kWVcgROCSV17_dpxxe863QO1u1AOP7MVT6xlH4Wk6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzdABEUr1LeRRY0q5rZ_97_oMclNApqtAvRyUVN_34RkpJaQQFgzn-iL7IQcu0nGyx21SyVAWHEU_79ti2Kid7GhY26ToxmN895N7liRnqNgjXYw5Mm1tRRctyf9YbLOiyxfh3w9u9Qj9jkwNVnHx4m_M4KIVs7_XDTdsPeJ8vSoVSB4kpIot2jVerJjPJhGeh6IIK4cVCX0_iwxNqhqvfhahDF2DFkbeNgWuepjZUZ7Op4YVixVU6o7zCXL_SdMaPHLW2HOfETy9k8J9IfKPUWEpaMomcJBRYLn6CmkfLu0jVj9zt2ukwjiJycUkH034y4UMpk2Vo0qT-7fyGcI2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmTuFS1W_fUQjxf4OLrPgjV90Qd7WTi2_8u1h0u4-PqKX4iEWZPd52PQDxhk-CkJSrYM-G_BVpnaNRuBOM1aRaj_MnjrI2E99K3l5vHvuB8H_tT0OGRhImeVW0bIy3SDSHuN8VcNy2FMQf-tTumVsI1z5IxS7ihrLC1UIWPPBVynlYvR7nxTAR2Y7pl_S7ptkk4qCTC0PKfwChAKlP-SCPijuLfc8tgYXQhk-XyH488KDILFu-b_aGseOXuJPOQcM1J-xUVYCOErKshWDHffM19_6leNLB6hMhRN4wuHROO1KkofGrLBqCMEsF4tEpFbplygGu5T0qq8Zq8juAv0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAfH5zHJEC0nz_2Gb_KptU1ru14GVxsIG4s5LHeiCMuCEK_NWcshSHX9UhEGLOI5AoF2So29ssSMvTSKBPSFKDBMri1x8VFAhCHh9glsnoti6FqbWIN6ZM3eu8NwbeZcbTFaTcon53qdSWcOOwvblWJCXdk_RDpkzrjBdKrmWTwUF0GVZhmRVnoWZr4SS2N4pCHCSIw6sTYntjlrmUfcnZ3idJ4KjoMUcNXmyF3Z5-uZn5PU_3bhtgYT_yd_b-yxgBQ21IpGEf_9fw6fK-4de9VqUYbFvcZ3F-ZWIaT7oIz2j8BRfNnMxGO9F8odSareUZfMFYBOYUKNaaAkumjG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_Jg6ZjYk2Tw437sLXGfD3DXw5Q5hREm9OiEKE6xqyBoLihAQEm8Nf6qy5tSkReh3BbVRjPoaG4M0-aQRCn-iYdH2oWjrjCKr5yL4RvNQuif5THAzIfnUJBugUPDrFHHeE7JRE1bZiFo0_2e_xc-ndmNNGgaQ_37_h-s3Y-mot3Q8gDk3dqvsXCc7rt7rk8LPp6CGRQr8S4fNSZOAkZChFcJlwCxYCKvSDp_914S2M2AWRGeOPMzeCLaJXWrTGh46GoAA_FlAYoUoWoOpVoLMJsj2vaBOICNpikto8iYqrNs9LtIL8rPoz7AqWWHv8yBe3QKI-L2wB-b2aROp0gr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTD6_u5wnIN1E0stb0i0n6uzWt8xlm1YaazgDECLyhSq5zwl-Nvhjw6fsjvB6jOaYsmXImBbY-FpmSBpJQccvMIDB8jg3RgoeJCAWw5CQCiSxw3l9dHVlPhhLitRVvZtX698FeZcyHXwXN9zHlSzMHK3KQZPUAqDPP7QE5YYDG_-ibm6p5ksQnybkCYKx640VAbwQoKwefXvqRR661nrWC6Mu1kVsHQEjEfh396LhAJcJsQqHk7qBfMcH2ec2f2ZPoUWaiJXNQpfSHzS3R8V-xsIkjmvTXD8Ak_woufJVMrESxF9U57QcEILUBSSe3BUUqpzPt10bLjaTQ3s7wGXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBymO1F5USnVqEi8Sh-BQWpl0a5El4j56yokvSUrIbB6J6j48UiWa2ESRiMJaik0fa87-y41D46j4WrMv2MKBzvTBSoRlcQuZvlm3vX4v3-SXhK2e6JFEntH-Nk3ml3D-arP7aS8Kv-MvN_64GYpeg9CEjSSiqbC4RBOj-auHySYhFnGvExs6trsidED8OFqBvPzkFw-As3uWCMWfU1lQaDRM7t7mZ1rdnouN7r-T_jGhDXHoSOcSbAO69TvzzzLUrfAD3nbjqkSEHpWsnoepF07w4qZaQZlW95oFCP3GKXtEXl3BMFNT0syCOx2cEHSiGfTQ8Xd-HzMsGTNBCELOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mknBmLoZqaC675gUP1_Rw7uRFZpDBZvtIa3iM4oYv4nOjQKAHFF8CpMUN0CPokH9F1OwIy5Zjg0PoiYYQ-AzPhm-mGVw1wU-uocV3AmA4dG92leMuadvZN55jwnol7WJvl2vYIfFr6_zBV8wGGAk5m8kam4dUiahrlUrc0rPB13zs6idGKz4BN8RhzsBcyAeB5jifP3T8l_B3wIL5arUfvDwWddI7jQc-jStEGievtiS4jcUrYSFjhmLzPRLYPiUZBsGOECNI7_IxnpzVlvFNR9d2ZIbFvbuq4BZHRPUzr7_fG6wyXnyPhPAsW1fQeeds6oLM6AN8qPcrCfpVLObIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/435799" target="_blank">📅 00:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435798">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دومین جلسۀ مجازی مجلس یکشنبه برگزار می‌شود
🔹
سخنگوی هیئت‌رئیسهٔ مجلس: دومین جلسۀ مجازی صحن مجلس با حضور وزیر رفاه و با محوریت مشکلات معیشتی مردم و پیگیری اقدامات حمایتی از جمله کالابرگ، یکشنبه ۲۷ اردیبهشت ماه برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farsna/435798" target="_blank">📅 00:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435797">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4b4be486.mp4?token=eC7PBmMsKnpwb5PJ5QxIUSSsmj-kbNHyMQlx4sWpkW_j1NkDlD2icOaYLCZRjlL8TmeFFfrjRozN425FB0OjI926A38FqAG9ac6hoMDRKloPtkA_iNrNp4cDcHxOxyoSDKg9KKoATYotbk8hPyAjiKxTcsBzVu66ur0G76V7EfU6BR8cnldJKM4Cp3gLpiB48XdSvHHuyLHgoppRKyAxXFQrmiKy5G9fUTbhTK3d-LtyUOTCHkXKY2EtCi3G0JCja_40GzIM4DyoorJANk6cB41nVoT-k9yXF4unDypPwtfGDw1b57qg4_pKQtshf6tQKWJjmNKiG-vZ1ipesFh_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4b4be486.mp4?token=eC7PBmMsKnpwb5PJ5QxIUSSsmj-kbNHyMQlx4sWpkW_j1NkDlD2icOaYLCZRjlL8TmeFFfrjRozN425FB0OjI926A38FqAG9ac6hoMDRKloPtkA_iNrNp4cDcHxOxyoSDKg9KKoATYotbk8hPyAjiKxTcsBzVu66ur0G76V7EfU6BR8cnldJKM4Cp3gLpiB48XdSvHHuyLHgoppRKyAxXFQrmiKy5G9fUTbhTK3d-LtyUOTCHkXKY2EtCi3G0JCja_40GzIM4DyoorJANk6cB41nVoT-k9yXF4unDypPwtfGDw1b57qg4_pKQtshf6tQKWJjmNKiG-vZ1ipesFh_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایلامی‌ها، همچنان در سنگر خیابان
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/435797" target="_blank">📅 00:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435796">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRIswPBxkyMhNcKilO9JZ2lgAO7rQHAq3g_95w9Ib-00CWnxKmLSsIsk8ZbDYeeg5Cj7OP-tPCmrNiN976LBj6Yg1VytLFGmQiIP8yTslJ1JAzPuUdUG4WIu4FQvy-xB897LwBpb4rjKD1Hyyxu5L4ct29rfYbFQfYbiIQnj0y3F5OxDyWjf7r2O896ivtMsyIToP3GhcNYX6-D2eo-z8WuyfLt3BtvG28SP-a7lfWpFG7Ge2WYdfbKBpNtVoFSAIV2lM_ivBk-6GR4hw26eIygzbScaFi7zxBsktlRs2DNS6s7Mx762prBu8HoNTvQrDClY_nCX87jNVaGbz31LoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاعردزدی
🔹
روزی انوری، شاعر قرن ۶ هجری، در بازار بلخ قدم می‌زد. ناگهان دید معرکه‌ای برپاست و فردی ایستاده و با صدای بلند و شور و حال بسیار، قصایدی را برای مردم می‌خواند.
🔹
انوری نزدیک‌تر رفت و با کمال تعجب شنید که آن شخص دارد قصاید خود انوری را به نام خودش برای مردم می‌خواند و تحسین آن‌ها را برمی‌انگیزد.
🔹
انوری جلو رفت و از مرد پرسید: «ای جوان، این شعرهایی که می‌خوانی از کیست؟»
🔹
مرد با اعتماد‌به‌نفس کامل پاسخ داد: «از دیوان انوری است.»
🔹
انوری لبخندی زد و پرسید: «آیا انوری را می‌شناسی؟»
🔹
مرد گفت: «چه می‌گویی؟ من خودم انوری هستم!»
🔹
انوری که با لحنی طنزآمیز گفت: «عجب! من شنیده بودم که «شعردزدی» وجود دارد، اما «شاعردزدی» ندیده بودم بنده خدا، آن که شعرهایش را می‌خوانی انوری است، اما آن که اکنون در برابر تو ایستاده نیز انوری است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/435796" target="_blank">📅 00:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435795">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6e8c5970.mov?token=btgikUhyo3ds6lPnrBAwD7ZUHLSOzoLMNSfZzQ95xylgGyFPUHt1OBQcKNDQvxImIj3Fq6VlKi01WciA1udrYyHK6ueO2CWfBj0CuxbbQtLz5EVfMH5jiq2xpZyc8oZZ5bFgyHuGWEnvZfgt6v0lrhAYTX_of4_jxnxmnvuKIHie1VB9IStuekVLeBhwt23RKO5fkE0UViirClvQF8goZhNfJxbvTYHbrJyLzwG4V0jy7ULOHFwSZvgGBB7rPRiuutgz6w-XAU7znSSsc4zg7RCD9DSvGSkHhneheHGPq7ivr4dPnDeW2bZbtpusZsj-f_pvmJMEYoROlnUJ14taIIOA3jRgfiUVKOPPFJjZuF4skjfQqneX2laa4kWJgxRu-7pdx7nE5e_cTYLu581AMkEVNKZrj-yugEXsAGvWS28qpas2n8CARFqsnZEGTnJR_PMsuLin3M-M1tC28ZJhfUkYrDeYQTgHpqaZRqrxDQpMBW_O8yoOoU04heTYUGzoWRQq-E_P12SEqKNWh-hMouqwgp6sJdIGCx4oLl3uQe_eodVtqOM8NxnGWHwqCzHf3MCv__4TYIgdWUEjYJskJUE7tCvfQEkgXZYJllWNW7d07PdZcMiUR9cS1QchLe_3PkyyWLDPbWlhKquZp0E9WK2tcMcwLgcxSTznpSFLMzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6e8c5970.mov?token=btgikUhyo3ds6lPnrBAwD7ZUHLSOzoLMNSfZzQ95xylgGyFPUHt1OBQcKNDQvxImIj3Fq6VlKi01WciA1udrYyHK6ueO2CWfBj0CuxbbQtLz5EVfMH5jiq2xpZyc8oZZ5bFgyHuGWEnvZfgt6v0lrhAYTX_of4_jxnxmnvuKIHie1VB9IStuekVLeBhwt23RKO5fkE0UViirClvQF8goZhNfJxbvTYHbrJyLzwG4V0jy7ULOHFwSZvgGBB7rPRiuutgz6w-XAU7znSSsc4zg7RCD9DSvGSkHhneheHGPq7ivr4dPnDeW2bZbtpusZsj-f_pvmJMEYoROlnUJ14taIIOA3jRgfiUVKOPPFJjZuF4skjfQqneX2laa4kWJgxRu-7pdx7nE5e_cTYLu581AMkEVNKZrj-yugEXsAGvWS28qpas2n8CARFqsnZEGTnJR_PMsuLin3M-M1tC28ZJhfUkYrDeYQTgHpqaZRqrxDQpMBW_O8yoOoU04heTYUGzoWRQq-E_P12SEqKNWh-hMouqwgp6sJdIGCx4oLl3uQe_eodVtqOM8NxnGWHwqCzHf3MCv__4TYIgdWUEjYJskJUE7tCvfQEkgXZYJllWNW7d07PdZcMiUR9cS1QchLe_3PkyyWLDPbWlhKquZp0E9WK2tcMcwLgcxSTznpSFLMzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با هر حجاب و پوششی که داریم، پرچم رو بر زمین نمی‌گذاریم
🔹
شعار امشب مردم در میدان انقلاب.
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/435795" target="_blank">📅 23:59 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435794">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
جشن ازدواج متفاوت در شب های ایستادگی مردم مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/435794" target="_blank">📅 23:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435793">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">بحث در دولت درباره افزایش کالابرگ
وزارت کار: مبلغ باید افزایش یابد؛ سازمان برنامه: پول نداریم
🔹
کمتر از یک هفته به شروع خردادماه مانده اما هنوز خبری از افزایش رقم کالابرگ نیست.
🔹
نمایندگان مجلس از پیشنهاد افزایش ۵۰۰ هزار تا ۱ میلیون‌تومانی رقم کالابرگ صحبت می‌کنند، برآوردها اما نشان می‌دهد، دولت تنها منابع افزایش ۲۵۰ هزارتومانی رقم کالابرگ را در اختیار دارد.
🔹
سال گذشته بود که سخنگوی دولت وعده داد، خردادماه رقم کالابرگ متناسب با افزایش قیمت‌ها بالا خواهد رفت.
🔹
اخبار رسیده به فارس تأیید می‌کند، وزارت کار در دولت، افزایش رقم کالابرگ را دنبال می‌کند اما سازمان برنامه مصر است که «منابع لازم را نداریم».
https://farsnews.ir/Economy/1778872819925622102</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/435793" target="_blank">📅 23:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435792">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gei7SkgW78NVj8aTyF5UhVZzoLzAAKGbb982Ricom3M5jATJG68XPEEY46RLmKHb6zm-zuzrisa2XiqcZ2KHSdXW_yQCtJzk53knhF8n88J8oPtKFaD8oXn45HB4kLbpWENllEsb9tkKzxwRNCpOA8r2aL43fTpAksU_flsVS-7gwhI7Z1C33zHy_T4PuEYcXR36PXJuku2ik0yjeqDW4qJ3jtk6LqyCdqkBCDJmsbwh1sVk0URn2IThK5M9IiUX7_jGpHsff2BWNt7437hWnuZ3EvfnLLr1O6jgDBw0hC7jw_1iYwh8P10-p7utvwDAsoAvJgd9mXtxn4l8-97-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفوذ هکرها به سامانه‌های پمپ‌بنزین‌ها در آمریکا
🔹
سی‌ان‌ان:  سامانه‌های نظارت بر ذخایر سوخت در پمپ‌بنزین‌های چند ایالت آمریکا هدف حملات سایبری قرار گرفته است.
🔹
هکرها با ورود به این سامانه ها ارقام نمایش‌ داده‌‌شده روی نمایش‌گر مخازن را دستکاری کرده‌اند.
🔹
کارشناسان آمریکایی می‌گویند این دسترسی به هکرها این امکان را می‌دهد که یک نشت واقعی گاز یا بنزین را از دید سیستم‌های نظارتی پنهان کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/435792" target="_blank">📅 23:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435791">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
منابع عراقی از حملۀ پهپادی به مقر گروهک‌های تجزیه‌طلب در کردستان عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/435791" target="_blank">📅 23:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435790">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پیکر کوهنورد مفقودشده در الوند بعد از ۴ ماه پیدا شد
🔹
بهمن‌ماه سال گذشته ۵ کوه‌نورد در ارتفاعات همدان درگیر بهمن شدند که جسد ۳ کوهنورد در روزهای نخست پیدا شد و یکی از حادثه‌دیدگان هم به سلامت به دامان خانواده بازگشت، اما تلاش‌ها برای یافتن پیکر آخرین مفقودی که در زیر برف مدفون شده بود پس از چندین روز بی‌نتیجه ماند.
🔹
در نهایت برادر این کوهنورد با یافتن پیکر وی به جستجوها پایان داد و با تلاش نیروهای هلال‌احمر و جمعی از کوهنوردان جسد به پایین انتقال یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/435790" target="_blank">📅 23:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435789">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6IT65qopxy3Geh3ggscYnMR8iOnxAuedi8iT-EE2_2fFl9fkuLC7Q3NPN0x5MyaHvSGnNWtwcYPeaUKK001ZvIcUra8q3HWbE0g3Ebu9wcIp1aaOU0ngTwTcRPPUfjIWtgOnaJKqAmAI12TPytuHFtdsuWj5_qr6PJhiFPDHhaEu53TyltyfNkS4ThZ9lHMRF9NWBZO-nnpXMSyCOHtdTfR-mXcJX8zZDis8-61nJGTr9zSakqAX6z_y4ZSNDAVVXAaEZwAf1DQujdmHHtm4wEjzbQ2AIRIZul7Pl7oa9-Z_nG6LoUUXaCjvkytrWA4u2Mx0w8dZhW2MOJ2mPdVwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: قواعد نظم جدید جهان آمریکامحور نیست
🔹
رئیس‌جمهور آمریکا نه از موضع قدرت، بلکه در سایه سنگین ناکامی در جنگ با ایران وارد پکن شد و آنجا را ترک کرد؛ وقتی او برای مهار بحران خودساخته به نفوذ چین چشم می‌دوزد، یعنی نظم جدید به سرعت در حال تنظیم قواعدی است که دیگر آمریکامحور نیست!
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/435789" target="_blank">📅 23:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435788">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3c36794a.mp4?token=cjrKhdHj-s1LSJJY7B-K00LVgIDRGNCPkSPMYcXcadt8n_8knVsUs8SEyv3lw2zBdhuaXiuypCNZb0Xv07bXpGFt8TN09PN7szV_I4W8xBuGlN0r_MdLpTt_4a4ZObdLU_ayx0GZ6rqRYsxXqRLKc-4CNlpVS6dZLdMkRe5EUvwshd2KjkesA_Q50cmDUSyYOvEDBg3RPhb7tYNM_nFXi6PiybXqQdph-I8BwnjfjFphA-w9Qg7k0226Xf7VF3ZY1_y7yq2MRTbuxCZNXQBHZ7eB6Qg8XIc19JEjoI602lloRPg-laoTm4BVREMs9iwc9cXtSyqRXOwnv5lFbl9wUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3c36794a.mp4?token=cjrKhdHj-s1LSJJY7B-K00LVgIDRGNCPkSPMYcXcadt8n_8knVsUs8SEyv3lw2zBdhuaXiuypCNZb0Xv07bXpGFt8TN09PN7szV_I4W8xBuGlN0r_MdLpTt_4a4ZObdLU_ayx0GZ6rqRYsxXqRLKc-4CNlpVS6dZLdMkRe5EUvwshd2KjkesA_Q50cmDUSyYOvEDBg3RPhb7tYNM_nFXi6PiybXqQdph-I8BwnjfjFphA-w9Qg7k0226Xf7VF3ZY1_y7yq2MRTbuxCZNXQBHZ7eB6Qg8XIc19JEjoI602lloRPg-laoTm4BVREMs9iwc9cXtSyqRXOwnv5lFbl9wUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات برنامۀ تیم ملی در ترکیه و سفر به آمریکا
🔹
نبی، مدیر تیم ملی: ۸ خرداد در ترکیه با گامبیا بازی داریم و یک دیدار دیگر نیز برای ۱۴ خرداد برنامه‌ریزی کرده‌ایم که تا چند روز دیگر بازی با این تیم خوب هم قطعی می‌شود‌.
🔹
تیم ملی ۱۵ خرداد عازم کمپ خود در آریزونا توسان می‌شود و ۱۹ خرداد هم یک بازی پشت درهای بسته مقابل پورتوریکو انجام می‌دهیم.
🔹
تا  ۱۱ خرداد نیز فهرست ۲۶ نفره و نهایی تیم ملی را به فیفا اعلام می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/435788" target="_blank">📅 22:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435787">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
باران شدید هم مانع میدان‌داری زنجانی‌ها نشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/435787" target="_blank">📅 22:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435786">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb304da96.mp4?token=TmaxgL3puo8HFZKsTBWvY4DEGhpwkXxdYzlBxl0mxywTeG3H4EygPzmsdWlbIuJI2XP9FNuCSrqZ4BUihZu5V1VStihR-TaV-Wu2BDyZCfuZU8zWZcP0AzWlLBDM-Uv7AFDzPu9Nm06cVUFgIKwIuCsl_npUaxvcfn_1WxIuaDnDW6ivP2s9umJZllE8ego-91RosBMQHwfIo55hkdwRmt4iYiS3PPFVp-vzKAjVA7a5Oyq7zVZJrAJRQNoQWXDr-xhwoK3iD73EGNDXB_cpBAbFULsWu-rilSMM3QHoNy2FX1sgucLxKUUV5gOERy-v0uTwoUROi59hhXNOj3tezReR9zst2sJF4H-aIELeoGuohIpwE6Op7zruj4UE_Hru9cOA-QpioplInv5lQZOA8alfYySVrsiDjnz0Qbq5Lq173x0EVillPC70szWhq5XNKi_unSMYUlGl6SN-hinpeUASOIDt9GLRM_jXxI2PKTq4t0V5R6T6f9hyDjRovkIucoL95VwYjLtLXbkZP9sWpy6Ew0cfz41_b2T6csfjmTVTdyoUER1fF2h1SOu5EAyzLMSx-P4p7_bSV0rdMptqdXXAEpvHr9JzCYihwZZMG3aoa4ni4_9l9aah48OqDy0P54eopCV6GUAlaKDuJgPxV0VipXod-eZiAyel4onlMyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb304da96.mp4?token=TmaxgL3puo8HFZKsTBWvY4DEGhpwkXxdYzlBxl0mxywTeG3H4EygPzmsdWlbIuJI2XP9FNuCSrqZ4BUihZu5V1VStihR-TaV-Wu2BDyZCfuZU8zWZcP0AzWlLBDM-Uv7AFDzPu9Nm06cVUFgIKwIuCsl_npUaxvcfn_1WxIuaDnDW6ivP2s9umJZllE8ego-91RosBMQHwfIo55hkdwRmt4iYiS3PPFVp-vzKAjVA7a5Oyq7zVZJrAJRQNoQWXDr-xhwoK3iD73EGNDXB_cpBAbFULsWu-rilSMM3QHoNy2FX1sgucLxKUUV5gOERy-v0uTwoUROi59hhXNOj3tezReR9zst2sJF4H-aIELeoGuohIpwE6Op7zruj4UE_Hru9cOA-QpioplInv5lQZOA8alfYySVrsiDjnz0Qbq5Lq173x0EVillPC70szWhq5XNKi_unSMYUlGl6SN-hinpeUASOIDt9GLRM_jXxI2PKTq4t0V5R6T6f9hyDjRovkIucoL95VwYjLtLXbkZP9sWpy6Ew0cfz41_b2T6csfjmTVTdyoUER1fF2h1SOu5EAyzLMSx-P4p7_bSV0rdMptqdXXAEpvHr9JzCYihwZZMG3aoa4ni4_9l9aah48OqDy0P54eopCV6GUAlaKDuJgPxV0VipXod-eZiAyel4onlMyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری خرم‌آبادی‌ها در هفتادوششمین شب حضور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/435786" target="_blank">📅 22:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435785">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4b5badbd.mp4?token=izy-dMgV78ph33H9XdzqGsDUq4OzyPrfteoo_NuuaP-zNXmgDrM_qL59LmNc_lJNNXfmwcPVsKaXJVvUgYtC--KsSrm2_bFSrhSleEF9L0t7ZYyDvAz_JeY9v8VJgEJeSphSHwJ9UsppdTtC93WiGJ-ztjXoNKrOB7D8nwhasH3KY8GJszeBO2ccSbR4fPlNkNM3z-lP_pTvFBuuxMxVswvvGhJyGf7LM9Ad9lygtRgkWze7tPsftcMoS1aQkZnDnJbivzvCYIo8IdDp9H2gs7DNX8y5lMRSQ07hyKpBEEltuFlu7f6qStJdrAyzV26r_GWn5dY1vwPdxU5_3Xq-k7ckI8IA3QnThxClQj7alw1NbdwOyttHnmZPhlh7qg6Jr0w5yvognoRAp7rgLBSRqivGmhDnFP4K-iJEsvDmolzJrwmI9v1DXqo0TpJ-YRlqE7sqzIVXhhzjSh5nBr2HJrSrcaEvVxBX60xwJ1_2hKHafbe8mcaUBNmigZtfjnz64RMM7AWtZWLOCxqoNcZocg9IKHt9q0HQ-W4IeNVIe0SUhaEswUKE_lGeTIyppqVGglSwt08oni2jMZT2DsKV0LBWUyA4MMzvThkhKpnUt-DzedK_JgR4UUrmtY3MKy9svB7LZyug0BZtr8I-aFEmBmBARDRx6eoDuHXzcCwC9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4b5badbd.mp4?token=izy-dMgV78ph33H9XdzqGsDUq4OzyPrfteoo_NuuaP-zNXmgDrM_qL59LmNc_lJNNXfmwcPVsKaXJVvUgYtC--KsSrm2_bFSrhSleEF9L0t7ZYyDvAz_JeY9v8VJgEJeSphSHwJ9UsppdTtC93WiGJ-ztjXoNKrOB7D8nwhasH3KY8GJszeBO2ccSbR4fPlNkNM3z-lP_pTvFBuuxMxVswvvGhJyGf7LM9Ad9lygtRgkWze7tPsftcMoS1aQkZnDnJbivzvCYIo8IdDp9H2gs7DNX8y5lMRSQ07hyKpBEEltuFlu7f6qStJdrAyzV26r_GWn5dY1vwPdxU5_3Xq-k7ckI8IA3QnThxClQj7alw1NbdwOyttHnmZPhlh7qg6Jr0w5yvognoRAp7rgLBSRqivGmhDnFP4K-iJEsvDmolzJrwmI9v1DXqo0TpJ-YRlqE7sqzIVXhhzjSh5nBr2HJrSrcaEvVxBX60xwJ1_2hKHafbe8mcaUBNmigZtfjnz64RMM7AWtZWLOCxqoNcZocg9IKHt9q0HQ-W4IeNVIe0SUhaEswUKE_lGeTIyppqVGglSwt08oni2jMZT2DsKV0LBWUyA4MMzvThkhKpnUt-DzedK_JgR4UUrmtY3MKy9svB7LZyug0BZtr8I-aFEmBmBARDRx6eoDuHXzcCwC9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیر تنگه هرمز
🔹
رزمنده‌ای که ۳ جنگ را در تنگه هرمز تجربه کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/435785" target="_blank">📅 22:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435784">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4d62d46f.mp4?token=fdb3pcJDJ0F5fPZe339-wsJir7jMI6bMoeETw3-uDp5v_cjj8CZWSOr3yNpwzmPdrLYk8DT8hSmypjQPjT9pZapnmCqs-SbNCvQvvXjm6rgpTHDNBXWOA9h_8U1dZo392gINaSXVQBLdO3qnuaisnH8AC7ZiNw1MhhKqdThAPK3aa7u5Lg9rgHoDXd_2E6C1MRD96I0T5fpUC4krLy8IAjuv0jaNKF-znnojkb9JSYHnsXLQuXorZx7SFri1i1C8Sx7E79n8LqUcRpebOB3q13qeVVAlkZshJdB2sYu5aN6K8AhkIoJ3ai2xRTg_u0Jtt6L9f1XI5cdfssX0nDo4Ikil2-Pc22po6SdE_f19TvGJqJUsKaF6MZ6NTou-25DcXLtupPNDk5WxabYmw9URJNsGE43KRV-gCd00jCtlCqXw0sLUiFVT_c2SLosL-4FixhBwkFwwEmLtbqwmoQrycJplcQ302Wdk-982cW1O2RlQ8AM8KNvyY1NuUuRUMC-qyJrSymkdlSpsoua61TRIGpbmgfILYWyQPF1c2Z7XPhJKzgBOYQ9Rx_K-2r9Aq0CM-dRYiafa6KBDkuEjT_1nprCtvWzd41Ivcmx32wHoCUBjhUSWG30qf5HaCBQdcLGu8rxWIcjxMwVxtTsn8SytWvlPcR6auiQTQUnNn165b1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4d62d46f.mp4?token=fdb3pcJDJ0F5fPZe339-wsJir7jMI6bMoeETw3-uDp5v_cjj8CZWSOr3yNpwzmPdrLYk8DT8hSmypjQPjT9pZapnmCqs-SbNCvQvvXjm6rgpTHDNBXWOA9h_8U1dZo392gINaSXVQBLdO3qnuaisnH8AC7ZiNw1MhhKqdThAPK3aa7u5Lg9rgHoDXd_2E6C1MRD96I0T5fpUC4krLy8IAjuv0jaNKF-znnojkb9JSYHnsXLQuXorZx7SFri1i1C8Sx7E79n8LqUcRpebOB3q13qeVVAlkZshJdB2sYu5aN6K8AhkIoJ3ai2xRTg_u0Jtt6L9f1XI5cdfssX0nDo4Ikil2-Pc22po6SdE_f19TvGJqJUsKaF6MZ6NTou-25DcXLtupPNDk5WxabYmw9URJNsGE43KRV-gCd00jCtlCqXw0sLUiFVT_c2SLosL-4FixhBwkFwwEmLtbqwmoQrycJplcQ302Wdk-982cW1O2RlQ8AM8KNvyY1NuUuRUMC-qyJrSymkdlSpsoua61TRIGpbmgfILYWyQPF1c2Z7XPhJKzgBOYQ9Rx_K-2r9Aq0CM-dRYiafa6KBDkuEjT_1nprCtvWzd41Ivcmx32wHoCUBjhUSWG30qf5HaCBQdcLGu8rxWIcjxMwVxtTsn8SytWvlPcR6auiQTQUnNn165b1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها با ذکر یاحیدر به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/435784" target="_blank">📅 22:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435783">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a581e71f0c.mp4?token=RBeuLTAXXhd7eNdaXyjXwhZyJfJshRGTc1Dyrv3LS0dqfgM3YCb2nh7x0nRokpJZty7EquavpduejBQElTs-FczuHK9ne8q75Anx3E4fBI1lKsJp-j2Ss7dOTg6w0ojZnbkfIMxFeExPrvWbpL5TobAx5_PDKy48ZU1sNtABzP6BhSsRUfFaajT7bnALXjtAMCf1kq5QePF_oAVu2Ys9OtVwdeCsq5RiTMHQcFKP9d8vsrFbWoI6b3jM9PZEZ-9jnC7OFeJzLlnZ9oFJOtxexauvlgReyKFOsNVpTnpkp9loczlrfwCh0KItmaT9sg2hzP-TK4TlHziNCEz8o4c05w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a581e71f0c.mp4?token=RBeuLTAXXhd7eNdaXyjXwhZyJfJshRGTc1Dyrv3LS0dqfgM3YCb2nh7x0nRokpJZty7EquavpduejBQElTs-FczuHK9ne8q75Anx3E4fBI1lKsJp-j2Ss7dOTg6w0ojZnbkfIMxFeExPrvWbpL5TobAx5_PDKy48ZU1sNtABzP6BhSsRUfFaajT7bnALXjtAMCf1kq5QePF_oAVu2Ys9OtVwdeCsq5RiTMHQcFKP9d8vsrFbWoI6b3jM9PZEZ-9jnC7OFeJzLlnZ9oFJOtxexauvlgReyKFOsNVpTnpkp9loczlrfwCh0KItmaT9sg2hzP-TK4TlHziNCEz8o4c05w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یامال در جشن قهرمانی بارسلونا پرچم فلسطین را برافراشت  @Farsna</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/435783" target="_blank">📅 22:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435782">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0dabaf70.mp4?token=WLTV2vSXWS4LF-K7xBVuOndIKuboSreO0ptJuZmYhaYqgGH_gSxhpFP14hKj-r5iRrqrqoInXhP_09LBCjNYEOo_832BH-7wgq7iU_70PYT3xaiPOgsebzgawy_5mauU9zyUhbAPRqunRV9jgh_XOSvjUHg30tDkHydsFw0GLQ4zFgbfjiYCJRbslZn0ojlbm_4pwJnIf-Vl2wcHgzpDVkyvb0TzjSQ0tdR6j2uu6iwyE8giroF-QdIZ4-BBgXbBgP2r2ORWfp-gRCcufAyNufwtyLmeia8HnxbLFUTGx1CfkaL3xWmCnmI1Y_JJcfIxsUPGmZIfEw8kwMaz8VG7BX4PQ3Ee_z5pg0xCSxzgVB_x88K4KW9mkpN5vJyQ-Ibgs-Z7eSaB7avulr6Gk6DessV9ectO6lSywvLIYhkDkuAgf0vI7iA1YUkbBLb5VIY8bLUUGBfyOvZnbKM1iIePIUAeyxtlPY7J7h8qLYdWZlTi6C_q7fluQiCqi8Kzv-BxgfHWveH0WtMPRbjda9M24xwxLG5lEf9cjf1BrVDQTBiaULaw844Uf-55SqE8h1mDbsmYpKow9-fygEx-Eca2wuT50FFiVvAG9j1hyHBcW_91TJTo962kXXFunDvbAJFhPTOwHNEKQWLnXQiDqtGRnRTK2d6veCGhVFnoyaQZTRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0dabaf70.mp4?token=WLTV2vSXWS4LF-K7xBVuOndIKuboSreO0ptJuZmYhaYqgGH_gSxhpFP14hKj-r5iRrqrqoInXhP_09LBCjNYEOo_832BH-7wgq7iU_70PYT3xaiPOgsebzgawy_5mauU9zyUhbAPRqunRV9jgh_XOSvjUHg30tDkHydsFw0GLQ4zFgbfjiYCJRbslZn0ojlbm_4pwJnIf-Vl2wcHgzpDVkyvb0TzjSQ0tdR6j2uu6iwyE8giroF-QdIZ4-BBgXbBgP2r2ORWfp-gRCcufAyNufwtyLmeia8HnxbLFUTGx1CfkaL3xWmCnmI1Y_JJcfIxsUPGmZIfEw8kwMaz8VG7BX4PQ3Ee_z5pg0xCSxzgVB_x88K4KW9mkpN5vJyQ-Ibgs-Z7eSaB7avulr6Gk6DessV9ectO6lSywvLIYhkDkuAgf0vI7iA1YUkbBLb5VIY8bLUUGBfyOvZnbKM1iIePIUAeyxtlPY7J7h8qLYdWZlTi6C_q7fluQiCqi8Kzv-BxgfHWveH0WtMPRbjda9M24xwxLG5lEf9cjf1BrVDQTBiaULaw844Uf-55SqE8h1mDbsmYpKow9-fygEx-Eca2wuT50FFiVvAG9j1hyHBcW_91TJTo962kXXFunDvbAJFhPTOwHNEKQWLnXQiDqtGRnRTK2d6veCGhVFnoyaQZTRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هفتاد و ششمین اجتماع مردم آبیک قزوین در دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/435782" target="_blank">📅 21:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435781">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
آتش‌بس بین لبنان و اسرائیل برای ۴۵ روز تمدید شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/435781" target="_blank">📅 21:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435780">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a5d8489d9.mp4?token=Kwf8UDXfI-PvuIhpLoarmBMF_Ls9bBG5ldCXypVDPnYqPbyblEK_aa-ksCsucyYAtDSPQsdtRS5Wn8NrpK87td7ul3ydH1RAwcsqCZf5lfOilsWHhGTpUuqbhkjpf-uyfPJHJ_WnxgsFBgD1HGJ6mol-a90VRx2vxWWwKuA1YdRLDGQIiRR3-wRs_gIwviYrQLg8JLhCaMzXt5xzDCqZlzpE8UZJ7Ubamdz6CA07jQXKIvqV0wXafYSUA5c5zI-Ha9MFZZ82xkSj4Fg3HKxp82aGWMLY8lQ4Qf5__Va7tT4w_gVEJUcH3ZOuzEYQxrfc0DppaNpG6wpd5o6YzzT3FzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a5d8489d9.mp4?token=Kwf8UDXfI-PvuIhpLoarmBMF_Ls9bBG5ldCXypVDPnYqPbyblEK_aa-ksCsucyYAtDSPQsdtRS5Wn8NrpK87td7ul3ydH1RAwcsqCZf5lfOilsWHhGTpUuqbhkjpf-uyfPJHJ_WnxgsFBgD1HGJ6mol-a90VRx2vxWWwKuA1YdRLDGQIiRR3-wRs_gIwviYrQLg8JLhCaMzXt5xzDCqZlzpE8UZJ7Ubamdz6CA07jQXKIvqV0wXafYSUA5c5zI-Ha9MFZZ82xkSj4Fg3HKxp82aGWMLY8lQ4Qf5__Va7tT4w_gVEJUcH3ZOuzEYQxrfc0DppaNpG6wpd5o6YzzT3FzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های در اهتزاز در دل شب
🔹
میدان‌داری شبانۀ مردم ایران به عدد ۷۶ رسید.
@Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/435780" target="_blank">📅 21:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435779">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سازمان اداری و استخدامی: ساعت کار اداره‌ها از ۲۶ اردیبهشت تا ۱۵ شهریور ۷ صبح تا ۱۳ خواهد بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/435779" target="_blank">📅 21:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7-qpla8CawM6pWGqWqD_SoI94HQnE_lWiMqQUoMoJOiSNRWh56uPo8vFo1eQN4n_Ux0AhKKnAwq7pFGXcjlnWiqpb_DzkslqP7KAHRLoe_R7xTUdw5kfo_ZqW432YsPtmnFo2T-pO2X95M-h_smZT9d1vFN4VIe_2bLIeQZfi_8LkeM23Qg-ie9f4X7XILGQQe7nVvecfO12ocOXcqB56KIN3n_c6NHvqFmWyjtzaM-S9ZhDOzeBWXD9nKiXhS-O335FzVUkf6nNgW2Bpv8WmoKRUd369oAomOyIVVGRnZfEOzgUUfdhydeYXF3N5tLFASTwzEUn-ohhBoyrAB90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbab850c7b.mp4?token=jSESWvbeMoBW_81Q7KVH7xJKZ-j4PVjITPapukTXv7wELRq_Vnu_WG1M-mvhunAuZTLumitiYbmUtc341V6Dpvq0SqZOX-_np2MueiV5__0RjYJhIL1CastxU0hQ87AUHPiamIokY23vbrj8xSrcYQrWEunqxGxdCxd8NwhY1COD2dByRFcjDBeLlX80rMwszpNJXP7SdVO9zT3H0f38SN8caxPgnEYWN6a-dvYI7cbx3XwTthqRq7_ndpYMWJBqLYFLo2NJjSk1NL8njwjBK842AI5_P8WTdpF-BvcEKtBlwsiw4cufTop1Z-7zp-AwNvp6LdNsW-KphTageXKsdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbab850c7b.mp4?token=jSESWvbeMoBW_81Q7KVH7xJKZ-j4PVjITPapukTXv7wELRq_Vnu_WG1M-mvhunAuZTLumitiYbmUtc341V6Dpvq0SqZOX-_np2MueiV5__0RjYJhIL1CastxU0hQ87AUHPiamIokY23vbrj8xSrcYQrWEunqxGxdCxd8NwhY1COD2dByRFcjDBeLlX80rMwszpNJXP7SdVO9zT3H0f38SN8caxPgnEYWN6a-dvYI7cbx3XwTthqRq7_ndpYMWJBqLYFLo2NJjSk1NL8njwjBK842AI5_P8WTdpF-BvcEKtBlwsiw4cufTop1Z-7zp-AwNvp6LdNsW-KphTageXKsdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: فرمانده عزالدین قسام را ترور کردیم
🔹
نتانیاهو و کاتس، وزیر جنگ رژیم صهیونیستی مدعی ترور «عزالدین حداد» فرمانده گردان‌‌های عزالدین قسام (شاخه نظامی حماس) در غزه شدند.
🔹
رسانه‌های اسرائیلی مدعی شده‌اند که عزالدین حداد در بمباران آپارتمانی در محله الرمال در غزه به شهادت رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/435777" target="_blank">📅 21:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de2cca144.mp4?token=vERchvYxqoVkoSj4iyBrUT3EAZt18Otf8bJ5qxQD5y-hZq6HtndzLnN-SpY4LpFP1OOH-_SW4PfQ56MmIurQbp5mqSjty31g3ahdN7U9Xr69wC61ZG6MrPL6j_wZkXlQHq4-xellmmhwWwehj4R1wWUqj8Gh7l02pFvuJVw-tG--ChzzHDKrLJJF7s1G1n6HYCTVSU87ccHjOjvkI15X5-cuOEsXORdOEppPfxUPGSAXUKbrO_bGKCuZbBBNPjcYmPrMNDAl-01Dxzlu4rCXBYXQWUoGaEpr-d0PWDo0hz0msH3i0D5B2g1TFUO3WOuG6PLQO1eFNMI2cDV-hfKy234_ZclvxjoWXNrkC-fuPNtVg09EVp8UFK9U6niaClXjGzz3awquoZB7wofTLU5xj-JknXHRx5i3S7Rd1WOFOoS4W-E8tGr8hdyk9fTyE4Uvb2GrKnpeoDT60mmoGndev4w-t4EvrdgYMErnKEKNhzKCQgApNzpJtRJzjQl8SxEPG1ivyB-Zs2FR0D3kyRHfPsWYhJ3xWpC5MnU1xFrXWlAKr6VChbW2vDwlDYYWzBYTsOElJGx8iqgFCno9kx4TGlX_00bPo_XEGlVWvKo3mOZbMfYX0ed_iwOq5HwJOYmfI_4UOLZUH4yI9RHFV0cah7FAqj3CfY4yxWQcZs6HseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de2cca144.mp4?token=vERchvYxqoVkoSj4iyBrUT3EAZt18Otf8bJ5qxQD5y-hZq6HtndzLnN-SpY4LpFP1OOH-_SW4PfQ56MmIurQbp5mqSjty31g3ahdN7U9Xr69wC61ZG6MrPL6j_wZkXlQHq4-xellmmhwWwehj4R1wWUqj8Gh7l02pFvuJVw-tG--ChzzHDKrLJJF7s1G1n6HYCTVSU87ccHjOjvkI15X5-cuOEsXORdOEppPfxUPGSAXUKbrO_bGKCuZbBBNPjcYmPrMNDAl-01Dxzlu4rCXBYXQWUoGaEpr-d0PWDo0hz0msH3i0D5B2g1TFUO3WOuG6PLQO1eFNMI2cDV-hfKy234_ZclvxjoWXNrkC-fuPNtVg09EVp8UFK9U6niaClXjGzz3awquoZB7wofTLU5xj-JknXHRx5i3S7Rd1WOFOoS4W-E8tGr8hdyk9fTyE4Uvb2GrKnpeoDT60mmoGndev4w-t4EvrdgYMErnKEKNhzKCQgApNzpJtRJzjQl8SxEPG1ivyB-Zs2FR0D3kyRHfPsWYhJ3xWpC5MnU1xFrXWlAKr6VChbW2vDwlDYYWzBYTsOElJGx8iqgFCno9kx4TGlX_00bPo_XEGlVWvKo3mOZbMfYX0ed_iwOq5HwJOYmfI_4UOLZUH4yI9RHFV0cah7FAqj3CfY4yxWQcZs6HseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روستایی‌‌زاده‌ای که آبروی هسته‌ای آذربایجان بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/435776" target="_blank">📅 20:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435775">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUus2BsnrASbevVcwiIc5FIvqsP3raZNf6wLIdz5kA8qZPWygfH9sypkAXWcdGvbBhZ6Qc5DofzNtsUzsO9IcLCgwMzlhY4y32vT6tTRnWIyzgWWGLDAbEhSdDyloDn9PdL8f5mwrfjPRBx0F1Risyd9h-RgL_Q2cDdfbp6j-R1aXIP0LhKfwL3tCYD6RzHd-kz0x6oM46hUITMk8Oix6RGlElisGLQhsqjUM3cMRSROW_qmeIXMPWog8imjpMtxF2Ppdvvnc_PPHUGn97qpgxIoll1XDbIh4ReIgRG0eN90o926e4dE1X0rf1Ew_jpsKDCmQqICflmA4DpJD4ytOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«داستان‌های موازی» اصغر فرهادی، ضعیف‌ترین فیلم کن تا روز سوم
🔹
در سومین روز از هفتاد و نهمین دوره فستیوال کن، اصغر فرهادی که در دوره‌های گذشته با آثاری از سینمای ایران حضور موفقی در فستیوال‌های جهانی داشت، آخرین اثرش که فیلمی تماماً اروپایی است به‌عنوان بدترین فیلم جشنواره کن تا پایان روز سوم معرفی شد.
🔹
اکثر منتقدان وب‌سایت مویر امتیاز متوسط را برای «داستان‌های موازی» که دهمین فیلم فرهادی است در نظر گرفتند و اسکرین‌دیلی نیز «داستان‌های موازی» را به عنوان ضعیف‌ترین اثر این دوره از جشنواره تا پایان روز سوم لقب داد.
🔹
منتقدان فرانسوی نیز به هیچ عنوان فیلم فرهادی را نپسندیدند و با نیم ستاره و  یک ‌ستاره از آن استقبال کردند که همین موضوع «داستان‌های موازی» را به بدترین اثر این دوره تاکنون برای آنان تبدیل کرده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/435775" target="_blank">📅 20:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435774">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfZNkTIN0F4gx7hZeDQoim_gR6k2UPeHRBd58KQAIZSryLAvOb-tOxar6bnjPrSPC82X-PZqDqKYzUyiArtzXeLQSLqtd3xY343k2Cm-EMWZWnU8Vu7qVxFqDE0UEwLiS_0CPiMfMnbYEjrdpasEpuQ6O5t988EcWqg0v0kLLYS3CtWcV9hKyfr8Rv-B1t5J8uyi6tSLEGnUS3rxdJ57NYd7kxkb0bJcziZrx_BbR5PXQiAMY9nZP92hu6lB-1GinCLFWR2nm46vURB5OlVGlomMM2IcOgz8XhcU4EL5tnSMdqQycc0DmZiAvF_f6wcs74s6s-FnuDIojvTJFFnxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تصاحب مواد هسته‌ای ایران ضروری نیست
🔹
رئیس‌جمهور آمریکا دونالد ترامپ در مصاحبه شب گذشته با شبکه خبری فاکس‌نیوز از ایده‌های متفاوت و متناقضی درباره تصاحب اورانیوم غنی‌شده ایران که او گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌کند حمایت کرده است.
🔹
متن کامل این بخش از مصاحبه را
در اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/435774" target="_blank">📅 20:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435773">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎥
جنگی بی‌صدا برای خالی کردن خیابان‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/435773" target="_blank">📅 20:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435772">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec1b837167.mp4?token=eJ8DCj7R7CHDdvElvvaGYrCmZQ_CSnV0DfctfF_5d3VSwHzzhalDLyAY_SAsmeLocuGEJ0jyskhFVwMRGQ08bEsm8D80w-JU6UmryRaFMoGv2BdBPKuYCsN09PRxWVjzs4KW98NalCDieeOldFTOk6I1D-X5ILLGixyVArP7YuNfhNkeCUP9NcS5AD7XGAXEITzABBeHAYOy5cseXDBSPPr_yMUw5W9oD0aiPJ_QlsGyONAK8YC5LuP0RRkBs8ci1RH83Lj4DwbbOyZzzmWsDbgnRwANHdRrRNz80eIsPOjFRRbo_Ak1w6mNJ8P8-O6J-85qWv-b8JA54d-Efw0lSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec1b837167.mp4?token=eJ8DCj7R7CHDdvElvvaGYrCmZQ_CSnV0DfctfF_5d3VSwHzzhalDLyAY_SAsmeLocuGEJ0jyskhFVwMRGQ08bEsm8D80w-JU6UmryRaFMoGv2BdBPKuYCsN09PRxWVjzs4KW98NalCDieeOldFTOk6I1D-X5ILLGixyVArP7YuNfhNkeCUP9NcS5AD7XGAXEITzABBeHAYOy5cseXDBSPPr_yMUw5W9oD0aiPJ_QlsGyONAK8YC5LuP0RRkBs8ci1RH83Lj4DwbbOyZzzmWsDbgnRwANHdRrRNz80eIsPOjFRRbo_Ak1w6mNJ8P8-O6J-85qWv-b8JA54d-Efw0lSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فردوسی؛ میهن‌‌پرست‌ عاشق امیرالمؤمنین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/435772" target="_blank">📅 19:55 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435771">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d09541d4.mp4?token=WaLY1CbE_oEzt3a9qkdq4yKRVl4yABHiNeah2_gyMcGZVZ9UMKUtP5EagmTPm9U1VLCyHTIsFvIeCeQOQ3_dNbdva31Le_ld_kjThPp4KpxLvzjC7OLA3i1k4NR16PbXAO5-IJwlxcQ9Nlad2_4bOFalbM0_KKeF9rXsaryDt3o8tFCyZ4klmH1Be1FWFj05Qv1jNkftuUgLNv6Scz6thhYUp8YhruawNsIPzEmKriKgKtLV6g7QrBp4RtT5EreNCpMZO7Cl2_3QDGgiwy9b1qD5xchtjOt_L14aO0dId3CtUIn_f41YzYKLnjyhF1KfRJUYQNtWqhVPUZ4_2AJR96LTubAu-detMAIvvoJHJiaXy_hhGW_an9D6xcqZhy9Ca7z8kQWAdQT93qRpibxHaHBtyvmvwEq4d8He3Ep-qWlA_PbI7388wX4ANCZ6FSe1zQr1W5r0Q0knOS9-4Gw6udoPl29p6fdpC6deiNT1D0V2u8jHsmlUR4JOrZVledh3fCeuMM1wvYx2n1K96Nz45QOR5E41K88kdFd119RchRiKS1FL21ZaiEjWBZq4Al9m4v0bdVD5HWn9z8hOx5HJ2PmSAxLZDNT1KVoHdI_6ZdPPIGHoUrr-ZiXEp-vkTRLokJOfBCm7nDChhjZfKRHto8m6AMKppGV93St3HWuXlJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d09541d4.mp4?token=WaLY1CbE_oEzt3a9qkdq4yKRVl4yABHiNeah2_gyMcGZVZ9UMKUtP5EagmTPm9U1VLCyHTIsFvIeCeQOQ3_dNbdva31Le_ld_kjThPp4KpxLvzjC7OLA3i1k4NR16PbXAO5-IJwlxcQ9Nlad2_4bOFalbM0_KKeF9rXsaryDt3o8tFCyZ4klmH1Be1FWFj05Qv1jNkftuUgLNv6Scz6thhYUp8YhruawNsIPzEmKriKgKtLV6g7QrBp4RtT5EreNCpMZO7Cl2_3QDGgiwy9b1qD5xchtjOt_L14aO0dId3CtUIn_f41YzYKLnjyhF1KfRJUYQNtWqhVPUZ4_2AJR96LTubAu-detMAIvvoJHJiaXy_hhGW_an9D6xcqZhy9Ca7z8kQWAdQT93qRpibxHaHBtyvmvwEq4d8He3Ep-qWlA_PbI7388wX4ANCZ6FSe1zQr1W5r0Q0knOS9-4Gw6udoPl29p6fdpC6deiNT1D0V2u8jHsmlUR4JOrZVledh3fCeuMM1wvYx2n1K96Nz45QOR5E41K88kdFd119RchRiKS1FL21ZaiEjWBZq4Al9m4v0bdVD5HWn9z8hOx5HJ2PmSAxLZDNT1KVoHdI_6ZdPPIGHoUrr-ZiXEp-vkTRLokJOfBCm7nDChhjZfKRHto8m6AMKppGV93St3HWuXlJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستگیری شبکۀ مرتبط با موساد در اردبیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/435771" target="_blank">📅 19:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435770">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">فاجعۀ نیم‌همتی در استقلال
کدال پرونده‌های مالی را روی دایره ریخت
🔹
انتشار صورت‌های مالی باشگاه استقلال در سامانه کدال آن هم بعد از وقفه‌ای تقریباً ۸ماهه، نکاتی جنجالی و جالب‌توجه از پرداختی‌ها و شکایات میلیاردی علیه این باشگاه را نشان می‌دهد.
🔹
در بخشی از این اسناد، حسابرس از باشگاه استقلال خواهان اسناد مربوط به پیش‌پرداخت رامین رضائیان شده که مبلغی ۵۷ میلیاردتومانی دارد.
🔹
در بخش خارجی‌ها، منتظر محمد بازیکن عراقی اسبق استقلال شکایتی به مبلغ ۲۸۸ میلیارد تومان علیه این باشگاه طرح کرده که البته رقم دلاری قید شده در گزارش (۵ هزار دلار) با آن تناقض دارد.
🔹
آلمدین زیلیکیچ و وردان کیوسفسکی، دو بازیکن بوسنیایی که در دوران سرمربیگری جواد نکونام به استقلال آمدند، در مجموع شکایتی یک میلیون و ۳۰۰ هزار یورویی را علیه استقلال طرح کرده‌اند.
🔹
کوین یامگا، بازیکن فرانسوی اسبق استقلال به دنبال دریافت ۸۱۵ هزار یورو و فیرمانی، ایجنت این بازیکن هم ۲۸۰ هزار یورو از آبی‌ها هستند.
🔹
پیتسو موسیمانه، سرمربی فصل گذشته استقلال با طرح شکایت در فیفا خواستار دریافت مطالبات خود که شامل (۶۵۶ هزار دلار، تسویه‌حساب مالیاتی، سه بلیت بیزینس کلاس و هشت بلیت رفت‌وبرگشت اکونومی و بیزینس برای خود و دستیارانش به مقصد آفریقا و ۵ درصد سود سالیانه) شده است.
🔹
مبالغی که اگر شکایت منظر محمد عراقی را از آن فاکتور بگیریم، تقریباً به ۳.۵ میلیون دلار می‌رسد که معادل ریالی آن بیش از ۶۰۰ میلیارد تومان است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/435770" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435763">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lp6PBgTyVTI6V6FJjhTvNHb5xUs1vikCl-l7xMbN3NkdwJHOmnZTcnJ2aogZKTWFV8tMSe6Ax2R8IpFbfEBMEoOPXZH4kM7giJ7xwO2X9KoC_9nyQ7Mdm0-vE8tDPhEjwo6nsu1xHnn_Di7y5Zym-Fpy9F44o3-Zn7DDQq7KafMp2Dz4ifvZeJogATUE-TE1FUJiG2a-4rwO1LwQlR57Rbfj9HFPvV8KlVIwPn0aE_ZqYAUM-KvZ2GAo_NV9zOTeNCfprNm26lFaBibXHr7sPJmCrM4vAUKEUdJHXLodFx61ejQ3x0KnuQVKcVhHwzWxBYazp3dimusq5tDaEBHQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDycP4cNS1CNDSWdrA07HnSx3c7eomfNIJkIdvvS6D1IPfh-nNR8B9LqIb2RUEQOoO5Su1WJB4shnCTX-aw-TCaOAjTVtlwk_3RYPpqcr8tLNFjRp3A3T5mI3b8ucA3L_tVriDg6hq6dkS73JgigLX8GODlqZCXvpWQdoB3FnMcIk_a7LX2JeVCitLTw5oFTxvg_wYIjulEpgNcFAiGoVUVYLubm__rPEY6tEPYiHJrVsAunN6lvK_17r8AJnvEZrCKbhXsRB_xvIGrPch0Zh5hQgzlcBH71pYG_Nl-ovXci8fCa1h0-UOVTa7kgOn_6RajGxgDjdXjeSvKOnxZtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTrfRETxSPExoj-jAVHk3V7H5RmNzPBGpHU_tSOSWUtlwMb9W1XrNDH4udWv4JyX_3H7bwDbq4_iFwZA5B02q42dGhR5I2B8DlDPSxNMaeuRLPsNup4rKK9_uePDbS69YxLyTNei7nf9pzlWabv0RKvSMF1NvWzoPix_lbPmdRBfCwladIUzGw9aEUlu0R_5Wlua_czjqpHnvBPf1aq0QflI9sQ_70CHW0nPuSklCc-031GCOKop3IC-JxmGAJnzWpdSgXGWfE3mpxa_6zDxv6TETKkMY34trifJkimveYUUbVJ0R2fhLx_ajqVJK5GqaccPOSIXXRGKJhHxiLZBiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSp7WY6DyRlguzF7iTb4esa8KfULfckZsg4iK-LV1wBCEAJsamRPio6cH-KPN7D4P5KjGjc-iZPxPbPYGHoJIQzp5zCiApY3pvgYPEC6uOKa3f4uGoYJRGPWfB-1dWlqRe-b8kMFGAWfybLPzhLuj_ofQaP6j7vbQuqWsJx3SGkPE9By7p9i8Q9nt1GBpnoYGt0CITYIi0gtIC03z1H_izMOs-A5m7E78cYio0sr2MirnXb61gEoy58UyquAsEXVFWJ-Le7vbX3ttY4QBTSyvrJpK6lDfK2dJIpKx1JAuaVp2_SJt6Bqu_6YDiMQCcHKPscO0a-GQPsy0_sUdJaoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3fETTCDJ9Ba4pRYCAgdvG3T-rS_ixEoPWXDBWV7yBplBmoQRBgDQLU73unNXxD0-1bpJpu6pCIuZxfHgq98DWoPWw0TnTz9aZq1mA_i3dwAoel5X2GXU0mIuoQxbYbdlqOCLGMGqiWwT0H4-73FOD3dbLj15PHThBm2PFP0DK40PVfp6yzp3YxN7qMLbE1_j3LpdJoqK8Sl0JMkvAHhZFvzhyq2jR-WktRSGzLZ1uesp-hXjJ638mWZgqzIi8KCgpYEGujpZaWtzUlScrlVthDQVJr1-s8TatZAalddlFzvKw6TheVV9dHwK666cjJdWlFFSKf4gTte-teoHaya1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAltGAEKyPmDkQex_nZ5JIMh797vJqtvzfwQFQmw5zQjEvHlM647MsZ6nZo4EB3fs4q3qi-vEEqmJ_0v0Ne9aCmpdYLrCOpiCtMGr_1gzMLDTX3mBQtwRCvs5QESgSM-1_JAw9vClhZu7ssOraRcK2EZEEOlVUVSEdq34h8SjT7dDJr5gGFYWXtqJAYt_Ts578KFsWm-ArtJ4DLiYgrIqMvFW4YFtz72Qyae9bMoTVGbYWTmCSxK82IuOIn18axiXX4_bGsrWEeE3y1o5UE7GUcnA6aa3Xci5TEQifFg4svX8Q8e_BXUt9dt40soJ-oKqVcPIvXm9_DfX_HqfgHAWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSnh0-3Bs3NDjXacMGVRWvCHMkoMcuOHeYsXRhkruG7gw_b81dDc5_BbnPm4ITiArCAnLYgTd93U32aIp6HvdUEe7E_IVHthbbcYMPjgm9K08AGIpX-rWA5IlDyIo-w09eInZ1J_0lVUr0YaJSbhFZbMqqS4gGK1ltU85mzVhGKKYueduoK3SGdkd0BDtqkpoNfGUoBwJ-9r2YdXPrSfoCFIAdD1BWjoolJOPq767sYLtOnaMQDwaPKiUbXT8B_EPp48ZeEEe7PrET1xXTZy10e7F79x9BLercxLRyB9cb4FP9MorK6Vfo6CNgwvtlxmcQJJpqAJhzM9NOYmWfftLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چهل و نهمین ندبه اجتماع قلوب مردم گرگان
عکس:
علی دهقان
@Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/435763" target="_blank">📅 19:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435762">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73dfccfc21.mp4?token=V0_r9zdIsM4k7zPHhqQiNekwz30wOXichbfkrlugR2l5LYU-aGiZPgf4JCgcr8fD77zEAN1-ZJP1I5C0YKWRkIn3kkbDCg6pgiHoNnL0wiCNpz2mkTeif3NZhXi4lo7eb9iRb0SsLkcsNnaHGkRFwxCUxdJOPc1JaxdJzjzvWIZqpGK9HiNEeF9L_enGyENB6W-jTR5k5Nl4sVMHX33sWHIkvy3A45VOWRSJdb8hkjM0LahE7j8O-9-AKx8_ZOenCyaRJ-SUTOD2EBchkbZOtTXbiHOWMN83nfGVxYzrHOa_fOnmysSKdnOr5K74J5Ulz2dJ8VgU-LJKYhk1O-iXoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73dfccfc21.mp4?token=V0_r9zdIsM4k7zPHhqQiNekwz30wOXichbfkrlugR2l5LYU-aGiZPgf4JCgcr8fD77zEAN1-ZJP1I5C0YKWRkIn3kkbDCg6pgiHoNnL0wiCNpz2mkTeif3NZhXi4lo7eb9iRb0SsLkcsNnaHGkRFwxCUxdJOPc1JaxdJzjzvWIZqpGK9HiNEeF9L_enGyENB6W-jTR5k5Nl4sVMHX33sWHIkvy3A45VOWRSJdb8hkjM0LahE7j8O-9-AKx8_ZOenCyaRJ-SUTOD2EBchkbZOtTXbiHOWMN83nfGVxYzrHOa_fOnmysSKdnOr5K74J5Ulz2dJ8VgU-LJKYhk1O-iXoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقوع آتش‌‌‌سوزی در پتخ‌تیکوا در شرق تل‌آویو اشغالی
@Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/435762" target="_blank">📅 19:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435761">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b819e8e9.mp4?token=MRPgcwHD5f5Gx2Lt_kqJnctvJHge9D09sLEQl0zQjREz_6tLM93KrVLU6AAvnm9hQwDMwNe89e4AHkedIlHRB6Bj6uDa3ZDoB-yywm7ceiQ8idHASm_cXi86YvjLObAp7fp2Q2IfZz7v272KE7j80M7uBdr1Vrq4S6l6QPesNvjjQA9Tb4aSEvacGeQFlUMvEpK8vbOsJDVjBoiI0gd86qChC0Ek2knKSrTHu_aJxfs5Qrw6wKnFqC8l8Y0tfaxV0OE1nLh9NcDcnpFOkezgHmFl7X0mCOS4Hz0aeD8sGOytK2tlohPhmcKuVj5qqWt6U5NG965nt16DS_mbm-ItUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b819e8e9.mp4?token=MRPgcwHD5f5Gx2Lt_kqJnctvJHge9D09sLEQl0zQjREz_6tLM93KrVLU6AAvnm9hQwDMwNe89e4AHkedIlHRB6Bj6uDa3ZDoB-yywm7ceiQ8idHASm_cXi86YvjLObAp7fp2Q2IfZz7v272KE7j80M7uBdr1Vrq4S6l6QPesNvjjQA9Tb4aSEvacGeQFlUMvEpK8vbOsJDVjBoiI0gd86qChC0Ek2knKSrTHu_aJxfs5Qrw6wKnFqC8l8Y0tfaxV0OE1nLh9NcDcnpFOkezgHmFl7X0mCOS4Hz0aeD8sGOytK2tlohPhmcKuVj5qqWt6U5NG965nt16DS_mbm-ItUzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعرخوانی دختران قزلباش در وصف شهدای جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/435761" target="_blank">📅 18:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435760">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4907051e.mp4?token=EmyLn_jCTMrLJGc0h3G_w8Cv9UI8iSSEYRoLs9P9Iho3wZ56N9KnHF9S63yJB4IsrU6BHFmiseg_0ioaQBm1hXRQ6IZ_Qm5RPJQ2Uu8Nm7pCBERJvnAKnA-6X1Bv7UoXjSho5oWc7zdv8bldc09TiLy7ebYG81CMdgNoQD288Ad7Bp9qhhIdN4n8gPX3fQfvLVCHCg-bdy8u5wbHNb_Pz-81oEMsFE8Kl2vnVMop3kMWufvHjoVJOoK7MiHDrQvUGjx9qNzjSBW7_mYQLeS1vOpsGgCbAa32iyomzyFvkKlkmfTXQLLneL3AMEy1QZOukFC6QIMnLchakUJn2bWS2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4907051e.mp4?token=EmyLn_jCTMrLJGc0h3G_w8Cv9UI8iSSEYRoLs9P9Iho3wZ56N9KnHF9S63yJB4IsrU6BHFmiseg_0ioaQBm1hXRQ6IZ_Qm5RPJQ2Uu8Nm7pCBERJvnAKnA-6X1Bv7UoXjSho5oWc7zdv8bldc09TiLy7ebYG81CMdgNoQD288Ad7Bp9qhhIdN4n8gPX3fQfvLVCHCg-bdy8u5wbHNb_Pz-81oEMsFE8Kl2vnVMop3kMWufvHjoVJOoK7MiHDrQvUGjx9qNzjSBW7_mYQLeS1vOpsGgCbAa32iyomzyFvkKlkmfTXQLLneL3AMEy1QZOukFC6QIMnLchakUJn2bWS2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای سربه‌زیر شدن ترامپ در چین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/435760" target="_blank">📅 18:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435759">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
همان رستم شاهنامه است او
🔹
نماهنگ داستانی «جهان پهلوان۲» منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/435759" target="_blank">📅 18:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435758">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGWO749_SIa8VxFVbymlL0J0UldLM7N4ia5UfGOgUT87TKORP_AOI0HOUSJpvoWs2wmHl9wNf-KUKiAPFg6BJSZWKsPxot6VxTilyobDAChyFFTGkdRwAu5p5aykLIY1Ur8vwUmuwuwyvLnba_Qo6BcsIomWE2GuZKFwcuCi7Qie1LHJipgcC94hGFE8PB40dUWeQBPPL3upi3FIny6nqqGMKs4WNTaQ0F-PBFADKZwS7i415ma0EhZY5NaOcm6UGfkJfBItcuP4kkY4riIw-KqMVT_ZBFd337DLrAjHCN7yJ2yRIoqwovkXWwulArHhiVQ9EJX7cZZ5F57O6p_YdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: فردوسی با شاهنامه هویت ایرانی را جاودانه کرد
🔹
فردوسی با شاهنامه، هویت تاریخی و فرهنگی ایران را جاودانه کرد و پهلوانی را در پیوند با عدالت معنا بخشید. امروز نیز فرزندان ایران، در برابر بیدادگران، پاسدار امنیت و سرافرازی این سرزمین‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/435758" target="_blank">📅 18:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435757">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">پاکستان از آزادی ۲۰ خدمه کشتی‌های ایرانی از دست آمریکا خبر داد
🔹
وزیر امور خارجه پاکستان خبر داد: ۱۱ شهروند پاکستانی و ۲۰ شهروند ایرانی که در کشتی‌های توقیف‌شده توسط آمریکا بودند، بازگردانده شدند.
🔹
محمد اسحاق دار افزود: تمامی افراد آزادشده از سنگاپور به بانکوک رسیده‌اند و اکنون با پروازی عازم اسلام‌آباد هستند.
🔹
او همچنین گفت: بازگشت برادران ایرانی ما به کشورشان تسهیل خواهد شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/435757" target="_blank">📅 18:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435755">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-36.pdf</div>
  <div class="tg-doc-extra">3.2 MB</div>
</div>
<a href="https://t.me/farsna/435755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-35.pdf</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/435755" target="_blank">📅 18:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">جام جهانی بالاخره به چین رسید
🔹
تلویزیون چین امروز اعلام کرد که در فاصله کم‌تر از یک ماه به شروع جام جهانی، با فیفا بر سر حق پخش مسابقات به توافق رسیده.
🔹
پیش‌از این چین با فیفا برای مبلغ حق پخش تلویزیونی جام جهانی به توافق نرسیده بود و نمایش این مسابقات در این کشور در هاله‌ای از ابهام قرار داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/farsna/435754" target="_blank">📅 17:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435753">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Axc9OSUf_Scy0l0QZE-4NDOp7Rahd6f2lo8ETCs1_WPmlrn8zegokhpRLvl2Y_aQcNJhQwBRiOqvtcwMr8QxlMZ0ySXcd6NceUgmBTgYKaRts5fkGHcc9YCYAkmmtvNhgn2SiWuWc4OQomWf9BZahtveakBYToYWMDRHjtkJgwhH3VyP0wIsNdyRgeqUJcefPWbKVSe6qBMSjDZw1SoBYVWRxXCkpEW8cKI9AWzbshEvhp056dwIQq9zCZK3JT_-30qVzUpOIqrT5UhbmZLOe-4tInSVbEFyO4wV_y79KHq4i6xP5y3RpSIjK6SNeMJ0eoISDU-bB6w9-ytRb0Yflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری قدیمی از امیر سرلشکر خلبان شهید نصیرزاده در کنار جنگنده F5 نیروی هوایی ارتش
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/435753" target="_blank">📅 17:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435752">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
گردشگران، عاشق این دریاچه هستند
🔸
دریاچهٔ سوها از جاهای دیدنی اردبیل بوده و در ۳۵ کیلومتری شرق اردبیل قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/435752" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435751">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
حسین ستوده کوتاه نمی‌آییم را خواند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/435751" target="_blank">📅 17:04 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
