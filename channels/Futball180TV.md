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
<img src="https://cdn5.telesco.pe/file/azStJDTFKUSNZkWUALg_zugCGkUySLRdgeTgKzlE7R8oCOp5WZ1gNsKtQkZYrIAvC94oCQdQLCdVa2QDrnNnvYFtbD1qtrX3DV6sVtRukGsrT3Tuy-Z9XFX4OA0ocfc-2V9x5Qqnht_-NKvErhMHitUpLz7Q1ijfi5fMgQuH8mDqwINJhsbWE9oFv4lEFEwknpsZERVhUUO0pjmrPdVp7v1AoIViCfIIdNjxxlCYaxXsHLpQzaAXomXlyOAaY3HA8abqIfwhYb5lDZ1Kew3TwDLmwHsmCdkrvAVeBbprKtX-dOHXop0g3soItUznqNZUs2TTFZk29Ly7SkxLQgPz7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 552K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 18:55:36</div>
<hr>

<div class="tg-post" id="msg-101342">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFlYS97TglWPQt6IV5VDPbZ-g8xXYmjiKK2oUwQJlrjhMLzSanGdYer8mrZZ-yJlMmDV2hHjwSm-sIyEv68BqfDNlQfbeAq69JM6e9bQH9B6lTixtv6ULMwZjxZZ53Q3QpeIzidt_q3nxOTaGUVeYymkiLecqvGAaVtZfutEfQEyvjRY8ZYc2zcazBTfkqfUNbKoMxOG1-lq8TDZA1c8kLP85yD4lMrCy3z0Qwi2uCAnMjz-AInTT2NgkbRAS9lCuQfeMl-9tqmje6ZQwiHXnJxUAVljDAtRQGdSXjW6io8v24HF_NgJluC9EyVMQYiL44hlQ-tWDfhdZz565gRMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
#فوووووری
؛ به نقل از منابع آرژانتینی، لیونل‌مسی تا امروز تصمیم به خداحافظی از دنیای ملی نگرفته و احتمال داره در کوپا ۲۰۲۸ نیز شرکت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/101342" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101341">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=g3sY4D0c0igGpOfVTofu6S1RPeAqQRvdvXr9ryDKhUtq58TXCcNN2jRh8bxKbqJHTioCgUG5mjxent4HBGkiPehlnTTcD3qXMH4abX2SonT_AtsesPxUZf94GZ-69bLqvpGU5t5loHWsmi3FZdbIRl13xjWZOjs75kMl8dNBOGWjk2iokE7PzHPVPkmuxM-UWghRiIuLP5L6klArp_LzZpHVsWbhYFCawjCW19EXb1uXEZOsvdXAcMWtODp7Nhe2fxK1PZh601bPArq4AQyDGd7rusYuLA8Mn2j7l_VSnbjiozV4ETm4i-JAtdaCaEPg6mfhLlUYmVSiRkidlhEifDKoyxxBb8qHopkwpLrjSVleEev6YzHYO9aJ0iNkSEPEAg6J7WorfCnBcsQmK1YasjiSkH1I5Kzzz72yx3khW3euPeI84LylHAIYp8wbQLNFj3mzaKjI_EevZJNC0zrmE_mEYVhuv4BA7hDCJmw3T0fYyzRT2hI25qb52DSIStw4kba4Qm2LmkPpeJCocHSPpmA2NtECgiEoAucLLE19biKg9_Gkg-LRFWq_fku5SlwKFyLO3W_fMd95bu9Y5PGEVTT-g4z8018ecKam-3lDtNZaQY8JpWo23zclCw7-8PBK5fzoApe0soUN8ooycIkL7TBP7cyjnFTWgD599DsXCg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=g3sY4D0c0igGpOfVTofu6S1RPeAqQRvdvXr9ryDKhUtq58TXCcNN2jRh8bxKbqJHTioCgUG5mjxent4HBGkiPehlnTTcD3qXMH4abX2SonT_AtsesPxUZf94GZ-69bLqvpGU5t5loHWsmi3FZdbIRl13xjWZOjs75kMl8dNBOGWjk2iokE7PzHPVPkmuxM-UWghRiIuLP5L6klArp_LzZpHVsWbhYFCawjCW19EXb1uXEZOsvdXAcMWtODp7Nhe2fxK1PZh601bPArq4AQyDGd7rusYuLA8Mn2j7l_VSnbjiozV4ETm4i-JAtdaCaEPg6mfhLlUYmVSiRkidlhEifDKoyxxBb8qHopkwpLrjSVleEev6YzHYO9aJ0iNkSEPEAg6J7WorfCnBcsQmK1YasjiSkH1I5Kzzz72yx3khW3euPeI84LylHAIYp8wbQLNFj3mzaKjI_EevZJNC0zrmE_mEYVhuv4BA7hDCJmw3T0fYyzRT2hI25qb52DSIStw4kba4Qm2LmkPpeJCocHSPpmA2NtECgiEoAucLLE19biKg9_Gkg-LRFWq_fku5SlwKFyLO3W_fMd95bu9Y5PGEVTT-g4z8018ecKam-3lDtNZaQY8JpWo23zclCw7-8PBK5fzoApe0soUN8ooycIkL7TBP7cyjnFTWgD599DsXCg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا اینقدر طرفدار داخلی داشته و‌ نمیدونستیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/Futball180TV/101341" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101340">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/101340" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101339">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L20ecoaosr6OSwzYtrsf3SHjontOaYvr3m71-LrkRztoN-yAeHglrzT32FYqaeenSpmanTIszxaZgdwxJUKe2bQWRJwl_K3x1LAciS1PeChGaxmM_djtyBc-sOgz7m4ZbAodIBgSc4RbgWdCHAn3enfSS11dREahpcPzsEyWQ_LuiNxrzi7jOv8X1izDZDs4Dx1bOG-43lXzeOn6Us9SueMpvk40MVxbMd6hk30NPgG_kony_RUH-hB71_GdCKg1cAxFLlUJ2xFSbnRQ1ARaTMFnpMKO8cvv2IRowR0biobGJKa9Viy1FkM2zRlQvnrzFtxH6uqT1EM0x7ESbbp05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/101339" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101338">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oInOHmu8ZtumWdQ-fOT15ULjBzUM0q4tTe3aNH928ZlAVQBcBgnHfZBi19grthdfZhh2Odbgn-Yt-Oyy1t9FMm-Kv1dxZNztCLzwxTDbahaACBTr7i0XKrpUhYA8QSFZYXVIvCjqD3qu4cUynp1B36tqc6eFzn6LVRmufJLPK5ZXUG6fSjqZ21tStmU0E6VNcewYx5pHKC_O0R-QdYd49cobJ6rfJGorzBmRnJnJcjgnkUXW5Y5jSxxil02qzf704ggP-65F3xjLqac2V4Oq0Er2Np6XmkIeXcxaUZKGCkpOyFgIb9kEv7bDZQ5SwdyjZFnG1sNBuujPg0zak0z1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی براساس سایت آنالیز اپتا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/101338" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101337">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBGqLHXP1KvsIHvWvnkL0YX8KG2PII6iaESkR3mJ-Vp5wQTVfBo6JJ5QHKk-6bE7BMflKwD4H26KNacWaIwFb3vK1sHTNq8SY8d4vJztdnwhwgEIU8f1ORmQgoKiyYfq6-hqckhvp5rwgwQKvH8l7kmaJY9DhPI07qo-oylGmFjr-1apPkoaNueuFFq23vNJ-yNBHCWbA2jTxhJdwads2FZv4MWoCjam8qZjggcuZaYvAUqmm4NLGY0Mcbc8qHEOJu0ZkbYlaU_YrsT4y9OPCbtHhcGvfM9gftgTBLN603lLODxQzLQzsjtr1JoCtUyj-WNvRqMltZ92sZVKJ3boEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتین:
انتظار می‌رود مارکوس رشفورد دوباره به ترکیب منچستریونایتد بازگردد. این بازیکن همچنان به بررسی پیشنهادهای دریافتی از بارسلونا، پاریس سن ژرمن، بایرن مونیخ یا رئال مادرید علاقه‌مند است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/101337" target="_blank">📅 18:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101336">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-Wu1OcadWbU5e48FWrCmwqoSTTsI075pZWULYn3duuG9nI2S_CCok2K2L00TwBXOgxSX5twgDWU71rgOanQmTjNZU_DfCR-x8wWOWc5riZP0j-_UnYaxqyY6smizOpbUYW1umfkzgQZsOCevyUVeJtwAyE5X-K8FNBhmqapMt04Lm7eehfkIuoGudyyXLLVnmCrRyXgNOa5-kB8L0rGIg8BYSVjGav6UbUqI6nmixP_90VsrTrGS2rrRW2x4f7OTIj7pFbyfZqxZuXetL1dHI-PFWw9cBwdUlSfGNPrENViZ6MCF07sqIP0SQQI8u3bhFAGduG_UaUGCGrFd3Jdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست لیورپول برای تور پیش‌فصل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/101336" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101335">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=pihc_F3wPldUm0zAIDiVtHfeTFM7zn0GR7nO2eut03N0pur3iIJ_6KmRHUo32NGf8Ye-BlzOZSY4j8YkBMc8tkUp0w00NbD8hebW2m0MkW_T5Ox9DS65ePnHeMN2OF_MqhOkkScw_RP-zCAe95_tF0anvgiPxWU2W1BcBwjC_XfpVBJ9oNDtTH5ZUExfvGhDcG8WV1XqQo80V9dBhwj3Mv-SUyF9fX1a3OE8qtkc001aEsknN5JVUeaMArn0e6ZURZZbX3gW66jnuuTCqRQ6-7LuVl7HPZhB_Jy64-whYME-cn0ryKMN8hxi_kLnRjZXCjiZFEuVRKwAsyPLVsoA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=pihc_F3wPldUm0zAIDiVtHfeTFM7zn0GR7nO2eut03N0pur3iIJ_6KmRHUo32NGf8Ye-BlzOZSY4j8YkBMc8tkUp0w00NbD8hebW2m0MkW_T5Ox9DS65ePnHeMN2OF_MqhOkkScw_RP-zCAe95_tF0anvgiPxWU2W1BcBwjC_XfpVBJ9oNDtTH5ZUExfvGhDcG8WV1XqQo80V9dBhwj3Mv-SUyF9fX1a3OE8qtkc001aEsknN5JVUeaMArn0e6ZURZZbX3gW66jnuuTCqRQ6-7LuVl7HPZhB_Jy64-whYME-cn0ryKMN8hxi_kLnRjZXCjiZFEuVRKwAsyPLVsoA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ اسطوره های بچگیمون
❤️
🥲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/101335" target="_blank">📅 18:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101334">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=IJ1QIM9oq6V93lJqPZCcMcIyuGXKulcP1ErELdlSQJxDAMpsHY2EGLlq0hSIdYlVO8eJL9X1FdtkSWWKTVgI3iJiMm5fLx78b9IyAvB2fedC-Nlon4k0tO3aMmVJnLHLbelmgKfqMf6jIWKuN-p0dZWyoorlFtlTg-IONjUP9_t852m4idf7JU1hmzoYWY1nMIMbIHa2tBksObLWMNEzC8OggNXa7ViFub2yDUf5yF8zUC4aEkdyCp2o-RBsUgE9aEepwj9IQUlE2WaQWxa88JthLvoI7cGnpAaYJxqucn2OYxdz-RIYELn05YDBH6s1j67aEC18sUuKoTBSbb3_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=IJ1QIM9oq6V93lJqPZCcMcIyuGXKulcP1ErELdlSQJxDAMpsHY2EGLlq0hSIdYlVO8eJL9X1FdtkSWWKTVgI3iJiMm5fLx78b9IyAvB2fedC-Nlon4k0tO3aMmVJnLHLbelmgKfqMf6jIWKuN-p0dZWyoorlFtlTg-IONjUP9_t852m4idf7JU1hmzoYWY1nMIMbIHa2tBksObLWMNEzC8OggNXa7ViFub2yDUf5yF8zUC4aEkdyCp2o-RBsUgE9aEepwj9IQUlE2WaQWxa88JthLvoI7cGnpAaYJxqucn2OYxdz-RIYELn05YDBH6s1j67aEC18sUuKoTBSbb3_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇪🇸
نیکو ویلیامز هم تصمیم گرفت که مدال قهرمانی جام‌جهانی رو به مادرش اهدا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/101334" target="_blank">📅 17:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101333">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=EMyedATXYqEJ-xWlRJ6qOdLj_CWjQ5BWULfA9Is61dCSbgjRP7T5cKC5KY3xaKxtEEXLEMPHf1l4jTwIsuo9uQEzAq_8lluTz4n6HixvxVHNBNNkhecWMusJd6-LBiOr80G86VEvPrgCdhoXJHqgCfKKG9Dpi9DHhFzqMyD8Ad2migbg1oXXHqjG5rey2pw8A-BDDRI1JphexaTqoDv357dWvz0IXA2WOyVs2cKdVNgyhb2Gunn-BeaFnr8u6GOYRgJ_dStnZ3Szk2ksxkP6sxvY7kwzl02z8js3ADC6aQ6ifCAcwTIhVQkWaNyZ1Uz1NpJ_jG-AzEfvgC8ZfChf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=EMyedATXYqEJ-xWlRJ6qOdLj_CWjQ5BWULfA9Is61dCSbgjRP7T5cKC5KY3xaKxtEEXLEMPHf1l4jTwIsuo9uQEzAq_8lluTz4n6HixvxVHNBNNkhecWMusJd6-LBiOr80G86VEvPrgCdhoXJHqgCfKKG9Dpi9DHhFzqMyD8Ad2migbg1oXXHqjG5rey2pw8A-BDDRI1JphexaTqoDv357dWvz0IXA2WOyVs2cKdVNgyhb2Gunn-BeaFnr8u6GOYRgJ_dStnZ3Szk2ksxkP6sxvY7kwzl02z8js3ADC6aQ6ifCAcwTIhVQkWaNyZ1Uz1NpJ_jG-AzEfvgC8ZfChf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های لیونل‌مسی در حین تشویق تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/101333" target="_blank">📅 17:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101332">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=vanV0WtR_K-hC-ydV-XQu_TvLZa80vecxE_zgmtw5z0Uw_DW3TeylSFWw_PY5SdP7jRb8vSiChOcVffiitrEjRD7q6sHnjoJhqYYs8nwjQSS35czeE71U7y69D-HlfM8Lv-26F1zEfIcth0FGhO-XEKPl0SOh862q-_uQX4HKehsyC8CL-wrkl-KNOdV5wZOkG8Hu8YSt8y-65Fw5TGdU-QdNJTIE0B5kPITAC1L7BbRA6VscVcbNj7HNmYUCydaVMiyMe8y5jLwMX48_05FvstnHnnIvAt89ZChqs6aYYwnUja1fTqcjQnsKPX4UeaVtUgDiBV1bw-s1BoewKHp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=vanV0WtR_K-hC-ydV-XQu_TvLZa80vecxE_zgmtw5z0Uw_DW3TeylSFWw_PY5SdP7jRb8vSiChOcVffiitrEjRD7q6sHnjoJhqYYs8nwjQSS35czeE71U7y69D-HlfM8Lv-26F1zEfIcth0FGhO-XEKPl0SOh862q-_uQX4HKehsyC8CL-wrkl-KNOdV5wZOkG8Hu8YSt8y-65Fw5TGdU-QdNJTIE0B5kPITAC1L7BbRA6VscVcbNj7HNmYUCydaVMiyMe8y5jLwMX48_05FvstnHnnIvAt89ZChqs6aYYwnUja1fTqcjQnsKPX4UeaVtUgDiBV1bw-s1BoewKHp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: کوکوریا و بعضی بازیکنا قول داده بودن بعد از قهرمانی تصویر صورت تو رو روی بدنشون تتو کنن⁣. نظرت در این باره چیه
🎙
دلافوئنته: کار اشتباهی کردن که قول دادن اما اونا به قولشون عمل میکنن چون آدمای متعهدین
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101332" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101331">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l48lGb-U6GyuRWLxu50Y6I0L8XfrhlCWx9WsG6Eeu-z7JeMj2br1-iomqA7aU32wAIz_J8qiJRAB6o6klYh9DZ6NXaufDJV5LIjdoZ9TznULTayzKE4NEka9juVLRrDe8S8k0uv1FHWi1gkD28B6zeSLwuj4mRKzw6iiS2Qm51Tir3DxDyuY-Fl8lO4ydCFytT5-dGp4Z_9JudprrEynblwWJ053wniFl1EQ1uq2zr4DiLa10lPRH74aUGJd_31ws5IespKKB6JE_A0lRsBDPXkJZ8S7BqgA7mJZhTJFOnUHQeV6GEDQAbq4FzoK597UlurhQTgA9-JdS-xWl8znyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسکای اسپورت:
فیفا تحقیقاتی را درباره رفتار بازیکنان آرژانتین پس از پایان مسابقه نهایی جام جهانی آغاز خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101331" target="_blank">📅 16:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101330">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=kv0QgakJZSWJDDvAJn4PFzv94VKTCUF2qUqwsL8cj2SScWe7bKjoZsQEk7X1_gdZCUDyJiscPpBWOsH2YZYnczQGH-CR7PFYQBhjGIvt1tQnZ8B6a7JkPj0sUP5byl1xD57_WKaEOL4bhAhC7szcmg7_HFVpkcKHZ7WqXxeOUsKynM8Rx7ucXWZDoqsw6XGMcv8Q9uXqiv0i-3kvL0sK0VSggZIYdLpLWSsvFna-3I-EfD8lxpszipuvlqBsDnrtO0wDKTxiCnyWQueM2Pw7K3M4Ck0MPH8os4YW7oSNmo6HOkbKiS-goO1z6u66-YYuSlKheREWoZXWPyP3MToRfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=kv0QgakJZSWJDDvAJn4PFzv94VKTCUF2qUqwsL8cj2SScWe7bKjoZsQEk7X1_gdZCUDyJiscPpBWOsH2YZYnczQGH-CR7PFYQBhjGIvt1tQnZ8B6a7JkPj0sUP5byl1xD57_WKaEOL4bhAhC7szcmg7_HFVpkcKHZ7WqXxeOUsKynM8Rx7ucXWZDoqsw6XGMcv8Q9uXqiv0i-3kvL0sK0VSggZIYdLpLWSsvFna-3I-EfD8lxpszipuvlqBsDnrtO0wDKTxiCnyWQueM2Pw7K3M4Ck0MPH8os4YW7oSNmo6HOkbKiS-goO1z6u66-YYuSlKheREWoZXWPyP3MToRfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت داداش یامال در بین ماموران امنیتی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101330" target="_blank">📅 16:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101329">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm5jb8dJhoxVn7HPZzu--pO-AxZX0Bdm-LtRMRk3TTlLFZcwiu9cf1R3WmXFLtbJF--LqQkYojY17d3hTWb4-j4Z6awzdb0SUF1nfAEg5xfGWtc2JaZbXDGiyGSOiAQFIBn55W4nVGSCBOOADybI0uz3AnmGDO1mZGrRRCrhhX8rpvPClMjAHmLZOv8A4A90x2psXJxDxx94rNbIu1cwn5XvjnlET_To1IN4n8cg7YVMwtwGc9j5sLNkr4Rw8AxRWV_WCewMatS7DNFTg9YyVu_zLsUhK9Sa87x5OsO-U3_gTqTGYOMh8vFB8t5EV_gR5ktLhfij90qpE2BUL8u2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
قهرمان جام‌جهانی به کشورش برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101329" target="_blank">📅 16:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHiwzNhCw6yeVIPPKdZ2tHdCaWa8J8vZ8VymxTtw3at5oJzvvQnhhQpn2NvTRDcuMDyFo8iNPWmUc6dosXIi-VxLsDU-XBRLJrTMloNgSUoiUau0QfuK-xHp5eOkvTyvJV5gqNc3TineI72yx_PW898S04INS7iY3ktWAdTcQPHb8kDNIg3fcuJxU4e9YI7m2B6nvpcFQWGcBt_U0l_NZH3o9XXfq9DW76vGYkZb4rI5xDvvF41wHA7jG2KsCtRPCW-ZhBMw6rhjA86ZzG_1ul7Tf-p2mGyGn0SF8VNqezEYCXSolOJ7No1DDY5hV0BUlWyzEHYcTrGAOWOA_16NyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
گاوی و بانو در مراسم دیشب فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101328" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxKaljJiovmzFFKoofboQb-dLFuJfVb5XYiM59koKYBWOFD-KByD4FpyLfMyb9xc15i8fJie9omefP1xTNDzSApyAGzMkeIfHpySwtL_ILOMufvUsKCge5AIsWpHgzocJMQ6lw4mpq_Rs-J9KNFkmGgQ_DHOGwBhc5iYpsUSLcOX4ono44PnxFxrDgaRyd5fCUEESFjLIkj3aH5HF7B96uaK-vZS0DV2qI5DDwhzsrvLfx4m6qVLhxTZkA_r0U8-6JL3DMkY9EZoIpPvZVkVSvEeA2DGzisCWhBq4Zjf_mtN5BxoYrk-p6t9fw5WdU9eT5SkyM6UN9cv7npkKV814Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رودی گارسیا از سرمربیگری تیم ملی بلژیک برکنار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101327" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=aNMvaEqBWJq8teDstJzYQQHpPT0qr1KKeaSoLqI75SIUUxidaVkb9iBpdtFVBdJVhtPqp0IzN8QTwLGCtHOKoIhLGgG3GsefsTDqk7UJ23TIBabGxlOozu_JUiCGpnUl9g_yiH4gLa5ZaXgLZoKx__atJBplxBWOf7h0hoNo-mShDatzKPua8xzfG45kHcsoHvtgS27qj8k7REQ42N2xyrdgUfJ8CNima5qElfiAucXYs3k5A78DlbReZ65gMr-OjZ6X0DFiDfiBm-L-EQMppDPlPwIRGBBBCt7lFgxOVEuS9MaKOxgDHBuF43wQ9qQOEph-R_GS3tOvwbl5rS2EAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=aNMvaEqBWJq8teDstJzYQQHpPT0qr1KKeaSoLqI75SIUUxidaVkb9iBpdtFVBdJVhtPqp0IzN8QTwLGCtHOKoIhLGgG3GsefsTDqk7UJ23TIBabGxlOozu_JUiCGpnUl9g_yiH4gLa5ZaXgLZoKx__atJBplxBWOf7h0hoNo-mShDatzKPua8xzfG45kHcsoHvtgS27qj8k7REQ42N2xyrdgUfJ8CNima5qElfiAucXYs3k5A78DlbReZ65gMr-OjZ6X0DFiDfiBm-L-EQMppDPlPwIRGBBBCt7lFgxOVEuS9MaKOxgDHBuF43wQ9qQOEph-R_GS3tOvwbl5rS2EAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خشن و اخراج انزو فرناندز از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101326" target="_blank">📅 16:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936d28a634.mp4?token=uE3fRWvN-z6S6vkVFXLEuE23kVhCSQwA9HgHhlPUfCcyLuiW6e00JeXpG6zp2UojvbmesYjB6VuBHw5dTixl43Lalx9ch2MYmIJ_zrlaF0XU__DuAI9dbskEirsM1ODJ6KBsXder6bRE9FGcfjJU8rgJ8nGJ-q7AfTXJP5Ry5PnG0f1FKFWuQnQEV_NrkrMt7ifwEOzDzw3ZdOhafkVcXH8TmzU1o1u3aHfKvDRd-vQ9HTSyQi3Xll8No2kUrQTfOOhCzqGQVTaGpomSbYS67cWQWHr2Z6LCIgEF05PRwR86UlMXyjYCwHnVgZoZRPqZEcLyY9xqpBy-Q_m2F76rig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936d28a634.mp4?token=uE3fRWvN-z6S6vkVFXLEuE23kVhCSQwA9HgHhlPUfCcyLuiW6e00JeXpG6zp2UojvbmesYjB6VuBHw5dTixl43Lalx9ch2MYmIJ_zrlaF0XU__DuAI9dbskEirsM1ODJ6KBsXder6bRE9FGcfjJU8rgJ8nGJ-q7AfTXJP5Ry5PnG0f1FKFWuQnQEV_NrkrMt7ifwEOzDzw3ZdOhafkVcXH8TmzU1o1u3aHfKvDRd-vQ9HTSyQi3Xll8No2kUrQTfOOhCzqGQVTaGpomSbYS67cWQWHr2Z6LCIgEF05PRwR86UlMXyjYCwHnVgZoZRPqZEcLyY9xqpBy-Q_m2F76rig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این ویدیو از تفاوت رفتار مسی و رونالدو از دیشب وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101325" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubf1Ogecv7K2_WUGH6VaamoKsLHPVmzVtGcIaa5T3z4ejaw3hanYGWt-kuBnJ2aQ6crbjS9EVImEEW4cAz8ecfKtdO5swgSLLDTxgly4paLXDua__q3nEwsk_KfhfEzpNJglxcHC6WMd2fDk8rdDVApZ-JhkW_oZN2-WJT6Zr3jhZcsu2JKQjNRpEZ8sefJqGpfBf-QB-EsSfMByX-Te-9hdyh6MXL8OU1lCy5rPHqyW95zDT7dAgrWa3Q0Vf25otosYk9OzQ-n0Z2O_WRgRNbu-c30CfsLEaBzJLR4H0b2jvDrU66cS-q26lWDNvtJ_8GeRMudL5_Meq5nGhmhkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مارک کوکوریا:
قهرمانی جام جهانی و انتقال به رئال مادرید؟ این یک تابستان بی‌نظیر است و من آن را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/101324" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46470a010c.mp4?token=DcGoKiraraaxo7QdYL0RQcnYAaDS0qLuu5f1PLyX75fd0kKYRzq1cC1zqQrJSxfiSoIwOAvOuFW1MmO_sHLt8Pvklx0-70bXYe1xGFg8sxGiJD7YBoJeiaf1l75iHSTync_c4ZmcWoaM38BnSFXyjBwatSr7OKAXkPwvDKLzr2iEDLgWd3g_Owt9_M4BVEWkLJKPdzlEonwI2B9d-E6FmVvEZhT1S1L0l8IPf9-p8N3HmAx3fm8p6gh0OYnHFHz8Fq5-jFOQZZHh98odNnpXOJ3Il81A418s_19qRpRMwivwyflRtsyE9NqkarBtJK8iBSmDCExL-HPLDuzYe1S1zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46470a010c.mp4?token=DcGoKiraraaxo7QdYL0RQcnYAaDS0qLuu5f1PLyX75fd0kKYRzq1cC1zqQrJSxfiSoIwOAvOuFW1MmO_sHLt8Pvklx0-70bXYe1xGFg8sxGiJD7YBoJeiaf1l75iHSTync_c4ZmcWoaM38BnSFXyjBwatSr7OKAXkPwvDKLzr2iEDLgWd3g_Owt9_M4BVEWkLJKPdzlEonwI2B9d-E6FmVvEZhT1S1L0l8IPf9-p8N3HmAx3fm8p6gh0OYnHFHz8Fq5-jFOQZZHh98odNnpXOJ3Il81A418s_19qRpRMwivwyflRtsyE9NqkarBtJK8iBSmDCExL-HPLDuzYe1S1zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قهرمان یورو در ۱۷ سالگی
قهرمان جام‌جهانی در ۱۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101323" target="_blank">📅 15:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=m5BRrK9SJ5F1fgqNJwQrCOxtr8WIBxQOLucueoi6y1M2LEHrM7JB-SHgF-SBzgXLaIwQbQENQxlhmXdQGcNz_bsFCd1gUnfSjIpQhf5wCEkNVsjesili29Irm0DaYMCXR1MCuveEwu7L-p16-syfE15TgaDAceZftskooChc2u1MOO0Zk20WUHxIy2vmZVAuuhiDUC8lfFS3G9mRiZCvOhm8a3R_ah0XE2Qm04PXblrbW1E0QXRbjbZKP2w7FaUP9adD4vSSC-mj_Z8_Wkj4WPIIDnGXmMflHCUMbr_HBDJkKDYDnXkoq3M_n6k8uQDp3VWnnl9YcCsJvXVYgjX_qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=m5BRrK9SJ5F1fgqNJwQrCOxtr8WIBxQOLucueoi6y1M2LEHrM7JB-SHgF-SBzgXLaIwQbQENQxlhmXdQGcNz_bsFCd1gUnfSjIpQhf5wCEkNVsjesili29Irm0DaYMCXR1MCuveEwu7L-p16-syfE15TgaDAceZftskooChc2u1MOO0Zk20WUHxIy2vmZVAuuhiDUC8lfFS3G9mRiZCvOhm8a3R_ah0XE2Qm04PXblrbW1E0QXRbjbZKP2w7FaUP9adD4vSSC-mj_Z8_Wkj4WPIIDnGXmMflHCUMbr_HBDJkKDYDnXkoq3M_n6k8uQDp3VWnnl9YcCsJvXVYgjX_qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😐
چه ابهتی داره سرخیو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101322" target="_blank">📅 15:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_OBkxT7xJ13LZZwsn4Bp2QGXUJAkNHFCOBoRUPFZghslMw-OvaaT-2E9gOfYCe5ob8WrGZfV-9b0av-vy-AEEjUTvjw_8tGEARWDfYpAtV_Irp8qU20hEmMalZUezDdWHmzmyaD6oiPb1reemfSYGcohoWwliHS3qPI8_295kvVoDCCsd4UrVgbqe9KNI1W7a8bUUTwxKu_qZVCd4t3LSjtH2cEC4vA7nN6KYupvKmbWa2q6ayNCFoQSjD-l6ILrr7djzq9xpXM7ouiVv6BeHLLtH-R9lrTh9NEOYXVFZg2wJcFxHuzX24M-B-HUA-5hdoqJPdFsU9qNnKrItilEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی اولین فینال خود را با تیم ملی آرژانتین در غیاب دوستش، آنخل دی ماریا، باخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101321" target="_blank">📅 15:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYluZ0vx0s2DO6EPAPsarq6VuO2EIJ5bEAbKC1JmA5Z2gRIUChJUOr8KiD6OcModfcSm98hBUkAwymo7_I_CoVR_iIFEbBZh6rrGrHMrKtDKw2AzAcCpkiAsUESkfPrF82eTwcngpPGfQevQ4zDTRR4z4iliHaCqEjwL6EtRpPfj5nrTKvU-pLdbJ8-gxpuC7rhkfg5OBzW5toke9uGtMvNPROz1qfpNFC0QjkOYACWp9pCJefb9GJHP_2HdAdKMhKrCkq_Dkavfd2vDqoKrg2-CITQra2SM5FLgKWrQm_VO4mKdw4dHkAPXFj3bfO26gviwpvSOL2lmbUBfH3nLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دی مارتزیو:
پائولو مالدینی و لئوناردو با پپ گواردیولا ملاقات کردند و ایده سرمربیگری تیم ملی ایتالیا را به او ارائه کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101320" target="_blank">📅 15:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=bDMX94weteg-CD-3GkmOln1LoEbycZC90wk7lmTB-TmdK9xGG3I_CZsx1n6JgNtjC69EZSLNFyFG0IFxF08OZ1OHE9AgpoySADREY1WUMAPVd6z-nRhoWNPYqEsj3aRQBr7eDxyKSNylQTdPRR8xmt08aTVRVZVxFQo18v8C4PyzlEE6Cqw89C7E9Lpw-fvIa-AERl803YfJ4U_IZEQa6XLNtCh9SmwqzE_PYRfhE9JUHaifhbFg2kMmxRKLpYeUJsbomHHZVD91-oFyC7hmyVaZEfZnI-GirZ6UtUy3pwWqngWlb-Me2AuKy-wt2VoTk9ByGHiBl6dO4_vumSXIjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=bDMX94weteg-CD-3GkmOln1LoEbycZC90wk7lmTB-TmdK9xGG3I_CZsx1n6JgNtjC69EZSLNFyFG0IFxF08OZ1OHE9AgpoySADREY1WUMAPVd6z-nRhoWNPYqEsj3aRQBr7eDxyKSNylQTdPRR8xmt08aTVRVZVxFQo18v8C4PyzlEE6Cqw89C7E9Lpw-fvIa-AERl803YfJ4U_IZEQa6XLNtCh9SmwqzE_PYRfhE9JUHaifhbFg2kMmxRKLpYeUJsbomHHZVD91-oFyC7hmyVaZEfZnI-GirZ6UtUy3pwWqngWlb-Me2AuKy-wt2VoTk9ByGHiBl6dO4_vumSXIjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نمای هوایی دونالد ترامپ از استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101319" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwXKJa6JFOU9Recr8_K2QsYlVVxfyEd2rAW8DKO9fwG2LmCzohE6oZevXS2DhYA7RDrwUvaaa3OQuk7RLIXt78MBfUy1_W0W6ZULXMk5fNfSd-SJU2Jaarxs643l59xbMpSds2f5XOmU7GTqvlW6V7MVaFUwMMWq1gbsP6wazT8riQbiNLMbr7K9WYKcSpfLHT3QxOlnmEdmnE4PzV3mvP7-KmuniuwAqi7j0m4m3kVfh_J4b1GOYJ-9gz4CFep4VxzMNol8c1Zp7qN0RaySzVTmdp55prxESerQFagFh0mZlIHf2H-Ll3lVqLXG-JgCL3qj5xXa6q2nfK2CPvT8_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کیلیان امباپه در فصل 2025/2026:
کفش طلای جام جهانی
کفش طلای لیگ قهرمانان اروپا
کفش طلا لیگ اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101318" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101317" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1S1xL4LngVTeJGnozEXcGRF2cYr_wO66LIUmrP4NJ_cHvlHFXuAe5QA6TdU8EzAdvUsmeacW-1oC8oiSskaLM788Gt1OWajMAEzAEtccuWgj8D5g0Vv-F9h0lzJTn1HDha2mlN-co-5xB4-YMEcXVnp8xSgr-5RQ0kAhkRwOQrt5YT3og7RKh3hbl3UW1nd6jL8J7VtT5JyzGT4wY6sdnqOeRmPTnEzfhqAgWW8bP_6gVdeeRv_L0857jOPSwRgS9BybAlO0zhUcTigGRE3_GedYQ6H2d2pIXidq0NNO5l0r5kCKYpB3zzqXF31gBk99WGTvjts03gVH750C17ETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101316" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=Oqy95XQaKTJEW_3OXAlu9aXWMF33nzTFqXW45CzRK1xU3VjUPWanq0mkKWuy4UHkrNDygt2xe2XyZXXVULRSKirIyHaTmoZ3XzoWInwJ-FMcu14eWFOAUp8EiUVb4BrJRqYEiIn0k0Vl1HXhCCa_klgzjsmfm7sLdZBv8540Iq5nFfGibCh7xI-hJyR9eMaE0B-iL6QETkuLnXH4bObPAf1Nr4_Iyy6BlfOXSagPl5RPkM4n2KeCmN9a61DEmRh9ER87kS7Ocu232A1aICK82ZdmCcx3_feIG9khBUT4Yy5prwh5OEQIaw93lTmKdbJ-NVX9TjsTPFb3W3doBOleLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=Oqy95XQaKTJEW_3OXAlu9aXWMF33nzTFqXW45CzRK1xU3VjUPWanq0mkKWuy4UHkrNDygt2xe2XyZXXVULRSKirIyHaTmoZ3XzoWInwJ-FMcu14eWFOAUp8EiUVb4BrJRqYEiIn0k0Vl1HXhCCa_klgzjsmfm7sLdZBv8540Iq5nFfGibCh7xI-hJyR9eMaE0B-iL6QETkuLnXH4bObPAf1Nr4_Iyy6BlfOXSagPl5RPkM4n2KeCmN9a61DEmRh9ER87kS7Ocu232A1aICK82ZdmCcx3_feIG9khBUT4Yy5prwh5OEQIaw93lTmKdbJ-NVX9TjsTPFb3W3doBOleLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ دیشب طبق معمول صحنه قهرمانی بازیکنان اسپانیا رو ول نمیداد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101315" target="_blank">📅 14:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=GEFeGp39KQ6EsMkvTtb7NIcF4JN3yW13ERQmZbEk-0lIvUi4_Ubc6j6rVuQVJFrRuoGWR1JTN4fTq5zfOa2UJcgh3qp_SISxbaj0aFD0WwJskaKiHZwcDjyyu0e2Wookwcsp-xtLGKc5ACi1AzOMXLq9DNLZQp9Soi4HUc2Ow4mnRAjetzW9J3J8HxRseES6g9qLcn9tK7q787X2HozaMWJcBQtXVUZiFPnss8aV8Kfx1yEqLSZONtEDjTvhkGA6ACl9392T5A4q-zSbAma7ffvVHiB2jKCSXhd60mRFVlWjhmmsOXua9HwUddxw_jDwQuLqbik8VAj6hXyba3pyWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=GEFeGp39KQ6EsMkvTtb7NIcF4JN3yW13ERQmZbEk-0lIvUi4_Ubc6j6rVuQVJFrRuoGWR1JTN4fTq5zfOa2UJcgh3qp_SISxbaj0aFD0WwJskaKiHZwcDjyyu0e2Wookwcsp-xtLGKc5ACi1AzOMXLq9DNLZQp9Soi4HUc2Ow4mnRAjetzW9J3J8HxRseES6g9qLcn9tK7q787X2HozaMWJcBQtXVUZiFPnss8aV8Kfx1yEqLSZONtEDjTvhkGA6ACl9392T5A4q-zSbAma7ffvVHiB2jKCSXhd60mRFVlWjhmmsOXua9HwUddxw_jDwQuLqbik8VAj6hXyba3pyWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🔥
وضعیت کریستیانو رونالدو هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101314" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=eoBUJ5AdG48ixUm4a3weYVSQnwpxNKLSM8xfqdJZi-WKNJtr_NVmaiwrbJerInkpc06T_xOiG04K1vPpsBOt9i6SXMWJs8Fa6HNzXOd-lTW-d8ygVF9e0bYwuSKTd4MnyaK6NQ0G_gpA3F4TTTi5w_Yt5e5r_8vLwqzByMRvDHznj2ROl3wLwnIuzHJd4ywo2vjqU7uKNZtBcr1t10z2g1xtX_VQCBgn1mPPouisZVyCPZdoEWwOFCxwo768WXg-aMpmnolSmQLuXCDKEkM4jkHl8tTUtkYs7KRl--Fi-HbZ8WOeKYzTrZL5yVsYG8-vSZzTPm3hkEwqTaCNtmzSXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=eoBUJ5AdG48ixUm4a3weYVSQnwpxNKLSM8xfqdJZi-WKNJtr_NVmaiwrbJerInkpc06T_xOiG04K1vPpsBOt9i6SXMWJs8Fa6HNzXOd-lTW-d8ygVF9e0bYwuSKTd4MnyaK6NQ0G_gpA3F4TTTi5w_Yt5e5r_8vLwqzByMRvDHznj2ROl3wLwnIuzHJd4ywo2vjqU7uKNZtBcr1t10z2g1xtX_VQCBgn1mPPouisZVyCPZdoEWwOFCxwo768WXg-aMpmnolSmQLuXCDKEkM4jkHl8tTUtkYs7KRl--Fi-HbZ8WOeKYzTrZL5yVsYG8-vSZzTPm3hkEwqTaCNtmzSXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
The end of an era..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101313" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101310">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSI3M2rnbrfnwAag4iisiJtBdhOI6e3lBDXGvzClKdMeGbLkVfaVojI5ZlvyYNmmGlXp50aTAGRwMVN8a-BUBccT8ghRCy-hvQbup-R4brdWiDozdLxaHFMN1GZTnJLghKs_TTDVEHLm8ZBrHnwMD3dcfls9F2KDJuZYRMtBifL9OuZJewXsX2uSTmITVEoAPWPS8Fs9_rMGyt-gIU79eA1miHaJWTOBODpcSfXE_cbesGVVsS4MELS4QvjVuUSUdq5CJ_rio2RfjtM1WkFdIf5eVI0MtfQ8bre8oXx1JUPUfYnJF22GylT0AMBNut4-qJNwDe47Br_dr7KPZTkEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ke-RdnBeRH3Sg8swG2Qnb3sxT_kEZaQUsKa5SCiT2ztkBrm1VWNAld3_ihI4zonQSkI0GnXCWtW2doTulHMRjpAfbMa0_v-KlgRowthEQQblQSzg8rJ4MqVvq2rUh49a1AuLKIjEndkmBuaYlwh-k4v6MfXdnGNpcIx4QuXgtyZ1CKnZzHWUohy3NfNgb-0EYMY3ozT69oGl03WetwpkqH3GnBvTemTJVq2ZR3PWaqZysuzU7nYIRCZJa6BJ32AUdViXUdIM6jDFUoiZOS3nmrIa_FDkN9WDPhI77aFoUVEFSY48openyasfTpdcYJH5Tdo9jPr4Vg8CmldlbjVkxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6w1M5X8uKPE6xFxA3LkAoxUzYBABCw3tlONno5PS7dE8tZTaASINyjzWoPuzcoTI8Q-_IAYejggEF_1YMLkY38T-tZ35otM1cbZuZzzzDgFA6GB9IO5OqIf_jat_7p5kTZpQ7LR4v4kyrDYwSiv330Yq1jygK9JLnll6GWiqx-ZTj6V3IM-q2OrlGDqD9lveXWqLjOyDnE_Pm0RJ78Oq62Bu35694LisBsocwpofYIb_PQMsGNLEqrKe44Rj074iXao0ipuBu4XoRpcDyWGAr3G1lCDXY9x6qXoyepG0J04euMMHKLoPkU3JcKavG5CnPsargKdBmmBSUtDIftReg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😆
🔥
کوچولوی دیوانه رو داشته باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101310" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGKtrkTbtstCFHxhmcyDgOaa7Xx0UML6MKwIFRgZ2dc4hZGVfY6t_U5SC_zfxGL-CDIJZjdrtAxn2_FnzFrQOP41p2b0kzSGlkXEPMVXH9R33hDFpGteEqcA9JewF15Exu6Atnfy11e_oho_6zxRkBuOt486fMFYJn8-M629xaA-JKvFeE7Og9TM0JVrd4Bk3ryjgeeLXHhrRW8tFkfKAnUmhi7CrwbGqqeCV1H9QDWKuhy-hqc26MBjiicJORchAKoK9iySv9cgSybR9pQVRfUCdAaC3pbpJi4T2_8MktOpoKoFjLHcsDuk-tuaUW3ujvm2YOrJOc1-NRiMl9ZmRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
😔
🏆
تنها 1420 روز (34,080ساعت) مانده به آغاز مسابقات جام‌جهانی 2030 فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101309" target="_blank">📅 14:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=skY-rrVMpHuH663vmg1GVEyf0IkaqdUXH77vd8YAX-NXVZy2c_eySdfR6c9NMhTHCN_XBIawVXL2dt51efwRMtwqv5pyioyo-MKxjnAxrlvveWoUEz47PkWOmwdJgpnLAiIjSM9zlV-pSzbit7zFd8QSpfzIOqq1E_Gtt3qi52AW9R82Np5M434nWeg4CU4rCfnDabnU1nUUGn8f8kRdMLteHorXgWfV7_6UgGcGzofCdh1LNk8XsNCSCLGxQ7fYwS8PsRTFCvsB9M2IOrCpDAbYUUFbv578izhyKMXKpDASLwFD5M5hA9zS0RrSJrQnOWRV6Har1Ml2J-cz2KnoFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=skY-rrVMpHuH663vmg1GVEyf0IkaqdUXH77vd8YAX-NXVZy2c_eySdfR6c9NMhTHCN_XBIawVXL2dt51efwRMtwqv5pyioyo-MKxjnAxrlvveWoUEz47PkWOmwdJgpnLAiIjSM9zlV-pSzbit7zFd8QSpfzIOqq1E_Gtt3qi52AW9R82Np5M434nWeg4CU4rCfnDabnU1nUUGn8f8kRdMLteHorXgWfV7_6UgGcGzofCdh1LNk8XsNCSCLGxQ7fYwS8PsRTFCvsB9M2IOrCpDAbYUUFbv578izhyKMXKpDASLwFD5M5hA9zS0RrSJrQnOWRV6Har1Ml2J-cz2KnoFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکیرا روی صحنه ورزشگاه، پیکه روی سکوها
و ساشا در حال تشویق مامانش، در حالی که شکیرا روی صحنه غوغا به پا کرده بود، پیکه از روی سکوها فینال رو تماشا می‌کرد. و ساشا هم با تمام انرژی مشغول تشویق مامانش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101308" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=UM3Y3YNDfMy22v8P495cFWmND1-blbxrlawGkPfRKZDAH87EuuHhnPQJV5FUjxh0awlbssoCleJ6p9JA3TzCfn_IwGnHjrrOv2Y2pXRwsby11QgejcTiPbS1DpuVy9M0jzwPcGni_Oh_Ewb-YDT_LkTiIJYGHGAW7gNbF0PenMzhOqlE2z5baUyYBDdPLdtvaPZaqdP6Jr-txP6c-CgrWi0P-Y6n3vck1fSAVdu1DHw5dAY7okqGeYNzYA27nDGG6h84nTW8GcAPlj95Oy7U1j3yyH87ITP9rZ1HuAH42SCNv02TK_ooPSVrJ6Zx9xUUuM6gLheS7eQyhsGvics_YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=UM3Y3YNDfMy22v8P495cFWmND1-blbxrlawGkPfRKZDAH87EuuHhnPQJV5FUjxh0awlbssoCleJ6p9JA3TzCfn_IwGnHjrrOv2Y2pXRwsby11QgejcTiPbS1DpuVy9M0jzwPcGni_Oh_Ewb-YDT_LkTiIJYGHGAW7gNbF0PenMzhOqlE2z5baUyYBDdPLdtvaPZaqdP6Jr-txP6c-CgrWi0P-Y6n3vck1fSAVdu1DHw5dAY7okqGeYNzYA27nDGG6h84nTW8GcAPlj95Oy7U1j3yyH87ITP9rZ1HuAH42SCNv02TK_ooPSVrJ6Zx9xUUuM6gLheS7eQyhsGvics_YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
اساطیر اسپانیا در هنگام گل‌اول به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101307" target="_blank">📅 13:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXYHOv50bVoLkep-qb3k3Ze4wEiPGIjz3QSijwBRdaDW6BBitBv7qovS9uoPCzueoc1u9nJR4uuJErY0sNyjrdyvQGN-erKTUpel3qX1dnM1JdgvlxiMljNoLrUi7tqev4op7ieNEPQa5d0_OzVa3593EfWJDBd89bE84TIfIvWiJlWI5zjLVIAsMiNBf-nBuFl-dKRNc-0-yuHNfRxo_pYeZcdhVDfqhlP-drUXbv_W3m0_Jxu0E6M7kGXeXEtoAiMDX37HbcyPNXaqqzi_A70SOrU6WusK2jMUM5NvROiKWQsaCWEWCXTloKYvpxsdh-DPueogkrKN_mdNyVLsZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
رومانو:
رم در حال آماده شدن برای سومین پیشنهاد رسمی به وستهام برای جذب کرسنسیو سامرویل است.
پیشنهاد دوم به ارزش بیش از 45 میلیون یورو نیز از سوی وستهام رد شد اما رم قصد دارد امروز دوباره تلاش کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101306" target="_blank">📅 13:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=FpPgA5YIxia4ztIolNWI-tuaMIkHd2Cx7EC_HoS5et5Ehgon9JXxIqvml0HfL3jHgNuC6-PP4VF0ZON3XGSNrQnG_OeqCYgUlRxWcWS125N6cLRb48hsu6kF1dXZ-c9l32wx8znxrQ37Mk0-Ey1d0WWHg84qjmGYrt3cvM17n7308n9r655VeHAtuLWx2GoZqACLBJanbhDrRwdEL_4RC7Lh89-tJoXM_WXHNXqw62Z0QyqvQXLza42f0_rGn7scArQvpZKB1KJWRcvlshaswCFrnI8obSsC5Iz2JBpvQos1sSAyTnK7lPo7Hnk1Jt81jIF-ixv4st9TQarRvbxl_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=FpPgA5YIxia4ztIolNWI-tuaMIkHd2Cx7EC_HoS5et5Ehgon9JXxIqvml0HfL3jHgNuC6-PP4VF0ZON3XGSNrQnG_OeqCYgUlRxWcWS125N6cLRb48hsu6kF1dXZ-c9l32wx8znxrQ37Mk0-Ey1d0WWHg84qjmGYrt3cvM17n7308n9r655VeHAtuLWx2GoZqACLBJanbhDrRwdEL_4RC7Lh89-tJoXM_WXHNXqw62Z0QyqvQXLza42f0_rGn7scArQvpZKB1KJWRcvlshaswCFrnI8obSsC5Iz2JBpvQos1sSAyTnK7lPo7Hnk1Jt81jIF-ixv4st9TQarRvbxl_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
خداحافظی جواد خیابانی با مسی و میراث مارادونا با شعر مدونا: هرگز انتظار نداشتم اینگونه شود، برای من گریه نکن آرژانتین، حقیقت این است که من هرگز تو را ترک نکرده ام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101305" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcYrkk1fMEOrWnytYoWHR9tWk7H_ZfFfARjGouiesdrsy4papnyiqC3UkN_rJfZCEq3Wc1BznLnu60RI1G_3xJKzGT3k68_L2586g7malFONrKKC-nXMf_kCPDUBhC8NzlTNwmAbcGXeOhb-GyIBvIyb2XYUMCE0CoxzJgpBlq1HZb-tCR1QDTeisala7n3lip1SDl4AVhmvmhq67nSNyYkI_TtS32T61G_dpZRA49vS7Uy0ALjGrLgCQfQuWfAaNrQGWF8-L8QDWNtIVMzio4HWTMn0DS0AhYUSRJAZXuNmJDrsu1Em5x9fAQHGyXPOtDZr6jYpZiqWKfiZCRnARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyvT3g1IZcMeguRyse6R2DilUiRM-Foh1fLmslXRvBgBBuNBerPipBIXXKlhJJXd4Kzfd6mMKZo8QpaPvwFg21cYFvw37xj8YO3HyypqX-R0xu6CJxMq4z1U47GOaErlTDtyN-r5u2oDfVX8xsEmUjZ0ZK6wxoaQB4KCrrL_U7FHEfYuHcJOlanJPxSf0fFGlCdCIt0sDoq7MnoUfEuPGr35xJ2LPtHtdkn-FTg5P2Qv1eLHndiKf7NZeHCggc5Z35Ox4UyvfHmvJy-xOlPq4xzRGnn25xPh9luqi2961-1AtAlYPdKoSz_zMRwk_-_O3Doa985-_r81Z8IXBsRbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmeCdKuptVleB2k39uy6CgkaTKL1gaFr9Nb-IqXI6jhvx5ej1uXSj0GK_DO2iswbspwaqWQT9ZoZD6dBkqA-UTppeuQJU008pVeW3xzI8uri-AvIkRYHM2dauJjIRcrvSMdJKg7EE9lKrpPyrjOvNhFt8_RjI7WdeP32LQT3jkmVZPK58lVwheUJ95F53FHs1jqiYC2Vw8SucU3ALn27y7xWXsOeQktAuLsPypp7Rjn95ed8_y_x7VUXyrCl0PgbAaYziS2aRhkEIoR242kfFNlBY8E-gV4dfW7gkPPTh1qEGpzg7jhKe1ypocfB1C371inAIpCsTnzJ8lc273YLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEaPK_nMydDIZrJtnVAtuKQEX_w_B-By0YTFhKTSLrYtoYzdWKeluXUTkYCTcJlYEWDkbQmJlROOKtj8MWM1FcFyKYQWEC-PAgKja5HD30tswGOMR0HPAXsVpHsfllTDE882dlBzZc-pd5_amQJQHUTkB6YoZGmunF3XibBIoCjkJahHEBQcTy8ehwhFdb1HyovQxTKm3a3PnZe6-RcX7e3KpTIMcMzMPscojizHYyFDRNDozc4FfdijXFvgVMbItJa6NzMym2KpXkZOxG-2tt4sa53hpHWwT0ggfg1kglrBRlsm-BY5JGx57U4sPPOOK3OHwNEvePVcWnbzZgb4sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
👍
پائو کوبارسی ستاره ۱۹ ساله اسپانیا و زیدش بعد فینال دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101301" target="_blank">📅 13:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=vU3ZyT6sFDqQfH5Qn7AlptiIP0c5_3YfvT0ujknm0TjdtvsWRF3xsjQdoIdbPatkm0jpIeXo3kKoH7uxbKF4YrquTsGbieBen9YPPs39aj7KXHoLZES_vIj_x558Nk8psLeA6_j7WGl-jw7FUbxZWa53cSQ-p3THlZrN97eKxAff8tjQESQ3iLiPqSZ3xgTjNyshuhArFXBkG4QvQ7myPoQKnkBG6E9Vq9t7FdvhJKuM5WwpKgkwVx6Y1qo-7vV5H0sErjHGHUZCiKj_lAlELteZ81xOLGyn95qWZAnQTYC-Fn4oPU39rQLm503UjRnGyZ9Run9y9oWQoRnkDcwuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=vU3ZyT6sFDqQfH5Qn7AlptiIP0c5_3YfvT0ujknm0TjdtvsWRF3xsjQdoIdbPatkm0jpIeXo3kKoH7uxbKF4YrquTsGbieBen9YPPs39aj7KXHoLZES_vIj_x558Nk8psLeA6_j7WGl-jw7FUbxZWa53cSQ-p3THlZrN97eKxAff8tjQESQ3iLiPqSZ3xgTjNyshuhArFXBkG4QvQ7myPoQKnkBG6E9Vq9t7FdvhJKuM5WwpKgkwVx6Y1qo-7vV5H0sErjHGHUZCiKj_lAlELteZ81xOLGyn95qWZAnQTYC-Fn4oPU39rQLm503UjRnGyZ9Run9y9oWQoRnkDcwuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما با دیدن این ویدیو یاد چی میفتید؟
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101300" target="_blank">📅 12:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpwg2MyBwqDN6jC7IQY82S3Obh4gDn95PYcKJFnB2oj_ky3YBnPLWs1Ze9Edznq_oQUjYWyBO2ZtaDPqjkdhzrqwTjYe4vkfF5omRPl5k1w5xzbtWYs9EZ8C38mHEgu5n0XRuF-892v1nPPzmyF2zC4U9dSp6oqmgRX3225eYK1arANh6sdP0WjWV3Rk1CP3_kykJ6_Q8ClQUh2wIFFCVQ6Dp1-xBZEV5z2cur9DRc7SV848YQsD1VYcKYvNFt1AuRb5TsFhLWelvEcvA42xCXII__wAEVU9gx3gLWGkhZjG6AaXCpXcg2oV8LIEL_xVsaPETxAih6a_CiZSKgHw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نوزادی مسی کونش رو شست
تو دوره نوجوونی کلی جام با بارسلونا برد
تو 16 سالگی قهرمان یورو شد
تو 19 سالگی جام جهانی رو برد
این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد
این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا ازش بخواد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101299" target="_blank">📅 12:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=U1-NiThxVxsiJpMtAfWANJbVRcCFJ47OitO-F03hGLyzZ_s5Y-GQRNaTth9hdC69VIGJ9zU8qiOUSsZtFmcZNqoOJwfgrO1-2lRNC1Z0OSjb_KHc5OCAzYvlj5ko9RHBWtdIlSqeEDAulkEG2omMpugVLifq1l4gUKBmNas9CU-Qio1h9OBEDbQnTLjdTW2gqLveDGYCHLBmreA3HtVZCMzaKKLWlPoYa87H52OtkOJ2BUKIyIOxJo6gMPBGQcis4AEDmjnk4dHLiJ70iw7O902qqDtyZj1OjtKr6AEoKK4PlSdE1dMyGZpc1xIUjaY38nAFkxdtgiMIbBrW2eoi6HjQAXDlq7FwoJnjlXQR-1p_MSzKbXDPWTYU_y0frpBgRSGOPOOrKA4j14XMqYGABgP1RMehALpk95PAg3t378l1ShMq7KXQE3WR50VLMzMQTcHGsFK8aYwM234Oe4vcCxN_yJdVUXkrZUUQdMGH7cyG7XGWJt6nT_MNu7h4wM6QQAbeNaaYYKL_A06gwTyqXuPqIKKGQE7xIKZn8QXmfV_79HSpIQYAEEEF1OP8yuR4jj5hizsQG02jvY5G7_tYRj1dkmifT3ihq8DVUBT1bhJvwF7UT-EJkfsPT4qeSjwtHPnSXpGLyn0epclEqCa_Xtkms1bjwqWYvrlnp6Tsdug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=U1-NiThxVxsiJpMtAfWANJbVRcCFJ47OitO-F03hGLyzZ_s5Y-GQRNaTth9hdC69VIGJ9zU8qiOUSsZtFmcZNqoOJwfgrO1-2lRNC1Z0OSjb_KHc5OCAzYvlj5ko9RHBWtdIlSqeEDAulkEG2omMpugVLifq1l4gUKBmNas9CU-Qio1h9OBEDbQnTLjdTW2gqLveDGYCHLBmreA3HtVZCMzaKKLWlPoYa87H52OtkOJ2BUKIyIOxJo6gMPBGQcis4AEDmjnk4dHLiJ70iw7O902qqDtyZj1OjtKr6AEoKK4PlSdE1dMyGZpc1xIUjaY38nAFkxdtgiMIbBrW2eoi6HjQAXDlq7FwoJnjlXQR-1p_MSzKbXDPWTYU_y0frpBgRSGOPOOrKA4j14XMqYGABgP1RMehALpk95PAg3t378l1ShMq7KXQE3WR50VLMzMQTcHGsFK8aYwM234Oe4vcCxN_yJdVUXkrZUUQdMGH7cyG7XGWJt6nT_MNu7h4wM6QQAbeNaaYYKL_A06gwTyqXuPqIKKGQE7xIKZn8QXmfV_79HSpIQYAEEEF1OP8yuR4jj5hizsQG02jvY5G7_tYRj1dkmifT3ihq8DVUBT1bhJvwF7UT-EJkfsPT4qeSjwtHPnSXpGLyn0epclEqCa_Xtkms1bjwqWYvrlnp6Tsdug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملاقات اسپید با گروه BTS در فینال
🙂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101298" target="_blank">📅 12:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242475ed92.mp4?token=g4aaZ5YMb51i0AJF-u2Vu3W-LZ28XH6v_woqCIDHJ4sct3qwpjfDTCB1u7X8pb3XGiL7YkNVgrxRkMxlZBq8j_JdI9HFrrqrmOoo-GUSXalhNtihNcggwJQpqEvpjJyWtV7wkZXDK30iGOjKfbBoLfN95UrXehjAf5XenDBG09cEYxco7hyVHJ4tozzrw9QYOvidyZ4Pgk0IARpjXlNVjfIcQjVn8ON3sCWhBhZDiQeAqZI_EmRc8J5TAQBsR-kfxy5-M4kG9Xl465y1ID-DFApE8VL37hGgjSf4E8jeWKYw1dtzv_V-YXdSJhwXQc6UxeT8xYnIzfYwvSiNNbmEzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242475ed92.mp4?token=g4aaZ5YMb51i0AJF-u2Vu3W-LZ28XH6v_woqCIDHJ4sct3qwpjfDTCB1u7X8pb3XGiL7YkNVgrxRkMxlZBq8j_JdI9HFrrqrmOoo-GUSXalhNtihNcggwJQpqEvpjJyWtV7wkZXDK30iGOjKfbBoLfN95UrXehjAf5XenDBG09cEYxco7hyVHJ4tozzrw9QYOvidyZ4Pgk0IARpjXlNVjfIcQjVn8ON3sCWhBhZDiQeAqZI_EmRc8J5TAQBsR-kfxy5-M4kG9Xl465y1ID-DFApE8VL37hGgjSf4E8jeWKYw1dtzv_V-YXdSJhwXQc6UxeT8xYnIzfYwvSiNNbmEzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با نایلون داره جام‌جهانی رو میبره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101297" target="_blank">📅 12:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=OszNyOe4N_rrRXbpOgfBcQ0oOSF00fM3r95AbPRJGfQoolSLs9ncq2esyzCnTIFaCCt6j9OgsSrt4yHElQ4pPgIKYS4TlLNqmDl-ms_TPI0chmCFRUxQmlpS4gNmGnyp6Co5ieMkGaboBGF8YAobfCguJD3AuHXky78nqNVKSeWXtAc3BJALxx4vCTOxQShpgwPsn56e8RKrlMDOBfBOUinIXtpu-FSxa46QwK8nT0BBoTKnccVmQIZkA5PUKYGRSFna87q1UOWcS02J8DZ8aHCCZ0nblHG5TYVbhWZZ7Gi4I12hS-PtNdEZ3FCSQ5yc_M_O_u47Ga9rGUsurIL8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=OszNyOe4N_rrRXbpOgfBcQ0oOSF00fM3r95AbPRJGfQoolSLs9ncq2esyzCnTIFaCCt6j9OgsSrt4yHElQ4pPgIKYS4TlLNqmDl-ms_TPI0chmCFRUxQmlpS4gNmGnyp6Co5ieMkGaboBGF8YAobfCguJD3AuHXky78nqNVKSeWXtAc3BJALxx4vCTOxQShpgwPsn56e8RKrlMDOBfBOUinIXtpu-FSxa46QwK8nT0BBoTKnccVmQIZkA5PUKYGRSFna87q1UOWcS02J8DZ8aHCCZ0nblHG5TYVbhWZZ7Gi4I12hS-PtNdEZ3FCSQ5yc_M_O_u47Ga9rGUsurIL8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
جملات عادل فردوسی‌پور درباره آخرین بازی لیونل‌مسی با لباس تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101296" target="_blank">📅 12:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE7FWcM0I8dJey0Nu7yIcqk9jBL0gNC-whKKhmR9TCnPXx84WvD_Q_2O3Twmeh2iVjj5DBp11FWZWceS-tm-dE8w7DNCw688IG3XrkmFZfmPUUyvzyU79U9iNYeJKZfKRHBkvMeMekmdUtPTawbKTyPqMsG6HHVWXBdyfYmpwSlvu9h1BLTIa3knFNwHovQJ1eYpTNUSLnqBKKpiaFsJgMJRGqFgayeYSK-l7OoaThrXE0qjlGhP0J_R4LTnfp7VMPt2FfBt9dSjQNmcUOi5-6gsf2xzH85-wR6tTxx-o42o2A0dRYfl8T6ORmxFOTC80Se1TLOSPEuoxN3KAyHZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😢
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101295" target="_blank">📅 12:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln5jV3xM5HwlD_1Q_dfaWdh1YOkBfGXKUCvZKOAp_c98M5ccaHXRErF0LF2XVubK5EHhZ5B6GREVeUDItBxrPLI3FjaPAIDFgrJWikHaeusHEfP0VBxYJS5nBZ180EgQJZycqr-VGCwxklRHEzmGkrE-28Bgu71ksAD0y4dauCnuqYmKAAI-J6UNZxmpFutYpm8CHxWKlGkAmRRjSmSnkblawK9RqvB6uYpoAU8EfNNsAbaEWv73ALSGNMbhOJe9WcNHNhjvW_qz_YUVic-qlL0_NVxPjM8wYkyWaLLLbX_NHWr--AUizbv6jdHXHdVK3MGKHqcdUjBbH97yuktW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
👍
لامین‌یامال و بانو در مراسم قهرمانی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101294" target="_blank">📅 12:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9dRi6G5upGGG_GoS7ja0PtsFmDTrqg031JS_uBICllsY_SYiHFq96Ez6y3iivXOdF-Z-LqrMmALXewh04nNsCkY-RItHbdu0SuX3z0ngJh6XVO_cbwwqQf5NukFC2Y2F8FkOc-AhKOZ3oI5LkoxoFDoQaIAbfwM_ZEZhv78mQC3VhZJ9oFtozzDhYF37Cv9B88nSFlj75Hz4aau0rHM9pds27VZpEWUOowfjD25GlrCm1i_M7qXaBnk1-RH8rBtE4EaIiEpayPhQSUGTf7GAXEFiNNxM7ZBLV5eA5hx0wy0Hcz-MLq7DK2DjVX702nxpcWKdpEt1aYRT7ViQzkKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام‌جهانی 2026 از نگاه سوفا اسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101293" target="_blank">📅 12:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTahRu3vG45Ezwt1_th2QSzlub0gNsN3csR7JB8-0uyP_5LXYjZ7HuvQ3V2tVriW1U0J6mx_QMq6iKrok2ttagcevho44C2bIqh_xTcQGVf8wGfzTJwZ7xYpkdhrA6cKc57FtCCymjJ-4btjG97s7mkVO2OpzhLKg8vn0arKd5B0RBhRGn-wGF07zCwb4MDTU1lRAK5YXQDsjjdZi2T0nE14YUbEZNwLuSHuHObOqgQya7j1i-dZ89t3v667-zAFDzI6OU6I383cdT8BRlNMn_XbqgCeFD1TMAhIrJAvMBowuu95CM2556-EmPzlwFFCTWraa_SIuVn8tZ9HoL2fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وبسایت سوفا اسکور برای دومین بار متوالی پس از جام جهانی 2022، لیونل مسی را به عنوان بهترین بازیکن جام جهانی 2026 انتخاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101292" target="_blank">📅 12:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su5_htAznFZ0z_QE0hPfDkUkR8c2VHFwUXZ1EQlOCrTkZ3V33Oz9uPgGntdiQdlr5nISKRVy38_JSPsXL82cgYkNyjhfm88ER3hqrn7YiurMv2DjJNRy0WDQ0bRiJIw-IIAyof_yH6KBINdq2duGqhhSLtbyPsn3TaV0AFIJCzS5N3Fo-W1NrMzc1lCHRbKyXPoGGQfpd_slWV4kRrlVB-v68XWXGW20-bakLn99JSf0610wQSJ0-cbmy7bOsXWKtSnEWD7GihZ1zSF4WVlfpU4M8zEdfzr9tl9t5wJENQsegZ13N9oEyb14jRwk_AtneXmg7gQ4cc0uy8JxUlu2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
پرزیدنت مسعود پزشکیان: شادمانی ملت عزیز اسپانیا، شادمانی ملت و دولت ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101291" target="_blank">📅 11:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fa95c026.mp4?token=AT5HYEIyGc0TlI-c7wdF7UW11YJVb1XwANDRPwj82Sf4QA_mFbfaosoLkODiv54xCJ_XvRqTmA248M0_k1xKLjTUCUg5Q-N6w1hy77eakWuRYCCumpwbocEn4jW-juUlOnF3D2AHDFdKJRQNJwbQCRSBB-4Wbl_yLvmgwAyjSwFDRKBtF8IXOi2g4ddRTpt9dgt-RkPv2Y2uMIOg8PSYhU5JQWGu3ry6BST-nw1bazBPR01Z4PU-RdraNbmNdw7IXsTQp7y2klHCzWn7ele45OBiUl8uYre3mQhrIYYnNpy6RPcLjP5bKq2jaDDvC7IFwy2ccExbiBkYorvNhoJH6lVqnawsi-ZNeM1BKjeRzyrDK-DCjLdGb2NdHXz59aELOzIktiDD3Rt_LJlJUQH9l5Xq39SfxyASB0iEFPzEuCQISnrpqpGl_vZzawZfIrEWn6AvmO4anK4PbhpUmlqfpjmFfPw2ypY_c_WsAPFasTSyxGbB7LnibKAw4FTHrTlZnKrs_4FdSLrVbHjE_WnHN2dXrGHBzo7hn5HaK0VY6EJcfrHFBIDO_dAjH6vucT9nt7Sad5kMkDMdrRMyvxg5M62fNSLcMg7iX9K7gQnAJnALXsk1BJtU8PYtffksFQOtd-hydgzRMCyq5Jh1wNOx6P4HSO__hWh-nE7DbLkV-wE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fa95c026.mp4?token=AT5HYEIyGc0TlI-c7wdF7UW11YJVb1XwANDRPwj82Sf4QA_mFbfaosoLkODiv54xCJ_XvRqTmA248M0_k1xKLjTUCUg5Q-N6w1hy77eakWuRYCCumpwbocEn4jW-juUlOnF3D2AHDFdKJRQNJwbQCRSBB-4Wbl_yLvmgwAyjSwFDRKBtF8IXOi2g4ddRTpt9dgt-RkPv2Y2uMIOg8PSYhU5JQWGu3ry6BST-nw1bazBPR01Z4PU-RdraNbmNdw7IXsTQp7y2klHCzWn7ele45OBiUl8uYre3mQhrIYYnNpy6RPcLjP5bKq2jaDDvC7IFwy2ccExbiBkYorvNhoJH6lVqnawsi-ZNeM1BKjeRzyrDK-DCjLdGb2NdHXz59aELOzIktiDD3Rt_LJlJUQH9l5Xq39SfxyASB0iEFPzEuCQISnrpqpGl_vZzawZfIrEWn6AvmO4anK4PbhpUmlqfpjmFfPw2ypY_c_WsAPFasTSyxGbB7LnibKAw4FTHrTlZnKrs_4FdSLrVbHjE_WnHN2dXrGHBzo7hn5HaK0VY6EJcfrHFBIDO_dAjH6vucT9nt7Sad5kMkDMdrRMyvxg5M62fNSLcMg7iX9K7gQnAJnALXsk1BJtU8PYtffksFQOtd-hydgzRMCyq5Jh1wNOx6P4HSO__hWh-nE7DbLkV-wE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کاملا جدی دیشب پرچم اسپانیا تو تجمع مردم ولایت‌مدار مشهد به اهتزاز دراومد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101290" target="_blank">📅 11:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101286">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEFY4k7AyMcaqC9XvMANfA4QVDuV3-2BuhZsd4BDYdKLNTULS2bKZs1bY1HOKuKPTDmNk1mnxb6LakD7w4fkP5pb6psV05fKUYTITfyvMX0oXVp69BJ105OwVdrtOyV4HQ-B0BTaAmAFVR-t1y0Sd4I9Uk_bw5gnMC9zLRtu_L80-DYubgJvpFTDI3j9SRRW5HYT_IXfXr-GoyPyvUIN9zsV3FeTXdyygGVcvs0fq_sKnCxxd0a7zvUBCmigJetfo1iTHdTn6HtGxDlD-Ba2_ylxqY075Vwio6wBamjHWIaOMw5AT_Msk4XtAMUH3cuI8yOPAJsC5M0DhWVqv9lwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kj4Qw0f-YJbMRcF8z7RliHV5UVsfIMA7aARNSzLsSTzgva5bliCn7ShijXcsXJDGd2XyqtQfQrT1Vlm2I3tHRlxszk_lBu5t4v7D021vysQNRos7AOKCD0RMwa2E9hUNq2-bc26uu61m_7WdqZM6mZR7oku9PXAIvks27i-1YF_4-6bH5tC99ZUGCxkJVDrLoQ8e2eoATJVlBu7ewkL8Q0xa_QLtgbWcpbZ_gy92CAK-K8mmo51xt5j-sh4l1hPuMnuLJ2vp9gBuTcCagBX4lEwgrwjy5Nl68gbzGlRl3SWkvYbThtjqIGC-QcaawTjFyU6OWOkmBMThN_wwftZY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GUoJMoe4vKsibKysbsFnGO3Qzwbo_wsVsvGPhKKc8OlJgp6VxAvUL3xVXZHLSSE-50pWGZgmPyauamSOBHvBV7Krpk5qhQG8uGiJ9WKG0JvNlJTCvTdYOOi9oIZtp0i7kAKvutZSlRTDmsfchqivpONXlg3gYK4BPTE6EevQJc4AoXjTEMNmq-BJ_PslxC5h1bZh_32_uQeZV87lMWzdN3hqRN5OLJx8-gqPURH2Lx04qC6PLzTweZ0PA93d--rdg4JheOpYsPLQI_98bRVAIDV0b7irIpMWf2bl4T64CUMw-VyCrOev3XUkkLVplfzh4pyUzGrYbMECdU1bJuxxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9XP-UaRMPAQy-VggKxZrirNGZV-yhTSF8dLsaSAdXXy5wNzKlAuR-Axwawv5RJxEMkPIUsF-kmrmHDSVMHwDaLNrKIFzFIJ6l-Nzi8z5snAYnivaQFsq7dJCgSwbPy1PeIBPAyDiTZUQSuyaFWIYCbUcyB_XX2YzmXXzo_n2MV12-bKYYcW-e6T6imFYFhY7t0uGI9-U3i_5MA-uAaNnlzb4gNCnHar3fe2j_I02GoOH2QTOJBUx2LY_veCjnn7Lu9wWO0d5cyI1RgyOdtzrnsF_XVwg-wnMmUt3NP8riGkzJnP8-Kq5AwIwwo_Nnf4WVRbbKWgJ31EtiMNU67gJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
رونمایی بایرن‌مونیخ از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101286" target="_blank">📅 11:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101285">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=fChdE9lzmPom3YmaJbxGd_MBbieJ2N1Hs3tmwva09EaYT4Eg2vNsSqabG6ugaEfnzn0HFAQfwErFS6v5Ra-BqlUS9vdQlcUUCEx7hXMhEPHZnMlbXwdXC-zlwtzyTlx2a4nFou9QmOYWeo36vg2Wv1W12U-6wVNRFkQpDfhgyKExfMRDwdC-DJsHE6WrH-_S5mrp1Br24nOOSliK1f2dR1q9WwSmmM-3d39tH3Ch0F_0kWwUnOAfCLYeL0HzIUlNv3baLvxe6zfojf8VvKD4rpSnGZOtWjEDwzOHZl5mGGjCThzWkGq1caoJissL6nuS78hZz2ttgJvLmmHYxkSfBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=fChdE9lzmPom3YmaJbxGd_MBbieJ2N1Hs3tmwva09EaYT4Eg2vNsSqabG6ugaEfnzn0HFAQfwErFS6v5Ra-BqlUS9vdQlcUUCEx7hXMhEPHZnMlbXwdXC-zlwtzyTlx2a4nFou9QmOYWeo36vg2Wv1W12U-6wVNRFkQpDfhgyKExfMRDwdC-DJsHE6WrH-_S5mrp1Br24nOOSliK1f2dR1q9WwSmmM-3d39tH3Ch0F_0kWwUnOAfCLYeL0HzIUlNv3baLvxe6zfojf8VvKD4rpSnGZOtWjEDwzOHZl5mGGjCThzWkGq1caoJissL6nuS78hZz2ttgJvLmmHYxkSfBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچارلیسون بعد قهرمانی اسپانیا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101285" target="_blank">📅 11:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101284">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=ohfA6y-MldOOJfI7qr2E_QLiOhfuKWLIGuNuefA9Ccsg7FU5CZnBZy4LD6-_wUw4Se4eU-vzV2M8E_fNaln9vqTSh8WATQBgCgdIxzybpJBTD2loJn5kmlB5B5yDIbnhx8cbYI7ne1TrH1Q11E30qzES9ZTjzBQIAZq6vdlPEruXnf7TGrLTSqQqn8LqalLdnrxHPeN6ok2FaBZt4P427lIkFG8uV8p3OUjKGhefWLxQl4Zs6UOrIkw9ZV88lUuG3kQRWUmuBBHNlBoJkt0OQ3EoVDbCA8LgII8rZ6pO9D0vQgRD00xOtVPfn_2PBK1PB2N5ey6lSv6lidD7wp6tsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=ohfA6y-MldOOJfI7qr2E_QLiOhfuKWLIGuNuefA9Ccsg7FU5CZnBZy4LD6-_wUw4Se4eU-vzV2M8E_fNaln9vqTSh8WATQBgCgdIxzybpJBTD2loJn5kmlB5B5yDIbnhx8cbYI7ne1TrH1Q11E30qzES9ZTjzBQIAZq6vdlPEruXnf7TGrLTSqQqn8LqalLdnrxHPeN6ok2FaBZt4P427lIkFG8uV8p3OUjKGhefWLxQl4Zs6UOrIkw9ZV88lUuG3kQRWUmuBBHNlBoJkt0OQ3EoVDbCA8LgII8rZ6pO9D0vQgRD00xOtVPfn_2PBK1PB2N5ey6lSv6lidD7wp6tsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
🇦🇷
🙂
مسیر آرژانتین تا فینال از زبان عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101284" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101283">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=liKn_kwCbDicuOCsNbZ1ny80rJd0BjX1woMANcVDIhgJ6IrQ8PiUCpy4Sa8miab6Ntg1rvMFPh1txf_2gTk9RFJhhWsRaU1LEnCjE_hsxUVap7JfnSb2Jb96ENnWG9iF-fjPFnjpO3ISgALwlhjUlvtPJGdLsc3ZcsPoi4rniKqktUZM0OkBJNFUBB6NEhCEowW4berK0g_woDlwrbbPxoH7vgZwdsJOo0_PmV_E-iKUmvCxbMVaUZYJUfx2VVwrszmNi21XJ8gyAz1MZc1-wpPp54q8zkOFAqJ-LVeSG1Aq_2rUmyZHvCxvZGFUm495IZy0cKOnTE5xsw4XLB4mzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=liKn_kwCbDicuOCsNbZ1ny80rJd0BjX1woMANcVDIhgJ6IrQ8PiUCpy4Sa8miab6Ntg1rvMFPh1txf_2gTk9RFJhhWsRaU1LEnCjE_hsxUVap7JfnSb2Jb96ENnWG9iF-fjPFnjpO3ISgALwlhjUlvtPJGdLsc3ZcsPoi4rniKqktUZM0OkBJNFUBB6NEhCEowW4berK0g_woDlwrbbPxoH7vgZwdsJOo0_PmV_E-iKUmvCxbMVaUZYJUfx2VVwrszmNi21XJ8gyAz1MZc1-wpPp54q8zkOFAqJ-LVeSG1Aq_2rUmyZHvCxvZGFUm495IZy0cKOnTE5xsw4XLB4mzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
میثاقی درباره عدم پخش مراسم قهرمانی اسپانیا: «حالمان بد می‌شود وقتی مجبور باشیم چهره این جنایتکار کثیف یعنی ترامپ را به تصویر بکشیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101283" target="_blank">📅 11:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101282">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh5a3SQHFO4VQC46hrH2Pc8-o3m2OI4oe6T5HLMV8kW071J19YTrJ_0wYBwJpkUbZ1P0DjC92oNbe9mqYevLehuE-QZ-pzCeI7vc9gZGt3RhkAqE-NND6fgHwibS6_9Ae0toHQXTT7gp4jXUGyo8hCFTbGcD55eDWZSWWIoYiQSFQb9FEiyGqpZOqMUOJDlc6R91SNQaBs6YK0AftX2lqH-g-IPp40RaSQrkWKSFi02bdIA3n6tRgYFuAeFzuGI2cyTPlPxiMfk1-ztYns1H7nH_wQsvmZVaHeAVFEux9tUlevnrlxVX9JPxeq_x6262apK-Ql-LlHCCItRejnPZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لامین‌یامال هم سیگاری شد
😆
😆
😆
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/101282" target="_blank">📅 10:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101281">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0s9hOSujTtFyJQmTLFGyy4BBDCp4_wtdt4eJw_mWWMhm6OXPSRFH4Y7kWMtzGbqvhzTnoET04f3g3NVMJfYnHRLRMbm5gDbRP8pYQcWeHAJuCgRK2pjT1s0YuBjSrhxwPeoat6U1iXTj6m7o5J6edr6JRcpZT-GQHzLz5Hn-h7KOrTy7A41n9SVoctatyovEz59vWqSvmQoeT1Z8pNefmFSDgUq53cxX_Yh7jYZNis4Q8xm3AQMVZkuN1USrg94T04SifiVVTjV2j6c41i5PuvPD1ggBDrmUK2TXNZWjSP5fKQtU5oNZW21dRKTBhjB2E-wuN7d4UVsuFWjZUHEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
🎙
دونالد ترامپ:
"این یکی از بزرگترین رویدادها در تاریخ بود. هیچ رویدادی مانند این وجود نداشته است، نه از نظر کلی و نه از نظر فوتبال. این رویداد چهار تا پنج برابر بزرگتر از هر نسخه قبلی بود که توسط فیفا برگزار شده بود، و ما به کشور خود و به تلاشی که همه انجام دادند، بسیار افتخار می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101281" target="_blank">📅 10:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101280">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=ura2guB4zpN3srfT4zcxoAEsDJvSpU5-DSQZXzoRO_LeqClU-61xWQijlGZsvp7oFszYKKe_gIdBYNOQohDtbRHGfwYjL6QmIddW6g_1M7Zxfd4S9Y-1Z0YifqcDub1JkbBh2YX-JVDdVhpOJR3_abzoyaUaqhFyrDRZ_7Hh4puk6D0Sho-A-nc3O5K3SF7TwNd14BwEUKgfJkvE5gcB4du2mMzMER4Z3n_P9xsMe0jJ1lo1GIAVASnPw-QVUc2gYyRY6KI2VAaL2ORCI7HLTDwW6_Q-Qa8cqTYlWGzQRtojswD-5n06ZwCPWF9gnYf4ezINDdrh4bhDK4UYi-BS9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=ura2guB4zpN3srfT4zcxoAEsDJvSpU5-DSQZXzoRO_LeqClU-61xWQijlGZsvp7oFszYKKe_gIdBYNOQohDtbRHGfwYjL6QmIddW6g_1M7Zxfd4S9Y-1Z0YifqcDub1JkbBh2YX-JVDdVhpOJR3_abzoyaUaqhFyrDRZ_7Hh4puk6D0Sho-A-nc3O5K3SF7TwNd14BwEUKgfJkvE5gcB4du2mMzMER4Z3n_P9xsMe0jJ1lo1GIAVASnPw-QVUc2gYyRY6KI2VAaL2ORCI7HLTDwW6_Q-Qa8cqTYlWGzQRtojswD-5n06ZwCPWF9gnYf4ezINDdrh4bhDK4UYi-BS9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
تنها موقعیت آرژانتین مقابل اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101280" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101279">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=SPTS2BnQKeQ-qSQd4oUtQrqqnz2Y3TwyFT_AQUDxzEhaVrbgo2wn6Ocwc-xq4ro2D3SYA4auahyEwzv3RgnngcNHRZQy9zG6WH0xl0Z42E16oLuAhwGwfSse6cGsESlWmLbebRoxpwgG_ZW7-_3RR6bSlY18FdYJjn-AqcvtTYzSVXKiWATVsLrHMHpBzsQk2qFMwpMY6KPN_GtDYzKGE_FhMslH_9U-Xr_eD5QIPWMkPc_SccqmjRMsKNoWQlm9zEEBL1ur6rI6vsf5xOL2NdizuTVGTSMc1aZYmRlYh9DD0VdGZdwHTuT642KKN_kvSeK5iam4mhZmcGBaQhBN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=SPTS2BnQKeQ-qSQd4oUtQrqqnz2Y3TwyFT_AQUDxzEhaVrbgo2wn6Ocwc-xq4ro2D3SYA4auahyEwzv3RgnngcNHRZQy9zG6WH0xl0Z42E16oLuAhwGwfSse6cGsESlWmLbebRoxpwgG_ZW7-_3RR6bSlY18FdYJjn-AqcvtTYzSVXKiWATVsLrHMHpBzsQk2qFMwpMY6KPN_GtDYzKGE_FhMslH_9U-Xr_eD5QIPWMkPc_SccqmjRMsKNoWQlm9zEEBL1ur6rI6vsf5xOL2NdizuTVGTSMc1aZYmRlYh9DD0VdGZdwHTuT642KKN_kvSeK5iam4mhZmcGBaQhBN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
و حالا پس از ۱۹ سال، لیونل‌مسی ایستاده قهرمان جدید جهان را تشویق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101279" target="_blank">📅 10:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101278">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3de45ea42.mp4?token=QMznZvLiyrIF8XPBYreCqkarGGZbPQz12v5WB2VRJ5by23R0uCCMCZfux1eXwUdRVsRzXyeSs25Z7tQb0iLt-_OwuLJ7o_b3W-1jvxkWmrFHx3k7UaFTt7eqvcFaHpIVUcd9FbAvjXNFPF5nhbjpYNpSjZbqhoKcB_oYIQvKHZix9ivXHfQk_00YU7WLxGptpIVBNBfsxVrbOaEacy6uR9UW_IbgfMpFGtB5o7_G7ErrfqjKxeD5u6yQfQyCuoH7oup1zWrYKoeqgP6tKo3h4JECAYWgg8zwlNK3ymUOpLOhsvK7XI5RdqlNn0c4xn9PdTjRrduZsBqUqEuLNEoMVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3de45ea42.mp4?token=QMznZvLiyrIF8XPBYreCqkarGGZbPQz12v5WB2VRJ5by23R0uCCMCZfux1eXwUdRVsRzXyeSs25Z7tQb0iLt-_OwuLJ7o_b3W-1jvxkWmrFHx3k7UaFTt7eqvcFaHpIVUcd9FbAvjXNFPF5nhbjpYNpSjZbqhoKcB_oYIQvKHZix9ivXHfQk_00YU7WLxGptpIVBNBfsxVrbOaEacy6uR9UW_IbgfMpFGtB5o7_G7ErrfqjKxeD5u6yQfQyCuoH7oup1zWrYKoeqgP6tKo3h4JECAYWgg8zwlNK3ymUOpLOhsvK7XI5RdqlNn0c4xn9PdTjRrduZsBqUqEuLNEoMVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نمایی دیگر از جنجال دیشب پاردس در فینال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101278" target="_blank">📅 09:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNhOG2PbQ5hyRIYFQZgIe8XRSRUwPfUo06bT-BTDp-2njdoI-pRmYc5sjfXuaeUdeMHNzLU2gTYjlLtmFx_nFyjpUD1clJFhmWDR9lJhMg1GR1haqX5zaO3-49HYkVCx-c5nu1-nkRHVK0U-4yvX8CMjhl4zSNbUlCBRSXojR-15mI5O-cp2c5Op1JXSMXxCIPTNL-j4sqCaUI3YvFLIf42Ve5TMxEyUukJSNDfvw3RotfrXR9YyzioP-QwGATkQtcE43G8ZqTCHvbyj-y-J2NTdgJ-pzsz7rPYWoWg0BnYO8wbncQggh-koY-aGe3LxKaVV_mBP_kPFC6K0157nXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت دلافوئنته اگه تو ایران به دنیا میومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101277" target="_blank">📅 09:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d46d00d3.mp4?token=BCG0O0nrX34GtBnYUKia7zSv5TJmim_fA6hPojGL0LbbX1WA-Puqcp8yBu2nT7b9bpwWcZcXO-inLNn8sFrWqLmyW6DncpW34CqTFJ-fGGVXj8OpcOUXyklvXc2Bl8VnJJypBF09odWXeCr_NY1-i57IGAjba6RsLbJwQGdR3MZLEhH2tZQv7OWdSR-x5rbAfblvOdEiakvusJY2ta6hAyLx6WR1K9y00mwapvFl8wTKIqd5GDZfe1o6qkPpxZPCq0vmvakYxqg-OB1l6lCTpIiXAHaIoPZzWpXTJ7dEw7t6yOsYIVPrKjMLrrilYBUzvmUQOd-qIpI_P4RzDpjTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d46d00d3.mp4?token=BCG0O0nrX34GtBnYUKia7zSv5TJmim_fA6hPojGL0LbbX1WA-Puqcp8yBu2nT7b9bpwWcZcXO-inLNn8sFrWqLmyW6DncpW34CqTFJ-fGGVXj8OpcOUXyklvXc2Bl8VnJJypBF09odWXeCr_NY1-i57IGAjba6RsLbJwQGdR3MZLEhH2tZQv7OWdSR-x5rbAfblvOdEiakvusJY2ta6hAyLx6WR1K9y00mwapvFl8wTKIqd5GDZfe1o6qkPpxZPCq0vmvakYxqg-OB1l6lCTpIiXAHaIoPZzWpXTJ7dEw7t6yOsYIVPrKjMLrrilYBUzvmUQOd-qIpI_P4RzDpjTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گاهی فوتبال فقط یک جام را می‌برد، اما بعضی بازیکن‌ها قلب میلیون‌ها نفر را برای همیشه فتح می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101276" target="_blank">📅 09:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101275">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a634e3021.mp4?token=sTT1u_MPVTsjWsarT4D4e3ELrzOXQ_e3JVGUgJp7mjneJbGfaoEy3rRfor52q0Ik3p1n4TNG4hcO6Vs0iorJnQ_9LqeTT8GRFpqaqSxYSne7DyrDOiqcoANgbgYLF4ltPHXH2SXIBqzX0MV-_3iym5LOiSJjHou_UXXjB_sCtUBoYzLYY6VIaMnC8jNuV6FNoYGK_H2S-YSQYlW_SRTvy8rNXbdhVPfcSpNbIPev31Ec1VqmEdmAw0CWKBhkQeG6kAlaBtdzu5eKvigAq2rAQrlmFGA7l6N1SQKsa8_ZZOURA3l7Jkzm2akkGHVeGAUt-tLULRVRZpO7UQEnv-TJh3crATzwkkM4-u00L27ZMV2nMDEkc-6YnGRTodIluouJ1Co7NyOO063WI6-NzcYH0FhWcR2dfprQ8caUezvWdCc76a_Tf8UXg6wiDMUVYSu4gt7C9xf5hNSptdFDD7L_R0fCb5hM0iWmQarWrUyXxrZ6J0tfc_duJ5Dt3n1nHKMyeUBGZdWqE2Rz0yYtZ64toq2BxX1aAW23y73jY2L24hk0KZhdtB_6_tscHVH8UQLLkZpy1GWsvsePyYmo4s3h5rK8RLmhd_Icma0w57NCh1gI2XwuagyayDlmd3rGp936ylKrcFIBfRhR6dwXYZJ7b8E0X81xwdNQaQV3wVn0MNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a634e3021.mp4?token=sTT1u_MPVTsjWsarT4D4e3ELrzOXQ_e3JVGUgJp7mjneJbGfaoEy3rRfor52q0Ik3p1n4TNG4hcO6Vs0iorJnQ_9LqeTT8GRFpqaqSxYSne7DyrDOiqcoANgbgYLF4ltPHXH2SXIBqzX0MV-_3iym5LOiSJjHou_UXXjB_sCtUBoYzLYY6VIaMnC8jNuV6FNoYGK_H2S-YSQYlW_SRTvy8rNXbdhVPfcSpNbIPev31Ec1VqmEdmAw0CWKBhkQeG6kAlaBtdzu5eKvigAq2rAQrlmFGA7l6N1SQKsa8_ZZOURA3l7Jkzm2akkGHVeGAUt-tLULRVRZpO7UQEnv-TJh3crATzwkkM4-u00L27ZMV2nMDEkc-6YnGRTodIluouJ1Co7NyOO063WI6-NzcYH0FhWcR2dfprQ8caUezvWdCc76a_Tf8UXg6wiDMUVYSu4gt7C9xf5hNSptdFDD7L_R0fCb5hM0iWmQarWrUyXxrZ6J0tfc_duJ5Dt3n1nHKMyeUBGZdWqE2Rz0yYtZ64toq2BxX1aAW23y73jY2L24hk0KZhdtB_6_tscHVH8UQLLkZpy1GWsvsePyYmo4s3h5rK8RLmhd_Icma0w57NCh1gI2XwuagyayDlmd3rGp936ylKrcFIBfRhR6dwXYZJ7b8E0X81xwdNQaQV3wVn0MNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو کامل‌تر از داداش یامال در جشن قهرمانی اسپانیا؛ دیوانست قشنگ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101275" target="_blank">📅 09:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101274">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWAIn89VfVWgNN9JozekdpH0aDtenKbtLxElT27qy1KVypAHruFaPO_mpO9bEFnHE1x8DaSMwqAdT_OCrA6PKl35dL5BLvxbK_qJkD2lV6HYoBM1XDFgfkqnnHna2LJNzIwvdPnTJgmiSRQhSDHAISOH56eDkCEqkcEJfylIaOh2SkVHdtXO6Esxchd7Tk-akurvUNMs59VW1Rk_TL9YO05HRBHk8qGPBpk4--nxrSB4UUi7BOsmkTA3BLJq8rbYsbesGWf6ESByrLYL0X9PFtSLARmsQWbuUwV7cF0DPXhqpIqcoPLwiPrm14cYDtjz63Lkq1bdEykvORjytvYUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
رودری یازدهمین فوتبالیستی شد که قهرمانی جام جهانی، لیگ قهرمانان و توپ طلا را کسب کرده است:
🇧🇷
کاکا
🇧🇷
ریوالدو
🇧🇷
رونالدینیو
🇩🇪
فرانس بکن‌باور
🇩🇪
گِرد مولر
🇫🇷
زین‌الدین زیدان
🇫🇷
عثمان دمبله
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بابی چارلتون
🇮🇹
پائولو روسی
🇦🇷
لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101274" target="_blank">📅 08:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101273">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deea9feba7.mp4?token=LrE9sUAc-uJlZbPLu-YOB0cqPoEKwRaU3uLJ0m8-KjLdHKBn4w5xV0UO6c6eFgCFbB3wQ-XaHJ9tsy6WoUWklsjRcIp-WmWDEjHIjxA1K6TauaiRZKTQ5fHuYTuguNioFWkxu74zeKDcQFF_EW9On6pYqnIdpZtFGMB7U0m4TnPrGYMAMoFkHQnjaPGdEw_OdluPbioMt4bzOzPbgXrUjlAG2MxzcYYP6U4aKjACV-DzEOMOrwUsOk4lZOXu9oBdtVs-KCKlr_JYXaLtydj-ougFR6aCyEQwpZwdtoiWM8NB-kFIq3wFx0sJdoBmcCOP2HzpP5ueVErEmA2fBjPi3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deea9feba7.mp4?token=LrE9sUAc-uJlZbPLu-YOB0cqPoEKwRaU3uLJ0m8-KjLdHKBn4w5xV0UO6c6eFgCFbB3wQ-XaHJ9tsy6WoUWklsjRcIp-WmWDEjHIjxA1K6TauaiRZKTQ5fHuYTuguNioFWkxu74zeKDcQFF_EW9On6pYqnIdpZtFGMB7U0m4TnPrGYMAMoFkHQnjaPGdEw_OdluPbioMt4bzOzPbgXrUjlAG2MxzcYYP6U4aKjACV-DzEOMOrwUsOk4lZOXu9oBdtVs-KCKlr_JYXaLtydj-ougFR6aCyEQwpZwdtoiWM8NB-kFIq3wFx0sJdoBmcCOP2HzpP5ueVErEmA2fBjPi3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیسی که داداش یامال با جام گرفته خداست
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101273" target="_blank">📅 08:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101271">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGtHg_3-hYlmNoIQgV1wbyTD-RvAvNMARR-hwb--1tPTBdJnV_kU95F9Lz-y6ABP2BJp857N75sCLyng3qQg-VK-i_kL4ky5Rpk28luBFG5IZEx3K6DHQx0dxJDHsc2VM1RCIdBH8aql8NCcyfDflLAx2u0t6U6V4rJnNNEY0xP41us8x6lQMwSIFQxjYg9twWniNfMMk96CkAAdeAYP3w1fhtMraH9U9Z1KSI0-WwOpEh_h7oGy5JQ9mm-SVjBe0lS61vSF79Ub2doQgMJL66Yc3zLeVkqdiftyZFvyIM4ywiKA832J36pCcnwY2MQsJ019VyLF-WcYEXbsSkiIDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6CZ3NYUrDRXMWsr1C4Q2e-7C4LFjAZu_CqHAIGPeIKzJO1o3fggCGW25BLY7tEZlnc8O5R2EwZqOyPeJvEeBk1PPBzrBAZRkx1L4A31Ioq97eEAFdUhZ1Q-h8FGt0cMU2OX8TGf422tC0XGuTKs-jEafiQRj_TYtq-9Le3UX14XlvFlyFbhMC_t3FpxPm-7dnBZ70dfIViW5alGpEbpx-TY0idPb-mDBXc9fpAhRXCmXtfJk0dm3OxQtozgF8WCHgZl52dKkB8uTxQT5mgQmsLa7hhvSp3R_yVUqUPgnqLfkWyBeRoPxCcKiUUjTz3ZGvp476hOH4x72I7uy58bKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوبارسی و بانو تو جشن قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101271" target="_blank">📅 08:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dduMp1C1vNt5sNL4lFbfaL7HKX0p8thNnFYjAore5ZVG65hso9hzpsi8Y3S2YaUodYBzz-JXHzc1jQXXtjElcogD6wL_nAc5K_--Uu0VilR0gBUU9g8TTkUxHxN9YSlklCgQZrMTo3geVLWN2AOs-Dz3FfZYrH_tm8i2fGPVp53JTsQIToTCEwa3Ig0-nBq2jzUwsR4K6bey5JLUGQWtAu0ZywdSLI1MER_X_hmN7CnNZBrIGpK0NgOkD22sd2bBZ2qPF6--aqJDoHol2uIkSsv1d0T25HtKNW0J5Bq4XQCC5yQ3lbsB32Ux-xIw2ztnDJs5KB2ays8HYqLkKhM7ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qp85Sr4GhrTryUbEXlYIoEUZVytaOimfcuIlOnu6HzUS0rHtSNnCb3WzNqekMvPDvzOice1QksO-Ept9x4Tz8XQwrHwgfCBukfDNxQRp1Yrz7WtBnLhJKTD3mQDqJEQoQ_wF4l6ZCg9WENemnnByN390KQJ1x9AQYj20QUca6E_FCPTsAMpFum42XkPiOz1Zm96opnkVbqlsc_ETdfNwV_6aKQENKGdI3wWrcTODKmdxrIzA_WXX2rNld0LIqL_jNCY1VX6trBHPVF6xdOEmFUmPW3DaMk5eB1nBNb-B0ZSywMoL5eT_3sMOayGmulE57lBNN_yld4FFRDA8ad-Eqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXeJOGQe-X0Z-a90aKzVikj1ecOADoE__z17hKTHH05tpc_Whur8gwVJ1uZmpKm5X-Ix21-Xge3V2xiltef0ze-rqWPFK7eJsPP83rwC9-nsZR-C9h324J75QyAUyUvaTAYc_rIrzNqYz1fNPUt2BnblHpUVuL9NO7jcxWr16ygMN1h1EwsD3c9T-DU3IFJ9AiyJCeoS4VsVfuleBydCFhkY95V23c2j8PGEvO-IjDswhqoiSlNVg8d0i2V0wjkcS0Rd_cpz56oczmeVEItkaF3Tw8SyGPwPOTySAUyRYURIrFJn0f3Rb-sOcbqqRw2BwFi1SFApbEqRWb03bmBqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKWkTt6VLbPucKKrw3KeOCUGCsQjMOulVh8BAKH8z11AedycoKVoMxdlVkDXLk17UxtG8c36DI-pZ7ljXj4SmN5J26DG_hAcevVh38WcT96ArJXjicWz9SCmkQjqEFA-1edVKuCwcBPgmm_GMCOj4TMs-teV9coA6bKX7ka64aPc6ine9MRoVRnD_nG01ad8HtbgLnhFsKO1mA-FCMmvVAHzzycP82MNh0crqaQjdH1mpMP630X1ooRkwJFAUrEz8lz9Ll7rZN1gJxvqZ6BFnNq0ZvrS6BCVtsdalo0BaPufBhMetERQB3NiJJHpbayChWIorHweUPj6Wxr4e2kwFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینم چنتا شات از یامال با جام قهرمانی برای نیازمنداش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101267" target="_blank">📅 07:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dd52c94d.mp4?token=XBzm_q_IgQO8fQFZ4a788HTy5rbVFYI8hiXob8LnBE0v6cQOV5Al-RmvOq8xbnSrJozX5zBD-mmNEJG8qdYv9Hw2cyd8Kh5SV9AYy-iGmINTTXt22ISX6M-CvsfI4NAn4Xiq3nhJFHDXapnpZrrxoScOMvWl4tPdM-Ko8uONvR6p5ijKVkjXGJbSXo1C3-wTr2IFNJKjKCOwu6GfaAmE1NTwUXWracTK6Rm-npnPjjdR5jzanWQF1MvNUyofCLgUiAalUMeCRCbjPfzTK-c5WKPdvJdLK-NC9E7FdhqYhrg0VEz15ss1sIO9pPpxnQwaa0tr8jwlXe3q2yc8mV1TAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dd52c94d.mp4?token=XBzm_q_IgQO8fQFZ4a788HTy5rbVFYI8hiXob8LnBE0v6cQOV5Al-RmvOq8xbnSrJozX5zBD-mmNEJG8qdYv9Hw2cyd8Kh5SV9AYy-iGmINTTXt22ISX6M-CvsfI4NAn4Xiq3nhJFHDXapnpZrrxoScOMvWl4tPdM-Ko8uONvR6p5ijKVkjXGJbSXo1C3-wTr2IFNJKjKCOwu6GfaAmE1NTwUXWracTK6Rm-npnPjjdR5jzanWQF1MvNUyofCLgUiAalUMeCRCbjPfzTK-c5WKPdvJdLK-NC9E7FdhqYhrg0VEz15ss1sIO9pPpxnQwaa0tr8jwlXe3q2yc8mV1TAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
💔
اشک های اسکالونی در کنفرانس خبری بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101266" target="_blank">📅 07:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b524eb5176.mp4?token=P2oev4Fuf9fJQJMElTzxcYZKEad2vkOFhnc6oY3S1-8RENi0o-uWZNyBF00wKYHef77D0nEIUmL2Lxcoqk5emGGPYr4IAehJbYPq-whWvHPb4Jz8NFutXet1RrzMfOsnlmvabmubgrh73Y8_LhcHWKioo6LIdjF4HMOUoE0Y9-P5kAoEVXUJ9tCZZJWtXRa3ERPKJLCLhPLCnb4lxtdICKsthcEX8zugc1NFcseavVAGaMnnIfP_4OkghZjxs8hqM93-Jteer4Bwp_i4wtz-3vTR7jHTrtudc24_Y0Bft78crTGy7Z6LTedKcEgMnvlWCkfW8sjYVUd6o2xmvS2gEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b524eb5176.mp4?token=P2oev4Fuf9fJQJMElTzxcYZKEad2vkOFhnc6oY3S1-8RENi0o-uWZNyBF00wKYHef77D0nEIUmL2Lxcoqk5emGGPYr4IAehJbYPq-whWvHPb4Jz8NFutXet1RrzMfOsnlmvabmubgrh73Y8_LhcHWKioo6LIdjF4HMOUoE0Y9-P5kAoEVXUJ9tCZZJWtXRa3ERPKJLCLhPLCnb4lxtdICKsthcEX8zugc1NFcseavVAGaMnnIfP_4OkghZjxs8hqM93-Jteer4Bwp_i4wtz-3vTR7jHTrtudc24_Y0Bft78crTGy7Z6LTedKcEgMnvlWCkfW8sjYVUd6o2xmvS2gEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کارلوس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101265" target="_blank">📅 07:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5BDn-o7g9yAeAoTiXZgJ9VQ8zUKphh2rmLPiYLUPy8gq5TbUaieXBMCvd54EiS_yYcHly3bbPGMrEdzdwGDTeaAZOXaF_l2Olb8J9LnxLu46xGLdFD0NmJyA6kjnpBEH0TFs6Ft9xDg4JvgjFYbsyeFuhwJNSvAwaDOhDKXaw3ZLSO4wuLtOjSXV1qppuM74YIb7EveNJi8PCn8CH_kJ4w301SvX6i3dwsGhUpU8dvgqnJQ2Ens5-lK2K9JgJWFg9XZjNs2PParheZJDo7nXj35yfRfKpo28yYuKV7QM7h0fUBO3rcMuNlT0i9sgB1AzQhPI1zMDUJj5LHT4f3pGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yyk-YwGvvyzM8IJIuTBcoUeV-HHN8kRR0DZLR7pGcNyH99Zo597gFTZeOQGKyE7pi1OQqvv_SrcUnaYYvz7UsyNE0R3FInfPxVSFNSklvr_jHymmqddR6rnG61iOSzzjTdIeYnc_5Fb5UigJ5ifXm_TkELVkSBmrR46z2Uz0PBN8aTUFzGsUhmAQFuYFLDObz0hBgbbk2Gv0l14KirSdhdPp1Us8LaP4oIPzyU3N1OaHzQNosOwhuCI3GDDwQYKPayBuYXvoKsRxOw7cZJ67_V6znByixPcUCoXO90iOgSkCeYr5p_Va6E8sWT4Hdnxz8xPKI5YP7OEL-xfUUqCdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PePKIacMoAiZ8lcz2yYngzdfy-e-VPn_nbENcRI5hYr0gAlHQsYMRKCoJ4a36w6V6a51PBdRV6lcGREq_Hr8BucGG_Nf7xUcPzNHyQQ3eUGexO1JLXB9HGLTaTDRaReBYaaDFPasmuHuIRftxk_-6pufjEbTYlPBJ-1l0ntUwDGz2UbIEHrpdlUhTOGM0VyMW4TqUqDkqvEhcxstQ0vjG35ZhTbtx8RtSKSAZNIGoLTtYoZuUWTyyd7Xbq7qqpyzFaPQplvMk8OFuPMddVoy3OhW3ID2WeQALiscWxWAO78pSIsCFHhomY76SZYmBzMYczb4C3kLdnff_xQhl3LfnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
❤️
مینی یامال برنده ویژه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101262" target="_blank">📅 06:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrDoOyiOt0fRPEUTBLGDT21bkpARvRo2X6S9Zo9wfLOzDkLkRl7Z94h0D8Dd2ckmWinjpbX-Y4GsWsxdNi8Q8lsllcJPjJ4jYvQB8XjKUc6M899U_RfjsLe8z-lmsfp20rVf_hLBYg8j4g1DVsEPFqzPQtSB9qkuQxxPQXWl9y3yVXiRiwRaQeJy5DIMTeMsjeltADQxgMOjaaXqBscUD_KvBkKYuOI17DOSO5mrtUejU9UC-VsmpLKhm4afikwKHPbdKNCPDWc15Xp9SsVgtQu2iKXyoNCHMGi5y25plhE0NOJBDA2mew4Ac67emrWTLPO6in7t0pFxLRWptLMMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
میکل مرینو:
هنوز هم در شوک هستم... ما قهرمانان جهان شدیم و این یک دستاورد بزرگ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/101261" target="_blank">📅 03:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA0jhOj4X7Fvc7QqbrlW3SlKVjZBajpNa624iM-Uai_dXcKHDP7vs9ATW0S3GBH-0xrj8mxUR36hiGzmI1iicbVfObU4phTGYdOs5cPr1rM0b5WUJBETHvoh018Z8juMuMkB-ly0XeX9ZYLlg9LD6r_fO0-MDeIoEuzCQ4_9VmsZFx-xceUnvEd8C4b4ThmPKu-byRZGKs7IO4cHdv6jwdy7qLIhj4rDlf0C0sm5mjypfNRWWB9CvWhfb1szqDydqKj3g02JxoDJonRAIUGcvubpchXJDLGWwUNdiwF4CSlbUmTLTh6-yUCjT8fpFL0lwqzhU6e-6YzYVmfixUl0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دلافوئنته:
رودری بهترین بازیکن جهان است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/101260" target="_blank">📅 03:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc89e4277.mp4?token=OJSqQBUgZnchephUmKVVGCIGbAWOSubN_Kspz6r6UOMJnK0hNu5JJ62JUqhDVSHu_E952HhWubrWdZtPjQH7qEyGHd-FWFGpeVX9STf6Y9TVF-BSQ1ooE39zZrDo74UciSvKUzuDuLDS7PALz5jQoBRjhHYVUYi6RllxT2VFHkunwxKC59iz-cs8g1xoeAL_xEmJ5vpzAHyTQgMvMTwgeTUZczM3NHoeUssPgPNaWn8-8SOELtTcelUK1IK3oeFnyW4D2UnVX7RXArdRFvDFgIbh6qmOaYlJgZdhLP4vdOwCvppFCWx-NyCqzfXcc19Z81Jga5Mm2LINlz5_1QN5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc89e4277.mp4?token=OJSqQBUgZnchephUmKVVGCIGbAWOSubN_Kspz6r6UOMJnK0hNu5JJ62JUqhDVSHu_E952HhWubrWdZtPjQH7qEyGHd-FWFGpeVX9STf6Y9TVF-BSQ1ooE39zZrDo74UciSvKUzuDuLDS7PALz5jQoBRjhHYVUYi6RllxT2VFHkunwxKC59iz-cs8g1xoeAL_xEmJ5vpzAHyTQgMvMTwgeTUZczM3NHoeUssPgPNaWn8-8SOELtTcelUK1IK3oeFnyW4D2UnVX7RXArdRFvDFgIbh6qmOaYlJgZdhLP4vdOwCvppFCWx-NyCqzfXcc19Z81Jga5Mm2LINlz5_1QN5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نمایی دیگر از لحظه بالا‌بردن جام توسط رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/101259" target="_blank">📅 03:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/du0J0Yh0yMWwsQrpflREcFPMpCJ-QpPnd1GSQwIaOKRSf0nFlTZwWMs2weYEHu7cL92DYEDjfmST9DXUVIxrTjsy9q1_cB6UkOx0KJfPhbxh9-vsoSt-DPcYQQG7WW6Qc6yLuXl3PYGWLInUFrlZ8UQje_5aPlC6phAch5dlgVwO66uKppUOURf-nvokDUl4rH4Tr1I_FrwfmtJouz9-cLNkBAz5JVIT3ShIjX3Sv6P_20gYMtKJ7MfUjAytXHmi5mQoisjPruNmaUCj0cKqd48-rcyeGPy6OTOJwPb6qVFun5LNLn0okbA7c3-V5XZftkXgd8yoY5fTO-RvNAoG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیونل اسکالونی:
مسی بهترین بازیکنی است که تا به حال پا به زمین گذاشته است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101258" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsrCgl19ZqyM84IHGoRlaQgWrSZeqDG3_Fpto7QsHxjEDlOF243-h9bBnhevMc9kQ2UNYXCfJDTuSj9PGRhsVGLEufAGlDTujOuDApz2X140uG3sRYHQrU1XRmEjfvFNArMC_1iOkBKekxL16n_np53qbtj0SHNe5HMNGwAIhFC8YXqybpwj8zgOZT5s5zlvaHS6pSIUj3K6ljofG6EonrNOHpR-wABxPhwLP2OAoS_IWocQ9gL1LIeNV20otXvvgeXcvy589OkcA4nNRJQsIsy7p4n3gMCRNxMVGMlR9FL19SkvxZYAYO0Ipy25Bf87x9E62WGPZP6T_yaskcD5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
😍
لامین‌یامال و برادرش پس از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/101257" target="_blank">📅 02:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNJIRwzc1KglRjn9pkdfXjqmb8xadgjH3Jon2fWyGwaogMeAAle4mw1P-EUEG5b8YAkG5_c6EnQFsNgopW8ADlYtsHNA2ijKe2rlPYqYWOLtpkxI4AhPZbIkqdwXxplQTZS4r0TVxEl7xBMmYaX8nV0nUAcxEnEKXn4NDbvwtDEJP9gSiEF2A3InaYSuiV9F0hIhMSLuWI7FtD6Wo2EKYDIhIhCl7qzRfhyuYG1PoUa_PwW9Wt4Gz6YOWLqwHvaZiweyrk_edUePPL_FKyN0YcGsD1pqzyoihM3fHhtDk_iT36azVbbTNBIl8RuHV8o1c-j-OyCxUjPXMtYyffnZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فران تورس:
دوست دارم همیشه در موقعیت‌های سخت گلزنی کنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/101256" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNvXmWnhAq-GcjaDgXORweqBnNq_3Ms_hsICVsV1Gq15axmTJG3iiVI6SDMPvv-NcMSjkX4qtKL-TuRZ3abD0giYKlwSl_UDwP8kAkrXErps8eTunh_Kcpz5Qev1_ugCO0zSN9c3pNYam9ANGsufIfzxkNY_2a-qLgsVSlazAUbiKJXW5XSiKnuArUy9XZUVdB1OHbdMVhyPfykSlo6lNmjRLXqz8fqs7GfmcziYUg4xyme6nEtoR1xqVll13Sin1uN5Jb0hX6DN-yPAKrmvC2iFlzJW-owOvYC_CEkIm48t-otXS_X8DLH6ZJRlE0Weaub8U5vO3tSAPT_FrA1X6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام: حملات ما به ایران برای نهمین شب پیاپی آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/101255" target="_blank">📅 02:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
چندین انفجار در تبریز و ماهشهر رخ داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101254" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd06e84d0.mp4?token=DEOkumLCQzx9ED7r9mPbwqUTY7o2A50g6jQgPYCL437cjvgFHI1stuICzIeC6i-Z0Uy3xga3tXnWy14jyQzfFFDNXTfsAp3c0Xak_uXkj2lKX_8cctltkbVdRYL9Knk5eawajOvdga4VekZjSlfi_jbycS2eNfotcLWetNUSH2aGf5MgKxusnIgcTyG4GITIi8dNvSf2R6A5sC4OwoRqHZe6XhbmiGP6ekJs1Mg7CHnFFfiVW3E9wI7kqH7FBEXjYRKksVzxcBvIcgEHGPBAdwnhIaElyxMGZvBEjphxNdVhH_0HspVPYYc0_-VjhFdYuOjeD9yxFBuEfylDnZLTwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd06e84d0.mp4?token=DEOkumLCQzx9ED7r9mPbwqUTY7o2A50g6jQgPYCL437cjvgFHI1stuICzIeC6i-Z0Uy3xga3tXnWy14jyQzfFFDNXTfsAp3c0Xak_uXkj2lKX_8cctltkbVdRYL9Knk5eawajOvdga4VekZjSlfi_jbycS2eNfotcLWetNUSH2aGf5MgKxusnIgcTyG4GITIi8dNvSf2R6A5sC4OwoRqHZe6XhbmiGP6ekJs1Mg7CHnFFfiVW3E9wI7kqH7FBEXjYRKksVzxcBvIcgEHGPBAdwnhIaElyxMGZvBEjphxNdVhH_0HspVPYYc0_-VjhFdYuOjeD9yxFBuEfylDnZLTwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇸
🔥
اثر جدید و تماشایی حمید سحری از قهرمانی اسپانیا در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/101253" target="_blank">📅 02:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOwYeA6wh510iXkEf4adYIvDmIlaPqu0sKJvfhWezTE1rEpl0WxN842OUA6Yox8lsXC2WO5YYVSO76M5BiAPb1rqoMFN6_Iy6YYs5HDs3GrMDYbmdbRaTfNIt8igTwP_cLdHov_oNfj4CCBwsZjVuupoJpk2wBax_FUjnFztW5NdMO9Xmz8zFbWgqBc3VoWM_MjPVi4oO7l9SOX-ajJKd20JiFE7SAc8MBSbdzCNmf40O7hf-O0YzasfvC4Jj5ihtMYQhwTHN4p0FzJpkTGl21vPj68iFNyxbJsBIkO-AThEDrCmobi8fPTJIdABPeoFasi8suXukLpMjFD9Yifoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚽️
بازیکنان بارسلونا با جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/101252" target="_blank">📅 02:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101250">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpSkyl9ch8Cfsac6Zrifuxixb0EXC9pIUEdqIiqj4dVXhFFzAy2Ca9mDx0V5BhWvTgpi32ItnqkJeGGCmrwM3y0XG88t5Nk3uWI_CPqjlHT9k1s0w3LGEu6ruGuyhMwG0YSq_5aIVB3U_EpUGz9PuLY2MvBFhARyNimSdmUUsWLYJCVONrnR2iBwcAhVnS5bEM9a-XoJewMhbWwh6LgqFiDerb8Yn3cib9zHsOgfhFLkH5biJFIEAsxYKSVxS_BenJxzuOk592NMl-JGALo5QzzvEu50N1059bfyy8FnXnzYRqY3gtIXthC8X-hhJD2IGIFBKJfm06iPyymDnCLumQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
🔥
مسی به این شکل جام‌جهانی 2026 رو به پایان رسوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/101250" target="_blank">📅 02:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101249">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🎙
👍
لامین یامال: "لیونل مسی، بازیکنی است که همیشه از کودکی به او علاقه داشته‌ام. من بزرگ شدم در حالی که او را تماشا می‌کردم، از او یاد می‌گرفتم و رویایی داشتم که حتی اگر بخش کوچکی از بازیکنی باشم که او هست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101249" target="_blank">📅 02:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101248">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s66-Gm2-wJfX5jcYijNiyiWoaYUyYSSUu-conAu13UqfdzMjf0iEb0gC1egfqbtK_2aDXuoLwHzKZfZww9VDqY8j6l0bdkTGKubMjpscZ0VFjdyBVKCTXG7IdvOPHnNlM4M5vzJ9xTC5tVX6zGluHLqdwL3uRyO8sMHwG99806LjFFTeEUChzvwqrDV1lwfDvQ18YONKtBHRUJScqSJbnA9WK9jiKVtBjxdOkJhEhGwyIe3qFzmyCubeCW-cVtvSPv_wp-kg5Dk1xaLSrMo553Iea11d409aPSZvQh8uMK2NpWKra086hkuSKN2YgiYtPX8Tl_uo-kR80Dpmu8VIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👍
لامین یامال:
"لیونل مسی، بازیکنی است که همیشه از کودکی به او علاقه داشته‌ام. من بزرگ شدم در حالی که او را تماشا می‌کردم، از او یاد می‌گرفتم و رویایی داشتم که حتی اگر بخش کوچکی از بازیکنی باشم که او هست."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101248" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPZTwNL_YiTLh8A10_Y-vQFdHMcqEhKMWhcI36T74ce5iVYD9tkDoHI5EIjr6N2DPJz21SEanS5nLBH3gnqH02n5652lBkyAgb_p9A1aY0PVuInNCxgmHvQrN0QI5KphSGDkqEKaQ2BKBnMCShYJEGR9-puwGmUbxmXZFt3aLMyT5pI4W6u04Fm069MZdrIUFzJG0vNdyxtsc7lP5vAhx-L3vUb7y3NxfCMJGIjyCb3RiSFKmz5V9svtz8rCz75RsAP_4PKVjbr0xjxjSAz73QbcF4yQw07k-uyAzGKIqungbQVd97aBAA40xozQQPCm81I0-zXglFUbHo6c5AtWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😆
بعد از بدون شکست بودن قلعه‌نویی، ببینید از دومین افتخار ایرانی‌ها در قلب آمریکا و جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101247" target="_blank">📅 02:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtiEfguSPAVXhbgZHp_OO2Yh70dXMZxUaPpocWYh4YrgoYfZv-wnSPbDEwFI5MA-4IewztikArXWYXJ-hwC1wkYIspWRL9JKyHvRgTb4IvYZNE8da4DEg9S_Y-vlgb3rHGM5wd9DeUyVkBgo043NrOfq6Xklf5L3FYGcMi3k1uD0EhFjvsdO0TrQLBVRiQYYiRpxxuwvNRjTDUfEZTU3f8gdea3jzlH7UYvtHGQtQ56zoHJnmWE5ESwAB0EcJasGiJNYokHkB-MbXeemNyTYJ-8zINX1s0KX0HwqXSZWLJRq_WcuobAUFjPxFHHri3BWGj8oFmxTGbuyOYrFUvwR3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
بانو شکیرا در حاشیه فینال امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101246" target="_blank">📅 02:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FvBJSIcS2yJTA0SyjeCq0cbWC3nVDyoXJo_sevhr2f9fYsd20lh1Kid7SKleJ_FrF34KmVZvVIWHPPdqBeQIWxhLpOXRQM0_XCoBCbBaee0Dewu0MXhB__WHx3ZC_g0pHKmNdaOIXRPj_1OCssnl5zD3CEl27fJcufPVXOqPO0z9Gxe8SFxqObtUglBCAJPAu6daN-1BHl5wIqlw4hGI3lUJPOJux-AsZHqBmOT59HyYONPZnAAPCgbX68S6ctNqncKkoK3m5Jzw2JD3rQ6F364GISx_UYfpIqDZlBaBscEribXrfd0OvffQIt6VfvqDTCZXVShm9Rf8EiZ2t8Lp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hug4HlqeXm6KOKW5PlaFmSTjm7A4dEEqdzSTQEJ4D2YgxywyE_41G41K4RpeRvoKzvMvND8eURuO4N96ZcjEeFs5l70njFKwUrz8R7mWlWlYXHZ3ROm7yWL3yyZVLj-WIJNtiLGc-2CM8TkD9VO3TtrinYnSo07FYTTtEWAFzC5LojQiNJtJSLdagDc-gfRJ5UrSyc2cXecU9BiL5XZFAtUNkcG6ypNj9Rxx4u15CizLWX1Up5SAMxNBXU0CZwAPFBqPXFATdPsOLorBhSH3EmwdbrHR-8GlwfRaxjEDeIc6E26ozVx6VblskJqwMJ25zRZ96wyZnWQjd-gazhWVCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جذاب برای فنای فران کوسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/101244" target="_blank">📅 02:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taB6QwwA8o_GnvgLu-fXxPAKEqqfjXXKCtm847Hl-DGzKmRn9csUWaYGtp2talPdwIHG85vrkZTVMl4VsLmg3HpPmKPZ39bVYFG86k7u2TNYNMwiuV-AoT6dxeZjDwW_cVdC6kOdtm7hXzczewzIEDiALtqWKLSD4t9v3v0OVGdP2h6L3rtpVl8LzOtFQjDGHRXnz1c_NLNDst7ifqLbDVjZk9z1LlRJEfANRHR5bcdIP5Jj39sIfNwvohGQMFIF2JNnTwRYnR1nBU6RIcUqiMBXAmGm3G3IfvNPELaCdhpzKElCirWc5cjNmXqtyEzRNyZQd0jMMpr56aznOaPO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🙂
بهت گفتم یه بار پوتین بهم گفته نابغه؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101243" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e244c0b930.mp4?token=d930oG9hlMF_Xs7f38iXt3XFU4ztIljPKIHgPfQcQelVdpqeIBPtkPu0M7tmQFur3m3rF8KBw7Kd0yFH67qy_auTtwhKa0a8I6Sru7wtTgXMRFC4V_PNCkLATzK1f8Xek6AGIEcp9HCHsFaEIbOwNpytO5fmMa_5tgcSqKzJrw18lP-PauAlvrqnLbq9Jl01IB75AJ20pMAstPYjZliGogFwm_M-JmYbsLzJQNaAA_P7PjQDkUznVAF5Z9ytXvNezOiwadlnfklMIz2N8wNtfZv5-INF81EeEf9JK8eaJtUgPcHQZTIbfCwnv9juk9q-RAKK9G2c-74qxqouodY7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e244c0b930.mp4?token=d930oG9hlMF_Xs7f38iXt3XFU4ztIljPKIHgPfQcQelVdpqeIBPtkPu0M7tmQFur3m3rF8KBw7Kd0yFH67qy_auTtwhKa0a8I6Sru7wtTgXMRFC4V_PNCkLATzK1f8Xek6AGIEcp9HCHsFaEIbOwNpytO5fmMa_5tgcSqKzJrw18lP-PauAlvrqnLbq9Jl01IB75AJ20pMAstPYjZliGogFwm_M-JmYbsLzJQNaAA_P7PjQDkUznVAF5Z9ytXvNezOiwadlnfklMIz2N8wNtfZv5-INF81EeEf9JK8eaJtUgPcHQZTIbfCwnv9juk9q-RAKK9G2c-74qxqouodY7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب دیگه بریم بخوابیم که جام‌جهانیم تموم شد
🤣
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101242" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIzaNeqQn-8701uqR07Y470QVWjqKe7eDyD-Sa4MpgVcIG2As5vhy0pMN9oulnOib0bazNB4Lz-IEhL_TaVFA3fHIBx4Fd42Ae-qMGc19DbKpU8QHuxyaKAlUOcFhcpCMpSDnvga8UUn8czDzoHpXuZW6ts9m7Hq-RJYqZpT5mj0tSUOXd7hGqX_ZFT6G5fmRLK_KdyILLbz5K7l_NuedDAeHrZTw__XBk7DVNCExE47ZMduonP3oKRV2YrSEhWN9pfJGpQPLYox5uzWgEgGG_GOE8-ul4vqlDzzNAkw4pfWijgh8q4CVyS4rLwim1ux7mhjoCbsDzeWQ2Z3SCvN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لوئیس دلافوئنته با جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101241" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtibGt3DfkQMCvPBLtVlGyM-NIG2pDmfqaysBziyo6MxJPkyiNYeW4We7ki0mtvsjvrxQdR4T-NerupMUYBIPLrCO00QG9pP5KwuGbTNmNsAAa34fKgYfE4Odr10EYvVUvS00ZVR3ZRkaStoKVQ49HT0QeE7m6Glv46UZWPcSZyIXWsfiwhgtW7z16_5TTVToI80mgCIcHyzqSpYbtzH2q8bkSp1B7lqTeV4R8nZZ4Txbi-PSPKYypZ9aaTr21zXDbtJ7Ay-HgHG6bAW5l6oagJD3NI2GrKUiVcT4tFr83yb08CpvxtWLJye-A5Ouy0BTweSCLhDRQVvnOpC-boaPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
اشک‌های شدید املیانو مارتینز گلر آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101240" target="_blank">📅 02:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohdI_ik8VeSeK4eRCnbO_OcDyhpYB8IeA4VkzCN6_su95FRYKQCrEoQWSRmcU6DaDdmiUxHDtH-er8MGF5oT_n2WYOBaJ6kwVaVy-GWpYGr6s5WkvLvPRqzBNFZzQWfCFMX3o0yfaZreV5g7UR-K1hsy0iyvSRWGu1yH-TXAfSrj3ymvLOF0ThGUsUdhMskTuxlSqkDEfH5ZITnkneLU7Uol3kNn7kTZdROmSDW6-lJPLR0g-_zw2WK0zzRNoNTj9xD_Fc7n24GfMksXSU3swuT3YW672TVsPxlJC4diXFYzHxAo2aHQkUWX3QOyDoK7Sd2Onzzkgv5khO6UXT-ZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
😆
😆
۱۰ سال دیگه فران‌تورس قراره این عکسو نشون بچش بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101239" target="_blank">📅 02:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101238">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxVbh0Y2O9VLAz-V7jXyoxNa55roCIEzDZ_wH7xr8gSrYJR42aaHT7SHs6DDJAXzrxFqRYantiTA1mmj0rqZ4Qq231LttIG1soeL_Ipn_03bBo8sG7vgcAyxNDuzu7pmLJrkYDnjPD640dyGQ6uOvlJcjCInhBRQ16LLe3QwYKtzeuLq2-sQ2MUlJij0UiMtfgQpQzthMD1JgMGHKBnVPVMzN4H3uMxob9Z3Oayz0Hs12ZKZ7H_TDybeDm1sZj8t2O4WB25eQV-Ayrcdjm6Q6khJm0EVmlz5bAagurUIgMPVALkOavJZ5C9oCR0Kmzv1qlNnfAD_jNgNfls5MEb3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اولین قهرمانی جام‌جهانی در ۱۹ سالگی برای یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101238" target="_blank">📅 02:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101237">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6713412f.mp4?token=VhH2tHxCulPyfxHtaCGpuuJNqoRMGwjBXDJ9oyoqk2TWIwDz62Gl5VcEZOvYiYQIEl9jKywQ0yLu0Ix9Hzc49sVID7ZkynSDeRTMW1b1z8MDZaDVhiEwc6mFumBxVzF-LtIsCDAC2TMusMoBUOlbpE45IoykEVqcF1-EddYHzcwyIAqpV1GyoE8OwJ0QWsUHJX7nFA7mz8roIgTSYB_Mgm6n0HIYRY-beJRj3wEjsXbbIzGLLwofThNa4uwc2qyfAOAseengupPQLx97PXtxE-OIyBAAAqQ1N6L3Hx6AHpOQQlQC4_LbU2KnyHSauUJN_b-wkkhKP70eWkvyNu5-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6713412f.mp4?token=VhH2tHxCulPyfxHtaCGpuuJNqoRMGwjBXDJ9oyoqk2TWIwDz62Gl5VcEZOvYiYQIEl9jKywQ0yLu0Ix9Hzc49sVID7ZkynSDeRTMW1b1z8MDZaDVhiEwc6mFumBxVzF-LtIsCDAC2TMusMoBUOlbpE45IoykEVqcF1-EddYHzcwyIAqpV1GyoE8OwJ0QWsUHJX7nFA7mz8roIgTSYB_Mgm6n0HIYRY-beJRj3wEjsXbbIzGLLwofThNa4uwc2qyfAOAseengupPQLx97PXtxE-OIyBAAAqQ1N6L3Hx6AHpOQQlQC4_LbU2KnyHSauUJN_b-wkkhKP70eWkvyNu5-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
لحظه‌بالابردن کاپ قهرمانی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101237" target="_blank">📅 02:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101236">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mLtNkXFiJ5OErFftaq7V4upSl5b6RwPGu6VjV66Xb5uvkc2wPyvg_iajWIugUthbbT5HPQGN7gXxpbQeucJ6hJz2lL3-hvdXHdE8vk2VP6W7OOXOo2q2SKOzYn_fL4y05pbzmsxzPTA5f1JdDzV0fY8BwPlPW6Oapexd7oKdZwc4YzgVCZ1q5Ej2837JzfbPdeL4J2_nMbIT_UxV5uEgqVznWwntfcQpagRDi1Dp4xEVTzPQQKESCb9UNNtwFWCrUCUSJpM1GZlS0dL8eIsvybk4IUfYiFTf1vfizFFIkiwWP9OQp5xJWCJhl8kzdXJTLTWcn4Btv82XsRxte1D6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
📊
با قهرمانی در جام‌جهانی، شانس کسب توپ‌طلا توسط لامین‌یامال در سال ۲۰۲۶ به بیش از ۵۰ درصد رسیده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101236" target="_blank">📅 02:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101235">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cz8xUq1FsvMNrQwIkfJxEegsHD9hVnlAW5v3wg7E1hgDIlmyOhhtG5QHWLv9Wy4dOiretGOXRXda6NenMIt_uwEem6zx_RYRmR6pzUAImLnRvmuhW12i7ecpnF0kTdZ8xPPk1vKUDk5LH5hd2X3dn25MmBRkY61T_pJZQhZijhjBBJfGd-rJOSON3j0sZmPPEGRn-h5bPKl3iewbEiJ7PSCiRe2HnmnwYNyDlPbHRzN-Q7VK3J1C1g3HwxZPogERIievDeh_gaXi8XMf2LGZWFWaSXiANloYAGCwoqDCcsPG-G-hQ0-KYYbDC5JTNeLImoGKnNlLosAuCQXXROQCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
#رسمیییییی
؛ تیم‌ملی هلند برنده جایزه بازی جوانمردانه جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101235" target="_blank">📅 02:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=sBdAjlT8FJ1GICLCdnY5Rvo9pDoctJ9FGoTJb4vh6OimUQI23dM8xPEiFN3WUYLoGxpY6_fBza3nb0UFCpn6WoQLxeXZUxXqGx3Y9dYFDNJGP2NbDDi-c0rn_jsgEZZn6f-lXZmcGFWw5Lv7dYDd9bjD0UkLvw7YPgqWmxKaSdgpn4jdB489_F21G6wsL-Ab_wQDVkpzcyM0bwcKc5waOE0iAz4qDGHTUY3RSo08H6GZOsp1cskfNFA6P1xsTC-yNF-y7dqr0Hkqjdjl7wDNM6eHOeKrfGIWTlTIgvit-Xbtazql16iZ-HR0_z3nO3DFX0w28I-KRVgfakKM6E7fGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab00af27c2.mp4?token=sBdAjlT8FJ1GICLCdnY5Rvo9pDoctJ9FGoTJb4vh6OimUQI23dM8xPEiFN3WUYLoGxpY6_fBza3nb0UFCpn6WoQLxeXZUxXqGx3Y9dYFDNJGP2NbDDi-c0rn_jsgEZZn6f-lXZmcGFWw5Lv7dYDd9bjD0UkLvw7YPgqWmxKaSdgpn4jdB489_F21G6wsL-Ab_wQDVkpzcyM0bwcKc5waOE0iAz4qDGHTUY3RSo08H6GZOsp1cskfNFA6P1xsTC-yNF-y7dqr0Hkqjdjl7wDNM6eHOeKrfGIWTlTIgvit-Xbtazql16iZ-HR0_z3nO3DFX0w28I-KRVgfakKM6E7fGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
🇺🇸
اهدای مدال طلا به بازیکنان اسپانیا توسط پرزیدنت ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101234" target="_blank">📅 02:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOmSwR5RRmnkWjEMhyPREX0g2C1bqaLzguwzNVb0CgrAGFJjclQ4Zb52FrRU7D-WoIOzqEC1412wCMISKQeOYw4LxxHfNk46IF-i3TDa3mJ5nV-zE7mOS1U9NuYEaWOkWn6QkBclhWtRRqJX6KQ3n3NM2HoqzOCJ1PH4hn-sH7pgT0QtcOpYfXsdmq0Zsx64WmpzTelgm3XSL1EfDMJX5KlYQl40dTZrDREEzJigYD9-3KP9gsKpyB4q9yI4wYSH0UAsYdMHxgOyEfw1KVxDZJI-90_Lcz-ijA6Wk8y6_fcuh3Cl3RNlftjuUlPFNUCucgQkb258-rO-j0Et2zjb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🇪🇸
و سکانس پایانی جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101233" target="_blank">📅 02:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لیونل‌مسی همچنان داره گریه میکنه
😭
😭
😭</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101232" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTM5A5Gc0Q6AWtwv_T_NznOtAIloD5l_kiGXtCuAIv_c1UA8MuC7wL1MPYyEnR8kZl1cQb4Avd9iwQpwje3o1VfY6XYHUOBfV8JoqCdjO4O3EBNBh2yaBN3Qrn-FFq-2HUIy9av5vDRew8RtRrdCZwCf8C68Q6YvEgNLCqFbrIQcJonLp9acHX1MUDtRR63cqmh92NKgAz2O6yPcw1sFXWQV-W966p8TLdNdJV4vNj7xsvkJts9CPbL_KxBolpieg7-DeMsPV5Vg4JX_i3_IwM_q9gBprEsG78N2Wk10VTyTCDOEaBv6-uKLzLg-EzCuT4e-vwfrSMy2ngV1ZNZXJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🇪🇸
و سکانس پایانی جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/101231" target="_blank">📅 02:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJUSw8NAWLyyQ7KAwgxPWNF1e1jtopKA9gVOw7PnRyFUlHHRbusRRGgnuwQcMJiitf6Elktu4AWGfAKm91BS5uCaZRp9GwAQByDFDZ4morT23zdAoUWsnuVQWFBr2v1KMMCi5W5osFa3dut6yJfH4LkYCAoF5QJR-tXmTiR5FBYEAf5gvMfIQTg6_UX68JWSfRlZeAonsAAPH15CUPEtQkE4WLy4vcEW69R8j69Pvl-TQdtKRGzCtj9Mr8Rz5U6gDD2HTokIS8rZBdd4jlDVjrmYOt5e4lrJHW2JS8fjysxZCpdhBZk5qL7NXz1Q987n9MDm2RP--bC7_CKYneEiDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
یکی جلو داداش یامالو بگیره
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101230" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb8a66352a.mp4?token=veYVsEE6YOvqI7fdz4h1ZjuylbKpuJStwyiPyJas_Dqb0XgJtVl2pwtf90ptGmEKP4fdNoENaQAl1UKhgRQHX3Dr0TbrX7oXfcwNUImYfLboSQMaS6LO-e88naeijmJLwpBm07H73oHZS9lx_sQ1oOWavFMfyQQ3eo-hzShaEDETR7wcUHyHx2ml6BDZ-WDMMTayRDwmugFTlgXYDFgyEKbF5KPw-ooNpP2ZWF6NZGL1Je0r43OwPUagCzBN16otL-dr1Tj5lf_CYepRPJnTnhM_SE0llEopQSllqW_8DRCzYjHm9KwwKD7e4qm10dFFXWHHOlw2Xdys9M4TN9QloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb8a66352a.mp4?token=veYVsEE6YOvqI7fdz4h1ZjuylbKpuJStwyiPyJas_Dqb0XgJtVl2pwtf90ptGmEKP4fdNoENaQAl1UKhgRQHX3Dr0TbrX7oXfcwNUImYfLboSQMaS6LO-e88naeijmJLwpBm07H73oHZS9lx_sQ1oOWavFMfyQQ3eo-hzShaEDETR7wcUHyHx2ml6BDZ-WDMMTayRDwmugFTlgXYDFgyEKbF5KPw-ooNpP2ZWF6NZGL1Je0r43OwPUagCzBN16otL-dr1Tj5lf_CYepRPJnTnhM_SE0llEopQSllqW_8DRCzYjHm9KwwKD7e4qm10dFFXWHHOlw2Xdys9M4TN9QloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
💋
ترامپ مدال نقره رو به مسی اهدا کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101229" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=cGF46i0heiOCU25Cet3UqHtcmqBbxzL9P0PWUDGx_lzzeXHv9psZ7w7PRfmIIna39rsiJZNbYejxLbPUPuiOE85gQshLElTuRFERYNn9IzVMHowDf1HXVuEa5nm_jW7aPO3CyRYgD4-GnyBIdbWXwegoAWHIImf-sk8ZEbByAlTZCoF993LhA7sRqBkBUFeFF8quG20s06AFgVrVcX_vhaS_YOk8RXIPKD-jXkAC5aRmugqxVSJ90y069nCTiubTZhdgQNcXNujSgy3dbqGsfB1rBm5RvMTFPRwSlRYVyqZ5x4VDfePl6xzeRFo9ZesZAOhE9K8riXrsM9xlEBzkjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecf5e7ca.mp4?token=cGF46i0heiOCU25Cet3UqHtcmqBbxzL9P0PWUDGx_lzzeXHv9psZ7w7PRfmIIna39rsiJZNbYejxLbPUPuiOE85gQshLElTuRFERYNn9IzVMHowDf1HXVuEa5nm_jW7aPO3CyRYgD4-GnyBIdbWXwegoAWHIImf-sk8ZEbByAlTZCoF993LhA7sRqBkBUFeFF8quG20s06AFgVrVcX_vhaS_YOk8RXIPKD-jXkAC5aRmugqxVSJ90y069nCTiubTZhdgQNcXNujSgy3dbqGsfB1rBm5RvMTFPRwSlRYVyqZ5x4VDfePl6xzeRFo9ZesZAOhE9K8riXrsM9xlEBzkjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇦🇷
🇺🇸
لحظاتی از اهدای مدال نقره به تیم ملی آرژانتین توسط دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101228" target="_blank">📅 02:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQdYTxI2kYvrDw8Ch5jvJqe03GZ91cX6Re9sOQ4FI7IIYP1v9XnJFrdAZrWL2EQduGR7cN-IUotPaItPQqzD5SqAIXToLh1I0VHyIebCZtEBQ7yJ-i_xuAUTZScCQlZlyk4uXwhiAB4PJFQBQfK-pWVt4BJYzjaCO3bN3qvJsqSqdlBG_B2zg1-tJWrNfpzBKNuMMMRaXEFRYpKRh7nSAveABT7qdXsphSAOfX2SXhqah8RFLMg2PgbWqan_nASziPOB9OFsdqhGGR1ndgDi6bt35tkZwo3Z1aKRLdIifhXvPdercQLbUC4hsGH4ceskMhQd8fM3F835ZgPEE93uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اسطوره فران‌تورس درحال دریافت مدال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101227" target="_blank">📅 02:10 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
