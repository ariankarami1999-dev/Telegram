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
<img src="https://cdn5.telesco.pe/file/gYXRjYA--e2f-iYQISvgNOt1GSi4kECofcLLbhuqh0lk06R26WokZuLVuZrLwJY2mbNTjHNkbifvFaCZYJUuwKiLVCxYmdcqruuHEkp68b1bYO8qJ8Z0uk6tHksQYPL3stfvHiVlFA3EuHKEsVd7PhAgeGBrhz5gf6YUJqFRnu7U8eyAJ3bDQKJrBryWBnxAv0ZkG1S22fU5JTKdb3WlUo3QR6pUgGLGeUUlJeGAvQRFUX9lBAuiz55hAjEJBmFaqoallDY-SZDXN70UMdsF2wHygizOcjHD4Ma5Ho8NH5dTyA-04mjt4ihwktRs4C_tNOYhUamkl8adf1xDuieLRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 397K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 12:18:18</div>
<hr>

<div class="tg-post" id="msg-107480">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA4eVSwz4kCQcw7blEtO92Wmg4bjmUWx5LMNv5DquGxazsGa7pOxUk0rfkg5WjQviP02SILnzhZBVJB0YmJyQ5yv0u170fdH5DuLBnL0xJXiNslTSWNmesADfsWb3Pi5j2J_AgFaRKKXKP8RqzIdZUmfpAq6payzo7ueOg7gjS7ZYlPXpjmI3cPQxyONs7rd10qttUFGB-kvLkreA47235QjJxSwk36YHlMHXTFE0r6vPLHLqKJO12Di_Xd-li3hKrgcLvpzESJOCssqN_V2od-fTS846SFwPPaqyJ8MCojf15aRJgbId8GMxDlKT942BeE7cntNuBNBVBM5f2puJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 673 · <a href="https://t.me/Futball180TV/107480" target="_blank">📅 12:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=LebN8hIEF8d6NJoQX7C_OPhgm7WocEvaSSfXmGS8F91wu74kRm5jP_yWpjYagAZx9UaDERDdJqjz5NKTqEN70i7cDUu5HmzKbx1Wj31tDkH0AeZ3umDNHhOG5XEAtobcQy5VgEX9wo0JgWyzzREr_bgDTQguOB6YRnbkkoG3EjbweZS09Fan0bNmAtI1VURaMseoH4TwWz8wh3K_W_KJa2PnZIZDQlC1vmGU763og1RTotWAqZGHi5QyEybYCSW2NxX-oajIJ2DMW3Iuf3dbAiqijc6ORz6FNk0lu9ypDqhV6smNbWO1XxfrdqztbP9iVxLS5B3RXjMZF_lWtpWqvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=LebN8hIEF8d6NJoQX7C_OPhgm7WocEvaSSfXmGS8F91wu74kRm5jP_yWpjYagAZx9UaDERDdJqjz5NKTqEN70i7cDUu5HmzKbx1Wj31tDkH0AeZ3umDNHhOG5XEAtobcQy5VgEX9wo0JgWyzzREr_bgDTQguOB6YRnbkkoG3EjbweZS09Fan0bNmAtI1VURaMseoH4TwWz8wh3K_W_KJa2PnZIZDQlC1vmGU763og1RTotWAqZGHi5QyEybYCSW2NxX-oajIJ2DMW3Iuf3dbAiqijc6ORz6FNk0lu9ypDqhV6smNbWO1XxfrdqztbP9iVxLS5B3RXjMZF_lWtpWqvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
تشکر عادل فردوسی‌پور از ابوطالب‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/Futball180TV/107479" target="_blank">📅 11:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evl2uDL9fuPycLsSgxfMmXPfTtvgBSUhSl7i3kHNN3335bayp712zggeb37pHPCrL-y4bD-cJTAHTty-1oxrG7IexdQ7KNRRQkzhLiF4K1bFwdPBWDrha7oJqTYOc44d7qSlLAsjHCsfrxXpOqTQqxGW4D1Mx9-pobS9kNmSmk2jDXyGOdlRIVR2yo4HzSRO4abUKv_DOH30vZrklHhkJfcTyHEuXNN5NFs3s2AmX-oWAR0Ks9QdNpJ_cPYqBFrVElLBDhkUK5AjYhBGWG7gPNQkxP8OadxXxC7WvPh9whEgmO-bJeiQYPcA3L5p_pL--K-6naPVFE_p6EErzMsgfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
وضعیت دلار تا این لحظه: ۲۵۰ هزار تومان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/107478" target="_blank">📅 11:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRv7TvVpFO_1Ov9Q2oPoirgLomsp-BPnW8oacR1OUKdMETntVH3Xme2JfSNsdfVO05qzJcxHns2IvhLeRR6KZAsdNqUrfmRbVVby5hKv3kuCWe6_egFde1W2ef-e9H2UT7_zKpCanrYDB3N-g0x_ZA14JyPyOJoheVgdP8EJYqfzrrAA1UBXKMZPoGR7DKOEarMg2CmmbwFQuwghzBWKJj-BJxO4HlFulV4eE-Qh5sSUvLaxUE_rbbtmp5aptfCY20c0_zO-ONdXN24147r0aZijHTLUCXFuW4VEJAYfgmmab0SREsseMhfeaHt6i--crGS_DtPlyTezBn5CpsPF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
🇪🇸
مقایسه آمار رافینیا زیر نظر فلیک‌و ژاوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/107477" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrgmKHRi41wI4DAFhV55eGzLZbpkcvrCMWJwhbeoXoavbD-OM1-2zTEn8MghuYGR4574lI9IpdRelNLLeHHlYiv0FtHv6xRzarqBcac-aqYKNZE4EA36Tg6VVP_Fxudvs80FtOpVfWiorciyN-3fCvDzN7TsseGzOuaknaPWGBIR-8nYg35aLHeZyxASE9Th1EqqV_xmbMQl00myEnLKQtkU_r7iCQL0x6DpcnGNxNoDwqgGgybMqcqw4jViNvD9yfwjHxwDDOV0OapsL5f2mDNDofYK5ME8nUXpOcWNUSE7VhfyaPOdU4Fxb_mcwE-gAtwWmFA4Z5WNIy5rnzBhbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
بازیکنانی با بیشترین گل‌زده از روی ضربه آزاد در تاریخ فوتبال؛ لیونل‌مسی تنها دو گل تا تاریخ‌سازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/107476" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107475" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/107475" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107474">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh1ypW7yiKyRwgKtlXHIbcFFTa-coCACGpJwT5eodkG0QsugZ0djof3ktK9PDeczzzQu9LersSq1sys9nkZcs6u29lCq62HQl15HZ-tEHe1mdTNuNrR7qoElyoSUHO9tjXjFFbqSfnUJel3rfLEIKGrkERxuRBdnRtCuSFmp5eBMI4qIWnK6MypjdVWShYq1ohuLdULX0GV42qXgCGo3QJ0GmJo5qKnFgB-p13Vc5eWO9P3MOzAFK2lbCbnp4JKjgOAKFMZKKDqxIw2Z_XwF9Xb7s7CdGUN9YKeXFQ68mSQNx628HRhblAkcZCjO2P6e3qmU1j2FLpXw5CQed-BDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/107474" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3862876082.mp4?token=k_eA22j8H2rwaTQjn8SYD6VpP-vBoExWzfNT3kil9V5zlq1z5INqYkFIpjw_gzCrEqMiz3p33JK0etLNE9ofaN1imNB-AP5ZvvUjzvC7OVd0kENa6_7AoY6IieU4S9gLNRVXIzGFHi0p1hKZFsPLFyCOu5yAThth55ro1EYw-YQ8tsYW9K95OXh2FCJ9zGbkptWyU8O67oNjuNE_1GkY1bz-mxclfTZP9ZG1aocOTZK6nmNr3NEWRuYh5uHvpJJPtkeO15Cb3z9zhP-iafDTYjzdVitxN00yyHbLgAGbssan3iC-ziENDB4HJGwmt_OWrQNw96l9wijeoY2Y7R1Rmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3862876082.mp4?token=k_eA22j8H2rwaTQjn8SYD6VpP-vBoExWzfNT3kil9V5zlq1z5INqYkFIpjw_gzCrEqMiz3p33JK0etLNE9ofaN1imNB-AP5ZvvUjzvC7OVd0kENa6_7AoY6IieU4S9gLNRVXIzGFHi0p1hKZFsPLFyCOu5yAThth55ro1EYw-YQ8tsYW9K95OXh2FCJ9zGbkptWyU8O67oNjuNE_1GkY1bz-mxclfTZP9ZG1aocOTZK6nmNr3NEWRuYh5uHvpJJPtkeO15Cb3z9zhP-iafDTYjzdVitxN00yyHbLgAGbssan3iC-ziENDB4HJGwmt_OWrQNw96l9wijeoY2Y7R1Rmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
انجام پدیکور فرشاد احمدزاده بازیکن فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/107473" target="_blank">📅 11:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
‼️
⚠️
ضرب و شتم دو نوجوان سنندجی بدون گواهینامه توسط نیروی انتظامی که‌در فضای مجازی حسابی جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/Futball180TV/107472" target="_blank">📅 10:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=h5_6c1MgxHsPktNNuT52HzRsyiWsCc2hsQNxJERRr0nB54l-B6IMmEJg6lyBLdfbYwrWczwXXlCi3IrRkb6izM3Z1Y-RtGClMHff-mMAvyi-AzkijS_Id_HNbezR9axuJKMDToG0QREwfi5EZDUF1uaQ9ptCfqxHWLu32PLJyq3g1FCfBXJB6DJlfspny0eePeVyPuGdqmsy3lq5HJRpwf3zEkpNjv_bS7Huf5Ri_DSb3fnVCLV1LNDH7ADMP80W3dkVXMwy3cDVM0VWk6563feDxO67JsTlgnuzmI3JNFDeS5TmXjhooVTaDQ_74hyBp9RlICfiNRXqJGedzxsjvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=h5_6c1MgxHsPktNNuT52HzRsyiWsCc2hsQNxJERRr0nB54l-B6IMmEJg6lyBLdfbYwrWczwXXlCi3IrRkb6izM3Z1Y-RtGClMHff-mMAvyi-AzkijS_Id_HNbezR9axuJKMDToG0QREwfi5EZDUF1uaQ9ptCfqxHWLu32PLJyq3g1FCfBXJB6DJlfspny0eePeVyPuGdqmsy3lq5HJRpwf3zEkpNjv_bS7Huf5Ri_DSb3fnVCLV1LNDH7ADMP80W3dkVXMwy3cDVM0VWk6563feDxO67JsTlgnuzmI3JNFDeS5TmXjhooVTaDQ_74hyBp9RlICfiNRXqJGedzxsjvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از عجیب‌ترین مصاحبه‌های امیرحسین قیاسی که پس از یکسال مجدد وایرال شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/107471" target="_blank">📅 10:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107470">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=C4Dhw_yqARJVS7XDFJXdZUDmY4o0otoWi1SSWZgKlA6XGaIkKosj1LJ0jMdexnPRjgU_AUfThQsq5_k54SZMacyghmv1Arlx9D2QxmM7_lALDSJ4iMBLVSV-8-ZPjXLVYAWCpHOMj7SZvhC6Bl9NBGalyW9fyB_B4dCiXbKDg7AhJuXdhiPo1ONMzuFo3StcKDaVtEVxFJ41ysk-q3rZtijSfwglUTCZxYL-G7L_GqjreCRHgkAub8WpshiqHAGFYlsCMK2FtRilb8T4hXRr7Gmul78jwFMoYCrpHSu_K1od1NMYJANDRDl5lWSuGdd-13sIoECwmfmtYv2E5-qk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=C4Dhw_yqARJVS7XDFJXdZUDmY4o0otoWi1SSWZgKlA6XGaIkKosj1LJ0jMdexnPRjgU_AUfThQsq5_k54SZMacyghmv1Arlx9D2QxmM7_lALDSJ4iMBLVSV-8-ZPjXLVYAWCpHOMj7SZvhC6Bl9NBGalyW9fyB_B4dCiXbKDg7AhJuXdhiPo1ONMzuFo3StcKDaVtEVxFJ41ysk-q3rZtijSfwglUTCZxYL-G7L_GqjreCRHgkAub8WpshiqHAGFYlsCMK2FtRilb8T4hXRr7Gmul78jwFMoYCrpHSu_K1od1NMYJANDRDl5lWSuGdd-13sIoECwmfmtYv2E5-qk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد نصرتی بازیکن سابق تیم‌ملی: آقای قلعه‌نویی آن مصاحبه مهدی‌قایدی را نادیده بگیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/107470" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107469">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=RF2vxL5xxJ0NrSpBAcEQWBnBWQ02YZPkyp43RUFpXp6Srm9kxiAZm_PO346Lue6Gg20KhjtM4nn5bnR2lgPJE92T2XfhmeP9PXrM_M7jYRKHA2LYaAHa_wbDx3m7Hunw2YxYZB4QQUeZa1l9o4S_K9cVyUKC887xiJXC-Hobn_9KlwrI2hTfjTXM7pVQjhu6AfreKv9pMASJAmj6lSYoRgAQVZgBi4FL9Dsn-wo4TxqJJ0b2JNTUiKl8WvIo-vbVk1xI3oYADZV9dgew_WKuMH9LlJvmhm1sstW7cKOH1elGL97QfoZPXgWP-B5sY20IEkmB9iqKQXy6Yq8NH7qMJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=RF2vxL5xxJ0NrSpBAcEQWBnBWQ02YZPkyp43RUFpXp6Srm9kxiAZm_PO346Lue6Gg20KhjtM4nn5bnR2lgPJE92T2XfhmeP9PXrM_M7jYRKHA2LYaAHa_wbDx3m7Hunw2YxYZB4QQUeZa1l9o4S_K9cVyUKC887xiJXC-Hobn_9KlwrI2hTfjTXM7pVQjhu6AfreKv9pMASJAmj6lSYoRgAQVZgBi4FL9Dsn-wo4TxqJJ0b2JNTUiKl8WvIo-vbVk1xI3oYADZV9dgew_WKuMH9LlJvmhm1sstW7cKOH1elGL97QfoZPXgWP-B5sY20IEkmB9iqKQXy6Yq8NH7qMJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تشکر هانی رامبد از مردم ایران بابت‌ حواشی اخیر: مرسی از حمایتتون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/107469" target="_blank">📅 09:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107468">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/capaLf0LO-lhBemUNRPKEbC_atPeUVCeh1KhdBePE7vBfJ5qOKXYT2zVgzgHYtgF2u9eGkaHnHLud9bSXiQgO1ENvhOSAqWAzX05ZbvF9VJWuHnB4NJhyjYCU71KaTPNGNjMtCeYobQ3D_NP3CbHeDiddOKXBJvee_EBp6XvybhtKTTJ6bT0cQUcDHw61fYIPxMKFjeMLGaVeN5TfcqhjSVeDIojk4jh3DmUUKxVyv5vhi5Ol0VzwbhgoPv8fAWk3sP0d8EFxfuxIwUkiIK8YvV0qdz_ARIeCpRZT3aKx03PVA_7AUEIO9kEvZTiUssHl_6MSJvcrWtRhi9pncdwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‼️
تیم ملی اسپانیا هیچ‌گاه در دیدارهایی که لامین یامال را در ترکیب اصلی داشته، شکست نخورده :
🔴
۲۹ بازی؛ ۲۳ برد؛ ۶ تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/107468" target="_blank">📅 09:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107467">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=DSiijoyV2yFYRVLV9rY-hBkq67bC9V0zSu-hytffCzvDJKtVLu-ECsXnJaSkgp3OvQ8T1HKmLuMe3OrIrsrw6Lh74Oj4jO6teOVFZ5F-4E6fRHLzWa_VLPR1-_1pKB0kx6GdllOkKkWRLImEuIFhobPBeJQDdK8M_hJMA2VJG4vBjW9tGFc0fA6narC3jBmm_oAV2-QNTt8678lR56xLYl2BCoO6eRg7-RdWAgNykSm03X0_vNh72xmoZF_FwYDvczosdvTkS3YdB_vQxYOLspnymQMmJrzX5L-UkZfy_-r4mk-etiKcRQ8cari7Phk5gPFDrj0MUTB3fnrz-TULazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=DSiijoyV2yFYRVLV9rY-hBkq67bC9V0zSu-hytffCzvDJKtVLu-ECsXnJaSkgp3OvQ8T1HKmLuMe3OrIrsrw6Lh74Oj4jO6teOVFZ5F-4E6fRHLzWa_VLPR1-_1pKB0kx6GdllOkKkWRLImEuIFhobPBeJQDdK8M_hJMA2VJG4vBjW9tGFc0fA6narC3jBmm_oAV2-QNTt8678lR56xLYl2BCoO6eRg7-RdWAgNykSm03X0_vNh72xmoZF_FwYDvczosdvTkS3YdB_vQxYOLspnymQMmJrzX5L-UkZfy_-r4mk-etiKcRQ8cari7Phk5gPFDrj0MUTB3fnrz-TULazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
پرونده قهرمان فصل نیمه تمام؛
جنگ بر سر جام نامرئی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107467" target="_blank">📅 08:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107466">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107466" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107465">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/107465" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107464">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107464" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107463">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYB-d8jMOXMJB8lR5kd36tUSQ9EyhrCmUytf9qw9C9s4B2uYg2zToFvfvaewy_czhRJSjhYNcz7BHZXysbJG9dzLlcBfA96377MzAAUd_oOZKAG4VgzblC9jbPswPLA-2WR4dS-_lnC66ijWO_iCN04d4fcPDEZFGONdK1guGpYANtqD7WyzVaHObGGhdbOGu3u2j_nHDLpyzCZbQbDgdpWp6giz-xsYqrKnRTtgt94EZgVjNjJG7gy84iBu7HzKbxFgr2hV72GyMP7yM7T6qAvvkSIViwcXIMUyAiEqbTfvSr2Vp7Jjb5QWycNl8YRdRiO8AG81AfbQYs04MWJo-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
❌
⭕️
🇮🇷
با اعلام سخنگوی فدراسیون، قراره جام فصل گذشته لیگ برتر به شهدای میناب تقدیم بشه و استقلال یه لوح یادگاری بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107463" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107462">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=Ruvr_vOsNFfkF1BW3YnttU_DEbxv7eNtVZtL0Vb7sxobjcpGtLnrJgJX9ERFLgrfmGgysq9Sd_kRp02wlVRLYPfrJXNjPqfB2huO_r2UDLGX3bjjc7M1f-E2QLSmk1hiD3_FoLMhuf8bkeu2_SruEUoa6uFQUpR3xJcFDD8MDBGJTpcoO4n5d4cACGJEQspH_thk3KH96V2bg0jK2-KeaOggQKLEQh4xSFDW3o_xPGrNQ75oBk9WIDPSn9cdrg1uIw5akfjau8uKbUxlB5VpIzVNoPzYy2QSESh9fw1_2B1sSI7Pgi41Havu37I0zMhsAuRnODD6uZR_2Wk3Dp8yA19Hxvxr0fiR0zwvBL9L8QhtT8J5GpA-_4ZRIe67nVn_AyAEuSWsMyvuZDwMul8mzTuemXAhVwAZCEzSqpwF_5EDv2fqg5IMN1SV0wzuKElRYldl3UdG1mi66cWRfF6GjZl1uLVL-zu35OvlQPqZhkjn1ziKc4u7YogZESsrNS402p4K0w8BpKteV5sKQ2UAb4vwkyZAMkbVk87zIVL6ZLBP_hxYjJvqDwPbju_ykq9bETYkgkBa7-PJ8tTcRR9JSDlpS7nK16UFAQ9lqPvd-yxy0zFKlMuolMSt2sH193_YwKwK6sk38MFNipqylCLbDKuk4fK6LaPLSaOVYZwcgq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=Ruvr_vOsNFfkF1BW3YnttU_DEbxv7eNtVZtL0Vb7sxobjcpGtLnrJgJX9ERFLgrfmGgysq9Sd_kRp02wlVRLYPfrJXNjPqfB2huO_r2UDLGX3bjjc7M1f-E2QLSmk1hiD3_FoLMhuf8bkeu2_SruEUoa6uFQUpR3xJcFDD8MDBGJTpcoO4n5d4cACGJEQspH_thk3KH96V2bg0jK2-KeaOggQKLEQh4xSFDW3o_xPGrNQ75oBk9WIDPSn9cdrg1uIw5akfjau8uKbUxlB5VpIzVNoPzYy2QSESh9fw1_2B1sSI7Pgi41Havu37I0zMhsAuRnODD6uZR_2Wk3Dp8yA19Hxvxr0fiR0zwvBL9L8QhtT8J5GpA-_4ZRIe67nVn_AyAEuSWsMyvuZDwMul8mzTuemXAhVwAZCEzSqpwF_5EDv2fqg5IMN1SV0wzuKElRYldl3UdG1mi66cWRfF6GjZl1uLVL-zu35OvlQPqZhkjn1ziKc4u7YogZESsrNS402p4K0w8BpKteV5sKQ2UAb4vwkyZAMkbVk87zIVL6ZLBP_hxYjJvqDwPbju_ykq9bETYkgkBa7-PJ8tTcRR9JSDlpS7nK16UFAQ9lqPvd-yxy0zFKlMuolMSt2sH193_YwKwK6sk38MFNipqylCLbDKuk4fK6LaPLSaOVYZwcgq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تاجرنیا، سرپرست مدیرعاملی استقلال: ترجیح می‌دهم به خاطر بازی حساس مقابل تراکتور فعلا درباره مسائل قهرمانی فصل‌گذشته سکوت کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/107462" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107461">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=mEFCwD9NvZLGO0XesPi_eowSiAoq1-tqalG2pKHKkgKAcKuypNu00J0MmOkYElCUK7FcB9AjWmdCCUl68lVFw9emk1DqnwePI2ci8Ron7Eib3IXEJHcGC9ttbHVoCBpCFK4Se0N2_3LZJI8x-SUYPxH7krin4RxGucYI5DebwuhtOcvwxXGOdbwehsBdMJlyaZb0rtIZEl4MN_CmkpeIZUJ_pmT8tz7KnThIcEfIPndlbkgsFYLVVri6JzHSwRzgdstqbcZdX6DIkOOMqyeDs4-1Zcus6i-GhdRaemzX_jL-N6mtJT7qKnij5XZcmZo8ks2ZttQVv3-cpw0pOgUd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=mEFCwD9NvZLGO0XesPi_eowSiAoq1-tqalG2pKHKkgKAcKuypNu00J0MmOkYElCUK7FcB9AjWmdCCUl68lVFw9emk1DqnwePI2ci8Ron7Eib3IXEJHcGC9ttbHVoCBpCFK4Se0N2_3LZJI8x-SUYPxH7krin4RxGucYI5DebwuhtOcvwxXGOdbwehsBdMJlyaZb0rtIZEl4MN_CmkpeIZUJ_pmT8tz7KnThIcEfIPndlbkgsFYLVVri6JzHSwRzgdstqbcZdX6DIkOOMqyeDs4-1Zcus6i-GhdRaemzX_jL-N6mtJT7qKnij5XZcmZo8ks2ZttQVv3-cpw0pOgUd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
علیرضا بیرانوند: اصلا دنبال معافیت پزشکی نیستم/ دوست ندارم به خاطر پرونده سربازی من، نظام‌وظیفه روی خیلی از بازیکنان دارای معافیت پزشکی لیگ زوم کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107461" target="_blank">📅 00:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107460">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
💵
⚪️
🔵
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه استقلال، قبل از اردوی ترکیه تیم ملی بزرگسالان؛ نامه شریعتمداری به تاج برای برگرداندن پول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/107460" target="_blank">📅 00:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107459">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=Qw7qcCqUpgATGIaa8Uo47Kw66SURPWbVoi3XDZrIolyIBW-42b7H0nlczTs0G6cRF3aR0LO_uCtDOl8lLtLD_ESKhs8mCXzIqZrgRRdJTu-Mly6o30eURVn0tGSJnQ1ymBI8C6KVZKbUqkWAD_8dwjvr9i8WLKReztSN55Z9YPGTB9Nh0KxsJDWhiInVOK08c1rblK2m_kM8ThAM9WZeWIuy87vI2Vv44v6x7C3BXhRDMx43OhHKfDDiTGhAzu7GLTRXJ7-mmwasDQfiSEyPeKPULQQcEiofbC26snkhulOA0IX7KqbyiGKLm5A2NtiaeisK3HsS8yXrnuOy-eaRoitx2L4xbkZIlLavygx_nVnBcO07ZiKGHsA4Rwm0WILKUomTtZ62Z2J8_61wSppGz_1ycJ7SOrnt7eDr5-zJYq3fsFjNPvXlFkaXPPWVfyTlnlOOK5WYGzLCYKm_-sgUdzKPCx_N7AUXKoj2LZ7CmO_gI56VoUq23ydGR4woo0pOY9UxHOOCgHKL72uJiH8PpIBA9ESFE4VBGnVWstSwZdX5IbQpdfUXEKiSwDg3llYoun7hHPpMN5x_JErONW5Abzmf7OjYyAHwk9j6lCWmYXqfcNEHHpp-e4G-lxYwBnZcCZvCXAZhV4vrZmIIEhX5xNmJTP5Qrt0Vd1nZa-1kpv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/373e4ffb08.mp4?token=Qw7qcCqUpgATGIaa8Uo47Kw66SURPWbVoi3XDZrIolyIBW-42b7H0nlczTs0G6cRF3aR0LO_uCtDOl8lLtLD_ESKhs8mCXzIqZrgRRdJTu-Mly6o30eURVn0tGSJnQ1ymBI8C6KVZKbUqkWAD_8dwjvr9i8WLKReztSN55Z9YPGTB9Nh0KxsJDWhiInVOK08c1rblK2m_kM8ThAM9WZeWIuy87vI2Vv44v6x7C3BXhRDMx43OhHKfDDiTGhAzu7GLTRXJ7-mmwasDQfiSEyPeKPULQQcEiofbC26snkhulOA0IX7KqbyiGKLm5A2NtiaeisK3HsS8yXrnuOy-eaRoitx2L4xbkZIlLavygx_nVnBcO07ZiKGHsA4Rwm0WILKUomTtZ62Z2J8_61wSppGz_1ycJ7SOrnt7eDr5-zJYq3fsFjNPvXlFkaXPPWVfyTlnlOOK5WYGzLCYKm_-sgUdzKPCx_N7AUXKoj2LZ7CmO_gI56VoUq23ydGR4woo0pOY9UxHOOCgHKL72uJiH8PpIBA9ESFE4VBGnVWstSwZdX5IbQpdfUXEKiSwDg3llYoun7hHPpMN5x_JErONW5Abzmf7OjYyAHwk9j6lCWmYXqfcNEHHpp-e4G-lxYwBnZcCZvCXAZhV4vrZmIIEhX5xNmJTP5Qrt0Vd1nZa-1kpv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
توضیحات میثاقی درباره شکایت اندونگ و کاریله از باشگاه استقلال
⚪️
محمدحسین میثاقی: در این هلدینگ خلیج فارس یک نفر نیست بپرسد که اندونگ کجاست؟ چه کسی قرارداد کاریله را امضا کرد؟ آقای تاجرنیا الان وقت آن است که مطب و آپارتمان خودت را بفروشی تا سهم خودت از این اشتباه را پرداخت کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107459" target="_blank">📅 00:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107458">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=irWFA2yx66bsWYsO1pmPq_cR_YxoafZLXGQhfsUAovAz0FlWl071PdTi3UYhtFRKorj0yAmBQyWhgItHwqcZadJCzo29rO-eDJMQf6rjQxcVd2TcRvw-DdaqTnBvQSUBQZ9JumZ_lWgzu8SJ4E8SXZ9prNgU4NjSpxI1GnjMmf8AUfzN3_mzqHkUWVwY4FbvIBT3cBR60CL7UvQw_uAkN18VAHvZXWc5i8z2zz4lpsz2IcMUbABekxHbqRPO2-yQuiaCkQwMUJVnV_vIUo9E2Av6WlT8VUpi18p6JO1ZytoBJMMarcVZUEL3rHa7RItKDbgngLhYhJ401FY6Sys0XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed66f5dc3.mp4?token=irWFA2yx66bsWYsO1pmPq_cR_YxoafZLXGQhfsUAovAz0FlWl071PdTi3UYhtFRKorj0yAmBQyWhgItHwqcZadJCzo29rO-eDJMQf6rjQxcVd2TcRvw-DdaqTnBvQSUBQZ9JumZ_lWgzu8SJ4E8SXZ9prNgU4NjSpxI1GnjMmf8AUfzN3_mzqHkUWVwY4FbvIBT3cBR60CL7UvQw_uAkN18VAHvZXWc5i8z2zz4lpsz2IcMUbABekxHbqRPO2-yQuiaCkQwMUJVnV_vIUo9E2Av6WlT8VUpi18p6JO1ZytoBJMMarcVZUEL3rHa7RItKDbgngLhYhJ401FY6Sys0XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
⚽️
خوشحالی فوق‌العاده زیدان پس از گل پیروزی بخش فرانسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107458" target="_blank">📅 00:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107457">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=Sg2FgvBk5gwJKZwPEMsNoPdJIDcnAus-xbuzboI6rxFn02J1f4GDQyQdP9BOzLf4Z8R56dfSFGizxkscjAw5dvzxnLwJLzZ7-z2-T6KMHLhjZ9URrhAsi5lweSZtpt8BI3gvI98iHK4PfI4RdaUy0RIDtyw0oX3H4rMC98ju6XmLUsnIWOz_HVPrJSv-8aonkEyeb4gF6aNBCHdJjpsLNiMM6IBUoSikkxZaoSnUYFY9N81SGSjT-s3MrRdU1l8DaCtE6XgkuLxPNgJMKuF7j7kQKGC2Wk0ElDi1GfivnOBlIvt4yrU4SS9IDNRrKdx85kSmjYh_Kf_lIcisvwPCbjqFQAzyN9cTNlqX3fyQFD2p0mWXYwM5i0gv_8fa4LZGp6snTmrQibN4YE40YfC-9bapgTRzzzsquQb4h-_SxcmLr2trwiLeoXaySibc5O9Dv28eOd7-LDEx1WK-yBlNj4rGTJ88bosdFkzKdluyNhERTBfmlX0BpatGYACkSdnghFGO8kY9sMQesTr74-00IDB50mhWavs9QCKnzwox-XgbEOFbBgLupzFedp42l5aHYrhoAFmBB0fPWw8oaIlyajNpuSE1N6GKL-3cHGeCyFcuLZLYVwm7NaI0pFNMPFHC00CKiRyy1dfYqkF8ZNQASPX9RFjNmc1pXwzZ-tlBPcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=Sg2FgvBk5gwJKZwPEMsNoPdJIDcnAus-xbuzboI6rxFn02J1f4GDQyQdP9BOzLf4Z8R56dfSFGizxkscjAw5dvzxnLwJLzZ7-z2-T6KMHLhjZ9URrhAsi5lweSZtpt8BI3gvI98iHK4PfI4RdaUy0RIDtyw0oX3H4rMC98ju6XmLUsnIWOz_HVPrJSv-8aonkEyeb4gF6aNBCHdJjpsLNiMM6IBUoSikkxZaoSnUYFY9N81SGSjT-s3MrRdU1l8DaCtE6XgkuLxPNgJMKuF7j7kQKGC2Wk0ElDi1GfivnOBlIvt4yrU4SS9IDNRrKdx85kSmjYh_Kf_lIcisvwPCbjqFQAzyN9cTNlqX3fyQFD2p0mWXYwM5i0gv_8fa4LZGp6snTmrQibN4YE40YfC-9bapgTRzzzsquQb4h-_SxcmLr2trwiLeoXaySibc5O9Dv28eOd7-LDEx1WK-yBlNj4rGTJ88bosdFkzKdluyNhERTBfmlX0BpatGYACkSdnghFGO8kY9sMQesTr74-00IDB50mhWavs9QCKnzwox-XgbEOFbBgLupzFedp42l5aHYrhoAFmBB0fPWw8oaIlyajNpuSE1N6GKL-3cHGeCyFcuLZLYVwm7NaI0pFNMPFHC00CKiRyy1dfYqkF8ZNQASPX9RFjNmc1pXwzZ-tlBPcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
افشاگری
باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
محمد
حسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت شکایت کرده است
در همین راستا این ایجنت قرار شده است مدارکی به پرسپولیس درباره فسخ آسانی بدهد و همچنین این بازیکن به پرسپولیس ملحق شود و مذاکرات حتی تا پیش قرارداد هم جلو رفته بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107457" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107456">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b959785a.mp4?token=gdqEr6eGmy80kXMEV7dCulUNaRSfNgAPSVGp3dVcdIZHc8e5GX_DmF2MbL_3lWJYSLknwgSC2ROq4p-hkK_DcwuuHHlPNdY4OauZv2l0pkvC8uSwv_CHa8UzXcgDyMQYrYGUtfSHoeqzsNXyPZbqO7RmoJzsya_BCS3HGhmJQpPIoNAmsAz4CQ0gS69yohRFl0xnmMjruikZ0nmsiRdx67ZXVhzwBJeY4dlnqaqyxXhgeuwsrvXeK3ywocYc0m74oHskyvnnJDLZBwMiBlkg2-tD97_ywcVxodvf5xy1g7Z_nMIdbmvoTAWpaN-rehBhoa5ooYdkOsFSeb4t5z9ZFz513v9QcsddX34ZM6NIizknjoaQOfSVtBc265FnPRmTQF14EhKU47_RubXyFSlDeAFjpqZV8QQBPhvylNRtf-cNr-jGvkBSMhcYT5KTTN6OjL1mjoQe0WalZR-HqBsZmg6UYWMz4WHgHOYSsuG4DbKVp8xgD7aGaVjHvAIuq4R8vRyG6c3L2EZjZSpx5qTu7uJqzKBgTw4sVopZeNpFncMGtuKwlQZXxSnY73pwK9X1ylydmyZx9MM2LQumhHq5Tb_6G8grL1UenhQcrrx8MvMIbi49HkIR9WNyjQedR1_A5sG_evjtxM83fAlPzkZLgNEq9oBvO7vTNF4y9bUMrxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b959785a.mp4?token=gdqEr6eGmy80kXMEV7dCulUNaRSfNgAPSVGp3dVcdIZHc8e5GX_DmF2MbL_3lWJYSLknwgSC2ROq4p-hkK_DcwuuHHlPNdY4OauZv2l0pkvC8uSwv_CHa8UzXcgDyMQYrYGUtfSHoeqzsNXyPZbqO7RmoJzsya_BCS3HGhmJQpPIoNAmsAz4CQ0gS69yohRFl0xnmMjruikZ0nmsiRdx67ZXVhzwBJeY4dlnqaqyxXhgeuwsrvXeK3ywocYc0m74oHskyvnnJDLZBwMiBlkg2-tD97_ywcVxodvf5xy1g7Z_nMIdbmvoTAWpaN-rehBhoa5ooYdkOsFSeb4t5z9ZFz513v9QcsddX34ZM6NIizknjoaQOfSVtBc265FnPRmTQF14EhKU47_RubXyFSlDeAFjpqZV8QQBPhvylNRtf-cNr-jGvkBSMhcYT5KTTN6OjL1mjoQe0WalZR-HqBsZmg6UYWMz4WHgHOYSsuG4DbKVp8xgD7aGaVjHvAIuq4R8vRyG6c3L2EZjZSpx5qTu7uJqzKBgTw4sVopZeNpFncMGtuKwlQZXxSnY73pwK9X1ylydmyZx9MM2LQumhHq5Tb_6G8grL1UenhQcrrx8MvMIbi49HkIR9WNyjQedR1_A5sG_evjtxM83fAlPzkZLgNEq9oBvO7vTNF4y9bUMrxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
گل‌تماشایی مایکل‌اولیسه مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107456" target="_blank">📅 00:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107455">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=voCJq5mh83FVfUMl5zgq48vCJorUxlVN_S0uhfsSs4nTgcHhGdne7C8Naspd0ggS9WMcHeteNfvPI1EFaEv7LoF3vjkfKFgOaw-NOeSU3t--smqhlxnjUDqUC8X3ZrLr06WTA8l5hz6SMQckld0dWpeD7PDY1SlOzosiybxDecPM319kl9qfg-zx2kg72ek2528shukO7RdsVdOPoQ0WM0OjnFE4ZYcLifx0_AcatmfpbNNWD7U-bE5m-ynA_Oz1LjRW8mlzF9r81EVsTMKGG4usG12f630a3bxaDqnKkOZKN4Ib1UazpQnNgMRSGJMbNsitajLZdpVNIlkYbcLCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba31d6094.mp4?token=voCJq5mh83FVfUMl5zgq48vCJorUxlVN_S0uhfsSs4nTgcHhGdne7C8Naspd0ggS9WMcHeteNfvPI1EFaEv7LoF3vjkfKFgOaw-NOeSU3t--smqhlxnjUDqUC8X3ZrLr06WTA8l5hz6SMQckld0dWpeD7PDY1SlOzosiybxDecPM319kl9qfg-zx2kg72ek2528shukO7RdsVdOPoQ0WM0OjnFE4ZYcLifx0_AcatmfpbNNWD7U-bE5m-ynA_Oz1LjRW8mlzF9r81EVsTMKGG4usG12f630a3bxaDqnKkOZKN4Ib1UazpQnNgMRSGJMbNsitajLZdpVNIlkYbcLCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
‼️
امیرمهدی ژوله جایگزین ابوطالب حسینی شد و برنامه فان فوتبال 360 رو اجرا خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107455" target="_blank">📅 00:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107454">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=S4yCl0gAHcBefV0-lDranY8EeMdvY3M4PFeY5iYe7kfti3w5CeVqDyHDv4OJpcf9pkOg_tycREUszUw7QUNVJGDm3UVaIwmPTFkHdoiyGE4mLyxgS1aYj8hDW8uD10zVVkGobXxtAt7a54PcBCn1j8E0WYvzbtdpRqFjU6M4Z5UU9RTDNg9LItJ40oAMoOjvfF28Zi1FEZmtF168WWe__FCIyzF7UUxWr748EL4nY9aQxCGmrBDUgZluLjSGi0wbPJWxSHbLKvgxFXyw3kJQ0xAxA1POCWvR8mpc6dI2GKaWAcwcQpfVYQs2UsEfJIROHgUWPvdNTLTNS5ygOEj__Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beb68432a.mp4?token=S4yCl0gAHcBefV0-lDranY8EeMdvY3M4PFeY5iYe7kfti3w5CeVqDyHDv4OJpcf9pkOg_tycREUszUw7QUNVJGDm3UVaIwmPTFkHdoiyGE4mLyxgS1aYj8hDW8uD10zVVkGobXxtAt7a54PcBCn1j8E0WYvzbtdpRqFjU6M4Z5UU9RTDNg9LItJ40oAMoOjvfF28Zi1FEZmtF168WWe__FCIyzF7UUxWr748EL4nY9aQxCGmrBDUgZluLjSGi0wbPJWxSHbLKvgxFXyw3kJQ0xAxA1POCWvR8mpc6dI2GKaWAcwcQpfVYQs2UsEfJIROHgUWPvdNTLTNS5ygOEj__Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
سوتی سمی عادل فردوسی‌پور و ریختن لیوان آب روی میز که با خنده‌های آسانی همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107454" target="_blank">📅 23:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107453">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=BefdyXKSNs5N6tfaj6gOteJ1GQCkB07uzuKbWHytuJlkxJEPjZOTcROY2zwPWAzuJPUvsysrr2XS2eaHreXKQyKgKvpclD53989E6e7aN6_aiBtDUXO_Sf2cf_GbWhpfCz4LW6iX4NlefZoERH3vP8_0qP9Qimz1NqOwtjRmyVnqhayDY8HkjYpKK8D0iF69peo3MLY4Q8UZABdzodxB7ny_QJMM9mYKj-RX6OWMpigUgZ3JjHpQ71JUzJC0i5NVXVpffAg66SDqvmsmiU9rlIPhhgnFt6kbotymgp-R1Lf03VUBlpytHZGZQ_wM1itnixe2lb2o5jhUodSIldZfnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5937fb4be6.mp4?token=BefdyXKSNs5N6tfaj6gOteJ1GQCkB07uzuKbWHytuJlkxJEPjZOTcROY2zwPWAzuJPUvsysrr2XS2eaHreXKQyKgKvpclD53989E6e7aN6_aiBtDUXO_Sf2cf_GbWhpfCz4LW6iX4NlefZoERH3vP8_0qP9Qimz1NqOwtjRmyVnqhayDY8HkjYpKK8D0iF69peo3MLY4Q8UZABdzodxB7ny_QJMM9mYKj-RX6OWMpigUgZ3JjHpQ71JUzJC0i5NVXVpffAg66SDqvmsmiU9rlIPhhgnFt6kbotymgp-R1Lf03VUBlpytHZGZQ_wM1itnixe2lb2o5jhUodSIldZfnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سردار آزمون: دیروز به زنوزی زنگ زدم و گفتم یه وقت نکند من را گردن نگیری/ انتخابم برای بازی در ایران تراکتور است مگر اینکه خودشان نخواهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107453" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107452">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=hOjEOLmU6QnJaeTDVxNs7QqL-Rx1pkKpBf1TnTR5uh0BB01O0oS0X-UxOQngeahNnK-hR1ro6zHI9e_N-Q3icdzu4RmGqAjAgKv9N_LLr7EsmwnhV4WQbPZENJNosDe2cGjoPVbpzl7DxeCvY7mQF0GawVnCjC3MI8JhDAJb6VWhQGgmuFSH6v5WrDDfwqYDrYNiTQa33tkbjoZN4SFmBwlF9H1-xmtBv2gM84hB2y5zxms6qU5yb5SvXcUqrvGFrD0SCE0TcnKjeJnsXTbf6aZ9NTDBx-epclFsiZGqR5I3dhyIBYn3Gcfjmu-Q5A5WtVSwecA9ZtoptXP75rWrnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07eddda0fb.mp4?token=hOjEOLmU6QnJaeTDVxNs7QqL-Rx1pkKpBf1TnTR5uh0BB01O0oS0X-UxOQngeahNnK-hR1ro6zHI9e_N-Q3icdzu4RmGqAjAgKv9N_LLr7EsmwnhV4WQbPZENJNosDe2cGjoPVbpzl7DxeCvY7mQF0GawVnCjC3MI8JhDAJb6VWhQGgmuFSH6v5WrDDfwqYDrYNiTQa33tkbjoZN4SFmBwlF9H1-xmtBv2gM84hB2y5zxms6qU5yb5SvXcUqrvGFrD0SCE0TcnKjeJnsXTbf6aZ9NTDBx-epclFsiZGqR5I3dhyIBYn3Gcfjmu-Q5A5WtVSwecA9ZtoptXP75rWrnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های سردار آزمون با بیرانوند درمورد رنگ مو و سربازی‌اش
🟠
همسر بیرانوند باز برایش حنا گذاشته ولی اصلا بهش نمیاد. یکی اکرم خانم (همسرش) و یکی اکرم عفیف او را در زندگی بدبخت کرده‌اند!
🟠
خدا کند علی در فجر مویش را نزند...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107452" target="_blank">📅 23:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107451">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
جنس متفاوت غافلگیرکردن یاسر آسانی!
👍
🇮🇷
خوش‌قلب و خیرخواه، مثل ستاره آلبانیایی استقلال؛ وقتی یاسر تصمیم گرفت برای اعضای نیازمند باشگاه، موتور و خانه تهیه کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107451" target="_blank">📅 22:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107450">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
از ختافه، ژاپن و عربستان پیشنهاد داشتم
🇮🇷
واکنش آسانی به پیشنهادهایی که بعد از فصل اولش در جمع استقلالی‌ها دریافت کرد؛ بهشان گفتم فقط وقتی پیشنهاد استقلال آمد به من زنگ بزنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107450" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107449">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
درباره رامین با ساپینتو حرف زدم؛ گفت برش می‌گردونم!
صحبت‌های یاسر آسانی درباره رابطه‌اش با رضاییان، اتفاقات جنجالی بعد از بازی با الوصل و پادرمیانی بین او و سرمربی سابق!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107449" target="_blank">📅 22:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107448">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎙
🇮🇷
توضیح آسانی درباره تکنیک‌های کری خواندن، از بازی مقابل پادیاب تا داربی برابر پرسپولیس!/ در استقلال، از تمام لحظات لذت می‌برم و خیلی خوشحالم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107448" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107447">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/133f025096.mp4?token=iUg6fKJLH3JWHhxRLbMxXdmcx_6-nZnuX3MH7ARVMD5PQEjcwBMtM6sSkceHsn1A1f6-BVznJWAKJBYk2W1oVrAS9sP2EJi77WmueJwVq3yFZPC8DnPSbVpaIta8v3Rw7KxPGxQnnanCrE5VLkEANjtJQXsc3Vjl1Qf1ntOK0HyFgcKM14RUpjobaZ-L9GH5Dy_nr3aSBkFm5Kh-D5s2fG20XLuSsOKsf3GtiTguCtveEp-rWxYB4pZHcg8CNFUNH14abV-XdjAHpG7W8iShiTdtvkNhbWIMBxoCoAZ3Z5T8Sc15dFP8R1YLcBpBr2n9wU9s2YJvXX_g7JAVh8yj4L8kik-xTXw4dYb-7O42yxSWJ7cY5RsiVXXfbwJRNiWQZyK7ia_o7sLKCEDBA0ai8016T_fjHLXsVwfiQ6IMLyJ11C291WepVLyAHXYM-Ho9YiHmYz_6wpb98cuFMjHQsxcYmrYs2nzzhyEjHZq5L5SxV3zegQ5Lj8HxlESsS1s34vAGvOCOUU9sIRGotr0M70ujuKf_i22XMDqhrzjiQIpWV-ma3SZKBJ_8H65QnfhzEBmCqSqyvd9akrgXxH5jiHkk94HMxcp_2TQa17ZjkHGM2m-M6PJ8CKhYbhS7NgxV-wWPCLJIQo4sar4uzt9sFtH2A3pV3wuGk5je57FyUQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/133f025096.mp4?token=iUg6fKJLH3JWHhxRLbMxXdmcx_6-nZnuX3MH7ARVMD5PQEjcwBMtM6sSkceHsn1A1f6-BVznJWAKJBYk2W1oVrAS9sP2EJi77WmueJwVq3yFZPC8DnPSbVpaIta8v3Rw7KxPGxQnnanCrE5VLkEANjtJQXsc3Vjl1Qf1ntOK0HyFgcKM14RUpjobaZ-L9GH5Dy_nr3aSBkFm5Kh-D5s2fG20XLuSsOKsf3GtiTguCtveEp-rWxYB4pZHcg8CNFUNH14abV-XdjAHpG7W8iShiTdtvkNhbWIMBxoCoAZ3Z5T8Sc15dFP8R1YLcBpBr2n9wU9s2YJvXX_g7JAVh8yj4L8kik-xTXw4dYb-7O42yxSWJ7cY5RsiVXXfbwJRNiWQZyK7ia_o7sLKCEDBA0ai8016T_fjHLXsVwfiQ6IMLyJ11C291WepVLyAHXYM-Ho9YiHmYz_6wpb98cuFMjHQsxcYmrYs2nzzhyEjHZq5L5SxV3zegQ5Lj8HxlESsS1s34vAGvOCOUU9sIRGotr0M70ujuKf_i22XMDqhrzjiQIpWV-ma3SZKBJ_8H65QnfhzEBmCqSqyvd9akrgXxH5jiHkk94HMxcp_2TQa17ZjkHGM2m-M6PJ8CKhYbhS7NgxV-wWPCLJIQo4sar4uzt9sFtH2A3pV3wuGk5je57FyUQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
گفت‌‌وگو با یاسر آسانی، درباره واکنش عجیبش به دعوت‌نشدن به تیم ملی آلبانی: حالا می‌توانم برای استقلال بهترین بازی‌هایم را انجام دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107447" target="_blank">📅 22:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107446">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=kT_tTrbEwcinMnJWABONMwgmka_-FHqOdPkRaQDjLYK65PfGwW4LGko0wo1gIRAmujcD3FZUQ6JTRsY_m1pWsGWUvEQ8FuseNqC3Qp9HHjhM5MGqUA6zvCqswt4Up2b_eVmLbzfqDOPpgB2exaKqYcGHfLe9cmnz-Ceou2bjAHSOc3QRjTv0K00shOFGg-9UkJkIuAda2nV4PYLtWyXB_FaWNDVI_VB59EvJmu0WhGGN1UqU2-6EUdlAakMm-Quh9WtL8rDGA_m59EdIYF353PRo_pfkSO7ZJEfNbmauDxiTSYFOWUh-mSB3KVmPpZg6UfWYlZDSdi__FBI3t6bj2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d5953f9f.mp4?token=kT_tTrbEwcinMnJWABONMwgmka_-FHqOdPkRaQDjLYK65PfGwW4LGko0wo1gIRAmujcD3FZUQ6JTRsY_m1pWsGWUvEQ8FuseNqC3Qp9HHjhM5MGqUA6zvCqswt4Up2b_eVmLbzfqDOPpgB2exaKqYcGHfLe9cmnz-Ceou2bjAHSOc3QRjTv0K00shOFGg-9UkJkIuAda2nV4PYLtWyXB_FaWNDVI_VB59EvJmu0WhGGN1UqU2-6EUdlAakMm-Quh9WtL8rDGA_m59EdIYF353PRo_pfkSO7ZJEfNbmauDxiTSYFOWUh-mSB3KVmPpZg6UfWYlZDSdi__FBI3t6bj2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
حسین‌
عبدی: رفتن به المپیک ربطی به سرمربی ندارد!
‼️
خیابانی: پس گواردیولا هم بیاید همین است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107446" target="_blank">📅 21:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107445">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uysxGBWmO2YOjkEN8dWtoDaKaCCu79b5mZtj_xZvNhq2A89B-K6gzLjNLr1rQK-zgDXpNSgEvuau4ScKcc_R2XHXuepOGQ_HQQ-wLIiz5V_WbuPfQUchYYnfMraEqZkWHR6VaFFoyFmdlWyMClGm8g_4A9tTcqw27AJ8rWRLCTy8cnci6192GRoWUNC5U_2RVrqR_opAR26sCh9-ZrUBh7oQz684-odlFun2wHNlPADNnuen31_tNuOzs7g4SYpOGedPCRZbLIT_sC6dq7HCGUyFCiTR_i6nNaw6ZUpnOgffNuYDScdOlc2vKrB_fuY0KgpaUK7itHqzyGrpvQpEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
یاسر‌آسانی تا دقایقی‌دیگر با حضور در برنامه عادل فردوسی‌پور با وی مصاحبه خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107445" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0794b34067.mp4?token=g8TNE8jpKB1olfpxKvhL0QR6-IMoxCHDTUk04rSWVwpuRDaIybCjBdlKOG9j9T5sbFDxyfhQqqwQcGP4PPX17KLPAWsWJLvPlIEwA0BKNL8YHr3ZH6mWh2pE3OXXdzLHCMGNB9gvm7saZCU6uBvFBoh6pn6-a_kUIG5He6Xnp4u8v-hjrxfROcd28yDxty6fBGhcE3lnqXXyXgWQc3TBMTgzZsXcEjKBjPD4qXnTfZqSoD3Ed70AzGJ8kn_c7jNBPqf-7bm30-Dq-ronHKEd-PanD54DB_Gcs-Cksm40Yk7mBATG5i7vgvf1x9sKKeM4XBexO5wLyXZolAnuh41ygg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0794b34067.mp4?token=g8TNE8jpKB1olfpxKvhL0QR6-IMoxCHDTUk04rSWVwpuRDaIybCjBdlKOG9j9T5sbFDxyfhQqqwQcGP4PPX17KLPAWsWJLvPlIEwA0BKNL8YHr3ZH6mWh2pE3OXXdzLHCMGNB9gvm7saZCU6uBvFBoh6pn6-a_kUIG5He6Xnp4u8v-hjrxfROcd28yDxty6fBGhcE3lnqXXyXgWQc3TBMTgzZsXcEjKBjPD4qXnTfZqSoD3Ed70AzGJ8kn_c7jNBPqf-7bm30-Dq-ronHKEd-PanD54DB_Gcs-Cksm40Yk7mBATG5i7vgvf1x9sKKeM4XBexO5wLyXZolAnuh41ygg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
مطابق گزارش خبرنگار شبکه الحدث در پاکستان، به گفته منابع، ایران با توقف فعالیت‌های غنی‌سازی موافقت کرده است، در ازای آن، تحریم‌های ایالات متحده علیه ایران کاهش خواهد یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107444" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107442">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9S3wMbJKYz5MC5h6dS7KJxXqASR9WGLfHC-JwG2Md0GuQudakfdYOon1iiszNdnTrIAWEKM4n2Lr9jScvZzE8nCTxD7aAelJsLqg2sFRilDXRMRtzjDBOAur6SN7nNYZ8uZA7LUwyp6gPfOSmd6buoo_NV6Jy-jZ7Buyxom35VEkUlBKJfds7qnmrDiTpMXsp3cmeghkAt2Z8dogrs5JfnqLdASc4fAQkqxUDgw-CntlU3-R76IVuIGZ0gNVk2gb7H0SUeua5hJl8sE0RlZkBJOO7rJbIaKupg7kHmxPLijUPkV87XScKJ_dGUWIoAobAVXaWsvbtbXO6ivFzqBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkjgRNs3vS2mFs27G-spAANYaZzTgMvfhbi2L8CxBKhcCHUM4JHnRhpAQ9gGjy2m-JRZjYqwTesZO40tGI_NydctK5t6AQ76b24wuJTDLfW-pJKRFMZQD3AKCHEqhuOrV2kQa2EzmjrJf1Ck6rIXxZBZOswGZGZeEoFDc3QIkZBoMOtgygl_I8MqjGxbulHqMzFBQfxiTsN41aSxET2kwTFZTJWnxhyncNbXs7w3q9fxAhk8TV2jo-qUd2xJP_4GSQiqKsdA0HtUAINkXpz4tgmWSBG1dbjaaHMJvUzcE5iJwiuKrwJ-0VPAGohvyQuR7jCsvrGFWU50tiz1SmmFOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
🇧🇪
ترکیب‌تیم‌های بلژیک x فرانسه
ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107442" target="_blank">📅 21:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107441">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا : از هواداران پرسپولیس گله دارم و ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107441" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107440">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=cZuPx_BopdTmjW0PzZ4Ms4EKxD4p89mx8iYcLOXnr36r91fOWRtv6bxCJNGXYqtBs48qSECtWeqOno8O_Nl1U5tlniCIfietHjb_ow7Ge2lwyDGnYzsGmi5_rn02s8kPhoEKCAz8jquyYaJ7nvSQv7loKt3wBhccWz4afGyRSDAt7to8q8H8cvuKbVOkCi24Gq69jdiJH76K-XVdYNO5LWOAAn-w4tVOzPN2J0e9ubS1jziIwq9xVUZMJAOBulBgTEdEtvXlIBMUSDhS5bZCFg3fuOQ2yPdWMCAgBqt59reFl0-Q3z9sWTGkGMfXEA9ckVCb59qvf2u8UBRkTsKCKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd0094f85.mp4?token=cZuPx_BopdTmjW0PzZ4Ms4EKxD4p89mx8iYcLOXnr36r91fOWRtv6bxCJNGXYqtBs48qSECtWeqOno8O_Nl1U5tlniCIfietHjb_ow7Ge2lwyDGnYzsGmi5_rn02s8kPhoEKCAz8jquyYaJ7nvSQv7loKt3wBhccWz4afGyRSDAt7to8q8H8cvuKbVOkCi24Gq69jdiJH76K-XVdYNO5LWOAAn-w4tVOzPN2J0e9ubS1jziIwq9xVUZMJAOBulBgTEdEtvXlIBMUSDhS5bZCFg3fuOQ2yPdWMCAgBqt59reFl0-Q3z9sWTGkGMfXEA9ckVCb59qvf2u8UBRkTsKCKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
کنایه مجری تلویزیون به زنوزی: باید از هواداران استقلال عذرخواهی کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107440" target="_blank">📅 20:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107439">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=JE_nWkIp487ORsN8UnoWg1tuwaooHaVhAbT-fEBUh8dXJy3GuAMCQDwSVYKg3a7a1XW3c0hbPg4IkyQWEgS4kHtTpK3LyZ6b-wGAWlyhss1rXVAV_VC_42mJebpGjNKkFjCOxnZzY-4payRoQBjrOzaW-A9s2y8MT8c2G8mY_iN2DZ8NL3bzy4iG9wIu9JSWhCgliDRzr6e6RzDx8wTAyA5ugfO2Er16AlmwkHYtZI76SecgOZlhF4xZ71kcTO_namHPodsCpueafxKkkzu7FKpFAlPVe3S07uOxGCxosuYMG4uzyhgD7yhroFbuJkA27GJzj93zgHT8boV31NUL4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd102e93c.mp4?token=JE_nWkIp487ORsN8UnoWg1tuwaooHaVhAbT-fEBUh8dXJy3GuAMCQDwSVYKg3a7a1XW3c0hbPg4IkyQWEgS4kHtTpK3LyZ6b-wGAWlyhss1rXVAV_VC_42mJebpGjNKkFjCOxnZzY-4payRoQBjrOzaW-A9s2y8MT8c2G8mY_iN2DZ8NL3bzy4iG9wIu9JSWhCgliDRzr6e6RzDx8wTAyA5ugfO2Er16AlmwkHYtZI76SecgOZlhF4xZ71kcTO_namHPodsCpueafxKkkzu7FKpFAlPVe3S07uOxGCxosuYMG4uzyhgD7yhroFbuJkA27GJzj93zgHT8boV31NUL4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📱
یامال دیوث اومده از عرق زیر بغل نیکو ویلیامز استوری گرفته و مسخرش میکنه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107439" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107438">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=LWJOqZ0vzKgx7Rna2mPXacRNVm5ZY3xohw2F0T9erk0T-m3XbXAgRaud6jdkwwrjj8Li0DVVGOfTD2rCBQ7bcgqqab0ugJplVZJDmanV9kWe9k-6Sz2ChB8Bvr7We95GUPqexggjZi0JLHHASjYTxJvgaqnHxY_GwXLe6bt4Sam7H3AtB8xloLBEdeO0mpx9ZX30TCHyfRLsvRyvlXMdzyBpbFr7PQQaF_9VPA6tgi5EZGsIHmlH9Krt1HuNmwbgZJXnzIUxNDqNJo9WzEhki7BVx5X9kUnL9n70FZj2I1wDOuRSbwt1LZwMUPQxt1oDEGhQ4duVHAciL3DPJbj_qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee7cdbb4e.mp4?token=LWJOqZ0vzKgx7Rna2mPXacRNVm5ZY3xohw2F0T9erk0T-m3XbXAgRaud6jdkwwrjj8Li0DVVGOfTD2rCBQ7bcgqqab0ugJplVZJDmanV9kWe9k-6Sz2ChB8Bvr7We95GUPqexggjZi0JLHHASjYTxJvgaqnHxY_GwXLe6bt4Sam7H3AtB8xloLBEdeO0mpx9ZX30TCHyfRLsvRyvlXMdzyBpbFr7PQQaF_9VPA6tgi5EZGsIHmlH9Krt1HuNmwbgZJXnzIUxNDqNJo9WzEhki7BVx5X9kUnL9n70FZj2I1wDOuRSbwt1LZwMUPQxt1oDEGhQ4duVHAciL3DPJbj_qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇮🇷
❌
فرزین دبیری عضو هیات رییسه فدراسیون فوتبال : علی تاجرنیا به اعضای هیات‌رییسه نامه زده که جام فصل گذشته به استقلال اهدا شود اما هنوز هیچ‌چیز قطعی نشده و هیچ کس هم به تاجرنیا قولی نداده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107438" target="_blank">📅 19:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107437">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3RfyQEIMreHFMmZLp9dSTAjJeP4OnXKqvWjvjjei2DqZWRgr27q3NxqM8m__qT3pI3bcpFIDjQyWuibns9OJJcDkz-goIE_9o_Mj3mVJAOj2IqvFTooRCfq_KJosjQTF8-0uBUF6u0E2zQ1zeThYKchS4DQ1gCeavVPEh9YtsEfL263ve5tV6uape0lHc0m0CDyRm63Ln0yX83MiH2a7Wc5mjI1PLFCtriJsJvuRlCAsCM4Njhr-EI53OGpN3bK5zeKskbV6IS_xU2774yVyDEupz74tEj5WlMF1YTImHofIwrXkiHgBSXnYJjYaxLsQEVe5QYhGcrEhd50y0cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
افشین‌قطبی، پیروز قربانی و رسول خطیبی سه گزینه نهایی فدراسیون فوتبال برای سرمربیگری تیم‌ملی امید هستند که بزودی یک نفر معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107437" target="_blank">📅 19:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107436">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=OZlsrlJj36L4pqWDsVt6YNLXkKGIGQEikFw1QeCPVx49lcm-H-3r7_mA7dk_c2So-_xqs6ajVZe2hwJ_llfUeE5lHFJ-81N74hnKcZ0LPFXKRxTYZdy5Gkd4Uqz5un2H4NIwO4fvqEBdzkj5X9xPWoQ4uJ-MLJ9zJd_ZVW2ZgZLDIOl-lXuJF2RcO1HejHxgYD_Lugc_Pz_n4YvU719KGoeH5LKsaiOcCo2RQN5oaNpn_IkKsPvomyKyjkYniT0hxUBbacqg8wF7tUG4VrYpecmfSVBMTLlE5U4Rh-kDpxzRm1w-GF2dPbbUblGbYA8WaRom1H5vtcHdhcKttKACy4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d622742.mp4?token=OZlsrlJj36L4pqWDsVt6YNLXkKGIGQEikFw1QeCPVx49lcm-H-3r7_mA7dk_c2So-_xqs6ajVZe2hwJ_llfUeE5lHFJ-81N74hnKcZ0LPFXKRxTYZdy5Gkd4Uqz5un2H4NIwO4fvqEBdzkj5X9xPWoQ4uJ-MLJ9zJd_ZVW2ZgZLDIOl-lXuJF2RcO1HejHxgYD_Lugc_Pz_n4YvU719KGoeH5LKsaiOcCo2RQN5oaNpn_IkKsPvomyKyjkYniT0hxUBbacqg8wF7tUG4VrYpecmfSVBMTLlE5U4Rh-kDpxzRm1w-GF2dPbbUblGbYA8WaRom1H5vtcHdhcKttKACy4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👍
ویدیو‌دیدنی از حرکات بانوی ژیمناستیک ایران در بازی‌های آسیایی که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107436" target="_blank">📅 19:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107435">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbDrOwZESMq39SV2O6_Ed3LMJi-N6OuvkAF-gmPfrTViXcnnVZ4bdhHHwuOSvtLLWENsfG4r96Vvn9VLAuR1J7Rgd4ciLP-UbkPwrQV0JkqxRHbJngvVOKK4u7xGkTV4RdBCMerPnBTQuOzkoZS2TAEYbRPgHtYXV4WXrcjS-Y2C8xOaQEsNrwMJAyuL8RBAGGHrA75L0QSjfN9aQDSii9n3zmmgLzyIRzqMxZo1TcyUEt-nh_6xEYbKWd74lakf3O2ckWNLgI19SjvUXpBmUaPnZVElvKf48NYqeYvOYwhhUbXb8RC-vvEtvZ2yxWV0EBvznDM45YYbbXIKPnBRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
دوایت باکس، گارد باتجربه آمریکایی، با تیم بسکتبال استقلال پیوست. این بازیکن آمریکای سابقه حضور در NBA تورنتو رپتورز، لس‌آنجلس لیکرز و دیترویت پیستونز را دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107435" target="_blank">📅 18:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107434">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=dFZYQC62xKm1cn04kZ7fn3l6eTMCnAWYOhou9XxSzJekmmtI3Z4jOsKpR_pLvD9_2inawRB3pBBOQgoZtj4FnH2nmbD0iKzLF5QDEKGQ7XoskNrQ2E-WyAtLFsUI_cdwHkCobncUQPxL9kipdYIOdFqBewDu9KClmdwkgN-B-lebg82IMdosLMJutJU_EPZTIx1iRJx3AUpj6OfgqfxmSWLeJaxyF6ggeOUWtBrqdKfh_6z7J60HGvSVCCtpdr70jnsCD9m4A5rwjrkiLaSBPs37XRJm9j45T-llmfp6CKAHoQZvCgUP-VafIJwVHb78lRixLqQwHYCFTfsbpT2VoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3874fb3e78.mp4?token=dFZYQC62xKm1cn04kZ7fn3l6eTMCnAWYOhou9XxSzJekmmtI3Z4jOsKpR_pLvD9_2inawRB3pBBOQgoZtj4FnH2nmbD0iKzLF5QDEKGQ7XoskNrQ2E-WyAtLFsUI_cdwHkCobncUQPxL9kipdYIOdFqBewDu9KClmdwkgN-B-lebg82IMdosLMJutJU_EPZTIx1iRJx3AUpj6OfgqfxmSWLeJaxyF6ggeOUWtBrqdKfh_6z7J60HGvSVCCtpdr70jnsCD9m4A5rwjrkiLaSBPs37XRJm9j45T-llmfp6CKAHoQZvCgUP-VafIJwVHb78lRixLqQwHYCFTfsbpT2VoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
تاجرنيا: خیلی ها من را سرزنش کردن که چرا موضع علیه سه جانبه نگرفتیم اما در نهایت دیدید که چه افتضاحی برایشان رقم خورد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107434" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107433">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFmuXMEjICNeXVrIoxPRjduWboE35hNMVKwxh90GX9PAKpBtMjirnNWAAfViqSqUhiUwn8cg5EsNS2o1h-DheuRGjxWLwwcGwV7flLeaSlFEEFonAeaARcW-eXXK1wqSQxxdZEL2hi23huWO1ujxidhO8dzDOsKbjVKipRjYXvRZYdodMWPZD_8kP1vPFppvURrzfU-IvcVzHwHhb915HqJ6ECRPRZTdBqT8JqzixfMKaxA8BrIXteCvZLssrJY4jUd4SyYEfEUJolg1umyg-SAoBeWGQRTT6W-vZMtW0I2lowWeNkgKOxLYNUyMYVQPoH_5TVdCE295UmcbugZHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد اسپانیا در ۵ بازی اخیر خودش
🔥
🇵🇹
برتری مقابل پرتغال —  رنکینگ 7 فیفا
🇧🇪
برتری مقابل بلژیک —  رنکینگ 8 فیفا
🇫🇷
برتری مقابل فرانسه — رنکینگ 3 فیفا
🇦🇷
برتری مقابل آرژانتین—  رنکینگ 2 فیفا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برتری مقابل انگلیس —  رنکینگ 4 فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107433" target="_blank">📅 17:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107432">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107432" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107432" target="_blank">📅 17:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107431">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMGX00fs3ZcZyVbHZfFx51_JCdy4ql8aN6WTpA8Qxm4ipf1e9awX__p7Hrqucw-oDW3f5LlILhx5XBKoOx1K34UjDKF8Flw0yo3cTKplTOZRfR95O0fJw6dTb2XEaNQQvcURurXvFwgQfuYOPVdUke-52sheMbWiBwQgRmbUe9yYHjDIkZl0TDLsOxDWw_Lbteq_m89oDzjqjf14i6taVLcFER0HiG3-XMNBmZI47SDtK2Lk3nsx548Vmj-4yOaC6fSiMMY8WW925qF3qT7ZvafPMf51xvmhw5ds8zL07Vj40H9aWxu6nKCmnCcf-NESu2iUr8HJuWNVxrxNtzun4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107431" target="_blank">📅 17:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107430">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=Na72MhczU7gQYM_aacVkwe1i0PFeC2ez8CK5vB1bioPhdeLtPR2jlQQ4iENPkTjll2gdONtsodgMjpJITW6204lVqY9G5FUQcJAY3CALaG0XqH_iDCeG-KjR0tVQmfy670wnvXzqg5Z5aZgYle-5SviGrAbR_VGIaL_MwqAj8DZxCGtSh7LHtdpCuVDBDr3XR_S2uoJ3ybi1y_SrZt8Pj6ygAvhl7ZGuq9mMe_1hHcqkxWeL6q2vKEgi-qr3yhcQzuDqEJK-zuYgxDRHgjMCvbglB9LsTgBrXz0FQctken0sNndNw9uFU4c2qirWXeYtU_q1H-5DMOMlchgPgdIJrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387378bb2a.mp4?token=Na72MhczU7gQYM_aacVkwe1i0PFeC2ez8CK5vB1bioPhdeLtPR2jlQQ4iENPkTjll2gdONtsodgMjpJITW6204lVqY9G5FUQcJAY3CALaG0XqH_iDCeG-KjR0tVQmfy670wnvXzqg5Z5aZgYle-5SviGrAbR_VGIaL_MwqAj8DZxCGtSh7LHtdpCuVDBDr3XR_S2uoJ3ybi1y_SrZt8Pj6ygAvhl7ZGuq9mMe_1hHcqkxWeL6q2vKEgi-qr3yhcQzuDqEJK-zuYgxDRHgjMCvbglB9LsTgBrXz0FQctken0sNndNw9uFU4c2qirWXeYtU_q1H-5DMOMlchgPgdIJrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیروزی پرتغال در خانه ی نروژ، در شب نیمکت نشینی رونالدو.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107430" target="_blank">📅 17:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107429">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKaLGtrmgPSKLQEY3RPCGCM3ImSEV2GI1Ks81JNUSEqHz2TLsqgfSCLLewWxwrCDM8ntVFa6gqSsZVlKvbCPLOHWl__JgOfBx9XFcqSkdm6bDqC8KvJnEB6MUFWajMtnzCZzvANr8oXWSEwmwfnbWVVgkIuzn6sN1LSDRmW9tTLKVmYIA3vGlEHK6XK3lAKo40nPO3DjDi1ocMq_-OC6I4H8HL-0h4-1lkzJuvY4qTEqm_W3e0jil_W2ZsJEWlVjZFnRj88TSqS0zS3YdxoJbUoN0BPzH-BQ1I4ifjmWl5FGIY3Gv61RO2XqC7dsT4kQ8gVjfpJbL9JzhkR-dfTWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عکس فوق العاده زیبا از برج میلاد و ماه که دیشب گرفته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107429" target="_blank">📅 17:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107428">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=JEjQMcfsqEUtDdSevh8K8tyqIisxjJeXbD6O-IqrgYnELPDjKetf3dIMAEovw082Em9n5agczxGeBhHjY7GZUlQSoVxkY7C64U3WuB5g3vVfsKtMo5mfaJH_yMSjr29MBMutTaElnf6CZ48v8FvNJJ3FOqZB5IgFa-9pAsH3071IbCA_qkBsDtLKx4QwtbtFl10XUnvrCLgCw3rE8Qan_wWm6gKtbzbXApFZKQNvhElZ_rpVhhzq2h1s_9wrBGX09zr5dwPtwN-QOSWbhMjDlJwAvfqqMVhrkkM9TRnVNw6lIyOJj2_Uqw04Ohstq81MjkVRJ9Eir5e-_UsggawjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302c2a5126.mp4?token=JEjQMcfsqEUtDdSevh8K8tyqIisxjJeXbD6O-IqrgYnELPDjKetf3dIMAEovw082Em9n5agczxGeBhHjY7GZUlQSoVxkY7C64U3WuB5g3vVfsKtMo5mfaJH_yMSjr29MBMutTaElnf6CZ48v8FvNJJ3FOqZB5IgFa-9pAsH3071IbCA_qkBsDtLKx4QwtbtFl10XUnvrCLgCw3rE8Qan_wWm6gKtbzbXApFZKQNvhElZ_rpVhhzq2h1s_9wrBGX09zr5dwPtwN-QOSWbhMjDlJwAvfqqMVhrkkM9TRnVNw6lIyOJj2_Uqw04Ohstq81MjkVRJ9Eir5e-_UsggawjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر بیرانوند روز اول خدمت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107428" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107427">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📊
🇳🇱
🇩🇪
آنالیز تاکتیک جذاب ژاوی در دیدار اخیر خود مقابل آلمان یورگن‌کلوپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107427" target="_blank">📅 16:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107426">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=qU7rVuS-K4OYaHyMiT4yjtlWfEMCmwEiwK8UsET9JLrxrHq3kUzxO5BOyDUBSvo1aI5bKsWjTe0bW0iAGmTXLa0x3h9y9ZwjpmCUdUkFydfWTUgXIurR-Na7-d4dmC6tr96Io9JAZxuQ5Lu3BEuDnRKv2-qhDe21LgR6Anrp3zNCmBjkGaFpBVOE1UDOcwjeppocjjzhHDL0aWvXeeXE12Pi4uj2Rzz_J0C5MerCsaAZ00mJ9qZt-nsgPZl-s9L9vBtKYSBXWfiDR6Ek4m_fc_FvPyTas7AWUk6bmnywsoXVPv_gz-KJJaDyQwSrPtDI9EoLjwgQpda1wpSrm6tOrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6242b00b.mp4?token=qU7rVuS-K4OYaHyMiT4yjtlWfEMCmwEiwK8UsET9JLrxrHq3kUzxO5BOyDUBSvo1aI5bKsWjTe0bW0iAGmTXLa0x3h9y9ZwjpmCUdUkFydfWTUgXIurR-Na7-d4dmC6tr96Io9JAZxuQ5Lu3BEuDnRKv2-qhDe21LgR6Anrp3zNCmBjkGaFpBVOE1UDOcwjeppocjjzhHDL0aWvXeeXE12Pi4uj2Rzz_J0C5MerCsaAZ00mJ9qZt-nsgPZl-s9L9vBtKYSBXWfiDR6Ek4m_fc_FvPyTas7AWUk6bmnywsoXVPv_gz-KJJaDyQwSrPtDI9EoLjwgQpda1wpSrm6tOrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مهدی‌مهدوی‌کیا: عدد فوتبال ایران پول خرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107426" target="_blank">📅 16:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107425">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=MloN4xR6vAiA5yo67h2V6iL0hSpwTs0hSLdawPdO-pc_xubpmxOP5yTSrlLBQAMlYoYlsRjEjEKVtTGJNq9TbN5fUL2ZqVf5G7i2_GJALgP5aCL0JiFpxZ4DsowYke7XWj44tBHVReq-WKfHPIO0Bm8SWm-Aud8ZJCImfJT44mMozneh4W81MmjjmoTxjAhwMECc2cUkV8VEuUrAtAA79XL_AyHVJqtC5o_vtLiG6evPMP0iX7uclOdnU3-V57JcfvKKFCmxwYQg2mBjVSu5J8T-Id_NihutQAeHeTB8kVnPIFk7c1WkUlHs4Y9kIwZBKxHdlSnfQfwuStyak8f_SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63162a7ef0.mp4?token=MloN4xR6vAiA5yo67h2V6iL0hSpwTs0hSLdawPdO-pc_xubpmxOP5yTSrlLBQAMlYoYlsRjEjEKVtTGJNq9TbN5fUL2ZqVf5G7i2_GJALgP5aCL0JiFpxZ4DsowYke7XWj44tBHVReq-WKfHPIO0Bm8SWm-Aud8ZJCImfJT44mMozneh4W81MmjjmoTxjAhwMECc2cUkV8VEuUrAtAA79XL_AyHVJqtC5o_vtLiG6evPMP0iX7uclOdnU3-V57JcfvKKFCmxwYQg2mBjVSu5J8T-Id_NihutQAeHeTB8kVnPIFk7c1WkUlHs4Y9kIwZBKxHdlSnfQfwuStyak8f_SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇪
نحوه برخورد بازیکنان ایرلند با اسرائیل در بازی دیشب که حسابی جنجالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107425" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107424">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=MBf3vMTJpcsCnR4tSigjZQPTkOMdLVb9_pDNUnE8bzFJ3PvrASGDQakLFCnL_Krg6ng-klL1Ei8rz226j1FTNmIvgB6exseU7PXINIHn3TMLh3JCjXRpD2p_WL-wATWDFpEYr_SSWTqe8z04RLpfDHyr19Rm9DDjxa715x7A3ST42NH-tXBS4fl86JpPcYHB7w-3W4L0vbM5JkprbbmpRvZIZaHUobr24p8ijnuwet7AHdZ3yM5N-hRi-9paxU9nEFneHPgwqmiV9fZZ-uXLQqXmgjWHjl_KmZnrbgIiQwSDNfCwONlcE97KjdM_f_xFVgb45ulV4NHcfhqq9z4neQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d3f57825.mp4?token=MBf3vMTJpcsCnR4tSigjZQPTkOMdLVb9_pDNUnE8bzFJ3PvrASGDQakLFCnL_Krg6ng-klL1Ei8rz226j1FTNmIvgB6exseU7PXINIHn3TMLh3JCjXRpD2p_WL-wATWDFpEYr_SSWTqe8z04RLpfDHyr19Rm9DDjxa715x7A3ST42NH-tXBS4fl86JpPcYHB7w-3W4L0vbM5JkprbbmpRvZIZaHUobr24p8ijnuwet7AHdZ3yM5N-hRi-9paxU9nEFneHPgwqmiV9fZZ-uXLQqXmgjWHjl_KmZnrbgIiQwSDNfCwONlcE97KjdM_f_xFVgb45ulV4NHcfhqq9z4neQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیتِ ناراحت کننده ی سرخیو آگوئرو.
🙁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107424" target="_blank">📅 15:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107423">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUEmRnnzkcd2ZWP_K9dUt_khUOUnYOEAsmcr-S1ehwuBkJYrvZSQdvpWvaK05-Abge-u-UJ8fQwz7mDgYUBHdH2ytGj23eHBags5L1DvG2NuGdEqs7HRlFrAGdcl1Wz2SCriBdMNR2NnUgru6dgFL0BlbNpHtkEfVAmGu0v7pVP6BJQKUvgnEQXEt-tSpFUuqHUkAx1-pIDBnYCD_yRtD28mn8RzTOzoM0BkOO7Qwz7BQO-S_e7Tj_FjqbbiGjmbgitywJf7c6h5BrbGHB0Rh2dcYH5F7OCSpN8iE0qqicX222XMrqIuvcr4epiuCjs0rboak55I5Op_ua5P7xieAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه آمار هالند و رونالدو تا ۲۶ سالگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107423" target="_blank">📅 15:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107422">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=dvfUUPUmgGyN6CarD6fkPjY7un9gHOL2WMTTQDTQTntuiHKXBIMfkaHvadDtFp7DreH1I-TYmn5N90_9VhOQiQpEVEfSVc7PMKioO0mHUkbAMArpMhi0haxIGu4vBkSGMn-QNpJjUmQpO_xqJb5AekT7eebKdHNE15NEwm6cT9ntrNxtuGDdZ9GGCZZuTv_i6RjZU2-03dCFWgEQMNaSEHYh4xcDDV1z6JeRgtO3i-XhVHnHQJ9kc-AVGgqlNzUwbrmXnoYd5_W25Y0WLaQNbzLBwDg8hLNJb4BVw-Hyv5-S9VJblYt1oluGlMbp3w5vNeg2oBYsiJJcZ7tdCC6VoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ff849b11.mp4?token=dvfUUPUmgGyN6CarD6fkPjY7un9gHOL2WMTTQDTQTntuiHKXBIMfkaHvadDtFp7DreH1I-TYmn5N90_9VhOQiQpEVEfSVc7PMKioO0mHUkbAMArpMhi0haxIGu4vBkSGMn-QNpJjUmQpO_xqJb5AekT7eebKdHNE15NEwm6cT9ntrNxtuGDdZ9GGCZZuTv_i6RjZU2-03dCFWgEQMNaSEHYh4xcDDV1z6JeRgtO3i-XhVHnHQJ9kc-AVGgqlNzUwbrmXnoYd5_W25Y0WLaQNbzLBwDg8hLNJb4BVw-Hyv5-S9VJblYt1oluGlMbp3w5vNeg2oBYsiJJcZ7tdCC6VoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت  بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107422" target="_blank">📅 14:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107421">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1947c53917.mp4?token=VlpZ29HUtsx4-zCkXe0HNMNpJzp4i5K5XVKBpH6O_ZR6eTCqgqB-A0x5LVPrKGcV7kW-Ypq2d2p5FxaEnN75Q-imou30qDRVadlVsrv_8Gqyqg9ZdjKJBEuPTwbmIbKETZ47samgzYIx_RlZw5J6gF1jJDKQNGbImO7BIOJ7movm8BKHrrc63pq-CgGNk3n7LE5JEvtdFbBC5EfgGVbWhWIJgIjznGV-1PXGZ1sjNPg3OnaNhr5LFaU7axPqsPlqhxm0Nm8pkRaq93IclhG_itT8BiNzsSziXm9Vgqcex84tytIlGd0O8X2Smhp9ayOxZl_WO3Ydrh9SN5PCTbNPvm9wR7FVXQnr5Gs8_vSH6qRcJicBYhje06AI-mV7C1XmVYPoLbttm464jVIZ6pab5HQZ4EZwZa2S0eUVp0VXW-OAdgeUXhi0uzsrgl7QTDtON-RCUiPGykzoUE6hNYHigjaMVMzozBew2HiGEUnDReDUtsIym3b65MvDdM-t00o3HnmmkEFcwNzONXKYOezIuBbxF0ccHP1dwPkw6_rDkSYjdcrH2Qmw7kXKEUbt6-gA3J9WKqPxTi61mL4M8eLFH13iEGal_wGFBAAbLpdZCl65AMK1YknIajnkt4689LAeZIqNFjnWVwsUdvX7Ifa9RbkV_r62B2GFGFKxt_0K0Yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1947c53917.mp4?token=VlpZ29HUtsx4-zCkXe0HNMNpJzp4i5K5XVKBpH6O_ZR6eTCqgqB-A0x5LVPrKGcV7kW-Ypq2d2p5FxaEnN75Q-imou30qDRVadlVsrv_8Gqyqg9ZdjKJBEuPTwbmIbKETZ47samgzYIx_RlZw5J6gF1jJDKQNGbImO7BIOJ7movm8BKHrrc63pq-CgGNk3n7LE5JEvtdFbBC5EfgGVbWhWIJgIjznGV-1PXGZ1sjNPg3OnaNhr5LFaU7axPqsPlqhxm0Nm8pkRaq93IclhG_itT8BiNzsSziXm9Vgqcex84tytIlGd0O8X2Smhp9ayOxZl_WO3Ydrh9SN5PCTbNPvm9wR7FVXQnr5Gs8_vSH6qRcJicBYhje06AI-mV7C1XmVYPoLbttm464jVIZ6pab5HQZ4EZwZa2S0eUVp0VXW-OAdgeUXhi0uzsrgl7QTDtON-RCUiPGykzoUE6hNYHigjaMVMzozBew2HiGEUnDReDUtsIym3b65MvDdM-t00o3HnmmkEFcwNzONXKYOezIuBbxF0ccHP1dwPkw6_rDkSYjdcrH2Qmw7kXKEUbt6-gA3J9WKqPxTi61mL4M8eLFH13iEGal_wGFBAAbLpdZCl65AMK1YknIajnkt4689LAeZIqNFjnWVwsUdvX7Ifa9RbkV_r62B2GFGFKxt_0K0Yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: پاى حرفم هستم ؛ پول كاريله رو ميدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107421" target="_blank">📅 14:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107420">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=LpepACsz-uz0Gj-LOsE7Bvo0Am1B6SdSvsPaW1fhhCMsVGP4pKNRiI81SGPO6INu1B0Wss_dGz-4GnQ92NH1OrrQ1sP62D4Y78dxuZrf9uVAVFLQA9tnSDseCeDXwk8NkIN99CR_bNZBy72S6sp4pNcVZUhYSq7oiTl2FkLtOXYGWBmDOMr4PyoZ369KKTF0D3uxHPtt90vSrB2daECD9hc3jEOxyhtUjkVzbYuIrm6oVfPRZQyqMuTPAedSO-HjMIHs2b25LtAMn2eRF-7qnVUCjyB2IBhgMxeUaGxFMxjBjIVZokHTOtjADUxYr3FEpVkT9r8quYQvTvkiVWqIrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdc8f323f.mp4?token=LpepACsz-uz0Gj-LOsE7Bvo0Am1B6SdSvsPaW1fhhCMsVGP4pKNRiI81SGPO6INu1B0Wss_dGz-4GnQ92NH1OrrQ1sP62D4Y78dxuZrf9uVAVFLQA9tnSDseCeDXwk8NkIN99CR_bNZBy72S6sp4pNcVZUhYSq7oiTl2FkLtOXYGWBmDOMr4PyoZ369KKTF0D3uxHPtt90vSrB2daECD9hc3jEOxyhtUjkVzbYuIrm6oVfPRZQyqMuTPAedSO-HjMIHs2b25LtAMn2eRF-7qnVUCjyB2IBhgMxeUaGxFMxjBjIVZokHTOtjADUxYr3FEpVkT9r8quYQvTvkiVWqIrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بیرانوند از خیابانی تو خدمت مرخصی میخواد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107420" target="_blank">📅 14:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107419">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=sI23MuEN9Igsx6elr3ZKb7CYKegk4Qd0_oCjwpZjWDZDT4VT4ADlaGdlQ_6lf3DSWtLF9ACftqVn3E_-IgoexLWLHMJ36jy5juNG4A2CHxcJ2_ISUHb78EFVBwEMjX7ifhYDGUEswCVkoRqWhiZoryb3jHE8Py_uQjZxvhl6LkSNvx5WCaEhaxoQmCpZO_U7GX_NeUE7BkTYGeWT-pRSUYRT4cT0BeTdBuceiPfUCJRU2rgj4lSI38lncS4kadeUMjjFD0Rpsh0J4OYWjESUGeU50XSmb3i43ebzmK7KzkdZUto1o94JHFomE8INQv79jortt2M391HdRXUoZJTWLqIkcOUVm-QfmsCRb_O8jon9nwTfQurdaChJB-DZHk7StHvexFiUklEouUoycON5YhQ6N-22cMK76xcBBULBA58sg5raydH5LqH8D4AwafM4O7YlEdxUWeA-SJO1ARJYlB9-wBhdJdtwtp8yPSZhRPT7d9BdNIe35ftZ_Hv-cLGrtDCaGcTdtwQG6PZgJVqpM4JQjTCazWn6CoNb8kQewnDqjM74clpETDlBhvkhnJTsJeG7WiPeyrG2pygD-DM09Rsy15UbYtK_XpfX656ayipnWbSS-VTZDbM_yfdLaU2VxYeY5p4T4we1s9HgeBBTnBvU9tC5W8QpkbrZc4tq_Ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39074d4c05.mp4?token=sI23MuEN9Igsx6elr3ZKb7CYKegk4Qd0_oCjwpZjWDZDT4VT4ADlaGdlQ_6lf3DSWtLF9ACftqVn3E_-IgoexLWLHMJ36jy5juNG4A2CHxcJ2_ISUHb78EFVBwEMjX7ifhYDGUEswCVkoRqWhiZoryb3jHE8Py_uQjZxvhl6LkSNvx5WCaEhaxoQmCpZO_U7GX_NeUE7BkTYGeWT-pRSUYRT4cT0BeTdBuceiPfUCJRU2rgj4lSI38lncS4kadeUMjjFD0Rpsh0J4OYWjESUGeU50XSmb3i43ebzmK7KzkdZUto1o94JHFomE8INQv79jortt2M391HdRXUoZJTWLqIkcOUVm-QfmsCRb_O8jon9nwTfQurdaChJB-DZHk7StHvexFiUklEouUoycON5YhQ6N-22cMK76xcBBULBA58sg5raydH5LqH8D4AwafM4O7YlEdxUWeA-SJO1ARJYlB9-wBhdJdtwtp8yPSZhRPT7d9BdNIe35ftZ_Hv-cLGrtDCaGcTdtwQG6PZgJVqpM4JQjTCazWn6CoNb8kQewnDqjM74clpETDlBhvkhnJTsJeG7WiPeyrG2pygD-DM09Rsy15UbYtK_XpfX656ayipnWbSS-VTZDbM_yfdLaU2VxYeY5p4T4we1s9HgeBBTnBvU9tC5W8QpkbrZc4tq_Ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔺
آنخل دی‌ماریا پس از به ثمر رساندن گلی شبیه گل مسی:⁣ قبل از بازی استرس داشتم و سعی می‌کردم با موبایلم خودم رو مشغول کنم و به بازی فکر نکنم که یهو گل ضربه آزاد مسب جلوی آمریکا روی صفحه گوشیم ظاهر شد. وقتی توی بازی صاحب کاشته شدیم، با خودم گفتم امتحان کنم؛ درسته من مسی نیستم، اما شاید جواب بده. و واقعاً جواب داد!⁣
🥇
روزاریو سنترال در فینال سوپرکوپا اینترنشنال آرژانتین با دبل دی‌ماریا ۳ بر ۱ استودیانتس رو برد و قهرمان شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107419" target="_blank">📅 14:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107418">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=SDATGrpuCmbjfOkcE_7G7edYhTjUPVg-kT1knobHkMreq6zZBVseaQKiz7iXVjQzG0GNjtjrrI9WmjDtmxJ74123pQkGOvO2uCMB1v9bjrXP7hwmLUS6hNhOZMDB-F_th0v4kJyN42BPJE_3G9CCLVwD2Je9UqPZWQc9tL-uPFwoW2m6EyTT93MwG5AIqzbkzOgLOGzVfQlYZDNyyAJHOuRUhQ_mouFM8YMRzvm7pVjlbc4SvIxQwWQLjjqijJL5Av6aCtnPUzdr5JBlSptk8_IFntUBo7n699xqMTuCDIXNviW8AgnJUsS-zKV1zkaU42VroJdYqGBbCDJ5Vs72gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4774088c.mp4?token=SDATGrpuCmbjfOkcE_7G7edYhTjUPVg-kT1knobHkMreq6zZBVseaQKiz7iXVjQzG0GNjtjrrI9WmjDtmxJ74123pQkGOvO2uCMB1v9bjrXP7hwmLUS6hNhOZMDB-F_th0v4kJyN42BPJE_3G9CCLVwD2Je9UqPZWQc9tL-uPFwoW2m6EyTT93MwG5AIqzbkzOgLOGzVfQlYZDNyyAJHOuRUhQ_mouFM8YMRzvm7pVjlbc4SvIxQwWQLjjqijJL5Av6aCtnPUzdr5JBlSptk8_IFntUBo7n699xqMTuCDIXNviW8AgnJUsS-zKV1zkaU42VroJdYqGBbCDJ5Vs72gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🐐
سوپرگل دیشب لیونل‌مسی از نماهای مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107418" target="_blank">📅 13:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107417">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=VCYUEWSdMC5H3s0y7mTVnoS4wQny3_5oCS7l0IqxKUMTNMLVn9uWYQKjKY1MqK2b42X-pmnm_QiTH80VsQaxvQB_Ef4cz3wJ7uQfih5rtBibkYW2YS_HG3lz_OHXeBkWYzr9my_hDTjQ8k7vX-LlmW_CGs2dXi8Qu_P8qQpeST7s7LriLMBRfp33osv9sA5mv6SDb-4crS1B3cnEV6vkecJBDrLwv3x-Y9qXEiGwelCxbnFqAfut-5Qnr4xvDzuiTGJprO6q4Q89nxY0njLK254QtsH-WJQrWDUwnBFEJnOmbxwsbubUVlgDahfeO5aYubGte8VPxI0MA0c6c2SM4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a5b80ac0.mp4?token=VCYUEWSdMC5H3s0y7mTVnoS4wQny3_5oCS7l0IqxKUMTNMLVn9uWYQKjKY1MqK2b42X-pmnm_QiTH80VsQaxvQB_Ef4cz3wJ7uQfih5rtBibkYW2YS_HG3lz_OHXeBkWYzr9my_hDTjQ8k7vX-LlmW_CGs2dXi8Qu_P8qQpeST7s7LriLMBRfp33osv9sA5mv6SDb-4crS1B3cnEV6vkecJBDrLwv3x-Y9qXEiGwelCxbnFqAfut-5Qnr4xvDzuiTGJprO6q4Q89nxY0njLK254QtsH-WJQrWDUwnBFEJnOmbxwsbubUVlgDahfeO5aYubGte8VPxI0MA0c6c2SM4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
ویدویی از درگیری بلینگهام و کوکوریا دو بازیکن رئال در بازی اخیر اسپانیا و انگلیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107417" target="_blank">📅 13:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107415">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f2619929.mp4?token=ntfZY7soYID_oIQD-vR7vgvPsBYjoDgchg3ZSBI3PjNJ5D18OhOZy-g7MGV144a9ky_wH-A_J3-jRem8NMuZ-s0WVQv4G3Op3tGZy7E13AaAOEQFOrwqWbHhaV-v6RCif78btg3mfvcTu3xORtQFiTEICrE2N1o2Kx0ogD99pk866mSOLNXOGix2a4jZOya52DCD5ryFuZ_lqf84tv91VDhKf24xJK7h1pZdfrNvf3CFPNBl2CGdB_ug1j8LmJi3SLgrUjZhb4WiwaY16QmPYQ7IvIefKA_PCzNkxdgFczBopn9Kw1GFGC88TkYCB3qimxC9V1qdGUPXWcgnMWcKkaCllYrQ6aMVPOeSpPG8dw9Kat-1qo5xAWmqQ-2xU72VPY3Pc9ULpXQp9r9FZtQsGeIKsA764z3m-F2CY6_8xzLj6nWQ0O-GvZ3u1J3Wn_GWl-ORdj4NthGuL64O5K0xXeQ6kXKX-TJcMATFDO4OG0kCfCeNZaULX3VTxK_QHM8b00_5Q1JxfK60JLLSgKTGgp8MVYReMll_BXPQuNsq3ubx3VLYYh-vGEfY_tuzL5qJ152BXiEiicpftpdUAS35PybB_eSxSt2avUfYoUYsmBpQk-TtKifvv8PKQYBCN7ssmvX3YqrNgDi00IVQwApyw--8-hFGvVA1PJZd_H3BaZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f2619929.mp4?token=ntfZY7soYID_oIQD-vR7vgvPsBYjoDgchg3ZSBI3PjNJ5D18OhOZy-g7MGV144a9ky_wH-A_J3-jRem8NMuZ-s0WVQv4G3Op3tGZy7E13AaAOEQFOrwqWbHhaV-v6RCif78btg3mfvcTu3xORtQFiTEICrE2N1o2Kx0ogD99pk866mSOLNXOGix2a4jZOya52DCD5ryFuZ_lqf84tv91VDhKf24xJK7h1pZdfrNvf3CFPNBl2CGdB_ug1j8LmJi3SLgrUjZhb4WiwaY16QmPYQ7IvIefKA_PCzNkxdgFczBopn9Kw1GFGC88TkYCB3qimxC9V1qdGUPXWcgnMWcKkaCllYrQ6aMVPOeSpPG8dw9Kat-1qo5xAWmqQ-2xU72VPY3Pc9ULpXQp9r9FZtQsGeIKsA764z3m-F2CY6_8xzLj6nWQ0O-GvZ3u1J3Wn_GWl-ORdj4NthGuL64O5K0xXeQ6kXKX-TJcMATFDO4OG0kCfCeNZaULX3VTxK_QHM8b00_5Q1JxfK60JLLSgKTGgp8MVYReMll_BXPQuNsq3ubx3VLYYh-vGEfY_tuzL5qJ152BXiEiicpftpdUAS35PybB_eSxSt2avUfYoUYsmBpQk-TtKifvv8PKQYBCN7ssmvX3YqrNgDi00IVQwApyw--8-hFGvVA1PJZd_H3BaZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
على تاجرنيا:صحبت های بازگشا مدیر پرسپولیس سخیف است و در شان من نیست جواب او را بدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107415" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107414">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107414" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRPef90AzVxWvB-vWmhWsP0ljKmypA0n1A6-tN17kdl5SJH1eJg17Ve1LxRDmjDqGNe024T6n9qJxbXQH2-7-EMw2Q9HRCvBV7YWAx54v8N9DgYzW3X7nrIr4nSwiUTdDLR6omm9Tpd8lx8i9TJvf-lxtGAEQXIgD03oyp85y3TWZtoKFHwIzoGMBvULO7sYDkwxT8JwtKId4G8y2ucFDTEIMMfmbEIZuYhIDunatk1cmTgqk3q0-pGN263S1J8Uyd_DNr4gHJYPrQUJHPSW_HdvYsdNRG9dmxgtYvcbdn7tXMbvzJEx-jU3wBS_sbcDJ295Z1_HuVIWsowmzF6dyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
فرانسه
🆚
بلژیک
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ تساوی و ۸ گل زده
بلژیک: ۴ برد، ۱ شکست و ۱۵ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107413" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107412">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVztY7hVfrKa6QC1YVdBxtS3jivW6Bq26ClYhR-33EeLGZLvc8d_uf7XyVqY6YC2vU1Wj8Sg8wzMMKZVWTOZb-nw_iz2oHaQByiIXLHvuOxG2cjilyexF8-i7kWA2pnAvN_gx3iozsMXhAsgJZaUeOZcZhJo-2QLqTs4GDQIhQn-ZBfDWXmx_kcwzQ6ldvB8baq3q9kOIQB-pQAQZQ5-D5yb6z1fjLqwDfxM3qH7jmWXTSRMxFgPNpLCkXs37qOu4XCXQ1qnB8sr7-_jHj16Zl3A65HXqOEgf47Xv8lHspQtuete1ZsDP_jGJajjqh2ZFvX541N2u4KSHeDhqsU24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🌍
آپدیت رنکینگ فیفا پس از بازی‌های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107412" target="_blank">📅 12:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107411">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=iz6DqUSNN_P52OfT15syJuckuTc_QH6Ke3dj_bHYrll2bIDkD8Cxa5kEqWg7lSznlgUzyn4CdXUrBFOpEvFlBV_Sq6Zw8KCO_49sJ9ywTxgpda5mHcEXW-ru6oN8IuZpqX0jm9HSYiYFpZktskb5k0exKdrFhdDYvDxoM10YdyQ7VRC8PiJttvlYCbxoa0m8AwD16mIVFzIxqNPT1RKfFiPtXCu5me5jeOa_YeaeR_ZuDQBb0i8ynZ3z8m2GFBgrQr23EgdSrYMGjOHZDxjmfahY2SbspQF0Ui98AI_RrPNERg-Spfjpm_dbMdN4oNJnt7YyjB_S4E61cGcpPaTcrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=iz6DqUSNN_P52OfT15syJuckuTc_QH6Ke3dj_bHYrll2bIDkD8Cxa5kEqWg7lSznlgUzyn4CdXUrBFOpEvFlBV_Sq6Zw8KCO_49sJ9ywTxgpda5mHcEXW-ru6oN8IuZpqX0jm9HSYiYFpZktskb5k0exKdrFhdDYvDxoM10YdyQ7VRC8PiJttvlYCbxoa0m8AwD16mIVFzIxqNPT1RKfFiPtXCu5me5jeOa_YeaeR_ZuDQBb0i8ynZ3z8m2GFBgrQr23EgdSrYMGjOHZDxjmfahY2SbspQF0Ui98AI_RrPNERg-Spfjpm_dbMdN4oNJnt7YyjB_S4E61cGcpPaTcrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پرویز برومند در جوانی ادای جلال طالبی رو در میاورد؛ عجب تقلید سمی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107411" target="_blank">📅 12:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107409">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCB11xZB9wky7k6ZMRxOffv0ecvM76Yr_QfXQDxPXq9Nd1zDtSjGQ5uM4claMtZz2hrf8uFAvBipLqR2MjPBf8l37gOfQ-LK-P1Vg2X2nw-PIDKwpS-1v6XO7Hr97F6ORnMoOu3pbMQG3XdWFuj5U-Xgu3nzclRic76Y7JyqxRUO7eM3sygCpJzhhvyy0OhcVN2KPQY5CJkkBXn2zRrSR2JYIQf8_UI7oowJeJ8xWp43w0V4m7zSD3eKCJUehkcPkNBo9JXa051T39SB7ViYyXvWs3wRHdq_F4DJKoqjhutwXhcb2DGcMiixcvUwvxd1cKoF_kXIrTWUdai7emQtFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت
بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107409" target="_blank">📅 11:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107408">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=GWt7LwJ8ZEnkDyPNA1zacSjvWTzVROYtkTUYqH2dg9y7JSxkC8ZSz0EPrQE49hXPKuM2D-aDmC2Ybf_pop5Sy2o-v-uIzodfvIz8JUTO-AZvIIHwxok3MvxdcB0JjzfbjV1qCesDyRy-wRULx_cqiX89tHTKeI5oc6apfo-ChaB2nMAC3VOeD2dmBhwL3WhiCiL_IGyhOSzZdz8zgiA9mFONhsBhHbmBvurXHLpzUwAGzai9PEpoITUQ4dStB9Et-sipYA1mya3o0y8CNzz9V3ZJw-7Pr96aUcRmOYaLtwn9xI3zYShASzOnBjD2qk32uAkAS7q2WKG_zFENh_Z1tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=GWt7LwJ8ZEnkDyPNA1zacSjvWTzVROYtkTUYqH2dg9y7JSxkC8ZSz0EPrQE49hXPKuM2D-aDmC2Ybf_pop5Sy2o-v-uIzodfvIz8JUTO-AZvIIHwxok3MvxdcB0JjzfbjV1qCesDyRy-wRULx_cqiX89tHTKeI5oc6apfo-ChaB2nMAC3VOeD2dmBhwL3WhiCiL_IGyhOSzZdz8zgiA9mFONhsBhHbmBvurXHLpzUwAGzai9PEpoITUQ4dStB9Et-sipYA1mya3o0y8CNzz9V3ZJw-7Pr96aUcRmOYaLtwn9xI3zYShASzOnBjD2qk32uAkAS7q2WKG_zFENh_Z1tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚔️
درگیری شدید بازیکنان در بازی دو تیم عراق و کویت در تورنمنت جعلی خلیج‌عربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107408" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107407">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2719da70df.mp4?token=lhLJm4DqN6ZfAES2rYvkLxKCZAWxJN5pFUmnAWA-PPmtx8xKvhDORtfHDZAUu2DI94lZyMgQUJSzkaVB85kRLYNNJh7ok1mzG09J9wYielFlzMfm_OvV0y-tQG93TWHb3skuuJzjExiy9qNKVOCbXeqJFtS5EGL4eTLXZTEBo7q4124SQAFsdAwpBfc_YdsoS-ObR4_hRTJQkL_kDpxVhZ3VHEAXRosX7emUlZ6UPgRxm-ps1hTpElApdqUe1n0QkFH1dGbFpKr8HhTjbQzQlh1WYIsIILItrUqOBfLBTpZsiJtG65LbH820VXrOjeJYeIlADiQTMpNa68I2xUkUv5232DTdIf6BJOQ8eEEhFp2dcqWunC9VBSkSMLfS3m15iiYdlZf4Nr450afzfefT8PukidDYe6isQRBkMzZX6GtPE5T0q3wxaiUiEZjV7pjR2sQHN97pIaad4oA0gH-XYY8HJIBeYLcXet6w5Ya95yzYc0BrZQgrf70IEGsSKVXUMK0RxaX6OmcyQwx1hobFjIOkSrm2dIM7OZGZMJjFe6T1hEcQA4f1hde_z1A_tjPLC-_LrxgARr6BSyYcFFyasVzGt3XyLhrRqK5UKN4Ap4qUi6Mz6oRrBJmbag9EPoXJ4LBTVeLgbHnc5_Ss2T6LvDP42sKqh2gVmpyYOlFX_Fo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2719da70df.mp4?token=lhLJm4DqN6ZfAES2rYvkLxKCZAWxJN5pFUmnAWA-PPmtx8xKvhDORtfHDZAUu2DI94lZyMgQUJSzkaVB85kRLYNNJh7ok1mzG09J9wYielFlzMfm_OvV0y-tQG93TWHb3skuuJzjExiy9qNKVOCbXeqJFtS5EGL4eTLXZTEBo7q4124SQAFsdAwpBfc_YdsoS-ObR4_hRTJQkL_kDpxVhZ3VHEAXRosX7emUlZ6UPgRxm-ps1hTpElApdqUe1n0QkFH1dGbFpKr8HhTjbQzQlh1WYIsIILItrUqOBfLBTpZsiJtG65LbH820VXrOjeJYeIlADiQTMpNa68I2xUkUv5232DTdIf6BJOQ8eEEhFp2dcqWunC9VBSkSMLfS3m15iiYdlZf4Nr450afzfefT8PukidDYe6isQRBkMzZX6GtPE5T0q3wxaiUiEZjV7pjR2sQHN97pIaad4oA0gH-XYY8HJIBeYLcXet6w5Ya95yzYc0BrZQgrf70IEGsSKVXUMK0RxaX6OmcyQwx1hobFjIOkSrm2dIM7OZGZMJjFe6T1hEcQA4f1hde_z1A_tjPLC-_LrxgARr6BSyYcFFyasVzGt3XyLhrRqK5UKN4Ap4qUi6Mz6oRrBJmbag9EPoXJ4LBTVeLgbHnc5_Ss2T6LvDP42sKqh2gVmpyYOlFX_Fo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
خاطره حنیف عمران‌زاده بازیکن سابق استقلال: هر بار گوسفندان را می‌شمردم، یکی اضافه می‌آمد؛ متوجه شدم خودم را هم دارم با آنها حساب می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107407" target="_blank">📅 11:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107406">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=i0AMaTWLkBEuOd9NX3s7gIne6Oe2S7Vux4YNVNefsX15gZRNpV8fME3l0ybzGpYuun6TibiujJhIzy9bLDcztKD5bWthUTmQ82bQZHTp34JkKwfGBuFi1xkDDuxDicrbEYPgMkPpCNNxepIaECOQcV1vlfcvKk7sYjDOLOwH-sEZRzQ07pMHp7HxEKE-ZwChwiNAXusygM407Uo-uuVZB3dVMpfkhC4egQsW8dUFZTBNH8tZKx_zrZNRkwP19I323NWX2ERCCqsd8Y2_YYVi6FQLLC_nMtbL11_GXevW3lSpslITvQlx8_yzqHZ205Fc2ImpuiVzDGX4K8eJ_9qxCIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=i0AMaTWLkBEuOd9NX3s7gIne6Oe2S7Vux4YNVNefsX15gZRNpV8fME3l0ybzGpYuun6TibiujJhIzy9bLDcztKD5bWthUTmQ82bQZHTp34JkKwfGBuFi1xkDDuxDicrbEYPgMkPpCNNxepIaECOQcV1vlfcvKk7sYjDOLOwH-sEZRzQ07pMHp7HxEKE-ZwChwiNAXusygM407Uo-uuVZB3dVMpfkhC4egQsW8dUFZTBNH8tZKx_zrZNRkwP19I323NWX2ERCCqsd8Y2_YYVi6FQLLC_nMtbL11_GXevW3lSpslITvQlx8_yzqHZ205Fc2ImpuiVzDGX4K8eJ_9qxCIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
با لابی‌های علیرضا دبیر،‌ معافیت بیرانوند همین‌ شکل یک‌ماه یک‌ماه جلو‌ خواهد رفت!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107406" target="_blank">📅 10:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107405">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=saIdb19OwbH2_hxP5nff8hvftdaAq9fqSDibBXV_U6etZrNpzPJJreXEvEbEbHddSwR8PEnonW2bxhfLxl90RiJywBR6_L4VMdjwcba_0-Qw4JpQGddKNDQTZCKMoHXFS0HETJeeh2nP68gX0IPYXe2-zLMaKmadyGk_QW5_TkYTxAxHy6EJzAApsOX4cn1UHT0lOp48Uu5fOl23sKFpBjiOlp-gk7TxPvBrTfGvmwZJSkaUvr4-z7jYSqrUT1dnXpTlsQPqU_nIg484Xn_hyuKqZqhtVyOrzZjouI1UqNQgVfRgiPVOwUFDhTzft_UEXtt9achUudAg_6mwzxwPapnNmLe5P43COp2eOXO5ufMvxPImV-7N-_sxcFKqri7UjN1dS1ap-eLEb13WaOsQX35COQKGTYdb_8I2ZEo_sRrNtMWLKU0Qn-sEA8KxpdAiOebVqGNpIPgJAiF8PKtIc5ReMtjq2YifrC9OUM2EPKTb3r40qyS3aMTeyJ0RGvcdttklcOquWZph8Qtqse58Evf1vfow0xZLJuCC0cvXW689787Qr0PvvHlPxfnrxW1kCnjfhjxt7OJmsUbD2-OWok1jA0ruMg9FUXewclx5ENuvi3V23SpsissbPYr3ktgBytgrBsjagyFuICJuL4qdOF5Ed0m8mo_MbWsrefs6H88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=saIdb19OwbH2_hxP5nff8hvftdaAq9fqSDibBXV_U6etZrNpzPJJreXEvEbEbHddSwR8PEnonW2bxhfLxl90RiJywBR6_L4VMdjwcba_0-Qw4JpQGddKNDQTZCKMoHXFS0HETJeeh2nP68gX0IPYXe2-zLMaKmadyGk_QW5_TkYTxAxHy6EJzAApsOX4cn1UHT0lOp48Uu5fOl23sKFpBjiOlp-gk7TxPvBrTfGvmwZJSkaUvr4-z7jYSqrUT1dnXpTlsQPqU_nIg484Xn_hyuKqZqhtVyOrzZjouI1UqNQgVfRgiPVOwUFDhTzft_UEXtt9achUudAg_6mwzxwPapnNmLe5P43COp2eOXO5ufMvxPImV-7N-_sxcFKqri7UjN1dS1ap-eLEb13WaOsQX35COQKGTYdb_8I2ZEo_sRrNtMWLKU0Qn-sEA8KxpdAiOebVqGNpIPgJAiF8PKtIc5ReMtjq2YifrC9OUM2EPKTb3r40qyS3aMTeyJ0RGvcdttklcOquWZph8Qtqse58Evf1vfow0xZLJuCC0cvXW689787Qr0PvvHlPxfnrxW1kCnjfhjxt7OJmsUbD2-OWok1jA0ruMg9FUXewclx5ENuvi3V23SpsissbPYr3ktgBytgrBsjagyFuICJuL4qdOF5Ed0m8mo_MbWsrefs6H88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
❌
آنالیز فنی از تیم‌قلعه‌نویی که مشخصا چیزی به اسم‌فوتبال بازی کردن بلد نیستن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107405" target="_blank">📅 10:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107404">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=WQ8909rtdQrG4A3eCNyjj7GHe8zn6qEumUP1Few7u1bAj0nkEpzptHXphhzsKbcCOUF9a6g_h5N4N8Z2A5ykCPE79KfOTgcMZPs1D86S7-bRxEd_AVmx6VtKS9iSXd780XgMchHRg2_BuvlO9ALcod7TFaBmbmzy3UH-NzL9xHHjYRqcS3tJxToXKIh5x57prIaxVeHLkGHM4uJ5bTwjMABqRU0R9LhOU0zTYB4xioI1JWGVFmHQH0PrsUZIWLJavjnFvk3slGfg7N98cwmwvJ6Dj-36Ld2KE-BHpJUSKv0h1xr1bVHL0jW5pDAX93-eKJzhYdAYny5BSQVBat4dgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=WQ8909rtdQrG4A3eCNyjj7GHe8zn6qEumUP1Few7u1bAj0nkEpzptHXphhzsKbcCOUF9a6g_h5N4N8Z2A5ykCPE79KfOTgcMZPs1D86S7-bRxEd_AVmx6VtKS9iSXd780XgMchHRg2_BuvlO9ALcod7TFaBmbmzy3UH-NzL9xHHjYRqcS3tJxToXKIh5x57prIaxVeHLkGHM4uJ5bTwjMABqRU0R9LhOU0zTYB4xioI1JWGVFmHQH0PrsUZIWLJavjnFvk3slGfg7N98cwmwvJ6Dj-36Ld2KE-BHpJUSKv0h1xr1bVHL0jW5pDAX93-eKJzhYdAYny5BSQVBat4dgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🎙
مرور صحبت‌های ژوزه مورینیو در ۲۰ آذر ۱۴۰۳ درباره اتهامات منچسترسیتی و پپ گواردیولا⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107404" target="_blank">📅 09:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107403">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me636gu3wmjohMk8ZNFRg4adwaTQgtDIfBll6ImdgVGAtDUOYP6j5HNFJkyV0i5_0JafaU-2ENSPaDyNlRGvDqH20C9H92WeqfePX4gn1GfTYRNhDMRxa2nh_kdP7e9Jf1YhYEsEsRPM8u5SdnEeszAgqhfJuA1QXwMsUIWjodfehP2teAtJdOjkWaGtqGrAEYUIjYmDAXzpFsFZSVz8WUJ5zAEBfcg92y4kbQY_PpP1u5tnCSgbYCW2oSpJoqiXSDWTVwJWVZ4Bsn69X2NqStOkrjwNHbyEol2__fDOrjbehoyyQLXt0MhG4enjPmf4WrnupWEBs8yJJ7S78-FASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
علی‌تاجرنیا خطاب به هواداران استقلال: جواب پرسپولیسی‌هارو ندید چون مکتب استقلال بر پایه احترام و اخلاق است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107403" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107402">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPg6sS6NM-k2e0Q7hTLDvjksfooBaGOkh2U_FORSE2d992emY6C5Cs5Ufr3m3O8ZNIC1oXfOOJ_AXC3iQJnAvxguED0P5EkrkbPzdQwA_BhbZ-fDEaQCoHCjKX9vGuA7AnunON84N50p8NqKJ2QOZcv3qHqyqPe8qtCaDOEZ6fxfgALfuaNqHJI141onJ95SBnoB0OJbMX5WAifeS9ZLex3XmFNjZ0r8RU-oXnzsp5Ihv_kr5usgAL6tmbhL1LyUqLG4a5RVxn6YxAWgyZfCVccgYEYiPq1yBDN60IUyxqKxNdO1eYtL302uMGvj40ysuwW1xIpB5xXaNoUk_FiUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
۱۳ سال ناکامی‌مطلق امیر قلعه‌نویی در ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107402" target="_blank">📅 09:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107401">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=DeyXsBfpOGz_bAXBRVI34ugyYdX76Nqi8xcUEYWzVTOaaBh_9_ND1adCO8MbQ9dOXP5vTNZkYpT-LvVFcY1_HPz2cwonz0GIQemrnhP57yZBRz8ntG4uKfjmldGwGez9RWdu-Tn7HWsWnR3SuUf791jdMCyYVD-YU9k0Wzt15o-YfisJHpDvkIunWATKg3rtLLG15va-80SydgSNiUv0lBnKHiviUIz_ZYaFR63ghBqiNWC8J4jBdgPDJa0RziuJRr09wwTNeHHqGiyovSU25RFK23kv2odnl3j8l_KfrhXpEv1a-aOuViI0XZtIzS3dZ4tmSeZ_fd5U-A37PEy_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=DeyXsBfpOGz_bAXBRVI34ugyYdX76Nqi8xcUEYWzVTOaaBh_9_ND1adCO8MbQ9dOXP5vTNZkYpT-LvVFcY1_HPz2cwonz0GIQemrnhP57yZBRz8ntG4uKfjmldGwGez9RWdu-Tn7HWsWnR3SuUf791jdMCyYVD-YU9k0Wzt15o-YfisJHpDvkIunWATKg3rtLLG15va-80SydgSNiUv0lBnKHiviUIz_ZYaFR63ghBqiNWC8J4jBdgPDJa0RziuJRr09wwTNeHHqGiyovSU25RFK23kv2odnl3j8l_KfrhXpEv1a-aOuViI0XZtIzS3dZ4tmSeZ_fd5U-A37PEy_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
مصاحبه جالب بازیکن خاتون‌بم پس از گلزنی و برتری مقابل استقلال در لیگ‌برتر بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107401" target="_blank">📅 09:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107400">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=MQGiPKQxPg1HpZLF5TPYgshoSx-YUPKFeIg2HWoCh8Q6Z_xWTC-AW-bEsJWUNLb_M_wzb1EiNw13JdLubJSp_a4NtfyGgQvOEV53W0-jKraLt76VMPeK15n1Qs2WkYvo5l3X6kn-mTxNNuUUNd5TnTdXvsskED_Z5U0SnK5HAtZbDcrWYBHFu9jhrKTZEkqtjD3uHOHIACYv9ZUiKrP4KuL8irhED3j3UZFaOZZtlPshE37TNL_fY_ISSrUBVGMQrfamWthsZpt2nsFxtVgzN0QGj9fr7KK8zBgXGwtkeL0kmNFddsUCKOmsfSCTNETv_KzYrfhbVN-Xn9aOrAcVJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=MQGiPKQxPg1HpZLF5TPYgshoSx-YUPKFeIg2HWoCh8Q6Z_xWTC-AW-bEsJWUNLb_M_wzb1EiNw13JdLubJSp_a4NtfyGgQvOEV53W0-jKraLt76VMPeK15n1Qs2WkYvo5l3X6kn-mTxNNuUUNd5TnTdXvsskED_Z5U0SnK5HAtZbDcrWYBHFu9jhrKTZEkqtjD3uHOHIACYv9ZUiKrP4KuL8irhED3j3UZFaOZZtlPshE37TNL_fY_ISSrUBVGMQrfamWthsZpt2nsFxtVgzN0QGj9fr7KK8zBgXGwtkeL0kmNFddsUCKOmsfSCTNETv_KzYrfhbVN-Xn9aOrAcVJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟣
سوپرگل لیونل‌مسی از روی ضربه‌کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107400" target="_blank">📅 07:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdamCD4n2NA-Wgj8IXbbXOrRg4j_GX0zh5ZbfHZZcx2aGSJPr_3Ukp0taeNRi9YRqFE1qp0_Pc4fhjhFoeTAMW2hT40chwt9tqOX-z-NW0R4X3wEvT9T2hhoML_wZQ1HIfXzIA8g04rkqvDtzKz0usq-hjYlEVNPNqQJOoTcPwHUg9JhD8QsYnG34NxbkkqMx5OUyS5d_-hPLlDgIptu-c6P7Iac63gdakDR_yPU0nXNFngSSNgV8vMAB1RQ4ER7h3juSC7DyyV8TJQqzum6Csy0UWObNfREmaDtG9i-nZ_LDzT8miCGxCnqmqCP48UKXQL5d5aCb00We32a5jrq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ژرژ ژسوس در مورد نيمکت‌نشینی رونالدو
او می‌توانست در این بازی بازی کند و مشکلی نداشت، اما احساس کردم به بازیکنی با ویژگی‌های متفاوت در این مسابقه نیاز داشتیم. این به این معنی نیست که او از برنامه‌های ما خارج شده است؛ ما قطعاً به او تکیه می‌کنیم و ممکن است در بازی‌های آینده نقش بزرگ‌تری ایفا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107397" target="_blank">📅 00:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWhvGC7rcbLwvI5MUmo2FHSZKYgc2AoR2rZM2nHOIxCiNfsDWTnAWdCrmJ_M0iBYCNOA4VQq2WdFQY0cegEu71qzVo_g3ZF-Cqe7tHPVlDxBwiXxeDujmBT8ieFNcRqH_dwFx0xR_dRlA_hw9CqGTTbTWi7To8Q5xbPBS3ISsJINr6Wktt_2UNINpvNUeob3ec4b3qCN-GuJKnro736rUW77MvsImKQDlF6sFNkwg8qJgrPlWq8hiMPcTdnWWd30Xd1r1bQWXprN09goLv-QJPECX3wG9koWC_RhsYy5B5oM1ZCf60PCCN4BkY8xA5LzH7QUx-rihGsLnCT5LyhUjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
❌
آلمان تحت رهبری یورگن کلوب:
❌
تساوی مقابل هلند در اولین بازی.
❌
شکست مقابل یونان در دومین بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107396" target="_blank">📅 00:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSW09r9h8Tz_NrDC9Xf5Q3kd2ELe5GCBzZuLBGmI9-_k5e721Y7b_gW7x4Rxmh-IW5YB583djESnLrR8gfjT-jWVIeV15vLa6hfRQ5iN3puq6cpcRTmHJdtptvgM9aPcaW_2wWPD86HM9OKL9G11FAKuaxECCM6le_v6tcHexbtCG1Q8iMOFCuWQ8C4EFNAwOTpv_flw9GT72BO_kqbCvsS1il8dsNLwxd9zCOrTb-aq1fC3n7u-SlLQ-7NmbkGGOoQt1QxvpnivvongRxiwRDFf3yX_3nIEKeKesNifaWV818XzLs8I8g3WSvjCBIeLKdG5h9Rq7_3tToRjvTJJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🔥
ارلینگ هالاند، [65] گل در [57] بازی با تیم ملی نروژ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107395" target="_blank">📅 00:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dE-PEGglzeyZp71NA0Df6n2eCfV7RqQIY3NGbquiHe23gwzDvln47tBsom8ViUNTF0QGaADQfvbFB7PWaq2q-CZvyPVpZzqs1fTiuyHIxRmLRv9nmnbvc6VHQfyFWbxEGBWk-ox6PtMFpcK8L2F3m9yDwPMxypbtgBtqelbPAgAeAFG9xphm-uzxx4HDgR8BalhTDfK681tpHBKtaTdHCAX1nWbhD2PfSIjAAV0GwFbKaAc7Gnntv1WfNNoJga5NfdiHa_OT91rrAvOyipXjatb_tK5KPDxP_K9wJquSoyELAgCGIrkxGjHn9LpkEfYWpZ8M63JBCQlWnN1tYzf2HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107394" target="_blank">📅 23:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uagAkDluqXT3J2M1Eo9I5WWwkxeiqfeW2iJnhFjhMo0o_oYReEwCvmXruL5-9fqvZBq-qclcherSsLSvOaHFdh_FLWFLcM8pnYQS05MzAdwciw9FGtb--nLxQsTD-COWNbWFduKMKjpS0bcYPqxUrYlQ1ciXsvwSiQwgh38yoVf_sIn6AVwQdfGjx12LP7jUR0tzggBdg-KfeJO4KNZ7CffnilwB84abBYr4JwehXrEHaf5UQ_XvjZWRPzvo34wFYS2l4kU64feMRsHSyvUU19qu2q34s-3F79yy6NC4y5GvHo_GR7h7XI0za6ypOgY8o4meAMChJuBNqVm62yGt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107393" target="_blank">📅 22:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gpOTsqIGdUlJJkFpgHhEMJFHGONDnbmPpTvHTUd4ahTJZGL1LRuFZYi-NOnSOMrlcFbGXmcJT_-zIiWy8InHZhmZ82eWIJe-2nPmW_WzUlSU0u5Y4c_Kx6fJX6xI63gStLR-zUwckvcXdF7n5weJJPJ51GZViyCSrFQGHybXA-kKdC8_lOfUc9P4d_9iCWP5OYs-0MOwoljkl_19tKw4LtFZJiFX2vJbjdlclVsOGtus2o-JPlJRZi3mUc2cEMN08Hgn-D4AYrGc_6nSQh6EhejIal3oawSyhyBolftegN-0nBfXzl5XRXzJRibS_f3cUHcNN6DjqeIb0qN9coEyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
امیرمهدی علوی سخنگوی فدراسیون فوتبال: من نمی‌دانم چه کسی به علی‌تاجرنیا گفته که جام قهرمانی را به استقلال می‌دهیم. هیچ‌ بحثی در این زمینه شکل نگرفته و صحبت‌های مدیر استقلال برای نمایش است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107392" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1tW7RqEnyASLqeScSBRjB192GJJVM7SQ933F4ZE6-eR74RNLmdA4srP2xFvv9MjMx4-qhdFKWiKPH-6QnNYrBNmbFDwh-Zr7BwN3EpoS1U7B25fOTlZlj0e2ixmAdHyW5iEIGIS4WJyEEvtJ7vNi5sTfJg4E84ttO0UJcfj8XHKmcTFRJHgT6Ec-qmyS5a0c20-mNMEN-yd8mdWsW3vfbaDoBcb5qTi7YreSLep6QHy1AhpFLMO2yIXEzIlZMUGeyFQ5gsJ1QGLHcDbGmL4-ooUw5jJyk3-Bz-5UhIgErTlBpyLGbBx7f0NSVc7VsLfqefd2KKY0x0QqWuWylRGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107391" target="_blank">📅 21:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klCtDzSIH-gn9QtOqQr_13Lzf2AbYj6e6_SjbnBMOSzyOjZ1ktlJgLyao4wLlNAtZkZjlTyxEn_j0cavbzssCAjnFH93wA8tQvnKQobuECIEvksk5a0LqZH_SKtZ5z40ItKFsL1KP46hR_1QZ7RaqxKT9qH2z5VrHBO4rPAXjZ8qcGGgGbft3YdIuVIo3WkIKhm6XHxTCXcANzLekkGj79PtBNqK2jRrl882DKO8kj7NfRM08tGO3S_oyu_9qobLMYXSaqtX1pLTKXxUMxUSJ5fU9xpxkEa0kHVTGaKKQN6PuOe-UWMr8ALu3Rg4CcBFnHS6rUu93rk6dOZ-wEOPsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
رونالدو روی نیمکت پرتغال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107390" target="_blank">📅 21:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=qgenjqb7w10jSECRPbUISkgxmgp0_0EkAGUd-u0bzvA-NxjVgJFs-nQcUruygCCPv5vURRriWIgY-VbfgCXe0WQLUFjp-N-9ZLn7P5l4vWCwkhr8jcthi01vBHdLRjjBbJ41YO8POz4YS6jskXaQBzdP7xSLlK8pEHbqBl2SOhtw8OzhUXLwLVRjWpCKru1UI1a9BFkKnJ1FiHUvRAoM3B1WJcROXCP6SaNTQuAAKM69W39akj7Pqo-9h-DqW_xR-AGGeGRDWYUu7ElOH8ukJaXIETWogCn4K1U4R0detZlFHj6mUBTSKgAqxk1hKhBd8tT0hM0jDcP4_YrVNnzgFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=qgenjqb7w10jSECRPbUISkgxmgp0_0EkAGUd-u0bzvA-NxjVgJFs-nQcUruygCCPv5vURRriWIgY-VbfgCXe0WQLUFjp-N-9ZLn7P5l4vWCwkhr8jcthi01vBHdLRjjBbJ41YO8POz4YS6jskXaQBzdP7xSLlK8pEHbqBl2SOhtw8OzhUXLwLVRjWpCKru1UI1a9BFkKnJ1FiHUvRAoM3B1WJcROXCP6SaNTQuAAKM69W39akj7Pqo-9h-DqW_xR-AGGeGRDWYUu7ElOH8ukJaXIETWogCn4K1U4R0detZlFHj6mUBTSKgAqxk1hKhBd8tT0hM0jDcP4_YrVNnzgFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقاد شدید مجتبی جباری از داریوش شجاعیان!
مجتبی جباری، سرمربی جزیره قشم، بعد از تساوی برابر فرد البرز، به انتقاد از رفتار داریوش شجاعیان که در دقایق پایانی بازی در نقش یک مربی به جباری مشاوره می داد، پرداخت و مدعی شد هیچ بازیکنی حق ندارد در کار فنی دخالت کند. جباری همچنین خاطرنشان کرد حتما با شجاعیان برخورد می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107389" target="_blank">📅 21:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twbFkGK3c01QCIWrkhLZlNapsa5OT9i25Sik5uLayE_oAAWpBWIxDcMxzzjDeKr6KP_6BT0RS8z9H_WuAoCu3L1WU1hyyIG5enRdvIKShxHGV_HVz0IOhbLCZVfd6WodqNeAPGZ3xwhEtZATlaoysamzx77rea5dPiNV2o9RzYTwXs9_7kLZZdGfhFc9LIJ0TYqvtClCMG8hW9avcyqsTG8Xb3YffYkeOA9EPcD1_8IfzD7TTqcHDBD9QcxKHQ4iZjxx8bKX1hcK4wuSGRONbMaFyOH4XDid7AW2zRucbUY-k5Eof6oYk_KWwEPjiLxr6DM9F6itSgl9hPMw0aunmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
استوری تتلو گونه‌ای رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107388" target="_blank">📅 21:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX-Da8QLh0XJ9jSSF7sZ6v50M3GaRw-GG5P-qnnM5GNNQUgggniLFV-MxtwW4wkOx3SuSxr8wb08-9ZkzTAuz_R8p663XJzNrZMPvH1cqy9XcrRtH0wDcr9gkUef0G0E226oYX4xnpbWxFEoQiNzRTC4ZOjbNSHmIdGU6mdcCqhycYkUq4d9cYKP7Sf-W1PI8pMtD2EB8x3YUx2c2a8QQ8DtyiocOj2uBfTxUC9q4zRKYo7zbpcun9AdkfyYbBkWIy6buCHTPGEVTBdTansAEOKNKcfEFCgZcYWFdJXCR9RcGelCxrdlXFmqgCoLHpTnPsy4lnzwHVU3QEm3JxAeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه چند سالیه رویه جدیدی در فوتبال حاکم شده و بعضی تیما دوست دارن بدون مسابقه جام ببرن و حتی فاتح مهم‌ترین عنوان ورزشی در طول یک سال بشن. جالب اینکه درباره عدالت هم صحبت می‌کنن اما در روز روشن چنین ادعایی رو به زبان میارن.
🔻
یک باشگاه میاد به زور و با زیرفشار گذاشتن فدراسیون و لابی کردن، باعث و بانی برگزاری یک تورنمنت سه جانبه میشه و دیگری میگه جام رو به ما بدید! معلومه چکار دارید می‌کنید؟ البته من دلیل این تلاش رو می‌دونم. هزینه‌های بسیار گزاف و چند همتی و خارج از قاعده‌ای انجام شده که برای توجیه آن‌ها باید هرطور شده یک جام بیاوریم حتی اگه تیم‌های شایسته‌تری وجود داشته باشن!
🔻
به هرحال در خیابان منیریه در شکل های مختلف و در سایزهای مختلف زیاده. اگه دوست دارن می‌تونن حتی با هزینه من برای خودشون جام بگیرن و روی پوسترشون بزنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107387" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=mqyrkmo0I3OBH3iNqNbL8Ldsl3cnMP2KHPySytr9wwMiTHHK-6gve_CXjqKo806mkk7RrggGckl--YDYLr8tZSueCA8trGDJhJeKxeJYqHvPgVWGZcg-_-GcFn7iPVnNudrbNh7EqCNvxogql39Qy6gq3g7QbEDvNVdl_4XpLimb8-xYTj7-jqHekncyC1SEJPpoWHBVKXsAgErfSVUB8DrofFQQC9VIQFSgQxviMKC9I_lJ3L27Tl6m-fz0W1PXicUPEBHpam9ZVyGp5u6a9vTrmgcBu2wyOVLtSPh4J0g-T-vDzERlAckoXog2OsC2laBrF5T79KQMcwIzPJgENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=mqyrkmo0I3OBH3iNqNbL8Ldsl3cnMP2KHPySytr9wwMiTHHK-6gve_CXjqKo806mkk7RrggGckl--YDYLr8tZSueCA8trGDJhJeKxeJYqHvPgVWGZcg-_-GcFn7iPVnNudrbNh7EqCNvxogql39Qy6gq3g7QbEDvNVdl_4XpLimb8-xYTj7-jqHekncyC1SEJPpoWHBVKXsAgErfSVUB8DrofFQQC9VIQFSgQxviMKC9I_lJ3L27Tl6m-fz0W1PXicUPEBHpam9ZVyGp5u6a9vTrmgcBu2wyOVLtSPh4J0g-T-vDzERlAckoXog2OsC2laBrF5T79KQMcwIzPJgENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباه وحشتناک ووزینیا بهترین گلر جام جهانی مقابل مالی در لیگ ملت ‌های آفریقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107386" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=RHwFu-uQC9qhH0k4lnH5ovrAF8NzsSMJpvg6hwoVb_C1MpN_wOjg61CG3CiXOovm0ImfZvpOjw20VOI9xVZxfAXE7GWSIEydV9cd56tz2-7AFZLuX2jPFHrBLUDnvG6YEoarjWJNx-nhTwagsuTRfkZdFCPouSEdtqPGzhqeY4y3xRtN4fJEdKLugVn5jZjn_WeMQeB-Ph1Zgfo7BNQCZ_v3vNW5BcXhPFjY-4dpmrJpwOn7Hzp2WTDFUb81-seX7IgqqCXYDqP6H1xixwV7ZpgdzR4SzX-bhdYg98p94SwTHvq2nEvkJTHvTO8fjIz4rBCW-lms4EZSa9GDs3FS0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=RHwFu-uQC9qhH0k4lnH5ovrAF8NzsSMJpvg6hwoVb_C1MpN_wOjg61CG3CiXOovm0ImfZvpOjw20VOI9xVZxfAXE7GWSIEydV9cd56tz2-7AFZLuX2jPFHrBLUDnvG6YEoarjWJNx-nhTwagsuTRfkZdFCPouSEdtqPGzhqeY4y3xRtN4fJEdKLugVn5jZjn_WeMQeB-Ph1Zgfo7BNQCZ_v3vNW5BcXhPFjY-4dpmrJpwOn7Hzp2WTDFUb81-seX7IgqqCXYDqP6H1xixwV7ZpgdzR4SzX-bhdYg98p94SwTHvq2nEvkJTHvTO8fjIz4rBCW-lms4EZSa9GDs3FS0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی برنامه نداره ...
وقتی حمید استیلی میخواست برای فرهاد مجیدی
در تیم ملی امید دستیار ایرانی بگیره ولی مورد قبولش
قرار نگرفت ، در ادامه به مجیدی میگن چطور مربی ایرانی
برنامه نداره ؟ امیر قلعه نویی رو براش مثال زدن اونم گفت
که اصلا قلعه نویی برنامه ای نداره
حالا برگردیم به مصاحبه کاناوارو سرمربی ازبکستان !
که گفت تاکتیک ایران فقط ضربه آزاد و کرنر هست
چرا قلعه نویی باید ماندگار باشه ؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107385" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=G67GNCy8SujHWoM5EdtkyLkxqJRQIGV6hAFU7SXpsIBgg9YMe6uYGDKXEmHI4Emvr7-vCNRe6L9heGN4VhRWtyivAhG66w2UaFf88d6_ljw6cNH_z7tgz3bkb2sN2V6rLEP-hdn58XGyQVEekKnob-KBIam3qTWup77i6aZHSUrOhALyx6tiHaLb98DVH7XpMqXCGw1LajnlzJ3ZovZvr6LIUZ1mpFfbsVibg0IqmAUyTez7pFeIj8jjCdCp4AsPHggijEeZcbvIVFd23bdiK_RKBUJtgruJqYP7FzHfeyc-g3Ag2Bqyusx4Gd13O7GFLXfTzxh45VcTlciVQazNyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=G67GNCy8SujHWoM5EdtkyLkxqJRQIGV6hAFU7SXpsIBgg9YMe6uYGDKXEmHI4Emvr7-vCNRe6L9heGN4VhRWtyivAhG66w2UaFf88d6_ljw6cNH_z7tgz3bkb2sN2V6rLEP-hdn58XGyQVEekKnob-KBIam3qTWup77i6aZHSUrOhALyx6tiHaLb98DVH7XpMqXCGw1LajnlzJ3ZovZvr6LIUZ1mpFfbsVibg0IqmAUyTez7pFeIj8jjCdCp4AsPHggijEeZcbvIVFd23bdiK_RKBUJtgruJqYP7FzHfeyc-g3Ag2Bqyusx4Gd13O7GFLXfTzxh45VcTlciVQazNyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
وزیر خزانه‌داری آمریکا: اقتصاد ایران تا دو هفته دیگه نابود می‌شه
چون اونا فقط ۱۵ میلیون بشکه نفت روی آب دارن و بعد از انتقالشون به چین، هیچ‌چیزی براشون نمی‌مونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107384" target="_blank">📅 19:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=FOdwxxZJF5XW6P8wn2c2f4GxLg9H27wR_pkXqO7lZFCCVRARr-iqHoreuTg9OOsyLgBFbete5xyIYCsQiM-DiU8L8fgrSfNOXZiBRR0Hz3kSOMcvs6zFXpP9EzydnN4MzmsEOYrjgOIap8tvNtYROkt1lpzrB-UYLrC183vHmT2eZiTxJNfK1U9N66q4faEkelVRUwVQLnhjnolBWv-hTyfVe9YwgwiNLPp2RFPhyj8-bPFpJgSZrm5ml4tbfi88BDcH_IPjqTtHXUboPZ8OQWVviPowPJm2_4Hx0DP5ndTLbMflQT_kbpGXjjjlZ-Axy61LdHcopgwna2NDJ0P-q4cDTr4keWoR_pXm73a0HR1XWK8eXE8NaE79LHKuBWoXSnO9hYFg6_zGaEr0wN3kWqG3mZ7H06DFdC84qN2Q4Y_m4iqG4T38ICuP4lW_nKmUM14OFbKhZw1m4Ryh43dn-3eDVxDLV5dnN5x2W9PudHsOfhfEalX50FU0kDksHbuOmZyfRhb23ivipLP_yfAysdbYi5ETV9JJVVgyVdLxSF3m2ofibXQipX6WSVTG0HpWDIGSF9yXHpy4C61oZMAY6Nsd7y6W67sWYJk54keHs5fi0cnSSCdXZPmYHVdlyNZQpHJj33cnbhgdLgACJXGWiQULwsYj-uQzAEO3BaY1Drg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=FOdwxxZJF5XW6P8wn2c2f4GxLg9H27wR_pkXqO7lZFCCVRARr-iqHoreuTg9OOsyLgBFbete5xyIYCsQiM-DiU8L8fgrSfNOXZiBRR0Hz3kSOMcvs6zFXpP9EzydnN4MzmsEOYrjgOIap8tvNtYROkt1lpzrB-UYLrC183vHmT2eZiTxJNfK1U9N66q4faEkelVRUwVQLnhjnolBWv-hTyfVe9YwgwiNLPp2RFPhyj8-bPFpJgSZrm5ml4tbfi88BDcH_IPjqTtHXUboPZ8OQWVviPowPJm2_4Hx0DP5ndTLbMflQT_kbpGXjjjlZ-Axy61LdHcopgwna2NDJ0P-q4cDTr4keWoR_pXm73a0HR1XWK8eXE8NaE79LHKuBWoXSnO9hYFg6_zGaEr0wN3kWqG3mZ7H06DFdC84qN2Q4Y_m4iqG4T38ICuP4lW_nKmUM14OFbKhZw1m4Ryh43dn-3eDVxDLV5dnN5x2W9PudHsOfhfEalX50FU0kDksHbuOmZyfRhb23ivipLP_yfAysdbYi5ETV9JJVVgyVdLxSF3m2ofibXQipX6WSVTG0HpWDIGSF9yXHpy4C61oZMAY6Nsd7y6W67sWYJk54keHs5fi0cnSSCdXZPmYHVdlyNZQpHJj33cnbhgdLgACJXGWiQULwsYj-uQzAEO3BaY1Drg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
تقلید صدای باحال از گزارشگران مراکز استان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107383" target="_blank">📅 19:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/464a64d711.mp4?token=YFqif86hZZakU-5uR0b3spSn1nbsuTtC96intu6zbsF_ZnOq7ye7Ihf_AlRv-kVDCW05UWyy1ECvgGowtFQZ2VrjhlWJfcf8HaNa13QB793iiQW2Pe65uYRk5I3YMwAtihqQOy7EkgbEaN9YW4KTj4oIrBI1Y97gOPy4LGdaijeXno-91c8V737mBjYCv1MLrAqyftodZ3KYP9yn6lTXfJ0ZeHj-eq1LQwmIaboCRL8X5od_RoYgEBkKWt-cwLHLQEZ8visTaEG7v5rlm8dTNKiFa8h1igjCKmC8qV3hY6tLuy9fSyxgGtm9j8jeFZ-QHpQ5WXSrSNfk01ViJy9raJEyNAovjxbFikzgYsd7UjjFsNiolE47crdBbl8Q4QJO0nQ9VIbKJKLTCcPsl-5tB3gf8NxqiwjnXzCu_xz9Gixabj62R0oR4CuYv7nKxIH_Fkfi_t46uJRunGKdErKT3QLnSYQk8XwFEEAbg1a2oOiNrFvISgZ8HeEcax_ZyPuFfDVcJm3hqRxRRN5spKSHqrinFNnYP9h6DFhDmuG8BV-fzbTxkuz--ui6q9u7nmYwb1i5XXMPtK6_7s2ykCSPNXpCx6sTtPPzsNm1hnD-LMG7JpJAh6CH85XSu6X8scCjr4A5pBOEdQpBGW-okmMDUdrDLIaILq5gfXUaI1nd-hU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/464a64d711.mp4?token=YFqif86hZZakU-5uR0b3spSn1nbsuTtC96intu6zbsF_ZnOq7ye7Ihf_AlRv-kVDCW05UWyy1ECvgGowtFQZ2VrjhlWJfcf8HaNa13QB793iiQW2Pe65uYRk5I3YMwAtihqQOy7EkgbEaN9YW4KTj4oIrBI1Y97gOPy4LGdaijeXno-91c8V737mBjYCv1MLrAqyftodZ3KYP9yn6lTXfJ0ZeHj-eq1LQwmIaboCRL8X5od_RoYgEBkKWt-cwLHLQEZ8visTaEG7v5rlm8dTNKiFa8h1igjCKmC8qV3hY6tLuy9fSyxgGtm9j8jeFZ-QHpQ5WXSrSNfk01ViJy9raJEyNAovjxbFikzgYsd7UjjFsNiolE47crdBbl8Q4QJO0nQ9VIbKJKLTCcPsl-5tB3gf8NxqiwjnXzCu_xz9Gixabj62R0oR4CuYv7nKxIH_Fkfi_t46uJRunGKdErKT3QLnSYQk8XwFEEAbg1a2oOiNrFvISgZ8HeEcax_ZyPuFfDVcJm3hqRxRRN5spKSHqrinFNnYP9h6DFhDmuG8BV-fzbTxkuz--ui6q9u7nmYwb1i5XXMPtK6_7s2ykCSPNXpCx6sTtPPzsNm1hnD-LMG7JpJAh6CH85XSu6X8scCjr4A5pBOEdQpBGW-okmMDUdrDLIaILq5gfXUaI1nd-hU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⚪️
⚽️
چرا تیم امید همیشه ناکام است؟ این ۱۴۰ ثانیه از فرهاد مجیدی را گوش کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107382" target="_blank">📅 18:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107379">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36187cd975.mp4?token=IW13KJsOuk0e0dC7CzHEMqY7ItV23stWY0OQvrrj2KiDK9ZWSjaFDbOcp2AkIrwUcslcVlQEOY95lBV7RL0eo37nH4aIU5UjZ26-dC5Fw9EiUGPDNWItklMSyq-AkS5FMS1qFbx_q_-IHiSFxM0EMdcUjSkKxz7FI8QKsYSgvKKn4Z8RagCU1Au7Elmf6xqmWmAZ0I1AZzyU9Rmc5325rXMGKePI_18nOYy23LmkMXljlRbTbgrfA5t5FPSNHH1cuMZm1N3Jk6k6uHsXaFPBDsAHECyMIGttDLLOsPnrds4_PQWMbLbaB9xCAvachHnoZoLaMGQABK2n082u61lMeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36187cd975.mp4?token=IW13KJsOuk0e0dC7CzHEMqY7ItV23stWY0OQvrrj2KiDK9ZWSjaFDbOcp2AkIrwUcslcVlQEOY95lBV7RL0eo37nH4aIU5UjZ26-dC5Fw9EiUGPDNWItklMSyq-AkS5FMS1qFbx_q_-IHiSFxM0EMdcUjSkKxz7FI8QKsYSgvKKn4Z8RagCU1Au7Elmf6xqmWmAZ0I1AZzyU9Rmc5325rXMGKePI_18nOYy23LmkMXljlRbTbgrfA5t5FPSNHH1cuMZm1N3Jk6k6uHsXaFPBDsAHECyMIGttDLLOsPnrds4_PQWMbLbaB9xCAvachHnoZoLaMGQABK2n082u61lMeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
محکومیت ۴۰۰ هزار دلاری استقلال در پرونده کاریله؛ آیا تاجرنیا طبق وعده ای که قبلا روی آنتن زنده تلویزیون داده بود، مطبش را برای پرداخت این جریمه می‌فروشد؟ آیا دیگر اعضای وقت هیات مدیره، طبق گفته تاجرنیا از جیبشان این خسارت تقریبا ۹۳ میلیارد تومانی را می‌پردازند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107379" target="_blank">📅 18:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107378">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=Xe94qYA6aGl8O8Qo91y3HVUuqTCW1vau_zDCb7QgOv8WPbiDNvrCvM82gJzyzEMr4jvFHYT8Ykgu1T1XSkeiY0BoxC1E_iRsKb-cCR6scGpIRlOrxHBpUlv_Nwh5pxiwsh8ZEUTpQQtPJvTAvqVLVT0YoK8Ah-u4bC3ZU57Ixi1lPIL43p08z2CTRPaLfmpMEgPWLIYlAwpw8Te8gM3zUtz_Q6IJgxbh5cFUuA04-TwILlNVvWui5WkV_gSe3b028qUWvSR8lKVkx9fNie57qNr65g_ZuRDm0WVD6leX7DDZyB5zKHgGExPBzLr_fjCu0sGNpBWyL4sprqdOVWvy4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=Xe94qYA6aGl8O8Qo91y3HVUuqTCW1vau_zDCb7QgOv8WPbiDNvrCvM82gJzyzEMr4jvFHYT8Ykgu1T1XSkeiY0BoxC1E_iRsKb-cCR6scGpIRlOrxHBpUlv_Nwh5pxiwsh8ZEUTpQQtPJvTAvqVLVT0YoK8Ah-u4bC3ZU57Ixi1lPIL43p08z2CTRPaLfmpMEgPWLIYlAwpw8Te8gM3zUtz_Q6IJgxbh5cFUuA04-TwILlNVvWui5WkV_gSe3b028qUWvSR8lKVkx9fNie57qNr65g_ZuRDm0WVD6leX7DDZyB5zKHgGExPBzLr_fjCu0sGNpBWyL4sprqdOVWvy4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درگیری شدید سوبوسلای و بازیکنان حریف در بازی اخیر مجارستان مقابل اوکراین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107378" target="_blank">📅 18:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107377">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=rdwd2VwbUyr2S6SW0A94KIrJYAU3LncjtSN8DT_BPfwh6wCtBrMmC8f99H9X8dGwAsZzL-Szv8Y72cPks7Q-Ybn3rRZYn9U8jpww05TJkYr7_r41BAjz77rJeTRGKXZkwEd6KOqrYT3aIy8Es9VvjEJ-EpdClTmZd97bKwGcEEtvjdBnrPhILKuzSVHSR_AQRE5AdoaGYHsHw_1YnVdGmZdV_WxkR_ab3VsFOQcqwohuDIMjSZAF3pS5aV9S-KonqT9FEoBUeGZIXLlqPqLsz9G7cpg_BRX2pZKXlpOwrP6ATNGpP2ffvMELTcS2agJarv31zoSpf85AXo6BS-2KTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=rdwd2VwbUyr2S6SW0A94KIrJYAU3LncjtSN8DT_BPfwh6wCtBrMmC8f99H9X8dGwAsZzL-Szv8Y72cPks7Q-Ybn3rRZYn9U8jpww05TJkYr7_r41BAjz77rJeTRGKXZkwEd6KOqrYT3aIy8Es9VvjEJ-EpdClTmZd97bKwGcEEtvjdBnrPhILKuzSVHSR_AQRE5AdoaGYHsHw_1YnVdGmZdV_WxkR_ab3VsFOQcqwohuDIMjSZAF3pS5aV9S-KonqT9FEoBUeGZIXLlqPqLsz9G7cpg_BRX2pZKXlpOwrP6ATNGpP2ffvMELTcS2agJarv31zoSpf85AXo6BS-2KTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
گریه‌های آرش‌افشین بازیکن سابق استقلال: نتونستم پول خوبی از فوتبال در بیارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107377" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107376">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=S9ILzI5nvGvVmLMyEil559YNK13gw6bxoJnDKlfrziIV4MhfXFkVH3dxosBeqMNHuJz04XHSDKCFEsGrffgPwfauvwMEIJiJQmLDm7ZU--2oczC3ZyuEzvF9X6LPzyU4YO2svpwweZHDAP0AMDyR3gCNGxNjfjw-eK7eMzdRHVf5yDez3TZyOFvEw971oLBAaV1RpJJID8MN66bOhaSP0Ck97GurZyycExtFJUADhAqQ3PUE7VUiep4rrwNSxxvd9cAJ-LR3yoLlPUw-PTlY8m-QpT4ZwDMaoXh_a9kOs0SrxCD8cg3O2ND1nLvLxdeFiigGWd_EqPAfTWXCwczR3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=S9ILzI5nvGvVmLMyEil559YNK13gw6bxoJnDKlfrziIV4MhfXFkVH3dxosBeqMNHuJz04XHSDKCFEsGrffgPwfauvwMEIJiJQmLDm7ZU--2oczC3ZyuEzvF9X6LPzyU4YO2svpwweZHDAP0AMDyR3gCNGxNjfjw-eK7eMzdRHVf5yDez3TZyOFvEw971oLBAaV1RpJJID8MN66bOhaSP0Ck97GurZyycExtFJUADhAqQ3PUE7VUiep4rrwNSxxvd9cAJ-LR3yoLlPUw-PTlY8m-QpT4ZwDMaoXh_a9kOs0SrxCD8cg3O2ND1nLvLxdeFiigGWd_EqPAfTWXCwczR3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
⚽️
افشاگری حجت‌کریمی عضو هیئت رئیسه فدراسیون: قلعه‌نویی قرارداد ۴ ساله می‌خواست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107376" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107375">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=hnNRXgLfGUkJa44voqdtPzN9m_xbH4aVT7cBiwSQ5oS57hP1wZ6L5yOuM7OYqXfX5RAITb8BBT68IZkFe2rtLqVIi_OVfaJBaDxT7ocIeJwhDenUiGy025ljvXPPVkHJwaM2aL2CXgMllhBbzFWks3t8B7w1bKssdC1rmgPczKWZ6xai70yqsG46wtZhAeI_6T5gWbg16V5AdvtJzJiVF0jYxwkastBPLDQNaCSJ5gmGyzkvXOJoLHXaH1N2ePkS85cgsp3BDG9y6Y6wm5zT-tuqSm82O1Fc__XwsmDxrFXIzi-RTukcnmoHEnTp-4rBETu-O43DdCiUsLrn0ZRUwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=hnNRXgLfGUkJa44voqdtPzN9m_xbH4aVT7cBiwSQ5oS57hP1wZ6L5yOuM7OYqXfX5RAITb8BBT68IZkFe2rtLqVIi_OVfaJBaDxT7ocIeJwhDenUiGy025ljvXPPVkHJwaM2aL2CXgMllhBbzFWks3t8B7w1bKssdC1rmgPczKWZ6xai70yqsG46wtZhAeI_6T5gWbg16V5AdvtJzJiVF0jYxwkastBPLDQNaCSJ5gmGyzkvXOJoLHXaH1N2ePkS85cgsp3BDG9y6Y6wm5zT-tuqSm82O1Fc__XwsmDxrFXIzi-RTukcnmoHEnTp-4rBETu-O43DdCiUsLrn0ZRUwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبرد دو هیولا از دو نسل! امشب در اسلوی نروژ.
🔥
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107375" target="_blank">📅 16:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107374">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119aac7582.mp4?token=Bwu7jt0ke0ccvYX3HpV5StkA9eR6r0K04QBt3HHUd7-5RAJD_BF-vdWvDAEyZo16vjMgbAzMqXYgVq2ds9QPJXKaVWPrbiQ-kPxZKX-Gb2QZG61XXrYV3Bk5GmEa177Sk0bLVpTSivaf6HmP-9ddsKup0MnpQNJOCQOhLCMoBR9YbAhHQMtjXGQJsqF-KyJRX7GpzcuxTOd3Tx4Gokeq4ZghrS4oLjUvIso4L__xRt4gPhq20Mr9gr7Jd_GoqfGUwzlTubw0F1k1QcMlwQZ9kBjdWaOdYhaeLhgF-u8aNDwj7SJbLut0N7JmFs5mj7vfSXYkn4vscovdbRvswru_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119aac7582.mp4?token=Bwu7jt0ke0ccvYX3HpV5StkA9eR6r0K04QBt3HHUd7-5RAJD_BF-vdWvDAEyZo16vjMgbAzMqXYgVq2ds9QPJXKaVWPrbiQ-kPxZKX-Gb2QZG61XXrYV3Bk5GmEa177Sk0bLVpTSivaf6HmP-9ddsKup0MnpQNJOCQOhLCMoBR9YbAhHQMtjXGQJsqF-KyJRX7GpzcuxTOd3Tx4Gokeq4ZghrS4oLjUvIso4L__xRt4gPhq20Mr9gr7Jd_GoqfGUwzlTubw0F1k1QcMlwQZ9kBjdWaOdYhaeLhgF-u8aNDwj7SJbLut0N7JmFs5mj7vfSXYkn4vscovdbRvswru_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دو بازی، دو گزارش، یک تفاوت عجیب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107374" target="_blank">📅 16:05 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
