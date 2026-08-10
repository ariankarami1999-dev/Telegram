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
<img src="https://cdn5.telesco.pe/file/ZEzTZQGvM9NxmsM2Qm5055YaR0sFNFYwMoiiUsJvzvmx5b_EBeMtBCyLRd9pd7a7QlhG-y3DWv5avILRclvKBuXpkYlfaHt_YIdDX_2hed_qDe_nOQqq9zjc8MmKn4fza_7sRwhgiBP-Oou3vHFvmK6QDjxn8349LS0k4bV38JQEei1uV1qGe2zWEv5_Cjbra9isfC7AgyXv_stE_O0gCjlZbqSMrt9dB-LR02Yl87mx3dGwP1WF_XA8sLB5Rc5zctH8JjI5p0t3Y8pH5jnYcO85Hantv_s4c34q6aRKYNNQSvxZazOU8b-WfxYFJxGSXZBnpajlgrKaCi4ATdwqQw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 479K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 16:17:14</div>
<hr>

<div class="tg-post" id="msg-103254">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇪🇸
Xavi and Iniesta
🆚
Italy
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/Futball180TV/103254" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103253">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a709379c25.mp4?token=V3Fe51frv7DMPoCqc5Lsbi8waB6N8RLe7GRewYuGaIbIxSq9azlaNIUDaLvfpkXF-4Rh7FCLvotPpTEOavwOWK4Shsr94PfRHWq70s2LroOgAuCkpdr2VyRamt-Eq27Uaqw9sYYxLQ1o0Vhv5STb03KJDZxd8AXdi9SS3uAix7qJovyd-4eVhq77ALiJjIRkUZb0H8JbCM7D2i-5dfYcATRICoXdqrqwaKMnfbqv0PJtpmQYWrQgnOTm9MiMHatKcWjbgSoiJ6PhKU7vYrcZRI2MLNYgI35n8UwAs9pFDQxgl-C30XefignLltXdiQ6fFZHGByOANvOlWytVZbXG6EvjWJ5u6MPIYDAbhFfMTLKImgH950mJsEpnBIue1tCjwEqcaimdllE3691or8YC25hPHV2ypkNKtYhd7giMkWCeBZxnGJ8dpg2azQMtTkYWMaND7UuGz8QHH7DYUHdwVZ4EEQOXFZrw4QSDCfv42YtuSlTYDR1j4SL-1PAbtqQes4AiU0ZalXkmSolSexzh2FH-1L9muRyvOKltiIZg75jg1TtbK0YzbF7kKiZlEiSqbKIbIGMKpBRP8W_kz4I6h5ucUIHyoUbZO7NmfjzF4_pwTkM-ZzRXH-Hf-MaD_zGNxeqEaXV1UkXCmm6qSRurOKZjDeGaj5zsy0UMuD85614" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a709379c25.mp4?token=V3Fe51frv7DMPoCqc5Lsbi8waB6N8RLe7GRewYuGaIbIxSq9azlaNIUDaLvfpkXF-4Rh7FCLvotPpTEOavwOWK4Shsr94PfRHWq70s2LroOgAuCkpdr2VyRamt-Eq27Uaqw9sYYxLQ1o0Vhv5STb03KJDZxd8AXdi9SS3uAix7qJovyd-4eVhq77ALiJjIRkUZb0H8JbCM7D2i-5dfYcATRICoXdqrqwaKMnfbqv0PJtpmQYWrQgnOTm9MiMHatKcWjbgSoiJ6PhKU7vYrcZRI2MLNYgI35n8UwAs9pFDQxgl-C30XefignLltXdiQ6fFZHGByOANvOlWytVZbXG6EvjWJ5u6MPIYDAbhFfMTLKImgH950mJsEpnBIue1tCjwEqcaimdllE3691or8YC25hPHV2ypkNKtYhd7giMkWCeBZxnGJ8dpg2azQMtTkYWMaND7UuGz8QHH7DYUHdwVZ4EEQOXFZrw4QSDCfv42YtuSlTYDR1j4SL-1PAbtqQes4AiU0ZalXkmSolSexzh2FH-1L9muRyvOKltiIZg75jg1TtbK0YzbF7kKiZlEiSqbKIbIGMKpBRP8W_kz4I6h5ucUIHyoUbZO7NmfjzF4_pwTkM-ZzRXH-Hf-MaD_zGNxeqEaXV1UkXCmm6qSRurOKZjDeGaj5zsy0UMuD85614" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمه‌نهایی UCL2012 و بازی جذاب بارسا - چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/103253" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103252">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fbe5b387a.mp4?token=jgoWL3GUAHU-Bs9E0F4O-KOBEAsv2UD3uEmx4McvCG_bai0BAL8erdTPJGt1XChn8f-lxsFcebONqs8i1zfulqB6hySNMBGnWS8vk2ZCymoHz_mSX-8gjlYk1LExx4ksUQ9b3cyFSQegUBCnpMwO88HONOJfcpcopu3e-uku9cZ6NcsOfNVWk6bFFbWkNAvjdXkgwObPn_OxA0KOQh7Bir77_xvpZskgnswIJXEfLaKvt2pV14HOUa1uIvSbJh5QjdYlUTL4lnsT4MkOPd-JVZviasGmg1jdJVKdummoyCuTxRohecmsNXGQ74yckJSoJtP4cKew7ES2H92I3C4FEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fbe5b387a.mp4?token=jgoWL3GUAHU-Bs9E0F4O-KOBEAsv2UD3uEmx4McvCG_bai0BAL8erdTPJGt1XChn8f-lxsFcebONqs8i1zfulqB6hySNMBGnWS8vk2ZCymoHz_mSX-8gjlYk1LExx4ksUQ9b3cyFSQegUBCnpMwO88HONOJfcpcopu3e-uku9cZ6NcsOfNVWk6bFFbWkNAvjdXkgwObPn_OxA0KOQh7Bir77_xvpZskgnswIJXEfLaKvt2pV14HOUa1uIvSbJh5QjdYlUTL4lnsT4MkOPd-JVZviasGmg1jdJVKdummoyCuTxRohecmsNXGQ74yckJSoJtP4cKew7ES2H92I3C4FEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ادعای خنده‌دار وزیر ارتباطات: به اپراتورها هشدار دادم که هیچگونه ضریبی روی بسته‌های اینترنت قرار ندن و باهاشون برخورد میشه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/103252" target="_blank">📅 15:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103251">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8870e38c3.mp4?token=DMxdd2iNKehJAlRfIrfQ5VtClWvcCwsb9WNo5jIDwnWC0-80YuSDQru6f2KvugCFgFpdSxplNU3px5BiAo9R_KcOZl6QIOsRyrIcXe5Lq9XOuEa1-RAEm8DhmEMhg6xX1c7qjeI18KRgV36uLgbUtZ9JHRrZWyKzgwkaHCSmLogTvAootPOKZFkIJH7eRUmSi8JTiJr9It-qbHQiB8uEsWAOZZAB1cBM8_227EpQcgXUMQmYRIQ_tHKcE_tsNCaBk-tnMVSYajlIFh8rAyksc5kkXZPdGvi2nJ48YL3MRL-_cZTkYe2h6ZbyQF1XQm83DbrRnz1aeM9YJR_q41w20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8870e38c3.mp4?token=DMxdd2iNKehJAlRfIrfQ5VtClWvcCwsb9WNo5jIDwnWC0-80YuSDQru6f2KvugCFgFpdSxplNU3px5BiAo9R_KcOZl6QIOsRyrIcXe5Lq9XOuEa1-RAEm8DhmEMhg6xX1c7qjeI18KRgV36uLgbUtZ9JHRrZWyKzgwkaHCSmLogTvAootPOKZFkIJH7eRUmSi8JTiJr9It-qbHQiB8uEsWAOZZAB1cBM8_227EpQcgXUMQmYRIQ_tHKcE_tsNCaBk-tnMVSYajlIFh8rAyksc5kkXZPdGvi2nJ48YL3MRL-_cZTkYe2h6ZbyQF1XQm83DbrRnz1aeM9YJR_q41w20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
امباپه، گولر، مورینیو! این مثلث رو قبلا جایی ندیده بودیم؟
👀
🤔
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/Futball180TV/103251" target="_blank">📅 14:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103250">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsDMaGuhulaJpVe8x3c-Ehm0DDaJbJAPpD7wuTBKYfoJJNUj25-rr0QmW-MaW2on0TRwLmGjr4FYatqP8JZgzJhsNYYPD2Dz0JYE3eBkpRqMfDZZEZe0IKrMG7ttDs5Z3bkRTngBr0drd9dd_3dRiSY4HRAGwj7B8WgqNk3A5oA19JZU3ugKSKwZgS9g02V-pbBroJeZFeknkd2FUsC69YwNTYrdQOeYAl-oYCqKaD7JKu7UpNJlGpxUNmLjFElmX7ECYrby-fGjovNaW46scz5_44TQEXfYetjo72QTFUh3Q3LkaFsXlqlpKSmvXHfJKN0b4uNkOcIutrBpGTNWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
پس از تشکیل تیم ماهیگیری باشگاه استقلال، تیم دوچرخه‌سواری استقلال نیز افتتاح شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/103250" target="_blank">📅 14:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103249">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hrzau2RriuNtXxUEB_tsPFt9hn8uN_mXJM1GTJ99iJ6xKksn_h07ImIKrv-GQgyz1qtyBu5rO_asEj08cnJKt0Ozy6NfZaOP1tVzL9deLOIj5gIzzqVVjxOx_PIaZ2unlUULNXDEDlOR0tUILuuw8RUhuZHw_4-PssJOSNOZjbKCGD3MKGFRyhvEwChHZ6_fhyHqD6vTnJhYnAz-Dis_qUhr4pjL5xzhtZmGtzagfpNOrScJZ3Ynoz2tZkvV6qvSXDJ4cJtvKLhhyy7my8J3M8E4QQNuu-K9Vyi1FlW6YVgm8ENBVAj9OtNiBBwoj6PY4N7GjZ4F3s0ZiWbOP3UmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇫🇷
#فوووووری
از متئو مورتو: بارسا و پاریس برای فران‌تورس بر سر مبلغ ۵۰ میلیون یورو به توافق رسیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103249" target="_blank">📅 14:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103248">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/103248" target="_blank">📅 14:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103247">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b442857f8c.mp4?token=FoEQtjiIsZQFXCj4kdj9E-D0kG1ZLg4AH8KLI1SuNn7ZHOL4UOklk0mAPJ3jEXFJhKnt5zWvOokWilbSRPHY2lSWqXUpcZ5RPsvltRGiInHHnETpbwac-HZ5r3e8fmyeg1RmgrI75HjSeLMU6-u5I23UaYktGqK7JdaCkEFAcsZYVIKsMiZCeMAfyOh5JSa2EF4LMDloQ2ORjvTMUfowFfQNhScLOUThPQOvrxA64ifh5xxpravkq9sNbKp5Tps9UMiBgfpaMC_YocTPW54ohgh8pJ-I-M_By5zowZpxzsnd-Qin8k-SlzQrkjhQv0vIb6bL2CcQLbvSaYFl4u7fnHBVVO96jhuOvVroM7T08Yp_le4TU35hBj2D9pEmaHQXss2_d0EMfRr0pGjUGD9Il4ZY9lRrb9HSkAtHaxUC2Y_oWrE1bz6xm6B8NyaJbdW3KoSF1wJSY2aibRhY3J60lA0lIsLjsoayV51o0NOkbQF64YJAF8JoMRy-674FaOe04nBzJIkJmsaFn2DfrUpWc5nj3lE3LocFrpI2HorPdtcmI6Ie2iDImqR_ZTaMuE_en5W_PjmzyKxQFq8hPL3wKuMfvjzfR0mSBrEblnGXhwcJrBsgSEeimHgtSIoAZlbnceBfenuC86ieszCc_1-6gkllRjOL_SE54Jbw3vETLao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b442857f8c.mp4?token=FoEQtjiIsZQFXCj4kdj9E-D0kG1ZLg4AH8KLI1SuNn7ZHOL4UOklk0mAPJ3jEXFJhKnt5zWvOokWilbSRPHY2lSWqXUpcZ5RPsvltRGiInHHnETpbwac-HZ5r3e8fmyeg1RmgrI75HjSeLMU6-u5I23UaYktGqK7JdaCkEFAcsZYVIKsMiZCeMAfyOh5JSa2EF4LMDloQ2ORjvTMUfowFfQNhScLOUThPQOvrxA64ifh5xxpravkq9sNbKp5Tps9UMiBgfpaMC_YocTPW54ohgh8pJ-I-M_By5zowZpxzsnd-Qin8k-SlzQrkjhQv0vIb6bL2CcQLbvSaYFl4u7fnHBVVO96jhuOvVroM7T08Yp_le4TU35hBj2D9pEmaHQXss2_d0EMfRr0pGjUGD9Il4ZY9lRrb9HSkAtHaxUC2Y_oWrE1bz6xm6B8NyaJbdW3KoSF1wJSY2aibRhY3J60lA0lIsLjsoayV51o0NOkbQF64YJAF8JoMRy-674FaOe04nBzJIkJmsaFn2DfrUpWc5nj3lE3LocFrpI2HorPdtcmI6Ie2iDImqR_ZTaMuE_en5W_PjmzyKxQFq8hPL3wKuMfvjzfR0mSBrEblnGXhwcJrBsgSEeimHgtSIoAZlbnceBfenuC86ieszCc_1-6gkllRjOL_SE54Jbw3vETLao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🐐
برخی از گل‌های کاشته تماشایی لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/103247" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103245">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMUsRe6Ic5A_7YdWA5ukDllkeHokK2qZMrWcmvv-KjuncbJvQsxFvJT3XFeuxoOZ7S0lxvpkPQDRmx4K_UqDFplZPLb3fbU4-hMLrSUP69_axvnFhjRmpL_wohMkbtJ7VqgiYT7jJ0vSBifN7Kxof97_cmUzEAZFWBgWXIymo7YPPKjOY7o6XyStQoZ3XrRPefgxHJU9uDmM8v8ESMR9vS_HIVq65OV9Fi-3ZUgrv04s_6RbwjDC7JzkSNdXNqXmjNyPEtFebdYiSfDvMrWGL4MhX0RbgyMVWEZcR8GD-T-pUjDZ8lxlTNA_Zp1j3xD8kHUWRiL1XVXILP5qz9pExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkoK-Y6cWbpHwDwtCAnw5lkcvvxpzksRhtfiVoJl5h1obAFkRU55pm6KP0wgGcutswl5EWM791g-CtaXru2U-q3sov3blAAnmsFTrVOQbq5uokf-kDu2At-LZU-jQrd9dTwfesGL3LC-rb97OekonavzarFAkztNlgaDlGnfr4ld-ZTVjOjr0XJT5GLSIIA4_aSDY56fc9z2PIhaKyWIXtdO0uIzwLNI-6c4ZcmC8wGn5Q6ZV8CajLga_w5o_SGCEkvcfLrtm2E2Q6w4Yo9_ndhbTI7YYyP7SQdnhGmhKkbVDElDBjMQndqQ0qSirw9Ee7XbT8JxM-hihu7kDCQ-4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⚪️
تمرینات امروز رئال مادرید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/103245" target="_blank">📅 13:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103244">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e730d0e84.mp4?token=KRhk3QuRth3dhVTrDrinJ06y34GAyNL3HqAXXDPXrTMZZw2Why7cVmDTp7CQjgLzw2PJ5za9x7AdIVlnZRgvk9ENH9Op37muUCwWaD9xK_Gb7py60NfPIw1JUrW5aeL-Oay4f2ooErXfI5w-2Nl-msoxh9J3nZvP132lBa3evYZkPQcMjED63-yga7l9uuzAQJwjMx3lhhT4nBDeq7-ASZ49S53Gnz6sdBbEa6YQOGP5lflJAbFJNX4Xgj3LhKHLSiDGpjFr9zBCkOg0Dsw3VRZ2mi8j1yad-dqwjRmuwzgK3YhYYGN81qS-ELouTg2hcs1yrS9hAUDolxAXrcRdrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e730d0e84.mp4?token=KRhk3QuRth3dhVTrDrinJ06y34GAyNL3HqAXXDPXrTMZZw2Why7cVmDTp7CQjgLzw2PJ5za9x7AdIVlnZRgvk9ENH9Op37muUCwWaD9xK_Gb7py60NfPIw1JUrW5aeL-Oay4f2ooErXfI5w-2Nl-msoxh9J3nZvP132lBa3evYZkPQcMjED63-yga7l9uuzAQJwjMx3lhhT4nBDeq7-ASZ49S53Gnz6sdBbEa6YQOGP5lflJAbFJNX4Xgj3LhKHLSiDGpjFr9zBCkOg0Dsw3VRZ2mi8j1yad-dqwjRmuwzgK3YhYYGN81qS-ELouTg2hcs1yrS9hAUDolxAXrcRdrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
با موسیالا هر غیرممکنی به راحتی ممکن میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103244" target="_blank">📅 13:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103243">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f008e3e11.mp4?token=k9AHxA4EiwqeIaN0q1kUbnpSNI1FkGeiXMKytEpzWxQUu2rnVbimKqbyKhpKw33FQ6bdErreJ3sUjKZSWfDW5EUw2Xonxk0oiC8XYkGumWAWsQjudF2JALxRsI1lHRkkTKVG39L8nisNSHGlR2G5VyikpZKC05oO6j-j-WNZv0uvPbdT6r8euePBpREKD4Nlh8GTvg8S2ca5WF8Q7c3AtssLb_74nkvyuiNavqdGePus0UWU6l-8WzOSD2sgU2cMdwQBxtocfWQhJS3dINqp-WOBbRFY0ulLJJ2cVEeaO4fqMy3OXLERlRl7LAZ42dc3ToavTp0RjV3TSy9tSVn9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f008e3e11.mp4?token=k9AHxA4EiwqeIaN0q1kUbnpSNI1FkGeiXMKytEpzWxQUu2rnVbimKqbyKhpKw33FQ6bdErreJ3sUjKZSWfDW5EUw2Xonxk0oiC8XYkGumWAWsQjudF2JALxRsI1lHRkkTKVG39L8nisNSHGlR2G5VyikpZKC05oO6j-j-WNZv0uvPbdT6r8euePBpREKD4Nlh8GTvg8S2ca5WF8Q7c3AtssLb_74nkvyuiNavqdGePus0UWU6l-8WzOSD2sgU2cMdwQBxtocfWQhJS3dINqp-WOBbRFY0ulLJJ2cVEeaO4fqMy3OXLERlRl7LAZ42dc3ToavTp0RjV3TSy9tSVn9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
وقتی گواردیولا به جای بازی پاریس-بایرن، دسته سوم انگلیس رو نگاه کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/103243" target="_blank">📅 13:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103242">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa14f9fec.mp4?token=VOWbcLBpUBW3wfD-3uFPapkO3g2qAWr1N248pfjnAzqRnuWRToNxWLLOmAXkYqPL0ILRaeEfeVkUHp-dTOEXUgZthIZ92M2sFGkbxu3ZUincPg6V9RVSp7ZNgX_2oQohh5TVVJY1cwxndTc0BtUW5DCbLJ1fc1ZWjIAXRQlMOXnvkNZ5gWkiAG0-InvltQz_hz-XZpAUdihCzpXOeuHzUch85euMs5yGKTqiCOlLRp3mdEDoMyB_MP4b8X5NB4lC6DS2f8ZHvjFculyWq1tc3okT_ahQj_KsBDHH7uhDOQSdd615NdtTLIekHG5F7bkUqnDaM6KCqNGrfpT0df_TClFr-WYBGIenV73DIrrZZNq8tRvHcFPpUOUxYjpf7RUxBTNKIEOm8m8TvHWTiB5KsnrWqzgMud17rRZHTrl1wRnI7jk8iiYkSVA3TVScG9xcJJ5o-dU576yesM6MTamrJ-S0yRqcP3o7q0zQbLh6WWgnp3KLwjID5N2BYeZd8hutPd-q3AiqvUYguTT04BMHwL7wiSrrvvSW0RnQ35dsE1Ogh9brYvb-HchXPR50jviaeuS8BhAjrn9ioKF2fHcU8qc4FguZdrq4kyCW_QaNJxgFGAancEUZf5m52Sm-7-JsVcW7wUNt-XS4L-sGUN3lVXgt8zwmKacJ3IpYYd20Jwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa14f9fec.mp4?token=VOWbcLBpUBW3wfD-3uFPapkO3g2qAWr1N248pfjnAzqRnuWRToNxWLLOmAXkYqPL0ILRaeEfeVkUHp-dTOEXUgZthIZ92M2sFGkbxu3ZUincPg6V9RVSp7ZNgX_2oQohh5TVVJY1cwxndTc0BtUW5DCbLJ1fc1ZWjIAXRQlMOXnvkNZ5gWkiAG0-InvltQz_hz-XZpAUdihCzpXOeuHzUch85euMs5yGKTqiCOlLRp3mdEDoMyB_MP4b8X5NB4lC6DS2f8ZHvjFculyWq1tc3okT_ahQj_KsBDHH7uhDOQSdd615NdtTLIekHG5F7bkUqnDaM6KCqNGrfpT0df_TClFr-WYBGIenV73DIrrZZNq8tRvHcFPpUOUxYjpf7RUxBTNKIEOm8m8TvHWTiB5KsnrWqzgMud17rRZHTrl1wRnI7jk8iiYkSVA3TVScG9xcJJ5o-dU576yesM6MTamrJ-S0yRqcP3o7q0zQbLh6WWgnp3KLwjID5N2BYeZd8hutPd-q3AiqvUYguTT04BMHwL7wiSrrvvSW0RnQ35dsE1Ogh9brYvb-HchXPR50jviaeuS8BhAjrn9ioKF2fHcU8qc4FguZdrq4kyCW_QaNJxgFGAancEUZf5m52Sm-7-JsVcW7wUNt-XS4L-sGUN3lVXgt8zwmKacJ3IpYYd20Jwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
برخی از سریع ترین گل های تاریخ فوتبال
⚽
🙌🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103242" target="_blank">📅 12:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103239">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ullyv4QXWUyfFa3N2kI0QHz5bqEXDc5yn-hNNplb_Xg2X1Q92gGY8NU0QMkyoNoaahj2wQEbgMvbjzvr_g-w3MlScGreHffFcwYEwkG4dgoR-ovElpym1j3X2wkwk761FWeyBCCMvu-ivrmjX08Sdy2kI3afKKJI-pIBkm15Zk97vq_M6yx7I0kCjQYoYhhLXWCi8RQZcjPxlvNX5IftYA67eX8QofZ7CYYAai170rI_vjyzoDGm-cPnzJo_cv5_KuZmB4DvWqVzqVBDjEuvpD_Hz4sreRd3j_9jXBVpaIw42IQQdBCiG9WBil1zLqmPZezCf-PiBqCTrQAksYGu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THhX7w6C0IjrubHycIgtdJYZ7q788K5-FKVV4NIrWxdRaPT0zLKtm9nMDqftareYjXpB7wRtFNdNF9AL99lFhiPoa2dFY1WlXkUjWfPACUSCRcocyk70GWQaG-D14xQ4rSAxJ0bKtqWuNq_s9D9B1PnG9GyglPxfZtkSu0NPDFUk3ppAIWXrDXfgwk2RNUKsYHq9XJvp266rp-EVCbQnli3f1bAPeklfNWfT3gOwC3ceQIYO8j1IIClNnMH7KqcFq7xpxSQNfZ3tQ1BehHoCmy1b7FXfsuJZia_FotDBP8mPwrTNCrUgQLHrEkNP453yQ_mEsJcjKCr5R6gOqrU3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAZk6WEXLpVMlO6vb-FRP-kPmNkm6HW16GDFOMybvRtu8NXXyUKhKpf33mdzR56KvABg_7EWL0z4USp2y7aMixxRpm7fOOLyiEzwnf1sfUtN5edwzEwxbTLgbtNoea1aToGS-olQnv-6CRMawtjXgL6HZ2QrhKUqyEL6k9IEVK7aOybOHtZ-b-WTPn2fMBl2O_zOhlJ3emGZrFFRAWwq1dzJ64GgwvuDv_zwhQHFP4AWKTRk3RZT9s5Bt6zIo5EutIHwTEPL7wKa2vl9y3HIwFkNjLs6M9rSxoyu7HjWe6oukGbsPOJJCuA2QHe9SAKitA1yH2hszzgwgIWM-orXMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امباپه ، کوناته و کوکوریا بعد از پشت سر گذاشتن تعطیلات تو تست پزشکی رئال شرکت کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103239" target="_blank">📅 12:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103238">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4861e800.mp4?token=M7bIZFWV6Z6zSkBEWjQkzlTrl4M3K5s-d9Hm6NFw14-rH2GaWNgqvtjzenEWj4U75ra2qlCCjV-liAToDRCtTuWqOf2YBd4UHAXTt5bEMwMkjPH80wOZxAPvKanHCpfwuWFrdOrrUSic0MNNpfaUeZQbOSeYTkuFnzc3eC8BeVSLpJIpsmVUt0oOH5cIa60mjiO9KIpolsNjOWAwmrhqnW6XS8PLVY66aA-nMS-gywj690Jl4lbpzr2U8Y3PpTQXG9iWvuLuoEK19mA6gsS-HoxQaQD_FQKJa-EmZhqawOcP4vtjpW4YNLwn-h53oyKoPKMOlnebx6tUtoAxeKB-Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4861e800.mp4?token=M7bIZFWV6Z6zSkBEWjQkzlTrl4M3K5s-d9Hm6NFw14-rH2GaWNgqvtjzenEWj4U75ra2qlCCjV-liAToDRCtTuWqOf2YBd4UHAXTt5bEMwMkjPH80wOZxAPvKanHCpfwuWFrdOrrUSic0MNNpfaUeZQbOSeYTkuFnzc3eC8BeVSLpJIpsmVUt0oOH5cIa60mjiO9KIpolsNjOWAwmrhqnW6XS8PLVY66aA-nMS-gywj690Jl4lbpzr2U8Y3PpTQXG9iWvuLuoEK19mA6gsS-HoxQaQD_FQKJa-EmZhqawOcP4vtjpW4YNLwn-h53oyKoPKMOlnebx6tUtoAxeKB-Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
علی‌فتح‌الله‌زاده: مسی بهم گفته منیرالحدادی بهترین بازیکنی است که با او همبازی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103238" target="_blank">📅 12:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103237">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccEVuyVkBw2sqUZRLUOTifU7EAlLE6CWmALI07_nKwRRvxyIIG-GACsSxbY6UCNP5cQSq_TfEvT9YqtFJ4tBWLWRRRnUGYGX0L5RiMcCggW3bPQo_tT6Jm424j0khk6yVWdw4JeDIL_AE99AaLhFvWqoyeu4zwEs-gQnn0V930W0ATYenViI009G3mtrwUikWeQmWSGmSs4zdiuZwOkFGU5zha2whNBLPQgxG1cusTK399VE5cEdpNNAK1fDFbqJF48IjbCwvF_lmnwBycoJN4CBTmg5ZoTUtJi18oIH9Q8Jwd1TBBz0jhaUi6Rq04c85yY1vdL2BmNgcnnyTITWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
بن جیکوبز | یوفا، کونکاکاف و ای‌اف‌سی نامه‌ای مشترک به فیفا ارسال کردن و خواستار یک بازبینی مستقل دربارهٔ FIFA Forward Enterprise یا همون برنامه اینفانتینو برای فروش سهام جام جهانی شدن.
نامه که توسط چفرین، شیخ سلمان و مونتاگلیانی امضا شده تاکید میکنه که اعتماد به‌واسطهٔ فریب از بین رفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/103237" target="_blank">📅 11:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103236">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82a19a1124.mp4?token=H7y7dmJuKNpMwTxe3PqJy22BqL5RIVOwsExTBA0H0N4N3HRxecm1czrmJ2ss02stxLKWK1BEn83hkitIa_nx2tC_qrYLDun5wDJ0sx2LLf6mW3siK7MKG_uSxroGj53wTyMIMeshRhDfcLrU-H2n1dNZ1NXtCmuNB94sp-KKSPNggic8EDKDSx0BwIHNBjR5Sao71YgAnBqbQfzXmWmQnt5elkcxaX-CTVHBSK0UvfMAxAVoGHOYSP9ORdb_aszPMwW22UJ6U32kvAdvm79DjNWkhSM3OwW-E3E4RgxvttRiOPcbH-knr1pBb-bOcmnbdtbO7g1FxGUzAYnTxrAI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82a19a1124.mp4?token=H7y7dmJuKNpMwTxe3PqJy22BqL5RIVOwsExTBA0H0N4N3HRxecm1czrmJ2ss02stxLKWK1BEn83hkitIa_nx2tC_qrYLDun5wDJ0sx2LLf6mW3siK7MKG_uSxroGj53wTyMIMeshRhDfcLrU-H2n1dNZ1NXtCmuNB94sp-KKSPNggic8EDKDSx0BwIHNBjR5Sao71YgAnBqbQfzXmWmQnt5elkcxaX-CTVHBSK0UvfMAxAVoGHOYSP9ORdb_aszPMwW22UJ6U32kvAdvm79DjNWkhSM3OwW-E3E4RgxvttRiOPcbH-knr1pBb-bOcmnbdtbO7g1FxGUzAYnTxrAI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
محبوبیت‌ دیدنی لئاندرو پاردس در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103236" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103235">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=Q4Dgs0uH7P-4q6tYyaH0zzyBMJH9gWl3k5x4oy2zROMrQufRxB8EHIsQNNkk2deyXla1PfDsF8zIbjGihlwIR6vTPWCs_fc3lwga9-6rUKYXjsWbZ0mpIUWTwfPoRrkTyFHKtqipQzWrduoLt-rZ9OwVCnOWYsFmMD-jti_LpKPm3C-13ImY-ad8TeXao61j_CaWj9DJMWIsUBAkbAZNrjkqm6TchZn-C6Zafu1AI1IXgyvcZUhs9_QymiFOvFj992pNE5uR2Z9AGr_iFRGEzcJuegONzGGokOT-3zEmBGFzTZHBQAS_4U5UVUHcAwqeedcoMZqpKIP4guXCWqy2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=Q4Dgs0uH7P-4q6tYyaH0zzyBMJH9gWl3k5x4oy2zROMrQufRxB8EHIsQNNkk2deyXla1PfDsF8zIbjGihlwIR6vTPWCs_fc3lwga9-6rUKYXjsWbZ0mpIUWTwfPoRrkTyFHKtqipQzWrduoLt-rZ9OwVCnOWYsFmMD-jti_LpKPm3C-13ImY-ad8TeXao61j_CaWj9DJMWIsUBAkbAZNrjkqm6TchZn-C6Zafu1AI1IXgyvcZUhs9_QymiFOvFj992pNE5uR2Z9AGr_iFRGEzcJuegONzGGokOT-3zEmBGFzTZHBQAS_4U5UVUHcAwqeedcoMZqpKIP4guXCWqy2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
🎙
داریوش: شجاعیان: شفر قبل دربی گفت اگر پنالتی شد فرشید بزند. رحمتی به منشا گفت بیرانوند تو را می‌شناسد و نذاشت پنالتی بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103235" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103234">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=lxJOR1wCjuypSQDzeYzWlQD4BEhpIbInpwx4vCPoNM_ZDjghl0VjORLyuAu2DNX-29EBIswNp9030xf9UxqEIICgNo6wP8YbfxVOjm73GuCMB6a6RRUz2OJHV9yiwgTWbWRzqbFWKFvp_I0JPRntNRoraTFf71w8XK2hZUxqnSt-dbHgzKF1ztRGIfuYVGrdc4oFTo5GP2uSEjkZUiTAgDM8o4x6hJ9dZbLJ2_CDngl-w59u5Yi2L2Kv0NoeUAS65HPcU-qSomRVgTmrtJd4mlSE8q3v31hiIEv_PFKXAnaEq-rctwRbo2jsn_HxTUWvCLPd_ekkulLwIdUpoEClYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=lxJOR1wCjuypSQDzeYzWlQD4BEhpIbInpwx4vCPoNM_ZDjghl0VjORLyuAu2DNX-29EBIswNp9030xf9UxqEIICgNo6wP8YbfxVOjm73GuCMB6a6RRUz2OJHV9yiwgTWbWRzqbFWKFvp_I0JPRntNRoraTFf71w8XK2hZUxqnSt-dbHgzKF1ztRGIfuYVGrdc4oFTo5GP2uSEjkZUiTAgDM8o4x6hJ9dZbLJ2_CDngl-w59u5Yi2L2Kv0NoeUAS65HPcU-qSomRVgTmrtJd4mlSE8q3v31hiIEv_PFKXAnaEq-rctwRbo2jsn_HxTUWvCLPd_ekkulLwIdUpoEClYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین‌بازی ضعیف دومفریس در‌ رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103234" target="_blank">📅 11:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103233">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7ItAT4X3scIY0vtTL5143FlnKR3muQrco1-1csXic5lbXbmERU9crH0x2H88538DeTHWbJa5JrObu65cCGePHqkanjK03F3T0Yg4vHw1Q3HK_bHlYBBzsa9uc4eCj9iBZ4ui6xc_Susaj72lOcECuQ5eD-bcuC657aaAW7GtJoomHlSGtqv9PbwhmNHxhH-JUk4plenCfIS_g-eg40RCZ6f6CLnRot7iPcWD1R9GAknEwbRNJWKWXjbh0qjgvu75OAQT5MaaB78xs-ftxijE_dJ8ELJwDta1maTDG0OqHQKvJLPmNsq3YaP0Q6_PDMWVaslv32H3bk8JR91VUkI5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
5 سال پیش در چنین روزی؛ لیونل مسی اسطوره فوتبال در انتقالی پشم ریزون به PSG پیوست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103233" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103232">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuSQIds7s9NDbJQ9bcUpyRikGuHyGd7CsiwD_SFbF2zUcitDLXj9pXW7EFnvUu9nXml3bxddmRMygU2DR0pSPOvhZACjGkS4ISxEIzGroG6vzi4NDQZ82ZCe52RfeXnFDO1ewM7viOrY3DVfN-60_Ovxreo6zBjlewc6Ujy2J6NHMr08Cbnqg74Ig1i7RYNtiIy7QvgAylVNLBlJrErN4EHaEoIg6enmPNic7TL0v8avS11x5IP19MBgiz14G8o0hKjg5LBdJ7wk6LQ4eIzHv97tGkuDZK1rxDZUxIzDFdrdXE_XpeCfXWI1IhUJ0_CKMvMjsbXswy3WgU8mDAuKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
😳
جرارد رومرو خبرنگار بارسایی امروز کسخل شده سر صبح داره دوربین‌های سطح شهر مادرید رو بررسی میکنه تا ببینه آلوارز کی رد میشه و کجا قراره بره
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103232" target="_blank">📅 10:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103231">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtY0n_BXsEm3MvxevMgJ3mp8-suYPSXzUGTpyfCds3aVZPb0IPSjw4KCScUUN5whgibriOiTI9qbWNBa8g870IuaQvWBpG0M2o0TuBLw08y-X9IfIak5YX5YyMtJlRBO8TVYMWhJzhXr2jLnQ4PyPHqry6fGhijEBl4bTM9gRARC-sAxCO9zqpP5BkhnN-p3zGZ5l8Gq9uzVXXl049xz1SdPsPimLZwQqZUKXbIDGpd0rXVQKd-Ub_CbpCXvA32HZDzbzt4NAA2a8zIPc1syFMAeG1_p4qKympiMxZg7OKvHQuH-yJyPBnAWsIDl9I9IUZQk3ux1ZFVQ8h5cOwziVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: ایوب‌بوعدی ستاره تیم‌ملی مراکش با منچسترسیتی به توافق شخصی رسیده و مذاکرات با باشگاه لیل‌ در جریانه. بوعدی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103231" target="_blank">📅 10:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103230">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=iBa6U1S9oWFnMhW3r5iCH8c32MlUcM1Kujj2kIR-hEv4lNYBPtwUj4Rcwo20wM_pUP0hQ7mPXwYGSk9axp7t3bdeza5Ub4n9B1KwX85tz4F_WPl5ShAWSM1MLjsZiRGm1ofe0NZt5pTx4JcgflK6MClvBjoS-IKhqQfo1jSwxv2IKgD49pHuuFitgKnwYXS93UnZ5feoapqiCQkCZCxXkgqu3KZiBLSxKwgyIpKnAImas9lfjQF2UXRKE-QSR3DD7bl3KAWVZ23JWnrJd3ARyB62Afsl_Fy0wLYVDrDHTnIP4v6EIeAi_N-ME3domRJFAYpcnvFRuG09a4_JSS4yebs5W9Q04WcyrsC9_3m9oyzzkc7bStLvJQaj9n07BYEekgIjsESSI4kXw00tahaf5sh1p_24rxnzvdNNAkqb0A-QWlMz-Lnf1qCeV1b_roR8rvbuihmiX3X9CCoKM1s_jdFdQN2uTOvzjNpF7WfuIHSAoXuoe2CaBmosBhNQAPXDrMXiPv8fbJx2_Cc_yaMyZcRLV0Oq1ugh-LRrF6orHnF8EpaTHYmtiwhcX71xtSsihZqC6Dv57iqiYtw-vU1cimDI1cEQhoOjqNFLgwIn1Bv4FVabtdxmgPcrgxcC1xRafyC8qjrORsyTGtu2TudAvDPwgywtXafcMcoycZbLPL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=iBa6U1S9oWFnMhW3r5iCH8c32MlUcM1Kujj2kIR-hEv4lNYBPtwUj4Rcwo20wM_pUP0hQ7mPXwYGSk9axp7t3bdeza5Ub4n9B1KwX85tz4F_WPl5ShAWSM1MLjsZiRGm1ofe0NZt5pTx4JcgflK6MClvBjoS-IKhqQfo1jSwxv2IKgD49pHuuFitgKnwYXS93UnZ5feoapqiCQkCZCxXkgqu3KZiBLSxKwgyIpKnAImas9lfjQF2UXRKE-QSR3DD7bl3KAWVZ23JWnrJd3ARyB62Afsl_Fy0wLYVDrDHTnIP4v6EIeAi_N-ME3domRJFAYpcnvFRuG09a4_JSS4yebs5W9Q04WcyrsC9_3m9oyzzkc7bStLvJQaj9n07BYEekgIjsESSI4kXw00tahaf5sh1p_24rxnzvdNNAkqb0A-QWlMz-Lnf1qCeV1b_roR8rvbuihmiX3X9CCoKM1s_jdFdQN2uTOvzjNpF7WfuIHSAoXuoe2CaBmosBhNQAPXDrMXiPv8fbJx2_Cc_yaMyZcRLV0Oq1ugh-LRrF6orHnF8EpaTHYmtiwhcX71xtSsihZqC6Dv57iqiYtw-vU1cimDI1cEQhoOjqNFLgwIn1Bv4FVabtdxmgPcrgxcC1xRafyC8qjrORsyTGtu2TudAvDPwgywtXafcMcoycZbLPL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🏟️
آخرین وضعیت استادیوم آزادی تهران
✅
قرار است به‌جای دروازه‌هایی که به‌ صورت ثابت در دل چمن نصب می‌شدند، از تیر دروازه‌های سوکتی استفاده شود تا در مواقع لازم ؛ امکان نصب، تعویض سریع یا جمع‌آوری آن‌ها فراهم باشد. عمق محل نصب سوکت‌ها، بسته به مدل ، معمولاً حدود ۴۰ تا ۵۰ سانتی‌متر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/103230" target="_blank">📅 10:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103229">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3E7Fx3MB35Ubim0LOVN2qzQ657VJORaiq2NL28S2mSZcB6xO_2-2eMTm33teP7iCcFtMwud5Qk_TMhRutXuU0ss0k60s_GrYFxEFrkdzhPcWPY7mQjjpV9tiytgySthTAUXFEA770FICvmihWhZVlaUhVDxLWH-z33214o-Giz20-LOcjSjCtxbYu79eWXkzstj-UidYaGiCjMPZQEpXn2DLElEhZiH2vTdy_ZfJ0K9rBzzBlaxiGRDzGbnwcp5fDtgInxEs3yWNd1zsyjpTGidhdgkuSyUS6CVChIIIBBI8AaT2UTaZRwix_APCneIM8gi33_2O-g3Uu5pVB7MFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
آرسنال برای فروش زوبیمندی خواستار دریافت رقم ۹۰ میلیون یورو شده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103229" target="_blank">📅 10:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103228">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=vhpzo2ugisCaitgO0mNS26O0p5KZprfFF0eFfClZilsHTAmJWeUjiGxg0j8Oed5-wjx08j4wZv66su__bISUC4OrLgEliPszL2LjSIhHxs-jofGcoCEMAVOn-dppm9dWTj1LDJs18wP_ITQnmAPinG4Kdt1rXJUwctjdkx9u0eztLm8lZOGByO-xFdBS187fRJXojG2PcmdfdTeB112NVe564HfRssZFtPNQPnQn_P6iRXWZYAZ1u2-s_mS_A-k9cXH8Hx24ybIOv5yWX8UPphJKWkHg52ti5S_ihjihrb_KVXAE272iDcp4OigIitx6Yxvve4XKSD6z4ZkuyBLHCWVzPuJg2UpWsO_ehGdfRnQJMXqD1Zwoo3IojMSNTZocS2MrSA7exO204xFr016bnSzRtwZM_XK3C8JOsrS7K2neku1fyDT3xpHRxzkb2WZH0WLupVdpl26Ky-pHEJ-_YgeGpYtFBX00KCeAIDdaSj_BvxRER6bpnsHkMtc1JCnJk9uRLa24loX8xUzGUTaDwFuwfUZNuKNOkmXmSLVKjTnDnxlARc6Le6uzvCR3gQ9CtkBo6kDQnEvZyICGE3mYSgPJFuOo-mOqpfuGV-RhJ0t8dQfXf43V1e4W0GLfd8wnKkIZdb_jEGensYqIB6PlFnK9X0G-K0rdi-fYhRk1Wso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=vhpzo2ugisCaitgO0mNS26O0p5KZprfFF0eFfClZilsHTAmJWeUjiGxg0j8Oed5-wjx08j4wZv66su__bISUC4OrLgEliPszL2LjSIhHxs-jofGcoCEMAVOn-dppm9dWTj1LDJs18wP_ITQnmAPinG4Kdt1rXJUwctjdkx9u0eztLm8lZOGByO-xFdBS187fRJXojG2PcmdfdTeB112NVe564HfRssZFtPNQPnQn_P6iRXWZYAZ1u2-s_mS_A-k9cXH8Hx24ybIOv5yWX8UPphJKWkHg52ti5S_ihjihrb_KVXAE272iDcp4OigIitx6Yxvve4XKSD6z4ZkuyBLHCWVzPuJg2UpWsO_ehGdfRnQJMXqD1Zwoo3IojMSNTZocS2MrSA7exO204xFr016bnSzRtwZM_XK3C8JOsrS7K2neku1fyDT3xpHRxzkb2WZH0WLupVdpl26Ky-pHEJ-_YgeGpYtFBX00KCeAIDdaSj_BvxRER6bpnsHkMtc1JCnJk9uRLa24loX8xUzGUTaDwFuwfUZNuKNOkmXmSLVKjTnDnxlARc6Le6uzvCR3gQ9CtkBo6kDQnEvZyICGE3mYSgPJFuOo-mOqpfuGV-RhJ0t8dQfXf43V1e4W0GLfd8wnKkIZdb_jEGensYqIB6PlFnK9X0G-K0rdi-fYhRk1Wso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
شلیک‌های سهمگین سوبوسلای ستاره لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103228" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103227">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103227" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/103227" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103226">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TEsoMX3TDRfib-PIhcpq58pgX30KPLKeuNeMv1BObFm-FNpulD3wFZiAIrUPkjY_YT0W4V-dHmyOpkp4ny086GZBXrdvFU6kwyTlvlvgDg97dskg_efNUYXKbSVcT84WoGoBfIWnmlt16ddihPL8KpiERlEnX6LEynZHLAMCP190YgpYGNQncrgR_RpsD_DYcw3Vb0rMuc0VqDceO5TfT-0jLFw_iDgwB-a2MsMQlYw8fGNPHzXnkVn7rNpf7uxy0o763UcTBCREmMWzRl39gK5n6LAsd1DVyR1HXUDvqouvPyeQvpI1bSD1wlofNumoci8tmqgsta8Yar6rbEANUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=TEsoMX3TDRfib-PIhcpq58pgX30KPLKeuNeMv1BObFm-FNpulD3wFZiAIrUPkjY_YT0W4V-dHmyOpkp4ny086GZBXrdvFU6kwyTlvlvgDg97dskg_efNUYXKbSVcT84WoGoBfIWnmlt16ddihPL8KpiERlEnX6LEynZHLAMCP190YgpYGNQncrgR_RpsD_DYcw3Vb0rMuc0VqDceO5TfT-0jLFw_iDgwB-a2MsMQlYw8fGNPHzXnkVn7rNpf7uxy0o763UcTBCREmMWzRl39gK5n6LAsd1DVyR1HXUDvqouvPyeQvpI1bSD1wlofNumoci8tmqgsta8Yar6rbEANUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103226" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103225">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqfkDrF8WRGwr4QQ5yxZWthF1Ftsf5pxZrxXIfZ1wVsYouR7mV9UpsF1PDyhzW17dKl5MZNgxcJsIv-EnB2Ica0fH9mWN135SJ0l1ccFwrf-wIFIpBgMTfsGOYOXl3KxmONYPfQDV05KXGUnhG3wa-8GDUgPxn-kubBFQ1HemsfN5agDEjRoGhplTh57edPdKjn4MOlgQjzycHpo6i1lRzL7bOkNBlW8usUSKqzSaL9kk-Y1lpMng4_kaWuUQkJbMfIAUixocUU_6I8Qi2fLxDlbKUJJAuby6LDyMo1WNA0AcLu6HJRGgZrIb5Q-0Bk5Y4AwtYrqgfjGyseo2Whcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
مقایسه آمار فرنکی‌دی‌یونگ و رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103225" target="_blank">📅 09:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103224">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJIHAdALsxGa0XN7yYoyXOgN4gf3482RX4drsrHk0V36suknCXaF0sHRdldegRCfeBGaRJGVHBCyU4EbnlUK352L5fA4A0FDbF-iBOzV6j-G5gz7Qstju9AxOvLWz6Em-_PjhZwsUIlcdpkrEzLlkd8DPjuq9r7WEuOgYFD_qg6EzmCPSJn1m0Qh1slx9ogeVTxzguVLYDjxRxDI_pk_kb4LGM2NMkdezw9ebh4lVikRiDXuxrYtWzB4bZ4zIPSv0m1W0c8R4XXWgBEWlfRRJQPG-ERYh5GAnCrVLt_sxdgJ8XDH4oyimNczfxS0CM0C6Kr5rO3D6HRtJ5EDW_aEPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط هجومی فصل‌آینده الکلاسیکو
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103224" target="_blank">📅 09:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103223">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👀
🔥
برخی از گل‌های چیپ تاریخی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103223" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103222">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsRerGv4jJNIx6hPFSKOQn1LjXqWqTJWHA40fFFJn3bSI--rdlNFkNlXVRaLtG5A8I99ZOOsTNR3riLpNoBzPxyEPQmI0ZHGKaFKBJ9sLGA7WYlmbm4-vBSX_BCSE_JgAAy_SLZc9oxt8aR7Hi29dBqpaXyi3dPbp0K3s17CwxWd6jxGT0uLmfosqhvFtBT3r_uS4Wgbtm8sT_GLWMmZwk_JaF6UMvjWC6h3-LwHg8H9s-xOjzpsrkocTHkNA7N6x-x7529_p1gcn6q0chdj0V7VWr-JAeePgpTUrtIa5DYOZ9xW8JiJERqd4P383qUtWaWMB2Rx-4ER11-JS48bPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇩🇪
نشریه‌تایمز انگلیس: هری‌کین بزودی قرارداد خود را با بایرن‌مونیخ تا ۲۰۲۹ تمدید میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103222" target="_blank">📅 08:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103221">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-DufT3vobUjBpoPYXv--BtLkR111_4s6l_7sYjqHZHb2xFBQZTnxaRt1LBwKSVS4vc8UudAp1oP_pNaVMKCC-H-SZG6D56m-fpGN00YDaIW3Dp7JvCevRGKemlGf-ON_xnySu1vuolfW_Xvs6qLyF3tnXx4hCX2a0fGRHPnLOfWfGA1vHuwIwH675Q28acRlxZPVkkxkL3OogGNgcFSgwYbVCCP1Z7gvncY4gbd_8E_b9zI2mp-Tx9Tm-EhRq_qOmdYtbR9pnTekHvp5SjJwIGxKYMX4XJBtFLaZT4z0OSStbcR2TUHDG8oD2Hlm82qAV65Te6Bei96iIDljGO1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
#فوووووری
از رومانو: اندریک خواهان موندن در رئال‌مادرید شده. از طرفی استون‌ویلا و رم برای جذب این بازیکن اقدام کردن و مشخص نیست که رئال راضی به قرض دادن مجدد این بازیکن میشه یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103221" target="_blank">📅 01:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103220">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ5e6mY3QeFnU8bn75Vz1AOPXETzA0W4REzzX_NVRtiXnztIVE34zJW34hWQyBA551GY57B_ANfHACi2Q3EtzH7NfGtCTyeFsRpPRuDKxMIM5ZRyuZ_swns9VqRB1GBjeM5wMatoqslXTLTM4-i1t8jN2AO6ZKfKQzrv1QGezWuuZdCzKeiAJEzJQRcAaBwybFsfeJT5G5k1ljbRy-yFUp8lhpzI1-o_D3Tjx3sp_llT9UC195DVYcnZ-nGZK2LU4pGXGCXwJGu_9s_zQnXEesph8y_5vMbbKYudQZuVEAGJ2_sEXeJQ_4wt41Vc6t7tqH3kt89Se9OtNq13KWci-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: کونده مدافع تیم‌ملی فرانسه و بارسلونا از یک تیم در لیگ‌برتر انگلیس پیشنهاد خوبی دریافت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/103220" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103219">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
👀
⚠️
حمله تُند و بی سابقه محمود فکری به عادل فردوسی پور: زورت برسه همه رو لِه می کنی! نرسه هم دستشون رو می بوسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/103219" target="_blank">📅 01:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103218">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🎙
‼️
📰
علیرضا دبیر: شبکه به‌دردنخور، آدم‌کش، جاسوس و کثافتِ اینترنشنال! من محکم تا تهش هستم؛ مسئولین هم نترسن، بزنن، بترکوننشون، به مردم بشناسونن این کثافت‌ها رو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/103218" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103217">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzBQBJMwu8IrDHJ6SYTzujEbvC2mBZBFoST5-QKXbKHtcKdv-AsUTuxmOgG02kVi03fsYwx7vtS5psGO1MVfdBmZX0wn8Izw7aheAihbTArU6Oy62anQJc83zfDZdzFIIyoGca1VFOgIxbWorfSbRiys9F-G-N46Ix86MKi4GYDT0BLCqzk6mEEJvaTsrB26xdgNVPxCRLj_AGkkDt-_Rj5niY_SO5S5FTDg17xgtrSn6rWruR5YLSq2rL1i7ft6F_nljMwNrcBUHY_PpUeZ5KNlZivt4wIgypyZS6kC1BCyJWOmGiMtZhey_YLSl25arWDroyy5GuLsGh_8vqOaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇹
برنامه فصل‌آینده مسابقات کوپا ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/103217" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103216">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103216" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103216" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103215">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=LrbGlzvisXQt3YO0TghEJpwc3hgEk4V43y3QOtCJEVwrp-JboaSffIUBtrONyfk6AmKUbVWJ2xC6Fwx4xV3_Phio8U8WGjhnCVrYPzRVHMP9FDo0-LpnvarloyIrY7dCHZYpXsDH-o-6LahkNvU2KWnfM4VKAm_xWl98ayEnHMmnFOLeRlORU6WxESKkB02YfMdBL6Tbz-imXBkQSAZA7vQsbXdBSSNFWn1mTB8LCynbcaxSi3yz-wSCLNnMtjT9rUJjZPFCpqUv59JNiYZAkX0MEVfTvPbrOhZ7ZT8cCEe5d3doIV849zcIMM56fSbKt7Sv-17Jj7hN_2eQmZpkAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=LrbGlzvisXQt3YO0TghEJpwc3hgEk4V43y3QOtCJEVwrp-JboaSffIUBtrONyfk6AmKUbVWJ2xC6Fwx4xV3_Phio8U8WGjhnCVrYPzRVHMP9FDo0-LpnvarloyIrY7dCHZYpXsDH-o-6LahkNvU2KWnfM4VKAm_xWl98ayEnHMmnFOLeRlORU6WxESKkB02YfMdBL6Tbz-imXBkQSAZA7vQsbXdBSSNFWn1mTB8LCynbcaxSi3yz-wSCLNnMtjT9rUJjZPFCpqUv59JNiYZAkX0MEVfTvPbrOhZ7ZT8cCEe5d3doIV849zcIMM56fSbKt7Sv-17Jj7hN_2eQmZpkAoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103215" target="_blank">📅 00:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103213">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
⭕️
🇮🇷
سپاه پاسداران یک کشتی در تنگه هرمز را با موشک هدف قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/103213" target="_blank">📅 00:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103212">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQWLkqz7EV_AuSkxfE7KA07srHfLPzUrIZNrTWAyof2pLxGvGN5-4DI1Dlf5YKcZZ4FcNiyyASY3KfGuQe_xHYXZpCnqpKrO20on_UeFwVnEQUkQkqdM68le5wvYSogTnaxzgEHK8J1nC6HmRi-TexdQCoVYNg0f1AZ2mQbuAwXM_FaR8MSawoFAHtNGFhbP441Hk3XhsN8oHF0pze5XEoPVPFAd2ubcxCBh2yVws39Pg6ZWo2QTRIW3N0kyyd3op1y9nBb0MRmFfUOhgxCOLQBVnQkMrHlAWAT6wWHZFP_yOog-VdwyM3mu0ogRC1U6f8P5uSpD-i7kqXHHmQu6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از گستون‌ایدول: کریستین رومرو مدافع آرژانتین به اتلتیکومادرید پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/103212" target="_blank">📅 00:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103211">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
گستون‌ایدول:
🔻
بارسلونا به خولیان قول داده بعد از صحبت او با مدیران تمام تلاششو می‌کنه و پیشنهاد مالی چشمگیری به اتلتیکو میدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/103211" target="_blank">📅 00:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103210">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJfbmyBQL1VEDvB0RDB6_TzG_NNPjtiwc2z2tfO7I_n2pWC18_QTGLWBtlJBarDBxopMeIKtrcSZkk7bkjVfmA0Mut1FLdGKZ2iwWuH7T5VSH6mv6m_YrVUIN24FmWmPYoC6L2HPwUPPg0p0rPLstNRAdMhrha1YvlZlxTl9NqmMFJ38pMc_0RcGDfdV9nxFfl1xTvW3VUSWf22jDdTO_IkzNmdKBYuSG0A9eiLEqOs6RjqWlGPBu8sf4qizijGu2g1HG3Xu02clsHe_syyPffs2Z-G0DIF29c-LAcUYZEFm5vHYsrh6WCDvISuLwFrhxCA_o5sSPzHm1bbzLR4jsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
و
#رسمیییییی
: داروین نونیز با عقد قراردادی به ترابوزان‌اسپور پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/103210" target="_blank">📅 00:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103209">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103209" target="_blank">📅 23:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103208">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/103208" target="_blank">📅 23:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103207">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/103207" target="_blank">📅 23:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103206">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffgL7QWJrRks1NcfbKoC6mHDzJn93kCAubPCIEBbttNT5q83w01mYct1WSbJwZhABsUG-4_60wraS7AEy3_JuiBAqgXRT8YciBuKOo0r6SprX5cwbtV2LgxnutcIaHfTWsqxFky2R6_IzQDKxrEAFDtYdUftXau2pLQLDr-FQTHXVxR67HjyamgWBdzX8A9FP5tI16TuAQWtLGWm4PVHT1IvMN4nvvfYYt-hXt3RP2ONRqKTBVZaibeiJFKiXLcIA1eOYa3_-CwDQnPFn-3dUq36nHq7RcgohdfnCb1HUkSdU4Lrgo-jyu_nxVrLGkM3eGxuM06-BK3BbFUFXDnf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از گستون‌ایدول: جولیان آلوارز قبل از جام جهانی با مالکان باشگاه اتلتیکو مادرید صحبت کرد و از آنها خواست پیشنهاد باشگاه بارسلونا را بپذیرند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/103206" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103205">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IzLrI6t4VA5eh6FpQmpCIybmwlS-1VB4MYB8GX248pTirVrfQc7FH_7rIGoNZ5QeJxrAne3t0ItjLSrrkUihN7O11FC2a4G3Df2hTWNhlYxqz3TMplynIGjH_Wqhhjtno6HTs77cSqGPLtFC_2ONz_-4qWQkDxeVuAMWgmPbNh36heSGq7gpujX8Z6AAAqWaNvjmz3-FmyOYfBrl3GH7SifC_if8L9yFSNyiEv6rtV1J9r8A2_5DNkv70YjVeKl2YXmGFdFf7FuxWwjjdV__wCJmfUcxBg2Dm_jGjHlLWrz2KkTnpmKq5cycT6XqMS730qWkiPQSJMJ9Lr6qkLCxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
باشگاه بارسلونا در اقدامی‌جالب نام رابرت لواندوفسکی رو‌ در لیست اساطیر تاریخ کاتالان‌ها قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103205" target="_blank">📅 23:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103204">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mABBr1vIea-hg318ogCBL0_BC-tWMjblBYjYKT_bfdBN4_DwaWwNCHERfz7vWtCKHCNU9AcdnAi3S6-kE5P0G6XT7nqVH1qdPuHot0vRDt38SEp6PNCq1tHNXMeXvPK77XtC-AEqW2GIZxU-FyrRSGGcDdaAjG56kB_muGBigIK24k6mjO2JpAGA3eCfDhpEwcb_mHcJ05QHvc2s057zhu4G24cIXk7BlR8sfr8KRRTVbZjErwl4HWyb0jYFdlpu6poV56Sa-HUlgvfGiLTmjTnd7-0aiXuqskLLgG-csHMkPjiZcbOo-U12CntuJqsDWvp06d-yMLXgOskdFu7NlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دفاع وسطای لیورپول در فصل 2026/27:
🇳🇱
ویرجیل فن دایک — قد 195 سانتی‌متر
🇫🇷
جرمی ژاکه — قد 188 سانتی‌متر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جو گومز — قد 188 سانتی‌متر
🇮🇹
جیوانی لئونی — قد 196 سانتی‌متر
🇺🇾
رونالد آرائوخو — قد 191 سانتی‌متر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103204" target="_blank">📅 23:37 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103203">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0zI79B5nl5xozx4cnbeDh2xzBsF0mX0ARyJBoaeg5o1J0OXoTvFztdeCVcPTEFqYFAcCd3dPDDojBrMTzaXYR_hetCuL3C2wSWw-Pv91ycOS4WKU-XlFabtUAXYxQ_ST_xX_4-rMQ5KWQ_flyaGtdjv73WPfBoJJdHzx6ssXUlypUgs02GzP9l8Hrlp1YNa6IQH-BvI1Jgmv4Hc7Wp3eCHn0bUOhkf0jhTS_dbxOKng5ikSKePZjeJQMS9LQg071jDM_cLrcU4HhgwF9AlLfM1-QwqplV08pBs-C154taqs0b6ma04k-2qwQ7GRULMrb4ErKA6UsjhnSxsN2L0ubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
پیشبینی هوش مصنوعی از جدول فصل بعد پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103203" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103202">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7WN7_mzi3bb56SdbxVk1AhKhFepbCLtKHN6K0XlvUoMxelygf6ueM9s1po0heUau1JeOch4WS6owqiaWpaCrx72YK7BU9FdZb-yiZ4cftrwKqsF8UosNI3m3iJMd-Bca_rI6mSQMR3f4ld_3m4YUK3cZ3H3W5n-JGpy9_VVoiBiRBsrMISAn3v1YjVTsCvbo_muATr9s7ltQafPziJQkuoBxoCd7owwQnN7FlKMQ2XGSLWglPxgr0ssBBURFu4JzvSvEaKa0vGu16RuEprll1Ihp7CjnPG012BtlvfEqn9I1C3D7cJ_5CPmf_amEdtGG7i6L-dqcy99gJdDKixlKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103202" target="_blank">📅 22:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103201">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_y6FbsRXxjyLpz-rHLoOD1PdWglJJnS1Ktbjw0ygdgSdNR1en6lvyT3q3Lwv08uzD_DiRbwzk3GnQ1sVmyKJuEIqs5JAkrLBSZdzxslqwjqVWR97eOAeuSIDpnwj9jMigMo0R3fzE-xw3PN95p2sl-tLJh99u2LTJ5f1rmc5FjZFH6E3QuwncxcmBp25HnS2H2ppKV5l_CxszqrfwFpexdrmPZd-AjUpmrb0DFhUoUozcU31Si7TLMzpFeJA6K_Io6UD4aLlXqSk2t3vgqqeYqxrYoJ8CdJyUJ_l3kBaDJ59RGQFHanG0F6xNxk1CFruFxwywaccMM7QxYaIcTfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از موندو :
✅
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توافق اولیه بین بارسلونا و منچسترسیتی حاصل شده. فقط حل چند جزئیات باقی مانده؛ این انتقال بسیار نزدیک است و وارد مراحل نهایی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103201" target="_blank">📅 22:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103200">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=jkqsHvtRzVpv4zUuxDhIyafaeE6tZFjKLrM98zE2xsRK9_1xhK3t0abaXjQGlifXzRe_5VmgT6eZKnVy7QLMmaIhp6a9jNyczgAWj9DuruV_ZHFr7jJcgAkyt5imxGSKohLUKew1FgdfQCqqxOWyqPj7sDQd5BPLsBQpv3FAlrgISFuCouGvE0HdqpQ6jT0gaDdcTXbw_BTJi1VjtnnxYbS8V71yTQdmsjHZfVJlkxb0WCuIKppiAI1cJdftwylZ3J3JMepdZhufPOQXzQLBD7dj7s4KoCrKdosg1mBWSe_F0o0N8Jbk8R0Qlf5JLX6BjowzwMtRZ1tJSozDwLNtwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b666d08ac3.mp4?token=jkqsHvtRzVpv4zUuxDhIyafaeE6tZFjKLrM98zE2xsRK9_1xhK3t0abaXjQGlifXzRe_5VmgT6eZKnVy7QLMmaIhp6a9jNyczgAWj9DuruV_ZHFr7jJcgAkyt5imxGSKohLUKew1FgdfQCqqxOWyqPj7sDQd5BPLsBQpv3FAlrgISFuCouGvE0HdqpQ6jT0gaDdcTXbw_BTJi1VjtnnxYbS8V71yTQdmsjHZfVJlkxb0WCuIKppiAI1cJdftwylZ3J3JMepdZhufPOQXzQLBD7dj7s4KoCrKdosg1mBWSe_F0o0N8Jbk8R0Qlf5JLX6BjowzwMtRZ1tJSozDwLNtwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😳
😳
😂
😂
کوروش اژدهاکش بازیکن جوان پرسپولیس: می گویند اجداد ما اژدهاکش بوده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103200" target="_blank">📅 22:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103199">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psrqAVLuV0XCwiHieNBU0Xur_WZkuLUTCWyW7tTpgnr0Jmj10iSLaz_Eb98Xsu8sW97HVstymXLIhAyZDPF63FSONKq3ZOMgkKj9SuW06ehgVkj0weXxAO02J3AkttUDbb4YPP5lJcJebrYziJvSnEvVXW_p_LHod4PS2euGOxCZJpUhHjD4GIJwsHJ7mWGoaC_Euj_lh38hAINSFt_sBZWU_WcVcUeH9wqXtcIMPEzG2cH4sskgK2a5hrS8cH7GqBR0uitPBmgeS9CXZjzh7jmrb4Lc8-ZX3kPEq3ht3lvprq35VU7aQOidahfiTcWUomeg0RhD_E5ZXBgYjLIe1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
‼️
درصد شانس قهرمانی در چمپیونزلیگ فصل بعد تو سایت های شرط بندی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103199" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103196">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnIlFkT1MDWXVx2Cz72Y2CZox_Nw2kcrE2MKN3A05tEbespGhS-xf9iVXYX6QKvo0iU-IytCMoe7Ary3uaBNCBdV7zTZmZcoMCqo9c3vJWNJjG9OAB8rWmjbnjWKhlrj_csOEmcpn081DowiREHMmwUsp_OK_l_KliD5cTKGNIu_NVyXoHvasrrxhLiPde4-RWiCb8zrmXjLtZ4d2552GHZ8Vknwtpg177OD_G0_7k13L_O0FvwX8RDhiSoqBAYxL1eZ6jv8xoINxJ0jdJgsdubVlLoXLKuj18PXII1Dhol9mcCIemW0o6jnqMohg9cjshrCCrLp4kXaPYd9XLSqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjO2O0HA5esH-bRzwVze1aFVeduzhP6FbGBRaXq3YzmWa6SPUuStfSqJ68lgK8Z99CeSrf5F7J__Bc4BCF14BT_a7Vwwk-pYAp0wiBOy9OrKcvvQ9v1jHPVjzLiPekElMAETwI_iqIUtsa2zIS8nM8ZEsBxCiTyFcHtF02qNAIH1sRcJdMb1DZAF4aqX3IeKB2firaRxNyeZhe_Jpt7hli5JJVOHxSABBjlwN5r2SM22qwwU2WCCkkU2DwjOy61Le3B4jF5imZWsBf_FN9fewHnTVnTw3HL05p1SXq8s6_j51kpbPgmZ_Derm6RLrq9lyrp92YDvJvm_sHv_NVITeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=DxVjL0-gxkMDUBGO1g-pOyETwuF32at5AQUojB49CBEYJukWxC1rC8MEbzMG6W-pUbDlhyPyxzMflqcOudzuyhkmu9-_4KiEuy0slzvLj8HHNVCZ0we4xZzpTH2qrw4Oz_STsIYYnnaOYwAblXWxLo1JKap9GKb-R27FKhJg1mYpCXhKQndNMsiI_zxl_ggm_78yIqilxNQLtTnT8OUa7YFMeZ0r5TnJM-0xMGZAmisz-5qgaTaJUXUA0cOjOy2GpuGoz8UeCz7xbKNHvzBDqx7ury7pQk99k6r_2SsVkux5NimSkL0P_87tosAieDohABpA4-Daq_Ee0GIK6rWj7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bef03110d.mp4?token=DxVjL0-gxkMDUBGO1g-pOyETwuF32at5AQUojB49CBEYJukWxC1rC8MEbzMG6W-pUbDlhyPyxzMflqcOudzuyhkmu9-_4KiEuy0slzvLj8HHNVCZ0we4xZzpTH2qrw4Oz_STsIYYnnaOYwAblXWxLo1JKap9GKb-R27FKhJg1mYpCXhKQndNMsiI_zxl_ggm_78yIqilxNQLtTnT8OUa7YFMeZ0r5TnJM-0xMGZAmisz-5qgaTaJUXUA0cOjOy2GpuGoz8UeCz7xbKNHvzBDqx7ury7pQk99k6r_2SsVkux5NimSkL0P_87tosAieDohABpA4-Daq_Ee0GIK6rWj7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان پیشنهاد میکنم حتما از ست‌های برند mimoa استفاده کنید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103196" target="_blank">📅 21:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103195">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQzF97dTN3TWqGw97IeZDN0Ir37PNpj7IeVpkeVuQkcvDm18ljZQXv-nGf_7578QhHOkGfKUzUdSv7W5OaUvpUKjSaw1QP_lINXIl588DmnjI-heArvMADAm8c1-5kMZAcAvH6iaKDPSTIXp2OBlp0lPzN7RcGNP5nmBp7_7hg1dImZgYR15TlJOjIl7BBwGm-SEWaodkL5IcFcsQ0vXzWAVb7ADbSkpbXSUnWZHmLskw90e0IMEypraxSoI-OwJpMsOx5qmxM5zpPt5Dg0ldfSEJ0mvwcYqp2-LfmiaCj61APJdKIMJOutZFgY082ye1Z6zyBv72nZJUeQ-FIhT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
🇹🇷
#فوووووری
از گری‌جیکوب: دو باشگاه گالاتاسرای و فنرباغچه ترکیه بدنبال جذب گابریل مارتینلی ستاره آرسنال هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103195" target="_blank">📅 21:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103194">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGytCBpMcvAgxO6V33E3v_q4wobLiRQQWKPZ1b5WY7lgACTKvPPH2z5gfwMRVexMd2pL0fMQAnnUp13pe5Q8vO6lEGr3I-jCke9cFx7lBckImii9uw2K7p1lS1GqpMD5tyyvjbMSgkjFZVVq2N_rGQnFZHnMLZfmtjWgGmqsdxvVW6-qCicheeokrG54XfLn-1frptyl2PebeFESZkvo03T-Gbp9C9qsqoJMHe3MzukEBA3dpiWdFj1QrIUxFF9TyYgVI2XGhzUpw_uXjY1BfHQFTMeBhNENhdtw_nBcCdlnYekm_2RpWSuh6KA3FYjHlm_xXBsaHnCCqzc-CIMn-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
باشگاه فولام‌انگلیس بدنبال ارائه پیشنهاد برای جذب هکتور فورت بازیکن بارسلونا است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103194" target="_blank">📅 21:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103193">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfDctse4xeQkE-hovGGheMkWmjnyCrutgzmSvSf4-ewXWmfdshuwKZsciSs2uvpu_WjreBATMg7GwMIkUrZuzmtcdGWIQnNHpEh5tAxJnV7rEndjht3DLiORQrgYNvvzMZd-eKMsotI7-Q7-CqHFR3pxIxw3mdiaoPMUIdf3yK5rNFvQ7qxgzJfrJlJK2CbLUBfkacMUbpjGv4gU5uFUrjWf3eEEZAjhUJlcBuv1CnO0se30x6lnx75kDY9aeaB8DarzqYeSrWLH3SCEGIkqT_tADiLvlGlQYB_-3lB7bxAYkM5C9Tx9ZxDDMKvZg25DvxBN83ZuaQn-k_qF7Dvgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🇫🇷
🇪🇸
لپاریسین: مذاکرات بین پاری‌سن‌ژرمن و بارسلونا هنوز آغاز نشده، اما ارزش انتقال او کمتر از ۵۰ میلیون یورو برآورد میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103193" target="_blank">📅 20:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103192">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ6AUWioAofUF_sWFx2HY6cWXSz4tkAdrwANW-72c2dYRHiqsj7ck69v509PHpMYTSQhKQs5-km4WhCEQQeYiL-CU6zBtHgsmpcY7FQAfxOm4yHZW0HWQY2GNFb1XhQEkjjVMAZHbs5MgE0OHt8yUBe--APuZ0EzflIGnjNizQOTaTlMRky6W9fBGIUD-e2KXkjYmtau6CGXDKiryc24BXuOPD_NitosetSshJMbsg8XGmu6JuZ01A31Ml5BX3LsY8oc5YeTVNzEaIzXUFXUoy7jbv-eCAD7YGgNMNnBu64DhG8FAtYzbVu8bxG27BmmzO_E6kOn6f2zJ74-Rq8-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103192" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103191">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t06xRdDQBpm-1_TgLjyHl0zy51L85qlI_qvCD1QGpdj28Ov6daZHkjOd9ZKG27QFQPaxsAu_9JyxQz8P-o9iEUh8HAG345cJNwnvxcjYMftHoJp6B5IpMpT7BDSizhU46txw2OK4opvsf56k1w0XuMM-x1KnfkxP_dn6i1FCK17ZsvcjhdC3Z_Srq-XNxVSga1rmEiaHz0g3lN6RQ2HSNPwqnzkHjo1h2VN00t4g7s7B2YCnko2rujnNl_Z50xRBca-L_gSXkuVRgg8LBXTy_QK8E3TYEFPA7qqWsLA5_poNyqM5kEeeGuW_mvpqR2sJPsp9kwS5DIORkQmYkkIY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
✅
رونمایی‌رسمی پاری‌سن‌ژرمن از لوکاس‌دینیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/103191" target="_blank">📅 20:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJnbHt_gp9Mblj8ZFZd07S8ZR-5OQbQP0X90ZRoHc0Nw-A1J93Fswf4oW_xhOvIxZJefq_Mpuca84c4BEHIKGbszPG1w6YVeVC9WYpKH3DHo52fGh9gYDkns3yv74a6x_sJBN_z02IYCPOhuQ2ODTIu_x2cp3D3DNhjeN_itN-OVlj38F2V09CN2L5wfkk1GTe8x6bzcnh7MqP1Oa33tS-nhPGhdWOmWdvRAVVrUC5-7xApytzotz4Ws0cpZ58faBAqCxvp_fTqX_t45qWRUIjXruLnM6tTP9g4d5fQzy7P1akk7RdmFG7CwC0LXElcOPsNNvITkUOLjNUywLQgH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره لیونل‌مسی در مراسم خاکسپاری پدرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103190" target="_blank">📅 19:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103189">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=T6ZabDsBlrFnR1KdJ4XMVt_5R6q50SoN9jQNPUbr02vHaznrpDSfAZ2e17Z_KaV6fpxnuZiAtPcxMq6IAA_rlGyol7-UikphKo2SWucCC8r4ng8Np5WokrMBxzZygITgBnfJGgkZv6OgzDOvpkb1Nj8r9BZrXHMKUsH777v4nTs3L5U1Gfe3CnFvJ-oakF_PP0hZ5pvjFzu8u1WQr0SzLo9VbrSsUffNKAP1nF_RYalcGQT9oX4nMlYHSnmzB0C0vTeRXlTIWih7NOvjS3vbczXh8aL6TjNRzX31MMW8Xu8GjXR1V7_9CSdhEncP3oIYvCjrRbqHPbdi5-uwW-FmsYXP6zVA76UYq0zi3skjIoIAlSuBGQ0A701nQ-juYTIK1MEuA9cinKQp2Deio1fcTobIx2o1MaKopfojl4FVJ5jmHNyTNp1fdcpWvTFNFTFStQkwXq709VgfSxZIGfnGAjWpBzBxkjem7pfe29dziCeoFTXJ4Ia1C6QQZ_yfgTfeOcgoM0pxcblVtq-pFntEa6BFNlJNxr_RC5mVba3qN4xAnu8XgFHSlIyyxcy_WhPJpgw9-NngZQjbj54yXtJ26vpTfLqy88bEP3jHpTo2tGQLSzF451FSWBCSfygZXauoCdCHRQY4vlfzleMbnqyFnfxXrM207rFTGNlS4kK0LTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=T6ZabDsBlrFnR1KdJ4XMVt_5R6q50SoN9jQNPUbr02vHaznrpDSfAZ2e17Z_KaV6fpxnuZiAtPcxMq6IAA_rlGyol7-UikphKo2SWucCC8r4ng8Np5WokrMBxzZygITgBnfJGgkZv6OgzDOvpkb1Nj8r9BZrXHMKUsH777v4nTs3L5U1Gfe3CnFvJ-oakF_PP0hZ5pvjFzu8u1WQr0SzLo9VbrSsUffNKAP1nF_RYalcGQT9oX4nMlYHSnmzB0C0vTeRXlTIWih7NOvjS3vbczXh8aL6TjNRzX31MMW8Xu8GjXR1V7_9CSdhEncP3oIYvCjrRbqHPbdi5-uwW-FmsYXP6zVA76UYq0zi3skjIoIAlSuBGQ0A701nQ-juYTIK1MEuA9cinKQp2Deio1fcTobIx2o1MaKopfojl4FVJ5jmHNyTNp1fdcpWvTFNFTFStQkwXq709VgfSxZIGfnGAjWpBzBxkjem7pfe29dziCeoFTXJ4Ia1C6QQZ_yfgTfeOcgoM0pxcblVtq-pFntEa6BFNlJNxr_RC5mVba3qN4xAnu8XgFHSlIyyxcy_WhPJpgw9-NngZQjbj54yXtJ26vpTfLqy88bEP3jHpTo2tGQLSzF451FSWBCSfygZXauoCdCHRQY4vlfzleMbnqyFnfxXrM207rFTGNlS4kK0LTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
حمله‌بیشرمانه مجری صداوسیما به علی‌دایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103189" target="_blank">📅 19:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103188">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFcQZhplobxvvPBEmMA8NtNaZdg1gBG-cRTrRMq1JC72HPoZV-quiZ2v0d_wJMgeBg2Tk9dEtIJWMprRu4rm-5ubrUaG040qE-KfYwjdQdMYI8sE0fQgRpW6ajIiT1HOFg0JN4u4drTXRnxyjwuV8pK23JNs5zQ4x0BMKPXyePE51Tf5FWruvxpahzEHraQ71aqUCEI7zPGHNVKQBsO0yNiV3Fhp5hX8qjIrZWq5seZpaVXmOE8XBrt9M-nCOMbTPKL8fAxkbGSOLZz2G2TrDz9xul6ynVltPIxytTc4Ryexbo9TdIQ7z83PYLuwb8Tr2HoDGRcqV_kLIs-ZwMNVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی، منتخب کرج را با نتیجه پرگل ۱۱ بر صفر شکست داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103188" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103187">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMpq78aH6A_AXSerWe8aewTdd0P_dBF1Elo48ruxAXGbdPbdMi1xSiHFfdfsEr4P1z3W81LuOlGra-RSILJ-iLppoGrY707Q0YpYAAnSk3-toWFANe6MOY-XGseLcf6vJ-lYXS6uTVo5luUFs1sA4ksS0AgfLoFzBVtP9t0RIWak-1oqFcGH_-S0VZMz2i_paJGEG13s-XoPt6G3hJ88XfdRO6bzhS-8qjRJ8VVOceeeeruYmKDxUdzGXTfdj3xK6uzZ7-ELFjETo_0S_6gq2dWydX2ykmWKtD5KZIxo7Bcyvdp1z8-Qpanyh3u_r_rymz6qlI3JF9xO9S0s3xzwtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🎙
انزو مارسکا: رودری؟ فعلاً او روز چهارشنبه در منچستر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103187" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103186">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103186" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103185">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8-uxhmLYis8h-qxrKadKVI6ZrWgqzWoYdUpz4S8zF7vhn9nBsWscmGSZ0NpSJq_Omlm0nkTwPirz7vqnMPbSkqx4ZH6G0N9RIPrdUuJGJ-lZxFZ4rtlfHJhQzHlxBr9ZVZ1GHBGp0GiQpld2-7GitEUc9BPX9JEJIDGUQAMpb8ZzJCxiPI00qJ9grPlHad1DHKQzi_-DqPYOeK-yojKVeGxefcuaRkEH-zFUtLMxI6imV_2ESUVuegZsOex9Xue6hKrfTHCmsEf2yyPNkz2iTpvxNk4c9HzYy2R5wIOzlY36aVuwVE3YiHcYQnJIzsBI-knKHWkfc4zrUikbfsSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103185" target="_blank">📅 19:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103184">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=TxjmayINaHTdDrJuuzJkrDSXku8lJRV2uSGflYj15laKroCsmnoP0_-9O1lH4EgLzlROWBKGBQlhCtxo4ZSI78HDhYPhoPNkl-a6QzSvEv_yDOq1vMO2E9yd7h-srAArMTBbqNYJvhPHhw5LMRr9T-4UJsFj7NDKzmqLzY1oMflkSv_DmOQdYKFkjUhsrpeBBr6ATbuArS_IZ3UIQFktv6KYMhmimgXtG3agEZSJIT53OfeuRXMU_BXp_7WvsIosGYeB3bH5ghMto2gyOBoKRfHKxmdgI0qjHHz9sbCAOOHbK8azD1ZV3HisDIzfnAOrgZvGlU6v-scJO_xT7JbdobrjZqH7oVOjm7tdREGuHeekAwFW7bNnG5F6O1ptum83GZJEnlIjzKLRN9ziAPCDr1Wm5gXhyHH1cU4Zle5Z948IC_Ngsfd25iFlu_BQiu2kRbrGYlBYlmvkKuaRYMShCSUIGDbI1oXyXH7wq2gcsHB-IGlW65F3omZiasewyxuQr39hnmqVI2ZuQvutxNsy8RmGFQw1uJ1RjRknyuugTir1ooifdaOtXDCFn44vhK_uW4LMXuWGUTAqm7W_pg1wbN9jPtDlAQpi6L2n10EQ2iaIFWdyxjmf8Monur7QrbAReJBxiBm4q-IjvGaeYc_JUJMLEQD7w8L8SDwbbLZlNUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd83a8ae00.mp4?token=TxjmayINaHTdDrJuuzJkrDSXku8lJRV2uSGflYj15laKroCsmnoP0_-9O1lH4EgLzlROWBKGBQlhCtxo4ZSI78HDhYPhoPNkl-a6QzSvEv_yDOq1vMO2E9yd7h-srAArMTBbqNYJvhPHhw5LMRr9T-4UJsFj7NDKzmqLzY1oMflkSv_DmOQdYKFkjUhsrpeBBr6ATbuArS_IZ3UIQFktv6KYMhmimgXtG3agEZSJIT53OfeuRXMU_BXp_7WvsIosGYeB3bH5ghMto2gyOBoKRfHKxmdgI0qjHHz9sbCAOOHbK8azD1ZV3HisDIzfnAOrgZvGlU6v-scJO_xT7JbdobrjZqH7oVOjm7tdREGuHeekAwFW7bNnG5F6O1ptum83GZJEnlIjzKLRN9ziAPCDr1Wm5gXhyHH1cU4Zle5Z948IC_Ngsfd25iFlu_BQiu2kRbrGYlBYlmvkKuaRYMShCSUIGDbI1oXyXH7wq2gcsHB-IGlW65F3omZiasewyxuQr39hnmqVI2ZuQvutxNsy8RmGFQw1uJ1RjRknyuugTir1ooifdaOtXDCFn44vhK_uW4LMXuWGUTAqm7W_pg1wbN9jPtDlAQpi6L2n10EQ2iaIFWdyxjmf8Monur7QrbAReJBxiBm4q-IjvGaeYc_JUJMLEQD7w8L8SDwbbLZlNUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
مراسم ترحیم پدر مسی اگه تو ایران بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103184" target="_blank">📅 19:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103183">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=v_i78sw49OJ6iYz0qQuclmoRtec9qn-qnwdtiLY1HcdpG9W-J0w-ixnjeO08-UkncMmasEw1sCwf8_SaaQvbzRqtBHLm3gB3BRvfphafWwXWFoNzKxElGAvQTJ2tJbJ4iDhRHs6COJPughyyj62MWBJCq6QrsUVlKcFj10ZtVzRq8BZAyjV5Ad9zUHb0iLNCrzx3ZXtwTwTF5_rZxctkNSdBgGZ8ueLzBFT96saUsP08rr8P53soiENkTW7rkZgZKXUMNXDjZ1h_yV7ivEcLtwUf3aQS841qlxB28RGmed7KdjXqYJvOfudZpoDfHSv8GB16cwqEynCWZywxNeKaoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc71e63ff.mp4?token=v_i78sw49OJ6iYz0qQuclmoRtec9qn-qnwdtiLY1HcdpG9W-J0w-ixnjeO08-UkncMmasEw1sCwf8_SaaQvbzRqtBHLm3gB3BRvfphafWwXWFoNzKxElGAvQTJ2tJbJ4iDhRHs6COJPughyyj62MWBJCq6QrsUVlKcFj10ZtVzRq8BZAyjV5Ad9zUHb0iLNCrzx3ZXtwTwTF5_rZxctkNSdBgGZ8ueLzBFT96saUsP08rr8P53soiENkTW7rkZgZKXUMNXDjZ1h_yV7ivEcLtwUf3aQS841qlxB28RGmed7KdjXqYJvOfudZpoDfHSv8GB16cwqEynCWZywxNeKaoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کارا چیه مرد حسابی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103183" target="_blank">📅 18:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103182">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
هایلایت بازی آرسنال 2-3 دورتمند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103182" target="_blank">📅 18:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103181">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=mNQzBHn7K1PpWfi-VfAHNNW8rZNsoDyCkqn5eGIjuM8whX2xnurN09ON6uYLchnTweI4FAhYko_jpYbN3kmV9Sgj4IifMcDguZP7rQryHBcWqjvLHWwc7MajzWFt_slyxcf_8w_zjWsu-wNg9ZcB5LzA_pdQQN8Z8JL__FiayWmFyFg8xZNH4KEqo-Ov-pMbOFMWsyYvWI7KxsWLHWS4opCzXj9VCHGPciwFML_zW36rSmcbn9OVrzBfkuO8D1UWa29OWIFqc5RcFVqxQrxrFSZlDaQdKbkxkFXKyr4uGrlFV8UhWQ6d6V7bYctNjLryclzjcck9Gr1X8FX51LGEDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55e5129ef.mp4?token=mNQzBHn7K1PpWfi-VfAHNNW8rZNsoDyCkqn5eGIjuM8whX2xnurN09ON6uYLchnTweI4FAhYko_jpYbN3kmV9Sgj4IifMcDguZP7rQryHBcWqjvLHWwc7MajzWFt_slyxcf_8w_zjWsu-wNg9ZcB5LzA_pdQQN8Z8JL__FiayWmFyFg8xZNH4KEqo-Ov-pMbOFMWsyYvWI7KxsWLHWS4opCzXj9VCHGPciwFML_zW36rSmcbn9OVrzBfkuO8D1UWa29OWIFqc5RcFVqxQrxrFSZlDaQdKbkxkFXKyr4uGrlFV8UhWQ6d6V7bYctNjLryclzjcck9Gr1X8FX51LGEDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلبم گرفت حقیقتا
💘
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103181" target="_blank">📅 18:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103180">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyVgakj70gUr0sH6QWt6YQtkKkk-izrgwcBVnPmK-e-53T0OkCHBljzKua7txqO1zkWclwFRNvwssnQWkMB08HjYD6v7eaIq3DQG0Pq81NDoq-2mtjJn_HEtAl2MViVOZ5cPLcTLoenXqSguJkX5KDoHCy8I3f3Z8z4LLi6nFsZ-Hu071dJURIVVH1iRByzGZdPkavSQU_56Tu3hzqVAFsfcI9VoNUd2UPY5Z11dgLac3b514_Ec_aBYVQTlpfvMUZEkLXj6xTHEi5Q-JAGhkAtS6N2SkuA9f36sACJEAQr8HRV25T34Kp7WobSTthIQwNBdhRLeDNINf1IPtWX7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🇪🇸
فابریزیو رومانو: پاری سن ژرمن زنگ زده بارسا و گفته با بازیکن تون به توافق رسیدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103180" target="_blank">📅 18:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103179">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=B9iMcPinbejwkcttJPv7SFqOUxjlwl9CRUl-FWwUmeYtJDN_-XMJVN3uoSJkDaPzhWA6pOHvvFrhiXOsCveB2YXaVn8KMahOLo8Gggl8JUgcBJlp8CtpaPMfonNwiJRtZOt8iua4ANVljdlq5iS_cf2N41hvRjrht8JCoAVIzmab7zGjhhSbLzfC9IWqn0bNCkfZ2eK32i1WHsbZl2OFm13BZjZQgklAghJISPK0COfhWcpNCbgbkpKUAXD_oKgr2x6GeTZy05zX7E7hFOuwCv7m5JZA5l0r6GPwfME1XpKVSVxoq3b4LPgj42hlRME30RbJjIZJTSLGuoNy50Mzig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5ca064762.mp4?token=B9iMcPinbejwkcttJPv7SFqOUxjlwl9CRUl-FWwUmeYtJDN_-XMJVN3uoSJkDaPzhWA6pOHvvFrhiXOsCveB2YXaVn8KMahOLo8Gggl8JUgcBJlp8CtpaPMfonNwiJRtZOt8iua4ANVljdlq5iS_cf2N41hvRjrht8JCoAVIzmab7zGjhhSbLzfC9IWqn0bNCkfZ2eK32i1WHsbZl2OFm13BZjZQgklAghJISPK0COfhWcpNCbgbkpKUAXD_oKgr2x6GeTZy05zX7E7hFOuwCv7m5JZA5l0r6GPwfME1XpKVSVxoq3b4LPgj42hlRME30RbJjIZJTSLGuoNy50Mzig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ساندرو تونالی هنوز فصل شروع نشده حواشی خودشو آغاز کرده و تو بازی دیروز تاتنهام وسط بازی با بازیکن حریف به شکل عجیبی درگیر شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103179" target="_blank">📅 18:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103177">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hfx7DPODHXL6aqer5lDtKdSrR-txRqgprxBhNVGhenoDUgWvow9pNEaJ2VoqBwrrydPdDjQz-fYg9Rk4qnzRbHs3jGw3_TZLXAa69bRpkHdQsVnU_sQ69cUqAQPPEnsJP6Uy0c5IhzguYcb4uMR2sB9VhuUoD5ysST1sy4h4AH-Kh3zN-tVo0BAlX-WkiRSsTt-V8b2-z-glV8KZEsUUcq5iTbJxUM4Q5ZslyJ9HjJNrDVG2AtfTSzTltbGNvxRnooHiOz4wkeZpxPFekW1y0EhLuWK09-q4OOPajOEGnFa4T2iezTM_8gbFz900WE5w0Y6uTqKIu_GSkrFrxpiBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAhtGE6i6VeUqoXPGBO4qhqFVuxQULfTlSKbd00r6a7Pib99esiGSH61TVntW_PqxXan-WediiKYe2fBuVkwuV3ymxVWHEw2bwxNAlmhZVYu2jsMICiV4OdrYl8UOtBaMfnBWEzDFdB2NoFTmrzFXFcx6vgjn8kwNW9TbSNQHAQYhaSsVkoq-xSmT963iTil0Uoq99bs1iX3JHZEuIh3jpeTsBICROUt7J2A_rIJYpxLqYgIWNREpXGw_IrqoJUTvCCcss1waHtpgWI9C9a47bZ_n-qHLFQs-cfsBfgded-CnBKLzpY-Ko5_QJopH_zotKBkNSCBl5Fay40NjWOLJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔴
رونمایی از برونو گیمارش پیش از بازی آرسنال و دورتموند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103177" target="_blank">📅 17:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103176">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8ffUq2b37XNS-Igp0gpWceSssnqSFmttbQentfm5Sc9RZmTecE890AptA_j2ifLry2A_FRCocAC3fLRfDwLesWCoSrpMLAreQVEnhEDFd45YFy1wTMGNBOr7KBUAYVQr9XNe8ZG8y-yc1B8AyhG9gXjbSBTzyGPAjRTKtDs5cNtLt-eC-Z7r5Gf128ij7VLGq2cmD_05yC212m8yP00yxzj5INoFS6NcDdLDMWZmiE1ibcguPCk8-DrddaxzySUmgVKzIhWF-K3W6OwxSTYu9Wfmv32UY_nKjvcz-E7T-hRdgos5K6EXk69VML_u-yNA9vtW_m1BT3JGocQY0Qt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
چلسی مقابل دارالتعظیم با پنالتی مساوی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103176" target="_blank">📅 17:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103175">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=LO72sPRw5N6-YLL8k6TeVEQMnSuy2GMs7rtaIPECXtxZzpEHokjUWDjZ-vgSHB2IHoO3TCUXHYFa0JcGuPIUih7A2vK5amuteaBRfod7_WsbRCm7BFHQVOsqnY3Yb0h3mx9K65LeozuLqU3MgjcLlJ7wLjlLciIi-sDLkQ4OrEJbbIyTYR9-1HRFQCWyojaHj6Wri3VmbXOG1d1r9k7QZ1jJlF6sFbYy2k1oJgrm04ET3F7p5z8rQnMxsQgTEGKuIfGPWl_iYuX8MtMxz1En1NON3XRN6GA6AUtUzAeQpdtYOrdeR_FgMYySoWF6CcTTrfBAK30CXGnTHHHIhcLRDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba95cb0cd.mp4?token=LO72sPRw5N6-YLL8k6TeVEQMnSuy2GMs7rtaIPECXtxZzpEHokjUWDjZ-vgSHB2IHoO3TCUXHYFa0JcGuPIUih7A2vK5amuteaBRfod7_WsbRCm7BFHQVOsqnY3Yb0h3mx9K65LeozuLqU3MgjcLlJ7wLjlLciIi-sDLkQ4OrEJbbIyTYR9-1HRFQCWyojaHj6Wri3VmbXOG1d1r9k7QZ1jJlF6sFbYy2k1oJgrm04ET3F7p5z8rQnMxsQgTEGKuIfGPWl_iYuX8MtMxz1En1NON3XRN6GA6AUtUzAeQpdtYOrdeR_FgMYySoWF6CcTTrfBAK30CXGnTHHHIhcLRDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
😢
وسط مراسم معارفه نکونام برق تبریز رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103175" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103173">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYt58Jh0g8AuoPjLCY_C1gIzeoQ9UQQMH0Em5caeVVUfJoKjjEtVDbSAs2Ww5YEyH8FSMPdFeFVxbdwaRtpAZat9AWU_UWB6joJL47u_w-s3gSMP41XpuwnsnmKpgiWjP1hcrRNSj9dPm_0jZqxcN5EsyGafhe-dl3fvW5e3a8mg7jSF4tKcQ4I-LwILZfnJZgLmNprBXXEG0tyvlNtbiYhOM0shMwLgmTXlPlUSuhCzkoWXaKJaAaoGuI86_O9yyTVb61yq78jY9uqr9P2mzxh23pbsxIBcl2d8crpssHGt7iU-rZK7E3a-QuovslPItGpYLFvZmWNZv3J-SXDy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه دومینگوئز بازیکن 16 ساله اتلتیکو تو بازی دوستانه به سیتی گل زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103173" target="_blank">📅 17:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103172">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66b01add9.mp4?token=EcaFyLx7tojD0XFaIp0BWlK86iixsUKijp-xfxyvNTvt3S48C2aL1bZKu9-L4fCt99JrjUAwNgKeBr_issC0f5IKR4qGUr4Uu1N_clehX2ptuMgpyPdoKQdKELhrJ9uhPa-X_OLG6hKM-f6BRHtdgIGBZeKTVzrSc35MpchLQ2v-5bKpnqQhcA7V0Y8lKxb6Q_JkevkFEKhAWwu2PJre3g1ckt-UhVs4cE9mPipB0X0T7tW6F9gLdiDDXDVcptXQPy1UFgFyCWyjZKkpj861FlisH94h9b-7RE4T_nTqsDB-7ewNfqBVrYt6GrYJYadEv6lfprEDqlCd1E8aZbnMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#نوستالژی
؛چالش‌دیدنی‌پسرمارسلو مدافع سابق رئال مادرید در رختکن کهکشانی‌ها و ادامه داستان...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103172" target="_blank">📅 16:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103171">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_Cu39Tv0fqFmqaLoM4OKTqFsCKISB6T-J04PqFXjg2kcCrawktdnx0w5oLthW12cK4zTE3Qhneg8-lQiEr66pKbilqAk9EJNkR99lRX-YIAkldfbnVr5XUbF2NLxvLFi8dGLvUphjcYUkecKXsfLbO5Ny1xSKINgz16iy0E6QcnvUkYnMMF-Iz6UdpgRisHzdSsXnB0H5-xekDTiKaGFZr9ehq47_VHfh32e-tFwK82MAx43uy3HfFuH8u0FF5xeiILDiS7eb5Srr1l4z2A6uQ7-EnRGkIxn-LKQNmDFBHdsTXszJJZ7wQtTdRd0iyz-psbAh4MHNWxXtoZzsTG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
8 سال پیش در چنین روزی، تیبو کورتوا با قراردادی 6 ساله به مبلغ 40 میلیون یورو به رئال مادرید پیوست.
🎙
تیبو کورتوا: تا هرموقع رئال مادرید منو بخواد میمونم و قراردادمو تمدید میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103171" target="_blank">📅 16:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103170">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=Qj9X4cyq-u8T-3x1ADalwvdQyiTc2BF_TYGLnu5Iid9bE2wKOQioj0SOnJsEP3KTknsgSTlg7BEzBrUljz03wyvDmz-Mu8gCLcLN7cAypuJgzTMTYhzLhRWheg5RC970IR68TP39826qQs3-DOnibpsr3OI0kv36n8PMbSPjsufO_5nsw8-hbC0bFBS-BI1BMvKTudKrkbgLQfDxWl-bnBoQzZrXzgOZCqn8C0GeJFgC8wy8J5ccqItw7cP2x6tpqLeUMLI8HGHTygQFE9zJW_qixX1NQtBIQ2rTRPTlsid7uJucznXAsZZ5uGJMgbjBtCGFoJdn41PAusOF_3SJSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca151bf7d.mp4?token=Qj9X4cyq-u8T-3x1ADalwvdQyiTc2BF_TYGLnu5Iid9bE2wKOQioj0SOnJsEP3KTknsgSTlg7BEzBrUljz03wyvDmz-Mu8gCLcLN7cAypuJgzTMTYhzLhRWheg5RC970IR68TP39826qQs3-DOnibpsr3OI0kv36n8PMbSPjsufO_5nsw8-hbC0bFBS-BI1BMvKTudKrkbgLQfDxWl-bnBoQzZrXzgOZCqn8C0GeJFgC8wy8J5ccqItw7cP2x6tpqLeUMLI8HGHTygQFE9zJW_qixX1NQtBIQ2rTRPTlsid7uJucznXAsZZ5uGJMgbjBtCGFoJdn41PAusOF_3SJSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلای تاریخی کیانوش رستمی در المپیک ریو
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103170" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103168">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/drzhOOT2FPRY3Rg8fpd3sa19SZTB81nVFOPtksFwIh6HolS91VZLHD5RJpAKmvRRjlR0GYjgGs3wHnsMbKRS2qpvX93vjeeKmyx9c1ZUZhapAbguYkxI_a02yOk3g7yWgj7x7SpSiyMQO7OXAznUv_5lpAKu_a1EPhIbj7QB2kG8UV1LGIMdLWLgHp6ItLlvmxulhsuuRUAQTNAt2bOlWZqVHYzxm2IIKjLz68iQNS8p41t5P8ODxvnxhpKfZQ-h3iNTbMza_vuwaKLXdrz0SN_Sd4QTT9hpBYS5JC2SDhb9MsQNu5F2ZJsa1QIbxLAWzLKjVZ2VhCfc6ohMdag5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1T4CswtgObPxbFy4WIj03S8KPuyJvhhl9sOS0H9A-3lq1LYzMNd5cvG_fjC11sD7Gjb4r8wNVAg3p0BA6Cff32E8GgSFMv2XF6l8a6nc26S4aZ8xx0KbPA7fnaYycd9YRdMLPFidTUlZ0p1ZO8G294qkRTEQhDb2QwF_f0eGXAlvz75RPn5XTBJFT-r7BBP38AJKUkVvksR_6DfdX2D5PFKCraNPDxSzpaKZnK7euo7kl11ogwC2HxMIfA184qFsc_mcznrRqhu0WYpipwDlpQ7nMDQWhKAp1Qrc1BL06jMJmmAHuZg417SPMgkdLtGun7YQJZzuEqK2dGBXPKk7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103168" target="_blank">📅 16:26 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103167">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=pkB73kmov-tVqH-NYugkSOj6yxuw1zyrnIbnkTAlf2_7BZIGhoFaBSs72PywIA9YYjSRI4Oc7Nlqbi3PxTxM44Q7ZoA3spOZxObVsR4EE-ePhh0kJHFiXr8icNyKlvryQLhPh_sohprrFMUYR5czT8telORRMdA-rDEb10kmQUwPJWzZL7elBTDghQmr2o2zljp3IjyqWSWEnoqz8MH3kq9-NoWdvNs1pzpq-sb7OcLeosLFJ2QMRTaZ5VWHB6QQEnzqtWcpiWyavAL8ZPlEu3PRTALPa8Recrz04lDtINB7GvSrC6q8pR2AV3x5KoqeFNNnLRUf8MXRYWL3BGqz-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53383c27e3.mp4?token=pkB73kmov-tVqH-NYugkSOj6yxuw1zyrnIbnkTAlf2_7BZIGhoFaBSs72PywIA9YYjSRI4Oc7Nlqbi3PxTxM44Q7ZoA3spOZxObVsR4EE-ePhh0kJHFiXr8icNyKlvryQLhPh_sohprrFMUYR5czT8telORRMdA-rDEb10kmQUwPJWzZL7elBTDghQmr2o2zljp3IjyqWSWEnoqz8MH3kq9-NoWdvNs1pzpq-sb7OcLeosLFJ2QMRTaZ5VWHB6QQEnzqtWcpiWyavAL8ZPlEu3PRTALPa8Recrz04lDtINB7GvSrC6q8pR2AV3x5KoqeFNNnLRUf8MXRYWL3BGqz-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روی کین اسطوره یونایتد: اینکه‌دنبال بازیکنی بدوی تا بخوای پیرهنت رو باهاش عوض کنی کار خوبی نیست. تا حالا نه دنبال کسی رفتم که باهاش پیرهن عوض کنم و نه از کسی درخواست عکس داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103167" target="_blank">📅 16:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103166">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD4JFZ5iusXUa9SDRaGjvqpND2IuqyzDcBvacfeM-BnEI0FlYi4xXnVoz0P9-sFzF6FXgzTstkmCMlylZO6xbu93APIszd0TJ75EQKKjPCvpvo07gErolv58rM-GJ9WJ2gpXnAyWPe9hM6kTHZI1aVgDLuCXJD3CvhjAPgf_a8C2wkYrwCb8QJ2ALwCsTvQSvk0hELFNq1UzPkUw31RoZlJdid3_XYE05BXiErJQJ1U57png04FLQnqSPprQ4PmSaM1cKnKOxiPTz7j8Nb4asl-Th742-c-nC5Zk3NRD66yuW5BEaEphmfNtRWTwTjbToCQGUL4AZ9un0c-OXB7pKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چلسی از دارالتعظیم مالزی گل خورده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103166" target="_blank">📅 16:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103165">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWzHrLcdls3ivXyn6lbPX8v0nzgMB-8MbbcfSvymjcAOZ_6Hx3LtO2AEbiBGZPuAlhyNlz_CzdC9JQrDgGeY8yPWlRQY5zAh5GXrVcCLWkxSPZkhY1Pifi_ArxaavDPYd8xEZK7594UXhYKtHun7KmDVTqDbdAGTpOTy8qmvwMUWofmZoSUKuU_v58ObI92RFVE_2dZaZzia_BooH33uQarg_dRM3VzmXmdCWmIs7QeL_KJFpPTc3IjCZWDcmyaz9TCygppjvXTDAbooopVU7OoqmiQFSXeyA6TTx5cUjkPT7545gO5OqteKsKM5qdDWK_WSEOyn1iQJ0W7TtN2fwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عمق‌اسکواد تیم‌آرسنال در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103165" target="_blank">📅 15:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=AjAT3rzhGLySYskEAG9c3MXMDD1eHK0XA5YyrO6hxCC35lwxshxJH5Ot_TpLCfneRVTyTT7uBADUQgdW_-7RMddSlkJIs5IZsR-DNQAdTtbrOK2M3qA_tFxP9DHB3xOpw7cWf8NDGZX7-2xGnaE5ECaI56NvBMKbSkdd-MabOZb0sULG6eMBNIWdLiLBx6xPDzESrtR8bjNyJvCNvLvo7cnouXYoC8hbHyzUj2_BP4k_IS4KhYdVu6kIskgcYixRoY_iG3Xroj9EbvkhHrZunXn4nH1Y8sobUajZL44tU9L-gHY2NeKpPby21Xv0g9Cz-YYfSiNFexl7q8ZqYMnReQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa7513247.mp4?token=AjAT3rzhGLySYskEAG9c3MXMDD1eHK0XA5YyrO6hxCC35lwxshxJH5Ot_TpLCfneRVTyTT7uBADUQgdW_-7RMddSlkJIs5IZsR-DNQAdTtbrOK2M3qA_tFxP9DHB3xOpw7cWf8NDGZX7-2xGnaE5ECaI56NvBMKbSkdd-MabOZb0sULG6eMBNIWdLiLBx6xPDzESrtR8bjNyJvCNvLvo7cnouXYoC8hbHyzUj2_BP4k_IS4KhYdVu6kIskgcYixRoY_iG3Xroj9EbvkhHrZunXn4nH1Y8sobUajZL44tU9L-gHY2NeKpPby21Xv0g9Cz-YYfSiNFexl7q8ZqYMnReQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
کابوس شب و روز بارساییا در فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103164" target="_blank">📅 15:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103163">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud6zeIME3yIP6Nb5k8kcMbgWl-VykMCbCvi76c5mKIn8NJr8vMD2Y0GX81za53c0FEoqrsGKVP-0KZw1IjUCmGf19Si-StGVXKuI49KXqmeFBRkGdaizA4qAHpPU5D_HTHgRsJvxN11E8ov2wq92dCkQbqwLbmRkHa4QGh1Xzda-ZogXs2ny3ZN69w-7n52MVI5tbNg2PuRZCjySlRb86Aids2RWEDYinGVgRirekTneYOFjG42p0FkvXCUICQxl2qqfjlXPIfvSMLjSYcSIh2IBucx1Ry5b0BE527HctCGcHt76AEsvTYXEuvws5SnxYa4KCfAEskIRMsdwqtmghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آرائوخو وارد انگلیس شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103163" target="_blank">📅 15:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103162">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeilQtE-pfwOVm5Jj5JHLZOPGaL18_1UqZdjdgdvKjhHp6C88dkqmZmlIVmNm2st2IQPQdrQXPlSo-22bjBhd5B2oHyFJpIY1DHbbpRezCefUQUf4ChpzLjV6462voH2jybpGfOpTONyaIDQATro9xavTZxQkNtvIM5oCi6r_OkoRmO8ubB6dCNg2d4_7B04pjLg91xr21Gw-jC2SSeEQG0URUJEaXHEdI6zdcUvQJkrLdShtStBx3W0bnquVm3yqysuSIjdGz7DFomTkCuZxE8V0lbhOL-IS1lSj2eQsgnviYZZ3u68M6Hyvgl8wJY5Dvjut-sDMg2geqLfL-TRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
هایجک‌های تاریخی بارسلونا از رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103162" target="_blank">📅 14:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103161">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=d9w8cyO-8P87U3uE0_Bo-9FGUrhwkUS68UqPwTat3wTciu3BvZqoOGiWltcah7DnCqqB9GHvMLFpXgsEfvC9WOeNmxIjaiKpbhYl00m7kKZcpSFCrTk4O5gR7yylQx6wcwDvAkT73E2HxQVDhWkTdnusr3hcqA_0mRZdz95nS_LfzsoYW3rT1DVCjSeNhb_9Ev8DbsQzRrxHzscqDXEMmbtpzDm2stM4qPv_Ea3XRRTNRMw1lqeqPohbnPjgs9FixojY2C1pMrUETmXfCu-Mz1glwv8hSE-DjqgXgXaxlDjzPC25_Szy_cB3Bq2nH3KeWCuT59wtu26qlo9-Tz7pag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729f5d60ed.mp4?token=d9w8cyO-8P87U3uE0_Bo-9FGUrhwkUS68UqPwTat3wTciu3BvZqoOGiWltcah7DnCqqB9GHvMLFpXgsEfvC9WOeNmxIjaiKpbhYl00m7kKZcpSFCrTk4O5gR7yylQx6wcwDvAkT73E2HxQVDhWkTdnusr3hcqA_0mRZdz95nS_LfzsoYW3rT1DVCjSeNhb_9Ev8DbsQzRrxHzscqDXEMmbtpzDm2stM4qPv_Ea3XRRTNRMw1lqeqPohbnPjgs9FixojY2C1pMrUETmXfCu-Mz1glwv8hSE-DjqgXgXaxlDjzPC25_Szy_cB3Bq2nH3KeWCuT59wtu26qlo9-Tz7pag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
یه ویدیو کاربردی برای دوستانی که حین رانندگی قصد دارن ویدیو بگیرن و همزمان موزیک گوش بدن؛ بفرستید برای دوستان ماشین‌سوارتون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103161" target="_blank">📅 14:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103159">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACzxk7kVRy4ssABFuF8N6d3Na2Qi0bXsi5e31FK9Me8Pe4lMZYVtlPPS9RrVnxXusA-UtGRfuKsvPVVlfVdLGAdrXCQ9qTYDM62Few2PHlMBD4mtoTsbnwhPpaY1Z0P77ta4lM04VvQwC91xWVWfv0CPTa6NJKxdRnBip6RhS2QLCJTwhRjo_EAiYZwmwC3p0rpTx3EIbliGhCeQ3FW8I7JZkWniNW7YNpgRtiVUmf6jZKvLK21uxkBJJEecEz2Ks8nRz0aGAw6lxbqmgW0z8PPa9hCyZo4kezr0CtDleziZabD8B9NVttwsi6WbE21gDbIHG0d006Cx9KKMwmZCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q489JJPPNRJ370XW9t8H--ENSUvMcyb-QsrTnfHFjqHKtVkESzLaoWv-tyy0mvaos_shvcfWCdw94w4s6hiVIyUAz7OTNef5mj90phaMSt6aFndlpXSAhlxWruQpC8SHAzLoiYwR9oc93u6EZSw3YXMhGU53YEzKZZrxFLbeDpBq1iSeFOX2brHCEowmf10KO-yox04paW6MOE0zp-OC_Z1QBIAtWfiJZxUjQTMR4_7m5GdWVl1GjRLRpOn0py-LnSwX813yPzoJfiscjxT0vfBTnh4Td8A2DIvUrssSAY1bOWoeguhxgl0IF5vE1M5tr0KAjKa_3X0lpYwmmHkw7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
ترکیب منچستر سیتی
🆚
اتلتیکو مادرید در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103159" target="_blank">📅 14:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103158">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=PRvpw68tGZ0IIKJrwwf_qyd5TEmIyrXlnUxeak7Yc2utcp9I6-Kl1FtQSiDJ8mUKPOCIpy6BgZHjcRr6Eeg0VmyIjdaBOGlXAGEdfTBk3txW72jF-FcqwnOeJDWkx8wp4mbtzmPmUVpl2Tbzz3xevgdySQZSWnBd8z3sLXUiuKLU0Yll68OopTjRCdhcA8MIkmM1VoxTPpzmyQyxaroZRoEFmoPQoiA9Q4Z05yFx56_ys4Yw8ebMbTHw_b3w11sXWQaB9z5ZQSMkq8oOhlW7pHDCOdgAwNm2nDpmQMMZCQ8MWeF5K6zvBpBw8pmE3dLu8O46aXQ4flUcIB_CFn1gLnG-Imj22JPuEzbs7pbt6xvcXnh0FKPINVVRvv6QJN6sf1XX4QJygpWTV16ywaECNmhR2vspeGsA6Swh5mmTb5S_ezgeOmAs98lQ7wX2c87EnoeDHirf_35GWGScqnUrJCszB4vOsrp4pYaWobX4xWLmu22kdQkVAP5VD3h8Lo7W7ZRGabFVNcql8k2WdDP_GNAFawYpGKh-i1mhkeGxmYLScQBU-7H2HYdThinNpqbfm4EzbhnUvbVdNOJlcbvFjbaVBjn-PxPizWhgIJa194e5CuFt6txvij3yfnLb7dpM-LkFDEu035jxg8ni0V5wvYqsOWq0RDL4SJ8ICWvY-ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815f97cdbe.mp4?token=PRvpw68tGZ0IIKJrwwf_qyd5TEmIyrXlnUxeak7Yc2utcp9I6-Kl1FtQSiDJ8mUKPOCIpy6BgZHjcRr6Eeg0VmyIjdaBOGlXAGEdfTBk3txW72jF-FcqwnOeJDWkx8wp4mbtzmPmUVpl2Tbzz3xevgdySQZSWnBd8z3sLXUiuKLU0Yll68OopTjRCdhcA8MIkmM1VoxTPpzmyQyxaroZRoEFmoPQoiA9Q4Z05yFx56_ys4Yw8ebMbTHw_b3w11sXWQaB9z5ZQSMkq8oOhlW7pHDCOdgAwNm2nDpmQMMZCQ8MWeF5K6zvBpBw8pmE3dLu8O46aXQ4flUcIB_CFn1gLnG-Imj22JPuEzbs7pbt6xvcXnh0FKPINVVRvv6QJN6sf1XX4QJygpWTV16ywaECNmhR2vspeGsA6Swh5mmTb5S_ezgeOmAs98lQ7wX2c87EnoeDHirf_35GWGScqnUrJCszB4vOsrp4pYaWobX4xWLmu22kdQkVAP5VD3h8Lo7W7ZRGabFVNcql8k2WdDP_GNAFawYpGKh-i1mhkeGxmYLScQBU-7H2HYdThinNpqbfm4EzbhnUvbVdNOJlcbvFjbaVBjn-PxPizWhgIJa194e5CuFt6txvij3yfnLb7dpM-LkFDEu035jxg8ni0V5wvYqsOWq0RDL4SJ8ICWvY-ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
⁉️
بهترین گل‌تاریخ فوتبال از نگاه امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103158" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103157">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soJHhPWLvFhLnP9-y9ZCZFLK34McEjaXd2kFoVwsauVt5sn83FmlWdnl4iyUHN5DDRLWoP0rucH93cuKOy5AdziVT_G523rTtUtwyvYjTzCc67wLvDcC61Sq-wAEZ8IwoNIt6YBuBRUXOhtUvFhej3l9mLBncVmZS1lFsB3WhKJafheOcg51qF04en91VpS476Pli8_nIuMBv1B9GvhTYHoBQS8YDHYv_KJJA9lF8kI1WvzmSD0trt9JRbICu1OxcrHawYrxCiHx5tkZK5POoPdaFV4IPptyoI15_3TxdnxennR2Fb80s_X1IAILCkofaGkv_b-Obq-18uXuM7K0Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گستون ایدول (خبرنگار آرژانتینی) :
✅
علاقه بارسلونا به جولیان آلوارز همچنان ادامه داره.
❌
آلوارز تمایلی به ادامه حضور در اتلتیکو نداره و احتمالاً دوشنبه با سیمیونه صحبت خواهد کرد.
💸
بارسلونا آماده‌ست تا پیشنهاد خودش رو تا ۱۲۰ میلیون یورو بالا ببره.
⚠️
هنوز معتقدم شانس خوبی وجود داره که او در بارسلونا بازی کنه
📌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103157" target="_blank">📅 13:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103156">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=FRXjMbip07RcRlEOdPp4fRZecOLXYuqpM7gvI5nv6ETvIlvcKQVQZoWzYkvVntaCWCjgs4rRcIxg4WzF3o7xLyqdOxaMshL2AlMVKwhKuRpWvl_Iu-faxlBfQ358lh9cXjDGTUVwMtaJ8mTI4WqhaurSsM7csMeSABmtZtSXnW-ozVufmm6zF_NufJY5bqm509Jgi0ur1K_p7saTUjPq6u5fPdC2sIe1shd2IwLWQyzrIHG5_-j35n_FjWo9kN4RNC8i2ZB5vYMUF2shAPksVf-EtIlCf_lZaWWTatc_3iloW2Ur4_ssOwdZ4qEvodE6gxHTJBQkgo4c5mmTYNoRRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b2c9a3f73.mp4?token=FRXjMbip07RcRlEOdPp4fRZecOLXYuqpM7gvI5nv6ETvIlvcKQVQZoWzYkvVntaCWCjgs4rRcIxg4WzF3o7xLyqdOxaMshL2AlMVKwhKuRpWvl_Iu-faxlBfQ358lh9cXjDGTUVwMtaJ8mTI4WqhaurSsM7csMeSABmtZtSXnW-ozVufmm6zF_NufJY5bqm509Jgi0ur1K_p7saTUjPq6u5fPdC2sIe1shd2IwLWQyzrIHG5_-j35n_FjWo9kN4RNC8i2ZB5vYMUF2shAPksVf-EtIlCf_lZaWWTatc_3iloW2Ur4_ssOwdZ4qEvodE6gxHTJBQkgo4c5mmTYNoRRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تخریب یکی از ورزشگاه‌های اوکراین پس از حملات اخیر کشور روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103156" target="_blank">📅 13:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103155">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOLzn4qKqJ_CSAncir1gBBZ_iSb5sdy-26ztmh6Za6Q-HY55AlOZJ_F_7FOTPYsM5o6ZuA_yHg0l8yxuxdDp8Q3OT_qRY4niqf-pXQkDtzEEzNk88mVF8H80ZujFIs7Zmefh06WqB9zr7YHAzqENDkYVaVsljoV_leIsari8rjl8-BP8tVNtAAQcu9_GmeYShrgiLViXAhjFt-yGXozoFOLZkpG5UsCdFkYV3PpsJcRtoEtRa_JLmadmF9xBMuNaPrivHHvzMh1kiqQzj1dqI55Qcqi0ughPX3u78a7AoRMuskJzZveuWQo-qfGCPhBMjK-nCZheOK0N5N8SM4Lgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنیل‌مالدینی با عقد قراردادی به کالیاری پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103155" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103154">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3sKr1Y1LtPj6qI4-wYgJoQ_8SMzmEYjuJYbc3LYOaJRbbM87V-o8xOT2NTfs21FgEjddwmO51GTUuxD20z41PZn7NXxQlOQMQznI1Jm6k9h3pva4dgBo14JMLUbquHqB9_tPbRUJ5WjErpH4tVm00oB-4VpixcI-iimDWhE8is3KLwjWEqsacRS4ywqUzmZnJJQguS12KKgwqo_y05yNlgOOYvQpCB8zsrXZt8lO7hr264XqJCI-1qd8a7szCy7TLTtvyyvPolvTXo2AYD9ls5esKRjM3Rg-tS7y6DqnQUT4CkuzLNA8-4dJVcWIyq8xLLV3dUjbt-zKDOAsIlxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤯
🤯
😳
😳
ایران مهد عجایب! یه مرد در طول روز، زیادی به خانمش دستور میداده که براش چای بیاره!
بعد از یه مدت، زنش توی دوران پریودی میزنه به سیم آخر و وقتی مرده میخوابه، قوری رو میکنه توی
کونش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103154" target="_blank">📅 12:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103153">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riiGiY_PpoMrjNGIQ0LYUoyEaLa0-__QsUWQN73zRpfRAETCmWaqUIl4a7nidfmWzU_RD_8BxZChtIIXM3zvXcEQf0ulfk1GffrfOBjasnBxqD5wry8VAkb6m0xhBJS_25QnLWmlGOxn03vQVLiGlD499Tn82EW-7reM4_Cm-fEQ1qngaOS9q4yQj8d-K-yYQqKdXXP4Uu8J7G_nbeGtbWNLSW9WL4Hg6IHplnQJXefYkzIxQW9PSziGuvNYlK9cB6nwRdB9zwBt5LS29lpKHNjIblsugIisApUCFLTSwwvfYTBaHo9JHTuWOYyTtIJ02jdt6WbOY8U9lqFQ6yDRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
روزنامه موندو دپورتیوو:
❌
🔻
اظهارات سیمئونه استراتژی بارسلونا را تغییر نمیده. هفته آینده برای مشخص شدن سرنوشت انتقال خولیان آلوارز تعیین‌کننده خواهد بود. اگر خولیان نتواند وضعیتش را حل کند، بارسلونا سراغ پلن B خواهد رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103153" target="_blank">📅 12:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103152">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FchCKfoA8YqGb1rnaEtc1kkiPltCYaj3C9QIKYdV65K1wbLtEGB5dsrca9sEwcRNu45hMJjwWf7l0PZp8vF5H9_tImwzM4qbH77X_ttq1v_wvbdUb22WuXUV8--PIUpW7T71CqOkbS5JNTEIKi1vZ9xTH0FlXD7iJcCyHzDpIxUyJRGc3i29g0UeAtuAHeLtw9QXfC8uLvaIVznzjrOoBjh2ZmscOOO03z7ubjhse1tG9jafv8JqpZGr9N662-95adGprr7x36y8ZYDBGFg_AlEgY3EIKcMAwS-Umn_0k6yBj7zDo4J5P3RO5MKb73Gg1DsAFZFYfjgsKJi0ou28JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
خنده‌های حجت‌کریمی و جواد‌نکونام بعد کودتا علیه محمد ربیعی در تبریز
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103152" target="_blank">📅 12:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103151">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjNHTD9FNfHd0KNQgloR73lfpZAm1XklL8eyxuKpGsVWLBDNuqgYMQRQp9EgKMe8PR3vNlWQpOAwxCAfuyBgIuHOSOqP5hECQWLUWCuhdFXjmIlNLAdDkdKo6jQODJld1Kjy8jheJG6PMzRMQVHR83t1T1HLWuRxOYm5puhi4UpT3EjfLKC18-dWDwsGOqzZIvN09VdbAaSQ0jKjj_0WgJWWXqIw7PpTggEmaz1qgCFUcy_tSoKmtNACSl8f3tn_RD-lDLTeILiW2OjiRIewdEFXLTYrVfZzFgGlD6ywRWClSgU2QxZNF46Dl-U7pMXkppCF1qGO3YcbnMSqlaNNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۲ سال از بازی منچستریونایتد و رئال‌مادرید در آمریکا و حضور ۱۰۹.۳۱۸ نفری گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103151" target="_blank">📅 12:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103150">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/103150" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103150" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103149">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFmMtBqmdNdKvfeIvC_TBhtzfpphmjXa5G_3Nsa4MH2jo2_ff3pKjkRGmAgfjuPYF6ZzfSsIXJP_KzKgTGfVpNaVRntMVgbwRcHzT-mBZkIbSzoinf7h98MvEIP-Y1xGOEOOoojKls01JA-DsqPyuf8YexcFGxqAMRywzGaR-bY8gg0esuZhVwyvOc5u0lsR4iea5Alt6QIqueFYu3qWi9EDWhr3RG0UOYCAR9VDliFJXsETFXq5ObwCCWA_cL5q5ifcJUfijSsdKMU15Uq9YwB_Y5UmdACvLbwmEEYw0j7qxos2P5eL4oWRsAsPOPnYyi_2ktaQkQ64bFAmonWzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103149" target="_blank">📅 12:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103148">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یکی از جذاب‌ترین دربی‌های سالیان اخیر منچستر و تقابل پپ‌گواردیولا و‌ مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103148" target="_blank">📅 11:55 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103147">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW8lsq-nOYhrLn3b2kGuWfNwFBNuhQGSOnIewjeZIoBKmDjELU4HC245sgsrXjT31DnDTdF4nkKJfVLmaaheoEj27zFz-4UG_gG9wDqzXtVH6WPdWy-SyB06bIG8Iu8zayP4dBVtTzZva4chovwWabYQO_so_NBOfIuqa-TcymwMp_9te2c7n3lJqfythugyqQHQfiBXEeX7CIMq8dBLKgrYWGsBbu_P81PKwAR2E8zf5g5Czym9RudX9zsVrVvqLYY5g8U2e8qhkqEAKbQdRionlJ2l82eL3y8uoA_08gtowo2AZaw6Fmgm7P_zHl4eTxs7dooUN3kIfo9NMA2Y3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
فده والورده:
من انتظار نداشتم مورینیو این‌طور باشه. او خیلی به ما نزدیکه. گاهی اوقات سخت‌‌گیره، اما فکر میکنم همین میتونه باعث پیشرفت ما بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103147" target="_blank">📅 11:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103146">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=JCCLwNLerTUVwX9rahhHLpm-vVQiFgP-urXr8R5MTPdoMTaDdl7DcScSiYkiecOkr3c4MrniVAtKNKda4JfjMKprDOxNGSSHGCUBTkR0nkVKEtXN7i1hX7YzV5YptfDsWMNeVWW-TlLc93CGgyLz4CHlNfLc6TViM1MqgfLMaWqcjBtXUaE7l_YeMwnXjhGs_mqA5yKE1uE3oNo5SqgCT6pwGA4g3z_MHpkS-y-r0FHqyqeiiFs07WXCFmMOthUxOpZ9my_axZlIEHX5qbxo6heEMdW4RFfpV8NS67RVYjgFUbETqByMTpzM2D-C6J-I_HcJqIZBeZFWZ9Y6-nHAZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c18fc924.mp4?token=JCCLwNLerTUVwX9rahhHLpm-vVQiFgP-urXr8R5MTPdoMTaDdl7DcScSiYkiecOkr3c4MrniVAtKNKda4JfjMKprDOxNGSSHGCUBTkR0nkVKEtXN7i1hX7YzV5YptfDsWMNeVWW-TlLc93CGgyLz4CHlNfLc6TViM1MqgfLMaWqcjBtXUaE7l_YeMwnXjhGs_mqA5yKE1uE3oNo5SqgCT6pwGA4g3z_MHpkS-y-r0FHqyqeiiFs07WXCFmMOthUxOpZ9my_axZlIEHX5qbxo6heEMdW4RFfpV8NS67RVYjgFUbETqByMTpzM2D-C6J-I_HcJqIZBeZFWZ9Y6-nHAZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اَبَر قهرمانی وفادار به عشقش فوتبال
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103146" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103145">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=sFatZT6MAmAOkZEzz92S0wVGFIjc8E2urvezhyteztJC1KGlj9nZ2tDI3e2oPEwLNrUWMhavKRA_xSos2YeFpyGam72WW0WmqWSd1jg6Xr58bep7JJBqjJb4P-jz078rbO88spmrYB7xuGDcHOPLX6-k7iUsEt9KfVVqiRJTuVFY_P0GhCqP8C3dPuE1ksxPAimF7_bGBMzNIOxLMIdG_T2SMgpxiW-8Dp13-qu78k9wYeaSonTWwRdPQ18NrewjKBC8YMQfp6gt__siBlj6NatpxMzH27le6ssbfxzkHxJwOo7k2l9Mk3ulRz9WNJyOQHt4L_erkGu0N7xxUjbNyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bfa87a9.mp4?token=sFatZT6MAmAOkZEzz92S0wVGFIjc8E2urvezhyteztJC1KGlj9nZ2tDI3e2oPEwLNrUWMhavKRA_xSos2YeFpyGam72WW0WmqWSd1jg6Xr58bep7JJBqjJb4P-jz078rbO88spmrYB7xuGDcHOPLX6-k7iUsEt9KfVVqiRJTuVFY_P0GhCqP8C3dPuE1ksxPAimF7_bGBMzNIOxLMIdG_T2SMgpxiW-8Dp13-qu78k9wYeaSonTWwRdPQ18NrewjKBC8YMQfp6gt__siBlj6NatpxMzH27le6ssbfxzkHxJwOo7k2l9Mk3ulRz9WNJyOQHt4L_erkGu0N7xxUjbNyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
والیبالیست های بانو رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103145" target="_blank">📅 11:05 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
