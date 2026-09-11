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
<img src="https://cdn5.telesco.pe/file/KKjYoAEBi2oaAPOpqi-v47KKX2bhj9DZPxeIXfg9JmDtDZMXa27zhNkXTydUp6pD5BU8w-ZpgjnTp-qP5XeG45HujCHjYzFj-gruzH1ZQdA5wXb253iT9gaNRYav4JYK60XBs77x_TsdGRJLu1i3U1ogenpFmK82BZKGa5u2vBy0vznnyFVHtNlaLOs4Plr_ast1HO9lI2svR5JAIAdihfTxc-6LqYts9BCaJEtk3OmcUOKD3xtMdqA0xNST1WcjpWUO4uR0FTx2Oe-dW7g5qPoRc2WwhVGWFowyhD57I26L0pynOAoC1F2Ls-kldoompYvyJYmhbIdFgXmqGmpg4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 418K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 19:04:30</div>
<hr>

<div class="tg-post" id="msg-106231">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=KVjhAoV715oLQ4q85fmlMHqX9F701dZZwTD_OYH7NiCv9e6WAheAsDB2kpWP8BnwI1tMQO2YceTsAq_0JXUoSuzNvXczj19Il79_U-c3gUU2w36ljmF146yI60BpFKuezM9QqRoL-TrZDbu06BKQ6pYpkdlAKJme4ks_x6LAoqtpf20hy4tRuRArwwSwf0q_VisYKkMPGNVDiDic73Hw6m9wMnGtwtHOsLNMoSWMIAgVl_Js7bN4vutdDf2K3yIaeX4L91iqhmdYugqwN65zsRu3cjMGEERAq7aS2I8aJFs3moULk21HXXl8IfJLOJ4h4t383SnHPxmqhVLWFFOlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=KVjhAoV715oLQ4q85fmlMHqX9F701dZZwTD_OYH7NiCv9e6WAheAsDB2kpWP8BnwI1tMQO2YceTsAq_0JXUoSuzNvXczj19Il79_U-c3gUU2w36ljmF146yI60BpFKuezM9QqRoL-TrZDbu06BKQ6pYpkdlAKJme4ks_x6LAoqtpf20hy4tRuRArwwSwf0q_VisYKkMPGNVDiDic73Hw6m9wMnGtwtHOsLNMoSWMIAgVl_Js7bN4vutdDf2K3yIaeX4L91iqhmdYugqwN65zsRu3cjMGEERAq7aS2I8aJFs3moULk21HXXl8IfJLOJ4h4t383SnHPxmqhVLWFFOlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
به مناسبت سالروز واقعه ۱۱ سپتامبر یادی کنیم از همدردی مردم شریف ایران با آمریکایی‌ها؛ این درحالیه که کشورهایی نظیر عراق جشن و سرور به پا کرده بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 482 · <a href="https://t.me/Futball180TV/106231" target="_blank">📅 19:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106230">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URm56nhe7ooyqOZbhauxqi5Mc-cGW8Ayj9PCf1-p3w2ZSJ4m3ROj8Oa3gph1c-GMc6MK9i6hyaWiSl8__Cdl9VzzEFiha6--WkksYahMCQjjnTGlHLJfKJau-ZvlOksl9b0RcFoCoDzXaVQ_hKhD189AH0AhGWBJlEibRcd8kfGOstJfvQdn4cgKnPYbgKgfkV9gp1DDo63NrF_kQsjy51rMAKid263y-lCmE34xqc4Jg_GR_82ogwmhgHC2_Ge8n8OKGGAYgbL5wyYytZBVnDX7uOEQQIBGkyAWvCG827Y9L8UixdWI16wnV8hriYIcIEkLKeXXS5zSCNyCJZrH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
👋
گئورگی گولسیانی مدافع سابق پرسپولیس ‌و سپاهان از فوتبال خداحافظی کرد. گولسیانی زننده گل قهرمانی پرسپولیس در لیگ بیست‌وسوم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/Futball180TV/106230" target="_blank">📅 19:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106229">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNJEJ_5LpyraOn7FouifJ8BNnuXgHTnUyOx6gJIgk-4-wjRi20VLO3gWVVaVq-PP8_y8fur-G4VfcETC4gSRcWnGSVD8xJxg-k6ysvria9mrvGc461TOnjfxEEr4uSYewYTFHXnOQcCfYCGlcRXCPogl3pahLHeCgNRlHJEutaN0ydRjxBZskrb_tUBPoPdm1f_Jxo52O2yMGUQYQW0g613lHerba_UBJa9ST6-EqWnZa_Jcl1nYLdhMChjoFpO1VYHnVaNJ2_FUTlKiW1IZuwmI-ldIdNlc4SdqKUVWt7btQ4YsEc_z1lII_r9mx4JEERln3x1OvrP2bDPvTPguEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🔥
🔥
🔥
اکتبر خونین که در پیش‌داریم!
🗓
🇪🇸
🇫🇷
20 اکتبر/بارسلونا - پاری‌سن‌ژرمن
🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
21اکتبر/آرسنال - بایرن‌مونیخ
🗓
🇪🇸
🇪🇸
25اکتبر/بارسلونا - رئال‌مادرید
🗓
🏆
26 اکتبر/اعلام رسمی برنده توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/106229" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106228">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/Futball180TV/106228" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106227">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VliDEZCNJZXcgt5wC_bpFUo72XloO4sOwIHDSq74PULqnRY1-PPeiuckX7MqBcVe4Ti-a-1CEdcjE7ECdwzXt1qwg9BcUTEteos4B6qjmDBOrnRRwsppgpKiHAWcD-7NGIrjZLxx1xGNZwP2QQ-c02aiW003wTSTOoYYuHFp8wRIgd6HeqhlTueny8R_gY1WFePNvQHsmJhCTXAuHV_GRfDaCUlWPzLd3LgDTWamp3sNEUL-YMt2ZW63ibWZx1LRKmegoF7d8-I_h_maAzOe6B5lsdFsjS0yAQaYy9kQ4iCWTh-WEN6E7dL3BRSSqmwKkUPnaNcT1VFV_UL7kkaEug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/Futball180TV/106227" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106226">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2YLmWotD85HHpPyghyeHUl2U7sRkYAevwbU4S5LG6_HZaFz2dySck2ZbjExxy8m3ol_gwaeihPywi78JSZWhtLmU7v__HbeK-Uc11H4W5Q01WGva-P-map65V4rvXpYUc5rLJzvHpvDIo605QNdR3rHQQyj1rv95x8IUeySoJkBm_k5pnMjqyiUfdc2nkM2i6K6S6B-q4zgV_SHrsFxd7Wv3_AxULVxPI69idXUgItWpCr8U3ip2r0LuHK8ANGE7cHTVlM2GnN7MUTQaC5-PR6wqSNYwyfcNoxnqUQoxqInfaDQcxaM_bVQ1VHewbNfOIy4BoKz3sRoZj3Sihnw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
تیم‌منتخب هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/106226" target="_blank">📅 18:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106225">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=JNKlsV_E_reZvEglkT8wprxJkYvGXKQ68q7lW-3i7DshqyJzWHd_Rk0spzVnuR3gSkSxqupFxF8WbIHYwVt9Gf6D_XjjbGl_oUSgoPcnAaWPPZM9Zv1JPPOUKbkrycB8b0jrbMRyQ9dRapxlsCeFWK9Kdjm3MWhH3NM1zmMZe0JGsj4dO3gh15ELeq0WTmWc4ZdMZObNVSYzJt023qhZmF8tTXfYheQJnXTFQ4P8diVpZVq45Op5jlNO8V7LEx-ZeP-lRHZ8ZsArXFchXu7DwudiZRE5DC-Vj4Tho2vO3vHHI4yu-LKmD6elWjwjTw6ESgtTE2xzX1Nbb8aYaAXYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=JNKlsV_E_reZvEglkT8wprxJkYvGXKQ68q7lW-3i7DshqyJzWHd_Rk0spzVnuR3gSkSxqupFxF8WbIHYwVt9Gf6D_XjjbGl_oUSgoPcnAaWPPZM9Zv1JPPOUKbkrycB8b0jrbMRyQ9dRapxlsCeFWK9Kdjm3MWhH3NM1zmMZe0JGsj4dO3gh15ELeq0WTmWc4ZdMZObNVSYzJt023qhZmF8tTXfYheQJnXTFQ4P8diVpZVq45Op5jlNO8V7LEx-ZeP-lRHZ8ZsArXFchXu7DwudiZRE5DC-Vj4Tho2vO3vHHI4yu-LKmD6elWjwjTw6ESgtTE2xzX1Nbb8aYaAXYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پخش‌صدای بانو هایده در مراسم هفته‌مد در نیویورک آمریکا؛ روحش شاد اسطوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/106225" target="_blank">📅 18:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106224">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=X7BxrVAcK9HF989Wt_cvUicgAxZRT46kGipQzpW99tqhwWrgheE0cQ1ML6NpC8IXUQ-WFHW-_8OIuRf-5auF02kFUbowYn9sgE0EzMu1QwslA952lvZeIKdL7sEimRNxgFfSFyViEIn85s8VJ8j2auHfFoF5WtW3jU6MNLG2fp3vTH_wzsSw8dxM9RsKO0s4fkiwyCHgmxYUqfEUjmC4EbxptDtueGXEOZCN61SQs_Q52UHMLdPk4GijcmnUbCz-7nZ0vfitpa-_6kmbavi3eawk3JK8WBrtriwyYaw93MEsw833HM77R_xV2Qe8tP0zv07OpvdBdmH4xxkye5jMEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=X7BxrVAcK9HF989Wt_cvUicgAxZRT46kGipQzpW99tqhwWrgheE0cQ1ML6NpC8IXUQ-WFHW-_8OIuRf-5auF02kFUbowYn9sgE0EzMu1QwslA952lvZeIKdL7sEimRNxgFfSFyViEIn85s8VJ8j2auHfFoF5WtW3jU6MNLG2fp3vTH_wzsSw8dxM9RsKO0s4fkiwyCHgmxYUqfEUjmC4EbxptDtueGXEOZCN61SQs_Q52UHMLdPk4GijcmnUbCz-7nZ0vfitpa-_6kmbavi3eawk3JK8WBrtriwyYaw93MEsw833HM77R_xV2Qe8tP0zv07OpvdBdmH4xxkye5jMEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇺
برخی از اتفاقات هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/106224" target="_blank">📅 17:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106223">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=pvoCg3sOJVORth8l0UNvt-ecDd770BqHobxnOkSyYjXHdrKhoTD3805gk0PRsZIJYPY0OmPo1urY8L7QMREMHsrW1JBZYu87YGEiYE-Yrxamk-E1-OO67x6slmhBLxkkGDcJIRiRtVGnwTUP3ZT9w22y57Z-kya5yF5mDi74OA9SvgPDcLFnxp-TvhUunU72M_KbHz7OPS4ql4ojSdCSzwh9t4ORudFFj-Q2zpbRwHYbIEk7ExtCX-nmPbSlNQjORTNlsowNagOwL0pVhCuyP0kgkcDub2LeZeRJ-eSZjQdDgAR_ob9p7zuWlyB5DytVXa123aScqBfwqcd-BrQA9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=pvoCg3sOJVORth8l0UNvt-ecDd770BqHobxnOkSyYjXHdrKhoTD3805gk0PRsZIJYPY0OmPo1urY8L7QMREMHsrW1JBZYu87YGEiYE-Yrxamk-E1-OO67x6slmhBLxkkGDcJIRiRtVGnwTUP3ZT9w22y57Z-kya5yF5mDi74OA9SvgPDcLFnxp-TvhUunU72M_KbHz7OPS4ql4ojSdCSzwh9t4ORudFFj-Q2zpbRwHYbIEk7ExtCX-nmPbSlNQjORTNlsowNagOwL0pVhCuyP0kgkcDub2LeZeRJ-eSZjQdDgAR_ob9p7zuWlyB5DytVXa123aScqBfwqcd-BrQA9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشیع جنازه بابای مسی با علی‌آقا دایی
😂
🚫
با صدای کم‌گوش بدید فقط
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/106223" target="_blank">📅 17:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106222">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8jduY8N4wIVfp_Co9301ycYNCYHDp0ztMsGvOxIjTl_0FLD72mCmdjtDVd0sYerhs6snw7qPetsS5iX_Ge9m3lNI3o_6hn7CR6oC2UsJA6fXGNQPnxY6C0p3aSOFeunpm915Ze9EcbLEM_y5UVKuhJp7Fl4favTwAXq51YvBx_T73m-sVCpKSLsz-lYPa2_Dz1I2PJ8izfsJ9G8b_P4r5usKwr-fwNfhAP6DwW308-7VplgHbGC21xG7fqsJJcS_zW2XhLoX9RH9jnPR77Ljs7_xYfi130OwPChKZyF0Q7it7SPjRGC9lIj4nGQWhYTaBSxe8r45xWhU8CIjuwBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
واکنش علی تاجرنیا به بخشیده شدن صالح‌حردانی توسط بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/Futball180TV/106222" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106221">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=RDs_PAWMpxuu25pcW5AS5Q-MeosjQgqmltsWUo7Tx0YwC-dkHJnY6CFRDTNyFs6TuASwr6dSH0yYSbe3nqKlZUxzW61iHyGxGlC10QZAXCdZmdBOXDncMZW5ihNLDMypUMGIl8pOLxldhCMtVKFViG_ii0Gi3D9Z0aeoOqCgOTd8wJQwQHsLQgl8ir0iOgbBVyXHaD_oMK2Cjg0Bzg5U9QYkL-XfEGbMTytUIC4sRMNhVzKDIrnsTrIDVafelQUClU-0Ou-EieusO1P-OG_BNNoH1MrpgDFwzuVKSuGNKYOZWD9LngFFd2yIwcVj_jJ0qw_zjVmiTGoADcciGQ1sEHj84RPrL-omVmcQwhiL1gSgUWTXNN5WWd_HvaoeznxTKnSiAIEFCMtyZiHhl6eE3E6IrSKvGmu9bOUK4h3EdGwo-7Pe2E0tqNsjrJ3j0PjKHDMBCYmspl2Ae8NWTB8jy21-bFyhfIP5Uvvwka6lv4rVP7GOsSYVwDLzshVLmeCU27TAksYhpp6P6_LBtjcvJrsCkr3up_19Nsg7cpn7CiXc38k0PeqvuFBMBGKKhuhDZeqO4jkXE79yziGPJAvmP17fwHTpsesM88ehpCmDKf1lDawgQiIrKLcVWr-EqKEUzyySYQRxeSnm13h0TewwN9f9a2KKiZhINXlx-OCN2Kc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=RDs_PAWMpxuu25pcW5AS5Q-MeosjQgqmltsWUo7Tx0YwC-dkHJnY6CFRDTNyFs6TuASwr6dSH0yYSbe3nqKlZUxzW61iHyGxGlC10QZAXCdZmdBOXDncMZW5ihNLDMypUMGIl8pOLxldhCMtVKFViG_ii0Gi3D9Z0aeoOqCgOTd8wJQwQHsLQgl8ir0iOgbBVyXHaD_oMK2Cjg0Bzg5U9QYkL-XfEGbMTytUIC4sRMNhVzKDIrnsTrIDVafelQUClU-0Ou-EieusO1P-OG_BNNoH1MrpgDFwzuVKSuGNKYOZWD9LngFFd2yIwcVj_jJ0qw_zjVmiTGoADcciGQ1sEHj84RPrL-omVmcQwhiL1gSgUWTXNN5WWd_HvaoeznxTKnSiAIEFCMtyZiHhl6eE3E6IrSKvGmu9bOUK4h3EdGwo-7Pe2E0tqNsjrJ3j0PjKHDMBCYmspl2Ae8NWTB8jy21-bFyhfIP5Uvvwka6lv4rVP7GOsSYVwDLzshVLmeCU27TAksYhpp6P6_LBtjcvJrsCkr3up_19Nsg7cpn7CiXc38k0PeqvuFBMBGKKhuhDZeqO4jkXE79yziGPJAvmP17fwHTpsesM88ehpCmDKf1lDawgQiIrKLcVWr-EqKEUzyySYQRxeSnm13h0TewwN9f9a2KKiZhINXlx-OCN2Kc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
یک‌دقیقه با کورتوا بهترین گلر فعلی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/106221" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106220">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=psw00VhHxpJ_Aw0GzA3tb6ocpNDgMEcRoN3nxMI3SaueavD_KK_7lmgsRl0250sNO_NWu5yAMwyPODjGnoUYwOO1vmOtQeBh5dWE8CPJarPSuE-9rG8PxkMKl4YiXtVIcu3RgNtXJoS43_5x2jKcbEQiDD1rtttU8Bt2g_pIIg7H5zRgB3MnWnISnATIqRqq39IYAoHHmJcknKbKB2OEFLWr6ZNDkWVgAI60GS0-wbO7aAtX1uwai9QXzo-zW0uvoj3PKpHRACWY1RAvxjfjJNuTgzTGnAjh3m5mrZSo9U8EQQ8EJ56_zOMj3cg-qpsh1mIpw6CEuWEFZOy7_BJAwAGHy0bsosiYtQMRMxzGI8J0rPpPilQ3aUMCbflEg4OsG8Mx6hCqVVRe7p9VwNytzxk8CYYmrpPL8UcMPDuXA_a4P6XuyQm-yC7zZ6hWscIeuOgUoKKeaVMJIpZAW6bNmun0l70jyWcwi6FNZv3aoPMMY46G9Qju2dEALWLqzVWfywIYp1WeBl_lPObpvfQ1-m3bmAgBlpFelIyFgq1fnbD9-7LhRhbIekGKrQ5qIld4UkCgW_4Bz4mKJrMiL1Lzqu1AB89M-sry3aUL-1Z-gXqaaUzRQ9SCYiAe3hEU3OQQbv2FF_YwaKjlpwc77IsLggwBC47p4iOopxB3LOEpXTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=psw00VhHxpJ_Aw0GzA3tb6ocpNDgMEcRoN3nxMI3SaueavD_KK_7lmgsRl0250sNO_NWu5yAMwyPODjGnoUYwOO1vmOtQeBh5dWE8CPJarPSuE-9rG8PxkMKl4YiXtVIcu3RgNtXJoS43_5x2jKcbEQiDD1rtttU8Bt2g_pIIg7H5zRgB3MnWnISnATIqRqq39IYAoHHmJcknKbKB2OEFLWr6ZNDkWVgAI60GS0-wbO7aAtX1uwai9QXzo-zW0uvoj3PKpHRACWY1RAvxjfjJNuTgzTGnAjh3m5mrZSo9U8EQQ8EJ56_zOMj3cg-qpsh1mIpw6CEuWEFZOy7_BJAwAGHy0bsosiYtQMRMxzGI8J0rPpPilQ3aUMCbflEg4OsG8Mx6hCqVVRe7p9VwNytzxk8CYYmrpPL8UcMPDuXA_a4P6XuyQm-yC7zZ6hWscIeuOgUoKKeaVMJIpZAW6bNmun0l70jyWcwi6FNZv3aoPMMY46G9Qju2dEALWLqzVWfywIYp1WeBl_lPObpvfQ1-m3bmAgBlpFelIyFgq1fnbD9-7LhRhbIekGKrQ5qIld4UkCgW_4Bz4mKJrMiL1Lzqu1AB89M-sry3aUL-1Z-gXqaaUzRQ9SCYiAe3hEU3OQQbv2FF_YwaKjlpwc77IsLggwBC47p4iOopxB3LOEpXTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
واکنش مجتبی‌پوربخش و علیرضا مرزبان به تصویر تلخ دستفروشی یک‌دختر خردسال در استادیوم اراک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/106220" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106219">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6ANU2-kyxp-oxUVoGEpntamnWrdqSZok76D2u92h84R8oo09qa92TSZVXDj1TfpWrl3ccTiepWGTE-tljB2Ii_Cnz0zPYvsRoxW3EZ8bqi7f4S4MSUInSdrKhLz7QfzhDxLciOOdonpenZSnJIGJus6RccERcnUU3SE3HAqrvN0lCQpx1FUoHcL8qoD_lELA-barf-pQVeYabE2vMgeW0qv_Xm5mC7S1Q8bhM_kQeQ3mrzkCeWzuV7Rh6JfhS87UkDqsG_jnC2S5Fq8bkc7t_6WRYUUR-yqMjyfi8tXTkQassd4jbdWIf_R219TTVSs6k5-povPXWiiLaIUvCqLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
📊
🏆
سوفا اسکور: مقایسه میانگین نمره رافینیا با نامزدهای توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106219" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106218">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kth7B57sV-h_kMvnKBBJ6ghtlqmcPeHc9BLQW2dZmn224572_yK0NiGol_RMVYzFal6hP3GvfHNrsubnVCtHEaT-wBJzyA3uvY5yPsundCwM-d2LW8w-bXMF1LxyP3MzievyX6bEj6Envc0ZQDQIoYH7yr1E8v6JhOvanJSmb9ecH5VAcZ6_dMvCEc7P_v7w3g_-ti8Y0n3UqC4aPFVNNccSJeIS39VpaLRzokS8I8rsKyu6t5qszLhyRk7uzH2h-eVy-Sd32Uf8SpzUAEhfKRuVIikUzad-_6Y3CMXbAiykP2YWr5z5nmV6H3EGtBkKMKWwZZu0ckc8KSKIPLnW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
امار و ارقام لامین یامال در کریرش
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106218" target="_blank">📅 15:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106217">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=c7-ozvUJ9uR9ZmQpL07alevuQstbMoD15Juq2QooF1GfGgFO9G_4nSK20PoX0qh9t1qZA1aP5Uvw7rviTVJAT0vjAoOP9969H03gj_FSoH2bEiO4sLnohTSK4f-rtwbR9WRc1IrhxTySm2N-7KbXdwI0NPCHeYI9god8GnTlPHF9qwY4rOS-UjnufpKqmi-fW5PqiMSezzzWeZyY8vWzJGmxAmuyB6VlRu1mkDFmbxR7X3POO9NuCFekSV84XLwybksa8vsl_Kg2gKn0cx00caiCfoniPv3M2jg0JNndO8xau-OF6L1nxZgBWpEVIHLpIKyH3_ShgJaoBDXOL6rt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=c7-ozvUJ9uR9ZmQpL07alevuQstbMoD15Juq2QooF1GfGgFO9G_4nSK20PoX0qh9t1qZA1aP5Uvw7rviTVJAT0vjAoOP9969H03gj_FSoH2bEiO4sLnohTSK4f-rtwbR9WRc1IrhxTySm2N-7KbXdwI0NPCHeYI9god8GnTlPHF9qwY4rOS-UjnufpKqmi-fW5PqiMSezzzWeZyY8vWzJGmxAmuyB6VlRu1mkDFmbxR7X3POO9NuCFekSV84XLwybksa8vsl_Kg2gKn0cx00caiCfoniPv3M2jg0JNndO8xau-OF6L1nxZgBWpEVIHLpIKyH3_ShgJaoBDXOL6rt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
از مالیدن روی آنتن‌زنده و صحبت از قناعت تا عروسی سوپرلاکچری سامان گوران مجری صداوسیما
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106217" target="_blank">📅 15:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106216">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=AnBTAfQKYgwMxVI6rYOWJy2nfyPlXPRO5HM_gPhjZ7qf6Lbit1vzIMXyRbEGlUC9z2ADOEdx0FuIrP2JtAzJ2BXY20ycak4q9jBOzTm41M_3LEbt0CqOrR58u9oqrZ2Y0rFch2oHxcOTgDkRF8156LOtqiS_q6h__7E-xu0c49am_CWz2xA0exST7-G1kwMZRfR1H05JK-XsSPWip2saD8mKAiXp1M-jKWZc_9q4Shzp8Nkr5g-_4evUKdxJysZPA61VmiCvRhcjZmVsto8jfPt24ytSmZKpzH-ZszfWiOTieQF4Brk0-Ojx9QioJTn3rdNSTWobgTnB8yIZkGVNSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=AnBTAfQKYgwMxVI6rYOWJy2nfyPlXPRO5HM_gPhjZ7qf6Lbit1vzIMXyRbEGlUC9z2ADOEdx0FuIrP2JtAzJ2BXY20ycak4q9jBOzTm41M_3LEbt0CqOrR58u9oqrZ2Y0rFch2oHxcOTgDkRF8156LOtqiS_q6h__7E-xu0c49am_CWz2xA0exST7-G1kwMZRfR1H05JK-XsSPWip2saD8mKAiXp1M-jKWZc_9q4Shzp8Nkr5g-_4evUKdxJysZPA61VmiCvRhcjZmVsto8jfPt24ytSmZKpzH-ZszfWiOTieQF4Brk0-Ojx9QioJTn3rdNSTWobgTnB8yIZkGVNSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
حس‌واقعی هنر در ایام‌قبل از انقلاب با حضور ستارگانی نظیر بانو گوگوش...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106216" target="_blank">📅 14:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2irbqJ6dm3V7E3l8atHQxS8u3FK44Zmc6uYwm5AoAt9b89S2TWIct7pWogFSQFJ7znxvlGw5xJYe3GFyuUUs5eLr-7qSBSXLuJnJk1vKRnpQbKJyXcKHsu5Tt6P1V5M6yRn6o5S98vegCLL4vp0Yot8KS2uGUzWLo_FbuCRD1BOY4vXULoL2kRXYkVaiaV6KEqXhmjFzRct9iSa_jTQlG4o90Wl3APWsFeoL21LyIeBweg6zRMRNJef5Yt07G5eFAzloWYativaIud8qSgKQ3Iod7kfR-I6go93UNtsZaKQJDTbsYcyed9vdwsoRlBVHADJWr_dsdQELcpGgCs8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
عملکرد فوق‌العاده رافینیا از شروع‌فصل:
🇪🇸
الچه
⚽️
⚽️
🔴
🇪🇸
بیلبائو
⚽️
🇪🇸
رایووایکانو
⚽️
⚽️
🇪🇸
والنسیا
⚽️
🇳🇱
فاینورد
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106215" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=dwgjocTWZsMoMigas1p44snyxg8v6zgpdYXnLa6fiwAXG_nn-CT1M_GttIpLB15i-PUf9Axl-NigizARuy_mD7r9roKfV1iSDIRJH8BRUeta13toJEeNdBdoyCwJzk82i7iKl6VINOdSgZ6lwKCXryeBwdFxXx0_Ox9IxLAHxdRM3D7PdJJ_k_M3fCxVh7z_Ue4061DDbti9dnLw1tRhU7xQ_1c631s-s8ZeyXrQBwP8c5zdsAX85gz846sVCCss3jxvDNQ71L4c3U0MDi9i7W_vVBGCNaiygsubhNQ4TInDgBh_5RwGDCcvQypebIzGjANoG3elweJep0L-2A_SIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=dwgjocTWZsMoMigas1p44snyxg8v6zgpdYXnLa6fiwAXG_nn-CT1M_GttIpLB15i-PUf9Axl-NigizARuy_mD7r9roKfV1iSDIRJH8BRUeta13toJEeNdBdoyCwJzk82i7iKl6VINOdSgZ6lwKCXryeBwdFxXx0_Ox9IxLAHxdRM3D7PdJJ_k_M3fCxVh7z_Ue4061DDbti9dnLw1tRhU7xQ_1c631s-s8ZeyXrQBwP8c5zdsAX85gz846sVCCss3jxvDNQ71L4c3U0MDi9i7W_vVBGCNaiygsubhNQ4TInDgBh_5RwGDCcvQypebIzGjANoG3elweJep0L-2A_SIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمین یا بلینگام؟‌ کی بهتره؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106214" target="_blank">📅 14:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol_imBX8xhehwAP0lBc3jyH0i8uPicsqny9mBLQCEgolEE1ASqOCWZDFJZKBbaniaiDUrMkVcFw2PYVc-0p8c8w4yaIek6BzH15dOxLcCaoselbt6NCu_y6MrcZ5E9dkJpJMJGWj8IYSBgL4UJINAp5Be0TOzADWFiie0KcngxnJsGMKjoPW_HeZqcV0_TvVdwWaCiwC1nh4YnHIttRWm6HxEQAhDv2RXbRm4QWijzShldtR45I-m_pyCuzfI-BisuTU2n914dn_2TC52gv6hapczimcOE5YRz4VVm8afixrrT9nPSiL09iBbU7tnZm7sctY6-Uj2IFd8yQtc-8z5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد درخشان مورگان راجرز در چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106213" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=ZpDi6BcNhv6m4JN8YfUOOQu8Q4Wh6GcxqQ_Pp2BBOFSQWzvpp4rLlJsabcvQs3_bQo_A_aLx6X_U45WGVFZDTwcFNrBwhpA4iGT2BdhJAh-iQ2BGJ6IxUaMqio7ChIUQtGR0YYwqaE9sY9igpaA-dftMiNq6CG9TqWVRE6sum6svTD3WNwOD7GtcYONhCQv47DbtURV5XCs9ibsHBEXplLpIYIB_XSL2Qq7kvYQZG4ZjUBJA7rtZTDAIws6dXjVBb_dikDNgX3F42bfMO2zwpF63RL6EYHQsTWf2Z9pjX-phli4qduGdfYbwjop880v4cXITv96fa8PlBinBnj4jlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=ZpDi6BcNhv6m4JN8YfUOOQu8Q4Wh6GcxqQ_Pp2BBOFSQWzvpp4rLlJsabcvQs3_bQo_A_aLx6X_U45WGVFZDTwcFNrBwhpA4iGT2BdhJAh-iQ2BGJ6IxUaMqio7ChIUQtGR0YYwqaE9sY9igpaA-dftMiNq6CG9TqWVRE6sum6svTD3WNwOD7GtcYONhCQv47DbtURV5XCs9ibsHBEXplLpIYIB_XSL2Qq7kvYQZG4ZjUBJA7rtZTDAIws6dXjVBb_dikDNgX3F42bfMO2zwpF63RL6EYHQsTWf2Z9pjX-phli4qduGdfYbwjop880v4cXITv96fa8PlBinBnj4jlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ویدیوی وایرال شده از تجمعات شبانه:
«تو تاریکی می‌شینیم، ذلت نمی‌پذیریم
بنزین رو کم میگیریم، ذلت نمی‌پذیریم
دلاری گوشت میگیریم، ذلت نمی‌پذیریم
مهریه کم میگیریم، ذلت نمی پذیریم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106212" target="_blank">📅 13:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=UEpOxMc-W9__mcy5xi0EHVoJjhBzxVlyC0GAM0gGRq2TY2pr7fKfHcuxwI3ClcxFxltkG-IBVuXjFL36c0VLS56t_iaRI4NRS2dP_CMVJ28qADi9Fx34BXqcxItKDmRl4NJFmp63vK55XezTVoa_mREHvieDvmv_yX_0jkd5Tg2JlonGji2pguMMUH6saIgloqUBVxsWj3zyDJskBTCI03h5JlYMCmNC48Qk0hu4Or7PWhRUzWyrdL6psU8chEeqPtGWwTgw3qu6dNqGK7AxlUFONt77q31B0YpsHG_xScZLF6coSzSuuk1QbnTXTmB-rEW6WDnLeKK4N1UnZDDr7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=UEpOxMc-W9__mcy5xi0EHVoJjhBzxVlyC0GAM0gGRq2TY2pr7fKfHcuxwI3ClcxFxltkG-IBVuXjFL36c0VLS56t_iaRI4NRS2dP_CMVJ28qADi9Fx34BXqcxItKDmRl4NJFmp63vK55XezTVoa_mREHvieDvmv_yX_0jkd5Tg2JlonGji2pguMMUH6saIgloqUBVxsWj3zyDJskBTCI03h5JlYMCmNC48Qk0hu4Or7PWhRUzWyrdL6psU8chEeqPtGWwTgw3qu6dNqGK7AxlUFONt77q31B0YpsHG_xScZLF6coSzSuuk1QbnTXTmB-rEW6WDnLeKK4N1UnZDDr7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106211" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106210" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vss3qEKxMZ10tHJFlc3a4q0PSEMrZd8iUL2G5tajARj5hpq-0C11xG_8yzd6GawvnSpSjgWJ6bi5WqGoHL-1Qy9R0pHwjNnZjOLldGDbFqfLpu881Z6R9_PgR3ROIDtTuMu_59ah1Jx22wcKYssmMigVPvCZ4fFNHxQbadpFvMI7ClHX4itRLrymfcr2bIeV9v9LroNQ79puCM6QAhc3O9lzrwoV6-JIb3u52FlfOA-n2QHxt9034a_foKQJ0e3uySiUaa-BXziMdzcHzJMxHcgN66sHjbLaLRtRcTd6ov9DZ0xObpQWh0G0nvEX6p58vRyJpJ9pDtlo7G_fCFn-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106209" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106207">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👀
🎙
🇹🇷
اسماعیل کارتال: بمولا از ۵ تا بازی اخیر تنها یکی باختم اونم جلو بشیکتاش بوده. تو پلی‌آف اروپا هم لیون رو بردم و به مرحله گروهی رسیدیم. نمیدونم مردم دیگه از یه سرمربی چی میخوان. دهنم سرویس شده و قصد استعفا دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106207" target="_blank">📅 12:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46400b9012.mp4?token=TwA5iCpMvTb6tYCp7F_0C-FeU0HzN_L1x7ri-18Dgf-eImdy6iTOyaS3lMXanZj3wDf8iTbrCuFBUCY-QziNKWnpVFA8CI1GZMHjDBgeYkB2WTgSI55We53IxTE6DFBCfy5i7pqk1PT6XH3kkHy5l_h6d4EJkTcuA066tuRde7_API8-IgQoOTFLFJAjbydd2OAT8u6rV0Gov1KiGmSEbKjr6z-zkaV9zjAmyoHg0SvKf-SforA02BtPwlKn8XGDkpbyGH1teFOjvs3CWaVji4ybaACzb-UfU5M6tLTrZvx8v5IWWUX4SJZyi4CnCf3Fqir6pMKTv0ITXoGdUIUq3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46400b9012.mp4?token=TwA5iCpMvTb6tYCp7F_0C-FeU0HzN_L1x7ri-18Dgf-eImdy6iTOyaS3lMXanZj3wDf8iTbrCuFBUCY-QziNKWnpVFA8CI1GZMHjDBgeYkB2WTgSI55We53IxTE6DFBCfy5i7pqk1PT6XH3kkHy5l_h6d4EJkTcuA066tuRde7_API8-IgQoOTFLFJAjbydd2OAT8u6rV0Gov1KiGmSEbKjr6z-zkaV9zjAmyoHg0SvKf-SforA02BtPwlKn8XGDkpbyGH1teFOjvs3CWaVji4ybaACzb-UfU5M6tLTrZvx8v5IWWUX4SJZyi4CnCf3Fqir6pMKTv0ITXoGdUIUq3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
محسن افشانی: اون شورت و کرستی که استوری کردم برای خریدن آبروی یک بازیکن فوتبال بود!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106206" target="_blank">📅 12:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=IIhWBVmeaxKyO8J1MejPwNsxiZCVjZEUc-D07Q_40h4WbhuJi5sFeP1JP3T1DgFd4l0RbospVdYOUVYtrjMEDKo0W0oiWSoIqg3BEDwlv57U04mnKjYZMY3pEfYGS51TrmRMwUsIaF5bsg2a9F1wFcLleqXl9G7r13PhaaeUhqFEFWY0vm3URPL619Z1WvEyMc5q1Cv5dNnFWw64_pvc454qhZThICpyGUzfkkTZ8ENHFlfD9rprPr9pB8axujDPOjbc4T8gypiMplLhlMUVLuMRdvBxOkuJMWXuCYv9M9BD4eu0VGZn_PRrSFQNerQG1kna9wpw4xOxZ2AEj8ayrlkJRW3gPEMjJVfJTrrcGP2UI1mO57sVwIMi0XTrVVSrpEkb4VqPhpRZahDwXodx9-u7DuN_9GVCcpndqBZGNA5V8bZYrVNW1LCl9ycUW5mJ-4PJcWlKaztZJDIYv0ekE8ZCRb_YLK9ak4jG0573VpaAmf4sCo7crGsTp2aRFQPhrwTpBOWYjTh9xqk7HvHRImqedquJsITPuTBOgqk_SxIjSjtxot3IFzi5Fh1UHUPWUBjUq2f0IXQRjj-hN5ST3UGbx1F5KXj9RI86K5MJTi9yb8faf0emw_jYtmFWMkbDaNvAVBq5EBm1q_CZgjwBA_dX8kCiX3WcwYbjtEuT3nI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdf4b56cc.mp4?token=IIhWBVmeaxKyO8J1MejPwNsxiZCVjZEUc-D07Q_40h4WbhuJi5sFeP1JP3T1DgFd4l0RbospVdYOUVYtrjMEDKo0W0oiWSoIqg3BEDwlv57U04mnKjYZMY3pEfYGS51TrmRMwUsIaF5bsg2a9F1wFcLleqXl9G7r13PhaaeUhqFEFWY0vm3URPL619Z1WvEyMc5q1Cv5dNnFWw64_pvc454qhZThICpyGUzfkkTZ8ENHFlfD9rprPr9pB8axujDPOjbc4T8gypiMplLhlMUVLuMRdvBxOkuJMWXuCYv9M9BD4eu0VGZn_PRrSFQNerQG1kna9wpw4xOxZ2AEj8ayrlkJRW3gPEMjJVfJTrrcGP2UI1mO57sVwIMi0XTrVVSrpEkb4VqPhpRZahDwXodx9-u7DuN_9GVCcpndqBZGNA5V8bZYrVNW1LCl9ycUW5mJ-4PJcWlKaztZJDIYv0ekE8ZCRb_YLK9ak4jG0573VpaAmf4sCo7crGsTp2aRFQPhrwTpBOWYjTh9xqk7HvHRImqedquJsITPuTBOgqk_SxIjSjtxot3IFzi5Fh1UHUPWUBjUq2f0IXQRjj-hN5ST3UGbx1F5KXj9RI86K5MJTi9yb8faf0emw_jYtmFWMkbDaNvAVBq5EBm1q_CZgjwBA_dX8kCiX3WcwYbjtEuT3nI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
روش‌های نوین تیم‌ساکت‌الهامی برای وقت‌کشی! الحق که رو دستش کارکشته‌باز نیومده
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106205" target="_blank">📅 11:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249d50f161.mp4?token=VFW4Yuxkc9jr0RSW_uum_bpQHalbYOjeyOmVabPfqtrQ1OS1BVYXra_1ML8_OpfQ3VH1eslytV2gCuKkiNx7hLBPYRKefWsqOntJUyADGa5aXE74w_N94Ig2okI8Vh2qzisEqNvDok1vY9FaogtUOzQHDHNTpyLhSNBN6LHL5-9J-ZES_wafvlEdVnSNIIX28-32dCQ7NAWL9YsX4RU9YPz4kVghUTzb-eyDjULlXyCc2XwYDk1J6YuFBWTu0UMx73Lh-KyYfrIeN2GFSNWEu2m6YmOC4jzUq7V_6XBCASrm5WYMzqUj9eEz0syGAfFHHV66XYgx_Ejp7w34igJiww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249d50f161.mp4?token=VFW4Yuxkc9jr0RSW_uum_bpQHalbYOjeyOmVabPfqtrQ1OS1BVYXra_1ML8_OpfQ3VH1eslytV2gCuKkiNx7hLBPYRKefWsqOntJUyADGa5aXE74w_N94Ig2okI8Vh2qzisEqNvDok1vY9FaogtUOzQHDHNTpyLhSNBN6LHL5-9J-ZES_wafvlEdVnSNIIX28-32dCQ7NAWL9YsX4RU9YPz4kVghUTzb-eyDjULlXyCc2XwYDk1J6YuFBWTu0UMx73Lh-KyYfrIeN2GFSNWEu2m6YmOC4jzUq7V_6XBCASrm5WYMzqUj9eEz0syGAfFHHV66XYgx_Ejp7w34igJiww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇪🇺
پس از ۱۰ سال ایران در UCL نماینده نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106204" target="_blank">📅 11:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=UT7qyqnnJLfcpIxl2oG4lOtHy52_05Fr12CjJi66_QmTZQw6pSZE6SBna7ndReAvDVNUUA7wxS3wLrmoLyj2L5AcA2Cfyo8vdavwtJA3H5X54jj2ldUq0_pGjlkBhqshuL9UGtaHkes7-EhmEbs8Sm9oLCnzHkXobBwaDdTaDQ6DG71h4kYkCQOVc7cErn5HA2soMHdut8z918JkzL0pqbiJo92vPJJKNfLMuMm08ZUu5rvaeuWRqWn81rpcYBg-97qxq1h099y4pgEUlE7by5aSJHMEL7hv09rS_hgZGaGcB44rI9yH5XMWQbcjfCII4i-ovWTgIWot4JOnY69qSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7627bb5d.mp4?token=UT7qyqnnJLfcpIxl2oG4lOtHy52_05Fr12CjJi66_QmTZQw6pSZE6SBna7ndReAvDVNUUA7wxS3wLrmoLyj2L5AcA2Cfyo8vdavwtJA3H5X54jj2ldUq0_pGjlkBhqshuL9UGtaHkes7-EhmEbs8Sm9oLCnzHkXobBwaDdTaDQ6DG71h4kYkCQOVc7cErn5HA2soMHdut8z918JkzL0pqbiJo92vPJJKNfLMuMm08ZUu5rvaeuWRqWn81rpcYBg-97qxq1h099y4pgEUlE7by5aSJHMEL7hv09rS_hgZGaGcB44rI9yH5XMWQbcjfCII4i-ovWTgIWot4JOnY69qSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
⚠️
ادموند اختر :لويى ويتون هزار دلارى رامين رو با دو تومن تو منيريه مى تونى بخرى
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106203" target="_blank">📅 11:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=ScI6sr2-dIE-QE_sCRahq2yWPzK6RKemT-u3Nzle9NpG6UF6ObNRHokkhgw9FQmSg7L0gLn-YoD7aOIUMrqLZM11imzk78SDkle9RUrKFGegByFtDdzScitPYyNBhr_CzjGOAMKzef8QPHH8N6veZlP9sMQYscyEXxFbWV0b3prIYh3LnJ639uda7dHmSjAnqHoUDn2Y7anEUh58b7-6CSHrjFeMkKQ873_x-HDHTR6Ut461ihwZ8eynnqMyhAdQvf06puRK4dBa18h0rWeS9NMKJ5_Wjy6_H9_ZHo1AXstbha9IraY9WdgimogXw2o7yukr6-QYPpHBDlY7xqZQIU7r2WqbzVsKFX9Qj3VyhbTHfZGxBydW1y3C7dD6BUT5woNBwn4r1hVrQqYGsjQnCq9S9G9FkCkK2DujENjJ_EU1ugRpPg_X0XMBdV9qiSTfbJseEQeJU4ociU7smmpvHyZ7K-w0mENNoOOeRW2ocjXsAQ8jzIcvLAu2SVJ3PNxIcd56F4pFT9S8XLFDidRjfrASl29WUNVuTZxJ3mq0NJaTD4ShWaUNWoa76hW18gFhNdVserYaEcDcIZpTZX5g0JRwK0kEZLfUs7w5g1pMkrVYCDXymRH-MEGUma8mYy_bdK_v5o487iGXvDVsU1wi5IADgQXDhfs_Kwg_PX__c7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629b78a14c.mp4?token=ScI6sr2-dIE-QE_sCRahq2yWPzK6RKemT-u3Nzle9NpG6UF6ObNRHokkhgw9FQmSg7L0gLn-YoD7aOIUMrqLZM11imzk78SDkle9RUrKFGegByFtDdzScitPYyNBhr_CzjGOAMKzef8QPHH8N6veZlP9sMQYscyEXxFbWV0b3prIYh3LnJ639uda7dHmSjAnqHoUDn2Y7anEUh58b7-6CSHrjFeMkKQ873_x-HDHTR6Ut461ihwZ8eynnqMyhAdQvf06puRK4dBa18h0rWeS9NMKJ5_Wjy6_H9_ZHo1AXstbha9IraY9WdgimogXw2o7yukr6-QYPpHBDlY7xqZQIU7r2WqbzVsKFX9Qj3VyhbTHfZGxBydW1y3C7dD6BUT5woNBwn4r1hVrQqYGsjQnCq9S9G9FkCkK2DujENjJ_EU1ugRpPg_X0XMBdV9qiSTfbJseEQeJU4ociU7smmpvHyZ7K-w0mENNoOOeRW2ocjXsAQ8jzIcvLAu2SVJ3PNxIcd56F4pFT9S8XLFDidRjfrASl29WUNVuTZxJ3mq0NJaTD4ShWaUNWoa76hW18gFhNdVserYaEcDcIZpTZX5g0JRwK0kEZLfUs7w5g1pMkrVYCDXymRH-MEGUma8mYy_bdK_v5o487iGXvDVsU1wi5IADgQXDhfs_Kwg_PX__c7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
💥
یک‌دقیقه خاطره‌بازی با اسطوره آرین‌روبن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106202" target="_blank">📅 10:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106201">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=bEDUYVC6rsG3XnAY1pSeWAhSBvtfxJ8N30FoyYQKjEAM3AOLsqU6-L7DlEpf-FS8mFD4jqjDygvagTNjUovqvKLYNB2FAvqvtA7jEcs3xp8sA77C_nbz9ZD507v2lfUxYA19ycwpCCoTVz8b6bi-PIyS4QmaI_UDpbASt3a0PCtcQAS7mpBU2OFr4RG_QcaeycQd-AhDqriyZxAHdDsQZI2clA_lRYHpD_6u_wCDAGOMKhlwbb9M7XP4oK0EejYFyx3Ptb10xcbVQGfOSyLlSWnT5QMY5Xa8LHSaWZ14Dhf_6C6nOkQQbG35oQJ4V2PxzTB9qrb_OEzm2Tn3sEy65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c278d8437.mp4?token=bEDUYVC6rsG3XnAY1pSeWAhSBvtfxJ8N30FoyYQKjEAM3AOLsqU6-L7DlEpf-FS8mFD4jqjDygvagTNjUovqvKLYNB2FAvqvtA7jEcs3xp8sA77C_nbz9ZD507v2lfUxYA19ycwpCCoTVz8b6bi-PIyS4QmaI_UDpbASt3a0PCtcQAS7mpBU2OFr4RG_QcaeycQd-AhDqriyZxAHdDsQZI2clA_lRYHpD_6u_wCDAGOMKhlwbb9M7XP4oK0EejYFyx3Ptb10xcbVQGfOSyLlSWnT5QMY5Xa8LHSaWZ14Dhf_6C6nOkQQbG35oQJ4V2PxzTB9qrb_OEzm2Tn3sEy65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
نیروی دفاعی اسرائیل (IDF) دیشب با انتشار این ویدیو از انهدام کامل تونل‌های متعلق به سپاه و حزب‌الله در منطقه استراتژیک علی‌الطاهر در جنوب لبنان خبر داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106201" target="_blank">📅 10:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106200">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsM2A3b3_Kl1LRXdp06bUqxhWB5W-Ab5Y6llQoVwLkXMjjyytEXgE73SsFBYgPLqYQ2yAgKziFM52Qs57tSANXAULx_vgBFpjKYRd6Ich1mW3GZ8w6kHGGtOQwdxSQy9R1jlJ3_hu9cvNbO09GGe7p-snYACeBn5bO42iVQv1gChFNQqynURVX5WlwzWH0ixweck_ohYaNbmkoY-DHveaTu_5C2jbJO0XDHJehXwXWVPgFUj567qaWTdn8VFJWZyPVm0SWvzyTK9XZspX81GhVWlgJSh42HXjjkiNyjgzN9ZCFkI9QQklMisgOV1_Oab0u6lCJODJsOrMQSIIk5paQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نامزدهای بهترین بازیکن هفته اول UCL
🔸
فران تورس
🔸
رافینیا
🔸
ارمدین دمیروویچ
🔸
مارک بارترا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106200" target="_blank">📅 10:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106199">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=c4giJN8Ikme2l-jTDOuqGer1pJXnDxmf4cd4ctcRvCyXZ6HlBVmrzIW7lZpfZbzDcwWxqrqYkdyvDp0e5Er5CP4J_MdyTsgQgfMhA9RT_Q7pwquDzbTN_2LGdd1C9MGjrtZXe5OW9ln1qPypaNYe08tEWaR0r8DMPMX_1WvrGRqpc4moK6gNtja1NBQP5zpVR5-RQMU_D_3bdBv2YvtrsiUuyDZ-qFCftu_jhnlmglBZCPJEFTc8hcJmBGNZSwqZ96Af58HtwBqnoFvtPaQFrpdyJ6_nKypC3M73fUaQwNPQpPTm8ZNHmAphu3LYpyhsS2Zl6Lb7ZzzO8drGs779uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c20f0a6e3.mp4?token=c4giJN8Ikme2l-jTDOuqGer1pJXnDxmf4cd4ctcRvCyXZ6HlBVmrzIW7lZpfZbzDcwWxqrqYkdyvDp0e5Er5CP4J_MdyTsgQgfMhA9RT_Q7pwquDzbTN_2LGdd1C9MGjrtZXe5OW9ln1qPypaNYe08tEWaR0r8DMPMX_1WvrGRqpc4moK6gNtja1NBQP5zpVR5-RQMU_D_3bdBv2YvtrsiUuyDZ-qFCftu_jhnlmglBZCPJEFTc8hcJmBGNZSwqZ96Af58HtwBqnoFvtPaQFrpdyJ6_nKypC3M73fUaQwNPQpPTm8ZNHmAphu3LYpyhsS2Zl6Lb7ZzzO8drGs779uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو وایرال شده و دلهره آور از جنگ اوکراین ؛ سربازی که شانس میاره و از زیر تانک سالم بیرون میاد ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106199" target="_blank">📅 09:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106198">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=OUUmelOj-8GlY8PLkItun6Hw2pDVQFlsI1ex06H65TbvsB1WLcNFiU35PG1yXvMfaxl8gY1pEfKz8kK2Z--pWGhd0lBBLE7f0hFSAMHibrViF0lfItpDtFlaAg1Z1chWQ65J2f9DAYSOOFIAq7AbIthb8rtGLZE-cDGza8TGgT-H9-Gt35G5vKyMlv7OAj0iuNgr6LWmpWQjIGDsvqq7lgVtVn7eWesU0_mKTYJ0_xn7V8x8aEf4ANQbGawvrkuZxfB0jE7c6shcqXbo207vwuULIIE_1RTLl7B_L8Hi8CdZ4SOgYajIfApkV_jc1w8wlLCMdHlYJDoAnTAlJeLIAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5454d366.mp4?token=OUUmelOj-8GlY8PLkItun6Hw2pDVQFlsI1ex06H65TbvsB1WLcNFiU35PG1yXvMfaxl8gY1pEfKz8kK2Z--pWGhd0lBBLE7f0hFSAMHibrViF0lfItpDtFlaAg1Z1chWQ65J2f9DAYSOOFIAq7AbIthb8rtGLZE-cDGza8TGgT-H9-Gt35G5vKyMlv7OAj0iuNgr6LWmpWQjIGDsvqq7lgVtVn7eWesU0_mKTYJ0_xn7V8x8aEf4ANQbGawvrkuZxfB0jE7c6shcqXbo207vwuULIIE_1RTLl7B_L8Hi8CdZ4SOgYajIfApkV_jc1w8wlLCMdHlYJDoAnTAlJeLIAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
🇪🇸
تعریف و‌ تمجید جالب تیری‌آنری از رودری خرید جدید بارسلونا و تشبیه‌ش به سرخیو بوسکتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106198" target="_blank">📅 09:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106197">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=Lt58hE4X7llrMQcc5KMuV1l7edomcgAZFEr_K8RIisvv__SIJszSoRgUQ7YtUpHhbpnwg1An_2wRlLxWRDdQI9CXPChQPuGLsC2bwiN9c5sSk3Qyput4PKQGo2KLLoAw9nWVBqWsWHvgIX9gjAdhNdvOPYnCEZ4pTT5oHddBmLM7JkypcZZq7DXkYcL_xaqwtYEDUD_JjK6imgaxj6wDpkFM1m86WokH2yM1ReZj9i_A1y8MJn4vx5wev1tZtzhdI3lBTf70ynha-V3XCrSll9YGO7KnW9HUkaa5tUDGufcfpdacudJAv_e8ZphqgCAZg7kJh_qZnlyDc6I-X7isfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8721a346.mp4?token=Lt58hE4X7llrMQcc5KMuV1l7edomcgAZFEr_K8RIisvv__SIJszSoRgUQ7YtUpHhbpnwg1An_2wRlLxWRDdQI9CXPChQPuGLsC2bwiN9c5sSk3Qyput4PKQGo2KLLoAw9nWVBqWsWHvgIX9gjAdhNdvOPYnCEZ4pTT5oHddBmLM7JkypcZZq7DXkYcL_xaqwtYEDUD_JjK6imgaxj6wDpkFM1m86WokH2yM1ReZj9i_A1y8MJn4vx5wev1tZtzhdI3lBTf70ynha-V3XCrSll9YGO7KnW9HUkaa5tUDGufcfpdacudJAv_e8ZphqgCAZg7kJh_qZnlyDc6I-X7isfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
اینبار کنایه تاجرنیا به پیمان حدادی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106197" target="_blank">📅 09:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106196">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8kU9m3BGgO1-tFQJ5KxB_A1MQ5-ZQ8HXiE6c3pRiUKldFe6mlZbYyTWdyjOyA9i2CNX7AdOUB5aBi4WDZq0u3e9qLQKvSk_5gkHBJNayj35HMFhweMYpKqusb7hPo7He23PgJpuz3LRuJDVKKU_WciX7zZlOROeJg7yW9dpXMYBZBV6qU4H1wg_a3viKDl97KKno9mWZpBtvNRqcRJXKwIYwRG3iGCZgi1ph561wSGBPc86jeJmtHu37twAIf6ACgN03YhvVeaGKUpLV14TmUgd4k7c8kXqPA4cr1kVoets6D_OFhDkzn5rBEdqFcSNLTWeAahPBDngT4Od1foisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔻
🇪🇺
کمترین تعداد بازی برای به ثمر رساندن 55 گل در لیگ قهرمانان اروپا:
◎
🥇
🥶
ارلینگ هالند — 49 بازی
⚽️
◎
🥈
رود فن نیستلروی — 70 بازی
⚽️
◉
🥉
هری کین — 71 بازی
⚽️
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106196" target="_blank">📅 08:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106192">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fcya1R4DbStm6DXtHQSSAhRvjXMrloKIhrPx1OmofoFds9dM0f0aXfpDN3XvHiDhzEI0gCjI6Ui9319hxJkE_Cb4I2y5Ay5Aw56HN7BZU5c8V97q56u5z8Ig4TCuj1-k7VczIDjbxDLcMIAADXh_T3p3pDCtwouDFqiVxnfNQGzIo2Q_wnkOPOXk1xnNXCWCG3sFoOR3hHGuE0VBQfP7rVkzVyYGOc2eqBhdngbQS0EC1cvyvwYpovosajV5cJo2zbJ2zgG6qIw-a2x0Lsunu0BevyESYutDsdX8ift2PZK7bH-8mK0sjq9INhprvoxRI-u9yafrzvkGELzPFaKORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
مقایسه آمار السد قطر و بارسلونا در لیگ:
🇪🇸
بارسلونا ۴ برد و ۱۷ گل‌زده و ۱۲ امتیاز
🇶🇦
السد ۴ برد و ۱۹ گل‌زده و ۱۲ امتیاز
❌
پ‌ن: دوشنبه هفته‌آینده ساعت ۲۱:۴۵ قراره استقلال ایران از السد قطر میزبانی کنه. ایشالا خیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106192" target="_blank">📅 01:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106191">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHd3W8nv_Iwq2cjftAr7RmBokgdA0wcz9a6NuhdRssUx4SJJczIVXrNh1PG34tqvudzfAhkV6Af4_AI1ji2AVcbsaxEvAqTYvFUBYuH-MVRzO1vQtUC1g4JkTz2kqXQq1lSG1QMchWH67NkzMh2_fuiLmmvZT8Z5Aiw31VFZSu9_AAci7UwZPqKW5bJvVUc-iVqQLkBiq-ZgvdseYk6wC0IC_76tNMeSGnpvwhH_KCJNgrYPrEe80QhxSJi0suxCTH0FZb_vfLsRmoR0S6-kWFpBVMCDrVtzjitlNFiSMLwLutHhYjalgNL3koEd8grTWKYWg6-ro3Z0GWbyf12L1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106191" target="_blank">📅 00:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYnNCxDVoNgU28yp9-jEJ2Dp6IYqgdr0NhSTo40D2yHhVSjRh4BtqS25QwNRGQjJWbkh-4e87gC9GtRkTjYOi1fgHGJUkukC_Iwy0J_BwBSkzd-fB35AVSfXFqHqyo8o4tH5xPN0_Jsy1s8m9bTel-HjIVClVTvSwk79VL4IVnlSYSJfgB0yFOl6smNLiNAZmExa6iHHDCM6CZLTPcE6Ab7gtBQqlJgZWkTJZvqgT84hQnyDNe4Yhz62-H7ZQTzLDIZ1MP9Q9WnI6GBkAAacGt15VfbJoqwURqNs3hyJ4G7S_YophG3JwOT3_1ADPSAXo84H-gl7tw0J5vmb5-Obfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106190" target="_blank">📅 00:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106189">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇿
هایلایت بازی منچستر یونایتد 4-0 صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106189" target="_blank">📅 00:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106188">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSomEmoVWc5Rz7vy7YtVVVsGOARJTTE_Ri3HQC8yUbiH1qGVpj-_XnPmeRNZG3xyDCivsH4N_OG2Xzm9DRqI09ecduXlE1cKkVVE-7kqdKOH5KdjzWu-W6L2C_bopVYtwJmCFrkq79abQD9vAQ4G0Kuf86VtBSX5YZMc2ZLxVINPUqVk8HFi-Ye4I1BF_KjcBN6IXa7scWbWNwogulDmym_nyiW7FELR1Ufc10sW4nWSmLpCzaP68jdETiUc4nf0Wtcpm4n0mMzgE8r0bhuaXLk__nJ4tDert3mWNfm3e8hYr3c5SKuhOcFynkltRlLpbPo6iQ3EMfN2hEQ5PEb9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106188" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106187">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3993269f13.mp4?token=WzfDxKSUyBJcVfUjGTG96H4BTY0BqnR_NF0pYCitKy4jbIJ2oP9IruYyNlXFXJ3EAa7Ark0pc3EcP5P1tP8UKeKm6eSF1SzJVnKnJj0UmL9Z7PeiAOuZ7Ma6wmT5P3TxHtV9-OAstWtQvxrd8paLe6SNSJXOLU5E80WZ6AJIukg4DR20p8cguLtU8xAEEse7-07yTZ-1KmaNG0s-FR0LRwwx2mlZoYBUbZlWzKoXrjSLXpRh3NPvtKmQGkavo11PjzGjDgxT60I0zsRxUSFZXxWtT9geBnlcmT_t9hF5XiRP3GEft8TvUvw_gajSaatzHX0Ou0s-SGwsxMHDyFfcx7Ehvs1Dz_mrH5Pio3k6im4Gboceo4Cbkqi2GBd4a4pmSjxX4lcLyntP_lp9P8A-6j3EMvsUDIWmrlMHr3euY8JW7bJwa1CNnTBrV6v7JMYIcrh98v1QXUH1umczch-3ruPErLWcCu5-S6DonC7xgkSt3uplGXr1zluVytLYfj4ih-3mHigtG8smeCMy-BG89axw4B4HCpAhSbJ_D789nLZXVW2yaCTvOH83wPIrrCDN2Rg6cmlfesvluN8KZYT4-B1TjX1uzZ8aB3-C16MHd5cpdZ8U2_rmy5m-QyDhH6AOc8eByF5SODQRshLpx_tfOxWUTc1YxL6Mp0v7udofyO8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3993269f13.mp4?token=WzfDxKSUyBJcVfUjGTG96H4BTY0BqnR_NF0pYCitKy4jbIJ2oP9IruYyNlXFXJ3EAa7Ark0pc3EcP5P1tP8UKeKm6eSF1SzJVnKnJj0UmL9Z7PeiAOuZ7Ma6wmT5P3TxHtV9-OAstWtQvxrd8paLe6SNSJXOLU5E80WZ6AJIukg4DR20p8cguLtU8xAEEse7-07yTZ-1KmaNG0s-FR0LRwwx2mlZoYBUbZlWzKoXrjSLXpRh3NPvtKmQGkavo11PjzGjDgxT60I0zsRxUSFZXxWtT9geBnlcmT_t9hF5XiRP3GEft8TvUvw_gajSaatzHX0Ou0s-SGwsxMHDyFfcx7Ehvs1Dz_mrH5Pio3k6im4Gboceo4Cbkqi2GBd4a4pmSjxX4lcLyntP_lp9P8A-6j3EMvsUDIWmrlMHr3euY8JW7bJwa1CNnTBrV6v7JMYIcrh98v1QXUH1umczch-3ruPErLWcCu5-S6DonC7xgkSt3uplGXr1zluVytLYfj4ih-3mHigtG8smeCMy-BG89axw4B4HCpAhSbJ_D789nLZXVW2yaCTvOH83wPIrrCDN2Rg6cmlfesvluN8KZYT4-B1TjX1uzZ8aB3-C16MHd5cpdZ8U2_rmy5m-QyDhH6AOc8eByF5SODQRshLpx_tfOxWUTc1YxL6Mp0v7udofyO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🔥
🔥
🔥
سوپرگل چهارم بایرن‌مونیخ توسط اولیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106187" target="_blank">📅 00:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106186">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=GXv504CUYzWpqGXkAIfeDZOSDVvurjZGKGU3sdpSgw1gyui7dp3ojoZ5QBESSjsU0blXLssEGNbmE-9hVGBvfVDTu5XyxDWefVwlwFmT85QS2TFgAkuS5_3BxCXoOpS0z9z7UUfLIuwQvXrwnPHPl8fHJz4tz2Eh_vQ_tJxORbbq5OLarTfuIe2rifqF-xQZvm_8mOUq9p_xpBKonHSqZHfIAHiZcLbAHETxlq4DbSsvNE7_R4ioxf4_U_qZkmBBHthj2xeBex9axMYqj6sKPFUNVp1HzE1EGjHcj8Pl7DTiMyzNlGV0-pFeEroJaHFiA2R_AuCk3RgkCQv072rb6qH2TIQmM01HS98dQ_t0QrXOUHbvOZo0PM-AOU0MzAF4WBeeiRJe0ir7Ix_QW3bHI0KujvoE2PTTeGgPPWvr_Pz54wR60mrIOtNEiDyJWe8IAcrFO29PL-MXGIFAxly40Hkv339zXu3Yzv1R_vXWXS6Cks6x6Vd274Q0Nv4fQE0lwoZMGh69uhndrnx--vseUuBou5rUfXzxCqpO7-0YRPv_8tgiO-0aPyoGCFzqvmhC-0VIvH2SIycJ-gdgZ3GD3x4svqvEpXyVANaS9SSz_VoW5dvUdHGw57VNAHyEDZQAiHG5AgAlnmrysMRnJ5mevsIb2CFiGseInzcS-2dx0v4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a3837ef974.mp4?token=GXv504CUYzWpqGXkAIfeDZOSDVvurjZGKGU3sdpSgw1gyui7dp3ojoZ5QBESSjsU0blXLssEGNbmE-9hVGBvfVDTu5XyxDWefVwlwFmT85QS2TFgAkuS5_3BxCXoOpS0z9z7UUfLIuwQvXrwnPHPl8fHJz4tz2Eh_vQ_tJxORbbq5OLarTfuIe2rifqF-xQZvm_8mOUq9p_xpBKonHSqZHfIAHiZcLbAHETxlq4DbSsvNE7_R4ioxf4_U_qZkmBBHthj2xeBex9axMYqj6sKPFUNVp1HzE1EGjHcj8Pl7DTiMyzNlGV0-pFeEroJaHFiA2R_AuCk3RgkCQv072rb6qH2TIQmM01HS98dQ_t0QrXOUHbvOZo0PM-AOU0MzAF4WBeeiRJe0ir7Ix_QW3bHI0KujvoE2PTTeGgPPWvr_Pz54wR60mrIOtNEiDyJWe8IAcrFO29PL-MXGIFAxly40Hkv339zXu3Yzv1R_vXWXS6Cks6x6Vd274Q0Nv4fQE0lwoZMGh69uhndrnx--vseUuBou5rUfXzxCqpO7-0YRPv_8tgiO-0aPyoGCFzqvmhC-0VIvH2SIycJ-gdgZ3GD3x4svqvEpXyVANaS9SSz_VoW5dvUdHGw57VNAHyEDZQAiHG5AgAlnmrysMRnJ5mevsIb2CFiGseInzcS-2dx0v4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌سوم بایرن‌مونیخ توسط آلفونسو دیویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106186" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106185">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29ed472619.mp4?token=vg_G4cwXduijRwqdElIl_es9zN1ozp8iSiLOZlStQ9WB-BWzjGNJ_28j9BevJP7GMRbPS_uEb85ad9q9Oza73GAK09gB-FGy4SoeXJ5zqDC-j_IvDKG1DLKOP2O5PuPsZeL0Z_muW305jpT6epuGrq0aLy-0RhY7H0A-qscwr4drwXwR51rxKge3QU8jSuxJd-nxIpHV4FsCqamSp9oScgx6lu0SWV7wcEUkDOj4zNt8vLCVkrd5_5gR7WlfVLWytKggtfN-ncaNrs64PB9zkITWeuYgD9ZJzl5dIIJfKVWSyINMFOWz5lnCE_5yZTpf2LYqdJCKoW5oZEdkF-twEEBBWTm4V4RM_pHfs-v309CeeajKfwy9q6OW44q2tzXPZ4aBZc_MMqfJMXr0dA6XZSwb9Q_H9eBonbeszqL89ysHwAKc5jcp3axV5Wirtfei-rouviVI2JaAmkMmnATAmm9URobkPJI1g0hSeyAMw5u8hjWQGMVXD6UfTsEZdgOOYaqpzIF0e9bHMHfH-qZL9yghCW5Hgkz76YJ9wlNb7dtswxjejTZIiMkt-iD4fVYTn3zfENdpoZ-hQexZNDLqFH3PZu3_zASk5Ss6rF-S750l8l91kH9I1Epva0qTTK-TpH_MHVb6lhwTCIh7gwbazyrJxX7fDZOVMTNSza4gz-U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29ed472619.mp4?token=vg_G4cwXduijRwqdElIl_es9zN1ozp8iSiLOZlStQ9WB-BWzjGNJ_28j9BevJP7GMRbPS_uEb85ad9q9Oza73GAK09gB-FGy4SoeXJ5zqDC-j_IvDKG1DLKOP2O5PuPsZeL0Z_muW305jpT6epuGrq0aLy-0RhY7H0A-qscwr4drwXwR51rxKge3QU8jSuxJd-nxIpHV4FsCqamSp9oScgx6lu0SWV7wcEUkDOj4zNt8vLCVkrd5_5gR7WlfVLWytKggtfN-ncaNrs64PB9zkITWeuYgD9ZJzl5dIIJfKVWSyINMFOWz5lnCE_5yZTpf2LYqdJCKoW5oZEdkF-twEEBBWTm4V4RM_pHfs-v309CeeajKfwy9q6OW44q2tzXPZ4aBZc_MMqfJMXr0dA6XZSwb9Q_H9eBonbeszqL89ysHwAKc5jcp3axV5Wirtfei-rouviVI2JaAmkMmnATAmm9URobkPJI1g0hSeyAMw5u8hjWQGMVXD6UfTsEZdgOOYaqpzIF0e9bHMHfH-qZL9yghCW5Hgkz76YJ9wlNb7dtswxjejTZIiMkt-iD4fVYTn3zfENdpoZ-hQexZNDLqFH3PZu3_zASk5Ss6rF-S750l8l91kH9I1Epva0qTTK-TpH_MHVb6lhwTCIh7gwbazyrJxX7fDZOVMTNSza4gz-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇩🇪
گل دوم بایرن‌مونیخ توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106185" target="_blank">📅 00:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106184">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=elp1bR0xFMGAs3p6xyJOVGX4hdgI7-QcCTiKghYXjw8ypQ6nNheYBB7T_mqwm9KmKj2xdDEwfPpVKLXpfg34Z7kdg_t98sviH2kjSCUm9RWn--VsLp_1VytFPSSECR8nEBfjUHA_TYlvJi-u3rC5NihZ76ny0EgmTwcNNu2AFw2CLQLnuEmrXf8ah10f022SxskmivzULRP2X_MqtJfsZII6cy-63ZDY7lQH6i95MUkchx1N_BpSXwzSEWcqjkxVlzg0d-mOXbCYbZjfqm1YLs6B2Bwzq-dryDtLv5QLm474Cb4uV8ePC_u5bUDMHXvzfhNZyhyjTZxmLVi_Xgv8tl0GiyktpWRMfbAs5qzFUGnMx1PLMt4rZ9Qr7wDbEyP-8i1We6tplsun85Lpjpe_-QiBWHfx0DotTY_h-cljcllzYAYOtXsvWpMK07FfvrVI1kLUgDE-xwQtZrqNwlvskunWEbjerSYVxxZ6OdyXB5U4FBbkH_hPziwlpQwGL8lWcVfboVpf99SavLF_MhFm0JjPBQVoFAofeFCezABAcIFag3NlQyMG3hfD3zeZcx2bT1QRbVOGUOoISBp-xwYe3xzPqKGqQ0-0QRww0vwh8e7p-rXSUpVBSMt0KLR-ju14s_7CSxuGdHF-OJ5b-yqQV6ypqSJ1oeNEcBJu7fOwAEc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/469ae1834b.mp4?token=elp1bR0xFMGAs3p6xyJOVGX4hdgI7-QcCTiKghYXjw8ypQ6nNheYBB7T_mqwm9KmKj2xdDEwfPpVKLXpfg34Z7kdg_t98sviH2kjSCUm9RWn--VsLp_1VytFPSSECR8nEBfjUHA_TYlvJi-u3rC5NihZ76ny0EgmTwcNNu2AFw2CLQLnuEmrXf8ah10f022SxskmivzULRP2X_MqtJfsZII6cy-63ZDY7lQH6i95MUkchx1N_BpSXwzSEWcqjkxVlzg0d-mOXbCYbZjfqm1YLs6B2Bwzq-dryDtLv5QLm474Cb4uV8ePC_u5bUDMHXvzfhNZyhyjTZxmLVi_Xgv8tl0GiyktpWRMfbAs5qzFUGnMx1PLMt4rZ9Qr7wDbEyP-8i1We6tplsun85Lpjpe_-QiBWHfx0DotTY_h-cljcllzYAYOtXsvWpMK07FfvrVI1kLUgDE-xwQtZrqNwlvskunWEbjerSYVxxZ6OdyXB5U4FBbkH_hPziwlpQwGL8lWcVfboVpf99SavLF_MhFm0JjPBQVoFAofeFCezABAcIFag3NlQyMG3hfD3zeZcx2bT1QRbVOGUOoISBp-xwYe3xzPqKGqQ0-0QRww0vwh8e7p-rXSUpVBSMt0KLR-ju14s_7CSxuGdHF-OJ5b-yqQV6ypqSJ1oeNEcBJu7fOwAEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌چهارم منچستریونایتد توسط لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106184" target="_blank">📅 00:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106183">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=BgrLCQE4BajnIVvWkomCCGOLCk6PaTpkkpOn9-Yxp0GFmSuSdaoZoQ5N9nDDMVr0zcRwFBddVE9fRvOInH-mMCd7V4dVW_R_wAFZvas_QmucUzZ7rESPKC7uQolx-8_Y4anQFbycOpVhHnmnPWcdbOT7kwZYMn9NfCupenfVBYi0oBgWVkhxuAtL7h0BcM6YdHsO4TAaILUwe-z2pXKib3SUjkHuOqEM2ao7GtZN6CkxX8bB2L4Iwgf83-SxCRSQF_O09nUxKhSapKbCzDtMOolg2u6rMurIhj_22J-SejmDxuF8GvZLPZsCgvDnzLtvrEYi1ZWTCktTixxA_tKLWhFVOtraclKeYr6a7amHzklyNvhe2BWWNMxp4OOlWOTaPADKbQBDvAJjxIdynHKg7M2QViudZkhGhE4kzoEBOgFroUzCkvFOyxdEUFy4L-BsTZGC3IppQn34VXY4ZUgSaNqrLQEpzjNEG0GZJzbhX-5sftGjFoxBbhSuEbPQaMq7--muJAL3v8EN7njAwQcJ2_u5x6b9E6TraiEafy7Mi4QgASMUHp7TjEl0qNJwkyxv4_I8oKsbIKBTDmszbknE3Depi8VT2Uc2-Sd1Dbm4vvUu0h5LgQz5vw-abRWi39NstHZcpMhA67-G4ZoKS_r-pNKHzz4oosr8QBC1264CepE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a73af6ae7.mp4?token=BgrLCQE4BajnIVvWkomCCGOLCk6PaTpkkpOn9-Yxp0GFmSuSdaoZoQ5N9nDDMVr0zcRwFBddVE9fRvOInH-mMCd7V4dVW_R_wAFZvas_QmucUzZ7rESPKC7uQolx-8_Y4anQFbycOpVhHnmnPWcdbOT7kwZYMn9NfCupenfVBYi0oBgWVkhxuAtL7h0BcM6YdHsO4TAaILUwe-z2pXKib3SUjkHuOqEM2ao7GtZN6CkxX8bB2L4Iwgf83-SxCRSQF_O09nUxKhSapKbCzDtMOolg2u6rMurIhj_22J-SejmDxuF8GvZLPZsCgvDnzLtvrEYi1ZWTCktTixxA_tKLWhFVOtraclKeYr6a7amHzklyNvhe2BWWNMxp4OOlWOTaPADKbQBDvAJjxIdynHKg7M2QViudZkhGhE4kzoEBOgFroUzCkvFOyxdEUFy4L-BsTZGC3IppQn34VXY4ZUgSaNqrLQEpzjNEG0GZJzbhX-5sftGjFoxBbhSuEbPQaMq7--muJAL3v8EN7njAwQcJ2_u5x6b9E6TraiEafy7Mi4QgASMUHp7TjEl0qNJwkyxv4_I8oKsbIKBTDmszbknE3Depi8VT2Uc2-Sd1Dbm4vvUu0h5LgQz5vw-abRWi39NstHZcpMhA67-G4ZoKS_r-pNKHzz4oosr8QBC1264CepE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل‌اول بایرن‌مونیخ به بودوگلیمت توسط موسیالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106183" target="_blank">📅 23:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106182">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hugUcjo9jutQ-gS96QotdcjZqI3qeLb_Saozw69JPH1_JEC1_x1i3KA1znil4g5xCpXC-CQUeFcqUnDHn8sl3WG0TJnyfmdcAlBVqF244QkojYx8FfJKTiVtUD__Jp5bZbyjO7EzZubO58auC7Y051LlEsikQwhqpzoRGa7-aESW2JoE13glSXZDE5xl2OWoVbCKCy51GRdtzF8HA9myF2PtasQiN31E62Hdz2UJzPx0Nkzmd67ICGbHrYxxNJfDgg0i15C5IZLkUSuJsahAiWEjuFVSZlPJ-1EuElh97Wk5tKx77EznUuKRTyk13Rk00fyJb1gFXp1tCiq9lDImoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔥
🗞
رومانو: فیلیپه کوتینیو با قراردادی آزاد به سانتوس پیوست و هم‌بازی نیمار شد، هیر وی گو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106182" target="_blank">📅 23:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106181">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106181" target="_blank">📅 23:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106180">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cj4gakZEMKp8vF1dy9rvsONkXdOZ3PjGBEbF5pyhE7qzum3iEOuin7BD5oVMOArTuz5l6N1VvYJTex5TVtXuNAmMjn0afZx5LDiSBeaiyr_sNm2QxaTsrtDoij0EZvXwCqTIvILfR4FG0r6WPRAWpwx-kA14-yh8wP20LQSbPeFuziVxg7ODVe8RnTT_mC-vTlfNIJ6lO-xvfdUK-XamL6K7fXaZfrav-gkf8xztNpsIclQONtNBUwCRIDWUrXmyR6vHl_0OLGqkp_yWrWgZ-5MHLhfVzCCa6BFNs6m0J7HmdTM1Qz9G1BvlKwkSLX63nORqP9aF-ntmMc00CjqCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇹🇷
اسماعیل‌کارتال پس از تساوی جلو رم در لیگ‌قهرمانان اروپا از هدایت فنرباغچه استعفا داد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106180" target="_blank">📅 23:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106179">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=Zx3DX4d-GsI1jCA8gmvpCxPTPCL7f7IsTzk3U2bN-kgXnAjie4os6xiVudzQXAWvwMRomDb-_CJZIuWGChZ6-Tp6uLkL4iCph4ZPy10MJfHR8sIZB6p_oDpwNo7HrNjALkDrQGg3OmYWwINg9hYR0SC1ozteacsNwq1HK5P94X08wwez1Y72oI8xzlK-mb9JxFsBnVn8o8COzYsOc1WUL1F_Jh2izvgua0JbBDCOHb7oKYzLFyfAAVM_sD-1xxGicc4_W_1Gcbxr7JDvolCv6L0LbgcdKNbmyzvNakk-vyUb1afED_FaeWicPRpCJPbJTq-yRVTGVMVSZezMwSRsIDEUvH3gTJ67lPk_GlM9TWeiqKPVBpAZL8r3vz7L-MDzFCmXDFBVShSPd8_y-smkMq8Xx1W6XV8dBqDbLwGnRqf6qaY4Lc9uGUquf-3DFyAI4Yqyyrk4_fgqCnzbjZuW_70_XTazTlTpJOadQeAArVp9TkBJaq0kDGoNkh1q-Z6nnEaNlnPWfh7ZgPNBk1VK_iZZxsgPf5TLqJjyh584YW36mH3audEtzBVXJRN1dmU1tIGPsF9w49LSpIDKn8Oa8hU7ExnvMcpaZE8g-dS_Z1ZFB43NAfkdzaP5y8PDLgmGzQzPHaNYtA_xd_0QiK2jucRDwgh3c2vSdCNnT0eJPug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2197035aa.mp4?token=Zx3DX4d-GsI1jCA8gmvpCxPTPCL7f7IsTzk3U2bN-kgXnAjie4os6xiVudzQXAWvwMRomDb-_CJZIuWGChZ6-Tp6uLkL4iCph4ZPy10MJfHR8sIZB6p_oDpwNo7HrNjALkDrQGg3OmYWwINg9hYR0SC1ozteacsNwq1HK5P94X08wwez1Y72oI8xzlK-mb9JxFsBnVn8o8COzYsOc1WUL1F_Jh2izvgua0JbBDCOHb7oKYzLFyfAAVM_sD-1xxGicc4_W_1Gcbxr7JDvolCv6L0LbgcdKNbmyzvNakk-vyUb1afED_FaeWicPRpCJPbJTq-yRVTGVMVSZezMwSRsIDEUvH3gTJ67lPk_GlM9TWeiqKPVBpAZL8r3vz7L-MDzFCmXDFBVShSPd8_y-smkMq8Xx1W6XV8dBqDbLwGnRqf6qaY4Lc9uGUquf-3DFyAI4Yqyyrk4_fgqCnzbjZuW_70_XTazTlTpJOadQeAArVp9TkBJaq0kDGoNkh1q-Z6nnEaNlnPWfh7ZgPNBk1VK_iZZxsgPf5TLqJjyh584YW36mH3audEtzBVXJRN1dmU1tIGPsF9w49LSpIDKn8Oa8hU7ExnvMcpaZE8g-dS_Z1ZFB43NAfkdzaP5y8PDLgmGzQzPHaNYtA_xd_0QiK2jucRDwgh3c2vSdCNnT0eJPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇺
گل‌سوم منچستریونایتد توسط ششکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106179" target="_blank">📅 23:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106178">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=dvOgw4JjXzzmS1E3cYjC2ZV_2HG5qSKRPubf8oA17CBbh5aKsMFC588jlC3b13Abo7HmMIZLqe5ap9JXz-PdmYqdFnH5nv8ls1Z4AmTH0NSHHJeF2kbeo5BjEvvb4imn8hV0vF_Egmj_lyFRHyYsQtnBq3KE19SaFC8mOLnWbP9Y4yU0Mvl9fKuySf0aECrcMYsVjZey3tl7-qAzctXsMaisJi1J7lTGke8EO4Ji10klaVnOyZ9kPuADRgCQk2AbN8JkIUcRYW1b6ya4lq3YYawk4yzUYXxrVgQrEK332wWXNVxtZLron5ulHw6rxvzPXIRVZkAaK8fM2KbnJLjTBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7c2e2ba0e.mp4?token=dvOgw4JjXzzmS1E3cYjC2ZV_2HG5qSKRPubf8oA17CBbh5aKsMFC588jlC3b13Abo7HmMIZLqe5ap9JXz-PdmYqdFnH5nv8ls1Z4AmTH0NSHHJeF2kbeo5BjEvvb4imn8hV0vF_Egmj_lyFRHyYsQtnBq3KE19SaFC8mOLnWbP9Y4yU0Mvl9fKuySf0aECrcMYsVjZey3tl7-qAzctXsMaisJi1J7lTGke8EO4Ji10klaVnOyZ9kPuADRgCQk2AbN8JkIUcRYW1b6ya4lq3YYawk4yzUYXxrVgQrEK332wWXNVxtZLron5ulHw6rxvzPXIRVZkAaK8fM2KbnJLjTBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم منچستریونایتد توسط برونو فرناندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106178" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106177">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=tnKQ05XzXb6nSkf4i5uaFLqBLBCqAcZx8YXdoxx0bdfjP6Y0k6EOG58NBghQsdwQNTmUhQ5pj4qx8VG2M55qO8JtMAoW0J4lWfJiW9ZuQW4JQM8fW5tAGn7UdRBEyYGrtv1gATTUo7QkchG-9BMSMcEyttxIFzvQ0rjbyBCIVwmN_t65hKy_QsfkgVUxfLZUoD6F2zw3XvHfeIixKs0cd0oTIYZb4A3h7CzqPb1vJ_Cfrmlo7q8Cz0vA6GZ-U-Q-5UROThme152WKbI7guUm59PAMZpvXBzFNPHdFQhrI8A8xyhR7dtv_5hK72oOPkZwIaHM3YRBxuPiMqvpXLMmMKPhS5nsMs7MAQqMQPGIeJ-5eUMs0hsvwwgdv9VhpYHcay_ezXwGNG5yXeBQy0UQ1djMXteweuvoFvCSH2lRnOzWg422QN74OamBITFdOCZ6JXPj6ROKkwwRuyhrsrK2z8-WdR8kBPvEULBiKRyvsSrPlH82qLAYCBDJ_36m231Iu5B6qTAqzEanPT8xQgwFzYml8Cq6cyURh5fjnsYFnyyUBPPcl3QVEZIp-ETWAoz--wLId2IhqtV1V1hnv7tYfQsE0DQGY_iVbBGbczS8xXipOWk_aRLX14WxzEsG5Z44Iq7y87NT7Egt5Hula2FBGdjkcH-W_U0Uw8HPB9a75jU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a2f3527a0.mp4?token=tnKQ05XzXb6nSkf4i5uaFLqBLBCqAcZx8YXdoxx0bdfjP6Y0k6EOG58NBghQsdwQNTmUhQ5pj4qx8VG2M55qO8JtMAoW0J4lWfJiW9ZuQW4JQM8fW5tAGn7UdRBEyYGrtv1gATTUo7QkchG-9BMSMcEyttxIFzvQ0rjbyBCIVwmN_t65hKy_QsfkgVUxfLZUoD6F2zw3XvHfeIixKs0cd0oTIYZb4A3h7CzqPb1vJ_Cfrmlo7q8Cz0vA6GZ-U-Q-5UROThme152WKbI7guUm59PAMZpvXBzFNPHdFQhrI8A8xyhR7dtv_5hK72oOPkZwIaHM3YRBxuPiMqvpXLMmMKPhS5nsMs7MAQqMQPGIeJ-5eUMs0hsvwwgdv9VhpYHcay_ezXwGNG5yXeBQy0UQ1djMXteweuvoFvCSH2lRnOzWg422QN74OamBITFdOCZ6JXPj6ROKkwwRuyhrsrK2z8-WdR8kBPvEULBiKRyvsSrPlH82qLAYCBDJ_36m231Iu5B6qTAqzEanPT8xQgwFzYml8Cq6cyURh5fjnsYFnyyUBPPcl3QVEZIp-ETWAoz--wLId2IhqtV1V1hnv7tYfQsE0DQGY_iVbBGbczS8xXipOWk_aRLX14WxzEsG5Z44Iq7y87NT7Egt5Hula2FBGdjkcH-W_U0Uw8HPB9a75jU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچستریونایتد به صباح توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106177" target="_blank">📅 23:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106176">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=blCUnL7S-iGXnCmGl005KhsrK5JQ4Pr5IRhPaR9SMMlpKNlhpEVNhHLRSj0SbtQSsiAGfAOpJuH5oYLWufO9PWCiTINTdi3Ew-afUsaP6DQ4LKoyiyzUNGXmvTYaK3s0RKSShWKNysXs7T-bjIQ3oC8cbbV5F6YxR1R0c88D9IZifZ0mOSafarmcJ1nxyA_GzzxNKQWttlKwaksaJRPWjK_7s1OQpeLobm37wqDps63ZmbnIlUb3sPZSc2-RSewUPSkPpmmyr2C_S8gF9bpQv3kaqhGdyH-XXQyD5WxTKX034vHqdLGnM8gCE0v3BJRhbS4_eVBLR9gXhp60buLe6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8476aaa93.mp4?token=blCUnL7S-iGXnCmGl005KhsrK5JQ4Pr5IRhPaR9SMMlpKNlhpEVNhHLRSj0SbtQSsiAGfAOpJuH5oYLWufO9PWCiTINTdi3Ew-afUsaP6DQ4LKoyiyzUNGXmvTYaK3s0RKSShWKNysXs7T-bjIQ3oC8cbbV5F6YxR1R0c88D9IZifZ0mOSafarmcJ1nxyA_GzzxNKQWttlKwaksaJRPWjK_7s1OQpeLobm37wqDps63ZmbnIlUb3sPZSc2-RSewUPSkPpmmyr2C_S8gF9bpQv3kaqhGdyH-XXQyD5WxTKX034vHqdLGnM8gCE0v3BJRhbS4_eVBLR9gXhp60buLe6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
بازی استقلال ـ پیکان، داغ ذوبی‌ها در دیدار با پرسپولیس را تازه کرد؛ باشگاه ذوب‌آهن نوشت: دلیل مصونیت تیم پرسپولیس چیست؟
❌
⚠️
باشگاه ذوب آهن: دو صحنه در یک نقطه از محوطه جریمه و در یک ورزشگاه
🟢
یکی امشب، چک شدن صحنه توسط وار و اعلام پنالتی به دلیل بی احتیاطی مدافع. دیگری سه شب پیش، خاموش کردن VAR و چک نشدن صحنه به بهانه پایان بازی و اعلام نشدن پنالتی و دقیقا همان بی احتیاطی مدافع پرسپولیس و ضایع شدن حق ذوب‌آهن برای بار چندم تا هفته ششم لیگ برتر
🟢
⁉️
قضاوت با شما؛ چه کسی پاسخگوی حقوق از دست رفته ذوب‌آهن است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106176" target="_blank">📅 23:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106175">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
‼️
🇮🇷
اظهارات خداداد عزیزی علیه فدراسیون فوتبال: پول ندادند، VAR آفساید را تشخیص نمی‌دهد
🔴
فدراسیون پول شرکتی که VAR را آورده نداده و VAR اصلا آفساید لاینشون کار نمی‌کند و نمی‌توانند سر صحنه های آفساید تشخیص بدهند.
🔴
آقای فدراسیون چرا خط کشی نکردی صحنه رو؟ شما وجود ندارید اگه راست میگید بیایید خط کشی کنید و نشون بدید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106175" target="_blank">📅 22:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106174">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOKAL75v-DD5id3-VQo97E0qOoTc8rHLvzGiBird9CKpBpCWtK7_iJ99U34EWl26pknffH15PZ-l55CRGEoDIvJuMDk1H0zCxDZ-fLxCATqqolDPTt4WZEtCr1PUHXtAAhxWZJkTtcKiYQhrftRWo2GuKapmYxelEQpN2Z15EihVS_ee7XcGCRtlLuuqFo9VQHv2roKYtV32EB07NuWKwsoNLPDkJc74cSdE7ilWtoIuz_8qiEfVzkxbqKaSzJrJXSBjaNhQSEbkR95Omh9VKXe8SABVa7cppoPKEF61oIv7_Dnd_1_pok5vAjmiKgjPxLuXaCkn0neeeJTTKvDdMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
‼️
واکنش خداداد به داوری بازی تراکتور و اس.خوزستان: تبریک به فدراسیون و کمیته داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106174" target="_blank">📅 22:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106173">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
❌
🇮🇷
🇮🇷
بیزاتی مربی استقلال:  دلیل لغو بازی رقبا را نمی‌دانم؛ شاید چون بازیکنان پرسپولیس قرار است بروند تیم ملی، بازی آن‌ها لغو شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106173" target="_blank">📅 22:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106172">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/588203f560.mp4?token=M3SE4q8R6b1SYSGlPZg1hDW0TTXZ3ptlNjO-eGS5rZwEw6ZpdtWqs5S7eacYQrNNrVF6xZsGZPJ-or3W1PQab29eVuXADLH9naOU_zBI9HGpQr7LvalDsPyeIF-AO305SGQ8aQxBY-DVlO9Puvt8zvWpN-rVR7mtMHTCplldJNkDeyLs1SOLnlQTUBr5WbxesDRwMMT6oXlxagJf1mW93oOqTpTcyZFACtQ9FZRccU1xNJb3jLIvisUQzufdO9FvljQkFC_Ot1nOsZDOCBOhQhmVlyKxAouysTBWEY-dbef_d9rEGj-loJ4ZNdghwfsYFynBsOsJNuBwXF6sbBGUHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/588203f560.mp4?token=M3SE4q8R6b1SYSGlPZg1hDW0TTXZ3ptlNjO-eGS5rZwEw6ZpdtWqs5S7eacYQrNNrVF6xZsGZPJ-or3W1PQab29eVuXADLH9naOU_zBI9HGpQr7LvalDsPyeIF-AO305SGQ8aQxBY-DVlO9Puvt8zvWpN-rVR7mtMHTCplldJNkDeyLs1SOLnlQTUBr5WbxesDRwMMT6oXlxagJf1mW93oOqTpTcyZFACtQ9FZRccU1xNJb3jLIvisUQzufdO9FvljQkFC_Ot1nOsZDOCBOhQhmVlyKxAouysTBWEY-dbef_d9rEGj-loJ4ZNdghwfsYFynBsOsJNuBwXF6sbBGUHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
وضعیت یاسر‌آسانی حین خروج از ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106172" target="_blank">📅 21:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106171">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AARk2csjTbS0W5Yfs2XweHb3rvJN0E5YhEU_JGQp8ELmgBZAOZcFPv9mndR_QM1nTX1Bd_4yAeAqCsFDyYkYd8lNMG4vNnwy3wlHmq9SKjFwcMaFzrMe6ygWPuSrkXuijNmiuLZOVoKzSwnhI8SR03sZVYqtis4WxJ4uo3XXBWfONWw4BEWNH3Ifd3C6urmn9AZ65ogjLMYRJvNVjEVeqSySpRAaoTh4MSPIeOy1Z43Ot0LzwBEWMYNccSowH_zaHMBjvaT6_SCVHqah4BviZqmTn0VR-g-5LnniwBQ_Kf5V5tv9-rqfR9QszfESj9WQjjRjYVPdFE0HbHdeBdAa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
❌
🇮🇷
پزشک استقلال در حین خروج از ورزشگاه: یاسر‌آسانی شرایط مطلوبی نداره و حضورش مقابل السد تقریبا منتفی هست هرچند باید تا روز شنبه منتظر بمونیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106171" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106170">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
مصدومیت ستاره استقلال در آستانه بازی با السد؛ آسانی لنگ‌لنگان از زمین خارج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106170" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106169">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1846b0f6.mp4?token=JmyH4xg6HFBAH3ZbAJ2Yy6DawcJVanWs4QRBeM36m142fCXzFIf4E1F_R3YdIht8cIn04ILX33X4XNkUmT-Z6Hrs89yzj2nrBWzHaV-5HfOwKXbu5PVJDXy4WL7WhNoH-v9u12aNQkARY9xi_AZSiBNLryI0yKWoqi-I6On6N6XYmhGVC-DhRIK_JP0G0L65VTnB4Tus0NZXiIhw9bzm1eHmhJm_1bNug396C7JxdDGNfEXnWcopiKs80zvFK2XFYQwhPXWSwuYSz9YUlVDDp6_GaUkSztsQVebBj2XPynQ5sLe40NE5AXnqjq3zbAidc4pHGbYjkqKvN_UZYXdLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1846b0f6.mp4?token=JmyH4xg6HFBAH3ZbAJ2Yy6DawcJVanWs4QRBeM36m142fCXzFIf4E1F_R3YdIht8cIn04ILX33X4XNkUmT-Z6Hrs89yzj2nrBWzHaV-5HfOwKXbu5PVJDXy4WL7WhNoH-v9u12aNQkARY9xi_AZSiBNLryI0yKWoqi-I6On6N6XYmhGVC-DhRIK_JP0G0L65VTnB4Tus0NZXiIhw9bzm1eHmhJm_1bNug396C7JxdDGNfEXnWcopiKs80zvFK2XFYQwhPXWSwuYSz9YUlVDDp6_GaUkSztsQVebBj2XPynQ5sLe40NE5AXnqjq3zbAidc4pHGbYjkqKvN_UZYXdLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
⭕️
🇮🇷
سعید سحرخیزان نیز لنگ لنگان استادیوم شهدای شهر قدس را ترک کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106169" target="_blank">📅 21:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106168">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020d7e0eea.mp4?token=eYDpJLHcsbic5c-I8BFaE6zNLXUrCp8aq3jGSDWI0Zvy1ghOHyTrXwzqfee6XYgOxvKEDMecV-tgSwkjCOnI4uhqaqaw82SSNO73Oy7CDrPgTmoLzA4RyZAfpdTlyR94z129AjTdb8WgYsFVRjKTOOQ-QWg7Gjo1EzME2Bqo9a4fm92_SvzD5lowcLmnzrRcorVpNsELNwetfq2SzkG48Vkr-TSyMGyNfhJqjl2PlC3jJKcxqgdsV0jRLGYoBlxkpo6x6V4SeHnd_fBXC8s8U_upM-t1sBAB_EvSInkJ169dXhSqE6BBCAYLd8r7di9f32JC9VKCxtPgRpOtBhtPiHS13xgliggMrEgK3sTwc3bjg6k0Uw2E5fYLon7dEKEfqf7JPq791BRFd1lrnObPNcIz8R1pe_LOtclFjn0WI_90ig1nI_Ntd0NPDqBDwRbI6BfejaT3vgvyAEJlf9x5oQevqvLkUHI4Ve4Ad0LYiIRl3uKfQ_0gPR2attgvd5x_xbJhSjmYs_F6LkMBkLBPpWWGW3uu4jvo1fDrJ4hqEfnSYc39F7is55mraQ7VhVLXryeBSNvOFmGoxFyagvGbkx4WSN4AtZHkXRkxWY3Y9T3Lbw67CR2LRzaDNQ8dmwsTShAm-0IDaHXwKvXzkxbS30NJ5H0jwFEJNOuBufHAmfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020d7e0eea.mp4?token=eYDpJLHcsbic5c-I8BFaE6zNLXUrCp8aq3jGSDWI0Zvy1ghOHyTrXwzqfee6XYgOxvKEDMecV-tgSwkjCOnI4uhqaqaw82SSNO73Oy7CDrPgTmoLzA4RyZAfpdTlyR94z129AjTdb8WgYsFVRjKTOOQ-QWg7Gjo1EzME2Bqo9a4fm92_SvzD5lowcLmnzrRcorVpNsELNwetfq2SzkG48Vkr-TSyMGyNfhJqjl2PlC3jJKcxqgdsV0jRLGYoBlxkpo6x6V4SeHnd_fBXC8s8U_upM-t1sBAB_EvSInkJ169dXhSqE6BBCAYLd8r7di9f32JC9VKCxtPgRpOtBhtPiHS13xgliggMrEgK3sTwc3bjg6k0Uw2E5fYLon7dEKEfqf7JPq791BRFd1lrnObPNcIz8R1pe_LOtclFjn0WI_90ig1nI_Ntd0NPDqBDwRbI6BfejaT3vgvyAEJlf9x5oQevqvLkUHI4Ve4Ad0LYiIRl3uKfQ_0gPR2attgvd5x_xbJhSjmYs_F6LkMBkLBPpWWGW3uu4jvo1fDrJ4hqEfnSYc39F7is55mraQ7VhVLXryeBSNvOFmGoxFyagvGbkx4WSN4AtZHkXRkxWY3Y9T3Lbw67CR2LRzaDNQ8dmwsTShAm-0IDaHXwKvXzkxbS30NJ5H0jwFEJNOuBufHAmfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
ساکت الهامی، سرمربی پیکان: این برد را به استقلال تبریک می‌گویم؛ ان‌شاءالله در آسیا موفق باشند/ در نیمه اول تیم برتر میدان ما بودیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106168" target="_blank">📅 21:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106167">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4fb8db538.mp4?token=GGhKvaHp2j95gSneJrLxOJMmNatB2sUyuIxyv7wkAprcDOQf9TKCRpmu0ZDprpbSL2Meb8_YEhRu0DaDd9uAzuZhPovG80QFsCvxXIWeb4dtN8MXqxkKR2zPMF1uBjNovaZqsK0UDIMqmZClxiwsYqgXbEBBTBQX8IhThml6H8mNfIwUOH8ihlMjA1nZUzv1eRfJqSUK8ljlAZobKHIwmnDPkIJvPIhVSykvx5voi9Hy3bcklJRS76rChdP1tqliNk3xXj_BNl1xRz0yHl7BPkuKtesAf0lY22PFYqQ5UAdyAudgPUysfYMa-IcDh_wlsBdaclRg8YiWGwPFc9EFyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4fb8db538.mp4?token=GGhKvaHp2j95gSneJrLxOJMmNatB2sUyuIxyv7wkAprcDOQf9TKCRpmu0ZDprpbSL2Meb8_YEhRu0DaDd9uAzuZhPovG80QFsCvxXIWeb4dtN8MXqxkKR2zPMF1uBjNovaZqsK0UDIMqmZClxiwsYqgXbEBBTBQX8IhThml6H8mNfIwUOH8ihlMjA1nZUzv1eRfJqSUK8ljlAZobKHIwmnDPkIJvPIhVSykvx5voi9Hy3bcklJRS76rChdP1tqliNk3xXj_BNl1xRz0yHl7BPkuKtesAf0lY22PFYqQ5UAdyAudgPUysfYMa-IcDh_wlsBdaclRg8YiWGwPFc9EFyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
هوادار تیم‌ فوتبال استقلال: تا قبل از ورود ماشاریپوف چیزی از تیم ندیدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106167" target="_blank">📅 21:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106166">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c788208205.mp4?token=bVRNuN52ySP3DELw_o93lc3Lqcjr0H-l72TCOkY5KDBzj-C7ST7Vkx_rcaS2HLLoIfMfM0PZcnJMQfndobsRDoYk0gN3dLoIh2z9IdEi9oDljKukadCVur6Uh4-_nILpVQpMG6ZEMcRTHC5USUKnwx570Ow6C_f9355E-nPqGY52i1KPym3hbeF0zj9yrGO5vNCaBeHWKJ3GWRZdsfXMG1eeotefHRjn0KVeM4VqEurvph4684ZtgedmDFtKfvf2YkAMYzHXIO3E_wGKPDkFBaFlwxjpbHwnYWr3w734altQ_Ld4AGv3gQVLUuGyPvo_S-m_fO-_bynONr6PYJOZ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c788208205.mp4?token=bVRNuN52ySP3DELw_o93lc3Lqcjr0H-l72TCOkY5KDBzj-C7ST7Vkx_rcaS2HLLoIfMfM0PZcnJMQfndobsRDoYk0gN3dLoIh2z9IdEi9oDljKukadCVur6Uh4-_nILpVQpMG6ZEMcRTHC5USUKnwx570Ow6C_f9355E-nPqGY52i1KPym3hbeF0zj9yrGO5vNCaBeHWKJ3GWRZdsfXMG1eeotefHRjn0KVeM4VqEurvph4684ZtgedmDFtKfvf2YkAMYzHXIO3E_wGKPDkFBaFlwxjpbHwnYWr3w734altQ_Ld4AGv3gQVLUuGyPvo_S-m_fO-_bynONr6PYJOZ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‼️
هوادار استقلال: به زور بردیم؛ آقا سهراب دست از لجبازی بردار!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106166" target="_blank">📅 21:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106165">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
صالح‌حردانی مدافع استقلال: از آقای سهراب بختیاری‌زاده عزیز عذرخواهی می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106165" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106164">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e33ed4a004.mp4?token=XQT6Zy_L8WThCyiPYh-3N5yYPr0fOgo3ht7qFsR7pxh39SbTSVNZrbEunbMZZE_32qDEywgFz0O6gMULVIQvhoggLyEvEjub1ZSxg-VRUb5REUgg_Hec7Xs13j3UIHmGDBl2-5mTvfTQsbR9cZMqYdx_twggJ44DTwOnFyZHB0hPR_hXbZk0uoyIY3b2yuGidBm2OCS7SNnX0W5PldzibF1DTfMHcWUj2Xz0093OjN6PIhlPvBxDvEyfYrW8d0QWJXxzFjef845QCOHVpFR0pFQD0vamCj8uRRLd_WS1jRi0otm_hYmcmd_Z80fYLEis26Da6UZDDMOgL7fKVvkmBBf4ojePkSqjEh-k3AY4NvD4ZKNcDdLxCEgbR8gMDXoZ7byJz9AByeKwkhQIseCNqwYZqlhEB5oglScIgJHOXKkIHu02o4T0eKhGOA5nHSMjQnK6geuKBh1sHLNzanDXbNkxV0qHCw68OYha3LvWYL4NJUIA0NCTE92QCK2Lv9WF-VJyAvNPx3HcNBitMu402DIGXLChiQe-pHXuJDwhsp5Anh8HX2BVvbb5Kt3HQ2DaIBGsAM3thURzG19RXsG755ydVKgiPMPgYZLmBXwgYTe_R07-PJgS46OnSpk5jIW1ejRdnsNHXckxeUCfYc2o2xdVFrdOL4vHdQXJ_sxve8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e33ed4a004.mp4?token=XQT6Zy_L8WThCyiPYh-3N5yYPr0fOgo3ht7qFsR7pxh39SbTSVNZrbEunbMZZE_32qDEywgFz0O6gMULVIQvhoggLyEvEjub1ZSxg-VRUb5REUgg_Hec7Xs13j3UIHmGDBl2-5mTvfTQsbR9cZMqYdx_twggJ44DTwOnFyZHB0hPR_hXbZk0uoyIY3b2yuGidBm2OCS7SNnX0W5PldzibF1DTfMHcWUj2Xz0093OjN6PIhlPvBxDvEyfYrW8d0QWJXxzFjef845QCOHVpFR0pFQD0vamCj8uRRLd_WS1jRi0otm_hYmcmd_Z80fYLEis26Da6UZDDMOgL7fKVvkmBBf4ojePkSqjEh-k3AY4NvD4ZKNcDdLxCEgbR8gMDXoZ7byJz9AByeKwkhQIseCNqwYZqlhEB5oglScIgJHOXKkIHu02o4T0eKhGOA5nHSMjQnK6geuKBh1sHLNzanDXbNkxV0qHCw68OYha3LvWYL4NJUIA0NCTE92QCK2Lv9WF-VJyAvNPx3HcNBitMu402DIGXLChiQe-pHXuJDwhsp5Anh8HX2BVvbb5Kt3HQ2DaIBGsAM3thURzG19RXsG755ydVKgiPMPgYZLmBXwgYTe_R07-PJgS46OnSpk5jIW1ejRdnsNHXckxeUCfYc2o2xdVFrdOL4vHdQXJ_sxve8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تاجرنیا: امیدوار به حل مشکل صالح هستیم. جام قهرمانی استقلال؟ خبر موثقی ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106164" target="_blank">📅 21:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106163">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBYIkNndX7szd6jqe6i7iUkAe_deXCxeTD8LzaBj1qPIZ52jDCuvc17RKSjkF5VrhC-H9lNe670qSaXX66afrCi0WySF7jpwRTU8Q2RGH1bxSoPt3RSoBRpszXquVEWpqr6I2x6RgeAXs-UxjYRv-XPK_F92VJxK8WbB0WWLSouxO4fdvsvO11fvSJdJANJKlKN2Zu_SB_7LDrHcnwEyUav_m4DLbRp-vgC6W0eeWc1xcUpRE5qlz3stoRLXAW8hPS0_aNznawFc-MSnPN2vUElkgyabzuqQS6INJ9_cp6bQ2RUKTUxrqCqXmjQVXTtheTQwFNSHexTdrsZEvXySWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌هفتم لیگ‌برتر فوتبال؛ خارجی‌ها عصای دست سهراب بختیاری‌زاده شدند؛ استقلال با برتری سخت و دشوار به استقبال بازی السد رفت!
🇮🇷
استقلال
😃
-
😏
پیکان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106163" target="_blank">📅 21:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106162">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6bc94122.mp4?token=oWAYixjC_OQ6mr5t_cQXSuq3QG572CS67a4tTO1G6AE5KXDJBkMFr-kQHAn_v0mKrh_3mgfylRcsf9jKIqysOlrjs0pSBIsVqKpBsXJqS1CT7q_W85TUvibouVR_vVSzW1V6Dce4z_zyxjrbehPWRipXFqvuuojl6fbo0GcqgNT-ib93sp4TErv_qhdrbwTIDmD9vZwammGtVSZTSqMTFXNTQTL8yQVOqrxMa-TobTSMfVFOmrCo6-8AGamGDNRbeKSbIK6_Y1vZhRUI7Qi5JgpH1pHfbXLDCoNIzR0qb6qaSjhjOEauKXGqOfS4pct-Xg2azmT5Z3ISkMoLJ8aR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6bc94122.mp4?token=oWAYixjC_OQ6mr5t_cQXSuq3QG572CS67a4tTO1G6AE5KXDJBkMFr-kQHAn_v0mKrh_3mgfylRcsf9jKIqysOlrjs0pSBIsVqKpBsXJqS1CT7q_W85TUvibouVR_vVSzW1V6Dce4z_zyxjrbehPWRipXFqvuuojl6fbo0GcqgNT-ib93sp4TErv_qhdrbwTIDmD9vZwammGtVSZTSqMTFXNTQTL8yQVOqrxMa-TobTSMfVFOmrCo6-8AGamGDNRbeKSbIK6_Y1vZhRUI7Qi5JgpH1pHfbXLDCoNIzR0qb6qaSjhjOEauKXGqOfS4pct-Xg2azmT5Z3ISkMoLJ8aR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🚑
🇮🇷
مصدومیت ستاره استقلال در آستانه بازی با السد؛
آسانی لنگ‌لنگان از زمین خارج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106162" target="_blank">📅 20:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106161">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
🇮🇷
خلاصه بازی استقلال یک پیکان صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106161" target="_blank">📅 20:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106160">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICqF9BkWIcQBj9U-i0YWyLOQThMmtwcCWakNNT4SEULqTKiDMqeUo7X2lGwg01HRW5ndVFPMKriawOzJUwy_5gaybDHVZkLH98id9Z1XjdnIqQoS7z7etgHtT7YXHjhrKKqaM4iBuVr5kD13JcuXqj0nGwHqpKJvy5Bv8HQKNClTME6tz1LX60tLOGGWK1zUMGpum8-CIqqjiWlEuhf9EevMTlYCH8F6P6lrVrAlo3IieVJ0OVu8bi-2ACc8umz505NwsjThW6s7jvuFC6Wt57nd1-NM1cKRqvLTFUkTMbRLYkJt4s_T95F9zlZhnrQDOm389HEIELg29ocM4ZuP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌هفتم لیگ‌برتر فوتبال؛ خارجی‌ها عصای دست سهراب بختیاری‌زاده شدند؛ استقلال با برتری سخت و دشوار به استقبال بازی السد رفت!
🇮🇷
استقلال
😃
-
😏
پیکان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106160" target="_blank">📅 20:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106159">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33ea76eac.mp4?token=lLB1P3MIGUD3H-_nWhi1SDzUIVFShucDEuNbWsFYclZwe-qrunpOqSJEP9T2EnY44rBi7GDsY8yzFj58aP2NiLUTIezsn0zS2D15Rt2kcTErc4WdZthTh9ef07IPPlLio93mJ-fvDpEtt5-_70J18TnnxO7jc3yj39eNFy2UxWU0PRqQpfTVBzKXpaZE-LbmAklnYl_KPM78-9LXlBTCbjy7uag9CuNYvZRrx25DQOQbjLCLMXU57bcL8BVlBcowNZDBb_e4OOdLPymwQKxkqaWF4i6ZVjwHMSzzu4cOsHJzQMxouY33KNY0ccVL9SQk_HXWA2yj18I7oi0hObc1lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33ea76eac.mp4?token=lLB1P3MIGUD3H-_nWhi1SDzUIVFShucDEuNbWsFYclZwe-qrunpOqSJEP9T2EnY44rBi7GDsY8yzFj58aP2NiLUTIezsn0zS2D15Rt2kcTErc4WdZthTh9ef07IPPlLio93mJ-fvDpEtt5-_70J18TnnxO7jc3yj39eNFy2UxWU0PRqQpfTVBzKXpaZE-LbmAklnYl_KPM78-9LXlBTCbjy7uag9CuNYvZRrx25DQOQbjLCLMXU57bcL8BVlBcowNZDBb_e4OOdLPymwQKxkqaWF4i6ZVjwHMSzzu4cOsHJzQMxouY33KNY0ccVL9SQk_HXWA2yj18I7oi0hObc1lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آزادی چه توپایی گل نمیزنه و ۱۰۰ میلیارد پول میگیره از استقلال
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106159" target="_blank">📅 20:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106158">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c661b28aa.mp4?token=m6dBFMU7-SQEfuJLCgRQiWPvXWx7wF83iee0Wcynk0mqf08Qxo5pgPsCJgk5M37C3t42q1FB1HSjVL4lAjQEejHu90-d0XZQg-ExdbTLP_FDM12IWqTuV29o8Ph5iCSggzJoeFeCqOJXrNN_EewFj-vx1C6qdTqhF7CrlzvSQmPmdgLJIaSsRRrdAtzbNOCLYBMhhAejWV0SmRTkTjwJr9PtznVBZZ1AnZ3nC15sIS5D0Y-rCc-FbX3-Ue5XnMWLBbG0-OLuCrXkDhCz7cfyIcc3qRaDASd_QpQ5XooMA-1bvJybfskddXe_2jx0RHcHxL2CfXTQe19NtO5TLCbLjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c661b28aa.mp4?token=m6dBFMU7-SQEfuJLCgRQiWPvXWx7wF83iee0Wcynk0mqf08Qxo5pgPsCJgk5M37C3t42q1FB1HSjVL4lAjQEejHu90-d0XZQg-ExdbTLP_FDM12IWqTuV29o8Ph5iCSggzJoeFeCqOJXrNN_EewFj-vx1C6qdTqhF7CrlzvSQmPmdgLJIaSsRRrdAtzbNOCLYBMhhAejWV0SmRTkTjwJr9PtznVBZZ1AnZ3nC15sIS5D0Y-rCc-FbX3-Ue5XnMWLBbG0-OLuCrXkDhCz7cfyIcc3qRaDASd_QpQ5XooMA-1bvJybfskddXe_2jx0RHcHxL2CfXTQe19NtO5TLCbLjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل اول استقلال به پیکان توسط آسانی(76)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106158" target="_blank">📅 20:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106157">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
✅
گل اول استقلال توسط یاسر‌آسانی</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106157" target="_blank">📅 20:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106156">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01d6e5347.mp4?token=r508sosbdbF1_58DF47p7P3OcEE_jayAVDSRFtP1Q8OWQMY0GqVy2I4cl1rSqNGREtrAqc_jfdpxsEbH7ht2RTdBCm6VqZsJnCIZ9YbtInNiMRFNbFQW6GYVktklVuNBeFcgy4BhDrQluXzDK44WpMEsxeElKECtqUyj5rd0tIKjrhVpROS7Vpenxa-MAn75XQ5WalB9khkh7RQ_UUUj3uDb7EvOwJcTFZzDruvvTyNWhiUk-Yem7c93HXnd1lfnVD9o-7wh9AS3NgpnvcnZkltQn06JJBmseHiozjRKYM0shqT2OEMjVt94KXQO3OOSQb3a2cgJrZGJj9HG0py1kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01d6e5347.mp4?token=r508sosbdbF1_58DF47p7P3OcEE_jayAVDSRFtP1Q8OWQMY0GqVy2I4cl1rSqNGREtrAqc_jfdpxsEbH7ht2RTdBCm6VqZsJnCIZ9YbtInNiMRFNbFQW6GYVktklVuNBeFcgy4BhDrQluXzDK44WpMEsxeElKECtqUyj5rd0tIKjrhVpROS7Vpenxa-MAn75XQ5WalB9khkh7RQ_UUUj3uDb7EvOwJcTFZzDruvvTyNWhiUk-Yem7c93HXnd1lfnVD9o-7wh9AS3NgpnvcnZkltQn06JJBmseHiozjRKYM0shqT2OEMjVt94KXQO3OOSQb3a2cgJrZGJj9HG0py1kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🇮🇷
لحظه اعلام پنالتی به سود تیم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106156" target="_blank">📅 20:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106155">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106155" target="_blank">📅 20:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106154">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106154" target="_blank">📅 20:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106153">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
احتمالا پنالتی برای استقلال گرفته بشه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106153" target="_blank">📅 20:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106152">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqQyjchWwRabKvlDkj_CtS1Vl6DQ9_v06VxEfflYC6tleD8zQXmyOQJjiBIcBmu4D465n4v8WnqkxiPm7q6v6LyIfY8jdTwjdm5tRqB8Ls4i-2jiYCiskq_lrNz96ExHzHwUsoZv1oGC62s7Ahfs5lIXKTp2t3Xws_9oBfumiJlgFfPsD9tYGf7TMPYcAu99FBikTH9_IGftakS-Vn6Jweu8DG4HLUF8Zj9wlxFmR_r__9dKkkpeFhWUNz2iInqeYL07xSwx440Gt3aZL0azI6_k2OtlmoRkUvERjH_9rG1u_Fia9eDM_UPR7EqGVLCkFoczlegzme65BjFjF6GvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
تیفو فوق‌العاده هواداران فنرباغچه مقابل رم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106152" target="_blank">📅 20:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac6a80c90.mp4?token=aY43XzKeMNzgymNxAC5IxBkQN_9rMEUBHYhW3dpWAZg_LC4Zep8rStZbPrh5sQsFL8DaguZDAqCW9mawo98NoBtX1oVVE3gGzaV3gZ57ZODLZ8gd8sX9m0ndY-8XDjej-kYs4xcY2X5Z1SF9N8bLYn9aykk0Nn-VAEn5MmAVLomFWuhhlmO072pHwK8R-MSWdVKEEOOL8K4l0nXdzKTW4ywmbL1Rb6fFTIMUqS66q3fbQg00yi5LdQ5tN5bKEeD_D2HI7IHfovpEu2Oxvh67C1QT_y3HjgSsPEP-GH_fQGwRAqYk0SBkuE61TO_pwnPBptX3AspnnLo9j31G_Ddisg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac6a80c90.mp4?token=aY43XzKeMNzgymNxAC5IxBkQN_9rMEUBHYhW3dpWAZg_LC4Zep8rStZbPrh5sQsFL8DaguZDAqCW9mawo98NoBtX1oVVE3gGzaV3gZ57ZODLZ8gd8sX9m0ndY-8XDjej-kYs4xcY2X5Z1SF9N8bLYn9aykk0Nn-VAEn5MmAVLomFWuhhlmO072pHwK8R-MSWdVKEEOOL8K4l0nXdzKTW4ywmbL1Rb6fFTIMUqS66q3fbQg00yi5LdQ5tN5bKEeD_D2HI7IHfovpEu2Oxvh67C1QT_y3HjgSsPEP-GH_fQGwRAqYk0SBkuE61TO_pwnPBptX3AspnnLo9j31G_Ddisg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
🔥
سوپرگل دیدنی العین به الوصل توسط عبدالکریم ترائوره با گزارش قائم خلیلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106151" target="_blank">📅 20:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106150">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226e1ece2c.mp4?token=kTau-zqK-mlAbvBx5gDk5ud69vz57dIsUvmshLIGo9oQZNrwo6Kx-LsxaTqwyyu39heshn1QHuW8QmG-kLdRkM3oe1yviEhsDPg66y8plRehVi7eppfP-cLx6FFomoIIMzqWudGtYLEOtl9M2cPXRkeHoLl6a0rwjIJenftJnxB0DpnnzgB4rWYmiYZtaFr5FTt8H7Jr_sAqliCzZdmawi7Huf42jU7Frn0tsEMgiEtik8Ef_vOIyAz3ISbBQmxLaN7dRDI-G81oqZANh7IeCmTWfG87vTcHlTyp0cnz0Rwy3a4hTrRYCcj8jFIvFL1Zwb8XNSScPt4ZTBFOzm_MUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226e1ece2c.mp4?token=kTau-zqK-mlAbvBx5gDk5ud69vz57dIsUvmshLIGo9oQZNrwo6Kx-LsxaTqwyyu39heshn1QHuW8QmG-kLdRkM3oe1yviEhsDPg66y8plRehVi7eppfP-cLx6FFomoIIMzqWudGtYLEOtl9M2cPXRkeHoLl6a0rwjIJenftJnxB0DpnnzgB4rWYmiYZtaFr5FTt8H7Jr_sAqliCzZdmawi7Huf42jU7Frn0tsEMgiEtik8Ef_vOIyAz3ISbBQmxLaN7dRDI-G81oqZANh7IeCmTWfG87vTcHlTyp0cnz0Rwy3a4hTrRYCcj8jFIvFL1Zwb8XNSScPt4ZTBFOzm_MUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل‌اول استقلال خوزستان به تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106150" target="_blank">📅 20:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106149">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn-KKGitXSRizRVkxx5vnrysLvj0Sqyovsi7_oZASX2SMQmfSpOhwik6LxV2D8BZcxDFRNGuBsK5f6IG2oXyqPlPG0Wcfmvb0K7xQ3zEnFsWL32boykG0DzKJuuDdWqs1_3B8WJBuv_0aksO95fZA1sjp0-Q_CC-Mlru4S4nCyau1_dD1JA3Qf7rytxH1e821t9RXo-zO7ufnGnd9UBCn_wsx32swEqRstL6CAKxAVq-o9nkvG2UvESwCip8clQwVs1t3JBGnXJSL8_BOGjRYsnF3-C0gGNxBgnUCsophLB1MKuGluUfGg7pSmsCaQVD5iNyrtFMvneJ4dOnxtKESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
‼️
سقف دستمزد پرداختی تیم‌های لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106149" target="_blank">📅 20:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106148">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce42c1eb19.mp4?token=DxgZjE-fZV4sbml1oM7-L3w486TJZiMOi8BVTRvSxaeg-DiOKoZSErXaGAXGjZn3JbzU22foBPD0F_LDY8LYcXxB_GXfTp-GVQQz8a3WKQeQPGoQqsZrqle_1KunKHOvsqV2gAaAhSu_tV0X0BdESh9t8IJwMmpkYMsOIFHRP8kT5waYeKugcZxz5Ld9pD3pMVhKI_8nXg3YgfPvbR9gIEiRqxhhIZVOTEcxoDrI8AyDSd-qwP8AiiMqEinitgThpmEt9fyiZvEJdxF5pBKLvHDCWFyFZP9ga4M1ztJUjeBvJzaWTH4I_bJnh8JXXXi1fOwjkkzW52sr4TZeL_Fr4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce42c1eb19.mp4?token=DxgZjE-fZV4sbml1oM7-L3w486TJZiMOi8BVTRvSxaeg-DiOKoZSErXaGAXGjZn3JbzU22foBPD0F_LDY8LYcXxB_GXfTp-GVQQz8a3WKQeQPGoQqsZrqle_1KunKHOvsqV2gAaAhSu_tV0X0BdESh9t8IJwMmpkYMsOIFHRP8kT5waYeKugcZxz5Ld9pD3pMVhKI_8nXg3YgfPvbR9gIEiRqxhhIZVOTEcxoDrI8AyDSd-qwP8AiiMqEinitgThpmEt9fyiZvEJdxF5pBKLvHDCWFyFZP9ga4M1ztJUjeBvJzaWTH4I_bJnh8JXXXi1fOwjkkzW52sr4TZeL_Fr4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
تشویق شدید صالح‌حردانی پس از عملکرد فوق ضعیف استقلال در نیمه‌اول مقابل پیکان
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106148" target="_blank">📅 19:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106147">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494b673a17.mp4?token=Ss1dZrP54Ett-YIwsw7rnhW77iVD35m1PPAHZ_axg-3bw6Gx6EfxkAl71KO1Wm9YP6gXYA_CJ09PQyAAzHBrVXbO7castCuGDQeHXNB30YondE57NiwoKmQn2rFcllFeCml7wjLs7PvurVifguSAEfRBarHsvdZPbyGuKDSBmNECOew9jx5O-J5S7rUKfBa8Gm7P7jvWziMHi8JyybiyNMRQ8sVi-ojwASUOOFEudIdT7xedtgv0T00dVy82qDFTI3mIfljDmqJE9rbUPEU13OiYAM2gIIuvqqD_a7r-5ZSGmjJ54MhpIDemGLWxpSfUvTEpMlf456-rhsae4q-59A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494b673a17.mp4?token=Ss1dZrP54Ett-YIwsw7rnhW77iVD35m1PPAHZ_axg-3bw6Gx6EfxkAl71KO1Wm9YP6gXYA_CJ09PQyAAzHBrVXbO7castCuGDQeHXNB30YondE57NiwoKmQn2rFcllFeCml7wjLs7PvurVifguSAEfRBarHsvdZPbyGuKDSBmNECOew9jx5O-J5S7rUKfBa8Gm7P7jvWziMHi8JyybiyNMRQ8sVi-ojwASUOOFEudIdT7xedtgv0T00dVy82qDFTI3mIfljDmqJE9rbUPEU13OiYAM2gIIuvqqD_a7r-5ZSGmjJ54MhpIDemGLWxpSfUvTEpMlf456-rhsae4q-59A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
آغاز حواشی در استقلال؛ درگیری حامیان صالح حردانی با حامیان سهراب بختیاری‌زاده پس از پایان نیمه‌اول روی سکوهای شهرقدس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106147" target="_blank">📅 19:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106146">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae32d5f075.mp4?token=BbgMgwdiiZIRbEMXGQPM-UOm0dJN7PZJxAFmAtBdEP7P5l0EBR9ZCzlBdgHjjVJYV7S3f5SQpWmVo5Xhb5uTqLRGo4NARgNBm3lp6okxjsMXaS5lkwW_TOgF2V0EXkdYvfAhRmOJFPg-sB-6m6USgSqaOd5e1lYPJVm6vqSzwWjJPcgnv55nkCSTjiZsmn7o74p5Wr4-1OMDFxD29jVzB5le00EDfK6kcn0c6IzVU9nmQHOrKgpdG5lfxl6GxNd7LbkzmjWTWyg-YlHTKIqpBnt6efEGLVS_VrqWiDxza_B56vuXIy8lajtp3xCBYEEuVeWIx6kmJKNESZvV6kBGrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae32d5f075.mp4?token=BbgMgwdiiZIRbEMXGQPM-UOm0dJN7PZJxAFmAtBdEP7P5l0EBR9ZCzlBdgHjjVJYV7S3f5SQpWmVo5Xhb5uTqLRGo4NARgNBm3lp6okxjsMXaS5lkwW_TOgF2V0EXkdYvfAhRmOJFPg-sB-6m6USgSqaOd5e1lYPJVm6vqSzwWjJPcgnv55nkCSTjiZsmn7o74p5Wr4-1OMDFxD29jVzB5le00EDfK6kcn0c6IzVU9nmQHOrKgpdG5lfxl6GxNd7LbkzmjWTWyg-YlHTKIqpBnt6efEGLVS_VrqWiDxza_B56vuXIy8lajtp3xCBYEEuVeWIx6kmJKNESZvV6kBGrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
درگیری لفظی عوامل دو تیم روی سکوها؛ تنش و حاشیه در جریان دیدار تراکتور و اس.خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106146" target="_blank">📅 19:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106145">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkKDlRoA7GRZiMXKN3MaHyDZNySZ3wjmooryXR9dRa51tMlSp6NMVT0Z_gSw7Ho-L1D9cvMo81xd3b-p3mDCVneYeyWjQrkMnGhpHlm0tIxg5cDd9QbOYJ_mj0wNXao0hfE_rqTitRWVefUWArLCZ-l286KSbr3IvcrybETtBPB3Xcru9uMdYM_KMzlIfJng9ETl2MuR-mngYr_uZ_y2eZecT4uJgSCV0q7KnRHDAxL7JtfNolKJ2pPnT8DwY8o9o37yvPiKJkuNTD1zI042znYxFaep1-l016rz2Wo_iWFRlHO1eoTlWRZfd19PjioxFWna2Ao5I-smpIxxWALg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🏆
فینال جام‌جهانی ۲۰۳۰ در استادیوم الحسن دوم کشور مراکش برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106145" target="_blank">📅 19:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106144">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">استقلال با این سبک بازی جلو السد باید به آیات الهی متوسل بشه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106144" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106143">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663dc60b7.mp4?token=WQ8W-4d5nglBotVt5KMH6nAVp5mHl7HTwnrwNnmJgdLoymizZMEHmqB9go_AD80TcJS5VEB4Yn4rX2JDtEB-OGna0Ng0oto8woknGWuG7YjVjCl5RFQCoU-UOzojAUDtWWGX092kMHWeYKVzcrQeKgsHfOW7VuEK2eROMXGH9yI83VhcO4PMZsO2Uo-EwnzNMCXqTL5qIftqLnmd49uA3hZXoyk8uxn3FciJBaoUagMcAPHRmbqeiLo5QnNTRBxK5bSV806DlwREJRqHYbCdMnw92Xiz7rVFvI3yvUFTHEacvz7jeNC52zAPGzukMSkL1pgTj1P6YD8-NILG1h_HEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663dc60b7.mp4?token=WQ8W-4d5nglBotVt5KMH6nAVp5mHl7HTwnrwNnmJgdLoymizZMEHmqB9go_AD80TcJS5VEB4Yn4rX2JDtEB-OGna0Ng0oto8woknGWuG7YjVjCl5RFQCoU-UOzojAUDtWWGX092kMHWeYKVzcrQeKgsHfOW7VuEK2eROMXGH9yI83VhcO4PMZsO2Uo-EwnzNMCXqTL5qIftqLnmd49uA3hZXoyk8uxn3FciJBaoUagMcAPHRmbqeiLo5QnNTRBxK5bSV806DlwREJRqHYbCdMnw92Xiz7rVFvI3yvUFTHEacvz7jeNC52zAPGzukMSkL1pgTj1P6YD8-NILG1h_HEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعار جدید استقلالی‌ها: جامو بدید، حق ماست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106143" target="_blank">📅 19:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106142">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa632d35c.mp4?token=g5RKog6g34Sl5IDZjnqMEV3d1ZH5Xc8vIrqc-bHp5z39FGiUBk7W3ZRxE44-Gj-X5rW4wTYsctpcJ8qfJ-7EfW1AMs3La1VYhBXhhSnEj-9ZYtaABqhwl6wHoM2mEK_8-sJL292xl18WdH2bqAOj9lqHKMhNKUyoAwd5vID1hSt56YrE2oVXSgjvc85tY7igDrJA5rx_3VHhr2RMYFH4iiSstuuQt1mZpzZxEbVYRC0MsvXBbvNPBS8vjQAAOR5Hxn_P18fshA4SWciYTN87dp9FUmYC1irn35eLkMz2K2OG0dVc90RMdycVIgyhRtF1gqbqE4ayf2SF7v6PtytT1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa632d35c.mp4?token=g5RKog6g34Sl5IDZjnqMEV3d1ZH5Xc8vIrqc-bHp5z39FGiUBk7W3ZRxE44-Gj-X5rW4wTYsctpcJ8qfJ-7EfW1AMs3La1VYhBXhhSnEj-9ZYtaABqhwl6wHoM2mEK_8-sJL292xl18WdH2bqAOj9lqHKMhNKUyoAwd5vID1hSt56YrE2oVXSgjvc85tY7igDrJA5rx_3VHhr2RMYFH4iiSstuuQt1mZpzZxEbVYRC0MsvXBbvNPBS8vjQAAOR5Hxn_P18fshA4SWciYTN87dp9FUmYC1irn35eLkMz2K2OG0dVc90RMdycVIgyhRtF1gqbqE4ayf2SF7v6PtytT1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
صالح حردانی با حضور در ورزشگاه، دیدار استقلال و پیکان را از نزدیک تماشا می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106142" target="_blank">📅 19:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d99249b1.mp4?token=Q2QxVZPNFRh2gSvQ0ioqnmpbIvDD14aGTRjcWklPIroahrxdV2VMoh17D9Drw0xFy11eDuDLGNDaEXBfU_x_V-oMg--nnR6Ft6ZalkQT7RIJk3n93yWrkYlsssgk1T_niYvPMk7BUEjIjd3hdPY50yLIhqxDntd68zdk8ZXnN0DGWW89KvuIPcjRhn566O8UG7HNgPDMCqx_QARIbFMjE5ifVqPK3WhPLUbEZOPeKeAo4yBL0gYc4v5PE8-jFtfiQnsVdyVV93ViojZ_qCuvLPn25R7pf650pUdNK_G1NzMeGWw-SvrI3AedupNlPk_sffoc6Ccwsk1nQ_JDmbB3xDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d99249b1.mp4?token=Q2QxVZPNFRh2gSvQ0ioqnmpbIvDD14aGTRjcWklPIroahrxdV2VMoh17D9Drw0xFy11eDuDLGNDaEXBfU_x_V-oMg--nnR6Ft6ZalkQT7RIJk3n93yWrkYlsssgk1T_niYvPMk7BUEjIjd3hdPY50yLIhqxDntd68zdk8ZXnN0DGWW89KvuIPcjRhn566O8UG7HNgPDMCqx_QARIbFMjE5ifVqPK3WhPLUbEZOPeKeAo4yBL0gYc4v5PE8-jFtfiQnsVdyVV93ViojZ_qCuvLPn25R7pf650pUdNK_G1NzMeGWw-SvrI3AedupNlPk_sffoc6Ccwsk1nQ_JDmbB3xDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شعار خاص هواداران استقلال: بختیاری، حردانی، می‌ریم برای قهرمانی
؛ این شعار به نوعی درخواست هواداران از سهراب بختیاری‌زاده برای بخشش کاپیتان آبی‌پوشان بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106141" target="_blank">📅 19:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac6e743e8.mp4?token=Q2ImTuyXR2XITIlLZU84BWzs0AFkDY-weJnmhTG6FOD9qyBKRa56jJZ4EE-Ab4eVwaGNg_naaG0eRDusbS5AYKCYFyD4dNB0piJL9zEgKcxzY1qZ21n_tEty8yIY-pTWLjo-rgkCplkr0bTj6D3xSNmX9ynSv14rY1cCvyAYgfn3pYx35sJOwfHMKGh9azpZ-wjk5Pbx4pv7ZtthVt0BFlt_tNsQZ5iuJQRINU2K8JjDVpWL-wYvekXDLFy6dk6B-DAkrHY81O3ZvzrrR_MN0hUJJmQbdXpJx746Y_MrAoglB5y-EmnKzWOdHt7y5Q6YqV8RmeXsqVFPbcX3BG2kkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac6e743e8.mp4?token=Q2ImTuyXR2XITIlLZU84BWzs0AFkDY-weJnmhTG6FOD9qyBKRa56jJZ4EE-Ab4eVwaGNg_naaG0eRDusbS5AYKCYFyD4dNB0piJL9zEgKcxzY1qZ21n_tEty8yIY-pTWLjo-rgkCplkr0bTj6D3xSNmX9ynSv14rY1cCvyAYgfn3pYx35sJOwfHMKGh9azpZ-wjk5Pbx4pv7ZtthVt0BFlt_tNsQZ5iuJQRINU2K8JjDVpWL-wYvekXDLFy6dk6B-DAkrHY81O3ZvzrrR_MN0hUJJmQbdXpJx746Y_MrAoglB5y-EmnKzWOdHt7y5Q6YqV8RmeXsqVFPbcX3BG2kkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
هوادار پرسپولیس: به عشق رضا شکاری آمدم پیکان را تشویق کنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106140" target="_blank">📅 18:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d4f3e014.mp4?token=M8A1O1EW_U-CV3ZEoHkfBf4SpCWdhvaPRGVoai--RIPsjZMQI9J_ZN0PQ5gSy3CmyWkQJaLWPf7Dhw3WZJ350HIKij448vHtlECIkgPoFcwCmTs0Y3H7nLOu6ohMkQcSBQXt9BcvBFxWr5kgHbgUyNrMcxxfbZslxujtJzb3PIY7Op-u0UIfXr_dHOsleJUy_AsoBklK9MRAWpZuGxiAz7XOeKvWERzxDpoP4FdXiym4DBmctW240itX4WLHGTJdFV6ulf3lc-EFonJsBdENk3KHNVLkW2vGVpZ1mGQMbmxPht3DPsD1bd31csI6lekx96jpaxbetbvq4mx-P3Mzkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d4f3e014.mp4?token=M8A1O1EW_U-CV3ZEoHkfBf4SpCWdhvaPRGVoai--RIPsjZMQI9J_ZN0PQ5gSy3CmyWkQJaLWPf7Dhw3WZJ350HIKij448vHtlECIkgPoFcwCmTs0Y3H7nLOu6ohMkQcSBQXt9BcvBFxWr5kgHbgUyNrMcxxfbZslxujtJzb3PIY7Op-u0UIfXr_dHOsleJUy_AsoBklK9MRAWpZuGxiAz7XOeKvWERzxDpoP4FdXiym4DBmctW240itX4WLHGTJdFV6ulf3lc-EFonJsBdENk3KHNVLkW2vGVpZ1mGQMbmxPht3DPsD1bd31csI6lekx96jpaxbetbvq4mx-P3Mzkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
هوادار استقلال: سهراب هم مثل فرهاد بدون باخت قهرمان می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106139" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8269376a.mp4?token=PxwGkACzt_2egtZx9CjEap-4ASl_eQjS2T0514SS_lf8u6LSyEhnwSweWJmkEQNLEiD1cl5yQWxARAzBj31-kS43VpdfoaZ096NaCGHpwmGlRoLQE7EPOQFx6SEJEg4gQU5DdhccGlJvvn-Qk154OgxuCoM2rZoVxa8tWqh3tZeeXKOGsSlX_yS3KbIej5DKo9lC2kVS2yd-SWjWeaotTiVieXwOHrFWsW5HUvlxwgIQ-GL-i6xpo12w35Uhbzfs6Q7D7dCG69GRcdr2jGKZF1fQFg8X4dX8IRKU2FT1i_wToMmVbLxIV82e9Uy7O8MK0ceo2Fsrdz4oMryHcgMA1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8269376a.mp4?token=PxwGkACzt_2egtZx9CjEap-4ASl_eQjS2T0514SS_lf8u6LSyEhnwSweWJmkEQNLEiD1cl5yQWxARAzBj31-kS43VpdfoaZ096NaCGHpwmGlRoLQE7EPOQFx6SEJEg4gQU5DdhccGlJvvn-Qk154OgxuCoM2rZoVxa8tWqh3tZeeXKOGsSlX_yS3KbIej5DKo9lC2kVS2yd-SWjWeaotTiVieXwOHrFWsW5HUvlxwgIQ-GL-i6xpo12w35Uhbzfs6Q7D7dCG69GRcdr2jGKZF1fQFg8X4dX8IRKU2FT1i_wToMmVbLxIV82e9Uy7O8MK0ceo2Fsrdz4oMryHcgMA1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
هوادار استقلال: مشکل فدراسیون با ماست؛ وگرنه جام را می‌دادند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106138" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106137" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuRstQQYVBMqKV1MILqFys8SZAbR7vUNS17369CfAM0dKvjJepOIAEOgCPcdXjeDUSiPzR4y3ASqr6ryJjTUyQK2zGLxl-6Wbr7VfPmsJKC8FjpCvJCh1cWt6N5PelGBmvgRt7KRdyJ14TPvo3pXIY1gvxoD4mz5Ucr3IimHglxcaWrhIxLaBJaENFZZDGjYKZR81DifTTJCMCjxZDSnfQqjjm9m_-L907RDF9mX2hhe8IDRllVdUCNVAyqr_e3hxFQL2H2rXgj33mypwwnQLaiOtjlmaassq4ptVlFrUc8hgNzLp6q1RxisxqsJ6nek3tZSDPHjEXkdrL1e6x4cyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106136" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106135">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VngrFxPt9kWSsohcq4cqGCo29yXEhhuWs8_BsQiIerTIo5tcZ5v2RcmC0mmgHNeXn3faZIGYXccs3ORRw6s1HOtSnNOOgZL3HRQQ4MCQI33d-oHwbtxaaBGPEGAAGOjL_gYdPLZQ7YbUES9_Xpjh4sI4TEpDn8f3uFJs7HEpdlIFlWRCwsm47g6jMYs64Rzr_nBt4AULDSRtsR4kOq5HU_ddzI511xkzY135get-5b2fuDGyZvQ7EgTOP7FMybAPLX50OHTEPLrv2-GqLLiFnlsSVQyT0vGoTjZ-vnyDYLDKnNV3QOkQLhUwQl-xl0QgWwQjablxD_F4pcypzni6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106135" target="_blank">📅 18:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106134">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oudyPBMMfCPCNsplXctiey-sFUXXqvpdwxNxPPY9g6rMf1gNiWV6-bQocCfT6wD2kBQ7IKFC-ify4EUp-aqrhDkhGW7bKJlvhf0fXacVTU1Jf0JE4oER-R8uValXsePsvHWKuTlLI4lrGu1iPH9xWdkGAYEDPL8q4N6G8_ucVb74ra80ly8bhcyUEyc4Toqv-4ggmeA3h6gE-_7X1EruqpP7VCAedtIh2QWLNGsv_p6mXYHOUqx7cHOvseqZorFrVU7Aj49PN00ML-CEYKUW-24i1bzAzknirpcFTsvoZA6RrVoiKPgaCJYjCKbJrDmLv3Sy1xLknebBzlikjtx40Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106134" target="_blank">📅 18:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106133">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
ترکیب تراکتور برابر
استقلال
خوزستان
علیرضا بیرانوند، شجاع خلیل‌زاده، محمد دانشگر، صادق محرمی، دانیال اسماعیلی‌فر، محمد نادری، مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و شهریار مغانلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106133" target="_blank">📅 17:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106132">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d73a4eaf66.mp4?token=G6IAS9lVgh2m3TgFCRt8nPkilIuXvUdsI6xj3lVn-Gj9kVisQmp4CuJTSww-7XQMGr-HmJAZrqIXBHuYL5m7XpBDZObWylCr2K5MWvGxSdHuMtTp-JcKbeyrtyIftQKLzzZpmCGffvqHPWI3jmZiw6o8QUU5F24KSHHeArFN06zCR9FNY6pMVKfV7BpcY5aV80SNvtTbElYJ7dbT_F7R9Dah0qF9mIDYN-XgSLS32d_lHlZp8t_1k5dYV73nlMBLLz65wzUkBk9zcUnYJfuFJbaHdc6B4PVb0NgMeELyN4uZH3eYLpcZHctvTMwynhg_9L-BfQregvCq9OSpUuGETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d73a4eaf66.mp4?token=G6IAS9lVgh2m3TgFCRt8nPkilIuXvUdsI6xj3lVn-Gj9kVisQmp4CuJTSww-7XQMGr-HmJAZrqIXBHuYL5m7XpBDZObWylCr2K5MWvGxSdHuMtTp-JcKbeyrtyIftQKLzzZpmCGffvqHPWI3jmZiw6o8QUU5F24KSHHeArFN06zCR9FNY6pMVKfV7BpcY5aV80SNvtTbElYJ7dbT_F7R9Dah0qF9mIDYN-XgSLS32d_lHlZp8t_1k5dYV73nlMBLLz65wzUkBk9zcUnYJfuFJbaHdc6B4PVb0NgMeELyN4uZH3eYLpcZHctvTMwynhg_9L-BfQregvCq9OSpUuGETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
حمله تند هوادار استقلال به بختیاری‌زاده: برای دلخوشی پرسپولیسی‌ها صالح را اخراج نکن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106132" target="_blank">📅 17:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106128">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_w4EiTUgkVf30Cxkfg4PQ08dak1aXJic2hsmsseUcDvIfX7M7GntkhXFSTvZ9xTl0oMKj3IIERMgSF5Z6RQmUUOu0GyI_VraCCN27heq5GX9uARJE7syLUy0tpwe4qSQouJiXbq53Sn0lWB3Opvi9oN1jGNIFxtrFOkZEZglsGmaUAXYYsS8XQyL7gJKU5jmpv_qTTmpF29YLzL-WQWBYM-aF97OG4XLyfKUfwMMOqXQX8mjnL7qrcSx6zPliC4R2CcBcaeaDzBoCRS9rOtQjLj72-fS4RcfnyZ89abY8vm6DuMdAp_pjjew4KFkxqNqXaIgTA5rSRd_ftkws940A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4PnUXv07SdU4aVPhCZABkn0OF_xdCOHRq8r9g0E8WYJFkHZtitFeppHhZlTQwWbjNBISjqzlP4imXC8_K95agF2ZSaGU3tZ1Qt2FsDd7SRyUqZdBDgqxtEiEkCI0BCsKd56FbnhKAacuFfB4wYWI_OPqJ1bChk8VAJSTRRDPayg7VW6jvoLahSRP4GaBEYMxyNOdoKnYNxU1bkB3b7aHAo-3MdQZcggFT1revizzujQIR7gcB7TrKZezwG-_mElFequwPhqiNAwyen75V-mXii6Lhi0x_ch6orJmoVN2S5aKYtXdALEvHujmst4f83a01BFwIfRkr885DZ_GcWwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUZdBmySay96EsqwcBH51ZFgxCi2Ii2aEoH3Bd9qDOGtv75hp0Ok8x6M8TP5I11_zzm0bBOipiKk2iEdVZAX-FrczIAdJWMOVBOrKJdVGil-Z1W6isu4BMK4oqTLLtsBTm6TniYAODk3ixQ9J9qRLhJY46OLNbGhk7QeJ635tRlg15AAUCTIDkXnvMqO--ftN996mQuk6u1-4gXoPj7YTdtOT6RC_T_rsvk7Qf6YsluRPw9RrsfpkTKcipM_8zcQpwrGL3ww9fPBvOjgsFNbR8lbGO1_42zNJh3PxeQGlrSTVO_HObC7gzyjDHnxuSWZHvDsK80a7TbdABU2-tMNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MixFZ62f78v7wJ7Iv9EX7-Ybuv7bBg5tCz5gzNVejx1Ni3Y2QCOBnOIU8JQtFxi1Rl4LbV6OWqPo4GkPeKX_TFzKypvDX6hKVqrHCPeVoVzsKWrjB8vOmuKcDfOtEEmVBKG1Sn6gzYefww6DckwSKln0qLBXwKqTMTSiYnOM5I_iGDJXEmP1Dssq_u7F-H4uuBjsLrW9UZnLS2Ee99HKFM-ABFGTrpYsE6T7GW_9mN5RYVWXhsn7eSsotSpHkjb2QPi5qj1V3IqkDr8Hwe8brchXhili3NSglkriKvMp2hkjuy_uHABo9hv-kNdV19uKTQ6ETyl9FeY0qRRRMNp6cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😍
زیدی خوشکل و سکسی امباپه تو فیلم جدیدش یعنی "Drawn Together"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106128" target="_blank">📅 17:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81979f53d.mp4?token=hSUTOszZm4zr2MMvktq_1oRztQcMVdaPtbsi0vyqOnVXRrHVwHtjuGkM__xrATFUN_EWS-eEKZt_yZzF98GLSfUV0VX1boR056LHqQJMXgwOzmRFuUXuW1JsklkRPzQ71X-0FGZEAzl52WB8wYTkM2BTUtU15PASzjmyXTbW3HyN0g7P8youUwDkZsg0pSGToIZr_nUtv0op8qm0GfqV3ChG3L8sKPieY40huiMYbGQDXUPHAPz4hVT3u_ZISKvcqEMl5mD-xkfVVQpVdGXP2McJQZN1lFbIRJfXlBOfAcsWygzq6AeS_FPsEKXAG3OaKMg1GXuTj33qJ53mJfLAJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81979f53d.mp4?token=hSUTOszZm4zr2MMvktq_1oRztQcMVdaPtbsi0vyqOnVXRrHVwHtjuGkM__xrATFUN_EWS-eEKZt_yZzF98GLSfUV0VX1boR056LHqQJMXgwOzmRFuUXuW1JsklkRPzQ71X-0FGZEAzl52WB8wYTkM2BTUtU15PASzjmyXTbW3HyN0g7P8youUwDkZsg0pSGToIZr_nUtv0op8qm0GfqV3ChG3L8sKPieY40huiMYbGQDXUPHAPz4hVT3u_ZISKvcqEMl5mD-xkfVVQpVdGXP2McJQZN1lFbIRJfXlBOfAcsWygzq6AeS_FPsEKXAG3OaKMg1GXuTj33qJ53mJfLAJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار استقلال: سهراب باید صالح را ببخشد؛ ستاره سوم را می‌گیریم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106127" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59106dd8ec.mp4?token=gk8t4I9xmF0O_5wWr6cr5IGh2VwzmzUSkIAoGao2LoQOwEKFzRahvSh6O8m93hWxftpvhGfLTbaJeg294kRAKs7bopXeSBc-EZuUfw4kzTvM2dFzU_Spxk12v94JO35WeuZUd9ql-Ek7aT5cGXuASPyqOyAasZH93vvEz_Ttz5q8oHlS4Nuxpf4rpaVVpxzujjSYPS5I9su6wlCNbPK2P75JlSmL0TmT5zz-cOUGeWRpNLIbANwkDmw4IpNBwsMXLNXAIg0pSxDMcdvzuiuvr7MCOymfjnPTrPZiCM1ejEbiH56i6SIz_EIIhHry6AozYIyWNk6j8DnMXE8oDHCXIqtBkAeFks4us8-kGLJ37griOcS_h0Xkmb6jCeENBgmarHqPez2clATPd1hSpK9hXKAjhcRFZUqDWcHqq-30H4qmwYMQe_g_CAOuQwkEQQXXTOV3XAW1nucz1E6xV0MEAmzGHOXy7Qbm5YWwmvXH_2WlTnDEjW9Xadxr681C9m5Q5HExXoAa1eAJP1VcrKSZvVJ-oDczhj08ixgYTqShH5wRmmwBq86stG2hO0oDf-BUlji6Y4WOObDPiwJZyyiKpRd86mJO4CSFlHsJB7kUn_pzz6_Ufy5X85j55qoAC3Fs1J33xNZ7KaEl3djO2APcVEsiI9bPMzBPaLFLKqD5aE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59106dd8ec.mp4?token=gk8t4I9xmF0O_5wWr6cr5IGh2VwzmzUSkIAoGao2LoQOwEKFzRahvSh6O8m93hWxftpvhGfLTbaJeg294kRAKs7bopXeSBc-EZuUfw4kzTvM2dFzU_Spxk12v94JO35WeuZUd9ql-Ek7aT5cGXuASPyqOyAasZH93vvEz_Ttz5q8oHlS4Nuxpf4rpaVVpxzujjSYPS5I9su6wlCNbPK2P75JlSmL0TmT5zz-cOUGeWRpNLIbANwkDmw4IpNBwsMXLNXAIg0pSxDMcdvzuiuvr7MCOymfjnPTrPZiCM1ejEbiH56i6SIz_EIIhHry6AozYIyWNk6j8DnMXE8oDHCXIqtBkAeFks4us8-kGLJ37griOcS_h0Xkmb6jCeENBgmarHqPez2clATPd1hSpK9hXKAjhcRFZUqDWcHqq-30H4qmwYMQe_g_CAOuQwkEQQXXTOV3XAW1nucz1E6xV0MEAmzGHOXy7Qbm5YWwmvXH_2WlTnDEjW9Xadxr681C9m5Q5HExXoAa1eAJP1VcrKSZvVJ-oDczhj08ixgYTqShH5wRmmwBq86stG2hO0oDf-BUlji6Y4WOObDPiwJZyyiKpRd86mJO4CSFlHsJB7kUn_pzz6_Ufy5X85j55qoAC3Fs1J33xNZ7KaEl3djO2APcVEsiI9bPMzBPaLFLKqD5aE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صحبت‌های عجیب و وایرال شده امیرمحمد زند درباره تفاوت زنان ایرانی و خارجی که در فضای مجازی موافقان و مخالفان خاص خودشو داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106126" target="_blank">📅 17:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8dcdf837b.mp4?token=bDqZHhN_VGkaSfZuLVyccQ7Kg6S7XAhnUKhtGJmMBduWYyGfLYHkk9uhgxq2lp3ZMcOf0JwzaB0veCZmxMbN8HiTWk7XkYpW11FxaU-molRc09QttF9hrFfT0Ue7-F5YB0WH8PpBCvYfxigtW_4jH2GOVIgWmZTknZDWwuKrcNJOU30FWR9Gym0T3yTyJYJGtrTlBTtrRqFnn2k-P-WcKDXiIzWc7ZgCaEqZPTalsEKcj8AK17THEVp8I-v50F_6iuV5emfqQAXzeaM6OIZdm7zc4nuPzKYlFlWWM5Kuj0qGsCqmSfpdVDAVo6miX_GHOUVQ7zpq-MWGsV3fJZzRohetc-027YWUKOGuxTxyPFG_criuk6eeI-Xyv2wRzhNAkbbD8rH51D3PP9dO9VnXawREq4uHrMsTKRc1OyoD7fBThQ8S3n5GSooyfwGyUJ59aBG1bJColODgsIWN1w6dU4DwE-1_av45VxQW8PVjiRuWy1UfPQHplR-E8GlgsIAz2SMdjIT5ya0HmIGhe3FKWD39TU10B48FUWkZuCEItiSMdeFWYX3xZInWFk3cDXSCj7A__Pe7tL1gVdpaKM-UwEo3PpSdgcL2NeDJT2YeXI-2C7OFszWKmJUaO09qE76dyMm1d84VV3F2yxXafFBAuPrpXf41pWI8GDUW_9KPCj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8dcdf837b.mp4?token=bDqZHhN_VGkaSfZuLVyccQ7Kg6S7XAhnUKhtGJmMBduWYyGfLYHkk9uhgxq2lp3ZMcOf0JwzaB0veCZmxMbN8HiTWk7XkYpW11FxaU-molRc09QttF9hrFfT0Ue7-F5YB0WH8PpBCvYfxigtW_4jH2GOVIgWmZTknZDWwuKrcNJOU30FWR9Gym0T3yTyJYJGtrTlBTtrRqFnn2k-P-WcKDXiIzWc7ZgCaEqZPTalsEKcj8AK17THEVp8I-v50F_6iuV5emfqQAXzeaM6OIZdm7zc4nuPzKYlFlWWM5Kuj0qGsCqmSfpdVDAVo6miX_GHOUVQ7zpq-MWGsV3fJZzRohetc-027YWUKOGuxTxyPFG_criuk6eeI-Xyv2wRzhNAkbbD8rH51D3PP9dO9VnXawREq4uHrMsTKRc1OyoD7fBThQ8S3n5GSooyfwGyUJ59aBG1bJColODgsIWN1w6dU4DwE-1_av45VxQW8PVjiRuWy1UfPQHplR-E8GlgsIAz2SMdjIT5ya0HmIGhe3FKWD39TU10B48FUWkZuCEItiSMdeFWYX3xZInWFk3cDXSCj7A__Pe7tL1gVdpaKM-UwEo3PpSdgcL2NeDJT2YeXI-2C7OFszWKmJUaO09qE76dyMm1d84VV3F2yxXafFBAuPrpXf41pWI8GDUW_9KPCj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
علیرضا مرزبان مربی سابق سپاهان: اگر بجای خداداد عزیزی شخص دیگری بود، قطعا محرومیت سنگینی برایش لحاظ میشد. عزیزی دارای مصونیت از سوی حکومت است و در رای کمیته انضباطی نیز همین موضوع مشهود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106125" target="_blank">📅 16:55 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
