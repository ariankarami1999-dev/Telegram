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
<img src="https://cdn4.telesco.pe/file/meHZS16YGnb4UVhhcHe7z8K1LusgMf8pqLlzPQwyfT0LhvHltHzBWLFoVypUY0MgcxmDpLtbCf3XqoBmOWZ0MktjC-EVNxiDAyh0z-OyAX69loIumekj_8fPQIJWmtlfp8Pso5igGniQJzCBdMimSRtqP3Q7NXsWZUCJBS9MbLOz6HpmW7yooJwzSMUKXOVJaG4i59MNv4mqLE2Lojv-GQIRQs6W6x_8zzfPJso2rirqlhr0-WrdufpBiIZVrb-Qd65xIk-NhY-kM37fjjrIDbkmlJqQeO8iu2pdi5bASPxGn94USkuYmv--ayFfGGAAtg8eARtlQaApa-OCApNcvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 87.5K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-756">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سرور جدید WhiteDNS مناسب موبایل و دسکتاپ
📱
💻
💥
لطفاً تجربه خودتون را با ما در میان بگذارید   تشکر    stromv.iranmotor.biz  da190952ef61ec61fee7597c09c72358  Encryption: AES-128-GCM   @whitedns
🔓</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/whitedns/756" target="_blank">📅 16:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-755">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سرور جدید WhiteDNS مناسب موبایل و دسکتاپ
📱
💻
💥
لطفاً تجربه خودتون را با ما در میان بگذارید
تشکر
stromv.iranmotor.biz
da190952ef61ec61fee7597c09c72358
Encryption: AES-128-GCM
@whitedns
🔓</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/whitedns/755" target="_blank">📅 16:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-754">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/754" target="_blank">📅 16:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-753">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAPtUHFHu19qJLAPXhRDm_oOrQDpOW1V2CCUwOOwy0_uV0J5Ta-J0vnNSrf_TqrWWfAHhndCDH_7fi4vVxURIyEqb_YHHL5YBQufR-Ti1Ab_NxByqA4p0ECIW4ad9QfUY8hykps84Dd2XIwJ8IfDYsYYSTtacN1rIRF5HKSRm7OaIM07Y8zx3mBaZfq7OXO3OAeNRP_JbyPhKjUVpkQFdKRl2Z00tuDDqQJPtxbGeZFv34Yg9KaIhgKl0D5iDJLy-9glOph7YE-1CuJEK87icXN1RqoElTG7AlzwTQgJXNvv6JU3ETZ-yNAGv-sbWY-mH4HQgmMg7RlDy-1jnA0kjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/whitedns/753" target="_blank">📅 15:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-752">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompythash</strong></div>
<div class="tg-text">سرور ها آپدیت شدن
دقت کنید هم رمز و هم دامنه تغییر کردن
سرور StormDNS اختصاصی چنل Pythash/پای هش
StormDNS Server Configs
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
@pythash
Domain:
v1.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
@pythash
Domain:
v2.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
نحوه اتصال:
windows , android:
https://t.me/pythash/74
linux:
https://t.me/pythash/81
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🌀
@pythash
🌀
@pythash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/752" target="_blank">📅 15:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-751">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/751" target="_blank">📅 14:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-749">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/749" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-748">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZYMh2V5HR0_MCIWjBfskRj927Kg9fNzsRe8FVBRWiQRC6rCydVXoF2jffT9zq9wzwDKMe3wLVMryrTn73jdFYuZzRM5HlJEkqBdsBvi5yKzYhOmYyyVtXyEQwQPBBnGeKgCnI1VZRTptx1HFvluIbhKZ6m9WNTSO-DXhenLncceRe0xnJyYNRiKxXOHwDzkfdwJK6z2JL8UmUsJUc7voykTE8LCcQH_EgJLhljSayBKFHaBdJ2aS4W4yy4pqS2S2w5wUyZ4UCoVaZ0EDYzPhBnBWTglw7kFg13bMbf7-9Ero1dyMbF6cuw73KbpAedsHbWr6tA10dQMXGOaTHYAc8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/748" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-747">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-poll">
<h4>📊 🌷نظرتون در مورد نسخه جدید Whitedns windows چی هست ؟👀⚠️</h4>
<ul>
<li>✓ عالی</li>
<li>✓ خوب</li>
<li>✓ متوسط</li>
<li>✓ بد</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/747" target="_blank">📅 13:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-745">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcwHawk4E7e1yhAUcgO2rHPTN9dyq8pJUF_Kq0__-AhTc8zFpF9DAgI2hJCTjB1_y7GGK_Tf7raBtoMCVdwO9X3vVzZ3FPFWBLPFxTVOTyv3Foj1pYcbtt4lmgtPJH_y0BM_bJ5l29umQHN_zKCBS60Nsseh5Aq-ttu4iSxOiqwX3sGqBhaFlHCg6ZJEqVWzpCNc90tKK4MZQk3azlqcDFAZ_c3ktX5gBUpuJAqodvxUcc3IfIATbgnsNJqeuNMILCIENiWlb4ACcSI9Lsy2KGEo_MfFkOEqnJe3l6lS0-yl1iK63XL1vX4z3BxRN4xwaDRzvCu82_Vr3_Ty9wKNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eRXnqA2dITLFeW3XPpCGE6YM1oaEKt9Up4tFr4CXLIVBVyckBWAuk3PSlA8VHBP9lNZBr6Ls9dK-HKdFFRjXbOX12nQcfPmVV7QuKeXAQUT0e80DUKSjZCHVfW0JE029751UiIcr2iNpBqKqoBWTqxqkq5w7vedZefPtrL1e_209KrMLvhnu-erbFJzptxthSzJgLef2XUriXA9gSmtEfWW9GWEZTBmK_uQov3-iZvOO_-rKiE0bAtLMi6C_cI241yO2Qtd2i1FKLMAIikPhLk5_zkSA3YBny1E0vKM_5nq1pSajc-8U54BZHZs7UoxjmFOwZITLr3rhL3gB_Rctkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♨️
نسخه 1.0.0 Beta 3 ویندوز WhiteDNS منتشر شد
♨️
سلام به همراهان عزیز WhiteDNS   نسخه جدید ویندوز منتشر شده و در این آپدیت تمرکز اصلی روی بهتر شدن تجربه کاربری، تست سریع‌تر تنظیمات، مدیریت راحت‌تر سرورها و ریزالورها و رفع مشکلات گزارش‌شده بوده است.
🔅
قابلیت‌های…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/745" target="_blank">📅 11:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-744">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👇
👇
👇
👇
👇
👇
این گروه توسط جمعی از فعالین این حوزه مدیریت می‌شود و هدف، دسترسی مردم به اینترنت آزاد است.
چت کردن، صحبتی به غیر از دسترسی به اینترنت، تبلیغ، سؤال راجب فروشنده‌های VPN = مستقیم بن
گروه اصلی:‌
https://t.me/Ir_Blackout
گروه کانفیگ:
https://t.me/Ir_Blackout_Config</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/whitedns/744" target="_blank">📅 10:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لینک های داخلی برای دانلود اپلیکیشن های دستکتاپ
⬇️
Windows
|
Linux
|
Mac
1
.0.0 Beta3
باتشکر از چنل
@masir_sefid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/743" target="_blank">📅 09:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-741">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-arm64.deb</div>
  <div class="tg-doc-extra">15.5 MB</div>
</div>
<a href="https://t.me/whitedns/741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/741" target="_blank">📅 09:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-735">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.9 MB</div>
</div>
<a href="https://t.me/whitedns/735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/735" target="_blank">📅 09:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-734">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKz7aoyhXo17tWfYtJN4FzQKsEkp-EwR5FClo-WitQffkgxAlHnPEZUeFTvu-t3gumqAWnNGjRDM6IoG1t4-vfgr9zMu0bY-NlAf1HOu5nXiJx1HsommqMfsAx4RlLXAq86oHICEANOy8e6tcr6Yri_4bMAu09WqqGp_jkrpM1jZovFe5BKayrZW_KYAtVsTxnWVc1pRVyFSLpYNSRM9gDN1pq7TuNYJTwfnEyUul9mK2eSMJPG34J5M-ik_7VPsQQsubFD9cDxY_Qj44lG3_TLSlG68VAHgzNW5ZuCWCkKlC2Blx7FvYDMwybKyL7J6PNgLTmma7-oihMQgMgDLWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
نسخه
1.0.0 Beta 3
ویندوز WhiteDNS منتشر شد
♨️
سلام به همراهان عزیز WhiteDNS
نسخه جدید ویندوز منتشر شده و در این آپدیت تمرکز اصلی روی بهتر شدن تجربه کاربری، تست سریع‌تر تنظیمات، مدیریت راحت‌تر سرورها و ریزالورها و رفع مشکلات گزارش‌شده بوده است.
🔅
قابلیت‌های جدید
✅
اضافه شدن قابلیت
Parallel Test
برای پیدا کردن بهترین تنظیمات اتصال
✅
اضافه شدن دکمه‌های جدید برای حذف لاگ، کپی لاگ، خروجی گرفتن از سرورها، ایمپورت DNS، خروجی گرفتن و ایمپورت تنظیمات
✅
امکان انتخاب نتایج اسکنر و ساخت پروفایل جدید بعد از اسکن
✅
امکان کپی همه نتایج اسکن، انتخاب دستی نتایج و کپی موارد انتخاب‌شده
✅
اضافه شدن قابلیت مرتب‌سازی تنظیمات، سرورها و ریزالورها
✅
نمایش IP ویندوز برای اشتراک‌گذاری اینترنت با موبایل و سایر دستگاه‌ها
✅
اضافه شدن قابلیت ریست تنظیمات برنامه
🔅
بروزرسانی‌ها و بهبودها
✅
بازطراحی و رفع مشکلات تب داشبورد
✅
اضافه شدن اسکرول در بخش‌های سرورها، ریزالورها و تنظیمات
✅
بهبودهای مختلف بر اساس گزارش‌های کاربران
لطفاً نسخه جدید را تست کنید و اگر مشکلی دیدید، همراه با لاگ و توضیح دقیق در بخش مربوطه گزارش دهید تا سریع‌تر بررسی شود.
ممنون از همراهی و گزارش‌های ارزشمند شما
🙏
@WhiteDNS</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/734" target="_blank">📅 08:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-732">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.8 MB</div>
</div>
<a href="https://t.me/whitedns/732" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
دوستان عزیز Linux, اپ دسکتاپ WhiteDNS Beta2 برای لینوکس هم آماده کردیم و میتونید دانلود کنید.
این نسخه بتا هستش  و ما در روز های آینده دایما با فیکس ها و فیچر های بیشتر آپدیت میدیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/whitedns/732" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-731">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8K7iu02fToLmkSWwupLs6jyPcf4U8_CLSMqcNzHVjQvGamcUtutuRjkn9P-BfgDi8skrmtJ8-zqFIiWk6bBo5p7l4AIyTde-0FXmoXHpKtgGkC-yKQDLzyshuWeJKq5fAbK9pTCuDTL25Ju_dCEF6to-eCTUO6j1wl_fklNelWOYOFZJOmZVgRHoHzAT6nV32VVPABz-wDPEiiXsUmlCorsFnM_TDA3YAJBTKgLoJSFfJEXWTGVyjJNSf7n1valhqFLJp_TrK1dQoMlzxeX05aSoYP3J7dUZt6oiAOjI3DWdr86X3EHRQRjdtfE7igX27EuJGZ4uTGADx30Mk-pAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/731" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">لیست ۱۰۰ ریزالور موقفی که در ۲۴ ساعت گذشته به سرور های WhiteDNS وصل شدن
80.75.7.2
31.214.169.244
185.208.183.29
62.60.144.87
93.115.127.9
5.160.128.142
109.230.89.90
185.142.158.162
134.255.206.205
185.53.142.174
94.232.173.28
185.88.178.196
2.188.21.58
46.245.80.82
62.60.144.85
185.255.91.60
185.109.61.27
2.188.21.70
74.63.24.210
185.208.174.167
185.141.105.139
185.51.201.58
217.66.203.211
2.188.21.46
85.185.157.181
5.202.252.30
172.64.32.0
173.245.58.0
93.118.127.118
108.162.192.0
78.39.234.140
178.252.128.66
158.58.184.147
37.191.95.70
164.138.17.122
185.50.37.52
46.32.31.30
185.53.141.230
92.246.87.191
93.118.109.213
5.160.140.16
2.188.21.146
2.188.21.138
2.188.21.62
5.160.227.78
5.160.2.55
5.160.137.130
109.72.197.1
74.80.77.246
80.210.40.53
74.80.77.247
80.210.40.50
207.211.215.145
185.191.79.210
74.80.77.244
81.16.121.151
78.157.41.60
217.218.59.18
45.135.241.33
194.61.120.143
74.80.77.245
217.219.76.102
85.185.1.10
185.129.170.75
46.209.44.74
43.226.5.169
87.107.9.233
79.175.172.101
2.188.21.78
172.253.228.147
185.213.11.85
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/730" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-729">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سلام عزیزان، امیدوارم در این اوضاعِ به شدت خراب و زندگی در کشوری که توسط یک رژیم فاسد اداره میشه همچنان قویی باشید و حال دلتون عالی باشه. همونطور که میدونید ما
به شدت
با پروسه‌ی فروش
مخالف
بوده ایم و تمام فعالیت های ما برای
تمام
مردم ایران به صورت
کاملا
رایگان
بوده؛ اما جا داره که از تمام کسانی که چه با کریپتو و چه با استارز زدن به پست ها از ما حمایت میکنند تا فعالیت چنل و سرورها مداوم باشه، تشکر کنم. در این مدت دقت کردم که تمامی پست های چنل حداقل یک استارز خورده و بدونید که تمام این حمایت ها حتی یک استارزی که میزنید برای ما خیلی با ارزشه و از شما قدردانی میکنیم که در این راه دشوار و مبارزه با این حکومت خون‌خوار در کنار ما ایستاده اید!
❤️
- کوچیک شما Patrick.
WhiteDNS-Team
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/729" target="_blank">📅 14:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-728">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">لینک داخلی تمام پلتفرم های برنامه‌ی WhiteDNS Desktop:
Macos-amd64:
https://guardts.ir/f/736498ddfb14
Macos-arm64:
https://guardts.ir/f/4594c5008167
Windows-x64(amd64):
https://guardts.ir/f/2549b69980b3
Windows-arm64:
https://guardts.ir/f/05e3847a8a43
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/728" target="_blank">📅 13:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-727">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/whitedns/727" target="_blank">📅 13:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-726">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/726" target="_blank">📅 11:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-725">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shw78TyNobtzsei96iiZCzJg0zk3x1z4I7XNHP7-VovUXca0D7-fzS_UaOBtyOSGaW_2vcuLs0FqqF3CutdRXN1ejgpIt_-xspS4F-5SwHhw3dtzBjzxgQ4eJBa6iRKzoMuMvsv9wNSffTNVVG9T-rELZk54ciULK4znxjY9LRpJqrVqQI6B5rRxyt-twvSoFpKbPkMTsxWE91CSaTMbIM-G94cGC-o56bBvMJ5nLgQmWoYr8jAE_n3uPcHTsL_mOrKsDRyq62jA70VvAr0DVz8cyl2D4YlMzAnpKTSwP4ySjzhBH4VeGMNxr93_zi5UPV_FYmnPScgzUYsAv5r2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی مک، دوستانی که مشکل باز کردن اپ رو دارید، دستور زیر رو اجرا کنید
chmod +x "/Applications/WhiteDNS Desktop.app/Contents/MacOS/WhiteDNS Desktop"
xattr -dr com.apple.quarantine "/Applications/WhiteDNS Desktop.app"
open "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/725" target="_blank">📅 11:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-721">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/whitedns/721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه WhiteDNS Desktop V1.0.0-beta2
✅
حل مشکل باز کردن در ورژن های قدیمی مک
✅
حل مشکل وصل نشدن و خطا بعد از ۴۵ ثانیه
✅
حل مشکل وارد کردن کانفیگ به صورت گروهی
✅
حل اضافه شدن دگه ذخیره برای ریزالور های سالم و. فعال به صورت جداگانه
✅
حل مشکل مشکی شدن صفحه در ویندوز
✅
اضافه شدن نسخه های لینوکس</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/whitedns/721" target="_blank">📅 10:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-717">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/whitedns/717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎉
WhiteDNS Desktop منتشر شد</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/717" target="_blank">📅 08:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-716">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjPG3TxLz-yQl0mmevNwwpQ0fptL1G4FO92_zDXIR4XdCVxL5O8WfeKxF7UID4wEB81C_mhzjAfMH2TInvChvqQYLRHdFLNzTjVmeaHMC_TMJFGp6z9H2oZ7K0zzDH63UR0pKozCXm0wVbXFYfVpPCOkVzdHA15yvxmdqE_obmZ7Q9oAu64LdTj9dPH154uHd0IEoxMa4e3JOxyphJGbDbOLM0no7LxkWyfcEKVeH37Cvp3PkETYxg6qT6dnexFOKh_IWIDzL8zUP89Xli93UMdfnR9zn4EciMxPZuKT_f0VtI4vvah5B6ESAJgGx2Zq9Ozn9GuzFRUI7p0mZkT5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteDNS Desktop منتشر شد
نسخه دسکتاپ WhiteDNS حالا آماده استفاده است.
این برنامه برای کسانی ساخته شده که می‌خواهند اتصال‌های MasterDNS و StormDNS را روی کامپیوتر، ساده‌تر، سریع‌تر و بدون درگیر شدن با ترمینال و فایل‌های تنظیمات اجرا کنند.
با WhiteDNS Desktop می‌توانید پروفایل اتصال را وارد کنید، Resolverها را مدیریت کنید، اتصال را فقط با یک دکمه روشن یا خاموش کنید و وضعیت همه‌چیز را به‌صورت زنده ببینید.
✨
امکانات اصلی
✅
اتصال و قطع اتصال فقط با یک دکمه
✅
رابط گرافیکی ساده برای Windows و macOS
✅
پراکسی محلی آماده برای مرورگرها و برنامه‌های دیگر
✅
پشتیبانی از SOCKS و HTTP از طریق sing-box
✅
امکان فعال کردن System Proxy
✅
وارد کردن پروفایل‌های آماده با لینک‌های
stormdns://
✅
ساخت و مدیریت چند پروفایل اتصال
✅
ساخت و مدیریت چند لیست Resolver
✅
بررسی خودکار معتبر بودن Resolverها
✅
نمایش Resolverهای فعال، آماده‌باش و ردشده
✅
نمایش سرعت دانلود، سرعت آپلود و مصرف کل داده
✅
نمایش روند اتصال و درصد پیشرفت هنگام راه‌اندازی
✅
امکان توقف و ادامه دادن تست MTU هنگام اتصال
✅
خروجی گرفتن از تنظیمات به‌صورت
client_config.toml
✅
بخش لاگ و جست‌وجوی لاگ‌ها برای عیب‌یابی راحت‌تر
⚙️
تنظیمات پیشرفته برای شبکه‌های ضعیف و ناپایدار
برای کاربرانی که روی اینترنت‌های محدود، ضعیف یا ناپایدار هستند، تنظیمات پیشرفته هم داخل برنامه قرار داده شده است:
✅
انتخاب روش بالانس بین Resolverها
✅
تنظیم Packet Duplication برای پایداری بیشتر
✅
تنظیم فشرده‌سازی آپلود و دانلود
✅
تنظیم MTU، Timeout، Retry و تعداد تست هم‌زمان
✅
کنترل Workerها، Streamها و صف‌ها برای سیستم‌های مختلف
✅
وجود Watchdog برای بررسی زنده بودن اتصال
🔍
ابزار Scanner داخلی
در این نسخه، یک ابزار Scanner هم داخل برنامه اضافه شده است تا تست و بررسی Endpointها راحت‌تر شود:
✅
تست سریع یک Host با چند پورت
✅
اسکن گروهی از فایل‌های TXT، CSV یا JSON
✅
تست پروتکل‌های TCP، TLS، HTTP، WebSocket، UDP، QUIC/H3 و DNS
✅
نمایش Score، Grade، Latency، Jitter، Packet Loss و Stability
✅
بررسی اینکه Endpoint برای Tunnel آماده هست یا نه
✅
امکان دیدن و کپی کردن نتیجه کامل به‌صورت JSON
این نسخه برای کاربران عادی طراحی شده تا اتصال راحت‌تر و بدون دردسر انجام شود؛ اما برای کاربران حرفه‌ای هم تنظیمات دقیق‌تر در دسترس است تا بتوانند اتصال را با شرایط شبکه خودشان بهتر هماهنگ کنند.
⚠️
توجه: این نسخه هنوز بتا است.
اگر مشکلی مشاهده کردید، ارسال گزارش خطا، لاگ برنامه و توضیح شرایط شبکه شما کمک زیادی به بهتر شدن نسخه‌های بعدی می‌کند.
ممنون از همراهی شما با WhiteDNS
🤍</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/716" target="_blank">📅 08:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-715">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRumUTWKH5ZXxULcF5ghZZMOXyUQb0AtNW2eJ__pjI06mmH0o9hTek7k1cSfV2IwS1boX8bH9EdyhJf5Zz09xRMoXf6RlBMjMSI79yv9Is25xUOHMIe7RuiX4JlqpTFPeDi8DnHYVXtHtab6Q0zU-tDIfpo0vkrDu_MQNRleYCOY738dtaPumJ7V0WwLZSzA-C9F3qnTOxFMNoEu0uykjjAJDncmewHw0vvyE6lxby6oIoFqwYx2POb2MG5rtuG2k-NtNzVaGHijERjniVAbEau20iFNL37__2oEkw7iZZN6Z6k-_1lfP1ZYEy5i_BjvgfIjCV2ymDq6GCebfxItGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همراهان عزیز،
بعد از بازخود هایی که ما از ورژن قبلی اپ ویندوز گرفتیم، تصمیم به بازنویسی این نرم‌افزار برای سیتم عامل های
مک ، ویندوز و لینوکس
گرفتیم.
تقریبا تمام امکانات اپلیکیشن اندروید در این اپ خلاصه شده اما با قدرت و منابع بیشتر.
سعی میکنیم هرچه زودتر اپ رو آماده و در اختیارتون قرار بدیم.
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/whitedns/715" target="_blank">📅 07:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-714">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">خب این هم آموزش SNI Spoof برای مک.
فرآیندش برای ویندوز و لینوکس کاملاً مشابه هم هستش. فقط باید فایل اجرایی‌ای که برای sni spoof هستش رو مطابق سیستم‌عاملتون دانلود کنین.
فرقی هم نداره که از چه برنامه‌ای برای کانفیگ‌ها استفاده کنین.
لینک دانلود برنامه SNI Spoof برای مک و لینوکس
برنامه آپلود شده در تلگرام
لیست کانفیگای جمع آوری شده توسط متین عزیز.
کانفیگ JSON
لینک دانلود ویدئو بالا برای اینترنت ایران.
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/714" target="_blank">📅 02:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-713">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5FR9uGlq1r7hj6dIjvIsBSNfm0Tc15FiT_9Hb2hHOHGqcJw0UkvltcMGKglwuJEf_S-MWSz9wa8N9J17lXsycI8FedyN2mcR5CExq5J1WbL6K_5cRYicLo78pXsPxxEUVRu9PpEHQbOzagYMIF93VySa0EZJeozQTkfxzgZI0Ij2dKWgyjkI1WnxUmEfvmtMHqXBGu9QtmHoSR6UoMF8H6PVIXmX66nj1I1NvUKMnOzaKcxCZYcqAut351T_mtmdpKPauWHcQiszVNvHRWBltYTp-qjd0Y-_u2SkNRa9-DOtvbEJebdrv4aU40t6nR6g99boDstB-NJ1-iW8Nl26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد میکنم تنظیمات موازی سازی MTU رو بین ۵۰ تا ۳۰۰ بسته به جدید قدرت گوشی همراهتون بذارید.</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/whitedns/713" target="_blank">📅 18:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-708">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/708" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/whitedns/708" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-707">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXsfUurWda-jEigkkRBmGXA9taICNlsmuG0-CjTAcuycgO-t1To7mY2PJ6gSqy0YDkZoBFT56cGZWgFG4MzrRXKK-1NldDG25iCPH06aCzW6yyD-bGlzKaBp9O_I3q_IgMdtEiuMLJl5zxVRjb8cjoXGdAwKPWx2l-nwtKDcD1PlyUSciIwtH_rbuKL7rMPwgp0_XkXO7jkXssPMng8JVvebnkqPGAXt_zg3qKLhmBjMw514xOWoXHrafQTEMPFVVmlMUO2KAwQ2m6VKTHQM4WPGhhBj5E3igImQRTpc-ObbM63rX7A4jA8dW5aoapw5zZ9uisixxg-6iUyI2EdwfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همراهان عزیز
تغییر بزرگی در این ورژن انجام نشده. تمرکز در این نسخه روی
بهبود  تست موازی تنظیمات بوده. در این نسخه تنطیمات بیشتری و بهینه تری به این قابلیت اضافه شده.
✅
نسخه اپلیکیشن به 1.5.1 ارتقا پیدا کرده
✅
جدا شدن تنظیمات پر مصرف و بهینه در تست موازی.
✅
بعد از یک همه پرسی در کانال، حالا تنظیمات در ۱۰ دسته متفاوت تقسیم شده تا بهینه ترین تنظیمات بر اساس ریزالور های انتخاب شده برای شما استافده شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/707" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">برای باز کردن اینستاگرام در مرورگر گوشی (بدون اینکه وارد اپلیکیشن شوید)، می‌توانید این مراحل را دنبال کنید:
📱
💻
۱.
مرورگر خود را باز کنید:
🌐
وارد مرورگر گوشی خود (مثل Chrome در اندروید، Safari در آیفون، یا Firefox) شوید.
۲.
به سایت اینستاگرام بروید:
📍
در نوار آدرس بالای صفحه،
[www.instagram.com](https://www.instagram.com)
را تایپ کرده و جستجو کنید.
۳.
وارد حساب کاربری خود شوید (Log In):
🔐
در صفحه باز شده، روی گزینه
Log In
ضربه بزنید و نام کاربری (یا ایمیل/شماره موبایل) و رمز عبور خود را وارد کنید.
نکته مهم (جلوگیری از باز شدن خودکار اپلیکیشن):
⚠️
بسیاری از اوقات، وقتی آدرس اینستاگرام را در مرورگر وارد می‌کنید، گوشی به طور خودکار شما را به اپلیکیشن اینستاگرام (اگر نصب باشد) هدایت می‌کند. برای جلوگیری از این اتفاق، می‌توانید از ترفندهای زیر استفاده کنید:
راه حل اول (سریع‌ترین راه):
🚀
مرورگر خود را در حالت
ناشناس (Incognito یا Private)
باز کنید و سپس سایت اینستاگرام را در آن وارد کنید. در این حالت، لینک‌ها به اپلیکیشن منتقل نمی‌شوند.
راه حل دوم (تغییر تنظیمات در اندروید):
🤖
به تنظیمات گوشی (Settings) بروید.
بخش برنامه‌ها (Apps) را باز کنید و Instagram را پیدا کنید.
به بخش
Open by default
(باز شدن به‌طور پیش‌فرض) یا
Set as default
بروید.
گزینه باز کردن لینک‌های پشتیبانی‌شده (Open supported links) را خاموش کنید یا روی حالت "همیشه بپرس" (Ask every time) قرار دهید.
راه حل سوم (در سافاری آیفون):
🍎
در گوگل کلمه Instagram را جستجو کنید. روی لینک سایت اینستاگرام در نتایج جستجو
انگشت خود را نگه دارید
(Long press) و از منوی باز شده گزینه
Open in New Tab
را انتخاب کنید.
@whitedns
📡</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/whitedns/705" target="_blank">📅 07:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">WhiteDns-Windows-Setup.exe</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/whitedns/704" target="_blank">📅 07:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/703" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteDns Windows 1.0.6
🖥
🔌
راهنمای اتصال هوشمند (Smart Connect)
🤖
قابلیت اتصال هوشمند به برنامه WhiteDns کمک می‌کند تا بهترین تنظیمات اتصال را به‌طور خودکار انتخاب کند. کاربران عادی نیازی به تغییر دستی تنظیماتی مانند MTU، Workers (تعداد پردازش‌گرها)، Packet Duplication (تکثیر بسته‌ها)، فشرده‌سازی (Compression) یا سایر تنظیمات در بخش پیشرفته (Advanced) ندارند.
✅
نحوه استفاده
📝
۱. برنامه
WhiteDns Windows
را باز کنید.
🪟
۲. به تب
Connect
(اتصال) بروید.
🔗
۳. مطمئن شوید که گزینه
Smart Connect
روی حالت روشن (
On
) قرار دارد.
🟢
۴. هدف اتصال خود را انتخاب کنید:
Stable (پایدار)
🛡
بهترین گزینه برای شبکه‌های ضعیف یا فیلترشده. این امن‌ترین و مطمئن‌ترین گزینه است.
Balanced (متعادل)
⚖️
برای اکثر کاربران توصیه می‌شود. این حالت تلاش می‌کند ضمن حفظ پایداری اتصال، سرعت خوبی نیز ارائه دهد.
Fast (سریع)
🚀
بهترین حالت برای زمانی که شبکه شما از قبل قوی است. ممکن است در این حالت از تنظیمات تهاجمی‌تری استفاده شود.
۵. موتور (Engine) را انتخاب کنید:
⚙️
MasterDNS
برای اکثر کاربران و اتصالات پایدار توصیه می‌شود.
StormDNS
در صورتی از این گزینه استفاده کنید که پروفایل/سرور شما برای StormDNS ساخته شده است یا می‌خواهید موتور سریع‌تر را آزمایش کنید.
⛈
۶. حالت پروکسی را انتخاب کنید:
🌐
System proxy (پروکسی سیستم)
برای وب‌گردی معمولی توصیه می‌شود. مرورگرها و بسیاری از برنامه‌های ویندوز به‌طور خودکار از WhiteDns استفاده خواهند کرد.
🖥
SOCKS5 only (فقط SOCKS5)
اگر می‌خواهید پروکسی را به‌صورت دستی در برنامه‌هایی مانند تلگرام تنظیم کنید، از این گزینه استفاده کنید.
📱
۷. روی
Connect
کلیک کنید.
👆
چه اتفاقاتی به‌طور خودکار رخ می‌دهد؟
🔄
وقتی اتصال هوشمند (Smart Connect) روشن است، WhiteDns کارهای زیر را انجام می‌دهد:
- استفاده از موتور انتخاب‌شده (MasterDNS یا StormDNS).
🛠
- بررسی تنظیمات موفق که در دفعات قبل جواب داده‌اند.
✔️
- انتخاب یک پیش‌تنظیم (Preset) مناسب بر اساس هدف شما.
🎯
- استفاده از بهترین تنظیمات شناخته‌شده برای تحلیلگر (Resolver).
📊
- امتحان کردن تنظیمات جایگزین امن‌تر (Fallback) در صورتی که تلاش اول ضعیف باشد.
🛡
- به خاطر سپردن تنظیمات موفق برای استفاده در دفعات بعدی.
💾
کدام هدف (Goal) را باید انتخاب کنم؟
🤔
ابتدا از
Balanced
استفاده کنید. این بهترین حالت پیش‌فرض برای اکثر کاربران است.
✅
در شرایط زیر از
Stable
استفاده کنید:
- اتصال مرتباً با شکست مواجه می‌شود.
❌
- اینترنت شما به شدت فیلتر است.
🚫
- تونل وصل می‌شود اما اتصال به سرعت قطع می‌گردد.
- سرعت برایتان نسبت به پایداری و اطمینان در درجه دوم اهمیت قرار دارد.
در شرایط زیر از
Fast
استفاده کنید:
- حالت Balanced در حال حاضر به خوبی کار می‌کند.
- سرعت بیشتری می‌خواهید.
⚡️
- شبکه یا سرور شما قوی است.
💪
تنظیمات پیشنهادی برای کاربران عادی
👥
اتصال هوشمند (Smart Connect):
On (روشن)
🟢
هدف (Goal):
Balanced
⚖️
موتور (Engine):
MasterDNS
🛠
پروکسی:
System proxy
🌐
سپس روی
Connect
کلیک کنید.
👆
اگر متصل نشد چه کار کنیم؟
🛠
این مراحل را به ترتیب امتحان کنید:
۱. هدف را به
Stable
تغییر دهید.
🛡
۲. گزینه Smart Connect را همچنان
On (روشن)
🟢
نگه دارید.
۳. دوباره روی
Connect
کلیک کنید.
۴. اگر باز هم متصل نشد، به بخش
Resolvers
بروید و یک اسکن اجرا کنید.
🔍
۵. بهترین نتایج Resolver را اعمال (Apply) کنید و سپس دوباره سعی کنید متصل شوید.
✅
برای کاربران تلگرام
💬
اگر از گزینه
SOCKS5 only
استفاده می‌کنید، پروکسی تلگرام دسکتاپ را به این شکل تنظیم کنید:
نوع (Type): SOCKS5
هاست (Host):
127.0.0.1
پورت (Port): 18000
نام کاربری/رمز عبور (Username/Password): خالی بگذارید
🔓
اگر از
System proxy
استفاده می‌کنید، مرورگرها معمولاً به‌طور خودکار متصل می‌شوند، اما تلگرام ممکن است همچنان به وارد کردن تنظیمات دستی SOCKS5 نیاز داشته باشد.
برای کاربران حرفه‌ای
🎓
اگر گزینه اتصال هوشمند را خاموش (
Off
) کنید، WhiteDns از پروفایل فعلی و تنظیمات پیشرفته‌ی (Advanced) شما دقیقاً همان‌طور که هستند استفاده خواهد کرد. این ویژگی برای زمانی که می‌خواهید کنترل کامل و دستی روی تنظیمات داشته باشید بسیار مفید است.
🔧
🚫
خیلی مهم :
به هیچ عنوان هیچ نرم افزار vpn دیگری مثل v2ray و یا ..... نباید روی سیستم شما باز باشد . مطمن شوید که حتی در پس زمینه هم بسته شوند
🚫
برای تست روی مرورگر ها حتما از گزینه New Private window یا New incognito window استفاده کنید
👍
@whitedns</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/whitedns/703" target="_blank">📅 07:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uq70jRUjYs7dpwdNcGcZmSwLKsKl6-bZQT5jkVjwVo4shU3KGebvmzMljy0z0nOe2WoLeFRF830yRDzYYrUyJY1o_sdb8hDs-mqKT25B2_EqR0i2zs6fsX_AW2tL69T_m98G2xQoqg17kw6cf28y_D_GDJVXRrjGas__FxohCNlFVZEpOkM_Y1nKMdbr8DHuLyO2-gjJHYOl37holiCO6fzbSr1qEw-AhejjsgYdoXGxpE7ZDOJ3mUOam_hj78xHFS-QTwBd-iHwDxJFLJoC0ZoiG_BFiw5q2sSKCMj6pcaJVchOoPhM-PF31QG75IMqSSAkn-bj4I8vvVKv2oZ9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در نسخه ۱.۰.۶ -
WhiteDns Windows
🪟
قابلیت
«اتصال هوشمند» (Smart Connect)
اضافه شده است؛ یک حالت اتصال خودکار جدید که به کاربران کمک می‌کند بدون نیاز به تغییر دستی تنظیمات در تب پیشرفته (Advanced)، به تنظیماتی پایدار و مطمئن دست پیدا کنند.
🚀
اکنون قابلیت اتصال هوشمند می‌تواند اتصال را بر اساس موتور (Engine) انتخاب‌شده، سرور، کیفیت تحلیلگر (Resolver) و نتایج موفق قبلی تنظیم و بهینه‌سازی کند.
⚙️
کاربران می‌توانند یک هدف ساده را انتخاب کنند:
پایدار (Stable)
🛡
متعادل (Balanced)
⚖️
سریع (Fast)
⚡️
. سپس برنامه پیش از برقراری ارتباط، به‌طور خودکار تنظیمات انتقال و تحلیلگر امن‌تری را برای MasterDNS یا StormDNS انتخاب می‌کند.
همچنین این نسخه نتایج موفق اتصال هوشمند را به تفکیک هر سرور، موتور و شبکه به خاطر می‌سپارد؛ در نتیجه اتصالات بعدی می‌توانند با استفاده از تنظیماتی که پیش‌تر جواب داده‌اند، سریع‌تر برقرار شوند.
🧠
اگر مسیر اتصال ضعیف باشد، قابلیت اتصال هوشمند پیش از نمایش پیام خطا، تنظیمات جایگزین امن‌تری (Fallback) را امتحان می‌کند.
🔄
صفحه اتصال (Connect) با یک پنل کنترل جدیدِ اتصال هوشمند به‌روزرسانی شده است، در حالی که امکان اتصال دستی معمولی همچنان برای کاربران حرفه‌ای در دسترس قرار دارد.
🛠
@whitedns</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/whitedns/702" target="_blank">📅 07:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-poll">
<h4>📊 با اپلیکیشن های ما تونستید به اینترنت متصل بشید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/whitedns/701" target="_blank">📅 05:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-700">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۸ اردیبهشت
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.5.0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygxKSIsInNlcnZlciI6eyJkb21haW4iOiJ2MS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygyKSIsInNlcnZlciI6eyJkb21haW4iOiJ2Mi5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygzKSIsInNlcnZlciI6eyJkb21haW4iOiJ2My5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg0KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg1KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg2KSIsInNlcnZlciI6eyJkb21haW4iOiJ2Ni5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg3KSIsInNlcnZlciI6eyJkb21haW4iOiJ2Ny5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg4KSIsInNlcnZlciI6eyJkb21haW4iOiJ2OC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg5KSIsInNlcnZlciI6eyJkb21haW4iOiJ2OS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygxMCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLm1hc2lyLXNlZmlkLm15IiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
⚡️
پک ریزالور
👍
تنظیمات مخصوص وایت دی ان اس
⬅️
نحوه ی اضافه کردن پروفایل ها
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/whitedns/700" target="_blank">📅 20:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-699">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/whitedns/699" target="_blank">📅 18:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-698">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای_جامع_استفاده_از_وایت_دی_ان_اس_ویندوز_.docx</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/whitedns/698" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
راهنمای جامع وایت دی‌ان‌اس (WhiteDns) برای ویندوز منتشر شد!
🚀
کاربران عزیز، اگر برای اتصال و تنظیم برنامه WhiteDns در ویندوز با چالشی مواجه هستید، این راهنمای کامل دقیقا برای شما آماده شده است. برنامه WhiteDns یک ابزار قدرتمند دسکتاپ برای تونلینگ و ساخت پروکسی محلی است و با استفاده از این راهنما می‌توانید بالاترین سرعت و پایداری را تجربه کنید.
📌
خلاصه‌ای از آنچه در این راهنما یاد می‌گیرید:
🔹
شروع سریع و آسان:
آموزش قدم‌به‌قدم ایجاد پروفایل، وارد کردن دامنه، کلید رمزنگاری (Encryption Key) و اتصال اولیه.
🔹
انتخاب حالت پروکسی:
تفاوت بین حالت دستی (SOCKS5 only) و اعمال پروکسی روی کل سیستم (System proxy) برای مرورگرها.
🔹
ابزار قدرتمند اسکنر (Resolvers):
آموزش پیدا کردن سریع‌ترین و پایدارترین تحلیلگرهای DNS با استفاده از اسکنر داخلی برنامه (در حالت‌های سریع، عمیق و با دقت بالا).
🔹
تنظیمات پیشرفته و موتورها:
معرفی تفاوت‌های موتور MasterDNS و StormDNS و نحوه استفاده از پروفایل‌های آماده (Presets) مانند
Stable Iran
(برای بالاترین پایداری در شبکه‌های محدود) تا حالت‌های تهاجمی‌تر (Aggressive).
🔹
تنظیمات مخصوص برنامه‌ها:
راهنمای دقیق ست کردن پروکسی محلی (
127.0.0.1:18000
) روی تلگرام دسکتاپ، فایرفاکس، کروم و مرورگر اج.
🔹
رفع مشکلات (Troubleshooting):
راهکارهای عملی برای حل مشکلاتی مثل وصل نشدن مرورگر با وجود اتصال برنامه، قطع شدن مداوم، و یا رفع گیر کردن روی راه‌اندازی کند تونل.
💡
فرمول طلایی اتصال:
بهترین و امن‌ترین مسیر برای اکثر کاربران این است: وارد کردن اطلاعات تونل
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای استفاده حرفه‌ای از این نرم‌افزار و دور زدن قطعی‌ها، حتماً فایل راهنمای کامل را مطالعه کنید.
#اموزش_ویندوز_whitedns
@whitedns</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/698" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-697">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تغییرات WhiteDns ویندوز نسخه 1.0.5
بازسازی رابط مدرن
بهبود جزئیات کوچک رابط کاربری و تراز کارت‌ها برای ظاهری تمیزتر و یکدست‌تر در دسکتاپ.
🖥
✨
اسکنر با دقت بالا :
یک اسکنر با دقت بالا برای شرایط سخت اضافه شد
طراحی شمارنده رزولور بهبود یافته
به‌روزرسانی استایل شمارنده رزولور تا با چیدمان کارت‌های اطراف هماهنگ‌تر شده و ظاهری مدرن‌تر داشته باشد.
🎨
پشتیبانی از سینی ویندوز بهبود یافته
رفتار سینی برنامه به‌روزرسانی شد تا در ویندوز طبیعی‌تر احساس شود و در پس‌زمینه در دسترس بماند.
🪟
🔌
فعالیت شبکه برای حالت SOCKS5 اصلاح شد
فعالیت شبکه اکنون ترافیک را زمانی که برنامه‌ها از پروکسی محلی SOCKS5 استفاده می‌کنند، ردیابی می‌کند، به جای نمایش فعالیت فقط از طریق مسیر HTTP/System Proxy.
🌐
🔍
سازگاری پورت SOCKS سفارشی
فعالیت شبکه اکنون هنگام تغییر پورت SOCKS در تب پیشرفته نیز به کار خود ادامه می‌دهد.
⚙️
حافظه اسکن رزولور اضافه شد
برنامه اکنون بهترین نتیجه اسکن رزولور را به خاطر می‌سپارد و اسکن‌های کامل تکراری را هنگام اتصال مجدد با مجموعه رزولور یکسان کاهش می‌دهد.
💾
🚀
تجربه اتصال مجدد سریع‌تر
اتصالات مجدد باید روان‌تر احساس شوند زیرا برنامه از اسکن مجدد غیرضروری رزولورها هنگام در دسترس بودن نتیجه معتبر قبلی خودداری می‌کند.
⚡️
وارد کردن دستی رزولور اضافه شد
گزینه وارد کردن .txt در کارت «وارد کردن / رزولورهای دستی» برای بارگذاری آسان‌تر لیست رزولورها اضافه شد.
📥
📝
نکات اتصال
از لیست رزولور باکیفیت و کوچک‌تر برای راه‌اندازی سریع‌تر استفاده کنید.
🚀
رزولورهای پایدارتر را در بالای لیست نگه دارید.
📌
هنگام آزمایش اتصال، ابتدا از حالت SOCKS5 استفاده کنید.
🧪
اگر حالت System Proxy با یک برنامه ناسازگار است، آن برنامه را به‌صورت دستی برای استفاده از
127.0.0.1
و پورت SOCKS نمایش داده شده در WhiteDns پیکربندی کنید.
⚙️
مگر در صورت نیاز، از تغییر مقادیر تونل پیشرفته خودداری کنید؛ مقادیر پیش‌فرض معمولاً پایدارترین هستند.
🛡
@whitedns</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/697" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-696">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برای اشتراک‌گذاری اتصال
WhiteDNS
روی وای‌فای با دستگاه‌های دیگر، کافی است داخل بخش تنظیمات، مقدار
Proxy Address
را از:
127.0.0.1
به این مقدار تغییر دهید:
0.0.0.0
بعد از انجام این تغییر، در بخش
Connection Info
یک آدرس IP جدید به شما نمایش داده می‌شود. از همان IP می‌توانید برای تنظیم پروکسی روی دستگاه‌های دیگری که به همان شبکه وای‌فای متصل هستند استفاده کنید.
لطفاً دقت کنید که برای اتصال دستگاه‌های دیگر، نباید از
127.0.0.1
استفاده کنید. باید حتماً از آدرس IP جدیدی که داخل
Connection Info
نمایش داده می‌شود استفاده شود.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/whitedns/696" target="_blank">📅 18:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-695">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پروژه‌ی TheFeed که متعلق به Sarto هست و قبلا درموردش حرف زدیم برای ios هم عرضه شد! میتونید با نصب برنامه‌ی Testflight در Appstore و رفتن به لینک زیر برنامه رو دانلود کنید:
https://testflight.apple.com/join/J6bfxDdZ
لینک کانال TheFeed
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/whitedns/695" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-694">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاوید نامان ایران(Bamdad)</strong></div>
<div class="tg-text">کانفیگ برای کلاینتهای وایت دی ان اس  بر روی اندروید، آی او اس، مک اوس، ویندوز و لینوکس
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDIiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5iYW1hay54eXoiLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDMiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5pcmRtYy5jb20iLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDQiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5qbmlyLm15IiwiZW5jcnlwdGlvbl9rZXkiOiJhYWY0YjYtQEphdmlkbmFtYW5JcmFuLWFhZjRiNmZmZiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5pZ29paS5vcmciLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDYiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5qYXZpZG5hbWFuLmNvbSIsImVuY3J5cHRpb25fa2V5IjoiYWFmNGI2LUBKYXZpZG5hbWFuSXJhbi1hYWY0YjZmZmYiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDEiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5uYW1hZC54eXoiLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/whitedns/694" target="_blank">📅 16:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-693">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه تشکر از کانال
https://t.me/Masir_Sefid
این دوستان عزیز از روز های اول شروع کردن به آموزش، تنظیمات و اشتراک گذاری سرور های رایگان برای اتصال رایگان.
اگر دوست دارید عضو چنلشون بشید و از آموزش، سرور و تنظیماتی که میذارن استفاده کنید.
ممنون از همه دوستانی که برای اتصال رایگان هموطن هامون تلاش میکنن
🫡
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/whitedns/693" target="_blank">📅 15:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-692">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">لیست ۱۰۰ ریزالور با بیشترین درخواست ها به سرور های WhiteDNS
185.94.98.34
185.142.158.162
5.160.128.142
2.189.44.68
93.115.127.9
109.230.89.90
217.219.162.200
94.232.173.28
134.255.206.205
80.75.7.2
185.208.174.167
185.37.55.30
185.51.201.58
185.53.142.174
185.255.91.60
185.88.178.196
164.138.17.122
78.157.41.60
5.202.252.30
31.214.169.244
185.109.61.27
2.188.21.58
185.213.11.85
178.252.128.66
2.188.21.70
185.105.101.1
2.189.44.98
109.107.159.86
77.238.123.179
2.188.21.46
172.64.32.0
173.245.58.0
151.232.36.4
108.162.192.0
185.208.175.228
185.137.25.146
185.208.183.29
207.211.215.145
185.50.37.52
2.188.21.138
109.230.206.175
2.189.44.14
85.185.1.10
46.32.31.30
109.72.197.1
2.189.44.84
2.189.44.82
80.191.163.249
2.189.44.86
2.189.44.83
2.189.44.85
78.39.234.140
85.185.157.181
37.191.95.70
185.191.79.210
185.141.105.139
74.80.77.247
78.38.174.2
74.63.24.210
74.63.24.211
2.189.44.93
185.53.141.230
2.189.44.94
74.80.77.246
2.189.44.91
2.189.44.92
2.189.44.90
2.188.21.146
172.253.228.147
74.63.24.205
172.253.12.151
172.253.12.155
172.253.228.150
172.253.228.145
172.253.12.16
172.253.13.147
172.253.13.146
172.253.13.156
172.253.13.154
172.253.13.152
172.253.13.149
172.253.228.156
78.38.114.66
172.253.12.221
172.253.12.150
172.253.13.157
172.253.12.154
172.253.12.210
172.253.13.145
172.253.13.148
172.253.12.212
172.253.13.151
172.253.12.216
172.253.228.148
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/692" target="_blank">📅 15:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-691">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">WhiteDNS-1.5.0-x86.apk</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/whitedns/691" target="_blank">📅 13:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-690">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستانی که تازه اضافه شدید، سوال دارید یا نمی‌دونید چطوری از WhiteDNS استفاده کنید، تمام مراحل زو اینجا براتون توضیح دادیم
https://t.me/whitedns_group/32380/32404</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/whitedns/690" target="_blank">📅 13:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-685">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/whitedns/685" target="_blank">📅 13:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-683">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqM1fp1pVg-fBYxexjeXL_DAb8mrS4eaK699gFHiGBq-_P-3uAujja-VBwnd49EjnfWO0YpMJ1zZpJ1VdBwYh7cBxppmwPRWZPN-MqIGHXZb7pOmH9LTgciax-LRKJ3FUtzns_N03pAVjPy17hC2qy7hm2cvxtL08uQZnHKnb4kufBEUdqidkSJ7lyENtuwjQPMyxOaUhvPLP_GkWmLPLpo2Pzkfr14WVT39W7ygyL9LmgT9I57fdkKf3YXdet0l1UdIB6SwBC4exBlw91dzHaCI3x7MylD21CiBduZVwVnz1BZNDu4eXXqpK7twDwESDuwwAMalVO-A2xTfS5eaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BP0tlMTwB_8qRCeua0tP_0FXvULCtkW85TivKnyb4ZLZwkCYhaZeuT2X-CymNuAE1IHRiHeUzjQDUyebexFdX_m5pXH4c92aELufs1M8966Op1ab3tZNRZtpnHkb7alYTB2Ia4wDXq3JiP6RzhHlqAI8aK3aoRi63Dem5yCGMpWrc1YTXdx9uKFsLnnL53E4q4FUJ9xeHAJqDUFyL_NyrsW5gK0ujtWWhPWbnHvvIjlG3R2E9BBs9B13TFLrAs6VEy8oOnNjfkpElTV0mJzC-eRC2rV63T4AUppNfU4RtmAchSEkYw6S2LUSTD1FVZkL2cFXQpfRKb7EcswxkDgbeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همراهان عزیز،
تمرکز در این نسخه روی زبان فارسی، دسترسی پذیری برای افراد با مشکلات بینایی، تست گروهی سرور ها و خروجی از ریزالور ها بوده.
✅
نسخه اپلیکیشن به 1.5.0 ارتقا پیدا کرده
✅
تست سرورها اضافه شده و می‌توانید سرعت، Ping و وضعیت سلامت همه سرورها یا هر سرور جداگانه را بررسی کنید
✅
نتیجه تست کنار هر پروفایل سرور نمایش داده می‌شود تا تشخیص سرورهای بهتر یا مشکل‌دار راحت‌تر باشد
✅
زبان فارسی به اپ اضافه شده و می‌توانید از داخل تنظیمات بین فارسی و انگلیسی جابه‌جا شوید
✅
چیدمان فارسی راست‌به‌چپ شده و فونت Vazirmatn برای خوانایی بهتر اضافه شده
✅
بخش‌های اصلی اپ مثل اتصال، پروفایل‌ها، اسکن، لاگ‌ها و تنظیمات فارسی‌سازی شده‌اند
✅
دسترس‌پذیری اپ برای TalkBack و صفحه‌خوان‌ها بهتر شده و دکمه‌ها، تب‌ها، اسلایدرها و کارت‌ها توضیح واضح‌تری دارند
✅
وارد کردن پروفایل با QR راحت‌تر شده
✅
خروجی گرفتن همه Resolverهای ذخیره‌شده در یک فایل اضافه شده و Resolverهای تکراری حذف می‌شوند
✅
تنظیمات Parallel Test مرتب‌تر شده و تنظیمات پایدار به‌صورت پیش‌فرض استفاده می‌شوند
✅
تنظیمات تهاجمی‌تر Parallel Test جدا شده‌اند و فقط در صورت فعال کردن استفاده می‌شوند
✅
نتیجه اسکن Resolver پایدارتر بروزرسانی می‌شود و پروفایل Scanner Result فقط بعد از پایان اسکن تغییر می‌کند
✅
پروفایل Default Resolver دیگر اشتباهی به‌عنوان پروفایل دستی ذخیره نمی‌شود
✅
وضعیت تست سرورها هنگام قطع اتصال یا خطا بهتر پاک می‌شود
ممنون از دانی عزیز برای تغییرات مربوط به زبان و دسترسی پذیری
❤️
در این ورژن تنظیمات جدیدی برای تست موازی MTU اضافه شده. دوستان عزیز که ابتدا مشکل داغ شدن گوشی موبایل داشتن، این گزینه رو بیارن پایینتر. مقدار حدود ۳۰ میتونه خوب باشه. اگر همچنان این مشکل رو داشتید مقدار های کمتر رو امتحان کنید.
همنین دوستانی که گوشی های مدل بالاتر دارند، میتونند مقدار های بالاتر رو تست کنند.
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/683" target="_blank">📅 13:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-682">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RRSweeFt4wR0QwQZNhEE7ZaqeWmHKWU0CZsy3u8KDUV8HM_J_6voZL4nroxHXS2OpUQ5uBZs4Cy395rLgcFRucqkGdgDALxlSbJzieTQDRPNYUQsVzq5-txn4Zhlu5Z-Pd9MTam4LqguN4sk9XZ-cbw5_fGLbC4wAoxVBzkWa4-up0PpGk0wrZ3B28oy0upu-JV1a42KNaAsWszRZKOLoJ1UDSuzeeD8cIRGcLL9BEImkbI9XJimQKGTiWzJ3KSfzqgSZ8k7tMfGBwY2GCik-G54rlMyDj3idAoiiZuhgtagJwy3kJoF0VyqWLKT_j_ClJBmwlqShYqgBm0ryV3X7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ اندروید
#چشم_عقاب
نه فقط یه خبرخوان، بلکه یه راه آفلاین برای دسترسی آزاد به اطلاعاته، که بدون اینترنت، بدون VPN و حتی بدون داشتن مجوز اینترنت روی گوشی، خبرها و اطلاعات رو مستقیما از ماهواره روی دستگاه شما میاره.
کافیه کانالش رو روی فرکانس 10762/27500V ماهواره ترکمن‌عالم باز کنین و دوربین گوشی رو سمت کدهای QR که روی صفحه نمایش داده میشن بگیرید، تا اپ در چند ثانیه اطلاعات رو بخونه و روی گوشی ذخیره کنه.
اپ فقط به دوربین دسترسی داره تا QR Codeها رو اسکن کنه و هیچ عکس یا ویدئویی ذخیره یا ارسال نمی‌کنه. تمام محتواهایی که دریافت می‌کنین، قبل از پخش با امضای رمزنگاری‌شده Ed25519 تأیید میشن تا اپ فقط اطلاعات واقعی و معتبر رو قبول کنه.
👉
play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/whitedns/682" target="_blank">📅 12:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-681">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from3rf4n vpn(3rf4n)</strong></div>
<div class="tg-text">سرور white dns متصل چنل
✅
Domain :
v.phtv1.lol
Key :
2ff051858125055a6999b91c515d19ef
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQHp5cGhlcnZwbnNhbGxlIiwic2VydmVyIjp7ImRvbWFpbiI6InYucGh0djEubG9sIiwiZW5jcnlwdGlvbl9rZXkiOiIyZmYwNTE4NTgxMjUwNTVhNjk5OWI5MWM1MTVkMTllZiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/681" target="_blank">📅 10:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-680">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
سرور وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۸ اردیبهشت
Domin Vip :
vip.masir-sefid.my
Domin 1:
v1.masir-sefid.my
Domin 2:
v2.masir-sefid.my
Domin 3:
v3.masir-sefid.my
Domin 4:
v4.masir-sefid.my
Domin 5:
v5.masir-sefid.my
Key :
Telegram-Channel--->@Masir_Sefid
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.4.0
1️⃣
WhiteDNS
(Windows)
1.0.5
⚡️
پک ریزالور
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
اگه وصل شدین ری اکشن برید بدونم
❤️
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/whitedns/680" target="_blank">📅 09:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-679">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=NuYXyJw0u8CqluqlEcVn9CfS_hxlOexciMhLNM6SRkPpwekc-og4rUzMSRXYZoKCHy8v90cAZqPIe0L4Ta_KguMgV74bY-DvyPFiB6srE683KAMiAM3AzI7oLwsWwdjSRjvauSy90J_rRKu_W7Z9UWXgbywYxtkVy1vitD7qHXvw77Q9fkMA2rvvJ_fd2m2mNzYmeCXWMP-PdMss0HNQa-Ijnwelv4e9Aeq4KiC4Yc_W0Xm14j-fdGIPLO6WIPajYqKViq8Oer0VHCmGH5i9f7sUOPtUFev-cSP1BpZRY_cz4WTerdNaY8UmJiVDUNYIdWpT74dzbNHIdk7Ulu_J-A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=NuYXyJw0u8CqluqlEcVn9CfS_hxlOexciMhLNM6SRkPpwekc-og4rUzMSRXYZoKCHy8v90cAZqPIe0L4Ta_KguMgV74bY-DvyPFiB6srE683KAMiAM3AzI7oLwsWwdjSRjvauSy90J_rRKu_W7Z9UWXgbywYxtkVy1vitD7qHXvw77Q9fkMA2rvvJ_fd2m2mNzYmeCXWMP-PdMss0HNQa-Ijnwelv4e9Aeq4KiC4Yc_W0Xm14j-fdGIPLO6WIPajYqKViq8Oer0VHCmGH5i9f7sUOPtUFev-cSP1BpZRY_cz4WTerdNaY8UmJiVDUNYIdWpT74dzbNHIdk7Ulu_J-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.wdn.best
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
@WhiteDNS</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/whitedns/679" target="_blank">📅 07:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-678">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIOFz7-Oyj53UB9lXDCyBAl5-vrlmHyRbl0VfKUqMueAAEI40Xb54t8xYtjODuvz4c2g6-smmmOX2H10mEQy3l5geeanJvEZPWS4Rt0shEx1BDldV06u_QlnXDqA5WBCBYDVeovewQkzPfD6bf5kDWL12c00AgPeqC4jMjmznmcDXfzSprQQ6cTzt0kWLkDx8qaloNnqDcU8AY7Zfp-1Dyg0_aNGE7r6u5GEl1u2tuRZGXSlQQ2qkgzdTFXLIy8DbciL59OsvL8GDKRWIz0bVCHREom7R2tMolPpfRinSnwg51ani3EBFpd_8aG5bFSxo16pqymn8bNzJLII5UO01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه بعدی WhiteDNS با ترجمه کامل تمام متن‌ها به زبان فارسی منتشر خواهد شد.
همچنین در این نسخه، دسترسی‌پذیری اپلیکیشن برای افرادی که از اسکرین‌ریدر استفاده می‌کنند و کاربران دارای معلولیت‌های جسمی به شکل کامل‌تر و بهتر بهبود داده شده است.
ممنون از دنی عزیز برای PR</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/whitedns/678" target="_blank">📅 07:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-677">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/677" target="_blank">📅 06:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-676">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFXSWOUEOfryoiEyfVsSGN7AqQMNtTlZ20SatJCdzVyfIIDv-Hg1zWkaWAcyRTquYYrXjQJLl6mvIYGkGOia196zwjpD1zq7UrASiQ02sNWq7Eb_9YjG4M7jpefwYZuBNMyZA_skZZ8aO1yHQ3TIhLBuAhNzKOCNqQhlp1JebFSw-8RY6GeV7Esew-giT01Vikln0DuJsKhElQ0LUTCwQ7XnZLPgTUXwb-gbzaVsmWA_nH0mqwuzvvp4dZ0Wwy0HmI5SjpfoxeKnTUtpbTdAIzc_35K9Z30aA9l7lrE1ZW-WsvEqr6_TYoFIDGhy6EUzTKZDVHgpYYAQ27FidaOUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/whitedns/676" target="_blank">📅 06:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-675">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">WhiteDNS
❌
WaitDNS
✅</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/whitedns/675" target="_blank">📅 04:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-673">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
سرور وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۷ اردیبهشت
Domin Vip :
vip.masir-sefid-3.shop
Domin 1:
v1.masir-sefid-3.shop
Domin 2:
v2.masir-sefid-3.shop
Domin 3:
v3.masir-sefid-3.shop
Domin 4:
v4.masir-sefid-3.shop
Domin 5:
v5.masir-sefid-3.shop
Key :
Telegram-Channel--->@Masir_Sefid
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.4.0
1️⃣
WhiteDNS
(Windows)
1.0.5
⚡️
پک ریزالور
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
اگه وصل شدین ری اکشن برید بدونم
❤️
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/whitedns/673" target="_blank">📅 17:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-672">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">☄️
WhiteDNS Premium Configs For StormDNS
☄️
😀
کانفیگ‌های اختصاصی، پایدار و قدرتمند
🚀
مناسب برای اتصال سریع، امن و بدون اختلال
📡
Optimized For Better Stability & Performance
🎁
کانفیگ اهدایی از طرف چنل:
@PersiaTMChannel
01.
🌐
Domain:
b1.persiatmx.us
🔑
Encryption Key:
843996e318d85f34a012240b24714d2f
━━━━━━━━━━━━━━━━━━
02.
🌐
Domain:
b2.persiatmx.us
🔑
Encryption Key:
6b51dfc5f065436a03f76f76af4c7416
━━━━━━━━━━━━━━━━━━
03.
🌐
Domain:
b3.persiatmx.us
🔑
Encryption Key:
2bee92b7342be563851a6f8da0090de4
━━━━━━━━━━━━━━━━━━
04.
🌐
Domain:
b4.persiatmx.us
🔑
Encryption Key:
9f9709ec0bb9c380227237e9ef7c9f3c
━━━━━━━━━━━━━━━━━━
05.
🌐
Domain:
b5.persiatmx.us
🔑
Encryption Key:
962f409687cf0069080d5aef96cccbdc
━━━━━━━━━━━━━━━━━━
06.
🌐
Domain:
b6.persiatmx.us
🔑
Encryption Key:
428c0d303605cefb06f7c33123484ac5
━━━━━━━━━━━━━━━━━━
07.
🌐
Domain:
b7.persiatmx.us
🔑
Encryption Key:
3ac7935006ba328616a5df2aef1ed8fd
━━━━━━━━━━━━━━━━━━
08.
🌐
Domain:
b8.persiatmx.us
🔑
Encryption Key:
6aecaa4877f463a773ab364560815f27
━━━━━━━━━━━━━━━━━━
09.
🌐
Domain:
b9.persiatmx.us
🔑
Encryption Key:
7f3aad92ab16b630fc2d0c7e8469c278
━━━━━━━━━━━━━━━━━━
10.
🌐
Domain:
b10.persiatmx.us
🔑
Encryption Key:
7fb2856813f16fe683a4483bb6ae0f71
Special Thanks To
🤝
@WhiteDNS
Channel
⭐️
StormDNS Project
For Their Support & Contribution.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/whitedns/672" target="_blank">📅 15:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-671">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/whitedns/671" target="_blank">📅 14:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-670">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=uIGdXh2IGR0N4Oh-aHZZfQOL-AAjJ0fOAH4IPx5pBZDXI57s9CVTzRl9a5V0vQL-_Gp18k1HM9WxrRfVpFVW2Rt_nSGFxHHZ4VKBm_9RLqcYvjmow2vH7gePNxaF3kReJD0NkmOGgnAfNSQrXhDt-LPfjqfVFETRZCU6A5Uc3sh3r3LC1EpjkmPBmvmJpICGxwUxk4b9almgrmKtqTJLgSyHDLgdxxMH_mUz2Pa49qo3tPjnvdwk4moQKcANVTldRTKrQqdU0Clw2TYSlX_zZ5xnjYdkZoOTuO73jb0Bh--2XZG4Qa-bMtEHv5_kGPS8qROuBcn9sao845Myti1Ahg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=uIGdXh2IGR0N4Oh-aHZZfQOL-AAjJ0fOAH4IPx5pBZDXI57s9CVTzRl9a5V0vQL-_Gp18k1HM9WxrRfVpFVW2Rt_nSGFxHHZ4VKBm_9RLqcYvjmow2vH7gePNxaF3kReJD0NkmOGgnAfNSQrXhDt-LPfjqfVFETRZCU6A5Uc3sh3r3LC1EpjkmPBmvmJpICGxwUxk4b9almgrmKtqTJLgSyHDLgdxxMH_mUz2Pa49qo3tPjnvdwk4moQKcANVTldRTKrQqdU0Clw2TYSlX_zZ5xnjYdkZoOTuO73jb0Bh--2XZG4Qa-bMtEHv5_kGPS8qROuBcn9sao845Myti1Ahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.store
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/whitedns/670" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-669">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
🙌
WhiteDNS یک پروژه غیرانتفاعی و رایگان است که برای کمک به دسترسی آزادتر کاربران ایرانی به اینترنت فعالیت می‌کند.
حمایت مالی شما کمک می‌کند این پروژه زنده بماند، سرورهای بیشتری راه‌اندازی شود و افراد بیشتری در ایران بتوانند به اینترنت آزاد متصل شوند.
هیچ اجباری برای کمک مالی وجود ندارد.
تمام حمایت‌ها فقط صرف هزینه‌های سرور، زیرساخت، توسعه و نگهداری پروژه WhiteDNS خواهد شد.
ممنون از اعتماد و همراهی شما
🙏
🤍
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/whitedns/669" target="_blank">📅 10:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-668">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">لیست ۱۰۰ ریزالوری که در ۲۴ ساعت گذشته به سرورهای WhiteDNS متصل شده‌اند:
185.142.158.162
185.255.91.60
94.232.173.28
217.219.162.200
185.53.142.174
134.255.206.206
185.51.201.58
134.255.206.205
5.202.252.30
109.230.89.90
31.214.169.244
93.115.127.9
185.88.178.196
185.208.174.167
185.37.55.30
80.75.7.2
164.138.17.122
5.160.128.142
158.58.184.147
2.189.44.68
2.188.21.58
185.109.61.27
185.50.37.52
5.236.93.157
185.137.25.146
109.230.206.175
178.252.128.66
185.208.175.228
2.186.121.65
2.188.21.70
78.157.41.60
2.188.21.46
108.162.192.0
173.245.58.0
172.64.32.0
46.209.209.209
207.211.215.145
185.141.105.139
78.39.234.140
37.191.95.70
2.189.44.98
2.188.21.138
185.208.183.29
80.191.163.249
5.160.140.16
46.32.31.30
2.189.44.94
2.189.44.91
5.160.227.78
2.189.44.90
2.189.44.92
2.189.44.93
74.80.77.246
66.185.123.244
109.72.197.1
89.32.197.226
85.185.157.181
185.141.106.238
2.188.21.62
74.80.77.247
78.38.174.2
74.63.24.205
74.63.24.206
172.253.12.221
172.253.13.149
172.253.228.150
77.104.104.104
172.253.228.147
172.253.13.147
172.253.13.146
172.253.228.145
172.253.12.210
172.253.13.156
172.253.13.154
172.253.12.216
172.253.12.154
172.253.12.151
172.253.228.152
172.253.13.157
172.253.13.148
172.253.13.152
172.253.13.144
172.253.13.153
85.133.167.108
172.253.228.156
172.253.228.149
74.63.24.210
172.253.13.151
172.253.228.154
172.253.228.151
172.232.181.197
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/whitedns/668" target="_blank">📅 09:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-667">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/whitedns/667" target="_blank">📅 09:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-666">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">full user-facing guide .txt</div>
  <div class="tg-doc-extra">18.6 KB</div>
</div>
<a href="https://t.me/whitedns/666" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
Quick Guide to WhiteDns for Windows!
🚀
Struggling to connect? Here is the absolute easiest way to set up WhiteDns for maximum speed and stability:
🛠
🔹
1. Basic Setup:
Create a profile and enter your Tunnel Domain and Encryption Key.
📝
🔹
2. Find the Best Connection:
Go to the "Resolvers" tab, run a quick scan, and apply the top-ranked resolver to your tunnel.
📡
🔹
3. Ultimate Stability:
Use the
MasterDNS
engine and select the
Stable Iran
preset for the most reliable experience on restricted networks.
🛡
🔹
4. Choose Proxy Mode:
Use
System proxy
to automatically route traffic for browsers like Chrome and Edge, or choose
SOCKS5 only
(
127.0.0.1:18000
) for manual configuration in apps like Telegram or Firefox.
⚙️
💡
The Golden Formula:
Enter details
➡️
Scan Resolvers
➡️
Apply Best Resolver
➡️
Choose 'Stable Iran'
➡️
Connect!
🏆
Check out the full attached guide below for step-by-step instructions and troubleshooting!
📚
@whitedns</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/whitedns/666" target="_blank">📅 09:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-665">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
The Comprehensive WhiteDns Guide for Windows is Out!
🚀
Dear users,
if you are facing any challenges connecting and configuring the WhiteDns app on Windows, this complete guide is made exactly for you. WhiteDns is a powerful desktop tool for tunneling and creating local proxies, and with this guide, you can experience the highest speed and stability.
📌
A quick summary of what you'll learn in this guide:
🔹
Quick & Easy Start:
Step-by-step tutorial on creating a profile, entering your domain, encryption key, and making the initial connection.
🔹
Choosing the Proxy Mode:
Understanding the difference between manual mode (SOCKS5 only) and applying the proxy to the entire system (System proxy) for browsers.
🔹
Powerful Scanner Tool (Resolvers):
How to find the fastest and most stable DNS resolvers using the app's built-in scanner across Quick, Deep, Advanced, and High Accuracy modes.
🔹
Advanced Settings & Engines:
Explaining the differences between the MasterDNS and StormDNS engines, and how to use Presets like
Stable Iran
(for maximum stability on restricted networks) up to Aggressive modes.
🔹
App-Specific Configurations:
Detailed instructions on setting up the local proxy (
127.0.0.1:18000
) on Telegram Desktop, Firefox, Chrome, and Edge.
🔹
Troubleshooting:
Practical solutions for common issues like browsers not connecting despite an active app connection, frequent disconnections, or slow tunnel startup.
💡
The Golden Formula for Connection:
The best and safest route for most users is: Set tunnel details
⬅️
Scan resolvers
⬅️
Apply the best resolver
⬅️
Use Stable Iran preset
⬅️
Connect!
@whitedns</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/whitedns/665" target="_blank">📅 08:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-664">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای_جامع_استفاده_از_وایت_دی_ان_اس_ویندوز_.docx</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/whitedns/664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
راهنمای جامع وایت دی‌ان‌اس (WhiteDns) برای ویندوز منتشر شد!
🚀
کاربران عزیز، اگر برای اتصال و تنظیم برنامه WhiteDns در ویندوز با چالشی مواجه هستید، این راهنمای کامل دقیقا برای شما آماده شده است. برنامه WhiteDns یک ابزار قدرتمند دسکتاپ برای تونلینگ و ساخت پروکسی محلی است و با استفاده از این راهنما می‌توانید بالاترین سرعت و پایداری را تجربه کنید.
📌
خلاصه‌ای از آنچه در این راهنما یاد می‌گیرید:
🔹
شروع سریع و آسان:
آموزش قدم‌به‌قدم ایجاد پروفایل، وارد کردن دامنه، کلید رمزنگاری (Encryption Key) و اتصال اولیه.
🔹
انتخاب حالت پروکسی:
تفاوت بین حالت دستی (SOCKS5 only) و اعمال پروکسی روی کل سیستم (System proxy) برای مرورگرها.
🔹
ابزار قدرتمند اسکنر (Resolvers):
آموزش پیدا کردن سریع‌ترین و پایدارترین تحلیلگرهای DNS با استفاده از اسکنر داخلی برنامه (در حالت‌های سریع، عمیق و با دقت بالا).
🔹
تنظیمات پیشرفته و موتورها:
معرفی تفاوت‌های موتور MasterDNS و StormDNS و نحوه استفاده از پروفایل‌های آماده (Presets) مانند
Stable Iran
(برای بالاترین پایداری در شبکه‌های محدود) تا حالت‌های تهاجمی‌تر (Aggressive).
🔹
تنظیمات مخصوص برنامه‌ها:
راهنمای دقیق ست کردن پروکسی محلی (
127.0.0.1:18000
) روی تلگرام دسکتاپ، فایرفاکس، کروم و مرورگر اج.
🔹
رفع مشکلات (Troubleshooting):
راهکارهای عملی برای حل مشکلاتی مثل وصل نشدن مرورگر با وجود اتصال برنامه، قطع شدن مداوم، و یا رفع گیر کردن روی راه‌اندازی کند تونل.
💡
فرمول طلایی اتصال:
بهترین و امن‌ترین مسیر برای اکثر کاربران این است: وارد کردن اطلاعات تونل
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای استفاده حرفه‌ای از این نرم‌افزار و دور زدن قطعی‌ها، حتماً فایل راهنمای کامل را مطالعه کنید.
#اموزش_ویندوز_whitedns
@whitedns</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/whitedns/664" target="_blank">📅 08:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-663">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/whitedns/663" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای صوتی برای whitedns windows v1.0.5
🚀
راهنمای سریع وایت دی‌ان‌اس (WhiteDns) برای ویندوز!
🚀
برای اتصال سریع و پایدار، این ساده‌ترین روش تنظیم برنامه است:
🔹
۱. تنظیمات اولیه:
یک پروفایل در تب Tunnel بسازید و آدرس دامنه (Domain) و کلید رمزنگاری (Encryption Key) خود را وارد کنید.
🔹
۲. یافتن بهترین اتصال:
به تب Resolvers بروید، یک اسکن سریع (Quick) انجام دهید و با انتخاب گزینه "Apply top to tunnel"، بهترین تحلیلگر را روی تونل اعمال کنید.
🔹
۳. بالاترین پایداری:
در تب Advanced، موتور
MasterDNS
را انتخاب کرده و برای داشتن اتصالی بدون قطعی در شبکه‌های محدود، حالت
Stable Iran
را فعال کنید.
🔹
۴. انتخاب پروکسی:
برای استفاده خودکار در مرورگرهایی مثل کروم و اج از حالت
System proxy
استفاده کنید. برای تنظیم دستی در تلگرام یا فایرفاکس، حالت
SOCKS5 only
(آدرس
127.0.0.1:18000
) را انتخاب کنید.
💡
فرمول طلایی:
وارد کردن اطلاعات
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای آموزش قدم‌به‌قدم و رفع هرگونه مشکل، فایل راهنمای کامل را در زیر مطالعه کنید.
👇
@whitedns</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/whitedns/663" target="_blank">📅 08:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-662">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aNdvWO4Q6oRmeNC1p0c4o1r_y301F906VzBVpgqX2c_0gkDQWHtzkPb7NOz1eriQl49GqHS6R1imKn43tEPxoVu2juO2zClYOVil01F8OJct9ppgyqwCW5mqFsx75L5baE6fVBnTRtpXMTkWvTASz84rLjnhxBMv4qeENpZ1cMUBb7K8gjS67HvRdkJhqwv1OOLi86GXBaMqhQB-Gdi3NMmpotdcFWN_JLslJ0P5OhBzbg2CIBPE8qYeNiFJssqVxqcKYY-N3KVl_p3kgNRDS8Gx_mr59VthuUd6ImsSiZN6lhDTnfVIEHInoq0TBrBh1QlZ2C2vTqHxFLR7K4xPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش جامع WhiteDns Windows</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/662" target="_blank">📅 08:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-661">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستان گرامی :
🤝
حتما در گروه اصلی whitedns عضو شوید تا راحت‌تر به آخرین مطالب دسترسی داشته باشید
🚀
سپاس
🙏
آدرس گروه اصلی :
@whitedns_group
📲</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/661" target="_blank">📅 06:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-660">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/660" target="_blank">📅 06:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-659">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تغییرات WhiteDns ویندوز نسخه 1.0.5
بازسازی رابط مدرن
بهبود جزئیات کوچک رابط کاربری و تراز کارت‌ها برای ظاهری تمیزتر و یکدست‌تر در دسکتاپ.
🖥
✨
اسکنر با دقت بالا :
یک اسکنر با دقت بالا برای شرایط سخت اضافه شد
طراحی شمارنده رزولور بهبود یافته
به‌روزرسانی استایل شمارنده رزولور تا با چیدمان کارت‌های اطراف هماهنگ‌تر شده و ظاهری مدرن‌تر داشته باشد.
🎨
پشتیبانی از سینی ویندوز بهبود یافته
رفتار سینی برنامه به‌روزرسانی شد تا در ویندوز طبیعی‌تر احساس شود و در پس‌زمینه در دسترس بماند.
🪟
🔌
فعالیت شبکه برای حالت SOCKS5 اصلاح شد
فعالیت شبکه اکنون ترافیک را زمانی که برنامه‌ها از پروکسی محلی SOCKS5 استفاده می‌کنند، ردیابی می‌کند، به جای نمایش فعالیت فقط از طریق مسیر HTTP/System Proxy.
🌐
🔍
سازگاری پورت SOCKS سفارشی
فعالیت شبکه اکنون هنگام تغییر پورت SOCKS در تب پیشرفته نیز به کار خود ادامه می‌دهد.
⚙️
حافظه اسکن رزولور اضافه شد
برنامه اکنون بهترین نتیجه اسکن رزولور را به خاطر می‌سپارد و اسکن‌های کامل تکراری را هنگام اتصال مجدد با مجموعه رزولور یکسان کاهش می‌دهد.
💾
🚀
تجربه اتصال مجدد سریع‌تر
اتصالات مجدد باید روان‌تر احساس شوند زیرا برنامه از اسکن مجدد غیرضروری رزولورها هنگام در دسترس بودن نتیجه معتبر قبلی خودداری می‌کند.
⚡️
وارد کردن دستی رزولور اضافه شد
گزینه وارد کردن .txt در کارت «وارد کردن / رزولورهای دستی» برای بارگذاری آسان‌تر لیست رزولورها اضافه شد.
📥
📝
نکات اتصال
از لیست رزولور باکیفیت و کوچک‌تر برای راه‌اندازی سریع‌تر استفاده کنید.
🚀
رزولورهای پایدارتر را در بالای لیست نگه دارید.
📌
هنگام آزمایش اتصال، ابتدا از حالت SOCKS5 استفاده کنید.
🧪
اگر حالت System Proxy با یک برنامه ناسازگار است، آن برنامه را به‌صورت دستی برای استفاده از
127.0.0.1
و پورت SOCKS نمایش داده شده در WhiteDns پیکربندی کنید.
⚙️
مگر در صورت نیاز، از تغییر مقادیر تونل پیشرفته خودداری کنید؛ مقادیر پیش‌فرض معمولاً پایدارترین هستند.
🛡
@whitedns</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/whitedns/659" target="_blank">📅 06:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-658">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tgpLl4_8I00A59HF_-l9WeJWhyLLmDjQ_elJx39T4CSHnvcL0j0p4gdkz7niIHw_JL4iPiyvw6L3YxjJ-FlqnEfswczhYPNSmqismDJ8knHbbwFIE_UyiFxWlUnXdhTeXAxZvwRSnuPStoqZSO0XWFIMuL_-vk4mlunF2i_hA9lLer5nFCA9K8OMkDOQwqp-9cbCtlznCnSjlpPtus14hxa2pqTu7QHJGqCaADpm1z4lwp6uCZH3lfU7IHf7zY6s44MiWwWU_MrcYvFx4JETBeZp3tbD93nPBQGsdJM6Wbxc65X1BLoiOxmsXJP21CARyY_ZCVdHm6b0ecN4zt2N2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/whitedns/658" target="_blank">📅 06:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-657">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">DNSForge-Guide-Persian.pdf</div>
  <div class="tg-doc-extra">79.4 KB</div>
</div>
<a href="https://t.me/whitedns/657" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش گام به گام و متنی برای اتصال به نسخه‌ی ios برنامه‌ی WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/whitedns/657" target="_blank">📅 22:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-656">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🙂
نسخه آزمایشی اپلیکیشن iOS تیم WhiteDNS برای تست اتصال‌های MasterDNS و فورک StormDNS آماده شده است.
برای استفاده، ابتدا باید اپلیکیشن TestFlight را روی دستگاه خود نصب کنید، بعد از طریق لینک زیر وارد نسخه آزمایشی شوید:
https://testflight.apple.com/join/GfUqXrFz
⚠️
لطفاً توجه داشته باشید که این نسخه آزمایشی است و ممکن است هنوز باگ یا ناپایداری داشته باشد.
@WhiteDNS</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/whitedns/656" target="_blank">📅 22:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-655">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-text">📱
آموزش کار با برنامه دفید (Thefeed):
برای دریافت آخرین نسخه و کانفیگ‌ها، به کانال زیر بروید و برنامه را نصب‌ کنید و لینک کانفیگ را کپی کنید:
@thefeedconfig
ورود به برنامه:
۱. برنامه را باز کنید و زبان را انتخاب نمایید.
۲. در قسمت مشخص شده (thefeed://...)، کانفیگ کپی شده را وارد کرده و دکمه «وارد کردن» را بزنید تا ثبت شود.
عملکرد برنامه:
پس از وارد کردن اولین کانفیگ، برنامه ریزالورهای موجود در کانفیگ را بررسی کرده (چند دقیقه طول میکشد) و سپس لیست کانال‌ها را دریافت می‌کند. شما می‌توانید کانال‌ها را باز کرده، پست‌ها را مشاهده و عکس، ویدیو، ویس و فایل‌ها را دانلود کنید.
نکته:
لیست کانال‌ها فقط توسط سازنده کانفیگ قابل تغییر است. (جلو تر یک‌روش دیگر برای کانال های دلخواه شما نیز نوشته ام)
افزودن کانفیگ جدید:
در صفحه اصلی با زدن دکمه + می‌توانید کانفیگ جدید وارد کنید یا کانفیگ‌های موجود دیگر را فعال نمایید.
🛠️
بخش ریزالور ها:
در این بخش می‌توانید ریزالورها را مدیریت کنید. دکمه‌ای به نام «بانک ریزالور» وجود دارد که لیست کامل را نمایش می‌دهد. همچنین یک لیست فعال به نام Default وجود دارد که پس از بررسی اولیه، ریزالورهای فعال را در خود نگه می‌دارد. شما می‌توانید برای اینترنت‌های مختلف، لیست‌های فعال متفاوتی داشته باشید. و با زدن دکمه «بررسی مجدد»، می‌توانید از بانک ریزالور فعال برای اینترنت خود را پیدا کرده و به لیست جدید اضافه کنید.
🔍
بخش پیدا کردن ریزالور:
این بخش بسیار مهم است. با استفاده از یک لیست پیش‌فرض ۵۰ هزارتایی، می‌توانید ریزالورهایی که برای اینترنت شما کار می‌کنند را پیدا کنید (زمانی که سرعت برنامه کم شده بود و یا کار‌ نمی‌کرد).
روش کار:
۱. وارد بخش شوید.
۲. دکمه بارگذاری لیست پیش‌فرض را بزنید.
۳. دکمه شروع اسکن را بزنید.
۴. برنامه شروع به پیدا کردن می‌کند. وقتی حدود ۱۰ تا ریزالور پیدا شد، توقف را بزنید و سپس دکمه «افزودن به لیست فعال» را بزنید.
*توجه:* حتماً باید VPN خاموش باشد.
📺
بخش کانال‌های دلخواه (teleMirror):
این بخش کاملاً از قسمت‌های قبلی جداست و مکانیزم متفاوتی دارد. این بخش از طریق سرویس‌های گوگل، پیام و عکس کانال‌های عمومی تلگرام را می‌آورد و نمایش می‌دهد.
*محدودیت‌ها:* این بخش نمی‌تواند ویدیو پخش کند یا فایل دانلود کند (به خاطر محدودیت‌های گوگل). همچنین برخی کانال‌های عمومی اجازه اشتراک‌گذاری در سایت را نمی‌دهند، و پست هایشان در این قسمت نمایش داده نمی‌شود.
نکته مهم:
این بخش فقط زمانی کار می‌کند که گوگل در دسترس باشد. اگر گوگل مسدود شود، فقط قسمت اصلی برنامه (معرفی شده در اول پست) کار خواهد کرد. همچنین سرویس‌های گوگل محدودیت تعداد درخواست دارند که ممکن است شما را محدود کنند.
🔔
برای اخبار پروژه حتما کانال اصلی را دنبال کنید:
@networkti</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/655" target="_blank">📅 22:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-654">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.18.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/whitedns/654" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید TheFeed (v0.18.10)
🚀
🔸
توی این نسخه چیز مهمی تغییر نکرده! فقط از اونجایی که گیتهاب اکانتم رو ساسپند کرد و هنوز اکانت باز نشده، پروژه TheFeed رو به گیتلب منتقل کردم و برنامه رو هم تغییر دادم که لینک ها و این چیزهای که توی برنامه بود به گیتلب هم اشاره کنه. البته قابلیت دانلود آخرین نسخه و نوتیف نسخه جدید هنوز به گیتلب وصل نشده و کار‌نمیکنن (گیتلب فیلتره و کمکی نمیکنه اضافه کردنش
🫠
).
البته توی تنظیمات یک دکمه هست به اسم "بررسی" که وقتی بزنیدش اخرین شماره نسخه رو از سرور میپرسه و نشون میده، این رو سمت سرور تغییر دادم که اگر‌ گیتهاب کار نکرد اخرین شماره نسخه رو از گیتلب بگیره و سمت کلاینت هم یک باگ داشت که رفع شد.
⚠️
این نسخه خیلی مهم نیست و میتونید آپدیت نکنید
آدرس سورس کد پروژه روی گیتلب:
https://gitlab.com/sartoopjj/thefeed
یک نفر لطف کرده بود و فیچر های دسترسی پذیری اضافه کرده بود و پول ریکوئست فرستاده بود، لطفا اگر این پیام رو میبینی مرج ریکویست بفرست روی گیتلب
🥲
❤️
کانال اصلیم:
@networkti
کانال کانفیگ برای برنامه:
@thefeedconfig</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/whitedns/654" target="_blank">📅 22:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/whitedns/653" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">WhiteDns-Windows-Setup.exe</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/whitedns/652" target="_blank">📅 09:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">White DNS
pinned «
⚠️
اعلان مهم
📢
تمام تبلیغاتی
📰
که در این کانال قرار می‌گیرند، هیچ ارتباطی با ما ندارند
🚫
و ما هیچ‌گونه مسئولیتی در قبال محتوای آگهی‌ها، معاملات، خرید و فروش، یا هر نوع کلاهبرداری احتمالی
🎭
قبول نمی‌کنیم.  دلیلش ساده است: ما هیچ کنترلی روی تبلیغات ارسال‌شده…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/651" target="_blank">📅 07:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-650">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚠️
اعلان مهم
📢
تمام تبلیغاتی
📰
که در این کانال قرار می‌گیرند، هیچ ارتباطی با ما ندارند
🚫
و ما هیچ‌گونه مسئولیتی در قبال محتوای آگهی‌ها، معاملات، خرید و فروش، یا هر نوع کلاهبرداری احتمالی
🎭
قبول نمی‌کنیم.
دلیلش ساده است: ما هیچ کنترلی روی تبلیغات ارسال‌شده نداریم
🤷‍♂️
. این تبلیغات به صورت خودکار توسط خود تلگرام در کانال گذاشته می‌شوند
🤖
مسئولیت هرگونه تعامل، پرداخت یا ارتباط با آگهی‌دهنده، کاملاً بر عهده خود کاربران
👥
است
@whitedns</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/whitedns/650" target="_blank">📅 07:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-649">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.2 MB</div>
</div>
<a href="https://t.me/whitedns/649" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه 1.0.3
یک آپدیت متمرکز بر پایداری است. در این نسخه پایداری اتصال بهتر شده، مپ شدن تنظیمات Advanced اصلاح شده، تفاوت بین SOCKS5 و System Proxy شفاف‌تر شده، و احتمال حالتی که برنامه Connected باشد ولی سایت‌ها باز نشوند کمتر شده است.
WhiteDns Windows v1.0.3
- راهنمای سریع تست
لطفا برای تست اول این تنظیمات را استفاده کنید:
1. برنامه را باز کنید.
2. وارد بخش Connect شوید.
3. گزینه Proxy Mode را روی System proxy بگذارید.
4. وارد بخش Advanced شوید.
5. گزینه Transport preset را روی Balanced بگذارید.
6. این موارد را بررسی کنید:
- Compression = off
- Base64-encode data = Off
- DNS listener enabled = Off
- SOCKS5 authentication = Off
- Packet duplication = 0
7. در صورت نیاز ذخیره کنید و سپس Connect بزنید.
اگر سایت ها ناپایدار بودند یا باز نشدند:
- فقط همین یک مورد را تغییر دهید:
- Transport preset = Stable Iran
لطفا این موارد را گزارش کنید:
- آیا اتصال با موفقیت انجام شد؟
- آیا یوتیوب و سایت های عادی باز شدند؟
- از چه Proxy Mode استفاده کردید؟
- سرعت مرور مناسب بود یا نه؟
- آیا برنامه یا سایتی بود که با وجود Connected بودن کار نکند؟
@whitedns</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/whitedns/649" target="_blank">📅 07:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-648">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ilYV5AZ-TlA9Butgjtvvs_TS3_39EIY7tASsNT9pXbbSQJnp3QS1I_GsWFBTQ4R1J6dTEN_OTwT8X96a1JolASxQwmAHCqwX4vbCoFhhSdLu6yUc8iwobwvTCjySUm_1TQw-HSDA-ceCjuAll4BdFY_jIb4oWWJ5GWJ434pC88xWDn9dJbxJRhPtDnTK8DXsFD7N-j4Nx7T-8YXmJougdcXIXyPhdU9Qjaet8K9F3MB6zu4uDDmeXD-OsvmS6CielL4KRvxfH5iiYay0cWvrQsGT0Exk0-jM7AVXpfM-NeUwCnAJ7hKfb9EHUwCSYGUKc-zNRXWjXKh5Yc-cZ5eaxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/whitedns/648" target="_blank">📅 07:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-647">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/whitedns/647" target="_blank">📅 04:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-646">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSOS Iran Connect</strong></div>
<div class="tg-text">🔶
خبرهای خوب:
۱. عبدالکریم، دوست بلوچ ما، تونست اپلیکیشن WhiteDNS را با کار تیمی دوستان راه بندازه
و وصل بشه
🎉
🗣
صدای خودشون، ۱۴۰۵.۰۲.۲۶، ۰۱:۵۲ ایران
۲. من داستان عبدالکریم روشندل را به Pedi جان در
@WhiteDNS
منتقل کردم، و دو درخواست مطرح کردم:
الف. داشتن رابط کاربری (user interface) پارسی در اپلیکیشن WhiteDNS.
ب. افزودن راهنمای پارسی به گیت‌هاب پروژه برای استفاده روشندلان با کمک ScreenReader.
ایشون از ایده‌ها استقبال کرد، ولی به زمان نیاز دارند.
⚪️
هدف دلی ما اینه که کاربرها خودکفا و مستقل باشند.
🫂
#همدلی
#ایران
💛
@WhiteDNS
🆔
@SOSIranConnect</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/646" target="_blank">📅 03:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-645">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/whitedns/645" target="_blank">📅 01:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-643">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=P_N-YrXbgxXZRwH7DWeLNSv0GZpxbJ8gbVjAvAniQETpld-drWTMw91XQYO5x1fYsJd7untM2NCvxLMQneraAvHTLWBh0MoUn4srm0fAu4ED29gUt16kNbSYFnsmWhqu26dqlOJDEdXQtQ4t4dcC3MUpj0Y7fLxWXTyo0t010im1SJaYOK1Ajdqoi69vgmL1QCXjmpkVRqOigv_LHiPhJaOdS_R8Eb30LLdjRmWunzd-mLFPGuw6DXAEuQN97mF-GsUa-1l_tzNseOA1Wy-O9j8tMzLwdFCn7ja6QhFjoU2F1ON8FmLVvXS6tY_lAGYOecPv5bkCA-ZmX2Y5Wnmeumq0gIxhfLYEhDteKePD6QGjBNUT6aWy9rfdF6udK3BJic6T2ZeAni_z2_MEGPIjaMflCWkS_kjx6HCb2QqyllBoPRG9IdKBQMrYX8mCUp_jTjFPFDFRP2F7dFvcz4hik8VtKDiU9FJrkvyQsjIbip5a9CfQp8MnuZliCHffUnSWmiWbNBlZNV6HttQGZHGtoLHJpvgFKvTAxP6LdonmAApLyaj3lJNanDTJuXeUptH3nlnT_hAkBcHaI9iHX8TrbVuex0tejhyMsOfT3KUOwj6L2dfTZ1-sbDszweVJvRjZgak4kEcbSc_7BSnw8W_DJiIxsgxuAGmt2P1uzQTU5Qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=P_N-YrXbgxXZRwH7DWeLNSv0GZpxbJ8gbVjAvAniQETpld-drWTMw91XQYO5x1fYsJd7untM2NCvxLMQneraAvHTLWBh0MoUn4srm0fAu4ED29gUt16kNbSYFnsmWhqu26dqlOJDEdXQtQ4t4dcC3MUpj0Y7fLxWXTyo0t010im1SJaYOK1Ajdqoi69vgmL1QCXjmpkVRqOigv_LHiPhJaOdS_R8Eb30LLdjRmWunzd-mLFPGuw6DXAEuQN97mF-GsUa-1l_tzNseOA1Wy-O9j8tMzLwdFCn7ja6QhFjoU2F1ON8FmLVvXS6tY_lAGYOecPv5bkCA-ZmX2Y5Wnmeumq0gIxhfLYEhDteKePD6QGjBNUT6aWy9rfdF6udK3BJic6T2ZeAni_z2_MEGPIjaMflCWkS_kjx6HCb2QqyllBoPRG9IdKBQMrYX8mCUp_jTjFPFDFRP2F7dFvcz4hik8VtKDiU9FJrkvyQsjIbip5a9CfQp8MnuZliCHffUnSWmiWbNBlZNV6HttQGZHGtoLHJpvgFKvTAxP6LdonmAApLyaj3lJNanDTJuXeUptH3nlnT_hAkBcHaI9iHX8TrbVuex0tejhyMsOfT3KUOwj6L2dfTZ1-sbDszweVJvRjZgak4kEcbSc_7BSnw8W_DJiIxsgxuAGmt2P1uzQTU5Qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
دور زدن فیلترینگ با کانفیگ سرورلس با ترکیب nekobox و v2rayng
•
✅
لینک کانفیگ nekobox
•
https://pastebin.com/raw/rWeHKSt3
•
✅
لینک داخلی کانفیگ nekobox
•
https://seup.shop/t/exks1
•
✅
لینک کانفیگ V2rayNg
•
https://pastebin.com/raw/Yfymhyy5
•
✅
لینک داخلی کانفیگ‌ V2rayNg
•
https://seup.shop/t/k9mmj
❗️
هر دو کلاینت رو، رو حالتvpnبزارید .
📥
لینک داخلی ویدیوها
•
🎥
https://seup.shop/f/uns5
•
🎥
https://seup.shop/f/v4jx
•
𝕏 Irvictorious
kian
•
@ConfigWireguard
💎
•
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/whitedns/643" target="_blank">📅 19:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-642">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">White DNS
pinned «
💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/642" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-641">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/whitedns/641" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-639">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">لیست ۱۰۰ ریزالور که طول ۲۴ ساعت گذشته به سرور های WhiteDNS وصل شدند
185.94.98.34
2.189.44.68
185.44.36.216
185.137.25.146
94.232.173.28
185.142.158.162
217.219.162.200
185.88.178.196
178.252.143.130
134.255.206.206
80.75.7.2
134.255.206.205
185.53.142.174
89.32.197.226
185.37.55.30
77.238.111.234
31.214.169.244
80.71.149.62
185.109.61.27
62.60.197.83
185.88.178.177
178.252.128.66
158.58.184.147
5.202.252.30
74.63.24.205
74.63.24.211
216.147.121.134
74.63.24.210
46.209.209.209
217.66.203.211
74.80.77.246
80.191.221.26
2.189.44.98
216.147.121.98
164.138.17.122
207.211.215.145
151.232.36.4
185.208.175.228
2.188.21.58
108.162.192.0
172.64.32.0
80.191.163.249
173.245.58.0
78.39.234.140
185.208.183.29
2.188.21.138
2.188.21.70
2.188.21.46
185.255.91.60
66.185.123.243
2.189.44.85
2.189.44.82
2.189.44.83
2.189.44.86
2.189.44.84
2.189.44.14
74.80.77.247
109.107.159.45
2.189.44.92
2.189.44.94
2.189.44.91
2.189.44.93
2.189.44.90
78.157.41.60
193.178.200.3
46.32.31.30
185.208.174.167
85.185.157.181
77.238.123.179
185.141.105.139
5.160.140.16
5.160.227.78
185.53.141.230
185.105.101.1
37.255.223.218
85.133.129.242
78.38.174.2
37.191.95.70
74.80.77.244
74.80.77.245
93.118.109.213
194.61.120.143
121.127.46.65
93.126.5.205
5.160.137.130
2.180.21.241
82.114.164.226
@WhiteDNS</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/whitedns/639" target="_blank">📅 16:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-636">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سرور اهدایی از رسول عزیز از تیم وایت دی ان اس
Name: H3 (Germany)
Domain:
v.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Serbia
Domain:
v3.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Turkey
Domain:
v4.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: USA
Domain:
v5.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Switzerland
Domain:
v6.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: RMFT g1-7
Domain:
g1-7.rmft.tech
Encryption Key:
a337e9fa75161c44bebe7d717da36afc</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/whitedns/636" target="_blank">📅 12:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-635">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سرور اهدایی از چنل
@Masir_Sefid
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
Name:
@Masir_Sefid
🕊
(1)
Domain:
v1.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(2)
Domain:
v2.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(3)
Domain:
v3.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Name:
@Masir_Sefid
🕊
(4)
Domain:
v4.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(5)
Domain:
v5.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/whitedns/635" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-633">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
Domain:
v2.abolfazlshahi.cloud
Key:
965a568dccef58af7afb86e8ee55eea6
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/whitedns/633" target="_blank">📅 12:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-631">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSwsluREBRVUlXiPRp0fWdrVCGoS5cQOtd0m_HjLkmdCBJvCh4pZ7zVlog9JpE4Ni6BNimKQl_7HBJOXvYjV89I1Q9WtGfBDsI0Nzj0NS4B7yPjQNSZiGoqrIAmsTOHnokcaxDQg1reODvRiOeLeNsJ3L-jPyUoEpUP8NRKcwfLI5dfVkegkLey67y8ysxoW83zXjA1Rj6_riJMGwoG8293H1BcqWNNz_ZKLS6RShGHltTbg9gKXNQ0XRsWUUTxbPuX3sUDirG99NqogsE_-h3T_OyLA51Mga8VgTcwfKgZxTEun4fIIMOMZNIAlfpPBMtGxeJQvwWzdwTKqU9Qe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkP5XxnU28sQhKuaru58h96MIVuE8Uh22pmRVPYHvCFtaii6ANrEUK_bzgfWR28UXyAAdIIiL907n5oM-5NSrY3bOxAFz6xiIraINAryNjm0nG2CtOmE-iUGdFWfZCHpbtIM4SaLV0IeWkEY1oc3wtZBRtnYHqZkJ3Jczorr0iwulM7m-s6ahxFS7lM_dh7RE6c2HEdnmMAPVjG-i33xeD5PgBGFJ5vSKOArPZ6rYioR5bZrVfE1kd2YpOc8DowtlOC4MM9HLb0eu9naXYjmuY3fPmaFX1txqcQPiW8RhPJ3DPdwAYVvGZJftdTb-csJUk1aKvxVUU37dS5mb6V49Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درحال حاضر نزدیک ۱۰۰۰ نفر فقط به سرور ما متصل هستند. سرور تا نزدیک ۲۴۰۰ نفر میتونه کاربر بدون افت کیفیت رو پشتیبانی کنه.
جدا از سرور های ما، سرور های اهدایی باقی چنل ها مثل مسیر سفید هم هست. ویدیو آموزش سرور اختصاصی هم پست های بالاتر گذاشتیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/whitedns/631" target="_blank">📅 11:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-630">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=jHYbnWt3dHUs65gaR8sqhHyNCKzlBo9P8lqxLEVt2Neh_hF1SH9JBi5qI1C9yHWO-Kqiexi4qyt2kYvcHUBwpsDSdjz8JB-4VsDk0VM-Gp6Z5fXTgrBMhHg66jfd25yb_E0ncEWD80cNvPS2ozLhJUsyXj5FKaMdZMBbxEcoiwEG_2ZFsw7nFcCfMzuo2AOgNrSqO_tIPy1-IgFV7kS-zw_JBFjxFstnTOIhlxyncrU0EYGiodZEKIAXyLQJ3pbOpdy2jG7bDKZUjmjfV8r1caapFt7yYdTFwq-OxPEA8AJyA3EO8ZYBi9svVkO7C3k8dAZIG8jRCAXqbMrZe8qNRw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=jHYbnWt3dHUs65gaR8sqhHyNCKzlBo9P8lqxLEVt2Neh_hF1SH9JBi5qI1C9yHWO-Kqiexi4qyt2kYvcHUBwpsDSdjz8JB-4VsDk0VM-Gp6Z5fXTgrBMhHg66jfd25yb_E0ncEWD80cNvPS2ozLhJUsyXj5FKaMdZMBbxEcoiwEG_2ZFsw7nFcCfMzuo2AOgNrSqO_tIPy1-IgFV7kS-zw_JBFjxFstnTOIhlxyncrU0EYGiodZEKIAXyLQJ3pbOpdy2jG7bDKZUjmjfV8r1caapFt7yYdTFwq-OxPEA8AJyA3EO8ZYBi9svVkO7C3k8dAZIG8jRCAXqbMrZe8qNRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.site
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/whitedns/630" target="_blank">📅 11:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-625">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.3 MB</div>
</div>
<a href="https://t.me/whitedns/625" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان  نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/whitedns/625" target="_blank">📅 11:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-624">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYSvuY7eV02Bjfq73hjTP1M4S660YevarQUoE5IEK0bwbyyeFh94hcTxugSDoVeP87JsfsizR8Wucb0IaHLUn_BePzTFs9Pxzel_edx5eFOhUEgNu1SyHtXmnvY_Vexp2bxQpoMZc7HJ7-DYWwtOF2_uzNe2BB59-DkTMrLs4SFeh15pFHIyfSApoY9jIwTSv5kvkBDd4-GTuOco1Mfx-hn7jG7t-19eS4Rgb45jJ2nF8vgRGsE59OQ4R9YE9jcCRI1ge_hEtqE7twxYZ2jJhrHwgf57qiionyqfbEjpX2lzD2IJdB7hnetJyRVB_NNspwXh171yfzPvPTFE5YN_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
تمرکز اصلی این نسخه روی ساده‌تر شدن اتصال و پیدا کردن بهترین تنظیم برای هر کاربر بوده است. هدف این بود که WhiteDNS قبل از اتصال، چند کانفیگ مختلف را با Parallel Test بررسی کند، بهترین گزینه را از نظر سرعت و کیفیت انتخاب کند، و کاربران بدون نیاز به گشتن دنبال Resolver، با لیست پیش‌فرض ۴۵۰۰+ Resolver داخل اپ سریع‌تر اسکن کنند و راحت‌تر وصل شوند.
تغییرات این نسخه
:
✅
نسخه اپلیکیشن به 1.4.0 ارتقا پیدا کرده
✅
قابلیت Parallel Test برای تست هم‌زمان چند تنظیم مختلف قبل از اتصال اضافه شده
✅
حالا WhiteDNS می‌تواند قبل از اتصال، چند حالت اتصال را هم‌زمان بررسی کند
✅
اپ سرعت و Ping هر تنظیم را تست می‌کند و بهترین گزینه را برای همان اتصال انتخاب می‌کند
✅
قابلیت Parallel Test هم برای Proxy Mode و هم برای Full VPN قابل استفاده است
✅
در حالت Full VPN، اپ اول بهترین تنظیم را با Parallel Test پیدا می‌کند و بعد اتصال VPN نهایی را روشن می‌کند
✅
نتایج Parallel Test بعد از اتصال داخل صفحه اصلی نمایش داده می‌شود
✅
می‌توانید تنظیم موفق Parallel Test را با نام دلخواه ذخیره کنید
✅
چند تنظیم آماده WhiteDNS برای تست سریع اضافه شده
✅
می‌توانید پروفایل‌های تنظیمات پیشرفته خودتان را هم وارد Parallel Test کنید
✅
بیش از 4500 Resolver داخل اپ قرار گرفته تا برای اسکن و اتصال راحت‌تر استفاده شود
✅
لیست Resolver پیش‌فرض داخل اپ کامل‌تر شده
✅
پروفایل Default Resolver اضافه شده تا اپ همیشه یک لیست آماده Resolver داشته باشد
✅
امکان اسکن مستقیم لیست Resolver پیش‌فرض اضافه شده
✅
اسکن فایل‌های بزرگ Resolver سبک‌تر و بهتر انجام می‌شود
✅
ریزالورهای تکراری یا قبلاً پیدا‌شده بهتر کنار گذاشته می‌شوند
✅
شمارش Resolverهای سالم و ردشده در اسکن دقیق‌تر شده
✅
اگر پروفایل اسکن سرور یا کلید نداشته باشد، اپ واضح‌تر جلوی شروع اسکن را می‌گیرد
✅
ویرایش سرور، Resolver و تنظیمات از صفحه اصلی راحت‌تر شده
✅
امکان حذف پروفایل‌های اتصال تکراری اضافه شده
✅
پروفایل Default Resolver از حذف یا جابه‌جایی اشتباهی محافظت می‌شود
✅
هشدار باتری حالا قابل بستن است
✅
نمایش سرعت، مصرف اینترنت و آمار اتصال دقیق‌تر شده
✅
تنظیمات پیشرفته برای اتصال‌های کندتر و مسیرهای سنگین‌تر بهتر تنظیم شده
✅
وارد کردن و خروجی گرفتن فایل‌های TOML با گزینه‌های جدید کامل‌تر شده
✅
هسته داخلی StormDNS به‌روزرسانی شده
تنظیماتی که به صورت اتوماتیک انتخاب میشوند، تمرکز روی سرعت و کیفیت دارد. امکان افزایش مصرف اینترنت شما با کانفیگ انتخاب شده می‌باشد. اگر نگران این موضوع هستید تنظیمات را مرور کرده و مقدار  Upload Dup را کمتر کنید.
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/whitedns/624" target="_blank">📅 11:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-623">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeNsQc7lcs0GzweYSwrtsmNUyhNdc-aTGgGFkvs726LgZsLYdF0fZf4b2xrLffXom0-gZYgmM045wA4cKpUPcrV204TIX744hnQVryxed_GTB8BdiFhugJjxmaQhQP8kG3MMyAwnK67dN0LAOCMXyO9p9kTpfEbB0ijFpUIsan9u9VbHX3wxmS8ZT-my3R9iL7HCHVEuDnJhKYJ0GB2AnBR_uHuY_teudTOWiyTXZzerlcnSsG-Aikuhh1Xju_sT8NCS7zZStzz4G_vd224r6B7PuB1iJgNH0sq_sMJqIOuUQJWkwmB7xTGosD8D6GX1WhKsil9gh1R6ZxyuV7Dt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن ۱.۴.۰ کلاینت اندروید WhiteDNS به‌زودی منتشر می‌شود. در این نسخه سعی کردیم کار شما را راحت‌تر کنیم و اتصال سریع‌تر و ساده‌تر انجام شود.
در این ورژن، اپ به‌صورت خودکار ۷ تنظیم مختلف را با قابلیت Parallel Test بررسی می‌کند و در نهایت بهترین کانفیگ را از نظر سرعت و کیفیت برای شما انتخاب می‌کند.
همچنین بیش از ۴۵۰۰ Resolver که قبلاً داخل بات و گروه منتشر شده بود، به‌عنوان لیست پیش‌فرض داخل اپ قرار گرفته است تا بدون نیاز به گشتن دنبال لیست، بتوانید مستقیم اسکن را شروع کنید و راحت‌تر وصل شوید.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/whitedns/623" target="_blank">📅 10:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-622">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kc7gguV24G3zrFFVQXpBu0jpKXAfm6j-Z-dJhkrunMkNI5BwtAt30DJk2Pq197szYK21zpcmsf8DHVWrjuxmqTqXddVHSDYzfOElyF0NmONJPN4Ufc4Fd-baU5aUQjts7creDs8hrw4kMeJxe3uzo-MvEwYP11oACpxB3edp-InOZ4RYXQRRHDyjqh2Ycc-0Vg8zn9ezmzOW9NX2Z_4A9YIg-gq8AHf9kd3h58T_gkCNHkc0fjnQOgs7WBfB8MWNOqTEDpP67-QnUXulKrIbeefdGRCJmPUsR1z8nxeehe40oM0hNPiSVSn3C2nUP7SXdFpm4ZZgvMn6LIjXpiFDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.space
Encryption Key:
bad99364093861634030e96f11fe3132
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
این بزرگترین سرور ما هستش. ۱۲ هسته سی‌پی‌يو و ۲۴ گیگ رم.
✈️
هر مشکلی هست، از سمت اختلال شبکه، تنظیمات و ریزالور ها هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/622" target="_blank">📅 07:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-620">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">StormDNS-Setup-Guide.mp4</div>
  <div class="tg-doc-extra">151.4 MB</div>
</div>
<a href="https://t.me/whitedns/620" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دوستان عزیز سلام
یک فیلم آموزشی آماده کردم برای نحوه راه‌اندازی سرور شخصی StormDNS/MasterDNS
دانلود سرور داخلی
https://guardts.ir/f/3c4216b2ea16
✍️
آموزش متنی
پیش‌نیاز:‌ تهیه سرور و دامنه خارج از ایران
1️⃣
آماده‌سازی DNS
ابتدا یک ساب‌دامین کوتاه بسازید و آن را به نیم‌سروری وصل کنید که به IP سرور شما اشاره می‌کند.
مثال:
ns.example.com  A   1.2.3.4
v.example.com   NS  ns.example.com
توضیح:
ns.example.com
باید به IP سرور شما وصل باشد.
v.example.com
باید به عنوان Subdomain Delegation به
ns.example.com
اشاره کند.
یعنی تمام درخواست‌های DNS مربوط به
v.example.com
به سرور شما ارسال می‌شود. اینترنت هم بالاخره یک جایی باید بفهمد با خودش چند چند است.
2️⃣
نصب سرور
روی سرور لینوکسی خود، دستور زیر را اجرا کنید:
bash <(curl -Ls https://raw.githubusercontent.com/nullroute1970/StormDNS/main/server_linux_install.sh)
بعد از نصب و اجرای سرور، برنامه به صورت خودکار کلید رمزنگاری فعال را نمایش می‌دهد.
همچنین این کلید داخل فایل زیر ذخیره می‌شود:
encrypt_key.txt
برای مشاهده کلید می‌توانید از دستور زیر استفاده کنید:
cat encrypt_key.txt
3️⃣
موارد موردنیاز برای اتصال کلاینت
بعد از راه‌اندازی، برای ساخت پروفایل یا اتصال کلاینت معمولاً به این اطلاعات نیاز دارید:
Domain: v.example.com
Encryption Key: مقدار داخل encrypt_key.txt
Server IP: 1.2.3.4
لینک داخلی:
https://guardts.ir/f/3c4216b2ea16
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/whitedns/620" target="_blank">📅 03:18 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
