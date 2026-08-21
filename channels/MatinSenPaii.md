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
<img src="https://cdn1.telesco.pe/file/QsCYNQB0g-KvIPXXy8uETbRX5ghsIoFykoXF2PqU3hpq7J7a0Q4QBksIytqF3x6EJwlr-qpltKdLbUSHkJiZ6wxGdSglhUc0IPxDx0H0QnGcNipm0wqaZPjqLAkOWNuKIZAJ2R30ajwWDlW0JAUduUkyCGbjZVVoVcpzN3htjh3BmBI6h8OZKn5AJtH3-to57XLTv6VgeUga_iMSbDRjMmAV7ywyhg7gBxcbmiXBIEQ_MnnrjD1jz9vo-YFMWu225zww1fhLOV3_7C4lJPh7SovP2T68tk9JLkOiK_v3yUVngMpDpgle1li9m4YX4QygKXaUs0HgOuQa_hocVhdSJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 06:57:27</div>
<hr>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lBZfo6dltEpCUvwMa3lYQU0phKNvOIlxB9IlxHV-CZqQw2yrSvzlXJuQUq3DGPYVjb6OQw7rAjGPJBLEldxYj53ELwNFKPKH2bBs030VznipHDiQfSit2GfQDnp8JSogic7MK-dOQOyjfkbutpF6x5a3XZnafD1aUsYqlWlQD3zfGpxJ8n85vb19vxQIOfQqRcgTIK9br3e3PF7No8AKJO6yWUenV-fPEA4dxQNBlCeYW1WKQwuk_RYtAUjyfzXVCAtPBE99vkjC6QKv1kCR5lDi-DUM8c4vPRz4tMzR_dWK9_bA_hPse23O9jBg6oOyJzT1AsM-EflIgfsDYqC-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4ysICUOUeykw-0jEJmyEB_qSNu8rkP94UuNUfar3_a6HI8ZARW_5mOe5gRwiPXFMZ9afkH9rVRymbYEAeplBc9ygTnbGJG4lISr6Q0JrSdz5e-hBFD_IvnmuErZOUoWhP6-ioBDEXL780MzArVuxJlaIphIRr_JaxBfOWKDCGuDrMIuAUERFMWc1TLX4jPMNvWkQ4ztwsqc05yLUx5gKm1HPXpRzIdtYCDM5kwPHPl-rbItKafIwfIiI-nLshToxcoREmDhURIMj1UQfjV1-ATn8oujAUv77HYEsr3zMPwbq7gLB_DOUj8fYRWOKyLSgU-4fE8z8CINdQqHiDyPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب هرمس وب یوآی با یک کلیک
متین سنپای
بهم گفت که Hermes WebUi نصبش سخته و بهتره با یک کلیک بشه نصبش کرد برای همین روی پروژه اصلی PR زدم که اگر تایید بشه از این به بعد میتونید راحت این پنل رو نصب کنید و ازش استفاده کنید.
لینک PR:
https://github.com/nesquena/hermes-webui/pull/7152
میتونید روش ری اکت بدید شاید تاثیری داشته باشه.
اگر هم تایید نکردن مهم نیست
یک پروژه جدید روی گیت هاب خودم اوردم بالا
لینک پروژه:
https://github.com/nesquena/hermes-webui
میتونید به هرمس بدید و بگید براتون نصبش کنه
خیلی ساده همون پروژه اصلی رو میاد براتون نصب میکنه
حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RGt6DEBJm8YTTiJLddgyhjjcPwbIfyrGVvn3QP-HlLYUJ0fdlodlDFrwzzd6rj0W8QrYBH6ZlCkk5AhUPPu4qUfciREFeMj99Iby1finGQDlL3ZnY6DyhSSCTOnBOVtYdWjc5OQL5I0ofjgh7kDqG7FKydHo8jHQpuGN9kcgghJdmbCvfHP75LslwpmUO-b7p_43Y-PVBKtCW0EClFYnA75hE09-f6tzRStUsG7T5epcIAA2mSR_jQraXSZMjOstGKTQwOBKBVV2XDLKxusRMQaxqtWoGEAb28SJmRV62ukdg8uh_V2kk5nGZIB2FvvpLcXaDTyXxvLAK0B2pNpg9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QHN7xmoDqlez_w_yFJub06zUWZJY8O0qehpDf0C99RmkPQwmKg81IMlJ1zJjNdJMhbE9P2_DX2QrzfruC2sM_6OMLD-9-5EPKmq-Y2nbvuALkCp4qXAdbeo6Pt4L1-_T3NU3h2iP6doYKoz49_GgsMyblgo2LwUJF-ceyr_rN5OBB1cDyBja91RP2HfJGZXvQDBpEK5RQjqQ1dQBI7m95nEi8_DXdSB4AixkC48uJU3n_ZNeioJuhC3QCvDEw6Ea7lvN-9Jr0b55yESFJe2jZKZogWFbTNFxG9qy6t9VtCFD_q_qdqxAxcRebdEORBc7SaLBTS6IJVw4MDzAaKcJAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NwluWy6z5TOR8eXIAeMJ3Q1J-J-SC4BgEJWE1aD3VjKQmczodnwuS0qpYnk5jyjynglw3-JtOMNUBCqB5OWia28v0cE8pLXsSncXTICNAy2PY1miuzBmMdDH8k9SBKf6CmBotcntaFSXTHsTKPjT869w-m36dDT0C6ifOGCxwuiQPrfOg1T1GMGxkVTMe8SkS6eSwTA2zAL54RAgunyabNFbZ8uU2ohcGuitJu-kviSGWpy4Hx1HOno_xx2jZSzF71sMv0c_vIJ-a4MWeNwYGfHSfvY5d2pI-X-ohW9NNSuwupiwxJzsL3Z8YSxmUtdJ7wIDegUNmugOZA1kNznDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس استریم شخصی هم نوشتم واسه خودم که با نت داخلی بیام روی Kick
(تانل rathole
😂
)
هاهاها
به من خندیدین؟
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CbptO3KAF3f_atYNSfUnT6d5t-XTUCRuvPpunsl9qr8-x1cL2X7FCVXhMklfZHOQTk2QSfvpF0nfgtMoFG9zxbGPJhdz7-czdA4GArhP_LxSJpdgFAQx_472KlaTS-QONIfiu7zT_laRugiF_Ec5KFNjCKwMITLi4BcQnYhPI0IrzSJjpA9IwRdPPllQoSVF-scbHkRiea7b_rKWsl4FDVGTKI2vuGCtM9lY-RRfCaQZMcY36ZqjfF5tueRs0qv3ipCyOzosF5y7IWiaa8WSh9T2y0Z7YFVE6CDn_rY1W605GYoZ8eMVIueswRc0tpNf2-t8F_x9DmucqVT-HuHr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJNUXDeji-UsWH1Z6EDs33Fy9ezOAGB9va41tEk5GrowR3DI1SKYpHlbhZ31O1mlNAGPUXNIUxNHZFnrHLUuJuPlpGkvXLqFv41yKLyv8B4OFHO32qTswtqkHwI_vN8WwTOE38ck0b_V3D4zFAcxQGXCV-wOxlYkhfNWJlcCvXNLOSSaEbXnWPb7bib0Ifv7elFLLPovfJFVqD3X667_XMdCkmN2gRl7SkfUWY4JBaJJh-87tGvuZeZt7tEF5BZuFkpKaNLsZHFcbKlh6_V6yHufEwkW1UnTSPcQu6hT5gxv-JOsBPOrmujgbJNVjOwFOu2CnmNtGB5djzvmOlZAxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lDY-nuC97Ad83MfD5S6P0rXs4m5PcVSefUIU1flYq7eni2IY_koFMRIYMxjxHT_bzLIRWkeEjp2yEKPh07hisaCQBIAuvCwEM4NiTxIF8eq1ExzhUrjeI3hpPrLVRwMhUf5V1aXIV_piEyaOwWiyGkzTsF-RKArjHb7xf3xhNxIeNHzJTjs_Pvxv0ynCO1_ZTyX11iUUiIc7_4nOMuBYJJ64clAONwxwhr1ioLG2NqxfPJAjWY0mZSIxNwiZ3eyKhjT46ltjVyY_uwJyLtj1I5T7xdsbwBDWxXFA40V7N4bXW9orhvqy986rwkyBy9J3SiF6DxDwt4NL8MP-a9BUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dsSjRYrIDgHuLecuwUpW7t3cF5D89Mi94OtUuE-7GoMGDS1MDnU6546SO5HwySIuzGnbGi9828AmxTTej31yE2_2vLKSikUAFHFHRwF993nFy9ot-czHTbZD3wckrDYq6xKFE59BDvwDyUv-_GkIE9ydExk9tXjTg-jQQ7OGUEiDYJfRnWFiIkKRaGLzapZ-sG5_--jZrsqy11z_gjyiQaLkAzVrZJePDYxtjaYtl8dfNA7mq6ORrBOoquAYrjPG2D5aMy403wZM7F8XKnaDFeuAYKlWihDItQ4ktbNHRmSN-rQ194fvE7798PteXicM58pNlZYnMaWtfODcNjvpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ4TioiGSpwSzne2rGoWnMg3FRSkxZrm31GKfqOMdWqtSwl8U2wf7lEsxZcYZDAbVXUZwUeXSV6SE399ttBQBmg_XHsBZmn5zv92HhCggeItF9OvBcxqk1WiHWNwfaQJzE0jhXzeqrXY3v8fl9XuoxjrGhIHVwHEQo5PBKurH3w4d1a34zwgVPXBdB8J4VuuKIQbcxRwe7LC6-oWUfDLxDkEcfO8ObFlRD7jsV5Pd7dfPht0MRJLx0H73imdJKukTTP4QN5Ho1qAamk7xaeT-o9fYCjcFDwH9wjbWPddWZGWWMS4-mJpwKlVAwNFK1gldKTQeckNkoiaxfaCAGwLAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MVmX3HA42vL6Co36Tq21BKqomkc83eQt2HipOHylHgS56bO-tPKcPaECNkGlXKwx7T87rkK5Hx9DioYw8Q3BRAZwMg4Sd-k2cJvBP3vEgDj0yqdRqYV2T62pGkKaK2xwZCHAqXn5HfKIjZXvC2QkL2tj_mSTPZdzkktM0LlLGrmSJVa9w2AGpZ-cPXQajyLh7ILSFvUw6YPXBexCnwJVHegARdqzfax02NP5dRUrofJzRkGo2Go05Wnq6MyEbS2Wy0DbY3ES-TLV1CgEHwf__NbLgYREg0hJsi8_oQxDkKeEZRWIQLqyDMNMSDTusJQf0X3lj7CTBTO3FYQ17TER8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kld3Oy6QWYdmWeZst2sTAicjK5sRiBhuloLIZAPqkKXqg5EDhO61Nt9tgToWeQ4yB4sYibhesVFP1TnALLAsDV4u-Jbx36gpQEw2ZPQ_h1aNaExwpJ1mHwGDDyubEkRZQVv3dWkHkQS94fQvw5sJ8tafbF-vX5DfjFXghvn-6cSUJYs7kTbxMWD8NVxuc8VzOxAmTDOWjetgTi_rQHh3PkTVoMqXuXZXfQNc7xNy_8H8asYtxDtacboV23dIg2zWajovalz44RmY4nVv69WrMteANqxRueM2rWjo2nhwuMr0PrH28glB9qJFNEM3Td550NO13KYiZUGjKA4QEWGFpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LwSsfWlyWsX8GIONTk65YQlvcNj8o-dsNTm4Jfprl6-tLMe44CW2FTqmHbhiJ1PMjloonTrZWjL5ZrGVcS-YzZj6qJY90Q8hWTHR8EwOzbMwY0Ak4f334Zv8SD5opib8DInvjRDJMIkT83tPE-GPRR2hBkX9GP6E6iDcMky_wv0jyqNDUBWSGsndGVDpqqAvV-LfQazYDnkluzNqdD9ryM59EOOuhSTajAdxjIa_-GuQFak16cPmkaOHN9JD0ZfNZoYXGRzUB8v0HS_nv-m_fu0SMCyEOJ6jhzuY4dyaTJOS5gtWWCsS1FBbdwxqZ3HGOC_y5I_o_3uYT6VeCaMD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FB6_f36WXq5_bXsxgX6DJ2tobu1L6z5rUqjmsgSkG2OwYYx9C4P93SEgpu0S4GEtl18n7zsp9vJW1HrgzjNK-VtJJZdtKZh4CdcoR248LzHwFJgz2J--CYEy3Y_paWlcjU6cyQXp0QJDQtzfzmx0q_eos6yiXMRcWHH5LoGB2J5VVvxpw-GJL_ty52gKvM9zQ_BpzXNy894XFKX-R2j9V4CzAsts6FBBbQMAh8pT4-x3Lq-2uCVXzGHLHm5R5Fz-hR_oUmxI5meXl22uwaxY0DbgjrQGt6U_2Km7ATWdQr2UVm1yfNrugs7pupyL_Y70qPSdZItpWd3xLma2ePnnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/axlmVI-FGD-joN35NQQviIZ2_eiEPQ6sx9G7h37XYUVabpmldnSEDhncRje2QnN9sP49x0V0QgiODCEWg3_yYNWeMExGvYPWMnzgPCPmsKJXNDNRzFfIxkD8Afi0USBTVjMhft_zLtXSpRZ1S1-yTmUhwpPC-nvtD8-GNaf6BsKGbgi2YI2QoSyEpT1D7VfKPf3uml3hFTs-FHXcCJRGg46siYoJRXiUAjIA6QtZDfkq1xrRxgy3DMMG_Ts85W2q_Cl4VT4MU10YlE7g2KozJ2CSfyK2ViMQE6cJXZVAme3blYMks9ne9nVz2zAkQBWOmFJMqF-zmnslcsc0rHQ7gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LjQdimfb4wGNbM2twVNjknKLSiBHBIgXJusEGL48n5Lc5En-Zly1QqrzdivPaWUU46vH6m8RKbhVf52VOoOVlBLhzgcH2iH6xr25XE-AzfopSAzGwF38JMfCun-oI5KMru7YcJTHvs17NMmBiWWcC7jfYHwxPvxiP8U3RDXqI_w1jYtyzEU8J7JAEuRtcusIndo0t3BBFgOb1rySwoI4VlnQz9v8GsTj67_uROOq2y7NXYXyM3fqAFxHhRZdyX9hoetdE87zJ1I7mnLMp3FMOmyGOGJ05IZ2uT944lcAibg8hK-goKUbmyOMpZYPOfU4cKNOnBVwLVTUWI_Iga3vyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S7Z7LiLiKN6LpQRYkRicDTVBAwInLDqD2Mj1oXdGLQ2PgXLPvB8g2JU49llhOiW2fzGXQEDonSLSkUvfxdV5eBWHRhrze3feiZHDPPewo6FnPaz0aXgX9nPsQAo5gWdPYkR3qzuA0ZB_ji5Tw5Pp7cBDkSpXBIKg80ZB9ycekvpKgakmg4EcMqLrlZxKl7JmnyhTZMPCBpLkJHSRKlCFrQVcf17Zcivxkn91EGvXBt_KdhU-CEMkOig0_1GfmIBedxKrFM6GXXOmi2QirOfvXB6UEZyKPR3aFUMfqCh8-J0Q2vNAomswQaC7j-w40-mqSgm4YOVRMh0ISRsQ6KHflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OCGvmNrhYu9yQcHwGZ85tI5ujFnGr6M37Ea_6XSpu7GzLXgfRtRSE-IACNVQfytVHCtrbl3Z237v26Xd4o3lr2tPAk_8o0AdCgOIUlETgrW1Rhkeid168Gm2Kkb_eV5DbGewZSlNOMXDAdC70ouzgc47o75B0y4XGmeGhX11XyavigR7K9Pm18zQVZVreWAFDmdFJJEdY9pKCZyy3EBlgW07Kf_WM29D0lWZ3mM1z68HhEuTVfsnSZpk28-CqGxlb48X8frmByXP8eQ4NYn0ona4Xl_MI3__APlAXMKg1eVe9NehaIrKooPANCWlHh9d0njfBN_hS3zRZFlqOrN6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KyMYzldZb4rUj442HucEkA04BHm3-sDlyUc50wpxgKtyrvH5kKnMscj-KIGzSzHRd6zwRXHhPH-225bfaj50bOGeoZtR8L3N_JzN1MNM2SvqPpTfe9tQjVzjYAdgR99INdYt1zJIJUGElx3o1DpmzKgUhdOTN5GVGS-X8yh5zbr79mhRasa0nrPtmiPIed_J9Vp1V980P4WSPPzVEi6YdlPYO_rB4RNEegKx0V_6FIkaOsiKbiU351jHvcpMayjJF3dHqR4KHl_5Paea2Z7VJSVWG45NjlJQUD4JHsKf1bcm8EJIlBTY6BBHPEPs7zq5iG47_bcd_AS8jGb9mr6lOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UTIcxgSrzCf21pyot8_o0S7aIraqyLftiSy9V9-d-_1Bi0s1L-3i4R1x8rFXo0KSgS15S7y0mONvcQQxw7iIol98FvsSEWmkpLwYxfYG3huHc1puOd7PcxFCeLGDCGSw7AXS0nj-kiVUzqcsr9acGsNRs_ZmnT2t5POwIAsjMH0NCDuBFgPl9eQQ9TKxv_Aq_dznbzt8jQlowoKHWD1y_JEAXOtKjKmHJs-Xgj4THrXXl9XHP3Hcp893_8PsqVuBU0RbZgkSfE6eG4Qmu23pD16SIBTtI890QuxeJXTucpZ5hwwhKxldjh_MK-GoLhXfYIGDebdLI3_eVQQdScHdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMDPbJBJaZz1yJKb3ZsKkSj31LS7ICIUaiASdA9Gj5Cc5xanwTIDlxxjmVacP6seJjs7jrHheAa77MPSl31wqPW8aBgGSxNRulMS5R1JtamvGpoM34kAhmMMWEpeSVTL7BYYKnvpYtY3IjfneZ8y54DEryEgrWg_qQi6mqctQN0uiJrjWlJVYDsTpORySK6mvvvkaGUzizymG8htWW1Us5aIKWVw3apV1TERVBKzc7OUXmCoQ4ugYNUwDODn8U3txTSFJDKJAJVZ1lx50ZyOxewt_ydnuyQ4ThBtbuzoBGhpt16AcBLYPBv8AyOBkN9X3pNns9wItQKsm6GmoJw9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=LU0l66QdrbrYZPWku46n5CYUIW8Pqs2mUDU3yS-6FTqJrQEzJW3DQGwz5KmBCu-6EFLvxD_9yG-TTRPOM1Byeyf7-94sC03oCwBH_Gd6IchI5F9oxeFswW35i0pGURgeX3cszDPPyv0A3MuDrFyGkY1JTDyOJXPmtJidLqcUwTEwxiazDPkVhYgktcBtymzgxyenF9k_UuA4pfT6NSHbEzEJk2NPRZeIM-3JBSlS9ifi4KIUA_QP9wL4vAI6z-CPAJVROQrxBleGAti3JZfVhhEtBcoRPgej5uUyGBKNwzujOD_zc2G7xsqdx0Bw4hbAsmulMBWBYJ-quF3Ybrt20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=LU0l66QdrbrYZPWku46n5CYUIW8Pqs2mUDU3yS-6FTqJrQEzJW3DQGwz5KmBCu-6EFLvxD_9yG-TTRPOM1Byeyf7-94sC03oCwBH_Gd6IchI5F9oxeFswW35i0pGURgeX3cszDPPyv0A3MuDrFyGkY1JTDyOJXPmtJidLqcUwTEwxiazDPkVhYgktcBtymzgxyenF9k_UuA4pfT6NSHbEzEJk2NPRZeIM-3JBSlS9ifi4KIUA_QP9wL4vAI6z-CPAJVROQrxBleGAti3JZfVhhEtBcoRPgej5uUyGBKNwzujOD_zc2G7xsqdx0Bw4hbAsmulMBWBYJ-quF3Ybrt20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGCqu5MM1taneCH8Yii-QHLTW5MGSSFQa6Nt9KG3nSEcLpjCEvRgJIO5OfXoelOWUlaF_IpeTutScjeDTIJFZB8146puvTUq0onJVA3rH_bHOlnt0qQxUZXwNy6vTN1ur5Ra1SF5QZLHZHy3IZ2jIfg7uNLVVAi7SQ5Tobkx-lVaEdVBDA_YMm0EO3m8ljLwwBlowhCA7xx7iIofKynRS5HIV6LZlbU3mFhNCJsXmJUK41AAyfuAnaUlra6Djm6e8QdW10gRUm05m9Q-NuD1WLQAC30_ADXt5dACAOG21UWFUH1kw7l1Esa2fyaU2FmVKO_Da1ynG--XQMhfpAJvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugTCeWIb5cxENjg3a_akRJuNpzueDMrZFdZPFsasCbTzYiTn8RCG617OCP18UMV53L7VYn2Ui9-tUtzVuCfoeEKJuGaboT9P4FpK8ZDwUm3Oqxd3Nt5fLklQI-AgvmtgaruOl2vaUqcs8XvxpktavLEVyIoJndLd6hTydVA2THTQjHXBsDsCnZf5HWaMkINkSf8DU2UjU4lAxC_bzBEhJUaWYQVYM0MegAZWWpqHdDSejOA8D4R1kmBy5n4g0r_cgAAhuUzwh5QsPrkuJDHZQbNUwg_jH5Gwa6AwYz_phqev_v7jqwUE4of8YTTSeyOA0wEBWeTRU3cUrrgsyFhdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k2Jj4eRuzQZZnanJwSkBtlL8ASneGhpz2_EiP7TVFONqhwKGxyedt8ucMs8PxfrGw6RHpKeQnMLUTgDpYVXcPqRjkCozMLdsC6St5vaSc2NS_M1bJ71LMUiOZKCj7SJIbuGctw1C59ReG2X148P4wgcIt4TZInbjKGPU8n5mdCqsSWvm53onkfmcCVd1D3vnAsp7pd-e7o4r5SG89pEmMhdut_9zosQKtyFt1GFpagMl8Ja6fG7IDdlfBR4OJK7TIitmP9do3P7OWxeH4Ra1VJv5a5Cm8D-GDs8plSeapZf6zMalgTO3CkG_uO3Sq_eg4kqqhnbyMsAnQdMzh6glmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OBV92xUyDevvWcX7TO7qBQkoSRPm-jqqLoYMi0rCScJeCJWgGgG6z303Qc78aIGaCmz7k-fWcq5r9QFfaTVJqx8HaRDzUpZUtsJRMMSFRdHDFmOEc6V5u06A36crjuU-XXgdNAXDNECDYJLkJFaKnVyrMSIog56zBpBZQsVLvn5FZwj_Izo0HkLtGvJsWwAOL63DaQWgPZw8KjXT5InBE3DGVUdBZbiHxrHrCqCPX_2C2YZrAKgmFirruCXecA6xbTk9IKX5FgOUrbCAGJRI33N4VMJfRP1e5IhT2h6N6ilSzsrkPBqSUeG-L7U7tpDwh8mn1TN72FkriUaANX2yXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TiFY7ZgeMQ0OOtO1ujmZ0eiTCE4Wl-uT89VCahK1EmW0b4p1K6RhUNUxEui56qM5AK3XUjb3dh1cUwddZkMsGrzGv35MO_x1T4TqCT03PGs707nSQjmclF6KP6qr3qmcOwU1cigGPLDIBrEIpj_6MuBEL2AJ2m9NNl1pfg-TNFLU7zvNfd7lTRZ3HVXUEXuXMoKkM3avXFpe0ovCS4KHr2A1OSiw9Y-QudqIsko7HgKgIY-16lhxhu_4THZD3JfI08UK9IHotjIE9ianJ0b4OqZUfMj6VFGqbTgtzBG2t4xU5Yd_mA3_eDVt4pWe6l7oQC-maFogwiapOILi-hoOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f-Mqz5hhYyak3UFH1wyWWqeqACYXNFGaqRK8-7N8sI0PQrKPrsnqBqQDBWSyP20n2HZAvSGnMeNPd6m_pDjYPrMee1yVU2JYw4wK8PfR0UUpiuxsQB6od6gfud7xg_iR9EeRiF_dR1bw8zB5Wupa8NhJoP6K0KqTMJw_VKZlm2McT5nL0NyvDu3HT9Ug12DVOdVPIzrx5CSDu83UuVHk4qJHB9V-dUbSMdLqMrQz217EyOCuJ5nsqWCWVv7ERHS1e7tTilw_xnX1mHm9lRSx-nYUCvSIQNbvB8_724iuAKkT_QH_K6NYg513ucj2dZQ12Hb-T-E_TYnaJ36RFLFIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FF4UFTH3XEoyCy0rmGgtbKjbO6TGq60Q9ms7L_AEg6bEnFN2VB2KRD5jM4l3FKFGCHNdP6NmI48oZvbbLr8c43E7zzclnipALgvpM5XrkaF0o14pnPEUmuE5QUlcWyeshmp9Xsgjp2jHXS56QIkKrhtI9dfF2caW_KcI9U7Xl0mBoiN8GLmbjnUoQ8VCdNCXfGaqeR-LuRT0oW8MJcD7BVx2_yVfHXS71_Q6pxj-_RibMQ6IzO3VlNkIxkurx9fIRIOTpnYFd-iNh7xkqw2mGCEbqLPKAaOK4q64dI2Pqi7jupWlWDg4uUFHphRimcBx2HbA9yW-FZ3UyKlug_qvDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omwuBNka-VP675v0svC_wj5o8a4uqFC15REEBTSdDZ3ZTT8SQhBHj0g3b20FIDC5LsIVBMANkFVAapawqdt3Adi19hdNhVcHWky3SZNfpxSBsS92HMZbYrzNSs0SEp3qXjAUTd-H3yLuzIEKX3e7-OgfZyq-K3nGStztgv6mnwDhfl3NMb9homheZMiHJhBfBvp66_sn2U35gcE304yUVm83W6a-CtKrutyUQPGG0_OrQIj7DmCYdH_KaKd87-GU_eoUm7aVZSpKMcQew9UfMnjfvMaM7dV9VjXj_bPWN6o8BqoyBids_Hm-fNGoipYd6kV4IKudeZW3SYZtAMuOXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q_jClMMq4iQrIwV0hDlA_Wx5el0pMTm1Y6SE_nBByRs7-gwSusSewOZ1_y8XxTjPelcKRFEM036K-C1cH6-jZenZ7gZTUrqHDGLsmpuVRIvpcCvDXVSFW2eUcEttbW5m3oGU0mngq_HY9n6HcghWhYPnKKBGlanjfV08jGDr8w4OK_CGOVv5SIvwVb9FCrFw0545F91A3ggeIPTucG9ARynnlXmLD15IENcXdqQFoLcKyugh_JvNlq2QfMy5ES_PUoNXuXVuPz9WhQAiSo_jra1woS8pnckSUYzsESn-Lq4N2hhnPPKx51K_-Jdw9_wQ8GvBANOpCefIKMOj8NNfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YpJZosFi7MnvbJLLMtA4INoKG6fltAH_XmOjVD4ij3uh9VnxNWsiJKGKhQi-LFJDUDyg_OOMuREJalEF_xOEUaR3QKmb-9TsBaJ1hm6x7jVlDODJN9fgvgSilIB_VQN4ggLtC5rXTEkTpPVMQILJG2R1LcAzYM7oRjm4e54cs5aQSkGqwFkLnJDdF3d3JW1IY6-zWc2u_Yc4YSzITpXT4Y7t_rQFeQ_5Hd_YA8FQsA8Edel_CU_WVaIXGDW-dTxycfPFk--yBBDAD52ujKU2Xuzrrh8Hf_3dO59r42WzyKNs3ifthPrt-c6mJOtODm4Z9IK35yLRpcxTuWtmbedqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z3XutjXO9I1cItNldquVirWqxu8ksyd0e6RYRaxa5FKaUHsNJn_IbSP1HIyqBxaufsznSxGSJosNhKt0MPv-et0qGTXZzBcKW9sFmwu6N8_ATb1LUzZX-kSP6ztKZge4MmMHdqDYo3Iw19ZSfKwDkfR_jiXvTD0I9ITWzMTts63EvlAg0j3_VtWWUyTHqmTG1tKdhWt6bzwEQgLEnblG__67pMPNTah8SDjmEJ9lr0JRCUbudpKc4Wld-zcUWmnqaKvTbZLh6oQCa_j9ii7NRPJX6Kp86nepTPFp410sHhTxtIYG6cJYyk9ibs-JnudNXR0zwmwVShNdaLEYsLo9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9rrqucbdbV0IVU8Ky0C4-Xp1QUXRjsNzu4DKEtgBetIB7jF8mEbfeWJVItU9w8-emqPUUrJ_nzFPCOMQvJizr3vT_Dkh5njOFLLiuU632tI0AS-jvi6Xbi9KK1mdoAp_wzNiLlojgNovlQcgPXcf1UzE0plYXKQDO0c9PFe1Qq6oqhHqE6jfriwbcm8xmsFr9CsZiy0K0SGVwP9oGcJKVQIaPRUYicp8wMie4mb6W-YX9h34M64y5Xtg3mIMvhNJST97AzkhWecUKoS-2DvMloRo9u2Q3H_NBrhkuLm_nG1gWOOcP_U-tdWD9MjPQnnwBFG2hN1DQ9YZ2OKvNPHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZK9tbPl0kNxuukFiWnonn7i2SvPNkGpDjOv_9kFbExfco5dVpiXAmepUBSEp5BHzVYPdTCs1X3lkI9Zkd0GHq1z8AEw5Y7vDzEKBHN_oG66HB66o6WFEW0u2YSDQlOnToidGIhxG2fyJuAqeaogpzoWMVSvgCdKsVTO6UuD8YMLCdC1o6CWEG53cgjs4_uEqr_LqAYSApyfTqUjK9KgYQctNDzPuQoqubBmVGEo75ttdb5hznKdHZK6AmU5farrCyZH3U6aQp4-_yVVXUi1Tn3QKQXSSAzLIS0ubxNNORkeGI06brV1e5wSUEtXXuxg4efrUZNaqVFW36_zW80nOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DnM0MKMkayp-ujepf98h09kyMqN0NC-sNjSL_8hJG2VrQAPwh2_LOS3ZhcMfxmD63NPZuJ8bG-bTgBkkrMIO7K69PZr2l9DpgpmMnMGReqCK7Z71-S92o1_Z54E9Y86Sfj9-rE7Cp_bXivxmzTtGUSbNFHRqYZ21HXtSZDZ9-P3gALBKVJ_moC2BHIzuVRXCakgnKqUqFX5b-NWDlaFBrZCWsMlUCoZb6InNMQx4NWZTPbccYiLu7bCPn341wTjp37TYxI_yidC5zdSx55sQL_fU9fsESetqcBozwN43FURsTeMwkpAFAlAjrPlCgE24dTQmIsytKRFt2hlTOIyerw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mdSZFAC8egWKNbVdo7yXGGKBZKp9cRJvqysgJ9eEC5rX813StcFOYKaCgjSVLaQY_Qqp50GC828PJO8pFYvYwdxHNCt8JaqAy6hyMTwYPpVHcV5NNrsHVtPtgJaNziNdafSk7aN4T4hshBDDOYu7k5iPQvpcXCHOGnu1udIVia0CkMzdchkDia9ly039eU2BbzWBmSDWGL_ahNLf7EV6TXdmp1bVK7EdAU8T4rKQKBTSk4SycnicSowoqeP8kOUjfXBjPeYJy-hEl3YWCIgxugB8AqFbGOcHHE3jXYtEH3kj89WfjXkjxzxaMgYZH92EKb8PIsgsJiafHVveUxetfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KW4BH8SfXipgZAPjEkJ9sfv9rJ6BKKL033fAV8oJa1CE27bohfL7BJ1JZbKS567hzWLWgAoFJkP4-34le4dSpZd9P4p2XlcONhr7r1097lS4Cw8-XlkBGy9koSy2L5tsiL0XyU3Kk6qL74DEs7YVFyyn4su6IpuBpziCiqUGEOWhaNDoHv7fY53JxewkLLd0h8u09HR1zb3Yq3WUnAKpH-JwP7d4KfB94dd6ohSxeY6cTVcpqO9AW_FKUwXYg6kdw5RzRy3CIXA0ZE8voURbEWVKhfqlzx1PhxZ_wi6zXl93R_FJ5vNQvUOJ7_B5KjGkxHby1-n8XjaoWF6t8pkn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NGSUtorWHjIsQdB85Hk9DnFCjwherHgGNfTr4PRGnzMFiWEfiDXkwHkRI0mSY8TrnPgUjMyF2SuolpPFj3SvJfw5t2_ainhMA4U8VBEP-SpaFi3B9wxVkZFeHsliXBFaN50O5VgY8auyAN0s5dZCbcvkLS_p0Jv0QCWHPdJ68q_db47wC8DteUey8HJueSb8hHANCGp7yzDmCmwjoBgQ8jSwmHisz-2SliflmudHw6I3od1PJwkYFxKMGJRun4PCre_x79nWRc34rKCAY2dz2XbAicH2WHMCmYRnFChcsbWaWXVFnukSJc-qMeXJy2Mk1bl5Z_m03DxsD7TUk1UXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HNURMBU-cXEHvy0fdjf79XE_Q6V2RertKdInZFGr1nbKTYpkZFmeGZPrX52ouayzTENCmXve99-n0ce0OPfA-k2ml4JxVDzhjPqavZaTIH-mL05XwA4MLRsYwEzC8bodlV-DE3aciV9eBJ77bgXeJ6QsWxdvQPd4JIVgDGZscluTOzEWVYJyNRx53kwTqN4yCOYWFozXs-F52DJmYQwTVjx_smi69zrDBS_Xwk7yy2NvoARIV1wwl5IGmPp57BG5S6vBV2AGGwxlEdLdQX7dIfbkf2pTkZmkU7KJ8JdCe_MpTIMVFWA5oL89Ehy82OfvXWtoD8ye-q37wrZNcn3A6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nhW9Yi7YlUnhew_vdKnksnEb3-WB_JEzW64XqK2afqiawNzsN9him4kztakfWDkTJg_uUrV-EWLo6AEVk2URR1RPY4SxPTJK8sEO_DbECUsV5izHBBikPwqWB8dfbIPx_4wJQ_k03g3GxsO26sfkfeKJ60mSXyMefRIxXsQEdvDzfdGnBINNuGcv9Uf8PTitoyJUj_7y5aXjR6QLGoXTu7_QeAaZghRvFZBaYDYBXandtWl3y__80WG3jaT5F6OZwPJdHJ2yLdRgpEag2hJF3s_lf84pbCC6xBD-i1vb9RYqffm_2OfBagKESmpaGwEG8bHpBXHNjU5T6L7VsCwyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qeg8jAylzVDftQWaeLujpR7PgNfjHUXNhjOpW3wQv9cMsvGO3mHEpsa2uuqQlC5wlOcq3DFVJ__LUOsn2upLfPnlCQyrmY2YxT8ZP5INVOCGUpv-qLlRD6_801OOmaAldNh18oFZb6moagorlg7P1HiiOd_67coCn3e_grb6N7PbaVLtCoYfNJ0C3RW3fe0TySHRLbgWbig7XC3nJ3OWHlRgcMYxnCPIADrxxNVDzJ5Ct0nu37oQtVDnRbRWwNICQ8DqVsGddEMACKAZJFoYs5bWyKpWzoOV4a1KVyAXnWAayLkjFgxSUmMuv0NUt0FXlOIizg63jxHU1L7iuGJd7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GsU62GWRYWKZuaRBenr21i22aueAfrqNGpKtzeAZ4LfdQS4rBal997CHbwYrXpltVbC99pDDah9jqP_voKymsqsdb8yndpmepLHiRXEPsz3FXen1dNaCKoH6wKiN4BKfUaqIqTAes7TjRSXa-GZknKek7Gb_RPNuM9G7zqWGqcP-l4Lx20L2hTD9bwsTNI8avVng5A8o_aMs7QSv-ceHDXO3ZgOkzMdY6oq4xYMQmmiC-uGecDiI6ztb-WM0fcrWISX-NCf1jPUfYdes7no0v9VRHrkjLc2lIZCX41aL7s6TRY8GZoH6kAGmMh0G_NCe8tBXPsdQbiBzgsCcPkm2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VmwlG-7M2m_jxucDmcMKykDyCI4PTP-iahwQ7oolMF-xl-qf3IcG8MMvDXFPIgKORxJBeHEawwetRICZIkDSE_5hjKMXE63fmd3BLOHf08pE2h5T20zj9oEqY-xcMecxKq5lR56JjzrH6C-TBeiTeC45Tzy2_ONSOc02Pai4Hs_mCYYYxX70y6ijY_px6DcX-qVnSk2CIx4xzjweanv3bNvgIXFrI15hgNckOVfZnU4xEZinHLW4HfYCOatgdGZVaWHqrC6HIkRB-dsFecsUZOjLbZyjd63M1fk8mnQ8DTo2kN-7VSTOM_ahxKXVDIT2uKhWyiBwtD-9NFA_OY31iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vFlVJA5Oam5bk-UuYYVuVPAWin-8qILKX2zb2PEeikwnxnFzWm3Zw5oA5CnR-m27rohxHXc2-Sr_w_RD7a2dmLPUiPgCl5is7lK46gDiveYANRZ1jM-9U8eqEnUToiCArrjahA1x7Y3IxQHxkQoJsnWQm8nKOk34dl5b_XegFg4pcLNi3SuBzPql9lX90Ji8XhzdNVLJJc98XnLVL53iY64WKVui__CK_jLSFnGDxp66pVBzlUxLyfnQKcRcNepMbufrE-Fnqn8vZ4O90kDEuVj5ZVN40vBVnxBXYmLtHb-ea144NeAax_U-LitjH30UAWkPM2Z_DxzcJpAeDcA7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XITnHF4g-Blwr36W10mJnZm7ioG0dzBCEHWLp9hMBN9V3Cy1ZQZjNeZI0K6PGpwTBQncuPFB9spzA9h6ddX74R_cVIb63V466LTo939_Bqw1wKQ4AemD9Y391m_TYB_qvgX_OvQbC48ZoeHWS6QHLEU_YGRmM3SikvL9XTIwwgFuIgibMIdFwbTu8IRnzfi-skYIplZr-eF1WWQfsy-4PyPbUGsRdL5VJSz4QrHHFOmm1q85qwLxZ8MpclM-v2kn0LSH7vAFLeMJQY0FPsdJuQLoJWJxS78JDU76Al1Iq0G0fqBjDxved8GfLNAchAK7NQ_a_R4oFCgb-hkhSFHbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/osuG5bmdIsBfwDKaI3ZBqtndvffhwkZxqjb7ESJHhtHkontrtHogwVqQlHXaSRi7_MNz_VC0iV78wbaXGGfOPzrxkt60xUT-JRlXeQlYfO3JxX6s5eVniJ3SGtI0xNRtWeDBSwloIEAsb6Rk0Y0nnpzlVIHpiPzBLx0rwLiAazGZyiPh8CbiJndAprPoBtz3grh23Bs5FrR9dSIYaFTCnEntasGQQpRnxt_KJ0uulzV6Cvp3OBKRhXkOmT15FG4HZDvniARDo_bEyEXv17bKmy_7Cx_IlI70cA3q5q1CDHeHvx0fSECr2QByy3kOlJbk8VQMvCf7j08NaolxxZjZ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diYhPnhEVOho-Ngav800bKXux9tCtx2TBu2U-2xsPaLZy-logX5iXjjybsHVlO0epKxcafwvUszjnFt4kI0tD76X_PhVqHzs3HU32VHbDMt8q09GSgeznpTeDNefnv9XJU7UTZcNXUF6qxnwybUed8Ww48lx97eXKXSZpLOl9RPE65TwXkTazc0LPWIShoR6qBL0NtUNDhmlmB0mZkwfWiKtvr_iWesFXfJv0Ddm3poHw6fuVgd52WxVgKvxqXwxh18fzy5gTU7ixr-SLzcsQAOwK3-j47aOBZANBx0F-BpeRSpzVUza5peilMgGnYVnpsfB66WeDts7WMtj_LU8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Da3WH0EFulq5eMf8aJndJqjdvPepDgSwQkCjaNFK1ehRsF1SbhMCnKSypVopBIWTdRi7ygFLj-msu2i0YU4WVxzBvn4hJBeu1twMjhPW4rB6XLVwAQlgKImior36vMhKvZv_HvzqQ_uZbKKD1_W6ar0Uppzyp0UxunZI0bwr8Nuw9FtgHRpjZC5m8CDKR2c9szIKjIz4-1m4BGZYk6mAHO_P9rDuxnr7y4fCIV3HtE-oZiQVVJLwL6eyim2BZGQIhSZPK9ABvFRP0S0U13azIUNH2T2HNvArxeks1q7i-BLxiBOz8ZzWB34_-9EN2ARDdBZKtiLtCcid_xWLQ8NiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rMTgIWLMeonEhbLGW76yOQbcRIBJ4USHgBRBljnmfUFhvTztH4uueUM-Vx6Ttu94VWunkvfvEu8lRuVlfrSiQdlhnVQ-0c5HIfVPcPMx9KWn2X0VsOkUJDEe9Rrv-WAzuPuu7QA1QTSzgYnftTJwxmGWta7NSz1hrI07lfTvhA-lpZZWcGH0ihXuiGHUf9egtijkcvSgqUa1suZs8T-BNn5xDVESOyhmyffAQb7vj4YKsvwPefCQMxwMqPCsBb5OFBWRMjYq1z1TYpCcL9ok3OvH-wGh6kgrVtS2ujpz6W5lDkTtYQSWsnha_2-UJtJutn1K37vZf-6v0hhMlQXSxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
