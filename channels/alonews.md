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
<img src="https://cdn4.telesco.pe/file/JnD4FpKP6RkHAVy2jSvlN67E1sV3MadOIrwXHe85QaKX7q7bSXUjy15wVVIiSGBUb7LuI4sy60XT9pOzx80W4bBLmexS36nshkVsyHHIQsjrevv2vXlZHnURuvInzAiup4AW1Y-K-rJk9Xwf4ckNr2yI7PlQWoCe3vyXM4y2yeyCfIKEd3e2PDTAsBlH5hXQDZY4fpSY6aXK_cW_cltUtm0vreX0nqd6sR2X0ByoHkkrzVhAl2dFHTI_89WOgN5tUfNendZNp29xg4bEZrlPwrUonJy7M5nAmruvmJLAtjPrtfSQFPl-cjwwmDmvArXW3jHy3B5iAyEYs00mt-fcTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 17:44:53</div>
<hr>

<div class="tg-post" id="msg-141334">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
گزارش CNN: وزارت امور خارجه آمریکا به دلیل تنش های احتمالی به سفارت‌های این کشور در خاورمیانه دستور داده است تا برنامه‌هایی را آماده کنند که به آن‌ها اجازه دهد با تعداد محدودی از کارکنان به فعالیت خود ادامه دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/alonews/141334" target="_blank">📅 17:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141333">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKvV06Xg0b2-KwIvwW-Tm3hXvEx6oMPsuv05ljlgU9nYb3l5KzKPQuQFVtK8DqudV5eqjSmXRiEc9UHrH0EU7bX3kEspn_pF0q1T3ekrZY0LmuU0GXaq5pnpUrhbd2jEFKD0hi9TaMWJ5w-8h6oAyhrzXdYxo5rkkveiNAt3kVcfv7djCdHOptebdm1AQWvzkD1KSohoNa5mOlZpflnGE4qKjgCV4o5XKyV7dAgKhWzwbYgda3NB-PbK40jgW36awRqaWI8yE4kxvzmvDQ3d_fl7R5EPWl2D_EUPBx2Wfs8qKsfyTlwB2hsXexWWIx7YvRlekjGP3pnCU-mMUdIiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
نفت آمریکا (WTI): ۸۲.۹۳ دلار
🔴
نفت برنت (معیار قیمت جهانی): ۸۸.۵۴ دلار
🔴
نفت امارات: ۸۹.۴۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/alonews/141333" target="_blank">📅 17:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سیدمحسن نقوی، وزیر کشور پاکستان با استقبال علی‌اکبر پورجمشیدیان قائم‌مقام وزیر کشور به مشهد سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/141332" target="_blank">📅 17:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سوال
:
چرا مجتبی خامنه‌ای توی طول این جنگ هیچ‌وقت جلوی مردم دیده نشده؟
🔴
نقدی : استراتژی دست اونه. دشمن ما جنایتکاره و به هیچ قانونی هم پایبند نیست
🔴
پرسش : یعنی به خاطر مسائل امنیتیه؟
🔴
نقدی : معلومه که به خاطر مسائل امنیتیه. قطعاً دلیل دیگه‌ای وجود نداره
🔴
پرسش : خودتون ایشون رو دیدید؟
🔴
نقدی : بیایید این موضوع رو دیگه ادامه ندیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/141331" target="_blank">📅 17:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141330">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یک هیئت عراقی فردا برای شرکت در مذاکرات مربوط به مسائل امنیتی مشترک به عربستان سعودی سفر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/141330" target="_blank">📅 17:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
حمزه صفوی:
ممکن است بمب اتم داشته باشی اما مردم انقلاب کنند
🔴
اگر بمب اتم هم داشته باشی، باید مسئله تحریم و اجماع جهانی را حل کنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/141329" target="_blank">📅 17:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-wceEVpS6FmKF7H78Fb4Ww0xfoDco6IOxJYHtMEsQ_P5aAkFeJW_wa74fbxzSDexd6Z6XoblV6cTb8Thw3oZstNcmF4S2_YbdK7NuZvrz5mD_5_vrYxKVV0CP0wN6KhCCLEoEUSVAxIeWgfhxB6w8xBWF2BNrWnIazA6oXSmQBR6QSG_sD2B2XBa3T8mGkazbcLis1O05iOHaUSZ_mJnML5Q_kG3Bj0gF4MMGrIho7JchTcmlDYPHhkUeQQHHhZ7nwwdevClyWeDWo7xTjFf5atIbFV7fHSSa24ajKJv28wkdJV-cbbBXrS3yqXaAtWOO_d-_MZhbTs_NruZsWeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قوی‌ترین پاسپورت‌های جهان
🔴
سنگاپور، کره‌جنوبی و ژاپن و امارات دارای قوی‌ترین پاسپورت‌ها
🔴
ایران هم جزو داغون ترین پاسپورت‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/141328" target="_blank">📅 17:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKcnfDJK6zXHMVJueOcMV6g650CwKK2utMPYANbY2b39tMj0e0w0pBMT3fA8k7KGcRjipPw6-1tc_TnpxiMQE3d8FEBAfHbpS-0BOfSyYa5cden1PGsXFsKoq93ywmF8hYqkv3J4pMnkppaqK_WIFg-v3aKP2qLQttG_R2kkmAL8KialBJDCLkVc3hSnPIL_QmYV0na3aMH7oyU10r49ia4JGezSyr5DqbFCBTSNbmAUrvHZOTq892GjRDmGv4th51zeBQ0Zw-8cqKo6mVcIBsfcTlG6I9i9NQLZCddqmLe2712KMdkgpiESsUZKQy_tU7m5brVKky91t8DrbXniKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
دموکرات ها (ترکیب احمق/Dumb و دموکرات)
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141327" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141326">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2FSrm1ODaOs8WdXop1Fto37b_BeI06YRW-9PnlVXdDlthRk4fjGx87bdnOzbbLOLl4JENKykpIO2EpEw15jmFDGnJu2Nz_LOPsZMUNDoxbyHkbPbYaM1ziyifQ0Ki146Q2KDLVzalF81Uqy7Kpc17HcaHdfgTTfDPltNku3eCBKCdeo3doUKtwiTeADIzvBLXXF835gWmZNcgKIKMUbNB-ZI49Ks-4UQYN9h1VLcojttyDQP4Kjq_3qp_CkE5FJ1RfzPBm__N6RmaKPZE3YeIVIWwdlqq_52mbwPUlwQ1mj9BkRZfk3YTHNN9Z9bggipUzqfI1wCKUm325QLBR_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده نیروی قدس سپاه پاسداران، قانی، در جریان بازدید اخیر خود از عراق، طبق گزارش شبکه العربیه، از دولت عراق درخواست کرد فرآیند خلع سلاح گروه‌های مسلح موافق جمهوری اسلامی توسط دولت را به تعویق بیندازد.
به گزارش منابع، قانی اظهار داشت که اعمال انحصار دولت بر سلاح‌ها در حال حاضر به عنوان «ضربه از پشت» به ایران تلقی خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/141326" target="_blank">📅 16:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ee3cab0d0.mp4?token=Lle9GmdEdqzWZwG8CbzD8L1EN37H64bsRB83hi-A75DIQbtA6ke089ZL9jIAeiUagGEFH776dcpTqSY6nHUsDE8MvzEbZlOtJymz0OmhljFYp-kaP_pgoDgv6Q98dGbmugGkqiQhBsVvS72yylt6k4oA5H3YSNBAjz0bC6z3PkGxT5s2USGiP6pCdZv9ILWQrNTSQ7URN13BirHQFwnEzQR6vimO6PSm6uIy7s_dpwBJ1Mpcg0Y1I5OsgkphPv1TWjpugJoej-VG-NKCbhdxJa560cIY2TrbeUNAGlMdjWsXgA40P3110egSyigksiWnQh7FYu3gT48lPuZMQRNYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ee3cab0d0.mp4?token=Lle9GmdEdqzWZwG8CbzD8L1EN37H64bsRB83hi-A75DIQbtA6ke089ZL9jIAeiUagGEFH776dcpTqSY6nHUsDE8MvzEbZlOtJymz0OmhljFYp-kaP_pgoDgv6Q98dGbmugGkqiQhBsVvS72yylt6k4oA5H3YSNBAjz0bC6z3PkGxT5s2USGiP6pCdZv9ILWQrNTSQ7URN13BirHQFwnEzQR6vimO6PSm6uIy7s_dpwBJ1Mpcg0Y1I5OsgkphPv1TWjpugJoej-VG-NKCbhdxJa560cIY2TrbeUNAGlMdjWsXgA40P3110egSyigksiWnQh7FYu3gT48lPuZMQRNYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یدونه جنگنده F16 ارتش ترکیه‌ حین پرواز آموزشی سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/141325" target="_blank">📅 16:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141324">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGPZDaG-iujgFQphI7we_fS6zupIXyWpGTLR9Xc8lEjwbqXQFyn3R-AWyUUvxJ4IAXkN9AZlm1B-lZdBBYE7DMUrc3mUYq4tosfQjHWsZqa1f4vCrEe5yDnUB1P82SC212mpfKtxw5qbcZvJfJ7ppByKYJmD5McRKf8s913x28YH2HABIHEka08Dam_OVpsYKhsitzCeeuY-bUaSZ_fNDeuj-TKmaS1y3qvunh1P8LsZuPOyzLqiX1Rt4q87vCW5oYLaqYZLz0t8rLndRRv5p8ciK9YhNXkGMTVSk9hLQkuAgwL6ANZmgfbXjArKV4CXcSIXoqYiE8Q0cZy6akQHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار فیلد مارشال محسن رضایی با لباس نظامی با وزیر کشور پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/141324" target="_blank">📅 16:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnSjKPlRA-zaq-niN497XyyKMGkD1Puv7kodQ0SQ-FhWqFqtIVtQioh07IB4iFOgMoCi46hctJWQWa0XR322AUYSMoM1iBjc_vYs7q6AsIfc6CoPk_Y5mOJWL1-knOcj6KW1PUbT4nniKMWwrSuZj1ybSW9hBWPNV7AysQuyuBBCKmII1xI9X4nlN85PLDmn2-wJ2gXBi1g5RBRMkxn13-g4zUvLHF1n676GTwPVtvmkgJYMqn994_6ZM9fcEpC5ZPn_9QhiSAVcrokwCQFgDrCtZDJitMUHEI6oLPX-PVLOF2REfI0zAoNOK4QM9_-b1SbQwwAWAZ9WGodh2vFudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه ایرج خواجه امیری خواننده با سابقه و قدیمی در ۹۴سالگی درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/141323" target="_blank">📅 16:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_2BIb7ZAUQuV5Lxbd7rm8mb-4darYTDplD67fvlJPJg5Mrvo7NSNGFsae44vQlToEhdIgVX3lXWxgzpY6eDkWrBYBX1FUBbw_SXmXMwU5dhrN27J13RExIatcsiG_dn70gv9pT7aYBVwiM265KZHx3VN-ZDmCDT87c7YuDzPGN_BAuxuQuyNnvQHhtEdhlj2k_gGQSYXnzF3rX7z0ZAZTPk06WO0Qxof2T6g2v-vsewj01rItgOTzcAaXu4GAXzfkVMQCIQ-FcMIezhnRDfleGivcgODaWe_bEGbsP3L1_gLJso5sAp4K2J1BvQFCfl_AjRWKxBwAgaS1O0aEsGAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی دولت:
گرانی ناشی از فشار اقتصادی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141322" target="_blank">📅 16:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141321">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-kyCKxTwQba5ZB9v_crCF7_W5srxmtOEKA-Q1sWRjkVBQfJGWkM8J3D9UGs4OR_NNyF4_e9DKi13v-b6WAyaVFyq0Fl_K5QClcTnyWe8LvRd7r-EzUFgCpU6qmAJbwl4zbc1rbojgUbhiVE6m5SWVLtQg8vARj10yxvUtxZQI7i-fy3GIs8rCUYjLCl9vWlfuCOsZGZlGnnVJpwEg0Rq0iAMhwQvBRjHarSN_kZWi-wOG3-gr6UfDgfb6Ux9hXjh12VgswuYkG-qpZUCY9lq5wNjVvZ3szbjJbHMm9ej-yj2IsAgKiPR9yp2JXrCsqtDogghVo7nQfVPidL6UPEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
تهدید‌های جانی زیادی علیه من وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/141321" target="_blank">📅 15:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNHYM_GbKlYFFjJj--jIsW_CRLOBfLu3bhG0dfYdpqkA1PKwWbutULk__cKehbNsFMs-uuaRXzF677bpZMZm11LqvrrLHlvZoHiT-0qONcyO2_uQAi31ka9w6TBVXAgoK3y-_CJynY8Hoyfdm5gUysf9rAwrxPs8LvbmP-4ywJdX4HZzUeFQZXMPzz_dE41sXMmQRkl8gm_Q5B1vfiwx_7BxSpcV-Wg_M0XUhu814ZrMj1FxQ4hN55cwH3C5AiBHMc3QpXqU3QTQfoH9J1qlwVHLRN1uO6AVsjZFCDCW22yziaW1ZESieazPuPbxhQJ8xiQ6pIY-RC7PwOJZoaCjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل تخریب ۲۶ ساختمان فلسطینی در نزدیکی جنین را آغاز کرده است.
🔴
هدف از این اقدام، فراهم کردن زمینه برای احداث یک شهرک اسرائیلی عنوان شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/141320" target="_blank">📅 15:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49eca3a5ff.mp4?token=pMyqjG3StwNXp3yvKUPIQ5ECnexZf_qTFLhXqTBUkxOre9IX3fXh2HJ_lf4L0CSyctborN9Vuskj6JvgHJJwvWmMbH6qx09ivvsy7GoIUWx7qcR6x0QJHci79fBnPmxdezjTnGpT3l7qC9RZDccJ6xwZg6XALOBh7cHXP0tIwA-hVUhV-DpZcUzKy3OdQa5vazuCV950kYgKdEqhaFtQTGV6rdrKUqojXj0nGpIlGiwzt0f6N2A-DrzYbEnzbt6RX3xathsPohxCm4ScIFL07hjO8jeYDsT9pkQ_YyKWoeTQle984JgQ45lgkZQSADmIdJurg5-nT1lht9NMBbv7ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49eca3a5ff.mp4?token=pMyqjG3StwNXp3yvKUPIQ5ECnexZf_qTFLhXqTBUkxOre9IX3fXh2HJ_lf4L0CSyctborN9Vuskj6JvgHJJwvWmMbH6qx09ivvsy7GoIUWx7qcR6x0QJHci79fBnPmxdezjTnGpT3l7qC9RZDccJ6xwZg6XALOBh7cHXP0tIwA-hVUhV-DpZcUzKy3OdQa5vazuCV950kYgKdEqhaFtQTGV6rdrKUqojXj0nGpIlGiwzt0f6N2A-DrzYbEnzbt6RX3xathsPohxCm4ScIFL07hjO8jeYDsT9pkQ_YyKWoeTQle984JgQ45lgkZQSADmIdJurg5-nT1lht9NMBbv7ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شروری که با قمه‌کشی، ضرب‌وشتم شهروندان و عربده‌کشی در خیابان‌های تهران اقدام به ایجاد رعب و وحشت می‌کرد و تصاویر اقداماتش را در فضای مجازی منتشر می‌کرد، دستگیر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141319" target="_blank">📅 15:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پی‌بی‌اس به نقل از کاخ سفید: عاقلانه است که ایران با توافق موافقت کند، در غیر این صورت می‌داند چه اتفاقی خواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141318" target="_blank">📅 15:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141317">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b51dddb4a.mp4?token=Y5XU4IC-_oyiT2THKNaXhYaohNrMPId2ijO2iIqJXfdPNfbsLZTkMIdNUQIXpFtxBjgLWDUAwh7H8tMJNsVHOluQ5Lke3nl6O7zDXuP55AWPtmncPGy1L2mvbRyXPjt5-r_IrfXKX64-8khQt2P9_xRDD7mXZJ_wot3yz0WYPWhe-odTs14CaF2ozZ-MwSB2Ihujsv2vRb8Ofn8NKGJFi7Lj3epgdsChKsMZ2MGZ6ImMiY-0wDXbPU5jvs78XrcSYTO-64cMwKyIY-H8Kq_MPmnKcAohU_dAl_mNpebwbl7lT17czquG57k_SpXdzgNo3xCEFI4z9lSLQNyJZ9HsIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b51dddb4a.mp4?token=Y5XU4IC-_oyiT2THKNaXhYaohNrMPId2ijO2iIqJXfdPNfbsLZTkMIdNUQIXpFtxBjgLWDUAwh7H8tMJNsVHOluQ5Lke3nl6O7zDXuP55AWPtmncPGy1L2mvbRyXPjt5-r_IrfXKX64-8khQt2P9_xRDD7mXZJ_wot3yz0WYPWhe-odTs14CaF2ozZ-MwSB2Ihujsv2vRb8Ofn8NKGJFi7Lj3epgdsChKsMZ2MGZ6ImMiY-0wDXbPU5jvs78XrcSYTO-64cMwKyIY-H8Kq_MPmnKcAohU_dAl_mNpebwbl7lT17czquG57k_SpXdzgNo3xCEFI4z9lSLQNyJZ9HsIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت عجیب سواحل جنوب که کاملا نفتی شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/141317" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
آتلانتیک: جنگ با ایران ذخایر موشکی آمریکا را فرسوده و دست ترامپ را بسته است؛ کاهش مهمات دوربرد و کمبود رهگیرهای پاتریوت و تاد، گزینه‌های نظامی واشنگتن را محدود کرده و دیپلماسی را به گزینه‌ای کم‌هزینه‌تر تبدیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/141316" target="_blank">📅 15:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141315">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در جاسک بر اثر عملیات خنثی‌سازی مهمات
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/141315" target="_blank">📅 15:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141314">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پوتین: توقیف کشتی‌های روسیه توسط برخی کشور‌های اروپایی، چیزی بیشتر از «دزدی دریایی» نیست
‏
🔴
اگر اروپا این اقدام را انجام دهد، پاسخ مشابهی خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/141314" target="_blank">📅 15:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141313">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فارس: نرخ خودکشی تو ارتش آمریکا بالا رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141313" target="_blank">📅 15:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141312">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
فارس به نقل از منبع ایرانی: هیچ مذاکره‌ای درباره تمدید آتش‌بس با آمریکا در جریان نیست
🔴
از دیدگاه ایران، آتش‌بس تاریخ شروعی نداشته که چیزی برای تمدید وجود داشته باشد.
🔴
آمریکا ۴۸ ساعت پس از توافق موقت آن را نقض کرد و چند روز بعد از آن خارج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/141312" target="_blank">📅 15:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141311">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / خبرگزاری آناتولی به نقل از منابع پاکستانی مدعی شد ایران و آمریکا با تمدید مهلت ۶۰ روزه مندرج در تفاهم‌نامه اسلام‌آباد موافقت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141311" target="_blank">📅 14:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بلومبرگ: روسیه طی یک سال بیش از ۱.۱ میلیارد دلار مواد معدنی راهبردی با کاربردهای مرتبط با صنایع نظامی وارد کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141310" target="_blank">📅 14:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141309">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: بسته ماندن تنگه هرمز و بالا بودن قیمت‌ها، بر مصرف نفت فشار وارد کرده
🔴
انتظار می‌رود که تقاضای جهانی نفت امسال روزانه ۱.۶ میلیون بشکه کاهش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141309" target="_blank">📅 14:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141308">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند. ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141308" target="_blank">📅 14:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141307">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
۴ ساحل قشم آلوده به نفت شدند
🔴
سواحل سوزا، شیب‌دراز، نقاشه و بخش‌هایی از جزیره هنگام دچار آلودگی نفتی شدند و مدیرکل آلودگی دریایی سازمان محیط‌زیست می‌گوید که علت این آلودگی هنوز مشخص نشده است.
🔴
هماهنگی‌های لازم برای پاکسازی کامل این محدوده انجام شده و پیش‌بینی می‌شود عملیات پاکسازی ساحل تا پایان امروز به‌طور کامل انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141307" target="_blank">📅 14:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141306">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8847ad310.mp4?token=Rw1-tyksDsu5uF9Xg7quAaH4NtL2HRajlgq7z_N1WS605lTw9-rAiI7oymwLS3v0Q5TaB2RGT8gn285oQ3B8PZXA-AHxSAfhfYP1Nadi363B4XKOyzgO_OotiBND_v5SQS9anT0vCtprxWZOSCx1_gMEBnxzpYi50sLcnUffylLuoXjAMp58l8Dl9GWO2vc5egOZXJQn-GYmYxt-yJ9AzqoEvnwu3nFXICIIHfFu55Gn1hiTxCbEW-oKlN3iIjr2u-G1P0ir01NSWL7fmxs1hpJrS3k5Va0yhMb7ejiuoqMCudtuBAG47iSgDcA9y6CpnTlafX97yiK5ni2ltyXjtDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8847ad310.mp4?token=Rw1-tyksDsu5uF9Xg7quAaH4NtL2HRajlgq7z_N1WS605lTw9-rAiI7oymwLS3v0Q5TaB2RGT8gn285oQ3B8PZXA-AHxSAfhfYP1Nadi363B4XKOyzgO_OotiBND_v5SQS9anT0vCtprxWZOSCx1_gMEBnxzpYi50sLcnUffylLuoXjAMp58l8Dl9GWO2vc5egOZXJQn-GYmYxt-yJ9AzqoEvnwu3nFXICIIHfFu55Gn1hiTxCbEW-oKlN3iIjr2u-G1P0ir01NSWL7fmxs1hpJrS3k5Va0yhMb7ejiuoqMCudtuBAG47iSgDcA9y6CpnTlafX97yiK5ni2ltyXjtDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خروج نیروهای آمریکایی از اربیل به سمت ترکیه
🔴
بر اساس ویدئوی منتشرشده، نیروهای آمریکایی بامداد امروز اربیل را ترک کرده و به سمت ترکیه حرکت کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/141306" target="_blank">📅 14:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141305">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بلومبرگ: امارات در صادرات نفت از طریق تنگه هرمز به عراق کمک می‌کند
🔴
نفت خام عراق با بهره‌گیری از زیرساخت‌های انرژی در امارات، برای صادرات به نقاط دیگر جهان ارسال می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141305" target="_blank">📅 14:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141304">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یک منبع ارشد ایرانی به رویترز گفت:
هیچ بحثی برای تمدید آتش‌بس بین آمریکا و ایران وجود ندارد
🔴
در عوض، مذاکرات بر بازگشت احتمالی آمریکا به توافق‌نامه تفاهم (MOU) و یک جدول زمانی برای اجرای تعهدات متمرکز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141304" target="_blank">📅 14:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141303">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcGf-pkTXkICT-Oi605JhwfCton9sfspIu3T9ZB3CBAtsgdtLZrGPKbuONfKg7YiHHCvusPquo8m33-rZyp3gqEcx4OGXYwmg-gYmv2pE_o5Mrkj8WbrDUWoxE5a1Qp-PvyiCVThkART-Usayv_UzSY_YaW5VAAF9-OKSAdosFrVBiUnIiMvbkj17aeBcP_iGKySlzc_fxU9VbRO3TpSWwlbXd2ztyYoWsNQwAUMdw_lSEPqRC2DQzpgmJLYb_Ie1C38PzsqHcz-EoE_pOjRfZLqo8hm_y5W7Wl1iEr1Yjyaw-j6YySnSVwWHn9XDn8yaVGaiG-qQn-hpnJtIXZQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت چندسال قبل حمید رسایی که پس از انتصاب روز گذشته حجت الاسلام طائب توسط مجتبی خامنه‌ای، مجدداً در فضای مجازی درحال انتشار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141303" target="_blank">📅 14:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141301">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پاکستان: روند صلح گسترده‌تر متوقف شده است؛ امیدواریم به زودی از سر گرفته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/141301" target="_blank">📅 14:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141300">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مدیر برق عسلویه حین جمع‌آوری ماینرهای غیرمجاز، از سوی یکی از استخراج‌کنندگان مورد ضرب‌وشتم قرار گرفت و به‌دلیل آسیب جدی به بیمارستان منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141300" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141299">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0GbnbqnRjn0mVcTFQ4J-3-bt14tV5dwPwV3vKNDmjIc0S0-K8TMB2yeysMO4mwIE1PBrnifGyFORps1WvyLMm14ETth6KYJDXr1uhJGe6lrCeOPKy6XifZiORNAklG3ZLyP7l-a581GTbzfcDd3quC7j4AUquCXKRhx7hQr2ctYkLSwqz9oGaI2DScs5Ie8XHq4VRKolKqLTkOg1z05EA8C8e8aw0ghLFSVGyF9Fa_vQmurL4jNxEUAIukAcr0APFNpGgbVTquldpxdaWqKg1dFDAevdyJAXAAYZyasMbfV3sfevgKH42jje0S7rRY_aTBrDcZabJ5ioFd0b2Tn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید نشان  می دهد که چین یک سامانه ناشناس را روی ناو آزمایشی رادارگریز خود نصب کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141299" target="_blank">📅 13:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141298">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLfmUND3nsazuho2FNHyRkKeaTLEQvCv5YK4BXGHh9cVXmnM27_FdWxU0FqlCL5Pnpcra5_1vVwaYRcW8_H9XPB3sOOGU4bUl_LSz5JZTso6S9aNEvQiI9w-sLbcMQBo0DksEWM_fN1xMZWrHhnTWaEYubrLQAmTocqcsWqWH1L6SxYz8l7j4jyabR31kLZKRlxhsatHwPxg4OaPom1hQmYgW28FI5veuBTBu94DQfUQSQGB12Hx9mEWyO6vN1hqAH7g1lH74qUV7GCX7gl9HgnIXYDVESfyslBQpzeyi6-uvNfiAV2moZGnUewtPIx5pXpFVDnFLiKY9n18KQt3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وندی شرمن، معاون پیشین وزیر امور خارجه آمریکا: در آینده قابل پیش‌بینی و شاید برای همیشه، ایران کنترل تنگه هرمز را در دست خواهد داشت
🔴
بعید است اعمال فشار اقتصادی بیشتر از سوی ترامپ، باعث شود رهبران ایران تسلیم شوند یا از مواضع خود عقب‌نشینی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141298" target="_blank">📅 13:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141297">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
گروه‌های حقوق بشری آمریکا علیه دولت ترامپ به دلیل تحریم‌های دیوان کیفری بین‌المللی شکایت کردند
🔴
چهار سازمان حقوق بشری آمریکا به دلیل تحریم‌های اعمال شده علیه دیوان کیفری بین‌الملل، علیه دولت ترامپ شکایت کرده‌اند و استدلال می‌کنند که این اقدامات نقض حقوق اساسی بوده و به صورت غیرقانونی فعالیت‌های حمایتی را محدود می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141297" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141296">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کپلر: تردد کشتی‌ها در تنگه هرمز به پایین‌ترین حد یک هفته اخیر رسید؛ تنها ۸ کشتی روز سه‌شنبه از این آبراه عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141296" target="_blank">📅 13:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
همتی در اجلاس بریکس: بریکس باید از گفت‌وگو به اقدام عملی برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141295" target="_blank">📅 13:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141294">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHiO_gOidujbutcdDrvvdweo5FiH8fMyoBaUIE003jxMMLO2ksQqLiglMPQmOw7R2wcGVZcXKTIYNtuZPhRTJZBuiFlRAJeeNqKn3K4BCoh6fuSqgNr5PsHAyjQOUblAzV5bDTmZBD2wgAej-lCEXeknGd2uCYfD5iMvyMA9DAB6ksc8wxNVmY9iENIC0RkFYF9HMUKNvpzuW5GFOm49eMe0GGxs4Ygz0bbyMQFvr5jtvPwrvdbdUz5bD0LN4hNCZiwFGN-gSLenrQds7QYhmZkMQB3GeE9tv4mg2mpxkxXqNRaN4WRYvH524o5Oxy-w4RRaC4rycpATDCjGJYPrjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: تهدید ایران که منجر به جابه‌جایی مخفیانه ترامپ در آنکارا شد، در آخرین روز نشست ناتو در ۸ جولای آشکار شد.
🔴
اطلاعات آمریکا چندین جریان اطلاعاتی دریافت کرد که نشان‌دهنده تهدید موشکی خاص علیه ایرفورس وان بود، صرف‌نظر از اینکه کدام هواپیما حامل رئیس‌جمهور باشد. یک فرد مسلح به موشک دوش‌پرتاب در نزدیکی محل نشست ناتو مشاهده شد و نیروهای ایرانی دقیقاً می‌دانستند ترامپ در کدام طبقه از ساختمان محل اقامتش در آنکارا مستقر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141294" target="_blank">📅 13:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141293">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
اداره‌ فرودگاه‌های هرمزگان: فعالیت پروازی فرودگاه بین‌المللی بندرعباس از ۲۴ مرداد آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141293" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141292">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA1CCKwYEYrbkJw6z9kAejFj9tTCiP-zOWDBlIq-2lYyKepVwd1j4T5pQtoGhUZbTYlTUFqNmbzCT6ywPsd5VHtAtWH1h3f4bGchvq1spS51xjfu-lSziOecyB1-ovgorKDyLSd0EWpHWRRsNqQBUB_GvPEbQ-ndLjTXtpgHE593jemNe4ISfsOPnVLyWlfgS-LaXTOV0oLV3RJujCQDzjhpkTi8bSDmPX49YQ1Ek7CJKDDqnVqmeDUc0-5xHx3LkX1JhNXRpV5TKs0HRqUYUoOGHzb4UNnJQelMjvgyd3r60jvjMa3cHpULndhAFQ1Tk2t-P5_9zVI9lZZ3_C2NCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس مجله اکونومیست، محبوبیت ترامپ به پایین ترین حالت خود رسیده. حتی از کم ترین محبوبیت دوره اول خودش و حتی بایدن، کم تر شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141292" target="_blank">📅 13:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141291">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65a8eb14e.mp4?token=qmcO84cuDasUAK0rvYX93fefwxbUbdz286YPCA8ZZxwXAHyTd-LF2oULeLhCo0HuRtklrsX13IrnMIEEhYVidJBRR45aX4Z7LQyN2Lyg8e17ee4GsnVKKAo9T0qSt208u22vyyVEZNk_XDqTTen82auTkaQJOsKrDC_qh0qL86ATZUBc4_ytd8SPcVJ-zr_M07jDwqgmcrno-fg1Uu-LJY-FfRziL5ims-JENjwskM0fLzp3nTLnZThxDPftReTllTuTsYhLs_JzB7Snn9GvTCWVuFgQPDqoIZ7_jWnSWPRX9pla1ISqq5y9E-W_tP8UUyOwfTgKHIuC0JdLtnheKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65a8eb14e.mp4?token=qmcO84cuDasUAK0rvYX93fefwxbUbdz286YPCA8ZZxwXAHyTd-LF2oULeLhCo0HuRtklrsX13IrnMIEEhYVidJBRR45aX4Z7LQyN2Lyg8e17ee4GsnVKKAo9T0qSt208u22vyyVEZNk_XDqTTen82auTkaQJOsKrDC_qh0qL86ATZUBc4_ytd8SPcVJ-zr_M07jDwqgmcrno-fg1Uu-LJY-FfRziL5ims-JENjwskM0fLzp3nTLnZThxDPftReTllTuTsYhLs_JzB7Snn9GvTCWVuFgQPDqoIZ7_jWnSWPRX9pla1ISqq5y9E-W_tP8UUyOwfTgKHIuC0JdLtnheKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک کشتی مسافربری در سواحل بالی آتش گرفت
🔴
۱۳۱ نفر در این کشتی بودند که بیشتر آنها توسط کشتی‌های عبوری و امدادگران نجات یافته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141291" target="_blank">📅 13:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141290">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فارس: هزینه اجاره نفتکش‌های غول‌پیکر در مسیر خاورمیانه به چین به‌دلیل افزایش ریسک عبور از تنگه هرمز، از ۲۵ تا ۳۰ هزار دلار به حدود ۵۰۰ هزار دلار در روز رسیده؛ یعنی ۲۰ برابر
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141290" target="_blank">📅 13:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141289">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9e409144.mp4?token=ZWpR7XIHaN3Xoyp2jvS3OVrz1yLCMucLo9a9MdigeS6hipsqF4qhFREPW0JNBV9-43qBzM2ukShshDNuSzNE3PQWWr0mDENUzTw0RfuEJtnCvShjk5YUQAY_2ApK4TDsI6_1P9W2_qAkeIGwTvhdL4G7-_7uBIXs6GRACJlk7RttqooJdqM6oxkosv-quFIiTXjTi5MEgZDf52AmDOB3M00I1AWTn7EUfuaFSzDgm5GecvDyXfmk7Hd8bQkEIU-hUbz0rL2UsAoKHhDw6UB9fh6TPEUohJG4R0nUugjTOOkmbreI2g4ZUJFv4WFoTVBkGA94g3kPnFI3gachF3s-u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9e409144.mp4?token=ZWpR7XIHaN3Xoyp2jvS3OVrz1yLCMucLo9a9MdigeS6hipsqF4qhFREPW0JNBV9-43qBzM2ukShshDNuSzNE3PQWWr0mDENUzTw0RfuEJtnCvShjk5YUQAY_2ApK4TDsI6_1P9W2_qAkeIGwTvhdL4G7-_7uBIXs6GRACJlk7RttqooJdqM6oxkosv-quFIiTXjTi5MEgZDf52AmDOB3M00I1AWTn7EUfuaFSzDgm5GecvDyXfmk7Hd8bQkEIU-hUbz0rL2UsAoKHhDw6UB9fh6TPEUohJG4R0nUugjTOOkmbreI2g4ZUJFv4WFoTVBkGA94g3kPnFI3gachF3s-u4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسعود نیلی: وقتی تفاهم‌نامه منتشر شد گفتم احسنت بر کسانی که توانستند این را از آمریکا بگیرند.
🔴
یک ساعت جنگ بیشتر به ضرر کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141289" target="_blank">📅 12:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141288">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی:
نشت نفت از نفتکشی که در شمال شرق جزیره قبلیه عمان به گل نشسته است.
🔴
انتظار می‌رود نشت نفت از نفتکش کارولین بیزینجی به عمان برسد.
🔴
بادها دسترسی به نفتکش به گل نشسته در نزدیکی عمان را محدود کرده و عملیات نجات را به تأخیر می‌اندازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141288" target="_blank">📅 12:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141287">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
زاکانی: زمان حمله آمریکا، آقا مجتبی تو منزل کنار همسرشون بودن و همسرشون شهید شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/141287" target="_blank">📅 12:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141286">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424fedac1b.mp4?token=tFfY7NZOU00zlwUJmZ5qBWZ_feLhPVkERINBftC7yPhJ5ZqRcoOG_V633vhrp_IjALgW70bD_9nmYohJKUkRWX9Tp_chzroVu_DwolXOEHf1t10yWD_1hVWOtPpxkq2CTzyitYgfwVTqFPerc8YX39Q_ePjLvor_HWnZwQJjBkNDdktscjasVrb5HTRm42f5Yc5jr2V_-S7gqT753wTWv70uC7ZttQE8iW3i5TVcsggsi0QB9KHiT19YsvCocxl1PQ9Px5zacqdz53iqL3zSchJ8_VksirzoaF4L-ujFyZWXTW8rRCp4fvo8qDQmrcV6bfuvPWj2RIs5fs-y5U5KAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424fedac1b.mp4?token=tFfY7NZOU00zlwUJmZ5qBWZ_feLhPVkERINBftC7yPhJ5ZqRcoOG_V633vhrp_IjALgW70bD_9nmYohJKUkRWX9Tp_chzroVu_DwolXOEHf1t10yWD_1hVWOtPpxkq2CTzyitYgfwVTqFPerc8YX39Q_ePjLvor_HWnZwQJjBkNDdktscjasVrb5HTRm42f5Yc5jr2V_-S7gqT753wTWv70uC7ZttQE8iW3i5TVcsggsi0QB9KHiT19YsvCocxl1PQ9Px5zacqdz53iqL3zSchJ8_VksirzoaF4L-ujFyZWXTW8rRCp4fvo8qDQmrcV6bfuvPWj2RIs5fs-y5U5KAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تفاوت خرید گوشت طی سال‌های اخیر را ببینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141286" target="_blank">📅 12:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141284">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK3VkU-j3Gf2WhRvesf_Fep0pptywOAS0P0is8rB9p8yRjTO4rqeuB3a2c-QlyeY1uB8OMuSH9qXejbXmtWtNuEUBzxfyhQvwTm5JwSQV_BJ2vbnRbtcbdp4DzX0wbIa5CGm9BtoPQwJLZCwslNTChGlkywo-cW_DNh5i7_Ct7GtWvy_kupTtgv69_t0ytGzVkjpWrTwDqcBs8jBl_69SoEu1JmFoRfZynFHIVdjjrMoo3nEQrpGa0lckq12-Gu03Dvc236ePcA5ni9JIiDRPBBsB3pf-QeJzYgXreOTcx530VST8ka2ibE3JR-MEnuiUEfaJtuQ6s1yY6FZKtwaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf690f4728.mp4?token=MUsCUDQfKdWOgFiOdd3rHwuo2wQUmD38qKHitLTBwXUXeBPgLNUpWjYG3j9EBjSD59j2LTbK1xT_SH2nQVsDgZRVCXdZPrpwWeAEqiyVn1ig9Eb2YCLUpEBw9m1jVAZwLPxjn9lifW0aiI3ri-PyYiZDIWSRwxVFaGO5F5bGDJ-csY9JyevswTU9oJJdZdvxnWGrainTNS0xjMHMCOxXFgmihQuaTV4g30eU6fD7nlYFQe-yrzDs9VmbDtSHvX9yEqnONyYRf9m782_FJyDr3uMrxoW_zKgMuTo-mID5KE8ChRO7mJAOYrPIpICINWhx-ZSwywbENeIshceEg4PEng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf690f4728.mp4?token=MUsCUDQfKdWOgFiOdd3rHwuo2wQUmD38qKHitLTBwXUXeBPgLNUpWjYG3j9EBjSD59j2LTbK1xT_SH2nQVsDgZRVCXdZPrpwWeAEqiyVn1ig9Eb2YCLUpEBw9m1jVAZwLPxjn9lifW0aiI3ri-PyYiZDIWSRwxVFaGO5F5bGDJ-csY9JyevswTU9oJJdZdvxnWGrainTNS0xjMHMCOxXFgmihQuaTV4g30eU6fD7nlYFQe-yrzDs9VmbDtSHvX9yEqnONyYRf9m782_FJyDr3uMrxoW_zKgMuTo-mID5KE8ChRO7mJAOYrPIpICINWhx-ZSwywbENeIshceEg4PEng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شاید باور نکنید ولی۲۰ سال قبل «پارسا پیروزفر» به دلیل خوشگل بودن زیادی برای همیشه از تلویزیون ممنوع التصویر شد و رفت سینما.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141284" target="_blank">📅 12:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141283">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: وزیر کشورمان پیام مهمی را از سوی نخست‌وزیر و فرمانده ارتش به رهبری ایران منتقل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141283" target="_blank">📅 12:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141282">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
روند صعودی بازار طلا شروع شد   امروز ساعت ۳ یک تحلیل بسیار مهم از طلا و تورم داریم و ساعت ۲۱ قسمت ششم دوره رایگان  «سواد مالی»   حواسا جمعه؟؟
❤️‍🔥</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141282" target="_blank">📅 12:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141281">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9cNoG2R89ROAILefAyMAu_4BVUJ73CiqxIyhrzMWlL9mLCccOv8ipAiKqi7dW6kCdR7T4HTTBcBysgLgZvusoHahSKpFJnsOKisGeqX-Xn8XTHzo2fyYtsQwk_JaoOtmyky9aZqKYJPthNQO5FWPfv_YZ5zHf8bPKHa42zawnbuDv96XfYvYIWlX5azoEztpC8ojrSMuMii2POw9MBfj_XI0wVgFtziVI1kzfnftbLEhRP0DCFq_PjKtJwcnuWzUBK7PCML4qvEpcAku0ljy7QXWHtR640ELbGAV2YzFWeOHK8sdn3j2f5k89H3RIGJBMC_abyLmPDeA2wsnXJ2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حجم نفت رها شده در نزدیکی جزیره قشم که بسیار خطرناک است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141281" target="_blank">📅 11:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141280">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: پرونده میانجیگری بین واشنگتن و تهران را نبسته‌ایم و مدت ۶۰ روز مندرج در یادداشت تفاهم قابل تمدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141280" target="_blank">📅 11:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141279">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cedbc59d6.mp4?token=SGAG_8t_ueKntPONwZeO_L538WS7mxRjVN7WBSoYgvvFYWrePWY66D_JGI6B-p5kxmx3mEjpP8y7kHKYkpPeiPhCCyFqbVo4Kd94GWZJF5UME_cx0RhU44NEI1BKy-N7v2on4yykFxqFN6TsDIPlwvPhMYl45eZg-WcKg4B4CGhcQcr2m0Uo-9o7dFFErgKkp-gWSMq2RH2v1waT8HDY-TPueaKfF8ujw16D4YSw38rNZKUQFYzwG7PVnbYEYGhXedVuhMbgez31hzJVsqB2j9jXNv9ip7BhetChzNXHgxwm9qCUY2z3C9BHrl5dVp6fFH4z4Vzc-QIV1DC5JllLPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cedbc59d6.mp4?token=SGAG_8t_ueKntPONwZeO_L538WS7mxRjVN7WBSoYgvvFYWrePWY66D_JGI6B-p5kxmx3mEjpP8y7kHKYkpPeiPhCCyFqbVo4Kd94GWZJF5UME_cx0RhU44NEI1BKy-N7v2on4yykFxqFN6TsDIPlwvPhMYl45eZg-WcKg4B4CGhcQcr2m0Uo-9o7dFFErgKkp-gWSMq2RH2v1waT8HDY-TPueaKfF8ujw16D4YSw38rNZKUQFYzwG7PVnbYEYGhXedVuhMbgez31hzJVsqB2j9jXNv9ip7BhetChzNXHgxwm9qCUY2z3C9BHrl5dVp6fFH4z4Vzc-QIV1DC5JllLPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های چندسال قبل احمدی نژاد درباره طائب: تعادل روانی نداره و پرونده سازی میکنه برای همه و دو به هم زنی میکنه فقط
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/141279" target="_blank">📅 11:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141278">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG2SsPddmJ2O15UPPxPIk0SVLxqnMi252m37Ef0mJhwz6TJEnhBt-x-OgPsl9punUJAOktiYDnzCM8owRSajdLUHacm-3R2JZDpq8R9fKd5RvBndJWrxRjZl2Wl25hriTHagvv53ZKQRAchL3Dwd-0dcjt05Lzx_4jX3q5o68u0ovwEjOsONXgYnM55lISqLGT5hMW93FZoq7o503BEys-KnzAVkOdSh3yd4-n7Fck0mdQ04xXIkTkd6qUzJ_bdxik-fG4S6S9BU4X-eHDQvSYOEaTQU421HMCkYvJITD63j43FRbhFMMWUIIV1HmoN0u1NQjVidLitEfSnU4zc6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنوب ایران نابود شد
‼️
🔴
لکه‌های نفتی به جنگل‌های حرا در قشم رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/141278" target="_blank">📅 11:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141277">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895ee6189.mp4?token=K1iNO-hWbEiL14W_YeV5_iKzFwrJIdtJqpdiAJFIEVb9gXdOQnee4lp7fdUjgviFhhlrCAv5_CZU7URezGy2y-A94gOUNLeSivDoA2gCR-Gn6ktUcq_vtOB-De4s2wKGENskRfOBVcUBcWXt1OqQ4SiS9a2_N-R5KGzbGnTIdGKBP4iJlDvDJFqYz3rTSIiAa2SBEockuKk9oVKvMeLH2jAwAIzFJAaDol9AtGJm_5YnFz1nkCd_PzZwJRUBwVjGIsKeD9SLuRt2ORRs952_81UR_xMYRJrF5yCfoyoWbcTDZ5abigT-dDsrV8e4x149_w7BS0HCwdwPWubmVRB_Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895ee6189.mp4?token=K1iNO-hWbEiL14W_YeV5_iKzFwrJIdtJqpdiAJFIEVb9gXdOQnee4lp7fdUjgviFhhlrCAv5_CZU7URezGy2y-A94gOUNLeSivDoA2gCR-Gn6ktUcq_vtOB-De4s2wKGENskRfOBVcUBcWXt1OqQ4SiS9a2_N-R5KGzbGnTIdGKBP4iJlDvDJFqYz3rTSIiAa2SBEockuKk9oVKvMeLH2jAwAIzFJAaDol9AtGJm_5YnFz1nkCd_PzZwJRUBwVjGIsKeD9SLuRt2ORRs952_81UR_xMYRJrF5yCfoyoWbcTDZ5abigT-dDsrV8e4x149_w7BS0HCwdwPWubmVRB_Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیه‌ی هردو سینه‌ یه خانم برابر با دیه کامل یه خانم هست ، و دیه کامل یه خانم کمتر از دیه‌ی بیضه سمت چپ یه آقا هست !
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141277" target="_blank">📅 11:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141276">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ارتش آمریکا در دو جنگ اخیر با ایران بیش از ۱٬۴۰۰ موشک و پهپاد را رهگیری کرده است
🔴
به گفته ژنرال جان رافرتی، فرمانده پدافند هوایی و موشکی ارتش آمریکا، نیروهای ارتش آمریکا در جریان جنگ ۱۲روزه ایران و اسرائیل ۱۲۵ موشک بالستیک و در عملیات «خشم حماسی» بیش از ۱٬۲۰۰ تهدید شامل موشک‌های بالستیک، کروز و پهپاد را منهدم یا رهگیری کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141276" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
یک پهپاد ناشناس با پرواز حدود دو ساعته در حریم ممنوعه فرودگاه هانوفر آلمان، دست‌کم ۶ پرواز مسافری را با تأخیر مواجه کرد و یک هواپیمای باری را نیز مجبور به تغییر مسیر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141274" target="_blank">📅 10:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبرگزاری رویترز گزارش داد کره شمالی در آستانه برگزاری رزمایش مشترک «سپر آزادی اولچی» میان آمریکا و کره جنوبی، یک موشک بالستیک شلیک کرده است
🔴
بر اساس این گزارش، موشک شلیک‌شده حدود ۷۰۰ کیلومتر پرواز کرده و سپس در دریا فرود آمده است. رزمایش مشترک آمریکا و کره جنوبی قرار است از ۱۷ تا ۲۷ اوت برگزار شود.
🔴
این پرتاب، یازدهمین آزمایش مشکوک موشک بالستیک کره شمالی در سال ۲۰۲۶ محسوب می‌شود. تحلیلگران کره جنوبی احتمال داده‌اند موشک شلیک‌شده از نوع مافوق‌صوت بوده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141273" target="_blank">📅 10:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سی‌ان‌ان‌: یک روز پس از اینکه ترامپ ادعا کرد تنگه هرمز باز است، مقامات دولت او درباره افزایش قیمت نفت و بنزین هشدار دادند، زیرا «محدودیت‌هایی» جریان انرژی از طریق این آبراه را مسدود کرده
🔴
اداره اطلاعات انرژی ایالات متحده پیش‌بینی خود را در مورد میزان توقف تولید نفت در خاورمیانه در ماه‌های آینده را بالا برده؛ این کاملاً در تضاد با اظهارات خود ترامپ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141272" target="_blank">📅 10:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رئیس‌کل بانک مرکزی: ایران به‌زودی عضو بانک توسعه نوین بریکس می‌شود؛ معتقدیم کشورهای عضو بریکس می‌توانند با پول‌های ملی با یکدیگر تبادلات تجاری داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141271" target="_blank">📅 10:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7-D5s7jqHIRY-uMVxcwV2m-RmWaVDaQkXpi9heblAajwq9doWcj-TqDIz1wq9wCBOycj9h0ItJTu64KzALtQ7XpfCP2mP5lLYzMS8dLQ8MgEzbuVBKBunzkx3mYbrWDQX3OiHPWvaYeDNQq5Pr0sAwjT99skvwkkQLKPbV4Dcrw2-kwDV_XI7LShvXPH5z5dYK-O_Tx7U77dOhQIn33MEv7lLiTg85trefyTGz0xhOWb0k_bn-noH37pip69sleC4IFCJop-8kcoxLxv_dM9ulSrIH1jiiqLPNBgJnwGCilFAdmy3UTewwoDn1SR-a5qOUXYHgyqcHkzQHOZ29MlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اپک‌تایمز: آمریکا ۲۰۰۰ گیمر را به‌دلیل تصمیم‌گیری سریع و عملکرد خوب در شرایط پراسترس، به‌عنوان کنترلر هوایی برج مراقبت فرودگاه‌ها استخدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141270" target="_blank">📅 10:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
الجزیره: روبیو و بسنت از جمله کسانی بودند که در ایرفورس‌وان که به عنوان طعمه استفاده می‌شد، باقی ماندند
🔴
به گفته یک مقام آمریکایی در عملیات انتقال مخفیانه ترامپ، مارکو روبیو (وزیر خارجه) و اسکات بسنت (وزیر خزانه‌داری) به همراه کارکنان کاخ سفید و خبرنگاران، در هواپیمای اصلی (بوئینگ ۷۴۷) ماندند تا به‌عنوان نوعی «طعمه» عمل کنند، در حالی که او با یک جت کوچک‌تر به‌صورت پنهانی به یک پایگاه نظامی در بریتانیا منتقل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141269" target="_blank">📅 10:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، امریکا درباره کوبا: من مطمئنم که تا پایان این دوره ریاست جمهوری آمریکا، کوبا در مسیری غیرقابل بازگشت به سوی آینده‌ای بسیار متفاوت قرار خواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141268" target="_blank">📅 10:17 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbB3gzNbmukDGk2JfjzIyFmT5muiy4K3AP_it11BnWDKklESLsvBIlnUHAYlN9XMZr4FiGfncIA-K4vs_QWdfxx9L1pDBUJxnWT9LXHQ8ogU-L29wvk_g2lGqQEpIiZxZslNtGOJ5hIvBasj_4jwrXqAuhL_aX6laj1bIhJ-iROgMGqg3-R_iFaIu6Gc6FTZivlpPRE9APbEX6JjrF1sSu_G3GaZgmv-iwYLKUjH8m7at5z8cSYlND55RpDXaGCM9pjW260hErYge9YPli07dq7y3_dk3R5rPJciqKMqdWJTr4AQCXuhqli25sHHnLIO4WH3w2cv14CQ72geBDF6lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ایران فعلا تنگه را باز نمی‌کند؛ جلوی امضای توافق با عمان _با جزییاتِ مدنظر آمریکا_ نیز گرفته شد
🔴
مُدل پیشنهادی ایران برای عبور از تنگه (شمالِ تنگه، مسیر ایران و جنوبِ تنگه، مسیر عمان) قرار بود برای ۳۰ روز تست شود و در صورت انعطافِ آمریکا در حوزه «تحریم ها» و «آزادسازی منابعِ ایران»، دائمی گردد که با لجاجت آمریکا فعلا همه چیز متوقف شده است
🔴
دو هفته‌ی آینده، بسیار حساس است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/141267" target="_blank">📅 10:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
وزیر خارجه پاکستان: کشته شدن ۳ نفر از شهروندان ما در حمله روز گذشته به یک کشتی در دریای سرخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141266" target="_blank">📅 10:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
شبکه الجزیره در خبری فوری از اصابت ۴ فروند پهپاد به استان اربیل عراق خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141265" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
الجزیره: قطعاً بین ترامپ و نتانیاهو شکاف ایجاد شده و ممکن است برای یکدیگر به «بار انتخاباتی» تبدیل شده باشند
🔴
هیچ واکنش مستقیمی از سوی دونالد ترامپ، رئیس‌جمهور، یا کاخ سفید [به رد طرح پیشنهادی صلح ترامپ در غزه از سوی اسرائیل] وجود نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/141264" target="_blank">📅 09:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae5a508392.mp4?token=GV8dvDkMZGTjtUjGsO7Ktj0gJPFKvXjnow2Sz72simYTPBDKTPbooXGQNjFa0lDSrCZKGvOYtrr8pdAY12BC26i8oegMgr7j1Iz9HEkndUvy49N2pRauh4_Oq1_HVG6xAkQ4eWLHvNdg9KmPxjwnuwAt4T5zgax1brumsYXJVWti8hslQpZiIN_mAZHnqUoHy587uy1nHBqGlGygry5Mys9trbiUUT8rqenvRdBjRO3o-Kk2Y1cPTOQcQgyVQ4r23MuIMNBoQpj5LIihLfyirfHXs4M_YR0cVbBFxDXYICt0l8hPUlVre3BACZQQMt9r4J6IkbW8zJw21WaXhe33cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae5a508392.mp4?token=GV8dvDkMZGTjtUjGsO7Ktj0gJPFKvXjnow2Sz72simYTPBDKTPbooXGQNjFa0lDSrCZKGvOYtrr8pdAY12BC26i8oegMgr7j1Iz9HEkndUvy49N2pRauh4_Oq1_HVG6xAkQ4eWLHvNdg9KmPxjwnuwAt4T5zgax1brumsYXJVWti8hslQpZiIN_mAZHnqUoHy587uy1nHBqGlGygry5Mys9trbiUUT8rqenvRdBjRO3o-Kk2Y1cPTOQcQgyVQ4r23MuIMNBoQpj5LIihLfyirfHXs4M_YR0cVbBFxDXYICt0l8hPUlVre3BACZQQMt9r4J6IkbW8zJw21WaXhe33cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله توپخانه‌ای اسرائیل به ارتفاعات «علی الطاهر» با گلوله‌های فسفری
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/141263" target="_blank">📅 09:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
هشدار سازمان غذا و دارو: با توصیه هوش مصنوعی دارو نخورید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141262" target="_blank">📅 09:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141261">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
مخالفت عربستان با پیوستن مصر به «توافق دفاعی مکه»
🔴
گزارش میدل‌ایست‌آی از یک تحول راهبردی خبر می‌دهد که ابعاد تنش‌های پنهان میان قاهره و ریاض را آشکار می‌کند؛ عربستان سعودی علی‌رغم فشار آنکارا، با ورود مصر به توافق دفاعی مشترک با ترکیه و پاکستان که هفته گذشته در مکه امضا شد، مخالفت کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141261" target="_blank">📅 09:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141260">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نورالدین الدغیر، خبرنگار الجزیره در تهران، می‌گوید: مذاکرات ایران و آمریکا درباره تنگه هرمز ظاهراً بار دیگر به نقطه آغاز بازگشته و در شرایط فعلی، توپ در زمین واشنگتن است
🔴
به گفته او، ممکن است تهران به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
🔴
با این حال، تلاش‌های دیپلماتیک و میانجی‌گری‌ها متوقف نشده و احتمالاً در روزهای آینده اهمیت بیشتری پیدا خواهند کرد.
🔴
الدغیر معتقد است: میانجی‌گری‌ها می‌توانند نقش مهمی در تعیین مسیر بعدی مذاکرات داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141260" target="_blank">📅 09:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141258">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWcPKSt-LFWrMGOsjEhdt7y1itm837EAofwOAWntsi0I5CUFREtThur5FuPQBWLC2fMFvtzMKHnmKWDqz0mG98SZ3uMQBXiDC7p-s58sKjN7ywJ9-6YOeQzlfBCq6KtpsPfy0lBx1xs_BSyfsOWhnAJYb00zuHgv5l_ZczMZHI33nEfzOWRdMC5O9O3UACEznpvT0O7qel5sAlVkLZPI2VS48q86Fyd5TbXDpkrPjeavOuv26D6hBTyCH-JkXsANDkDIW5ecIKpsYZs0Bkd5RT012nIzh7jUnywUOBdQbd9MgC-ZA1TN3eU7tUh2jaiDuEKzqrMnVoSpogH4Px_LMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0a4d934f1.mp4?token=ggv7sacgVAmV5oMuNWHnmTgMcXdj0M06rQWSNDPx0ZaXPD_cW0uJpU3vj5qZKyOiDh1xdqrGyLdaHYxtxpi4AwLatF2ci7_WvH8E86NSeofF4Znk5bBHNPwre369yxZpjlJ1ecwBiO80O-3nlwTrcNDz5gwW2JWz7b1act_hg7kWs8TNmZzHxdorRfsqbFnzIRMI6IiOKF0x6Jn6D3vBcapD0E-k-3xkcBorZWdeW2QTxSOJEDj8xi41iRFLoZx9IPSCHqxKE1NREOwJPIgO7CrPZw1cDtmDizvvUZ5Q_icszhSJFXczdtqO3slhzbGmYjZTFMIu-HgGPIRO2w7Apw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0a4d934f1.mp4?token=ggv7sacgVAmV5oMuNWHnmTgMcXdj0M06rQWSNDPx0ZaXPD_cW0uJpU3vj5qZKyOiDh1xdqrGyLdaHYxtxpi4AwLatF2ci7_WvH8E86NSeofF4Znk5bBHNPwre369yxZpjlJ1ecwBiO80O-3nlwTrcNDz5gwW2JWz7b1act_hg7kWs8TNmZzHxdorRfsqbFnzIRMI6IiOKF0x6Jn6D3vBcapD0E-k-3xkcBorZWdeW2QTxSOJEDj8xi41iRFLoZx9IPSCHqxKE1NREOwJPIgO7CrPZw1cDtmDizvvUZ5Q_icszhSJFXczdtqO3slhzbGmYjZTFMIu-HgGPIRO2w7Apw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات گسترده اوکراین به روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/141258" target="_blank">📅 09:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141257">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
به گزارش نیویورک تایمز، آمریکا در یک روز حدود ۵۰ فروند موشک رهگیر پاتریوت را در خاورمیانه شلیک کرد که هزینه هر موشک حدود ۴ میلیون دلار است.
🔴
یک کارشناس گفت ترامپ تصور می‌کرد جنگ کوتاه خواهد بود و ذخایر موشک‌های رهگیر پاتریوت را به خطر نخواهد انداخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141257" target="_blank">📅 08:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141256">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0dffaedf3.mp4?token=XJR0o8w_IQxk_RWDGGPqZS6WcfVQiqWtuuzLncYoD9iGShI6uZgHPtlHJ_cR2Dc7njQD5dmOhtIl73ca0urReJAR5l_9qUHZ3W8MD5_ztiyVbnt374GnGjUMiNTs66qRqZTQzJz2pWxh2LpOVjT2zTZ5WVORzc1bCiiK7DuyJBJ8TgZmzeBI2P9UF_Gem9QwmkHHfYvho6cNnQcIfmEz-5kbHCjR6ydpzKpEDY12WULhuUJK6gQuCJohsXUMgAoaXpt4n5Pd3PkIeEYD1fxB3KQLOWgr9BamV_xfyc5ujysh3hSYBZrju8d7eFwGk006q0hnT4YH-5i5jgf481JQoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0dffaedf3.mp4?token=XJR0o8w_IQxk_RWDGGPqZS6WcfVQiqWtuuzLncYoD9iGShI6uZgHPtlHJ_cR2Dc7njQD5dmOhtIl73ca0urReJAR5l_9qUHZ3W8MD5_ztiyVbnt374GnGjUMiNTs66qRqZTQzJz2pWxh2LpOVjT2zTZ5WVORzc1bCiiK7DuyJBJ8TgZmzeBI2P9UF_Gem9QwmkHHfYvho6cNnQcIfmEz-5kbHCjR6ydpzKpEDY12WULhuUJK6gQuCJohsXUMgAoaXpt4n5Pd3PkIeEYD1fxB3KQLOWgr9BamV_xfyc5ujysh3hSYBZrju8d7eFwGk006q0hnT4YH-5i5jgf481JQoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من به ایران اعتماد ندارم، چرا؟ مگه فکر می‌کنید به ایران اعتماد دارم؟
🔴
من آخرین کسی‌ام که به ایران اعتماد می‌کنه مدام به من دروغ گفتن، الان ما کاملاً کنترل تنگه رو در دست داریم
🔴
اونا کنترلش رو ندارند، ما کامل کنترلش می‌کنیم، مال ماست، شاید یه زمانی کاری بکنن و اون‌وقت کارشون تمومه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/141256" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141255">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e1e30aad.mp4?token=qc8wWyQKVf4T5VQk927pbAuXO9iExvme88CjbzBAdtNWN687nst_KNqnHt8uyzNGN4UdyNTHaELIN_FwMIVYPowiIJq6mbYqWGVT4vKTlhk2SuqUdZEYoW1PZ7xvSaAYfMiwfZ9WOpExb7Nvj9dQ48hM4QPPgfuj_JIuLXQg-oMZcLBXSRBROZAIcJvFs7vRVI3ShpVmfLSWEmr3DJ7OqQnZ5EZHnnjFSmeY3iltiU5A4XkfQ-09cIDW2e_bx2595kpAyFs3y79YD0ULDnwBDEFdNa6iS2wSS3A2GIt24JoWgMeHMkkuTI1pC5NHg1fZNcD6YXihhT7XaQlV_r0NKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e1e30aad.mp4?token=qc8wWyQKVf4T5VQk927pbAuXO9iExvme88CjbzBAdtNWN687nst_KNqnHt8uyzNGN4UdyNTHaELIN_FwMIVYPowiIJq6mbYqWGVT4vKTlhk2SuqUdZEYoW1PZ7xvSaAYfMiwfZ9WOpExb7Nvj9dQ48hM4QPPgfuj_JIuLXQg-oMZcLBXSRBROZAIcJvFs7vRVI3ShpVmfLSWEmr3DJ7OqQnZ5EZHnnjFSmeY3iltiU5A4XkfQ-09cIDW2e_bx2595kpAyFs3y79YD0ULDnwBDEFdNa6iS2wSS3A2GIt24JoWgMeHMkkuTI1pC5NHg1fZNcD6YXihhT7XaQlV_r0NKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
تهدیدهای زیادی علیه من هست که شما ازشون خبر ندارید
🔴
هر رئیس‌جمهور تأثیرگذاری تهدیدهای زیادی دریافت می‌کنه، رئیس‌جمهورهای بی‌اهمیت تهدید نمی‌شند
🔴
فکر می‌کنم شاید من تأثیرگذارترین رئیس‌جمهور باشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141255" target="_blank">📅 08:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141254">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ درباره اینکه چرا خودش با ایر فورس وان پرواز نکرد ولی خبرنگارا پرواز کردن : نمی‌دونم، اتفاقاً فکر می‌کنم هواپیمایی که من سوار شدم بیشتر در معرض خطر بود
🔴
خبرنگار : چرا؟ ترامپ : چون فکر می‌کنم همون هواپیمایی بود که احتمال بیشتری داشت هدف قرار بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141254" target="_blank">📅 08:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141253">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65563b805.mp4?token=uPbpRFcMui5nHZKMK6kZ5iwbg0omozFqhckEn75AHd-mRdSKuXk4NDxEU6rl9SWXtYI-3dRXSRZckHL2tF6LBncdlnQx3b8fIJ_Av73h1Qog2kpygft4eLxJmCQ3Qp4rdejFnN4pa06BdxuwwQyXQMRotn1emEMyya-WIIN_eW0iwv9gIvPfXZXyWRaBwEvSDWdMEm_7aTiGmaPqFzbej0yrLCajwh5nrb7sX_o-5HCdUNp5nhdysvpfl2ymEhRoWEw2pt-iVYcV_gDNnVEW5SjhZuEYC0ClIYpzUjF-4QCRkg__i__uM643ZUv2B2UmPtRwIhn-wYFGZh7ugCxxNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65563b805.mp4?token=uPbpRFcMui5nHZKMK6kZ5iwbg0omozFqhckEn75AHd-mRdSKuXk4NDxEU6rl9SWXtYI-3dRXSRZckHL2tF6LBncdlnQx3b8fIJ_Av73h1Qog2kpygft4eLxJmCQ3Qp4rdejFnN4pa06BdxuwwQyXQMRotn1emEMyya-WIIN_eW0iwv9gIvPfXZXyWRaBwEvSDWdMEm_7aTiGmaPqFzbej0yrLCajwh5nrb7sX_o-5HCdUNp5nhdysvpfl2ymEhRoWEw2pt-iVYcV_gDNnVEW5SjhZuEYC0ClIYpzUjF-4QCRkg__i__uM643ZUv2B2UmPtRwIhn-wYFGZh7ugCxxNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
،
درباره نامزدیش :  دوست دارم دوباره تو سال ۲۰۲۸ نامزد بشم، ولی قانون اجازه نمی‌ده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/141253" target="_blank">📅 08:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ee228998.mp4?token=Rim9OcFO3USdbw4n1Mw9hDBhxf5bmxolTzRucCr5leygc0uwW-ixeGzVnb3s7Mv-UWRs27qs3E-j2Jpjy45g2a7HGRv7G2jRH2yt-5NBoKNVVjViSZvFAHcoLR77tr6jLzGSF87yeNTOeT4KSqmcblvP9hQ-EhXwxSzEDkZzTy293LWATHJhkghpmzmfXD9ViJJACQSzaLoe9XzsuyOS1-iVyPGD2LorXAmHhmr22AtLB3ZaDuDeDqzUGY4vMquvx0jxJHw1uQIrQ397acMuyY8KelYF71xDSBRxV81prWsk-oLQSTxm4NhtP-QmUgS2XenwJ5PKqAwL1hArzGtvdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ee228998.mp4?token=Rim9OcFO3USdbw4n1Mw9hDBhxf5bmxolTzRucCr5leygc0uwW-ixeGzVnb3s7Mv-UWRs27qs3E-j2Jpjy45g2a7HGRv7G2jRH2yt-5NBoKNVVjViSZvFAHcoLR77tr6jLzGSF87yeNTOeT4KSqmcblvP9hQ-EhXwxSzEDkZzTy293LWATHJhkghpmzmfXD9ViJJACQSzaLoe9XzsuyOS1-iVyPGD2LorXAmHhmr22AtLB3ZaDuDeDqzUGY4vMquvx0jxJHw1uQIrQ397acMuyY8KelYF71xDSBRxV81prWsk-oLQSTxm4NhtP-QmUgS2XenwJ5PKqAwL1hArzGtvdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
اوضاع ایران داره عالی پیش میره ما کاملاً کنترل تنگه هرمز رو در دست داریم و نیروی دریایی‌مون فوق‌العاده‌ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141252" target="_blank">📅 08:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141251">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e66e57720.mp4?token=rPktAjh2L5p4AiywyCJ9-TYd9gAvFDMBEPO_vuov0N-LHRXrQwfx4NvoXaT9QdMrOELlLP2_WanYdbDPVbkpXVWb--MbWKoML5im37-rhUy-8OR3newr34BTcbwaQhAj1Hb9omlD7jsO1GlT6oTbMa6TtlL0NYfDlGoMtkyaMrIGPna8vmnCzwpWjD2F3RiqetKvagYrnoF92j1Ocr61T7wVSusFDT2fYr6n-yTg6nsfJk2wAV85TvpgSl7Wohc3A5R7iVFdOC9szg80n-JYJsM2-Sln0Fxf5szDMHEPQd9T9e3BB4Nq8LXpSjz5qi7z9UI5OQ4jodgDQY5VK9I3hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e66e57720.mp4?token=rPktAjh2L5p4AiywyCJ9-TYd9gAvFDMBEPO_vuov0N-LHRXrQwfx4NvoXaT9QdMrOELlLP2_WanYdbDPVbkpXVWb--MbWKoML5im37-rhUy-8OR3newr34BTcbwaQhAj1Hb9omlD7jsO1GlT6oTbMa6TtlL0NYfDlGoMtkyaMrIGPna8vmnCzwpWjD2F3RiqetKvagYrnoF92j1Ocr61T7wVSusFDT2fYr6n-yTg6nsfJk2wAV85TvpgSl7Wohc3A5R7iVFdOC9szg80n-JYJsM2-Sln0Fxf5szDMHEPQd9T9e3BB4Nq8LXpSjz5qi7z9UI5OQ4jodgDQY5VK9I3hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شیوه جدید کلاهبرداری: گوشت بوفالو به جای گوساله و گوسفند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/141251" target="_blank">📅 08:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0bRDGgJ1_6-1a4caEaDfnJgOsWld-cjchpsaz_Qh64K1vXw7YKotFe0o9m9iYYWhbDe5l9oyHqeDHy5FMUnx-Jx5WyOYjDPW60sqk0tJKxyJtq_hgv8FACMbrcb8jzLacFtkzYWk7CB9OEjpCCYtkQOV-t9LXXCPFJt4X-JOSacwwqp1T2eH4PZCTlOH2tXWqyMOxLtzHMZ6WWWU3Q8kr8DlTgSqmABloDs3jRVqZ_asrvCGxIXowZK-tU65-2_bxv2Yr9CYR92q_F6J9usIQIH_1FhUnyah52MFq6dx2smIt767UZHOSGlsAftjZ9aUasij9mAL3K8QxgZJ98OaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار نقدی:
پیروز شدیم و به پیروزی ادامه میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/141250" target="_blank">📅 02:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPVaj4QcNdWFXPM0SgyyacVKRTnbRTIsYjcLPlEXklqbryQ8-eBP9MiLmokuVFucg7ICQLb35TAHFyEKtkBO8CwDc3eoC-V5MQLSr8-YU1EhevYvUp9rpNc78H1xuola8y001Lm18NAc0SixuehoUAhA_NdErqoV8OP6lfLgstDX-A_4ucJOsK2FzSR2l9FSkAAH-YnW64zGgyvdUoyOkeUDAExGzYQc8X_QUK-mhVirYbOhSJP9JU6YyXEmy9PIhLE3bGAb0QejjcbVUwgQtk48CB2x1aVUMBwlr7LJHNL_YmFgycDLAxm_XBuYjSpwqqCSxmAkTCAq2R4oQ6KiHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خسارت شرکت ترامپ مدیا در سه ماهه دوم سال به 238 میلیون دلار رسید - در حالی که سال گذشته این رقم 20 میلیون دلار بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/141249" target="_blank">📅 02:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سی ان ان: ترامپ دیگر جنگ نمیخواهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/141248" target="_blank">📅 02:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141246">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دوستان تهرانی صدا رعدوبرق بود نگران نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/141246" target="_blank">📅 02:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141245">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ان‌بی‌سی: ایران نفوذ چهره‌های تندرو را در مراکز تصمیم‌گیری، به‌ویژه در حوزه امنیت و دفاع، تقویت می‌کند.
🔴
این اقدام نشان می‌دهد تهران به جای امتیازدهی سریع، خود را برای احتمال تداوم تشدید تنش و رویارویی آماده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/141245" target="_blank">📅 01:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
صدای جنگنده تو تهران شنیده میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/141244" target="_blank">📅 01:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOhAaEEcxp23D99e40K6xfOVKlB8h1sXWufz3Z4H5mQUoUOKiLjCGx02iYtwWV8_VcOEU6ez7EIbU8s8xQQsYHaFlLzZ87eSxhVtE3K0FePgvMMTA-gHxKCmHlkyhj8UaDkqf4O_fXtpkUFDQVdmA9_uN_VapNEBU1cB9iPGHeF97B06QPhVGYLaUo_zitCtb_gKKvJbgB95IZK702RTAcwwkbJAH8XYxK6VQya3yEhs3_5BNQPkDcMA3K6corBMatpzz5b4eQhgNe_LtSWz0iqRNI6kqFJCxyNOBi30GXKRZCWNKkExvTCj1HmH7QujJWmkD7gsCEv9drVObgfdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: آرزوی شهادت دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/141243" target="_blank">📅 01:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zum36wI-E7VVNO8nzJJTFeYrzRpEUetW1xQtkotBJx60nnNR588n4KDQ5PewxWvCvqdCEiumDo5b9LOW13J5wiVT9x761XMrx3TN_tt41UBS8wmEJc-QF0qR9UXYctUV_Eg0tkaSsviIW4YXSmvutF8_Wn1QdfxNLdgtoHBk10S-Ns-VDvTJBOVtCUBkF4jo_BHBS0h8awMVxb5DQ5m9MCYw0FjITg5iDjON9gv9eo4SD5b61HhfjnYCXqvDZ9t-ZEPtPsCJII_5eUSL1-7OS04LjteW40_3cmqDdICQE4vnT5eD1g5DYSVxsamrkFJuHjdqJZ36eecD3th8N02g6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: نیروهای آمریکایی در طول حملات ایران به پایگاه‌های مستقر در اردن حدود 50 موشک پاتریوت را شلیک کردند. این میزان معادل حدود 200 میلیون دلار در یک روز بود، با توجه به اینکه هر موشک پاتریوت حدود 4 میلیون دلار قیمت دارد.
🔴
ایران از موشک‌هایی با قابلیت تغییر مسیر استفاده کرد تا هزینه‌های سنگینی را تحمیل کند و ذخایر محدود موشک‌های پاتریوت را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/141242" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbUpgixL5Y3XSk7jIOKvRgj1yicaZQWh2UmyH8SXMiPFAqVAk7kOkO4BEBKkKhIPfPesC3oh5QQ8OLhgtP7-9k8JfORiETrZK39tLKXzC4crntH035p1fD8cFdamQqhKSJQtqns5G8RqI54yL4wOgsNiHeA907POXajdshnBmJd97wWv1M489zRoPUXOVNGnuHbSVVxPoK8K9vIHUwux-LB21OS_62DG7o7AvvdpV6UlCJTuBo0JcEdhiMqTFTE3Jp1TXwVvDTnXgDYfHiqmd8G6DIB617v5_8_FCix6nBcD5DCaOeUWKpMzXEKPE2oHCJUVuXNKpFeGShaHOH46ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/141241" target="_blank">📅 00:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLElwHeWTJpD0VEk95kiCS9Pqva_IrncgtEoZ0WWpLl3Z16eD7YW9ZCT04NJ4OIoLPQvPouiwYFl1lKW5QvGvzTXXPx5wfmxuXC8IbtB2VNkBRVjhD37q7Gvm3n9_p867tVRpOr9feasO0ulpc9MG1Z3291wcGqlY5VzDz_MHOHcYeAen5ONuh_xsHxZYwP3JlEs8D-v908hWUiMIXEMUSoTfhhWd-mDQza___snVMQdayv8f3RsdKxEnSt3tBXO65ZwWeVJwCyjLukZGfgOAQuOdGnHYfX7JPsYu76BIV4t606g1yqxI0cXtE4M3tzPkq1CfCKNYT7irz0yfLFFGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت به ۸۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/141240" target="_blank">📅 00:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf2v9bR6LlwdjCvLnpDD4fs_O2ja4wRMOqyE1xPUtFrVyHeKGt_KiUCaVTsXAstJjrMCa6bYl1eveOgIlqWUhZL3Qb3id87EE7PYsLQqyp13ZtMqP1XHBI6lqyc2ozAgwXykb_tUa2xbA26i1IXqvnHLmlaekpf73TrLgYE8pm1lZ0lzMvtQSWbxSC7RLRmq1RRSs8Dt64WwUPam7IcI-5tfUVIk-odrCNHUo_RCNYTmgFQ6TZi98Uv29Ojupq4ERgxWLFbXTUomgkNtyKPDmYTrjj3Owl-mtaT-of6uY2FrFqqBSRjj8zOB3YOYNMC5FrWZ2ZwiDnWkHbNKSLs4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک :
پایگاه ماه آلفا شگفت انگیز خواهد بود. ما این پایگاه را طوری خواهیم ساخت تا هرکی بخواد بتونه به ماه بره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/141239" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141237">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/141237" target="_blank">📅 00:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تسنیم در یک خبر اختصاصی مدعی شد عربستان سعودی درخواستی محرمانه به حوثی ها داده تا جنگ را متوقف کنند که با رد درخواست از طرف انصارالله رو‌به‌رو شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/141234" target="_blank">📅 00:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیروهای مسلح یمن: حملۀ امروز ما به مواضع نیروهای وابسته به سعودی با دقت بالایی انجام شد و ده‌ها کشته و زخمی به‌جا گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/141233" target="_blank">📅 23:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
جروزالم‌پست گزارش داده سه هفته پس از آغاز طرح آزمایشی خلع سلاح حزب‌الله، ارتش لبنان وارد برخی مناطق شده و چند انبار سلاح و مهمات را کشف کرده است.
🔴
با این حال، یک مقام مسئول گفته اقدامات انجام‌شده «هنوز کافی نیست»؛ ارزیابی‌ای که نشان می‌دهد اجرای این طرح با موانع جدی و سرعتی کمتر از انتظار روبه‌روست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/141232" target="_blank">📅 23:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الجزیره: ایران و آمریکا در حال تعیین «هزینه ورود احتمالی به مذاکرات» هستند/ این رسانه می‌گوید: هیچ‌یک از طرفین خواهان جنگ تمام‌عیار نیستند، اما دستیابی به صلح دشوارتر از پیروزی در جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/141231" target="_blank">📅 23:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE-l2o_hRBsmFxfKVbxFV_Der57ch6H5-KM48nxxqIT1yCcvXoglQed-re1jxUVtvyj1tEZBDfrBBnDD5eN9c5XHPnybVMSY9aFtJFHjFNF3TnBuDxPC0E4Ax_rtbvIDz27n8q3lepQyuzUzDk8UPI3fcL4zlbOI3bdcFPFFCiRUwve8y17BYdyTPTL3doriiN3QNOgZAKM1fcX3TE9wuqF5dzTsGwOPOoL7KwwbWeydKrp7afafzSZhrcQo3hDrhHqXGyhH_lbnkVqnxrFb_B-utcP8_yVVaPAUGEKafM-pWh5UKVGwSTxXccEA_SD02vFD6xkGMGWsN8c_aEwZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تعدادی پهپاد رو به سمت روسیه فرستاده، طبق ادعای منابع روسی، تخمین زده میشه حدود ۴۰۰ پهپاد بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/141230" target="_blank">📅 23:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزیر کشور پاکستان در جریان سفر به تهران پس از دیدار با همتای ایرانی خود اعلام کرد: پیام نخست‌وزیر و فرمانده ارتش پاکستان به رئیس جمهور ایران منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/141228" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141227">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMBQcuXDxUvjrQbhgoueH3T3csXs_qfURqUoRRkfkm7xWJuOIu1qtOQbcwWMNX2CYg0nsJlpwD-s4sIpahWcZJtfOYZpBJ8LTli1dxEDYMwBuO6JJPUz2Q5cJt3Q9jyt2U1UBDlg8TtneDw0dwdGEdernt_MDXcKEOt4jsQvtjbGs-7XFW1KWHgAtjT3oLS7J67KLt4bU98xAiyn9OksQzaNNNKyDAk6yLyRhwln0BjY0C3PTWUlN2ZFcdpSpHr3p9Ood28_VoUjvfdyssc9iz6_PpMJR5aQcfAn_IEq9u481RbnmOEZIhuTgoTRS_IaIsCd2NxrNxS_FfLJQq6XdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مجتبی شش تندرو جدید را برای رهبری جنگ بعدی ایران منصوب می‌کند
با وجود شایعات فزاینده درباره سلامت رهبر عالی‌رتبه مجتبی خامنه‌ای، تهران ادعا می‌کند که او شش تندرو از رژیم را برای رهبری جنگ بعدی ایران منصوب کرده است؛ پیامی نگران‌کننده برای اسرائیل و ایالات متحده مبنی بر اینکه رژیم در حال تشدید تنش‌هاست، نه عقب‌نشینی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/141227" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141226">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=ONFAMhtos6T4i0BhiU5X1909bHBAD4cFa3xM1ys5NAtJQvzSnfQ6f94McyjbD4L_eyAPTgqBKfQU5BjyPC4LyqMfOWTt-rivkVcWYtIGc2lnkOB-x6feF8HTMdz4HNJwh5DiPEgNgtbTo_qBL-cw0KFJhh38Bn6nRsXy9LbUPpmHYhiTIYZ4t8SDhUqwluv7Bqg959aNSvzFcBQcsLTK1F_e8ISkLF-_prWYiqnlpkq8Dw3jel4wPIv4aXf7fZrQuYsKuy66j_1M41ABTqwv8QyPzfp2v4fXyofOWIK8INdhf0ipM6kUHZt1HWpO2JYWuaQPUYd3XLc3YoFQ41LzSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7021b6ac.mp4?token=ONFAMhtos6T4i0BhiU5X1909bHBAD4cFa3xM1ys5NAtJQvzSnfQ6f94McyjbD4L_eyAPTgqBKfQU5BjyPC4LyqMfOWTt-rivkVcWYtIGc2lnkOB-x6feF8HTMdz4HNJwh5DiPEgNgtbTo_qBL-cw0KFJhh38Bn6nRsXy9LbUPpmHYhiTIYZ4t8SDhUqwluv7Bqg959aNSvzFcBQcsLTK1F_e8ISkLF-_prWYiqnlpkq8Dw3jel4wPIv4aXf7fZrQuYsKuy66j_1M41ABTqwv8QyPzfp2v4fXyofOWIK8INdhf0ipM6kUHZt1HWpO2JYWuaQPUYd3XLc3YoFQ41LzSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار نقدی: بعد از جنگ، جمهوری اسلامی طرفداران زیادی در دنیا پیدا کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/141226" target="_blank">📅 23:22 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
